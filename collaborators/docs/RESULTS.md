# Authors' claims and our findings

[Briefing](../README.md) · [Research stages](PROGRESS.md) · [Methods](METHODS.md) · [Sources](SOURCES.md)

**Author statements, our calculations and our interpretations are separate kinds of evidence.** Author statements below are paraphrases of the cited papers, not quotations or reference answers that an Agent must reproduce. Project numbers come from the deposited analyses and recorded checks linked below; reorganizing this page does not constitute a new scientific replication.

## The comparison at a glance

| Case | What the paper argues | What we analysed | Our bounded conclusion |
|---|---|---|---|
| HSP90 | NMR-guided modelling and MD support an interpretation involving a transiently populated closed state of the ATP-binding domain. | Persistent direction labels and deposited open/closed NOE-violation series. | Moving toward the open reference is not the same as satisfying its distance restraints or observing a complete physical transition. |
| DHFR | Experimental inhibition differences are discussed together with local inhibitor interactions, hydrogen-bond networks and molecular simulations. | Specified protein–ligand distances after correcting their periodic representation. | Selected proximity differences are consistent with part of the proposed local-interaction picture, but do not independently establish an inhibition mechanism. |
| ADK | Time-resolved scattering and structural modelling describe the response to ATP photorelease in the presence of AMP. | Project-defined domain-distance descriptors in two deposited apo trajectories. | The finite MD window comparisons do not reproduce or refute the ATP-triggered experimental intermediate. |
| Nanodisc, earlier development | MD, SAXS and NMR information can be integrated through ensemble refinement. | Cross-observable prediction and source-specific treatment of supplied predictions, bounds and weights. | Fitting one observable is not evidence of agreement with every other observable or of a unique ensemble. This case is not part of the portable three-system replay. |

