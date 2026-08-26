# Exposed real-case vertical slice v1-alpha

This directory is the first case-driven artifact after the proposal-only Rules v1-alpha merge. It is deliberately narrow:

- one projection of the exposed `lincoff_2020_xeisd_maintext` v0.3 metadata asset;
- two source records, one candidate-pool/J-coupling edge, and exact local `XEI-M03`/`XEI-M04` attestation markers;
- the merged F01/F02/F03/F06 evaluator, without a second evaluator or scheduler; and
- three route fixtures: complete lookup then direct bounded review, missing composition then abstain, and explicit condition mismatch then a blocked relation.

`xeisd_case_projection_seed_v1.json` retains the raw case identity and a relative frozen-input path in `projection_provenance`. The subprojection has its own case ID so it cannot be mistaken for the original v0.3 CaseGraph. `frozen_inputs/provenance_manifest_v1.json` records every upstream path/hash, fixture hash, and extraction boundary needed for this repository-contained slice.

The lookup executor reads only the exact local review derivative declared in the allowlist. Its fixed `lookup_kind` is `EXACT_REVIEW_DERIVATIVE_ATTESTATION`; it verifies the frozen derivative hash and exact locator marker, then returns a `SOURCE_LOOKUP` route receipt. A deterministic helper derives Draft declaration-status fields from the successful receipt plus existing source fields. It does not search the web, parse arbitrary documents, certify source science, or silently normalize the raw edge record: the allowlist records that raw `DOCUMENTED` bridge evidence maps only to a Draft declared-bridge control label.

`F06R03` is retained as `NOT_APPLICABLE` for this pair because no validation claim is asserted. It is not silently counted as an independence result. Each packet separates `route_disposition` (`RELATION_REVIEWABLE`, `RELATION_BLOCKED`, or `ABSTAIN`) from `scientific_disposition = NOT_EVALUATED`, retains a HumanDecisionGate, and forbids shared-population, independent-validation, kinetics, mechanism, or final-science wording.

## Case B: HSP90 Rule-to-Operator closure

`hsp90_case_dossier_v1.json` starts from the pre-existing HSP90 time-anatomy
question: whether the declared 40-trajectory, ordered two-readout packet has a
fixed-horizon directional-block control record. The new local overlay has one
SOURCE-targeted F04 rule, `F04R02_SOURCE_DECLARED_TIME_ANATOMY_CONTROL`. It is
not a generic reliability rule, a new F05 forward-model rule, or a new PR1B
phase. Before execution it produces the real unresolved gap
`COMPUTABLE_TIME_ANATOMY_CONTROL_EVIDENCE_MISSING`.

The exact route is constrained by:

- `hsp90_operator_input_manifest_v1.json`, which binds the case, source,
  RuleInstance, implementation, two inputs, hashes, 40-by-1001 time contract,
  and `[5, 20, 50]` grid;
- the case-bound registered Operator
  `hsp90.directional_time_anatomy.v1_case_bound`; and
- `hsp90_time_anatomy_output_v1.schema.json` plus the deterministic validator,
  which checks the four output files, input hashes, grid, trajectory cohort,
  row identities, and claim-boundary text.

`ExecutionEvidenceContext` is a runtime provenance boundary rather than a
deserializable evidence map. It admits this route only after it revalidates the
fixed receipt and frozen output directory against the current manifest and
`ROSTER_PASS` case-bound OperatorSpec. That shared-registry entry is explicitly
`EXPOSED_DEVELOPMENT_ACTIVE`, `EXACT_CASE_BOUND`, `NOT_GENERAL`, and
`NOT_PRODUCTION`; its case/source/profile/sub-rule constraints are executable
route guards. A prefilled `PASS` label, a CaseGraph stride/window mismatch, a
wrong case, or a forged PASS RuleResult therefore cannot turn this obligation
into a PASS or materialize a scientific disposition.

The original `hsp90.directional_time_anatomy.v0` canary remains unchanged and
non-routable. The v1 entry reuses the same standard-library implementation but
adds the missing case/input binding and output contract. It can route only the
F04R02 HSP90 RuleInstance; an unrelated HSP90 label, MD source, or canary cannot
select it.

`outputs/hsp90_b1_rule_to_operator/` records the actual exposed run:

```text
F04R02 UNRESOLVED
  -> exact exposed-development ROSTER_PASS resolution
  -> registered Operator receipt and validated EvidenceResult
  -> F04R02 PASS
  -> RULE_CONTRACT_PASS route disposition
```

That final route disposition means only that the exact same-packet control record
validated. `scientific_disposition` remains `NOT_EVALUATED`; it does not validate
source science or emit a biological, kinetic, equilibrium, population, free-energy,
pathway, mechanism, or mutation claim.
