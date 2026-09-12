# mdCATH: A Large-Scale MD Dataset for Data-Driven Computational Biophysics

**Authors:** Antonio Mirarchi, Toni Giorgino, Gianni De Fabritiis
**Year:** 2024
**Venue:** Scientific Data
**DOI:** 10.1038/s41597-024-04140-z
**Source PDF URL:** local Zotero attachment (already in library)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

mdCATH: A Large-Scale MD
Data Descriptor Dataset for Data-Driven
Computational Biophysics
OPEN

Antonio Mirarchi

1,5

, Toni Giorgino

2,5 ✉

& Gianni De Fabritiis1,3,4 ✉

Recent advancements in protein structure determination are revolutionizing our understanding of
proteins. Still, a significant gap remains in the availability of comprehensive datasets that focus on the
dynamics of proteins, which are crucial for understanding protein function, folding, and interactions.
To address this critical gap, we introduce mdCATH, a dataset generated through an extensive set of
all-atom molecular dynamics simulations of a diverse and representative collection of protein domains.
This dataset comprises all-atom systems for 5,398 domains, modeled with a state-of-the-art classical
force field, and simulated in five replicates each at five temperatures from 320 K to 450 K. The mdCATH
dataset records coordinates and forces every 1 ns, for over 62 ms of accumulated simulation time,
effectively capturing the dynamics of the various classes of domains and providing a unique resource for
proteome-wide statistical analyses of protein unfolding thermodynamics and kinetics. We outline the
dataset structure and showcase its potential through four easily reproducible case studies, highlighting
its capabilities in advancing protein science.

Background and Summary

Proteins, the building blocks of life, are central to nearly all biological processes, and understanding their structure and dynamics is crucial for advancements in fields ranging from biochemistry to pharmaceuticals. The convergence of advanced computational methods and biophysical techniques has led to unprecedented insights into
molecular structures and functions of proteins. Molecular dynamics (MD), for example, is a compute-intensive
technique that attempts to model the dynamics of biological macromolecules in realistic environments, often at
all-atom resolution, based on empirical force-fields whose quality has been improving over decades1–3. Machine
learning, especially through the development of neural network potentials (NNPs), has the potential to further
enhance computational protein research by enabling more accurate predictions and simulations of behaviors4–6.
However, the lack of comprehensive datasets capturing the dynamic behaviors of proteins remains a significant
challenge7. Such datasets are vital for training machine learning models that can predict protein folding, functions, and interactions — often dynamic and transient processes, yet critical for understanding how macromolecules work, interact, and how they might be targeted. High-quality datasets are thus pivotal in advancing our
comprehension of these complex phenomena. In recent years, efforts have been made to provide MD datasets,
especially for key targets in drug discovery. Notable databases include GPCRmd8, a platform dedicated to the
study of G-protein-coupled receptors (GPCRs) dynamics, and SCOV2-MD9 as well as BioExcel-CV1910, both
showcasing the power of collaborative MD databases in the context of COVID-19 research. However, these initiatives are limited by their focus on specific proteome subsets, leaving a gap in comprehensive proteome-wide
dynamic datasets. Previous projects such as MoDEL11, Dynameomics12 and ATLAS13, and the MDDB14 and
MDRepo15 initiatives have been introduced to provide dynamics datasets encompassing a broader range of proteins, often in a single replica and at room temperature, but the computational cost of MD has generally limited
databases in terms of coverage breadth and timescales.
Here, we introduce mdCATH, a dataset focused on providing extensive all-atom MD-derived dynamics for
most protein domains in the CATH classification system16. mdCATH features simulations of 5,398 domains at

Computational Science Laboratory, Universitat Pompeu Fabra, Barcelona Biomedical Research Park (PRBB), Carrer
Dr. Aiguader 88, Barcelona, 08003, Spain. 2Biophysics Institute, National Research Council (CNR-IBF), Via Celoria
26, Milan, 20133, Italy. 3Institució Catalana de Recerca i Estudis Avançats (ICREA), Passeig Lluis Companys 23,
Barcelona, 08010, Spain. 4Acellera Labs, Doctor Trueta 183, Barcelona, 08005, Spain. 5These authors contributed
equally: Antonio Mirarchi, Toni Giorgino. ✉e-mail: toni.giorgino@cnr.it; g.defabritiis@gmail.com

