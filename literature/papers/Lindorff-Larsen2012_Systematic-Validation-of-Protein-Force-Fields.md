# Systematic Validation of Protein Force Fields against Experimental Data

**Authors:** Kresten Lindorff-Larsen, Paul Maragakis, Stefano Piana, Michael P. Eastwood, Ron O. Dror, David E. Shaw
**Year:** 2012
**Venue:** PLoS ONE
**DOI:** 10.1371/journal.pone.0032131
**Source PDF URL:** https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0032131&type=printable
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Systematic Validation of Protein Force Fields against
Experimental Data
Kresten Lindorff-Larsen1., Paul Maragakis1., Stefano Piana1., Michael P. Eastwood1, Ron O. Dror1,
David E. Shaw1,2*
1 D. E. Shaw Research, New York, New York, United States of America, 2 Center for Computational Biology and Bioinformatics, Columbia University, New York, New York,
United States of America

     Abstract
     Molecular dynamics simulations provide a vehicle for capturing the structures, motions, and interactions of biological
     macromolecules in full atomic detail. The accuracy of such simulations, however, is critically dependent on the force field—
     the mathematical model used to approximate the atomic-level forces acting on the simulated molecular system. Here we
     present a systematic and extensive evaluation of eight different protein force fields based on comparisons of experimental
     data with molecular dynamics simulations that reach a previously inaccessible timescale. First, through extensive
     comparisons with experimental NMR data, we examined the force fields’ abilities to describe the structure and fluctuations
     of folded proteins. Second, we quantified potential biases towards different secondary structure types by comparing
     experimental and simulation data for small peptides that preferentially populate either helical or sheet-like structures. Third,
     we tested the force fields’ abilities to fold two small proteins—one a-helical, the other with b-sheet structure. The results
     suggest that force fields have improved over time, and that the most recent versions, while not perfect, provide an accurate
     description of many structural and dynamical properties of proteins.

  Citation: Lindorff-Larsen K, Maragakis P, Piana S, Eastwood MP, Dror RO, et al. (2012) Systematic Validation of Protein Force Fields against Experimental Data. PLoS
  ONE 7(2): e32131. doi:10.1371/journal.pone.0032131
  Editor: Daniel J. Muller, Swiss Federal Institute of Technology Zurich, Switzerland
  Received November 1, 2011; Accepted January 24, 2012; Published February 22, 2012
  Copyright: ß 2012 Lindorff-Larsen et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits
  unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
  Funding: These authors have no support or funding to report.
  Competing Interests: The authors have read the journal’s policy and have the following conflicts: All the authors are affiliated with D. E. Shaw Research, the
  funder of this study. This research was conducted within D. E. Shaw Research, of which D.E.S. is the sole beneficial owner and Chief Scientist. There are no patents,
  products in development or marketed products to declare. This does not alter the authors’ adherence to all the PLoS ONE policies on sharing data and materials,
  as detailed online in the guide for authors.
  * E-mail: David.Shaw@DEShawResearch.com
  . These authors contributed equally to this work.

Introduction                                                                             have not been changed for some time, a number of force fields
                                                                                         have recently been refined in order to improve their accuracy for
   Historically, two principal factors have limited the utility of                       proteins and peptides. These developments have led to a plethora
molecular dynamics (MD) simulations as a research tool in biology                        of new force fields that often differ only in the parameters
and biophysics [1]. First, lengthy and computationally intensive                         associated with a few (important) torsion angles.
simulations may be required to sufficiently sample the conforma-                            With some notable exceptions [10,11], previous comparisons of
tional space of the molecules under study. Thanks to recent                              different force fields’ abilities to reproduce the structure and
developments in computing hardware [2–4] and in methods to                               dynamics of peptides and proteins have mostly involved only a few
distribute [5] and parallelize [6] simulations or enhance sampling                       versions of related force fields. In most cases such studies have
efficiency [7], it is now possible to simulate directly protein                          utilized only one or a few related test systems, leaving unresolved
dynamics on the millisecond timescale [8] or to reconstruct long-                        questions about how different force fields compare more generally
timescale behavior from shorter simulations [9].                                         in their ability to provide an accurate description of protein
   Second, in order for MD simulations to provide a realistic                            conformational ensembles. Here we describe the results of an
