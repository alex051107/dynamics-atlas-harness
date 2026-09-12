# Developing a molecular dynamics force field for both folded and disordered protein states

**Authors:** Paul Robustelli, Stefano Piana, David E. Shaw
**Year:** 2018
**Venue:** Proceedings of the National Academy of Sciences
**DOI:** 10.1073/pnas.1800690115
**Source PDF URL:** https://europepmc.org/articles/PMC6003505?pdf=render
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Developing a molecular dynamics force field for both
folded and disordered protein states
Paul Robustellia, Stefano Pianaa,1, and David E. Shawa,b,1
a
    D. E. Shaw Research, New York, NY 10036; and bDepartment of Biochemistry and Molecular Biophysics, Columbia University, New York, NY 10032

Edited by Michael L. Klein, Temple University, Philadelphia, PA, and approved April 16, 2018 (received for review January 19, 2018)

Molecular dynamics (MD) simulation is a valuable tool for charac-                disordered states that more closely agree with experimental
terizing the structural dynamics of folded proteins and should be                measurements (7). Unfortunately, in preliminary tests, this water
similarly applicable to disordered proteins and proteins with both               model sometimes resulted in less accurate simulations of folded
folded and disordered regions. It has been unclear, however,                     proteins (7). Initial studies of the other force-field improvements
whether any physical model (force field) used in MD simulations                  mentioned above with folded proteins are more encouraging (8,
accurately describes both folded and disordered proteins. Here,                  9). In the absence of large-scale systematic tests of force-field
we select a benchmark set of 21 systems, including folded and                    accuracy, however, it has been unclear whether any force field
disordered proteins, simulate these systems with six state-of-the-               currently in use can accurately describe both folded and disordered
art force fields, and compare the results to over 9,000 available                protein states. A force field that is capable of providing accurate
experimental data points. We find that none of the tested force                  descriptions of both ordered and disordered proteins is naturally
fields simultaneously provided accurate descriptions of folded                   highly desirable, as it would enable simulations of, for example,
proteins, of the dimensions of disordered proteins, and of the                   proteins containing both ordered and disordered regions and
secondary structure propensities of disordered proteins. Guided                  proteins that transition between ordered and disordered states.
by simulation results on a subset of our benchmark, however, we                     In this investigation, we systematically and quantitatively as-
modified parameters of one force field, achieving excellent                      sess the accuracy of a number of state-of-the-art force fields from
agreement with experiment for disordered proteins, while main-                   the CHARMM and Amber families through MD simulations of
taining state-of-the-art accuracy for folded proteins. The resulting             a variety of ordered and disordered proteins. We assembled a
force field, a99SB-disp, should thus greatly expand the range of
                                                                                 large benchmark set of 21 experimentally well-characterized
biological systems amenable to MD simulation. A similar approach
                                                                                 proteins and peptides, including folded proteins, fast-folding
could be taken to improve other force fields.
                                                                                 proteins, weakly structured peptides, disordered proteins with
                                                                                 some residual secondary structure, and disordered proteins with
computer simulations    | intrinsically disordered proteins | protein dynamics   almost no detectable secondary structure. This benchmark set
                                                                                 contains over 9,000 previously reported experimental data
M      any biologically important functions are carried out by
       disordered proteins or proteins containing structurally
disordered regions. Unlike folded proteins, disordered proteins
                                                                                 points. The Amber force fields tested were a99SB*-ILDN (11,
                                                                                 12) with the TIP3P water model (13), a99SB-ILDN with the
                                                                                 TIP4P-D water model (7), the a03ws force field containing em-
have native states that lack a well-defined tertiary structure. To               pirically optimized solute–solvent dispersion interactions (8),
structurally characterize such proteins, with the aim of ultimately              and the a99SB force field with modified Lennard–Jones (LJ)
giving mechanistic insight into their function, it is necessary to
determine the heterogeneous ensembles of conformations that
                                                                                      Significance
they adopt. One potential approach is molecular dynamics (MD)
simulation, which, in principle, provides a direct computational
route to determining structurally disordered states in atomic detail.                 Many proteins that perform important biological functions are
The quality of MD simulation results is, however, strongly de-                        completely or partially disordered under physiological condi-
                                                                                      tions. Molecular dynamics simulations could be a powerful tool
pendent on the accuracy of the physical model (force field) used.
                                                                                      for the structural characterization of such proteins, but it has
   Significant progress has recently been made in the ability of
                                                                                      been unclear whether the physical models (force fields) used in
MD force fields to accurately describe folded proteins (1–6).
                                                                                      simulations are sufficiently accurate. Here, we systematically
Despite these remarkable successes, however, initial compari-
                                                                                      compare the accuracy of a number of different force fields in
sons of MD simulations of disordered proteins and peptides with
                                                                                      simulations of both ordered and disordered proteins, finding
experimental measurements from techniques including NMR
                                                                                      that each force field has strengths and limitations. We then
spectroscopy, small angle X-ray scattering (SAXS), and FRET
                                                                                      describe a force field that substantially improves on the state-
showed significant discrepancies (7–9). Our study of multiple
                                                                                      of-the-art accuracy for simulations of disordered proteins
popular force fields and water models (7), for example, showed
                                                                                      without sacrificing accuracy for folded proteins, thus broad-
that all tested combinations produced disordered states that were
                                                                                      ening the range of biological systems amenable to molecular
substantially more compact than estimated from experiments.
                                                                                      dynamics simulations.
   There have been a number of attempts to improve the ability
of force fields to describe disordered states. Head-Gordon and                   Author contributions: P.R., S.P., and D.E.S. designed research; P.R. and S.P. performed
coworkers (9) optimized solvent–water van der Waals (vdW)                        research; and P.R., S.P., and D.E.S. wrote the paper.
interactions to reproduce experimental solvation free energies                   The authors declare no conflict of interest.
for a number of model organic compounds. Best et al. (8)                         This article is a PNAS Direct Submission.
rescaled protein–water interactions in the a03w protein force                    This open access article is distributed under Creative Commons Attribution-NonCommercial-
field (10) by a constant factor to produce more realistic dimen-                 NoDerivatives License 4.0 (CC BY-NC-ND).
sions of unfolded states of proteins. Recently, we found that                    1
                                                                                     To whom correspondence may be addressed. Email: Stefano.Piana-Agostinetti@
dispersion interactions in the water models used for MD simu-                        DEShawResearch.com or David.Shaw@DEShawResearch.com.
lation are severely underestimated; simulations performed with a                 This article contains supporting information online at www.pnas.org/lookup/suppl/doi:10.
water model that was designed to have a more balanced de-                        1073/pnas.1800690115/-/DCSupplemental.
scription of dispersion and electrostatic interactions produced                  Published online May 7, 2018.

E4758–E4766 | PNAS | vol. 115 | no. 21                                                                                www.pnas.org/cgi/doi/10.1073/pnas.1800690115
                                                                                                                                                                           PNAS PLUS

parameters proposed by Head-Gordon and coworkers (9). The                              linker and SAXS scattering curves that report on the overall di-
CHARMM force fields tested were C22* (14) and C36m (6).                                mensions of the solution ensemble. Simulations of calmodulin can
C36m is a recent update to the C36 force field that was shown to                       simultaneously probe the ability of a force field to describe flexi-
greatly improve the structural properties of small disordered pep-                     bility in the linker region, to avoid overly compact structures, and
tides, but that does not solve the problem of overcompactness of                       to maintain the structures of globular folded domains. To probe
disordered proteins. In general, we find that the tested force fields                  the ability of the force fields to accurately describe the equilibrium
give results in good agreement with experiment for many bench-                         between ordered and disordered conformations, we examined the
mark systems but that none of these previously existing force fields                   temperature-dependent native-state stability of the fast-folding
produce accurate dimensions and residual secondary structure                           variant of the villin head piece (referred to here as villin) (16),
propensities for disordered proteins while simultaneously providing                    Trp-cage (17), the GTT variant of the WW domain FiP35 (re-
accurate descriptions of folded proteins.                                              ferred to here as GTT) (18), the helical (AAQAA)3 15-mer pep-
   We complete our investigation by attempting to improve the                          tide (19), and the small β-hairpin–forming peptide CLN025 (20).