Fig. 1 Exclusion criteria and the resulting number of domains at each step, starting from the 14,433 domains in
the S20 homology set of CATH release 4.2.0, and ending with 5,398 domains included in the mdCATH dataset
presented in this work.

five different temperatures, each in five replicas, therefore offering statistically relevant large-scale insights into
protein structure dynamics under a multiplicity of conditions. This extensive and homogeneously-collected
dataset of all-atom molecular dynamics simulations fills a critical void in the available molecular datasets by
offering a rich, diverse, and physiologically relevant array of protein domain dynamics, enabling systematic,
proteome-wide studies into protein thermodynamics, folding, and kinetics. It is possible to exploit mdCATH for
learning data-driven (e.g. neural network-based) potentials17, also thanks to the inclusion, unique to our knowledge, of instantaneous forces derived from a state-of-the-art all-atom force field. We hope that the mdCATH
dataset will facilitate improvements in the design and refinement of biomolecular force fields.

Dataset Requirements

Our goal is to take a step forward in creating a proteome-wide molecular dynamics dataset for advancing drug
discovery and enabling researchers to explore the dynamic behaviors of diverse protein targets. We built the
mdCATH dataset to meet the following design features:
•

•
•

•
•
•

Comprehensive coverage of structural features. mdCATH provides molecular dynamics information across
5,398 protein domains from the CATH classification system. This extensive coverage ensures a broad representation of the proteome, making the dataset valuable for a wide range of research applications in drug
discovery.
MD-derived coordinates and forces. The dataset includes both coordinates and forces from simulated trajectories. The presence of forces is a unique feature in this dataset, which enables training force-based machine
learning potentials.
Wide conformational space sampling. mdCATH features multiple replicas at different temperatures, capturing
a variety of conformations, including higher energy states encountered in molecular dynamics simulations.
This ensures that the potential functions trained on this dataset produce accurate results across all relevant
conformations.
High quality data. To ensure the highest accuracy, mdCATH utilizes state-of-the-art force fields, code, and
computational resources. The accuracy of the dataset directly impacts the performance of models trained on
it, making the use of the most accurate level of theory practical a priority.
Derived metadata. The dataset includes pre-computed information such as root-mean-square deviation
(RMSD), root-mean-square fluctuation (RMSF), secondary structure composition, and so on.
Reproducibility. Reproducibility is ensured by including the PDB and PSF files in the dataset. Additionally, the
data is stored in the efficient HDF5 binary data format, facilitating easy access and manipulation of the dataset
for further research and model training.

Methods

We built the dataset on the basis of the domain definitions provided by the CATH database18–20. CATH, a publicly available resource maintained by the Orengo group, provides a set of domains clustered by general architecture according to the class, architecture, topology, and homologous superfamily hierarchy16. We started from
14,433 non-homologous domains at the S20 (20%) homology level in CATH release 4.2.0. We then restricted
the selection to the subset of 13,470 domains between 50 and 500 amino acids, to focus on globular structures.
Next, we excluded all the structures whose backbone was non-contiguous, e.g. due to unresolved regions in the
original experimental structures; we also excluded sequences containing non-standard amino acids (also absent
from CATH model files). The inclusion criteria left 5,883 residues for further processing.
All the domain structures have been prepared with a standard protonation protocol at pH 7 including charge
state assignments, proton placement and H-bond network optimization21. Peptide chains were capped with

Field

Size

Type

Unit

Description

Domain ID/
chain

element

pdb

psf

pdbProteinAtoms

resid

resname

z

.numResidues

N

string

Chain ID

N

string

Chemical element

string

PDB file used for simulation

string

Topology file used for simulation

string

PDB file with the N reported atoms

N

integer

Residue number

N

string

Residue name

N

integer

Atomic number

integer

Number of residues (attribute)

coords

