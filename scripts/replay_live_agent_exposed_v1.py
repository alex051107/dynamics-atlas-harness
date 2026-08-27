#!/usr/bin/env python3
"""Replay committed Live-Agent outputs without starting a model transport.

This utility accepts only an existing repository-relative recorded-run directory.
It reads the committed packets, references, raw responses, proposals, and original
call receipts; it never constructs a provider or sends HTTP traffic.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from dynamics_atlas_harness.live_agent_exposed_v1 import replay_recorded_run


REPO_ROOT = Path(__file__).resolve().parents[1]
EXPERIMENT_ROOT = REPO_ROOT / "agent_experiments" / "v1"


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_replay_artifacts(recorded_dir: Path, replay: dict[str, Any]) -> None:
    """Overwrite only deterministic derived artifacts, never proposals or raw responses."""

    for unit_id, artifacts in replay["unit_artifacts"].items():
        unit_dir = recorded_dir / unit_id
        write_json(unit_dir / "packet_validation.json", artifacts["packet_validation"])
        write_json(unit_dir / "evaluation.json", artifacts["evaluation"])
    write_json(recorded_dir / "model_visible_workspace_report.json", replay["workspace_report"])
    write_json(recorded_dir / "hard_gate_report.json", replay["hard_gates"])
    (recorded_dir / "comparison_report.md").write_text(
        replay["comparison_report"], encoding="utf-8"
    )
    write_json(recorded_dir / "run_receipt.json", replay["run_receipt"])
    write_json(recorded_dir / "evaluation_manifest.json", replay["manifest"])
    write_json(recorded_dir / "deterministic_replay_receipt.json", replay["replay_receipt"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--recorded-dir",
        action="append",
        required=True,
        help="Existing repository-relative recorded-run directory; repeat for both committed runs.",
    )
    args = parser.parse_args()

    exit_code = 0
    for relative_dir in args.recorded_dir:
        recorded_dir = (REPO_ROOT / relative_dir).resolve()
        if not recorded_dir.is_relative_to(REPO_ROOT) or not recorded_dir.is_dir():
            raise SystemExit("recorded directory must be an existing repository-relative path")
        replay = replay_recorded_run(recorded_dir, EXPERIMENT_ROOT, REPO_ROOT)
        write_replay_artifacts(recorded_dir, replay)
        print(f"{relative_dir}: {replay['status']}")
        if replay["status"] == "FAIL":
            exit_code = 1
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
