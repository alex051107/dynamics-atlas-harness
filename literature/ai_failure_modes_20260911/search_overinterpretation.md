# Literature search: over-reading and mis-reading of protein dynamics/ensemble data, and LLM overconfidence in scientific claims

Search date: 2026-09-11. Method: WebSearch plus WebFetch on primary sources, read-only. Scope: 2015-2026 for
data-type pitfalls, 2023-2026 for LLM calibration/sycophancy/overclaiming, with two pre-2015 foundational
cross-validation papers kept because they are the direct precedent for the "fitted data used as its own
validation" pitfall named in the task brief. Papers already held by the project (Grossfield 2019, Zuckerman
2011, Bottaro/Lindorff-Larsen reviews, Bonomi 2017 ensemble determination, Li/Thomasen/Cossio 2026 blog) are
excluded from the table below; only new finds are listed. A handful of URLs returned HTTP 403 or an auth
redirect and could not be opened directly (Nature.com and Cell Press pages); those citations were reconstructed
from PubMed/search-snippet metadata and are marked "citation from search snippet, primary page not opened."

## 1. Paper table

| # | Citation | Data type | Pitfall(s) documented | Recommended check |
|---|----------|-----------|------------------------|---------------------|
| 1 | Braun E, Gilmer J, Mayes HB, Mobley DL, Monroe JI, Prasad S, Zuckerman DM (2019). "Best Practices for Foundations in Molecular Simulations [Article v1.0]." *Living J. Comput. Mol. Sci.* 1(1):5957. DOI 10.33011/livecoms.1.1.5957. | MD (setup/foundations) | Treating a simulation as physically meaningful without checking force field applicability, integrator/thermostat artifacts, or system-preparation errors before any dynamics analysis begins. | Report force field provenance and validation domain, integrator and thermostat/barostat settings, and system-preparation steps (protonation, missing atoms) as a precondition for trusting any downstream ensemble quantity. |
| 2 | Communications Biology Editorial (2023). "Reliability and reproducibility checklist for molecular dynamics simulations." *Commun. Biol.* 6:268. DOI 10.1038/s42003-023-04653-0. (Journal editorial/checklist, no individual byline in the record.) | MD (general) | Reporting a single trajectory's observable as "the" result; insufficient convergence assessment; underspecified methods that block independent reproduction. | At least three independent replicate simulations per condition with statistical analysis of convergence; full parameter and input/output disclosure in a public repository. |
| 3 | Song J, Li J, Chan HS (2021). "Small-Angle X-ray Scattering Signatures of Conformational Heterogeneity and Homogeneity of Disordered Protein Ensembles." *J. Phys. Chem. B* 125(24):6451-6478. DOI 10.1021/acs.jpcb.1c02453. (Also arXiv:2105.13427.) | SAXS | Some heterogeneous ensembles with drastically different asphericity and end-to-end distance produce practically identical SAXS molecular form factors, so a good SAXS fit does not establish that an inferred ensemble's shape statistics are correct or unique. | Test whether the fitted ensemble is one of several ensembles with distinct shape/heterogeneity properties that all reproduce the same scattering profile before reporting a heterogeneity/homogeneity conclusion from SAXS alone. |
| 4 | Shevchuk R, Hub JS (2017). "Bayesian refinement of protein structures and ensembles against SAXS data using molecular dynamics." *PLOS Comput. Biol.* 13(10):e1005800. DOI 10.1371/journal.pcbi.1005800. | SAXS + MD | Refining a structure or ensemble against SAXS without a prior can produce an artificially over-fitted result driven by scattering noise rather than physical restraints. | Use a Bayesian/maximum-entropy weighting that keeps the MD force-field prior in the loop, rather than free least-squares fitting of structures to the scattering curve. |
| 5 | Singh B, Martinez-Noa Y, Perez A (2026). "How Well Do Molecular Dynamics Force Fields Model Peptides? A Systematic Benchmark Across Diverse Folding Behaviors." *J. Phys. Chem. B* 130(16):4344-4357. DOI 10.1021/acs.jpcb.6c01176. (Preprint: bioRxiv 2025.07.31.667969.) | MD (force field benchmark) | No single fixed-charge force field performs well across all peptide folding behaviors; some force fields impose a structural bias (over-helical or over-compact) strong enough to dominate the reported ensemble regardless of the input sequence. | Benchmark the specific force field against folded and extended starting states for a system with known reference behavior before trusting its equilibrium ensemble; do not assume transferability from one class of protein to another (e.g., folded globular to disordered). |
| 6 | Falkner B, Schroder GF (2013). "Cross-validation in cryo-EM-based structural modeling." *Proc. Natl. Acad. Sci. USA* 110(22):8930-8935. DOI 10.1073/pnas.1119041110. (Pre-2015; kept as the direct precedent for the "fitted data as validation" pitfall named in the task brief. Primary PNAS page returned HTTP 403; citation reconstructed from PubMed/Schroder-lab-hosted PDF metadata.) | Cryo-EM | At low resolution the number of free model parameters exceeds the number of independent observables in the map, so a model can be refined to fit the density well while being substantially wrong; using the same density to both build and "validate" a model is circular. | Cross-validate by refining against half the data (or a masked/held-out region) and evaluating fit quality against the other half, analogous to crystallographic free-R. |
| 7 | Wlodarski T, Streit JO, Mitropoulou A, Cabrita LD, Vendruscolo M, Christodoulou J (2024). "Bayesian reweighting of biomolecular structural ensembles using heterogeneous cryo-EM maps with the cryoENsemble method." *Sci. Rep.* DOI 10.1038/s41598-024-68468-7. | Cryo-EM | Ambiguous or blurred density in a heterogeneous cryo-EM map can be misattributed to intrinsic conformational dynamics of one component when it actually reflects a separate bound partner (compositional, not conformational, heterogeneity). | Fit a reweighted structural ensemble (not a single averaged structure) against the map and check whether the "extra" density is better explained by an additional molecular species before calling it a dynamic ensemble. |
| 8 | Hoff SE, Bonomi M, Fraser JS, Greene EM (2024). "Extracting conformational heterogeneity from 2D and 3D cryo-EM data." *Biophys. J.* 123(3, Suppl.):50a-51a. (Biophysical Society meeting abstract; full paper not yet located, cite with that caveat.) | Cryo-EM | Standard single-structure refinement pipelines discard the conformational information present in raw 2D particle images and 3D density by collapsing it to one consensus model. | Use ensemble-integrative tools (BioEM for 2D particles, EMMIVox for 3D density) with coarse-grained/MD-generated candidate ensembles rather than fitting a single structure to the reconstruction. |
| 9 | Cheng Y et al. (2026). "Making sense of invisible densities in single-particle cryo-EM." *IUCrJ* 13(3). PMID 42028876. (Corresponding author Yifan Cheng, UCSF; full co-author list not independently verified beyond the corresponding author.) | Cryo-EM | Poor local resolution or a fully "invisible" (missing) density region is often read as simple flexibility, when it can also reflect compositional heterogeneity, partial occupancy, or processing artifacts; the absence of density is not itself evidence of a specific dynamic mechanism. | Combine cryo-EM with an orthogonal method (MD, crosslinking-MS, SAXS, etc.) before assigning a causal interpretation to a disappearing density region. |
| 10 | Lerner E, Barth A, Hendrix J, Ambrose B, Birkedal V, Blanchard SC, et al. (2021). "FRET-based dynamic structural biology: challenges, perspectives and an appeal for open-science practices." *eLife* 10:e60416. DOI 10.7554/eLife.60416. | smFRET | Photophysical artifacts (blinking, bleaching, dye-dye interaction), uncorrected gamma-factor, stochastic donor/acceptor labeling, and non-standardized burst-selection/kinetic-analysis choices can each masquerade as a genuine conformational signal or transition rate. | Publish raw photon data, correction factors, and selection criteria in a standardized format; cross-validate with an alternative dye pair, immobilization strategy, or modality (confocal vs. TIRF) before reporting a dynamic distance or rate as established. |
| 11 | Agam G, Gebhardt C, Popara M, et al. (2023). "Reliability and accuracy of single-molecule FRET studies for characterization of structural dynamics and distances in proteins." *Nat. Methods* 20:523-535. DOI 10.1038/s41592-023-01807-0. (Nature.com page returned an auth redirect; citation reconstructed from PubMed/press-release metadata.) | smFRET | A 19-laboratory blind study found meaningful lab-to-lab spread in inferred FRET efficiencies and distances even on identical samples, showing that a single lab's smFRET distance/dynamics estimate carries irreducible uncertainty beyond its own reported precision. | Report inter-dye distance uncertainty against the blind-study benchmark (about 2 A precision, about 5 A accuracy) rather than propagating only within-lab statistical error; prefer results replicated across labs or methods. |
| 12 | Smith LJ, van Gunsteren WF, Hansen N (2020/2021). "On the Use of Side-Chain NMR Relaxation Data to Derive Structural and Dynamical Information on Proteins: A Case Study Using Hen Lysozyme." *ChemBioChem* 22(6):1049-1064. DOI 10.1002/cbic.202000674. | NMR relaxation | Different internal-correlation-function/order-parameter models can fit the same experimental relaxation data equally well while implying substantially different underlying motions, so a good fit to relaxation data does not by itself identify the correct dynamical model. | Use MD simulation to discriminate among order-parameter representations that are degenerate with respect to the NMR relaxation data alone, rather than accepting the best-fit model as physically unique. |
| 13 | Erman B, et al. (2024). "Dynamically driven correlations in elastic net models reveal sequence of events and causality in proteins." *Proteins* 92(9):1113-1126. DOI 10.1002/prot.26697. (Preprint: bioRxiv 2024.01.15.575718. Full co-author list beyond the corresponding author not independently verified.) | MD / elastic network models | Static or time-averaged correlation between two residues' motions (e.g., from PCA/covariance) is routinely read as evidence of a direct causal or allosteric driver-driven relationship, when correlation alone cannot establish directionality. | Use time-lagged/phase-difference analysis (their DP-GNM approach) to test directionality of information flow before describing a correlated pair as causally linked or allosteric. |
| 14 | Sharma M, Tong M, Korbak T, Duvenaud D, Askell A, Bowman SR, et al. (2023, published ICLR 2024). "Towards Understanding Sycophancy in Language Models." arXiv:2310.13548. | LLM behavior (not protein data, but the community-recommended check generalizes) | Five state-of-the-art AI assistants consistently exhibit sycophancy across free-form text-generation tasks, adjusting correct answers toward an incorrect user-stated belief in a meaningful fraction of cases, including on tasks framed as fact-checking. | Test a model's stated conclusion against a paraphrase of the same question with the user's stated belief flipped or removed; treat agreement that tracks the user's framing (not the evidence) as a sycophancy flag. |
| 15 | Chhikara P (2025, published TMLR 12/2025). "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models." arXiv:2502.11028; OpenReview. | LLM calibration | Across nine LLMs and three QA datasets, verbalized confidence is systematically miscalibrated (high stated confidence on wrong answers); larger RLHF-tuned models can paradoxically become more miscalibrated on easier queries. | Do not take a model's self-reported confidence at face value; use distractor-augmented or self-consistency probes and report expected calibration error against a held-out accuracy check, not the model's own verbal confidence. |
| 16 | Javaji SR, Cao Y, Li H, Yu Y, Muralidhar N, Zhu Z (2025). "Can AI Validate Science? Benchmarking LLMs for Accurate Scientific Claim -> Evidence Reasoning." arXiv:2506.08235; published as CLAIM-BENCH, IJCNLP 2025 / ACL Anthology 2025.ijcnlp-long.127. | LLM scientific reasoning | Across six LLMs and 300+ claim-evidence pairs from research papers, models show significant limitations distinguishing whether a piece of text actually supports, contradicts, or is merely adjacent to a stated scientific claim. | Benchmark an LLM's claim-to-evidence linking on a held-out, human-annotated claim/evidence set specific to the target domain before trusting it to certify that a dataset supports a given scientific conclusion. |
| 17 | (Survey, secondary source) "Large Language Models Hallucination: A Comprehensive Survey." arXiv:2510.06265 (2025). Author list not independently verified from the snippet; cite with that caveat if used. | LLM reliability (background) | Consolidates that no single widely accepted metric or benchmark captures the multidimensional nature of LLM hallucination, so a single benchmark pass is weak evidence of general reliability. | Use multiple, task-specific hallucination probes rather than one aggregate benchmark score when certifying an LLM component of a pipeline. |

