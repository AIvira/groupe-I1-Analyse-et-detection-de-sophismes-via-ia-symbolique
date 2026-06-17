"""Tests de la couche symbolique (TweetyProject / Dung via JPype).

Necessite le JAR Tweety dans lib/ et un JVM ; ces tests sont ignores si JPype
ou le JAR sont absents.
"""

import pytest

jpype = pytest.importorskip("jpype")

from src.symbolic.dung import DungAF, arbitrate, symbolic_verdict  # noqa: E402

# Le JVM ne peut etre demarre qu'une fois par processus ; on saute proprement
# s'il n'y a pas de JAR.
try:
    DungAF()
    _SYMBOLIC_OK = True
except Exception:  # pragma: no cover - depend de l'environnement
    _SYMBOLIC_OK = False

pytestmark = pytest.mark.skipif(not _SYMBOLIC_OK, reason="JAR TweetyProject indisponible")


def test_grounded_reinstatement_chain():
    # a -> b -> c : l'extension fondee est {a, c} (c reinstaure par a)
    af = DungAF().add_attack("a", "b").add_attack("b", "c")
    assert af.grounded_extension() == {"a", "c"}


def test_odd_cycle_has_empty_grounded_and_no_stable():
    af = DungAF().add_attack("a", "b").add_attack("b", "c").add_attack("c", "a")
    assert af.grounded_extension() == set()
    assert af.extensions("stable") == []


def test_even_cycle_has_two_preferred_extensions():
    af = DungAF().add_attack("a", "b").add_attack("b", "a")
    preferred = af.extensions("preferred")
    assert {"a"} in preferred and {"b"} in preferred


def test_scheme_verdict_unanswered_is_fallacious():
    verdict = symbolic_verdict("false_dilemma")
    assert verdict.status == "fallacieux"
    assert verdict.claim_accepted is False
    assert "CLAIM" not in verdict.grounded_extension


def test_scheme_verdict_answered_reinstates_claim():
    verdict = symbolic_verdict("false_dilemma", critical_question_answered=True)
    assert verdict.status == "valide"
    assert verdict.claim_accepted is True
    assert "CLAIM" in verdict.grounded_extension


def test_arbitration_explicit_rule_overrides_ml():
    result = arbitrate(
        ml_label="straw_man", ml_confidence=0.6,
        rule_label="false_dilemma", rule_confidence=0.95,
    )
    assert result["final_label"] == "false_dilemma"
    assert result["winner"] == "RULE"
    assert result["disagreement"] is True


def test_arbitration_weak_rule_yields_to_ml():
    result = arbitrate(
        ml_label="ad_hominem", ml_confidence=0.8,
        rule_label="straw_man", rule_confidence=0.6,
    )
    assert result["final_label"] == "ad_hominem"
    assert result["winner"] == "ML"


def test_arbitration_no_detector_returns_not_fallacy():
    result = arbitrate(
        ml_label="other_fallacy", ml_confidence=0.9,
        rule_label=None, rule_confidence=0.0,
    )
    assert result["final_label"] == "not_fallacy"
    assert result["winner"] == "DEFAULT_NONE"
