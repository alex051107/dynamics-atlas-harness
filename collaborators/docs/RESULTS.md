# Author claims, project questions and supported results

[Back to the research brief](../README.md)

These are completed, selected-case analyses, not a full reproduction of each paper. Author claims below are paraphrases of the cited sources. Project results come from the saved analyses and audits linked in each section; this documentation edit did not rerun the science. A narrower result does not by itself refute a paper whose conclusion used additional evidence.

## HSP90: direction is not the same as reference agreement

**What the authors argued.** Henot and colleagues used solution NMR, mutagenesis and MD to characterize a transient closed ATP-lid conformation in the isolated human HSP90α N-terminal domain and interpret it as a metastable state. NMR relaxation supplied kinetic and thermodynamic information. The connection between the exchange-detected excited state and the closed structural model remains part of the authors' interpretation. [Original paper, Results, Fig. 4 and Discussion](https://www.nature.com/articles/s41467-022-35399-8)

**What we tested.** Do the saved trajectories move toward an open reference, and do the corresponding frames also agree with the deposited open-state NOE reference under a specified tolerance? NOE here refers to distance-sensitive NMR restraints; the native series records positive violations of upper-distance bounds. We did not estimate new kinetic rates from these derived labels.

**Observed result.** There are 40 trajectories, 20 per starting group, with 1,001 saved points per trajectory over 20–1020 ns. At a five-saved-point persistence threshold, 10/20 closed-start trajectories show a sustained open-direction segment: five have open as their **first qualifying segment**, and five reach it later. This is not a claim that the first five were open at simulation time zero. After the first qualifying direction, opposite-direction candidates number 5/20, 4/20 and 1/20 at thresholds of 5, 20 and 50 saved points; the open-start group has none. These thresholds alter the reference segment as well as the persistence requirement.

At a 1 Å project tolerance, among the ten closed-start candidates, nine are classified as relative-direction only, one as partially consistent, and none as consistent with the open reference. Of the twenty open-start controls, eighteen are consistent, one partial and one relative-only. The denominator is **10 selected candidates versus 20 controls**; neither number is a count of independent experiments. Classification changes with tolerance.

**What we can say.** Some closed-start trajectories move relatively toward open while remaining substantially outside the two native reference sets under the chosen criterion. Direction, absolute reference agreement and a complete physical state transition are different claims. The author's 7/about 9/4 trajectory grouping uses native NOE and structural judgments, not our 5/4/1 operational event definition. This is a method-specific comparison, not a reproduction or rejection of the full population or metastability argument.

**Who produced it.** The first Agent pilot computed and summarized some direction counts. The later native-NOE crosswalk and corrected interpretation were developer analyses; subsequent Agents received prepared evidence. They are not all attributable to rule guidance.

[First-round records](../../review/hsp90_q01-round-20260910/HSP90_Q01_VERIFIED_REPORT_ZH.md) · [Native-NOE analysis, thresholds and trajectory-level sources](../../review/hsp90_q01-round-20260910/v4_native_noe/outputs/report/DEEP_READER_ZH.md) · [Portable input provenance](../data/MANIFEST.json)

## Nanodisc: a better scattering fit did not improve both NOE readouts

