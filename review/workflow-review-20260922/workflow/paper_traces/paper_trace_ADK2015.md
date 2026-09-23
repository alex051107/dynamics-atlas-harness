# Paper Trace: Kerns et al. 2015, "The energy landscape of adenylate kinase during catalysis"

Locators: R1–R5 = the five Results subsections in order (electrostatic pivot; MD; rapid kinetics; lid-opening NMR; conserved arginine). "M:X" = an Online Methods subsection.

## 0. ACCESS
Full text via Europe PMC (PMCID PMC4318763, open access), read as PMC HTML through ~12 targeted WebFetch passes covering every section, both tables, figure legends, and Accession Codes. The `fullTextXML` endpoint 500'd twice, so HTML rendering was the actual source; each pass runs through an intermediate summarizing model rather than returning raw text, so quotes are best-extraction, not hand-verified verbatim. Locators are section/figure names — this render carries no page/paragraph numbers. The local `ADK2015.html` capture was unused; Supplementary Information (1 .docx, 2 .pdf) was not opened, per the no-download instruction.

## 1. PAPER
Kerns SJ, Agafonov RV, Cho YJ, Pontiggia F, Otten R, Pachov DV, Kutter S, Phung LA, Murphy PN, Thai V, Alber T, Hagan MF, Kern D. *Nat Struct Mol Biol* 2015 Jan 12;22(2):124–131. DOI 10.1038/nsmb.2941. Structures use *Aquifex aeolicus* Adk (AAdk, thermophile, crystallizable); kinetics/NMR use *Escherichia coli* Adk (EAdk) instead, explicitly because AAdk dynamics "could not be measured... by NMR," justified only by conserved "active-site architecture, catalytic mechanism, and rate-limiting steps" between orthologs [R1]. Substrates: ADP, AMP, AlF4⁻ (transition-state mimic), Mg2+/Ca2+/Co2+ cofactors [Tables 1–2]. "Alternative state" = the catalytically closed LID/NMP conformation the nucleotide-bound enzyme transiently adopts mid-cycle, versus an open, release-competent conformation [Abstract; Intro]. This is on-pathway exchange of a bound complex, not the ligand-free protein's own ensemble: "apo" never appears in the text; the only ligand-free/bound mention is a generic citation to prior structures [Intro]. Apo AdK sampling closed-like states — this project's motivating example — is **not** what this paper measures; calling its closed state an "alternative APO state" is a category error. That apo claim traces to other AdK/NMR papers from the same lab lineage — background knowledge, not confirmed here.

## 2. DATA & AVAILABILITY
X-ray: 11 structures (AAdk1–11), 1.24–2.37 Å, P2₁2₁2₁ [M:crystallography]. Public PDB IDs [Accession Codes]: 4JL5 (AAdk1, WT Mg-ADP-ADP), 4JLD/4JLB/4JL8/4JLA (AAdk2/3/4/6, more ADP-ADP snapshots), 4JL6 (AAdk5, AMPPN), 4JKY (AAdk7, Co2+ control), 3SR0 (AAdk8, TS mimic Mg-ADP-AMP-AlF4⁻), 4JLO/4JLP (AAdk9/10, R150K), 4CF7 (AAdk11, high-pH). NMR: BMRB 19089–19093, public, unmapped to samples in-text [checked; not stated]. Kinetics: quench/stopped-flow + steady-state HPLC rates (Table 2), figure/table-only. MD and APBS electrostatics: Methods-only; movies apparently in SI (unopened).

