# Independent numerical replay and new fitting

Run from the repository root with the existing scientific environment (NumPy and SciPy). Obtain original eTCSPC_wildtype.zip from Zenodo3376527 as recorded in q09_method_admission_v1/input_manifest.json; keep it in INPUT_ROOT and extract original eTCSPC/ beneath INPUT_ROOT/unpacked/. The runtime checks the deposited archive MD5, all consumed member bytes, metadata and axes.

To recompute saved predictions, losses, diagnostics and same-instance reassessment without optimization or historical failed runners:

```sh
PYTHONPATH=src python scripts/replay_q09_numeric_evidence_v1.py --input-root INPUT_ROOT --evidence-dir research/paper_result_reproduction_screen_v1/q09_forward_adequacy_v1 --output-dir FRESH_REPLAY_DIR
```

To execute the rule-controlled diagnostic from predeclared initializations (up to11 bounded optimizer calls):

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH=src python scripts/run_q09_forward_adequacy_v1.py --input-root INPUT_ROOT --output-dir FRESH_RUN_DIR
```

The old donor2/K2 saved model is a read-only current-model reference from q09_pq_joint_v3/summary.json; its predictions and likelihood are recomputed from raw observations. It is not an author answer or a requirement to executev1/v2 failures. The original pre-repair runtime snapshot and final reassessment source are both retained. No raw ZIP/PDF or original full per-bin counts are republished; the commands generate per-bin predictions and observed counts locally. Core CI runs synthetic/interface checks, not external data downloads or full scientific optimizations.
