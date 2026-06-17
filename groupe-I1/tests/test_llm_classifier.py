"""Tests du classifieur LLM (version 2) avec un client Anthropic mocke.

Pas d'appel reseau : on injecte un faux client qui imite `messages.parse`.
Valide le schema (enum 13 labels) et le flux classify / classify_many.
"""

import pytest

pytest.importorskip("pydantic")

from src.classifiers.llm import LABELS, LLMFallacyClassifier, _build_schema


def test_schema_constrains_to_13_labels():
    schema = _build_schema()
    enum = schema.model_json_schema()["properties"]["label"]["enum"]
    assert set(enum) == set(LABELS)
    assert len(LABELS) == 13


class _Parsed:
    def __init__(self, label):
        self.label = label
        self.rationale = "test rationale"


class _Resp:
    def __init__(self, label):
        self.parsed_output = _Parsed(label)


class _MockMessages:
    def parse(self, **kwargs):
        text = kwargs["messages"][0]["content"].lower()
        label = "false_dilemma" if "either" in text else "ad_hominem"
        return _Resp(label)


class _MockClient:
    messages = _MockMessages()


def test_classify_returns_label_and_rationale():
    clf = LLMFallacyClassifier(client=_MockClient())
    label, rationale = clf.classify("Either you support this or you hate us")
    assert label == "false_dilemma"
    assert rationale


def test_classify_many_preserves_order():
    clf = LLMFallacyClassifier(client=_MockClient())
    labels = clf.classify_many(["Either A or B", "you are wrong"])
    assert labels == ["false_dilemma", "ad_hominem"]


def test_classify_many_robust_to_errors():
    class _Boom:
        class messages:
            @staticmethod
            def parse(**kwargs):
                raise RuntimeError("network down")

    clf = LLMFallacyClassifier(client=_Boom())
    # repli neutre 'intentional' au lieu de planter
    assert clf.classify_many(["x"]) == ["intentional"]
