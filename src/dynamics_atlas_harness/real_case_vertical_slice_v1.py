"""Case-bound, no-Agent X-EISD vertical slice for Rules v1-alpha.

This module intentionally reuses the proposal-only Rules-v1 evaluator.  It is not a
general source-search, Stage-2, or workflow-engine implementation: it accepts only
the exposed Lincoff X-EISD source pair and exact, locally allowlisted locators.
"""

from __future__ import annotations

import csv
import hashlib
import json
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

from .registered_operators import execute_hsp90_time_anatomy_adapter
from .rules_prototype_v1 import (
    RulePrototypeError,
    evaluate_active_rules,
    load_json,
    rule_instance_id,
)


X_EISD_CASE_ID = "lincoff_2020_xeisd_random_j_relation_v1_alpha"
X_EISD_PARENT_CASE_ID = "lincoff_2020_xeisd_maintext"
X_EISD_SOURCE_IDS = (
    "xeisd_random_candidate_pool",
    "xeisd_j_coupling_fit",
)
X_EISD_EDGE_ID = "xeisd_random_pool_vs_j_coupling_question"
X_EISD_FROZEN_REQUESTED_CLAIM = (
    "Can the declared RANDOM candidate-pool and J-coupling relation be reviewed "
    "without claiming a shared population, independent validation, kinetics, or mechanism?"
)
X_EISD_FROZEN_SELECTED_RULE_INSTANCE_IDS = (
    "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION::SOURCE::xeisd_random_candidate_pool",
    "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION::SOURCE::xeisd_j_coupling_fit",
    "F02R02_EDGE_CONDITION_COMPATIBILITY::EDGE::xeisd_random_pool_vs_j_coupling_question",
    "F03R01_SOURCE_NATIVE_MEASUREMENT::SOURCE::xeisd_random_candidate_pool",
    "F03R01_SOURCE_NATIVE_MEASUREMENT::SOURCE::xeisd_j_coupling_fit",
    "F01R01_CASE_CLAIM_DECLARATION::CASE::lincoff_2020_xeisd_random_j_relation_v1_alpha",
    "F01R02_CASE_REQUESTED_WORDING_SCOPE::CASE::lincoff_2020_xeisd_random_j_relation_v1_alpha",
    "F06R01_SOURCE_EVIDENCE_ROLE::SOURCE::xeisd_random_candidate_pool",
    "F06R01_SOURCE_EVIDENCE_ROLE::SOURCE::xeisd_j_coupling_fit",
    "F06R02_EDGE_COMPARABILITY::EDGE::xeisd_random_pool_vs_j_coupling_question",
)
X_EISD_FROZEN_BASE_PROJECTION_PATH = (
    "evidence/real_case_vertical_slice_v1/frozen_inputs/xeisd/"
    "base_projection_manifest_v1.json"
)
X_EISD_FROZEN_BASE_PROJECTION_SHA256 = (
    "32e802b31dbc175087248bfc548665aa7fa8708a3eb72c17ea2b6446598c746c"
)
HSP90_CASE_ID = "hsp90_directional_time_anatomy_development_v1_alpha"
HSP90_SOURCE_ID = "hsp90_md_round2_directional_packet"
HSP90_RUNTIME_SUBRULE_ID = "F04R02_SOURCE_DECLARED_TIME_ANATOMY_CONTROL"
HSP90_OPERATOR_ID = "hsp90.directional_time_anatomy.v1_case_bound"
HSP90_METHOD_PROFILE_ID = "hsp90_md_directional_time_anatomy_v0"
HSP90_CAPABILITY_ID = "MD_DIRECTIONAL_TIME_ANATOMY_CONTROL"
HSP90_TIME_ANATOMY_ACTION = "MD_DIRECTIONAL_TIME_ANATOMY_CONTROL"
HSP90_EXACT_REQUEST_ID = "B1_EXACT_HSP90_RULE_TO_OPERATOR"
HSP90_EXACT_OUTPUT_DIRECTORY = (
    "evidence/real_case_vertical_slice_v1/outputs/"
    "hsp90_b1_rule_to_operator/operator_outputs"
)
HSP90_REFERENCE_DEMO_OUTPUT_DIRECTORY = "routes/hsp90_b1/operator_outputs"
_HSP90_EXACT_TIME_CONTRACT = {
    "analysis_window_ns": [20, 1020],
    "frame_dependence": "CORRELATED_WITHIN_TRAJECTORY",
    "frames_per_trajectory": 1001,
    "saved_stride_ns": 1,
    "statistical_unit": "TRAJECTORY",
    "trajectory_count": 40,
}
_HSP90_EXACT_FIXED_PARAMETERS = {
    "persistence_saved_frames": [5, 20, 50],
    "state_rule": "existing zero-sign two-readout rule",
}
_REQUIRED_SUBRULE_IDS = frozenset(
    {
        "F01R01_CASE_CLAIM_DECLARATION",
        "F01R02_CASE_REQUESTED_WORDING_SCOPE",
        "F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION",
        "F02R02_EDGE_CONDITION_COMPATIBILITY",
        "F03R01_SOURCE_NATIVE_MEASUREMENT",
        "F06R01_SOURCE_EVIDENCE_ROLE",
        "F06R02_EDGE_COMPARABILITY",
    }
)
_ALLOWED_LOOKUP_FIELDS = {
    "SOURCE": frozenset({"sample_composition"}),
    "EDGE": frozenset({"condition_relation", "relation_type", "bridge_status"}),
}
_EXACT_REVIEW_DERIVATIVE_ATTESTATION = "EXACT_REVIEW_DERIVATIVE_ATTESTATION"
_EXACT_HSP90_EXPOSED_DEVELOPMENT_SCOPE = {
    "activation_scope": "EXPOSED_DEVELOPMENT_ACTIVE",
    "routing_scope": "EXACT_CASE_BOUND",
    "generalization_status": "NOT_GENERAL",
    "deployment_status": "NOT_PRODUCTION",
}


@dataclass(frozen=True)
class _Hsp90OutputLocation:
    """One of the two explicitly permitted locations for the exposed B1 output."""

    output_dir: Path
    receipt_output_directory: str


class VerticalSliceError(ValueError):
    """Raised when an X-EISD-only vertical-slice contract is violated."""


def load_json_object(path: Path) -> dict[str, Any]:
    """Load a JSON object with the same fail-closed convention as Rules v1."""

    value = load_json(path)
    if not isinstance(value, dict):  # Defensive; ``load_json`` already enforces this.
        raise VerticalSliceError(f"expected JSON object: {path}")
    return value


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise VerticalSliceError(f"{label} must be a mapping")
    return value


def _harness_root(workspace_root: Path) -> Path:
    """Return the checked repository root; never permit a parent-workspace asset."""

    workspace_root = workspace_root.resolve()
    module_repository_root = Path(__file__).resolve().parents[2]
    if workspace_root != module_repository_root:
        raise VerticalSliceError(
            "workspace_root must match the checked-out dynamics-atlas-harness repository"
        )
    return module_repository_root


def _safe_local_source_path(workspace_root: Path, relative_path: str) -> Path:
    harness_root = _harness_root(workspace_root)
    candidate = (harness_root / relative_path).resolve()
    if not candidate.is_relative_to(harness_root):
        raise VerticalSliceError("allowlisted lookup path escapes the harness repository")
    return candidate


def validate_xeisd_projection(case_graph: Mapping[str, Any]) -> None:
    """Fail closed unless the input is the one documented X-EISD subprojection."""

    case_graph = _mapping(case_graph, "case_graph")
    case = _mapping(case_graph.get("case"), "case_graph.case")
    if case.get("case_id") != X_EISD_CASE_ID:
        raise VerticalSliceError("X-EISD projection uses an unexpected case_id")
    if case.get("parent_case_id") != X_EISD_PARENT_CASE_ID:
        raise VerticalSliceError("X-EISD projection must retain its parent_case_id")
    provenance = _mapping(case_graph.get("projection_provenance"), "projection_provenance")
    if provenance.get("base_asset_id") != "xeisd-rich-casegraph-v0.3":
        raise VerticalSliceError("X-EISD projection must identify its frozen v0.3 asset")
    if provenance.get("workspace_relative_base_asset_path") != X_EISD_FROZEN_BASE_PROJECTION_PATH:
        raise VerticalSliceError("X-EISD projection must retain the frozen base-projection path")
    if provenance.get("base_asset_fixture_sha256") != X_EISD_FROZEN_BASE_PROJECTION_SHA256:
        raise VerticalSliceError("X-EISD projection must retain the frozen base-projection hash")

    sources = case_graph.get("evidence_items")
    edges = case_graph.get("comparisons")
    if not isinstance(sources, list) or not isinstance(edges, list):
        raise VerticalSliceError("X-EISD projection needs source and comparison collections")
    source_ids = [item.get("source_id") for item in sources if isinstance(item, Mapping)]
    if tuple(source_ids) != X_EISD_SOURCE_IDS or len(set(source_ids)) != len(source_ids):
        raise VerticalSliceError("X-EISD projection must contain exactly the documented source pair")
    edge_ids = [item.get("comparison_id") for item in edges if isinstance(item, Mapping)]
    if edge_ids != [X_EISD_EDGE_ID]:
        raise VerticalSliceError("X-EISD projection must contain exactly the documented edge")
    for source in sources:
        source = _mapping(source, "X-EISD source")
        if source.get("origin_case_id") != X_EISD_PARENT_CASE_ID:
            raise VerticalSliceError("X-EISD source must retain parent case provenance")
        locators = source.get("source_locator_ids")
        if not isinstance(locators, list) or not all(isinstance(item, str) and item for item in locators):
            raise VerticalSliceError("X-EISD source must retain exact source locator IDs")


def _ensure_unique_allowlist_ids(entries: Sequence[Any]) -> None:
    lookup_ids = [item.get("lookup_id") for item in entries if isinstance(item, Mapping)]
    if len(lookup_ids) != len(entries) or any(not isinstance(item, str) or not item for item in lookup_ids):
        raise VerticalSliceError("each allowlist entry needs a nonempty lookup_id")
    if len(set(lookup_ids)) != len(lookup_ids):
        raise VerticalSliceError("allowlisted lookup IDs must be unique")