## 3. WORKFLOW TRACE
1. Prior AdK structures/NMR reviewed → Q: quantitative catalytic energy landscape available? → EXPLICIT no ("few... solved with natural substrates in an active quaternary complex") [Intro].
2. Crystallize AAdk across the reaction coordinate (11 structures; ambiguous Mg2+/water density resolved via a Co2+ anomalous-scattering structure) → Mg2+ fixed, only donor phosphoryl+R150 move (~1 Å) → judgment: Mg2+ is an "electrostatic pivot" [R1]. EXPLICIT.
3. MD ± Mg2+ on the AAdk1 complex (4×100ns/condition, 4 extended to 200ns, several µs total) → without Mg2+, donor phosphate/waters sample far more states → judgment: Mg2+ suppresses non-productive fluctuations [R2]. EXPLICIT.
4. Q: rates of chemistry and lid-opening individually, not just kcat? → EAdk quench-flow ±Mg2+ → chemistry >5000 vs 0.14±0.1 s⁻¹; lid-opening 190±30 vs 0.05±0.01 s⁻¹ → judgment: Mg2+ separately gates both steps [R3]. EXPLICIT.
5. Confirm lid-opening via 15N CPMG NMR during turnover → kex 210±80 s⁻¹ (+Mg2+) matches kinetics 190±30 s⁻¹; without Mg2+ dispersion flat, resolved via a 20–40°C ramp → judgment: two orthogonal methods agree [R4]. EXPLICIT.
6. Test conserved arginine → R150K EAdk, same battery → 10³-fold P-transfer defect, negligible lid-opening effect; mutant structure shows lost H-bond to β-phosphate → judgment: guanidinium geometry, not charge, matters [R5]. EXPLICIT.
7. Test cation specificity → Mg2+/Ca2+/Co2+ rate comparison + APBS electrostatics on MD structures → judgment: chemistry Mg2+-specific, lid-opening acceleration more general [R5; Table 2]. EXPLICIT.
8. Integrate into one landscape, contrast non-enzymatic Mg2+ effect (~10-fold) → judgment: AdK evolved to co-activate chemistry and conformational change with one cofactor [Discussion]. EXPLICIT.

## 4. DETECTION & CHARACTERIZATION OF ALTERNATIVE STATES
Detected two ways, cross-validated: quench-flow kinetics (direct rate) and 15N CPMG relaxation dispersion NMR (kex) on EAdk with bound ADP-ADP [R3–R4]. No population (pB) or Δω reported — RD fits give exchange/rate constants only [checked; not stated]. Numbers: lid-opening forward/reverse 190±30/2800±200 s⁻¹ (+Mg2+) vs 0.05±0.01/0.09±0.05 s⁻¹ (−Mg2+); NMR kex 210±80 s⁻¹ (+Mg2+) [R3–R4]. Mg2+ accelerates phosphoryl transfer >10⁵-fold (Mg2+-specific) and lid-opening ~10³-fold (shared with Ca2+/Co2+) [Abstract; R3, R5].

## 5. COMPETING EXPLANATIONS AND CONTROLS
- Mg2+ vs. water in electron density → Co2+ anomalous-scattering structure (AAdk7) [Methods].
- Charge vs. geometry for R150 → resolved structurally (lost H-bond in R150K, not just lost charge) [R5].
- Mg2+-specific vs. general-divalent effect → Mg2+/Ca2+/Co2+ comparison: chemistry Mg2+-selective, lid-opening not [Table 2; R5].
- Kinetics vs. NMR cross-validate one lid-opening rate rather than relying on a single method [R4].
- Cross-species extrapolation (AAdk structures → EAdk kinetics/NMR), controlled only by a conservation argument, not direct AAdk measurement [R1].

## 6. STUCK POINTS (most valuable)
1. AAdk (the crystallized construct) could not be studied by NMR → switched species to EAdk on conservation grounds alone — the paper's largest inferential leap, EXPLICIT [R1].
2. Quench-flow burst amplitudes turned "unphysical" past instrument dead time (Mg2+/Ca2+/Co2+) → built a time-correction procedure constraining forward+reverse bursts to equal total enzyme concentration [M:time-correction]. EXPLICIT.
3. Without Mg2+, CPMG dispersion was flat (too slow to fit kex) → ran a 20–40°C series to shift exchange into an observable regime, reporting only a bounding Rex (~1 s⁻¹) [R4]. EXPLICIT.

## 7. ROLE OF MD / COMPUTATION AND STRUCTURES
Two computational methods, both mechanistic, not rate-measuring. (a) MD: CHARMM22/CMAP, TIP3P, NAMD→GROMACS, NPT 300K, from AAdk1, 4×100ns/condition (±Mg2+), 4 extended to 200ns, several µs combined [M:MD]. Sampled only local active-site fluctuations, not full LID/NMP transitions [R2] — evidence Mg2+ suppresses non-productive sampling, not a rate source. (b) APBS Poisson-Boltzmann electrostatics on MD-derived structures (298.15K) argues Mg2+ lowers the electrostatic barrier to lid-opening — a post-hoc rationalization, not independent evidence [R5].

