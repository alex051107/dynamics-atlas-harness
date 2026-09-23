# Paper Trace: De Paula et al. 2020 (IL-2 capping switch)
Source: local PMC full-text HTML, parsed to text. SI Appendix not opened; described only from main-text citations.

## 1. PAPER
De Paula VS et al. "Interleukin-2 druggability is modulated by global conformational transitions controlled by a helical capping switch." *PNAS* 117(13):7183–7192 (2020). DOI 10.1073/pnas.2000419117.

Protein: mouse IL-2 (mIL-2, "a model system"), WT + R52A. Partners: antibody JES6-1 (scFv), receptor IL-2Rα, small molecule Ro 26-4550. Construct (range/tags/host) and NMR sample buffer/pH: not stated.

Conditions: 25 °C for CPMG/HMQC (600/800 MHz); 10 °C for CEST; ITC at 293 K, 20 mM phosphate pH 7.2, 150 mM NaCl.

Alternative state = a minor (~8%) excited conformation free mIL-2 samples at equilibrium, detected only indirectly (CPMG/CEST "invisible minor state," not a visible peak). Is an alternative APO state: present unliganded, resembling the antibody-bound "open" form, pre-existing and later selected by a partner (Abstract; "Free mIL-2 Samples..." §).

## 2. DATA & AVAILABILITY
Data types: HMQC titrations; ¹³C methyl CPMG; ¹³C-CEST; 3D NOESY; TITAN line-shape fitting; qualitative ¹H-¹⁵N TROSY (amides too broadened); SEC-MALS; Rosetta homology + rotamer enumeration (not MD); ITC; STAT5 assay. No new X-ray/cryo-EM or MD (§7).

Accessions (refs. 25–27,36), chemical-shift **assignments only**, not rate data: BMRB 27969 (free WT), 27970 (+JES6-1), 27971 (+IL-2Rα), 27974 (R52A).

PDB cited, all pre-existing: 4YQX (mIL-2/JES6-1), 2B5I (human IL-2/IL-2Rα template), 1M47 (apo human IL-2, "closed" template), 1M48 (human IL-2/Ro 26-4550 cocrystal).

Public: the 4 BMRB lists + 4 PDB entries. Figure/SI-only: raw CPMG/CEST curves, per-residue kex/pE/Δω (Figs. S3–S5, Table S1), NOE distances (Table S2), ITC table (Table S3), rotamer figures (S8–S9) — all in one SI PDF, not opened.

## 3. WORKFLOW TRACE
1. **Assign & QC free protein** — MILV + stereospecific Iδ1/proS-L,V labeling; SEC-MALS (clean, well-probed?) → 60 methyls assigned, strictly monomeric → methyls become the primary probe. [Results "Long-Range Effects..."; SI Fig. S1] EXPLICIT.
2. **Map bound-state effects** — HMQC titrations, free vs +JES6-1 vs +IL-2Rα (where do partners perturb structure?) → CSPs to 0.6 ppm, slow exchange, reach A/B/C/D helices past the AB loop → binding is not local. [Fig. 1 C–E] EXPLICIT.
3. **Free-protein amide spectrum fails** — 33% of amide peaks broadened past detection (does unliganded mIL-2 exchange on its own?) → pivot to methyl detection. [Results "Free mIL-2 Samples..." §] EXPLICIT.
4. **Quantify the exchange** — ¹³C-CPMG (25 °C, 20/60 methyls) + ¹³C-CEST (10 °C) (kex/population/Δω?) → global fit kex=1,000±72 s⁻¹, pE=8.0±0.4%; CPMG/CEST Δω correlate (2 outliers = temperature) → one cooperative process. [Fig. 2 A–C; SI Figs. S3–S5, Table S1] EXPLICIT.
5. **Assign the major state, propose a mechanism for the minor one** — NOE distances vs. 3 models (1M47, 4YQX, 2B5I-based) show the 92% ground state is "closed"; since de novo shift-based structure of the 8% state is unreliable, compare exchanging residues to the C-capping network unique to 4YQX instead → candidate switch: R52. [Fig. 2 F,G; Fig. 3 A–D; SI Table S2] EXPLICIT, partly on an EXPLICIT limitation.
6. **Test the switch causally** — repeat CPMG/CEST on R52A (does removing it quench exchange everywhere?) → quenched at every site; kex/population unfittable (no χ² minimum) — a quantitative failure read as qualitative confirmation. [Fig. 3 E,F; SI Figs. S3B,S5,S6] EXPLICIT.
7. **Attach function, replicate with an independent perturbation** — ITC+STAT5 (CTLL-2 cells) on WT/R52A+JES6-1; separately, NMR/TITAN/CPMG under Ro 26-4550 → R52A loses ~1,000-fold JES6-1 affinity (WT: ΔH=+12.7, −TΔS=−24.3 kcal/mol) and JES6-1-mediated suppression; ligand binds Kd=39.4±5.5 µM and dampens dispersion globally, like R52A. [Fig. 3 G,H; Fig. 5 A–D; SI Table S3, Fig. S7] EXPLICIT.
8. **Explain the coupling physically** — Rosetta rotamer-satisfiability, closed vs. open backbones (what links the loop to core CSPs >12 Å away?) → a defined residue path shows different rotamer sets between states (list §10). [Fig. 4 A–C; SI Figs. S8–S9] EXPLICIT result; INFERRED as the paper's chosen step to integrate stages 2+4+5.

