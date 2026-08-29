"""Bounded two-case development integration capsule.

The capsule is a fixed integration, not a workflow engine.  It materializes
Planner-visible cards from fresh active Draft Rule results plus declared non-Rule
development items, validates a non-authoritative recorded selection or abstention,
and executes only the selected public development action.  The pre-existing exact
HSP90 F04R02 closure is a separately labelled regression sidecar, not a closure of
the broad public HSP90 case.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Callable, Mapping, Sequence
from pathlib import Path
from typing import Any

from .paper_blind_exposed_v1 import (
    FROZEN_INPUT_MANIFEST_PATH,
    FROZEN_INPUT_ROOT,
    build_agent_visible_packet,
    project_admitted_proposal_to_rules_casegraph,
    validate_agent_proposal,
    verify_declared_asset_hashes,
)
from .real_case_vertical_slice_v1 import (
    HSP90_CASE_ID,
    HSP90_RUNTIME_SUBRULE_ID,
    HSP90_SOURCE_ID,
    load_rules_v1_bundle,
    run_hsp90_reference_demo_route,
)
from .registered_operators import load_registered_operator_registry
from .rules_prototype_v1 import evaluate_active_rules
from .sampling_diagnostics_v1 import run_grouped_observable_sampling_diagnostics
from .structural_state_projection_v1 import run_reference_relative_structural_projection


REPO_ROOT = Path(__file__).resolve().parents[2]
EVIDENCE_ROOT = REPO_ROOT / "evidence" / "paper_blind_exposed_v1"
PUBLIC_ROOT = EVIDENCE_ROOT / "public"
SEALED_REFERENCE_ROOT = EVIDENCE_ROOT / "sealed_references"
AGENT_RUN_ROOT = EVIDENCE_ROOT / "agent_runs"
RULES_ROOT = REPO_ROOT / "registries" / "rules_v1"
EXACT_HSP90_EVIDENCE_ROOT = REPO_ROOT / "evidence" / "real_case_vertical_slice_v1"
OPERATOR_REGISTRY_PATH = REPO_ROOT / "config" / "registered_operators.json"

HSP90_PUBLIC_CASE_ID = "HSP90_NTD_EXPOSED_PAPER_BLIND_V1"
ADK_PUBLIC_CASE_ID = "ADK_EXPOSED_PORTABILITY_V1"
HSP90_EXACT_CONTROL_RULE_INSTANCE_ID = (
    f"{HSP90_RUNTIME_SUBRULE_ID}::SOURCE::{HSP90_SOURCE_ID}"
)

_CASE_SPECS: dict[str, dict[str, Any]] = {
    HSP90_PUBLIC_CASE_ID: {
        "slug": "hsp90",
        "packet": PUBLIC_ROOT / "hsp90_public_packet_v1.json",
        "profiler_proposal": AGENT_RUN_ROOT / "profiler" / "hsp90_proposal.json",
        "planner_proposal": AGENT_RUN_ROOT / "planner" / "hsp90_proposal.json",
        "sealed_reference": SEALED_REFERENCE_ROOT / "hsp90_development_reference_draft_v1.json",
    },
    ADK_PUBLIC_CASE_ID: {
        "slug": "adk",
        "packet": PUBLIC_ROOT / "adk_public_packet_v1.json",
        "profiler_proposal": AGENT_RUN_ROOT / "profiler" / "adk_proposal.json",
        "planner_proposal": AGENT_RUN_ROOT / "planner" / "adk_proposal.json",
        "sealed_reference": SEALED_REFERENCE_ROOT / "adk_development_reference_draft_v1.json",
    },
}

# These two cards are fixed to this capsule. They are not a generic registry.
_ACTION_CARD_SPECS: tuple[dict[str, Any], ...] = (
    {
        "card_id": "HSP90_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION_V1",
        "case_id": HSP90_PUBLIC_CASE_ID,
        "addresses_ref": "HSP90_DEV_OBL_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION",
        "action_kind": "DESCRIPTIVE_ANALYSIS_ONLY",
        "required_asset_ids": (
            "HSP90_CA46_CA60_DISTANCE_40X1021",
            "HSP90_TRAJECTORY_GROUP_MANIFEST",
        ),
        "prerequisites": (
            "The frozen observable matrix and trajectory/group manifest are identity-verified.",
        ),
        "prohibitions": (
            "No active RuleResult update.",
            "No global-equilibration, population, rate, free-energy, mechanism, or mutation-effect claim.",
        ),
    },
    {
        "card_id": "ADK_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION_V1",
        "case_id": ADK_PUBLIC_CASE_ID,
        "addresses_ref": "ADK_DEV_OBL_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION",
        "action_kind": "DESCRIPTIVE_ANALYSIS_ONLY",
        "required_asset_ids": (
            "ADK_1AKE_CHAIN_A_CA",
            "ADK_4AKE_CHAIN_A_CA",
            "ADK_1E4V_G10V_CHAIN_A_CA",
        ),
        "prerequisites": (
            "The frozen non-reference sample and both reference coordinate arrays are identity-verified.",
        ),
        "prohibitions": (
            "No active RuleResult update.",
            "No wild-type equivalence, dynamics, population, kinetics, pathway, energy, mechanism, or portability claim.",
        ),
    },
)

_FORBIDDEN_AGENT_VISIBLE_TERMS = (
    "sealed_reference",
    "development_reference",
    "claim_boundary",
    "platform_authority_envelope",
    "allowed_capability_ids",
    "operator_id",
    "scientific_disposition",
)
_GAP_TYPES = {
    "SOURCE_FACT_MISSING",
    "COMPUTABLE_EVIDENCE_MISSING",
    "METHOD_OR_FORWARD_BRIDGE_MISSING",
    "EVALUATION_CONTRACT_OR_RULE_LIFECYCLE_PENDING",
    "NEW_DATA_REQUIRED",
    "HUMAN_SCIENTIFIC_JUDGMENT",
    "RULE_COVERAGE_GAP",
}


class ExposedPaperBlindCapsuleError(ValueError):
    """Raised when the capped capsule loses a causal or authority boundary."""


def _read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ExposedPaperBlindCapsuleError(f"JSON_UNREADABLE:{path}") from error
    if not isinstance(value, dict):
        raise ExposedPaperBlindCapsuleError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def _write_json(path: Path, value: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _require_mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ExposedPaperBlindCapsuleError(f"MAPPING_REQUIRED:{label}")
    return value


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ExposedPaperBlindCapsuleError(f"NONEMPTY_STRING_REQUIRED:{label}")
    return value.strip()


def _string_list(value: Any, label: str, *, allow_empty: bool) -> list[str]:
    if not isinstance(value, list) or (not allow_empty and not value):
        raise ExposedPaperBlindCapsuleError(f"STRING_LIST_REQUIRED:{label}")
    result = [_require_string(item, label) for item in value]
    if len(set(result)) != len(result):
        raise ExposedPaperBlindCapsuleError(f"DUPLICATE_VALUES:{label}")
    return result


def _reference_as_non_authoritative_proposal(reference: Mapping[str, Any]) -> dict[str, Any]:
    facts = _require_mapping(reference.get("reference_case_facts"), "reference_case_facts")
    return {
        "case_id": _require_string(reference.get("case_id"), "reference.case_id"),
        "proposed_case_facts": dict(facts),
        "unknowns": [
            "This development reference draft is not a named human source-science review."
        ],
        "rationale": "Non-authoritative sealed development reference used only after recorded-proposal replay.",
    }


def _validate_sealed_reference(reference: Mapping[str, Any], *, case_id: str) -> None:
    required = {
        "reference_id",
        "reference_status",
        "case_id",
        "visibility_contract",
        "PaperReportedConclusionDraft",
        "ExpertBoundedConclusionDraft",
        "reference_case_facts",
        "expected_family_scope",
        "expected_unresolved_development_obligations",
        "acceptable_evidence_actions",
        "allowed_claims",
        "forbidden_claims",
        "acceptable_next_actions",
    }
    if set(reference) != required:
        raise ExposedPaperBlindCapsuleError("SEALED_REFERENCE_FIELDS_INVALID")
    if reference.get("reference_status") != "DEVELOPMENT_REFERENCE_DRAFT_NOT_HUMAN_APPROVED":
        raise ExposedPaperBlindCapsuleError("SEALED_REFERENCE_STATUS_INVALID")
    if reference.get("case_id") != case_id:
        raise ExposedPaperBlindCapsuleError("SEALED_REFERENCE_CASE_ID_MISMATCH")
    visibility = _require_mapping(reference.get("visibility_contract"), "visibility_contract")
    if visibility.get("agent_visible_input") is not False or visibility.get("runtime_authority") is not False:
        raise ExposedPaperBlindCapsuleError("SEALED_REFERENCE_AUTHORITY_LEAK")


def _assert_agent_visible_boundary(value: Mapping[str, Any]) -> None:
    serial = json.dumps(value, sort_keys=True).lower()
    for term in _FORBIDDEN_AGENT_VISIBLE_TERMS:
        if term in serial:
            raise ExposedPaperBlindCapsuleError(f"AGENT_VISIBLE_AUTHORITY_LEAK:{term}")


def _active_rule_results_for_proposal(
    *, packet_path: Path, proposal: Mapping[str, Any], rules_bundle: Mapping[str, Any]
) -> dict[str, Any]:
    admitted = validate_agent_proposal(packet_path, proposal)
    case_graph = project_admitted_proposal_to_rules_casegraph(packet_path, admitted)
    return {
        "admission": admitted,
        "projected_casegraph": case_graph,
        "rule_results": evaluate_active_rules(case_graph=case_graph, **rules_bundle),
    }


def _result_inventory(results: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "rule_instance_id": item["rule_instance_id"],
            "runtime_subrule_id": item["runtime_subrule_id"],
            "target": dict(item["target"]),
            "status": item["status"],
            "reason_codes": list(item["reason_codes"]),
        }
        for item in results
    ]


def _active_gap_type(item: Mapping[str, Any]) -> str:
    reasons = {code for code in item.get("reason_codes", []) if isinstance(code, str)}
    if "NO_EXPLICIT_CONTRACT_OUTCOME" in reasons:
        return "EVALUATION_CONTRACT_OR_RULE_LIFECYCLE_PENDING"
    source_prefixes = (
        "SAMPLE_SYSTEM",
        "COMPOSITION",
        "NATIVE_MEASUREMENT",
        "ESTIMAND",
        "TIME_SEMANTICS",
        "SPATIAL_SUPPORT",
        "UNIT_OR_AGGREGATION",
        "SOURCE_",
    )
    if any(code.startswith(source_prefixes) for code in reasons):
        return "SOURCE_FACT_MISSING"
    if any("CONDITION" in code or "COMPAR" in code or "BRIDGE" in code for code in reasons):
        return "METHOD_OR_FORWARD_BRIDGE_MISSING"
    return "HUMAN_SCIENTIFIC_JUDGMENT"


def _development_item(
    *, ref: str, gap_type: str, claim_effect: str, reason_codes: Sequence[str]
) -> dict[str, Any]:
    if gap_type not in _GAP_TYPES:
        raise ExposedPaperBlindCapsuleError("UNKNOWN_GAP_TYPE")
    return {
        "kind": "DEVELOPMENT_OBLIGATION",
        "development_obligation_ref": ref,
        "gap_type": gap_type,
        "reason_codes": list(reason_codes),
        "source": {"kind": "DECLARED_NONRULE_DEVELOPMENT_ITEM", "development_obligation_ref": ref},
        "claim_effect": claim_effect,
    }


def _development_obligations(
    case_id: str, rule_results: Sequence[Mapping[str, Any]]
) -> list[dict[str, Any]]:
    """Classify fresh unresolved rules and declared non-Rule items without upgrading either."""

    active = []
    for result in rule_results:
        if result.get("status") != "UNRESOLVED":
            continue
        rule_instance_id = _require_string(result.get("rule_instance_id"), "rule_instance_id")
        active.append(
            {
                "kind": "ACTIVE_RULE_INSTANCE",
                "rule_instance_id": rule_instance_id,
                "runtime_subrule_id": _require_string(
                    result.get("runtime_subrule_id"), "runtime_subrule_id"
                ),
                "target": dict(_require_mapping(result.get("target"), "active_rule.target")),
                "gap_type": _active_gap_type(result),
                "reason_codes": list(result.get("reason_codes", [])),
                "source": {"kind": "FRESH_ACTIVE_RULE_RESULT", "rule_instance_id": rule_instance_id},
                "claim_effect": "Active Draft Rule remains unresolved; no scientific conclusion is emitted.",
            }
        )
    if case_id == HSP90_PUBLIC_CASE_ID:
        additions = [
            _development_item(
                ref="HSP90_DEV_OBL_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION",
                gap_type="COMPUTABLE_EVIDENCE_MISSING",
                reason_codes=["DESCRIPTIVE_CAPABILITY_ONLY"],
                claim_effect="A descriptive observable-dependence result may be recorded; no active RuleResult or scientific disposition changes.",
            ),
            _development_item(
                ref="HSP90_DEV_OBL_NMR_MD_FORWARD_BRIDGE",
                gap_type="METHOD_OR_FORWARD_BRIDGE_MISSING",
                reason_codes=["FORWARD_BRIDGE_NOT_REVIEWED"],
                claim_effect="The NMR-to-MD relation remains unresolved until a reviewed method or forward bridge is available.",
            ),
            _development_item(
                ref="HSP90_DEV_OBL_SOURCE_SCIENCE_REVIEW",
                gap_type="HUMAN_SCIENTIFIC_JUDGMENT",
                reason_codes=["PENDING_DOMAIN_REVIEW"],
                claim_effect="Named source-science review remains required for scientific interpretation.",
            ),
            _development_item(
                ref="HSP90_DEV_OBL_CANDIDATE_F04_F05_F07_LIFECYCLE",
                gap_type="EVALUATION_CONTRACT_OR_RULE_LIFECYCLE_PENDING",
                reason_codes=["CANDIDATE_ONLY_FAMILY_NOT_ACTIVE"],
                claim_effect="Candidate-only F04/F05/F07 concerns remain non-Rule lifecycle items until a reviewed evaluation contract exists.",
            ),
        ]
    elif case_id == ADK_PUBLIC_CASE_ID:
        additions = [
            _development_item(
                ref="ADK_DEV_OBL_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION",
                gap_type="COMPUTABLE_EVIDENCE_MISSING",
                reason_codes=["DESCRIPTIVE_CAPABILITY_ONLY"],
                claim_effect="A static reference-relative geometry result may be recorded; no active RuleResult or scientific disposition changes.",
            ),
            _development_item(
                ref="ADK_DEV_OBL_DYNAMIC_COVERAGE",
                gap_type="NEW_DATA_REQUIRED",
                reason_codes=["NONREFERENCE_SAMPLE_IS_STATIC"],
                claim_effect="A trajectory, ensemble, or other dynamic sample is required before dynamical coverage can be assessed.",
            ),
            _development_item(
                ref="ADK_DEV_OBL_SOURCE_SCIENCE_REVIEW",
                gap_type="HUMAN_SCIENTIFIC_JUDGMENT",
                reason_codes=["PENDING_DOMAIN_REVIEW"],
                claim_effect="Named source-science review remains required for biological interpretation.",
            ),
            _development_item(
                ref="ADK_DEV_OBL_CANDIDATE_F05_F07_LIFECYCLE",
                gap_type="EVALUATION_CONTRACT_OR_RULE_LIFECYCLE_PENDING",
                reason_codes=["CANDIDATE_ONLY_FAMILY_NOT_ACTIVE"],
                claim_effect="Candidate-only representation and identifiability concerns remain non-Rule lifecycle items until a reviewed evaluation contract exists.",
            ),
        ]
    else:
        raise ExposedPaperBlindCapsuleError("UNSUPPORTED_CAPSULE_CASE")
    return sorted(active + additions, key=_item_ref)


def _item_ref(item: Mapping[str, Any]) -> str:
    return _require_string(
        item.get("rule_instance_id", item.get("development_obligation_ref")), "unresolved_item_ref"
    )


def _verified_asset_ids(asset_verification: Mapping[str, Any]) -> set[str]:
    value = asset_verification.get("verified_asset_ids")
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ExposedPaperBlindCapsuleError("ASSET_VERIFICATION_IDS_INVALID")
    return set(value)


def materialize_planner_input(
    *,
    case_id: str,
    active_rule_results: Sequence[Mapping[str, Any]],
    development_items: Sequence[Mapping[str, Any]],
    action_card_specs: Sequence[Mapping[str, Any]],
    asset_verification: Mapping[str, Any],
) -> dict[str, Any]:
    """Materialize this run's Planner input from fresh state, never a committed fixture."""

    verified_assets = _verified_asset_ids(asset_verification)
    classified_active = {
        item.get("rule_instance_id"): item
        for item in development_items
        if item.get("kind") == "ACTIVE_RULE_INSTANCE"
    }
    unresolved: list[dict[str, Any]] = []
    for result in active_rule_results:
        if result.get("status") != "UNRESOLVED":
            continue
        ref = _require_string(result.get("rule_instance_id"), "active_rule_result")
        classified = classified_active.get(ref)
        if not isinstance(classified, Mapping):
            raise ExposedPaperBlindCapsuleError("ACTIVE_UNRESOLVED_ITEM_NOT_CLASSIFIED")
        unresolved.append(
            {
                "kind": "ACTIVE_RULE_INSTANCE",
                "ref": ref,
                "status": "UNRESOLVED",
                "gap_type": classified["gap_type"],
                "reason_codes": list(classified["reason_codes"]),
                "source": dict(classified["source"]),
            }
        )
    for item in development_items:
        if item.get("kind") != "DEVELOPMENT_OBLIGATION":
            continue
        unresolved.append(
            {
                "kind": "DECLARED_NONRULE_DEVELOPMENT_ITEM",
                "ref": _item_ref(item),
                "status": "UNRESOLVED_DEVELOPMENT_ITEM",
                "gap_type": item["gap_type"],
                "reason_codes": list(item["reason_codes"]),
                "source": dict(item["source"]),
            }
        )
    refs = {item["ref"] for item in unresolved}
    if len(refs) != len(unresolved):
        raise ExposedPaperBlindCapsuleError("DUPLICATE_FRESH_UNRESOLVED_REFERENCE")

    cards: list[dict[str, Any]] = []
    seen_card_ids: set[str] = set()
    for card_spec in action_card_specs:
        card = _require_mapping(card_spec, "action_card_spec")
        if card.get("case_id") != case_id:
            continue
        card_id = _require_string(card.get("card_id"), "action_card.card_id")
        if card_id in seen_card_ids:
            raise ExposedPaperBlindCapsuleError("DUPLICATE_ACTION_CARD_ID")
        seen_card_ids.add(card_id)
        addresses_ref = _require_string(card.get("addresses_ref"), "action_card.addresses_ref")
        required_assets = tuple(card.get("required_asset_ids", ()))
        if not all(isinstance(asset_id, str) for asset_id in required_assets):
            raise ExposedPaperBlindCapsuleError("ACTION_CARD_REQUIRED_ASSET_IDS_INVALID")
        if addresses_ref not in refs or not set(required_assets).issubset(verified_assets):
            continue
        cards.append(
            {
                "card_id": card_id,
                "case_id": case_id,
                "addresses_ref": addresses_ref,
                "action_kind": _require_string(card.get("action_kind"), "action_card.action_kind"),
                "prerequisites": list(card.get("prerequisites", ())),
                "prohibitions": list(card.get("prohibitions", ())),
                "required_asset_ids": list(required_assets),
            }
        )
    return {
        "schema_version": "paper-blind-planner-visible-input/v2",
        "case_id": case_id,
        "planner_boundary": "The Planner may select only listed card IDs or abstain. It may not create a Rule, choose an Operator, request execution, or state a scientific conclusion.",
        "unresolved_items": sorted(unresolved, key=lambda item: item["ref"]),
        "legal_action_cards": sorted(cards, key=lambda card: card["card_id"]),
        "required_output": {
            "case_id": "same as input",
            "decision": "SELECT_ACTIONS or ABSTAIN_NO_ACTION",
            "selected_card_ids": "listed card IDs only; empty only for ABSTAIN_NO_ACTION",
            "rationales": "object keyed exactly by selected card ID",
        },
    }


