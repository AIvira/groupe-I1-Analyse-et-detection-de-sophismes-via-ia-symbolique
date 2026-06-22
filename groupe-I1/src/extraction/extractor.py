"""Extraction de la structure argumentative depuis un texte brut.

Conformement au sujet I1, un LLM realise l'extraction initiale des segments
argumentatifs (premisses, conclusions, relations d'attaque/support, types de
sophismes). Cette etape alimente la couche symbolique (projection en AF de
Dung). On fournit :

- `LLMArgumentExtractor` : extraction via un LLM (SDK openai), sortie structuree
  (JSON valide via `chat.completions.parse` + schema Pydantic). Le backend est
  OpenAI distant si `OPENAI_API_KEY` est defini, sinon Ollama local (`llama3.2`)
  — voir `src.llm_backend`.
- `HeuristicArgumentExtractor` : repli deterministe hors-ligne base sur les
  marqueurs de discours (« because », « therefore », « but »...) + les regles
  lexicales de sophismes. Permet de faire tourner et tester tout le pipeline
  sans LLM (et sert aussi de repli si l'appel LLM echoue).

`get_extractor()` choisit le LLM si un backend est disponible, sinon le repli.
"""

from __future__ import annotations

import re
import sys
from typing import List, Optional

from src.extraction.argmodel import ArgRelation, ArgUnit, ArgumentMap

# Marqueurs de discours pour le repli heuristique.
_CONCLUSION_MARKERS = re.compile(
    r"\b(therefore|thus|hence|so|consequently|donc|ainsi|par consequent)\b", re.I
)
_PREMISE_MARKERS = re.compile(r"\b(because|since|as|for|car|parce que|puisque)\b", re.I)
_ATTACK_MARKERS = re.compile(r"\b(but|however|yet|although|though|mais|cependant|pourtant)\b", re.I)


# ---------------------------------------------------------------------------
# Repli heuristique (hors-ligne, deterministe, testable)
# ---------------------------------------------------------------------------

class HeuristicArgumentExtractor:
    """Extraction par marqueurs de discours + regles de sophismes."""

    def __init__(self) -> None:
        from src.rules.detector import RuleBasedFallacyDetector

        self._detector = RuleBasedFallacyDetector()

    @staticmethod
    def _split_clauses(text: str) -> List[str]:
        # decoupe sur la ponctuation forte et les marqueurs de discours
        parts = re.split(r"(?<=[.!?;])\s+", text.strip())
        clauses: List[str] = []
        for part in parts:
            sub = re.split(r"\b(?:but|however|yet|because|since|therefore|so|thus|mais|car|donc)\b",
                           part, flags=re.I)
            clauses.extend(c.strip(" ,.;:") for c in sub if c.strip())
        return [c for c in clauses if c]

    def extract(self, text: str) -> ArgumentMap:
        amap = ArgumentMap(meta={"extractor": "heuristic", "raw_text": text})
        clauses = self._split_clauses(text)
        if not clauses:
            clauses = [text.strip()]

        # Heuristique de role : une clause suivie/precedee d'un marqueur de
        # conclusion est la conclusion ; les autres sont des premisses.
        conclusion_idx = 0
        for i, clause in enumerate(clauses):
            # la clause apres un marqueur de conclusion est souvent la these
            if _CONCLUSION_MARKERS.search(text) and i == len(clauses) - 1:
                conclusion_idx = i

        for i, clause in enumerate(clauses):
            role = "conclusion" if i == conclusion_idx else "premise"
            if len(clauses) == 1:
                role = "claim"
            amap.add_unit(ArgUnit(id=f"u{i}", text=clause, role=role))

        # la derniere clause est adversative si un marqueur d'attaque est present
        adversative_idx = (
            len(clauses) - 1 if (_ATTACK_MARKERS.search(text) and len(clauses) >= 2) else None
        )

        # supports : chaque premisse (non adversative) soutient la conclusion
        for i in range(len(clauses)):
            if i != conclusion_idx and i != adversative_idx and len(clauses) > 1:
                amap.add_relation(ArgRelation(source=f"u{i}", target=f"u{conclusion_idx}", kind="support"))

        # attaque interne : la clause adversative attaque la conclusion
        if adversative_idx is not None:
            amap.add_relation(
                ArgRelation(source=f"u{adversative_idx}", target=f"u{conclusion_idx}", kind="attack")
            )

        # sophismes : on tague l'unite (ou la conclusion) avec le label des regles
        pred = self._detector.predict(text)
        if pred.label != "not_fallacy":
            target = f"u{conclusion_idx}" if f"u{conclusion_idx}" in amap.units else next(iter(amap.units))
            amap.tag_fallacy(target, pred.label)
        return amap


