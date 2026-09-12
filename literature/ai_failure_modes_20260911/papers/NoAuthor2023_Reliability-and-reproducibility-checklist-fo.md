# Reliability and reproducibility checklist for molecular dynamics simulations

**Authors:** (no author listed; journal Editorial)
**Year:** 2023
**Venue:** Communications Biology
**DOI:** 10.1038/s42003-023-04653-0
**Source PDF URL:** https://www.nature.com/articles/s42003-023-04653-0.pdf
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

EDITORIAL
                  https://doi.org/10.1038/s42003-023-04653-0               OPEN

                  Reliability and reproducibility checklist for
                  molecular dynamics simulations
                  We present a checklist to improve the reliability and reproducibility of molecular dynamics simulations
                  and related methods.


                                                                      M
                                                                                       olecular dynamics (MD)             simulation, the corresponding quantitative
                                                                                       simulations and related            analysis also needs to be presented to show
                                                                                       methods involving mole-            that    the     snapshots     are    indeed
                                                                                       cular docking, enhanced            representative.
                                                                                       sampling, coarse-graining,
                                                                      and quantum mechanical calculations are
                                                                                                                          Connection to experiments
                                                                      widely used to provide mechanistic insight
                                                                                                                          Communications Biology welcomes high-

1234567890():,;
                                                                      into biological, chemical, and physical
                                                                                                                          quality computational work that generates
                                                                      phenomena at the atomistic or molecular
                                                                                                                          new biological insights and testable
                                                                      level. The insights are valuable provided
                                                                                                                          hypotheses. New experimental validation is
                                                                      that appropriate convergence and relia-
                                                                                                                          highly encouraged but not required for
                                                                      bility checks are done when analyzing the
                                                                                                                          publication. When new experimental vali-
                                                                      simulations. To maximize the value to the
                                                                                                                          dation is not provided, the physiological
                                                                      research community, sufﬁcient informa-
                                                                                                                          relevance of MD simulation results should
                                                                      tion is required to allow reproduction or
                                                                                                                          be discussed in connection with published
                                                                      extension of the simulations for other
                                                                                                                          experimental data. It’s important to note
                                                                      applications.
                                                                                                                          that these criteria are in line with our
                                                                         Here, we present a checklist for report-
                                                                                                                          current expectations for computational
                                                                      ing and assessing simulation data and data
                                                                                                                          work but may change as the journal
                                                                      reproducibility (Table 1). It is our hope
                                                                                                                          matures.
                                                                      that this checklist, although far from
                                                                      extensive and subject to potential reﬁne-
                                                                      ment in future, will serve as a clear               Method choice
                                                                      guideline for publishing high quality               Method choice in MD simulations com-
                                                                      computational work in Communications                prises two factors: model accuracy and
                                                                      Biology. The guidelines in each section of          sampling technique. With rapid growing
                                                                      the checklist include:                              computing capacity and algorithmic
                                                                                                                          advances, we are now witnessing MD stu-
                                                                                                                          dies of increasingly large and complex
                                           “It is our hope that this              Convergence of                          biomolecular systems, such as those
                                                                                  simulations and                         involving membrane proteins, intrinsically
                                           checklist, although far from           analysis                                disordered proteins, glycans, and nucleic
                                           extensive and subject to               Without convergence                     acids, at longer timescales. A simpliﬁed
                                                                                  analysis,      simulation               model that has been sampled well is more
                                           potential reﬁnement in future,         results are compro-                     valuable than a large, complex model with
                                                                                  mised. While it may                     poor convergence and statistics (see
                                           will serve as a clear guideline        not be possible to prove                “Convergence of simulations and analy-
                                                                                  “absolute convergence”,                 sis”). As the best choice always depends on
                                           for publishing high quality
                                                                                  multiple independent                    the system of interest, the authors need to
                                           computational work in                  simulations       starting              justify that the chosen model, resolution,
                                                                                  from different conﬁg-                   and force ﬁeld are accurate enough to
                                           Communications Biology.”               urations and time-                      answer the speciﬁc question.
                                                                                  course analyses can                        With respect to sampling methods, the
                                                                                  detect the lack of con-                 functional relevant states of biomolecules
                                                               vergence. At least three independent                       are often separated by rugged free energy
                                                               simulations with statistical analysis should               landscapes. Convergence analysis of the
                                                               be performed to show that the properties                   unbiased trajectories mentioned above may
                                                               being measured have converged. When                        not detect slow transitions between kine-
                                                               presenting representative snapshots of a                   tically trapped metastable states. Therefore,

                  COMMUNICATIONS BIOLOGY | (2023)6:268 | https://doi.org/10.1038/s42003-023-04653-0 | www.nature.com/commsbio                                        1


