# How Well Do Molecular Dynamics Force Fields Model Peptides? A Systematic Benchmark Across Diverse Folding Behaviors

**Authors:** Bhumika Singh, Yenny Martinez-Noa, Alberto Perez
**Year:** 2026
**Venue:** Journal of Physical Chemistry B (OA copy via bioRxiv preprint 10.1101/2025.07.31.667969)
**DOI:** 10.1021/acs.jpcb.6c01176
**Source PDF URL:** https://www.biorxiv.org/content/10.1101/2025.07.31.667969v1.full.pdf
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

How Well Do Molecular Dynamics Force Fields
              Model Peptides? A Systematic Benchmark
                           Across Diverse Folding Behaviors

                   Bhumika Singh,†,¶ Yisel Martı́nez-Noa,†,¶ and Alberto Perez∗,†,‡

                   †Department of Chemistry, University of Florida, Gainesville, FL, USA
                    ‡Quantum Theory Project, University of Florida, Gainesville, FL, USA
                                      ¶These authors contributed equally to this work

                                                     E-mail: perez@chem.ufl.edu


                                                                  Abstract

                  Linear peptides play essential roles in biology and drug discovery, frequently medi-

             ating protein–protein interactions through short, flexible motifs. However, their struc-

             tural plasticity—ranging from disordered to context-dependent folding—makes them

             challenging targets for molecular simulations. In this work, we benchmark the perfor-

             mance of twelve popular and emerging fixed-charge force fields across a curated set of

             twelve peptides spanning structured miniproteins, context-sensitive epitopes, and dis-

             ordered sequences. Each peptide was simulated from both folded (200 ns) and extended

             (10 µs) states to assess stability, folding behavior, and force field biases. Our analysis

             reveals consistent trends: some force fields exhibit strong structural bias, others allow

             reversible fluctuations, and no single model performs optimally across all systems. The

             study highlights limitations in current force fields’ ability to balance disorder and sec-

             ondary structure, particularly when modeling conformational selection. These results





             offer practical guidance for peptide modeling and establish a benchmark framework for

             future force field development and validation in peptide-relevant regimes.


     Introduction

     Peptide epitopes—short regions within proteins that mediate molecular recognition—play
     central roles in biology and drug discovery. Many cellular interactions are driven by such
     short linear motifs 1,2 , which bind to specific partner proteins and often undergo disorder-to-
     order transitions in the process 3 . This structural plasticity is both biologically important
     and a significant modeling challenge.
          Peptides are particularly attractive drug candidates because they can engage extended
     and shallow protein surfaces that are typically inaccessible to small molecules 4 . Advances
     such as peptide cyclization have improved their proteolytic stability and membrane perme-
     ability, further boosting their therapeutic potential 5 . Accurate modeling of peptide structure
     and binding is thus crucial for structure-based design of peptide therapeutics, peptidomimet-
     ics, and small molecules that mimic peptide–protein interactions.
          Yet, modeling peptides remains difficult. Many peptides are intrinsically disordered in
     isolation and only fold upon binding to a target 6,7 . Others form defined secondary structures
     under specific solution conditions, but not others 8,9 . A singular protein receptor might
     recognize different peptide sequences via distinct binding modes (e.g., peptide binds as a
     helix or hairpin) 10 , while a given peptide sequence may bind different protein receptors by
     adopting different structures 11,12 . This environmental sensitivity places peptides near the
     edge of structural stability, where small changes in sequence, solvent, or receptor can trigger
     large conformational shifts. Unlike globular proteins, which are stabilized by dense networks
     of non-bonded interactions, peptides often lack such extensive stabilizing contacts 13,14 . As a
     result, even small inaccuracies in the force field can lead to significant errors in conformational
     preferences 15–17 .





          From a computational standpoint, peptides are small enough that conformational sam-
     pling is not generally a limiting factor. However, their responsiveness to small perturbations
     makes them especially susceptible to force field biases 18–20 . For instance, modest secondary
     structure preferences encoded in a force field may not strongly affect the native fold of a
     protein but can dominate the ensemble of a flexible peptide 21 . Despite recent improvements,
     traditional force fields were largely developed and parameterized to describe well-folded pro-
     teins, often leading to over-compact ensembles for disordered systems.
          Increasing computer time and access to better benchmark experimental data have shown
     several force field deficiencies, such as inaccurate helical propensities or incorrect compaction
     in disordered proteins 22,23 . This has led to an explosion in the number of groups participating
     in force field development as well as the number of available force fields. Yet, many of these
     developments have focused on large protein systems, and it remains unclear which force fields
     best describe peptides across different structural regimes 24,25 .
          In this work, we systematically assess the performance of 11 modern force fields across
     a benchmark set of 12 peptides. These include peptides that are structured in solution,
     intrinsically disordered peptides, and peptides that remain disordered in water but fold
     in alternative solvent environments. We evaluate both structure stability (via simulations
     initiated from folded states) and folding behavior (via simulations initiated from extended
     conformations). While no force field performs optimally in all cases, our results reveal
     meaningful trends and biases, offering practical guidance for researchers modeling peptide-
     mediated interactions.


     Computational Methods

     Systems of study

     A total of twelve peptides (see Table 1) were selected as model systems to evaluate and
     compare force fields.





                                     Table 1: Benchmark systems used in this study.

       Name                                  PDB ID           Method            Sequence
       Miniproteins

       tc5b                                  1L2Y 26          NMR               NLYIQWLKDGGPSSGRPPPS
       tryptophan zipper 2                   1LE1 27          NMR               SWTWENGKWTWK
                                                                                DHYNCVSSGGQCLYSACPIFTKIQGT
       human beta-defensin-1                 1IJU 28          X-ray
                                                                                CYRGKAKCCK

       Partially Structured Peptides

       protein G C-termini                   1GB1 29          NMR               GEWTYDDATKTFTVTE
       ribonuclease A C-peptide              5RSA 30          X-ray             AETAAAKFLRAHA
       analog
       EK peptide                            –                CD 31             YAEAAKAAEAAKAF

       Structured Upon Binding

       matα2                                 1MNM 32          X-ray             VFNVVTQDMINKST (Residue 115–128)
       nrf2 peptide                          2FLU 33          X-ray             AFFAQLQLDEETGEFL
       dynorphin A                           2N2F 34          NMR               YGGFLRRIRPKLK

       Disordered in Water, Ordered in Solvent Mixtures
                                                                                HAEGTFTSDVSSYLEGQAAKEFIAWL
       glucagon-like peptide-1-              1D0R 35          NMR
                                                                                VKGR
       (7–36)-amide
       proadrenomedullin N-20                2FLY 36          NMR               ARLDVASEFRKKWNKWALSR
       terminal
       phylloseptin-1                        2JQ0 37          NMR               FLSLIPHAINAVSAIAKHNX


     Force field choices

     We took some traditional force fields ff19SB, 38 ff99SB, 39 and charmm36m 40 commonly used
     in the field, as well as some IDP optimized force fields ff99IDPs, 41 ff14IDPs, 42 ff14IDPSFF, 43
     C36IDPSFF, 44 OPLDIDPSFF, 45 and some physics-enhanced modern force fields a99SBdisp, 15
     Des-Amber. 46 For each force field, we used the water model recommended for it (see table
     2). While this is not an exhaustive list of force fields, it is representative of different trends
     in the field and readily available for running simulations.





        Table 2: Summary of force fields and water models employed in this benchmark study.

                                      Forcefield                            Water Model
                                      ff19SB                                OPC 47
                                      ff99SB                                OPC 47
                                      ff99IDPs                              TIP3P 48
                                      ff14IDPs                              TIP3P 48
                                      ff14IDPSFF                            TIP3P 48
                                      OPLSIDPSFF                            TIP4P 48
                                      a99SBdisp                             a99SBdisp-water 15
                                      DES-Amber                             TIP4P-D 49
                                      DES-Amber-SF1.0                       TIP4P-D 49
                                      Charmm36m                             TIP3P 48
                                      C36IDPSFF                             TIP3P 48


     Simulation protocols

     Molecular dynamics simulations were performed using twelve force fields, including variants
     incorporating CMAP corrections. The force fields examined in this study, along with their
     recommended water models, are summarized in Table 2. Molecular dynamics simulations
     were conducted using GROMACS 50 and Amber, 51,52 according to the availability of the
     corresponding force field. We use hydrogen mass repartitioning with a 4 fs timestep, and
     we saved frames every 20ps. Simulations initiated from the unfolded state ran for 10 µs and
     those starting from the folded state ran for 200 ns.


     AMBER protocols

     For the AMBER simulations, we solvated the systems employing tleap with the initial pa-
     rameters of the force fields ff14SB 53 , ff99SB, and f19SB initially, and the peptides were
     solvated in 8 Å water buffer in a truncated octahedron. We used cloride or sodium neu-
     tralizing ions and brought up their concentration to 0.1M , randomizing their positions. For
     the force fields ff14IDPs and ff14IDPsFF, we first initialized the systems using ff14SB pa-





     rameters and subsequently applied the corresponding CMAP corrections. Similarly, systems
     using ff99IDPs were initialized with ff99SB and then updated with the CMAP corrections
     specific to ff99IDPs. For charmm36m we prepared our input through the CHARMMGUI
     platform 54–56 , using the solution builder input generator, likewise we add sodium and chlo-
     rine ions in an 8 Å water octahedron box. All minimization steps were performed using
     the sander module from AMBER20 51 . A series of restrained energy minimizations were
     conducted to gradually relax the system while maintaining the structural integrity of the
     solute. The protocol involved six sequential minimization steps with harmonic positional
     restraints applied to all non-hydrogen atoms of the solute, progressively decreasing the re-
                                                         −2                           −2                                                 −2
     straint weight from 50 kcal mol−1 Å                     to 5 kcal mol−1 Å           in increments of 10 kcal mol−1 Å .
     The final minimization step was performed without restraints. Each minimization was car-
     ried out using 4000 total steps, with the first 2000 steps utilizing steepest descent, followed
     by conjugate gradient minimization for the remaining steps. Restraints were applied to all
     atoms except hydrogen and water molecules. The system was first thermalized over 5 ns,
     gradually increasing the temperature from 0 K to 298.15 K using Langevin dynamics 57–59
     with a collision frequency of 1 ps−1 to control temperature fluctuations. Following this, a
     10 ns equilibration step was carried out with positional restraints on the solute and periodic
     boundary conditions were enforced. Additionally, a second equilibration was performed for
     an additional 10 ns at constant pressure of 1 atm using the Berendsen barostat 60 . Temper-
     ature control continued through Langevin dynamics, with an increased collision frequency
     of 2 ps−1 . Finally, the MD simulations of 10 µs for the systems initiated from the unfolded
     state and 200 ns for the systems initiated from the experimentally folded state, were run
     with a 4 fs time step.


     GROMACS protocols

     Simulations using the OPLSIDPSFF, 45 a99SBdisp, 15 DES-Amber, 46 DES-Amber-SF1.0, 46
     and C36IDPSFF 44 force fields were performed with GROMACS version 2019.2 50 . To ensure





     consistency with the AMBER-based simulations, similar protocols and conditions were ap-
     plied across all systems. For simulations initiated from the unfolded state extended linear
     conformations were generated using the xleap module in AMBER. In contrast, folded-state
     simulations were based on experimentally determined structures retrieved from the RCSB
     Protein Data Bank (PDB). 61 Each peptide’s topologies and coordinates were prepared sep-
     arately for each force field. Each system was solvated in a truncated octahedral box using
     the water model recommended for the respective force field (see Table 2), maintaining at
     least 8 Å of padding between the solute and the box boundaries. Sodium (Na+ ) and chloride
     (Cl– ) ions were added to neutralize the system and to achieve a final salt concentration of
     0.1M.
          Energy minimization was performed in two stages: an initial steepest descent minimiza-
     tion of up to 50,000 steps, followed by 2,000 steps of conjugate gradient minimization 62 . The
     systems were then gradually heated to 300 K over 10 ns in the canonical (NVT) ensemble, fol-
     lowed by a 20 ns equilibration in the isothermal-isobaric (NPT) ensemble. Covalent bonds
     involving hydrogen atoms were constrained using the LINCS algorithm 63 . Lennard-Jones
     and short-range electrostatic interactions were truncated at 10 Å. Long-range electrostatics
     were treated using the Particle Mesh Ewald (PME) method 64 . Temperature was controlled
     using the velocity-rescale thermostat set at 300 K, and pressure was maintained at 1 atm
     using the Parrinello-Rahman barostat 65,66 .
          Finally, simulations were conducted with a 2 fs integration time step during the heating
     and equilibration phases. After applying hydrogen mass repartitioning 67 , the time step was
     increased to 4 fs during production. For each force field, production simulations of 10 µs were
     performed for the unfolded systems, while 200 ns simulations were conducted for systems
     starting from folded PDB structures.
          Following the simulations, we utilized the cpptraj 68,69 and MDAnalysis 70,71 tools for the
     analysis step, and VMD 72 for the visualization and trajectory analysis.





     Analysis

     Ramachandran Plots

     To evaluate the stereochemical quality and conformational preferences of amino acid residues
     within the peptide sequences, Ramachandran 73 plots were generated. These plots provide
     a visual representation of the backbone dihedral angles (ϕ and ψ), offering insights into the
     propensity of residues to adopt specific secondary structural elements such as α-helices, β-
     sheets, or random coils. The analysis was performed using the MDAnalysis toolkit, employing
     the Ramachandran class to compute ϕ and ψ angles across all residues over time. Stripped
     and aligned trajectories, along with the corresponding topology files, were used as input to
     ensure accurate dihedral angle calculations.


     Clustering

     To identify representative conformations and their populations sampled during the simula-
     tions, structural clustering was performed on each trajectory for every force field and system.
     Hierarchical agglomerative clustering with average linkage was applied using an RMSD-based
     metric with an ϵ cutoff of 3.0 Å, as implemented in cpptraj, part of the AmberTools suite.
     For the 10 µs simulations, every 50th frame was extracted; for the 200 ns simulations, all
     frames were used. Clustering was based on the backbone heavy atoms (C, N, O, Cα, and
     Cβ) of all peptide residues. Cluster centroids were selected as representative structures. No-
     tably, inclusion of all residues led to similar conformations being distributed across multiple
     clusters in some cases, likely due to increased flexibility in loop regions.


     Secondary Structure preferences

     Secondary structure content of the simulated peptides was analyzed using the secstruct
     command in cpptraj. Prior to analysis, trajectories were preprocessed with the autoimage
     command to correct for periodic boundary conditions and maintain peptide chain continuity.





     Secondary structure assignment was carried out using the DSSP algorithm 74 as implemented
     in cpptraj, which classifies structural elements—including α-helices, β-strands, turns, and
     coils—based on backbone hydrogen bonding patterns and geometric features.


     Conformational Diversity and Structural Deviation Analysis

     To quantify the conformational diversity sampled by each force field, Shannon entropy 75
     was calculated based on the fractional populations of clusters obtained from the hierarchical
     clustering analysis (as described in the Clustering section). This metric captures the degree
     of structural heterogeneity within a simulation, where higher entropy values indicate greater
     conformational diversity. Entropy, S, was calculated using the following equation:


                                                                     X
                                                           S=−              Pi log Pi
                                                                       i

          where Pi is the population fraction of the i-th cluster. Calculations were performed with
     the pandas 76 and NumPy 77 Python libraries.
          To assess structural deviations from the native state, root-mean-square deviation (RMSD)
     was computed for the most populated cluster for each force field in each system. The ref-
     erence structure corresponded to the experimentally determined folded state of the peptide.
     RMSD was calculated using the backbone heavy atoms (C, N, O, Cα, and Cβ) of all residues,
     employing cpptraj from the AmberTools suite.


     Results

     Systems of study

     The structural characterization of peptides presents a particularly stringent test for molecular
     force fields. While most peptide sequences are intrinsically disordered in solution, certain
     peptides have been experimentally observed to adopt defined secondary structures under





     specific conditions—such as binding to a partner protein, folding in a membrane-mimetic
     solvent, or being excised from a larger folded domain. These context-dependent peptides
     occupy an intermediate regime between fully folded miniproteins and disordered chains,
     making them ideal benchmarks for assessing force field accuracy and bias. We selected twelve
     experimentally characterized peptides that span four categories: (1) miniproteins with well-
     defined structures in solution, (2) partially structured peptides, (3) peptides that fold upon
     binding to a protein target, and (4) disordered peptides that adopt defined structure only
     in membrane-mimetic or mixed solvents. This set (see Fig. 1) enables us to evaluate force
     field performance across a biologically meaningful spectrum of structural propensities.


     Figure 1: Experimentally folded structures of benchmark peptide systems used
     in this study, shown with their corresponding PDB IDs.


     Miniproteins: These peptides adopt well-defined, compact tertiary folds under aqueous
     conditions and are considered stable, folded entities in solution. Trp-cage (1L2Y) is of-
     ten classified as a miniprotein, as it exhibits over 95% folded population at physiological





     pH, forming a compact helical bundle stabilized by a hydrophobic core nucleated around
     a tryptophan residue. 26 This 20 residue sequence was optimized starting from a 39 residue
     protein. Trp-zip (1LE1) is a 13-residue de novo designed sequence that folds as a β-hairpin.
     Four tryptophan residues create a hydrophobic side in the hairpin, while polar and charged
     residues are present in the other side. Trp-zip is highly stable with high hairpin populations
     (>95%) in water, as confirmed by NMR. 27 Finally, β-defensin-1 (1IJU) is a natural antimi-
     crobial peptide that forms stable monomers and dimers in crystallographic studies. NMR of
     a homologous defensin confirms that monomeric structure is preserved in dilute solution. 28,78
     This 36 residue sequence is the longest in our dataset.


     Partially structured peptides: These peptides exhibit some degree of structure in so-
     lution, often sampling a mixture of folded and unfolded conformations. Two of them are
     fragments derived from larger proteins, whereas the third one is a designed peptide. The C-
     termini from Protein G (β-hairpin, 1GB1) is a 16-residue segment from the immunoglobulin
     binding domain of streptococcal protein G. This hairpin is expected to be formed early in
     protein G folding 79 and experimental studies suggests that this peptide should adopt ∼20%
     hairpin population in solution. 27 C-peptide (helical, 5RSA) is a 13-residue analog from the
     RNase A N-terminal with moderate α-helical content in water. The original C-termini had
     a small helical population in solution and analogs produced with sequence optimization in-
     creased the helical stability with populations ranging from 40–60% depending on temperature
     and variant. 80,81 The EK peptide is a designed helical peptide with favorable electrostatics
     (E,K at i, i + 4 positions). Circular dichroism (CD) studies estimate 40% helical population
     in solution. 82 The AlphaFold 83 prediction is used as a reference.


     Structured upon binding: These peptides are expected to be disordered or dynamic in
     isolation but adopt specific folded conformations upon binding to a protein receptor. The
     MATα2 epitope (1MNM) is a context-dependent peptide from MATα2 (residues 115-128)
     that has been observed binding as both a helix or a hairpin in the same crystal structure. 32





     This unique chameleon-like behavior is a practical test case for our force fields. The NRF2
     peptide (2FLU) forms a small β-hairpin motif when bound to the Kelch domain of KEAP1. 33
     Its unbound conformation is not structurally characterized, making it a useful test for de-
     tecting folding bias. The dynorphin A peptide (2N2F) binds the human κ-opioid receptor
     (KOR) as a structured peptide (residues 1-13 from dynorphin A) with a central helical motif,
     flanked by disordered termini. 34


     Disordered in water, ordered in solvent mixtures: These systems adopt helical struc-
     ture in mixed solvent environments such as Trifluoroethanol (TFE)/water or membrane
     mimetics but remain disordered in pure water. They serve as sensitive probes for helical
     bias. The glucagon-like peptide-1 (GLP-1, 1D0R) is a peptide hormone that is unstructured
     in water but adopts a helix in 35% TFE. NMR experiments at different TFE concentra-
     tions shows that the C-terminal region has a higher helix propensity. 35 The PAMP peptide
     (2FLY) also exhibits α-helicity in both membrane mimetic and TFE environments according
     to NMR studies. 36 Finally, Phylloseptin-1 (2JQ0) is an antimicrobial peptide whose helical
     population increases with TFE concentration—from 53% at 30% to 70% at 60%. 37

     To evaluate force field performance for these systems, we conducted two sets of simulations
     for each system: 1) Short simulations (200 ns) initiated from the experimentally determined
     or AlphaFold-predicted (EK peptide) structure, to assess structural stability and strong
     biases. 2) Long simulations (10 µs) initiated from extended conformations, to assess folding
     tendencies, sampling breadth, and subtle biases.
          Each system’s simulation outputs— Ramachandran analysis, secondary structure propen-
     sities, cluster entropy, RMSD trajectories, representative conformers—are summarized in the
     main text and detailed in Supplementary Figures S1–S60. These results guide our analysis
     of force field accuracy and conformational bias.





     Modeling peptide stability

     Short, 200 ns simulations starting from a folded conformation provide a practical means to
     detect strong force field biases. While unfolding proteins and nucleic acids in explicit sol-
     vent simulations in denaturing solvent mixtures requires long timescales, 84,85 peptides—due
     to their smaller size and limited stabilizing contacts—can unfold spontaneously within this
     timescale, especially when the native structure is marginally stable or environment-dependent. 84,85
     Thus, we use this protocol to detect whether force fields maintain starting structural features
     or quickly deviate toward alternative states.


     Miniproteins

     For the three miniproteins (1L2Y, 1LE1, 1IJU), all of which are expected to remain stably
     folded in solution, most force fields preserve native structure throughout the simulation.
     Trp-cage (1L2Y) retains its compact helical bundle in most force fields, though ff99IDPs,
     OPLSIDPs, and ff14IDPSFF show partial helix loss (SI Fig.1-4). Trpzip (1LE1), a highly
     stable β-hairpin, is preserved in all force fields except ff99IDPs, which fails to maintain the
     strand pairing (SI fig 6-9). For β-defensin (1IJU), which is the longest sequence in our set
     and not a designed miniprotein, most force fields retain the native-like β-sheet, though IDP-
     biased force fields (ff99IDPs, ff14IDPs, ff14IDPSFF, C36IDPSFF) along with Charmm36m
     show partial unfolding (SI fig. 11-14). ff99IDPs maintains some regions of strand pairings
     but loses the overall fold. Some force fields (ff14IDPSFF, Charmm36m, and C36IDPSFF)
     lose the N-terminal helix at least partially, as observed in β-defensin2.


     Partially structured peptides

     These peptides (1GB1, 5RSA, EK) are expected to adopt partially folded conformations. In
     this short timescale we expect that either the structure could be either stabilized totally or
     partially. We do not necessarily expect to see unfolding and refolding in this short timescale.
     In 1GB1, a fragment from protein G, all force fields maintain the native β-hairpin in this short





     timescale, consistent with experimental data pointing to the presence of folded structures
     in the ensemble. Ff99IDPs is the only exception, where the tail of the hairpin is lost for
     most of the trajectory, with short lived helical turns forming in those regions (seef SI Fig
     16-19). For C-peptide (5RSA), approximately half of the force fields lose helicity early in the
     simulation (SI Fig. 21-24). a99SBdisp and ff99IDPs show unfolding and partial refolding
     behavior, while Charmm36m transitions to a β-hairpin-like state in the final 40 ns. For EK,
     a designed helix, several force fields (including OPLSIDPSFF and Charmm36m) lose the
     structure entirely and do not recover it, while ff19SB and ff99IDPs show unfolding followed
     by partial refolding (SI Fig. 26-29). Interestingly, OPLSIDPSFF samples β-hairpin-like
     states near the end of the trajectory, indicating a possible strand-biased artifact.


     Structured upon binding

     These peptides (1MNM, 2FLU, 2N2F) fold only upon receptor binding and are expected
     to show low stability as isolated monomers. For 1MNM, which was started in the helical
     form but can also adopt a hairpin when bound, most force fields unfold the helix, with
     only ff19SB, a99SBdisp, and des-amber-SF1.0 retaining structure (SI Fig. 31-34). Some
     (ff99IDPs, ff14IDPs) transiently refold the helix. NRF2 (2FLU) is maintained as a short c-
     termini hairpin in C36IDPSFF, charmm36m, and ff14IDPSFF. Ff19SB and ff99SB stabilize
     it for the first part of the trajectory – with ff99SB sampling helical states the second half of
     the trajectory (see SI Fig. 36-39). FF99IDPs and ff14IDPSFF have helical tendencies, with
     the remaining force fields adopting almost no secondary structure for the whole trajectory.
     For 2N2F, the central helix is rapidly lost in most simulations, with only a few force fields
     showing transient recovery of the folded motif (ff19SB, a99SBdisp, des-amber-SF1.0, and
     ff14IDPs) (SI Fig. 41-44). Additionally, ff14IDPs sampled short hairpin states.





     Solvent-sensitive helices

     The last group comprises peptides (1D0R, 2FLY, 2JQ0) (SI Fig. 46-60) that form helices
     in membrane-mimetic or TFE-containing solvents but are disordered in water. Several force
     fields lose helical structure rapidly, and some maintain it during most or all of the simulation
     length – at least partially. However, ff99IDPs occasionally samples β-hairpin conformations
     in 2FLY and 2JQ0, suggesting a mild β-bias. These results indicate that force fields with
     strong secondary structure biases may alter the misfolding landscape even when the native
     state is unstructured.


     Summary. Taken together, these 200 ns simulations reveal consistent trends across pep-
     tide classes (Fig. 2 and SI Table 1). Force fields such as ff19SB and a99SBdisp strike
     a balance between stability and flexibility, maintaining expected structure in miniproteins
     and partially structured peptides while allowing partial unfolding in binding-induced and
     solvent-sensitive systems. In contrast, ff99IDPs frequently destabilizes folded helices and oc-
     casionally introduces β-structures in non-β contexts. OPLSIDPSFF and Charmm36m show
     occasional strand-bias, highlighting how tuning for disordered ensembles can influence the
     behavior of context-sensitive peptides.


     Modeling peptide folding

     While short simulations reveal whether force fields preserve native structures, they cannot as-
     sess whether force fields can discover such conformations from unfolded states. We therefore
     turn to long-timescale simulations initiated from extended conformations to examine folding
     behavior, landscape preferences, and potential biases in structural sampling (10 µs). This
     approach helps detect dominant basins in the energy landscape and potential biases—e.g.,
     force fields that prefer β-hairpins across many sequences or that stabilize incorrect folds once
     visited.
          Some peptides that appeared disordered in the 200 ns simulations now display unexpected





     Figure 2: Summary of the overall trends observed for each force field across dif-
     ferent systems during 200 ns simulations initiated from experimentally folded
     structures. Solid-colored helices or hairpins represent stable native secondary structures,
     while striped representations indicate partial retention or stabilization of non-native sec-
     ondary structures. Wavy lines denote disordered ensemble sampling.





     structure preferences, with certain force fields systematically promoting strand pairing or
     helix formation. Conversely, some force fields fail to reach native-like states for peptides
     known to be structured. Notably, OPLSIDPSFF frequently stabilizes β-hairpins early and
     maintains them, regardless of the peptide’s native fold. Force fields such as ff19SB and
     ff99IDPs often revisit native-like helices intermittently, suggesting balanced sampling.


     Miniproteins

     Trp-cage (1L2Y), with two helical regions, is folded only by ff19SB and a99SBdisp, with the
     former stabilizing the structure longer. OPLSIDPSFF and several others prefer β-hairpin-like
     folds, indicating non-native bias (SI Fig. 1-5). For Trpzip (1LE1), a highly stable β-hairpin,
     six force fields fold the correct structure within 2.5µs (SI Fig. 6-10). ff14IDPS initially folds
     a β-hairpin but then samples and stabilizes a helical motif. The longest peptide in this set,
     β-defensin-1 (1IJU), remains unfolded across all force fields (SI Fig. 11-15). OPLSIDPSFF
     again stand out by stabilizing a non-native three-stranded β-sheet, while others sample
     isolated elements of native structure without convergence into the native fold.


     Partially structured peptides

     EK and C-peptide (5RSA) both exhibit moderate helical content experimentally. ff19SB and
     ff99IDPs are the only force fields that consistently sample and stabilize helical conformations
     for both peptides (SI Fig 21-30). OPLSIDPSFF favors hairpin states instead. Interestingly,
     these same force fields (ff19SB and ff99IDPs) partially lost helicity in 200 ns stability sim-
     ulations—suggesting that their ability to unfold and refold reflects a relatively unbiased,
     physically realistic ensemble rather than a strong bias towards helical states.
          For the Protein G C-terminal hairpin (1GB1), only OPLSIDPSFF successfully folds the
     hairpin within the first 100 ns and maintains it throughout the simulation. This is reflected
     in its clustering analysis, which reveals a single dominant state comprising over 80% of the
     trajectory. In contrast, ff14IDPs and ff99IDPs favor helical conformations for much of the





     trajectory, but without consistent convergence—top cluster populations are only ∼10% and
     ∼20%, respectively. The remaining force fields sample structurally diverse ensembles with
     little secondary structure (SI Figs. 16–20). Notably, des-amber, C36mIDPsFF, and ff14IDPs
     populate hairpin-like states frequently enough for them to define the most populated cluster,
     although these clusters still represent less than 15% of the total ensemble.


     Structured upon binding

     These peptides are unstructured in isolation but adopt defined folds when bound to protein
     partners. Their behavior in extended simulations is highly force field-dependent.
          The MATα2 chameleon peptide (1MNM) exhibits divergent behavior: ff99SB, and ff99IDPs
     sample both helix and hairpin conformations sparingly, while other force fields show pref-
     erence for either helix (ff19SB, ff14IDPs, a99SBdisp) or β-structure (OPLSIDPSFF). Other
     force fields adopt secondary structure sparingly (SI Fig. 31-35). For NRF2 (2FLU), OPLSIDPSFF
     stabilizes a non-native β-hairpin, four force fields (ff19SB, ff99IDPs, ff14IDPs, and ff14IDPSFF)
     exhibit helical tendencies, and the remaining form secondary structure sparingly, with C36IDPsFF
     stabilizing a native-like hairpin with low population (SI Fig. 36-40). In 2N2F, ff19SB samples
     native helical motifs at low populations, while most others show low degrees of secondary
     structure (SI Fig. 41-45). Despite this, clustering indicates convergence: top clusters are
     highly populated and structurally similar to each other and to stability simulations, suggest-
     ing a shared ensemble.


     Solvent-sensitive helices

     Peptides such as GLP-1 (1D0R), PAMP (2FLY), and phylloseptin-1 (2JQ0) adopt helices
     only in TFE or membrane mimetic conditions and are expected to remain disordered in
     pure water. Force fields that introduce structured states in this regime indicate potential
     over-structuring.
          Across all three peptides, ff14IDPSFF and OPLSIDPSFF frequently stabilize β-hairpin-





     like motifs. To a lesser extent, C36IDPSFF and ff99IDPs show similar behavior. In contrast,
     ff19SB, des-amber, and des-amber-SF1.0 promote helicity in 1D0R and 2FLY, particularly
     in the C-terminal region—consistent with NMR (SI Fig 46-55). 2JQ0 shows lower helical
     content overall (SI Fig. 56-60).


     Summary. Folding simulations highlight distinct tendencies among force fields (Fig. 3 and
     SI Table 2). OPLSIDPSFF displays a strong and consistent β-bias across systems, often pro-
     ducing dominant clusters regardless of peptide identity. ff19SB and ff99IDPs show context-
     sensitive behavior, folding miniproteins and moderately structured peptides while avoiding
     strong misfolding. IDP-optimized force fields vary widely in behavior: some (ff14IDPSFF)
     promote β-structure, while others (ff99IDPs) show flexibility and helix recovery. These
     simulations emphasize the need to assess force field performance across multiple structural
     regimes and not assume generality based on protein-focused benchmarks.
          Across nearly all peptides, OPLSIDPSFF shows a consistent β-hairpin preference, often
     early in the trajectory (e.g., 1GB1, EK, 1D0R), leading to dominant cluster populations
     (e.g., 1GB1: > 80%). In contrast, ff19SB and ff99IDPs intermittently recover native-like
     helices in marginal systems (e.g., EK, 5RSA), suggesting balanced behavior.


     Entropy as a proxy for conformational sampling across force fields

     Entropy derived from population-weighted cluster occupancies using Shannon’s entropy of-
     fers a compact way to compare the breadth and distribution of conformational space explored
     by different force fields. Because both system size and trajectory length modulate the ab-
     solute value, we treat the 200 ns native-start and 10 µs extended-start ensembles separately
     (Fig. 4 and SI Figs. 61-62). Our objective is not exhaustive sampling, but rather to iden-
     tify systematic force field tendencies—whether they artificially constrain (low entropy) or
     overly-disperse (high entropy) the ensemble.
          We interpret the entropy-RMSD landscape (see Fig. 4) using three qualitative regimes:





     Figure 3: Summary of overall trends observed for each force field across different
     systems during 10 µs simulations initiated from linear peptide sequences. Solid-
     colored helices or hairpins represent the formation of native secondary structures, while
     striped helices or hairpins indicate partial formation of native structures or stabilization of
     non-native secondary structures. Wavy lines denote disordered ensemble sampling.





     Figure 4: Relationship between Shannon entropy and RMSD across different pep-
     tide systems for each force field. For each system, triangle markers (top panels) rep-
     resent data from 200 ns simulations initiated from experimentally folded structures, while
     circle markers (bottom panels) correspond to 10 µs simulations starting from linear peptide
     sequences. Numbers in parentheses indicate the length of each peptide sequence.





     1) Stable native basin (low entropy, low RMSD); 2) Non-native traps (low entropy, high
     RMSD); 3)Broad exploration (high entropy, any RMSD). Entropy values are not normalized
     across systems and should be interpreted within each system’s context.


     Miniproteins (1L2Y, 1LE1, 1IJU):

     In short simulations (200 ns) from native conformations, all three systems retain low RMSD
     (4Å) and low entropy (1.0) under most force fields. FF99IDPs consistently shows higher
     RMSD and entropy, suggesting destabilization. In long simulations from extended chains,
     only ff19SB and a99SBdisp achieve partial folding of Trp-cage (1L2Y) from extended con-
     formations. In contrast, the Trpzip (1LE1) fold is readily sampled by several force fields,
     resulting in low RMSD (1.5Å) and low entropy (2.0) for several force fields. Interestingly,
     OPLSIDPSFF finds a non-native hairpin that is readily stabilized as seen by its lowest
     entropy, indicating that its β-bias might be unbalanced with respect to subtle sequence-
     dependent properties. None of the force fields successfully folds the larger β-defensin-1
     (1IJU) within 10 µs, where even the top clusters have very low population (SI Fig. 13).
     Examination of secondary structure timeseries (SI Fig. 12) reveals long-lived hairpins, par-
     ticularly in OPLSIDPSFF, but as most of the system remains disordered, this leads to
     overall low population clusters. Interestingly, most of the secondary structure sampled is
     incompatible with native-like secondary structure preferences.


     Partially structured peptides (1GB1, 5RSA, EKpep):

     1GB1 remains stable from the native state (low entropy and RMSD). OPLSIDPSFF shows
     especially low entropy, consistent with its known hairpin preference. Approximately half
     of the force fields recover folded-like clusters from extended states. In contrast, 5RSA and
     EKpep show higher entropies even when RMSD remains low, indicating dynamic exchange
     between folded and unfolded states. Only ff99IDPs and ff19SB recover native-like clusters
     for these two systems starting from extended. Interestingly, neither of these two force fields





     was among those that fold 1GB1, suggesting there might be a slight bias towards helical
     states.


     Structured upon binding (1MNM, 2FLU, 2N2F):

     In native-start simulations, 1MNM and 2FLU retain native-like clusters but with moderate-
     to-high entropy, consistent with transient helicity in the absence of a binding partner. Few
     force fields succeed in refolding these systems from extended chains. For the chameleon
     1MNM, OPLSIDPSFF and ff14IDPSFF favor the hairpin conformation, with OPLSIDPSFF
     sampling it at low entropy (contrasting with the high entropy in runs starting from the helical
     conformation). 2N2F remains disordered independently of the starting point, with high
     RMSD and moderate entropy, confirming that no dominant folded state is sampled. This
     contrasts with 1MNM and 2FLU supports a nuanced view of conformational selection versus
     induced fit. The latter two sample bound-like structures as top clusters (albeit with low
     populations and high entropy), implying that a complementary binding site could stabilize
     these conformations. In contrast, 2N2F appears to require interaction with its binding
     partner to access the native-like fold as the top state.


     Solvent-sensitive helices (1D0R, 2FLY, 2JQO):

     Native-start trajectories preserve helical structure to varying degrees (RMSD < 5Å) with
     moderate entropy. Surprisingly, extended-start simulations show lower entropy despite longer
     duration, often converging to compact, non-native states (RMSD 6–10Å, entropy < 2) –
     with some force fields (ff19SB, charmm36m, des-amber, des-amber-SF1.0) stabilizing partial
     helices at one termini, with intrachain hydrophobic interactions collapsing the remainder of
     the sequence. These compact states are not unexpected: starting helices are stabilized in
     membrane-mimicking environments and expose hydrophobic side chains. In aqueous solvent,
     collapse likely reflects an entropic and enthalpic drive to shield hydrophobics from water,
     which in turn leads to low-entropy conformations that are structurally distinct from the





     input helix.


     Discussion

     Peptides sit at the edge of stability: they lack the extensive tertiary contacts that stabilize
     globular proteins. Some peptides adopt stable structures under physiological conditions and
     are often classified as miniproteins. Others become structured only in specific contexts, such
     as in non-aqueous solvents, macromolecular crowding, or upon binding to a partner. This
     intermediate regime, between intrinsically disordered and stably folded, makes peptides a
     sensitive benchmark to detect and characterize force field biases. The peptides chosen for
     this study span this continuum, including well-folded systems, disordered peptides, and
     context-dependent examples.
          As peptide therapeutics continue to gain traction in pharmaceutical research, it is crit-
     ical to assess what improvements are needed in computational pipelines to reliably predict
     peptide binding. A useful decomposition of the binding free energy is:
          ∆Gbind = (∆Gprotein           peptide
                      conf ormation + ∆Gconf ormation ) + ∆Ginteraction ;

          In practice, the protein’s conformational penalty between the apo and holo state (∆Gprotein
                                                                                              conf ormation )

     often cancels in relative binding comparisons (∆∆Gbind ) between two peptides. However, the
     peptide’s conformational free energy depends strongly on the force field’s ability to model
     its unbound and bound ensembles accurately. When two peptides are differentially affected
     by force field errors—such as differing helix propensities or hairpin lengths—the resulting
     ∆Gbind can be significantly biased.
          Our interest in this topic stems from efforts to predict peptide epitopes, their binding
     modes, and complex structures using data-guided simulations. 86–88 In this context, sparse
     experimental data guide the peptide to approach the protein binding site (typically within
     ∼8 Å, avoiding diffusion times that hinder binding simulations), allowing the force field and
     sampling to determine the binding pose and whether the peptide folds upon binding. We ob-





     serve a consistent trend where weaker binders (micromolar and millimolar) require stronger
     guiding data to reproduce expected binding poses, whereas nanomolar binders typically re-
     cover experimental binding modes with significantly less data. In low-affinity binders, where
     the energetic contributions from folding and binding are comparable, even minor force field
     biases may disrupt the delicate balance required for productive complex formation – requir-
     ing higher guiding power. 89 Identifying such trends is important for going from qualitative
     relative binding affinities (e.g., from competitive binding simulations 86,90 ) into more quan-
     titative and robust measurements. The use of implicit solvent in previous methodologies
     inherits deficiencies from this force field selection. Thus, the current work helps users make
     better decisions for choosing force fields for transferring these methodologies into explicit
     solvent environments.
          The force fields selected include both traditional parameterizations, originally optimized
     for folded proteins, and newer variants that aim to balance folded and disordered state sam-
     pling. Force field developers already benchmark their methods using metrics tailored to
     their development goals, often comparing simulated observables to experimental data such
     as NMR chemical shifts or scalar couplings, 91 with agreement quantified via χ2 statistics.
     Additionally, studies that compare across an array of force fields are usually intended to
     identify alternative metrics or benchmarks that support more informed force field selection
     choices. 25,92? ? ,93 Such studies provide valuable insight into force field performance and un-
     derscore the complexity of assessing accuracy in molecular simulations.
          One interesting note is that traditionally it has been easier to assess helicity than it is
     β propensity. Thus, many force field assessments have focused on whether the force field is
     too helical or not – looking at helical vs coil balance. However, it is entirely possible that a
     force field has either too much propensity to form both helices and strands, 20,94 or too little
     of both of them compared to coil conformations.
          Our paired simulation design (starting from native or extended) allows us to distinguish
     between a force field’s ability to preserve native conformations and its ability to discover





     them from unfolded states. Several force fields (e.g., ff14IDPSFF, OPLSIDPSFF) maintain
     hairpins once formed but fail to reach them from extended structures—suggesting shallow
     but narrow basins. Others (e.g., ff19SB, ff99IDPs) allow reversible transitions, consistent
     with broader landscape exploration.
          RMSD alone cannot distinguish between realistic flexibility and biased trapping. By ana-
     lyzing Shannon entropy over cluster populations, we reveal whether force fields sample broad
     ensembles (suggesting realistic disorder) or artificially narrow basins (indicative of structural
     bias). For example, OPLSIDPSFF often shows low entropy across peptides, consistent with
     early stabilization of compact, non-native basins.
          Our results indicate that no single force field performs best across all systems. Nonethe-
     less, clear trends emerge. Some force fields exhibit a strong bias toward specific secondary
     structures, stabilizing helices or strands even when these are not experimentally favored.
     Others tend to sample transient structure without stabilizing it long enough to be bio-
     logically relevant. A third group largely suppresses structure formation, even in peptides
     expected to fold. These behaviors are informative of underlying biases and limitations.
          In our simulations, OPLSIDPSFF consistently promotes β-hairpins even in systems like
     EK or GLP-1 that are not β-structured, highlighting a consistent strand bias. In contrast,
     ff99IDPs frequently destabilizes helices, even in stable miniproteins like Trp-cage, and occa-
     sionally introduces β-structure in disordered or helical systems. ff19SB and a99SBdisp, by
     contrast, maintain expected secondary structure in folded systems and allow context-sensitive
     folding in marginal peptides. Notably, force fields optimized for disordered ensembles do not
     consistently outperform traditional models. For example, ff14IDPSFF introduces non-native
     β-hairpins in several peptides, while OPLSIDPSFF frequently stabilizes strand-pairing even
     in helically biased systems. These results caution against assuming that IDP-tuned force
     fields generalize to all flexible peptide systems.
          Based on stability, folding, and entropy behavior across twelve peptides, ff19SB and
     a99SBdisp consistently show the most balanced performance—preserving native folds, avoid-





     ing over-stabilization, and sampling relevant ensembles. These force fields represent a strong
     starting point for modeling flexible peptides. Ongoing improvements in force field design,
     expanded benchmark sets, and longer simulations, combined with FAIR (Findable, Acces-
     sible, Interoperable, Reproducible) principles, offer new opportunities to detect and correct
     structural biases. Our benchmark shows that peptides, as sensitive probes between order and
     disorder, expose biases not always evident in globular protein models. We advocate for rou-
     tine inclusion of diverse peptide benchmarks—covering miniproteins, disordered sequences,
     and context-dependent folders—in future evaluations.


     Conclusion

     Peptides inhabit a structurally diverse and biologically significant regime that challenges
     current molecular mechanics force fields. Our systematic benchmark, combining short simu-
     lations from native structures and long folding trajectories from extended chains, reveals that
     while many force fields are capable of maintaining folded states in select systems, few are
     unbiased across the full peptide landscape. Force fields such as ff19SB and a99SBdisp strike
     a useful balance—retaining native structure in well-folded systems while allowing transitions
     in marginal or context-sensitive peptides. Others, such as ff99IDPs or OPLSIDPSFF, show
     clear tendencies toward particular secondary structures, often stabilizing non-native folds.
          These findings have important implications for peptide modeling in drug discovery, where
     ∆G predictions depend not only on interaction energies but also on accurate modeling of
     conformational ensembles. When comparing different peptides, force field-dependent errors
     in the conformational component of ∆G can bias binding predictions. Our results under-
     score the need for caution when interpreting peptide simulations and highlight the value of
     ensemble-based and comparative strategies.
          We anticipate that this benchmark will serve both as a practical resource for force field
     users and as a testbed for future force field development targeting intrinsically disordered





     and conformationally adaptive systems. The dataset, simulation protocols, and analysis
     framework are available at https://github.com/PDNALab/peptFF-benchmark to facilitate
     further refinement and standardization in the community.


     Acknowledgement

     The authors thank the support from the National Institutes of Health grant R01GM149646.


     Supporting Information Available

     Additional Figures can be found in the Supplementary information.


     References

       (1) Diella, F.; Haslam, N.; Chica, C.; Budd, A.; Michael, S.; Brown, N. P.; Trave, G.;
             Gibson, T. J.; others Understanding eukaryotic linear motifs and their role in cell
             signaling and regulation. Front Biosci 2008, 13, 603.

       (2) Neduva, V.; Russell, R. B. Peptides mediating interaction networks: new leads at last.
             Current opinion in biotechnology 2006, 17, 465–471.

       (3) Katuwawala, A.; Peng, Z.; Yang, J.; Kurgan, L. Computational prediction of MoRFs,
             short disorder-to-order transitioning protein binding regions. Computational and Struc-
             tural Biotechnology Journal 2019, 17, 454–462.

       (4) Lee, A. C.-L.; Harris, J. L.; Khanna, K. K.; Hong, J.-H. A comprehensive review on
             current advances in peptide drug development and design. International journal of
             molecular sciences 2019, 20, 2383.





       (5) Chang, L.; Mondal, A.; Singh, B.; Martı́nez-Noa, Y.; Perez, A. Revolutionizing peptide-
             based drug discovery: Advances in the post-AlphaFold era. Wiley Interdisciplinary
             Reviews: Computational Molecular Science 2024, 14 .

       (6) Mollica, L.; Bessa, L. M.; Hanoulle, X.; Jensen, M. R.; Blackledge, M.; Schneider, R.
             Binding mechanisms of intrinsically disordered proteins: theory, simulation, and exper-
             iment. Frontiers in molecular biosciences 2016, 3, 52.

       (7) Robustelli, P.; Piana, S.; Shaw, D. E. Mechanism of coupled folding-upon-binding of an
             intrinsically disordered protein. Journal of the American Chemical Society 2020, 142,
             11092–11101.

       (8) Luong, T. D.; Nagpal, S.; Sadqi, M.; Muñoz, V. A modular approach to map out the
             conformational landscapes of unbound intrinsically disordered proteins. Proceedings of
             the National Academy of Sciences 2022, 119, e2113572119.

       (9) Milstein, M. L.; Kimler, V. A.; Ghatak, C.; Ladokhin, A. S.; Goldberg, A. F. An in-
             ducible amphipathic helix within the intrinsically disordered C terminus can participate
             in membrane curvature generation by peripherin-2/rds. Journal of Biological Chemistry
             2017, 292, 7850–7865.

     (10) Mondal, A.; Swapna, G.; Lopez, M. M.; Klang, L.; Hao, J.; Ma, L.; Roth, M. J.;
             Montelione, G. T.; Perez, A. Structure determination of challenging protein–peptide
             complexes combining NMR chemical shift data and molecular dynamics simulations.
             Journal of chemical information and modeling 2023, 63, 2058–2072.

     (11) Kannan, S.; Lane, D. P.; Verma, C. S. Long range recognition and selection in IDPs:
             the interactions of the C-terminus of p53. Scientific reports 2016, 6, 23750.

     (12) Patel, K.; Walport, L. J.; Walshe, J. L.; Solomon, P. D.; Low, J. K.; Tran, D. H.;
             Mouradian, K. S.; Silva, A. P.; Wilkinson-White, L.; Norman, A.; others Cyclic peptides





             can engage a single binding pocket through highly divergent modes. Proceedings of the
             National Academy of Sciences 2020, 117, 26728–26738.

     (13) Csizmok, V.; Follis, A. V.; Kriwacki, R. W.; Forman-Kay, J. D. Dynamic protein in-
             teraction networks and new structural paradigms in signaling. Chemical reviews 2016,
             116, 6424–6462.

     (14) Tesei, G.; Trolle, A. I.; Jonsson, N.; Betz, J.; Knudsen, F. E.; Pesce, F.; Johans-
             son, K. E.; Lindorff-Larsen, K. Conformational ensembles of the human intrinsically
             disordered proteome. Nature 2024, 626, 897–904.

     (15) Robustelli, P.; Piana, S.; Shaw, D. E. Developing a molecular dynamics force field
             for both folded and disordered protein states. Proceedings of the National Academy of
             Sciences 2018, 115, E4758–E4766.

     (16) Jephthah, S.; Pesce, F.; Lindorff-Larsen, K.; Skepo, M. Force field effects in simulations
             of flexible peptides with varying polyproline II propensity. Journal of chemical theory
             and computation 2021, 17, 6634–6646.

     (17) Palazzesi, F.; Prakash, M. K.; Bonomi, M.; Barducci, A. Accuracy of current all-atom
             force-fields in modeling protein disordered states. Journal of chemical theory and com-
             putation 2015, 11, 2–7.

     (18) Matthes, D.; De Groot, B. L. Secondary structure propensities in peptide folding simula-
             tions: a systematic comparison of molecular mechanics interaction schemes. Biophysical
             journal 2009, 97, 599–608.

     (19) Lincoff, J.; Sasmal, S.; Head-Gordon, T. The combined force field-sampling problem in
             simulations of disordered amyloid-β peptides. The Journal of chemical physics 2019,
             150 .





     (20) Best, R. B.; Hummer, G. Optimized Molecular Dynamics Force Fields Applied to the
             HelixCoil Transition of Polypeptides. The journal of physical chemistry. B 2009, 113,
             9004 – 9015.

     (21) Perez, A.; MacCallum, J. L.; Brini, E.; Simmerling, C.; Dill, K. A. Grid-based backbone
             correction to the ff12SB protein force field for implicit-solvent simulations. Journal of
             chemical theory and computation 2015, 11, 4770–4779.

     (22) Rahman, M. U.; Rehman, A. U.; Liu, H.; Chen, H.-F. Comparison and evaluation of
             force fields for intrinsically disordered proteins. Journal of chemical information and
             modeling 2020, 60, 4912–4923.

     (23) Yu, L.; Li, D.-W.; Bruschweiler, R. Systematic differences between current molecular
             dynamics force fields to represent local properties of intrinsically disordered proteins.
             The Journal of Physical Chemistry B 2021, 125, 798–804.

     (24) Lopes, P. E.; Guvench, O.; MacKerell Jr, A. D. Molecular modeling of proteins;
             Springer, 2014; pp 47–71.

     (25) Beauchamp, K. A.; Lin, Y.-S.; Das, R.; Pande, V. S. Are protein force fields getting bet-
             ter? A systematic benchmark on 524 diverse NMR measurements. Journal of chemical
             theory and computation 2012, 8, 1409–1414.

     (26) Neidigh, J. W.; Fesinmeyer, R. M.; Andersen, N. H. Designing a 20-residue protein.
             Nature structural biology 2002, 9, 425 – 430.

     (27) Cochran, A. G.; Skelton, N. J.; Starovasnik, M. A. Tryptophan zippers: stable,
             monomeric beta -hairpins. Proceedings of the National Academy of Sciences of the
             United States of America 2001, 98, 5578 – 5583, trpzip2 ACE SER TRP THR TRP
             GLU ASN GLY LYS TRP THR TRP LYS NME.





     (28) Hoover, D. M.; Chertov, O.; Lubkowski, J. The structure of human β-defensin-1: new
             insights into structural properties of β-defensins. Journal of Biological Chemistry 2001,
             276, 39021–39026.

     (29) Gronenborn, A. M.; Filpula, D. R.; Essig, N. Z.; Achari, A.; Whitlow, M.; Wing-
             field, P. T.; Clore, G. M. A novel, highly stable fold of the immunoglobulin binding
             domain of streptococcal protein G. Science 1991, 253, 657–661.

     (30) Wlodawer, A.; Borkakoti, N.; Moss, D.; Howlin, B. Comparison of two independently
             refined models of ribonuclease-A. Structural Science 1986, 42, 379–387.

     (31) Sommese, R. F.; Sivaramakrishnan, S.; Baldwin, R. L.; Spudich, J. A. Helicity of short
             E-R/K peptides. Protein Science 2010, 19, 2001–2005.

     (32) Tan, S.; Richmond, T. J. Crystal structure of the yeast MATα2/MCM1/DNA ternary
             complex. Nature 1998, 391, 660–666.

     (33) Lo, S.; Li, X.; Henzl, M. T.; Beamer, L. J.; Hannink, M. Structure of the Keap1:Nrf2
             interface provides mechanistic insight into Nrf2 signaling. The EMBO Journal 2006,
             25, 3605–3617.

     (34) O’Connor, C.; White, K. L.; Doncescu, N.; Didenko, T.; Roth, B. L.; Czaplicki, G.;
             Stevens, R. C.; Wüthrich, K.; Milon, A. NMR structure and dynamics of the ago-
             nist dynorphin peptide bound to the human kappa opioid receptor. Proceedings of the
             National Academy of Sciences 2015, 112, 11852–11857.

     (35) Chang, X.; Keller, D.; Bjørn, S.; Led, J. J. Structure and folding of glucagon-like
             peptide-1-(7–36)-amide in aqueous trifluoroethanol studied by NMR spectroscopy. Mag-
             netic Resonance in Chemistry 2001, 39, 477–483.

     (36) Lucyk, S.; Taha, H.; Yamamoto, H.; Miskolzie, M.; Kotovych, G. NMR conformational





             analysis of proadrenomedullin N-terminal 20 peptide, a proangiogenic factor involved
             in tumor growth. Biopolymers: Original Research on Biomolecules 2006, 81, 295–308.

     (37) Resende, J. M.; Moraes, C. M.; Prates, M. V.; Cesar, A.; Almeida, F. C.;
             Mundim, N. C.; Valente, A. P.; Bemquerer, M. P.; Piló-Veloso, D.; Bechinger, B.
             Solution NMR structures of the antimicrobial peptides phylloseptin-1,-2, and-3 and
             biological activity: the role of charges and hydrogen bonding interactions in stabilizing
             helix conformations. Peptides 2008, 29, 1633–1644.

     (38) Tian, C.; Kasavajhala, K.; Belfon, K. A.; Raguette, L.; Huang, H.; Migues, A. N.;
             Bickel, J.; Wang, Y.; Pincay, J.; Wu, Q.; others ff19SB: amino-acid-specific protein
             backbone parameters trained against quantum mechanics energy surfaces in solution.
             Journal of chemical theory and computation 2019, 16, 528–552.

     (39) Hornak, V.; Abel, R.; Okur, A.; Strockbine, B.; Roitberg, A.; Simmerling, C. Com-
             parison of multiple Amber force fields and development of improved protein backbone
             parameters. Proteins: Structure, Function, and Bioinformatics 2006, 65, 712–725.

     (40) Huang, J.; Rauscher, S.; Nawrocki, G.; Ran, T.; Feig, M.; De Groot, B. L.;
             Grubmüller, H.; MacKerell Jr, A. D. CHARMM36m: an improved force field for folded
             and intrinsically disordered proteins. Nature methods 2017, 14, 71–73.

     (41) Wang, W.; Ye, W.; Jiang, C.; Luo, R.; Chen, H.-F. New force field on modeling intrin-
             sically disordered proteins. Chemical biology & drug design 2014, 84, 253–269.

     (42) Song, D.; Wang, W.; Ye, W.; Ji, D.; Luo, R.; Chen, H.-F. ff14IDPs force field improving
             the conformation sampling of intrinsically disordered proteins. 2017.

     (43) Song, D.; Luo, R.; Chen, H.-F. The IDP-specific force field ff14IDPSFF improves the
             conformer sampling of intrinsically disordered proteins. Journal of chemical information
             and modeling 2017, 57, 1166–1178.





     (44) Liu, H.; Song, D.; Zhang, Y.; Yang, S.; Luo, R.; Chen, H.-F. Extensive tests and
             evaluation of the CHARMM36IDPSFF force field for intrinsically disordered proteins
             and folded proteins. Physical Chemistry Chemical Physics 2019, 21, 21918–21931.

     (45) Yang, S.; Liu, H.; Zhang, Y.; Lu, H.; Chen, H. Residue-specific force field improving
             the sample of intrinsically disordered proteins and folded proteins. Journal of Chemical
             Information and Modeling 2019, 59, 4793–4805.

     (46) Piana, S.; Robustelli, P.; Tan, D.; Chen, S.; Shaw, D. E. Development of a force field
             for the simulation of single-chain proteins and protein–protein complexes. Journal of
             chemical theory and computation 2020, 16, 2494–2507.

     (47) Izadi, S.; Anandakrishnan, R.; Onufriev, A. V. Building water models: a different
             approach. The journal of physical chemistry letters 2014, 5, 3863–3871.

     (48) Jorgensen, W. L.; Chandrasekhar, J.; Madura, J. D.; Impey, R. W.; Klein, M. L.
             Comparison of simple potential functions for simulating liquid water. The Journal of
             chemical physics 1983, 79, 926–935.

     (49) Piana, S.; Donchev, A. G.; Robustelli, P.; Shaw, D. E. Water dispersion interactions
             strongly influence simulated structural properties of disordered protein states. The jour-
             nal of physical chemistry B 2015, 119, 5113–5123.

     (50) Lindahl, E.; Abraham, M. J.; Hess, B.; van der Spoel, D. GROMACS 2019.2 Manual.
             2019.

     (51) Case, D.; Belfon, K.; Ben-Shalom, I.; Brozell, S.; Cerutti, D.; Cheatham III, T.;
             Cruzeiro, V.; Darden, T.; Duke, R.; Giambasu, G.; others AMBER 20. 2020. San
             Francisco: University of California.[Google Scholar]

     (52) Case, D. A.; Aktulga, H. M.; Belfon, K.; Ben-Shalom, I. Y.; Berryman, J. T.;





             Brozell, S. R.; Cerutti, D. S.; Cheatham III, T. E.; Cisneros, G. A.; Cruzeiro, V.
             W. D.; others Amber 2023 ; University of California, San Francisco, 2023.

     (53) Maier, J. A.; Martinez, C.; Kasavajhala, K.; Wickstrom, L.; Hauser, K. E.; Simmer-
             ling, C. ff14SB: improving the accuracy of protein side chain and backbone parameters
             from ff99SB. Journal of chemical theory and computation 2015, 11, 3696–3713.

     (54) Jo, S.; Kim, T.; Iyer, V. G.; Im, W. CHARMM-GUI: a web-based graphical user
             interface for CHARMM. Journal of computational chemistry 2008, 29, 1859–1865.

     (55) Brooks, B. R.; Brooks III, C. L.; Mackerell Jr, A. D.; Nilsson, L.; Petrella, R. J.;
             Roux, B.; Won, Y.; Archontis, G.; Bartels, C.; Boresch, S.; others CHARMM: the
             biomolecular simulation program. Journal of computational chemistry 2009, 30, 1545–
             1614.

     (56) Lee, J.; Cheng, X.; Jo, S.; MacKerell, A. D.; Klauda, J. B.; Im, W. CHARMM-GUI in-
             put generator for NAMD, GROMACS, AMBER, OpenMM, and CHARMM/OpenMM
             simulations using the CHARMM36 additive force field. Biophysical journal 2016, 110,
             641a.

     (57) Pastor, R. W.; Brooks, B. R.; Szabo, A. An analysis of the accuracy of Langevin and
             molecular dynamics algorithms. Molecular Physics 1988, 65, 1409–1419.

     (58) Wu, X.; Brooks, B. R. Self-guided Langevin dynamics simulation method. Chemical
             physics letters 2003, 381, 512–518.

     (59) Wu, X.; Brooks, B. R.; Vanden-Eijnden, E. Self-guided L angevin dynamics via gener-
             alized L angevin equation. Journal of computational chemistry 2016, 37, 595–601.

     (60) Berendsen, H. J.; Postma, J. v.; Van Gunsteren, W. F.; DiNola, A.; Haak, J. R. Molecu-
             lar dynamics with coupling to an external bath. The Journal of chemical physics 1984,
             81, 3684–3690.





     (61) Berman, H. M.; Westbrook, J.; Feng, Z.; Gilliland, G.; Bhat, T. N.; Weissig, H.;
             Shindyalov, I. N.; Bourne, P. E. The protein data bank. Nucleic acids research 2000,
             28, 235–242.

     (62) Press, W. H.; Teukolsky, S. A.; Vetterling, W. T.; Flannery, B. P. Numerical recipes
             3rd edition. Cambridge: New York 2007,

     (63) Hess, B. P-LINCS: A parallel linear constraint solver for molecular simulation. Journal
             of chemical theory and computation 2008, 4, 116–122.

     (64) Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. A
             smooth particle mesh Ewald method. The Journal of chemical physics 1995, 103, 8577–
             8593.

     (65) Parrinello, M.; Rahman, A. Crystal structure and pair potentials: A molecular-
             dynamics study. Physical review letters 1980, 45, 1196.

     (66) Parrinello, M.; Rahman, A. Strain fluctuations and elastic constants. The Journal of
             Chemical Physics 1982, 76, 2662–2666.

     (67) Hopkins, C. W.; Le Grand, S.; Walker, R. C.; Roitberg, A. E. Long-time-step molec-
             ular dynamics through hydrogen mass repartitioning. Journal of chemical theory and
             computation 2015, 11, 1864–1874.

     (68) Roe, D. R.; Cheatham III, T. E. PTRAJ and CPPTRAJ: software for processing and
             analysis of molecular dynamics trajectory data. Journal of chemical theory and com-
             putation 2013, 9, 3084–3095.

     (69) Roe, D. R.; Cheatham III, T. E. Parallelization of CPPTRAJ enables large scale anal-
             ysis of molecular dynamics trajectory data. 2018.

     (70) Gowers, R. J.; Linke, M.; Barnoud, J.; Reddy, T. J. E.; Melo, M. N.; Seyler, S. L.;





             Domanski, J.; Dotson, D. L.; Buchoux, S.; Kenney, I. M.; others MDAnalysis: a Python
             package for the rapid analysis of molecular dynamics simulations; 2019.

     (71) Michaud-Agrawal, N.; Denning, E. J.; Woolf, T. B.; Beckstein, O. MDAnalysis: a
             toolkit for the analysis of molecular dynamics simulations. Journal of computational
             chemistry 2011, 32, 2319–2327.

     (72) Humphrey, W.; Dalke, A.; Schulten, K. VMD: visual molecular dynamics. Journal of
             molecular graphics 1996, 14, 33–38.

     (73) Ramachandran, G. N. Stereochemistry of polypeptide chain configurations. J. Mol.
             Biol. 1963, 7, 95–99.

     (74) Kabsch, W.; Sander, C. Dictionary of protein secondary structure: pattern recogni-
             tion of hydrogen-bonded and geometrical features. Biopolymers: Original Research on
             Biomolecules 1983, 22, 2577–2637.

     (75) Shannon, C. E. A mathematical theory of communication. The Bell system technical
             journal 1948, 27, 379–423.

     (76) McKinney, W.; others Data structures for statistical computing in Python. scipy 2010,
             445, 51–56.

     (77) Harris, C. R.; Millman, K. J.; Van Der Walt, S. J.; Gommers, R.; Virtanen, P.; Cour-
             napeau, D.; Wieser, E.; Taylor, J.; Berg, S.; Smith, N. J.; others Array programming
             with NumPy. nature 2020, 585, 357–362.

     (78) Sawai, M. V.; Jia, H. P.; Liu, L.; Aseyev, V.; Wiencek, J. M.; McCray, P. B.; Ganz, T.;
             Kearney, W. R.; Tack, B. F. The NMR Structure of Human -Defensin-2 Reveals a Novel
             -Helical Segment † , ‡. Biochemistry 2001, 40, 3810–3816.

     (79) Chang, L.; Perez, A. Deciphering the Folding Mechanism of Proteins G and L and
             Their Mutants. Journal of the American Chemical Society 2022, 144, 14668–14677.





     (80) Shoemaker, K. R.; Kim, P. S.; Brems, D. N.; Marqusee, S.; York, E. J.; Chaiken, I. M.;
             Stewart, J. M.; Baldwin, R. L. Nature of the charged-group effect on the stability of the
             C-peptide helix. Proceedings of the National Academy of Sciences of the United States
             of America 1985, 82, 2349 – 2353, c-peptide LYS GLU THR ALA ALA ALA LYS
             PHE GLU ARG GLN HIS HSE ribo ALA GLU THR ALA ALA ALA LYS PHE LEU
             ARG ALA HIE ALA c-peptide LYS GLU THR ALA ALA ALA LYS PHE GLU ARG
             GLN HIS HSE ribo ALA GLU THR ALA ALA ALA LYS PHE LEU ARG ALA HIE
             ALA.

     (81) Brüschweiler, R.; Morikis, D.; Wright, P. E. Hydration of the partially folded peptide
             RN-24 studied by multidimensional NMR. Journal of biomolecular NMR 1995, 5, 353
             356, ribonuclease ribonuclease.

     (82) Sommese, R. F.; Sivaramakrishnan, S.; Baldwin, R. L.; Spudich, J. A. Helicity of short
             E-R/K peptides. Protein Science 2010, 19, 2001 – 2005.

     (83) Jumper, J.; Evans, R.; Pritzel, A.; Green, T.; Figurnov, M.; Ronneberger, O.; Tunya-
             suvunakool, K.; Bates, R.; Žı́dek, A.; Potapenko, A.; others Highly accurate protein
             structure prediction with AlphaFold. nature 2021, 596, 583–589.

     (84) Candotti, M.; Pérez, A.; Ferrer-Costa, C.; Rueda, M.; Meyer, T.; Gelpı́, J. L.;
             Orozco, M. Exploring Early Stages of the Chemical Unfolding of Proteins at the Pro-
             teome Scale. PLoS Computational Biology 2013, 9, e1003393.

     (85) Perez, A.; Orozco, M. Real-time atomistic description of DNA unfolding. Angewandte
             Chemie (International ed. in English) 2010, 49, 4805 – 4808.

     (86) Morrone, J. A.; Perez, A.; MacCallum, J.; Dill, K. A. Computed binding of peptides to
             proteins with MELD-accelerated molecular dynamics. Journal of chemical theory and
             computation 2017, 13, 870–876.





     (87) Lang, L.; Perez, A. Binding Ensembles of p53-MDM2 Peptide Inhibitors by Combining
             Bayesian Inference and Atomistic Simulations. Molecules 2021, 26, 198.

     (88) Mondal, A.; Swapna, G.; Lopez, M. M.; Klang, L.; Hao, J.; Ma, L.; Roth, M. J.;
             Montelione, G. T.; Perez, A. Structure determination of challenging protein–peptide
             complexes combining NMR chemical shift data and molecular dynamics simulations.
             Journal of chemical information and modeling 2023, 63, 2058–2072.

     (89) Singh, B.; Mondal, A.; Gaalswyk, K.; MacCallum, J. L.; Perez, A. MELD-Adapt:
             On-the-Fly Belief Updating in Integrative Molecular Dynamics. Journal of Chemical
             Theory and Computation 2024, 20, 9230–9242.

     (90) Parui, S.; Robertson, J. C.; Somani, S.; Tresadern, G.; Liu, C.; Dill, K. A. MELD-
             Bracket Ranks Binding Affinities of Diverse Sets of Ligands. Journal of Chemical In-
             formation and Modeling 2023, 63, 2857–2865.

     (91) Koes, D. R.; Vries, J. K. Evaluating amber force fields using computed NMR chemical
             shifts. Proteins: Structure, Function, and Bioinformatics 2017, 85, 1944–1956.

     (92) Sarthak, K.; Winogradoff, D.; Ge, Y.; Myong, S.; Aksimentiev, A. Benchmarking Molec-
             ular Dynamics Force Fields for All-Atom Simulations of Biological Condensates. Journal
             of Chemical Theory and Computation 2023, 19, 3721–3740.

     (93) Huggins, D. J. Comparing the Performance of Different AMBER Protein Forcefields,
             Partial Charge Assignments, and Water Models for Absolute Binding Free Energy
             Calculations. Journal of Chemical Theory and Computation 2022, 18, 2616–2630.

     (94) Best, R. B.; Mittal, J. Balance between and Structures in Ab Initio Protein Folding.
             The journal of physical chemistry. B 2010, 114, 8790 – 8798.





     TOC Graphic
