from __future__ import annotations


import re
from collections import defaultdict
from typing import Dict, List

from src.domain.models import Prediction, RuleHit


class RuleBasedFallacyDetector:
    """Moteur de regles lexicales/structurelles explicable.

    Chaque regle associe un motif a un label, un poids de confiance et une
    justification en clair. Les poids eleves (>= 0.85) servent de garde-fou :
    dans l'arbitrage symbolique (Dung), une regle explicite tres confiante peut
    contredire la prediction neuronale. Les poids faibles n'apportent qu'un
    signal d'appoint. Les motifs sont volontairement de haute precision.
    """

    def __init__(self) -> None:
        self.patterns: Dict[str, List[tuple[re.Pattern[str], float, str]]] = {
            "ad_hominem": [
                (re.compile(r"\b(you are|you're|tu es|vous etes)\b[^.?!]{0,40}\b(stupid|ignorant|idiot|idiotic|moron|moronic|liar|fool|foolish|hypocrite|coward|naive|imbecile|ridicule)\b", re.I), 0.9, "attaque personnelle explicite"),
                (re.compile(r"\b(he|she|they|his|her|their)\b[^.?!]{0,30}\b(is|are)\b[^.?!]{0,20}\b(a |an )?(idiot|liar|fool|hypocrite|criminal|corrupt)\b", re.I), 0.88, "disqualification de la personne plutot que de l'argument"),
                (re.compile(r"\battack(ing|s)?\b[^.?!]{0,20}\b(the )?(person|individual|man|character)\b", re.I), 0.9, "attaque de la personne (ad hominem nomme)"),
                (re.compile(r"\b(against the man|ad hominem)\b", re.I), 0.95, "ad hominem explicite"),
                (re.compile(r"\b(personne comme toi|someone like you|what would you know|coming from someone)\b", re.I), 0.8, "delegitimation de la personne"),
                (re.compile(r"\bwhat would (you|he|she|they) know\b", re.I), 0.85, "disqualification de la competence de l'interlocuteur"),
            ],
            "false_dilemma": [
                (re.compile(r"\beither\b[^.?!]{1,60}\bor\b", re.I), 0.9, "construction binaire 'either...or'"),
                (re.compile(r"\b(soit)\b[^.?!]{1,60}\b(soit|ou)\b", re.I), 0.85, "construction binaire 'soit...soit'"),
                (re.compile(r"\bif you('re| are)? not\b[^.?!]{0,40}\b(you('re| are)?|then)\b[^.?!]{0,30}\bagainst\b", re.I), 0.92, "alternative forcee 'si pas avec, alors contre'"),
                (re.compile(r"\b(if you are not with us, you are against us|avec nous ou contre nous|with us or against us)\b", re.I), 0.95, "alternative forcee classique"),
                (re.compile(r"\bonly two (choices|options|ways|sides|possibilities)\b", re.I), 0.9, "reduction explicite a deux options"),
                (re.compile(r"\b(il n'y a que deux choix|there are only two options)\b", re.I), 0.9, "reduction explicite a deux options"),
            ],
            "straw_man": [
                (re.compile(r"\b(so you are saying|so you're saying|donc tu dis que|donc vous dites que)\b", re.I), 0.7, "reformulation potentiellement deformante"),
                (re.compile(r"\b(by your logic|selon ta logique|selon votre logique)\b", re.I), 0.7, "reformulation rhetorique de la position adverse"),
                (re.compile(r"\b(you want everyone to|tu veux que tout le monde|vous voulez que tout le monde)\b", re.I), 0.75, "amplification de la position adverse"),
                (re.compile(r"\b(fallacy of extension|misrepresent(ing|s|ed)?|distort(ing|s|ed)?)\b[^.?!]{0,25}\b(position|argument|view)\b", re.I), 0.8, "deformation de la position adverse"),
            ],
            "ad_populum": [
                (re.compile(r"\b(everyone|everybody|most people|the majority of people|nobody)\b[^.?!]{0,25}\b(knows|believes|agrees|thinks|does|says)\b", re.I), 0.85, "appel a la croyance majoritaire"),
                (re.compile(r"\b(everyone is doing it|millions of people can't be wrong|it's popular so)\b", re.I), 0.9, "appel a la popularite"),
                (re.compile(r"\b(3 out of 4|9 out of 10|\d+ ?% of (people|americans|users))\b", re.I), 0.7, "argument par les chiffres de popularite"),
            ],
            "faulty_generalization": [
                (re.compile(r"\b(all|every)\b \w+ (are|is|will|can't|cannot)\b", re.I), 0.6, "generalisation universelle a partir de cas"),
                (re.compile(r"\b(all (men|women|politicians|people)|everybody always|they all)\b", re.I), 0.65, "generalisation hative sur un groupe"),
            ],
        }

    def score(self, text: str) -> tuple[Dict[str, float], List[RuleHit]]:
        scores: Dict[str, float] = defaultdict(float)
        hits: List[RuleHit] = []
        for label, rules in self.patterns.items():
            for pattern, weight, evidence in rules:
                if pattern.search(text):
                    scores[label] = max(scores[label], weight)
                    hits.append(RuleHit(label=label, weight=weight, evidence=evidence))
        if not scores:
            scores["not_fallacy"] = 0.5
        return dict(scores), hits

    def predict(self, text: str) -> Prediction:
        scores, hits = self.score(text)
        label = max(scores, key=scores.get)
        return Prediction(
            text=text,
            label=label,
            confidence=scores[label],
            mode="rules",
            evidence=[hit.evidence for hit in hits if hit.label == label],
            scores=scores,
        )
