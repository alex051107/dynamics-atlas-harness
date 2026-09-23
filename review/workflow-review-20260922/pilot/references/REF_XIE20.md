# REF_XIE20 — sealed reference answer

Xie T, Saleh T, Rossi P, Kalodimos CG. Conformational states dynamically populated by a kinase determine its function. Science 2020;370:eabc2754.
Sources read: main text (PMC7920495, NIH author manuscript), Supplementary Materials (figs. S1–S12, Table S1, Movie captions), BMRB 30770–30772, PDB 6XR6/6XR7/6XRG.

## PART 1 — REFERENCE ENTRY

1. **Protein** — Abl (ABL1) tyrosine kinase, kinase domain [paper; Results]. The text does not state the species; the deposited entries record *Homo sapiens*, UniProt P00519 [our reading of the paper's data; PDB 6XR6; BMRB 30770].

2. **Construct and conditions** — Kinase domain, residues 248–534 (isoform 1b numbering), wild type and unphosphorylated. No nucleotide, Mg²⁺ or inhibitor [paper; Methods "Expression…", "NMR Sample Preparation"]. Buffer: 25 mM sodium phosphate pH 7.1, 75 mM NaCl, 3 mM BME, ²H₂O. ¹³CHD₂ methyls on a U-²H background [paper; Methods]. CEST at 10 °C, Tmix 500 ms, B₁ 15 and 25 Hz [paper; fig. S2 legend; Methods "CEST experiments"]. CEST field not stated (spectrometers: 600 MHz–1.1 GHz) [paper; Methods "NMR Spectroscopy"]. Series at pH 6.5, 7.1 and 7.7 [paper; Fig. 6D–F] and at 5, 10 and 15 °C on H415P [our reading of the paper's data; Fig. 6G,H]. Structure datasets: 283 K, 850 and 1100 MHz, pH 7.1 (active), 6.5 (I1) and 7.7 (I2) [our reading of the paper's data; BMRB 30770–30772].

3. **Apo relative to** — ATP-site inhibitors: chiefly imatinib (its bound-state shifts identify I2, which it selects) and PD173955 (its shifts identify I1) [paper; Fig. 1E,F legends ("apo"); Results "Structure of the Abl excited state 1/2"]. The "unliganded" domain also lacks nucleotide, substrate and the SH3-SH2 module [paper; Methods].

4. **Verdict** — Strong. CEST detects two minor states in unliganded wild-type Abl, with traceable populations and rates. Independent support: inhibitor chemical-shift matches, state-stabilizing mutants with slow-exchange peak doubling, ZZ-exchange and NOE structures. The functional link is strong for I2; for I1 it is limited to selection by PD173955 [paper; Fig. 1; figs. S5, S6; Discussion].

5. **Major state** — Active state, 88%: DFG-in; αC-in (Lys290–Glu305 ion pair); A-loop open (Tyr412 H-bonded to Arg381 and Arg405); regulatory spine assembled. NMR structure PDB 6XR6 / BMRB 30770, compatible with dasatinib binding [paper; Figs. 1D, 2A, 4A; fig. S3].

6. **Alternative state(s)** — **I1 (E1), 5.9 ± 0.1%.** DFG-out by a 180° flip, with Asp400 buried. The A-loop stays open, but Leu403–Met407 flip. Arg405 forms a salt bridge with Glu311; αC stays in. Resembles Abl–PD173955 (1M52). PDB 6XR7 / BMRB 30771 [paper; Fig. 2B; fig. S5H; Methods "CEST data fitting"].
**I2 (E2), 6.1 ± 0.7%.** DFG-out with Phe401 moved ~11 Å into a pocket, where it blocks ATP. The A-loop is closed, with Tyr412 as a pseudosubstrate; the P-loop is stretched and αC is out. Matches Abl–imatinib (1IEP) in the A-loop and DFG but not in αC or the P-loop; resembles inactive IRK (1IRK). PDB 6XRG / BMRB 30772 [paper; Fig. 2C,D; fig. S12].

7. **Evidence type** — ¹³C-methyl CEST: 40 probes with one minor dip, 43 with two [paper; Fig. 1B,C]. Line broadening of A-loop and αC resonances at ≥20 °C [paper; fig. S1]. Doubled slow-exchange peaks in stabilized variants, and ¹H-¹³C ZZ-exchange cross peaks in T408Y, kinetics not quantified [paper; figs. S5C, S6B–D]. CEST as a function of pH and temperature [paper; Fig. 6].

8. **Exchange parameters** — Global linear fit G↔E1↔E2 in ChemEx. kex(G↔E1) = 46.8 ± 4.3 s⁻¹, fixed from a two-state fit of H415P (pE1 12.1 ± 0.5%). kex(E1↔E2) = 88.7 ± 13.5 s⁻¹. pE1 = 5.9 ± 0.1%, pE2 = 6.1 ± 0.7% [paper; Methods "CEST data fitting"; Fig. 1D]. The star model E1↔G↔E2 fit equally well (χ²red 1.41 vs 1.42); the linear model was chosen for agreement with H415P [paper; Methods]. ¹³C Δϖ runs from about −1.4 to +1.5 ppm for E1 and from −2.8 to +2.0 ppm for E2. Dips within ±0.3 ppm of G were not resolved [our reading of the paper's data; Fig. 1E,F]. The A→I1 Arrhenius activation energy (H415P) is ~36 kcal/mol [paper; Fig. 6H,I].

9. **Residues or regions** — A-loop (DFG 400–402, Leu403–Met407, Thr408, Tyr412, His415); αC helix (Glu305, Glu311); P-loop (Gly269–Glu274); Lys290 and Lys293; regulatory spine (Met309, Leu320, His380, Phe401). Exchanging probes span the domain and concentrate at the A-loop and αC [paper; Figs. 1B, 2, 4A].

10. **Identity basis** — E1 CEST shifts track the apo-to-PD173955 shift changes, not those for dasatinib or imatinib. E2 shifts track the apo-to-imatinib changes, except for the αC methyls. Methyls within 6 Å of the inhibitor were excluded [paper; Fig. 1E,F; figs. S5A, S8]. The stabilizing mutants reproduce the CEST shifts and supply the NOEs [paper; figs. S5E, S6B,E].

11. **Structural mapping and simulations** — NMR structures of all three states (CYANA/CNS; 867, 849 and 729 NOEs; 20 conformers each) [paper; Methods "Structure determination"; Table S1]. The I1 structure uses M309L/H415P (~50% I1 at pH 6.5) plus Abl–PD173955 restraints for unchanged regions. The I2 structure uses G269E/M309L/T408Y (~90% I2) [paper; Methods; fig. S5D]. No simulation sampled the states; Movies S1–S3 are morphs [paper; SI p. 21].

12. **Functional relevance** — Imatinib selects I2, as do nilotinib, ponatinib and rebastinib. PD173955 binds I1; dasatinib and axitinib bind the active state [paper; Figs. 3A, 5D; figs. S3, S4]. Remote resistance mutations deplete I2 (I2 change; affinity loss): H415P (<1%; 5×), Y272H (~7×; ~10×), F378V (~4×; ~4×), E274V (~1.4 kcal/mol) [paper; Fig. 3]. The SH3-SH2 module raises I2 from 6% to 34%, and GNF5 raises it to 95%. H415P, T334I and pY412 restore the active state [paper; Fig. 5]. M309L/L320I (82% I2) and F401V (>95% I2, ≥20× lower activity) inactivate the kinase [paper; Fig. 4; fig. S11]. The role of I1 is "not apparent" [paper; Discussion].

13. **Competing explanations addressed** — Mutant-induced structural change: the mutant shifts fall on the CEST values [paper; figs. S5E, S6E, S8B]. Dip assignment: opposite pH dependence and H415P removing E2 [paper; Methods]; E311K removes only E1 [paper; Fig. 2E]. Kinetic topology: three models compared; populations above ~10% did not fit [paper; Methods]. E2–imatinib outliers: αC and P-loop differences plus Trp254/Phe420 ring currents [paper; fig. S8].

14. **What this evidence cannot support** — Wild-type structures of the minor states (they come from mutants at altered pH). Pure conformational selection by imatinib (it remodels αC and the P-loop). A uniquely determined kinetic topology. Reading 36 kcal/mol as a free-energy barrier or applying it to wild type or A↔I2. Populations for full-length Abl, Bcr-Abl, 37 °C or cells (Abl^FK: 2D spectra only, I1 undetermined) [inference; Methods; Fig. 5A legend].

15. **Provenance** — DOI 10.1126/science.abc2754; PMID 33004676; PMC7920495 (NIHMS1671082). Figs. 1–6; figs. S1–S12; Table S1; Methods "CEST data fitting" [paper]. PDB/BMRB pairs: 6XR6/30770 (active), 6XR7/30771 (I1), 6XRG/30772 (I2). Comparators: 1M52, 1IEP, 2GQG, 4TWP, 4XEY, 1IRK [paper; Data availability; figure legends]. Inconsistencies: E2 is given once as 5%; fig. S7 writes I2M as "M309L/G369E/T408Y" (G269E elsewhere and in 6XRG); 6XR7/30771 list a wild-type sequence [our reading of the paper's data].

## PART 2 — MUST-GET-RIGHT

- **Verdict and apo definition.** The verdict is strong. "Apo" means the isolated, unphosphorylated Abl kinase domain (residues 248–534, isoform 1b) with no inhibitor or nucleotide. The ligand that defines apo is imatinib, whose target is I2; PD173955 plays that role for I1 (Results "Structure of the Abl excited state 1/2"; Fig. 1E,F; Methods).
- **Three states and their populations.** The ground state is the active state (88%), not an inactive one. The minor states are I1 ≈ 6% (5.9 ± 0.1%) and I2 ≈ 6% (6.1 ± 0.7%) at pH 7.1 and 10 °C (Fig. 1D; Methods "CEST data fitting"; fig. S2).
- **Exchange measurement.** ¹³C-methyl CEST, with 40 one-dip and 43 two-dip probes, fitted to a linear G↔E1↔E2 model. kex(G↔E1) = 46.8 ± 4.3 s⁻¹, fixed from the H415P two-state fit; kex(E1↔E2) = 88.7 ± 13.5 s⁻¹. Exchange is slow on the chemical-shift timescale (Fig. 1B–D; Methods).
- **State structures.** I1 is DFG-out, αC-in and A-loop open, matching PD173955-bound Abl (1M52). I2 is DFG-out, αC-out, A-loop closed and P-loop stretched; it matches imatinib-bound Abl (1IEP) only in the A-loop and DFG (Fig. 2B–D; fig. S5H).
- **Identity basis.** CEST ¹³C shifts were correlated with inhibitor-bound shifts, with dasatinib and imatinib as negative controls for I1. Mutants raise each state's population: M309L/H415P to ~50% I1 at pH 6.5; T408Y to 70% and G269E/M309L/T408Y to ~90% I2. The mutants show doubled slow-exchange peaks, ZZ-exchange cross peaks and shifts that match CEST (Fig. 1E,F; figs. S5, S6, S8).
- **Deposited structures.** 6XR6/BMRB 30770 (active, wild type); 6XR7/30771 (I1, data from M309L/H415P); 6XRG/30772 (I2, G269E/M309L/T408Y) (Data availability; PDB/BMRB records).
- **Imatinib resistance.** Imatinib selects I2. Resistance mutations remote from the drug deplete I2 and lower affinity: H415P (I2 <1%, affinity 5× lower), Y272H (I2 ~7× lower, affinity ~10× lower), F378V (~4× and ~4×), E274V (I2 destabilized by ~1.4 kcal/mol) (Fig. 3; fig. S9).
- **Autoinhibition.** I2 is the autoinhibited state. In Abl^FK the SH3-SH2 module raises I2 from 6% to 34%, and GNF5 raises it to 95%. T334I, pY412 and H415P counteract this (Fig. 5).
- **pH and flip barrier.** pH 6.5 favours I1 and pH 7.7 favours I2, while the total inactive population stays constant. The A→I1 DFG flip has an Arrhenius activation energy of ~36 kcal/mol, measured on H415P from 5 to 15 °C (Fig. 6).
- **Role of I1.** The biological role of I1 is not apparent. E311K depletes I1 without changing I2, and the authors therefore consider I1 not an obligatory intermediate (Discussion; Fig. 2E).

## PART 3 — OVER-CLAIMS

- **"NMR structures of the wild-type excited states were determined."** The structures come from stabilizing mutants at shifted pH: I1 from M309L/H415P at pH 6.5, partly restrained from the PD173955 complex; I2 from G269E/M309L/T408Y at pH 7.7. Equivalence to wild type rests on chemical-shift agreement only (Methods "Structure determination"; figs. S5E, S6E).
- **"Imatinib binds purely by conformational selection; I2 is the imatinib-bound conformation."** I2 matches the complex only in the A-loop and DFG, and imatinib must remodel αC and the P-loop. The authors say imatinib "apparently" binds I2 selectively, and no binding kinetics were measured (Results "Structural differences"; Fig. 2D).
- **"The DFG flip has a ~36 kcal/mol free-energy barrier in Abl."** The value is an Arrhenius activation energy from three temperatures (5–15 °C). It covers only A↔I1, and only in H415P. Fig. 6I's "ΔG‡" label conflicts with its legend's "activation enthalpy". By the Eyring relation, the ~6 s⁻¹ forward rate at 283 K implies a free-energy barrier near 15.5 kcal/mol (inference, background knowledge).
- **"The mechanism is linear, and I1 is (or is not) an obligatory intermediate."** With kex1 fixed, the star model fits equally well (χ²red 1.41 vs 1.42). Equilibrium populations such as those of E311K cannot test pathway order (Methods; Discussion; inference).
- **"About 6% of cellular Bcr-Abl is in I1 and I2, interconverting at these rates."** The measurements are for the isolated domain at 10 °C in vitro. The SH3-SH2 module alone raises I2 to 34%. Abl^FK was quantified by 2D spectra only, its I1 population is unknown, and there are no cellular data (Fig. 5A legend; Methods).
- **"Every imatinib-resistance mutation acts by depleting I2."** G269E raises I2 about 4-fold and Q271H raises P-loop I2, yet both lower affinity. E274V's effect on I2 was measured only in the I2M background. All of these data come from isolated-domain constructs, not from patients or cells (fig. S10; Fig. 3F).
- **"I1 is a regulatory state, and these states are general across the kinome."** The authors see no biological function for I1. The kinome extension is structural analogy to crystal structures (IRK, KIT and others), not measured dynamics (Discussion; fig. S12).
- **Residue numbering.** The paper uses isoform 1b numbering. Background knowledge: 1b numbers are 1a numbers plus 19, so T334I is the clinical "T315I" and H415P is "H396P". Mixing the two schemes misassigns residues (Methods "Expression").

## ERRATA AFTER INDEPENDENT CHECK (applied before grading)

A separate checker compared this reference with the paper, its Fig. 6 image and the cited PDB and BMRB records (see CHECK_XIE20.md). No corrections were needed, and no over-claim item turned out to be supported by the paper. Notes:

- Over-claim D3 (the ~36 kcal/mol "free-energy barrier"): the panel of Fig. 6I is labelled "ΔG‡~36.4", while the main text says activation energy and the legend says activation enthalpy. The checker judged that the over-claim stands; an entry that cites the panel label is quoting the paper.
- Not verified, because the checker could not open the supplement: the Table S1 NOE counts (867/849/729), the Movie S1–S3 captions and the "SI p.21" locator, the "G369E" typo in fig. S7 (RCSB confirms G269E is correct), the Trp254/Phe420 ring-current detail in fig. S8, and the exact fold-changes for G269E and Q271H in figs. S9–S10.
