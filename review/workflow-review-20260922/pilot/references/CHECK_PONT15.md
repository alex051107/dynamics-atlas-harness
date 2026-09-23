# CHECK_PONT15 — verification of REF_PONT15 against Pontiggia et al. 2015 (Nat Commun 6:7284)

Method: full text pulled from the PMC page (PMC4470301, rendered HTML converted to plain text,
1614 lines) after the EuropePMC XML endpoint returned HTTP 500 on repeated tries. Six main-figure
JPEGs (Figs 1–6) were pulled from the PMC image CDN and read visually to check axis/residue labels
not present in the running text. The Supplementary PDF was unreachable at the PMC `bin/` URL (Google
reCAPTCHA challenge page — not attempted further, per the no-CAPTCHA rule) but was obtained instead
from the publisher's own CDN (media.springernature.com, linked from the Nature Communications page
for the same DOI) and read in full (10 pages, Supplementary Figs 1–5 with captions). PDB 2MSL/2MSK
were queried at data.rcsb.org and BMRB 25125/25124 at api.bmrb.io, both cited by the paper's own
Accession-codes line and by REF_PONT15 itself.

Status legend: CONFIRMED / WRONG / NOT FOUND / SI ONLY / NOT CHECKED / DISPUTED.

## A. Part 2 — must-get-right

| # | Reference statement | What the paper says | Locator | Status |
|---|---|---|---|---|
| A1 | Apo = unphosphorylated NtrC^R; alternative apo state is the active conformer; not "unphosphorylated vs phosphorylated protein" | "NtrC^R exists in its apo form in a mixed equilibrium of its active and inactive states... shifted upon phosphorylation of aspartate 54" | Introduction | CONFIRMED |
| A2 | Verdict "strong," source of exchange numbers flagged | Rate/population stated with citations (refs 11–13/12–13), no new exchange experiment in this paper | Introduction; Results | CONFIRMED (see §C) |
| A3 | ≈13,000 s⁻¹ and ≈15% both cited; no CPMG/R1ρ/CEST/ZZ data, no chemical-shift differences | "interconversion rate of approximately 13,000 s⁻¹ 11,12,13"; "about 15% of the active state is sampled 12,13"; no exchange-experiment keyword anywhere in body text | Introduction; Results | CONFIRMED |
| A4 | MSM numbers are simulation outputs, not measurements; slowest process ≈100 μs, imprecise; macrostates ≈52%/48%, not assigned to A/I; A ≈5% of 2168 microstates by count ≠ population | "precise estimate of the slow interconversion rate is not possible"; "similar populations (about 52% and 48%)" (no A/I assignment given); "approximately 5% of the 2168 microstates are assigned to A" | Results, "The active and inactive states are kinetically defined" and "Homogeneous active versus heterogeneous inactive state" | CONFIRMED |
| A5 | Simulation came first (string → MSM → Anton), predictions tested by new 35 °C NMR (2MSL/2MSK, helicity, NOEs); NMR models relaxed by MD and compared to measured S²; no exchange experiment run | Matches Results narrative order and "NMR experiments support the free energy landscape model" section | Results; Fig. 5; Supplementary Fig. 5 | CONFIRMED |
| A6 | States differ by α4 rotation; Y94–α3 in I, Q96–α3 in A; apo α4 partial helicity to Q96 (old model stopped at Y94); F99 does not switch in new structures | "Y94 is close to helix 3 only in I, while Q96 is only close to helix 3 in A"; "α4 partially extends up to Q96, whereas in the previous inactive model... it ended at Y94"; "the side-chain of F99 does not change position between the two states" | Figs 2C–I, 5C–E; Supplementary Fig. 5B | CONFIRMED |
| A7 | 2MSL = apo, deposited as inactive state, population average incl. ~15% A; 2MSK = BeF3−-activated; no structure of apo minor state solved, mapped to 2MSK/simulated A | Accession codes: "2MSL (NtrC^R inactive state) and 2MSK (NtrC^R active state)"; "about 15% of the active state is sampled" in the apo NMR sample | Accession codes; Fig. 5; Supplementary Fig. 5A | CONFIRMED |
| A8 | I heterogeneous / A homogeneous, both kinetically defined; I sub-states interconvert in a few μs (up to ~10 μs); some I conformers within 2.5 Å RMSD of A; heterogeneity is force-field dependent (CHARMM27 vs Amber99SB) | "these sub-states can interconvert on timescales of the order of a few microseconds" (Discussion); "reaching up to 10 microseconds" (Results, "Comparison..."); "backbone RMSD's as close as 2.5Å" (Results); force-field attribution stated explicitly | Figs 2A, 4D, 6; Results; Discussion | CONFIRMED |
| A9 | Phosphorylation of D54 by NtrB stabilizes A, propagates signal, activates nitrogen-starvation genes (refs 13,15); earlier H-bond mutants raised barrier without changing I/A (ref 13); no functional assay here | "upon phosphorylation by its cognate histidine kinase NtrB, activates the transcription of genes in response to nitrogen starvation"; "shifted upon phosphorylation of aspartate 54... promotes propagation... 13,15"; "increase in the activation barrier without affecting I and A 13" | Introduction; Fig. 3 legend/text | CONFIRMED |
| A10 | Construct: WT *S. typhimurium* NtrC 1–124 (from PDB); NMR 35 °C, pH 6.75, 600/800 MHz; sims CHARMM27 300 K (MSM)/320 K (Anton); apo/BeF3− model has no phosphoryl/BeF3−/Mg²⁺ (inference) | PDB 2MSL polymer entity: 124 aa, 0 mutations, *Salmonella typhimurium* (rcsb_entity_source_organism); "All spectra were obtained at 35 °C"; BMRB 25125/25124 pH 6.75; Methods gives 300 K (string, MSM) and 320 K (Anton); no phosphoryl/BeF3−/Mg²⁺ terms found in Methods | PDB 2MSL/2MSK; BMRB 25125/25124; Methods | CONFIRMED |

