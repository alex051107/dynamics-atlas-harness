"""One-case execution boundary for the exposed development capsule.

This module composes the causal primitives already implemented by
``exposed_paper_blind_capsule_v1``.  It adds no scientific method and computes no
terminal scientific verdict.  The default registry contains only the repository's
HSP90 and ADK exposed-development packets and their recorded proposals.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from copy import deepcopy
from pathlib import Path
from typing import Any

from . import exposed_paper_blind_capsule_v1 as capsule
from .proposal_provenance_v1 import (
    CALLER_SUPPLIED_IN_MEMORY,
    RECORDED_PROPOSAL_REPLAY,
    ProposalProvenanceV1Error,
    build_proposal_provenance_v1,
    canonical_json_sha256,
)


REPO_ROOT = Path(__file__).resolve().parents[2]

# Packet selection is data-driven.  Extending the runner requires an explicitly
# curated repository packet and proposal pair; the execution code has no
# protein-name branch.
_CASE_PACKET_REGISTRY: dict[str, dict[str, Path]] = {
    case_id: {
        "packet": Path(spec["packet"]),
        "profile_proposal": Path(spec["profiler_proposal"]),
        "planner_proposal": Path(spec["planner_proposal"]),
    }
    for case_id, spec in capsule._CASE_SPECS.items()
}

# These aliases deliberately reuse the capsule's reviewed card and executor
# registries rather than restating either scientific action here.
_ACTION_CARD_SPECS: Sequence[Mapping[str, Any]] = capsule._ACTION_CARD_SPECS


class CaseRunnerV1Error(ValueError):
    """Raised when a case run loses freshness, scope, or evidence linkage."""


RuleReevaluator = Callable[[Mapping[str, Any], Mapping[str, Any]], Mapping[str, Any]]


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CaseRunnerV1Error(f"NONEMPTY_STRING_REQUIRED:{label}")
    return value.strip()


def _repository_file(path: Path, label: str) -> Path:
    candidate = path.resolve()
    try:
        candidate.relative_to(REPO_ROOT.resolve())
    except ValueError as error:
        raise CaseRunnerV1Error(f"REPOSITORY_INPUT_REQUIRED:{label}") from error
    if not candidate.is_file():
        raise CaseRunnerV1Error(f"REPOSITORY_INPUT_UNAVAILABLE:{label}")
    return candidate


def _relative_repository_path(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def _action_card_case_index() -> dict[str, str]:
    index: dict[str, str] = {}
    for raw_spec in _ACTION_CARD_SPECS:
        if not isinstance(raw_spec, Mapping):
            raise CaseRunnerV1Error("ACTION_CARD_SPEC_MUST_BE_MAPPING")
        card_id = _require_string(raw_spec.get("card_id"), "action_card.card_id")
        case_id = _require_string(raw_spec.get("case_id"), "action_card.case_id")
        if card_id in index:
            raise CaseRunnerV1Error("DUPLICATE_ACTION_CARD_ID")
        index[card_id] = case_id
    return index


def _selected_card_ids(proposal: Mapping[str, Any]) -> list[str] | None:
    selected = proposal.get("selected_card_ids")
    if not isinstance(selected, list) or any(not isinstance(item, str) for item in selected):
        return None
    return list(selected)


def _preflight_selected_cards(
    *, case_id: str, planner_input: Mapping[str, Any], planner_proposal: Mapping[str, Any]
) -> None:
    """Reject known cross-case or stale selections before any action executes."""

    selected = _selected_card_ids(planner_proposal)
    if selected is None:
        return
    card_cases = _action_card_case_index()
    legal_ids = {
        card.get("card_id")
        for card in planner_input.get("legal_action_cards", [])
        if isinstance(card, Mapping) and isinstance(card.get("card_id"), str)
    }
    for card_id in selected:
        registered_case = card_cases.get(card_id)
        if registered_case is None:
            raise CaseRunnerV1Error("SELECTED_ACTION_CARD_UNKNOWN")
        if registered_case != case_id:
            raise CaseRunnerV1Error("SELECTED_ACTION_CARD_CROSS_CASE")
        if card_id not in legal_ids:
            raise CaseRunnerV1Error("SELECTED_ACTION_CARD_NOT_FRESH")


def _assert_descriptive_evidence_has_no_rule_effect(evidence: Mapping[str, Any]) -> None:
    if evidence.get("affected_rule_instance_id") is not None:
        raise CaseRunnerV1Error("DESCRIPTIVE_EVIDENCE_LINKED_ACTIVE_RULE")
    if evidence.get("active_rule_effect") is not None:
        raise CaseRunnerV1Error("DESCRIPTIVE_EVIDENCE_ATTEMPTED_ACTIVE_RULE_EFFECT")
    if evidence.get("contract_status") == "PASS" or evidence.get("rule_status") == "PASS":
        raise CaseRunnerV1Error("DESCRIPTIVE_EVIDENCE_CANNOT_FORGE_RULE_PASS")
    result = evidence.get("descriptive_result")
    if not isinstance(result, Mapping):
        raise CaseRunnerV1Error("DESCRIPTIVE_EVIDENCE_RESULT_REQUIRED")
    if result.get("rule_effect") != "NO_ACTIVE_RULE_EFFECT":
        raise CaseRunnerV1Error("DESCRIPTIVE_EVIDENCE_ATTEMPTED_ACTIVE_RULE_EFFECT")
    if result.get("affected_rule_instance_id") is not None:
        raise CaseRunnerV1Error("DESCRIPTIVE_EVIDENCE_LINKED_ACTIVE_RULE")
    if result.get("contract_status") == "PASS" or result.get("rule_status") == "PASS":
        raise CaseRunnerV1Error("DESCRIPTIVE_EVIDENCE_CANNOT_FORGE_RULE_PASS")


def _rule_instance_identity(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return the complete identity that a reevaluator is forbidden to change."""

    target = result.get("target")
    if not isinstance(target, Mapping):
        raise CaseRunnerV1Error("RULE_INSTANCE_TARGET_REQUIRED")
    return {
        "rule_instance_id": _require_string(
            result.get("rule_instance_id"), "rule_result.rule_instance_id"
        ),
        "runtime_subrule_id": _require_string(
            result.get("runtime_subrule_id"), "rule_result.runtime_subrule_id"
        ),
        "target": deepcopy(dict(target)),
    }