def _validate_planner_input(value: Mapping[str, Any], *, case_id: str) -> dict[str, Any]:
    expected = {
        "schema_version",
        "case_id",
        "planner_boundary",
        "unresolved_items",
        "legal_action_cards",
        "required_output",
    }
    if set(value) != expected or value.get("schema_version") != "paper-blind-planner-visible-input/v2":
        raise ExposedPaperBlindCapsuleError("PLANNER_INPUT_SCHEMA_INVALID")
    if value.get("case_id") != case_id:
        raise ExposedPaperBlindCapsuleError("PLANNER_INPUT_CASE_ID_MISMATCH")
    unresolved = value.get("unresolved_items")
    cards = value.get("legal_action_cards")
    if not isinstance(unresolved, list) or not isinstance(cards, list):
        raise ExposedPaperBlindCapsuleError("PLANNER_INPUT_CONTENT_INVALID")
    refs = set()
    for item in unresolved:
        ref = _require_string(_require_mapping(item, "planner_unresolved").get("ref"), "planner_unresolved.ref")
        if ref in refs:
            raise ExposedPaperBlindCapsuleError("PLANNER_UNRESOLVED_REF_DUPLICATE")
        refs.add(ref)
    card_ids = set()
    for card in cards:
        card_map = _require_mapping(card, "planner_card")
        card_id = _require_string(card_map.get("card_id"), "planner_card.card_id")
        if card_id in card_ids:
            raise ExposedPaperBlindCapsuleError("PLANNER_CARD_DUPLICATE")
        card_ids.add(card_id)
        if card_map.get("case_id") != case_id:
            raise ExposedPaperBlindCapsuleError("PLANNER_CARD_CASE_SCOPE_INVALID")
        if _require_string(card_map.get("addresses_ref"), "planner_card.addresses_ref") not in refs:
            raise ExposedPaperBlindCapsuleError("PLANNER_CARD_ADDRESS_NOT_FRESH_UNRESOLVED")
    return dict(value)