forces

dssp

gyrationRadius

rmsd

rmsf

box

.numFrames

Group for the 320 K simulations
Data of the first replica
F×N×3

float

Å

Atom coordinates

F×N×3

float

kcal/mol/Å

Forces

nm

Gyration radius

F×R

string

F

double

DSSP secondary str. assignments

F

float

nm

Root-mean square deviation w.r.t. begin

R

float

nm

Cα root-mean-square fluctuation

3×3

float

nm

integer

Simulation unit cell
Number of frames for this replica (attribute)
Second replica

…
…

Table 1. Hierarchical organization of the data fields in the mdCATH dataset, with units and description. The
following groups and fields are provided in an HDF5 file for each simulated CATH domain. Key: N, number of
atoms; R, number of residues; F, trajectory length in frames (1 frame corresponds to 1 ns of simulated time).

Fig. 2 (a) Distribution of the number of atoms per domain, revealing a variation of nearly an order of
magnitude in the atom counts across systems. (b) Distribution of the total number of residues per domain,
showing a broad peak of around 100 residues and a long tail of up to 500 residues (cut-off size). (c) Distribution
of trajectory lengths, peaking at 500 ns. (d) Distribution of root mean square deviation (RMSD) of the protein’s
heavy atoms between the first and the last frame of each trajectory.

Domains

5,398

Trajectories

134,950

Total sampled time

62.6 ms

Total atoms

11,671,592

Total amino acids

740,813

Avg. traj. length

464 ns

Avg. system size

2,162 atoms

Avg. domain length

137 AAs

Total file size

3.3 TB

Table 2. Descriptive statistics of the mdCATH dataset.

Fig. 3 Relation between the radius of gyration and the number of residues in α or β secondary structure
elements for six of the mdCATH domains simulated. Each point represents a frame, taken between 0 and 500 ns
(blue to yellow) at 1 ns intervals, from the first replica of a run at 320 K.

acetylated and N-methylated termini. The systems were solvated in cubic boxes of TIP3P water with at least
9 Å of padding on each side, neutralized, and ionized with Na+ and Cl− ions at 0.150 M concentration. Systems
whose resulting solvation cubic box was larger than (100 Å)3 were discarded. The final dataset includes 5,398
accepted domains, as illustrated in Fig. 1. HTMD version 1.16 was used for all the building steps22,23.
All systems were parameterized with the CHARMM22* forcefield1. Long-range electrostatic forces were
treated with the particle-mesh Ewald (PME) summation24, with an integration timestep of 4 fs enabled by the
hydrogen mass repartitioning scheme of 4 amu per H atom25. The simulations were performed with ACEMD26
on GPUGRID.net distributed network27.
Each system thus obtained was subjected to a pre-equilibration phase for 20 ns with a time-step of 4 fs in the
NPT ensemble at 1 atm and 300 K utilizing the Montecarlo barostat. Harmonic restraints were applied to the
protein’s carbon α atoms (1.0 kcal/mol/Å) and heavy atoms (0.1 kcal/mol/Å) to maintain them close to their
initial positions during the first half (10 ns) of equilibration. The second half of equilibration (10 ns to 20 ns) was
performed without restraints. No restraints were used during the subsequent production phase.
The final configuration of each system was used as a starting point for 25 production simulations, spawning
runs at five temperatures in geometric progression (320 K, 348 K, 379 K, 413 K, 450 K), each in five replicas. The
production simulations were performed in the NVT ensemble using Langevin thermostat for integration and a
0.1 ps−1 relaxation time. The use of the constant-volume ensemble sidesteps issues with the poor reproduction
of the water phase and pressure by TIP3P28,29. Bonds involving hydrogen atoms were constrained at the equilibrium length with the M-shake algorithm30 with a tolerance of 10−5. Atom positions and forces acting on each
atom were recorded every 1 ns and made available as part of the dataset as described below. A sampling rate of

