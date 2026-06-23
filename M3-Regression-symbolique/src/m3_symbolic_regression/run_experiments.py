"""Command line runner for the M3 symbolic regression project."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from .baselines import fit_kernel_ridge_baseline, fit_polynomial_baseline
from .datasets import DATASET_BUILDERS, make_dataset
from .metrics import interpretability_score, kolmogorov_proxy
from .plotting import plot_model_comparison, plot_pareto
from .symbolic import PySRSearchConfig, fit_pysr


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="M3 - Regression symbolique avec PySR.")
    parser.add_argument("--datasets", nargs="+", default=list(DATASET_BUILDERS), choices=list(DATASET_BUILDERS))
    parser.add_argument("--output-dir", default="outputs")
    parser.add_argument("--samples", type=int, default=360)
    parser.add_argument("--noise", type=float, default=0.01)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--test-size", type=float, default=0.25)
    parser.add_argument("--skip-pysr", action="store_true", help="Execute seulement les baselines classiques.")
    parser.add_argument("--niterations", type=int, default=40)
    parser.add_argument("--populations", type=int, default=8)
    parser.add_argument("--population-size", type=int, default=24)
    parser.add_argument("--maxsize", type=int, default=24)
    parser.add_argument("--parsimony", type=float, default=0.002)
    parser.add_argument("--timeout", type=float, default=None)
    parser.add_argument("--procs", type=int, default=4)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output_dir)
    data_dir = output_dir / "data"
    results_dir = output_dir / "results"
    figures_dir = output_dir / "figures"
    report_dir = output_dir / "reports"
    for path in [data_dir, results_dir, figures_dir, report_dir]:
        path.mkdir(parents=True, exist_ok=True)

    config = PySRSearchConfig(
        niterations=args.niterations,
        populations=args.populations,
        population_size=args.population_size,
        maxsize=args.maxsize,
        parsimony=args.parsimony,
        timeout_in_seconds=args.timeout,
        random_state=args.seed,
        procs=args.procs,
    )

    all_metrics: list[dict[str, object]] = []
    all_equations: list[pd.DataFrame] = []
    report_lines = [
        "# Rapport M3 - Regression symbolique",
        "",
        "Objectif: decouvrir des equations physiques a partir de donnees, puis comparer precision et parcimonie.",
        "",
        "## Configuration PySR",
        "",
        f"- iterations: {config.niterations}",
        f"- populations: {config.populations}",
        f"- population_size: {config.population_size}",
        f"- maxsize: {config.maxsize}",
        f"- parsimony: {config.parsimony}",
        f"- operateurs binaires: {', '.join(config.binary_operators)}",
        f"- operateurs unaires: {', '.join(config.unary_operators)}",
        "",
    ]

    for offset, dataset_name in enumerate(args.datasets):
        dataset = make_dataset(dataset_name, n_samples=args.samples, noise=args.noise, seed=args.seed + offset)
        df = pd.DataFrame(dataset.X, columns=dataset.feature_names)
        df[dataset.target_name] = dataset.y
        df.to_csv(data_dir / f"{dataset.name}.csv", index=False)

        X_train, X_test, y_train, y_test = train_test_split(
            dataset.X,
            dataset.y,
            test_size=args.test_size,
            random_state=args.seed,
        )

        report_lines.extend(
            [
                f"## Dataset `{dataset.name}`",
                "",
                dataset.description,
                "",
                f"- expression analytique: `{dataset.analytic_expression}`",
                f"- echantillons: {len(dataset.y)}",
                "",
            ]
        )

        baselines = [
            fit_polynomial_baseline(X_train, y_train, X_test, y_test, degree=3),
            fit_kernel_ridge_baseline(X_train, y_train, X_test, y_test),
        ]
        for baseline in baselines:
            all_metrics.append(
                {
                    "dataset": dataset.name,
                    "method": baseline.name,
                    "equation": baseline.expression,
                    "complexity": baseline.complexity,
                    **baseline.metrics,
                }
            )

        if not args.skip_pysr:
            model_dir = output_dir / "pysr_runs" / dataset.name
            _, equations, selected = fit_pysr(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                feature_names=dataset.feature_names,
                output_dir=model_dir,
                config=config,
            )
            equations.insert(0, "dataset", dataset.name)
            all_equations.append(equations)
            equations.to_csv(results_dir / f"{dataset.name}_pysr_equations.csv", index=False)
            plot_pareto(equations, selected, dataset.name, figures_dir / f"{dataset.name}_pareto.png")

            bits = kolmogorov_proxy(selected["sympy"])
            all_metrics.append(
                {
                    "dataset": dataset.name,
                    "method": "pysr_symbolic",
                    "equation": selected["sympy"],
                    "complexity": int(selected["complexity"]),
                    "rmse": float(selected["rmse"]),
                    "mae": float(selected["mae"]),
                    "r2": float(selected["r2"]),
                    "mape": float(selected["mape"]),
                    "kolmogorov_proxy": float(bits),
                    "interpretability": interpretability_score(float(selected["complexity"]), float(bits)),
                }
            )
            report_lines.extend(
                [
                    f"- equation PySR retenue: `{selected['sympy']}`",
                    f"- RMSE test PySR: {float(selected['rmse']):.6g}",
                    f"- complexite PySR: {int(selected['complexity'])}",
                    "",
                ]
            )
        else:
            report_lines.append("- PySR ignore par option `--skip-pysr`.")
            report_lines.append("")

    metrics = pd.DataFrame(all_metrics).sort_values(["dataset", "rmse"])
    metrics.to_csv(results_dir / "metrics.csv", index=False)
    if all_equations:
        pd.concat(all_equations, ignore_index=True).to_csv(results_dir / "all_pysr_equations.csv", index=False)
    plot_model_comparison(metrics, figures_dir / "model_comparison.png")

    report_lines.extend(
        [
            "## Comparaison globale",
            "",
            "```",
            metrics[["dataset", "method", "rmse", "r2", "complexity", "interpretability", "equation"]].to_string(
                index=False
            ),
            "```",
            "",
            "Lecture: PySR cherche une equation explicite, tandis que kernel ridge maximise surtout la precision sans forme analytique lisible.",
        ]
    )
    (report_dir / "report.md").write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Done. Report: {report_dir / 'report.md'}")


if __name__ == "__main__":
    main()
