# The need to implement FAIR principles in biomolecular simulations

**Authors:** Rommie E. Amaro, Johan Åqvist, Ivet Bahar, et al. (community statement, ~150 co-authors)
**Year:** 2025
**Venue:** Nature Methods
**DOI:** 10.1038/s41592-025-02635-0
**Source PDF URL:** https://europepmc.org/articles/PMC12950262?pdf=render (Europe PMC author manuscript, PMC12950262; green OA)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

HHS Public Access
Author manuscript

Published in final edited form as:
Nat Methods. 2025 April ; 22(4): 641–645. doi:10.1038/s41592-025-02635-0.

The need to implement FAIR principles in biomolecular
simulations
A full list of authors and affiliations appears at the end of the article.

Abstract

In the Big Data era, a change of paradigm in the use of molecular dynamics is required.
Trajectories should be stored under FAIR (findable, accessible, interoperable and reusable)
requirements to favor its reuse by the community under an open science paradigm.

The communities that embraced data archiving efforts decades ago are now, in the era
of data-driven biology, gaining the most from the AI revolution. The structural biology
community was a pioneer in this regard, establishing the Protein Data Bank in 1971 and
making data accessible using the FAIR principles even before these were articulated1,2.
The genomics and bioinformatics community has followed the example, establishing many
widely used databases3,4. By contrast, molecular simulation has been anchored in usage
paradigms dating back to the seventies, when molecular dynamics (MD) simulation was first
applied to study biomacromolecules5. At that time, MD was used by theoretical physicists
and chemists in proof-of-concept simulations, but 50 years later, MD has evolved into a
cornerstone molecular biology technique that can provide accurate, quantitative analysis and
property prediction. MD is now employed by tens of thousands of researchers worldwide,
accounting for roughly 15% of global supercomputer usage. Unfortunately, these rich and
costly data are not systematically maintained, and when further analyses are required,
simulations have to be rerun — an unacceptable situation from scientific, environmental and
sustainability standpoints. In this letter, we argue for a collaborative endeavor to archive MD
simulation data and describe ongoing efforts to establish cost-effective and sustainable data
archiving strategies.

Advances in computer technology have made it possible to simulate large, realistic
biological systems beyond the millisecond time-scale, and we are seeing simulations in
the 109-particle range, covering entire organelles and even minimal cells, resulting in
a “deluge of data”6 in a field that lacks agreed strategies for data storage. As in the
seventies, trajectories obtained after a huge effort are often ignored (or even deleted) after a
hypothesis-driven analysis is presented in a scientific publication. For a field entirely based
on sampling, and where the recipe for observations can be described exactly and critically

✉
adam.hospital@irbbarcelona.org; modesto.orozco@irbbarcelona.org.
Author contributions
M.O. conceived the idea. M.O., A.H. and E.L. wrote the draft of the paper, which was corrected first by other members of the MDDB
project (S.V., P.C.B., J.L.G., J.I.-F., A.C.) and later by all the authors.

Competing interests
The authors declare no competing interests.

assessed, this is a huge problem. Instead of being able to reanalyze, reuse, and potentially
spot undetected artifacts or new features in data, readers are often expected to blindly trust
the closed set of statements made by the authors in a paper. The lack of a systematic
approach to storing data (and associated provenance and metadata) prevents new studies
based on previous trajectories; impedes meta-analyses, extension of trajectories, training
of machine learning approaches, optimization of force fields and simulation protocols,
generation of new conformations for modeling of reactivity; hampers the use of trajectories
to train coarse-grained and mesoscopic models or generative models; and prohibits the
integration of MD results into the rich ecosystem of biology databases. Some journals
and funding institutions now require the deposition of trajectories. Without a centralized
reference repository, this has led to the use of existing generic repositories (for example,
Zenodo, Figshare) and the creation of numerous small, independent databases. As a result,
we may face vast amounts of dispersed and disconnected data, which are expensive to
maintain and often useless for further analysis. It is clear that the community needs to escape
from a paradigm that made sense in the seventies but now hinders progress, and move to an
open science model.

