"""Compatible Profiler envelope with diagnostic-only field annotations.

The envelope keeps the existing four-field paper-blind Profiler proposal intact.
Only that extracted core is admitted by ``validate_agent_proposal`` and may enter
the deterministic Rules projection.  ``field_annotations`` describe provenance
and epistemic status for development diagnostics; they have no routing authority.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from collections.abc import Mapping
from copy import deepcopy
from numbers import Real
from pathlib import Path
from typing import Any

from .paper_blind_exposed_v1 import (
    build_agent_visible_packet,
    load_public_packet,
    validate_agent_proposal,
)


PROFILE_PROPOSAL_ENVELOPE_SCHEMA = "paper-blind-profile-proposal-envelope/v1"
PROFILE_PROPOSAL_ENVELOPE_ADMISSION_SCHEMA = (
    "paper-blind-profile-proposal-envelope-admission/v1"
)

CORE_PROPOSAL_FIELDS = (
    "case_id",
    "proposed_case_facts",
    "unknowns",
    "rationale",
)
ANNOTATION_STATUSES = (
    "EXTRACTED",
    "INFERRED_WITH_SUPPORT",
    "UNKNOWN",
    "CONFLICTING_SOURCES",
    "HUMAN_CHECK_REQUIRED",
)
ANNOTATION_TARGET_TYPES = ("CASE", "SOURCE", "EDGE")
EVIDENCE_POINTER_TYPES = (
    "SOURCE_LOCATOR",
    "PERMITTED_FACT",
    "PACKET_POINTER",
)
PACKET_POINTER_SOURCE_ID = "PACKET"

_ENVELOPE_FIELDS = frozenset((*CORE_PROPOSAL_FIELDS, "field_annotations"))
_ANNOTATION_FIELDS = frozenset(
    {
        "target_type",
        "target_id",
        "field",
        "status",
        "evidence_pointers",
        "confidence",
    }
)
_EVIDENCE_POINTER_FIELDS = frozenset({"pointer_type", "source_id", "value"})
_CRITICAL_FIELDS = {
    "CASE": (
        "scientific_claim",
        "requested_claim_level",
        "intended_use",
        "declared_request_scope",
        "forbidden_upgrades",
    ),
    "SOURCE": (
        "construct_and_condition",
        "sample_composition",
        "native_observable",
        "estimand",
        "time_semantics.kind",
        "spatial_support",
        "unit_or_aggregation",
    ),
    "EDGE": (
        "relation_type",
        "condition_relation",
        "bridge_status",
        "validation_independence",
        "shared_error_status",
    ),
}
_UNKNOWN_TOKEN = re.compile(r"\bUNKNOWN\b", flags=re.IGNORECASE)
_UNRESOLVED_STATUSES = {
    "UNKNOWN",
    "CONFLICTING_SOURCES",
    "HUMAN_CHECK_REQUIRED",
}
_ALLOWED_EVIDENCE_ROLES = (
    "CONSTRUCTION",
    "DIAGNOSTIC",
    "FIT_TARGET",
    "HELD_OUT_VALIDATION",
    "UNKNOWN",
)


class ProfileProposalEnvelopeV1Error(ValueError):
    """Raised when an annotation envelope crosses its diagnostic boundary."""


def _object_schema(properties: Mapping[str, Any], required: tuple[str, ...]) -> dict[str, Any]:
    return {
        "type": "object",
        "additionalProperties": False,
        "required": list(required),
        "properties": dict(properties),
    }


def _nonempty_string_schema(**extra: Any) -> dict[str, Any]:
    # Enum members in this contract are all non-empty. Omitting the redundant
    # minLength assertion for enum fields keeps the strict schema inside the
    # xgrammar subset used by the pinned Sail Research endpoint.
    return {
        "type": "string",
        **({} if "enum" in extra or "const" in extra else {"minLength": 1}),
        **extra,
    }


def build_profile_proposal_envelope_schema(packet_path: str | Path) -> dict[str, Any]:
    """Build one strict JSON Schema without exposing sealed reference material."""

    packet = load_public_packet(packet_path)
    case_id = packet["case_id"]
    source_ids = [source["source_id"] for source in packet["source_materials"]]

    case_schema = _object_schema(
        {
            "scientific_claim": _nonempty_string_schema(),
            "requested_claim_level": _nonempty_string_schema(),
            "intended_use": _nonempty_string_schema(),
            "declared_request_scope": {
                "type": "array",
                "minItems": 1,
                "items": _nonempty_string_schema(),
            },
            "forbidden_upgrades": {
                "type": "array",
                "minItems": 1,
                "items": _nonempty_string_schema(),
            },
        },
        (
            "scientific_claim",
            "requested_claim_level",
            "intended_use",
            "declared_request_scope",
            "forbidden_upgrades",
        ),
    )
    source_schema = _object_schema(
        {
            "source_id": _nonempty_string_schema(enum=source_ids),
            "evidence_role": _nonempty_string_schema(enum=list(_ALLOWED_EVIDENCE_ROLES)),
            "construct_and_condition": _nonempty_string_schema(),
            "sample_composition": _nonempty_string_schema(),
            "native_observable": _nonempty_string_schema(),
            "estimand": _nonempty_string_schema(),
            "time_semantics": _object_schema(
                {"kind": _nonempty_string_schema()}, ("kind",)
            ),
            "spatial_support": _nonempty_string_schema(),
            "unit_or_aggregation": _nonempty_string_schema(),
        },
        (
            "source_id",
            "evidence_role",
            "construct_and_condition",
            "sample_composition",
            "native_observable",
            "estimand",
            "time_semantics",
            "spatial_support",
            "unit_or_aggregation",
        ),
    )
    edge_schema = _object_schema(
        {
            "edge_id": _nonempty_string_schema(),
            "left_source_id": _nonempty_string_schema(enum=source_ids),
            "right_source_id": _nonempty_string_schema(enum=source_ids),
            "relation_type": _nonempty_string_schema(),
            "condition_relation": _nonempty_string_schema(),
            "bridge_status": _nonempty_string_schema(),
            "validation_independence": _nonempty_string_schema(),
            "shared_error_status": _nonempty_string_schema(),
        },
        (
            "edge_id",
            "left_source_id",
            "right_source_id",
            "relation_type",
            "condition_relation",
            "bridge_status",
            "validation_independence",
            "shared_error_status",
        ),
    )
    pointer_schema = _object_schema(
        {
            "pointer_type": _nonempty_string_schema(enum=list(EVIDENCE_POINTER_TYPES)),
            "source_id": _nonempty_string_schema(
                enum=[*source_ids, PACKET_POINTER_SOURCE_ID]
            ),
            "value": _nonempty_string_schema(),
        },
        ("pointer_type", "source_id", "value"),
    )
    annotation_schema = _object_schema(
        {
            "target_type": _nonempty_string_schema(enum=list(ANNOTATION_TARGET_TYPES)),
            "target_id": _nonempty_string_schema(),
            "field": _nonempty_string_schema(
                enum=sorted({field for fields in _CRITICAL_FIELDS.values() for field in fields})
            ),
            "status": _nonempty_string_schema(enum=list(ANNOTATION_STATUSES)),
            "evidence_pointers": {
                "type": "array",
                "minItems": 1,
                "items": pointer_schema,
            },
            "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        },
        (
            "target_type",
            "target_id",
            "field",
            "status",
            "evidence_pointers",
            "confidence",
        ),
    )
    facts_schema = _object_schema(
        {
            "case": case_schema,
            "sources": {"type": "array", "minItems": 1, "items": source_schema},
            "edges": {"type": "array", "minItems": 1, "items": edge_schema},
        },
        ("case", "sources", "edges"),
    )
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "title": "Dynamics Atlas compatible Profiler proposal envelope",
        "description": (
            "The existing four-field proposal is the only routing input. "
            "field_annotations are diagnostic-only."
        ),
        **_object_schema(
            {
                "case_id": {"type": "string", "const": case_id},
                "proposed_case_facts": facts_schema,
                "unknowns": {
                    "type": "array",
                    "minItems": 1,
                    "items": _nonempty_string_schema(),
                },
                "rationale": _nonempty_string_schema(),
                "field_annotations": {
                    "type": "array",
                    "minItems": 1,
                    "items": annotation_schema,
                },
            },
            (*CORE_PROPOSAL_FIELDS, "field_annotations"),
        ),
    }


def extract_core_proposal(envelope: Mapping[str, Any]) -> dict[str, Any]:
    """Extract a deep-copied legacy proposal and reject any envelope shape drift."""

    if not isinstance(envelope, Mapping):
        raise ProfileProposalEnvelopeV1Error("ENVELOPE_MUST_BE_OBJECT")
    if set(envelope) != _ENVELOPE_FIELDS:
        raise ProfileProposalEnvelopeV1Error("ENVELOPE_FIELDS_DO_NOT_MATCH_CONTRACT")
    return {field: deepcopy(envelope[field]) for field in CORE_PROPOSAL_FIELDS}


def _require_nonempty_string(value: Any, code: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ProfileProposalEnvelopeV1Error(code)
    return value.strip()


def _decode_json_pointer_token(token: str) -> str:
    index = 0
    decoded: list[str] = []
    while index < len(token):
        if token[index] != "~":
            decoded.append(token[index])
            index += 1
            continue
        if index + 1 >= len(token) or token[index + 1] not in {"0", "1"}:
            raise ProfileProposalEnvelopeV1Error("PACKET_POINTER_INVALID_ESCAPE")
        decoded.append("~" if token[index + 1] == "0" else "/")
        index += 2
    return "".join(decoded)


def _resolve_visible_packet_pointer(visible_packet: Mapping[str, Any], pointer: str) -> Any:
    if not pointer.startswith("/"):
        raise ProfileProposalEnvelopeV1Error("PACKET_POINTER_MUST_BE_JSON_POINTER")
    current: Any = visible_packet
    for raw_token in pointer.split("/")[1:]:
        token = _decode_json_pointer_token(raw_token)
        if isinstance(current, Mapping):
            if token not in current:
                raise ProfileProposalEnvelopeV1Error("PACKET_POINTER_DANGLING")
            current = current[token]
        elif isinstance(current, list):
            if not token.isdigit() or (len(token) > 1 and token.startswith("0")):
                raise ProfileProposalEnvelopeV1Error("PACKET_POINTER_DANGLING")
            index = int(token)
            if index >= len(current):
                raise ProfileProposalEnvelopeV1Error("PACKET_POINTER_DANGLING")
            current = current[index]
        else:
            raise ProfileProposalEnvelopeV1Error("PACKET_POINTER_DANGLING")
    if not isinstance(current, str) or not current.strip():
        raise ProfileProposalEnvelopeV1Error("PACKET_POINTER_MUST_RESOLVE_TO_STRING_LEAF")
    return current


def _validate_evidence_pointer(
    value: Any,
    *,
    packet_sources: Mapping[str, Mapping[str, Any]],
    visible_packet: Mapping[str, Any],
) -> dict[str, str]:
    if not isinstance(value, Mapping) or set(value) != _EVIDENCE_POINTER_FIELDS:
        raise ProfileProposalEnvelopeV1Error("EVIDENCE_POINTER_FIELDS_INVALID")
    pointer_type = _require_nonempty_string(
        value.get("pointer_type"), "EVIDENCE_POINTER_TYPE_REQUIRED"
    )
    if pointer_type not in EVIDENCE_POINTER_TYPES:
        raise ProfileProposalEnvelopeV1Error("EVIDENCE_POINTER_TYPE_INVALID")
    source_id = _require_nonempty_string(
        value.get("source_id"), "EVIDENCE_POINTER_SOURCE_ID_REQUIRED"
    )
    pointer_value = _require_nonempty_string(
        value.get("value"), "EVIDENCE_POINTER_VALUE_REQUIRED"
    )

    if pointer_type == "PACKET_POINTER":
        if source_id != PACKET_POINTER_SOURCE_ID:
            raise ProfileProposalEnvelopeV1Error("PACKET_POINTER_SOURCE_ID_INVALID")
        _resolve_visible_packet_pointer(visible_packet, pointer_value)
    else:
        source = packet_sources.get(source_id)
        if source is None:
            raise ProfileProposalEnvelopeV1Error("EVIDENCE_POINTER_SOURCE_DANGLING")
        if pointer_type == "SOURCE_LOCATOR":
            if pointer_value != source["source_locator"]:
                raise ProfileProposalEnvelopeV1Error("SOURCE_LOCATOR_NOT_PERMITTED")
        elif pointer_value not in source["permitted_facts"]:
            raise ProfileProposalEnvelopeV1Error("PERMITTED_FACT_POINTER_NOT_PERMITTED")
    return {
        "pointer_type": pointer_type,
        "source_id": source_id,
        "value": pointer_value,
    }


def _critical_target_values(core: Mapping[str, Any]) -> dict[tuple[str, str, str], Any]:
    case_id = core["case_id"]
    facts = core["proposed_case_facts"]
    result: dict[tuple[str, str, str], Any] = {}
    for field in _CRITICAL_FIELDS["CASE"]:
        result[("CASE", case_id, field)] = facts["case"][field]
    for source in facts["sources"]:
        source_id = source["source_id"]
        for field in _CRITICAL_FIELDS["SOURCE"]:
            result[("SOURCE", source_id, field)] = (
                source["time_semantics"]["kind"]
                if field == "time_semantics.kind"
                else source[field]
            )
    for edge in facts["edges"]:
        edge_id = edge["edge_id"]
        for field in _CRITICAL_FIELDS["EDGE"]:
            result[("EDGE", edge_id, field)] = edge[field]
    return result


def _contains_unknown_token(value: Any) -> bool:
    if isinstance(value, str):
        return _UNKNOWN_TOKEN.search(value) is not None
    if isinstance(value, list):
        return any(_contains_unknown_token(item) for item in value)
    if isinstance(value, Mapping):
        return any(_contains_unknown_token(item) for item in value.values())
    return False


def _validate_confidence(value: Any) -> float:
    if (
        not isinstance(value, Real)
        or isinstance(value, bool)
        or not math.isfinite(float(value))
        or not 0 <= float(value) <= 1
    ):
        raise ProfileProposalEnvelopeV1Error("ANNOTATION_CONFIDENCE_OUT_OF_RANGE")
    return float(value)


def _validate_annotations(
    *,
    packet: Mapping[str, Any],
    visible_packet: Mapping[str, Any],
    core: Mapping[str, Any],
    annotations: Any,
) -> list[dict[str, Any]]:
    if not isinstance(annotations, list) or not annotations:
        raise ProfileProposalEnvelopeV1Error("FIELD_ANNOTATIONS_MUST_BE_NONEMPTY_LIST")
    expected_targets = _critical_target_values(core)
    packet_sources = {
        source["source_id"]: source for source in packet["source_materials"]
    }
    seen_targets: set[tuple[str, str, str]] = set()
    normalized: list[dict[str, Any]] = []

    for annotation in annotations:
        if not isinstance(annotation, Mapping) or set(annotation) != _ANNOTATION_FIELDS:
            raise ProfileProposalEnvelopeV1Error("ANNOTATION_FIELDS_INVALID")
        target_type = _require_nonempty_string(
            annotation.get("target_type"), "ANNOTATION_TARGET_TYPE_REQUIRED"
        )
        if target_type not in ANNOTATION_TARGET_TYPES:
            raise ProfileProposalEnvelopeV1Error("ANNOTATION_TARGET_TYPE_INVALID")
        target_id = _require_nonempty_string(
            annotation.get("target_id"), "ANNOTATION_TARGET_ID_REQUIRED"
        )
        field = _require_nonempty_string(
            annotation.get("field"), "ANNOTATION_TARGET_FIELD_REQUIRED"
        )
        target = (target_type, target_id, field)
        if target not in expected_targets:
            raise ProfileProposalEnvelopeV1Error("ANNOTATION_TARGET_DANGLING_OR_NONCRITICAL")
        if target in seen_targets:
            raise ProfileProposalEnvelopeV1Error("DUPLICATE_ANNOTATION_TARGET")
        seen_targets.add(target)

        status = _require_nonempty_string(
            annotation.get("status"), "ANNOTATION_STATUS_REQUIRED"
        )
        if status not in ANNOTATION_STATUSES:
            raise ProfileProposalEnvelopeV1Error("ANNOTATION_STATUS_INVALID")
        core_signals_unknown = _contains_unknown_token(expected_targets[target])
        if status == "UNKNOWN" and not core_signals_unknown:
            raise ProfileProposalEnvelopeV1Error("UNKNOWN_STATUS_CORE_VALUE_MISMATCH")
        if core_signals_unknown and status not in _UNRESOLVED_STATUSES:
            raise ProfileProposalEnvelopeV1Error("KNOWN_STATUS_CORE_VALUE_MISMATCH")

        raw_pointers = annotation.get("evidence_pointers")
        if not isinstance(raw_pointers, list) or not raw_pointers:
            raise ProfileProposalEnvelopeV1Error("ANNOTATION_EVIDENCE_POINTERS_REQUIRED")
        pointers = [
            _validate_evidence_pointer(
                pointer,
                packet_sources=packet_sources,
                visible_packet=visible_packet,
            )
            for pointer in raw_pointers
        ]
        pointer_keys = {
            (pointer["pointer_type"], pointer["source_id"], pointer["value"])
            for pointer in pointers
        }
        if len(pointer_keys) != len(pointers):
            raise ProfileProposalEnvelopeV1Error("DUPLICATE_ANNOTATION_EVIDENCE_POINTER")
        if status == "CONFLICTING_SOURCES" and len(pointer_keys) < 2:
            raise ProfileProposalEnvelopeV1Error(
                "CONFLICTING_SOURCES_REQUIRES_MULTIPLE_POINTERS"
            )

        normalized.append(
            {
                "target_type": target_type,
                "target_id": target_id,
                "field": field,
                "status": status,
                "evidence_pointers": pointers,
                "confidence": _validate_confidence(annotation.get("confidence")),
            }
        )

    if seen_targets != set(expected_targets):
        raise ProfileProposalEnvelopeV1Error("CRITICAL_ANNOTATION_COVERAGE_INCOMPLETE")
    return normalized


def _diagnostic_summary(
    *, case_id: str, annotations: list[Mapping[str, Any]]
) -> dict[str, Any]:
    status_counts = Counter(annotation["status"] for annotation in annotations)
    target_counts = Counter(annotation["target_type"] for annotation in annotations)
    pointer_counts = Counter(
        pointer["pointer_type"]
        for annotation in annotations
        for pointer in annotation["evidence_pointers"]
    )
    return {
        "schema_version": "paper-blind-profile-annotation-diagnostic-summary/v1",
        "case_id": case_id,
        "coverage_status": "COMPLETE",
        "annotation_count": len(annotations),
        "status_counts": {
            status: status_counts.get(status, 0) for status in ANNOTATION_STATUSES
        },
        "target_counts": {
            target_type: target_counts.get(target_type, 0)
            for target_type in ANNOTATION_TARGET_TYPES
        },
        "evidence_pointer_count": sum(pointer_counts.values()),
        "evidence_pointer_type_counts": {
            pointer_type: pointer_counts.get(pointer_type, 0)
            for pointer_type in EVIDENCE_POINTER_TYPES
        },
        "routing_effect": "NONE_DIAGNOSTIC_ONLY",
        "scientific_authority": "NONE",
    }


def validate_profile_proposal_envelope(
    packet_path: str | Path, envelope: Mapping[str, Any]
) -> dict[str, Any]:
    """Admit the unchanged core and independently validate diagnostic annotations."""

    packet = load_public_packet(packet_path)
    visible_packet = build_agent_visible_packet(packet_path)
    core = extract_core_proposal(envelope)
    core_admission = validate_agent_proposal(packet_path, core)
    annotations = _validate_annotations(
        packet=packet,
        visible_packet=visible_packet,
        core=core,
        annotations=envelope["field_annotations"],
    )
    summary = _diagnostic_summary(case_id=core["case_id"], annotations=annotations)
    return {
        "schema_version": PROFILE_PROPOSAL_ENVELOPE_ADMISSION_SCHEMA,
        "proposal_status": "ADMISSIBLE_NONAUTHORITATIVE_WITH_DIAGNOSTIC_ANNOTATIONS",
        "core_admission": core_admission,
        "field_annotations": annotations,
        "diagnostic_summary": summary,
        "routing_input": {
            "kind": "EXISTING_CORE_ADMISSION_ONLY",
            "schema_version": core_admission["schema_version"],
            "proposal_status": core_admission["proposal_status"],
        },
        "boundary": (
            "Only core_admission may enter the existing deterministic Rules projection. "
            "field_annotations are diagnostic-only and confer no Rule, route, execution, "
            "scientific-disposition, or review authority."
        ),
    }


def build_profile_annotation_diagnostic_summary(
    packet_path: str | Path, envelope: Mapping[str, Any]
) -> dict[str, Any]:
    """Return the diagnostic summary only after full envelope validation."""

    return deepcopy(validate_profile_proposal_envelope(packet_path, envelope)["diagnostic_summary"])


__all__ = [
    "ANNOTATION_STATUSES",
    "ANNOTATION_TARGET_TYPES",
    "CORE_PROPOSAL_FIELDS",
    "EVIDENCE_POINTER_TYPES",
    "PACKET_POINTER_SOURCE_ID",
    "PROFILE_PROPOSAL_ENVELOPE_ADMISSION_SCHEMA",
    "PROFILE_PROPOSAL_ENVELOPE_SCHEMA",
    "ProfileProposalEnvelopeV1Error",
    "build_profile_annotation_diagnostic_summary",
    "build_profile_proposal_envelope_schema",
    "extract_core_proposal",
    "validate_profile_proposal_envelope",
]