parameters of an existing force field. Using the a99SB-ILDN                               We also selected for inclusion in the benchmark a set of
protein force field with the TIP4P-D water model as a starting                         proteins that are disordered under physiological conditions and
point, we optimized torsion parameters and introduced small                            for which extensive sets of NMR and SAXS data are available.
changes in the protein and water vdW interaction terms,                                Disordered proteins can vary widely in terms of local order, re-
resulting in a force field, a99SB-disp, that achieves unprece-                         sidual secondary structure propensities, and compactness, and
dented levels of accuracy in simulations of disordered protein                         our selections reflect this diversity. The benchmark includes the
states while maintaining state-of-the-art accuracy for folded                          disordered proteins ACTR (21), drkN SH3 (22), α-synuclein
proteins. The parameters were obtained by iteratively in-                              (23), the NTAIL domain of the measles virus nucleoprotein (24),
troducing parameter modifications to reduce the observed                               Aβ40 (25), the ParE2-associated antitoxin PaaA2 (26), the pro-
discrepancies between simulations and experimental mea-                                liferating cell nuclear antigen-associated factor p15PAF (27), the
surements on a subset of our benchmark dataset. The final                              cyclin-dependent kinase inhibitor Sic1 (28), and an intrinsically
parameters were tested on the remainder of the benchmark to                            disordered region from the Saccharomyces cerevisiae transcrip-
reduce the risk of overfitting. We expect that a99SB-disp will                         tion factor Ash1 (29) (a region that we will refer to simply as
enable substantially more accurate simulations to be carried                           Ash1). Simulations of disordered proteins were compared with
out for a range of important biological systems. The example                           experimental NMR J couplings, chemical shifts, and RDCs to
of a99SB-disp also shows that the simplified functional forms                          assess the accuracy of local conformational distributions; ex-
currently used in MD force fields are not incompatible with                            perimental paramagnetic relaxation enhancements (PREs) to
the accurate simulation of both ordered and disordered pro-                            assess the accuracy of transient tertiary contacts; and experi-

                                                                                                                                                                              BIOPHYSICS AND
tein states with a single set of parameters; it is likely that the                     mental SAXS scattering data to determine the accuracy of sim-
parameters of other force fields can similarly be improved by                          ulated radii of gyration (Rg). We also included the bZip domain
using the benchmark presented here.                                                    of the GCN4 transcription factor (which we refer to as GCN4)
                                                                                       (30), a partially disordered dimer with an ordered helical coiled
                                                                                                                                                                           COMPUTATIONAL BIOLOGY
Results                                                                                coil dimerization domain. Simulations of GCN4 were compared
Composition of the Benchmark Set. To determine the accuracy of                         with experimental NMR chemical shifts and order parameters to
force fields for both ordered and disordered protein states, we                        assess local conformational distributions and fluctuations. To
assembled a benchmark set of 21 proteins and peptides, in-                             study the ability of force fields to describe an unstructured
cluding folded and disordered systems (Fig. 1). Over 9,000 ex-                         peptide, we examined the disordered polyalanine peptide Ala5
perimental data points are available for this set of proteins.                         (31), for which NMR J couplings are available. A full list of
   This benchmark set includes four folded proteins [ubiquitin,                        experimental measurements used to evaluate the accuracy of
GB3, hen egg white lysozyme (HEWL), and bovine pancreatic                              simulations is contained in SI Appendix, Table S1.
trypsin inhibitor (BPTI)] that have been characterized by ex-
perimental NMR J couplings, residual dipolar couplings (RDCs),                         Assessment of the Ability of Current Force Fields to Reproduce the
and order parameters that describe their conformational fluctua-                       Experimental Data. We examined the ability of a number of force
tions. Calmodulin, a multidomain protein with two folded do-                           fields to accurately reproduce experimental data for the bench-
mains connected by a flexible linker (15), has been characterized                      mark set. The force fields examined were the Amber force fields
by experimental NMR chemical shifts and RDCs that report on                            a99SB*-ILDN (11, 12) with TIP3P (13), a03ws (8), a99SB-ILDN
the structure and dynamics of the folded domains and flexible                          with TIP4P-D (7), and a99SB with TIP4P-Ew (32) and the

                                                                       Villin Trp-cage GTT               PaaA2      NTAIL   Ala5 Αβ40
                                    BPTI     HEWL

                                    GB3                                    CLN025 (AAQAA)3           GCN4 DrkN SH3 ACTR α-synuclein
                            Order                                                                                                    Disorder
                                        Folded      Folded Proteins with      Equilibrium        Disordered Proteins    Disordered
                                        Proteins    Disordered Regions      Folding/Unfolding   with Residual Structure Proteins

Fig. 1. Schematic illustration of systems contained in the benchmark set of proteins simulated in this work to assess and refine the accuracy of protein force
fields for both ordered and disordered protein states.

Robustelli et al.                                                                                                                       PNAS | vol. 115 | no. 21 | E4759
Head-Gordon LJ (9) and dihedral (33) modifications (we refer                                                       Folded Proteins                             Multi-Domain        Partially Disordered
                                                                                                                                                                 Protein                   Dimer
to this force field as a99SB-UCB) as well as the CHARMM force                             3.0                                                                3.0
                                                                                                                              a99SB*-ILDN/TIP3P
fields C22* (14) with TIP3P-CHARMM (34) and C36m (6) with                                                                     C36m
                                                                                                                                                                                     6.0
TIP3P-CHARMM. This set of force fields allowed for the

                                                                      Force Field Score
                                                                                          2.5                                 C22*/TIP3P                     2.5                     5.0
comparison of the accuracy of two “helix-coil balanced” force                                                                 a03ws
                                                                                                                              a99SB-ILDN/TIP4P-D
fields optimized for use with three-point water models (a99SB*-                           2.0                                 a99SB-disp                     2.0                     4.0
ILDN and C22*), the recently optimized C36m force field, and
three force fields that use four-point water models. Comparisons                                                                                                                     3.0
                                                                                          1.5                                                                1.5
of simulations with experimental measurements are represented
                                                                                                                                                                                     2.0
by a normalized force-field score (Methods), where a normalized
force-field score of one indicates that a simulation with a given                         1.0                                                                1.0                     1.0
force field produces the closest agreement with experiment                                      GB3 Ubiquitin HEWL                  BPTI       Average              Calmodulin             GCN4
among all of the force fields tested for all classes of the experi-                                                                   Disordered Proteins
mental observables considered. We discuss the most salient re-                            3.0
sults from simulations with these six force fields in the text; a
detailed comparison between calculated and experimental                                   2.5

                                                                      Force Field Score
properties for each force field for each member of the bench-
mark set of proteins is reported in SI Appendix, Tables S2–S17.
Results for simulations run using a99SB-UCB are reported in                               2.0
SI Appendix.
Folded proteins. To assess the performance of the force fields on
folded proteins, we first simulated four proteins for which ex-                           1.5
tensive NMR data are available; 10-μs simulations of the folded
proteins ubiquitin, GB3, HEWL, and BPTI performed with                                    1.0
a99SB*-ILDN, C36m, C22*, and a99SB-ILDN/TIP4P-D rather
                                                                                                                                                                   p15PAF
                                                                                                                                α-synuclein
                                                                                                                                                                            Sic1   Ash1
                                                                                                 drkN SH3
                                                                                                                      NTail                   PaaA2
                                                                                                                                                                                           Average
accurately reproduced the experimental NMR measurements                                                     ACTR                                      Αβ40
(Fig. 2 and SI Appendix, Fig. S1 and Tables S3–S6 and S18).
Simulations of folded proteins run with the a03ws and a99SB-
UCB force fields gave substantially larger deviations from the
experimental results. Analysis of the trajectories reveals that, in   Fig. 2. Normalized force-field scores for simulations of folded and disor-
                                                                      dered proteins from the benchmark examined in this work. Average scores
many cases, partial or complete unfolding of the proteins was
                                                                      are also shown for calmodulin, which contains two folded globular domains
