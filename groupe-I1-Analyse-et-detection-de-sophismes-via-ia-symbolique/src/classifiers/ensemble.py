"""Ensemble de classifieurs pour la prediction de sophismes.

Resultat de l'evaluation (test 13 classes, dataset complet) :

    modele                 macro_f1   accuracy
    TF-IDF (baseline)        0.399      0.413
    RoBERTa                  0.448      0.479
    NLI (label-matching)     0.263      0.337
    -------------------------------------------
    TF-IDF + RoBERTa         0.470      0.497   <-- meilleur
    TF-IDF + RoBERTa + NLI   0.451      0.476

Le NLI est trop faible et degrade tout ensemble ou il entre : on combine donc
uniquement **TF-IDF + RoBERTa**, par moyenne des distributions de probabilite.

Les classes ci-dessous miment l'API sklearn (`classes_`, `predict_proba`) afin de
s'enficher dans `HybridFallacyPipeline` sans aucune modification de la pipeline :
celle-ci n'appelle jamais que `model.predict_proba(features)` et `model.classes_`.
"""
from __future__ import annotations

import pickle
from pathlib import Path
from typing import List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd


def _softmax(logits: np.ndarray) -> np.ndarray:
    stabilized = logits - logits.max(axis=1, keepdims=True)
    exp = np.exp(stabilized)
    return exp / exp.sum(axis=1, keepdims=True)


class TransformerProbaClassifier:
    """Expose un transformer fine-tune (RoBERTa) via l'API sklearn.

    `predict_proba` accepte le meme DataFrame que la pipeline construit
    (colonnes `text`, `masked_text`, `context`) et renvoie une distribution
    softmax alignee sur `classes_`.
    """

    def __init__(
        self,
        model_dir: str,
        device: Optional[str] = None,
        max_length: int = 256,
        batch_size: int = 32,
        use_masked_text: bool = True,
    ) -> None:
        import torch
        from transformers import AutoModelForSequenceClassification, AutoTokenizer

        self._torch = torch
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_dir).to(self.device).eval()
        id2label = {int(k): v for k, v in self.model.config.id2label.items()}
        self.classes_ = [id2label[i] for i in range(len(id2label))]
        self.max_length = max_length
        self.batch_size = batch_size
        self.use_masked_text = use_masked_text

    def _build_texts(self, df: pd.DataFrame) -> List[str]:
        texts: List[str] = []
        for _, row in df.iterrows():
            text = str(row.get("text", "")).strip()
            masked = str(row.get("masked_text", "")).strip()
            if self.use_masked_text and masked:
                texts.append(f"{text} [MASKED] {masked}".strip())
            else:
                texts.append(text)
        return texts

    def predict_proba(self, df: pd.DataFrame) -> np.ndarray:
        texts = self._build_texts(df)
        torch = self._torch
        chunks: List[np.ndarray] = []
        with torch.no_grad():
            for start in range(0, len(texts), self.batch_size):
                batch = texts[start:start + self.batch_size]
                encoded = self.tokenizer(
                    batch,
                    truncation=True,
                    padding=True,
                    max_length=self.max_length,
                    return_tensors="pt",
                ).to(self.device)
                chunks.append(self.model(**encoded).logits.detach().cpu().numpy())
        return _softmax(np.vstack(chunks))


class EnsembleProbaClassifier:
    """Moyenne ponderee des distributions de plusieurs classifieurs.

    Tous les estimateurs doivent exposer `classes_` et `predict_proba`, et
    partager le meme ensemble de labels dans le meme ordre.
    """

    def __init__(
        self,
        estimators: Sequence[Tuple[str, object]],
        weights: Optional[Sequence[float]] = None,
    ) -> None:
        if not estimators:
            raise ValueError("Au moins un estimateur est requis.")
        self.estimators = list(estimators)
        reference = list(self.estimators[0][1].classes_)
        for name, estimator in self.estimators:
            if list(estimator.classes_) != reference:
                raise ValueError(
                    f"Labels de '{name}' non alignes avec '{self.estimators[0][0]}'."
                )
        self.classes_ = reference
        raw = list(weights) if weights is not None else [1.0] * len(self.estimators)
        if len(raw) != len(self.estimators):
            raise ValueError("Le nombre de poids doit egaler le nombre d'estimateurs.")
        total = float(sum(raw))
        self.weights = [w / total for w in raw]

    def predict_proba(self, df: pd.DataFrame) -> np.ndarray:
        proba: Optional[np.ndarray] = None
        for (_, estimator), weight in zip(self.estimators, self.weights):
            scaled = np.asarray(estimator.predict_proba(df), dtype=float) * weight
            proba = scaled if proba is None else proba + scaled
        return proba


def load_ml_model(
    baseline_path: str,
    transformer_dir: Optional[str] = None,
    weights: Optional[Sequence[float]] = None,
):
    """Charge le classifieur ML a brancher dans la pipeline.

    - Sans `transformer_dir` (ou s'il est absent) : renvoie le baseline TF-IDF seul
      (comportement historique, retro-compatible).
    - Avec un `transformer_dir` valide : renvoie l'ensemble **TF-IDF + RoBERTa**
      (meilleure config mesuree, macro F1 ~0.47 contre ~0.40/0.45 en solo).
    """
    with open(baseline_path, "rb") as handle:
        baseline = pickle.load(handle)

    if transformer_dir is None:
        return baseline
    if not Path(transformer_dir).exists():
        return baseline

    transformer = TransformerProbaClassifier(transformer_dir)
    return EnsembleProbaClassifier(
        [("tfidf", baseline), ("roberta", transformer)],
        weights=weights,
    )