Fig. 4 Relation between the radius of gyration and the number of residues in α or β secondary structure
elements for domain 5sicI00 (subtilisin inhibitor-like, a 2-layer α-β sandwich of 106 amino acids) at
increasing temperatures. Destabilization is seen at 413 K, and at 450 K complete unfolding occurs within 100 ns
(last two panels, fixed scale and full view respectively). Axes and legend are as in Fig. 3.

1 ns bounds the tractable kinetics, enabling the resolution of the dynamics of relatively slow degrees of freedom
such as conformational changes, but not faster motions (e.g. solvent-exposed side-chain rotations). For both
NPT and NVT simulations, a 9 Å cutoff was applied for PME, while van der Waals interactions used a cutoff of
9 Å and a switching distance of 7.5 Å. Analysis of the trajectories was conducted using the HTMD library23, in
order to include potentially useful pre-computed metadata. Secondary structure assignments have been computed for each frame and residue using the implementation of the DSSP algorithm in moleculekit version 1.8.32,
encoded following the customary 8-class codes31.

Data Records

The mdCATH dataset makes the trajectories available under a CC BY 4.0 license. It is available at HuggingFace32.
It is possible to (1) download individual domain files from HuggingFace via a browser; (2) retrieve them
via the HuggingFace dataset API (Listing 2); (3) visualize them interactively (without downloading) on the
PlayMolecule website (see the “Code Availability” section); (4) download them from PlayMolecule in XTC
format.

Organization. The dataset is provided as a set of files in the Hierarchical Data Format, version 5 (HDF5).
HDF5 allows the efficient storage and random access of heterogeneous data fields and arrays organized in a
filesystem-like hierarchy. For the sake of simplicity, all of the data related to a given domain were collected into
an individual HDF5 file. The dataset provided is structured into fields that describe snapshots of molecular simulation trajectories and derived quantities as shown in Table 1. The root group of each file in the dataset is the
domain ID, which aggregates fields such as chain, element, resid, resname, and z, each a vector of length
N, representing the number of protein atoms. The pdb and psf strings hold, respectively, the verbatim PDB
file used for the simulation (with solvent) and its topology in CHARMM/XPLOR protein structure file (PSF)
format; pdbProteinAtoms holds a PDB of the N solute atoms used for analysis. Data on the dynamics are
organized hierarchically: five groups at the top-most level named according to the temperature; each temperature group includes five groups for each of the replicas; finally, each replica holds fields for atomic coordinates,
forces, simulation box, as well as pre-computed derived quantities such as secondary structure assignments,
instantaneous gyration radius, root-mean-square deviation, and fluctuations. Coordinates and forces are stored
as three-dimensional arrays, their axes running along frames, atoms, and spatial dimensions. DSSP secondary
structure assignments are provided per residue and frame following the standard 8-letter codes.
Size. At the production cut-off date, we collected 134,950 trajectories for 5,398 domains, which were included

in the dataset. Figure 2a and 2b show the distribution of system sizes that made it to the production simulation
phase in terms of the number of solute atoms and the number of amino acids. Due to the distributed nature of
the computing network, the length of the simulations varies (independently from system size), the majority of

Fig. 5 Relationship between the fraction of time each residue spends in α or β secondary structure elements
and its root mean squared fluctuation (RMSF) across actin-binding protein T-fimbrin domain (5j8eA00),
cytochrome Bc1 complex domain (2a06B02), and HUP superfamily domain (2xryA01). Each point
indicates a residue, colored by its position along the sequence, from purple (N-terminal) to red (C-terminal).
The relationship is presented in two temperature conditions, 320 K (left) and 450 K (right; note the different
RMSF scale). At 320 K, secondary structure presence exhibits a bimodal distribution, weakly correlated with
RMSF. Bimodality disappears at 450 K, showing a continuum in the participation to structure elements, which is
roughly inversely correlated to the corresponding fluctuations.

trajectories being 500 ns long (average 464 ns, standard deviation 76 ns; Fig. 2c). The total simulated time is over
62 ms. The full dataset size is over 3 TB. Further aggregate statistics are reported in Table 2.

Technical Validation

We perform several statistical analyses of the dataset to validate its content.

