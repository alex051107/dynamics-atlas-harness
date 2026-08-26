# Rules Prototype v1 — PR1B Review Packet

## Review disposition

This is the first post-PR4 Rules Draft. This bounded remediation is ready for human merge review only after the final repository check and GitHub CI readback. It remains proposal-only: it does not activate a Rule, replace the active v0.3 runtime, authorize an Operator, introduce an Agent, or authorize its own merge.

PR4 merged the architecture baseline at `main@7c0f602`. This Draft closes the next, tightly bounded prerequisite layer:

- F02R01 was narrowed from a broad construct declaration to a SOURCE sample-system/composition declaration;
- F02R02 may classify an explicitly declared EDGE condition relation only after both endpoint F02R01 results pass;
- F03R01 records SOURCE-native measurement semantics;
- a guarded, proposal-local `EvaluationContext` stores freshly produced Draft F02R01, F02R02, and F03R01 results derived from declared fixture fields; and
- one explicit F06 replay proves that same-run Draft prerequisites, rather than a seeded stand-in, control the F06R02 result.

The evaluator still emits no terminal scientific `SUPPORT` or `CANNOT_SUPPORT` verdict. Every result remains a local Draft classification for the HumanDecisionGate.

## Review decisions

| Family | Architecture decision | Source-grounding decision | Runtime readiness | Review disposition |
| --- | --- | --- | --- | --- |
| F01 Claim Contract and Ceiling | `APPROVE_AFTER_MINOR_FIX` — fixed in this commit; the registry records final `APPROVE` | `SEP-F01-CLAIM-CONTRACT` is `LOCATOR_REVIEWED_FOR_PROPOSED_CONTROL_LOGIC`; F01's remaining packet is pending domain review | `NOT_READY` for active runtime | The intake contract and requested-wording scope are distinct from a future evidence-supported ceiling. |
| F02 System Construct and Condition | `APPROVE` | `PENDING_DOMAIN_REVIEW` | `NOT_READY` for active runtime | F02R01 now records only sample-system/composition context; F02R02 records a declared condition relation. |
| F03 Source Measurement Semantics | `APPROVE` | `PENDING_DOMAIN_REVIEW` | `NOT_READY` for active runtime | F03R01 records native measurement semantics before a relation-level comparison. |
| F04 Source Reliability and Uncertainty | `REVISE` | `PENDING_DOMAIN_REVIEW` | `DEFER` | Keep a generic provenance umbrella separate from method-specific profiles. |
| F05 Representation Support and Forward Bridge | `REVISE` | `PENDING_DOMAIN_REVIEW` | `DEFER` | Keep candidate-support coverage and forward-bridge validity separate; determine the target in a later method profile. |
| F06 Cross-source Comparability and Evidence Role | `REVISE` | `PENDING_DOMAIN_REVIEW` | `NOT_READY` for active runtime | F06R02 now replays same-run Draft F02R02/F03R01 results; the SOURCE role / EDGE comparability / EDGE independence split remains proposal-only. |
| F07 Identifiability and Next Discriminating Action | `DEFER` | `PENDING_DOMAIN_REVIEW` | `DEFER` | It belongs after the source and edge rules can supply reviewable unresolved metadata. |

No family is active. The source-packet dispositions below support narrow control logic only; family-level source grounding still awaits domain review.

## What this Draft contains

| Item | Current scope |
| --- | --- |
| Human-facing families | 7 |
| Candidate runtime sub-rules | 12 |
| Complete Draft sub-rules | 8: F01R01, F01R02, F02R01, F02R02, F03R01, F06R01, F06R02, and F06R03 |
| Candidate-map-only sub-rules | 4: F04R01, F05R01, F05R02, and F07R01 |
| Source Evidence Packets | 12 review derivatives; four are `LOCATOR_REVIEWED_FOR_PROPOSED_CONTROL_LOGIC` and eight remain pending |
| Behavioral scenarios | 48 cases across positive, one-field-negative, missing-evidence, wrong-target, conflict, request-scope, unknown-status, dependency, and mixed-failure conditions |
| Focused Rules-v1 validation | 15 of 15 tests passed |
| Repository discovery validation | 39 discovered; 37 passed; 2 workspace-dependent tests skipped in GitHub CI |

The evaluator never emits a terminal scientific `SUPPORT` or `CANNOT_SUPPORT` verdict in this PR. Each RuleResult instead carries a local route, decision class, and claim ceiling for human review.

## Architecture boundary

The proposal keeps scientific facts and evaluator state separate:

```text
Canonical CaseGraph
  -> selected single-target RuleInstance
  -> Resolution Policy and Evaluation Contract
  -> RuleResult
  -> EvaluationContext (keyed by stable RuleInstance ID)
  -> downstream RuleInstance, where a declared dependency exists
  -> HumanDecisionGate
```

