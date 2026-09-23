# CHECK_STILLER22 — verification of REF_STILLER22.md against Stiller et al. 2022 *Nature* 603:528–535

Sources used: NCBI/PMC full-text XML (NIHMS1802544, author manuscript, identical scientific content to
the VoR), the article's Figs. 1–4 (full-resolution JPGs served from PMC), Extended Data Figs. 1–10
(captions in the manuscript XML), the Supplementary Information PDF (NIHMS1802544-supplement, 13 pp.:
Methods, Supplementary Table 1, Supplementary Figs. 1–5), BMRB entries 51232, 51233, 27239 (api.bmrb.io),
and PDB entries 4QBH, 4AKE (data.rcsb.org). No web search was used; no other paper was read. The Europe
PMC `fullTextXML` endpoint 500'd repeatedly, so the NCBI eutils mirror was used instead — same manuscript,
confirmed by matching DOI/PMCID/author list. A stray, unrelated PDF ("abc_2754_Supplementary_Materials",
a *Science* paper) briefly appeared in the browser's PDF viewer once after a scroll action; it was not
read or used for anything below — I re-navigated to the correct SI PDF and re-verified the page count (13)
and content before continuing.

## A/B. Part 2 (must‑get‑right) and Part 1 numbers/IDs/conditions/populations

### A. Part 2 must-get-right bullets

| # | Reference statement | Paper says (quote/paraphrase) | Locator | Status |
|---|---|---|---|---|
| 1 | Verdict "Not included"; apo = nucleotide-free; state only detected at saturating Mg-ADP | "the high-energy state must be occupied with substrate or product" | Results, high-energy-structure paragraph; Methods, NMR spectroscopy | CONFIRMED |
| 2 | Major: closed, 4QBH-like, ≈87%. Minor: partially open, pB = 12.6 ± 2.5% | "population of the high-energy state (pB) of 12.6 ± 2.5%" | Results (PCS–CPMG of Adk section) | CONFIRMED |
| 3 | Joint kex 1,428 ± 83 s⁻¹ (Zn 1,355±65; Co 1,367±71); k_open 180±36 s⁻¹; 600 MHz, 25 °C, pH 7.0; no-Mg k_open≈2 s⁻¹ | "kex, of 1,428 ± 83 s⁻¹"; "kopen = 180 ± 36 s⁻¹"; "kopen,ADP = 2.6 ± 0.3 s⁻¹" | Results; Methods, NMR spectroscopy; ED Fig. 3 | CONFIRMED |
| 4 | Partially, not fully, open: AMP lid ~15° (~50%), ATP-lid metal ~1.8 Å, r.m.s.d. 2.67 Å closed vs 7.03 Å open | "AMP lid opens by about 15°, corresponding to approximately 50% opening"; "r.m.s.d.closed = 2.67 Å versus r.m.s.d.open = 7.03 Å" | Results; Fig. 3c–e; SI Table 1 | CONFIRMED |
| 5 | 93-residue PCS restraints, Q=3.7%, 4-fold sign ambiguity resolved by EM-annealing; benchmarked on 12 simulated states, 90±8% correct; identity leans on ref. 25 | "correct PCS found for 90 ± 8% of residues"; "yielding 93 residues for the refinement procedure...(Q = 3.7%)" | Results ("Benchmarking..." and "Structure of the high-energy state" sections); Fig. 2c,d; Fig. 3a | CONFIRMED |
| 6 | Apo Adk: HSQC only, Q=47.9% fit, no CPMG/kex/pB | "fit significantly worse (Q = 47.9%) to the closed state" | ED Fig. 2 legend (panel c) | CONFIRMED |
| 7 | Minor state ≠ apo-open state: Δδpara smaller than 4AKE-predicted and smaller than apo-vs-saturated PCS diff | "observed Δδpara is less than would be expected from known open...and closed...crystal structures" | Results; ED Fig. 4 | CONFIRMED |
| 8 | Same kex for Zn/Co ⇒ metal moves only with lid; RDC- and PCS-tensors agree | "equivalent exchange processes seen for the diamagnetic and paramagnetic species"; ED Fig. 2d: RDC- and PCS-tensors "provide similar tensor values" | Results; ED Fig. 2d | CONFIRMED |
| 9 | Functional link: k_open≈kcat, primed for substrate/product, conformational-selection-then-induced-fit is proposed; refs 42–44 cited, no new mutants/activity data | Fig. 3f caption: "**Proposed** mechanism for substrate binding and product release..."; Discussion cites ref. 42 (lid cross-links "tightens the affinity for substrates") and ref. 44 (transition state "coincides halfway") | Introduction; Results; Fig. 3e,f; Discussion | CONFIRMED |
| 10 | DOI; BMRB 51232 (Zn)/51233 (Co); PDB 4QBH/4AKE; no PDB for minor state; ubiquitin/trigger-factor/calmodulin-Src controls as described | "deposited in the BioMagResBank...under accession codes 51232 and 51233"; no PDB ID given for the minor-state model anywhere in the paper | Data availability; Methods | CONFIRMED |