## 8. CLAIM AND LIMITS
Claim: one Mg2+ cofactor activates phosphoryl transfer (>10⁵-fold, Mg2+-specific) and LID-opening (~10³-fold, cation-general); R150 adds a further 10³-fold to phosphoryl transfer via guanidinium geometry [Abstract; Discussion]. Limits: dynamics measured on EAdk, not the crystallized AAdk [R1]; Mg2+ chemistry acceleration is a lower bound (>5000 s⁻¹ is dead-time-limited) [R3]; NMR RD gives rates only, no populations/Δω [not stated]; MD never observed a full transition [R2]; only one arginine mutant tested, no charge-conservative control [R5].

## 9. BEST REPLICATION TARGET FOR AN AGENT
Unit: "Mg2+ accelerates EAdk LID-opening ~1000-fold, confirmed by two independent methods" (190±30 s⁻¹ kinetics vs. 210±80 s⁻¹ NMR, +Mg2+, ADP-ADP-bound EAdk, 25°C) [R3–R4]. Inputs: public — paper text/Table 2 for both rates; PDB structures (4JL5, 3SR0) for context; BMRB 19089–19093 exist but aren't mapped to conditions in-text, so an agent cannot assume a usable labeled curve without inspecting them directly. Effort: low–moderate — number extraction and cross-check, not re-simulation or wet-lab work. Success criterion: agent reports both rates with correct locators and condition (EAdk, +Mg2+, bound ADP-ADP — not AAdk, not apo), and states within-error agreement. Over-claiming risks: (i) calling this an "apo" state when it's substrate/product-bound; (ii) treating >5000 s⁻¹ as measured rather than dead-time-bounded; (iii) conflating AAdk numbering/species with EAdk; (iv) assuming BMRB entries are usable without checking.

## 10. DRAFT DATABASE ENTRY
- Protein/UniProt: Adenylate kinase (EC 2.7.4.3). E. coli Adk UniProt commonly P69441 — background knowledge, not verified here. AAdk UniProt: unfilled.
- Construct: EAdk WT and R150K (kinetics/NMR); AAdk WT, R150K, Co2+ variant (crystallography only) [R1, R5].
- Conditions: 25°C (also 30/40°C, NMR series), pH 7.0, 100 mM HEPES/50 mM NaCl/5 mM TCEP, 20 mM ADP, ±Mg2+ (also Ca2+/Co2+, kinetics) [M:NMR Dynamics].
- Major/alternative state: open LID/NMP (release-competent) vs. closed LID/NMP (catalytically competent, transiently populated mid-turnover in the bound complex — **not** ligand-free/apo, see §1) [Intro; R3; Abstract].
- Evidence type: pre-steady-state kinetics + 15N CPMG NMR, cross-validated; X-ray + MD/APBS as mechanistic support [R2–R4].
- Timescale: lid ms regime (k≈190/2800 s⁻¹, +Mg2+); chemistry ≥5000 s⁻¹ (+Mg2+, lower bound) [R3–R4].
- Population: not stated (RD fits give exchange rates only).
- Residues/domains: LID, NMP domains; active-site R150 (AAdk numbering, applied to EAdk mutant) [R1, R5].
- Structural model (PDB): 4JL5 (WT Mg-ADP-ADP), 3SR0 (TS-mimic), 4JLO/4JLP (R150K) [Accession Codes].
- Functional relevance: LID-opening is, with chemistry, one of two Mg2+-gated steps setting turnover [Abstract; Discussion].
- Confidence tier: high for the rate constants (two-method agreement); unfilled/low for population or ensemble claims beyond the crystallographic end-states.
- Provenance: Kerns et al., *Nat Struct Mol Biol* 2015;22:124–131, DOI 10.1038/nsmb.2941, PMCID PMC4318763.
