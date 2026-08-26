# Rules Prototype v1 Review Packet

## Review disposition

This Draft is ready to merge as a **proposal-only Rules architecture baseline** once the final repository test run and GitHub CI pass. It does not activate a Rule, replace the active v0.3 runtime, authorize an Operator, or introduce an Agent.

The prior review disposition was `PASS_TO_ONE_FINAL_BOUNDED_FIX`. This commit closes that bounded fix:

- a confirmed fatal failure is evaluated before a generic missing-evidence return;
- post-evaluation RuleResults are held outside the scientific CaseGraph;
- F06R03 evaluates independence only, rather than rechecking comparability prerequisites;
- the review record now distinguishes architecture, source grounding, and runtime readiness.

## Review decisions

| Family | Architecture decision | Source-grounding decision | Runtime readiness | Review disposition |
| --- | --- | --- | --- | --- |
| F01 Claim Contract and Ceiling | `APPROVE_AFTER_MINOR_FIX` — fixed in this commit; the registry records final `APPROVE` | `SEP-F01-CLAIM-CONTRACT` is `VERIFIED_FOR_PROPOSED_CONTROL_LOGIC`; F01's remaining packet is pending domain review | `NOT_READY` for active runtime | The intake contract and requested-wording scope are distinct from a future evidence-supported ceiling. |
| F02 System Construct and Condition | `APPROVE` | `PENDING_DOMAIN_REVIEW` | `READY_FOR_NEXT_DRAFT` | Implement next as two single-target prerequisites. |
| F03 Source Measurement Semantics | `APPROVE` | `PENDING_DOMAIN_REVIEW` | `READY_FOR_NEXT_DRAFT` | Implement next as the source-native measurement prerequisite. |
| F04 Source Reliability and Uncertainty | `REVISE` | `PENDING_DOMAIN_REVIEW` | `DEFER` | Keep a generic provenance umbrella separate from method-specific profiles. |
| F05 Representation Support and Forward Bridge | `REVISE` | `PENDING_DOMAIN_REVIEW` | `DEFER` | Keep candidate-support coverage and forward-bridge validity separate; determine the target in a later method profile. |
| F06 Cross-source Comparability and Evidence Role | `REVISE` | `PENDING_DOMAIN_REVIEW` | `NOT_READY` for active runtime | The three-way SOURCE role / EDGE comparability / EDGE independence split remains provisional until real F02/F03 results exist. |
| F07 Identifiability and Next Discriminating Action | `DEFER` | `PENDING_DOMAIN_REVIEW` | `DEFER` | It belongs after the source and edge rules can supply real unresolved evidence. |

No family is active. `READY_FOR_NEXT_DRAFT` authorizes proposal work only; it is not scientific approval or production/runtime activation.

## What this Draft contains

| Item | Current scope |
| --- | --- |
| Human-facing families | 7 |
| Candidate runtime sub-rules | 12 |
| Complete Draft sub-rules | 5: F01R01, F01R02, F06R01, F06R02, and F06R03 |
| Candidate-map-only sub-rules | 7, including F02R01, F02R02, and F03R01 |
| Source Evidence Packets | 12 review derivatives; one has a narrow control-logic disposition and the other 11 remain pending |
| Behavioral scenarios | 32 cases across positive, one-field-negative, missing-evidence, wrong-target, conflict, request-scope, unknown-status, dependency, and mixed-failure conditions |
| Focused Rules-v1 validation | 14 of 14 tests passed |
| Repository discovery validation | 38 of 38 tests passed through default unittest discovery |

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

`CaseGraph` records CASE, SOURCE, and EDGE facts. `EvaluationContext.rule_results_by_instance` records post-evaluation statuses, keyed as `<runtime_subrule_id>::<target_kind>::<target_id>`. It is a proposal-local input, not a CaseGraph field and not scientific evidence. The positive fixture supplies stand-in prior results only to exercise wiring; they are not F02/F03 evaluations and establish no cross-source scientific conclusion.

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

F06R02 evaluates EDGE comparability. It may pass only after separately stored `PASS` results for F02R02 on the current EDGE and F03R01 on each source referenced by that EDGE. The dependency grammar is `PRIOR_RESULT_STATUS`; it reads `EvaluationContext` and does not write a result into CaseGraph.

F06R03 evaluates DATA / LINEAGE / SHARED-ERROR independence only. It reads `validation_independence`, `shared_error_status`, and `data_lineage_status`. It does not require condition compatibility or an F02/F03 result. A relation can therefore be independent but non-comparable: the fixture reports `F06R02 = FAIL` and `F06R03 = PASS` for that state.

A future Stage-2 aggregator may decide how a comparability result and an independence result combine. This Draft does not implement that aggregator.

## Source-grounding boundary

Each Source Evidence Packet is a review derivative with a locator, atomic statement, proposed reusable use, and forbidden generalization. The runtime registry stores only packet IDs and does not copy source passages into executable bindings.

`SEP-F01-CLAIM-CONTRACT` is marked `VERIFIED_FOR_PROPOSED_CONTROL_LOGIC` under a narrow scope: intended use determines which evaluation criterion and evidence constraints are meaningful for an ensemble claim. It does not validate the Atlas CASE schema, deterministic predicates, source validation, or an evidence-supported claim ceiling.

The other eleven packet records retain `PENDING`. At the family review layer, that is recorded as `PENDING_DOMAIN_REVIEW`; none of those derivatives is primary-source approval. This distinction preserves the existing packet schema while making the human-review status explicit.

| Packet used by a complete Draft sub-rule | Atomic statement | Explicit limit |
| --- | --- | --- |
| SEP-F01-CLAIM-CONTRACT | Intended use determines which evaluation criterion and evidence constraints are meaningful for an ensemble claim. | Declaring a question does not validate a source or a scientific conclusion. |
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
| F02R01 Source Construct Declaration | F02 | SOURCE | Candidate map only | SEP-F02-CONSTRUCT |
| F02R02 Edge Condition Compatibility | F02 | EDGE | Candidate map only | SEP-F02-CONDITION |
| F03R01 Source Native Measurement | F03 | SOURCE | Candidate map only | SEP-F03-MEASUREMENT |
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

Result: 14 of 14 passed.

Repository-discovery command:

```text
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Result: 38 of 38 passed. Default discovery includes every `rules_v1.test_*` module, so the existing GitHub workflow can cover the Rules-v1 package without a special test command.

The matrix exercises all five complete sub-rules with positive, one-field-negative, missing-evidence, wrong-target, and conflict behavior. It also checks that `UNKNOWN`, `UNRESOLVED`, and unknown vocabulary do not become `PASS`; they remain `UNRESOLVED`. The new mixed scenario proves fatal-failure precedence. The two F06 scenarios prove that F06R02's context dependency is separate from F06R03's independence finding.

## Scope after merge

After this PR is merged, the only authorized next branch is `feature/rules-v1-f02-f03-prerequisites`. That Draft may implement:

- F02R01 Source Construct Declaration;
- F02R02 Edge Condition Compatibility;
- F03R01 Source Native Measurement;
- a minimal writable `EvaluationContext` / RuleResult store; and
- one F06 dependency replay using real F02/F03 RuleResults.

The next Draft must review the F02 construct, F02 condition, and F03 measurement packets plus at most one necessary supporting source. It must retain explicit `PASS`, `FAIL`, `UNRESOLVED`, and default-`UNRESOLVED` behavior.

The following remain outside this PR and the next F02/F03 Draft: Stage-2 scientific verdicts, HSP90 Rule-to-Operator work, Operators, live Profiler or Planner Agents, RVC, ADK portability, fourth-protein work, and held-out evaluation.