def execute_exact_source_lookup(
    *,
    allowlist: Mapping[str, Any],
    request: Mapping[str, Any],
    workspace_root: Path,
) -> dict[str, Any]:
    """Resolve one declared field mapping from a local exact-locator allowlist.

    The executor never searches the network, discovers documents, or infers a
    scientific value from free text. It verifies a hash-bound, predeclared review
    derivative and exact locator marker before returning a predeclared field update
    as an attested Draft input.
    """

    allowlist = _mapping(allowlist, "allowlist")
    request = _mapping(request, "request")
    if allowlist.get("lookup_kind") != _EXACT_REVIEW_DERIVATIVE_ATTESTATION:
        raise VerticalSliceError("allowlist must declare exact review-derivative attestation")
    lookup_id = request.get("lookup_id")
    case_id = request.get("case_id")
    target_kind = request.get("target_kind")
    target_id = request.get("target_id")
    locator_id = request.get("locator_id")
    if not all(isinstance(value, str) and value for value in (lookup_id, case_id, target_kind, target_id, locator_id)):
        raise VerticalSliceError("lookup request needs nonempty lookup_id, case_id, target_kind, target_id, and locator_id")

    if case_id != X_EISD_CASE_ID or allowlist.get("case_id") != X_EISD_CASE_ID:
        return {
            "lookup_kind": _EXACT_REVIEW_DERIVATIVE_ATTESTATION,
            "lookup_id": lookup_id,
            "case_id": case_id,
            "target": {"kind": target_kind, "id": target_id},
            "requested_locator_id": locator_id,
            "status": "NOT_ALLOWED",
            "route": "HUMAN_OR_NEW_DATA",
            "reason_code": "CASE_NOT_IN_EXACT_ALLOWLIST",
            "field_updates": {},
        }

    entries = allowlist.get("entries")
    if not isinstance(entries, list):
        raise VerticalSliceError("allowlist entries must be a list")
    _ensure_unique_allowlist_ids(entries)
    entry = next((item for item in entries if isinstance(item, Mapping) and item.get("lookup_id") == lookup_id), None)
    if entry is None:
        return {
            "lookup_kind": _EXACT_REVIEW_DERIVATIVE_ATTESTATION,
            "lookup_id": lookup_id,
            "case_id": case_id,
            "target": {"kind": target_kind, "id": target_id},
            "requested_locator_id": locator_id,
            "status": "NOT_FOUND",
            "route": "HUMAN_OR_NEW_DATA",
            "reason_code": "EXACT_LOOKUP_ID_NOT_ALLOWLISTED",
            "field_updates": {},
        }
    if (
        entry.get("target_kind") != target_kind
        or entry.get("target_id") != target_id
        or entry.get("locator_id") != locator_id
    ):
        return {
            "lookup_kind": _EXACT_REVIEW_DERIVATIVE_ATTESTATION,
            "lookup_id": lookup_id,
            "case_id": case_id,
            "target": {"kind": target_kind, "id": target_id},
            "requested_locator_id": locator_id,
            "status": "NOT_ALLOWED",
            "route": "HUMAN_OR_NEW_DATA",
            "reason_code": "LOOKUP_REQUEST_DOES_NOT_MATCH_ALLOWLISTED_TARGET",
            "field_updates": {},
        }

    relative_path = entry.get("workspace_relative_path")
    locator_marker = entry.get("exact_locator_marker")
    field_updates = entry.get("field_updates")
    expected_fixture_sha256 = entry.get("fixture_sha256")
    if not isinstance(relative_path, str) or not relative_path:
        raise VerticalSliceError("allowlist entry lacks workspace_relative_path")
    if not isinstance(locator_marker, str) or not locator_marker:
        raise VerticalSliceError("allowlist entry lacks exact_locator_marker")
    if not isinstance(field_updates, Mapping) or not field_updates:
        raise VerticalSliceError("allowlist entry lacks field_updates")
    if not isinstance(expected_fixture_sha256, str) or len(expected_fixture_sha256) != 64:
        raise VerticalSliceError("allowlist entry lacks a fixture_sha256")
    allowed_fields = _ALLOWED_LOOKUP_FIELDS.get(target_kind)
    if allowed_fields is None or not set(field_updates).issubset(allowed_fields):
        raise VerticalSliceError("allowlist attempts an unauthorized target-field update")

    source_path = _safe_local_source_path(workspace_root, relative_path)
    if not source_path.is_file():
        return {
            "lookup_kind": _EXACT_REVIEW_DERIVATIVE_ATTESTATION,
            "lookup_id": lookup_id,
            "case_id": case_id,
            "target": {"kind": target_kind, "id": target_id},
            "requested_locator_id": locator_id,
            "status": "SOURCE_UNAVAILABLE",
            "route": "HUMAN_OR_NEW_DATA",
            "reason_code": "ALLOWLISTED_LOCAL_SOURCE_UNAVAILABLE",
            "field_updates": {},
            "workspace_relative_path": relative_path,
        }
    observed_fixture_sha256 = _sha256(source_path)
    if observed_fixture_sha256 != expected_fixture_sha256:
        return {
            "lookup_kind": _EXACT_REVIEW_DERIVATIVE_ATTESTATION,
            "lookup_id": lookup_id,
            "case_id": case_id,
            "target": {"kind": target_kind, "id": target_id},
            "requested_locator_id": locator_id,
            "status": "FIXTURE_HASH_MISMATCH",
            "route": "HUMAN_OR_NEW_DATA",
            "reason_code": "ALLOWLISTED_FIXTURE_HASH_MISMATCH",
            "field_updates": {},
            "workspace_relative_path": relative_path,
        }
    if locator_marker not in source_path.read_text(encoding="utf-8"):
        return {
            "lookup_kind": _EXACT_REVIEW_DERIVATIVE_ATTESTATION,
            "lookup_id": lookup_id,
            "case_id": case_id,
            "target": {"kind": target_kind, "id": target_id},
            "requested_locator_id": locator_id,
            "status": "LOCATOR_NOT_FOUND",
            "route": "HUMAN_OR_NEW_DATA",
            "reason_code": "ALLOWLISTED_LOCATOR_MARKER_MISSING",
            "field_updates": {},
            "workspace_relative_path": relative_path,
        }

    return {
        "lookup_kind": _EXACT_REVIEW_DERIVATIVE_ATTESTATION,
        "lookup_id": lookup_id,
        "case_id": case_id,
        "target": {"kind": target_kind, "id": target_id},
        "requested_locator_id": locator_id,
        "status": "FOUND",
        "route": "SOURCE_LOOKUP",
        "next_evaluation": "DIRECT_EVALUATION",
        "reason_code": "EXACT_REVIEW_DERIVATIVE_ATTESTATION_FOUND",
        "field_updates": dict(field_updates),
        "workspace_relative_path": relative_path,
        "fixture_sha256": observed_fixture_sha256,
        "source_kind": entry.get("source_kind"),
        "raw_observation": entry.get("raw_observation"),
        "field_update_derivation": entry.get("field_update_derivation"),
        "attestation_boundary": "EXPOSED_DEVELOPMENT_DERIVATIVE_NOT_SOURCE_SCIENCE_VALIDATION",
    }


def apply_lookup_result(
    *, case_graph: Mapping[str, Any], lookup_result: Mapping[str, Any]
) -> dict[str, Any]:
    """Apply one successful, case-bound declaration attestation to a copy."""

    validate_xeisd_projection(case_graph)
    case_graph = deepcopy(dict(case_graph))
    lookup_result = _mapping(lookup_result, "lookup_result")
    if lookup_result.get("status") != "FOUND":
        return case_graph
    if lookup_result.get("lookup_kind") != _EXACT_REVIEW_DERIVATIVE_ATTESTATION:
        raise VerticalSliceError("successful lookup result must be an exact review-derivative attestation")
    target = _mapping(lookup_result.get("target"), "lookup_result.target")
    target_kind = target.get("kind")
    target_id = target.get("id")
    updates = _mapping(lookup_result.get("field_updates"), "lookup_result.field_updates")
    if lookup_result.get("case_id") != X_EISD_CASE_ID:
        raise VerticalSliceError("lookup result has an unexpected case identity")
    allowed_fields = _ALLOWED_LOOKUP_FIELDS.get(target_kind)
    if allowed_fields is None or not set(updates).issubset(allowed_fields):
        raise VerticalSliceError("lookup result attempts an unauthorized target-field update")
    if target_kind == "SOURCE":
        collection = case_graph.get("evidence_items")
        key = "source_id"
    elif target_kind == "EDGE":
        collection = case_graph.get("comparisons")
        key = "comparison_id"
    else:
        raise VerticalSliceError("allowlisted lookup targets must be SOURCE or EDGE")
    if not isinstance(collection, list):
        raise VerticalSliceError("case graph collection is missing")
    record = next((item for item in collection if isinstance(item, Mapping) and item.get(key) == target_id), None)
    if record is None:
        raise VerticalSliceError("allowlisted lookup target does not exist in this case graph")
    if not isinstance(record, dict):
        record = dict(record)
        index = collection.index(next(item for item in collection if isinstance(item, Mapping) and item.get(key) == target_id))
        collection[index] = record
    existing_attestations = record.get("lookup_attestations", [])
    if not isinstance(existing_attestations, list):
        raise VerticalSliceError("lookup_attestations must be a list when present")
    lookup_id = lookup_result.get("lookup_id")
    if lookup_id in existing_attestations:
        raise VerticalSliceError("a lookup receipt may not be applied twice")
    for field, value in updates.items():
        if field in record and record[field] != value:
            raise VerticalSliceError("lookup result conflicts with an existing projected field")
    record.update(updates)
    record.setdefault("lookup_attestations", []).append(lookup_id)
    return case_graph


def derive_declaration_attestations(
    *, case_graph: Mapping[str, Any], lookup_results: Sequence[Mapping[str, Any]]
) -> dict[str, Any]:
    """Derive status labels from exact lookup receipts and preserved source fields.

    The allowlist cannot write declaration statuses.  This narrow deterministic
    validator derives them only after a matching successful receipt supplies the
    source-context field; the status is still a Draft field-presence statement.
    """

    validate_xeisd_projection(case_graph)
    derived = deepcopy(dict(case_graph))
    found_source_ids: set[str] = set()
    for result in lookup_results:
        if not isinstance(result, Mapping) or result.get("status") != "FOUND":
            continue
        if result.get("lookup_kind") != _EXACT_REVIEW_DERIVATIVE_ATTESTATION:
            raise VerticalSliceError("declaration statuses require exact review-derivative attestations")
        target = result.get("target")
        if isinstance(target, Mapping) and target.get("kind") == "SOURCE":
            target_id = target.get("id")
            if isinstance(target_id, str):
                found_source_ids.add(target_id)
    for source in derived["evidence_items"]:
        if source["source_id"] in found_source_ids and source.get("sample_composition"):
            source["sample_system_composition_declaration_status"] = "DECLARED"
        measurement_fields = (
            "native_observable",
            "estimand",
            "time_semantics",
            "spatial_support",
            "unit_or_aggregation",
        )
        if all(source.get(field) for field in measurement_fields) and source.get("time_semantics", {}).get("kind"):
            source["native_measurement_declaration_status"] = "DECLARED"
    return derived


def evaluate_xeisd_case(
    *,
    case_graph: Mapping[str, Any],
    runtime_subrules: Mapping[str, Any],
    bindings: Mapping[str, Any],
    contracts: Mapping[str, Any],
) -> list[dict[str, Any]]:
    """Run the merged explicit F01/F02/F03/F06 replay for the one X-EISD pair."""

    validate_xeisd_projection(case_graph)
    return evaluate_active_rules(
        case_graph=case_graph,
        runtime_subrules=runtime_subrules,
        bindings=bindings,
        contracts=contracts,
    )


