from __future__ import annotations

from pathlib import Path
from typing import Iterable, List

import numpy as np
import pandas as pd

from .domain import BenchmarkConfig, SatInstance
from .encodings import default_benchmark_instances
from .solver_sat import SolveResult, solve_cnf
from .solver_smt import solve_smt_for_instance
from .validation import validate_model


def build_default_config() -> BenchmarkConfig:
    return BenchmarkConfig(
        graph_vertices=[5, 6, 7, 8],
        pigeon_holes=[3, 4, 5],
        ramsey_vertices=[4, 5, 6],
        solver_names=["glucose3", "cadical153", "lingeling", "dpll"],
        sat_time_limit_s=10.0,
        smt_time_limit_s=10.0,
        include_smt=True,
    )


def build_instances(config: BenchmarkConfig) -> List[SatInstance]:
    return default_benchmark_instances(
        graph_vertices=config.graph_vertices,
        pigeon_holes=config.pigeon_holes,
        ramsey_vertices=config.ramsey_vertices,
    )


def run_single_sat(instance: SatInstance, solver_name: str, time_limit_s: float) -> dict:
    result = solve_cnf(instance.cnf, solver_name=solver_name, time_limit_s=time_limit_s)
    validation = validate_model(instance, result.model) if result.satisfiable else {"feasible": None, "violations": []}
    expected_ok = (
        None
        if instance.expected_sat is None or result.satisfiable is None
        else bool(instance.expected_sat == result.satisfiable)
    )
    return _base_row(instance) | {
        "backend": "SAT",
        "solver": result.solver,
        "status": result.status,
        "satisfiable": result.satisfiable,
        "expected_ok": expected_ok,
        "valid_model": validation["feasible"],
        "time_s": result.wall_time_s,
        "message": result.message,
    }


def run_single_smt(instance: SatInstance, time_limit_s: float) -> dict:
    result = solve_smt_for_instance(instance, time_limit_s=time_limit_s)
    expected_ok = (
        None
        if instance.expected_sat is None or result.satisfiable is None
        else bool(instance.expected_sat == result.satisfiable)
    )
    return _base_row(instance) | {
        "backend": "SMT",
        "solver": result.solver,
        "status": result.status,
        "satisfiable": result.satisfiable,
        "expected_ok": expected_ok,
        "valid_model": None,
        "time_s": result.wall_time_s,
        "message": result.message,
    }


def run_benchmark(config: BenchmarkConfig) -> pd.DataFrame:
    rows = []
    for instance in build_instances(config):
        ok, message = instance.validate()
        if not ok:
            raise ValueError(f"invalid instance {instance.name}: {message}")
        for solver_name in config.solver_names:
            rows.append(run_single_sat(instance, solver_name, config.sat_time_limit_s))
        if config.include_smt:
            rows.append(run_single_smt(instance, config.smt_time_limit_s))
    return pd.DataFrame(rows)


def summarize(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return pd.DataFrame()

    solved_statuses = {"SATISFIABLE", "UNSATISFIABLE"}
    data = df.copy()
    data["solved"] = data["status"].isin(solved_statuses)
    data["available"] = data["status"] != "UNAVAILABLE"
    data["time_for_solved"] = data["time_s"].where(data["solved"], np.nan)
    data["expected_ok_num"] = data["expected_ok"].map({True: 1.0, False: 0.0})

    summary = (
        data.groupby(["backend", "solver", "family"], as_index=False)
        .agg(
            instances=("instance_name", "count"),
            available_rate=("available", "mean"),
            solved_rate=("solved", "mean"),
            expected_ok_rate=("expected_ok_num", _nanmean),
            mean_time_s=("time_for_solved", _nanmean),
            mean_n_vars=("n_vars", "mean"),
            mean_n_clauses=("n_clauses", "mean"),
        )
        .sort_values(["backend", "solver", "family"])
        .reset_index(drop=True)
    )
    return summary


def export_results(df: pd.DataFrame, summary: pd.DataFrame, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_dir / "benchmark_raw.csv", index=False)
    summary.to_csv(out_dir / "benchmark_summary.csv", index=False)


def export_dimacs_examples(instances: Iterable[SatInstance], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    seen = set()
    for instance in instances:
        if instance.family in seen:
            continue
        seen.add(instance.family)
        instance.cnf.save_dimacs(out_dir / f"{instance.name}.cnf")


def _base_row(instance: SatInstance) -> dict:
    metadata = instance.metadata or {}
    return {
        "instance_name": instance.name,
        "family": instance.family,
        "expected_sat": instance.expected_sat,
        "n_vars": instance.cnf.n_vars,
        "n_clauses": len(instance.cnf.clauses),
        "size": _size_label(instance),
        "metadata": {key: value for key, value in metadata.items() if key != "var_map"},
    }


def _size_label(instance: SatInstance) -> int:
    metadata = instance.metadata or {}
    if "n_vertices" in metadata:
        return int(metadata["n_vertices"])
    if "n_holes" in metadata:
        return int(metadata["n_holes"])
    return instance.cnf.n_vars


def _nanmean(values: Iterable[float]) -> float:
    arr = np.asarray(list(values), dtype=float)
    if arr.size == 0:
        return np.nan
    valid = arr[~np.isnan(arr)]
    if valid.size == 0:
        return np.nan
    return float(valid.mean())

