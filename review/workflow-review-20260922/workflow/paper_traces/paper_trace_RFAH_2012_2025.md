# Paper Trace: RfaH Fold Switching — Burmann et al. 2012 vs. Cai et al. 2025

Locators: "2012" = Burmann et al., *Cell* 150:291–303 (PMC3430373, DOI 10.1016/j.cell.2012.05.042, PMID 22817892). "2025" = Cai et al., *PNAS* 122:e2506441122 (PMC12107155, DOI 10.1073/pnas.2506441122, PMID 40366684). Parsed from local HTML, no PDFs downloaded. R1, R2… = Results subsections in order (2012: closed state, CTD refolds, functional role, S10 in vivo, S10 in vitro; 2025: assign B, secondary structure, RDC/relaxation, CS-ROSETTA, CEST, CPMG); CR = Concluding Remarks (2025). Trace stages are EXPLICIT unless marked [INFERRED].

## PAPER A — Burmann et al. 2012, *Cell*

### 1. Paper
Full-length RfaH (162 aa); isolated NTD(~1–100)/CTD(~101–162); mutants E48S/E48A (salt bridge), I146D/L145D (S10 interface); TEV-linker construct; ops-lux ±RBS reporters, ΔrfaH strain IA149 [Results]. NMR 288 K, 18.8 T [Fig.2]; buffer/pH not stated (unread SI). Alternative state = complete CTD fold switch, α-hairpin (NTD-bound) vs. β-barrel (isolated, RMSD 0.65 Å to NusG-CTD) [R2]. Counts as alternative APO state only partly: apo full-length shows only the closed fold [R1]; β-fold appears only isolated or once the interface is weakened/cut [R2,Fig.4] — real, but reached by dissociation, framed as RNAP/ops-triggered, not spontaneous apo breathing.

### 2. Data & Availability
Types: solution NMR (HSQC, assignment, CSI, R1/R2), luciferase reporters, qRT-PCR, ChIP-chip, crosslink-MS, gel filtration [R1–R5]. Accession: PDB 2LCL (CTD ensemble, deposited here, public) [Footnotes]. Reused only: 2OUG, 2JVV/2K06, 3D3B [Fig.1,3,6]. No BMRB code anywhere despite full backbone assignment — confirmed by direct search, a real gap. ChIP-chip/crosslink-MS/pause data are figure-only, no accession. SI: 2 PDFs+1 video, "nine figures, one table" [Footnotes]; not opened.

### 3. Workflow Trace
1. Compared 2OUG (RfaH closed) vs. NusG (β-barrel CTD) [Fig.1].
2. Q: does the fold hold in solution? Full-length NMR: CSI matches crystal, τc=13.4 ns → apo = crystal fold [R1].
3. Isolated-CTD HSQC → 5 β-strands, RMSD 0.65 Å to NusG-CTD → CTD's intrinsic fold is β, NTD imposes α [R2].
4. Stuck: heat/TFE precipitated the protein [R2] → pivoted to E48S mutant + TEV-linker cleavage; both show the switch (E48S: ~1:1 α:β peaks; TEV: full conversion to β-CTD by 42 h) → domain release itself drives the switch [R2,Fig.4].
5. Titrated Rho (no binding) then S10 (binding, NusG-like interface) into isolated CTD [R3–R5,Fig.5–6].
6. CTD-interface mutants + reporters/qRT-PCR/ChIP-chip/crosslink-MS → mutants cripple RBS− translation and wbbI; S10 enriched on rfb without NusB/NusG → the switch is load-bearing in vivo [R3–R4,Fig.5,S7].

### 4. Detection & Characterization
CSI + R1/R2 (τc=13.4 ns, 288 K, 18.8 T); no exchange-detecting pulse sequence — states are separate static samples, not one interconverting sample [R1–R2]. E48S: α:β≈1:1 by peak intensity, qualitative [R2]. TEV: peak presence/absence over 42 h only, no rate constant [Fig.4]. CTD:S10 Kd "not possible" by NMR (cf. NusG-CTD:S10:NusB Kd=50 µM) [R5].