responsible for these deviations. We also examined the stability      connected by a flexible linker, and GCN4, a partially disordered dimer that
of 11 additional folded proteins from the set by Huang et al. (6)     contains an ordered coiled coil dimer interface. We note that simulations of
in 20-μs simulations in each force field (SI Appendix, Table S20)     GB3, ubiquitin, drkN SH3, ACTR, NTAIL, and α-synuclein were used in the
and the agreement with NMR chemical shift and NOE mea-                training of the parameters of a99SB-disp. Statistical uncertainties in the
surements for 41 additional folded proteins taken from the set by     force-field score were estimated to be ∼0.1 for individual proteins (SI Ap-
Mao et al. (35) in 10-μs simulations in each force field (SI Ap-      pendix, Fig. S14).
pendix, Fig. S15 and Tables S21 and S26). We found that
a99SB*-ILDN/TIP3P yielded both the most stable simulations of
the proteins in the set by Huang et al. (6) and the closest           NTAIL molecular recognition (MoRE) element, a truncated 31-
agreement with experimental chemical shifts and NOEs in the           residue NTAIL construct that is too small to experience a re-
dataset by Mao et al. (35). Simulations run with C36m and C22*        strictive hydrophobic collapse, showed helical propensities in
were somewhat less stable and had a higher average fraction of        excellent agreement with experimental measurements, whereas
NOE violations. Simulations run with a99SB-ILDN/TIP4P-D               in the simulation of the entire NTAIL domain, the MoRE ele-
and a03ws destabilized a larger fraction of proteins and pro-         ment had restricted conformational flexibility because of the
duced the largest average fraction of NOE violations. We found        overly compact structures sampled and did not sample any he-
that the trends in stability and agreement with NMR measure-          lical conformations (SI Appendix, Fig. S2). Overcollapse gener-
ments of these additional 52 proteins were generally consistent       ally resulted in persistent secondary structure forming in simulations
with conclusions drawn from the comparison of simulations of          where none is experimentally observed and overall poor agreement
HEWL, BPTI, GB3, and ubiquitin with more extensive sets of            with experimental secondary structure propensities. One exception
experimental NMR data, with the exception that a99SB-ILDN/            was the simulation of PaaA2, which was initiated from a confor-
TIP4P-D partially unfolded some of these 52 additional proteins.      mation containing two helices in the correct locations. The helices
Disordered and partially disordered proteins. We next examined the    remained intact in the initial collapsed structure and were stable
accuracy of the force fields for simulating disordered proteins. In   throughout the simulation.
simulations of the disordered proteins drkN SH3, ACTR, NTAIL,            Disordered protein simulations run with C22* and C36m
α-synuclein, Aβ40, PaaA2, p15PAF, Sic1, and Ash1 run with             showed less restricted sampling and featured larger Rg fluctua-
a99SB*-ILDN, we observed a systematic underestimation of the          tions, larger average Rg values, and more frequent rearrange-
average Rg values compared with experimental values, with             ments of the chain topology than simulations run with a99SB*-
proteins adopting compact molten globule-like structures. In the      ILDN, but simulations in both CHARMM force fields still
30-μs timescale examined here, sampling in simulations run with       substantially underestimated the Rg of larger (>60 residues)
a99SB*-ILDN tended to be restricted to conformations with very        disordered proteins, producing ensembles that are not consistent
similar topologies and contacts to the first structures sampled       with experimental data (SI Appendix, Fig. S3). Consistent with
after an initial hydrophobic collapse. As a result, the secondary     the less restricted sampling, C22* and C36m showed better
structure propensities observed in these simulations were largely     agreement with experimental secondary structure propensities
dictated by the conformation of the initial collapsed structure       and NMR chemical shifts than a99SB*-ILDN for the majority of
and were less dependent on the intrinsic secondary structure          the proteins examined here (Figs. 2 and 3 and SI Appendix,
propensity of the local sequence. This interpretation is supported    Tables S7–S16) but did not capture residual helical propensities
by the observation that an a99SB*-ILDN simulation of the              in drkN SH3, NTAIL, and GCN4 (SI Appendix, Figs. S5, S11, and

E4760 | www.pnas.org/cgi/doi/10.1073/pnas.1800690115                                                                                                                                  Robustelli et al.
                                                                                                                                                       PNAS PLUS

S12); both force fields also contained some elevated β pro-                        Simulations run with a99SB-ILDN/TIP4P-D showed no heli-
pensities in drkN SH3 and α-synuclein that were not in agree-                   cal propensity for any regions of the proteins in the benchmark
ment with experimental chemical shifts and RDCs (SI Appendix,                   set, and the helical coiled coil interface of the dimeric protein
Figs. S5 and S7 and Tables S7 and S10). [We note that, in the                   GCN4 was unstable and dissociated into unstructured mono-
C36m simulation of PaaA2, the stable helices seem to be the                     mers. These results suggest that the TIP4P-D water model in
result of stabilization of initial helical conformations from an                combination with the a99SB-ILDN force field strongly destabi-
unphysical hydrophobic collapse (SI Appendix, Fig. S3).] Nota-                  lizes helical conformations. In contrast, the simulated ensembles
bly, of all of the force fields examined in this study, C36m pro-               of Aβ40 and α-synuclein, which contain little or no secondary
duced the best agreement with the NMR measurements of Aβ40,                     structure, showed good agreement with experimental NMR
a relatively compact disordered protein that is too short to ex-                measurements (SI Appendix, Tables S10 and S12).
perience a restrictive hydrophobic collapse in simulation. C36m                    Simulations run with a99SB-UCB also substantially under-
resulted in slightly more expanded disordered-state ensembles                   estimated residual helicity in all of the proteins tested, although
compared with C22* (SI Appendix, Fig. S3 and Tables S7–S16),                    regions of drkN SH3 and NTAIL with stable experimental helices
which uses the same water model, possibly as a result of the                    showed small amounts of helical propensity in simulation (SI
changes introduced to the vdW terms of alkanes in C36m. This                    Appendix, Figs. S5–S12). The GCN4 dimer also dissociated into
result suggests that it may be interesting in future studies to                 unstructured monomers when simulated with a99SB-UCB.
further explore changes to alkane vdW parameters and water                      These results suggest the a99SB-UCB vdW overrides also
model parameters and their effect on disordered protein com-                    strongly destabilize helical conformations. Simulations of
pactness and the hydrophobic effect.                                            Aβ40 and α-synuclein using a99SB-UCB produced excellent
  Simulations of disordered proteins run with a99SB-ILDN/                       agreement with experimental NMR measurements, surpassing
TIP4P-D, a99SB-UCB, and a03ws had Rg values much closer to                      the agreement of simulations run with a99SB-ILDN/TIP4P-D.
experimental measurements. The percentage deviations of the                        Simulations run with a03ws had substantially more residual
average Rg from the experimental estimate for the disordered                    helicity than a99SB-ILDN/TIP4P-D and a99SB-UCB. In the
proteins in the benchmark set were 10, 13, and 9% for a99SB-                    a03ws simulations, several experimentally observed helices were
ILDN/TIP4P-D, a99SB-UCB, and a03ws, respectively, compared                      populated, although several other regions showed helical pro-
with 22, 26, and 36% for C36m, C22*, and a99SB*-ILDN,                           pensity where it was not observed experimentally or lacked he-
respectively.                                                                   lical propensity where stable helices were detected in experiment
                                                                                (Fig. 3 and SI Appendix, Figs. S5–S12). We note that, even in the
                                                                                more expanded ensembles of a03ws, we still observed some
                                                                                contact-based secondary structure stabilization, although it ten-
                       A                            B
                                                                                                                                                          BIOPHYSICS AND
                           drkN SH3                      ACTR                   ded to be with closely neighboring regions, as long-range con-
                               a99SB*-ILDN/TIP3P
                                                                                tacts were much more transient in these ensembles. These results