def reevaluate_explicitly_linked_rule_results(
    *,
    case_id: str,
    before_rule_results: Sequence[Mapping[str, Any]],
    evidence_results: Sequence[Mapping[str, Any]],
    reevaluators: Mapping[str, RuleReevaluator] | None = None,
) -> dict[str, Any]:
    """Apply validated evidence only to its explicit same-RuleInstance target.

    A case-specific reevaluator remains responsible for validating an active
    EvidenceResult against its frozen Evaluation Contract.  This function enforces
    attachment scope: descriptive evidence changes nothing, active evidence must
    name one current RuleInstance, and the reevaluator may return only that same ID.
    """

    normalized_case_id = _require_string(case_id, "case_id")
    before = [deepcopy(dict(item)) for item in before_rule_results]
    by_id: dict[str, dict[str, Any]] = {}
    positions: dict[str, int] = {}
    for position, result in enumerate(before):
        rule_id = _require_string(result.get("rule_instance_id"), "rule_result.rule_instance_id")
        if rule_id in by_id:
            raise CaseRunnerV1Error("DUPLICATE_RULE_INSTANCE_ID")
        by_id[rule_id] = result
        positions[rule_id] = position

    after = deepcopy(before)
    applied: set[str] = set()
    active_evidence_result_ids: set[str] = set()
    links: list[dict[str, Any]] = []
    available_reevaluators = dict(reevaluators or {})
    for raw_evidence in evidence_results:
        if not isinstance(raw_evidence, Mapping):
            raise CaseRunnerV1Error("EVIDENCE_RESULT_MUST_BE_MAPPING")
        evidence = deepcopy(dict(raw_evidence))
        evidence_case_id = evidence.get("case_id")
        if evidence_case_id is not None and evidence_case_id != normalized_case_id:
            raise CaseRunnerV1Error("EVIDENCE_RESULT_CROSS_CASE")

        if evidence.get("rule_effect") == "NO_ACTIVE_RULE_EFFECT":
            _assert_descriptive_evidence_has_no_rule_effect(evidence)
            continue

        if (
            evidence.get("rule_effect") != "ACTIVE_RULE_EFFECT"
            and evidence.get("active_rule_effect") != "ACTIVE_RULE_EFFECT"
        ):
            raise CaseRunnerV1Error("ACTIVE_EVIDENCE_EFFECT_MARKER_REQUIRED")

        affected_id = _require_string(
            evidence.get("affected_rule_instance_id"),
            "evidence_result.affected_rule_instance_id",
        )
        evidence_result_id = _require_string(
            evidence.get("evidence_result_id"), "evidence_result.evidence_result_id"
        )
        if evidence_result_id in active_evidence_result_ids:
            raise CaseRunnerV1Error("DUPLICATE_ACTIVE_EVIDENCE_RESULT_ID")
        active_evidence_result_ids.add(evidence_result_id)
        if affected_id not in by_id:
            raise CaseRunnerV1Error("EVIDENCE_RESULT_AFFECTED_RULE_NOT_CURRENT")
        if affected_id in applied:
            raise CaseRunnerV1Error("MULTIPLE_EVIDENCE_RESULTS_FOR_RULE_INSTANCE")
        reevaluator = available_reevaluators.get(affected_id)
        if reevaluator is None:
            raise CaseRunnerV1Error("NO_REEVALUATOR_FOR_AFFECTED_RULE_INSTANCE")
        reevaluated = reevaluator(deepcopy(by_id[affected_id]), deepcopy(evidence))
        if not isinstance(reevaluated, Mapping):
            raise CaseRunnerV1Error("REEVALUATOR_MUST_RETURN_RULE_RESULT")
        reevaluated_result = deepcopy(dict(reevaluated))
        if reevaluated_result.get("rule_instance_id") != affected_id:
            raise CaseRunnerV1Error("REEVALUATOR_CHANGED_RULE_INSTANCE_ID")
        if _rule_instance_identity(reevaluated_result) != _rule_instance_identity(
            by_id[affected_id]
        ):
            raise CaseRunnerV1Error("REEVALUATOR_CHANGED_RULE_INSTANCE_IDENTITY")
        if reevaluated_result == by_id[affected_id]:
            raise CaseRunnerV1Error("ACTIVE_EVIDENCE_REEVALUATION_MUST_CHANGE_RULE_RESULT")
        after[positions[affected_id]] = reevaluated_result
        applied.add(affected_id)
        links.append(
            {
                "affected_rule_instance_id": affected_id,
                "evidence_result_id": evidence_result_id,
                "before_status": by_id[affected_id].get("status"),
                "after_status": reevaluated_result.get("status"),
                "same_rule_instance": True,
            }
        )

    for rule_id, position in positions.items():
        if rule_id not in applied and after[position] != before[position]:
            raise CaseRunnerV1Error("UNEFFECTED_RULE_INSTANCE_CHANGED")
    return {
        "schema_version": "case-runner-rule-reevaluation/v1",
        "case_id": normalized_case_id,
        "before_rule_results": before,
        "after_rule_results": after,
        "reevaluated_rule_instance_ids": sorted(applied),
        "evidence_links": sorted(links, key=lambda item: item["affected_rule_instance_id"]),
        "boundary": (
            "Only an explicitly linked, contract-validated EvidenceResult may be "
            "reevaluated, and only its same RuleInstance may change."
        ),
    }


