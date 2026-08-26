# Rules Prototype v1 Review Packet

## Review request

This is a Draft, proposal-only Rules Prototype. It makes the Rules layer inspectable before any rule is activated, any Operator is routed, or any Agent is introduced.

This packet separates three decisions that the first version incorrectly compressed into one approval:

- `architecture_decision`: APPROVE, REVISE, REJECT, or DEFER.
- `source_grounding_decision`: VERIFIED, PENDING_DOMAIN_REVIEW, or REJECTED.
- `runtime_readiness`: READY_FOR_NEXT_DRAFT, NOT_READY, or DEFER.

The review directions below do not verify a primary-source entailment and do not activate runtime behavior. Every Source Evidence Packet remains `PENDING_DOMAIN_REVIEW`.

## What this Draft delivers

| Item | Result |
| --- | --- |
| Human-facing families | 7 |
| Candidate runtime sub-rules | 12 |
| Fully executable Draft sub-rules | 5, covering F01 and F06 |
| Candidate-map-only sub-rules | 7, covering F02, F03, F04, F05, and F07 |
| Source Evidence Packets | 12 review derivatives, each marked PENDING |
| Behavioral fixtures | 31 cases across positive, semantic one-field-negative, missing-evidence, wrong-target, conflict, request-scope, unknown-status, and F02/F03 dependency behavior |
| Focused validation | 14 of 14 Rules-v1 tests passed after this bounded remediation |
| CI-equivalent repository discovery | 38 of 38 tests passed; default discovery listed every `rules_v1.test_*` module |

The runner evaluates only the five F01/F06 Draft sub-rules. A confirmed failure blocks first; otherwise an explicit unresolved state blocks PASS; PASS requires a frozen pass condition; every unmatched value defaults to UNRESOLVED. It never returns a terminal scientific verdict.

## Design boundary

The Draft follows this sequence:

    Canonical CaseGraph fixture
      -> binding grammar
      -> single-target RuleInstance
      -> Resolution Policy
      -> direct evaluation, source lookup, or human/new-data stop
      -> rule-specific Evaluation Contract
      -> HumanDecisionGate

HumanDecisionGate is separate from scientific evaluation. It records architecture, source-grounding, and runtime-readiness dispositions after deterministic evaluation. It cannot alter a RuleResult, calculate an evidence-supported claim ceiling, or approve publication wording.

The four route names are fixed:

1. DIRECT_EVALUATION
2. SOURCE_LOOKUP
3. REGISTERED_OPERATOR
4. HUMAN_OR_NEW_DATA

`SOURCE_LOOKUP` is deliberately narrow but is not implemented in this Draft. It declares a future read-only lookup by exact Source Evidence Packet ID or locator; no lookup executor or `EvidenceLookupResult` exists yet. It cannot search the web, retrieve an undeclared paper, invoke RAG, or infer a missing fact. The Operator route is represented in the vocabulary only and is disabled.

## Human-facing family map

| Family | Runtime targets | Draft state | Architecture | Source grounding | Runtime readiness | Review question |
| --- | --- | --- | --- | --- | --- | --- |
| F01 Claim Contract and Ceiling | CASE | Complete Draft slice | REVISE | PENDING_DOMAIN_REVIEW | NOT_READY | Is the claim contract now separate from intake-declared wording scope and the future evidence-supported ceiling? |
| F02 System Construct and Condition | SOURCE, EDGE | Candidate map only | APPROVE | PENDING_DOMAIN_REVIEW | DEFER | Are construct declaration and cross-source condition compatibility the right split? |
| F03 Source Measurement Semantics | SOURCE | Candidate map only | APPROVE | PENDING_DOMAIN_REVIEW | DEFER | Does the proposed source-native measurement contract preserve estimand and support? |
| F04 Source Reliability and Uncertainty | SOURCE | Candidate map only | REVISE | PENDING_DOMAIN_REVIEW | DEFER | Is the generic umbrella sufficiently separate from method-specific control profiles? |
| F05 Representation Support and Forward Bridge | SOURCE | Candidate map only | REVISE | PENDING_DOMAIN_REVIEW | DEFER | Should support coverage and forward-bridge validity remain independent obligations? |
| F06 Cross-source Comparability and Evidence Role | SOURCE, EDGE | Complete Draft slice | REVISE | PENDING_DOMAIN_REVIEW | NOT_READY | Does the source-role / comparability / independence split remain valid once F02/F03 are explicit prerequisites? |
| F07 Identifiability and Next Discriminating Action | CASE | Candidate map only | DEFER | PENDING_DOMAIN_REVIEW | DEFER | Does the candidate contract preserve non-identifiability as a valid outcome? |

## Runtime sub-rule map

Every runtime entry has exactly one target. A human-facing family may have several entries because source facts and edge relations are different questions.

| Runtime sub-rule | Family | Target | Status | Evidence packet |
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

