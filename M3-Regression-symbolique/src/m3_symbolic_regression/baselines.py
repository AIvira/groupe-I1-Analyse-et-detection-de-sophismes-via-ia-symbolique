"""Classical regression baselines for comparison with symbolic regression."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import RidgeCV
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

from .metrics import interpretability_score, kolmogorov_proxy, regression_metrics


@dataclass
class BaselineResult:
    name: str
    model: object
    metrics: dict[str, float]
    complexity: int
    expression: str


def fit_polynomial_baseline(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray,
    y_test: np.ndarray,
    degree: int = 3,
) -> BaselineResult:
    """Fit polynomial features with ridge regularization."""

    model = Pipeline(
        [
            ("scale", StandardScaler()),
            ("poly", PolynomialFeatures(degree=degree, include_bias=False)),
            ("ridge", RidgeCV(alphas=np.logspace(-6, 3, 12))),
        ]
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    ridge = model.named_steps["ridge"]
    non_zero = int(np.sum(np.abs(ridge.coef_) > 1e-10))
    expression = f"Ridge polynomial degree {degree} with {non_zero} active coefficients"
    values = regression_metrics(y_test, y_pred)
    bits = kolmogorov_proxy(expression)
    values["kolmogorov_proxy"] = float(bits)
    values["interpretability"] = interpretability_score(non_zero, bits)
    return BaselineResult(
        name=f"polynomial_degree_{degree}",
        model=model,
        metrics=values,
        complexity=non_zero,
        expression=expression,
    )


def fit_kernel_ridge_baseline(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_test: np.ndarray,
    y_test: np.ndarray,
) -> BaselineResult:
    """Fit an RBF kernel ridge model with a compact grid search."""

    model = Pipeline(
        [
            ("scale", StandardScaler()),
            (
                "krr",
                GridSearchCV(
                    KernelRidge(kernel="rbf"),
                    param_grid={
                        "alpha": [1e-4, 1e-3, 1e-2, 1e-1],
                        "gamma": [0.1, 0.5, 1.0, 2.0],
                    },
                    scoring="neg_root_mean_squared_error",
                    cv=3,
                ),
            ),
        ]
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    complexity = int(X_train.shape[0])
    best = model.named_steps["krr"].best_params_
    expression = f"Kernel ridge RBF alpha={best['alpha']} gamma={best['gamma']}"
    values = regression_metrics(y_test, y_pred)
    bits = kolmogorov_proxy(expression)
    values["kolmogorov_proxy"] = float(bits)
    values["interpretability"] = interpretability_score(complexity, bits)
    return BaselineResult(
        name="kernel_ridge_rbf",
        model=model,
        metrics=values,
        complexity=complexity,
        expression=expression,
    )

