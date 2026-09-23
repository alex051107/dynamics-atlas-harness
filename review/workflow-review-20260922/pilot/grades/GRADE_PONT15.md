# PONT15 grading: E1–E4

Graded against REF_PONT15 (errata applied: one locator fix) and task_common.md. Scale: 0 wrong or missing, 1 partly right, 2 right. The paper has information for all nine items, so none is NA.

| Entry | 1 Apo + ligand | 2 States | 3 Exchange | 4 Residues | 5 Identity | 6 Structures/sims | 7 Function | 8 Evidence/provenance | 9 Tier | Over-claims | Factual errors | Total | Scored items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 | 2 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 17 | 9 |
| E2 | 2 | 1 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 1 | 0 | 15 | 9 |
| E3 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 3 | 0 | 13 | 9 |
| E4 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 16 | 9 |

```json
{"E1": {"items": [2, 2, 2, 1, 2, 2, 2, 2, 2], "over_claims": 0, "factual_errors": 0}, "E2": {"items": [2, 1, 2, 1, 1, 2, 2, 2, 2], "over_claims": 1, "factual_errors": 0}, "E3": {"items": [2, 2, 1, 2, 1, 2, 1, 1, 1], "over_claims": 3, "factual_errors": 0}, "E4": {"items": [2, 2, 1, 1, 2, 2, 2, 2, 2], "over_claims": 2, "factual_errors": 0}}
```

## Deductions

**E1**
- Item 4 = 1: E1 says F99, like Y94 and Q96, moves relative to helices α3/α5 ("reposition vs. helix α3/α5"). That is the old-model picture. The new structures put F99 in the same position in both states (Results, NMR section, F99 paragraph; Supplementary Fig. 5B), and F99 orientation does not separate the MSM macrostates (Results, homogeneous-versus-heterogeneous section; Fig. 2).

**E2**
- Item 2 = 1: The major state's only population is the MSM ≈48%. E2 pairs it with I by sentence order and flags that as inference. A "dominant" I is therefore given a figure below 50%, the ≈85% that follows from the cited 15% never appears, and A is tagged ≈52%.
- Item 4 = 1: E2 counts F99 among the side chains that differ between states. The new structures contradict this (see E1).
- Item 5 = 1: The identity basis is the 2MSK–model match plus an overstated helicity point. The Y94–α3 versus Q96–α3 NOE switch appears only in fields 7–8, not as identity evidence. The kinetic reason for calling the MSM states A and I (≈100 μs, comparable to the NMR rate) is missing.
- Over-claim: E2 says the higher terminal helicity is "attributed by the authors to ~15% admixture". The paper says only that the excess "might be partially due to" the 15% A, and offers inaccurate MSM sub-state populations as the other explanation. E2 drops the hedge and uses the point as identity evidence.

**E3**
- Item 3 = 1: E3 gives "I≈52%, A≈48% [paper, Fig. 2]", but the paper reports the two macrostate populations without saying which is A. The ≈100 μs slow process is also missing.
- Item 5 = 1: E3 omits the paper's main identity links. These are the BeF₃⁻ structure matching the simulated active state (which E3 downgrades to [inference]), the Y94/Q96–α3 NOE switch and the kinetic basis. The agreement between the two MSMs that E3 cites shows the simulations are robust; it does not identify the minor state.
- Item 7 = 1: E3 calls the cited, established link (D54 phosphorylation stabilizes A; Introduction, refs 13 and 15) a Discussion proposal, "proposed, not tested". It also names partners the paper never mentions (RNA polymerase, σ54, oligomerization) and drops the transcription link and the ref-13 H-bond mutants.
- Item 8 = 1: E3 says the cited kinetics come from "relaxation-dispersion-type literature". The paper calls that evidence only earlier NMR dynamics data, with exchange broadening at 25 °C.
- Item 9 = 1: The weak label names the right gap (numbers cited from refs 11–13). It also adds "functional relevance is proposed, not tested", which misreads the cited functional link. The reference accepts weak only when that first gap alone is the reason.
- Over-claim: E3 labels the MSM split A≈48%, I≈52% as [paper] (fields 6, 8 and 14). The paper makes no such assignment (reference over-claim list, item 2).
- Over-claim: E3 writes "new NMR data show Y101 adopts multiple orientations independent of T82". This is an MSM result (Supplementary Fig. 3A,B) that agrees with experiments in ref 25. This paper's NMR does not address Y101 or T82.
- Over-claim: "relaxation-dispersion-type" names an exchange method the paper never states. It is a general-knowledge fill, and it makes the cited evidence look stronger.

**E4**
- Item 3 = 1: E4 states "MSM macrostate population ~48% for A … [paper, Results]". The paper makes no A/I assignment.
- Item 4 = 1: E4 states "Y94, Q96, F99, Y101 switch packing against helices α3/α5". F99 does not switch (see E1).
- Over-claim: the A ≈48% assignment (reference over-claim list, item 2).
- Over-claim: E4 says "heterogeneity persists across force fields" and repeats it in field 11 ("all sample … inactive-state heterogeneity"). The paper traces the larger I heterogeneity to the force field (CHARMM27 vs Amber99SB). The Anton runs that reproduce it use the same CHARMM27 force field (Results, MSM-comparison section).

No entry has a factual error in numbers, IDs or conditions. Checked against the paper or the reference: Table 1 counts, spectrometers, pH, the cited 13,000 s⁻¹ and 15%, 2,168 microstates, 8,000 runs and 978 μs, the Anton lengths, and the PDB, BMRB, DOI, PMCID and PMID identifiers.

## Notes

- **Paper opened.** I read the PMC4470301 main text in a separate browser tab because the Europe PMC XML endpoint returned HTTP 500. I did not open the supplementary PDF. The paper settled five disagreements:
  - The 52%/48% macrostates carry no A/I label. Only sentence order pairs 52% with A, which E2 flags as inference; E3 and E4 assign the reverse.
  - The authors' caution covers the slow-rate estimate and the I sub-state populations, not the 52/48 split. E1, E2 and E4 attach it to the split; this is not counted.
  - Single unbiased Folding@home runs started mid-string do complete I↔A transitions (Fig. 3D,E), so E1's and E2's statements stand. The Anton runs show none.
  - Table 1 gives 2,428 NOEs and 173 dihedral restraints for the apo structure, so E1 is correct. The Methods text gives different counts.
  - The paper also ties the larger I heterogeneity to string-seeded starting points, so E3's seeding remark stands.
- **Tier.** E1 and E2 take the reference's acceptable weak route and name the gap exactly. E4 matches the reference's strong verdict; it flags the cited numbers in fields 7, 8 and 14 rather than in the verdict line.
- **F99.** E3 is the only entry that says F99 does not move. Its missing Y94/Q96–α3 contact switch is charged under item 5, not item 4.
- **Shared omissions, not deducted.** No entry says the cited exchange data are from 25 °C. No entry says 2MSL averages over a sample that is ~15% A; E4 comes closest.
- **Not verified, not counted.** E1's UniProt P41789 (via BMRB), E3's strain and E4's locus tag come from database fields I did not open.
- **Rule slips, not scored.** E1 field 10 and E3 field 15 contain process notes. E4 attributes the BMRB IDs to the paper's accession codes, which list only PDB IDs.
