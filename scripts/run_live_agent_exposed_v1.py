#!/usr/bin/env python3
"""Run the bounded, tool-less Live-Agent exposed-case comparison.

The runner calls a local model at most once per role/case, with one JSON repair at
most. It writes receipts even when a proposal is rejected. It deliberately stops
after separate Profiler and Planner evaluation; it does not perform an end-to-end
route execution.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from dynamics_atlas_harness.live_agent_exposed_v1 import (
    LocalModelCallError,
    LocalOllamaJsonProvider,
    PLANNER_ROLE,
    PROFILER_ROLE,
    evaluate_planner_proposal,
    evaluate_profiler_proposal,
    load_json_object,
    model_visible_workspace_report,
    sha256_text,
    validate_model_visible_packet,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT_ROOT = REPO_ROOT / "agent_experiments" / "v1"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def failure_evaluation(*, case_id: str, role: str, receipt: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "agent-call-failure-evaluation/v1",
        "case_id": case_id,
        "role": role,
        "status": "FAIL",
        "reason_codes": list(receipt.get("reason_codes", [])) or ["MODEL_CALL_FAILED"],
        "free_form": {"status": "NOT_EVALUATED"},
        "vocabulary_assisted": {"status": "NOT_EVALUATED"},
        "bounded_harness": {"status": "NOT_EVALUATED"},
    }


def failure_layers(evaluation: dict[str, Any]) -> list[str]:
    layers: list[str] = []
    for key, label in (
        ("free_form", "FREE_FORM"),
        ("vocabulary_assisted", "TYPED_CONTRACT"),
        ("bounded_harness", "BOUNDED_HARNESS"),
    ):
        view = evaluation.get(key)
        if isinstance(view, dict) and view.get("status") == "FAIL":
            layers.append(label)
    if evaluation.get("status") == "FAIL":
        layers.append("MODEL_CALL")
    return layers


def hard_gate_report(unit_results: list[dict[str, Any]], workspace_report: dict[str, Any]) -> dict[str, Any]:
    violations: list[dict[str, Any]] = []
    if workspace_report.get("status") != "PASS":
        violations.append({"gate": "ANSWER_LEAKAGE", "detail": "MODEL_VISIBLE_WORKSPACE"})
    for unit in unit_results:
        evaluation = unit["evaluation"]
        serialized = json.dumps(evaluation, ensure_ascii=False)
        if "ANSWER_BEARING_KEY:" in serialized or "FORBIDDEN_TEXT:" in serialized:
            violations.append({"gate": "ANSWER_LEAKAGE", "unit": unit["unit_id"]})
        if "CRITICAL_SOURCE_FACT_MISMATCH" in serialized or "CRITICAL_EDGE_FACT_MISMATCH" in serialized:
            violations.append({"gate": "CRITICAL_SCIENTIFIC_FACT", "unit": unit["unit_id"]})
        if "REQUIRED_UNKNOWN_MISSING" in serialized or "MISSING_OR_FABRICATED_UNKNOWN" in serialized:
            violations.append({"gate": "UNKNOWN_REQUIRED", "unit": unit["unit_id"]})
        authorization = (
            evaluation.get("bounded_harness", {}).get("deterministic_authorization", {})
            if isinstance(evaluation.get("bounded_harness"), dict)
            else {}
        )
        if authorization and authorization.get("registered_operator_calls") != 0:
            violations.append({"gate": "UNREGISTERED_OR_EXECUTED_OPERATOR", "unit": unit["unit_id"]})
        if "UNSAFE_SCIENTIFIC_DISPOSITION" in serialized:
            violations.append({"gate": "UNSAFE_CLAIM_UPGRADE", "unit": unit["unit_id"]})
    return {
        "schema_version": "live-agent-hard-gate-report/v1",
        "status": "PASS" if not violations else "FAIL",
        "violations": violations,
        "hard_gates": {
            "critical_scientific_fact_errors": 0
            if not any(item["gate"] == "CRITICAL_SCIENTIFIC_FACT" for item in violations)
            else len([item for item in violations if item["gate"] == "CRITICAL_SCIENTIFIC_FACT"]),
            "answer_leakage": 0
            if not any(item["gate"] == "ANSWER_LEAKAGE" for item in violations)
            else len([item for item in violations if item["gate"] == "ANSWER_LEAKAGE"]),
            "unregistered_operator_calls": 0
            if not any(item["gate"] == "UNREGISTERED_OR_EXECUTED_OPERATOR" for item in violations)
            else len([item for item in violations if item["gate"] == "UNREGISTERED_OR_EXECUTED_OPERATOR"]),
            "unsafe_claim_upgrades": 0
            if not any(item["gate"] == "UNSAFE_CLAIM_UPGRADE" for item in violations)
            else len([item for item in violations if item["gate"] == "UNSAFE_CLAIM_UPGRADE"]),
        },
    }


def comparison_markdown(unit_results: list[dict[str, Any]], hard_gates: dict[str, Any]) -> str:
    lines = [
        "# Live-Agent exposed-case comparison report",
        "",
        "The Profiler and Planner were evaluated separately. The Planner consumed the human canonical packet, not the Profiler proposal. No end-to-end execution ran.",
        "",
        "| Case | Role | Free-form | Vocabulary-assisted | Bounded harness | Failure layers |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for unit in unit_results:
        evaluation = unit["evaluation"]
        lines.append(
            "| {case} | {role} | {free} | {typed} | {bounded} | {layers} |".format(
                case=unit["case_key"],
                role=unit["role"],
                free=evaluation.get("free_form", {}).get("status", "NOT_EVALUATED"),
                typed=evaluation.get("vocabulary_assisted", {}).get("status", "NOT_EVALUATED"),
                bounded=evaluation.get("bounded_harness", {}).get("status", "NOT_EVALUATED"),
                layers=", ".join(failure_layers(evaluation)) or "none",
            )
        )
    lines.extend(
        [
            "",
            f"Hard gates: **{hard_gates['status']}**.",
            "",
            "The three columns assess the same recorded proposal at increasing deterministic controls; they are not independent model samples and no percentage metric is reported.",
            "",
            "Claim ceiling: this is a two-case exposed-development comparison only. It does not establish source-science validity, scientific support, Agent value, general Operator behavior, transfer, or held-out performance.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default="qwen2.5:1.5b")
    parser.add_argument("--endpoint", default="http://127.0.0.1:11434/api/generate")
    parser.add_argument("--timeout-seconds", type=int, default=90)
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Empty repository-relative directory for this one recorded run.",
    )
    args = parser.parse_args()

    output_dir = (REPO_ROOT / args.output_dir).resolve()
    if not output_dir.is_relative_to(REPO_ROOT):
        raise SystemExit("output directory must stay inside the repository")
    if output_dir.exists():
        raise SystemExit("output directory already exists; preserve the prior receipt")

    workspaces_root = EXPERIMENT_ROOT / "workspaces"
    workspace_report = model_visible_workspace_report(workspaces_root)
    output_dir.mkdir(parents=True)
    write_json(output_dir / "model_visible_workspace_report.json", workspace_report)
    if workspace_report["status"] != "PASS":
        write_json(
            output_dir / "run_receipt.json",
            {
                "schema_version": "live-agent-run-receipt/v1",
                "status": "BLOCKED",
                "reason_codes": workspace_report["reason_codes"],
                "live_model_calls": 0,
                "end_to_end": "NOT_RUN",
            },
        )
        return 2

    prompts = {
        PROFILER_ROLE: read_text(EXPERIMENT_ROOT / "prompts" / "profiler_v1.md"),
        PLANNER_ROLE: read_text(EXPERIMENT_ROOT / "prompts" / "planner_v1.md"),
    }
    provider = LocalOllamaJsonProvider(
        model=args.model,
        endpoint=args.endpoint,
        profiler_prompt=prompts[PROFILER_ROLE],
        planner_prompt=prompts[PLANNER_ROLE],
        timeout_seconds=args.timeout_seconds,
    )
    profiler_reference = load_json_object(
        EXPERIMENT_ROOT / "sealed_references" / "profiler_reference_v1.json"
    )
    planner_reference = load_json_object(
        EXPERIMENT_ROOT / "sealed_references" / "planner_reference_v1.json"
    )
    units = [
        ("xeisd_profiler", "xeisd", PROFILER_ROLE),
        ("hsp90_profiler", "hsp90", PROFILER_ROLE),
        ("xeisd_planner", "xeisd", PLANNER_ROLE),
        ("hsp90_planner", "hsp90", PLANNER_ROLE),
    ]
    unit_results: list[dict[str, Any]] = []
    for unit_id, case_key, role in units:
        packet = load_json_object(workspaces_root / unit_id / "input.json")
        packet_validation = validate_model_visible_packet(packet, role)
        unit_dir = output_dir / unit_id
        unit_dir.mkdir()
        write_json(unit_dir / "packet_validation.json", packet_validation)
        if packet_validation["status"] != "PASS":
            evaluation = failure_evaluation(
                case_id=packet.get("case_id", "UNKNOWN"),
                role=role,
                receipt=packet_validation,
            )
            write_json(unit_dir / "evaluation.json", evaluation)
            unit_results.append({"unit_id": unit_id, "case_key": case_key, "role": role, "evaluation": evaluation})
            continue
        try:
            proposal = (
                provider.propose_profile(packet)
                if role == PROFILER_ROLE
                else provider.propose(packet)
            )
        except LocalModelCallError:
            receipt = provider.last_receipt or {
                "status": "FAILED",
                "reason_codes": ["LOCAL_MODEL_UNRECORDED_FAILURE"],
            }
            evaluation = failure_evaluation(
                case_id=packet["case_id"], role=role, receipt=receipt
            )
            write_json(unit_dir / "model_call_receipt.json", receipt)
            write_json(unit_dir / "evaluation.json", evaluation)
            if provider.last_raw_response is not None:
                (unit_dir / "raw_response.txt").write_text(
                    provider.last_raw_response, encoding="utf-8"
                )
            unit_results.append({"unit_id": unit_id, "case_key": case_key, "role": role, "evaluation": evaluation})
            continue
        receipt = provider.last_receipt or {"status": "FAILED", "reason_codes": ["MISSING_RECEIPT"]}
        write_json(unit_dir / "model_call_receipt.json", receipt)
        write_json(unit_dir / "proposal.json", proposal)
        if provider.last_raw_response is not None:
            (unit_dir / "raw_response.txt").write_text(
                provider.last_raw_response, encoding="utf-8"
            )
        evaluation = (
            evaluate_profiler_proposal(proposal, packet, profiler_reference)
            if role == PROFILER_ROLE
            else evaluate_planner_proposal(proposal, packet, planner_reference, REPO_ROOT)
        )
        write_json(unit_dir / "evaluation.json", evaluation)
        unit_results.append({"unit_id": unit_id, "case_key": case_key, "role": role, "evaluation": evaluation})

    hard_gates = hard_gate_report(unit_results, workspace_report)
    write_json(output_dir / "hard_gate_report.json", hard_gates)
    (output_dir / "comparison_report.md").write_text(
        comparison_markdown(unit_results, hard_gates), encoding="utf-8"
    )
    call_count = sum(
        int(
            load_json_object(output_dir / item["unit_id"] / "model_call_receipt.json").get(
                "call_count", 0
            )
        )
        for item in unit_results
        if (output_dir / item["unit_id"] / "model_call_receipt.json").is_file()
    )
    write_json(
        output_dir / "run_receipt.json",
        {
            "schema_version": "live-agent-run-receipt/v1",
            "status": "COMPLETE_SAFE" if hard_gates["status"] == "PASS" else "COMPLETE_WITH_REJECTION_RECEIPTS",
            "model": args.model,
            "provider_id": provider.provider_id,
            "prompt_hashes": {role: sha256_text(prompt) for role, prompt in prompts.items()},
            "live_model_calls": call_count,
            "unit_count": len(unit_results),
            "hard_gates": hard_gates,
            "end_to_end": "NOT_RUN_SEPARATE_ARMS_ONLY",
            "scientific_disposition": "NOT_EVALUATED",
            "cost_status": "LOCAL_UNMETERED_NOT_ESTIMATED",
        },
    )
    return 0 if hard_gates["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
