# Dynamics Atlas: scientific results, four-layer validation, and the next investment decision

**Research progress report · 10 September 2026 · English delivery edition**

**The Rules Table showed mixed, case-dependent results. This pilot did not establish a stable incremental benefit from the rule selector or the current conclusion checker. Explicit subquestions improved answer coverage in both tested cases.**

The practical decision is to keep scientific questions, a short analysis protocol, established numerical methods, and traceable reports at the centre of the project. Retain the source-linked rule library for review and reference. Pause expansion of the selector and generic conclusion-enforcement layer.

This report covers 74 completed Agent outputs, the underlying results for HSP90, DHFR and adenylate kinase (ADK), and the evidence behind each component decision. It distinguishes scientific calculations performed by the developer from analyses actually performed by the evaluated Agent.

## 1. The original question and how the project reached this point

Dynamics Atlas began with a practical scientific problem: how can a researcher or a tool-using Agent combine molecular simulations, nuclear magnetic resonance measurements and scattering data to give a useful answer that another analyst can check? The Rules Table was one proposed aid. Its 33 source-linked candidate rules recorded assumptions, method requirements and limits on conclusions.

The early work established a knowledge resource, but rule coverage did not establish scientific answer quality. Development on the Q05 nanodisc case made a real cross-observable calculation possible while exposing a second issue: the developer still selected much of the analysis workflow. The project report and strategic review of 8 September therefore returned the scientific question and analysis protocol to the centre of the design.

Subsequent work produced three concrete results. HSP90 combined a direction classification with native nuclear magnetic resonance distance restraints. DHFR exposed and corrected a coordinate-representation error before interpreting local ligand distances. ADK established valid distances in a complete molecular representation and compared domain motion descriptors. HSP90 directly addressed a cross-source interpretation problem; the DHFR and ADK results mainly describe differences within molecular dynamics data. Their contribution is narrower than validating an interpretation against independent experiments.

The present pilot asked which forms of assistance improve answers once an Agent already has prepared source information, data tables and mature tools. It tested admission information, one round of checker feedback, retrieved method guidance and explicit question decomposition. It did not test a fully autonomous scientist or automatic construction of a scientific workflow from an uncurated literature collection.

## 2. The scientific results that the software must explain

A molecular dynamics (MD) trajectory is a time-ordered simulation of atomic coordinates. An ensemble is a collection or distribution of molecular conformations. Observing a conformation in a trajectory establishes neither its equilibrium population nor its transition rate. Different experiments also observe different functions of the underlying structures. These distinctions determine what each result below can support.

### HSP90: movement toward an open direction is not agreement with an open reference

The deposited HSP90 analysis comprised 20 closed-start and 20 open-start trajectories. In the closed-start set, 10 trajectories exhibited the specified open-direction classification: five already did so at the beginning and five did so later. The remaining ten never did. Thus, the relevant decomposition is **10/20 = 5 initially open-direction + 5 later open-direction**, rather than ten newly observed opening events.

Nuclear Overhauser effect (NOE) measurements provide distance-sensitive restraints between specified atoms. The native deposited series used here reports positive violations of upper bounds. Its second column is the native violation measure; an older direction calculation used the third, derived pseudo-distance column. These columns must not be interpreted as the same physical observable.

At a 1 Å tolerance, nine of the ten closed-start trajectories with an open-direction classification were classified as relative-direction only, one as partially consistent, and none as consistent with the open reference under the frozen trajectory criterion. The open-start comparison set contained 18 consistent, one partially consistent and one relative-only trajectory. The threshold matters: at 0.5 Å, only seven open-start controls were classified as consistent; at 2 Å, three of the ten closed-start candidates were consistent, two partial and five relative-only.

The result refines the direction-based interpretation. Leaving the closed reference and approaching the open reference are separate questions. Neither a sign change nor a frame fraction establishes an equilibrium state population or a physical transition rate. The source paper and the project's native-series crosswalk support this distinction. [Henot et al., 2022](https://doi.org/10.1038/s41467-022-35399-8); see the preserved three-system reader and source map for trajectory-level records.

