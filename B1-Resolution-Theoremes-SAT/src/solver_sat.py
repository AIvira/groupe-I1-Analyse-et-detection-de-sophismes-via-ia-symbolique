from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
import time
from typing import Dict, Iterable, List

from .cnf import CNF, cnf_satisfied


@dataclass(frozen=True)
class SolveResult:
    solver: str
    status: str
    satisfiable: bool | None
    model: List[int] | None
    wall_time_s: float
    n_vars: int
    n_clauses: int
    valid_model: bool | None = None
    proof_lines: List[str] | None = None
    message: str | None = None


def solve_cnf(
    cnf: CNF,
    solver_name: str = "auto",
    time_limit_s: float | None = 10.0,
    with_proof: bool = False,
) -> SolveResult:
    normalized = solver_name.lower()
    if normalized == "auto":
        pysat_result = solve_with_pysat(cnf, "glucose3", time_limit_s=time_limit_s, with_proof=with_proof)
        if pysat_result.status != "UNAVAILABLE":
            return pysat_result
        return solve_dpll(cnf, time_limit_s=time_limit_s)
    if normalized in {"dpll", "dpll_fallback"}:
        return solve_dpll(cnf, time_limit_s=time_limit_s)
    return solve_with_pysat(cnf, normalized, time_limit_s=time_limit_s, with_proof=with_proof)


def solve_with_pysat(
    cnf: CNF,
    solver_name: str,
    time_limit_s: float | None = 10.0,
    with_proof: bool = False,
) -> SolveResult:
    start = time.perf_counter()
    try:
        from pysat.solvers import Solver
    except Exception as exc:  # pragma: no cover - depends on local optional dependency
        return SolveResult(
            solver=solver_name,
            status="UNAVAILABLE",
            satisfiable=None,
            model=None,
            wall_time_s=time.perf_counter() - start,
            n_vars=cnf.n_vars,
            n_clauses=len(cnf.clauses),
            message=f"PySAT unavailable: {exc}",
        )

    try:
        with Solver(
            name=solver_name,
            bootstrap_with=cnf.clauses,
            use_timer=True,
            with_proof=with_proof,
        ) as solver:
            sat = solver.solve()
            elapsed = time.perf_counter() - start
            model = solver.get_model() if sat else None
            proof_lines = None
            if with_proof and sat is False:
                try:
                    proof_lines = list(solver.get_proof() or [])
                except Exception:
                    proof_lines = None
    except TypeError:
        try:
            with Solver(name=solver_name, bootstrap_with=cnf.clauses, use_timer=True) as solver:
                sat = solver.solve()
                elapsed = time.perf_counter() - start
                model = solver.get_model() if sat else None
                proof_lines = None
        except Exception as exc:  # pragma: no cover - depends on installed solvers
            return _unavailable(cnf, solver_name, start, exc)
    except Exception as exc:  # pragma: no cover - depends on installed solvers
        return _unavailable(cnf, solver_name, start, exc)

    valid_model = cnf_satisfied(cnf, model) if sat and model is not None else None
    return SolveResult(
        solver=solver_name,
        status="SATISFIABLE" if sat else "UNSATISFIABLE",
        satisfiable=bool(sat),
        model=model,
        wall_time_s=elapsed,
        n_vars=cnf.n_vars,
        n_clauses=len(cnf.clauses),
        valid_model=valid_model,
        proof_lines=proof_lines,
        message=None if time_limit_s is None else "PySAT solve() does not enforce a wall-clock timeout in this wrapper",
    )


def _unavailable(cnf: CNF, solver_name: str, start: float, exc: Exception) -> SolveResult:
    return SolveResult(
        solver=solver_name,
        status="UNAVAILABLE",
        satisfiable=None,
        model=None,
        wall_time_s=time.perf_counter() - start,
        n_vars=cnf.n_vars,
        n_clauses=len(cnf.clauses),
        message=str(exc),
    )


