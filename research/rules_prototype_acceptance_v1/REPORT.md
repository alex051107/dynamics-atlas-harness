# Rules Prototype Acceptance Suite v1

The eight recorded CaseGraphs completed through one bounded development runtime: admission, current Rule evaluation, obligation selection, legal route, EvidenceResult, same-Rule re-evaluation, and a three-state ConclusionPacket. The runtime reads cases.jsonl only; it does not load expected_results.jsonl.

| Task | Legal route | Executed action | EvidenceResults | Rule transition | Terminal state |
| --- | --- | --- | ---: | --- | --- |
| T1_COMPLETE_SOURCE_MEASUREMENT_DECLARATION | DIRECT_EVALUATION | DIRECT_EVALUATION | 0 | none | SUPPORT_WITHIN_CEILING |
| T2_F03_REQUIRED_FIELD_MISSING | SOURCE_LOOKUP | STOP | 0 | none | ABSTAIN_OR_HUMAN_REVIEW |
| T3_EXPLICIT_EDGE_CONDITION_MISMATCH | HUMAN_OR_NEW_DATA | DIRECT_EVALUATION | 0 | none | CANNOT_SUPPORT_REQUESTED_CLAIM |
| T4_WRONG_TARGET_SOURCE_RULE | HUMAN_OR_NEW_DATA | STOP | 0 | none | ABSTAIN_OR_HUMAN_REVIEW |
| T5_XEISD_EXACT_LOOKUP_AVAILABLE | SOURCE_LOOKUP | EXACT_LOOKUP | 1 | UNRESOLVED to PASS | ABSTAIN_OR_HUMAN_REVIEW |
| T6_XEISD_LOOKUP_UNAVAILABLE | SOURCE_LOOKUP | STOP | 0 | none | ABSTAIN_OR_HUMAN_REVIEW |
| T7_HSP90_REGISTERED_OPERATOR_CLOSURE | REGISTERED_OPERATOR | REGISTERED_OPERATOR | 1 | UNRESOLVED to PASS | ABSTAIN_OR_HUMAN_REVIEW |
| T8_ADK_BOUNDED_STRUCTURAL_COMPUTATION | DIRECT_EVALUATION | DESCRIPTIVE_COMPUTATION | 1 | none | ABSTAIN_OR_HUMAN_REVIEW |

## Acceptance

- Eight tasks completed: 8.
- Routes observed: DESCRIPTIVE_COMPUTATION, DIRECT_EVALUATION, EXACT_LOOKUP, REGISTERED_OPERATOR, STOP.
- Post-action statuses observed: FAIL, NOT_APPLICABLE, PASS, UNRESOLVED.
- Terminal states observed: ABSTAIN_OR_HUMAN_REVIEW, CANNOT_SUPPORT_REQUESTED_CLAIM, SUPPORT_WITHIN_CEILING.
- Same-Rule unresolved-to-PASS closures: 2.
- EvidenceResults recorded: 3.
- Unauthorized tool calls: 0.
- Wrong-RuleInstance mutations: 0.
- Unsafe claim upgrades: 0.

## Boundaries

This is a recorded, paper-derived development acceptance suite. SUPPORT_WITHIN_CEILING means only that the selected local Rule contract passed within its explicit ceiling; every ConclusionPacket retains scientific_disposition = NOT_EVALUATED and a human decision gate. The suite does not test paper extraction, family coverage, Rules validation, Agent value, held-out transfer, or H1. No canonical Rule, source record, or scientific disposition changed.
