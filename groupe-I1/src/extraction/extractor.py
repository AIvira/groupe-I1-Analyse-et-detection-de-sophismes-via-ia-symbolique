"""Extraction de la structure argumentative depuis un texte brut.

Conformement au sujet I1, un LLM realise l'extraction initiale des segments
argumentatifs (premisses, conclusions, relations d'attaque/support, types de
sophismes). Cette etape alimente la couche symbolique (projection en AF de
Dung). On fournit :

- `LLMArgumentExtractor` : extraction via Claude (SDK Anthropic), sortie
  structuree (JSON valide via `messages.parse` + schema Pydantic).
- `HeuristicArgumentExtractor` : repli deterministe hors-ligne base sur les
  marqueurs de discours (« because », « therefore », « but »...) + les regles
  lexicales de sophismes. Permet de faire tourner et tester tout le pipeline
  sans cle API.

`get_extractor()` choisit le LLM si une cle API est disponible, sinon le repli.
"""

from __future__ import annotations

import os
import re
from typing import List, Optional

from src.extraction.argmodel import ArgRelation, ArgUnit, ArgumentMap

# Modele Claude par defaut (surchargeable via ANTHROPIC_MODEL).
DEFAULT_MODEL = "claude-opus-4-8"

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
# Extraction LLM (Claude / SDK Anthropic)
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
    """Extraction via Claude avec sortie structuree (JSON valide)."""

    def __init__(self, model: Optional[str] = None, max_tokens: int = 2048) -> None:
        import anthropic  # import paresseux

        self._client = anthropic.Anthropic()  # lit ANTHROPIC_API_KEY de l'env
        self._model = model or os.environ.get("ANTHROPIC_MODEL", DEFAULT_MODEL)
        self._max_tokens = max_tokens
        self._schema = _build_schema()

    def extract(self, text: str) -> ArgumentMap:
        response = self._client.messages.parse(
            model=self._model,
            max_tokens=self._max_tokens,
            system=_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": text}],
            output_format=self._schema,
        )
        parsed = response.parsed_output
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
    import importlib.util

    return bool(os.environ.get("ANTHROPIC_API_KEY")) and (
        importlib.util.find_spec("anthropic") is not None
    )


def get_extractor(prefer_llm: bool = True):
    """Renvoie l'extracteur LLM si possible, sinon le repli heuristique."""
    if prefer_llm and llm_available():
        try:
            return LLMArgumentExtractor()
        except Exception:  # pragma: no cover - depend de l'env
            pass
    return HeuristicArgumentExtractor()
