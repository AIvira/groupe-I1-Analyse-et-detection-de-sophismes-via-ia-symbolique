from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Mapping


Literal = int
Clause = List[Literal]


@dataclass
class CNF:
    n_vars: int = 0
    clauses: List[Clause] = field(default_factory=list)
    var_names: Dict[int, str] = field(default_factory=dict)

    def new_var(self, name: str | None = None) -> int:
        self.n_vars += 1
        if name:
            self.var_names[self.n_vars] = name
        return self.n_vars

    def add_clause(self, literals: Iterable[int]) -> None:
        clause = [int(lit) for lit in literals]
        if not clause:
            self.clauses.append([])
            return
        max_var = max(abs(lit) for lit in clause)
        if max_var > self.n_vars:
            self.n_vars = max_var
        self.clauses.append(clause)

    def extend(self, clauses: Iterable[Iterable[int]]) -> None:
        for clause in clauses:
            self.add_clause(clause)

    def copy(self) -> "CNF":
        return CNF(
            n_vars=self.n_vars,
            clauses=[clause[:] for clause in self.clauses],
            var_names=dict(self.var_names),
        )

    def to_dimacs(self, include_comments: bool = True) -> str:
        lines: List[str] = []
        if include_comments:
            for idx in sorted(self.var_names):
                lines.append(f"c var {idx} {self.var_names[idx]}")
        lines.append(f"p cnf {self.n_vars} {len(self.clauses)}")
        for clause in self.clauses:
            lines.append(" ".join(str(lit) for lit in clause) + " 0")
        return "\n".join(lines) + "\n"

    def save_dimacs(self, path, include_comments: bool = True) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.to_dimacs(include_comments=include_comments), encoding="utf-8")


def exactly_one(cnf: CNF, literals: Iterable[int]) -> None:
    lits = list(literals)
    cnf.add_clause(lits)
    at_most_one_pairwise(cnf, lits)


def at_most_one_pairwise(cnf: CNF, literals: Iterable[int]) -> None:
    lits = list(literals)
    for i, left in enumerate(lits):
        for right in lits[i + 1 :]:
            cnf.add_clause([-left, -right])


def model_to_assignment(model: Iterable[int] | Mapping[int, bool] | None) -> Dict[int, bool]:
    if model is None:
        return {}
    if isinstance(model, Mapping):
        return {int(var): bool(value) for var, value in model.items()}
    assignment: Dict[int, bool] = {}
    for lit in model:
        if lit != 0:
            assignment[abs(int(lit))] = int(lit) > 0
    return assignment


def clause_satisfied(clause: Clause, assignment: Mapping[int, bool]) -> bool:
    return any(assignment.get(abs(lit), False) == (lit > 0) for lit in clause)


def cnf_satisfied(cnf: CNF, model: Iterable[int] | Mapping[int, bool] | None) -> bool:
    assignment = model_to_assignment(model)
    return all(clause_satisfied(clause, assignment) for clause in cnf.clauses)