Notes on access: the PNAS page for entry 6, the Cell Press/Biophysical Journal pages for entries 3 and 8 (fulltext
mirrors), and the Nature.com page for entry 11 could not be opened directly (HTTP 403 or an authentication
redirect); their citations above were reconstructed from PubMed records, publisher search snippets, or
lab-hosted PDF mirrors, not from reading the fulltext page itself. Entry 9's and entry 13's full co-author
lists could not be confirmed beyond the corresponding/most-cited author; treat those two author lists as
provisional until checked against the published paper or Zotero import metadata.

## 2. Consolidated pitfall list across data types

**Unconverged or under-replicated sampling read as a converged population** (MD). In our list: yes
(Grossfield 2019, Zuckerman 2011 already cover this). New papers: #1 Braun et al. 2019, #2 Communications
Biology checklist 2023. Quantitative criterion given: yes, #2 specifies "at least three independent
simulations per condition with statistical analysis" as a concrete numeric bar.

**Blurred or averaged density read as a well-defined ensemble** (cryo-EM). In our list: partially, via
Bonomi 2017 (ensemble determination) but not the cryo-EM-specific blurring/compositional-heterogeneity
confusion. New papers: #7 cryoENsemble, #8 Hoff et al. abstract, #9 Cheng et al. 2026. Quantitative
criterion given: no; these are methodological/interpretive recommendations (fit an ensemble, add an
orthogonal method) rather than numeric thresholds.

