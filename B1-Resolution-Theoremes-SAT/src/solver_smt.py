from __future__ import annotations

from dataclasses import dataclass
import time
from typing import Any, Mapping

from .domain import SatInstance


@dataclass(frozen=True)
class SmtResult:
    solver: str
    status: str
    satisfiable: bool | None
    wall_time_s: float
    message: str | None = None


def solve_smt_for_instance(instance: SatInstance, time_limit_s: float = 10.0) -> SmtResult:
    metadata = instance.metadata or {}
    if instance.family == "graph_coloring":
        return solve_graph_coloring_smt(metadata, time_limit_s=time_limit_s)
    if instance.family == "pigeonhole":
        return solve_pigeonhole_smt(metadata, time_limit_s=time_limit_s)
    if instance.family == "ramsey_R33":
        return solve_ramsey_smt(metadata, time_limit_s=time_limit_s)
    return SmtResult(
        solver="z3",
        status="UNSUPPORTED",
        satisfiable=None,
        wall_time_s=0.0,
        message=f"no SMT encoding for family {instance.family}",
    )


def solve_graph_coloring_smt(metadata: Mapping[str, Any], time_limit_s: float = 10.0) -> SmtResult:
    start = time.perf_counter()
    try:
        import z3
    except Exception as exc:  # pragma: no cover - depends on optional dependency
        return _unavailable(start, exc)

    n_vertices = int(metadata["n_vertices"])
    k_colors = int(metadata["k_colors"])
    edges = metadata["edges"]
    solver = z3.Solver()
    solver.set("timeout", int(time_limit_s * 1000))

    colors = [z3.Int(f"c_{v}") for v in range(n_vertices)]
    for color in colors:
        solver.add(color >= 0, color < k_colors)
    for u, v in edges:
        solver.add(colors[u] != colors[v])

    return _finish_z3(solver, start)


def solve_pigeonhole_smt(metadata: Mapping[str, Any], time_limit_s: float = 10.0) -> SmtResult:
    start = time.perf_counter()
    try:
        import z3
    except Exception as exc:  # pragma: no cover - depends on optional dependency
        return _unavailable(start, exc)

    n_pigeons = int(metadata["n_pigeons"])
    n_holes = int(metadata["n_holes"])
    solver = z3.Solver()
    solver.set("timeout", int(time_limit_s * 1000))

    holes = [z3.Int(f"h_{p}") for p in range(n_pigeons)]
    for hole in holes:
        solver.add(hole >= 0, hole < n_holes)
    solver.add(z3.Distinct(holes))

    return _finish_z3(solver, start)


def solve_ramsey_smt(metadata: Mapping[str, Any], time_limit_s: float = 10.0) -> SmtResult:
    start = time.perf_counter()
    try:
        import z3
    except Exception as exc:  # pragma: no cover - depends on optional dependency
        return _unavailable(start, exc)

    n_vertices = int(metadata["n_vertices"])
    solver = z3.Solver()
    solver.set("timeout", int(time_limit_s * 1000))

    edge_vars = {}
    for u in range(n_vertices):
        for v in range(u + 1, n_vertices):
            edge_vars[(u, v)] = z3.Bool(f"e_{u}_{v}_red")

    for a in range(n_vertices):
        for b in range(a + 1, n_vertices):
            for c in range(b + 1, n_vertices):
                ab = edge_vars[(a, b)]
                ac = edge_vars[(a, c)]
                bc = edge_vars[(b, c)]
                solver.add(z3.Or(z3.Not(ab), z3.Not(ac), z3.Not(bc)))
                solver.add(z3.Or(ab, ac, bc))

    return _finish_z3(solver, start)


def _finish_z3(solver, start: float) -> SmtResult:
    result = solver.check()
    elapsed = time.perf_counter() - start
    status = str(result).upper()
    if status == "SAT":
        return SmtResult(solver="z3", status="SATISFIABLE", satisfiable=True, wall_time_s=elapsed)
    if status == "UNSAT":
        return SmtResult(solver="z3", status="UNSATISFIABLE", satisfiable=False, wall_time_s=elapsed)
    return SmtResult(solver="z3", status="UNKNOWN", satisfiable=None, wall_time_s=elapsed)


def _unavailable(start: float, exc: Exception) -> SmtResult:
    return SmtResult(
        solver="z3",
        status="UNAVAILABLE",
        satisfiable=None,
        wall_time_s=time.perf_counter() - start,
        message=f"Z3 unavailable: {exc}",
    )

