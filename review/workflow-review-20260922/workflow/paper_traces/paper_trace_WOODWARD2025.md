# Workflow trace — Woodward et al. 2025, J Mol Biol 437(2):168892 (IL-2 core allostery)

## 1. ACCESS
Read via PMC full text (https://pmc.ncbi.nlm.nih.gov/articles/PMC12077578/), targeted passes over Results, Methods, figure legends, Data Availability, author list. Europe PMC XML mirror returned HTTP 500, unused. No PDF, no bioRxiv cross-check. Quotes are single-pass extractions, not hash-verified.

## 2. SYSTEM AND STATES
Human IL-2, four constructs: wild-type (C125S; BMRB 28104, published previously by this group), superkine S15 (7 substitutions, directed evolution), superkine S1 (17 substitutions incl. remodeled BC-loop, computational design), S1 L56A (point mutant on S1, made for this paper). All NMR/MD on free cytokine, no receptor present (50 mM NaCl, 20 mM phosphate pH 6.0, 5% D2O; CPMG at 5 °C, 600/800 MHz). Major state ≈ crystallized conformation (WT 1m47, S15 7raa, S1 7ra9); minor/"excited" state = CPMG-detected conformer, not independently solved. "Apo" is never used; receptor-free is implicit, and the only explicit ligand-relative framing is functional (SPR/pSTAT5 vs. IL-2Rβ/CD122).

## 3. WORKFLOW TRACE
1. **[St.1]** WT assignments + superkine crystals → do superkines differ from WT in solution despite near-identical crystals? → backbone/methyl assignment, 89–97% coverage → compare dynamics, not just statics. Methods. EXPLICIT.
2. **[St.4]** Methyl CPMG (5 °C, 600/800 MHz) → is there exchange, construct-dependent? → global two-site fit (CATIA); kex = 4088±190 (WT), 2878±44 (S15), 651±16 s⁻¹ (S1); Rex≥3 in 9/20/19 probes; population (pB) not extractable, "degeneracy in the χ2 landscape" → exchange is real, slower in superkines, not "quenched"; rate reported, population withheld (§4). Fig. 3; Methods. EXPLICIT.
3. **[St.5]** |Δω| per residue, WT vs. S15 vs. S1 → same region exchanging? → overlapping but distinct sets (mini-helix/A'B-loop/B-helix, C-helix); S1 generally smaller → distinct, not merely damped, networks. Fig. 3. EXPLICIT.
4. **[St.6]** New adaptive-sampling MD (FAST-RMSD; GROMACS 2023.2, CHARMM36m/TIP3P; seeded 1m47/7raa/7ra9; 10 gen. × 10 runs × 50 ns = 5 μs/protein), tICA on distances between CPMG-exchanging methyls → what does the minor state look like, does MD track NMR? → WT pivots about mini-helix; S15 mini-helix unfolds; S1 mini-helix folded but shifts inward, C-helix shifts most; "residues with increased structural variation… also show high Rex" → three distinct repacking mechanisms; MD gives "a plausible mechanism," not kinetic proof. Fig. 4; Results MD section. EXPLICIT.
5. **[St.6→7, hub-finding]** CARDS/mutual-information network from S1 trajectories → which residue, mutated, breaks the network without touching the receptor interface? → high-MI cluster in A'B-loop/B-helix overlapping CPMG residues (Fig. S14); Leu56 selected: buried, central, interface-distal → nominate L56A. Results "Rational mutation…"; Fig. S14. EXPLICIT.
6. **[St.5/7, perturbation + control]** S1 L56A: new CPMG, MD, CD, SPR, pSTAT5; plus V84A control (destabilizing, network-orthogonal) → does removing this contact collapse network and function, and is that specific to the network rather than to stability loss? → L56A: reduced Rex, faster kex, altered helix distances in MD, Tm ↓~20 °C vs. S1, KD 18.6→46.2 nM, kd 0.0184→0.0393 s⁻¹, ~2.5-fold higher EC50; V84A: stability drops but dynamics/network/binding unchanged → L56 is specifically load-bearing (§4). Figs. 5–6; Discussion. EXPLICIT.
7. **[St.8, synthesis]** Prior "quenching/priming" model (refs 7,21,22,37–39) → supported? → "we expected… quenched… Instead… certainly not quenched" → revise to "distinct core repacking," proposed here only. Discussion. EXPLICIT.

## 4. STUCK POINTS
- **Fit non-identifiability** (step 2): CPMG fits gave robust kex but not pB, from χ² degeneracy. Response: report kex/Rex only, name the limit rather than force a number. EXPLICIT — a "state the limit" move, not an extra experiment.
- **Which residue to mutate**, out of ~9–20 exchanging methyls (step 5): CPMG flags a set, not which member is causal or interface-safe. Response: rank residues with a new MD-derived correlated-motion network (CARDS + mutual information), intersect with the CPMG set and interface distance. EXPLICIT chain (Fig. S14 → Leu56) — the paper's central "when stuck" move, and the one most absent from Card 6.
- **Ruling out a trivial confound** (step 6): an obvious alternative is "any destabilizing mutation would do this." Response: a second, stability-matched but network-orthogonal mutation (V84A) that does not reproduce the phenotype. EXPLICIT designed negative control.
- **Timescale mismatch** (ns–μs adaptive MD vs. μs–ms CPMG exchange): never addressed directly; the paper substitutes a correlational argument (same residues flexible in MD and exchanging in CPMG) for a kinetic one. INFERRED gap — no reconciling sentence found.

## 5. HOW NMR AND MD WERE COMBINED
GROMACS 2023.2, CHARMM36m/TIP3P, seeded from crystal structures (1m47/7raa/7ra9); goal-directed adaptive sampling (FAST-RMSD), 10 generations × 10 runs × 50 ns = 5 μs/protein, repeated for S1 L56A. No Markov state model; dimensionality reduction is tICA only, on pairwise methyl-methyl distances of CPMG-exchanging residues — the NMR result chose MD's input features, then MD was read out structurally. Tighter than "run MD, then compare," with a real risk of circularity: MD is steered toward coordinates CPMG already flagged. Comparison metric: per-residue Cα RMSF/χ² spread in MD vs. per-residue Rex from CPMG, qualitative only — no direct kinetic or S² overlay. Agreement licensed a structural narrative (Figs. 4–5) and a mutagenesis target (Fig. S14), not numeric validation — the authors' own language is "plausible allosteric pathways," never a reproduction of the exchange.

## 6. COMPARISON WITH THE DRAFT CARDS
**(a) MATCHES**
- Card 4, "Check whether many residues fit one global process" — the joint two-site CPMG fit per protein.
- Card 2 stuck signal, "BMRB has the chemical-shift assignments but none of the exchange data" — BMRB 52582/52583/52591 are assignments only; CPMG numbers stay in the paper/figures; MD trajectories "available upon request," not deposited.
- Card 5 try #4, "Remove a key contact by mutation; the exchange should vanish [De Paula 2020, R52A]" — matched by L56A, same lab (Sgourakis) and protein as De Paula 2020 (WT BMRB 28104 predates this paper) — INFERRED continuity, not re-confirmed against De Paula 2020 this session.
- Card 7, "whether mutations that shift the population change binding or activity" — matched by L56A→SPR/pSTAT5.

**(b) NEW MOVES** (Card 6 unless noted)
- NMR-steered adaptive sampling (CPMG residues as MD/tICA features) — Card 6 routine move; contradicts its scope, "No new simulations are run."
- CARDS/mutual-information network nominating a causal hub from a larger exchanging set — Card 6 "when stuck," feeding Card 5's identity step.
- Stability-matched, network-orthogonal negative control (V84A) — Card 7 "when stuck."
- Stating, then rejecting, the field's prior mechanistic hypothesis before testing — Card 1/8 routine move: record the hypothesis under test.

**(c) CONTRADICTIONS**
- Card 6's "No new simulations are run" and its stuck signal implying only long/passive MD informs — this paper's short (5 μs/protein), goal-directed sampling gave distinct, interpretable transitions; strategy, not length, is decisive.
- Card 5's assumption that identity is pinned against an independent pre-existing structure — here identity is an MD cluster seeded from the same residues CPMG flagged, a more circular claim.

## 7. DEFINITION ISSUES
All three non-WT constructs are engineered (7–17 substitutions each); the question itself is how engineering changes the excited-state landscape — stronger than Card 1's existing flags (K-Ras, RfaH), since the baseline is inter-construct, not single-protein major-vs-minor. "Apo" is never stated; it must be inferred as "no receptor present," with the ligand (IL-2Rβ) entering only via separate functional assays — a clean case for Card 1's "record apo relative to <ligand> explicitly." The minor state's structure is an MD/tICA cluster, not an independently solved structure, and that MD was steered by the same residues CPMG flagged — worth a note on whether a state is "structurally identified" when the identifying simulation was pointed at it by the data that found it.