description of the molecules under study, the molecular mechanics                        extensive test of eight protein force fields, using simulations of a
force field used in such simulations must be sufficiently accurate to                    number of diverse protein and peptide systems and subsequent
provide biologically useful results. A large number of force fields                      comparison of the resulting conformational ensembles with
are available for studying proteins by MD simulation. While the                          experimental data.
mathematical functional forms of many of these force fields are                             When evaluating a force field, it is important to sample the test
quite similar, they differ in the parameters that describe the                           systems as extensively as possible in order to ensure that the level
various energetic components and in the methods employed to                              of agreement with experiments is a reliable measure of the
obtain these parameters. Current protein force fields were for the                       accuracy of the force field. The choice of test systems should thus
most part derived by fitting parameters to data from quantum-                            be based in part on the extent to which such systems could be
level calculations or experiments on small molecules thought to                          sampled using available computational resources. We have
mimic the properties of proteins. Although most such parameters                          recently described the construction and initial applications of a

       PLoS ONE | www.plosone.org                                                    1                              February 2012 | Volume 7 | Issue 2 | e32131
                                                                                                        Systematic Validation of Protein Force Fields

specialized computer for MD simulations called Anton [2,8].                   ensemble sufficiently well using MD simulations on Anton. We
Anton is capable of performing simulations that are two orders of             thus performed 10-ms simulations for both ubiquitin and GB3 in
magnitude longer than the prior state of the art, enabling much               each of the eight force fields considered here.
more comprehensive testing of force fields than was previously                   In all but one case we found the native state to be stable and the
feasible.                                                                     protein to remain close to the experimental structure throughout
   We have used Anton to perform a broad range of computa-                    the 10-ms MD simulation. (In the case of GB3 simulated with
tionally demanding tests using protein and peptide systems. For               CHARMM22, we found that the native state was not stable and
each of the eight different force fields that we examined, we ran a           that the protein unfolded during the simulation.) We focused our
total of 100 ms of simulation distributed across six different                comparison on the polypeptide backbone because this is the most
molecular systems: (i) two folded proteins, (ii) two peptides that            fundamental part of the protein structure, and because most
preferentially populate a helical or strand-like structure, respec-           problems in the description of side chains will eventually reveal
tively, and (iii) an a-helical and a b-sheet protein, simulated at a          themselves at the level of the backbone as the protein distorts in an
temperature where they would be expected to fold and unfold.                  attempt to accommodate inaccurate rotamer distributions of the
Our results suggest that force fields are improving over time and             side chains. In Figure 1, we show the agreement between the
that, for the tests described here, simulations in two of the force           ensembles obtained from simulations and NMR measurements of
fields result in particularly good overall agreement with experi-             backbone scalar and residual dipolar couplings as well as NMR
mental data. Our results also highlight certain remaining                     order parameters. Overall, four force fields (ff99SB-ILDN,
deficiencies in all force fields studied here and point towards               ff99SB*-ILDN, CHARMM27 and CHARMM22*) provide a
areas for future improvements.                                                reasonably accurate description of the native state of ubiquitin and
                                                                              GB3, close to that of ensembles that were reconstructed to fit the
Results                                                                       experimental data [22]. For the four of the eight force fields that
                                                                              had been studied previously using similar tests [11], we find good
   In the last few years, a substantial number of studies have                agreement between our results and these earlier studies.
revised existing force fields by modifying the torsion potentials
associated with a few important dihedral angles. Simmerling and               Temperature-dependent structural propensities in short
colleagues [12] modified the backbone potential in the original
                                                                              peptides
Amber ff99 force field by fitting to additional quantum-level data
                                                                                 The simulations of ubiquitin and GB3 provide a detailed test of
and thus derived the improved Amber ff99SB force field. Best and
                                                                              a force field’s ability to describe a well-defined folded state and the
colleagues followed up on this work by modifying the backbone
                                                                              fluctuations within that state. In those simulations, only a few
potential in ff99SB and ff03 to obtain a better energetic balance
                                                                              substantial conformational excursions are observed. These tests
between helix and coil conformations, thus producing the ff99SB*
                                                                              might thus miss differences in force fields that arise, for example,
and ff03* force fields [13]. We modified the side-chain torsion
                                                                              from variations in the relative energies between the different basins
potential for four amino acid types in ff99SB to produce the
                                                                              on the Ramachandran map. Indeed, although our tests of
ff99SB-ILDN force field [14], and more recently we changed
                                                                              ubiquitin and GB3 suggested that CHARMM27 and ff99SB-
parameters associated with both the backbone and certain side
                                                                              ILDN perform equally well, it has been shown that CHARMM27
chains in a CHARMM force field to produce CHARMM22* [15].
                                                                              severely overstabilizes the formation of helical structures [10,23]
We also demonstrated that the ‘‘ILDN’’ side chain modifications               and that ff99SB-ILDN underestimates the stability of helices [13].
can be combined with the ff99SB* potential to produce the
                                                                                 We thus performed simulations of two small peptide systems
ff99SB*-ILDN force field [15].
                                                                              with the aim of evaluating how well the eight force fields provide a
   We decided to evaluate a number of the modified force fields               balance between propensity to form helical, sheet-like, and coil
