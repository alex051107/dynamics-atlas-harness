"""Artifact-only read model for exposed Dynamics Atlas development cases.

``build_case_view`` accepts either a recorded capsule case directory or a
``case_runner_v1`` run directory.  It validates the artifact links it follows and
copies recorded values into a UI-friendly read model.  It performs no Rule
evaluation, action execution, or terminal scientific-state calculation.
"""

from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Any

from .proposal_provenance_v1 import canonical_json_sha256


REPO_ROOT = Path(__file__).resolve().parents[2]


class CaseViewIntegrityError(ValueError):
    """Raised when a CaseView cannot faithfully project its artifact graph."""

    def __init__(self, code: str, detail: str | None = None) -> None:
        self.code = code
        self.detail = detail
        message = code if detail is None else f"{code}:{detail}"
        super().__init__(message)


def unavailable(reason: str) -> dict[str, str]:
    """Return the explicit sentinel used for optional absent artifacts."""

    return {"availability": "UNAVAILABLE", "reason": reason}


@dataclass(frozen=True)
class CaseView:
    """Validated projection of recorded case/run artifacts.

    Collections remain JSON-shaped because the sole consumer is a static HTML
    renderer.  ``to_dict`` returns a deep copy so callers cannot mutate this read
    model and mistake that mutation for canonical scientific state.
    """

    schema_version: str
    case_id: str
    artifact_kind: str
    artifact_root_name: str
    integrity_status: str
    question: Any
    current_gate: Any
    claim_ceiling: Any
    sources_and_locators: Any
    agent_proposal: Any
    admitted_facts: Any
    rule_instances: list[dict[str, Any]]
    rule_results: list[dict[str, Any]]
    unresolved_obligations: list[dict[str, Any]]
    legal_action_cards: list[dict[str, Any]]
    planner_proposal: Any
    authorization: Any
    executed_actions: Any
    receipts: Any
    descriptive_evidence_no_active_rule_effect: list[dict[str, Any]]
    active_rule_evidence: list[dict[str, Any]]
    exact_control_regression: Any
    before_after_rule_result_links: Any
    conclusion_packet: Any
    human_review_state: Any
    terminal_scientific_state: Any
    boundary: str

    def to_dict(self) -> dict[str, Any]:
        return deepcopy(asdict(self))


def _read_object(path: Path, label: str, *, required: bool = True) -> dict[str, Any] | None:
    if not path.is_file():
        if required:
            raise CaseViewIntegrityError("REQUIRED_ARTIFACT_MISSING", label)
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise CaseViewIntegrityError("ARTIFACT_MALFORMED", label) from error
    if not isinstance(value, dict):
        raise CaseViewIntegrityError("ARTIFACT_OBJECT_REQUIRED", label)
    return value


def _require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise CaseViewIntegrityError("OBJECT_REQUIRED", label)
    return value


def _require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        raise CaseViewIntegrityError("LIST_REQUIRED", label)
    return value


def _require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CaseViewIntegrityError("NONEMPTY_STRING_REQUIRED", label)
    return value.strip()


def _assert_case_id(value: Any, case_id: str, label: str) -> None:
    if value != case_id:
        raise CaseViewIntegrityError("CROSS_CASE_ARTIFACT", label)


def _rule_identity(result: dict[str, Any], label: str) -> dict[str, Any]:
    rule_instance_id = _require_string(result.get("rule_instance_id"), f"{label}.rule_instance_id")
    runtime_subrule_id = _require_string(
        result.get("runtime_subrule_id"), f"{label}.runtime_subrule_id"
    )
    target = _require_object(result.get("target"), f"{label}.target")
    _require_string(target.get("kind"), f"{label}.target.kind")
    _require_string(target.get("id"), f"{label}.target.id")
    return {
        "rule_instance_id": rule_instance_id,
        "runtime_subrule_id": runtime_subrule_id,
        "target": deepcopy(target),
    }


def _rule_index(results: Any, label: str) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    raw_results = _require_list(results, label)
    normalized: list[dict[str, Any]] = []
    by_id: dict[str, dict[str, Any]] = {}
    for position, raw in enumerate(raw_results):
        result = _require_object(raw, f"{label}[{position}]")
        identity = _rule_identity(result, f"{label}[{position}]")
        rule_id = identity["rule_instance_id"]
        if rule_id in by_id:
            raise CaseViewIntegrityError("DUPLICATE_RULE_INSTANCE_ID", rule_id)
        copied = deepcopy(result)
        normalized.append(copied)
        by_id[rule_id] = copied
    return normalized, by_id