### 5. Competing Explanations and Controls
Four candidate anti-Rho mechanisms enumerated; only TEC modification and NusG exclusion pre-supported; direct Rho binding tested and ruled out (no shift on titration); translation increase supported here [Discussion]. Control: ChIP-chip S10 signal on rfb lacks NusB/NusG co-signal, against those alternatives [R4,Fig.5D–G].

### 6. Stuck Points
(a) Heat/TFE precipitated the protein → pivot to E48S + TEV-cleavage (§3.4) — most valuable item here. (b) CTD:S10 Kd unobtainable by NMR [R5] → substituted shift-mapping plus in vivo phenotype for a functional, not biophysical, claim.

### 7. Role of MD and Structures
No simulation. Prior structures (2OUG, 2JVV, 2K06, 3D3B) used only as fixed comparison targets. New structure 2LCL comes from standard NOE-based calculation, detailed only in unread SI [R2,Footnotes].

### 8. Claim and Limits
Claim: domain release triggers a genuine α→β CTD switch enabling S10 binding and translation activation [Discussion]. Ceiling: shown in isolated/mutant/cleaved constructs plus in vivo phenotype; CTD's fold during real transcription was never directly observed. No rate constants, no reversibility proof, no CTD:S10 Kd.

### 9. Best Replication Target for an Agent
Unit: isolated RfaH-CTD folds as a 5-strand β-barrel, RMSD 0.65 Å to NusG-CTD over P112–L162 [R2]. Inputs: PDB 2LCL + 2JVV, both public. Effort: low — fetch both, compute backbone RMSD. Success: computed RMSD within ±0.2 Å of 0.65 Å. Over-claiming risk: low here; rises sharply if generalized to full-length apo RfaH instead of the isolated/domain-separated CTD.

### 10. Draft Database Entry
- Protein/UniProt: RfaH / P0AFW0 (E. coli K-12, 162 aa) — looked up directly, not stated in either paper.
- Construct: isolated CTD, ~101–162, boundary imprecise in main text. Conditions: not stated (unread SI).
- Major/alt. states: closed α-hairpin CTD (full-length) [R1] vs. β-barrel CTD (isolated/released), RMSD 0.65 Å to NusG-CTD [R2].
- Evidence type: static two-sample NMR (CSI), no exchange kinetics. Timescale/population: not determined; ~1:1 α:β in E48S only, qualitative [R2].
- Residues: CTD≈101–162; interdomain patch I129,L142,I146,V116,V154,F159 [R2,Fig.3].
- Structural model: PDB 2LCL (β-form, public). Functional relevance: enables S10 binding → translation activation [R3–R5].
- Confidence tier: High (isolated-CTD β-fold, deposited+cross-validated); Low (full-length apo protein sampling β-form — not observed).
- Provenance: RFAH2012.html, PMC3430373.

## PAPER B — Cai et al. 2025, *PNAS*

### 1. Paper
Construct: isolated RfaH-CTD only, U-[15N/13C/2H] or U-[15N/2H]; no full-length NMR here (full-length data cited from a separate prior paper, ref.12) [Exp.Proc.,Fig.1]. Conditions: 25 °C, pH 6.5, 25 mM K-phosphate, 0.5 mM EDTA, ~1.0 mM, 500–900 MHz [NMR Experiments]. Alternative state = five kinetically distinct CTD states: major β-roll A, minor unfolded-ish B (both observed, populations §4), plus sparse "dark" A′/B′/B″ seen only via CPMG lineshape, never as separate peaks [Abstract,CR]. Counts as alternative APO state: yes for this isolated-CTD system — no RNAP/NTD/S10 present, A/B meet the two-peak/CEST criterion directly. Debatable for RfaH overall: no interconversion is seen for free full-length RfaH [Intro,refs4/10/12] — shown for a domain standing in for a partner-triggered transition, not spontaneous behavior of the intact protein.

