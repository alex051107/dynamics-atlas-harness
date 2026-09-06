#!/bin/bash
cd TEMP_WORKDIR
env 'PYTHONPATH=REPOSITORY_ROOT/src' PYTHONDONTWRITEBYTECODE=1 'WORKSPACE/dynamics-atlas-harness-openrouter/local/venvs/exposed-capsule-v1-py311/bin/python' -c 'from dynamics_atlas_harness.cli import main; raise SystemExit(main())' run-case --case-id q05_nanodisc_saxs_noe_20260904 --output-dir 'REVIEW_ROOT/outputs/q05_rules_baseline_existing_env_v1/runtime_output'