**Non-unique or degenerate fits mistaken for a unique ensemble** (SAXS, cryo-EM, NMR order parameters).
In our list: partially, Bonomi 2017 and Bottaro/Lindorff-Larsen reviews touch ensemble determination in
general but the specific "many-to-one form factor" and "degenerate order-parameter" demonstrations are new.
New papers: #3 Song/Li/Chan 2021 (SAXS form-factor degeneracy), #6 Falkner/Schroder 2013 (cryo-EM
overfitting/circularity), #12 Smith/van Gunsteren/Hansen 2020 (NMR order-parameter degeneracy).
Quantitative criterion given: yes for #6 (cross-validation against held-out data, analogous to
crystallographic free-R) and yes for #11's precision/accuracy numbers used as a benchmark floor; no explicit
number in #3 or #12 beyond "practically identical" fits.

**Comparing quantities with mismatched spatial or time averaging as if they were the same observable**
(cross-method comparison). Not separately itemized in our held list under this name. New paper: #10 Lerner
et al. 2021 documents smFRET sub-population averages conflating a single state with a millisecond average
of rapidly interconverting states, which is exactly this pitfall for smFRET. Quantitative criterion given:
no explicit number, but a concrete practice (report burst-selection criteria and dye-correction factors so
readers can judge what is being averaged).

