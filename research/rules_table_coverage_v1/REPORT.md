# Rules Table Coverage Challenge v1

**Development status:** `RULES_TABLE_PARTIALLY_COVERED_WITH_RECURRING_GAPS`

This report concerns the frozen exposed-development corpus only. It compares source-first review obligations with the post-merge Rules baseline at `86fc842f36002e57bcd71e6cb3fd90f9fed98d4b`. It does not alter canonical Rules, bindings, contracts, policies, source packets, H1, or scientific dispositions.

## Scope and reproducibility

- **Corpus:** 20 frozen challenge units from 15 frozen source identities.
- **Pass A:** source-first obligation extraction used only the scientific question, authorized primary-PDF passages, exact source identity, and a neutral review template. It was frozen before the Rules baseline was loaded. Its hash is recorded in [`manifest.json`](manifest.json).
- **Pass B:** each frozen mandatory obligation was compared with the seven families and twelve runtime Rules from the post-merge baseline. Row-level findings are in [`rule_coverage_results.jsonl`](rule_coverage_results.jsonl) and [`coverage_matrix.csv`](coverage_matrix.csv).
- **Source boundary:** the artifacts contain citations, frozen hashes, and exact primary-PDF locator codes. They do not include full-text PDFs or Markdown derivatives.

## Observed evidence

### Corpus and obligation counts

| Measure | Count |
| --- | ---: |
| Challenge units | 20 |
| Source identities | 15 |
| Source-first mandatory obligations | 40 |
| Deferred repair issues requiring layer decision | 1 |
| Canonical Rule mutations | 0 |

### Coverage labels

Each mandatory obligation has exactly one coverage label.

| Coverage label | Count |
| --- | ---: |
| `COVERED_EXACT` | 14 |
| `COVERED_PARTIAL` | 23 |
| `UNCOVERED_OBLIGATION` | 0 |
| `OVERTRIGGERED_RULE` | 0 |
| `WRONG_TARGET_SCOPE` | 0 |
| `WRONG_DEPENDENCY` | 0 |
| `WRONG_RESOLUTION_ROUTE` | 0 |
| `CLAIM_CEILING_TOO_HIGH` | 0 |
| `CLAIM_CEILING_TOO_LOW` | 0 |
| `HUMAN_JUDGMENT_ONLY` | 2 |
| `SOURCE_SPECIFIC_ONLY` | 1 |
| `DATA_INSUFFICIENT` | 0 |

`OVERTRIGGERED_RULE` is zero as an obligation-level label. Separately, the broad SOURCE predicates for F02R01 and F03R01 generated eight declaration obligations across four challenge units and three source identities. The recurring finding is recorded as deferred issue `CR-001` in [`candidate_repairs.json`](candidate_repairs.json).

### Taxonomic representation and executable coverage

The two measures answer different questions and must remain separate.

| Measure | Result | Interpretation |
| --- | --- | --- |
| Taxonomic representation | 40 / 40 | Every curated obligation can be placed in a current family. |
| Exact executable contract coverage | 14 / 40 | A Complete Draft Rule directly matches the obligation's target, evidence path, and local claim ceiling. |
| Partial coverage | 23 / 40 | A family or Rule is adjacent, but the contract, evidence path, or evaluation capability remains incomplete. |
| Candidate Map Only | 19 / 40 | The scientific need is represented but deferred. It is not an executable Rule success. |

### Coverage by family

The table counts source-first obligations mapped to each family. Candidate Map Only entries remain deferred and cannot produce an executable local PASS.

| Family | Mapped obligations | Row-level outcome |
| --- | ---: | --- |
| F01, claim contract and ceiling | 3 | 2 exact; 1 partial |
| F02, system, construct, and condition | 5 | 4 exact; 1 partial |
| F03, source measurement semantics | 7 | 3 exact; 2 partial; 2 human-only |
| F04, source reliability and uncertainty | 6 | 6 partial; Candidate Map Only |
| F05, representation, support, and forward bridge | 9 | 9 partial; Candidate Map Only |
| F06, cross-source comparability and evidence role | 6 | 5 exact; 1 partial |
| F07, identifiability and next action | 4 | 3 partial; 1 source-specific; Candidate Map Only |

No mandatory obligation was labelled `WRONG_TARGET_SCOPE`. The F04, F05, and F07 mappings identify recurring scientific needs, but their 19 Candidate Map Only records do not count as executable Rule coverage.

