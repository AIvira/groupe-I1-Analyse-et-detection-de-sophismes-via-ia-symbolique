"""Couche symbolique : argumentation abstraite de Dung via TweetyProject (JPype).

Ce module est le coeur "Intelligence Symbolique" du projet I1. Il fait trois
choses :

1. `DungAF` : un wrapper Python propre autour des frameworks d'argumentation
   abstraite de TweetyProject (`org.tweetyproject.arg.dung`). On construit un
   graphe arguments/attaques et on calcule les extensions sous les semantiques
   de Dung (grounded, complete, preferred, stable).

2. Une bibliotheque de *schemes argumentatifs* (Walton) : pour chaque type de
   sophisme on connait la "question critique" qui le met en defaut. On encode
   cela formellement comme un petit AF `claim <- critical_question`. Si la
   question critique reste sans reponse (cas par defaut d'un sophisme), la
   conclusion n'est pas dans l'extension fondee => verdict formel "fallacieux".
   Si une reponse est fournie, la conclusion est reinstauree => le sophisme
   detecte par le neuronal etait un faux positif.

3. Un *arbitrage* regle vs ML resolu par la semantique fondee de Dung, qui
   illustre comment le symbolique filtre / corrige les predictions neuronales.

Le JVM est demarre paresseusement : importer ce module ne demarre pas Java.
"""

from __future__ import annotations

import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

_JVM_LOCK = threading.Lock()
_JVM_STARTED = False
_CLASSES: Dict[str, object] = {}

SEMANTICS = ("grounded", "complete", "preferred", "stable", "admissible")


def _default_jar_paths() -> List[str]:
    lib_dir = Path(__file__).resolve().parents[2] / "lib"
    return sorted(str(p) for p in lib_dir.glob("*.jar"))


def start_jvm(jar_paths: Optional[List[str]] = None) -> None:
    """Demarre le JVM et charge les classes Tweety (idempotent, thread-safe)."""
    global _JVM_STARTED
    if _JVM_STARTED:
        return
    with _JVM_LOCK:
        if _JVM_STARTED:
            return
        import jpype
        import jpype.imports  # noqa: F401  (active l'import de classes Java)

        jars = jar_paths or _default_jar_paths()
        if not jars:
            raise RuntimeError(
                "Aucun JAR TweetyProject trouve dans lib/. "
                "Telecharger org.tweetyproject.arg.dung-<version>-with-dependencies.jar."
            )
        if not jpype.isJVMStarted():
            jpype.startJVM(classpath=jars)

        from org.tweetyproject.arg.dung.syntax import DungTheory, Argument, Attack
        from org.tweetyproject.arg.dung.reasoner import (
            SimpleGroundedReasoner,
            SimpleCompleteReasoner,
            SimplePreferredReasoner,
            SimpleStableReasoner,
            SimpleAdmissibleReasoner,
        )

        _CLASSES.update(
            DungTheory=DungTheory,
            Argument=Argument,
            Attack=Attack,
            grounded=SimpleGroundedReasoner,
            complete=SimpleCompleteReasoner,
            preferred=SimplePreferredReasoner,
            stable=SimpleStableReasoner,
            admissible=SimpleAdmissibleReasoner,
        )
        _JVM_STARTED = True


