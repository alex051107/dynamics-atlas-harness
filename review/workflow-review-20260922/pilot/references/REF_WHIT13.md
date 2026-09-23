# REF_WHIT13: Whittier, Hengge & Loria, Science 2013;341:899-903

Sources read: PMC4078984 main text, Figs. 1-4 and Table 1; the paper's supplement (NIHMS592895 Supplemental_Material.docx, the PMC-hosted file, read from its 2024-04-23 Internet Archive capture because PMC's own link is reCAPTCHA-gated); PDB 1SUG, 3EB1, 2I42, 3I80, 1YPT, 2HNP and BMRB 19272, all cited by the paper. Locators: "¶n" is the nth paragraph of the PMC main text (¶3 begins "The apo (ligand-free) forms"); "SM <heading>" is a supplement section.

## PART 1: REFERENCE ENTRY

1. **Protein**: Human PTP1B and YopH, "a virulence factor from Yersinia" [paper, ¶2]. YopH species not stated (authors' BMRB 19272: *Y. pestis*; cited PDB 1YPT/2I42: *Y. enterocolitica*); UniProt not stated (cited PDB entries: P18031, P15273) [our reading of the paper's data: BMRB/PDB].

2. **Construct and conditions**: Wild-type PTP1B 1-298 and the YopH catalytic domain Yop51*Δ162 (residues 163-468), 2H/15N(/13C)-labelled. Eight PTP1B WPD-loop point mutants (e.g. W179F, F182A, A189V) were used only for assignment [paper, SM Protein Expression, SM Assignments; Fig. S1a]. No cofactor. Buffer: 20 mM Bis-Tris propane pH 6.5 with NaCl, DTT, EDTA and 7% D2O [paper, SM Protein Expression]. 293 K [paper, SM NMR Relaxation Experiments; BMRB 19272]; the SM kinetics section says 23 °C [our reading of the paper's data]. Fields: 15N CPMG at 600/800 MHz; for apo YopH, 15N CPMG at 800, 15N R1ρ at 900 and Hahn echo at 600 MHz; 1H R1ρ field not stated [paper, Figs. 2, 4, S4, S6].

3. **Apo relative to**: The phosphotyrosine substrate (modelled by the non-hydrolysable F2Pmp peptide Ac-DADEXLIP-NH2) and any active-site oxyanion (phosphate, tungstate, vanadate). Apo samples are "ligand-free" [paper, ¶3] in an oxyanion-free buffer. Vanadate appears only in crystal structures (Fig. 1); tungstate only in assignment checks and lineshape titrations, never in dispersion experiments [our reading of the paper's data, SM].

4. **Verdict**: PTP1B **strong**: two-field CPMG shows a minor closed-loop state in the ligand-free enzyme, and independent peptide-bound and structure-calculated shifts match its |Δω| (Table 1). YopH **weak**: exchange is detected, but its Δω and population were not measured, so the closed identity is assumed [our reading of the paper's data, ¶5-¶6, Table 1].

5. **Major state**: Open WPD loop. PTP1B pa = 97.5 ± 1.4% (Keq open/closed 40); YopH ≈97% (97.0 ± 0.5% from S361, 97.4% from A359; Keq 34) [paper, ¶3, ¶6, Table 1, SM Hahn-Echo]. Structures: apo open PTP1B crystals (ref. 22, e.g. 2HNP); YopH 1YPT, the only apo structure [paper, ¶4; SM Estimation].

6. **Alternative state(s)**: Closed, catalytically competent WPD loop (a ~10 Å move) that places the general acid (PTP1B D181, YopH D356) at the leaving-group oxygen [paper, ¶2, Fig. 1B]. Populations: PTP1B pb 2.5%, YopH ≈3% [paper, ¶3, ¶6]. Structures: for PTP1B, 1SUG (apo, closed) plus 21 other closed entries (e.g. vanadate complex 3I80); for YopH, 10 closed entries (e.g. vanadate complex 2I42), none apo [paper, ¶4; SM PDB lists]. 1SUG holds an active-site glycerol that contacts F182 and A217 [our reading of the paper's data: PDB 1SUG]. Excluded as not apo: peptide-bound states (open minor ≈13% PTP1B, ≈1% YopH) and tungstate complexes [our reading of the paper's data, Table 1].

7. **Evidence type**: PTP1B: 15N TROSY relaxation-compensated CPMG. YopH: flat 15N CPMG and R1ρ (kex ≥30,000 s-1), a modified TROSY-detected off-resonance 1H R1ρ (Fig. S5), and 15N TROSY Hahn-echo Rex [paper, ¶3-¶6; Figs. 2, 3, S4-S6].

8. **Exchange parameters**: PTP1B apo: kex 920 ± 190 s-1, kclose 22 ± 5, kopen 890 ± 190 s-1; |Δω| A189 3.8 ± 0.6, F182 3.4 ± 1.3, W179 2.8 ± 0.9 ppm (W179 from Rex 31.4 ± 4.6 s-1 with pa fixed) [paper, ¶3, Table 1]. YopH apo: kex 43,000 ± 6,200 s-1, kclose 1,240 ± 200 (text ± 280), kopen 42,000 ± 6,000 s-1; Δω not determined; Hahn-echo Rex S361 3.94 ± 0.36 and A359 0.99 ± 0.12 s-1 [paper, ¶5-¶6, Table 1, SM Hahn-Echo]. The reported YopH populations follow from the ShiftX2 proxies (6.4 and 3.4 ppm at 600 MHz). The measured-shift proxy that ¶6 names gives ≈92% (S361) and ≈98% (A359) [our reading of the paper's data; ppm conversion: background knowledge]. Not apo, for comparison: peptide-bound kclose/kopen 30 ± 4/4.5 ± 1 s-1 (PTP1B) and 1,770 ± 240/18 ± 2 s-1 (YopH); bound |Δω| 3.2-4.5 ppm [paper, ¶7-¶8, Table 1].

9. **Residues or regions**: WPD loop (ten residues per ¶2, nine per SM). Probes: PTP1B W179, F182, A189 (G183 and S187 too weak, V184 overlapped); YopH A359, S361 (T358 overlapped, V360 too broad) [paper, ¶3, ¶5; SM Assignments].

10. **Identity basis**: PTP1B: fitted |Δω| ≈ ΔδmeasN (apo vs peptide-bound: A189 3.87, F182 3.60 ppm) ≈ ΔδcalcN (ShiftX2 on closed crystal structures: A189 3.7 ± 0.2, F182 4.9 ± 1.0, W179 1.9 ± 0.5 ppm), plus the apo closed structure 1SUG [paper, ¶4, Fig. 3, Table 1]. The SM concedes poor calculated agreement for F182 (its cited Fig. S8 is missing) [paper, SM Estimation]. YopH: ΔδmeasN ≈ ΔδcalcN (A359; S361 agrees poorly) supports a closed peptide-bound loop. For the apo exchange, "closed" is assumed to derive pb, not tested [paper, ¶5-¶6; inference].

11. **Structural mapping and simulations**: ShiftX2 was run on 22 closed and 9 open PTP1B entries and on 10 closed and 1 open YopH entries. Fig. 1 uses 2I42 and 3I80. 3EB1 (inhibitor-bound, loop open) is cited as precedent for an open loop with ligand bound [paper, ¶4, ¶7, SM]. No MD here (acknowledged Monte Carlo simulations: purpose not stated). The cited MD (ref. 30) sampled open↔partially closed YopH, not the 22 µs open↔fully closed exchange seen by NMR [paper, ¶9, Acknowledgments].

12. **Functional relevance**: The loop must be closed for chemistry [paper, ¶6]. The substrate mimic favours the closed state by slowing opening (PTP1B 890→4.5, YopH 42,000→18 s-1) while kclose barely changes (22→30 and 1,240→1,770 s-1) [paper, ¶7-¶8, Table 1]. kclose tracks kcleavage (PTP1B 30-80 s-1; YopH 1,400-2,000 s-1, estimated as 2-3× kcat of 700 s-1). The authors suggest that closure is concerted with leaving-group protonation [paper, ¶4, ¶6-¶8, SM Enzyme kinetics]. Product-mimic tungstate koff is similar for both (YopH 16,400, PTP1B 18,000 s-1) [paper, ¶8, SM Lineshape].

13. **Competing explanations addressed**: Concerted vs local motion: similar per-residue kex before global fitting [paper, ¶3]. Minor-state identity: three-way shift comparison [paper, ¶4]. Faster (ns) fluorescence and MD motion in apo YopH: fluorescence reports only a Trp side chain; the bound-state T-jump difference: a different ligand [paper, ¶9]. Hydrolysis limiting kcat: kclose compared with kcleavage, not kcat [paper, ¶2, SM kinetics]. Product release: similar tungstate koff [paper, ¶8]. Not addressed: peptide association/dissociation as a source of the "bound" dispersion, and the sign of Δω [inference].

14. **What this evidence cannot support**: Loop closure causing cleavage: only rates agree; nothing perturbed the dynamics. A measured YopH population, Δω or kcleavage. An atomic identity for the minor state beyond the 15N shifts of two or three residues. The proline speculation in ¶11. Tungstate-bound loop kinetics: only ligand koff was measured [inference].

15. **Provenance**: DOI 10.1126/science.1241735; PMC4078984 (NIHMS592895); PMID 23970698. Figs. 1-4 and Table 1; SM Methods and Figs. S1-S7 (the SM's Fig. S3 is mislabelled "Fig. S1"). BMRB 19272 (apo YopH). PDB 1SUG, 3EB1, 2I42, 3I80, 1YPT, 2HNP.

## PART 2: MUST-GET-RIGHT

- **Apo means ligand-free wild-type enzyme**: no substrate-mimic peptide and no tungstate, vanadate or phosphate, in Bis-Tris propane at pH 6.5 and 293 K. The apo dispersion (Fig. 2, the Table 1 "apo" rows, Figs. S4 and S6) meets the definition. The peptide-bound data (Fig. 4) and the tungstate data (Fig. S7) do not. [¶3; Fig. 2 and Fig. 4 legends; SM Protein Expression, NMR Relaxation Experiments, NMR Lineshape Analysis]
- **The verdict splits by protein**: PTP1B is strong; YopH is weak because its Δω and population were not measured and the closed identity is assumed. [Table 1; ¶4-¶6; SM Hahn-Echo]
- **States**: Both apo enzymes have an open major state and a closed minor state. The closed loop is the catalytically competent conformation that places D181 (PTP1B) or D356 (YopH) at the leaving group. Populations: PTP1B 97.5 ± 1.4% / 2.5%; YopH ≈97% / ≈3%. [¶2-¶4, ¶6; Fig. 1B; Table 1]
- **PTP1B apo numbers**: 15N CPMG at 600/800 MHz on W179, F182 and A189; kex 920 ± 190 s-1; kclose 22 ± 5 s-1; kopen 890 ± 190 s-1; |Δω| 2.8-3.8 ppm. [¶3; Fig. 2B-C; Table 1]
- **YopH apo numbers**: 15N CPMG and R1ρ are flat. TROSY 1H R1ρ on A359 and S361 gives kex 43,000 ± 6,200 s-1; Hahn-echo Rex plus a shift proxy gives pa ≈97%; kclose 1,240 s-1, kopen 42,000 s-1. [¶5-¶6; Fig. 2D; Figs. S4-S6; Table 1]
- **Identity basis (PTP1B)**: fitted |Δω| ≈ ΔδmeasN (apo vs peptide-bound) ≈ ΔδcalcN (ShiftX2 on closed crystal structures), plus the apo closed crystal structure 1SUG. [¶4; Fig. 3; Table 1; SM Estimation of Chemical Shift Differences]
- **Ligand effect**: The non-hydrolysable F2Pmp peptide makes the closed loop the major state (≈87% in PTP1B, 99% in YopH). It does so by slowing opening about 200-fold and 2,300-fold while kclose barely moves (30 and 1,770 s-1). [¶7-¶8; Fig. 4; Table 1]
- **The functional link is a rate correlation**: kclose ≈ kcleavage. PTP1B's kcleavage of 30-80 s-1 is derived from kcat and khydrolysis; YopH's 1,400-2,000 s-1 is estimated. The authors only "suggest" that closure is concerted with leaving-group protonation. [¶2, ¶4, ¶6-¶8; SM Enzyme kinetics]
- **Provenance anchors**: DOI 10.1126/science.1241735; BMRB 19272; PDB 1SUG (apo, closed), 3EB1 (inhibitor-bound, open), 2I42 and 3I80 (vanadate, Fig. 1), 1YPT (apo YopH, open). [¶4, ¶7; Fig. 1; SM]

## PART 3: OVER-CLAIMS

- **"The apo loop dynamics were measured with vanadate or tungstate present, so the entry is not included."** Vanadate is only in the Fig. 1 crystal structures, and tungstate only in assignment checks and the Fig. S7 titrations. All apo dispersion data come from ligand-free enzyme.
- **"The open loop of the peptide-bound enzyme (≈13% PTP1B, ≈1% YopH) is an alternative apo state."** It exists only with saturating substrate mimic bound. It is a catalytic-cycle, Michaelis-complex-like state, not an apo state.
- **"Loop closure is the rate-limiting step of, or causes, phosphoryl transfer."** The paper shows only that kclose ≈ kcleavage and "suggests" coupling; no mutant, isotope or perturbation test connects the motion to the chemistry.
- **"NMR measured the YopH minor state as a 3% closed loop."** Only kex and Rex were measured. pb follows from assuming that Δω equals an open-closed shift difference, and the other available proxy gives 92-98% for the major state.
- **"YopH kclose matches its measured kcleavage."** YopH kcleavage (1,400-2,000 s-1) is estimated as 2-3× kcat by analogy with PTP1B, not measured.
- **"WPD-loop mutants confirm that the dynamics matter, and the extra prolines slow the PTP1B loop."** The mutants were used only to assign peaks; the proline idea is untested speculation (¶11).
- **"The apo minor state is the 1SUG (or vanadate-complex) structure."** The identity rests on 15N shift magnitudes of two or three residues, with the sign unknown and poor calculated agreement for F182. 1SUG also has a glycerol in the active site.
- **"Peptide binds by conformational selection, and kclose is proven identical with and without ligand."** No peptide binding kinetics were measured, and peptide association/dissociation was not separated from loop motion. kclose rises about 1.4-fold, and the tungstate-bound loop kinetics were inferred from koff rather than measured.

## ERRATA AFTER INDEPENDENT CHECK (applied before grading)

A separate checker compared this reference with the paper and its supplement (see CHECK_WHIT13.md). All must-get-right items were confirmed, both verdicts (PTP1B strong, YopH weak) and both "apo relative to" fields were judged defensible, and no over-claim item turned out to be supported by the paper. Notes:

- Part 1, item 2: the eight PTP1B WPD-loop mutants and their assignment-only use are correct, but the mutant spectra are in supplementary Fig. S1b–d; Fig. S1a is the sequence alignment.
- Disputed: whether A359 or S361 shows the poorer agreement between measured and calculated shifts in apo YopH. Table 1 supports the reference (S361 agrees poorly); the supplement's prose literally names A359, apparently a typo. Do not count either reading as a factual error.
- Not verified: that the 1SUG glycerol contacts F182 and A217 specifically (glycerol presence is confirmed). Do not penalize an entry that omits this or states it differently.
- The YopH Hahn-echo Rex values (S361 3.94 ± 0.36, A359 0.99 ± 0.12 s⁻¹) are not printed in the paper or supplement; the checker recomputed them from Table 1 and they match.
