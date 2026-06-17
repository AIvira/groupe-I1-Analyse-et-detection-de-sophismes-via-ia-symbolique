"""Metriques unifiees pour toutes les approches (baseline, transformer, NLI).

Toutes les approches produisent un `TrainingArtifacts` exposant un DataFrame
`predictions` avec au moins les colonnes `label` (verite) et `predicted_label`.
Ce module calcule un jeu de metriques standard a partir de ce DataFrame, de
maniere homogene, et fournit des sorties console + JSON.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    balanced_accuracy_score,
    precision_recall_fscore_support,
)

TRUE_COL = "label"
PRED_COL = "predicted_label"


def compute_metrics(y_true: List[str], y_pred: List[str]) -> Dict:
    """Calcule un dictionnaire de metriques standard.

    Renvoie accuracy, balanced accuracy, et F1/precision/rappel en macro,
    micro et weighted, plus un detail par classe.
    """
    labels = sorted(set(y_true) | set(y_pred))

    macro = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average="macro", zero_division=0
    )
    micro = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average="micro", zero_division=0
    )
    weighted = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average="weighted", zero_division=0
    )
    per_class = precision_recall_fscore_support(
        y_true, y_pred, labels=labels, average=None, zero_division=0
    )

    per_class_metrics = {}
    for i, label in enumerate(labels):
        per_class_metrics[label] = {
            "precision": float(per_class[0][i]),
            "recall": float(per_class[1][i]),
            "f1": float(per_class[2][i]),
            "support": int(per_class[3][i]),
        }

    return {
        "n_examples": len(y_true),
        "n_classes": len(labels),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy": float(balanced_accuracy_score(y_true, y_pred)),
        "macro_f1": float(macro[2]),
        "macro_precision": float(macro[0]),
        "macro_recall": float(macro[1]),
        "micro_f1": float(micro[2]),
        "weighted_f1": float(weighted[2]),
        "per_class": per_class_metrics,
    }


def metrics_from_predictions(predictions: pd.DataFrame) -> Dict:
    if TRUE_COL not in predictions.columns or PRED_COL not in predictions.columns:
        raise ValueError(
            f"Le DataFrame de predictions doit contenir '{TRUE_COL}' et '{PRED_COL}'."
        )
    y_true = predictions[TRUE_COL].astype(str).tolist()
    y_pred = predictions[PRED_COL].astype(str).tolist()
    return compute_metrics(y_true, y_pred)


def metrics_from_predictions_csv(csv_path: str) -> Dict:
    return metrics_from_predictions(pd.read_csv(csv_path))


def write_metrics_json(artifacts, output_path: str) -> None:
    """Ecrit un JSON structure: metriques globales + selection de modele."""
    metrics = metrics_from_predictions(artifacts.predictions)
    payload = {
        "model_name": getattr(artifacts, "model_name", "unknown"),
        "dev_macro_f1": float(getattr(artifacts, "dev_macro_f1", 0.0)),
        "candidate_dev_macro_f1": dict(getattr(artifacts, "candidate_scores", {}) or {}),
        "train_size": int(getattr(artifacts, "train_size", 0)),
        "dev_size": int(getattr(artifacts, "dev_size", 0)),
        "test_size": int(getattr(artifacts, "test_size", 0)),
        "test_metrics": metrics,
    }
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def _bar(value: float, width: int = 20) -> str:
    filled = int(round(value * width))
    return "#" * filled + "." * (width - filled)


def format_metrics_dict(metrics: Dict) -> str:
    """Rendu console lisible d'un dictionnaire de metriques."""
    lines = []
    lines.append("=" * 56)
    lines.append("  METRIQUES (test)")
    lines.append("=" * 56)
    lines.append(f"  examples           : {metrics['n_examples']}")
    lines.append(f"  classes            : {metrics['n_classes']}")
    lines.append(f"  accuracy           : {metrics['accuracy']:.4f}  {_bar(metrics['accuracy'])}")
    lines.append(
        f"  balanced accuracy  : {metrics['balanced_accuracy']:.4f}  {_bar(metrics['balanced_accuracy'])}"
    )
    lines.append(f"  macro F1           : {metrics['macro_f1']:.4f}  {_bar(metrics['macro_f1'])}")
    lines.append(f"  micro F1           : {metrics['micro_f1']:.4f}")
    lines.append(f"  weighted F1        : {metrics['weighted_f1']:.4f}")
    lines.append(f"  macro precision    : {metrics['macro_precision']:.4f}")
    lines.append(f"  macro recall       : {metrics['macro_recall']:.4f}")
    lines.append("-" * 56)
    lines.append(f"  {'classe':<24}{'P':>7}{'R':>7}{'F1':>7}{'n':>6}")
    lines.append("-" * 56)
    per_class = metrics["per_class"]
    # tri par F1 croissant: on voit d'abord les classes les plus faibles
    for label in sorted(per_class, key=lambda c: per_class[c]["f1"]):
        m = per_class[label]
        lines.append(
            f"  {label:<24}{m['precision']:>7.3f}{m['recall']:>7.3f}{m['f1']:>7.3f}{m['support']:>6}"
        )
    lines.append("=" * 56)
    return "\n".join(lines)


def format_metrics_console(artifacts) -> str:
    """Resume console complet pour un artifacts d'entrainement."""
    metrics = metrics_from_predictions(artifacts.predictions)
    lines = []
    lines.append("")
    lines.append(f"### Modele: {getattr(artifacts, 'model_name', 'unknown')}")
    candidates = getattr(artifacts, "candidate_scores", {}) or {}
    if len(candidates) > 1:
        lines.append("Selection (dev macro F1):")
        for name, score in sorted(candidates.items(), key=lambda kv: -kv[1]):
            mark = "  <- best" if name == artifacts.model_name else ""
            lines.append(f"  {name:<28}{score:.4f}{mark}")
    lines.append(f"Dev macro F1: {getattr(artifacts, 'dev_macro_f1', 0.0):.4f}")
    lines.append(format_metrics_dict(metrics))

    top = getattr(artifacts, "top_confusions", None)
    if top is not None and not top.empty:
        lines.append("")
        lines.append("Top confusions (vrai -> predit):")
        lines.append(top.head(10).to_string(index=False))
    return "\n".join(lines)