described above, as well as the force fields from which they were             structures. The first test involves a 15-residue peptide consisting of
originally derived. We also included the widely used OPLS-AA                  three repeats of the amino acid sequence AAQAA [24]. NMR and
force field, such that our comparison set was comprised of the                circular dichroism measurements suggest that this peptide is
following eight protein force fields: Amber ff99SB-ILDN [12,14],              ,45% helical at a temperature of 275 K, and that the helicity has
Amber ff99SB*-ILDN [12–14] Amber ff03 [16], Amber ff03*                       a relatively steep temperature dependency resulting in less than
[13,16], OPLS-AA [17], CHARMM22 [18], CHARMM22 with                           10% helicity at 320 K. Using 10 ms of simulated tempering MD
the CMAP correction ([18,19]; herein termed CHARMM27), and                    simulations, we calculated the temperature-dependent fraction of
CHARMM22* [15,18,19].                                                         helical structure of the AAQAA peptide in each of the eight force
                                                                              fields (Fig. 2a). The results confirm that the force fields display a
Comparison of simulations with NMR data for folded                            broad range of propensities towards forming helical structure, with
proteins                                                                      CHARMM27 and Amber ff03 overstabilizing helices and ff99SB-
   MD simulations are often used to study the structural dynamics             ILDN understabilizing them. The three ‘‘helix coil–balanced’’
of folded proteins, and we thus first examined the ability of the             force fields (ff99SB*-ILDN, ff03* and CHARMM22*) all provide
eight force fields to reproduce experimental data describing the              a better description of this peptide system. This result is not
folded-state structure and dynamics of two well-characterized                 surprising, however, given that the comparison with the helicity of
proteins, ubiquitin and GB3. Both proteins are relatively small (76           the AAQAA peptide was part of the optimization procedure used
and 56 residues, respectively) and have been characterized                    to refine these force fields.
extensively by solution-state NMR spectroscopy, thus providing                   As a second test, we performed a comparable set of calculations
experimental data for evaluating the ability of a force field to              for the 10-residue peptide CLN025 [25]. CLN025 preferentially
describe the folded state of a protein correctly [11]. Further, these         attains a hairpin-like structure in solution at temperatures less than
NMR experiments have shown that the two proteins are very                     ,340 K, and only at higher temperatures is the unfolded ‘‘coil’’
stable and display only relatively little (albeit possibly biologically       structure the free-energy minimum. In Figure 2b, we show the
important) motion on timescales beyond microseconds [20,21],                  temperature-dependent stability of CLN025 in the eight force
suggesting that it should be possible to sample the native state              fields and the comparison to the experimentally derived melting

       PLoS ONE | www.plosone.org                                         2                          February 2012 | Volume 7 | Issue 2 | e32131
                                                                                                      Systematic Validation of Protein Force Fields

Figure 1. Comparison between simulation and experimental NMR data probing the structure and dynamics of the backbone in
folded proteins. The plot shows the results for (a, b, c) ubiquitin and (d, e, f) GB3. In (a, d) we show the agreement between calculated and
experimental scalar couplings, in (b, e) the agreement between calculated and experimental order parameters, and in (c, f) the agreement between
calculated and experimental residual dipolar couplings. Low RMSD values or Q scores [39] imply better agreement with experiments. Error bars
represent the standard error of the mean.
doi:10.1371/journal.pone.0032131.g001

curve. As for the AAQAA system, the eight force fields display a            of a force field is thus to be able to find the native state of at least
broad range of behaviors, with the very helical CHARMM27                    two proteins of very different structural classes, such as one with an
force field being the biggest outlier, as it forms almost no folded         a-helical structure and one with a b-sheet [8,28].
structures at any temperature.                                                 The timescales for the folding of even the fastest-folding proteins
   In addition to quantifying the different force fields’ ability to        are in the microsecond range, so systematic studies of different
capture the subtle balance between helical, sheet-like and coil             force fields’ abilities to fold proteins have previously been
structures, these simulations also highlight an important deficiency        computationally demanding. Anton’s ability to perform long
in current molecular mechanics force fields [13]. In particular,            MD simulations now makes such a test feasible, and we performed
even for the most well-balanced force fields, the temperature               folding simulations for two proteins using all eight force fields. For
dependency of the melting of the AAQAA-helix and the native                 these tests, we chose the fastest folding a- and b-proteins known:
state of CLN025 is much weaker than suggested from experiment.              the Nle/Nle double mutant of the villin headpiece, a small a-
This in turn means that these force fields can match the                    helical protein with a folding time of ,1 ms [29]; and the GTT
experiments closely only in a narrow range of temperatures.                 variant of the FiP35 WW domain, which folds in ,4–6 ms [30]
Capturing the cooperativity of helix and hairpin formation and              and whose native state consists of three b-strands.
melting thus appears to be a general area for further improvement              Protein folding is a stochastic process, and one expects
of force fields.                                                            considerable variation in the exponentially distributed waiting
                                                                            times between individual folding events. For both villin and the