`CaseGraph` records CASE, SOURCE, and EDGE facts. `EvaluationContext.rule_results_by_instance` holds post-evaluation state keyed as `<runtime_subrule_id>::<target_kind>::<target_id>`. It is not a CaseGraph field and not scientific evidence. The two declaration-status fields are derived/attested Draft fields: synthetic fixtures provide them only as test inputs, and a future Agent may propose raw facts or locators but may not self-assign `DECLARED` as an authoritative input to F02R01 or F03R01.

PR1B uses two fixed phases rather than a generic graph engine. The first phase runs and stores F02R01 for each SOURCE, F02R02 on the current EDGE, and F03R01 for each SOURCE. The second phase runs F01/F06 against that fresh Context. The Context accepts only emitted statuses with nonempty CASE, SOURCE, or EDGE IDs; it rejects `UNKNOWN` fallback IDs, mismatched identities, duplicate writes, and `NOT_RUN`. F06 results are not stored.

The evaluator uses this precedence for applicable targets:

```text
known fatal FAIL
  -> generic missing evidence
  -> explicit UNRESOLVED
  -> explicit PASS
  -> default UNRESOLVED
```

A three-valued fatal scan prevents a missing, unrelated field from hiding a confirmed contradiction. The mixed fixture therefore returns `FAIL` when `condition_relation = MISMATCH` even when `bridge_status` is absent. A failure predicate that itself relies on missing evidence remains unresolved rather than fabricating a failure.

The declared route vocabulary is:

1. `DIRECT_EVALUATION`
2. `SOURCE_LOOKUP`
3. `REGISTERED_OPERATOR`
4. `HUMAN_OR_NEW_DATA`

`SOURCE_LOOKUP` is declared-only. There is no lookup executor, `EvidenceLookupResult`, RAG component, web search, undeclared-paper retrieval, Operator route, or Agent in this Draft.

## F06 dependency semantics

F06R02 evaluates EDGE comparability. It may pass only after same-run Draft `PASS` results for F02R02 on the current EDGE and F03R01 on each source referenced by that EDGE. F02R02 itself may pass only after both endpoint F02R01 results pass and the edge condition relation is explicitly `MATCHED`. The dependency grammar is `PRIOR_RESULT_STATUS`; it reads `EvaluationContext` and does not write a result into CaseGraph.

The replay test begins with a fresh, empty Context. Complete declared fixture fields yield two F02R01 `PASS` results, F02R02 `PASS`, two F03R01 `PASS` results, then F06R02 `PASS`. Deleting one sample-composition field yields its F02R01 `UNRESOLVED`, F02R02 `UNRESOLVED`, and F06R02 `UNRESOLVED`. A contradicted source declaration yields a source-local F02R01 `FAIL` but leaves F02R02 and F06R02 `UNRESOLVED` unless the edge itself explicitly records `MISMATCH`. Deleting one F03 measurement field yields F03R01 `UNRESOLVED` and F06R02 `UNRESOLVED`; an explicit F02R02 mismatch yields F06R02 `FAIL`.

The legacy seeded Context fixture remains only for direct `evaluate_rule_instance` coverage. `evaluate_active_rules` rejects every nonempty Context, including a preseeded result for a phantom endpoint, so a caller cannot bypass F02/F03 production.

F06R03 evaluates DATA / LINEAGE / SHARED-ERROR independence only. It reads `validation_independence`, `shared_error_status`, and `data_lineage_status`. It does not require condition compatibility or an F02/F03 result. A relation can therefore be independent but non-comparable: the fixture reports `F06R02 = FAIL` and `F06R03 = PASS` for that state.

A future Stage-2 aggregator may decide how a comparability result and an independence result combine. This Draft does not implement that aggregator.

## Source-grounding boundary

Each Source Evidence Packet is a review derivative with a locator, atomic statement, proposed reusable use, and forbidden generalization. The runtime registry stores only packet IDs and does not copy source passages into executable bindings.

`SEP-F01-CLAIM-CONTRACT`, `SEP-F02-CONSTRUCT`, `SEP-F02-CONDITION`, and `SEP-F03-MEASUREMENT` are marked `LOCATOR_REVIEWED_FOR_PROPOSED_CONTROL_LOGIC`. Each disposition is narrow. It supports the stated Draft control rule and is not a domain-review decision, source-science verification, full CaseGraph-schema approval, numerical threshold, reliability determination, validation determination, or claim ceiling.

The other eight packet records retain `PENDING`. At the family review layer, every family remains `PENDING_DOMAIN_REVIEW`; none of these packet dispositions is final scientific approval. This keeps the source-derivative boundary explicit.