def _xeisd_relevant_results(results: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    relevant: list[dict[str, Any]] = []
    for result in results:
        target = result.get("target") if isinstance(result, Mapping) else None
        if not isinstance(target, Mapping):
            continue
        subrule_id = result.get("runtime_subrule_id")
        target_id = target.get("id")
        if subrule_id not in _REQUIRED_SUBRULE_IDS:
            continue
        if target.get("kind") == "CASE" and target_id == X_EISD_CASE_ID:
            relevant.append(dict(result))
        elif target.get("kind") == "SOURCE" and target_id in X_EISD_SOURCE_IDS:
            relevant.append(dict(result))
        elif target.get("kind") == "EDGE" and target_id == X_EISD_EDGE_ID:
            relevant.append(dict(result))
    if not relevant:
        raise VerticalSliceError("no required X-EISD RuleResults were emitted")
    return relevant


def _xeisd_nonblocking_results(results: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    return [
        dict(result)
        for result in results
        if isinstance(result, Mapping)
        and result.get("runtime_subrule_id") == "F06R03_EDGE_VALIDATION_INDEPENDENCE"
        and isinstance(result.get("target"), Mapping)
        and result["target"].get("id") == X_EISD_EDGE_ID
    ]


def materialize_xeisd_conclusion_packet(
    *,
    case_graph: Mapping[str, Any],
    rule_results: Sequence[Mapping[str, Any]],
    lookup_results: Sequence[Mapping[str, Any]],
    scenario_id: str,
) -> dict[str, Any]:
    """Materialize one X-EISD-only terminal route, never a scientific verdict."""

    validate_xeisd_projection(case_graph)
    case = _mapping(case_graph.get("case"), "case_graph.case")
    relevant = _xeisd_relevant_results(rule_results)
    nonblocking = _xeisd_nonblocking_results(rule_results)
    blocking = [result for result in relevant if result.get("status") == "FAIL"]
    unresolved = [result for result in relevant if result.get("status") == "UNRESOLVED"]
    lookup_results = [dict(item) for item in lookup_results]

    if blocking:
        first = blocking[0]
        route_disposition = "RELATION_BLOCKED"
        terminal_route = "HUMAN_OR_NEW_DATA"
        claim_ceiling = "The declared cross-source relation is blocked; neither source-local observation is invalidated. Human scientific review remains required."
    elif unresolved:
        first = unresolved[0]
        route_disposition = "ABSTAIN"
        terminal_route = (
            "HUMAN_OR_NEW_DATA"
            if any(item.get("status") != "FOUND" for item in lookup_results)
            else str(first.get("claim_effect", {}).get("route", "SOURCE_LOOKUP"))
        )
        claim_ceiling = "A missing declared field or exact source locator leaves the requested relation unresolved; no cross-source claim is emitted."
    else:
        first = None
        route_disposition = "RELATION_REVIEWABLE"
        terminal_route = "DIRECT_EVALUATION"
        claim_ceiling = "Only the declared X-EISD relation is reviewable from attested local fields. This is not evidence of numeric equivalence, a shared population, independent validation, or a final scientific conclusion."

    packet = {
        "schema_version": "conclusion-packet/v1-alpha",
        "packet_kind": "EXPOSED_X_EISD_RULES_V1_ALPHA",
        "development_status": "EXPOSED_DEVELOPMENT_ACTIVE",
        "scenario_id": scenario_id,
        "case_id": X_EISD_CASE_ID,
        "parent_case_id": X_EISD_PARENT_CASE_ID,
        "edge_id": X_EISD_EDGE_ID,
        "terminal_route": terminal_route,
        "route_disposition": route_disposition,
        "scientific_disposition": "NOT_EVALUATED",
        "claim_ceiling": claim_ceiling,
        "human_decision_gate_required": True,
        "unsafe_claim_upgrade": False,
        "first_failed_dependency": (
            None
            if first is None
            else {
                "rule_instance_id": first.get("rule_instance_id"),
                "status": first.get("status"),
                "reason_codes": list(first.get("reason_codes", [])),
                "missing_paths": list(first.get("missing_paths", [])),
            }
        ),
        "requested_claim": case["scientific_claim"],
        "selected_rule_instance_ids": [result["rule_instance_id"] for result in relevant],
        "blocking_rule_instance_ids": [result["rule_instance_id"] for result in blocking],
        "rule_results": relevant,
        "nonblocking_rule_results": nonblocking,
        "evidence_lookup_results": lookup_results,
        "operator_results": [],
        "human_review_items": [
            "Review whether the local predeclared review-derivative attestations are sufficient for source-science use.",
            "Review the explicit DOCUMENTED-to-DECLARED bridge vocabulary mapping before treating it as any scientific comparability judgment.",
            "F06R03 is retained only as a nonblocking NOT_APPLICABLE result because this pair asserts no validation claim.",
        ],
        "next_action": (
            "Review the bounded relation gate."
            if route_disposition == "RELATION_REVIEWABLE"
            else "Resolve the first failed dependency through a human review or new data; do not infer a cross-source claim."
        ),
        "provenance": {
            "case_projection_boundary": case_graph.get("projection_boundary"),
            "projection_provenance": case_graph.get("projection_provenance"),
            "source_locator_ids": [
                locator
                for item in case_graph.get("evidence_items", [])
                if isinstance(item, Mapping)
                for locator in item.get("source_locator_ids", [])
            ],
        },
    }
    validate_xeisd_conclusion_packet(packet)
    return packet


def _validate_xeisd_route_inventory_and_scope(
    packet: Mapping[str, Any], rule_results: Sequence[Mapping[str, Any]]
) -> None:
    """Keep the exact X-EISD relation contract from being relabeled or truncated."""

    selected_ids = packet.get("selected_rule_instance_ids")
    if not isinstance(selected_ids, list) or any(
        not isinstance(rule_id, str) or not rule_id for rule_id in selected_ids
    ):
        raise VerticalSliceError("X-EISD ConclusionPacket has invalid selected RuleInstances")
    if tuple(selected_ids) != X_EISD_FROZEN_SELECTED_RULE_INSTANCE_IDS:
        raise VerticalSliceError(
            "X-EISD ConclusionPacket selected RuleInstances must match the frozen inventory"
        )

    observed_ids: list[str] = []
    failed_results: list[Mapping[str, Any]] = []
    for result in rule_results:
        result = _mapping(result, "X-EISD ConclusionPacket RuleResult")
        rule_id = result.get("rule_instance_id")
        if not isinstance(rule_id, str) or not rule_id:
            raise VerticalSliceError("X-EISD RuleResult has no rule_instance_id")
        observed_ids.append(rule_id)
        if result.get("status") == "FAIL":
            failed_results.append(result)

    if len(set(observed_ids)) != len(observed_ids) or observed_ids != selected_ids:
        raise VerticalSliceError(
            "X-EISD ConclusionPacket RuleResult inventory must match selected RuleInstances exactly"
        )

    expected_blocking_ids = [result["rule_instance_id"] for result in failed_results]
    if packet.get("blocking_rule_instance_ids") != expected_blocking_ids:
        raise VerticalSliceError(
            "X-EISD ConclusionPacket blocking RuleInstances must match failed RuleResults"
        )

    if packet.get("requested_claim") != X_EISD_FROZEN_REQUESTED_CLAIM:
        raise VerticalSliceError(
            "X-EISD ConclusionPacket requested claim must remain the exact frozen relation claim"
        )

    if failed_results:
        if packet.get("route_disposition") != "RELATION_BLOCKED":
            raise VerticalSliceError(
                "X-EISD failed RuleResults must retain the relation-blocked route"
            )
        for result in failed_results:
            target = _mapping(result.get("target"), "X-EISD failed RuleResult target")
            if target.get("kind") != "EDGE" or target.get("id") != X_EISD_EDGE_ID:
                raise VerticalSliceError(
                    "X-EISD relation block may only be caused by the declared comparison edge"
                )


def validate_xeisd_conclusion_packet(packet: Mapping[str, Any]) -> None:
    """Validate only the narrow X-EISD ConclusionPacket contract."""

    packet = _mapping(packet, "ConclusionPacket")
    required = {
        "schema_version",
        "packet_kind",
        "development_status",
        "scenario_id",
        "case_id",
        "edge_id",
        "terminal_route",
        "route_disposition",
        "scientific_disposition",
        "claim_ceiling",
        "human_decision_gate_required",
        "unsafe_claim_upgrade",
        "first_failed_dependency",
        "requested_claim",
        "selected_rule_instance_ids",
        "blocking_rule_instance_ids",
        "rule_results",
        "nonblocking_rule_results",
        "evidence_lookup_results",
        "operator_results",
        "human_review_items",
        "next_action",
        "provenance",
    }
    missing = sorted(required.difference(packet))
    if missing:
        raise VerticalSliceError(f"ConclusionPacket missing required fields: {', '.join(missing)}")
    if packet["case_id"] != X_EISD_CASE_ID or packet["edge_id"] != X_EISD_EDGE_ID:
        raise VerticalSliceError("ConclusionPacket has an unexpected case or edge identity")
    if packet["development_status"] != "EXPOSED_DEVELOPMENT_ACTIVE":
        raise VerticalSliceError("ConclusionPacket has an invalid development status")
    if packet["route_disposition"] not in {
        "RELATION_REVIEWABLE",
        "RELATION_BLOCKED",
        "ABSTAIN",
    }:
        raise VerticalSliceError("ConclusionPacket has an unknown route disposition")
    if packet["scientific_disposition"] != "NOT_EVALUATED":
        raise VerticalSliceError("ConclusionPacket must not emit a scientific disposition")
    if packet["human_decision_gate_required"] is not True:
        raise VerticalSliceError("ConclusionPacket must retain the HumanDecisionGate")
    if packet["unsafe_claim_upgrade"] is not False:
        raise VerticalSliceError("ConclusionPacket must fail closed on claim upgrades")
    if not isinstance(packet["rule_results"], list) or not packet["rule_results"]:
        raise VerticalSliceError("ConclusionPacket must retain its RuleResults")
    if not isinstance(packet["nonblocking_rule_results"], list):
        raise VerticalSliceError("ConclusionPacket must retain nonblocking RuleResults")
    if not isinstance(packet["operator_results"], list):
        raise VerticalSliceError("ConclusionPacket must retain Operator results, even when empty")
    _validate_xeisd_route_inventory_and_scope(packet, packet["rule_results"])


def load_rules_v1_bundle(rules_root: Path) -> dict[str, Any]:
    """Load the existing merged Rules-v1 artifacts without copying their logic."""

    return {
        "runtime_subrules": load_json_object(rules_root / "runtime_subrules_v1.json"),
        "bindings": load_json_object(rules_root / "applicability_bindings_v1.json"),
        "contracts": load_json_object(rules_root / "evaluation_contracts_v1.json"),
    }


# ---------------------------------------------------------------------------
# Case B: one HSP90 RuleInstance -> exact registered Operator -> EvidenceResult
# ---------------------------------------------------------------------------
#
# These functions intentionally stay outside ``evaluate_active_rules``.  PR1B's
# two fixed phases remain frozen; this is one case-bound F04 evaluator and one
# execution-evidence context, not a generic dependency scheduler.


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _project_relative_path(workspace_root: Path, relative_path: str) -> Path:
    """Resolve one repository-contained manifest asset while forbidding an escape."""

    if not isinstance(relative_path, str) or not relative_path:
        raise VerticalSliceError("manifest path must be a nonempty string")
    harness_root = _harness_root(workspace_root)
    candidate = (harness_root / relative_path).resolve()
    if not candidate.is_relative_to(harness_root):
        raise VerticalSliceError("manifest path escapes the harness repository")
    return candidate


def load_hsp90_case_bundle(evidence_root: Path) -> dict[str, Any]:
    """Load the one exposed HSP90 case, local rule overlay, and fixed manifest."""

    return {
        "case_graph": load_json_object(evidence_root / "hsp90_case_dossier_v1.json"),
        "rule_overlay": load_json_object(
            evidence_root / "hsp90_f04r02_rule_overlay_v1.json"
        ),
        "input_manifest": load_json_object(
            evidence_root / "hsp90_operator_input_manifest_v1.json"
        ),
    }


def _hsp90_source(case_graph: Mapping[str, Any]) -> Mapping[str, Any]:
    evidence_items = case_graph.get("evidence_items")
    if not isinstance(evidence_items, list):
        raise VerticalSliceError("HSP90 CaseGraph needs an evidence_items list")
    matches = [
        item
        for item in evidence_items
        if isinstance(item, Mapping) and item.get("source_id") == HSP90_SOURCE_ID
    ]
    if len(matches) != 1:
        raise VerticalSliceError("HSP90 CaseGraph needs exactly one declared MD source")
    return matches[0]


def _validate_hsp90_frozen_manifest_contract(input_manifest: Mapping[str, Any]) -> None:
    """Reject a manifest whose declared time contract is not the exposed B1 contract."""

    input_manifest = _mapping(input_manifest, "HSP90 input manifest")
    expected_time_contract = _mapping(
        input_manifest.get("expected_time_contract"),
        "HSP90 manifest.expected_time_contract",
    )
    if dict(expected_time_contract) != _HSP90_EXACT_TIME_CONTRACT:
        raise VerticalSliceError("HSP90 manifest has an unexpected exact time contract")
    fixed_parameters = _mapping(
        input_manifest.get("fixed_parameters"), "HSP90 manifest.fixed_parameters"
    )
    if dict(fixed_parameters) != _HSP90_EXACT_FIXED_PARAMETERS:
        raise VerticalSliceError("HSP90 manifest has unexpected fixed parameters")


def validate_hsp90_case_dossier(
    case_graph: Mapping[str, Any], input_manifest: Mapping[str, Any]
) -> None:
    """Validate the immutable facts and manifest-bound time contract for Case B."""

    case_graph = _mapping(case_graph, "HSP90 CaseGraph")
    _validate_hsp90_frozen_manifest_contract(input_manifest)
    case = _mapping(case_graph.get("case"), "HSP90 CaseGraph.case")
    if case.get("case_id") != HSP90_CASE_ID:
        raise VerticalSliceError("HSP90 CaseGraph has an unexpected case_id")
    if case.get("development_role") != "EXPOSED_DEVELOPMENT":
        raise VerticalSliceError("HSP90 CaseGraph must remain an exposed development case")
    if case.get("requested_claim_scope") != "SAME_PACKET_DESCRIPTIVE_DIRECTIONAL_DIAGNOSTIC":
        raise VerticalSliceError("HSP90 CaseGraph has an unsafe requested claim scope")
    forbidden = case.get("forbidden_upgrades")
    if not isinstance(forbidden, list) or not {
        "TRANSITION_RATE",
        "EQUILIBRIUM_POPULATION",
        "FREE_ENERGY",
        "COMPLETE_PATHWAY",
        "MECHANISM",
        "MUTATION_EFFECT",
    }.issubset(set(forbidden)):
        raise VerticalSliceError("HSP90 CaseGraph must retain its forbidden claim upgrades")

    source = _hsp90_source(case_graph)
    required_pairs = {
        "method_id": "MD_TRAJECTORY",
        "evidence_role": "DIAGNOSTIC",
        "method_profile_id": HSP90_METHOD_PROFILE_ID,
        "analysis_contract_id": "HSP90_ATLAS_V1_20260728",
        "required_evidence_action": HSP90_TIME_ANATOMY_ACTION,
    }
    for field, expected in required_pairs.items():
        if source.get(field) != expected:
            raise VerticalSliceError(f"HSP90 source has an invalid {field}")
    time = _mapping(source.get("time_semantics"), "HSP90 source.time_semantics")
    if time.get("kind") != "ORDERED_TRAJECTORY":
        raise VerticalSliceError("HSP90 source must retain ordered trajectory semantics")
    identity = _mapping(source.get("trajectory_identity"), "HSP90 source.trajectory_identity")
    if identity.get("packet_id") != "hsp90_round2_40_trajectory_directional_packet":
        raise VerticalSliceError("HSP90 source has an unexpected trajectory packet")
    control = _mapping(source.get("time_anatomy_control"), "HSP90 source.time_anatomy_control")
    if control.get("persistence_saved_frames") != _HSP90_EXACT_FIXED_PARAMETERS[
        "persistence_saved_frames"
    ]:
        raise VerticalSliceError("HSP90 source has an unexpected persistence grid")
    expected = _HSP90_EXACT_TIME_CONTRACT
    comparisons = {
        "time_semantics.analysis_window_ns": time.get("analysis_window_ns"),
        "time_semantics.saved_stride_ns": time.get("saved_stride_ns"),
        "trajectory_identity.frame_dependence": identity.get("frame_dependence"),
        "trajectory_identity.frames_per_trajectory": identity.get("frames_per_trajectory"),
        "trajectory_identity.trajectory_count": identity.get("trajectory_count"),
        "time_anatomy_control.analysis_window_ns": control.get("analysis_window_ns"),
        "time_anatomy_control.frame_dependence": control.get("frame_dependence"),
        "time_anatomy_control.saved_stride_ns": control.get("saved_stride_ns"),
        "time_anatomy_control.statistical_unit": control.get("statistical_unit"),
        "time_anatomy_control.trajectory_count": control.get("trajectory_count"),
    }
    expected_values = {
        "time_semantics.analysis_window_ns": expected["analysis_window_ns"],
        "time_semantics.saved_stride_ns": expected["saved_stride_ns"],
        "trajectory_identity.frame_dependence": expected["frame_dependence"],
        "trajectory_identity.frames_per_trajectory": expected["frames_per_trajectory"],
        "trajectory_identity.trajectory_count": expected["trajectory_count"],
        "time_anatomy_control.analysis_window_ns": expected["analysis_window_ns"],
        "time_anatomy_control.frame_dependence": expected["frame_dependence"],
        "time_anatomy_control.saved_stride_ns": expected["saved_stride_ns"],
        "time_anatomy_control.statistical_unit": expected["statistical_unit"],
        "time_anatomy_control.trajectory_count": expected["trajectory_count"],
    }
    for path, observed in comparisons.items():
        if observed != expected_values[path]:
            raise VerticalSliceError(
                f"HSP90 CaseGraph {path} does not match the exact manifest contract"
            )


def _hsp90_rule_overlay_parts(
    rule_overlay: Mapping[str, Any],
) -> tuple[Mapping[str, Any], Mapping[str, Any], Mapping[str, Any], Mapping[str, Any]]:
    rule_overlay = _mapping(rule_overlay, "HSP90 rule overlay")
    if rule_overlay.get("schema_version") != "case-bound-rule-overlay/v1-alpha":
        raise VerticalSliceError("HSP90 rule overlay has an unknown schema version")
    subrule = _mapping(rule_overlay.get("runtime_subrule"), "HSP90 runtime_subrule")
    binding = _mapping(rule_overlay.get("binding"), "HSP90 binding")
    contract = _mapping(rule_overlay.get("evaluation_contract"), "HSP90 evaluation_contract")
    policy = _mapping(rule_overlay.get("resolution_policy"), "HSP90 resolution_policy")
    if subrule.get("runtime_subrule_id") != HSP90_RUNTIME_SUBRULE_ID:
        raise VerticalSliceError("HSP90 rule overlay has an unexpected RuleInstance type")
    if subrule.get("family_id") != "F04_SOURCE_RELIABILITY_AND_UNCERTAINTY":
        raise VerticalSliceError("HSP90 rule overlay must remain an F04 rule")
    if subrule.get("target_kind") != "SOURCE" or binding.get("target_kind") != "SOURCE":
        raise VerticalSliceError("HSP90 rule overlay must be SOURCE-targeted")
    if binding.get("runtime_subrule_id") != HSP90_RUNTIME_SUBRULE_ID:
        raise VerticalSliceError("HSP90 binding does not match its runtime sub-rule")
    if contract.get("runtime_subrule_id") != HSP90_RUNTIME_SUBRULE_ID:
        raise VerticalSliceError("HSP90 contract does not match its runtime sub-rule")
    if policy.get("resolution_policy_id") != binding.get("resolution_policy_id"):
        raise VerticalSliceError("HSP90 binding and resolution policy do not match")
    return subrule, binding, contract, policy


def _hsp90_rule_result(
    *,
    subrule: Mapping[str, Any],
    binding: Mapping[str, Any],
    contract: Mapping[str, Any],
    status: str,
    applicability_status: str,
    reason_codes: Sequence[str],
    missing_paths: Sequence[str],
) -> dict[str, Any]:
    if status not in {"PASS", "FAIL", "UNRESOLVED", "NOT_APPLICABLE"}:
        raise VerticalSliceError("HSP90 F04R02 has an invalid RuleResult status")
    source_id = HSP90_SOURCE_ID
    effect = _mapping(contract.get("result_effects"), "HSP90 contract.result_effects").get(status)
    effect = _mapping(effect, f"HSP90 result effect for {status}")
    return {
        "schema_version": "rules-prototype-rule-result/v1",
        "rule_instance_id": rule_instance_id(
            HSP90_RUNTIME_SUBRULE_ID, "SOURCE", source_id
        ),
        "runtime_subrule_id": HSP90_RUNTIME_SUBRULE_ID,
        "family_id": subrule["family_id"],
        "target": {"kind": "SOURCE", "id": source_id},
        "applicability_status": applicability_status,
        "status": status,
        "reason_codes": list(reason_codes),
        "missing_paths": list(missing_paths),
        "resolution_policy_id": binding["resolution_policy_id"],
        "evaluation_contract_id": contract["evaluation_contract_id"],
        "claim_effect": dict(effect),
        "scientific_verdict": "NOT_EMITTED_PROPOSAL_ONLY",
        "human_decision_gate_required": True,
        "human_decision_gate_id": contract["human_decision_gate_id"],
    }


class ExecutionEvidenceContext:
    """Verified Case-B execution state, kept outside the canonical CaseGraph.

    The context intentionally has no deserialization constructor and does not accept
    a loose EvidenceResult.  A record enters it only after the exact receipt,
    manifest, registry, and output files have been revalidated together.  This is a
    runtime provenance boundary, not a generic persistence format.
    """

    def __init__(self) -> None:
        self._evidence_results_by_rule_instance: dict[str, dict[str, Any]] = {}
        self._operator_runs_by_rule_instance: dict[str, dict[str, Any]] = {}

    @property
    def evidence_results_by_rule_instance(self) -> dict[str, dict[str, Any]]:
        """Return a copy for inspection without exposing mutable runtime state."""

        return deepcopy(self._evidence_results_by_rule_instance)

    def result_for(self, rule_id: str) -> Mapping[str, Any] | None:
        value = self._evidence_results_by_rule_instance.get(rule_id)
        return deepcopy(value) if value is not None else None

    def operator_run_for(self, rule_id: str) -> Mapping[str, Any] | None:
        value = self._operator_runs_by_rule_instance.get(rule_id)
        return deepcopy(value) if value is not None else None

    def record_validated_operator_run(
        self,
        *,
        operator_run: Mapping[str, Any],
        operator_registry: Mapping[str, Any],
        input_manifest: Mapping[str, Any],
        workspace_root: Path,
    ) -> None:
        """Admit one revalidated exact Case-B Operator run and no loose evidence."""

        self._record_validated_operator_run(
            operator_run=operator_run,
            operator_registry=operator_registry,
            input_manifest=input_manifest,
            workspace_root=workspace_root,
            output_location=_hsp90_historical_output_location(workspace_root),
        )

    def _record_validated_operator_run(
        self,
        *,
        operator_run: Mapping[str, Any],
        operator_registry: Mapping[str, Any],
        input_manifest: Mapping[str, Any],
        workspace_root: Path,
        output_location: _Hsp90OutputLocation,
    ) -> None:
        """Admit one exact receipt using a fixed historical or demo output binding."""

        validated = _validate_hsp90_operator_run_for_context(
            operator_run=operator_run,
            operator_registry=operator_registry,
            input_manifest=input_manifest,
            workspace_root=workspace_root,
            output_location=output_location,
        )
        rule_id = validated["evidence_result"]["affected_rule_instance_id"]
        if rule_id in self._evidence_results_by_rule_instance:
            raise VerticalSliceError("ExecutionEvidenceContext refuses duplicate EvidenceResults")
        self._evidence_results_by_rule_instance[rule_id] = deepcopy(
            validated["evidence_result"]
        )
        self._operator_runs_by_rule_instance[rule_id] = deepcopy(validated)


def _hsp90_required_paths_missing(source: Mapping[str, Any]) -> list[str]:
    def missing(path: str) -> bool:
        value: Any = source
        for part in path.split("."):
            if not isinstance(value, Mapping) or part not in value:
                return True
            value = value[part]
        return value is None or value == "" or value == []

    paths = (
        "method_profile_id",
        "analysis_contract_id",
        "time_semantics.kind",
        "trajectory_identity.packet_id",
        "trajectory_identity.trajectory_count",
        "trajectory_identity.frames_per_trajectory",
        "time_anatomy_control.analysis_window_ns",
        "time_anatomy_control.saved_stride_ns",
        "time_anatomy_control.statistical_unit",
        "time_anatomy_control.persistence_saved_frames",
    )
    return [f"source.{path}" for path in paths if missing(path)]


def evaluate_hsp90_time_anatomy_f04r02(
    *,
    case_graph: Mapping[str, Any],
    rule_overlay: Mapping[str, Any],
    input_manifest: Mapping[str, Any],
    evidence_context: ExecutionEvidenceContext | None = None,
    target_id: str = HSP90_SOURCE_ID,
) -> dict[str, Any]:
    """Evaluate only Case B's one F04 RuleInstance before or after execution.

    The pre-execution state is an actual computable-evidence gap.  A successful
    Operator run changes only this RuleInstance because the EvidenceResult is keyed
    outside CaseGraph by its stable RuleInstance identifier.
    """

    validate_hsp90_case_dossier(case_graph, input_manifest)
    subrule, binding, contract, _ = _hsp90_rule_overlay_parts(rule_overlay)
    if target_id != HSP90_SOURCE_ID:
        return _hsp90_rule_result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            status="NOT_APPLICABLE",
            applicability_status="WRONG_TARGET",
            reason_codes=["WRONG_TARGET_ID"],
            missing_paths=[],
        )
    source = _hsp90_source(case_graph)
    if (
        source.get("method_id") != "MD_TRAJECTORY"
        or source.get("required_evidence_action") != HSP90_TIME_ANATOMY_ACTION
    ):
        return _hsp90_rule_result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            status="NOT_APPLICABLE",
            applicability_status="NOT_MATCHED",
            reason_codes=["APPLICABILITY_PREDICATE_FALSE"],
            missing_paths=[],
        )
    missing_paths = _hsp90_required_paths_missing(source)
    if missing_paths:
        return _hsp90_rule_result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            status="UNRESOLVED",
            applicability_status="MATCHED",
            reason_codes=["REQUIRED_METHOD_PROFILE_OR_TIME_CONTROL_MISSING"],
            missing_paths=missing_paths,
        )

    context = evidence_context or ExecutionEvidenceContext()
    evidence = context.result_for(
        rule_instance_id(HSP90_RUNTIME_SUBRULE_ID, "SOURCE", HSP90_SOURCE_ID)
    )
    if evidence is None:
        return _hsp90_rule_result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            status="UNRESOLVED",
            applicability_status="MATCHED",
            reason_codes=["COMPUTABLE_TIME_ANATOMY_CONTROL_EVIDENCE_MISSING"],
            missing_paths=[],
        )
    if evidence.get("contract_status") == "FAIL":
        validation = evidence.get("output_validation")
        reason_codes = (
            list(validation.get("reason_codes", []))
            if isinstance(validation, Mapping)
            else []
        )
        return _hsp90_rule_result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            status="FAIL",
            applicability_status="MATCHED",
            reason_codes=reason_codes or ["TIME_ANATOMY_CONTROL_CONTRACT_INVALID"],
            missing_paths=[],
        )
    if evidence.get("contract_status") == "PASS":
        return _hsp90_rule_result(
            subrule=subrule,
            binding=binding,
            contract=contract,
            status="PASS",
            applicability_status="MATCHED",
            reason_codes=["CASE_BOUND_TIME_ANATOMY_CONTROL_EVIDENCE_VALIDATED"],
            missing_paths=[],
        )
    return _hsp90_rule_result(
        subrule=subrule,
        binding=binding,
        contract=contract,
        status="UNRESOLVED",
        applicability_status="MATCHED",
        reason_codes=["CASE_BOUND_EVIDENCE_RESULT_STATUS_UNRESOLVED"],
        missing_paths=[],
    )


