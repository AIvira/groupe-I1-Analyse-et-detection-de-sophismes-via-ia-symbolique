"""Classifieur de sophismes par LLM (Claude) — la "version 2".

But pedagogique pour la soutenance : comparer une approche **LLM zero/few-shot**
(Claude) a nos classifieurs **statistiques** (TF-IDF, transformer fine-tune) sur
exactement le meme split de test. Le LLM gere la variabilite linguistique et les
classes semantiquement diffuses (ex. `intentional`) la ou un sac-de-mots echoue.

Sortie structuree (un label parmi les 13) via `messages.parse` + schema. Le
prompt systeme (definitions des labels) est mis en cache pour reduire le cout
sur tout le jeu de test. Le client Anthropic est injectable pour les tests.
"""

from __future__ import annotations

import os
from typing import Dict, List, Optional, Tuple

# Les 13 labels de la taxonomie `full` + definition concise (sert de prompt).
FALLACY_DEFINITIONS: Dict[str, str] = {
    "ad_hominem": "attacking the person making the argument rather than the argument itself",
    "ad_populum": "appeal to popularity: claiming something is true because many people believe it",
    "appeal_to_emotion": "manipulating emotions (fear, pity, pride) in place of valid reasoning",
    "circular_reasoning": "the conclusion is assumed in the premises (begging the question)",
    "equivocation": "a key term shifts meaning between premises, making the argument seem valid",
    "fallacy_of_credibility": "appeal to an illegitimate, biased, or irrelevant authority",
    "fallacy_of_logic": "an invalid inference or formal reasoning error",
    "fallacy_of_relevance": "premises that are logically irrelevant to the conclusion (red herring)",
    "false_causality": "inferring a causal link from mere correlation or temporal succession",
    "false_dilemma": "presenting only two options when more exist",
    "faulty_generalization": "a hasty generalization from a small or unrepresentative sample",
    "intentional": "a deliberate or deceptive use of a fallacy; a catch-all for tricks like loaded questions",
    "straw_man": "misrepresenting or exaggerating an opponent's position to refute it more easily",
}

LABELS: List[str] = list(FALLACY_DEFINITIONS)
DEFAULT_MODEL = "claude-opus-4-8"


def _system_prompt() -> str:
    lines = [
        "You are an expert in informal logic. Classify the argumentative text into "
        "exactly ONE logical fallacy type from the list below. Choose the single best "
        "fit even if several seem plausible. Definitions:",
        "",
    ]
    for label, definition in FALLACY_DEFINITIONS.items():
        lines.append(f"- {label}: {definition}")
    return "\n".join(lines)


def _build_schema():
    from pydantic import BaseModel
    from typing import Literal

    # Literal sur les 13 labels => le LLM ne peut renvoyer qu'un label valide.
    class FallacyPrediction(BaseModel):
        label: Literal[tuple(LABELS)]  # type: ignore[valid-type]
        rationale: str

    return FallacyPrediction


class LLMFallacyClassifier:
    """Classement zero-shot des sophismes par Claude (sortie structuree)."""

    def __init__(
        self,
        model: Optional[str] = None,
        client=None,
        max_tokens: int = 512,
        cache_system: bool = True,
    ) -> None:
        if client is None:
            import anthropic

            client = anthropic.Anthropic()  # lit ANTHROPIC_API_KEY
        self._client = client
        self._model = model or os.environ.get("ANTHROPIC_MODEL", DEFAULT_MODEL)
        self._max_tokens = max_tokens
        self._schema = _build_schema()
        if cache_system:
            self._system = [
                {"type": "text", "text": _system_prompt(), "cache_control": {"type": "ephemeral"}}
            ]
        else:
            self._system = _system_prompt()

    def classify(self, text: str) -> Tuple[str, str]:
        """Renvoie (label, justification) pour un texte."""
        response = self._client.messages.parse(
            model=self._model,
            max_tokens=self._max_tokens,
            system=self._system,
            messages=[{"role": "user", "content": text}],
            output_format=self._schema,
        )
        parsed = response.parsed_output
        return parsed.label, parsed.rationale

    def classify_many(self, texts: List[str], on_progress=None) -> List[str]:
        labels: List[str] = []
        for i, text in enumerate(texts):
            try:
                label, _ = self.classify(text)
            except Exception:  # pragma: no cover - robustesse reseau
                label = "intentional"  # repli neutre
            labels.append(label)
            if on_progress is not None:
                on_progress(i + 1, len(texts))
        return labels


def llm_available() -> bool:
    import importlib.util

    return bool(os.environ.get("ANTHROPIC_API_KEY")) and (
        importlib.util.find_spec("anthropic") is not None
    )
