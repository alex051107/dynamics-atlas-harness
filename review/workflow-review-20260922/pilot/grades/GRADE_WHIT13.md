# GRADE_WHIT13: Whittier, Hengge & Loria, Science 2013 (PTP1B and YopH WPD loop)

Graded against REF_WHIT13.md with its errata applied. Items: 1 apo verdict and ligand · 2 major and alternative states · 3 exchange parameters with sources · 4 residues or regions · 5 identity basis · 6 structural mapping and simulations · 7 functional relevance (wording matched to evidence) · 8 evidence type and provenance · 9 tier.

| Entry | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | Over-claims | Factual errors | Total | Scored items |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | 1 | 1 | 1 | 0 | 11 | 9 |
| E2 | 2 | 2 | 2 | 2 | 1 | 2 | 1 | 1 | 1 | 2 | 0 | 14 | 9 |
| E3 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 1 | 1 | 0 | 1 | 15 | 9 |
| E4 | 2 | 2 | 1 | 2 | 1 | 2 | 1 | 1 | 1 | 2 | 1 | 13 | 9 |

```json
{"E1": {"items": [2, 1, 1, 1, 1, 2, 1, 1, 1], "over_claims": 1, "factual_errors": 0}, "E2": {"items": [2, 2, 2, 2, 1, 2, 1, 1, 1], "over_claims": 2, "factual_errors": 0}, "E3": {"items": [2, 1, 2, 2, 2, 2, 2, 1, 1], "over_claims": 0, "factual_errors": 1}, "E4": {"items": [2, 2, 1, 2, 1, 2, 1, 1, 1], "over_claims": 2, "factual_errors": 1}}
```

## Deductions

### E1 (writes the entry for PTP1B only; YopH appears only in asides)
- Item 2 = 1: PTP1B open 97.5% / closed 2.5% and 1SUG are right; the YopH states and populations (≈97% / ≈3%) are absent.
- Item 3 = 1: PTP1B apo and peptide-bound parameters are right and sourced; YopH apo kex 43,000, kclose 1,240 and kopen 42,000 s⁻¹, and the proxy-derived pa, are absent.
- Item 4 = 1: the YopH probes A359 and S361 (T358 overlapped, V360 weak) are absent.
- Item 5 = 1: the PTP1B three-way shift agreement is right, including the W179 caveat; there is no YopH identity basis (the apo closed state is assumed there).
- Item 7 = 1: PTP1B kclose ≈ kcleavage is right; the YopH link and the tungstate result are absent, and a binding mechanism is attributed to the paper (over-claim below).
- Item 8 = 1: the YopH evidence (flat 15N CPMG/R1ρ, TROSY 1H R1ρ, Hahn-echo Rex) is absent; BMRB 19272 and PDB 1YPT (supplement only) are missing.
- Item 9 = 1: "Strong" is right for PTP1B; YopH gets no tier (reference: weak).
- Over-claim 1: field 12, "consistent with selection of a pre-existing minor conformation rather than induction of a new one [paper, main text]". The paper makes no selection-versus-induction claim and measured no peptide-binding kinetics (reference over-claim list).

### E2
- Item 5 = 1: the PTP1B three-way agreement is right; field 10 gives no YopH basis, and the verdict says the YopH minor-state shifts were cross-validated.
- Item 7 = 1: the rate correlation and the 200-fold (PTP1B) and 2,300-fold (YopH) slowing of opening are right; YopH kcleavage is presented as "separately measured".
- Item 8 = 1: evidence types for both enzymes are complete; BMRB 19272 and PDB 1YPT (supplement only) are missing.
- Item 9 = 1: one "Strong" verdict covers both enzymes; YopH should be weak because its Δω and population were not measured.
- Over-claim 1: the verdict says apo dispersion "in both enzymes resolves a minor closed-WPD-loop state whose shift signature is cross-validated" against 1SUG and the bound spectrum. For apo YopH, Table 1 lists Δω as "Not Determined", and pa comes from a shift proxy.
- Over-claim 2: the verdict says the "closing rate tracks each enzyme's separately measured cleavage rate", and field 12 says "independent kcleavage". The YopH value of 1,400–2,000 s⁻¹ is inferred ("these kinetic data indicate"; the reference reads the supplement as 2–3× kcat), not measured (reference over-claim list).