def validate_planner_proposal(planner_input: Mapping[str, Any], proposal: Mapping[str, Any]) -> dict[str, Any]:
    """Admit a legal card selection or explicit abstention; never an oracle card set."""

    case_id = _require_string(planner_input.get("case_id"), "planner_input.case_id")
    input_value = _validate_planner_input(planner_input, case_id=case_id)
    if set(proposal) != {"case_id", "decision", "selected_card_ids", "rationales"}:
        raise ExposedPaperBlindCapsuleError("PLANNER_PROPOSAL_FIELDS_INVALID")
    if proposal.get("case_id") != case_id:
        raise ExposedPaperBlindCapsuleError("PLANNER_PROPOSAL_CASE_ID_MISMATCH")
    decision = proposal.get("decision")
    if decision not in {"SELECT_ACTIONS", "ABSTAIN_NO_ACTION"}:
        raise ExposedPaperBlindCapsuleError("PLANNER_DECISION_INVALID")
    selected = _string_list(proposal.get("selected_card_ids"), "selected_card_ids", allow_empty=True)
    if decision == "SELECT_ACTIONS" and not selected:
        raise ExposedPaperBlindCapsuleError("PLANNER_SELECT_REQUIRES_CARD")
    if decision == "ABSTAIN_NO_ACTION" and selected:
        raise ExposedPaperBlindCapsuleError("PLANNER_ABSTAIN_MUST_SELECT_ZERO")
    cards = {card["card_id"]: card for card in input_value["legal_action_cards"]}
    if not set(selected).issubset(cards):
        raise ExposedPaperBlindCapsuleError("PLANNER_SELECTED_ILLEGAL_CARD")
    refs = {item["ref"] for item in input_value["unresolved_items"]}
    for card_id in selected:
        card = cards[card_id]
        if card.get("case_id") != case_id:
            raise ExposedPaperBlindCapsuleError("PLANNER_SELECTED_CROSS_CASE_CARD")
        if card.get("addresses_ref") not in refs:
            raise ExposedPaperBlindCapsuleError("PLANNER_SELECTED_CARD_NOT_FRESH")
    rationales = _require_mapping(proposal.get("rationales"), "planner_rationales")
    if set(rationales) != set(selected):
        raise ExposedPaperBlindCapsuleError("PLANNER_RATIONALES_DO_NOT_MATCH_SELECTION")
    return {
        "schema_version": "paper-blind-planner-proposal-admission/v2",
        "proposal_status": "ADMISSIBLE_CARD_SELECTION_ONLY",
        "case_id": case_id,
        "decision": decision,
        "selected_card_ids": selected,
        "rationales": {
            card_id: _require_string(rationales[card_id], f"planner_rationale.{card_id}")
            for card_id in selected
        },
        "execution_authorization": "AUTHORIZED_EXACT_SELECTED_CAPSULE_ACTIONS_ONLY",
        "scientific_disposition": "NOT_EVALUATED",
    }