def _write_run_artifacts(
    output_root: Path,
    manifest: Mapping[str, Any],
    input_snapshots: Mapping[str, Mapping[str, Any]],
) -> None:
    proposal_provenance = manifest["proposal_provenance"]
    capsule._write_json(
        output_root / "profiler_proposal_provenance.json",
        proposal_provenance["profiler"],
    )
    capsule._write_json(
        output_root / "planner_proposal_provenance.json",
        proposal_provenance["planner"],
    )
    capsule._write_json(output_root / "fresh_rule_state.json", manifest["fresh_rule_state"])
    capsule._write_json(output_root / "planner_visible_input.json", manifest["planner_visible_input"])
    capsule._write_json(output_root / "planner_authorization.json", manifest["authorization"])
    capsule._write_json(output_root / "selected_action_execution.json", manifest["action_execution"])
    capsule._write_json(output_root / "rule_reevaluation.json", manifest["rule_reevaluation"])
    for relative_path, snapshot in input_snapshots.items():
        capsule._write_json(output_root / relative_path, snapshot)
    for evidence in manifest["action_execution"]["evidence_results"]:
        card_id = _require_string(evidence.get("card_id"), "evidence_result.card_id")
        capsule._write_json(output_root / "actions" / card_id / "evidence_result.json", evidence)
    capsule._write_json(output_root / "case_run_manifest_v1.json", manifest)


