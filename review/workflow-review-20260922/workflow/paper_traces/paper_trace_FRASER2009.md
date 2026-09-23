# Workflow trace — Fraser et al. 2009, Nature 462(7273):669–673 (CypA proline isomerase)

## 1. ACCESS
Read via Europe PMC full-text XML (PMC2805857/fullTextXML): verbatim paragraphs, all 4 figure legends, Methods Summary + Full Methods, footnotes, references; cross-checked against the PMC HTML page. Actual title is "Hidden **alternate** structures…", not "alternative." Supplementary Information is a separate PDF (footnote FN1), not opened per the no-download rule — SI content below is only what the main text says about it. No BMRB accession appears in the main text.

## 2. SYSTEM AND STATES
Human cyclophilin A (CypA), a peptidyl-prolyl cis/trans isomerase (¶1). Constructs: wild-type; new point mutants Ser99Thr and Arg55Lys (new crystals + NMR here); Lys82Ala (Eisenmesser et al. 2005, ref. 4, used as comparator). Every sample is the free enzyme — no substrate or ligand anywhere in this paper (¶1: "the free enzyme samples the same two conformations"). Major state = conformation in ordinary cryogenic crystallography and the dominant NMR peak; minor/alternative state = a millisecond-exchange, low-population conformation of the same free enzyme, known only from NMR before this paper (ref. 4), never resolved crystallographically (¶1–2, Supp. Fig. 1). Apo is relative to CypA's peptide substrate (e.g., AAPF): the minor conformation is argued to resemble the enzyme's own substrate-bound conformation (¶1, ¶5) — never phrased as "apo relative to X"; that framing is INFERRED.

## 3. WORKFLOW TRACE
1. **[St.1, EXPLICIT]** Definitions inherited from ref. 4: free CypA has a known major/minor exchange; apo = no ligand here. ¶1.
2. **[St.2, EXPLICIT]** Superpose 48 existing CypA PDB structures (apo + liganded) for backbone RMSD, before any new experiment. ¶1; Supp. Fig. 1.
3. **[St.6, EXPLICIT]** First attempt fails: 1.2 Å cryo structure, standard 1σ building, no heterogeneity. Ringer (dihedral scan, 0.3σ cutoff; validated on 402 structures ≥1.5 Å, >15% show real sub-threshold peaks) on the same map finds only active-site rotamers (Met61/Arg55), not Leu98/Ser99. ¶2.
4. **[St.6, EXPLICIT]** New room-temperature data (15 °C, 96% humidity, 1.39 Å) + Ringer adds Leu98/Ser99; manual inspection (prompted by a modeled Ser99–Phe113 clash) finds Phe113's rotamer, missed by Ringer itself; bias-free omit maps confirm all three. ¶3–4; Fig. 1.
5. **[St.5, EXPLICIT]** Propose identity: the coupled Leu98/Ser99/Phe113 rotamer network is the structural basis of the NMR minor state; alternate Phe113 proposed to explain the large chemical-shift differences. ¶4–5; Fig. 1d.
6. **[St.1/4 via new construct, EXPLICIT]** Design Ser99Thr (>14 Å from Arg55) to favor the minor rotamers; crystallize (1.6, 2.3 Å) → Phe113 found only in the former minor rotamer, confirmed independently by solution J-coupling NMR (χ1 flips +60°→−60°). ¶6; Fig. 2.
7. **[St.4, EXPLICIT]** Confirm exchange is still real, not statically trapped: shift direction matches (exceeds) the Lys82Ala reference; CPMG shows group-I still exchanges, ~60-fold slower (k1 = 1.0±0.3 s⁻¹ at 10 °C vs ~60 s⁻¹ WT), now slow-exchange per REX-temperature trend and B0 α (0.16 vs 2.0). ¶7–8; Fig. 3.
8. **[St.4, stuck-fix, EXPLICIT]** Standard CPMG fitting not robust in this new slow regime (no minor peak resolved); population bounded indirectly at ~10% upper limit from line-broadening; k1 stays well-determined from REX alone. Methods "NMR Methods" ¶2.
9. **[St.7, EXPLICIT]** Function: kcat/KM 300-fold lower for Ser99Thr; Arg55Lys (chemistry-only mutant, dynamics/structure unperturbed) gives a similar drop; KD only 3–6-fold weaker for both (6.7±0.8, 11.3±2.5 mM) → defect is turnover, not binding (¶9; Fig. 4a). Direct ZZ-exchange NMR confirms it: kcatisom WT 1.3×10⁴±800 s⁻¹ → Ser99Thr 1.9×10²±20 s⁻¹ (~70-fold), matching the ~60-fold slowed free-enzyme k1 — the paper's central claim (¶10–11; Fig. 4b,c).