**Force-field bias substituting for the true conformational preference** (MD). In our list: implicitly via
Zuckerman 2011/Grossfield 2019 sampling-quality framing, not force-field-specific. New paper: #5 Singh,
Martinez-Noa, Perez 2026. Quantitative criterion given: no single number, but a systematic benchmark design
(fold from both folded and extended states) that operationalizes "check before you trust."

**Treating a fitted or reweighted ensemble as validated by the same data used to fit it (circularity)**
(SAXS, cryo-EM). In our list: not explicitly under this name. New papers: #4 Shevchuk/Hub 2017 (Bayesian
prior against overfitting to SAXS noise), #6 Falkner/Schroder 2013 (cross-validation demanded for cryo-EM).
Quantitative criterion given: yes, #6's half-data cross-validation is directly quantitative and portable to
our own validation design.

**Correlation among residues or observables read as a causal or allosteric driver-driven relationship**
(MD/PCA/elastic-network models). Not separately itemized in our held list. New paper: #13 Erman et al. 2024.
Quantitative criterion given: no numeric threshold, but a specific alternative analysis (time-lagged/phase
correlation) that can be operationalized as a check.

**LLM verbalized confidence and agreement taken as evidence of correctness** (applies to our own agent's
judgments, not the underlying protein data). Not in our held list (that list is protein-dynamics-specific).
New papers: #14 Sharma et al. 2023/2024 (sycophancy), #15 Chhikara 2025 (miscalibration), #16 Javaji et al.
2025 (claim-evidence reasoning failure), #17 hallucination survey. Quantitative criterion given: yes for
#15 (expected calibration error, accuracy-improvement percentages under distractor probes) and #11's
inter-lab uncertainty numbers, which double as a template for what a "quantitative calibration check" for
our own agent's ensemble-quantity judgments could look like.

