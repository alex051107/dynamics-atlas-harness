# Rules Prototype v1 Review Packet

## Review request

This is a Draft, proposal-only Rules Prototype. It makes the Rules layer inspectable before any rule is activated, any Operator is routed, or any Agent is introduced.

For each family, choose one of these decisions:

- APPROVE
- REVISE
- REJECT
- DEFER

No decision in this packet changes the active v0.3 runtime. A scientific claim still requires source review and human scientific judgment.

## What this Draft delivers

| Item | Result |
| --- | --- |
| Human-facing families | 7 |
| Candidate runtime sub-rules | 12 |
| Fully executable Draft sub-rules | 5, covering F01 and F06 |
| Candidate-map-only sub-rules | 7, covering F02, F03, F04, F05, and F07 |
| Source Evidence Packets | 12 review derivatives, each marked PENDING |
| Behavioral fixtures | 26 cases across positive, one-field-negative, missing-evidence, wrong-target, conflict, and claim-ceiling behavior |
| Focused validation | 11 of 11 tests passed |

The runner evaluates only the five F01/F06 Draft sub-rules. It returns PASS, FAIL, UNRESOLVED, or NOT_APPLICABLE. It never returns a terminal scientific verdict.

## Design boundary

The Draft follows this sequence:

    Canonical CaseGraph fixture
      -> binding grammar
      -> single-target RuleInstance
      -> Resolution Policy
      -> direct evaluation, source lookup, or human/new-data stop
      -> rule-specific Evaluation Contract
      -> HumanDecisionGate

HumanDecisionGate is separate from scientific evaluation. A rule can set a wording ceiling or reject a requested label without asking whether a human approved publication. The human gate records the later review decision only.

The four route names are fixed:

1. DIRECT_EVALUATION
2. SOURCE_LOOKUP
3. REGISTERED_OPERATOR
4. HUMAN_OR_NEW_DATA

The lookup route is deliberately narrow. It can read a declared Source Evidence Packet by exact packet ID or locator. It cannot search the web, retrieve an undeclared paper, invoke RAG, or infer a missing fact. The Operator route is represented in the vocabulary only; it is disabled in this Draft.

## Human-facing family map

| Family | Runtime targets | Draft state | Review decision | Review question |
| --- | --- | --- | --- | --- |
| F01 Claim Contract and Ceiling | CASE | Complete Draft slice | PENDING | Is the claim contract separate enough from the wording ceiling? |
| F02 System Construct and Condition | SOURCE, EDGE | Candidate map only | PENDING | Are construct declaration and cross-source condition compatibility the right split? |
| F03 Source Measurement Semantics | SOURCE | Candidate map only | PENDING | Does the proposed source-native measurement contract preserve estimand and support? |
| F04 Source Reliability and Uncertainty | SOURCE | Candidate map only | PENDING | Is the generic umbrella sufficiently separate from method-specific control profiles? |
| F05 Representation Support and Forward Bridge | SOURCE | Candidate map only | PENDING | Should support coverage and forward-bridge validity remain independent obligations? |
| F06 Cross-source Comparability and Evidence Role | SOURCE, EDGE | Complete Draft slice | PENDING | Does the source-role / comparability / independence split prevent validation-role leakage? |
| F07 Identifiability and Next Discriminating Action | CASE | Candidate map only | PENDING | Does the candidate contract preserve non-identifiability as a valid outcome? |

## Runtime sub-rule map

Every runtime entry has exactly one target. A human-facing family may have several entries because source facts and edge relations are different questions.

| Runtime sub-rule | Family | Target | Status | Evidence packet |
| --- | --- | --- | --- | --- |
| F01R01 Case Claim Declaration | F01 | CASE | Complete Draft | SEP-F01-CLAIM-CONTRACT |
| F01R02 Case Claim Ceiling Alignment | F01 | CASE | Complete Draft | SEP-F01-CLAIM-CEILING |
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
| SEP-F01-CLAIM-CEILING | Different claim levels need different supporting evidence. | Lower-level compatibility does not establish kinetics, function, or mechanism. |
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

## Behavioral evidence

Focused command:

    PYTHONPATH=src python3 -m unittest discover -s tests/rules_v1 -p 'test_*.py' -v

Result: 11 of 11 passed.

The fixture matrix tests all five complete sub-rules with a positive match, a one-field applicability negative that does not match, a missing-evidence case that becomes UNRESOLVED, a wrong-target case that does not fire, and a conflict that becomes FAIL. A dedicated claim-ceiling case makes MECHANISM exceed the Draft ceiling and returns CANNOT_SUPPORT_REQUESTED_WORDING.

The positive fixture produces six RuleResults: two CASE results, two SOURCE-role results, and two EDGE results. All six are PASS for the fixture only. Their scientific verdict field remains NOT_EMITTED_IN_PR1.

## What remains outside this PR

- The active v0.3 selector and runtime remain unchanged.
- No Rule is scientifically frozen or approved.
- No HSP90 obligation is created or routed.
- No Operator is selected, promoted, or executed.
- No Live Profiler or Planner Agent is added.
- No RVC, ADK, fourth protein, held-out case, or scientific verdict is introduced.

## Required human review

The first Draft stops here. The reviewer should assess:

1. Whether the seven family boundaries reflect the intended protein-dynamics reasoning framework.
2. Whether each F01/F06 atomic statement supports its proposed reusable use and forbidden generalization.
3. Whether the F01 and F06 single-target splits are the right runtime units.
4. Whether the vNext path ownership is acceptable before any active runtime migration is proposed.
5. Whether the candidate-only families should be revised, deferred, or advanced in a later bounded batch.

Current gate: PENDING_HUMAN_SCIENTIFIC_REVIEW.