# ---------------------------------------------------------------------------
# Extraction LLM (OpenAI / SDK openai)
# ---------------------------------------------------------------------------

_SYSTEM_PROMPT = (
    "You are an argument-mining expert. Given an argumentative text, extract its "
    "structure: argumentative units (premises and conclusions), and the relations "
    "between them (support or attack). Also flag any logical fallacy you detect on "
    "the relevant unit, using labels from this set: ad_hominem, ad_populum, "
    "appeal_to_emotion, circular_reasoning, equivocation, fallacy_of_credibility, "
    "fallacy_of_logic, fallacy_of_relevance, false_causality, false_dilemma, "
    "faulty_generalization, intentional, straw_man. Use stable short unit ids like "
    "u0, u1. Only include attack/support relations you can justify from the text."
)


def _build_schema():
    from pydantic import BaseModel
    from typing import List as _List, Literal

    class _Unit(BaseModel):
        id: str
        text: str
        role: Literal["premise", "conclusion", "claim"]

    class _Relation(BaseModel):
        source: str
        target: str
        kind: Literal["attack", "support"]

    class _Fallacy(BaseModel):
        unit_id: str
        label: str

    class ExtractedArgMap(BaseModel):
        units: _List[_Unit]
        relations: _List[_Relation]
        fallacies: _List[_Fallacy]

    return ExtractedArgMap


class LLMArgumentExtractor:
    """Extraction via OpenAI avec sortie structuree (JSON valide)."""

    def __init__(self, model: Optional[str] = None, max_tokens: int = 2048) -> None:
        from src.llm_backend import default_model, make_client

        self._client = make_client()  # OpenAI distant ou Ollama local selon l'env
        self._model = model or default_model()
        self._max_tokens = max_tokens
        self._schema = _build_schema()
        self._fallback: Optional[HeuristicArgumentExtractor] = None

    def extract(self, text: str) -> ArgumentMap:
        try:
            response = self._client.chat.completions.parse(
                model=self._model,
                max_completion_tokens=self._max_tokens,
                messages=[
                    {"role": "system", "content": _SYSTEM_PROMPT},
                    {"role": "user", "content": text},
                ],
                response_format=self._schema,
            )
        except Exception as exc:  # quota, reseau, auth... -> repli heuristique
            print(
                f"[extraction] appel OpenAI echoue ({type(exc).__name__}: {exc}); "
                "repli sur l'extracteur heuristique.",
                file=sys.stderr,
            )
            if self._fallback is None:
                self._fallback = HeuristicArgumentExtractor()
            return self._fallback.extract(text)
        parsed = response.choices[0].message.parsed
        amap = ArgumentMap(meta={"extractor": "llm", "model": self._model, "raw_text": text})
        for u in parsed.units:
            amap.add_unit(ArgUnit(id=u.id, text=u.text, role=u.role))
        for r in parsed.relations:
            if r.source in amap.units and r.target in amap.units:
                amap.add_relation(ArgRelation(source=r.source, target=r.target, kind=r.kind))
        for f in parsed.fallacies:
            if f.unit_id in amap.units:
                amap.tag_fallacy(f.unit_id, f.label)
        return amap


def llm_available() -> bool:
    from src.llm_backend import llm_available as _available

    return _available()


def get_extractor(prefer_llm: bool = True):
    """Renvoie l'extracteur LLM si possible, sinon le repli heuristique."""
    if prefer_llm and llm_available():
        try:
            return LLMArgumentExtractor()
        except Exception:  # pragma: no cover - depend de l'env
            pass
    return HeuristicArgumentExtractor()
