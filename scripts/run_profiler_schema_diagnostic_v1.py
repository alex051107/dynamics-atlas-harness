#!/usr/bin/env python3
"""Run at most two schema-constrained, tool-less local Profiler calls.

The script is deliberately case-bound: one X-EISD packet and one HSP90 packet.
It does not construct a Planner request, invoke an Operator, or execute an
end-to-end route.  A failed metadata preflight or first transport attempt stops
the diagnostic without fallback, repair, prompt iteration, or a third call.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from dynamics_atlas_harness.live_agent_exposed_v1 import (
    LocalModelCallError,
    LocalOllamaJsonProvider,
    build_profiler_output_schema,
    evaluate_profiler_proposal,
    load_json_object,
    sha256_json,
    sha256_text,
    validate_model_visible_packet,
)


REPO_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT_ROOT = REPO_ROOT / "agent_experiments" / "v1"
WORKSPACES = EXPERIMENT_ROOT / "workspaces"
PROFILER_PROMPT_PATH = EXPERIMENT_ROOT / "prompts" / "profiler_v1.md"
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
    allowed_root = (EXPERIMENT_ROOT / "diagnostics").resolve()
    if not output_dir.is_relative_to(allowed_root):
        raise SystemExit("output directory must be under agent_experiments/v1/diagnostics")
    if output_dir.exists():
        raise SystemExit("output directory already exists; refusing to overwrite diagnostic evidence")
    output_dir.mkdir(parents=True)
    return output_dir


def case_packet(case_key: str) -> tuple[Path, dict[str, Any]]:
    path = WORKSPACES / f"{case_key}_profiler" / "input.json"
    return path, load_json_object(path)


def preflight_case(packet: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None]:
    packet_validation = validate_model_visible_packet(packet, "PROFILER")
    try:
        output_schema = build_profiler_output_schema(packet)
    except ValueError as exc:
        return (
            {
                "packet_validation": packet_validation,
                "schema_status": "FAIL",
                "reason_codes": [f"OUTPUT_SCHEMA_BUILD_FAILED:{type(exc).__name__}"],
            },
            None,
        )
    return (
        {
            "packet_validation": packet_validation,
            "schema_status": "PASS" if packet_validation["status"] == "PASS" else "FAIL",
            "reason_codes": []
            if packet_validation["status"] == "PASS"
            else list(packet_validation["reason_codes"]),
        },
        output_schema,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        required=True,
        help="New repository-relative directory under agent_experiments/v1/diagnostics.",
    )
    parser.add_argument("--model", default="qwen2.5:1.5b")
    parser.add_argument("--endpoint", default="http://127.0.0.1:11434/api/generate")
    parser.add_argument("--timeout-seconds", type=int, default=90)
    args = parser.parse_args()

    output_dir = new_output_directory(args.output_dir)
    profiler_prompt = PROFILER_PROMPT_PATH.read_text(encoding="utf-8")
    packets: dict[str, dict[str, Any]] = {}
    schemas: dict[str, dict[str, Any]] = {}
    preflights: dict[str, dict[str, Any]] = {}
    packet_ready = True
    for case_key in CASE_KEYS:
        packet_path, packet = case_packet(case_key)
        preflight, output_schema = preflight_case(packet)
        preflight["packet_path"] = relative(packet_path)
        preflight["packet_sha256"] = sha256_json(packet)
        preflight["schema_sha256"] = sha256_json(output_schema) if output_schema else None
        case_dir = output_dir / f"{case_key}_profiler"
        case_dir.mkdir()
        write_json(case_dir / "preflight.json", preflight)
        if output_schema is not None:
            write_json(case_dir / "output_schema.json", output_schema)
        packets[case_key] = packet
        preflights[case_key] = preflight
        if output_schema is None or preflight["schema_status"] != "PASS":
            packet_ready = False
        else:
            schemas[case_key] = output_schema

    provider = LocalOllamaJsonProvider(
        model=args.model,
        endpoint=args.endpoint,
        profiler_prompt=profiler_prompt,
        planner_prompt="PLANNER_NOT_EVALUATED_IN_PROFILER_SCHEMA_DIAGNOSTIC",
        timeout_seconds=args.timeout_seconds,
        allow_one_json_repair=False,
    )
    runtime_metadata = provider.runtime_metadata()
    write_json(output_dir / "runtime_metadata.json", runtime_metadata)
    if not packet_ready or runtime_metadata["status"] != "PASS":
        receipt = {
            "schema_version": "profiler-schema-diagnostic-run-receipt/v1",
            "status": "BLOCKED_PRECONDITION",
            "reason_codes": (
                ([] if packet_ready else ["MODEL_VISIBLE_PACKET_OR_SCHEMA_INVALID"])
                + ([] if runtime_metadata["status"] == "PASS" else runtime_metadata["reason_codes"])
            ),
            "role_scope": "PROFILER_SCHEMA_DIAGNOSTIC_ONLY",
            "planner_evaluation": "NOT_RUN",
            "end_to_end": "NOT_RUN",
            "scientific_disposition": "NOT_EVALUATED",
            "model_generation_requests_attempted": 0,
            "model_generation_calls_completed": 0,
            "registered_operator_calls": 0,
            "execution_performed": False,
            "prompt": {
                "path": relative(PROFILER_PROMPT_PATH),
                "sha256": sha256_text(profiler_prompt),
            },
            "runtime_metadata": runtime_metadata,
            "case_preflights": preflights,
        }
        write_json(output_dir / "run_receipt.json", receipt)
        print(f"{relative(output_dir)}: {receipt['status']}")
        return 2

    sealed_reference = load_json_object(
        EXPERIMENT_ROOT / "sealed_references" / "profiler_reference_v1.json"
    )
    case_summaries: list[dict[str, Any]] = []
    attempted = 0
    completed = 0
    stopped_reason: str | None = None
    for case_key in CASE_KEYS:
        packet = packets[case_key]
        output_schema = schemas[case_key]
        case_dir = output_dir / f"{case_key}_profiler"
        attempted += 1
        try:
            proposal = provider.propose_profile_schema_constrained(packet, output_schema)
        except LocalModelCallError as exc:
            stopped_reason = str(exc)
            if provider.last_raw_response is not None:
                (case_dir / "raw_response.txt").write_text(
                    provider.last_raw_response, encoding="utf-8"
                )
            receipt = dict(provider.last_receipt or {})
            receipt.update(
                {
                    "response_schema_sha256": sha256_json(output_schema),
                    "response_schema_path": "output_schema.json",
                    "seed": "NOT_SET",
                    "bounded_json_repair_attempted": False,
                    "diagnostic_boundary": "NO_FALLBACK_NO_RETRY_STOP_AFTER_FIRST_TRANSPORT_OR_PARSE_FAILURE",
                }
            )
            write_json(case_dir / "model_call_receipt.json", receipt)
            case_summaries.append(
                {
                    "case_key": case_key,
                    "case_id": packet.get("case_id"),
                    "status": "FAILED_AND_STOPPED",
                    "reason_code": stopped_reason,
                    "artifact_directory": relative(case_dir),
                }
            )
            break
        completed += 1
        raw_response = provider.last_raw_response
        if raw_response is None:
            raise RuntimeError("successful local provider call did not retain raw response")
        (case_dir / "raw_response.txt").write_text(raw_response, encoding="utf-8")
        write_json(case_dir / "proposal.json", proposal)
        receipt = dict(provider.last_receipt or {})
        receipt.update(
            {
                "response_schema_sha256": sha256_json(output_schema),
                "response_schema_path": "output_schema.json",
                "seed": "NOT_SET",
                "bounded_json_repair_attempted": False,
                "diagnostic_boundary": "ONE_SCHEMA_CONSTRAINED_TOOLLESS_PROFILER_CALL",
            }
        )
        write_json(case_dir / "model_call_receipt.json", receipt)
        evaluation = evaluate_profiler_proposal(proposal, packet, sealed_reference)
        write_json(case_dir / "evaluation.json", evaluation)
        case_summaries.append(
            {
                "case_key": case_key,
                "case_id": packet.get("case_id"),
                "status": "RECORDED",
                "typed_contract_status": evaluation["typed_contract_view"]["status"],
                "sealed_reference_status": evaluation[
                    "sealed_reference_and_authorization_view"
                ]["status"],
                "call_count": receipt.get("call_count"),
                "tool_calls": receipt.get("tool_calls"),
                "artifact_directory": relative(case_dir),
            }
        )

    status = "COMPLETE_TWO_CASE_DIAGNOSTIC" if completed == len(CASE_KEYS) else "STOPPED_AFTER_SINGLE_FAILURE"
    receipt = {
        "schema_version": "profiler-schema-diagnostic-run-receipt/v1",
        "status": status,
        "reason_codes": [] if stopped_reason is None else [stopped_reason],
        "role_scope": "PROFILER_SCHEMA_DIAGNOSTIC_ONLY",
        "planner_evaluation": "NOT_RUN",
        "end_to_end": "NOT_RUN",
        "scientific_disposition": "NOT_EVALUATED",
        "model": args.model,
        "endpoint": args.endpoint,
        "prompt": {
            "path": relative(PROFILER_PROMPT_PATH),
            "sha256": sha256_text(profiler_prompt),
        },
        "runtime_metadata": runtime_metadata,
        "model_generation_requests_attempted": attempted,
        "model_generation_calls_completed": completed,
        "registered_operator_calls": 0,
        "execution_performed": False,
        "cases": case_summaries,
        "claim_boundary": "This is a two-case, schema-constrained Profiler diagnostic for one local configuration. It does not evaluate Planner behavior, execute a route, establish scientific support, Agent value, generalization, or production readiness.",
    }
    write_json(output_dir / "run_receipt.json", receipt)
    print(f"{relative(output_dir)}: {receipt['status']}")
    return 0 if stopped_reason is None else 2


if __name__ == "__main__":
    raise SystemExit(main())