## Source grounding

The Source Evidence Packets are review derivatives. Each packet retains a paper identifier and locator, a short review-derived passage, one atomic paper statement, the reusable use proposed for the Rule, a forbidden generalization, and PENDING human-review status.

The runtime registry stores packet IDs only. It does not copy source passages into bindings or turn review derivatives into a second scientific authority.

| Packet | Atomic statement used in this Draft | Explicit limit |
| --- | --- | --- |
| SEP-F01-CLAIM-CONTRACT | Claim level and intended use determine which evidence comparison is meaningful. | A declared question does not validate a source or a conclusion. |
| SEP-F01-REQUESTED-WORDING-SCOPE | Different claim levels need different supporting evidence. | An intake scope check does not calculate an evidence-supported ceiling. |
| SEP-F06-SOURCE-ROLE | Evidence role is distinct from independent validation. | A validation label alone does not establish independence. |
| SEP-F06-COMPARABILITY | A relation needs an explicit bridge; non-comparability is valid. | The runner does not force numeric equivalence. |
| SEP-F06-INDEPENDENCE | Agreement alone does not establish independent validation. | Same-data or shared-error agreement cannot receive a held-out label. |

## Binding and path contract

The implemented predicate grammar contains only EQ, IN, EXISTS, ALL, ANY, NOT, FOR_EACH_SOURCE, and FOR_EACH_EDGE.

Every required path is classified as one of:

    CURRENT_CASEGRAPH_FIELD
    DERIVED_FIELD
    VNEXT_CASEGRAPH_FIELD
    POST_OPERATOR_FIELD
    POST_EVALUATION_FIELD

This prevents a binding from silently depending on an undefined field. The Draft fixture can use proposed vNext fields, but the registry identifies them as such instead of presenting them as active v0.3 data.

F01R02 now checks `case.claim_contract.declared_request_scope`. It answers whether the request fits the intake contract. The future `evaluation.evidence_supported_claim_ceiling` is a post-evaluation Stage-2 field and is not computed here.

F06R02 and F06R03 require three post-evaluation prerequisites before they can PASS: F02 edge-condition compatibility and F03 native-measurement results for the left and right sources. F02 and F03 remain candidate-map-only, so a real CaseGraph has no route to manufacture those results in this PR.

The positive fixture contains synthetic prerequisite `PASS` values only to test this dependency wiring. Removing or downgrading any prerequisite produces UNRESOLVED. Those fixture values are not F02/F03 evaluations and do not establish a cross-source scientific conclusion.

## Behavioral evidence

Focused command:

    PYTHONPATH=src python3 -m unittest discover -s tests/rules_v1 -p 'test_*.py' -v

Result: 14 of 14 passed.

CI-equivalent command:

    PYTHONPATH=src python3 -m unittest discover -s tests -v

Result: 38 of 38 passed. The output listed all 14 Rules-v1 tests under `rules_v1.test_*`, so the existing GitHub workflow now covers the Draft package through ordinary unittest discovery.

The fixture matrix tests all five complete sub-rules with a positive match, a one-field semantic applicability negative that does not match, a missing-evidence case that becomes UNRESOLVED, a wrong-target case that does not fire, and a confirmed conflict that becomes FAIL. It also verifies that `UNKNOWN`, `UNRESOLVED`, and unknown vocabulary never become PASS; they remain UNRESOLVED. F01's request-scope conflict asks for `MECHANISM` outside the intake scope and returns `REQUEST_SCOPE_CONFLICT`, not a scientific cannot-support verdict.

The positive fixture produces six RuleResults: two CASE results, two SOURCE-role results, and two EDGE results. All six are PASS for the fixture only. Their scientific verdict field remains NOT_EMITTED_IN_PR1. The two EDGE PASS results depend on synthetic F02/F03 prerequisite stand-ins and carry no scientific meaning.

## What remains outside this PR

- The active v0.3 selector and runtime remain unchanged.
- No Rule is scientifically frozen or approved.
- No HSP90 obligation is created or routed.
- No Operator is selected, promoted, or executed.
- No Live Profiler or Planner Agent is added.
- No RVC, ADK, fourth protein, held-out case, or scientific verdict is introduced.

## Required human review

The revised Draft stops here. The next reviewers should assess:

1. **Architecture:** whether the seven family boundaries, F01 request-scope split, F06 F02/F03 dependency interface, and candidate-family priorities are the right design.
2. **Source grounding:** whether each F01/F06 locator and primary passage entails its atomic statement and proposed reusable use. The current packet remains a review derivative, not source approval.
3. **Runtime readiness:** whether a later Draft may implement F02/F03. No family is ready for active runtime or scientific decision output.

Current gates: `PENDING_HUMAN_ARCHITECTURE_REVIEW` and `PENDING_DOMAIN_REVIEW`.
