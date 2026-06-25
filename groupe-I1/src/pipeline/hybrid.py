from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, Optional

import pandas as pd

from src.domain.models import Prediction, TrainingConfig
from src.rules.detector import RuleBasedFallacyDetector

LABEL_ALIASES = {
    "ad hominem": "ad_hominem",
    "ad populum": "ad_populum",
    "appeal to emotion": "appeal_to_emotion",
    "circular reasoning": "circular_reasoning",
    "equivocation": "equivocation",
    "fallacy of extension": "straw_man",
    "fallacy of logic": "fallacy_of_logic",
    "fallacy of relevance": "fallacy_of_relevance",
    "false causality": "false_causality",
    "false dilemma": "false_dilemma",
    "faulty generalization": "faulty_generalization",
    "intentional": "intentional",
    "miscellaneous": "miscellaneous",
}


class HybridFallacyPipeline:
    def __init__(
        self,
        model=None,
        config: Optional[TrainingConfig] = None,
        mappings_path: Optional[str] = None,
        extract_structure: bool = True,
        extractor=None,
    ) -> None:
        self.model = model
        self.config = config or TrainingConfig()
        self.rule_detector = RuleBasedFallacyDetector()
        self.label_metadata = self._load_label_metadata(mappings_path)
        self.extract_structure = extract_structure
        self._extractor = extractor

    def _load_label_metadata(self, mappings_path: Optional[str]) -> Dict[str, Dict[str, str]]:
        if mappings_path is None:
            return {}
        path = Path(mappings_path)
        if not path.exists():
            return {}
        metadata: Dict[str, Dict[str, str]] = {}
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                key = row["Original Name"].strip().lower()
                value = {
                    "understandable_name": row.get("Understandable Name", "").strip(),
                    "description": row.get("Description", "").strip(),
                    "logical_form": row.get("Logical Form", "").strip(),
                    "masked_logical_form": row.get("Masked Logical Form", "").strip(),
                }
                metadata[key] = value
                alias = LABEL_ALIASES.get(key)
                if alias:
                    metadata[alias] = value
        return metadata

    def _enrich_with_label_metadata(self, prediction: Prediction) -> Prediction:
        meta = self.label_metadata.get(prediction.label.lower())
        if not meta:
            return prediction
        enriched = list(prediction.evidence)
        if meta["description"]:
            enriched.append(f"description: {meta['description']}")
        if meta["logical_form"]:
            enriched.append(f"logical_form: {meta['logical_form']}")
        prediction.evidence = enriched
        return prediction

    def predict_rules(self, text: str) -> Prediction:
        return self._enrich_with_label_metadata(self.rule_detector.predict(text))

    def _build_inference_frame(self, text: str) -> pd.DataFrame:
        return pd.DataFrame(
            [
                {
                    "text": text,
                    "masked_text": "",
                    "context": "",
                }
            ]
        )

    def predict_ml(self, text: str) -> Prediction:
        if self.model is None:
            raise RuntimeError("Aucun modele supervise n'est charge.")
        features = self._build_inference_frame(text)
        probabilities = self.model.predict_proba(features)[0]
        labels = list(self.model.classes_)
        scores = {label: float(prob) for label, prob in zip(labels, probabilities)}
        label = max(scores, key=scores.get)
        return self._enrich_with_label_metadata(Prediction(
            text=text,
            label=label,
            confidence=scores[label],
            mode="ml",
            evidence=["prediction du classifieur supervise (TF-IDF ou ensemble TF-IDF+RoBERTa)"],
            scores=scores,
        ))

    def analyze(self, text: str) -> Dict[str, object]:
        """Analyse neuro-symbolique complete d'un texte.

        Combine la couche neuronale/ML, le moteur de regles, puis la couche
        symbolique (TweetyProject) : arbitrage des detecteurs par semantique
        fondee de Dung + verdict formel via le scheme argumentatif du sophisme.
        Le module `symbolic` (et donc le JVM) n'est importe qu'ici.
        """
        from src.symbolic.dung import arbitrate, symbolic_verdict

        rule_prediction = self.predict_rules(text)
        rule_label = rule_prediction.label if rule_prediction.label != "not_fallacy" else None
        rule_conf = rule_prediction.confidence if rule_label else 0.0

        if self.model is not None:
            ml_prediction = self.predict_ml(text)
            ml_label, ml_conf = ml_prediction.label, ml_prediction.confidence
        else:
            ml_prediction = None
            ml_label, ml_conf = None, 0.0

        arbitration = arbitrate(
            ml_label=ml_label,
            ml_confidence=ml_conf,
            rule_label=rule_label,
            rule_confidence=rule_conf,
        )
        final_label = arbitration["final_label"]

        # On extrait d'abord la structure : son AF de Dung sert a decider si la
        # question critique du scheme est "repondue" (objection a la conclusion
        # reinstauree) -> le symbolique filtre alors un faux positif du neuronal.
        structure = None
        if self.extract_structure:
            from src.extraction.extractor import get_extractor

            extractor = self._extractor or get_extractor()
            argmap = extractor.extract(text)
            structure = {
                "extractor": argmap.meta.get("extractor"),
                "units": [u.to_dict() for u in argmap.units.values()],
                "relations": [r.to_dict() for r in argmap.relations],
                "fallacies": dict(argmap.fallacies),
                "coherence": argmap.coherence("grounded"),
            }

        cq_answered = self._critical_question_answered(structure)
        verdict = symbolic_verdict(final_label, critical_question_answered=cq_answered)
        # Faux positif filtre : le neuronal/regles a detecte un sophisme mais la
        # structure argumentative resiste a son objection (conclusion reinstauree).
        false_positive_filtered = (
            final_label not in ("not_fallacy", "other_fallacy") and verdict.claim_accepted
        )

        return {
            "text": text,
            "final_label": final_label,
            "decided_by": arbitration["winner"],
            "argument_structure": structure,
            "neural": {"label": ml_label, "confidence": ml_conf} if ml_prediction else None,
            "rules": {
                "label": rule_label,
                "confidence": rule_conf,
                "evidence": rule_prediction.evidence,
            },
            "symbolic_arbitration": {
                "disagreement": arbitration["disagreement"],
                "attacks": arbitration["attacks"],
                "grounded_extension": arbitration["grounded_extension"],
            },
            "symbolic_verdict": {
                "scheme": verdict.scheme,
                "critical_question": verdict.critical_question,
                "status": verdict.status,
                "claim_accepted": verdict.claim_accepted,
                "critical_question_answered": cq_answered,
                "false_positive_filtered": false_positive_filtered,
                "grounded_extension": verdict.grounded_extension,
                "explanation": verdict.explanation,
            },
        }

    @staticmethod
    def _critical_question_answered(structure: Optional[Dict[str, object]]) -> bool:
        """La question critique est-elle "repondue" par la structure extraite ?

        Critere formel : il existe une **objection** (attaque) visant une
        conclusion/these, mais cette conclusion reste **acceptee dans l'extension
        fondee** de l'AF extrait (elle a ete reinstauree par un contre-argument).
        Autrement dit, l'argument resiste a son objection => le sophisme detecte
        par le neuronal est tenu pour un faux positif.
        """
        if not structure:
            return False
        coherence = structure.get("coherence", {}) or {}
        accepted = set(coherence.get("accepted", []))
        roles = {u["id"]: u.get("role") for u in structure.get("units", [])}
        for attack in coherence.get("attacks", []):
            # `attacks` est une liste de paires (source, cible).
            if not isinstance(attack, (list, tuple)) or len(attack) != 2:
                continue
            target = attack[1]
            if roles.get(target) in ("conclusion", "claim") and target in accepted:
                return True
        return False

    def predict_hybrid(self, text: str) -> Prediction:
        rule_prediction = self.predict_rules(text)
        if self.model is None:
            return rule_prediction

        ml_prediction = self.predict_ml(text)
        combined: Dict[str, float] = {}
        labels = set(rule_prediction.scores) | set(ml_prediction.scores)
        for label in labels:
            combined[label] = (
                self.config.hybrid_ml_weight * ml_prediction.scores.get(label, 0.0)
                + self.config.hybrid_rule_weight * rule_prediction.scores.get(label, 0.0)
            )

        if (
            rule_prediction.label != "not_fallacy"
            and rule_prediction.confidence >= self.config.min_rule_confidence
        ):
            combined[rule_prediction.label] = combined.get(rule_prediction.label, 0.0) + self.config.hybrid_rule_bonus

        label = max(combined, key=combined.get)
        evidence = []
        evidence.extend(f"regle: {item}" for item in rule_prediction.evidence)
        evidence.extend(f"ml: {item}" for item in ml_prediction.evidence)
        return self._enrich_with_label_metadata(Prediction(
            text=text,
            label=label,
            confidence=combined[label],
            mode="hybrid",
            evidence=evidence,
            scores=combined,
        ))
