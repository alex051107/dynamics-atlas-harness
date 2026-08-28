#!/usr/bin/env python3
"""Replay the two recorded Planner selections with a platform-owned envelope.

This is intentionally a historical, deterministic replay.  It never constructs a
model provider, sends transport, invokes an Operator, or overwrites the recorded
model outputs that supplied the card selections.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from dynamics_atlas_harness.live_agent_exposed_v1 import (
    build_recorded_run_manifest,
    evaluate_planner_proposal,
    load_json_object,
    materialize_planner_card_selection,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT_ROOT = REPO_ROOT / "agent_experiments" / "v1"
RECORDED_RUN = (
    EXPERIMENT_ROOT / "recorded" / "qwen2_5_1_5b_20260826_prompt_remediation1"
)
CASE_KEYS = ("xeisd", "hsp90")


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def relative(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def new_output_directory(relative_path: str) -> Path:
    candidate = Path(relative_path)
    if candidate.is_absolute():
        raise SystemExit("output directory must be repository-relative")
    output_dir = (REPO_ROOT / candidate).resolve()
    allowed_root = (EXPERIMENT_ROOT / "derived_replays").resolve()
    if not output_dir.is_relative_to(allowed_root):
        raise SystemExit("output directory must be under agent_experiments/v1/derived_replays")
    if output_dir.exists():
        raise SystemExit("output directory already exists; refusing to overwrite replay evidence")
    output_dir.mkdir(parents=True)
    return output_dir


def card_selection_from_recorded(proposal: dict[str, Any]) -> tuple[dict[str, Any] | None, str | None]:
    """Project the two model-owned fields from one already-verified historical reply."""

    actions = proposal.get("proposed_actions")
    if not isinstance(actions, list) or not actions:
        return None, "RECORDED_PLANNER_ACTIONS_MISSING"
    selected_card_ids: list[str] = []
    rationales: dict[str, str] = {}
    for action in actions:
        card_id = action.get("card_id") if isinstance(action, dict) else None
        rationale = action.get("rationale") if isinstance(action, dict) else None
        if not isinstance(card_id, str) or not card_id or not isinstance(rationale, str) or not rationale.strip():
            return None, "RECORDED_PLANNER_SELECTION_INVALID"
        if card_id in rationales:
            return None, "RECORDED_PLANNER_CARD_ID_DUPLICATE"
        selected_card_ids.append(card_id)
        rationales[card_id] = rationale
    return {"selected_card_ids": selected_card_ids, "rationales": rationales}, None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        required=True,
        help="New repository-relative directory under agent_experiments/v1/derived_replays.",
    )
    args = parser.parse_args()
    output_dir = new_output_directory(args.output_dir)
    source_manifest = build_recorded_run_manifest(RECORDED_RUN, EXPERIMENT_ROOT, REPO_ROOT)
    planner_reference = load_json_object(
        EXPERIMENT_ROOT / "sealed_references" / "planner_reference_v1.json"
    )
    case_summaries: list[dict[str, Any]] = []
    all_pass = True
    for case_key in CASE_KEYS:
        packet_path = EXPERIMENT_ROOT / "workspaces" / f"{case_key}_planner" / "input.json"
        source_dir = RECORDED_RUN / f"{case_key}_planner"
        packet = load_json_object(packet_path)
        source_integrity = source_manifest["unit_integrity"][f"{case_key}_planner"]
        integrity_pass = not any(
            isinstance(check, dict) and check.get("status") == "FAIL"
            for check in source_integrity.values()
        )
        selection, extraction_error = card_selection_from_recorded(
            load_json_object(source_dir / "proposal.json")
        )
        materialization = materialize_planner_card_selection(selection, packet)
        proposal = materialization.get("canonical_proposal")
        evaluation = (
            evaluate_planner_proposal(proposal, packet, planner_reference, REPO_ROOT)
            if isinstance(proposal, dict)
            else {
                "schema_version": "planner-evaluation/v2",
                "case_id": packet.get("case_id"),
                "status": "NOT_RUN_MATERIALIZATION_FAILED",
                "reason_codes": materialization.get("reason_codes", []),
            }
        )
        case_dir = output_dir / f"{case_key}_planner"
        case_dir.mkdir()
        write_json(case_dir / "materialization.json", materialization)
        write_json(case_dir / "evaluation.json", evaluation)
        evaluation_status = (
            evaluation.get("sealed_reference_and_authorization_view", {}).get("status")
            if isinstance(evaluation, dict)
            else None
        )
        case_pass = (
            integrity_pass
            and extraction_error is None
            and materialization["status"] == "PASS"
            and evaluation_status == "PASS"
        )
        all_pass = all_pass and case_pass
        case_summaries.append(
            {
                "case_key": case_key,
                "case_id": packet.get("case_id"),
                "status": "PASS" if case_pass else "FAIL",
                "source_integrity": source_integrity,
                "extraction_status": "PASS" if extraction_error is None else "FAIL",
                "extraction_reason": extraction_error,
                "materialization_status": materialization["status"],
                "evaluation_status": evaluation_status,
                "artifact_directory": relative(case_dir),
            }
        )
    receipt = {
        "schema_version": "planner-card-selection-normalization-replay/v1",
        "status": "PASS" if all_pass else "FAIL",
        "replay_kind": "RECORDED_SELECTION_EXTRACTION_AND_PLATFORM_NORMALIZATION_REPLAY",
        "source_recorded_run": relative(RECORDED_RUN),
        "historical_live_model_calls_in_source_run": 2,
        "replay_model_transport_invocations": 0,
        "registered_operator_calls": 0,
        "execution_performed": False,
        "scientific_disposition": "NOT_EVALUATED",
        "cases": case_summaries,
        "claim_boundary": "The model-owned fields are card IDs and rationales only; the platform copies case, route action, target, operator ID, no-execution, and scientific-disposition fields from the fixed packet. This replay does not validate a new live Planner contract, Agent value, scientific support, or execution authorization beyond the existing no-execution evaluator.",
    }
    write_json(output_dir / "run_receipt.json", receipt)
    print(f"{relative(output_dir)}: {receipt['status']}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
