"""Matplotlib figures for symbolic regression experiments."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_pareto(equations: pd.DataFrame, selected: pd.Series, dataset_name: str, output_path: Path) -> None:
    """Save a Pareto accuracy-complexity plot for one dataset."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(7.5, 5.0), constrained_layout=True)
    ax.scatter(
        equations["complexity"],
        equations["rmse"],
        s=42,
        alpha=0.72,
        color="#2f6f8f",
        label="Equations PySR",
    )
    ax.scatter(
        [selected["complexity"]],
        [selected["rmse"]],
        s=120,
        marker="*",
        color="#c4512f",
        label="Equation retenue",
        zorder=5,
    )
    ax.set_xlabel("Complexite")
    ax.set_ylabel("RMSE test")
    ax.set_title(f"Frontiere precision-complexite - {dataset_name}")
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.savefig(output_path, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def plot_model_comparison(metrics: pd.DataFrame, output_path: Path) -> None:
    """Save grouped bar plots comparing RMSE and interpretability."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    labels = metrics["dataset"] + "\n" + metrics["method"]
    fig, axes = plt.subplots(2, 1, figsize=(10.5, 8.0), constrained_layout=True)
    axes[0].bar(labels, metrics["rmse"], color="#4c78a8")
    axes[0].set_ylabel("RMSE test")
    axes[0].set_title("Precision predictive")
    axes[0].tick_params(axis="x", rotation=45)
    axes[0].grid(axis="y", alpha=0.25)

    axes[1].bar(labels, metrics["interpretability"], color="#59a14f")
    axes[1].set_ylabel("Score interpretabilite")
    axes[1].set_title("Parcimonie et lisibilite")
    axes[1].tick_params(axis="x", rotation=45)
    axes[1].grid(axis="y", alpha=0.25)
    fig.savefig(output_path, dpi=180, bbox_inches="tight", facecolor="white")
    plt.close(fig)

