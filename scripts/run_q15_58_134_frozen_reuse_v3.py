"""Produce a v3 58/134 reader report with a reader-time identity record.

The numerical calculation remains the preserved v2 frozen reader.  Version 3
adds a narrow producer record after that reader has written its final report;
the v3 bridge consumes the record before it admits any derived input.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from dynamics_atlas_harness import q15_apbs_comparison_v1 as q15


INTAKE = "q15_58_134_full_input_intake_v1"
REPORT_VERSION = "q15-58-134-frozen-reuse/v3"
PRODUCER_RECORD_VERSION = "q15-58-134-producer-admission/v1"
V2_SCRIPT = Path(__file__).with_name("run_q15_58_134_frozen_reuse_v2.py")
SNAPSHOT_FILES = {
    "selected_members": "selected_members.json",
    "complete_receipt": "retry1_receipt.json",
    "input_quality_report": "input_quality_report.json",
}


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _canonical_sha256(payload: Any) -> str:
    return _sha256_bytes(json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8"))


def _load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text())


def build_producer_record(task: Path, report_path: Path, report: dict[str, Any]) -> dict[str, Any]:
    """Bind final reader bytes and its declared input snapshots at production time."""
    source_root = task / "outputs" / INTAKE
    snapshots: dict[str, dict[str, str]] = {}
    for label, filename in SNAPSHOT_FILES.items():
        path = source_root / filename
        if not path.is_file():
            raise ValueError(f"REQUIRED_SOURCE_SNAPSHOT_UNAVAILABLE:{label}")
        snapshots[label] = {"relative_path": f"{INTAKE}/{filename}", "sha256": _sha256_bytes(path.read_bytes())}
    quality = _load(source_root / SNAPSHOT_FILES["input_quality_report"])
    if quality.get("source_admission") != "COMPLETE" or not quality.get("apbs", {}).get("matches_frozen_export_policy"):
        raise ValueError("QUALITY_SNAPSHOT_NOT_ADMISSIBLE")
    if quality.get("frozen_policy") != q15.POLICY:
        raise ValueError("FROZEN_POLICY_CHANGED")
    return {
        "version": PRODUCER_RECORD_VERSION,
        "producer": {
            "adapter_version": REPORT_VERSION,
            "calculation_core": "q15-58-134-frozen-reuse/v2",
            "frozen_policy": q15.POLICY,
        },
        "report": {
            "relative_path": "report.json",
            "sha256": _sha256_bytes(report_path.read_bytes()),
            "six_repetition_payload_sha256": _canonical_sha256(report["repetitions"]),
        },
        "source_snapshots": snapshots,
    }


def write_producer_admission(task: Path, report_path: Path, report: dict[str, Any]) -> Path:
    record_path = report_path.with_name("producer_admission.json")
    record_path.write_text(json.dumps(build_producer_record(task, report_path, report), ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    return record_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    task, output = args.task_root.resolve(), args.output.resolve()
    if output.exists():
        raise FileExistsError(f"REFUSING_TO_OVERWRITE:{output}")
    subprocess.run(
        [sys.executable, str(V2_SCRIPT), "--task-root", str(task), "--output", str(output)],
        check=True,
    )
    report_path = output / "report.json"
    report = _load(report_path)
    report["version"] = REPORT_VERSION
    report["producer_binding"] = {
        "record": "producer_admission.json",
        "record_version": PRODUCER_RECORD_VERSION,
        "calculation_core": "q15-58-134-frozen-reuse/v2",
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    record_path = write_producer_admission(task, report_path, report)
    print(json.dumps({"pair": report["source_selection"]["pair"], "report": str(report_path), "producer_record": str(record_path)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
