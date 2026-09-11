# Rules Table, version 2

Updated 11 September 2026. Version 1 (7 August 2026) is kept unchanged in [RULES_TABLE.md](RULES_TABLE.md) and [rule_registry_v0.1.csv](rule_registry_v0.1.csv). The machine-readable version 2 is [rules_v2.csv](rules_v2.csv).

Version 1 listed what 11 methods papers warn about, three rules per paper. Version 2 is organized the way the table was meant to work from the start: each rule names the question it helps answer, the situation that triggers it, the analysis (operator) it acts through, what must hold, what the result may claim, and where to stop. Each row also records what has happened to the rule so far and the file that shows it. The table keeps all 33 original rules and adds four rules from the literature on sampling quality and kinetics in MD, and five rules we learned from our own data.

## Version 1 and version 2

| | Version 1 (7 August 2026) | Version 2 (11 September 2026) |
|---|---|---|
| Organized by | Source paper, three rules each | The question a rule helps answer |
| Rules | 33, from 11 methods papers on smFRET, SAXS, cryo-EM, DEER and ensemble modelling | 42: the same 33, 4 from the MD sampling-quality and kinetics literature, 5 learned from our own data |
| One row holds | What the paper showed, what to check, where to stop, how far the lesson carries | When the rule applies, the operator or check it acts through, what must hold, what may be claimed, where to stop, and its status |
| How a rule reaches an analysis | A selector matched rules by data type, and the text was pasted into the AI's prompt | Through operator preconditions, claim limits and the answer check; the AI does not read rule text |
| Tested so far | As prompt text, method cards, a warning file and a post-answer check (10 September): no stable gain, and FRET conditions leaked into an NMR question | Inside operators with an answer check (11 September): numbers became checkable, and two definitions failed a control. The same content given as text has not been compared yet |

## What version 2 shows

- Of the 33 original rules, 13 bear on the four cases. They act as framing, as limits on what may be claimed, or inside the nanodisc analysis. The other 20 concern smFRET, cryo-EM or DEER data, which none of the cases has. Two of those 20 (C001-RULE-002 and C003-RULE-002) were applied to the HSP90 NMR question on 10 September, where they did not belong.
- None of the 33 says how to decide whether an MD quantity has converged, whether a population can be stated, or whether a state has been reached, which are the questions HSP90 needed. The criteria for those in version 2 come from the sampling-quality and kinetics literature (Grossfield et al. 2019; Prinz et al. 2011), which our literature review covered on 8 September but the rules never drew on, and from errors found in our own data.
- The rules that decided the 11 September results were written by us (P-01 to P-05). P-05 records a definition that failed its control. No domain expert has reviewed any rule in either version.
- Version 2 records the intended links. The operator cards used on 11 September do not cite these rule IDs yet, and version 2 has not been tested against version 1 or against the same rules given as text.

## How to read a row

- **Applies when**: the situation in the analysis that triggers the rule.
- **Acts through**: the operator or check that carries the rule. "None" means no analysis in this project uses it yet. The indented line says what must hold before the result is used.
- **What may be claimed**: the strongest statement allowed, and the label reported when the rule's check cannot be made.
- **Status**: what has happened to the rule so far, with the file that shows it. S- rules come from the sampling-quality and kinetics literature, P- rules from our own data, C- rules from version 1.


## Can a population, a transition or a rate be stated?