Fraction Helical
                               C22*/TIP3P                                       suggest that, although the relative stabilities of helix, sheet, and
                               C36m
                               a03ws
                                                                                coil in a03ws are in more reasonable agreement with experiment

                                                                                                                                                       COMPUTATIONAL BIOLOGY
                               a99SB-ILDN/TIP4P-D                               than in a99SB-ILDN/TIP4P-D and a99SB-UCB, the relative
                               a99SB-disp
                               Experiment                                       stabilities of the secondary structure elements for different
                                                                                amino acids may require further tuning (36).
                                                                                Ala5. For testing force-field performance on small peptides, we
                                                                                performed 500-ns simulations of Ala5 with each force field and
                                                                                computed scalar couplings. In SI Appendix, Table S2, we report
                       C     NTAIL                  D    PaaA2                  χ2 values (SI Appendix, Eq. S1) for each force field, taking into
                                                                                account estimates of the errors produced by uncertainty in the

    Fraction Helical
                                                                                Karplus equation coefficients (8). All force fields investigated
                                                                                here were parameterized against this NMR dataset or similar
                                                                                data and, thus, reproduced the experimental scalar couplings
                                                                                reasonably well. Simulations run with C36m, a03ws, a99SB-
                                                                                UCB, and a99SB-ILDN/TIP4P-D had χ2 values < 1, which
                                                                                suggest agreement with experiment within the error of the
                                                                                Karplus equation predictions.
                       E    GCN4                    F   -synuclein             Fast-folding proteins and peptides. We performed simulated tem-
                                                                                pering runs of the two short peptides (AAQAA)3 and CLN025

Fraction Helical
                                                                                (Fig. 4), which have been widely used as force-field benchmarks
                                                                                due to their ability to form helical or β structure. Consistent with
                                                                                previous studies (2, 8), all force fields considered here consid-
                                                                                erably underestimated the cooperativity of both hairpin and helix
                                                                                formation. C22* best captured the helical propensity of
                                                                                (AAQAA)3 at 300 K; a99SB*-ILDN, C36m, and a03ws per-
                                                                                formed similarly on (AAQAA)3, showing helical propensities of
                            Residue                       Residue               5–12% with relatively little temperature dependence. We ob-
                                                                                served no helicity in (AAQAA)3 simulations run with a99SB-
Fig. 3. Helical propensities observed in simulations of the disordered pro-     ILDN/TIP4P-D and a99SB-UCB. a99SB*-ILDN and C22*
teins drkN SH3 (A), ACTR (B), NTAIL (C), PaaA2 (D), GCN4 (E), and α-synuclein   showed the closest agreement with the melting curve of CLN025.
(F). Black lines are experimental estimates from restrained ensemble models
                                                                                All other force fields underestimated the stability of the native
calculated from NMR data [drkN SH3 (65), NTAIL (66), PaaA2 (26)] or predicted
from experimental NMR chemical shifts using the program δ2d (67) (ACTR,
                                                                                CLN025 hairpin at 300 K to different extents.
α-synuclein, GCN4). We note that simulations of drkN SH3, ACTR, NTAIL, and         In simulated tempering simulations of the fast-folding proteins
α-synuclein were used in the training of the parameters of a99SB-disp. For      Trp-cage, GTT, and villin, we found that simulations run using
clarity of presentation, error bars have been omitted but are displayed in SI   a99SB*-ILDN showed the closest agreement with the experimental
Appendix, Figs. S5–S7 and S10–S12.                                              melting curves, while overestimating the melting temperatures by

Robustelli et al.                                                                                                   PNAS | vol. 115 | no. 21 | E4761
   A                                              B                            the protein that were stable on the 30-μs timescale observed
                    (AAQAA)3                               CLN025              here. These interactions fortuitously stabilized a static domain

                                       Fraction Folded
                                                                               orientation with an Rg in reasonable agreement with experiment.

Fraction Helix
                                                                               In the simulation run with C22*, the two domains collapsed to-
                                                                               gether and then progressively unfolded throughout the remainder
                                                                               of the simulation. In the a03ws simulation, the N-terminal do-
                                                                               main became destabilized and largely unfolded after 2 μs, while
                                                                               the C-terminal domain remained structured. In the a99SB-ILDN
                                                                               simulations with TIP4P-D, the linker was highly flexible and
                   Temperature (K)                        Temperature (K)      dynamic, and the two domains sampled a large number of ori-
                                                                               entations with an average Rg in excellent agreement with ex-
   C                  Villin                      D        Trp-cage            periment, but the helical interfaces within the globular domains
                                                                               became somewhat destabilized. Calmodulin simulations run with

Fraction Folded                      Fraction Folded
                                                                               a99SB-UCB were the least stable, with the N-terminal domain
                                                                               unfolding after 0.5 μs and the C-terminal domain unfolding after
                                                                               5 μs, resulting in the poorest agreement with the experimental
                                                                               measurements. Calmodulin simulations in C36m showed flexi-
                                                                               bility in the linker domain, sampled several orientations of the
                                                                               two domains, and were in excellent agreement with experimental
                                                                               measurements.
                   Temperature (K)                       Temperature (K)
                                                                               Summary of force-field benchmark testing. In our benchmark testing,
   E               GTT Fip35                                                   several of the force fields performed well in simulations of folded
                                                          a99SB*-ILDN/TIP3P
                                                                               proteins, but none of the force fields produced accurate di-

 Fraction Folded
                                                          C36m                 mensions and residual secondary structure propensities across
                                                          C22*/TIP3P           the set of disordered proteins while attaining state-of-the-art
                                                          a03ws                performance for folded proteins. a99SB*-ILDN, for example,
                                                          a99SB-ILDN/TIP4P-D   performed well for simulations of folded proteins, small disor-
                                                          a99SB-disp           dered peptides, and fast-folding proteins but produced un-
                                                                               realistic dimensions and poor agreement with residual secondary
                                                          Experiment
                   Temperature (K)                                             structure propensities for disordered proteins. Simulations run
                                                                               with C22* and C36m performed well for folded proteins and
Fig. 4. Stability of the weakly structured peptides (AAQAA)3 (A) and           showed decent agreement with experimental measurements for
CLN025 (B) and the fast-folding proteins villin (C), Trp-cage (D), and GTT     small disordered proteins (<60 residues). Small peptides and
Fip35 (E) from simulated tempering simulations. Experimental melting
                                                                               fast-folding proteins, however, were understabilized in C36m.
curves are shown in black. We note that simulations of (AAQAA)3 were used
in the training of the parameters of a99SB-disp. No folded structures were     Simulations run with C22* and C36m also produced overly col-
observed in simulations of (AAQAA)3, villin, Trp-cage, or GTT Fip35 run with   lapsed ensembles of longer disordered proteins and showed
a99SB-ILDN/TIP4P-D, and there were no folded structures observed in sim-       discrepancies in residual secondary structure propensities of
ulations of villin run with a03ws.                                             some disordered proteins.
                                                                                  Simulations run with force fields optimized to prevent the
                                                                               overcollapse of disordered states produced more realistic di-
10–50 K (Fig. 4). In simulations run with C36m, the stabilities of             mensions for disordered proteins but often at the expense of the
villin and Trp-cage were underestimated, and no folded struc-                  accuracy of descriptions of residual secondary structure pro-
tures of GTT were observed. In simulations run with a03ws, we                  pensity and/or the stability of folded proteins. Simulations run
observed reasonable agreement with the experimental melting                    with a03ws, for example, accurately described the residual sec-
curve of Trp-cage and a moderate underestimation of the sta-                   ondary populations of small peptides and the stability of some of
bility and melting temperature of GTT. No stable folded struc-                 the fast-folding proteins, but they often resulted in lower stability
tures were observed in the a03ws simulation of villin, and a                   and degraded performance for folded proteins and inaccurate
simulation of the native state of villin unfolded after 0.4 μs in a            residual secondary structure content in disordered proteins.
300-K simulation. In simulated tempering simulations run with                     Simulations of disordered proteins without residual secondary
a99SB-ILDN/TIP4P-D and a99SB-UCB, we did not observe any                       structure performed with a99SB-UCB were in good agreement
folded species for any of the fast-folding proteins examined here.             with experimental measurements, but simulations of folded
Simulations of the native folded structures of Trp-cage and villin             proteins were unstable, and the stability of residual secondary
run at 300 K confirmed that these structures are not stable on the             structure propensities was substantially underestimated in dis-
microsecond timescale in these force fields. Simulations of the                ordered proteins and small peptides. Simulations run with
native state of GTT were stable at 300 K for 10 μs in C36m and                 a99SB-ILDN/TIP4P-D performed well for folded proteins and
a99SB-UCB, and we previously observed reversible folding of                    also provided accurate descriptions of disordered protein regions
GTT in a99SB-ILDN/TIP4P-D at 395 K (7), suggesting that the                    with no residual secondary structure. The stability of secondary
absence of folded states in the 300-μs simulated tempering runs                structure elements in small peptides and disordered proteins was
is likely the result of unconverged sampling.                                  severely underestimated, however, and the fast-folding proteins
Calmodulin. Experimental measurements for Ca2+-bound cal-                      and small peptides were unstable in this force field.
modulin indicate that it consists of two stable globular domains
connected by a flexible linker (15, 37–39). Ca2+-bound calmod-                 Optimization of a99SB-disp. We next asked if the difficulty in
ulin simulations were initiated from the “dumbbell”-shaped                     consistently obtaining accurate results for both ordered and
crystal structure (40), in which the dynamic linker is in an entirely          disordered proteins reflects an intrinsic limitation in the force-
helical conformation.                                                          field functional forms or whether substantial improvements are
   In simulations run with a99SB*-ILDN in TIP3P, the linker                    possible through parameter optimization alone. As a starting
