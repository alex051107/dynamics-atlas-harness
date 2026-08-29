"""Fixed two-case paper-blind development capsule.

This module is deliberately a capped integration, not a workflow engine.  It runs
two exposed development cases with the merged public-packet admission boundary,
the current F01/F02/F03/F06 Draft Rules evaluator, two descriptive package-backed
analysis adapters, and the pre-existing exact HSP90 F04R02 control route.

It never upgrades a candidate Rule, registers an Operator, emits scientific
SUPPORT, or turns an AI-authored development reference into human source-science
approval.  DHFR is absent by design.
"""

from __future__ import annotations

import hashlib
import json
from collections.abc import Mapping, Sequence
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

_CASE_SPECS = {
    HSP90_PUBLIC_CASE_ID: {
        "slug": "hsp90",
        "packet": PUBLIC_ROOT / "hsp90_public_packet_v1.json",
        "profiler_proposal": AGENT_RUN_ROOT / "profiler" / "hsp90_proposal.json",
        "planner_input": AGENT_RUN_ROOT / "planner" / "hsp90_action_input.json",
        "planner_proposal": AGENT_RUN_ROOT / "planner" / "hsp90_proposal.json",
        "sealed_reference": SEALED_REFERENCE_ROOT / "hsp90_development_reference_draft_v1.json",
        "required_cards": (
            "HSP90_GROUPED_SAMPLING_DESCRIPTION_V1",
            "HSP90_EXISTING_F04R02_EXACT_CONTROL_ROUTE",
        ),
    },
    ADK_PUBLIC_CASE_ID: {
        "slug": "adk",
        "packet": PUBLIC_ROOT / "adk_public_packet_v1.json",
        "profiler_proposal": AGENT_RUN_ROOT / "profiler" / "adk_proposal.json",
        "planner_input": AGENT_RUN_ROOT / "planner" / "adk_action_input.json",
        "planner_proposal": AGENT_RUN_ROOT / "planner" / "adk_proposal.json",
        "sealed_reference": SEALED_REFERENCE_ROOT / "adk_development_reference_draft_v1.json",
        "required_cards": ("ADK_NONREFERENCE_REFERENCE_PROJECTION_V1",),
    },
}

_FORBIDDEN_AGENT_VISIBLE_TERMS = (
    "sealed_reference",
    "development_reference",
    "claim_boundary",
    "platform_authority_envelope",
    "allowed_capability_ids",
    "operator_id",
    "scientific_disposition",
)


class ExposedPaperBlindCapsuleError(ValueError):
    """Raised when the fixed development capsule loses an authority boundary."""


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


