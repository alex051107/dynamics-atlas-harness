#!/usr/bin/env python3
"""Run the fixed HSP90+ADK exposed development capsule into a fresh directory."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from dynamics_atlas_harness.exposed_paper_blind_capsule_v1 import (
    create_clean_output_root,
    run_exposed_paper_blind_capsule,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    output_root = create_clean_output_root(args.output_root)
    result = run_exposed_paper_blind_capsule(output_root=output_root)
    print(json.dumps(result["summary"], indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
