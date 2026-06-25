from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def plot_benchmark_summary(summary: pd.DataFrame):
    if summary.empty:
        raise ValueError("summary is empty")

    fig, axes = plt.subplots(1, 3, figsize=(16, 4))
    sat_summary = summary[summary["backend"] == "SAT"].copy()
    sat_solved = sat_summary[sat_summary["solved_rate"] > 0].copy()

    if sat_solved.empty:
        axes[0].text(0.5, 0.5, "No SAT solver available", ha="center", va="center")
        axes[0].set_axis_off()
    else:
        pivot = sat_solved.pivot_table(
            index="family",
            columns="solver",
            values="mean_time_s",
            aggfunc="mean",
        )
        pivot.plot(kind="bar", ax=axes[0], rot=15)
        axes[0].set_title("Mean SAT Solve Time")
        axes[0].set_ylabel("Seconds")
        axes[0].grid(axis="y", alpha=0.25)

    availability = summary.pivot_table(
        index="solver",
        columns="backend",
        values="available_rate",
        aggfunc="mean",
    ).fillna(0.0)
    availability.plot(kind="bar", ax=axes[1], rot=20)
    axes[1].set_title("Solver Availability")
    axes[1].set_ylim(0.0, 1.05)
    axes[1].set_ylabel("Rate")
    axes[1].grid(axis="y", alpha=0.25)

    sizes = (
        summary.groupby("family", as_index=False)
        .agg(mean_n_vars=("mean_n_vars", "mean"), mean_n_clauses=("mean_n_clauses", "mean"))
        .sort_values("family")
    )
    x = np.arange(len(sizes))
    width = 0.35
    axes[2].bar(x - width / 2, sizes["mean_n_vars"], width=width, label="Variables")
    axes[2].bar(x + width / 2, sizes["mean_n_clauses"], width=width, label="Clauses")
    axes[2].set_xticks(x)
    axes[2].set_xticklabels(sizes["family"], rotation=15)
    axes[2].set_title("Mean CNF Size")
    axes[2].grid(axis="y", alpha=0.25)
    axes[2].legend()

    plt.tight_layout()
    return fig, axes


def save_figure(fig, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=180, bbox_inches="tight")

