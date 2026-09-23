# Workflow trace — Bouvignies et al. 2011, Nature 477:111–114 (T4 lysozyme L99A excited state)

## 1. ACCESS
Full text read via PMC (pmc.ncbi.nlm.nih.gov/articles/PMC3706084/): abstract, Results, Discussion, full Methods, all four figure legends, references, data-deposition footer. Europe PMC's XML endpoint (.../PMC3706084/fullTextXML) returned HTTP 500, unused. Supplementary Information is a separate PDF (NIHMS483958-supplement-Supplementary_Information.pdf, ~4.3 MB) linked from PMC; not downloaded (read-only rule). Statements below about Supplementary Figs. 1–10/Tables 1–9 are INFERRED from how the main text describes their contents, not read directly.

## 2. SYSTEM AND STATES
Protein: T4 lysozyme, engineered cavity mutant L99A (Leu99→Ala, ~150 Å3 cavity, C-terminal domain), not wild type; plus L99A,G113A T4L and triple mutant L99A,G113A,R119P T4L, built for validation. Conditions: ~1.5 mM protein, pH 5.5, 500–800 MHz; 25 °C default, 1 °C and 34–35 °C for specific experiments (Methods). States: ground state G (97% at 25 °C, matches X-ray PDB 3DMV) and excited state E (~3%, ~1 ms lifetime; Abstract, ref. 5). G and E are both unliganded conformers of L99A T4L, not an apo/holo pair — "apo" is defined relative to small hydrophobic ligands (benzene, Fig. 3c–e): G binds benzene, E does not.

## 3. WORKFLOW TRACE
1. (Stage 1, EXPLICIT) L99A cavity mutant of T4L; states G vs. E; apo relative to hydrophobic small molecules. Abstract; Intro ¶1–3.
2. (Stages 2–3, EXPLICIT) G⇌E (97%/3%, ~1 ms) reused from Mulder et al. 2001 (ref. 5); later experiments run at temperatures chosen per exchange regime — 25 °C main CPMG, 1 °C for G113A/benzene, 34–35 °C for triple-mutant assignment. Intro ¶3; Methods.
3. (Stage 4, EXPLICIT) Global two-site CPMG fit across residues/nuclei (Methods) gives near-complete E-state shift magnitudes (Supp. Fig. 1, Tables 1–5); separate sign experiments (multi-field comparison, ZQ/DQ CPMG) fix sign, since magnitude alone is two-valued — absent from the draft cards. Methods, "Sign experiments."
4. (Stage 5, EXPLICIT) ΔωRMS flags residues 100–120/132–146 (Fig. 1a); order parameters/TALOS+ show the regions stay ordered but gain F–G loop helicity (Fig. 1c, d). No known structure matched, so identity and structure are solved together, not by comparison.
5. (Stage 6, EXPLICIT) CS-Rosetta restricted to the flagged regions, rest fixed to X-ray (3DMV); 9,600→96 structures (Methods; Supp. Fig. 2), validated by a ground-state control (0.6 ± 0.2 Å). E ensemble 0.7 ± 0.2 Å r.m.s.d. (Supp. Table 6), PDB 2LCB — splits into trans/gauche– Phe114 χ1 clusters. STUCK: shifts alone can't tell which is real.
6. (Stage 6, EXPLICIT) Rosetta ΔΔG design screens mutations (105–120) for ones favoring E over G (Supp. Table 7); selects G113A, which at 1 °C gives two resolved peak sets at predicted G/E positions (Fig. 3a, b): pE = 34 ± 2%, kex = 48 ± 1 s⁻¹ (from <0.5%). Adding R119P fully inverts populations (G-like falls to 3.8 ± 0.1%, kex = 806 ± 28 s⁻¹; Supp. Fig. 8); J-coupling on this now-dominant proxy gives unambiguous trans χ1 (Supp. Fig. 9, Table 9), resolving step 5.
7. (Stage 7, EXPLICIT) Benzene (1:1) + G113A, 1 °C; three-state exchange fit: kGB = 11.6 ± 0.3 s⁻¹, kBG = 17.4 ± 0.4 s⁻¹ vs. kEB/kBE < 0.1 s⁻¹, F-test-confirmed zero (Methods; Supp. Fig. 5, Table 8) — only G binds. Binding-competent fraction: 97% → 66% → <5% (L99A / G113A / G113A,R119P; Fig. 4).
8. (Stage 8-adjacent, EXPLICIT) PDB 2LCB, 2LC9 deposited; no BMRB accession in the main text. Discussion separately flags a broader evolutionary proposal, distinct from the tested result.