Establishing an archive for biosimulation data — upon quality assessment — would address
these issues, democratize the field, and have a material impact of MD simulations on
life science research. The traditional view held by the simulation community that storing
and archiving is more expensive than recomputing, which might have been correct in the
past, is no longer valid, as demonstrated by the massive Folding@home study on the
SARS-CoV-2 main protease7, or for simulations with many millions of atoms8. However,
the new science that can be learned from stored trajectories is more important than the
cost. For instance, the ABC Consortium9 was established in 2004 as a community effort
generating a multi-gigabyte database of DNA simulations, which had grown to hold 15
terabytes of data by 2019. The original goal of ABC was to study DNA polymorphisms,
but the database has become crucial in other fields, such as force field refinement, the
study of signal transfer in DNA and the development of coarse-grained models. The current
HexABC database contains 400 terabytes of data generated by 14 different groups to explore
hexamer dependencies of DNA dynamics. However, its future use, which is difficult to
anticipate, might be more important than the current goals of the project. Another example
emerged during the COVID-19 pandemic10,11, when the Molecular Sciences Software
Institute (MolSSI), in collaboration with European groups including BioExcel, European
Open Science Cloud, European Bioinformatics Institute and Zenodo, created the COVID-19
Molecular Structure and Therapeutics Hub (https://covid.molssi.org). It went live in April
2020, connecting scientists across the global biomolecular simulation community, as well
as improving the connection between simulation and experimental and clinical data and
their investigators. A further example is MDverse (https://mdverse.github.io/), an effort to
make MD trajectories FAIRer by indexing and curating thousands of simulations scattered
across the internet. Many other examples are now under development, highlighting the
general belief of the community that the traditional paradigm from the seventies should
be abandoned and all well-annotated, validated trajectories should be stored and integrated
in a general data infrastructure to favor the advance of science and the optimization of
computational resources.

The challenges that lie ahead for the community are diverse. The technical ones —sustained
data storage capacity, bandwidth, and processing capacity for analysis — can be alleviated
by a distributed database policy following initiatives such as the EGA infrastructure
(European Genome-Phenome Archive; https://ega-archive.org/) and by the commitment of
funding institutions and high-performance computing centers, offering storage, bandwidth
and processing capabilities. Other key decisions such as quality requirements for storing
and maintaining the data, the sparsity of the trajectory, the compression strategy, or whether
stored trajectory should be dry or contain also solvent molecules should be taken by the
community, keeping in mind that, while storing all the potential information derived by
an MD simulation might be impossible, preserving as much data as possible should be a
priority.

A centralized management entity should coordinate the federated nodes, defining required
metadata (crucial for reproducibility, extension of trajectories, increase of the time density
of snapshots, or meta-analysis), setting deposition policies, guaranteeing compliance of
FAIR rules and providing a common entry point through web-based and programmatic
representational state transfer (REST) API interfaces. The myriads of variants of MD
programs, protocols, formats and simulation conditions lead to more complex problems.
Recent MD repositories and databases11 are already prepared to manage not only plain
MD trajectories but also Markov state models, ensembles, multiscale simulations (hybrid
or combined approaches involving mesoscale, coarse-grained and atomistic methods, as
well as quantum mechanics with molecular mechanics), constant pH, replica exchange, and
MD trajectories biased with metadynamics or similar methods. NoSQL databases such as
MongoDB (with the GridFS file storage and retrieving specification) allow efficient storing
and querying of the diversity of outputs provided by MD engines and are already adopted
by MD storage initiatives. However, much more work is required for an effective analysis
framework that can manage an increasingly large number of MD variants and trajectory
formats.

Data should be findable, with each entry registered with a persistent identifier, ideally
a DOI, ensuring a proper citation, following the example of the WorkflowHub registry
(https://workflowhub.eu/). Furthermore, they should be stored in an interoperable manner,
so that they can be read and exploited by current and future data scraping and machine
learning algorithms. To this end, the community must reach an agreement to standardize
MD data exchange formats with (i) efficient trajectory compression, including simple
system specifications (for example, atom or residue names and connectivity); (ii) key-value
trees storing high-level and full simulation settings metadata; and (iii) metadata-based
ontology12, which would allow the user to search databases on the basis of the contents,
the nature or even the purpose of the simulations. Standardized provenance should be
stored by means of data blocks specifying commands or operations used to generate the
trajectory, together with names, stored hash sums of the complete files used for input,
and specific software used (with precise versions). This would allow the user to reproduce
all the different steps followed to prepare and run the simulation, including modeling of
missing residues, physical conditions (for example, pH, salt concentration, temperature and
pressure) and force fields, methodology used to obtain parameters involving non-standard
molecules (for example, small molecules, membrane systems, ionic coordination), and the

equilibration and possibly sampling process. Minimum metadata should include system
information, simulation parameters, author(s), data license and copyright, and, importantly,
the main purpose of the simulation. The definition of standardized protocols (that is, list of
operations) for production run and analysis, including a troubleshooting section, could be
added. These, along with a set of metadata-dependent quality control analyses, both general
and system specific, are crucial requisites for gaining trust from the community and for
defining deposition rules. A data repository following FAIR principles and the associated
analysis tools will increase the impact and the reproducibility (complex at the binary level;
that is, it is difficult to reproduce exactly the same trajectory owing to numerical errors)
of MD in related fields in the life science data ecosystem, from genomics to structural
biology and from protein and drug design to molecular biology. MD data would provide
unique dynamic information of biological macromolecules fully complementary with the
rich information available from the Protein Data Bank. This could be integrated into the life
science ecosystem following the approach of the Protein Data Bank in Europe Knowledge
Base, designed for the integration and enrichment of 3D structure data and functional
annotations13. All this information will contribute to knowledge democratization, helping
research teams with limited resources and fueling further advances in artificial intelligence
(AI) in the scientific domain14 (Fig. 1).

The MDDB project (https://mddbr.eu/) and similar initiatives aim to establish such a
repository, allowing (i) data quality assessment metrics to increase the trust of the
community in the deposited data; (ii) common data format, metadata requirements and
ontologies to facilitate interoperability; (iii) a minimum set of information needed to store
and reproduce the simulations, including data provenance, license and copyright; and (iv) a
standard and robust infrastructure to store and share the data, with persistent identifiers and
different ways to access them. We believe science will be better served by fully embracing
this data-driven view of biomolecular simulation. Furthermore, data-driven initiatives such
that supported by this Correspondence would help the interaction with other simulation
communities, such as the materials science one, which share some of the problems the
biomolecular simulation community is facing.

Authors

Rommie E. Amaro1, Johan Åqvist2, Ivet Bahar3,4, Federica Battistini5, Adam
Bellaiche6, Daniel Beltran7, Philip C. Biggin8, Massimiliano Bonomi9, Gregory
R. Bowman10, Richard A. Bryce11, Giovanni Bussi12, Paolo Carloni13,14,
David A. Case15, Andrea Cavalli16,17, Chia-En A. Chang18, Thomas E.
Cheatham III19, Margaret S. Cheung20,21, Christophe Chipot22,23,24, Lillian
T. Chong25, Preeti Choudhary6, G. Andres Cisneros26,27, Cecilia Clementi28,
Rosana Collepardo-Guevara29,30,31, Peter Coveney32,33, Roberto Covino34,35,
T. Daniel Crawford36,37, Matteo Dal Peraro38, Bert L. de Groot39, Lucie
Delemotte40, Marco De Vivo41, Jonathan W. Essex42, Franca Fraternali43,
Jiali Gao44, Josep Ll. Gelpí5,45, Francesco L. Gervasio46,47,48,49, Fernando
D. González-Nilo50, Helmut Grubmüller51, Marina G. Guenza52, Horacio V.
Guzman53, Sarah Harris54, Teresa Head-Gordon55, Rigoberto Hernandez56, Adam
Hospital7,57,✉, Niu Huang58, Xuhui Huang59, Gerhard Hummer60,61, Javier Iglesias-

Fernández62, Jan H. Jensen63, Shantenu Jha64, Wanting Jiao65, William L.
Jorgensen66, Shina C. L. Kamerlin67,68, Syma Khalid8, Charles Laughton69,
Michael Levitt70, Vittorio Limongelli71, Erik Lindahl40,72, Kresten Lindorff-Larsen73,
Sharon Loverde74, Magnus Lundborg40, Yun L. Luo75, F. Javier Luque76,77,
Charlotte I. Lynch8, Alexander D. MacKerell Jr78, Alessandra Magistrato79,
Siewert J. Marrink80, Hugh Martin32, J. Andrew McCammon81,82, Kenneth
Merz83,84, Vicent Moliner85, Adrian J. Mulholland86, Sohail Murad87, Athi N.
Naganathan88, Shikha Nangia89, Frank Noe90,91,92,93, Agnes Noy94, Julianna
Oláh95, Megan L. O’Mara96, Mary Jo Ondrechen97, Jose N. Onuchic92,98,99,100,
Alexey Onufriev101,102,103, Sílvia Osuna104,105, Giulia Palermo18,106, Anna R.
Panchenko107,108,109, Sergio Pantano110,111, Carol Parish112, Michele Parrinello113,
Alberto Perez114, Tomas Perez-Acle115,116, Juan R. Perilla117, B. Montgomery
Pettitt118, Adriana Pietropaolo119, Jean-Philip Piquemal120, Adolfo B. Poma121,
Matej Praprotnik122,123, Maria J. Ramos124, Pengyu Ren125, Nathalie Reuter126,127,
Adrian Roitberg114, Edina Rosta128, Carme Rovira105,129, Benoit Roux130,
Ursula Rothlisberger131, Karissa Y. Sanbonmatsu132,133, Tamar Schlick134,135,
Alexey K. Shaytan136,137, Carlos Simmerling3,138, Jeremy C. Smith139,140, Yuji
Sugita141,142,143, Katarzyna Świderek85, Makoto Taiji144, Peng Tao145, D. Peter
Tieleman146, Irina G. Tikhonova147, Julian Tirado-Rives66, Iñaki Tuñón148, Marc W.
van der Kamp149, David van der Spoel2, Sameer Velankar6, Gregory A. Voth150,
Rebecca Wade151, Ariel Warshel152, Valerie Vaissier Welborn37,153, Stacey D.
Wetmore154, Travis J. Wheeler155, Chung F. Wong156, Lee-Wei Yang157, Martin
Zacharias158, Modesto Orozco5,7,✉

Affiliations

1Department of Molecular Biology, University of California San Diego, La Jolla, CA,

2Department of Cell and Molecular Biology, Uppsala University, Uppsala, Sweden.
3Laufer Center for Physical and Quantitative Biology, Stony Brook University, Stony

Brook, NY, USA.
4Department of Biochemistry and Cell Biology, Renaissance School of Medicine,

Stony Brook University, Stony Brook, NY, USA.
5Department of Biochemistry and Molecular Biomedicine, University of Barcelona,

Barcelona, Spain.
6European Molecular Biology Laboratory, European Bioinformatics Institute,

Hinxton, UK.
7Institute for Research in Biomedicine (IRB Barcelona), Barcelona, Spain.
8Structural Bioinformatics and Computational Biochemistry, Department of

Biochemistry, University of Oxford, Oxford, UK.
9Institut Pasteur, Université Paris Cité, CNRS UMR 3528, Computational Structural

Biology Unit, Paris, France.

10Department of Biochemistry and Biophysics, University of Pennsylvania,

Philadelphia, PA, USA.
11Division of Pharmacy and Optometry, University of Manchester, Manchester, UK.
12Scuola Internazionale Superiore di Studi Avanzati-SISSA, Trieste, Italy.
13Computational Biomedicine, Institute of Advanced Simulations IAS-5/Institute

for Neuroscience and Medicine INM-9, Forschungszentrum Jülich GmbH, Jülich,
Germany.
14Department of Physics and Universitätsklinikum, RWTH Aachen University,

Aachen, Germany.
15Department of Chemistry & Chemical Biology, Rutgers University, Piscataway, NJ,

16Istituto Italiano di Tecnologia, Drug Discovery and Development, Bologna, Italy.
17Centre Européen de Calcul Atomique et Moléculaire (CECAM), Ecole

Polytechnique Fédérale de Lausanne (EPFL), Lausanne, Switzerland.
18Department of Chemistry, University of California, Riverside, CA, USA.
19Department of Medicinal Chemistry, College of Pharmacy, University of Utah, Salt

Lake City, UT, USA.
20Department of Physics, University of Washington, Seattle, Washington, USA.
21Pacific Northwest National Laboratory, Richland, Washington, USA.
22LIA CNRS-UIUC, UMR 7019, Université de Lorraine, Vandœuvre-lès-Nancy,

France.
23Department of Physics, University of Illinois at Urbana-Champaign, Urbana, IL,

24Department of Biochemistry and Molecular Biology, The University of Chicago,

Chicago, IL, USA.
25Department of Chemistry, University of Pittsburgh, Pittsburgh, PA, USA.
26Department of Chemistry and Biochemistry, University of Texas at Dallas,

Richardson, TX, USA.
27Department of Physics, University of Texas at Dallas, Richardson, TX, USA.

28Theoretical and Computational Biophysics, Department of Physics, Freie

Universität Berlin, Berlin, Germany.
29Maxwell Centre, Cavendish Laboratory, Department of Physics, University of

Cambridge, Cambridge, UK.
30Yusuf Hamied Department of Chemistry, University of Cambridge, Cambridge, UK.
31Department of Genetics, University of Cambridge, Cambridge, UK.
32Centre for Computational Science, University College London, London, UK.

33Institute for Informatics, University of Amsterdam, Amsterdam, Netherlands.

34Institute of Computer Science, Goethe University Frankfurt, Frankfurt am Main,

Germany.
35Frankfurt Institute for Advanced Studies, Frankfurt am Main, Germany.
36Molecular Sciences Software Institute, Blacksburg, VA, USA.
37Department of Chemistry, Virginia Tech, Blacksburg, VA, USA.
38Institute of Bioengineering, School of Life Sciences, Ecole Polytechnique Fédérale

de Lausanne (EPFL), Lausanne, Switzerland.
39Computational Biomolecular Dynamics Group, Department of Theoretical and

Computational Biophysics, Max Planck Institute for Multidisciplinary Sciences,
Göttingen, Germany.
40Department of Applied Physics, Science for Life Laboratory, KTH Royal Institute of

Technology, Solna, Sweden.
41Laboratory of Molecular Modelling & Drug Discovery, Istituto Italiano di

Tecnologia, Genoa, Italy.
42School of Chemistry and Chemical Engineering, University of Southampton,

Southampton, UK.
43Institute of Structural and Molecular Biology, University College London, London,

UK.
44Department of Chemistry, University of Minnesota, Minneapolis, MN, USA.

45Barcelona Supercomputing Center (BSC), Barcelona, Spain.
46Pharmaceutical Sciences, University of Geneva, Geneva, Switzerland.
47Institute of Pharmaceutical Sciences of Western Switzerland, Geneva,

Switzerland.
48Chemistry Department, University College London, London, UK.
49Swiss Bioinformatics Institute, Geneva, Switzerland.
50Center for Bioinformatics and Integrative Biology (CBIB), Facultad Ciencias de la

Vida, Universidad Andrés Bello, Santiago, Chile.
51Department of Theoretical and Computational Biophysics, Max-Planck-Institute for

Multidisciplinary Sciences, Göttingen, Germany.
52Department of Chemistry and Biochemistry, University of Oregon, Eugene, OR,

53Institut de Ciència de Materials de Barcelona, CSIC, Barcelona, Spain.
54School of Physics and Astronomy, University of Sheffield, Sheffield, UK.

55Pitzer Theory Center and Departments of Chemistry, Bioengineering, Chemical

and Biomolecular Engineering, University of California, Berkeley, Berkeley, CA,
56Department of Chemistry, Johns Hopkins University, Baltimore, MD, USA.
57Spanish National Institute of Bioinformatics (INB)/ELIXIR-ES, Barcelona, Spain.
58National Institute of Biological Sciences, Beijing, China.
59Department of Chemistry, Data Science Institute, University of Wisconsin-

Madison, Madison, WI, USA.
60Department of Theoretical Biophysics, Max Planck Institute of Biophysics,

Frankfurt am Main, Germany.

61Institute for Biophysics, Goethe University Frankfurt, Frankfurt am Main, Germany.
62NBD | Nostrum Biodiscovery, Barcelona, Spain.
63Department of Chemistry, University of Copenhagen, Copenhagen, Denmark.
64Department of Electrical and Computer Engineering, Rutgers University, New

Brunswick, NJ, USA.
65Ferrier Research Institute, Victoria University of Wellington, Wellington, New

Zealand.
66Department of Chemistry, Yale University, New Haven, CT, USA.
67Department of Chemistry, Lund University, Lund, Sweden.

68School of Chemistry and Biochemistry, Georgia Institute of Technology, Atlanta,

GA, USA.
69School of Pharmacy and Centre for Biomolecular Sciences, University of

Nottingham, Nottingham, UK.
70Department of Structural Biology, Stanford University School of Medicine,

Stanford, CA, USA.
71Euler Institute, Faculty of Biomedical Sciences, Università della Svizzera italiana

(USI), Lugano, Switzerland.
72Department of Biochemistry and Biophysics, Science for Life Laboratory,

Stockholm University, Solna, Sweden.

73Structural Biology and NMR Laboratory & the Linderstrøm-Lang Centre for Protein

Science, Department of Biology, University of Copenhagen, Copenhagen, Denmark.
74Department of Chemistry, College of Staten Island, The City University of New

York, New York, NY, USA.
75College of Pharmacy, Western University of Health Sciences, Pomona, CA, USA.
76Institute of Biomedicine, University of Barcelona, Santa Coloma de Gramanet,

Spain.

77Institute of Theoretical and Computational Chemistry, University of Barcelona,

Santa Coloma de Gramanet, Spain.
78Department of Pharmaceutical Sciences, School of Pharmacy, University of

Maryland, Baltimore, MD, USA.
79National Research Council-Institute of Material Foundry at Scuola Internazionale

Superiore di Studi Avanzati (SISSA), Trieste, Italy.
80Groningen Biomolecular Sciences and Biotechnology Institute, University of

Groningen, Groningen, the Netherlands.
81Department of Chemistry and Biochemistry, University of California, San Diego,

La Jolla, CA, USA.
82Department of Pharmacology, University of California, San Diego, La Jolla, CA,

83Lerner Research Institute Cleveland Clinic, Cleveland, OH, USA.
84Department of Chemistry, Michigan State University, East Lansing, MI, USA.
85BioComp Group, Institute of Advanced Materials (INAM), Universitat Jaume I,

Castellón, Spain.
86Centre for Computational Chemistry, School of Chemistry, University of Bristol,

Bristol, UK.
87Department of Chemical and Biological Engineering, Illinois Institute of

Technology, Chicago, IL, USA.

88Department of Biotechnology, Bhupat and Jyoti Mehta School of Biosciences,

Indian Institute of Technology Madras, Chennai, India.
89Department of Biomedical and Chemical Engineering, Syracuse University,

Syracuse, NY, USA.
90Department of Physics, Freie Universität Berlin, Berlin, Germany.
91Department of Mathematics and Computer Science, Freie Universität Berlin,

Berlin, Germany.
92Department of Chemistry, Rice University, Houston, TX, USA.
93Microsoft Research AI4Science, Berlin, Germany.
94School of Physics, Engineering and Technology, University of York, York, UK.

95Department of Inorganic and Analytical Chemistry, Budapest University of

Technology and Economics, Budapest, Hungary.
96Australian Institute for Bioengineering and Nanotechnology, The University of

Queensland, Brisbane, Queensland, Australia.
97Department of Chemistry and Chemical Biology, Northeastern University, Boston,

MA, USA.

98Center for Theoretical Biological Physics, Rice University, Houston, TX, USA.

99Department of Physics and Astronomy, Rice University, Houston, TX, USA.
100Department of BioSciences, Rice University, Houston, TX, USA.
101Department of Computer Science, Virginia Polytechnic Institute and State

University, Blacksburg, VA, USA.
102Department of Physics, Virginia Polytechnic Institute and State University,

Blacksburg, VA, USA.
103Center for Soft Matter and Biological Physics, Virginia Polytechnic Institute and

State University, Blacksburg, VA, USA.
104Institut de Química Computacional i Catàlisi (IQCC) and Departament de

Química, Universitat de Girona, Girona, Spain.
105Catalan Institution for Research and Advanced Studies (ICREA), Barcelona,

Spain.
106Department of Bioengineering, University of California Riverside, Riverside, CA,

107Department of Pathology and Molecular Medicine, School of Medicine, Queen’s

University, Kingston, Ontario, Canada.
108Department of Biology and Molecular Sciences, Queen’s University, Kingston,

Ontario, Canada.
109School of Computing, Queen’s University, Kingston, Ontario, Canada.

110Biomolecular Simulations Group, Institut Pasteur de Montevideo, Montevideo,

Uruguay.
111Bioinformatics Area, DETEMA, Faculty of Chemistry, Udelar, Montevideo,

Uruguay.
112Department of Chemistry, Gottwald Center for the Sciences, University of

Richmond, Richmond, VA, USA.
113Atomistic Simulations, Italian Institute of Technology, Genova, Italy.
114Department of Chemistry and Quantum Theory Project, University of Florida,

Gainesville, FL, USA.
115Computational Biology Lab, Fundación Ciencia & Vida, Santiago, Chile.

116Facultad de Ingeniería, Universidad San Sebastián, Santiago, Chile.
117Department of Chemistry and Biochemistry, University of Delaware, Newark, DE,

118University of Texas Medical Branch, Galveston, TX, USA.
119Dipartimento di Scienze della Salute, Università di Catanzaro, Catanzaro, Italy.

120Laboratory of Theoretical Chemistry, Department of Chemistry, Sorbonne

University, Paris, France.
121Biosystems and Soft Matter Division, Institute of Fundamental Technological

Research, Polish Academy of Sciences, Warsaw, Poland.
122Laboratory for Molecular Modeling, National Institute of Chemistry, Ljubljana,

Slovenia.
123Department of Physics, Faculty of Mathematics and Physics, University of

Ljubljana, Ljubljana, Slovenia.
124Department of Chemistry and Biochemistry, Faculty of Sciences, University of

Porto, Porto, Portugal.
125Department of Biomedical Engineering, The University of Texas at Austin, Austin,

TX, USA.
126Department of Chemistry, University of Bergen, Bergen, Norway.
127Computational Biology Unit, Department of Informatics, University of Bergen,

Bergen, Norway.
128Department of Physics and Astronomy, University College London, London, UK.
129Departament de Química Inorgànica i Orgànica (Secció de Química Orgànica)

and Institut de Química Teòrica i Computacional (IQTCUB), Universitat de
Barcelona, Barcelona, Spain.
130Department of Chemistry, University of Chicago, Chicago, IL, USA.

131Laboratory of Computational Chemistry and Biochemistry, Institute of Chemical

Sciences and Engineering, Swiss Federal Institute of Technology (EPFL),
Lausanne, Switzerland.
132Theoretical Biology and Biophysics, Los Alamos National Laboratory, Los

Alamos, NM, USA.
133New Mexico Consortium, Los Alamos, NM, USA.
134Department of Chemistry and Courant Institute of Mathematical Sciences, New

York University, New York, NY, USA.
135Simons Center for Computational Physical Chemistry, New York University, New

York, NY, USA.

136Department of Biology, Lomonosov Moscow State University, Moscow, Russia.
137International Laboratory of Bioinformatics, AI and Digital Sciences Institute,

Faculty of Computer Science, HSE University, Moscow, Russia.
138Department of Chemistry, Stony Brook University, Stony Brook, NY, USA.
139Biosciences Division and Center for Molecular Biophysics, Oak Ridge National

Laboratory, Oak Ridge, TN, USA.

140Department of Biochemistry and Cellular and Molecular Biology, University of

Tennessee, Knoxville, TN, USA.
141Computational Biophysics Research Team, RIKEN Center for Computational

Science, Kobe, Japan.
142Theoretical Molecular Science Laboratory, RIKEN Cluster for Pioneering

Research, Saitama, Japan.
143Laboratory for Biomolecular Function Simulation, RIKEN Center for Biosystems

Dynamics Research, Kobe, Japan.
144Laboratory for Computational Molecular Design, RIKEN Center for Biosystems

Dynamics Research, Kobe, Japan.
145Department of Chemistry, O’Donnell Data Science and Research Computing

Institute, Center for Drug Discovery, Design, and Delivery (CD4), Southern
Methodist University, Dallas, TX, USA.
146Department of Biological Sciences and Centre for Molecular Simulation,

University of Calgary, Calgary, Alberta, Canada.
147School of Pharmacy, Queen’s University Belfast, Belfast, UK.
148Departamento de Química Física, Universidad de Valencia, Burjassot, Spain.
149School of Biochemistry, University of Bristol, Bristol, UK.
150Department of Chemistry, Chicago Center for Theoretical Chemistry, Institute

for Biophysical Dynamics, and James Franck Institute, The University of Chicago,
Chicago, IL, USA.

151Molecular and Cellular Modeling Group, Heidelberg Institute for Theoretical

Studies (HITS), Heidelberg, Germany.
152Department of Chemistry, University of Southern California, Los Angeles, CA,

153Macromolecules Innovation Institute, Virginia Tech, Blacksburg, VA, USA.
154Department of Chemistry and Biochemistry, University of Lethbridge, Lethbridge,

Alberta, Canada.
155R. Ken Coit College of Pharmacy, University of Arizona, Tucson, Arizona, USA.
156Department of Chemistry and Biochemistry, University of Missouri-St. Louis, St.

Louis, MO, USA.
157Institute of Bioinformatics and Structural Biology, National Tsing Hua University,

Hsinchu, Taiwan.
158Physics Department, Technical University of Munich, Garching, Germany.

Acknowledgements
The authors thank the whole MD community for useful inputs and discussions. The MDDB project is supported
by European Union’s Horizon Europe programme under grant agreement 101094651 awarded to M.O., E.L., S.V.,
J.L.G., J.I., A.C. and P.C.B.

References

1. wwPDB Consortium. Nucleic Acids Res. 47, D520–D528 (2019). (D1). [PubMed: 30357364]
2. Wilkinson MD et al. Sci. Data 3, 160018 (2016). [PubMed: 26978244]
3. Thakur M et al. Nucleic Acids Res. 51, D9–D17 (2023). (D1). [PubMed: 36477213]
4. Rigden DJ & Fernández XM Nucleic Acids Res. 50, D1–D10 (2022). (D1). [PubMed: 34986604]
5. McCammon JA, Gelin BR & Karplus M Nature 267, 585–590 (1977). [PubMed: 301613]
6. Hospital A et al. Wiley Interdiscip. Rev. Comput. Mol. Sci. 10, e1449 (2020).
7. von Delft F et al. Nature 594, 330–332 (2021). [PubMed: 34127864]
8. Dommer A et al. Int. J. High Perform. Comput. Appl. 37, 28–44 (2023). [PubMed: 36647365]
9. da Rosa G et al. Biophys. Rev. 13, 995–1005 (2021). [PubMed: 35059023]
10. Amaro RE & Mulholland AJ J. Chem. Inf. Model. 60, 2653–2656 (2020). [PubMed: 32255648]
11. Beltrán D et al. Nucleic Acids Res. 52, D393–D403 (2024). (D1). [PubMed: 37953362]
12. Hospital A et al. Nucleic Acids Res. 44, D272–D278 (2016). (D1). [PubMed: 26612862]
13. Consortium PDBe-KB. Nucleic Acids Res. 48, D344–D353 (2019). (D1).
14. Dessimoz C & Thomas PD Sci. Data 11, 268 (2024). [PubMed: 38443367]

Fig. 1 |. Data cycle workflow for implementing FAIR (findable, accessible, interoperable and
reusable) principles in biomolecular simulations.

The diagram highlights the added value that can be extracted from accessible open data.
