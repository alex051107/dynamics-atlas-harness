# Dynamics Atlas: findings and decisions for the next stage

*Research-group brief · 10 September 2026*

**We now have useful, bounded analyses of real protein data. What we have not established is that a Rules Table should organize the whole analysis, or that adding more rules will make the Agent more reliable.** This brief separates those two questions so that the next step can be chosen for its scientific value.

Read this page first. The [claim-by-claim results](docs/RESULTS.md) supply numbers, original-paper links and the limits of each comparison. The [existing English results slides](../review/four-layer-20260910/outputs/COLLABORATOR_REPORT_EN.pptx) are an optional visual companion, not an additional reading requirement. The slides retain the earlier result presentation; the framing and open decisions below are the current discussion brief.

## 1. The problem we set out to solve

A researcher may have simulation trajectories, nuclear magnetic resonance (NMR) measurements, scattering and fluorescence data for the same protein. These sources do not necessarily measure the same quantity or describe the same conditions. We want to identify what they can support together, what remains unresolved, and which further analysis would actually help.

For example, a simulation can move toward an open reference without closely matching that reference, and neither result alone establishes an equilibrium population or transition rate. A useful answer should preserve the supported structural observation rather than either overstate it or discard it because the stronger questions remain open.

The intended workflow is **a concrete scientific question → source and measurement interpretation → an appropriate established analysis → an evidence-linked answer**. Rules are a proposed aid to this workflow, not its scientific endpoint.

## 2. Where the work stands

| Stage | What was done | What it established |
|---|---|---|
| Literature to candidate checks | Recorded 33 candidate rules from 11 papers, with source-specific assumptions and limits | A reviewable knowledge resource, not 33 validated universal laws |
| Selected-rule prototype | Converted case metadata into review obligations and rendered the selected text for an Agent | The path ran, but HSP90 also exposed inappropriate transfer of method-specific wording |
| Scientific case analyses | Compared HSP90 direction with native NOE references, corrected DHFR coordinates, analysed ADK domain distances, and performed a nanodisc cross-observable comparison | Concrete results below, with substantial developer preparation and checking |
| Component pilot — complete | Tested warning-card availability, one round of feedback, method guidance and explicit subquestions | Mixed effects; no stable benefit from the current selector or checker |
| Next stage — not decided here | Choose a scientific milestone and the specific assistance worth retaining | This requires a research decision, not another automatic rollout |