def _safe_repository_reference(raw_path: Any, label: str) -> Path:
    relative = _require_string(raw_path, label)
    posix = PurePosixPath(relative)
    if posix.is_absolute() or ".." in posix.parts:
        raise CaseViewIntegrityError("UNSAFE_ARTIFACT_REFERENCE", label)
    candidate = (REPO_ROOT / Path(*posix.parts)).resolve()
    try:
        candidate.relative_to(REPO_ROOT.resolve())
    except ValueError as error:
        raise CaseViewIntegrityError("UNSAFE_ARTIFACT_REFERENCE", label) from error
    if not candidate.is_file():
        raise CaseViewIntegrityError("STALE_ARTIFACT_REFERENCE", label)
    return candidate


def _proposal_from_receipt(receipt: dict[str, Any], case_id: str, label: str) -> dict[str, Any]:
    path = _safe_repository_reference(receipt.get("recorded_proposal_path"), f"{label}.path")
    expected_sha = _require_string(receipt.get("recorded_proposal_sha256"), f"{label}.sha256")
    observed_sha = hashlib.sha256(path.read_bytes()).hexdigest()
    if observed_sha != expected_sha:
        raise CaseViewIntegrityError("STALE_ARTIFACT_REFERENCE_HASH", label)
    proposal = _read_object(path, label)
    assert proposal is not None
    _assert_case_id(proposal.get("case_id"), case_id, label)
    return proposal


def _input_snapshot(
    *,
    loaded: dict[str, dict[str, Any]],
    input_provenance: dict[str, Any],
    snapshot_name: str,
    case_id: str,
) -> dict[str, Any]:
    records = _require_object(
        input_provenance.get("snapshot_artifacts"), "input_provenance.snapshot_artifacts"
    )
    record = _require_object(
        records.get(snapshot_name), f"input_provenance.snapshot_artifacts.{snapshot_name}"
    )
    path = _require_string(record.get("path"), f"snapshot_artifacts.{snapshot_name}.path")
    value = loaded.get(path)
    if value is None:
        raise CaseViewIntegrityError("REQUIRED_INPUT_SNAPSHOT_MISSING", snapshot_name)
    expected_sha = _require_string(
        record.get("canonical_sha256"),
        f"snapshot_artifacts.{snapshot_name}.canonical_sha256",
    )
    if canonical_json_sha256(value) != expected_sha:
        raise CaseViewIntegrityError("STALE_INPUT_SNAPSHOT_HASH", snapshot_name)
    if "case_id" in value:
        _assert_case_id(value.get("case_id"), case_id, snapshot_name)
    return deepcopy(value)


def _verify_proposal_receipt(
    *,
    receipt: dict[str, Any],
    case_id: str,
    role: str,
    mode: Any,
    source_path: Any,
    visible_input: dict[str, Any],
    parsed_proposal: dict[str, Any],
    admission_evaluation: dict[str, Any],
) -> None:
    _assert_case_id(receipt.get("case_id"), case_id, f"{role}.proposal_provenance")
    if receipt.get("role") != role:
        raise CaseViewIntegrityError("PROPOSAL_RECEIPT_ROLE_MISMATCH", role)
    if receipt.get("mode") != mode:
        raise CaseViewIntegrityError("PROPOSAL_RECEIPT_MODE_MISMATCH", role)
    if receipt.get("source_path") != source_path:
        raise CaseViewIntegrityError("PROPOSAL_RECEIPT_SOURCE_PATH_MISMATCH", role)
    checks = (
        (receipt.get("visible_input"), visible_input, "visible_input"),
        (receipt.get("parsed_proposal"), parsed_proposal, "parsed_proposal"),
        (
            receipt.get("contract_admission_evaluation"),
            admission_evaluation,
            "contract_admission_evaluation",
        ),
    )
    for raw_record, value, label in checks:
        record = _require_object(raw_record, f"{role}.{label}")
        expected = _require_string(
            record.get("canonical_sha256"), f"{role}.{label}.canonical_sha256"
        )
        if canonical_json_sha256(value) != expected:
            raise CaseViewIntegrityError("STALE_PROPOSAL_RECEIPT_HASH", f"{role}.{label}")


