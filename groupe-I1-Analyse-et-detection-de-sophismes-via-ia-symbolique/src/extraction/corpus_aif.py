"""Chargement de corpus d'argument mining au format AIF (US2016, AIFdb).

Le format AIF (Argument Interchange Format) modelise un debat annote comme un
graphe de noeuds typees :
  - I  : Information node = une proposition (un argument atomique)
  - RA : Rule of inference = une inference (premisses -> conclusion) => SUPPORT
  - CA : Conflict = un conflit entre propositions               => ATTAQUE
  - MA : rephrase, L : locution, YA/TA : ancrage illocutoire (ignores ici)

Les aretes relient I -> CA -> I (l'attaquant pointe vers le CA, le CA pointe
vers l'attaque) et premisses -> RA -> conclusion. On en derive une
`ArgumentMap` dont les attaques alimentent directement un AF de Dung.

C'est la realisation de l'objectif du sujet : evaluer la structure
argumentative sur un corpus annote (US2016) avec les frameworks de Dung.
"""

from __future__ import annotations

import json
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from src.extraction.argmodel import ArgRelation, ArgUnit, ArgumentMap

US2016_JSON_URL = "http://corpora.aifdb.org/US2016/json"


def aifdb_url(corpus_name: str) -> str:
    """URL JSON d'un corpus AIFdb a partir de son nom (ex. 'US2016', 'ArgMine')."""
    return f"http://corpora.aifdb.org/{corpus_name}/json"


def download_aif(url: str, dest: str, timeout: int = 60) -> str:
    path = Path(dest)
    path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=timeout) as resp:  # noqa: S310 (corpus public)
        data = resp.read()
    path.write_bytes(data)
    return str(path)


def load_aif(path_or_dict, only_conflict_graph: bool = True) -> ArgumentMap:
    """Parse un nodeset AIF (JSON) en `ArgumentMap`.

    Si `only_conflict_graph` est vrai, ne garde que les propositions (I-nodes)
    impliquees dans au moins une attaque (CA) ou un support (RA) — c'est le
    graphe argumentatif utile, bien plus petit que le corpus complet.
    """
    if isinstance(path_or_dict, (str, Path)):
        data = json.loads(Path(path_or_dict).read_text(encoding="utf-8"))
    else:
        data = path_or_dict

    nodes = {n["nodeID"]: n for n in data["nodes"]}
    incoming: Dict[str, List[str]] = defaultdict(list)   # node -> [from...]
    outgoing: Dict[str, List[str]] = defaultdict(list)   # node -> [to...]
    for e in data.get("edges", []):
        outgoing[e["fromID"]].append(e["toID"])
        incoming[e["toID"]].append(e["fromID"])

    amap = ArgumentMap(meta={"format": "AIF", "source": "AIFdb"})

    def is_inode(nid: str) -> bool:
        return nodes.get(nid, {}).get("type") == "I"

    used: set[str] = set()

    # CA (conflits) -> attaques
    for nid, node in nodes.items():
        if node.get("type") != "CA":
            continue
        attackers = [s for s in incoming.get(nid, []) if is_inode(s)]
        targets = [t for t in outgoing.get(nid, []) if is_inode(t)]
        for a in attackers:
            for t in targets:
                amap.add_relation(ArgRelation(source=a, target=t, kind="attack"))
                used.update((a, t))

    # RA (inferences) -> supports (premisses -> conclusion)
    for nid, node in nodes.items():
        if node.get("type") != "RA":
            continue
        premises = [s for s in incoming.get(nid, []) if is_inode(s)]
        conclusions = [t for t in outgoing.get(nid, []) if is_inode(t)]
        for p in premises:
            for c in conclusions:
                amap.add_relation(ArgRelation(source=p, target=c, kind="support"))
                used.update((p, c))

    # Unites : I-nodes (filtres au graphe utile si demande)
    for nid, node in nodes.items():
        if node.get("type") != "I":
            continue
        if only_conflict_graph and nid not in used:
            continue
        # role heuristique : cible d'un support = conclusion, source = premisse
        amap.add_unit(ArgUnit(id=nid, text=node.get("text", ""), role="claim"))

    # roles depuis les supports
    support_targets = {t for _, t in amap.supports()}
    support_sources = {s for s, _ in amap.supports()}
    for uid, unit in amap.units.items():
        if uid in support_targets:
            unit.role = "conclusion"
        elif uid in support_sources:
            unit.role = "premise"

    amap.meta["n_nodes_total"] = len(nodes)
    return amap


def attack_subgraph(amap: ArgumentMap) -> ArgumentMap:
    """Restreint la carte au sous-graphe des seules attaques (pour le AF de Dung)."""
    sub = ArgumentMap(meta=dict(amap.meta))
    attack_units: set[str] = set()
    for s, t in amap.attacks():
        attack_units.update((s, t))
    for uid in attack_units:
        if uid in amap.units:
            sub.add_unit(amap.units[uid])
    for r in amap.relations:
        if r.kind == "attack":
            sub.add_relation(r)
    return sub
