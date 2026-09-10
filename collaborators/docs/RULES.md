# What the Rules Table means after the pilot

[Briefing](../README.md) · [Research stages](PROGRESS.md) · [Scientific results](RESULTS.md)

**Keep the scientific knowledge; do not assume a rule engine is necessary.** The pilot tested particular ways of helping an Agent. It did not show that a table can determine scientific truth, or that rules are useless in every task.

## Three different uses should not be confused

A **source-linked rule table** stores a scientific concern, its source, its applicable conditions and the limit of the inference. It remains useful to review. The archive contains [33 candidate rules from 11 papers](../../review/pro_briefing_20260910/rules/rule_registry.tsv); these counts describe the archive, not validated scientific coverage.

A **guidance prompt** gives some of that material to an Agent. The model must still judge whether a method applies, run appropriate calculations and interpret their results.

A **deterministic checker** is separately written code. It can test specific input relations or flag a restricted class of answer inconsistencies. Its authority is no wider than the implemented test and the evidence it receives. A matching rule ID, a valid JSON object or a successful calculation does not establish a scientifically adequate answer.

The completed pilot used the same basic Agent environment and prepared data, then changed one form of assistance in each comparison. It did not install four independently validated scientific layers into a complete harness.

## What each comparison actually tested

| Assistance | What changed for the Agent | Observed result | Interpretation boundary |
|---|---|---|---|
| **Input-warning card** | A file described a known problem in a defective DHFR input table. | All four card-condition runs listed its filename; none read the contents. Neither condition detected the defect in its four runs. | A file being available did not deliver its warning. This does not show that a read warning is useless. |
| **One round of answer feedback** | After an initial submission, a Python checker returned specific flags, followed by one revision opportunity. | All nine flags concerned numerical trace matching; none identified a core scientific error in the reviewed claim. None of the twelve feedback answers reduced its core-error count from initial to final. | This is a result for that checker and revision policy, not for every possible scientific validator. The evidence-role branch lacked applicable inputs in this test. |
| **Method guidance** | A seven-point protocol, full selected rules, or short method-family cards were supplied. | Full rules performed better on Q05 and worse on HSP90. Short cards did not meet the two-case continuation criterion. | Matching a method family, such as NMR, does not establish that a specific operation, such as reweighting, is needed. |
| **Explicit subquestions** | The question separately requested direction, magnitude/reference agreement and interpretation limits. | Supported coverage increased in both tested cases. HSP90 also had one additional core error across four runs. | More complete delivery is not uniform accuracy improvement. The split version added explicit requests; it was not an equal-length paraphrase. |

Evidence: [card access audit](../../review/four-layer-20260910/outputs/E1B_CARD_ACCESS_AUDIT.json), [feedback review](../../review/four-layer-20260910/outputs/E2_CHECKER_EFFECT_REVIEW_ZH.md), and [complete scored results](../../review/four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md#6-retrieved-method-cards-did-not-outperform-the-short-protocol-consistently).

### The method-guidance result should stay visible in both directions

| Task | Seven-point protocol | Full selected rules | Short method cards |
|---|---:|---:|---:|
| HSP90 native NOE | 4.5 | 2.0 | 2.5 |
| Q05 nanodisc | 4.5 | 5.0 | 4.5 |

Values are medians of correct predefined content units, out of five, across four outputs per condition. They are not percentages of scientific truth or independent biological replications. All four Q05 full-rule answers covered all five units. This positive case must not be erased by the lack of a stable overall benefit. [Individual scores](../../review/four-layer-20260910/outputs/UNBLINDED_SCORES.csv).

Supported-subquestion coverage changed from a median of **2/3 to 2.5/3** for HSP90 and **2/3 to 3/3** for ADK. HSP90's core-error total changed from **one to two across four runs**. These measure different outcomes and should be shown together. [Question-framing results](../../review/four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md#7-explicit-subquestions-improved-coverage-with-a-residual-accuracy-cost).

## What the checker was—and was not

The tested post-answer checker was not another scientific expert and did not compare the answer to the Rules Table as a reference solution. Its emitted warnings concerned whether declared numbers could be matched to tool outputs. A derived ratio may be correct without appearing verbatim in a tool response; a number copied from a tool response may still come from the wrong calculation. The warning itself said that an unmatched number was not a determination of falsehood.

The input checker likewise relied on prepared source metadata and reference values. It detected six planted defects and raised no alarms on three clean packages, but the clean numerical inputs matched their references. It did not independently discover and repair a periodic-coordinate defect from raw trajectories. Producing the trustworthy reference was separate developer work. [Admission-check scope](../../review/four-layer-20260910/outputs/E1A_CHECK_COVERAGE_AUDIT.json).

Scientific scores were assigned afterward with condition labels masked. The scorer also helped curate the cases. The checker that sends feedback and the person/agent assigning scientific evaluation labels are different roles; the former did not certify the latter's judgments.

## What remains worth keeping

The working protocol should continue to ask what is being compared, whether sources refer to compatible objects, how each observable is generated, what the statistical unit is, whether evidence was reused in fitting, and which interpretations remain unresolved. Those questions need source-specific methods, not a universal PASS/FAIL checklist.

Retain the literature archive and concise guidance where applicable. Implement a narrow check only when its inputs and failure meaning are clear and its false positives can be evaluated. Treat unsupported methods or missing facts as unverified—not automatically as scientific failure or success.

The current recommendation is to pause expansion of the generic selector and conclusion-enforcement layer. No claim is made that all computational checks fail, that a complete harness has been validated, or that data preparation accounts for a measured majority of project errors.