def _require_string_list(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or not value:
        raise ExposedPaperBlindCapsuleError(f"NONEMPTY_STRING_LIST_REQUIRED:{label}")
    result = [_require_string(item, label) for item in value]
    if len(set(result)) != len(result):
        raise ExposedPaperBlindCapsuleError(f"DUPLICATE_VALUES:{label}")
    return result


def _reference_as_non_authoritative_proposal(reference: Mapping[str, Any]) -> dict[str, Any]:
    """Use a sealed draft solely as a post-run comparison arm input.

    It goes through the same fact admission path as an Agent proposal, but its
    result remains labeled as an AI-authored reference draft rather than authority.
    """

    facts = _require_mapping(reference.get("reference_case_facts"), "reference_case_facts")
    return {
        "case_id": _require_string(reference.get("case_id"), "reference.case_id"),
        "proposed_case_facts": dict(facts),
        "unknowns": [
            "This development reference draft is not a named human source-science review."
        ],
        "rationale": "Non-authoritative sealed development reference used only after the answer-blind run.",
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


def _validate_planner_input(value: Mapping[str, Any], *, case_id: str) -> dict[str, Any]:
    expected = {
        "schema_version",
        "case_id",
        "planner_boundary",
        "unresolved_items",
        "legal_action_cards",
        "required_output",
    }
    if set(value) != expected or value.get("schema_version") != "paper-blind-planner-visible-input/v1":
        raise ExposedPaperBlindCapsuleError("PLANNER_INPUT_SCHEMA_INVALID")
    if value.get("case_id") != case_id:
        raise ExposedPaperBlindCapsuleError("PLANNER_INPUT_CASE_ID_MISMATCH")
    _require_string(value.get("planner_boundary"), "planner_boundary")
    unresolved = value.get("unresolved_items")
    cards = value.get("legal_action_cards")
    if not isinstance(unresolved, list) or not unresolved or not isinstance(cards, list) or not cards:
        raise ExposedPaperBlindCapsuleError("PLANNER_INPUT_CONTENT_INVALID")
    card_ids: list[str] = []
    for card in cards:
        card_map = _require_mapping(card, "legal_action_card")
        card_ids.append(_require_string(card_map.get("card_id"), "legal_action_card.card_id"))
        _require_string(card_map.get("addresses_ref"), "legal_action_card.addresses_ref")
        _require_string(card_map.get("action_kind"), "legal_action_card.action_kind")
    if len(set(card_ids)) != len(card_ids):
        raise ExposedPaperBlindCapsuleError("PLANNER_CARD_DUPLICATE")
    return dict(value)


def validate_planner_proposal(
    planner_input: Mapping[str, Any], proposal: Mapping[str, Any], *, required_cards: Sequence[str]
) -> dict[str, Any]:
    """Validate the isolated Planner's card-only proposal and nothing more."""

    case_id = _require_string(planner_input.get("case_id"), "planner_input.case_id")
    _validate_planner_input(planner_input, case_id=case_id)
    if set(proposal) != {"case_id", "selected_card_ids", "rationales"}:
        raise ExposedPaperBlindCapsuleError("PLANNER_PROPOSAL_FIELDS_INVALID")
    if proposal.get("case_id") != case_id:
        raise ExposedPaperBlindCapsuleError("PLANNER_PROPOSAL_CASE_ID_MISMATCH")
    selected = _require_string_list(proposal.get("selected_card_ids"), "selected_card_ids")
    legal = {
        _require_string(_require_mapping(card, "planner_card").get("card_id"), "planner_card.card_id")
        for card in planner_input["legal_action_cards"]
    }
    if not set(selected).issubset(legal):
        raise ExposedPaperBlindCapsuleError("PLANNER_SELECTED_ILLEGAL_CARD")
    if set(selected) != set(required_cards):
        raise ExposedPaperBlindCapsuleError("PLANNER_REQUIRED_CARD_MISSING")
    rationales = _require_mapping(proposal.get("rationales"), "planner_rationales")
    if set(rationales) != set(selected):
        raise ExposedPaperBlindCapsuleError("PLANNER_RATIONALES_DO_NOT_MATCH_SELECTION")
    normalized_rationales = {
        card_id: _require_string(rationales[card_id], f"planner_rationale.{card_id}")
        for card_id in selected
    }
    return {
        "schema_version": "paper-blind-planner-proposal-admission/v1",
        "proposal_status": "ADMISSIBLE_CARD_SELECTION_ONLY",
        "case_id": case_id,
        "selected_card_ids": selected,
        "rationales": normalized_rationales,
        "execution_authorization": "AUTHORIZED_EXACT_CAPSULE_ACTIONS_ONLY",
        "scientific_disposition": "NOT_EVALUATED",
    }


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
    results = evaluate_active_rules(case_graph=case_graph, **rules_bundle)
    return {
        "admission": admitted,
        "projected_casegraph": case_graph,
        "rule_results": results,
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


def _development_obligations(case_id: str, rule_results: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Classify gaps without manufacturing a candidate-family RuleResult."""

    unresolved_active = [
        {
            "kind": "ACTIVE_RULE_INSTANCE",
            "rule_instance_id": item["rule_instance_id"],
            "runtime_subrule_id": item["runtime_subrule_id"],
            "target": dict(item["target"]),
            "gap_type": "SOURCE_FACT_MISSING",
            "reason_codes": list(item["reason_codes"]),
            "claim_effect": "Active Draft Rule remains unresolved; no scientific conclusion is emitted.",
        }
        for item in rule_results
        if item.get("status") == "UNRESOLVED"
    ]
    if case_id == HSP90_PUBLIC_CASE_ID:
        additions = [
            {
                "kind": "EXISTING_CASE_BOUND_CONTROL",
                "rule_instance_id": HSP90_EXACT_CONTROL_RULE_INSTANCE_ID,
                "gap_type": "COMPUTABLE_EVIDENCE_MISSING",
                "claim_effect": "Only the existing exact HSP90 control record may change from UNRESOLVED to PASS after its frozen route validates.",
            },
            {
                "kind": "DEVELOPMENT_OBLIGATION",
                "development_obligation_ref": "HSP90_DEV_OBL_SAMPLING_DESCRIPTION",
                "gap_type": "COMPUTABLE_EVIDENCE_MISSING",
                "claim_effect": "Descriptive evidence only; no active RuleResult or scientific disposition may change.",
            },
            {
                "kind": "DEVELOPMENT_OBLIGATION",
                "development_obligation_ref": "HSP90_DEV_OBL_NMR_MD_FORWARD_BRIDGE",
                "gap_type": "NEW_DATA_REQUIRED",
                "claim_effect": "Cross-source relation remains unresolved without a reviewed bridge.",
            },
            {
                "kind": "DEVELOPMENT_OBLIGATION",
                "development_obligation_ref": "HSP90_DEV_OBL_SOURCE_SCIENCE_REVIEW",
                "gap_type": "HUMAN_SCIENTIFIC_JUDGMENT",
                "claim_effect": "Named source-science review remains required.",
            },
            {
                "kind": "DEVELOPMENT_OBLIGATION",
                "development_obligation_ref": "HSP90_DEV_OBL_F04_F05_F07_CANDIDATE_COVERAGE",
                "gap_type": "RULE_COVERAGE_GAP",
                "claim_effect": "Candidate-only families stay outside the active RuleResult inventory.",
            },
        ]
    elif case_id == ADK_PUBLIC_CASE_ID:
        additions = [
            {
                "kind": "DEVELOPMENT_OBLIGATION",
                "development_obligation_ref": "ADK_DEV_OBL_REFERENCE_RELATIVE_PROXIMITY",
                "gap_type": "COMPUTABLE_EVIDENCE_MISSING",
                "claim_effect": "Descriptive evidence only; no active RuleResult or scientific disposition may change.",
            },
            {
                "kind": "DEVELOPMENT_OBLIGATION",
                "development_obligation_ref": "ADK_DEV_OBL_DYNAMIC_COVERAGE",
                "gap_type": "NEW_DATA_REQUIRED",
                "claim_effect": "A static mutant structure cannot establish dynamical coverage.",
            },
            {
                "kind": "DEVELOPMENT_OBLIGATION",
                "development_obligation_ref": "ADK_DEV_OBL_SOURCE_SCIENCE_REVIEW",
                "gap_type": "HUMAN_SCIENTIFIC_JUDGMENT",
                "claim_effect": "Named source-science review remains required for biological interpretation.",
            },
            {
                "kind": "DEVELOPMENT_OBLIGATION",
                "development_obligation_ref": "ADK_DEV_OBL_F05_F07_CANDIDATE_COVERAGE",
                "gap_type": "RULE_COVERAGE_GAP",
                "claim_effect": "Candidate-only representation and identifiability families remain unevaluated.",
            },
        ]
    else:
        raise ExposedPaperBlindCapsuleError("UNSUPPORTED_CAPSULE_CASE")
    return unresolved_active + additions


def _manifest_asset_path(asset_id: str) -> Path:
    manifest = _read_json(FROZEN_INPUT_MANIFEST_PATH)
    assets = _require_mapping(manifest.get("assets"), "frozen_assets")
    asset = _require_mapping(assets.get(asset_id), f"asset.{asset_id}")
    relative = _require_string(asset.get("relative_path"), f"asset.{asset_id}.relative_path")
    candidate = (FROZEN_INPUT_ROOT / relative).resolve()
    if not candidate.is_relative_to(FROZEN_INPUT_ROOT.resolve()) or not candidate.is_file():
        raise ExposedPaperBlindCapsuleError(f"FROZEN_ASSET_UNAVAILABLE:{asset_id}")
    return candidate


def _execute_hsp90_selected_actions(*, output_root: Path) -> dict[str, Any]:
    operator_registry = load_registered_operator_registry(OPERATOR_REGISTRY_PATH)
    exact_route = run_hsp90_reference_demo_route(
        evidence_root=EXACT_HSP90_EVIDENCE_ROOT,
        operator_registry=operator_registry,
        workspace_root=REPO_ROOT,
        output_root=output_root / "hsp90_exact_f04r02_control",
    )
    if exact_route["pre_operator_rule_result"]["status"] != "UNRESOLVED":
        raise ExposedPaperBlindCapsuleError("HSP90_EXACT_ROUTE_PRECONDITION_CHANGED")
    if exact_route["post_operator_rule_result"]["status"] != "PASS":
        raise ExposedPaperBlindCapsuleError("HSP90_EXACT_ROUTE_DID_NOT_CLOSE_SAME_RULE")
    if (
        exact_route["pre_operator_rule_result"]["rule_instance_id"]
        != exact_route["post_operator_rule_result"]["rule_instance_id"]
        or exact_route["post_operator_rule_result"]["rule_instance_id"]
        != HSP90_EXACT_CONTROL_RULE_INSTANCE_ID
    ):
        raise ExposedPaperBlindCapsuleError("HSP90_EXACT_ROUTE_RULE_IDENTITY_CHANGED")
    sampling = run_grouped_observable_sampling_diagnostics(
        observable_path=_manifest_asset_path("HSP90_CA46_CA60_DISTANCE_40X1021"),
        trajectory_group_manifest_path=_manifest_asset_path("HSP90_TRAJECTORY_GROUP_MANIFEST"),
        observable_id="HSP90_CA46_CA60_DISTANCE",
        analysis_window_label="FROZEN_1021_FRAME_OBSERVED_WINDOW",
    )
    if sampling.get("rule_effect") != "NO_RULE_RESULT_EMITTED":
        raise ExposedPaperBlindCapsuleError("HSP90_SAMPLING_MUST_NOT_EMIT_RULE_RESULT")
    return {"exact_hsp90_control": exact_route, "sampling_description": sampling}


def _execute_adk_selected_actions() -> dict[str, Any]:
    projection = run_reference_relative_structural_projection(
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
    if projection.get("rule_effect") != "NO_RULE_RESULT_EMITTED":
        raise ExposedPaperBlindCapsuleError("ADK_PROJECTION_MUST_NOT_EMIT_RULE_RESULT")
    return {"reference_relative_projection": projection}


def _source_ids(facts: Mapping[str, Any]) -> set[str]:
    sources = facts.get("sources")
    if not isinstance(sources, list):
        return set()
    return {
        item.get("source_id")
        for item in sources
        if isinstance(item, Mapping) and isinstance(item.get("source_id"), str)
    }


def _edge_pairs(facts: Mapping[str, Any]) -> set[tuple[str, str]]:
    edges = facts.get("edges")
    if not isinstance(edges, list):
        return set()
    pairs: set[tuple[str, str]] = set()
    for item in edges:
        if not isinstance(item, Mapping):
            continue
        left, right = item.get("left_source_id"), item.get("right_source_id")
        if isinstance(left, str) and isinstance(right, str):
            pairs.add(tuple(sorted((left, right))))
    return pairs


def _edge_pair_counts(facts: Mapping[str, Any]) -> dict[tuple[str, str], int]:
    edges = facts.get("edges")
    counts: dict[tuple[str, str], int] = {}
    if not isinstance(edges, list):
        return counts
    for item in edges:
        if not isinstance(item, Mapping):
            continue
        left, right = item.get("left_source_id"), item.get("right_source_id")
        if isinstance(left, str) and isinstance(right, str):
            pair = tuple(sorted((left, right)))
            counts[pair] = counts.get(pair, 0) + 1
    return counts


def _overlap_metrics(observed: set[Any], expected: set[Any]) -> dict[str, Any]:
    overlap = observed & expected
    return {
        "observed": sorted(observed),
        "reference": sorted(expected),
        "matched": sorted(overlap),
        "omitted_from_observed": sorted(expected - observed),
        "extra_in_observed": sorted(observed - expected),
        "precision": None if not observed else len(overlap) / len(observed),
        "recall": None if not expected else len(overlap) / len(expected),
    }


def _semantic_rule_tokens(
    results: Sequence[Mapping[str, Any]], casegraph: Mapping[str, Any]
) -> set[str]:
    """Compare Rule applicability by target meaning, not agent-chosen edge labels."""

    edge_pairs = {
        item.get("comparison_id"): tuple(sorted((item.get("left_source_id"), item.get("right_source_id"))))
        for item in casegraph.get("comparisons", [])
        if isinstance(item, Mapping)
        and isinstance(item.get("comparison_id"), str)
        and isinstance(item.get("left_source_id"), str)
        and isinstance(item.get("right_source_id"), str)
    }
    tokens: set[str] = set()
    for result in results:
        target = result.get("target")
        if not isinstance(target, Mapping):
            continue
        kind, target_id = target.get("kind"), target.get("id")
        runtime_subrule_id = result.get("runtime_subrule_id")
        if not isinstance(runtime_subrule_id, str) or not isinstance(kind, str) or not isinstance(target_id, str):
            continue
        if kind == "EDGE":
            pair = edge_pairs.get(target_id)
            if pair is None:
                continue
            semantic_target = "EDGE_ENDPOINTS:" + "|".join(pair)
        else:
            semantic_target = f"{kind}:{target_id}"
        tokens.add(f"{runtime_subrule_id}::{semantic_target}")
    return tokens


def _rule_applicability_comparison(
    observed: Sequence[Mapping[str, Any]],
    expected: Sequence[Mapping[str, Any]],
    *,
    observed_casegraph: Mapping[str, Any],
    expected_casegraph: Mapping[str, Any],
) -> dict[str, Any]:
    return _overlap_metrics(
        _semantic_rule_tokens(observed, observed_casegraph),
        _semantic_rule_tokens(expected, expected_casegraph),
    )


def _reference_comparison(
    *, reference: Mapping[str, Any], agent_rule_arm: Mapping[str, Any], reference_rule_arm: Mapping[str, Any]
) -> dict[str, Any]:
    reference_facts = _require_mapping(reference.get("reference_case_facts"), "reference_facts")
    proposal = _require_mapping(agent_rule_arm["admission"].get("proposal"), "agent_admission")
    observed_facts = _require_mapping(proposal.get("proposed_case_facts"), "agent_facts")
    observed_case = _require_mapping(observed_facts.get("case"), "agent_case")
    reference_case = _require_mapping(reference_facts.get("case"), "reference_case")
    return {
        "comparison_status": "DEVELOPMENT_REFERENCE_COMPARISON_NOT_HUMAN_ADJUDICATION",
        "reference_status": reference["reference_status"],
        "casegraph_fact_comparison": {
            "source_identity": _overlap_metrics(_source_ids(observed_facts), _source_ids(reference_facts)),
            "edge_endpoint_pairs": _overlap_metrics(_edge_pairs(observed_facts), _edge_pairs(reference_facts)),
            "observed_edge_count": len(observed_facts.get("edges", [])),
            "reference_edge_count": len(reference_facts.get("edges", [])),
            "observed_duplicate_edge_endpoint_pairs": [
                list(pair)
                for pair, count in sorted(_edge_pair_counts(observed_facts).items())
                if count > 1
            ],
            "requested_claim_level_match": observed_case.get("requested_claim_level")
            == reference_case.get("requested_claim_level"),
            "intended_use_match": observed_case.get("intended_use") == reference_case.get("intended_use"),
        },
        "rule_applicability": _rule_applicability_comparison(
            agent_rule_arm["rule_results"],
            reference_rule_arm["rule_results"],
            observed_casegraph=agent_rule_arm["projected_casegraph"],
            expected_casegraph=reference_rule_arm["projected_casegraph"],
        ),
        "reference_expected_unresolved_development_obligations": list(
            reference["expected_unresolved_development_obligations"]
        ),
        "paper_reported_conclusion_draft": dict(reference["PaperReportedConclusionDraft"]),
        "expert_bounded_conclusion_draft": dict(reference["ExpertBoundedConclusionDraft"]),
        "boundary": "Comparison can expose development differences only. It cannot adjudicate science, approve source grounding, or upgrade a claim.",
    }


def _case_human_packet(
    *,
    case_id: str,
    agent_rule_arm: Mapping[str, Any],
    development_obligations: Sequence[Mapping[str, Any]],
    evidence: Mapping[str, Any],
    comparison: Mapping[str, Any],
) -> dict[str, Any]:
    unresolved = [item for item in agent_rule_arm["rule_results"] if item.get("status") == "UNRESOLVED"]
    first_blocker = unresolved[0]["rule_instance_id"] if unresolved else None
    if case_id == HSP90_PUBLIC_CASE_ID:
        next_actions = [
            {
                "action": "Named source-science review of NMR/MD condition and measurement bridge",
                "type": "HUMAN_REVIEW",
                "resolves": "Source semantics and comparability uncertainties.",
                "stop_condition": "Keep the relation unresolved without a bounded bridge.",
            },
            {
                "action": "Independent trajectory/observable assessment under a reviewed method profile",
                "type": "COMPUTATION_OR_NEW_SIMULATION",
                "resolves": "Whether the descriptive trace behavior is robust beyond the exact control record.",
                "stop_condition": "Do not promote a descriptive result to a population or kinetic claim.",
            },
            {
                "action": "Acquire a bridgeable experimental observable",
                "type": "NEW_EXPERIMENT",
                "resolves": "The unresolved NMR-to-MD interpretation.",
                "stop_condition": "Abstain if it cannot discriminate the ATP-lid interpretations.",
            },
        ]
    elif case_id == ADK_PUBLIC_CASE_ID:
        next_actions = [
            {
                "action": "Acquire a traceable wild-type ADK trajectory or ensemble with condition metadata",
                "type": "NEW_DATA_OR_COMPUTATION",
                "resolves": "Dynamic coverage beyond one static G10V sample.",
                "stop_condition": "Keep static proximity descriptive if no time-resolved data are admitted.",
            },
            {
                "action": "Named source-science review of endpoint and mutant comparability",
                "type": "HUMAN_REVIEW",
                "resolves": "Whether the static relation carries biological meaning.",
                "stop_condition": "Do not equate G10V geometry with a wild-type state without review.",
            },
            {
                "action": "Specify an observable and forward bridge",
                "type": "NEW_EXPERIMENT",
                "resolves": "A modality-appropriate link to the anchor structures.",
                "stop_condition": "Abstain if the observable cannot discriminate the open/closed interpretation.",
            },
        ]
    else:
        raise ExposedPaperBlindCapsuleError("UNSUPPORTED_HUMAN_PACKET_CASE")
    return {
        "schema_version": "exposed-paper-blind-human-decision-packet/v1",
        "case_id": case_id,
        "development_status": "EXPOSED_DEVELOPMENT_ONLY",
        "terminal_disposition": "ABSTAIN_OR_HUMAN_REVIEW",
        "scientific_disposition": "NOT_EVALUATED",
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "requested_claim": agent_rule_arm["projected_casegraph"]["case"]["scientific_claim"],
        "first_blocking_rule_instance": first_blocker,
        "active_rule_results": _result_inventory(agent_rule_arm["rule_results"]),
        "development_obligations": list(development_obligations),
        "evidence_results": dict(evidence),
        "development_reference_comparison": dict(comparison),
        "human_review_items": [
            "All scientific interpretation remains subject to named source-science review.",
            "The comparison reference is AI-authored and development-only, not a human-approved gold standard.",
        ],
        "next_actions": next_actions,
        "forbidden_claims": [
            "scientific SUPPORT",
            "source-science approval",
            "population",
            "kinetic rate",
            "free energy",
            "mechanism",
            "general portability",
        ],
    }


def _write_arm(output_case_root: Path, arm_id: str, value: Mapping[str, Any]) -> None:
    _write_json(output_case_root / f"{arm_id}.json", value)


def _write_run_artifact_manifest(output_root: Path) -> dict[str, Any]:
    """Freeze this one generated run without introducing a reusable artifact service."""

    manifest_path = output_root / "development_run_artifact_manifest_v1.json"
    records = []
    for path in sorted(output_root.rglob("*")):
        if not path.is_file() or path == manifest_path:
            continue
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


def run_exposed_paper_blind_capsule(*, output_root: str | Path) -> dict[str, Any]:
    """Run the one capped HSP90+ADK development capsule into an empty directory."""

    target_root = Path(output_root).resolve()
    if target_root.exists() and any(target_root.iterdir()):
        raise ExposedPaperBlindCapsuleError("OUTPUT_ROOT_MUST_BE_EMPTY")
    target_root.mkdir(parents=True, exist_ok=True)
    rules_bundle = load_rules_v1_bundle(RULES_ROOT)
    case_outputs: dict[str, Any] = {}

    for case_id, spec in _CASE_SPECS.items():
        case_root = target_root / spec["slug"]
        packet_path = Path(spec["packet"])
        visible_input = build_agent_visible_packet(packet_path)
        _assert_agent_visible_boundary(visible_input)
        _write_json(case_root / "agent_visible_input.json", visible_input)
        asset_verification = verify_declared_asset_hashes(packet_path)
        _write_json(case_root / "asset_identity_verification.json", asset_verification)

        profiler_proposal = _read_json(Path(spec["profiler_proposal"]))
        agent_rule_arm = _active_rule_results_for_proposal(
            packet_path=packet_path, proposal=profiler_proposal, rules_bundle=rules_bundle
        )
        _write_arm(case_root, "arm_b_agent_profile_rules", agent_rule_arm)

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
                "schema_version": "exposed-paper-blind-obligation-classification/v1",
                "case_id": case_id,
                "active_rule_results": _result_inventory(agent_rule_arm["rule_results"]),
                "development_obligations": obligations,
                "boundary": "Candidate-only F04/F05/F07 items are development obligations, not emitted RuleResults.",
            },
        )

        planner_input = _validate_planner_input(_read_json(Path(spec["planner_input"])), case_id=case_id)
        _assert_agent_visible_boundary(planner_input)
        _write_json(case_root / "planner_visible_input.json", planner_input)
        planner_admission = validate_planner_proposal(
            planner_input,
            _read_json(Path(spec["planner_proposal"])),
            required_cards=spec["required_cards"],
        )
        _write_json(case_root / "planner_proposal_admission.json", planner_admission)

        if case_id == HSP90_PUBLIC_CASE_ID:
            evidence = _execute_hsp90_selected_actions(output_root=case_root / "arm_c_full_harness")
        else:
            evidence = _execute_adk_selected_actions()
        _write_arm(
            case_root,
            "arm_c_full_harness",
            {
                "schema_version": "exposed-paper-blind-full-harness-arm/v1",
                "case_id": case_id,
                "planner_admission": planner_admission,
                "evidence_results": evidence,
                "scientific_disposition": "NOT_EVALUATED",
                "boundary": "Only exact selected actions ran. Descriptive adapters do not update RuleResults.",
            },
        )

        comparison = _reference_comparison(
            reference=sealed_reference,
            agent_rule_arm=agent_rule_arm,
            reference_rule_arm=reference_rule_arm,
        )
        _write_json(case_root / "development_reference_comparison.json", comparison)
        human_packet = _case_human_packet(
            case_id=case_id,
            agent_rule_arm=agent_rule_arm,
            development_obligations=obligations,
            evidence=evidence,
            comparison=comparison,
        )
        _write_json(case_root / "human_decision_packet.json", human_packet)
        case_outputs[case_id] = {
            "asset_verification": asset_verification,
            "agent_rule_arm": agent_rule_arm,
            "reference_rule_arm": reference_rule_arm,
            "planner_admission": planner_admission,
            "evidence_results": evidence,
            "human_decision_packet": human_packet,
        }

    summary = {
        "schema_version": "exposed-paper-blind-scientific-decision-capsule/v1",
        "development_status": "EXPOSED_DEVELOPMENT_ONLY",
        "cases": list(_CASE_SPECS),
        "capability_categories": [
            "EXISTING_HSP90_DIRECTIONAL_TIME_ANATOMY_EXACT_CONTROL",
            "GROUPED_OBSERVABLE_SAMPLING_DESCRIPTION",
            "REFERENCE_RELATIVE_STRUCTURAL_PROXIMITY_DESCRIPTION",
        ],
        "new_adapters": [
            "GROUPED_OBSERVABLE_SAMPLING_DESCRIPTION",
            "REFERENCE_RELATIVE_STRUCTURAL_PROXIMITY_DESCRIPTION",
        ],
        "scientific_disposition": "NOT_EVALUATED",
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "dhfr_accessed": False,
        "network_accessed": False,
        "external_model_transport": False,
        "unsupported_support_packets": 0,
        "case_packets": {
            case_id: case_outputs[case_id]["human_decision_packet"]["terminal_disposition"]
            for case_id in _CASE_SPECS
        },
        "boundary": "One fixed development capsule; no generic scheduler, capability registry, Operator promotion, Rule activation, or portability claim.",
    }
    _write_json(target_root / "capsule_summary.json", summary)
    artifact_manifest = _write_run_artifact_manifest(target_root)
    return {
        "summary": summary,
        "cases": case_outputs,
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