Simulating the folding of a-helical and b-sheet proteins                    WW domain, we performed simulations with a length ,10 times
   The ability to fold a protein from an unfolded state to the              the experimentally determined folding time: simulation lengths
correct native structure is a very stringent test of a molecular            were 10 ms for villin and 50 ms for the WW domain. We
mechanics force field [26]. For many proteins, the folding free             performed these simulations at the experimental melting temper-
energy is relatively small, suggesting that even minor force field          ature, where the experimental folding and unfolding times are
errors could result in the native state not being the free-energy           equal. Simulations with an accurate force field that are an order of
minimum in simulation. Further, the folding process from an                 magnitude longer than the experimental average folding time are
unfolded to a folded state involves structural changes throughout           expected to result in the observation of reversible folding and
the protein—at the level of both the side chains and the                    unfolding.
polypeptide backbone—causing small errors in individual force                  Table 1 shows the number of folding and unfolding events
field terms (such as for the backbone torsions) to be amplified [27].       observed during the simulations of villin and WW in each of the
As a result, simulations of protein folding might be able to detect         eight force fields. In six of the eight force fields we were able to fold
even relatively minor problems in force fields. In certain cases, it        villin to its correct native state, and in five force fields the WW
might be possible to compensate for such force field deficiencies in        domain folded. In four force fields we were able to fold both villin
folding simulations by choosing a force field that overstabilizes the       and the WW domain; these include all three helix-coil balanced
secondary structure found in the native state. A more stringent test        force fields (ff99SB*-ILDN, ff03* and CHARMM22*) as well as

      PLoS ONE | www.plosone.org                                        3                           February 2012 | Volume 7 | Issue 2 | e32131
                                                                                                            Systematic Validation of Protein Force Fields

                                                                                Table 1. Evaluating force fields by folding simulations.

                                                                                Force field                               Villin             WW

                                                                                Amber ff99SB-ILDN                         3 (1/1)            3 (1/0)
                                                                                Amber ff99SB*-ILDN                        3 (2/2)            3 (1/0)
                                                                                Amber ff03                                3 (1/0)            7
                                                                                Amber ff03*                               3 (1/1)            3 (1/1)
                                                                                OPLS-AA                                   7                  3 (1/0)
                                                                                CHARMM22                                  7                  7
                                                                                CHARMM27                                  3 (1/0)            7
                                                                                CHARMM22*                                 3 (4/4)            3 (1/1)

                                                                                The table shows whether we observed any folding events of villin and the WW
                                                                                domain in our simulations. A check mark indicates that simulations started in
                                                                                the unfolded state were able to reach the folded state in 10 ms (villin at 360 K)
                                                                                or 50 ms (WW domain at 370 K), while an ‘‘X’’ means that we did not observe
                                                                                any folding events. In those cases where we did observe at least one folding
                                                                                event, the numbers in parentheses indicate the number of folding/unfolding
                                                                                events we observed in that simulation. For ff99SB-ILDN, for example, we
                                                                                observed first a folding event and subsequently an unfolding event for villin,
                                                                                but only a folding event with no subsequent unfolding event for the WW
                                                                                domain. Since the simulations are roughly 10 times longer than the
                                                                                experimental folding and unfolding times, one would expect roughly five
                                                                                folding and five unfolding events in a force field that models perfectly both the
                                                                                kinetics and thermodynamics of folding.
                                                                                doi:10.1371/journal.pone.0032131.t001

                                                                               suggests that the smaller (and easier to sample) peptide systems
                                                                               indeed contain useful information that can be used to optimize
                                                                               force fields for application to conformational changes in proteins.
                                                                               As sampling efficiency and force fields continue to improve in the
                                                                               future, we expect that more detailed and quantitative studies of the
                                                                               thermodynamics and kinetics of folding [31] might provide even
                                                                               more stringent tests of force fields.

Figure 2. Comparison between calculated and experimental                       Discussion
secondary structure propensities. In (a), we show the helical
fraction of the (AAQAA)3 15-mer peptide in simulations and experiment             We have presented a systematic comparison of a number of
as a function of temperature. In (b), we show the fraction folded of the       force fields for all-atom simulations in explicit solvent. Although
CLN025 10-residue peptide in simulations and experiments as a
function of temperature.                                                       several of the test systems have previously been used individually to
doi:10.1371/journal.pone.0032131.g002                                          evaluate force fields, the broad nature of the tests applied here—as
                                                                               well as the increased length of the simulations—allows us to draw
                                                                               broader conclusions about the ability of the various force fields to
