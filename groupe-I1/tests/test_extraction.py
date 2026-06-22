"""Tests de l'extraction d'arguments, du modele de carte et du parseur AIF."""

import pytest

from src.extraction.argmodel import ArgRelation, ArgUnit, ArgumentMap
from src.extraction.corpus_aif import attack_subgraph, load_aif
from src.extraction.extractor import HeuristicArgumentExtractor, get_extractor

jpype = pytest.importorskip("jpype")

try:
    from src.symbolic.dung import DungAF

    DungAF()
    _SYMBOLIC_OK = True
except Exception:  # pragma: no cover
    _SYMBOLIC_OK = False

needs_symbolic = pytest.mark.skipif(not _SYMBOLIC_OK, reason="JAR TweetyProject indisponible")


def test_heuristic_extractor_finds_units_and_fallacy():
    ext = HeuristicArgumentExtractor()
    amap = ext.extract("We must ban it because everyone knows it is bad, but they deny it.")
    assert len(amap.units) >= 2
    assert any(u.role == "conclusion" for u in amap.units.values())
    # marqueur "everyone knows" -> ad_populum
    assert "ad_populum" in amap.fallacies.values()
    # marqueur adversatif "but" -> au moins une attaque
    assert len(amap.attacks()) >= 1


def test_get_extractor_falls_back_to_heuristic_without_backend(monkeypatch):
    # Aucun backend LLM : ni cle OpenAI, ni serveur local joignable.
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_BASE_URL", raising=False)
    monkeypatch.delenv("LLM_BASE_URL", raising=False)
    monkeypatch.setattr("src.llm_backend._server_reachable", lambda *a, **k: False)
    assert isinstance(get_extractor(), HeuristicArgumentExtractor)


@needs_symbolic
def test_argmap_coherence_rejects_attacked_conclusion():
    amap = ArgumentMap()
    amap.add_unit(ArgUnit("c", "claim", "conclusion"))
    amap.add_unit(ArgUnit("o", "objection", "premise"))
    amap.add_relation(ArgRelation("o", "c", "attack"))
    coh = amap.coherence("grounded")
    assert "o" in coh["accepted"]
    assert "c" in coh["rejected"]


# Fixture AIF synthetique (pas de reseau) : a -CA-> b, p -RA-> b
_AIF = {
    "nodes": [
        {"nodeID": "1", "text": "A is true", "type": "I"},
        {"nodeID": "2", "text": "B is true", "type": "I"},
        {"nodeID": "3", "text": "P supports B", "type": "I"},
        {"nodeID": "10", "text": "Default Conflict", "type": "CA"},
        {"nodeID": "11", "text": "Default Inference", "type": "RA"},
        {"nodeID": "99", "text": "speaker said", "type": "L"},
    ],
    "edges": [
        {"fromID": "1", "toID": "10"},   # A -> CA
        {"fromID": "10", "toID": "2"},   # CA -> B  (A attaque B)
        {"fromID": "3", "toID": "11"},   # P -> RA
        {"fromID": "11", "toID": "2"},   # RA -> B  (P soutient B)
    ],
}


def test_load_aif_maps_conflicts_to_attacks_and_inferences_to_supports():
    amap = load_aif(_AIF)
    assert ("1", "2") in amap.attacks()      # CA -> attaque
    assert ("3", "2") in amap.supports()     # RA -> support
    # B est conclusion (cible d'un support), P premisse
    assert amap.units["2"].role == "conclusion"
    assert amap.units["3"].role == "premise"
    # la locution L n'est pas une unite
    assert "99" not in amap.units


@needs_symbolic
def test_aif_attack_subgraph_grounded_rejects_attacked_node():
    amap = load_aif(_AIF)
    sub = attack_subgraph(amap)
    coh = sub.coherence("grounded")
    assert "1" in coh["accepted"]   # A non attaque -> accepte
    assert "2" in coh["rejected"]   # B attaque par A -> rejete
