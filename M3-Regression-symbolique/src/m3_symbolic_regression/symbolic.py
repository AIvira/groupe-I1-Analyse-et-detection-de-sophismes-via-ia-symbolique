"""PySR symbolic regression orchestration."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from .metrics import (
    interpretability_score,
    kolmogorov_proxy,
    pareto_front,
    regression_metrics,
    select_balanced_equation,
    sympy_complexity,
)


@dataclass(frozen=True)
class PySRSearchConfig:
    """Relevant genetic programming hyperparameters for PySR."""

    niterations: int = 40
    populations: int = 8
    population_size: int = 24
    maxsize: int = 24
    parsimony: float = 0.002
    timeout_in_seconds: float | None = None
    random_state: int = 42
    procs: int = 4
    precision: int = 32
    unary_operators: tuple[str, ...] = ("sin", "sqrt")
    binary_operators: tuple[str, ...] = ("+", "-", "*", "/")


def fit_pysr(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray,
    y_test: np.ndarray,
    feature_names: list[str],
    output_dir: Path,
    config: PySRSearchConfig,
) -> tuple[Any, pd.DataFrame, pd.Series]:
    """Fit PySR and return model, equation table and selected Pareto equation."""

    from pysr import PySRRegressor

    output_dir.mkdir(parents=True, exist_ok=True)
    parallel_kwargs = (
        {"parallelism": "multiprocessing", "procs": max(1, config.procs)}
        if config.procs > 1
        else {"parallelism": "serial"}
    )
    model = PySRRegressor(
        niterations=config.niterations,
        populations=config.populations,
        population_size=config.population_size,
        maxsize=config.maxsize,
        parsimony=config.parsimony,
        timeout_in_seconds=config.timeout_in_seconds,
        binary_operators=list(config.binary_operators),
        unary_operators=list(config.unary_operators),
        complexity_of_operators={
            "+": 1,
            "-": 1,
            "*": 1,
            "/": 2,
            "sin": 3,
            "sqrt": 3,
        },
        constraints={"/": (-1, 5), "sqrt": 5},
        model_selection="best",
        elementwise_loss="loss(x, y) = (x - y)^2",
        tournament_selection_n=max(2, min(15, config.population_size - 1)),
        topn=max(1, min(12, config.population_size)),
        precision=config.precision,
        deterministic=config.procs == 1,
        random_state=config.random_state,
        verbosity=0,
        progress=False,
        output_directory=str(output_dir),
        temp_equation_file=False,
        delete_tempfiles=True,
        **parallel_kwargs,
    )
    model.fit(X_train, y_train, variable_names=feature_names)
    equations = _equation_frame(model, X_test, y_test)
    front = pareto_front(equations, complexity_col="complexity", error_col="rmse")
    selected = select_balanced_equation(front, complexity_col="complexity", error_col="rmse")
    return model, equations, selected


def _equation_frame(model: Any, X_test: np.ndarray, y_test: np.ndarray) -> pd.DataFrame:
    raw = model.equations_.copy()
    rows: list[dict[str, Any]] = []
    for equation_index, row in raw.iterrows():
        try:
            y_pred = model.predict(X_test, index=int(equation_index))
            values = regression_metrics(y_test, y_pred)
        except Exception:
            values = {"rmse": np.nan, "mae": np.nan, "r2": np.nan, "mape": np.nan}
        
        expression = row.get("sympy_format", row.get("equation", ""))
        complexity = int(row.get("complexity", sympy_complexity(expression)))
        bits = kolmogorov_proxy(expression)
        values["kolmogorov_proxy"] = float(bits)
        values["interpretability"] = interpretability_score(complexity, bits)
        rows.append(
            {
                "equation_index": int(equation_index),
                "equation": str(row.get("equation", expression)),
                "sympy": str(expression),
                "complexity": complexity,
                "pysr_loss": float(row.get("loss", np.nan)),
                "pysr_score": float(row.get("score", np.nan)),
                **values,
            }
        )
    return pd.DataFrame(rows).dropna(subset=["rmse"]).sort_values(["complexity", "rmse"]).reset_index(drop=True)