EDITORIAL                                                               COMMUNICATIONS BIOLOGY | https://doi.org/10.1038/s42003-023-04653-0


 Table 1 Reliability and reproducibility checklist for molecular dynamics simulations.

 1. Convergence of simulations and analysis
 1a. Is an evaluation presented in the text to show that the property being measured has equilibrated in the simulations (e.g., time-course analysis)?
 1b. Then, is it described in the text how simulations are split into equilibration and production runs and how much data were analyzed from
     production runs?
 1c. Are there at least 3 simulations per simulation condition with statistical analysis?
 1d. Is evidence provided in the text that the simulation results presented are independent of initial conﬁguration?
 2. Connection to experiments
 2a. Are calculations provided that can connect to experiments (e.g., loss or gain in function from mutagenesis, binding assays, NMR chemical shifts, J-
      couplings, SAXS curves, interaction distances or FRET distances, structure factors, diffusion coefﬁcients, bulk modulus and other mechanical
      properties, etc.)?
 3. Method choice
 3a. Do simulations contain membranes, membrane proteins, intrinsically disordered proteins, glycans, nucleic acids, polymers, or cryptic ligand binding?
 3b. Is it described in the text whether the accuracy of the chosen model(s) is sufﬁcient to address the question(s) under investigation (e.g., all-atom vs.
      coarse-grained models, ﬁxed charge vs. polarizable force ﬁelds, implicit vs. explicit solvent or membrane, speciﬁc force ﬁeld and water model, etc.?
 3c. Is the timescale of the event(s) under investigation beyond the brute-force MD simulation timescale in this study that enhanced sampling methods
     are needed?
        If YES, are the parameters and convergence criteria for the enhanced sampling method clearly stated?
        If NO, is the evidence provided in the text?
 4. Code and reproducibility
 4a. Is a table provided describing the system setup that includes simulation box dimensions, total number of atoms, number of water molecules, salt
      concentration, lipid composition (number of molecules and type)?
 4b. Are other parameters for the system setup described in the text, such as protonation state, type of structural restraints if applied, nonbonded cutoff,
      thermostat and barostat, etc.?
 4c. Is it described in the text what simulation and analysis software and which versions are used?
 4d. Are initial coordinate and simulation input ﬁles and a coordinate ﬁle of the ﬁnal output provided as supplementary ﬁles or in a public repository?
 4e. Is there custom code or custom force ﬁeld parameters?
        If YES, are they provided as supplementary ﬁles or in a public repository?


if the timescale of the event of interest is         with editorial policies and reporting
beyond unbiased sampling, the choice of              standards in the Nature Portfolio.
enhanced sampling method(s) and the                     For manuscripts containing MD simu-
convergence of the enhanced sampling                 lations or related methods, Communica-
need to be provided.                                 tions Biology will require authors to submit
                                                     their responses to the checklist for evalua-                          Open Access This article is licensed
                                                                                                                           under a Creative Commons Attribution
                                                     tion by the editors and reviewers, and to
                                                                                                          4.0 International License, which permits use, sharing,
Code and reproducibility                             update the checklist when going through              adaptation, distribution and reproduction in any medium
At minimum, details on simulation para-              revisions.                                           or format, as long as you give appropriate credit to the
meters need to be provided in the Methods               We hope that the guidelines and                   original author(s) and the source, provide a link to the
section, as well as simulation input ﬁles            checklist presented here will be helpful to          Creative Commons license, and indicate if changes were
and ﬁnal coordinate ﬁles. These can be               authors, referees and, ultimately, readers of        made. The images or other third party material in this
provided in the Supplementary ﬁles or                work involving molecular simulations. We             article are included in the article’s Creative Commons
                                                                                                          license, unless indicated otherwise in a credit line to the
deposited in a suitable public repository,           welcome feedback—please get in touch by              material. If material is not included in the article’s Creative
and should be sufﬁciently detailed to                emailing commsbio@nature.com.                        Commons license and your intended use is not permitted
enable others to reproduce or extend the                We are grateful to our Editorial Board            by statutory regulation or exceeds the permitted use, you
simulations.                                         Member Yun Lyna Luo, Western Uni-                    will need to obtain permission directly from the copyright
   Custom code and parameters that are               versity of Health Sciences, Pomona, Cali-            holder. To view a copy of this license, visit http://
                                                                                                          creativecommons.org/licenses/by/4.0/.
central to the manuscript must also be               fornia, for her assistance in developing
made available for review and publicly               these guidelines and contributing to the
accessible upon publication in compliance            writing of this Editorial.                           © Springer Nature Limited 2023


2                           COMMUNICATIONS BIOLOGY | (2023)6:268 | https://doi.org/10.1038/s42003-023-04653-0 | www.nature.com/commsbio