### DHFR: a reproducible local distance difference after correcting periodic representation

The DHFR comparison used wild type (WT) and L28R with trimethoprim (TMP) and 4′-DTMP, one trajectory per condition and 990 analysed frames per trajectory. Periodic simulation boxes can place parts of a physical neighbourhood in different coordinate images. Directly measuring an inappropriate wrapped representation produced apparent distances of roughly 60–90 Å. The two original Agent answers did not identify this input defect.

After correcting the local periodic ligand representation, the mean M20–O3P distance decreased from 8.688 to 4.622 Å in WT and from 10.436 to 4.809 Å in L28R when comparing TMP with 4′-DTMP. An independent VMD calculation agreed to approximately 0.00001 Å. The field label O3P is an atom identifier here; it must not be interpreted as evidence that TMP contains a phosphate group.

These calculations support a local proximity difference in the deposited trajectories. They do not by themselves establish hydrogen bonding, which also requires appropriate geometry, or a unique inhibition mechanism. The paper's inhibition measurements and structural interpretation provide context, but a single trajectory per condition does not estimate between-trajectory reproducibility. The corrected numerical result is a developer analysis; the original Agent evaluation on the defective table remains invalid for assessing scientific analysis quality on correct data. [Cetin et al., 2023, Table 1 and Figs. 3–4](https://pmc.ncbi.nlm.nih.gov/articles/PMC10428214/).

### ADK: valid large intramolecular distances, without shared closure in the endpoint windows

ADK contains a relatively stable CORE and mobile NMP and LID regions. The project measured average Cα distances between predefined regions in a complete molecular representation. A Cα atom is the backbone carbon used here to describe protein geometry. The project definitions were CORE residues 1–29, 68–115 and 168–214; NMP 30–67; and LID 118–160. These are project-defined descriptors, not a reproduction of the paper's full structural inference.

A protein can legitimately extend beyond half a periodic box length. Intramolecular distances were therefore measured directly after reconstructing a complete molecule, rather than shortened using the nearest periodic image. Chain continuity, atom mapping, units and time axes were checked. GROMACS cross-checks of the specified atom pairs over all frames agreed within approximately 0.005 Å, below the 0.01 Å criterion. An independent SciPy implementation reproduced the domain descriptors to within 10⁻¹⁰ Å.

| Starting structure | NMP–CORE: last window minus first / Å | LID–CORE: last window minus first / Å |
|---|---:|---:|
| Open | +0.070721 | +2.290411 |
| Closed | +1.090895 | +1.176421 |

Positive values indicate greater separation for these descriptors. The first and last windows each used 10% of frames. The open-start trajectory covered 0–450.4 ns, with windows spanning 0–44.8 and 405.6–450.4 ns. The closed-start trajectory covered 0–335.4 ns, with windows spanning 0–33.2 and 302.2–335.4 ns. The absolute window durations therefore differed.

Neither trajectory showed joint closure of both regions in this comparison, and the distance distributions overlapped. The deposited simulations were apo, meaning no ATP or AMP was present in the deposited structures. The paper instead studied the response to photoreleased ATP in the presence of AMP using time-resolved X-ray solution scattering. The simulation and experiment also differed in temperature and timescale. These MD descriptors do not test the paper's ATP-triggered intermediate or reproduce its scattering fit. [Orädd et al., *Tracking the ATP-binding response in adenylate kinase in real time*](https://doi.org/10.1126/sciadv.abi5514); [deposited data, Zenodo 5583119](https://zenodo.org/records/5583119).

## 3. What was held constant, what changed, and how answers were scored

The completed campaign comprised 72 controlled outputs and two additional plain-Agent ADK outputs. All conditions used Luna with medium reasoning, the same frozen container and tool environment, and the same per-run limits. Each experimental question–condition pair had four fresh runs in a frozen randomized order. Ordinary controls already received prepared data. Rules, card availability, feedback or question wording were the experimental differences.

