from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List

from .cnf import CNF


@dataclass(frozen=True)
class SatInstance:
    name: str
    family: str
    cnf: CNF
    expected_sat: bool | None = None
    metadata: Dict[str, Any] | None = None

    def validate(self) -> tuple[bool, str]:
        if not self.name:
            return False, "instance name is empty"
        if not self.family:
            return False, "instance family is empty"
        if self.cnf.n_vars <= 0:
            return False, "CNF has no variables"
        for clause in self.cnf.clauses:
            for lit in clause:
                if lit == 0:
                    return False, "literal 0 is reserved for DIMACS terminators"
                if abs(lit) > self.cnf.n_vars:
                    return False, f"literal {lit} is outside variable range"
        return True, "ok"


@dataclass(frozen=True)
class BenchmarkConfig:
    graph_vertices: List[int]
    pigeon_holes: List[int]
    ramsey_vertices: List[int]
    solver_names: List[str]
    sat_time_limit_s: float = 10.0
    smt_time_limit_s: float = 10.0
    include_smt: bool = True

