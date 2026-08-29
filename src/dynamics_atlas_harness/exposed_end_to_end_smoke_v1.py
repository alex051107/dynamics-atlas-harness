"""Exact two-case question-to-human-review smoke test for exposed development.

The primary input is the existing Lincoff X-EISD paper-derived development
question.  The companion HSP90 control proves the already-case-bound registered
Operator path.  This module binds pre-existing, recorded answer-blind Planner
card selections to the pre-existing reference routes; it is deliberately not a
general agent runtime, paper-retrieval layer, router, scheduler, or conclusion
engine.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from .exposed_proposal_smoke_v1 import (
    load_exposed_planner_fixtures,
    materialize_exposed_planner_proposal,
)
from .live_agent_exposed_v1 import evaluate_planner_proposal
from .real_case_vertical_slice_v1 import (
    evaluate_hsp90_time_anatomy_f04r02,
    evaluate_xeisd_case,
    load_hsp90_case_bundle,
    load_json_object,
    load_rules_v1_bundle,
    validate_hsp90_case_dossier,
    validate_xeisd_projection,
)
from .runnable_reference_demo_v1 import run_reference_demo


SMOKE_SCHEMA_VERSION = "exposed-end-to-end-smoke/v1"
SMOKE_RUN_ID = "exposed_end_to_end_smoke_v1"
_RECORDED_RUN = "qwen2_5_1_5b_20260826_prompt_remediation1"


class ExposedEndToEndSmokeError(ValueError):
    """Raised when the exact development smoke path cannot fail closed."""


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _read_json_value(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ExposedEndToEndSmokeError(f"cannot read smoke artifact {path}: {exc}") from exc


def _read_json(path: Path) -> dict[str, Any]:
    value = _read_json_value(path)
    if not isinstance(value, dict):
        raise ExposedEndToEndSmokeError(f"smoke artifact must be a JSON object: {path}")
    return value


def _prepare_output_dir(output_dir: Path) -> Path:
    output_dir = output_dir.resolve()
    if output_dir.exists() and (not output_dir.is_dir() or any(output_dir.iterdir())):
        raise ExposedEndToEndSmokeError("OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def _planner_reference(experiment_root: Path) -> dict[str, Any]:
    return _read_json(experiment_root / "sealed_references" / "planner_reference_v1.json")


def _actions_by_card(proposal: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    actions = proposal.get("proposed_actions")
    if not isinstance(actions, list) or not actions:
        raise ExposedEndToEndSmokeError("CANONICAL_PLANNER_PROPOSAL_HAS_NO_ACTIONS")
    result: dict[str, Mapping[str, Any]] = {}
    for action in actions:
        if not isinstance(action, Mapping) or not isinstance(action.get("card_id"), str):
            raise ExposedEndToEndSmokeError("CANONICAL_PLANNER_PROPOSAL_ACTION_INVALID")
        card_id = action["card_id"]
        if card_id in result:
            raise ExposedEndToEndSmokeError("CANONICAL_PLANNER_PROPOSAL_CARD_DUPLICATE")
        result[card_id] = action
    return result


def _expected_card_ids(packet: Mapping[str, Any]) -> set[str]:
    cards = packet.get("permitted_action_cards")
    if not isinstance(cards, list) or not cards:
        raise ExposedEndToEndSmokeError("PLANNER_PACKET_HAS_NO_PERMITTED_CARDS")
    ids = {
        card.get("card_id")
        for card in cards
        if isinstance(card, Mapping) and isinstance(card.get("card_id"), str)
    }
    if len(ids) != len(cards):
        raise ExposedEndToEndSmokeError("PLANNER_PACKET_CARD_IDENTITIES_INVALID")
    return ids


def _fresh_pre_agent_rule_selection(*, case_key: str, repo_root: Path) -> dict[str, Any]:
    """Recompute the existing prerequisite RuleResults before a Planner sees cards.

    This is fixed fixture preparation for the two exposed cases, not an execution
    router: action authority is still evaluated only after a Planner proposal is
    deterministically admitted below.
    """

    evidence_root = repo_root / "evidence" / "real_case_vertical_slice_v1"
    if case_key == "xeisd":
        seed = load_json_object(evidence_root / "xeisd_case_projection_seed_v1.json")
        validate_xeisd_projection(seed)
        bundle = load_rules_v1_bundle(repo_root / "registries" / "rules_v1")
        rule_results = evaluate_xeisd_case(case_graph=seed, **bundle)
        case = seed.get("case")
        if not isinstance(case, Mapping):
            raise ExposedEndToEndSmokeError("XEISD_PRE_AGENT_CASE_INVALID")
        return {
            "schema_version": "fresh-pre-agent-rule-selection/v1",
            "case_id": case.get("case_id"),
            "source_kind": "EXISTING_RULES_V1_EVALUATION_ON_EXPOSED_SEED",
            "case_graph_admission": {
                "status": "PASS",
                "validator": "validate_xeisd_projection",
                "scope": "EXACT_EXPOSED_PAPER_DERIVED_PROJECTION",
            },
            "rule_results": rule_results,
        }
    if case_key == "hsp90":
        bundle = load_hsp90_case_bundle(evidence_root)
        validate_hsp90_case_dossier(
            bundle["case_graph"], bundle["input_manifest"]
        )
        result = evaluate_hsp90_time_anatomy_f04r02(
            case_graph=bundle["case_graph"],
            rule_overlay=bundle["rule_overlay"],
            input_manifest=bundle["input_manifest"],
        )
        case = bundle["case_graph"].get("case")
        if not isinstance(case, Mapping):
            raise ExposedEndToEndSmokeError("HSP90_PRE_AGENT_CASE_INVALID")
        return {
            "schema_version": "fresh-pre-agent-rule-selection/v1",
            "case_id": case.get("case_id"),
            "source_kind": "EXISTING_F04R02_EVALUATION_ON_EXPOSED_CASE",
            "case_graph_admission": {
                "status": "PASS",
                "validator": "validate_hsp90_case_dossier",
                "scope": "EXACT_EXPOSED_CASE_BOUND_DOSSIER",
            },
            "rule_results": [result],
        }
    raise ExposedEndToEndSmokeError(f"UNSUPPORTED_EXPOSED_PRE_AGENT_CASE:{case_key}")


def _bind_authorized_proposal(
    *,
    case_key: str,
    packet: Mapping[str, Any],
    pre_agent_rule_selection: Mapping[str, Any],
    materialization: Mapping[str, Any],
    evaluation: Mapping[str, Any],
) -> dict[str, Any]:
    """Verify that a non-authoritative card proposal reaches one exact route.

    The route descriptor is derived from permitted card fields and the existing
    authorization receipt.  No case name, model rationale, or terminal result is
    used to choose an Operator or scientific disposition.
    """

    if materialization.get("status") != "PASS":
        raise ExposedEndToEndSmokeError("PLANNER_MATERIALIZATION_NOT_PASS")
    proposal = materialization.get("canonical_proposal")
    if not isinstance(proposal, Mapping):
        raise ExposedEndToEndSmokeError("PLANNER_MATERIALIZATION_MISSING_PROPOSAL")
    if proposal.get("execution_requested") is not False:
        raise ExposedEndToEndSmokeError("PLANNER_PROPOSAL_REQUESTED_EXECUTION")
    if proposal.get("scientific_disposition") != "NOT_EVALUATED":
        raise ExposedEndToEndSmokeError("PLANNER_PROPOSAL_ESCALATED_SCIENCE")

    typed = evaluation.get("typed_contract_view")
    sealed = evaluation.get("sealed_reference_and_authorization_view")
    if not isinstance(typed, Mapping) or typed.get("status") != "PASS":
        raise ExposedEndToEndSmokeError("PLANNER_TYPED_CONTRACT_NOT_PASS")
    if not isinstance(sealed, Mapping) or sealed.get("status") != "PASS":
        raise ExposedEndToEndSmokeError("PLANNER_REFERENCE_OR_AUTHORIZATION_NOT_PASS")
    authorization = sealed.get("deterministic_authorization")
    if not isinstance(authorization, Mapping) or authorization.get("status") != "AUTHORIZED_NO_EXECUTION":
        raise ExposedEndToEndSmokeError("PLANNER_ACTION_NOT_AUTHORIZED")
    if authorization.get("execution_performed") is not False:
        raise ExposedEndToEndSmokeError("PLANNER_AUTHORIZATION_EXECUTED_ACTION")

    actions = _actions_by_card(proposal)
    permitted_ids = _expected_card_ids(packet)
    if set(actions) != permitted_ids:
        raise ExposedEndToEndSmokeError("PLANNER_CARDS_DO_NOT_CLOSE_EXACT_EXPOSED_GAPS")
    selected_rules = packet.get("selected_rule_instances")
    if not isinstance(selected_rules, list) or not selected_rules:
        raise ExposedEndToEndSmokeError("PLANNER_PACKET_HAS_NO_SELECTED_RULE_INSTANCES")
    expected_rule_ids = {
        item.get("rule_instance_id")
        for item in selected_rules
        if isinstance(item, Mapping) and isinstance(item.get("rule_instance_id"), str)
    }
    action_rule_ids = {
        action.get("target_rule_instance_id")
        for action in actions.values()
        if isinstance(action.get("target_rule_instance_id"), str)
    }
    if action_rule_ids != expected_rule_ids:
        raise ExposedEndToEndSmokeError("PLANNER_CARD_TARGETS_DO_NOT_MATCH_SELECTED_RULES")
    if pre_agent_rule_selection.get("case_id") != proposal.get("case_id"):
        raise ExposedEndToEndSmokeError("FRESH_RULE_SELECTION_CASE_MISMATCH")
    admission = pre_agent_rule_selection.get("case_graph_admission")
    if not isinstance(admission, Mapping) or admission.get("status") != "PASS":
        raise ExposedEndToEndSmokeError("FRESH_CASE_GRAPH_ADMISSION_NOT_PASS")
    fresh_results = pre_agent_rule_selection.get("rule_results")
    if not isinstance(fresh_results, list):
        raise ExposedEndToEndSmokeError("FRESH_RULE_SELECTION_RESULTS_INVALID")
    fresh_by_id = {
        result.get("rule_instance_id"): result
        for result in fresh_results
        if isinstance(result, Mapping) and isinstance(result.get("rule_instance_id"), str)
    }
    if not action_rule_ids.issubset(fresh_by_id):
        raise ExposedEndToEndSmokeError("PLANNER_CARD_TARGETS_MISSING_FROM_FRESH_RULE_SELECTION")
    expected_route_by_action = {
        "EXACT_ATTESTATION": "SOURCE_LOOKUP",
        "REGISTERED_OPERATOR": "REGISTERED_OPERATOR",
    }
    for action in actions.values():
        result = fresh_by_id[action["target_rule_instance_id"]]
        if (
            result.get("status") != "UNRESOLVED"
            or result.get("claim_effect", {}).get("route")
            != expected_route_by_action.get(action.get("action"))
        ):
            raise ExposedEndToEndSmokeError("FRESH_RULE_SELECTION_DOES_NOT_PERMIT_PROPOSED_TRACK")

    actions_by_kind = {
        action.get("action")
        for action in actions.values()
        if isinstance(action.get("action"), str)
    }
    if actions_by_kind == {"EXACT_ATTESTATION"}:
        authorized_actions = authorization.get("authorized_actions")
        if not isinstance(authorized_actions, list):
            raise ExposedEndToEndSmokeError("ATTESTATION_AUTHORIZATION_ACTIONS_MISSING")
        authorized_ids = {
            action.get("card_id")
            for action in authorized_actions
            if isinstance(action, Mapping)
            and action.get("authorization_kind") == "EXACT_ALLOWLISTED_ATTESTATION_ONLY"
        }
        if authorized_ids != set(actions):
            raise ExposedEndToEndSmokeError("ATTESTATION_AUTHORIZATION_CARDS_MISMATCH")
        return {
            "case_key": case_key,
            "case_id": proposal["case_id"],
            "selected_card_ids": sorted(actions),
            "selected_rule_instance_ids": sorted(action_rule_ids),
            "pre_agent_rule_selection": "rules/xeisd_pre_agent_rule_selection.json",
            "selected_track": "EXACT_REVIEW_DERIVATIVE_ATTESTATION_THEN_DIRECT_EVALUATION",
            "authorization_boundary": "EXACT_ALLOWLISTED_ATTESTATION_ONLY",
            "execution_performed_by_planner": False,
            "scientific_disposition": "NOT_EVALUATED",
        }

    if actions_by_kind == {"REGISTERED_OPERATOR"} and len(actions) == 1:
        resolution = authorization.get("resolution")
        action = next(iter(actions.values()))
        if (
            not isinstance(resolution, Mapping)
            or resolution.get("status") != "ROUTABLE"
            or resolution.get("route") != "REGISTERED_OPERATOR"
            or resolution.get("operator_id") != action.get("operator_id")
            or resolution.get("affected_rule_instance_id") != action.get("target_rule_instance_id")
        ):
            raise ExposedEndToEndSmokeError("REGISTERED_OPERATOR_AUTHORIZATION_MISMATCH")
        return {
            "case_key": case_key,
            "case_id": proposal["case_id"],
            "selected_card_ids": sorted(actions),
            "selected_rule_instance_ids": sorted(action_rule_ids),
            "pre_agent_rule_selection": "rules/hsp90_pre_agent_rule_selection.json",
            "selected_track": "EXACT_CASE_BOUND_REGISTERED_OPERATOR_THEN_RULE_REEVALUATION",
            "operator_id": action.get("operator_id"),
            "authorization_boundary": "EXACT_CASE_BOUND_ROSTER_PASS_ONLY",
            "execution_performed_by_planner": False,
            "scientific_disposition": "NOT_EVALUATED",
        }

    raise ExposedEndToEndSmokeError("PLANNER_ACTION_SET_HAS_NO_EXACT_SMOKE_ROUTE")


def materialize_and_bind_exposed_case(*, case_key: str, repo_root: Path) -> dict[str, Any]:
    """Create one recorded Planner proposal and bind it to an exact route contract."""

    experiment_root = repo_root / "agent_experiments" / "v1"
    packet, _recorded_selection = load_exposed_planner_fixtures(
        case_key, experiment_root=experiment_root
    )
    pre_agent_rule_selection = _fresh_pre_agent_rule_selection(
        case_key=case_key, repo_root=repo_root
    )
    materialization = materialize_exposed_planner_proposal(
        case_key, experiment_root=experiment_root
    )
    proposal = materialization.get("canonical_proposal")
    if not isinstance(proposal, Mapping):
        raise ExposedEndToEndSmokeError("PLANNER_MATERIALIZATION_MISSING_PROPOSAL")
    evaluation = evaluate_planner_proposal(
        proposal,
        packet,
        _planner_reference(experiment_root),
        repo_root,
    )
    binding = _bind_authorized_proposal(
        case_key=case_key,
        packet=packet,
        pre_agent_rule_selection=pre_agent_rule_selection,
        materialization=materialization,
        evaluation=evaluation,
    )
    return {
        "planner_packet": packet,
        "pre_agent_rule_selection": pre_agent_rule_selection,
        "materialization": materialization,
        "evaluation": evaluation,
        "route_binding": binding,
    }


def _paper_question(repo_root: Path) -> dict[str, Any]:
    """Expose the exact paper-derived question without pretending to parse a paper."""

    evidence_root = repo_root / "evidence" / "real_case_vertical_slice_v1"
    seed = _read_json(evidence_root / "xeisd_case_projection_seed_v1.json")
    derivative = _read_json(
        evidence_root / "frozen_inputs/xeisd/exact_review_derivative_excerpt_v1.json"
    )
    case = seed.get("case")
    paper = derivative.get("paper_identity")
    if not isinstance(case, Mapping) or not isinstance(paper, Mapping):
        raise ExposedEndToEndSmokeError("PAPER_QUESTION_INPUT_INVALID")
    return {
        "schema_version": "paper-derived-question-input/v1",
        "input_kind": "EXACT_LOCAL_PAPER_DERIVED_DEVELOPMENT_REFERENCE",
        "paper_identity": paper,
        "case_id": case.get("case_id"),
        "parent_case_id": case.get("parent_case_id"),
        "scientific_question": case.get("scientific_claim"),
        "requested_claim_level": case.get("requested_claim_level"),
        "question_preparation": "Human-authored exposed-development CaseGraph projection. This smoke does not claim model paper parsing or passage entailment.",
        "allowed_source_paths": [
            "evidence/real_case_vertical_slice_v1/xeisd_case_projection_seed_v1.json",
            "evidence/real_case_vertical_slice_v1/frozen_inputs/xeisd/exact_review_derivative_excerpt_v1.json",
        ],
        "forbidden_interpretations": [
            "The local derivative is not free-text paper retrieval.",
            "The attestation route is not source-science validation.",
            "A route-control pass is not a scientific-support determination.",
        ],
    }


def _route_artifact_paths() -> dict[str, dict[str, str]]:
    return {
        "xeisd": {
            "route_packet": "reference_demo/routes/xeisd_a1/conclusion_packet.json",
            "lookup_receipts": "reference_demo/routes/xeisd_a1/lookup_receipts.json",
            "stage2_packet": "reference_demo/stage2/xeisd_a1_complete_stage2_conclusion_packet.json",
        },
        "hsp90": {
            "route_packet": "reference_demo/routes/hsp90_b1/conclusion_packet.json",
            "pre_operator_rule": "reference_demo/routes/hsp90_b1/pre_operator_rule_result.json",
            "operator_receipt": "reference_demo/routes/hsp90_b1/operator_run_receipt.json",
            "evidence_result": "reference_demo/routes/hsp90_b1/evidence_result.json",
            "post_operator_rule": "reference_demo/routes/hsp90_b1/post_operator_rule_result.json",
            "stage2_packet": "reference_demo/stage2/hsp90_b1_operator_contract_stage2_conclusion_packet.json",
        },
    }


def _bind_fresh_route_artifacts(
    *,
    output_dir: Path,
    bindings: Mapping[str, Mapping[str, Any]],
) -> dict[str, dict[str, Any]]:
    """Ensure the freshly rerun exact artifacts close only the proposed gaps."""

    paths = _route_artifact_paths()
    results: dict[str, dict[str, Any]] = {}
    for case_key, binding in bindings.items():
        case_paths = paths[case_key]
        route_packet = _read_json(output_dir / case_paths["route_packet"])
        stage2_packet = _read_json(output_dir / case_paths["stage2_packet"])
        selected_rule_ids = set(route_packet.get("selected_rule_instance_ids", []))
        proposed_rule_ids = set(binding["selected_rule_instance_ids"])
        if not proposed_rule_ids.issubset(selected_rule_ids):
            raise ExposedEndToEndSmokeError("FRESH_ROUTE_DID_NOT_REEVALUATE_PROPOSED_RULES")
        route_disposition = route_packet.get("route_disposition")
        terminal_disposition = stage2_packet.get("terminal_disposition")
        route_artifact = stage2_packet.get("route_artifact")
        if (
            not isinstance(route_artifact, Mapping)
            or route_artifact.get("scientific_disposition") != "NOT_EVALUATED"
            or stage2_packet.get("human_final_authority") is not True
            or stage2_packet.get("unsafe_claim_upgrade") is not False
        ):
            raise ExposedEndToEndSmokeError("STAGE2_PACKET_ESCALATED_SCIENTIFIC_DISPOSITION")

        if binding["selected_track"] == "EXACT_REVIEW_DERIVATIVE_ATTESTATION_THEN_DIRECT_EVALUATION":
            lookup_receipts = _read_json_value(output_dir / case_paths["lookup_receipts"])
            receipts = lookup_receipts if isinstance(lookup_receipts, list) else []
            if len(receipts) != len(proposed_rule_ids) or any(
                receipt.get("lookup_kind") != "EXACT_REVIEW_DERIVATIVE_ATTESTATION"
                or receipt.get("status") != "FOUND"
                for receipt in receipts
                if isinstance(receipt, Mapping)
            ):
                raise ExposedEndToEndSmokeError("FRESH_XEISD_ATTESTATION_ROUTE_INVALID")
            if route_disposition != "RELATION_REVIEWABLE":
                raise ExposedEndToEndSmokeError("FRESH_XEISD_ROUTE_DISPOSITION_CHANGED")
        else:
            pre_rule = _read_json(output_dir / case_paths["pre_operator_rule"])
            operator_receipt = _read_json(output_dir / case_paths["operator_receipt"])
            evidence = _read_json(output_dir / case_paths["evidence_result"])
            post_rule = _read_json(output_dir / case_paths["post_operator_rule"])
            expected_rule_id = next(iter(proposed_rule_ids))
            if (
                pre_rule.get("status") != "UNRESOLVED"
                or pre_rule.get("rule_instance_id") != expected_rule_id
                or operator_receipt.get("operator_id") != binding.get("operator_id")
                or evidence.get("affected_rule_instance_id") != expected_rule_id
                or evidence.get("contract_status") != "PASS"
                or evidence.get("scientific_evaluation_status") != "PENDING_HUMAN_VALIDATION"
                or post_rule.get("rule_instance_id") != expected_rule_id
                or post_rule.get("status") != "PASS"
                or route_disposition != "RULE_CONTRACT_PASS"
            ):
                raise ExposedEndToEndSmokeError("FRESH_HSP90_OPERATOR_ROUTE_INVALID")
        if terminal_disposition != "ABSTAIN_OR_HUMAN_REVIEW":
            raise ExposedEndToEndSmokeError("FRESH_EXPOSED_ROUTE_MUST_REMAIN_HUMAN_REVIEW")
        results[case_key] = {
            **binding,
            "route_disposition": route_disposition,
            "stage2_terminal_disposition": terminal_disposition,
            "route_artifacts": case_paths,
        }
    return results


def _human_decision_packet(
    *,
    paper_question: Mapping[str, Any],
    fresh_routes: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    """Render the existing decision boundary in one human-readable packet."""

    return {
        "schema_version": "exposed-human-decision-packet/v1",
        "packet_kind": "TWO_CASE_EXPOSED_DEVELOPMENT_SMOKE",
        "scientific_disposition": "NOT_EVALUATED",
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "system_recommendation": "ABSTAIN_OR_HUMAN_REVIEW",
        "primary_paper_question": {
            "paper_identity": paper_question["paper_identity"],
            "scientific_question": paper_question["scientific_question"],
            "selected_track": fresh_routes["xeisd"]["selected_track"],
            "rule_instance_ids": fresh_routes["xeisd"]["selected_rule_instance_ids"],
            "route_disposition": fresh_routes["xeisd"]["route_disposition"],
            "terminal_disposition": fresh_routes["xeisd"]["stage2_terminal_disposition"],
            "claim_assessment": "NOT_EVALUATED_PENDING_NAMED_DOMAIN_REVIEW",
            "human_review_question": "Do the named reviewer and project owner accept the narrowly declared source grounding and claim ceiling for this exact relation?",
        },
        "companion_operator_control": {
            "case_id": fresh_routes["hsp90"]["case_id"],
            "selected_track": fresh_routes["hsp90"]["selected_track"],
            "operator_id": fresh_routes["hsp90"].get("operator_id"),
            "rule_instance_ids": fresh_routes["hsp90"]["selected_rule_instance_ids"],
            "route_disposition": fresh_routes["hsp90"]["route_disposition"],
            "terminal_disposition": fresh_routes["hsp90"]["stage2_terminal_disposition"],
            "claim_assessment": "NOT_EVALUATED_PENDING_NAMED_DOMAIN_REVIEW",
            "human_review_question": "Does the named reviewer accept the exact same-packet control record only at its declared descriptive ceiling?",
        },
        "required_human_record": {
            "human_decision_gate_id": "HDG-RULES-V1-SOURCE-SCIENCE-REVIEW",
            "review_scope": ["F01", "F02", "F03", "F04", "F06"],
            "status": "PENDING_DOMAIN_REVIEW",
            "recording_authority": "Existing repository source-grounding review packet; this smoke creates no new approval workflow.",
        },
        "forbidden_claims": [
            "Neither route establishes scientific support.",
            "The X-EISD route does not establish numeric equivalence, shared population, or independent validation.",
            "The HSP90 route does not establish kinetics, equilibrium population, free energy, pathway, mechanism, or mutation effect.",
        ],
    }


def _report(human_packet: Mapping[str, Any]) -> str:
    paper = human_packet["primary_paper_question"]
    hsp90 = human_packet["companion_operator_control"]
    return (
        "# Exposed end-to-end smoke test\n\n"
        "The existing Lincoff X-EISD paper-derived question was replayed through a "
        "recorded answer-blind Planner selection, deterministic admission, the exact "
        "local attestation/direct-evaluation route, and the current Stage-2 reducer. "
        "The companion HSP90 Planner selection was admitted to the exact case-bound "
        "Operator route, which generated a fresh receipt and EvidenceResult before "
        "the same RuleInstance was reevaluated.\n\n"
        "| Input | Selected track | Route outcome | Human-facing disposition |\n"
        "| --- | --- | --- | --- |\n"
        f"| X-EISD paper-derived relation | {paper['selected_track']} | {paper['route_disposition']} | {paper['terminal_disposition']} |\n"
        f"| HSP90 same-packet control | {hsp90['selected_track']} | {hsp90['route_disposition']} | {hsp90['terminal_disposition']} |\n\n"
        "Both outputs remain `NOT_EVALUATED` scientifically. The next action is one "
        "named F01/F02/F03/F04/F06 source-science review, not another model run, "
        "Rule expansion, or Operator expansion.\n"
    )


def run_exposed_end_to_end_smoke(*, output_dir: Path) -> dict[str, Any]:
    """Run the fixed paper-question-to-human-review development smoke path."""

    repo_root = _repo_root()
    output_dir = _prepare_output_dir(output_dir)
    paper_question = _paper_question(repo_root)
    bound_cases = {
        case_key: materialize_and_bind_exposed_case(case_key=case_key, repo_root=repo_root)
        for case_key in ("xeisd", "hsp90")
    }
    for case_key, case_artifacts in bound_cases.items():
        _write_json(
            output_dir / "rules" / f"{case_key}_pre_agent_rule_selection.json",
            case_artifacts["pre_agent_rule_selection"],
        )
        _write_json(output_dir / "agent" / case_key / "planner_packet.json", case_artifacts["planner_packet"])
        _write_json(output_dir / "agent" / case_key / "materialization.json", case_artifacts["materialization"])
        _write_json(output_dir / "agent" / case_key / "evaluation.json", case_artifacts["evaluation"])
        _write_json(output_dir / "tracks" / f"{case_key}_route_binding.json", case_artifacts["route_binding"])
    _write_json(output_dir / "inputs" / "xeisd_paper_question.json", paper_question)

    # The Planner only proposes.  Existing deterministic code owns the actual
    # attestation/Operator execution and writes fresh evidence receipts.
    reference_demo = run_reference_demo(output_dir=output_dir / "reference_demo")
    fresh_routes = _bind_fresh_route_artifacts(
        output_dir=output_dir,
        bindings={
            case_key: artifacts["route_binding"]
            for case_key, artifacts in bound_cases.items()
        },
    )
    human_packet = _human_decision_packet(
        paper_question=paper_question,
        fresh_routes=fresh_routes,
    )
    manifest = {
        "schema_version": SMOKE_SCHEMA_VERSION,
        "run_id": SMOKE_RUN_ID,
        "run_kind": "EXACT_TWO_CASE_EXPOSED_DEVELOPMENT_SMOKE",
        "primary_input": "Lincoff X-EISD paper-derived development question",
        "companion_control": "HSP90 case-bound Operator closure",
        "recorded_agent_run": _RECORDED_RUN,
        "live_model_calls": 0,
        "agent_model_transport_invocations": 0,
        "external_network_accessed": False,
        "credential_reads": 0,
        "external_spend": 0,
        "reference_demo_manifest": "reference_demo/run_manifest.json",
        "human_decision_packet": "human_decision_packet.json",
        "scientific_disposition": "NOT_EVALUATED",
        "boundary": "Replays existing exact routes only. It does not parse a paper, retrieve free text, validate source science, generalize the route, or produce a scientific conclusion.",
    }
    summary = {
        "schema_version": SMOKE_SCHEMA_VERSION,
        "run_id": SMOKE_RUN_ID,
        "status": "SUCCEEDED",
        "paper_question_terminal_disposition": fresh_routes["xeisd"]["stage2_terminal_disposition"],
        "hsp90_control_terminal_disposition": fresh_routes["hsp90"]["stage2_terminal_disposition"],
        "scientific_support_packets": 0,
        "scientific_disposition": "NOT_EVALUATED",
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "next_action": "Named human/domain source-science review for F01/F02/F03/F04/F06.",
    }
    _write_json(output_dir / "human_decision_packet.json", human_packet)
    _write_json(output_dir / "run_manifest.json", manifest)
    _write_json(output_dir / "run_summary.json", summary)
    (output_dir / "report.md").write_text(_report(human_packet), encoding="utf-8")
    return {
        "manifest": manifest,
        "summary": summary,
        "human_decision_packet": human_packet,
        "reference_demo": reference_demo,
        "output_dir": str(output_dir),
    }
