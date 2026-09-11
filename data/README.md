# Data guide

Every number in [README.md](../README.md), [RESULTS.md](../RESULTS.md) and the slides comes from a file in this folder. This page says what each file contains, what its columns mean, where it came from, and how to check the numbers quoted in the text.

| Folder | What it supports |
|---|---|
| [`hsp90/`](hsp90/) | Direction of change and agreement with the NOE references, 40 trajectories |
| [`nanodisc/`](nanodisc/) | SAXS-only reweighting and its effect on NOE agreement |
| [`dhfr/`](dhfr/) | Protein–ligand distances after the periodic-image correction |
| [`adk/`](adk/) | Domain distances along the two deposited trajectories |
| [`rules/`](rules/) | The 33 candidate rules |
| [`rules_test/`](rules_test/) | Scores for every answer in the tests of the rules |
| [`operators/`](operators/) | The 11 September operator round: cards, fixed results, the HSP90 trust table, the number-check replay and scores |

All distances are in ångström (Å). Times are in nanoseconds (ns). The primary data are the authors' depositions listed in [SOURCES.md](../SOURCES.md); the files here are our derived tables and results.

---

## hsp90/

Source: trajectories and NOE violation series deposited with Henot et al. 2022. 40 trajectories, 20 started from the open crystal structure and 20 from a closed model; window 20 to 1020 ns, 1001 saved points each.

### `direction_event_counts.csv`

Counts of sustained directions for each start and each persistence threshold. A direction is "sustained" when the sign of the two difference readouts stays the same for at least the threshold number of consecutive saved points.

| Column | Meaning |
|---|---|
| `persistence_threshold_points` | 5, 20 or 50 consecutive saved points |
| `start` | `closed_start` or `open_start` |
| `n_trajectories` | 20 |
| `first_sustained_direction_open` / `_closed` | runs whose first sustained segment points toward open / toward closed |
| `no_sustained_direction` | runs with no sustained segment at this threshold |
| `departures_from_first_direction` | runs that later hold the opposite sustained direction |
| `returns` | runs that go back after departing |

At 5 points, closed start: 5 first open + 5 departures (closed then open) = 10 of 20 runs with a sustained open direction. Departures fall to 4 and 1 at 20 and 50 points.

### `noe_crosswalk_per_trajectory.tsv`

One row per trajectory.

| Column | Meaning |
|---|---|
| `trajectory` | trajectory name as deposited (the `ES` number is used in the text) |
| `seed_lineage` | `closed_seeded` or `open_seeded` |
| `partition_5`, `partition_50` | `FIRST_OPEN`, `CLOSED_THEN_OPEN` or `ONLY_CLOSED` at 5 and 50 points |
| `open_direction_fraction` | fraction of saved points in the open direction |
| `judgment` | classification at 1 Å: `AGREEMENT`, `PARTIAL`, `RELATIVE_ONLY`; `NOT_APPLICABLE` for runs with no open direction |
| `first_reference_entry_ns` | time the run first stays within the control band (95th percentile of open-start values, 1.32 Å) for 50 points |
| `first100_Vopen_mean`, `last100_Vopen_mean` | mean violation of the open-state NOE references over the first / last 100 points (Å) |
| `first100_Vclosed_mean`, `last100_Vclosed_mean` | the same for the closed-state references |
| `OPEN_NOE_fraction`, `CLOSED_NOE_fraction`, `BOTH_FAR_fraction`, `BOTH_NEAR_fraction` | fraction of all points within 1 Å of the open reference only, the closed reference only, neither, or both |
| `within_direction_*` | the same four fractions, counted only over open-direction points |

`RELATIVE_ONLY` means at least half of a run's open-direction points are far from both references. Check: 9 closed-start rows have `judgment = RELATIVE_ONLY`, 1 has `PARTIAL` (ES04); 18 open-start rows have `AGREEMENT`. The ES15 change quoted in the text is `first100_Vopen_mean` 9.07 → `last100_Vopen_mean` 1.12.

