"""Small, deterministic validators for the prototype boundary."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import asdict, dataclass
from typing import Any


FORBIDDEN_ANSWER_KEYS = frozenset(
    {
        "answer",
        "expected_answer",
        "expected_result",
        "gold",
        "gold_answer",
        "reference_answer",
        "supports_claim",
        "verdict",
    }
)

ALLOWED_SOURCE_TYPES = frozenset({"TABULAR_METADATA", "MD_TRAJECTORY"})


@dataclass(frozen=True)
class ProfileAdmission:
    schema_version: str
    case_id: str | None
    status: str
    reason_codes: tuple[str, ...]
    selector_access_allowed: bool
    method_profile_registry_id: str | None

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["reason_codes"] = list(self.reason_codes)
        return result


def _is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def find_forbidden_answer_paths(value: Any, path: str = "$") -> list[str]:
    """Return every recursively nested answer-bearing key path."""

    paths: list[str] = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            key_text = str(key)
            child_path = f"{path}.{key_text}"
            if key_text.casefold() in FORBIDDEN_ANSWER_KEYS:
                paths.append(child_path)
            paths.extend(find_forbidden_answer_paths(item, child_path))
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, item in enumerate(value):
            paths.extend(find_forbidden_answer_paths(item, f"{path}[{index}]"))
    return paths


def validate_case_profile(
    proposal: Mapping[str, Any],
    approved_method_profiles: set[str] | frozenset[str],
    method_profile_registry_id: str | None = None,
) -> ProfileAdmission:
    """Validate a proposal without selecting rules or inspecting answer material."""

    errors: list[str] = []
    method_reasons: list[str] = []
    case_id = proposal.get("case_id") if isinstance(proposal, Mapping) else None

    if not isinstance(proposal, Mapping):
        return ProfileAdmission(
            schema_version="profile-admission/v0.1",
            case_id=None,
            status="INVALID_PROFILE",
            reason_codes=("PROFILE_NOT_OBJECT",),
            selector_access_allowed=False,
            method_profile_registry_id=method_profile_registry_id,
        )

    if proposal.get("schema_version") != "case-profile-proposal/v0.1":
        errors.append("INVALID_PROFILE_SCHEMA")
    if not _is_nonempty_string(case_id):
        errors.append("MISSING_CASE_ID")
        case_id = None
    if not _is_nonempty_string(proposal.get("question")):
        errors.append("MISSING_QUESTION")

    forbidden_paths = find_forbidden_answer_paths(proposal)
    errors.extend(f"ANSWER_BEARING_KEY:{path}" for path in forbidden_paths)

    sources = proposal.get("sources")
    source_ids: set[str] = set()
    if not isinstance(sources, list) or not sources:
        errors.append("MISSING_SOURCES")
        sources = []
    for index, source in enumerate(sources):
        if not isinstance(source, Mapping):
            errors.append(f"SOURCE_NOT_OBJECT:{index}")
            continue
        source_id = source.get("source_id")
        source_type = source.get("source_type")
        if not _is_nonempty_string(source_id):
            errors.append(f"MISSING_SOURCE_ID:{index}")
            continue
        if source_id in source_ids:
            errors.append(f"DUPLICATE_SOURCE_ID:{source_id}")
        source_ids.add(str(source_id))
        if not _is_nonempty_string(source_type):
            errors.append(f"MISSING_SOURCE_TYPE:{source_id}")
            continue
        if source_type not in ALLOWED_SOURCE_TYPES:
            errors.append(f"UNREGISTERED_SOURCE_TYPE:{source_id}:{source_type}")
            continue
        if source_type == "MD_TRAJECTORY":
            profile_id = source.get("method_profile_id")
            if not _is_nonempty_string(profile_id) or profile_id not in approved_method_profiles:
                method_reasons.append(f"NEEDS_METHOD_PROFILE:{source_id}")

    edges = proposal.get("edges", [])
    if not isinstance(edges, list):
        errors.append("EDGES_NOT_LIST")
        edges = []
    for index, edge in enumerate(edges):
        if not isinstance(edge, Mapping):
            errors.append(f"EDGE_NOT_OBJECT:{index}")
            continue
        edge_id = edge.get("edge_id")
        source_a = edge.get("source_a")
        source_b = edge.get("source_b")
        if not _is_nonempty_string(edge_id):
            errors.append(f"MISSING_EDGE_ID:{index}")
        if source_a not in source_ids or source_b not in source_ids:
            errors.append(f"EDGE_ENDPOINT_NOT_FOUND:{edge_id or index}")

    unknowns = proposal.get("unknowns", [])
    if not isinstance(unknowns, list) or any(
        not _is_nonempty_string(item) for item in unknowns
    ):
        errors.append("INVALID_UNKNOWNS")

    if errors:
        status = "INVALID_PROFILE"
        reasons = tuple(errors + method_reasons)
    elif method_reasons:
        status = "NEEDS_METHOD_PROFILE"
        reasons = tuple(method_reasons)
    else:
        status = "PROFILE_READY"
        reasons = ()

    return ProfileAdmission(
        schema_version="profile-admission/v0.1",
        case_id=case_id,
        status=status,
        reason_codes=reasons,
        selector_access_allowed=status == "PROFILE_READY",
        method_profile_registry_id=method_profile_registry_id,
    )


def validate_review_obligation(obligation: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    if obligation.get("schema_version") != "review-obligation/v0.1":
        errors.append("INVALID_OBLIGATION_SCHEMA")
    for field in ("obligation_id", "obligation_type", "target_kind", "target_id", "question"):
        if not _is_nonempty_string(obligation.get(field)):
            errors.append(f"MISSING_OBLIGATION_FIELD:{field}")
    options = obligation.get("allowed_resolution_actions")
    if not isinstance(options, list) or not options or any(
        not _is_nonempty_string(item) for item in options
    ):
        errors.append("INVALID_ALLOWED_RESOLUTION_ACTIONS")
    errors.extend(
        f"ANSWER_BEARING_KEY:{path}" for path in find_forbidden_answer_paths(obligation)
    )
    return errors


def validate_resolution_proposal(
    proposal: Mapping[str, Any], obligation: Mapping[str, Any]
) -> list[str]:
    errors: list[str] = []
    if not isinstance(proposal, Mapping):
        return ["PROVIDER_OUTPUT_NOT_OBJECT"]
    if proposal.get("schema_version") != "resolution-proposal/v0.1":
        errors.append("INVALID_RESOLUTION_PROPOSAL_SCHEMA")
    if proposal.get("obligation_id") != obligation.get("obligation_id"):
        errors.append("OBLIGATION_ID_MISMATCH")
    action = proposal.get("action")
    allowed_actions = obligation.get("allowed_resolution_actions", [])
    if action not in allowed_actions:
        errors.append("ACTION_NOT_ALLOWED_FOR_OBLIGATION")
    if action == "RUN_OPERATOR":
        if not _is_nonempty_string(proposal.get("operator_id")):
            errors.append("MISSING_OPERATOR_ID")
        if not isinstance(proposal.get("operator_inputs"), Mapping):
            errors.append("MISSING_OPERATOR_INPUTS")
    elif action == "ABSTAIN":
        if not _is_nonempty_string(proposal.get("reason")):
            errors.append("MISSING_ABSTAIN_REASON")
    errors.extend(
        f"ANSWER_BEARING_KEY:{path}" for path in find_forbidden_answer_paths(proposal)
    )
    return errors
