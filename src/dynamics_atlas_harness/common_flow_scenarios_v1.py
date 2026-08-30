"""Deterministic common-flow scenarios over the existing exact case routes.

This module is a thin orchestration and artifact-writing layer.  It does not add
an evaluator, lookup mechanism, Operator dispatcher, or conclusion reducer.  The
four route families and three terminal behaviors below are recomputed through
the existing X-EISD, exact HSP90-control, and minimal Stage-2 implementations.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Mapping, Sequence

from .minimal_stage2_exposed_conclusions_v1 import (
    materialize_stage2_conclusion_packet,
    source_grounding_by_family,
)
from .real_case_vertical_slice_v1 import (
    HSP90_CASE_ID,
    X_EISD_CASE_ID,
    X_EISD_FROZEN_SELECTED_RULE_INSTANCE_IDS,
    apply_lookup_result,
    derive_declaration_attestations,
    evaluate_xeisd_case,
    execute_exact_source_lookup,
    load_json_object,
    load_rules_v1_bundle,
    materialize_xeisd_conclusion_packet,
    run_hsp90_reference_demo_route,
)
from .registered_operators import load_registered_operator_registry


SCENARIO_SUITE_SCHEMA_VERSION = "common-flow-scenario-suite/v1"
SCENARIO_MATRIX_SCHEMA_VERSION = "common-flow-scenario-matrix/v1"
SCENARIO_RECEIPT_SCHEMA_VERSION = "common-flow-scenario-receipt/v1"
SCENARIO_SUITE_RUN_ID = "common_flow_scenarios_v1"

DIRECT_SCENARIO_ID = "A_DIRECT_EVALUATION_XEISD_A1"
LOOKUP_SCENARIO_ID = "B_NARROW_LOOKUP_XEISD_RANDOM_COMPOSITION"
COMPUTATION_SCENARIO_ID = "C_REGISTERED_COMPUTATION_HSP90_EXACT_CONTROL"
STOP_SCENARIO_ID = "D_EXPLICIT_STOP_XEISD_MISSING_COMPOSITION"
SYNTHETIC_SUPPORT_SCENARIO_ID = "T1_SUPPORT_SYNTHETIC_CONTRACT_BEHAVIOR_ONLY"
CANNOT_SUPPORT_SCENARIO_ID = "T2_CANNOT_SUPPORT_XEISD_EXPLICIT_MISMATCH"

_SCENARIO_ORDER = (
    DIRECT_SCENARIO_ID,
    LOOKUP_SCENARIO_ID,
    COMPUTATION_SCENARIO_ID,
    STOP_SCENARIO_ID,
    SYNTHETIC_SUPPORT_SCENARIO_ID,
    CANNOT_SUPPORT_SCENARIO_ID,
)
_RANDOM_COMPOSITION_LOOKUP_ID = "XEI-LOOKUP-RANDOM-DECLARATIONS"
_MISSING_COMPOSITION_LOOKUP_ID = "XEI-LOOKUP-MISSING-COMPOSITION"
_RANDOM_SOURCE_ID = "xeisd_random_candidate_pool"
_RANDOM_COMPOSITION_RULE_INSTANCE_ID = X_EISD_FROZEN_SELECTED_RULE_INSTANCE_IDS[0]
_EXPECTED_TERMINAL_DISPOSITIONS = {
    DIRECT_SCENARIO_ID: "ABSTAIN_OR_HUMAN_REVIEW",
    LOOKUP_SCENARIO_ID: "ABSTAIN_OR_HUMAN_REVIEW",
    COMPUTATION_SCENARIO_ID: "ABSTAIN_OR_HUMAN_REVIEW",
    STOP_SCENARIO_ID: "ABSTAIN_OR_HUMAN_REVIEW",
    SYNTHETIC_SUPPORT_SCENARIO_ID: "SUPPORT_WITHIN_CEILING",
    CANNOT_SUPPORT_SCENARIO_ID: "CANNOT_SUPPORT_REQUESTED_CLAIM",
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _prepare_output_dir(output_dir: Path) -> Path:
    output_dir = output_dir.resolve()
    if output_dir.exists() and (not output_dir.is_dir() or any(output_dir.iterdir())):
        raise ValueError("OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )


def _relative_path(path: Path, output_dir: Path) -> str:
    return path.relative_to(output_dir).as_posix()


def _scenario_dir(output_dir: Path, scenario_id: str) -> Path:
    return output_dir / "scenarios" / scenario_id


def _lookup_request(allowlist: Mapping[str, Any], lookup_id: str) -> dict[str, str]:
    entries = allowlist.get("entries")
    if not isinstance(entries, Sequence) or isinstance(entries, (str, bytes)):
        raise ValueError("X_EISD_ALLOWLIST_ENTRIES_MISSING")
    entry = next(
        (
            item
            for item in entries
            if isinstance(item, Mapping) and item.get("lookup_id") == lookup_id
        ),
        None,
    )
    if not isinstance(entry, Mapping):
        raise ValueError(f"X_EISD_ALLOWLIST_ENTRY_MISSING:{lookup_id}")
    return {
        "lookup_id": lookup_id,
        "case_id": X_EISD_CASE_ID,
        "target_kind": str(entry["target_kind"]),
        "target_id": str(entry["target_id"]),
        "locator_id": str(entry["locator_id"]),
    }


def _missing_lookup_request() -> dict[str, str]:
    return {
        "lookup_id": _MISSING_COMPOSITION_LOOKUP_ID,
        "case_id": X_EISD_CASE_ID,
        "target_kind": "SOURCE",
        "target_id": _RANDOM_SOURCE_ID,
        "locator_id": "XEI-M04",
    }


def _rule_by_id(
    rule_results: Sequence[Mapping[str, Any]], rule_instance_id: str
) -> dict[str, Any]:
    matches = [
        result
        for result in rule_results
        if result.get("rule_instance_id") == rule_instance_id
    ]
    if len(matches) != 1:
        raise ValueError(
            f"EXPECTED_ONE_RULE_RESULT:{rule_instance_id}:OBSERVED:{len(matches)}"
        )
    return copy.deepcopy(dict(matches[0]))


def _rule_summary(rule_result: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "rule_instance_id": rule_result.get("rule_instance_id"),
        "status": rule_result.get("status"),
        "reason_codes": list(rule_result.get("reason_codes", [])),
        "missing_paths": list(rule_result.get("missing_paths", [])),
    }


def _status_counts(rule_results: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for result in rule_results:
        status = str(result.get("status", "UNKNOWN"))
        counts[status] = counts.get(status, 0) + 1
    return dict(sorted(counts.items()))


def _status_transitions(
    before_results: Sequence[Mapping[str, Any]],
    after_results: Sequence[Mapping[str, Any]],
) -> list[dict[str, str]]:
    before_by_id = {
        str(result.get("rule_instance_id")): str(result.get("status"))
        for result in before_results
    }
    after_by_id = {
        str(result.get("rule_instance_id")): str(result.get("status"))
        for result in after_results
    }
    if set(before_by_id) != set(after_by_id):
        raise ValueError("RULE_INVENTORY_CHANGED_DURING_REEVALUATION")
    return [
        {
            "rule_instance_id": rule_id,
            "before_status": before_by_id[rule_id],
            "after_status": after_by_id[rule_id],
        }
        for rule_id in sorted(before_by_id)
        if before_by_id[rule_id] != after_by_id[rule_id]
    ]


def _remove_random_composition(complete_graph: Mapping[str, Any]) -> dict[str, Any]:
    graph = copy.deepcopy(dict(complete_graph))
    sources = graph.get("evidence_items")
    if not isinstance(sources, list):
        raise ValueError("X_EISD_EVIDENCE_ITEMS_MISSING")
    source = next(
        (
            item
            for item in sources
            if isinstance(item, dict) and item.get("source_id") == _RANDOM_SOURCE_ID
        ),
        None,
    )
    if not isinstance(source, dict):
        raise ValueError("X_EISD_RANDOM_SOURCE_MISSING")
    source.pop("sample_composition", None)
    source.pop("sample_system_composition_declaration_status", None)
    attestations = source.get("lookup_attestations", [])
    if not isinstance(attestations, list):
        raise ValueError("X_EISD_LOOKUP_ATTESTATIONS_INVALID")
    source["lookup_attestations"] = [
        item for item in attestations if item != _RANDOM_COMPOSITION_LOOKUP_ID
    ]
    return graph


def _stage2_packet(
    *,
    route_packet: Mapping[str, Any],
    source_grounding: Mapping[str, str],
    scenario_id: str,
    route_artifact_path: str,
) -> dict[str, Any]:
    packet = materialize_stage2_conclusion_packet(
        route_packet=route_packet,
        source_grounding=source_grounding,
        scenario_id=scenario_id,
        route_artifact_path=route_artifact_path,
    )
    expected = _EXPECTED_TERMINAL_DISPOSITIONS[scenario_id]
    if packet.get("terminal_disposition") != expected:
        raise ValueError(
            f"SCENARIO_TERMINAL_DISPOSITION_CHANGED:{scenario_id}:"
            f"{packet.get('terminal_disposition')}"
        )
    return packet


def _write_scenario_receipt(
    *, scenario_dir: Path, output_dir: Path, row: Mapping[str, Any]
) -> None:
    receipt = {
        "schema_version": SCENARIO_RECEIPT_SCHEMA_VERSION,
        **copy.deepcopy(dict(row)),
    }
    receipt_path = scenario_dir / "scenario_receipt.json"
    _write_json(receipt_path, receipt)
    artifact_paths = row.get("artifact_paths")
    if not isinstance(artifact_paths, list):
        raise ValueError("SCENARIO_ARTIFACT_PATHS_MISSING")
    expected_path = _relative_path(receipt_path, output_dir)
    if expected_path not in artifact_paths:
        raise ValueError("SCENARIO_RECEIPT_PATH_NOT_DECLARED")


def _base_row(
    *,
    scenario_id: str,
    case_id: str,
    input_role: str,
    expected_route_family: str,
    actual_route: str,
    deterministic_authorization: str,
    action_count: int,
    evidence_result_class: str,
    affected_rule_instance: str | None,
    before_rule_result: Mapping[str, Any] | None,
    after_rule_result: Mapping[str, Any] | None,
    terminal_reducer_state: str,
    claim_ceiling: str,
    artifact_paths: Sequence[str],
    authority_status: str,
) -> dict[str, Any]:
    return {
        "scenario_id": scenario_id,
        "case_id": case_id,
        "input_role": input_role,
        "expected_route_family": expected_route_family,
        "actual_route": actual_route,
        "agent_mode": "NO_AGENT_DETERMINISTIC_SCENARIO",
        "deterministic_authorization": deterministic_authorization,
        "action_count": action_count,
        "evidence_result_class": evidence_result_class,
        "affected_rule_instance": affected_rule_instance,
        "before_rule_result": (
            None if before_rule_result is None else copy.deepcopy(dict(before_rule_result))
        ),
        "after_rule_result": (
            None if after_rule_result is None else copy.deepcopy(dict(after_rule_result))
        ),
        "terminal_reducer_state": terminal_reducer_state,
        "claim_ceiling": claim_ceiling,
        "actual_cost": 0.0,
        "result_status": "SUCCEEDED",
        "authority_status": authority_status,
        "artifact_paths": list(artifact_paths),
    }


def run_common_flow_scenario_suite(*, output_dir: Path) -> dict[str, Any]:
    """Materialize the four exact routes and three bounded reducer behaviors."""

    repo_root = _repo_root()
    output_dir = _prepare_output_dir(output_dir)
    evidence_root = repo_root / "evidence" / "real_case_vertical_slice_v1"
    rules_root = repo_root / "registries" / "rules_v1"
    complete_graph_path = evidence_root / "outputs" / "xeisd_a1_complete_casegraph.json"
    allowlist_path = evidence_root / "xeisd_source_lookup_allowlist_v1.json"
    family_overlay_path = rules_root / "family_overlay_v1.json"

    complete_graph = load_json_object(complete_graph_path)
    allowlist = load_json_object(allowlist_path)
    rules_bundle = load_rules_v1_bundle(rules_root)
    real_source_grounding = source_grounding_by_family(
        load_json_object(family_overlay_path)
    )
    rows: list[dict[str, Any]] = []

    # A: existing structured evidence goes directly through the frozen evaluator.
    direct_dir = _scenario_dir(output_dir, DIRECT_SCENARIO_ID)
    direct_results = evaluate_xeisd_case(
        case_graph=complete_graph, **rules_bundle
    )
    direct_route = materialize_xeisd_conclusion_packet(
        case_graph=complete_graph,
        rule_results=direct_results,
        lookup_results=[],
        scenario_id=DIRECT_SCENARIO_ID,
    )
    direct_route_path = direct_dir / "route_packet.json"
    direct_stage2_path = direct_dir / "stage2_conclusion_packet.json"
    direct_artifacts = [
        _relative_path(direct_dir / "input_casegraph.json", output_dir),
        _relative_path(direct_dir / "rule_results.json", output_dir),
        _relative_path(direct_route_path, output_dir),
        _relative_path(direct_stage2_path, output_dir),
        _relative_path(direct_dir / "scenario_receipt.json", output_dir),
    ]
    direct_stage2 = _stage2_packet(
        route_packet=direct_route,
        source_grounding=real_source_grounding,
        scenario_id=DIRECT_SCENARIO_ID,
        route_artifact_path=_relative_path(direct_route_path, output_dir),
    )
    if direct_route.get("terminal_route") != "DIRECT_EVALUATION":
        raise ValueError("DIRECT_SCENARIO_ROUTE_CHANGED")
    _write_json(direct_dir / "input_casegraph.json", complete_graph)
    _write_json(direct_dir / "rule_results.json", direct_results)
    _write_json(direct_route_path, direct_route)
    _write_json(direct_stage2_path, direct_stage2)
    direct_row = _base_row(
        scenario_id=DIRECT_SCENARIO_ID,
        case_id=X_EISD_CASE_ID,
        input_role="EXISTING_STRUCTURED_EVIDENCE",
        expected_route_family="DIRECT_EVALUATION",
        actual_route=str(direct_route["terminal_route"]),
        deterministic_authorization="NOT_REQUIRED_DIRECT_EVALUATION",
        action_count=0,
        evidence_result_class="NONE_DIRECT_EVALUATION",
        affected_rule_instance=None,
        before_rule_result=None,
        after_rule_result={
            "scope": "FROZEN_XEISD_REQUIRED_RULE_INVENTORY",
            "status_counts": _status_counts(direct_route["rule_results"]),
        },
        terminal_reducer_state=str(direct_stage2["terminal_disposition"]),
        claim_ceiling=str(direct_stage2["current_claim_ceiling"]),
        artifact_paths=direct_artifacts,
        authority_status="REAL_REPOSITORY_SOURCE_REVIEW_STATUS_RETAINED",
    )
    _write_scenario_receipt(
        scenario_dir=direct_dir, output_dir=output_dir, row=direct_row
    )
    rows.append(direct_row)

    # B: one exact source fact is attached, then the same target RuleInstance is
    # inspected before and after fresh deterministic reevaluation.  Downstream
    # dependent Rule transitions are recorded rather than hidden.
    lookup_dir = _scenario_dir(output_dir, LOOKUP_SCENARIO_ID)
    lookup_before_graph = _remove_random_composition(complete_graph)
    lookup_before_results = evaluate_xeisd_case(
        case_graph=lookup_before_graph, **rules_bundle
    )
    lookup_request = _lookup_request(allowlist, _RANDOM_COMPOSITION_LOOKUP_ID)
    lookup_result = execute_exact_source_lookup(
        allowlist=allowlist,
        request=lookup_request,
        workspace_root=repo_root,
    )
    if lookup_result.get("status") != "FOUND" or lookup_result.get("route") != "SOURCE_LOOKUP":
        raise ValueError("NARROW_LOOKUP_NOT_AUTHORIZED")
    lookup_after_graph = apply_lookup_result(
        case_graph=lookup_before_graph, lookup_result=lookup_result
    )
    lookup_after_graph = derive_declaration_attestations(
        case_graph=lookup_after_graph, lookup_results=[lookup_result]
    )
    lookup_after_results = evaluate_xeisd_case(
        case_graph=lookup_after_graph, **rules_bundle
    )
    lookup_before_target = _rule_by_id(
        lookup_before_results, _RANDOM_COMPOSITION_RULE_INSTANCE_ID
    )
    lookup_after_target = _rule_by_id(
        lookup_after_results, _RANDOM_COMPOSITION_RULE_INSTANCE_ID
    )
    if (
        lookup_before_target.get("status") != "UNRESOLVED"
        or lookup_after_target.get("status") != "PASS"
    ):
        raise ValueError("NARROW_LOOKUP_SAME_RULE_TRANSITION_CHANGED")
    lookup_transitions = _status_transitions(
        lookup_before_results, lookup_after_results
    )
    if _RANDOM_COMPOSITION_RULE_INSTANCE_ID not in {
        item["rule_instance_id"] for item in lookup_transitions
    }:
        raise ValueError("NARROW_LOOKUP_TARGET_RULE_NOT_REEVALUATED")
    lookup_route = materialize_xeisd_conclusion_packet(
        case_graph=lookup_after_graph,
        rule_results=lookup_after_results,
        lookup_results=[lookup_result],
        scenario_id=LOOKUP_SCENARIO_ID,
    )
    lookup_route_path = lookup_dir / "route_packet.json"
    lookup_stage2_path = lookup_dir / "stage2_conclusion_packet.json"
    lookup_artifact_names = (
        "input_casegraph_before.json",
        "before_rule_results.json",
        "lookup_request.json",
        "lookup_result.json",
        "input_casegraph_after.json",
        "after_rule_results.json",
        "rule_transition.json",
        "route_packet.json",
        "stage2_conclusion_packet.json",
        "scenario_receipt.json",
    )
    lookup_artifacts = [
        _relative_path(lookup_dir / name, output_dir)
        for name in lookup_artifact_names
    ]
    lookup_stage2 = _stage2_packet(
        route_packet=lookup_route,
        source_grounding=real_source_grounding,
        scenario_id=LOOKUP_SCENARIO_ID,
        route_artifact_path=_relative_path(lookup_route_path, output_dir),
    )
    _write_json(lookup_dir / "input_casegraph_before.json", lookup_before_graph)
    _write_json(lookup_dir / "before_rule_results.json", lookup_before_results)
    _write_json(lookup_dir / "lookup_request.json", lookup_request)
    _write_json(lookup_dir / "lookup_result.json", lookup_result)
    _write_json(lookup_dir / "input_casegraph_after.json", lookup_after_graph)
    _write_json(lookup_dir / "after_rule_results.json", lookup_after_results)
    _write_json(
        lookup_dir / "rule_transition.json",
        {
            "affected_rule_instance_id": _RANDOM_COMPOSITION_RULE_INSTANCE_ID,
            "before_rule_result": lookup_before_target,
            "after_rule_result": lookup_after_target,
            "all_changed_rule_statuses": lookup_transitions,
            "boundary": "The lookup is attached to one exact source fact. Fresh deterministic reevaluation may also update declared downstream Rule dependencies; those transitions are recorded explicitly.",
        },
    )
    _write_json(lookup_route_path, lookup_route)
    _write_json(lookup_stage2_path, lookup_stage2)
    lookup_row = _base_row(
        scenario_id=LOOKUP_SCENARIO_ID,
        case_id=X_EISD_CASE_ID,
        input_role="MISSING_EXACT_SOURCE_FACT",
        expected_route_family="NARROW_LOOKUP",
        actual_route="SOURCE_LOOKUP_THEN_DIRECT_EVALUATION",
        deterministic_authorization="AUTHORIZED_EXACT_ALLOWLIST_HASH_LOCATOR",
        action_count=1,
        evidence_result_class="SOURCE_LOOKUP_RESULT",
        affected_rule_instance=_RANDOM_COMPOSITION_RULE_INSTANCE_ID,
        before_rule_result=_rule_summary(lookup_before_target),
        after_rule_result=_rule_summary(lookup_after_target),
        terminal_reducer_state=str(lookup_stage2["terminal_disposition"]),
        claim_ceiling=str(lookup_stage2["current_claim_ceiling"]),
        artifact_paths=lookup_artifacts,
        authority_status="REAL_REPOSITORY_SOURCE_REVIEW_STATUS_RETAINED",
    )
    _write_scenario_receipt(
        scenario_dir=lookup_dir, output_dir=output_dir, row=lookup_row
    )
    rows.append(lookup_row)

    # C: use the existing exact HSP90 control route, including actual-output
    # validation and its case-bound same-Rule ExecutionEvidenceContext.
    computation_dir = _scenario_dir(output_dir, COMPUTATION_SCENARIO_ID)
    hsp90 = run_hsp90_reference_demo_route(
        evidence_root=evidence_root,
        operator_registry=load_registered_operator_registry(
            repo_root / "config" / "registered_operators.json"
        ),
        workspace_root=repo_root,
        output_root=computation_dir,
    )
    hsp90_rule_id = str(hsp90["evidence_result"]["affected_rule_instance_id"])
    if (
        hsp90["pre_operator_rule_result"].get("rule_instance_id") != hsp90_rule_id
        or hsp90["post_operator_rule_result"].get("rule_instance_id") != hsp90_rule_id
        or hsp90["operator_run_receipt"].get("affected_rule_instance_id") != hsp90_rule_id
        or hsp90["pre_operator_rule_result"].get("status") != "UNRESOLVED"
        or hsp90["post_operator_rule_result"].get("status") != "PASS"
    ):
        raise ValueError("HSP90_EXACT_CONTROL_SAME_RULE_TRANSITION_CHANGED")
    computation_route_path = computation_dir / "conclusion_packet.json"
    computation_stage2_path = computation_dir / "stage2_conclusion_packet.json"
    computation_artifact_names = (
        "pre_rule_result.json",
        "resolution_route.json",
        "operator_run_receipt.json",
        "evidence_result.json",
        "post_rule_result.json",
        "conclusion_packet.json",
        "stage2_conclusion_packet.json",
        "run_receipt.json",
        "scenario_receipt.json",
    )
    computation_artifacts = [
        _relative_path(computation_dir / name, output_dir)
        for name in computation_artifact_names
    ]
    computation_artifacts.extend(
        _relative_path(path, output_dir)
        for path in sorted(
            (computation_dir / "routes" / "hsp90_b1" / "operator_outputs").glob("*")
        )
        if path.is_file()
    )
    computation_stage2 = _stage2_packet(
        route_packet=hsp90["conclusion_packet"],
        source_grounding=real_source_grounding,
        scenario_id=COMPUTATION_SCENARIO_ID,
        route_artifact_path=_relative_path(computation_route_path, output_dir),
    )
    _write_json(computation_dir / "pre_rule_result.json", hsp90["pre_operator_rule_result"])
    _write_json(computation_dir / "resolution_route.json", hsp90["resolution_route"])
    _write_json(computation_dir / "operator_run_receipt.json", hsp90["operator_run_receipt"])
    _write_json(computation_dir / "evidence_result.json", hsp90["evidence_result"])
    _write_json(computation_dir / "post_rule_result.json", hsp90["post_operator_rule_result"])
    _write_json(computation_route_path, hsp90["conclusion_packet"])
    _write_json(computation_stage2_path, computation_stage2)
    _write_json(computation_dir / "run_receipt.json", hsp90["run_receipt"])
    computation_row = _base_row(
        scenario_id=COMPUTATION_SCENARIO_ID,
        case_id=HSP90_CASE_ID,
        input_role="COMPUTABLE_EXACT_CONTROL_EVIDENCE_MISSING",
        expected_route_family="REGISTERED_COMPUTATION",
        actual_route=str(hsp90["conclusion_packet"]["terminal_route"]),
        deterministic_authorization="AUTHORIZED_EXACT_REGISTERED_OPERATOR",
        action_count=1,
        evidence_result_class="OPERATOR_EVIDENCE_RESULT",
        affected_rule_instance=hsp90_rule_id,
        before_rule_result=_rule_summary(hsp90["pre_operator_rule_result"]),
        after_rule_result=_rule_summary(hsp90["post_operator_rule_result"]),
        terminal_reducer_state=str(computation_stage2["terminal_disposition"]),
        claim_ceiling="EXACT_CONTROL_ONLY: "
        + str(computation_stage2["current_claim_ceiling"]),
        artifact_paths=computation_artifacts,
        authority_status="PENDING_HUMAN_VALIDATION_EXACT_CONTROL_ONLY",
    )
    _write_scenario_receipt(
        scenario_dir=computation_dir, output_dir=output_dir, row=computation_row
    )
    rows.append(computation_row)

    # D: the exact lookup is absent from the allowlist.  The workflow records the
    # stop and performs no undeclared retrieval, computation, or inference.
    stop_dir = _scenario_dir(output_dir, STOP_SCENARIO_ID)
    stop_graph = _remove_random_composition(complete_graph)
    stop_before_results = evaluate_xeisd_case(case_graph=stop_graph, **rules_bundle)
    stop_request = _missing_lookup_request()
    stop_lookup = execute_exact_source_lookup(
        allowlist=allowlist,
        request=stop_request,
        workspace_root=repo_root,
    )
    if (
        stop_lookup.get("status") != "NOT_FOUND"
        or stop_lookup.get("route") != "HUMAN_OR_NEW_DATA"
    ):
        raise ValueError("EXPLICIT_STOP_LOOKUP_BEHAVIOR_CHANGED")
    stop_after_graph = apply_lookup_result(
        case_graph=stop_graph, lookup_result=stop_lookup
    )
    stop_after_results = evaluate_xeisd_case(
        case_graph=stop_after_graph, **rules_bundle
    )
    stop_before_target = _rule_by_id(
        stop_before_results, _RANDOM_COMPOSITION_RULE_INSTANCE_ID
    )
    stop_after_target = _rule_by_id(
        stop_after_results, _RANDOM_COMPOSITION_RULE_INSTANCE_ID
    )
    if (
        stop_before_target.get("status") != "UNRESOLVED"
        or stop_after_target.get("status") != "UNRESOLVED"
        or _status_transitions(stop_before_results, stop_after_results)
    ):
        raise ValueError("EXPLICIT_STOP_RULE_STATE_CHANGED")
    stop_route = materialize_xeisd_conclusion_packet(
        case_graph=stop_after_graph,
        rule_results=stop_after_results,
        lookup_results=[stop_lookup],
        scenario_id=STOP_SCENARIO_ID,
    )
    stop_route_path = stop_dir / "route_packet.json"
    stop_stage2_path = stop_dir / "stage2_conclusion_packet.json"
    stop_artifact_names = (
        "input_casegraph.json",
        "before_rule_results.json",
        "lookup_request.json",
        "lookup_result.json",
        "after_rule_results.json",
        "rule_transition.json",
        "route_packet.json",
        "stage2_conclusion_packet.json",
        "stop_receipt.json",
        "scenario_receipt.json",
    )
    stop_artifacts = [
        _relative_path(stop_dir / name, output_dir) for name in stop_artifact_names
    ]
    stop_stage2 = _stage2_packet(
        route_packet=stop_route,
        source_grounding=real_source_grounding,
        scenario_id=STOP_SCENARIO_ID,
        route_artifact_path=_relative_path(stop_route_path, output_dir),
    )
    if stop_route.get("terminal_route") != "HUMAN_OR_NEW_DATA":
        raise ValueError("EXPLICIT_STOP_TERMINAL_ROUTE_CHANGED")
    _write_json(stop_dir / "input_casegraph.json", stop_graph)
    _write_json(stop_dir / "before_rule_results.json", stop_before_results)
    _write_json(stop_dir / "lookup_request.json", stop_request)
    _write_json(stop_dir / "lookup_result.json", stop_lookup)
    _write_json(stop_dir / "after_rule_results.json", stop_after_results)
    _write_json(
        stop_dir / "rule_transition.json",
        {
            "affected_rule_instance_id": _RANDOM_COMPOSITION_RULE_INSTANCE_ID,
            "before_rule_result": stop_before_target,
            "after_rule_result": stop_after_target,
            "all_changed_rule_statuses": [],
        },
    )
    _write_json(stop_route_path, stop_route)
    _write_json(stop_stage2_path, stop_stage2)
    _write_json(
        stop_dir / "stop_receipt.json",
        {
            "schema_version": "explicit-stop-receipt/v1",
            "scenario_id": STOP_SCENARIO_ID,
            "lookup_status": stop_lookup["status"],
            "route": stop_lookup["route"],
            "authorized_lookup_actions": 1,
            "unauthorized_analysis_actions": 0,
            "unregistered_tool_calls": 0,
            "network_accessed": False,
            "result": "STOPPED_HUMAN_OR_NEW_DATA",
        },
    )
    stop_row = _base_row(
        scenario_id=STOP_SCENARIO_ID,
        case_id=X_EISD_CASE_ID,
        input_role="DATA_UNAVAILABLE_AFTER_EXACT_LOOKUP",
        expected_route_family="EXPLICIT_STOP",
        actual_route=str(stop_route["terminal_route"]),
        deterministic_authorization="AUTHORIZED_EXACT_LOOKUP_THEN_STOP",
        action_count=1,
        evidence_result_class="SOURCE_LOOKUP_RESULT",
        affected_rule_instance=_RANDOM_COMPOSITION_RULE_INSTANCE_ID,
        before_rule_result=_rule_summary(stop_before_target),
        after_rule_result=_rule_summary(stop_after_target),
        terminal_reducer_state=str(stop_stage2["terminal_disposition"]),
        claim_ceiling=str(stop_stage2["current_claim_ceiling"]),
        artifact_paths=stop_artifacts,
        authority_status="HUMAN_OR_NEW_DATA_REQUIRED",
    )
    _write_scenario_receipt(
        scenario_dir=stop_dir, output_dir=output_dir, row=stop_row
    )
    rows.append(stop_row)

    # T1: exercise only the reducer's SUPPORT contract with a synthetic source-
    # review override.  The override is isolated and never replaces repository
    # source-review state.
    support_dir = _scenario_dir(output_dir, SYNTHETIC_SUPPORT_SCENARIO_ID)
    synthetic_grounding = {
        family_id: "VERIFIED" for family_id in real_source_grounding
    }
    support_stage2_path = support_dir / "stage2_conclusion_packet.json"
    support_artifact_names = (
        "source_grounding_override.json",
        "stage2_conclusion_packet.json",
        "authority_receipt.json",
        "scenario_receipt.json",
    )
    support_artifacts = [
        _relative_path(support_dir / name, output_dir)
        for name in support_artifact_names
    ]
    support_stage2 = _stage2_packet(
        route_packet=direct_route,
        source_grounding=synthetic_grounding,
        scenario_id=SYNTHETIC_SUPPORT_SCENARIO_ID,
        route_artifact_path=_relative_path(direct_route_path, output_dir),
    )
    _write_json(
        support_dir / "source_grounding_override.json",
        {
            "authority_status": "SYNTHETIC_OVERRIDE_NOT_REPOSITORY_STATUS",
            "source_grounding": synthetic_grounding,
        },
    )
    _write_json(support_stage2_path, support_stage2)
    _write_json(
        support_dir / "authority_receipt.json",
        {
            "schema_version": "synthetic-authority-receipt/v1",
            "scenario_id": SYNTHETIC_SUPPORT_SCENARIO_ID,
            "authority_status": "SYNTHETIC_CONTRACT_BEHAVIOR_ONLY",
            "source_grounding_authority": "SYNTHETIC_OVERRIDE_NOT_REPOSITORY_STATUS",
            "real_scientific_support_packets": 0,
            "scientific_claim_upgrade": False,
            "boundary": "This row proves only the deterministic reducer's SUPPORT branch. It is not source-science approval or support for a real public case.",
        },
    )
    support_row = _base_row(
        scenario_id=SYNTHETIC_SUPPORT_SCENARIO_ID,
        case_id=X_EISD_CASE_ID,
        input_role="SYNTHETIC_VERIFIED_SOURCE_GATE",
        expected_route_family="TERMINAL_REDUCER_CONTRACT",
        actual_route="DIRECT_EVALUATION_THEN_SUPPORT_WITHIN_CEILING",
        deterministic_authorization="NOT_APPLICABLE_SYNTHETIC_REDUCER_INPUT",
        action_count=0,
        evidence_result_class="NONE_DIRECT_EVALUATION",
        affected_rule_instance=None,
        before_rule_result=None,
        after_rule_result={
            "scope": "FROZEN_XEISD_REQUIRED_RULE_INVENTORY",
            "status_counts": _status_counts(direct_route["rule_results"]),
        },
        terminal_reducer_state=str(support_stage2["terminal_disposition"]),
        claim_ceiling="SYNTHETIC_CONTRACT_BEHAVIOR_ONLY: "
        + str(support_stage2["current_claim_ceiling"]),
        artifact_paths=support_artifacts,
        authority_status="SYNTHETIC_CONTRACT_BEHAVIOR_ONLY",
    )
    _write_scenario_receipt(
        scenario_dir=support_dir, output_dir=output_dir, row=support_row
    )
    rows.append(support_row)

    # T2: an explicit declared relation mismatch exercises the same reducer's
    # CANNOT_SUPPORT branch without invalidating either source-local observation.
    cannot_dir = _scenario_dir(output_dir, CANNOT_SUPPORT_SCENARIO_ID)
    cannot_graph = copy.deepcopy(complete_graph)
    comparisons = cannot_graph.get("comparisons")
    if not isinstance(comparisons, list) or len(comparisons) != 1:
        raise ValueError("X_EISD_EXACT_COMPARISON_MISSING")
    comparisons[0]["condition_relation"] = "MISMATCH"
    cannot_results = evaluate_xeisd_case(case_graph=cannot_graph, **rules_bundle)
    cannot_route = materialize_xeisd_conclusion_packet(
        case_graph=cannot_graph,
        rule_results=cannot_results,
        lookup_results=[],
        scenario_id=CANNOT_SUPPORT_SCENARIO_ID,
    )
    cannot_route_path = cannot_dir / "route_packet.json"
    cannot_stage2_path = cannot_dir / "stage2_conclusion_packet.json"
    cannot_artifact_names = (
        "input_casegraph.json",
        "rule_results.json",
        "route_packet.json",
        "stage2_conclusion_packet.json",
        "scenario_receipt.json",
    )
    cannot_artifacts = [
        _relative_path(cannot_dir / name, output_dir)
        for name in cannot_artifact_names
    ]
    cannot_stage2 = _stage2_packet(
        route_packet=cannot_route,
        source_grounding=real_source_grounding,
        scenario_id=CANNOT_SUPPORT_SCENARIO_ID,
        route_artifact_path=_relative_path(cannot_route_path, output_dir),
    )
    if cannot_route.get("route_disposition") != "RELATION_BLOCKED":
        raise ValueError("CANNOT_SUPPORT_RELATION_ROUTE_CHANGED")
    failed_dependency = cannot_stage2.get("first_failed_dependency")
    if not isinstance(failed_dependency, Mapping):
        raise ValueError("CANNOT_SUPPORT_FAILED_DEPENDENCY_MISSING")
    failed_rule = _rule_by_id(
        cannot_results, str(failed_dependency.get("rule_instance_id"))
    )
    _write_json(cannot_dir / "input_casegraph.json", cannot_graph)
    _write_json(cannot_dir / "rule_results.json", cannot_results)
    _write_json(cannot_route_path, cannot_route)
    _write_json(cannot_stage2_path, cannot_stage2)
    cannot_row = _base_row(
        scenario_id=CANNOT_SUPPORT_SCENARIO_ID,
        case_id=X_EISD_CASE_ID,
        input_role="DECLARED_EXACT_RELATION_MISMATCH",
        expected_route_family="TERMINAL_REDUCER_CONTRACT",
        actual_route="HUMAN_OR_NEW_DATA_THEN_CANNOT_SUPPORT_REQUESTED_CLAIM",
        deterministic_authorization="NOT_REQUIRED_DIRECT_EVALUATION",
        action_count=0,
        evidence_result_class="NONE_DIRECT_EVALUATION",
        affected_rule_instance=str(failed_rule["rule_instance_id"]),
        before_rule_result=None,
        after_rule_result=_rule_summary(failed_rule),
        terminal_reducer_state=str(cannot_stage2["terminal_disposition"]),
        claim_ceiling=str(cannot_stage2["current_claim_ceiling"]),
        artifact_paths=cannot_artifacts,
        authority_status="REAL_REPOSITORY_SOURCE_REVIEW_STATUS_RETAINED",
    )
    _write_scenario_receipt(
        scenario_dir=cannot_dir, output_dir=output_dir, row=cannot_row
    )
    rows.append(cannot_row)

    if tuple(row["scenario_id"] for row in rows) != _SCENARIO_ORDER:
        raise ValueError("COMMON_FLOW_SCENARIO_ORDER_CHANGED")
    terminal_dispositions = {
        row["scenario_id"]: row["terminal_reducer_state"] for row in rows
    }
    if terminal_dispositions != _EXPECTED_TERMINAL_DISPOSITIONS:
        raise ValueError("COMMON_FLOW_TERMINAL_MATRIX_CHANGED")

    matrix = {
        "schema_version": SCENARIO_MATRIX_SCHEMA_VERSION,
        "run_id": SCENARIO_SUITE_RUN_ID,
        "development_status": "DEVELOPMENT_DIAGNOSTIC_ONLY",
        "agent_value_status": "NOT_AGENT_VALUE_ESTABLISHED",
        "scenarios": rows,
    }
    manifest = {
        "schema_version": SCENARIO_SUITE_SCHEMA_VERSION,
        "run_id": SCENARIO_SUITE_RUN_ID,
        "run_kind": "DETERMINISTIC_COMMON_FLOW_CONTRACT_SUITE",
        "scenario_matrix_artifact": "common_flow_matrix.json",
        "scenario_ids": list(_SCENARIO_ORDER),
        "terminal_dispositions": terminal_dispositions,
        "input_artifacts": {
            "xeisd_complete_casegraph": "evidence/real_case_vertical_slice_v1/outputs/xeisd_a1_complete_casegraph.json",
            "xeisd_lookup_allowlist": "evidence/real_case_vertical_slice_v1/xeisd_source_lookup_allowlist_v1.json",
            "hsp90_exact_control_inputs": "evidence/real_case_vertical_slice_v1",
            "registered_operator_registry": "config/registered_operators.json",
            "source_grounding_overlay": "registries/rules_v1/family_overlay_v1.json",
        },
        "network_accessed": False,
        "model_calls": 0,
        "credential_reads": 0,
        "external_spend": 0.0,
        "real_scientific_support_packets": 0,
        "synthetic_contract_support_packets": 1,
        "scientific_disposition": "NOT_EVALUATED",
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "hsp90_broad_closure_status": "NOT_ESTABLISHED_EXACT_CONTROL_ONLY",
        "boundary": "Four deterministic route families and three reducer behaviors over existing exact fixtures. The SUPPORT row is synthetic contract behavior only; no real scientific authority is upgraded.",
    }
    _write_json(output_dir / "common_flow_matrix.json", matrix)
    _write_json(output_dir / "scenario_suite_manifest.json", manifest)
    return {"manifest": manifest, "matrix": matrix, "output_dir": str(output_dir)}
