# Rules Prototype Acceptance Suite v1

This is fixture-driven Rules Prototype scenario acceptance: four synthetic contract fixtures (T1-T4) and four exposed development scenarios (T5-T8). A common acceptance driver combines bounded existing paths; it does not claim automatic Rule selection or general routing.

The driver runs admission, current Rule evaluation, a task-card-selected unresolved obligation when one exists, a preauthorized action or fail-closed STOP, EvidenceResult, same-Rule re-evaluation, and a three-state ConclusionPacket. Generated acceptance is computed by comparing actual output with predeclared expected_results.jsonl.

| Task | Scenario type | Legal route | Executed action | EvidenceResults | Rule transition | Terminal state | Acceptance |
| --- | --- | --- | --- | ---: | --- | --- | --- |
| T1_COMPLETE_SOURCE_MEASUREMENT_DECLARATION | SYNTHETIC_CONTRACT_FIXTURE | DIRECT_EVALUATION | DIRECT_EVALUATION | 0 | none | SUPPORT_WITHIN_CEILING | PASS |
| T2_F03_REQUIRED_FIELD_MISSING | SYNTHETIC_CONTRACT_FIXTURE | SOURCE_LOOKUP | STOP | 0 | none | ABSTAIN_OR_HUMAN_REVIEW | PASS |
| T3_EXPLICIT_EDGE_CONDITION_MISMATCH | SYNTHETIC_CONTRACT_FIXTURE | HUMAN_OR_NEW_DATA | DIRECT_EVALUATION | 0 | none | CANNOT_SUPPORT_REQUESTED_CLAIM | PASS |
| T4_WRONG_TARGET_SOURCE_RULE | SYNTHETIC_CONTRACT_FIXTURE | HUMAN_OR_NEW_DATA | DIRECT_EVALUATION | 0 | none | ABSTAIN_OR_HUMAN_REVIEW | PASS |
| T5_XEISD_EXACT_LOOKUP_AVAILABLE | EXPOSED_DEVELOPMENT_SCENARIO | SOURCE_LOOKUP | EXACT_LOOKUP | 1 | UNRESOLVED to PASS | ABSTAIN_OR_HUMAN_REVIEW | PASS |
| T6_XEISD_LOOKUP_UNAVAILABLE | EXPOSED_DEVELOPMENT_SCENARIO | SOURCE_LOOKUP | STOP | 0 | none | ABSTAIN_OR_HUMAN_REVIEW | PASS |
| T7_HSP90_REGISTERED_OPERATOR_CLOSURE | EXPOSED_DEVELOPMENT_SCENARIO | REGISTERED_OPERATOR | REGISTERED_OPERATOR | 1 | UNRESOLVED to PASS | ABSTAIN_OR_HUMAN_REVIEW | PASS |
| T8_ADK_BOUNDED_STRUCTURAL_COMPUTATION | DESCRIPTIVE_NO_ACTIVE_RULE_CONTROL | DIRECT_EVALUATION | DESCRIPTIVE_COMPUTATION | 1 | none | ABSTAIN_OR_HUMAN_REVIEW | PASS |

## Acceptance

- Comparator verdict: PASS (8/8 task contracts passed; 0 mismatches).
- Eight tasks completed: 8.
- Routes observed: DESCRIPTIVE_COMPUTATION, DIRECT_EVALUATION, EXACT_LOOKUP, REGISTERED_OPERATOR, STOP.
- Post-action statuses observed: FAIL, NOT_APPLICABLE, PASS, UNRESOLVED.
- Terminal states observed: ABSTAIN_OR_HUMAN_REVIEW, CANNOT_SUPPORT_REQUESTED_CLAIM, SUPPORT_WITHIN_CEILING.
- Same-Rule unresolved-to-PASS closures: 2.
- EvidenceResults recorded: 3.
- Unauthorized tool calls: 0.
- Mutation-guard passes: 8/8.
- Claim-ceiling source checks: 8/8.

Generated JSON canonicalizes floating values to 12 decimal places for cross-platform artifact reconstruction; it does not alter RuleResult status, EvidenceResult target, or claim ceiling.

## Boundaries

T1-T4 are synthetic contract fixtures, not paper-derived scientific validation. T5-T7 reuse exposed development assets. T8 is DESCRIPTIVE_NO_ACTIVE_RULE_CONTROL: it records static descriptive evidence without creating a Rule closure and does not test Rule-driven computation routing. Every ConclusionPacket retains scientific_disposition = NOT_EVALUATED and a human decision gate. The suite does not test paper extraction, automatic family selection, general routing, family coverage, Rules validation, Agent value, held-out transfer, or H1. No canonical Rule, source record, or scientific disposition changed.