## B. Part 1 — numbers, IDs, conditions, populations

| # | Field | Reference statement | What the paper/DB says | Locator | Status |
|---|---|---|---|---|---|
| B1 | 1. Protein | Species not stated in paper; UniProt not stated; PDB/SIFTS maps chain to A0A0M3KKS6 | No "Salmonella"/"typhimurium"/"UniProt" anywhere in body text (grep-confirmed); RCSB `polymer_entity/2MSL/1` → `rcsb_polymer_entity_align` gives SIFTS UniProt accession **A0A0M3KKS6** | PDB 2MSL entity 1 (data.rcsb.org) | CONFIRMED |
| B2 | 2. Construct | Residues 1–124, no mutations, WT | PDB 2MSL entity: `rcsb_sample_sequence_length: 124`, `rcsb_mutation_count: 0`; sequence not stated as such in paper body | PDB 2MSL/2MSK | CONFIRMED |
| B3 | 2. Conditions | Apo: 1 mM ¹³C/¹⁵N protein, 50 mM NaPhos, 50 mM NaCl, no Mg²⁺ | BMRB 25125 `sample_1`: Receiver Domain of NtrC [U-13C,15N] 1 mM; sodium phosphate 50 mM; sodium chloride 50 mM; no Mg component listed | BMRB 25125 | CONFIRMED |
| B4 | 2. Conditions | Activated: 0.3 mM protein, 4.4 mM BeCl₂, 29 mM NaF, 7.2 mM MgCl₂ | BMRB 25124 `sample_1`: protein 0.3 mM; beryllium chloride 4.4 mM; sodium fluoride 29 mM; magnesium chloride 7.2 mM | BMRB 25124 | CONFIRMED |
| B5 | 2. Conditions | NMR at 35 °C | "All spectra were obtained at 35 °C." | Methods, "NMR structure refinement" | CONFIRMED |
| B6 | 2. Conditions | pH 6.75 | BMRB 25125 & 25124 `sample_conditions_1`: pH 6.75 (both); PDB 2MSL/2MSK `pdbx_nmr_exptl_sample_conditions`: pH 6.75 (both) | BMRB/PDB records | CONFIRMED |
| B7 | 2. Conditions | 600 MHz (assignment) and 800 MHz cryoprobe (NOESY) | "Varian INOVA 600 MHz spectrometer"; "Bruker Avance II 800 MHz spectrometer with a TCI cryoprobe" | Methods | CONFIRMED |
| B8 | 2. Conditions | Cited exchange data from earlier 25 °C work | "In previous NMR experiments on NtrC^R recorded at 25°C 11,12,13,14..." | Results, "NMR experiments support..." | CONFIRMED |
| B9 | 2. Conditions | Sims: CHARMM27 300 K (strings, MSM), 320 K (Anton); no phosphoryl/BeF3−/Mg²⁺ described | String calcs both at "T = 300 K"; F@H MSM "Nose-Hoover thermostat to keep the temperature at 300 K"; Anton "Nose-Hoover thermostat at 320 K"; no phosphate/BeF3−/Mg²⁺ term anywhere in Methods (grep-confirmed) | Methods | CONFIRMED |
| B10 | 3. Apo relative to | D54 phosphorylation, mimicked by BeF3− | "shifted upon phosphorylation of aspartate 54"; Fig. 5 legend labels apo (2MSL) vs "BeF3− activated form" (2MSK) | Introduction; Fig. 5 legend | CONFIRMED |
| B11 | 4. Verdict numbers | ≈13,000 s⁻¹ citing refs 11–13; ≈15% citing refs 12,13 | "approximately 13,000 s⁻¹ 11,12,13" (Introduction); "about 15% of the active state is sampled 12,13" (Results) — ref sets are genuinely different (11–13 vs 12–13) | Introduction; Results | CONFIRMED |
| B12 | 5. Major state | Population ≈85% (labelled inference, complement of 15%) | Not itself stated by paper — correctly tagged [inference] | — | CONFIRMED (correctly tagged) |
| B13 | 5/6. Structures | 2MSL apo/inactive, 2MSK BeF3−/active | "deposited... under accession codes 2MSL (NtrC^R inactive state) and 2MSK (NtrC^R active state)" | Accession codes | CONFIRMED |
| B14 | 8. Exchange parameters | 100 μs slowest MSM process, imprecise estimate | "one single slow process occurring in about 100 μs"; "a precise estimate... is not possible" | Results, "kinetically defined"; Supplementary Fig. 2 | CONFIRMED |
| B15 | 8. Exchange parameters | Macrostates ≈52%/48%; 5% of 2168 microstates = A | "similar populations (about 52% and 48%)"; "approximately 5% of the 2168 microstates are assigned to A" | Results | CONFIRMED |
| B16 | 8. Exchange parameters | I sub-states interconvert "a few μs, up to ~10 μs" | Content confirmed ("a few microseconds," Discussion; "reaching up to 10 microseconds," Results) but **locator is wrong** — see §Corrections | Results ("Comparison of MSM models..."), not Discussion | **WRONG (locator only)** |
| B17 | 9. Residues | α4 (H84–Q96), α4–β5 loop; Y94, Q96, L87, S92, Q95, A98, F99, Y101, T82, K67 | All residues visually confirmed as labelled in Figs 1A, 2D/E, 3F/G axes, 4C/D, 5C/E, 6E (T82, S85D/G, Y94, Q96N, Y101F axis on Fig. 3F,G; D86/S85/L87/V91/Q96/Y94/A98/F99 in Fig. 1A; D88/L87/A90/V91/S92/Y94/Q95 in Fig. 5C; K67/Q95/Q96 in Fig. 6E) | Figs 1A, 2, 3F–G, 4C–D, 5C,E, 6 | CONFIRMED |
| B18 | 11. Simulations | 26 configs (Str1 input), 80 frames (Str2 input) | "extracting 26 protein configurations..."; "80 frames were extracted and used as input pathway" | Methods, "Pathway calculations" | CONFIRMED |
| B19 | 11. Simulations | 8,000 F@H runs; 1.015 ms collected; 978 μs used after filtering; 2,168 microstates; 50 ns lag; 2 or 10 macrostates | "8000 independent simulations"; "1.015 ms simulation time was collected"; "leaving a total of about 978 μs"; "resulted in 2168 microstates"; "lagtime of 50 ns"; two vs ten macrostates both described | Methods, "Markov State Model" | CONFIRMED |
| B20 | 11. Simulations | Anton ~21 μs from I, ~71 μs from A (extended), no A↔I transition | "two long, unbiased MD simulations (approximately 21 μs)"; "active state trajectory was extended to about 71 μs"; "No transitions to the inactive states are observed, even when extending... to ~71 μs" | Methods, "Long unbiased simulations on Anton"; Results | CONFIRMED |
| B21 | 11. Simulations | Old models = TMD end states, patched; PDB IDs not stated | "2 end structures of the TMD of Lei et al. were equilibrated, after being patched..."; no PDB code given for these old models anywhere (grep-confirmed: no other PDB ID besides 2MSL/2MSK appears in body text) | Methods | CONFIRMED |
| B22 | 15. Provenance | DOI 10.1038/ncomms8284; PMC4470301; NIHMS684984; PMID 26073309 | "PMCID: PMC4470301 NIHMSID: NIHMS684984 PMID: 26073309"; "doi: 10.1038/ncomms8284" | PMC page header | CONFIRMED |
| B23 | 15. Provenance | Figs 1–6, Table 1, Supp Figs 1–5 | Confirmed structure: 6 main figs, 1 table, 5 supplementary figs (all read in full) | whole paper + SI PDF | CONFIRMED |
| B24 | 15. Provenance | Table 1 NOE counts differ from Methods text | Methods: apo 984 long-range/2282 total; BeF3− 638 long-range/1866 total. Table 1: apo 922 long-range/2428 total; BeF3− 694 long-range/2226 total — all four figures differ from the Methods-text values | Table 1 vs Methods | CONFIRMED |
| B25 | 15. Provenance | BMRB 25125 (apo), 25124 (BeF3−), chemical shifts only, linked from PDB, not cited by paper text | BMRB IDs do not appear anywhere in paper body text (grep-confirmed); PDB 2MSL `rcsb_external_references`→BMRB 25125; PDB 2MSK→BMRB 25124; both entries contain only `assigned_chemical_shifts`, no coordinates saveframe of their own | PDB 2MSL/2MSK `pdbx_database_related`; BMRB 25125/25124 saveframe list | CONFIRMED |
| B26 | 15. Provenance | BMRB lists 273 K despite "35C" in the entry titles | BMRB 25125 title: "...Apo form... at 35C"; `sample_conditions_1` → temperature **273** K, units K. Same pattern in BMRB 25124 title "...BeF3 activated... at 35C" → temperature **273** K | BMRB 25125 & 25124, `sample_conditions_1` | CONFIRMED |