def validate_hsp90_operator_input_manifest(
    *,
    input_manifest: Mapping[str, Any],
    operator_spec: Mapping[str, Any],
    workspace_root: Path,
) -> dict[str, Any]:
    """Verify exact case/input/implementation binding before the one Operator run."""

    input_manifest = _mapping(input_manifest, "HSP90 input manifest")
    _validate_hsp90_frozen_manifest_contract(input_manifest)
    operator_spec = _mapping(operator_spec, "HSP90 OperatorSpec")
    expected = {
        "case_id": HSP90_CASE_ID,
        "source_id": HSP90_SOURCE_ID,
        "runtime_subrule_id": HSP90_RUNTIME_SUBRULE_ID,
        "rule_instance_id": rule_instance_id(
            HSP90_RUNTIME_SUBRULE_ID, "SOURCE", HSP90_SOURCE_ID
        ),
        "operator_id": HSP90_OPERATOR_ID,
        "method_profile_id": HSP90_METHOD_PROFILE_ID,
        "capability_id": HSP90_CAPABILITY_ID,
    }
    for field, value in expected.items():
        if input_manifest.get(field) != value:
            raise VerticalSliceError(f"HSP90 input manifest has an invalid {field}")
    if operator_spec.get("operator_id") != HSP90_OPERATOR_ID:
        raise VerticalSliceError("HSP90 OperatorSpec identity does not match the manifest")
    if operator_spec.get("capability_id") != HSP90_CAPABILITY_ID:
        raise VerticalSliceError("HSP90 OperatorSpec capability does not match the manifest")
    if operator_spec.get("implementation_ref") != _mapping(
        input_manifest.get("implementation"), "HSP90 manifest.implementation"
    ).get("workspace_relative_path"):
        raise VerticalSliceError("HSP90 implementation path does not match the manifest")
    if operator_spec.get("fixed_inputs") != {
        name: _mapping(item, f"HSP90 manifest input {name}").get(
            "workspace_relative_path"
        )
        for name, item in _mapping(
            input_manifest.get("fixed_inputs"), "HSP90 manifest.fixed_inputs"
        ).items()
    }:
        raise VerticalSliceError("HSP90 fixed inputs do not match the manifest")
    if operator_spec.get("fixed_parameters") != input_manifest.get("fixed_parameters"):
        raise VerticalSliceError("HSP90 fixed parameters do not match the manifest")

    assets: dict[str, Mapping[str, Any]] = {
        "implementation": _mapping(
            input_manifest.get("implementation"), "HSP90 manifest.implementation"
        )
    }
    assets.update(
        {
            str(name): _mapping(item, f"HSP90 manifest input {name}")
            for name, item in _mapping(
                input_manifest.get("fixed_inputs"), "HSP90 manifest.fixed_inputs"
            ).items()
        }
    )
    resolved_assets: dict[str, dict[str, str]] = {}
    for name, asset in assets.items():
        path = _project_relative_path(workspace_root, asset.get("workspace_relative_path"))
        if not path.is_file():
            raise VerticalSliceError(f"HSP90 manifest asset is unavailable: {name}")
        observed_sha256 = _sha256(path)
        if observed_sha256 != asset.get("sha256"):
            raise VerticalSliceError(f"HSP90 manifest asset hash mismatch: {name}")
        resolved_assets[name] = {
            "workspace_relative_path": str(asset["workspace_relative_path"]),
            "sha256": observed_sha256,
        }
    return {
        "manifest_id": input_manifest.get("manifest_id"),
        "resolved_assets": resolved_assets,
        "expected_time_contract": input_manifest.get("expected_time_contract"),
        "fixed_parameters": input_manifest.get("fixed_parameters"),
    }


