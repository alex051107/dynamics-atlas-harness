"""Truthful provenance for recorded or caller-supplied proposal replay.

This module records what the current case runner can actually establish.  It
does not reconstruct an absent prompt, raw response, provider, model, timestamp,
or cost, and it contains no credential reader or model transport.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from copy import deepcopy
from pathlib import Path, PurePosixPath, PureWindowsPath
from typing import Any


RECORDED_PROPOSAL_REPLAY = "RECORDED_PROPOSAL_REPLAY"
CALLER_SUPPLIED_IN_MEMORY = "CALLER_SUPPLIED_IN_MEMORY"
_ALLOWED_ROLES = {"PROFILER", "PLANNER"}
_ALLOWED_MODES = {RECORDED_PROPOSAL_REPLAY, CALLER_SUPPLIED_IN_MEMORY}
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
            raise ProposalProvenanceV1Error("IN_MEMORY_PROPOSAL_MUST_NOT_HAVE_SOURCE_PATH")
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

    unavailable_status = (
        "UNAVAILABLE_NOT_RECORDED"
        if mode == RECORDED_PROPOSAL_REPLAY
        else "UNAVAILABLE_CALLER_SUPPLIED_IN_MEMORY"
    )
    normalized_source_path = _repository_relative_source_path(source_path, mode=mode)
    return {
        "schema_version": "dynamics-atlas-proposal-provenance/v1",
        "role": role,
        "case_id": case_id,
        "mode": mode,
        "source_path": normalized_source_path,
        "source_path_status": (
            "REPOSITORY_RELATIVE"
            if normalized_source_path is not None
            else "UNAVAILABLE_CALLER_SUPPLIED_IN_MEMORY"
        ),
        "provider": {"provider_id": None, "status": unavailable_status},
        "model": {"model_id": None, "status": unavailable_status},
        "visible_input": {
            "canonicalization": _CANONICALIZATION,
            "canonical_sha256": canonical_json_sha256(visible_input),
        },
        "prompt": {
            "version": None,
            "sha256": None,
            "status": unavailable_status,
        },
        "raw_response": {"sha256": None, "status": unavailable_status},
        "parsed_proposal": {
            "canonicalization": _CANONICALIZATION,
            "canonical_sha256": canonical_json_sha256(parsed_proposal),
        },
        "recorded_timestamp": None,
        "recorded_timestamp_status": unavailable_status,
        "reported_cost": None,
        "reported_cost_status": unavailable_status,
        "contract_admission_evaluation": _evaluation_summary(
            contract_admission_evaluation,
            evaluator=contract_evaluator.strip(),
            case_id=case_id,
        ),
        "answer_blindness_status": "ANSWER_BLINDNESS_NOT_INDEPENDENTLY_VERIFIED",
        "filesystem_isolation_technically_enforced": False,
        "boundary": (
            "This receipt proves deterministic replay inputs and admission only. "
            "It does not prove a live model call, answer-blind isolation, Agent "
            "performance, or scientific correctness."
        ),
    }
