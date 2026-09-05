# Q05 R1: claim applicability and source-lineage repair

The new Q05 run returns **7 declaration PASS, 8 UNRESOLVED and 2 NOT_APPLICABLE**, versus the preserved R0's7 PASS and10 UNRESOLVED. There is still no numerical obligation or scientific answer. The result count is17 because the evaluator retains NOT_APPLICABLE target records; those two records do not represent required scientific checks.

The profiling projection previously wrote a nonempty sentence denying a validation claim. The EXISTS binding treated the sentence as a claim and selected an independence check. Profiling does not request independent validation, so the projection now omits the claim. The global EXISTS semantics and actual validation rule are unchanged. A counterfactual explicit validation claim with SAME_DATA still fails.

The source-role contract now explicitly handles AGENT_PROPOSED_UNVERIFIED with SOURCE_PROPOSED_LINEAGE_REQUIRES_VERIFICATION. All three affected source instances remain UNRESOLVED; their provenance status is not promoted. The action remains source lookup. This repair gives the unresolved result a specific cause, not scientific approval.

The probe's local_adapter_uncommitted field now reflects git status for the adapter file, including staged/untracked changes. It was true for this run. It describes the adapter only, not the whole working tree.

## Evidence and replay

- [Raw results](raw_rule_results.json), [projected input](projected_casegraph.json), [Rules snapshot](rules_bundle_snapshot.json), [receipt](receipt.json), [focused validation](validation.json).
- [Exact tracked implementation delta](implementation.patch) from fcc15858070588129c6a3ec063c5a90362db6ad1, captured before commit; current source and tests are in the same PR commit. The run is from that base plus this patch, not from a clean fcc1585 checkout.
- Original public packet, proposal and method-only input are unchanged. All R0 outputs in ../q05_review_evidence remain unchanged.

Run from repository root using an environment with the declared dependencies:

```bash
PYTHONPATH=src python scripts/run_q05_rules_probe_v1.py --fact-packet research/paper_result_reproduction_screen_v1/q05_review_evidence/outputs/q05_rules_baseline_v0/q05_fact_packet.json --output-dir /tmp/q05-r1-fresh
python -m unittest tests.test_q05_review_repairs_v1 tests.test_paper_blind_exposed_v1 tests.rules_v1.test_binding_behavior tests.rules_v1.test_contract_consistency
```

The tests require src on PYTHONPATH or the project installed.21 focused tests passed in one invocation; one actual Q05 run was recorded. No numerical rerun, full build or repeated hashes. Portable receipt paths replace local roots with REPOSITORY_ROOT, TASK_ROOT, WORKSPACE, USER_HOME and TEMP_WORKDIR; local originals are preserved.

## Remaining work

This batch closes two semantics defects from Pro round3. It does not close proposal fact fidelity, UNKNOWN string normalization, the joint-fit relation's lack of scientific criteria, coordinate-to-matrix mapping, shape analysis or the original method configuration. Those remain explicit next work. The next scientific localization is fixed author-weight back-calculation on the independent review side, without tuning or feeding author weights into Rules. The eventual capability needs real obligations, numerical EvidenceResults and re-evaluation on the same instance, assessed against the whole scientific question.

The original20 questions remain the evaluation denominator. Metadata PASS, abstention and human reference calculations do not count as complete correct answers. This exposed development repair does not establish generalization or Rules accuracy gain.