Validation of temperature denaturation. As a first validation of the dataset, we examined the correlation between the amount of secondary structure and the radius of gyration, which was assumed to be a proxy for

Fig. 6 Distribution of protein secondary structures content–helical (top), strand (left), and coil/turn (right)–
organized by CATH domain class and temperature. It represents data taken from the final snapshot of all
replicas across all domains, illustrating how the proportions of helical and strand structures shift toward coil
content as temperatures increase.

domain compactness. The fraction of amino acids that are in helical or β-strand configurations, represented by
the DSSP codes G, H, I, E, and B, is used to define the amount of secondary structure. This will be referred to as
“α + β” for simplicity. Figure 3 shows the results for six domains at 320 K (only one replica is shown for clarity).
The radius of gyration and the fraction of sequence in secondary structure elements naturally depend on the
domain architecture. At 320 K the domains are generally stable, and both values exhibit fluctuations around mean
values but no systematic drift nor marked correlations, with the possible exception of 1w9rA00, which undergoes a transition compacting its radius of gyration from 2.4 nm to 1.8 nm.
We then validated whether the relationship holds at increasing temperatures. Figure 4 shows the relation between the radius of gyration and the fraction of sequence in secondary structure elements for a specific domain, subtilisin inhibitor-like, a 2-layer α-β sandwich of 106 amino acids (CATH-Gene3D entry
G3DSA:3.30.350.10), at increasing temperatures. Between 320 K and 379 K, the dynamics appear essentially
unchanged, namely both quantities fluctuate randomly and uncorrelated within the 500 ns of sampled time.

Fig. 7 Example of an mdCATH trajectory loaded in the PlayMolecule platform.

Some destabilization starts to appear at 413 K: the fraction of α/β structure is unchanged, while the radius of
gyration has a marked increase beyond the 1.4 nm threshold. At 450 K the system unfolds: the amount of secondary structure drops below 30%, and the radius of gyration grows beyond 1.5 nm within 100 ns.

Fluctuation-unfolding cooperativity.

We further validated the dataset by assessing the fluctuation of
residues in relation to secondary structure and temperatures. Figure 5 displays, for each residue, the fraction of
time spent in an α or β secondary structure element compared to the root mean squared fluctuation (RMSF) of
the same residue. The structure-fluctuation relationships are shown for three domains taken as examples, namely
5j8eA00 (actin-binding protein, T-fimbrin, domain 1; mainly α), 2a06B02 (cytochrome Bc1 complex, chain
A, domain 1; α-β), and 2xryA01 (HUP superfamily, 6-strand sheet Rossmann fold), in rows, each shown at
low (320 K, left column) and high temperature (450 K, right column). A clear inverse relationship between local
structure and fluctuation emerges which supports that the dataset is well constructed.

Class-wise thermodynamics of denaturation. It is possible to combine the annotations and metadata
provided by the CATH database to cross-reference dynamic data with protein classification. For example, we
can leverage CATH metadata by conditioning the analysis on the top-most classification level of CATH (Class),
defined in terms of the general architectural organization of the domain: mainly α, mainly β, α-β, few secondary
structures, and special.
Figure 6 illustrates the construction of probability distribution for various domains, conditioned using domain
class annotations. This figure uses ternary plots to show the distribution of protein secondary structures — helical
(top), strand (left), and coil/turn (right) content — on a plane. These plots are based on data from the last snapshot of all replicas across all domains, categorized by temperature and domain type. The plots clearly show a shift
in the fractions of helical and strand structures toward coil content at temperatures of 413 K and 450 K. Notably,
the strand content shows greater resistance to thermal denaturation compared to the helical content.
Kinetics of secondary structure loss.

As a last example, we show how it is possible to combine the annotations and metadata provided by the CATH database to extract proteome-wide kinetic data. Supplementary
Figure S1 analyzes the conservation of α/β structure in time as a function of temperature for the four classes
(mdCATH has no representative of the “special” class). Each panel reports time on the horizontal axis and the
fraction of residues in secondary structure elements, normalized so the initial value is one, on the vertical axis.
Values for 50 domains per class and replicas are aggregated and displayed as distributions. Different cooperativity
regimes emerge for the four classes (Kolmogorov-Smirnov tests for all distribution pairs at 400 ns: p ≪ 10−6).

