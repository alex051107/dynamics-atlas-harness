# Workflow evidence table · draft v1

2026-09-22 · built from nine papers · locations come from assistant reads and are being checked against the originals

Each row is one move in the workflow for finding alternative apo states. "Support" lists the papers where the move appears, with the location in that paper. A move becomes a normal card item when papers on two or more different proteins support it; support from one protein makes it a single-source item, even when several papers on that protein show it; a move no paper supports yet is marked as our own inference and goes to Gina for a verdict.

**Paper codes.** Batch 1, sent by Gina: ADK15 = Kerns 2015 (adenylate kinase); IL2_20 = De Paula 2020 (IL-2); KRAS23 = Hansen 2023 (K-Ras); RFAH12 = Burmann 2012 and RFAH25 = Cai 2025 (RfaH). Batch 2, added by us: FRASER09 = Fraser 2009 (cyclophilin A); BOUV11 = Bouvignies 2011 (T4 lysozyme L99A); SPOER01 = Spoerner 2001 (H-Ras); WOOD25 = Woodward 2025 (IL-2 superkines). Two further papers (Xie 2020, Stiller 2022) are held out unread for testing the frozen workflow.

**Kinds.** Routine = what is normally done at this stage. Stuck signal = what tells you the stage is stuck. When stuck = what was done next. Limit = what the evidence cannot support.

**Status.** 2+ = papers on two or more different proteins · 1 = one protein only (one paper, or several papers on the same protein; the Support column shows which) · ours = our inference · probe = found in our own data search, not in a paper's workflow. Two papers on the same protein share the system and often the lab and the method, so they count once.

**Where the workflow stands after nine papers.** The table holds 105 moves: 24 supported by two or more proteins, 61 by one protein, 14 that are our inference, and 6 that come from our own data search. Five of the inference rows were added on 22 September from failures seen in the prompt-level pilot (pilot_workflow_ab/RESULTS.md); they wait for Gina's verdict like the others. Counted by paper, as in the first version of this table, 28 moves had two or more papers; four of those rest on one protein (three on IL-2, one on RfaH), and one more rests on H-Ras and K-Ras, two members of the same family. The second batch of four papers confirmed 21 moves already in the table. Its new moves fell mostly in stage 6 (9 new) and stage 5 (5 new); stages 3 and 4 hardly changed. The rule we set before reading the second batch was at most one new routine move per stage and at most two new "when stuck" moves in total. By that rule the workflow is not settled yet, so a third batch aimed at stages 5 to 7 comes before we freeze it.

## Stage 1 · Frame the question

| Move | Kind | Support | Status |
|---|---|---|---|
| Write the state pair and the ligand relative to which the protein counts as apo | Routine | ours; papers do this implicitly | ours |
| Record the hypothesis being tested and say afterwards whether it held | Routine | WOOD25 (Discussion: expected quenched dynamics, found repacking) | 1 |
| The protein is always bound to a nucleotide or cofactor | Stuck signal | KRAS23 (Methods p.11); SPOER01 (Results, Kinetics: always Mg·GppNHp) | 2+ |
| The alternative state was measured with substrate bound | Stuck signal | ADK15 (Intro; Results 3–4) | 1 |
| The state is seen only in an isolated domain, not the full-length protein | Stuck signal | RFAH12 (Results 1–2); RFAH25 (Intro; Concluding remarks) | 1 |
| The state belongs to an engineered variant (cavity mutant, superkine), not the wild type | Stuck signal | BOUV11 (L99A; wild type shows much less broadening, Intro); WOOD25 (superkines S15, S1) | 2+ |
| The reference ligand is a generic probe, not a physiological partner | Stuck signal | BOUV11 (benzene) | 1 |
| Scope the claim explicitly to the construct that was measured | When stuck | RFAH25 (Concluding remarks) | 1 |
| When a contact-based structural explanation fails, reframe the question as one about dynamics | When stuck | SPOER01 (Introduction: Thr-35 makes no effector contact) | 1 |
| Look for a study of the ligand-free, full-length protein of the same system | When stuck | ours | ours |
| When a paper covers several proteins or state pairs, write one entry per pair and give each its own tier | Routine | ours; pilot 2026-09-22: of four Whittier 2013 entries, one left out YopH and two folded it into PTP1B's "strong" | ours |

