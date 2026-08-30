"""Truthful provenance for recorded, caller-supplied, or live proposals.

This module records only what the current case runner can establish.  Recorded
and in-memory modes do not reconstruct absent call metadata.  Live mode accepts a
sanitized, fail-closed transport receipt but contains no credential reader or model
transport itself.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections.abc import Mapping
from copy import deepcopy
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any


RECORDED_PROPOSAL_REPLAY = "RECORDED_PROPOSAL_REPLAY"
CALLER_SUPPLIED_IN_MEMORY = "CALLER_SUPPLIED_IN_MEMORY"
LIVE_OPENROUTER_PROPOSAL = "LIVE_OPENROUTER_PROPOSAL"
_ALLOWED_ROLES = {"PROFILER", "PLANNER"}
_ALLOWED_MODES = {
    RECORDED_PROPOSAL_REPLAY,
    CALLER_SUPPLIED_IN_MEMORY,
    LIVE_OPENROUTER_PROPOSAL,
}
_CANONICALIZATION = "SORTED_KEYS_COMPACT_JSON_UTF8_V1"


class ProposalProvenanceV1Error(ValueError):
    """Raised when a proposal provenance receipt would overstate its evidence."""


def canonical_json_sha256(value: Any) -> str:
    """Hash one JSON value using this module's declared stable encoding."""

    try:
        encoded = json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError) as error:
        raise ProposalProvenanceV1Error("JSON_SERIALIZABLE_VALUE_REQUIRED") from error
    return hashlib.sha256(encoded).hexdigest()


def _repository_relative_source_path(value: str | Path | None, *, mode: str) -> str | None:
    if mode == CALLER_SUPPLIED_IN_MEMORY:
        if value is not None:
            raise ProposalProvenanceV1Error(
                "IN_MEMORY_PROPOSAL_MUST_NOT_HAVE_SOURCE_PATH"
            )
        return None
    if mode == LIVE_OPENROUTER_PROPOSAL:
        if value is not None:
            raise ProposalProvenanceV1Error("LIVE_PROPOSAL_MUST_NOT_HAVE_SOURCE_PATH")
        return None
    if not isinstance(value, (str, Path)) or not str(value).strip():
        raise ProposalProvenanceV1Error("RECORDED_PROPOSAL_SOURCE_PATH_REQUIRED")
    text = str(value).strip()
    if Path(text).is_absolute() or PureWindowsPath(text).is_absolute():
        raise ProposalProvenanceV1Error("PROPOSAL_SOURCE_PATH_MUST_BE_REPOSITORY_RELATIVE")
    normalized = PurePosixPath(text.replace("\\", "/"))
    if normalized == PurePosixPath(".") or ".." in normalized.parts:
        raise ProposalProvenanceV1Error("PROPOSAL_SOURCE_PATH_MUST_BE_REPOSITORY_RELATIVE")
    return normalized.as_posix()


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ProposalProvenanceV1Error(f"LIVE_CALL_RECEIPT_FIELD_REQUIRED:{label}")
    return value.strip()


def _require_sha256(value: Any, label: str) -> str:
    text = _require_string(value, label)
    if len(text) != 64 or any(character not in "0123456789abcdef" for character in text):
        raise ProposalProvenanceV1Error(f"LIVE_CALL_RECEIPT_SHA256_INVALID:{label}")
    return text