### 2. Data & Availability
Types: 15N-CEST, 15N-CPMG, 3D zz-exchange (NUS), triple-resonance assignment, RDCs (Pf1), R1/R2/NOE, CS-ROSETTA, TALOS-N [R1–R6]. Accessions: BMRB 52718 (A), 52719 (B), deposited here, public [NMR Experiments]; BMRB 52348 (full-length CTD) reused from ref.12, not redeposited [Fig.2]. PDB 2LCL/2OUG/6C6C reused as reference only [Fig.1,3]. Raw CEST/CPMG data + Matlab fitting code: figshare DOI 10.6084/m9.figshare.28629485.v1, public — unusually complete for reproduction. SI: one bundled PDF, ≥22 figures, ≥7 tables; not itemized.

### 3. Workflow Trace
1. Looked at own prior CEST result (ref.13: slow 100–200 ms exchange to an unstructured minor state) and a prior full-length NTD excited-state (ref.12); asked what B's structure is, and whether faster invisible states hide beneath it [Intro].
2. 3D zz-exchange HNH/NNH (NUS) assigns B via exchange cross-peaks after ordinary 3D experiments failed on its weak/overlapped peaks → full A/B assignment (BMRB 52718/52719) [R1]. Δδ13Cα/13C′+TALOS-N on B → random coil overall but transient α5* helix (~40% occ.) and β1*/β2* hairpin (~10–20% occ.), echoing both end folds → B is a candidate intermediate, not simple unfolding [R2].
3. CS-ROSETTA (10,000 models, B's shifts only) → 8/10 models pack the two elements within ~50–70° — a shift-driven hypothesis, not a measurement [R4,Fig.4].
4. Global 2-state CEST fit (A/B) → τex≈300 ms, kAB≈0.8 s⁻¹, kBA≈2.4 s⁻¹, pA≈75%, pB≈25%, cross-validated vs. zz-exchange shifts [R5].
5. Stuck: model fails CPMG (χ²=22.6/51.7) → add invisible states stepwise, refit CPMG+CEST jointly, stop at 5 states (linear/branched, χ²≈1.0, indistinguishable) [R5–R6,Fig.6] — most valuable item in either paper; branched preferred only via a shift-pattern argument, flagged as inference [CR].

### 4. Detection & Characterization
15N-CEST (TCEST=600 ms, RF 10/15/25 Hz, 600 MHz, 25 °C): slow A↔B as in §3.4. 15N-CPMG (600/900 MHz, νCPMG 17–1000 Hz): A′ τex≈500 µs/pop≈0.35%; B′ τex≈1.2–1.3 ms/pop≈0.25–0.35%; B″ τex≈0.8–1 ms/pop≈0.05% [R6]. RDC+R1/R2/NOE: A rigid (S²=0.83, τR=5.8 ns), B disordered (RDCs ~5× smaller, S²slow≈0.45–0.7) — independent, non-exchange confirmation [R3]. State identity inferred from Δω sign/magnitude vs. random-coil and full-length-α references, plus CS-ROSETTA [R2].

### 5. Competing Explanations and Controls
Topologies tested and rejected: plain 2-state (fails CPMG); A↔I↔B and A↔B↔B′ for the A-branch (high χ²) vs. A′↔A↔B (accepted); A↔B↔B′ for the B-branch (residual deviation) extended to 4-/5-state, reported as statistically indistinguishable rather than forced [R5–R6]. Control: R1ρ vs. CEST-R2 shows a faster regime CEST misses, motivating CPMG.

### 6. Stuck Points
(a) CEST-only 2-state model fails CPMG (χ²=22.6/51.7) → resolved by stepwise hidden-state addition with a joint-fit/χ² stopping rule, not looser error bars (§3.5) — single most valuable item across both papers, a reusable "second experiment breaks the model → add one hidden state, refit jointly" template. (b) Linear vs. branched topology indistinguishable by relaxation data → reported as unresolved, decided only qualitatively [CR].

### 7. Role of MD and Structures
No MD. CS-ROSETTA is the only computational step — chemical-shift-driven fragment assembly, caveated as giving a poorly defined relative orientation in 8/10 models [R4]. PDB structures reused as fixed comparison points only. Neither RfaH paper uses an MD engine; an MD-trajectory adapter is inapplicable to either source.

### 8. Claim and Limits
Claim: isolated CTD visits ≥5 kinetically distinct states with defined populations/timescales, several consistent with fold-switch intermediates [Abstract,CR]. Ceiling: scoped to the isolated construct; exchange not seen in free full-length protein, so the claim doesn't extend to intact apo RfaH absent the not-yet-done NTD+CTD reconstitution [Intro,CR]. Limit: B″ at ~0.05% population, Δω sign undetermined; rests on magnitude-only data plus a non-distinguishable model choice.

### 9. Best Replication Target for an Agent
Unit: isolated-CTD states A/B exchange, τex≈300 ms, kAB≈0.8 s⁻¹, kBA≈2.4 s⁻¹ (§3.4). Inputs: BMRB 52718/52719 + figshare data/code (DOI 10.6084/m9.figshare.28629485.v1) + PDB 2LCL — all public, no paywall. Effort: low to re-extract numbers, moderate to re-run the Matlab fit. Success: extracted pA,pB,τex,kAB,kBA match paper values within stated error; if refit, χ²(all)≈1.0 within tolerance. Over-claiming risk: high if "isolated CTD" is dropped and reported as a full-length-RfaH apo finding.

### 10. Draft Database Entry
- Protein/UniProt: RfaH / P0AFW0 (E. coli K-12, 162 aa) — looked up directly, not stated in either paper.
- Construct: isolated CTD, U-[15N/13C/2H], boundary not restated numerically. Conditions: 25 °C, pH 6.5, 25 mM K-Pi, 0.5 mM EDTA, ~1.0 mM [NMR Experiments].
- Major/alt. states: β-roll A ~75–77% (Abstract vs. R5 fit differ slightly); B ~23–25%; A′~0.35%; B′~0.25–0.35%; B″~0.05% (§1,§4).
- Evidence type: 15N-CEST+CPMG+zz-exchange; CS-ROSETTA/TALOS-N inference.
- Timescale: τex(A-B)≈300 ms; (A-A′)≈500 µs; (B-B′)≈1.2–1.3 ms; (B/B′-B″)≈0.8–1 ms.
- Residues: α5*≈136–145; β1*≈115–120; β2*≈127–132; A′ at β1/β2 loop+strand β4.
- Structural model: A = PDB 2LCL (public); B/A′/B′/B″ = CS-ROSETTA only, unmapped.
- Functional relevance: proposed intermediates linking NTD-bound α-hairpin and RNAP/S10-competent β-roll (link from Paper A).
- Confidence tier: High (A,B); Medium (A′,B′, unmapped); Low (B″, pop.0.05%); Unsupported (extension to intact apo full-length RfaH).
- Provenance: RFAH2025.html, PMC12107155.

## 11. How the Workflow Changed from 2012 to 2025

2012 asked a structural question — does this domain have two folds, and does it matter for a phenotype — answered with static NMR snapshots of engineered constructs (isolated domain, salt-bridge mutant, protease-cleaved linker) versus known reference folds, closed with genetics and ChIP. 2025 asked a kinetic question — how many states does the domain visit, in what order, at what rate — unanswerable by 2012's toolkit, which never probed exchange within one sample. Two advances made it answerable: exchange-detecting pulse sequences (CEST, CPMG, zz-exchange) revealing populations below ~1% invisible to ordinary HSQC, and a disciplined joint-fitting strategy (add one hidden state at a time, judge by χ²) turning "the model doesn't fit" into a search, not a dead end. 2025 was only askable once 2012 had fixed the two end states: a workflow must match method to the question's timescale and observability — a static comparison cannot answer a kinetic-pathway question, and exchange spectroscopy is wasted before the end states are known.