## Stage 2 · Gather evidence

| Move | Kind | Support | Status |
|---|---|---|---|
| Collect full text, supplement, BMRB, PDB, author deposits and existing MD; search wide first | Routine | FRASER09 (superposed 48 existing CypA structures before any new experiment, Suppl. Fig. 1); otherwise ours | 1 |
| BMRB has chemical-shift assignments but no exchange data | Stuck signal | ADK15, IL2_20, KRAS23, RFAH25, WOOD25 (data probe; WOOD25 Data availability) | probe |
| Exchange data sit in a general repository (Dryad, Figshare) | Stuck signal | KRAS23 (Data availability); RFAH25 (Data availability) | probe |
| MD trajectories are "available upon request" only | Stuck signal | WOOD25 (Data availability) | probe |
| No BMRB entry at all; shift data only in the supplement | Stuck signal | BOUV11 (data deposition footer: PDB only) | 1 |
| A PDB code printed in the paper resolves to an unrelated structure | Stuck signal | RFAH25 ("6C6C") | probe |
| BMRB citation metadata never updated to the published paper | Stuck signal | ADK15 (BMRB 19089) | probe |
| Look for BMRB entries titled "minor state" or "excited state" | When stuck | RFAH25 (BMRB 52719) | probe |
| Transcribe supplementary tables before digitizing figures, and flag digitized values | When stuck | ours | ours |

## Stage 3 · Check conditions

| Move | Kind | Support | Status |
|---|---|---|---|
| List construct, species, mutations, bound ligand, temperature, pH, buffer, field for every item | Routine | ours | ours |
| Structures and NMR come from different species | Stuck signal | ADK15 (Results 1) | 1 |
| Measurements taken at different temperatures are put side by side | Stuck signal | IL2_20 (Fig. 2C: CPMG 25 °C, CEST 10 °C); KRAS23 (Methods p.11: assignments 283/288 K, exchange 298 K); SPOER01 (NMR 5 °C, stopped-flow 10 °C, affinities 37 °C, compared without comment) | 2+ |
| Attribute outlier residues to the condition difference and say so | When stuck | IL2_20 (Fig. 2C) | 1 |
| Justify transfer across species by a conserved active site and mechanism | When stuck | ADK15 (Results 1) | 1 |

## Stage 4 · Is the exchange real?