[History and source trail](docs/RULES.md#how-the-rules-entered-the-analysis) · [Completed pilot](../review/four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md#3-what-was-held-constant-what-changed-and-how-answers-were-scored)

## 3. What the scientific work actually says

**HSP90:** of 20 closed-start trajectories, 10 displayed sustained open-direction segments under the specified definition. At a 1 Å project tolerance, nine of those ten were classified as moving relatively toward open while still predominantly departing from both native NOE reference sets. This distinguishes direction from reference agreement; it neither reproduces nor refutes the paper's complete transition interpretation. [Author claim, result and scope](docs/RESULTS.md#hsp90-direction-is-not-the-same-as-reference-agreement)

**Nanodisc:** fitting only the scattering observations reduced their mean penalty from 10.0188 to 1.1707, while the two NOE mean penalties increased from 0.9334 to 0.9647 and from 3.8931 to 4.4695. These are within-channel comparisons under a fixed candidate pool and error model, not proof that the experiments are physically inconsistent. [Author claim, result and scope](docs/RESULTS.md#nanodisc-a-better-scattering-fit-did-not-improve-both-noe-readouts)

**DHFR and ADK:** coordinate handling changed what a distance meant. DHFR required a corrected local periodic representation; a blanket half-box rule then wrongly rejected legitimate ADK intramolecular geometry. Their corrected analyses describe local proximity and finite-window domain changes, not the source papers' complete kinetic mechanisms. These corrections were developer work, not discoveries by the original tested Agents. [DHFR](docs/RESULTS.md#dhfr-corrected-proximity-is-not-a-kinetic-mechanism) · [ADK](docs/RESULTS.md#adk-apo-domain-motion-does-not-reproduce-an-atp-triggered-experiment)

## 4. What the assistance tests did — and did not — establish

| Assistance tested | Observed result | What remains unresolved |
|---|---|---|
| A file warning about a defective input | All four card-condition runs listed the file; none read its contents | Whether actually delivering the warning would help; this was not a test of an Agent reading and rejecting it |
| A checker after the first answer | All nine warnings were numerical trace warnings; none targeted a core scientific error. None of 12 feedback runs reduced its initial core-error count | Whether a different, scientifically appropriate checker would help; the tested checker was not a general scientific judge |
| Guidance during analysis | Full rules performed better on the nanodisc task but worse on HSP90; short method cards did not meet the two-case comparison criterion | Content, applicability, retrieval, reading burden and case dependence were not independently separated |
| More explicit subquestions | Supported coverage increased in both cases; HSP90 core errors across four runs increased from one to two | More complete delivery is not uniform accuracy improvement or autonomous question discovery |

[Individual scores](../review/four-layer-20260910/outputs/UNBLINDED_SCORES.csv) · [Warning access](../review/four-layer-20260910/outputs/E1B_CARD_ACCESS_AUDIT.json) · [Feedback analysis](../review/four-layer-20260910/outputs/E2_CHECKER_EFFECT_REVIEW_ZH.md)

There were 72 controlled final answers plus two ordinary ADK answers, and 24 saved feedback initial answers. Scores were sealed before condition labels were revealed, but the scorer also helped prepare the cases. Most cases were exposed development material; there were four runs per question and condition, not four independent proteins. These results do not estimate general scientific accuracy or savings in researcher time. [Evaluation scope](../review/four-layer-20260910/outputs/METHODS_AND_LIMITS_ZH.md)

## 5. Four decisions on which we need guidance

### A. Is the main problem rule content, applicability, or the role assigned to rules?

We have direct evidence of method-specific conditions reaching an inappropriate task, of an unread warning, and of a checker that did not target the relevant scientific errors. We do **not** have evidence that all rules are poor, or that better rules alone would fix the system.

**Decision requested:** should the next step repair one demonstrated applicability problem, or should we first work without automated rule selection until a scientific task establishes its need? Our proposal is to pause broad selector expansion while retaining the source-linked knowledge. This is an investment recommendation, not proof that a simpler system is universally superior.

### B. Where should guidance or enforcement enter the scientific work?

A physical check needs the intended observable, not just a generic data-type label. Method advice must match the operation being performed. A post-answer warning is useful only when its claim-to-evidence check is meaningful.

**Decision requested:** which requirements should be handled before analysis, which should remain optional method guidance, and which explicit contradictions are suitable for automatic feedback? Our proposal is a readable protocol with a few individually justified checks, not four mandatory software layers. [What each form means](docs/RULES.md)

### C. What level of scientific answer should define the next milestone?

The current work can establish selected structural differences or readout disagreements without identifying a unique ensemble or mechanism. That is narrower than several author-level claims, but it can still be useful.

**Decision requested:** is a reproducible cross-observable comparison with a clearly defined interpretive limit a sufficient next milestone, or is a particular state, population or mechanistic inference required? In particular, which current HSP90 or nanodisc distinction is scientifically worth resolving next? A narrower project result is not, by itself, evidence against the original paper.

### D. What work should the Agent actually remove from the researcher?

Developers currently prepare source correspondence, numerical inputs and some checks. The corrected science must not be credited to the Agent merely because it later reads the resulting tables.

**Decision requested:** should the next evaluation start from checked tables, or require the Agent to identify measurement and preparation issues from less curated sources? Choose one boundary, then measure supported answers, material errors, unnecessary omissions and preparation/correction time. We should not change the task, tools, guidance and checker together and attribute the result to Rules.

## 6. How the two recommended readings change the design question

[Li, Thomasen and Cossio — *Are We Capturing the Ensemble?*](https://rs-station.github.io/2026/08/31/are-we-capturing-the-ensemble.html) asks which differences between molecular distributions survive measurement and processing. [Bhakat's T4 lysozyme paper](https://doi.org/10.1021/acs.jcim.6c02044) provides a concrete reason to evaluate structural coverage, estimated populations and experimental predictions separately. Neither source establishes a Rules architecture. Our design inference is to organize the work around the scientific distinction and the evidence that can resolve it. [Papers and specific uses](docs/SOURCES.md)

**Proposed next step, for discussion:** select one scientifically useful distinction from the completed analyses, confirm the method and interpretation needed to address it, and use the simplest existing workflow that can deliver that answer. Any new comparison of assistance should change one specific intervention. This briefing does not start new calculations, Agent runs or an expansion to another system.

<details>
<summary>Optional: methods, reproduction and preserved evidence</summary>

[Methods](docs/METHODS.md) · [Analysed-table reproduction](docs/REPRODUCE.md) · [Input provenance](data/MANIFEST.json) · [Original papers](docs/SOURCES.md) · [Full pilot report and evidence links](../review/four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md)

The replay package reproduces selected HSP90, DHFR and ADK summaries from supplied analysed tables; it is not a raw-coordinate reconstruction or independent biological validation. The earlier downloadable ZIP and offline HTML remain archived reproduction snapshots, not updated copies of this decision brief.

This presentation uses the source snapshot `c025a74ed8235ddde463572158c73458753780b0`. Reorganizing the reading path did not alter inputs, original answers, sealed scores or failed analyses. Superseded plans and raw execution detail stay outside the primary reading path, available through the historical evidence records.

</details>