def _validate_exact_hsp90_exposed_development_scope(
    operator_spec: Mapping[str, Any],
) -> None:
    """Reject any shared-registry record that loosens the exposed B1 boundary."""

    for field, expected in _EXACT_HSP90_EXPOSED_DEVELOPMENT_SCOPE.items():
        if operator_spec.get(field) != expected:
            raise VerticalSliceError(
                f"HSP90 exact Operator has an invalid {field}: expected {expected}"
            )


def resolve_hsp90_time_anatomy_obligation(
    *,
    rule_result: Mapping[str, Any],
    case_graph: Mapping[str, Any],
    rule_overlay: Mapping[str, Any],
    operator_registry: Mapping[str, Any],
    input_manifest: Mapping[str, Any],
    workspace_root: Path,
) -> dict[str, Any]:
    """Match Case B's one real unresolved obligation to one eligible Operator."""

    validate_hsp90_case_dossier(case_graph, input_manifest)
    _, binding, _, policy = _hsp90_rule_overlay_parts(rule_overlay)
    rule_result = _mapping(rule_result, "HSP90 RuleResult")
    fresh_rule_result = evaluate_hsp90_time_anatomy_f04r02(
        case_graph=case_graph,
        rule_overlay=rule_overlay,
        input_manifest=input_manifest,
    )
    if dict(rule_result) != fresh_rule_result:
        raise VerticalSliceError(
            "HSP90 resolver requires the freshly produced exact Case-B RuleResult"
        )
    expected_rule_id = rule_instance_id(
        HSP90_RUNTIME_SUBRULE_ID, "SOURCE", HSP90_SOURCE_ID
    )
    if rule_result.get("rule_instance_id") != expected_rule_id:
        raise VerticalSliceError("HSP90 resolver received a different RuleInstance")
    if rule_result.get("resolution_policy_id") != binding.get("resolution_policy_id"):
        raise VerticalSliceError("HSP90 resolver received an unrelated resolution policy")
    if rule_result.get("status") != "UNRESOLVED" or "COMPUTABLE_TIME_ANATOMY_CONTROL_EVIDENCE_MISSING" not in rule_result.get("reason_codes", []):
        return {
            "route": "HUMAN_OR_NEW_DATA",
            "status": "NOT_ROUTABLE",
            "reason_code": "RULE_INSTANCE_IS_NOT_THE_COMPUTABLE_TIME_ANATOMY_GAP",
        }
    if policy.get("operator_route_allowed") is not True:
        raise VerticalSliceError("HSP90 resolution policy forbids an Operator route")
    operators = operator_registry.get("operators")
    spec = operators.get(HSP90_OPERATOR_ID) if isinstance(operators, Mapping) else None
    if not isinstance(spec, Mapping):
        return {
            "route": "HUMAN_OR_NEW_DATA",
            "status": "NOT_ROUTABLE",
            "reason_code": "EXACT_HSP90_OPERATOR_NOT_REGISTERED",
        }
    if spec.get("status") != "ROSTER_PASS" or spec.get("routable") is not True:
        return {
            "route": "HUMAN_OR_NEW_DATA",
            "status": "NOT_ROUTABLE",
            "reason_code": "EXACT_HSP90_OPERATOR_NOT_ROSTER_PASS_AND_ROUTABLE",
        }
    _validate_exact_hsp90_exposed_development_scope(spec)
    if spec.get("handler") != "case_bound_hsp90_time_anatomy_v1":
        raise VerticalSliceError("HSP90 OperatorSpec has an unsafe handler")
    if spec.get("capability_id") != HSP90_CAPABILITY_ID:
        raise VerticalSliceError("HSP90 OperatorSpec has an invalid capability")
    route_match = _mapping(spec.get("route_match"), "HSP90 OperatorSpec.route_match")
    expected_matches = {
        "runtime_subrule_ids": HSP90_RUNTIME_SUBRULE_ID,
        "gap_classes": "COMPUTABLE_TIME_ANATOMY_CONTROL_EVIDENCE_MISSING",
        "target_types": "SOURCE",
        "method_ids": "MD_TRAJECTORY",
        "case_ids": HSP90_CASE_ID,
        "source_ids": HSP90_SOURCE_ID,
        "method_profile_ids": HSP90_METHOD_PROFILE_ID,
    }
    for field, value in expected_matches.items():
        if value not in route_match.get(field, []):
            raise VerticalSliceError(f"HSP90 OperatorSpec lacks exact route match: {field}")
    manifest_receipt = validate_hsp90_operator_input_manifest(
        input_manifest=input_manifest,
        operator_spec=spec,
        workspace_root=workspace_root,
    )
    return {
        "route": "REGISTERED_OPERATOR",
        "status": "ROUTABLE",
        "operator_id": HSP90_OPERATOR_ID,
        "operator_scope": dict(_EXACT_HSP90_EXPOSED_DEVELOPMENT_SCOPE),
        "affected_rule_instance_id": expected_rule_id,
        "resolution_policy_id": binding["resolution_policy_id"],
        "manifest_receipt": manifest_receipt,
    }