ff99SB-ILDN (in agreement with earlier findings [8]). The two                  reproduce a range of experimentally measured properties
very helical force fields (ff03 and CHARMM27) were able to fold                correctly. For example, while Amber ff99SB-ILDN and
villin correctly, but were not able to fold the b-sheet–containing             CHARMM27 appear to describe folded proteins equally well
WW domain. For both of these force fields the villin domain                    (Fig. 1), our tests on flexible peptides (Fig. 2) revealed large
folded relatively quickly (0.2 ms and 0.8 ms for ff03 and                      differences between these two force fields. We thus stress the need
CHARMM27, respectively), after which the protein stayed folded                 for validating force fields using as broad a set of systems as
for the remainder of the simulation, suggesting that the native state          possible.
is too stable, as also observed previously [15]. For all four force               In an attempt to evaluate and compare the different force fields
fields that were able to fold both proteins, we also observed                  across all three sets of tests, we assigned a ‘‘force field score’’
reversible folding and unfolding of villin; only for CHARMM22*                 reflecting the degree of agreement between the experiments and
did we observe reversible folding of both proteins.                            simulations. While one might in principle define a score directly
   Even minor force field deficiencies can result in substantial               from a quantitative comparison between the calculated and
changes in calculated folding rates and melting temperature—                   experimental results, such a score would depend on a number of
even in the case where the folded state is a free-energy minimum.              somewhat arbitrary parameters and functional forms used to
Because the simulations were run for only 10 times the                         aggregate across the different results. Instead, we decided to assign
experimental folding time and only at a single temperature, one                a very simple score manually (using integer values ranging from 0
should avoid overinterpreting the results in Table 1. Nevertheless,            to 6, with low values indicating good agreement with experiments;
it is worth noting that the three force fields that were                       see Methods for details), thus explicitly acknowledging that the
parameterized to obtain a reasonable balance between helical                   score relies in part on subjective choices and that others might
and coil structures were all able to fold both an a-helical and a b-           assign different scores based on the same set of results. The
sheet protein. The agreement between these two different tests                 assigned scores indicate that two of the eight force fields, ff99SB*-

       PLoS ONE | www.plosone.org                                          4                             February 2012 | Volume 7 | Issue 2 | e32131
                                                                                                          Systematic Validation of Protein Force Fields

ILDN and CHARMM22*, perform consistently well in repro-                         were the high-resolution NMR structures of ubiquitin ([34]; PDB
ducing the experimental data in the set of tests presented here                 entry 1D3Z) and GB3 ([35]; PDB entry 1P7E). The structures were
(Fig. 3). As these two force fields are also among the most recent              solvated in a cubic box with side lengths 58 Å, and were first
ones, we examined whether force fields have generally improved                  minimized, heated to 300 K during 0.4 ns, and finally equilibrated
over time. The results show a clear correlation between the year of             in the NPT ensemble for 0.8 ns. The frame with the volume closest
publication of a force field and the assigned force field score,                to the average during this NPT simulation was used as starting point
suggesting that force fields are indeed improving over time (Fig. 3).           for the production simulations in the NVT ensemble, thus ensuring
   It should be noted that other factors will often be relevant to the          that the average pressure in the simulations is close to the reference
choice of a force field for specific types of MD simulations. Such              standard pressure. For both ubiquitin and GB3 we also performed
factors may include the availability of force field parameters for              simulations in the NPT ensemble (using ff99SB*-ILDN) and found
molecules other than proteins (e.g., lipids, nucleic acids, carbohy-            that the calculated NMR observables are within error the same as
drates, co-factors, substrates or drug molecules). In particular, it            those in the corresponding simulations in the NVT ensemble.
should be noted that our tests do not include any membrane                         We calculated backbone scalar couplings using published
proteins, and that the force field best used to describe such proteins          Karplus relationships for HNHA, HNCO and HNCB [36], and
might in principle depend on the lipid model employed.                          HACO [37] couplings and compared to experimental data
   Our results also highlight areas for future improvements of the              measured for ubiquitin ([38]; HNHA, HNCO, HNCB and
force fields we tested. These include the ability to model the                  HACO) and GB3 ([36]; HNHA, HNCO and HNCB). We
temperature dependency of the conformational propensities in                    calculated backbone residual dipolar couplings and the associated
both the AAQAA and CLN025 peptides, and to more accurately                      Q scores as previously described [39] and compared to
match the kinetics and thermodynamics of the folding of villin and              experimental values in ubiquitin [34] and GB3 [35]. Order
the WW domain. We are hopeful that the tests described here will                parameters were calculated from the values of the internal
prove useful in further refining contemporary force fields, thus                autocorrelation functions at lag times close to the experimentally
enhancing the value of MD simulation as a tool for elucidating the              determined rotational correlation times.
molecular details of important biological processes.                               Simulated tempering simulations and analysis of
                                                                                AAQAA and CLN025 peptides. The temperature-dependent
Methods                                                                         conformational properties of the (AAQAA)3 [24] and CLN025
                                                                                [25] peptides were obtained using simulated tempering simulations
   Common methods. All production molecular dynamics                            [40] in the NPT ensemble. In contrast to the simulations of folded