## C. Verdict and "Apo relative to" vs. tier definitions (task_common.md)

| Item | Reference statement | Assessment | Status |
|---|---|---|---|
| C1 | Verdict = Strong | Strong requires: (i) paper reports the alternative state, (ii) exchange data exist, (iii) ≥1 independent line of support, (iv) numbers traceable to the paper. All four hold here: the I/A equilibrium is reported with a rate and population (traceable to Introduction/Results even though the values originate in refs 11–13); independent support comes from the new BeF3− structure (2MSK), an MSM whose single slow timescale (~100 μs) is comparable to the cited rate, and the Y94/Q96–α3 NOE switch. Task_common.md's Weak tier is defined by a missing *identity*, *origin*, or *functional-link* piece — none of the three is missing here (identity: NOE + MSM markers; origin: D54 phosphorylation; functional link: refs 13/15 to downstream signalling). I agree the tier is defensible as written, given the reference explicitly flags the citation status of the exchange numbers as instructed. | CONFIRMED (defensible) |
| C2 | Apo relative to = D54 phosphorylation, BeF3− mimic | Matches the paper's own framing exactly (Introduction + Fig. 5 legend use apo vs. BeF3−-activated as the two conditions) | CONFIRMED |

## D. Part 3 — over-claims (paper should NOT support these)

