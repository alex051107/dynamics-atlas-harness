"""Case-bound Stage-2 aggregation for the two exposed no-Agent artifacts.

This is deliberately a reducer, not a scheduler or a replacement for the existing
route packets.  It consumes a validated PR #6 route packet plus the explicit
family-level source-grounding statuses, then produces a separate case-level packet.
No lookup, Operator, Agent, or Rule evaluation occurs here.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping, Sequence

from .real_case_vertical_slice_v1 import (
    HSP90_CASE_ID,
    X_EISD_CASE_ID,
    X_EISD_EDGE_ID,
    X_EISD_FROZEN_REQUESTED_CLAIM,
    X_EISD_FROZEN_SELECTED_RULE_INSTANCE_IDS,
    validate_hsp90_conclusion_packet,
    validate_xeisd_conclusion_packet,
)


STAGE2_SCHEMA_VERSION = "stage2-conclusion-packet/v1-alpha"
_TERMINAL_DISPOSITIONS = frozenset(
    {
        "SUPPORT_WITHIN_CEILING",
        "CANNOT_SUPPORT_REQUESTED_CLAIM",
        "ABSTAIN_OR_HUMAN_REVIEW",
    }
)
_SOURCE_GROUNDING_DECISIONS = frozenset(
    {"VERIFIED", "PENDING_DOMAIN_REVIEW", "REJECTED"}
)
_REQUIRED_RULE_STATUSES = frozenset({"PASS", "FAIL", "UNRESOLVED"})
_SOURCE_SCIENCE_GATE_ID = "HDG-RULES-V1-SOURCE-SCIENCE-REVIEW"


class MinimalStage2ConclusionError(ValueError):
    """Raised when a frozen exposed-route packet cannot be reduced safely."""


def _mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise MinimalStage2ConclusionError(f"{label} must be a mapping")
    return value


def _result_list(value: Any, label: str) -> list[dict[str, Any]]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
        raise MinimalStage2ConclusionError(f"{label} must be a sequence")
    copied: list[dict[str, Any]] = []
    for index, item in enumerate(value):
        item = _mapping(item, f"{label}[{index}]")
        copied.append(deepcopy(dict(item)))
    return copied


def source_grounding_by_family(family_overlay: Mapping[str, Any]) -> dict[str, str]:
    """Read the existing human-owned source-grounding decisions without upgrading them."""

    family_overlay = _mapping(family_overlay, "family_overlay")
    families = family_overlay.get("families")
    if not isinstance(families, Sequence) or isinstance(families, (str, bytes)):
        raise MinimalStage2ConclusionError("family_overlay.families must be a sequence")
    decisions: dict[str, str] = {}
    for index, family in enumerate(families):
        family = _mapping(family, f"family_overlay.families[{index}]")
        family_id = family.get("family_id")
        decision = family.get("source_grounding_decision")
        if not isinstance(family_id, str) or not family_id:
            raise MinimalStage2ConclusionError("family overlay has an invalid family_id")
        if decision not in _SOURCE_GROUNDING_DECISIONS:
            raise MinimalStage2ConclusionError(
                f"family {family_id} has an invalid source-grounding decision: {decision!r}"
            )
        if family_id in decisions:
            raise MinimalStage2ConclusionError(f"family overlay repeats {family_id}")
        decisions[family_id] = str(decision)
    return decisions


def _validate_route_packet(route_packet: Mapping[str, Any]) -> None:
    case_id = route_packet.get("case_id")
    if case_id == X_EISD_CASE_ID:
        validate_xeisd_conclusion_packet(route_packet)
    elif case_id == HSP90_CASE_ID:
        validate_hsp90_conclusion_packet(route_packet)
    else:
        raise MinimalStage2ConclusionError(f"unexpected exposed case_id: {case_id!r}")


def _required_family_ids(rule_results: Sequence[Mapping[str, Any]]) -> list[str]:
    family_ids: list[str] = []
    for result in rule_results:
        family_id = result.get("family_id")
        if not isinstance(family_id, str) or not family_id:
            raise MinimalStage2ConclusionError("required RuleResult has no family_id")
        if family_id not in family_ids:
            family_ids.append(family_id)
    return family_ids


def _source_review_records(
    family_ids: Sequence[str], source_grounding: Mapping[str, str]
) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for family_id in family_ids:
        decision = source_grounding.get(family_id)
        if decision not in _SOURCE_GROUNDING_DECISIONS:
            raise MinimalStage2ConclusionError(
                f"missing or invalid source-grounding decision for {family_id}"
            )
        records.append(
            {
                "family_id": family_id,
                "human_decision_gate_id": _SOURCE_SCIENCE_GATE_ID,
                "source_grounding_decision": str(decision),
            }
        )
    return records


def _aggregate_source_review_status(records: Sequence[Mapping[str, str]]) -> str:
    decisions = [record["source_grounding_decision"] for record in records]
    if all(decision == "VERIFIED" for decision in decisions):
        return "VERIFIED"
    if len(set(decisions)) == 1:
        return decisions[0]
    return "MIXED"


def _rule_dependency(result: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "dependency_kind": "RULE_RESULT",
        "rule_instance_id": result.get("rule_instance_id"),
        "status": result.get("status"),
        "reason_codes": list(result.get("reason_codes", [])),
        "missing_paths": list(result.get("missing_paths", [])),
    }


def _source_review_dependency(record: Mapping[str, str]) -> dict[str, str]:
    return {
        "dependency_kind": "SOURCE_SCIENCE_REVIEW_GATE",
        "human_decision_gate_id": _SOURCE_SCIENCE_GATE_ID,
        "family_id": record["family_id"],
        "status": record["source_grounding_decision"],
        "reason_code": "SOURCE_SCIENCE_REVIEW_NOT_VERIFIED",
    }


def _pending_evidence_dependencies(
    evidence_results: Sequence[Mapping[str, Any]],
) -> list[dict[str, str]]:
    """Return only explicit human-validation gaps already present in route evidence."""

    dependencies: list[dict[str, str]] = []
    for evidence in evidence_results:
        result = evidence.get("result")
        if not isinstance(result, Mapping):
            continue
        if result.get("scientific_evaluation_status") != "PENDING_HUMAN_VALIDATION":
            continue
        dependencies.append(
            {
                "dependency_kind": "EVIDENCE_RESULT",
                "evidence_kind": str(evidence.get("evidence_kind", "UNKNOWN")),
                "evidence_result_id": str(result.get("evidence_result_id", "UNKNOWN")),
                "affected_rule_instance_id": str(
                    result.get("affected_rule_instance_id", "UNKNOWN")
                ),
                "status": "PENDING_HUMAN_VALIDATION",
                "reason_code": "EVIDENCE_RESULT_PENDING_HUMAN_VALIDATION",
            }
        )
    return dependencies


def _validate_case_bound_final_packet_inputs(
    *,
    packet: Mapping[str, Any],
    required_rule_results: Sequence[Mapping[str, Any]],
    evidence_results: Sequence[Mapping[str, Any]],
) -> None:
    """Reject mutations that escape the two frozen exposed-case boundaries."""

    if packet["case_id"] == X_EISD_CASE_ID:
        if packet["requested_claim"] != X_EISD_FROZEN_REQUESTED_CLAIM:
            raise MinimalStage2ConclusionError(
                "X-EISD Stage2 ConclusionPacket must retain the exact frozen relation claim"
            )
        observed_rule_ids = tuple(
            result.get("rule_instance_id") for result in required_rule_results
        )
        if observed_rule_ids != X_EISD_FROZEN_SELECTED_RULE_INSTANCE_IDS:
            raise MinimalStage2ConclusionError(
                "X-EISD Stage2 ConclusionPacket must retain the frozen RuleResult inventory"
            )
        failed_rule_results = [
            result for result in required_rule_results if result["status"] == "FAIL"
        ]
        for result in failed_rule_results:
            target = _mapping(result.get("target"), "X-EISD failed RuleResult target")
            if target.get("kind") != "EDGE" or target.get("id") != X_EISD_EDGE_ID:
                raise MinimalStage2ConclusionError(
                    "X-EISD cannot-support disposition may only block the declared comparison edge"
                )
        return

    if len(evidence_results) != 1:
        raise MinimalStage2ConclusionError(
            "HSP90 Stage2 ConclusionPacket must retain one pending EvidenceResult"
        )
    evidence = _mapping(evidence_results[0], "HSP90 Stage2 evidence")
    if evidence.get("evidence_kind") != "OPERATOR_EVIDENCE_RESULT":
        raise MinimalStage2ConclusionError("HSP90 Stage2 ConclusionPacket has an invalid evidence kind")
    result = _mapping(evidence.get("result"), "HSP90 Stage2 EvidenceResult")
    if result.get("scientific_evaluation_status") != "PENDING_HUMAN_VALIDATION":
        raise MinimalStage2ConclusionError(
            "HSP90 Stage2 ConclusionPacket must retain PENDING_HUMAN_VALIDATION"
        )


def _terminal_state(
    *,
    required_rule_results: Sequence[Mapping[str, Any]],
    source_review_records: Sequence[Mapping[str, str]],
    evidence_results: Sequence[Mapping[str, Any]],
) -> tuple[str, dict[str, Any] | None]:
    """Apply the bounded Stage-2 precedence without interpreting new evidence."""

    failed_rule_results = [
        result for result in required_rule_results if result["status"] == "FAIL"
    ]
    unresolved_rule_results = [
        result for result in required_rule_results if result["status"] == "UNRESOLVED"
    ]
    if failed_rule_results:
        return "CANNOT_SUPPORT_REQUESTED_CLAIM", _rule_dependency(failed_rule_results[0])
    if unresolved_rule_results:
        return "ABSTAIN_OR_HUMAN_REVIEW", _rule_dependency(unresolved_rule_results[0])

    pending_evidence = _pending_evidence_dependencies(evidence_results)
    if pending_evidence:
        return "ABSTAIN_OR_HUMAN_REVIEW", pending_evidence[0]

    source_science_review_status = _aggregate_source_review_status(source_review_records)
    if source_science_review_status != "VERIFIED":
        pending = next(
            record
            for record in source_review_records
            if record["source_grounding_decision"] != "VERIFIED"
        )
        return "ABSTAIN_OR_HUMAN_REVIEW", _source_review_dependency(pending)
    return "SUPPORT_WITHIN_CEILING", None


def _evidence_and_receipts(
    route_packet: Mapping[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    evidence_results: list[dict[str, Any]] = []
    operator_receipts: list[dict[str, Any]] = []
    for lookup in _result_list(
        route_packet.get("evidence_lookup_results", []), "evidence_lookup_results"
    ):
        evidence_results.append(
            {"evidence_kind": "SOURCE_LOOKUP_RESULT", "result": lookup}
        )
    for operator_result in _result_list(
        route_packet.get("operator_results", []), "operator_results"
    ):
        evidence = operator_result.get("evidence_result")
        receipt = operator_result.get("operator_run_receipt")
        if evidence is not None:
            evidence_results.append(
                {
                    "evidence_kind": "OPERATOR_EVIDENCE_RESULT",
                    "result": deepcopy(dict(_mapping(evidence, "operator evidence_result"))),
                }
            )
        if receipt is not None:
            operator_receipts.append(deepcopy(dict(_mapping(receipt, "operator_run_receipt"))))
    return evidence_results, operator_receipts


def _next_action(terminal_disposition: str) -> str:
    if terminal_disposition == "SUPPORT_WITHIN_CEILING":
        return "Retain the bounded conclusion and send the provenance packet to human final review."
    if terminal_disposition == "CANNOT_SUPPORT_REQUESTED_CLAIM":
        return "Do not support the requested claim; inspect the first failed RuleResult without invalidating unrelated source-local observations."
    return "Do not emit the requested scientific claim; resolve the first dependency or obtain human source-science review."


def materialize_stage2_conclusion_packet(
    *,
    route_packet: Mapping[str, Any],
    source_grounding: Mapping[str, str],
    scenario_id: str,
    route_artifact_path: str,
) -> dict[str, Any]:
    """Reduce one validated exposed route packet into a terminal Stage-2 packet."""

    route_packet = _mapping(route_packet, "route_packet")
    _validate_route_packet(route_packet)
    if route_packet.get("scientific_disposition") != "NOT_EVALUATED":
        raise MinimalStage2ConclusionError(
            "Stage 2 may only consume a route packet that has not emitted a scientific disposition"
        )
    if not isinstance(scenario_id, str) or not scenario_id:
        raise MinimalStage2ConclusionError("scenario_id must be a nonempty string")
    if not isinstance(route_artifact_path, str) or not route_artifact_path:
        raise MinimalStage2ConclusionError("route_artifact_path must be a nonempty string")

    required_rule_results = _result_list(route_packet.get("rule_results"), "rule_results")
    advisory_rule_results = _result_list(
        route_packet.get("nonblocking_rule_results", []), "nonblocking_rule_results"
    )
    if not required_rule_results:
        raise MinimalStage2ConclusionError("Stage 2 requires at least one required RuleResult")
    for result in required_rule_results:
        status = result.get("status")
        if status not in _REQUIRED_RULE_STATUSES:
            raise MinimalStage2ConclusionError(
                f"required RuleResult has unsupported Stage-2 status: {status!r}"
            )

    failed_rule_results = [
        result for result in required_rule_results if result["status"] == "FAIL"
    ]
    unresolved_rule_results = [
        result for result in required_rule_results if result["status"] == "UNRESOLVED"
    ]
    source_review_records = _source_review_records(
        _required_family_ids(required_rule_results), source_grounding
    )
    source_science_review_status = _aggregate_source_review_status(source_review_records)

    evidence_results, operator_receipts = _evidence_and_receipts(route_packet)
    terminal_disposition, first_failed_dependency = _terminal_state(
        required_rule_results=required_rule_results,
        source_review_records=source_review_records,
        evidence_results=evidence_results,
    )
    human_review_items = list(route_packet.get("human_review_items", []))
    for record in source_review_records:
        if record["source_grounding_decision"] != "VERIFIED":
            human_review_items.append(
                "Source-science review remains "
                f"{record['source_grounding_decision']} for {record['family_id']}."
            )
    for evidence in evidence_results:
        result = evidence.get("result")
        if isinstance(result, Mapping) and result.get(
            "scientific_evaluation_status"
        ) == "PENDING_HUMAN_VALIDATION":
            human_review_items.append(
                "Operator EvidenceResult remains PENDING_HUMAN_VALIDATION; execution-contract PASS is not source-science approval."
            )

    packet = {
        "schema_version": STAGE2_SCHEMA_VERSION,
        "packet_kind": "MINIMAL_STAGE2_EXPOSED_CONCLUSION_V1",
        "development_status": "EXPOSED_DEVELOPMENT_ACTIVE",
        "scenario_id": scenario_id,
        "case_id": route_packet["case_id"],
        "requested_claim": route_packet["requested_claim"],
        "current_claim_ceiling": route_packet["claim_ceiling"],
        "terminal_disposition": terminal_disposition,
        "route_disposition": route_packet["route_disposition"],
        "required_rule_results": required_rule_results,
        "failed_rule_results": failed_rule_results,
        "unresolved_rule_results": unresolved_rule_results,
        "advisory_rule_results": advisory_rule_results,
        "evidence_results": evidence_results,
        "operator_receipts": operator_receipts,
        "source_science_review_status": source_science_review_status,
        "source_science_review_records": source_review_records,
        "first_failed_dependency": first_failed_dependency,
        "human_final_authority": True,
        "unsafe_claim_upgrade": False,
        "human_review_items": human_review_items,
        "next_action": _next_action(terminal_disposition),
        "route_artifact": {
            "path": route_artifact_path,
            "schema_version": route_packet["schema_version"],
            "packet_kind": route_packet["packet_kind"],
            "route_disposition": route_packet["route_disposition"],
            "scientific_disposition": route_packet["scientific_disposition"],
        },
        "provenance": {
            "aggregation_policy": "EXACT_EXPOSED_ARTIFACT_REDUCTION_ONLY",
            "source_science_gate": _SOURCE_SCIENCE_GATE_ID,
            "source_grounding_input": {
                record["family_id"]: record["source_grounding_decision"]
                for record in source_review_records
            },
            "route_packet_provenance": deepcopy(dict(route_packet.get("provenance", {}))),
        },
    }
    validate_stage2_conclusion_packet(packet, source_grounding=source_grounding)
    return packet


def validate_stage2_conclusion_packet(
    packet: Mapping[str, Any], *, source_grounding: Mapping[str, str]
) -> None:
    """Validate a Stage-2 packet against its authoritative source-review input."""

    packet = _mapping(packet, "Stage2 ConclusionPacket")
    required = {
        "schema_version",
        "packet_kind",
        "development_status",
        "scenario_id",
        "case_id",
        "requested_claim",
        "current_claim_ceiling",
        "terminal_disposition",
        "route_disposition",
        "required_rule_results",
        "failed_rule_results",
        "unresolved_rule_results",
        "advisory_rule_results",
        "evidence_results",
        "operator_receipts",
        "source_science_review_status",
        "source_science_review_records",
        "first_failed_dependency",
        "human_final_authority",
        "unsafe_claim_upgrade",
        "human_review_items",
        "next_action",
        "route_artifact",
        "provenance",
    }
    missing = sorted(required.difference(packet))
    if missing:
        raise MinimalStage2ConclusionError(
            "Stage2 ConclusionPacket missing: " + ", ".join(missing)
        )
    if packet["schema_version"] != STAGE2_SCHEMA_VERSION:
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket has an invalid schema version")
    if packet["packet_kind"] != "MINIMAL_STAGE2_EXPOSED_CONCLUSION_V1":
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket has an invalid packet kind")
    if packet["development_status"] != "EXPOSED_DEVELOPMENT_ACTIVE":
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket has an invalid development status")
    if packet["case_id"] not in {X_EISD_CASE_ID, HSP90_CASE_ID}:
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket has an unexpected case")
    if packet["terminal_disposition"] not in _TERMINAL_DISPOSITIONS:
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket has an unknown terminal disposition")
    if packet["human_final_authority"] is not True:
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket must retain human final authority")
    if packet["unsafe_claim_upgrade"] is not False:
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket must fail closed on claim upgrades")
    required_results = _result_list(packet["required_rule_results"], "required_rule_results")
    if not required_results:
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket has no required RuleResults")
    if any(result.get("status") not in _REQUIRED_RULE_STATUSES for result in required_results):
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket has an unsupported required RuleResult status")
    expected_failed = [result for result in required_results if result["status"] == "FAIL"]
    expected_unresolved = [
        result for result in required_results if result["status"] == "UNRESOLVED"
    ]
    if packet["failed_rule_results"] != expected_failed:
        raise MinimalStage2ConclusionError("failed RuleResults do not match required RuleResults")
    if packet["unresolved_rule_results"] != expected_unresolved:
        raise MinimalStage2ConclusionError("unresolved RuleResults do not match required RuleResults")
    evidence_results = _result_list(packet["evidence_results"], "evidence_results")
    _validate_case_bound_final_packet_inputs(
        packet=packet,
        required_rule_results=required_results,
        evidence_results=evidence_results,
    )
    source_records = packet["source_science_review_records"]
    if not isinstance(source_records, list) or not source_records:
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket has no source-science review records")
    required_family_ids = _required_family_ids(required_results)
    observed_family_ids: list[str] = []
    for record in source_records:
        record = _mapping(record, "source_science_review_record")
        family_id = record.get("family_id")
        if not isinstance(family_id, str) or not family_id:
            raise MinimalStage2ConclusionError("Stage2 ConclusionPacket source-review record has no family_id")
        observed_family_ids.append(family_id)
        if record.get("human_decision_gate_id") != _SOURCE_SCIENCE_GATE_ID:
            raise MinimalStage2ConclusionError("Stage2 ConclusionPacket has an invalid source-science gate")
        if record.get("source_grounding_decision") not in _SOURCE_GROUNDING_DECISIONS:
            raise MinimalStage2ConclusionError("Stage2 ConclusionPacket has an invalid source-grounding decision")
    if observed_family_ids != required_family_ids:
        raise MinimalStage2ConclusionError(
            "source-science review records must cover each required RuleResult family exactly once"
        )
    expected_source_status = _aggregate_source_review_status(source_records)
    if packet["source_science_review_status"] != expected_source_status:
        raise MinimalStage2ConclusionError("aggregate source-science review status is inconsistent")
    provenance = _mapping(packet["provenance"], "provenance")
    source_grounding_input = _mapping(
        provenance.get("source_grounding_input"), "provenance.source_grounding_input"
    )
    expected_grounding_input = {
        record["family_id"]: record["source_grounding_decision"] for record in source_records
    }
    if dict(source_grounding_input) != expected_grounding_input:
        raise MinimalStage2ConclusionError(
            "source-science review records do not match the recorded source-grounding input"
        )
    expected_authoritative_grounding = {
        family_id: source_grounding.get(family_id) for family_id in required_family_ids
    }
    if expected_authoritative_grounding != expected_grounding_input:
        raise MinimalStage2ConclusionError(
            "source-science review records do not match the authoritative source-grounding input"
        )
    expected_disposition, expected_first_dependency = _terminal_state(
        required_rule_results=required_results,
        source_review_records=source_records,
        evidence_results=evidence_results,
    )
    if packet["terminal_disposition"] != expected_disposition:
        raise MinimalStage2ConclusionError("terminal disposition does not match the required precedence")
    if packet["first_failed_dependency"] != expected_first_dependency:
        raise MinimalStage2ConclusionError(
            "first failed dependency does not match the required precedence"
        )
    route_artifact = _mapping(packet["route_artifact"], "route_artifact")
    if route_artifact.get("scientific_disposition") != "NOT_EVALUATED":
        raise MinimalStage2ConclusionError("Stage2 route artifact must preserve NOT_EVALUATED")
    if not isinstance(packet["human_review_items"], list) or not packet["human_review_items"]:
        raise MinimalStage2ConclusionError("Stage2 ConclusionPacket needs human-review items")
