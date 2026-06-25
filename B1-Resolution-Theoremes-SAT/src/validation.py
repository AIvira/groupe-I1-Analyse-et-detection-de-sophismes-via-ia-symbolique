from __future__ import annotations

from itertools import combinations
from typing import Any, Dict, Mapping

from .cnf import cnf_satisfied, model_to_assignment
from .domain import SatInstance


def validate_model(instance: SatInstance, model) -> Dict[str, Any]:
    if model is None:
        return {"feasible": False, "violations": ["no model"]}
    if not cnf_satisfied(instance.cnf, model):
        return {"feasible": False, "violations": ["model does not satisfy the CNF"]}

    metadata = instance.metadata or {}
    assignment = model_to_assignment(model)
    family = instance.family
    if family == "graph_coloring":
        return validate_graph_coloring(metadata, assignment)
    if family == "pigeonhole":
        return validate_pigeonhole(metadata, assignment)
    if family == "ramsey_R33":
        return validate_ramsey(metadata, assignment)
    return {"feasible": True, "violations": []}


def validate_graph_coloring(metadata: Mapping[str, Any], assignment: Mapping[int, bool]) -> Dict[str, Any]:
    n_vertices = int(metadata["n_vertices"])
    k_colors = int(metadata["k_colors"])
    edges = metadata["edges"]
    var_map = metadata["var_map"]
    violations = []
    coloring = {}

    for vertex in range(n_vertices):
        chosen = [color for color in range(k_colors) if assignment.get(var_map[(vertex, color)], False)]
        if len(chosen) != 1:
            violations.append(f"vertex {vertex} has {len(chosen)} colors")
        else:
            coloring[vertex] = chosen[0]

    for u, v in edges:
        if coloring.get(u) == coloring.get(v):
            violations.append(f"edge ({u}, {v}) is monochromatic")

    return {"feasible": not violations, "violations": violations, "coloring": coloring}


def validate_pigeonhole(metadata: Mapping[str, Any], assignment: Mapping[int, bool]) -> Dict[str, Any]:
    n_pigeons = int(metadata["n_pigeons"])
    n_holes = int(metadata["n_holes"])
    var_map = metadata["var_map"]
    violations = []
    placement = {}

    for pigeon in range(n_pigeons):
        chosen = [hole for hole in range(n_holes) if assignment.get(var_map[(pigeon, hole)], False)]
        if len(chosen) != 1:
            violations.append(f"pigeon {pigeon} has {len(chosen)} holes")
        else:
            placement[pigeon] = chosen[0]

    used = {}
    for pigeon, hole in placement.items():
        if hole in used:
            violations.append(f"hole {hole} contains pigeons {used[hole]} and {pigeon}")
        used[hole] = pigeon

    return {"feasible": not violations, "violations": violations, "placement": placement}


def validate_ramsey(metadata: Mapping[str, Any], assignment: Mapping[int, bool]) -> Dict[str, Any]:
    n_vertices = int(metadata["n_vertices"])
    var_map = metadata["var_map"]
    violations = []
    red_edges = []
    blue_edges = []

    for edge, var in var_map.items():
        if assignment.get(var, False):
            red_edges.append(edge)
        else:
            blue_edges.append(edge)

    red_set = set(red_edges)
    blue_set = set(blue_edges)
    for a, b, c in combinations(range(n_vertices), 3):
        tri = {tuple(sorted((a, b))), tuple(sorted((a, c))), tuple(sorted((b, c)))}
        if tri <= red_set:
            violations.append(f"red triangle ({a}, {b}, {c})")
        if tri <= blue_set:
            violations.append(f"blue triangle ({a}, {b}, {c})")

    return {
        "feasible": not violations,
        "violations": violations,
        "red_edges": red_edges,
        "blue_edges": blue_edges,
    }

