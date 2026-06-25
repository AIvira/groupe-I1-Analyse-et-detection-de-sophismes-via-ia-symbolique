from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

from src.encodings import pigeonhole_instance
from src.experiments import (
    build_default_config,
    build_instances,
    export_dimacs_examples,
    export_results,
    run_benchmark,
    summarize,
)
from src.plotting import plot_benchmark_summary, save_figure
from src.proof import export_pysat_proof, verify_with_drat_trim


def try_export_unsat_proof(out_dir: Path) -> None:
    proof_dir = out_dir / "proofs"
    instance = pigeonhole_instance(n_pigeons=4, n_holes=3, name="php_4_into_3")
    result, export_status = export_pysat_proof(
        instance=instance,
        out_dir=proof_dir,
        solver_name="glucose4",
        time_limit_s=10.0,
    )

    print(f"Proof export ({result.solver}): {export_status.status}")
    if export_status.message:
        print(f"Proof export detail: {export_status.message}")
    if export_status.proof_path is None:
        return

    cnf_path = proof_dir / f"{instance.name}.cnf"
    check = verify_with_drat_trim(cnf_path, export_status.proof_path)
    print(f"DRAT-trim check: {check.status}")
    if check.message:
        print(f"DRAT-trim detail: {check.message}")


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    out_dir = project_dir / "results"
    fig_dir = out_dir / "figures"

    config = build_default_config()
    instances = build_instances(config)

    raw = run_benchmark(config)
    summary = summarize(raw)
    export_results(raw, summary, out_dir)
    export_dimacs_examples(instances, out_dir / "dimacs")

    fig, _ = plot_benchmark_summary(summary)
    save_figure(fig, fig_dir / "benchmark_overview.png")
    save_figure(fig, project_dir / "benchmark_overview.png")
    plt.close(fig)

    try_export_unsat_proof(out_dir)

    print("Benchmark complete.")
    print(f"Raw results : {out_dir / 'benchmark_raw.csv'}")
    print(f"Summary     : {out_dir / 'benchmark_summary.csv'}")
    print(f"DIMACS      : {out_dir / 'dimacs'}")
    print(f"Figure      : {fig_dir / 'benchmark_overview.png'}")
    print(f"Root figure : {project_dir / 'benchmark_overview.png'}")


if __name__ == "__main__":
    main()