simulations were performed on Anton [2]. Simulations were                       proteins or of protein folding, we found it necessary to perform
performed in the TIP3P water model ([32]; for Amber and OPLS-                   these simulations in the NPT ensemble to avoid changing the
AA force fields) or the CHARMM modified TIP3P water model                       average pressure as the temperature varied. We used a 9.5-Å cutoff
([18,32]; for CHARMM force fields).
                                                                                for the Lennard-Jones and short-range electrostatic interactions;
   Simulations and analysis of the native state of                              long-range electrostatic interactions were treated with the Gaussian
ubiquitin and GB3. Production simulations of ubiquitin and                      split Ewald method [33].
GB3 were performed in the NVT ensemble. We used a 9.5-Å cutoff
                                                                                   The helical fraction of the AAQAA-peptide was calculated as
for the Lennard-Jones and short-range electrostatic interactions;
                                                                                the fraction of helical residues [13,15] at each temperature in the
long-range electrostatic interactions were treated with the Gaussian
                                                                                simulated tempering simulations and compared to the experimen-
split Ewald method [33]. The starting structures for the simulations
                                                                                tal values [24]. The fraction of the CLN025 that was folded was
                                                                                determined by applying a dual-cutoff approach [15,41] to separate
                                                                                the simulations into folded and unfolded states. In this analysis, a
                                                                                folding event was recorded if the Ca-RMSD to the experimental
                                                                                NMR structure dropped below 1.0 Å and an unfolding event was
                                                                                recorded once the same RMSD went above 4.0 Å.
                                                                                   Folding simulations of villin and WW domain. Simula-
                                                                                tions of fast-folding variants of villin [29] and the WW domain
                                                                                [30] were performed in the NVT ensemble using a Nose-Hoover
                                                                                thermostat and a force-shifted cutoff [42] of 10.0 Å (villin) or 10.5 Å
                                                                                (WW domain) for the Lennard-Jones and electrostatic interactions.
                                                                                The starting structures for the simulations were heat-unfolded states
                                                                                of the two proteins in a cubic box of water with side length 52 Å.
                                                                                The simulations were performed near the experimental melting
                                                                                temperatures (at 360 K for villin and 370 K for the WW domain).
                                                                                For the WW domain, we recorded a folding event when the Ca-
                                                                                RMSDs (to PDB entry 2F21) calculated over four stretches of amino
                                                                                acids all were below the cutoff value: 2–33 (2.0 Å), 8–22 (1.1 Å), 12–
                                                                                18 (0.6 Å), 19–30 (0.9 Å). An unfolding event was recorded when
Figure 3. Improvement of force fields over time. For each force                 the same set of RMSDs went above 7.0 Å, 5.8 Å, 1.8 Å and 3.8 Å,
field, we assigned a score depending on the agreement with                      respectively. For villin, we recorded a folding event when the Ca-
experiments in the tests presented here. Low scores indicate good               RMSDs (to PDB entry 2F4K) calculated over three stretches of
agreement with experiments. These scores are plotted against the year
                                                                                amino acids were all below the cutoff value: 3–31 (1.2 Å), 3–18
in which the force field was published. For the force fields that involve
multiple corrections (e.g., ff99SB*-ILDN), we use the year of the most          (0.9 Å), 14–31 (0.9 Å). An unfolding event was recorded when the
recently published correction.                                                  same set of RMSDs simultaneously went above 5.0 Å, 4.6 Å, and
doi:10.1371/journal.pone.0032131.g003                                           2.5 Å, respectively.

       PLoS ONE | www.plosone.org                                           5                           February 2012 | Volume 7 | Issue 2 | e32131
                                                                                                                          Systematic Validation of Protein Force Fields

   Assigning a force field score. For each of the three sets of                            presented in Figure 3, however, would not change even if the
tests we manually assigned to each force field a number in the                             AAQAA tests were excluded. Finally, we stress that the assigned
range 0–2, with 0 referring to a reasonable agreement, 1 to some                           scores rely in part on subjective choices and that different sets of
agreement and 2 to severe discrepancies with respect to the                                scores could be derived from the data presented in Figures 1 and 2
experimental data. The assigned scores for each of these tests                             and Table 1.
(folded proteins/peptides/folding) were 0/1/0 (ff99SB-ILDN), 0/
0/0 (ff99SB*-ILDN), 1/2/1 (ff03), 1/1/0 (ff03*), 2/1/1 (OPLS-                              Acknowledgments
AA), 2/1/2 (CHARMM22), 0/2/1 (CHARMM27) and 0/0/0
(CHARMM22*). Each force field was then assigned an overall                                 We thank Morten Jensen and John Klepeis for valuable discussions, and
score (between 0 and 6) that was the sum of the values for each of                         Mollie Kirk and Rebecca Kastleman for editorial assistance.
the three tests. When evaluating the results of the simulations of
the AAQAA and CLN025 peptides, we focused mostly on the                                    Author Contributions
temperature range around 280–320 K, where most biomolecular                                Conceived and designed the experiments: KL-L PM SP MPE ROD DES.
simulations are performed. Since simulations of the AAQAA                                  Performed the experiments: KL-L PM SP. Analyzed the data: KL-L PM
peptide were used in the re-parameterization of the three helix                            SP. Contributed reagents/materials/analysis tools: KL-L PM SP. Wrote
coil–balanced force fields, one could argue that these results should                      the paper: KL-L PM SP ROD DES.
not be included in the evaluation. The nature of the results

