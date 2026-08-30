#!/usr/bin/env python3
"""Consolidate the bounded 2026-08-30 OpenRouter campaign receipts.

The live calls were intentionally split across an initial frozen matrix, one
prompt repair, one diagnostic fallback, and a final Planner-only continuation
that reused an already-paid Profiler response.  This builder deduplicates that
reused response ID, replays the current deterministic Profiler core admission,
and emits one machine-readable campaign receipt without making a network call.
The frozen config supplies campaign identity and authorization ceilings; observed
receipts supply completed-call and cost totals.
"""

from __future__ import annotations

import json
from decimal import Decimal
from pathlib import Path
from typing import Any

from dynamics_atlas_harness import case_runner_v1 as runner
from dynamics_atlas_harness.profile_proposal_envelope_v1 import (
    ProfileProposalEnvelopeV1Error,
    extract_core_proposal,
    validate_profile_proposal_envelope,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
DEVELOPMENT_ROOT = (
    REPO_ROOT / "evidence" / "live_agent_common_flows_v1" / "development_runs"
)
INPUT_ROOTS = (
    DEVELOPMENT_ROOT / "authorized_campaign_live_20260830",
    DEVELOPMENT_ROOT / "authorized_campaign_repair1_20260830",
    DEVELOPMENT_ROOT / "authorized_campaign_terra_fallback_20260830",
    DEVELOPMENT_ROOT / "authorized_planner_from_frozen_hsp90_luna_20260830",
    DEVELOPMENT_ROOT
    / "authorized_planner_from_frozen_hsp90_minimax_repair1_20260830",
)
OUTPUT_ROOT = DEVELOPMENT_ROOT / "authorized_campaign_final_20260830"
CONFIG_PATH = (
    REPO_ROOT
    / "agent_experiments"
    / "live_agent_common_flows_v1"
    / "config"
    / "live_agent_common_flows_v1.json"
)


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def _trial_root(receipt_path: Path) -> Path:
    # receipt -> role -> live_calls/failed_live_calls -> trial root
    return receipt_path.parents[2]


def _response_content(raw_path: Path) -> dict[str, Any] | None:
    try:
        response = _read_json(raw_path)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return None
    choices = response.get("choices")
    if not isinstance(choices, list) or len(choices) != 1:
        return None
    choice = choices[0]
    message = choice.get("message") if isinstance(choice, dict) else None
    content = message.get("content") if isinstance(message, dict) else None
    if not isinstance(content, str):
        return None
    try:
        parsed = json.loads(content)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def _profiler_replay(
    *, case_id: str, proposal: dict[str, Any] | None
) -> tuple[str, str, str | None]:
    if proposal is None:
        return "UNAVAILABLE_NO_JSON_PROPOSAL", "NOT_EVALUATED", None
    packet_path = runner._CASE_PACKET_REGISTRY[case_id]["packet"]
    try:
        core = extract_core_proposal(proposal)
        runner.capsule.validate_agent_proposal(packet_path, core)
    except Exception as error:
        return "REJECTED", "NOT_EVALUATED", str(error).split(":", 1)[0]
    try:
        validate_profile_proposal_envelope(packet_path, proposal)
    except ProfileProposalEnvelopeV1Error as error:
        return "PASS", "REJECTED_DIAGNOSTIC_ONLY", str(error).split(":", 1)[0]
    return "PASS", "PASS", None


def _attempt_row(path: Path, receipt: dict[str, Any]) -> dict[str, Any]:
    trial_root = _trial_root(path)
    failure_path = trial_root / "live_agent_case_failure.json"
    manifest_path = trial_root / "case_run_manifest_v1.json"
    failure = _read_json(failure_path) if failure_path.is_file() else None
    manifest = _read_json(manifest_path) if manifest_path.is_file() else None
    proposal = _response_content(path.with_name("raw_response.txt"))
    role = receipt.get("role")
    core_status = "NOT_APPLICABLE"
    annotation_status = "NOT_APPLICABLE"
    core_error = None
    if role == "PROFILER":
        core_status, annotation_status, core_error = _profiler_replay(
            case_id=str(receipt.get("case_id")), proposal=proposal
        )
    completed = receipt.get("transport_status") == "COMPLETED_RESPONSE"
    return {
        "attempt_artifact": _relative(path),
        "case_id": receipt.get("case_id"),
        "role": role,
        "requested_model": receipt.get("requested_model"),
        "requested_provider_endpoint_tag": receipt.get(
            "requested_provider_endpoint_tag"
        ),
        "actual_provider": receipt.get("actual_provider"),
        "service_tier": receipt.get("service_tier"),
        "attempt_number_for_exact_cell": receipt.get("attempt_number"),
        "http_status": receipt.get("http_status"),
        "completed_response": completed,
        "response_id": receipt.get("response_id"),
        "finish_reason": receipt.get("finish_reason"),
        "transport_schema_status": receipt.get("status"),
        "reason_codes": receipt.get("reason_codes", []),
        "reported_cost_usd": receipt.get("reported_cost_usd"),
        "usage": receipt.get("usage"),
        "latency_ms": receipt.get("latency_ms"),
        "profiler_core_admission": core_status,
        "profiler_annotation_diagnostic": annotation_status,
        "profiler_core_or_annotation_error": core_error,
        "case_run_status": (
            "SUCCEEDED"
            if manifest is not None
            else failure.get("status")
            if failure is not None
            else "NO_CASE_RUN_ARTIFACT"
        ),
        "case_run_error": failure.get("error_code") if failure is not None else None,
        "scientific_disposition": (
            manifest.get("scientific_disposition")
            if manifest is not None
            else "NOT_EVALUATED"
        ),
    }


def build() -> dict[str, Any]:
    config = _read_json(CONFIG_PATH)
    campaign_id = config["campaign_id"]
    maximum_calls = config["max_completed_calls"]
    maximum_cost = Decimal(str(config["budget_usd"]))
    receipt_paths = sorted(
        path
        for root in INPUT_ROOTS
        for path in root.rglob("model_call_receipt.json")
    )
    attempts: list[dict[str, Any]] = []
    reused_artifacts: list[dict[str, Any]] = []
    response_owner: dict[str, str] = {}
    completed_cost = Decimal("0")
    completed_calls = 0
    for path in receipt_paths:
        receipt = _read_json(path)
        response_id = receipt.get("response_id")
        if isinstance(response_id, str) and response_id in response_owner:
            reused_artifacts.append(
                {
                    "response_id": response_id,
                    "canonical_receipt": response_owner[response_id],
                    "reused_receipt": _relative(path),
                    "network_call_repeated": False,
                }
            )
            continue
        row = _attempt_row(path, receipt)
        attempts.append(row)
        if isinstance(response_id, str):
            response_owner[response_id] = _relative(path)
        if row["completed_response"]:
            completed_calls += 1
            cost = row["reported_cost_usd"]
            if cost is None:
                raise ValueError("COMPLETED_CALL_COST_UNAVAILABLE")
            completed_cost += Decimal(str(cost))

    if completed_calls > maximum_calls:
        raise ValueError("COMPLETED_CALL_COUNT_EXCEEDS_CONFIGURED_MAXIMUM")
    if completed_cost > maximum_cost:
        raise ValueError("COMPLETED_CALL_COST_EXCEEDS_CONFIGURED_BUDGET")
    successful_root = (
        DEVELOPMENT_ROOT
        / "authorized_planner_from_frozen_hsp90_minimax_repair1_20260830"
        / "trial-1"
    )
    successful_manifest = _read_json(successful_root / "case_run_manifest_v1.json")
    before = successful_manifest["rule_reevaluation"]["before_rule_results"]
    after = successful_manifest["rule_reevaluation"]["after_rule_results"]
    matrix = {
        "schema_version": "live-agent-development-attempt-matrix/v1",
        "campaign_id": campaign_id,
        "attempted_http_requests": len(attempts),
        "completed_api_calls": completed_calls,
        "actual_cost_usd": str(completed_cost),
        "attempts": attempts,
        "reused_frozen_artifacts": reused_artifacts,
        "development_evidence_status": "DEVELOPMENT_DIAGNOSTIC_ONLY",
        "agent_value_status": "NOT_AGENT_VALUE_ESTABLISHED",
    }
    manifest = {
        "schema_version": "live-agent-common-flows-campaign-completion/v1",
        "campaign_id": campaign_id,
        "campaign_state": "CLOSED_FROZEN",
        "status": "LIVE_MODEL_PROPOSAL_TRANSPORT_V1_COMPLETE_WITH_FAIL_CLOSED_REJECTIONS",
        "base_commit": "e8d4f7781590c4c0424c83dffb62f62fbe526fcf",
        "head_commit_source": "GITHUB_PR_METADATA_AFTER_FINAL_COMMIT",
        "credential_handling": {
            "authorized_local_secret_store_injected_into_inherited_environment": True,
            "credential_source_recorded_by_calls": "INHERITED_ENVIRONMENT",
            "key_value_printed": False,
            "key_value_persisted": False,
            "unrelated_locations_scanned": False,
        },
        "http_attempts": len(attempts),
        "completed_api_calls": completed_calls,
        "maximum_authorized_completed_calls": maximum_calls,
        "actual_cost_usd": str(completed_cost),
        "maximum_authorized_cost_usd": str(config["budget_usd"]),
        "transport_settings": {
            "api": "OPENROUTER_CHAT_COMPLETIONS",
            "structured_output": "STRICT_JSON_SCHEMA",
            "hosted_tools": False,
            "model_tool_calls": False,
            "automatic_retries": 0,
            "max_output_tokens": config["max_output_tokens"],
            "exact_provider_routing": True,
            "server_side_max_price": True,
        },
        "catalog_snapshots": [
            {
                "path": (
                    "agent_experiments/live_agent_common_flows_v1/config/"
                    "openrouter_endpoint_selection_20260830.json"
                ),
                "canonical_sha256": (
                    "4032c962a185ecae6f67e83f80dd12ac7974738d9cab89f53d67ef3498110c36"
                ),
                "scope": "LUNA_DEEPSEEK_MINIMAX",
            },
            {
                "path": (
                    "agent_experiments/live_agent_common_flows_v1/config/"
                    "openrouter_endpoint_selection_with_terra_20260830.json"
                ),
                "canonical_sha256": (
                    "707ec451cc90e34f2dd3bdc3e8bf85d8385b038adb9430457c8a99485e0aba9a"
                ),
                "scope": "HISTORICAL_TERRA_CALL_RECEIPT_BINDING",
            },
        ],
        "successful_live_proposal_transport_runs": 1,
        "successful_live_path": {
            "artifact_root": _relative(successful_root),
            "case_id": successful_manifest["case_id"],
            "profiler_model": "minimax/minimax-m2.5",
            "profiler_core_admission": "CORE_ADMISSION_PASS",
            "full_annotation_envelope": "FULL_ANNOTATION_ENVELOPE_FAIL",
            "profiler_field_annotation_error": "UNKNOWN_STATUS_CORE_VALUE_MISMATCH",
            "profiler_transport": "REUSED_FROZEN_ALREADY_PAID_RESPONSE",
            "planner_model": "minimax/minimax-m2.5",
            "planner_decision_surface": "ONE_LEGAL_CARD_VERSUS_ABSTAIN",
            "planner_utility_boundary": "NOT_NONTRIVIAL_ROUTE_SELECTION",
            "planner_transport": "LIVE_OPENROUTER_CALL",
            "deterministic_authorization": successful_manifest["authorization"][
                "status"
            ],
            "action_count": successful_manifest["authorization"][
                "executed_action_count"
            ],
            "evidence_class": "DESCRIPTIVE_EVIDENCE_NO_ACTIVE_RULE_EFFECT",
            "same_rule_transition_count": len(
                successful_manifest["rule_reevaluation"][
                    "reevaluated_rule_instance_ids"
                ]
            ),
            "same_rule_transition_status": "SAME_RULE_TRANSITION_COUNT_ZERO",
            "before_after_rule_results_identical": before == after,
            "conclusion_packet_status": "CONCLUSION_PACKET_NOT_CALCULATED",
            "terminal_scientific_state": successful_manifest[
                "terminal_scientific_state"
            ],
            "scientific_disposition": successful_manifest[
                "scientific_disposition"
            ],
        },
        "campaign_adaptation": {
            "profiler_prompt_versions": [
                "LIVE_AGENT_COMMON_FLOWS_PROFILER_V1",
                "LIVE_AGENT_COMMON_FLOWS_PROFILER_V2_BOUNDED_REPAIR_1",
            ],
            "prompt_repairs_used": 1,
            "luna_planner_http_400_attempts": 2,
            "luna_planner_completed_or_charged_calls": 0,
            "planner_schema_repair": (
                "REMOVED_TOP_LEVEL_CONDITIONAL_BRANCHES; DETERMINISTIC_VALIDATOR_"
                "RETAINS_SELECTION_SEMANTICS"
            ),
            "stop_reason": "FIRST_FULL_LIVE_PATH_SUCCEEDED; NO_FURTHER_SPEND_NEEDED",
        },
        "common_flow_matrix": (
            "evidence/common_flow_scenarios_v1/development_runs/"
            "common_flow_scenarios_v1/common_flow_matrix.json"
        ),
        "common_flow_coverage": {
            "agent_mode": "NO_AGENT_DETERMINISTIC_SCENARIO",
            "coverage_boundary": "NOT_LIVE_AGENT_COMMON_FLOW_COVERAGE",
            "scenario_count": 6,
            "route_families": [
                "DIRECT_EVALUATION",
                "NARROW_LOOKUP",
                "REGISTERED_COMPUTATION",
                "EXPLICIT_STOP",
            ],
            "terminal_states": [
                "SUPPORT_WITHIN_CEILING",
                "CANNOT_SUPPORT_REQUESTED_CLAIM",
                "ABSTAIN_OR_HUMAN_REVIEW",
            ],
            "support_scope": "SYNTHETIC_CONTRACT_BEHAVIOR_ONLY",
            "registered_computation_scope": "HSP90_EXACT_CONTROL_ONLY",
        },
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "broad_hsp90_closure_status": "NOT_ESTABLISHED",
        "adk_dynamics_status": "NOT_ESTABLISHED_STATIC_EXPOSURE_ONLY",
        "held_out_status": "NOT_ACCESSED",
        "agent_value_status": "NOT_AGENT_VALUE_ESTABLISHED",
        "claim_ceiling": "DEVELOPMENT_DIAGNOSTIC_ONLY",
    }
    _write_json(OUTPUT_ROOT / "live_agent_development_matrix.json", matrix)
    _write_json(OUTPUT_ROOT / "live_agent_campaign_manifest.json", manifest)
    return manifest


if __name__ == "__main__":
    print(json.dumps(build(), indent=2, sort_keys=True))