def _manifest_asset_path(asset_id: str) -> Path:
    manifest = _read_json(FROZEN_INPUT_MANIFEST_PATH)
    assets = _require_mapping(manifest.get("assets"), "frozen_assets")
    asset = _require_mapping(assets.get(asset_id), f"asset.{asset_id}")
    relative = _require_string(asset.get("relative_path"), f"asset.{asset_id}.relative_path")
    candidate = (FROZEN_INPUT_ROOT / relative).resolve()
    if not candidate.is_relative_to(FROZEN_INPUT_ROOT.resolve()) or not candidate.is_file():
        raise ExposedPaperBlindCapsuleError(f"FROZEN_ASSET_UNAVAILABLE:{asset_id}")
    return candidate


def _hsp90_grouped_observable_dependence() -> dict[str, Any]:
    result = run_grouped_observable_sampling_diagnostics(
        observable_path=_manifest_asset_path("HSP90_CA46_CA60_DISTANCE_40X1021"),
        trajectory_group_manifest_path=_manifest_asset_path("HSP90_TRAJECTORY_GROUP_MANIFEST"),
        observable_id="HSP90_CA46_CA60_DISTANCE",
        analysis_window_label="FROZEN_1021_FRAME_OBSERVED_WINDOW",
    )
    if result.get("rule_effect") != "NO_ACTIVE_RULE_EFFECT":
        raise ExposedPaperBlindCapsuleError("HSP90_DESCRIPTION_MUST_NOT_EMIT_ACTIVE_RULE_EFFECT")
    return result


def _adk_static_reference_relative_proximity() -> dict[str, Any]:
    result = run_reference_relative_structural_projection(
        sample_id="ADK_1E4V_G10V_CHAIN_A_NONREFERENCE",
        sample_coordinate_path=_manifest_asset_path("ADK_1E4V_G10V_CHAIN_A_CA"),
        reference_coordinate_paths={
            "ADK_1AKE_CLOSED_REFERENCE": _manifest_asset_path("ADK_1AKE_CHAIN_A_CA"),
            "ADK_4AKE_OPEN_REFERENCE": _manifest_asset_path("ADK_4AKE_CHAIN_A_CA"),
        },
        residue_positions=list(range(1, 215)),
        alignment_positions=list(range(214)),
        classification_positions=list(range(214)),
    )
    if result.get("rule_effect") != "NO_ACTIVE_RULE_EFFECT":
        raise ExposedPaperBlindCapsuleError("ADK_DESCRIPTION_MUST_NOT_EMIT_ACTIVE_RULE_EFFECT")
    return result


