"""Synthetic physics reference datasets for symbolic regression."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np


@dataclass(frozen=True)
class PhysicsDataset:
    """Container for a generated physics law dataset."""

    name: str
    X: np.ndarray
    y: np.ndarray
    feature_names: list[str]
    target_name: str
    analytic_expression: str
    description: str


def _with_relative_noise(y: np.ndarray, relative_noise: float, rng: np.random.Generator) -> np.ndarray:
    if relative_noise <= 0:
        return y.copy()
    scale = np.std(y)
    return y + rng.normal(0.0, relative_noise * scale, size=y.shape)


def make_gravity(n_samples: int = 500, noise: float = 0.01, seed: int = 42) -> PhysicsDataset:
    """Newton gravity in normalized units: F = m1 * m2 / r^2."""

    rng = np.random.default_rng(seed)
    m1 = rng.uniform(1.0, 10.0, n_samples)
    m2 = rng.uniform(1.0, 10.0, n_samples)
    r = rng.uniform(0.7, 5.0, n_samples)
    y_clean = m1 * m2 / (r**2)
    X = np.column_stack([m1, m2, r])
    return PhysicsDataset(
        name="gravity",
        X=X,
        y=_with_relative_noise(y_clean, noise, rng),
        feature_names=["m1", "m2", "r"],
        target_name="F",
        analytic_expression="m1*m2/r**2",
        description="Loi de gravitation en unites normalisees, constante G=1.",
    )


def make_ideal_gas(n_samples: int = 500, noise: float = 0.01, seed: int = 43) -> PhysicsDataset:
    """Ideal gas law in normalized units: P = n * T / V."""

    rng = np.random.default_rng(seed)
    n = rng.uniform(0.5, 5.0, n_samples)
    temperature = rng.uniform(250.0, 500.0, n_samples)
    volume = rng.uniform(1.0, 12.0, n_samples)
    y_clean = n * temperature / volume
    X = np.column_stack([n, temperature, volume])
    return PhysicsDataset(
        name="ideal_gas",
        X=X,
        y=_with_relative_noise(y_clean, noise, rng),
        feature_names=["n", "T", "V"],
        target_name="P",
        analytic_expression="n*T/V",
        description="Loi des gaz parfaits en unites normalisees, constante R=1.",
    )


def make_pendulum(n_samples: int = 500, noise: float = 0.01, seed: int = 44) -> PhysicsDataset:
    """Pendulum angular acceleration: alpha = -(g / L) * sin(theta)."""

    rng = np.random.default_rng(seed)
    theta = rng.uniform(-2.6, 2.6, n_samples)
    g = rng.uniform(2.0, 20.0, n_samples)
    length = rng.uniform(0.4, 3.0, n_samples)
    y_clean = -(g / length) * np.sin(theta)
    X = np.column_stack([theta, g, length])
    return PhysicsDataset(
        name="pendulum",
        X=X,
        y=_with_relative_noise(y_clean, noise, rng),
        feature_names=["theta", "g", "L"],
        target_name="alpha",
        analytic_expression="-(g/L)*sin(theta)",
        description="Acceleration angulaire du pendule simple sans frottement, avec g varie pour identifier son role.",
    )


DATASET_BUILDERS: dict[str, Callable[[int, float, int], PhysicsDataset]] = {
    "gravity": make_gravity,
    "ideal_gas": make_ideal_gas,
    "pendulum": make_pendulum,
}


def make_dataset(name: str, n_samples: int = 500, noise: float = 0.01, seed: int = 42) -> PhysicsDataset:
    """Create one named dataset."""

    try:
        builder = DATASET_BUILDERS[name]
    except KeyError as exc:
        available = ", ".join(sorted(DATASET_BUILDERS))
        raise ValueError(f"Unknown dataset '{name}'. Available: {available}") from exc
    return builder(n_samples=n_samples, noise=noise, seed=seed)


def make_all_datasets(n_samples: int = 500, noise: float = 0.01, seed: int = 42) -> list[PhysicsDataset]:
    """Create all reference datasets with deterministic, distinct seeds."""

    return [
        make_dataset(name, n_samples=n_samples, noise=noise, seed=seed + offset)
        for offset, name in enumerate(DATASET_BUILDERS)
    ]
