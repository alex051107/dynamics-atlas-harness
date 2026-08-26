"""Minimal persistent DAG for unresolved evidence routes."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


def _source_attributes(case_graph: Mapping[str, Any]) -> tuple[dict[str, str], dict[str, str]]:
    methods: dict[str, str] = {}
    method_profiles: dict[str, str] = {}
    for source in case_graph.get("evidence_items", []):
        if isinstance(source, Mapping):
            source_id = source.get("source_id")
            method_id = source.get("method_id")
            if isinstance(source_id, str) and isinstance(method_id, str):
                methods[source_id] = method_id
            method_profile_id = source.get("method_profile_id")
            if isinstance(source_id, str) and isinstance(method_profile_id, str):
                method_profiles[source_id] = method_profile_id
    return methods, method_profiles


def _case_id(case_graph: Mapping[str, Any]) -> str | None:
    case = case_graph.get("case")
    if isinstance(case, Mapping) and isinstance(case.get("case_id"), str):
        return case["case_id"]
    value = case_graph.get("case_id")
    return value if isinstance(value, str) else None


def _target_source_ids(target: Mapping[str, Any]) -> set[str]:
    values = target.get("source_ids", [])
    source_ids = {value for value in values if isinstance(value, str)} if isinstance(values, list) else set()
    source_id = target.get("source_id")
    if isinstance(source_id, str):
        source_ids.add(source_id)
    return source_ids


def _operator_matches(
    spec: Mapping[str, Any],
    gap: Mapping[str, Any],
    methods: Mapping[str, str],
    method_profiles: Mapping[str, str],
    case_id: str | None,
) -> bool:
    if spec.get("status") != "ROSTER_PASS" or spec.get("routable") is not True:
        return False
    match = spec.get("route_match", {})
    if not isinstance(match, Mapping):
        return False
    case_ids = set(match.get("case_ids", []))
    if case_ids and case_id not in case_ids:
        return False
    runtime_subrule_ids = set(match.get("runtime_subrule_ids", []))
    if runtime_subrule_ids and gap.get("runtime_subrule_id") not in runtime_subrule_ids:
        return False
    gap_classes = match.get("gap_classes", [])
    if gap_classes and gap.get("gap_class") not in gap_classes:
        return False
    target = gap.get("target") if isinstance(gap.get("target"), Mapping) else {}
    target_types = match.get("target_types", [])
    if target_types and target.get("target_type") not in target_types:
        return False
    source_ids = _target_source_ids(target)
    allowed_source_ids = set(match.get("source_ids", []))
    if allowed_source_ids and (not source_ids or not source_ids.issubset(allowed_source_ids)):
        return False
    allowed_methods = set(match.get("method_ids", []))
    if allowed_methods:
        actual_methods = {methods.get(source_id) for source_id in source_ids}
        if not actual_methods.intersection(allowed_methods):
            return False
    allowed_method_profiles = set(match.get("method_profile_ids", []))
    if allowed_method_profiles:
        actual_profiles = {method_profiles.get(source_id) for source_id in source_ids}
        if not actual_profiles.intersection(allowed_method_profiles):
            return False
    path_terms = match.get("input_path_contains", [])
    input_path = str(gap.get("input_path") or "")
    if path_terms and not any(term in input_path for term in path_terms):
        return False
    return True


def build_run_plan(
    *,
    run_id: str,
    case_graph: Mapping[str, Any],
    evaluation: Mapping[str, Any],
    operator_registry: Mapping[str, Any],
) -> dict[str, Any]:
    if evaluation.get("branch") != "RUN_PLAN_REQUIRED":
        raise ValueError("RUN_PLAN_REQUIRES_GAP_BRANCH")
    methods, method_profiles = _source_attributes(case_graph)
    case_id = _case_id(case_graph)
    operators = operator_registry.get("operators", {})
    nodes: list[dict[str, Any]] = [
        {"node_id": "profile", "node_type": "PROFILE", "status": "SUCCEEDED"},
        {"node_id": "select-rules", "node_type": "SELECT_RULES", "status": "SUCCEEDED"},
        {"node_id": "evaluate-current", "node_type": "EVALUATE_CURRENT", "status": "SUCCEEDED"},
    ]
    edges: list[dict[str, Any]] = [
        {"edge_id": "exec-001", "edge_kind": "EXECUTION_DEPENDENCY", "from": "profile", "to": "select-rules"},
        {"edge_id": "exec-002", "edge_kind": "EXECUTION_DEPENDENCY", "from": "select-rules", "to": "evaluate-current"},
    ]
    blocked = 0
    for index, gap in enumerate(evaluation.get("gaps", []), start=1):
        matches = [
            operator_id
            for operator_id, spec in operators.items()
            if isinstance(spec, Mapping)
            and _operator_matches(spec, gap, methods, method_profiles, case_id)
        ]
        node_id = f"resolve-gap-{index:03d}"
        status = "READY" if len(matches) == 1 else "BLOCKED"
        if status == "BLOCKED":
            blocked += 1
        nodes.append(
            {
                "node_id": node_id,
                "node_type": "RESOLVE_GAP",
                "status": status,
                "gap": dict(gap),
                "operator_id": matches[0] if len(matches) == 1 else None,
                "reason_codes": []
                if len(matches) == 1
                else (["MULTIPLE_REGISTERED_OPERATORS"] if matches else ["NO_REGISTERED_OPERATOR_FOR_GAP"]),
            }
        )
        edges.append(
            {
                "edge_id": f"exec-{index + 2:03d}",
                "edge_kind": "EXECUTION_DEPENDENCY",
                "from": "evaluate-current",
                "to": node_id,
            }
        )
    nodes.extend(
        [
            {
                "node_id": "reevaluate",
                "node_type": "REEVALUATE",
                "status": "BLOCKED" if blocked else "PENDING",
            },
            {
                "node_id": "human-review",
                "node_type": "HUMAN_REVIEW",
                "status": "PENDING",
            },
        ]
    )
    gap_nodes = [node["node_id"] for node in nodes if node["node_type"] == "RESOLVE_GAP"]
    for node_id in gap_nodes:
        edges.append(
            {
                "edge_id": f"exec-{len(edges) + 1:03d}",
                "edge_kind": "EXECUTION_DEPENDENCY",
                "from": node_id,
                "to": "reevaluate",
            }
        )
    edges.append(
        {
            "edge_id": f"exec-{len(edges) + 1:03d}",
            "edge_kind": "EXECUTION_DEPENDENCY",
            "from": "reevaluate",
            "to": "human-review",
        }
    )
    plan = {
        "schema_version": "run-plan/v0.1",
        "run_id": run_id,
        "case_id": evaluation.get("case_id"),
        "status": "BLOCKED" if blocked else "READY",
        "nodes": nodes,
        "execution_edges": edges,
        "scientific_evidence_edges_source": "CASE_GRAPH_COMPARISONS_NOT_COPIED_HERE",
        "blocked_gap_count": blocked,
        "request_validate_commit": "FUTURE_FEATURE",
    }
    validate_run_plan(plan)
    return plan


def validate_run_plan(plan: Mapping[str, Any]) -> None:
    if plan.get("schema_version") != "run-plan/v0.1":
        raise ValueError("INVALID_RUN_PLAN_SCHEMA")
    nodes = plan.get("nodes")
    edges = plan.get("execution_edges")
    if not isinstance(nodes, list) or not isinstance(edges, list):
        raise ValueError("INVALID_RUN_PLAN_GRAPH")
    node_ids = [node.get("node_id") for node in nodes if isinstance(node, Mapping)]
    if len(node_ids) != len(nodes) or len(set(node_ids)) != len(node_ids):
        raise ValueError("INVALID_OR_DUPLICATE_RUN_PLAN_NODE")
    adjacency = {node_id: [] for node_id in node_ids}
    for edge in edges:
        if not isinstance(edge, Mapping) or edge.get("edge_kind") != "EXECUTION_DEPENDENCY":
            raise ValueError("INVALID_EXECUTION_EDGE")
        source, target = edge.get("from"), edge.get("to")
        if source not in adjacency or target not in adjacency:
            raise ValueError("EXECUTION_EDGE_ENDPOINT_NOT_FOUND")
        adjacency[source].append(target)

    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node_id: str) -> None:
        if node_id in visiting:
            raise ValueError("RUN_PLAN_CYCLE")
        if node_id in visited:
            return
        visiting.add(node_id)
        for target in adjacency[node_id]:
            visit(target)
        visiting.remove(node_id)
        visited.add(node_id)

    for node_id in node_ids:
        visit(node_id)
