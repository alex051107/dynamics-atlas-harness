"""Deterministic authorization around proposal-only provider output."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
from typing import Any

from .contracts import (
    ProfileAdmission,
    validate_case_profile,
    validate_resolution_proposal,
    validate_review_obligation,
)
from .operators import execute_operator, operator_summary, resolve_operator
from .providers import ProposalProvider


def admit_profile(
    proposal: Mapping[str, Any],
    approved_method_profiles: set[str] | frozenset[str],
    method_profile_registry_id: str | None = None,
) -> ProfileAdmission:
    return validate_case_profile(
        proposal,
        approved_method_profiles,
        method_profile_registry_id=method_profile_registry_id,
    )


def _abstain_artifacts(
    obligation: Mapping[str, Any],
    proposal: Mapping[str, Any] | None,
    request_id: str,
    reason_codes: list[str],
    operator_id: str | None = None,
    operator_version: str | None = None,
    provider_id: str | None = None,
    operator_registry_id: str | None = None,
) -> dict[str, dict[str, Any]]:
    receipt = {
        "schema_version": "operator-run-receipt/v0.1",
        "request_id": request_id,
        "obligation_id": obligation.get("obligation_id"),
        "operator_id": operator_id,
        "operator_version": operator_version,
        "proposal_provider_id": provider_id,
        "operator_registry_id": operator_registry_id,
        "status": "ABSTAINED",
        "reason_codes": reason_codes,
    }
    evidence = {
        "schema_version": "evidence-result/v0.1",
        "status": "NOT_PRODUCED",
        "evaluation_status": "NOT_EVALUATED",
        "reason_codes": reason_codes,
    }
    review = {
        "schema_version": "review-packet/v0.1",
        "workflow_status": "ABSTAIN",
        "review_status": "HUMAN_REVIEW_REQUIRED",
        "selected_obligation": dict(obligation),
        "resolution_proposal": dict(proposal) if proposal is not None else None,
        "proposal_provider_id": provider_id,
        "operator_registry_id": operator_registry_id,
        "operator_run_receipt": receipt,
        "evidence_result": evidence,
        "forbidden_conclusions": [
            "SUPPORT",
            "CANNOT_SUPPORT",
            "SCIENTIFICALLY_VALIDATED",
            "AGENT_VALUE_ESTABLISHED",
        ],
    }
    return {
        "operator_run_receipt": receipt,
        "evidence_result": evidence,
        "review_packet": review,
    }


def run_resolution_stage(
    obligation: Mapping[str, Any],
    provider: ProposalProvider,
    registry: Mapping[str, Any],
    allowed_root: Path,
    request_id: str,
) -> dict[str, dict[str, Any]]:
    """Ask for one bounded proposal, then validate and authorize it deterministically."""

    obligation_errors = validate_review_obligation(obligation)
    provider_id = getattr(provider, "provider_id", None)
    operator_registry_id = registry.get("registry_id")
    if obligation_errors:
        return _abstain_artifacts(
            obligation,
            None,
            request_id,
            obligation_errors,
            provider_id=provider_id,
            operator_registry_id=operator_registry_id,
        )

    bounded_view = {
        "schema_version": "resolution-request-view/v0.1",
        "selected_obligation": dict(obligation),
        "registered_operator_summaries": operator_summary(registry),
        "authority": "PROPOSAL_ONLY",
    }
    try:
        proposal = provider.propose(bounded_view)
    except Exception as exc:  # provider implementations are an untrusted boundary
        return _abstain_artifacts(
            obligation,
            None,
            request_id,
            [f"PROVIDER_ERROR:{type(exc).__name__}"],
            provider_id=provider_id,
            operator_registry_id=operator_registry_id,
        )
    if not isinstance(proposal, Mapping):
        return _abstain_artifacts(
            obligation,
            None,
            request_id,
            ["PROVIDER_OUTPUT_NOT_OBJECT"],
            provider_id=provider_id,
            operator_registry_id=operator_registry_id,
        )
    proposal_errors = validate_resolution_proposal(proposal, obligation)
    if proposal_errors:
        return _abstain_artifacts(
            obligation,
            proposal,
            request_id,
            proposal_errors,
            provider_id=provider_id,
            operator_registry_id=operator_registry_id,
        )

    if proposal.get("action") == "ABSTAIN":
        return _abstain_artifacts(
            obligation,
            proposal,
            request_id,
            ["PROVIDER_REQUESTED_ABSTAIN", str(proposal.get("reason"))],
            provider_id=provider_id,
            operator_registry_id=operator_registry_id,
        )

    operator_id = str(proposal.get("operator_id"))
    spec, resolve_reasons = resolve_operator(
        registry, operator_id, str(obligation.get("obligation_type"))
    )
    if spec is None or resolve_reasons:
        return _abstain_artifacts(
            obligation,
            proposal,
            request_id,
            resolve_reasons,
            operator_id=operator_id,
            operator_version=str(spec.get("version")) if spec else None,
            provider_id=provider_id,
            operator_registry_id=operator_registry_id,
        )

    operator_inputs = proposal.get("operator_inputs")
    assert isinstance(operator_inputs, Mapping)
    try:
        output = execute_operator(spec, operator_inputs, allowed_root)
    except (OSError, ValueError) as exc:
        return _abstain_artifacts(
            obligation,
            proposal,
            request_id,
            [str(exc)],
            operator_id=operator_id,
            operator_version=str(spec.get("version")),
            provider_id=provider_id,
            operator_registry_id=operator_registry_id,
        )

    receipt = {
        "schema_version": "operator-run-receipt/v0.1",
        "request_id": request_id,
        "obligation_id": obligation.get("obligation_id"),
        "operator_id": operator_id,
        "operator_version": spec.get("version"),
        "proposal_provider_id": provider_id,
        "operator_registry_id": operator_registry_id,
        "status": "SUCCEEDED",
        "reason_codes": [],
        "input_summary": {
            "source_path": output["source_path"],
            "json_pointer": output["json_pointer"],
        },
    }
    evidence = {
        "schema_version": "evidence-result/v0.1",
        "status": "OBSERVED",
        "evaluation_status": "PENDING_HUMAN_VALIDATION",
        "obligation_id": obligation.get("obligation_id"),
        "observed_value": output["observed_value"],
        "provenance": {
            "operator_id": operator_id,
            "operator_version": spec.get("version"),
            "operator_registry_id": operator_registry_id,
            "proposal_provider_id": provider_id,
            "source_path": output["source_path"],
            "json_pointer": output["json_pointer"],
        },
        "claim_ceiling": spec.get("claim_ceiling"),
    }
    review = {
        "schema_version": "review-packet/v0.1",
        "workflow_status": "EVIDENCE_OBSERVED",
        "review_status": "HUMAN_REVIEW_REQUIRED",
        "selected_obligation": dict(obligation),
        "resolution_proposal": dict(proposal),
        "proposal_provider_id": provider_id,
        "operator_registry_id": operator_registry_id,
        "operator_run_receipt": receipt,
        "evidence_result": evidence,
        "forbidden_conclusions": [
            "SUPPORT",
            "CANNOT_SUPPORT",
            "SCIENTIFICALLY_VALIDATED",
            "AGENT_VALUE_ESTABLISHED",
        ],
    }
    return {
        "operator_run_receipt": receipt,
        "evidence_result": evidence,
        "review_packet": review,
    }
