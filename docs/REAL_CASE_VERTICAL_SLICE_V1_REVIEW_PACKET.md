# Real-Case Vertical Slice v1 — Review Packet

## Decision requested

Review whether this branch establishes the bounded no-Agent Milestone A on two
exposed development cases. It does not request source-science approval, a final
scientific conclusion, a generic Stage-2 engine, a Live Agent, ADK portability,
or held-out authorization.

## Why this change exists

PR #5 established a proposal-only Rules v1-alpha prerequisite baseline. The
highest-value next check was whether those contracts could drive real-case
actions. This branch closes that question with two local, provenance-carrying
paths instead of extending synthetic fixtures or building a scheduler.

| Case | Real question | Emitted gap / action | Resulting bounded route |
| --- | --- | --- | --- |
| X-EISD | Can the selected candidate-pool/J-coupling relation be reviewed from declared local metadata? | Exact allowlisted source lookup where the frozen source lacks a needed declaration | Direct bounded review, explicit abstain for missing composition, and relation-only failure for an explicit mismatch |
| HSP90 | Does the existing round-2 MD packet have the fixed trajectory-level time-anatomy control record required for its declared same-packet diagnostic? | `F04R02_SOURCE_DECLARED_TIME_ANATOMY_CONTROL` emits `COMPUTABLE_TIME_ANATOMY_CONTROL_EVIDENCE_MISSING` | Exact registered Operator, validated EvidenceResult, reevaluation of the affected RuleInstance |

## Case A: X-EISD

The branch retains a two-source/one-edge projection of the frozen
`lincoff_2020_xeisd_maintext` v0.3 asset. It uses no web access or arbitrary
document search. The allowlist accepts only the declared local derivative and
exact locator markers, then the existing Rules-v1 evaluator produces fresh Draft
RuleResults.

The three pre-registered behaviors are present in
`evidence/real_case_vertical_slice_v1/outputs/`:

1. `A1_COMPLETE_LOOKUP_THEN_DIRECT`: exact local lookup results lead to a
   bounded `DIRECT_EVALUATION` route.
2. `A2_MISSING_COMPOSITION`: removing a source composition declaration produces
   `ABSTAIN_OR_HUMAN_REVIEW`; F02R01 is the first failed dependency.
3. `A3_EXPLICIT_CONDITION_MISMATCH`: an explicit edge mismatch produces
   `CANNOT_SUPPORT_REQUESTED_CLAIM` for the relation only.

Each X-EISD packet remains `NOT_EMITTED_PROPOSAL_ONLY`. A declared field is not
treated as a validated source fact or a scientific comparability result.

## Case B: HSP90

The Case B question comes from the prior HSP90 time-anatomy task specification,
not from the existence of a script. It asks whether a defined, same-packet
two-readout directional diagnostic has its required time-semantics and
persistence-sensitivity control evidence. The initial F04R02 RuleResult is
therefore a genuine unresolved computation obligation.

The original `hsp90.directional_time_anatomy.v0` remains `CANARY_PASS` and
non-routable. This branch adds a separate
`hsp90.directional_time_anatomy.v1_case_bound` OperatorSpec. It reuses the
existing standard-library implementation while freezing the missing executable
contract:

- exact CaseGraph, source, RuleInstance, method profile, and capability;
- immutable implementation and two input hashes;
- the 20–1020 ns / 1 ns / 40 trajectory / 1001 frame contract;
- fixed `[5, 20, 50]` persistence parameters; and
- exact output validation for the four expected files, trajectory/horizon rows,
  cohort, input hashes, and claim-boundary wording.

The HSP90 execution context is deliberately not a JSON preload surface. It admits
an EvidenceResult only by revalidating the exact case-bound receipt against the
current manifest, roster entry, fixed output directory, output hashes, and saved
summary. A copied `contract_status=PASS`, a mismatched time contract, or a forged
RuleResult cannot produce a `PASS` RuleResult or a `SUPPORT_WITHIN_CEILING`
ConclusionPacket.

The generated receipt confirms the specific state transition:

```text
F04R02 UNRESOLVED
  -> REGISTERED_OPERATOR
  -> EvidenceResult contract_status=PASS
  -> F04R02 PASS
```

The resulting `SUPPORT_WITHIN_CEILING` means only that the frozen same-packet
control record validates. The EvidenceResult is still marked
`PENDING_HUMAN_VALIDATION`, and the ConclusionPacket emits no final scientific
verdict. It expressly rejects transition-rate, equilibrium, population,
free-energy, pathway, mechanism, and mutation wording.

## Behavioral evidence

The focused real-case suite covers:

- X-EISD raw-metadata fail-closed behavior, exact lookup, missing composition,
  explicit mismatch, duplicate receipt, unsafe status patch, and duplicate
  allowlist rejection;
- HSP90 initial real obligation, exact roster/manifest match, CANARY_PASS stop,
  wrong target, manifest-hash mismatch, actual output validation, preseeded
  context rejection, CaseGraph-to-manifest time-contract mismatch, forged-PASS
  packet rejection, duplicate EvidenceResult rejection, and isolated
  reevaluation of F04R02.

The test command is:

```text
PYTHONPATH=src python3 -m unittest tests.real_cases_v1.test_xeisd_vertical_slice tests.real_cases_v1.test_hsp90_vertical_slice -v
```

## Explicitly out of scope

- No active v0.3 selector/runtime change.
- No generic dependency scheduler or generic Operator router.
- No new Rule family; Case B adds one case-bound F04 control rule and no F05
  rule.
- No web/RAG, SQLite/state service, MCP, RVC, Live Agent, ADK, held-out case,
  or unregistered tool call.
- No source-science approval, scientific claim upgrade, transfer claim, or Agent
  evaluation.

## Review decision boundary

Approve only the exposed no-Agent route integrity and bounded implementation.
The next decision after approval is whether to begin the separately authorized
Live-Agent exposed-case slice; this packet alone does not authorize that work.