| # | Over-claim | Does the paper support it? | Locator checked | Status |
|---|---|---|---|---|
| D1 | Paper measured I/A exchange (kex≈13,000 s⁻¹, 15% active) by relaxation dispersion | No — no CPMG/R1ρ/CEST/ZZ or any exchange-experiment term anywhere in the paper; both numbers carry citations to refs 11–13 | Introduction; Results; full-text grep | Confirmed NOT supported |
| D2 | MSM shows ~5% (or ~48–52%) of apo NtrC^R is in the active state | No — "5%" is explicitly a count of microstates, not a population; 52/48 is never assigned to A or I | Results | Confirmed NOT supported |
| D3 | MSM gives the I→A rate, or "reproduces" the NMR rate | No — paper explicitly says a precise rate estimate "is not possible"; only calls the timescale "comparable" | Results | Confirmed NOT supported |
| D4 | 2MSK is the apo minor-state structure, or 2MSL is a "pure" inactive structure | No — 2MSK is explicitly the BeF3−-activated structure; 2MSL is explicitly an ensemble average of a sample where "about 15% of the active state is sampled" | Fig. 5 legend; Results | Confirmed NOT supported |
| D5 | NMR "detected" several alternative inactive sub-states | No — sub-states come from the MSM/simulations, are shown to be force-field-dependent (CHARMM27 vs Amber99SB), and NMR support is only indirect (helicity, NOEs, MD-relaxed models) | Results, "Comparison..."; Supplementary Fig. 5C | Confirmed NOT supported |
| D6 | Inactive = unphosphorylated protein, active = phosphorylated protein | No — both states explicitly coexist in the unphosphorylated (apo) protein; phosphorylation only shifts the population | Introduction | Confirmed NOT supported |
| D7 | Multiple pathways / nonnative H-bonds / barrier lowering shown experimentally; Anton captured A↔I transitions | No — these are MSM/committor/simulated-trajectory results (Fig. 3); Anton runs explicitly show "No transitions to the inactive states are observed" even at ~71 μs; Fig. 2J is stated to be a kinetic-Monte-Carlo meta-trajectory from the MSM, not a measured trace | Results | Confirmed NOT supported |
| D8 | The two states have no structural difference; findings generalize to all signalling proteins | No — extensive structural difference (α4 rotation, Y94/Q96 switch) is the paper's central finding; generality is explicitly hedged as "may be general features," stated as a closing speculation, not a result | Abstract; Discussion | Confirmed NOT supported |

## Corrections needed

- **B16 / Part 1, item 8** — "I sub-states interconvert in a few μs, up to ~10 μs" is correctly stated, but its locator `[paper; Discussion; "Comparison of MSM models…"]` is wrong. "Comparison of MSM models started from string and end-states" is an h3 subsection of **Results** (it sits between the "NMR experiments support..." subsection and the Fig. 6 legend, all still under the Results h2, and ends immediately before the separate Discussion h2 begins — confirmed from the page's heading hierarchy, not just running prose). The "up to 10 microseconds" figure appears only in that Results subsection. The Discussion does separately paraphrase "a few microseconds" (without the ~10 μs figure or the subsection name), so the correct locator is **[paper; Results, "Comparison of MSM models started from string and end-states"]**, with the Discussion citable only for the shorter "a few microseconds" restatement.

No other numeric, ID, condition, or population value in Part 1 was found wrong; no Part 2 item was found wrong; the Verdict and "Apo relative to" tier calls are both defensible from the paper.

## Over-claim items the paper actually supports

none