### B. Additional Part 1 numbers, IDs, conditions and populations (not already covered above)

| Item | Reference statement | Paper/database says | Locator | Status |
|---|---|---|---|---|
| 1 | UniProt not stated in paper | No occurrence of "UniProt" anywhere in full text | Whole-text search | CONFIRMED |
| 1 | PDB 4QBH maps to UniProt P27142 | SIFTS mapping: `reference_database_accession: "P27142"`, full coverage | data.rcsb.org polymer_entity 4QBH/1 | CONFIRMED |
| 1 | Trigger factor PPD–SBD is *E. coli* | `Organism_name_scientific: "Escherichia coli"` (NCBI taxid 562), entity `$TF` | api.bmrb.io entry 27239, natural_source loop | CONFIRMED (paper's own running text never states the organism for PPD–SBD; this rests on the BMRB record the paper cites, as the reference itself flags) |
| 2 | WT, no mutations stated; C-terminal TEV site + His6 | "cloned into the plate-11 vector with a C-terminal TEV cleavage site and His6-tag" | Methods, protein expression and purification | CONFIRMED |
| 2 | Deposited sequence 223 aa, ends "...ENLYFQ" | `Polymer_seq_one_letter_code` = 223 residues, last 10 = "GLARENLYFQ" (identical in both entries) | api.bmrb.io entries 51232 and 51233, entity_1 | CONFIRMED |
| 2 | 2 mM Adk, 50 mM MOPS, 50 mM NaCl, 2 mM TCEP, pH 7.0 | "Adk samples were prepared at 2 mM enzyme in 50 mM MOPS, 50 mM NaCl, 2 mM TCEP...at pH 7.0" | Methods, NMR spectroscopy | CONFIRMED |
| 2 | 1H_N CPMG, 25 °C, 600 MHz only, 24 ms CT, 16 νCPMG 83–1,500 Hz | "24 ms constant-time relaxation period with 16 vCPMG frequencies ranging from 83 to 1,500 Hz for Adk"; "performed at 25 °C"; "Agilent DD2 600 MHz" | Methods, NMR spectroscopy | CONFIRMED (only field strength used for Adk anywhere in the paper; the one "800 MHz" hit in the text is a generic background number in the Introduction, unrelated to any Adk experiment) |
| 3 | Apo = nucleotide-free; Zn/Co present in every sample, doesn't define apo | ED Fig. 2 fits PCS in "20 mM Mg²⁺ ADP (a), 20mM ADP (b), and apo (c)" — metal is the constant across all three | ED Fig. 2 legend | CONFIRMED |
| 6 | SI Table 1: AMP-lid angle 66.1±1.0° (Δ15.2±1.0°); Co²⁺–core Δ0.4±0.33 Å | Table row "AMP Lid Angle (°) 66.1 ± 1.0 / Δ 15.2 ± 1.0"; "Co²⁺-Core Distance (Å) ... Δ 0.4 ± 0.33" | SI Table 1 (SI p.5) | CONFIRMED (exact) |
| 6 | Fig. 3c shows "top five" structures | "The top five highest likelihood structures of the minor state..." | Fig. 3c legend | CONFIRMED |
| 6 | No PDB accession for the minor-state model | Data-availability paragraph lists only BMRB 51232/51233; no PDB ID for any Adk minor-state coordinate set | Data availability | CONFIRMED |
| 8 | Residue 38: ΔδZn 0.02, ΔδCo 0.24 ppm; diamagnetic mean ≈0.05 ppm | Fig. 1f panel "38ₕₙ": "Δδ_Zn = 0.02 ppm" / "Δδ_Co = 0.24 ppm"; Methods: diamagnetic shifts sampled from "an exponential distribution with a mean of 0.05 ppm, which matches...Adk" | Fig. 1f; Methods, benchmarking section | CONFIRMED (exact) |
| 8 | ΔPCS(minor−major) ≈ −0.22 to +0.09 ppm | Fig. 3b bar plot: tallest positive bar ≈ +0.09–0.10 ppm, deepest negative bar ≈ −0.20 to −0.22 ppm (read directly off the axis gridlines at 0.1/0/−0.1/−0.2) | Fig. 3b | CONFIRMED (visual read, consistent with reference's own "our reading" tag) |
| 9 | Amides ~130–170 near the metal give no restraints | Fig. 3a's residue axis has a hard break with no data plotted between ~residue 125 and ~175, coinciding with the ATP-lid/metal region (128–157); ED Fig. 1: "many residues surrounding the metal binding site are lost due to...Curie relaxation or exchange" | Fig. 3a axis break; ED Fig. 1 legend | CONFIRMED |
| 11 | 4QBH = stabilized multi-mutant with Ap5A, Mg²⁺, Zn²⁺ | `pdbx_mutation: "34 mutations"`; title "Crystal structure of a stable adenylate kinase variant AKlse5"; `nonpolymer_bound_components: ["AP5","MG","ZN"]` | data.rcsb.org entry/polymer_entity 4QBH | CONFIRMED (exact) |
| 11 | 4AKE = open reference, *E. coli* | `pdbx_gene_src_scientific_name: "Escherichia coli"`; no ligands; UniProt P69441 | data.rcsb.org polymer_entity 4AKE/1 | CONFIRMED (again, organism is PDB metadata, not paper prose — same caveat as trigger factor above) |
| 11 | 12 homology-modelled Adk benchmark structures; PDB codes 2EU8, 2AKY, 1ZIP, 2BBW, 2AK3, 2AR7, 1DVR, 2RH5 (+4AKE) | "homology models...produced with the SWISS-MODEL software...2EU8B, 2AKYA, 1ZIPA, 2BBWB, 2AK3A, 2BBWA, 2AR7B, 1DVRA, 2RH5A, 4AKEB, 4AKEA" (11 chains + 4QBH start = 12) | Methods, benchmarking PCS–CPMG section | CONFIRMED |
| 11 | Simulations: calmodulin 1CLL/1PRW; Src 2SRC/1Y57 | "extended conformation...(PDB 1CLL71)...compact structure...(PDB 1PRW35)"; "closed conformation of Src...(PDB 2SRC72)...open structure...(PDB 1Y5736)" | Methods, benchmarking PCS–CPMG section | CONFIRMED |
| 15 | BMRB 51232/51233: 2 mM Adk, 20 mM ADP, pH 7.0, 298 K, 600 MHz, no Mg²⁺ | sample_conditions loop: pH 7.0, 298 K; sample loop: 2 mM Adk, 20 mM ADP, no Mg component; NMR_spectrometer: Agilent DD2, 600 MHz | api.bmrb.io entries 51232, 51233 | CONFIRMED (exact, both entries) |
| 15 | SI Fig. 1 legend gives kex ± 31 s⁻¹, vs. ± 83 s⁻¹ in the main text | Legend: "kₑₓ = 1428 ± 31 s⁻¹; pB = 12.6 ± 2.5%" vs. Results: "kex, of 1,428 ± 83 s⁻¹" | SI Fig. 1 legend (SI p.6); Results | CONFIRMED — genuine internal inconsistency in the paper, correctly caught by the reference |

## C. Verdict and "Apo relative to" against the tier definitions

**Agree with "Not included."** The task's own "Not included" tier example is "it was only measured with
substrate bound" — that is exactly this case: the only alternative state with kinetics/population/structure
(pB=12.6%, kex, PCS-derived model) was measured under 20 mM Mg²⁺-ADP, and the paper itself states the state
"must be occupied with substrate or product" (Results). The nucleotide-free condition has HSQC PCS fits only
(Q=47.9%, ED Fig. 2c), with no CPMG, kex or pB — so there is no apo exchange data to grade as Strong/Weak/
Candidate. "Apo relative to" nucleotides (ATP/AMP/ADP, Mg²⁺ as cofactor) is correct and explicit in the paper
(ED Fig. 2 legend distinguishes Mg-ADP/ADP/apo conditions; Zn²⁺/Co²⁺ is constant across all three and is
never treated as the apo-defining ligand anywhere in the text).

## D. Part 3 over-claims — does the paper actually support any of them?

| # | Claim | Paper's actual position | Locator | Status |
|---|---|---|---|---|
| 1 | Apo Adk samples the partially open state at ~13% | pB=12.6% measured only under saturating Mg-ADP; apo has no dispersion data at all | Results; ED Fig. 2c | Confirmed unsupported |
| 2 | Paper demonstrates conformational selection | Fig. 3f legend: "**Proposed** mechanism..."; abstract: state "**suggests** a two-step mechanism" | Fig. 3f legend; Abstract | Confirmed unsupported |
| 3 | High-energy state = fully open, 4AKE-like | "ATP lid moves only slightly (1.8 Å)"; r.m.s.d. 2.67 Å (closed) vs 7.03 Å (open) — explicitly rejects the earlier full-opening/smFRET model | Discussion; Results | Confirmed unsupported |
| 4 | Atomic-resolution structure solved and deposited | Rigid-body domain model from 93 backbone-amide PCSs; no PDB accession exists | Data availability; Methods | Confirmed unsupported |
| 5 | Bound Mg²⁺-ADP directly observed in the minor state | Occupancy is inferred from saturation ("[ADP] = 20 mM,...KM,ADP ≈ 50 μM"); only protein-backbone amide PCSs are used as restraints, no nucleotide-specific restraint | Results | Confirmed unsupported — **with one nuance**: Fig. 3c's legend does explicitly label the modeled ligand spheres as "two ADP substrates," so the figure is not agnostic about which nucleotide is drawn. This is a rendering choice consistent with the experimental design (only ADP was in the sample), not a new structural observation restraining nucleotide identity — no PCS restraint in the paper is on a nucleotide atom. Doesn't rise to the paper "supporting" the over-claim, but worth knowing if grading this point strictly. |
| 6 | Mutants/activity assays confirm the minor state controls catalysis | No Adk mutant or activity-assay data anywhere in Methods/Results; link rests on kopen≈kcat plus refs 25,42–44 | Methods; Discussion | Confirmed unsupported |
| 7 | PCS–CPMG solved structures for trigger factor, calmodulin, Src | Trigger factor: "kex ≈ 3,000 s⁻¹, which prevented...determination of the minor-state pseudocontact shifts"; calmodulin/Src are simulated datasets only (Fig. 4a–d) | Results (PCS–CPMG using a lanthanide-binding tag section) | Confirmed unsupported |
| 8 | These kinetics generalize (no-Mg, other temps, >2 states) | Two-state Carver–Richards, 600 MHz only, 25 °C, with Mg-ADP; removing Mg²⁺ drops kopen ~69-fold (180/2.6) | Results; Methods; ED Fig. 3 | Confirmed unsupported |

## Corrections needed

None. Every checked value, ID, condition and locator in Part 1 and Part 2 matched the paper, its Supplementary
Information, or the BMRB/PDB records it cites — including several fine-grained numbers that could easily have
been mistyped (residue-38 Δδ values, the exact SI Table 1 figures, the 223-residue/ENLYFQ BMRB sequence, and
the SI-legend-vs-main-text kex discrepancy, which the reference correctly flagged rather than "fixed").

## Over-claim items the paper actually supports

None. All seven Part 3 items remain correctly identified as claims the paper does not make or actively
contradicts. One is worth a light annotation rather than a flag: over-claim 5's rebuttal ("which nucleotides
occupy it is not resolved") is defensible, but Fig. 3c's own legend does name the modeled ligand as "two ADP
substrates" — a labeling choice, not new restraint data, so it does not amount to the paper supporting the
over-claim.