def _evidence_lanes(evidence_results: Any, case_id: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    descriptive: list[dict[str, Any]] = []
    active: list[dict[str, Any]] = []
    for position, raw in enumerate(_require_list(evidence_results, "evidence_results")):
        evidence = _require_object(raw, f"evidence_results[{position}]")
        if "case_id" in evidence:
            _assert_case_id(evidence.get("case_id"), case_id, f"evidence_results[{position}]")
        descriptive_result = evidence.get("descriptive_result")
        nested_effect = (
            descriptive_result.get("rule_effect")
            if isinstance(descriptive_result, dict)
            else None
        )
        is_descriptive = (
            evidence.get("rule_effect") == "NO_ACTIVE_RULE_EFFECT"
            or nested_effect == "NO_ACTIVE_RULE_EFFECT"
            or evidence.get("action_kind") == "DESCRIPTIVE_ANALYSIS_ONLY"
        )
        is_active = (
            evidence.get("rule_effect") == "ACTIVE_RULE_EFFECT"
            or evidence.get("active_rule_effect") == "ACTIVE_RULE_EFFECT"
        )
        if is_descriptive and is_active:
            raise CaseViewIntegrityError("EVIDENCE_EFFECT_MARKERS_CONFLICT")
        if is_descriptive:
            if evidence.get("affected_rule_instance_id") is not None:
                raise CaseViewIntegrityError("DESCRIPTIVE_EVIDENCE_LINKED_ACTIVE_RULE")
            if evidence.get("active_rule_effect") not in (None, "NO_ACTIVE_RULE_EFFECT"):
                raise CaseViewIntegrityError("DESCRIPTIVE_EVIDENCE_HAS_ACTIVE_RULE_EFFECT")
            descriptive.append(deepcopy(evidence))
        elif is_active:
            _require_string(
                evidence.get("evidence_result_id"),
                f"evidence_results[{position}].evidence_result_id",
            )
            _require_string(
                evidence.get("affected_rule_instance_id"),
                f"evidence_results[{position}].affected_rule_instance_id",
            )
            active.append(deepcopy(evidence))
        else:
            raise CaseViewIntegrityError("EVIDENCE_EFFECT_CLASSIFICATION_UNKNOWN")
    return descriptive, active


def _validated_reevaluation_links(
    *,
    reevaluation: dict[str, Any],
    before_by_id: dict[str, dict[str, Any]],
    after_by_id: dict[str, dict[str, Any]],
    active_evidence: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    for rule_id in before_by_id:
        if _rule_identity(before_by_id[rule_id], "before_rule_result") != _rule_identity(
            after_by_id[rule_id], "after_rule_result"
        ):
            raise CaseViewIntegrityError("RULE_INSTANCE_IDENTITY_CHANGED", rule_id)

    changed_ids = {
        rule_id for rule_id in before_by_id if before_by_id[rule_id] != after_by_id[rule_id]
    }
    raw_reevaluated = _require_list(
        reevaluation.get("reevaluated_rule_instance_ids"),
        "rule_reevaluation.reevaluated_rule_instance_ids",
    )
    reevaluated_ids = [
        _require_string(value, "reevaluated_rule_instance_id") for value in raw_reevaluated
    ]
    if len(reevaluated_ids) != len(set(reevaluated_ids)):
        raise CaseViewIntegrityError("DUPLICATE_REEVALUATED_RULE_INSTANCE_ID")
    if set(reevaluated_ids) != changed_ids:
        raise CaseViewIntegrityError("REEVALUATED_RULE_CHANGE_SET_MISMATCH")

    active_by_id: dict[str, dict[str, Any]] = {}
    active_targets: dict[str, str] = {}
    for evidence in active_evidence:
        evidence_id = _require_string(
            evidence.get("evidence_result_id"), "active_evidence.evidence_result_id"
        )
        affected = _require_string(
            evidence.get("affected_rule_instance_id"),
            "active_evidence.affected_rule_instance_id",
        )
        if evidence_id in active_by_id:
            raise CaseViewIntegrityError("DUPLICATE_ACTIVE_EVIDENCE_RESULT_ID", evidence_id)
        if affected in active_targets.values():
            raise CaseViewIntegrityError("MULTIPLE_ACTIVE_EVIDENCE_FOR_RULE_INSTANCE", affected)
        active_by_id[evidence_id] = evidence
        active_targets[evidence_id] = affected

    links: list[dict[str, Any]] = []
    linked_rule_ids: set[str] = set()
    linked_evidence_ids: set[str] = set()
    for position, raw in enumerate(
        _require_list(reevaluation.get("evidence_links"), "rule_reevaluation.evidence_links")
    ):
        link = _require_object(raw, f"evidence_links[{position}]")
        affected = _require_string(
            link.get("affected_rule_instance_id"),
            f"evidence_links[{position}].affected_rule_instance_id",
        )
        evidence_id = _require_string(
            link.get("evidence_result_id"), f"evidence_links[{position}].evidence_result_id"
        )
        if affected in linked_rule_ids or evidence_id in linked_evidence_ids:
            raise CaseViewIntegrityError("DUPLICATE_RULE_REEVALUATION_LINK")
        if affected not in before_by_id or affected not in after_by_id:
            raise CaseViewIntegrityError("STALE_RULE_RESULT_LINK", affected)
        if active_targets.get(evidence_id) != affected:
            raise CaseViewIntegrityError("ACTIVE_EVIDENCE_LINK_MISMATCH", evidence_id)
        if link.get("same_rule_instance") is not True:
            raise CaseViewIntegrityError("SAME_RULE_INSTANCE_ATTESTATION_REQUIRED", affected)
        if link.get("before_status") != before_by_id[affected].get("status"):
            raise CaseViewIntegrityError("REEVALUATION_BEFORE_STATUS_MISMATCH", affected)
        if link.get("after_status") != after_by_id[affected].get("status"):
            raise CaseViewIntegrityError("REEVALUATION_AFTER_STATUS_MISMATCH", affected)
        linked_rule_ids.add(affected)
        linked_evidence_ids.add(evidence_id)
        links.append(deepcopy(link))

    if linked_rule_ids != changed_ids or linked_evidence_ids != set(active_by_id):
        raise CaseViewIntegrityError("ACTIVE_EVIDENCE_REEVALUATION_LINK_SET_MISMATCH")
    return links


def _selected_card_consistency(
    *,
    case_id: str,
    planner_input: dict[str, Any],
    planner_admission: dict[str, Any],
    execution: dict[str, Any],
) -> None:
    _assert_case_id(planner_input.get("case_id"), case_id, "planner_visible_input")
    _assert_case_id(planner_admission.get("case_id"), case_id, "planner_admission")
    _assert_case_id(execution.get("case_id"), case_id, "selected_action_execution")
    legal_cards = _require_list(planner_input.get("legal_action_cards"), "legal_action_cards")
    legal_ids: set[str] = set()
    for position, raw in enumerate(legal_cards):
        card = _require_object(raw, f"legal_action_cards[{position}]")
        _assert_case_id(card.get("case_id"), case_id, f"legal_action_cards[{position}]")
        legal_ids.add(_require_string(card.get("card_id"), f"legal_action_cards[{position}].card_id"))
    admitted = _require_list(planner_admission.get("selected_card_ids"), "planner_admission.selected_card_ids")
    executed = _require_list(execution.get("selected_card_ids"), "execution.selected_card_ids")
    if admitted != executed:
        raise CaseViewIntegrityError("STALE_SELECTED_CARD_REFERENCE")
    if any(card_id not in legal_ids for card_id in admitted):
        raise CaseViewIntegrityError("STALE_LEGAL_ACTION_CARD_REFERENCE")
    evidence = _require_list(execution.get("evidence_results"), "execution.evidence_results")
    evidence_card_ids = [
        _require_string(_require_object(item, "evidence_result").get("card_id"), "evidence_result.card_id")
        for item in evidence
    ]
    if admitted != evidence_card_ids:
        raise CaseViewIntegrityError("STALE_EXECUTED_ACTION_REFERENCE")


def _build_capsule_case_view(root: Path) -> CaseView:
    artifacts = {
        name: _read_object(root / f"{name}.json", name)
        for name in (
            "human_decision_packet",
            "agent_visible_input",
            "arm_b_recorded_profile_rules",
            "planner_visible_input",
            "planner_proposal_admission",
            "arm_c_selected_public_actions",
            "profiler_proposal_provenance",
            "planner_proposal_provenance",
            "unresolved_obligation_classification",
            "asset_identity_verification",
        )
    }
    packet = artifacts["human_decision_packet"]
    assert packet is not None
    case_id = _require_string(packet.get("case_id"), "human_decision_packet.case_id")
    for name in (
        "agent_visible_input",
        "planner_visible_input",
        "planner_proposal_admission",
        "unresolved_obligation_classification",
        "asset_identity_verification",
    ):
        artifact = artifacts[name]
        assert artifact is not None
        _assert_case_id(artifact.get("case_id"), case_id, name)

    profile_rules = artifacts["arm_b_recorded_profile_rules"]
    planner_input = artifacts["planner_visible_input"]
    planner_admission = artifacts["planner_proposal_admission"]
    selected = artifacts["arm_c_selected_public_actions"]
    unresolved = artifacts["unresolved_obligation_classification"]
    profiler_receipt = artifacts["profiler_proposal_provenance"]
    planner_receipt = artifacts["planner_proposal_provenance"]
    assert all(
        value is not None
        for value in (
            profile_rules,
            planner_input,
            planner_admission,
            selected,
            unresolved,
            profiler_receipt,
            planner_receipt,
        )
    )
    assert isinstance(profile_rules, dict)
    assert isinstance(planner_input, dict)
    assert isinstance(planner_admission, dict)
    assert isinstance(selected, dict)
    assert isinstance(unresolved, dict)
    assert isinstance(profiler_receipt, dict)
    assert isinstance(planner_receipt, dict)

    profile_admission = _require_object(profile_rules.get("admission"), "profile_admission")
    profile_proposal = _require_object(profile_admission.get("proposal"), "profile_proposal")
    _assert_case_id(profile_proposal.get("case_id"), case_id, "profile_proposal")
    projected = _require_object(profile_rules.get("projected_casegraph"), "projected_casegraph")
    projected_case = _require_object(projected.get("case"), "projected_casegraph.case")
    _assert_case_id(projected_case.get("case_id"), case_id, "projected_casegraph.case")

    selected_admission = _require_object(selected.get("planner_admission"), "selected.planner_admission")
    selected_execution = _require_object(selected.get("selected_execution"), "selected.selected_execution")
    _assert_case_id(selected.get("case_id"), case_id, "arm_c_selected_public_actions")
    if selected_admission != planner_admission:
        raise CaseViewIntegrityError("STALE_PLANNER_ADMISSION_REFERENCE")
    _selected_card_consistency(
        case_id=case_id,
        planner_input=planner_input,
        planner_admission=planner_admission,
        execution=selected_execution,
    )

    rich_rules, rich_by_id = _rule_index(profile_rules.get("rule_results"), "profile_rule_results")
    compact_rules, compact_by_id = _rule_index(packet.get("active_rule_results"), "active_rule_results")
    unresolved_rules, unresolved_by_id = _rule_index(
        unresolved.get("active_rule_results"), "unresolved_classification.active_rule_results"
    )
    if set(rich_by_id) != set(compact_by_id) or set(compact_by_id) != set(unresolved_by_id):
        raise CaseViewIntegrityError("STALE_RULE_RESULT_REFERENCE")
    for rule_id, compact in compact_by_id.items():
        rich = rich_by_id[rule_id]
        unresolved_copy = unresolved_by_id[rule_id]
        for field in ("runtime_subrule_id", "status", "target", "reason_codes"):
            if compact.get(field) != rich.get(field) or compact.get(field) != unresolved_copy.get(field):
                raise CaseViewIntegrityError("STALE_RULE_RESULT_REFERENCE", rule_id)

    profile_raw = _proposal_from_receipt(profiler_receipt, case_id, "profiler_proposal")
    planner_raw = _proposal_from_receipt(planner_receipt, case_id, "planner_proposal")
    if profile_raw != profile_proposal:
        raise CaseViewIntegrityError("STALE_PROFILE_PROPOSAL_REFERENCE")
    descriptive, active = _evidence_lanes(selected_execution.get("evidence_results"), case_id)
    if descriptive != packet.get("descriptive_evidence_results_no_active_rule_effect"):
        raise CaseViewIntegrityError("STALE_EVIDENCE_RESULT_REFERENCE")

    exact_file = _read_object(root / "existing_exact_hsp90_control_regression.json", "exact_control", required=False)
    embedded_exact = packet.get("existing_exact_hsp90_control_regression")
    if exact_file is not None and embedded_exact != exact_file:
        raise CaseViewIntegrityError("STALE_EXACT_CONTROL_REFERENCE")
    if not isinstance(embedded_exact, dict) or embedded_exact.get("status") == "NOT_RUN_IN_THIS_CAPSULE_INVOCATION":
        exact_control: Any = unavailable("No exact control regression belongs to this case artifact.")
    else:
        exact_control = deepcopy(embedded_exact)

    sources = _require_list(artifacts["agent_visible_input"].get("source_materials"), "source_materials")  # type: ignore[union-attr]
    obligations = _require_list(unresolved.get("development_obligations"), "development_obligations")
    legal_cards = _require_list(planner_input.get("legal_action_cards"), "legal_action_cards")
    rule_instances = [_rule_identity(result, "rule_result") for result in rich_rules]
    return CaseView(
        schema_version="dynamics-atlas-case-view/v1",
        case_id=case_id,
        artifact_kind="RECORDED_EXPOSED_CAPSULE_CASE",
        artifact_root_name=root.name,
        integrity_status="PASS",
        question=packet.get("requested_claim", artifacts["agent_visible_input"].get("research_question")),  # type: ignore[union-attr]
        current_gate=packet.get("source_science_review_status", "UNKNOWN"),
        claim_ceiling={
            "requested_claim": packet.get("requested_claim", "UNKNOWN"),
            "forbidden_claims": deepcopy(packet.get("forbidden_claims", [])),
        },
        sources_and_locators=deepcopy(sources),
        agent_proposal={
            "kind": "AGENT_PROPOSAL",
            "proposal": profile_raw,
            "provenance": deepcopy(profiler_receipt),
        },
        admitted_facts={
            "kind": "PLATFORM_ADMITTED_FACT",
            "admission": deepcopy(profile_admission),
            "projected_casegraph": deepcopy(projected),
        },
        rule_instances=rule_instances,
        rule_results=rich_rules,
        unresolved_obligations=deepcopy(obligations),
        legal_action_cards=deepcopy(legal_cards),
        planner_proposal={
            "kind": "AGENT_PROPOSAL",
            "proposal": planner_raw,
            "provenance": deepcopy(planner_receipt),
        },
        authorization=deepcopy(planner_admission),
        executed_actions=deepcopy(selected_execution),
        receipts={
            "profiler_provenance": deepcopy(profiler_receipt),
            "planner_provenance": deepcopy(planner_receipt),
            "asset_identity_verification": deepcopy(artifacts["asset_identity_verification"]),
        },
        descriptive_evidence_no_active_rule_effect=descriptive,
        active_rule_evidence=active,
        exact_control_regression=exact_control,
        before_after_rule_result_links=unavailable(
            "The recorded capsule exposes no broad same-Rule before/after evidence link."
        ),
        conclusion_packet={"kind": "CONCLUSION_PACKET", "artifact": deepcopy(packet)},
        human_review_state={
            "kind": "HUMAN_REVIEW",
            "status": packet.get("source_science_review_status", "UNKNOWN"),
            "items": deepcopy(packet.get("human_review_items", [])),
        },
        terminal_scientific_state=packet.get("terminal_disposition", "UNKNOWN"),
        boundary=(
            "This view copies the recorded capsule state. It does not recalculate a "
            "terminal disposition or promote descriptive/exact-control evidence."
        ),
    )


_RUN_REQUIRED_ARTIFACTS = (
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
    "case_run_manifest_v1.json",
)


def _manifest_artifact_paths(root: Path, manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw_paths = _require_list(manifest.get("artifact_paths"), "manifest.artifact_paths")
    if len(raw_paths) != len(set(raw_paths)):
        raise CaseViewIntegrityError("DUPLICATE_ARTIFACT_REFERENCE")
    path_set: set[str] = set()
    loaded: dict[str, dict[str, Any]] = {}
    for position, raw_path in enumerate(raw_paths):
        relative = _require_string(raw_path, f"manifest.artifact_paths[{position}]")
        posix = PurePosixPath(relative)
        if posix.is_absolute() or ".." in posix.parts:
            raise CaseViewIntegrityError("UNSAFE_ARTIFACT_REFERENCE", relative)
        path_set.add(posix.as_posix())
        path = (root / Path(*posix.parts)).resolve()
        try:
            path.relative_to(root.resolve())
        except ValueError as error:
            raise CaseViewIntegrityError("UNSAFE_ARTIFACT_REFERENCE", relative) from error
        value = _read_object(path, relative)
        assert value is not None
        loaded[posix.as_posix()] = value
    missing = sorted(set(_RUN_REQUIRED_ARTIFACTS) - path_set)
    if missing:
        raise CaseViewIntegrityError("REQUIRED_ARTIFACT_REFERENCE_MISSING", ",".join(missing))
    return loaded


def _build_case_run_view(root: Path) -> CaseView:
    manifest = _read_object(root / "case_run_manifest_v1.json", "case_run_manifest_v1")
    assert manifest is not None
    case_id = _require_string(manifest.get("case_id"), "manifest.case_id")
    loaded = _manifest_artifact_paths(root, manifest)
    profiler_provenance = loaded["profiler_proposal_provenance.json"]
    planner_provenance = loaded["planner_proposal_provenance.json"]
    fresh = loaded["fresh_rule_state.json"]
    planner_input = loaded["planner_visible_input.json"]
    authorization = loaded["planner_authorization.json"]
    execution = loaded["selected_action_execution.json"]
    reevaluation = loaded["rule_reevaluation.json"]
    for label, artifact in (
        ("fresh_rule_state", fresh),
        ("profiler_proposal_provenance", profiler_provenance),
        ("planner_proposal_provenance", planner_provenance),
        ("planner_visible_input", planner_input),
        ("planner_authorization", authorization),
        ("selected_action_execution", execution),
        ("rule_reevaluation", reevaluation),
    ):
        if "case_id" in artifact:
            _assert_case_id(artifact.get("case_id"), case_id, label)

    expected_copies = (
        (manifest.get("fresh_rule_state"), fresh, "fresh_rule_state"),
        (manifest.get("planner_visible_input"), planner_input, "planner_visible_input"),
        (manifest.get("authorization"), authorization, "planner_authorization"),
        (manifest.get("action_execution"), execution, "selected_action_execution"),
        (manifest.get("rule_reevaluation"), reevaluation, "rule_reevaluation"),
    )
    for embedded, standalone, label in expected_copies:
        if embedded != standalone:
            raise CaseViewIntegrityError("STALE_EMBEDDED_ARTIFACT_REFERENCE", label)
    proposal_provenance = _require_object(
        manifest.get("proposal_provenance"), "manifest.proposal_provenance"
    )
    if proposal_provenance.get("profiler") != profiler_provenance:
        raise CaseViewIntegrityError(
            "STALE_EMBEDDED_ARTIFACT_REFERENCE", "profiler_proposal_provenance"
        )
    if proposal_provenance.get("planner") != planner_provenance:
        raise CaseViewIntegrityError(
            "STALE_EMBEDDED_ARTIFACT_REFERENCE", "planner_proposal_provenance"
        )

    planner_admission = _require_object(manifest.get("planner_admission"), "manifest.planner_admission")
    _assert_case_id(planner_admission.get("case_id"), case_id, "planner_admission")
    _selected_card_consistency(
        case_id=case_id,
        planner_input=planner_input,
        planner_admission=planner_admission,
        execution=execution,
    )

    before, before_by_id = _rule_index(reevaluation.get("before_rule_results"), "before_rule_results")
    after, after_by_id = _rule_index(reevaluation.get("after_rule_results"), "after_rule_results")
    fresh_results, fresh_by_id = _rule_index(fresh.get("rule_results"), "fresh_rule_state.rule_results")
    if set(before_by_id) != set(after_by_id) or set(before_by_id) != set(fresh_by_id):
        raise CaseViewIntegrityError("STALE_RULE_RESULT_REFERENCE")
    for rule_id in before_by_id:
        if before_by_id[rule_id] != fresh_by_id[rule_id]:
            raise CaseViewIntegrityError("STALE_RULE_RESULT_REFERENCE", rule_id)

    descriptive, active = _evidence_lanes(execution.get("evidence_results"), case_id)
    links = _validated_reevaluation_links(
        reevaluation=reevaluation,
        before_by_id=before_by_id,
        after_by_id=after_by_id,
        active_evidence=active,
    )
    selected_ids = _require_list(execution.get("selected_card_ids"), "execution.selected_card_ids")
    for card_id, evidence in zip(selected_ids, _require_list(execution.get("evidence_results"), "evidence_results")):
        relative = f"actions/{card_id}/evidence_result.json"
        if loaded.get(relative) != evidence:
            raise CaseViewIntegrityError("STALE_EVIDENCE_RESULT_REFERENCE", relative)

    input_provenance = _require_object(manifest.get("input_provenance"), "input_provenance")
    public_packet = _input_snapshot(
        loaded=loaded,
        input_provenance=input_provenance,
        snapshot_name="public_case_packet",
        case_id=case_id,
    )
    profiler_visible_input = _input_snapshot(
        loaded=loaded,
        input_provenance=input_provenance,
        snapshot_name="profiler_visible_input",
        case_id=case_id,
    )
    profile_proposal = _input_snapshot(
        loaded=loaded,
        input_provenance=input_provenance,
        snapshot_name="profile_proposal",
        case_id=case_id,
    )
    planner_proposal = _input_snapshot(
        loaded=loaded,
        input_provenance=input_provenance,
        snapshot_name="planner_proposal",
        case_id=case_id,
    )
    planner_input_snapshot = _input_snapshot(
        loaded=loaded,
        input_provenance=input_provenance,
        snapshot_name="planner_visible_input",
        case_id=case_id,
    )
    if planner_input_snapshot != planner_input:
        raise CaseViewIntegrityError("STALE_PLANNER_VISIBLE_INPUT_SNAPSHOT")
    sources = deepcopy(public_packet.get("source_materials", []))
    admission = _require_object(fresh.get("admission"), "fresh_rule_state.admission")
    _verify_proposal_receipt(
        receipt=profiler_provenance,
        case_id=case_id,
        role="PROFILER",
        mode=input_provenance.get("profile_mode"),
        source_path=input_provenance.get("profile_proposal"),
        visible_input=profiler_visible_input,
        parsed_proposal=profile_proposal,
        admission_evaluation=admission,
    )
    _verify_proposal_receipt(
        receipt=planner_provenance,
        case_id=case_id,
        role="PLANNER",
        mode=input_provenance.get("planner_mode"),
        source_path=input_provenance.get("planner_proposal"),
        visible_input=planner_input,
        parsed_proposal=planner_proposal,
        admission_evaluation=planner_admission,
    )
    projected = _require_object(fresh.get("projected_casegraph"), "fresh_rule_state.projected_casegraph")
    projected_case = _require_object(projected.get("case"), "projected_casegraph.case")
    _assert_case_id(projected_case.get("case_id"), case_id, "projected_casegraph.case")
    obligations = _require_list(fresh.get("development_obligations"), "development_obligations")
    legal_cards = _require_list(planner_input.get("legal_action_cards"), "legal_action_cards")
    rule_instances = [_rule_identity(result, "rule_result") for result in after]
    return CaseView(
        schema_version="dynamics-atlas-case-view/v1",
        case_id=case_id,
        artifact_kind="CASE_RUNNER_V1_RUN",
        artifact_root_name=root.name,
        integrity_status="PASS",
        question=manifest.get("research_question", "UNKNOWN"),
        current_gate=manifest.get("source_science_review_status", "UNKNOWN"),
        claim_ceiling=deepcopy(manifest.get("claim_boundary", "UNKNOWN")),
        sources_and_locators=sources,
        agent_proposal={
            "kind": "AGENT_PROPOSAL",
            "proposal": profile_proposal,
            "admission": deepcopy(admission),
            "provenance": deepcopy(profiler_provenance),
        },
        admitted_facts={
            "kind": "PLATFORM_ADMITTED_FACT",
            "admission": deepcopy(admission),
            "projected_casegraph": deepcopy(projected),
        },
        rule_instances=rule_instances,
        rule_results=after,
        unresolved_obligations=deepcopy(obligations),
        legal_action_cards=deepcopy(legal_cards),
        planner_proposal={
            "kind": "AGENT_PROPOSAL",
            "proposal": planner_proposal,
            "provenance": deepcopy(planner_provenance),
        },
        authorization=deepcopy(authorization),
        executed_actions=deepcopy(execution),
        receipts={
            "input_provenance": deepcopy(input_provenance),
            "profiler_proposal_provenance": deepcopy(profiler_provenance),
            "planner_proposal_provenance": deepcopy(planner_provenance),
            "authorization": deepcopy(authorization),
            "artifact_paths": deepcopy(manifest.get("artifact_paths")),
        },
        descriptive_evidence_no_active_rule_effect=descriptive,
        active_rule_evidence=active,
        exact_control_regression=unavailable(
            "case_runner_v1 does not synthesize or import an exact-control sidecar."
        ),
        before_after_rule_result_links=deepcopy(links),
        conclusion_packet=unavailable(
            "case_runner_v1 does not calculate a ConclusionPacket or terminal verdict."
        ),
        human_review_state={
            "kind": "HUMAN_REVIEW",
            "status": manifest.get("source_science_review_status", "UNKNOWN"),
        },
        terminal_scientific_state=manifest.get("terminal_scientific_state", "UNKNOWN"),
        boundary=_require_string(manifest.get("boundary"), "manifest.boundary"),
    )


def build_case_view(case_or_run_root: str | Path) -> CaseView:
    """Project a recorded case/run directory into a validated ``CaseView``.

    The function recognizes the artifact set, validates required artifacts and
    their same-case/fresh references, and leaves optional absence explicit.  It
    never evaluates Rules or computes a conclusion.
    """

    root = Path(case_or_run_root)
    if not root.is_dir():
        raise CaseViewIntegrityError("CASE_OR_RUN_ROOT_UNAVAILABLE", root.name or ".")
    is_run = (root / "case_run_manifest_v1.json").is_file()
    is_capsule_case = (root / "human_decision_packet.json").is_file()
    if is_run and is_capsule_case:
        raise CaseViewIntegrityError("AMBIGUOUS_CASE_OR_RUN_ROOT", root.name)
    if is_run:
        return _build_case_run_view(root)
    if is_capsule_case:
        return _build_capsule_case_view(root)
    raise CaseViewIntegrityError("CASE_OR_RUN_ROOT_UNRECOGNIZED", root.name)