### `noe_crosswalk_summary.json`

Group counts at tolerances 0.5, 1 and 2 Å (`sensitivity`), and the control-band value `p95_open_A` = 1.32.

---

## nanodisc/

Source: ensemble, experimental data and published weights of Bengtsen et al. 2020. 1195 MD frames; 90 SAXS points; 292 amide and 40 methyl NOE upper bounds.

### `fit_summary.csv`

One row per weighting scheme and data type.

| Column | Meaning |
|---|---|
| `scheme` | `uniform` = before any fit; `saxs_theta6` = fitted to SAXS only (main setting); `saxs_theta60` = SAXS only, stronger regularization; `local_joint_v2` = fitted to all data; `author_joint` = the authors' published weights |
| `channel` | `saxs`, `amide` (NOE), `methyl` (NOE) |
| `n` | number of SAXS points or NOE restraints |
| `fixed_mean_loss` | mean disagreement between prediction and data; this is the number quoted in the text |
| `raw_upper_violations` | number of NOE upper bounds exceeded |
| `max_abs_standardized_residual` | largest single disagreement, in units of the experimental error |
| `relative_entropy`, `entropy_effective_fraction`, `max_weight` | how far the weights moved from uniform |

The text compares `uniform` with `saxs_theta6`: SAXS 10.02 → 1.17, amide 0.933 → 0.965, methyl 3.89 → 4.47. With stronger regularization (`saxs_theta60`) the NOE values also do not improve (0.971 and 3.93).

### Other files

- `per_observable.csv`: prediction and data for every SAXS point and NOE restraint under each scheme.
- `comparisons.csv`: for each scheme, how many restraints improved or worsened relative to `uniform`.
- `weights_before_fit.csv`, `weights_after_saxs_fit.csv`: weight of each of the 1195 frames.

---

## dhfr/

Source: trajectories deposited with Cetin et al. 2023 (Zenodo 7966540), one per condition: wild type and L28R, each with TMP and with 4′-DTMP. Frames 11 to 1000 (990 frames). Distances use the nearest periodic copy of the ligand.

### `ligand_distance_comparison.csv`

| Column | Meaning |
|---|---|
| `variant` | `WT` or `L28R` |
| `protein_atom_to_ligand_atom` | e.g. `r20_N_O3P` = backbone N of residue 20 (Met20) to ligand atom O3P |
| `mean_distance_TMP_A`, `mean_distance_4DTMP_A` | mean over 990 frames |
| `change_4DTMP_minus_TMP_A` | negative = closer with 4′-DTMP |

The text quotes `r20_N_O3P`: WT 8.69 → 4.62 Å, L28R 10.44 → 4.81 Å.

### Other files

- `distance_statistics_per_condition.tsv`: mean, standard deviation, minimum and maximum for each condition and atom pair. `system` codes: `tmpp-wt` = TMP, wild type; `d4tmpp-wt` = 4′-DTMP, wild type; `tmpp-l28r`, `d4tmpp-l28r` likewise.
- `vmd_crosscheck.json`: largest difference between our distances and an independent calculation with VMD, per condition (about 10⁻⁵ Å).

---

## adk/

Source: trajectories deposited with Orädd et al. 2021 (Zenodo 5583119). No ATP or AMP in the coordinates.

### `domain_distances_open_start.tsv`, `domain_distances_closed_start.tsv`

| Column | Meaning |
|---|---|
| `frame_index` | saved frame |
| `time_ns` | 0.2 ns between frames; 0–450.4 ns (open start), 0–335.4 ns (closed start) |
| `NMP_CORE_mean_CA_distance_A` | mean distance over all Cα pairs between NMP and CORE |
| `LID_CORE_mean_CA_distance_A` | the same for LID and CORE |

Domains: CORE residues 1–29, 68–115, 168–214; NMP 30–67; LID 118–160. Distances are measured inside the whole molecule, without folding pairs across the periodic box.

### `window_changes_recomputed.json`