def _validated_live_call_receipt(
    *,
    receipt: Mapping[str, Any] | None,
    role: str,
    case_id: str,
    visible_input: Mapping[str, Any],
    parsed_proposal: Mapping[str, Any],
) -> dict[str, Any]:
    if not isinstance(receipt, Mapping):
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_REQUIRED")
    value = deepcopy(dict(receipt))
    if value.get("schema_version") != "openrouter-proposal-call-receipt/v1":
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_SCHEMA_INVALID")
    expected = {
        "status": "ADMITTED_TYPED_PROPOSAL",
        "transport_status": "COMPLETED_RESPONSE",
        "proposal_parse_status": "PARSED_JSON_OBJECT",
        "schema_validation_status": "PASS",
        "role": role,
        "case_id": case_id,
        "finish_reason": "stop",
        "incomplete_status": "NOT_INCOMPLETE",
        "tool_calls": 0,
        "automatic_retries": 0,
    }
    for field, expected_value in expected.items():
        if value.get(field) != expected_value:
            raise ProposalProvenanceV1Error(
                f"LIVE_CALL_RECEIPT_INVARIANT_MISMATCH:{field}"
            )
    if value.get("reason_codes") != []:
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_HAS_BLOCKING_REASON")
    for field in (
        "requested_model",
        "returned_model",
        "requested_provider_endpoint_tag",
        "expected_provider_display_name",
        "actual_provider",
        "response_id",
        "recorded_at",
        "prompt_version",
    ):
        _require_string(value.get(field), field)
    accepted_model_ids = value.get("accepted_returned_model_ids")
    if not isinstance(accepted_model_ids, list) or any(
        not isinstance(model_id, str) or not model_id.strip()
        for model_id in accepted_model_ids
    ):
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_ACCEPTED_MODELS_INVALID")
    if value.get("returned_model") not in accepted_model_ids:
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_MODEL_MISMATCH")
    if value.get("returned_model_provenance_status") not in {
        "EXACT_REQUEST_ID",
        "ACCEPTED_CANONICAL_ID",
    }:
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_MODEL_PROVENANCE_INVALID")
    if value.get("provider_provenance_status") != "EXACT_MATCH":
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_PROVIDER_PROVENANCE_INVALID")
    if (
        value["actual_provider"].casefold()
        != value["expected_provider_display_name"].casefold()
    ):
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_PROVIDER_MISMATCH")
    allowed_service_tiers = value.get("allowed_service_tiers")
    if not isinstance(allowed_service_tiers, list) or value.get(
        "service_tier"
    ) not in allowed_service_tiers:
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_SERVICE_TIER_MISMATCH")
    if value.get("service_tier_provenance_status") != "EXACT_ALLOWED_VALUE":
        raise ProposalProvenanceV1Error(
            "LIVE_CALL_RECEIPT_SERVICE_TIER_PROVENANCE_INVALID"
        )
    if role == "PROFILER":
        annotation_status = value.get("field_annotation_validation_status")
        if annotation_status not in {"PASS", "REJECTED_DIAGNOSTIC_ONLY"}:
            raise ProposalProvenanceV1Error(
                "LIVE_CALL_RECEIPT_ANNOTATION_STATUS_INVALID"
            )
        annotation_error = value.get("field_annotation_error_code")
        if annotation_status == "PASS" and annotation_error is not None:
            raise ProposalProvenanceV1Error(
                "LIVE_CALL_RECEIPT_ANNOTATION_ERROR_UNEXPECTED"
            )
        if annotation_status == "REJECTED_DIAGNOSTIC_ONLY" and (
            not isinstance(annotation_error, str) or not annotation_error
        ):
            raise ProposalProvenanceV1Error(
                "LIVE_CALL_RECEIPT_ANNOTATION_ERROR_REQUIRED"
            )
    hashes = value.get("hashes")
    if not isinstance(hashes, Mapping):
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_HASHES_REQUIRED")
    for field in (
        "system_prompt_sha256",
        "visible_input_sha256",
        "output_schema_sha256",
        "request_payload_sha256",
        "raw_response_sha256",
        "parsed_proposal_sha256",
    ):
        _require_sha256(hashes.get(field), field)
    if hashes["visible_input_sha256"] != canonical_json_sha256(visible_input):
        raise ProposalProvenanceV1Error("LIVE_CALL_VISIBLE_INPUT_HASH_MISMATCH")
    if value.get("routing_proposal_sha256") != canonical_json_sha256(parsed_proposal):
        raise ProposalProvenanceV1Error("LIVE_CALL_ROUTING_PROPOSAL_HASH_MISMATCH")
    usage = value.get("usage")
    if not isinstance(usage, Mapping):
        raise ProposalProvenanceV1Error("LIVE_CALL_USAGE_REQUIRED")
    for field in ("prompt_tokens", "completion_tokens", "total_tokens"):
        token_count = usage.get(field)
        if not isinstance(token_count, int) or isinstance(token_count, bool) or token_count < 0:
            raise ProposalProvenanceV1Error(f"LIVE_CALL_USAGE_INVALID:{field}")
    reported_cost = value.get("reported_cost_usd")
    if not isinstance(reported_cost, str) or not reported_cost:
        raise ProposalProvenanceV1Error("LIVE_CALL_REPORTED_COST_REQUIRED")
    try:
        numeric_cost = float(reported_cost)
    except ValueError as error:
        raise ProposalProvenanceV1Error("LIVE_CALL_REPORTED_COST_INVALID") from error
    if numeric_cost < 0 or not math.isfinite(numeric_cost):
        raise ProposalProvenanceV1Error("LIVE_CALL_REPORTED_COST_INVALID")
    if not isinstance(value.get("campaign_budget"), Mapping):
        raise ProposalProvenanceV1Error("LIVE_CALL_CAMPAIGN_BUDGET_REQUIRED")
    latency_ms = value.get("latency_ms")
    if not isinstance(latency_ms, (int, float)) or isinstance(latency_ms, bool) or latency_ms < 0:
        raise ProposalProvenanceV1Error("LIVE_CALL_LATENCY_INVALID")
    return value


