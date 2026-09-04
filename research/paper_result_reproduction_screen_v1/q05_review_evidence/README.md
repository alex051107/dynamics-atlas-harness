# Q05 code and execution evidence for independent review

This package exposes the actual implementation and evidence, including failed entries. It is available for broad scientific and engineering review. No limit is placed on reviewer scope, length, number of findings or recommendations.

The objective is for Rules and connected Operators to answer all20 screened scientific questions with high correctness and coverage. We have not set a justified numeric accuracy target yet. The evaluator should distinguish answered-and-correct, answered-and-wrong, justified abstention and unavailable/uncovered questions; an abstention does not become a correct scientific answer or full coverage.

## Current observed facts

- Original `run-case` failed first on absent pymbar, then actually rejected Q05 in an existing environment with pymbar4.0.3.
- A new Q05-only probe reuses unchanged public-packet admission/projector and the full existing active Draft evaluator. It returns17 instances from8 rule kinds:7 declaration PASS and10 UNRESOLVED; no numerical obligation or scientific verdict.
- The projector lineage string falls through the explicit source-role contract branches for3 instances. Whether this warrants correction, and how, should be independently reviewed.
- A prior manual BME reference computation and a fixed-function comparison are separate from Rules execution.28 fixed-weight/multiplier comparisons match the pinned functions under stated configuration; this is not original-paper configuration verification.

## Review entry points

- [Probe implementation](../../../scripts/run_q05_rules_probe_v1.py), [public packet](../../../evidence/paper_blind_exposed_v1/public/q05_public_fact_packet_v1.json), [recorded proposal](../q05_fact_proposal_v1.json).
- [Actual RuleInstances](outputs/q05_active_rules_probe_v1/raw_rule_results.json), [projected input](outputs/q05_active_rules_probe_v1/projected_casegraph.json), [Rules snapshot](outputs/q05_active_rules_probe_v1/rules_bundle_snapshot.json), [result report](outputs/q05_active_rules_probe_v1/REPORT_ZH.md), [input checks](admission_checks.json).
- [Original dependency failure](outputs/q05_rules_baseline_v0/receipt.json), [actual registry rejection](outputs/q05_rules_baseline_existing_env_v1/receipt.json).
- [Local numerical source](scripts/q05_numeric_v0.py), [fixed-function comparison source](scripts/q05_fixed_weight_audit_v0.py), [numeric result](outputs/q05_numeric_v0/result.json), [method comparison](outputs/q05_fixed_weight_audit_v0/result.json), per-observable TSVs in the same folder.
- [Author download manifest](inputs/q05_author/manifest.json). Paper [Bengtsen2020 eLife56518](https://elifesciences.org/articles/56518); [author inputs at85979b1](https://github.com/KULL-Centre/papers/tree/85979b1b4123b6b5391b617d16551969eda9f56e/2020/nanodisc-bengtsen-et-al); [BME source at314d3b5](https://github.com/KULL-Centre/BME/tree/314d3b5bb8cd400c1a9eee984acdb903a03c3da4).

Run from repository root with the existing declared dependencies:

```bash
PYTHONPATH=src python scripts/run_q05_rules_probe_v1.py   --fact-packet research/paper_result_reproduction_screen_v1/q05_review_evidence/outputs/q05_rules_baseline_v0/q05_fact_packet.json   --output-dir /tmp/q05-review-fresh
```

The output directory must be new. Host paths in receipt/report copies are replaced with documented placeholders; full local originals are retained. Scientific numbers and recorded statuses are unchanged. Numerical scripts use the mirrored task-relative layout and require the publicly linked original inputs; they are not claimed runnable without those inputs. No raw paper text or author source files are included.

The scientific question is joint SAXS/NOE ensemble consistency and shape heterogeneity. Question wording, projected declarations, selected active slice, interpretation of source roles, failure classification, missing numerical semantics and the evaluation protocol are all open to challenge. See the full parent20-question roster and repository history as needed.
