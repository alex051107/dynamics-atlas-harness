# Batch20 Frozen Rules Pattern Audit — Bounded Repair Update

**Development status:** `BLIND_RECONSTRUCTION_COMPLETE_WITH_SAFETY_ALERT`
**Authority boundary:** exposed-development calibration only; not H1 approval, Rules release,
held-out evaluation, generalization evidence, scientific approval, or Agent-value proof.

## Core outcome

The 20 frozen Pass A records, 20 frozen v1 Pass B projections, and all existing Critic
outputs are preserved. The bounded repair corrected three origin-accounting entries, the
mixed SOURCE/EDGE projections in Cases 011–012, the F02 over-strong local annotations in
Cases 003–004, candidate-map aggregation, and the routing-control label. It also added an
auditable Critic contract, schema, five exact visible inputs, and five fresh blind outputs.

The fresh blind check did not clear its safety criterion: 5/5 outputs report
`unsafe_false_pass_risk=true`. This is evidence that the supplied blind review surface can
still turn partial construct/condition context into a `PASS`. The result is a Critic-contract
blind spot; it is not a canonical Rule amendment and it does not rewrite a frozen projection.

## Existing confirmation reviews, correctly separated

| Interpretation class | Cases | Count | Meaning |
| --- | --- | ---: | --- |
| `COMPLETE_DRAFT_APPROVE_KEEP_CONFIRMATION` | 001–002, 006–012, 020 | 10 | Existing critics did not find an obvious contradiction in an already supplied complete-draft projection. They did not independently reconstruct it. |
| `CANDIDATE_MAP_KEEP_DEFERRED` | 013–017 | 5 | Existing critics retained a candidate/deferred state; these are not executable generic PASS/FAIL evidence. |
| `UNASSIGNED_ROUTING_ABSTENTION_CONTROL` | 018–019 | 2 | Existing critics confirmed preassigned safe abstention; they were not family-selection accuracy tests. |
| `PENDING_MODEL_REVIEW` | 003–005 | 3 | Historical confirmation-style review is still pending. Case 003 separately has a fresh blind output. |

Do not compress these four rows into “17/17 KEEP.”

## Repaired factual and scope record

- `not_target_rule_origin_units` is **17**, not 20. Cases 006–007 are Fuertes/F03R01
  grounding units; Case 012 is Bengtsen/F06R01/F06R03 grounding.
- Cases 011–012 now record F06R01 as `SOURCE` instances and F06R02/F06R03 as `EDGE`
  instances in a post-freeze repair overlay. Their frozen Pass B fields remain available for
  historical comparison.
- Cases 003–004 now have post-freeze F02 `UNRESOLVED` overlays because the bounded locators
  do not provide an exact sample-composition declaration. Case 005 remains `UNRESOLVED`.
- Case 008 retains a human question about publication-bundle versus atomic modality source
  granularity. No F03 canonical decision follows.

## Candidate patch and regression

No task-local candidate patch is accepted. The repeated blind alert concerns the evidence
surface of this Critic contract, not a demonstrated canonical-Rule defect across independent
source units. `candidate_vnext_patch.json` therefore remains no-patch, and regression remains
`NOT_RUN_NO_ACCEPTED_TASK_LOCAL_CANDIDATE_PATCH`.

## Claim ceiling

This PR can state that Batch20 produced a preserved exposed-development calibration corpus,
corrected task-local records, an auditable visible-input contract, and five blind advisory
outputs that exposed an unresolved review-design safety gap. It cannot state that Rules are
scientifically validated, that generalization is established, that candidate families are
executable, that H1 passed, or that Agent value is established.