Mainly β domains appear to be the most stable, losing structure only at 450 K. Mainly α domains exhibit a partial
loss of structure at 413 K; interestingly, at 450 K their transition to a low-secondary structure state is, on average, abrupt (∼100 ns). Mixed α-β domains have an intermediate behaviour showing aspects of both. Lastly, as
expected, the few secondary structures class is pretty much diffuse and heterogeneous.

Usage Notes

An ad-hoc class, torch_geometric.data.Dataset, has been integrated into TorchMD-Net33 to streamline the use of the mdCATH dataset, providing precise control over the protein domain selection and advanced
filtering options for trajectories. Listing 1 shows a self-contained code demonstrating how to use the mdCATH
data loader in TorchMD-Net for model training, highlighting how additional dataset arguments can be used to
focus on specific cases of interest. Future dataset releases will include additional simulations at 300 K to expand
coverage around room-temperature conditions.

Listing 1. Importing mdCATH as a training set in TorchMD-NET.

Listing 2. Example of how to download an mdCATH HDF5 file using the HuggingFace API.

Code availability

Companion code to load the HDF5 files in VMD34 for interactive inspection and analysis, to import them in
HTMD molecular analysis library23, and to convert them to standard molecular file formats (PDB and XTC)
is provided at https://github.com/compsciencelab/mdCATH. In addition to HuggingFace, the full dataset is
also available in the PlayMolecule.org interactive viewer at https://open.playmolecule.org/mdcath, both for
visualization and for further processing via the PlayMolecule platform21,35 (Fig. 7). All the scripts used to generate
and analyze the mdCATH dataset are also available at https://github.com/compsciencelab/mdCATH.
Received: 23 July 2024; Accepted: 15 November 2024;
Published: xx xx xxxx

References

