from __future__ import annotations

from .encodings import complete_graph, graph_coloring_instance, pigeonhole_instance, ramsey_instance
from .solver_sat import SolveResult, solve_cnf
from .tseitin import And, Atom, Not, Or, to_cnf
from .validation import validate_model


def _assert_status(label: str, result: SolveResult, expected_sat: bool) -> None:
    if result.satisfiable is not expected_sat:
        raise AssertionError(f"{label}: expected SAT={expected_sat}, got {result.status}")
    if expected_sat and not result.valid_model:
        raise AssertionError(f"{label}: model does not satisfy CNF")


def _assert_instance(label: str, instance, expected_sat: bool) -> None:
    result = solve_cnf(instance.cnf, solver_name="auto", time_limit_s=5.0)
    _assert_status(label, result, expected_sat)
    if expected_sat:
        check = validate_model(instance, result.model)
        if not check["feasible"]:
            raise AssertionError(f"{label}: invalid decoded model: {check['violations']}")


def main() -> None:
    contradiction = to_cnf(And([Atom("p"), Not(Atom("p"))])).cnf
    satisfiable_formula = to_cnf(Or([Atom("p"), Atom("q")])).cnf

    _assert_status("Tseitin contradiction", solve_cnf(contradiction, "auto", 5.0), False)
    _assert_status("Tseitin satisfiable formula", solve_cnf(satisfiable_formula, "auto", 5.0), True)

    triangle_3color = graph_coloring_instance(3, complete_graph(3), 3, expected_sat=True)
    triangle_2color = graph_coloring_instance(3, complete_graph(3), 2, expected_sat=False)
    _assert_instance("triangle 3-coloring", triangle_3color, True)
    _assert_instance("triangle 2-coloring", triangle_2color, False)

    _assert_instance("pigeonhole 3 into 2", pigeonhole_instance(3, 2), False)
    _assert_instance("Ramsey R(3,3) n=5", ramsey_instance(5), True)
    _assert_instance("Ramsey R(3,3) n=6", ramsey_instance(6), False)

    print("Smoke test passed.")
    print("Tseitin, graph coloring, pigeonhole and Ramsey encodings are consistent.")


if __name__ == "__main__":
    main()

