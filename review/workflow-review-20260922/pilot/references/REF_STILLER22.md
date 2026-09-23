# REF_STILLER22 — sealed reference answer

Paper: Stiller JB, Otten R, Häussinger D, Rieder PS, Theobald DL, Kern D. Structure determination of high-energy states in a dynamic protein ensemble. *Nature* 2022;603:528–535. DOI 10.1038/s41586-022-04468-9 (PMC9126080; SI = publisher Supplementary Information PDF).

## PART 1 — REFERENCE ENTRY

1. **Protein** — Adenylate kinase (Adk), *Geobacillus stearothermophilus* [paper; Results, Adk section; Methods]. UniProt not stated [paper]; the cited PDB 4QBH maps to P27142 [our reading of PDB 4QBH]. Ubiquitin, *E. coli* trigger factor PPD–SBD and simulated calmodulin/Src are method tests only [paper, Fig. 4; BMRB 27239].

2. **Construct and conditions** — Wild-type sequence, no mutations stated; C-terminal TEV site and His6 tag [paper, Methods, protein expression]; deposited sequence ends in an ENLYFQ remnant (223 residues) [our reading of BMRB 51232/51233]. Natural tetra-cysteine ATP-lid site loaded with diamagnetic Zn2+ or paramagnetic Co2+ [paper, Results]. Perdeuterated 15N Adk, 2 mM, in 50 mM MOPS, 50 mM NaCl, 2 mM TCEP, pH 7.0 [paper, Methods, NMR]. Detection condition: turnover, 20 mM ADP + 20 mM MgCl2. Comparisons: 20 mM ADP without Mg2+, and nucleotide-free (HSQC only) [paper, Results; ED Figs 2–4]. 1H_N CPMG at 25 °C, 600 MHz only, 24 ms constant time, 16 νCPMG values 83–1,500 Hz [paper, Methods].

3. **Apo relative to** — Nucleotide substrates and products (ATP, AMP, ADP; Mg2+ is the catalytic cofactor); the paper's apo means nucleotide-free [paper, Results; ED Figs 2c, 4]. The structural Zn2+/Co2+ is present in every sample and does not define apo [our reading of the paper's data].

4. **Verdict** — **Not included.** The only characterized alternative state was detected at saturating Mg2+-ADP, and the authors conclude it "must be occupied with substrate or product" [paper, Results, high-energy structure section]. Nucleotide-free Adk has HSQC data only, no relaxation dispersion [paper, ED Figs 2c, 4]. The apo partially closed state in Fig. 3f is an author proposal; entered separately it would be at most a candidate, testable by Zn2+/Co2+ PCS–CPMG on nucleotide-free Adk [inference].