**What the authors argued.** Bengtsen and colleagues combined NMR, SAXS, SANS, MD and other measurements to describe a nanodisc ensemble with heterogeneous elliptical shapes. They compared separately and jointly reweighted ensembles and evaluated additional observables. The original paper already contains SAXS-only/NOE-only/joint comparisons. [Original paper](https://doi.org/10.7554/eLife.56518) · [Open-access full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7426092/)

**What we tested.** Using the deposited candidate pool, does changing weights to fit SAXS alone also improve NOE predictions when both old and new weights are scored on the same fixed constraints? BME reweighting changes the contributions of existing conformations; it does not generate missing structures.

**Observed result.** The analysis uses 1,195 candidate frames, 90 SAXS points, 292 amide-labelled and 40 methyl NOE constraints. The main result is a within-channel comparison of one-sided, error-scaled NOE penalties, averaged over a fixed constraint set; smaller means less discrepancy under that definition.

| Weights | SAXS mean penalty | Amide NOE mean penalty | Methyl NOE mean penalty |
|---|---:|---:|---:|
| Uniform | 10.0188 | 0.9334 | 3.8931 |
| SAXS-only, θ = 6 | 1.1707 | 0.9647 | 4.4695 |
| SAXS-only, θ = 60 | 2.1178 | 0.9710 | 3.9275 |

NOE was not used in these two optimizations. Both NOE penalties rise at both settings, but the magnitude differs; for methyl NOE it is approximately 14.81% and 0.88%, respectively. These are descriptive changes, not significance tests. Author and older joint-fit weights remain reference results, not independent NOE validation.

**What we can say.** Improving SAXS does not automatically improve the tested NOE predictions. This does not establish physical inconsistency between experiments, a unique ensemble or a shape distribution. Candidate construction and earlier method development used NMR-related information, so withholding NOE from this particular optimizer is not a fully independent validation of the entire workflow. The project's statistic is not silently substituted for the paper's differently reported NOE summary.

**Who produced it.** Developers specified and performed the cross-observable comparison. A later narrow adapter passed saved scores to the prototype. The direct and Rules paths shared the numerical core and answer formatter; their agreement did not demonstrate independent reasoning or rule-specific accuracy gain.

[Deposited methods and inputs](https://github.com/KULL-Centre/papers/tree/main/2020/nanodisc-bengtsen-et-al/BME_reweight) · [Saved project report](https://github.com/alex051107/dynamics-atlas-harness/blob/316471a135a95032f8726999e807393f55f6ceb5/review/rules-agent-study-20260909/references/07_REPORT_ZH.md) · [Q05's separate role in the completed method-guidance comparison](../../review/four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md#6-retrieved-method-cards-did-not-outperform-the-short-protocol-consistently)

The portable three-system replay in this folder does not rerun this nanodisc calculation. Do not conflate the new SAXS-only analysis with the later Agent task on supplied author predictions and weights.

## DHFR: corrected proximity is not a kinetic mechanism

**What the authors argued.** Cetin and colleagues linked the improved performance of 4′-DTMP relative to TMP to local interactions and protein-wide dynamical networks, supporting a kinetic rather than a simple thermodynamic explanation. Their study included experimental information, free-energy calculations, hydrogen-bond geometry and network analysis. [Original paper, Abstract, Figs. 4–8 and Conclusions](https://pubs.acs.org/doi/10.1021/acs.jcim.3c00818) · [PubMed record](https://pubmed.ncbi.nlm.nih.gov/37491825/)

**What we tested.** After appropriate coordinate preparation, how do selected protein–ligand distances differ between the two inhibitors in the deposited WT and L28R trajectories?

**Observed result.** An inappropriate wrapped representation initially created apparent large separations. The first two Agents did not identify that input defect. Developers corrected the local periodic representation and cross-checked selected distances with VMD to approximately 0.00001 Å. The reported window uses 990 frames, frames 11–1000, from one selected trajectory per condition.

| Variant | TMP mean M20–O3P / Å | 4′-DTMP mean M20–O3P / Å |
|---|---:|---:|
| WT | 8.687677 | 4.622056 |
| L28R | 10.435783 | 4.808910 |

**What we can say.** The chosen local distance is smaller for 4′-DTMP in both variants in these trajectories. That is a local proximity observation, not a test of hydrogen-bond angles, an independent kinetic estimate or a unique inhibition mechanism. The single-trajectory scope belongs to this project subset, not a claim that the original paper had no other simulations. O3P is the deposited atom label, not evidence of a phosphate group in TMP.

**Who produced it.** The correction and cross-check were developer work. Original Agent answers on the defective table remain preserved; corrected numbers are not substituted into their scores.

[Scientific report and correction trail](../../review/dhfr_q01-round-20260910/report/DEEP_READER_ZH.md) · [Original data](https://zenodo.org/records/7966540) · [Reproduction scope](REPRODUCE.md)

## ADK: apo domain motion does not reproduce an ATP-triggered experiment

**What the authors argued.** Orädd and colleagues studied the ATP-binding response of adenylate kinase using time-resolved X-ray solution scattering, with ATP photorelease in the presence of AMP. The reported experimental response is not an observation from the apo trajectories used here. [Original paper](https://doi.org/10.1126/sciadv.abi5514)

**What we tested.** In two deposited apo trajectories, how do project-defined LID–CORE and NMP–CORE Cα distance descriptors change between the first and last 10% of saved frames?

**Observed result.** A generic half-box rejection initially misclassified legitimate distances within a complete protein. The analysis instead used a complete molecular representation, checked continuity and atom mapping, and cross-checked specified pairs against GROMACS (approximately 0.005 Å difference). Another implementation agreed on the domain descriptors to within 10⁻¹⁰ Å. The open-start trajectory covers 0–450.4 ns and the closed-start trajectory 0–335.4 ns, with one trajectory per start.

| Start | NMP–CORE change / Å | LID–CORE change / Å |
|---|---:|---:|
| Open | +0.070721 | +2.290411 |
| Closed | +1.090895 | +1.176421 |

**What we can say.** Both descriptors increase in each endpoint-window comparison; neither comparison shows joint net closure. Overlapping distributions and local events remain possible. Different ligands, timescales and observables prevent treating this result as a reproduction or refutation of the experimental ATP-triggered intermediate.

**Who produced it.** Developers prepared and validated the distance representation. The two ordinary Agent runs correctly reported the four endpoint changes; that does not mean they discovered the coordinate treatment independently.

[Analysis and condition comparison](../../review/four-layer-20260910/outputs/ADK_SCIENCE_ZH.md) · [Original data](https://zenodo.org/records/5583119) · [Agent–paper relationship record](../../review/four-layer-20260910/outputs/ADK_PAPER_RELATIONSHIPS.md)

## The Rules experiment is a separate claim

Our hypothesis was that source-linked guidance or limited checks could improve supported answers over an Agent with the same prepared data and tools. The hypothesis was not that agreement with an author's wording, successful execution or more references to rules would establish scientific correctness.

The method-guidance medians below summarize four runs per question and condition, using five frozen content units. They are not percentages of general scientific accuracy.

| Guidance | HSP90: correct units / 5 | Nanodisc: correct units / 5 |
|---|---:|---:|
| Short protocol | 4.5 | 4.5 |
| Full selected rules | 2.0 | 5.0 |
| Method cards | 2.5 | 4.5 |

Full rules' Q05 benefit is retained, alongside the HSP90 loss. The evidence does not separate all effects of knowledge content, retrieval, text length, task difficulty and baseline ability.

The other tests found that the warning-card file was not read in any of four card runs; none of nine numeric-trace warnings targeted a core scientific error; and none of twelve feedback answers reduced its initial core-error count. Explicit subquestions raised median supported coverage from 2 to 2.5 out of 3 in HSP90 and from 2 to 3 out of 3 in ADK, but HSP90 core errors totaled one before and two after the framing change. The questions added explicit requests; this is not proof of improved autonomous reasoning.

[Sealed individual scores, now unblinded](../../review/four-layer-20260910/outputs/UNBLINDED_SCORES.csv) · [Evaluation and intervention limits](../../review/four-layer-20260910/outputs/METHODS_AND_LIMITS_ZH.md) · [Feedback audit](../../review/four-layer-20260910/outputs/E2_CHECKER_EFFECT_REVIEW_ZH.md)

## What has not been established

There is no overall scientific accuracy estimate, independent domain-expert evaluation of the full pilot, or measured reduction in researcher preparation/correction time. Successful numerical reproduction supports the declared calculations, not their complete biological interpretation. The component pilot has finished; this page proposes no rerun or post-unblinding score change.

[Return to the decisions for discussion](../README.md#5-four-decisions-on-which-we-need-guidance)