The five frozen core units for each question were scored as correct, erroneous or missing. Core errors, overclaims and omissions were reported separately. A missing part of a bundled unit counted as an omission even when the rest of that unit was correct. These scores measure coverage of predefined scientific content; they are not a general scientific accuracy percentage.

All final outputs were scored with condition labels removed. The scores were sealed before revealing the condition mapping. Initial and final submissions in the feedback experiment were also scored for revision analysis. Answers that reached the token limit were evaluated on their actual content, with completion status retained separately. No score was changed after unblinding.

The scorer also helped curate the cases. Label masking therefore does not constitute independent domain-expert review, and content could sometimes reveal the condition. HSP90, DHFR and Q05 were exposed development materials; ADK represented one new source group. Four runs per condition and one new source group support a bounded investment decision, not a population-level estimate of effectiveness. Exact outputs and scores remain available in [the unblinded score table](UNBLINDED_SCORES.csv) and [the evidence ledger](WORK_EVIDENCE_LEDGER.json).

## 4. Admission information did not reach the Agent's analysis

The deterministic admission test detected all six planted defects and reported no false alarms on three clean packages. This demonstrated consistency checking against trusted metadata and reference values. It did not demonstrate independent discovery of physical defects from raw coordinates. The three clean packages were identical to their reference values, making zero false alarms a weak self-consistency control.

The checker compared labels, expected row counts, time ordering and alignment, and numerical matrices. It also read the status of an upstream physical check. Numerical discrepancies and label errors depended on trusted references; missing-row detection required an expected count. Time monotonicity could be checked within the table, while time alignment still required a reference. The names of seven reported checks did not correspond to seven fully implemented scientific validations.

Both the ordinary and admission-card conditions detected the defective DHFR table in **0/4** runs and appropriately downgraded the answer in **0/4** runs. Tool-access records showed that all four card-condition runs listed the card filename but never read its contents. The observed failure was therefore a failure of making a card available to deliver its information. It does not establish that the Agent read and disregarded the warning.

| Question | Condition | n | Correct units /5 | Core errors | Overclaims | Omissions /5 | Cost $ |
|---|---|---:|---:|---:|---:|---:|---:|
| DHFR defective table | Admission card | 4 | 2 | 2.5 | 2 | 0 | 0.06495 |
| DHFR defective table | Prepared data | 4 | 3 | 1 | 1 | 1 | 0.08190 |

The appropriate architectural response is to enforce physical admission during data preparation. A bad derived table should not depend on the Agent discovering a warning file. See [the card-access audit](E1B_CARD_ACCESS_AUDIT.json) and [the checker coverage audit](E1A_CHECK_COVERAGE_AUDIT.json).

## 5. One round of conclusion feedback did not meet the continuation criterion

Only ADK showed a lower group median of core errors without more omissions, below the frozen requirement of improvement in at least two of three questions.

| Question | Condition | n | Correct units /5 | Core errors | Overclaims | Omissions /5 | Cost $ |
|---|---|---:|---:|---:|---:|---:|---:|
| ADK domains | Prepared data | 4 | 4 | 0.5 | 0 | 1 | 0.04915 |
| ADK domains | One feedback round | 4 | 4 | 0 | 0 | 1 | 0.05112 |
| DHFR corrected table | Prepared data | 4 | 4 | 0 | 0 | 0.5 | 0.07312 |
| DHFR corrected table | One feedback round | 4 | 3 | 0.5 | 0 | 1.5 | 0.08047 |
| HSP90 native NOE | Prepared data | 4 | 3 | 0 | 0 | 1 | 0.06485 |
| HSP90 native NOE | One feedback round | 4 | 3.5 | 0.5 | 0 | 0.5 | 0.06709 |

All nine emitted warnings concerned numerical trace matching. None identified a substantive core scientific error in the reviewed claim. A number absent verbatim from a tool output can still be valid after a unit conversion or an arithmetic operation; a number present in a tool output can come from an incorrect calculation. The actual warnings illustrate the weakness of matching numbers without checking their derivation.

