from src.rules.detector import RuleBasedFallacyDetector


def test_detect_false_dilemma() -> None:
    detector = RuleBasedFallacyDetector()
    prediction = detector.predict("Either you support this reform or you hate the country.")
    assert prediction.label == "false_dilemma"


def test_detect_ad_hominem() -> None:
    detector = RuleBasedFallacyDetector()
    prediction = detector.predict("You are ignorant, so your argument is worthless.")
    assert prediction.label == "ad_hominem"
