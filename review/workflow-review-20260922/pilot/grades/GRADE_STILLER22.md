# GRADE_STILLER22: blind grading of E1–E4 against REF_STILLER22

Scale: 2 = right, with the reference's must-get-right points and the sub-fields the task asks for all present; 1 = one of those missing or misstated; 0 = wrong or missing. No item is NA because the paper covers all nine.

| Entry | 1 Verdict + apo ligand | 2 States | 3 Exchange | 4 Regions | 5 Identity | 6 Mapping + simulations | 7 Function | 8 Evidence + provenance | 9 Tier | Over-claims | Factual errors | Total | Scored items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 2 | 2 | 1 | 0 | 14 | 9 |
| E2 | 2 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 1 | 16 | 9 |
| E3 | 2 | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 15 | 9 |
| E4 | 2 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 17 | 9 |

```json
{"E1": {"items": [2, 2, 1, 2, 1, 1, 1, 2, 2], "over_claims": 1, "factual_errors": 0}, "E2": {"items": [2, 1, 1, 2, 2, 2, 2, 2, 2], "over_claims": 0, "factual_errors": 1}, "E3": {"items": [2, 1, 1, 1, 2, 2, 2, 2, 2], "over_claims": 0, "factual_errors": 0}, "E4": {"items": [2, 2, 1, 2, 2, 2, 2, 2, 2], "over_claims": 0, "factual_errors": 0}}
```

## Deductions

**E1**
- Item 3: says the Δδ range is "not stated". The paper plots per-residue Δδ (Fig. 1f,g) and gives a 0.05 ppm mean diamagnetic Δδ (Methods); the reference reads ≈0–0.3 ppm.
- Item 5: gives the de novo PCS basis but no evidence that the structure is right (12 benchmark states with 90 ± 8% correct PCS; 93 restraints at Q = 3.7%).
- Item 6: says no molecular-dynamics simulation of the transition is reported, and leaves out the cited metadynamics study (ref. 43), which the paper reads as consistent with the state.
- Item 7: never says the functional link has no mutant, binding or activity data behind it (the support is only literature, refs 42–44). "Nucleotide binds the closed major state" also blurs the proposed order: binding to the partially closed state first, then closure.
- Over-claim: describes the apo sample as "qualitatively matching 4AKE" (field 6). The paper never compares apo PCSs with 4AKE. The cited ED Fig. 4d,f fit turnover PCSs to 4AKE and report a poor fit.

**E2**
- Item 2: says no alternative apo state is proposed (fields 6 and 10). The Results and Fig. 3f propose that the apo ensemble partially closes into a state that nucleotides then select.
- Item 3: no Δδ range. The per-metal kex values (Zn2+ 1,355 ± 65, Co2+ 1,367 ± 71 s−1) are left out.
- Factual error: says the per-residue values are in Supplementary Table 1. The main text cites that table only for the lid-opening structural parameters, and the reference reads it as AMP-lid angle and Co2+–core distance.

**E3**
- Item 2: gives no major-state population (≈87%).
- Item 3: no Δδ range. The per-metal kex values are left out; the entry only says "individual fits equivalent".
- Item 4: puts the ATP lid alongside the AMP lid as the largest change. The Fig. 3b,d that E3 cites put the largest change in the AMP lid and show only slight ATP-lid motion.

**E4**
- Item 3: no Δδ range. It only says Δδpara is below the ≥0.5 ppm open–closed prediction.

## Notes

- E4 is the strongest entry. Every number checks out, it presents the Fig. 3f mechanism as a proposed apo-binding role that was never measured on an apo sample, and it states the limits from one field, one temperature and rigid-body refinement. Its only gap is the Δδ range.
- All four reach the correct verdict: Not included, with apo defined by the absence of nucleotide, not by Zn2+/Co2+. All four report the core kinetics correctly (kex 1,428 ± 83 s−1, pB 12.6 ± 2.5%, kopen 180 ± 36 s−1, and 2.6 ± 0.3 s−1 without Mg2+). All four describe the minor state as partially open (AMP lid ~15°, metal shift 1.8 Å, r.m.s.d. 2.67 vs 7.03 Å) and still occupied by nucleotide. None makes a claim from the reference's over-claim list.
- Gaps shared by all four: none gives a Δδ range, and none says that calling the minor state the rate-limiting lid-opening state depends on earlier work (ref. 25). Listing the Fig. 3f apo partially closed state as a Candidate was optional, and no entry did it.
- E2 comes close to E4. The two are the only entries that report the RDC/PCS tensor control against metal motion. E2 loses points for the table-locator error and for saying the paper proposes no apo state.
- E3 has accurate numbers and the most complete identity basis (benchmarks, leave-one-out, independence from the starting structure). It leaves out the major-state population and ranks the ATP lid too high.
- E1 is accurate on conditions and numbers. It is the only entry that says what the other test proteins show: calmodulin and Src are simulated, and ubiquitin and trigger factor are method tests. It is thin on validation of the identity, on simulations and on the evidence behind the functional link, and it adds the 4AKE over-claim.

## Paper consultation

Europe PMC's full-text endpoint returned a server error, so I read the PMC article page (PMC9126080). I used it to settle points where the entries and the reference differ, or where the reference is silent:
- "kcat ≈ kopen ≈ 100 s−1" is stated in the Results, so E1–E3 are correct.
- Assignment was done at 40 °C, with 92% (Zn2+) and 83% (Co2+) coverage (Methods). E3 and E4 are correct.
- Methods define two rigid-body schemes. The first stage uses core 1–28/62–113/165–217, AMP lid 32–55, hinge 116–125 and ATP lid 128–157; the second stage adds AMP lid 3 = 62–79. The ranges in the entries and in the reference are both correct.
- The ED Fig. 3 legend literally reads "p>0.05", which E1 quotes. ED Fig. 4b gives ">0.1 ppm" and 4g gives "|0.5 ppm| or greater", so E2–E4 are correct.
- Ref. 44 is the authors' high-pressure NMR paper (E2 is correct). 4AKE chains were among the homology-modelled benchmarks (E2 is correct). The PMID is 35236984 (E3 is correct). "Bacillus stearothermophilus" appears in the title of a cited reference, which supports E2 and E3.
- The Supplementary Information PDF sits behind a PMC bot check, so I did not retrieve it. E2's Supplementary Table 1 error therefore rests on the main text and the reference.
- I did not check E3's details taken from PDB records (4QBH "AKlse5", 1.67 Å; 4AKE 2.2 Å) because those records are outside the allowed sources. They are consistent with the reference's description (a stabilized 4QBH variant; 4AKE from *E. coli*) and were not scored.
