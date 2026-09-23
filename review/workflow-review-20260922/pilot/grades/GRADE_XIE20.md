# GRADE_XIE20 — blind grade of E1–E4

**Paper:** Xie, Saleh, Rossi, Kalodimos, Science 2020;370:eabc2754 (Abl kinase domain).
**Graded against:** `_sealed_reference/REF_XIE20.md` (errata applied) and `task_common.md`.
**Paper check:** I read the PMC main text (PMC7920495) to settle disagreements between entries and the reference; those lines are marked *(paper checked)*. The Europe PMC full-text endpoint returned HTTP 500. The supplementary PDF was not opened.

**Scale.** 2 = right, 1 = partly right, 0 = wrong or missing. The paper has information for all nine items, so none is NA. Content is credited wherever it appears in an entry. Each unsupported statement is counted once: as an over-claim (a claim about mechanism, function or evidence that the paper does not support) or as a factual error (a wrong number, ID, construct or condition). An error lowers an item when it displaces a must-get-right fact, or, for item 7, when it breaks "wording matched to the evidence". Item 3 is scored on the must-get-right exchange facts (CEST probe counts, linear model, kex values with kex1 fixed from H415P, populations); the Δϖ range and the flip barrier are covered in the notes. Hedge drops, mislabels and locator slips are listed as "noted" and not counted.

| Entry | 1 Apo + ligand | 2 States | 3 Exchange | 4 Residues | 5 Identity | 6 Structures / sims | 7 Function | 8 Evidence / provenance | 9 Tier | Over-claims | Factual errors | Total | Scored items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 | 1 | 1 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 1 | 0 | 15 | 9 |
| E2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 | 2 | 2 | 3 | 0 | 17 | 9 |
| E3 | 1 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 2 | 3 | 1 | 13 | 9 |
| E4 | 2 | 2 | 2 | 1 | 2 | 2 | 1 | 2 | 2 | 0 | 0 | 16 | 9 |

Totals are out of 18. Over-claims and factual errors are separate counts and are not subtracted from the total.

```json
{"E1": {"items": [1, 1, 2, 2, 1, 2, 2, 2, 2], "over_claims": 1, "factual_errors": 0}, "E2": {"items": [2, 2, 2, 2, 2, 2, 1, 2, 2], "over_claims": 3, "factual_errors": 0}, "E3": {"items": [1, 2, 1, 2, 1, 2, 1, 1, 2], "over_claims": 3, "factual_errors": 1}, "E4": {"items": [2, 2, 2, 1, 2, 2, 1, 2, 2], "over_claims": 0, "factual_errors": 0}}
```

## Deductions

### E1
- **Item 1 (1).** The apo field lists imatinib, dasatinib and PD173955 as equals. It does not identify imatinib (I2) and PD173955 (I1) as the ligands that define apo, and dasatinib binds the major, active state.
- **Item 2 (1).** Says I2's "exact DFG rotamer [is] not stated", but the paper says E2's DFG "adopts the 'out' conformation", with Phe401 translated ~11 Å (Results, Fig. 2C) *(paper checked)*. It also calls I1 "otherwise close to G", missing the 180° flip of Leu403–Met407.
- **Item 5 (1).** Says the CEST shifts match the PD173955- and imatinib-bound "crystal structure". The paper correlates CEST Δϖ with NMR shift changes of the inhibitor complexes (Fig. 1E,F) *(paper checked)*. It omits the 6 Å exclusion, the αC outliers that separate I2 from the imatinib complex, and the agreement of the mutant shifts with CEST.
- **Over-claim 1 (reference D4).** "Global CEST fitting favored sequential G↔I1↔I2 over two branched models (χ²=1.15 vs 1.29/1.41)". Those χ² values come from unconstrained fits whose excited-state populations (about 10% and above) the authors judged inconsistent with the CEST profiles and set aside. In the fit that produced the reported rates (kex1 fixed at 46.8 s⁻¹), model 1 and the star model scored 1.42 vs 1.41; model 1 was kept for its agreement with H415P. Model 3 is linear through E2, not branched (Methods "CEST data fitting") *(paper checked)*.
- *Noted, not counted:* "(I1 only)" for the 40 one-dip probes (the Fig. 1B legend says only "one" excited state). "Explaining its potency" drops the paper's "could explain". Comparator PDB IDs are called "not stated", though 1IEP is in the Fig. 2D legend. "Spine energetics Fig. 2" should be Fig. 4C.

### E2
- **Item 7 (1).** The function field carries the three over-claims below. It also leaves out the spine/DFG inactivation data (M309L/L320I at 82% I2; F401V at >95% I2 with ≥20-fold lower activity).
- **Over-claim 1 (D2).** "Conformational selection, not induced fit". The paper says imatinib "apparently binds selectively" to I2, which differs from the complex in the αC helix and P-loop, and that imatinib "expends energy to elicit the structural changes required for its binding" (Results) *(paper checked)*.
- **Over-claim 2 (D6).** Says seven resistance mutations, including G269E, Q271H and T231R, "deplete pI2, matching ITC-measured affinity loss". The main text calls G269E and Q271H "more complex" (fig. S10B,C). G269E raises I2 from ~85% to 90% when added to M309L/T408Y (Methods "Structure determination"). T231R acts through SH2–N-lobe docking in AblFKΔSH3-I2M, with no ITC reported *(paper checked)*.
- **Over-claim 3.** Says T334I and pY412 are "each activating the kinase per CrkII-phosphorylation assays". The main text reports CrkII assays (fig. S11) only for M309L/L320I and F401V; T334I and pY412 are shown by NMR populations only (Fig. 4C,D,F) *(paper checked; fig. S11 not opened)*.
- *Noted, not counted:* the Leu406 label "(I2 vs. imatinib)" is loose. "Full data are presumably in the supplement" is wrong: the Δϖ values are plotted in main Fig. 1E,F.

