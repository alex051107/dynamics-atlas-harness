#!/bin/bash
# Exact attempted command; requires an environment with declared project dependencies.
cd TEMP_WORKDIR
env 'PYTHONPATH=REPOSITORY_ROOT/src' PYTHONDONTWRITEBYTECODE=1 python3 (original environment) -c 'from dynamics_atlas_harness.cli import main; raise SystemExit(main())' run-case --case-id q05_nanodisc_saxs_noe_20260904 --output-dir 'REVIEW_ROOT/outputs/q05_rules_baseline_v0/runtime_output'