def run_case_v1(
    *,
    case_id: str,
    output_dir: str | Path,
    profile_proposal: Mapping[str, Any] | None = None,
    planner_proposal: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Run one registered exposed-development case into an empty directory.

    Mapping overrides are in-memory replay/test seams only.  They cannot add packet
    paths, cards, executors, credentials, or network transport.
    """

    normalized_case_id = _require_string(case_id, "case_id")
    spec = _CASE_PACKET_REGISTRY.get(normalized_case_id)
    if spec is None:
        raise CaseRunnerV1Error("CASE_NOT_IN_EXPOSED_DEVELOPMENT_REGISTRY")

    try:
        output_root = capsule.create_clean_output_root(output_dir)
        packet_path = _repository_file(spec["packet"], "public_case_packet")
        profile_path = _repository_file(spec["profile_proposal"], "profile_proposal")
        planner_path = _repository_file(spec["planner_proposal"], "planner_proposal")
        packet = capsule._read_json(packet_path)
        if packet.get("case_id") != normalized_case_id:
            raise CaseRunnerV1Error("PUBLIC_PACKET_CASE_ID_MISMATCH")
        profiler_visible_input = capsule.build_agent_visible_packet(packet_path)
        capsule._assert_agent_visible_boundary(profiler_visible_input)
        profile = (
            deepcopy(dict(profile_proposal))
            if profile_proposal is not None
            else capsule._read_json(profile_path)
        )
        proposal = (
            deepcopy(dict(planner_proposal))
            if planner_proposal is not None
            else capsule._read_json(planner_path)
        )

        rules_bundle = capsule.load_rules_v1_bundle(capsule.RULES_ROOT)
        fresh_state = capsule._active_rule_results_for_proposal(
            packet_path=packet_path,
            proposal=profile,
            rules_bundle=rules_bundle,
        )
        obligations = capsule._development_obligations(
            normalized_case_id, fresh_state["rule_results"]
        )
        asset_verification = capsule.verify_declared_asset_hashes(packet_path)
        planner_input = capsule.materialize_planner_input(
            case_id=normalized_case_id,
            active_rule_results=fresh_state["rule_results"],
            development_items=obligations,
            action_card_specs=_ACTION_CARD_SPECS,
            asset_verification=asset_verification,
        )
        capsule._validate_planner_input(planner_input, case_id=normalized_case_id)
        _preflight_selected_cards(
            case_id=normalized_case_id,
            planner_input=planner_input,
            planner_proposal=proposal,
        )
        admission = capsule.validate_planner_proposal(planner_input, proposal)
        selected = list(admission["selected_card_ids"])
        if admission["decision"] == "SELECT_ACTIONS" and len(selected) != 1:
            raise CaseRunnerV1Error("CASE_RUNNER_REQUIRES_EXACTLY_ONE_SELECTED_CARD")
        if admission["decision"] == "ABSTAIN_NO_ACTION" and selected:
            raise CaseRunnerV1Error("CASE_RUNNER_ABSTAIN_MUST_EXECUTE_ZERO_ACTIONS")

        execution = capsule._execute_selected_actions(
            case_id=normalized_case_id,
            planner_input=planner_input,
            planner_admission=admission,
        )
        if execution.get("selected_card_ids") != selected:
            raise CaseRunnerV1Error("EXECUTION_SELECTION_DIVERGED_FROM_AUTHORIZATION")
        evidence_results = execution.get("evidence_results")
        if not isinstance(evidence_results, list) or len(evidence_results) != len(selected):
            raise CaseRunnerV1Error("EXECUTED_ACTION_COUNT_DIVERGED_FROM_AUTHORIZATION")
        reevaluation = reevaluate_explicitly_linked_rule_results(
            case_id=normalized_case_id,
            before_rule_results=fresh_state["rule_results"],
            evidence_results=evidence_results,
            reevaluators={},
        )
        profiler_mode = (
            CALLER_SUPPLIED_IN_MEMORY
            if profile_proposal is not None
            else RECORDED_PROPOSAL_REPLAY
        )
        planner_mode = (
            CALLER_SUPPLIED_IN_MEMORY
            if planner_proposal is not None
            else RECORDED_PROPOSAL_REPLAY
        )
        profiler_provenance = build_proposal_provenance_v1(
            role="PROFILER",
            mode=profiler_mode,
            visible_input=profiler_visible_input,
            parsed_proposal=profile,
            contract_evaluator="validate_agent_proposal",
            contract_admission_evaluation=fresh_state["admission"],
            source_path=(
                None
                if profile_proposal is not None
                else _relative_repository_path(profile_path)
            ),
        )
        planner_provenance = build_proposal_provenance_v1(
            role="PLANNER",
            mode=planner_mode,
            visible_input=planner_input,
            parsed_proposal=proposal,
            contract_evaluator="validate_planner_proposal",
            contract_admission_evaluation=admission,
            source_path=(
                None
                if planner_proposal is not None
                else _relative_repository_path(planner_path)
            ),
        )
    except (capsule.ExposedPaperBlindCapsuleError, ProposalProvenanceV1Error) as error:
        raise CaseRunnerV1Error(str(error)) from error

    authorization = {
        "schema_version": "case-runner-authorization/v1",
        "case_id": normalized_case_id,
        "status": (
            "AUTHORIZED_EXACTLY_ONE_SELECTED_CARD"
            if selected
            else "AUTHORIZED_ABSTENTION_ZERO_ACTIONS"
        ),
        "selected_card_ids": selected,
        "executed_action_count": len(evidence_results),
        "boundary": "Authorized selected card IDs are the sole execution input.",
    }
    claim_boundary = packet.get("platform_authority_envelope", {}).get("claim_boundary")
    if not isinstance(claim_boundary, Mapping):
        raise CaseRunnerV1Error("PUBLIC_PACKET_CLAIM_BOUNDARY_REQUIRED")
    manifest = {
        "schema_version": "dynamics-atlas-case-run/v1",
        "case_id": normalized_case_id,
        "run_scope": "EXPOSED_DEVELOPMENT_ONLY",
        "research_question": packet.get("research_question"),
        "claim_boundary": deepcopy(dict(claim_boundary)),
        "input_provenance": {
            "public_case_packet": _relative_repository_path(packet_path),
            "profile_proposal": (
                None
                if profile_proposal is not None
                else _relative_repository_path(profile_path)
            ),
            "planner_proposal": (
                None
                if planner_proposal is not None
                else _relative_repository_path(planner_path)
            ),
            "profile_mode": profiler_mode,
            "planner_mode": planner_mode,
            "snapshot_artifacts": {
                "public_case_packet": {
                    "path": "inputs/public_case_packet.json",
                    "canonical_sha256": canonical_json_sha256(packet),
                },
                "profiler_visible_input": {
                    "path": "inputs/profiler_visible_input.json",
                    "canonical_sha256": canonical_json_sha256(profiler_visible_input),
                },
                "profile_proposal": {
                    "path": "inputs/profile_proposal.json",
                    "canonical_sha256": canonical_json_sha256(profile),
                },
                "planner_proposal": {
                    "path": "inputs/planner_proposal.json",
                    "canonical_sha256": canonical_json_sha256(proposal),
                },
                "planner_visible_input": {
                    "path": "planner_visible_input.json",
                    "canonical_sha256": canonical_json_sha256(planner_input),
                },
            },
        },
        "proposal_provenance": {
            "profiler": profiler_provenance,
            "planner": planner_provenance,
        },
        "fresh_rule_state": {
            "admission": deepcopy(fresh_state["admission"]),
            "projected_casegraph": deepcopy(fresh_state["projected_casegraph"]),
            "rule_results": deepcopy(fresh_state["rule_results"]),
            "development_obligations": deepcopy(obligations),
            "asset_verification": deepcopy(asset_verification),
        },
        "planner_visible_input": deepcopy(planner_input),
        "planner_admission": deepcopy(admission),
        "authorization": authorization,
        "action_execution": deepcopy(execution),
        "rule_reevaluation": reevaluation,
        "terminal_scientific_state": "NOT_CALCULATED_BY_CASE_RUNNER",
        "scientific_disposition": "NOT_EVALUATED",
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "network_accessed": False,
        "credentials_accessed": False,
        "external_model_transport": False,
        "artifact_paths": [
            "inputs/public_case_packet.json",
            "inputs/profiler_visible_input.json",
            "inputs/profile_proposal.json",
            "inputs/planner_proposal.json",
            "profiler_proposal_provenance.json",
            "planner_proposal_provenance.json",
            "fresh_rule_state.json",
            "planner_visible_input.json",
            "planner_authorization.json",
            "selected_action_execution.json",
            "rule_reevaluation.json",
            *(
                [f"actions/{selected[0]}/evidence_result.json"]
                if selected
                else []
            ),
            "case_run_manifest_v1.json",
        ],
        "boundary": (
            "This runner records deterministic exposed-development behavior only. "
            "It does not compute a terminal verdict, source-science approval, broad "
            "HSP90 closure, ADK dynamics portability, or Agent effectiveness."
        ),
    }
    _write_run_artifacts(
        output_root,
        manifest,
        {
            "inputs/public_case_packet.json": packet,
            "inputs/profiler_visible_input.json": profiler_visible_input,
            "inputs/profile_proposal.json": profile,
            "inputs/planner_proposal.json": proposal,
        },
    )
    return manifest