## 4. STUCK POINTS
- **48 existing structures + a new 1.2 Å cryo structure show nothing** (steps 2–3): high resolution alone isn't enough. Next: mine density below the modeling threshold instead of another cryo structure. EXPLICIT, ¶1–2.
- **Ringer-on-cryo incomplete, then blind to Phe113** (steps 3–4): the automated method covers only the active site, then misses a residue whose backbone shift hides its density inside the major rotamer. Next: change the physical condition (room temperature — "crystal freezing can alter conformational distributions") and fall back to manual, hypothesis-driven inspection for what the algorithm misses. EXPLICIT, ¶2–4.
- **Minor state too rare/fast to study directly in WT** (step 6): instead of a knockout that abolishes exchange, engineer a mutation that stabilizes and inverts the equilibrium, then cross-validate the "trap" by crystallography plus independent solution NMR. EXPLICIT, ¶6.
- **Standard CPMG fitting breaks in the new slow-exchange regime** (step 8): no minor peak resolved, so population can't be fit directly. Next: use REX magnitude alone for rate, and bound (not measure) population from line-broadening theory. EXPLICIT, Methods "NMR Methods" ¶2 — the most transferable move found here, absent from the current card.
- **Attributing the catalytic defect specifically to dynamics** (step 9): one kinetic number can't separate binding, chemistry, and dynamics as the cause. Next: an independent KD (rules out binding), a second, mechanistically distinct mutant that breaks chemistry instead (Arg55Lys, similar defect), and a dynamics-independent kinetic method (ZZ-exchange) whose fold-change is checked against k1's fold-change. EXPLICIT, ¶9–11.

## 5. HOW THE ALTERNATIVE STATE WAS ESTABLISHED
Detection: NMR relaxation dispersion in free CypA (ref. 4; extended here by showing the same exchange persists, ~60-fold slower, in Ser99Thr, ¶8). Identity: room-temperature crystallography resolves a coupled Leu98/Ser99/Phe113 rotamer network below the 1σ threshold, cross-validated by independent solution J-coupling NMR (Phe113 χ1 +60°→−60°, ¶3–4,6). Structure: 6 new/re-refined crystal structures, PDB 3K0M–3K0R (footnote FN4; which code maps to which construct is not stated). Function: 300-fold drop in kcat/KM and ~70-fold drop in directly measured kcatisom (1.3×10⁴→1.9×10² s⁻¹, ¶10), matching the ~60-fold slowed exchange rate (¶11) — identity and function rest on one rate-matching argument, not separate steps.

## 6. COMPARISON WITH THE DRAFT CARDS
**(a) MATCHES**
- Card 2, "Search wide first and filter later" ↔ 48-PDB comparison before any new experiment (step 2).
- Card 4 try #6, "Cross-validate with a second method" ↔ J-coupling validating the crystal rotamer flip (step 6); ZZ-exchange validating the assay (step 9).
- Card 5, "Compare signed chemical-shift differences with those between reference states" ↔ Ser99Thr-vs-WT shifts vs Lys82Ala (step 7).
- Card 7, "whether mutations that shift the population change binding or activity" ↔ step 9 (kcat/KM, KD for both mutants).

**(b) NEW MOVES**
- Sub-threshold density mining (0.3σ) around every side-chain dihedral, not just 1σ, plus a frame-subset radiation-damage check as the crystallographic artifact test Card 4 doesn't have — Card 6 routine move (steps 3–4).
- New room-temperature data collection because freezing itself suppresses the state, not just reusing depositions — Card 6, "when stuck: no matching structure" (step 4).
- Engineering a stabilizing, population-inverting mutation, distinct from "remove a contact, exchange should vanish" — Card 5, "when stuck" (step 6).
- Bounding, not measuring, a population from peak absence plus line-broadening theory when standard fitting breaks — Card 4, "when stuck" (step 8).

**(c) CONTRADICTIONS**
- Card 3 treats conditions like temperature as a comparability hazard to flag; here temperature is varied deliberately as the core diagnostic separating slow- from fast-exchange residues (step 7) — a method, not a confound.
- Card 6 matches states only to existing PDB structures and excludes new simulation, saying nothing about new crystallography; here all existing structures failed and the decisive evidence needed genuinely new data under new conditions plus a purpose-built method (steps 2–4) — search-only would have wrongly landed on "unmapped."

## 7. DEFINITION ISSUES
- **Visible vs invisible, twice over**: never a resolved, separate NMR peak — not in WT (fast exchange, CPMG-only) and not even in the "trapped" Ser99Thr mutant (slow exchange, peak broadened past detection, population bounded at <~10%). Both leave the state invisible, testing Card 1's "visible second peak" vs "invisible, CPMG/CEST-only" as a clean binary.
- **Crystal vs solution**: the atomic model comes from one crystal lattice's sub-1σ density, linked to the solution NMR state only by chemical-shift direction-matching plus an independent J-coupling angle — an indirect cross-resource identity claim, not a shared direct observable.
- **Catalysis context collapses Cards 4–6 into Card 7**: the minor conformation is functionally defined by resemblance to the substrate-bound state, and the same rate-matching argument (¶11) argues both that the state is real/identified and that it is functionally relevant. The draft cards' boundary between "establish the state" and "test whether it matters" does not hold for this system.
