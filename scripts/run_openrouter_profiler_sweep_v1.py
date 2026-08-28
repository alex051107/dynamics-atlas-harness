#!/usr/bin/env python3
"""Run a human-frozen OpenRouter Profiler screening matrix only when explicitly asked.

Without --execute, this script validates no credential and makes no network request.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from dynamics_atlas_harness.openrouter_profiler_sweep_v1 import (
    OpenRouterProfilerSweepError,
    read_openrouter_api_key,
    run_screening,
    validate_execution_config,
    validate_frozen_input_hashes,
)


REPO_ROOT = Path(__file__).parents[1]
CONFIG_PATH = REPO_ROOT / "agent_experiments" / "v1" / "config" / "openrouter_profiler_screening_v1.json"


def load_config() -> dict:
    value = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise OpenRouterProfilerSweepError("screening configuration must be an object")
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true", help="make the admitted screening calls")
    parser.add_argument("--output-root", type=Path, help="required only with --execute")
    args = parser.parse_args()
    config = load_config()
    config_findings = validate_execution_config(config)
    frozen_input_findings = validate_frozen_input_hashes(config, REPO_ROOT)
    findings = config_findings + [
        finding for finding in frozen_input_findings if finding not in config_findings
    ]
    if not args.execute:
        print(json.dumps({"execute": False, "preflight_findings": findings}, indent=2))
        return
    if findings:
        raise SystemExit("execution blocked: " + ", ".join(item["code"] for item in findings))
    if args.output_root is None:
        raise SystemExit("--output-root is required with --execute")
    api_key = read_openrouter_api_key()
    receipt = run_screening(
        config=config,
        repo_root=REPO_ROOT,
        output_root=args.output_root,
        api_key=api_key,
    )
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