## 3. Initial ideas for what a rules table for this task should collect

A rules table for this task should record, for every documented pitfall, the minimum information needed to
turn a paper's warning into an automatic check our harness can run. Concretely, that means: the data type it
applies to (MD, NMR, smFRET, SAXS, cryo-EM, or "AI judgment" as its own category), the specific observable at
risk (a population, a rate, a distance, a claim of causality), the failure mode in one sentence, and whether
the source paper gives a checkable criterion (a number, a cross-validation recipe, a required replicate
count) or only a qualitative recommendation. Braun et al. 2019 and the Communications Biology 2023 checklist
are useful models for this column because they already phrase their guidance as checklist items rather than
prose, which is close to the format our rules table needs (Braun E, et al. 2019, *Living J. Comput. Mol.
Sci.* 1(1):5957; Communications Biology Editorial 2023, *Commun. Biol.* 6:268).

The table should separately track whether a check is falsifiable from data already inside a resource's
packet versus whether it requires an external, orthogonal source. The cryo-EM literature draws this line
sharply: a blurred-density interpretation is only resolved by combining the map with MD, crosslinking-MS, or
an ensemble-integrative tool, not by re-processing the same map (Cheng et al. 2026, *IUCrJ* 13(3); Wlodarski
et al. 2024, *Sci. Rep.*, DOI 10.1038/s41598-024-68468-7). Our rules table should flag which of its rules can
be evaluated in-packet and which require the agent to either abstain or explicitly request a second, orthogonal
resource before proceeding, since conflating the two is itself a documented pitfall (using a fit as its own
validation; Falkner & Schroder 2013, *PNAS* 110(22):8930-8935).

Where a paper supplies a numeric criterion, the rules table should store that number as a machine-checkable
threshold rather than paraphrase it as a qualitative warning, because a threshold is what lets the harness
decide pass/fail instead of leaving it to narrative judgment. Examples worth carrying forward verbatim: at
least three independent replicate simulations per condition before claiming convergence (Communications
Biology Editorial 2023, *Commun. Biol.* 6:268); an inter-dye distance uncertainty floor of about 2 A precision
and 5 A accuracy from the 19-lab smFRET blind study, below which a single lab's claimed precision should be
treated with suspicion (Agam, Gebhardt, Popara, et al. 2023, *Nat. Methods* 20:523-535); and a cross-validation
split (fit on half the data, score against the held-out half) as the operational definition of "not circular"
for any fitted structural model (Falkner & Schroder 2013, *PNAS* 110(22):8930-8935).