Change between the first and last 10 % of frames, recomputed independently: open start LID +2.290, NMP +0.071 Å; closed start LID +1.176, NMP +1.091 Å.

---

## rules/

- [`RULES_TABLE.md`](rules/RULES_TABLE.md): the 33 rules in a readable table.
- `rule_registry_v0.1.csv`: the original table, 33 rows × 20 columns. The file uses commas even though earlier copies were named `.tsv`. Key columns: `paper_finding` (what the paper showed), `proposed_project_rule` and `required_fields` (what we ask to be checked), `abstain_route` (where to stop), `transfer_scope` (how far it carries).

---

## rules_test/

### `scores_per_answer.csv`

One row per answer: 74 answers across the four tests plus two plain runs.

| Column | Meaning |
|---|---|
| `test` | `question_framing`, `data_check_card`, `method_guidance`, `check_after_answer`, `plain_run` |
| `question` | which case question was asked |
| `condition` | the version of help given, e.g. `without_help`, `with_warning_card`, `full_rule_text`, `method_cards`, `split_question` |
| `repeat` | 1–4 |
| `core_parts_correct_of_5` | how many of the five parts a correct answer must contain were right |
| `core_errors` | wrong statements on those parts |
| `overclaims` | conclusions stronger than the data support |
| `answerable_parts_missed` | parts the data could answer that the answer left out |
| `input_defect_detected`, `conclusion_downgraded_for_defect` | for the defective DHFR input only |
| `sub_questions_covered_of_3` | for the framing test only |
| `cost_usd` | model cost of the answer |

The tables in the text are medians over the four repeats of each question and condition.

---

## operators/

The operator round of 11 September. Operator code, every AI run and the scoring sheets are on the branch `feature/operator-plan-review-20260911`; this folder keeps what is needed to check the numbers quoted in the text.

| File | What it holds |
|---|---|
| `cards/OP1.md` … `OP6.md` | one card per operator: purpose, inputs, allowed parameters, preconditions, output, claim limit |
| `results/*.json` | the fixed-pipeline result of each operator; `OP1_p5`, `_p20`, `_p50` are the three persistence thresholds; `OP3_state_core` uses the older state labels; two ADK results |
| `D1_TABLE_HSP90.md`, `.json` | the trust table as produced by the pipeline, one row per quantity, with the result ids behind it |
| `binding_replay_claims.csv` | the 14 statements from earlier AI answers used to test the number check: 7 known errors (`ERR-`) and 7 correct statements (`CTRL-`), each with the operator result and field it is compared against |
| `binding_replay_result.json` | the outcome: 6 errors flagged, 7 correct statements passed, 1 error (`ERR-12`) with no operator |
| `scores_by_group.csv` | rubric points per question and arm (`F` fixed pipeline, `D` free analysis, `O` operator-bound); six dimensions scored 0–2 per core unit |
| `runs_summary.csv` | one row per run: operators used, times sent back, unbound numbers, tool calls, cost |

How to check the quoted numbers:

- 5 / 4 / 1 reversals: `results/OP1_p5.json`, `_p20`, `_p50`, field `group_summary.closed_seeded.opposite_candidate`.
- 18 of 20 open-start runs agree at 1 Å: `results/OP2.json`, field `summary_by_tau["1"].trajectory_judgment_counts.open_seeded.AGREEMENT`; the same block gives the closed-start counts (1 `PARTIAL`, 9 `RELATIVE_ONLY`), and keys `"0.5"` and `"2"` give 7 and 19.
- 99.99 % of open-start frames outside both references: `results/OP6.json`, `group_summary.open_seeded.NONE` = 0.99985. The radii are in `results/OP5.json`, `parameters.r_open_A` = 1.354 and `r_closed_A` = 2.625.
- 58 % and 98 % (HSP90), 74 % and 100 % (ADK): column `percent` in `scores_by_group.csv`.
- 6 of 7: `binding_replay_result.json`, `checker.summary`.