Across the 12 feedback runs, no final answer had fewer core errors than its initial answer. Three lost answerable content. One softened an earlier error but introduced another, leaving the error count unchanged. The ADK difference between groups already existed in their initial answers, so it cannot be attributed to checker-induced correction. Some degradation occurred after a zero-warning response; the relevant intervention is the full feedback-and-revision procedure, not false alarms alone.

The evidence-role branch had no applicable public-facts input in these three cases and was not tested. In a separate historical replay, the checker missed all seven targeted core numerical errors and produced one false alarm by reading the exponent in Å⁻¹ as an unmatched number. [Actual warning review](E2_FLAG_REVIEW.json); [initial–final comparison](E2_REVISION_COMPARISON.json).

## 6. Retrieved method cards did not outperform the short protocol consistently

The method-guidance comparison included a seven-point protocol, full selected rules, and scoped method cards. It yielded opposite patterns across the two questions.

| Question | Condition | n | Correct units /5 | Core errors | Overclaims | Omissions /5 | Cost $ |
|---|---|---:|---:|---:|---:|---:|---:|
| HSP90 native NOE | Seven-point protocol | 4 | 4.5 | 0 | 0 | 0.5 | 0.07958 |
| HSP90 native NOE | Selected full rules | 4 | 2 | 1.5 | 0 | 1 | 0.07713 |
| HSP90 native NOE | Method cards | 4 | 2.5 | 0.5 | 0 | 0.5 | 0.07765 |
| Q05 nanodisc | Seven-point protocol | 4 | 4.5 | 0.5 | 0 | 0 | 0.07105 |
| Q05 nanodisc | Selected full rules | 4 | 5 | 0 | 0 | 0 | 0.05261 |
| Q05 nanodisc | Method cards | 4 | 4.5 | 0.5 | 0 | 0 | 0.05776 |

For HSP90, the median number of correct core units was 4.5 with the protocol, 2 with full rules, and 2.5 with method cards. For Q05, the corresponding medians were 4.5, 5 and 4.5. All four Q05 full-rule answers covered all five units. This benefit must remain visible when interpreting the overall mixed result.

Method cards failed the frozen requirement of being non-inferior to both alternatives on both questions. The frozen inapplicable-term metric did not distinguish conditions: none affirmatively imposed R0, dye, accessible volume (AV) or RMP as a requirement. Additional concerns about BME terminology were analysed separately after the review, without adding them to the frozen primary metric.

The HSP90 retrieval illustrates why a method family is too broad an applicability criterion. Matching nuclear magnetic resonance returned a Bayesian/maximum-entropy reweighting card, although the current task compared deposited NOE violations and did not require new weight fitting. Q05 retrieved four cards, including guidance specific to other ensemble observables. A shared measurement family does not imply the same requested operation.

Q05 itself involves small-angle X-ray scattering (SAXS) and NOE. SAXS reports scattering intensity averaged over structures; NOE effective distances require the specified nonlinear averaging and upper-bound treatment. For the supplied weights, the analysis counted 47/292 backbone HN and 8/40 methyl upper-bound violations. A good scattering fit therefore did not establish agreement with all NOE restraints or a unique molecular distribution. These are the distinctions useful guidance should help the Agent preserve. See [the source-linked method-card analysis](METHOD_CARD_DESIGN_ANALYSIS_ZH.md) and [the exploratory sentence-level review](E3_EXPLORATORY_REVIEW_ZH.md); these detailed supporting records remain in Chinese.

## 7. Explicit subquestions improved coverage, with a residual accuracy cost

Supported-subquestion coverage increased from a median of 2/3 to 2.5/3 for HSP90 and from 2/3 to 3/3 for ADK. Both questions met the frozen coverage criterion without an increase in overclaims.

