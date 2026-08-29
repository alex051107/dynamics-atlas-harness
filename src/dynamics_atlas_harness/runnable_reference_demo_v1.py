"""One-command rerun of the two frozen exposed-development reference routes.

This module intentionally orchestrates only X-EISD A1/A2/A3, HSP90 B1, and the
existing minimal Stage-2 reducer.  It is not a general workflow engine, source
retrieval layer, or scientific conclusion system.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

from .minimal_stage2_exposed_conclusions_v1 import (
    materialize_stage2_conclusion_packet,
    source_grounding_by_family,
)
from .real_case_vertical_slice_v1 import (
    X_EISD_CASE_ID,
    apply_lookup_result,
    derive_declaration_attestations,
    evaluate_xeisd_case,
    execute_exact_source_lookup,
    load_json_object,
    load_rules_v1_bundle,
    materialize_xeisd_conclusion_packet,
    run_hsp90_reference_demo_route,
)
from .registered_operators import load_registered_operator_registry


DEMO_SCHEMA_VERSION = "runnable-reference-demo/v1"
DEMO_RUN_ID = "runnable_reference_demo_v1"


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _prepare_output_dir(output_dir: Path) -> Path:
    output_dir = output_dir.resolve()
    if output_dir.exists() and (not output_dir.is_dir() or any(output_dir.iterdir())):
        raise ValueError("OUTPUT_DIR_MUST_BE_NEW_OR_EMPTY")
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _input_identity(repo_root: Path, relative_path: str) -> dict[str, str]:
    path = (repo_root / relative_path).resolve()
    if not path.is_relative_to(repo_root) or not path.is_file():
        raise ValueError(f"REFERENCE_DEMO_INPUT_UNAVAILABLE:{relative_path}")
    return {"workspace_relative_path": relative_path, "sha256": _sha256(path)}


def _lookup_request(allowlist: Mapping[str, Any], lookup_id: str) -> dict[str, str]:
    entries = allowlist.get("entries")
    if not isinstance(entries, list):
        raise ValueError("X_EISD_ALLOWLIST_ENTRIES_MISSING")
    entry = next(
        (
            item
            for item in entries
            if isinstance(item, Mapping) and item.get("lookup_id") == lookup_id
        ),
        None,
    )
    if not isinstance(entry, Mapping):
        raise ValueError(f"X_EISD_ALLOWLIST_ENTRY_MISSING:{lookup_id}")
    return {
        "lookup_id": lookup_id,
        "case_id": X_EISD_CASE_ID,
        "target_kind": str(entry["target_kind"]),
        "target_id": str(entry["target_id"]),
        "locator_id": str(entry["locator_id"]),
    }


def run_xeisd_a1_reference_route(*, repo_root: Path) -> dict[str, Any]:
    """Rerun only the exact complete-metadata X-EISD reference route.

    This is the existing A1 attestation/direct-evaluation path extracted so a
    caller that has already authorized A1 does not need to execute the separate
    A2/A3 reference scenarios. It is still exact-case development code, not a
    generic lookup or route executor.
    """

    evidence_root = repo_root / "evidence" / "real_case_vertical_slice_v1"
    seed = load_json_object(evidence_root / "xeisd_case_projection_seed_v1.json")
    allowlist = load_json_object(evidence_root / "xeisd_source_lookup_allowlist_v1.json")
    bundle = load_rules_v1_bundle(repo_root / "registries" / "rules_v1")

    case_graph = copy.deepcopy(seed)
    lookup_receipts: list[dict[str, Any]] = []
    for lookup_id in (
        "XEI-LOOKUP-RANDOM-DECLARATIONS",
        "XEI-LOOKUP-JCOUPLING-DECLARATIONS",
        "XEI-LOOKUP-RANDOM-JCOUPLING-EDGE",
    ):
        result = execute_exact_source_lookup(
            allowlist=allowlist,
            request=_lookup_request(allowlist, lookup_id),
            workspace_root=repo_root,
        )
        if result.get("status") != "FOUND":
            raise ValueError(f"X_EISD_REFERENCE_LOOKUP_FAILED:{lookup_id}:{result.get('status')}")
        lookup_receipts.append(result)
        case_graph = apply_lookup_result(case_graph=case_graph, lookup_result=result)
    case_graph = derive_declaration_attestations(
        case_graph=case_graph, lookup_results=lookup_receipts
    )
    rule_results = evaluate_xeisd_case(case_graph=case_graph, **bundle)
    conclusion_packet = materialize_xeisd_conclusion_packet(
        case_graph=case_graph,
        rule_results=rule_results,
        lookup_results=lookup_receipts,
        scenario_id="A1_COMPLETE_LOOKUP_THEN_DIRECT",
    )
    return {
        "case_graph": case_graph,
        "lookup_receipts": lookup_receipts,
        "conclusion_packet": conclusion_packet,
    }


def _run_xeisd_routes(repo_root: Path) -> dict[str, Any]:
    """Reuse the frozen exact-attestation and deterministic evaluation paths."""

    a1 = run_xeisd_a1_reference_route(repo_root=repo_root)
    a1_graph = a1["case_graph"]
    a1_lookups = a1["lookup_receipts"]
    a1_packet = a1["conclusion_packet"]

    evidence_root = repo_root / "evidence" / "real_case_vertical_slice_v1"
    allowlist = load_json_object(evidence_root / "xeisd_source_lookup_allowlist_v1.json")
    bundle = load_rules_v1_bundle(repo_root / "registries" / "rules_v1")

    a2_graph = copy.deepcopy(a1_graph)
    a2_graph["evidence_items"][0].pop("sample_composition")
    a2_results = evaluate_xeisd_case(case_graph=a2_graph, **bundle)
    a2_lookup = execute_exact_source_lookup(
        allowlist=allowlist,
        request={
            "lookup_id": "XEI-LOOKUP-MISSING-COMPOSITION",
            "case_id": X_EISD_CASE_ID,
            "target_kind": "SOURCE",
            "target_id": "xeisd_random_candidate_pool",
            "locator_id": "XEI-M04",
        },
        workspace_root=repo_root,
    )
    a2_packet = materialize_xeisd_conclusion_packet(
        case_graph=a2_graph,
        rule_results=a2_results,
        lookup_results=[a2_lookup],
        scenario_id="A2_MISSING_COMPOSITION",
    )

    a3_graph = copy.deepcopy(a1_graph)
    a3_graph["comparisons"][0]["condition_relation"] = "MISMATCH"
    a3_results = evaluate_xeisd_case(case_graph=a3_graph, **bundle)
    a3_packet = materialize_xeisd_conclusion_packet(
        case_graph=a3_graph,
        rule_results=a3_results,
        lookup_results=a1_lookups,
        scenario_id="A3_EXPLICIT_CONDITION_MISMATCH",
    )
    return {
        "a1_case_graph": a1_graph,
        "a1_lookup_receipts": a1_lookups,
        "a1_conclusion_packet": a1_packet,
        "a2_lookup_receipt": a2_lookup,
        "a2_conclusion_packet": a2_packet,
        "a3_conclusion_packet": a3_packet,
    }


def _write_xeisd_routes(output_dir: Path, xeisd: Mapping[str, Any]) -> dict[str, str]:
    paths = {
        "XEISD_A1_COMPLETE_METADATA": "routes/xeisd_a1/conclusion_packet.json",
        "XEISD_A2_MISSING_COMPOSITION": "routes/xeisd_a2/conclusion_packet.json",
        "XEISD_A3_EXPLICIT_CONDITION_MISMATCH": "routes/xeisd_a3/conclusion_packet.json",
    }
    _write_json(output_dir / "routes/xeisd_a1/case_graph.json", xeisd["a1_case_graph"])
    _write_json(output_dir / "routes/xeisd_a1/lookup_receipts.json", xeisd["a1_lookup_receipts"])
    _write_json(output_dir / paths["XEISD_A1_COMPLETE_METADATA"], xeisd["a1_conclusion_packet"])
    _write_json(output_dir / "routes/xeisd_a2/missing_composition_lookup.json", xeisd["a2_lookup_receipt"])
    _write_json(output_dir / paths["XEISD_A2_MISSING_COMPOSITION"], xeisd["a2_conclusion_packet"])
    _write_json(output_dir / paths["XEISD_A3_EXPLICIT_CONDITION_MISMATCH"], xeisd["a3_conclusion_packet"])
    return paths


def write_hsp90_reference_route_artifacts(
    *, output_root: Path, hsp90: Mapping[str, Any]
) -> str:
    """Write the exact B1 route packet tree under one caller-owned output root."""

    route_dir = output_root / "routes/hsp90_b1"
    for name in (
        "pre_operator_rule_result",
        "resolution_route",
        "operator_run_receipt",
        "evidence_result",
        "post_operator_rule_result",
        "conclusion_packet",
        "run_receipt",
    ):
        _write_json(route_dir / f"{name}.json", hsp90[name])
    return "routes/hsp90_b1/conclusion_packet.json"


def _write_stage2_packets(
    *,
    repo_root: Path,
    output_dir: Path,
    route_packets: Mapping[str, tuple[Mapping[str, Any], str]],
) -> tuple[dict[str, str], dict[str, str]]:
    family_overlay_path = repo_root / "registries/rules_v1/family_overlay_v1.json"
    source_grounding = source_grounding_by_family(load_json_object(family_overlay_path))
    output_names = {
        "XEISD_A1_COMPLETE_METADATA": "xeisd_a1_complete_stage2_conclusion_packet.json",
        "XEISD_A2_MISSING_COMPOSITION": "xeisd_a2_missing_composition_stage2_conclusion_packet.json",
        "XEISD_A3_EXPLICIT_CONDITION_MISMATCH": "xeisd_a3_condition_mismatch_stage2_conclusion_packet.json",
        "HSP90_B1_OPERATOR_CONTRACT_PASS": "hsp90_b1_operator_contract_stage2_conclusion_packet.json",
    }
    stage2_paths: dict[str, str] = {}
    terminal_dispositions: dict[str, str] = {}
    for scenario_id, (route_packet, route_path) in route_packets.items():
        packet = materialize_stage2_conclusion_packet(
            route_packet=route_packet,
            source_grounding=source_grounding,
            scenario_id=scenario_id,
            route_artifact_path=route_path,
        )
        relative_path = f"stage2/{output_names[scenario_id]}"
        _write_json(output_dir / relative_path, packet)
        stage2_paths[scenario_id] = relative_path
        terminal_dispositions[scenario_id] = packet["terminal_disposition"]
    return stage2_paths, terminal_dispositions


def _report(terminal_dispositions: Mapping[str, str]) -> str:
    rows = "\n".join(
        f"| {scenario_id} | {disposition} |"
        for scenario_id, disposition in terminal_dispositions.items()
    )
    return (
        "# Runnable reference demo\n\n"
        "This run recomputed the existing X-EISD A1/A2/A3 and HSP90 B1 "
        "exposed-development routes from repository-contained frozen inputs. It then "
        "fed the fresh route packets to the existing deterministic Stage-2 reducer.\n\n"
        "| Scenario | Development disposition |\n"
        "| --- | --- |\n"
        f"{rows}\n\n"
        "The result is a reproducible development reference, not a source-science "
        "approval or a final scientific conclusion. X-EISD A1 and HSP90 B1 still "
        "require human review. X-EISD A2 remains unresolved, and X-EISD A3 blocks "
        "only the declared cross-source relation.\n\n"
        "No network request, model call, credential read, or external spend occurred. "
        "The named F01/F02/F03/F04/F06 source-science review remains pending.\n"
    )


def run_reference_demo(*, output_dir: Path) -> dict[str, Any]:
    """Create one fresh runnable-reference output tree from the frozen inputs."""

    repo_root = _repo_root()
    output_dir = _prepare_output_dir(output_dir)
    xeisd = _run_xeisd_routes(repo_root)
    xeisd_paths = _write_xeisd_routes(output_dir, xeisd)

    hsp90 = run_hsp90_reference_demo_route(
        evidence_root=repo_root / "evidence" / "real_case_vertical_slice_v1",
        operator_registry=load_registered_operator_registry(
            repo_root / "config" / "registered_operators.json"
        ),
        workspace_root=repo_root,
        output_root=output_dir,
    )
    hsp90_path = write_hsp90_reference_route_artifacts(
        output_root=output_dir, hsp90=hsp90
    )
    route_packets: dict[str, tuple[Mapping[str, Any], str]] = {
        "XEISD_A1_COMPLETE_METADATA": (xeisd["a1_conclusion_packet"], xeisd_paths["XEISD_A1_COMPLETE_METADATA"]),
        "XEISD_A2_MISSING_COMPOSITION": (xeisd["a2_conclusion_packet"], xeisd_paths["XEISD_A2_MISSING_COMPOSITION"]),
        "XEISD_A3_EXPLICIT_CONDITION_MISMATCH": (xeisd["a3_conclusion_packet"], xeisd_paths["XEISD_A3_EXPLICIT_CONDITION_MISMATCH"]),
        "HSP90_B1_OPERATOR_CONTRACT_PASS": (hsp90["conclusion_packet"], hsp90_path),
    }
    stage2_paths, terminal_dispositions = _write_stage2_packets(
        repo_root=repo_root,
        output_dir=output_dir,
        route_packets=route_packets,
    )
    expected_terminal_dispositions = {
        "XEISD_A1_COMPLETE_METADATA": "ABSTAIN_OR_HUMAN_REVIEW",
        "XEISD_A2_MISSING_COMPOSITION": "ABSTAIN_OR_HUMAN_REVIEW",
        "XEISD_A3_EXPLICIT_CONDITION_MISMATCH": "CANNOT_SUPPORT_REQUESTED_CLAIM",
        "HSP90_B1_OPERATOR_CONTRACT_PASS": "ABSTAIN_OR_HUMAN_REVIEW",
    }
    if terminal_dispositions != expected_terminal_dispositions:
        raise ValueError("REFERENCE_DEMO_TERMINAL_DISPOSITIONS_CHANGED")

    input_identities = {
        "xeisd_case_projection_seed": _input_identity(
            repo_root, "evidence/real_case_vertical_slice_v1/xeisd_case_projection_seed_v1.json"
        ),
        "xeisd_lookup_allowlist": _input_identity(
            repo_root, "evidence/real_case_vertical_slice_v1/xeisd_source_lookup_allowlist_v1.json"
        ),
        "xeisd_exact_review_derivative": {
            "workspace_relative_path": xeisd["a1_lookup_receipts"][0]["workspace_relative_path"],
            "sha256": xeisd["a1_lookup_receipts"][0]["fixture_sha256"],
        },
        "hsp90_manifest_receipt": hsp90["resolution_route"]["manifest_receipt"],
        "stage2_family_overlay": _input_identity(
            repo_root, "registries/rules_v1/family_overlay_v1.json"
        ),
    }
    manifest = {
        "schema_version": DEMO_SCHEMA_VERSION,
        "run_id": DEMO_RUN_ID,
        "run_kind": "EXPOSED_DEVELOPMENT_REFERENCE_DEMO",
        "input_identities": input_identities,
        "route_artifacts": {scenario_id: path for scenario_id, (_, path) in route_packets.items()},
        "stage2_artifacts": stage2_paths,
        "network_accessed": False,
        "model_calls": 0,
        "credential_reads": 0,
        "external_spend": 0,
        "scientific_disposition": "NOT_EVALUATED",
        "boundary": "Exact exposed-development rerun only. The command performs no free-text retrieval, source-science review, general workflow inference, or claim upgrade.",
    }
    summary = {
        "schema_version": DEMO_SCHEMA_VERSION,
        "run_id": DEMO_RUN_ID,
        "status": "SUCCEEDED",
        "terminal_dispositions": terminal_dispositions,
        "scientific_support_packets": 0,
        "network_accessed": False,
        "model_calls": 0,
        "source_science_review_status": "PENDING_DOMAIN_REVIEW",
        "next_action": "Named human/domain source-science review for F01/F02/F03/F04/F06.",
    }
    _write_json(output_dir / "run_manifest.json", manifest)
    _write_json(output_dir / "run_summary.json", summary)
    (output_dir / "report.md").write_text(_report(terminal_dispositions), encoding="utf-8")
    return {"manifest": manifest, "summary": summary, "output_dir": str(output_dir)}