### E3
- Item 2 = 1: the state fields describe PTP1B only (the YopH ≈97% / ≈3% split is never stated; field 8 gives only Keq 34) and contain the factual error below.
- Item 8 = 1: evidence types for both enzymes are complete; BMRB 19272 and PDB 1YPT (supplement only) are missing.
- Item 9 = 1: "Strong" is right for PTP1B; YopH is called "consistent but more indirect" for the right reason (apo Δω not fitted) but gets no tier.
- Factual error 1: field 6 gives the PTP1B peptide-bound closed population as "~99%". Table 1 gives Keq 0.15, which means ≈87% closed, and E3's own field 8 lists 0.15. The 99% figure belongs to YopH.

### E4
- Item 3 = 1: PTP1B and peptide-bound values are right; the apo YopH Δω is reported as measured (factual error below).
- Item 5 = 1: the PTP1B three-way agreement is right, with numbers; field 10 gives no YopH basis, while the verdict calls the YopH identity "corroborated by independent crystal forms".
- Item 7 = 1: YopH kcleavage is called "independently measured", and the peptide effect is framed as conformational selection (both over-claims below).
- Item 8 = 1: evidence types are complete; BMRB 19272 and PDB 1YPT (supplement only) are missing.
- Item 9 = 1: one "Strong" verdict covers both paralogs; YopH should be weak.
- Over-claim 1: field 12, "Apo kclose approximates the independently measured phosphoryl-cleavage rate kcleavage in both". The YopH value is inferred, not measured (reference over-claim list).
- Over-claim 2: field 12, "consistent with conformational selection [paper, Table 1]". The paper never says this and measured no binding kinetics (reference over-claim list).
- Factual error 1: field 8, "Δω(measured)=3.4–6.4 ppm (A359, S361)" for apo YopH. Those numbers are the ShiftX2 Δδcalc values. The measured apo-versus-bound differences are 3.82 and 3.96 ppm, and Table 1 lists the apo Δω as "Not Determined".

## Notes
- **Paper opened.** The Europe PMC XML endpoint returned HTTP 500, so I read the PMC main text in my own browser tab to settle disagreements. What it showed:
  - The paper itself says "loop closure is the same in apo and peptide bound PTP1B; peptide binding only slows loop opening", so "kclose unchanged" (E1, E2) is not counted.
  - pH 6.6 and 293 K belong to the cited kinetics, as E2 and E3 say.
  - kcleavage for both enzymes is introduced as "these kinetic data indicate…", never as a direct measurement.
  - The main text never discusses conformational selection.
  - Table 1 gives apo YopH Δω as "Not Determined", with Δδcalc 3.4/6.4 and Δωmeas 3.82/3.96 ppm.
  - The eight-residue P-loop and R221 (E4), "no available data for comparison" (E1), "static on the timescale observable by NMR" (E3), and the 50-fold gap with p-nitrocatechol sulfate (E2) are all in the text.
- **Scoring conventions.**
  - The paper has two apo alternative states (PTP1B and YopH), and every item was scored against both, as the reference does.
  - None of the entries read the supplement. The supplement-only must-get-right anchors (BMRB 19272, PDB 1YPT) count as missing under item 8 for all four, not as factual errors.
  - The supplement-only conditions (Bis-Tris propane, pH 6.5, 293 K) are missing from all four, but they belong to the ungraded construct field. Item 1 was scored on the ligand-free verdict and the pTyr-substrate ligand, which all four get right.
  - No item is NA.
- **Borderline calls, not counted:**
  - E3's "consistent with binding trapping a pre-existing closed state" is labelled [our reading] and restates the measured kinetics: the closed state exists without ligand, and opening slows with it.
  - E3's "literature kcleavage" makes no measurement claim.
  - "ShiftX2 from 1SUG" (E1, E2, E4) follows the main text's "the crystal structure"; only the supplement says 22 closed structures were used.
  - E4's "~20–40-fold" kcat gap fits the stated rates (700–1,000 vs 15–30 s⁻¹), although the text says "about 20-fold".
- **Overall.** E3 is the only entry that marks YopH as weaker for the right reason, and it makes no over-claims; its one slip is the 99% figure. E2 has the most complete numbers but extends the PTP1B evidence to YopH. E4 does the same, mislabels the YopH shifts and adds conformational selection. E1 is accurate for PTP1B but leaves out YopH.