## 4. DETECTION & CHARACTERIZATION OF THE ALTERNATIVE STATE
¹³C-CPMG (600/800 MHz, 25 °C) and ¹³C-CEST (800 MHz, 10 °C, B1=16.2 Hz) on MILV methyls, free WT; 20/60 assigned methyls usable. [Fig. 2A,B; SI Fig. S3A]

Fitted (global 2-site model): kex=1,000±72 s⁻¹; pE=8.0±0.4% (ground 92%); CPMG/CEST |Δω| correlate (Fig. 2C); largest |Δω| at the AB loop and B-helix/core sites (full residue list §10). [Fig. 2 C,D; SI Fig. S4]

Structural identity **not solved de novo** ("challenged by the ambiguity in interpreting methyl chemical shifts"). Inferred instead by: overlap of exchanging methyls (Fig. 2D) with methyls perturbed by binding (Fig. 1D,E); match to the C-capping network unique to 4YQX; causal quench with R52A and with Ro 26-4550 (Kd=39.4±5.5 µM) — which sites respond, never a directly observed spectrum of the isolated minor state.

## 5. COMPETING EXPLANATIONS AND CONTROLS
- **Aggregation/oligomerization** → excluded by SEC-MALS (strictly monomeric, SI Fig. S1) before the exchange analysis.
- **Local vs. global exchange** → 20 methyls across the AB loop + B/C/D helices fit one global kex/pE; R52A quenches every distant site at once (Fig. 3E,F) — the paper's main argument against independent local motions.
- **CPMG/CEST disagreement** → cross-correlated (Fig. 2C); 2 outliers attributed to the 25 vs 10 °C difference, not distinct processes.
- **Mutant-specific artifact** → R52A and Ro 26-4550 (unrelated chemistry) converge on the same closed-state-stabilization effect.
- **Species/construct effects** → not directly tested; mouse IL-2 used as "a model system," human relevance argued from fold conservation (ref. 11), not shown here.

## 6. STUCK POINTS
- EXPLICIT: free-mIL-2 amide TROSY "of marginal quality" (33% broadened) — forced the whole study onto methyl detection.
- EXPLICIT: de novo excited-state structure determination from shifts alone stated not feasible — worked around via comparison to existing structures/homology models.
- EXPLICIT: R52A CPMG fit had no well-defined χ² minimum — kex/population not extractable; fell back to qualitative dispersion/CEST presence-absence.
- EXPLICIT: only 20/60 assigned methyls gave usable dispersion; rest dropped for low S/N/overlap — a post hoc, data-quality selection, not pre-registered.
- INFERRED: pairing CPMG/CEST at different temperatures, and using a mutant rather than a second structure attempt as the main causal test, read as deliberate hedges against each method's blind spot and the unsolved de novo problem — never framed as strategy in the text.

## 7. ROLE OF MD AND STRUCTURES
No MD was run here. MD is cited twice as prior external evidence: ref. 15 (Spangler et al. 2018, *J Immunol*) for AB/BC-loop rearrangement between bound states, and refs. 10/15 for free IL-2 sampling AB-loop conformations like both bound crystal forms — framing, not generating, evidence.