quickly frayed and formed interactions with the C-terminal tail of             point, we chose the a99SB-ILDN/TIP4P-D force field and

E4762 | www.pnas.org/cgi/doi/10.1073/pnas.1800690115                                                                                  Robustelli et al.
                                                                                                                                              PNAS PLUS

attempted to modify its parameters to improve its performance             Through iterative adjustments of the backbone torsion po-
for both ordered and disordered proteins.                              tential and of the strength of the LJ modification for carbonyl
   Inspired by previous successful efforts to reparameterize           oxygen and amide hydrogen pairs, we were able to produce a
force-field torsion angles to obtain a more accurate balance           force field, which we term a99SB-disp, that performed reason-
between helix and coil states (10, 11, 14), we performed a similar     ably well across our training set of proteins. In addition to these
torsion optimization targeting (AAQAA)3 fraction helicity and          modifications, a99SB-disp includes a series of side-chain torsion
polyalanine scalar couplings as described previously (14). At          modifications targeting Protein Data Bank (PDB) rotamer dis-
improved levels of helicity, we observed previously described          tributions and quantum mechanical (QM) energy scans; a repar-
(36) discrepancies in the helical propensities of charged residues,    ameterization of the side-chain charges of aspartate, glutamate,
and we thus incorporated the corrections of the a99SB*-ILDN-Q          and arginine residues to match the guanidinium acetate associa-
force field (36). We found that, through torsion optimizations, it     tion constant (14); and a reparameterization of glycine backbone
was possible to produce good agreement with the temperature-           torsion angles targeting a PDB coil library distribution (41, 42).
dependent helicity of (AAQAA)3 and polyalanine scalar cou-             The final parameters and further information regarding the pa-
plings (χ2 = 0.94). Simulations of disordered proteins performed       rameterization of a99SB-disp are contained in SI Appendix (SI
with this torsion-optimized force field, however, produced en-         Appendix, Tables S22–S25).
sembles that were too helical compared with experimental                  In the training set, a99SB-disp performed comparably with the
measurements (SI Appendix, Fig. S4) and, in the case of ACTR,          best-performing force fields for the folded proteins GB3 and
induced a hydrophobic collapse. There seemed to be some                ubiquitin (Fig. 2 and SI Appendix, Tables S3, S4, and S15), and
cooperativity between helix formation and collapse in disordered       (AAQAA)3 helicity (Fig. 4) was comparable with a99SB*-ILDN,
proteins, as we observed that torsion parameters that accurately       a03ws, and C36m. Simulations of NTAIL, drkN SH3, ACTR, and
described helical propensities in small peptides, such as (AAQAA)3,    α-synuclein were in good agreement with experiment (Figs. 2 and
and small disordered peptides, such as NTAIL MoRE, did not             3 and SI Appendix, Tables S7–S10 and S15), containing a rea-
produce accurate simulations of partially helical disordered           sonable amount of residual helicity in the correct regions of the
proteins that were large enough to experience hydrophobic col-         protein sequences (Fig. 3). A similar level of accuracy was
lapse. This force field also substantially degraded the accuracy       obtained for the simulations of the test set of proteins not used in
of simulations of GB3 and ubiquitin by destabilizing the packing       the parameter optimization: HEWL, BPTI, Aβ40, PaaA2, p15PAF,
of β sheets.                                                           Sic1, Ash1, GCN4, and calmodulin (Figs. 2 and 3 and SI Ap-
   These results suggest that it may be difficult to accurately        pendix, Tables S5, S6, and S11–S17), suggesting that the pa-
describe helical propensities, the dimensions of disordered pro-       rameters obtained are reasonably transferable and that the level
teins, and the stability of native states in a99SB*-ILDN-Q/            of accuracy obtained was not the result of overfitting on the

                                                                                                                                                 BIOPHYSICS AND
TIP4PD using torsion optimization alone. To overcome this              training set of proteins. Simulations run with a99SB-disp also
difficulty, we thus also tested modifications in the strength of the   produced the best agreement with experiment among all force
C6 dispersion term in our water model. In an attempt to alleviate      fields tested on an additional 52 folded proteins from the test
the overcollapse of helical disordered proteins, we optimized a        sets by Huang et al. (6) and Mao et al. (35) (SI Appendix, Fig.

                                                                                                                                              COMPUTATIONAL BIOLOGY
water model with a slightly stronger C6 dispersion term than that      S15 and Tables S20, S21, and S26), none of which were used in
of TIP4P-D (960 kcal mol−1 Å−6 in our water model as opposed to        parameterization, providing further evidence for the trans-
900 kcal mol−1 Å−6 in TIP4P-D) as described previously (7). We         ferability of the parameters.
compared the liquid water properties of this water model, which           Importantly, in our benchmark set, which includes nine dis-
we refer to as a99SB-disp water, with those of TIP4P-D in SI           ordered proteins with lengths ranging from 40 to 140 residues
Appendix, Table S22; we found most properties to be very similar,      and experimental Rg values ranging from 12 to 32 Å, simulations
although for some, such as the diffusion coefficient, slightly worse   of disordered proteins run with a99SB-disp had the closest
agreement with experiment was observed with a99SB-disp water.          agreement with experimental Rg measurements of all force fields
We also compared the solvation free energies of protein side-          tested, with an average deviation of only 6% from experimental
chain analogs in TIP3P, TIP4P-D, and a99SB-disp water (SI Ap-          values. In particular, for all disordered proteins with more than
pendix, Fig. S13) and found them to be very similar. We found that     60 residues, simulations run with a99SB-disp produced ensem-
a99SB-disp water successfully reduced the occurrence of hydro-         bles that were substantially more expanded, in much closer
phobic collapse of disordered helical states but also destabilized     agreement with experiment, than those in simulations run with
folded proteins and helical conformations in (AAQAA)3, drkN            the next best force field, C36m (27% deviation from experi-
SH3, ACTR, and NTAIL.                                                  mental Rg values) (SI Appendix, Fig. S3). This difference is most
   Inspired by previous work (9), we then attempted to increase        pronounced in simulations of larger proteins with more hydro-
