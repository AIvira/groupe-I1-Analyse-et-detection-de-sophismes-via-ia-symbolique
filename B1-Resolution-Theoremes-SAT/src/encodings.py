from __future__ import annotations

from itertools import combinations
from random import Random
from typing import Iterable, List, Tuple

from .cnf import CNF, exactly_one
from .domain import SatInstance


Edge = Tuple[int, int]


def normalize_edges(edges: Iterable[Edge]) -> List[Edge]:
    normalized = {tuple(sorted((int(u), int(v)))) for u, v in edges if int(u) != int(v)}
    return sorted(normalized)


def cycle_graph(n_vertices: int) -> List[Edge]:
    return normalize_edges((i, (i + 1) % n_vertices) for i in range(n_vertices))


def complete_graph(n_vertices: int) -> List[Edge]:
    return normalize_edges(combinations(range(n_vertices), 2))


def random_graph(n_vertices: int, density: float, seed: int) -> List[Edge]:
    rng = Random(seed)
    edges = []
    for u, v in combinations(range(n_vertices), 2):
        if rng.random() <= density:
            edges.append((u, v))
    return normalize_edges(edges)


def graph_coloring_instance(
    n_vertices: int,
    edges: Iterable[Edge],
    k_colors: int,
    name: str | None = None,
    expected_sat: bool | None = None,
) -> SatInstance:
    cnf = CNF()
    edges = normalize_edges(edges)
    color_vars: dict[tuple[int, int], int] = {}

    for vertex in range(n_vertices):
        literals = []
        for color in range(k_colors):
            var = cnf.new_var(f"x_v{vertex}_c{color}")
            color_vars[(vertex, color)] = var
            literals.append(var)
        exactly_one(cnf, literals)

    for u, v in edges:
        for color in range(k_colors):
            cnf.add_clause([-color_vars[(u, color)], -color_vars[(v, color)]])

    instance_name = name or f"graph_coloring_n{n_vertices}_k{k_colors}"
    return SatInstance(
        name=instance_name,
        family="graph_coloring",
        cnf=cnf,
        expected_sat=expected_sat,
        metadata={
            "n_vertices": n_vertices,
            "edges": edges,
            "k_colors": k_colors,
            "var_map": color_vars,
        },
    )


def pigeonhole_instance(n_pigeons: int, n_holes: int, name: str | None = None) -> SatInstance:
    cnf = CNF()
    assign_vars: dict[tuple[int, int], int] = {}

    for pigeon in range(n_pigeons):
        literals = []
        for hole in range(n_holes):
            var = cnf.new_var(f"x_p{pigeon}_h{hole}")
            assign_vars[(pigeon, hole)] = var
            literals.append(var)
        exactly_one(cnf, literals)

    for left, right in combinations(range(n_pigeons), 2):
        for hole in range(n_holes):
            cnf.add_clause([-assign_vars[(left, hole)], -assign_vars[(right, hole)]])

    instance_name = name or f"pigeonhole_p{n_pigeons}_h{n_holes}"
    return SatInstance(
        name=instance_name,
        family="pigeonhole",
        cnf=cnf,
        expected_sat=n_pigeons <= n_holes,
        metadata={
            "n_pigeons": n_pigeons,
            "n_holes": n_holes,
            "var_map": assign_vars,
        },
    )


def ramsey_instance(n_vertices: int, name: str | None = None) -> SatInstance:
    cnf = CNF()
    edge_vars: dict[tuple[int, int], int] = {}

    for u, v in combinations(range(n_vertices), 2):
        edge_vars[(u, v)] = cnf.new_var(f"e_{u}_{v}_red")

    for a, b, c in combinations(range(n_vertices), 3):
        ab = edge_vars[tuple(sorted((a, b)))]
        ac = edge_vars[tuple(sorted((a, c)))]
        bc = edge_vars[tuple(sorted((b, c)))]
        cnf.add_clause([-ab, -ac, -bc])
        cnf.add_clause([ab, ac, bc])

    instance_name = name or f"ramsey_R33_n{n_vertices}"
    return SatInstance(
        name=instance_name,
        family="ramsey_R33",
        cnf=cnf,
        expected_sat=n_vertices <= 5,
        metadata={
            "n_vertices": n_vertices,
            "var_map": edge_vars,
        },
    )


def default_benchmark_instances(
    graph_vertices: Iterable[int],
    pigeon_holes: Iterable[int],
    ramsey_vertices: Iterable[int],
) -> List[SatInstance]:
    instances: List[SatInstance] = []

    for n_vertices in graph_vertices:
        edges = cycle_graph(n_vertices)
        instances.append(
            graph_coloring_instance(
                n_vertices=n_vertices,
                edges=edges,
                k_colors=2,
                name=f"cycle_{n_vertices}_2color",
                expected_sat=(n_vertices % 2 == 0),
            )
        )

    for n_holes in pigeon_holes:
        instances.append(
            pigeonhole_instance(
                n_pigeons=n_holes + 1,
                n_holes=n_holes,
                name=f"php_{n_holes + 1}_into_{n_holes}",
            )
        )

    for n_vertices in ramsey_vertices:
        instances.append(ramsey_instance(n_vertices=n_vertices))

    return instances

