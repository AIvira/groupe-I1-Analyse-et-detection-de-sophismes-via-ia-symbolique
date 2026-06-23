from __future__ import annotations

import unittest

import numpy as np
import pandas as pd

from m3_symbolic_regression.datasets import make_dataset
from m3_symbolic_regression.metrics import kolmogorov_proxy, pareto_front, regression_metrics


class DatasetTests(unittest.TestCase):
    def test_reference_datasets_have_expected_shapes(self) -> None:
        for name in ["gravity", "ideal_gas", "pendulum"]:
            dataset = make_dataset(name, n_samples=25, noise=0.0, seed=123)
            self.assertEqual(dataset.X.shape[0], 25)
            self.assertEqual(dataset.y.shape, (25,))
            self.assertEqual(dataset.X.shape[1], len(dataset.feature_names))

    def test_gravity_matches_analytic_law_without_noise(self) -> None:
        dataset = make_dataset("gravity", n_samples=10, noise=0.0, seed=7)
        m1, m2, r = dataset.X.T
        np.testing.assert_allclose(dataset.y, m1 * m2 / (r**2))


class MetricTests(unittest.TestCase):
    def test_regression_metrics(self) -> None:
        values = regression_metrics(np.array([1.0, 2.0]), np.array([1.0, 3.0]))
        self.assertAlmostEqual(values["rmse"], 2**-0.5)
        self.assertIn("r2", values)

    def test_pareto_front_keeps_non_dominated_points(self) -> None:
        frame = pd.DataFrame(
            {
                "complexity": [1, 2, 3, 4],
                "rmse": [10.0, 8.0, 9.0, 6.0],
            }
        )
        front = pareto_front(frame)
        self.assertEqual(front["complexity"].tolist(), [1, 2, 4])

    def test_kolmogorov_proxy_is_positive(self) -> None:
        self.assertGreater(kolmogorov_proxy("m1*m2/r**2"), 0)


if __name__ == "__main__":
    unittest.main()