def solve_dpll(cnf: CNF, time_limit_s: float | None = 10.0) -> SolveResult:
    start = time.perf_counter()
    deadline = None if time_limit_s is None else start + time_limit_s
    clauses = [clause[:] for clause in cnf.clauses]

    try:
        assignment = _dpll(clauses, {}, deadline)
    except TimeoutError:
        return SolveResult(
            solver="dpll_fallback",
            status="TIMEOUT",
            satisfiable=None,
            model=None,
            wall_time_s=time.perf_counter() - start,
            n_vars=cnf.n_vars,
            n_clauses=len(cnf.clauses),
            message="DPLL fallback reached the time limit",
        )

    elapsed = time.perf_counter() - start
    if assignment is None:
        return SolveResult(
            solver="dpll_fallback",
            status="UNSATISFIABLE",
            satisfiable=False,
            model=None,
            wall_time_s=elapsed,
            n_vars=cnf.n_vars,
            n_clauses=len(cnf.clauses),
        )

    model = [var if assignment.get(var, False) else -var for var in range(1, cnf.n_vars + 1)]
    return SolveResult(
        solver="dpll_fallback",
        status="SATISFIABLE",
        satisfiable=True,
        model=model,
        wall_time_s=elapsed,
        n_vars=cnf.n_vars,
        n_clauses=len(cnf.clauses),
        valid_model=cnf_satisfied(cnf, model),
    )


def _dpll(
    clauses: List[List[int]],
    assignment: Dict[int, bool],
    deadline: float | None,
) -> Dict[int, bool] | None:
    _check_deadline(deadline)
    propagated = _propagate(clauses, assignment, deadline)
    if propagated is None:
        return None
    clauses, assignment = propagated
    if not clauses:
        return assignment

    branch_var = _choose_branch_var(clauses, assignment)
    for value in (True, False):
        next_assignment = dict(assignment)
        next_assignment[branch_var] = value
        lit = branch_var if value else -branch_var
        simplified = _apply_literal(clauses, lit)
        if simplified is None:
            continue
        result = _dpll(simplified, next_assignment, deadline)
        if result is not None:
            return result
    return None


def _propagate(
    clauses: List[List[int]],
    assignment: Dict[int, bool],
    deadline: float | None,
) -> tuple[List[List[int]], Dict[int, bool]] | None:
    clauses = [clause[:] for clause in clauses]
    assignment = dict(assignment)
    changed = True

    while changed:
        _check_deadline(deadline)
        changed = False

        unit = _find_unit_clause(clauses)
        if unit is not None:
            if not _assign_literal(assignment, unit):
                return None
            clauses = _apply_literal(clauses, unit)
            if clauses is None:
                return None
            changed = True
            continue

        pure_literals = _find_pure_literals(clauses, assignment)
        if pure_literals:
            for lit in pure_literals:
                if not _assign_literal(assignment, lit):
                    return None
                clauses = _apply_literal(clauses, lit)
                if clauses is None:
                    return None
            changed = True

    return clauses, assignment


def _find_unit_clause(clauses: Iterable[List[int]]) -> int | None:
    for clause in clauses:
        if len(clause) == 0:
            return None
        if len(clause) == 1:
            return clause[0]
    return None


def _find_pure_literals(clauses: Iterable[List[int]], assignment: Dict[int, bool]) -> List[int]:
    signs: Dict[int, set[bool]] = {}
    for clause in clauses:
        for lit in clause:
            var = abs(lit)
            if var not in assignment:
                signs.setdefault(var, set()).add(lit > 0)
    return [var if next(iter(values)) else -var for var, values in signs.items() if len(values) == 1]


def _assign_literal(assignment: Dict[int, bool], lit: int) -> bool:
    var = abs(lit)
    value = lit > 0
    previous = assignment.get(var)
    if previous is not None and previous != value:
        return False
    assignment[var] = value
    return True


def _apply_literal(clauses: List[List[int]], lit: int) -> List[List[int]] | None:
    simplified: List[List[int]] = []
    negated = -lit
    for clause in clauses:
        if lit in clause:
            continue
        reduced = [candidate for candidate in clause if candidate != negated]
        if not reduced:
            return None
        simplified.append(reduced)
    return simplified


def _choose_branch_var(clauses: Iterable[List[int]], assignment: Dict[int, bool]) -> int:
    counts = Counter(abs(lit) for clause in clauses for lit in clause if abs(lit) not in assignment)
    if not counts:
        return 1
    return counts.most_common(1)[0][0]


def _check_deadline(deadline: float | None) -> None:
    if deadline is not None and time.perf_counter() > deadline:
        raise TimeoutError