the stability of helical states and folded proteins by introducing     phobic sequences (α-synuclein, NTAIL, and Sic1). In simulations
modifications to the O-H LJ pair between backbone carbonyl             of shorter, more compact disordered proteins, such as Aβ40 and
oxygens and backbone amide hydrogens, which strengthened               drkN SH3, and in simulations of the highly charged disordered
protein backbone hydrogen bonds. To find reasonable combi-             protein Ash1 (net charge of −15 at pH 7), both force fields
nations of the carbonyl-oxygen and backbone amide hydrogen             produced Rg values in good agreement with experiment. On
O-H LJ pair and backbone torsion adjustments while reducing            average, simulations of disordered proteins run with a99SB-disp
the risk of overfitting, we optimized these parameters against a       were also in substantially better agreement with experimental
“training” subset of the benchmark set introduced above: ubiq-         NMR measurements than were simulations run with C36m, with
uitin, GB3, (AAQAA)3, Ala5, NTAIL MoRE, NTAIL, drkN SH3,               similar levels of improvement observed in simulations of disor-
ACTR, and α-synuclein. We also ran constant temperature                dered proteins in both the training and test sets.
folding simulations of villin and GTT near their melting tem-             The a99SB-disp melting curves for villin, Trp-cage, and GTT,
peratures to ensure that they could reversibly fold and unfold. In     proteins that were not part of the training set, were also in much
our search of parameter space, we found that we were unable to         better agreement with experiment than the a99SB-ILDN/TIP4P-
simultaneously reproduce the helicity of both (AAQAA)3 and             D melting curves, which showed no folded populations at any
helical disordered proteins with high accuracy and ultimately          temperature for these proteins. There was no noticeable im-
accepted worse agreement with (AAQAA)3 helicity in favor of            provement in the folded population of CLN025 compared with
more accurate descriptions of NTAIL MoRE, NTAIL, drkN SH3,             simulations run with a99SB-ILDN/TIP4P-D (Fig. 4). We see
ACTR, and α-synuclein.                                                 some evidence of cold denaturation in the a99SB-disp melting

Robustelli et al.                                                                                          PNAS | vol. 115 | no. 21 | E4763
curve of villin, which is likely attributable to a subtle shift in the          modified TIP4P/2005 interactions) (8), a99SB and TIP4P-Ew (32) with the
folding enthalpy and heat capacity induced by the water model                   Head-Gordon vdW (9) and dihedral (33) modifications (termed a99SB-
(SI Appendix, Fig. S16).                                                        UCB), a99SB-ILDN (12) with TIP4P-D (7), and a99SB-disp. (The parameters
                                                                                for the a99SB-disp force field are listed in SI Appendix.) Systems were
Discussion                                                                      initially equilibrated at 300 K and 1 bar for 1 ns using the Desmond soft-
                                                                                ware (44). Production runs at 300 K were performed in the NPT ensemble
We have assessed six protein force fields commonly used in MD                   (45–47) with Anton specialized hardware (48) using a 2.5-fs time step and
simulation and found that, although the force fields tested pro-                a 1:2 RESPA scheme (49). Bonds involving hydrogen atoms were restrained
duced results in good agreement with experiment in many cases,                  to their equilibrium lengths using the M-SHAKE algorithm (50). Non-
simulations of the disordered proteins in our benchmark                         bonded interactions were truncated at 12 Å, and the Gaussian split Ewald
revealed limitations in each of the force fields. We have                       method (51) with a 32 × 32 × 32 mesh was used for the electrostatic in-
proposed a force field, a99SB-disp, with improved parame-                       teractions. All simulations were run at 300 K, with the exception of
ters that were trained on and tested against separate subsets                   (AAQAA)3, CLN025, and the fast-folding proteins Trp-cage, villin, and GTT,
of the benchmark; this force field advances the state of the art                which used simulated tempering (52) to improve sampling. In simulated
for accuracy for simulations of disordered proteins, while                      tempering simulations of (AAQAA)3 and CLN025, 20 rungs were spaced
achieving accuracy comparable with the best force fields for                    geometrically spanning 278–390 K. In simulated tempering simulations of
folded proteins.                                                                Trp-cage, villin, and GTT, 60 rungs were spaced geometrically spanning
                                                                                278–400 K.
   The transferability of a99SB-disp across the benchmark ex-
amined here suggests that it should be suitable for studying a
                                                                                Calculation of Experimental Observables. Backbone scalar coupling constants
number of systems that are not well-described by existing force                 were calculated using published Karplus relationships (53) for 3JHNHα, 3JHNC′,
fields. The ability of a99SB-disp to describe both ordered and                  3
                                                                                  JHNCβ (54), 3JHαC′ (55), and 3JC′C′ (56). Side-chain scalar coupling constants
disordered states should enable accurate simulations of proteins                were calculated using published Karplus relationships for 3JHαHβ, 3JC’Hβ,
with both ordered and disordered domains as well as simulations                 3
                                                                                  JC’Cγ, and 3JNCγ (57), with the exception of 3JC’Cγ and 3JNCγ values for Ile,
of transitions between disordered and ordered states, such as                   Thr, and Val, which were computed using Karplus parameters from the
those observed in the coupled folding-upon-binding of intrinsi-                 work by Chou et al. (58). Through-hydrogen bond 3HJNC′ scalar coupling
cally disordered proteins with their binding partners. Further                  constants were calculated according to the work by Barfield (59). RDCs of
studies that examine the performance of a99SB-disp in simulations               folded proteins were calculated as reported previously (60). RDCs of dis-
of a wider variety of disordered proteins and explore its perfor-               ordered proteins were calculated using PALES (61) using a local alignment
mance from the perspective of polymer physics (43) should also be               window of 15 residues. Backbone amide and methyl S2 order parameters
of considerable interest.                                                       were calculated from the value of the internal autocorrelation functions
                                                                                of the relevant bond vectors at lag times corresponding to the experi-
   It is notable that the transferability of a99SB-disp was achieved
                                                                                mentally determined rotational correlation times as described previously
within the constraints of the approximate functional forms used
                                                                                (62). Internal autocorrelation functions were calculated after aligning
in current fixed charge force fields. The parameters of a99SB-                  trajectories to the backbone atoms of the simulation starting structures
disp are the result of introducing modest changes to an existing                for ubiquitin, GB3, and HEWL and to backbone atoms of the stable leu-
force field to enable the accurate description of both ordered                  cine zipper coiled coil dimer interface for GCN4 (63). NMR chemical shifts
and disordered proteins. We found that we were able to achieve                  were calculated using Sparta+ (64). PREs were calculated as described
this goal by modifying the water model and iteratively testing                  previously (7).
small changes in backbone torsion corrections and the strength
of a backbone O-H LJ pair. We believe that the demonstration                    Calculation of Normalized Force-Field Scores. To compare the relative accuracy
that the simplified functional form of a nonpolarizable force field             of each force field, we report normalized force-field scores. For folded
is sufficient to describe folded proteins and a wide range of                   proteins, the rmsd from each class of experimental data, such as side-chain
disordered and partially disordered systems provides a note-                    scalar couplings, is normalized by the smallest observed rmsd among the
worthy proof of principle and that the accuracy achieved in                     seven force fields examined here. The normalized force-field score is de-
                                                                                termined by taking the average of the normalized rmsds over all classes of
a99SB-disp simulations of folded proteins, disordered proteins,
                                                                                experimental measurements (the classes used for a specific protein are given
fast-folding proteins, and multidomain proteins suggests that this
                                                                                in the first columns of SI Appendix, Tables S3–S6; note that a class may in-
force field could be useful for the accurate simulation of a wide               clude multiple datasets listed in SI Appendix, Table S1):
variety of systems that present difficulties for existing force fields.
   Due to the computational cost of obtaining sufficiently con-                                                               1 XN
                                                                                                                                     FFrmsd
verged simulations of the proteins in our training set, our search                                 Folded Protein FFScore =                  ,
                                                                                                                              N i=1 rmsdNorm
for a set of optimal parameters was not exhaustive. It is thus
possible that the performance of a99SB-disp could benefit from                  where N is the number of classes of experimental data considered, FFrmsd is
further optimization. In particular, it is likely that modifications            the rmsd of the simulated values from the corresponding experimental
not explored in this study, such as more extensive changes to the               values for class i, and rmsdNorm is the smallest observed rmsd of all of the
nonbonded parameters, could further improve a99SB-disp (and                     seven force fields examined in this study for class i. In this metric, a nor-
                                                                                malized FFScore of one indicates that a force field produces the closest
other fixed charge force fields). Joint optimizations of alkane
                                                                                agreement with experiment among all of the force fields tested for all of the
vdW terms (such as those introduced in C36m) and water model
                                                                                classes of experimental observables considered.
parameters, for example, may better capture the physics of the
                                                                                   For disordered proteins, GCN4, and calmodulin, force-field scores are
