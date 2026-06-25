from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Sequence

from .cnf import CNF


class Formula:
    pass


@dataclass(frozen=True)
class Atom(Formula):
    name: str


@dataclass(frozen=True)
class Not(Formula):
    child: Formula


@dataclass(frozen=True)
class And(Formula):
    children: Sequence[Formula]


@dataclass(frozen=True)
class Or(Formula):
    children: Sequence[Formula]


@dataclass(frozen=True)
class Implies(Formula):
    left: Formula
    right: Formula


@dataclass(frozen=True)
class Iff(Formula):
    left: Formula
    right: Formula


@dataclass(frozen=True)
class TseitinResult:
    cnf: CNF
    root: int
    atom_vars: Dict[str, int]


class TseitinEncoder:
    def __init__(self) -> None:
        self.cnf = CNF()
        self.atom_vars: Dict[str, int] = {}

    def encode(self, formula: Formula, assert_root: bool = True) -> TseitinResult:
        root = self._encode(formula)
        if assert_root:
            self.cnf.add_clause([root])
        return TseitinResult(cnf=self.cnf, root=root, atom_vars=dict(self.atom_vars))

    def _atom(self, name: str) -> int:
        if name not in self.atom_vars:
            self.atom_vars[name] = self.cnf.new_var(name)
        return self.atom_vars[name]

    def _encode(self, formula: Formula) -> int:
        if isinstance(formula, Atom):
            return self._atom(formula.name)
        if isinstance(formula, Not):
            return self._encode_not(formula.child)
        if isinstance(formula, And):
            return self._encode_and(formula.children)
        if isinstance(formula, Or):
            return self._encode_or(formula.children)
        if isinstance(formula, Implies):
            return self._encode(Or([Not(formula.left), formula.right]))
        if isinstance(formula, Iff):
            return self._encode(
                And(
                    [
                        Implies(formula.left, formula.right),
                        Implies(formula.right, formula.left),
                    ]
                )
            )
        raise TypeError(f"unsupported formula type: {type(formula)!r}")

    def _encode_not(self, child: Formula) -> int:
        child_var = self._encode(child)
        out = self.cnf.new_var(f"aux_not_{child_var}")
        self.cnf.add_clause([-out, -child_var])
        self.cnf.add_clause([out, child_var])
        return out

    def _encode_and(self, children: Sequence[Formula]) -> int:
        child_vars = [self._encode(child) for child in children]
        out = self.cnf.new_var("aux_and")
        if not child_vars:
            self.cnf.add_clause([out])
            return out
        for child_var in child_vars:
            self.cnf.add_clause([-out, child_var])
        self.cnf.add_clause([out] + [-child_var for child_var in child_vars])
        return out

    def _encode_or(self, children: Sequence[Formula]) -> int:
        child_vars = [self._encode(child) for child in children]
        out = self.cnf.new_var("aux_or")
        if not child_vars:
            self.cnf.add_clause([-out])
            return out
        self.cnf.add_clause([-out] + child_vars)
        for child_var in child_vars:
            self.cnf.add_clause([out, -child_var])
        return out


def to_cnf(formula: Formula, assert_root: bool = True) -> TseitinResult:
    return TseitinEncoder().encode(formula, assert_root=assert_root)

