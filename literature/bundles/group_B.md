# Group B: Integrating MD with NMR, SAXS and force-field validation

7 papers.



---

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


---

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


---

# Efficient Ensemble Refinement by Reweighting

**Authors:** Jürgen Köfinger, Lukas S. Stelzl, Klaus Reuter, César Allande, Katrin Reichel, Gerhard Hummer
**Year:** 2019
**Venue:** Journal of Chemical Theory and Computation
**DOI:** 10.1021/acs.jctc.8b01231
**Source PDF URL:** https://europepmc.org/articles/PMC6727217?pdf=render
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

This is an open access article published under a Creative Commons Attribution (CC-BY)
                                                        License, which permits unrestricted use, distribution and reproduction in any medium,
                                                        provided the author and source are cited.

                                                                                                                                                        Article

                                                         Cite This: J. Chem. Theory Comput. 2019, 15, 3390−3401                             pubs.acs.org/JCTC

Eﬃcient Ensemble Reﬁnement by Reweighting
Jürgen Köﬁnger,*,† Lukas S. Stelzl,† Klaus Reuter,‡ César Allande,‡ Katrin Reichel,†
and Gerhard Hummer*,†,¶
†
 Department of Theoretical Biophysics, Max Planck Institute of Biophysics, Max-von-Laue-Straße 3, 60438 Frankfurt am Main,
 Germany
‡
 Max Planck Computing and Data Facility, Gießenbachstr. 2, 85748 Garching, Germany
¶
  Institute for Biophysics, Goethe University, 60438 Frankfurt am Main, Germany
    *
    S Supporting Information

    ABSTRACT: Ensemble reﬁnement produces structural en-
    sembles of ﬂexible and dynamic biomolecules by integrating
    experimental data and molecular simulations. Here we present
    two eﬃcient numerical methods to solve the computationally
    challenging maximum-entropy problem arising from a
    Bayesian formulation of ensemble reﬁnement. Recasting the
    resulting constrained weight optimization problem into an
    unconstrained form enables the use of gradient-based
    algorithms. In two complementary formulations that diﬀer in
    their dimensionality, we optimize either the log-weights
    directly or the generalized forces appearing in the explicit
    analytical form of the solution. We ﬁrst demonstrate the
    robustness, accuracy, and eﬃciency of the two methods using
    synthetic data. We then use NMR J-couplings to reweight an all-atom molecular dynamics simulation ensemble of the
    disordered peptide Ala-5 simulated with the AMBER99SB*-ildn-q force ﬁeld. After reweighting, we ﬁnd a consistent increase in
    the population of the polyproline-II conformations and a decrease of α-helical-like conformations. Ensemble reﬁnement makes
    it possible to infer detailed structural models for biomolecules exhibiting signiﬁcant dynamics, such as intrinsically disordered
    proteins, by combining input from experiment and simulation in a balanced manner.

1. INTRODUCTION                                                                  reﬁnement8,18 or replica simulations,15,19,20 limit the weight
To infer structures and functions of biological macromolecules,                  changes relative to the reference ensemble as is done in
we combine information from diverse experimental and                             maximum-entropy approaches14,15,21,22 or in Bayesian formula-
theoretical sources.1−3 However, in many experiments the                         tions,4,21 or limit both ensemble size and weight changes.8 See
observables reporting on biomolecular structure are averaged                     ref 15 for an in-depth discussion and further references.
over ensembles. Nuclear magnetic resonance (NMR) and                                The reference ensemble is often deﬁned in terms of a
pulsed electron paramagnetic resonance (EPR) experiments                         molecular simulation force ﬁeld, that is, a classical potential
provide ensemble-averaged high-resolution information about                      energy function for which one has some conﬁdence that it
distances (e.g., using the nuclear Overhauser eﬀect, para-                       captures essential features. The experimental data can then be
magnetic relaxation enhancement, or double electron−electron                     used directly as a bias in molecular dynamics (MD)
resonance (DEER))4−9 and angles (e.g., using J-couplings and                     simulations5,19,23−28 or a posteriori to reweight an unbiased
residual dipolar couplings).10,11 Small-angle X-ray scattering                   ensemble in a way that improves the agreement with
(SAXS) experiments provide ensemble-averaged information                         experiment.8,18,21,29,30 Biased simulations improve the coverage
about macromolecular size and shape,12 and wide-angle X-ray                      of the conﬁguration space but suﬀer from ﬁnite-size eﬀects due
scattering (WAXS) experiments report on secondary structure                      to a limited ensemble size in simulations. Reweighting requires
and fold.13 Ensemble reﬁnement promises faithful descriptions
                                                                                 good coverage but can handle much larger ensemble sizes. The
of the true ensemble of structures underlying the experimental
                                                                                 “Bayesian inference of ensembles” (BioEn) approach21 makes it
data even for highly dynamic systems.8,14−17
   The conformational diversity of the ensemble can be                           possible to combine, if needed, biased sampling and subsequent
described in terms of a set of representative reference structures.              reweighting to ensure both good coverage of the conﬁguration
The relative weights of the ensemble members are then                            space and a well-deﬁned, converged ensemble.
determined by ensemble reﬁnement against experimental data.
To regularize this inverse problem one can, for example, restrict                Received: December 7, 2018
the number of conformers as is done in minimal-ensemble                          Published: April 2, 2019

                              © 2019 American Chemical Society            3390                                                         DOI: 10.1021/acs.jctc.8b01231
                                                                                                                       J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                                                             Article

   Ensemble reﬁnement by reweighting is a computationally                       P(w|data) ∝ P(w)P(data|w)                                                     (1)
challenging optimization problem because the number of
structures in the ensemble, usually generated in simulations,                P(data|w) is the likelihood function, and w is the vector of
                                                                             weights wα. The prior is given by
                                                                                                         ij w 0 yz α
and the number of experimental data points provided by

                                                                                P(w) ∝ exp( −θSKL) = ∏ jjj α zzz
experiments can both be large. Simulations can easily create
                                                                                                          jw z
                                                                                                                 N             θw

                                                                                                     α=1 k α {
hundreds of thousands of structures. In general, we would like to
include as many structures as possible in ensemble reﬁnement,                                                                                                 (2)
not only to avoid artifacts due to the ﬁnite size of the ensemble21
but also to ensure that we pick up small but signiﬁcant                      where
subensembles. Experiments like NMR, SAXS/WAXS, and                                       N
                                                                                                     wα
DEER can provide thousands of data points. The numbers of                       SKL = ∑ wα ln
pixels or voxels in electron-microscopy projection images or 3D                        α=1
                                                                                                    wα0                                                       (3)
maps, respectively, are of even larger magnitude. More than ten                                                           31
thousand data points are thus common when integrating data                   is the Kullback−Leibler divergence. Both reﬁned weights (wα
from diﬀerent experimental sources.                                          > 0) and reference weights (w0α > 0) are normalized, ∑Nα=1wα =
   With respect to computational eﬃciency, we also have to take              ∑Nα=1w0α = 1. The parameter θ expresses the conﬁdence in the
into account that we usually want to perform multiple                        reference ensemble. Large values of θ express high conﬁdence,
reweighting runs for diﬀerent subensembles and subsets of the                and the optimal weights will be close to the reference weights.
experimental data, while at the same time varying the conﬁdence                 Instead of maximizing the posterior with respect to wα, we can
that we have in the reference ensemble. Consequently, we have                minimize the negative log-posterior given by
to be able to eﬃciently solve the optimization problem                                  N
                                                                                                     wα
underlying ensemble reﬁnement by reweighting for large                          L = θ ∑ wα ln             − ln P(data|w)
numbers of structures and data points.                                                 α=1
                                                                                                    wα0                                                       (4)
   The paper is organized as follows. In section 2, “Theory”, we
present two complementary numerical methods to calculate the                 The optimization problem is constrained by
optimal ensemble by reweighting based on the “ensemble                          0 ≤ wα for all α                                                              (5)
reﬁnement of SAXS” (EROS) method,14 which is a special case
of BioEn.21 In both methods, positivity and normalization                    and
constraints on the statistical weights are taken into account                      N
implicitly such that we can take advantage of eﬃcient gradient-                 ∑ wα = 1
based optimization algorithms. In the ﬁrst method, we solve for                 α=1                                                                           (6)
the logarithms of the N statistical weights, where N is the
number of structures. In the second method, we solve for M                   that is, the weights lie in a simplex. For uncorrelated Gaussian
generalized forces, where M is the number of experimental data               errors, σi, of the ensemble-averaged measurements, Yi, of the
points. The eﬃciency of the two methods depends on N and M.                  observables i = 1, ..., M, the likelihood is given by
For both methods, we derive analytical expressions for the                      P(data|w) ∝ exp( −χ 2 /2)
                                                                                                     ij M                        2y
                                                                                                      jj        ∑α = 1 wαyiα − Yi zzz
gradients that render gradient-based optimization algorithms

                                                                                             = expjjjj−∑                            zz
highly eﬃcient. In section 4, “Results”, we systematically
                                                                                                                                     zz
                                                                                                                 N
                                                                                                             (                          )
                                                                                                       jj i = 1                       zz
                                                                                                        j                              z
investigate the eﬃciency and accuracy of these methods using

                                                                                                        k                              {
synthetic data. For illustration, we then reﬁne fully atomistic MD                                                     2σ i
simulations of Ala-5 using J-couplings. In the Supporting                                                                                                     (7)
Information, we present a detailed derivation of the gradients               Here, yαi is the calculated value of observable i for the individual
for correlated Gaussian errors.                                              structure α. Note that the measurements Yi can stem from
                                                                             diﬀerent experimental methods, for example, from SAXS and
2. THEORY                                                                    NMR, and that σi2 = (σi,exp)2 + (σi,calc)2 is the sum of
We ﬁrst present the BioEn posterior,21 whose maximum                         uncertainties in the experiment and in the calculation of the yαi .4
determines the optimal statistical weights of the structures in                 The negative log-posterior then becomes
the ensemble. We then show that the optimal solution is unique.                                                                               2
To be able to apply gradient-based optimization methods to the                          N
                                                                                L = θ ∑ wα ln
                                                                                                     wα
                                                                                                          +∑
                                                                                                              M
                                                                                                                     (∑αN=1 wαyiα − Yi)
constrained optimization problem, we recast the posterior as a
function of log-weights and as a function of the generalized                           α=1
                                                                                                    wα0      i=1
                                                                                                                                2σi 2                         (8)
forces, as already introduced in ref 21. For both formulations, we           Note that for Gaussian errors the negative log-posterior L
calculate the respective gradients analytically, facilitating                corresponds to the EROS free energy χ2 − θS, where S = −SKL is
eﬃcient optimization. We focus here on uncorrelated Gaussian                 the negative Kullback−Leibler divergence.14 The BioEn and
errors. Supporting Information contains a detailed derivation of             EROS formulations diﬀer by a factor 1/2 scaling χ2, which is
the gradients for correlated Gaussian errors, which includes the             equivalent to a trivial rescaling of θ.
expressions for uncorrelated Gaussians in the main text as                     To solve this optimization problem eﬃciently, we ﬁrst show
special cases.                                                               that the negative log-posterior is convex such that there is a
   2.1. Background. In the BioEn method,21 which is a

                                                                                          ij w        yz
                                                                             unique solution. The gradient of eq 8 is given by
generalization of the EROS method,14 we determine the

                                                                                    = θ jjjln α0 + 1zzz + ∑ i i 2
                                                                                           j w         z
optimum of the posterior probability as a function of the                       ∂L
                                                                                                          M
                                                                                                             y α (⟨y ⟩ − Yi )

                                                                                           k           { i=1
statistical weights, wα, where α is the index of the N ensemble
                                                                                ∂wα           α                     σi                                        (9)
members (α = 1, ..., N) given the experimental data,
                                                                      3391                                                            DOI: 10.1021/acs.jctc.8b01231
                                                                                                                      J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                                                                 Article

where angular brackets indicate the average over the reweighted                corresponding to gα = ln(w0α/w0N) = Gα − GN. In a practical
ensemble, that is, ⟨yi⟩ = ∑Nα=1wαyαi . The Hessian is given by                 implementation, a procedure to evaluate L and its gradients,
                                       M     α γ                               called with gμ (μ = 1, ..., N − 1) as arguments, would do the
          ∂ 2L    θ          y y                                               following:
   hαγ ≡         = δαγ + ∑ i 2i
         ∂wα ∂wγ  wα     i=1
                              σi                                (10)             (1) deﬁne gN = 0,
                                                                                 (2) evaluate wα according to eq 13 for α = 1, ..., N,
where δαγ = 1 if α = γ and δαγ = 0 otherwise. By casting the
                                                                                 (3) evaluate L according to eq 8 or eq 17 below, and
Hessian in this form, as a sum of a positive deﬁnite diagonal
matrix and of dyadic products of vectors, it is straightforward to               (4) evaluate the gradient according to eq 14.
show that the quadratic form xThx is positive deﬁnite,                            Both L and its gradient can be evaluated eﬃciently using
                                                                               vector-matrix operations. Given the gα, we deﬁne vα = egα, s =
                     xα 2
                           NM  ∑α = 1 xαyiα  ( N        ) >0                   ∑Nα=1vα = ∑Nα=1egα, s0 = ∑Nα=1eGα, and wα = vα/s (all being
   ∑ xαhαγ xγ = θ ∑       +∑                                                   eﬃciently evaluated in vector form). The averages can be
   α ,γ
                      w
                  α=1 α    i=1
                                   σi2                          (11)           calculated as vector dot products:
for |x|
          = ∑Nα=1xα2 = 1. The Hessian is thus positive deﬁnite                      ⟨g ⟩ = g ·w                                                                 (15)
everywhere, and the optimal solution is unique.
   A possible concern is that the optimal solution is on the                        ⟨G⟩ = G·w                                                                   (16)
boundary of the simplex, that is, wα = 0 for some α, because the
                                                                                            i                s y 1
                                                                               We then have

                                                                                    L = θ jjj⟨g ⟩ − ⟨G⟩ + ln 0 zzz + | ̃yw − Ỹ |2
Kullback−Leibler divergence is bounded. One might then not

                                                                                            k                 s{ 2
be able to use gradient-based methods without modiﬁcation.
However, because of the nonanalytical character of the                                                                                                          (17)
logarithm, the partial derivatives of L with respect to every wα
                                                                               where ỹ is an M × N matrix with components ỹiα = yαi /σi, and Ỹ is
diverge to negative and positive inﬁnity at wα = 0 and 1,
                                                                               a vector with M components Yi/σi that can be precalculated.
respectively, and are monotonic in between. Therefore, the
                                                                                  To evaluate the gradient, the averages in eq 14 can be
optimal solution is contained within the simplex, not on its
                                                                               evaluated as dot products. The ﬁrst part on the right-hand side of
surface.
                                                                               eq 14 can then be evaluated as an in-place vector operation. The
   Another concern is that to ﬁnd the unique optimal solution,
                                                                               second part can also be evaluated by a combination of matrix-
we have to take into account the constraints acting on the
                                                                               vector multiplication (for ⟨yi⟩), vector dot products (for the sum
weights given by eqs 5 and 6. One could optimize the log-
                                                                               over i), and in-place vector operations (for the diﬀerent μ).
posterior given by eq 8 using algorithms for constrained
                                                                                  2.3. Optimization via Generalized Forces. We showed
optimization like LBFGS-B that take advantage of the
                                                                               previously21 that the weights at the maximum of the log-
gradient.32 To avoid the performance penalty associated with
                                                                               posterior can be expressed in terms of generalized forces
treating constraints explicitly, we instead recast the optimization
problem into an unconstrained form.                                                          ⟨yk ⟩ − Yk
   2.2. Optimization via Log-Weights. To optimize the log-                          Fk = −
                                                                                                  θσk 2                                                         (18)
posterior given by eq 8 under the constraints given by eqs 5 and
6 and to determine the optimal values of the weights wα > 0 by                 as
gradient-based minimization, we introduce log-weights
   gα = ln wα                                                   (12)                wα =
                                                                                                          (   M
                                                                                                                   )
                                                                                              wα0 exp ∑ j = 1 yjα Fj
                                                                                            N              M
which are only determined up to an additive constant. This                                 ∑γ = 1 wγ0 exp ∑i = 1 yiγ Fi
                                                                                                              (           )                                     (19)
constant cancels in the normalization of wα. We can then write
                                                                               Note that these generalized forces correspond to Lagrange
              e gα                                                             multipliers in closely related maximum entropy (MaxEnt)
   wα =      N                                                                 approaches to ensemble reﬁnement.25,30,33−35 See ref 21 and the
           ∑γ= 1 e gγ                                           (13)           Discussion (section 5) below concerning the relation between
Without loss of generality, because all wα > 0, we can set gN = 0.             MaxEnt and BioEn methods. In many practical cases, we have
For the gradient of L with respect to the remaining gμ (μ = 1, ...,            fewer observables than weights, M ≪ N. In such cases, one may
N − 1), we have                                                                want to take advantage of eq 19 and minimize L with respect to
                                                                               the M generalized forces Fk instead of the N weights. By applying
   ∂L                                                                          the chain rule, we obtain the gradient with respect to the

                                                                                              Ä                                            ÉÑ
       = wμθ(gμ − ⟨g ⟩ − Gμ + ⟨G⟩)

                                                                                           N ÅÅÅ i w                   yiα (⟨yi ⟩ − Yi ) ÑÑÑ
                                                                               generalized forces as
                                                                                                             yz
   ∂gμ

                                                                                               ÅÅ jj          z                             ÑÑ
                                                                                       = ∑ ÅÅθ jjln 0 + 1zz + ∑                              ÑÑ
                                                                                                ÅÅ j w        z
                                                                                                                   M
                     M
                           (⟨yi ⟩ − Yi )(yiμ − ⟨yi ⟩)
                                                                                                 Å k                                          ÑÖÑ
                                                                                   ∂L
                                                                                          α=1 Ç               { i=1
                                                                                                      α
            + wμ ∑                                                                                                                2
                     i=1              σi 2                      (14)               ∂Fk                α                       σ i

where Gα = ln w0α and angular brackets indicate the average over                             × wα(ykα − ⟨yk ⟩)                                                  (20)
the reweighted ensemble, for example, ⟨g⟩ = ∑Nα=1wαgα. We
simpliﬁed the expressions by taking advantage of the normal-                   In a numerical minimization of L with respect to the M
ization condition.                                                             generalized forces, one would thus at each iteration step do the
   Importantly, we need to minimize L only with respect to the N               following:
− 1 variables gμ (μ = 1, ..., N − 1). A starting point of a gradient-            (1) calculate the current weights wα from the forces according
based minimization of L could be the normalized prior w0α,                           to eq 19;
                                                                        3392                                                              DOI: 10.1021/acs.jctc.8b01231
                                                                                                                          J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                                                      Article

 (2) evaluate L according to eq 8 or eq 17;                                  performing parallel reductions can lead to numerically slightly
 (3) evaluate the gradient according to eq 20.                               diﬀerent results. The reason is that parallel reductions introduce
                                                                             nondeterministic summation orders such that round-oﬀ errors
   Equations 8, 19, and 20 can be evaluated eﬃciently by using               vary between runs. Therefore, we also provide parallelized C
vector-matrix methods in NumPy etc., using precalculated                     kernels where we eliminated any nonreproducibility eﬀects.
vectors of intermediates. However, for large M × N, care should                 3.2. Simulation Details. Ala-5 was simulated at pH 2, using
be taken to minimize the memory requirements by avoiding M ×                 the AMBER99SB*-ildn-q force ﬁeld matching the experimental
N matrices other than yαi .                                                  solution conditions.41 To describe the protonated C-terminus at
   2.4. Optimization Strategies. Small θ values are more                     a low pH, we took partial charges from the protonated aspartate
challenging than large θ values because the optimal weights will             side chain. Excess charges were distributed across the C-terminal
deviate more from the reference weights. In practice, we usually             residue. The simulations of Ala-5 were run for 1 μs using
do not know how to set θ a priori. In such cases, we recommend               simulation options previously described.42 J-couplings were
to perform an L-curve analysis.36 In an L-curve or elbow plot, we            calculated as in previous work43 for the 50000 structures used for
plot χ2 or the reduced chi-square value, χ2/M, as a function of the          the BioEn reweighting. Chemical shifts were calculated with
relative entropy SKL for the optimal solutions at diﬀerent θ                 SPARTA+44 using MDTraj.45 MD simulations were analyzed
values. The χ2 values will decrease with increasing relative
                                                                             using MDAnalysis.46,47
entropy SKL, and we can choose a θ value corresponding to the
elbow in this plot.
   Finding optimal solutions for a series of θ values also has the           4. RESULTS
advantage that we can use the more rapidly converging optimal                We ﬁrst investigate the stability, accuracy, and eﬃciency of the
solutions at large θ values as starting points for optimizations at          optimization methods using log-weights and generalized forces
smaller θ values.                                                            by applying them to synthetic data. We then reﬁne molecular
                                                                             dynamics simulation ensembles for Ala-5 using J-couplings.
3. METHODS                                                                       4.1. Accuracy and Performance of Optimization
   3.1. Implementation. With the analytical expressions for                  Methods. We investigate how accuracy and eﬃciency of the
gradients in the log-weights and forces formulations derived                 log-weights and forces methods depend on the size of the
above, we can take advantage of highly optimized gradient-based              ensemble N and the number of data points M using synthetic
optimization methods. The BioEn optimize package, which can                  data. To generate a data set, we drew M experimental values Yi
be downloaded from https://github.com/bio-phys/BioEn,                        from a normal distribution, that is, Yi ≈ 5(0, 1). We generated
provides Python and C implementations of the log-posterior                   calculated observables yiα by drawing Gaussian numbers from
and its gradient for both methods and a selection of diﬀerent                N(Yi + 1, 2), where the oﬀset of 1 mimics systematic deviations
gradient-based optimizers and implementations.                               due to force ﬁeld inaccuracies. We set the experimental error for
   The reference implementation is based on Python and on the                all data points to σ = 0.5. For each combination of ﬁve M-values,
packages NumPy and SciPy in particular. The log-posterior and                M = 102, 316 (∼102.5), 103, 3162 (∼103.5), and 104, and nine N-
its derivatives are written in NumPy notation, and the BFGS                  values, N = 102, 316 (∼102.5), 103, 3162 (∼103.5), 104, 31623
minimizer from SciPy is used to compute the minimum.37                       (∼104.5), 105, 316228 (∼105.5), and 106, we generated randomly
Thanks to the fact that NumPy is typically linked to high-                   four sets, giving us 5 × 9 × 4 = 180 data sets in total.
performance mathematical libraries such as MKL, the Python-                     To fully deﬁne the optimization problem, we chose uniform
based implementation is capable of exploiting vectorization and              reference weights w0α = 1/N and a value for the conﬁdence
multithreading on state-of-the-art hardware. On the other hand,              parameter θ = 0.01. The latter expresses little conﬁdence in our
there is some overhead associated with NumPy related to the use
                                                                             reference ensemble, such that the optimal weights will be
of temporary buﬀers during expression evaluation.
                                                                             signiﬁcantly diﬀerent from the reference weights, rendering this
   To improve the performance, we provide C-based imple-
                                                                             optimization more challenging than for large values of θ. We
mentations of the log-posterior functions and their derivatives,
largely avoiding temporary buﬀers by using explicit loops to                 minimize the negative log-posterior L given by eq 8 for each data
implement the expressions. OpenMP directives are used to                     set using the log-weights and forces methods.
explicitly leverage vectorization and thread parallelization. The               The eﬃciency and accuracy of gradient-based optimization
Python interfaces are written in Cython. While these kernels are             methods depends strongly on their detailed parametrization.
signiﬁcantly faster than the NumPy-based code, there is still                Here, we present results for the limited-memory BFGS
some overhead when the BFGS minimizer from SciPy is used                     (LBFGS) algorithm.39,40 Due to its memory eﬃciency, we can
because it is written in plain Python.                                       reﬁne larger ensembles using more data points compared to
   To eliminate the bottleneck caused by the SciPy minimizer,                other algorithms like BFGS or conjugate gradients. Speciﬁcally,
we have implemented a Cython-based interface to the                          we explored the eﬀect of the choice of the line search algorithm
multidimensional minimizers of the GNU Scientiﬁc Library                     and the convergence criteria on the convergence behavior. We
(GSL), that is, conjugate gradient, BFGS, and steepest descent               found that using the backtracking line search algorithm applying
minimizers.38 In doing so, the minimization is performed                     the Wolfe condition48,49 in connection with a convergence
completely in the C layer without any overhead from the Python               criterion acting on the relative diﬀerence of the log-posterior
layer. Additionally, the C implementation of Jorge Nocedal’s                 with respect to a previous value (relative diﬀerence 10 iterations
Fortran implementation of the limited-memory BFGS algo-                      before the current one <10−6) strikes the best balance between
rithm39,40 by Naoaki Okazaki (https://github.com/chokkan/                    accuracy, eﬃciency, and robustness. We used these parameters
liblbfgs) can be used.                                                       to obtain the results we show in the following. From all optimal
   A test suite is provided to check the implementations against             solutions found in our exploration of the parameter space of the
each other. During code development work, we noticed that                    LBFGS algorithm, we chose for each data set the solution with
                                                                      3393                                                     DOI: 10.1021/acs.jctc.8b01231
                                                                                                               J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                                                              Article

the lowest negative log-posterior to compare with. We call these
solutions the most optimal solutions in the following.
   To characterize the optimization problem for the synthetic
data sets considered here, we plot the optimal reduced χ2 value
as a function of the optimal relative entropies, SKL, in Figure 1.

                                                                                    Figure 2. Cumulative distribution functions of Pearson’s correlation
                                                                                    coeﬃcient r given by eq 21 of the optimized weights obtained with the
                                                                                    log-weights and forces methods with respect to the most optimal
                                                                                    weights found in optimizations with diﬀerent parameters for the
                                                                                    LBFGS algorithm. The lowest r values for particular (M, N)
                                                                                    combinations are shown in Figure 3.

Figure 1. Scatter plot of the optimal reduced χ2 and the optimal relative           methods to the most optimal negative log-posterior, L(opt),
entropy, SKL, obtained with the log-weights method (circles) and the                found. An average over all samples for given M and N indicates
forces method (crosses) for 5 × 9 = 45 values of (M, N) and θ = 0.01.               that the forces method performs well (see Figure 3, top left).
For each value of (M, N), we show results for four synthetic data sets              Only when M ≈ N, we ﬁnd occasional small deviations from the
drawn at random as speciﬁed in the text. Crosses on top of circles                  most optimal values. The log-weights method performs
indicate excellent agreement of the two methods. Optimal values for the
                                                                                    excellently for M ≈ N, but not as well where N ≫ M. This
four data sets for a speciﬁc (M, N) can be visually identiﬁed as clusters,
especially for large N.                                                             behavior is also reﬂected in the minimum value of the correlation
                                                                                    coeﬃcients over the four random samples at given M and N (see
                                                                                    Figure 3, bottom).
The larger the value of the relative entropy SKL, the more the
                                                                                       For the chosen convergence criterion and line search
optimal weights diﬀer from the reference weights and the more
                                                                                    algorithm, the log-weights method is computationally more
challenging is the optimization problem. In general, we found
                                                                                    eﬃcient than the forces method (Figure 4). We performed
that the optimal values for the log-weights and forces methods
                                                                                    benchmark calculations on a single node with two E5-2680-v3
agree well with each other. Due to the nature of the synthetic
                                                                                    CPUs, 12 cores each, and 64 GB RAM using OpenMP. For the
data sets, results for individual (M, N) can be visually identiﬁed
                                                                                    largest system considered, (N, M) = (106, 105) we used a
as clusters, especially for large ensemble sizes N. Note that for
                                                                                    machine with identical CPUs but 128 GB RAM. For all values of
the data sets considered here, the clusters for large N pose more
                                                                                    the number of data points M, the run time as a function of the
challenging optimization problems because the optimal weights
                                                                                    ensemble size N shows a step where the matrix of calculated
are further from the initial weights.
                                                                                    observables y has reached a size of ∼107 elements, that is, at M ×
  The optimal weights obtained with the two methods are
                                                                                    N = 102 × 105, 103 × 104, and 104 × 103. At this size, the matrix y
highly correlated and correlate excellently with the most optimal
                                                                                    no longer ﬁts into the CPU cache. However, for larger sizes the
weights found in our exploration of parameter space of the
                                                                                    run time again depends linearly on the ensemble size. In Table 1,
LBFGS algorithm. We quantify these correlations using
                                                                                    we summarize the average run times for the largest ensemble size
Pearson’s correlation coeﬃcient r,50 which for two sets of
                                                                                    considered here (N = 106). For M = 100 the log-weights
weights w(1)         (2)
           α and wα is given by                                                     methods is ∼20 times faster than the forces method (∼12 s
              N                       N
           ∑α = 1 (wα(1) − N −1) ∑γ = 1 (wγ(2) − N −1)                              versus ∼4 min on a single node; see Table 1).
   r=                                                                                  In conclusion, for the chosen convergence criterion and line
              N                        N
           ∑α = 1 (wα(1) − N −1)2 ∑γ = 1 (wγ(2) − N −1)2             (21)
                                                                                    search algorithm, optimization using the LBFGS algorithm is
                                                                                    stable, eﬃcient, and accurate for both the forces method and the
We ﬁnd that the cumulative distribution functions of the                            log-weights method. In cases where the ensemble size is much
correlation coeﬃcient for the forces and log-weights methods                        larger than the number of data points, N ≫ M, the forces method
with respect to the most optimal weights found are strongly                         is more accurate but also less eﬃcient. In cases where N ≈ M, the
peaked at r = 1 (see Figure 2). For the forces method, 91% of all                   log-weights method is both more eﬃcient and more accurate
samples have a correlation coeﬃcient of r > 0.99. For the log-                      than the forces method. The BioEn optimization library has
weights method, the peak at r = 1 is even narrower as 95% of all                    been written to make it easy and straightforward not only to
samples have a correlation coeﬃcient of r > 0.99. However, the                      choose from a variety of optimization algorithms, but also to
log-weights solutions of fewer than 10 out of 180 samples have a                    ﬁne-tune the chosen optimization algorithms to further improve
correlation coeﬃcient of r < 0.9 and thus show poorer                               accuracy or eﬃciency or both.
correlation with the most optimal weights.                                             4.2. Reﬁnement of Ala-5 Using J-Couplings. As a
  A more detailed analysis of the accuracy shows that the log-                      realistic example for a biomolecular system, we have conducted
weights method performs not as well in cases where the                              BioEn reﬁnement of the disordered peptide penta-alanine (Ala-
ensemble size is much larger than the number of data points, N                      5) against NMR J-couplings.41 The Ala-5 model system is simple
≫ M. To quantify the accuracy, we calculate the diﬀerence in                        enough that well converged simulations can be obtained
log-posterior, ΔL, obtained with the forces and log-weights                         straightforwardly. Nevertheless, it displays much of the
                                                                             3394                                                      DOI: 10.1021/acs.jctc.8b01231
                                                                                                                       J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                                                            Article

Figure 3. Optimality of solutions as a function of the ensemble size N (horizontal axis) and number of experimental data points M (vertical axis) with
respect to the most optimal solutions found with diﬀerent convergence criteria and line search algorithms. (top) Diﬀerence of negative log-posterior
values to optimum for the forces method (left) and the log-weights method (right). (bottom) Minimum value of the Pearson correlation coeﬃcient r
over the four samples at a given (M, N) with respect to the optimal weights for the forces method (left) and log-weights method (right).

                                                                                Table 1. Average Single-Node Run Time in Minutes and
                                                                                Minimum and Mean Value of the Pearson’s Correlation
                                                                                Coeﬃcient, r, Calculated for the Optimized and Most
                                                                                Optimal Weights for the Largest Ensemble Size, N = 106 and
                                                                                M = 100, 1000, and 10000 Data Points
                                                                                                run time [min]                        min./avg. r
                                                                                   M        log-weights     forces         log-weights               forces
                                                                                  102           0.2            4            0.63/0.78             1.00/1.00
                                                                                  103           1.5            7            0.98/0.99             1.00/1.00
                                                                                  104          48            140            1.00/1.00             0.98/0.99

Figure 4. Run times for the log-weights (circles) and forces (crosses)
                                                                                J-couplings.41 J-couplings were calculated from the MD
optimization methods as a function of ensemble size N for diﬀerent
numbers of data points M = 100, 1000, and 10000 (in green, orange,              trajectory using the Karplus parameters from the original
and blue, respectively). Run times have been averaged (bold symbols)            publication41 and two sets of Karplus parameters determined
over four diﬀerent synthetic data sets each (light symbols).                    from DFT calculations (DFT1 and DFT2).52 The DFT2
                                                                                parameters were used to deﬁne the AMBER99SB*-ildn-q force
                                                                                ﬁeld, and hence we initially focused on this set of Karplus
complexity encountered in MD simulations of intrinsically                       parameters.
disordered proteins (IDPs) with a myriad of shallow free energy                    Even without reﬁnement, the MD simulation gives very good
minima. Hence, details of the force ﬁeld matter greatly for such                agreement with the experimental J-couplings with χ2/M ≈ 1.0
systems, and simulations do not provide results at a level                      (1.1 and 0.8 for original and DFT1 Karplus parameters,
routinely achieved for well-ordered proteins. NMR observables                   respectively) using the error model of ref 43. For uncorrelated
such as J-couplings, which report on dihedral angle equilibria,                 errors, χ 2/M < 1 would signify agreement within the
provide accurate information on disordered systems.51                           experimental uncertainty on average. However, a closer
  We assessed the quality of a 1 μs simulation of Ala-5 with the                inspection of measured and calculated J-couplings shows that
AMBER99SB*-ildn-q force ﬁeld by comparison to experimental                      there are systematic deviations. For the 3JHNHα and 3JHαC′
                                                                         3395                                                        DOI: 10.1021/acs.jctc.8b01231
                                                                                                                     J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                                                           Article

Figure 5. Comparison of J-couplings measured by NMR41 (black squares) and calculated from MD simulation with the AMBER99SB*-ildn-q force
ﬁeld (red squares) and the optimal BioEn ensemble (blue circles, θ = 6.65). The DFT2 set of Karplus parameters was used to calculate J-couplings.

couplings, which report on the ϕ-dihedral angle equilibrium, the
simulations predict larger couplings than in experiments (Figure
5A,C). In addition, for the 2JNCα couplings, which are sensitive to
the ψ-dihedral angle equilibrium, couplings calculated from
simulations are all smaller than the experimental couplings
(Figure 5G).
   With BioEn reweighting, we reﬁned the weights of 50000
structures from the 1 μs simulation of Ala-5 against 28
experimental J-couplings. Optimizing the eﬀective log-posterior
at diﬀerent values of the conﬁdence parameter θ (Figure 6A), we
see the expected drop in χ2 as θ is decreased. At small values of θ,
we ﬁnd only marginal improvements in χ2, but start to move                    Figure 6. BioEn optimization for Ala-5. (A) L-curve analysis to
                                                                              determine the optimal value of the conﬁdence parameter θ by plotting
away from the reference weights as indicated by a substantial                 χ2 as a function of SKL for diﬀerent values of θ. (B) Cumulative weight of
increase in the relative entropy. At θ = 6.65, we ﬁnd a good                  rank-ordered wα for the uniformly distributed reference weights w0α
compromise between reducing χ2 and staying close to the                       (red) and for optimized weights (blue) at θ = 6.65 with SKL ≈ 0.5.
reference weights. The agreement with experiment increased or
stayed the same for all J-couplings (Figure S6) except for 3JHNC′
and 3JHNCβ of residue 2 for which the already very good                       ments are consistent with each other. In particular, for the
agreement got somewhat worse (Supporting Information). The                     JHNHα (Figure 5A) and 3JHαC′ (Figure 5C) couplings, which
overall improvement demonstrates that the diﬀerent experi-                    report on the ϕ dihedral angle, and the 2JNCα couplings (Figure
                                                                       3396                                                         DOI: 10.1021/acs.jctc.8b01231
                                                                                                                    J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                                                      Article

Figure 7. Ala-5 Ramachandran maps. (A) Free energy surface G(ϕ,ψ) = −ln p(ϕ, ψ) from MD simulation with the AMBER99SB*-ildn-q force ﬁeld
averaged over the central residues 2−4. (B) Ramachandran plot for Ala residues outside of regular secondary structure from the PDB.11 (C) Free
energy surface for the optimal BioEn ensemble with DFT2 Karplus parameters. (D) Free energy diﬀerences between initial ensemble and the optimal
BioEn ensemble.

5G), reporting on the ψ dihedral angles, systematic deviations               favorable at the expense of α-helical like conformations (Figure
from the experiment disappear with the reﬁnement. The                        S5). For the original Karplus parameters, we also ﬁnd a
changes in the weights are associated with an entropy SKL ≈                  reduction in β-strand like conformations and an even larger ppII
0.5 (Figure 6A). The weights of most structures were changed                 population than for DFT1 and DFT2. While the choice of
only slightly by the reweighting. In the optimal BioEn ensemble,             Karplus parameter model somewhat aﬀects the optimal
the most important 20% of the structures constitute ∼60% of the              ensemble, the overall conclusions are robust.
reﬁned ensemble (Figure 6B). The weights of these structures                    The ensemble reﬁnement improves and preserves the
approximately double with the reﬁnement. After reﬁnement                     agreement with experimental data not included in the
∼20% of the structures contribute negligibly to the ensemble,                reﬁnement, Protein Data Bank (PDB) statistics, and the
with weights close to zero. As expected, the optimal weights                 experimental chemical shifts. The distribution of ϕ and ψ angles
from the log-weights or generalized forces methods were highly               for Ala residues outside of regular secondary structure from the
correlated (Figure S1), conﬁrming the equivalence of the two                 PDB,11 while clearly not reﬂective of the structure of a speciﬁc
methods to solve the BioEn reweighting problem. Using the                    disordered protein in solution, provides a measure of conforma-
LBFGS algorithm, the run times of the forces and log-weights                 tional preferences of disordered proteins. Indeed, the BioEn
optimizations for all θ values are comparable, at 42 and 33 s,               reweighting of the α and ppII conformations leads to a
respectively, on a standard workstation.
                                                                             Ramachandran plot agreeing more closely with the PDB
   The polyproline-II (ppII) conformation at ϕ ≈ −60° and ψ ≈
                                                                             statistics, with a large reduction in the population of left-handed
150° becomes more populated in the optimal ensemble (Figure
7D), irrespective of the choice of Karplus parameters. The shift             α-helical conformations as is apparent from Figure 7D, Figure
to ppII is in agreement with the original analysis of the J-                 S3, and Figure S4. No information from PDB statistics was
couplings for Ala-5,41 where it was concluded that the ppII state            included in the reﬁnement and the improved agreement with an
dominates the conformational equilibrium, and with infrared                  independent data set is encouraging. As a second independent
(IR) spectroscopy.53 The same conclusion was drawn from                      data set, which was not included in the BioEn reﬁnement, we
reﬁning Ala-3 MD simulation ensembles against 2D-IR data.54                  compare the experimental chemical shifts for Ala-541 to the
The 3JCC′ coupling for residue 2 has been highlighted as                     initial ensemble and the optimal ensemble. The chemical shifts
potentially spurious by Best et al.55 because the reported                   predicted by SPARTA+44 are within the prediction error before
coupling is atypical for a polyalanine. Leaving out this observable          and after ensemble reﬁnement (Figure S7). The comparison
from the BioEn reﬁnement results in an essentially unchanged                 shows the following for Ala-5: (1) Chemical shifts cannot be
reﬁned ensemble (Figure S5). Using alternative Karplus                       used to reﬁne the ensemble because the initial ensemble already
parameters to calculate the J-couplings (Figure S2) also leads               agrees with experiment within the large prediction error. (2)
to a shift to the ppII state (original and DFT1 in Figures S3 and            Ensemble reﬁnement either improves or leaves unchanged
S4, respectively), and in all cases, the ppII state becomes more             predictions for observables not included in the reﬁnement.
                                                                      3397                                                     DOI: 10.1021/acs.jctc.8b01231
                                                                                                               J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                                                         Article

   The BioEn reweighting leads to a better description of the
disordered peptide Ala-5 and highlights the trade-oﬀs inherent
even in the most advanced force ﬁelds. Current ﬁxed-charge
protein force ﬁelds underestimate the cooperativity of the helix−
coil equilibrium56 because force ﬁelds describe the formation
hydrogen bonds relatively poorly. To compensate for the lack of
cooperativity of helix formation, the formation of α-helices was
favored by the “star” correction to the ψ torsion potential with
the aim to deﬁne a force ﬁeld balanced between helix and coil
conformations. The slight rebalancing of the AMBER force
ﬁeld56 enabled the folding of both α-helical and β-sheet
proteins.57 Here BioEn reweighting compensates for an adverse
eﬀect of the overall very successful rebalancing of the AMBER
force ﬁeld, that is, the overestimation of the helix content for
short peptides such as Ala-5. BioEn reweighting can thus serve as
a system speciﬁc correction to the force ﬁeld, which is a
promising avenue to tackle systems such as intrinsically
disordered proteins where the details of the force ﬁeld are
critical.58,59

5. DISCUSSION
We have presented two separate approaches to optimizing the
BioEn posterior, the log-weights and generalized forces
methods. Both approaches have in common that the resulting
optimization problem is unconstrained, that is, both log-weights
and forces can take on any real value in principle (with positivity          Figure 8. MaxEnt approaches to ensemble reﬁnement as special cases
of the weights enforced by the Kullback−Leibler divergence).                 of BioEn. For BioEn optimal ensembles, we plot the reduced χ2 and the
For such unconstrained optimization problems, eﬃcient                        relative entropy SKL parametrized by the conﬁdence parameter θ (blue).
gradient-based optimization methods exist. We take advantage                 The solution of Gull−Daniell-type60 methods is given by the
of these by deriving analytical expressions for the gradients in             intersection of this curve with χ2 = 1 (orange), of traditional MaxEnt
                                                                             methods20,22,61,62 by the intersection with χ2 = 0 (green), and of the
both formulations.                                                           method of Cesari et al.25,30 by the BioEn solution for θ = 1 (red). For a
   The main diﬀerences between the log-weights and the forces                simple model (M × N = 1 × 2, y = (0,1), σ = 0.14), we vary the
methods concerns the dimensionality of the underlying                        experimental value Y, top to bottom. (A) All methods provide a solution
optimization problem. Usually, higher-dimensional problems                   for an experimental value Y = 0.09 within the range of calculated
are harder to optimize. We can either optimize for N − 1 log-                observables. (B) Traditional MaxEnt methods fail to give a solution for
weights, where N is the ensemble size, or for M generalized                  Y values outside this range (Y = 1.08). (C) Both traditional MaxEnt and
forces, where M is the number of data points. We have shown                  Gull−Daniell-type methods fail to give a solution where a reduced χ2 ≤
here for the memory eﬃcient LBFGS optimization algo-                         1 cannot be realized by reweighting (Y = 1.16). The vertical gray lines
rithm39,40 and synthetic data sets that optima corresponding                 indicate the maximum value SKL = ln(2) for a two-state system.
to identical weights are reliably and eﬃciently found with both
formulations.                                                                solution exists, then this condition determines a particular value
   Importantly, the BioEn method contains solutions of                       of θ.
traditional MaxEnt approaches to ensemble reﬁnement as                          Reweighting relies on good coverage of the conformational
special cases (see Figure 8). These methods either treat                     space such that the true ensemble underlying the experimental
experimental observables as strict constraints20,22,61,62 or                 data is a subensemble of the simulation ensemble.63 In coarse-
consider errors explicitly.25,30,60 If solutions for these methods           grained simulations, sampling is eﬃcient and the free-energy
exist then they correspond to diﬀerent choices of the value of the           landscapes are smooth such that good coverage can be achieved.
conﬁdence parameter θ: The BioEn optimal ensemble                            In atomistic simulations, where sampling is more expensive and
approaches the traditional MaxEnt solution with strict                       the free energy landscape is rougher, we often have to apply
constraints forcing deviations from the experimental values to               enhanced sampling methods to obtain good coverage.
vanish, that is, χ2 = 0, in the limit of θ → 0+. Note that if an             Independent of the details of the enhanced sampling method
experimental observable does not fall within the range of the                and with or without steering by experimental values, one can use
calculated observables, such a strict constraint cannot be fulﬁlled          binless WHAM42,64 or MBAR65 to obtain the reference weights
and the MaxEnt method in principle fails to give a solution                  of the unbiased ensemble, which serve as input for ensemble
(though, in practice, methods such as replica sampling20 will still          reﬁnement by reweighting.21
give a result). In these cases where the MaxEnt solution does not               Here, we demonstrated that even without applying enhanced
exist, the limit of θ → 0+ corresponds to the least-χ2 solution              sampling methods, reﬁnement of fully atomistic trajectories of
under the constraints that all weights are positive and                      penta-alanine using J-couplings alleviates deﬁciencies in the
normalized. As for MaxEnt approaches that account for                        force ﬁeld and leads to better agreement not only with the NMR
Gaussian errors, the method of Cesari et al. gives the same                  data but also with expectations from experimental structures for
solution as BioEn for θ = 1.25,30 The MaxEnt method of Gull and              proteins. These results indicate that ensemble reﬁnement via
Daniell60 includes errors but uses a strict constraint by                    reweighting is a promising route for highly ﬂexible systems such
demanding that the reduced χ2 is equal to one. If such a                     as nucleic acids30 and intrinsically disordered proteins.58,59 For
                                                                      3398                                                        DOI: 10.1021/acs.jctc.8b01231
                                                                                                                  J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                                                        Article

such systems, the number of accessible states can be enormous               github.com/bio-phys/BioEn at no cost under the GPLv3
and consequently even small inaccuracies in the simulation force            license.
ﬁelds can lead to a poor representation of the experimental
ensemble.
   Importantly, ensembles do not have to be generated by
                                                                            ■
                                                                            *
                                                                                 ASSOCIATED CONTENT
                                                                            S Supporting Information
simulations to be amenable to ensemble reﬁnement via                        The Supporting Information is available free of charge on the
reweighting. For example, in the analysis of EPR experiments                ACS Publications website at DOI: 10.1021/acs.jctc.8b01231.
like DEER, libraries of the rotameric states of spin labels are                  Detailed derivation of the gradients for correlated
used. For a speciﬁc residue, one selects from this library all                   Gaussian errors, which includes the expressions for
rotameric states that do not have steric clashes with the protein                uncorrelated Gaussian in the main text as special cases,
structure. However, the interactions of the spin label with its                  comparison of the Ala-5 ensemble reﬁnement using
surroundings can make some rotameric states in this ensemble                     generalized forces and log-weights, quantiﬁcation of the
more preferable than others. To account for this uncertainty,                    eﬀects of the choice of Karplus parameters on the optimal
one can perform a BioEn reﬁnement using the DEER data and                        Ala-5 ensemble, discussion of the information content of
the ensemble of rotameric states. This procedure has been used                   individual J-couplings, and comparison of calculated
recently to resolve angstrom-scale protein domain move-                          chemical shifts to experiment (PDF)

                                                                            ■
ments.66 BioEn-type ensemble reﬁnement has also been applied
successfully to IDP structural modeling using NMR data as input
                                                                                 AUTHOR INFORMATION
and coil libraries as reference.10,11
   To integrate experimental results, we often have to take                 Corresponding Authors
nuisance parameters into account. For reﬁning against SAXS                  *E-mail: juergen.koeﬁnger@biophys.mpg.de.
intensities, we have to consider an unknown scaling parameter               *E-mail: gerhard.hummer@biophys.mpg.de.
and often use an additive constant to account for inelastic                 ORCID
scattering and, to a ﬁrst approximation, for diﬀerences in the              Jürgen Köﬁnger: 0000-0001-8367-1077
contrast. Using DEER data, we have to determine the                         Lukas S. Stelzl: 0000-0002-5348-0277
modulation depths. We can include such nuisance parameters                  Gerhard Hummer: 0000-0001-7768-746X
in the optimization either directly (by minimizing L                        Funding
simultaneously with respect to the weights and nuisance                     We acknowledge ﬁnancial support from the German Research
parameters) or iteratively. In the iterative approach, we perform           Foundation (CRC902: Molecular Principles of RNA Based
the following: (1) A least chi-squared ﬁt of the calculated                 Regulation) and by the Max Planck Society.
ensemble averages determined by the current weights to the
                                                                            Notes
experimental data sets with the corresponding nuisance
                                                                            The authors declare no competing ﬁnancial interest.

                                                                            ■
parameters as ﬁt parameters. We have to perform one ﬁt for
every experimental method providing data. (2) With these ﬁtted                  ACKNOWLEDGMENTS
values of the nuisance parameters, we adjust the calculated
observables yαi . These enter another round of optimization from            We thank Dr. Sandro Bottaro, Prof. Kresten Lindorﬀ-Larsen,
                                                                            and Dr. Jakob T. Bullerjahn for useful discussions.

                                                                            ■
which we obtain the optimal weights given the values of the
nuisance parameters. (3) We use these weights for another
round starting with step 1 until convergence is achieved. Note
                                                                                 REFERENCES
that instead of using least-chi-squared ﬁts, one can also include            (1) Ward, A. B.; Sali, A.; Wilson, I. A. Integrative Structural Biology.
priors acting on the nuisance parameters in both the direct and             Science 2013, 339, 913−915.
                                                                             (2) Bottaro, S.; Lindorff-Larsen, K. Biophysical experiments and
iterative formulations.                                                     biomolecular simulations: A perfect match? Science 2018, 361, 355−
   Interestingly, ensemble reﬁnement by reweighting oﬀers a                 360.
way to quantify the agreement between simulations and                        (3) Bonomi, M.; et al. Principles of protein structural ensemble
experiment. After reweighting, we can make a quantitative                   determination. Curr. Opin. Struct. Biol. 2017, 42, 106−116.
statement of how much we would have had to change the                        (4) Rieping, W.; Habeck, M.; Nilges, M. Inferential Structure
simulated ensemble, expressed by the relative entropy or                    Determination. Science 2005, 309, 303−306.
Kullback−Leibler divergence to be able to obtain agreement                   (5) Scheek, R. M.; et al. Structure Determination by NMR. The
with experiment. The quantiﬁcation of the agreement between                 Modeling of NMR Parameters As Ensemble Averages. NATO Advanced
                                                                            Science Institutes Series Series A Life Sciences 1991, 225, 209−217.
simulation and experiment can also be used to identify and                   (6) Lange, O. F.; et al. Recognition Dynamics up to Microseconds
correct deﬁciencies in molecular dynamics force ﬁelds.21 In a               Revealed from an RDC-Derived Ubiquitin Ensemble in Solution.
perturbative formulation, one can seek force ﬁeld corrections               Science 2008, 320, 1471−1475.
that capture the weight change.25                                            (7) Olsson, S.; et al. Probabilistic Determination of Native State
   BioEn accommodates a wide range of error models. With the                Ensembles of Proteins. J. Chem. Theory Comput. 2014, 10, 3484−3491.
gradients of the BioEn log-posterior presented here for Gaussian             (8) Boura, E.; et al. Solution Structure of the ESCRT-I Complex by
error models, with and without correlation, we already cover a              Small-Angle X-Ray Scattering EPR and FRET Spectroscopy. Proc. Natl.
large range of experimental methods. Moreover, in many cases                Acad. Sci. U. S. A. 2011, 108, 9437−9442.
                                                                             (9) Boura, E.; et al. Solution Structure of the ESCRT-I and -II
the Gaussian error model can be used to eﬃciently obtain an                 Supercomplex Implications for Membrane Budding and Scission.
initial estimate for the optimal weights. These estimates can then          Structure 2012, 20, 874−886.
be used as initial weights for an optimization using a more                  (10) Mantsyzov, A. B.; et al. A maximum entropy approach to the
accurate error model but perhaps a less eﬃcient optimization                study of residue-specific backbone angle distributions in α-synuclein, an
method. We provide an open-source implementation at https://                intrinsically disordered protein. Protein Sci. 2014, 23, 1275−1290.

                                                                     3399                                                        DOI: 10.1021/acs.jctc.8b01231
                                                                                                                 J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                                                                 Article

 (11) Mantsyzov, A. B.; et al. MERA: a webserver for evaluating                     Entropy Reweighting Approach. Preprint bioRxiv, https://www.
backbone torsion angle distributions in dynamic and disordered                      biorxiv.org/content/10.1101/457952v1, 2018.
proteins from NMR data. J. Biomol. NMR 2015, 63, 85.                                  (36) Hansen, P. C.; O’Leary, D. P. The Use of the L-Curve in the
 (12) Koch, M. H. J.; Vachette, P.; Svergun, D. I. Small-angle                      Regularization of Discrete Ill-Posed Problems. SIAM J. Sci. Comput.
scattering: a view on the properties, structures and structural changes of          1993, 14, 1487−1503.
biological macromolecules in solution. Q. Rev. Biophys. 2003, 36, 147−                (37) Fletcher, R. Practical Methods of Optimization, 2nd ed.; Wiley-
227.                                                                                Interscience: New York, NY, USA, 1987.
 (13) Makowski, L.; et al. Characterization of Protein Fold by Wide-                  (38) Nocedal, J.; Wright, S. J. Numerical Optimization, 2nd ed.;
Angle X-ray Solution Scattering. J. Mol. Biol. 2008, 383, 731−744.                  Springer: New York, 2006.
 (14) Rozycki, B.; Kim, Y. C.; Hummer, G. SAXS Ensemble                               (39) Liu, D. C.; Nocedal, J. On the limited memory BFGS method for
Refinement of ESCRT-III Chmp3 Conformational Transitions.                           large scale optimization. Math. Program. 1989, 45, 503−528.
Structure 2011, 19, 109−116.                                                          (40) Nocedal, J. Updating Quasi-Newton Matrices with Limited
 (15) Boomsma, W.; Ferkinghoff-Borg, J.; Lindorff-Larsen, K.                        Storage. Math. Comput. 1980, 35, 773−782.
Combining Experiments and Simulations Using the Maximum Entropy                       (41) Graf, J.; et al. Structure and Dynamics of the Homologous Series
Principle. PLoS Comput. Biol. 2014, 10, No. e1003406.                               of Alanine Peptides: A Joint Molecular Dynamics/NMR Study. J. Am.
 (16) Sali, A.; et al. Outcome of the First wwPDB Hybrid/Integrative                Chem. Soc. 2007, 129, 1179−1189.
Methods Task Force Workshop. Structure 2015, 23, 1156−1167.                           (42) Stelzl, L. S.; et al. Dynamic Histogram Analysis To Determine
 (17) Vallat, B.; et al. Development of a Prototype System for Archiving            Free Energies and Rates from Biased Simulations. J. Chem. Theory
Integrative/Hybrid Structure Models of Biological Macromolecules.                   Comput. 2017, 13, 6328−6342.
Structure 2018, 26, 894.                                                              (43) Best, R. B.; Buchete, N.-V.; Hummer, G. Are Current Molecular
 (18) Berlin, K.; et al. Recovering a Representative Conformational                 Dynamics Force Fields too Helical? Biophys. J. 2008, 95, L07−L09.
Ensemble from Underdetermined Macromolecular Structural Data. J.                      (44) Shen, Y.; Bax, A. SPARTA+: a modest improvement in empirical
Am. Chem. Soc. 2013, 135, 16595−16609.                                              NMR chemical shift prediction by means of an artificial neural network.
 (19) Best, R. B.; Vendruscolo, M. Determination of Protein Structures              J. Biomol. NMR 2010, 48, 13−22.
Consistent with NMR Order Parameters. J. Am. Chem. Soc. 2004, 126,                    (45) McGibbon, R. T.; et al. MDTraj: A Modern Open Library for the
8090−8091.                                                                          Analysis of Molecular Dynamics Trajectories. Biophys. J. 2015, 109,
 (20) Roux, B.; Weare, J. On the Statistical Equivalence of Restrained-             1528−1532.
Ensemble Simulations With the Maximum Entropy Method. J. Chem.                        (46) Michaud-Agrawal, N.; et al. MDAnalysis: A Toolkit for the
Phys. 2013, 138, 084107.                                                            Analysis of Molecular Dynamics Simulations. J. Comput. Chem. 2011,
 (21) Hummer, G.; Köfinger, J. Bayesian ensemble refinement by                     32, 2319−2327.
replica simulations and reweighting. J. Chem. Phys. 2015, 143, 243150.                (47) Gowers, R. J.; et al. MDAnalysis: A Python Package for the Rapid
 (22) Pitera, J. W.; Chodera, J. D. On the Use of Experimental                      Analysis of Molecular Dynamics Simulations. Proceedings of the 15th
Observations to Bias Simulated Ensembles. J. Chem. Theory Comput.                   Python in Science Conference 2016, 98−105.
2012, 8, 3445−3451.                                                                   (48) Wolfe, P. Convergence Conditions for Ascent Methods. SIAM
 (23) White, A. D.; Voth, G. A. Efficient and Minimal Method to Bias                Rev. 1969, 11, 226−235.
Molecular Simulations with Experimental Data. J. Chem. Theory                         (49) Wolfe, P. Convergence Conditions for Ascent Methods. II: Some
Comput. 2014, 10, 3023−3030.                                                        Corrections. SIAM Rev. 1971, 13, 185−188.
 (24) White, A. D.; Dama, J. F.; Voth, G. A. Designing Free Energy                    (50) Pearson, K. Notes on regression and inheritance in the case of
Surfaces That Match Experimental Data With Metadynamics. J. Chem.                   two parents. Proc. R. Soc. London 1895, 58, 240−242.
Theory Comput. 2015, 11, 2451−2460.                                                   (51) Meier, S.; Blackledge, M.; Grzesiek, S. Conformational
 (25) Cesari, A.; Gil-Ley, A.; Bussi, G. Combining Simulations and                  distributions of unfolded polypeptides from novel NMR techniques.
Solution Experiments as a Paradigm for RNA Force Field Refinement. J.               J. Chem. Phys. 2008, 128, 052204.
Chem. Theory Comput. 2016, 12, 6192−6200.                                             (52) Case, D. A.; Scheurer, C.; Brüschweiler, R. Static and Dynamic
 (26) Dannenhoffer-Lafage, T.; White, A. D.; Voth, G. A. A Direct                   Effects on Vicinal Scalar J Couplings in Proteins and Peptides: A MD/
Method for Incorporating Experimental Data into Multiscale Coarse-                  DFT Analysis. J. Am. Chem. Soc. 2000, 122, 10390−10397.
Grained Models. J. Chem. Theory Comput. 2016, 12, 2144−2153.                          (53) Feng, Y.; et al. Structure of Penta-Alanine Investigated by Two-
 (27) Bonomi, M.; et al. Metainference: A Bayesian inference method                 Dimensional Infrared Spectroscopy and Molecular Dynamics Simu-
for heterogeneous systems. Sci. Adv. 2016, 2, No. e1501177.                         lation. J. Phys. Chem. B 2016, 120, 5325−5339.
 (28) Bonomi, M.; Camilloni, C.; Vendruscolo, M. Metadynamic                          (54) Feng, C.-J.; Dhayalan, B.; Tokmakoff, A. Refinement of Peptide
metainference: Enhanced sampling of the metainference ensemble                      Conformational Ensembles by 2D IR Spectroscopy: Application to Ala-
using metadynamics. Sci. Rep. 2016, 6, 31232.                                       Ala-Ala. Biophys. J. 2018, 114, 2820−2832.
 (29) Francis, D. M.; et al. Structural basis of p38 alpha regulation by              (55) Best, R. B.; Zheng, W.; Mittal, J. Balanced Protein-Water
hematopoietic tyrosine phosphatase. Nat. Chem. Biol. 2011, 7, 916−                  Interactions Improve Properties of Disordered Proteins and Non-
924.                                                                                Specific Protein Association. J. Chem. Theory Comput. 2014, 10, 5113−
 (30) Bottaro, S.; et al. Conformational ensembles of RNA                           5124.
oligonucleotides from integrating NMR and molecular simulations.                      (56) Best, R. B.; Hummer, G. Optimized Molecular Dynamics Force
Sci. Adv. 2018, 4, No. eaar8521.                                                    Fields Applied to the Helix-Coil Transition of Polypeptides. J. Phys.
 (31) Kullback, S.; Leibler, R. A. On Information and Sufficiency. Ann.             Chem. B 2009, 113, 9004−9015.
Math. Stat. 1951, 22, 79−86.                                                          (57) Lindorff-Larsen, K.; et al. Systematic Validation of Protein Force
 (32) Byrd, R. H.; Nocedal, J.; et al. A Limited Memory Algorithm for               Fields against Experimental Data. PLoS One 2012, 7, e32131.
Bound Constrained Optimization. SIAM Journal on Scientific and                        (58) Wright, P. E.; Dyson, H. J. Intrinsically disordered proteins in
Statistical Computing 1995, 16, 1190−1208.                                          cellular signalling and regulation. Nat. Rev. Mol. Cell Biol. 2015, 16, 18.
 (33) Mead, L. R.; Papanicolaou, N. Maximum entropy in the problem                    (59) Fisher, C. K.; Stultz, C. M. Constructing ensembles for
of moments. J. Math. Phys. 1984, 25, 2404−2417.                                     intrinsically disordered proteins. Curr. Opin. Struct. Biol. 2011, 21,
 (34) Cesari, A.; Reißer, S.; Bussi, G. Using the Maximum Entropy                   426−431.
Principle to Combine Simulations and Solution Experiments.                            (60) Gull, S. F.; Daniell, G. J. Image-Reconstruction from Incomplete
Computation 2018, 6, 15.                                                            and Noisy Data. Nature 1978, 272, 686−690.
 (35) Bottaro, S.; Bengtsen, T.; Lindorﬀ-Larsen, K. Integrating                       (61) Cavalli, A.; Camilloni, C.; Vendruscolo, M. Molecular Dynamics
Molecular Simulation and Experimental Data: A Bayesian/Maximum                      Simulations With Replica-Averaged Structural Restraints Generate

                                                                             3400                                                         DOI: 10.1021/acs.jctc.8b01231
                                                                                                                          J. Chem. Theory Comput. 2019, 15, 3390−3401
Journal of Chemical Theory and Computation                                                                      Article

Structural Ensembles According to the Maximum Entropy Principle. J.
Chem. Phys. 2013, 138, 094112.
 (62) Boomsma, W.; et al. Equilibrium Simulations of Proteins Using
Molecular Fragment Replacement and NMR Chemical Shifts. Proc.
Natl. Acad. Sci. U. S. A. 2014, 111, 13852−13857.
 (63) Rangan, R.; et al. Determination of Structural Ensembles of
Proteins: Restraining vs Reweighting. J. Chem. Theory Comput. 2018,
14, 6632.
 (64) Rosta, E.; et al. Catalytic Mechanism of RNA Backbone Cleavage
by Ribonuclease H from Quantum Mechanics/Molecular Mechanics
Simulations. J. Am. Chem. Soc. 2011, 133, 8934−8941.
 (65) Shirts, M. R.; Chodera, J. D. Statistically optimal analysis of
samples from multiple equilibrium states. J. Chem. Phys. 2008, 129,
124105.
 (66) Reichel, K.; et al. Precision DEER Distances from Spin-Label
Ensemble Refinement. J. Phys. Chem. Lett. 2018, 9, 5748−5752.

                                                                        3401                   DOI: 10.1021/acs.jctc.8b01231
                                                                               J. Chem. Theory Comput. 2019, 15, 3390−3401


---

# Metainference: A Bayesian inference method for heterogeneous systems

**Authors:** Massimiliano Bonomi, Carlo Camilloni, Andrea Cavalli, Michele Vendruscolo
**Year:** 2016
**Venue:** Science Advances
**DOI:** 10.1126/sciadv.1501177
**Source PDF URL:** https://arxiv.org/pdf/1509.05684
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Metainference: A Bayesian Inference Method for Heterogeneous Systems

Massimiliano Bonomi1,*,†, Carlo Camilloni1,†, Andrea Cavalli1,2 and Michele Vendruscolo1,*
†
    These authors contributed equally to this work
*
    Corresponding author. E-mail: mb2006@cam.ac.uk (M.B.); mv245@cam.ac.uk (M.V.)

    Department of Chemistry, University of Cambridge, Cambridge CB2 1EW, UK.
    Institute for Research in Biomedicine (IRB), Bellinzona, Switzerland.

                                           Abstract
Modelling a complex system is almost invariably a challenging task. The incorporation of
experimental observations can be used to improve the quality of a model, and thus to obtain
better predictions about the behavior of the corresponding system. This approach, however, is
affected by a variety of different errors, especially when a system populates simultaneously an
ensemble of different states and experimental data are measured as averages over such states. To
address this problem we present a Bayesian inference method, called ‘metainference’, that is able
to deal with errors in experimental measurements as well as with experimental measurements
averaged over multiple states. To achieve this goal, metainference models a finite sample of the
distribution of models using a replica approach, in the spirit of the replica-averaging modelling
based on the maximum entropy principle. To illustrate the method we present its application to a
heterogeneous model system and to the determination of an ensemble of structures
corresponding to the thermal fluctuations of a protein molecule. Metainference thus provides an
approach to model complex systems with heterogeneous components and interconverting
between different states by taking into account all possible sources of errors.
Introduction

The quantitative interpretation of experimental measurements requires the construction of a
model of the system under observation. The model usually consists of a description of the system
in terms of several parameters, which are determined by requiring the consistency with the
experimental measurements themselves as well as with theoretical information, being physical or
statistical in nature. This procedure presents several complications. First, experimental data (Fig.
1A) are always affected by random and systematic errors (Fig. 1B, green), which must be
properly accounted for to obtain accurate and precise models. Furthermore, when integrating
multiple experimental observations, one must consider that each experiment has a different level
of noise so that every element of information is properly weighted according to its reliability.
Second, the prediction of experimental observables from the model, which is required to assess
the consistency, is often based on an approximate physico-chemical description of a given
experiment (the so-called ‘forward model’) and thus it is intrinsically inaccurate in itself (Fig.
1B, green). Third, physical systems in equilibrium conditions often populate a variety of
different states whose thermodynamic behaviour can be described by statistical mechanics. In
these heterogeneous systems, experimental observations depend from - and thus probe - a
population of states (Fig. 1B, purple), so that one should determine an ensemble of models
rather than a single one (Fig. 1C).

Among the theoretical approaches available for model building, two frameworks have emerged
as particulary succesfull: Bayesian inference (1-3) and the maximum entropy principle (4).
Bayesian modelling is a rigorous approach to combine prior information on a system with
experimental data and to deal with errors in such data (1-3, 5-8). It proceeds by constructing a
model of noise as a function of one or more unknown uncertainty parameters, which quantify the
agreement between predictions and observations and which are inferred along with the model of
the system. This method has a long history and it is routinely used in a wide range of
applications, including the reconstruction of phyologenetic trees (9), the determination of
population structures from genotype data (10), the interpolation of noisy data (11), image
reconstruction (12), decision theory (13), the analysis of microarray data (14), and the structure
determination of proteins (15, 16) and protein complexes (17). It has also been extended to deal
with mixture of states (18-21) by treating the number of states as a parameter to be determined
by the procedure. The maximum entropy principle is at the basis of approaches that deal with
experimental data averaged over an ensemble of states (4) and provides a link between
information theory and statistical mechanics. In these methods, an ensemble generated using a
prior model is minimally modified by some partial and inaccurate information to match exactly
the observed data. In the recently proposed replica-averaging scheme (22-26), this result is
achieved by modelling an ensemble of replicas of the system using the available information and
additional terms that restraint the average values of the predicted data close to the experimental
observations. This method has been used to determine ensembles representing the structure and
dynamics of proteins (22-26).

Each of the two methods described above can deal with some, but not all of the challenges in
characterizing complex systems by integrating multiple sources of information (Fig. 1B). To
overcome all these problems simultaneously, we present the ‘metainference’ method, a Bayesian
inference approach that quantifies the extent to which a prior distribution of models is modified
by the introduction of experimental data that are expectation values over a heterogeneous
distribution and subject to errors. To achieve this goal, metainference models a finite sample of
this distribution, in the spirit of the replica-averaged modelling based on the maximum entropy
principle. Notably, our approach reduces to the maximum entropy modelling in the limit of
absence of noise in the data, and to standard Bayesian modelling when experimental data are not
ensemble averages. This link between Bayesian inference and the maximum entropy principle is
not surprising given the connections between these two approaches (27, 28). We first benchmark
the accuracy of our method on a simple heterogeneous model system, in which synthetic
experimental data can be generated with different level of noise as averages over a discrete
number of states of the system. We then show its application with nuclear magnetic resonance
(NMR) spectroscopy data in the case of the structural fluctuations of the protein ubiquitin in its
native state, which we modelled by combining chemical shift with residual dipolar couplings
(RDCs).

Results and Discussions

Metainference is a Bayesian approach to model a heterogeneous system and all sources of error
by considering a set of copies of the system (replicas), which represent a finite sample of the
distribution of models, in the spirit of the replica-averaged formulation of the maximum entropy
principle (22-26). The generation of models by suitable sampling algorithms (typically Monte
Carlo or molecular dynamics) is guided by a score given in terms of the negative logarithm of
the posterior probability (Materials and Methods):

      score                                     input                             errors

                         X                                               X 1
 s(X, ) =                      log P (Xr ,              r) +         (X)     2
                           r                                             r
                                                                           2 r
                                                                                  SEM 2     B 2
                                       prior                measurements    2
                                                                            r =   r     +   r

where X = [Xr ] and σ = [σ r ] are respectively the sets of conformational states and
uncertainties, one for each replica. σ r includes all the sources of errors, i.e. the error in
representing the ensemble with a finite number of replicas ( σ rSEM ), as well as random,
systematic, and forward model errors ( σ rB ). P is the prior probability which encodes
information other than experimental data and Δ 2 (X) is the deviation of the experimental data
from the data predicted by the forward model. While this schematic equation, which omits the
data likelihood normalization term for the uncertainty parameters, holds for Gaussian errors and
a single data point, a more general formulation can be found in the Materials and Methods
section, Eqs. 5 and 8.

Metainference of a heterogeneous model system. We first illustrate the metainference method
for a model system that can populate simultaneously a set of discrete states, i.e. a mixture. In this
example, the number of states in the mixture and their population can be varied arbitrarily. We
created synthetic data as ensemble averages over these discrete states (Fig. 2A) and we added
random and systematic noise. We thus introduced a prior information, which provides an
approximate description of the system and its distribution of states, and whose accuracy can also
be tuned. We then used the reference data to complement the prior information and recover the
correct number and populations of the states. We tested the following approaches: metainference
(with the Gaussian and outliers noise models in Eqs. 9 and 11, respectively), replica-averaging
maximum entropy, and standard Bayesian inference (i.e. Bayesian inference without mixtures).
The accuracy of a given approach was defined as the root mean square deviation (RMSD) of the
inferred from the correct populations of the discrete states. We benchmarked the accuracy as a
function of the number of data points used, the level of noise in the data, the number of states
and replicas, and the accuracy of the prior information. Details of the simulations, generation of
data, sampling algorithm, likelihood and model to treat systematic errors and outliers can be
found in Supplementary Materials (SM).

Comparison with the maximum entropy method. We found that the metainference and the
maximum entropy methods perform equally well in absence of noise in the data or in presence of
random noise alone (Fig. 2B,C, grey and orange lines), as expected, given that maximum
entropy is particularly effective in the case of mixtures of states (22, 23). The accuracy of the
two methods was comparable and, most importantly, increased with the number of data points
used (Fig. 2B,C). With 20 data points, 128 replicas, and in absence of noise, the accuracy
averaged on 300 independent simulations of a 5-state system was equal to 0.4%±0.2% and
0.2%±0.1% for the metainference and maximum entropy approaches, respectively. For
reference, the accuracy of the prior information alone was much lower, i.e. 16%. Metainference,
however, outperformed the maximum entropy approach in the presence of systematic errors (Fig.
2B,C, green lines). The accuracy of metainference increased significantly more rapidly upon
adding new information, despite the high level of noise. When using 20 data points, 128 replicas,
and 30% outliers ratio, the accuracy averaged on 300 independent simulations of a 5-state system
was equal to 2%±2% and 14%±5% for the metainference and maximum entropy approaches,
respectively. As systematic errors are ubiquitous, both in the experimental data and in the
forward model used to predict the data, this situation reflects more closely a realistic scenario.
The ability of metainference to deal at the same time and effectively with conformational
averaging and with the presence of systematic errors is the major motivation for introducing this
method. This approach can thus leverage the substantial amount of noisy data produced by high-
throughput techniques and accurately model conformational ensembles of heterogeneous
systems.

Comparison with standard Bayesian modelling. In the standard Bayesian approach one assumes
the presence of a single state in the sample and estimates its probability or confidence level given
experimental data and prior knowledge available. When modelling multiple-states systems with
ensemble-averaged data and standard Bayesian modelling, one could be tempted to interpret the
probability of each state as its equilibrium population. In doing so, however, one makes a
significant error, which grows with the number of data points used, regardless of the level of
noise in the data (Fig. 2D).

Role of the prior information. We tested two priors with different accuracy, with an average
population error per state equal to 8% and 16%, respectively. The results suggest that the number
of experimental data points required to achieve a given accuracy of the inferred populations
depends on the quality of the prior information (Fig. S1). The more accurate is the prior, the
fewer data points are needed. This is an intuitive, yet important, result. Accurate priors almost
invariably require more complex descriptions of the system under study, thus they come at a
higher computational costs.

Scaling with the number of replicas. As the number of replicas grows, the error in estimating
ensemble averages using a finite number of replicas decreases and the overall accuracy of the
inferred populations increases (Fig. S2), regardless of the level of noise in the data. Furthermore,
we verified numerically that, in the absence of random and systematic errors in the data, the
intensity of the harmonic restraint, which couples the average of the forward model on the N
replicas to the experimental data (Eq. 7), scales as N 2 (Fig. 3). This test confirms that, in the
limit of absence of noise in the data, metainference coincides with the replica-averaging
maximum entropy modelling (Materials and Methods).

Scaling with the number of states. Metainference is also robust to the number of states populated
by the system. We tested our model in the case of 5 and 50 states and determined that the number
of data points needed to achieve a given accuracy scales less than linearly with the number of
states (Fig. S3).

Outliers model and error marginalization. As the number of data points and replicas increases, it
becomes computationally more and more inconvenient to use one error parameter per replica and
data point. In this situation one can assume a unimodal and long-tailed distribution for the errors,
peaked around a typical value for a dataset (or experiment type) and replica, and marginalize all
the uncertainty parameters of the single data points (Materials and Methods). The accuracy of
this marginalized error model was found to be similar to the case in which a single error
parameter was used for each data point (Fig. S4).

Analysis of the inferred uncertainties. We analyzed the distribution of inferred uncertainties σ B
in presence of systematic errors (outliers), when using a Gaussian data likelihood with one
uncertainty per data point (Eq. 9) and the outliers model with one uncertainty per dataset (Eq.
11). In the former case, metainference was able to automatically detect the data points affected
by systematic errors, assign them a higher uncertainty, and thus downweight the associated
restraints (Fig 4A). In the latter, the inferred typical dataset uncertainty was somewhere in
between the uncertainty inferred using the Gaussian likelihood on the data points with no noise
and on the outliers (Fig 4B). In this specific test (5 states, 20 data points, including 8 outliers,
prior accuracy equal to 16%, 128 replicas), both data noise models generated ensemble of
comparable accuracy (3%).

Metainference in integrative structural biology. We compared the metainference and maximum
entropy approaches using NMR experimental data on a classical example in structural biology,
the structural fluctuations in the native state of ubiquitin (22, 29, 30). A conformational ensemble
of ubiquitin was modelled using CA, CB, CO, HA, HN, and NH chemical shifts combined with
RDCs collected in a steric medium (30) (Fig. 5A). The ensemble was validated by multiple
criteria (Table S1). The stereochemical quality was assessed by PROCHECK (31); data not used
for modelling, including 3JHNC and 3JHNHA scalar couplings and RDCs collected in other media
(32), were backcalculated and compared with the experimental data. Exhaustive sampling was
achieved by 1 µs long molecular dynamics simulations, performed with GROMACS (33)
equipped with PLUMED (34). As prior information we used the CHARMM22* force field (35).
Additional details of these simulations can be found in SM.

The quality of the metainference ensemble (Fig. 5B) was higher than that of the maximum
entropy ensemble, as suggested by the better fit with the data not used in the modelling (Fig. 5C
and Table S1) and by the stereochemical quality (Table S2). Data used as restraints were also
more accurately reproduced by metainference. One of the major differences between the two
approaches is that metainference can deal more effectively with the errors in the chemical shifts
calculated on different nuclei. The more inaccurate HN and NH chemical shifts were detected by
metainference and thus automatically downweighted in constructing the ensemble (Fig. 6).

We also compared the metainference ensemble with an ensemble generated by standard
molecular dynamics simulations (MD) and with a high-resolution NMR structure (NMR). The
metainference ensemble obtained by combining chemical shifts and RDCs reproduced all the
experimental data not used for the modelling better than the MD ensemble and the NMR
structure. The only exception were the 3JHNC scalar couplings, which were slightly more accurate
in the MD ensemble, and the 3JHNHA scalar couplings, which were better predicted by the NMR
structure (Fig. 5C and Table S1).

The NMR structure, which was determined according to the criterion of maximum parsimony,
accurately reproduced most of the available experimental data. Ubiquitin, however, exhibits rich
dynamical properties over a wide range of time scales that are averaged in the experimental data
(36). In particular, a main source of dynamics involves a flip of the backbone of residues D52-
G53 coupled with the formation of a hydrogen bond between the side chain of E24 and the
backbone of G53. While metainference was able to capture the conformational exchange
between these two states, the static representation provided by the NMR structure could not (Fig.
5B).

In conclusion, we have presented the metainference approach, which enables building ensemble
of models consistent with experimental data when the data are affected by errors and are
averaged over a mixtures of states of a system. Since complex systems and experimental data
almost invariably exhibit both heterogeneity and errors, we anticipate that our method will find
applications across a wide variety of scientific fields, including genomics, proteomics,
metabolomics and integrative structural biology.

Materials and Methods

The quantitative understanding of a system involves the construction of a model M to represent
it. If a system can occupy multiple possible states, one should determine the distribution of
models p(M ) that specifies in which states the system is found and with which probability. To
construct this distribution of models, one should take into account the consistency with the
overall knowledge that one has about the system. This includes theoretical knowledge (called the
‘prior’ information, I ), and the information acquired from experimental measurements (i.e. the
‘data’, D ) (1). In Bayesian inference the probability of a model given the information available
is known as the posterior probability p(M | D, I ) of M given D and I , and it is given by

p(M | D, I ) ∝ p(D | M, I )p(M | I )                                                          (1)

where the likelihood function p(D | M, I ) is the probability of observing D given M and I , and
the prior probability p(M | I ) is the probability of M given I . To define the likelihood
function, one needs a forward model f (M ) that predicts the data that would be observed for
model M , and a noise model that specifies the distribution of the deviations between the
observed and predicted data. In the following we assume that the forward model depends only on
the conformational state X of the system and that the noise model is defined in terms of
unknown parameters σ that are part of the model M = (X, σ ) . These parameters quantify the
level of noise in the data and they are inferred along with the state X by sampling the posterior
distribution. The sampling is usually carried out using computational techniques such as Monte
Carlo, molecular dynamics, or combined methods based on Gibbs sampling (1).

Mixture of states. Experimental data collected under equilibrium conditions are usually the
result of ensemble averages over a large number of states. In metainference, the prior
information p(X) of state X provides an a priori description of the distribution of states. To
quantify the fit with the observed data and determine to which extent the prior distribution is
modified by the introduction of the data, we need to calculate expectation values of the forward
model over the distribution of states. Inspired by the replica-averaged modelling based on the
maximum entropy principle (22-26), we consider a finite sample of this distribution by
modelling simultaneously N replicas of the model M = [M r ] and we calculate the forward
model as an average over the states X = [Xr ]

            1 N
     f (X) = ∑ f (Xr )                                                                                          (2)
            N r=1

Typically we have information only about expectation values on the distribution of states X ,
and not on the other parameters of the model, such as σ . However, we are interested in
determining also how the prior distributions of these parameters are modified by the introduction
of the experimental data and in doing so we need to treat all the parameters of the model in the
same way , i.e. symmetrically. Therefore, we model a finite sample of the distributions of all
parameters of the model.

To reduce the computational cost, typically a relatively small number of replicas is used in the
modelling. In this situation, the estimate f (X) of the forward model deviates from the average
 f! that would be obtained using an infinite number of replicas. This is an unknown quantity,
which we add to the parameters of our model. However, the central limit theorem provides a
strong parametric prior since it guarantes that the probability of having a certain value of f!
given a finite number of states X is a Gaussian distribution

                                     " f! − f (X) 2 %
    p( f! | X, σ SEM ) =
                                 exp $−
                                               (    '       )
                         2πσ SEM     $ 2 σ SEM ' 2
                                                                                                                (3)
                                     #   ( ) &
where the standard error of the mean σ SEM decreases with the square root of the number of
replicas

 σ SEM ∝                                                                                                              (4)
           N

We have recognized so far that in considering a finite sample of our distribution of states we
introduce an error in the calculation of expectation values. Therefore, experimental data should
be compared to the (unknown) average of the forward model over an infinite number of replicas
 f! , which is then related to the average over our finite sample f (X) via the central limit theorem
of Eq. 3. From these considerations, we can derive the posterior probability of the ensemble of
 N replicas representing a finite sample of our distribution of models M = (X, f! , σ B, σ SEM ) . In
the case of a single experimental data point d , this can be expressed as (see SM)

                                      N
     p(X, f! , σ B, σ SEM | d, I ) ∝ ∏ p(d | f!r , σ rB )⋅ p( f!r | X, σ rSEM )⋅ p(σ rB )⋅ p(Xr )⋅ p(σ rSEM )   (5)
                                      r=1
The data likelihood p(d | f!r , σ rB ) relates the experimental data d to the average of the forward
model over an infinite number of replicas, given the uncertainty σ rB . This parameter describes
random and systematic errors in the experimental data as well as errors in the forward model.
The functional form of p(d | f!r , σ rB ) depends on the nature of the experimental data, and it is
typically a Gaussian or log-normal distribution. As noted above, p( f!r | X, σ rSEM ) is the parametric
prior on f!r that relates the (unknown) average f!r to the estimate f (X) computed with a finite
number of replicas N via the central limit theorem of Eq. 3, and thus it is always a Gaussian
distribution. p(σ rSEM ) is the prior on the standard error of the mean σ rSEM and encodes Eq. 4,
 p(σ rB ) is the prior on the uncertainty parameter σ rB , and p(Xr ) is the prior on the structure X r .

Gaussian noise model. We can further simplify Eq. 5 in the case of Gaussian data likelihood
p(d | f!r , σ rB ) . In this situation, f!r can be marginalized (see SM) and the posterior probability can
be written as

                           N
                                1        # ( d − f (X))2 &
    p(X, σ | d, I ) ∝ ∏              exp %−              ( p(σ r )p(Xr )                                                (6)
                        r=1    2πσ r     %$     2σ r2    ('

                                                      SEM 2         B 2
where the effective uncertainty σ r =             (σ ) + (σ )
                                                      r             r      encodes all sources of errors: the
statistical error due to the use of a finite number of replicas, experimental and systematic errors,
and errors in the forward model. The associated energy function in units of kBT becomes

                           N           N
                       2        1
    E = ( d − f (X)) ∑            2
                                    + ∑#$log σ r − log p (σ r ) − log p(Xr )%&                                          (7)
                           r=1 2σ r   r=1

This equation shows how metainference includes different existing modelling methods in
limiting cases. In the absence of data and forward model errors ( σ rB = 0 ), our approach reduces
to the replica-averaged maximum entropy modelling, in which a harmonic restraint couples the
                                                                                               N
replica-averaged observable to the experimental data. The intensity of the restraint k = ∑ 2
                                                                                              r=1 σ r

scales with the number of replicas as N , i.e. more than linearly, as required by the maximum

entropy principle (24). We numerically verified this behavior in our heterogeneous model
system, in absence of any errors in the data (Fig. 3). In presence of errors ( σ rB ≠ 0 ), the intensity
 k scales as N and it is modulated by the data uncertainty σ rB . Finally, in the case in which the
experimental data are not ensemble averages ( σ rSEM = 0 ), we recover the standard Bayesian
modelling.

Multiple experimental data points. Eq. 5 can be extended to the case of N d independent data
points D = [di ] , possibly gathered in different experiments with varying levels of noise (see SM)

                                   N   Nd                                                                   N
p(X, f! , σ B, σ SEM | D, I ) ∝ ∏∏ p(di | f!r,i , σ r,iB )⋅ p( f!r,i | X, σ r,iSEM )⋅ p(σ r,iB )⋅ p(σ r,iSEM ) ⋅ ∏ p(Xr ) (8)
                                  r=1 i=1                                                                  r=1
Outliers model. To reduce the number of parameters that need to be sampled in the case of
multiple experimental data points, one can model the distribution of the errors around a typical
dataset error and marginalize the error parameters for the individual data points. For example, a
dataset can be defined as a set of chemical shifts or RDCs on a given nucleus. In this cases, it is
reasonable to assume that the level of error of the individual data points in the dataset is
homogenoues, except for the presence of few outliers. Let us consider for example the case of
Gaussian data noise. In the case of multiple experimental data points, Eq. 6 becomes

                             N           Nd
                                                1          $ ( d − f (X))2 '
        p(X, σ | D, I ) ∝ ∏ p(Xr )∏                    exp &− i i 2        ) p (σ r,i )                      (9)
                             r=1         i=1   2πσ r,i     &%    2σ r,i    )(

The prior p (σ r,i ) can be modeled using a unimodal distribution peaked around a typical dataset
effective uncertainty σ r,0 and with a long tail to tolerate outliers data points (37)

                  2σ r,0       " σ2 %
   p (σ r,i ) =            exp $$ − r,0
                                     2 '
                                        '                                                                    (10)
                   πσ r,i2      # σ r,i &

                          SEM 2      B 2
where σ r,0 =           (σ ) + (σ ) , with σ
                                     r,0
                                                        SEM
                                                              is the the standard error of the mean for all data
points in the dataset and replicas and σ r,0B
                                              is the typical data uncertainty of the dataset. We can
thus marginalize σ r,i by integrating over all its possible values, given that all the data
uncertainties σ r,iB range from 0 to infinity

                         N          Nd    +∞
                                           2σ r,0       ' 0.5 ( d − f (X))2 + σ 2 *
p(X, σ 0 | D, I ) ∝ ∏ p(Xr ) ⋅ ∏ ∫ dσ r,i    3
                                                  ⋅ exp )−       i   i
                                                                                r,0
                                                                                    ,
                    r=1        i=1 σ SEM  πσ r,i        )(          σ r,i           ,+

   N              Nd                                         *       $                      2  2 '.
                         2σ r,0               1              ,       &  0.5 ( di − fi (X)) + σ r,0 ),/
= ∏ p(Xr ) ⋅ ∏                  ⋅                          ⋅ +1− exp  −
                          π                     2
                                  ( di − fi (X)) + 2σ r,02 ,-        &                    2
                                                                                                   ), (11)
  r=1             i=1
                                                                     %           (σ SEM )          (0

After marginalization, we are left with just one parameter σ r,0
                                                             B
                                                                 per replica that needs to be
sampled.
References and Notes

1.    G. E. Box, G. C. Tiao, Bayesian inference in statistical analysis. (John Wiley & Sons, 2011),
      vol. 40.
2.    J. M. Bernardo, A. F. Smith, Bayesian theory. (John Wiley & Sons, 2009), vol. 405.
3.    P. M. Lee, Bayesian statistics: an introduction. (John Wiley & Sons, 2012).
4.    E. T. Jaynes, Information theory and statistical mechanics. Phys. Rev. 106, 620-630 (1957).
5.    S. Tavaré, D. J. Balding, R. C. Griffiths, P. Donnelly, Inferring coalescence times from DNA
      sequence data. Genetics 145, 505-518 (1997).
6.    J. K. Pritchard, M. T. Seielstad, A. Perez-Lezaun, M. W. Feldman, Population growth of human
      Y chromosomes: a study of Y chromosome microsatellites. Mol. Biol. Evol. 16, 1791-1798
      (1999).
7.    D. Poole, A. E. Raftery, Inference for deterministic simulation models: the Bayesian melding
      approach. J. Am. Stat. Assoc. 95, 1244-1255 (2000).
8.    M. C. Kennedy, A. O'Hagan, Bayesian calibration of computer models. J. R. Statist. Soc. B, 425-
      464 (2001).
9.    J. P. Huelsenbeck, F. Ronquist, MRBAYES: Bayesian inference of phylogenetic trees.
      Bioinformatics 17, 754-755 (2001).
10.   J. K. Pritchard, M. Stephens, P. Donnelly, Inference of population structure using multilocus
      genotype data. Genetics 155, 945-959 (2000).
11.   D. J. MacKay, Bayesian interpolation. Neural Comp. 4, 415-447 (1992).
12.   S. Geman, D. Geman, Stochastic relaxation, Gibbs distributions, and the Bayesian restoration of
      images. IEEE Trans. Pattern Anal. Mach. Intell. 6, 721-741 (1984).
13.   J. O. Berger, Statistical decision theory and Bayesian analysis. (Springer Science & Business
      Media, 2013).
14.   P. Baldi, A. D. Long, A Bayesian framework for the analysis of microarray expression data:
      regularized t-test and statistical inferences of gene changes. Bioinformatics 17, 509-519 (2001).
15.   W. Rieping, M. Habeck, M. Nilges, Inferential structure determination. Science 309, 303-306
      (2005).
16.   J. L. MacCallum, A. Perez, K. A. Dill, Determining protein structures by combining semireliable
      data with atomistic physical models by Bayesian inference. Proc. Natl. Acad. Sci. USA 112,
      6985-6990 (2015).
17.   J. P. Erzberger et al., Molecular Architecture of the 40S⋅ eIF1⋅ eIF3 Translation Initiation
      Complex. Cell 158, 1123-1135 (2014).
18.   P. Cossio, G. Hummer, Bayesian analysis of individual electron microscopy images: towards
      structures of dynamic and heterogeneous biomolecular assemblies. J. Struct. Biol. 184, 427-437
      (2013).
19.   M. T. Marty et al., Bayesian Deconvolution of Mass and Ion Mobility Spectra: From Binary
      Interactions to Polydisperse Ensembles. Anal. Chem. 87, 4370-4376 (2015).
20.   K. S. Molnar et al., Cys-scanning disulfide crosslinking and bayesian modeling probe the
      transmembrane signaling mechanism of the histidine kinase, PhoQ. Structure 22, 1239-1251
      (2014).
21.   T. O. Street et al., Elucidating the mechanism of substrate recognition by the bacterial Hsp90
      molecular chaperone. J. Mol. Biol. 426, 2393-2404 (2014).
22.   K. Lindorff-Larsen, R. B. Best, M. A. DePristo, C. M. Dobson, M. Vendruscolo, Simultaneous
      determination of protein structure and dynamics. Nature 433, 128-132 (2005).
23.   A. Cavalli, C. Camilloni, M. Vendruscolo, Molecular dynamics simulations with replica-
      averaged structural restraints generate structural ensembles according to the maximum entropy
      principle. J. Chem. Phys. 138, 094112 (2013).
24.   B. Roux, J. Weare, On the statistical equivalence of restrained-ensemble simulations with the
      maximum entropy method. J. Chem. Phys. 138, 084107 (2013).
25.   J. W. Pitera, J. D. Chodera, On the use of experimental observations to bias simulated ensembles.
      J. Chem. Theory Comp. 8, 3445-3451 (2012).
26.   W. Boomsma, J. Ferkinghoff-Borg, K. Lindorff-Larsen, Combining experiments and simulations
      using the maximum entropy principle. PLoS Comp. Biol. 10, e1003406 (2014).
27.   A. Giffin, A. Caticha, Updating probabilities with data and moments. arXiv preprint
      arXiv:0708.1593, (2007).
28.   A. Caticha, Entropic inference. arXiv preprint arXiv:1011.0723, (2010).
29.   S. Vijay-Kumar, C. E. Bugg, W. J. Cook, Structure of ubiquitin refined at 1.8 Åresolution. J.
      Mol. Biol. 194, 531-544 (1987).
30.   G. Cornilescu, J. L. Marquardt, M. Ottiger, A. Bax, Validation of protein structure from
      anisotropic carbonyl chemical shifts in a dilute liquid crystalline phase. J. Am. Chem. Soc. 120,
      6836-6837 (1998).
31.   R. A. Laskowski, M. W. MacArthur, D. S. Moss, J. M. Thornton, PROCHECK: a program to
      check the stereochemical quality of protein structures. J. Appl. Crystallogr. 26, 283-291 (1993).
32.   O. F. Lange et al., Recognition dynamics up to microseconds revealed from an RDC-derived
      ubiquitin ensemble in solution. Science 320, 1471-1475 (2008).
33.   S. Pronk et al., GROMACS 4.5: a high-throughput and highly parallel open source molecular
      simulation toolkit. Bioinformatics 29, 845–854 (2013).
34.   G. A. Tribello, M. Bonomi, D. Branduardi, C. Camilloni, G. Bussi, PLUMED 2: New feathers
      for an old bird. Comp. Phys. Comm. 185, 604-613 (2014).
35.   S. Piana, K. Lindorff-Larsen, D. E. Shaw, How robust are protein folding simulations with
      respect to force field parameterization? Bioph. J. 100, L47-L49 (2011).
36.   N. Salvi, S. Ulzega, F. Ferrage, G. Bodenhausen, Time scales of slow motions in ubiquitin
      explored by heteronuclear double resonance. J. Am. Chem. Soc. 134, 2481-2484 (2012).
37.   D. Sivia, J. Skilling, Data analysis: A Bayesian tutorial., (Oxford University Press, 1996).
38.   K. J. Kohlhoff, P. Robustelli, A. Cavalli, X. Salvatella, M. Vendruscolo, Fast and accurate
      predictions of protein NMR chemical shifts from interatomic distances. J. Am. Chem. Soc. 131,
      13894-13895 (2009).
39.   W. L. Jorgensen, J. Chandrasekhar, J. D. Madura, R. W. Impey, M. L. Klein, Comparison of
      simple potential functions for simulating liquid water. J. Chem. Phys. 79, 926-935 (1983).
40.   B. Hess, H. Bekker, H. J. Berendsen, J. G. Fraaije, LINCS: a linear constraint solver for
      molecular simulations. J. Comp. Chem. 18, 1463-1472 (1997).
41.   G. Bussi, D. Donadio, M. Parrinello, Canonical sampling through velocity rescaling. J. Chem.
      Phys. 126, 014101 (2007).
42.   Y. Shen, A. Bax, SPARTA+: a modest improvement in empirical NMR chemical shift prediction
      by means of an artificial neural network. J. Biomol. NMR 48, 13-22 (2010).
43.   M. Zweckstetter, A. Bax, Prediction of sterically induced alignment in a dilute liquid crystalline
      phase: aid to protein structure determination by NMR. J. Am. Chem. Soc. 122, 3791-3792
      (2000).
44.   M. Barfield, Structural dependencies of interresidue scalar coupling h3 J nc'and donor 1H
      chemical shifts in the hydrogen bonding regions of proteins. J. Am. Chem. Soc. 124, 4158-4168
      (2002).
45.   B. Vögeli, J. Ying, A. Grishaev, A. Bax, Limits on variations in protein backbone dynamics from
      precise measurements of scalar couplings. J. Am. Chem. Soc. 129, 9377-9385 (2007).

      Acknowledgments

      The authors would like to thank Antonietta Mira for useful Bayesian discussions.
Figures and Tables

 a) Input                                            b) Errors
   Measurement+Prior                                  Mixing

                                                      Random

                                                      Systematic

                                                      Forward model

 c) Output
            Metainference: Ensemble of models

Figure 1. Schematic illustration of the metainference method. To generate accurate and
precise models from input information (A), one must recognize that data from experimental
measurements are always affected by random and systematic errors and that the physico-
chemical interpretation of an experiment is also inaccurate (B, green panels). Moreover, data
collected on heterogeneous systems depend on a multitude of states and by their population (B,
purple panel). Metainference can treat all these sources of error and thus it can properly combine
multiple experimental data with prior knowledge of a system to produce ensembles of models
consistent with the input information (C).
                                                                     Metainference
 a)                                              b)
                                                                                        MaxEnt
                                                                                        Bayes

                                                   Error

                                                                  Maximum entropy
                                                 c)

        Mixture of              Mixture of         Error
        Species                  States

                  Measurement
                                                                  Bayesian inference
                                                 d)

                                                   Error

                                                                         # data

Figure 2. Metainference of a model heterogeneous system. Equilibrium measurements on
mixtures of different species or states do not reflect a single specie or conformation, but are
instead averaged over the whole ensemble (A). We describe such a scenario using a model
heterogeneous system composed of multiple discrete states on which we tested metainference
(B), the maximum entropy approach (C), and standard Bayesian modelling (D), using synthetic
data. We assess the accuracy of these methods in determining the populations of the states as a
function of the number of data points used and the level of noise in the data. Among these
approaches metainference is the only one that can deal with both heterogeneity and errors in the
data; the maximum entropy approach can treat only the former, while standard Bayesian
modelling only the latter.
                               <r>=0.999991

              k [kBT]

                            82 642    1282                             2562
                                                 N2
Figure 3. Scaling of the matainference harmonic restraint intensity in absence of noise in
the data. We verified numerically that in absence of noise in the data, and with a Gaussian noise
                                                                     N
model, the intensity of the metainference harmonic restraint k = ∑ 2 , which couples the
                                                                    r=1 σ r
average of the forward model over the N replicas to the experimental data point (Eq. 7), scales
as N 2 . This test was carried out in the model system at 5 discrete states, with 20 data points and
the prior with accuracy equal to 16%. For each of the 20 data points, we report the average
restraint intensity over the entire Monte Carlo simulation and its standard deviation, when using
8, 16, 32, 64, 128, and 256 replicas. The average Pearson’s correlation coefficient on the 20 data
points is 0.999991 ± 3·10-6, showing that metainference coincides with the replica-averaging
maximum entropy modelling in the limit of absence of noise in the data.
                 a)
                                                                           B
                                                                   B
                                                                           B
                                                                   B
                                                                           B

                 PDF

                 b)
                                                                    B

                 PDF

                                                    B

Figure 4. Analysis of the inferred uncertainties. Distributions of inferred uncertainties in
presence of systematic errors, (A) using a Gaussian data likelihood with one uncertainty per data
point and (B) the outliers model with one uncertainty per dataset. This test was carried out in the
model system at 5 discrete states, with 20 data points (of which 8 were outliers), 128 replicas,
and the prior with accuracy equal to 16%. For the Gaussian noise model, we report the
                                                                    B
distributions of 3 representative points not affected by noise ( σ 1−3 ) and of 2 affected by
systematic errors ( σ 4B and σ 5B ). For the outliers model, we report the distribution of the typical
dataset uncertainty ( σ 0B ).
  a) Input                    b) Ensemble
                                                                      α                                                      βHB+
                                                     D52
                                                                                                               D52
                                                                              E24
                                                              G53                                                 G53                E24

                                                                                    d (E24 NH - D52 CO) (nm)
                                                                     β ~35%                                                         βHB-

                                                                                                                  βHB+
                                                      φ G53

                                                                α ~65%                                                   α

                                                                    ψ D52                                      d (E24 sc - G53 NH) (nm)

  c) Validation
              3J
                HNC
                                     3J
                                       HNHA                    RDCs set 2                                            RDCs set 3

  RMSD (Hz)

Figure 5. Example of the application of metainference in integrative structural biology. (A)
Comparison of the metainference and maximum entropy approaches by modelling the structural
fluctuations of the protein ubiquitin in its native state using NMR chemical shifts and RDC data.
(B) The metainference ensemble supports the finding (36) that a major source of dynamics
involves a flip of the backbone of residues D52-G53 (B, left scatter plot), which interconverts
between an α state with a 65% population and a β state with a 35% population. This flip is
coupled with the formation of a hydrogen bond between the side-chain of E24 and the backbone
of G53 (B, right scatter plot); the state in which the hydrogen bond is present (βHB+) is populated
30% of the time, and the state in which the hydrogen bond is absent (βHB-) is populated 5% of the
time. By contrast the NMR structure (PDB code 1D3Z) provides a static picture of ubiquitin in
this region in which the α state is the only populated one (black triangle). (C) Validation of the
metainference (red) and maximum entropy (green) ensembles, along with the NMR structure
(blue) and the MD ensemble (purple), by the back-calculation of experimental data not used in
the modelling: 3JHNC and 3JHNHA scalar couplings and two independent sets of RDCs (RDCs sets 2
and 3).
                                prior error = 0.08

               PDF

                                        k [kJ/mol]

Figure 6. Distributions of restraint intensities for different chemical shifts of ubiquitin.
When combining data from different experiments, metainference automatically determines the
weight of each piece of information. In the case of ubiquitin, the NH and HN chemical shifts
were determined as the noisiest data and thus downweighted in the construction of the ensemble
of models. At this stage, it is impossible to determine whether these two specific datasets have a
higher level of random or systematic noise, or whether instead the CAMSHIFT predictor (38) is
less accurate for these specific nuclei.
Supplementary Materials

Derivation of the basic metainference equations

1) The metainference posterior in the case of a single experimental data point. Here we derive
Eq. 5 of the main text, which is the general metainference equation in the case of a single
experimental data point d . As discussed in the main text (Materials and Methods), we are
interested in determining how the prior distribution of models (including structural states and
other parameters) is affected by the introduction of experimental information. Since experimental
data in equilibrium conditions are the result of ensemble averages over a distribution of states,
we model a finite sample of the distribution of models, which we refer to as the set of N
replicas of the system. These include: the coordinates of the system X = [X r ] , the averages of
the forward model over an infinite number of replicas f! = [ f!r ] , the uncertainty parameters that
describes random and systematic errors in the experimental data as well as errors in the forward
           B        B                                                 SEM
model σ = [σ r ] , the standard errors of the mean σ                        = [σ rSEM ] .
The metainference posterior probability is thus

     p(X, f! , σ B , σ SEM | d, I )                                                                          (S1)

                                             SEM
We first recognize that X and σ                    do not dependent from the data d . Therefore

      p(X, f! , σ B , σ SEM | d, I ) = p( f! , σ B | d, I ) ⋅ p(X) ⋅ p(σ SEM )                              (S2)

At this point, we should take into account that each set f! = [ f!r ] , σ = [σ r ] , and
                                                                         B     B

σ SEM = [σ rSEM ] is composed of independent variables, and that the configurations X = [Xr ]
are a priori independent. Given these considerations, we can write from Eq. S2

                                       N
      p(X, f! , σ B, σ SEM | d, I ) = ∏ p( f!r , σ rB | d, I )⋅ p(Xr )⋅ p(σ rSEM )                           (S3)
                                      r=1
By applying Bayes theorem to p( f!r , σ rB | d, I ) we can thus derive Eq. 5 of the main text

                                       N
      p(X, f! , σ B, σ SEM | d, I ) ∝ ∏ p(d | f!r , σ rB )⋅ p( f!r | X, σ rSEM )⋅ p(σ rB )⋅ p(Xr )⋅ p(σ rSEM ) (S4)
                                       r=1

2) Gaussian data noise and marginalization. We can further simply Eq. S4 in the case of
Gaussian data likelihood
                                       ⎡      ! 2⎤
      p(d | f!r , σ rB ) =
                                 ⋅ exp ⎢−
                                          d − f(r ⎥    )                              (S5)
                               B
                           2πσ r       ⎢ 2 σB 2 ⎥
                                       ⎣   ( r) ⎦
In this case, we can write
                                                         ⎡      ! 2⎤               ⎡ !            2⎤

 p(d | f!r , σ rB )⋅ p( f!r | X, σ rSEM ) =
                                                   ⋅ exp ⎢−
                                                            d − (
                                                                f r ⎥⋅ 1)    ⋅ exp ⎢−
                                                                                      f r − f (X)    (
                                                                                                   ⎥ (S6)        )
                                            2πσ rB       ⎢ 2 σ B 2 ⎥ 2πσ SEM       ⎢ 2 σ SEM 2 ⎥
                                                         ⎣   ( r) ⎦      r
                                                                                   ⎣      ( r ) ⎦
The product of the two Gaussian probability density functions (PDFs) is a scaled Gaussian PDF

                                                        ⎡ !        2⎤

   p(d | f!r , σ rB )⋅ p( f!r | X, σ rSEM ) =
                                               S
                                                  ⋅ exp ⎢−
                                                           f r −(f  ⎥   )                                             (S7)
                                              2πσ       ⎢    2 σ 2  ⎥
                                                        ⎣           ⎦

where

               B 2         SEM 2                       SEM 2                B 2

   σ=
       (σ ) ⋅ (σ ) and f = d ⋅ (σ ) + f (X)⋅ (σ )
               r           r                           r                    r
                                                                                                                      (S8)
               B 2         SEM 2                          B 2       SEM 2
      (σ ) + (σ )
               r           r     (σ ) + (σ )              r         r

The scaling factor is itself a Gaussian PDF

                                ⎡                     2
                                                            ⎤
               1                ⎢      ( d − f (X)  )       ⎥
    S=                    ⋅ exp ⎢−                          ⎥                                                        (S9)
                (
             SEM 2    B 2
       2π (σ r ) + (σ r )       ⎢
                                ⎣
                                   2 (σ
                                        )SEM 2
                                         r   )  + (σ  (r
                                                        B 2
                                                         )  ⎥
                                                            ⎦               )
Since typically we are not interested in determining f!r , we can marginalize it as

                                                               1          ⎡ ( d − f (X))2 ⎤
    ∫ p(d | f!r , σ rB )⋅ p( f!r | X, σ rSEM )⋅ d f!r = S =   2πσ r
                                                                    ⋅ exp ⎢−
                                                                                 2σ r2
                                                                                          ⎥                          (S10)
                                                                          ⎣⎢              ⎦⎥

                                                                       SEM 2         B 2
where the effective uncertainty parameters σ r =                    (σ ) + (σ ) encodes all sources of error.
                                                                       r             r

If we incorporate Eq. S10 into Eq. S4 we obtain the marginalized version of Eq. 5 that holds for
Gaussian data noise (Eq. 6 in the main text).

3) The metainference posterior in the case of multiple independent data points. We now extend
Eq. S4 to the case of N d independent data points D = [di ] . We thus introduce one f! , σ r,iB , and
  SEM
σ r,i per data point i and replica r . In this case                 f! = [[ f!r,i ]] , σ B = [[σ r,iB ]] , and
σ SEM = [[σ r,iSEM ]] .
                     SEM
Since X and σ               do not dependent from the data D , the posterior can be written as

   p(X, f! , σ B , σ SEM | D, I ) = p( f! , σ B | D, I ) ⋅ p(X) ⋅ p(σ SEM )                                          (S11)
Each set f! = [[ f!r,i ]] , σ
                                     B
                                         = [[σ r,iB ]] , and σ SEM = [[σ r,iSEM ]] is composed of independent
variables, and the configurations X = [X r ] are a priori independent. Therefore we can write

                                              N    Nd                                     N
   p(X, f! , σ B, σ SEM | D, I ) = ∏∏ p( f!r,i , σ r,iB | D, I )⋅ p(σ r,iSEM ) ⋅ ∏ p(Xr )                             (S12)
                                             r=1 i=1                                      r=1

By applying Bayes theorem to the data likelihood p( f!r,i , σ r,iB | D, I ) , we can write

                                          N       Nd                                                         N
 p(X, f! , σ B, σ SEM | D, I ) ∝ ∏∏ p(D | f!r,i , σ r,iB )⋅ p( f!r,i | X, σ r,iSEM )⋅ p(σ r,iB )⋅ p(σ r,iSEM ) ⋅ ∏ p(Xr ) (S13)
                                         r=1 i=1                                                            r=1

We now use the fact that the multiple data points are independent to factorize the data likelihood
                           Nd
  p(D | f!r,i , σ r,iB ) = ∏ p(d j | f!r,i , σ r,iB )                                                                  (S14)
                           j=1

and since the data point d j depends only on f!r, j and σ r, j , we can write
                                                                                 B

                                                         Nd
   p(D | f!r,i , σ r,iB ) = p(di | f!r,i , σ r,iB )⋅ ∏ p(d j ) ∝p(di | f!r,i , σ r,iB )                               (S15)
                                                       j=1, j≠i

By inserting Eq. S15 into Eq. S13 we obtain the metainference equation for the case of multiple
independent data points (Eq. 8 in the main text)

                                         N        Nd                                                        N
 p(X, f! , σ B, σ SEM | D, I ) ∝ ∏∏ p(di | f!r,i , σ r,iB )⋅ p( f!r,i | X, σ r,iSEM )⋅ p(σ r,iB )⋅ p(σ r,iSEM ) ⋅ ∏ p(Xr ) (S16)
                                         r=1 i=1                                                            r=1

Details of the model system simulations.

To assess the accuracy of the different modelling approaches considered in this work, we studied
a model system characterized by multiple discrete states, for which the number of states N S and
their population [w 0 ] can be varied arbitrarily. This system captures some of the complexity of
real mixtures of different species and/or conformations in which equilibrium measurements mix
contributions from all states. A simulation of this model system consists of 4 steps.

1) Generation of states and synthetic experimental data. For each state, we randomly extracted
its population w 0k and N d real numbers di,k in the range from 1.0 to 10.0. These numbers are the
pure experimental data points for each state and they will be used as forward model in the next
                                                                                                NS

step. The pure observed data points are a mixture on all states, di = ∑ w k ⋅ di,k . We introduced

                                                                                                k=1
two types of noise to the pure observed data points to mimic the presence of random and
systematic errors. Random errors were modeled with a Gaussian noise with standard deviation
equal to 0.5, while systematic errors were modeled by adding a random offset in the range from
3.0 to 5.0 to 30% of the data points. We modeled systems of 5 states using 2, 5, 10, and 20 data
points and systems of 50 states using 20, 50, 100, and 200 data points. For both model sizes, we
genereted 4 datasets: (i) without errors, (ii) with only random errors, (iii) with only systematic
errors, and (iv) with both random and systematic errors.

2) Scoring. In metainference, the total energy of the system is defined as

      E = −kBT ⋅ log p ( X, σ | D, I )                                                              (S17)

where we used a Gaussian noise with one uncertainty parameter σ r,i per replica and data point
(Eq. 9) or an outliers model with one uncertainty parameter per dataset (Eq. 11). In both cases,
we used a Jeffrey’s prior p(σ ) =1/ σ for the uncertainty of each data point or for the typical
                                 was kept fixed and equal to σ! SEM / N , with σ!
                           SEM                                                      SEM
dataset uncertainty. σ                                                                    = 5.66. For the
                                         SEM
standard Bayesian modelling, σ       was set to zero. For the replica-averaged approach, we
introduced harmonic restraints to couple forward model predictions to the observed data points.
The intensity of the harmonic restraints was set to k = N 2 ⋅ k1 , with k1 = 0.03. We used the same
prior information for the metainference, standard Bayesian modelling, and replica-averaged
approaches. We randomly perturbed the exact populations w 0k to obtain approximate weights
w k for each state and thus we defined the energy associated to the prior information as
E = −kBT ⋅ log w k . To study the effect of the prior accuracy, we created high and low accuracy
  k

priors, with an average population error per state equal to 0.08 and 0.16, respectively.

3) Sampling. We simulated N copies of the system to benchmark the metainference and replica-
averaged approaches, and a single replica for standard Bayesian modelling. In the former case,
we used 8, 16, 32, 64, and 128 replicas. The following unknown variables were sampled by
Monte Carlo; a discrete index that determines which state of the system is occupied and the data
uncertainty parameters for metainference and standard Bayesian modelling. The data uncertainty
parameters were sampled in the range 0.00001-200, by proposing random moves at most equal to
10.0. kBT was set to 1.0. A total of 50,000 Monte Carlo steps were carried out in each simulation.

4) Analysis. During each Monte Carlo simulation we accumulated the histogram of the discrete
variable that indicates which state of the system is istantaneously populated. From this
histogram, we calculated the population of each state w! k determined from prior information and
experimental data. We defined as accuracy the root mean squared deviation of [ w! k ] from the
exact populations [wk0 ] . For each approach to test and choice of parameters (number of data
points, level of noise in the data, and number of replicas), we run 300 indipendent simulations
with random reference state populations and data points. The reported accuracy is averaged over
the 300 simulations.
Details of the molecular dynamics simulations of ubiquitin

Classical all-atom molecular dynamics simulations of ubiquitin were perfomed using
GROMACS (33) together with PLUMED (34). The X-ray structure 1UBQ (29) has been used as
starting point in the simulations, using the CHARMM22* force field (35), in a cubic box of 6.3
nm of side with 7800 TIP3P water molecules (39). A time step of 2 fs was used together with
LINCS constraints (40). The van der Waals and Coulomb interactions were cut-off at 0.9 nm,
while long-range electrostatic effects was treated with the particle mesh Ewald method. All
simulations were carried out in the canonical ensemble by keeping the volume fixed and by
thermosetting the system at 300 K with the Bussi-Donadio-Parrinello thermostat (41). A 1 ms
molecular dynamics simulation was perfomed as a reference sampling of the a priori information
of the CHARMM22* force field.

Maximum entropy replica-averaged simulations and metainference replica-averaged simulations
were perfomed using backbone chemical shifts (bmr17760) and residual dipolar couplings
measured in a liquid-crystallin phase (N-H, Cα-Hα, Cα-C′, C′-N, C′-H and Cα-Cb bonds) as
structural restraints modelled with CamShifts and the exact ϑ-method, respectively. Maximum
entropy and metainference simulations were performed using 8 replicas, in all cases for a total
simulation time of 1 ms, consistently with the reference sampling. A Gaussian noise model with
one error parameter per nucleus was used in the metainference approach, along with a Jeffrey’s
prior on each error parameter.

From the resulting ensembles we back-calculated chemical shifts using SPARTA+ (42), RDCs
measured in a large number of conditions (32) using PALES in the SVD approximation (43)
using only data for residues 1 to 70 to obtain the alignment tensor. Scalar couplings across
hydrogen bonds have been calculated as h3JNC = (-357 Hz)exp(-3.2rHO/Å)cos2θ where θ
represents the H…O=C angle (44), while H-Hα scalar coupling have been calculated using the
Karplus equation with previously reported parameters (45). In addition the presence of distorted
geometries have been tested with PROCHECK (31). The ensembles have been also compared
with the 1UBQ X-ray (29) and the 1D3Z NMR (30) structures.
a)                 prior error = 0.08              b)           prior error = 0.16

 Error

                          # data                                        # data

Figure S1. Effect of prior accuracy on the error of the metainference method. Metainference
error as a function of the number of data points and for varying levels of noise in the data in the
case of prior with average error in the state populations equal to 0.08 (A) and 0.16 (B). The
quality of the prior information influences the number of data points required to achieve a given
accuracy of the inferred state populations. The more accurate is the prior, the fewer data points
are needed. These simulations were carried out on a 5-state model, using 128 replicas.
          Error

                                            # replicas
Figure S2. Scaling of metainference error with number of replicas for varying level of noise
in the data. As the number of replicas increases, the statistical error in calculating ensemble
averages with a finite number of replicas converges to zero, and the overall accuracy of
metainference increases. These simulations were carried out on a 5-state model, using 20 data
points and the prior with average error equal to 0.16.
a)                      5 states                  b)                50 states

 Error

                         # data                                        # data

Figure S3. Scaling of metainference error with number of states. The metainference error as
a function of the number of data points and for varying levels of noise in the data for a system
composed of 5 (A) and 50 (B) states. These simulations were carried using 64 replicas and the
prior with average error equal to 0.08.
a)                  outliers model                 b)            multiple sigmas

 Error

                          # data                                        # data

Figure S4. Accuracy of the outliers model. Metainference error as a function of the number of
data points and for varying levels of noise in the data with an outlier model for the errors that
uses a single error parameter per dataset (A) and with one error parameter per data point (B).
These simulations were carried out on a 5-state model, using 128 replicas and the prior with
average error equal to 0.16.
                         Maximum
           Score                        Metainference           NMR        MD             X-ray
                          entropy
                                                   Modelling
         Chemical
          shifts
           CA               0.76            0.72                0.63       0.90            0.71
           CB               0.89            0.93                0.89       1.12            0.94
           CO               0.80            0.81                0.75       0.93            0.80
           HA               0.13            0.13                0.21       0.23            0.17
           HN               0.34            0.39                0.40       0.44            0.39
           NH               2.51            2.32                1.86       2.77            2.03
         RDC set 1
            NH              0.16            0.15                0.19       0.27            0.21
            CAC             0.13            0.13                0.27       0.23            0.31
           CAHA             0.15            0.15                0.13       0.23            0.28
             CN             0.15            0.14                0.23       0.24            0.21
             CH             0.52            0.18                0.29       0.31            0.32
                                                   Validation
              JHNC
           RMSD             0.26            0.17                0.30       0.15            0.22
             JHNHA
           RMSD             1.08            0.89                0.69       0.99            0.89
         RDC set 2
          NH(36)            0.23            0.20                0.29       0.28            0.29
         RDC set 3
            NH              0.32            0.24                0.24       0.24            0.29
            CAC             0.27            0.22                0.28       0.24            0.32
           CAHA             0.37            0.33                0.40       0.32            0.42
             CN             0.27            0.23                0.28       0.32            0.33
             CH             0.34            0.26                0.51       0.34            0.47

Table S1. Comparison of the quality of the ensembles obtained using different modelling
approaches in the case of the native state of the protein ubiquitin. Maximum entropy and
metainference indicate the ensembles generated in this work using 8 replicas and chemical shifts
combined with RDCs. NMR, MD and X-ray indicate a structure determined using high-resolution NMR
methods (PDB code 1D3Z (30)), an ensemble determined by standard molecular dynamics simulations,
and a X-ray structure (1UBQ) (29), respectively. In the upper part of the Table (“Modelling”) we report
the fit with the data used in the modelling, in the lower part (“Validation”) the fit with independent data
not used in the modelling.
                  Maximum
        Score                   Metainference      NMR            MD             X-ray
                  Entropy

      Procheck
       RAMA           1.6            1.2            1.0            1.0            1.0
      HBGEO           2.3            1.9            1.4            2.1            1.7
       CHI-1          1.4            1.4            1.0            1.3            2.0
       CHI-2          1.0            1.0            1.0            1.0            1.4
      OMEGA           2.5            2.0            1.0            2.0            1.0

Table S2. Comparison of the stereochemical quality of the ensembles or single models generated
by the approaches defined in Table S1. The quality was assessed with PROCHECK (31).


---

# Convergent views on disordered protein dynamics from NMR and computational approaches

**Authors:** Nicola Salvi, Vojtěch Zapletal, Zuzana Jaseňáková, Milan Zachrdla, Petr Padrta, Subhash Narasimhan, Thorsten Marquardsen, Jean-Max Tyburn, Lukáš Žídek, Martin Blackledge, Fabien Ferrage, Pavel Kadeřávek
**Year:** 2022
**Venue:** Biophysical Journal
**DOI:** 10.1016/j.bpj.2022.09.016
**Source PDF URL:** https://europepmc.org/articles/PMC9674986?pdf=render
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Article

Convergent views on disordered protein dynamics
from NMR and computational approaches
Nicola Salvi,1 Vojt                         áková,2 Milan Zachrdla,3 Petr Padrta,4 Subhash Narasimhan,2
                   ech Zapletal,2 Zuzana Jasen
                                                   
Thorsten Marquardsen, Jean-Max Tyburn, Lukás Zı́dek,
                        5                  6               2
                                                             Martin Blackledge,1,* Fabien Ferrage,3,*
and Pavel Kaderávek4,*
  Institut de Biologie Structurale (IBS), CEA, CNRS, University Grenoble Alpes, Grenoble, France; 2National Centre for Biomolecular Research,
Faculty of Science and Central European Institute of Technology, Masaryk University, Brno, Czech Republic; 3Laboratoire des Biomole   cules,
LBM, De   partement de chimie, École normale superieure, PSL University, Sorbonne Universite, CNRS, Paris, France; 4Central European
Institute of Technology, Masaryk University, Brno, Czech Republic; 5Bruker BioSpin GmbH, Rheinstetten, Germany; and 6BioSpin,
Wissembourg Cedex, France

ABSTRACT Intrinsically disordered proteins (IDPs) or intrinsically disordered regions (IDRs) is a class of biologically important
proteins exhibiting specific biophysical characteristics. They lack a hydrophobic core, and their conformational behavior is
strongly influenced by electrostatic interactions. IDPs and IDRs are highly dynamic, and a characterization of the motions of
IDPs and IDRs is essential for their physically correct description. NMR together with molecular dynamics simulations are
the methods best suited to such a task because they provide information about dynamics of proteins with atomistic resolution.
Here, we present a study of motions of a disordered C-terminal domain of the delta subunit of RNA polymerase from Bacillus
subtilis. Positively and negatively charged residues in the studied domain form transient electrostatic contacts critical for the bio-
logical function. Our study is focused on investigation of ps-ns dynamics of backbone of the delta subunit based on analysis of
amide 15N NMR relaxation data and molecular dynamics simulations. In order to extend an informational content of NMR data to
lower frequencies, which are more sensitive to slower motions, we combined standard (high-field) NMR relaxation experiments
with high-resolution relaxometry. Altogether, we collected data reporting the relaxation at 12 different magnetic fields, resulting in
an unprecedented data set. Our results document that the analysis of such data provides a consistent description of dynamics
and confirms the validity of so far used protocols of the analysis of dynamics of IDPs also for a partially folded protein. In addition,
the potential to access detailed description of motions at the timescale of tens of ns with the help of relaxometry data is dis-
cussed. Interestingly, in our case, it appears to be mostly relevant for a region involved in the formation of temporary contacts
within the disordered region, which was previously proven to be biologically important.

  SIGNIFICANCE Dynamics of proteins is essential for their function in biological systems. The importance of the
  dynamics is even more pronounced in the case of intrinsically disordered proteins (IDPs), which lack a stable three-
  dimensional structure and are highly flexible. A combination of analyses of molecular dynamic simulations and NMR
  relaxation data provides detailed information about the motions at the ps-ns timescale, but sampling of slower motions is
  limited. We are presenting an approach overcoming this limitation by employing high-resolution relaxometry as
  demonstrated for a case study of the delta subunit of RNA polymerase from Bacillus subtilis, where it is used to describe
  biologically relevant dynamics of its C-terminal domain involved in regulation of transcription.

                                                                            INTRODUCTION
                                                                            Proteins are dynamic biomolecules that feature motions
Submitted June 11, 2022, and accepted for publication September 15, 2022.
                                                                            occurring on timescales from ps to days. It is widely
*Correspondence: martin.blackledge@ibs.fr or fabien.ferrage@ens.psl.eu      accepted that the problem of describing the functional
or pavel.kaderavek@mail.muni.cz                                             mechanisms of a protein is essentially equivalent to
Nicola Salvi’s present address is Bio Structure and Biophysics (BSB), Sa-   the problem of describing its functional dynamics with
nofi R&D, 94400 Vitry-sur-Seine, France.                                    sufficient accuracy (1). This statement is particularly rele-
Thorsten Marquardsen is deceased.                                           vant in the case of intrinsically disordered regions (IDRs)
Editor: Scott Showalter.                                                    and intrinsically disordered proteins (IDPs), which lack a
https://doi.org/10.1016/j.bpj.2022.09.016
Ó 2022 Biophysical Society.
This is an open access article under the CC BY-NC-ND license (http://
creativecommons.org/licenses/by-nc-nd/4.0/).

                                                                               Biophysical Journal 121, 3785–3794, October 18, 2022 3785
Salvi et al.

well-defined three-dimensional fold and are best described       tribution of correlation times for chain-like motions from
by an ensemble of diverse conformations sampled in solu-         the analysis of relaxation rates measured at high magnetic
tion (2,3). A direct yet often unclear link between the struc-   fields (5). It is still unclear whether the presence of addi-
tural ensemble of an IDP, the dynamics of interconversion        tional motions is masked by the particular range of time-
between conformers within such ensemble, and protein             scales HF spin relaxation is intrinsically most sensitive to,
function exists. The development of approaches to describe       even when multiple HFs are combined. Because the sensi-
this link has been the subject of considerable research effort   tivity of NMR relaxation depends on the available transition
in recent years (4–11).                                          frequencies of the spin system of interest, the range of mag-
   Among the experimental techniques applied to IDPs,            netic fields at which relaxation is measured defines the range
NMR spectroscopy is unique in providing multiple probes          of timescales of the motions that can be probed by a partic-
of dynamics, effectively covering most timescales from ps        ular set of relaxation rates (17–22). Measurements of 15N
to days with atomic resolution. In particular, in the present    relaxation at magnetic fields from 9.4 to 28 T can, in princi-
work, we focus on motions occurring on tens of ps to tens        ple, probe motions in the range of tens of ps to tens of ns,
of ns. Dynamics on these timescales is conveniently probed       with limited sensitivity above a few ns. The accurate and
by nuclear spin relaxation. High magnetic fields are, in gen-    sensitive determination of motions slower than a few ns
eral, required to obtain sufficient spectral resolution and      timescales requires measurement at magnetic fields lower
sensitivity in complex biomolecules, so relaxation is            than those allowed by high magnetic fields. Relaxation mea-
conventionally measured at high (>9.4 T) magnetic field          surements have already been performed over a much
(high-field [HF]) strengths in the case of proteins.             broader range of magnetic fields down to 0.5 mT by sacri-
   More precisely, spin relaxation probes the spectral den-      ficing high-resolution and thus the ability to assign motions
sity function J(u) which is the Fourier transform of the cor-    to any particular region of a protein (23).
relation function, describing the power dissipated by the           Recently, high-resolution relaxometry, which combines
fluctuations as a function of frequency u. Measured spin         relaxation at low magnetic fields and detection at high
relaxation rates depend on the spectral density function         magnetic fields, emerged as a promising tool to expand
evaluated at specific u values dictated by spin physics, usu-    the sampling of the spectral density function to otherwise
ally the interaction of nuclear spins with the strong magnetic   inaccessible u values while preserving the resolution and
field of the NMR magnet. For example, in the case of the         sensitivity of high-field NMR. Applications of high-resolu-
relaxation of 15N spins in the backbone of a protein used        tion relaxometry to small folded proteins have demonstrated
extensively in the present work, measured relaxation rates       enhanced sensitivity to motions with correlations times of
depend on linear combinations of the spectral density func-      hundreds of ps to a few ns, both on the backbone (24,25)
tion evaluated at the following frequencies: 0, the Larmor       and side chains (26,27).
frequency of 15N spins (uN ) and that of 1H spins (uH ). As         Insight into the nature of dynamic fluctuations that is
both uN and uH are proportional to the magnetic field            complementary to experimental NMR studies can be pro-
strength B0 , it is evident that a strategy to maximize the      vided by molecular dynamics (MD) simulations. In fact,
amount of information that can be extracted from relaxation      MD trajectories are used to calculate rotational autocorrela-
studies is to measure relaxation at as many B0 values as         tion functions of NH bond vectors (and consequently J(u)
possible, as availability of instruments, resolution, and        values) describing the reorientational properties of relaxa-
sensitivity requirements allow. It has been shown in a num-      tion-active interactions such as dipole-dipole couplings
ber of systems and experimental conditions (4,5,7,12,13)         and chemical shift anisotropy (CSA), thereby providing a
that HF relaxation data measured on disordered proteins at       direct and quantitative way of comparing simulated dy-
multiple fields can be convincingly interpreted in the frame-    namics with experimental spin relaxation rates. In the case
work of (extended) model-free (MF) analysis (14), whereby        of unfolded proteins, MD simulations have been shown to
the spectral density function is decomposed into the sum of      be largely consistent with the three-timescale model derived
three Lorentzian components, characterized by their ampli-       from MF studies (9,28,29).
tudes (Ai ) and timescales (t i ). These three components are       In this work, we perform high-resolution relaxometry, HF
associated with fast bond librations on tens of ps, intermedi-   spin relaxation measurements, and MD simulations on a
ate sampling of backbone dihedral angles on hundreds of ps,      particularly challenging half structured and half disordered
and slower chain-like motions occurring on timescales of         d subunit of RNA polymerase. The d subunit of RNA poly-
several ns (9,12).                                               merase is a subunit unique for Gram-positive bacteria that
   The timescales of these chain-like motions have been pro-     was shown to be essential for virulency of some pathogens
posed to follow a continuous distribution (15,16). An anal-      like Streptococcus agalactiae and Staphylococcus aureus
ysis based on the interpretation of motions by projection        (30), and it was demonstrated that the d subunit causes a sensi-
onto an array of correlation times (IMPACT), which uses          tivity of RNA polymerase activity to the concentration of initi-
a discretized distribution of correlation times, could not       ating nucleoside triphosphates, making the d subunit essential
identify slower motional modes or a possible tail of the dis-    for rapid changes of gene expression (31). Here, the d subunit

3786 Biophysical Journal 121, 3785–3794, October 18, 2022
                                                                                                                      IDPs dynamics by NMR and MD

of a model Gram-positive bacteria Bacillus subtilis is investi-                nonuniformly sampled (for 15N and 13C dimensions) spectra with varying
gated. The d subunit is composed from two domains: the                         relaxation delays (summarized in Table S1) were acquired for each
                                                                               magnetic field in an interleaved manner as a pseudo-four-dimensional
N-terminal domain has a well-defined structure formed by a                     experiment (experimental relaxometry relaxation rates are available in
core of three a-helices, while the C-terminal domain is disor-                 Tables S2–S4). An in-house program was used to generate the NUS
dered (32), and it does not show any propensity to form any                    schedule using Poisson discs sampling (38) with the Gauss-function used
secondary structure element within its sequence. The C-termi-                  to weight the density of sampled points. A complete set of real and imag-
nal domain is highly negatively charged except a lysine-rich                   inary components for quadrature detection in indirect dimensions were ac-
                                                                               quired, each of them measured with four scans to accumulate the signal.
motif 96KAKKKKAKK104 involved in the formation of tran-                        Additional details about the experimental setup of the high-resolution relax-
sient electrostatic contacts with negatively charged amino                     ometry measurements can be found in Table S1.
acids in the remaining parts of the C-terminal domain (32).                       Experiments for the determination of proton exchange rates with the sol-
   We combine high-resolution relaxometry measurements                         vent were carried out according to the RELAX-EXSY protocol (39) on
with HF spin relaxation data to probe as broad a range of                      samples of the delta subunit with identical composition but different con-
                                                                               tents of D2O (1%, 10%, 30%, and 50% contents of D2O was used). These
correlation times as possible in the disordered domain of                      experiments were carried out on a 600 MHz NMR spectrometer equipped
the d subunit of RNA polymerase. Although the high-field                       with a cryo-cooled 5 mm TCI probe. Relaxation delays of 44.8, 179.2,
dataset analyzed here is relatively sparse, this combination                   380.8, 627.2, and 1,030.4 ms were used.
also provides us with the opportunity to assess whether                           Steady-state nuclear Overhauser effect (NOE) experiment and measure-
low-field measurements can identify additional dynamic                         ment of longitudinal relaxation rates were carried out on an 850 MHz NMR
                                                                               spectrometer equipped with a cryo-cooled 5 mm TCI probe (BMRB: 27245)
processes to those derived from uniquely HF spin relaxation                    using the published pulse sequence for uniformly 15N and 13C labeled disor-
or indeed whether this information can be refined by prob-                     dered proteins (40). The longitudinal relaxation rates were measured with
ing the spectral density function at lower frequencies. We                     relaxation delays 0.0448, 0.0672, 0.112, 0.1792*, 0.2464, 0.3808, 0.784, and
find that all measurements are consistent and mostly report                    1.232 s (the asterisk denotes the spectra repeated twice). The saturation in
on the same three motional processes described above. This                     the steady-state NOE experiment was achieved with 5 s irradiation composed
                                                                               from inversion proton pulses separated by 22.22 ms, and the reference exper-
observation is confirmed by a detailed analysis of motions                     iment was measured with a 15 s interscan delay (41).
sampled by multi-ms MD simulation. Our results indicate
that small inconsistencies between the analyses of relaxa-
tion data measured at low and high field would be the                          NMR processing and data analysis
hallmark of IDP dynamics more complex than the state-
                                                                               All NMR spectra were processed using NMRpipe (42) software v.9.9 and
of-the-art MF model.                                                           SMILE 2.0beta (43) for the nonuniformly sampled spectra.
                                                                                  No extrapolation (NUS zero-filling) was used in the processing of the
                                                                               nonuniformly sampled data, and the same signal downscaling factor was
MATERIALS AND METHODS                                                          used for the independently processed spectra of various relaxation delays.
                                                                               The spectra were analyzed using the program NMRFAM-Sparky 1.413
Sample preparation
                                                                               (44). The extracted peak intensities of the high-resolution relaxometry
The d subunit of RNA polymerase was prepared as uniformly 15N and 13C          spectra were fitted to mono-exponential decay functions in the Octave
labeled recombinant protein expressed in Escherichia coli BL21(DE3)            3.8.2 program (45) using the function leasqr from the package optim.Errors
strain. The purification protocol is described elsewhere (33). NMR samples     of the fitted relaxation rates were estimated based on the smooth Bootstrap
contain 1.2 mM of the protein in 20 mM phosphate buffer (pH ¼ 6.6; un-         method (46,47). 300 Monte Carlo simulations for each Bootstrap sample
corrected reading) and 10 mM NaCl and 10% D2O.                                 were generated based on the estimated error of the peak intensities from
   Prepared NMR samples were degassed upon mild vacuum and sealed in a         the noise in the spectra. The steady-state NOE was determined from the ra-
special tube (25) for the high-resolution relaxometry experiments. The         tio of the peak intensities in the spectra acquired with saturation and refer-
design of the tube was modified compared with the reported prototype           ence spectra. The error of signal intensities was estimated from the noise.
(25) to increase the active sample volume to 120 mL. HF NMR experiments        The longitudinal relaxation rates were fitted in the Octave 4.0.3 program
were measured in standard 5 mm NMR tubes.                                      (45), and the error was obtained by Bootstrap method.

NMR measurements                                                               Analysis of relaxation rates
All NMR experiments were performed at (300.0 5 0.2) K, which was cali-         The high-resolution relaxometry rates were combined with previously pub-
brated using temperature standards before every measurement.                   lished longitudinal relaxation rates and steady-state NOE acquired at
   High-resolution relaxometry relaxation rates were acquired with a 600       500 MHz spectrometer; longitudinal relaxation rates, steady-state NOE,
MHz spectrometer equipped with a special 3.2 mm room-temperature               and transverse and longitudinal cross-correlated cross-relaxation rates
TXI probe and a shuttling device (25). The shuttling device allows sample      measured at 600 MHz (using a uniformly 15N labeled sample (4)); longitu-
movement along the bore of the magnet in order to reach a position corre-      dinal relaxation rates, steady-state NOE, and longitudinal and transverse
sponding to any desired magnetic field between 0.01 and 14.1 T, at which       cross-correlated cross-relaxation rates acquired with 13C, 15N labeled sam-
relaxation rates are to be measured. The pulse sequence for the measure-       ple at 600 MHz (40); and longitudinal relaxation rates and steady-state
ment of high-resolution relaxometry rates (Fig. S1) is derived from the pre-   NOE measured with the identical 13C, 15N labeled sample at 850 MHz.
viously published pulse sequence for the determination of relaxation rates     Transverse auto-relaxation rates were not used in this analysis due to
at 0.33 T using a two-field NMR spectrometer (34–37). 15N longitudinal         possible contributions of chemical exchange (4), resulting in one single
relaxation rates R1 were measured at nine magnetic fields: 0.10, 0.33,         high-resolution relaxation rate that reports on J(0). Errors of the relaxation
0.67, 1.00, 1.46, 2.00, 2.50, 4.00, and 6.00 T. Three-dimensional HNCO         rates were estimated to be at least 2% of the relaxation rate.

                                                                                   Biophysical Journal 121, 3785–3794, October 18, 2022 3787
Salvi et al.

   The measured relaxometry relaxation rates and high-field relaxation rates         dimensional experiments using the HNCO correlation; the
were analyzed using the IMPACT approach (5). The relaxometry relaxation              benefit of a better resolution is documented in Fig. S2).
rates were corrected via the ICARUS protocol (25,48) to consider the ef-
fects of cross-relaxation during the sample shuttle transfers, stabilization
                                                                                        The ICARUS-IMPACT analysis of the experimental data
delays, and relaxation delays during the measurements. A 1 ms time step              results in a description of the spectral density function in the
was used in the ICARUS correction simulation. The accurate low-field                 form of J(u) ¼ 0.4 Si Bi Ti/(1 þ (u Ti)2) with i ¼ 1–7. The
(0.33 T) relaxation rates measured in a two-field NMR spectrometer (37)              seven Ti values span the range between 11 ps and 70 ns and
were not used in the analysis, so they could serve as an independent verifi-         are equidistant on a logarithmic scale (correlation times
cation of the ICARUS correction procedure.
   The applied IMPACT method follows the originally outlined methodol-
                                                                                     approximately 0.01, 0.05, 0.2, 0.9, 4, 16, and 70 ns). Exper-
ogy (5), but the analysis protocol was extended, and a grid search for the           imental data and back-calculated values are in excellent
optimal ratio (ranging between 200 and 10,000 with steps of 200) between             agreement (Fig. S3–S5). The correction factors applied to
the smallest and the largest correlation time (ranging between 10 and 120 ns         consider the cross-relaxation pathways during the relaxom-
with steps of 10 ns) was included. The analysis was performed using in-              etry experiment range from 3.0% to 11.5% depending on the
house script written in Mathematica 10.1.0 (49). The error of the optimized
parameters of the selected variant of J(u) was estimated based on 4,000
                                                                                     experimental setup (the corrected relaxometry relaxation
Monte Carlo simulations. The IMPACT analysis was also performed for                  rates are in Tables S5–S7). These values are consistent
individual residues separately using high-field data and the corrected relax-        with those previously reported for ubiquitin (25). To further
ometry relaxation rates obtained after the last iteration of the ICARUS-             verify the accuracy of the correction factors derived from
IMPACT analysis.                                                                     the ICARUS procedure, we compared the relaxometry
   MF analysis was carried out as previously described (12). Briefly, exper-
imental relaxation rates were modeled using a spectral density function of
                                                                                     relaxation rates measured at 0.33 T with longitudinal relax-
the form J(u) ¼ 0.4 Si Ai ti/(1 þ (u ti)2), in which i ¼ 1–3, the sum of the         ation rates measured at the same field (37) with a two-field
three amplitudes Ai is constrained to 1, and t1 is fixed to 45 ps. Three Lor-        NMR spectrometer (34,35), in which the effect of cross-
entzian terms have been used because this number provided the best fit for           relaxation pathways can be removed by means of 13C and
all residues in previous studies of disordered proteins (7,12). Thus, the            proton inversion pulses during the relaxation delay (36).
model effectively contains only four parameters to be determined (two am-
plitudes and two timescales). Monte Carlo simulations were used to quan-
                                                                                     While uncorrected high-resolution relaxometry rates are
tify the error bars on fitted parameters. Chemical shielding tensor of amide         systematically lower than the values acquired suppressing
   N was defined following published analysis (50) with the angle between            cross-relaxation pathways (Fig. 1 a), the correction factors
the main tensor component and 15N-1H bond set to 21 (4).                            derived from the ICARUS protocol effectively restore a
                                                                                     quantitative agreement with the data measured at a two-field
MD simulations                                                                       NMR spectrometer (Fig. 1 b). Therefore, these correction
                                                                                     factors are used throughout this work.
MD simulations were performed with the software Gromacs 5.0 (51) using the              The result of IMPACT analysis provides insight into the
force-field Amber99SB_ILDN (52). The simulations were run with explicit
                                                                                     distribution of timescales of motions. Of the seven fixed
solvent water molecules TIP4P-D (6). The choice of the setup reflected previ-
ous analysis of the effect of the force-field and water molecule models (53).        timescales, only four appear to contribute significantly to
Thirteen MD trajectories were calculated with various initial conformations          the spectral density function. The fastest motions on the or-
of the C-terminal domain. The starting structures are representative of the          der of several tens of ps B1 and B2 have a cumulated ampli-
structural flexibility of the C-terminal domain, and they covered both extended      tude of about 0.3, with little if any sequence dependence
conformations of the C-terminal domain and a more compact state that fea-
                                                                                     (Fig. 2 a shows the joint amplitudes B1þB2; separated plots
tures transient electrostatic interactions between the IDR and the folded N-ter-
minal domain. The charge of the system was neutralized using sodium and              for B1 and B2 can be found in Fig. S6). B4 amplitudes, asso-
chloride ions, and additional Naþ and Cl ions were added to match the exper-        ciated with a timescale close to 1 ns (Fig. 2 c), are the largest
imental NaCl concentration (10 mM). The appropriate protonation of side              contribution to relaxation for most residues and appear to
chains in the MD simulations was checked experimentally by pH titration in           monotonically increase from the end of the N-terminal
the range 8 to 5.4 and analysis of the chemical shifts of side-chain carbons (54).
                                                                                     folded domain to the C-terminus, indicating a gradual
   Each trajectory was divided into 22 nonoverlapping segments of variable
length (100–120 ns). For each segment, the rotational correlation function           reduction of the effect of the folded domain on the dynamics
of each NH bond vector was calculated and fitted to a predefined grid of             of the IDR, despite the presence of long-range contacts of
timescales as previously described (8).                                              electrostatic nature (55). Finally, the fifth component associ-
                                                                                     ated with a timescale of the order of several ns (Fig. 2 d) is
                                                                                     an important driver of relaxation for the residues close to the
RESULTS AND DISCUSSION
                                                                                     folded domain and those including and surrounding the
Remarkably, in spite of very limited signal dispersion (32)                          lysine-rich stretch (K-tract, K96–K104), which is involved
and technical challenges associated with the high-resolution                         in charge-mediated interactions (55).
relaxometry setup, resolution and sensitivity of the high-res-                          Of the remaining three timescales, values of B3 ¼ 0.1 are
olution relaxometry experiments were sufficient to probe                             found for all residues outside the K-tract (Fig. 2 b), indi-
dynamics of 68 out of 90 nonproline residues in the disor-                           cating that relatively fast dynamics might be quenched by
dered region of the delta subunit (in order to achieve spectra                       long-range interactions in the K-tract. Similarly, nonzero
with well-resolved peaks suitable for a quantitative analysis,                       values of B6 are found in the proximity of the folded
we performed relaxation measurements as pseudo-four-                                 domain (Fig. 2 e), probably to compensate for the fact that

3788 Biophysical Journal 121, 3785–3794, October 18, 2022
                                                                                                          IDPs dynamics by NMR and MD

          a                                                                deviate from the monotonous dependence of the amplitudes
                                                                           on the correlation times of the Zimm model for polyelectro-
                                                                           lytes (59). It documents a strong effect of electrostatic con-
                                                                           tacts on the conformation of the C-terminal domain of the
                                                                           delta subunit studied previously by small angle X-ray scat-
                                                                           tering and paramagnetic relaxation enhancement (32,55).
                                                                              In order to characterize the extent of slow ns dynamics and
                                                                           quantify their potential contributions to NMR relaxation from
                                                                           a theoretical standpoint, we performed a pool of MD simula-
                                                                           tions as described in the materials and methods section and
                                                                           calculated relaxation rates averaged across the pool (Fig. S8
                                                                           and S9). While the simulation is in good agreement with
                                                                           experimental relaxometry data, longitudinal relaxation rates
                                                                           measured at HF are systematically overestimated by the simu-
                                                                           lation, whereas the only rate that depends on J(0) in our data-
          b
                                                                           set—the CSA/dipole-dipole cross-correlated cross-relaxation
                                                                           rates hxy measured at 600 MHz—is significantly higher in the
                                                                           experiment than in the simulation. Taken together, these two
                                                                           observations indicate that protein dynamics are excessively
                                                                           fast in the simulation compared with in the experiment. We
                                                                           attribute this quantitative disagreement between experiment
                                                                           and simulation to our choice of water model (TIP4P-D),
                                                                           which has been shown to promote excessive flexibility in
                                                                           both folded and unfolded proteins (10).
                                                                              We applied the average block selection using relaxation
                                                                           data (ABSURD) method to select, among the segments of
                                                                           trajectories in our pool, a subset of trajectories minimizing
                                                                           the root-mean-square deviation between experimental and
                                                                           simulated data (8). This approach accounts for conforma-
FIGURE 1 Correlation of the relaxation rates measured at 0.33 T            tional variability across conformers interconverting on time-
(experimental uncertainties are indicated by error bars). Correlation of   scales faster than the coalescence limit while filtering for
the longitudinal relaxation rates R12FNMR measured with two-field NMR      poor sampling of slower motional modes responsible for un-
spectrometer and the relaxometry decay rates R1relaxometry (a) and their
corrected values R1corrected (b).
                                                                           stable averaging of the autocorrelation function. All rates
                                                                           measured at 500, 600, and 850 MHz except heteronuclear
                                                                           NOEs were combined in the ABSURD target function for
T5 ¼ 3.81 ns is smaller than the actual rotational correlation             selection. Somewhat disappointingly, we obtain a suben-
time of the folded N-terminal domain tc ¼ 5 ns based on hy-                semble of four out of a total of 44 segments. In addition,
drodynamical calculations (56,57) (estimated for N-termi-                  simulated relaxation rates evaluated from this subensemble
nal domain of the d subunit alone; the comparison of the                   (Figs. S10 and S11) are very close to those averaged over the
relaxation data acquired for the separated N-terminal                      entire pool, indicating that protein dynamics are accelerated
domain (58) and the full length d subunit (4) shows a negli-               in the entire pool of trajectories to a similar degree,
gible effect of the C-terminal domain on the rotational diffu-             rendering the ABSURD selection process very inefficient.
sion of the N-terminal domain). This effect is similar to the              Although the experimental sequence dependence of relaxa-
one observed in the IMPACT analysis of HF relaxation data                  tion rates presented in Figs. S8–S11 is qualitatively repro-
measured on the partially disordered Engrailed2 (5). Finally,              duced by the ABSURD ensemble of trajectories, there are
the parameter B7 (Fig. 2 f), associated with a correlation                 systematic differences that appear to report on systematic
time on the orders of several tens of ns features very small               errors in the depiction of both ns motions (only one high-
values throughout the sequence. While these values are                     field longitudinal rate is correctly reproduced, the 500 and
significantly different from zero for residues 110 to 135,                 600 MHz R1 values are clearly not) and, most severely,
which might suggest a tail of the distribution of correlation              the unique probe of slower motions (hxy). Under these con-
times with a nonzero density for correlation times t > T6 ¼                ditions, it would be hazardous to over-interpret the fact that
16.3 ns, they never represent more than 1% of the angular                  relaxometry data are, apparently serendipitously, actually
correlation function/spectral density function. Similar con-               quite well reproduced by the simulation.
clusions can be obtained from the analysis done on a per-                     In an attempt to shed further light on the shortcomings of
residue basis (the results are shown in Fig. S7). The results              the simulation, we compare the dynamic fingerprint of the

                                                                              Biophysical Journal 121, 3785–3794, October 18, 2022 3789
Salvi et al.

 a                                                                              b

 c                                                                              d

 e                                                                              f

FIGURE 2 Fitted coefficients Bi (with error bars) used to model the distribution of the timescales. The coefficients are related to the terms of the spectral
density function associated with correlation times 11 and 48 ps taken together (a), 0.2 ns (b), 0.9 ns (c), 3.8 ns (d), 16.3 ns (e), and 70 ns (f).

protein derived from the IMPACT analysis (Fig. 2) with an                           the simulation to be accurate, that the derived timescale of
analog fingerprint extracted from the simulation.                                   50 ps often found in IDPs irrespective of their sequence
    To do so, for each NH bond vector, we average the rota-                         and length (12,13) is in fact a value representative of a dis-
tional correlation functions calculated for each segment and                        tribution of fast dynamics. In the IDR, we find two addi-
fit the averaged autocorrelation function to a predefined grid                      tional motional processes, one around 1 ns and a slower
of 128 timescales as previously described (8). The results of                       one, around 4 ns, that identify with the fourth and fifth
the fit are shown in Fig. 3. Besides a minor component at                           component of the IMPACT analysis, respectively. We note
5 ns, most ns dynamics in the folded domain (residues                              that both these processes appear to occur on timescales
1–90) occur at 3 ns, which is shorter than the expected                            that are close to, but well distinct from, the reorientation
rotational correlation time of the protein, highlighting yet                        of the folded domain. This indicates that slow dynamics in
again that our choice of water model does not reproduce                             IDRs is of segmental nature and decoupled from the rota-
protein hydrodynamics with sufficient accuracy. In both                             tional diffusion of the folded domain beyond the persistence
the folded domain and IDR, the two fastest motional pro-                            length of several residues, implying that the use of ‘‘order
cesses occur around 10 and 100 ps, suggesting, assuming                             parameters’’ is not the most informative for understanding

3790 Biophysical Journal 121, 3785–3794, October 18, 2022
                                                                                                                   IDPs dynamics by NMR and MD

                                                                                                     FIGURE 3 Motional timescales derived from fits
                                                                                                     of average autocorrelation functions to a predefined
                                                                                                     grid of 128 timescales, from 1 ps to 50 ns. The size
                                                                                                     of each dot is proportional to the amplitude of the
                                                                                                     associated timescale.

the dynamic richness of long IDRs. We suggest that a dy-                      ps) displays many features identified above. t2 is close to
namic description in terms of multiple timescales and their                   900–1,000 ps for the entire sequence, with the exception
associated amplitudes is a more natural framework to under-                   of the region broadly centered around the K-tract. This
stand the functional mechanisms of disordered proteins.                       observation is consistent with our interpretation of the third
   We note that, despite a lack of quantitative agreement                     and fourth components of the IMPACT analysis. t3, which
with the high-field data due to excessively fast multi-ns mo-                 appears to be poorly defined because of the scarcity of in-
tions, the simulation, particularly with the use of ABSURD,                   formation on J(0) in our dataset, does not show any evident
reproduces relaxometry rates well. This demonstrates that                     sequence dependence, suggesting again that slow motions
relaxometry data can be described with a model that does                      are segmental chain-like dynamics largely independent of
not include >10 ns motions, as an alternative to the use of                   the rotation of the N-terminal domain. We find that the
the correlation times T6 and T7 of the IMPACT analysis.                       product of A3 and t3 is much more robustly determined
   MF analysis of HF data and high-resolution relaxometry                     in our analysis, in line with decades of applications of
measurements simultaneously reproduces relaxation rates                       MF analysis to folded proteins. Consistently with B1-B2
measured at low (Fig. S12) and high (Fig. S13) fields                         features in IMPACT, the amplitude of fast motions
with good accuracy. The sequence dependence of fitted pa-                     (Fig. 4 f) increases only slightly going from the N- to the
rameters (Fig. 4, we remind the reader that t1 is fixed to 45                 C-terminus. The amplitudes of intermediate (Fig. 4 e)

 a                                                  b                                                  c

 d                                                  e                                                  f

FIGURE 4 Motional timescales (a and b) and amplitudes (d–f) resulting from the model-free analysis of either the entire dataset comprising both high-
resolution relaxometry and HF spin relaxation data (blue) or HF measurements only (orange). The product of A3 and t3 is better defined than the two in-
dividual parameters (c). Shaded areas represent uncertainties on fitted parameters, estimated by Monte Carlo simulations.

                                                                                  Biophysical Journal 121, 3785–3794, October 18, 2022 3791
Salvi et al.

and slow (Fig. 4 d) motions match B4 and B5 in the                  ysis of the full set of high- and low-field relaxation rates.
IMPACT analysis, respectively. Overall, the results are             We note, however, that it is again difficult to make any
consistent with what was expected for an IDR of similar             meaningful comparison because of the limited size of the
length in the absence of significant partially formed sec-          high-field data set (only 6 rates are available for the determi-
ondary structure elements.                                          nation of 4 independent parameters).
   Recent studies of the dynamics of IDPs have exploited               The region spanning residues 105–140 was shown (55) to
full sets of R1, R2, 1H-15N NOE and cross- correlated               electrostatically interact with the K-tract and with the struc-
CSA-dipole cross-relaxation hxy at three or more magnetic           tured part of the d subunit. The electrostatic interactions
fields. The relative sparsity of experimental data available at     with the K-tract are essential for the role of the d subunit
high field in this study precludes a systematic comparison of       in regulation of RNA polymerase activity by a stabilization
the information content present in high- and low-field relax-       of initiation complexes of RNA polymerase-DNA interac-
ometry data. We have nevertheless repeated the MF analysis          tion (55). The accurate description of the dynamics in this
using only the spin relaxation data measured at 500, 600,           region is therefore of a particular interest. If confirmed by
and 850 MHz. Rates back calculated from the results of              further investigations, motions with an effective timescale
this MF analysis closely match the experimental values              of 10 ns or more, such as the contribution for T7 in the
(Fig. S14). Interestingly, cross-validation of the MF results       ICARUS-IMPACT analysis, could be related to the forma-
using the relaxometry data, which are not actively used in          tion of a temporarily compacted conformation of the part
the fit, reveals that the overall trend of longitudinal relaxa-     of the C-terminal domain involving the positively charged
tion at low field can be predicted with good accuracy from          K-tract and the part of the acidic regions. Yet, the contribu-
the information about dynamics encoded in the high-field            tion of such motions is very small in the ICARUS-IMPACT
data in most cases (Fig. S15). Such overall agreement               analysis and therefore not reflected by MF analysis and not
is expected since high-field relaxation probes the spectral         captured by MD simulations.
density function, a monotonous, decreasing function of the
frequency, down to 50 MHz and at zero frequency. In addi-
                                                                    CONCLUSIONS
tion, the precision of low-field relaxation rates is much
lower than that of high-field rates due to the limited sensi-       We presented a detailed comparison of complementary
tivity of the shuttle and probe apparatus (about 20% of the         NMR- and computational-based approaches to probe and
sensitivity of a room-temperature probe or 7% of the               describe ps-ns dynamics in disordered systems using a
600 MHz spectrometer used for high-field relaxation                 well-characterized model system. Overall, our results indi-
measurements).                                                      cate that three timescales and their associated amplitudes
   The spectral density at zero frequency J(0) obtained from        are in general sufficient to model most observations
high-field measurements probes the slowest motions in a             in vitro and in silico. While this has been shown already
way where amplitude and correlation times are convoluted.           in a number of IDPs, here we add an example of a disordered
The magnetic-field dependence of low-field relaxation rates         region in a partially folded protein, and we show that the
should therefore provide novel information concerning               presence of the folded domain does not increase the
small, but statistically significant, differences between           complexity of the dynamic features, which can be captured
experimental relaxometry relaxation rates and those pre-            by the tools and models developed specifically for IDPs.
dicted by the analysis of high-field relaxation alone. The             Our study combines 15N relaxation measured at atomic
presence of additional information contained in relaxometry         resolution of an IDP over an unprecedented range of mag-
relaxation rates is suggested by a direct comparison of             netic field strengths and therefore a broader spectrum of
the MF parameters obtained by an analysis of high-field             timescales of reorientational modes than has been available
relaxation alone and with the addition of relaxometry data          until now. We observe that the model assuming three major
(Fig. 4), which have different profiles in the region between       contributions to the spectral density function can predict the
105 and 137 (results are listed in Tables S8 and S9, respec-        relaxometry data measured down to 4.26 MHz with good
tively). Both analyses provide similar estimates of the prod-       accuracy in most cases, confirming the overall robustness
uct of A3 and t3, which is just slightly lower in the analysis      of this commonly used framework. The potential for
of the full dataset (Fig. 4 c). Not surprisingly, this product is   refining more complex motional models by including relax-
defined with more precision because of the information              ometry data into such an analysis is, however, self-evident.
about the spectral density values close to 0, due to the higher     Although our study suffers from suboptimal sampling of
number of relaxometry data at the lowest fields reporting on        high-field data and force-field inaccuracies, which have
slower motions. However, overall A3 parameters are lower            been amply discussed in the literature, our analysis never-
and t3 higher in this region when the relaxometry data are          theless provide tantalizing indications of the potential
included (Fig. 4 a and d), which could be numerically               of combining high-field relaxation and high-resolution
similar to the appearance of very small contribution of the         relaxometry to enhance sampling of the spectral density
longest correlation time T7 in the ICARUS-IMPACT anal-              function at frequencies not accessible to HF relaxation

3792 Biophysical Journal 121, 3785–3794, October 18, 2022
                                                                                                                      IDPs dynamics by NMR and MD

measurements, in particular with respect to the details of                       7. Gill, M. L., R. A. Byrd, and A. G. Palmer, III. 2016. Dynamics of
                                                                                    GCN4 facilitate DNA interaction: a model-free analysis of an intrinsi-
slower, possibly functionally important, motions in the                             cally disordered region. Phys. Chem. Chem. Phys. 18:5839–5849.
d subunit of RNA polymerase. We expect that further
                                                                                 8. Salvi, N., A. Abyzov, and M. Blackledge. 2016. Multi-timescale dy-
studies applying high-resolution relaxometry with enhanced                          namics in intrinsically disordered proteins from NMR relaxation and
sensitivity or other techniques will help to further refine mo-                     molecular simulation. J. Phys. Chem. Lett. 7:2483–2489.
tions in this important family of proteins beyond the model                      9. Salvi, N., A. Abyzov, and M. Blackledge. 2017. Analytical description
with three ps-ns effective processes.                                               of NMR relaxation highlights correlated dynamics in intrinsically
                                                                                    disordered proteins. Angew. Chem., Int. Ed. Engl. 56:14020–14024.
                                                                                10. Robustelli, P., S. Piana, and D. E. Shaw. 2018. Developing a molecular
SUPPORTING MATERIAL                                                                 dynamics force field for both folded and disordered protein states.
                                                                                    Proc. Natl. Acad. Sci. USA. 115:E4758–E4766.
Supporting material can be found online at https://doi.org/10.1016/j.bpj.       11. Thomasen, F. E., F. Pesce, ., K. Lindorff-Larsen. 2022. Improving
2022.09.016.                                                                        martini 3 for disordered and multidomain proteins. J. Chem. Theor.
                                                                                    Comput. 18:2033–2041.
                                                                                12. Abyzov, A., N. Salvi, ., M. Blackledge. 2016. Identification of dy-
AUTHOR CONTRIBUTIONS                                                                namic modes in an intrinsically disordered protein using tempera-
                                                                                    ture-dependent NMR relaxation. J. Am. Chem. Soc. 138:6240–6251.
N.S., V.Z., M.B., and P.K. analyzed data; Z.J. and S.N. prepared NMR sam-
ples; V.Z., M.Z., J.-M.T., T.M., L.Z., F.F., and P.K performed NMR exper-       13. Adamski, W., N. Salvi, ., M. Blackledge. 2019. A unified description
iments; V.Z., Z.J., P.P., and P.K. processed and analyzed NMR spectra; N.S.,        of intrinsically disordered protein dynamics under physiological condi-
                                                                                    tions using NMR spectroscopy. J. Am. Chem. Soc. 141:17817–17829.
L.Z., M.B., F.F., and P.K. wrote the manuscript; F.F., M.B., and P.K. ob-
tained funding for the project.                                                 14. Clore, G. M., A. Szabo, ., A. M. Gronenborn. 1990. Deviations from
                                                                                    the simple two-parameter model-free approach to the interpretation of
                                                                                    nitrogen-15 nuclear magnetic relaxation of proteins. J. Am. Chem. Soc.
                                                                                    112:4989–4991.
ACKNOWLEDGMENTS                                                                 15. Buevich, A. V., and J. Baum. 1999. Dynamics of unfolded proteins:
                                                                                    incorporation of distributions of correlation times in the model free
This work was supported by Czech Science Foundation grant no. GJ18-
                                                                                    analysis of NMR relaxation data. J. Am. Chem. Soc. 121:8671–8672.
04197Y (to P.K., V.Z., and Z.J.), from European Regional Development
Fund-Project MSCAfellow2@MUNI, No. CZ.02.2.69/0.0/0.0/18_070/                   16. Hsu, A., F. Ferrage, and A. G. Palmer. 2018. Analysis of NMR spin-
0009846 (to P.P. and P.K.), and grant no. ANR-18-CE29-0003 (NANO-                   relaxation data using an inverse Gaussian distribution function.
DISPRO), provided by Agence Nationale de la Recherche (to F.F. and                  Biophys. J. 115:2301–2309.
M.B.). Short scientific mission of P.K. to perform measurements at the          17. Bloembergen, N., E. M. Purcell, and R. V. Pound. 1948. Relaxation ef-
NMR spectrometer allowing high-resolution relaxometry experiments                   fects in nuclear magnetic resonance absorption. Phys. Rev. 73:679–712.
was supported by a STSM grant from the EURELAX COST Action                      18. Wangsness, R. K., and F. Bloch. 1953. The dynamical theory of nuclear
CA15209. CIISB, Instruct-CZ Centre of Instruct-ERIC EU consortium,                  induction. Phys. Rev. 89:728–739.
funded by MEYS CR infrastructure project LM2018127, is gratefully
                                                                                19. Solomon, I. 1955. Relaxation processes in a system of two spins. Phys.
acknowledged for the financial support of the measurements at the Josef             Rev. 99:559–565.
Dadok National NMR Centre.
                                                                                20. Redfield, A. G. 1957. On the theory of relaxation processes. IBM J.
                                                                                    Res. Dev. 1:19–31.
                                                                                21. Abragam, A. 1961. The Principles of Nuclear Magnetism. Clarendon
DECLARATION OF INTERESTS                                                            Press.
T.M. and J.-M.T. were employees of the Bruker BioSpin. The other authors        22. Smith, A. A., M. Ernst, and B. H. Meier. 2017. Because the light is bet-
declare no other conflict of interest.                                              ter here: correlation-time analysis by NMR spectroscopy. Angew.
                                                                                    Chem., Int. Ed. Engl. 56:13590–13595.
                                                                                23. Parigi, G., N. Rezaei-Ghaleh, ., C. Luchinat. 2014. Long-range corre-
REFERENCES                                                                          lated dynamics in intrinsically disordered proteins. J. Am. Chem. Soc.
                                                                                    136:16201–16209.
 1. Henzler-Wildman, K., and D. Kern. 2007. Dynamic personalities of            24. Clarkson, M. W., M. Lei, ., D. Kern. 2009. Mesodynamics in the
    proteins. Nature. 450:964–972.                                                  SARS nucleocapsid measured by NMR field cycling. J. Biomol.
 2. Dyson, H. J., and P. E. Wright. 2005. Intrinsically unstructured proteins       NMR. 45:217–225.
    and their functions. Nat. Rev. Mol. Cell Biol. 6:197–208.                   25. Charlier, C., S. N. Khan, ., F. Ferrage. 2013. Nanosecond time scale
 3. Jensen, M. R., M. Zweckstetter, ., M. Blackledge. 2014. Exploring               motions in proteins revealed by high-resolution NMR relaxometry.
    free-energy landscapes of intrinsically disordered proteins at atomic           J. Am. Chem. Soc. 135:18665–18672.
    resolution using NMR spectroscopy. Chem. Rev. 114:6632–6660.                26. Cousin, S. F., P. Kaderávek, ., F. Ferrage. 2018. Time-resolved pro-
 4. Kaderávek, P., V. Zapletal, ., L. 
                                        Zı́dek. 2014. Spectral density map-         tein side-chain motions unraveled by high-resolution relaxometry and
    ping protocols for analysis of molecular motions in disordered proteins.        molecular dynamics simulations. J. Am. Chem. Soc. 140:13456–13465.
    J. Biomol. NMR. 58:193–207.                                                 27. Smith, A. A., N. Bolik-Coulon, ., F. Ferrage. 2021. How wide is the
 5. Khan, S. N., C. Charlier, ., F. Ferrage. 2015. Distribution of pico- and        window opened by high-resolution relaxometry on the internal dy-
    nanosecond motions in disordered proteins from nuclear spin relaxa-             namics of proteins in solution? J. Biomol. NMR. 75:119–131.
    tion. Biophys. J. 109:988–999.                                              28. Prompers, J. J., and R. Br€uschweiler. 2002. General framework for
 6. Piana, S., A. G. Donchev, ., D. E. Shaw. 2015. Water dispersion in-             studying the dynamics of folded and nonfolded proteins by NMR relax-
    teractions strongly influence simulated structural properties of disor-         ation spectroscopy and MD simulation. J. Am. Chem. Soc. 124:4522–
    dered protein states. J. Phys. Chem. B. 119:5113–5123.                          4534.

                                                                                    Biophysical Journal 121, 3785–3794, October 18, 2022 3793
Salvi et al.

29. Salvi, N., A. Abyzov, and M. Blackledge. 2019. Solvent-dependent            44. Lee, W., M. Tonelli, and J. L. Markley. 2015. NMRFAM-SPARKY:
    segmental dynamics in intrinsically disordered proteins. Sci. Adv.              enhanced software for biomolecular NMR spectroscopy. Bioinformat-
    5:eaax2348.                                                                     ics. 31:1325–1327.
30. Seepersaud, R., R. H. V. Needham, ., A. L. Jones. 2006. Abundance           45. Eaton, J. W., D. Bateman, and S. Hauberg. 2009. GNU Octave Version
    of the d subunit of RNA polymerase is linked to the virulence of Strep-         3.0.1 Manual: A High-Level Interactive Language for Numerical Com-
    tococcus agalactiae. J. Bacteriol. 188:2096–2105.                               putations. CreateSpace Independent Publishing Platform.
31. Rabatinová, A., H. Sanderová, ., L. Krásný. 2013. The d subunit of     46. Tibshirani, R. 1988. Variance stabilization and the Bootstrap. Bio-
    RNA polymerase is required for rapid changes in gene expression                 metrika. 75:433–444.
    and competitive fitness of the cell. J. Bacteriol. 195:2603–2611.           47. Hall, P. 1988. Theoretical comparison of Bootstrap confidence inter-
                                                                                    vals. Ann. Stat. 16:927–953.
32. Papousková, V., P. Kaderávek, ., L. 
                                            Zı́dek. 2013. Structural study of
    the partially disordered full-length d subunit of RNA polymerase            48. Bolik-Coulon, N., P. Kaderávek, ., S. F. Cousin. 2020. Theoretical
    from Bacillus subtilis. Chembiochem. 14:1772–1779.                              and computational framework for the analysis of the relaxation proper-
                                                                                    ties of arbitrary spin systems. Application to high-resolution relaxom-
33. López de Saro, F. J., A. Y. Woody, and J. D. Helmann. 1995. Structural         etry. J. Magn. Reson. 313:106718.
    analysis of the Bacillus subtilis delta factor: a protein polyanion which
    displaces RNA from RNA polymerase. J. Mol. Biol. 252:189–202.               49. Wolfram Research, Inc. 2015. Mathematica. 10.1. Champaign Illinois.
                                                                                50. Loth, K., P. Pelupessy, and G. Bodenhausen. 2005. Chemical shift
34. Cousin, S. F., P. Kaderávek, ., F. Ferrage. 2016. Recovering invisible
                                                                                    anisotropy tensors of carbonyl, nitrogen, and amide proton nuclei in
    signals by two-field NMR spectroscopy. Angew. Chem., Int. Ed. Engl.
                                                                                    proteins through cross-correlated relaxation in NMR spectroscopy.
    55:9886–9889.
                                                                                    J. Am. Chem. Soc. 127:6062–6068.
35. Cousin, S. F., C. Charlier, ., F. Ferrage. 2016. High-resolution two-       51. Abraham, M. J., T. Murtola, ., E. Lindahl. 2015. GROMACS: high
    field nuclear magnetic resonance spectroscopy. Phys. Chem. Chem.                performance molecular simulations through multi-level parallelism
    Phys. 18:33187–33194.                                                           from laptops to supercomputers. SoftwareX. 1–2:19–25.
36. Kaderávek, P., N. Bolik-Coulon, ., F. Ferrage. 2019. Protein dy-          52. Lindorff-Larsen, K., S. Piana, ., D. E. Shaw. 2010. Improved side-
    namics from accurate low-field site-specific longitudinal and transverse        chain torsion potentials for the Amber ff99SB protein force field. Pro-
    nuclear spin relaxation. J. Phys. Chem. Lett. 10:5917–5922.                     teins. 78:1950–1958.
        náková, Z., V. Zapletal, ., P. Kaderávek. 2020. Boosting the
37. Jase                                                                       53. Zapletal, V., A. Mládek, ., J. Hritz. 2020. Choice of force field for pro-
    resolution of low-field $$^{15}\hbox {N}$$ relaxation experiments               teins containing structured and intrinsically disordered regions.
    on intrinsically disordered proteins with triple-resonance NMR.                 Biophys. J. 118:1621–1633.
    J. Biomol. NMR. 74:139–145.                                                 54. Tollinger, M., J. D. Forman-Kay, and L. E. Kay. 2002. Measurement of
38. Kazimierczuk, K., A. Zawadzka, and W. Kozminski. 2008. Optimiza-              side-chain carboxyl pK(a) values of glutamate and aspartate residues in
    tion of random time domain sampling in multidimensional NMR.                    an unfolded protein by multinuclear NMR spectroscopy. J. Am. Chem.
    J. Magn. Reson. 192:123–130.                                                    Soc. 124:5714–5717.
39. Lopez, J., P. Ahuja, ., G. Lippens. 2014. H/D exchange of a 15N             55. Kubán, V., P. Srb, ., L.  Zı́dek. 2019. Quantitative conformational
    labelled Tau fragment as measured by a simple Relax-EXSY experi-                analysis of functionally important electrostatic interactions in the
    ment. J. Magn. Reson. 249:32–37.                                                intrinsically disordered region of delta subunit of bacterial RNA poly-
                                                                                    merase. J. Am. Chem. Soc. 141:16817–16828.
40. Srb, P., J. Novácek, ., L. 
                                 Zı́dek. 2017. Triple resonance 15N NMR
                                                                                56. Garcı́a de la Torre, J., M. L. Huertas, and B. Carrasco. 2000.
    relaxation experiments for studies of intrinsically disordered proteins.
                                                                                    HYDRONMR: prediction of NMR relaxation of globular proteins
    J. Biomol. NMR. 69:133–146.
                                                                                    from atomic-level structures and hydrodynamic calculations.
41. Ferrage, F., D. Cowburn, and R. Ghose. 2009. Accurate sampling of               J. Magn. Reson. 147:138–146.
    high-frequency motions in proteins by steady-state 15N{1H} nuclear         57. Garcı́a De La Torre, J., M. L. Huertas, and B. Carrasco. 2000. Calcu-
    overhauser effect measurements in the presence of cross-correlated              lation of hydrodynamic properties of globular proteins from their
    relaxation. J. Am. Chem. Soc. 131:6048–6049.                                    atomic-level structure. Biophys. J. 78:719–730.
42. Delaglio, F., S. Grzesiek, ., A. Bax. 1995. NMRPipe: a multidimen-          58. Kaderávek, P., C. Diehl, ., M. Akke. 2011. Complementation of 3D
    sional spectral processing system based on UNIX pipes. J. Biomol.               structure of delta subunit of RNA polymerase from Bacillus subtilis
    NMR. 6:277–293.                                                                 with description of internal motions in terms of reduced spectral den-
43. Ying, J., F. Delaglio, ., A. Bax. 2017. Sparse multidimensional itera-          sity mapping. Mater. Struct. 18:3–5.
    tive lineshape-enhanced (SMILE) reconstruction of both non-uni-             59. Zimm, B. H. 1956. Dynamics of polymer molecules in dilute solution:
    formly sampled and conventional NMR data. J. Biomol. NMR.                       viscoelasticity, flow birefringence and dielectric loss. J. Chem. Phys.
    68:101–118.                                                                     24:269–278.

3794 Biophysical Journal 121, 3785–3794, October 18, 2022


---

# Rotational Dynamics of Proteins from Spin Relaxation Times and Molecular Dynamics Simulations

**Authors:** O. H. Samuli Ollila, Harri A. Heikkinen, Hideo Iwaï
**Year:** 2018
**Venue:** The Journal of Physical Chemistry B
**DOI:** 10.1021/acs.jpcb.8b02250
**Source PDF URL:** https://europepmc.org/articles/PMC6150695?pdf=render
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

This is an open access article published under a Creative Commons Attribution (CC-BY)
                                                        License, which permits unrestricted use, distribution and reproduction in any medium,
                                                        provided the author and source are cited.

                                                                                                                                                       Article

                                                         Cite This: J. Phys. Chem. B 2018, 122, 6559−6569                                  pubs.acs.org/JPCB

Rotational Dynamics of Proteins from Spin Relaxation Times and
Molecular Dynamics Simulations
O. H. Samuli Ollila,*,†,‡ Harri A. Heikkinen,† and Hideo Iwaï†
†
 Research Program in Structural Biology and Biophysics, Institute of Biotechnology, University of Helsinki, 00014 Helsinki, Finland
‡
 Institute of Organic Chemistry and Biochemistry, Czech Academy of Sciences, 117 20 Prague 6, Czech Republic
    *
    S Supporting Information

    ABSTRACT: Conformational ﬂuctuations and rotational tumbling of proteins can be experimentally accessed with nuclear spin
    relaxation experiments. However, interpretation of molecular dynamics from the experimental data is often complicated,
    especially for molecules with anisotropic shape. Here, we apply classical molecular dynamics simulations to interpret the
    conformational ﬂuctuations and rotational tumbling of proteins with arbitrarily anisotropic shape. The direct calculation of spin
    relaxation times from simulation data did not reproduce the experimental data. This was successfully corrected by scaling the
    overall rotational diﬀusion coeﬃcients around the protein inertia axes with a constant factor. The achieved good agreement with
    experiments allowed the interpretation of the internal and overall dynamics of proteins with signiﬁcantly anisotropic shape. The
    overall rotational diﬀusion was found to be Brownian, having only a short subdiﬀusive region below 0.12 ns. The presented
    methodology can be applied to interpret rotational dynamics and conformation ﬂuctuations of proteins with arbitrary anisotropic
    shape. However, a water model with more realistic dynamical properties is probably required for intrinsically disordered proteins.

■    INTRODUCTION
Conformational ﬂuctuations and the entropy of proteins play a
                                                                                 and the available time scales in the simulations.17−19,28−31 The
                                                                                 main issues have been the overestimated overall rotational
signiﬁcant role in their functionality and interactions with other               diﬀusion of proteins due to inaccuracies in water models19,29,32
biomolecules. Conformational ﬂuctuations and the overall                         and the insuﬃcient accuracy of correlation functions calculated
Brownian tumbling of proteins are experimentally accessible                      from single molecules in MD simulations.30,33
through the spin relaxation times of 15N and 13C nuclei                             In this work, we overcome these issues by assuming that the
measured with nuclear magnetic resonance (NMR) techni-                           overall rotational dynamics of protein follows anisotropic rigid
ques.1−7 The spin relaxation rates have been used to, for                        body diﬀusion. Diﬀusion coeﬃcients around inertia axes are
example, analyze conformational entropies,1,8−11 binding                         directly calculated from angular displacements. The diﬀusion
entropies,1,12 resolve sampled structures,3−5,13 and validate                    coeﬃcients are then used to determine the contribution of the
molecular dynamics (MD) simulations.14−21 These analyses are                     overall rotational tumbling to the rotational correlation
almost exclusively based on the separation of the internal                       functions of N−H bonds in the protein backbone. This
conformational ﬂuctuations and the overall rotational tum-                       reduces the required simulation length for the accurate
bling.22,23 Also, the isotropic overall diﬀusion is often assumed,               determination of the rotational correlation functions. Fur-
whereas analysis of anisotropic molecules is signiﬁcantly more                   thermore, the overestimated overall Brownian tumbling rates
complicated.1,2,24−27 Thus, new approaches are needed to                         due to the inaccurate water model can be corrected during the
interpret spin relaxation times measured from anisotropic or                     correlation function calculation by scaling the diﬀusion
intrinsically disordered molecules.                                              coeﬃcients in all directions with a constant factor. The
   Classical MD simulation methods are promising tools to                        corrected correlation functions can be used to interpret the
interpret spin relaxation experiments for molecules with
signiﬁcantly anisotropic shape or correlations between internal                  Received: March 7, 2018
and overall rotational motions. Practical applications are,                      Revised: May 27, 2018
however, limited by inaccuracies in the force ﬁeld descriptions                  Published: May 29, 2018

                              © 2018 American Chemical Society            6559                                                        DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                            J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                               Article

spin relaxation experiments for proteins with arbitrarily                      where CI(t) and CO(t) are correlation functions for the internal
anisotropic shapes.                                                            dynamics and overall rotations, respectively. Conformational
   The developed approach is demonstrated by interpreting the                  ﬂuctuations can be described in this approximation by using the
experimental spin relaxation data of C-terminal domains of                     square of the order parameter with respect to molecular axes S2,
TonB proteins from Helicobacter pyroli (HpTonB-92)34 and                       which are given by the plateau of the internal rotational
from Pseudomonas aeruginosa (PaTonB-96),35 having 92 and 96                    correlation function. Timescales for the ﬂuctuations can be
residues, respectively. Both proteins have signiﬁcantly aniso-                 characterized by using the eﬀective correlation time
tropic shape, which would complicate the standard spin                                       ∞
relaxation data analysis.1,2,24−27                                                         ∫0 CI′(t )dt
■
                                                                                  τeff =
                                                                                                                                                         (7)
    METHODS
                                                                                                    C(t ) − S 2
   Spin Relaxation Experiments and Rotational Dynam-                           where C I′(t ) =   I
                                                                                                       is the reduced correlation function.23
                                                                                                1 − S2
ics of Molecules. Molecular dynamics of the protein                              The overall rotational correlation function is often described
backbone residues and spin relaxation experiments can be                       by approximating the protein as a rigid body. For arbitrarily
connected by using the spectral density J(ω)                                   anisotropic molecules, the correlation functions can be
                       ∞                                                       presented as a sum of ﬁve exponentials2,24
    J(ω) = 2  ∫0 C(t ) cos(ωt )dt                                 (1)                          5
                                                                                  CO(t ) = ∑ Aj e−t / τj
which is the Fourier transformation of the second-order
rotational correlation function for N−H bond vector                                           j=1                                                        (8)

               3                1                                              where the prefactors Aj depend on the directions of chemical
    C(t ) =      cos2 θt ′+ t −                                                bonds with respect to the molecular axes24,26 and the time
               2                2                                 (2)
                                      t′                                       constants τj are related to the diﬀusion constants around three
where θt′+t is the N−H bond angle between times t′ and t′ + t                  principal axes of a molecule (Dx , Dy , and Dz) through
and angular brackets refer to the ensemble average. Connection                 equations2,24
to the experimentally measured spin relaxation times T1, T2 and
the nuclear Overhauser eﬀect (NOE) relaxation is given by the                     τ1 = (4Dx + Dy + Dz )−1
Redﬁeld equations36,37
                                                                                  τ2 = (Dx + 4Dy + Dz )−1
    1    d N
       = NH H [J(ωH − ω N) + 3J(ω N) + 6J(ω N + ωH)]                              τ3 = (Dx + Dy + 4Dz )−1
    T1    20
              (σω N)2                                                             τ4 = [6(Dav + (Dav 2 − L2)1/2 )]−1
          +           J (ω N )
                15                                                (3)
                                                                                  τ5 = [6(Dav − (Dav 2 − L2)1/2 )]−1                                     (9)
    1     1 dNH NH
        =          [4J(0) + 3J(ω N) + J(ωH − ω N) + 6J(ωH)                     where
    T2    2 20
                          (σω N)2                                                          1                         1
       + 6J(ω N + ωH)] +          [4J(0) + 3J(ω N)]
                                                           (4)                    Dav =      (Dx + Dy + Dz ) and L2 = (Dx Dy + Dx Dz + DyDz)
                            90                                                             3                         3
                       dNH 2NH                             γ T1                   The simplest approach to extract molecular dynamics from
    NOE = 1 +                  [6J(ω N + ωH) + J(ωH − ω N)] H
                         20                                 γN                 the experimental data is the original “model-free analysis”,23
                                                                  (5)          where an isotropic diﬀusion is assumed for the overall rotation
                                                                               of the protein. This reduces eq 8 to a monoexponential form
where ωN and ωH are the Larmor angular frequencies of 15N                      and the overall rotational dynamics can be described with a
and 1H, respectively, and the number of bound protons NH = 1                   single time constant τc. Also, the internal correlation functions
for N−H bonds. The dipolar coupling constant is given by                       for each residue are assumed to decay exponentially with a
               μ0 ℏγHγN                                                        single time constant τeff toward to the square of the order
    dNH = −                                                                    parameter S2. The three parameters (τc, τeff, and S2) can be then
              4π ⟨rNH 3⟩
                                                                               successfully resolved from a ﬁt to the experimental data.
where μ0 is the magnetic constant or vacuum permeability, ℏ is                 However, the number of parameters to be ﬁtted increases if the
the reduced Planck constant, and γN and γH are the                             protein experiences an anisotropic overall diﬀusion or has
gyromagnetic constants of 15N and 1H, respectively. The                        several timescales for internal motions. In this case, the ﬁtting
average cubic length is calculated as ⟨rNH3⟩ = (0.101 nm), and                 becomes often ambiguous, even if the experimental data would
the value of Δσ = −160 ppm is used for the chemical shift                      be measured with multiple magnetic ﬁeld strengths.1,26,40 The
anisotropy of N−H bonds in proteins.37,38                                      anisotropic rotational diﬀusion is sometimes described with
  Spin relaxation experiments are typically interpreted for                    hydrodynamical calculations but they are sensitive to the
proteins by assuming that the motions related to the overall                   estimation of the hydration shell around the protein.41
Brownian tumbling and conformational ﬂuctuations are                              A rough estimate for the timescale of overall rotational
independent.39 The rotational correlation function for each                    dynamics is often given by using the T1/T2 ratio.37 This is
N−H bond can be then written as1,2,22,23,39                                    based on the assumptions that T1 and T2 are independent of
                                                                               the internal motions and that the overall dynamics is isotropic.
    C(t ) = C I(t )CO(t )                                         (6)          The spectral density then reduces to
                                                                        6560                                                     DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                       J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                            Article

                     τc′                                                     and the correlation time describing the overall rotational
   J ′(ω) = S2                                                               motion, τ′c, can be estimated by numerically minimizing the
                 1 + (ωτc′)2                                  (10)           equation

                   1 dNH NH                                                                                  (σω )2
          T1                [4J ′(0) + 3J ′(ω Ν) + J ′(ωH − ω N) + 6J ′(ωH) + 6J ′(ω N + ωH)] + 90N [4J ′(0) + 3J ′(ω N)]
             ≈ 2       20
          T2                           dNH 2NH                                                        (σω N)2
                                               [J ′( ω H − ω N ) + 3J ′( ω N ) + 6J ′( ω N + ω H )] +   15
                                                                                                              J ′(ω N)                              (11)

with respect to the experimentally measured T1/T2 ratio.                       (4) The mean square angle deviations of rotation around
    Rotational Dynamics from MD Simulations. A classical                           protein inertia axes are calculated from the MD
MD simulation gives a trajectory for each atom in the system as                    simulation trajectory.
a function of time. Rotational correlation functions for each                  (5) rotational diﬀusion constants Dx, Dy, and Dz around
bond can be then directly calculated from the trajectories by eq                   inertia axes are calculated by ﬁtting a straight line to the
2 and used to calculate the spin relaxation times through eqs                      mean square angle deviations
1−5. The resulting values can be compared to experimental
data to assess simulation model quality14−21,31,42 and to                       ⟨Δαt ′+ t 2⟩t ′ = 2Dx t
interpret experiments.21,42,43                                                   ⟨Δβt ′+ t 2⟩t ′ = 2Dyt
   The direct comparison with experiments is, however, often
complicated by the insuﬃcient statistics for the calculated                      ⟨Δγt ′+ t 2⟩t ′ = 2Dz t                                            (12)
correlation functions and the overestimated rotational diﬀusion
due to inaccuracies in the used water models.29,30,32 Here, we               where ⟨Δαt′+t ⟩t′, ⟨Δβt′+t ⟩t′, and ⟨Δγt′+t ⟩t′ are the mean square
                                                                                             2             2          2

show that the statistical accuracy of the contribution of the                angle deviations of the rotation around inertia axes from the
overall tumbling to the correlation functions, CO(t), in eq 6, can           longest protein inertia axis to the shortest, respectively.
be increased for rigid proteins by directly calculating the                    (6) contribution of the overall rotational tumbling to all
diﬀusion coeﬃcients of the inertia axes. The rotational diﬀusion                   correlation functions is assumed to follow eq 8 with the
coeﬃcients can be related to the timescales τj of the correlation                  timescales τj calculated from the rotational diﬀusion
function for anisotropic rigid body rotation in eq 8 by using the                  constants by using the relations in eq 9. Weighting
relations in eq 9.24                                                               factors Aj are determined by ﬁtting the equation to the
   The rotational diﬀusion coeﬃcients are calculated by ﬁtting a                   overall rotational correlation functions calculated from
linear slope to the square angle deviation of the inertia axes (see                MD simulations in step 3.
below). Lag times up to one hundredth of the total simulation                  (7) The new correlation functions are calculated by
length were used. This is expected to be the maximum lag time                      substituting internal correlation functions, CI(t), from
for the good statistics of rotational dynamics analyzed from a                     step 2 and anisotropic rigid body rotational correlation
single molecule in MD simulations.33 Error bars for the                            functions, CO(t), from step 6 to eq 6 giving
diﬀusion coeﬃcients were deﬁned to include results when the                                         5
lag time was varied with ±1 ns. This requires less simulation                   C N(t ) = C I(t )∑ Aj e−t / τj
data for the good statistics than a direct ﬁt of the                                               j=1                                              (13)
multiexponential sum in eq 8 to the rotational correlation
function calculated from MD simulation. In addition, the                        These correlation functions are then used to calculate spin
overestimated rotational diﬀusion due to the water                           relaxation times from eqs 1−5. The incorrect overall rotational
model19,29,32 can be corrected by scaling the diﬀusion                       diﬀusion due to a water model can be corrected at this point by
coeﬃcients around all inertia axes by a constant factor. This                scaling the rotational diﬀusion coeﬃcients, that is, timescales τj,
approach takes into account the anisotropic shape of the                     with a constant factor before calculating new correlation
molecule. This is a signiﬁcant advancement to the previous                   functions from eq 13. Here, we determine the optimal scaling
studies, which assume isotropic rotational diﬀusion with a                   factors separately for each system. Scaling factors between 1
                                                                             and 4 are explored with the spacing of 0.1 and the value giving
single exponential rotational correlation function10,15−17,44 or
                                                                             the best agreement with the experimental spin relaxation data is
use order parameters to compare simulations with experimental
                                                                             selected to be the optimal scaling factor.
data.14,17,18,44                                                                Simulation and Analysis Details. All simulations were
   The practical analysis can be divided into seven steps as                 performed using Gromacs 554 software and Amber ﬀ99SB-
follows:                                                                     ILDN55 force ﬁeld for proteins. The protein was solvated to
   (1) The total rotational correlation functions C(t) for N−H               tip3p,56 tip4p,56 or OPC457 water models. Initial structures
       bond vectors in a protein are directly calculated from the            were taken from the lowest-energy NMR structures of
       MD simulation trajectory by applying eq 2.                            HpTonB-92 (PDB code: 5LW8)34 and PaTonB-96 (PDB
   (2) The rotational correlation functions for internal dynam-              code: 6FIP).35 The results from diﬀerent initial conformations
                                                                             of both proteins with the tip3p water model are shown in
       ics CI(t) are calculated from the MD simulation
                                                                             Section S2 in the Supporting Information. The temperature
       trajectory by removing the overall rotation of the protein.           was coupled to the desired value with the v-rescale thermo-
   (3) The overall and internal motions are assumed to be                    stat,58 and the pressure was isotropically set to 1 bar using a
       independent and the overall rotational correlation                    Parrinello−Rahman barostat.59 Time step was 2 fs, Lennard-
       function is calculated from eq 6 as CO(t) = C(t)/CI(t).               Jones interactions were cut oﬀ at 1.0 nm, particle mesh
                                                                      6561                                                    DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                    J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                  Article

Table 1. Simulated Systems and Rotational Diﬀusion Coeﬃcients (rad2·107/s) Calculated from Simulations
      protein         watera        T (K)b   ts (ns)c   ta (ns)d       Dx               Dy             Dz           D∥/D⊥e                Davf            ﬁlesg
    PaTonB-96         tip3p          298      400        300        4.2 ± 0.1        4.4 ± 0.1     10.4 ± 0.1     2.42 ± 0.1          6.4 ± 0.1            45
    PaTonB-96         tip4p          298      400        390       1.81 ± 0.01      2.06 ± 0.03    4.55 ± 0.03    2.35 ± 0.04        2.80 ± 0.02           46
    PaTonB-96         tip4p          310      400        390       2.60 ± 0.02      2.22 ± 0.05     5.0 ± 0.1     2.07 ± 0.09        3.26 ± 0.07           47
    PaTonB-96         OPC4           310      1200       1190      2.01 ± 0.01      2.19 ± 0.01    5.01 ± 0.03    2.39 ± 0.02        3.07 ± 0.01           48
    HpTonB-92         tip3p          310      570        370       8.25 ± 0.05      7.67 ± 0.06    15.9 ± 0.3     1.99 ± 0.06        10.6 ± 0.2            49
    HpTonB-92         tip3p          303      800        790       6.24 ± 0.02      7.04 ± 0.03    11.9 ± 0.2     1.80 ± 0.03        8.40 ± 0.07           50
    HpTonB-92         tip4p          310      470        370        3.6 ± 0.1       3.24 ± 0.01     6.3 ± 0.3      1.8 ± 0.1          4.4 ± 0.2            51
    HpTonB-92         tip4p          303      400        200        2.7 ± 0.1       2.71 ± 0.02     5.6 ± 0.5      2.1 ± 0.2          3.7 ± 0.2            52
    HpTonB-92         OPC4           310      800        790       2.85 ± 0.01      2.70 ± 0.01    5.56 ± 0.01    2.00 ± 0.01        3.70 ± 0.01           53
a                                                                                                                                                1
    Water model used in simulation. bSimulation temperature. cTotal simulation time. dAnalyzed simulation time. eD = Dz ,                D⊥ = 2 (Dx + Dy)
f       1
  Dav = 3 (Dx + Dy + Dz) gCitation to a repository containing the simulation data.

Ewald60,61 was used for electrostatics, and LINCS was used to                       The T1 and T2 relaxation times were measured using the
constrain all bond lengths.62 The simulated systems are listed in                   following series of the delays: 10, 50, 100, 200, 300, 500, 800,
Table 1 with the references giving access to the trajectories and                   1000, 1200, and 2000 ms for T1 and 16, 64, 96, 128, 156, 196,
the related simulation ﬁles. Equilibration of the trajectories was                  224, and 256 ms for T2. Recycle delays of 3.0 and 2.0 s were
followed by monitoring the protein root-mean-square-devia-                          used for T1 and T2 experiments, respectively. The relaxation
tion, inertia tensor eigenvalues, and rotation angles. Suﬃcient                     rates (R1 = 1/T1, R2 = 1/T2) were calculated as an exponential
amount of data was omitted from the beginning of simulation                         ﬁt of a single exponential decay to peak intensity values: I(t) =
trajectories to remove the signiﬁcant ﬂuctuations in these                          I0 exp(−t/T1) or I(t) = I0 exp(−t/T2), where I(t) is the peak
parameters. If such ﬂuctuations were not observed, the ﬁrst 10                      volume at a time t. The 15N{1H}-NOE measurements were
ns of the trajectory was omitted as an equilibration period.                        carried out with a recycling delay of 5.1 s with and without
   The rotational correlation functions are calculated with gmx                     saturation of the amide protons. The 15N{1H}-NOE values
rotacf from Gromacs package.63 The overall rotation was                             were derived from the volumes of the heteronuclear single-
removed for CI(t) calculation by using a ﬁt option of the gmx                       quantum coherence (HSQC) peaks using the equation of ν =
trjconv tool in Gromacs package.63 The order parameters S2                          I/I0. The relaxation data were processed and analyzed using
were determined by averaging the rotational correlation                             Bruker Dynamic Center software (version 2.1.8).

                                                                                    ■
functions from the oriented trajectory, CI(t), over the lag
times above 50 ns. The eﬀective correlation times were then                              RESULTS AND DISCUSSION
calculated by eq 7. Inertia axes of proteins were calculated with
the compute_inertia_tensor function from MDTraj python                                 Global Rotational Dynamics of the Protein. The mean
library.64                                                                          square angle deviations for the rotation of the PaTonB-96
   Spectral density was calculated by ﬁtting a sum of 471                           protein around inertia axes in the simulation with the OPC4
exponentials with timescales from 1 ps to 50 ns with                                water model are shown in Figure 1. This is the longest
logarithmic spacing                                                                 simulation data set in this work (1.2 μs), and the linear
                                                                                    behavior of the mean square angle deviations is observed for
                N
                                                                                    the lag times up to one hundredth of the total simulation length
     C N(t ) = ∑ αi e−t / τi                                                        (12 ns), which is expected to be the maximum lag time for the
                i=1                                                   (14)
                                                                                    good statistics of rotational dynamics analyzed from a single
to the new correlation function from eq 13 by using the                             molecule in MD simulations.33 Deviations from the linear
lsqnonneg routine in MATLAB.65 The Fourier transform was                            behavior are only seen with the lag times longer than this limit,
then calculated by using the analytical function for the sum of                     as also demonstrated for the shorter simulations with tip4p
exponentials                                                                        water at two diﬀerent temperatures in Figures S1 and S2 in the
                 N
                                                                                    Supporting Information. The plots with log−log scale in
                               τi                                                   Figures 1, S1, and S2 reveal a weakly subdiﬀusive region only
      J(ω) = 2∑ αi
                        1 + ω 2τi 2                                   (15)
                                                                                    below very short timescales of approximately 0.12 ns. Thus, we
                i=1
                                                                                    conclude that the protein experiences the Brownian rotational
   A similar approach has been previously used for the lamellar                     tumbling with a good approximation. The diﬀusion coeﬃcients
lipid and surfactant systems in combination with solid-state                        can be then calculated from the slope of the mean square angle
NMR experiments.66,67 All computer programs used for the                            deviations according to eq 12 by using the lag times less than
analysis are available from ref 68.                                                 one hundredth of the total MD simulation length. The error
   Spin Relaxation Experiments. NMR experiments were                                bars were calculated by varying the lag time with 1 ns to both
recorded on a Bruker Avance III HD NMR spectrometer                                 directions. The data from HpTonB-92 protein (not shown) led
operated at 1H frequency of 850.4 MHz equipped with a                               to similar conclusions.
cryogenic probe head. The longitudinal (T1), transverse (T2),                          The resulting rotational diﬀusion constants from diﬀerent
and 1H−15N-heteronuclear NOE spin relaxation times for the                          simulations are summarized in Table 1. As expected, the
backbone 15N atoms of HpTonB-9234 were collected at 303 K                           rotational diﬀusion coeﬃcients increase with the temperature
using the well-established NMR pulse sequences described                            and the decreasing size of a protein. The values are, however,
previously.37,69,70 The similarly detected spin relaxation data for                 larger than expected from the experimental T1/T2 ratio
PaTonB-96 at 298 K are also reported in another publication.35                      analyzed with eq 11 and from the previously reported values
                                                                             6562                                                   DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                          J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                Article

                                                                               Figure 2. Rotational correlation functions calculated from MD
                                                                               simulations of PaTonB-96 with the tip4p water model at 298 K for
                                                                               residues at diﬀerent regions. (Top) Total correlation functions C(t)
Figure 1. Mean square angle deviations of the rotation around inertia          calculated from MD simulation (solid lines) and new correlation
tensor axes calculated from PaTonB-96 simulation with the OPC                  functions determined from eqs 6 and 8 by using rotational diﬀusion
water model. The data are shown with linear (top) and logarithmic              constants and ﬁtted prefactors (dashed lines); (middle) correlation
scale (bottom).                                                                functions for internal motions calculated from simulation with
                                                                               removed overall protein rotation; and (bottom) correlation function
                                                                               for overall motions determined as CO(t) = C(t)/CI(t) (solid lines) and
for proteins with similar sizes,71 especially when tip3p water                 by ﬁtting to eq 8 with timescales from rotational diﬀusion coeﬃcients
model is used. Similar results were previously explained by the                in Table 1 (dashed lines).
overestimated water self-diﬀusion of the tip3p water
model.19,29,32                                                                 simulation. The new correlation functions, determined from
   The analysis leading to the new correlation functions in eq                 eq 13 and shown in Figure 2 (top, dashed lines), are
13 (see Methods section) is exempliﬁed in Figure 2 for three                   indistinguishable from the correlation functions calculated
residues located in diﬀerent domains of PaTonB-96 with                         from the original MD simulations with the lag times shorter
diﬀerent characteristic rotational dynamics. The ﬂexible C-                    than one hundredth of the total simulation time (approximately
terminus is represented by the residue 341, more rigid β-sheet                 4−12 ns), which is the maximum lag time for the good statistics
by the residue 331, and a ﬂexible loop between two β-strands                   in single-molecule MD simulations.33 This suggests that the
by residue 322 (see the labeling in Figure 6). The total                       anisotropic rigid body diﬀusion model (eq 8) and the
correlation functions C(t) of all residues in Figure 2 (top, solid             separation of internal and global motions (eq 6) are good
lines) decay toward zero within ∼10−50 ns. The internal                        approximations for the proteins studied in this work. The
correlation functions CI(t) in Figure 2 (middle) decay to a                    analytical description of the overall rotation with eq 8 in the
plateau value, which deﬁnes the square of the order parameter                  new correlation functions clearly reduces the statistical
S2. As expected, the internal correlation function for residue                 ﬂuctuations with the long lag times in Figure 2. The eﬀect is
331 in the rigid β-sheet rapidly decays to the largest order                   most visible for the ﬂexible C-terminus (residue 341) having
parameter value, whereas the correlation functions of the                      the smallest, thus the least detectable, contribution from the
residues in the loop and C-terminus decay slower to the smaller                overall rotation of the protein due to the small order
order parameter values because of the larger conformational                    parameters.
ensemble sampled by these regions.                                                Global Rotational Dynamics in Simulations and
   The overall rotational correlation functions, CO(t) = C(t)/                 Experiments. Spin relaxation times of HpTonB-92 are
CI(t), are shown in Figure 2 (bottom, solid lines). Also, the                  compared between the experiments and simulations using
correlation functions of anisotropic rigid body rotation from eq               two diﬀerent water models in Figure 3. The simulation with
8 are shown in Figure 2 (bottom, dashed lines). The timescales                 tip3p water model underestimates the T1/T2 ratios, suggesting
for the latter, τi, are given by the rotational diﬀusion coeﬃcients            too fast overall rotational diﬀusion dynamics.72 This is in
from the simulation and the relations in eq 9. The prefactors,                 agreement with the previous study, where the overestimated
Aj, are determined by ﬁtting eq 8 to the overall rotation                      rotational diﬀusion was attributed to the self-diﬀusion of
correlation functions, C O (t), calculated from the MD                         tip3p.19,29,32 On the other hand, simulation results with tip4p
                                                                        6563                                                      DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                        J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                              Article

Figure 3. 15N spin relaxation times for HpTonB-92 from experimental
data (circles) and MD simulations with diﬀerent water models
(squares).

water model show better agreement with the experimental data
in Figure 3.
   To see if the discrepancy in spin relaxation times for
simulations with tip3p water model could be explained by the
overestimated overall diﬀusion of the protein, the diﬀusion
coeﬃcients were divided by the optimal scaling factor before
applying eq 13 to calculate the new correlation functions. The
scaling factor value of 2.9 gave the best agreement with the
experimental spin relaxation data. The spin relaxation times
calculated from the new correlation functions after scaling the
rotational diﬀusion coeﬃcients with the optimal scaling factor
value are shown in Figure 4.
   Similar comparison for the spin relaxation times of PaTonB-
96 between experiments and simulations with tip3p, tip4p, and
OPC4 water models is shown in Figure 5. The experimentation
of the OPC4 water model was inspired by the recent study
reporting signiﬁcant improvements in lipid monolayer simu-
lations when this water model was used.75 The underestimation                Figure 4. (A) Structures of HpTonB-92 from the MD simulations with
of T1/T2 ratio was also observed in the simulations of PaTonB-               tip3p at 303 K (100 structures taken from 400 ns long trajectory).
                                                                             Secondary structures are color-labeled with Visual Molecular
96 with tip4p and OPC4 water models when compared with
                                                                             dynamics;73,74 α-helices are highlighted in red and β-strands in blue.
the experiments. The discrepancy is, however, less severe than               Terminal ends are labeled with N and C. The structure from left is
with tip3p, suggesting that the required scaling factor for the              rotated with approximately 150° to the ﬁgure on right. (B) Spin
overall rotational diﬀusion should be smaller for tip4p and                  relaxation times from experiments (circles) and tip3p simulations
OPC4 water models. Indeed, the spin relaxation times                         (squares) with rotational diﬀusion coeﬃcients divided by a constant
calculated from PaTonB-96 simulation with the tip4p water                    factor of 2.9 at 303 K. Order parameters and eﬀective internal
model were found to be in good agreement with the                            correlation times calculated from simulations.
experiments in Figure 6 when the diﬀusion coeﬃcients were
divided with a constant factor of 1.2, which is smaller than 2.9             Table S1 together with the corresponding coeﬃcients for self-
used for the tip3p simulation of HpTonB-92 above. The scaling                diﬀusion of water.29,57 Notably, the eﬀect of 12 °C temperature
factors used to correct the overall rotational diﬀusion of                   diﬀerence on the spin relaxation times from tip4p simulations
diﬀerent proteins with diﬀerent water models are shown in                    in Figure 5 is signiﬁcantly smaller than the observed diﬀerences
                                                                      6564                                                      DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                      J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                 Article

Figure 5. Plots of experimental (circles) and simulated (squares) spin
relaxation times for PaTonB-96.

between simulations and experiments or the changes due to the
scaling of the diﬀusion coeﬃcient.
   The scaling of the overall rotational diﬀusion coeﬃcients
with a constant factor led to a good agreement with the
experimental spin relaxation data for both systems simulated
with diﬀerent water models, as seen in Figures 4 and 6. The
good agreement with experiments suggests that the scaled
rotational diﬀusion coeﬃcients from MD simulations can be
considered as an interpretation of the anisotropic rotational
motion in NMR experiments. The scaled rotational diﬀusion
coeﬃcients from the simulations giving the best agreement with
the experimental data are summarized in Table 2. In contrast to
the unscaled diﬀusion constants in Table 1, these results are in
line with the previously reported values for proteins with similar
sizes.71 Also, the timescales, τc′, estimated from eq 11 are close
to the average diﬀusion coeﬃcient, τc = (6Dav)−1, in Table 1.
   Interpretation of Protein Internal Relaxation from MD
Simulations. The good agreement of the spin relaxation times
between the simulations with the scaled overall rotational
diﬀusion coeﬃcients and the experiments (Figures 4 and 6)                       Figure 6. (A) Structures sampled by PaTonB-96 from MD simulations
suggests that the simulations can be used to interpret the                      with tip4p at 298 K (100 structures from 400 ns long trajectory).
internal mobility of proteins from the experimental data.                       Secondary structures are color-labeled with Visual Molecular
   Only small variations between diﬀerent residues are observed                 dynamics;73,74 α-helixes and β-strands are red and blue, respectively.
for spin relaxation times of HpTonB-92 in Figure 4. This                        Residues 246−251, 320−326, and 338−342 with increased internal
indicates a rather rigid protein structure, which is also seen in               dynamics are yellow and α-helix ﬂuctuations between two orientations
                                                                                (residues 266−270) are violet in the left column. Terminal ends are
the MD simulation snapshots overlayed in Figure 4A. Only few                    labeled with N and C. The structure from left is rotated with
residues in the terminal ends show slightly enhanced                            approximately 100° to the ﬁgure on right. (B) Spin relaxation times
conformational ﬂuctuations in the MD simulation and in spin                     from experiments (circles) and tip4p simulations (squares) with
relaxation data. In addition, some deviations from the average                  rotational diﬀusion coeﬃcients divided by a constant factor of 1.2 at
spin relaxation times are observed in the experimental data                     298 K. Order parameters and eﬀective internal correlation times
close to residues 210−222. Simulations of HpTonB-92 do not                      calculated from simulations.

                                                                         6565                                                      DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                         J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                Article

Table 2. Rotational Diﬀusion Coeﬃcients (rad2·107/s)
Giving the Best Agreement with Experimental Spin
Relaxation dataa
                             HpTonB-92                 PaTonB-96
      Dx                     2.15 ± 0.01              1.51 ± 0.01
      Dy                     2.43 ± 0.01              1.72 ± 0.03
      Dz                     4.10 ± 0.01              3.79 ± 0.03
      Dav                    2.90 ± 0.03              2.30 ± 0.02
      τc (ns)b                5.7 ± 0.1                7.2 ± 0.1
      τ′c (ns)c               5.8 ± 0.1                6.9 ± 0.1
a
  For HpTonB-92 construct, the values calculated from simulation with
tip3p were scaled with 2.9 (spin relaxation data in Figure 4), and for
PaTonB-96, the values from tip4p simulation at 298 K were scaled by
1.2 (spin relaxation data in Figure 6). bτc = (6Dav)−1. cAverage overall
residues given by eq 11.
                                                                                  Figure 7. Prefactors αi corresponding to diﬀerent timescales τi
oﬀer any explanation for this observation; however, the similar                   resulting from a ﬁt of eq 14 to correlation functions from MD
region in PaTonB-96 simulation shows ﬂuctuations between                          simulation of PaTonB-96 at 298 K. The used correlation functions
                                                                                  give a good agreement with experimental spin relaxation times as
two orientations of α-helix.35 Exceptionally low order                            shown in Figure 6.
parameters and long eﬀective correlation times are observed
in simulations for residues 245−250 of HpTonB-92. Moreover,
short T1 times are experimentally observed close to this region,                  the dynamics of residue 341 probably arise from the slow
but the interpretation is not straightforward as the low T1 times                 conformational ﬂuctuations of the N-terminus, rather than the
are not reproduced by MD simulations.                                             overall rotational dynamics. This supports the conclusion that
   PaTonB-96 exhibits more internal mobility and the segments                     the large amount of sampled conformations lead to the small
with enhanced conformational ﬂuctuations are labeled with                         order parameters and large eﬀective correlation times observed
yellow color in Figure 6. The larger number of sampled                            in Figure 5. Although the separation of rotational dynamics of
conformations in both terminal ends is characterized by the low                   individual N−H bonds to diﬀerent components gives intuitively
order parameters and long eﬀective internal correlation times                     understandable results, it should be kept in mind that it is based
observed in the simulations. Enhanced conformational                              on the ﬁtting of a multiexponential sum to the simulation data
ﬂuctuations are also observed for residues 320−326, which                         and the solution of such ﬁt is not unique.
correspond to the loop between two β-strands. MD simulations
predict low order parameters and long internal eﬀective
correlation times also close to residues 266−271, which can
                                                                                  ■    CONCLUSIONS
                                                                                  The experimental spin relaxation data for protein backbone N−
be explained by two diﬀerent orientations sampled by the α-                       H bonds were successfully reproduced by using the classical
helix in this region (color-labeled with violet in Figure 6A). The                MD simulations for two diﬀerent small domains. Thus, the
orientational ﬂuctuations of the similar short helix could also                   simulation trajectories give an atomic resolution interpretation
explain the above mentioned deviations of spin relaxation times                   for protein dynamics measured with NMR experiments.
for residues 210−222 of HpTonB-92.34                                              Interpretation of the overall and internal dynamics was
   MD simulations can be used to analyze diﬀerent components                      demonstrated for two proteins with anisotropic molecular
contributing to the rotational dynamics of individual N−H                         shape and some ﬂexible regions. Interpretation of the 15N spin
bonds. In this work, we have ﬁtted a sum of 471 diﬀerent                          relaxation data measured from such proteins has been very
timescales to the correlation functions according to eq 14. Most                  challenging with the previously available methods.26,69
of the prefactors (αi in eq 14) are zero in all correlation                          The overall rotation of the studied proteins was found to be
functions after the ﬁtting; thus, the timescales τi corresponding                 Brownian, having only a small subdiﬀusive behavior with short
to nonzero prefactors are considered as the components                            timescales below ∼0.12 ns, which could be contrasted with
contributing to the total relaxation process of each N−H bond.                    crowded environments, where anomalous diﬀusion is expected
The prefactors are shown in Figure 7 for the same residues of                     to be more signiﬁcant.76 The direct analysis of classical MD
PaTonB-96, which were used to exemplify the correlation                           trajectories did not, however, reproduce the experimental 15N
functions in Figure 2. As expected for residue 322 in the rigid β-                spin relaxation data. Comparison between the rotational
sheet with large order parameter, the rotational relaxation is                    diﬀusion coeﬃcients and spin relaxation times between
dominated by timescales of ∼5.5 and ∼8 ns, matching with the                      simulations and experiments suggested that the overall
protein overall rotation. Also, the dynamics of residue 322 in                    Brownian tumbling of proteins is too rapid in the simulations,
the ﬂexible loop of PaTonB is dominated by the timescales                         in agreement with the previous report suggesting that the
around ∼8 ns corresponding to the protein overall rotation;                       discrepancy arises from the inaccuracies in water models.19,29,32
however, the fast motions from internal mobility are more                         Scaling down the anisotropic diﬀusion coeﬃcients in the
evident than for the rigid β-sheet residue. This is in agreement                  simulation data led to a good agreement with the experimental
with smaller order parameter observed in the ﬂexible loop                         data. Overall rotational diﬀusion coeﬃcients were over-
residues. On the other hand, the rotational dynamics of residue                   estimated by a factor of ∼3 in the HpTonB-92 simulations
341 in the ﬂexible N-terminus of PaTonB is dominated by                           with the tip3p water model, in line with previous
timescales below 3 ns, most likely related to the internal motion                 studies.28−30,77 Simulations with tip4p and OPC4 water models
of the protein. Contributions from timescales around ∼13 ns to                    gave the spin relaxation times in reasonable agreement with
                                                                           6566                                                   DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                        J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                    Article

experiments with scaling factors of ∼1−1.2, which are                              (4) Eisenmesser, E. Z.; Millet, O.; Labeikovsky, W.; Korzhnev, D. M.;
signiﬁcantly less than that for tip3p. The scaling factors for                   Wolf-Watz, M.; Bosco, D. A.; Skalicky, J. J.; Kay, L. E.; Kern, D.
diﬀerent proteins with diﬀerent water models are summarized                      Intrinsic Dynamics of an Enzyme Underlies Catalysis. Nature 2005,
in Table S1.                                                                     438, 117−121.
   The similarity between the correlation functions from the                       (5) Van den Bedem, H.; Fraser, J. S. Integrative, Dynamic Structural
                                                                                 Biology at Atomic Resolution−It’s About Time. Nat. Methods 2015,
original MD trajectory and the new correlation functions from
                                                                                 12, 307−318.
eq 13 suggests that the usage of the inertia axes and the                          (6) Lewandowski, J. R.; Halse, M. E.; Blackledge, M.; Emsley, L.
separation of internal and the overall rotational motions (eq 6)                 Direct Observation of Hierarchical Protein Dynamics. Science 2015,
are good approximations for the above investigated proteins.                     348, 578−581.
This is in line with the previous studies of other proteins with                   (7) Lamley, J. M.; Lougher, M. J.; Sass, H. J.; Rogowski, M.; Grzesiek,
well-deﬁned structure.10,29 However, it remains to be seen how                   S.; Lewandowski, J. R. Unraveling the Complexity of Protein Backbone
well this and other related approaches28,30,78 will succeed for                  Dynamics with Combined 13C and 15N Solid-state NMR Relaxation
intrinsically disordered proteins without the well-deﬁned shape.                 Measurements. Phys. Chem. Chem. Phys. 2015, 17, 21997−22008.
Because the correction of the incorrect overall rotational                         (8) Yang, D.; Kay, L. E. Contributions to Conformational Entropy
diﬀusion due to the water model may become highly                                Arising from Bond Vector Fluctuations Measured from NMR-Derived
complicated for such proteins, it may be necessary to employ                     Order Parameters: Application to Protein Folding. J. Mol. Biol. 1996,
a water model giving correct overall rotational diﬀusion                         263, 369−382.
coeﬃcients for biomolecules.19,32                                                  (9) Kasinath, V.; Sharp, K. A.; Wand, A. J. Microscopic Insights into
                                                                                 the NMR Relaxation-Based Protein Conformational Entropy Meter. J.
   As further demonstrated in ref 35, the approach presented in
                                                                                 Am. Chem. Soc. 2013, 135, 15092−15100.
this work can be used to interpret the rotational dynamics of                      (10) Allnér, O.; Foloppe, N.; Nilsson, L. Motions and Entropies in
proteins with anisotropic shape from 15N spin relaxation data                    Proteins as Seen in NMR Relaxation Experiments and Molecular
measured only with one magnetic ﬁeld strength. This is a                         Dynamics Simulations. J. Phys. Chem. B 2015, 119, 1114−1128.
signiﬁcant advancement over currently available methods,                           (11) Solomentsev, G.; Diehl, C.; Akke, M. Conformational Entropy
which may not be applicable in such cases, even though                           of FK506 Binding to FKBP12 Determined by Nuclear Magnetic
experimental data would be measured with multiple magnetic                       Resonance Relaxation and Molecular Dynamics Simulations. Bio-
ﬁeld strengths.                                                                  chemistry 2018, 57, 1451−1461.

■    ASSOCIATED CONTENT
* Supporting Information
 S
                                                                                   (12) Akke, M.; Brueschweiler, R.; Palmer, A. G. NMR Order
                                                                                 Parameters and Free Energy: an Analytical Approach and Its
                                                                                 Application to Cooperative Calcium(2+) Binding by Calbindin D9k.
                                                                                 J. Am. Chem. Soc. 1993, 115, 9832−9833.
The Supporting Information is available free of charge on the
                                                                                   (13) Sanchez-Medina, C.; Sekhar, A.; Vallurupalli, P.; Cerminara, M.;
ACS Publications website at DOI: 10.1021/acs.jpcb.8b02250.                       Muñoz, V.; Kay, L. E. Probing the Free Energy Landscape of the Fast-
     Mean square angle deviations of PaTonB-96 simulations                       Folding gpW Protein by Relaxation Dispersion NMR. J. Am. Chem.
     with tip4p water model at 310 K and 298 K and accuracy                      Soc. 2014, 136, 7444−7451.
     estimation of the scaling factors for the rotational                          (14) Best, R. B.; Vendruscolo, M. Determination of Protein
     diﬀusion (PDF)                                                              Structures Consistent with NMR Order Parameters. J. Am. Chem.

■
                                                                                 Soc. 2004, 126, 8090−8091.
                                                                                   (15) Showalter, S. A.; Brüschweiler, R. Validation of Molecular
     AUTHOR INFORMATION                                                          Dynamics Simulations of Biomolecules Using NMR Spin Relaxation as
Corresponding Author                                                             Benchmarks: Application to the AMBER99SB Force Field. J. Chem.
*E-mail: samuli.ollila@helsinki.ﬁ.                                               Theory Comput. 2007, 3, 961−975.
ORCID                                                                              (16) Showalter, S. A.; Johnson, E.; Rance, M.; Brüschweiler, R.
                                                                                 Toward Quantitative Interpretation of Methyl Side-Chain Dynamics
O. H. Samuli Ollila: 0000-0002-8728-1006                                         from NMR by Molecular Dynamics Simulations. J. Am. Chem. Soc.
Hideo Iwaï: 0000-0001-7376-5264                                                  2007, 129, 14146−14147.
Notes                                                                              (17) Maragakis, P.; Lindorff-Larsen, K.; Eastwood, M. P.; Dror, R.
The authors declare no competing ﬁnancial interest.                              O.; Klepeis, J. L.; Arkin, I. T.; Jensen, M. Ø.; Xu, H.; Trbovic, N.;

■   ACKNOWLEDGMENTS
Academy of Finland (277335) and Sigrid Jusélius Foundation
                                                                                 Friesner, R. A.; et al. Microsecond Molecular Dynamics Simulation
                                                                                 Shows Effect of Slow Loop Dynamics on Backbone Amide Order
                                                                                 Parameters of Proteins. J. Phys. Chem. B 2008, 112, 6155−6158.
                                                                                   (18) Trbovic, N.; Kim, B.; Friesner, R. A.; Palmer, A. G. Structural
are acknowledged for the ﬁnancial support to complete this                       Analysis of Protein Dynamics by MD Simulations and NMR Spin-
work. The Finnish Biological NMR Center is supported by                          relaxation. Proteins: Struct., Funct., Bioinf. 2008, 71, 684−694.
Biocenter Finland and HiLIFE-INFRA. We acknowledge CSC-                            (19) Debiec, K. T.; Cerutti, D. S.; Baker, L. R.; Gronenborn, A. M.;
IT center for science for computational resources.

■
                                                                                 Case, D. A.; Chong, L. T. Further along the Road Less Traveled:
                                                                                 AMBER ff15ipq, an Original Protein Force Field Built on a Self-
     REFERENCES                                                                  Consistent Physical Model. J. Chem. Theory Comput. 2016, 12, 3926−
 (1) Jarymowycz, V. A.; Stone, M. J. Fast Time Scale Dynamics of                 3947.
Protein Backbones: NMR Relaxation Methods, Applications, and                       (20) Hoffmann, F.; Mulder, F. A. A.; Schäfer, L. V. Accurate Methyl
Functional Consequences. Chem. Rev. 2006, 106, 1624−1671.                        Group Dynamics in Protein Simulations with AMBER Force Fields. J.
 (2) Korzhnev, D. M.; Billeter, M.; Arseniev, A. S.; Orekhov, V. Y.              Phys. Chem. B 2018, 122, 5038−5048, DOI: 10.1021/
NMR Studies of Brownian Tumbling and Internal Motions in                         acs.jpcb.8b02769.
Proteins. Prog. Nucl. Magn. Reson. Spectrosc. 2001, 38, 197−266.                   (21) Debiec, K. T.; Whitley, M. J.; Koharudin, L. M. I.; Chong, L. T.;
 (3) Mulder, F. A. A.; Mittermaier, A.; Hon, B.; Dahlquist, F. W.; Kay,          Gronenborn, A. M. Integrating NMR, SAXS, and Atomistic
L. E. Studying Excited States of Proteins by NMR Spectroscopy. Nat.              Simulations: Structure and Dynamics of a Two-Domain Protein.
Struct. Mol. Biol. 2001, 8, 932−935.                                             Biophys. J. 2018, 114, 839−855.

                                                                          6567                                                        DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                            J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                     Article

  (22) Wennerstroem, H.; Lindman, B.; Soederman, O.; Drakenberg,                  Selective Order Parameter Analysis of NMR Relaxation Data. J. Chem.
T.; Rosenholm, J. B. Carbon-13 Magnetic Relaxation in Micellar                    Theory Comput. 2017, 13, 3276−3289.
Solutions. Influence of Aggregate Motion on T1. J. Am. Chem. Soc.                   (44) Gu, Y.; Li, D.-W.; Brüschweiler, R. NMR Order Parameter
1979, 101, 6860−6864.                                                             Determination from Long Molecular Dynamics Trajectories for
  (23) Lipari, G.; Szabo, A. Model-Free Approach to the Interpretation            Objective Comparison with Experiment. J. Chem. Theory Comput.
of Nuclear Magnetic Resonance Relaxation in Macromolecules. 1.                    2014, 10, 2599−2607.
Theory and Range of Validity. J. Am. Chem. Soc. 1982, 104, 4546−                    (45) Ollila, O. H. S. MD simulation data for Pseudomonas aeruginosa
4559.                                                                             TonB-CTD. Amber ﬀ99SB-ILDN, tip3p, 298K, Gromacs, 2018, http://
  (24) Woessner, D. E. Nuclear Spin Relaxation in Ellipsoids                      dx.doi.org/10.5281/zenodo.1244108.
Undergoing Rotational Brownian Motion. J. Chem. Phys. 1962, 37,                     (46) Ollila, O. H. S. MD simulation data for Pseudomonas aeruginosa
647−654.                                                                          TonB-CTD. Amber ﬀ99SB-ILDN, tip4p, 298K, Gromacs, 2017, https://
  (25) Shimizu, H. Effect of Molecular Shape on Nuclear Magnetic                  doi.org/10.5281/zenodo.1010415.
Relaxation. J. Chem. Phys. 1962, 37, 765−778.                                       (47) Ollila, O. H. S. MD simulation data for Pseudomonas aeruginosa
  (26) Luginbühl, P.; Pervushin, K. V.; Iwai, H.; Wüthrich, K.                  TonB-CTD. Amber ﬀ99SB-ILDN, tip4p, 310K, Gromacs, 2017, https://
Anisotropic Molecular Rotational Diffusion in 15N Spin Relaxation                 doi.org/10.5281/zenodo.1010405.
Studies of Protein Mobility. Biochemistry 1997, 36, 7305−7312.                      (48) Ollila, O. H. S. MD simulation data for Pseudomonas aeruginosa
  (27) Blake-Hall, J.; Walker, O.; Fushman, D. In Protein NMR                     TonB-CTD. Amber ﬀ99SB-ILDN, OPC4, 310K, Gromacs, 2017,
Techniques; Downing, A. K., Ed.; Humana Press: Totowa, NJ, 2004; pp               https://doi.org/10.5281/zenodo.1010437.
139−159.                                                                            (49) Ollila, O. H. S. MD simulation data for Helicobacter pylori TonB-
  (28) Prompers, J. J.; Brüschweiler, R. General Framework for                   CTD (residues 194-285) (PDB ID: 5LW8; BMRB entry: 34043).
Studying the Dynamics of Folded and Nonfolded Proteins by NMR                     Amber ﬀ99SB-ILDN, tip3p, 310K, Gromacs, 2017, https://doi.org/10.
Relaxation Spectroscopy and MD Simulation. J. Am. Chem. Soc. 2002,                5281/zenodo.1010231.
124, 4522−4534.                                                                     (50) Ollila, O. H. S. MD simulation data for Helicobacter pylori TonB-
  (29) Wong, V.; Case, D. A. Evaluating Rotational Diffusion from                 CTD (residues 194-285) (PDB ID: 5LW8; BMRB entry: 34043).
Protein MD Simulations. J. Phys. Chem. B 2008, 112, 6013−6024.                    Amber ﬀ99SB-ILDN, tip3p, 303K, Gromacs, 2017, https://doi.org/10.
  (30) Anderson, J. S.; LeMaster, D. M. Rotational Velocity Rescaling             5281/zenodo.1010141.
of Molecular Dynamics Trajectories for Direct Prediction of Protein                 (51) Ollila, O. H. S. MD simulation data for Helicobacter pylori TonB-
NMR Relaxation. Biophys. Chem. 2012, 168, 28−39.                                  CTD (residues 194-285) (PDB ID: 5LW8; BMRB entry: 34043).
  (31) Salvi, N.; Abyzov, A.; Blackledge, M. Multi-Timescale Dynamics             Amber ﬀ99SB-ILDN, tip4p, 310K, Gromacs, 2017, https://doi.org/10.
in Intrinsically Disordered Proteins from NMR Relaxation and
                                                                                  5281/zenodo.1010237.
Molecular Simulation. J. Phys. Chem. Lett. 2016, 7, 2483−2489.                      (52) Ollila, O. H. S. MD simulation data for Helicobacter pylori TonB-
  (32) Takemura, K.; Kitao, A. Water Model Tuning for Improved
                                                                                  CTD (residues 194-285) (PDB ID: 5LW8; BMRB entry: 34043).
Reproduction of Rotational Diffusion and NMR Spectral Density. J.
                                                                                  Amber ﬀ99SB-ILDN, tip4p, 303K, Gromacs, 2017, https://doi.org/10.
Phys. Chem. B 2012, 116, 6279−6287.
                                                                                  5281/zenodo.1010351.
  (33) Lu, C.-Y.; Bout, D. A. V. Effect of Finite Trajectory Length on
                                                                                    (53) Ollila, O. H. S.. MD simulation data for Helicobacter pylori
the Correlation Function Analysis of Single Molecule Data. J. Chem.
                                                                                  TonB-CTD (residues 194-285) (PDB ID: 5LW8; BMRB entry:
Phys. 2006, 125, 124701.
  (34) Ciragan, A.; Aranko, A. S.; Tascon, I.; Iwaï, H. Salt-inducible            34043). Amber ﬀ99SB-ILDN, OPC4, 310K, Gromacs, 2017, https://doi.
Protein Splicing in cis and trans by Inteins from Extremely Halophilic            org/10.5281/zenodo.1010356.
Archaea as a Novel Protein-Engineering Tool. J. Mol. Biol. 2016, 428,               (54) Abraham, M. J.; Murtola, T.; Schulz, R.; Páll, S.; Smith, J. C.;
4573−4588.                                                                        Hess, B.; Lindahl, E. GROMACS: High Performance Molecular
  (35) Oeemig, J. S.; Ollila, O. H. S.; Iwaï, H. The NMR structure of             Simulations Through Multi-level Parallelism from Laptops to
the C-terminal domain of TonB protein from Pseudomonas aeruginosa,                Supercomputers. SoftwareX 2015, 1−2, 19−25.
2018, submitted.                                                                    (55) Lindorff-Larsen, K.; Piana, S.; Palmo, K.; Maragakis, P.; Klepeis,
  (36) Abragam, A. The Principles of Nuclear Magnetism; Oxford                    J. L.; Dror, R. O.; Shaw, D. E. Improved Side-chain Torsion Potentials
University Press, 1961.                                                           for the Amber ff99SB Protein Force Field. Proteins: Struct., Funct.,
  (37) Kay, L. E.; Torchia, D. A.; Bax, A. Backbone Dynamics of                   Bioinf. 2010, 78, 1950−1958.
Proteins as Studied by Nitrogen-15 Inverse Detected Heteronuclear                   (56) Jorgensen, W. L.; Chandrasekhar, J.; Madura, J. D.; Impey, R.
NMR Spectroscopy: Application to Staphylococcal Nuclease. Bio-                    W.; Klein, M. L. Comparison of Simple Potential Functions for
chemistry 1989, 28, 8972−8979.                                                    Simulating Liquid Water. J. Chem. Phys. 1983, 79, 926−935.
  (38) Hiyama, Y.; Niu, C. H.; Silverton, J. V.; Bavoso, A.; Torchia, D.            (57) Izadi, S.; Anandakrishnan, R.; Onufriev, A. V. Building Water
A. Determination of 15N Chemical Shift Tensor via 15N-2H Dipolar                  Models: A Different Approach. J. Phys. Chem. Lett. 2014, 5, 3863−
Coupling in Boc-glycylglycyl[15N glycine]benzyl ester. J. Am. Chem.               3871.
Soc. 1988, 110, 2378−2383.                                                          (58) Bussi, G.; Donadio, D.; Parrinello, M. Canonical Sampling
  (39) Halle, B. The Physical Basis of Model-free Analysis of NMR                 Through Velocity Rescaling. J. Chem. Phys. 2007, 126, 014101.
Relaxation Data From Proteins and Complex Fluids. J. Chem. Phys.                    (59) Parrinello, M.; Rahman, A. Polymorphic Transitions in Single
2009, 131, 224507.                                                                Crystals: A New Molecular Dynamics Method. J. Appl. Phys. 1981, 52,
  (40) Dosset, P.; Hus, J.-C.; Blackledge, M.; Marion, D. Efficient               7182−7190.
Analysis of Macromolecular Rotational Diffusion from Heteronuclear                  (60) Darden, T.; York, D.; Pedersen, L. Particle Mesh Ewald: An N·
Relaxation Data. J. Biomol. NMR 2000, 16, 23−28.                                  log(N) Method for Ewald Sums in Large Systems. J. Chem. Phys. 1993,
  (41) de la Torre, J. G.; Huertas, M.; Carrasco, B. HYDRONMR:                    98, 10089−10092.
Prediction of NMR Relaxation of Globular Proteins from Atomic-                      (61) Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.;
Level Structures and Hydrodynamic Calculations. J. Magn. Reson.                   Pedersen, L. G. A Smooth Particle Mesh Ewald Potential. J. Chem.
2000, 147, 138−146.                                                               Phys. 1995, 103, 8577−8593.
  (42) Fisette, O.; Lagüe, P.; Gagné, S.; Morin, S. Synergistic                   (62) Hess, B. P-LINCS: A Parallel Linear Constraint Solver for
Applications of MD and NMR for the Study of Biological Systems.                   Molecular Simulation. J. Chem. Theory Comput. 2008, 4, 116−122.
J. Biomed. Biotechnol. 2012, 2012, 254208.                                          (63) Abraham, M.; van der Spoel, D.; Lindahl, E.; Hess, B. The
  (43) Anderson, J. S.; Hernández, G.; LeMaster, D. M. Prediction of             GROMACS development team, GROMACS user manual. Version
Bond Vector Autocorrelation Functions from Larmor Frequency-                      5.0.7, 2015.

                                                                           6568                                                        DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                             J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                           Article

  (64) McGibbon, R. T.; Beauchamp, K. A.; Harrigan, M. P.; Klein, C.;
Swails, J. M.; Hernández, C. X.; Schwantes, C. R.; Wang, L.-P.; Lane,
T. J.; Pande, V. S. MDTraj: A Modern Open Library for the Analysis
of Molecular Dynamics Trajectories. Biophys. J. 2015, 109, 1528−
1532.
  (65) MATLAB, R2016a; The MathWorks, Inc., Natick, Massachu-
setts, United States.
  (66) Nowacka, A.; Bongartz, N. A.; Ollila, O. H. S.; Nylander, T.;
Topgaard, D. Signal Intensities in 1H−13C CP and INEPT MAS
NMR of Liquid Crystals. J. Magn. Reson. 2013, 230, 165−175.
  (67) Ferreira, T. M.; Ollila, O. H. S.; Pigliapochi, R.; Dabkowska, A.
P.; Topgaard, D. Model-free Estimation of the Effective Correlation
Time for C-H Bond Reorientation in Amphiphilic Bilayers: 1H-13C
Solid-state NMR and MD Simulations. J. Chem. Phys. 2015, 142,
044905.
  (68) Ollila, O. H. S. ProteinDynamics, 2017, https://doi.org/10.
5281/zenodo.1288573.
  (69) Barbato, G.; Ikura, M.; Kay, L. E.; Pastor, R. W.; Bax, A.
Backbone Dynamics of Calmodulin Studied by Nitrogen-15 Relaxation
Using Inverse Detected Two-dimensional NMR Spectroscopy: The
Central Helix is Flexible. Biochemistry 1992, 31, 5269−5278.
  (70) Farrow, N. A.; Muhandiram, R.; Singer, A. U.; Pascal, S. M.;
Kay, C. M.; Gish, G.; Shoelson, S. E.; Pawson, T.; Forman-Kay, J. D.;
Kay, L. E. Backbone Dynamics of a Free and a Phosphopeptide-
Complexed Src Homology 2 Domain Studied by 15N NMR
Relaxation. Biochemistry 1994, 33, 5984−6003.
  (71) Krishnan, V. V.; Cosman, M. An Empirical Relationship
Between Rotational Correlation Time and Solvent Accessible Surface
Area. J. Biomol. NMR 1998, 12, 177−182.
  (72) Carper, W. R.; Keller, C. E. Direct Determination of NMR
Correlation Times from Spin-Lattice and Spin-Spin Relaxation Times.
J. Phys. Chem. A 1997, 101, 3246−3250.
  (73) Frishman, D.; Argos, P. Knowledge-based Protein Secondary
Structure Assignment. Proteins: Struct., Funct., Bioinf. 1995, 23, 566−
579.
  (74) Humphrey, W.; Dalke, A.; Schulten, K. VMD − Visual
Molecular Dynamics. J. Mol. Graphics 1996, 14, 33−38.
  (75) Javanainen, M.; Lamberg, A.; Cwiklik, L.; Vattulainen, I.; Ollila,
O. H. S. Atomistic Model for Nearly Quantitative Simulations of
Langmuir Monolayers. Langmuir 2018, 34, 2565−2572.
  (76) Höfling, F.; Franosch, T. Anomalous Transport in the Crowded
World of Biological Cells. Rep. Prog. Phys. 2013, 76, 046602.
  (77) Linke, M.; Köfinger, J.; Hummer, G. Fully Anisotropic
Rotational Diffusion Tensor from Molecular Dynamics Simulations.
J. Phys. Chem. B 2018, 122, 5630.
  (78) Chen, P.-c.; Hologne, M.; Walker, O.; Hennig, J. Ab Initio
Prediction of NMR Spin Relaxation Parameters from Molecular
Dynamics Simulations. J. Chem. Theory Comput. 2018, 14, 1009−1019.

                                                                            6569             DOI: 10.1021/acs.jpcb.8b02250
                                                                                   J. Phys. Chem. B 2018, 122, 6559−6569


---

# How to learn from inconsistencies: Integrating molecular simulations with experimental data

**Authors:** Simone Orioli, Andreas Haahr Larsen, Sandro Bottaro, Kresten Lindorff-Larsen
**Year:** 2020
**Venue:** Progress in Molecular Biology and Translational Science
**DOI:** 10.1016/bs.pmbts.2019.12.006
**Source PDF URL:** https://arxiv.org/pdf/1909.06780
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

How to learn from inconsistencies: Integrating

arXiv:1909.06780v2 [physics.chem-ph] 8 Dec 2019
                                                       molecular simulations with experimental data
                                                      Simone Orioli1,2 *, Andreas Haahr Larsen1,2,3 *, Sandro Bottaro1,4
                                                                         and Kresten Lindorff-Larsen1

                                                    Structural Biology and NMR Laboratory & Linderstrøm-Lang Centre for Protein
                                                  Science, Department of Biology, University of Copenhagen, Copenhagen, Denmark. 2
                                                  Structural Biophysics, Niels Bohr Institute, Faculty of Science, University of Copen-
                                                  hagen, Copenhagen, Denmark. 3 Present address: Structural Bioinformatics and
                                                  Computational Biochemistry Unit, Department of Biochemistry, University of Ox-
                                                  ford, Oxford, United Kingdom. 4 Atomistic Simulations Laboratory, Istituto Italiano
                                                  di Tecnologia, Genova, Italy. ∗ These authors contributed equally to this work
                                                  Keywords: Molecular simulations; Integration with experiments; Force fields; Maxi-
                                                  mum Entropy; Bayesian Methods; Time-dependent; Time-resolved

                                                                                          Abstract
                                                             Molecular simulations and biophysical experiments can be used to pro-
                                                         vide independent and complementary insights into the molecular origin of
                                                         biological processes. A particularly useful strategy is to use molecular sim-
                                                         ulations as a modelling tool to interpret experimental measurements, and
                                                         to use experimental data to refine our biophysical models. Thus, explicit
                                                         integration and synergy between molecular simulations and experiments
                                                         is fundamental for furthering our understanding of biological processes.
                                                         This is especially true in the case where discrepancies between measured
                                                         and simulated observables emerge. In this chapter, we provide an overview
                                                         of some of the core ideas behind methods that were developed to improve
                                                         the consistency between experimental information and numerical predic-
                                                         tions. We distinguish between situations where experiments are used to
                                                         refine our understanding and models of specific systems, and situations
                                                         where experiments are used more generally to refine transferable models.
                                                         We discuss different philosophies and attempt to unify them in a single
                                                         framework. Until now, such integration between experiments and simula-
                                                         tions have mostly been applied to equilibrium data, and we discuss more
                                                         recent developments aimed to analyse time-dependent or time-resolved
                                                         data.

Contents
1 Introduction                                                                 3

2 Reweighting strategies                                                        5
  2.1 Maximum Entropy . . . . . . . . . . . . . . . . . . . . . . . . . .       7
  2.2 Maximum Parsimony . . . . . . . . . . . . . . . . . . . . . . . . .       9
  2.3 Bayesian inference or MaxPrior . . . . . . . . . . . . . . . . . . .     10
  2.4 Comparing MaxEnt, MaxPars and MaxPrior reweighting . . . .               13
      2.4.1 Interpretation of the results . . . . . . . . . . . . . . . . .    13
      2.4.2 General applicability . . . . . . . . . . . . . . . . . . . . .    14
      2.4.3 Imperfect force fields . . . . . . . . . . . . . . . . . . . . .   15
  2.5 Numerical challenges . . . . . . . . . . . . . . . . . . . . . . . . .   15

3 Experiment-biased simulations                                              17
  3.1 Maximum Entropy . . . . . . . . . . . . . . . . . . . . . . . . . . 18
  3.2 Empirical energy terms . . . . . . . . . . . . . . . . . . . . . . . 18
  3.3 Bayesian inference . . . . . . . . . . . . . . . . . . . . . . . . . . 19
  3.4 Comparing reweighting with experiment-biased methods . . . . . 20
      3.4.1 Adaptability . . . . . . . . . . . . . . . . . . . . . . . . . 20
      3.4.2 Forward models . . . . . . . . . . . . . . . . . . . . . . . . 21
      3.4.3 Imperfect force fields . . . . . . . . . . . . . . . . . . . . . 21

4 Force field optimisation                                                   22
  4.1 Background on force field parametrisation . . . . . . . . . . . . . 22
  4.2 Refining Protein and RNA force fields . . . . . . . . . . . . . . . 24
      4.2.1 Proteins . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
      4.2.2 RNA . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

5 Matching time-dependent and time-resolved data                            30
  5.1 Maximum Entropy and Likelihood in dynamical systems . . . . . 32
  5.2 Maximum Caliber . . . . . . . . . . . . . . . . . . . . . . . . . . 34
  5.3 Average Block Selection . . . . . . . . . . . . . . . . . . . . . . . 37

6 Challenges                                                                 39
  6.1 Balance between simulations and experimental data . . . . . . . 39
  6.2 Interplay between reweighting and force field corrections . . . . . 41
  6.3 Using kinetic data to reweight equilibrium ensembles . . . . . . . 42
  6.4 A new generation of force fields . . . . . . . . . . . . . . . . . . . 42

7 Conclusions                                                                  44

1    Introduction
Molecular mechanics simulations of biological systems have matured over the
last decades, to a state where reliable predictions and interpretations of biolog-
ical phenomena can be achieved [1, 2]. Simulations can readily be used either
before experiments to suggest hypotheses and design experiments, or after ex-
periments to analyse and interpret the data. With simulations it is possible to
probe timescales and spatial details that are, yet, impossible to access exper-
imentally, and thus they provide a unique tool to study, e.g. conformational
transitions [3–7], signalling events [8], ion transport [8, 9], and many other phe-
nomena. Since most experimental observables are averaged over time and a large
number of molecules, simulations can help resolve the underlying structural and
dynamical distribution with atomistic spatial accuracy and femtosecond time
resolution.
    As simulations are in essence a theoretical framework, experimental verifica-
tion is pivotal and there are still, in many cases, significant differences between
experimental data and the corresponding observables calculated from state-of-
the art simulations [10]. These discrepancies are usually due to imperfect force
fields [11–14], insufficient sampling [15] or inaccurate forward models [16]. Even
with accurate forward models and robust sampling, however, the quality of
the simulation results are bound by the accuracy of the underlying force field
[13]. Indeed, molecular mechanics is intrinsically limited by the fact that it em-
ploys classical approximations for phenomena that are known to happen on a
quantum scale. Force fields have been developed to approximate these quantum
interactions within a classical framework, in such a way to balance between com-
putational simplicity and accuracy: thus, an exact match is not to be expected
and synergy between simulations and experiments remains of fundamental im-
portance. Substantial efforts of the biophysical community have been therefore
directed towards the development of methods that correct the results of simu-
lations by accounting for experimental information, either in a system specific
or generalisable fashion. In this chapter we provide a self-contained overview of
the principles and strategies that have been applied to infer conformational en-
sembles, i.e. collections of structures reflecting the dynamism and plasticity of
a molecule, as well as to improve force fields using experimental data. In other
words, we will make a clear cut distinction between system-specific and general
force field corrections: in the former case, simulations are performed according
to experimental conditions, and if inconsistencies emerge, the resulting ensemble
is corrected according to the available experimental information; in the latter

case, instead, discrepancies between simulations and experimental observables
are used to actively improve the physical potential employed to describe the
system. We note that the goal of the chapter is not to be comprehensive of all
the literature that has been previously published: rather, it focuses on some
cornerstone principles and methods that summarise the efforts of the commu-
nity. For this reason we also focus mostly on the methods and theory, and only
provide few examples of applications.
    This chapter is meant for readers experienced in molecular simulations and
comfortable with the fundamentals of statistics. It is particularly suited for
scientists that approach the combination of experiments with simulations for
the first time or readers interested in a non-technical overview of the field.
    The chapter is comprised of seven sections, each one concerned with a dif-
ferent aspect of the literature on the subject. Section 2 is dedicated to the
description of some of the main strategies to obtain consistency between sim-
ulation and data by manipulating the ensemble after simulations have been
performed. Differently, in section 3 we will discuss how consistency can be
achieved by introducing a system-specific empirical energy term in the force
field. In this case, the refinement step occurs before the actual simulation, as
the experimental bias will guide the sampling towards only the relevant regions
of conformational space. In section 4 we discuss how to employ experimental
data to refine the physical description of macromolecules, i.e. the force field,
instead of the conformational ensemble of a particular system. Like the biased
force field approaches described in section 3, these methods also adjust the force
field before the production simulation. In section 5 we discuss how to combine
time-dependent and time-resolved data with simulations. This is particularly
relevant, as computational power [17–20] and enhanced sampling techniques
[3, 21] have pushed the reachable timescales to the ones resolved by some ex-
perimental techniques. In section 6 we discuss some of the most important
overall challenges arising from combining experimental data and simulations,
and, finally, in section 7 we conclude by summarising similarities and differ-
ences between the various approaches. We thus aim to give an overview of the
present state of the field as well as pointing out key aspects where further collec-
tive effort is needed to improve the predictive power of combined computational
and experimental methods for structural studies of biological systems.

2     Reweighting strategies
Consistency between simulations and experimental data can in many cases be
achieved by reweighting a trajectory (or a set of trajectories) obtained with a
given force field (Fig. 1). Let us assume to perform a molecular dynamics (MD)
or Monte Carlo (MC) simulation and to save N snapshots, Xi , . . . , XN , from
the trajectory for analysis. Each frame in the simulation is given an initial
weight that reflects the population of that structure as predicted by the force
field. We denote the initial set of weights, w0 = w10 , w20 , ..., wN
                                                                      , the reference
distribution and we assume them to be non-negative and normalised as prob-
           P 0
abilities,   i wi = 1. When performing a standard MD/MC simulation and
under the assumption that enough sampling has been performed, the initial
weights are constant, wi0 = 1/N , as such simulations generate conformations
distributed according to the Boltzmann distribution. When using enhanced
sampling techniques that do not directly sample the Boltzmann distribution or,
in the case of shorter off-equilibrium simulations, the initial weights are in gen-
eral non-uniform [22]. Given the N snapshots and the reference distribution, a
static observable can, in the simplest case, be calculated as a weighted ensemble
average:
                                           N
                                           X
                           hOcalc i(w) =         wi Ocalc (Xi ).                    (1)
                                           i=1

Some experimental quantities (e.g. NMR relaxation rates and other inherently
time-dependent observables) cannot generally be expressed as linear ensemble
averages over individual structures, i.e. employing Eq. (1). Therefore, through-
out the manuscript the validity of Eq. (1) will be taken as a working assumption
until section 5, where we will discuss the case of time-dependent observables.
    In a reweighting process, the weights are modified until the calculated ob-
servables become consistent with corresponding experimental observables, Ojexp ,
where j = 1, . . . , M . We deonote the reweighted set of weights, w = w1 , w2 , ..., wN ,
the optimal distribution [23]. Unfortunately, many possible sets of weights can
lead to the same averages, and thus to consistency with data. I.e. it is an ill-
posed problem, and strategies are therefore needed to regularise the problem,
so the most optimal of these distributions can be selected. There exist several
strategies to regularise and solve the resulting optimisation problem [24], and
we here focus on three of them: the principle of maximum entropy (MaxEnt,
section 2.1), the principle of maximum parsimony (MaxPars, section 2.2) and
Bayesian inference (MaxPrior, section 2.3). Each method encodes a different

                                                      Simulation                         Analysis

   Experimental                Experiment-Biased FF                    Sampling                           Probability density
    information

                                                                                            Reweighting
                  Simulation                           Analysis                                           MaxEnt/MaxPrior

      Bare FF                       Sampling                       Probability density

                                                                                                               MaxPars

Figure 1: Overview of methods to achieve consistency between simulation and
experimental data for the distribution of a generic static observable. All methods
start with an initial force field Eff (x) (‘bare’ FF, blue line) which is either
employed as is or modified in accordance to some experimentally driven bias
(experiment-biased FF, red dashed line). In the upper case, the biased force field
is sampled to directly generate an observable distribution which is coherent with
experimental data. In the lower case, the observable distribution is subsequently
reweighted against experimental data using either the MaxEnt/MaxPrior or
MaxPars principles to yield some reweighted distributions (red dashed line).

philosophy for what it means for a set of weights to be optimal, which translates
into different optimal distributions after reweighting.

2.1    Maximum Entropy
The principle of maximum entropy (MaxEnt) [25] states that the optimal dis-
tribution is the one adding the least amount of information given some imposed
constraints, e.g. hOcalc i = Oexp . In other words, the solution with highest en-
tropy and still consistent with the data is considered optimal. In this context,
entropy is quantified via the relative entropy which we define as the negative of
the Kullback-Leibler divergence [26]:
                                     N                       
                                     X                  wi
                          S(w) = −         wi log                 ,           (2)
                                     i=1
                                                        wi0

where wi0 and wi are the weights of frame Xi before and after reweighting.
Other expressions for the entropy are possible [27, 28], but Eq. (2) is usually
preferred [29–32]. As the distributions of initial and refined weights diverges,
S(w) becomes smaller, and vice versa. In the simplest case, the set of weights
that maximises the entropy is chosen by the only constraint that the weights
are normalised as probabilities, i.e. we look for weights for which the function
              P
g0 (w) = 1 − i wi is zero. This problem can be solved by constructing a
Lagrangian:

                         L(w, λ0 ) = S(w) − λ0 g0 (w),                        (3)

where λ0 is a Lagrange multiplier. The solution of the set of equations

                                     ∇L = 0                                   (4)

gives the highest entropy weights which fulfil the normalisation condition, which
are simply w = w0 . It is clear then, that the problem is interesting only
when more constraints are introduced. For example, exact consistency with
a given set of experimental data can be imposed via functions of the form
gj (w) = Ojexp − hOjcalc i(w). The Lagrangian in Eq. (3), in the case of M
experimental constraints and the normalisation constraint, becomes:
                                              M
                                              X
                        L(w, λ) = S(w) −            λj gj (w),                (5)
                                              j=0

where a Lagrange multiplier λj is introduced for each constraint. The solution of
Eq. (4) for the Lagrangian in Eq. (5) provides weights that ensure consistency

between the reweighted trajectory and the experimental data. The optimal
weights are uniquely given in terms of the M Lagrange multipliers [33–37]:
                                      h P                  i
                                          M
                             wi0 exp − j=0 λj Ojcalc (Xi )
                wi (λ) = P              h P                    i,          (6)
                            N      0 exp −  M       calc (X )
                            k=0 kw             λ O
                                            j=0 j j          k

where Ojcalc (Xi ) is the value of the j-th observable, as calculated from the i-
th frame in the simulation. Note that the denominator just ensures proper
normalisation of the weights.
    Fitting data tightly to gain full consistency by imposed constraints might,
however, be unrealistic and lead to overfitting because of errors in the data and
in the model [34]. Indeed, experimental observables are only known with some
limited certainty and, likewise, forward models used to calculate observables
from simulations have an associated uncertainty [16]. Systematic errors in the
data lead to further disagreement with the model [23, 38, 39], and finally, the
finite number of structures N used to compute the theoretical observable (see
Eq. (1)) introduces additional error to the estimated averages [39]. All these
effects add up to an effective uncertainty for each observable, σj . Therefore it is
generally preferable to apply restraints rather than constraints, i.e. to impose
consistency with the data only within the estimated uncertainty (restraining)
rather than exactly (constraining). This translates into relaxing the equality
hOcalc i = Oexp to a similarity hOcalc i ∼ Oexp within a given threshold.
    There are two main strategies to introduce restraints in the MaxEnt method
using Lagrange multipliers. The first one consists in modifying the constraints
in such a way that the calculated and experimental observables are allowed to
differ by some small quantity ε, i.e. gjσ (w) = (Ojexp + ε(λj , σj )) − hOjcalc i(w). ε
depends on the effective uncertainty, σj and the Lagrange multiplier associated
to the constraint, λj [36, 40, 41]. The second way to include experimental errors
was introduced by Gull and Daniel [42] and, in the assumption of normally
distributed errors, describes the discrepancy between data and model via the
χ2 distribution:
                                                               !2
                                 M
                                 X      Ojexp − hOjcalc i(w)
                      χ (w) =                                       ,              (7)
                                 j=1
                                                σj

The expectation value of χ2 is equal to the number of degrees of freedom ν, so
a reduced χ2 can be defined such that its expectation value is unity,
                                               1 2
                                       χ2r =     χ .                               (8)
                                               ν

Experimental restraints can thus be included by imposing the constraint func-
tion gχ2r (w) = χ2r (w)−1 to be zero, with a Lagrange multiplier that we call θ−1 ,
and whose role we discuss in further detail below. This treatment is correct in
the assumption of normally distributed errors and for datasets that guarantee
χ2r = 1. The latter assumption is not safe, as point estimates can deviate from
the χ2r expectation value: more details on this are provided in section 6. To
overcome this problem, the optimal distribution can be obtained by minimising
the equation [23, 29, 32]

                         TMaxEnt (w) = χ2 (w) − θS(w),                         (9)

where θ is treated as an adjustable parameter rather than a Lagrange multiplier,
and controls how tightly the data should be fitted. The solution is then said
to be regularised by the entropy, i.e. at a fixed value of θ the optimal solution
is the one with the highest entropy S(w) among the ones that minimise the
discrepancy with the data, χ2 (w).
    After reweighting, some of the weights may be close to zero and the cor-
responding structures will thus effectively be ignored in the calculation of the
new averages. MaxEnt ensures that the optimised ensemble preserves as many
structures from the reference one as possible. In this sense, the entropy term
S can be interpreted via a more intuitive quantity, φeff , which represents the
effective fraction of frames used in the reweighted ensemble compared to the
initial ensemble [32]:

                              φeff (w) = exp[S(w)].                           (10)

If the reference distribution is unaltered, φeff (w = w0 ) = 1. In the opposite
extreme all weight is given to a few frames of the simulation and φeff (w)  1,
meaning that the force field is in poor agreement with data and/or sampling is
poor. We note that other possibilities exist to estimate the effective size of the
sample, e.g. the Kish formula [43, 44]:
                                     P         2
                                         N
                                         i=1 wi
                                K = PN             .                          (11)
                                          i=1 wi

When a single frame is dominant over all the others, Eq. (11) returns K = 1,
while in a situation where no particular frame is preferred one has K = N .

2.2    Maximum Parsimony
The principle of Maximum Parsimony (MaxPars), also referred to as Occam’s
razor, is another strategy that can help choosing among several models consis-

tent with the data. As we shall discuss later, many different interpretations of
Occam’s razor exist. In this section, the principle is interpreted as follows: the
optimal distribution coherent with a given set of data is the one providing the
smallest possible ensemble while still fitting the data. The basic idea is that if a
model (ensemble) with few parameters (structures) can explain the data, there
is no reason to further complicate the model by introducing more parameters.
The above principle can for example be quantified by the Akaike information
criterion [45]:

                               AIC = 2n − 2 log L,                             (12)

where the optimal solution is found by simultaneously maximising the likeli-
hood, L, that quantifies agreement with experimental data, and minimising the
number of model parameters, n. While the number n is effectively equal to
the number of frames in the ensemble, it is customary to associate it to the
number of non-zero weights, so n  N . For normally distributed experimental
restraints one has log L = −χ2 (w)/2, so:

                      TMaxPars (w, n) = AIC = χ2 (w) + θn,                     (13)

where θ = 2 if Eq. (12) is directly applied. θ was introduced here to emphasise
similarity with the MaxEnt methods, i.e. that the difference is in the form of
the regularisation term.
    The Akaike information criterion was directly applied by Bowerman et al.
[46] to find a minimal ensemble of tri-ubiquitin, using MD simulations and
SAXS data. Bouma et al. [47], on the other hand, used θ as a free adjustable
parameter to tune the strength of the MaxPars regularisation term. In most
methods however, the optimal n is found by increasing it by incremental steps
and, for each step, finding the ensemble with lowest χ2 (w). The optimal n
is then found when χ2 (w) has converged, either judged by manual assessment
[48, 49] or by an automatic convergence criterion [50–52], thus avoiding having
to set an explicit value for θ.

2.3    Bayesian inference or MaxPrior
An alternative method to MaxEnt and MaxPars is provided by Bayesian statis-
tics [23, 37, 53, 54]. While MaxEnt regularises the negative log-likelihood by
the entropy, and MaxPars by parsimony, Bayesian inference employs the prior
for the same goal. For this reason we will refer to this approach as MaxPrior.

    In Bayesian inference all available information is expressed by means of prob-
abilities, as captured in Bayes’ theorem:
                                         P (O exp |w, σ)
                     P (w|O exp , σ) =                   P (w).              (14)
                                          P (O exp , σ)

P (w) is called the prior and it quantifies the information known about the sys-
tem prior to the introduction of experimental data. In case of reweighting, it
represents the prior probability associated to the weights, and typically comes
from the distribution encoded in an energy function. The term P (O exp |w, σ),
known as the likelihood L(w), represents the probability of measuring the ex-
perimental observables, given the set of weights and uncertainties. Assuming
normally distributed errors, L(w) is given as:
                                                            
                   P (O exp |w, σ) = L(w) ∝ exp − χ2 (w) .                  (15)
Note that this is not the only possible expression for the likelihood. More com-
plicated expressions, even non-analytical ones, can occur if different types of
data are combined or when sources of error cannot be assumed to be Gaussian
[55, 56]. The term on the left-hand side of Eq. (14) is known as the posterior
and represents the probability of the weights after experimental data have been
considered. Finally, the term in the denominator is treated as a normalisa-
tion constant in which case Bayes’ theorem takes the form of a proportionality
relation:

                     P (w|O exp , σ) ∝ P (O exp |w, σ)P (w).                 (16)

Given Eq. (16), Bayesian inference defines the optimal distribution by following
a two-step procedure: first, the information from data is included, i.e. a like-
lihood function is defined; second, all other forms of data are included, i.e. a
prior on the weights is provided. If we assume the employed force field to rep-
resent the best estimate of our prior knowledge on the system, then the prior
probability P (w) must decrease as w deviates from w0 . This observation can
e.g. be quantified through the relative entropy S(w) from Eq. 2 [32, 57, 58], in
which case the prior takes the form:
                                                
                                           θ
                            P (w) ∝ exp      S(w) .                         (17)

The factor 1/2 is introduced for sake of simplicity of the final result. Other
forms of the prior can be used. For example, Gaussian errors are used as priors
in several reweighting methods [59–62], while other methods assume a Dirichlet

distribution for the weights [63]. If the relative entropy term is used as prior,
Bayesian inference and MaxEnt approaches result in the same regularised ex-
pression. Indeed, by inserting the likelihood (Eq. (15)) and prior (Eq. (17))
into Bayes theorem (Eq. (16)) and taking the negative logarithm, we obtain a
regularised functional, TMaxPrior (w), that must be minimised to find the optimal
distribution, w:

            −2 log P (w|O exp , σ) ∝ TMaxPrior (w) = χ2 (w) − θS(w).           (18)

It is important to note that, differently from the case of MaxEnt where θ was
empirically used to tune the strength of the regularisation term, in a Bayesian
framework the interpretation of θ is clear. Indeed, it accounts fot the uncertainty
on the weights, σwi0 , and thus effectively on the force field, i.e. θ = (σwi0 )−1 .
This means that if the uncertainty on the weights, data and model were known
accurately, θ could be exactly determined. Unfortunately, the uncertainty on
the force field parameters, and thus on the weights, is generally unknown and
θ must therefore be treated as a hyperparameter of the model. In practice, θ
plays a double-role: it expresses our trust in the force field and at the same time
it can be used to compensate for over- or underestimated experimental errors,
as well as errors in the forward model [23, 64]. See more on the determination
of θ in section 6.
    The usefulness of Bayes theorem in refining structural ensembles from sim-
ulations and data is clear from the amount of studies on the subject, all includ-
ing the word Bayesian in their title [23, 31, 38, 39, 50, 57, 59–67] (see also the
overview in [68]). The methodology has become so widespread in the field, that
one could argue that researchers should start stating in the title when Bayesian
methods are not used, rather than the opposite. We note also that different
methods may differ substantially in how and the extent to which they apply the
Bayesian formalism including whether priors are defined over all parameters and
whether these are integrated out during the procedures.
    Several methods combine MaxPars, MaxEnt and MaxPrior approaches (see
an overview in Table 1 in the review by Bonomi et al. [68]). Bayesian priors
can, e.g., be constructed to prefer minimal ensembles [63, 69], thus combining
MaxPrior with MaxPars. Additional information can also be used together with
prior information from the simulation, e.g. secondary structure restraints, like
in the case where MD simulated data are fitted into low-resolution cryo-electron
microscopy density maps [70]. Therefore, the Bayesian approach should be seen
more as a toolbox than an actual principle for selection among ensembles.
    The Bayesian framework also provides an interpretation of the principle of

parsimony, which is different from the Akaike Information Criterion, where the
model with fewer parameters is considered the simplest one. In a Bayesian
setting, the principle of maximum parsimony is a matter of surprise: the fur-
ther a posterior result is from the prior, the more surprising it is. This leads
to a Bayesian Occam’s term: a measure of the distance between the reference
distribution (prior) and the optimal distribution (posterior) [71, 72]. The prin-
ciple is implicitly built into Bayes theorem. In that sense, the S(w) term in the
Bayesian inference and MaxEnt methods can be interpreted as an Occam’s term,
and both these methods could claim to fulfil the principle of maximum parsi-
mony. However, to keep notation clear, we will use the Akaike interpretation of
Occam’s razor.

2.4     Comparing MaxEnt, MaxPars and MaxPrior reweight-
        ing
Different interpretations of the concept of optimal distribution can lead to dra-
matically different conformational ensembles. Indeed, MaxEnt includes as many
configurations of the initial ensemble as possible, while MaxPars tries to include
only the ones that are strictly necessary to model the data. The behaviour of
MaxPrior, on the other hand, depends on the prior employed. In most ap-
proaches however, a term similar to MaxEnt is used, preferring solutions that
are consistent with the reference distribution [68], so that MaxPrior will lead to
solutions with as many frames as possible. Therefore, we will only distinguish
between MaxEnt and MaxPars in the following, when discussing which method
is more appropriate under what circumstances. To our knowledge, no system-
atic and direct comparison of the different reweighting methods have been made.
However, the methods have some clear and important differences that will be
discussed below.

2.4.1   Interpretation of the results

A relevant point of comparison between the methods is how easily the results
are interpreted. The results of the MaxPars method are easier to interpret and
visualise, as the optimal ensemble usually contains only 2-5 representative struc-
tures [65, 73], whereas the MaxEnt method may result in an optimal ensemble
with thousands of structures, whereof many are similar.

2.4.2   General applicability

As argued by Bonomi et al. [68] and Ravera et al. [24], both methods can be used
when the system’s free energy landscape shows a few distinct and well-defined
minima. In that case, the ensemble is represented well by a few structures, one
for each free energy minimum and weighted by its corresponding depth (see
Fig. 1). On the other hand, if the energy landscape representing the ensemble
is flat or high-dimensional, i.e. in case of high-entropy systems, a few structures
provide a poor description of the ensemble, even if they may fit the data. So
in the case of high-entropy systems, the MaxEnt method should be preferred
over MaxPars. A simplistic example of a high entropy system is a regular
die[24, 33, 35]. For an unbiased die, all six faces, which represent the states of
the system, are equally likely. Let us consider the experimental observation that
the average result of throwing the die is 3.5. The application of MaxPars to this
problem would lead to the conclusion that the die is well described by two states
only, e.g states 3 and 4 with weights w3 = w4 = 0.5, or states 2 and 4 with
weights w2 = 0.25 and w4 = 0.75, or any other pair of states consistent with
the observation. This result is ambiguous, as many combinations are equally
optimal, and it is also a poor description of the regular die. MaxEnt, on the
other hand, would lead to a uniform distribution for all outcomes. More relevant
examples of high-entropy systems are multi-domain proteins with flexible linkers
[74], intrinsically disordered proteins [75], and unfolded proteins [76], which are
all described poorly by a few distinct states. Thus, the MaxEnt method is
more versatile, in the sense that it gives reliable results also for high-entropy
systems [24, 68]. The dimensionality of the system also plays an important
role. For reasonably small systems, a description in terms of low-dimensional
free-energy landscapes might be possible and relevant. I.e. a few structures
can adequately represent the system. However, for high-dimensional biological
systems the assumption that a few coordinates, or states, can properly describe
the collective dynamics of the molecule might be ventured. Recent studies have
highlighted how also the dynamics of some fast-folding proteins might be too
complex to be represented in fewer than ∼ 10 dimensions [77]. Therefore, we
suggest that MaxEnt, or related methods, should be considered the method of
choice when no safe assumptions can be made about the free energy landscape
of the ensemble.

2.4.3   Imperfect force fields

The choice of the reweighting method also depends on the quality of the sim-
ulations used to generate the reference distribution w0 . Indeed, the results of
MaxEnt and MaxPrior (with e.g. Gaussian [59–62] and Dirichlet priors [63])
reweighting will strongly depend on the quality of the simulation, because the
optimal distribution is expected not to deviate too much from w0 . On the other
hand, MaxPars reweighting depends less on the quality of the initial distribu-
tion, as it freely picks the simulated structures that best represent the data.
This decoupling from the initial simulation is both the strength and the weak-
ness of the MaxPars method. It implies that, in principle, a realistic reference
distribution is not necessarily preferred over a poor one, as long as some good
representative structures have been sampled (Fig. 2). Consequently, approxi-
mate but efficient simulation methods, e.g. Monte Carlo sampling with implicit
water, can be used in conjunction with the MaxPars method (e.g. Rosetta [78]),
allowing for a fast exploration of the conformational space and better overall
sampling without the need for enhanced sampling methods. Such approximate
simulation methods are evidently less suitable for the MaxEnt and MaxPrior
reweighting and therefore, more costly explicit solvent MD simulations should
be employed. On the other hand, MaxPars does not benefit much from the
qualified prior information of a good force field. We want to stress here that
one of the main advantages of using accurate simulations as a prior is when
the provided experimental dataset is sparse. In that case, the refined ensembles
obtained from MaxEnt/MaxPrior are generally more reliable than MaxPars, as
they are regularised by the simulated model.

2.5     Numerical challenges
Reweighting methods, as we presented them here, are essentially optimisation
problems. As such, they are cursed by the problem of dimensionality [79] or,
in other words, the higher the dimension of the parameter space the more com-
putationally challenging it becomes to find the true minimum of the functional
of interest. Several strategies have been employed to reduce the computational
burden of reweighting.
    In MaxEnt, for example, the principal numerical challenge is to find the set
of weights that minimise Eq. (5). This can become highly nontrivial when N is
large, e.g. for tens of thousands of structures. The computational complexity
can nonetheless be alleviated by optimising the values of the M Lagrange mul-
tipliers (Eq. (6)) rather than the N weights, as usually M  N [23, 29, 32]. We

                                                         Simulation                         Analysis
    Experimental
     information

                                  Experiment-Biased FF                    Sampling                           Probability density

                     Simulation

                                                                                               Reweighting
      Inexact FF                                                                                                  MaxEnt
                                    Poor sampling

                                                         Analysis

                     Simulation                                       Probability density

     Unreliable FF                      Sampling                                                                  MaxPars

Figure 2: Lower two rows: The two cases of poor sampling of an inexact force
field and the one of full sampling of an unreliable force field can both lead to a re-
sult where the distribution of an observable of interest is poorly estimated. The
performance of subsequent MaxEnt/MaxPrior and MaxPars reweighting differ,
as a poor prior inevitably leads to a poor reweighted distribution in the case of
MaxEnt/MaxPrior, while MaxPars can still select some relevant conformations
from the initial unreliable pool. Top row: In both cases, experiment-biased
simulations can help alleviate the problem.

note however that, depending on the implementation, the optimisation of the N
weights can be faster than the one of the Lagrange multipliers [37]. Moreover,
the functional in Eq. 18 is strictly convex for finite θ [80], so the corresponding
optimisation can be carried out in a straightforward fashion by means of highly
efficient routines such as limited memory Broyden-Fletcher-Goldfarb-Shanno
(L-BFGS) algorithm [81].
     In MaxPars, the numerically challenging part is provided by the test of the
N !/(n!(N − n)!) combinations of n-sized ensembles out of N structures. A
naive approach where all the possible combinations are tested is intractable for
realistic situations as, for example, in the case of n = 5 and N = 1000 the
number of combinations becomes C(n, N ) ∼ 1013 . Therefore, the best fitting
combinations of n structures has to be determined with some other strategies,
e.g. via Monte Carlo minimisation [82] or more complex algorithms such as the
one implemented in ASTEROID [83]. Other strategies limit the search to the
subset of structures that best match the experimental data individually [52],
which however violates the principle that the goodness of fit should only be
assessed only against the ensemble average (Eq. (1)), and not against the fit to
single structures.
     As a final remark, we note that both MaxPars and MaxEnt methods can
benefit from clustering, where structures are grouped according to their struc-
tural resemblance, to reduce N before reweighting [29, 60, 61].

3    Experiment-biased simulations
In section 2 we focused on three possible principles, MaxEnt, MaxPars and
MaxPrior, to reweight the results of simulations a posteriori. However, as we
argued in section 1, this is not the only possible approach. Instead of changing
the simulated ensemble after the simulation has been performed, the simulation
can be guided by adding a bias to the underlying force field, Eff (X), employed
in the simulation to ensure consistency with the experimental data. In this
section we provide an overview of the methods that have been applied with
this goal, which are either based on the MaxEnt principle (section 3.1), on the
addition of empirical energy terms (section 3.2), or on the MaxPrior principle
(section 3.3). Finally, in section 3.4 we compare and discuss the differences
between experiment-biased simulations and a posteriori reweighting strategies,
discussing their possible advantages and shortcomings.

3.1    Maximum Entropy
In section 2.1, we discussed how Maximum Entropy can be used to obtain
consistency between data and simulations by optimising a set of Lagrange mul-
tipliers (see Eq. (6) and Ref. [36]). The mathematical formulation of the
principle makes it immediate to extend it to the problem of experiment-biased
simulations. Starting from an unbiased force field Eff (X) (Fig. 1), the idea is
to perturb it as little as possible under the constraint/restraint of consistency
with some given experimental data. Maximum Entropy principle can be ex-
pressed in terms of the probability of a conformation X given the new force
field P (X) ∝ exp(−βE(X)), where β = (kB T )−1 with kB being the Boltzmann
constant and T the temperature of the system, and the probability of the same
configuration obtained from the unbiased force field Pff (X) ∝ exp(−βEff (X))
[34, 41]:
                                   Z                      
                                                    P (X)
                    S[P (X)] = − dXP (X) log                 .               (19)
                                                   Pff (X)

Practical examples of this approach are provided by experiment directed sim-
ulations (EDS) [84] and experiment directed metadynamics (EDM) [85]. The
effective error from experiment and forward model can also be accounted for in
the Lagrangian framework, thus only restraining the solution within the given
uncertainty [40, 41].

3.2    Empirical energy terms
Rather than approaching with MaxEnt, experimental restraints can be directly
included as empirical penalty terms [86]:

                 E(X) = Eff (X) + Eexp (hO calc i, O exp , σ)
                                      M
                                      X
                        = Eff (X) +         θj hj (hOjcalc i, Ojexp , σj ),   (20)
                                      j=1

where the sum is carried out over M restraints. θj are the force constants
associated to each restraint, while the specific choice for the functional form
of each hj depends on the distribution of the corresponding observable. The
constraints are usually expressed as squared residuals [39, 86] or, when errors
are taken into account, as χ2 terms [68] (Eq. (7)).
    For concreteness and simplicity, we assume here normally distributed ex-
perimental observables. We also assume that the same force constant can be
used for all observables. This is a good assumption, e.g. when the observables

come from SAXS data [38], but cannot generally be assumed when more than
one experimental techniques are combined. With this assumption, the energy
function reduces to:

                   E(X) = Eff (X) + θχ2 (hO calc i, O exp , σ).               (21)

Just as in reweighting approaches, parameter θ in Eq. (21) takes into account
unknown uncertainties of the force field parameters as well as unknown or im-
perfectly determined errors in the data and the forward model. Therefore, θ
is generally not known and determining it is one of the key challenges of the
method [23, 37].
    Another issue in the practical implementation of this approach is that the
average hO calc i can only be determined after the simulation is over. Thus the
restraints need to be applied iteratively [35]. As an alternative approach to ob-
tain an ensemble averages at each point in the simulation, replica methods have
been introduced [23, 87–89], where N independent replicas of the same system
are simulated and observables are calculated as ensemble averages from these.
Interestingly, replica experiment-biased methods mathematically converge to a
Maximum Entropy constrained solution as N → ∞ and θ → ∞, as discussed by
Pitera & Chodera [90], Roux & Weare [34] and Cavalli et al. [91], and reviewed
by Boomsma et al. [35]. Very recently, Köfinger et al. [37] combined reweighting
and experiment-biased methods to simultaneously ensure a large ensemble (as
in MaxEnt) is considered and that all relevant states are visited by adding a
biasing energy term to the force field.

3.3    Bayesian inference
Just as in the case of MaxEnt, Bayesian inference, or MaxPrior principle (see
section 2.3), can be also employed to bias a priori molecular simulations rather
than just reweighting them a posteriori. The method known as Metainference
[39] is an implementation of this principle: it employs a Bayesian approach
to quantify how much the prior is modified by the introduction of noisy and
heterogeneous sources of data. In its essence, the strategy works by running
N replicas of the system and guiding the sampling by means of a log-posterior
scoring function:
                              N                                  N
                              X                                 X    1
                s(X, σ) = −         log P (Xi , σi ) + ∆2 (X)            ,    (22)
                              i=1                               i=1
                                                                    2σi2

where σ takes into account all the sources of errors, P (Xi , σi ) is the prior and
the factor ∆2 (X) estimates the deviation between the predicted observables

and the experimental ones. It can be shown that in the single-replica limit,
N = 1, Eq. (22) reduces to Eq. (18). Therefore, the log-prior plays the role of
an effective entropy term, while the second component of s(X, σ) is a χ2 term
computed over the replicas. It is interesting to notice here that the equivalence
between Eq. (22) and Eq. (18) is valid only in the θ = 1 case: this comes
from the fact that the method proposes a model to take into account all the
sources of error [39], which means that θ is not expected to be a free parameter
anymore. We notice that Eq. (22) is only valid for Gaussian error sources, and
more complicated and complete expressions can be obtained in the general case
(see the discussion in section Materials and Methods in Ref. [39] and Ref. [92]).
    Metainference has been effectively combined with Metadynamics [93–95] in
its parallel bias formulation [92, 96]: this synergy enables one to explore the con-
figuration space in an efficient way while simultaneously sampling conformations
that are coherent with experimental data.

3.4     Comparing reweighting with experiment-biased meth-
        ods
3.4.1   Adaptability

Reweighting methods can be used with many different types of simulations and
force fields, as the reweighting process is independent from the simulation and
sampling (Fig. 1). This makes it a rather adaptable module-like tool, with the
input being the trajectory and the experimental data only [32, 36, 44]. Also, new
experimental data can easily be incorporated in the reweighting process without
having to re-run the conformational sampling. In the experiment-biased sim-
ulations, the implementation is more specific, as the empirical energy term is
an integrated part of the simulation [38]. Decisions about types of experiments
and force field constants have therefore to be taken before the simulation. It is
still possible, however, to reweight experiment-biased simulations a posteriori
to remove or add sets of experimental data, though the procedure is techni-
cally somewhat more challenging than reweighting MD trajectories; indeed, the
applied experimental bias has to be estimated and subtracted from the simula-
tion before further reweighting [23, 44]. For the same reason, experiment-biased
simulations are often not carried out together with enhanced sampling tech-
niques. A notable exception is provided by metadynamics [97], which has been
combined with metainference [39, 92] to increase its efficiency, and in principle
metadynamics (and other enhanced sampling methods) could be used in other
methods for experiment-biased simulations.

3.4.2   Forward models

When a trajectory is reweighted a posteriori, the forward model is only evalu-
ated on the frames that are to be reweighted, which are typically only a small
fraction of the frames generated during the simulation. Also, as long as the
observables are calculated according to Eq. (1), the calculations are done inde-
pendently of one another and may thus be easily parallelised. For these reasons,
the forward model can be of high complexity (e.g. quantum calculations can
be carried out on the ensemble structures [98]). This is not the case, however,
of experiment-biased simulations: when implemented within a molecular simu-
lation, forward models are evaluated and differentiated at (almost) every step,
so they have to be sufficiently simple to assure computational efficiency [44]
and their gradients have to be known analytically. Therefore, for complex for-
ward models reweighting might be more applicable than a priori experimental
bias. In some cases, such as for NMR chemical shifts, it is possible to employ a
fast forward model [99] that is almost as accurate as more refined and complex
models [100], which would be too complex to be computed at each step in a
simulation. In other cases, it might not be possible to derive sufficiently compu-
tationally efficient and accurate forward models. We suggest that a possibility
would be to use simpler and less accurate models to bias the simulations and
then reweight a posteriori the simulation with the more realistic models.

3.4.3   Imperfect force fields

Reweighting methods and experiment-biased simulation methods may in prac-
tice perform differently in cases where the force field provides a relatively poor
description of the system’s conformational space. With a poor force field, some
relevant states may be rarely or never visited when running an unbiased simu-
lation (Fig. 2). Consequently, reweighting methods may fail in predicting the
correct average of an observable. An indication that this is happening is usu-
ally provided by the fraction of effective frames φeff becoming close to 0 and by
the reweighted distributions of relevant observables being skewed towards the
experimental average (Fig. 2). In principle, this can be overcome by sufficient
sampling, but it might be computationally very expensive and practically un-
realistic. Experiment-biased force fields, on the other hand, can better provide
reasonable results even when a rather poor unperturbed force field is used as ba-
sis, as the empirical energy term will alter the energy landscape such that even
relevant states with high energies in the unbiased force field become reachable
(Fig. 2). The effect of the added empirical energy term can be monitored by

comparison with a control simulation without the additional energy term (θ = 0
in Eq. (21)).

4     Force field optimisation
In sections 2 and 3 we described techniques to refine simulations in a system-
specific manner by including experimental data. From a different perspective,
substantial progress has been made when using experimental data to improve
the force field as a general and transferable predictive tool. In this section we
focus on this point and review some of the fundamental advancements in the
subject.

4.1    Background on force field parametrisation
As widely discussed in literature and assessed by empirical knowledge, the qual-
ity of the physical description provided by force fields is fundamental for the
accuracy of biophysical simulations. The reliability of these simulations indeed
depends critically on the ability of the underlying physical description to effec-
tively model all the relevant inter-atomic interactions. After decades of force
fields development [101–104], MD simulations have reached a high level of re-
liability and the ever-growing amount of experimental observations calls for a
systematic and detailed comparison of theoretical predictions, coming from MD
simulations, with the available data.
    Unfortunately, force fields do not always provide results that are in per-
fect agreement with experimental findings. To understand the reasons and the
sources of these emerging discrepancies, we shall first recall how a force field is
usually designed. For a comprehensive introduction on the subject we refer the
reader to Chapter 1 of this book, and here we instead focus on how experimental
data may be used in force field parameterization.
    The typical force field is composed by two fundamental elements: (i) A func-
tional form E(X). This element embeds our physical understanding of molecu-
lar processes by providing a classical parametrisation of the Born-Oppenheimer
energy surface [105]. The typical functional form of the force fields used for
biomolecular simulations (with minor re-adjustments among the different inter-

pretations) is given by [106]:

  E(X) = Ebonded (X) + Enon-bonded (X)
         X                   X                              X
       =     kb (r − r0 )2 +     kθ (θ − θ0 )2 +                      kφ [1 + cos(nφ − φ0 )]
             bonds                    angles              dihedrals
                              "                     #
                  X               Aij   Bij   qi qj
         +                         12 − r 6 + r
                                  rij
                                                      ,                                  (23)
                                         ij     ij
             i,j∈non-bonded

where X is a configuration of the system and r, θ and φ are functions of the
atomic coordinates and q are atomic charges. kb , kθ and kφ denote the dif-
ferent strengths of the interactions and are usually tensors, as they depend on
the specific group of atoms involved in the interaction; (ii) A set of parameters
ξ = (r0 , θ0 , φ0 , kb , kθ , kφ , . . .). The functional expression of the force field de-
pends on the choice of these parameters which set, for example, the strength
of interactions, equilibrium distances and angles. To determine their values, it
is necessary to fit them against known experimental and quantum mechanical
(i.e. ab initio) properties. The specific choice of these properties depends on
the philosophy underlying the force field development.
    Historically, force field development has always been a daunting task be-
cause of its technical complexity and the amount of time, experimental data
and simulations required [107–110]. To give an example of this, let us focus
on the AMBER class of force fields. In its first version [104], bonded angles
were fit to the vibrational frequencies of single amino acids or small molecules,
in order to reproduce experimental frequencies; fixed charges were fit to repro-
duce the results of quantum calculations [111–113]. Lennard-Jones parameters,
instead, were set in such a way to reproduces enthalpies of vaporisation and
densities in organic liquids [101]. Finally, dihedral and torsional angles were fit
to reproduce quantum calculations of single amino acids or experimental barrier
heights of small molecules. With the increasing quality of experimental and ab
initio data, modern and widely used versions of the AMBER force fields [114]
have reached a high level of complexity. Nonetheless, the underlying general
philosophy remained the same: fit the force field parameters to ab initio and
experimental data of single amino acids or small molecules and compare the
results against data available for larger systems. Force field ff19SB, obtained
by only employing ab initio simulations, constitutes a notable exception [115].
Despite its historical significance and great success, this procedure shows some
important limitations: (i) It is difficult, within this approach, to improve the
force field parameters by making use of discrepancies with respect to experimen-
tal data on large biomolecules; (ii) errors induced by the forward models used to

calculate experimental observables are not consistently taken into account, and
errors on the force field parameters are not estimated and/or not used. In the
last decade, many new strategies for force field parametrisation have been de-
veloped, that less strictly follow the traditional approaches and instead embrace
a more Bayesian approach [116–124]. These efforts, combined with the growing
interest in automated force field parametrisation (as exemplified by the develop-
ment of the ForceBalance framework [121, 122, 124]), partially solve the issues
reported in point (ii). A deeper discussion on point (ii) will be left for section 6.
In this section we focus on point (i) or, more precisely, describe and summarise
the strategies available in the literature to optimise force field parameters using
discrepancies between MD simulations and experimental observations on longer
peptides or even entire proteins. As we will see, these methods are tightly con-
nected to common reweighting algorithms (see section 2) but, when applied to
a wide set of molecules, provide a an answer of more general purpose than the
sole ensemble refinement.

4.2    Refining Protein and RNA force fields
NMR data have been widely and successfully used in combination with ensemble
reweighting strategies of proteins [30, 32, 48, 57, 58, 61, 62, 64, 83, 125–135];
other approaches employed various sources of experimental data, e.g. for small
molecules. This fact opens to the appealing possibility to use NMR data on
full proteins to directly optimise force fields. Such an approach is more general
than ensemble reweighting, in the sense that experimental NMR data can be
collected for a larger number of proteins and used to increase the quality of the
force field rather than optimising the description of a single system of interest.
To understand how this could be possible in practice, we need first to realise that
the general scheme of ensemble reweighting methods basically comprises of three
steps: (i) Generation of an ensemble of structures with a given force field; (ii)
Calculation of experimental observables from the ensemble; (iii) Determination
of weights, associated to each structure, that better describe the experimental
observables.
    If this procedure is repeated for a large set of proteins, the information
carried by the optimised weights can be in principle used to increase the quality
of the underlying physical model, i.e. the values of the force field fit parameters,
rather than just the single molecule ensemble (Fig. 3). We note, however, that
this approach is less flexible than, e.g., MaxEnt where the weights of all the
simulation frames can be fine tuned. When optimising a force field, one is

inevitably constrained by its functional form and only limited adjustments can
be made.
    In the next sections we review the different strategies that have been de-
veloped to compute and use the weights in force field refinement for proteins
(section 4.2.1) and RNA (section 4.2.2).

4.2.1   Proteins

Let us assume we can access a given set of N snapshots Xi obtained from a
sampling strategy of choice (MD or Monte Carlo) and generated using a given
force field Eff , defined by a set of parameters ξ 0 . These snapshots can be used
to calculate the ensemble average of some observables of interest, hOjcalc i, for
which we possess experimental information Ojexp . The goal is to determine a
set of force field parameters ξ that decreases the discrepancy between experi-
mental and simulated averages. This discrepancy can be estimated via the χ2
(Eq. (7)), whose minimisation with respect to the force field parameters would
maximise the compatibility between simulations and the experiments of choice.
The search for the χ2 minimum can in principle be done in a brute force fashion,
by infinitesimally perturbing the set of force field parameters by a quantity δξi
and re-simulating the system of interest. However, this strategy is particularly
inefficient, as it corresponds to a search in a high-dimensional parameter space,
where the evaluation of each new trial force field requires a full re-sampling of
the system’s conformational ensemble. To avoid this, it is possible to use some
ideas coming from statistical mechanics. In principle, if we knew the exact force
field Eexact describing our system, we could reweight each configuration using
the Boltzmann relationship:

                       wiexact = wi0 e−β(Eexact (Xi )−Eff (Xi )) .           (24)

Eq. (24) is the same idea behind the method of free energy perturbation [136]
devised by Zwanzing to determine the changes in the free energy of a system
when a perturbing potential is introduced. In this case, force field Eff plays
the role of the unperturbed potential of the system, while the exact force field
Eexact is the contribution to the total energy provided by the perturbation.
Even though Eexact can never be known, Eq. (24) can be used as the basis of an
efficient optimisation strategy [116, 137–139]. In this method, a force field Eold
is iteratively optimised to obtain a new one, Enew , that is used to recompute
the weights of the parent MD simulation via:

                       winew = wiold e−β(Enew (Xi )−Eold (Xi )) .            (25)

                                                        Observable

                                                                     Experimental
                                                                      information

                                      Forward
                                       model                                Refinement

        Initial FF                     Sampling                           NewFF
                                                                          i-th FF

                     Simulation                       High
                                                     overlap
                                                     with old
                                                        FF

       Refined FF                                         Weights
                                  Low overlap
                                  with old FF                              Calculation
                                                                         of new weights
                                   Convergence

Figure 3: Schematic representation of the force field optimisation process. First,
an initial force field Eff (X) is employed to sample an ensemble of configurations
of some systems of interest. A forward model is then applied to the computed
frames, to reproduce the known experimental average of a set of relevant ob-
servables. If the computed and the experimental observables disagree, further
experimental information is used to refine the current force field parameters and
defining a new force field Ei (X). A weight is associated to each frame obtained
from the previous sampling using Eq. (25). If the overlap between the old and
the new force field is high (i.e. most of the weights do not change substantially)
the new weights are used to refine the estimation of the observable’s average,
which in turn is used to further refine the force field parameters and to estimate
new weights. If the overlap is instead small, a further round of conformational
sampling is carried out with the new force field Ei (X). The process is repeated
until some convergence criterion is satisfied.

The new weights winew are used to refine the estimation of the simulated average
by means of Eq. (1). Enew force field is obtained by minimising the χ2 , where
the specific strategy for minimisation can change (e.g. Levenberg-Marquardt
procedure [116, 140], simplex minimisation [137] or simulated annealing followed
by simplex minimisation [138]). The strength of the reweighting strategy in Eq.
(25) is that it does not require one to sample new conformations every time
the force field parameters are updated. Nonetheless, it only works under the
assumption that minimal perturbations of the force field are introduced by the
χ2 minimisation and therefore that the snapshots Xi could have been reasonably
sampled also by means of the Enew force field. For this reason, a sensible
overlap between Eold and Enew force fields is expected to exist, and particular
care is dedicated to the assessment of this overlap [138, 141], which can be
quantified, e.g. through φeff (Eq. (10)). A re-sampling of the full conformational
ensemble needs to be repeated every time the overlap between the two force
fields becomes too small: when φeff < ε, with ε  1 being a given threshold,
one can argue that the overlap between force fields is too small to allow a
further round of optimisation. As described, this strategy is based on a method
designed to compute free energy differences between different energy function.
Thus, for future applications other and more general methods could be employed
including Bennett Acceptance Ratio [142] and its multi-state extension [143].
These methods may likely also be fruitfully combined with the use of (adaptive)
surrogate models [120], though work remains to be done to make such models
accurate and efficient for high dimensional problems.
    Norgaard et al. [116] introduced the method discussed above to optimise a
force field for coarse-grained simulations of unfolded proteins. Reference data
were collected from paramagnetic relaxation enhancement NMR, useful to de-
termine long-range effects in unfolded proteins [144–147]. In the first round of
optimisation, all the interaction parameters of the coarse-grained force field were
set to zero for sake of simplicity, while conformational ensembles are generated
using Metropolis Monte Carlo. The method was applied to the ∆131∆ frag-
ment of staphylococcal nuclease [144, 148] to obtain reproducible and consistent
results.
    Li and Brüschweiler [137] applied the strategy from Norgaard et al. [116] to
all atom simulations to derive the Amber ff99SBnmr1 force field starting from
backbone dihedral angle potential of Amber ff99SB [149]. This was done by
employing as observables the time-averaged chemical shifts of Cα , Cβ and C0
carbon atoms of 4 trial proteins and subsequently benchmarking it against a test
set of 18 proteins of different topologies. The obtained results show an average

improvement of the comparison with the experimental data for the proteins in
the test set, and was later refined further [138].
    More recently Chen et al. [139] extended the method from Norgaard et
al. [116] to use Markov State Models (refer to section 5.1 for more details on
Markov State Models) as an intermediate step to calculate observables from sim-
ulations and parameterize the conformational landscape. Despite the different
framework, the general philosophy of the method, named ODEM (Observable-
driven Design of Effective Molecular models), remains unaltered. ODEM has
been applied to design a Cα − Cβ coarse-grained model of protein FIP35 which
is able to reproduce relevant pair-distance distributions measured by FRET.

4.2.2   RNA

Molecular simulations may also be used to study the conformational landscapes
and dynamics of RNA molecules. Unfortunately, the precision of RNA force
fields is still limited and not comparable to the one reached by force fields
designed for proteins [150–153]. The approach of integrative structural biology
therefore becomes a powerful tool to enhance the comprehension of fundamental
processed governing RNA dynamics and indeed the effectiveness of a posteriori
reweighting on RNA simulations has been established by several works [32, 154–
157]. The lack of a common strategy to increase the reliability of RNA force
fields from first principles [158–160], however, makes it particularly appealing
to resort to approaches that exploit discrepancies between MD simulations and
experimental data to refine force fields. Here we review a recent study [134]
that tackles this problem by proposing a likelihood minimisation scheme. Let
us assume the system of interest is described by a force field Eff (X) and a
corresponding Boltzmann probability distribution P0 (X) ∝ e−βEff (X) . For the
same system, M experimental data have also been collected. In this work, the
authors seek for an optimised probability density
                                              PN
                       P (X, µ) ∝ P0 (X)e−β    i=0 µi fi (X)               (26)

where now the force field is expressed by an expansion on a basis fi (X), where
each function is associated to a weight µi . We stress that weights µ have not
to be interpreted as the previously introduced weights w, as the former are
arbitrarily normalised and not interpreted as probability densities. Each of the
N terms helps in reproducing the M experimental constraints, but, differently
from MaxEnt methods, fi (X) do not represent the forward model connecting
configuration X to an experimental measurements. Rather, fi (X) can be generic
functions and N is sought in such a way that N  M . While the analytic form

of the basis functions is enforced at the beginning of the optimisation process,
the value of the weights λi needs to be determined through the minimisation of a
function describing the discrepancy between the simulated and the experimental
observables. We note that in this strategy the functional form of the force field
is actively modified by introducing basis functions fi (X) that are not explicitly
included in Eff (X). Alternatively, this can be seen as a way to associate non-zero
weights to terms in the force field that have an effective null coupling constant.
If functions fi (X) are already part of the potential, instead, the corresponding
weights µi amount for a refinement of the interaction strength. Supposing to
be interested in M observables Ojcalc , the target for the minimisation takes the
form of a regularised error function

            T (µ) = T (hO1calc i(µ), . . . , hOM
                                               calc
                                                    i(µ)) + θ|µ|2   θ≥0       (27)

where the averages hOj i(µ) are computed in the refined ensemble
                                  Z
                    hOj i(µ) =      dX Ojcalc (X)P (X, µ)                     (28)
                                Z
The error function is designed to enforce both equalities and inequalities, i.e.
hOjcalc i(µ) = Ojexp and hOjcalc i(µ) < Ojexp and the optimal set of weights µ is
obtained as the one minimising T . The strength θ of the regularisation term is
key to the strategy: for θ → ∞ the error function does not feel the contribu-
tion of the experimental constraints and thus the potential resulting from the
optimisation is just the original one Eff (X). Instead, for θ → 0 the deviations
from the original potential are not restrained, and the prior information from
the simulations is effectively ignored. Therefore, an optimal value of θ has to
be determined or alternative statistical tools have to be applied to integrate
out the variable. In this work the authors employ cross-validation to determine
the optimal θ, but this is a general issue common to many ensemble optimisa-
tion methods. We refer therefore to section 6 and references therein for further
details on the choice of the optimal prior strength.
    The RNA systems chosen for this application were four tetranucleotides
and two tetraloops, and NOEs (Nuclear Overhouser Effect) as well as scalar
coupling NMR data were used in the force field refinement procedure. The
basis functions were chosen to be sines and cosines acting on torsional angles,
while the employed guess force field was Amber ff99bsc0 + χOL3 with the OPC
water model [104, 161–163].

5    Matching time-dependent and time-resolved
     data
When dealing with systems at equilibrium, the average of an observable hOi is
consistent with many possible distributions of the same observable p(O). As
we discussed in section 2, MaxEnt, MaxPars and MaxPrior principles can help
discriminate, among the several possibilities, which one is the optimal distri-
bution. Suppose, however, we can access a good description of some relevant
conformations of a molecule (by experimental evidences or previous sampling)
and we are now interested in understanding the dynamics of interconversion
between them. From an MD perspective, one can hope to see interconversions
happening by running several trajectories starting from the collected relevant
configurations. If extensive sampling is achieved and enough state transitions
are captured, one can for example use the trajectories to build a Markov State
Model for the system, and obtain the desired information about the inter-state
dynamics [164–166]. However, full sampling of the conformational dynamics
might be challenging to achieve, especially when the desired motions happen in
the µs timescale or above. Moreover, as discussed in detail in section 4, limi-
tations in the force field employed in the simulations might lead to conclusions
which disagree with key experimental data, even in the case of excellent sam-
pling. This may be the case, for example, for NMR spin relaxation experiments:
spin relaxation rates are sensitive to both short- and long-range dynamics of a
protein, occurring from the picosecond to the nanosecond timescale [167]. For
dynamical observables like NMR spin relaxation rates, methods developed to
increase the consistency between computed and experimental values of static
observables might be of only limited help and different strategies are needed.
In this section we describe some recent efforts in this direction and how it is
possible to use simulations to match experimental knowledge on time-dependent
observables (i.e. observables that depend on time because of fast processes hap-
pening in the system and cannot therefore be expressed by means of Eq. (1), e.g.
NOEs with spin diffusion [135]) and time-resolved ones (i.e. observables that are
at equilibrium locally in time, but have been monitored for long timescales and
can therefore be expressed as in Eq. (1) by including a time label, e.g. time-
resolved SAXS). The following sections will focus on applications concerning
Maximum Entropy and Likelihood estimation applied to Markov State Models
[168, 169] (section 5.1), the principle of Maximum Caliber [170] (section 5.2)
and average block selection [171] (section 5.3) (Fig. 4).

(a)                                         Augmented Markov Models

         2                                                                2

  pik0       w0     1
                                                   Experimental    pik        w    1
                                                    information
         0                                                                0

(b)                                                      (c)
                  Maximum Caliber Principle                            Average Block Selection

                                                                  w0          w1       w2        w3
                             Experimental
                              information

Figure 4: Graphical summary of methods implemented to recover time-
dependent and time-resolved data. (a) Augmented Markov Models employ ex-
perimental information to refine a guess Markov State Model and consequently
better estimate kinetic observables of interests; (b) Maximum Caliber, in its
experiment-biased formulation, is employed to bias the sampling to match some
time-resolved experimental quantities; (c) Average block selection is used to
assign weights to sub-trajectories and better estimate time-dependent experi-
mental data.

5.1    Maximum Entropy and Likelihood in dynamical sys-
       tems
In a kinetic model, the equilibrium distribution w can be determined from a
transition probability matrix T (τ ), i.e. a matrix whose elements pik provide
the probabilities for the system to be found in state k at time t + τ , given it
was in the state i at time t. T (τ ), together with the structures of the states
among which transitions happen, is usually known as a Markov State Model
(MSM) [165, 168]. In this section, we will discuss a method to refine a MSM by
adding static (not time-dependent or time-resolved) experimental information.
This framework, that balances data coming from simulations and experimental
averages, is called Augmented Markov Model (AMM) [172].
     The construction of an AMM starts from the definition of an initial MSM,
T 0 (τ ), with transition probabilities p0ik . The MSM is typically built by following
a multi-step procedure [165, 168]: (i) relevant features (e.g. dihedral angles,
contact maps etc.) of the system are selected. The dynamics of these features
needs to play a key role in the conformational transitions under consideration,
so their identification might not be trivial. This task can become easier with
the help of automatic selection tools [173, 174]; (ii) the features are used to
generate a lower-dimensional representation of the system dynamics [175, 176];
(iii) the lower dimensionality [177] allows one to cluster similar configurations
in the dimensionally reduced space. The N clusters will define the states of the
model; (iv) finally, statistical tools [168] are employed to estimate the transition
matrix T 0 (τ ). Among other possibilities, the transition probability matrix can
be obtained by maximisation of the likelihood [165, 168]:
                                              Y
                                 L(T 0 ) ∝      (p0ik )cik ,                      (29)
                                           i,k

where cik is the number of transitions occurring between state i and k, which are
obtained by explicitly counting the transitions between states in the simulation
[178, 179]. The resulting transition matrix has to satisfy further criteria, e.g.
it has to be row- or column-stochastic, and detailed balance can be enforced
explicitly. Maximisation of Eq. (29) is equivalent to minimising the negative
log-likelihood:
                                           N
                                           X
                             S(T 0 ) = −         cik log p0ik ,                  (30)
                                           i,k

We note that while Eq. 30 resembles an entropy term, but it cannot represent a
proper one, as the counts cik enter Eq. 29 un-normalised. However, S(T 0 ) can

be used in a similar way as a regularising prior when including experimental in-
formation, as we describe further below. The equilibrium distribution of the sys-
tem, usually referred to as the stationary probability distribution of the MSM, is
obtained from the transition probability matrix by solving the eigenvalue equa-
tion T 0 (τ )w0 = w0 . For more information about Markov State Models, we
refer the reader to some excellent reviews on the subject [164–166, 168, 180].
    Given the initial Markov State Model T 0 (τ ), the framework of Augmented
Markov Models employs the MaxEnt principle and likelihood maximisation to
build an optimised MSM, T (τ ). Let us assume we can access both the expec-
tation values of M experimental observables and an MSM built on simulation
data, with the reference stationary distribution w0 . To obtain the optimal dis-
tribution w, one can apply MaxEnt principle, as reported in Eq. (6), which
bridges the model distribution with the experimental one by means of the pro-
vided experimental averages. Rather than estimating the weights corresponding
to the optimised distribution w, the MaxEnt formulation allows one to optimise
the set of Lagrange multipliers λ (Eq. (6)). As usual, the Lagrange multipliers
are obtained by enforcing constraints on the experimental averages. In order
to account for the statistical errors in both sampling and experiments, one can
introduce the so-called Augmented Markov Model likelihood, assuming Gaussian
errors:                                       
                                                     1 2
                                     Y
                       L(w, T ) ∝  (pik )cik  e− 2 χ (w) .                 (31)
                                    i,k

The term in the parentheses is the MSM likelihood, Eq. (29), while the second
term incorporates the Gaussian error model proposed for the observables. The
corresponding negative log-likelihood is thus proportional to:

                        TAMM (w, T ) = χ2 (w) − θS(T ),                      (32)

where S(T ) is the entropy-like term introduced in Eq. (30). Note that w
is uniquely determined by T by solving the eigenvalue equation T (τ )w = w,
so Eq. (32) is effectively a minimisation problem for the matrix elements pik
alone. We stress that we have introduced Eq. (32) only to show the similarity
with the reweighting methods for equilibrium ensembles, Eq. (9) and (13), and
that it does not directly represent the way AMMs are practically implemented.
Rather, one obtains an AMM that optimally balances between the information
from simulation and the experimental data (Fig. 4a) by employing fixed-point
iteration algorithm to maximise Eq. 31 with respect to the unknowns pik and the
weights w (see the supplementary information of Ref. [172] for further details).
Olsson et al. [172] applied this method to two 1 ms simulations of ubiquitin.

They built AMMs using NMR scalar and residual dipolar couplings, i.e. static
data, and their results were compared against NMR relaxation dispersion data.
The results of such experiments can either be calculated directly from a long
molecular dynamics simulation [18, 181] or indirectly from a MSM [182]. The
authors found that the AMM that had been optimized against the experimental
data was in overall better agreement this indpendent data compared to the raw
MSM. This is a strong indication of a non-trivial fact: reweighting an MSM with
respect to experimental equilibrium observables helps increase the reliability in
the prediction of time-dependent data.

5.2    Maximum Caliber
The principle of Maximum Caliber (MaxCal) can be regarded as a generalisation
of MaxEnt, and enables one to compute the probabilities associated to dynam-
ical pathways, rather than probabilities (weights) associated with equilibrium
states. To infer pathway probabilities, MaxCal principle maximises a path en-
tropy [183] defined over all the possible pathways, constrained to reproduce a
given dynamical observable. The path entropy is defined as:
                                      X
                        S[p0 (γ)] = −     p0 (γ) log p0 (γ),               (33)
                                         γ

where p0 (γ) is the probability that the system follows the structural path γ.
Each path is considered as a collection of configurations, γ = {X0γ , . . . , XTγ },
labelled by a discrete time index t = 0, . . . , T . Maximisation of Eq. (33),
together with M constraints of the form:

                           g j [p0 (γ)] = 0 j = 1, . . . , M                   (34)

yields the optimal distribution p(γ) over pathways. Just like in the MaxEnt
case, constraints are usually enforced by Lagrange multipliers, and typically
they concern the calculated dynamical observables Ocalc (Xtγ ) and corresponding
experimental values at the same time point t, Otexp :
                         X
                            p0 (γ)Ocalc (Xtγ ) − Otexp = 0                  (35)
                           γ

The normalisation of the probability distribution of pathways is also enforced:
                              X
                                  p0 (γ) − 1 = 0.                          (36)
                                  γ

If it is possible to introduce an estimate for the time-dependent error σt , then
the notion of χ2 can be extended to a time-dependent form as well, χ2 = χ2t .

In this way, by analogy with MaxEnt, MaxCal principle can also be expressed
in a regularised fashion as

                      TMaxCal [p0 (γ)] = χ2t [p0 (γ)] − θt S[p0 (γ)]            (37)

where the parameter θ of Eq. (9) acquires a dependence on time. All the
terms in Eq. (37) are functionals of the probability density in the space of
pathways: as such, the minimisation of TMaxCal [p0 (γ)] would require a search
in path space, which is knowingly a hard task [184–187]. To our knowledge,
indeed, MaxCal principle has never been used in the acceptation of Eq. (37).
Instead, the principle of Maximum Caliber can be employed to run restrained
MD simulations, where restraints are provided by time-resolved experimental
data (Fig. 4b).
    Note, when comparing simulations with time-resolved experiments, a single
simulation cannot be used to generate an ensemble as in the MaxEnt method
(section 2), due to the non-equilibrium conditions. Therefore, replicas are
needed to describe ensemble development over time (see also section 3). Capelli
et al. [188] introduced such replica-averaging implementation of MaxCal, so
ensembles can be determined at each time t. In this formulation, Eq. (35) and
(36) are employed to constrain the minimisation of the path entropy, together
with the path probability density normalisation and two more equations. The
first one constrains the system’s diffusion constant D:
                         1 X          γ
                              p0 (γ)[Xt+1 − Xtγ ]2 − D = 0,                     (38)
                        2∆t γ

while the other constrains the standard deviation σt of the observable of interest
at time t, obtained by averaging it over all the N replicas
     X                         i
                                           2       X
           p0 (γ i ) hOcalc (Xtγ )i − Otexp − σt2 =   p0 (γ i )ξt2 − σt2 = 0,   (39)
      γi                                               γi
        P
where γ i is used to specify that the sum is carried out over all the possible
pathways of all replicas and the average h·i is computed over replicas. The ex-
pression of the path entropy, together with all the constraints (in this particular
case, Eq. (35), (36), (38) and (39)) imposed via Lagrange multipliers is called
caliber. The result of caliber maximisation provides the optimal distribution of
pathways:
                                                                          
                 1          X  γ               2
                                (νti Xt+1 − Xtγ + λit O(Xti,γ ) + µit ξt2 ) ,
                                               
         p(γ) = exp −                                                         (40)
                 Z          t,i

where Z is a normalisation factor, νti , λit and µit are replica- and time-dependent
Lagrange multipliers. Despite the complicated expression of the optimal path
probability distribution, it is possible to prove that, in the assumption where
the system’s dynamics is Brownian and by analogy with MaxEnt [188–190], the
MaxCal distribution in Eq. (40) can be sampled by adding a time-dependent,
harmonic bias potential to the underlying force field:
                                                                  2
                    Eexp (γ i , t) = N k hOcalc (Xtγ )i − Otexp        ,       (41)

where the constant k is used to tune the strength of the interaction. This ap-
proach was applied to the case of the second hairpin of protein G B1 domain
by employing synthetically generated time-resolved SAXS data [188].

    Rather than using MaxCal principle as an experiment-biasing technique,
it is also possible to employ it for reweighting, in particular for the case of
MSMs [191–193]. Suppose we built a MSM from a set of trajectories and we
want to predict how a given non-equilibrium observable Oik changes in the
transition between state i and state k. A possible example would be the change
in a spectroscopic signal (e.g. Förster resonance energy transfer or circular
dichroism) when passing from a partially unfolded state i to a helical state k of
a protein. The average, computed over many transitions, is provided by:
                                        X
                          hOcalc i(w) =    wi0 pik Oik
                                                    calc
                                                         ,                   (42)
                                             i,k

where w0 is the stationary probability distribution of the MSM. Let us suppose
we also possess experimental information of such observable, Oexp and that the
computed average does not match the expected result. In this case, we can use
the MaxCal principle to select among the models with the correct average [192].
To do so, first the entropy is built as:
                                                          
                                      X               pik
                        S(T, w) = −      wi pik log          ,             (43)
                                                      p0ik
                                       i,k

where w is the optimal stationary distribution and pik are the refined transition
probabilities. Note that Eq. (43) is a version of Eq. (33) in the case of discrete
pathways. The entropy has to be maximised together with the constraint that
the function
                          g(w) = hOcalc i(w) − Oexp                           (44)
is zero, where hOcalc i(w) is the average over transitions introduced in Eq. (42).
Moreover, wi and pik are interdependent because of probability conservation,

so three more constraints naturally emerge:
         X                    X                          X
             wi pik − wk = 0       wi pik − wi = 0             wi pik − 1 = 0.    (45)
           i                       k                     i,k

The minimisation of the entropy in Eq. (43), with the constraints in Eq. (44)
and (45), can be carried out with the method of Lagrange multipliers. It yields:

                          pik = ηφk φ−1         0     calc
                                     i Mik (λ, pik , Oik )                        (46)

where Mik (λ, p0ik , Oik
                      calc
                           ) is a non-Hermitian matrix, φ is its only right-eigenvector
having only positive elements (whose existence and uniqueness is guaranteed by
the Perron-Frobenius theorem), η the corresponding eigenvalue and λ is the La-
grange multiplier controlling the constraint in Eq. (44). The positivity of the
elements of vector φ is necessary to guarantee the positivity of the transition
probabilities. Eq. (46) provides a new set of transition probabilities defining
an optimal transition probability matrix T (τ ). Effectively, similarly to what
happened in the case of AMMs, the introduction of experimental information
actively modifies the transition probabilities between states, and interconver-
sions can become more or less favourable depending on the cases. Finally, the
optimal stationary distribution is obtained as:

                                       wi = ψi φi ,                               (47)

where ψ is the left-eigenvector of matrix Mik (λ, p0ik , Oikcalc
                                                                 ) corresponding to the
                                     0    calc
eigenvalue η. Matrix Mik (λ, pik , Oik ) only depends on the Lagrange multi-
plier λ, which is used as a parameter, and on quantities that can be readily
computed from the initial MSM, i.e. the transition probabilities and the ob-
servables of interest. Therefore, the optimal transition probabilities and equi-
librium probability distribution can be obtained by single value decomposition
of Mik (λ, p0ik , Oik
                   calc
                        ) for different values of λ: the optimal Lagrange multiplier
will be the one for which the constraint in Eq. (44), estimated a posteriori from
the updated MSM, holds true.
    In the original work, the method was tested on a toy model for a growth
factor activation pathway, showing how the incorporation of experimental infor-
mation can help correcting the transition probabilities in a guess MSM. Despite
the method, as illustrated here, does not incorporate experimental errors, it is
possible to take them into account in a Bayesian fashion [192].

5.3    Average Block Selection
Time-dependent data can also be applied directly in the ensemble refinement by
means of time-dependent average block selection. Suppose we have N MD tra-

jectories, started from different conformations, and a set of M time-dependent
experimental observables Ojexp . As anticipated at the beginning of this section,
by time-dependent we here mean observables that cannot be calculated using
Eq. (1) because the values depend on the underlying dynamics as well as on the
stationary distribution. To increase the accuracy of the MD predictions, given
the experimental data, and preserve information about dynamical processes,
Salvi et al. [171] proposed to divide each trajectory into B blocks representing
subsequent time-windows. The total number of blocks is then N × B, each one
associated to a weight wb . The block-weights are then optimised by minimising
the residual sum:
                                 M           N ·B
                                                           !2
                                X       exp
                                             X
                        2                             calc
                      R (w) =         Oj −        wb Obj                     (48)
                                j=1           b=1

         calc
where Obj     is the j-th observable computed from the b-th block. In later studies,
the authors included errors in the expression by the usual χ2 (w) expression [194].
Division in blocks allows to determine how much each block contributes to the
time-dependent experimental signal. For example, blocks with null weights are
excluded and can be interpreted as non-physical artefacts. Despite the similarity
with other approaches used for equilibrium observables, this method shows two
important differences: on the one hand, weights are not associated to a single
structure of an ensemble, but rather to sub-trajectories (Fig. 4c). It is evident,
then, that the method can be effective only in the case where the experimental
timescales of interest can be sampled within a single trajectory. On the other
hand the method as it stands is unregularised, i.e. it assumes that the optimal
solution is obtained by minimising the sum of residuals without adding any
restraint. This is a crucial difference with respect to MaxEnt, MaxPars and
MaxPrior strategies: one would expect nonetheless the method to benefit from
regularisation terms. The addition of such terms would be advisable in further
applications, but it is not clear what kind of prior would be needed in this
case. Because of the fact that Eq. (48) associates weights to pathways and not
conformations, it might be possible to explore a connection with a posteriori
reweighting using MaxCal principle.
    In its original formulation, the method (called ABSURD — Average Block
Selection Using Relaxation Data) [171] was designed to deal in particular with
NMR spin relaxation rates, but its application can be extended to any experi-
mental source sharing similar timescales in a straightforward way. ABSURD was
applied to the C-terminal domain of the nucleoprotein of Sandai virus. A cumu-
lative time of approximately 6.5 µs of MD was sampled, employing two different

water models. While the reproduction of spin relaxation rates by MD simula-
tions alone was imperfect, the ABSURD-optimised trajectories were found in
much better agreement with relaxation data on a wide spectrum of timescales,
even in the simplest case where a single experimental rate was employed in the
optimisation.

6     Challenges
In sections 2–5 we focused on major efforts that have been done to merge in-
formation coming from experiments and simulations to refine conformational
ensembles or improve existing force fields. Despite many important steps for-
ward in the last decade, some major challenges remain. In this section we will
point out some of these and try to draw a possible paths for solutions. In section
6.1 we will focus on the problem of setting the parameter θ in a robust way. In
section 6.2 we will discuss the option of combining force field corrections and
reweighting for a given system. In section 6.3 we discuss possibilities and obsta-
cles to employ kinetic data to reweight equilibrium ensembles. Finally, section
6.4 is dedicated to a discussion on the next generation of force fields.

6.1    Balance between simulations and experimental data
In the MaxEnt and MaxPars reweighting methods, and equivalent methods bias-
ing on the fly, the prior knowledge coming from simulations is balanced against
experimental data by tuning the parameter θ (Eqs. (9), (13) and (21)). In prin-
ciple, the balance could be exactly known if the effective uncertainties on the
weights, force field, sampling, and on the both the calculated and experimental
observables were known (as also discussed in section 3.3). However, the uncer-
tainties on the weights are usually unknown and the experimental uncertainty
stems from different sources, only some of which are typically known or easy to
estimate. We can subdivide the sources to the experimental uncertainty in the
following categories: (i) Statistical errors on experimental data; (ii) statistical
errors in the calculation of average observables from a limited amount of struc-
tures (Eq. (1)); (iii) systematic errors on experimental data; (iv) inaccuracy
of the forward model. For normally distributed errors, these add up to a total
variance [23]. In the following we will shortly discuss each of them.
    The statistical error on experimental data is usually estimated by repetitive
measurements and counting statistics, and it is included in most approaches,
e.g. as standard deviation in the χ2 . Over- or underestimated errors may be

detected by visual good fits having χ2r much lower or higher than unity.
    The statistical error on the mean of the observables calculated from the en-
semble can easily be taken into account [68]. This is important when the ensem-
ble is small, which is typically the case for MaxPars methods and experiment-
biased approaches with replicas.
    Systematic errors in experimental data are generally difficult to take into
account, as their magnitude and nature are usually unknown and may be sys-
tem specific (e.g. incorrect buffer subtraction in SAXS [38]). Shevchuk and
Hub [195] treated the systematic errors with Bayesian statistics as a nuisance
parameter, i.e. an unknown (and uninteresting) parameter that should be de-
termined together with the model parameters. Bonomi et al. [39] discussed
the more general case of outliers, and showed that an approach that combines
reweighting and experiment-biased force fields is more robust against outliers
than other related methods. Similar methods are also discussed by Köfinger et
al. [37].
    Inaccuracies in the forward model are likewise highly non-trivial to estimate.
While negligible in some cases, they are the dominant error source in others,
e.g. NMR chemical shifts, where they can be orders of magnitude greater than
the statistical error. SAXS forward models share similar problems [16]. The
source of the model inaccuracy might also come from neglecting an intrinsic
time-dependency of the observable (e.g. spin diffusion or dynamic effects in the
estimation of NOEs [135]).
    In summary, as long as errors in the force field, systematic errors in the
experimental data, and errors on the forward model continue to be challenging,
if not impossible, to estimate accurately, the parameter θ remains necessary as
an effective scaling of the total error σ. A key challenge is therefore to determine
it. A simple way is to tune θ until χ2r reaches unity (Eq. (8)). This is, however,
not generally a valid approach [196]. First, the number of degrees of freedom
ν is ill-defined when reweighting is concerned. Conventionally, ν is estimated
as M − k, where M is the number of data points and k is the number of fitted
parameters. In MaxEnt, for example, k is given by the number of Lagrange
multipliers, k = M , therefore ν is effectively zero and χ2r has consequently no
meaning. Second, although the expectation value of χ2r is one, point estimates
are typically different from unity and χ2r -distributed. Therefore, this method
may provide incorrect balance between data and simulation. Another strategy
to determine θ is to plot S(w) against χ2 (w) and look for an elbow in the curve
[32, 37]. Indeed, if plotted with double-logarithmic axis, χ2 (S) often becomes an
L-shaped curve, and the optimal θ can be estimated by finding the kink of the

curve [197]. A third strategy is cross-validation, i.e. fitting the optimal ensemble
to a separate set of data that has not been used in the analysis [64, 86, 134,
198, 199]. The reweighting or experiment-biased simulation may then be done
for several values of θ to monitor when the goodness of fit to the unused data
starts to decrease. While intuitively appealing, the practical implementation
may be difficult. First, the data needs to be divided into independent subsets,
which may sometimes be difficult for highly correlated or interdependent data.
Second, as different sources of data may report on very different aspects of the
system, they may in practice not be useful for cross validation [199]. A fourth
strategy for determining θ is strictly Bayesian, and θ is in that context treated
as a nuisance parameter. The posterior probabilities at each value of θ are
calculated and used to find the most probable value of θ [72], or to integrate
out θ completely [23].

6.2    Interplay between reweighting and force field correc-
       tions
In section 3.4 we mentioned that reweighting might fail in reproducing the
experimental averages when the prior (force field) used is too inaccurate, because
relevant states are either poorly sampled or not sampled at all. A pragmatic,
and potentially transferable, solution to this problem would be to identify the
parameters in the force field responsible for the incorrect behaviour and modify
them slightly in order to move closer to the expected averages. Such rescaling
approaches have proved succesful for specific systems and force fields, e.g. for
adjusting the protein-protein interaction strength in the coarse-grained Martini
force field [200, 201] or protein-water interactions for simulations of disordered
proteins [202]. A subsequent reweighting of the obtained trajectories might
correct for inconsistencies that are not related to the identified and re-scaled
parameter, and could therefore lead to better consistency with the experimental
data.
    Applying such approaches, however, raises some relevant questions. For
example, to what extent should one correct the force field? Considerable modi-
fications to a force field would typically require the need to iteratively re-sample
the system under consideration, an exercise that might become computation-
ally expensive. Moreover, after any substantial reparametrisation the force field
should be benchmarked against other data and ab initio calculations, as done
in the original parametrisation of the force field. Therefore, should one perhaps
modify the force field just enough to allow for reweighting? And, more gener-

ally, should force field corrections and reweighting be employed together at all?
Standard force field reparameterization effectively corresponds to reweighting
a conformational ensemble, but the extent is limited by the functional form
of the energy function, and the simultaneous consideration of data on other
systems. A concurrent application of reweighting and force field optimization
could violate the Bayesian principle of having well-defined prior and likelihood
in the reweighting process, as the re-scaled prior used for reweigting has already
been adjusted against experimental data. The data is, so to say, used twice
in such protocol. We do not have an answer to the aforementioned questions,
nonetheless we believe they provide important points of discussion for future
applications of reweighting, and that Bayesian methods for force field parame-
terization would make it easier to merge these two different strategies.

6.3    Using kinetic data to reweight equilibrium ensembles
As discussed in section 5.1, Augmented Markov Models are a framework based
on Maximum Entropy and Maximum Likelihood to include experimental infor-
mation in a Markov State Model. Olsson et al. [172] used AMMs to predict
NMR relaxation dispersion data, by employing only static experimental data to
reweight the model. This fact leads to intriguing questions which, to our knowl-
edge, have been largely unanswered in literature. As a matter of principle,
it should be possible to directly employ kinetic data for ensemble reweight-
ing, just like it is done with the ABSURD method [171]. What would happen
then to equilibrium observables? Would the amount of provided information be
enough to increase the accuracy of simulated averages with respect to experi-
mental equilibrium quantities? What would be the optimal framework to test
this hypothesis? While the first question has no clear answer yet, concerning
the latter we believe that a suitable framework would be the one of Markov
State Models, because of their intrinsic ability to encode kinetic information
[172, 191]. We note however that MSMs, by construction, ignore the fastest
dynamical timescales of the system, which can however be important for some
types of experimental measurements. Therefore, a careful choice of kinetic data
is recommended.

6.4    A new generation of force fields
Force field parametrisation has been historically guided by a combination of
chemical and biological intuition, ab initio quantum calculation of small molecules
and trial and error approaches [108]. This approach has been proven to be ex-

tremely successful [203] but, as the ever growing amount of experimental in-
formation calls for force fields which are easily improvable once new data are
collected, the complexity and the amount of expertise required in this procedure
have made it somewhat impractical. We discussed some advancements in sec-
tion 4.2, but none of the applications we reviewed provided an ultimate solution.
Indeed, suggested improvements are usually small adjustments (e.g. modifica-
tions in the backbone dihedral angles terms [137, 138]), though in some cases
more extensive changes have been introduced using such fitting to experiments
[13, 121, 122, 124]. Therefore, in this section we want to discuss some principles
on which a new generation of force fields could be build.
    One of the main challenges in force field development lies in how to in-
clude new data, which is potentially conflicting with old information, and use
it to improve the force field after it has already been parametrised. Auto-
matic reparametrisation would make it extremely easy to modify and update
force field once such new experimental data become available. The develop-
ment of a Bayesian formalism [116] and later the more systematic ForceBalance
[121, 122, 124] framework, for example, goes exactly in this direction and shows
that it is possible in principle to approach to the problem in an automated
fashion. It would be also important to assign some level of trust to force field
parameters, such that it can be assessed to what degree new data should al-
ter their values. At the same time, a fully Bayesian approach would involve
distribution of force fields, rather than point estimates, and thus parallel simu-
lations could be used to integrate out force field uncertainty. We also stress that
such developments would ideally be carried concurrently with the construction
of worldwide accessible and curated databases of experimental and simulation
data. In order to include new data in a more automatic fashion, there have to be
data quality checks and consensus on experimental and forward model errors,
as this all affects how much the new data should be able to alter the existing
parametrisation (in case of inconsistency). At the same time, it is also impor-
tant to keep in mind that such models should ideally capture well-understood
physical effects, and that lack of agreement with experiments might indicate
important effects that are missing from the functional form or parameter com-
bining rules [110].
    The molecular mechanics force fields were developed as a classical parametri-
sation of the Born-Oppenheimer energy surface that balances computational
speed and precision and the choices of functional forms of the force field terms
has always been guided by chemical intuition. This has led to families of force
fields with differences in the parametrisation [106] and to the proliferation of

big sets of parameters needed to accommodate empirical choices (see, for ex-
ample, the discussion on atom types in Refs. [204, 205]). We expect the next
generation of force fields to be more flexible with respect to specific choices of
parametrisation: more specifically, tools are required to define not only the force
field parameters, but also the functional shapes of each term in a data-driven
fashion. These developments go hand in hand with a robust estimation of both
statistical and systematic errors: the two sources of errors need to be fully de-
coupled and it should be clear when poor estimates are due to poor training
datasets.
    Some of these advancements have already been applied to the SMIRNOFF99Frosst
force field and the Open Force Field Toolkit [204], developed by the Open Force
Field Initiative [206]. For now, SMIRNOFF99Frosst has been tested only on a
wide set of pharmaceutically relevant small molecules, but it represents nonethe-
less an important step towards a new generation of force fields.

7    Conclusions
Much research in the field of structural biology and molecular biophysics re-
quires one to integrate several heterogeneous sources of data, coming both from
diverse experimental techniques and simulations. Experiments are employed to
characterise thermodynamic and kinetic quantities of the system under study
and simulations aid the interpretation of or complement these results thanks to
their high spatial and time resolutions. However, technological [17–20] and theo-
retical [3, 21] advancements in the field of molecular mechanics have highlighted
the existence of discrepancies between simulations and experiments [11–16]. In
this review, we have approached this issue through a specific perspective: in-
consistencies between computational and experimental results carry information
that can be systematically extracted and exploited to improve our understand-
ing of biochemical entities and more general biophysical models. To pursue this
perspective, we focused on the cornerstone ideas that have guided the optimi-
sation of system-specific conformational ensembles (sections 2 and 3) or general
purpose force fields (section 4) against experimental information. We provided
a summary of alternative strategies and discussed their strengths and short-
comings depending on the level of trust one places in the force field used to
carry out the simulations. For each method, we critically assessed how much
a realistic scenario deviates from the ideal version of the approach, examining
the challenges that arise when the systems grow in size and complexity. We
stressed that many sources of data can be employed and different strategies are

needed depending on whether observables can or cannot be represented as a
linear combination of a given forward model applied to the single structures in
the ensemble (see Eq. (1) and section 5). Despite the differences in the techni-
cal implementation, however, we argued that most of the approaches presented
here share a common framework, rooted in the minimisation of the functional

                                  T = χ2 − θR,                                (49)

where χ2 is the negative log-likelihood in the case of normally distributed errors,
θ is a hyperparameter that balances between simulations and experimental data
and R is a regularisation term. Depending on the method, R assumes different
functional shapes: in MaxEnt, it becomes a cross-entropy term, Eq. (9); in
MaxPars, it reduces a parsimony term, i.e. the negative number of conforma-
tions with non-zero associated weight, Eq. (13); in MaxPrior, the regularisation
term is provided by the log-prior, Eq. (18); in AMMs R represents the logarithm
of the MSM likelihood, Eq. (32); in MaxCal the regularisation term takes the
form of a path-entropy, Eq. (37); finally, average block selection is unregularised
and so R = 0, Eq. (48). Therefore, the different philosophies that distinguish
among the several approaches are encoded in the choice of the regularisation
term.
    As a final remark, we devoted section 6 to the challenges that the community
is facing and we anticipate some open questions that we believe will capture
experts’ attention in the incoming years.

Acknowledgements
We acknowledge support by a grant from the Lundbeck Foundation to the
BRAINSTRUC structural biology initiative, the NordForsk Nordic Neutron Sci-
ence Programme, the Carlsberg Foundation, a grant from the Velux Founda-
tions and a Hallas-Møller Stipend from the Novo Nordisk Foundation. We would
like to thank members of the Linderstrøm-Lang Centre for Protein Science for
numerous discussions on these topics, and thank Giovanni Bussi, Ramon Cre-
huet, Clemens Kauffmann and Simon Olsson for insightful comments on the
manuscript.

References
  [1] P. E. M. Lopes, O. Guvench, and A. D. MacKerell, Current Status of
      Protein Force Fields for Molecular Dynamics Simulations, pp. 47–71. New

    York, NY: Springer New York, 2015.

 [2] S. Bottaro and K. Lindorff-Larsen, “Biophysical experiments and
     biomolecular simulations: A perfect match?,” Science, vol. 361, no. 6400,
     pp. 355–360, 2018.

 [3] T. Maximova, R. Moffatt, B. Ma, R. Nussinov, and A. Shehu, “Principles
     and overview of sampling methods for modeling macromolecular structure
     and dynamics,” PLoS Computational Biology, vol. 12, no. 4, p. e1004619,
     2016.

 [4] S. A. Adcock and J. A. McCammon, “Molecular dynamics: survey
     of methods for simulating the activity of proteins,” Chemical Reviews,
     vol. 106, no. 5, pp. 1589–1615, 2006.

 [5] J. L. Klepeis, K. Lindorff-Larsen, R. O. Dror, and D. E. Shaw, “Long-
     timescale molecular dynamics simulations of protein structure and func-
     tion,” Current Opinion in Structural Biology, vol. 19, no. 2, pp. 120–127,
     2009.

 [6] C. Abrams and G. Bussi, “Enhanced sampling in molecular dynamics us-
     ing metadynamics, replica-exchange, and temperature-acceleration,” En-
     tropy, vol. 16, no. 1, pp. 163–199, 2013.

 [7] R. Elber, “Perspective: Computer simulations of long time dynamics,”
     The Journal of Chemical Physics, vol. 144, no. 6, p. 060901, 2016.

 [8] S. A. Hollingsworth and R. O. Dror, “Molecular dynamics simulation for
     all,” Neuron, vol. 99, no. 6, pp. 1129–1143, 2018.

 [9] C. Maffeo, S. Bhattacharya, J. Yoo, D. Wells, and A. Aksimentiev, “Mod-
     eling and simulation of ion channels,” Chemical Reviews, vol. 112, no. 12,
     pp. 6250–6284, 2012.

[10] W. F. van Gunsteren, X. Daura, N. Hansen, A. E. Mark, C. Oosten-
     brink, S. Riniker, and L. J. Smith, “Validation of molecular simulation:
     an overview of issues,” Angewandte Chemie International Edition, vol. 57,
     no. 4, pp. 884–902, 2018.

[11] S. Rauscher, V. Gapsys, M. J. Gajda, M. Zweckstetter, B. L. de Groot, and
     H. Grubmüller, “Structural ensembles of intrinsically disordered proteins
     depend strongly on force field: a comparison to experiment,” Journal of
     Chemical Theory and Computation, vol. 11, no. 11, pp. 5513–5524, 2015.

[12] J. Henriques, C. Cragnell, and M. Skepö, “Molecular dynamics simulations
     of intrinsically disordered proteins: force field evaluation and comparison
     with experiment,” Journal of Chemical Theory and Computation, vol. 11,
     no. 7, pp. 3420–3431, 2015.

[13] P. Robustelli, S. Piana, and D. E. Shaw, “Developing a molecular dynam-
     ics force field for both folded and disordered protein states,” Proceedings
     of the National Academy of Sciences, vol. 115, no. 21, pp. E4758–E4766,
     2018.

[14] P. S. Nerenberg and T. Head-Gordon, “New developments in force fields
     for biomolecular simulations,” Current Opinion in Structural Biology,
     vol. 49, pp. 129–138, 2018.

[15] R. C. Bernardi, M. C. Melo, and K. Schulten, “Enhanced sampling tech-
     niques in molecular dynamics simulations of biological systems,” Biochim-
     ica et Biophysica Acta (BBA)-General Subjects, vol. 1850, no. 5, pp. 872–
     877, 2015.

[16] T. N. Cordeiro, P. C. Chen, A. De Biasio, N. Sibille, F. J. Blanco, J. S.
     Hub, R. Crehuet, and P. Bernadó, “Disentangling polydispersity in the
     PCNA-p15PAF complex, a disordered, transient and multivalent macro-
     molecular assembly,” Nucleic Acids Research, vol. 45, no. 3, pp. 1501–
     1515, 2017.

[17] S. Piana, K. Lindorff-Larsen, and D. E. Shaw, “Atomic-level description
     of ubiquitin folding,” Proceedings of the National Academy of Sciences,
     vol. 110, no. 15, pp. 5915–5920, 2013.

[18] K. Lindorff-Larsen, P. Maragakis, S. Piana, and D. E. Shaw, “Picosecond
     to millisecond structural dynamics in human ubiquitin,” The Journal of
     Physical Chemistry B, vol. 120, no. 33, pp. 8313–8320, 2016.

[19] V. A. Voelz, M. Jäger, S. Yao, Y. Chen, L. Zhu, S. A. Waldauer, G. R.
     Bowman, M. Friedrichs, O. Bakajin, L. J. Lapidus, et al., “Slow unfolded-
     state structuring in acyl-coa binding protein folding revealed by simulation
     and experiment,” Journal of the American Chemical Society, vol. 134,
     no. 30, pp. 12565–12577, 2012.

[20] G. R. Bowman, V. A. Voelz, and V. S. Pande, “Atomistic folding simu-
     lations of the five-helix bundle protein λ6- 85,” Journal of the American
     Chemical Society, vol. 133, no. 4, pp. 664–667, 2010.

[21] C. Camilloni and F. Pietrucci, “Advanced simulation techniques for the
     thermodynamic and kinetic characterization of biological systems,” Ad-
     vances in Physics: X, vol. 3, no. 1, p. 1477531, 2018.

[22] H. Wu, F. Nüske, F. Paul, S. Klus, P. Koltai, and F. Noé, “Varia-
     tional koopman models: Slow collective variables and molecular kinetics
     from short off-equilibrium simulations,” The Journal of Chemical Physics,
     vol. 146, no. 15, p. 154104, 2017.

[23] G. Hummer and J. Köfinger, “Bayesian ensemble refinement by replica
     simulations and reweighting,” The Journal of Chemical Physics, vol. 143,
     p. 243150, 2015.

[24] E. Ravera, L. Sgheri, and C. Luchinat, “A critical assessment of methods
     to recover information from averaged data,” Physical Chemistry Chemical
     Physics, vol. 18, pp. 5686–5701, 2016.

[25] E. T. Jaynes, “Information Theory and Statistical Mechanics,” The Phys-
     ical Review, vol. 106, no. 4, pp. 620–630, 1957.

[26] S. Kullback and R. Leibler, “On Information and Sufficiency,” Annals of
     Mathematical Statistics, vol. 22, no. 1, pp. 79–86, 1951.

[27] S. Hansen and J. Pedersen, “A comparison of three different methods for
     analysing small-angle scattering data,” Journal of Applied Crystallogra-
     phy, vol. 24, pp. 541–548, 1991.

[28] J. Skilling, Maximum Entropy and Bayesian Methods. Springer Nether-
     lands, 1989.

[29] B. Rózycki, Y. C. Kim, and G. Hummer, “SAXS ensemble refinement of
     ESCRT-III CHMP3 conformational transitions,” Structure, vol. 19, no. 1,
     pp. 109–116, 2011.

[30] H. T. A. Leung, O. Bignucolo, R. Aregger, S. A. Dames, A. Mazur,
     S. Bernèche, and S. Grzesiek, “A Rigorous and Efficient Method to
     Reweight Very Large Conformational Ensembles Using Average Exper-
     imental Data and to Determine Their Relative Information Content,”
     Journal of Chemical Theory and Computation, vol. 12, no. 1, pp. 383–
     394, 2016.

[31] K. Reichel, L. S. Stelzl, J. Köfinger, and G. Hummer, “Precision DEER
     Distances from Spin-Label Ensemble Refinement,” Journal of Physical
     Chemistry Letters, vol. 9, no. 19, pp. 5748–5752, 2018.

[32] S. Bottaro, G. Bussi, S. D. Kennedy, D. H. Turner, and K. Lindorff-Larsen,
     “Conformational ensembles of rna oligonucleotides from integrating nmr
     and molecular simulations,” Science Advances, vol. 4, no. 5, p. eaar8521,
     2018.

[33] E. T. Jaynes, Where Do We Stand on Maximum Entropy? In: Papers on
     Probability, Statistics and Statistical Physics. Springer, Dordrecht, 1978.

[34] B. Roux and J. Weare, “On the statistical equivalence of restrained-
     ensemble simulations with the maximum entropy method,” The Journal
     of Chemical Physics, vol. 138, no. 8, p. 084107, 2013.

[35] W. Boomsma, J. Ferkinghoff-Borg, and K. Lindorff-Larsen, “Combining
     Experiments and Simulations Using the Maximum Entropy Principle,”
     PLoS Computational Biology, vol. 10, no. 2, p. e1003406, 2014.

[36] A. Cesari, S. Reißer, and G. Bussi, “Using the Maximum Entropy Prin-
     ciple to Combine Simulations and Solution Experiments,” Computation,
     vol. 6, no. 1, p. 15, 2018.

[37] J. Köfinger, L. S. Stelzl, K. Reuter, C. Allande, K. Reichel, and G. Hum-
     mer, “Efficient ensemble refinement by reweighting,” Journal of Chemical
     Theory and Computation, vol. 15, no. 5, pp. 3390–3401, 2019.

[38] R. Shevchuk and J. S. Hub, “Bayesian refinement of protein structures and
     ensembles against SAXS data using molecular dynamics,” PLoS Compu-
     tational Biology, vol. 13, no. 10, pp. 1–27, 2017.

[39] A. Cavalli, M. Bonomi, C. Camilloni, and M. Vendruscolo, “Metainfer-
     ence: A Bayesian inference method for heterogeneous systems,” Science
     Advances, vol. 2, no. 1, pp. e1501177–e1501177, 2016.

[40] A. Cesari, A. Gil-Ley, and G. Bussi, “Combining simulations and solu-
     tion experiments as a paradigm for rna force field refinement,” Journal of
     Chemical Theory and Computation, vol. 12, no. 12, pp. 6192–6200, 2016.

[41] D. B. Amirkulova and A. D. White, “Recent advances in maximum en-
     tropy biasing techniques for molecular dynamics,” ArXiv, p. 1902.02252v1,
     2019.

[42] S. F. Gull and G. J. Daniell, “Image reconstruction from incomplete and
     noisy data,” Nature, vol. 272, pp. 686–690, 1978.

[43] H. Wiegand, “Kish, l.: Survey sampling. john wiley & sons, inc., new
     york, london 1965, ix + 643 s., 31 abb., 56 tab., preis 83 s.,” Biometrische
     Zeitschrift, vol. 10, no. 1, pp. 88–89, 1968.

[44] R. Rangan, M. Bonomi, G. T. Heller, A. Cesari, G. Bussi, and M. Ven-
     druscolo, “Determination of structural ensembles of proteins: restraining
     vs reweighting,” Journal of Chemical Theory and Computation, vol. 14,
     no. 12, pp. 6632–6641, 2018.

[45] H. A. I. Akaike, “A New Look at the Statistical Model Identification,”
     IEEE Transaction on Automatic Control, vol. 19, no. 6, pp. 716–723,
     1974.

[46] S. Bowerman, A. S. J. B. Rana, A. Rice, G. H. Pham, E. R. Strieter, and
     J. Wereszczynski, “Determining Atomistic SAXS Models of Tri-Ubiquitin
     Chains from Bayesian Analysis of Accelerated Molecular Dynamics Simu-
     lations Samuel,” Journal of Chemical The, vol. 13, no. 6, pp. 2418–2429,
     2017.

[47] E. Boura, B. Różycki, D. Z. Herrick, H. S. Chung, J. Vecer, W. A.
     Eaton, D. S. Cafiso, G. Hummer, and J. H. Hurley, “Solution struc-
     ture of the escrt-i complex by small-angle x-ray scattering, epr, and fret
     spectroscopy,” Proceedings of the National Academy of Sciences, vol. 108,
     no. 23, pp. 9437–9442, 2011.

[48] Y. Chen, S. L. Campbell, and N. V. Dokholyan, “Deciphering protein
     dynamics from NMR data using explicit structure sampling and selection,”
     Biophysical Journal, vol. 93, no. 7, pp. 2300–2306, 2007.

[49] D. M. Francis, B. Rä, D. Koveal, G. Hummer, R. Page, and W. Peti,
     “Structural basis of p38 regulation by hematopoietic tyrosine phos-
     phatase,” Nature Chemical Biology, vol. 7, no. 12, pp. 916–924, 2011.

[50] P. Cossio and G. Hummer, “Bayesian analysis of individual electron
     microscopy images: Towards structures of dynamic and heterogeneous
     biomolecular assemblies,” Journal of Structural Biology, vol. 184, no. 3,
     pp. 427–437, 2013.

[51] K. Berlin, C. A. Castañeda, D. Schneidman-Duhovny, A. Sali, A. Nava-
     Tudela, and D. Fushman, “Recovering a representative conformational
     ensemble from underdetermined macromolecular structural data,” Journal
     of the American Chemical Society, vol. 135, no. 44, pp. 16595–16609, 2013.

[52] D. Schneidman-Duhovny, M. Hammel, J. A. Tainer, and A. Sali, “FoXS ,
     FoXSDock and MultiFoXS : Single-state and multi-state structural mod-
     eling of proteins and their complexes based on SAXS profiles,” Nucleic
     Acids Research, vol. 44, no. Web server issue, pp. 424–429, 2016.

[53] W. Rieping, “Inferential Structure Determination,” Science, vol. 309,
     no. 5732, pp. 303–306, 2005.

[54] S. Olsson, J. Frellsen, W. Boomsma, K. V. Mardia, and T. Hamelryck,
     “Inference of structure ensembles of flexible biomolecules from sparse, av-
     eraged data,” PLOS ONE, vol. 8, pp. 1–7, 11 2013.

[55] R. Dutta, Z. F. Brotzakis, and A. Mira, “Bayesian calibration of force-
     fields from experimental data: Tip4p water,” The Journal of Chemical
     Physics, vol. 149, no. 15, p. 154110, 2018.

[56] P. Pernot and F. Cailliez, “A critical review of statistical calibra-
     tion/prediction models handling data inconsistency and model inade-
     quacy,” AIChE Journal, vol. 63, no. 10, pp. 4642–4665, 2017.

[57] K. A. Beauchamp, V. S. Pande, and R. Das, “Bayesian energy landscape
     tilting: Towards concordant models of molecular ensembles,” Biophysical
     Journal, vol. 106, no. 6, pp. 1381–1390, 2014.

[58] D. H. Brookes and T. Head-Gordon, “Experimental inferential structure
     determination of ensembles for intrinsically disordered proteins,” Journal
     of the American Chemical Society, vol. 138, no. 13, pp. 4530–4538, 2016.

[59] C. K. Fisher, A. Huang, and C. M. Stultz, “Modeling intrinsically disor-
     dered proteins with Bayesian statistics,” Journal of the American Chem-
     ical Society, vol. 132, no. 42, pp. 14919–14927, 2010.

[60] A. Sethi, D. Anunciado, J. Tian, D. M. Vu, and S. Gnanakaran, “Deduc-
     ing conformational variability of intrinsically disordered proteins from in-
     frared spectroscopy with Bayesian statistics,” Chemical Physics, vol. 422,
     pp. 143–155, 2013.

[61] X. Xiao, N. Kallenbach, and Y. Zhang, “Peptide conformation analysis
     using an integrated bayesian approach,” Journal of Chemical Theory and
     Computation, vol. 10, no. 9, pp. 4152–4159, 2014.

[62] Y. Ge and V. A. Voelz, “Model Selection Using BICePs: A Bayesian
     Approach for Force Field Validation and Parameterization,” Journal of
     Physical Chemistry B, vol. 122, no. 21, pp. 5610–5622, 2018.

[63] W. Potrzebowski, J. Trewhella, and I. Andre, “Bayesian inference of pro-
     tein conformational ensembles from limited structural data,” PLoS Com-
     putational Biology, vol. 14, no. 12, p. e1006641, 2018.

[64] S. Bottaro, T. Bengtsen, and K. Lindor, “Integrating Molecular Simula-
     tion and Experimental Data : A Bayesian / Maximum Entropy reweight-
     ing approach,” bioRxiv, 2018.

[65] K. S. Molnar, M. Bonomi, R. Pellarin, G. D. Clinthorne, G. Gonzalez,
     S. D. Goldberg, M. Goulian, A. Sali, and W. F. Degrado, “Cys-Scanning
     disulfide crosslinking and bayesian modeling probe the transmembrane
     signaling mechanism of the histidine kinase, PhoQ,” Structure, vol. 22,
     no. 9, pp. 1239–1251, 2014.

[66] M. Mechelke and M. Habeck, “Bayesian weighting of statistical potentials
     in nmr structure calculation,” PloS one, vol. 9, no. 6, p. e100197, 2014.

[67] L. D. Antonov, S. Olsson, W. Boomsma, and T. Hamelryck, “Bayesian in-
     ference of protein ensembles from SAXS data,” Physical Chemistry Chem-
     ical Physics, vol. 18, no. 8, pp. 5832–5838, 2016.

[68] M. Bonomi, G. T. Heller, C. Camilloni, and M. Vendruscolo, “Princi-
     ples of protein structural ensemble determination,” Current Opinion in
     Structural Biology, vol. 42, pp. 106–116, 2017.

[69] C. K. Fisher, O. Ullman, and C. M. Stultz, “Efficient construction of dis-
     ordered protein ensembles in a Bayesian framework with optimal selection
     of conformations,” Pac Symp Biocomput, pp. 82–93, 2012.

[70] S. Kirmizialtin, J. Loerke, E. Behrmann, C. M. Spahn, and K. Y. San-
     bonmatsu, Using molecular simulation to model high-resolution cryo-EM
     reconstructions, vol. 558. Elsevier Inc., 1 ed., 2015.

[71] D. J. C. MacKay, “Bayesian model comparison and backprop nets,” in
     Advances in Neural Information Processing Systems 4 (J. E. Moody, S. J.
     Hanson, and R. P. Lippmann, eds.), pp. 839–846, Morgan-Kaufmann,
     1992.

[72] A. H. Larsen, L. Arleth, and S. Hansen, “Analysis of small-angle scattering
     data using model fitting and Bayesian regularization,” Journal of Applied
     Crystallography, vol. 51, no. 4, pp. 1151–1161, 2018.

[73] M. Pelikan, G. L. Hura, and M. Hammel, “Structure and flexibility within
     proteins as identified through small angle x-ray scattering,” General Phys-
     iology and Biophysics, vol. 28, no. 2, p. 174, 2009.

[74] C. Vogel, M. Bashton, N. D. Kerrison, C. Chothia, and S. A. Teichmann,
     “Structure, function and evolution of multidomain proteins,” Current
     Opinion in Structural Biology, vol. 14, no. 2, pp. 208–216, 2004.

[75] H. J. Dyson and P. E. Wright, “Intrinsically unstructured proteins and
     their functions,” Nature Reviews Molecular Cell Biology, vol. 6, no. 3,
     pp. 197–208, 2005.

[76] K. Lindorff-Larsen, N. Trbovic, P. Maragakis, S. Piana, and D. E. Shaw,
     “Structure and dynamics of an unfolded protein examined by molecular
     dynamics simulation,” Journal of the American Chemical Society, vol. 134,
     no. 8, pp. 3787–3791, 2012.

[77] A. Rodriguez, M. d’Errico, E. Facco, and A. Laio, “Computing the free en-
     ergy without collective variables,” Journal of Chemical Theory and Com-
     putation, vol. 14, no. 3, pp. 1206–1215, 2018.

[78] R. F. Alford, A. Leaver-Fay, J. R. Jeliazkov, M. J. O’Meara, F. P. DiMaio,
     H. Park, M. V. Shapovalov, P. D. Renfrew, V. K. Mulligan, K. Kappel,
     J. W. Labonte, M. S. Pacella, R. Bonneau, P. Bradley, R. L. Dunbrack,
     R. Das, D. Baker, B. Kuhlman, T. Kortemme, and J. J. Gray, “The
     Rosetta All-Atom Energy Function for Macromolecular Modeling and De-
     sign,” Journal of Chemical Theory and Computation, vol. 13, pp. 3031–
     3048, 2017.

[79] R. E. Bellman, Adaptive control processes: a guided tour, vol. 2045. Prince-
     ton university press, 2015.

[80] N. Agmon, Y. Alhassid, and R. D. Levine, “An algorithm for finding
     the distribution of maximal entropy,” Journal of Computational Physics,
     vol. 30, no. 2, pp. 250–258, 1979.

[81] R. Malouf, “A comparison of algorithms for maximum entropy parame-
     ter estimation,” in Proceedings of the 6th conference on Natural language
     learning-Volume 20, pp. 1–7, Association for Computational Linguistics,
     2002.

[82] P. Bernadó, E. Mylonas, M. V. Petoukhov, M. Blackledge, and D. I. Sver-
     gun, “Structural characterization of flexible proteins using small-angle

    X-ray scattering,” Journal of the American Chemical Society, vol. 129,
    no. 17, pp. 5656–5664, 2007.

[83] G. Nodet, L. Salmon, V. Ozenne, S. Meier, M. R. Jensen, and M. Black-
     ledge, “Quantitative description of backbone conformational sampling of
     unfolded proteins at amino acid resolution from NMR residual dipolar
     couplings,” Journal of the American Chemical Society, vol. 131, no. 49,
     pp. 17908–17918, 2009.

[84] A. D. White and G. A. Voth, “Efficient and minimal method to bias molec-
     ular simulations with experimental data,” Journal of Chemical Theory and
     Computation, vol. 10, no. 8, pp. 3023–3030, 2014.

[85] A. D. White, J. F. Dama, and G. A. Voth, “Designing Free Energy Sur-
     faces That Match Experimental Data with Metadynamics,” Journal of
     Chemical Theory and Computation, vol. 11, no. 6, pp. 2451–2460, 2015.

[86] K. Lindorff-Larsen, R. B. Best, M. A. DePristo, C. M. Dobson, and
     M. Vendruscolo, “Simultaneous determination of protein structure and
     dynamics,” Nature, vol. 433, no. 7022, pp. 128–132, 2005.

[87] M. Vendruscolo, “Determination of conformationally heterogeneous states
     of proteins,” Current Opinion in Structural Biology, vol. 17, no. 1, pp. 15–
     20, 2007.

[88] B. T. Burnley, P. V. Afonine, P. D. Adams, and P. Gros, “Modelling
     dynamics in protein crystal structures by ensemble refinement,” eLife,
     vol. 1, p. e00311, 2012.

[89] E. J. Levin, D. A. Kondrashov, G. E. Wesenberg, and G. N. J. Phillips,
     “Ensemble refinement of protein crystal structures: validation and appli-
     cation,” Structure, vol. 15, no. 9, pp. 1040–1052, 2007.

[90] J. W. Pitera and J. D. Chodera, “On the use of experimental observations
     to bias simulated ensembles,” Journal of Chemical Theory and Computa-
     tion, vol. 8, no. 10, pp. 3445–3451, 2012.

[91] A. Cavalli, C. Camilloni, and M. Vendruscolo, “Molecular dynamics simu-
     lations with replica-averaged structural restraints generate structural en-
     sembles according to the maximum entropy principle,” The Journal of
     Chemical Physics, vol. 138, no. 9, p. 094112, 2013.

 [92] T. Löhr, C. Camilloni, M. Bonomi, and M. Vendruscolo, “A practical
      guide to the simultaneous determination of protein structure and dynam-
      ics using metainference,” arXiv preprint arXiv:1901.08030, 2019.

 [93] A. Laio and F. L. Gervasio, “Metadynamics: a method to simulate rare
      events and reconstruct the free energy in biophysics, chemistry and ma-
      terial science,” Reports on Progress in Physics, vol. 71, no. 12, p. 126601,
      2008.

 [94] A. Barducci, M. Bonomi, and M. Parrinello, “Metadynamics,” Wiley In-
      terdisciplinary Reviews: Computational Molecular Science, vol. 1, no. 5,
      pp. 826–843, 2011.

 [95] L. Sutto, S. Marsili, and F. L. Gervasio, “New advances in metadynamics,”
      Wiley Interdisciplinary Reviews: Computational Molecular Science, vol. 2,
      no. 5, pp. 771–779, 2012.

 [96] J. Pfaendtner and M. Bonomi, “Efficient sampling of high-dimensional
      free-energy landscapes with parallel bias metadynamics,” Journal of
      Chemical Theory and Computation, vol. 11, no. 11, pp. 5062–5067, 2015.

 [97] M. Bonomi, C. Camilloni, and M. Vendruscolo, “Metadynamic metain-
      ference: enhanced sampling of the metainference ensemble using metady-
      namics,” Scientific Reports, vol. 6, p. 31232, 2016.

 [98] A. Ianeselli, S. Orioli, G. Spagnolli, P. Faccioli, L. Cupellini, S. Jurinovich,
      and B. Mennucci, “Atomic detail of protein folding revealed by an ab
      initio reappraisal of circular dichroism,” Journal of the American Chemical
      Society, vol. 140, no. 10, pp. 3674–3682, 2018.

 [99] K. J. Kohlhoff, P. Robustelli, A. Cavalli, X. Salvatella, and M. Vendrus-
      colo, “Fast and accurate predictions of protein nmr chemical shifts from in-
      teratomic distances,” Journal of the American Chemical Society, vol. 131,
      no. 39, pp. 13894–13895, 2009.

[100] Y. Shen and A. Bax, “Sparta+: a modest improvement in empirical nmr
      chemical shift prediction by means of an artificial neural network,” Journal
      of Biomolecular NMR, vol. 48, no. 1, pp. 13–22, 2010.

[101] W. L. Jorgensen, D. S. Maxwell, and J. Tirado-Rives, “Development and
      testing of the opls all-atom force field on conformational energetics and
      properties of organic liquids,” Journal of the American Chemical Society,
      vol. 118, no. 45, pp. 11225–11236, 1996.

[102] C. Oostenbrink, A. Villa, A. E. Mark, and W. F. Van Gunsteren, “A
      biomolecular force field based on the free enthalpy of hydration and sol-
      vation: the gromos force-field parameter sets 53a5 and 53a6,” Journal of
      Computational Chemistry, vol. 25, no. 13, pp. 1656–1676, 2004.

[103] A. D. MacKerell Jr, D. Bashford, M. Bellott, R. L. Dunbrack Jr, J. D.
      Evanseck, M. J. Field, S. Fischer, J. Gao, H. Guo, S. Ha, et al., “All-
      atom empirical potential for molecular modeling and dynamics studies of
      proteins,” The Journal of Physical Chemistry B, vol. 102, no. 18, pp. 3586–
      3616, 1998.

[104] W. D. Cornell, P. Cieplak, C. I. Bayly, I. R. Gould, K. M. Merz, D. M.
      Ferguson, D. C. Spellmeyer, T. Fox, J. W. Caldwell, and P. A. Kollman,
      “A second generation force field for the simulation of proteins, nucleic
      acids, and organic molecules,” Journal of the American Chemical Society,
      vol. 117, no. 19, pp. 5179–5197, 1995.

[105] M. Tuckerman, Statistical mechanics: theory and molecular simulation.
      Oxford University Press, 2010.

[106] O. Guvench and A. D. MacKerell, Comparison of Protein Force Fields for
      Molecular Dynamics Simulations, pp. 63–88. Totowa, NJ: Humana Press,
      2008.

[107] J. W. Ponder and D. A. Case, “Force fields for protein simulations,” in
      Advances in Protein Chemistry, vol. 66, pp. 27–85, Elsevier, 2003.

[108] X. Zhu, P. E. Lopes, and A. D. MacKerell Jr, “Recent developments and
      applications of the charmm force fields,” Wiley Interdisciplinary Reviews:
      Computational Molecular Science, vol. 2, no. 1, pp. 167–185, 2012.

[109] P. Dauber-Osguthorpe and A. T. Hagler, “Biomolecular force fields: where
      have we been, where are we now, where do we need to go and how do we
      get there?,” Journal of Computer-aided Molecular Design, vol. 33, no. 2,
      pp. 133–203, 2019.

[110] A. T. Hagler, “Force field development phase ii: Relaxation of physics-
      based criteria. . . or inclusion of more rigorous physics into the represen-
      tation of molecular energetics,” Journal of Computer-aided Molecular De-
      sign, vol. 33, no. 2, pp. 205–264, 2019.

[111] C. I. Bayly, P. Cieplak, W. Cornell, and P. A. Kollman, “A well-behaved
      electrostatic potential based method using charge restraints for deriving

      atomic charges: the resp model,” The Journal of Physical Chemistry,
      vol. 97, no. 40, pp. 10269–10280, 1993.

[112] A. Jakalian, B. L. Bush, D. B. Jack, and C. I. Bayly, “Fast, efficient
      generation of high-quality atomic charges. am1-bcc model: I. method,”
      Journal of Computational Chemistry, vol. 21, no. 2, pp. 132–146, 2000.

[113] A. Jakalian, D. B. Jack, and C. I. Bayly, “Fast, efficient generation of high-
      quality atomic charges. am1-bcc model: Ii. parameterization and valida-
      tion,” Journal of Computational Chemistry, vol. 23, no. 16, pp. 1623–1641,
      2002.

[114] K. Lindorff-Larsen, S. Piana, K. Palmo, P. Maragakis, J. L. Klepeis, R. O.
      Dror, and D. E. Shaw, “Improved side-chain torsion potentials for the am-
      ber ff99sb protein force field,” Proteins: Structure, Function, and Bioin-
      formatics, vol. 78, no. 8, pp. 1950–1958, 2010.

[115] C. Tian, K. Kasavajhala, K. Belfon, L. Raguette, H. Huang, A. Migues,
      J. Bickel, Y. Wang, J. Pincay, Q. Wu, et al., “ff19sb: Amino-acid specific
      protein backbone parameters trained against quantum mechanics energy
      surfaces in solution,” ChemRxiv, 2019.

[116] A. B. Norgaard, J. Ferkinghoff-Borg, and K. Lindorff-Larsen, “Experimen-
      tal parameterization of an energy function for the simulation of unfolded
      proteins,” Biophysical Journal, vol. 94, no. 1, pp. 182–192, 2008.

[117] R. B. Best and G. Hummer, “Optimized molecular dynamics force fields
      applied to the helix- coil transition of polypeptides,” The Journal of Phys-
      ical Chemistry B, vol. 113, no. 26, pp. 9004–9015, 2009.

[118] F. Cailliez and P. Pernot, “Statistical approaches to forcefield calibra-
      tion and prediction uncertainty in molecular simulation,” The Journal of
      Chemical Physics, vol. 134, no. 5, p. 054124, 2011.

[119] F. Rizzi, H. N. Najm, B. J. Debusschere, K. Sargsyan, M. Salloum,
      H. Adalsteinsson, and O. M. Knio, “Uncertainty quantification in md sim-
      ulations. part ii: Bayesian inference of force-field parameters,” Multiscale
      Modeling & Simulation, vol. 10, no. 4, pp. 1460–1492, 2012.

[120] P. Angelikopoulos, C. Papadimitriou, and P. Koumoutsakos, “Bayesian
      uncertainty quantification and propagation in molecular dynamics simu-
      lations: a high performance computing framework,” The Journal of Chem-
      ical Physics, vol. 137, no. 14, p. 144103, 2012.

[121] L.-P. Wang, J. Chen, and T. Van Voorhis, “Systematic parametrization of
      polarizable force fields from quantum chemistry data,” Journal of Chem-
      ical Theory and Computation, vol. 9, no. 1, pp. 452–460, 2012.

[122] L.-P. Wang, T. J. Martinez, and V. S. Pande, “Building force fields: An
      automatic, systematic, and reproducible approach,” The Journal of Phys-
      ical Chemistry Letters, vol. 5, no. 11, pp. 1885–1891, 2014.

[123] S. Wu, P. Angelikopoulos, C. Papadimitriou, R. Moser, and P. Koumout-
      sakos, “A hierarchical bayesian framework for force field selection in
      molecular dynamics simulations,” Philosophical Transactions of the Royal
      Society A: Mathematical, Physical and Engineering Sciences, vol. 374,
      no. 2060, p. 20150032, 2016.

[124] L.-P. Wang, K. A. McKiernan, J. Gomes, K. A. Beauchamp, T. Head-
      Gordon, J. E. Rice, W. C. Swope, T. J. Martı́nez, and V. S. Pande, “Build-
      ing a more predictive protein force field: a systematic and reproducible
      route to amber-fb15,” The Journal of Physical Chemistry B, vol. 121,
      no. 16, pp. 4023–4039, 2017.

[125] A. M. Bonvin, R. Boelens, and R. Kaptein, “Time-and ensemble-averaged
      direct noe restraints,” Journal of Biomolecular NMR, vol. 4, no. 1,
      pp. 143–149, 1994.

[126] J.-r. Huang and S. Grzesiek, “Ensemble calculations of unstructured pro-
      teins constrained by rdc and pre data: a case study of urea-denatured
      ubiquitin,” Journal of the American Chemical Society, vol. 132, no. 2,
      pp. 694–705, 2009.

[127] O. F. Lange, N.-A. Lakomek, C. Farès, G. F. Schröder, K. F. Walter,
      S. Becker, J. Meiler, H. Grubmüller, C. Griesinger, and B. L. De Groot,
      “Recognition dynamics up to microseconds revealed from an rdc-derived
      ubiquitin ensemble in solution,” Science, vol. 320, no. 5882, pp. 1471–1475,
      2008.

[128] S. Olsson, B. R. Vögeli, A. Cavalli, W. Boomsma, J. Ferkinghoff-Borg,
      K. Lindorff-Larsen, and T. Hamelryck, “Probabilistic determination of
      native state ensembles of proteins,” Journal of Chemical Theory and Com-
      putation, vol. 10, no. 8, pp. 3484–3491, 2014.

[129] S. Esteban-Martı́n, R. B. Fenwick, and X. Salvatella, “Refinement of
      ensembles describing unstructured proteins using nmr residual dipolar

      couplings,” Journal of the American Chemical Society, vol. 132, no. 13,
      pp. 4626–4632, 2010.

[130] R. Scheek, A. Torda, J. Kemmink, and W. Van Gunsteren, “Structure
      determination by nmr: The modeling of nmr parameters as ensemble av-
      erages,” in Computational aspects of the study of biological macromolecules
      by nuclear magnetic resonance spectroscopy, pp. 209–217, Springer, 1991.

[131] A. B. Mantsyzov, A. S. Maltsev, J. Ying, Y. Shen, G. Hummer, and
      A. Bax, “A maximum entropy approach to the study of residue-specific
      backbone angle distributions in α-synuclein, an intrinsically disordered
      protein,” Protein Science, vol. 23, no. 9, pp. 1275–1290, 2014.

[132] A. B. Mantsyzov, Y. Shen, J. H. Lee, G. Hummer, and A. Bax, “Mera: a
      webserver for evaluating backbone torsion angle distributions in dynamic
      and disordered proteins from nmr data,” Journal of Biomolecular NMR,
      vol. 63, no. 1, pp. 85–95, 2015.

[133] J. Graf, P. H. Nguyen, G. Stock, and H. Schwalbe, “Structure and dy-
      namics of the homologous series of alanine peptides: a joint molecular dy-
      namics/nmr study,” Journal of the American Chemical Society, vol. 129,
      no. 5, pp. 1179–1189, 2007.

[134] A. Cesari, S. Bottaro, K. Lindorff-Larsen, P. Banáš, J. Sponer, and
      G. Bussi, “Fitting corrections to an rna force field using experimental
      data,” Journal of Chemical Theory and Computation, 2019.

[135] F. Vasile and G. Tiana, “Determination of structural ensembles of flexible
      molecules in solution from nmr data undergoing spin diffusion,” Journal
      of Chemical Information and Modeling, 2019.

[136] R. W. Zwanzig, “High-temperature equation of state by a perturbation
      method. i. nonpolar gases,” The Journal of Chemical Physics, vol. 22,
      no. 8, pp. 1420–1426, 1954.

[137] D.-W. Li and R. Brüschweiler, “Nmr-based protein potentials,” Ange-
      wandte Chemie International Edition, vol. 49, no. 38, pp. 6778–6780, 2010.

[138] D.-W. Li and R. Brüschweiler, “Iterative optimization of molecular me-
      chanics force fields from nmr data of full-length proteins,” Journal of
      Chemical Theory and Computation, vol. 7, no. 6, pp. 1773–1782, 2011.

[139] J. Chen, J. Chen, G. Pinamonti, and C. Clementi, “Learning effective
      molecular models from experimental observables,” Journal of Chemical
      Theory and Computation, vol. 14, no. 7, pp. 3849–3858, 2018.

[140] S. A. Teukolsky, B. P. Flannery, W. Press, and W. Vetterling, “Numerical
      recipes in c,” SMR, vol. 693, no. 1, pp. 59–70, 1992.

[141] R. Brüschweiler, “Collective protein dynamics and nuclear spin relax-
      ation,” The Journal of Chemical Physics, vol. 102, no. 8, pp. 3396–3403,
      1995.

[142] C. H. Bennett, “Efficient estimation of free energy differences from monte
      carlo data,” Journal of Computational Physics, vol. 22, no. 2, pp. 245–268,
      1976.

[143] M. R. Shirts and J. D. Chodera, “Statistically optimal analysis of sam-
      ples from multiple equilibrium states,” The Journal of Chemical Physics,
      vol. 129, no. 12, p. 124105, 2008.

[144] J. R. Gillespie and D. Shortle, “Characterization of long-range structure
      in the denatured state of staphylococcal nuclease. i. paramagnetic relax-
      ation enhancement by nitroxide spin labels,” Journal of Molecular Biology,
      vol. 268, no. 1, pp. 158–169, 1997.

[145] M. A. Lietzow, M. Jamin, H. J. Dyson, and P. E. Wright, “Mapping
      long-range contacts in a highly unfolded protein,” Journal of Molecular
      Biology, vol. 322, no. 4, pp. 655–662, 2002.

[146] Q. Yi, M. L. Scalley-Kim, E. J. Alm, and D. Baker, “Nmr characteriza-
      tion of residual structure in the denatured state of protein l,” Journal of
      Molecular Biology, vol. 299, no. 5, pp. 1341–1351, 2000.

[147] K. Teilum, B. B. Kragelund, and F. M. Poulsen, “Transient structure
      formation in unfolded acyl-coenzyme a-binding protein observed by site-
      directed spin labelling,” Journal of Molecular Biology, vol. 324, no. 2,
      pp. 349–357, 2002.

[148] J. R. Gillespie and D. Shortle, “Characterization of long-range structure in
      the denatured state of staphylococcal nuclease. ii. distance restraints from
      paramagnetic relaxation and calculation of an ensemble of structures,”
      Journal of Molecular Biology, vol. 268, no. 1, pp. 170–184, 1997.

[149] V. Hornak, R. Abel, A. Okur, B. Strockbine, A. Roitberg, and C. Sim-
      merling, “Comparison of multiple amber force fields and development of
      improved protein backbone parameters,” Proteins: Structure, Function,
      and Bioinformatics, vol. 65, no. 3, pp. 712–725, 2006.

[150] D. E. Condon, S. D. Kennedy, B. C. Mort, R. Kierzek, I. Yildirim, and
      D. H. Turner, “Stacking in rna: Nmr of four tetramers benchmark molec-
      ular dynamics,” Journal of Chemical Theory and Computation, vol. 11,
      no. 6, pp. 2729–2742, 2015.

[151] C. Bergonzo, N. M. Henriksen, D. R. Roe, and T. E. Cheatham, “Highly
      sampled tetranucleotide and tetraloop motifs enable evaluation of common
      rna force fields,” RNA, vol. 21, no. 9, pp. 1578–1590, 2015.

[152] P. Kuhrova, R. B. Best, S. Bottaro, G. Bussi, J. Sponer, M. Otyepka, and
      P. Banas, “Computer folding of rna tetraloops: identification of key force
      field deficiencies,” Journal of Chemical Theory and Computation, vol. 12,
      no. 9, pp. 4534–4548, 2016.

[153] S. Bottaro, P. Banáš, J. Sponer, and G. Bussi, “Free energy landscape of
      gaga and uucg rna tetraloops,” The Journal of Physical Chemistry Letters,
      vol. 7, no. 20, pp. 4032–4038, 2016.

[154] A. N. Borkar, M. F. Bardaro, C. Camilloni, F. A. Aprile, G. Varani,
      and M. Vendruscolo, “Structure of a low-population binding intermedi-
      ate in protein-rna recognition,” Proceedings of the National Academy of
      Sciences, vol. 113, no. 26, pp. 7171–7176, 2016.

[155] M. Krepl, M. Blatter, A. Cléry, F. F. Damberger, F. H. Allain, and
      J. Sponer, “Structural study of the fox-1 rrm protein hydration reveals
      a role for key water molecules in rrm-rna recognition,” Nucleic Acids Re-
      search, vol. 45, no. 13, pp. 8046–8063, 2017.

[156] P. Podbevšek, F. Fasolo, C. Bon, L. Cimatti, S. Reißer, P. Carninci,
      G. Bussi, S. Zucchelli, J. Plavec, and S. Gustincich, “Structural deter-
      minants of the sine b2 element embedded in the long non-coding rna
      activator of translation as uchl1,” Scientific Reports, vol. 8, no. 1, p. 3189,
      2018.

[157] H. Kooshapur, N. R. Choudhury, B. Simon, M. Mühlbauer, A. Jussupow,
      N. Fernandez, A. N. Jones, A. Dallmann, F. Gabel, C. Camilloni, et al.,

     “Structural basis for terminal loop recognition and stimulation of pri-
     mirna-18a processing by hnrnp a1,” Nature Communications, vol. 9, no. 1,
     p. 2479, 2018.

[158] A. H. Aytenfisu, A. Spasic, A. Grossfield, H. A. Stern, and D. H. Math-
      ews, “Revised rna dihedral parameters for the amber force field improve
      rna molecular dynamics,” Journal of Chemical Theory and Computation,
      vol. 13, no. 2, pp. 900–915, 2017.

[159] D. Tan, S. Piana, R. M. Dirks, and D. E. Shaw, “Rna force field with
      accuracy comparable to state-of-the-art protein force fields,” Proceedings
      of the National Academy of Sciences, vol. 115, no. 7, pp. E1346–E1355,
      2018.

[160] P. Kuhrova, V. Mlynsky, M. Zgarbova, M. Krepl, G. Bussi, R. B. Best,
      M. Otyepka, J. Sponer, and P. Banas, “Improving the performance of
      the amber rna force field by tuning the hydrogen-bonding interactions,”
      Journal of Chemical Theory and Computation, vol. 15, no. 5, pp. 3288–
      3305, 2019.

[161] A. Pérez, I. Marchán, D. Svozil, J. Sponer, T. E. Cheatham III, C. A.
      Laughton, and M. Orozco, “Refinement of the amber force field for nucleic
      acids: improving the description of α/γ conformers,” Biophysical Journal,
      vol. 92, no. 11, pp. 3817–3829, 2007.

[162] M. Zgarbová, M. Otyepka, J. Šponer, A. Mládek, P. Banáš, T. E.
      Cheatham III, and P. Jurecka, “Refinement of the cornell et al. nucleic
      acids force field based on reference quantum chemical calculations of gly-
      cosidic torsion profiles,” Journal of Chemical Theory and Computation,
      vol. 7, no. 9, pp. 2886–2902, 2011.

[163] S. Izadi, R. Anandakrishnan, and A. V. Onufriev, “Building water models:
      a different approach,” The Journal of Physical Chemistry Letters, vol. 5,
      no. 21, pp. 3863–3871, 2014.

[164] V. S. Pande, K. Beauchamp, and G. R. Bowman, “Everything you wanted
      to know about markov state models but were afraid to ask,” Methods,
      vol. 52, no. 1, pp. 99–105, 2010.

[165] G. R. Bowman, V. S. Pande, and F. Noé, An introduction to Markov
      state models and their application to long timescale molecular simulation,
      vol. 797. Springer Science & Business Media, 2013.

[166] B. E. Husic and V. S. Pande, “Markov state models: From an art to
      a science,” Journal of the American Chemical Society, vol. 140, no. 7,
      pp. 2386–2396, 2018.

[167] A. G. Palmer III, “Nmr characterization of the dynamics of biomacro-
      molecules,” Chemical Reviews, vol. 104, no. 8, pp. 3623–3640, 2004.

[168] J.-H. Prinz, H. Wu, M. Sarich, B. Keller, M. Senne, M. Held, J. D.
      Chodera, C. Schütte, and F. Noé, “Markov models of molecular kinetics:
      Generation and validation,” The Journal of Chemical Physics, vol. 134,
      no. 17, p. 174105, 2011.

[169] C. R. Schwantes, R. T. McGibbon, and V. S. Pande, “Perspective: Markov
      models for long-timescale biomolecular dynamics,” The Journal of Chem-
      ical Physics, vol. 141, no. 9, p. 09B201 1, 2014.

[170] E. T. Jaynes, “The minimum entropy production principle,” Annual Re-
      view of Physical Chemistry, vol. 31, no. 1, pp. 579–601, 1980.

[171] N. Salvi, A. Abyzov, and M. Blackledge, “Multi-timescale dynamics in in-
      trinsically disordered proteins from nmr relaxation and molecular simula-
      tion,” The Journal of Physical Chemistry Letters, vol. 7, no. 13, pp. 2483–
      2489, 2016.

[172] S. Olsson, H. Wu, F. Paul, C. Clementi, and F. Noé, “Combining experi-
      mental and simulation data of molecular processes via augmented markov
      models,” Proceedings of the National Academy of Sciences, vol. 114, no. 31,
      pp. 8265–8270, 2017.

[173] G. R. Bowman, K. A. Beauchamp, G. Boxer, and V. S. Pande, “Progress
      and challenges in the automated construction of markov state models for
      full protein systems,” The Journal of Chemical Physics, vol. 131, no. 12,
      p. 124101, 2009.

[174] M. M. Sultan, G. Kiss, D. Shukla, and V. S. Pande, “Automatic selection
      of order parameters in the analysis of large scale molecular dynamics sim-
      ulations,” Journal of Chemical Theory and Computation, vol. 10, no. 12,
      pp. 5217–5223, 2014.

[175] G. Pérez-Hernández, F. Paul, T. Giorgino, G. De Fabritiis, and F. Noé,
      “Identification of slow molecular order parameters for markov model con-
      struction,” The Journal of Chemical Physics, vol. 139, no. 1, p. 07B604 1,
      2013.

[176] C. R. Schwantes and V. S. Pande, “Improvements in markov state model
      construction reveal many non-native interactions in the folding of ntl9,”
      Journal of Chemical Theory and Computation, vol. 9, no. 4, pp. 2000–
      2009, 2013.

[177] F. Noé and C. Clementi, “Kinetic distance and kinetic maps from molecu-
      lar dynamics simulation,” Journal of Chemical Theory and Computation,
      vol. 11, no. 10, pp. 5002–5011, 2015.

[178] M. K. Scherer, B. Trendelkamp-Schroer, F. Paul, G. Pérez-Hernández,
      M. Hoffmann, N. Plattner, C. Wehmeyer, J.-H. Prinz, and F. Noé,
      “Pyemma 2: A software package for estimation, validation, and analy-
      sis of markov models,” Journal of Chemical Theory and Computation,
      vol. 11, no. 11, pp. 5525–5542, 2015.

[179] M. P. Harrigan, M. M. Sultan, C. X. Hernández, B. E. Husic, P. Eastman,
      C. R. Schwantes, K. A. Beauchamp, R. T. McGibbon, and V. S. Pande,
      “Msmbuilder: statistical models for biomolecular dynamics,” Biophysical
      Journal, vol. 112, no. 1, pp. 10–15, 2017.

[180] F. Noé and E. Rosta, “Markov models of molecular kinetics,” The Journal
      of Chemical Physics, vol. MMMK, p. 190401, 2019.

[181] Y. Xue, J. M. Ward, T. Yuwen, I. S. Podkorytov, and N. R. Skryn-
      nikov, “Microsecond time-scale conformational exchange in proteins: us-
      ing long molecular dynamics trajectory to simulate nmr relaxation dis-
      persion data,” Journal of the American Chemical Society, vol. 134, no. 5,
      pp. 2555–2562, 2012.

[182] S. Olsson and F. No’e, “Mechanistic models of chemical exchange induced
      relaxation in protein nmr,” Journal of the American Chemical Society,
      vol. 139, no. 1, pp. 200–210, 2016.

[183] S. Pressé, K. Ghosh, J. Lee, and K. A. Dill, “Principles of maximum
      entropy and maximum caliber in statistical physics,” Reviews of Modern
      Physics, vol. 85, no. 3, p. 1115, 2013.

[184] P. G. Bolhuis, D. Chandler, C. Dellago, and P. L. Geissler, “Transition
      path sampling: Throwing ropes over rough mountain passes, in the dark,”
      Annual Review of Physical Chemistry, vol. 53, no. 1, pp. 291–318, 2002.

[185] P. Eastman, N. Grønbech-Jensen, and S. Doniach, “Simulation of protein
      folding by reaction path annealing,” The Journal of Chemical Physics,
      vol. 114, no. 8, pp. 3823–3841, 2001.

[186] A. C. Pan, D. Sezer, and B. Roux, “Finding transition pathways using
      the string method with swarms of trajectories,” The Journal of Physical
      Chemistry B, vol. 112, no. 11, pp. 3432–3440, 2008.

[187] E. Weinan, W. Ren, and E. Vanden-Eijnden, “String method for the study
      of rare events,” Physical Review B, vol. 66, no. 5, p. 052301, 2002.

[188] R. Capelli, G. Tiana, and C. Camilloni, “An implementation of the
      maximum-caliber principle by replica-averaged time-resolved restrained
      simulations,” The Journal of Chemical Physics, vol. 148, no. 18, p. 184114,
      2018.

[189] B. Roux and J. Weare, “On the statistical equivalence of restrained-
      ensemble simulations with the maximum entropy method,” The Journal
      of Chemical Physics, vol. 138, no. 8, p. 02B616, 2013.

[190] A. Cavalli, C. Camilloni, and M. Vendruscolo, “Molecular dynamics simu-
      lations with replica-averaged structural restraints generate structural en-
      sembles according to the maximum entropy principle,” The Journal of
      Chemical Physics, vol. 138, no. 9, p. 03B603, 2013.

[191] P. D. Dixit and K. A. Dill, “Caliber corrected markov modeling (c2m2):
      Correcting equilibrium markov models,” Journal of Chemical Theory and
      Computation, vol. 14, no. 2, pp. 1111–1119, 2018.

[192] P. D. Dixit, “Communication: Introducing prescribed biases in out-of-
      equilibrium markov models,” The Journal of Chemical Physics, vol. 148,
      no. 9, p. 091101, 2018.

[193] M. Bause, T. Wittenstein, K. Kremer, and T. Bereau, “Microscopic
      reweighting for non-equilibrium steady states dynamics,” arXiv preprint
      arXiv:1907.08480, 2019.

[194] N. Salvi, A. Abyzov, and M. Blackledge, “Solvent-dependent segmental
      dynamics in intrinsically disordered proteins,” Science Advances, vol. 5,
      no. 6, p. eaax2348, 2019.

[195] R. Shevchuk and J. S. Hub, “Bayesian refinement of protein structures
      and ensembles against saxs data using molecular dynamics,” PLoS Com-
      putational Biology, vol. 13, no. 10, p. e1005800, 2017.

[196] R. Andrae, T. Schulze-Hartung, and P. Melchior, “Dos and don’ts of re-
      duced chi-squared,” arXiv, p. 1012.374v1, 2010.

[197] P. C. Hansen, “The l-curve and its use in the numerical treatment of in-
      verse problems,” in Computational Inverse Problems in Electrocardiology,
      WIT Press, 2000.

[198] P.-c. Chen, R. Shevchuk, F. M. Strnad, C. Lorenz, L. Karge, R. Gilles,
      A. M. Stadler, J. Hennig, and J. S. Hub, “Combined small-angle x-ray and
      neutron scattering restraints in molecular dynamics simulations,” Journal
      of Chemical Theory and Computation, vol. 0, p. 0, 0.

[199] R. Crehuet, P. J. B. Jorro, K. Lindorff-Larsen, and X. Salvatella,
      “Bayesian-maximum-entropy reweighting of idps ensembles based on nmr
      chemical shifts,” bioRxiv, p. 689083, 2019.

[200] A. C. Stark, C. T. Andrews, and A. H. Elcock, “Toward optimized po-
      tential functions for protein-protein interactions in aqueous solutions: Os-
      motic second virial coefficient calculations using the MARTINI coarse-
      grained force field,” Journal of Chemical Theory and Computation, vol. 9,
      no. 9, pp. 4176–4185, 2013.

[201] M. Javanainen, H. Martinez-Seara, and I. Vattulainen, “Excessive aggre-
      gation of membrane proteins in the martini model,” PLOS ONE, vol. 12,
      pp. 1–20, 11 2017.

[202] R. B. Best, W. Zheng, and J. Mittal, “Balanced protein–water interac-
      tions improve properties of disordered proteins and non-specific protein
      association,” Journal of chemical theory and computation, vol. 10, no. 11,
      pp. 5113–5124, 2014.

[203] A. Hospital, J. R. Goñi, M. Orozco, and J. L. Gelpı́, “Molecular dynamics
      simulations: advances and applications,” Advances and Applications in
      Bioinformatics and Chemistry: AABC, vol. 8, p. 37, 2015.

[204] D. L. Mobley, C. C. Bannan, A. Rizzi, C. I. Bayly, J. D. Chodera, V. T.
      Lim, N. M. Lim, K. A. Beauchamp, D. R. Slochower, M. R. Shirts, et al.,
      “Escaping atom types in force fields using direct chemical perception,”
      Journal of Chemical Theory and Computation, vol. 14, no. 11, pp. 6076–
      6092, 2018.

[205] C. Zanette, C. C. Bannan, C. I. Bayly, J. Fass, M. K. Gilson, M. R. Shirts,
      J. D. Chodera, and D. L. Mobley, “Toward learned chemical perception

     of force field typing rules,” Journal of chemical theory and computation,
     vol. 15, no. 1, pp. 402–423, 2018.

[206] Open Force Field Initiative, “Open force field initiative,” 2019. [Online;
      accessed 28-July-2019].
