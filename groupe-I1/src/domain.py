from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass(slots=True)
class RuleHit:
    label: str
    weight: float
    evidence: str


@dataclass(slots=True)
class Prediction:
    text: str
    label: str
    confidence: float
    mode: str
    evidence: List[str] = field(default_factory=list)
    scores: Dict[str, float] = field(default_factory=dict)


@dataclass(slots=True)
class TrainingConfig:
    text_column: str = "text"
    label_column: str = "label"
    word_max_features: int = 12000
    char_max_features: int = 8000
    masked_max_features: int = 4000
    context_max_features: int = 3000
    min_df: int = 2
    use_masked_text_features: bool = True
    use_context_features: bool = False
    drop_text_overlap_between_splits: bool = True
    test_size: float = 0.2
    random_state: int = 42
    min_rule_confidence: float = 0.55
    hybrid_rule_bonus: float = 0.15
    hybrid_ml_weight: float = 0.7
    hybrid_rule_weight: float = 0.3