| Question | Condition | n | Correct units /5 | Core errors | Overclaims | Omissions /5 | Cost $ |
|---|---|---:|---:|---:|---:|---:|---:|
| HSP90 direction/reference | Original question | 4 | 2.5 | 0 | 0 | 2 | 0.06881 |
| HSP90 direction/reference | Explicit subquestions | 4 | 3 | 0 | 0 | 1.5 | 0.06479 |
| ADK domains | Original question | 4 | 4 | 0 | 0 | 1 | 0.04785 |
| ADK domains | Explicit subquestions | 4 | 5 | 0 | 0 | 0 | 0.04974 |

HSP90's total core errors nevertheless increased from one to two across four runs, even though the median remained zero. The benefit was more complete delivery, not uniformly greater accuracy. ADK's decomposed question elicited the distribution centres and overlap more completely.

The intervention explicitly requested additional subquestions. It was not a length-matched paraphrase and did not show improved autonomous question discovery. The measured gain supports asking separately about observable direction, magnitude and limits on interpretation.

## 8. Completed execution, cost and preservation of evidence

| Batch | Completed outputs | Settled cost / USD | Cap / USD |
|---|---:|---:|---:|
| Admission-card comparison | 8 | 0.14685032 | 0.20 |
| Plain-Agent ADK | 2 | 0.02328782 | 0.15 |
| One-feedback comparison | 24 | 0.38581429 | 0.55 |
| Method-guidance comparison | 24 | 0.41578250 | 0.55 |
| Question decomposition | 16 | 0.23118686 | 0.40 |
| **Total** | **74** | **1.20292179** | **1.85** |

All 74 outputs completed and charges were settled. Model execution took approximately 90 minutes; scoring and report preparation were separate work. Four reconciled historical batches comprised 16 outputs costing $0.28550861. That amount is not a total for the project's entire history. The two additional ADK outputs are counted only once in the current campaign.

Both plain-Agent ADK answers correctly reported the four endpoint-window changes, with scores of five and four correct core units. Neither contained a core error or overclaim; one omitted part of the experimental-condition comparison. Their results are documented in [the ADK answer–paper relationship table](ADK_PAPER_RELATIONSHIPS.md).

Original answers, initial submissions, tool outputs, frozen files and cost receipts were preserved. Review suggestions received after an experiment's first call were documented rather than applied retrospectively. Human correction time was not measured, so the proposed 25% efficiency benefit remains untested. Existing Claude reviews covered materials and design; a final independent domain review of these answers remains outstanding.

## 9. Decision and next scientific step

**Keep the short protocol and source-linked literature library; pause expansion of the rule selector and generic conclusion checker.** The present evidence does not justify their cost as the project's central architecture. The full-rule benefit on Q05 warrants retention as a case-specific observation, not a claim of stable generalization.

Continue scientific work through a concrete question, validated input preparation, established calculations and a report that links each claim to evidence. Use explicit subquestions when they clarify what the reader needs. Make physical admission part of data preparation, and organize method guidance by the operation being attempted and its prerequisites.

Any repaired checker or revised retrieval policy should be a separately versioned proposal tested on new questions with criteria fixed beforehand. The current outputs and scores should remain unchanged. Before a broader effectiveness claim, obtain independent domain review of the answer boundaries and use additional independent source groups. These are future validation needs, not work completed by this pilot.

## 10. Reading and verification guide

Start with [the one-page decision](RULES_TABLE_VERDICT_EN.md) and [the English meeting deck](COLLABORATOR_REPORT_EN.pptx). This report contains the scientific background and main results. The detailed Chinese source readers and audit records are retained for traceability, including [the three-system reader](THREE_SYSTEMS_SCIENCE_ZH.md), [the ADK reader](ADK_SCIENCE_ZH.md), and [methods and limitations](METHODS_AND_LIMITS_ZH.md).

For numerical verification, use [the score table](UNBLINDED_SCORES.csv), [the evidence ledger](WORK_EVIDENCE_LEDGER.json), [the claim–source map](claim_source_map.jsonl), and [the deviations record](DEVIATIONS.md). Original run records and frozen inputs are packaged with the review materials in [PR #27](https://github.com/alex051107/dynamics-atlas-harness/pull/27). The report and deck translate and consolidate completed results; they introduce no new experiment or post-unblinding score changes.
