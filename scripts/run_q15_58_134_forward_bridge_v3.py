"""Run F05R02 only from the v3 reader report and its producer-time record."""

from __future__ import annotations

import argparse
import copy
import datetime
import hashlib
import importlib.util
import json
from pathlib import Path
from typing import Any

from dynamics_atlas_harness import forward_bridge_use_v1 as bridge
from dynamics_atlas_harness import q15_apbs_comparison_v1 as q15


PAIR = "58_134"
INTAKE = "q15_58_134_full_input_intake_v1"
READER_DIR = "q15_58_134_frozen_reuse_v3"
REPORT_VERSION = "q15-58-134-frozen-reuse/v3"
PRODUCER_RECORD_VERSION = "q15-58-134-producer-admission/v1"
SNAPSHOT_FILES = {
    "selected_members": "selected_members.json",
    "complete_receipt": "retry1_receipt.json",
    "input_quality_report": "input_quality_report.json",
}
V2_SCRIPT = Path(__file__).with_name("run_q15_58_134_forward_bridge_v2.py")


def _load_v2() -> Any:
    spec = importlib.util.spec_from_file_location("q15_58_134_bridge_v2", V2_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


v2 = _load_v2()


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_sha256(payload: Any) -> str:
    return _sha256_bytes(json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8"))


def validate_producer_binding(task: Path, report_path: Path, report: dict[str, Any]) -> dict[str, Any]:
    """Reject a report that was not the exact result bound by the reader record."""
    record_path = report_path.with_name("producer_admission.json")
    if not record_path.is_file():
        raise ValueError("PRODUCER_ADMISSION_RECORD_UNAVAILABLE")
    record = _load(record_path)
    producer = record.get("producer", {})
    if record.get("version") != PRODUCER_RECORD_VERSION or producer.get("adapter_version") != REPORT_VERSION:
        raise ValueError("PRODUCER_ADMISSION_VERSION_UNAVAILABLE")
    if report.get("version") != REPORT_VERSION or producer.get("calculation_core") != "q15-58-134-frozen-reuse/v2" or producer.get("frozen_policy") != q15.POLICY:
        raise ValueError("PRODUCER_ADMISSION_METHOD_OR_POLICY_MISMATCH")
    report_record = record.get("report", {})
    if report_record.get("relative_path") != "report.json" or report_record.get("sha256") != _sha256_bytes(report_path.read_bytes()):
        raise ValueError("PRODUCER_REPORT_BYTES_MISMATCH")
    if report_record.get("six_repetition_payload_sha256") != _canonical_sha256(report.get("repetitions")):
        raise ValueError("PRODUCER_REPETITION_PAYLOAD_MISMATCH")
    snapshots = record.get("source_snapshots")
    if not isinstance(snapshots, dict) or set(snapshots) != set(SNAPSHOT_FILES):
        raise ValueError("PRODUCER_SOURCE_SNAPSHOT_SET_MISMATCH")
    source_root = task / "outputs" / INTAKE
    for label, filename in SNAPSHOT_FILES.items():
        path = source_root / filename
        saved = snapshots[label]
        if not path.is_file():
            raise ValueError(f"REQUIRED_SOURCE_SNAPSHOT_UNAVAILABLE:{label}")
        if saved.get("relative_path") != f"{INTAKE}/{filename}" or saved.get("sha256") != _sha256_bytes(path.read_bytes()):
            raise ValueError(f"SOURCE_SNAPSHOT_BYTES_MISMATCH:{label}")
    quality = _load(source_root / SNAPSHOT_FILES["input_quality_report"])
    if quality.get("source_admission") != "COMPLETE" or not quality.get("apbs", {}).get("matches_frozen_export_policy"):
        raise ValueError("QUALITY_SNAPSHOT_NOT_ADMISSIBLE")
    if quality.get("frozen_policy") != q15.POLICY:
        raise ValueError("QUALITY_SNAPSHOT_POLICY_MISMATCH")
    return record


def validate_producer_report(report: dict[str, Any], expected_members: list[dict[str, Any]], expected_groups: dict[str, dict[str, list[str]]]) -> tuple[dict[str, Any], dict[str, Any]]:
    """Reuse v2's arithmetic reconstruction only after v3 origin validation."""
    compatible = copy.deepcopy(report)
    compatible["version"] = "q15-58-134-frozen-reuse/v2"
    return v2.validate_producer_report(compatible, expected_members, expected_groups)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-root", type=Path, required=True)
    parser.add_argument("--comparison", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    task, comparison_path, output = args.task_root.resolve(), args.comparison.resolve(), args.output.resolve()
    expected_path = task / "outputs" / READER_DIR / "report.json"
    if comparison_path != expected_path or output.exists():
        raise ValueError("EXPECTED_V3_PRODUCER_PATH_REQUIRED" if comparison_path != expected_path else f"REFUSING_TO_OVERWRITE:{output}")
    report = _load(comparison_path)
    producer_record = validate_producer_binding(task, comparison_path, report)
    expected_members, expected_groups = v2.expected_source_map(task)
    direction, diagnostics = validate_producer_report(report, expected_members, expected_groups)
    root = Path(__file__).resolve().parents[1]
    reference = _load(root / "research" / "paper_result_reproduction_screen_v1" / "q15_full_table2_reference_admission_v1.json")
    if reference.get("forward_distance_semantics") != "FRET_EFFICIENCY_AVERAGED_MODEL_DISTANCE":
        raise ValueError("REFERENCE_SEMANTICS_INCOMPATIBLE")
    source = v2._source_record()
    scope = {"source_id": source["source_id"], "model_id": "author-FPS-open-closed-reference", "observable": "FRET_E", "probe": "AF555_AF647_58_134", "condition": "apo:1mM_SA_archive_label", "unit": "dimensionless_efficiency", "aggregation": "equal_repetition_mean_E_vs_efficiency_weighted_reference_R", "target_support": "apo:holo"}
    value = {"scope": scope, "method_id": "efficiency_weighted_reference_direction_v1", "data": {"reference_definition": "EFFICIENCY_WEIGHTED_DISTANCE", "observed_change": direction["holo_minus_apo_E"], "reference_apo": reference["pairs"][PAIR]["FRET_sim"]["apo"], "reference_holo": reference["pairs"][PAIR]["FRET_sim"]["holo"], "direction_checks": [diagnostics["equal_repetition_median_effect"], *diagnostics["leave_one_per_condition_effects"]]}}
    use = {"contract": bridge.CONTRACT, "use_id": "reference-58_134-v3", "scope": scope, "method_id": value["method_id"], "input_ref": "input-reference-58_134-v3", "requested_use": "MODEL_OBSERVATION_COMPARISON"}
    context = {"inputs": {use["input_ref"]: value}, "admissions": {use["input_ref"]: {"input_digest": bridge.digest(value), "source_receipts": ["q15_58_134_full_input_intake_v1/retry1_receipt.json", "q15_58_134_full_input_intake_v1/input_quality_report.json", "q15-58-134-frozen-reuse/v3/report.json", "q15-58-134-frozen-reuse/v3/producer_admission.json", "q15_full_table2_reference_admission_v1.json"], "method_basis": reference["locator"] + "; existing frozen Q15 correction and stable-probe reference hypothesis; no mean-distance conversion.", "conditional_assumptions": ["stable-probe reference hypothesis", "efficiency-weighted reference output, not mean distance", "shared frozen calibration remains conditionally applicable"], "authority_binding": {"source_id": source["source_id"], "source_version": "Peter2022 Figure3 selected 58/134 members and SI Table2 rows1-2", "measurement_version": REPORT_VERSION, "relationship_to_graph": "LATER_ADMITTED_SOURCE_FOR_CURRENT_USE", "relevant_contradictions": []}, "role": "NEW_DERIVED_INPUT_ADMISSION_FROM_PRIOR_SOURCES_NOT_SCIENTIFIC_APPROVAL"}}}
    graph = {"case": {"case_id": "development-q15-58-134-local-direction-v3", "intake_kind": "SCIENTIFIC_CLAIM_REVIEW", "scientific_claim": "For the admitted 58/134 source exports, does the frozen efficiency direction agree with the published efficiency-weighted FPS reference direction?", "requested_claim_level": "LOCAL_MODEL_OBSERVATION_DIRECTION", "intended_use": "DEVELOPMENT_REPLAY", "observability_target": {"event_signature": "Admitted source-derived local direction check", "target_time_scale": "SOURCE_DECLARED", "target_spatial_scale": "TWO_FLUOROPHORE_LABEL_POSITIONS"}, "claim_contract": {"internal_consistency": "CONSISTENT", "declared_request_scope": ["LOCAL_MODEL_OBSERVATION_DIRECTION"], "forbidden_upgrades": ["BIOLOGICAL_ACTIVITY", "BACKBONE_DISTANCE_AS_PROBE_DISTANCE", "STRUCTURAL_POPULATION", "FULL_Q15_ANSWER"]}}, "evidence_items": [source], "comparisons": [], "projection_boundary": "One v3 producer-bound use under frozen F05R02; it has no whole-question verdict.", "forward_bridge_uses": [use]}
    kwargs = {"case_graph": graph, "runtime_subrules": _load(root / "registries/rules_v1/runtime_subrules_v1.json"), "bindings": _load(root / "registries/rules_v1/applicability_bindings_v1.json"), "contracts": _load(root / "registries/rules_v1/evaluation_contracts_v1.json")}
    off = bridge.run_checks(**kwargs, context=context, enabled=False)
    on = bridge.run_checks(**kwargs, context=context, enabled=True)
    reentry_context = copy.deepcopy(context)
    reentry_context["evidence"] = on["evidence"]
    reentry = bridge.run_checks(**kwargs, context=reentry_context, enabled=True)
    pick = lambda result: next(row for row in result["after"] if row.get("use_id") == use["use_id"])
    off_row, on_row, reentry_row = pick(off), pick(on), pick(reentry)
    if off_row.get("reason") != "REQUESTED_USE_NUMERICAL_CHECK_MISSING" or off["operator_calls"] or len(on["operator_calls"]) != 1 or not on_row.get("check_completed") or reentry["operator_calls"]:
        raise ValueError("RULES_REENTRY_NOT_REPRODUCIBLE")
    output.mkdir(parents=True)
    for name, payload in (("casegraph", graph), ("admission", context), ("producer_admission", producer_record), ("off", off), ("on", on), ("reentry", reentry)):
        (output / f"{name}.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    result = {"version": "q15-58-134-forward-bridge/v3", "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(), "comparison_report": str(comparison_path), "producer_record_valid": True, "rule_instance_id": on_row["rule_instance_id"], "operator": bridge.RULE_ID, "method_id": value["method_id"], "producer_reconstructed": True, "off": {key: off_row.get(key) for key in ("status", "route", "reason", "check_completed")}, "on": {key: on_row.get(key) for key in ("status", "route", "reason", "check_completed", "local_support", "numerical", "allowed_conclusion", "claim_ceiling", "conditional_assumptions")}, "reentry": {key: reentry_row.get(key) for key in ("status", "route", "reason", "check_completed", "local_support")}, "operator_calls": {"off": len(off["operator_calls"]), "on": len(on["operator_calls"]), "reentry": len(reentry["operator_calls"])}, "new_fits": 0, "full_question_count_change": 0, "claim_ceiling": "One conditional local 58/134 model-observation direction relation, not a protein-state, activity, absolute-distance, full-Q15 or accuracy conclusion."}
    (output / "report.json").write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
