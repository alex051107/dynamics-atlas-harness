# Dynamics Atlas: findings and decisions for the next stage

*Research-group brief · 10 September 2026*

**We have useful, bounded analyses of real protein data. We have not established that a Rules Table should organize the whole analysis, or that adding more rules will make the Agent more reliable.** The next decision is which scientific result to pursue and what assistance is worth retaining.

Start with this page. [Authors' claims and our findings](docs/RESULTS.md) provides the detailed comparisons; [the existing 12-slide deck (PDF)](../review/four-layer-20260910/outputs/COLLABORATOR_REPORT_EN.pdf) is a visual companion, with an [editable PowerPoint version](../review/four-layer-20260910/outputs/COLLABORATOR_REPORT_EN.pptx). No installation or code review is needed for this discussion.

## 1. The problem we set out to solve

A researcher may have simulation trajectories, nuclear magnetic resonance (NMR), scattering and fluorescence data for the same protein. These sources do not necessarily measure the same quantity or describe the same conditions. We want to identify what they can support together, what remains unresolved, and which further analysis would help.

The intended workflow is **a concrete scientific question → source and measurement interpretation → an appropriate established analysis → an evidence-linked answer**. Reliable quantities and cross-source comparison are the scientific goals. Reusable workflows serve them; AI assistance is a separate hypothesis that may fail without invalidating the scientific result.

## 2. Where the work stands

| Stage | Actual work and its result |
|---|---|
| Literature to candidate checks | 33 candidate rules from 11 papers recorded source assumptions and limits. This is a reviewable knowledge resource, not 33 validated universal laws. |
| Selected-rule prototype | Metadata led to review obligations and rendered guidance. HSP90 exposed transfer of method-specific requirements without an established need. |
| Scientific case analyses | HSP90 distinguished direction from native reference agreement; DHFR and ADK exposed different coordinate-representation requirements; nanodisc analysis compared scattering and NOE predictions. Developers performed substantial preparation and checking. |
| Component pilot — complete | Warning-card availability, one-round feedback, method guidance and explicit subquestions were tested. Results were scored and unblinded; effects were mixed. |
| Next stage — undecided | Select a scientific milestone and the specific assistance worth retaining. Another experiment is not an automatic next step. |

[Stage-by-stage evidence](docs/PROGRESS.md)

## 3. What our results mean relative to the papers

**HSP90.** The paper combines NMR, structural modelling and MD to support a transient closed ATP-lid interpretation. We tested a narrower relation: does moving toward open imply agreement with the native open reference? Ten of twenty closed-start trajectories displayed sustained open-direction segments under the chosen definition. At a 1 Å project tolerance, nine of those ten were predominantly outside both reference tolerances. This separates direction from reference agreement; it does not refute the paper's full argument. [Results and original paper](docs/RESULTS.md#hsp90-direction-reference-agreement-and-transition-are-different-claims)

**Nanodisc.** The authors had already studied integration of scattering and NMR using an ensemble. Our earlier SAXS-only analysis reduced the scattering penalty from 10.0188 to 1.1707, while the two NOE mean penalties increased from 0.9334 to 0.9647 and from 3.8931 to 4.4695. These are within-channel comparisons under a fixed candidate pool and error model, not proof that the experiments are physically inconsistent. The later Agent task on supplied author weights was a separate experiment. [Saved project result](https://github.com/alex051107/dynamics-atlas-harness/blob/316471a135a95032f8726999e807393f55f6ceb5/review/rules-agent-study-20260909/references/07_REPORT_ZH.md) · [Paper and scope](docs/RESULTS.md#the-nanodisc-case-remains-a-cross-observable-development-example)

**DHFR and ADK.** The original papers make broader kinetic or experimentally triggered structural arguments. Our work describes selected local distances and finite-window domain changes. DHFR needed corrected local periodic coordinates; a blanket half-box rule then wrongly rejected legitimate ADK intramolecular geometry. The corrections were developer work, not discoveries by the original tested Agents. [DHFR claim comparison](docs/RESULTS.md#dhfr-corrected-distances-support-proximity-not-a-unique-inhibition-mechanism) · [ADK claim comparison](docs/RESULTS.md#adk-the-deposited-apo-trajectories-do-not-test-the-atp-triggered-experiment)

## 4. What the assistance tests tell us

| Intervention | Observed result | Limit of the conclusion |
|---|---|---|
| An input-warning file | All four card runs listed it; none read it | We did not test what happens when the Agent actually reads the warning |
| A checker after the first answer | Nine numeric-trace warnings targeted no core scientific error; none of twelve feedback runs reduced its initial core-error count | This implementation was not a general scientific judge; an untested evidence-role branch cannot be judged by these results |
| Guidance during analysis | Full rules did better on nanodisc but worse on HSP90; short cards missed the two-case criterion | Content, applicability, retrieval and reading burden were not independently separated |
| Explicit subquestions | Supported coverage improved in both cases; HSP90 core errors across four runs increased from one to two | More complete delivery is not uniform accuracy improvement or autonomous question discovery |

The pilot comprised 72 controlled final answers plus two ordinary ADK answers, with 24 saved feedback initial answers. Scores were sealed before revealing group labels, but the scorer also helped prepare the cases. Most materials had been used in development; four runs per condition are not four independent proteins. There is no general accuracy estimate or measured saving in researcher time. [Detailed results and limits](docs/RULES.md) · [Individual scores](../review/four-layer-20260910/outputs/UNBLINDED_SCORES.csv)

## 5. Four decisions on which we need guidance

### A. Is the problem rule content, applicability, or the role assigned to rules?

There is direct evidence of inapplicable conditions reaching a task, an unread warning, and a checker that did not address the relevant errors. There is no evidence that all scientific rules are poor, or that better rule wording alone would fix the system.

**Decision requested:** should we repair one demonstrated applicability problem, or first work without automated rule selection until a scientific task establishes its need? Our proposal is to pause broad selector expansion while retaining the source-linked knowledge. This is an investment recommendation, not proof that a simpler system is universally superior.

### B. At what stage should guidance become an automatic check?

Input checks require a defined physical quantity; method advice must match the operation; post-answer checks need a meaningful claim-to-evidence relation.

**Decision requested:** which requirements belong in data preparation, which should remain optional method guidance, and which explicit contradictions justify automatic feedback? Our proposal is a readable protocol with a few individually justified checks, not four mandatory software layers.

### C. What scientific answer should define the next milestone?

Current results identify selected structural differences and readout disagreements without identifying a unique ensemble or mechanism. They are narrower than several author-level claims but may still be useful.

**Decision requested:** is a reproducible cross-observable comparison with an explicit interpretive limit sufficient, or is a particular state, population or mechanism required? Which HSP90 or nanodisc distinction would be most useful to resolve next? A narrower project result is not evidence against a paper that used additional information.

### D. What work should the Agent remove from the researcher?

Developers currently prepare source correspondence, numerical inputs and some checks. An Agent reading the corrected tables does not inherit credit for that preparation.

**Decision requested:** should the next evaluation start from checked tables, or require measurement and preparation issues to be identified from less curated sources? Choose one boundary, then evaluate supported answers, material errors, unnecessary omissions and preparation/correction time. Do not change the task, tools, guidance and checker together and attribute the result to Rules.

## 6. Why the recommended readings matter

[Li, Thomasen and Cossio — Are We Capturing the Ensemble?](https://rs-station.github.io/2026/08/31/are-we-capturing-the-ensemble.html) asks which differences between molecular distributions survive measurement and processing. [Bhakat's T4 lysozyme paper](https://doi.org/10.1021/acs.jcim.6c02044), including its Supporting Information, shows why structural coverage, estimated populations and experimental predictions need separate evaluation. Neither source establishes a Rules architecture. Organizing our workflow around a scientific distinction is our design inference, not their experimental result. [All primary-paper links](docs/SOURCES.md)

**Proposed next step, for discussion:** choose one scientifically useful distinction from the completed analyses, confirm the method and interpretation needed to address it, and use the simplest existing workflow that can deliver that answer. Any later comparison of assistance should change one specific intervention. This page starts no new calculation, Agent run or expansion to another system.

<details>
<summary>Optional: slide-version notes, methods and preserved evidence</summary>

The existing slides are retained unchanged. Their HSP90 phrase “initially open-direction” means the first qualifying persistent segment, not necessarily simulation time zero. Proposed upstream admission in the deck is not an experimentally established general validator.

[Methods](docs/METHODS.md) · [Analysed-table reproduction](docs/REPRODUCE.md) · [Input provenance](data/MANIFEST.json) · [Full pilot report and evidence links](../review/four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md)

The replay regenerates selected summaries from supplied analysed tables; it does not rebuild raw coordinates or independently validate the biology. The earlier ZIP and offline HTML remain reproduction snapshots, not updated copies of this decision brief.

This reading edit incorporates the collaborator update at `6dd3df59c328902774b3183c86027b57424a4d60`. It does not alter inputs, original answers, scores or failed analyses. Old plans and execution details remain in the audit record, outside the primary reading path. Access to this private repository is required.

</details>