| Rule | Applies when | Acts through | What may be claimed | Status |
|---|---|---|---|---|
| **S-01**<br>Grossfield et al. 2019 | A mean or a state fraction is computed from MD frames. | OP3, to be rebuilt as block averaging per observable.<br>*Must hold:* The uncertainty is estimated for that observable from block averages or independent runs; frames are not independent samples. | The fraction with its uncertainty and window. No equilibrium population unless S-02 holds. Stop: `UNCERTAINTY_NOT_ESTIMABLE` | Planned. The current OP3 uses an uncalibrated 0.05 window test instead.<br>`data/operators/results/OP3.json` |
| **S-02**<br>Henot et al. 2022; Grossfield et al. 2019; project criterion of 28 July 2026 | A population ratio is read from MD runs. | The return count from OP4, used as a gate on OP3.<br>*Must hold:* Runs cross between the states in both directions, more than once. | Without returns, residence and one-way events only. Stop: `POPULATION_NOT_ESTIMABLE` | In use. 0 of 40 HSP90 runs return, so no population is stated.<br>`data/operators/results/OP4.json` |
| **S-03**<br>Grossfield et al. 2019; project criterion of 28 July 2026 | A run is called converged or equilibrated. | None yet (for example, per-residue fluctuations tested separately from domain states).<br>*Must hold:* The observable and the state definition are named, and convergence is tested for each. | A run can be converged for local fluctuations and not for domain states. Stop: `CONVERGENCE_OBSERVABLE_UNSPECIFIED` | Not implemented. |
| **S-04**<br>Prinz et al. 2011 | A rate or time scale is read from MD. | None.<br>*Must hold:* A validated kinetic model: implied time scales stable with lag time, a Chapman–Kolmogorov test, and enough transitions. | Otherwise event counts and times only. Stop: `RATE_NOT_ESTIMABLE` | Not implemented; no case reports a rate. |
| **C006-RULE-002**<br>Shevchuk and Hub 2017 | Weights from reweighting or refinement are read as populations. | Claim limit on the nanodisc weights and on OP3. | Weights depend on the candidates, the prior and the error model; they are not thermodynamic populations. Stop: `PRIOR_DOMINANCE_OR_MISSING_STATE` | In use as a claim limit.<br>`data/nanodisc/` |
| **C010-RULE-001**<br>Sanabria et al. 2020 | A transient or minor state is claimed. | Structure of the HSP90 trust table: existence (OP1, OP2), population (OP3) and time scale (OP4) are separate rows. | Existence, population, time scale and function are separate claims. Stop: `CLAIM_LEVEL_UNSUPPORTED` | In use in the trust table.<br>`data/operators/D1_TABLE_HSP90.md` |

## Is a state reached, or only approached?

| Rule | Applies when | Acts through | What may be claimed | Status |
|---|---|---|---|---|
| **P-01**<br>This project, HSP90 NOE crosswalk, 10 September 2026 | A direction is called from the difference between two reference readouts. | OP2 NOE reference crosswalk.<br>*Must hold:* The absolute readout for a state is checked before a run is called near that state. | A sustained open direction is a direction. Agreement needs the open-state violation within tolerance. Stop: `RELATIVE_ONLY` | Operator in use. Control passed: 18 of 20 open-start runs agree at 1 Å.<br>`data/operators/results/OP2.json; data/hsp90/noe_crosswalk_per_trajectory.tsv` |
| **P-05**<br>This project, OP6 result, 11 September 2026; the general lesson is C005-RULE-001 | A neighbourhood around a reference ensemble is defined. | OP5 excursions and OP6 reference neighbourhoods.<br>*Must hold:* The radius is measured in the same quantity as the frame distance, and it passes a positive control (open-start runs mostly inside the open neighbourhood) and a negative control. | None until both controls pass. Stop: `REFERENCE_DEFINITION_FAILED_CONTROL` | Not met. OP5 and OP6 are withdrawn.<br>`data/operators/results/OP6.json` |
| **C006-RULE-003**<br>Shevchuk and Hub 2017 | A refinement or reweighting works over a fixed set of candidate structures, or a frame lies outside every reference. | Claim limit on the nanodisc result and on OP5. | Refinement cannot create a state absent from the candidates; a frame outside the references is not a new state. Stop: `MISSING_STATE_SUPPORT` | In use as a claim limit. |
| **C010-RULE-003**<br>Sanabria et al. 2020 | A residual suggests a state that no reference contains. | Claim limit on OP5. | A residual that points to an unknown state does not give that state's structure. Stop: `FUNCTIONAL_LINK_UNSUPPORTED` | Claim limit; OP5 is withdrawn. |

## Are two readouts the same quantity, and is the input the one reported?

| Rule | Applies when | Acts through | What may be claimed | Status |
|---|---|---|---|---|
| **C005-RULE-001**<br>Fuertes et al. 2017 | Two observables with different spatial support or averaging are compared, for example a SAXS radius of gyration and a dye distance. | Should have been applied to our own OP5 and OP6 definition (see P-05). | Not one direct numerical comparison. Stop: `ESTIMAND_OR_SUPPORT_MISMATCH` | Lesson not applied on 11 September; basis of P-05. |
| **C007-RULE-001**<br>Bengtsen et al. 2020 | NMR, SAXS, SANS and MD results are combined. | Nanodisc results reported per observable; OP2 keeps the NOE readouts separate from the geometric direction. | No single merged metric. Stop: `SOURCE_SEMANTICS_MERGED` | In use.<br>`data/nanodisc/per_observable.csv` |
| **C012-RULE-001**<br>Wankowicz and Bonomi 2026 | Any comparison is set up. | Framing template at workflow step 3: question, observable, forward model, uncertainty. | The comparison unit is condition, claim, observable, forward model and uncertainty. Stop: `BENCHMARK_SCOPE_UNDEFINED` | In use in framing. |
| **P-02**<br>This project, HSP90 NOE crosswalk, 10 September 2026 | The authors' NOE violation files are read. | OP2 input check.<br>*Must hold:* The native violation (second data column) is used; the pseudo-distance (third column) is a different quantity. | Stop: `COLUMN_SEMANTICS_UNVERIFIED` | In use.<br>`data/operators/results/OP2.json` |
| **P-03**<br>This project, DHFR and ADK, 10 September 2026 | Distances are computed from periodic MD coordinates. | Admission check before a data package is frozen; ADK distance operators.<br>*Must hold:* Protein–ligand distances use the nearest periodic copy; distances inside one protein use the whole molecule; an independent tool reproduces them. | Stop: `PERIODIC_GEOMETRY_UNVERIFIED` | In use. VMD and GROMACS agree within 1e-5 Å and 0.005 Å.<br>`data/dhfr/vmd_crosscheck.json; data/adk/window_changes_recomputed.json` |