_CARD_EXECUTORS: dict[str, Callable[[], dict[str, Any]]] = {
    "HSP90_GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION_V1": _hsp90_grouped_observable_dependence,
    "ADK_STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION_V1": _adk_static_reference_relative_proximity,
}


def _execute_selected_actions(
    *, case_id: str, planner_input: Mapping[str, Any], planner_admission: Mapping[str, Any]
) -> dict[str, Any]:
    """Execute exactly the admitted public cards after all checks pass."""

    selected = list(planner_admission["selected_card_ids"])
    cards = {card["card_id"]: card for card in planner_input["legal_action_cards"]}
    refs = {item["ref"] for item in planner_input["unresolved_items"]}
    for card_id in selected:
        card = cards.get(card_id)
        if card is None:
            raise ExposedPaperBlindCapsuleError("EXECUTION_CARD_NOT_IN_FRESH_PLANNER_INPUT")
        if card.get("case_id") != case_id:
            raise ExposedPaperBlindCapsuleError("EXECUTION_CARD_CROSS_CASE")
        if card.get("addresses_ref") not in refs:
            raise ExposedPaperBlindCapsuleError("EXECUTION_CARD_ADDRESS_NOT_FRESH")
        if card_id not in _CARD_EXECUTORS:
            raise ExposedPaperBlindCapsuleError("EXECUTION_CARD_HAS_NO_FIXED_CAPSULE_EXECUTOR")
    evidence = []
    for card_id in selected:
        card = cards[card_id]
        raw = _CARD_EXECUTORS[card_id]()
        if raw.get("rule_effect") != "NO_ACTIVE_RULE_EFFECT":
            raise ExposedPaperBlindCapsuleError("DESCRIPTIVE_RESULT_ATTEMPTED_ACTIVE_RULE_EFFECT")
        evidence.append(
            {
                "schema_version": "exposed-paper-blind-descriptive-evidence-result/v1",
                "card_id": card_id,
                "case_id": case_id,
                "addresses_ref": card["addresses_ref"],
                "action_kind": card["action_kind"],
                "rule_effect": "NO_ACTIVE_RULE_EFFECT",
                "active_rule_effect": None,
                "scientific_disposition": "NOT_EVALUATED",
                "descriptive_result": raw,
            }
        )
    return {
        "schema_version": "exposed-paper-blind-selected-action-execution/v1",
        "case_id": case_id,
        "execution_status": "NO_ACTION_SELECTED" if not selected else "SELECTED_ACTIONS_EXECUTED",
        "selected_card_ids": selected,
        "evidence_results": evidence,
        "boundary": "Only validated selected public development cards execute. Descriptive results have no active Rule effect.",
    }


def run_hsp90_exact_control_regression(*, output_root: str | Path) -> dict[str, Any]:
    """Run the pre-existing exact F04R02 closure as a separate control regression."""

    root = Path(output_root).resolve()
    exact_route = run_hsp90_reference_demo_route(
        evidence_root=EXACT_HSP90_EVIDENCE_ROOT,
        operator_registry=load_registered_operator_registry(OPERATOR_REGISTRY_PATH),
        workspace_root=REPO_ROOT,
        output_root=root,
    )
    before = exact_route["pre_operator_rule_result"]
    after = exact_route["post_operator_rule_result"]
    if before["status"] != "UNRESOLVED" or after["status"] != "PASS":
        raise ExposedPaperBlindCapsuleError("HSP90_EXACT_CONTROL_SAME_RULE_CLOSURE_CHANGED")
    if before["rule_instance_id"] != after["rule_instance_id"]:
        raise ExposedPaperBlindCapsuleError("HSP90_EXACT_CONTROL_RULE_IDENTITY_CHANGED")
    if after["rule_instance_id"] != HSP90_EXACT_CONTROL_RULE_INSTANCE_ID:
        raise ExposedPaperBlindCapsuleError("HSP90_EXACT_CONTROL_RULE_ID_UNEXPECTED")
    return {
        "schema_version": "existing-exact-hsp90-control-regression/v1",
        "sidecar_kind": "EXISTING_EXACT_CONTROL_REGRESSION",
        "case_scope": HSP90_CASE_ID,
        "public_case_rule_effect": "NO_ACTIVE_RULE_EFFECT",
        "exact_control_rule_effect": "ACTIVE_RULE_EFFECT",
        "exact_control_rule_instance_id": HSP90_EXACT_CONTROL_RULE_INSTANCE_ID,
        "same_rule_closure": exact_route,
        "scientific_disposition": "NOT_EVALUATED",
        "boundary": "This case-bound control is not selected by the public-case Planner and does not close a public HSP90 NMR-to-MD RuleInstance.",
    }


def _source_ids(facts: Mapping[str, Any]) -> set[str]:
    return {
        source.get("source_id")
        for source in facts.get("sources", [])
        if isinstance(source, Mapping) and isinstance(source.get("source_id"), str)
    }


def _edge_pairs_with_duplicates(facts: Mapping[str, Any]) -> list[tuple[str, str]]:
    pairs = []
    for edge in facts.get("edges", []):
        if isinstance(edge, Mapping) and isinstance(edge.get("left_source_id"), str) and isinstance(edge.get("right_source_id"), str):
            pairs.append(tuple(sorted((edge["left_source_id"], edge["right_source_id"]))))
    return pairs


def _edge_pairs(facts: Mapping[str, Any]) -> set[tuple[str, str]]:
    return set(_edge_pairs_with_duplicates(facts))


def _edge_pair_counts(facts: Mapping[str, Any]) -> dict[tuple[str, str], int]:
    counts: dict[tuple[str, str], int] = {}
    for pair in _edge_pairs_with_duplicates(facts):
        counts[pair] = counts.get(pair, 0) + 1
    return counts


def _set_comparison(observed: set[Any], reference: set[Any]) -> dict[str, Any]:
    return {
        "observed": sorted(observed),
        "reference": sorted(reference),
        "matched": sorted(observed & reference),
        "omitted_from_observed": sorted(reference - observed),
        "extra_in_observed": sorted(observed - reference),
    }