| Move | Kind | Support | Status |
|---|---|---|---|
| Detect two states directly as two resolved peaks (slow exchange on the chemical-shift timescale) | Routine | SPOER01 (Fig. 1, ³¹P); RFAH25 (states A and B); RFAH12 (E48S, both folds ~1:1) | 2+ |
| Fit many residues to one global exchange process | Routine | IL2_20 (Fig. 2); KRAS23 (Table 1); RFAH25 (Results 5); WOOD25 (Fig. 3); BOUV11 (Methods) | 2+ |
| Cross-validate with a second method (CPMG against CEST, NMR against kinetics, crystal against J-couplings) | Routine | IL2_20 (Fig. 2C); KRAS23 (joint fit, Table 1); ADK15 (Results 3–4); RFAH25 (CEST, ZZ-exchange, CPMG); FRASER09 (J-couplings confirm the crystal rotamer; ZZ-exchange confirms turnover) | 2+ |
| Measure a control state where no exchange is expected | Routine | KRAS23 (Suppl. Fig. 4, GDP-bound) | 1 |
| Name a specific artifact or confound and test it directly, instead of listing it as a caveat | Routine | IL2_20 (aggregation, SEC-MALS, SI Fig. S1); KRAS23 (hydrolysis: exchange rate against turnover, p.1454); SPOER01 (weaker Mg²⁺ binding measured, too small to explain the effect) | 2+ |
| Amide peaks broadened beyond detection | Stuck signal | IL2_20 (a third of amide peaks) | 1 |
| Dispersion curves are flat | Stuck signal | ADK15 (Results 4, without Mg²⁺) | 1 |
| Minor-state peaks too weak or overlapped to assign | Stuck signal | RFAH25 (Results 1) | 1 |
| A two-state model fits one experiment but fails another | Stuck signal | RFAH25 (Results 5–6) | 1 |
| Populations cannot be separated from the fit | Stuck signal | WOOD25 (χ² degeneracy); IL2_20 (R52A fit has no minimum) | 1 |
| The sample changes chemically during measurement | Stuck signal | KRAS23 (GTP hydrolysis, Methods) | 1 |
| Harsh destabilization (heat, TFE) makes the protein precipitate | Stuck signal | RFAH12 (Results 2) | 1 |
| A single peak cannot tell one fixed conformation from a fast-averaging ensemble | Stuck signal | SPOER01 (Results, Conformational Transitions ¶4) | 1 |
| Switch probe, for example amides to methyls | When stuck | IL2_20 | 1 |
| Choose the temperature to bring exchange into the window of the method being used, or vary it to tell slow from fast exchange | When stuck | ADK15 (Results 4, 20–40 °C series); BOUV11 (1 °C for slow-exchange work, 34–35 °C for assignment); FRASER09 (temperature dependence of Rex, Fig. 3) | 2+ |
| Assign weak minor-state peaks through exchange cross-peaks | When stuck | RFAH25 (Results 1) | 1 |
| Add one hidden state at a time, refit all data jointly, stop on goodness of fit | When stuck | RFAH25 (Results 5–6) | 1 |
| Read a model's failure for one variant as a different mechanism, but only with independent structural support | When stuck | SPOER01 (T35A kinetics; Ala cannot coordinate Mg²⁺). Contrast RFAH25, which added hidden states instead | 1 |
| Resolve a single-peak ambiguity with independent probes (crystal disorder, generic flexibility mutants) | When stuck | SPOER01 (Fig. 3; V29G, I36G) | 1 |
| Report only what the fit determines (exchange rate), and name what it cannot | When stuck | WOOD25 (Results, CPMG); IL2_20 (Fig. 3E,F) | 1 |
| Use gentler perturbations (interface mutant, cleavable linker) instead of harsh ones | When stuck | RFAH12 (Results 2) | 1 |
| Use a different dynamics method when standard order parameters miss the motion | When stuck | KRAS23 (Suppl. Fig. 5, NASR) | 1 |
| Report a bound, not a value, when the instrument or the fit limits the measurement | When stuck | ADK15 (Results 3, dead time); FRASER09 (population bounded at ~10% from line broadening when CPMG fitting broke, Methods) | 2+ |
| Check prolines next to doubled peaks | When stuck | ours | ours |
| Check concentration dependence | When stuck | ours | ours |
| Exchange alone does not establish a functional state | Limit | ours | ours |
| Report the parameters from the fit the authors used for their final numbers, not from fits they set aside | Routine | ours; pilot 2026-09-22: two of four Xie 2020 entries quoted χ² values from unconstrained fits the authors discarded | ours |

## Stage 5 · What is the alternative state?