### E3
- **Item 1 (1).** Lists seven inhibitors with no ranking, including the active-state binders dasatinib and axitinib. Imatinib (I2) and PD173955 (I1) are not named as the ligands that define apo.
- **Item 3 (1).** The rates are not linked to the kex1 value (46.8 s⁻¹) fixed from the H415P two-state fit. The model-1 χ² (1.15) paired with them comes from the rejected unconstrained fit, which gave kex1 12.3 and kex2 145.5 s⁻¹ with pE1 10.6% *(paper checked)*.
- **Item 5 (1).** Never says that I2 matches the imatinib complex only in the A-loop and DFG (αC outliers in Fig. 1F; αC and P-loop differences in Fig. 2D). It presents the comparison with 1IEP as confirming I2's identity.
- **Item 7 (1).** Carries over-claims 2 and 3 below, and gives no activity numbers for the spine/DFG variants (82% I2; F401V ≥20-fold).
- **Item 8 (1).** Gives no 40/43 split and states a wrong count of exchanging probes (factual error 1).
- **Over-claim 1 (D4).** "Three sequential exchange topologies were compared by χ²red (model 1 … =1.15 vs. 1.29 and 1.41)". As in E1, these are the rejected fits; with kex1 fixed, model 1 and the star model could not be separated (1.42 vs 1.41). Model 2 is branched, not sequential *(paper checked)*.
- **Over-claim 2 (D6).** Says G269E and Q271H "deplete I2, matching ITC-measured affinity losses". The paper calls them "more complex", and G269E raises I2 in I2M *(paper checked)*.
- **Over-claim 3.** "Gatekeeper T334I … change CrkII-phosphorylation activity": no CrkII assay is reported for T334I *(paper checked; fig. S11 not opened)*.
- **Factual error 1.** "87 show exchange" (§7, §9). The paper reports 40 one-dip + 43 two-dip = 83 of 104 probes (Results, Fig. 1B) *(paper checked)*.
- *Noted, not counted:* the Leu406 values labelled "I2−G" are the shift changes on imatinib binding. The ~36 kcal/mol is called an enthalpy and attributed to "Results" (the Results call it an activation energy), and the H415P construct is not given. "The authors ... cannot fully exclude" is marked [paper], but the authors do not say it.

### E4
- **Item 4 (1).** The field gives only where the exchanging probes concentrate (A-loop, αC). Elsewhere the entry names the differing elements only as state descriptors (§6). It gives no residue-level differences (Glu305–Lys290 ion pair, Tyr272 shift, Phe401 translation, Tyr412) and no regulatory-spine region.
- **Item 7 (1).** Leaves out the autoinhibition result, a must-get-right item: SH3-SH2 raises I2 from 6% to 34% in AblFK and GNF5 raises it to 95%, making I2 the autoinhibited state (Fig. 5A,B).
- *Noted, not counted:* the verdict calls both excited-state structures "de novo", but the I1 structure borrowed Abl–PD173955 restraints for unchanged regions (Methods "Structure determination"). "In one buffer" overlooks the pH series and the separate ITC and kinase-assay buffers.

## Notes

- **Ranking.** E4 is the most accurate entry: no over-claims or factual errors, with points lost only for thin residue coverage and the missing autoinhibition result. E2 covers the most but makes three over-claims, two of them on the reference list (D2, D6). E1 gets function right but misses facts the paper states and repeats the rejected-fit χ² argument. E3 scores lowest: three over-claims, a wrong probe count, and partial apo, exchange and identity fields.
- **Gaps shared by all four entries.** None gives a Δϖ range: the reference reads about −1.4 to +1.5 ppm for E1 and −2.8 to +2.0 ppm for E2 from Fig. 1E,F. All four quote Leu406 instead (−2.8/+2.1 ppm), which the text reports as the shift change on imatinib binding. None mentions the borrowed PD173955 restraints in the I1 structure.
- **Over-claims no entry makes.** None claims wild-type excited-state structures, cellular or Bcr-Abl populations, kinome generality, or a function for I1. None calls ~36 kcal/mol a free-energy barrier, and all four keep isoform 1b numbering.
- **Flip barrier.** E2 scopes the ~36 kcal/mol correctly (A↔I1, H415P). E3 gives it without the construct. E1 and E4 omit it.
- **What the paper check changed.** The reference cites only the fixed-kex1 χ² (1.42 vs 1.41). The 1.15/1.29/1.41 values that E1 and E3 quote are real, but they come from the unconstrained fits the authors discarded. Also found in the main text: the ~20–500 s⁻¹ CEST window (E3, E4), I2M at 85–90% (E2), pY412 "~3.0 kcal/mol" and "eliminates both I1 and I2" (E1), and the I1 "by-product of the evolutionary process" remark (E1).