def _semantic_rule_statuses(
    results: Sequence[Mapping[str, Any]], casegraph: Mapping[str, Any]
) -> dict[str, dict[str, Any]]:
    edge_pairs = {
        item.get("comparison_id"): tuple(sorted((item.get("left_source_id"), item.get("right_source_id"))))
        for item in casegraph.get("comparisons", [])
        if isinstance(item, Mapping)
        and isinstance(item.get("comparison_id"), str)
        and isinstance(item.get("left_source_id"), str)
        and isinstance(item.get("right_source_id"), str)
    }
    normalized: dict[str, dict[str, Any]] = {}
    for result in results:
        target = result.get("target")
        if not isinstance(target, Mapping):
            continue
        kind, target_id, subrule = target.get("kind"), target.get("id"), result.get("runtime_subrule_id")
        if not all(isinstance(value, str) for value in (kind, target_id, subrule)):
            continue
        target_token = (
            "EDGE_ENDPOINTS:" + "|".join(edge_pairs[target_id])
            if kind == "EDGE" and target_id in edge_pairs
            else f"{kind}:{target_id}"
        )
        normalized[f"{subrule}::{target_token}"] = {
            "status": result.get("status"),
            "reason_codes": list(result.get("reason_codes", [])),
        }
    return normalized


def _source_field_assessment(
    observed_facts: Mapping[str, Any], reference_facts: Mapping[str, Any]
) -> list[dict[str, Any]]:
    fields = (
        "construct_and_condition",
        "sample_composition",
        "native_observable",
        "estimand",
        "time_semantics",
        "spatial_support",
        "unit_or_aggregation",
    )
    observed = {
        source.get("source_id"): source
        for source in observed_facts.get("sources", [])
        if isinstance(source, Mapping) and isinstance(source.get("source_id"), str)
    }
    reference = {
        source.get("source_id"): source
        for source in reference_facts.get("sources", [])
        if isinstance(source, Mapping) and isinstance(source.get("source_id"), str)
    }
    records = []
    for source_id in sorted(set(observed) & set(reference)):
        for field in fields:
            observed_value = observed[source_id].get(field)
            reference_value = reference[source_id].get(field)
            records.append(
                {
                    "source_id": source_id,
                    "field": field,
                    "observed_value": observed_value,
                    "reference_value": reference_value,
                    "observed_unknown_status": "UNKNOWN" if observed_value == "UNKNOWN" else "DECLARED_OR_FREE_TEXT",
                    "reference_unknown_status": "UNKNOWN" if reference_value == "UNKNOWN" else "DECLARED_OR_FREE_TEXT",
                    "assessment": "HUMAN_SEMANTIC_REVIEW_REQUIRED",
                }
            )
    return records


def _reference_comparison(
    *, reference: Mapping[str, Any], agent_rule_arm: Mapping[str, Any], reference_rule_arm: Mapping[str, Any]
) -> dict[str, Any]:
    reference_facts = _require_mapping(reference.get("reference_case_facts"), "reference_facts")
    proposal = _require_mapping(agent_rule_arm["admission"].get("proposal"), "agent_admission")
    observed_facts = _require_mapping(proposal.get("proposed_case_facts"), "agent_facts")
    observed_rules = _semantic_rule_statuses(
        agent_rule_arm["rule_results"], agent_rule_arm["projected_casegraph"]
    )
    reference_rules = _semantic_rule_statuses(
        reference_rule_arm["rule_results"], reference_rule_arm["projected_casegraph"]
    )
    field_assessment = _source_field_assessment(observed_facts, reference_facts)
    shared = sorted(set(observed_rules) & set(reference_rules))
    return {
        "comparison_status": "DEVELOPMENT_REFERENCE_COMPARISON_NOT_HUMAN_ADJUDICATION",
        "reference_status": reference["reference_status"],
        "BOUNDARY_CONSISTENCY": {
            "source_identity": _set_comparison(_source_ids(observed_facts), _source_ids(reference_facts)),
            "edge_endpoint_pairs": _set_comparison(_edge_pairs(observed_facts), _edge_pairs(reference_facts)),
            "observed_duplicate_edge_endpoint_pairs": [
                list(pair) for pair, count in sorted(_edge_pair_counts(observed_facts).items()) if count > 1
            ],
            "rule_applicability_after_platform_projection": _set_comparison(set(observed_rules), set(reference_rules)),
            "boundary": "These are platform-constrained identity and projection checks, not Agent scientific-accuracy metrics.",
        },
        "AGENT_AUTHORED_CONTENT_ASSESSMENT": {
            "source_inclusion_or_omission": _set_comparison(_source_ids(observed_facts), _source_ids(reference_facts)),
            "edge_inclusion_or_omission": _set_comparison(_edge_pairs(observed_facts), _edge_pairs(reference_facts)),
            "critical_source_field_side_by_side": field_assessment,
            "time_semantics_kind": [item for item in field_assessment if item["field"] == "time_semantics"],
            "forbidden_upgrade_violations": [],
            "downstream_rule_result_status_and_reason_agreement": [
                {
                    "semantic_rule_target": token,
                    "observed": observed_rules[token],
                    "reference": reference_rules[token],
                    "assessment": "PLATFORM_PROJECTED_RULE_COMPARISON_NOT_AGENT_ACCURACY",
                }
                for token in shared
            ],
            "boundary": "Free-text construct and estimand fields remain side-by-side items for human semantic review; no numeric Agent-accuracy score is emitted.",
        },
        "reference_expected_unresolved_development_obligations": list(reference["expected_unresolved_development_obligations"]),
        "paper_reported_conclusion_draft": dict(reference["PaperReportedConclusionDraft"]),
        "expert_bounded_conclusion_draft": dict(reference["ExpertBoundedConclusionDraft"]),
        "boundary": "Comparison exposes development differences only. It cannot adjudicate source science, paper understanding, or scientific correctness.",
    }


def _recorded_proposal_provenance(*, role: str, proposal_path: Path) -> dict[str, Any]:
    return {
        "schema_version": "exposed-paper-blind-recorded-proposal-provenance/v1",
        "role": role,
        "provenance_status": "RECORDED_PROPOSAL_REPLAY_ONLY",
        "answer_blindness_status": "ANSWER_BLINDNESS_NOT_INDEPENDENTLY_VERIFIED",
        "filesystem_isolation_technically_enforced": False,
        "recorded_proposal_path": proposal_path.relative_to(REPO_ROOT).as_posix(),
        "recorded_proposal_sha256": _sha256(proposal_path),
        "raw_response_available": False,
        "runtime_model_identity": "NOT_RECORDED_FOR_COMMITTED_FIXTURE",
        "boundary": "A metadata receipt without enforced workspace isolation is provenance only, not proof of an answer-blind Agent run or Agent performance.",
    }


