"""Validate public answer-blind preparation packets without selecting science.

This small module keeps three boundaries executable: public packet content,
frozen-asset identity, and a non-authoritative profiling proposal. It deliberately
does not create a RuleInstance, select a capability, parse numerical payloads, run
an Operator, or emit an evidence or scientific result.
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
_AGENT_OUTPUT_FIELDS = ["case_id", "proposed_source_ids", "unknowns", "rationale"]
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


def _validate_source_materials(value: Any) -> list[str]:
    if not isinstance(value, list) or not value:
        raise PaperBlindPublicPacketError("INVALID_SOURCE_MATERIALS")
    source_ids: list[str] = []
    for source in value:
        if not isinstance(source, Mapping) or set(source) != {
            "source_id",
            "source_kind",
            "source_locator",
            "permitted_facts",
            "excluded_sections",
        }:
            raise PaperBlindPublicPacketError("INVALID_SOURCE_MATERIAL")
        source_id = source.get("source_id")
        if not isinstance(source_id, str) or not source_id.strip():
            raise PaperBlindPublicPacketError("INVALID_SOURCE_ID")
        source_ids.append(source_id)
        for field in ("source_kind", "source_locator"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                raise PaperBlindPublicPacketError(f"INVALID_{field.upper()}")
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
            if not isinstance(asset[field], str) or not asset[field].strip():
                raise PaperBlindPublicPacketError("INVALID_DATA_ASSET")
        asset_ids.append(asset["asset_id"])
    if len(set(asset_ids)) != len(asset_ids):
        raise PaperBlindPublicPacketError("DUPLICATE_DATA_ASSET_ID")
    return asset_ids


def _validate_agent_proposal_schema(value: Any) -> None:
    if not isinstance(value, Mapping) or value != {
        "allowed_output_fields": _AGENT_OUTPUT_FIELDS
    }:
        raise PaperBlindPublicPacketError("INVALID_AGENT_PROPOSAL_SCHEMA")


def _validate_platform_authority_envelope(value: Any) -> None:
    if not isinstance(value, Mapping) or set(value) != {
        "execution_authorization",
        "scientific_disposition",
        "claim_boundary",
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
        if not isinstance(packet[field], str) or not packet[field].strip():
            raise PaperBlindPublicPacketError(f"INVALID_{field.upper()}")
    if packet["case_role"] not in {
        "EXPOSED_DEVELOPMENT",
        "EXPOSED_PORTABILITY_PREPARATION",
    }:
        raise PaperBlindPublicPacketError("UNAUTHORIZED_CASE_ROLE")
    _validate_source_materials(packet["source_materials"])
    _validate_data_assets(packet["data_assets"])
    _validate_agent_proposal_schema(packet["agent_proposal_schema"])
    _validate_platform_authority_envelope(packet["platform_authority_envelope"])
    hidden_boundary = packet["hidden_reference_boundary"]
    if not isinstance(hidden_boundary, Mapping) or hidden_boundary != {
        "status": "EXTERNAL_HUMAN_CURATED_REFERENCE_REQUIRED",
        "repository_visibility": "NOT_PRESENT_IN_PUBLIC_PACKET_OR_RUNTIME",
    }:
        raise PaperBlindPublicPacketError("INVALID_HIDDEN_REFERENCE_BOUNDARY")
    return dict(packet)


def build_agent_visible_packet(packet_path: str | Path) -> dict[str, Any]:
    """Return only scientific question/source/data/proposal-schema information."""

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


def validate_agent_proposal(packet_path: str | Path, proposal: Any) -> dict[str, Any]:
    """Admit a profiling proposal without assigning authority or an action."""

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
    proposed_sources = _string_list(
        proposal.get("proposed_source_ids"), label="PROPOSED_SOURCE_IDS", minimum=1
    )
    if not set(proposed_sources).issubset(allowed_sources):
        raise PaperBlindPublicPacketError("AGENT_PROPOSAL_UNKNOWN_SOURCE_ID")
    _string_list(proposal.get("unknowns"), label="UNKNOWNS", minimum=1)
    if not isinstance(proposal.get("rationale"), str) or not proposal["rationale"].strip():
        raise PaperBlindPublicPacketError("INVALID_RATIONALE")
    return {
        "schema_version": "paper-blind-agent-proposal-admission/v1",
        "proposal_status": "ADMISSIBLE_NONAUTHORITATIVE",
        "proposal": dict(proposal),
    }


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_declared_asset_hashes(packet_path: str | Path) -> dict[str, Any]:
    """Verify only the identity of assets listed by a public packet."""

    packet = load_public_packet(packet_path)
    manifest = _read_json(FROZEN_INPUT_MANIFEST_PATH)
    if not isinstance(manifest, Mapping) or manifest.get("schema_version") != "paper-blind-frozen-inputs/v1":
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
