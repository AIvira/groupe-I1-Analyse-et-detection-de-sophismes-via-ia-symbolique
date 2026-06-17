"""Modele de structure argumentative + projection vers un AF de Dung.

C'est le pont entre l'extraction (LLM ou corpus annote) et la couche
symbolique. Un texte / un document est represente comme une *carte
argumentative* : des unites (premisses, conclusions) reliees par des relations
d'attaque et de support. On projette ensuite cette carte dans un framework
d'argumentation abstraite de Dung (via TweetyProject) pour calculer
l'acceptabilite des arguments.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class ArgUnit:
    id: str
    text: str
    role: str = "claim"          # premise | conclusion | claim

    def to_dict(self) -> dict:
        return {"id": self.id, "text": self.text, "role": self.role}


@dataclass
class ArgRelation:
    source: str                  # id de l'unite source
    target: str                  # id de l'unite cible
    kind: str = "attack"         # attack | support | rephrase

    def to_dict(self) -> dict:
        return {"source": self.source, "target": self.target, "kind": self.kind}


@dataclass
class ArgumentMap:
    """Carte argumentative : unites + relations + sophismes detectes."""

    units: Dict[str, ArgUnit] = field(default_factory=dict)
    relations: List[ArgRelation] = field(default_factory=list)
    fallacies: Dict[str, str] = field(default_factory=dict)   # unit_id -> label
    meta: dict = field(default_factory=dict)

    # -- construction -------------------------------------------------------
    def add_unit(self, unit: ArgUnit) -> "ArgumentMap":
        self.units[unit.id] = unit
        return self

    def add_relation(self, relation: ArgRelation) -> "ArgumentMap":
        self.relations.append(relation)
        return self

    def tag_fallacy(self, unit_id: str, label: str) -> "ArgumentMap":
        self.fallacies[unit_id] = label
        return self

    # -- accesseurs ---------------------------------------------------------
    def attacks(self) -> List[Tuple[str, str]]:
        return [(r.source, r.target) for r in self.relations if r.kind == "attack"]

    def supports(self) -> List[Tuple[str, str]]:
        return [(r.source, r.target) for r in self.relations if r.kind == "support"]

    # -- projection symbolique ---------------------------------------------
    def to_dung(self, include_isolated: bool = True):
        """Projette la carte dans un AF de Dung (TweetyProject).

        Les unites deviennent des arguments ; les relations d'attaque
        deviennent des attaques. Les supports ne sont pas representables
        directement dans un AF abstrait de Dung : on les ignore ici (ils
        servent a la lecture / a une eventuelle reduction ASPIC ulterieure).
        Import paresseux de `symbolic` pour ne pas demarrer le JVM sans raison.
        """
        from src.symbolic.dung import DungAF

        af = DungAF()
        attack_pairs = self.attacks()
        if include_isolated:
            for uid in self.units:
                af.add_argument(uid)
        for src, tgt in attack_pairs:
            af.add_attack(src, tgt)
        return af

    def coherence(self, semantics: str = "grounded") -> Dict[str, object]:
        """Verifie la coherence logique via l'extension de Dung.

        Renvoie l'ensemble accepte, les unites rejetees (attaquees et non
        reinstaurees) et un verdict de coherence (au moins une extension
        non vide / conflit irreductible).
        """
        af = self.to_dung()
        if semantics == "grounded":
            accepted = af.grounded_extension()
            extensions = [accepted]
        else:
            extensions = af.extensions(semantics)
            accepted = set().union(*extensions) if extensions else set()

        all_units = set(self.units.keys())
        rejected = sorted(all_units - accepted)
        return {
            "semantics": semantics,
            "accepted": sorted(accepted),
            "rejected": rejected,
            "n_extensions": len(extensions),
            "coherent": len(accepted) > 0,
            "attacks": af.attacks(),
        }

    # -- serialisation ------------------------------------------------------
    def to_dict(self) -> dict:
        return {
            "units": [u.to_dict() for u in self.units.values()],
            "relations": [r.to_dict() for r in self.relations],
            "fallacies": dict(self.fallacies),
            "meta": dict(self.meta),
        }

    def summary(self) -> str:
        n_att = len(self.attacks())
        n_sup = len(self.supports())
        lines = [
            f"unites: {len(self.units)} (premisses={sum(u.role=='premise' for u in self.units.values())}, "
            f"conclusions={sum(u.role=='conclusion' for u in self.units.values())})",
            f"relations: {len(self.relations)} (attaques={n_att}, supports={n_sup})",
            f"sophismes detectes: {len(self.fallacies)}",
        ]
        return "\n".join(lines)