| Move | Kind | Support | Status |
|---|---|---|---|
| Overlap exchanging residues with the residues a binding partner perturbs | Routine | IL2_20 (Figs. 1D,E and 2D) | 1 |
| Determine the sign of the shift differences (CEST, multi-field or zero/double-quantum CPMG) before comparing with references | Routine | KRAS23 (p.1451, signs from CEST); BOUV11 (Methods, sign experiments) | 2+ |
| Compare signed shift differences with those between reference states, region by region | Routine | KRAS23 (Table 2); RFAH25 (Results 2) | 2+ |
| Compare exchanging residues across variants of the same protein | Routine | WOOD25 (Fig. 3) | 1 |
| Read secondary structure from chemical shifts (CSI, SSP, TALOS-N) | Routine | RFAH12 (Results 2); RFAH25 (Results 2); KRAS23 (Fig. 4) | 2+ |
| Mutate a key contact; the exchange or the equilibrium should change | Routine | IL2_20 (Fig. 3E,F, R52A); WOOD25 (Fig. 5, L56A); SPOER01 (Fig. 1, T35S and T35A collapse to state 1) | 2+ |
| Add the binding partner to a mutant and check it restores the bound-like state | Routine | SPOER01 (Fig. 4, Raf-RBD and RalGDS-RBD drive T35S to state 2) | 1 |
| Repeat with a second, unrelated perturbation | Routine | IL2_20 (Fig. 5, Ro 26-4550) | 1 |
| Chemical shifts alone cannot determine the structure | Stuck signal | IL2_20 (Results); KRAS23 (p.1448) | 2+ |
| Two metrics prefer different reference states | Stuck signal | KRAS23 (Table 2, Switch I) | 1 |
| Several kinetic models fit equally well | Stuck signal | RFAH25 (Concluding remarks) | 1 |
| No known structure matches the minor state | Stuck signal | BOUV11 (identity and structure solved together) | 1 |
| Examine outlier residues one by one for local chemistry | When stuck | KRAS23 (Suppl. Fig. 2, γ-phosphate) | 1 |
| If a mutant fit does not converge, compare presence or absence of exchange | When stuck | IL2_20 (Fig. 3E,F) | 1 |
| Build a structural model from minor-state shifts and label it a hypothesis until independently validated | When stuck | RFAH25 (Results 4, CS-ROSETTA); BOUV11 (CS-Rosetta restricted to flagged regions, PDB 2LCB) | 2+ |
| Validate the modeling protocol on the ground state before trusting it on the minor state | When stuck | BOUV11 (ground-state control, 0.6 ± 0.2 Å) | 1 |
| Resolve an ambiguity in the model with an independent measurement on a mutant where the minor state dominates | When stuck | BOUV11 (J-couplings on G113A/R119P settle the Phe114 rotamer) | 1 |
| Report models the data cannot separate as unresolved | When stuck | RFAH25 (Concluding remarks) | 1 |
| Name the state by mapping to an earlier measurement of the same system | When stuck | KRAS23 (p.1449–1450, ³¹P equilibrium) | 1 |
| Write "consistent with the perturbation pattern of X", never "the structure is X", unless an independent experiment has validated the model | Limit | IL2_20; KRAS23 (structure inferred, not solved). BOUV11 calls its model "the structure" only after designed mutants and J-couplings confirmed it. SPOER01 states identity more directly; entries keep the stricter wording | 2+ |

## Stage 6 · Structure and simulation

