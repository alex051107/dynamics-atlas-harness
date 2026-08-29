"""Public answer-blind packet admission for the exposed development capsule.

The module admits a Profiler's scientific *facts* as a non-authoritative proposal.
It keeps the agent-visible packet free of the sealed development reference, legal
action cards, execution authority, Rule identifiers, and claim ceiling. The
deterministic projection below can feed the current draft Rules evaluator, but it
does not select an action, emit an EvidenceResult, or make a scientific verdict.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "paper_blind_exposed_v1"
PUBLIC_ROOT = EVIDENCE_ROOT / "public"
FROZEN_INPUT_ROOT = EVIDENCE_ROOT / "frozen_inputs"
FROZEN_INPUT_MANIFEST_PATH = EVIDENCE_ROOT / "frozen_input_manifest_v1.json"

PUBLIC_PACKET_SCHEMA = "paper-blind-public-packet/v1"
_PUBLIC_PACKET_FIELDS = {
    "schema_version",
    "packet_id",
    "case_id",
    "case_role",
    "research_question",
    "source_materials",
    "data_assets",
    "agent_proposal_schema",
    "platform_authority_envelope",
    "hidden_reference_boundary",
}
_AGENT_OUTPUT_FIELDS = ["case_id", "proposed_case_facts", "unknowns", "rationale"]
_CASE_FACT_CONTRACT = {
    "case": [
        "scientific_claim",
        "requested_claim_level",
        "intended_use",
        "declared_request_scope",
        "forbidden_upgrades",
    ],
    "sources": [
        "source_id",
        "evidence_role",
        "construct_and_condition",
        "sample_composition",
        "native_observable",
        "estimand",
        "time_semantics",
        "spatial_support",
        "unit_or_aggregation",
    ],
    "edges": [
        "edge_id",
        "left_source_id",
        "right_source_id",
        "relation_type",
        "condition_relation",
        "bridge_status",
        "validation_independence",
        "shared_error_status",
    ],
}
_FORBIDDEN_PUBLIC_FIELD_NAMES = {
    "canonical_case_graph",
    "expected_rule_instances",
    "expected_rules",
    "expected_operator_route",
    "expected_route",
    "paper_reported_conclusion",
    "expert_bounded_conclusion",
    "hidden_gold",
    "gold",
    "development_card",
    "development_obligation_id",
    "rule_instance_id",
    "allowed_capability_ids",
    "capability_id",
}
_FORBIDDEN_PROPOSAL_FIELD_NAMES = _FORBIDDEN_PUBLIC_FIELD_NAMES | {
    "candidate_capability_ids",
    "execution_request",
    "execution_authorization",
    "operator_id",
    "scientific_conclusion",
    "scientific_disposition",
    "claim_boundary",
}
_ALLOWED_CASE_ROLES = {
    "EXPOSED_DEVELOPMENT",
    "EXPOSED_PORTABILITY_PREPARATION",
    "EXPOSED_PORTABILITY_DEVELOPMENT",
}
_ALLOWED_EVIDENCE_ROLES = {
    "CONSTRUCTION",
    "DIAGNOSTIC",
    "FIT_TARGET",
    "HELD_OUT_VALIDATION",
    "UNKNOWN",
}


class PaperBlindPublicPacketError(ValueError):
    """Raised when a public packet crosses its authority or identity boundary."""


def _read_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def _is_within(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError:
        return False
    return True


def _require_public_path(path: Path) -> Path:
    resolved = path.resolve()
    if not _is_within(resolved, PUBLIC_ROOT):
        raise PaperBlindPublicPacketError("PUBLIC_PACKET_MUST_BE_UNDER_PUBLIC_ROOT")
    if not resolved.is_file():
        raise PaperBlindPublicPacketError("PUBLIC_PACKET_NOT_FOUND")
    return resolved


def _reject_forbidden_fields(value: Any, *, forbidden: set[str], label: str) -> None:
    if isinstance(value, Mapping):
        for key, nested in value.items():
            if not isinstance(key, str):
                raise PaperBlindPublicPacketError(f"INVALID_FIELD_NAME:{label}")
            if key in forbidden:
                raise PaperBlindPublicPacketError(f"FORBIDDEN_FIELD:{key}")
            _reject_forbidden_fields(nested, forbidden=forbidden, label=key)
    elif isinstance(value, list):
        for item in value:
            _reject_forbidden_fields(item, forbidden=forbidden, label=label)


def _string_list(value: Any, *, label: str, minimum: int = 0) -> list[str]:
    if not isinstance(value, list) or len(value) < minimum:
        raise PaperBlindPublicPacketError(f"INVALID_{label}")
    result: list[str] = []
    for item in value:
        if not isinstance(item, str) or not item.strip():
            raise PaperBlindPublicPacketError(f"INVALID_{label}")
        result.append(item.strip())
    if len(set(result)) != len(result):
        raise PaperBlindPublicPacketError(f"DUPLICATE_{label}")
    return result


def _require_string(value: Any, *, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise PaperBlindPublicPacketError(f"INVALID_{label}")
    return value.strip()


def _validate_source_materials(value: Any) -> list[str]:
    if not isinstance(value, list) or not value:
        raise PaperBlindPublicPacketError("INVALID_SOURCE_MATERIALS")
    source_ids: list[str] = []
    expected_fields = {
        "source_id",
        "source_kind",
        "source_locator",
        "permitted_facts",
        "excluded_sections",
    }
    for source in value:
        if not isinstance(source, Mapping) or set(source) != expected_fields:
            raise PaperBlindPublicPacketError("INVALID_SOURCE_MATERIAL")
        source_id = _require_string(source.get("source_id"), label="SOURCE_ID")
        source_ids.append(source_id)
        _require_string(source.get("source_kind"), label="SOURCE_KIND")
        _require_string(source.get("source_locator"), label="SOURCE_LOCATOR")
        _string_list(source.get("permitted_facts"), label="PERMITTED_FACTS", minimum=1)
        excluded = _string_list(source.get("excluded_sections"), label="EXCLUDED_SECTIONS", minimum=2)
        if "Discussion" not in excluded or "Conclusion" not in excluded:
            raise PaperBlindPublicPacketError(
                "PUBLIC_PACKET_MUST_EXCLUDE_DISCUSSION_AND_CONCLUSION"
            )
    if len(set(source_ids)) != len(source_ids):
        raise PaperBlindPublicPacketError("DUPLICATE_SOURCE_ID")
    return source_ids


def _validate_data_assets(value: Any) -> list[str]:
    if not isinstance(value, list) or not value:
        raise PaperBlindPublicPacketError("INVALID_DATA_ASSETS")
    asset_ids: list[str] = []
    for asset in value:
        if not isinstance(asset, Mapping) or set(asset) != {
            "asset_id",
            "asset_kind",
            "public_description",
        }:
            raise PaperBlindPublicPacketError("INVALID_DATA_ASSET")
        for field in asset:
            _require_string(asset[field], label="DATA_ASSET")
        asset_ids.append(asset["asset_id"])
    if len(set(asset_ids)) != len(asset_ids):
        raise PaperBlindPublicPacketError("DUPLICATE_DATA_ASSET_ID")
    return asset_ids


def _agent_schema() -> dict[str, Any]:
    return {
        "allowed_output_fields": _AGENT_OUTPUT_FIELDS,
        "proposed_case_facts_contract": _CASE_FACT_CONTRACT,
    }


def _validate_agent_proposal_schema(value: Any) -> None:
    if not isinstance(value, Mapping) or dict(value) != _agent_schema():
        raise PaperBlindPublicPacketError("INVALID_AGENT_PROPOSAL_SCHEMA")


def _validate_platform_authority_envelope(value: Any) -> None:
    if not isinstance(value, Mapping) or set(value) != {
        "execution_authorization",
        "scientific_disposition",
        "claim_boundary",
        "rules_projection_authority",
    }:
        raise PaperBlindPublicPacketError("INVALID_PLATFORM_AUTHORITY_ENVELOPE")
    if value.get("execution_authorization") != "NO_EXECUTION":
        raise PaperBlindPublicPacketError("UNAUTHORIZED_EXECUTION_AUTHORITY")
    if value.get("scientific_disposition") != "NOT_EVALUATED":
        raise PaperBlindPublicPacketError("UNAUTHORIZED_SCIENTIFIC_DISPOSITION")
    boundary = value["claim_boundary"]
    if not isinstance(boundary, Mapping) or set(boundary) != {
        "allowed_descriptions",
        "forbidden_claims",
    }:
        raise PaperBlindPublicPacketError("INVALID_CLAIM_BOUNDARY")
    _string_list(boundary.get("allowed_descriptions"), label="ALLOWED_DESCRIPTIONS", minimum=1)
    _string_list(boundary.get("forbidden_claims"), label="FORBIDDEN_CLAIMS", minimum=1)
    _validate_rules_projection_authority(value["rules_projection_authority"])


def _validate_rules_projection_authority(value: Any) -> None:
    """Validate fixed, non-Agent inputs to the current Draft Rules projection."""

    if not isinstance(value, Mapping) or set(value) != {
        "case",
        "source_evidence_roles",
        "comparisons",
    }:
        raise PaperBlindPublicPacketError("INVALID_RULES_PROJECTION_AUTHORITY")
    case = value["case"]
    if not isinstance(case, Mapping) or set(case) != set(_CASE_FACT_CONTRACT["case"]):
        raise PaperBlindPublicPacketError("INVALID_RULES_PROJECTION_CASE_AUTHORITY")
    for field in ("scientific_claim", "requested_claim_level", "intended_use"):
        _require_string(case.get(field), label=f"RULES_PROJECTION_{field.upper()}")
    _string_list(case.get("declared_request_scope"), label="RULES_PROJECTION_SCOPE", minimum=1)
    _string_list(
        case.get("forbidden_upgrades"), label="RULES_PROJECTION_FORBIDDEN_UPGRADES", minimum=1
    )

    source_roles = value["source_evidence_roles"]
    if not isinstance(source_roles, Mapping) or not source_roles:
        raise PaperBlindPublicPacketError("INVALID_RULES_PROJECTION_SOURCE_ROLES")
    for source_id, role in source_roles.items():
        _require_string(source_id, label="RULES_PROJECTION_SOURCE_ID")
        if _require_string(role, label="RULES_PROJECTION_EVIDENCE_ROLE") not in _ALLOWED_EVIDENCE_ROLES:
            raise PaperBlindPublicPacketError("INVALID_RULES_PROJECTION_EVIDENCE_ROLE")

    comparisons = value["comparisons"]
    if not isinstance(comparisons, list) or not comparisons:
        raise PaperBlindPublicPacketError("INVALID_RULES_PROJECTION_COMPARISONS")
    endpoint_pairs: set[tuple[str, str]] = set()
    expected_fields = {
        "comparison_id",
        "left_source_id",
        "right_source_id",
        "condition_relation",
        "relation_type",
        "bridge_status",
        "validation_independence",
        "shared_error_status",
    }
    for comparison in comparisons:
        if not isinstance(comparison, Mapping) or set(comparison) != expected_fields:
            raise PaperBlindPublicPacketError("INVALID_RULES_PROJECTION_COMPARISON")
        _require_string(comparison.get("comparison_id"), label="RULES_PROJECTION_COMPARISON_ID")
        left = _require_string(
            comparison.get("left_source_id"), label="RULES_PROJECTION_LEFT_SOURCE"
        )
        right = _require_string(
            comparison.get("right_source_id"), label="RULES_PROJECTION_RIGHT_SOURCE"
        )
        if left == right:
            raise PaperBlindPublicPacketError("INVALID_RULES_PROJECTION_COMPARISON_ENDPOINTS")
        pair = tuple(sorted((left, right)))
        if pair in endpoint_pairs:
            raise PaperBlindPublicPacketError("DUPLICATE_RULES_PROJECTION_ENDPOINT_PAIR")
        endpoint_pairs.add(pair)
        for field in expected_fields - {"comparison_id", "left_source_id", "right_source_id"}:
            _require_string(comparison.get(field), label=f"RULES_PROJECTION_{field.upper()}")


def _rules_projection_authority(packet: Mapping[str, Any]) -> dict[str, Any]:
    """Return runtime-owned Rule fields that are deliberately absent from Agent input."""

    envelope = packet.get("platform_authority_envelope")
    if not isinstance(envelope, Mapping):
        raise PaperBlindPublicPacketError("INVALID_PLATFORM_AUTHORITY_ENVELOPE")
    authority = envelope.get("rules_projection_authority")
    _validate_rules_projection_authority(authority)
    assert isinstance(authority, Mapping)

    public_source_ids = {item["source_id"] for item in packet["source_materials"]}
    roles = authority["source_evidence_roles"]
    assert isinstance(roles, Mapping)
    if set(roles) != public_source_ids:
        raise PaperBlindPublicPacketError("RULES_PROJECTION_SOURCE_ROLES_DO_NOT_MATCH_PACKET")
    comparisons = authority["comparisons"]
    assert isinstance(comparisons, list)
    for comparison in comparisons:
        if (
            comparison["left_source_id"] not in public_source_ids
            or comparison["right_source_id"] not in public_source_ids
        ):
            raise PaperBlindPublicPacketError("RULES_PROJECTION_COMPARISON_SOURCE_NOT_IN_PACKET")
    return {
        "case": dict(authority["case"]),
        "source_evidence_roles": dict(roles),
        "comparisons": [dict(item) for item in comparisons],
    }


def _validate_hidden_reference_boundary(value: Any) -> None:
    expected = {
        "status": "DEVELOPMENT_REFERENCE_DRAFT_NOT_HUMAN_APPROVED",
        "repository_visibility": "SEALED_NON_AGENT_INPUT",
    }
    if not isinstance(value, Mapping) or dict(value) != expected:
        raise PaperBlindPublicPacketError("INVALID_HIDDEN_REFERENCE_BOUNDARY")


def load_public_packet(packet_path: str | Path) -> dict[str, Any]:
    """Load one public packet without parsing its scientific data payload."""

    path = _require_public_path(Path(packet_path))
    packet = _read_json(path)
    if not isinstance(packet, Mapping):
        raise PaperBlindPublicPacketError("PUBLIC_PACKET_MUST_BE_OBJECT")
    _reject_forbidden_fields(packet, forbidden=_FORBIDDEN_PUBLIC_FIELD_NAMES, label="packet")
    if set(packet) != _PUBLIC_PACKET_FIELDS:
        raise PaperBlindPublicPacketError("PUBLIC_PACKET_FIELDS_DO_NOT_MATCH_V1")
    if packet["schema_version"] != PUBLIC_PACKET_SCHEMA:
        raise PaperBlindPublicPacketError("UNEXPECTED_PUBLIC_PACKET_SCHEMA")
    for field in ("packet_id", "case_id", "case_role", "research_question"):
        _require_string(packet[field], label=field.upper())
    if packet["case_role"] not in _ALLOWED_CASE_ROLES:
        raise PaperBlindPublicPacketError("UNAUTHORIZED_CASE_ROLE")
    _validate_source_materials(packet["source_materials"])
    _validate_data_assets(packet["data_assets"])
    _validate_agent_proposal_schema(packet["agent_proposal_schema"])
    _validate_platform_authority_envelope(packet["platform_authority_envelope"])
    _validate_hidden_reference_boundary(packet["hidden_reference_boundary"])
    return dict(packet)


def build_agent_visible_packet(packet_path: str | Path) -> dict[str, Any]:
    """Return only question, public source/data material, and a fact-only schema."""

    packet = load_public_packet(packet_path)
    return {
        "schema_version": "paper-blind-agent-visible-input/v1",
        "packet_id": packet["packet_id"],
        "case_id": packet["case_id"],
        "research_question": packet["research_question"],
        "source_materials": packet["source_materials"],
        "data_assets": packet["data_assets"],
        "agent_proposal_schema": packet["agent_proposal_schema"],
    }


def _validate_proposed_case_facts(
    value: Any, *, allowed_source_ids: set[str]
) -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != set(_CASE_FACT_CONTRACT):
        raise PaperBlindPublicPacketError("INVALID_PROPOSED_CASE_FACTS")
    case = value.get("case")
    if not isinstance(case, Mapping) or set(case) != set(_CASE_FACT_CONTRACT["case"]):
        raise PaperBlindPublicPacketError("INVALID_PROPOSED_CASE_FACTS_CASE")
    for field in ("scientific_claim", "requested_claim_level", "intended_use"):
        _require_string(case.get(field), label=f"PROPOSED_CASE_{field.upper()}")
    _string_list(case.get("declared_request_scope"), label="DECLARED_REQUEST_SCOPE", minimum=1)
    _string_list(case.get("forbidden_upgrades"), label="FORBIDDEN_UPGRADES", minimum=1)

    sources = value.get("sources")
    if not isinstance(sources, list) or not sources:
        raise PaperBlindPublicPacketError("INVALID_PROPOSED_CASE_FACTS_SOURCES")
    source_ids: list[str] = []
    for source in sources:
        if not isinstance(source, Mapping) or set(source) != set(_CASE_FACT_CONTRACT["sources"]):
            raise PaperBlindPublicPacketError("INVALID_PROPOSED_CASE_FACT_SOURCE")
        source_id = _require_string(source.get("source_id"), label="PROPOSED_SOURCE_ID")
        if source_id not in allowed_source_ids:
            raise PaperBlindPublicPacketError("AGENT_PROPOSAL_UNKNOWN_SOURCE_ID")
        source_ids.append(source_id)
        evidence_role = _require_string(source.get("evidence_role"), label="PROPOSED_EVIDENCE_ROLE")
        if evidence_role not in _ALLOWED_EVIDENCE_ROLES:
            raise PaperBlindPublicPacketError("INVALID_PROPOSED_EVIDENCE_ROLE")
        for field in (
            "construct_and_condition",
            "sample_composition",
            "native_observable",
            "estimand",
            "spatial_support",
            "unit_or_aggregation",
        ):
            _require_string(source.get(field), label=f"PROPOSED_{field.upper()}")
        time_semantics = source.get("time_semantics")
        if not isinstance(time_semantics, Mapping) or set(time_semantics) != {"kind"}:
            raise PaperBlindPublicPacketError("INVALID_PROPOSED_TIME_SEMANTICS")
        _require_string(time_semantics.get("kind"), label="PROPOSED_TIME_SEMANTICS_KIND")
    if len(set(source_ids)) != len(source_ids):
        raise PaperBlindPublicPacketError("DUPLICATE_PROPOSED_SOURCE_ID")

    edges = value.get("edges")
    if not isinstance(edges, list) or not edges:
        raise PaperBlindPublicPacketError("INVALID_PROPOSED_CASE_FACTS_EDGES")
    edge_ids: list[str] = []
    source_id_set = set(source_ids)
    for edge in edges:
        if not isinstance(edge, Mapping) or set(edge) != set(_CASE_FACT_CONTRACT["edges"]):
            raise PaperBlindPublicPacketError("INVALID_PROPOSED_CASE_FACT_EDGE")
        edge_id = _require_string(edge.get("edge_id"), label="PROPOSED_EDGE_ID")
        edge_ids.append(edge_id)
        left = _require_string(edge.get("left_source_id"), label="PROPOSED_EDGE_LEFT_SOURCE")
        right = _require_string(edge.get("right_source_id"), label="PROPOSED_EDGE_RIGHT_SOURCE")
        if left not in source_id_set or right not in source_id_set or left == right:
            raise PaperBlindPublicPacketError("INVALID_PROPOSED_EDGE_SOURCE_LINK")
        for field in (
            "relation_type",
            "condition_relation",
            "bridge_status",
            "validation_independence",
            "shared_error_status",
        ):
            _require_string(edge.get(field), label=f"PROPOSED_{field.upper()}")
    if len(set(edge_ids)) != len(edge_ids):
        raise PaperBlindPublicPacketError("DUPLICATE_PROPOSED_EDGE_ID")
    endpoint_pairs = [tuple(sorted((edge["left_source_id"], edge["right_source_id"]))) for edge in edges]
    if len(set(endpoint_pairs)) != len(endpoint_pairs):
        raise PaperBlindPublicPacketError("DUPLICATE_PROPOSED_EDGE_ENDPOINT_PAIR")
    return {
        "case": dict(case),
        "sources": [dict(source) for source in sources],
        "edges": [dict(edge) for edge in edges],
    }


def validate_agent_proposal(packet_path: str | Path, proposal: Any) -> dict[str, Any]:
    """Admit one fact-only profiling proposal without assigning any authority."""

    packet = load_public_packet(packet_path)
    if not isinstance(proposal, Mapping):
        raise PaperBlindPublicPacketError("AGENT_PROPOSAL_MUST_BE_OBJECT")
    _reject_forbidden_fields(
        proposal, forbidden=_FORBIDDEN_PROPOSAL_FIELD_NAMES, label="proposal"
    )
    if set(proposal) != set(_AGENT_OUTPUT_FIELDS):
        raise PaperBlindPublicPacketError("AGENT_PROPOSAL_FIELDS_DO_NOT_MATCH_PUBLIC_CONTRACT")
    if proposal.get("case_id") != packet["case_id"]:
        raise PaperBlindPublicPacketError("AGENT_PROPOSAL_CASE_ID_MISMATCH")
    allowed_sources = {source["source_id"] for source in packet["source_materials"]}
    facts = _validate_proposed_case_facts(
        proposal.get("proposed_case_facts"), allowed_source_ids=allowed_sources
    )
    authority = _rules_projection_authority(packet)
    proposed_pairs = {
        tuple(sorted((edge["left_source_id"], edge["right_source_id"]))) for edge in facts["edges"]
    }
    authorized_pairs = {
        tuple(sorted((edge["left_source_id"], edge["right_source_id"])))
        for edge in authority["comparisons"]
    }
    if proposed_pairs != authorized_pairs:
        raise PaperBlindPublicPacketError("AGENT_PROPOSAL_EDGE_ENDPOINTS_DO_NOT_MATCH_PACKET")
    _string_list(proposal.get("unknowns"), label="UNKNOWNS", minimum=1)
    _require_string(proposal.get("rationale"), label="RATIONALE")
    return {
        "schema_version": "paper-blind-agent-proposal-admission/v1",
        "proposal_status": "ADMISSIBLE_NONAUTHORITATIVE",
        "proposal": {
            "case_id": packet["case_id"],
            "proposed_case_facts": facts,
            "unknowns": list(proposal["unknowns"]),
            "rationale": proposal["rationale"].strip(),
        },
    }


def _declared_or_unknown(*values: str) -> str:
    return "UNKNOWN" if any(value == "UNKNOWN" for value in values) else "DECLARED"


def project_admitted_proposal_to_rules_casegraph(
    packet_path: str | Path, admitted_proposal: Mapping[str, Any]
) -> dict[str, Any]:
    """Create a deterministic draft Rules projection from an admitted fact proposal.

    The derived `DECLARED` labels mean only that a public-packet fact was supplied;
    they are not Agent-assigned scientific verification or source-science approval.
    """

    packet = load_public_packet(packet_path)
    if not isinstance(admitted_proposal, Mapping):
        raise PaperBlindPublicPacketError("ADMITTED_PROPOSAL_MUST_BE_OBJECT")
    if admitted_proposal.get("proposal_status") != "ADMISSIBLE_NONAUTHORITATIVE":
        raise PaperBlindPublicPacketError("ADMITTED_PROPOSAL_STATUS_INVALID")
    proposal = admitted_proposal.get("proposal")
    if not isinstance(proposal, Mapping) or proposal.get("case_id") != packet["case_id"]:
        raise PaperBlindPublicPacketError("ADMITTED_PROPOSAL_CASE_ID_INVALID")
    facts = _validate_proposed_case_facts(
        proposal.get("proposed_case_facts"),
        allowed_source_ids={source["source_id"] for source in packet["source_materials"]},
    )
    authority = _rules_projection_authority(packet)
    case_facts = authority["case"]
    evidence_items: list[dict[str, Any]] = []
    for source in facts["sources"]:
        source_values = [source["construct_and_condition"], source["sample_composition"]]
        measurement_values = [
            source["native_observable"],
            source["estimand"],
            source["time_semantics"]["kind"],
            source["spatial_support"],
            source["unit_or_aggregation"],
        ]
        evidence_items.append(
            {
                "source_id": source["source_id"],
                "case_evidence_scope": "CLAIM_EVIDENCE",
                "evidence_role": authority["source_evidence_roles"][source["source_id"]],
                "source_locator": next(
                    item["source_locator"]
                    for item in packet["source_materials"]
                    if item["source_id"] == source["source_id"]
                ),
                "data_lineage_status": "AGENT_PROPOSED_UNVERIFIED",
                "construct_and_condition": source["construct_and_condition"],
                "sample_composition": source["sample_composition"],
                "sample_system_composition_declaration_status": _declared_or_unknown(
                    *source_values
                ),
                "native_observable": source["native_observable"],
                "estimand": source["estimand"],
                "time_semantics": dict(source["time_semantics"]),
                "spatial_support": source["spatial_support"],
                "unit_or_aggregation": source["unit_or_aggregation"],
                "native_measurement_declaration_status": _declared_or_unknown(
                    *measurement_values
                ),
            }
        )
    comparisons = [
        {
            "comparison_id": edge["comparison_id"],
            "left_source_id": edge["left_source_id"],
            "right_source_id": edge["right_source_id"],
            "shared_claim": case_facts["scientific_claim"],
            "validation_claim": "No validation claim is emitted by a development profiling proposal.",
            "condition_relation": edge["condition_relation"],
            "relation_type": edge["relation_type"],
            "bridge_status": edge["bridge_status"],
            "validation_independence": edge["validation_independence"],
            "shared_error_status": edge["shared_error_status"],
            "data_lineage_status": "PLATFORM_DECLARED_PUBLIC_PACKET_CONTRACT",
        }
        for edge in authority["comparisons"]
    ]
    return {
        "case": {
            "case_id": packet["case_id"],
            "intake_kind": "SCIENTIFIC_CLAIM_REVIEW",
            "scientific_claim": case_facts["scientific_claim"],
            "requested_claim_level": case_facts["requested_claim_level"],
            "intended_use": case_facts["intended_use"],
            "observability_target": {
                "event_signature": "Answer-blind public-packet fact proposal",
                "target_time_scale": "Source-declared or UNKNOWN",
                "target_spatial_scale": "Source-declared or UNKNOWN",
            },
            "claim_contract": {
                "internal_consistency": "CONSISTENT",
                "declared_request_scope": list(case_facts["declared_request_scope"]),
                "forbidden_upgrades": list(case_facts["forbidden_upgrades"]),
            },
        },
        "evidence_items": evidence_items,
        "comparisons": comparisons,
        "projection_boundary": (
            "Agent-proposed factual fields are evaluated as unverified Draft inputs. "
            "Case claim, evidence roles, comparison identities, and comparison semantics "
            "come only from the platform-owned public-packet contract."
        ),
    }


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_declared_asset_hashes(packet_path: str | Path) -> dict[str, Any]:
    """Verify only identities of frozen assets declared by a public packet."""

    packet = load_public_packet(packet_path)
    manifest = _read_json(FROZEN_INPUT_MANIFEST_PATH)
    if (
        not isinstance(manifest, Mapping)
        or manifest.get("schema_version") != "paper-blind-frozen-inputs/v1"
    ):
        raise PaperBlindPublicPacketError("INVALID_FROZEN_INPUT_MANIFEST")
    manifest_assets = manifest.get("assets")
    if not isinstance(manifest_assets, Mapping):
        raise PaperBlindPublicPacketError("INVALID_FROZEN_INPUT_MANIFEST")

    verified_asset_ids: list[str] = []
    for asset_id in _validate_data_assets(packet["data_assets"]):
        manifest_asset = manifest_assets.get(asset_id)
        if not isinstance(manifest_asset, Mapping) or set(manifest_asset) != {
            "relative_path",
            "sha256",
            "source_record",
            "extraction_boundary",
        }:
            raise PaperBlindPublicPacketError("INVALID_FROZEN_INPUT_ASSET")
        relative_path = manifest_asset["relative_path"]
        expected_hash = manifest_asset["sha256"]
        if not isinstance(relative_path, str) or not relative_path:
            raise PaperBlindPublicPacketError("INVALID_FROZEN_INPUT_PATH")
        if not isinstance(expected_hash, str) or len(expected_hash) != 64:
            raise PaperBlindPublicPacketError("INVALID_FROZEN_INPUT_HASH")
        asset_path = (FROZEN_INPUT_ROOT / relative_path).resolve()
        if not _is_within(asset_path, FROZEN_INPUT_ROOT) or not asset_path.is_file():
            raise PaperBlindPublicPacketError("FROZEN_INPUT_NOT_FOUND")
        if _sha256(asset_path) != expected_hash:
            raise PaperBlindPublicPacketError("FROZEN_INPUT_HASH_MISMATCH")
        verified_asset_ids.append(asset_id)

    return {
        "schema_version": "paper-blind-frozen-asset-verification/v1",
        "packet_id": packet["packet_id"],
        "case_id": packet["case_id"],
        "verified_asset_ids": verified_asset_ids,
        "verification_scope": "IDENTITY_AND_PUBLIC_PACKET_BOUNDARY_ONLY",
    }
