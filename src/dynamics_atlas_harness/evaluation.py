"""Deterministic evidence-bundle routing under an explicit Evaluation Contract."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


ACCEPTED_RESULT_STATUSES = frozenset({"ACCEPTED_BY_CONTRACT"})
REJECTED_RESULT_STATUSES = frozenset({"REJECTED_BY_CONTRACT"})


def build_evaluation_contract(
    case_graph: Mapping[str, Any], selector_output: Mapping[str, Any]
) -> dict[str, Any]:
    case = case_graph.get("case", {})
    obligations = selector_output.get("obligations", [])
    return {
        "schema_version": "evaluation-contract/v0.1",
        "contract_id": f"{case.get('case_id', 'unknown')}--evaluation-v0.1",
        "case_id": case.get("case_id"),
        "scientific_claim": case.get("scientific_claim"),
        "requested_claim_level": case.get("requested_claim_level"),
        "required_obligations": [
            {
                "obligation_id": item.get("obligation_id"),
                "rule_id": item.get("rule_id"),
                "target": item.get("target"),
                "claim_scope": item.get("claim_scope"),
                "required_check": item.get("required_check"),
                "evidence_evaluation_required": bool(
                    item.get("evidence_evaluation_required")
                ),
            }
            for item in obligations
        ],
        "aggregation_policy": "ALL_REQUIRED_OBLIGATIONS_NEED_EXPLICIT_RESULT",
        "allowed_routes": [
            "DIRECT_BOUNDED_RESULT",
            "RUN_PLAN_REQUIRED",
            "ABSTAIN",
        ],
        "direct_result_semantics": [
            "SUFFICIENT_FOR_DECLARED_CONTRACT",
            "INSUFFICIENT_FOR_DECLARED_CONTRACT",
        ],
        "claim_ceiling": selector_output.get("authority_boundary", {}).get(
            "claim_ceiling", "REVIEW_OBLIGATIONS_ONLY"
        ),
        "human_final_authority": True,
        "forbidden_upgrades": [
            "SCIENTIFIC_CORRECTNESS_ESTABLISHED",
            "HELD_OUT_TRANSFER_ESTABLISHED",
            "AGENT_VALUE_ESTABLISHED",
            "PRODUCTION_READY",
        ],
    }


def evaluate_current_bundle(
    *,
    contract: Mapping[str, Any],
    selector_output: Mapping[str, Any],
    evidence_results: list[Mapping[str, Any]],
) -> dict[str, Any]:
    """Choose direct or gap route without interpreting scientific payloads."""

    results_by_obligation = {
        item.get("obligation_id"): item
        for item in evidence_results
        if isinstance(item.get("obligation_id"), str)
    }
    gaps: list[dict[str, Any]] = []
    for index, unresolved in enumerate(selector_output.get("unresolved_inputs", []), start=1):
        gaps.append(
            {
                "gap_id": f"selector-gap-{index:03d}",
                "gap_source": "SELECTOR_UNRESOLVED_INPUT",
                "gap_class": unresolved.get("gap_class", "UNRESOLVED"),
                "input_path": unresolved.get("input_path"),
                "target": unresolved.get("target"),
                "why_it_matters": unresolved.get("why_it_matters"),
            }
        )

    accepted = 0
    rejected = 0
    missing_obligation_ids: list[str] = []
    for requirement in contract.get("required_obligations", []):
        if not requirement.get("evidence_evaluation_required"):
            continue
        obligation_id = requirement.get("obligation_id")
        result = results_by_obligation.get(obligation_id)
        if result is None:
            if isinstance(obligation_id, str):
                missing_obligation_ids.append(obligation_id)
            continue
        status = result.get("contract_status")
        if status in ACCEPTED_RESULT_STATUSES:
            accepted += 1
        elif status in REJECTED_RESULT_STATUSES:
            rejected += 1
        else:
            gaps.append(
                {
                    "gap_id": f"evaluation-gap-{obligation_id}",
                    "gap_source": "EVALUATION_RESULT_INVALID",
                    "gap_class": "NOT_EVALUATED",
                    "input_path": None,
                    "target": requirement.get("target"),
                    "obligation_id": obligation_id,
                    "why_it_matters": "EvidenceResult lacks an allowed contract_status.",
                }
            )

    if missing_obligation_ids:
        gaps.append(
            {
                "gap_id": "evaluation-gap-batch-001",
                "gap_source": "EVALUATION_RESULT_MISSING",
                "gap_class": "NOT_EVALUATED",
                "input_path": None,
                "target": {"target_type": "CASE"},
                "obligation_ids": missing_obligation_ids,
                "why_it_matters": "Selected rule obligations still require explicit EvidenceResults under this contract.",
            }
        )

    if gaps:
        branch = "RUN_PLAN_REQUIRED"
        bundle_status = "INCOMPLETE"
    else:
        branch = "DIRECT_BOUNDED_RESULT"
        bundle_status = (
            "INSUFFICIENT_FOR_DECLARED_CONTRACT"
            if rejected
            else "SUFFICIENT_FOR_DECLARED_CONTRACT"
        )
    return {
        "schema_version": "deterministic-evaluation/v0.1",
        "contract_id": contract.get("contract_id"),
        "case_id": contract.get("case_id"),
        "branch": branch,
        "bundle_status": bundle_status,
        "accepted_result_count": accepted,
        "rejected_result_count": rejected,
        "gap_count": len(gaps),
        "gaps": gaps,
        "claim_ceiling": contract.get("claim_ceiling"),
        "review_status": "HUMAN_REVIEW_REQUIRED",
    }