## 4. STUCK POINTS
- Magnitude-only shifts, no reference structure (EXPLICIT, steps 3–4): CPMG gives magnitude only (sign needs extra experiments), and no PDB entry matched the pattern, so modeling went de novo rather than by resemblance.
- Ambiguous Phe114 rotamer between two CS-Rosetta clusters (EXPLICIT, steps 5–6): resolved by escalating mutant design — G113A confirms the shift assignments are real; G113A/R119P then inverts populations so an independent method (J-coupling) settles the rotamer without depending on the model under test.
- Exchange outside a method's window (EXPLICIT, step 2): G⇌E and benzene on/off are too fast at 25 °C for slow-exchange methods; 1 °C brings both into range; 34–35 °C instead cuts signal loss for assignment — temperature as an active lever, not just a caveat.
- Proving absence, not presence (EXPLICIT, step 7): kEB/kBE fit as free parameters, then F-tested to zero to show no benzene binding to E.

## 5. HOW THE ALTERNATIVE STATE WAS ESTABLISHED
Detection (steps 2–3): G⇌E first reported by Mulder et al. 2001 (97%/3%, ~1 ms), extended here to near-complete signed E-state shifts. Identity/structure (steps 3–5): shifts localize the change to residues 100–120/132–146; restricted, control-validated CS-Rosetta gives a converged ensemble (0.7 ± 0.2 Å, PDB 2LCB) but leaves the Phe114 rotamer ambiguous. Validation (step 6), the paper's central move: Rosetta ΔΔG design predicts G113A stabilizes E; tested, pE shifts from <0.5% to 34 ± 2%, a real spectral change. R119P then fully inverts the equilibrium (minor state 3.8 ± 0.1%); J-coupling on this proxy independently confirms trans χ1, closing the ambiguity without relying on the CS-Rosetta fit. Ligand state (step 7): three-state exchange gives kGB/kBG ≈ 11–17 s⁻¹ vs. kEB/kBE < 0.1 s⁻¹ (F-test zero) — binding proceeds only through G, matching Phe114 in the cavity in E. One designed mutation thus confirms both structure and function, a closure most papers in this set reach less directly.

## 6. COMPARISON WITH THE DRAFT CARDS

**(a) MATCHES**
- Card 3: NMR methods run at different temperatures — matches the 25 °C/1 °C/34–35 °C split here.
- Card 4: "many residues fit one global process" — matches the shared two-site fit.
- Card 4, when-stuck 5: "change temperature to bring the exchange into the measurable window" — matches the 1 °C work.
- Card 7: "which ligand or partner binds which state" — matches the three-state benzene fit, more quantitatively than the card implies.

**(b) NEW MOVES**
- Card 4/5 (routine): sign experiments to fix Δω's sign, missing from both cards, needed before a shift can support anything beyond rate/population.
- Card 6 (when stuck, high value): Rosetta ΔΔG design to pick a population-shifting mutation, test it, then invert fully so an invisible state becomes directly measurable — outside the card's current when-stuck list (trajectory length, starting bias, sampling), which addresses simulation, not experiment design.
- Card 2 (stronger stuck signal): shift/exchange data may exist only in a supplementary PDF; no BMRB entry was findable at all here.

**(c) CONTRADICTIONS**
- Cards 5 and 6 assume a candidate reference/matching structure exists to compare against. Here none did; identity and structure were solved in one de novo step, not two.
- Card 5's claim limit ("never 'the structure is <PDB>'") is stricter than this paper's own practice: after two mutant confirmations, the authors call their deposited result "the" excited-state structure (PDB 2LCB).

## 7. DEFINITION ISSUES
E is apo like G but loses ligand competence rather than gaining it — Phe114 occupies the pocket that binds benzene in G. Tests whether "functional relevance" must mean a new binding mode, or whether losing one counts equally.

L99A is an engineered cavity mutant; wild-type T4L shows much less broadening (Intro ¶3, ref. 5), so the process may be largely a property of the substitution, not a state wild-type T4L samples. Card 1's claim limit excludes substrate-bound and isolated-domain cases but has no language for an engineered-cavity case.

Benzene, the reference ligand, is a generic hydrophobic probe (refs 4, 20), not a physiological partner — tests whether the Atlas requires biological relevance in the reference ligand.