References
 1. Klepeis JL, Lindorff-Larson K, Dror RO, Shaw DE (2009) Long-timescale                  21. Fenwick RB, Esteban-Martı́n S, Richter B, Lee D, Walter KFA, et al. (2011)
    molecular dynamics simulations of protein structure and function. Curr Opin                Weak long-range correlated motions in a surface patch of ubiquitin involved in
    Struct Biol 19: 120–127.                                                                   molecular recognition. J Am Chem Soc 133: 10336–103369.
 2. Shaw DE, Dror RO, Salmon JK, Grossman JP, Mackenzie KM, et al. (2009)                  22. Lange OF, Lakomek N-A, Farès C, Schröder GF, Walter KFA, et al. (2008)
    Millisecond-scale molecular dynamics simulations on Anton. Proceedings of the              Recognition dynamics up to microseconds revealed from an RDC-derived
    Conference on High Performance Computing, Networking, Storage and                          ubiquitin ensemble in solution. Science 320: 1471–1475.
    Analysis (SC09). New York: ACM.                                                        23. Freddolino PL, Park S, Roux B, Schulten K (2009) Force field bias in protein
 3. Stone JE, Hardy DJ, Ufimtsev IS, Schulten K (2010) GPU-accelerated                         folding simulations. Biophys J 96: 3772–3780.
    molecular modeling coming of age. J Mol Graph Model 29: 116–125.                       24. Shalongo W, Dugad L, Stellwagen E (1994) Distribution of helicity within the
 4. Vendruscolo M, Dobson CM (2011) Protein dynamics: Moore’s law in                           model peptide acetyl(AAQAA)3amide. J Am Chem Soc 116: 8288–8293.
    molecular biology. Curr Biol 21: R68–R70.                                              25. Honda S, Akiba T, Kato YS, Sawada Y, Sekijima M, et al. (2008) Crystal
 5. Voter AF (1998) Parallel replica method for dynamics of infrequent events. Phys            structure of a ten-amino acid protein. J Am Chem Soc 130: 15327–15331.
    Rev B 57: R13985–R13988.                                                               26. Freddolin PL, Harrison CB, Liu Y, Schulten K (2010) Challenges in protein
                                                                                               folding simulations: timescale, representation, and analysis. Nat Phys 6:
 6. Bowers KJ, Dror RO, Shaw DE (2007) Zonal methods for the parallel execution
                                                                                               751–758.
    of range-limited N-body simulations. J Comput Phys 221: 303–329.
                                                                                           27. Faver JC, Benson ML, He X, Roberts BP, Wang B, et al. (2011) The energy
 7. Lei H, Duan Y (2007) Improved sampling methods for molecular simulation.
                                                                                               computation paradox and ab initio protein folding. PLoS One 6: e18868.
    Curr Opin Struct Biol 17: 187–191.                                                     28. Best RB, Mittal J (2010) Balance between alpha and beta structures in ab initio
 8. Shaw DE, Maragakis P, Lindroff-Larsen K, Piana S, Dror RO, et al. (2010)                   protein folding. J Phys Chem B 114: 8790–8798.
    Atomic-level characterization of the structural dynamics of proteins. Science          29. Kubelka J, Chiu TK, Davies DR, Eaton WA, Hofrichter J (2006) Sub-
    330: 341–346.                                                                              microsecond protein folding. J Mol Biol 359: 546–553.
 9. Prinz JH, Wu H, Sarich M, Keller B, Senne M, et al. (2011) Markov models of            30. Piana S, Sarkar K, Lindorff-Larsen K, Guo M, Gruebele M, et al. (2011)
    molecular kinetics: generation and validation. J Chem Phys 134: 174105.                    Computational design and experimental testing of the fastest-folding b-sheet
10. Best RB, Buchete NV, Hummer G (2008) Are current molecular dynamics force                  protein. J Mol Biol 405: 43–48.
    fields too helical? Biophys J 95: L07–09.                                              31. Lindorff-Larsen K, Piana S, Dror RO, Shaw DE (2011) How fast-folding