5. **Major state** — Fully closed, nucleotide-bound; ≈87% (1 − pB) [our reading of the paper's data]. Matches closed, Ap5A-bound PDB 4QBH: PCS fit Q = 11.6% under turnover (population-averaged), 7.6% in ADP without Mg2+ [paper, Results; ED Fig. 2a,b].

6. **Alternative state(s)** — Partially open, nucleotide-occupied high-energy state, pB = 12.6 ± 2.5% [paper, Results]. The AMP lid opens ~15° (~50% of closed-to-open); the ATP-lid Co2+ moves ~1.8 Å, partly separating the lid from the nucleotides and exposing a product-exit tunnel; r.m.s.d. 2.67 Å to closed vs 7.03 Å to open [paper, Results; Fig. 3c–e]. SI Table 1: AMP-lid angle 66.1 ± 1.0° (Δ 15.2 ± 1.0°); Co2+–core distance change 0.4 ± 0.33 Å [paper, SI]. Structure: new PCS–CPMG rigid-body model (top five, Fig. 3c), no PDB accession [paper, Data availability]. Not the apo open ensemble [paper, ED Fig. 4].

7. **Evidence type** — Paired diamagnetic (Zn2+) and paramagnetic (Co2+) 1H_N CPMG relaxation dispersion (PCS–CPMG); HSQC PCSs in turnover, ADP-only and apo conditions; slow-exchange CPMG without Mg2+; expectation-maximization simulated annealing on minor-state PCSs [paper, Figs 1–3; ED Figs 2–4; SI Methods].

8. **Exchange parameters** — Two-state Carver–Richards global fits: Zn2+ kex 1,355 ± 65 s−1, Co2+ 1,367 ± 71 s−1; joint kex 1,428 ± 83 s−1, pB 12.6 ± 2.5%; k_open 180 ± 36 s−1 [paper, Results; SI Fig. 1; ED Fig. 3c]; k_close ≈ 1,250 s−1 [our reading of the paper's data]. Without Mg2+, k_open ≈ 2 s−1 (2.6 ± 0.3) [paper, ED Fig. 3]. 103/186 residues have Rex > 3 Hz [paper, Results]. 1H_N |Δδ| ≈ 0–0.3 ppm (residue 38: ΔδZn 0.02, ΔδCo 0.24 ppm; diamagnetic mean ≈ 0.05 ppm) [paper, Fig. 1f,g; Methods]; ΔPCS(minor − major) ≈ −0.22 to +0.09 ppm [our reading of Fig. 3b].

9. **Residues or regions** — Global dispersion; largest minor-state PCS change in the AMP lid (rigid bodies 32–55, 62–79); slight ATP-lid (128–157) motion [paper, Results; Methods]. Amides ~130–170 near the metal give no restraints (paramagnetic broadening) [our reading of Fig. 3a; ED Fig. 1].

10. **Identity basis** — Structure computed directly from 93 minor-state PCS restraints (Q = 3.7%) after expectation maximization resolves the four-fold sign ambiguity [paper, Fig. 3a]; the method recovered 12 simulated Adk states (90 ± 8% correct PCS) independent of starting structure [paper, Fig. 2; ED Figs 5–7]. Naming it the rate-limiting lid-opening/product-release state relies on k_open ≈ kcat and the Mg2+ dependence from earlier work (ref. 25) [paper, Introduction; ED Fig. 3].

11. **Structural mapping and simulations** — Closed reference/start 4QBH; open reference 4AKE (*E. coli*) [paper; ED Figs 4, 6]; 4QBH is a stabilized multi-mutant variant with Ap5A, Mg2+, Zn2+ [our reading of PDB 4QBH]. Benchmarks: 12 homology-modelled Adk structures [paper, Methods; Fig. 2f]. XPLOR-NIH rigid-body annealing is refinement; no molecular-dynamics sampling of the Adk minor state is reported; metadynamics (ref. 43) is cited as consistent [paper, Methods; Discussion].

12. **Functional relevance** — Minor state described as primed for substrate binding or product release; lid opening (k_open ≈ kcat) is rate-limiting [paper, Introduction; Results; Fig. 3e]. Proposed mechanism: nucleotides select a partially closed state, then induced fit to full closure [paper, Fig. 3f]. Support is literature consistency (lid cross-linking tightens affinity, ref. 42; transition-state ensemble halfway to this state, ref. 44); no new mutants, binding or activity data [paper, Discussion].

13. **Competing explanations addressed** — Metal motion: identical Zn2+/Co2+ kex; RDC- and PCS-derived tensors agree [paper, Results; ED Fig. 2d]. Full opening (earlier chemical-shift model; smFRET): Δδ_para smaller than predicted from open vs closed crystal structures and than apo-vs-saturated PCS differences; ATP-lid metal moves only 1.8 Å [paper, ED Fig. 4; Discussion]. Sign ambiguity and starting-model bias: benchmarks, open vs closed starts, likelihood–r.m.s.d. correlation, leave-one-out uncertainties [paper, ED Figs 5–7; Methods]. Not tested: three-state exchange, multi-field fits, direct nucleotide occupancy of the minor state [our reading of the paper's data].

14. **What this evidence cannot support** — That the partially open state exists in nucleotide-free Adk, or that conformational selection is demonstrated; side-chain or ATP-lid internal detail; mutational proof of function; a trigger-factor minor-state population or structure (fast exchange, kex ≈ 3,000 s−1); experimental calmodulin or Src structures (simulated only) [paper, Results, Fig. 4; inference].

15. **Provenance** — DOI 10.1038/s41586-022-04468-9 (PMC9126080); Figs 1–3; ED Figs 1–4; SI Table 1; SI Fig. 1 (legend kex ± 31 s−1, text ± 83 s−1). BMRB 51232 (Zn2+), 51233 (Co2+) amide assignments, both listing 2 mM Adk, 20 mM ADP, pH 7.0, 298 K, 600 MHz, no Mg2+ [our reading of BMRB]; BMRB 27239, 15410 (trigger factor, ubiquitin). PDB 4QBH, 4AKE; benchmarks 2EU8, 2AKY, 1ZIP, 2BBW, 2AK3, 2AR7, 1DVR, 2RH5; simulations 1CLL/1PRW, 2SRC/1Y57.

## PART 2 — MUST-GET-RIGHT

- **Verdict and the apo-defining ligand.** Not included. Apo is relative to nucleotides (ATP/AMP/ADP, with Mg2+ as cofactor). The high-energy state was detected only with 20 mM ADP + 20 mM MgCl2, and the authors conclude it is occupied by substrate or product (Results, high-energy structure section; Methods, NMR spectroscopy). Rating the closed/partially open pair Strong or Weak, or treating Zn2+/Co2+ as the apo-defining ligand, is wrong. Listing the Fig. 3f apo partially closed state separately as a Candidate, with apo PCS–CPMG as the next measurement, is acceptable.
- **States and populations.** Major: fully closed, nucleotide-bound, 4QBH-like, ≈87%. Minor: partially open, pB = 12.6 ± 2.5% (Results; SI Fig. 1).
- **Kinetics and conditions.** Joint kex = 1,428 ± 83 s−1 (Zn2+ 1,355 ± 65; Co2+ 1,367 ± 71); k_open = 180 ± 36 s−1; 1H_N CPMG at 600 MHz, 25 °C, pH 7.0. Without Mg2+, exchange becomes slow (k_open ≈ 2 s−1) (Results; ED Fig. 3; Methods).
- **Shape of the minor state.** Partially, not fully, open: AMP lid ~15° (~50%), ATP-lid metal shift ~1.8 Å, r.m.s.d. 2.67 Å to closed vs 7.03 Å to open (Results; Fig. 3c–e; SI Table 1).
- **Identity basis.** Minor-state PCSs come from paired Zn2+/Co2+ dispersion. The four-fold sign ambiguity is resolved by expectation-maximization simulated annealing (93 residues, Q = 3.7%), benchmarked on 12 simulated Adk states (90 ± 8% correct PCS) (Fig. 2; Fig. 3a; ED Figs 5–7). Identifying it as the rate-limiting lid opening leans on prior work (ref. 25).
- **Apo evidence is thin.** Nucleotide-free Adk has HSQC data only: weakened PCSs (fit to closed structure Q = 47.9%) and PCS-induced line broadening, read as an open ensemble. There is no CPMG, kex or pB for apo Adk (Results; ED Figs 2c, 4).
- **The minor state is not the apo open state.** Δδ_para is smaller than predicted for closed→open (4AKE) and smaller than the measured apo-vs-saturated PCS differences (Results; ED Fig. 4).
- **Metal-motion control.** The same kex with Zn2+ and Co2+ shows the metal moves only with the lid; RDC- and PCS-derived tensors agree (Results; ED Fig. 2d).
- **Functional link.** Lid opening is rate-limiting (k_open ≈ kcat); the minor state is primed for substrate binding or product release (exit tunnel, Fig. 3e); the conformational-selection-then-induced-fit mechanism is proposed (Fig. 3f). The paper has no mutants or activity assays; the Discussion cites refs 42–44 as consistent.
- **Provenance and scope.** DOI 10.1038/s41586-022-04468-9; BMRB 51232 (Zn2+) and 51233 (Co2+); PDB 4QBH (closed start) and 4AKE (open); no PDB entry for the minor state (Data availability). Ubiquitin is a no-millisecond-motion control; trigger factor PPD–SBD exchange was too fast (kex ≈ 3,000 s−1) for pB or minor-state PCSs; calmodulin and Src are simulated (Fig. 4; Results).

## PART 3 — OVER-CLAIMS

- **Claim: apo Adk samples the partially open state at ~13%.** The 12.6% was measured at saturating Mg2+-ADP, the authors treat the state as nucleotide-occupied, and no dispersion was measured without nucleotide.
- **Claim: the paper demonstrates conformational selection for nucleotide binding.** The abstract presents the two-step mechanism as a suggestion and Fig. 3f labels it proposed; no binding kinetics, apo exchange data or mutants test it.
- **Claim: the high-energy state is the open, 4AKE-like conformation with both lids fully open.** The central result is the opposite: partially open, 2.67 Å from closed vs 7.03 Å from open. The earlier full-opening model and the smFRET large-ATP-lid model are rejected.
- **Claim: an atomic-resolution minor-state structure was solved and deposited.** It is a rigid-body domain model from ~93 amide 1H PCSs. ATP-lid amides near the metal are missing, accuracy is estimated from simulations (<3.5 Å), and there is no PDB accession.
- **Claim: bound Mg2+-ADP was directly observed in the minor state.** Occupancy is inferred from saturation (20 mM ADP vs KM ≈ 50 μM). Which nucleotides (ADP or ATP/AMP) occupy it is not resolved.
- **Claim: mutants or activity assays confirm that the minor state controls catalysis.** The paper has no mutants or activity assays; the link rests on k_open ≈ kcat and cited literature (refs 25, 42–44).
- **Claim: PCS–CPMG solved high-energy structures for trigger factor, calmodulin and Src.** Trigger-factor exchange (kex ≈ 3,000 s−1) was too fast to extract pB or minor-state PCSs; calmodulin and Src were synthetic datasets.
- **Claim: these kinetics describe Adk in general, without Mg2+, at other temperatures or with more than two states.** The fits are two-state, at one field (600 MHz) and 25 °C, with Mg2+-ADP; removing Mg2+ slows k_open about 70-fold.

## ERRATA AFTER INDEPENDENT CHECK (applied before grading)

A separate checker compared this reference with the paper, its Supplementary Information and the cited BMRB and PDB records (see CHECK_STILLER22.md). No corrections were needed; the "Not included" verdict and the "apo relative to" field were judged defensible, and no over-claim item turned out to be supported by the paper. One note:

- Over-claim 5: the legend of Fig. 3c labels the modeled ligand spheres as "two ADP substrates". The checker judged this a rendering choice consistent with the ADP-only sample, not restraint data on the nucleotide, so the over-claim stands; an entry that cites the legend's wording is quoting the paper.
