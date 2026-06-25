"""Evaluation metrics for accuracy, parsimony and Pareto analysis."""

from __future__ import annotations

import math
import zlib
from typing import Any

import numpy as np
import pandas as pd
import sympy as sp
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error


def regression_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    """Compute standard regression metrics."""

    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    eps = np.finfo(float).eps
    return {
        "rmse": float(root_mean_squared_error(y_true, y_pred)),
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "r2": float(r2_score(y_true, y_pred)),
        "mape": float(np.mean(np.abs((y_true - y_pred) / np.maximum(np.abs(y_true), eps)))),
    }


def kolmogorov_proxy(expression: Any) -> int:
    """Approximate Kolmogorov complexity by compressed expression length."""

    text = str(expression)
    return len(zlib.compress(text.encode("utf-8"), level=9))


def sympy_complexity(expression: Any) -> int:
    """Compute a simple symbolic complexity score."""

    try:
        expr = sp.sympify(str(expression))
        return int(sp.count_ops(expr, visual=False) + len(str(expr)))
    except Exception:
        return len(str(expression))


def interpretability_score(complexity: float, kolmogorov_bits: float) -> float:
    """Higher is more interpretable, combining tree size and compressed length."""

    return float(1.0 / (1.0 + math.log1p(max(complexity, 0.0) + max(kolmogorov_bits, 0.0))))


def pareto_front(
    frame: pd.DataFrame,
    complexity_col: str = "complexity",
    error_col: str = "rmse",
) -> pd.DataFrame:
    """Return non-dominated rows for lower complexity and lower error."""

    if frame.empty:
        return frame.copy()
    ordered = frame.sort_values([complexity_col, error_col], ascending=[True, True]).reset_index(drop=True)
    best_error = math.inf
    keep: list[int] = []
    for idx, row in ordered.iterrows():
        error = float(row[error_col])
        if error < best_error:
            keep.append(idx)
            best_error = error
    return ordered.loc[keep].reset_index(drop=True)


def select_balanced_equation(
    frame: pd.DataFrame,
    complexity_col: str = "complexity",
    error_col: str = "rmse",
    complexity_weight: float = 0.35,
    kolmogorov_col: str = "kolmogorov_proxy",
    kolmogorov_weight: float = 0.2,
) -> pd.Series:
    """Select a knee-like point on the Pareto front and kolmogorov complexity proxy."""

    if frame.empty:
        raise ValueError("Cannot select from an empty Pareto frame.")
    work = frame.copy()
    error = work[error_col].astype(float)
    complexity = work[complexity_col].astype(float)
    error_norm = (error - error.min()) / max(error.max() - error.min(), np.finfo(float).eps)
    complexity_norm = (complexity - complexity.min()) / max(
        complexity.max() - complexity.min(), np.finfo(float).eps
    )
    score = error_norm + complexity_weight * complexity_norm
    if kolmogorov_col in work.columns:
        kolmogorov = work[kolmogorov_col].astype(float)
        kolmogorov_norm = (kolmogorov - kolmogorov.min()) / max(
            kolmogorov.max() - kolmogorov.min(), np.finfo(float).eps
        )
        score = score + kolmogorov_weight * kolmogorov_norm
    work["_balanced_score"] = score
    return work.loc[work["_balanced_score"].idxmin()]