_DIRECTIONAL_RUN_COLUMNS = (
    "trajectory",
    "seed_lineage",
    "label",
    "start_time_ns",
    "end_time_ns",
    "length_saved_frames",
    "length_ns",
)
_TIME_ANATOMY_COLUMNS = (
    "trajectory",
    "seed_lineage",
    "persistence_saved_frames",
    "persistence_ns",
    "first_persistent_direction",
    "first_persistent_start_ns",
    "opposite_direction_departure_candidate",
    "opposite_departure_start_ns",
    "return_candidate",
    "return_start_ns",
    "strict_core_frames",
)
_TIME_BIN_COLUMNS = (
    "trajectory",
    "seed_lineage",
    "bin_index",
    "start_time_ns",
    "end_time_ns",
    "n_saved_frames",
    "bin_route",
)


def _read_tsv(path: Path, expected_columns: Sequence[str]) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != tuple(expected_columns):
            raise VerticalSliceError(f"unexpected TSV columns: {path.name}")
        return list(reader)


def validate_hsp90_time_anatomy_outputs(
    *,
    output_dir: Path,
    input_manifest: Mapping[str, Any],
) -> dict[str, Any]:
    """Validate actual Case-B outputs without interpreting a biological result."""

    expected_files = {
        "directional_runs.tsv",
        "trajectory_time_anatomy.tsv",
        "trajectory_time_bins_50ns.tsv",
        "results_summary.json",
    }
    reason_codes: list[str] = []
    observed_counts: dict[str, int] = {}
    try:
        if not output_dir.is_dir():
            raise VerticalSliceError("operator output directory is missing")
        files = {path.name for path in output_dir.iterdir() if path.is_file()}
        if files != expected_files:
            raise VerticalSliceError("operator output file set is not exact")
        summary = json.loads((output_dir / "results_summary.json").read_text(encoding="utf-8"))
        if not isinstance(summary, Mapping):
            raise VerticalSliceError("results_summary is not a JSON object")
        expected_summary_keys = {
            "task",
            "evidence_level",
            "inputs",
            "statistical_unit",
            "persistence_grid_saved_frames",
            "display_bin",
            "summary",
            "allowed_wording",
            "forbidden_wording",
        }
        if set(summary) != expected_summary_keys:
            raise VerticalSliceError("results_summary does not match the exact output schema")
        if summary.get("evidence_level") != "v0_same_packet_diagnostic":
            raise VerticalSliceError("results_summary has an invalid evidence level")
        if summary.get("persistence_grid_saved_frames") != [5, 20, 50]:
            raise VerticalSliceError("results_summary has an invalid persistence grid")
        if "trajectory (n=40)" not in str(summary.get("statistical_unit")):
            raise VerticalSliceError("results_summary has an invalid statistical unit")
        manifest_inputs = _mapping(input_manifest.get("fixed_inputs"), "HSP90 manifest.fixed_inputs")
        summary_inputs = _mapping(summary.get("inputs"), "results_summary.inputs")
        for output_name, manifest_name in (
            ("frame_state_assignments.tsv", "frame_state_assignments"),
            ("route_predictions.tsv", "route_predictions"),
        ):
            expected_hash = _mapping(
                manifest_inputs.get(manifest_name), f"HSP90 manifest input {manifest_name}"
            ).get("sha256")
            actual_hash = _mapping(
                summary_inputs.get(output_name), f"results_summary input {output_name}"
            ).get("sha256")
            if actual_hash != expected_hash:
                raise VerticalSliceError(f"results_summary input hash mismatch: {output_name}")
        for prohibited in ("transition rate", "equilibrium", "population", "free energy", "mechanism"):
            if prohibited not in str(summary.get("forbidden_wording", "")).lower():
                raise VerticalSliceError(f"results_summary loses forbidden claim boundary: {prohibited}")

        directional_rows = _read_tsv(
            output_dir / "directional_runs.tsv", _DIRECTIONAL_RUN_COLUMNS
        )
        if not directional_rows:
            raise VerticalSliceError("directional_runs must contain rows")
        if len({tuple(row.get(field, "") for field in _DIRECTIONAL_RUN_COLUMNS) for row in directional_rows}) != len(directional_rows):
            raise VerticalSliceError("directional_runs contains duplicate rows")
        if not {row["label"] for row in directional_rows}.issubset(
            {"OPEN_CONSENSUS", "CLOSED_CONSENSUS", "READOUT_CONFLICT"}
        ):
            raise VerticalSliceError("directional_runs contains an unknown directional label")

        anatomy_rows = _read_tsv(
            output_dir / "trajectory_time_anatomy.tsv", _TIME_ANATOMY_COLUMNS
        )
        expected_pairs = {(row["trajectory"], row["persistence_saved_frames"]) for row in anatomy_rows}
        if len(anatomy_rows) != 120 or len(expected_pairs) != 120:
            raise VerticalSliceError("trajectory_time_anatomy must have one row per trajectory/horizon")
        horizons = {row["persistence_saved_frames"] for row in anatomy_rows}
        if horizons != {"5", "20", "50"}:
            raise VerticalSliceError("trajectory_time_anatomy has an invalid horizon set")
        if any(row["persistence_ns"] != row["persistence_saved_frames"] for row in anatomy_rows):
            raise VerticalSliceError("trajectory_time_anatomy has inconsistent time horizons")
        if any(
            len({row["trajectory"] for row in anatomy_rows if row["persistence_saved_frames"] == horizon}) != 40
            for horizon in horizons
        ):
            raise VerticalSliceError("trajectory_time_anatomy does not retain 40 trajectories per horizon")

        bin_rows = _read_tsv(
            output_dir / "trajectory_time_bins_50ns.tsv", _TIME_BIN_COLUMNS
        )
        expected_bin_pairs = {(row["trajectory"], row["bin_index"]) for row in bin_rows}
        if len(bin_rows) != 840 or len(expected_bin_pairs) != 840:
            raise VerticalSliceError("trajectory_time_bins must have one row per trajectory/bin")
        if len({row["trajectory"] for row in bin_rows}) != 40:
            raise VerticalSliceError("trajectory_time_bins does not retain 40 trajectories")
        if any(row["bin_route"] not in {"OPEN_CONSENSUS", "CLOSED_CONSENSUS", "READOUT_CONFLICT"} for row in bin_rows):
            raise VerticalSliceError("trajectory_time_bins contains an unknown directional label")

        summary_by_horizon = _mapping(summary.get("summary"), "results_summary.summary")
        if set(summary_by_horizon) != {"5", "20", "50"}:
            raise VerticalSliceError("results_summary has an invalid horizon summary")
        for horizon, result in summary_by_horizon.items():
            result = _mapping(result, f"results_summary.summary.{horizon}")
            if set(result) != {
                "n_trajectories",
                "opposite_departure_candidate_n",
                "return_candidate_n",
                "strict_core_frame_count_total",
                "by_seed_lineage",
            }:
                raise VerticalSliceError("results_summary horizon record has an unexpected schema")
            if result.get("n_trajectories") != 40:
                raise VerticalSliceError("results_summary does not retain n=40")
            by_lineage = _mapping(result.get("by_seed_lineage"), "results_summary.by_seed_lineage")
            if set(by_lineage) != {"closed_seeded", "open_seeded"}:
                raise VerticalSliceError("results_summary has an unexpected lineage schema")
            for lineage in by_lineage.values():
                if set(_mapping(lineage, "results_summary.lineage")) != {
                    "n_trajectories",
                    "opposite_departure_candidate_n",
                    "return_candidate_n",
                }:
                    raise VerticalSliceError("results_summary lineage record has an unexpected schema")
            if {
                item: _mapping(by_lineage.get(item), f"lineage {item}").get("n_trajectories")
                for item in ("closed_seeded", "open_seeded")
            } != {"closed_seeded": 20, "open_seeded": 20}:
                raise VerticalSliceError("results_summary has an invalid lineage cohort")
        observed_counts = {
            "directional_run_rows": len(directional_rows),
            "trajectory_time_anatomy_rows": len(anatomy_rows),
            "trajectory_time_bin_rows": len(bin_rows),
        }
    except (OSError, json.JSONDecodeError, VerticalSliceError, ValueError) as exc:
        reason_codes.append(f"OUTPUT_CONTRACT_INVALID:{exc}")

    if reason_codes:
        return {"status": "FAIL", "reason_codes": reason_codes, "observed_counts": observed_counts}
    return {
        "status": "PASS",
        "reason_codes": [],
        "observed_counts": observed_counts,
        "output_hashes": {
            name: _sha256(output_dir / name) for name in sorted(expected_files)
        },
    }


def _exact_hsp90_roster_operator(
    operator_registry: Mapping[str, Any],
) -> Mapping[str, Any]:
    """Return only the exposed B1 OperatorSpec when its lifecycle is exact."""

    operators = operator_registry.get("operators")
    spec = operators.get(HSP90_OPERATOR_ID) if isinstance(operators, Mapping) else None
    if not isinstance(spec, Mapping):
        raise VerticalSliceError("HSP90 exact case-bound Operator is not registered")
    if spec.get("operator_id") != HSP90_OPERATOR_ID:
        raise VerticalSliceError("HSP90 exact Operator has an invalid identity")
    if spec.get("status") != "ROSTER_PASS" or spec.get("routable") is not True:
        raise VerticalSliceError("HSP90 exact Operator is not ROSTER_PASS and routable")
    _validate_exact_hsp90_exposed_development_scope(spec)
    if spec.get("handler") != "case_bound_hsp90_time_anatomy_v1":
        raise VerticalSliceError("HSP90 exact Operator has an unsafe handler")
    if spec.get("capability_id") != HSP90_CAPABILITY_ID:
        raise VerticalSliceError("HSP90 exact Operator has an invalid capability")
    return spec


def _hsp90_historical_output_location(workspace_root: Path) -> _Hsp90OutputLocation:
    workspace_root = workspace_root.resolve()
    candidate = (workspace_root / HSP90_EXACT_OUTPUT_DIRECTORY).resolve()
    if not candidate.is_relative_to(workspace_root):
        raise VerticalSliceError("HSP90 exact output directory escapes the harness repository")
    return _Hsp90OutputLocation(
        output_dir=candidate,
        receipt_output_directory=HSP90_EXACT_OUTPUT_DIRECTORY,
    )


def _hsp90_reference_demo_output_location(output_root: Path) -> _Hsp90OutputLocation:
    """Bind the rerunnable demo to its one documented output subdirectory.

    This does not create a general output-routing mechanism.  It exists solely so
    the existing exact Case-B adapter can rerun from frozen repository inputs
    without touching the historical evidence directory.
    """

    output_root = output_root.resolve()
    candidate = (output_root / HSP90_REFERENCE_DEMO_OUTPUT_DIRECTORY).resolve()
    if not candidate.is_relative_to(output_root):
        raise VerticalSliceError("HSP90 reference-demo output directory escapes its output root")
    return _Hsp90OutputLocation(
        output_dir=candidate,
        receipt_output_directory=HSP90_REFERENCE_DEMO_OUTPUT_DIRECTORY,
    )


def validate_hsp90_operator_run_for_context(
    *,
    operator_run: Mapping[str, Any],
    operator_registry: Mapping[str, Any],
    input_manifest: Mapping[str, Any],
    workspace_root: Path,
) -> dict[str, dict[str, Any]]:
    """Revalidate the historical fixed-output Case-B receipt."""

    return _validate_hsp90_operator_run_for_context(
        operator_run=operator_run,
        operator_registry=operator_registry,
        input_manifest=input_manifest,
        workspace_root=workspace_root,
        output_location=_hsp90_historical_output_location(workspace_root),
    )