## Does a fit to one observable support another?

| Rule | Applies when | Acts through | What may be claimed | Status |
|---|---|---|---|---|
| **C005-RULE-002**<br>Fuertes et al. 2017 | Two data types disagree. | Nanodisc: SAXS-only fit with the NOEs held out (analysis script of 9 September, not packaged as an operator). | A reproducible discrepancy is reported as evidence; it is not averaged away. Stop: `BRIDGE_UNAVAILABLE` | Used in the nanodisc interpretation.<br>`data/nanodisc/fit_summary.csv` |
| **C006-RULE-001**<br>Shevchuk and Hub 2017 | An ensemble is refined or reweighted against SAXS. | Nanodisc SAXS reweighting (analysis script).<br>*Must hold:* Explicit forward model, prior, error model and uncertainty. | State weights depend on those choices. Stop: `POSTERIOR_AMBIGUITY` | Used in the nanodisc analysis.<br>`data/nanodisc/` |
| **C007-RULE-002**<br>Bengtsen et al. 2020 | Maximum-entropy reweighting is used. | Nanodisc SAXS reweighting (analysis script). | Reweighting limits departure from the MD prior; it does not discover states or give kinetics. Stop: `INTEGRATION_OPERATOR_UNVERIFIED` | Used in the nanodisc analysis. On 10 September it was retrieved as a method card for the HSP90 NOE question, which involves no reweighting.<br>`data/nanodisc/` |
| **C007-RULE-003**<br>Bengtsen et al. 2020 | Support is claimed from combined data. | Nanodisc design: fit SAXS, then test the held-out NOEs.<br>*Must hold:* Source independence, matched conditions, forward calculations and held-out validation are stated. | Agreement across sources is not stronger evidence by default. Stop: `SHARED_ERROR_OR_CONDITION_MISMATCH` | The nanodisc test follows this rule.<br>`data/nanodisc/comparisons.csv` |
| **C012-RULE-002**<br>Wankowicz and Bonomi 2026 | A fit to several data types is presented as the ensemble. | Claim limit on the nanodisc result. | A compatible ensemble is not the unique ensemble. Stop: `NON_IDENTIFIABILITY_OR_MISSING_SUPPORT` | In use as a claim limit. |

## What may the answer claim, and can each number be traced?

| Rule | Applies when | Acts through | What may be claimed | Status |
|---|---|---|---|---|
| **C012-RULE-003**<br>Wankowicz and Bonomi 2026 | Results are reported. | Report format: trust table with allowed and forbidden wording, uncertainty and next step. | Stop: `GROUND_TRUTH_OR_VALIDATION_MISSING` | In use in the report format.<br>`data/operators/D1_TABLE_HSP90.md` |
| **P-04**<br>This project, errors in the first HSP90 round and in a DHFR answer, 10 September 2026 | An answer states a calculated number. | Answer check.<br>*Must hold:* Each number carries the operator result it came from and matches it. | An unbound number is reported as unverified. Stop: `UNBOUND_NUMBER` | In use. On 8 earlier answers it caught 6 of 7 numerical errors, with no false alarm on 7 correct statements; the old check caught none.<br>`data/operators/binding_replay_result.json` |

## Rules with no case in this project

These 20 rules concern smFRET, cryo-EM or DEER data. None of the four cases has such data, so none of them governs an analysis here. They stay in the table for comparisons across experiments.

