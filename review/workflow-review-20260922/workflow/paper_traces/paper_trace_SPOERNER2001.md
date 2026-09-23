# Workflow trace — Spoerner et al. 2001, PNAS 98:4944–4949 (Ras switch I)

## 1. ACCESS

Full text read via PMC (https://pmc.ncbi.nlm.nih.gov/articles/PMC33143/): Abstract, Introduction, Methods, Results/Discussion, Conclusion, Tables 1–4, all five figure legends, references. No PDF downloaded, no analysis run. 2001 PNAS Track II paper; no supplementary information exists.

## 2. SYSTEM AND STATES

H-Ras ("Ras"), residues 1–166: wild type, switch I mutants T35S/T35A (Thr-35 is switch I's one invariant residue), and flexibility controls V29G/I36G/V29G+I36G (Methods: Protein Purification). GppNHp+Mg²⁺ is bound throughout — "the protein is always complexed by Mg²⁺·GppNHp" (Results, Kinetics, EXPLICIT). Effectors: Raf-RBD, RalGDS-RBD, AF6-RBD, Byr2-RBD. Conditions vary by method: NMR 5 °C, stopped-flow 10 °C, GDI affinities 37 °C. State 1 = nonbinding conformation; state 2 = minor wild-type conformation matching the effector-bound structure. "Apo" means apo-effector, never apo-nucleotide — no nucleotide-free Ras is studied.

## 3. WORKFLOW TRACE

1. **[Stage 1/2, EXPLICIT]** T35S's use as a "RalGDS-selective" tool, despite no direct Thr-35–effector contact in the Raps·Raf-RBD structure (ref. 37) → GDI-method KD (37 °C) tests this: Raf-RBD 60-fold weaker (0.02→1.2 µM), RalGDS-RBD ≥29-fold, AF6-RBD ≥25-fold, Byr2-RBD 12-fold → all four effectors weakened, not just RalGDS; since Thr-35 makes no contact, the cause must be indirect/dynamic. *Introduction ¶3–4; Table 1.*
2. **[Stage 4, EXPLICIT]** ³¹P-NMR, wt·GppNHp, 5 °C → two resolved α-/β-P peaks (states 1/2), K*=1.09, interconversion 130–1,900 s⁻¹ (ref. 7) → real two-state equilibrium at rest. *Fig. 1; Table 2.*
3. **[Stage 4→5, EXPLICIT]** Same NMR, T35S/T35A → single peak each at WT's state-1 shifts (T35S −11.10/−2.57 ppm; T35A −11.09/−2.49 vs. WT δ1 −11.20/−2.56), K*<0.05 both → state 2 essentially abolished (interpretive ambiguity noted in §7). V29G/I36G/double "hinge" mutants (flexibility, not at Thr-35) give the same single-peak spectrum, favoring a flexible-ensemble reading. *Fig. 1; Table 2; Results ¶4.*
4. **[Stage 6, EXPLICIT]** T35S x-ray, 2.9 Å, 3 molecules/asymmetric unit → switch I (~30–38) and II (~61–70) invisible in all three; fold otherwise unchanged (rms 0.47–0.73 Å); different space group than WT. Artifact check: lattice contacts, plus a control structure (Ras·GppCH2p, 6q21) whose contact-free molecules stay ordered; modeling WT's loop into T35S's contact-bearing sites would clash with symmetry mates → disorder is real, not packing. *Fig. 3; Table 3; Results ¶1–2.*
5. **[Stage 5/7, EXPLICIT]** NMR titration of Raf-RBD/RalGDS-RBD into T35S/T35A → T35S shifts fully to state-2 with either effector (+RalGDS-RBD −11.53/−3.26 vs. WT+RalGDS −11.6/−3.4); T35A shows only slight change with Raf-RBD, none with RalGDS-RBD. GDI saturates out of range for T35S+RalGDS-RBD ("too low to be determined") → switched to the NMR peak-integral ratio itself as titration, KD≈360 µM; T35A+RalGDS-RBD has no resolvable shift at all → switched again to γ-P line-broadening vs. concentration, KD≈10 mM. *Fig. 4; Table 2; Results, "Conformational State...".*
6. **[Stage 4/5/7, EXPLICIT]** Stopped-flow, Raf-RBD + mGppNHp-Ras, 10 °C, two-step model → WT K1=11.7 µM, k2=415 s⁻¹, KD=0.05 µM; T35S K1=68.8 µM, k2=211 s⁻¹, KD=2.1 µM (≈GDI's 1.2 µM); T35A shows no saturation (model doesn't fit), apparent KD=7.2 µM from koff/kon — read as a different mechanism (Ala can't coordinate Mg²⁺ like Thr/Ser). Confound check: Mg²⁺ affinity drops only 3-fold (T35S)/4-fold (T35A) — far smaller than the 42–60-fold effector loss, matching a prior mGDP result (ref. 46) — ruled out. RalGDS-RBD stopped-flow with either mutant: "no change in fluorescence signal," unresolved. *Fig. 5; Table 4; Results, "Kinetics...".*

## 4. STUCK POINTS

All EXPLICIT. (1) Direct-contact reasoning failed first — Thr-35 doesn't touch the effector — pushing the paper toward dynamics instead (step 1). (2) A single collapsed NMR peak was ambiguous between a fixed conformation and a fast ensemble (step 3); resolved not with more NMR but with **crystallography — switch I/II's missing electron density read as positive evidence of disorder** (step 4), only after a packing-artifact check, and cross-checked against flexibility mutants reproducing the same spectrum (step 3). (3) The GDI affinity assay ran out of range for weaker pairs; the paper swapped methods twice as the signal weakened — to NMR peak-integral titration, then to line-broadening (step 5). (4) A kinetic model that failed to fit T35A was not patched with a hidden state — the failure itself became the finding, anchored to Ala's inability to coordinate Mg²⁺; a named confound (Mg²⁺ affinity) was measured directly and shown too small to matter; and RalGDS-RBD stopped-flow gave no signal at all for either mutant, reported as a null rather than dropped (all step 6).

## 5. HOW THE ALTERNATIVE STATE WAS ESTABLISHED

Detection: two ³¹P peaks per phosphate at rest, K*=1.09 (step 2; Fig. 1, Table 2). Mutants shifting the equilibrium: T35S/T35A collapse to the state-1 peak alone, K*<0.05 (step 3; same locators). Effector binding shifting it back: Raf-RBD/RalGDS-RBD drive T35S fully to state-2 shifts; T35A does not follow (step 5; Fig. 4, Table 2). Kinetics showing an isomerization step: a saturating two-step fit for WT (KD=0.05 µM) and T35S (KD=2.1 µM, matching the 1.2 µM GDI value), but no saturation for T35A (step 6; Fig. 5, Table 4). Chain: peak-splitting → mutation removes the minor peak → effector restores it → kinetics locate a mutation-sensitive isomerization step at the same equilibrium — together tying "state 2" to a mechanistically real, effector-competent conformation, not a curve-fitting artifact.

## 6. COMPARISON WITH THE DRAFT CARDS

**(a) MATCHES**
- Card 1's "protein is always nucleotide-bound [Hansen 2023, K-Ras·GTP]" stuck signal — recurs identically (§2).
- Card 4 "when stuck" #6, "Cross-validate with a second method ... NMR against kinetics" — step 6 (kinetic KD 2.1 µM vs. GDI KD 1.2 µM).
- Card 5 routine move, "Find a mutation or ligand that shifts the population" — the paper's central move (steps 3, 5).
- Card 7 routine move, "whether mutations that shift the population change binding or activity" — steps 1, 3, 6 together.

**(b) NEW MOVES**
- Card 6 "when stuck": read missing electron density in the target region as positive evidence of flexibility, only after a crystal-contact/control-structure check rules out a packing artifact (step 4).
- Card 4 "when stuck": when a shift titration loses resolution, fall back stepwise — peak integrals, then line-broadening — before giving up on an affinity number (step 5).
- Card 4 "when stuck": a failed model fit can itself be the finding if backed by independent structural rationale; name a specific confound and measure it directly rather than list it generically; report a method's outright null result explicitly rather than drop the comparison (step 6, three related moves).

**(c) CONTRADICTIONS**
- Card 3's comparability check is skipped: NMR (5 °C), stopped-flow (10 °C), and GDI (37 °C) KD's are treated as consistent (2.1 vs. 1.2 µM) with no discussion of the temperature spread — even a careful, highly-cited paper omits the check the draft wants mandatory.
- Card 5's claim limit ("consistent with the perturbation pattern of <PDB>, never 'the structure is <PDB>'") is stricter than this paper's own wording, which states state 2 "corresponds to" the effector-bound structure directly.
- Card 6's "done when" (samples/does-not/cannot-tell verdict on existing MD) has no valid answer for a 2001 paper — no MD of this system existed yet; the card needs a fourth outcome.

## 7. DEFINITION ISSUES

The abstract calls the two states "rapidly interconverting," yet detecting them requires slow exchange on the ³¹P timescale (two resolved peaks, not one averaged peak). Background knowledge: the rate (130–1,900 s⁻¹) is fast biologically but still slow relative to the ³¹P shift separation at 202 MHz — both timescales need their numbers attached, or "rapid" could be misread as "no splitting expected." Ras is nucleotide-bound in every experiment (§2); "apo" is unambiguous only if recorded as apo-relative-to-effector, never apo-relative-to-nucleotide — the same trap flagged for K-Ras recurs here. The authors flag that one collapsed NMR peak fits either a fixed conformation or a disordered ensemble (Results ¶4, step 3) — an entry built from mutant NMR alone would need the crystallography and flexibility-mutant evidence (steps 3–4) to call "state 1" one coherent thing rather than a family of substates.
