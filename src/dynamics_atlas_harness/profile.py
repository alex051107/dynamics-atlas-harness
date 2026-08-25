"""Profile Agent proposal boundary for the existing rich CaseGraph contract."""

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .contracts import find_forbidden_answer_paths


@dataclass(frozen=True)
class CaseGraphAdmission:
    schema_version: str
    case_id: str | None
    status: str
    selector_access_allowed: bool
    reason_codes: tuple[str, ...]
    contract_version: str | None
    validator: str

    def to_dict(self) -> dict[str, Any]:
        value = asdict(self)
        value["reason_codes"] = list(self.reason_codes)
        return value


def build_profile_request(
    *,
    request_id: str,
    question: str,
    data_manifest: list[dict[str, Any]],
    prompt_ref: str,
    prompt_version: str,
) -> dict[str, Any]:
    """Build the bounded request seen by a Profile Agent implementation."""

    return {
        "schema_version": "profile-request/v0.1",
        "request_id": request_id,
        "question": question,
        "data_manifest": data_manifest,
        "prompt_ref": prompt_ref,
        "prompt_version": prompt_version,
        "authority": "PROPOSE_CASE_GRAPH_ONLY",
        "forbidden_actions": [
            "SELECT_RULES",
            "AUTHORIZE_OPERATOR",
            "READ_REFERENCE_ANSWER",
            "EMIT_FINAL_SCIENTIFIC_VERDICT",
        ],
    }


def _load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_case_graph(proposal: Mapping[str, Any], schema_path: Path) -> CaseGraphAdmission:
    """Validate a Profile proposal against the existing metadata contract.

    JSON Schema owns structural validation. This wrapper adds answer isolation and
    graph-identity checks before the existing selector can read the proposal.
    """

    if not isinstance(proposal, Mapping):
        return CaseGraphAdmission(
            schema_version="case-graph-admission/v0.1",
            case_id=None,
            status="INVALID_PROFILE",
            selector_access_allowed=False,
            reason_codes=("PROFILE_NOT_OBJECT",),
            contract_version=None,
            validator="jsonschema.Draft202012Validator",
        )

    errors: list[str] = []
    forbidden = find_forbidden_answer_paths(proposal)
    errors.extend(f"ANSWER_BEARING_KEY:{path}" for path in forbidden)

    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        errors.append("VALIDATOR_BACKEND_UNAVAILABLE:jsonschema")
    else:
        schema = _load_json(schema_path)
        validator = Draft202012Validator(schema)
        for error in sorted(validator.iter_errors(dict(proposal)), key=lambda item: list(item.path)):
            location = "$"
            for part in error.path:
                location += f"[{part}]" if isinstance(part, int) else f".{part}"
            errors.append(f"SCHEMA_ERROR:{location}:{error.validator}")

    case = proposal.get("case")
    case_id = case.get("case_id") if isinstance(case, Mapping) else None
    if not isinstance(case_id, str) or not case_id.strip():
        errors.append("MISSING_CASE_ID")
        case_id = None

    evidence_items = proposal.get("evidence_items")
    source_ids: set[str] = set()
    if isinstance(evidence_items, list):
        for item in evidence_items:
            source_id = item.get("source_id") if isinstance(item, Mapping) else None
            if isinstance(source_id, str):
                if source_id in source_ids:
                    errors.append(f"DUPLICATE_SOURCE_ID:{source_id}")
                source_ids.add(source_id)

    comparisons = proposal.get("comparisons")
    if isinstance(comparisons, list):
        for comparison in comparisons:
            if not isinstance(comparison, Mapping):
                continue
            comparison_id = comparison.get("comparison_id", "UNKNOWN")
            for field in ("left_source_id", "right_source_id"):
                endpoint = comparison.get(field)
                if endpoint not in source_ids:
                    errors.append(f"EDGE_ENDPOINT_NOT_FOUND:{comparison_id}:{field}")

    status = "INVALID_PROFILE" if errors else "PROFILE_READY"
    return CaseGraphAdmission(
        schema_version="case-graph-admission/v0.1",
        case_id=case_id,
        status=status,
        selector_access_allowed=not errors,
        reason_codes=tuple(errors),
        contract_version=str(proposal.get("contract_version"))
        if proposal.get("contract_version") is not None
        else None,
        validator="jsonschema.Draft202012Validator",
    )