### Repeated SOURCE-applicability overtrigger: CR-001

The F02R01 and F03R01 bindings currently apply to every SOURCE with a `source_id`. This predicate also generates sample-declaration and source-native-measurement obligations for sources that do not present one admitted empirical evidence object.

- Case 001 is a simulation sampling guide (`PDFMD-018`, `GRO-P01-ABSTRACT`; `GRO-P01-SCOPE`).
- Cases 002 and 016 are a conceptual review of experiments, models, and observable calculations (`PDFMD-017`, `THO-P01-ABSTRACT`; `THO-P01-INTRO`).
- Case 019 is a maximum-entropy methods paper (`PDFMD-027`, `PIT-P01-ABSTRACT`; `PIT-P01-INTRO`).

The recurrence establishes an overtrigger investigation across three source identities. It does not establish the correct repair layer. `CR-001` is therefore `DEFER` rather than a selected binding repair.

The pending question is whether source purpose belongs in CaseGraph admission or source typing, or whether a later Binding can safely reuse the existing `source.case_evidence_scope == CLAIM_EVIDENCE` boundary used by F06R01. A later proposal must reject a Binding-only guard if it is circular or suppresses an empirical object embedded in a review or methods paper.

### Human source-science questions

- **Case 001:** Does the general guide provide an empirical evidence object that should receive F02/F03 obligations, or should it remain a method/reference source?
- **Case 008:** Should the integrative NMR, SAXS, SANS, and MD publication be admitted as one source object or modality-level source objects linked to an integrated representation?
- **Case 020:** Does F03 source-local measurement semantics require F02 source context as a prerequisite, or only later EDGE comparability and CASE interpretation?

Case 020 is `HUMAN_JUDGMENT_ONLY`, not `WRONG_DEPENDENCY`. F03R01 declares source-native semantics and has no F02 prerequisite in its local contract. Relevant F06 EDGE comparability contracts separately require F02R02 and endpoint F03R01 evidence. One source does not establish a new generic dependency.

### Remaining source-specific issue

Case 019 raises maximum-entropy bias and distribution non-uniqueness beyond the present candidate identifiability map. It remains `SOURCE_SPECIFIC_ONLY` and method-profile-specific in this corpus. It is not a basis for a new family or runtime Rule.

## Inference

The current taxonomy can place all 40 curated obligations in a family. The current executable scientific contracts are incomplete: 14 obligations are exact matches, 23 are partial, and 19 of those mappings remain Candidate Map Only.

The evidence supports `RULES_TABLE_PARTIALLY_COVERED_WITH_RECURRING_GAPS` for this exposed development set. It identifies one recurring SOURCE-applicability overtrigger and two human source-science questions. It does not establish a canonical repair.

This result does not scientifically validate the Rules Table, establish complete family coverage, approve H1, demonstrate transfer or held-out success, establish Agent value, establish general Operator utility, or convert a local Rule PASS into a case-level support conclusion.

## Design proposals

### Deferred repair issue only

`CR-001` remains a deferred repair issue. Before any vNext proposal, named source-science review must decide who owns source purpose. The choice is between admission or typing, and a later narrow applicability guard based on the existing claim-evidence boundary. This PR does not choose a layer, add an ontology, or edit a canonical binding.

Any later repair must preserve empirical-source applicability, retain existing local claim ceilings, and leave F06, X-EISD, and HSP90 behavior unchanged unless independent evidence justifies a separate change. The future behavior checks are recorded in [`candidate_repairs.json`](candidate_repairs.json).

### Smallest next scientific decision

Obtain source-science review for Cases 001, 008, and 020 using their listed primary-PDF locators. That review should decide whether `CR-001` warrants one bounded Rules vNext proposal. No Rule implementation is authorized by this PR.

## Allowed claim and forbidden upgrades

**Allowed claim:** The current Rules Table has been systematically compared with source-first scientific review obligations from 20 exposed-development cases. The comparison identifies obligations that are exactly covered, partially covered, deferred in Candidate Maps, overtriggered at the SOURCE-applicability layer, or dependent on human scientific judgment.

**Forbidden upgrades:** Do not claim that the Rules Table is scientifically validated, that the seven families are complete, that H1 passed, that this corpus demonstrates transfer, that an Agent benefits from the Rules, that an Operator has general scientific utility, or that a local Rule PASS is a scientific case-level SUPPORT decision.