class DungAF:
    """Framework d'argumentation abstraite de Dung (arguments + attaques)."""

    def __init__(self) -> None:
        start_jvm()
        self._theory = _CLASSES["DungTheory"]()
        self._args: Dict[str, object] = {}

    def add_argument(self, name: str) -> "DungAF":
        if name not in self._args:
            arg = _CLASSES["Argument"](name)
            self._args[name] = arg
            self._theory.add(arg)
        return self

    def add_attack(self, source: str, target: str) -> "DungAF":
        self.add_argument(source)
        self.add_argument(target)
        self._theory.add(_CLASSES["Attack"](self._args[source], self._args[target]))
        return self

    def arguments(self) -> List[str]:
        return list(self._args.keys())

    def attacks(self) -> List[Tuple[str, str]]:
        result = []
        for att in self._theory.getAttacks():
            result.append((str(att.getAttacker().getName()), str(att.getAttacked().getName())))
        return sorted(result)

    def _reasoner(self, semantics: str):
        if semantics not in _CLASSES:
            raise ValueError(f"Semantique inconnue: {semantics}. Choisir parmi {SEMANTICS}.")
        return _CLASSES[semantics]()

    def extensions(self, semantics: str = "preferred") -> List[Set[str]]:
        """Toutes les extensions sous la semantique donnee (set de noms)."""
        reasoner = self._reasoner(semantics)
        models = reasoner.getModels(self._theory)
        result = []
        for ext in models:
            result.append({str(a.getName()) for a in ext})
        return result

    def grounded_extension(self) -> Set[str]:
        """L'unique extension fondee (skeptique, deterministe)."""
        model = self._reasoner("grounded").getModel(self._theory)
        return {str(a.getName()) for a in model}

    def describe(self) -> str:
        lines = [f"Arguments: {{{', '.join(sorted(self._args))}}}"]
        atts = self.attacks()
        lines.append("Attaques: " + (", ".join(f"{s}->{t}" for s, t in atts) if atts else "(aucune)"))
        for sem in ("grounded", "complete", "preferred", "stable"):
            exts = self.extensions(sem)
            rendered = "; ".join("{" + ", ".join(sorted(e)) + "}" for e in exts) or "(aucune)"
            lines.append(f"{sem:<10}: {rendered}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Schemes argumentatifs : sophisme -> question critique (Walton)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Scheme:
    label: str
    scheme: str          # nom du scheme argumentatif
    critical_question: str  # la question critique qui defait l'argument


FALLACY_SCHEMES: Dict[str, Scheme] = {
    "ad_hominem": Scheme(
        "ad_hominem", "Argument from ethos / attaque personnelle",
        "L'attaque sur la personne est-elle pertinente pour la verite de sa these ?",
    ),
    "ad_populum": Scheme(
        "ad_populum", "Argument from popular opinion",
        "Le fait qu'une opinion soit populaire etablit-il sa verite ?",
    ),
    "appeal_to_emotion": Scheme(
        "appeal_to_emotion", "Appeal to emotion",
        "Les emotions invoquees ont-elles un rapport avec la verite de la conclusion ?",
    ),
    "circular_reasoning": Scheme(
        "circular_reasoning", "Begging the question",
        "La conclusion est-elle deja presupposee dans les premisses ?",
    ),
    "equivocation": Scheme(
        "equivocation", "Equivocation",
        "Un terme cle garde-t-il le meme sens dans toutes les premisses ?",
    ),
    "fallacy_of_credibility": Scheme(
        "fallacy_of_credibility", "Appeal to authority",
        "L'autorite citee est-elle un expert legitime sur cette question precise ?",
    ),
    "fallacy_of_logic": Scheme(
        "fallacy_of_logic", "Inference invalide",
        "La conclusion decoule-t-elle des premisses par une inference valide ?",
    ),
    "fallacy_of_relevance": Scheme(
        "fallacy_of_relevance", "Red herring / non-pertinence",
        "Les premisses sont-elles pertinentes pour la conclusion ?",
    ),
    "false_causality": Scheme(
        "false_causality", "Argument from correlation to cause",
        "Existe-t-il un lien causal au-dela d'une simple correlation ou succession ?",
    ),
    "false_dilemma": Scheme(
        "false_dilemma", "False dilemma",
        "Les options presentees sont-elles vraiment les seules possibles ?",
    ),
    "faulty_generalization": Scheme(
        "faulty_generalization", "Hasty generalization",
        "L'echantillon est-il assez grand et representatif pour generaliser ?",
    ),
    "intentional": Scheme(
        "intentional", "Erreur de raisonnement intentionnelle",
        "Le raisonnement repose-t-il sur une tromperie deliberee plutot que sur la logique ?",
    ),
    "straw_man": Scheme(
        "straw_man", "Straw man",
        "La position reformulee correspond-elle a la position reelle de l'adversaire ?",
    ),
}


@dataclass
class SymbolicVerdict:
    label: str
    scheme: str
    critical_question: str
    claim_accepted: bool
    status: str          # "fallacieux" ou "valide"
    grounded_extension: List[str]
    af: DungAF = field(repr=False, default=None)
    explanation: str = ""


def build_scheme_af(label: str, critical_question_answered: bool = False) -> Tuple[DungAF, Scheme]:
    """Construit l'AF canonique d'un scheme de sophisme.

    Structure :
        CLAIM            : la conclusion avancee
        CRITICAL_QUESTION attaque CLAIM
        ANSWER (option.) attaque CRITICAL_QUESTION   (si la CQ a une reponse)

    Sans reponse a la question critique (cas par defaut d'un sophisme), CLAIM
    est defaite => verdict formel "fallacieux". Avec reponse, CLAIM reinstauree.
    """
    scheme = FALLACY_SCHEMES.get(label)
    if scheme is None:
        scheme = Scheme(label, "scheme generique", "L'argument resiste-t-il a l'examen critique ?")

    af = DungAF()
    af.add_argument("CLAIM")
    af.add_attack("CRITICAL_QUESTION", "CLAIM")
    if critical_question_answered:
        af.add_attack("ANSWER", "CRITICAL_QUESTION")
    return af, scheme


def symbolic_verdict(label: str, critical_question_answered: bool = False) -> SymbolicVerdict:
    """Verdict formel : la conclusion survit-elle a la question critique ?"""
    af, scheme = build_scheme_af(label, critical_question_answered)
    grounded = af.grounded_extension()
    accepted = "CLAIM" in grounded
    status = "valide" if accepted else "fallacieux"
    if accepted:
        explanation = (
            f"La question critique du scheme '{scheme.scheme}' a recu une reponse : "
            f"la conclusion (CLAIM) est reinstauree dans l'extension fondee "
            f"{sorted(grounded)}. Le sophisme detecte est donc un faux positif."
        )
    else:
        explanation = (
            f"La question critique reste sans reponse : « {scheme.critical_question} » "
            f"L'objection (CRITICAL_QUESTION) defait la conclusion. L'extension fondee "
            f"est {sorted(grounded)}, CLAIM n'y figure pas => raisonnement fallacieux confirme."
        )
    return SymbolicVerdict(
        label=label,
        scheme=scheme.scheme,
        critical_question=scheme.critical_question,
        claim_accepted=accepted,
        status=status,
        grounded_extension=sorted(grounded),
        af=af,
        explanation=explanation,
    )


# ---------------------------------------------------------------------------
# Arbitrage regle vs ML par semantique de Dung
# ---------------------------------------------------------------------------

def arbitrate(
    ml_label: Optional[str],
    ml_confidence: float,
    rule_label: Optional[str],
    rule_confidence: float,
    rule_override_threshold: float = 0.9,
    none_labels: Tuple[str, ...] = ("not_fallacy", "other_fallacy"),
) -> Dict[str, object]:
    """Resout un desaccord regle/ML par la semantique fondee de Dung.

    Modele : un argument "default" NOT_FALLACY (il n'y a pas de sophisme) est
    attaque par tout detecteur qui annonce un sophisme. Si regle et ML sont en
    desaccord, une regle explicite tres confiante attaque la prediction ML
    (la regle prime), sinon le ML attaque la regle. Le label retenu est le
    detecteur acceptable (dans l'extension fondee) le plus confiant.
    """
    af = DungAF()
    af.add_argument("DEFAULT_NONE")

    detectors: Dict[str, Tuple[str, float]] = {}
    if ml_label and ml_label not in none_labels:
        detectors["ML"] = (ml_label, ml_confidence)
        af.add_attack("ML", "DEFAULT_NONE")
    if rule_label and rule_label not in none_labels:
        detectors["RULE"] = (rule_label, rule_confidence)
        af.add_attack("RULE", "DEFAULT_NONE")

    disagree = (
        "ML" in detectors and "RULE" in detectors and detectors["ML"][0] != detectors["RULE"][0]
    )
    if disagree:
        if rule_confidence >= rule_override_threshold:
            af.add_attack("RULE", "ML")  # la regle explicite prime
        else:
            af.add_attack("ML", "RULE")  # sinon le ML prime

    grounded = af.grounded_extension()
    accepted = [d for d in detectors if d in grounded]
    if not accepted:
        final_label = none_labels[0]
        winner = "DEFAULT_NONE"
    else:
        winner = max(accepted, key=lambda d: detectors[d][1])
        final_label = detectors[winner][0]

    return {
        "final_label": final_label,
        "winner": winner,
        "grounded_extension": sorted(grounded),
        "attacks": af.attacks(),
        "disagreement": disagree,
        "af": af,
    }