1. Piana, S., Lindorff-Larsen, K. & Shaw, D. E. How Robust Are Protein Folding Simulations with Respect to Force Field
Parameterization? Biophysical Journal 100, L47–L49, https://doi.org/10.1016/j.bpj.2011.03.051 (2011).
2. MacKerell, A. D. et al. All-Atom Empirical Potential for Molecular Modeling and Dynamics Studies of Proteins. The Journal of
Physical Chemistry B 102, 3586–3616, https://doi.org/10.1021/jp973084f (1998).
3. Piana, S., Robustelli, P., Tan, D., Chen, S. & Shaw, D. E. Development of a Force Field for the Simulation of Single-Chain Proteins and
Protein–Protein Complexes. Journal of Chemical Theory and Computation 16, 2494–2507, https://doi.org/10.1021/acs.jctc.9b00251
(2020).
4. Anand, N. & Achim, T. Protein structure and sequence generation with equivariant denoising diffusion probabilistic models. arXiv
preprint arXiv:2205.15019 (2022).
5. Mosalaganti, S. et al. Ai-based structure prediction empowers integrative structural analysis of human nuclear pores. Science 376,
eabm9506 (2022).
6. Isert, C., Atz, K. & Schneider, G. Structure-based drug design with geometric deep learning. Current Opinion in Structural Biology
79, 102548 (2023).
7. Vander Meersche, Y., Cretin, G., de Brevern, A. G., Gelly, J.-C. & Galochkina, T. Medusa: prediction of protein flexibility from
sequence. Journal of molecular biology 433, 166882 (2021).
8. Rodrguez-Espigares, I. et al. Gpcrmd uncovers the dynamics of the 3d-gpcrome. Nature Methods 17, 777–787 (2020).
9. Torrens-Fontanals, M. et al. SCoV2-MD: a database for the dynamics of the SARS-CoV-2 proteome and variant impact predictions.
Nucleic Acids Research 50, D858–D866, https://doi.org/10.1093/nar/gkab977 (2022).
10. Beltrán, D., Hospital, A., Gelp, J. L. & Orozco, M. A new paradigm for molecular dynamics databases: the covid-19 database, the
legacy of a titanic community effort. Nucleic Acids Research 52, D393–D403 (2024).
11. Meyer, T. et al. MoDEL (Molecular Dynamics Extended Library): a database of atomistic molecular dynamics trajectories. Structure
(London, England: 1993) 18, 1399–1409, https://doi.org/10.1016/j.str.2010.07.013 (2010).
12. van der Kamp, M. W. et al. Dynameomics: A comprehensive database of protein dynamics. Structure 18, 423–435, https://doi.
org/10.1016/j.str.2010.01.012 (2010).
13. Vander Meersche, Y., Cretin, G., Gheeraert, A., Gelly, J.-C. & Galochkina, T. Atlas: protein flexibility description from atomistic
molecular dynamics simulations. Nucleic Acids Research 52, D384–D392 (2024).
14. Amaro, R. et al. The need to implement fair principles in biomolecular simulations (2024).
15. Roy, A. et al. Mdrepo – an open environment for data warehousing and knowledge discovery from molecular dynamics simulations.
bioRxiv https://doi.org/10.1101/2024.07.11.602903 (2024).
16. Sillitoe, I. et al. CATH: increased structural coverage of functional space. Nucleic Acids Research 49, D266–D273, https://doi.
org/10.1093/nar/gkaa1079 (2021).
17. Mirarchi, A., Peláez, R. P., Simeon, G. & De Fabritiis, G. AMARO: All heavy-atom transferable neural network potentials of protein
thermodynamics. J. Chem. Theory Comput. https://doi.org/10.1021/acs.jctc.4c01239. Preprint available at https://arxiv.org/
abs/2409.17852 (2024).
18. Sillitoe, I. et al. CATH: expanding the horizons of structure-based functional annotations for genome sequences. Nucleic acids
research 47, D280–D284 (2019).
19. Pearl, F. M. et al. The CATH database: an extended protein family resource for structural and functional genomics. Nucleic acids
research 31, 452–455 (2003).
20. Orengo, C. A. et al. CATH–a hierarchic classification of protein domain structures. Structure 5, 1093–1109 (1997).
21. Martínez-Rosell, G., Giorgino, T. & De Fabritiis, G. PlayMolecule ProteinPrepare: A Web Application for Protein Preparation for
Molecular Dynamics Simulations. Journal of Chemical Information and Modeling 57, 1511–1516, https://doi.org/10.1021/acs.
jcim.7b00190 (2017).
22. Doerr, S., Giorgino, T., Martínez-Rosell, G., Damas, J. M. & De Fabritiis, G. High-Throughput Automated Preparation and
Simulation of Membrane Proteins with HTMD. Journal of Chemical Theory and Computation 13, 4003–4011, https://doi.
org/10.1021/acs.jctc.7b00480 (2017).
23. Doerr, S., Harvey, M. J., Noé, F. & De Fabritiis, G. HTMD: High-Throughput Molecular Dynamics for Molecular Discovery. Journal
of Chemical Theory and Computation 12, 1845–1852, https://doi.org/10.1021/acs.jctc.6b00049 (2016).
24. Darden, T., York, D. & Pedersen, L. Particle mesh Ewald: An N log(N) method for Ewald sums in large systems. The Journal of
Chemical Physics 98, 10089–10092, https://doi.org/10.1063/1.464397 (1993).
25. Feenstra, K. A., Hess, B. & Berendsen, H. J. C. Improving efficiency of large time-scale molecular dynamics simulations of hydrogenrich systems. Journal of Computational Chemistry 20, 786–798, https://doi.org/10.1002/(SICI)1096-987X(199906)20:8<786::AIDJCC5>3.0.CO;2-B (1999).
26. Harvey, M. J., Giupponi, G. & Fabritiis, G. D. Acemd: accelerating biomolecular dynamics in the microsecond time scale. Journal of
chemical theory and computation 5, 1632–1639 (2009).
27. Buch, I., Harvey, M. J., Giorgino, T., Anderson, D. P. & De Fabritiis, G. High-throughput all-atom molecular dynamics simulations
using distributed computing. Journal of Chemical Information and Modeling 50, 397–403, https://doi.org/10.1021/ci900455r (2010).
28. Quoika, P. K. & Zacharias, M. Liquid–Vapor Coexistence and Spontaneous Evaporation at Atmospheric Pressure of Common Rigid
Three-Point Water Models in Molecular Simulations. The Journal of Physical Chemistry B 128, 2457–2468, https://doi.org/10.1021/
acs.jpcb.3c08183 (2024).
29. Vega, C., Abascal, J. L. F., Conde, M. M. & Aragones, J. L. What ice can teach us about water interactions: a critical comparison of the
performance of different water models. Faraday Discussions 141, 251–276, https://doi.org/10.1039/B805531A (2008).
30. Kräutler, V. & van Gunsteren, W. F. & Hünenberger, P. H. A fast SHAKE algorithm to solve distance constraint equations for small
molecules in molecular dynamics simulations. Journal of Computational Chemistry 22, 501–508, https://doi.org/10.1002/1096987X(20010415)22:5<501::AID-JCC1021>3.0.CO;2-V (2001).
31. Kabsch, W. & Sander, C. Dictionary of protein secondary structure: Pattern recognition of hydrogen-bonded and geometrical
features. Biopolymers 22, 2577–2637, https://doi.org/10.1002/bip.360221211 (1983).
32. Mirarchi, A., Giorgino, T. & Fabritiis, G. D. mdCATH (Revision 2393a6d) https://doi.org/10.57967/hf/3201 (2024).