def _evaluation_summary(
    evaluation: Mapping[str, Any], *, evaluator: str, case_id: str
) -> dict[str, Any]:
    status = evaluation.get("proposal_status", evaluation.get("status"))
    result = {
        field: deepcopy(evaluation[field])
        for field in (
            "schema_version",
            "proposal_status",
            "status",
            "decision",
            "selected_card_ids",
            "execution_authorization",
            "scientific_disposition",
        )
        if field in evaluation
    }
    return {
        "evaluator": evaluator,
        "case_id": case_id,
        "status": status if isinstance(status, str) and status else "STATUS_NOT_EXPOSED",
        "canonical_sha256": canonical_json_sha256(evaluation),
        "result": result,
    }


def build_proposal_provenance_v1(
    *,
    role: str,
    mode: str,
    visible_input: Mapping[str, Any],
    parsed_proposal: Mapping[str, Any],
    contract_evaluator: str,
    contract_admission_evaluation: Mapping[str, Any],
    source_path: str | Path | None,
    live_call_receipt: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build one fail-closed receipt without inventing missing call metadata."""

    if role not in _ALLOWED_ROLES:
        raise ProposalProvenanceV1Error("PROPOSAL_ROLE_INVALID")
    if mode not in _ALLOWED_MODES:
        raise ProposalProvenanceV1Error("PROPOSAL_MODE_INVALID")
    if not isinstance(visible_input, Mapping):
        raise ProposalProvenanceV1Error("VISIBLE_INPUT_MAPPING_REQUIRED")
    if not isinstance(parsed_proposal, Mapping):
        raise ProposalProvenanceV1Error("PARSED_PROPOSAL_MAPPING_REQUIRED")
    if not isinstance(contract_admission_evaluation, Mapping):
        raise ProposalProvenanceV1Error("CONTRACT_EVALUATION_MAPPING_REQUIRED")
    if not isinstance(contract_evaluator, str) or not contract_evaluator.strip():
        raise ProposalProvenanceV1Error("CONTRACT_EVALUATOR_REQUIRED")
    case_id = parsed_proposal.get("case_id")
    if not isinstance(case_id, str) or not case_id.strip():
        raise ProposalProvenanceV1Error("PARSED_PROPOSAL_CASE_ID_REQUIRED")

    if mode != LIVE_OPENROUTER_PROPOSAL and live_call_receipt is not None:
        raise ProposalProvenanceV1Error("LIVE_CALL_RECEIPT_FOR_NONLIVE_MODE")
    live_receipt = (
        _validated_live_call_receipt(
            receipt=live_call_receipt,
            role=role,
            case_id=case_id,
            visible_input=visible_input,
            parsed_proposal=parsed_proposal,
        )
        if mode == LIVE_OPENROUTER_PROPOSAL
        else None
    )
    unavailable_status = (
        "UNAVAILABLE_NOT_RECORDED"
        if mode == RECORDED_PROPOSAL_REPLAY
        else "UNAVAILABLE_CALLER_SUPPLIED_IN_MEMORY"
    )
    normalized_source_path = _repository_relative_source_path(source_path, mode=mode)
    result = {
        "schema_version": "dynamics-atlas-proposal-provenance/v1",
        "role": role,
        "case_id": case_id,
        "mode": mode,
        "source_path": normalized_source_path,
        "source_path_status": (
            "REPOSITORY_RELATIVE"
            if normalized_source_path is not None
            else (
                "LIVE_CALL_ARTIFACT"
                if live_receipt is not None
                else "UNAVAILABLE_CALLER_SUPPLIED_IN_MEMORY"
            )
        ),
        "provider": (
            {
                "provider_id": live_receipt["actual_provider"],
                "requested_provider_endpoint_tag": live_receipt[
                    "requested_provider_endpoint_tag"
                ],
                "expected_provider_display_name": live_receipt[
                    "expected_provider_display_name"
                ],
                "service_tier": live_receipt["service_tier"],
                "status": "VERIFIED_FROM_OPENROUTER_RESPONSE_METADATA",
            }
            if live_receipt is not None
            else {"provider_id": None, "status": unavailable_status}
        ),
        "model": (
            {
                "model_id": live_receipt["returned_model"],
                "requested_model_id": live_receipt["requested_model"],
                "status": "VERIFIED_AGAINST_FROZEN_ACCEPTED_MODEL_IDS",
            }
            if live_receipt is not None
            else {"model_id": None, "status": unavailable_status}
        ),
        "visible_input": {
            "canonicalization": _CANONICALIZATION,
            "canonical_sha256": canonical_json_sha256(visible_input),
        },
        "prompt": (
            {
                "version": live_receipt["prompt_version"],
                "sha256": live_receipt["hashes"]["system_prompt_sha256"],
                "status": "RECORDED_LIVE_CALL",
            }
            if live_receipt is not None
            else {"version": None, "sha256": None, "status": unavailable_status}
        ),
        "raw_response": (
            {
                "sha256": live_receipt["hashes"]["raw_response_sha256"],
                "status": "RECORDED_LIVE_CALL",
            }
            if live_receipt is not None
            else {"sha256": None, "status": unavailable_status}
        ),
        "parsed_proposal": {
            "canonicalization": _CANONICALIZATION,
            "canonical_sha256": canonical_json_sha256(parsed_proposal),
        },
        "recorded_timestamp": live_receipt["recorded_at"] if live_receipt is not None else None,
        "recorded_timestamp_status": (
            "RECORDED_LIVE_CALL" if live_receipt is not None else unavailable_status
        ),
        "reported_cost": (
            live_receipt["reported_cost_usd"] if live_receipt is not None else None
        ),
        "reported_cost_status": (
            "PROVIDER_REPORTED" if live_receipt is not None else unavailable_status
        ),
        "response_id": live_receipt["response_id"] if live_receipt is not None else None,
        "finish_reason": live_receipt["finish_reason"] if live_receipt is not None else None,
        "latency_ms": live_receipt["latency_ms"] if live_receipt is not None else None,
        "usage": deepcopy(live_receipt["usage"]) if live_receipt is not None else None,
        "campaign_budget": (
            deepcopy(live_receipt["campaign_budget"])
            if live_receipt is not None
            else None
        ),
        "live_call_receipt": live_receipt,
        "contract_admission_evaluation": _evaluation_summary(
            contract_admission_evaluation,
            evaluator=contract_evaluator.strip(),
            case_id=case_id,
        ),
        "answer_blindness_status": (
            "PUBLIC_PACKET_ONLY_INPUT_HASH_RECORDED"
            if live_receipt is not None
            else "ANSWER_BLINDNESS_NOT_INDEPENDENTLY_VERIFIED"
        ),
        "filesystem_isolation_technically_enforced": False,
        "boundary": (
            "This receipt proves the recorded proposal input and deterministic admission. "
            + (
                "For live mode it also records one bounded OpenRouter proposal transport. "
                if live_receipt is not None
                else "It does not prove a live model call. "
            )
            + "It does not prove independent answer-blind isolation, Agent value, or scientific correctness."
        ),
    }
    return result