Own computation is Rosetta, not MD: a homology model of free mIL-2 from apo human 1M47 (NOE reference for "closed," Fig. 2G), and satisfiability-based rotamer enumeration on closed vs. open backbones (Fig. 4; SI Figs. S8–S9) proposing the packing path from loop to core — a static comparison of two fixed backbones, not a dynamics simulation.

## 8. CLAIM AND LIMITS
Claim: free mIL-2 is a two-state pre-equilibrium — 92% "closed/uncapped" (receptor-competent) and 8% "open/capped" (antibody-like) — interconverting at kex≈1,000 s⁻¹ via one cooperative AB-loop/core motion gated by an R52 C-capping switch; perturbing the switch shifts the equilibrium, changing JES6-1 affinity ~1,000-fold and cellular signaling (Discussion; Fig. 6).

Authors' caveats: excited-state structure inferred by analogy/perturbation, not solved de novo; binding is an initial-encounter complex with added induced-fit steps atop conformational selection, not pure selection (ref. 34); results established in mouse IL-2 "as a model system," with human relevance argued, not shown here.

## 9. BEST REPLICATION TARGET FOR AN AGENT
Target: Fig. 2A–E — free mIL-2 populates an 8.0±0.4% excited state at kex=1,000±72 s⁻¹, from a global 2-site CPMG fit across 20 methyls (25 °C).

Inputs: raw R2,eff vs. νCPMG per methyl per field. **Not public as structured data** — the four BMRB entries are shift-assignment lists only, not dispersion-rate tables; curves live only in SI Fig. S3A/Table S1, inside one unopened PDF. Effort is low if Table S1 tabulates per-residue kex/pE/Δω; much higher if only plotted (needs digitization).

Success = an independently fit global 2-site model reproducing kex and pE within the paper's stated errors, on a comparable methyl subset.

Over-claiming: treating a successful fit as confirming the excited state's structure (never solved de novo), the R52A/ITC/STAT5 story (separate assays), or conformational selection over induced fit (paper claims both).

## 10. DRAFT DATABASE ENTRY
- **Protein/UniProt**: mouse IL-2 (Il2); UniProt not stated (background knowledge: P04351, unverified against text).
- **Construct**: WT + R52A; MILV-methyl-labeled, perdeuterated, plus Iδ1/proS-L,V variant; residue range/expression/tags not stated.
- **Conditions**: 25 °C (CPMG, HMQC); 10 °C (CEST); 293 K/20 mM phosphate pH 7.2/150 mM NaCl (ITC); sample buffer/pH not stated.
- **Major (apo) state**: "closed/uncapped," ~92%, IL-2Rα-recognition-competent (Fig. 2E,G; Fig. 6).
- **Alternative state**: "open/capped," R52-C-capping-stabilized, ~8.0±0.4%, kex≈1,000±72 s⁻¹, JES6-1-recognition-like (Fig. 2E; Fig. 3; Fig. 6).
- **Evidence type**: ¹³C methyl CPMG + CEST; corroborated by NOE, mutant/ligand perturbation, ITC, cell-based STAT5.
- **Timescale**: µs–ms. **Population**: pE=8.0±0.4% minor / 92% major.
- **Residues**: AB loop (R52, M53, L54) plus A–D helix core sites (e.g. L80, I101, V130, L133, W136) (full list: Figs. 1D/E, 2D, 4A/B).
- **Structural model of alternative state**: unmapped — no coordinates solved for the free-state excited conformation; nearest proxy is PDB 4YQX (JES6-1-bound), used by the authors as the presumed analog (Fig. 3A) — Inference/Proposal, not a direct determination.
- **Functional relevance**: closed↔IL-2Rα (agonist signaling); open/excited↔JES6-1 (Treg-biasing antibody); Ro 26-4550 and R52A both push toward closed, cutting JES6-1 affinity ~1,000-fold (Fig. 3G,H; Fig. 6).
- **Confidence tier** (Proposal): high for existence/population/kex (two NMR methods, global fit, two orthogonal perturbations agree); medium-low for the excited state's 3D structure (analogy only).
- **Provenance**: Results §§ listed in §3; Discussion; Figs. 1–6; Data and Materials Availability (BMRB 27969/70/71/74); SI Appendix (Figs. S1–S9, Tables S1–S3, not opened).
