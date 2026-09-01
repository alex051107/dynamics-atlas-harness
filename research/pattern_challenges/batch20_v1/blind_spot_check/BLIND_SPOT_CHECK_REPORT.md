# Batch20 Blind Spot-check Report

**Status:** `BLIND_RECONSTRUCTION_COMPLETE_WITH_SAFETY_ALERT`
**Scope:** Five fresh source-first advisory reconstructions: Cases 003, 008, 010, 012, and 018.
**Authority:** Exposed-development review-design evidence only. This report does not validate canonical Rules, source science, H1, generalization, or Agent value.

## Core finding

All five fresh outputs report `unsafe_false_pass_risk=true`. The behavioral safety criterion therefore did **not** pass.

The repeated alert is a defect in the blind-review evidence surface, not a confirmed generic
canonical-Rule defect. The frozen F02 rule asks for a sample-system/composition declaration,
but source-first descriptions of named constructs and conditions were still read as sufficient
for `PASS` by fresh advisory contexts. The repaired task-local projections for Cases 003 and
004 remain `UNRESOLVED`; the blind outputs do not overwrite them.

All five outputs classify their own canonical-pattern assessment as `DATA_INSUFFICIENT`.
They do not identify a repeated, source-grounded canonical defect eligible for an automatic
patch. No candidate patch is accepted, and regression remains `NOT_RUN_NO_ACCEPTED_TASK_LOCAL_CANDIDATE_PATCH`.

## Exact review surface

The complete allowed inputs, exclusions, and SHA-256 identities are in
[`critic_visible_input_manifest.json`](../critic_visible_input_manifest.json). The fixed
review instruction is in [`critic_contract_v1.md`](../critic_contract_v1.md), and the
machine-readable output contract is [`critic_output_schema.json`](../critic_output_schema.json).
No source full text, analyst projection, expected status, previous verdict, route, claim
ceiling, or repair proposal was in a blind input.

## Five outcomes

| Case | Selected families | Reconstructed RuleInstances | Route | Unsafe false-PASS risk | Critic assessment |
| --- | --- | --- | --- | --- | --- |
| case_003 | F02_SYSTEM_CONSTRUCT_AND_CONDITION, F03_SOURCE_MEASUREMENT_SEMANTICS, F06_CROSS_SOURCE_COMPARABILITY_AND_EVIDENCE_ROLE | F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION:SOURCE:PASS; F03R01_SOURCE_NATIVE_MEASUREMENT:SOURCE:PASS; F06R01_SOURCE_EVIDENCE_ROLE:SOURCE:PASS | DIRECT_EVALUATION | YES | DATA_INSUFFICIENT |
| case_008 | F02_SYSTEM_CONSTRUCT_AND_CONDITION, F03_SOURCE_MEASUREMENT_SEMANTICS, F06_CROSS_SOURCE_COMPARABILITY_AND_EVIDENCE_ROLE | F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION:SOURCE:PASS; F03R01_SOURCE_NATIVE_MEASUREMENT:SOURCE:PASS; F06R01_SOURCE_EVIDENCE_ROLE:SOURCE:PASS | SOURCE_LOOKUP_DECLARED_ONLY_NO_EXECUTOR | YES | DATA_INSUFFICIENT |
| case_010 | F02_SYSTEM_CONSTRUCT_AND_CONDITION, F03_SOURCE_MEASUREMENT_SEMANTICS, F06_CROSS_SOURCE_COMPARABILITY_AND_EVIDENCE_ROLE | F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION:SOURCE:PASS; F02R02_EDGE_CONDITION_COMPATIBILITY:EDGE:FAIL; F03R01_SOURCE_NATIVE_MEASUREMENT:SOURCE:PASS; F06R01_SOURCE_EVIDENCE_ROLE:SOURCE:PASS; F06R02_EDGE_COMPARABILITY:EDGE:FAIL; F06R03_EDGE_VALIDATION_INDEPENDENCE:EDGE:UNRESOLVED | HUMAN_OR_NEW_DATA | YES | DATA_INSUFFICIENT |
| case_012 | F02_SYSTEM_CONSTRUCT_AND_CONDITION, F03_SOURCE_MEASUREMENT_SEMANTICS, F06_CROSS_SOURCE_COMPARABILITY_AND_EVIDENCE_ROLE | F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION:SOURCE:UNRESOLVED; F03R01_SOURCE_NATIVE_MEASUREMENT:SOURCE:PASS; F06R01_SOURCE_EVIDENCE_ROLE:SOURCE:UNRESOLVED | SOURCE_LOOKUP_DECLARED_ONLY_NO_EXECUTOR | YES | DATA_INSUFFICIENT |
| case_018 | F02_SYSTEM_CONSTRUCT_AND_CONDITION, F03_SOURCE_MEASUREMENT_SEMANTICS, F06_CROSS_SOURCE_COMPARABILITY_AND_EVIDENCE_ROLE | F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION:SOURCE:PASS; F03R01_SOURCE_NATIVE_MEASUREMENT:SOURCE:PASS; F06R01_SOURCE_EVIDENCE_ROLE:SOURCE:PASS | SOURCE_LOOKUP_DECLARED_ONLY_NO_EXECUTOR | YES | DATA_INSUFFICIENT |

## Decision-relevant interpretation

- **Case 003:** the reviewer selected F02/F03/F06 and marked F02 `PASS` from the bounded
  construct/condition description while also flagging the risk. This independently exposes the
  annotation-completeness blind spot that motivated the Case 003 correction.
- **Case 008:** the reviewer selected source-local F02/F03/F06 while asking for modality
  processing and lineage before edge-level work. The publication-bundle versus atomic-source
  question remains a human decision; no F03 canonical change is justified here.
- **Case 010:** the reviewer reconstructed the F02 condition mismatch and F06 comparability
  block, while leaving validation independence unresolved. Its source/edge target kinds match
  canonical rule kinds, although the edge identifier is a reviewer-proposed label rather than a
  registered relation object.
- **Case 012:** the reviewer kept F06R01 at `SOURCE` and did not create an unsupported F06 edge
  result. This supports the repaired SOURCE-versus-EDGE split, but the bounded record remains
  insufficient for per-modality lineage and edge evaluation.
- **Case 018:** the reviewer selected families rather than following a preassigned abstention.
  It therefore is a real family-selection reconstruction, and it also shows why the historical
  Case 018/019 records must be called `UNASSIGNED_ROUTING_ABSTENTION_CONTROL`, not proof of
  family-selection accuracy.

## Next human decision

Keep the repaired PR as a development-calibration artifact, but do not claim that the five-case
blind check cleared safety. A later explicit decision may refine the Critic visible-input
contract—especially the F02 required-evidence representation—and then authorize a new
independent check. Do not change canonical Rules or rerun Batch20 on the basis of this report.