def _validate_hsp90_operator_run_for_context(
    *,
    operator_run: Mapping[str, Any],
    operator_registry: Mapping[str, Any],
    input_manifest: Mapping[str, Any],
    workspace_root: Path,
    output_location: _Hsp90OutputLocation,
) -> dict[str, dict[str, Any]]:
    """Revalidate receipt, exact files, and EvidenceResult before re-evaluation.

    This deliberately derives a trusted execution record from the current frozen
    files.  Merely supplying a mapping whose ``contract_status`` says ``PASS`` is
    never sufficient to change the RuleInstance.
    """

    operator_run = _mapping(operator_run, "HSP90 operator run")
    receipt = _mapping(operator_run.get("operator_run_receipt"), "HSP90 run receipt")
    evidence = _mapping(operator_run.get("evidence_result"), "HSP90 EvidenceResult")
    spec = _exact_hsp90_roster_operator(operator_registry)
    manifest_receipt = validate_hsp90_operator_input_manifest(
        input_manifest=input_manifest,
        operator_spec=spec,
        workspace_root=workspace_root,
    )
    expected_rule_id = rule_instance_id(
        HSP90_RUNTIME_SUBRULE_ID, "SOURCE", HSP90_SOURCE_ID
    )
    expected_receipt = {
        "schema_version": "operator-run-receipt/v1-alpha",
        "request_id": HSP90_EXACT_REQUEST_ID,
        "receipt_id": f"HSP90-TIME-ANATOMY-RECEIPT::{HSP90_EXACT_REQUEST_ID}",
        "case_id": HSP90_CASE_ID,
        "source_id": HSP90_SOURCE_ID,
        "affected_rule_instance_id": expected_rule_id,
        "operator_id": HSP90_OPERATOR_ID,
        "operator_version": spec.get("version"),
        "operator_registry_id": operator_registry.get("registry_id"),
        "input_manifest_id": manifest_receipt.get("manifest_id"),
        "manifest_receipt": manifest_receipt,
        "fixed_parameters": spec.get("fixed_parameters"),
        "output_contract": spec.get("output_contract"),
        "claim_ceiling": spec.get("claim_ceiling"),
    }
    for field, expected in expected_receipt.items():
        if receipt.get(field) != expected:
            raise VerticalSliceError(f"HSP90 run receipt has an invalid {field}")
    output_dir = output_location.output_dir
    if receipt.get("output_directory") != output_location.receipt_output_directory:
        raise VerticalSliceError("HSP90 run receipt has an unexpected output directory")
    validation = validate_hsp90_time_anatomy_outputs(
        output_dir=output_dir, input_manifest=input_manifest
    )
    if receipt.get("output_validation") != validation:
        raise VerticalSliceError("HSP90 run receipt does not match fresh output validation")
    expected_receipt_status = "SUCCEEDED" if validation["status"] == "PASS" else "FAILED"
    if receipt.get("status") != expected_receipt_status:
        raise VerticalSliceError("HSP90 run receipt status does not match output validation")
    expected_output_files = sorted(
        path.name for path in output_dir.iterdir() if path.is_file()
    )
    if receipt.get("output_files") != expected_output_files:
        raise VerticalSliceError("HSP90 run receipt output files do not match the frozen directory")

    expected_contract_status = "PASS" if validation["status"] == "PASS" else "FAIL"
    expected_evidence_status = "OBSERVED" if expected_contract_status == "PASS" else "NOT_PRODUCED"
    expected_evidence = {
        "schema_version": "evidence-result/v1-alpha",
        "evidence_result_id": f"HSP90-TIME-ANATOMY-EVIDENCE::{HSP90_EXACT_REQUEST_ID}",
        "case_id": HSP90_CASE_ID,
        "source_id": HSP90_SOURCE_ID,
        "affected_rule_instance_id": expected_rule_id,
        "operator_id": HSP90_OPERATOR_ID,
        "operator_version": spec.get("version"),
        "method_profile_id": HSP90_METHOD_PROFILE_ID,
        "operator_run_receipt_id": expected_receipt["receipt_id"],
        "status": expected_evidence_status,
        "contract_status": expected_contract_status,
        "scientific_evaluation_status": "PENDING_HUMAN_VALIDATION",
        "output_validation": validation,
        "claim_ceiling": spec.get("claim_ceiling"),
        "forbidden_claims": spec.get("forbidden_claims", []),
    }
    for field, expected in expected_evidence.items():
        if evidence.get(field) != expected:
            raise VerticalSliceError(f"HSP90 EvidenceResult has an invalid {field}")
    expected_result = (
        json.loads((output_dir / "results_summary.json").read_text(encoding="utf-8"))
        if expected_contract_status == "PASS"
        else None
    )
    if evidence.get("result") != expected_result:
        raise VerticalSliceError("HSP90 EvidenceResult does not match the frozen output summary")
    return {
        "operator_run_receipt": deepcopy(dict(receipt)),
        "evidence_result": deepcopy(dict(evidence)),
    }


def _run_hsp90_case_bound_operator(
    *,
    resolution: Mapping[str, Any],
    case_graph: Mapping[str, Any],
    rule_overlay: Mapping[str, Any],
    operator_registry: Mapping[str, Any],
    input_manifest: Mapping[str, Any],
    workspace_root: Path,
    output_location: _Hsp90OutputLocation,
    request_id: str,
) -> dict[str, dict[str, Any]]:
    """Execute the one exact HSP90 Operator and materialize a receipt/EvidenceResult."""

    resolution = _mapping(resolution, "HSP90 resolution")
    if request_id != HSP90_EXACT_REQUEST_ID:
        raise VerticalSliceError("HSP90 execution has an unexpected request ID")
    output_dir = output_location.output_dir
    fresh_rule_result = evaluate_hsp90_time_anatomy_f04r02(
        case_graph=case_graph,
        rule_overlay=rule_overlay,
        input_manifest=input_manifest,
    )
    expected_resolution = resolve_hsp90_time_anatomy_obligation(
        rule_result=fresh_rule_result,
        case_graph=case_graph,
        rule_overlay=rule_overlay,
        operator_registry=operator_registry,
        input_manifest=input_manifest,
        workspace_root=workspace_root,
    )
    if dict(resolution) != expected_resolution:
        raise VerticalSliceError("HSP90 execution requires the freshly resolved exact obligation")
    if resolution.get("route") != "REGISTERED_OPERATOR" or resolution.get("status") != "ROUTABLE":
        raise VerticalSliceError("HSP90 execution requires a routable exact resolution")
    if resolution.get("operator_id") != HSP90_OPERATOR_ID:
        raise VerticalSliceError("HSP90 execution received an unexpected Operator")
    expected_rule_id = rule_instance_id(
        HSP90_RUNTIME_SUBRULE_ID, "SOURCE", HSP90_SOURCE_ID
    )
    if resolution.get("affected_rule_instance_id") != expected_rule_id:
        raise VerticalSliceError("HSP90 execution received an unrelated RuleInstance")
    spec = _exact_hsp90_roster_operator(operator_registry)
    manifest_receipt = validate_hsp90_operator_input_manifest(
        input_manifest=input_manifest,
        operator_spec=spec,
        workspace_root=workspace_root,
    )
    receipt_base = {
        "schema_version": "operator-run-receipt/v1-alpha",
        "receipt_id": f"HSP90-TIME-ANATOMY-RECEIPT::{request_id}",
        "request_id": request_id,
        "case_id": HSP90_CASE_ID,
        "source_id": HSP90_SOURCE_ID,
        "affected_rule_instance_id": expected_rule_id,
        "operator_id": HSP90_OPERATOR_ID,
        "operator_version": spec.get("version"),
        "operator_registry_id": operator_registry.get("registry_id"),
        "input_manifest_id": manifest_receipt.get("manifest_id"),
        "manifest_receipt": manifest_receipt,
        "fixed_parameters": spec.get("fixed_parameters"),
        "output_contract": spec.get("output_contract"),
        "claim_ceiling": spec.get("claim_ceiling"),
    }
    try:
        payload = execute_hsp90_time_anatomy_adapter(
            spec=spec,
            workspace_root=workspace_root,
            output_dir=output_dir,
        )
        validation = validate_hsp90_time_anatomy_outputs(
            output_dir=output_dir, input_manifest=input_manifest
        )
    except (OSError, ValueError, VerticalSliceError) as exc:
        validation = {
            "status": "FAIL",
            "reason_codes": [f"OPERATOR_EXECUTION_FAILED:{exc}"],
            "observed_counts": {},
        }
        payload = {"output_files": [], "stdout_tail": ""}
    contract_status = "PASS" if validation["status"] == "PASS" else "FAIL"
    receipt = {
        **receipt_base,
        "status": "SUCCEEDED" if contract_status == "PASS" else "FAILED",
        "reason_codes": list(validation.get("reason_codes", [])),
        "output_directory": output_location.receipt_output_directory,
        "output_files": payload.get("output_files", []),
        "stdout_tail": payload.get("stdout_tail", ""),
        "output_validation": validation,
    }
    evidence_result = {
        "schema_version": "evidence-result/v1-alpha",
        "evidence_result_id": f"HSP90-TIME-ANATOMY-EVIDENCE::{request_id}",
        "case_id": HSP90_CASE_ID,
        "source_id": HSP90_SOURCE_ID,
        "affected_rule_instance_id": expected_rule_id,
        "operator_id": HSP90_OPERATOR_ID,
        "operator_version": spec.get("version"),
        "method_profile_id": HSP90_METHOD_PROFILE_ID,
        "operator_run_receipt_id": receipt["receipt_id"],
        "status": "OBSERVED" if contract_status == "PASS" else "NOT_PRODUCED",
        "contract_status": contract_status,
        "scientific_evaluation_status": "PENDING_HUMAN_VALIDATION",
        "output_validation": validation,
        "claim_ceiling": spec.get("claim_ceiling"),
        "forbidden_claims": spec.get("forbidden_claims", []),
        "result": payload.get("result") if contract_status == "PASS" else None,
    }
    return {"operator_run_receipt": receipt, "evidence_result": evidence_result}


def run_hsp90_case_bound_operator(
    *,
    resolution: Mapping[str, Any],
    case_graph: Mapping[str, Any],
    rule_overlay: Mapping[str, Any],
    operator_registry: Mapping[str, Any],
    input_manifest: Mapping[str, Any],
    workspace_root: Path,
    output_dir: Path,
    request_id: str,
) -> dict[str, dict[str, Any]]:
    """Execute the historical fixed-output Case-B operator route unchanged."""

    output_location = _hsp90_historical_output_location(workspace_root)
    if output_dir.resolve() != output_location.output_dir:
        raise VerticalSliceError("HSP90 execution has an unexpected output directory")
    return _run_hsp90_case_bound_operator(
        resolution=resolution,
        case_graph=case_graph,
        rule_overlay=rule_overlay,
        operator_registry=operator_registry,
        input_manifest=input_manifest,
        workspace_root=workspace_root,
        output_location=output_location,
        request_id=request_id,
    )