11. Lange OF, van der Spoel D, de Groot BL (2010) Scrutinizing molecular                       proteins fold. Science 334: 517–520.
    mechanics force fields on the submicrosecond timescale with NMR data.                  32. Jorgensen WL, Chandrasekhar J, Madura JD, Impey RW, Klein ML (1983)
    Biophys J 99: 647–655.                                                                     Comparison of simple potential functions for simulating liquid water. J Chem
12. Hornak V, Abel R, Okur A, Strockbine B, Roitberg A, et al. (2006) Comparison               Phys 79: 926–935.
    of multiple Amber force fields and development of improved protein backbone            33. Shan Y, Klepeis JL, Eastwood MP, Dror RO, Shaw DE (2005) Gaussian split
    parameters. Proteins 65: 712–725.                                                          Ewald: a fast Ewald mesh method for molecular simulation. J Chem Phys 122:
13. Best RB, Hummer G (2009) Optimized molecular dynamics force fields applied                 54101.
    to the helix-coil transition of polypeptides. J Phys Chem B 113: 9004–9015.            34. Conilescu G, Marquardt JL, Ottiger M, Bax A (1998) Validation of protein
14. Lindorff-Larsen K, Piana S, Palmo K, Maragakis P, Klepeis JL, et al. (2010)                structure from anisotropic carbonyl chemical shifts in a dilute liquid crystalline
    Improved side-chain torsion potentials for the Amber ff99SB protein force field.           phase. J Am Chem Soc 120: 6836–6837.
    Proteins 78: 1950–1958.                                                                35. Ulmer TS, Ramirez BE, Delaglio F, Bax A (2003) Evaluation of backbone
15. Piana S, Lindorff-Larsen K, Shaw DE (2011) How robust are protein folding                  proton positions and dynamics in a small protein by liquid crystal NMR
    simulations with respect to force field parameterization? Biophys J 100:                   spectroscopy. J Am Chem Soc 125: 9179–9191.
    L47–L49.                                                                               36. Vögeli B, Ying J, Grishaev A, Bax A (2007) Limits on variations in protein
16. Duan Y, Wu C, Chowdhury S, Lee MC, Xiong G, et al. (2003) A point-charge                   backbone dynamics from precise measurements of scalar couplings. J Am Chem
    force field for molecular mechanics simulations of proteins based on condensed-            Soc 129: 9377–9985.
    phase quantum mechanical calculations. J Comput Chem 24: 1999–2012.                    37. Lindorff-Larsen K, Best RB, Vendruscolo M (2005) Interpreting dynamically-
                                                                                               averaged scalar couplings in proteins. J Biomol NMR 32: 273–280.
17. Kaminski GA, Friesner RA, Tirado-Rives J, Jorgensen WL (2001) Evaluation
                                                                                           38. Wang AC, Bax A (1996) Determination of the backbone dihedral angles Q in
    and parametrization of the OPLS-AA force field for proteins via comparison
                                                                                               human ubiquitin from reparametrized empirical Karplus equations. J Am Chem
    with accurate quantum chemical calculations on peptides. J Phys Chem B 105:
                                                                                               Soc 118: 2483–2494.
    6474–6487.
                                                                                           39. Lindorff-Larsen K, Best RB, Depristo MA, Dobson CM, Vendruscolo M (2005)
18. MacKerell AD, Jr., Bashord D, Bellott M, Dunbrack RL, Jr., Evanseck JD, et al.             Simultaneous determination of protein structure and dynamics. Nature 433:
    (1998) All-atom empirical potential for molecular modeling and dynamics                    128–132.
    studies of proteins. J Phys Chem B 102: 3586–3616.                                     40. Marinari E, Parisi G (1992) Simulated tempering: a new Monte Carlo scheme.
19. MacKerell AD, Jr., Feig M, Brooks CL (2004) Extending the treatment of                     Europhys Lett 19: 451–458.
    backbone energetics in protein force fields: limitations of gas-phase quantum          41. Northrup SH, Hynes JT (1980) The stable states picture of chemical reactions. I.
    mechanics in reproducing protein conformational distributions in molecular                 Formulation for rate constants and initial conditional effects. J Chem Phys 73:
    dynamics simulations. J Comput Chem 25: 1400–1415.                                         2700–2714.
20. Markwick PR, Bouvignies G, Blackledge M (2007) Exploring multiple timescale            42. Fennell CJ, Gezelter D (2006) Is the Ewald summation still necessary? Pairwise
    motions in protein GB3 using accelerated molecular dynamics and NMR                        alternatives to the accepted standard for long-range electrostatics. J Chem Phys
    spectroscopy. J Am Chem Soc 129: 4734–4730.                                                124: 234104.

        PLoS ONE | www.plosone.org                                                     6                               February 2012 | Volume 7 | Issue 2 | e32131