Original sources and relevant locations: [Henot et al., Results/Fig. 4 and Methods](https://doi.org/10.1038/s41467-022-35399-8); [Çetin et al., Table 1, Figs. 3–4 and analysis methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC10428214/); [Orädd et al., Results/Fig. 4 and Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC8597995/); [Bengtsen et al., Table 2 and Methods](https://doi.org/10.7554/eLife.56518).

## HSP90: direction, reference agreement and transition are different claims

### What the author analysis supplies

Henot and colleagues combined solution NMR, restrained structural modelling and MD to study an otherwise sparsely populated closed state. The correspondence between the state detected by CPMG relaxation dispersion and a particular closed structure remains a model interpretation; it is not a direct identity measurement. The authors' trajectory groups are based on their native NOE and structural criteria, not our later persistence-count definition.

### What our analysis establishes

The deposited analysis comprises 40 trajectories, 20 closed-start and 20 open-start. Each contributes 1001 saved points from 20 to 1020 ns. At the five-saved-point threshold, 10 closed-start trajectories ever exhibit a sustained open direction: five have an open direction in their **first qualifying persistent segment**, and five acquire it after an earlier qualifying direction. This is not a statement that five simulations began physically open.

Counting an opposite persistent direction after the first qualifying direction gives 5, 4 and 1 closed-start candidates at thresholds of 5, 20 and 50 saved points; the open-start counts are zero. Changing the threshold can change the first qualifying direction itself. These are definition-dependent event counts, not estimates of transition rates.

The native series then asks a different question: how far are the predictions from the two reference sets of NOE upper-distance bounds? At the project tolerance of 1 Å, nine of the ten closed-start trajectories with open-direction points have at least half of those points outside both reference tolerances. One is partially consistent, and none meets the project's trajectory-level open-reference agreement criterion. Among the open-start controls, 18 of 20 meet the agreement criterion.

The result does not erase improvement within a trajectory. For example, ES15's mean open-reference violation decreases from 9.0741 Å in the first 100 points to 1.1154 Å in the last 100. The 1 Å classification and the size of this decrease describe different properties.

### What remains unresolved, and who did what

These are analyses of deposited, partly derived quantities. The absolute-series comparison was prepared by the developer after correcting an input-column interpretation; it was not discovered by the initial A/B Agent experiment. The first-round Agent answers and later native-data analysis remain separate records.

The 0.5, 1 and 2 Å tolerances are project operating definitions. At 2 Å, three of the ten candidates meet the agreement criterion; at 0.5 Å, none do. Neither choice establishes a uniquely calibrated physical state. We have not fully reproduced the paper's 7/about-9/4 structural grouping, equilibrium populations or complete transition pathways.

Evidence: [first-round report](../../review/hsp90_q01-round-20260910/HSP90_Q01_VERIFIED_REPORT_ZH.md); [native-NOE analysis, definitions, sensitivity and reading correction](../../review/hsp90_q01-round-20260910/v4_native_noe/outputs/report/DEEP_READER_ZH.md). The [portable replay](REPRODUCE.md) starts from supplied analysed tables, not raw coordinates.

## DHFR: corrected distances support proximity, not a unique inhibition mechanism

### What the paper argues

Çetin and colleagues relate inhibitor behaviour in WT and L28R DHFR to local interactions and dynamical barriers. Experimental affinity/inhibition results, atom-pair distances, hydrogen-bond geometry and broader interaction analyses are different evidence types. Our distance comparison addresses only part of that argument.

### What our analysis establishes

One deposited trajectory per condition covers WT/L28R with trimethoprim (TMP) or 4′-DTMP. The analysis uses frames 11–1000, 990 frames per condition. Direct distances from an inappropriate wrapped representation produced apparent separations above 70 Å in some frames. The developer corrected the periodic representation and cross-checked selected distances with VMD; the recorded maximum difference was 0.00001132 Å.

| Protein background | TMP: mean M20–O3P / Å | 4′-DTMP: mean M20–O3P / Å |
|---|---:|---:|
| WT | 8.687677 | 4.622056 |
| L28R | 10.435783 | 4.808910 |

The corrected distance is smaller with 4′-DTMP in both backgrounds for this specified atom pair. O3P is the author's atom label; it does not imply that TMP contains a phosphate group. Other atom pairs need their own comparisons: the result must not be generalized to every contact.

### What remains unresolved, and who did what

The two original plain-Agent runs did not identify the defective input representation. Their answers are preserved and are not retrospectively improved by the developer's correction. Later evaluations using the corrected table are separate runs.

One trajectory per condition does not provide between-trajectory uncertainty. A short distance alone is not a hydrogen-bond definition, a dissociation rate or proof that one interaction causes the inhibition difference. Our finding is a local proximity result that can be discussed alongside the author's experiments, not independent validation of the whole mechanism.

Evidence: [complete DHFR reader, sections 2–7](../../review/dhfr_q01-round-20260910/report/DEEP_READER_ZH.md), including the original failure, correction, physical cross-check and paper relationship. The portable replay reproduces table summaries; it does not repeat the periodic-coordinate preparation.

## ADK: the deposited apo trajectories do not test the ATP-triggered experiment

### What the paper argues

Orädd and colleagues used time-resolved X-ray solution scattering after ATP photorelease, in the presence of AMP, together with structural modelling to interpret the response. The reported experimental transient and structural intermediate cannot be inferred from arbitrary MD distance curves alone.

### What our analysis establishes

The two deposited apo trajectories start from open and closed structures. They contain 2253 and 1678 frames over 0–450.4 ns and 0–335.4 ns, respectively. Domain separation is the average Cα-pair distance between declared project regions, not a reproduction of every descriptor used in the paper. We compare each trajectory's first and last 10% of frames.

| Starting structure | NMP–CORE change / Å | LID–CORE change / Å |
|---|---:|---:|
| Open | +0.070721 | +2.290411 |
| Closed | +1.090895 | +1.176421 |

Positive changes mean greater separation for these descriptors. Neither endpoint-window comparison shows both distances decreasing. This does not exclude closure in a shorter interval, and the distance distributions overlap.

A generic half-box threshold initially rejected valid intramolecular distances. The corrected analysis uses a complete molecule rather than shortening every atom-pair distance to its nearest periodic image. Recorded GROMACS checks agreed at about 0.005 Å; a separate numerical implementation checked domain averages. These checks support the declared calculation, not the truth of a biological model.

### What remains unresolved, and who did what

The input preparation and physical cross-checks were developer work. The two subsequent plain-Agent answers correctly reported the four endpoint-window changes; one omitted part of the experimental-condition comparison. Those answer-level observations are distinct from the validity of the prepared data.

The MD structures are apo; the experimental ligand conditions, temperatures and timescales differ. Our descriptors therefore neither reproduce nor refute the ATP-triggered scattering intermediate. There is one trajectory per starting condition, not hundreds of independent molecular experiments.

Evidence: [ADK scientific reader](../../review/four-layer-20260910/outputs/ADK_SCIENCE_ZH.md); [answer–paper comparison](../../review/four-layer-20260910/outputs/ADK_PAPER_RELATIONSHIPS.md).

## The nanodisc case remains a cross-observable development example

Bengtsen and colleagues had already studied SAXS-only, NOE-only and joint ensemble refinement. Our earlier work reused published conformers, predictions and observations to investigate what changes when weights are fitted to one observable and another is evaluated afterward. It is a conditional method application, not a newly discovered biological problem.

The later Agent task also used supplied author predictions and NOE bounds. It required keeping SAXS and NOE definitions separate, distinguishing a bound from a point target, and not calling data used in fitting independent validation. Full selected rules performed well on that particular task; this positive result remains part of the pilot, alongside the poorer HSP90 performance.

Evidence: [original nanodisc paper, Table 2](https://doi.org/10.7554/eLife.56518); [completed pilot report, section 6](../../review/four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md#6-retrieved-method-cards-did-not-outperform-the-short-protocol-consistently). Nanodisc calculations and Agent experiments are **not** rerun by the three-system portable reproduction script.

## The distinction to retain

**A numerical check can confirm that a declared calculation was reproduced. A scientific claim additionally needs a suitable observable, sample, comparison and interpretation.** Developer-corrected analyses, author reports, Agent outputs and future proposals are kept separate so that a polished report does not overstate what the Agent or the data established.
