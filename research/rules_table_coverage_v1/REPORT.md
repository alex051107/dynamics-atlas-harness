# Rules Table Coverage Challenge v1

**Development status:** `RULES_TABLE_COVERAGE_STABLE_WITH_BOUNDED_REPAIRS_PROPOSED`

This report covers the frozen exposed-development corpus only. It compares source-first scientific review obligations with the post-merge Rules baseline at `86fc842f36002e57bcd71e6cb3fd90f9fed98d4b`. It does not change canonical Rules, bindings, contracts, policies, source packets, H1, or scientific dispositions.

## Scope and reproducibility

- **Corpus:** 20 frozen challenge units from 15 frozen source identities.
- **Pass A:** source-first obligation extraction used only the scientific question, authorized primary-PDF passages, exact source identity, and a neutral review template. It was frozen before the Rules baseline was loaded; the file hash is recorded in [`manifest.json`](manifest.json).
- **Pass B:** each frozen mandatory obligation was mapped against the seven families and twelve runtime Rules from the post-merge baseline. The row-level mapping is in [`rule_coverage_results.jsonl`](rule_coverage_results.jsonl) and [`coverage_matrix.csv`](coverage_matrix.csv).
- **Source boundary:** the artifacts contain citation metadata, frozen hashes, and exact primary-PDF locator codes. They do not include full-text PDFs or Markdown derivatives.

## Observed evidence

### Corpus and obligation counts

| Measure | Count |
| --- | ---: |
| Challenge units | 20 |
| Source identities | 15 |
| Source-first mandatory obligations | 40 |
| Candidate repairs proposed | 1 |
| Canonical Rule mutations | 0 |

### Coverage labels

Each of the 40 mandatory obligations has exactly one coverage label.

| Coverage label | Count |
| --- | ---: |
| `COVERED_EXACT` | 14 |
| `COVERED_PARTIAL` | 23 |
| `UNCOVERED_OBLIGATION` | 0 |
| `OVERTRIGGERED_RULE` | 0 |
| `WRONG_TARGET_SCOPE` | 0 |
| `WRONG_DEPENDENCY` | 1 |
| `WRONG_RESOLUTION_ROUTE` | 0 |
| `CLAIM_CEILING_TOO_HIGH` | 0 |
| `CLAIM_CEILING_TOO_LOW` | 0 |
| `HUMAN_JUDGMENT_ONLY` | 1 |
| `SOURCE_SPECIFIC_ONLY` | 1 |
| `DATA_INSUFFICIENT` | 0 |

`OVERTRIGGERED_RULE` is zero as an obligation-level label. Separately, the current SOURCE applicability bindings produced four case-level overtrigger findings: two declaration Rules created eight unnecessary Rule-instance obligations across four challenge units and three source identities. Those findings are recorded in [`candidate_repairs.json`](candidate_repairs.json) as `CR-001`.

### Coverage by family

The table counts source-first obligations mapped to each family. A mapped Candidate Map Only entry represents a deferred scientific need; it is not an executable Rule success.

| Family | Mapped obligations | Row-level outcome |
| --- | ---: | --- |
| F01 — claim contract and ceiling | 3 | 2 exact; 1 partial |
| F02 — system, construct, and condition | 5 | 4 exact; 1 partial |
| F03 — source measurement semantics | 7 | 3 exact; 2 partial; 1 human-only; 1 wrong dependency |
| F04 — source reliability and uncertainty | 6 | 6 partial; Candidate Map Only |
| F05 — representation, support, and forward bridge | 9 | 9 partial; Candidate Map Only |
| F06 — cross-source comparability and evidence role | 6 | 5 exact; 1 partial |
| F07 — identifiability and next action | 4 | 3 partial; 1 source-specific; Candidate Map Only |

F02 source declarations, F03 source-native measurement semantics, and F06 source/edge relationships matched recurring empirical review questions with appropriate source or edge ownership in this exposed set. No mandatory obligation was labelled `WRONG_TARGET_SCOPE`.

The 19 F04/F05/F07 Candidate Map Only mappings were retained as deferred coverage. None was counted as an executable local PASS, and each remains bounded to a human or new-data route.

### Repeated overtrigger finding: CR-001

The current `F02R01_SOURCE_SAMPLE_SYSTEM_COMPOSITION_DECLARATION` and `F03R01_SOURCE_NATIVE_MEASUREMENT` bindings apply whenever a SOURCE target has a `source_id`. That predicate also creates sample-declaration and source-native-measurement obligations for sources that are not one admitted empirical evidence object:

- Case 001: a simulation sampling guide (`PDFMD-018`, `GRO-P01-ABSTRACT`; `GRO-P01-SCOPE`).
- Cases 002 and 016: a conceptual review of experiments, models, and observable calculations (`PDFMD-017`, `THO-P01-ABSTRACT`; `THO-P01-INTRO`).
- Case 019: a maximum-entropy methods paper (`PDFMD-027`, `PIT-P01-ABSTRACT`; `PIT-P01-INTRO`).

This is a recurring applicability problem, not a paper-specific annotation issue: the same structural predicate overtriggers in three distinct source identities. `CR-001` therefore proposes, but does not implement, a future narrowing of these bindings to an admitted empirical or claim-evidence source object with a declared measurement/source purpose. Its rejection condition and regression cases are recorded in [`candidate_repairs.json`](candidate_repairs.json).

### Remaining findings that do not yet justify a generic repair

- **Source-object granularity:** Case 008 raises whether an integrative paper should be represented as one publication-level source object or separate modality-level objects. This is `HUMAN_JUDGMENT_ONLY`, because the answer is source-science design rather than a mechanically inferred generic split.
- **F02-to-F03 prerequisite:** Case 020 exposes one instance in which construct/condition context may be needed before interpreting source measurement semantics. It is labelled `WRONG_DEPENDENCY`, but one direct source instance does not meet the two-independent-paper threshold for an ordinary generic repair.
- **Maximum-entropy interpretation:** Case 019 exposes bias and non-uniqueness questions beyond the present candidate identifiability map. It is `SOURCE_SPECIFIC_ONLY` / method-profile-specific in this corpus, not a basis for a new family or runtime Rule.
- **Claim ceilings:** no row was labelled `CLAIM_CEILING_TOO_HIGH` or `CLAIM_CEILING_TOO_LOW`. An F01 intake scope record remains an intake boundary, not an evidence-supported scientific conclusion.

## Inference

On this exposed development set, the Rules Table represents every mandatory obligation at least partially and gives exact coverage to 14 of 40 obligations. This is not a completeness result: 23 mappings remain partial, largely because F04, F05, and F07 are intentionally Candidate Map Only rather than executable Rules.

The evidence supports a bounded stability finding: the current table has one recurring, source-type applicability overtrigger suitable for a separately reviewed candidate repair, while the remaining gaps are either below the recurrence threshold or require human source-science judgment. The status therefore is `RULES_TABLE_COVERAGE_STABLE_WITH_BOUNDED_REPAIRS_PROPOSED` for this development corpus.

This result does not scientifically validate the Rules Table, establish that the seven families are complete, approve H1, demonstrate transfer or held-out success, establish Agent value, establish general Operator utility, or turn a local Rule PASS into a case-level support conclusion.

## Design proposals

### Candidate repair proposal only

`CR-001` has disposition `NARROW` and status `PROPOSED_NOT_IMPLEMENTED`. A later vNext proposal could narrow F02R01/F03R01 SOURCE applicability using an admitted empirical or claim-evidence object plus declared source purpose. It must retain applicability for the empirical regression cases listed in [`candidate_repairs.json`](candidate_repairs.json), must never broaden a claim ceiling, and must be rejected if the guard cannot be populated without circular inference.

No canonical Rule, applicability binding, evaluation contract, resolution policy, source packet, H1 record, or scientific disposition changed in this milestone.

### Exact human-review questions

1. Can a source-purpose/evidence-object guard be defined before Rule applicability without circularly deciding the scientific question it is intended to control?
2. For integrative publications, what source-object granularity should be admitted before F03 evaluates source-native measurement semantics?
3. Does the possible F02-to-F03 source-local dependency recur in a second independent empirical source, and if so, what evidence should the prerequisite require?

### Smallest next scientific decision

External review should decide whether `CR-001` is sufficiently well specified to become one separate, bounded Rules vNext proposal. The source-object-granularity and F02-to-F03-dependency questions should remain human-review questions until they have independent source evidence. No Rule implementation is part of this PR.

## Allowed claim and forbidden upgrades

**Allowed claim:** The current Rules Table has been systematically compared against source-first scientific review obligations from 20 exposed-development cases, revealing which obligations are exactly covered, partially covered, missing, overtriggered, assigned to the wrong target, or dependent on human scientific judgment.

**Forbidden upgrades:** Do not claim that the Rules Table is scientifically validated, that the seven families are complete, that H1 passed, that this corpus demonstrates transfer, that an Agent benefits from the Rules, that an Operator has general scientific utility, or that a local Rule PASS is a scientific case-level SUPPORT decision.