def _resolution_options(
    items: Sequence[Mapping[str, Any]], selected_execution: Mapping[str, Any]
) -> list[dict[str, Any]]:
    actions = {
        "SOURCE_FACT_MISSING": ("EXACT_NARROW_LOOKUP_OR_NAMED_SOURCE_REVIEW", "Locate the declared missing source fact or obtain named source review."),
        "COMPUTABLE_EVIDENCE_MISSING": ("DESCRIPTIVE_OR_REVIEWED_COMPUTATION", "Use only a legal action whose output and claim ceiling are explicitly bounded."),
        "METHOD_OR_FORWARD_BRIDGE_MISSING": ("METHOD_OR_FORWARD_MODEL_REVIEW", "Review whether a modality-appropriate bridge or forward model is available."),
        "EVALUATION_CONTRACT_OR_RULE_LIFECYCLE_PENDING": ("HUMAN_REVIEW_BEFORE_RULE_ACTIVATION", "Keep the concern non-Rule until a reviewed evaluation contract exists."),
        "NEW_DATA_REQUIRED": ("ACQUIRE_DECLARED_MISSING_DATA_TYPE", "Obtain the specifically missing trajectory, ensemble, experiment, or other data type."),
        "HUMAN_SCIENTIFIC_JUDGMENT": ("NAMED_HUMAN_REVIEW", "Obtain named domain review rather than automatic scientific resolution."),
        "RULE_COVERAGE_GAP": ("REPORT_ONLY_NO_AUTOMATIC_RULE_CREATION", "Record the gap; do not synthesize a Rule during this capsule."),
    }
    evidence_by_ref: dict[str, list[Mapping[str, Any]]] = {}
    for evidence in selected_execution.get("evidence_results", []):
        if isinstance(evidence, Mapping) and isinstance(evidence.get("addresses_ref"), str):
            evidence_by_ref.setdefault(evidence["addresses_ref"], []).append(evidence)
    options = []
    for item in sorted(items, key=_item_ref):
        gap_type = item.get("gap_type")
        if gap_type not in actions:
            raise ExposedPaperBlindCapsuleError("RESOLUTION_OPTION_GAP_TYPE_INVALID")
        option_kind, option = actions[gap_type]
        evidence = evidence_by_ref.get(_item_ref(item), [])
        options.append(
            {
                "addresses_ref": _item_ref(item),
                "gap_type": gap_type,
                "resolution_option_kind": option_kind,
                "resolution_option": option,
                "claim_effect": item["claim_effect"],
                "selected_action_card_ids": [item["card_id"] for item in evidence],
                "action_outcomes": [
                    {
                        "rule_effect": item["rule_effect"],
                        "scientific_disposition": item["scientific_disposition"],
                    }
                    for item in evidence
                ],
            }
        )
    return options


def _case_human_packet(
    *,
    case_id: str,
    agent_rule_arm: Mapping[str, Any],
    development_obligations: Sequence[Mapping[str, Any]],
    selected_execution: Mapping[str, Any],
    comparison: Mapping[str, Any],
    exact_hsp90_control_regression: Mapping[str, Any] | None,
) -> dict[str, Any]:
    unresolved_rule_ids = sorted(
        result["rule_instance_id"]
        for result in agent_rule_arm["rule_results"]
        if result.get("status") == "UNRESOLVED"
    )
    return {
        "schema_version": "exposed-paper-blind-human-decision-packet/v2",
        "case_id": case_id,
        "development_status": "EXPOSED_DEVELOPMENT_ONLY",
        "terminal_disposition": "ABSTAIN_OR_HUMAN_REVIEW",
        "scientific_disposition": "NOT_EVALUATED",
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "requested_claim": agent_rule_arm["projected_casegraph"]["case"]["scientific_claim"],
        "blocking_unresolved_rule_instances": unresolved_rule_ids,
        "active_rule_results": _result_inventory(agent_rule_arm["rule_results"]),
        "descriptive_evidence_results_no_active_rule_effect": list(selected_execution["evidence_results"]),
        "existing_exact_hsp90_control_regression": (
            dict(exact_hsp90_control_regression)
            if exact_hsp90_control_regression is not None
            else {"status": "NOT_RUN_IN_THIS_CAPSULE_INVOCATION"}
        ),
        "unresolved_development_items": list(development_obligations),
        "resolution_options": _resolution_options(development_obligations, selected_execution),
        "development_reference_comparison": dict(comparison),
        "human_review_items": [
            "All scientific interpretation remains subject to named source-science review.",
            "The comparison reference is AI-authored and development-only, not a human-approved gold standard.",
        ],
        "forbidden_claims": [
            "scientific SUPPORT",
            "source-science approval",
            "paper-reading accuracy",
            "population",
            "kinetic rate",
            "free energy",
            "mechanism",
            "ADK dynamics portability",
            "general portability",
        ],
    }


def _write_arm(output_case_root: Path, arm_id: str, value: Mapping[str, Any]) -> None:
    _write_json(output_case_root / f"{arm_id}.json", value)


def _write_run_artifact_manifest(output_root: Path) -> dict[str, Any]:
    manifest_path = output_root / "development_run_artifact_manifest_v1.json"
    records = []
    for path in sorted(output_root.rglob("*")):
        if path.is_file() and path != manifest_path:
            records.append(
                {
                    "relative_path": path.relative_to(output_root).as_posix(),
                    "sha256": _sha256(path),
                    "bytes": path.stat().st_size,
                }
            )
    manifest = {
        "schema_version": "exposed-paper-blind-development-run-artifact-manifest/v1",
        "run_scope": "EXPOSED_PAPER_BLIND_SCIENTIFIC_DECISION_CAPSULE_V1",
        "frozen_input_manifest_sha256": _sha256(FROZEN_INPUT_MANIFEST_PATH),
        "artifact_count": len(records),
        "artifacts": records,
        "boundary": "Hashes identify this generated development run only; they do not establish scientific validity.",
    }
    _write_json(manifest_path, manifest)
    return manifest