| Packet used by a complete Draft sub-rule | Atomic statement | Explicit limit |
| --- | --- | --- |
| SEP-F01-CLAIM-CONTRACT | Intended use determines which evaluation criterion and evidence constraints are meaningful for an ensemble claim. | Declaring a question does not validate a source or a scientific conclusion. |
| SEP-F02-CONSTRUCT | Sample-system and composition context determine whether a source can be treated as a homogeneous single-species ensemble. | It does not prescribe a full construct-metadata schema. |
| SEP-F02-CONDITION | Conditions and known perturbations must be assessed before a relation is treated as one conformational ensemble. | It sets no universal compatibility tolerance and no validation label. |
| SEP-F03-MEASUREMENT | Declared observable, representation, support, and averaging semantics distinguish a source-native measurement from a differently transformed quantity. | A complete declaration does not prove reliability, comparability, or a scientific verdict. |
| SEP-F01-REQUESTED-WORDING-SCOPE | Different claim levels require different supporting evidence. | An intake scope check does not calculate an evidence-supported ceiling. |
| SEP-F06-SOURCE-ROLE | Evidence role is distinct from independent validation. | A validation label alone does not establish independence. |
| SEP-F06-COMPARABILITY | A cross-source relation needs an explicit relation type and bridge; non-comparability is a valid outcome. | The runner does not force numeric equivalence. |
| SEP-F06-INDEPENDENCE | Agreement alone does not establish an independent validation relationship. | Same-data or shared-error agreement cannot receive a held-out label. |

## Runtime sub-rule map

Every runtime sub-rule has exactly one target.

| Runtime sub-rule | Family | Target | State | Evidence packet |
| --- | --- | --- | --- | --- |
| F01R01 Case Claim Declaration | F01 | CASE | Complete Draft | SEP-F01-CLAIM-CONTRACT |
| F01R02 Case Requested Wording Scope | F01 | CASE | Complete Draft | SEP-F01-REQUESTED-WORDING-SCOPE |
| F02R01 Source Sample-System / Composition Declaration | F02 | SOURCE | Complete Draft | SEP-F02-CONSTRUCT |
| F02R02 Edge Condition Compatibility | F02 | EDGE | Complete Draft | SEP-F02-CONDITION |
| F03R01 Source Native Measurement | F03 | SOURCE | Complete Draft | SEP-F03-MEASUREMENT |
| F04R01 Source Reliability Provenance | F04 | SOURCE | Candidate map only | SEP-F04-RELIABILITY |
| F05R01 Source Candidate Support | F05 | SOURCE | Candidate map only | SEP-F05-SUPPORT |
| F05R02 Source Forward Bridge | F05 | SOURCE | Candidate map only | SEP-F05-FORWARD-BRIDGE |
| F06R01 Source Evidence Role | F06 | SOURCE | Complete Draft | SEP-F06-SOURCE-ROLE |
| F06R02 Edge Comparability | F06 | EDGE | Complete Draft | SEP-F06-COMPARABILITY |
| F06R03 Edge Validation Independence | F06 | EDGE | Complete Draft | SEP-F06-INDEPENDENCE |
| F07R01 Case Identifiability | F07 | CASE | Candidate map only | SEP-F07-IDENTIFIABILITY |

## Behavioral evidence

Focused command:

```text
PYTHONPATH=src python3 -m unittest discover -s tests/rules_v1 -p 'test_*.py' -v
```

Result: 15 of 15 passed.

Repository-discovery command:

```text
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

GitHub result: 39 discovered; 37 passed; 2 workspace-dependent tests skipped; CI status `SUCCESS`. Default discovery includes every `rules_v1.test_*` module, so the existing GitHub workflow can cover the Rules-v1 package without a special test command. A local workspace run may execute the workspace-dependent tests; it is not reported as the GitHub result.

The matrix exercises all eight complete sub-rules with positive, one-field-negative, missing-evidence, wrong-target, and conflict behavior. It also checks that `UNKNOWN`, `UNRESOLVED`, and unknown vocabulary do not become `PASS`; they remain `UNRESOLVED`. The mixed scenario preserves fatal-failure precedence. The replay checks prove that freshly produced Draft F02R01/F02R02/F03R01 results derived from declared fixture fields drive F06R02 while F06R03 remains an independent lineage/shared-error decision. PR1B does not infer these fields from raw papers or data and does not validate source science.

## Stop point

This PR1B Draft stops after review. It does not authorize its own merge or any next implementation layer.

The following remain outside PR1B: Stage-2 scientific verdicts, HSP90 Rule-to-Operator work, Operators, live Profiler or Planner Agents, RVC, ADK portability, fourth-protein work, and held-out evaluation.