hydrophobic effect and further improve the ability of fixed                     computed as a combination of a backbone NMR chemical shift score (CSScore),
charge models to balance the stability of small peptides and the                a score based on additional NMR measurements (NMRScore), and an Rg de-
dimensions of disordered proteins. The benchmark set of pro-                    viation penalty (RgPenalty). The CSScore is determined analogously to the
teins described here should provide a valuable tool in future                   folded protein score by normalizing the rmsd for each class of chemical shift
efforts to develop force fields that accurately describe a broad                type (the classes are listed in SI Appendix, Tables S7–S17) (for drkN SH3, for
range of disordered systems.                                                    example, the classes are Cα, Hα, HN, C′, and Cβ) by the smallest rmsd observed
                                                                                for the seven force fields and taking an average of the normalized rmsds
Methods                                                                         over all sets of experimental chemical shifts. The NMR score is computed
MD Simulations. Details of the MD simulation setup for each of the systems      analogously for all additional classes of NMR measurements. The RgPenalty is
studied in this work can be found in SI Appendix, Table S16. All systems were   zero if the average simulated Rg is within the experimentally estimated
simulated using the following force fields: a99SB*-ILDN (11, 12) with TIP3P     error (RgExp error). For deviations larger than the estimated experimental
(13), C22* (14) with TIP3P-CHARMM (34), C36m (6), a03ws (containing             error, the RgPenalty is calculated as

E4764 | www.pnas.org/cgi/doi/10.1073/pnas.1800690115                                                                                             Robustelli et al.
                                                                                                                                                                                               PNAS PLUS

                                      jRgExp − RgSim j − RgExp error                             experiment for each of the experimental measurements considered here for
                        RgPenalty =                                  .                           each force field. To provide a measure of the sensitivity of the calculated force-
                                                 RgExp
                                                                                                 field scores to the initial simulation conditions on the timescales examined in
The combined disordered protein force-field score is computed as                                 this study, we repeated simulations of the folded and disordered proteins ex-
                                                                                                 amined in this study using the a99SB-disp force field with a different set of
                                              CS Score + NMR Score
           Disordered Protein FFScore =                            + RgPenalty .                 randomized initial velocities. We compare the resulting force-field scores with
                                                                                                 those obtained from the previous set of simulations in SI Appendix, Fig. S14.
We find it helpful to summarize the accuracy of each force field in this way as
a single number. Clearly, however, the details of the definition of the score                    ACKNOWLEDGMENTS. We thank Michael Eastwood for helpful discussions
are, to some extent, arbitrary. To facilitate examination of alternative scores,                 and a critical reading of the manuscript and Rebecca Bish-Cornelissen and
we have included in SI Appendix the deviation of the simulated values from                       Berkman Frank for editorial assistance.

 1. Lange OF, van der Spoel D, de Groot BL (2010) Scrutinizing molecular mechanics force         29. Martin EW, et al. (2016) Sequence determinants of the conformational properties of
    fields on the submicrosecond timescale with NMR data. Biophys J 99:647–655.                      an intrinsically disordered protein prior to and upon multisite phosphorylation. J Am
 2. Lindorff-Larsen K, et al. (2012) Systematic validation of protein force fields against           Chem Soc 138:15323–15335.
    experimental data. PLoS One 7:e32131.                                                        30. Bracken C, Carr PA, Cavanagh J, Palmer AG, 3rd (1999) Temperature dependence of
 3. Beauchamp KA, Lin YS, Das R, Pande VS (2012) Are protein force fields getting better?            intramolecular dynamics of the basic leucine zipper of GCN4: Implications for the
    A systematic benchmark on 524 diverse NMR measurements. J Chem Theory Comput                     entropy of association with DNA. J Mol Biol 285:2133–2146.
    8:1409–1414.                                                                                 31. Graf J, Nguyen PH, Stock G, Schwalbe H (2007) Structure and dynamics of the ho-
 4. Lindorff-Larsen K, Piana S, Dror RO, Shaw DE (2011) How fast-folding proteins fold.              mologous series of alanine peptides: A joint molecular dynamics/NMR study. J Am
    Science 334:517–520.                                                                             Chem Soc 129:1179–1189.
 5. Mittal J, Best RB (2010) Tackling force-field bias in protein folding simulations: Folding   32. Horn HW, et al. (2004) Development of an improved four-site water model for bio-
    of Villin HP35 and Pin WW domains in explicit water. Biophys J 99:L26–L28.                       molecular simulations: TIP4P-Ew. J Chem Phys 120:9665–9678.
 6. Huang J, et al. (2017) CHARMM36m: An improved force field for folded and in-                 33. Nerenberg PS, Head-Gordon T (2011) Optimizing protein−solvent force fields to re-
    trinsically disordered proteins. Nat Methods 14:71–73.                                           produce intrinsic conformational preferences of model peptides. J Chem Theory
 7. Piana S, Donchev AG, Robustelli P, Shaw DE (2015) Water dispersion interactions                  Comput 7:1220–1230.
    strongly influence simulated structural properties of disordered protein states. J Phys      34. MacKerell AD, et al. (1998) All-atom empirical potential for molecular modeling and
    Chem B 119:5113–5123.                                                                            dynamics studies of proteins. J Phys Chem B 102:3586–3616.
 8. Best RB, Zheng W, Mittal J (2014) Balanced protein–water interactions improve                35. Mao B, Tejero R, Baker D, Montelione GT (2014) Protein NMR structures refined with
    properties of disordered proteins and non-specific protein association. J Chem Theory            Rosetta have higher accuracy relative to corresponding X-ray crystal structures. J Am
    Comput 10:5113–5124.                                                                             Chem Soc 136:1893–1906.
 9. Nerenberg PS, Jo B, So C, Tripathy A, Head-Gordon T (2012) Optimizing solute-water           36. Best RB, de Sancho D, Mittal J (2012) Residue-specific α-helix propensities from mo-
    van der Waals interactions to reproduce solvation free energies. J Phys Chem B 116:              lecular simulation. Biophys J 102:1462–1467.
    4524–4534.                                                                                   37. Bertini I, et al. (2004) Experimentally exploring the conformational space sampled by

                                                                                                                                                                                                  BIOPHYSICS AND
10. Best RB, Mittal J (2010) Protein simulations with an optimized water model: Co-                  domain reorientation in calmodulin. Proc Natl Acad Sci USA 101:6841–6846.
    operative helix formation and temperature-induced unfolded state collapse. J Phys            38. Bertini I, et al. (2010) Conformational space of flexible biological macromolecules
                                                                                                     from average data. J Am Chem Soc 132:13553–13558.
    Chem B 114:14916–14923.
                                                                                                 39. Kukic P, Camilloni C, Cavalli A, Vendruscolo M (2014) Determination of the individual
11. Best RB, Hummer G (2009) Optimized molecular dynamics force fields applied to the
                                                                                                     roles of the linker residues in the interdomain motions of calmodulin using NMR
    helix-coil transition of polypeptides. J Phys Chem B 113:9004–9015.

                                                                                                                                                                                               COMPUTATIONAL BIOLOGY
                                                                                                     chemical shifts. J Mol Biol 426:1826–1838.
12. Lindorff-Larsen K, et al. (2010) Improved side-chain torsion potentials for the Amber
                                                                                                 40. Chattopadhyaya R, Meador WE, Means AR, Quiocho FA (1992) Calmodulin structure
    ff99SB protein force field. Proteins 78:1950–1958.
                                                                                                     refined at 1.7 A resolution. J Mol Biol 228:1177–1192.
13. Jorgensen WL, Chandrasekhar J, Madura JD, Impey RW, Klein ML (1983) Comparison
                                                                                                 41. Jiang F, Han W, Wu YD (2013) The intrinsic conformational features of amino acids
    of simple potential functions for simulating liquid water. J Chem Phys 79:926–935.
                                                                                                     from a protein coil library and their applications in force field development. Phys
14. Piana S, Lindorff-Larsen K, Shaw DE (2011) How robust are protein folding simula-
                                                                                                     Chem Chem Phys 15:3413–3428.
    tions with respect to force field parameterization? Biophys J 100:L47–L49.
                                                                                                 42. Jiang F, Zhou C-Y, Wu Y-D (2014) Residue-specific force field based on the protein coil
15. Chou JJ, Li S, Klee CB, Bax A (2001) Solution structure of Ca(2+)-calmodulin reveals
                                                                                                     library. RSFF1: Modification of OPLS-AA/L. J Phys Chem B 118:6983–6998.
    flexible hand-like properties of its domains. Nat Struct Biol 8:990–997.
                                                                                                 43. Mao AH, Crick SL, Vitalis A, Chicoine CL, Pappu RV (2010) Net charge per residue
16. Kubelka J, Chiu TK, Davies DR, Eaton WA, Hofrichter J (2006) Sub-microsecond pro-
                                                                                                     modulates conformational ensembles of intrinsically disordered proteins. Proc Natl
    tein folding. J Mol Biol 359:546–553.
                                                                                                     Acad Sci USA 107:8183–8188.
17. Neidigh JW, Fesinmeyer RM, Andersen NH (2002) Designing a 20-residue protein. Nat
                                                                                                 44. Bowers KJ, et al. (2006) Scalable algorithms for molecular dynamics simulations on
    Struct Biol 9:425–430.
                                                                                                     commodity clusters. Proceedings of the ACM/IEEE Conference on Supercomputing
18. Piana S, et al. (2011) Computational design and experimental testing of the fastest-
                                                                                                     (SC06) (IEEE, New York).
    folding β-sheet protein. J Mol Biol 405:43–48.
                                                                                                 45. Nosé S (1984) A unified formulation of the constant temperature molecular dynamics
19. Shalongo W, Dugad L, Stellwagen E (1994) Distribution of helicity within the model
                                                                                                     methods. J Chem Phys 81:511–519.
    peptide acetyl(AAQAA)3amide. J Am Chem Soc 116:8288–8293.
                                                                                                 46. Hoover WG (1985) Canonical dynamics: Equilibrium phase-space distributions. Phys
20. Honda S, et al. (2008) Crystal structure of a ten-amino acid protein. J Am Chem Soc
                                                                                                     Rev A Gen Phys 31:1695–1697.
    130:15327–15331.
                                                                                                 47. Martyna GJ, Tobias DJ, Klein ML (1994) Constant pressure molecular dynamics algo-
21. Iesmantavičius V, et al. (2013) Modulation of the intrinsic helix propensity of an in-
                                                                                                     rithms. J Chem Phys 101:4177–4189.
    trinsically disordered protein reveals long-range helix-helix interactions. J Am Chem
                                                                                                 48. Shaw DE, et al. (2009) Millisecond-scale molecular dynamics simulations on Anton.
    Soc 135:10155–10163.                                                                             Proceedings of the Conference on High Performance Computing, Networking,
22. Zhang O, Forman-Kay JD (1995) Structural characterization of folded and unfolded
                                                                                                     Storage and Analysis (SC09) (ACM, New York).
    states of an SH3 domain in equilibrium in aqueous buffer. Biochemistry 34:                   49. Tuckerman M, Berne BJ, Martyna GJ (1992) Reversible multiple time scale molecular
    6784–6794.                                                                                       dynamics. J Chem Phys 97:1990–2001.
23. Bertoncini CW, et al. (2005) Release of long-range tertiary interactions potentiates         50. Kräutler V, Van Gunsteren WF, Hünenberger PH (2001) A fast SHAKE algorithm to
    aggregation of natively unstructured α-synuclein. Proc Natl Acad Sci USA 102:                    solve distance constraint equations for small molecules in molecular dynamics simu-
    1430–1435.                                                                                       lations. J Comput Chem 22:501–508.
24. Jensen MR, et al. (2011) Intrinsic disorder in measles virus nucleocapsids. Proc Natl        51. Shan Y, Klepeis JL, Eastwood MP, Dror RO, Shaw DE (2005) Gaussian split Ewald: A
    Acad Sci USA 108:9839–9844.                                                                      fast Ewald mesh method for molecular simulation. J Chem Phys 122:54101.
25. Sgourakis NG, Yan Y, McCallum SA, Wang C, Garcia AE (2007) The Alzheimer’s pep-              52. Marinari E, Parisi G (1992) Simulated tempering: A new Monte Carlo scheme.
    tides Abeta40 and 42 adopt distinct conformations in water: A combined MD/NMR                    Europhys Lett 19:451–458.
    study. J Mol Biol 368:1448–1457.                                                             53. Karplus M (1959) Contact electron-spin coupling of nuclear magnetic moments.
26. Sterckx YG, et al. (2014) Small-angle X-ray scattering- and nuclear magnetic                     J Chem Phys 30:11–15.
    resonance-derived conformational ensemble of the highly flexible antitoxin PaaA2.            54. Vögeli B, Ying J, Grishaev A, Bax A (2007) Limits on variations in protein backbone
    Structure 22:854–865.                                                                            dynamics from precise measurements of scalar couplings. J Am Chem Soc 129:
27. De Biasio A, et al. (2014) p15PAF is an intrinsically disordered protein with non-               9377–9385.
    random structural preferences at sites of interaction with other proteins. Biophys J         55. Lindorff-Larsen K, Best RB, Vendruscolo M (2005) Interpreting dynamically-averaged
    106:865–874.                                                                                     scalar couplings in proteins. J Biomol NMR 32:273–280.
28. Mittag T, et al. (2010) Structure/function implications in a dynamic complex of the          56. Li F, Lee JH, Grishaev A, Ying J, Bax A (2015) High accuracy of Karplus equations for
    intrinsically disordered Sic1 with the Cdc4 subunit of an SCF ubiquitin ligase. Structure        relating three-bond J couplings to protein backbone torsion angles. ChemPhysChem
    18:494–506.                                                                                      16:572–578.

Robustelli et al.                                                                                                                                PNAS | vol. 115 | no. 21 | E4765
57. Pérez C, Löhr F, Rüterjans H, Schmidt JM (2001) Self-consistent Karplus parametriza-      63. Robustelli P, Trbovic N, Friesner RA, Palmer AG, 3rd (2013) Conformational dynamics
    tion of 3J couplings depending on the polypeptide side-chain torsion chi1. J Am Chem          of the partially disordered yeast transcription factor GCN4. J Chem Theory Comput 9:
    Soc 123:7081–7093.                                                                            5190–5200.
58. Chou JJ, Case DA, Bax A (2003) Insights into the mobility of methyl-bearing side chains   64. Shen Y, Bax A (2010) SPARTA+: A modest improvement in empirical NMR
    in proteins from (3)J(CC) and (3)J(CN) couplings. J Am Chem Soc 125:8959–8966.                chemical shift prediction by means of an artificial neural network. J Biomol NMR
59. Barfield M (2002) Structural dependencies of interresidue scalar coupling (h3)J(NC’)
                                                                                                  48:13–22.
    and donor (1)H chemical shifts in the hydrogen bonding regions of proteins. J Am
                                                                                              65. Marsh JA, Forman-Kay JD (2009) Structure and disorder in an unfolded state under
    Chem Soc 124:4158–4168.
                                                                                                  nondenaturing conditions from ensemble models consistent with a large number of
60. Lindorff-Larsen K, Best RB, Depristo MA, Dobson CM, Vendruscolo M (2005) Simul-
    taneous determination of protein structure and dynamics. Nature 433:128–132.                  experimental restraints. J Mol Biol 391:359–374.
61. Zweckstetter M, Bax A (2000) Prediction of sterically induced alignment in a dilute       66. Ozenne V, et al. (2012) Mapping the potential energy landscape of intrinsically dis-
    liquid crystalline phase: Aid to protein structure determination by NMR. J Am Chem            ordered proteins at amino acid resolution. J Am Chem Soc 134:15138–15148.
    Soc 122:3791–3792.                                                                        67. Camilloni C, De Simone A, Vranken WF, Vendruscolo M (2012) Determination of
62. Trbovic N, Kim B, Friesner RA, Palmer AG, 3rd (2008) Structural analysis of protein           secondary structure populations in disordered states of proteins using nuclear mag-
    dynamics by MD simulations and NMR spin-relaxation. Proteins 71:684–694.                      netic resonance chemical shifts. Biochemistry 51:2224–2231.

E4766 | www.pnas.org/cgi/doi/10.1073/pnas.1800690115                                                                                                                 Robustelli et al.