def _materialize_hsp90_conclusion_packet(
    *,
    case_graph: Mapping[str, Any],
    rule_overlay: Mapping[str, Any],
    input_manifest: Mapping[str, Any],
    operator_registry: Mapping[str, Any],
    workspace_root: Path,
    output_location: _Hsp90OutputLocation,
    rule_result: Mapping[str, Any],
    operator_run: Mapping[str, Any] | None,
    scenario_id: str,
) -> dict[str, Any]:
    """Materialize Case B's bounded terminal route without a scientific verdict."""

    validate_hsp90_case_dossier(case_graph, input_manifest)
    rule_result = _mapping(rule_result, "HSP90 RuleResult")
    context = ExecutionEvidenceContext()
    canonical_operator_run: Mapping[str, Any] | None = None
    if operator_run is not None:
        context._record_validated_operator_run(
            operator_run=operator_run,
            operator_registry=operator_registry,
            input_manifest=input_manifest,
            workspace_root=workspace_root,
            output_location=output_location,
        )
        canonical_operator_run = context.operator_run_for(
            rule_instance_id(HSP90_RUNTIME_SUBRULE_ID, "SOURCE", HSP90_SOURCE_ID)
        )
    canonical_rule_result = evaluate_hsp90_time_anatomy_f04r02(
        case_graph=case_graph,
        rule_overlay=rule_overlay,
        input_manifest=input_manifest,
        evidence_context=context,
    )
    if dict(rule_result) != canonical_rule_result:
        raise VerticalSliceError(
            "HSP90 ConclusionPacket requires the exact re-evaluated RuleResult"
        )
    status = canonical_rule_result["status"]
    if status == "PASS" and canonical_operator_run is None:
        raise VerticalSliceError(
            "HSP90 PASS ConclusionPacket requires a validated exact Operator run"
        )
    if status == "PASS":
        route_disposition = "RULE_CONTRACT_PASS"
        terminal_route = "REGISTERED_OPERATOR"
        first_failed = None
        next_action = "Human scientific review of the bounded same-packet diagnostic wording."
    elif status == "FAIL":
        route_disposition = "ABSTAIN"
        terminal_route = "HUMAN_OR_NEW_DATA"
        first_failed = rule_result
        next_action = "Resolve the failed exact Operator contract; do not reuse its output as evidence."
    else:
        route_disposition = "ABSTAIN"
        terminal_route = "HUMAN_OR_NEW_DATA"
        first_failed = rule_result
        next_action = "Resolve the missing time-anatomy control evidence through an exact registered Operator or new data."
    operator_results = [] if canonical_operator_run is None else [canonical_operator_run]
    case = _mapping(case_graph.get("case"), "HSP90 CaseGraph.case")
    packet = {
        "schema_version": "conclusion-packet/v1-alpha",
        "packet_kind": "EXPOSED_HSP90_RULE_TO_OPERATOR_V1_ALPHA",
        "development_status": "EXPOSED_DEVELOPMENT_ACTIVE",
        "scenario_id": scenario_id,
        "case_id": HSP90_CASE_ID,
        "terminal_route": terminal_route,
        "route_disposition": route_disposition,
        "scientific_disposition": "NOT_EVALUATED",
        "claim_ceiling": "At most, the exact frozen same-packet diagnostic has a validated trajectory-level control record. No transition rate, equilibrium, population, free-energy, pathway, mechanism, or mutation claim is emitted.",
        "human_decision_gate_required": True,
        "unsafe_claim_upgrade": False,
        "first_failed_dependency": (
            None
            if first_failed is None
            else {
                "rule_instance_id": first_failed.get("rule_instance_id"),
                "status": first_failed.get("status"),
                "reason_codes": list(first_failed.get("reason_codes", [])),
                "missing_paths": list(first_failed.get("missing_paths", [])),
            }
        ),
        "requested_claim": case["scientific_claim"],
        "selected_rule_instance_ids": [canonical_rule_result["rule_instance_id"]],
        "blocking_rule_instance_ids": (
            [] if status == "PASS" else [canonical_rule_result["rule_instance_id"]]
        ),
        "rule_results": [canonical_rule_result],
        "nonblocking_rule_results": [],
        "evidence_lookup_results": [],
        "operator_results": operator_results,
        "human_review_items": [
            "The EvidenceResult validates the exact execution contract, not source science or a biological mechanism.",
            "The diagnostic remains trajectory-level and same-packet; frames are correlated observations, not independent replicates.",
            "Any rate, equilibrium, population, free-energy, pathway, mechanism, or mutation wording is forbidden.",
        ],
        "next_action": next_action,
        "provenance": {
            "case_provenance": case_graph.get("case_provenance"),
            "source_id": HSP90_SOURCE_ID,
            "runtime_subrule_id": HSP90_RUNTIME_SUBRULE_ID,
            "operator_id": HSP90_OPERATOR_ID,
            "operator_scope": dict(_EXACT_HSP90_EXPOSED_DEVELOPMENT_SCOPE),
        },
    }
    validate_hsp90_conclusion_packet(packet)
    return packet


def materialize_hsp90_conclusion_packet(
    *,
    case_graph: Mapping[str, Any],
    rule_overlay: Mapping[str, Any],
    input_manifest: Mapping[str, Any],
    operator_registry: Mapping[str, Any],
    workspace_root: Path,
    rule_result: Mapping[str, Any],
    operator_run: Mapping[str, Any] | None,
    scenario_id: str,
) -> dict[str, Any]:
    """Materialize the historical fixed-output Case-B packet unchanged."""

    return _materialize_hsp90_conclusion_packet(
        case_graph=case_graph,
        rule_overlay=rule_overlay,
        input_manifest=input_manifest,
        operator_registry=operator_registry,
        workspace_root=workspace_root,
        output_location=_hsp90_historical_output_location(workspace_root),
        rule_result=rule_result,
        operator_run=operator_run,
        scenario_id=scenario_id,
    )


def run_hsp90_reference_demo_route(
    *,
    evidence_root: Path,
    operator_registry: Mapping[str, Any],
    workspace_root: Path,
    output_root: Path,
) -> dict[str, Any]:
    """Rerun only the exposed B1 route into the documented demo output tree.

    It reuses the existing case-bound resolution, adapter, receipt validation, and
    same-Rule reevaluation.  It is intentionally limited to the one frozen HSP90
    case and is not a reusable Operator router.
    """

    output_location = _hsp90_reference_demo_output_location(output_root)
    bundle = load_hsp90_case_bundle(evidence_root)
    pre_rule = evaluate_hsp90_time_anatomy_f04r02(
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        input_manifest=bundle["input_manifest"],
    )
    resolution = resolve_hsp90_time_anatomy_obligation(
        rule_result=pre_rule,
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        operator_registry=operator_registry,
        input_manifest=bundle["input_manifest"],
        workspace_root=workspace_root,
    )
    operator_run = _run_hsp90_case_bound_operator(
        resolution=resolution,
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        operator_registry=operator_registry,
        input_manifest=bundle["input_manifest"],
        workspace_root=workspace_root,
        output_location=output_location,
        request_id=HSP90_EXACT_REQUEST_ID,
    )
    evidence_context = ExecutionEvidenceContext()
    evidence_context._record_validated_operator_run(
        operator_run=operator_run,
        operator_registry=operator_registry,
        input_manifest=bundle["input_manifest"],
        workspace_root=workspace_root,
        output_location=output_location,
    )
    post_rule = evaluate_hsp90_time_anatomy_f04r02(
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        input_manifest=bundle["input_manifest"],
        evidence_context=evidence_context,
    )
    conclusion_packet = _materialize_hsp90_conclusion_packet(
        case_graph=bundle["case_graph"],
        rule_overlay=bundle["rule_overlay"],
        input_manifest=bundle["input_manifest"],
        operator_registry=operator_registry,
        workspace_root=workspace_root,
        output_location=output_location,
        rule_result=post_rule,
        operator_run=operator_run,
        scenario_id="HSP90_B1_OPERATOR_CONTRACT_PASS",
    )
    return {
        "pre_operator_rule_result": pre_rule,
        "resolution_route": resolution,
        "operator_run_receipt": operator_run["operator_run_receipt"],
        "evidence_result": operator_run["evidence_result"],
        "post_operator_rule_result": post_rule,
        "conclusion_packet": conclusion_packet,
        "run_receipt": {
            "run_kind": "EXPOSED_HSP90_RULE_TO_OPERATOR_REFERENCE_DEMO_V1",
            "case_id": HSP90_CASE_ID,
            "operator_id": HSP90_OPERATOR_ID,
            "network_accessed": False,
            "agent_calls": 0,
            "unregistered_tool_calls": 0,
            "development_status": "EXPOSED_DEVELOPMENT_ACTIVE",
            "scientific_disposition": "NOT_EVALUATED",
            "output_directory": output_location.receipt_output_directory,
            "boundary": "Exact case-bound rerun from frozen repository inputs; output-contract PASS remains PENDING_HUMAN_VALIDATION for science.",
        },
    }


def validate_hsp90_conclusion_packet(packet: Mapping[str, Any]) -> None:
    """Validate the narrow Case-B packet boundary."""

    packet = _mapping(packet, "HSP90 ConclusionPacket")
    required = {
        "schema_version",
        "packet_kind",
        "development_status",
        "scenario_id",
        "case_id",
        "terminal_route",
        "route_disposition",
        "scientific_disposition",
        "claim_ceiling",
        "human_decision_gate_required",
        "unsafe_claim_upgrade",
        "first_failed_dependency",
        "requested_claim",
        "selected_rule_instance_ids",
        "blocking_rule_instance_ids",
        "rule_results",
        "nonblocking_rule_results",
        "evidence_lookup_results",
        "operator_results",
        "human_review_items",
        "next_action",
        "provenance",
    }
    missing = sorted(required.difference(packet))
    if missing:
        raise VerticalSliceError("HSP90 ConclusionPacket missing: " + ", ".join(missing))
    if packet.get("case_id") != HSP90_CASE_ID:
        raise VerticalSliceError("HSP90 ConclusionPacket has an unexpected case")
    if packet.get("development_status") != "EXPOSED_DEVELOPMENT_ACTIVE":
        raise VerticalSliceError("HSP90 ConclusionPacket has an invalid development status")
    if packet.get("scientific_disposition") != "NOT_EVALUATED":
        raise VerticalSliceError("HSP90 ConclusionPacket must not emit a scientific disposition")
    if packet.get("human_decision_gate_required") is not True:
        raise VerticalSliceError("HSP90 ConclusionPacket must retain a HumanDecisionGate")
    if packet.get("unsafe_claim_upgrade") is not False:
        raise VerticalSliceError("HSP90 ConclusionPacket must reject claim upgrades")
    if packet.get("route_disposition") not in {
        "RULE_CONTRACT_PASS",
        "ABSTAIN",
    }:
        raise VerticalSliceError("HSP90 ConclusionPacket has an unknown route disposition")
    expected_rule_id = rule_instance_id(
        HSP90_RUNTIME_SUBRULE_ID, "SOURCE", HSP90_SOURCE_ID
    )
    rule_results = packet.get("rule_results")
    if not isinstance(rule_results, list) or len(rule_results) != 1:
        raise VerticalSliceError("HSP90 ConclusionPacket must retain exactly one RuleResult")
    result = _mapping(rule_results[0], "HSP90 ConclusionPacket RuleResult")
    if result.get("rule_instance_id") != expected_rule_id:
        raise VerticalSliceError("HSP90 ConclusionPacket has an unrelated RuleInstance")
    if packet.get("selected_rule_instance_ids") != [expected_rule_id]:
        raise VerticalSliceError("HSP90 ConclusionPacket has invalid selected RuleInstances")
    operator_results = packet.get("operator_results")
    if not isinstance(operator_results, list):
        raise VerticalSliceError("HSP90 ConclusionPacket must retain Operator results")
    if result.get("status") == "PASS":
        if packet.get("terminal_route") != "REGISTERED_OPERATOR":
            raise VerticalSliceError("HSP90 PASS ConclusionPacket has an invalid route")
        if packet.get("route_disposition") != "RULE_CONTRACT_PASS":
            raise VerticalSliceError("HSP90 PASS ConclusionPacket has an invalid route disposition")
        if len(operator_results) != 1:
            raise VerticalSliceError("HSP90 PASS ConclusionPacket needs one Operator run")
        run = _mapping(operator_results[0], "HSP90 ConclusionPacket Operator run")
        receipt = _mapping(run.get("operator_run_receipt"), "HSP90 ConclusionPacket receipt")
        evidence = _mapping(run.get("evidence_result"), "HSP90 ConclusionPacket evidence")
        if (
            receipt.get("affected_rule_instance_id") != expected_rule_id
            or evidence.get("affected_rule_instance_id") != expected_rule_id
            or receipt.get("status") != "SUCCEEDED"
            or evidence.get("contract_status") != "PASS"
            or evidence.get("scientific_evaluation_status") != "PENDING_HUMAN_VALIDATION"
            or evidence.get("operator_run_receipt_id") != receipt.get("receipt_id")
        ):
            raise VerticalSliceError("HSP90 PASS ConclusionPacket lacks linked validated evidence")
    elif packet.get("route_disposition") != "ABSTAIN":
        raise VerticalSliceError("HSP90 non-PASS ConclusionPacket must abstain")