| Move | Kind | Support | Status |
|---|---|---|---|
| Map the states to existing PDB structures and compute differences | Routine | IL2_20 (4YQX, 1M47); KRAS23 (Fig. 6); RFAH12 (2LCL against NusG); RFAH25 (2LCL) | 2+ |
| Compare structural variability in MD with NMR exchange, residue by residue | Routine | WOOD25 (Results, MD section) | 1 |
| Existing MD shows only local motion or no transition | Stuck signal | ADK15 (Results 2); our HSP90 analysis | 1 |
| The exchange is too slow for conventional MD | Stuck signal | KRAS23 (p.1454) | 1 |
| MD and NMR probe different timescales and the paper does not reconcile them | Stuck signal | WOOD25 (inferred gap) | 1 |
| No simulation exists for this system | Stuck signal | SPOER01 (2001, none); IL2_20 and RFAH12/25 (no MD run) | 2+ |
| Fit a weighted ensemble of existing crystal structures to NMR order parameters | When stuck | KRAS23 (Fig. 6) | 1 |
| Read missing electron density as disorder only after ruling out crystal packing (lattice contacts, a control structure) | When stuck | SPOER01 (Results, Crystal Structure ¶2; control PDB 6Q21) | 1 |
| Run adaptive MD steered by the residues NMR flags as exchanging (paper's own move; our agent does not run new MD) | When stuck | WOOD25 (Fig. 4) | 1 |
| Use correlated-motion networks from MD to pick which residue to mutate | When stuck | WOOD25 (Fig. S14) | 1 |
| Design a mutation that stabilizes the minor state, then invert the populations so it becomes directly measurable | When stuck | BOUV11 (Rosetta ΔΔG → G113A, then R119P; Fig. 3, Suppl. Fig. 8); FRASER09 (Ser99Thr, crystals and J-couplings, Fig. 2) | 2+ |
| When no deposited structure shows the state, look for room-temperature or multi-temperature crystal structures and density below the usual modeling threshold | When stuck | FRASER09 (48 cryo structures and a 1.2 Å cryo map showed nothing; room-temperature data plus Ringer found the minor rotamers, Fig. 1) | 1 |
| Frozen crystals can hide the minor state | Stuck signal | FRASER09 (¶2–4) | 1 |
| Compare trajectory length with the exchange time before reading absence as evidence | When stuck | ours; HSP90 lesson | ours |
| An MD cluster chosen by the same residues NMR flagged is weaker identity evidence than an independent structure | Limit | WOOD25 (inferred circularity) | 1 |
| A short simulation without a transition cannot refute the state | Limit | ours; ADK15 and KRAS23 both decline to use MD as counter-evidence | 2+ |
| Do not assign a label the paper does not assign, such as which MSM macrostate is the active state | Limit | ours; pilot 2026-09-22: two of four Pontiggia 2015 entries | ours |

## Stage 7 · Functional relevance

| Move | Kind | Support | Status |
|---|---|---|---|
| Determine which state the ligand or partner binds | Routine | BOUV11 (three-state fit with benzene: only the ground state binds); SPOER01 (effectors drive T35S into state 2, Fig. 4); IL2_20 (antibody-like open state, Discussion) | 2+ |
| Measure binding affinity for variants that shift the population | Routine | IL2_20 (Fig. 3G, ITC); WOOD25 (Fig. 6, SPR); BOUV11 (binding-competent fraction 97% → 66% → <5%, Fig. 4) | 2+ |
| Measure cellular signaling for those variants | Routine | IL2_20 (Fig. 3H); WOOD25 (Fig. 6, pSTAT5) | 1 |
| Link to phenotype with genetics or reporters in cells | Routine | RFAH12 (Results 3–4) | 1 |
| Compare variant dynamics with activity rates from the literature | Routine | KRAS23 (p.1453) | 1 |
| Relevance is only proposed ("may be instrumental") | Stuck signal | KRAS23 (p.1452–1453) | 1 |
| Affinity cannot be measured by NMR | Stuck signal | RFAH12 (Results 5) | 1 |
| Use control mutations that change something else (stability, chemistry) to show the effect comes from the state | When stuck | WOOD25 (V84A, stability-matched); FRASER09 (Arg55Lys, chemistry-only; plus an independent KD to rule out binding, Fig. 4a) | 2+ |
| Prove that a state does not bind by fitting that rate and testing it against zero | When stuck | BOUV11 (kEB, kBE < 0.1 s⁻¹, F-test) | 1 |
| When an affinity measurement runs out of range, switch readout instead of stopping | When stuck | RFAH12 (Results 5: functional phenotype instead of Kd); SPOER01 (NMR peak integrals, then line broadening against ligand concentration) | 2+ |
| A correlation between population and activity across variants does not show cause | Limit | KRAS23 (hedged wording) | 1 |
| Losing a binding ability can be the functional relevance, not only gaining one | Limit | BOUV11 (excited state cannot bind benzene) | 1 |

## Stage 8 · Write the entry and review

| Move | Kind | Support | Status |
|---|---|---|---|
| Report null results and failed methods explicitly | Routine | SPOER01 (Results, Kinetics ¶3: no fluorescence signal) | 1 |
| Tiers, claim limits, reviewer agent, human sign-off | Routine | ours | ours |
| Keep the authors' hedges: "apparently", "these data indicate" and "might be partially due to" do not become "shows", "measured" or "attributed"; do not write "conformational selection" without binding kinetics | Limit | ours; pilot 2026-09-22: 8 of 19 over-claims, four in each group | ours |
| Before finishing, check that the entry gives the range of chemical-shift differences | Routine | ours; pilot 2026-09-22: none of the eight Stiller 2022 and Xie 2020 entries gave it | ours |

No paper documents how entries are reviewed; this stage is our design and needs Gina's view on which stages require a person.