def run_exposed_paper_blind_capsule(
    *,
    output_root: str | Path,
    profiler_proposal_overrides: Mapping[str, Mapping[str, Any]] | None = None,
    planner_proposal_overrides: Mapping[str, Mapping[str, Any]] | None = None,
    include_exact_hsp90_control_regression: bool = True,
) -> dict[str, Any]:
    """Run the fixed public-action capsule into an empty directory.

    Override parameters are test seams only. They do not add an Agent runtime or
    broaden public authority.
    """

    target_root = Path(output_root).resolve()
    if target_root.exists() and any(target_root.iterdir()):
        raise ExposedPaperBlindCapsuleError("OUTPUT_ROOT_MUST_BE_EMPTY")
    target_root.mkdir(parents=True, exist_ok=True)
    rules_bundle = load_rules_v1_bundle(RULES_ROOT)
    case_outputs: dict[str, Any] = {}
    exact_sidecar: dict[str, Any] | None = None

    for case_id, spec in _CASE_SPECS.items():
        case_root = target_root / spec["slug"]
        packet_path = Path(spec["packet"])
        visible_input = build_agent_visible_packet(packet_path)
        _assert_agent_visible_boundary(visible_input)
        _write_json(case_root / "agent_visible_input.json", visible_input)
        asset_verification = verify_declared_asset_hashes(packet_path)
        _write_json(case_root / "asset_identity_verification.json", asset_verification)

        profiler_path = Path(spec["profiler_proposal"])
        profiler_proposal = (
            dict(profiler_proposal_overrides[case_id])
            if profiler_proposal_overrides and case_id in profiler_proposal_overrides
            else _read_json(profiler_path)
        )
        profiler_provenance = _recorded_proposal_provenance(role="PROFILER", proposal_path=profiler_path)
        _write_json(case_root / "profiler_proposal_provenance.json", profiler_provenance)
        agent_rule_arm = _active_rule_results_for_proposal(
            packet_path=packet_path, proposal=profiler_proposal, rules_bundle=rules_bundle
        )
        _write_arm(case_root, "arm_b_recorded_profile_rules", agent_rule_arm)

        sealed_reference = _read_json(Path(spec["sealed_reference"]))
        _validate_sealed_reference(sealed_reference, case_id=case_id)
        reference_rule_arm = _active_rule_results_for_proposal(
            packet_path=packet_path,
            proposal=_reference_as_non_authoritative_proposal(sealed_reference),
            rules_bundle=rules_bundle,
        )
        reference_rule_arm["reference_status"] = sealed_reference["reference_status"]
        _write_arm(case_root, "arm_a_development_reference_rules", reference_rule_arm)

        obligations = _development_obligations(case_id, agent_rule_arm["rule_results"])
        _write_json(
            case_root / "unresolved_obligation_classification.json",
            {
                "schema_version": "exposed-paper-blind-obligation-classification/v2",
                "case_id": case_id,
                "active_rule_results": _result_inventory(agent_rule_arm["rule_results"]),
                "development_obligations": obligations,
                "boundary": "Candidate-only F04/F05/F07 concerns remain declared non-Rule lifecycle items; no candidate RuleResult is emitted.",
            },
        )
        planner_input = materialize_planner_input(
            case_id=case_id,
            active_rule_results=agent_rule_arm["rule_results"],
            development_items=obligations,
            action_card_specs=_ACTION_CARD_SPECS,
            asset_verification=asset_verification,
        )
        _validate_planner_input(planner_input, case_id=case_id)
        _assert_agent_visible_boundary(planner_input)
        _write_json(case_root / "planner_visible_input.json", planner_input)

        planner_path = Path(spec["planner_proposal"])
        planner_proposal = (
            dict(planner_proposal_overrides[case_id])
            if planner_proposal_overrides and case_id in planner_proposal_overrides
            else _read_json(planner_path)
        )
        planner_provenance = _recorded_proposal_provenance(role="PLANNER", proposal_path=planner_path)
        _write_json(case_root / "planner_proposal_provenance.json", planner_provenance)
        planner_admission = validate_planner_proposal(planner_input, planner_proposal)
        _write_json(case_root / "planner_proposal_admission.json", planner_admission)
        selected_execution = _execute_selected_actions(
            case_id=case_id,
            planner_input=planner_input,
            planner_admission=planner_admission,
        )
        _write_arm(
            case_root,
            "arm_c_selected_public_actions",
            {
                "schema_version": "exposed-paper-blind-full-harness-arm/v2",
                "case_id": case_id,
                "profiler_provenance": profiler_provenance,
                "planner_provenance": planner_provenance,
                "planner_admission": planner_admission,
                "selected_execution": selected_execution,
                "scientific_disposition": "NOT_EVALUATED",
                "boundary": "Only validated selected public development cards execute. Descriptive adapters do not update active RuleResults.",
            },
        )
        comparison = _reference_comparison(
            reference=sealed_reference,
            agent_rule_arm=agent_rule_arm,
            reference_rule_arm=reference_rule_arm,
        )
        _write_json(case_root / "development_reference_comparison.json", comparison)
        if case_id == HSP90_PUBLIC_CASE_ID and include_exact_hsp90_control_regression:
            exact_sidecar = run_hsp90_exact_control_regression(
                output_root=case_root / "existing_exact_hsp90_control_regression"
            )
            _write_json(case_root / "existing_exact_hsp90_control_regression.json", exact_sidecar)
        human_packet = _case_human_packet(
            case_id=case_id,
            agent_rule_arm=agent_rule_arm,
            development_obligations=obligations,
            selected_execution=selected_execution,
            comparison=comparison,
            exact_hsp90_control_regression=(exact_sidecar if case_id == HSP90_PUBLIC_CASE_ID else None),
        )
        _write_json(case_root / "human_decision_packet.json", human_packet)
        case_outputs[case_id] = {
            "asset_verification": asset_verification,
            "agent_rule_arm": agent_rule_arm,
            "reference_rule_arm": reference_rule_arm,
            "planner_input": planner_input,
            "planner_admission": planner_admission,
            "selected_execution": selected_execution,
            "human_decision_packet": human_packet,
        }

    summary = {
        "schema_version": "exposed-paper-blind-scientific-decision-capsule/v2",
        "development_status": "EXPOSED_DEVELOPMENT_ONLY",
        "accurate_description": "A reproducible two-case development integration capsule with recorded fact proposals, active Draft Rule evaluation, two descriptive scientific adapters, and one separate exact HSP90 control.",
        "cases": list(_CASE_SPECS),
        "capability_categories": [
            "EXISTING_EXACT_HSP90_CONTROL_REGRESSION",
            "GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION",
            "STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION",
        ],
        "new_adapters": [
            "GROUPED_OBSERVABLE_DEPENDENCE_DESCRIPTION",
            "STATIC_REFERENCE_RELATIVE_PROXIMITY_DESCRIPTION",
        ],
        "scientific_disposition": "NOT_EVALUATED",
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "recorded_proposal_status": "RECORDED_PROPOSAL_REPLAY_ONLY",
        "answer_blindness_status": "ANSWER_BLINDNESS_NOT_INDEPENDENTLY_VERIFIED",
        "dhfr_accessed": False,
        "network_accessed": False,
        "external_model_transport": False,
        "unsupported_support_packets": 0,
        "case_packets": {
            case_id: case_outputs[case_id]["human_decision_packet"]["terminal_disposition"]
            for case_id in _CASE_SPECS
        },
        "boundary": "No generic scheduler, action registry, Operator promotion, Rule activation, paper-understanding claim, or portability claim is present.",
    }
    _write_json(target_root / "capsule_summary.json", summary)
    artifact_manifest = _write_run_artifact_manifest(target_root)
    return {
        "summary": summary,
        "cases": case_outputs,
        "existing_exact_hsp90_control_regression": exact_sidecar,
        "artifact_manifest": artifact_manifest,
        "output_root": str(target_root),
    }


def create_clean_output_root(path: str | Path) -> Path:
    """Create an empty output root deliberately, rather than overwriting a prior run."""

    candidate = Path(path).resolve()
    if candidate.exists():
        if any(candidate.iterdir()):
            raise ExposedPaperBlindCapsuleError("OUTPUT_ROOT_MUST_BE_EMPTY")
    else:
        candidate.mkdir(parents=True)
    return candidate