| Rule | Paper | What the paper showed | Status |
|---|---|---|---|
| **C001-RULE-001** | Hellenkamp et al. 2018 | Raw and corrected FRET efficiency, FRET-averaged distance and mean-position distance are different estimands. | No case: no smFRET data. |
| **C001-RULE-002** | Hellenkamp et al. 2018 | FRET distance uncertainty must include correction, R0, dye motion and model assumptions, not only histogram spread. | No case: no smFRET data. Applied by mistake to the HSP90 NMR question on 10 September. |
| **C001-RULE-003** | Hellenkamp et al. 2018 | A DNA benchmark shows reproducibility under its setup, not protein-distance accuracy. | No case: no smFRET data. |
| **C002-RULE-001** | Agam et al. 2023 | A protein smFRET comparison keeps the corrected observable, condition and label context; a bare structural distance is not equivalent. | No case: no smFRET data. |
| **C002-RULE-002** | Agam et al. 2023 | Comparing structures with smFRET needs an explicit dye and linker forward model. | No case: no smFRET data. |
| **C002-RULE-003** | Agam et al. 2023 | A dynamic shift in BVA or E–τ plots needs photophysical and probe explanations ruled out first. | No case: no smFRET data. |
| **C003-RULE-001** | Dimura et al. 2020 | FRET-guided modelling needs a candidate ensemble, a probe-aware forward model, informative pairs and independent validation pairs. | No case: no FRET data. |
| **C003-RULE-002** | Dimura et al. 2020 | A good FRET fit cannot repair a fold or state missing from the candidates. | No case: no FRET data. Applied by mistake to the HSP90 NMR question on 10 September (its RMP restraint was treated as required). |
| **C003-RULE-003** | Dimura et al. 2020 | Model uncertainty, reference-structure accuracy and agreement with FRET are separate quantities. | No case: no FRET data. |
| **C005-RULE-003** | Fuertes et al. 2017 | Polymer models used to invert mean FRET values need system-specific scrutiny. | No case: no FRET data. |
| **C008-RULE-001** | Hoff et al. 2024 | Cryo-EM voxel evidence needs correlation-aware sampling, half-map and noise provenance, and a forward model. | No case: no cryo-EM data. |
| **C008-RULE-002** | Hoff et al. 2024 | Fuzzy density must be separated into conformational heterogeneity and noise or B-factor effects. | No case: no cryo-EM data. |
| **C008-RULE-003** | Hoff et al. 2024 | A map-consistent ensemble may describe local dynamics around one macrostate, not the full landscape. | No case: no cryo-EM data. |
| **C009-RULE-001** | Peter et al. 2022 | DEER and smFRET distances keep probe chemistry, sample state, averaging and condition; the nominal distance is not one observable. | No case: no DEER or smFRET data. |
| **C009-RULE-002** | Peter et al. 2022 | Probe–protein interactions and cryoprotectants can explain differences between methods. | No case: no DEER or smFRET data. |
| **C009-RULE-003** | Peter et al. 2022 | Agreement across the tested datasets supports complementary use under the stated protocols only. | No case: no DEER or smFRET data. |
| **C010-RULE-002** | Sanabria et al. 2020 | Global shared-fraction analysis improves identifiability but stays model- and condition-dependent. | No case: no FRET data. |
| **C011-RULE-001** | Steffen et al. 2021 | Predicting FRET from a trajectory needs dye, linker, trajectory and photon-statistics metadata. | No case: no FRET data. |
| **C011-RULE-002** | Steffen et al. 2021 | Predicted FRET width mixes conformational sampling and shot noise, which must be separated. | No case: no FRET data. |
| **C011-RULE-003** | Steffen et al. 2021 | A DNA demonstration shows an implementation path, not protein-specific accuracy. | No case: no FRET data. |

## Sources added in version 2

- Grossfield A. et al. (2019) Best Practices for Quantification of Uncertainty and Sampling Quality in Molecular Simulations [Article v1.0]. *Living Journal of Computational Molecular Science* 1, 5067. [doi:10.33011/livecoms.1.1.5067](https://doi.org/10.33011/livecoms.1.1.5067)
- Prinz J.-H. et al. (2011) Markov models of molecular kinetics: generation and validation. *Journal of Chemical Physics*. [doi:10.1063/1.3565032](https://doi.org/10.1063/1.3565032)
- Henot F. et al. (2022), for the statement that the HSP90 runs are not ergodic. [doi:10.1038/s41467-022-35399-8](https://doi.org/10.1038/s41467-022-35399-8)
- The project criterion of 28 July 2026: a population ratio from MD needs repeated crossings between the states.

The sources of the 33 original rules are listed in [SOURCES.md](../../SOURCES.md).