33. Pelaez, R. P. et al. Torchmd-net 2.0: Fast neural network potentials for molecular simulations. Journal of Chemical Theory and
Computation, (2024).
34. Humphrey, W., Dalke, A. & Schulten, K. VMD: Visual molecular dynamics. Journal of Molecular Graphics 14, 33–38, https://doi.
org/10.1016/0263-7855(96)00018-5 (1996).
35. Torrens-Fontanals, M., Tourlas, P., Doerr, S. & De Fabritiis, G. PlayMolecule Viewer: A Toolkit for the Visualization of Molecules
and Other Data. Journal of Chemical Information and Modeling 64, 584–589, https://doi.org/10.1021/acs.jcim.3c01776 (2024).

Acknowledgements

AM is financially supported by Generalitat de Catalunya’s Agency for Management of University and Research
Grants (AGAUR) PhD grant FI-1-00278 and PID2020-116564GB-I00 has been funded by MCIN / AEI /
https://doi.org/10.13039/501100011033. TG acknowledges financial support from the Spoke 7 of the National
Centre for HPC, Big Data and Quantum Computing (Centro Nazionale 01 – CN0000013), funded by the
European Union–NextGenerationEU, Mission 4, Component 2, Investment line 1.4, CUP B93C22000620006;
from the PRIN 2022 (BioCat4BioPol) from the Ministero dell’Università e Ricerca, funded by the European
Union–NextGenerationEU, Mission 4 Component C2, CUP B53D23015140006; and from the project InvAtInvecchiamento Attivo e in Salute (FOE 2022) CUP B53C22010140001. We thank the volunteers of GPUGRID.net
for donating computing time for the simulations. Research reported in this publication was partially supported
by the National Institute of General Medical Sciences (NIGMS) of the National Institutes of Health under award
number R01GM140090. The content is solely the responsibility of the authors and does not necessarily represent
the official views of the National Institutes of Health.

Author contributions

G.D.F.: design and project lead. T.G.: generation of the MD data. AM: conversion of MD trajectories into HDF5
datasets. A.M., T.G. and G.D.F.: data analysis and writing-up of the manuscript.

Competing interests

The authors declare no competing interests.

Additional information

Supplementary information The online version contains supplementary material available at https://doi.org/
10.1038/s41597-024-04140-z.
Correspondence and requests for materials should be addressed to T.G. or G.D.F.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International
License, which permits use, sharing, adaptation, distribution and reproduction in any medium or
format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the
material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the
copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
© The Author(s) 2024
