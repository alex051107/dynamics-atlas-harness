# FRET-based dynamic structural biology: challenges, perspectives and an appeal for open-science practices

**Authors:** Eitan Lerner, Anders Barth, Jelle Hendrix, Benjamin Ambrose, Victoria Birkedal, Scott C. Blanchard, et al.
**Year:** 2021
**Venue:** eLife
**DOI:** 10.7554/eLife.60416
**Source PDF URL:** https://cdn.elifesciences.org/articles/60416/elife-60416-v2.pdf
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

REVIEW ARTICLE


                                     FRET-based dynamic structural biology:
                                     Challenges, perspectives and an appeal
                                     for open-science practices
                                     Eitan Lerner1†*, Anders Barth2†*, Jelle Hendrix3†*, Benjamin Ambrose4,
                                     Victoria Birkedal5, Scott C Blanchard6, Richard Börner7, Hoi Sung Chung8,
                                     Thorben Cordes9, Timothy D Craggs4, Ashok A Deniz10, Jiajia Diao11, Jingyi Fei12,
                                     Ruben L Gonzalez13, Irina V Gopich8, Taekjip Ha14, Christian A Hanke2,
                                     Gilad Haran15, Nikos S Hatzakis16,17, Sungchul Hohng18, Seok-Cheol Hong19,
                                     Thorsten Hugel20, Antonino Ingargiola21, Chirlmin Joo22, Achillefs N Kapanidis23,
                                     Harold D Kim24, Ted Laurence25, Nam Ki Lee26, Tae-Hee Lee27,
                                     Edward A Lemke28,29, Emmanuel Margeat30, Jens Michaelis31, Xavier Michalet21,
                                     Sua Myong32, Daniel Nettels33, Thomas-Otavio Peulen34, Evelyn Ploetz35,
                                     Yair Razvag1, Nicole C Robb36, Benjamin Schuler33, Hamid Soleimaninejad37,
                                     Chun Tang38, Reza Vafabakhsh39, Don C Lamb35*, Claus AM Seidel2*,
                                     Shimon Weiss21,40*
                                      Department of Biological Chemistry, The Alexander Silberman Institute of Life
                                     Sciences, and The Center for Nanoscience and Nanotechnology, Faculty of
                                     Mathematics & Science, The Edmond J. Safra Campus, The Hebrew University of
*For correspondence:                 Jerusalem, Jerusalem, Israel; 2Lehrstuhl für Molekulare Physikalische Chemie,
eitan.lerner@mail.huji.ac.il (EL);   Heinrich-Heine-Universität, Düsseldorf, Germany; 3Dynamic Bioimaging Lab,
a.barth@tudelft.nl (AB);             Advanced Optical Microscopy Centre and Biomedical Research Institute (BIOMED),
jelle.hendrix@uhasselt.be (JH);
                                     Hasselt University, Diepenbeek, Belgium; 4Department of Chemistry, University of
d.lamb@lmu.de (DCL);
cseidel@hhu.de (CAMS);               Sheffield, Sheffield, United Kingdom; 5Department of Chemistry and iNANO center,
sweiss@chem.ucla.edu (SW)            Aarhus University, Aarhus, Denmark; 6Department of Structural Biology, St. Jude
†
 These authors contributed
                                     Children’s Research Hospital, Memphis, United States; 7Laserinstitut HS Mittweida,
equally to this work                 University of Applied Science Mittweida, Mittweida, Germany; 8Laboratory of
                                     Chemical Physics, National Institute of Diabetes and Digestive and Kidney Diseases,
Competing interests: The
authors declare that no
                                     National Institutes of Health, Bethesda, United States; 9Physical and Synthetic
competing interests exist.           Biology, Faculty of Biology, Ludwig-Maximilians-Universität München, Planegg-
                                     Martinsried, Germany; 10Department of Integrative Structural and Computational
Funding: See page 41
                                     Biology, The Scripps Research Institute, La Jolla, United States; 11Department of
Received: 29 June 2020
                                     Cancer Biology, University of Cincinnati School of Medicine, Cincinnati, United
Accepted: 09 February 2021
Published: 29 March 2021
                                     States; 12Department of Biochemistry and Molecular Biology and The Institute for
                                     Biophysical Dynamics, University of Chicago, Chicago, United States; 13Department
Reviewing editor: Olga               of Chemistry, Columbia University, New York, United States; 14Department of
Boudker, Weill Cornell Medicine,
United States
                                     Biophysics and Biophysical Chemistry, Department of Biomedical Engineering,
                                     Johns Hopkins University School of Medicine, Howard Hughes Medical Institute,
   This is an open-access article,
                                     Baltimore, United States; 15Department of Chemical and Biological Physics,
free of all copyright, and may be
freely reproduced, distributed,
                                     Weizmann Institute of Science, Rehovot, Israel; 16Department of Chemistry &
transmitted, modified, built         Nanoscience Centre, University of Copenhagen, Copenhagen, Denmark; 17Denmark
upon, or otherwise used by           Novo Nordisk Foundation Centre for Protein Research, Faculty of Health and
anyone for any lawful purpose.       Medical Sciences, University of Copenhagen, Copenhagen, Denmark; 18Department
The work is made available under     of Physics and Astronomy, and Institute of Applied Physics, Seoul National
the Creative Commons CC0
public domain dedication.
                                     University, Seoul, Republic of Korea; 19Center for Molecular Spectroscopy and


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                      1 of 69




                                    Dynamics, Institute for Basic Science and Department of Physics, Korea University,
                                    Seoul, Republic of Korea; 20Institute of Physical Chemistry and Signalling Research
                                    Centres BIOSS and CIBSS, University of Freiburg, Freiburg, Germany; 21Department
                                    of Chemistry and Biochemistry, and Department of Physiology, University of
                                    California, Los Angeles, Los Angeles, United States; 22Department of
                                    BioNanoScience, Kavli Institute of Nanoscience, Delft University of Technology,
                                    Delft, Netherlands; 23Biological Physics Research Group, Clarendon Laboratory,
                                    Department of Physics, University of Oxford, Oxford, United Kingdom; 24School of
                                    Physics, Georgia Institute of Technology, Atlanta, United States; 25Physical and Life
                                    Sciences Directorate, Lawrence Livermore National Laboratory, Livermore, United
                                    States; 26School of Chemistry, Seoul National University, Seoul, Republic of Korea;
                                      Department of Chemistry, Pennsylvania State University, University Park, United
                                    States; 28Departments of Biology and Chemistry, Johannes Gutenberg University,
                                    Mainz, Germany; 29Institute of Molecular Biology (IMB), Mainz, Germany; 30Centre
                                    de Biologie Structurale (CBS), CNRS, INSERM, Universitié de Montpellier,
                                    Montpellier, France; 31Institüt of Biophysics, Ulm University, Ulm, Germany;
                                      Department of Biophysics, Johns Hopkins University, Baltimore, United States;
                                      Department of Biochemistry and Department of Physics, University of Zurich,
                                    Zurich, Switzerland; 34Department of Bioengineering and Therapeutic Sciences,
                                    University of California, San Francisco, San Francisco, United States; 35Physical
                                    Chemistry, Department of Chemistry, Center for Nanoscience (CeNS), Center for
                                    Integrated Protein Science Munich (CIPSM) and Nanosystems Initiative Munich
                                    (NIM), Ludwig-Maximilians-Universität, München, Germany; 36Warwick Medical
                                    School, University of Warwick, Coventry, United Kingdom; 37Biological Optical
                                    Microscopy Platform (BOMP), University of Melbourne, Parkville, Australia;
                                      College of Chemistry and Molecular Engineering, PKU-Tsinghua Center for Life
                                    Sciences, Beijing National Laboratory for Molecular Sciences, Peking University,
                                    Beijing, China; 39Department of Molecular Biosciences, Northwestern University,
                                    Evanston, United States; 40Department of Physiology, CaliforniaNanoSystems
                                    Institute, University of California, Los Angeles, Los Angeles, United States


                                    Abstract Single-molecule FRET (smFRET) has become a mainstream technique for studying
                                    biomolecular structural dynamics. The rapid and wide adoption of smFRET experiments by an ever-
                                    increasing number of groups has generated significant progress in sample preparation,
                                    measurement procedures, data analysis, algorithms and documentation. Several labs that employ
                                    smFRET approaches have joined forces to inform the smFRET community about streamlining how
                                    to perform experiments and analyze results for obtaining quantitative information on biomolecular
                                    structure and dynamics. The recent efforts include blind tests to assess the accuracy and the
                                    precision of smFRET experiments among different labs using various procedures. These multi-lab
                                    studies have led to the development of smFRET procedures and documentation, which are
                                    important when submitting entries into the archiving system for integrative structure models, PDB-
                                    Dev. This position paper describes the current ‘state of the art’ from different perspectives, points
                                    to unresolved methodological issues for quantitative structural studies, provides a set of ‘soft
                                    recommendations’ about which an emerging consensus exists, and lists openly available resources
                                    for newcomers and seasoned practitioners. To make further progress, we strongly encourage
                                    ‘open science’ practices.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                             2 of 69



                                    Introduction
                                    Understanding how biomolecules couple structural dynamics with function is at the heart of several
                                    disciplines and remains an outstanding goal in biology. Linking conformational states and their tran-
                                    sitions to biochemical function requires the ability to precisely resolve the structure and dynamics of
                                    a biological system, which is often altered upon ligand binding or influenced by the chemical and
                                    physical properties of its environment. The most well-established structural biology tools have pro-
                                    vided high-resolution ‘snapshots’ of states in a crystallized or frozen form (e.g., X-ray crystallography
                                    and single-particle cryo-electron microscopy, cryoEM) or an ensemble average of all contributing
                                    conformations (e.g., nuclear magnetic resonance, NMR; small-angle X-ray scattering, SAXS; small-
                                    angle neutron scattering, SANS; double electron-electron resonance, DEER; cross-linking mass spec-
                                    trometry, XL-MS; ensemble-FRET). In recent years, further developments have enabled these con-
                                    ventional structural tools to detect conformational dynamics and reaction intermediates. For
                                    example, NMR techniques (Anthis and Clore, 2015; Clore and Iwahara, 2009; Palmer, 2004;
                                    Ravera et al., 2014; Sekhar and Kay, 2019) and electron paramagnetic resonance techniques
                                    (Jeschke, 2018; Jeschke, 2012; Krstić et al., 2011) have been advanced to study conformational
                                    dynamics and capture transient intermediates. Time-resolved crystallographic investigations have
                                    been employed to resolve functionally relevant structural displacements associated with a biological
                                    function (Kupitz et al., 2014; Moffat, 2001; Schlichting et al., 1990; Schlichting and Chu, 2000;
                                    Schotte et al., 2003). Advances in microfluidic mixing and spraying devices have enabled time-
                                    resolved cryoEM (Feng et al., 2017; Kaledhonkar et al., 2018) and cross-linking mass spectrometry
                                    (XL-MS or CL-MS) (Braitbard et al., 2019; Brodie et al., 2019; Chen et al., 2020; Iacobucci et al.,
                                    2019; Murakami et al., 2013; Slavin and Kalisman, 2018). Progress in computational methods has
                                    also afforded novel tools for examining biomolecular structure and dynamics. Each of these advan-
                                    ces highlights an increased awareness that one needs to directly and continuously track the dynam-
                                    ical properties of individual biomolecules in order to understand their function and regulation.
                                        In this context, FRET (referred to as fluorescence resonance energy transfer or Förster resonance
                                    energy transfer [Braslavsky et al., 2008]) studies at the ensemble and single-molecule levels have
                                    emerged as important tools for measuring structural dynamics over at least 12 orders of magnitude
                                    in time and mapping the conformational and functional heterogeneities of biomolecules under ambi-
                                    ent conditions. FRET studies probing fluorescence decays at the ensemble level (Grinvald et al.,
                                    1972; Haas et al., 1975; Haas and Steinberg, 1984; Hochstrasser et al., 1992) (time-resolved
                                    FRET) permitted already in the early 1970s the study of structural heterogeneities on timescales lon-
                                    ger than the fluorescence lifetime (a few ns). This approach is still used nowadays (Becker, 2019;
                                    Orevi et al., 2014; Peulen et al., 2017) and has been transferred to single-molecule studies. The
                                    ability to measure FRET in single molecules (Deniz et al., 1999; Ha et al., 1996; Lerner et al.,
                                    2018a) has made the method even more appealing. The single-molecule FRET (smFRET) approach
                                    has been extensively used to study conformational dynamics and biomolecular interactions under
                                    steady-state conditions (Dupuis et al., 2014; Larsen et al., 2019; Lerner et al., 2018a;
                                    Lipman et al., 2003; Margittai et al., 2003; Mazal and Haran, 2019; Michalet et al., 2006;
                                    Orevi et al., 2014; Ray et al., 2019; Sasmal et al., 2016; Schuler et al., 2005; Schuler et al., 2002;
                                    Steiner et al., 2008; Zhuang et al., 2000). It is notable that, in many mechanistic studies, it suffices
                                    to use FRET for distinguishing different conformations and determining kinetic rates such that abso-
                                    lute FRET efficiencies and thereby distances do not need to be determined. However, the ability to
                                    measure accurate distances and kinetics with smFRET has led to its emergence as an important tool
                                    in this new era of ‘dynamic structural biology’ for mapping biomolecular heterogeneities and for
                                    measuring structural dynamics over a wide range of timescales (Lerner et al., 2018a; Mazal and
                                    Haran, 2019; Sanabria et al., 2020; Schuler and Hofmann, 2013; Weiss, 1999).
                                        Single-molecule FRET (smFRET) approaches have many advantages as a structural biology
                                    method, including:
                                       .   sensitivity to macro-molecular distances (2.5–10 nm),
                                       .   the ability to resolve structural and dynamic heterogeneities,
                                       .   high-quality measurements with low sample consumption of the molecules of interest (low con-
                                           centrations and low volumes), as the sample is analyzed one molecule at a time,
                                       .   determination of structural transitions in equilibrium, hence without the need for
                                           synchronization,


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                             3 of 69



                                       .   the ability to detect (very) rare events. Indeed, in biology, the most interesting molecules to
                                           study are often the sparse, functionally active ones amidst a sea of inactive molecules,
                                       .   high sensitivity and specificity for labeled molecules. As only the labeled molecule uniquely
                                           contributes to the detected signal, these tracers can also be applied as FRET-reporters in
                                           crowded environments (Dupuis et al., 2014; Soranno et al., 2014; Zosel et al.,
                                           2020b) (hence smFRET can be used to validate results determined in isolation or detect the
                                           modulation of conformational preferences and/or structural dynamics through so-called qui-
                                           nary interactions [Guin and Gruebele, 2019]), and
                                       .   high specificity for residues/domains via specific labeling. Biomolecules can be specifically
                                           labeled by a unique dye pair enabling smFRET measurements to be applicable on all sizes of
                                           molecules, including large complex assemblies (see Figure 1 [Kilic et al., 2018]), active biolog-
                                           ical machines (e.g., the ribosomes) (Dunkle et al., 2011) and even on whole native virions
                                           (Lu et al., 2019; Munro et al., 2014).
                                       Several methods have been utilized to determine structural ensembles such as NMR, single-parti-
                                    cle cryoEM or XL-MS, and, recently, also smFRET in an integrative/hybrid (I/H) approach with compu-
                                    tational modeling to overcome the sparsity of experimental data with respect to an atomistic
                                    description (Berman et al., 2019; de Souza and Picotti, 2020; Dimura et al., 2020; Gauto et al.,
                                    2019; Koukos and Bonvin, 2020; Na and Paek, 2020; Tang and Gong, 2020; Webb et al., 2018).
                                    I/H structural models derived from smFRET experiments using inter-dye distances as restraints were
                                    reported for flexible folded proteins (Brunger et al., 2011; Hellenkamp et al., 2017;
                                    Margittai et al., 2003; McCann et al., 2012), conformational ensembles of disordered/unstructured
                                    and unfolded proteins (Borgia et al., 2018; Holmstrom et al., 2018; Schuler et al., 2020), nucleic
                                    acids and protein-nucleic acid complexes (Craggs et al., 2019; Craggs and Kapanidis, 2012;
                                    Kalinin et al., 2012; Lerner et al., 2018b; Muschielok et al., 2008; Wozniak et al., 2008).
                                       A further unique aspect of smFRET studies is that structural, kinetic, and spectroscopic informa-
                                    tion on large and complex systems can be recorded simultaneously in a single measurement. This
                                    facilitates linking dynamic and structural information in an integrative approach to
                                    (Figure 1A) (Hellenkamp et al., 2017; Kilic et al., 2018; Li et al., 2020b; Sanabria et al., 2020;
                                    Wasserman et al., 2016; Yanez Orozco et al., 2018):
                                       .   define the number of possible structures consistent with data,
                                       .   potentially reduce the ambiguity between different structural models compatible with the
                                           experimental data, and
                                       .   reveal the dynamic exchange pathways that are structurally allowed.
                                       As an example, Figure 1B shows the outcome of a multimodal smFRET study on the conforma-
                                    tional landscape of a 12-mer chromatin array (~2.5 MDa) (Kilic et al., 2018) with dynamics occurring
                                    on timescales from nanoseconds to hours. SmFRET experiments could detect the flexible chromatin
                                    conformations (Figure 1B, middle panel), revealing their dynamic structural heterogeneity
                                    (Figure 1B, bottom panel), in contrast to the well-ordered static structures of chromatin fibers
                                    (Figure 1B, top panel). These flexible, partially-open and open conformations that are quite abun-
                                    dant in solution (population of >70%; Figure 1B, bottom panel) were not resolved before, although
                                    they are essential for proper gene organization and function. They represent the central interconver-
                                    sion hub for the distinct stacking registers of chromatin and are difficult to detect with other struc-
                                    tural techniques. This approach of visualizing biomolecules in action under ambient conditions
                                    emphasizes the importance of their dynamic nature by resolving transitions between various confor-
                                    mational states, which, in many cases, promotes function (Aviram et al., 2018; Henzler-
                                    Wildman et al., 2007; Iljina et al., 2020; Lerner et al., 2018b; Sanabria et al., 2020; Tassis et al.,
                                    2020).
                                       SmFRET measurements are typically performed using two approaches: with surface-immobilized
                                    molecules using total internal reflection fluorescence microscopy (TIRFM) and camera-based detec-
                                    tion, or with freely diffusing molecules in solution using confocal microscopy and point detectors.
                                    Experimental systems are available commercially but are typically home-built. Samples are prepared
                                    and the data collected using lab-specific protocols, where data are stored in a variety of file formats
                                    and analyzed using an array of increasingly powerful software. For the field in general and for struc-
                                    tural studies in particular, it is important to demonstrate that smFRET, as a method, is reproducible
                                    and reliable regardless of where and how the sample is measured. To this end, in an effort led by
                                    Thorsten Hugel, twenty laboratories joined in measuring smFRET on several dsDNA constructs


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                             4 of 69


           Review Article                                            Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics


   A                 WƌŝŽƌŝŶĨŽƌŵĂƟŽŶ
                                                            B                   12-mer nucleosome array model
                                                                                                                            Prior: Structural models
                                                                                                                                                                Tetranucleosome structure

                                                                      N1                                                    N2                       N5                                                 N8
                                                                                                                                         TN1


             ^ƉĂĐĞŽĨƉŽƐƐŝďůĞƐŽůƵƟŽŶƐ                                         N3
                                                                                                                      N7
                                                                                                                           N4
                                                                                                                                         TN2
               ĨŽƌ&ZdĞǆƉĞƌŝŵĞŶƚƐ                                                  N5                                        D
                                                                                                                                A
                                                                            N10                                                 N9                   DA1
                                                                                                                                         TN3                                      DA3
                                                                     N12                                                          N11                N7               DA2                               N6


                                     Models                                                                     FRET experiments - TIRF + confocal
          Structural                                                                    Immobilized molecules                                                   Molecules in solution
                                       for

                                                                                    EFRET F(a.u.)
           Models                                                                                   1500                                                                                        B
                                    Dynamics                                                        1000
                                                                                                                                                                    0.8
                                                                                                                                                                                                {A,C}
                                                                                                      0.8                                                   EFRET   0.4

                                                                                                     0.4                                                                                         D
                                                                                                                                                                    0.0
                                                                                                            0   4     8      12      16     20                            0   2     4
                                                                                                                      Time (s)                                            ¢ D(A)²F (ns)


                                                                                                                    Dynamic structural ensemble
                         Reduction                                                                                                        Degree of compactness
                            of
                                                                                                     locked                unlocked              unstacked                half open               open
                         ambiguity


                                                                                 Register 1
                                                                                                                    >100                  (150±120               500±60
                                                                                                                     ms                      Ps)                   µs

                                                                                                                                                                                      2.6±0.5
                    Correct Model                                                                                                                                                        ms


                                                                     Stacking
                                                                                                        A1                          A2                     A3
                                                                                                                                                                              C

                                                                                                                                                                    (~3-4 ms)


                                                                                 Register 2
                                                                                                                    >100                  150±120
                                                                                                                     ms                     Ps


                                                                                                        B1                          B2                           D1
                                                                                                                                                                                                     Dn


Figure 1. Workflow of modeling dynamic structures from FRET measurements. (A) Integrative modeling requires structural and dynamic information.
Prior information from conventional approaches (X-ray, NMR, cryoEM) together with computational tools defines the space of possible solutions for
FRET-assisted structural modeling. The combination of structural (inter-dye distances) and dynamic information (kinetic connectivity and exchange rates)
enables identification of a consistent model. (B) Study of structure and dynamics of chromatin fibers. A combined TIRF and confocal FRET study of
structure and dynamics of chromatin fibers using three FRET labeling positions (DA1-3) for two pairs of dyes with distinct Förster distances. Förster
distances ( is defined in section Inter-dye distances, Equation 6). Prior structural information provided by cryo-electron microscopy (top, left)
(Song et al., 2014) and X-ray crystallography (top, right PDB ID: 1ZBB Schalch et al., 2005) is combined with the structural and dynamic information
obtained by FRET experiments on immobilized molecules measured by total internal reflection (TIRF) microscopy and on freely diffusing molecules by
confocal microscopy (Kilic et al., 2018). From the combined information, a consistent model is derived for chromatin fiber conformations with shifted
registers, which are connected by slow (>100 ms) and fast de-compaction processes (150 ms) that do not proceed directly, but rather through an open
fiber conformation. Figure 1B was reproduced from Figures 1, 3, and 6 in Kilic et al., 2018, Nature Communications with permission, published under
the Creative Commons Attribution 4.0 International Public License (CC BY 4.0; https://creativecommons.org/licenses/by/4.0/).
Ó 2018, Kilic et al. Panel B was reproduced from Figures 1, 3 and 6 in Kilic et al., 2018 , with permission, published under the Creative Commons
Attribution 4.0 International Public License.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                                                                           5 of 69



                                    (Hellenkamp et al., 2018a). Studying six distinct samples with different dyes and varying inter-dye
                                    distances, the mean FRET efficiencies obtained by the participating labs exhibited a surprisingly high
                                    degree of agreement (a DE between 0.02 and 0.05 depending on the details of the sample). The
                                    quantitative assessment and reproducibility of the intensity-based smFRET measurements and dis-
                                    cussions about data analysis was an important milestone. These dsDNA FRET standards are now
                                    available for every day calibration and are especially useful for new groups joining the community.
                                       Encouraged by the insights gained in the above-mentioned FRET endeavor (Hellenkamp et al.,
                                    2018a), new multi-lab blind studies have been initiated. The next comparative FRET study, led by
                                    Thorben Cordes, investigates the robustness and reliability of smFRET experiments on proteins
                                    undergoing ligand-induced conformational changes (Gebhardt et al., in preparation). This study uses
                                    two distinct model proteins to assess the reproducibility and accuracy of protein-based smFRET for
                                    inter-dye distance determination measurements. Protein systems bring new challenges, including
                                    statistical dye labeling, site-specific dye properties, protein stability, shipping, storage and confor-
                                    mational dynamics. Hence, the study also assesses the ability of smFRET to discover and quantify
                                    dynamics on different timescales from microseconds to seconds. Another FRET challenge, initiated
                                    by Sonja Schmid, is the kinSoftChallenge (http://www.kinsoftchallenge.com, Götz et al., in prepara-
                                    tion), which evaluates existing tools for extracting kinetic information from single-molecule time tra-
                                    jectories. This challenge aims to: (1) demonstrate the ability of smFRET-based kinetic analyses to
                                    accurately infer dynamic information and (2) provide the community with the means of evaluating
                                    the different available software tools.
                                       One important outcome of the various multi-lab FRET studies was that, although the agreement
                                    was good, it could be improved even further. In particular, the data analysis, and specifically correc-
                                    tions, can have an impact on the determined FRET efficiencies and resulting distances. Hence, an
                                    open discussion regarding which approaches work most reliably under what conditions is necessary.
                                    Access to the primary data and the ability to process them with various analysis approaches is, and
                                    will remain, the most transparent way to move the field forward. Currently, this is difficult given the
                                    many variations in methods employed, their documentation, file formats and experimental proce-
                                    dures implemented across laboratories establishing the optimal conditions, workflow and best prac-
                                    tices even for existing, well-tested methods is challenging since a comparison of these methods is
                                    time-consuming and the necessary information is, in many cases, not available. With the increase in
                                    open scientific practices and submission of published data to repositories, a consensus is needed
                                    regarding what data and metadata should be stored and in which possible formats so that it can be
                                    readily utilized by the community.
                                       Due to these considerations and the many opportunities for growth of the smFRET community,
                                    several laboratories with expertise in FRET, without pretension to be exhaustive or exclusive, have
                                    gathered to endorse these efforts and propose steps to organize the community around consistent
                                    and open-science practices. This action translates into general methodological recommendations or
                                    suggestions, which we introduce following the typical workflow of a smFRET experiment, including
                                    sample preparation and characterization, setup description, data acquisition and preservation, and
                                    data analysis. These recommendations on how to ‘practice’ smFRET are not an attempt to regiment
                                    the community but rather an initial suggestion that aims at encouraging an open dialog about exist-
                                    ing practices in our field and leads to higher reproducibility in the results from smFRET experiments.
                                    We then discuss open science practices as well as the first steps that have been taken to form an
                                    international FRET community. We end with highlighting a few of the areas where we see smFRET
                                    making a big impact in various scientific fields in the near future.


                                    State of the art of single-molecule FRET experiments
                                    Within the FRET community, considerable know-how and expertise exists for the design, measure-
                                    ment and analysis of FRET experiments. In this section of the paper, we:
                                       .   review the workflow of smFRET experiments,
                                       .   discuss practical problems and potential pitfalls,
                                       .   provide recommendations for good practice, and
                                       .   list key scientific challenges that the field faces.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                             6 of 69



                                       In the following, we consider each of these four aspects at every step of the smFRET workflow,
                                    from the choice of instrumentation all the way to the generation of structural and dynamic models.

                                    Experimental approaches: free diffusion or surface immobilization?
                                    The workflow of smFRET studies starts with choosing one of the two most popular smFRET imple-
                                    mentations: confocal and TIRF microscopy. Confocal microscopy is especially well-suited for studying
                                    freely diffusing molecules (Figure 2A), while TIRF microscopy is typically used for surface-immobi-
                                    lized molecules (Figure 2B; e.g., reviewed in Juette et al., 2014; Roy et al., 2008; Sasmal et al.,
                                    2016).
                                        Compared to most other single-molecule approaches, both smFRET modalities offer relatively
                                    high throughput.
                                       .   In the confocal modality, the free diffusion of molecules into the observation volume and the
                                           short residence times enable the acquisition of many single-molecule events for extended
                                           amounts of time at rates of a few events per second. It can offer sub-nanosecond time resolu-
                                           tion, yet single molecules are only observed during diffusion through the confocal excitation
                                           volume (typically <10 milliseconds). This allows one to obtain snapshots of thousands of indi-
                                           vidual molecules over the course of hours.
                                       .   In the TIRF modality, hundreds to thousands of dye-labeled molecules can be imaged simulta-
                                           neously in one field of view. This approach reveals ‘motion pictures’ of individual molecules
                                           from seconds to minutes until the fluorophores photobleach. It typically has a lower temporal
                                           resolution of about a few tens of milliseconds but this is improving with technological advan-
                                           ces. TIRF can be performed by illuminating through a high-numerical-aperture objective
                                           (Figure 2B) or through a quartz prism (Roy et al., 2008).
                                       When embarking on the investigation of conformational dynamics of a new biological system, the
                                    method of choice most often depends on the availability of the proper instrumentation. However,
                                    the dynamical aspects (reviewed in section Conformational dynamics) of the biological system under
                                    investigation, which are typically not known a priori, will eventually define which of the two methods
                                    is best suited. Because the dynamics of biological systems occur over a range of timescales from
                                    nanoseconds to seconds (Figure 3), ideally one would like to apply both modalities in parallel to
                                    obtain a complete understanding of the system (e.g., as shown in Figure 1).
                                       Many variations exist with respect to the above-mentioned basic modalities to:
                                       1) maximize the information content of the fluorescence signal.
                                       .   The confocal modality equipped with TCSPC and polarization-sensitive detections, so-called
                                           multiparameter fluorescence detection (MFD), allows monitoring of the fluorescence lifetime
                                           and anisotropy in addition to the fluorescence intensity (Kühnemuth and Seidel, 2001;
                                           Rothwell et al., 2003; Sisamakis et al., 2010; Widengren et al., 2006). The simultaneous col-
                                           lection and analysis of multiple parameters provides valuable insights into conformational
                                           dynamics, impurities and other spurious fluorophore-related artifacts.
                                       .   Alternating laser excitation (ALEX) (Kapanidis et al., 2004) allows for optical sorting of mole-
                                           cules exhibiting fluorescence from a single dye or from the two dyes in the FRET experiment
                                           (Figure 2A-iv) and also extract information on dye photophysics. In the TIRF modality, millisec-
                                           ond ALEX (msALEX) (Margeat et al., 2006) is typically used; in the confocal modality micro-
                                           second ALEX (msALEX) (Kapanidis et al., 2005; Kapanidis et al., 2004; Lee et al., 2005) or
                                           nanosecond ALEX (nsALEX), aka. pulsed interleaved excitation (PIE) (Kudryavtsev et al.,
                                           2012; Laurence et al., 2005; Müller et al., 2005) are used.
                                       .   Three or more spectral channels can be used for multi-color smFRET (Clamme and Deniz,
                                           2005; Hohng et al., 2004; Lee et al., 2010c; Lee et al., 2007a; Ratzke et al., 2014;
                                           Stein et al., 2011).
                                       2) optimize data collection.
                                       .   A confocal microscope equipped with a laser and a sample or laser scanning module is also
                                           suited to study immobilized molecules (Chung et al., 2012; Edman et al., 1999; Ha et al.,
                                           1999; Ha et al., 1997; Hanson et al., 2007; Rhoades et al., 2003; Sabanayagam et al.,
                                           2004; Sturzenegger et al., 2018; Uphoff et al., 2011; Wang and Lu, 2010). It is the ‘best of
                                           both worlds’ in terms of timing, that is high time resolution and long observation times. How-
                                           ever, it requires localizing and measuring each molecule individually, leading to lower
                                           throughput.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                             7 of 69


            Review Article                                                            Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics


   A-i                                                         A-ii            Confocal volume                                                           A-iv

                                                                                                                                              A
                     Sample                                           A                                                          D
                                                                                         A
                                                                                  D
                                                                  D
                  Objective

    D Laser
                                                                                      1-10 ms
                                       DM

                            TL                                                   Freely diffusing
                                                             DM            L

                             M
                                                    L                                                                                         A-iii        Single-molecule bursts
                                      Pinhole                         EF                                                             30


                                                                                                                   Countrate (kHz)
                                                        L                                                                                                            DD
                                                                                                                                                                     DA
       DM: dichroic mirror                                                                                                           20
                                                                                                                                              FRET                                         D-only
       TL: tube lens                                                  Point detectors
       L: lens
       M: mirror
       EF: emission filter
                                                                                                                                          0                0.5             1         1.5            2

                                                                                                                                                                          Time (s)

   B-i                       Surface-immobilized                                         B-iii
                                                                                                                                     Donor channel Acceptor channel


             100-200 nm
                                                                                                                                                        No FRET
                                                                                                                                                       No FRET
                                        A       Fluorophores                                                                                         No FRET A-only
                                                                                                                                                      No FRET
                                                                                                                                                    No FRET
                             Biotin                                                                                                                No FRET
                                            D                                                                                                     D-only          FRET
                                                            Streptavidin                                                                                         FRET
                                                                                                                                                                FRET


          Evanescent wave
                                                                                                                                                               FRET
                                                                                                                                                              FRET
                                                                                                                                                        FRET FRET
                                                            PEG                                                                                        FRET FRET
                                                                                                                                                     FRET
                                                                                                                                                    FRET
                                                                                                                                                   FRET
                                                            Coverslip                                                                             FRET

                     Critical angle


                                                                                                                              DexDem                      DexAem                   # frames
                                                                                                                                                                               ~10-100 ms/frame


   B-ii                                                                                  B-iv
                                                                       Camera                                                                                     Time trace


                                                                                                Intensity [a.u.]
                                        Objective                                                                      300
      D Laser L                                                            L                                           200
                                       DM
                                                     EF                                                                100
                                       TL                                 EF
                                                                                                                           0                       10        20      30      40      50        60
                                 M                                    M
                                                                                                                                                                    Time [s]
                                        A        L          DM


Figure 2. Different smFRET modalities. (A) Confocal smFRET measurements on freely-diffusing molecules. (i) A schematic of a single-color excitation
confocal microscope with point detectors used for two-color detection. The excitation light is guided to the microscope body and reflected by a
dichroic mirror (DM) toward a high numerical aperture (NA) objective lens that focuses the light in solution. The fluorescence emission is collected
through the same objective lens, passes through the DM and pinhole and is spectrally split into donor and acceptor detection channels by a second
Figure 2 continued on next page


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                                                                           8 of 69


           Review Article                                              Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics

Figure 2 continued
DM in the detection path. After passing through emission filters (EF), single photons are detected on point detectors with high quantum efficiency,
typically avalanche photodiodes (APD). (ii) Illustration of a double-labeled molecule freely diffusing through the confocal excitation spot. (iii) Exemplary
confocal smFRET measurement showing photon bursts arising from single-molecules diffusing through the confocal volume. Green: Donor emission.
Red: Acceptor emission. Exemplary bursts belonging to a single- or a double-labeled molecule are indicated with arrows. (iv) In ALEX or PIE
experiments, the two-dimensional histogram of the molecule-wise FRET efficiency E and stoichiometry S allows one to separate single- and double-
labeled populations (2005 Elsevier Ltd. All rights reserved. The figure was originally published as Figure 2A in Lee et al., 2005. Biophysical Journal, 88
(4): 2939–2953. Further reproduction of this panel would need permission from the copyright holder). (B) TIRF-based smFRET experiments on surface-
immobilized molecules. (i) Illustration of a surface-immobilized sample labeled with donor and acceptor fluorophores. (ii) Scheme of a single-color
objective-type TIRF excitation two-color wide-field detection microscope. A: Aperture, TL: Tube lens, L: Lens, M: Mirror, DM: Dichroic mirror, EF:
Emission filter. (iii) Illustration of an image of single molecules, in which the donor and acceptor (FRET) signals are split onto two halves of the camera.
Mapping between the two channels is typically done using fluorescent beads (Joo and Ha, 2012; Roy et al., 2008; Zhuang et al., 2000) or zero-mode
waveguides (Salem et al., 2019). (iv) Single-molecule fluorescence trajectory of the donor and acceptor (FRET) dyes, illustrating an anti-correlation
indicative of FRET dynamics.
Ó 2005, Elsevier. All rights reserved. Panel Aiv was originally published as Figure 2A in Lee et al., 2005. Further reproduction of this panel would need
permission from the copyright holder.


                                         .   Multi-spot detection, on arrays of single-photon avalanche diode detectors (SPAD arrays) and
                                             other state-of-the-art detectors, increases the throughput of confocal-based smFRET measure-
                                             ments and enables the study of non-equilibrium kinetics with higher time resolution
                                             (Ingargiola et al., 2016b; Ingargiola et al., 2018a; Segal et al., 2019).
                                         .   Objective-type TIRF can be combined with micro-mirrors in the excitation path to reduce back-
                                             ground (Larson et al., 2014).
                                         .   Novel large-chip sCMOS cameras allow imaging at higher frame rates than their EMCCD coun-
                                             terparts. With the larger chip size, it can detect tens of thousands of molecules simultaneously
                                             (Juette et al., 2016) and the time resolution can be pushed into the sub-millisecond time scale
                                             (Fitzgerald et al., 2019; Girodat et al., 2020; Pati et al., 2020).
                                         3) control the sample.
                                         .   In the confocal modality, the upper limit of the observation time can be pushed by recurrence
                                             analysis (Hoffmann et al., 2011) or by conjugating the molecules to large slowly-diffusing par-
                                             ticles or liposomes (Diez et al., 2004; Kim et al., 2015a). Alternatively, the Moerner group
                                             confined molecules of interest to the observation volume without immobilization by using an
                                             anti-Brownian electrokinetic (ABEL) trap (Cohen and Moerner, 2005; Wilson and Wang,
                                             2019).
                                         .   The space available for diffusion can be confined by using nanochannel devices
                                             (Fontana et al., 2019; Tyagi et al., 2014) or limiting the sectioning of the excited region
                                             through highly inclined and laminated optical (HILO) excitation (Gilboa et al., 2019) so that
                                             freely diffusing molecules can be tracked with camera detection.
                                         .   Microfluidics-based sample handling devices, including various mixers (Gambin et al., 2011;
                                             Hellenkamp et al., 2018b; Kim et al., 2011; Lemke et al., 2009; Lipman et al., 2003;
                                             Wunderlich et al., 2013; Zijlstra et al., 2017), allow automated sample handling and enable
                                             non-equilibrium measurements (Hamadani and Weiss, 2008; Juette et al., 2016).
                                          The many possibilities available in the choice of hardware underscore the importance of precisely
                                      describing the components of the experimental setup. This includes optical elements (e.g., lenses,
                                      filters, mirrors, dichroics), light sources, optomechanical/optoelectronic devices and their characteris-
                                      tics, and detectors and their associated electronics. These details contribute in many ways to the
                                      finally recorded data and cannot, in general, be inferred retrospectively.
                                          With the palette of FRET modalities increasing steadily, we recommend a rigorous comparative
                                      study of the different methods using well-characterized model samples. First and foremost, the study
                                      should determine the precision and limitations of each method and their complementarity. As one
                                      example, potential pitfalls in the determination of data correction factors (described in the section
                                      FRET efficiency) could be identified by a side-by-side comparison of fluorescence lifetime and inten-
                                      sity-based FRET methods.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                        9 of 69


              Review Article                                                      Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics


                                      AE$%&',D&$#%@3                       *"+,%&-./%&,%&-
                                                                                                                      ;+%-"#6(%<$)%"&            8--(6-$)%"&
                                      !"#$%&'(")$)%"&   !" #$%&'$&%(                             )" #$%&'$&%(


                &'!&'                &'!"                &'!#                           &'!$                          &'%                 &'$                  !"#$ %&'
                                                                                                                A$#6($1B$36,
    (##)*"+",$-
                                                                                                    9:A1B$36,

                                                        A"((6+$)%"& 9C6@)("3@"CD

       ./$$0                   4%56)%#6                                          0'1 2%3)"-($#             789:                         =$&>$+ =%?%&-
     1"223&")4                                                                                           =%@("5+>%,%@3


               !                               "                                   #                              $                            %


     *""                                                    ()*+*%&,-,.&
     *!!
     *!"
       !"##     # "##
              !! $%&'


Figure 3. Exemplary methods for following smFRET dynamics on different timescales. Top: Biomolecular dynamics cover a wide range of timescales.
Biomolecular rotations occur in the pico- to nanosecond range, while conformational changes take place in nano- to microseconds (ns-ms), as in chain
dynamics of disordered proteins, and protein folding in microseconds to minutes. Transitions along energetically unfavorable pathways can take up to
hours or longer, as in protein misfolding (Borgia et al., 2011; Tosatto et al., 2015). (2013 Elsevier Ltd. All rights reserved. The figure was originally
published as Figure 1 in Schuler and Hofmann, 2013. Current Opinion in Structural Biology, 23(1): 36–47. Further reproduction of this panel would
need permission from the copyright holder.) Bottom: (A) Picosecond (ps) to millisecond (ms) processes are typically examined with confocal methods
such as polarization-resolved fluorescence lifetime measurements and Fluorescence Correlation Spectroscopy (FCS). Example shown: chain dynamics of
an IDP from nsFCS. (B) Conformational states are identified by individual populations with characteristic positions in the FRET efficiency - lifetime
diagrams as discussed in the sections Detection and characterization of intra-state dynamics and Future of smFRET (adapted from Soranno et al.,
2012). (C) Fast transitions measured using confocal microscopy can be analyzed using the photon trajectory and applying a photon-by-photon
maximum likelihood approach (2018 Elsevier Ltd. All rights reserved. The figure was originally published as Figures 2 and 3 in Chung and Eaton, 2018.
Current Opinion in Structural Biology, 48: 30–39. Further adaptation of this panel would need permission from the copyright holder.) The timescale over
which kinetics can be measured can be extended for diffusing molecules at low concentrations by using a recurrence analysis of single particles (RASP,
Hoffmann et al., 2011). (D) Non-equilibrium experiments over extended periods of time can be performed with microfluidic mixing devices.
(Copyright 2011, Nature Publishing Group, a division of Macmillan Publishers Limited. All Rights Reserved. Reproduced from Gambin et al., 2011, with
permission. Nature Methods 8:239–241. Further reproduction of this panel would need permission from the copyright holder.) (E) Slow changes in
conformations over a broad range of timescales can be followed in smFRET efficiency trajectories registered by single-photon counting (SPC) or
cameras over minutes to many hours when the sample is immobilized (adapted from Figure 1 of Zosel et al., 2018).
Ó 2013, Elsevier Ltd. All rights reserved. Figure 3 (top) and panel A was originally published as Figure 1 in Schuler and Hofmann, 2013. Further
reproduction of this panel would need permission from the copyright holder.
Ó 2018, Elsevier Ltd. All rights reserved. Panel C was originally published as Figures 2 and 3 in Chung and Eaton, 2018. Further adaptation of this
panel would need permission from the copyright holder.
Ó 2011, Nature Publishing Group, a division of Macmillan Publishers Limited. All Rights Reserved. Panel D was originally published as Figure 1f in
Gambin et al., 2011. Further reproduction of this panel would need permission from the copyright holder.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                                        10 of 69



                                    Sample preparation
                                    Dyes
                                    For studying biomolecular conformations and their dynamics with smFRET, the biomolecules of inter-
                                    est must be labeled with organic dyes that are suitable for single-molecule fluorescence detection
                                    (intrinsically fluorescent aromatic amino acids are not stable or bright enough). These dyes usually
                                    include three modules: (i) a chemically reactive group that forms a covalent bond preferentially with
                                    a specific nucleic acid base or amino acid residue of choice, (ii) a sufficiently long linker of a few con-
                                    necting bonds to ensure isotropic rotation of the fluorophore, and (iii) an (often bulky) p-conjugated
                                    fluorophore that typically has hydrophobic regions and charged or polar substitutions.
                                        To compete with background-noise, smFRET-compatible dyes should be very bright. They should
                                    hence possess a sufficiently large extinction coefficient (>50,000 M 1cm 1 at the wavelength of exci-
                                    tation) and high fluorescence quantum yield (fF ~  > 0.3), be very photostable ( ~  > 106 excitation cycles
                                    before photobleaching), exhibit low photoblinking, should not possess long-lived dark states to
                                    avoid optical saturation and have a large fundamental anisotropy, that is have approximately collin-
                                    ear absorption and emission transition dipole moments (typically, r0 ~  > 0.37). The fluorescence lifetime
                                    should be on the 1-5 ns scale. In the case of TCSPC experiments, a general rule of thumb is that the
                                    laser repetition period should be chosen at least four times as large as the fluorescence lifetime. For
                                    instance, for a dye with a fluorescence lifetime of 4 ns, a laser pulse repetition rate of ~64 MHz for
                                    one-color excitation or ~32 MHz for two-color nsALEX/PIE experiments should be used. In addition,
                                    using dyes with intrinsic mono-exponential fluorescence decays simplifies the analysis. Continuous
                                    efforts are ongoing to further improve smFRET dyes by:
                                       .   structural modifications of the core dye structure (Matikonda et al., 2020b): rhodamines and
                                           silicon rhodamines, carbopyronines, oxazines; cyanines (Matikonda et al., 2020a;
                                           Michie et al., 2017), carbocyanines; BODIPY dyes, perylenes or others, aiming to produce
                                           higher absorption cross-sections and fluorescence quantum yields (Grimm et al., 2017;
                                           Grimm et al., 2015), good chemical stabilities, water solubility (e.g., sulfonated carbocyanines)
                                           (Mujumdar et al., 1993) and a decoupling between the photophysical properties and the
                                           microenvironment (Hell et al., 2015; Levitus and Ranjit, 2011; Michie et al., 2017),
                                       .   ‘self-healing’ dyes, where the fluorophore is directly linked to a photostabilizing moiety to
                                           achieve high photon counting rates (Altman et al., 2012; Isselstein et al., 2020; Bodo et al.,
                                           1981; Pati et al., 2020; Schafer et al., 1982; van der Velde et al., 2013; Zheng et al., 2014),
                                       .   switchable, caged, and photoactivatable dyes for measuring multiple donor-acceptor distances
                                           (Jazi et al., 2017; Uphoff et al., 2010),
                                       .   using multiple acceptors, which can extend the overall duration of the fluorescence signal and/
                                           or the distance-range for FRET measurements (Krainer et al., 2015), and
                                       .   developing inorganic probes that are brighter or have long fluorescence lifetimes, such as
                                           nanoparticles and lanthanides, which have also been applied for FRET studies (Clegg, 1995;
                                           Guo et al., 2019; Léger et al., 2020).
                                       Finally, a pair of FRET dyes should always be chosen such that its Förster distance, R0 , (defined in
                                    section Inter-dye distances, Equation 6) is around the expected inter-probe distance, RDA , where the
                                    dependence of the FRET efficiency, E, is most sensitive to RDA . When quantifying conformational
                                    dynamics, the FRET dye pair should be chosen such that the expected change in FRET efficiency is
                                    as large as possible.

                                    Conjugation
                                    To measure intra-molecular distances within biomolecules, smFRET experiments require the conjuga-
                                    tion of two dye molecules to the same biomolecule or the same biomolecular complex. Site-specific
                                    conjugations in proteins utilize the introduction of point mutations, typically to cysteines, that will
                                    accommodate the specific conjugation chemistry, usually maleimide- or iodoacetamide-cysteine
                                    chemistry. In this case, two cysteines are often stochastically labeled, leading to a mixture of donor-
                                    acceptor and acceptor-donor labeled molecules. While interchanging the donor and acceptor posi-
                                    tions has a negligible effect, from the geometric standpoint, on the FRET-averaged distance
                                    (Peulen et al., 2017), stochastic labeling might cause problems when the donor/acceptor dyes pos-
                                    sess different spectroscopic properties at the different labeling positions.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            11 of 69



                                       Potential issues related to stochastic labeling can be excluded when, for example, a multi-dimen-
                                    sional analysis available from MFD-PIE shows no dye-induced sub-populations. Alternatively, sto-
                                    chastic labeling can also be avoided by:
                                       .   exploiting the differences in thiolate reactivities when carrying out double cysteine labeling
                                           (Hohlbein et al., 2013; Jacob et al., 2005; Orevi et al., 2014; Santoso et al., 2010a), or
                                           blocking the accessibility of specific cysteines (Jäger et al., 2005),
                                       .   combining cysteine labeling with bio-orthogonal labeling approaches such as unnatural amino
                                           acids (Chakraborty et al., 2012; Milles et al., 2012; Quast et al., 2019; Sadoine et al., 2017;
                                           Sanabria et al., 2020), native chemical ligation (Deniz et al., 2000), or using other bio-conju-
                                           gation approaches that are specific and selective to other amino acids, for instance, methio-
                                           nine (Kim et al., 2020),
                                       .   purifying specific dye-labeled species via analytical chromatography (Lerner et al., 2013;
                                           Orevi et al., 2014; Zosel et al., 2020a),
                                       .   using different dyes that can be introduced to the same system using DNA hybridization
                                           (Auer et al., 2017; Deußner-Helfmann et al., 2018; Filius et al., 2020),
                                       .   the aid of self-labeling enzymes or peptide tags, such as SNAP-tag (Olofsson et al., 2014),
                                           HaloTag (Okamoto et al., 2020), ACP-tag (Meyer et al., 2006a; Meyer et al., 2006b;
                                           Munro et al., 2014; Wang et al., 2012), or the enzymes sortase (Kim and Chung, 2020) and
                                           transglutaminase (Jäger et al., 2006), and
                                       .   the use of fluorescent proteins (Düser et al., 2008; Okamoto et al., 2020), which have also
                                           been applied in smFRET studies.
                                        Different approaches are applied for nucleic acids (e.g., reviewed in Hanspach et al., 2019;
                                    Steffen et al., 2019). For short nucleic acids, site-specific conjugation is generally achieved by post-
                                    synthetic labeling of reactive groups (e.g., through click chemistry) that are incorporated during
                                    solid-phase synthesis. Strategies have also been developed to site-specifically label longer RNAs
                                    (Anhäuser and Rentmeister, 2017; Baum and Silverman, 2007; Büttner et al., 2014; Zhao et al.,
                                    2018), and the use of hybridizing probes (Steiner et al., 2008) and fluorescent nucleobase ana-
                                    logues as intrinsic probes (Karimi et al., 2020; Steinmetzger et al., 2020) has been explored.
                                        A general recommendation for labeling is to aim for high-purity sample preparations with opti-
                                    mized labeling protocols, as only this will result in substantially and specifically labeled samples with
                                    both donor and acceptor dyes. Single-molecule measurements have the ability to separate out the
                                    donor-acceptor-labeled molecules and thus purify the sample ex post facto, but a significant amount
                                    of double-labeled samples is advantageous. After labeling, we recommend using a rigorous screen-
                                    ing procedure that compares the activities of labeled and unlabeled wild-type biomolecules to
                                    determine whether the mutations introduced to a biomolecule and/or the labeling with the dyes sig-
                                    nificantly influence the biomolecule’s functionality (e.g., catalytic activity, binding affinity) and stabil-
                                    ity (e.g., against denaturants or thermally-induced transition curves) (Best et al., 2018; Deniz et al.,
                                    2000; Lerner et al., 2018b; Orevi et al., 2014; Riback et al., 2019; Sottini et al., 2020). To check
                                    for structural integrity, methods such as mass spectrometry, circular dichroism (CD), dynamic light
                                    scattering (DLS), and small-angle X-ray scattering (SAXS) can be used (Best et al., 2018;
                                    Borgia et al., 2016; Riback et al., 2019). We also recommend reporting the labeling and purifica-
                                    tion procedures as well as the labeling efficiency. In cases where no labeling alternative exists that
                                    does not modify the structure and/or rate of function, mechanistic insights into biomolecules or com-
                                    plexes can often still be obtained. Nevertheless, the results and conclusions concerning wild-type
                                    and unlabeled protein, respectively, should be interpreted cautiously. Finally, when samples need to
                                    be frozen/thawed, we recommend testing the long-term stability and functionality versus fresh pro-
                                    tein preparations.

                                    Immobilization
                                    For long observation times, labeled molecules are typically immobilized. This is most frequently
                                    achieved via a biotin-streptavidin linkage. Immobilization must be carefully performed in order to
                                    systematically eliminate spurious contributions from molecules that are non-specifically bound
                                    (Lamichhane et al., 2010; Traeger and Schwartz, 2017). To address this potential issue, efforts
                                    have been made to optimize surface passivation procedures (Hua et al., 2014; Kuzmenkina et al.,
                                    2005; Park et al., 2020; Selvin and Ha, 2008). Alternatives that avoid the direct linking
                                    of biomolecules to surfaces are:


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            12 of 69




                                       .   mimicking a native environment by reconstitution of membrane proteins in nanodiscs
                                           (Bavishi et al., 2018; Hartmann et al., 2015) or liposomes (Diez et al., 2004),
                                       .   encapsulating biomolecules in spatially-restricted volumes such as liposomes (Boukobza et al.,
                                           2001; Cisse et al., 2007; Fitzgerald et al., 2019; Okumus et al., 2004; Rhoades et al., 2003;
                                           Zelger-Paulus et al., 2020). Care should be taken since the fraction of functioning proteins
                                           can be reduced due to the encapsulation process itself. Also, interactions between the protein
                                           and/or dyes and the lipids can pose a problem, and
                                       .   precise positioning of biomolecular assemblies on DNA-origami platforms (Bartnik et al.,
                                           2020; Gietl et al., 2012).
                                       We recommend reporting the immobilization conditions, the control experiments that demon-
                                    strate the specific nature of the surface immobilization strategy, and the percentage of functional or
                                    dynamic molecules (Bavishi and Hatzakis, 2014; Lamichhane et al., 2010; Roy et al., 2008) in
                                    detail. Finally, when possible, we recommend cross-validating the results of surface-immobilization
                                    based smFRET experiments by comparing them either to those obtained in ensemble or single-mol-
                                    ecule FRET experiments on non-immobilized, freely-diffusing molecules (Pirchi et al., 2011), or to
                                    results using different immobilization strategies (Gregorio et al., 2017; Whitford et al., 2010).

                                    Spectroscopic characterization
                                    Fluorescent dyes are characterized by particular spectroscopic properties, which may change when
                                    conjugated to a protein (Lerner et al., 2013; Peulen et al., 2017; Sindbert et al., 2011;
                                    Steffen et al., 2016) or even between different structural states of the labeled biomolecule
                                    (Kudryavtsev et al., 2012). The most important artifacts to look out for are:
                                       .   photoblinking, photobleaching, changes of fluorescence anisotropies or the molecular bright-
                                           ness, and spectral shifts can create artifactual FRET-species when not properly identified and
                                           corrected for or removed (Chung et al., 2009; Kong et al., 2007; Sindbert et al., 2011;
                                           van der Velde et al., 2016). Protein-induced fluorescence enhancement (PIFE) (Hwang et al.,
                                           2011; Hwang and Myong, 2014) has to be taken into account for the donor properties and
                                           at the same time can serve as a molecular ruler at molecular distances inaccessible to other
                                           spectroscopic rulers in addition to FRET (Lerner et al., 2016; Ploetz et al., 2016),
                                       .   optical saturation effects that reduce the overall observed dye brightness (Gregor et al.,
                                           2005; Nettels et al., 2015). Acceptors that have a strong tendency for triplet-state formation
                                           or photoisomerization are particularly susceptible to optical saturation,
                                       .   dye-dye interactions that may lead to artificial high-FRET states (Sánchez-Rico et al., 2017) or
                                           to quenchable FRET (Cordes et al., 2010), and
                                       .   interactions between the dye and the labeled molecule can lead to dye-stacking in a prede-
                                           fined orientation that modulates the orientational factor, k2 (e.g., Cy3 base stacking to 5’-end
                                           of DNA [Liu and Lilley, 2017; Ouellet et al., 2011; Sanborn et al., 2007]), or they can lead to
                                           quenching and shifts in the apparent transfer efficiency, for example, via photoinduced elec-
                                           tron transfer (PET) to aromatic groups (Doose et al., 2009; Haenni et al., 2013).
                                        When the local and/or global environment influences the photophysical properties of either the
                                    donor or the acceptor dyes differently, different subpopulations might appear (Kalinin et al., 2010a;
                                    Vandenberk et al., 2018). Depending on the research question at hand, these subpopulations per
                                    se may provide additional information beyond FRET (e.g., PIFE [Ploetz et al., 2016], PET
                                    [Doose et al., 2009], or quenchable FRET [Cordes et al., 2010]). In cases where accurate distance
                                    measurements are needed, properly designed control experiments of fluorescence lifetimes and ani-
                                    sotropies of single-label versions for both labeling positions and dyes can be used to detect and
                                    eventually correct these spectroscopic alterations a posteriori. In addition, dye-artifacts can be iden-
                                    tified from the information provided by ALEX or PIE experiments (Kapanidis et al., 2004;
                                    Kudryavtsev et al., 2012), MFD-based detection (Hellenkamp et al., 2017; Rothwell et al., 2003)
                                    or analysis of the width of FRET efficiency distributions (Kalinin et al., 2010a; Nir et al., 2006). Note
                                    that the influence of dye photoblinking must be taken into account: (1) when determining the correc-
                                    tion factors necessary for precise FRET efficiency measurements (see section Determining absolute
                                    FRET efficiencies from fluorescence intensities) or (2) in the donor fluorescence quantum yield, when
                                    accurate distance estimations are required, which, in turn, depends on a correct Förster distance, R0
                                    (defined in section Inter-dye distances, Equation 6).


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            13 of 69



                                       When dye- and microenvironment- dependent influences exist, they can be characterized or
                                    taken into account by a careful choice of fluorophores and/or labeling locations or coarse-grained
                                    computer simulations (Peulen et al., 2017), or they can be ruled out completely by validating the
                                    observations with (an)other FRET pair(s) (Borgia et al., 2018; Borgia et al., 2016; de Boer et al.,
                                    2019b; Husada et al., 2018; Lerner et al., 2017; Vandenberk et al., 2018; Voelz et al., 2012) or
                                    switching fluorophore positions (Sanabria et al., 2020). How important a detailed spectroscopic
                                    analysis is, depends on the nature of the research question being addressed.

                                    Photostabilization
                                    Often, chemical photostabilizers are added to reduce oxidative photodamage by lowering the time
                                    spent in triplet or radical-ion dark states (Ha and Tinnefeld, 2012; Widengren et al., 2007). The
                                    choice of the photostabilizing agent is specific to the fluorophore used and finding the correct con-
                                    ditions for both the donor and acceptor fluorophores can be challenging. Commonly used photosta-
                                    bilizers for smFRET include 6-hydroxy-2,5,7,8-tetramethylchroman-2-carboxylic acid (Trolox)
                                    (Cordes et al., 2009; Dave et al., 2009; Rasnik et al., 2006; Vandenberk et al., 2018), n-propylgal-
                                    late (Widengren et al., 2007), b-mercaptoethanol (Campos et al., 2011; Ha and Tinnefeld, 2012),
                                    ascorbic acid (Aitken et al., 2008; Gidi et al., 2020; Vogelsang et al., 2008; Widengren et al.,
                                    2007), linear polyenes (Pfiffi et al., 2010) and cyclopolyenes (Dave et al., 2009; Targowski et al.,
                                    1987; Widengren et al., 2007), methylviologen (Vogelsang et al., 2008) and a range of other com-
                                    pounds (Glembockyte et al., 2015; Isselstein et al., 2020). For optimal performance, reducing and
                                    oxidizing agents can be combined (Dave et al., 2009; Vogelsang et al., 2008). Fluorophore perfor-
                                    mance and photon budgets can be enhanced by removing oxygen from the buffer through oxygen
                                    scavenging systems such as glucose oxidase (Kim et al., 2002) or the PCA/PCD system
                                    (Aitken et al., 2008), in which case an exogenous triplet quencher, such as those mentioned above,
                                    is required to prevent long-lived dark states. In any case, we recommend verifying that the use of
                                    these photostabilization reagents does not interfere with the biological system under study. In the
                                    case of lipid bilayers, an influence of several of the commonly used photostabilization agents on
                                    membrane properties was observed (Alejo et al., 2013).

                                    Molecule identification and validation
                                    After data collection in either confocal or TIRF modalities, the single-molecule fluorescent signal in
                                    the resulting time traces or videos must be identified and validated before further detailed analysis
                                    can be performed.

                                    Identification
                                    In the confocal modality, the raw ‘burst’ data includes a sequence of photon detection or arrival
                                    times from at least two detectors. The first step is to identify fluorescence bursts arising from single
                                    molecules from the background, commonly referred to as the ‘burst search’ (Figure 2A–iii). Various
                                    approaches have been described for the robust and accurate detection of single-molecule events
                                    (Enderlein et al., 1997; Fries et al., 1998; Nir et al., 2006; Schaffer et al., 1999; Sisamakis et al.,
                                    2010). After the burst search step, the identified single-molecule events are filtered based on the
                                    burst properties (e.g., burst size, duration or width, brightness, burst separation times, average fluo-
                                    rescence lifetime or quantities calculated from these burst parameters). The burst search and burst
                                    selection criteria have an impact on the resulting smFRET histograms. Hence, we recommend that
                                    the applied burst property thresholds and algorithms should be reported in detail when publishing
                                    the results, for example, in the methods section of papers but potentially also in analysis code repos-
                                    itories. Often, burst search parameters are chosen arbitrarily based on rules-of-thumb, standard lab
                                    practices or personal experience. However, the optimal burst search and parameters vary based on
                                    the experimental setup, dye choice and biomolecule of interest. For example, the detection thresh-
                                    old and applied sliding (smoothing) windows should be adapted based on the brightness of the fluo-
                                    rophores, the magnitude of the non-fluorescence background and diffusion time. We recommend
                                    establishing procedures to determine the optimal burst search and filtering/selection parameters.
                                       In the TIRF modality, molecule identification and data extraction can be performed using various
                                    protocols (Börner et al., 2016; Holden et al., 2010; Juette et al., 2016; Preus et al., 2016). In
                                    brief, the molecules first need to be localized (often using spatial and temporal filtering to improve


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            14 of 69



                                    molecule identification) and then the fluorescence intensities of the donor and acceptor molecules
                                    extracted from the movie. The local background needs to be determined and then subtracted from
                                    the fluorescence intensities. Mapping is performed to identify the same molecule in the donor and
                                    acceptor detection channels. This procedure uses a reference measurement of fluorescent beads or
                                    zero-mode waveguides (Salem et al., 2019) or is done directly on samples where single molecules
                                    are spatially well separated. The outcome is a time series of donor and acceptor fluorescence inten-
                                    sities stored in a file that can be further visualized and processed using custom scripts. In a next
                                    step, filtering is generally performed to select molecules that exhibit only a single-step photobleach-
                                    ing event, that have an acceptor signal when the acceptor fluorophores are directly excited by a sec-
                                    ond laser, or that meet certain signal-to-noise ratio values. However, potential bias induced by such
                                    selection should be considered.

                                    User bias
                                    Despite the ability to manually determine burst search and selection criteria, molecule sorting algo-
                                    rithms in the confocal modality, such as those based on ALEX/PIE (Kapanidis et al., 2005;
                                    Kudryavtsev et al., 2012; Tomov et al., 2012), do not suffer from a substantial user bias. In the
                                    early days, many TIRF modality users have relied on visual inspection of individual single-molecule
                                    traces. Such user bias was considerably reduced by the use of hard selection criteria, such as inten-
                                    sity-based thresholds and single-step photobleaching, intensity-based automatic sorting algorithms
                                    (e.g., as implemented in the programs MASH-FRET [Hadzic et al., 2019], iSMS [Preus et al., 2015]
                                    or SPARTAN [Juette et al., 2016]), and, most recently, artificial intelligence-based molecular sorting
                                    (deepFRET [Thomsen et al., 2020] and AutoSiM [Li et al., 2020a]).
                                         Single-molecule experiments are often advertised as being able to detect rare events. Nonethe-
                                    less, even for such sparsely populated states, it has to be confirmed that they are biologically rele-
                                    vant and neither a result of the selection procedure, coincidence or photophysical artifacts. To this
                                    end, users should specify how selections were performed and what percentage of the molecules was
                                    used for further analysis.
                                         Ideally, a recommended protocol with implicit validation would be to start in the confocal modal-
                                    ity to determine (i) the degree of labeling, (ii) the FRET properties of major biochemical species, and
                                    (iii) their populations and dynamic properties (see Figure 1). With this information at hand, experi-
                                    ments can be performed in the TIRF modality, where the percentage of FRET-active molecules and
                                    their FRET properties can be directly compared with the confocal data. Both datasets should be
                                    mutually consistent and, in this way, provide direct feedback with respect to potential artifacts (e.g.,
                                    due to immobilization).

                                    Conformational dynamics
                                    Many users in the FRET community employ the detection and characterization of different subpopu-
                                    lations or measurements of conformational dynamics as a handle to study biomolecules or biomolec-
                                    ular systems. Conformational dynamics are typically defined as:
                                       .   conformational transitions between distinct states separated by an activation barrier, typically
                                           defined as larger than the thermal energy, kB T, where kB is Boltzmann’s constant and T is the
                                           absolute temperature, and
                                       .   or conformational fluctuations within states, defined by the shape of the potential wells
                                           between activation barriers.
                                       Transitions can occur under equilibrium conditions, can be induced by the addition of substrates,
                                    ligands, or interaction partners (de Boer et al., 2019a; Mapa et al., 2010; Mazal et al., 2018;
                                    Schluesche et al., 2007); induced by mixing with denaturants (Kuzmenkina et al., 2006;
                                    Lindhoud et al., 2015; Maity and Reddy, 2016; Moosa et al., 2018; Nienhaus, 2006; Pirchi et al.,
                                    2011; Rieger et al., 2011; Schuler et al., 2002); or triggered by temperature (Ebbinghaus et al.,
                                    2010; Holmstrom et al., 2014; Nettels et al., 2009; Zhao et al., 2010a) and pressure modulations
                                    (Schneider et al., 2018; Sung and Nesbitt, 2020). Structural transitions can also occur
                                    spontaneously.
                                       SmFRET is unique in that it allows the detection and analysis of equilibrium and non-equilibrium
                                    conformational dynamics across at least 12 orders of magnitude in time, that is from the nanosec-
                                    onds to, in principle, thousands of seconds (Figure 3). Notably, it is important to optimize the


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            15 of 69



                                    labeling positions to maximize the distinction between different conformational states based on their
                                    FRET efficiencies (Dimura et al., 2020).

                                    Detecting dynamics
                                    Biomolecules are dynamic systems that show conformational flexibility and dynamics on fast time
                                    scales (Henzler-Wildman and Kern, 2007). Oftentimes, conformational interconversions occur on a
                                    timescale faster than the sampling time of the detection system, for example < 10 ms for TIRF
                                    modality or < 0.1 ms for confocal modality, resulting in the observed single-molecule time series or
                                    FRET efficiency histogram exhibiting only time-averaged FRET values, weighted by the fractional
                                    population of each conformational state. Several groups have developed methods for detecting and
                                    analyzing such ‘dynamic averaging’ from confocal-modality data. In general, these methods allow
                                    retrieval of dynamics on the milliseconds and sub-millisecond timescales by analyzing the average
                                    fluorescence lifetimes and/or photon counting statistics of single-molecule bursts. The precise knowl-
                                    edge of the experimental shot noise separates smFRET from other techniques in structural biology
                                    and enables a quantitative analysis of fluctuations caused by biomolecular dynamics. A number of
                                    methods have been developed for detecting and quantifying smFRET dynamics, which we discuss in
                                    more detail below on slower (section Slow dynamics) and faster time scales (section
                                    Faster dynamics). The first step in analyzing smFRET dynamics is the verification that dynamics are
                                    present. Popular methods for the visual detection of dynamics include:
                                       .   2D histograms of burst-integrated average donor fluorescence lifetimes versus burst-inte-
                                           grated FRET efficiencies (Gopich and Szabo, 2012; Kalinin et al., 2010b; Rothwell et al.,
                                           2003; Schuler et al., 2016),
                                       .   burst variance analysis (BVA) (Torella et al., 2011),
                                       .   two-channel kernel-based density distribution estimator (2CDE) (Tomov et al., 2012),
                                       .   FRET efficiency distribution-width analysis, for example by comparison to the shot noise limit
                                           (Antonik et al., 2006; Gopich and Szabo, 2005a; Ingargiola et al., 2018b; Laurence et al.,
                                           2005; Nir et al., 2006) or known standards (Geggier et al., 2010; Gregorio et al., 2017;
                                           Schuler et al., 2002), and time-window analysis (Chung et al., 2011; Kalinin et al., 2010a;
                                           Gopich and Szabo, 2007), and
                                       .   direct visualization of the FRET efficiency fluctuations in the trajectories (Campos et al., 2011;
                                           Diez et al., 2004; Margittai et al., 2003).


                                    Slow dynamics
                                    For dynamics on the order of 10 ms or slower, transitions between conformational states can be
                                    directly observed using TIRF-modality approaches, as have been demonstrated in numerous studies
                                    (Blanchard et al., 2004; Deniz, 2016; Juette et al., 2014; Robb et al., 2019; Sasmal et al., 2016;
                                    Zhuang et al., 2000). Nowadays, hidden Markov models (HMM) (Figure 4E) are routinely used for a
                                    quantitative analysis of smFRET time traces to determine the number of states, the connectivity
                                    between them and the individual transition rates (Andrec et al., 2003; Keller et al., 2014;
                                    McKinney et al., 2006; Munro et al., 2007; Steffen et al., 2020; Stella et al., 2018; Zarrabi et al.,
                                    2018). Below, we list extensions and other approaches for studying slow dynamics.
                                       .   Classical HMM analysis has been extended to Bayesian inference-based approaches such as
                                           variational Bayes (Bronson et al., 2009), empirical Bayes (van de Meent et al., 2014), com-
                                           bined with boot-strapping (Hadzic et al., 2018) or modified to infer transition rates that are
                                           much faster than the experimental acquisition rate (Kinz-Thompson and Gonzalez, 2018).
                                       .   Bayesian non-parametric approaches go beyond classical HMM analysis and also infer the
                                           number of states (Sgouralis et al., 2019; Sgouralis and Pressé, 2017).
                                       .   Hidden Markov modeling approaches have been extended to detect heterogeneous kinetics
                                           in smFRET data (Hon and Gonzalez, 2019; Schmid et al., 2016).
                                       .   Concatenation of time traces in combination with HMM can measure kinetic rate constants of
                                           conformational transitions that occur on timescales comparable to or longer than the measure-
                                           ment time (Kim et al., 2015b).
                                       .   In the confocal modality, slower timescales are accessible by exploiting the reentry of single
                                           molecules into the observation volume (recurrence analysis of single particles, RASP)
                                           (Hoffmann et al., 2011).


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            16 of 69


                Review Article                                                                              Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics


   #                   !"! #$%&                          $                                                '()                 %                 *+!,"*-.


                                                                             1#/23/(3.345+/#+)2.
                                                                                                                                                              δ!!"#$#"%
                                                                                                                             δ!!"#%

     7 + 64                                                                                                                  δ!#"#%                           δ!#"#$#"%

                                                                                   )6..!"
        #+,
                                                   -.:
              4.τ
                                          <+   42 <
               /τ !                 66+
                "# $          9:;.4
                                                                                                    '()*+,+#-.(/#+).!0                                                          #" "&%

   !           /0%&%1"23"#0%&%1456!                      "                                         7899:145;<=%>4?%9:$@                &        ,<;1@8&8%149:1@8&34#$%&


                                                                                                                                           89:;.466+<+42<-.


                                                         89:;.466+<+42<-.:                                                                 /6#4(.#(/2&+#+)2


                                                                                                             ;+,4.&#4=                                              89:;.466+<+42<-.
                                                                                                                                                                   >46)(4.#(/2&+#+)2


Figure 4. Exemplary selection of approaches to detect and quantify conformational dynamics in smFRET. (A) Dynamics in a three-state system are
detected using the two-dimensional distribution of the FRET efficiency and donor fluorescence lifetime (Reproduced from Gopich and Szabo, 2012.
Further reproduction of this panel would need permission from the copyright holder.) (B) The two-state dynamics of a DNA hairpin are revealed from
the standard deviation of the proximity ratio E that is higher than expected for photon counting statistics alone in the burst variance analysis (BVA).
(2011 The Biophysical Society. Published by Elsevier Inc All rights reserved. The figure was originally published as Figure 4C in Torella et al., 2011.
Biophysical Journal, 100(6): 1568–1577. Further reproduction of this panel would need permission from the copyright holder.) (C) In fluorescence
correlation spectroscopy (FCS), the dynamics show up as a positive correlation in the autocorrelation functions GDD and GAA and an anti-correlation in
the cross-correlation function GDA (2010 American Chemical Society Ltd. All rights reserved. The figure was originally published as Figure 1B and C in
(Gurunathan and Levitus, 2010, reproduced with permission). Copyright 2010 ACS Publications. Further reproduction of this panel would need
permission from the copyright holder.) (D) Photon-by-photon maximum likelihood estimation (MLE) infers the kinetic parameters directly from the
photon arrival times (2011 American Chemical Society Ltd. All rights reserved. The figure was originally published as the Abstract Figure in
Chung et al., 2011, reproduced with permission. Copyright 2011 ACS Publications. Further reproduction of this panel would need permission from the
copyright holder.) (E–F) A hidden Markov model (HMM) is applied to the time traces of the FRET efficiency to estimate the states and interconversion
rates (E). From the transition density plot (F), the connectivity of the FRET states is revealed. Displayed data in E and F are simulated. (Panels E and F:
2006 The Biophysical Society. Published by Elsevier Inc All rights reserved. The figures were originally published as Figure 4A and D in McKinney et al.,
2006. Biophysical Journal, 91(5): 1941–1951. Further reproduction of this panel would need permission from the copyright holder.)
Ó 2012, Gopich and Szabo. Panel A was originally published as Figure 1C in Gopich and Szabo, 2012. Further reproduction of this panel would need
permission from the copyright holder.
Ó 2011, The Biophysical Society. Published by Elsevier Inc. All rights reserved. Panel B was originally published as Figure 4C in Torella et al., 2011.
Further reproduction of this panel would need permission from the copyright holder.
Ó 2010, American Chemical Society Ltd. All rights reserved. Panel C was originally published as Figures 1B and 1C in Gurunathan and Levitus, 2010.
Further reproduction of this panel would need permission from the copyright holder.
Ó 2011, American Chemical Society Ltd. All rights reserved. Panel D was originally published as the abstract figure in Chung et al., 2011. Further
reproduction of this panel would need permission from the copyright holder.
Ó 2006, The Biophysical Society. Published by Elsevier Inc. All rights reserved. Panels E and F were originally published as Figures 4A and 4D in
McKinney et al., 2006. Further reproduction of this panel would need permission from the copyright holder.


                                                    There are still many challenges with respect to the accuracy of the approaches that need to be
                                                 discussed and improvements made to provide a reliable determination of kinetics.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                                                            17 of 69



                                    Faster dynamics
                                    Several methods exist that assist in the quantification of the kinetic parameters governing fast con-
                                    formational dynamics, as also exemplified in Figure 3A,B.
                                       .   Dynamic photon distribution analyses (PDA) that analyze the width of FRET efficiency distribu-
                                           tions with respect to photon shot noise and broadening by dynamic exchange (Gopich and
                                           Szabo, 2007; Kalinin et al., 2010b; Santoso et al., 2010b).
                                       .   Applying hidden Markov models on a photon-by-photon basis extends the achievable time
                                           resolution into the microsecond regime (Aviram et al., 2018; Keller et al., 2014; Mazal et al.,
                                           2019; Pirchi et al., 2016). More generally, photon-by-photon maximum likelihood analysis
                                           (Figure 4D) of diffusing or immobilized molecules has made it possible to extract sub-millisec-
                                           ond transition rates (Chung and Gopich, 2014; Chung et al., 2011; Gopich and Szabo,
                                           2009), transition path times of protein folding (Chung et al., 2012; Chung and Eaton, 2018)
                                           and binding of disordered proteins (Kim et al., 2018a; Sturzenegger et al., 2018; Kim and
                                           Chung, 2020) on the microsecond timescale.
                                       .   Using confocal-modality approaches, numerous studies also directly mapped transitions
                                           between conformational states for dynamics on the order of 0.5 ms or slower (Diez et al.,
                                           2004; Hanson et al., 2007; Margittai et al., 2003).
                                       .   Plasmonic enhancement of the fluorescence signal, reaching count rates in the megahertz
                                           regime for single molecules, allows a direct visualization of dynamics on the sub-millisecond
                                           timescale without analysis of the photon statistics (Acuna et al., 2012; Bohlen et al., 2019).
                                       .   Higher time resolution for TIRF experiments below 10 ms can be achieved using stroboscopic
                                           illumination (Farooq and Hohlbein, 2015) or fast sCMOS cameras (Fitzgerald et al., 2019;
                                           Girodat et al., 2020; Juette et al., 2016; Pati et al., 2020), reaching into the sub-millisecond
                                           domain.
                                       Fluorescence correlation spectroscopy (FCS) (Magde et al., 1972; Rigler et al., 1993) methods
                                    have also been widely applied and the observed kinetic rates are model-independent (i.e.,
                                    unbiased).
                                       .   By combining smFRET with FCS (Felekyan et al., 2013; Gurunathan and Levitus, 2010;
                                           Margittai et al., 2003; Schuler, 2018; Torres and Levitus, 2007), it is possible to quantify
                                           FRET dynamics that are faster than the diffusion timescale (Figure 4C).
                                       .   FRET dynamics as fast as a few picoseconds can also be retrieved from a variant of FCS
                                           dubbed ‘nanosecond FCS’ (nsFCS) (Nettels et al., 2008; Nettels et al., 2007; Schuler and
                                           Hofmann, 2013; Figure 3A).
                                       .   Using statistical filters, it is possible to extract species-specific properties and to quantify the
                                           exchange rates between different sub-populations (filtered-FCS) (Böhmer et al., 2002;
                                           Enderlein et al., 2005; Felekyan et al., 2013; Kapusta et al., 2007).
                                       .   Species-specific hydrodynamic radii can be extracted using single-burst FCS (Bravo et al.,
                                           2018; Laurence et al., 2008; Laurence et al., 2007). In combination with FRET-FCS or fil-
                                           tered-FCS, this approach simplifies the analysis of kinetics by eliminating the contribution of
                                           single-labeled molecules (Barth et al., 2018; Felekyan et al., 2013).
                                       In the analysis of fast dynamics and subpopulations, it is generally important to account for fast
                                    photophysical transitions, such as dye photoblinking, and for interactions of the dyes with the bio-
                                    molecular surface, which may interfere with subpopulation dynamics and result in inaccurate transi-
                                    tion rates (Chung and Gopich, 2014; Ingargiola et al., 2018b; Lerner et al., 2018b).
                                       The detection and analysis of fast dynamics is one of the issues addressed in the protein FRET
                                    challenge (Gebhardt et al., in preparation). Finally, at the moment of this writing, different analysis
                                    algorithms are typically being applied to the data independently from each other (e.g., MFD, BVA,
                                    2CDE, PDA, filtered-FCS in burst analysis) while, in fact, they could corroborate each other or even
                                    help in deciding on models. The field could focus on creating global multi-algorithm workflows or
                                    tools to test, how a model obtained with one algorithm would influence the results of other
                                    analyses.

                                    Detection and characterization of intra-state dynamics
                                    Rapid structural dynamics within a given conformational state, that is within a single energy mini-
                                    mum, can also be studied with smFRET by modeling them as a continuous distribution rather than a
                                    state-dependent distribution. In the given example, rigid and flexible conformational states can be


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            18 of 69



                                    distinguished in the measurement. Information regarding the flexibility of a given conformation can
                                    be retrieved by:
                                       .   describing their kinetic signatures in FRET efficiency vs. lifetime (E t ) plots (Figure 4A–
                                           B) (Gopich and Szabo, 2012; Kalinin et al., 2010b),
                                       .   using the fluorescence lifetime information available with TCSPC, which can be used to analyze
                                           sub-ensemble fluorescence decays and retrieve the inter-dye distance distribution and the
                                           inter-dye distance diffusion coefficient (Gansen et al., 2018; Lerner et al., 2014;
                                           Neubauer et al., 2007; Rahamim et al., 2015; Sisamakis et al., 2010),
                                       .   analyzing brightness by sub-ensemble fluorescence intensity distribution analysis (FIDA)
                                           (Neubauer et al., 2007),
                                       .   analyzing the photon statistics of the time-stamped photon arrival trajectories
                                           (Ingargiola et al., 2018b; Ramanathan and Muñoz, 2015), and
                                       .   relating the time-averaged FRET efficiencies and subpopulation-specific nsFCS to polymer
                                           models or simulated ensembles (Borgia et al., 2018; Holmstrom et al., 2018).
                                       It is, however, important to mention that the distinction between dynamics within a conforma-
                                    tional state and dynamics of transitions between different conformational states is still under debate,
                                    which highly depends on the definition of an activation barrier for different modes of structural
                                    dynamics and on the different smFRET modalities used.

                                    FRET efficiency
                                    The efficiency of the energy transfer process, that is the FRET efficiency, E, is defined as the fraction
                                    of donor excitations that result in energy transfer. Assuming a single distance between the centers
                                    of the donor and acceptor molecules, RDA , the FRET efficiency is given by:
                                                                                    kFRET              1
                                                                             E¼              ¼         6 ;                                  (1)
                                                                                  kFRET þ kD           RDA
                                                                                                 1þ    R0


                                    where kFRET is the rate of energy transfer, kD is the rate of donor de-excitation in the absence of an
                                    acceptor molecule, and R0 is the Förster distance (discussed in section Dye models). Hence, FRET is
                                    indeed a tool that can measure distances on the molecular scale (Förster, 1948; Stryer and Haug-
                                    land, 1967). For many smFRET studies, a qualitative indicator of the inter-probe distance is suffi-
                                    cient, for example, to merely be able to distinguish between conformational subpopulations or their
                                    transitions. Therefore, for all FRET experiments that do not require the exact inter-dye distance, the
                                    absolute value of E does not need to be known. However, special care should be taken to ensure
                                    that the observed changes of the donor and acceptor intensities report on a structural change of the
                                    molecule and are not a result of dye photophysics or dye-surface interactions. In the cases where
                                    accurate distance measurements are desired, smFRET can be used for that purpose.

                                    Determining absolute FRET efficiencies from fluorescence intensities
                                    Typically, in smFRET, the FRET efficiency is determined from the fluorescence intensities:
                                                                                          FAemjDex
                                                                                E¼                       ;                                    (2)
                                                                                     FDemjDex þ FAemjDex

                                    where FAemjDex is the sensitized fluorescence signal from the acceptor after donor excitation and
                                    FDemjDex is the signal emanating from the donor. Here, we use a notation specific to experiments
                                    using alternating laser excitation, but equivalent expressions can be derived for single-color excita-
                                    tion. In reality, the absolute value for E requires knowledge of some correction factors
                                    (Hellenkamp et al., 2018a; Lee et al., 2005):
                                                                                                         
                                                                             IAemjDex aIDemjDex dIAemjAex
                                                               E¼                                             ;                    (3)
                                                                    g IDemjDex þ IAemjDex    aIDemjDex dIAemjAex

                                    where IAemjDex is the background-corrected signal in the acceptor emission channel after donor exci-
                                    tation, IDemjDex is the background-corrected signal in the donor emission channel after donor excita-
                                    tion and IAemjAex is the background-corrected signal in the acceptor emission channel after acceptor


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            19 of 69



                                    excitation. The last term can be estimated using the acceptor-only species and fluorescence signal
                                    after acceptor excitation when the ALEX/PIE method is used (Hellenkamp et al., 2018a;
                                    Kudryavtsev et al., 2012; Lee et al., 2005) or by comparing fluorescence intensities before and
                                    after donor photobleaching prior to acceptor photobleaching in trajectories from immobilized
                                    molecules (Yoo et al., 2018).
                                       The required correction factors are:
                                       .   a, the fraction of the donor fluorescence signal detected in the acceptor channel due to spec-
                                           tral crosstalk,
                                       .   d, the fraction of acceptor photons arising from excitation of the acceptor at the wavelength
                                           of the donor-exciting laser, directly, and not excitation via energy transfer,
                                       .   the g factor (Ha et al., 1999), which compensates for the fact that the number of photons
                                           detected from the donor and acceptor fluorophores is not proportional to the number of their
                                           excitation/de-excitation cycles for two reasons: (i) fluorophores, in general, have different fluo-
                                           rescence quantum yields, fF values, and (ii) the efficiencies of detecting photons are different
                                           for the two channels due to different optical transmission efficiencies (owing to the characteris-
                                           tics of the filters and optics used) and different spectral sensitivities of the detectors.
                                      The optimal procedures for determining the correction parameters is still a matter of active
                                    debate within the community. In the following, we focus on the g factor, which we identify as the
                                    major contribution to uncertainty in smFRET experiments.

                                    Determining the g factor in confocal mode
                                    Whenever a broad E distribution is reported in the confocal mode, the g factor can be extracted
                                    using ALEX/PIE measurements. This method exploits the fact that the stoichiometry parameter, S
                                    (Kapanidis et al., 2004) (i.e., the ratio between the number of photons emitted after donor excita-
                                    tion and the number of photons emitted after donor and acceptor excitations), is independent of E
                                    when properly corrected for g. It is thus essential that the sample contains two or more species with
                                    different distances and thus FRET efficiencies, E, yet identical values of g for this method to work
                                    (Lee et al., 2005). Thus, accurate measurements of fF for both dyes have to be performed for each
                                    species. Alternatively, fluorescence lifetime measurements and the correlated analysis of intensity
                                    and lifetime data is often used to determine individual g factors for each E sub-population, since life-
                                    time-based FRET, in principle, provides the absolute E of a sub-population of single-molecule bursts
                                    independently from its intensity-based counterpart (Rothwell et al., 2003; Sisamakis et al., 2010;
                                    Vandenberk et al., 2018). However, when one or more species are dynamically averaged, a proper
                                    determination of the g factor becomes more challenging and different assumptions need to be
                                    made.
                                        Currently, the uncertainty in the determination of g is one of the largest contributions to discrep-
                                    ancies of smFRET histograms measured from different laboratories (Gebhardt et al., in preparation).
                                    Hence, it would be beneficial to discuss optimal approaches to determine a robust confocal-mode g
                                    value.

                                    Determining the g factor in TIRF mode
                                    When ALEX data are collected on immobilized samples, the g factor can also be estimated for indi-
                                    vidual molecules, provided that the acceptor photobleaches before the donor (Ha et al., 1999;
                                    Hildebrandt et al., 2015; McCann et al., 2010). Here, the decrease in the acceptor signal and the
                                    increase in donor signal upon acceptor photobleaching can be directly compared. This is also true
                                    for molecules undergoing slow dynamics between different conformations as the changes in inten-
                                    sity reflect the changes in detection efficiency. For this approach to be accurate, however, the accep-
                                    tor must not enter a transient (e.g., redox or triplet) state that still absorbs energy from the donor
                                    (Hofkens et al., 2003; Nettels et al., 2015). The individual g factors are usually broadly distributed,
                                    indicating a potential variability in its value. Nevertheless, an average g factor is often applied to
                                    molecules where the donor photobleaches before the acceptor.

                                    Determining absolute FRET efficiencies from fluorescence lifetimes
                                    In addition to the traditional intensity-based FRET efficiency (E) can also be determined from the
                                    fluorescence lifetime (t DðAÞ ) of the donor in the presence and absence of the acceptor, denoted by


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            20 of 69



                                    t DðAÞ and t Dð0Þ , respectively. Assuming a single distance between donor and acceptor fluorophores
                                    (i.e., no distance fluctuations), the FRET efficiency is given by:
                                                                                                t DðAÞ
                                                                                        E¼1                                                   (4)
                                                                                                t Dð0Þ

                                       The advantage of this approach is that correction factors are not needed, as most of the above-
                                    mentioned corrections influence the relative number of photons detected in the donor and acceptor
                                    channels, but not the donor fluorescence decay. The lifetime approach can also be used in ensem-
                                    ble/imaging measurements under conditions of incomplete labeling. Combined intensity- and life-
                                    time-based FRET efficiencies can additionally be used for checking the self-consistency of the data
                                    and for detecting dynamics (e.g., via E-t plots) (Gopich and Szabo, 2012; Kalinin et al., 2010b;
                                    Rothwell et al., 2003; Schuler et al., 2016).

                                    Other methods for determining FRET efficiencies
                                    There are additional procedures for determining the FRET efficiency, most of which are compatible
                                    with single-molecule fluorescence techniques. The FRET efficiency can also be determined:
                                       .   from the steady-state donor anisotropy (Clegg, 1992),
                                       .   from the ratio of the acceptor’s intensity after donor excitation to the acceptor’s intensity after
                                           acceptor excitation (Clegg, 1992),
                                       .   from the acceptor’s intensity in the presence and absence of the donor (e.g., via donor photo-
                                           bleaching) (Clegg et al., 1992),
                                       .   from the donor’s intensity in the presence and absence of the acceptor (e.g., via acceptor pho-
                                           tobleaching) (Bastiaens et al., 1996),
                                       .   from time-resolved anisotropy measurements, in particular in homo-FRET experiments, where
                                           two identical probes are used as a donor-acceptor pair (Bergström et al., 1999;
                                           Somssich et al., 2015),
                                       .   using fluorescence correlation spectroscopy methods (Müller et al., 2005; Widengren et al.,
                                           2001).


                                    Inter-dye distances
                                    When smFRET experiments are used for structural studies or accurate distance determination is
                                    desired, many steps need to be taken to convert the raw data (photons detected and registered by
                                    the detectors) into absolute inter-dye distances. In essence, it requires exact knowledge of the För-
                                    ster distance, R0 (also referred to as the Förster radius) and therefore of all parameters required for
                                    determining it, as well as knowledge with respect to the flexibility of the attached fluorophores
                                    (approximated using a dye-model). In this section, we review the various issues involved.

                                    Förster distance R0
                                    In FRET, the excitation energy of the donor fluorophore is transferred to an acceptor fluorophore via
                                    weak dipolar coupling. Considering a single donor-acceptor distance, RDA , the efficiency, E, of this
                                    non-radiative transfer process scales with the sixth power of RDA normalized by the Förster distance,
                                    R0 (Equation 1). In smFRET studies, dyes are usually coupled to the biomolecules via long (ranging
                                    typically between 10 and 15 atoms) mostly flexible linkers, which result in an equilibrium distribution
                                    of RDA values, pðRDA Þ, caused by the flexibility of the dye linkers. In this case, one may observe a
                                    mean FRET efficiency hEi related to the FRET efficiency, averaged over all distances and their
                                    probabilities:
                                                                                        Z¥
                                                                                            pðRDA Þ
                                                                               hE i ¼          6 dRDA :                                     (5)
                                                                                               RDA
                                                                                        0 1 þ  R0


                                       It is noteworthy to mention that Equation 5 holds under the assumption that the inter-dye dis-
                                    tance remains unchanged during the excited-state lifetime of the donor fluorophore. From the mean
                                    FRET efficiency hEi, one obtains the FRET-averaged apparent donor-acceptor distance, hRDA iE ,
                                    which differs from the distance between the mean dye positions (Kalinin et al., 2012) and is depen-
                                    dent on the flexibility and dynamics of the dye.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            21 of 69



                                       As mentioned before, R0 (Equation 1) is the distance at which half of the donor de-excitation
                                    events occur via energy transfer to the acceptor fluorophore. R0 (in Å) is given by:
                                                                                  2                           16
                                                                                  k FF;Dð0Þ
                                                                                            Z
                                                                     R0 ¼ 0:2108              F D ðlÞ"A ðlÞl dl ;                             (6)
                                                                                     n4im

                                    meaning that it depends on the donor fluorescence quantum yield in the absence of an acceptor,
                                    fF;Dð0Þ , the overlap between the area-normalized donor emission spectrum, F D ðlÞ, and the acceptor
                                    excitation spectrum with extinction coefficient, "A ðlÞ (in M 1cm 1), at the wavelength l (in nm), the
                                    relative orientation of the dye dipoles captured by the orientation factor, k2, and the refractive index
                                    of the medium, nim , between and around the dyes. It should be noted that, due to the l4 depen-
                                    dence of the overlap integral, small shifts in the spectra can have large effects on the R0 . The follow-
                                    ing sections describe the factors that influence R0 and the FRET efficiency in more detail.

                                    Extinction coefficient "
                                    The extinction coefficient of the acceptor dye affects R0 and the expected excitation rate in ALEX/
                                    PIE experiments. In the absence of an easy or affordable way to measure this parameter (it requires
                                    large amounts of dye for gravimetric analysis or FCS with controlled dilution [Fries et al., 1998]), the
                                    experimenter typically relies on the value given by the manufacturer, a value that can at times be
                                    unreliable. Alternatively, the extinction coefficient of the dyes may be theoretically assessed via the
                                    Strickler and Berg, 1962 equation, when fF;Dð0Þ and the fluorescence lifetime are known. Fortu-
                                    nately, " is not expected to vary much depending on the environment of the fluorophores, since
                                    both the fF;Dð0Þ and the fluorescence lifetime, in most cases, vary accordingly. Hence, one can con-
                                    clude that the local environment does not heavily influence the excitation probability (according to
                                    the Strickler-Berg equation mentioned above).

                                    Fluorescence quantum yield fF
                                    fF oftentimes changes upon labeling and can be sensitive to the local environment at the labeling
                                    position, to the conformational state of the molecule and to the binding of ligands, substrates or
                                    complex partners. Even dyes that are considered relatively insensitive to their local environment
                                    have been shown to exhibit a large change in fF upon conjugation to nucleic acids or proteins. As
                                    an extreme example, the quantum yield of Cy3B ranges from 0.19 to 0.97 at different labeling posi-
                                    tions on dsDNA, leading to considerable variation in the value of R0 for the pair Cy3B-ATTO 647N
                                    between 54.8 Å and 65.9 Å (Lerner et al., 2018b; Craggs et al., 2019). For dyes of the cyanine fam-
                                    ily, such as Cy3 and Cy5, or its variants Alexa Fluor 555 and Alexa Fluor 647 (Gebhardt et al., in
                                    preparation), fF is dependent on the excited-state isomerization, which is influenced by viscosity,
                                    steric restriction and (stacking) interactions (Hwang and Myong, 2014; Lerner et al., 2016;
                                    Levitus and Ranjit, 2011; Sanborn et al., 2007; White et al., 2006; Widengren et al., 2001). In
                                    summary, independent determination of fF for different labeling positions is strongly recom-
                                    mended. Notably, nsALEX/PIE and MFD experiments can probe the fluorescence lifetime, and thus
                                    directly identify changes in fF . Development of standard procedures for measuring or estimating
                                    fF , for example using an integrating sphere (Gaigalas and Wang, 2008; Pati et al., 2020) or a
                                    nanocavity (Chizhik et al., 2013; Chizhik et al., 2011), would benefit the field and should be
                                    discussed.

                                    Refractive index nim
                                    The actual index of refraction to be used for calculation of R0 lies somewhere between the index of
                                    refraction of an aqueous buffer (1.33) and that for proteins and DNA (~1.5) but the exact value is not
                                    known. Robert Clegg recommended using an intermediate value of 1.4, which reduces the maximal
                                    error in R0 to ~ 4% (Clegg, 1992). However, different values may be more appropriate depending
                                    on the geometry and environment of the fluorophores. To date, the refractive index has received
                                    very little attention in the field (Knox and van Amerongen, 2002).


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            22 of 69


             Review Article                                                                 Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics

                                                      Dye transition dipole orientation factor k2
                                                      This parameter describes the relative orientation of the transition dipole moments of the dyes and
                                                      strongly depends on dye mobility. Since the dyes’ orientations can change randomly on the time
                                                      scale of typical FRET events, the mean value of <k2> = 2/3 is typically taken. This well-known
                                                      dynamic averaging approximation assumes that the rotational diffusion timescale of a FRET pair is
                                                      much shorter than the fluorescence lifetime of the donor. However, it may well be that one of the
                                                      dyes is not freely rotating on this timescale (e.g., it may interact with the microenvironment). An
                                                      extreme example is a FRET system in which non-canonical fluorescent nucleotides were incorporated
                                                      into dsDNA. The rigid structure and natural helical twist of the DNA caused the relationship between
                                                      E and RDA to follow an interesting trend (Ranjit et al., 2009) with E being relatively low around
                                                      RDA ~ R0 , because of k2 ~ 0 (Wranne et al., 2017). In another smFRET experiment, a DNA molecule
                                                      was end-labeled with Cy dyes without sulfonic acids groups (Cy3 and Cy5), which have a tendency
                                                      to stack onto bases at the DNA termini (Iqbal et al., 2008; Ouellet et al., 2011), and the influence
                                                      of orientational effects on the FRET efficiency was measured. Although an influence of the orienta-
                                                      tion could be detected, the data showed that orientational effects average-out quite well in most
                                                      realistic cases (Iqbal et al., 2008). A method to estimate the lower and upper bounds for <k2> from
                                                      the donor and acceptor time-resolved anisotropies was proposed in the 1970s (Dale et al., 1979;
                                                      van der Meer, 2002). In smFRET measurements using the polarization-resolved MFD modality,


   A              dynamic average                               B       Atomistic dye description                                              C
              krotation , ktranslation >> kFRET
                                                                             9Å

              D
                                        A                                                                                                                                       Molecular
                  D                                                                                                                                                             dynamics
          DD
                                         A
                                           A A                                     20 Å
                                                                                                                                                                                simulations
                  D                               A
                                                                     Alexa488 C5           Alexa647 C2
                                                                     maleimide             maleimide
                  isotropic average
              ktranslation < kFRET < krotation
                                                                D       Representations of coarse-grained dyes
              D
                                         A        A                  Credible                     Accessible                   Accessible               Weighted
                  D                                                  Volume                       Volume                       Contact                  Accessible
          D
                                         A             A             (NPS)                                                     Volume                   Volume
                  D                               A
         D


                     static average
              krotation , ktranslation << kFRET
                                                                                   LLink                       LLink                        LLink                       LLink
              D                           A       A                   WDye                         WDye                         WDye                        WDye
                   D
          D
                                         A             A
          D       D                                                                           R                            R                            R                             R
                                                  A                 Dye       Localized                   Free diffusion               Free diffusion              Gaussian chain
                                                                    model      antenna                                                   + contact                   diffusion


Figure 5. Dye models for FRET. (A) The different kinetic averaging regimes for rotation and diffusion are shown schematically. In the dynamic averaging
regime, rotation and diffusion happen on a timescale faster than the FRET process. In the isotropic averaging regime, translation is slower than the
FRET process, but rotation is fast. The static average applies if both rotation and diffusion are slow compared to the rate of energy transfer. For most
experimental situations, the isotropic average is most appropriate. (2008 National Academy of Sciences. Reproduced from Wozniak et al., 2008.
Further reproduction of this panel would need permission from the copyright holder.) (B) A schematic of a donor/acceptor fluorophore pair (Alexa488,
Alexa647) attached to the protein Atlastin-1. (C) The accessible volume that the acceptor fluorophore can explore is determined from a molecular
dynamics simulation. (D) Different coarse-grained dye models are used in the community to describe the three-dimensional dye density rDye (see main
text). (Panels B, C, and D were reproduced from Dimura et al., 2016, Current Opinion in Structural Biology with permission, published under the
Creative Commons Attribution 4.0 International Public License (CC BY 4.0; https://creativecommons.org/licenses/by/4.0/).)
Ó 2008, National Academy of Sciences. Panel A was originally published as Figure S2 in Wozniak et al., 2008. Further reproduction of this panel would
need permission from the copyright holder.
Ó 2016, Dimura et al. Panels B, C and D were originally published as Figure 1a-d in Dimura et al., 2016, published under the Creative Commons
Attribution 4.0 International Public License.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                                                                 23 of 69



                                    information on the donor and acceptor fluorescence intensities, lifetimes, and anisotropies
                                    (Schaffer et al., 1999) are collected simultaneously and fluorescence anisotropy decays of different
                                    single-molecule sub-populations can be used to assess the <k2> uncertainty per conformational
                                    state (Ivanov et al., 2009; Kudryavtsev et al., 2012; Sindbert et al., 2011). It is noteworthy to
                                    mention that the majority of fluorophores used as donor and acceptor dyes in smFRET have a mono-
                                    exponential fluorescence decay and, hence, have one major emission dipole. In this case, the estima-
                                    tion of <k2> depends on the orientation of these single transition dipole moments. It has been pro-
                                    posed that the assumption of <k2> = 2/3 would carry much less uncertainty when the fluorescence
                                    signal is emanating from more than one emission dipole, yielding multi-exponential decays
                                    (Haas et al., 1978). This is an intriguing idea that could provide a realistic estimation for k2 and thus
                                    help simplify the transformation of FRET efficiencies into inter-dye distances. For a review on the
                                    dependence of FRET on k2, the reader is referred to (van der Meer, 2002). Finally, we note that
                                    there are several routines recommended by experienced members of the community to determine
                                    R0 accurately. Which approach is the most optimal is still under discussion.

                                    Dye models
                                    The Förster equation (Equation 1) allows the extraction of a distance directly from a FRET efficiency
                                    measurement. This distance directly corresponds only to the separation of the FRET fluorophores
                                    when the positions of the donor and the acceptor molecules are constant, the dye’s orientations are
                                    rapidly averaged and their microenvironment is known. Strictly speaking, this is never the case, even
                                    for a stable conformation of the labeled macromolecule, since dye molecules are typically attached
                                    to the macromolecules via flexible linkers, and the labeled macromolecule usually restricts the vol-
                                    ume accessible to the fluorophore (Best et al., 2007; Hellenkamp et al., 2018a; Ingargiola et al.,
                                    2018b). In addition, diffusion of the dyes while the donor is in the excited state can also influence
                                    the measured FRET efficiency (Ingargiola et al., 2018b). When the FRET rate is not too high (leading
                                    to a FRET efficiency of E<0:8) and the dyes do not interact with the protein surface, deviations due
                                    to dye dynamics are usually negligible (Hellenkamp et al., 2018a; Hellenkamp et al., 2017;
                                    Kalinin et al., 2012).
                                       Various groups have developed detailed dye models that account for the translational and rota-
                                    tional flexibility of the dyes and thus allow a more accurate description of the actual distance FRET
                                    measures (Figure 5D) (Beckers et al., 2015; Craggs and Kapanidis, 2012; Dimura et al., 2016;
                                    Haas et al., 1978; Kalinin et al., 2012; Muschielok et al., 2008; Schuler et al., 2020;
                                    Sindbert et al., 2011) and to test them experimentally (Hellenkamp et al., 2018a; Nagy et al.,
                                    2018; Peulen et al., 2017; Wozniak et al., 2008). For any given FRET efficiency, different dye mod-
                                    els will lead to slightly different extracted RDA distributions (deviations  5%). Choosing an appropri-
                                    ate model is therefore important for the accurate determination of RDA .
                                       Changes in RDA and the relative orientation of the dyes can occur on many different time scales,
                                    including the excited state lifetime, the interphoton time, and the photon burst duration. Averaging
                                    over these different distances and orientations is complicated due to the inherent non-linearity of
                                    the energy transfer process. However, there are exact analyses that describe the photon statistics in
                                    smFRET experiments (Antonik et al., 2006; Gopich and Szabo, 2005a; Nir et al., 2006).
                                       Since the dye linker lengths of the typical dyes used in smFRET experiments are long (ranging
                                    typically between 10 and 15 atoms, Figure 5B), translational and rotational diffusion of the dyes
                                    within the accessible volumes constrained by their linkers and the macromolecules to which they are
                                    conjugated lead to considerable changes in RDA . Such dynamics can occur on timescales comparable
                                    to the fluorescence lifetime, which leads to changes in RDA , from the moment of donor excitation to
                                    the moment of donor de-excitation. This process leads to the well-documented phenomenon
                                    termed diffusion-enhanced FRET (Beechem and Haas, 1989; Haas and Steinberg, 1984;
                                    Orevi et al., 2014), where the measured FRET efficiencies are higher than expected from a static
                                    distribution of RDA due to the increase in the probability for FRET to occur when RDA shortens while
                                    the donor is in the excited state (Eilert et al., 2018; Ingargiola et al., 2018b).
                                       This phenomenon has been treated by incorporating both rotational and translational diffusion of
                                    the fluorophores as fluctuations in RDA inside a potential well of the reaction coordinate RDA
                                    (Dingfelder et al., 2018; Haas and Steinberg, 1984; Ingargiola et al., 2018b). Similarly, rotational
                                    motions lead to changes in the relative orientation of the donor and the acceptor molecules and


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            24 of 69




    ; !"#"$%&'$(%$')*"+#                                                                                2 23.$"&0.%4'05/.


                              !                  !            !


          &+-+.%/0.+'(               !"#$%&'()&*+,)(                                                    40()%3+5'36%.6'%70(+)+0,

     < ,+-./&0.%-.0.)1"'+                                                                               : 6!,78#5"$.$%9:


                                      !                           !

                                                                          !"#$%&''(')*+,')-./).-*

        ()&12)1&*3%',('4/3'                !"#$%.+()*,2'(
                                                                          "*0*-*1/*,2%-&3,')-./).-*
                                                                                                               !""#$%&'()*+


Figure 6. Approaches to integrative modeling using FRET restraints. (A) Rigid bodies, representing either different domains of a protein or different
proteins within a complex, are arranged by translation and rotation to satisfy the FRET restraints. Adapted from Figure 1 of Hellenkamp et al., 2017.
(B) The structure that best satisfies all FRET restraints is selected from a prior ensemble. Adapted from Figure 2 of Dimura et al., 2020. (C) Using
triangulation, the most likely dye position is estimated from the FRET distances with respect to known reference positions on the structure.
(Reproduced from Andrecka et al., 2009, Nucleic Acid Research with permission, published under the Creative Commons Attribution-NonCommercial
4.0 International Public License (CC BY NC 4.0; https://creativecommons.org/licenses/by-nc/4.0). Further reproduction of this panel would need
permission from the copyright holder.) (D) Starting from a known structure, a molecular dynamics simulation is guided using the FRET information by
applying forces based on the FRET distances. (Reproduced from Dimura et al., 2020. Further reproduction of this panel would need permission from
the copyright holder.)
Ó 2009, Andrecka et al. Panel C was originally published as Figure 2A in Andrecka et al., 2009, published under the Creative Commons Attribution-
NonCommercial 4.0 International Public License.
Ó 2020, Dimura et al. Panel D was originally published as Figure 2A in Dimura et al., 2020. Published under the Creative Commons Attribution 4.0
International Public License.


                                    therefore to changes in R0 via k2. To this end, a complete kinetic theory treating both rotational and
                                    translational diffusion has been developed (Eilert et al., 2018). In many cases, a dynamic rotation -
                                    static translation model can be used (i.e., krotation >>kFRET >>ktranslation ) (Figure 5A). Interestingly,
                                    Monte-Carlo simulations show that this often-applied simplification can lead to errors in RDA
                                    (Hellenkamp et al., 2018a). The magnitude of the uncertainty depends on the donor fluorescence
                                    lifetime, the FRET efficiency, and the dye molecules’ diffusion constants and rotational correlation
                                    times. So far, no major disagreement of the dynamic rotation – static translation model with experi-
                                    mental data has been reported, thus supporting the use of the isotropic average of <k2> = 2/3.
                                        To obtain atomistic insights into the behavior of dyes on biomolecules, molecular dynamics simu-
                                    lations have been explored (Best et al., 2007; Deplazes et al., 2011; Spiegel et al., 2016;
                                    Girodat et al., 2020; Grotz et al., 2018; Hoefling et al., 2011; Reinartz et al., 2018; Shoura et al.,
                                    2014). By simulating the whole system, including the fluorophores, information is obtained about
                                    the accessible volume of the fluorophore, its potential interactions with the biomolecular surface and
                                    the dynamics of the system. The results of such simulations crucially depend on the parameterization
                                    (force field) of the dyes. Different parameter sets have been reported for commonly used dyes and
                                    validated against experimental data (Best et al., 2015; Graen et al., 2014; Schepers and Gohlke,
                                    2020; Shaw et al., 2020), but a consensus on the optimal parameterization has not yet been
                                    reached.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                25 of 69



                                    Structural modeling
                                    By accounting for various uncertainties described in the section Inter-dye distances, precise distan-
                                    ces can be calculated from FRET efficiencies. This enables the application of FRET for FRET-based
                                    structural studies, which are particularly promising for studying the conformations of large, heteroge-
                                    neous, flexible, and dynamic biomolecules and their complexes (Brunger et al., 2011; Craggs et al.,
                                    2019; Filius et al., 2020; Hellenkamp et al., 2017; Holmstrom et al., 2018; Kilic et al., 2018;
                                    Muschielok et al., 2008; Nagy et al., 2015; Sanabria et al., 2020; Treutlein et al., 2012;
                                    Yanez Orozco et al., 2018). Such systems are notoriously difficult to study with classical structural
                                    biology methods. For structure determination, there are further steps that need to be taken.

                                    Pipeline
                                    Different approaches have been used to derive structural models from FRET distance restraints. The
                                    general pipeline consists of the following steps:
                                       .   preparation and measurement of multiple donor-acceptor labeled variants with different label-
                                           ing positions,
                                       .   control experiments to assess the activity after labeling or immobilization, the photophysics of
                                           the probes, and the rotational freedom of the dyes,
                                       .   the non-trivial transformation from proximity ratios (uncorrected E values) to absolute FRET
                                           efficiencies of the different conformational subpopulations, to inter-dye distance information
                                           (or equilibrium distance distributions),
                                       .   relating the inter-dye distances to the structure by an appropriate dye model, and
                                       .   assessing the quality of the structural model.
                                        The FRET information alone is insufficient to generate an atomistic model de novo. FRET-
                                    restrained structural modeling thus relies on prior structural knowledge, from which novel structural
                                    models are generated. Different approaches have been used, each with specific advantages and lim-
                                    itations (Figure 6).
                                       .   Rigid body modeling/docking: The different parts or domains of the structure or complex are
                                           treated as rigid bodies and arranged in 3D space to satisfy the FRET restraints (Choi et al.,
                                           2010; Hellenkamp et al., 2017; Kalinin et al., 2012; Mekler et al., 2002; Peulen et al.,
                                           2020).
                                       .   Ensemble selection: An ensemble of structures is generated (e.g., based on MD simulations or
                                           normal mode analysis), from which the structures that are best explained by the FRET results
                                           are selected (Dimura et al., 2016; Kalinin et al., 2012; Sanabria et al., 2020).
                                       .   Credible volumes: The relative position of unresolved structural elements with respect to the
                                           known structure is estimated from the FRET-derived distances (Muschielok et al., 2008).
                                       .   FRET-guided molecular dynamics: To guide the simulation, FRET-restraints can be incorpo-
                                           rated into coarse-grained structural modeling and in all-atom MD simulations (Dimura et al.,
                                           2020).
                                       Different laboratories use different approaches to analyze their experimental results in context-
                                    dependent manners and the steps necessary for the conversion from FRET information to inter-dye
                                    distance information are still under debate. Importantly, the overall uncertainties in inter-dye distan-
                                    ces need to be determined from the uncertainty in R0 , the dye model and experimental precision,
                                    and to be incorporated into the integrative structural modeling (Dimura et al., 2016;
                                    Hellenkamp et al., 2018a; Hellenkamp et al., 2017; Kalinin et al., 2012; Muschielok et al., 2008;
                                    Muschielok and Michaelis, 2011; Peulen et al., 2017). As a result, FRET restraints yielded structural
                                    models that showed excellent agreement with existing models in benchmark studies (Kalinin et al.,
                                    2012; Mekler et al., 2002), resolved the structure of flexible parts and short-lived excited conforma-
                                    tional states that were inaccessible in crystallographic studies (Andrecka et al., 2009;
                                    Sanabria et al., 2020) and quantified the conformational flexibility of crystallographic states
                                    (Hellenkamp et al., 2017). To increase the success of FRET-derived structural models, a protocol
                                    has recently been proposed to determine the most informative labeling positions, the number of
                                    labeling positions needed to resolve a given conformation and the accuracy that can be expected
                                    for the FRET-derived structural models (Dimura et al., 2020).
                                       We should also be aware of the expected uncertainty for the determined structural model, which
                                    can be computed from the number of measurements, their average quality and the properties of the


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            26 of 69



                                    underlying computational method. Besides estimating the precision (Dimura et al., 2020), it is useful
                                    to introduce a quantitative quality estimate, 2n , for judging the accuracy of FRET-derived structure
                                    models based on a cross-validation statistical method in the spirit of Rfree used in X-ray crystallogra-
                                    phy (Brünger, 1992). Such accuracy estimates are essential for the quality control of I/H structure
                                    models, especially those deposited in the PDB-Dev. Dimura et al., 2020 pointed out that the com-
                                    plexity arising from different experiments could be mitigated by using Bayesian hierarchical data
                                    processing frameworks, which abstracts the experimental data and propagates the information and
                                    uncertainties to enable structural modeling at higher precision and accuracy. Combining the smFRET
                                    information with additional constraints provided by complementary methods has the potential to fur-
                                    ther improve the accuracy of the obtained I/H structural models (Berman et al., 2019).

                                    Verification of steps in the workflow using simulations
                                    At various points along the workflow, simulations can be extremely useful. They can be used to gain
                                    a better understanding of the analysis procedures (e.g., to test the impact of specific burst search
                                    and selection parameters) (Hagai and Lerner, 2019) or to determine to what extent a particular
                                    data analysis procedure is capable of extracting results reliably (e.g., distinguishing between one or
                                    two subpopulations) (Blanco and Walter, 2010; Chen et al., 2016). Having a ‘ground truth’ to com-
                                    pare to is also very helpful when developing new analysis methods before applying it to real data.
                                    This question is relevant, especially when other common analysis procedures yield different results.
                                    Of course, this practice should not replace control measurements and analyses with an established
                                    system for validation of a given method, although numerical simulations can give an economical and
                                    initial guidance. Using prior knowledge about the measured system and the experimental setup,
                                    one can perform simulations mimicking real measurements and then check the results of different
                                    analysis procedures. In this way, it is possible to determine which analysis procedure is most promis-
                                    ing in a given context. Another insightful aspect that simulations can provide is a consistency check
                                    of the data. One can simulate smFRET data assuming the number of states and/or kinetic rates
                                    derived from the experiments to see how well the model describes the measured data.


                                    Open science
                                    One of the cornerstones of the scientific method is the ability to reproduce experimental results. As
                                    experiments become more sophisticated, a clear description of the experiments is crucial. Recent
                                    trends toward Open Science practices call for full transparency of the scientific process, as has been
                                    formulated in the FAIR principle that data should be ‘Findable, Accessible, Interoperable, and Re-
                                    usable’ (Wilkinson et al., 2016). To this end, the procedures taken to acquire, analyze, and interpret
                                    experimental data should be provided. That includes describing each step, the reasons for taking
                                    the step and the information associated with the step. To ensure that the analysis remains transpar-
                                    ent and tractable, code should generally be openly available and all parameters and settings used in
                                    the analysis should be stored.
                                       Funding agencies embracing this philosophy (e.g., https://datascience.nih.gov/strategicplan)
                                    expect grantees to publish in open-access (OA) journals (and pay for the corresponding OA fees) or
                                    deposit manuscripts on preprint servers (e.g., Pubmed Central, arXiv, bioRxiv, ChemRxiv, medRxiv),
                                    and deposit data (sometimes also raw data) in repositories (e.g., Zenodo, the Dryad Digital Reposi-
                                    tory, FigShare) as well as analyses codes (e.g., GitHub). Open science disseminates knowledge by
                                    freely sharing results and the tools developed by independent scientists or teams working as part of
                                    a collaborative network. We would like to see the FRET community embrace and be committed to
                                    open science. Some tools are already in place, while others still need to be developed to make it
                                    easier to communicate the continuously growing knowledge and experience present in the FRET
                                    community.

                                    Intellectual property and software licenses
                                    There is obviously some tension between the precepts of open science and requirements imposed
                                    by some intellectual property (IP) policies. IP rights, including patent laws, were put in place to pro-
                                    mote the development of science and technology for the benefit of society by allowing those devel-
                                    oping intellectual property to retain the rights for the IP they developed. In fact, in some sense,
                                    patents were the first form of open access publication, only with a restrictive license for reuse. We


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            27 of 69



                                    do not oppose intellectual property rights, but given the developmental stage the FRET field is cur-
                                    rently in, we support the disclosure of methods, data, and software. For the advancement of the
                                    field, other groups must be able to reproduce the analyses of existing data, extend upon them and,
                                    if needed, be able to reproduce the experiments. The acquisition and analysis must be modifiable
                                    and extendable in agreement with the license chosen by the data or software creator. This license
                                    should be set as liberal as possible, taking into account the IP considerations mentioned above, but
                                    also encourage recognition of the considerable effort invested in producing successful protocols,
                                    designs, data, or software. Ultimately, if practiced fairly, open science should entice everyone,
                                    including commercial vendors, to adopt and contribute to community-defined file formats, provide
                                    free file-conversion codes, and open their analysis tools for scrutiny by the community.

                                    Proper documentation of data analysis practices
                                    By making analysis codes and protocols freely available, we hope to stimulate the acceptance, utili-
                                    zation, and exchange of new methods and tools. It is true that there already exist a large number of
                                    open-access programs that offer a large variety of analysis procedures for single-molecule photon
                                    trajectories (free-diffusion smFRET) and single-molecule videos (immobilized smFRET) data (see
                                    Table 1).
                                        To further improve the inter-operation between methods and analysis and to establish convenient
                                    documentation protocols, it is essential to work in an open multivalent environment. For this goal,
                                    the use of browser-based software such as ‘Jupyter notebooks’ and/or other available workspaces
                                    may serve as a convenient platform. Such workspaces provide an interactive scripting environment
                                    by combining formatted ‘rich’ text with well-commented code commands as well as code outputs
                                    (e.g., figures, tables, comments, equations) and explanations in a single web-based document. Such
                                    web-based workspace environments support several programming languages, including Python, R,
                                    C++, and, to some extent, MATLAB and Mathematica. Practitioners using this environment can then
                                    easily read, distribute, re-run, check, and modify the code. Software engineering approaches in sci-
                                    entific software usually include version control, code review, unit testing, continuous integration, and
                                    auto-generation of HTML manuals. In the next step, Jupyter notebooks or similar workspaces can
                                    also help newcomers perform complex analyses already in the web-based environment with minimal
                                    adaptation efforts, which will accelerate the dissemination of new analyses. Indeed, well-docu-
                                    mented, easy-to-use notebooks have been provided by various groups (Ambrose et al., 2020;
                                    Ingargiola et al., 2016b; Ingargiola et al., 2016a; Lerner, 2020; Lerner, 2019) (e.g., at https://
                                    github.com/tritemio/FRETBursts or https://craggslab.github.io/smfBox/).
                                        Although the notebook approach offers advantages to experienced users and software develop-
                                    ers, it might be difficult for many end-users to adapt to the script-based workflow. For those users, it
                                    may be more convenient to use the established and tested algorithms embedded in a graphical user
                                    interface (GUI). Indeed, there is a large variety of user-friendly software available (compiled in
                                    Table 1). To further increase the ease of use, the FRETboard software aims to make the underlying
                                    analysis algorithms of other packages available through a single web-based GUI (de Lannoy et al.,
                                    2020). As it can be used in a browser through a remote web server, this would allow any user to
                                    freely experiment with different analysis methods without the need for software installation or heavy
                                    computational resources.
                                        As the first step toward FAIR-compliant analysis practices, we propose establishing a software
                                    library that contains tested and proven algorithms for the analysis of fluorescence experiments,
                                    which will assist in their efficient distribution and implementation in existing workflows. Such efforts
                                    have already been initiated in the FRETbursts software package (Ingargiola et al., 2016b), and a
                                    GitHub group has been established at https://github.com/Fluorescence-Tools to collect software
                                    packages and connect software developers. Establishing a community-wide working group of ‘Anal-
                                    ysis software for FRET’ would be an important step in organizing and moderating this process.

                                    Standard file format
                                    To expedite the exchange of data between different groups and testing of different analysis meth-
                                    ods, it would be beneficial to have a minimal number of file formats, and to avoid the multiplication
                                    of ad hoc formats developed independently. In fact, the absence of a standard file format and sup-
                                    porting documents has caused issues within individual labs with respect to long-term data storage


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            28 of 69



Table 1. List of available software for smFRET analysis.
Software           Type       Description                                                                       URL
ALiX               Confocal   ALiX is developed for basic research on diffusing two-color smFRET in single or   https://sites.google.com/a/g.ucla.
                              multiple spot geometries (Ingargiola et al., 2017).                               edu/alix/
Fretica            Confocal   Fretica, a Mathematica package with a backend written in C++, is a user-          https://schuler.bioc.uzh.ch/programs/
                              extendable toolbox that supports MFD, PIE/ALEX, PCH (Huang et al., 2004;
                              Müller et al., 2000), FIDA (Gopich and Szabo, 2005b; Kask et al., 1999), PDA
                              (Antonik et al., 2006; Ernst et al., 2020), recurrence analysis (Hoffmann et al.,
                              2011), fluorescence lifetime fitting, FLIM, FCS, FLCS (Arbour and Enderlein,
                              2010; Dertinger et al., 2007), dual-focus FCS, nsFCS (Nettels et al., 2007;
                              Schuler and Hofmann, 2013), maximum likelihood estimation from photon-by-
                              photon (Gopich and Szabo, 2009) and binned trajectories, simulation of confocal
                              experiments and more (Nettels and Schuler, 2020; https://schuler.bioc.uzh.ch/
                              programs/).
FRET_3colorCW      Confocal   C++ and MATLAB GUI-based CPU-GPU co-parallelization software package for          https://github.com/hoisunglab/FRET_
                              an enhanced maximum likelihood analysis of two- and three-color fluorescence      3colorCW
                              photon trajectories generated by continuous-wave donor excitation (Yoo et al.,
                              2020).
gSMFRETda          Confocal   gSMFRETda is a GPU-capable program for Monte Carlo simulations of PDA. It can https://github.com/liu-kan/
                              sample dwell time and other parameters in fine grids, thus allowing the analysis of gSMFRETda
                              rapid dynamic interconversions (Liu et al., 2019).
H2MM               Confocal   H2MM is a maximum likelihood estimation algorithm for a photon-by-photon          http://pubs.acs.org/doi/suppl/10.
                              analysis of smFRET experiments (Pirchi et al., 2016).                             1021/acs.jpcb.6b10726/suppl_file/
                                                                                                                jp6b10726_si_002.zip
MFD              Confocal     A modular software package for confocal fluorescence spectroscopy and imaging https://www.mpc.hhu.de/software/3-
Spectroscopy and              experiments using multiparameter fluorescence detection (MFD) with all tools  software-package-for-mfd-fcs-and-
Imaging                       (FCS, fFCS, PDA, seTCSPC, trace analysis, 2D simulation of MFD diagrams,      mfis
                              Burbulator) and multiparameter fluorescence image spectroscopy (MFIS)
                              (Antonik et al., 2006; Felekyan et al., 2005; Kühnemuth and Seidel, 2001;
                              Widengren et al., 2006; Felekyan et al., 2020).
OpenSMFS           Confocal   A collection of tools (Ingargiola et al., 2016b) for solution-based single-molecule https://github.com/OpenSMFS
                              fluorescence spectroscopy, including smFRET, FCS, MC-DEPI (Ingargiola et al.,
                              2018b).
smfBox             Confocal   A confocal smFRET platform, providing build instructions and open-source          https://craggslab.github.io/smfBox/
                              acquisition software (Ambrose et al., 2020).
rFRET              Confocal   rFRET is a comprehensive, MATLAB-based program for analyzing ratiometric          https://peternagy.webs.com/fret#rfret
                   Imaging    microscopic FRET experiments (Nagy et al., 2016).
ChiSurf            Confocal ChiSurf is a fluorescence analysis platform for the analysis of time-resolved       https://github.com/Fluorescence-
                   Imaging fluorescence decays (Peulen et al., 2017).                                           Tools/ChiSurf/wiki
                   Ensemble
PAM - PIE          Confocal PAM (PIE analysis with MATLAB) is a GUI-based software package for the analysis RRID:SCR_020966, https://www.cup.
Analysis with      Imaging of fluorescence experiments and supports a large number of analysis methods      uni-muenchen.de/pc/lamb/software/
MATLAB             Ensemble ranging from single-molecule methods to imaging (Schrimpf et al.,               pam.html
                            2018; Barth et al., 2020).
AutoSiM            TIRF       AutoSiM is a deep-learning developed MATLAB program for automatically             https://doi.org/10.7302/ck2m-qf69
                              selecting and sorting smFRET traces (Li et al., 2020a).
BIASD              TIRF       BIASD uses Bayesian inference to infer transition rates that are more than three http://github.com/ckinzthompson/
                              orders of magnitude larger than the acquisition rate of the experimental smFRET biasd
                              data (Kinz-Thompson and Gonzalez, 2018).
DeepFRET           TIRF       smFRET software based on deep-learning for automatic trace selection and           https://github.com/hatzakislab/
                              classification. It includes all common features: image analysis, background-       DeepFRET-GUI
                              corrected trace-extraction, hidden Markov analysis, correction factor application,
                              and data visualization (Thomsen et al., 2020).
ebFRET             TIRF       ebFRET performs combined analysis on multiple smFRET time-series to learn a set https://ebfret.github.io/
                              of rates and states (van de Meent et al., 2014).
FRETboard          TIRF       smFRET data preprocessing and analysis using algorithms of choice and user        https://github.com/cvdelannoy/
                              supervision. Also offered as a web-based user interface (de Lannoy et al., 2020). FRETboard
HaMMy              TIRF       smFRET analysis and hidden Markov modeling (McKinney et al., 2006).               http://ha.med.jhmi.edu/resources/
hFRET              TIRF       hFRET uses variational Bayesian inference to estimate the parameters of a         https://github.com/
                              hierarchical hidden Markov model, thereby enabling robust identification and      GonzalezBiophysicsLab/hFRET
                              characterization of kinetic heterogeneity (Hon and Gonzalez, 2019).
Table 1 continued on next page


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                 29 of 69


Table 1 continued
Software             Type       Description                                                                        URL
iSMS                 TIRF       iSMS is a user-interfaced software package for smFRET data analysis. It includes http://isms.au.dk/
                                extraction of time-traces from movies, traces grouping/selection tools according
                                to defined criteria, application of corrections, data visualization and analysis with
                                hidden Markov modeling, and import/export possibilities in different formats for
                                data-sharing (Preus et al., 2015; Preuss et al., 2020).
MASH-FRET            TIRF       MASH-FRET is a MATLAB-based software package for the simulation                     https://rna-fretools.github.io/MASH-
                                (Börner et al., 2018) and analysis of single-molecule FRET videos and trajectories FRET/
                                (video processing [Hadzic et al., 2016], histogram analysis [König et al., 2013],
                                and transitions analysis [Hadzic et al., 2018; König et al., 2013]).
miCUBE               TIRF       TIRF smFRET platform, providing detailed build instructions and open-source        https://hohlbeinlab.github.io/miCube/
                                acquisition software (Martens et al., 2019).                                       index.html
SMACKS               TIRF       SMACKS (single-molecule analysis of complex kinetic sequences) is a maximum- https://www.singlemolecule.uni-
                                likelihood approach to extract kinetic rate models from noisy single-molecule data freiburg.de/software/smacks
                                (Schmid et al., 2016).
smCamera             TIRF       smFRET data acquisition (Windows. exe) and analysis (IDL, MATLAB) with example http://ha.med.jhmi.edu/resources/
                                data (Roy et al., 2008).
SPARTAN              TIRF       Automated analysis of smFRET multiple single-molecule recordings. It includes      https://www.scottcblanchardlab.com/
                                extraction of traces from movies, trace selection according to defined criteria,   software
                                application of corrections, hidden Markov modeling, simulations, and data
                                visualization (Juette et al., 2016).
STaSI                TIRF       STaSI uses the Student’s t-test and groups the segments into states by hierarchical https://github.com/LandesLab/STaSI
                                clustering (Shuang et al., 2014).
TwoTone              TIRF       A TIRF-FRET analysis package for the automatic analysis of single-molecule FRET https://groups.physics.ox.ac.uk/
                                movies (Holden et al., 2011).                                                   genemachines/group/Main.Software.
                                                                                                                html
vbFRET               TIRF       vbFRET uses variational Bayesian inference to learn hidden Markov models from http://www.columbia.edu/cu/
                                individual, smFRET time trajectories (Bronson et al., 2009).                  chemistry/groups/gonzalez/software.
                                                                                                              html
Fast NPS             Modeling A nano-positioning system for macromolecular structural analysis (Eilert et al.,     http://dx.doi.org/10.17632/7ztzj63r68.
                              2017).                                                                               1
Fluordynamics        Modeling Fluordynamics is a PyMOL plugin to label biomolecules with organic fluorophores https://github.com/RNA-FRETools/
                              for all-atom molecular dynamics simulations. It builds on AMBERDYES             fluordynamics
                              (Schepers and Gohlke, 2020) and extends the force field to common nucleic acid
                              linker chemistries (Steffen et al., 2016).
FPS                  Modeling A toolkit for FRET restrained modeling of biomolecules and their complexes for https://www.mpc.hhu.de/software/1-
                              quantitative applications in structural biology (Kalinin et al., 2012).        fret-positioning-and-screening-fps
FRETraj              Modeling FRETraj is a Python API to the LabelLib package, which integrates into PyMOL to https://github.com/RNA-FRETools/
                              interactively calculate accessible-contact volumes and predict FRET efficiencies fretraj
                              (Steffen et al., 2016).
FRETrest in          Modeling FRETrest is a set of helper scripts for generating FRET-restraints for Molecular     http://ambermd.org/doc12/Amber20.
Amber20                       Dynamics (MD) simulations performed with the AMBER Software Suite                    pdf
                              (Dimura et al., 2020).
LabelLib             Modeling LabelLib is a C++ library for the simulation of the accessible volume (AV) of small https://github.com/Fluorescence-
                              probes flexibly coupled to biomolecules (Dimura et al., 2016; Kalinin et al.,       Tools/LabelLib
                              2012).


                                      and re-analysis. Online data deposition in well-documented file formats would therefore save a lot of
                                      headaches for many laboratories. Even if standard file formats are carefully designed or developed,
                                      it will be inevitable to modify the existing formats or introduce new formats in the future. The list of
                                      standard formats should be regularly updated, and the analysis codes should also be kept current
                                      and properly maintained to guarantee their compatibility with the new standard formats.
                                          The raw experimental data should be supplied in a universal data file format that can be easily
                                      read and scrutinized (Figure 7 left). Ideally, the file should store both raw data and sufficient meta-
                                      data to specify the measurement, setup, and sample. The metadata should be stored in a human-
                                      readable text-based format, while space-efficient storage of the raw photon data should be ensured
                                      by lossless compression. There are currently many different file formats for smFRET data, developed


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                    30 of 69


           Review Article                                             Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics


Figure 7. Concept for data storage following the FAIR principle. All essential information should be contained in two data files, one for raw data and a
second with the essential information regarding the associated analysis. (Left) Structure of proposed data file formats containing confocal or TIRF raw
data in a time-tagged, TT, or time-tagged time-resolved, TTTR, format together with sample- and experiment-specific metadata (for details, see
Figure 8). The measurement specifications are needed by the reading routine to reconstruct the photon trace from the stored data, for example, for
timing in the TT format (sampling frequencies expressed as time bins or frame rates) or in the TTTR format (laser repetition rates, time binning in time-
correlated single-photon counting). Moreover, the detector that measured the signal is noted (detector #) along with the detection time with a given
time resolution. For representing the detection time of single photons in time-resolved smFRET studies, the TTTR format is used where the time
corresponds to the sum of the macro time and the nano time (upper left panel). The macro time comprises multiple cycles of excitation laser pulses
(blue vertical lines) and the nano time is determined by time-correlated single-photon counting with picosecond resolution. The TTTR format is the
most compact data format for single-molecule fluorescence data for detection times with picosecond time resolution and macro-times of hours
(Felekyan et al., 2005). The representation of the photon detection of intensity-based and imaging-based smFRET studies is in the TT format, where
the macro-time comprises multiples of the external clock pulse or readout cycles, where single or several photons were detected. The stack of TIFF
images acquired in TIRF measurements (lower left panel) is transformed into the TT format for analyzing photon time traces for selected spots. (Middle)
For the corresponding data file, a metadata system as implemented in the Photon-HDF5 file format (Ingargiola et al., 2016a) is suggested. (Right) The
analysis file should contain the determined parameters obtained by a quantitative analysis together with analysis metadata that assure evaluation,
reproducibility, and re-usability of the analysis. The processed data should be documented as outlined in Figure 8D.


                                     by different research groups and companies. In general, such files are hard to access for other labo-
                                     ratories and they are not guaranteed to be perennial, which poses an additional challenge to the
                                     community. To promote the adaptation of new file formats, conversion tools for older file formats
                                     should be provided so that future software codes can focus on handling one (or at least only a very
                                     few) common file formats, such as the phconvert suite of notebooks for transforming many file for-
                                     mats into Photon-HDF5 (see http://photon-hdf5.github.io/phconvert/). Reaching such a consensus is
                                     possible, as has been demonstrated by the acceptance of a single file format for the deposition of
                                     NMR data (Ulrich et al., 2019).

                                     File formats for (time-correlated) photon counting with point-detector data
                                     (confocal modality)
                                     Several formats have been used and reported for time-correlated single-photon counting data
                                     (Brand et al., 1997; Brooks Shera et al., 1990; Eggeling et al., 2001; Felekyan et al., 2005;
                                     Rigler et al., 1993; Schaffer et al., 1999; Tellinghuisen et al., 1994; Wahl et al., 2008;
                                     Widengren et al., 2006). One example is the time-tagged time-resolved (TTTR) file format given in
                                     the left panel of Figure 7. Because of its compactness, this file format has been widely adopted by


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                    31 of 69




                                                            General informaon
              Who: Experimenter informaon: Name, ORCID                                                                      A
              Where: Reference to citaon/bibliography (if applicable): Author list, journal (volume, pages, year), preprint
      W       server, links to addional repositories (e.g. for data)
              What: Sample name and biological source: Sample name, source type (natural, recombinant, synthec), natural
              source organism, recombinant source organism,(e.g. E. coli BL21 ( DE3)), polymer sequence (protein, RNA, DNA)


                              Method-speciﬁc informaon adapted to smFRET studies

      § Live-cell or in vitro                    Sample               B            Experiment               § Instrument details:          C
      § Sample properes                                                                                       • Measurement modality +
        of wild type vs. labeled                                                                                 speciﬁcaons
      § Buﬀer and addives                                                                                     • Data acquision electronics
      § FRET details                                                                                             + ming
        • dyes and linkages                                                                                    • Opcal ﬁlters, polarizers
        • labeling posions                                                                                    • Detectors
        • sample type                                                                                          • Calibraon
          (measured FRET-pairs)                                                                             § Acquision parameters:
                                                                                                               • Laser power, repeon rate
                                                                                                            § Temperature
     § Potenal Inputs:
        • Derived data with FRET-
                                         Interpretaon E
                                                                                                                                D
        pair speciﬁc uncertaines for: & Final Model                               Measurement § •Protocols for:
                                                                                                   Burst search, ﬁltering/selecon
           • Inter-dye distances                    C3                             & Analysis    • Analysis to determine dye and
                                                Relaxaon
           • Heterogeneity descriptors
                                                                                                             FRET parameters with quality of
        • Förster distance + uncertainty
                                                   me
                                                                                                              ﬁts and uncertaines:
        • Assigned state
                                                  C1/C2                                                       • Brightness,
        • Kinec network
                                                  E                                                           • Fluorescence lifeme

                                                                                FRET Intensity
          with relaxaon mes
                                                                                                              • Fluorescence anisotropy
        • Modeling procedure, so$ware
                                                                                                              • FRET eﬃciency
         and parameters

                                                                              eﬃciency
                                                                                                         § Reference measurements
     § Integrave s                                                                                      § Calibraon parameters
     § Kinec                                         C1, C2                                             § Used so$ware
                                                                                                 Time
     § Model precision and quality esmates          +C3                                                 § Link to raw and processed data


Figure 8. Disseminating the results of smFRET studies. Recommended categories for data and method-specific information (metadata), which are
needed for documentation of smFRET studies where the authors want to archive their obtained kinetic/structural models. (A) General information. (B)
Information on the sample and FRET-specific properties. (C) Information on the experiment and data acquisition. (D) Information on processing and
analysis procedures. (E) Information on the interpretation of the data and the final kinetic network or structural model.


                                    commercial companies (e.g., Becker and Hickl and PicoQuant) providing TCSPC electronics and
                                    point detectors for solution/imaging studies.
                                       The basic formats have been extended in the Photon-HDF5 (Ingargiola et al., 2016a) file format
                                    that connects rich metadata with the raw photon information in a single, space-efficient format suit-
                                    able for sharing and long-term data archival. Moreover, several software programs exist that can
                                    easily transform raw data files to the Photon-HDF5 format. Once enough metadata is available in the
                                    community, the relative importance of particular metadata entries on the resulting FRET data can be
                                    assessed.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                32 of 69


           Review Article                                              Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics

                                     File format for camera-based acquisition (wide-field/TIRF modality)
                                     Camera-based data is acquired as a stack of images (e.g., TIFF). To extract time trajectories, several
                                     steps are needed to yield the time-binned fluorescence intensity (e.g., spot identification; donor and
                                     acceptor spot registration; thresholding; background subtraction, etc.). A file format for TIRF-based
                                     smFRET (immobilized) measurements has been proposed (Greenfeld et al., 2015). Alternatively,
                                     human-readable plain text files with an agreed format and greatly downsized from the raw TIFF
                                     stacks can also work well for TIRF-based smFRET traces. Binary file formats for efficient data com-
                                     pression have also been implemented (Juette et al., 2016).

                                     Exchange file format for processed data
                                     In addition to standardized raw file formats, we recommend defining exchange file formats for differ-
                                     ent levels of processed data (Figure 7, middle panel). This will allow researchers to establish flexible
                                     and modular workflows spanning different software packages and facilitate the adoption of novel
                                     analysis approaches. The deposition of processed data in agreed-upon file formats also ensures that
                                     published data can be re-used at a later time point, for example, for more elaborate structural
                                     modeling approaches (Köfinger et al., 2019). For the storage of processed data, we believe that it
                                     is important to retain the connection to the raw data by including the relevant metadata. For exam-
                                     ple, corrected FRET efficiency histograms should be deposited together with the raw signal intensi-
                                     ties in the donor and acceptor channels, the background intensities and the calibration factors.

                                     Repositories and data bank for FRET data and models
                                     Metadata for FRET experiments
                                     To ensure that the reported results are reproducible, raw data must be sufficiently annotated. One
                                     important source of inspiration for developing recommendations and standards for the FRET com-
                                     munity comes from the world-wide Protein Data Bank (wwPDB) (Berman et al., 2003; Young and
                                     Westbrook, 2019). Following the standards of the wwPDB, it is recommended to provide additional
                                     information to the models as outlined in Figure 8.

                                     Archiving FRET experiments
                                     In this respect, we strongly encourage the publication of datasets with detailed descriptions of the
                                     acquisition and analysis in scientific journals. Alternatively, or in addition, structural information and
                                     raw datasets should immediately be deposited in repositories provided by the publisher or general-
                                     ist repositories (Table 2) with a Digital Object Identifier or link for access and citation. Online and
                                     public repositories also act as a form of data and knowledge backup, which is difficult to achieve
                                     and maintain at the scale of a single laboratory. Comparing a repository with a database, it is obvi-
                                     ous that a database has significant advantages for the scientific community. While both archive forms
                                     provide open access to the data for all users, only a database can fulfill the quality criteria for safe
                                     usage of the deposited data by (1) creating standard definitions for the experimental data used for
                                     determining kinetic and/or structural models and their features; (2) developing methods to collect
                                     the minimum amount of required information for curation and validation of models and data; and (3)


Table 2. A list of repositories for citable data storage.
Repository name        URL                          Size limits                              Fee/Costs
Dryad Digital          https://datadryad.org/       No                                       $120 USD for first 20 GB, and $50 USD for each additional
Repository             stash                                                                 10 GB
figshare               https://figshare.com/        1 TB per dataset                         It varies with publishers
Harvard Dataverse      https://dataverse.harvard.   2.5 GB per file, 10 GB per dataset       Free
                       edu/
Open Science           https://osf.io/              5 GB per file, multiple files can be     Free
Framework                                           uploaded
Zenodo                 https://zenodo.org/          50 GB per dataset                        Donation
Mendeley Data          https://data.mendeley.       10 GB per dataset                        Free
                       com/


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                33 of 69



                                    building the infrastructure for acquiring, archiving and disseminating the models and the data. To
                                    conclude, a database assures appropriate documentation with a defined format and quality control
                                    of the results.
                                       Given the importance of integrative structures for advancing life sciences and the significant
                                    world-wide investment made to determine them, the wwPDB has proposed a governance structure
                                    for federating archives containing structural models (e.g., PDB, Electron Microscopy Data Bank,
                                    EMDB Tagari et al., 2002) or experimental data. Moreover, for integrative modeling integrative/
                                    hybrid modeling structures (Sali et al., 2015), PDB-Dev (Berman et al., 2019; Vallat et al., 2018)
                                    was established as an associated prototype system for archiving multi-state and ensemble structures
                                    on multiple spatial scales. In addition, associated kinetic models can be deposited.
                                       To deposit structural models and kinetic networks obtained using FRET experiments in PDB-Dev,
                                    a dictionary for FRET data is under development (https://github.com/ihmwg/FLR-
                                    dictionary; Vallat et al., 2020), serving as a method-specific extension to the existing integrative/
                                    hybrid modeling (IHM) dictionary that contains the data categories described in Figure 8. Presently,
                                    three integrative FRET-assisted structural models can be found on PDB-Dev.
                                       In addition to archiving the models themselves, all relevant experimental data and metadata
                                    should be archived in a technique-associated data bank similar to the Biological Magnetic Resonance
                                    Data Bank, BMRB (Ulrich et al., 2019; Ulrich et al., 2008). Reaching such a consensus is possible, as
                                    has been demonstrated by the acceptance of a single file format for the deposition of NMR data
                                    (Ulrich et al., 2019). In the future, federated resources for other biophysical techniques are
                                    expected to align with the structural model archives of the wwPDB for participating in data
                                    exchange. Thus, it would be desirable to establish a federated data bank for archiving FRET and,
                                    more generally, fluorescence data that could be referred to as the Fluorescence Data Bank (FLDB).


                                    Community actions to bring FRET scientists together
                                    To better achieve a consensus on the current and the future directions of the smFRET community,
                                    an open forum is needed where the current issues, needs, and desires could be discussed. We pro-
                                    pose the following tools to organize the community around standardization efforts and open science
                                    practices. Some of these tools have already been put in place.

                                    Community website as a central hub
                                    A website for the FRET community has been established at https://www.fret.community. The com-
                                    munity is open to everybody and registered members can populate their user profiles with addi-
                                    tional information such as a description of their scientific interests or a list of key-publications.
                                    Besides providing regular updates on the activities within the community, the website also provides
                                    resources such as a curated list of software packages (see Table 1) and offers a discussion platform
                                    through an integrated forum. The website serves as a platform for ongoing discussions, announce-
                                    ments of accepted relevant papers, notifications about upcoming meetings, workshops, competi-
                                    tions and other activities that might be relevant to the community. An advisory board, elected by
                                    the community, moderates the website. One can also envision adding an educational section, much
                                    like the popular website for general microscopy education (https://micro.magnet.fsu.edu).

                                    Listserv
                                    To facilitate the dissemination of important information to the FRET community, an electronic mail-
                                    ing list (Listserv) has been established. In order to subscribe to it, smFRET practitioners are
                                    requested to register (free of charge) using the following link: https://www.fret.community/register.
                                    The members will be informed through the email list about ongoing activities and developments
                                    within the community, such as experimental or computational challenges, key publications in the
                                    fields, and workshops or meetings.

                                    Server and repository
                                    A repository will be established, which will be accessible through the community website, to host a
                                    collection of software packages and facilitate the community-driven joint development of analysis
                                    tools. The repository will contain dedicated sections for acquisition software, raw data, analysis


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            34 of 69



                                    codes, analyzed data files, and file conversion utilities. In order to deposit code in the repository,
                                    guidelines for the required documentation will be provided.
                                       The concept of the repository is to support open science and transparency. Anyone registered on
                                    the website will be able to access raw data, and analyze and compare performances of the various
                                    analysis codes. Moreover, the codes can be updated and expanded (while keeping original versions)
                                    by anyone. In this way, improvements and enhancements can be implemented and tested. In that
                                    context, it is important to mention that such a repository can also serve the purpose of source data
                                    deposition, nowadays required by many scientific journals.

                                    Participation in CASP(-like) competitions
                                    Critical Assessment of protein Structure Prediction (CASP, http://predictioncenter.org/) is a grass-
                                    roots effort for predicting a three-dimensional protein structure from its amino acid sequence. CASP
                                    has been run, since 1994, as a double-blind competition. It provides research groups with an oppor-
                                    tunity to test their structure prediction methods objectively. CASP has been exploring modeling
                                    methods based, in part, on sparse experimental data, including data from SAXS, NMR, crosslinking,
                                    and FRET. This integrative CASP experiment was highlighted at the recent CASP13 meeting (http://
                                    www.predictioncenter.org/), where the carbohydrate-binding module (CBM56) of a b 1,3-glucanase
                                    from Bacillus circulans with 184 amino acids (18.9 kDa) was studied as the first FRET data-assisted
                                    target F0964. In CASP14, the single-model protein structure prediction by the artificial intelligence
                                    (AI) network AlphaFold2, which was developed by Google’s AI offshoot DeepMind (https://deep-
                                    mind.com), has approached perfection (Callaway, 2020). This deep-learning program combines the
                                    evolutionary information from multiple sequence alignments with structural information from the
                                    PDB for computing 3D structural models of a protein from its amino-acid sequence.
                                       However, one has to be aware that many proteins do not only adopt their thermodynamically
                                    most stable conformation but frequently exist as ensembles of conformations that have high func-
                                    tional relevance. Thus, mapping dynamic ensembles represents the subsequent challenge of struc-
                                    tural biology for the next decades. Due to their high time-resolution, smFRET-studies and
                                    integrative modeling can contribute a lot to solving this problem. We propose that members of the
                                    smFRET community who are interested in using smFRET for integrative structural biology participate
                                    in the CASP competition. Involvement could progress in several stages: (1) Predicting single- and
                                    multi-state structural models: the smFRET community will only submit distances that will be evalu-
                                    ated with respect to the known (but undisclosed) crystal structure(s). (2) Predicting ensembles as in
                                    the case of CBM56: for targets that are identified as difficult by the predictors and for which multiple
                                    possible folds are submitted without a clear winner, a FRET-assisted round could be insightful where
                                    the FRET distances distributions can be used as an experimental ‘ground truth’ for checking whether
                                    multiple conformations in an exchange are present.
                                       These recommendations apply mostly to present and future practitioners of smFRET-driven inte-
                                    grative modeling. That being said, smFRET is one of many biophysical techniques that can provide
                                    experimental restraints in integrative modeling (XL-MS, single-particle cryoEM, NMR, SAXS). There-
                                    fore, we propose that, at a later stage, an all-biophysics integrative structural biology competition
                                    be established.

                                    SmFRET meetings
                                    Several gatherings of FRET practitioners at the Annual Biophysical Society Meetings, supported by
                                    the Biological Fluorescence subgroup, provided a platform for planning future activities and estab-
                                    lishing the FRET community. As further joint actions, satellite meetings to the Conference on Meth-
                                    ods and Applications in Fluorescence (MAF) have been organized to discuss practices, standards,
                                    competitions, and joint publications. We envision an occasional dedicated meeting for the smFRET
                                    community, such as the Bunsen meetings on FRET held in 2011 and the international discussion
                                    meeting in 2016 at the Max Planck Institute for Biophysical Chemistry in Göttingen, Germany (http://
                                    fret.uni-duesseldorf.de/cms/home.html). However, to open these meetings to smFRET practitioners
                                    outside of Europe, we propose to rotate the venue among continents. We also suggest using the
                                    satellite meetings and workshops to disseminate information (details of accurate FRET measure-
                                    ments, common practices, standards and competitions) and to give newcomers the chance to inter-
                                    act with the experienced researchers in the field.


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            35 of 69



                                       Inspired by the online seminars emerging in response to the COVID-19 pandemic, smFRET webi-
                                    nars and web conferences open to all should be pursued. They provide FRET researchers the unique
                                    opportunity to attend and socialize virtually and would be a forum for good scientific practice of
                                    open science for the FRET community.

                                    Special issues in journals
                                    To further stimulate newcomers to engage in advanced smFRET experiments, the FRET community
                                    could benefit by hosting special issues in journals dedicated to data analyses (e.g., Data in Brief,
                                    Methods in Molecular Biology, or Nature Protocols). Here, various laboratories can describe typical
                                    datasets or protocols for the methods they have developed. Also, journals disseminating methodolo-
                                    gies and protocols from A-to-Z via video recordings could be useful. For example, there is a special
                                    issue focusing on FRET planned in the Journal of Visualized Experiments (https://www.jove.com/
                                    methods-collections/682).


                                    Future of smFRET
                                    With improved communication and dissemination within the FRET community and agreement on the
                                    standard information required for depositing FRET-based or integrative structural data, smFRET will
                                    be better positioned to impact the expanding field of dynamic structural biology. We expect inte-
                                    grated approaches such as combining smFRET with NMR (Aznauryan et al., 2016; Liu et al., 2018;
                                    Milles et al., 2015; Sottini et al., 2020; Tsytlonok et al., 2019; Voith von Voithenberg et al.,
                                    2016), EPR (Boura et al., 2011; Masliah et al., 2018; Peter et al., 2020; Peulen et al., 2020;
                                    Sanabria et al., 2020; Vöpel et al., 2014), cross-linking mass spectrometry (Calabrese et al., 2020;
                                    Liu et al., 2018; Tyagi and Lemke, 2015), hydrogen/deuterium exchange (Calabrese et al., 2020;
                                    Liu et al., 2018; Munro and Lee, 2018), and/or MD simulations (see section Structural modeling
                                    and below) will have a big impact in the future.
                                        One example of a major area of interest that is profiting from these developments is the study of
                                    intrinsically disordered proteins using smFRET experiments (Gomes and Gradinaru, 2017;
                                    Gomes et al., 2020; LeBlanc et al., 2018; Lee et al., 2018; Metskas and Rhoades, 2020;
                                    Nasir et al., 2020; Schuler et al., 2016). The dynamic nature of these proteins and their interactions
                                    play major roles in numerous cellular processes, including the formation of membrane-less intracellu-
                                    lar biomolecular condensates, a new paradigm that presents huge challenges for traditional tools of
                                    structural biology (Banani et al., 2017; Choi et al., 2020; van der Lee et al., 2014; Wright and
                                    Dyson, 2015). Many IDPs undergo large folding transitions in conjunction with binding to partners,
                                    while others remain disordered upon complex formation (Schuler et al., 2020; Wang and Wang,
                                    2019; Wu et al., 2017). SmFRET studies of these systems began more than a decade ago and have
                                    tackled increasingly complex systems using more advanced methods, including three-color smFRET
                                    or complex labeling schemes (Borgia et al., 2018; Kim and Chung, 2020; Lee et al., 2018;
                                    Metskas and Rhoades, 2020; Milles et al., 2015; Nasir et al., 2019; Schuler et al., 2016;
                                    Yoo et al., 2020). A recent study that combined smFRET, NMR, and MD simulations to investigate
                                    the interaction of H1 with ProTa is highlighted in Figure 9 (Borgia et al., 2018).
                                        Studies of IDPs are even more challenging in heterogeneous environments such as phase-sepa-
                                    rated mesoscale structures (e.g., membrane-less organelles) or cells (Nasir et al., 2019). Here, the
                                    strengths of smFRET would be especially valuable, while the field, at the same time, will benefit from
                                    the methodological developments. The ultimate goal is to combine both the structural and dynamic
                                    information in order to reduce the ambiguity in the underlying structures of conformational states
                                    and to gain detailed information on kinetic pathways between the associated states.
                                        Although we have focused mostly on kinetic studies, smFRET-based structure determination and
                                    structural dynamics in this paper, there are a myriad of other new exciting directions where smFRET
                                    will have future impact. A detailed description of the various possibilities is beyond the scope of this
                                    report, but it is worth mentioning a few of them below.
                                       .   Combining FRET with other fluorescence methods: Several groups have combined smFRET
                                           with other fluorescence techniques, including protein-induced fluorescence enhancement
                                           (PIFE) (Hwang et al., 2011; Hwang and Myong, 2014; Lerner et al., 2016; Ploetz et al.,
                                           2016), photoinduced electron transfer (PET) (Haenni et al., 2013), quenchable
                                           FRET (Cordes et al., 2010) and stacking-induced fluorescence increase (SIFI) (Morten et al.,


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            36 of 69


             Review Article                                                                                                   Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics


         A                                                         Experiment                                                      B               Simulation
                                2                                        56
                                                                                               110                                                              PC1

              -1                              0.38                   0.58            0.55


                                              0.45                   0.69            0.63


         104 89                                                                                                                                     3


                                                                                                   Relative event frequency
                                              0.48                   0.83            0.73
                                              0.46                   0.83            0.70
                    151                       0.46                   0.86            0.68                                                                   6

                                                                                                                                     PC2                                       PC3
                                              0.49                   0.87            0.71                                                                                 11

                                              0.44                   0.77            0.66

                                    0   0.5              1 0     0.5     1 0            0.5    1
                                                          Transfer e ciency


                                         C                         1.0
                                                                                  Experiment                                         Simulation
                                                                   0.9
                                                                   0.8


                                               Transfer e ciency
                                                                   0.7
                                                                   0.6
                                                                   0.5
                                                                   0.4
                                                                   0.3
                                                                   0.2        +    +                                                 +
                                                                                               +                                               +
                                                                   0.1
                                                                    0        P2 − P56
                                                                          P56− P110
                                                                           P2 − P110
                                                                             P2 − H-1
                                                                             P2 − H89
                                                                           P2 − H104
                                                                           P2 − H113
                                                                            P2 − H151
                                                                           P2 − H161
                                                                           P2 − H194
                                                                           P56− H-1
                                                                           P56 − H89
                                                                          P56 − H104
                                                                          P56 − H113
                                                                          P56 − H151
                                                                          P56 − H161
                                                                          P56 − H194
                                                                          P110 − H-1
                                                                          P110− H89
                                                                         P110− H104
                                                                         P110− H113
                                                                         P110− H151
                                                                         P110− H161
                                                                         P110− H194
                                                                          H-1 − H113
                                                                          H-1− H194
                                                                         H104− H194
                                                                         H113− H194


Figure 9. Using smFRET to investigate the structure and dynamics of ultrahigh-affinity IDP complexes. (A) SmFRET efficiency histograms for FRET
between a donor label (Alexa488) attached at various positions to the linker histone H1 (shown in blue) with the IDP ProTa (shown in red) labeled at
different positions with the acceptor fluorophore (Alexa594). (B) For structural calculations of the H1-ProTa complex, coarse-grained MD simulations
were performed. From the MD simulations, an ensemble of structures was determined. Eleven examples of configurations are shown and projected
onto the first three principle components (PC1, PC2, and PC3) of the inter-residue distance map. 2D projections of the full ensemble are shown in gray
(axes are labeled in Å). (C) A comparison of the experimental FRET efficiencies (filled squares) and the FRET efficiencies estimated from simulated
structures (open circles) shows good agreement between the measured and simulated values. Pictograms indicate the variations of dye positions
studied. (Panels A, B, and C: Copyright 2018, Nature Publishing Group, a division of Macmillan Publishers Limited. All rights reserved. Reproduced from
Borgia et al., 2018, with permission. Further reproduction of this panel would need permission from the copyright holder.)
Ó 2018, Macmillan Publishers Limited, part of Springer Nature. All rights reserved. Panels A-C were originally published as Figure 3i, 4c and 4a in
Borgia et al., 2018. Further reproduction of this panel would need permission from the copyright holder


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                                                                      37 of 69



                                           2020). The advantages of combining smFRET with other fluorescence-based rulers with higher
                                           sensitivity at short distances are obvious – gaining more spatial information on biomolecular
                                           systems being measured as well as information on possible synchronized motions between dif-
                                           ferent parts of the biomolecule or biomolecular complex and between different modes of
                                           motion. As an example, single-molecule PIFE was used for probing the local structural stabili-
                                           zation in the intrinsically disordered protein a-Synuclein (Chen et al., 2020), which typically
                                           appears globally disordered when measured over larger distances using smFRET experiments.
                                           Another possibility is combining FRET with information regarding the shape of biomolecules
                                           and their assemblies via their translational (Dertinger et al., 2008; Sherman and Haran, 2006)
                                           and rotational diffusion (Möckel et al., 2019; Pieper and Enderlein, 2011; Viegas et al.,
                                           2020), determined using various FCS modalities. Recently, fluorescence anisotropy- and polari-
                                           zation-resolved FCS were used in integrative studies with non-FRET methods to probe local
                                           flexibilities (Möckel et al., 2019) or identify hinge-regions of a protein (Tsytlonok et al., 2020;
                                           Tsytlonok et al., 2019).
                                       .   Combining FRET with force spectroscopy. Another popular combination is FRET with various
                                           manipulation methods including optical tweezers (Hohng et al., 2007), magnetic tweezers
                                           (Lee et al., 2010a; Long et al., 2016; Swoboda et al., 2014), tethered particle motion
                                           (May et al., 2014), and force spectroscopy by DNA origami (Nickels et al., 2016). The advan-
                                           tages of combining smFRET with force manipulation techniques are obvious – detecting local
                                           structural changes or molecular interactions (via smFRET) as well as the global extension of
                                           macromolecules (via bead tracking) synchronously under mechanical control.
                                       .   Combining FRET with MD simulations. MD simulations have been widely applied with smFRET
                                           experiments to provide atomistic insights into the dynamic behavior of biomolecules and their
                                           assemblies, as shown in Figure 9 (Barth et al., 2018; Borgia et al., 2018; Holmstrom et al.,
                                           2018; Lehmann et al., 2020; Matsunaga and Sugita, 2018; Tsytlonok et al., 2020;
                                           Yanez Orozco et al., 2018; Zhao et al., 2010b). The vast information provided by MD simula-
                                           tions often motivates new hypotheses about the functional mechanism that can be tested
                                           experimentally via targeted mutations. MD simulations can also be combined with the informa-
                                           tion provided by smFRET experiments to steer the simulation from one conformational state
                                           to the other using accelerated or enhanced sampling techniques (Dimura et al., 2020). To
                                           characterize highly dynamic systems, coarse-grained approaches have been applied to intrinsi-
                                           cally disordered proteins (Borgia et al., 2018), nucleic acids (Craggs et al., 2019), large chro-
                                           matin arrays (Kilic et al., 2018) or large DNA origami nanostructures (Bartnik et al., 2020;
                                           Khara et al., 2018), to sample the conformational space of the system more efficiently. Alter-
                                           natively, discrete MD simulations coupled with replica exchange, where discretized potential
                                           energies are employed, also assist in accelerating atomistic MD simulations of the ensemble
                                           structure of intrinsically disordered proteins (Brodie et al., 2019; Brodie et al., 2017;
                                           Chen et al., 2020; Fay et al., 2016; Hadi-Alijanvand et al., 2016; Popov et al., 2019) and
                                           holds great promises for being incorporated with single-molecule fluorescence-based
                                           technique.
                                       .   Combining FRET with imaging. SmFRET can be combined with super-resolution imaging
                                           (STED-FRET, Kim et al., 2018b; Tardif et al., 2019; Szalai et al., 2021) or FRET-DNA-PAINT
                                           (Deußner-Helfmann et al., 2018; Filius et al., 2020). The combination of fluorescence imag-
                                           ing with spectroscopy makes it possible to detect more species within a pixel of an image,
                                           expanding the information that can be extracted from such an experiment. Correlative imag-
                                           ing with electron microscopy, fluorescence and FRET also has the potential to allow the recog-
                                           nition of different subpopulations in the sample, which can then be separated for single-
                                           particle reconstructions (Ando et al., 2018; de Boer et al., 2015; Schirra and Zhang, 2014;
                                           Verkade and Collinson, 2019).
                                       .   SmFRET in live cells. Genetically-encoded fluorescent proteins are the most widely used fluoro-
                                           phores in live-cell imaging. Their maximal brightness and photon yield are, however, limited
                                           by excitation-dependent blinking and photobleaching, respectively (Dickson et al., 1997;
                                           Seefeldt et al., 2008). Combined with their large size, this makes them non-ideal for quantita-
                                           tive FRET studies. Nevertheless, considerable efforts have been made to extract quantitative
                                           FRET information to live-cell imaging data using the fluorescence intensity (Coullomb et al.,
                                           2020; Periasamy et al., 2008) or lifetime and anisotropy information (Hinde et al., 2012;
                                           Kravets et al., 2016; Kudryavtsev et al., 2007; Liput et al., 2020; Weidtkamp-Peters et al.,
                                           2009), and to develop an appropriate dye model for fluorescent proteins (Greife et al.,
                                           2016). Recently, the green fluorescent protein has been used for in-cell smFRET measure-
                                           ments in combination with an organic dye attached via the self-labeling protein tag (HaloTag)
                                           (Okamoto et al., 2020). To avoid the drawbacks of fluorescent proteins, several groups have


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            38 of 69



                                           shown that smFRET can be performed in live bacterial and eukaryotic cells by using in vitro
                                           labeled biomolecules that can be internalized in cells by several means. Electroporation has
                                           been shown to work well for the internalization of ssDNA, dsDNA, tRNA and proteins into bac-
                                           teria and yeast cells (Craggs et al., 2019; Plochowietz et al., 2017; Plochowietz et al., 2016;
                                           Plochowietz et al., 2014; Sustarsic et al., 2014; Volkov et al., 2018). Microinjection of
                                           labeled molecules is an alternative approach, especially for smFRET in live eukaryotic cells, and
                                           has been demonstrated to yield structural information and dynamics from nanoseconds to
                                           milliseconds (König et al., 2015; Sakon and Weninger, 2010). With the further development
                                           of probes and labeling strategies, and the engineering of better fluorescent proteins
                                           (Shaner et al., 2007), there are many exciting possibilities for investigating cellular processes
                                           with unprecedented detail (Sustarsic and Kapanidis, 2015).
                                       .   SmFRET studies in crowded environments. SmFRET can be used to investigate the influence of
                                           the surrounding environment on biomolecules. Such studies can be performed over a drastic
                                           range of measurement conditions: from single molecules isolated in solvent cages to molecular
                                           environments equivalent to cellular conditions with millimolar concentrations of crowded bio-
                                           molecules. An important thermodynamic effect of the limited space is minimization of the
                                           excluded volume. This (i) influences the hydrodynamic volume of biomolecules with potential
                                           consequences for their internal structure, dynamics and functionality and (ii) favors the associa-
                                           tion state in binding equilibria leading to phase transitions (Banani et al., 2017;
                                           Kuznetsova et al., 2014). The profound experimental impact of crowding was confirmed by
                                           computer simulations (Nawrocki et al., 2019; Sugita and Feig, 2020) and experimental stud-
                                           ies (Gao et al., 2016; Gnutt et al., 2015; Guin and Gruebele, 2019; Möckel et al., 2019;
                                           Nasir et al., 2019; Neubauer et al., 2007; Reinkemeier et al., 2019; Zosel et al., 2020b)
                                           using labeled molecules as tracers even down to the single-molecule level. In the context of liv-
                                           ing cells, biomolecular condensates formed by liquid-liquid phase separation have recently
                                           been recognized as an important mechanism to spatially organize complex biochemical reac-
                                           tions in membrane-less organelles within the cytoplasm or nucleus (Banani et al., 2017;
                                           Hyman et al., 2014). We envision that smFRET studies, especially in combination with integra-
                                           tive experimental approaches, will play a central role in uncovering the dynamic organization
                                           and interactions within phase-separated droplets in vitro and in living cells.
                                       .   In vitro smFRET of membrane proteins. One class of proteins that remains understudied by
                                           structural biology in general is membrane proteins, owing to the complexity of membrane pro-
                                           tein production, stabilization and crystallization. As smFRET requires only low amounts of pro-
                                           tein to be produced and is performed under experimental conditions that potentially limit
                                           solubility issues, it serves a vital role here. Indeed, in recent years, smFRET is increasingly being
                                           used to study a variety of membrane proteins, including G-protein-coupled receptors
                                           (Gregorio et al., 2017; Olofsson et al., 2014), transporters (Akyuz et al., 2013; Ciftci et al.,
                                           2020; Dyla et al., 2017; Fitzgerald et al., 2019; Husada et al., 2018; Terry et al., 2018), and
                                           ion channels (Bavi et al., 2016; Wang et al., 2016; Wang et al., 2014). For some recent
                                           reviews, see Husada et al., 2015; Martinac, 2017; Quast and Margeat, 2019. However,
                                           membrane proteins in a living cell are surrounded by specific lipids, proteins, ion gradients
                                           and an electric membrane potential. In addition to investing in intracellular smFRET assays, an
                                           important challenge for in vitro smFRET on membrane proteins is to further develop ‘cell-mim-
                                           icking’ assays.
                                       .   SmFRET between multiple chromophores. By measuring the transfer of excitation energy
                                           between three or more spectrally different fluorophores, multiple distances are obtained
                                           simultaneously, and the correlation of the distances can be determined. Following early
                                           ensemble implementations (Haustein et al., 2003; Horsey et al., 2000; Ramirez-Carrozzi and
                                           Kerppola, 2001; Watrob et al., 2003; Yim et al., 2012), three- and four-color smFRET experi-
                                           ments have been applied to various static (Clamme and Deniz, 2005; Lee et al., 2007b;
                                           Stein et al., 2011) and dynamic systems (Ferguson et al., 2015; Götz et al., in preparation;
                                           Hohng et al., 2004; Lee et al., 2010c; Lee et al., 2010b; Morse et al., 2020; Munro et al.,
                                           2010; Ratzke et al., 2014; Vušurović et al., 2017; Wasserman et al., 2016). FRET to many
                                           acceptors has also been reported (Krainer et al., 2015; Uphoff et al., 2010). Multi-color FRET
                                           experiments, however, remain challenging, in particular for diffusion-based experiments,
                                           because of the increased shot-noise, and the more complex FRET efficiency calculations and
                                           corrections. Recent advances in this respect include the development of a photon distribution
                                           analysis for three-color FRET to extract three-dimensional distance distributions (Barth et al.,
                                           2019) and a maximum likelihood approach applied to the study of fast protein folding
                                           (Kim and Chung, 2020; Yoo et al., 2020; Yoo et al., 2018). Further progress in multiple-chro-
                                           mophore smFRET will require expanding the useable spectral range to the near infra-red


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            39 of 69



                                           (which requires better fluorophores and detectors in that region) and measurement of the sin-
                                           gle-molecule spectra (Lacoste et al., 2000; Squires and Moerner, 2017) rather than the use
                                           of individual channels.
                                       .   SmFRET with nanomaterials. Emerging structurally synthesized and targeted specific nanoma-
                                           terials such as quantum dots (QDs) (Jamieson et al., 2007), aggregation-induced emission
                                           (AIE) nanoparticles (Hong et al., 2011), and nitrogen-vacancy centers in diamond
                                           (Schirhagl et al., 2014; Tisler et al., 2011) have made it possible to implement chemically
                                           engineered fluorophores for a wide range of applications in structural biology investigations
                                           and, more specifically, in FRET-related studies (Börsch et al., 2009; Medintz et al., 2003;
                                           Oh et al., 2005; Shi et al., 2006; Soleimaninejad et al., 2017).
                                       .   SmFRET with plasmonics. Placing fluorescent dyes close to metallic nanostructures in ‘plas-
                                           monic hotspots’ increases the detectable signal of a single molecule into the megahertz region
                                           (Acuna et al., 2012; Grabenhorst et al., 2020). Recent work has shown the possibility of plas-
                                           mon-assisted FRET (Baibakov et al., 2020; Baibakov et al., 2019; Bohlen et al., 2019). Excit-
                                           ingly, it has recently been shown that tryptophan fluorescence of proteins can be detected
                                           with single-molecule resolution in zero-mode waveguides (Barulin et al., 2019), paving the
                                           way toward studies using intrinsic labels.


                                    Epilogue
                                    In this article, we have summarized current perspectives on the status of the smFRET field, limitations
                                    that still need to be overcome, and joint efforts towards the adoption of consistent methodologies
                                    and open-science practices. While this article encourages a discussion regarding optimal smFRET
                                    practices, it is important to remember that, as scientists, we should value independence of thought
                                    and creativity. Hence, our recommendations should be taken as constructive suggestions, and it is
                                    important to realize that many biological questions can be answered using multiple approaches. On
                                    the one hand, the reproducibility and reliability of smFRET measurements are currently limited by
                                    the variety of approaches taken to calculate the FRET efficiency and the resulting inter-dye distance.
                                    Combining years of experience from various experts in an open discussion can help us, as a commu-
                                    nity, to improve the methodology and overcome many of its challenges. On the other hand, it is
                                    important to be open to new ideas and approaches. Here is where open scientific practices can help
                                    the community to quickly exchange data and analysis approaches to test new ideas. Such a commu-
                                    nity effort is necessary to consolidate the role of smFRET as a useful tool in various fields and to
                                    jointly move the field forward. Our hope is that these efforts will benefit not only the smFRET com-
                                    munity, but also the structural biology community and science in general.


                                    Acknowledgements
                                    We wish to thank Niko Hildebrandt and Sonja Schmid for fruitful discussions. We thank Niels Van-
                                    denberk, KU Leuven for use of a figure from his PhD thesis, and Bianca Herman, Universität Freiburg,
                                    for providing material for Figure 6. RB wishes to thank Fabio D Steffen for insightful discussions.
                                    This position paper was supported by the National Institutes of Health (NIH, grant R01 GM130942
                                    to SW, and to EL as a subaward; grant R01 GM095904 to XM; grants R01 GM079238 and
                                    7R01GM098859-09 to SCB; grants R01 GM084288 and R01 GM137608 to RLG; grant R01
                                    GM112882 to HDK; grants R01 GM123164 and R01 GM130793 to THL; grant R01 GM140272 to RV;
                                    grant R35 GM130375 to AAD; New Innovator Award 1DP2GM128185-01 to JF), the Intramural
                                    Research Program of the National Institute of Diabetes and Digestive and Kidney Diseases, NIH (to
                                    HSC and IVG), the National Science Foundation (NSF, grants MCB-1818147 and MCB-1842951 to
                                    SW; grant CHE-2004016 to RLG), the Human Frontier Science Program (HFSP, grant RGP0061/2019
                                    to SW), the European Research Council (ERC; grant numbers 638536 and 860954 to TC; grant
                                    SMPFv2.0 to EAL; grant No. 671208 (hybridFRET) to CAMS; grant No. 819299 to CJ), the Deutsche
                                    Forschungsgemeinschaft (DFG, grants GRK2062 (C03) and SFB863 (A13) to TC; grant (PL696/4-1) to
                                    EP; grants SPP2191 402723784 and SFB 1129 240245660 to EAL; grant SE 1195/21–1 (SPP 2191) to
                                    CAMS; Germany’s Excellence Strategy, CIBSS – EXC-2189 – project ID 390939984 to T Hugel), the
                                    Wellcome Trust (grant 110164/Z/15/Z to AK), the Swiss National Science Foundation (to BS), the UK
                                    Biotechnology and Biological Sciences Research Council (grant BB/S008896/1 to AK; grant BB/
                                    T008032/1 to TDC), the Royal Society (grant RGS\R2\180405 to TDC; grants DKR00620 and RGF\R1


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            40 of 69


           Review Article                                            Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics

                                    \180054 to NCR), the Agence Nationale de la Recherche (grants ANR-17-CE09-0026-02, ANR-18-
                                    CE11-0004-02 and ANR-19-CE44-0009-02 to EM), the Israel Science Foundation (ISF, grant 1250/19
                                    to GH; grant 3565/20 within the KillCorona – Curbing Coronavirus Research Program to EL), the
                                    National Research Foundation of Korea (grant 2019R1A2C2090896 to NKL; grant NRF-
                                    2019R1A2C2005209 to SH, grant NRF-2019R1A2C1089808 to SCH.), the Independent Fund Den-
                                    mark (grant 6110-00623B to VB), the National Key R and D Program from the Ministry of Science
                                    and Technology of China (grant 2018YFA0507700 to CT), the Milner Fund (to EL), the Hebrew Uni-
                                    versity of Jerusalem (start-up funds to EL), the DFG SFB1035, project A11 and Ludwig Maximillian
                                    Universität (LMU, the LMUinnovativ program BioImaging Network, BIN and Center for NanoScience
                                    (CeNS)) to DCL, the Biological Optical Microscopy Platform (BOMP) at University of Melbourne (to
                                    HS), the Searle Scholars Program (to JF), the University of Applied Sciences Mittweida and the
                                    Alfred-Werner-Legat of the Department of Chemistry, University Zurich (financial support to RB), the
                                    EPSRC DTP Studentship (to BA), the UHasselt BOF fund (R-10789 to JH), KU Leuven
                                    Special Research Fund (C14/16/053 to JH) and the CASLMU fellowship (to TC, SW, EL). Carlsberg
                                    Foundation Distinguished Associate Professor program CF16-0797, the Villum Foundation Center of
                                    Excellence BIONEC (grant 18333), and Novo Nordisk Foundation (grant NNF14CC0001) to Novo
                                    Nordisk Foundation Center for Protein Research (for NSH). GH holds the Hilda Pomeraniec Memorial
                                    Professorial Chair. This work was performed under the auspices of the U.S. Department of Energy
                                    by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344 (for TL).


                                    Additional information
                                    Funding
                                    Funder                           Grant reference number     Author
                                    National Institutes of Health    GM130942                   Eitan Lerner
                                                                                                Shimon Weiss
                                    National Institutes of Health    GM095904                   Xavier Michalet
                                    National Institutes of Health    GM079238                   Scott C Blanchard
                                    National Institutes of Health    GM098859                   Scott C Blanchard
                                    National Institutes of Health    GM084288                   Ruben L Gonzalez
                                    National Institutes of Health    GM137608                   Ruben L Gonzalez
                                    National Institutes of Health    GM112882                   Harold D Kim
                                    National Institutes of Health    GM123164                   Tae-Hee Lee
                                    National Institutes of Health    GM130793                   Tae-Hee Lee
                                    National Institutes of Health    GM140272                   Reza Vafabakhsh
                                    National Institutes of Health    GM130375                   Ashok A Deniz
                                    National Institutes of Health    128185                     Jingyi Fei
                                    National Institute of Diabetes                              Hoi Sung Chung
                                    and Digestive and Kidney Dis-                               Irina V Gopich
                                    eases
                                    National Science Foundation      1818147                    Shimon Weiss
                                    National Science Foundation      1842951                    Shimon Weiss
                                    National Science Foundation      2004016                    Ruben L Gonzalez
                                    Human Frontier Science Pro-      RGP0061/2019               Shimon Weiss
                                    gram
                                    European Research Council        638536                     Thorben Cordes
                                    European Research Council        860954                     Thorben Cordes
                                    European Research Council        SMPFv2.0                   Edward A Lemke
                                    European Research Council        671208                     Claus AM Seidel


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                             41 of 69



                                    European Research Council       819299                       Chirlmin Joo
                                    Deutsche Forschungsge-          GRK2062                      Thorben Cordes
                                    meinschaft
                                    Deutsche Forschungsge-          SFB863                       Thorben Cordes
                                    meinschaft
                                    Deutsche Forschungsge-          PL696/4-1                    Evelyn Ploetz
                                    meinschaft
                                    Deutsche Forschungsge-          SPP2191 402723784            Edward A Lemke
                                    meinschaft
                                    Deutsche Forschungsge-          SFB 1129 240245660           Edward A Lemke
                                    meinschaft
                                    Deutsche Forschungsge-          SE 1195/21-1 (SPP 2191)      Claus AM Seidel
                                    meinschaft
                                    Deutsche Forschungsge-          CIBSS - EXC-2189 - project   Thorsten Hugel
                                    meinschaft                      ID 390939984
                                    Wellcome Trust                  110164/Z/15/Z                Achillefs N Kapanidis
                                    Swiss National Science Foun-                                 Benjamin Schuler
                                    dation
                                    Biotechnology and Biological    BB/S008896/1                 Achillefs N Kapanidis
                                    Sciences Research Council
                                    Biotechnology and Biological    BB/T008032/1                 Timothy D Craggs
                                    Sciences Research Council
                                    Royal Society                   RGS\R2\180405                Timothy D Craggs
                                    Royal Society                   DKR00620                     Nicole C Robb
                                    Royal Society                   RGF\R1\180054                Nicole C Robb
                                    Agence Nationale de la Re-      ANR-17-CE09-0026-02          Emmanuel Margeat
                                    cherche
                                    Agence Nationale de la Re-      ANR-18-CE11-0004-02          Emmanuel Margeat
                                    cherche
                                    Agence Nationale de la Re-      ANR-19-CE44-0009-02          Emmanuel Margeat
                                    cherche
                                    Israel Science Foundation       1250/19                      Gilad Haran
                                    Israel Science Foundation       3565/20                      Eitan Lerner
                                    National Research Foundation 2019R1A2C2090896                Nam Ki Lee
                                    of Korea
                                    National Research Foundation NRF-2019R1A2C2005209            Sungchul Hohng
                                    of Korea
                                    National Research Foundation NRF-2019R1A2C1089808            Seok-Cheol Hong
                                    of Korea
                                    Independent Fund Denmark        6110-00623B                  Viktoria Birkedal
                                    National Key Research and   2018YFA0507700                   Chun Tang
                                    Development Program of Chi-
                                    na
                                    UHasselt BOF fund               R-10789                      Jelle Hendrix
                                    Deutsche Forschungsge-          SFB1035                      Don C Lamb
                                    meinschaft
                                    Milner Fund                                                  Eitan Lerner
                                    KU Leuven Special Research      C14/16/053                   Jelle Hendrix
                                    Fund
                                    Carlsbergfondet                 CF16-0797                    Nikos S Hatzakis
                                    Villum Fonden                   18333                        Nikos S Hatzakis
                                    Novo Nordisk                    NNF14CC0001                  Nikos S Hatzakis


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            42 of 69


           Review Article                                             Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics

                                    Ludwig-Maximilians-Universität                              Timothy D Craggs
                                    München
                                    Carolina Cancer Center of Na-                                Timothy D Craggs
                                    notechnology Excellence
                                    University of Melbourne                                      Hamid Soleimaninejad
                                    Searle Scholars Program                                      Jingyi Fei
                                    University of Zurich                                         Richard Börner
                                    EPSRC                                                        Benjamin Ambrose

                                    The funders had no role in study design, data collection and interpretation, or the
                                    decision to submit the work for publication.

                                    Author contributions
                                    Eitan Lerner, Shimon Weiss, Wrote the initial draft of the manuscript, coordinated the input from all
                                    authors and discussed the revisions; Anders Barth, Jelle Hendrix, Claus AM Seidel, Expanded the ini-
                                    tial draft, contributed extensively to the writing and revising of the manuscript, and prepared figures;
                                    Benjamin Ambrose, Victoria Birkedal, Scott C Blanchard, Richard Börner, Hoi Sung Chung, Thorben
                                    Cordes, Timothy D Craggs, Ashok A Deniz, Jiajia Diao, Jingyi Fei, Ruben L Gonzalez, Irina V Gopich,
                                    Taekjip Ha, Gilad Haran, Nikos S Hatzakis, Sungchul Hohng, Seok-Cheol Hong, Thorsten Hugel,
                                    Antonino Ingargiola, Chirlmin Joo, Achillefs N Kapanidis, Harold D Kim, Ted Laurence, Nam Ki Lee,
                                    Tae-Hee Lee, Edward A Lemke, Emmanuel Margeat, Jens Michaelis, Xavier Michalet, Sua Myong,
                                    Daniel Nettels, Thomas-Otavio Peulen, Evelyn Ploetz, Yair Razvag, Nicole C Robb, Benjamin Schuler,
                                    Hamid Soleimaninejad, Chun Tang, Reza Vafabakhsh, Contributed to writing the manuscript; Chris-
                                    tian A Hanke, prepared figures and contributed to writing the manuscript; Don C Lamb, Expanded
                                    the initial draft, contributed extensively to the writing and revising of the manuscript

                                    Author ORCIDs
                                    Eitan Lerner     https://orcid.org/0000-0002-3791-5277
                                    Anders Barth       https://orcid.org/0000-0003-3671-3072
                                    Jelle Hendrix      https://orcid.org/0000-0001-5731-1297
                                    Scott C Blanchard        https://orcid.org/0000-0003-2717-9365
                                    Richard Börner      https://orcid.org/0000-0001-8407-6624
                                    Thorben Cordes         https://orcid.org/0000-0002-8598-5499
                                    Timothy D Craggs         https://orcid.org/0000-0002-7121-0609
                                    Jingyi Fei    https://orcid.org/0000-0002-9775-3820
                                    Ruben L Gonzalez         https://orcid.org/0000-0002-1344-5581
                                    Taekjip Ha     https://orcid.org/0000-0003-2195-6258
                                    Gilad Haran      https://orcid.org/0000-0003-1837-9779
                                    Thorsten Hugel        https://orcid.org/0000-0003-3292-4569
                                    Antonino Ingargiola        https://orcid.org/0000-0002-9348-1397
                                    Nam Ki Lee       https://orcid.org/0000-0002-6597-555X
                                    Edward A Lemke          https://orcid.org/0000-0002-0634-0503
                                    Xavier Michalet       https://orcid.org/0000-0001-6602-7693
                                    Evelyn Ploetz      https://orcid.org/0000-0003-0922-875X
                                    Benjamin Schuler        https://orcid.org/0000-0002-5970-4251
                                    Don C Lamb        https://orcid.org/0000-0002-0232-1903
                                    Claus AM Seidel        https://orcid.org/0000-0002-5171-149X
                                    Shimon Weiss        https://orcid.org/0000-0002-0720-5426


                                    References
                                    Acuna GP, Möller FM, Holzmeister P, Beater S, Lalkens B, Tinnefeld P. 2012. Fluorescence enhancement at
                                     docking sites of DNA-directed self-assembled nanoantennas. Science 338:506–510. DOI: https://doi.org/10.
                                     1126/science.1228638, PMID: 23112329


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                              43 of 69



                                    Aitken CE, Marshall RA, Puglisi JD. 2008. An oxygen scavenging system for improvement of dye stability in
                                      single-molecule fluorescence experiments. Biophysical Journal 94:1826–1835. DOI: https://doi.org/10.1529/
                                      biophysj.107.117689, PMID: 17921203
                                    Akyuz N, Altman RB, Blanchard SC, Boudker O. 2013. Transport dynamics in a glutamate transporter
                                      homologue. Nature 502:114–118. DOI: https://doi.org/10.1038/nature12265, PMID: 23792560
                                    Alejo JL, Blanchard SC, Andersen OS. 2013. Small-molecule photostabilizing agents are modifiers of lipid bilayer
                                      properties. Biophysical Journal 104:2410–2418. DOI: https://doi.org/10.1016/j.bpj.2013.04.039,
                                      PMID: 23746513
                                    Altman RB, Terry DS, Zhou Z, Zheng Q, Geggier P, Kolster RA, Zhao Y, Javitch JA, Warren JD, Blanchard SC.
                                      2012. Cyanine fluorophore derivatives with enhanced photostability. Nature Methods 9:68–71. DOI: https://
                                      doi.org/10.1038/nmeth.1774
                                    Ambrose B, Baxter JM, Cully J, Willmott M, Steele EM, Bateman BC, Martin-Fernandez ML, Cadby A, Shewring
                                      J, Aaldering M, Craggs TD. 2020. The smfBox is an open-source platform for single-molecule FRET. Nature
                                      Communications 11:5641. DOI: https://doi.org/10.1038/s41467-020-19468-4, PMID: 33159061
                                    Ando T, Bhamidimarri SP, Brending N, Colin-York H, Collinson L, De Jonge N, de Pablo PJ, Debroye E, Eggeling
                                      C, Franck C, Fritzsche M, Gerritsen H, Giepmans BNG, Grunewald K, Hofkens J, Hoogenboom JP, Janssen
                                      KPF, Kaufman R, Klumpermann J, Kurniawan N, et al. 2018. The 2018 correlative microscopy techniques
                                      roadmap. Journal of Physics D: Applied Physics 51:443001. DOI: https://doi.org/10.1088/1361-6463/aad055,
                                      PMID: 30799880
                                    Andrec M, Levy RM, Talaga DS. 2003. Direct determination of kinetic rates from Single-Molecule photon arrival
                                      trajectories using hidden markov models. The Journal of Physical Chemistry A 107:7454–7464. DOI: https://doi.
                                      org/10.1021/jp035514+, PMID: 19626138
                                    Andrecka J, Treutlein B, Arcusa MA, Muschielok A, Lewis R, Cheung AC, Cramer P, Michaelis J. 2009. Nano
                                      positioning system reveals the course of upstream and nontemplate DNA within the RNA polymerase II
                                      elongation complex. Nucleic Acids Research 37:5803–5809. DOI: https://doi.org/10.1093/nar/gkp601, PMID: 1
                                      9620213
                                    Anhäuser L, Rentmeister A. 2017. Enzyme-mediated tagging of RNA. Current Opinion in Biotechnology 48:69–
                                      76. DOI: https://doi.org/10.1016/j.copbio.2017.03.013, PMID: 28399446
                                    Anthis NJ, Clore GM. 2015. Visualizing transient dark states by NMR spectroscopy. Quarterly Reviews of
                                      Biophysics 48:35–116. DOI: https://doi.org/10.1017/S0033583514000122, PMID: 25710841
                                    Antonik M, Felekyan S, Gaiduk A, Seidel CA. 2006. Separating structural heterogeneities from stochastic
                                      variations in fluorescence resonance energy transfer distributions via photon distribution analysis. The Journal
                                      of Physical Chemistry B 110:6970–6978. DOI: https://doi.org/10.1021/jp057257+, PMID: 16571010
                                    Arbour TJ, Enderlein J. 2010. Application of dual-focus fluorescence correlation spectroscopy to microfluidic
                                      flow-velocity measurement. Lab on a Chip 10:1286–1292. DOI: https://doi.org/10.1039/b924594d
                                    Auer A, Strauss MT, Schlichthaerle T, Jungmann R. 2017. Fast, background-free DNA-PAINT imaging using
                                      FRET-based probes. Nano Letters 17:6428–6434. DOI: https://doi.org/10.1021/acs.nanolett.7b03425, PMID: 2
                                      8871786
                                    Aviram HY, Pirchi M, Mazal H, Barak Y, Riven I, Haran G. 2018. Direct observation of ultrafast large-scale
                                      dynamics of an enzyme under turnover conditions. PNAS 115:3243–3248. DOI: https://doi.org/10.1073/pnas.
                                      1720448115, PMID: 29531052
                                    Aznauryan M, Delgado L, Soranno A, Nettels D, Huang JR, Labhardt AM, Grzesiek S, Schuler B. 2016.
                                      Comprehensive structural and dynamical view of an unfolded protein from the combination of single-molecule
                                      FRET, NMR, and SAXS. PNAS 113:E5389–E5398. DOI: https://doi.org/10.1073/pnas.1607193113,
                                      PMID: 27566405
                                    Baibakov M, Patra S, Claude JB, Moreau A, Lumeau J, Wenger J. 2019. Extending single-molecule Förster
                                      resonance energy transfer (FRET) Range beyond 10 nanometers in zero-mode waveguides. ACS Nano 13:
                                      8469–8480. DOI: https://doi.org/10.1021/acsnano.9b04378, PMID: 31283186
                                    Baibakov M, Patra S, Claude JB, Wenger J. 2020. Long-range single-molecule Förster resonance energy transfer
                                      between Alexa dyes in zero-mode waveguides. ACS Omega 5:6947–6955. DOI: https://doi.org/10.1021/
                                      acsomega.0c00322, PMID: 32258931
                                    Banani SF, Lee HO, Hyman AA, Rosen MK. 2017. Biomolecular condensates: organizers of cellular biochemistry.
                                      Nature Reviews Molecular Cell Biology 18:285–298. DOI: https://doi.org/10.1038/nrm.2017.7, PMID: 28225081
                                    Barth A, Hendrix J, Fried D, Barak Y, Bayer EA, Lamb DC. 2018. Dynamic interactions of type I cohesin modules
                                      fine-tune the structure of the cellulosome of Clostridium thermocellum. PNAS 115:E11274–E11283.
                                      DOI: https://doi.org/10.1073/pnas.1809283115, PMID: 30429330
                                    Barth A, Voith von Voithenberg L, Lamb DC. 2019. Quantitative single-molecule three-color Förster resonance
                                      energy transfer by photon distribution analysis. The Journal of Physical Chemistry B 123:6901–6916.
                                      DOI: https://doi.org/10.1021/acs.jpcb.9b02967
                                    Barth A, Schrimpf W, Hendrix J, Wanninger S, Lamb DC. 2020. PAM – PIE analysis with MATLAB. GitLab. https://
                                      gitlab.com/PAM-PIE/PAM
                                    Bartnik K, Barth A, Pilo-Pais M, Crevenna AH, Liedl T, Lamb DC. 2020. A DNA origami platform for single-pair
                                      Förster resonance energy transfer investigation of DNA-DNA interactions and ligation. Journal of the American
                                      Chemical Society 142:815–825. DOI: https://doi.org/10.1021/jacs.9b09093, PMID: 31800234
                                    Barulin A, Claude JB, Patra S, Bonod N, Wenger J. 2019. Deep ultraviolet plasmonic enhancement of single
                                      protein autofluorescence in Zero-Mode waveguides. Nano Letters 19:7434–7442. DOI: https://doi.org/10.
                                      1021/acs.nanolett.9b03137, PMID: 31526002


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                44 of 69



                                    Bastiaens PI, Majoul IV, Verveer PJ, Söling HD, Jovin TM. 1996. Imaging the intracellular trafficking and state of
                                      the AB5 quaternary structure of cholera toxin. The EMBO Journal 15:4246–4253. DOI: https://doi.org/10.1002/
                                      j.1460-2075.1996.tb00799.x, PMID: 8861953
                                    Baum DA, Silverman SK. 2007. Deoxyribozyme-Catalyzed labeling of RNA. Angewandte Chemie International
                                      Edition 46:3502–3504. DOI: https://doi.org/10.1002/anie.200700357
                                    Bavi N, Cortes DM, Cox CD, Rohde PR, Liu W, Deitmer JW, Bavi O, Strop P, Hill AP, Rees D, Corry B, Perozo E,
                                      Martinac B. 2016. The role of MscL amphipathic N terminus indicates a blueprint for bilayer-mediated gating of
                                      mechanosensitive channels. Nature Communications 7:11984. DOI: https://doi.org/10.1038/ncomms11984,
                                      PMID: 27329693
                                    Bavishi K, Li D, Eiersholt S, Hooley EN, Petersen TC, Møller BL, Hatzakis NS, Laursen T. 2018. Direct observation
                                      of multiple conformational states in cytochrome P450 oxidoreductase and their modulation by membrane
                                      environment and ionic strength. Scientific Reports 8:6817. DOI: https://doi.org/10.1038/s41598-018-24922-x,
                                      PMID: 29717147
                                    Bavishi K, Hatzakis NS. 2014. Shedding light on protein folding, structural and functional dynamics by single
                                      molecule studies. Molecules 19:19407–19434. DOI: https://doi.org/10.3390/molecules191219407, PMID: 2542
                                    Becker W. 2019. The bh TCSPC Handbook, Eighth Edition. Becker & Hickl GmbH.
                                    Beckers M, Drechsler F, Eilert T, Nagy J, Michaelis J. 2015. Quantitative structural information from single-
                                      molecule FRET. Faraday Discussions 184:117–129. DOI: https://doi.org/10.1039/C5FD00110B,
                                      PMID: 26407323
                                    Beechem JM, Haas E. 1989. Simultaneous determination of intramolecular distance distributions and
                                      conformational dynamics by global analysis of energy transfer measurements. Biophysical Journal 55:1225–
                                      1236. DOI: https://doi.org/10.1016/S0006-3495(89)82918-2, PMID: 2765658
                                    Bergström F, Hägglöf P, Karolin J, Ny T, Johansson LB. 1999. The use of site-directed fluorophore labeling and
                                      donor-donor energy migration to investigate solution structure and dynamics in proteins. PNAS 96:12477–
                                      12481. DOI: https://doi.org/10.1073/pnas.96.22.12477, PMID: 10535947
                                    Berman H, Henrick K, Nakamura H. 2003. Announcing the worldwide protein data bank. Nature Structural &
                                      Molecular Biology 10:980. DOI: https://doi.org/10.1038/nsb1203-980, PMID: 14634627
                                    Berman HM, Adams PD, Bonvin AA, Burley SK, Carragher B, Chiu W, DiMaio F, Ferrin TE, Gabanyi MJ, Goddard
                                      TD, Griffin PR, Haas J, Hanke CA, Hoch JC, Hummer G, Kurisu G, Lawson CL, Leitner A, Markley JL, Meiler J,
                                      et al. 2019. Federating structural models and data: outcomes from A workshop on archiving integrative
                                      structures. Structure 27:1745–1759. DOI: https://doi.org/10.1016/j.str.2019.11.002, PMID: 31780431
                                    Best RB, Merchant KA, Gopich IV, Schuler B, Bax A, Eaton WA. 2007. Effect of flexibility and Cis residues in
                                      single-molecule FRET studies of polyproline. PNAS 104:18964–18969. DOI: https://doi.org/10.1073/pnas.
                                      0709567104, PMID: 18029448
                                    Best RB, Hofmann H, Nettels D, Schuler B. 2015. Quantitative interpretation of FRET experiments via molecular
                                      simulation: force field and validation. Biophysical Journal 108:2721–2731. DOI: https://doi.org/10.1016/j.bpj.
                                      2015.04.038, PMID: 26039173
                                    Best RB, Zheng W, Borgia A, Buholzer K, Borgia MB, Hofmann H, Soranno A, Nettels D, Gast K, Grishaev A,
                                      Schuler B. 2018. Comment on "Innovative scattering analysis shows that hydrophobic disordered proteins are
                                      expanded in water". Science 361:eaar7101. DOI: https://doi.org/10.1126/science.aar7101, PMID: 30166459
                                    Blanchard SC, Gonzalez RL, Kim HD, Chu S, Puglisi JD. 2004. tRNA selection and kinetic proofreading in
                                      translation. Nature Structural & Molecular Biology 11:1008–1014. DOI: https://doi.org/10.1038/nsmb831,
                                      PMID: 15448679
                                    Blanco M, Walter NG. 2010. Analysis of complex single-molecule FRET time trajectories. In: Walter E (Ed).
                                      Methods in Enzymology. Academic Press. p. 153–178. DOI: https://doi.org/10.1016/S0076-6879(10)72011-5
                                    Bodo L, Bernd L, Lüttke W. 1981. Laser dyes with intramolecular triplet quenching. Optics Communications 38:
                                      207–210. DOI: https://doi.org/10.1016/0030-4018(81)90325-4
                                    Bohlen J, Cuartero-González Á, Pibiri E, Ruhlandt D, Fernández-Domı́nguez AI, Tinnefeld P, Acuna GP. 2019.
                                      Plasmon-assisted Förster resonance energy transfer at the single-molecule level in the moderate quenching
                                      regime. Nanoscale 11:7674–7681. DOI: https://doi.org/10.1039/C9NR01204D, PMID: 30946424
                                    Böhmer M, Wahl M, Rahn H-J, Erdmann R, Enderlein J. 2002. Time-resolved fluorescence correlation
                                      spectroscopy. Chemical Physics Letters 353:439–445. DOI: https://doi.org/10.1016/S0009-2614(02)00044-1
                                    Borgia MB, Borgia A, Best RB, Steward A, Nettels D, Wunderlich B, Schuler B, Clarke J. 2011. Single-molecule
                                      fluorescence reveals sequence-specific misfolding in multidomain proteins. Nature 474:662–665. DOI: https://
                                      doi.org/10.1038/nature10099, PMID: 21623368
                                    Borgia A, Zheng W, Buholzer K, Borgia MB, Schüler A, Hofmann H, Soranno A, Nettels D, Gast K, Grishaev A,
                                      Best RB, Schuler B. 2016. Consistent view of polypeptide chain expansion in chemical denaturants from
                                      multiple experimental methods. Journal of the American Chemical Society 138:11714–11726. DOI: https://doi.
                                      org/10.1021/jacs.6b05917, PMID: 27583570
                                    Borgia A, Borgia MB, Bugge K, Kissling VM, Heidarsson PO, Fernandes CB, Sottini A, Soranno A, Buholzer KJ,
                                      Nettels D, Kragelund BB, Best RB, Schuler B. 2018. Extreme disorder in an ultrahigh-affinity protein complex.
                                      Nature 555:61–66. DOI: https://doi.org/10.1038/nature25762, PMID: 29466338
                                    Börner R, Kowerko D, Miserachs HG, Schaffer MF, Sigel RKO. 2016. Metal ion induced heterogeneity in RNA
                                      folding studied by smFRET. Coordination Chemistry Reviews 327-328:123–142. DOI: https://doi.org/10.1016/j.
                                      ccr.2016.06.002


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                  45 of 69


           Review Article                                            Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics

                                    Börner R, Kowerko D, Hadzic M, König SLB, Ritter M, Sigel RKO. 2018. Simulations of camera-based single-
                                      molecule fluorescence experiments. PLOS ONE 13:e0195277. DOI: https://doi.org/10.1371/journal.pone.
                                      0195277, PMID: 29652886
                                    Börsch M, Reuter R, Balasubramanian G, Erdmann R, Jelezko F, Wrachtrup J. 2009. Fluorescent nanodiamonds
                                      for FRET-based monitoring of a single biological nanomotor FoF1 -ATP synthase. Multiphoton Microscopy in
                                      the Biomedical Sciences 7183:812720. DOI: https://doi.org/10.1117/12.812720
                                    Boukobza E, Sonnenfeld A, Haran G. 2001. Immobilization in surface-tethered lipid vesicles as a new tool for
                                      single biomolecule spectroscopy. The Journal of Physical Chemistry B 105:12165–12170. DOI: https://doi.org/
                                      10.1021/jp012016x
                                    Boura E, Rozycki B, Herrick DZ, Chung HS, Vecer J, Eaton WA, Cafiso DS, Hummer G, Hurley JH. 2011. Solution
                                      structure of the ESCRT-I complex by small-angle X-ray scattering, EPR, and FRET spectroscopy. PNAS 108:
                                      9437–9442. DOI: https://doi.org/10.1073/pnas.1101763108
                                    Braitbard M, Schneidman-Duhovny D, Kalisman N. 2019. Integrative structure modeling: overview and
                                      assessment. Annual Review of Biochemistry 88:113–135. DOI: https://doi.org/10.1146/annurev-biochem-
                                      013118-111429, PMID: 30830798
                                    Brand L, Eggeling C, Zander C, Drexhage KH, Seidel CAM. 1997. Single-Molecule identification of Coumarin-120
                                      by time-resolved fluorescence detection: Comparison of one- and two-photon excitation in solution. The
                                      Journal of Physical Chemistry A 101:4313–4321. DOI: https://doi.org/10.1021/jp963729w
                                    Braslavsky SE, Fron E, Rodrı́guez HB, Román ES, Scholes GD, Schweitzer G, Valeur B, Wirz J. 2008. Pitfalls and
                                      limitations in the practical use of Förster’s theory of resonance energy transfer. Photochemical &
                                      Photobiological Sciences 7:1444–1448. DOI: https://doi.org/10.1039/b810620g, PMID: 19037495
                                    Bravo JPK, Borodavka A, Barth A, Calabrese AN, Mojzes P, Cockburn JJB, Lamb DC, Tuma R. 2018. Stability of
                                      local secondary structure determines selectivity of viral RNA chaperones. Nucleic Acids Research 46:7924–
                                      7937. DOI: https://doi.org/10.1093/nar/gky394
                                    Brodie NI, Popov KI, Petrotchenko EV, Dokholyan NV, Borchers CH. 2017. Solving protein structures using short-
                                      distance cross-linking constraints as a guide for discrete molecular dynamics simulations. Science Advances 3:
                                      e1700479. DOI: https://doi.org/10.1126/sciadv.1700479, PMID: 28695211
                                    Brodie NI, Popov KI, Petrotchenko EV, Dokholyan NV, Borchers CH. 2019. Conformational ensemble of native a-
                                      synuclein in solution as determined by short-distance crosslinking constraint-guided discrete molecular
                                      dynamics simulations. PLOS Computational Biology 15:e1006859. DOI: https://doi.org/10.1371/journal.pcbi.
                                      1006859, PMID: 30917118
                                    Bronson JE, Fei J, Hofman JM, Gonzalez RL, Wiggins CH. 2009. Learning rates and states from biophysical time
                                      series: a bayesian approach to model selection and single-molecule FRET data. Biophysical Journal 97:3196–
                                      3205. DOI: https://doi.org/10.1016/j.bpj.2009.09.031, PMID: 20006957
                                    Brooks Shera E, Seitzinger NK, Davis LM, Keller RA, Soper SA. 1990. Detection of single fluorescent molecules.
                                      Chemical Physics Letters 174:553–557. DOI: https://doi.org/10.1016/0009-2614(90)85485-U
                                    Brünger AT. 1992. Free R value: a novel statistical quantity for assessing the accuracy of crystal structures.
                                      Nature 355:472–475. DOI: https://doi.org/10.1038/355472a0, PMID: 18481394
                                    Brunger AT, Strop P, Vrljic M, Chu S, Weninger KR. 2011. Three-dimensional molecular modeling with single
                                      molecule FRET. Journal of Structural Biology 173:497–505. DOI: https://doi.org/10.1016/j.jsb.2010.09.004,
                                      PMID: 20837146
                                    Büttner L, Javadi-Zarnaghi F, Höbartner C. 2014. Site-specific labeling of RNA at internal ribose hydroxyl groups:
                                      terbium-assisted deoxyribozymes at work. Journal of the American Chemical Society 136:8131–8137.
                                      DOI: https://doi.org/10.1021/ja503864v, PMID: 24825547
                                    Calabrese AN, Schiffrin B, Watson M, Karamanos TK, Walko M, Humes JR, Horne JE, White P, Wilson AJ, Kalli
                                      AC, Tuma R, Ashcroft AE, Brockwell DJ, Radford SE. 2020. Inter-domain dynamics in the chaperone SurA and
                                      multi-site binding to its outer membrane protein clients. Nature Communications 11:2155. DOI: https://doi.
                                      org/10.1038/s41467-020-15702-1, PMID: 32358557
                                    Callaway E. 2020. ’It will change everything’: DeepMind’s AI makes gigantic leap in solving protein structures.
                                      Nature 588:203–204. DOI: https://doi.org/10.1038/d41586-020-03348-4, PMID: 33257889
                                    Campos LA, Liu J, Wang X, Ramanathan R, English DS, Muñoz V. 2011. A photoprotection strategy for
                                      microsecond-resolution single-molecule fluorescence spectroscopy. Nature Methods 8:143–146. DOI: https://
                                      doi.org/10.1038/nmeth.1553, PMID: 21217750
                                    Chakraborty A, Wang D, Ebright YW, Korlann Y, Kortkhonjia E, Kim T, Chowdhury S, Wigneshweraraj S, Irschik
                                      H, Jansen R, Nixon BT, Knight J, Weiss S, Ebright RH. 2012. Opening and closing of the bacterial RNA
                                      polymerase clamp. Science 337:591–595. DOI: https://doi.org/10.1126/science.1218716, PMID: 22859489
                                    Chen J, Pyle JR, Sy Piecco KW, Kolomeisky AB, Landes CF. 2016. A two-step method for smFRET data analysis.
                                      The Journal of Physical Chemistry B 120:7128–7132. DOI: https://doi.org/10.1021/acs.jpcb.6b05697,
                                      PMID: 27379815
                                    Chen J, Zaer S, Drori P, Zamel J, Joron K, Kalisman N, Lerner E, Dokholyan N . 2020. The structural
                                      heterogeneity of a-synuclein is governed by several distinct subpopulations with interconversion times slower
                                      than milliseconds. bioRxiv. DOI: https://doi.org/10.1101/2020.11.09.374991
                                    Chizhik AI, Chizhik AM, Khoptyar D, Bär S, Meixner AJ, Enderlein J. 2011. Probing the radiative transition of
                                      single molecules with a tunable microresonator. Nano Letters 11:1700–1703. DOI: https://doi.org/10.1021/
                                      nl200215v, PMID: 21410240


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                  46 of 69



                                    Chizhik AI, Gregor I, Ernst B, Enderlein J. 2013. Nanocavity-based determination of absolute values of
                                      photoluminescence quantum yields. ChemPhysChem 14:505–513. DOI: https://doi.org/10.1002/cphc.
                                      201200931, PMID: 23335303
                                    Choi UB, Strop P, Vrljic M, Chu S, Brunger AT, Weninger KR. 2010. Single-molecule FRET-derived model of the
                                      synaptotagmin 1-SNARE fusion complex. Nature Structural & Molecular Biology 17:318–324. DOI: https://doi.
                                      org/10.1038/nsmb.1763, PMID: 20173763
                                    Choi JM, Holehouse AS, Pappu RV. 2020. Physical principles underlying the complex biology of intracellular
                                      phase transitions. Annual Review of Biophysics 49:107–133. DOI: https://doi.org/10.1146/annurev-biophys-
                                      121219-081629, PMID: 32004090
                                    Chung HS, Louis JM, Eaton WA. 2009. Experimental determination of upper bound for transition path times in
                                      protein folding from single-molecule photon-by-photon trajectories. PNAS 106:11837–11844. DOI: https://doi.
                                      org/10.1073/pnas.0901178106, PMID: 19584244
                                    Chung HS, Gopich IV, McHale K, Cellmer T, Louis JM, Eaton WA. 2011. Extracting rate coefficients from single-
                                      molecule photon trajectories and FRET efficiency histograms for a fast-folding protein. The Journal of Physical
                                      Chemistry A 115:3642–3656. DOI: https://doi.org/10.1021/jp1009669, PMID: 20509636
                                    Chung HS, McHale K, Louis JM, Eaton WA. 2012. Single-molecule fluorescence experiments determine protein
                                      folding transition path times. Science 335:981–984. DOI: https://doi.org/10.1126/science.1215768,
                                      PMID: 22363011
                                    Chung HS, Eaton WA. 2018. Protein folding transition path times from single molecule FRET. Current Opinion in
                                      Structural Biology 48:30–39. DOI: https://doi.org/10.1016/j.sbi.2017.10.007, PMID: 29080467
                                    Chung HS, Gopich IV. 2014. Fast single-molecule FRET spectroscopy: theory and experiment. Physical Chemistry
                                      Chemical Physics 16:18644–18657. DOI: https://doi.org/10.1039/C4CP02489C, PMID: 25088495
                                    Ciftci D, Huysmans GHM, Wang X, He C, Terry D, Zhou Z, Fitzgerald G, Blanchard SC, Boudker O. 2020. Single-
                                      molecule transport kinetics of a glutamate transporter homolog shows static disorder. Science Advances 6:
                                      eaaz1949. DOI: https://doi.org/10.1126/sciadv.aaz1949
                                    Cisse I, Okumus B, Joo C, Ha T. 2007. Fueling protein DNA interactions inside porous nanocontainers. PNAS
                                      104:12646–12650. DOI: https://doi.org/10.1073/pnas.0610673104, PMID: 17563361
                                    Clamme JP, Deniz AA. 2005. Three-color single-molecule fluorescence resonance energy transfer.
                                      ChemPhysChem 6:74–77. DOI: https://doi.org/10.1002/cphc.200400261, PMID: 15688649
                                    Clegg RM. 1992. Fluorescence resonance energy transfer and nucleic acids. Methods in Enzymology 211:353–
                                      388. DOI: https://doi.org/10.1016/0076-6879(92)11020-j, PMID: 1406315
                                    Clegg RM, Murchie AI, Zechel A, Carlberg C, Diekmann S, Lilley DM. 1992. Fluorescence resonance energy
                                      transfer analysis of the structure of the four-way DNA junction. Biochemistry 31:4846–4856. DOI: https://doi.
                                      org/10.1021/bi00135a016, PMID: 1591245
                                    Clegg RM. 1995. Fluorescence resonance energy transfer. Current Opinion in Biotechnology 6:103–110.
                                      DOI: https://doi.org/10.1016/0958-1669(95)80016-6
                                    Clore GM, Iwahara J. 2009. Theory, practice, and applications of paramagnetic relaxation enhancement for the
                                      characterization of transient low-population states of biological macromolecules and their complexes. Chemical
                                      Reviews 109:4108–4139. DOI: https://doi.org/10.1021/cr900033p, PMID: 19522502
                                    Cohen AE, Moerner WE. 2005. The anti-Brownian electrophoretic trap (ABEL trap): fabrication and software.
                                      Proceedings of SPIE 5699, Imaging, Manipulation, and Analysis of Biomolecules and Cells: Fundamentals and
                                      Applications III 296–305. DOI: https://doi.org/10.1117/12.598689
                                    Cordes T, Vogelsang J, Tinnefeld P. 2009. On the mechanism of trolox as antiblinking and antibleaching reagent.
                                      Journal of the American Chemical Society 131:5018–5019. DOI: https://doi.org/10.1021/ja809117z, PMID: 1
                                      9301868
                                    Cordes T, Santoso Y, Tomescu AI, Gryte K, Hwang LC, Camará B, Wigneshweraraj S, Kapanidis AN. 2010.
                                      Sensing DNA opening in transcription using quenchable Förster resonance energy transfer. Biochemistry 49:
                                      9171–9180. DOI: https://doi.org/10.1021/bi101184g, PMID: 20818825
                                    Coullomb A, Bidan CM, Qian C, Wehnekamp F, Oddou C, Albigès-Rizo C, Lamb DC, Dupont A. 2020. QuanTI-
                                      FRET: a framework for quantitative FRET measurements in living cells. Scientific Reports 10:6504. DOI: https://
                                      doi.org/10.1038/s41598-020-62924-w, PMID: 32300110
                                    Craggs TD, Sustarsic M, Plochowietz A, Mosayebi M, Kaju H, Cuthbert A, Hohlbein J, Domicevica L, Biggin PC,
                                      Doye JPK, Kapanidis AN. 2019. Substrate conformational dynamics facilitate structure-specific recognition of
                                      gapped DNA by DNA polymerase. Nucleic Acids Research 47:10788–10800. DOI: https://doi.org/10.1093/nar/
                                      gkz797, PMID: 31544938
                                    Craggs TD, Kapanidis AN. 2012. Six steps closer to FRET-driven structural biology. Nature Methods 9:1157–
                                      1158. DOI: https://doi.org/10.1038/nmeth.2257, PMID: 23223168
                                    Dale RE, Eisinger J, Blumberg WE. 1979. The orientational freedom of molecular probes. the orientation factor in
                                      intramolecular energy transfer. Biophysical Journal 26:161–193. DOI: https://doi.org/10.1016/S0006-3495(79)
                                      85243-1, PMID: 262414
                                    Dave R, Terry DS, Munro JB, Blanchard SC. 2009. Mitigating unwanted photophysical processes for improved
                                      single-molecule fluorescence imaging. Biophysical Journal 96:2371–2381. DOI: https://doi.org/10.1016/j.bpj.
                                      2008.11.061, PMID: 19289062
                                    de Boer P, Hoogenboom JP, Giepmans BNG. 2015. Correlated light and electron microscopy: ultrastructure
                                      lights up!. Nature Methods 12:503–513. DOI: https://doi.org/10.1038/nmeth.3400


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                               47 of 69



                                    de Boer M, Gouridis G, Muthahari YA, Cordes T. 2019a. Single-molecule observation of ligand binding and
                                     conformational changes in FeuA. Biophysical Journal 117:1642–1654. DOI: https://doi.org/10.1016/j.bpj.2019.
                                     08.005, PMID: 31537314
                                    de Boer M, Gouridis G, Vietrov R, Begg SL, Schuurman-Wolters GK, Husada F, Eleftheriadis N, Poolman B,
                                     McDevitt CA, Cordes T. 2019b. Conformational and dynamic plasticity in substrate-binding proteins underlies
                                     selective transport in ABC importers. eLife 8:e44652. DOI: https://doi.org/10.7554/eLife.44652, PMID: 30900
                                    de Lannoy C, Filius M, Kim SH, Joo C, de Ridder D. 2020. FRETboard: semi-supervised classification of fret
                                     traces. bioRxiv. DOI: https://doi.org/10.1101/2020.08.28.272195
                                    de Souza N, Picotti P. 2020. Mass spectrometry analysis of the structural proteome. Current Opinion in Structural
                                     Biology 60:57–65. DOI: https://doi.org/10.1016/j.sbi.2019.10.006, PMID: 31841731
                                    Deniz AA, Dahan M, Grunwell JR, Ha T, Faulhaber AE, Chemla DS, Weiss S, Schultz PG. 1999. Single-pair
                                     fluorescence resonance energy transfer on freely diffusing molecules: observation of Förster distance
                                     dependence and subpopulations. PNAS 96:3670–3675. DOI: https://doi.org/10.1073/pnas.96.7.3670,
                                     PMID: 10097095
                                    Deniz AA, Laurence TA, Beligere GS, Dahan M, Martin AB, Chemla DS, Dawson PE, Schultz PG, Weiss S. 2000.
                                     Single-molecule protein folding: diffusion fluorescence resonance energy transfer studies of the denaturation of
                                     chymotrypsin inhibitor 2. PNAS 97:5179–5184. DOI: https://doi.org/10.1073/pnas.090104997, PMID: 10792044
                                    Deniz AA. 2016. Deciphering complexity in molecular biophysics with Single-Molecule resolution. Journal of
                                     Molecular Biology 428:301–307. DOI: https://doi.org/10.1016/j.jmb.2015.12.011, PMID: 26707199
                                    Deplazes E, Jayatilaka D, Corry B. 2011. Testing the use of molecular dynamics to simulate fluorophore motions
                                     and FRET. Physical Chemistry Chemical Physics 13:11045–11054. DOI: https://doi.org/10.1039/c1cp20447e
                                    Dertinger T, Pacheco V, von der Hocht I, Hartmann R, Gregor I, Enderlein J. 2007. Two-focus fluorescence
                                     correlation spectroscopy: a new tool for accurate and absolute diffusion measurements. ChemPhysChem 8:
                                     433–443. DOI: https://doi.org/10.1002/cphc.200600638, PMID: 17269116
                                    Dertinger T, Loman A, Ewers B, Müller CB, Krämer B, Enderlein J. 2008. The optics and performance of dual-
                                     focus fluorescence correlation spectroscopy. Optics Express 16:14353–14368. DOI: https://doi.org/10.1364/
                                     OE.16.014353, PMID: 18794971
                                    Deußner-Helfmann NS, Auer A, Strauss MT, Malkusch S, Dietz MS, Barth HD, Jungmann R, Heilemann M. 2018.
                                     Correlative Single-Molecule FRET and DNA-PAINT imaging. Nano Letters 18:4626–4630. DOI: https://doi.org/
                                     10.1021/acs.nanolett.8b02185, PMID: 29943993
                                    Dickson RM, Cubitt AB, Tsien RY, Moerner WE. 1997. On/off blinking and switching behaviour of single
                                     molecules of green fluorescent protein. Nature 388:355–358. DOI: https://doi.org/10.1038/41048, PMID:
                                     9237752
                                    Diez M, Zimmermann B, Börsch M, König M, Schweinberger E, Steigmiller S, Reuter R, Felekyan S, Kudryavtsev
                                     V, Seidel CA, Gräber P. 2004. Proton-powered subunit rotation in single membrane-bound F0F1-ATP synthase.
                                     Nature Structural & Molecular Biology 11:135–141. DOI: https://doi.org/10.1038/nsmb718, PMID: 14730350
                                    Dimura M, Peulen TO, Hanke CA, Prakash A, Gohlke H, Seidel CA. 2016. Quantitative FRET studies and
                                     integrative modeling unravel the structure and dynamics of biomolecular systems. Current Opinion in Structural
                                     Biology 40:163–185. DOI: https://doi.org/10.1016/j.sbi.2016.11.012, PMID: 27939973
                                    Dimura M, Peulen TO, Sanabria H, Rodnin D, Hemmen K, Hanke CA, Seidel CAM, Gohlke H. 2020. Automated
                                     and optimally FRET-assisted structural modeling. Nature Communications 11:1–14. DOI: https://doi.org/10.
                                     1038/s41467-020-19023-1, PMID: 33106483
                                    Dingfelder F, Benke S, Nettels D, Schuler B. 2018. Mapping an equilibrium folding intermediate of the cytolytic
                                     pore toxin ClyA with single-molecule FRET. The Journal of Physical Chemistry B 122:11251–11261.
                                     DOI: https://doi.org/10.1021/acs.jpcb.8b07026, PMID: 30156409
                                    Doose S, Neuweiler H, Sauer M. 2009. Fluorescence quenching by photoinduced electron transfer: a reporter for
                                     conformational dynamics of macromolecules. ChemPhysChem 10:1389–1398. DOI: https://doi.org/10.1002/
                                     cphc.200900238, PMID: 19475638
                                    Dunkle JA, Wang L, Feldman MB, Pulk A, Chen VB, Kapral GJ, Noeske J, Richardson JS, Blanchard SC, Cate JH.
                                     2011. Structures of the bacterial ribosome in classical and hybrid states of tRNA binding. Science 332:981–984.
                                     DOI: https://doi.org/10.1126/science.1202692, PMID: 21596992
                                    Dupuis NF, Holmstrom ED, Nesbitt DJ. 2014. Molecular-crowding effects on single-molecule RNA folding/
                                     unfolding thermodynamics and kinetics. PNAS 111:8464–8469. DOI: https://doi.org/10.1073/pnas.1316039111,
                                     PMID: 24850865
                                    Düser MG, Bi Y, Zarrabi N, Dunn SD, Börsch M. 2008. The proton-translocating a subunit of F0F1-ATP synthase is
                                     allocated asymmetrically to the peripheral stalk. Journal of Biological Chemistry 283:33602–33610.
                                     DOI: https://doi.org/10.1074/jbc.M805170200, PMID: 18786919
                                    Dyla M, Terry DS, Kjaergaard M, Sørensen TL, Lauwring Andersen J, Andersen JP, Rohde Knudsen C, Altman RB,
                                     Nissen P, Blanchard SC. 2017. Dynamics of P-type ATPase transport revealed by single-molecule FRET. Nature
                                     551:346–351. DOI: https://doi.org/10.1038/nature24296, PMID: 29144454
                                    Ebbinghaus S, Dhar A, McDonald JD, Gruebele M. 2010. Protein folding stability and dynamics imaged in a
                                     living cell. Nature Methods 7:319–323. DOI: https://doi.org/10.1038/nmeth.1435, PMID: 20190760
                                    Edman L, Földes-Papp Z, Wennmalm S, Rigler R. 1999. The fluctuating enzyme: a single molecule approach.
                                     Chemical Physics 247:11–22. DOI: https://doi.org/10.1016/S0301-0104(99)00098-1


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                               48 of 69



                                    Eggeling C, Berger S, Brand L, Fries JR, Schaffer J, Volkmer A, Seidel CA. 2001. Data registration and selective
                                      single-molecule analysis using multi-parameter fluorescence detection. Journal of Biotechnology 86:163–180.
                                      DOI: https://doi.org/10.1016/S0168-1656(00)00412-0, PMID: 11257530
                                    Eilert T, Beckers M, Drechsler F, Michaelis J. 2017. Fast-NPS—A Markov Chain Monte Carlo-based analysis tool
                                      to obtain structural information from single-molecule FRET measurements. Computer Physics Communications
                                      219:377–389. DOI: https://doi.org/10.1016/j.cpc.2017.05.027
                                    Eilert T, Kallis E, Nagy J, Röcker C, Michaelis J. 2018. Complete kinetic theory of FRET. The Journal of Physical
                                      Chemistry B 122:11677–11694. DOI: https://doi.org/10.1021/acs.jpcb.8b07719, PMID: 30351105
                                    Enderlein J, Robbins DL, Ambrose WP, Goodwin PM, Keller RA. 1997. Statistics of single-molecule detection.
                                      The Journal of Physical Chemistry B 101:3626–3632. DOI: https://doi.org/10.1021/jp963261x
                                    Enderlein J, Gregor I, Patra D, Dertinger T, Kaupp UB. 2005. Performance of fluorescence correlation
                                      spectroscopy for measuring diffusion and concentration. ChemPhysChem 6:2324–2336. DOI: https://doi.org/
                                      10.1002/cphc.200500414, PMID: 16273566
                                    Ernst P, Zosel F, Reichen C, Nettels D, Schuler B, Plückthun A. 2020. Structure-guided design of a peptide lock
                                      for modular peptide binders. ACS Chemical Biology 15:457–468. DOI: https://doi.org/10.1021/acschembio.
                                      9b00928, PMID: 31985201
                                    Farooq S, Hohlbein J. 2015. Camera-based single-molecule FRET detection with improved time resolution.
                                      Physical Chemistry Chemical Physics 17:27862–27872. DOI: https://doi.org/10.1039/C5CP04137F, PMID: 2643
                                    Fay JM, Zhu C, Proctor EA, Tao Y, Cui W, Ke H, Dokholyan NV. 2016. A phosphomimetic mutation stabilizes
                                      SOD1 and rescues cell viability in the context of an ALS-Associated mutation. Structure 24:1898–1906.
                                      DOI: https://doi.org/10.1016/j.str.2016.08.011, PMID: 27667694
                                    Felekyan S, Kühnemuth R, Kudryavtsev V, Sandhagen C, Becker W, Seidel CAM. 2005. Full correlation from
                                      picoseconds to seconds by time-resolved and time-correlated single photon detection. Review of Scientific
                                      Instruments 76:083104–083114. DOI: https://doi.org/10.1063/1.1946088
                                    Felekyan S, Kalinin S, Sanabria H, Valeri A, Seidel CA. 2012. Filtered FCS: species auto- and cross-correlation
                                      functions highlight binding and dynamics in biomolecules. ChemPhysChem 13:1036–1053. DOI: https://doi.
                                      org/10.1002/cphc.201100897, PMID: 22407544
                                    Felekyan S, Sanabria H, Kalinin S, Kühnemuth R, Seidel CAM. 2013. Analyzing Förster resonance energy transfer
                                      with fluctuation algorithms. In: Tetin E (Ed). Methods in Enzymology. Academic Press. p. 39–85. DOI: https://
                                      doi.org/10.1016/B978-0-12-405539-1.00002-6
                                    Felekyan S, Eggeling C, Schaffer J, Antonik M, Haustein E, Kudryavtsev V, Kalinin S, Marawske S, Seidel CAM.
                                      2020. MFD Spectroscopy and Imaging software package. HHU Düsseldorf. http://www.mpc.hhu.de/software/
                                      software-package.html
                                    Feng X, Fu Z, Kaledhonkar S, Jia Y, Shah B, Jin A, Liu Z, Sun M, Chen B, Grassucci RA, Ren Y, Jiang H, Frank J,
                                      Lin Q. 2017. A fast and effective microfluidic spraying-plunging method for high-resolution single-particle Cryo-
                                      EM. Structure 25:663–670. DOI: https://doi.org/10.1016/j.str.2017.02.005, PMID: 28286002
                                    Ferguson A, Wang L, Altman RB, Terry DS, Juette MF, Burnett BJ, Alejo JL, Dass RA, Parks MM, Vincent CT,
                                      Blanchard SC. 2015. Functional dynamics within the human ribosome regulate the rate of active protein
                                      synthesis. Molecular Cell 60:475–486. DOI: https://doi.org/10.1016/j.molcel.2015.09.013, PMID: 26593721
                                    Filius M, Kim SH, Severins I, Joo C. 2020. High-Resolution Single-Molecule FRET via DNA eXchange (FRET X).
                                      bioRxiv. DOI: https://doi.org/10.1101/2020.10.15.340885
                                    Fitzgerald GA, Terry DS, Warren AL, Quick M, Javitch JA, Blanchard SC. 2019. Quantifying secondary transport
                                      at single-molecule resolution. Nature 575:528–534. DOI: https://doi.org/10.1038/s41586-019-1747-5,
                                      PMID: 31723269
                                    Fontana M, Fijen C, Lemay SG, Mathwig K, Hohlbein J. 2019. High-throughput, non-equilibrium studies of single
                                      biomolecules using glass-made nanofluidic devices. Lab on a Chip 19:79–86. DOI: https://doi.org/10.1039/
                                      C8LC01175C
                                    Förster T. 1948. Zwischenmolekulare Energiewanderung und Fluoreszenz. Annalen Der Physik 437:55–75.
                                      DOI: https://doi.org/10.1002/andp.19484370105
                                    Fries JR, Brand L, Eggeling C, Köllner M, Seidel CAM. 1998. Quantitative identification of different single
                                      molecules by selective time-resolved confocal fluorescence spectroscopy. The Journal of Physical Chemistry A
                                      102:6601–6613. DOI: https://doi.org/10.1021/jp980965t
                                    Gaigalas AK, Wang L. 2008. Measurement of the fluorescence quantum yield using a spectrometer with an
                                      integrating sphere detector. Journal of Research of the National Institute of Standards and Technology 113:
                                      17–28. DOI: https://doi.org/10.6028/jres.113.004, PMID: 27096110
                                    Gambin Y, VanDelinder V, Ferreon AC, Lemke EA, Groisman A, Deniz AA. 2011. Visualizing a one-way protein
                                      encounter complex by ultrafast single-molecule mixing. Nature Methods 8:239–241. DOI: https://doi.org/10.
                                      1038/nmeth.1568, PMID: 21297620
                                    Gansen A, Felekyan S, Kühnemuth R, Lehmann K, Tóth K, Seidel CAM, Langowski J. 2018. High precision FRET
                                      studies reveal reversible transitions in nucleosomes between microseconds and minutes. Nature
                                      Communications 9:4628. DOI: https://doi.org/10.1038/s41467-018-06758-1, PMID: 30401903
                                    Gao M, Gnutt D, Orban A, Appel B, Righetti F, Winter R, Narberhaus F, Müller S, Ebbinghaus S. 2016. RNA
                                      hairpin folding in the crowded cell. Angewandte Chemie International Edition 55:3224–3228. DOI: https://doi.
                                      org/10.1002/anie.201510847
                                    Gauto DF, Estrozi LF, Schwieters CD, Effantin G, Macek P, Sounier R, Sivertsen AC, Schmidt E, Kerfah R, Mas G,
                                      Colletier JP, Güntert P, Favier A, Schoehn G, Schanda P, Boisbouvier J. 2019. Integrated NMR and cryo-EM


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                 49 of 69



                                     atomic-resolution structure determination of a half-megadalton enzyme complex. Nature Communications 10:
                                     2697. DOI: https://doi.org/10.1038/s41467-019-10490-9, PMID: 31217444
                                    Geggier P, Dave R, Feldman MB, Terry DS, Altman RB, Munro JB, Blanchard SC. 2010. Conformational sampling
                                     of aminoacyl-tRNA during selection on the bacterial ribosome. Journal of Molecular Biology 399:576–595.
                                     DOI: https://doi.org/10.1016/j.jmb.2010.04.038, PMID: 20434456
                                    Gidi Y, Payne L, Glembockyte V, Michie MS, Schnermann MJ, Cosa G. 2020. Unifying mechanism for thiol-
                                     induced photoswitching and photostability of cyanine dyes. Journal of the American Chemical Society 142:
                                     12681–12689. DOI: https://doi.org/10.1021/jacs.0c03786, PMID: 32594743
                                    Gietl A, Holzmeister P, Grohmann D, Tinnefeld P. 2012. DNA origami as biocompatible surface to match single-
                                     molecule and ensemble experiments. Nucleic Acids Research 40:e110. DOI: https://doi.org/10.1093/nar/
                                     gks326, PMID: 22523083
                                    Gilboa B, Jing B, Cui TJ, Sow M, Plochowietz A, Mazumder A, Kapanidis AN. 2019. Confinement-free wide-field
                                     ratiometric tracking of single fluorescent molecules. Biophysical Journal 117:2141–2153. DOI: https://doi.org/
                                     10.1016/j.bpj.2019.10.033, PMID: 31711608
                                    Girodat D, Pati AK, Terry DS, Blanchard SC, Sanbonmatsu KY. 2020. Quantitative comparison between sub-
                                     millisecond time resolution single-molecule FRET measurements and 10-second molecular simulations of a
                                     biosensor protein. PLOS Computational Biology 16:e1008293. DOI: https://doi.org/10.1371/journal.pcbi.
                                     1008293, PMID: 33151943
                                    Glembockyte V, Lincoln R, Cosa G. 2015. Cy3 photoprotection mediated by Ni2+ for extended single-molecule
                                     imaging: old tricks for new techniques. Journal of the American Chemical Society 137:1116–1122. DOI: https://
                                     doi.org/10.1021/ja509923e, PMID: 25594101
                                    Gnutt D, Gao M, Brylski O, Heyden M, Ebbinghaus S. 2015. Excluded-volume effects in living cells. Angewandte
                                     Chemie International Edition 54:2548–2551. DOI: https://doi.org/10.1002/anie.201409847
                                    Gomes GW, Krzeminski M, Namini A, Martin EW, Mittag T, Head-Gordon T, Forman-Kay JD, Gradinaru CC.
                                     2020. Conformational ensembles of an intrinsically disordered protein consistent with NMR, SAXS, and Single-
                                     Molecule FRET. Journal of the American Chemical Society 142:15697–15710. DOI: https://doi.org/10.1021/
                                     jacs.0c02088, PMID: 32840111
                                    Gomes GN, Gradinaru CC. 2017. Insights into the conformations and dynamics of intrinsically disordered
                                     proteins using single-molecule fluorescence. Biochimica Et Biophysica Acta (BBA) - Proteins and Proteomics
                                     1865:1696–1706. DOI: https://doi.org/10.1016/j.bbapap.2017.06.008, PMID: 28625737
                                    Gopich I, Szabo A. 2005a. Theory of photon statistics in single-molecule Förster resonance energy transfer. The
                                     Journal of Chemical Physics 122:14707. DOI: https://doi.org/10.1063/1.1812746, PMID: 15638691
                                    Gopich IV, Szabo A. 2005b. Photon counting histograms for diffusing fluorophores. The Journal of Physical
                                     Chemistry B 109:17683–17688. DOI: https://doi.org/10.1021/jp052345f, PMID: 16853263
                                    Gopich IV, Szabo A. 2007. Single-molecule FRET with diffusion and conformational dynamics. The Journal of
                                     Physical Chemistry B 111:12925–12932. DOI: https://doi.org/10.1021/jp075255e, PMID: 17929964
                                    Gopich IV, Szabo A. 2009. Decoding the pattern of photon colors in single-molecule FRET. The Journal of
                                     Physical Chemistry B 113:10965–10973. DOI: https://doi.org/10.1021/jp903671p, PMID: 19588948
                                    Gopich IV, Szabo A. 2012. Theory of the energy transfer efficiency and fluorescence lifetime distribution in
                                     single-molecule FRET. PNAS 109:7747–7752. DOI: https://doi.org/10.1073/pnas.1205120109, PMID: 22550169
                                    Grabenhorst L, Trofymchuk K, Steiner F, Glembockyte V, Tinnefeld P. 2020. Fluorophore photostability and
                                     saturation in the hotspot of DNA origami nanoantennas. Methods and Applications in Fluorescence 8:24003.
                                     DOI: https://doi.org/10.1088/2050-6120/ab6ac8
                                    Graen T, Hoefling M, Grubmüller H. 2014. AMBER-DYES: characterization of charge fluctuations and force field
                                     parameterization of fluorescent dyes for molecular dynamics simulations. Journal of Chemical Theory and
                                     Computation 10:5505–5512. DOI: https://doi.org/10.1021/ct500869p, PMID: 26583233
                                    Greenfeld M, van de Meent JW, Pavlichin DS, Mabuchi H, Wiggins CH, Gonzalez RL, Herschlag D. 2015. Single-
                                     molecule dataset (SMD): a generalized storage format for raw and processed single-molecule data. BMC
                                     Bioinformatics 16:3. DOI: https://doi.org/10.1186/s12859-014-0429-4, PMID: 25591752
                                    Gregor I, Patra D, Enderlein J. 2005. Optical saturation in fluorescence correlation spectroscopy under
                                     continuous-wave and pulsed excitation. ChemPhysChem 6:164–170. DOI: https://doi.org/10.1002/cphc.
                                     200400319, PMID: 15688660
                                    Gregorio GG, Masureel M, Hilger D, Terry DS, Juette M, Zhao H, Zhou Z, Perez-Aguilar JM, Hauge M,
                                     Mathiasen S, Javitch JA, Weinstein H, Kobilka BK, Blanchard SC. 2017. Single-molecule analysis of ligand
                                     efficacy in b2AR-G-protein activation. Nature 547:68–73. DOI: https://doi.org/10.1038/nature22354, PMID: 2
                                     8607487
                                    Greife A, Felekyan S, Ma Q, Gertzen CG, Spomer L, Dimura M, Peulen TO, Wöhler C, Häussinger D, Gohlke H,
                                     Keitel V, Seidel CA. 2016. Structural assemblies of the di- and oligomeric G-protein coupled receptor TGR5 in
                                     live cells: an MFIS-FRET and integrative modelling study. Scientific Reports 6:36792. DOI: https://doi.org/10.
                                     1038/srep36792, PMID: 27833095
                                    Grimm JB, English BP, Chen J, Slaughter JP, Zhang Z, Revyakin A, Patel R, Macklin JJ, Normanno D, Singer RH,
                                     Lionnet T, Lavis LD. 2015. A general method to improve fluorophores for live-cell and single-molecule
                                     microscopy. Nature Methods 12:244–250. DOI: https://doi.org/10.1038/nmeth.3256, PMID: 25599551
                                    Grimm JB, Muthusamy AK, Liang Y, Brown TA, Lemon WC, Patel R, Lu R, Macklin JJ, Keller PJ, Ji N, Lavis LD.
                                     2017. A general method to fine-tune fluorophores for live-cell and in vivo imaging. Nature Methods 14:987–
                                     994. DOI: https://doi.org/10.1038/nmeth.4403, PMID: 28869757


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                               50 of 69



                                    Grinvald A, Haas E, Steinberg IZ. 1972. Evaluation of the distribution of distances between energy donors and
                                     acceptors by fluorescence decay. PNAS 69:2273–2277. DOI: https://doi.org/10.1073/pnas.69.8.2273,
                                     PMID: 16592008
                                    Grotz KK, Nueesch MF, Holmstrom ED, Heinz M, Stelzl LS, Schuler B, Hummer G. 2018. Dispersion correction
                                     alleviates dye stacking of single-stranded DNA and RNA in simulations of single-molecule fluorescence
                                     experiments. The Journal of Physical Chemistry B 122:11626–11639. DOI: https://doi.org/10.1021/acs.jpcb.
                                     8b07537, PMID: 30285443
                                    Guin D, Gruebele M. 2019. Weak chemical interactions that drive protein evolution: crowding, sticking, and
                                     quinary structure in folding and function. Chemical Reviews 119:10691–10717. DOI: https://doi.org/10.1021/
                                     acs.chemrev.8b00753, PMID: 31356058
                                    Guo J, Qiu X, Mingoes C, Deschamps JR, Susumu K, Medintz IL, Hildebrandt N. 2019. Conformational details of
                                     quantum dot-DNA resolved by Förster resonance energy transfer lifetime nanoruler. ACS Nano 13:505–514.
                                     DOI: https://doi.org/10.1021/acsnano.8b07137, PMID: 30508369
                                    Gurunathan K, Levitus M. 2010. FRET fluctuation spectroscopy of diffusing biopolymers: contributions of
                                     conformational dynamics and translational diffusion. The Journal of Physical Chemistry B 114:980–986.
                                     DOI: https://doi.org/10.1021/jp907390n, PMID: 20030305
                                    Ha T, Enderle T, Ogletree DF, Chemla DS, Selvin PR, Weiss S. 1996. Probing the interaction between two single
                                     molecules: fluorescence resonance energy transfer between a single donor and a single acceptor. PNAS 93:
                                     6264–6268. DOI: https://doi.org/10.1073/pnas.93.13.6264, PMID: 8692803
                                    Ha T, Chemla DS, Enderle T, Weiss S. 1997. Single molecule spectroscopy with automated positioning. Applied
                                     Physics Letters 70:782–784. DOI: https://doi.org/10.1063/1.118259
                                    Ha T, Ting AY, Liang J, Caldwell WB, Deniz AA, Chemla DS, Schultz PG, Weiss S. 1999. Single-molecule
                                     fluorescence spectroscopy of enzyme conformational dynamics and cleavage mechanism. PNAS 96:893–898.
                                     DOI: https://doi.org/10.1073/pnas.96.3.893, PMID: 9927664
                                    Ha T, Tinnefeld P. 2012. Photophysics of fluorescent probes for single-molecule biophysics and super-resolution
                                     imaging. Annual Review of Physical Chemistry 63:595–617. DOI: https://doi.org/10.1146/annurev-physchem-
                                     032210-103340, PMID: 22404588
                                    Haas E, Wilchek M, Katchalski-Katzir E, Steinberg IZ. 1975. Distribution of end-to-end distances of oligopeptides
                                     in solution as estimated by energy transfer. PNAS 72:1807–1811. DOI: https://doi.org/10.1073/pnas.72.5.1807
                                    Haas E, Katchalski-Katzir E, Steinberg IZ. 1978. Effect of the orientation of donor and acceptor on the probability
                                     of energy transfer involving electronic transitions of mixed polarization. Biochemistry 17:5064–5070.
                                     DOI: https://doi.org/10.1021/bi00616a032, PMID: 718874
                                    Haas E, Steinberg IZ. 1984. Intramolecular dynamics of chain molecules monitored by fluctuations in efficiency of
                                     excitation energy transfer. A theoretical study. Biophysical Journal 46:429–437. DOI: https://doi.org/10.1016/
                                     S0006-3495(84)84040-0, PMID: 6498263
                                    Hadi-Alijanvand H, Proctor EA, Ding F, Dokholyan NV, Moosavi-Movahedi AA. 2016. A hidden aggregation-
                                     prone structure in the heart of hypoxia inducible factor prolyl hydroxylase. Proteins: Structure, Function, and
                                     Bioinformatics 84:611–623. DOI: https://doi.org/10.1002/prot.25011
                                    Hadzic M, Kowerko D, Börner R, Zelger-Paulus S, Sigel RKO. 2016. Detailed analysis of complex single molecule
                                     FRET data with the software MASH. Proc. SPIE 9711, Imaging, Manipulation, and Analysis of Biomolecules,
                                     Cells, and Tissues IX, 971119. DOI: https://doi.org/10.1117/12.2211191
                                    Hadzic M, Börner R, König SLB, Kowerko D, Sigel RKO. 2018. Reliable state identification and state transition
                                     detection in fluorescence intensity-based single-molecule Förster resonance energy-transfer data. The Journal
                                     of Physical Chemistry B 122:6134–6147. DOI: https://doi.org/10.1021/acs.jpcb.7b12483, PMID: 29737844
                                    Hadzic M, Kowerko D, Börner R, Paulus S, Sigel R, König S, Ritter M. 2019. MASH-FRET: a user-friendly
                                     simulation and analyzing tool for single-molecule FRET videos. GitHub. https://github.com/RNA-FRETools/
                                     MASH-FRET
                                    Haenni D, Zosel F, Reymond L, Nettels D, Schuler B. 2013. Intramolecular distances and dynamics from the
                                     combined photon statistics of single-molecule FRET and photoinduced electron transfer. The Journal of
                                     Physical Chemistry B 117:13015–13028. DOI: https://doi.org/10.1021/jp402352s, PMID: 23718771
                                    Hagai D, Lerner E. 2019. Systematic assessment of burst impurity in confocal-based single-molecule fluorescence
                                     detection using brownian motion simulations. Molecules 24:2557. DOI: https://doi.org/10.3390/
                                     molecules24142557
                                    Hamadani KM, Weiss S. 2008. Nonequilibrium single molecule protein folding in a coaxial mixer. Biophysical
                                     Journal 95:352–365. DOI: https://doi.org/10.1529/biophysj.107.127431, PMID: 18339751
                                    Hanson JA, Duderstadt K, Watkins LP, Bhattacharyya S, Brokaw J, Chu JW, Yang H. 2007. Illuminating the
                                     mechanistic roles of enzyme conformational dynamics. PNAS 104:18055–18060. DOI: https://doi.org/10.1073/
                                     pnas.0708600104, PMID: 17989222
                                    Hanspach G, Trucks S, Hengesbach M. 2019. Strategic labelling approaches for RNA single-molecule
                                     spectroscopy. RNA Biology 16:1119–1132. DOI: https://doi.org/10.1080/15476286.2019.1593093, PMID: 30
                                     874475
                                    Hartmann A, Krainer G, Keller S, Schlierf M. 2015. Quantification of millisecond protein-folding dynamics in
                                     membrane-mimetic environments by single-molecule Förster resonance energy transfer spectroscopy.
                                     Analytical Chemistry 87:11224–11232. DOI: https://doi.org/10.1021/acs.analchem.5b03207, PMID: 26457727
                                    Haustein E, Jahnz M, Schwille P. 2003. Triple FRET: a tool for studying long-range molecular interactions.
                                     ChemPhysChem 4:745–748. DOI: https://doi.org/10.1002/cphc.200200634, PMID: 12901306


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                  51 of 69



                                    Hell SW, Sahl SJ, Bates M, Zhuang X, Heintzmann R, Booth MJ, Bewersdorf J, Shtengel G, Hess H, Tinnefeld P,
                                     Honigmann A, Jakobs S, Testa I, Cognet L, Lounis B, Ewers H, Davis SJ, Eggeling C, Klenerman D, Willig KI,
                                     et al. 2015. The 2015 super-resolution microscopy roadmap. Journal of Physics D: Applied Physics 48:443001.
                                     DOI: https://doi.org/10.1088/0022-3727/48/44/443001
                                    Hellenkamp B, Wortmann P, Kandzia F, Zacharias M, Hugel T. 2017. Multidomain structure and correlated
                                     dynamics determined by self-consistent FRET networks. Nature Methods 14:174–180. DOI: https://doi.org/10.
                                     1038/nmeth.4081
                                    Hellenkamp B, Schmid S, Doroshenko O, Opanasyuk O, Kühnemuth R, Rezaei Adariani S, Ambrose B, Aznauryan
                                     M, Barth A, Birkedal V, Bowen ME, Chen H, Cordes T, Eilert T, Fijen C, Gebhardt C, Götz M, Gouridis G,
                                     Gratton E, Ha T, et al. 2018a. Precision and accuracy of single-molecule FRET measurements-a multi-laboratory
                                     benchmark study. Nature Methods 15:669–676. DOI: https://doi.org/10.1038/s41592-018-0085-0,
                                     PMID: 30171252
                                    Hellenkamp B, Thurn J, Stadlmeier M, Hugel T. 2018b. Kinetics of transient protein complexes determined via
                                     diffusion-independent microfluidic mixing and fluorescence stoichiometry. The Journal of Physical Chemistry B
                                     122:11554–11560. DOI: https://doi.org/10.1021/acs.jpcb.8b07437, PMID: 30351113
                                    Henzler-Wildman KA, Thai V, Lei M, Ott M, Wolf-Watz M, Fenn T, Pozharski E, Wilson MA, Petsko GA, Karplus
                                     M, Hübner CG, Kern D. 2007. Intrinsic motions along an enzymatic reaction trajectory. Nature 450:838–844.
                                     DOI: https://doi.org/10.1038/nature06410, PMID: 18026086
                                    Henzler-Wildman K, Kern D. 2007. Dynamic personalities of proteins. Nature 450:964–972. DOI: https://doi.org/
                                     10.1038/nature06522, PMID: 18075575
                                    Hildebrandt LL, Preus S, Birkedal V. 2015. Quantitative single molecule FRET efficiencies using TIRF microscopy.
                                     Faraday Discussions 184:131–142. DOI: https://doi.org/10.1039/C5FD00100E, PMID: 26416760
                                    Hinde E, Digman MA, Welch C, Hahn KM, Gratton E. 2012. Biosensor Förster resonance energy transfer
                                     detection by the phasor approach to fluorescence lifetime imaging microscopy. Microscopy Research and
                                     Technique 75:271–281. DOI: https://doi.org/10.1002/jemt.21054, PMID: 21858900
                                    Hochstrasser RA, Chen SM, Millar DP. 1992. Distance distribution in a dye-linked oligonucleotide determined by
                                     time-resolved fluorescence energy transfer. Biophysical Chemistry 45:133–141. DOI: https://doi.org/10.1016/
                                     0301-4622(92)87005-4, PMID: 1286148
                                    Hoefling M, Lima N, Haenni D, Seidel CA, Schuler B, Grubmüller H. 2011. Structural heterogeneity and
                                     quantitative FRET efficiency distributions of polyprolines through a hybrid atomistic simulation and monte carlo
                                     approach. PLOS ONE 6:e19791. DOI: https://doi.org/10.1371/journal.pone.0019791, PMID: 21629703
                                    Hoffmann A, Nettels D, Clark J, Borgia A, Radford SE, Clarke J, Schuler B. 2011. Quantifying heterogeneity and
                                     conformational dynamics from single molecule FRET of diffusing molecules: recurrence analysis of single
                                     particles (RASP). Physical Chemistry Chemical Physics 13:1857–1871. DOI: https://doi.org/10.1039/c0cp01911a,
                                     PMID: 21218223
                                    Hofkens J, Cotlet M, Vosch T, Tinnefeld P, Weston KD, Ego C, Grimsdale A, Müllen K, Beljonne D, Brédas JL,
                                     Jordens S, Schweitzer G, Sauer M, De Schryver F. 2003. Revealing competitive Förster-type resonance energy-
                                     transfer pathways in single bichromophoric molecules. PNAS 100:13146–13151. DOI: https://doi.org/10.1073/
                                     pnas.2235805100, PMID: 14583594
                                    Hohlbein J, Aigrain L, Craggs TD, Bermek O, Potapova O, Shoolizadeh P, Grindley ND, Joyce CM, Kapanidis
                                     AN. 2013. Conformational landscapes of DNA polymerase I and mutator derivatives establish fidelity
                                     checkpoints for nucleotide insertion. Nature Communications 4:2131. DOI: https://doi.org/10.1038/
                                     ncomms3131, PMID: 23831915
                                    Hohng S, Joo C, Ha T. 2004. Single-molecule three-color FRET. Biophysical Journal 87:1328–1337. DOI: https://
                                     doi.org/10.1529/biophysj.104.043935, PMID: 15298935
                                    Hohng S, Zhou R, Nahas MK, Yu J, Schulten K, Lilley DM, Ha T. 2007. Fluorescence-force spectroscopy maps
                                     two-dimensional reaction landscape of the holliday junction. Science 318:279–283. DOI: https://doi.org/10.
                                     1126/science.1146113, PMID: 17932299
                                    Holden SJ, Uphoff S, Hohlbein J, Yadin D, Le Reste L, Britton OJ, Kapanidis AN. 2010. Defining the limits of
                                     single-molecule FRET resolution in TIRF microscopy. Biophysical Journal 99:3102–3111. DOI: https://doi.org/
                                     10.1016/j.bpj.2010.09.005, PMID: 21044609
                                    Holden SJ, Uphoff S, Kapanidis AN. 2011. DAOSTORM: an algorithm for high- density super-resolution
                                     microscopy. Nature Methods 8:279–280. DOI: https://doi.org/10.1038/nmeth0411-279, PMID: 21451515
                                    Holmstrom ED, Dupuis NF, Nesbitt DJ. 2014. Pulsed IR heating studies of single-molecule DNA duplex
                                     dissociation kinetics and thermodynamics. Biophysical Journal 106:220–231. DOI: https://doi.org/10.1016/j.bpj.
                                     2013.11.008, PMID: 24411254
                                    Holmstrom ED, Holla A, Zheng W, Nettels D, Best RB, Schuler B. 2018. Accurate transfer efficiencies, distance
                                     distributions, and ensembles of unfolded and intrinsically disordered proteins from single-molecule FRET. In:
                                     Rhoades E (Ed). Methods in Enzymology. Academic Press. p. 287–325. DOI: https://doi.org/10.1016/bs.mie.
                                     2018.09.030
                                    Hon J, Gonzalez RL. 2019. Bayesian-estimated hierarchical HMMs enable robust analysis of single-molecule
                                     kinetic heterogeneity. Biophysical Journal 116:1790–1802. DOI: https://doi.org/10.1016/j.bpj.2019.02.031,
                                     PMID: 31010664
                                    Hong Y, Lam JW, Tang BZ. 2011. Aggregation-induced emission. Chemical Society Reviews 40:5361–5388.
                                     DOI: https://doi.org/10.1039/c1cs15113d, PMID: 21799992


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                               52 of 69



                                    Horsey I, Furey WS, Harrison JG, Osborne MA, Balasubramanian S. 2000. Double fluorescence resonance energy
                                       transfer to explore multicomponent binding interactions: a case study of DNA mismatches. Chemical
                                       Communications 10:1043–1044. DOI: https://doi.org/10.1039/b002540m
                                    Hua B, Han KY, Zhou R, Kim H, Shi X, Abeysirigunawardena SC, Jain A, Singh D, Aggarwal V, Woodson SA, Ha T.
                                       2014. An improved surface passivation method for single-molecule studies. Nature Methods 11:1233–1236.
                                       DOI: https://doi.org/10.1038/nmeth.3143
                                    Huang B, Perroud TD, Zare RN. 2004. Photon counting histogram: one-photon excitation. ChemPhysChem 5:
                                       1523–1531. DOI: https://doi.org/10.1002/cphc.200400176, PMID: 15535551
                                    Husada F, Gouridis G, Vietrov R, Schuurman-Wolters GK, Ploetz E, de Boer M, Poolman B, Cordes T. 2015.
                                       Watching conformational dynamics of ABC transporters with single-molecule tools. Biochemical Society
                                       Transactions 43:1041–1047. DOI: https://doi.org/10.1042/BST20150140
                                    Husada F, Bountra K, Tassis K, de Boer M, Romano M, Rebuffat S, Beis K, Cordes T. 2018. Conformational
                                       dynamics of the ABC transporter McjD seen by single-molecule FRET. The EMBO Journal 37:e100056.
                                       DOI: https://doi.org/10.15252/embj.2018100056, PMID: 30237313
                                    Hwang H, Kim H, Myong S. 2011. Protein induced fluorescence enhancement as a single molecule assay with
                                       short distance sensitivity. PNAS 108:7414–7418. DOI: https://doi.org/10.1073/pnas.1017672108
                                    Hwang H, Myong S. 2014. Protein induced fluorescence enhancement (PIFE) for probing protein-nucleic acid
                                       interactions. Chem. Soc. Rev. 43:1221–1229. DOI: https://doi.org/10.1039/C3CS60201J, PMID: 24056732
                                    Hyman AA, Weber CA, Jülicher F. 2014. Liquid-liquid phase separation in biology. Annual Review of Cell and
                                       Developmental Biology 30:39–58. DOI: https://doi.org/10.1146/annurev-cellbio-100913-013325, PMID: 252
                                       88112
                                    Iacobucci C, Piotrowski C, Aebersold R, Amaral BC, Andrews P, Bernfur K, Borchers C, Brodie NI, Bruce JE, Cao
                                       Y, Chaignepain S, Chavez JD, Claverol S, Cox J, Davis T, Degliesposti G, Dong MQ, Edinger N, Emanuelsson
                                       C, Gay M, et al. 2019. First community-wide, comparative cross-linking mass spectrometry study. Analytical
                                       Chemistry 91:6953–6961. DOI: https://doi.org/10.1021/acs.analchem.9b00658, PMID: 31045356
                                    Iljina M, Mazal H, Goloubinoff P, Riven I, Haran G. 2020. Single-molecule spectroscopy reveals dynamic allostery
                                       mediated by the substrate-binding domain of a AAA+ machine. bioRxiv. DOI: https://doi.org/10.1101/2020.09.
                                       13.295345
                                    Ingargiola A, Laurence T, Boutelle R, Weiss S, Michalet X. 2016a. Photon-HDF5: an open file format for
                                       timestamp-based single-molecule fluorescence experiments. Biophysical Journal 110:26–33. DOI: https://doi.
                                       org/10.1016/j.bpj.2015.11.013, PMID: 26745406
                                    Ingargiola A, Lerner E, Chung S, Weiss S, Michalet X. 2016b. FRETBursts: an open source toolkit for analysis of
                                       freely-diffusing single-molecule FRET. PLOS ONE 11:e0160716. DOI: https://doi.org/10.1371/journal.pone.
                                       0160716, PMID: 27532626
                                    Ingargiola A, Lerner E, Chung S, Panzeri F, Gulinatti A, Rech I, Ghioni M, Weiss S, Michalet X. 2017. Multispot
                                       single-molecule FRET: High-throughput analysis of freely diffusing molecules. PLOS ONE 12:e0175766.
                                       DOI: https://doi.org/10.1371/journal.pone.0175766
                                    Ingargiola A, Segal M, Gulinatti A, Rech I, Labanca I, Maccagnani P, Ghioni M, Weiss S, Michalet X. 2018a. 48-
                                       spot single-molecule FRET setup with periodic acceptor excitation. The Journal of Chemical Physics 148:
                                       123304. DOI: https://doi.org/10.1063/1.5000742
                                    Ingargiola A, Weiss S, Lerner E. 2018b. Monte carlo diffusion-enhanced photon inference: distance distributions
                                       and conformational dynamics in single-molecule FRET. The Journal of Physical Chemistry B 122:11598–11615.
                                       DOI: https://doi.org/10.1021/acs.jpcb.8b07608, PMID: 30252475
                                    Iqbal A, Arslan S, Okumus B, Wilson TJ, Giraud G, Norman DG, Ha T, Lilley DMJ. 2008. Orientation dependence
                                       in fluorescent energy transfer between Cy3 and Cy5 terminally attached to double-stranded nucleic acids.
                                       PNAS 105:11176–11181. DOI: https://doi.org/10.1073/pnas.0801707105
                                    Isselstein M, Zhang L, Glembockyte V, Brix O, Cosa G, Tinnefeld P, Cordes T. 2020. Self-healing dyes-keeping
                                       the promise? The Journal of Physical Chemistry Letters 11:4462–4480. DOI: https://doi.org/10.1021/acs.jpclett.
                                       9b03833, PMID: 32401520
                                    Ivanov V, Li M, Mizuuchi K. 2009. Impact of emission anisotropy on fluorescence spectroscopy and FRET
                                       distance measurements. Biophysical Journal 97:922–929. DOI: https://doi.org/10.1016/j.bpj.2009.05.025,
                                       PMID: 19651051
                                    Jacob MH, Amir D, Ratner V, Gussakowsky E, Haas E. 2005. Predicting reactivities of protein surface cysteines as
                                       part of a strategy for selective multiple labeling. Biochemistry 44:13664–13672. DOI: https://doi.org/10.1021/
                                       bi051205t, PMID: 16229456
                                    Jäger M, Michalet X, Weiss S. 2005. Protein-protein interactions as a tool for site-specific labeling of proteins.
                                       Protein Science 14:2059–2068. DOI: https://doi.org/10.1110/ps.051384705, PMID: 15987886
                                    Jäger M, Nir E, Weiss S. 2006. Site-specific labeling of proteins for single-molecule FRET by combining chemical
                                       and enzymatic modification. Protein Science 15:640–646. DOI: https://doi.org/10.1110/ps.051851506,
                                       PMID: 16452617
                                    Jamieson T, Bakhshi R, Petrova D, Pocock R, Imani M, Seifalian AM. 2007. Biological applications of quantum
                                       dots. Biomaterials 28:4717–4732. DOI: https://doi.org/10.1016/j.biomaterials.2007.07.014
                                    Jazi AA, Ploetz E, Arizki M, Dhandayuthapani B, Waclawska I, Krämer R, Ziegler C, Cordes T. 2017. Caging and
                                       photoactivation in single-molecule Förster resonance energy transfer experiments. Biochemistry 56:2031–2041.
                                       DOI: https://doi.org/10.1021/acs.biochem.6b00916, PMID: 28362086
                                    Jeschke G. 2012. DEER distance measurements on proteins. Annual Review of Physical Chemistry 63:419–446.
                                       DOI: https://doi.org/10.1146/annurev-physchem-032511-143716, PMID: 22404592


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                 53 of 69


           Review Article                                            Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics

                                    Jeschke G. 2018. The contribution of modern EPR to structural biology. Emerging Topics in Life Sciences 2:9–18.
                                      DOI: https://doi.org/10.1042/ETLS20170143, PMID: 33525779
                                    Joo C, Ha T. 2012. Single-molecule FRET with total internal reflection microscopy. Cold Spring Harbor Protocols
                                      7:1223–1237. DOI: https://doi.org/10.1101/pdb.top072058
                                    Juette MF, Terry DS, Wasserman MR, Zhou Z, Altman RB, Zheng Q, Blanchard SC. 2014. The bright future of
                                      single-molecule fluorescence imaging. Current Opinion in Chemical Biology 20:103–111. DOI: https://doi.org/
                                      10.1016/j.cbpa.2014.05.010
                                    Juette MF, Terry DS, Wasserman MR, Altman RB, Zhou Z, Zhao H, Blanchard SC. 2016. Single-molecule imaging
                                      of non-equilibrium molecular ensembles on the millisecond timescale. Nature Methods 13:341–344.
                                      DOI: https://doi.org/10.1038/nmeth.3769
                                    Kaledhonkar S, Fu Z, White H, Frank J. 2018. Time-resolved cryo-electron microscopy using a microfluidic chip.
                                      In: Marsh J. A (Ed). Methods in Molecular Biology. Springer. p. 59–71. DOI: https://doi.org/10.1007/978-1-
                                      4939-7759-8_4
                                    Kalinin S, Sisamakis E, Magennis SW, Felekyan S, Seidel CA. 2010a. On the origin of broadening of single-
                                      molecule FRET efficiency distributions beyond shot noise limits. The Journal of Physical Chemistry B 114:6197–
                                      6206. DOI: https://doi.org/10.1021/jp100025v, PMID: 20397670
                                    Kalinin S, Valeri A, Antonik M, Felekyan S, Seidel CA. 2010b. Detection of structural dynamics by FRET: a photon
                                      distribution and fluorescence lifetime analysis of systems with multiple states. The Journal of Physical Chemistry
                                      B 114:7983–7995. DOI: https://doi.org/10.1021/jp102156t, PMID: 20486698
                                    Kalinin S, Peulen T, Sindbert S, Rothwell PJ, Berger S, Restle T, Goody RS, Gohlke H, Seidel CAM. 2012. A
                                      toolkit and benchmark study for FRET-restrained high-precision structural modeling. Nature Methods 9:1218–
                                      1225. DOI: https://doi.org/10.1038/nmeth.2222
                                    Kapanidis AN, Lee NK, Laurence TA, Doose S, Margeat E, Weiss S. 2004. Fluorescence-aided molecule sorting:
                                      Analysis of structure and interactions by alternating-laser excitation of single molecules. PNAS 101:8936–8941.
                                      DOI: https://doi.org/10.1073/pnas.0401690101
                                    Kapanidis AN, Laurence TA, Lee NK, Margeat E, Kong X, Weiss S. 2005. Alternating-laser excitation of single
                                      molecules. Accounts of Chemical Research 38:523–533. DOI: https://doi.org/10.1021/ar0401348, PMID: 1602
                                    Kapusta P, Wahl M, Benda A, Hof M, Enderlein J. 2007. Fluorescence lifetime correlation spectroscopy. Journal
                                      of Fluorescence 17:43–48. DOI: https://doi.org/10.1007/s10895-006-0145-1, PMID: 17171439
                                    Karimi A, Börner R, Mata G, Luedtke NW. 2020. A highly fluorescent nucleobase molecular rotor. Journal of the
                                      American Chemical Society 142:14422–14426. DOI: https://doi.org/10.1021/jacs.0c05180, PMID: 32786749
                                    Kask P, Palo K, Ullmann D, Gall K. 1999. Fluorescence-intensity distribution analysis and its application in
                                      biomolecular detection technology. PNAS 96:13756–13761. DOI: https://doi.org/10.1073/pnas.96.24.13756
                                    Keller BG, Kobitski A, Jäschke A, Nienhaus GU, Noé F. 2014. Complex RNA folding kinetics revealed by single-
                                      molecule FRET and hidden markov models. Journal of the American Chemical Society 136:4534–4543.
                                      DOI: https://doi.org/10.1021/ja4098719, PMID: 24568646
                                    Khara DC, Schreck JS, Tomov TE, Berger Y, Ouldridge TE, Doye JPK, Nir E. 2018. DNA bipedal motor walking
                                      dynamics: an experimental and theoretical study of the dependency on step size. Nucleic Acids Research 46:
                                      1553–1561. DOI: https://doi.org/10.1093/nar/gkx1282
                                    Kilic S, Felekyan S, Doroshenko O, Boichenko I, Dimura M, Vardanyan H, Bryan LC, Arya G, Seidel CAM, Fierz B.
                                      2018. Single-molecule FRET reveals multiscale chromatin dynamics modulated by HP1a. Nature
                                      Communications 9:235. DOI: https://doi.org/10.1038/s41467-017-02619-5, PMID: 29339721
                                    Kim HD, Nienhaus GU, Ha T, Orr JW, Williamson JR, Chu S. 2002. Mg2+-dependent conformational change of
                                      RNA studied by fluorescence correlation and FRET on immobilized single molecules. PNAS 99:4284–4289.
                                      DOI: https://doi.org/10.1073/pnas.032077799
                                    Kim S, Streets AM, Lin RR, Quake SR, Weiss S, Majumdar DS. 2011. High-throughput single-molecule optofluidic
                                      analysis. Nature Methods 8:242–245. DOI: https://doi.org/10.1038/nmeth.1569
                                    Kim J-Y, Kim C, Lee NK. 2015a. Real-time submillisecond single-molecule FRET dynamics of freely diffusing
                                      molecules with liposome tethering. Nature Communications 6:6992. DOI: https://doi.org/10.1038/
                                      ncomms7992
                                    Kim SE, Lee IB, Hyeon C, Hong SC. 2015b. Deciphering kinetic information from single-molecule FRET data that
                                      show slow transitions. The Journal of Physical Chemistry B 119:6974–6978. DOI: https://doi.org/10.1021/acs.
                                      jpcb.5b03991, PMID: 25989531
                                    Kim J-Y, Meng F, Yoo J, Chung HS. 2018a. Diffusion-limited association of disordered protein by non-native
                                      electrostatic interactions. Nature Communications 9:4707. DOI: https://doi.org/10.1038/s41467-018-06866-y
                                    Kim N, Kwon J, Lim Y, Kang J, Bae S, Kim SK. 2018b. Incorporation of STED technique into single-molecule
                                      spectroscopy to break the concentration limit of diffusing molecules in single-molecule detection. Chemical
                                      Communications 54:9667–9670. DOI: https://doi.org/10.1039/C8CC05726E
                                    Kim J, Li BX, Huang RY, Qiao JX, Ewing WR, MacMillan DWC. 2020. Site-Selective functionalization of
                                      methionine residues via photoredox catalysis. Journal of the American Chemical Society 142:21260–21266.
                                      DOI: https://doi.org/10.1021/jacs.0c09926, PMID: 33290649
                                    Kim J-Y, Chung HS. 2020. Disordered proteins follow diverse transition paths as they fold and bind to a partner.
                                      Science 368:1253–1257. DOI: https://doi.org/10.1126/science.aba3854
                                    Kinz-Thompson CD, Gonzalez RL. 2018. Increasing the time resolution of single-molecule experiments with
                                      bayesian inference. Biophysical Journal 114:289–300. DOI: https://doi.org/10.1016/j.bpj.2017.11.3741, PMID: 2
                                      9401427


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                  54 of 69



                                    Knox RS, van Amerongen H. 2002. Refractive index dependence of the Förster resonance excitation transfer
                                      rate. The Journal of Physical Chemistry B 106:5289–5293. DOI: https://doi.org/10.1021/jp013927+
                                    Köfinger J, Stelzl LS, Reuter K, Allande C, Reichel K, Hummer G. 2019. Efficient ensemble refinement by
                                      reweighting. Journal of Chemical Theory and Computation 15:3390–3401. DOI: https://doi.org/10.1021/acs.
                                      jctc.8b01231, PMID: 30939006
                                    Kong X, Nir E, Hamadani K, Weiss S. 2007. Photobleaching pathways in single-molecule FRET experiments.
                                      Journal of the American Chemical Society 129:4643–4654. DOI: https://doi.org/10.1021/ja068002s,
                                      PMID: 17375921
                                    König SL, Hadzic M, Fiorini E, Börner R, Kowerko D, Blanckenhorn WU, Sigel RK. 2013. BOBA FRET: bootstrap-
                                      based analysis of single-molecule FRET data. PLOS ONE 8:e84157. DOI: https://doi.org/10.1371/journal.pone.
                                      0084157, PMID: 24386343
                                    König I, Zarrine-Afsar A, Aznauryan M, Soranno A, Wunderlich B, Dingfelder F, Stüber JC, Plückthun A, Nettels
                                      D, Schuler B. 2015. Single-molecule spectroscopy of protein conformational dynamics in live eukaryotic cells.
                                      Nature Methods 12:773–779. DOI: https://doi.org/10.1038/nmeth.3475, PMID: 26147918
                                    Koukos PI, Bonvin A. 2020. Integrative modelling of biomolecular complexes. Journal of Molecular Biology 432:
                                      2861–2881. DOI: https://doi.org/10.1016/j.jmb.2019.11.009, PMID: 31783069
                                    Krainer G, Hartmann A, Schlierf M. 2015. farFRET: extending the range in single-molecule FRET experiments
                                      beyond 10 nm. Nano Letters 15:5826–5829. DOI: https://doi.org/10.1021/acs.nanolett.5b01878,
                                      PMID: 26104104
                                    Kravets E, Degrandi D, Ma Q, Peulen TO, Klümpers V, Felekyan S, Kühnemuth R, Weidtkamp-Peters S, Seidel
                                      CA, Pfeffer K. 2016. Guanylate binding proteins directly attack Toxoplasma gondii via supramolecular
                                      complexes. eLife 5:e11479. DOI: https://doi.org/10.7554/eLife.11479, PMID: 26814575
                                    Krstić I, Hänsel R, Romainczyk O, Engels JW, Dötsch V, Prisner TF. 2011. Long-range distance measurements on
                                      nucleic acids in cells by pulsed EPR spectroscopy. Angewandte Chemie 50:5070–5074. DOI: https://doi.org/10.
                                      1002/anie.201100886, PMID: 21506223
                                    Kudryavtsev V, Felekyan S, Woźniak AK, König M, Sandhagen C, Kühnemuth R, Seidel CA, Oesterhelt F. 2007.
                                      Monitoring dynamic systems with multiparameter fluorescence imaging. Analytical and Bioanalytical Chemistry
                                      387:71–82. DOI: https://doi.org/10.1007/s00216-006-0917-0, PMID: 17160654
                                    Kudryavtsev V, Sikor M, Kalinin S, Mokranjac D, Seidel CA, Lamb DC. 2012. Combining MFD and PIE for
                                      accurate single-pair Förster resonance energy transfer measurements. ChemPhysChem 13:1060–1078.
                                      DOI: https://doi.org/10.1002/cphc.201100822, PMID: 22383292
                                    Kühnemuth R, Seidel CAM. 2001. Principles of single molecule multiparameter fluorescence spectroscopy.
                                      Single Molecules 2:251–254. DOI: https://doi.org/10.1002/1438-5171(200112)2:4<251::AID-SIMO251>3.0.CO;
                                      2-T
                                    Kupitz C, Basu S, Grotjohann I, Fromme R, Zatsepin NA, Rendek KN, Hunter MS, Shoeman RL, White TA, Wang
                                      D, James D, Yang J-H, Cobb DE, Reeder B, Sierra RG, Liu H, Barty A, Aquila AL, Deponte D, Kirian RA, et al.
                                      2014. Serial time-resolved crystallography of photosystem II using a femtosecond X-ray laser. Nature 513:261–
                                      265. DOI: https://doi.org/10.1038/nature13453
                                    Kuzmenkina EV, Heyes CD, Nienhaus GU. 2005. Single-molecule Förster resonance energy transfer study of
                                      protein dynamics under denaturing conditions. PNAS 102:15471–15476. DOI: https://doi.org/10.1073/pnas.
                                      0507728102
                                    Kuzmenkina EV, Heyes CD, Nienhaus GU. 2006. Single-molecule FRET study of denaturant induced unfolding of
                                      RNase H. Journal of Molecular Biology 357:313–324. DOI: https://doi.org/10.1016/j.jmb.2005.12.061,
                                      PMID: 16426636
                                    Kuznetsova IM, Turoverov KK, Uversky VN. 2014. What macromolecular crowding can do to a protein.
                                      International Journal of Molecular Sciences 15:23090–23140. DOI: https://doi.org/10.3390/ijms151223090,
                                      PMID: 25514413
                                    Lacoste TD, Michalet X, Pinaud F, Chemla DS, Alivisatos AP, Weiss S. 2000. Ultrahigh-resolution multicolor
                                      colocalization of single fluorescent probes. PNAS 97:9461–9466. DOI: https://doi.org/10.1073/pnas.170286097
                                    Lamichhane R, Solem A, Black W, Rueda D. 2010. Single-molecule FRET of protein-nucleic acid and protein-
                                      protein complexes: surface passivation and immobilization. Methods 52:192–200. DOI: https://doi.org/10.
                                      1016/j.ymeth.2010.06.010, PMID: 20554047
                                    Larsen KP, Choi J, Prabhakar A, Puglisi EV, Puglisi JD. 2019. Relating structure and dynamics in RNA biology.
                                      Cold Spring Harbor Perspectives in Biology 11:a032474. DOI: https://doi.org/10.1101/cshperspect.a032474,
                                      PMID: 31262948
                                    Larson J, Kirk M, Drier EA, O’Brien W, MacKay JF, Friedman LJ, Hoskins AA. 2014. Design and construction of a
                                      multiwavelength, micromirror total internal reflectance fluorescence microscope. Nature Protocols 9:2317–
                                      2328. DOI: https://doi.org/10.1038/nprot.2014.155
                                    Laurence TA, Kong X, Jager M, Weiss S. 2005. Probing structural heterogeneities and fluctuations of nucleic
                                      acids and denatured proteins. PNAS 102:17348–17353. DOI: https://doi.org/10.1073/pnas.0508584102
                                    Laurence TA, Kwon Y, Yin E, Hollars CW, Camarero JA, Barsky D. 2007. Correlation spectroscopy of minor
                                      fluorescent species: signal purification and distribution analysis. Biophysical Journal 92:2184–2198.
                                      DOI: https://doi.org/10.1529/biophysj.106.093591, PMID: 17189306
                                    Laurence TA, Kwon Y, Johnson A, Hollars CW, O’Donnell M, Camarero JA, Barsky D. 2008. Motion of a DNA
                                      sliding clamp observed by single molecule fluorescence spectroscopy. Journal of Biological Chemistry 283:
                                      22895–22906. DOI: https://doi.org/10.1074/jbc.M800174200


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                               55 of 69



                                    LeBlanc S, Kulkarni P, Weninger K. 2018. Single molecule FRET: a powerful tool to study intrinsically disordered
                                      proteins. Biomolecules 8:140. DOI: https://doi.org/10.3390/biom8040140
                                    Lee NK, Kapanidis AN, Wang Y, Michalet X, Mukhopadhyay J, Ebright RH, Weiss S. 2005. Accurate FRET
                                      measurements within single diffusing biomolecules using alternating-laser excitation. Biophysical Journal 88:
                                      2939–2953. DOI: https://doi.org/10.1529/biophysj.104.054114, PMID: 15653725
                                    Lee NK, Koh HR, Han KY, Kim SK. 2007a. Folding of 8-17 deoxyribozyme studied by three-color alternating-laser
                                      excitation of single molecules. Journal of the American Chemical Society 129:15526–15534. DOI: https://doi.
                                      org/10.1021/ja0725145, PMID: 18027936
                                    Lee NK, Kapanidis AN, Koh HR, Korlann Y, Ho SO, Kim Y, Gassman N, Kim SK, Weiss S. 2007b. Three-color
                                      alternating-laser excitation of single molecules: monitoring multiple interactions and distances. Biophysical
                                      Journal 92:303–312. DOI: https://doi.org/10.1529/biophysj.106.093211, PMID: 17040983
                                    Lee M, Kim SH, Hong S-C. 2010a. Minute negative superhelicity is sufficient to induce the B-Z transition in the
                                      presence of low tension. PNAS 107:4985–4990. DOI: https://doi.org/10.1073/pnas.0911528107
                                    Lee S, Lee J, Hohng S. 2010b. Single-molecule three-color FRET with both negligible spectral overlap and long
                                      observation time. PLOS ONE 5:e12270. DOI: https://doi.org/10.1371/journal.pone.0012270, PMID: 20808851
                                    Lee J, Lee S, Ragunathan K, Joo C, Ha T, Hohng S. 2010c. Single-molecule four-color FRET. Angewandte Chemie
                                      International Edition 49:9922–9925. DOI: https://doi.org/10.1002/anie.201005402, PMID: 21104966
                                    Lee TC, Moran CR, Cistrone PA, Dawson PE, Deniz AA. 2018. Site-specific three-color labeling of a-synuclein via
                                      conjugation to uniquely reactive cysteines during assembly by native chemical ligation. Cell Chemical Biology
                                      25:797–801. DOI: https://doi.org/10.1016/j.chembiol.2018.03.009, PMID: 29681525
                                    Léger C, Yahia-Ammar A, Susumu K, Medintz IL, Urvoas A, Valerio-Lepiniec M, Minard P, Hildebrandt N. 2020.
                                      Picomolar biosensing and conformational analysis using artificial bidomain proteins and terbium-to-quantum
                                      dot Förster resonance energy transfer. ACS Nano 14:5956–5967. DOI: https://doi.org/10.1021/acsnano.
                                      0c01410, PMID: 32216328
                                    Lehmann K, Felekyan S, Kühnemuth R, Dimura M, Tóth K, Seidel CAM, Langowski J. 2020. Dynamics of the
                                      nucleosomal histone H3 N-terminal tail revealed by high precision single-molecule FRET. Nucleic Acids
                                      Research 48:1551–1571. DOI: https://doi.org/10.1093/nar/gkz1186, PMID: 31956896
                                    Lemke EA, Gambin Y, Vandelinder V, Brustad EM, Liu HW, Schultz PG, Groisman A, Deniz AA. 2009. Microfluidic
                                      device for single-molecule experiments with enhanced photostability. Journal of the American Chemical
                                      Society 131:13610–13612. DOI: https://doi.org/10.1021/ja9027023, PMID: 19772358
                                    Lerner E, Hilzenrat G, Amir D, Tauber E, Garini Y, Haas E. 2013. Preparation of homogeneous samples of
                                      double-labelled protein suitable for single-molecule FRET measurements. Analytical and Bioanalytical
                                      Chemistry 405:5983–5991. DOI: https://doi.org/10.1007/s00216-013-7002-2
                                    Lerner E, Orevi T, Ben Ishay E, Amir D, Haas E. 2014. Kinetics of fast changing intramolecular distance
                                      distributions obtained by combined analysis of FRET efficiency kinetics and time-resolved FRET equilibrium
                                      measurements. Biophysical Journal 106:667–676. DOI: https://doi.org/10.1016/j.bpj.2013.11.4500,
                                      PMID: 24507607
                                    Lerner E, Ploetz E, Hohlbein J, Cordes T, Weiss S. 2016. A quantitative theoretical framework for protein-
                                      induced fluorescence enhancement-Förster-type resonance energy transfer (PIFE-FRET). The Journal of Physical
                                      Chemistry B 120:6401–6410. DOI: https://doi.org/10.1021/acs.jpcb.6b03692, PMID: 27184889
                                    Lerner E, Ingargiola A, Lee JJ, Borukhov S, Michalet X, Weiss S. 2017. Different types of pausing modes during
                                      transcription initiation. Transcription 8:242–253. DOI: https://doi.org/10.1080/21541264.2017.1308853
                                    Lerner E, Cordes T, Ingargiola A, Alhadid Y, Chung S, Michalet X, Weiss S. 2018a. Toward dynamic structural
                                      biology: Two decades of single-molecule Förster resonance energy transferster resonance energy transfer.
                                      Science 359:eaan1133. DOI: https://doi.org/10.1126/science.aan1133
                                    Lerner E, Ingargiola A, Weiss S. 2018b. Characterizing highly dynamic conformational states: The transcription
                                      bubble in RNAP-promoter open complex as an example. The Journal of Chemical Physics 148:123315.
                                      DOI: https://doi.org/10.1063/1.5004606
                                    Lerner E. 2019. PIE/nsALEX FRET analysis notebook using FRETbursts - corrections, MFD, FCS, 2CDE & BVA.
                                      Zenodo. . DOI: https://doi.org/10.5281/zenodo.3630498
                                    Lerner E. 2020. Microsecond ALEX FRET analysis notebook using FRETbursts - corrections, FRET burst analysis of
                                      recurring molecules, FCS, 2CDE & BVA [Data set]. Zenodo. . DOI: https://doi.org/10.5281/zenodo.3630474
                                    Levitus M, Ranjit S. 2011. Cyanine dyes in biophysical research: the photophysics of polymethine fluorescent
                                      dyes in biomolecular environments. Quarterly Reviews of Biophysics 44:123–151. DOI: https://doi.org/10.1017/
                                      S0033583510000247
                                    Li J, Zhang L, Johnson-Buck A, Walter NG. 2020a. Automatic classification and segmentation of single-molecule
                                      fluorescence time traces with deep learning. Nature Communications 11:5833. DOI: https://doi.org/10.1038/
                                      s41467-020-19673-1
                                    Li Z, Li W, Lu M, Bess J, Chao CW, Gorman J, Terry DS, Zhang B, Zhou T, Blanchard SC, Kwong PD, Lifson JD,
                                      Mothes W, Liu J. 2020b. Subnanometer structures of HIV-1 envelope trimers on aldrithiol-2-inactivated virus
                                      particles. Nature Structural & Molecular Biology 27:726–734. DOI: https://doi.org/10.1038/s41594-020-0452-2
                                    Lindhoud S, Pirchi M, Westphal AH, Haran G, van Mierlo CPM. 2015. Gradual folding of an off-pathway molten
                                      globule detected at the single-molecule level. Journal of Molecular Biology 427:3148–3157. DOI: https://doi.
                                      org/10.1016/j.jmb.2015.07.002
                                    Lipman EA, Schuler B, Bakajin O, Eaton WA. 2003. Single-molecule measurement of protein folding kinetics.
                                      Science 301:1233–1235. DOI: https://doi.org/10.1126/science.1085399, PMID: 12947198


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                              56 of 69



                                    Liput DJ, Nguyen TA, Augustin SM, Lee JO, Vogel SS. 2020. A guide to fluorescence lifetime microscopy and
                                      Förster’s Resonance Energy Transfer in Neuroscience. Current Protocols in Neuroscience 94:e108. DOI: https://
                                      doi.org/10.1002/cpns.108, PMID: 33232577
                                    Liu Z, Gong Z, Cao Y, Ding YH, Dong MQ, Lu YB, Zhang WP, Tang C. 2018. Characterizing protein dynamics
                                      with integrative use of bulk and single-molecule techniques. Biochemistry 57:305–313. DOI: https://doi.org/10.
                                      1021/acs.biochem.7b00817, PMID: 28945353
                                    Liu Z, Dong X, Yi HW, Yang J, Gong Z, Wang Y, Liu K, Zhang WP, Tang C. 2019. Structural basis for the
                                      recognition of K48-linked ub chain by proteasomal receptor Rpn13. Cell Discovery 5:19. DOI: https://doi.org/
                                      10.1038/s41421-019-0089-7, PMID: 30962947
                                    Liu Y, Lilley DMJ. 2017. Crystal structures of cyanine fluorophores stacked onto the end of double-stranded RNA.
                                      Biophysical Journal 113:2336–2343. DOI: https://doi.org/10.1016/j.bpj.2017.10.002, PMID: 29211987
                                    Long X, Parks JW, Stone MD. 2016. Integrated magnetic tweezers and single-molecule FRET for investigating
                                      the mechanical properties of nucleic acid. Methods 105:16–25. DOI: https://doi.org/10.1016/j.ymeth.2016.06.
                                      009, PMID: 27320203
                                    Lu M, Ma X, Mothes W. 2019. Illuminating the virus life cycle with single-molecule FRET imaging. Advances in
                                      Virus Research 105:239–273. DOI: https://doi.org/10.1016/bs.aivir.2019.07.004, PMID: 31522706
                                    Magde D, Elson E, Webb WW. 1972. Thermodynamic fluctuations in a reacting system—measurement by
                                      Fluorescence Correlation Spectroscopy. Physical Review Letters 29:705–708. DOI: https://doi.org/10.1103/
                                      PhysRevLett.29.705
                                    Maity H, Reddy G. 2016. Folding of protein L with implications for collapse in the denatured state ensemble.
                                      Journal of the American Chemical Society 138:2609–2616. DOI: https://doi.org/10.1021/jacs.5b11300
                                    Mapa K, Sikor M, Kudryavtsev V, Waegemann K, Kalinin S, Seidel CA, Neupert W, Lamb DC, Mokranjac D. 2010.
                                      The conformational dynamics of the mitochondrial Hsp70 chaperone. Molecular Cell 38:89–100. DOI: https://
                                      doi.org/10.1016/j.molcel.2010.03.010, PMID: 20385092
                                    Margeat E, Kapanidis AN, Tinnefeld P, Wang Y, Mukhopadhyay J, Ebright RH, Weiss S. 2006. Direct observation
                                      of abortive initiation and promoter escape within single immobilized transcription complexes. Biophysical
                                      Journal 90:1419–1431. DOI: https://doi.org/10.1529/biophysj.105.069252, PMID: 16299085
                                    Margittai M, Widengren J, Schweinberger E, Schröder GF, Felekyan S, Haustein E, König M, Fasshauer D,
                                      Grubmüller H, Jahn R, Seidel CA. 2003. Single-molecule fluorescence resonance energy transfer reveals a
                                      dynamic equilibrium between closed and open conformations of syntaxin 1. PNAS 100:15516–15521.
                                      DOI: https://doi.org/10.1073/pnas.2331232100, PMID: 14668446
                                    Martens KJA, van Beljouw SPB, van der Els S, Vink JNA, Baas S, Vogelaar GA, Brouns SJJ, van Baarlen P,
                                      Kleerebezem M, Hohlbein J. 2019. Visualisation of dCas9 target search in vivo using an open-microscopy
                                      framework. Nature Communications 10:3552. DOI: https://doi.org/10.1038/s41467-019-11514-0, PMID: 313
                                      91532
                                    Martinac B. 2017. Single-molecule FRET studies of ion channels. Progress in Biophysics and Molecular Biology
                                      130:192–197. DOI: https://doi.org/10.1016/j.pbiomolbio.2017.06.014, PMID: 28648629
                                    Masliah G, Maris C, König SL, Yulikov M, Aeschimann F, Malinowska AL, Mabille J, Weiler J, Holla A, Hunziker J,
                                      Meisner-Kober N, Schuler B, Jeschke G, Allain FH. 2018. Structural basis of siRNA recognition by TRBP double-
                                      stranded RNA binding domains. The EMBO Journal 37:e97089. DOI: https://doi.org/10.15252/embj.
                                      201797089, PMID: 29449323
                                    Matikonda SS, Hammersley G, Kumari N, Grabenhorst L, Glembockyte V, Tinnefeld P, Ivanic J, Levitus M,
                                      Schnermann MJ. 2020a. Impact of cyanine conformational restraint in the near-infrared range. The Journal of
                                      Organic Chemistry 85:5907–5915. DOI: https://doi.org/10.1021/acs.joc.0c00236, PMID: 32275153
                                    Matikonda SS, Ivanic J, Gomez M, Hammersley G, Schnermann MJ. 2020b. Core remodeling leads to long
                                      wavelength fluoro-coumarins. Chemical Science 11:7302–7307. DOI: https://doi.org/10.1039/D0SC02566F
                                    Matsunaga Y, Sugita Y. 2018. Linking time-series of single-molecule experiments with molecular dynamics
                                      simulations by machine learning. eLife 7:e32668. DOI: https://doi.org/10.7554/eLife.32668, PMID: 29723137
                                    May PFJ, Pinkney JNM, Zawadzki P, Evans GW, Sherratt DJ, Kapanidis AN. 2014. Tethered fluorophore motion:
                                      studying large DNA conformational changes by single-fluorophore imaging. Biophysical Journal 107:1205–
                                      1216. DOI: https://doi.org/10.1016/j.bpj.2014.07.024, PMID: 25185556
                                    Mazal H, Aviram H, Riven I, Haran G. 2018. Effect of ligand binding on a protein with a complex folding
                                      landscape. Physical Chemistry Chemical Physics 20:3054–3062. DOI: https://doi.org/10.1039/C7CP03327C,
                                      PMID: 28721412
                                    Mazal H, Iljina M, Barak Y, Elad N, Rosenzweig R, Goloubinoff P, Riven I, Haran G. 2019. Tunable microsecond
                                      dynamics of an allosteric switch regulate the activity of a AAA+ disaggregation machine. Nature
                                      Communications 10:1438. DOI: https://doi.org/10.1038/s41467-019-09474-6, PMID: 30926805
                                    Mazal H, Haran G. 2019. Single-molecule FRET methods to study the dynamics of proteins at work. Current
                                      Opinion in Biomedical Engineering 12:8–17. DOI: https://doi.org/10.1016/j.cobme.2019.08.007, PMID: 31
                                      989063
                                    McCann JJ, Choi UB, Zheng L, Weninger K, Bowen ME. 2010. Optimizing methods to recover absolute FRET
                                      efficiency from immobilized single molecules. Biophysical Journal 99:961–970. DOI: https://doi.org/10.1016/j.
                                      bpj.2010.04.063, PMID: 20682275
                                    McCann JJ, Zheng L, Rohrbeck D, Felekyan S, Kühnemuth R, Sutton RB, Seidel CA, Bowen ME. 2012.
                                      Supertertiary structure of the synaptic MAGuK scaffold proteins is conserved. PNAS 109:15775–15780.
                                      DOI: https://doi.org/10.1073/pnas.1200254109, PMID: 23019361


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                              57 of 69



                                    McKinney SA, Joo C, Ha T. 2006. Analysis of single-molecule FRET trajectories using hidden Markov modeling.
                                     Biophysical Journal 91:1941–1951. DOI: https://doi.org/10.1529/biophysj.106.082487, PMID: 16766620
                                    Medintz IL, Clapp AR, Mattoussi H, Goldman ER, Fisher B, Mauro JM. 2003. Self-assembled nanoscale
                                     biosensors based on quantum dot FRET donors. Nature Materials 2:630–638. DOI: https://doi.org/10.1038/
                                     nmat961, PMID: 12942071
                                    Mekler V, Kortkhonjia E, Mukhopadhyay J, Knight J, Revyakin A, Kapanidis AN, Niu W, Ebright YW, Levy R,
                                     Ebright RH. 2002. Structural organization of bacterial RNA polymerase holoenzyme and the RNA polymerase-
                                     promoter open complex. Cell 108:599–614. DOI: https://doi.org/10.1016/S0092-8674(02)00667-0, PMID: 11
                                     893332
                                    Metskas LA, Rhoades E. 2020. Single-Molecule FRET of intrinsically disordered proteins. Annual Review of
                                     Physical Chemistry 71:391–414. DOI: https://doi.org/10.1146/annurev-physchem-012420-104917, PMID: 320
                                     97582
                                    Meyer BH, Martinez KL, Segura JM, Pascoal P, Hovius R, George N, Johnsson K, Vogel H. 2006a. Covalent
                                     labeling of cell-surface proteins for in-vivo FRET studies. FEBS Letters 580:1654–1658. DOI: https://doi.org/10.
                                     1016/j.febslet.2006.02.007, PMID: 16497304
                                    Meyer BH, Segura JM, Martinez KL, Hovius R, George N, Johnsson K, Vogel H. 2006b. FRET imaging reveals
                                     that functional neurokinin-1 receptors are monomeric and reside in membrane microdomains of live cells.
                                     PNAS 103:2138–2143. DOI: https://doi.org/10.1073/pnas.0507686103, PMID: 16461466
                                    Michalet X, Weiss S, Jäger M. 2006. Single-molecule fluorescence studies of protein folding and conformational
                                     dynamics. Chemical Reviews 106:1785–1813. DOI: https://doi.org/10.1021/cr0404343, PMID: 16683755
                                    Michie MS, Götz R, Franke C, Bowler M, Kumari N, Magidson V, Levitus M, Loncarek J, Sauer M, Schnermann
                                     MJ. 2017. Cyanine conformational restraint in the far-red range. Journal of the American Chemical Society 139:
                                     12406–12409. DOI: https://doi.org/10.1021/jacs.7b07272, PMID: 28862842
                                    Milles S, Tyagi S, Banterle N, Koehler C, VanDelinder V, Plass T, Neal AP, Lemke EA. 2012. Click strategies for
                                     single-molecule protein fluorescence. Journal of the American Chemical Society 134:5187–5195. DOI: https://
                                     doi.org/10.1021/ja210587q, PMID: 22356317
                                    Milles S, Mercadante D, Aramburu IV, Jensen MR, Banterle N, Koehler C, Tyagi S, Clarke J, Shammas SL,
                                     Blackledge M, Gräter F, Lemke EA. 2015. Plasticity of an ultrafast interaction between nucleoporins and nuclear
                                     transport receptors. Cell 163:734–745. DOI: https://doi.org/10.1016/j.cell.2015.09.047, PMID: 26456112
                                    Möckel C, Kubiak J, Schillinger O, Kühnemuth R, Della Corte D, Schröder GF, Willbold D, Strodel B, Seidel CAM,
                                     Neudecker P. 2019. Integrated NMR, fluorescence, and molecular dynamics benchmark study of protein
                                     mechanics and hydrodynamics. The Journal of Physical Chemistry B 123:1453–1480. DOI: https://doi.org/10.
                                     1021/acs.jpcb.8b08903, PMID: 30525615
                                    Moffat K. 2001. Time-resolved biochemical crystallography: a mechanistic perspective. Chemical Reviews 101:
                                     1569–1582. DOI: https://doi.org/10.1021/cr990039q, PMID: 11709992
                                    Moosa MM, Goodman AZ, Ferreon JC, Lee CW, Ferreon ACM, Deniz AA. 2018. Denaturant-specific effects on
                                     the structural energetics of a protein-denatured ensemble. European Biophysics Journal 47:89–94.
                                     DOI: https://doi.org/10.1007/s00249-017-1260-4, PMID: 29080139
                                    Morse JC, Girodat D, Burnett BJ, Holm M, Altman RB, Sanbonmatsu KY, Wieden HJ, Blanchard SC. 2020.
                                     Elongation factor-Tu can repetitively engage aminoacyl-tRNA within the ribosome during the proofreading
                                     stage of tRNA selection. PNAS 117:3610–3620. DOI: https://doi.org/10.1073/pnas.1904469117,
                                     PMID: 32024753
                                    Morten MJ, Steinmark IE, Magennis SW. 2020. Probing DNA dynamics: stacking-induced fluorescence increase
                                     (SIFI) versus FRET. ChemPhotoChem 4:664–667. DOI: https://doi.org/10.1002/cptc.202000069
                                    Mujumdar RB, Ernst LA, Mujumdar SR, Lewis CJ, Waggoner AS. 1993. Cyanine dye labeling reagents:
                                     sulfoindocyanine succinimidyl esters. Bioconjugate Chemistry 4:105–111. DOI: https://doi.org/10.1021/
                                     bc00020a001, PMID: 7873641
                                    Müller JD, Chen Y, Gratton E. 2000. Resolving heterogeneity on the single molecular level with the photon-
                                     counting histogram. Biophysical Journal 78:474–486. DOI: https://doi.org/10.1016/S0006-3495(00)76610-0,
                                     PMID: 10620311
                                    Müller BK, Zaychikov E, Bräuchle C, Lamb DC. 2005. Pulsed interleaved excitation. Biophysical Journal 89:3508–
                                     3522. DOI: https://doi.org/10.1529/biophysj.105.064766, PMID: 16113120
                                    Munro JB, Altman RB, O’Connor N, Blanchard SC. 2007. Identification of two distinct hybrid state intermediates
                                     on the ribosome. Molecular Cell 25:505–517. DOI: https://doi.org/10.1016/j.molcel.2007.01.022,
                                     PMID: 17317624
                                    Munro JB, Altman RB, Tung CS, Cate JH, Sanbonmatsu KY, Blanchard SC. 2010. Spontaneous formation of the
                                     unlocked state of the ribosome is a multistep process. PNAS 107:709–714. DOI: https://doi.org/10.1073/pnas.
                                     0908597107, PMID: 20018653
                                    Munro JB, Gorman J, Ma X, Zhou Z, Arthos J, Burton DR, Koff WC, Courter JR, Smith AB, Kwong PD, Blanchard
                                     SC, Mothes W. 2014. Conformational dynamics of single HIV-1 envelope trimers on the surface of native
                                     virions. Science 346:759–763. DOI: https://doi.org/10.1126/science.1254426, PMID: 25298114
                                    Munro JB, Lee KK. 2018. Probing structural variation and dynamics in the HIV-1 env fusion glycoprotein. Current
                                     HIV Research 16:5–12. DOI: https://doi.org/10.2174/1570162X16666171222110025
                                    Murakami K, Elmlund H, Kalisman N, Bushnell DA, Adams CM, Azubel M, Elmlund D, Levi-Kalisman Y, Liu X,
                                     Gibbons BJ, Levitt M, Kornberg RD. 2013. Architecture of an RNA polymerase II transcription pre-initiation
                                     complex. Science 342:1238724. DOI: https://doi.org/10.1126/science.1238724, PMID: 24072820


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                               58 of 69



                                    Muschielok A, Andrecka J, Jawhari A, Brückner F, Cramer P, Michaelis J. 2008. A nano-positioning system for
                                     macromolecular structural analysis. Nature Methods 5:965–971. DOI: https://doi.org/10.1038/nmeth.1259,
                                     PMID: 18849988
                                    Muschielok A, Michaelis J. 2011. Application of the nano-positioning system to the analysis of fluorescence
                                     resonance energy transfer networks. The Journal of Physical Chemistry B 115:11927–11937. DOI: https://doi.
                                     org/10.1021/jp2060377, PMID: 21888382
                                    Na S, Paek E. 2020. Computational methods in mass spectrometry-based structural proteomics for studying
                                     protein structure, dynamics, and interactions. Computational and Structural Biotechnology Journal 18:1391–
                                     1402. DOI: https://doi.org/10.1016/j.csbj.2020.06.002, PMID: 32637038
                                    Nagy J, Grohmann D, Cheung AC, Schulz S, Smollett K, Werner F, Michaelis J. 2015. Complete architecture of
                                     the archaeal RNA polymerase open complex from single-molecule FRET and NPS. Nature Communications 6:
                                     6161. DOI: https://doi.org/10.1038/ncomms7161, PMID: 25635909
                                    Nagy P, Szabó Á, Váradi T, Kovács T, Batta G, Szöllősi J. 2016. rFRET: a comprehensive, Matlab-based program
                                     for analyzing intensity-based ratiometric microscopic FRET experiments. Cytometry Part A 89:376–384.
                                     DOI: https://doi.org/10.1002/cyto.a.22828
                                    Nagy J, Eilert T, Michaelis J. 2018. Precision and accuracy in smFRET based structural studies—A benchmark
                                     study of the Fast-Nano-Positioning system. The Journal of Chemical Physics 148:123308. DOI: https://doi.org/
                                     10.1063/1.5006477, PMID: 29604844
                                    Nasir I, Onuchic PL, Labra SR, Deniz AA. 2019. Single-molecule fluorescence studies of intrinsically disordered
                                     proteins and liquid phase separation. Biochimica Et Biophysica Acta (BBA) - Proteins and Proteomics 1867:
                                     980–987. DOI: https://doi.org/10.1016/j.bbapap.2019.04.007, PMID: 31054969
                                    Nasir I, Bentley EP, Deniz AA. 2020. Ratiometric Single-Molecule FRET measurements to probe conformational
                                     subpopulations of intrinsically disordered proteins. Current Protocols in Chemical Biology 12:e80. DOI: https://
                                     doi.org/10.1002/cpch.80, PMID: 32159932
                                    Nawrocki G, Karaboga A, Sugita Y, Feig M. 2019. Effect of protein-protein interactions and solvent viscosity on
                                     the rotational diffusion of proteins in crowded environments. Physical Chemistry Chemical Physics 21:876–883.
                                     DOI: https://doi.org/10.1039/C8CP06142D, PMID: 30560249
                                    Nettels D, Gopich IV, Hoffmann A, Schuler B. 2007. Ultrafast dynamics of protein collapse from single-molecule
                                     photon statistics. PNAS 104:2655–2660. DOI: https://doi.org/10.1073/pnas.0611093104, PMID: 17301233
                                    Nettels D, Hoffmann A, Schuler B. 2008. Unfolded protein and peptide dynamics investigated with single-
                                     molecule FRET and correlation spectroscopy from picoseconds to seconds. The Journal of Physical Chemistry B
                                     112:6137–6146. DOI: https://doi.org/10.1021/jp076971j, PMID: 18410159
                                    Nettels D, Müller-Späth S, Küster F, Hofmann H, Haenni D, Rüegger S, Reymond L, Hoffmann A, Kubelka J,
                                     Heinz B, Gast K, Best RB, Schuler B. 2009. Single-molecule spectroscopy of the temperature-induced collapse
                                     of unfolded proteins. PNAS 106:20740–20745. DOI: https://doi.org/10.1073/pnas.0900622106, PMID: 1
                                     9933333
                                    Nettels D, Haenni D, Maillot S, Gueye M, Barth A, Hirschfeld V, Hübner CG, Léonard J, Schuler B. 2015. Excited-
                                     state annihilation reduces power dependence of single-molecule FRET experiments. Physical Chemistry
                                     Chemical Physics 17:32304–32315. DOI: https://doi.org/10.1039/C5CP05321H, PMID: 26584062
                                    Nettels D, Schuler B. 2020. Fretica. University of Zurich. https://schuler.bioc.uzh.ch/programs/.
                                    Neubauer H, Gaiko N, Berger S, Schaffer J, Eggeling C, Tuma J, Verdier L, Seidel CA, Griesinger C, Volkmer A.
                                     2007. Orientational and dynamical heterogeneity of rhodamine 6G terminally attached to a DNA helix revealed
                                     by NMR and single-molecule fluorescence spectroscopy. Journal of the American Chemical Society 129:12746–
                                     12755. DOI: https://doi.org/10.1021/ja0722574, PMID: 17900110
                                    Nickels PC, Wünsch B, Holzmeister P, Bae W, Kneer LM, Grohmann D, Tinnefeld P, Liedl T. 2016. Molecular
                                     force spectroscopy with a DNA origami-based nanoscopic force clamp. Science 354:305–307. DOI: https://doi.
                                     org/10.1126/science.aah5974, PMID: 27846560
                                    Nienhaus GU. 2006. Exploring protein structure and dynamics under denaturing conditions by single-molecule
                                     FRET analysis. Macromolecular Bioscience 6:907–922. DOI: https://doi.org/10.1002/mabi.200600158,
                                     PMID: 17099864
                                    Nir E, Michalet X, Hamadani KM, Laurence TA, Neuhauser D, Kovchegov Y, Weiss S. 2006. Shot-noise limited
                                     single-molecule FRET histograms: comparison between theory and experiments. The Journal of Physical
                                     Chemistry B 110:22103–22124. DOI: https://doi.org/10.1021/jp063483n, PMID: 17078646
                                    Oh E, Hong MY, Lee D, Nam SH, Yoon HC, Kim HS. 2005. Inhibition assay of biomolecules based on
                                     fluorescence resonance energy transfer (FRET) between quantum dots and gold nanoparticles. Journal of the
                                     American Chemical Society 127:3270–3271. DOI: https://doi.org/10.1021/ja0433323, PMID: 15755131
                                    Okamoto K, Hibino K, Sako Y. 2020. In-cell single-molecule FRET measurements reveal three conformational
                                     state changes in RAF protein. Biochimica Et Biophysica Acta (BBA) - General Subjects 1864:129358.
                                     DOI: https://doi.org/10.1016/j.bbagen.2019.04.022, PMID: 31071411
                                    Okumus B, Wilson TJ, Lilley DM, Ha T. 2004. Vesicle encapsulation studies reveal that single molecule ribozyme
                                     heterogeneities are intrinsic. Biophysical Journal 87:2798–2806. DOI: https://doi.org/10.1529/biophysj.104.
                                     045971, PMID: 15454471
                                    Olofsson L, Felekyan S, Doumazane E, Scholler P, Fabre L, Zwier JM, Rondard P, Seidel CA, Pin JP, Margeat E.
                                     2014. Fine tuning of sub-millisecond conformational dynamics controls metabotropic glutamate receptors
                                     agonist efficacy. Nature Communications 5:5206. DOI: https://doi.org/10.1038/ncomms6206, PMID: 25323157


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                59 of 69



                                    Orevi T, Lerner E, Rahamim G, Amir D, Haas E. 2014. Ensemble and single-molecule detected time-resolved
                                      FRET methods in studies of protein conformations and dynamics. Methods in Molecular Biology 1076:113–169.
                                      DOI: https://doi.org/10.1007/978-1-62703-649-8_7, PMID: 24108626
                                    Ouellet J, Schorr S, Iqbal A, Wilson TJ, Lilley DM. 2011. Orientation of cyanine fluorophores terminally attached
                                      to DNA via long, flexible tethers. Biophysical Journal 101:1148–1154. DOI: https://doi.org/10.1016/j.bpj.2011.
                                      07.007, PMID: 21889452
                                    Palmer AG. 2004. NMR characterization of the dynamics of biomacromolecules. Chemical Reviews 104:3623–
                                      3640. DOI: https://doi.org/10.1021/cr030413t, PMID: 15303831
                                    Park SR, Hauver J, Zhang Y, Revyakin A, Coleman RA, Tjian R, Chu S, Pertsinidis A. 2020. A single-molecule
                                      surface-based platform to detect the assembly and function of the human RNA polymerase II transcription
                                      machinery. Structure 28:1337–1343. DOI: https://doi.org/10.1016/j.str.2020.07.009, PMID: 32763141
                                    Pati AK, El Bakouri O, Jockusch S, Zhou Z, Altman RB, Fitzgerald GA, Asher WB, Terry DS, Borgia A, Holsey MD,
                                      Batchelder JE, Abeywickrama C, Huddle B, Rufa D, Javitch JA, Ottosson H, Blanchard SC. 2020. Tuning the
                                      Baird aromatic triplet-state energy of cyclooctatetraene to maximize the self-healing mechanism in organic
                                      fluorophores. PNAS 117:24305–24315. DOI: https://doi.org/10.1073/pnas.2006517117, PMID: 32913060
                                    Periasamy A, Wallrabe H, Chen Y, Barroso M. 2008. Chapter 22: quantitation of protein-protein interactions:
                                      confocal FRET microscopy. Methods in Cell Biology 89:569–598. DOI: https://doi.org/10.1016/S0091-679X(08)
                                      00622-5, PMID: 19118691
                                    Peter MF, Gebhardt C, Mächtel R, Glaenzer J, Thomas GH, Cordes T, Hagelueken G. 2020. Cross-validation of
                                      distance measurements in proteins by PELDOR/DEER and single-molecule FRET. bioRxiv. DOI: https://doi.org/
                                      10.1101/2020.11.23.394080
                                    Peulen TO, Opanasyuk O, Seidel CAM. 2017. Combining graphical and analytical methods with molecular
                                      simulations to analyze time-resolved FRET measurements of labeled macromolecules accurately. The Journal of
                                      Physical Chemistry B 121:8211–8241. DOI: https://doi.org/10.1021/acs.jpcb.7b03441, PMID: 28709377
                                    Peulen TO, Hengstenberg CS, Biehl R, Dimura M, Lorenz C, Valeri A, Ince S, Vöpel T, Faragó B, Gohlke H, Klare
                                      JP, Stadler AM, Seidel CAM, Herrmann C. 2020. Integrative dynamic structural biology unveils conformers
                                      essential for the oligomerization of a large GTPase. arXiv. https://arxiv.org/abs/2004.04229.
                                    Pfiffi D, Bier BA, Marian CM, Schaper K, Seidel CA. 2010. Diphenylhexatrienes as photoprotective agents for
                                      ultrasensitive fluorescence detection. The Journal of Physical Chemistry A 114:4099–4108. DOI: https://doi.
                                      org/10.1021/jp909033x, PMID: 20218613
                                    Pieper CM, Enderlein J. 2011. Fluorescence correlation spectroscopy as a tool for measuring the rotational
                                      diffusion of macromolecules. Chemical Physics Letters 516:1–11. DOI: https://doi.org/10.1016/j.cplett.2011.06.
                                    Pirchi M, Ziv G, Riven I, Cohen SS, Zohar N, Barak Y, Haran G. 2011. Single-molecule fluorescence spectroscopy
                                      maps the folding landscape of a large protein. Nature Communications 2:493. DOI: https://doi.org/10.1038/
                                      ncomms1504, PMID: 21988909
                                    Pirchi M, Tsukanov R, Khamis R, Tomov TE, Berger Y, Khara DC, Volkov H, Haran G, Nir E. 2016. Photon-by-
                                      photon hidden Markov model analysis for microsecond single-molecule FRET kinetics. The Journal of Physical
                                      Chemistry B 120:13065–13075. DOI: https://doi.org/10.1021/acs.jpcb.6b10726, PMID: 27977207
                                    Plochowietz A, Crawford R, Kapanidis AN. 2014. Characterization of organic fluorophores for in vivo FRET
                                      studies based on electroporated molecules. Phys. Chem. Chem. Phys. 16:12688–12694. DOI: https://doi.org/
                                      10.1039/C4CP00995A, PMID: 24837080
                                    Plochowietz A, El-Sagheer AH, Brown T, Kapanidis AN. 2016. Stable end-sealed DNA as robust nano-rulers for
                                      in vivo single-molecule fluorescence. Chemical Science 7:4418–4422. DOI: https://doi.org/10.1039/
                                      C6SC00639F, PMID: 30155088
                                    Plochowietz A, Farrell I, Smilansky Z, Cooperman BS, Kapanidis AN. 2017. In vivo single-RNA tracking shows
                                      that most tRNA diffuses freely in live Bacteria. Nucleic Acids Research 45:926–937. DOI: https://doi.org/10.
                                      1093/nar/gkw787, PMID: 27625389
                                    Ploetz E, Lerner E, Husada F, Roelfs M, Chung S, Hohlbein J, Weiss S, Cordes T. 2016. Förster resonance energy
                                      transfer and protein-induced fluorescence enhancement as synergetic multi-scale molecular rulers. Scientific
                                      Reports 6:33257. DOI: https://doi.org/10.1038/srep33257, PMID: 27641327
                                    Popov KI, Makepeace KAT, Petrotchenko EV, Dokholyan NV, Borchers CH. 2019. Insight into the structure of the
                                      "Unstructured" Tau Protein. Structure 27:1710–1715. DOI: https://doi.org/10.1016/j.str.2019.09.003,
                                      PMID: 31628033
                                    Preus S, Noer SL, Hildebrandt LL, Gudnason D, Birkedal V. 2015. iSMS: single-molecule FRET microscopy
                                      software. Nature Methods 12:593–594. DOI: https://doi.org/10.1038/nmeth.3435, PMID: 26125588
                                    Preus S, Hildebrandt LL, Birkedal V. 2016. Optimal background estimators in single-molecule FRET microscopy.
                                      Biophysical Journal 111:1278–1286. DOI: https://doi.org/10.1016/j.bpj.2016.07.047, PMID: 27653486
                                    Preuss S, Gudnason D, Birkedal V. 2020. iSMS: Single-molecule FRET microscopy software. Aarhus University.
                                      http://isms.au.dk
                                    Quast RB, Fatemi F, Kranendonk M, Margeat E, Truan G. 2019. Accurate determination of human CPR
                                      conformational equilibrium by smFRET using dual orthogonal noncanonical amino acid labeling. ChemBioChem
                                      20:659–666. DOI: https://doi.org/10.1002/cbic.201800607, PMID: 30427570
                                    Quast RB, Margeat E. 2019. Studying GPCR conformational dynamics by single molecule fluorescence. Molecular
                                      and Cellular Endocrinology 493:110469. DOI: https://doi.org/10.1016/j.mce.2019.110469, PMID: 31163201


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                               60 of 69



                                    Rahamim G, Chemerovski-Glikman M, Rahimipour S, Amir D, Haas E. 2015. Resolution of two sub-populations of
                                      conformers and their individual dynamics by time resolved ensemble level FRET measurements. PLOS ONE 10:
                                      e0143732. DOI: https://doi.org/10.1371/journal.pone.0143732, PMID: 26699718
                                    Ramanathan R, Muñoz V. 2015. A method for extracting the free energy surface and conformational dynamics of
                                      fast-folding proteins from single molecule photon trajectories. The Journal of Physical Chemistry B 119:7944–
                                      7956. DOI: https://doi.org/10.1021/acs.jpcb.5b03176, PMID: 25988351
                                    Ramirez-Carrozzi VR, Kerppola TK. 2001. Dynamics of Fos-Jun-NFAT1 complexes. PNAS 98:4893–4898.
                                      DOI: https://doi.org/10.1073/pnas.091095998, PMID: 11320240
                                    Ranjit S, Gurunathan K, Levitus M. 2009. Photophysics of backbone fluorescent DNA modifications: reducing
                                      uncertainties in FRET. The Journal of Physical Chemistry B 113:7861–7866. DOI: https://doi.org/10.1021/
                                      jp810842u, PMID: 19473039
                                    Rasnik I, McKinney SA, Ha T. 2006. Nonblinking and long-lasting single-molecule fluorescence imaging. Nature
                                      Methods 3:891–893. DOI: https://doi.org/10.1038/nmeth934, PMID: 17013382
                                    Ratzke C, Hellenkamp B, Hugel T. 2014. Four-colour FRET reveals directionality in the Hsp90 multicomponent
                                      machinery. Nature Communications 5:4192. DOI: https://doi.org/10.1038/ncomms5192, PMID: 24947016
                                    Ravera E, Salmon L, Fragai M, Parigi G, Al-Hashimi H, Luchinat C. 2014. Insights into domain-domain motions in
                                      proteins and RNA from solution NMR. Accounts of Chemical Research 47:3118–3126. DOI: https://doi.org/10.
                                      1021/ar5002318, PMID: 25148413
                                    Ray S, Chauvier A, Walter NG. 2019. Kinetics coming into focus: single-molecule microscopy of riboswitch
                                      dynamics. RNA Biology 16:1077–1085. DOI: https://doi.org/10.1080/15476286.2018.1536594, PMID: 30328748
                                    Reinartz I, Sinner C, Nettels D, Stucki-Buchli B, Stockmar F, Panek PT, Jacob CR, Nienhaus GU, Schuler B, Schug
                                      A. 2018. Simulation of FRET dyes allows quantitative comparison against experimental data. The Journal of
                                      Chemical Physics 148:123321. DOI: https://doi.org/10.1063/1.5010434, PMID: 29604831
                                    Reinkemeier CD, Girona GE, Lemke EA. 2019. Designer membraneless organelles enable codon reassignment of
                                      selected mRNAs in eukaryotes. Science 363:eaaw2644. DOI: https://doi.org/10.1126/science.aaw2644,
                                      PMID: 30923194
                                    Rhoades E, Gussakovsky E, Haran G. 2003. Watching proteins fold one molecule at a time. PNAS 100:3197–
                                      3202. DOI: https://doi.org/10.1073/pnas.2628068100, PMID: 12612345
                                    Riback JA, Bowman MA, Zmyslowski AM, Plaxco KW, Clark PL, Sosnick TR. 2019. Commonly used FRET
                                      fluorophores promote collapse of an otherwise disordered protein. PNAS 116:8889–8894. DOI: https://doi.
                                      org/10.1073/pnas.1813038116, PMID: 30992378
                                    Rieger R, Kobitski A, Sielaff H, Nienhaus GU. 2011. Evidence of a folding intermediate in RNase H from single-
                                      molecule FRET experiments. ChemPhysChem 12:627–633. DOI: https://doi.org/10.1002/cphc.201000693,
                                      PMID: 21344597
                                    Rigler R, , Widengren J, Kask P. 1993. Fluorescence correlation spectroscopy with high count rate and low
                                      background: analysis of translational diffusion. European Biophysics Journal 22:169–175. DOI: https://doi.org/
                                      10.1007/BF00185777
                                    Robb NC, Te Velthuis AJW, Fodor E, Kapanidis AN. 2019. Real-time analysis of single influenza virus replication
                                      complexes reveals large promoter-dependent differences in initiation dynamics. Nucleic Acids Research 47:
                                      6466–6477. DOI: https://doi.org/10.1093/nar/gkz313, PMID: 31032520
                                    Rothwell PJ, Berger S, Kensch O, Felekyan S, Antonik M, Wöhrl BM, Restle T, Goody RS, Seidel CA. 2003.
                                      Multiparameter single-molecule fluorescence spectroscopy reveals heterogeneity of HIV-1 reverse
                                      transcriptase:primer/template complexes. PNAS 100:1655–1660. DOI: https://doi.org/10.1073/pnas.
                                      0434003100, PMID: 12578980
                                    Roy R, Hohng S, Ha T. 2008. A practical guide to single-molecule FRET. Nature Methods 5:507–516.
                                      DOI: https://doi.org/10.1038/nmeth.1208, PMID: 18511918
                                    Sabanayagam CR, Eid JS, Meller A. 2004. High-throughput scanning confocal microscope for single molecule
                                      analysis. Applied Physics Letters 84:1216–1218. DOI: https://doi.org/10.1063/1.1646725
                                    Sadoine M, Cerminara M, Kempf N, Gerrits M, Fitter J, Katranidis A. 2017. Selective double-labeling of cell-free
                                      synthesized proteins for more accurate smFRET studies. Analytical Chemistry 89:11278–11285. DOI: https://
                                      doi.org/10.1021/acs.analchem.7b01639, PMID: 29022338
                                    Sakon JJ, Weninger KR. 2010. Detecting the conformation of individual proteins in live cells. Nature Methods 7:
                                      203–205. DOI: https://doi.org/10.1038/nmeth.1421
                                    Salem C-B, Ploetz E, Lamb DC. 2019. Chapter 2 - Probing dynamics in single molecules. In: Johnson CK (Ed).
                                      Developments in Physical & Theoretical Chemistry, Spectroscopy and Dynamics of Single Molecules. Elsevier.
                                      p. 71–115. DOI: https://doi.org/10.1016/B978-0-12-816463-1.00002-X
                                    Sali A, Berman HM, Schwede T, Trewhella J, Kleywegt G, Burley SK, Markley J, Nakamura H, Adams P, Bonvin
                                      AM, Chiu W, Peraro MD, Di Maio F, Ferrin TE, Grünewald K, Gutmanas A, Henderson R, Hummer G, Iwasaki K,
                                      Johnson G, et al. 2015. Outcome of the first wwPDB hybrid/Integrative methods task force workshop. Structure
                                      23:1156–1167. DOI: https://doi.org/10.1016/j.str.2015.05.013, PMID: 26095030
                                    Sanabria H, Rodnin D, Hemmen K, Peulen TO, Felekyan S, Fleissner MR, Dimura M, Koberling F, Kühnemuth R,
                                      Hubbell W, Gohlke H, Seidel CAM. 2020. Resolving dynamics and function of transient states in single enzyme
                                      molecules. Nature Communications 11:1231. DOI: https://doi.org/10.1038/s41467-020-14886-w,
                                      PMID: 32144241
                                    Sanborn ME, Connolly BK, Gurunathan K, Levitus M. 2007. Fluorescence properties and photophysics of the
                                      sulfoindocyanine Cy3 linked covalently to DNA. The Journal of Physical Chemistry B 111:11064–11074.
                                      DOI: https://doi.org/10.1021/jp072912u, PMID: 17718469


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                              61 of 69



                                    Sánchez-Rico C, Voith von Voithenberg L, Warner L, Lamb DC, Sattler M. 2017. Effects of fluorophore attachment
                                      on protein conformation and dynamics studied by spFRET and NMR spectroscopy. Chemistry - a European
                                      Journal 23:14267–14277. DOI: https://doi.org/10.1002/chem.201702423
                                    Santoso Y, Joyce CM, Potapova O, Le Reste L, Hohlbein J, Torella JP, Grindley ND, Kapanidis AN. 2010a.
                                      Conformational transitions in DNA polymerase I revealed by single-molecule FRET. PNAS 107:715–720.
                                      DOI: https://doi.org/10.1073/pnas.0910909107, PMID: 20080740
                                    Santoso Y, Torella JP, Kapanidis AN. 2010b. Characterizing single-molecule FRET dynamics with probability
                                      distribution analysis. ChemPhysChem 11:2209–2219. DOI: https://doi.org/10.1002/cphc.201000129,
                                      PMID: 20575136
                                    Sasmal DK, Pulido LE, Kasal S, Huang J. 2016. Single-molecule fluorescence resonance energy transfer in
                                      molecular biology. Nanoscale 8:19928–19944. DOI: https://doi.org/10.1039/C6NR06794H, PMID: 27883140
                                    Schafer FP, Zhang F-G, Jethwa J. 1982. Intramolecular TT-energy transfer in bifluorophoric laser dyes. Applied
                                      Physics B Photophysics and Laser Chemistry 28:37–41. DOI: https://doi.org/10.1007/BF00693890
                                    Schaffer J, Volkmer A, Eggeling C, Subramaniam V, Striker G, Seidel CAM. 1999. Identification of single
                                      molecules in aqueous solution by time-resolved fluorescence anisotropy. The Journal of Physical Chemistry A
                                      103:331–336. DOI: https://doi.org/10.1021/jp9833597
                                    Schalch T, Duda S, Sargent DF, Richmond TJ. 2005. X-ray structure of a tetranucleosome and its implications for
                                      the chromatin fibre. Nature 436:138–141. DOI: https://doi.org/10.1038/nature03686, PMID: 16001076
                                    Schepers B, Gohlke H. 2020. AMBER-DYES in AMBER: implementation of fluorophore and linker parameters into
                                      AmberTools. The Journal of Chemical Physics 152:221103. DOI: https://doi.org/10.1063/5.0007630,
                                      PMID: 32534525
                                    Schirhagl R, Chang K, Loretz M, Degen CL. 2014. Nitrogen-vacancy centers in diamond: nanoscale sensors for
                                      physics and biology. Annual Review of Physical Chemistry 65:83–105. DOI: https://doi.org/10.1146/annurev-
                                      physchem-040513-103659, PMID: 24274702
                                    Schirra RT, Zhang P. 2014. Correlative fluorescence and electron microscopy. Current Protocols in Cytometry 10:
                                      1–10. DOI: https://doi.org/10.1002/0471142956.cy1236s70
                                    Schlichting I, Almo SC, Rapp G, Wilson K, Petratos K, Lentfer A, Wittinghofer A, Kabsch W, Pai EF, Petsko GA.
                                      1990. Time-resolved X-ray crystallographic study of the conformational change in Ha-Ras p21 protein on GTP
                                      hydrolysis. Nature 345:309–315. DOI: https://doi.org/10.1038/345309a0, PMID: 2111463
                                    Schlichting I, Chu K. 2000. Trapping intermediates in the crystal: ligand binding to myoglobin. Current Opinion
                                      in Structural Biology 10:744–752. DOI: https://doi.org/10.1016/S0959-440X(00)00158-5, PMID: 11114513
                                    Schluesche P, Stelzer G, Piaia E, Lamb DC, Meisterernst M. 2007. NC2 mobilizes TBP on core promoter TATA
                                      boxes. Nature Structural & Molecular Biology 14:1196–1201. DOI: https://doi.org/10.1038/nsmb1328,
                                      PMID: 17994103
                                    Schmid S, Götz M, Hugel T. 2016. Single-molecule analysis beyond dwell times: demonstration and assessment
                                      in and out of equilibrium. Biophysical Journal 111:1375–1384. DOI: https://doi.org/10.1016/j.bpj.2016.08.023,
                                      PMID: 27705761
                                    Schneider S, Paulsen H, Reiter KC, Hinze E, Schiene-Fischer C, Hübner CG. 2018. Single molecule FRET
                                      investigation of pressure-driven unfolding of cold shock protein A. The Journal of Chemical Physics 148:
                                      123336. DOI: https://doi.org/10.1063/1.5009662, PMID: 29604829
                                    Schotte F, Lim M, Jackson TA, Smirnov AV, Soman J, Olson JS, Phillips GN, Wulff M, Anfinrud PA. 2003.
                                      Watching a protein as it functions with 150-ps time-resolved x-ray crystallography. Science 300:1944–1947.
                                      DOI: https://doi.org/10.1126/science.1078797, PMID: 12817148
                                    Schrimpf W, Barth A, Hendrix J, Lamb DC. 2018. PAM: a framework for integrated analysis of imaging, single-
                                      molecule, and ensemble fluorescence data. Biophysical Journal 114:1518–1528. DOI: https://doi.org/10.1016/j.
                                      bpj.2018.02.035, PMID: 29642023
                                    Schuler B, Lipman EA, Eaton WA. 2002. Probing the free-energy surface for protein folding with single-molecule
                                      fluorescence spectroscopy. Nature 419:743–747. DOI: https://doi.org/10.1038/nature01060, PMID: 12384704
                                    Schuler B, Lipman EA, Steinbach PJ, Kumke M, Eaton WA. 2005. Polyproline and the "spectroscopic ruler"
                                      revisited with single-molecule fluorescence. PNAS 102:2754–2759. DOI: https://doi.org/10.1073/pnas.
                                      0408164102, PMID: 15699337
                                    Schuler B, Soranno A, Hofmann H, Nettels D. 2016. Single-molecule FRET spectroscopy and the polymer physics
                                      of unfolded and intrinsically disordered proteins. Annual Review of Biophysics 45:207–231. DOI: https://doi.
                                      org/10.1146/annurev-biophys-062215-010915, PMID: 27145874
                                    Schuler B. 2018. Perspective: chain dynamics of unfolded and intrinsically disordered proteins from nanosecond
                                      fluorescence correlation spectroscopy combined with single-molecule FRET. The Journal of Chemical Physics
                                      149:10901. DOI: https://doi.org/10.1063/1.5037683
                                    Schuler B, Borgia A, Borgia MB, Heidarsson PO, Holmstrom ED, Nettels D, Sottini A. 2020. Binding without
                                      folding - the biomolecular function of disordered polyelectrolyte complexes. Current Opinion in Structural
                                      Biology 60:66–76. DOI: https://doi.org/10.1016/j.sbi.2019.12.006, PMID: 31874413
                                    Schuler B, Hofmann H. 2013. Single-molecule spectroscopy of protein folding dynamics—expanding scope and
                                      timescales. Current Opinion in Structural Biology 23:36–47. DOI: https://doi.org/10.1016/j.sbi.2012.10.008,
                                      PMID: 23312353
                                    Seefeldt B, Kasper R, Seidel T, Tinnefeld P, Dietz KJ, Heilemann M, Sauer M. 2008. Fluorescent proteins for
                                      single-molecule fluorescence applications. Journal of Biophotonics 1:74–82. DOI: https://doi.org/10.1002/jbio.
                                      200710024, PMID: 19343637


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                               62 of 69



                                    Segal M, Ingargiola A, Lerner E, Chung S, White JA, Streets A, Weiss S, Michalet X. 2019. High-throughput
                                      smFRET analysis of freely diffusing nucleic acid molecules and associated proteins. Methods 169:21–45.
                                      DOI: https://doi.org/10.1016/j.ymeth.2019.07.021, PMID: 31356875
                                    Sekhar A, Kay LE. 2019. An NMR view of protein dynamics in health and disease. Annual Review of Biophysics
                                      48:297–319. DOI: https://doi.org/10.1146/annurev-biophys-052118-115647, PMID: 30901260
                                    Selvin PR, Ha T. 2008. Single-Molecule Techniques. Cold Spring Harbor Laboratory Press.
                                    Sgouralis I, Madaan S, Djutanta F, Kha R, Hariadi RF, Pressé S. 2019. A Bayesian nonparametric approach to
                                      single molecule Förster resonance energy transfer. The Journal of Physical Chemistry B 123:675–688.
                                      DOI: https://doi.org/10.1021/acs.jpcb.8b09752, PMID: 30571128
                                    Sgouralis I, Pressé S. 2017. An introduction to infinite HMMs for single-molecule data analysis. Biophysical
                                      Journal 112:2021–2029. DOI: https://doi.org/10.1016/j.bpj.2017.04.027, PMID: 28538142
                                    Shaner NC, Patterson GH, Davidson MW. 2007. Advances in fluorescent protein technology. Journal of Cell
                                      Science 120:4247–4260. DOI: https://doi.org/10.1242/jcs.005801, PMID: 18057027
                                    Shaw RA, Johnston-Wood T, Ambrose B, Craggs TD, Hill JG. 2020. CHARMM-DYES: parameterization of
                                      fluorescent dyes for use with the CHARMM force field. Journal of Chemical Theory and Computation 16:7817–
                                      7824. DOI: https://doi.org/10.1021/acs.jctc.0c00721, PMID: 33226216
                                    Sherman E, Haran G. 2006. Coil-globule transition in the denatured state of a small protein. PNAS 103:11539–
                                      11543. DOI: https://doi.org/10.1073/pnas.0601395103, PMID: 16857738
                                    Shi L, De Paoli V, Rosenzweig N, Rosenzweig Z. 2006. Synthesis and application of quantum dots FRET-based
                                      protease sensors. Journal of the American Chemical Society 128:10378–10379. DOI: https://doi.org/10.1021/
                                      ja063509o, PMID: 16895398
                                    Shoura MJ, Ranatunga R, Harris SA, Nielsen SO, Levene SD. 2014. Contribution of fluorophore dynamics and
                                      solvation to resonant energy transfer in protein-DNA complexes: a molecular-dynamics study. Biophysical
                                      Journal 107:700–710. DOI: https://doi.org/10.1016/j.bpj.2014.06.023, PMID: 25099809
                                    Shuang B, Cooper D, Taylor JN, Kisley L, Chen J, Wang W, Li CB, Komatsuzaki T, Landes CF. 2014. Fast step
                                      transition and state identification (STaSI) for discrete single-molecule data analysis. The Journal of Physical
                                      Chemistry Letters 5:3157–3161. DOI: https://doi.org/10.1021/jz501435p, PMID: 25247055
                                    Sindbert S, Kalinin S, Nguyen H, Kienzler A, Clima L, Bannwarth W, Appel B, Müller S, Seidel CA. 2011. Accurate
                                      distance determination of nucleic acids via förster resonance energy transfer: implications of dye linker length
                                      and rigidity. Journal of the American Chemical Society 133:2463–2480. DOI: https://doi.org/10.1021/
                                      ja105725e, PMID: 21291253
                                    Sisamakis E, Valeri A, Kalinin S, Rothwell PJ, Seidel CA. 2010. Accurate single-molecule FRET studies using
                                      multiparameter fluorescence detection. Methods in Enzymology 475:455–514. DOI: https://doi.org/10.1016/
                                      S0076-6879(10)75018-7, PMID: 20627168
                                    Slavin M, Kalisman N. 2018. Structural analysis of protein complexes by cross-linking and mass spectrometry. In:
                                      Marsh J. A (Ed). Methods in Molecular Biology. Springer. p. 173–183. DOI: https://doi.org/10.1007/978-1-
                                      4939-7759-8_11
                                    Soleimaninejad H, Chen MZ, Lou X, Smith TA, Hong Y. 2017. Measuring macromolecular crowding in cells
                                      through fluorescence anisotropy imaging with an AIE fluorogen. Chemical Communications 53:2874–2877.
                                      DOI: https://doi.org/10.1039/C6CC09916E
                                    Somssich M, Ma Q, Weidtkamp-Peters S, Stahl Y, Felekyan S, Bleckmann A, Seidel CA, Simon R. 2015. Real-time
                                      dynamics of peptide ligand-dependent receptor complex formation in planta. Science Signaling 8:ra76.
                                      DOI: https://doi.org/10.1126/scisignal.aab0598, PMID: 26243190
                                    Song F, Chen P, Sun D, Wang M, Dong L, Liang D, Xu RM, Zhu P, Li G. 2014. Cryo-EM study of the chromatin
                                      fiber reveals a double helix twisted by tetranucleosomal units. Science 344:376–380. DOI: https://doi.org/10.
                                      1126/science.1251413, PMID: 24763583
                                    Soranno A, Buchli B, Nettels D, Cheng RR, Müller-Späth S, Pfeil SH, Hoffmann A, Lipman EA, Makarov DE,
                                      Schuler B. 2012. Quantifying internal friction in unfolded and intrinsically disordered proteins with single-
                                      molecule spectroscopy. PNAS 109:17800–17806. DOI: https://doi.org/10.1073/pnas.1117368109, PMID: 22492
                                    Soranno A, Koenig I, Borgia MB, Hofmann H, Zosel F, Nettels D, Schuler B. 2014. Single-molecule spectroscopy
                                      reveals polymer effects of disordered proteins in crowded environments. PNAS 111:4874–4879. DOI: https://
                                      doi.org/10.1073/pnas.1322611111, PMID: 24639500
                                    Sottini A, Borgia A, Borgia MB, Bugge K, Nettels D, Chowdhury A, Heidarsson PO, Zosel F, Best RB, Kragelund
                                      BB, Schuler B. 2020. Polyelectrolyte interactions enable rapid association and dissociation in high-affinity
                                      disordered protein complexes. Nature Communications 11:5736. DOI: https://doi.org/10.1038/s41467-020-
                                      18859-x, PMID: 33184256
                                    Spiegel JD, Fulle S, Kleinschmidt M, Gohlke H, Marian CM. 2016. Failure of the IDA in FRET systems at close
                                      inter-dye distances is moderated by frequent low k2 Values. The Journal of Physical Chemistry B 120:8845–
                                      8862. DOI: https://doi.org/10.1021/acs.jpcb.6b05754, PMID: 27490865
                                    Squires AH, Moerner WE. 2017. Direct single-molecule measurements of phycocyanobilin photophysics in
                                      monomeric C-phycocyanin. PNAS 114:9779–9784. DOI: https://doi.org/10.1073/pnas.1705435114, PMID: 2
                                      8847963
                                    Steffen FD, Sigel RK, Börner R. 2016. An atomistic view on carbocyanine photophysics in the realm of RNA.
                                      Physical Chemistry Chemical Physics 18:29045–29055. DOI: https://doi.org/10.1039/C6CP04277E, PMID: 277
                                      83069


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                 63 of 69


           Review Article                                            Biochemistry and Chemical Biology Structural Biology and Molecular Biophysics

                                    Steffen FD, Börner R, Freisinger E, Sigel RKO. 2019. Stick, flick, click: DNA-guided fluorescent labeling of long
                                      RNA for single-molecule FRET. CHIMIA International Journal for Chemistry 73:257–261. DOI: https://doi.org/
                                      10.2533/chimia.2019.257, PMID: 30975253
                                    Steffen FD, Khier M, Kowerko D, Cunha RA, Börner R, Sigel RKO. 2020. Metal ions and sugar puckering balance
                                      single-molecule kinetic heterogeneity in RNA and DNA tertiary contacts. Nature Communications 11:104.
                                      DOI: https://doi.org/10.1038/s41467-019-13683-4, PMID: 31913262
                                    Stein IH, Steinhauer C, Tinnefeld P. 2011. Single-molecule four-color FRET visualizes energy-transfer paths on
                                      DNA origami. Journal of the American Chemical Society 133:4193–4195. DOI: https://doi.org/10.1021/
                                      ja1105464, PMID: 21250689
                                    Steiner M, Karunatilaka KS, Sigel RK, Rueda D. 2008. Single-molecule studies of group II intron ribozymes. PNAS
                                      105:13853–13858. DOI: https://doi.org/10.1073/pnas.0804034105, PMID: 18772388
                                    Steinmetzger C, Bäuerlein C, Höbartner C. 2020. Supramolecular fluorescence resonance energy transfer in
                                      nucleobase-modified fluorogenic RNA aptamers. Angewandte Chemie International Edition 59:6760–6764.
                                      DOI: https://doi.org/10.1002/anie.201916707
                                    Stella S, Mesa P, Thomsen J, Paul B, Alcón P, Jensen SB, Saligram B, Moses ME, Hatzakis NS, Montoya G. 2018.
                                      Conformational activation promotes CRISPR-Cas12a catalysis and resetting of the endonuclease activity. Cell
                                      175:1856–1871. DOI: https://doi.org/10.1016/j.cell.2018.10.045, PMID: 30503205
                                    Strickler SJ, Berg RA. 1962. Relationship between absorption intensity and fluorescence lifetime of molecules.
                                      The Journal of Chemical Physics 37:814–822. DOI: https://doi.org/10.1063/1.1733166
                                    Stryer L, Haugland RP. 1967. Energy transfer: a spectroscopic ruler. PNAS 58:719–726. DOI: https://doi.org/10.
                                      1073/pnas.58.2.719, PMID: 5233469
                                    Sturzenegger F, Zosel F, Holmstrom ED, Buholzer KJ, Makarov DE, Nettels D, Schuler B. 2018. Transition path
                                      times of coupled folding and binding reveal the formation of an encounter complex. Nature Communications
                                      9:4708. DOI: https://doi.org/10.1038/s41467-018-07043-x, PMID: 30413694
                                    Sugita Y, Feig M. 2020. All-atom molecular dynamics simulation of proteins in crowded environments. In-Cell
                                      NMR Spectroscopy 10:228–248. DOI: https://doi.org/10.1039/9781788013079-00228
                                    Sung HL, Nesbitt DJ. 2020. Correction: high pressure single-molecule FRET studies of the lysine riboswitch:
                                      cationic and osmolytic effects on pressure induced denaturation. Physical Chemistry Chemical Physics 22:
                                      17008–17009. DOI: https://doi.org/10.1039/D0CP90155E, PMID: 32726381
                                    Sustarsic M, Plochowietz A, Aigrain L, Yuzenkova Y, Zenkin N, Kapanidis A. 2014. Optimized delivery of
                                      fluorescently labeled proteins in live bacteria using electroporation. Histochemistry and Cell Biology 142:113–
                                      124. DOI: https://doi.org/10.1007/s00418-014-1213-2, PMID: 24696085
                                    Sustarsic M, Kapanidis AN. 2015. Taking the ruler to the jungle: single-molecule FRET for understanding
                                      biomolecular structure and dynamics in live cells. Current Opinion in Structural Biology 34:52–59. DOI: https://
                                      doi.org/10.1016/j.sbi.2015.07.001, PMID: 26295172
                                    Swoboda M, Grieb MS, Hahn S, Schlierf M. 2014. Measuring two at the same time: combining magnetic
                                      tweezers with single-molecule FRET. In: Toseland C. P, Fili N (Eds). Exs. Basel. Springer. p. 253–276.
                                      DOI: https://doi.org/10.1007/978-3-0348-0856-9_12
                                    Szalai AM, Siarry B, Lukin J, Giusti S, Unsain N, Cáceres A, Steiner F, Tinnefeld P, Refojo D, Jovin TM, Stefani FD.
                                      2021. Super-resolution imaging of energy transfer by Intensity-Based STED-FRET. Nano Letters 21:2296–2303.
                                      DOI: https://doi.org/10.1021/acs.nanolett.1c00158, PMID: 33621102
                                    Tagari M, Newman R, Chagoyen M, Carazo JM, Henrick K. 2002. New electron microscopy database and
                                      deposition system. Trends in Biochemical Sciences 27:589. DOI: https://doi.org/10.1016/S0968-0004(02)02176-
                                      X, PMID: 12417136
                                    Tang C, Gong Z. 2020. Integrating non-NMR distance restraints to augment NMR depiction of protein structure
                                      and dynamics. Journal of Molecular Biology 432:2913–2929. DOI: https://doi.org/10.1016/j.jmb.2020.01.023,
                                      PMID: 32044345
                                    Tardif C, Nadeau G, Labrecque S, Côté D, Lavoie-Cardinal F. 2019. Fluorescence lifetime imaging nanoscopy for
                                      measuring Förster resonance energy transfer in cellular nanodomains. Neurophotonics 6:1. DOI: https://doi.
                                      org/10.1117/1.NPh.6.1.015002
                                    Targowski P, Zie˛tek B, Ba˛czyński A. 1987. Luminescence quenching of rhodamines by cyclooctatetraene.
                                      Zeitschrift Für Naturforschung A 42:1009–1013. DOI: https://doi.org/10.1515/zna-1987-0914
                                    Tassis K, Vietrov R, de Koning M, de Boer M, Gouridis G, Cordes T. 2020. Single-molecule studies of
                                      conformational states and dynamics in the ABC importer OpuA. FEBS Letters 12:14026. DOI: https://doi.org/
                                      10.1002/1873-3468.14026
                                    Tellinghuisen J, Goodwin PM, Ambrose WP, Martin JC, Keller RA. 1994. Analysis of fluorescence lifetime data
                                      for single rhodamine molecules in flowing sample streams. Analytical Chemistry 66:64–72. DOI: https://doi.org/
                                      10.1021/ac00073a013
                                    Terry DS, Kolster RA, Quick M, LeVine MV, Khelashvili G, Zhou Z, Weinstein H, Javitch JA, Blanchard SC. 2018. A
                                      partially-open inward-facing intermediate conformation of LeuT is associated with Na+ release and substrate
                                      transport. Nature Communications 9:230. DOI: https://doi.org/10.1038/s41467-017-02202-y, PMID: 29335402
                                    Thomsen J, Sletfjerding MB, Jensen SB, Stella S, Paul B, Malle MG, Montoya G, Petersen TC, Hatzakis NS. 2020.
                                      DeepFRET, a software for rapid and automated single-molecule FRET data classification using deep learning.
                                      eLife 9:e60404. DOI: https://doi.org/10.7554/eLife.60404, PMID: 33138911
                                    Tisler J, Reuter R, Lämmle A, Jelezko F, Balasubramanian G, Hemmer PR, Reinhard F, Wrachtrup J. 2011. Highly
                                      efficient FRET from a single nitrogen-vacancy center in nanodiamonds to a single organic molecule. ACS Nano
                                      5:7893–7898. DOI: https://doi.org/10.1021/nn2021259, PMID: 21899301


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                   64 of 69



                                    Tomov TE, Tsukanov R, Masoud R, Liber M, Plavner N, Nir E. 2012. Disentangling subpopulations in single-
                                      molecule FRET and ALEX experiments with photon distribution analysis. Biophysical Journal 102:1163–1173.
                                      DOI: https://doi.org/10.1016/j.bpj.2011.11.4025, PMID: 22404939
                                    Torella JP, Holden SJ, Santoso Y, Hohlbein J, Kapanidis AN. 2011. Identifying molecular dynamics in single-
                                      molecule FRET experiments with burst variance analysis. Biophysical Journal 100:1568–1577. DOI: https://doi.
                                      org/10.1016/j.bpj.2011.01.066, PMID: 21402040
                                    Torres T, Levitus M. 2007. Measuring conformational dynamics: a new FCS-FRET approach. The Journal of
                                      Physical Chemistry B 111:7392–7400. DOI: https://doi.org/10.1021/jp070659s, PMID: 17547447
                                    Tosatto L, Horrocks MH, Dear AJ, Knowles TP, Dalla Serra M, Cremades N, Dobson CM, Klenerman D. 2015.
                                      Single-molecule FRET studies on alpha-synuclein oligomerization of Parkinson’s disease genetically related
                                      mutants. Scientific Reports 5:16696. DOI: https://doi.org/10.1038/srep16696, PMID: 26582456
                                    Traeger JC, Schwartz DK. 2017. Surface-mediated DNA hybridization: effects of DNA conformation, surface
                                      chemistry, and electrostatics. Langmuir 33:12651–12659. DOI: https://doi.org/10.1021/acs.langmuir.7b02675,
                                      PMID: 29023127
                                    Treutlein B, Muschielok A, Andrecka J, Jawhari A, Buchen C, Kostrewa D, Hög F, Cramer P, Michaelis J. 2012.
                                      Dynamic architecture of a minimal RNA polymerase II open promoter complex. Molecular Cell 46:136–146.
                                      DOI: https://doi.org/10.1016/j.molcel.2012.02.008, PMID: 22424775
                                    Tsytlonok M, Sanabria H, Wang Y, Felekyan S, Hemmen K, Phillips AH, Yun MK, Waddell MB, Park CG,
                                      Vaithiyalingam S, Iconaru L, White SW, Tompa P, Seidel CAM, Kriwacki R. 2019. Dynamic anticipation by Cdk2/
                                      Cyclin A-bound p27 mediates signal integration in cell cycle regulation. Nature Communications 10:1676.
                                      DOI: https://doi.org/10.1038/s41467-019-09446-w, PMID: 30976006
                                    Tsytlonok M, Hemmen K, Hamilton G, Kolimi N, Felekyan S, Seidel CAM, Tompa P, Sanabria H. 2020. Specific
                                      conformational dynamics and expansion underpin a multi-step mechanism for specific binding of p27 with
                                      Cdk2/Cyclin A. Journal of Molecular Biology 432:2998–3017. DOI: https://doi.org/10.1016/j.jmb.2020.02.010,
                                      PMID: 32088186
                                    Tyagi S, VanDelinder V, Banterle N, Fuertes G, Milles S, Agez M, Lemke EA. 2014. Continuous throughput and
                                      long-term observation of single-molecule FRET without immobilization. Nature Methods 11:297–300.
                                      DOI: https://doi.org/10.1038/nmeth.2809, PMID: 24441935
                                    Tyagi S, Lemke EA. 2015. Single-molecule FRET and crosslinking studies in structural biology enabled by
                                      noncanonical amino acids. Current Opinion in Structural Biology 32:66–73. DOI: https://doi.org/10.1016/j.sbi.
                                      2015.02.009, PMID: 25757192
                                    Ulrich EL, Akutsu H, Doreleijers JF, Harano Y, Ioannidis YE, Lin J, Livny M, Mading S, Maziuk D, Miller Z,
                                      Nakatani E, Schulte CF, Tolmie DE, Kent Wenger R, Yao H, Markley JL. 2008. BioMagResBank. Nucleic Acids
                                      Research 36:D402–D408. DOI: https://doi.org/10.1093/nar/gkm957, PMID: 17984079
                                    Ulrich EL, Baskaran K, Dashti H, Ioannidis YE, Livny M, Romero PR, Maziuk D, Wedell JR, Yao H, Eghbalnia HR,
                                      Hoch JC, Markley JL. 2019. NMR-STAR: comprehensive ontology for representing, archiving and exchanging
                                      data from nuclear magnetic resonance spectroscopic experiments. Journal of Biomolecular NMR 73:5–9.
                                      DOI: https://doi.org/10.1007/s10858-018-0220-3, PMID: 30580387
                                    Uphoff S, Holden SJ, Le Reste L, Periz J, van de Linde S, Heilemann M, Kapanidis AN. 2010. Monitoring multiple
                                      distances within a single molecule using switchable FRET. Nature Methods 7:831–836. DOI: https://doi.org/10.
                                      1038/nmeth.1502, PMID: 20818380
                                    Uphoff S, Gryte K, Evans G, Kapanidis AN. 2011. Improved temporal resolution and linked hidden markov
                                      modeling for switchable single-molecule FRET. ChemPhysChem 12:571–579. DOI: https://doi.org/10.1002/
                                      cphc.201000834, PMID: 21280168
                                    Vallat B, Webb B, Westbrook JD, Sali A, Berman HM. 2018. Development of a prototype system for archiving
                                      integrative/hybrid structure models of biological macromolecules. Structure 26:894–904. DOI: https://doi.org/
                                      10.1016/j.str.2018.03.011, PMID: 29657133
                                    Vallat B, Hanke CA, Lawson CL, Westbrook JD, Berman HM, Seidel CAM. 2020. mmCIF-based extension
                                      dictionary for structural models derived from Fluorescence / FRET experiments. GitHub. https://github.com/
                                      ihmwg/FLR-dictionary
                                    van de Meent JW, Bronson JE, Wiggins CH, Gonzalez RL. 2014. Empirical bayes methods enable advanced
                                      population-level analyses of single-molecule FRET experiments. Biophysical Journal 106:1327–1337.
                                      DOI: https://doi.org/10.1016/j.bpj.2013.12.055, PMID: 24655508
                                    van der Lee R, Buljan M, Lang B, Weatheritt RJ, Daughdrill GW, Dunker AK, Fuxreiter M, Gough J, Gsponer J,
                                      Jones DT, Kim PM, Kriwacki RW, Oldfield CJ, Pappu RV, Tompa P, Uversky VN, Wright PE, Babu MM. 2014.
                                      Classification of intrinsically disordered regions and proteins. Chemical Reviews 114:6589–6631. DOI: https://
                                      doi.org/10.1021/cr400525m, PMID: 24773235
                                    van der Meer BW. 2002. Kappa-squared: from nuisance to new sense. Reviews in Molecular Biotechnology 82:
                                      181–196. DOI: https://doi.org/10.1016/S1389-0352(01)00037-X
                                    van der Velde JH, Ploetz E, Hiermaier M, Oelerich J, de Vries JW, Roelfes G, Cordes T. 2013. Mechanism of
                                      intramolecular photostabilization in self-healing cyanine fluorophores. ChemPhysChem 14:4084–4093.
                                      DOI: https://doi.org/10.1002/cphc.201300785, PMID: 24302532
                                    van der Velde JHM, Oelerich J, Huang J, Smit JH, Aminian Jazi A, Galiani S, Kolmakov K, Gouridis G, Eggeling
                                      C, Herrmann A, Roelfes G, Cordes T. 2016. A simple and versatile design concept for fluorophore derivatives
                                      with intramolecular photostabilization. Nature Communications 7:10144. DOI: https://doi.org/10.1038/
                                      ncomms10144


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                               65 of 69



                                    Vandenberk N, Barth A, Borrenberghs D, Hofkens J, Hendrix J. 2018. Evaluation of Blue and Far-Red Dye Pairs
                                      in Single-Molecule Förster Resonance Energy Transfer Experiments. The Journal of Physical Chemistry B 122:
                                      4249–4266. DOI: https://doi.org/10.1021/acs.jpcb.8b00108
                                    Verkade P, Collinson L. 2019. Correlative Imaging. Wiley. DOI: https://doi.org/10.1002/9781119086420
                                    Viegas A, Dollinger P, Verma N, Kubiak J, Viennet T, Seidel CAM, Gohlke H, Etzkorn M, Kovacic F, Jaeger K-E.
                                      2020. Structural and dynamic insights revealing how lipase binding domain MD1 of Pseudomonas aeruginosa
                                      foldase affects lipase activation. Scientific Reports 10:3578. DOI: https://doi.org/10.1038/s41598-020-60093-4
                                    Voelz VA, Jäger M, Yao S, Chen Y, Zhu L, Waldauer SA, Bowman GR, Friedrichs M, Bakajin O, Lapidus LJ, Weiss
                                      S, Pande VS. 2012. Slow unfolded-state structuring in Acyl-CoA binding protein folding revealed by simulation
                                      and experiment. Journal of the American Chemical Society 134:12565–12577. DOI: https://doi.org/10.1021/
                                      ja302528z, PMID: 22747188
                                    Vogelsang J, Kasper R, Steinhauer C, Person B, Heilemann M, Sauer M, Tinnefeld P. 2008. A reducing and
                                      oxidizing system minimizes photobleaching and blinking of fluorescent dyes. Angewandte Chemie International
                                      Edition 47:5465–5469. DOI: https://doi.org/10.1002/anie.200801518, PMID: 18601270
                                    Voith von Voithenberg L, Sánchez-Rico C, Kang HS, Madl T, Zanier K, Barth A, Warner LR, Sattler M, Lamb DC.
                                      2016. Recognition of the 3’ splice site RNA by the U2AF heterodimer involves a dynamic population shift.
                                      PNAS 113:E7169–E7175. DOI: https://doi.org/10.1073/pnas.1605873113, PMID: 27799531
                                    Volkov IL, Lindén M, Aguirre Rivera J, Ieong KW, Metelev M, Elf J, Johansson M. 2018. tRNA tracking for direct
                                      measurements of protein synthesis kinetics in live cells. Nature Chemical Biology 14:618–626. DOI: https://doi.
                                      org/10.1038/s41589-018-0063-y, PMID: 29769736
                                    Vöpel T, Hengstenberg CS, Peulen TO, Ajaj Y, Seidel CA, Herrmann C, Klare JP. 2014. Triphosphate induced
                                      dimerization of human guanylate binding protein 1 involves association of the C-terminal helices: a joint double
                                      electron-electron resonance and FRET study. Biochemistry 53:4590–4600. DOI: https://doi.org/10.1021/
                                      bi500524u, PMID: 24991938
                                    Vušurović N, Altman RB, Terry DS, Micura R, Blanchard SC. 2017. Pseudoknot formation seeds the twister
                                      ribozyme cleavage reaction coordinate. Journal of the American Chemical Society 139:8186–8193.
                                      DOI: https://doi.org/10.1021/jacs.7b01549, PMID: 28598157
                                    Wahl M, Rahn H-J, Röhlicke T, Kell G, Nettels D, Hillger F, Schuler B, Erdmann R. 2008. Scalable time-correlated
                                      photon counting system with multiple independent input channels. Review of Scientific Instruments 79:123113.
                                      DOI: https://doi.org/10.1063/1.3055912
                                    Wang L, Pulk A, Wasserman MR, Feldman MB, Altman RB, Cate JHD, Blanchard SC. 2012. Allosteric control of
                                      the ribosome by small-molecule antibiotics. Nature Structural & Molecular Biology 19:957–963. DOI: https://
                                      doi.org/10.1038/nsmb.2360
                                    Wang Y, Liu Y, DeBerg HA, Nomura T, Hoffman MT, Rohde PR, Schulten K, Martinac B, Selvin PR. 2014. Single
                                      molecule FRET reveals pore size and opening mechanism of a mechano-sensitive ion channel. eLife 3:e01834.
                                      DOI: https://doi.org/10.7554/eLife.01834
                                    Wang S, Vafabakhsh R, Borschel WF, Ha T, Nichols CG. 2016. Structural dynamics of potassium-channel gating
                                      revealed by single-molecule FRET. Nature Structural & Molecular Biology 23:31–36. DOI: https://doi.org/10.
                                      1038/nsmb.3138
                                    Wang Y, Lu HP. 2010. Bunching effect in single-molecule T4 lysozyme nonequilibrium conformational dynamics
                                      under enzymatic reactions. The Journal of Physical Chemistry B 114:6669–6674. DOI: https://doi.org/10.1021/
                                      jp1004506, PMID: 20369804
                                    Wang W, Wang D. 2019. Extreme fuzziness: direct interactions between two IDPs. Biomolecules 9:81.
                                      DOI: https://doi.org/10.3390/biom9030081
                                    Wasserman MR, Alejo JL, Altman RB, Blanchard SC. 2016. Multiperspective smFRET reveals rate-determining
                                      late intermediates of ribosomal translocation. Nature Structural & Molecular Biology 23:333–341. DOI: https://
                                      doi.org/10.1038/nsmb.3177
                                    Watrob HM, Pan C-P, Barkley MD. 2003. Two-Step FRET as a Structural Tool. Journal of the American Chemical
                                      Society 125:7336–7343. DOI: https://doi.org/10.1021/ja034564p
                                    Webb B, Viswanath S, Bonomi M, Pellarin R, Greenberg CH, Saltzberg D, Sali A. 2018. Integrative structure
                                      modeling with the integrative modeling platform. Protein Science 27:245–258. DOI: https://doi.org/10.1002/
                                      pro.3311, PMID: 28960548
                                    Weidtkamp-Peters S, Felekyan S, Bleckmann A, Simon R, Becker W, Kühnemuth R, Seidel CA. 2009.
                                      Multiparameter fluorescence image spectroscopy to study molecular interactions. Photochemical &
                                      Photobiological Sciences 8:470–480. DOI: https://doi.org/10.1039/b903245m, PMID: 19337660
                                    Weiss S. 1999. Fluorescence spectroscopy of single biomolecules. Science 283:1676–1683. DOI: https://doi.org/
                                      10.1126/science.283.5408.1676, PMID: 10073925
                                    White SS, Li H, Marsh RJ, Piper JD, Leonczek ND, Nicolaou N, Bain AJ, Ying L, Klenerman D. 2006.
                                      Characterization of a single molecule DNA switch in free solution. Journal of the American Chemical Society
                                      128:11423–11432. DOI: https://doi.org/10.1021/ja0614870, PMID: 16939265
                                    Whitford PC, Geggier P, Altman RB, Blanchard SC, Onuchic JN, Sanbonmatsu KY. 2010. Accommodation of
                                      aminoacyl-tRNA into the ribosome involves reversible excursions along multiple pathways. RNA 16:1196–1204.
                                      DOI: https://doi.org/10.1261/rna.2035410
                                    Widengren J, Schweinberger E, Berger S, Seidel CAM. 2001. Two new concepts to measure fluorescence
                                      resonance energy transfer via fluorescence correlation spectroscopy: Theory and Experimental Realizations. The
                                      Journal of Physical Chemistry A 105:6851–6866. DOI: https://doi.org/10.1021/jp010301a


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                66 of 69



                                    Widengren J, Kudryavtsev V, Antonik M, Berger S, Gerken M, Seidel CAM. 2006. Single-molecule detection and
                                      identification of multiple species by multiparameter fluorescence detection. Analytical Chemistry 78:2039–
                                      2050. DOI: https://doi.org/10.1021/ac0522759, PMID: 16536444
                                    Widengren J, Chmyrov A, Eggeling C, Löfdahl PA, Seidel CA. 2007. Strategies to improve photostabilities in
                                      ultrasensitive fluorescence spectroscopy. The Journal of Physical Chemistry A 111:429–440. DOI: https://doi.
                                      org/10.1021/jp0646325, PMID: 17228891
                                    Wilkinson MD, Dumontier M, Aalbersberg IJ, Appleton G, Axton M, Baak A, Blomberg N, Boiten JW, da Silva
                                      Santos LB, Bourne PE, Bouwman J, Brookes AJ, Clark T, Crosas M, Dillo I, Dumon O, Edmunds S, Evelo CT,
                                      Finkers R, Gonzalez-Beltran A, et al. 2016. The FAIR guiding principles for scientific data management and
                                      stewardship. Scientific Data 3:160018. DOI: https://doi.org/10.1038/sdata.2016.18, PMID: 26978244
                                    Wilson H, Wang Q. 2019. ABEL-FRET: tether-free single-molecule FRET with hydrodynamic profiling. bioRxiv.
                                      DOI: https://doi.org/10.1101/786897
                                    Wozniak AK, Schröder GF, Grubmüller H, Seidel CAM, Oesterhelt F. 2008. Single-molecule FRET measures
                                      bends and kinks in DNA. PNAS 105:18337–18342. DOI: https://doi.org/10.1073/pnas.0800977105, PMID: 1
                                      9020079
                                    Wranne MS, Füchtbauer AF, Dumat B, Bood M, El-Sagheer AH, Brown T, Gradén H, Grøtli M, Wilhelmsson LM.
                                      2017. Toward complete sequence flexibility of nucleic acid base analogue FRET. Journal of the American
                                      Chemical Society 139:9271–9280. DOI: https://doi.org/10.1021/jacs.7b04517, PMID: 28613885
                                    Wright PE, Dyson HJ. 2015. Intrinsically disordered proteins in cellular signalling and regulation. Nature Reviews
                                      Molecular Cell Biology 16:18–29. DOI: https://doi.org/10.1038/nrm3920
                                    Wu S, Wang D, Liu J, Feng Y, Weng J, Li Y, Gao X, Liu J, Wang W. 2017. The dynamic multisite interactions
                                      between two intrinsically disordered proteins. Angewandte Chemie International Edition 56:7515–7519.
                                      DOI: https://doi.org/10.1002/anie.201701883, PMID: 28493424
                                    Wunderlich B, Nettels D, Benke S, Clark J, Weidner S, Hofmann H, Pfeil SH, Schuler B. 2013. Microfluidic mixer
                                      designed for performing single-molecule kinetics with confocal detection on timescales from milliseconds to
                                      minutes. Nature Protocols 8:1459–1474. DOI: https://doi.org/10.1038/nprot.2013.082
                                    Yanez Orozco IS, Mindlin FA, Ma J, Wang B, Levesque B, Spencer M, Rezaei Adariani S, Hamilton G, Ding F,
                                      Bowen ME, Sanabria H. 2018. Identifying weak interdomain interactions that stabilize the supertertiary
                                      structure of the N-terminal tandem PDZ domains of PSD-95. Nature Communications 9:3724. DOI: https://doi.
                                      org/10.1038/s41467-018-06133-0
                                    Yim SW, Kim T, Laurence TA, Partono S, Kim D, Kim Y, Weiss S, Reitmair A. 2012. Four-Color Alternating-Laser
                                      excitation Single-Molecule fluorescence spectroscopy for Next-Generation biodetection assays. Clinical
                                      Chemistry 58:707–716. DOI: https://doi.org/10.1373/clinchem.2011.176958
                                    Yoo J, Louis JM, Gopich IV, Chung HS. 2018. Three-color single-molecule FRET and fluorescence lifetime analysis
                                      of fast protein folding. The Journal of Physical Chemistry B 122:11702–11720. DOI: https://doi.org/10.1021/
                                      acs.jpcb.8b07768
                                    Yoo J, Kim J-Y, Louis JM, Gopich IV, Chung HS. 2020. Fast three-color single-molecule FRET using statistical
                                      inference. Nature Communications 11:3336. DOI: https://doi.org/10.1038/s41467-020-17149-w
                                    Young J, Westbrook J. 2019. Creating and maintaining a data archive for 3D structures of biological
                                      macromolecules. F1000Research 8:1111762. DOI: https://doi.org/10.7490/f1000research.1111762.1
                                    Zarrabi N, Schluesche P, Meisterernst M, Börsch M, Lamb DC. 2018. Analyzing the dynamics of single TBP-DNA-
                                      NC2 complexes using hidden Markov models. Biophysical Journal 115:2310–2326. DOI: https://doi.org/10.
                                      1016/j.bpj.2018.11.015, PMID: 30527334
                                    Zelger-Paulus S, Hadzic M, Sigel RKO, Börner R. 2020. Encapsulation of fluorescently labeled RNAs into surface-
                                      tethered vesicles for single-molecule FRET studies in TIRF microscopy. In: Arluison V, Wien F (Eds). Methods in
                                      Molecular Biology. Springer. p. 1–16. DOI: https://doi.org/10.1007/978-1-0716-0278-2_1
                                    Zhao R, Marshall M, Alemán EA, Lamichhane R, Feig A, Rueda D. 2010a. Laser-assisted single-molecule refolding
                                      (LASR). Biophysical Journal 99:1925–1931. DOI: https://doi.org/10.1016/j.bpj.2010.07.019, PMID: 20858438
                                    Zhao Y, Terry D, Shi L, Weinstein H, Blanchard SC, Javitch JA. 2010b. Single-molecule dynamics of gating in a
                                      neurotransmitter transporter homologue. Nature 465:188–193. DOI: https://doi.org/10.1038/nature09057
                                    Zhao M, Steffen FD, Börner R, Schaffer MF, Sigel RKO, Freisinger E. 2018. Site-specific dual-color labeling of
                                      long RNAs for single-molecule spectroscopy. Nucleic Acids Research 46:e13. DOI: https://doi.org/10.1093/nar/
                                      gkx1100
                                    Zheng Q, Juette MF, Jockusch S, Wasserman MR, Zhou Z, Altman RB, Blanchard SC. 2014. Ultra-stable organic
                                      fluorophores for single-molecule research. Chem. Soc. Rev. 43:1044–1056. DOI: https://doi.org/10.1039/
                                      C3CS60237K
                                    Zhuang X, Bartley LE, Babcock HP, Russell R, Ha T, Herschlag D, Chu S. 2000. A single-molecule study of RNA
                                      catalysis and folding. Science 288:2048–2051. DOI: https://doi.org/10.1126/science.288.5473.2048, PMID: 10
                                      856219
                                    Zijlstra N, Dingfelder F, Wunderlich B, Zosel F, Benke S, Nettels D, Schuler B. 2017. Rapid microfluidic dilution
                                      for Single-Molecule spectroscopy of Low-Affinity biomolecular complexes. Angewandte Chemie International
                                      Edition 56:7126–7129. DOI: https://doi.org/10.1002/anie.201702439, PMID: 28510311
                                    Zosel F, Mercadante D, Nettels D, Schuler B. 2018. A proline switch explains kinetic heterogeneity in a coupled
                                      folding and binding reaction. Nature Communications 9:3332. DOI: https://doi.org/10.1038/s41467-018-05725-
                                    Zosel F, Holla A, Schuler B. 2020a. Labeling of proteins for single-molecule fluorescence spectroscopy.
                                      ChemRxiv. DOI: https://doi.org/10.26434/chemrxiv.11537913


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                                67 of 69



                                    Zosel F, Soranno A, Buholzer KJ, Nettels D, Schuler B. 2020b. Depletion interactions modulate the binding
                                     between disordered proteins in crowded environments. PNAS 117:13480–13489. DOI: https://doi.org/10.
                                     1073/pnas.1921617117


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                             68 of 69



                                    Appendix 1
                                    Simulation software

                                       .   simFCS (https://www.lfd.uci.edu/globals/) was developed for simulating various modalities in
                                           fluorescence, beginning with FCS. Using two channels, the simulation of burst analysis smFRET
                                           data can be performed. The concentration, diffusion coefficient and molecular brightness in
                                           different channels and dynamics between them can be adjusted.
                                       .   PyBroMo (https://github.com/tritemio/PyBroMo) is a Python-based software package for simu-
                                           lating free-diffusion single-molecule fluorescence detection, including differences in transla-
                                           tional diffusion coefficients, in concentrations, or in dye brightnesses and exchange dynamics
                                           between conformational states (currently between two states). This approach has been
                                           employed in a few recent works (Ingargiola et al., 2017; Lerner et al., 2018b; Hagai and
                                           Lerner, 2019).
                                       .   PAM software package (https://www.cup.uni-muenchen.de/pc/lamb/software/pam.html). The
                                           PAM software package is a MATLAB-based software that can simulate smFRET experiments of
                                           freely diffusing or immobilized molecules, including fluorescence lifetime and anisotropy as
                                           well as exchange dynamics between multiple conformational states (up to 8) Szalai et al.,
                                           2021 Schrimpf et al., 2018).
                                       .   The Burbulator software within the MFD program package, programed in LabVIEW
                                           (Dimura et al., 2016; Felekyan et al., 2012; Kalinin et al., 2010b) (https://www.mpc.hhu.de/
                                           software/3-software-package-for-mfd-fcs-and-mfis), can simulate smFRET experiments (with
                                           and without diffusion) combined fluorescence lifetime and anisotropy as well as exchange
                                           dynamics between multiple conformational states (up to 8). These tools have been applied to
                                           benchmark novel quantitative analysis methods to obtain structural and kinetic information.
                                       .   Fretica (https://schuler.bioc.uzh.ch/programs/) enables the simulation of single-molecule multi-
                                           channel-detection of immobilized molecules and mixtures of freely diffusing species, including
                                           a dynamic exchange between an arbitrary number of conformational states (König et al.,
                                           2015; Zosel et al., 2018).
                                       .   The MATLAB -based MASH-FRET software package (Börner et al., 2018) (https://rna-fretools.
                                           github.io/MASH-FRET/) has been applied to evaluate transition detection and state identifica-
                                           tion algorithms used in particular for time-binned smFRET trajectories (Hadzic et al., 2018) as
                                           well as for spot detection in single-molecule videos (SMV).
                                       .   The python-based software DeepFRET (Thomsen et al., 2020) comes with a trace simulator
                                           capable of simulating traces with 17 adjustable features that include the number of FRET
                                           states, their values, noise level, transition probability and more (https://github.com/hatzaki-
                                           slab/DeepFRET-GUI).


Lerner, Barth, Hendrix, et al. eLife 2021;10:e60416. DOI: https://doi.org/10.7554/eLife.60416                                            69 of 69