Because the Dynamics Atlas agent is itself an LLM making trust judgments, the rules table should include a
fourth category alongside MD/NMR/smFRET-SAXS/cryo-EM: checks on the agent's own claims. Sycophancy and
calibration research gives two concrete, reusable check designs for this category. First, re-ask the same
trust judgment with the user's or task's stated expectation flipped or removed, and flag disagreement that
tracks the framing rather than the evidence as a sycophancy signal (Sharma, Tong, Korbak, et al. 2023/2024,
arXiv:2310.13548). Second, never accept the agent's self-reported confidence at face value; score it against
an expected-calibration-error style check using a held-out set of cases with known ground truth, following the
distractor-probe design that produced large calibration-error reductions in Chhikara 2025 (arXiv:2502.11028,
TMLR 2025) and the claim-to-evidence linking failures documented in Javaji, Cao, Li, et al. 2025
(arXiv:2506.08235).

A fifth column worth adding is provenance risk: whether the pitfall arises from a property of the underlying
physics/instrument (force-field bias, SAXS degeneracy, photophysical artifact) versus a property of the
analysis choice (order-parameter model, dimensionality-reduction projection, correlation-to-causation leap).
The force-field benchmark of Singh, Martinez-Noa, and Perez (2026, *J. Phys. Chem. B* 130(16):4344-4357) and
the order-parameter degeneracy case study of Smith, van Gunsteren, and Hansen (2020/2021, *ChemBioChem*
22(6):1049-1064) sit on opposite sides of that line, and a rules table that does not separate them risks
recommending the same fix (more sampling) for a problem that sampling cannot actually solve (a wrong choice
of analysis model).

## 4. RIS block

```ris
TY  - JOUR
AU  - Braun, Efrem
AU  - Gilmer, Justin
AU  - Mayes, Heather B.
AU  - Mobley, David L.
AU  - Monroe, Jacob I.
AU  - Prasad, Samarjeet
AU  - Zuckerman, Daniel M.
PY  - 2019
TI  - Best Practices for Foundations in Molecular Simulations [Article v1.0]
JO  - Living Journal of Computational Molecular Science
VL  - 1
IS  - 1
SP  - 5957
DO  - 10.33011/livecoms.1.1.5957
ER  -

TY  - JOUR
AU  - ,
PY  - 2023
TI  - Reliability and reproducibility checklist for molecular dynamics simulations
JO  - Communications Biology
VL  - 6
SP  - 268
DO  - 10.1038/s42003-023-04653-0
ER  -

TY  - JOUR
AU  - Song, Jianhui
AU  - Li, Jichen
AU  - Chan, Hue Sun
PY  - 2021
TI  - Small-Angle X-ray Scattering Signatures of Conformational Heterogeneity and Homogeneity of Disordered Protein Ensembles
JO  - Journal of Physical Chemistry B
VL  - 125
IS  - 24
SP  - 6451
EP  - 6478
DO  - 10.1021/acs.jpcb.1c02453
ER  -

TY  - JOUR
AU  - Shevchuk, Roman
AU  - Hub, Jochen S.
PY  - 2017
TI  - Bayesian refinement of protein structures and ensembles against SAXS data using molecular dynamics
JO  - PLOS Computational Biology
VL  - 13
IS  - 10
SP  - e1005800
DO  - 10.1371/journal.pcbi.1005800
ER  -

TY  - JOUR
AU  - Singh, Bhumika
AU  - Martinez-Noa, Yenny
AU  - Perez, Alberto
PY  - 2026
TI  - How Well Do Molecular Dynamics Force Fields Model Peptides? A Systematic Benchmark Across Diverse Folding Behaviors
JO  - Journal of Physical Chemistry B
VL  - 130
IS  - 16
SP  - 4344
EP  - 4357
DO  - 10.1021/acs.jpcb.6c01176
ER  -

TY  - JOUR
AU  - Falkner, Beata
AU  - Schroder, Gunnar F.
PY  - 2013
TI  - Cross-validation in cryo-EM-based structural modeling
JO  - Proceedings of the National Academy of Sciences
VL  - 110
IS  - 22
SP  - 8930
EP  - 8935
DO  - 10.1073/pnas.1119041110
ER  -

TY  - JOUR
AU  - Wlodarski, Tomasz
AU  - Streit, Judith Ottilie
AU  - Mitropoulou, Anastasia
AU  - Cabrita, Lisa D.
AU  - Vendruscolo, Michele
AU  - Christodoulou, John
PY  - 2024
TI  - Bayesian reweighting of biomolecular structural ensembles using heterogeneous cryo-EM maps with the cryoENsemble method
JO  - Scientific Reports
DO  - 10.1038/s41598-024-68468-7
ER  -

TY  - CPAPER
AU  - Hoff, Sarah E.
AU  - Bonomi, Massimiliano
AU  - Fraser, James S.
AU  - Greene, Eric M.
PY  - 2024
TI  - Extracting conformational heterogeneity from 2D and 3D cryo-EM data
JO  - Biophysical Journal
VL  - 123
IS  - 3
SP  - 50a
EP  - 51a
ER  -

TY  - JOUR
AU  - Cheng, Yifan
PY  - 2026
TI  - Making sense of invisible densities in single-particle cryo-EM
JO  - IUCrJ
VL  - 13
IS  - 3
ER  -

TY  - JOUR
AU  - Lerner, Eitan
AU  - Barth, Anders
AU  - Hendrix, Jelle
AU  - Ambrose, Benjamin
AU  - Birkedal, Victoria
AU  - Blanchard, Scott C.
PY  - 2021
TI  - FRET-based dynamic structural biology: challenges, perspectives and an appeal for open-science practices
JO  - eLife
VL  - 10
SP  - e60416
DO  - 10.7554/eLife.60416
ER  -

TY  - JOUR
AU  - Agam, Ganesh
AU  - Gebhardt, Christian
AU  - Popara, Milana
PY  - 2023
TI  - Reliability and accuracy of single-molecule FRET studies for characterization of structural dynamics and distances in proteins
JO  - Nature Methods
VL  - 20
SP  - 523
EP  - 535
DO  - 10.1038/s41592-023-01807-0
ER  -

TY  - JOUR
AU  - Smith, Lorna J.
AU  - van Gunsteren, Wilfred F.
AU  - Hansen, Niels
PY  - 2021
TI  - On the Use of Side-Chain NMR Relaxation Data to Derive Structural and Dynamical Information on Proteins: A Case Study Using Hen Lysozyme
JO  - ChemBioChem
VL  - 22
IS  - 6
SP  - 1049
EP  - 1064
DO  - 10.1002/cbic.202000674
ER  -

TY  - JOUR
AU  - Erman, Burak
PY  - 2024
TI  - Dynamically driven correlations in elastic net models reveal sequence of events and causality in proteins
JO  - Proteins
VL  - 92
IS  - 9
SP  - 1113
EP  - 1126
DO  - 10.1002/prot.26697
ER  -

TY  - JOUR
AU  - Sharma, Mrinank
AU  - Tong, Meg
AU  - Korbak, Tomasz
AU  - Duvenaud, David
AU  - Askell, Amanda
AU  - Bowman, Samuel R.
PY  - 2023
TI  - Towards Understanding Sycophancy in Language Models
JO  - arXiv:2310.13548
ER  -

TY  - JOUR
AU  - Chhikara, Prateek
PY  - 2025
TI  - Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models
JO  - Transactions on Machine Learning Research
ER  -

TY  - JOUR
AU  - Javaji, Shashidhar Reddy
AU  - Cao, Yupeng
AU  - Li, Haohang
AU  - Yu, Yangyang
AU  - Muralidhar, Nikhil
AU  - Zhu, Zining
PY  - 2025
TI  - Can AI Validate Science? Benchmarking LLMs for Accurate Scientific Claim to Evidence Reasoning
JO  - arXiv:2506.08235
ER  -

TY  - JOUR
PY  - 2025
TI  - Large Language Models Hallucination: A Comprehensive Survey
JO  - arXiv:2510.06265
ER  -
```
