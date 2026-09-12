# Group D: Datasets, generative ensembles, ensemble resolution

13 papers.



---

# ATLAS: protein flexibility description from atomistic molecular dynamics simulations

**Authors:** Yann Vander Meersche, Gabriel Cretin, Aria Gheeraert, Jean-Christophe Gelly, Tatiana Galochkina
**Year:** 2024
**Venue:** Nucleic Acids Research
**DOI:** 10.1093/nar/gkad1084
**Source PDF URL:** https://europepmc.org/articles/PMC10767941?pdf=render (Europe PMC copy of PMC10767941; gold OA, Nucleic Acids Research)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Nucleic Acids Research, 2024, 52, D384–D392
https://doi.org/10.1093/nar/gkad1084
Advance access publication date: 20 November 2023
Database issue

ATLAS: protein flexibility description from atomistic
molecular dynamics simulations
Yann Vander Meersche , Gabriel Cretin , Aria Gheeraert , Jean-Christophe Gelly * and
Tatiana Galochkina *
Université Paris Cité and Université des Antilles and Université de la Réunion, INSERM, BIGR, F-75014 Paris, France
*

To whom correspondence should be addressed. Tel: +33 1 81 72 43 30; Email: tatiana.galochkina@u-paris.fr
Correspondence may also be addressed to Jean-Christophe Gelly. Tel: +33 1 81 72 43 23; Email: jean-christophe.gelly@u-paris.fr

Abstract
Dynamical behaviour is one of the most crucial protein characteristics. Despite the advances in the field of protein structure resolution and prediction, analysis and prediction of protein dynamic properties remains a major challenge, mostly due to the low accessibility of data and its diversity
and heterogeneity. To address this issue, we present ATLAS, a database of standardised all-atom molecular dynamics simulations, accompanied
by their analysis in the form of interactive diagrams and trajectory visualisation. ATLAS offers a large-scale view and valuable insights on protein
dynamics for a large and representative set of proteins, by combining data obtained through molecular dynamics simulations with information
extracted from experimental structures. Users can easily analyse dynamic properties of functional protein regions, such as domain limits (hinge
positions) and residues involved in interaction with other biological molecules. Additionally, the database enables exploration of proteins with
uncommon dynamic properties conditioned by their environment such as chameleon subsequences and Dual Personality Fragments. The ATLAS
database is freely available at https://www.dsimb.inserm.fr/ATLAS.

Graphical abstract

Introduction
Proteins are dynamic entities that undergo continuous conformational changes of varying magnitudes, which are essential in biological processes such as enzyme catalysis, proteinprotein interactions, and allosteric enzyme activation (1–3).
Information on protein flexibility can be obtained using experimental methods, such as X-ray crystallography (B-factor)
or NMR spectroscopy (order parameter), However, these
methods have limitations. First, experimental methods can
only provide indirect information on protein dynamics without atomistic details on the corresponding transitions. Secondly, experimental conditions vary significantly, complicat-

ing comparison across experiments and are often far from the
conditions expected in vivo (4–7). While the current revolution in the field of structural bioinformatics brought by the
AlphaFold2 (8) release has significantly democratised access
to static three-dimensional structures of numerous proteins,
analysis and prediction of protein dynamics still remains one
of the most important challenges, primarily due to the lack of
reliable data (9,10).
During the last decades, molecular dynamics (MD) simulations were demonstrated to provide valuable information on
protein conformational behaviour on both local and global
scales (11–16). In particular, protein structure ensembles gen-

Received: August 11, 2023. Revised: October 15, 2023. Editorial Decision: October 25, 2023. Accepted: October 30, 2023
© The Author(s) 2023. Published by Oxford University Press on behalf of Nucleic Acids Research.
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/),
which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

erated using MD trajectories of tens of nanoseconds enhance
docking performance (17–21), allow detection of pockets participating in protein-protein interaction (22) or detect flexibility patterns characteristic for residues involved in proteinprotein interface formation (23). MD simulations lasting for
hundreds of nanoseconds allow detection of allosteric pathways (24–26), while longer MD can bring valuable insights
on major conformational changes (27,28). Nevertheless, systematic comparative analysis of simulations conducted by different research groups is significantly complicated by the divergence in the system settings, MD simulations protocols as
well as software and force field used for the simulations. To
overcome this issue, several initiatives have led to the release of
public databases for specific protein classes. Examples include
MemProtMD (29), which focuses on coarse-grained simulations of membrane proteins, GPCRmd (30), which gathers
trajectories of G protein-coupled receptor (GPCR) proteins,
and SCoV2-MD (31), gathering simulations and analysis of
SARS-CoV-2 proteins. Prior to our work, only two databases
attempted to provide general datasets of MD for soluble proteins: MoDEL (32) and Dynameomics (33). However, only
MoDEL is still accessible, though it is only partially functional
and no longer updated. Dynameomics contained native state
as well as unfolding dynamics, but is currently inaccessible.
Additionally, both databases face issues, the major one being
the lack of a uniform protocol, necessary for rigorous comparison between multiple protein simulations, and replicates
for ensuring model reliability.
Here, we present ATLAS, a database of standardised allatom molecular dynamics simulations on a large set of representative protein structures. All the trajectories, their analyses,
as well as their biological annotations are freely accessible online in the form of a website containing interactive diagrams
and trajectory visualisation at https://www.dsimb.inserm.fr/
ATLAS. ATLAS consists of three datasets of molecular dynamics simulations. Currently, the main ATLAS dataset comprises
1390 protein chains, carefully chosen to provide an exhaustive sampling of the conformational space within the Protein
Data Bank (PDB) (34). Two other datasets focus on proteins
with specific dynamics behaviour. First one reports MD of 100
proteins containing Dual Personality Fragments (DPFs). DPFs
are protein regions that can exist in both disordered and ordered states within different crystallographic structures of the
same protein (35). The transition of a DPF to an ordered state
is often associated with the presence of a protein partner or interaction with a ligand. The second one reports dynamics for
32 proteins containing chameleon sequences (36), which can
adopt a different ordered secondary structure conformation
(α-helix or β-strand) in different proteins. Both chameleon sequences and Dual Personality Fragments are of great biological interest and the understanding of their dynamic properties
can bring new information on the mechanism of the corresponding protein function and evolution.

Materials and methods

D385
have first selected all X-ray structures of protein chains of
at least 38 residues long with resolution below or equal to
2 Å, in accordance with MolProbity’s quality thresholds (38).
We have filtered out proteins without an ECOD ID (v285)
and membrane proteins (consensus of OPM (39), PDBTM
(40), MemProtMD (29), and mpstruc from RCSB PDB - April
2023) (41). We then selected the best chain for each ECOD
X-class domain. To do so, proteins with more than 10 consecutive missing residues were excluded. Among the remaining
proteins, we prioritised those present in the quality-filtered rotamer datasets Top8000 and Top2018 (38,42). We also gave
priority to proteins crystalised in monomeric state by selecting
first structures crystalised as monomers and predicted by PISA
(43) as such, then monomeric structures predicted as multimeric by PISA and finally multimeric structures. In cases of
multiple resolved structures, we selected one of them based
on i) the lowest number of consecutive gaps, ii) the biggest
sequence length, and iii) the lowest proportion of gapped positions with respect to the protein sequence length. Therefore,
the ATLAS dataset contains 1068 proteins with 1149 strictly
non-redundant X-class ECOD domains, which we will further
refer to as ‘non-redundant core’.
For 322 proteins of the non-redundant core, we have performed MD simulations of the alternative high-quality protein
structures sharing the same ECOD X-class. The main goal of
ATLAS is to provide several representative dynamics per structural class and progressively expand it. For today, the ATLAS
dataset contains MD trajectories for 1390 different proteins.
Chameleon sequences
For all chameleon sequences of the ChSeq database (36)
longer than 7 amino acids we have manually chosen those
containing high-quality structures. We have selected two protein structures per chameleon sequence: one for helical and
one for β-strand conformation.
Dual personality fragments
To identify proteins containing DPFs, we used the following
protocol. First, we gathered all high-quality protein structures
from the PDB with a resolution of 2 Å or better, matching the
same protein sequence. Within each group of structures, we
identified the largest continuous protein fragment that was
observed in both the folded and disordered states (missing
residues in the PDB file), excluding extremities. We then selected the best quality representative structure in the folded
state. To ensure diversity, we filtered out proteins with sequences sharing more than 20% identity using MMseqs2 (44).
From the remaining candidates, we selected 100 DPFs with
lengths ranging from 8 to 20 amino acids, while sampling fragments that adopt alpha, beta and coil secondary structures in
equal proportion. We used Dictionary of Secondary Structure
of Proteins (DSSP) assignments to define these classes (45). A
fragment with four consecutive helix residues or more is assigned to the alpha helix class, and one with 3 consecutive
strand residues is allocated to the beta sheet class. If none of
these conditions are verified, the fragment is assigned as coil.

Protein selection
Representative dataset (ATLAS dataset)
High-quality protein chains from the PDB (version of July
2022) were thoroughly filtered to ensure structural diversity
by removing redundancy in terms of X-class ECOD (37) domains (indicating similar fold and possible homology). We

Protein structure preparation for MD simulations
All water and ligand molecules were removed from crystal structures to ensure protocol uniformity. Missing residues
were modelled using MODELLER v10.1 (46) for proteins
with no more than five consecutive gaps (or modified residues)

D386
and AlphaFold v2.1.0 (8) for proteins with 6–10 consecutive
gaps in their resolved structures. These thresholds were chosen to maximise model reliability within reasonable computation time. Indeed, only 2.5% of the reconstructed residues
with MODELLER have a low accuracy for five residue long
loop reconstruction, and 0% below this threshold (47). For
DPF and chameleon sequences, we used only MODELLER to
complete missing residues.

Molecular dynamics simulation protocol
All-atom molecular dynamics simulations were performed
with GROMACS v2019.4 (48) with the CHARMM36m force
field (July 2020 version), which was developed to provide a
balanced sampling of folded and unfolded conformations for
both folded and intrinsically disordered proteins (49) and provides extensive parameters for various compounds such as
proteins, lipids and sugars (50). Each protein was placed in a
periodic triclinic box, solvated using TIP3P water molecules,
and neutralised with Na+ /Cl− ions at a concentration of 150
mM.
To optimise the system’s geometry before the simulation,
we performed energy minimisation using the steepest descent
algorithm for 5000 steps. Subsequently, we conducted equilibration in a canonical ensemble (NVT) for 200 ps with a 1 fs
time step. This was followed by equilibration in an isothermalisobaric thermodynamic ensemble (NPT) for 1 ns with a 2 fs
time step, employing the leap-frog integrator. The temperature
was maintained at 300 K using the Nosé-Hoover thermostat
with corrections applied every 1 ps (τT) for both the NVT and
NPT ensembles. During NPT equilibration, we maintained
the pressure at 1 bar using the isotropic Parrinello-Rahman
barostat with a τp value of 5 ps. Throughout the minimisation and equilibration stages, heavy atom positions were restrained using a harmonic potential with force constant of
1000 kJ/mol/nm2 . For all proteins density stabilisation was
observed by the end of the first 100 ps of NPT equilibration with average values of 1045 kJ/mol/nm2 . Subsequently,
heavy atom restraints were released for the NPT production
step, employing the same thermo- and barostat as for the NPT
equilibration. The final production molecular dynamics simulations were carried out in three replicates using a different
seed for the random starting velocities assigned from a Boltzman distribution. Each 100 ns replicate ran with a time step
of 2 fs and atomic coordinates were saved every 10 ps. Covalent bonds involving hydrogen atoms were constrained using
the LINCS algorithm in all the simulations. Long-range electrostatic interactions were managed using the Particle-Mesh
Ewald (PME) method.
These calculations were performed on the Juliot-Curie’s
Irene Rome supercomputer (TGCC/CEA), utilising dualprocessor compute nodes running at 2.6 GHz with 64 cores
per processor. The simulations generated 13.2 Terabytes of
raw data (.xtc and .trr files) for the 1522 protein chains in the
three datasets. In total, considering the three replicates, this
amounts to 456.6 μs of simulation time, encompassing 4566
trajectories of 100 ns, and corresponding to over one million
simulated amino acids.

Protein dynamics report and description
The obtained MD trajectories were subjected to various analyses to assess the overall behaviour of the protein and the local flexibility of its backbone. These analyses are presented on

interactive web pages with downloadable data, such as metrics calculated from MD data, information available in the
crystal structure as well as annotations from other biological
databases. The following parameters are reported:
Global protein behaviour:
• Root mean square deviation (RMSD) (in Å): The RMSD
measures the deviation of the protein structure from its
initial conformation. It is calculated on the backbone
atoms using GROMACS.
• Gyration radius (in Å): The gyration radius indicates
the compactness of the structure, computed with GROMACS along simulation.
• Contact map: The contact map shows the pairwise distances between the closest residue’s heavy atoms, computed with MDTraj (51) using a 4.5 Å threshold to define
contacts.
Local flexibility of protein backbone:
• Root mean square fluctuation (RMSF) (in Å): The RMSF
represents the standard deviation of atomic positions in
the trajectory. It is calculated on α-carbons using GROMACS.
• Phi and Psi angles (in ◦ ): The two main dihedral angles of
peptide bonds in the protein, Phi and Psi, are calculated
for each frame of the trajectory using MDTraj.
• Entropy-based index Neq: The Neq quantifies the average number of protein blocks (PBs) (52) at a given position in the sequence, reflecting the local deformability
of the backbone during the dynamics. It ranges from 1
to 16, indicating the number of observed PBs during the
dynamics (1: No PB variation, 16: Fully random PB distribution). The assignment of protein blocks is based on
Phi / Psi angles and processed with PBxplore (53).
• Secondary structure assignment: The DSSP assigns secondary structure elements into eight categories for each
frame of the trajectory, determined using MDTraj.
• Experimental B-factor extracted from initial PDB files
for α-carbons (in Å2 ): The B-factor reflects the attenuation of X-ray scattering due to thermal motion, capturing atom vibrations and static structural disorder.
To provide a comprehensive assessment of flexibility, additional information is included:
• Co-crystalised interactions: Residues interacting with cocrystallised protein chains, ligands, ions or nucleotides.
An interaction is defined by a distance between the αcarbon of the target residue and any heavy-atom of the
co-crystallised partner inferior to 6 Å.
• Protein domains: ECOD/SCOPe/CATH (37,54,55) domain assignments extracted from the downloadable version of the respective databases, as well as domains assigned using the local version of SWORD2 (56,57).
• Minimum TM-score between first and last conformation
among three replicates: A custom metric estimating the
deviation of the protein structure at the end of the trajectories from the starting conformation, calculated with
TM-align (58) (higher value indicates greater stability).
• Minimum TM-score between most divergent conformations: A custom metric evaluating the distance between
the most divergent conformations among the replicates,
calculated with TM-align (higher value indicates better
reproducibility).

D387

• AlphaFold2 predicted local distance difference test
(pLDDT): AlphaFold2 pLDDT, which is a per-residue
prediction confidence metric rather than a flexibility
measurement. Computed locally with AlphaFold2 Collab v1.5.1 (59).
• Other general properties extracted from the PDB or
UniProt such as organism or experimental resolution.

The calculations on the MD trajectory other than RMSD
and gyration radius, were conducted after truncating the first
100 ps of the dynamics. This truncation was implemented to
reduce the noise arising from the release of constraints at the
beginning of the simulation.

Results
Database content
In its current version, the main ATLAS dataset contains 1390
protein chains, enabling us to capture a wide range of protein
motions. Indeed, we provide MD trajectories for 1149 protein
domains with unique ECOD X-class (denoting possible homology). This covers 97 out of the 100 most common ECOD
domains and thus 91% of proteins with available ECOD ID.
Although it does not currently include all 2458 identified
folds in ECOD, the database contains every X-class ECOD
domain with available structure satisfying our stringent criteria. 1309 folds not featured in the database are either found
only in the membrane proteins or do not have any representative X-ray structure of high resolution in the current version
of the PDB.
From the point of view of structural diversity, we cover a
wide range of different folds from all-alpha to all-beta structures (Figure 1A) and protein sizes varying from 38 to 2128
residues (Figure S1A) and resolution from 0.72 to 2.0 Å (Figure S1B). The majority of proteins reported in ATLAS come
from bacteria or eukaryotes (Figure 1B). Nevertheless, the
database also contains proteins from archaea and viruses with
original folds. Coiled regions correspond on average to 40%
of protein residues per protein (Figure S1C). Finally, we report almost 6% of protein residues forming an interface with
other chains in the crystal structure, while 4%, 2% and less
than a percent of the residues were found in interaction with
a ligand, ion or nucleotide respectively (Figure 1C). For DPF
and chameleon protein regions this proportion increases significantly, therefore highlighting the role of intermolecular interaction in their stabilisation (Figure S2A, B).
Among simulated proteins, the majority demonstrates a
rather modest deviation from the initial conformation with
minimal TM-score between any frame of the trajectory and
starting conformation of around 0.8 (Figure S1E). Minimal
TM-score between starting and final conformation among
replicates is higher than 0.9 for 32% of proteins indicating
that conformational fluctuations during the simulation were
reversible (Figure S1D) and the majority of protein structures
tend to stabilise along the simulation (Figures S3 and S4).

Browse by structural domains
Users have an option to explore the ATLAS dataset by domains using the ECOD, SCOPe or CATH domain classifications. The Browse page presents collapsible trees for easy navigation.

Search in the database
Three methods can be used to search for a protein in the ATLAS database.
Search by features
This procedure enables users to filter the database using protein dynamics descriptors (such as average RMSF, average
Neq, conformational divergence during trajectories) as well as
general protein properties gathered from external databases
(e.g. domain classifications, UniProt/PDB annotations). The
results are presented in a user-friendly table format and can
be exported as a text file. An advanced search builder is also
provided, allowing users to create more complex filtering rules
(Figure 2A).
Search by sequence
The sequence search system allows users to query a protein sequence against the different databases to find similar proteins
using local-global, local-local, and global-global search methods, from fasta36 v36.3.8 software (60). The alignment results table displays clickable target IDs, percentage of identity,
alignment score, bit-score, and E-value of the matches with
an E-value lower than 10. Additionally, a graphical summary
of the alignment is provided for a quick overview of aligned
regions and alignment quality (Figure 2B).
Search by structure
With the structure search approach, users can query a protein structure to find similar folds in ATLAS database using
ProDy (61) to extract the requested protein chain and Kpax
5.1.3 (62) for structure alignment. They have the option to
search for entire proteins in the three databases or by ECOD
domains specifically present in the ATLAS dataset, useful for
querying multi-domain proteins. ‘Flexible alignment’ option is
available, allowing to flexibly superpose the target structure
over the rigid query structure to account for backbone fluctuations. The alignment results table includes clickable target
IDs, alignment length, RMSD, and TM-score of the top 10
best matches. Besides, a 3D structure viewer is provided to visualise the alignment between the query (displayed in white)
and the target (displayed in green) (Figure 2C).

Protein page
Page header
This section displays information from external databases and
programs, such as UniProt ID, secondary structure content,
and domain delineations. It also provides general parameters
computed from the molecular dynamics simulations, such as
average RMSF and the minimum TM-score between the start
and final conformations. Users can download trajectory data
as a .zip archive using the ‘Download’ buttons in reduced format with the corresponding analyses (1000 frames for each
replicate with solution molecules removed) and in complete
format (10 000 frames for each replicate) either with or without solvent (Figure 3A).
General properties
Here, users can obtain an overview of main protein properties averaged over the replicates. The section includes visualisations of secondary structures, protein domain delineations (ECOD, CATH, SCOPe and SWORD2), experimental B-factor values, flexibility profiles (RMSF and Neq) aver-

D388

Figure 1. ATLAS main database content in terms of different protein domains (A), native species (B) and contacts found in crystal structures (C).

aged over the three MD replicates, and AlphaFold2 Collab
pLDDT. Detailed values and positions in the sequence (the
author-specified numbering extracted from PDB and a sequential numbering that starts from 1) are accessible on mouse
hover. In addition, users can choose between min–max normalisation of flexibility profile from the protein only, for a
better view of the subtle variations, or min-max normalisation
of flexibility profile from the whole database (in log2 scale) to
compare flexibility profiles of different proteins (Figure 3B).
Replicates overview
In this section, detailed flexibility profiles (RMSF, B-factor,
Neq + pLDDT) and global analyses of protein conformational
mobility during the simulation (RMSD and gyration radius)
are provided. Users can view the diagrams for different replicates together or individually by clicking on the legend, and
zoom in on specific regions of interest through click-and-drag
functionality (Figure 3C).
Detailed analysis
To delve into the detected conformational changes, users can
visualise the structure and MD trajectory, contact maps, Ramachandran plots and DSSP plots of each replicate. In the 3D
viewers, protein can be coloured by sequence position or initial secondary structure. Flexibility visualisation is available
either on the structure, modifying both the colour and width
of the structure, or simply by visualising the trajectory itself
on the ‘Dynamics’ tab (Figure 3E). Besides, the animated contact map illustrates the formation and destruction of contacts
along the trajectory, and Ramachandran plots ensure coherent
conformations of most residues (Figure 3D).
In Supplementary Information, we provide detailed examples of ATLAS protein page analysis (section ‘Examples of the
protein page analysis’). We tackle the issue of inter-domain
hinges and analysis of co-crystallised partners effects on the

example of human HLA class 1 (Figures S5–S8) histocompatibility antigen as well as analyse dynamics of a Dual Personality Fragment located near the active site of hypoxanthineguanine phosphoribosyltransferase (Figures S9–S12).

Downloadable data
A Download page provides access to the GROMACS
molecular dynamics protocols (.mdp) and force field files
(CHARMM36m), the list of proteins composing different
datasets, as well as parsable content of the protein page annotations for a more advanced protein selection. This page is
also used to keep track of the database updates.

REST API
Database data can also be accessed programmatically using
the REST API documented in the ‘API’ tab. Users can download protein simulation data in the three possible formats
(‘analysis’, ‘protein’ and ‘total’), as well as protein page summary in .json format available for each entry. API also allows
the users to search for a protein in the datasets by sequence
and by structure (see ‘Search in the database’ for the details),
to download the MD parameters as well as to dump the latest
release of the parsable version of the database (see ‘Downloadable data’ section).

Discussion and perspectives
ATLAS database provides all-atom molecular dynamics simulations representative of the structural diversity of the PDB.
Standardised protocol for protein selection and MD simulations followed by a thorough analysis of the resulting trajectories provides a source of valuable and comparable information on protein dynamics at different scales. Indeed, in
their natural environment, proteins exhibit dynamic proper-

D389

Figure 2. Example of search outputs. (A) Search by features, (B) search by sequence and (C) search by structure.

ties potentially linked to interaction with various molecules,
and to their biological function under various conditions. Our
database captures possible scenarios of this inherent diversity,
providing information which is not directly available from Xray structures. Combination of the reported dynamics information with protein annotations and contacts reported in the
experimental data could help to deepen our understanding of
the protein sequence-structure-function relationships.
The main goal of ATLAS is to provide information on the
expected protein flexibility profile in solution and in absence
of other molecular interactions. While three replicates of 100
ns simulations offer valuable insights into dynamics properties
of proteins with a relatively stable structure, exploration of
rare events or major conformational rearrangements of large
proteins may require longer simulations. For now, the users
can easily extend protein MD simulations using the last or the
most divergent frames of the reported simulation as a starting
point for further conformational sampling. In the mediumterm perspective we will extend ATLAS database content both

in terms of the simulation time and in terms of protein content. ATLAS will continue to expand to encompass emerging
folds resolved in high-quality, as well as new representatives of
existing folds with divergent sequences. In particular, the developed protocol for the selection of the representative highquality protein structures will be regularly applied to the updated PDB content. Finally, the development of a unified MD
repository such as the upcoming European initiative MDDB
(https://mddbr.eu/) would be particularly beneficial for the expansion, sharing and the long-term sustainability of the ATLAS simulations.
The most interesting conclusions on protein dynamicfunction relationships often depend on modelling intermolecular interactions. For now, accurate MD modelling of proteinligand interactions requires extensive human expertise, incompatible with our automated and reproducible protocols,
due to both lack of the adapted force field parameters covering
chemical variability of different compounds and the problem
of correct identification of the biologically relevant interac-

D390

Figure 3. Example of protein page (PDB ID: 1k5n chain A). (A) Page header with annotations and downloadable data. (B) General residue-wise
characteristics. (C) Replicates overview (left: RMSD, right: Gyration radius). (D) Detailed analysis (left: animated contact map, right: Ramachandran
plot). (E) Examples of available structure visualisations in the Detailed analysis section (Replicate no. 1 – top: RMSF coloration, middle: Neq coloration,
bottom: visualisation of the MD trajectory coloured by initial secondary structure).

tions (63). Nevertheless, our first specialised Dual Personality
Fragment dataset has for purpose to shed light on conformational behaviour of the protein fragments particularly sensitive to ligand/partner removal. We will continue to expand
ATLAS by adding several specialised datasets of MD simulations for proteins of particular biological interest, such as
moonlight proteins. In the long-term perspective, such simulations will be completed by explicit MD simulations with
protein partners as well as its post-translational modifications
in order to explore their impact on protein dynamics, which is
still poorly described for today. These expansions will enhance
the diversity and scope of the ATLAS database, empowering

users to explore a broader range of protein dynamics and behaviours.

Data availability
The database website is freely available online without login
requirement at https://www.dsimb.inserm.fr/ATLAS.

Supplementary data
Supplementary Data are available at NAR Online.

Acknowledgements
The authors thank the Laboratoire d’Excellence GR-Ex, Paris,
France.

Funding
Ministry of Research (France); Université Paris Cité (France);
National Institute for Health and Medical Research (INSERM, France); IdEx [ANR-18-IDEX-0001]; French National Research Agency [ANR-21-CE45-0019]; all the production simulations were performed using high performance
computing (HPC) resources at CINES (Centre informatique national de l’enseignement supérieur) [A0090712053];
TGCC (Très Grand Centre de Calcul) [A0110712053,
A0140712053] funded by the GENCI (Grand Equipement
National de Calcul Intensif, France). Funding for open access
charge: INSERM and Université Paris Cité.

Conflict of interest statement
None declared.

References
1. Kokkinidis,M., Glykos,N.M. and Fadouloglou,V.E. (2012) Protein
flexibility and enzymatic catalysis. Adv. Protein Chem. Struct.
Biol., 87, 181–218.
2. Jubb,H., Blundell,T.L. and Ascher,D.B. (2015) Flexibility and small
pockets at protein-protein interfaces: new insights into
druggability. Prog. Biophys. Mol. Biol., 119, 2–9.
3. Teilum,K., Olsen,J.G. and Kragelund,B.B. (2009) Functional
aspects of protein flexibility. Cell. Mol. Life Sci. CMLS, 66,
2231–2247.
4. Carugo,O. (2018) How large B-factors can be in protein crystal
structures. BMC Bioinf., 19, 61.
5. Carugo,O. (2019) Maximal B-factors in protein crystal structures.
Z. Für Krist. - Cryst. Mater., 234, 73–77.
6. Carugo,O. (2021) How anisotropic and isotropic atomic
displacement parameters monitor protein covalent bonds rigidity:
isotropic B-factors underestimate bond rigidity. Amino Acids, 53,
779–782.
7. Carugo,O. (2022) B-factor accuracy in protein crystal structures.
Acta Crystallogr. Sect. Struct. Biol., 78, 69–74.
8. Jumper,J., Evans,R., Pritzel,A., Green,T., Figurnov,M.,
Ronneberger,O., Tunyasuvunakool,K., Bates,R., Žídek,A.,
Potapenko,A., et al. (2021) Highly accurate protein structure
prediction with AlphaFold. Nature, 596, 583–589.
9. Vander Meersche,Y., Cretin,G., de Brevern,A.G., Gelly,J.-C. and
Galochkina,T. (2021) MEDUSA: prediction of Protein Flexibility
from Sequence. J. Mol. Biol., 433, 166882.
10. Marchetti,F., Moroni,E., Pandini,A. and Colombo,G. (2021)
Machine learning prediction of allosteric drug activity from
molecular dynamics. J. Phys. Chem. Lett., 12, 3724–3732.
11. Hansson,T., Oostenbrink,C. and van Gunsteren,W. (2002)
Molecular dynamics simulations. Curr. Opin. Struct. Biol., 12,
190–196.
12. Collier,T.A., Piggot,T.J. and Allison,J.R. (2020) Molecular
dynamics simulation of proteins. Methods Mol. Biol. Clifton NJ,
2073, 311–327.
13. Karplus,M. and Petsko,G.A. (1990) Molecular dynamics
simulations in biology. Nature, 347, 631–639.
14. Lindorff-Larsen,K., Piana,S., Dror,R.O. and Shaw,D.E. (2011)
How fast-folding proteins fold. Science, 334, 517–520.
15. Gheeraert,A., Pacini,L., Batista,V.S., Vuillon,L., Lesieur,C. and
Rivalta,I. (2019) Exploring allosteric pathways of a V-type enzyme

D391
with dynamical perturbation networks. J. Phys. Chem. B, 123,
3452–3461.
16. Saltalamacchia,A., Casalino,L., Borišek,J., Batista,V.S., Rivalta,I.
and Magistrato,A. (2020) Decrypting the information exchange
pathways across the spliceosome machinery. J. Am. Chem. Soc.,
142, 8403–8411.
17. Santos,L.H.S., Ferreira,R.S. and Caffarena,E.R. (2019) Integrating
molecular docking and molecular dynamics simulations. Methods
Mol. Biol., 2053, 13–34.
18. Watanabe,Y., Fukuyoshi,S., Kato,K., Hiratsuka,M., Yamaotsu,N.,
Hirono,S., Gouda,H. and Oda,A. (2017) Investigation of substrate
recognition for cytochrome P450 1A2 mediated by water
molecules using docking and molecular dynamics simulations. J.
Mol. Graph. Model., 74, 326–336.
19. Terefe,E.M. and Ghosh,A. (2022) Molecular docking, validation,
dynamics simulations, and pharmacokinetic prediction of
phytochemicals isolated from Croton dichogamus against the
HIV-1 reverse transcriptase. Bioinforma. Biol. Insights, 16,
11779322221125604.
20. Tian,S., Sun,H., Pan,P., Li,D., Zhen,X., Li,Y. and Hou,T. (2014)
Assessing an ensemble docking-based virtual screening strategy for
kinase targets by considering protein flexibility. J. Chem. Inf.
Model., 54, 2664–2679.
21. Wang,B., Buchman,C.D., Li,L., Hurley,T.D. and Meroueh,S.O.
(2014) Enrichment of chemical libraries docked to protein
conformational ensembles and application to aldehyde
dehydrogenase 2. J. Chem. Inf. Model., 54, 2105–2116.
22. Eyrisch,S. and Helms,V. (2007) Transient pockets on protein
surfaces involved in protein-protein interaction. J. Med. Chem., 50,
3457–3464.
23. Fornili,A., Pandini,A., Lu,H.-C. and Fraternali,F. (2013)
Specialized dynamical properties of promiscuous residues revealed
by simulated conformational ensembles. J. Chem. Theory
Comput., 9, 5127–5147.
24. Rivalta,I., Sultan,M.M., Lee,N.-S., Manley,G.A., Loria,J.P. and
Batista,V.S. (2012) Allosteric pathways in imidazole glycerol
phosphate synthase. Proc. Natl. Acad. Sci. U.S.A., 109,
E1428–E1436.
25. Rivalta,I., Lisi,G.P., Snoeberger,N.-S., Manley,G., Loria,J.P. and
Batista,V.S. (2016) Allosteric communication disrupted by a small
molecule binding to the imidazole glycerol phosphate synthase
protein–protein interface. Biochemistry, 55, 6484–6494.
26. Wurm,J.P., Sung,S., Kneuttinger,A.C., Hupfeld,E., Sterner,R.,
Wilmanns,M. and Sprangers,R. (2021) Molecular basis for the
allosteric activation mechanism of the heterodimeric imidazole
glycerol phosphate synthase complex. Nat. Commun., 12, 2748.
27. Klepeis,J.L., Lindorff-Larsen,K., Dror,R.O. and Shaw,D.E. (2009)
Long-timescale molecular dynamics simulations of protein
structure and function. Curr. Opin. Struct. Biol., 19, 120–127.
28. Ayaz,P., Lyczek,A., Paung,Y., Mingione,V.R., Iacob,R.E., de
Waal,P.W., Engen,J.R., Seeliger,M.A., Shan,Y. and Shaw,D.E.
(2023) Structural mechanism of a drug-binding process involving
a large conformational change of the protein target. Nat.
Commun., 14, 1885.
29. Newport,T.D., Sansom,M.S.P. and Stansfeld,P.J. (2019) The
MemProtMD database: a resource for membrane-embedded
protein structures and their lipid interactions. Nucleic. Acids. Res.,
47, D390–D397.
30. Rodríguez-Espigares,I., Torrens-Fontanals,M., Tiemann,J.K.S.,
Aranda-García,D., Ramírez-Anguita,J.M., Stepniewski,T.M.,
Worp,N., Varela-Rial,A., Morales-Pastor,A., Medel-Lacruz,B.,
et al. (2020) GPCRmd uncovers the dynamics of the
3D-GPCRome. Nat. Methods, 17, 777–787.
31. Torrens-Fontanals,M., Peralta-García,A., Talarico,C.,
Guixà-González,R., Giorgino,T. and Selent,J. (2022) SCoV2-MD:
a database for the dynamics of the SARS-CoV-2 proteome and
variant impact predictions. Nucleic. Acids. Res., 50, D858–D866.
32. Meyer,T., D’Abramo,M., Hospital,A., Rueda,M., Ferrer-Costa,C.,
Pérez,A., Carrillo,O., Camps,J., Fenollosa,C., Repchevsky,D., et al.

D392
(2010) MoDEL (Molecular Dynamics Extended Library): a
database of atomistic molecular dynamics trajectories. Struct.
Lond. Engl., 18, 1399–1409.
33. van der Kamp,M.W., Schaeffer,R.D., Jonsson,A.L., Scouras,A.D.,
Simms,A.M., Toofanny,R.D., Benson,N.C., Anderson,P.C.,
Merkley,E.D., Rysavy,S., et al. (2010) Dynameomics: a
comprehensive database of protein dynamics. Struct. Lond. Engl.,
18, 423–435.
34. Berman,H.M., Westbrook,J., Feng,Z., Gilliland,G., Bhat,T.N.,
Weissig,H., Shindyalov,I.N. and Bourne,P.E. (2000) The Protein
Data Bank. Nucleic Acids Res., 28, 235–242.
35. Zhang,Y., Stec,B. and Godzik,A. (2007) Between order and
disorder in protein structures: analysis of ‘dual personality’
fragments in proteins. Struct. Lond. Engl., 15, 1141–1147.
36. Li,W., Kinch,L.N., Karplus,P.A. and Grishin,N.V. (2015) ChSeq: a
database of chameleon sequences. Protein Sci. Publ. Protein Soc.,
24, 1075–1086.
37. Schaeffer,R.D., Liao,Y., Cheng,H. and Grishin,N.V. (2017) ECOD:
new developments in the evolutionary classification of domains.
Nucleic Acids Res., 45, D296–D302.
38. Hintze,B.J., Lewis,S.M., Richardson,J.S. and Richardson,D.C.
(2016) MolProbity’s ultimate rotamer-library distributions for
model validation. Proteins, 84, 1177–1189.
39. Lomize,M.A., Lomize,A.L., Pogozheva,I.D. and Mosberg,H.I.
(2006) OPM: orientations of proteins in membranes database.
Bioinforma, 22, 623–625.
40. Kozma,D., Simon,I. and Tusnády,G.E. (2013) PDBTM: protein
Data Bank of transmembrane proteins after 8 years. Nucleic Acids
Res., 41, D524–D529.
41. Bittrich,S., Rose,Y., Segura,J., Lowe,R., Westbrook,J.D.,
Duarte,J.M. and Burley,S.K. (2022) RCSB Protein Data Bank:
improved annotation, search and visualization of membrane
protein structures archived in the PDB. Bioinforma, 38,
1452–1454.
42. Williams,C.J., Richardson,D.C. and Richardson,J.S. (2022) The
importance of residue-level filtering and the Top2018 best-parts
dataset of high-quality protein residues. Protein Sci. Publ. Protein
Soc., 31, 290–300.
43. Krissinel,E. and Henrick,K. (2007) Inference of macromolecular
assemblies from crystalline state. J. Mol. Biol., 372, 774–797.
44. Steinegger,M. and Söding,J. (2017) MMseqs2 enables sensitive
protein sequence searching for the analysis of massive data sets.
Nat. Biotechnol., 35, 1026–1028.
45. Touw,W.G., Baakman,C., Black,J., te Beek,T.A.H., Krieger,E.,
Joosten,R.P. and Vriend,G. (2015) A series of PDB-related
databanks for everyday needs. Nucleic. Acids. Res., 43,
D364–D368.
46. Webb,B. and Sali,A. (2016) Comparative Protein Structure
Modeling Using MODELLER. Curr. Protoc. Bioinforma., 54,
5.6.1–5.6.37.
47. Fiser,A., Do,R.K. and Sali,A. (2000) Modeling of loops in protein
structures. Protein Sci. Publ. Protein Soc., 9, 1753–1773.
48. Abraham,M.J., Murtola,T., Schulz,R., Páll,S., Smith,J.C., Hess,B.
and Lindahl,E. (2015) GROMACS: high performance molecular

simulations through multi-level parallelism from laptops to
supercomputers. SoftwareX, 1–2, 19–25.
49. Huang,J., Rauscher,S., Nawrocki,G., Ran,T., Feig,M., de
Groot,B.L., Grubmüller,H. and MacKerell,A.D. (2017)
CHARMM36m: an improved force field for folded and
intrinsically disordered proteins. Nat. Methods, 14, 71–73.
50. Hollingsworth,S.A. and Dror,R.O. (2018) Molecular Dynamics
Simulation for All. Neuron, 99, 1129–1143.
51. McGibbon,R.T., Beauchamp,K.A., Harrigan,M.P., Klein,C.,
Swails,J.M., Hernández,C.X., Schwantes,C.R., Wang,L.-P.,
Lane,T.J. and Pande,V.S. (2015) MDTraj: a modern open library
for the analysis of molecular dynamics trajectories. Biophys. J.,
109, 1528–1532.
52. de Brevern,A.G., Etchebest,C. and Hazout,S. (2000) Bayesian
probabilistic approach for predicting backbone structures in terms
of protein blocks. Proteins, 41, 271–287.
53. Barnoud,J., Santuz,H., Craveur,P., Joseph,A.P., Jallu,V., de
Brevern,A.G. and Poulain,P. (2017) PBxplore: a tool to analyze
local protein structure and deformability with Protein Blocks.
PeerJ, 5, e4013.
54. Fox,N.K., Brenner,S.E. and Chandonia,J.-M. (2014) SCOPe:
structural classification of proteins–extended, integrating SCOP
and ASTRAL data and classification of new structures. Nucleic
Acids Res., 42, D304–D309.
55. Sillitoe,I., Bordin,N., Dawson,N., Waman,V.P., Ashford,P.,
Scholes,H.M., Pang,C.S.M., Woodridge,L., Rauer,C., Sen,N., et al.
(2021) CATH: increased structural coverage of functional space.
Nucleic Acids Res., 49, D266–D273.
56. Postic,G., Ghouzam,Y., Chebrek,R. and Gelly,J.-C. (2017) An
ambiguity principle for assigning protein structural domains. Sci.
Adv., 3, e1600552.
57. Cretin,G., Galochkina,T., Vander Meersche,Y., de Brevern,A.G.,
Postic,G. and Gelly,J.-C. (2022) SWORD2: hierarchical analysis of
protein 3D structures. Nucleic Acids Res., 50, W732–W738.
58. Zhang,Y. and Skolnick,J. (2005) TM-align: a protein structure
alignment algorithm based on the TM-score. Nucleic Acids Res.,
33, 2302–2309.
59. Mirdita,M., Schütze,K., Moriwaki,Y., Heo,L., Ovchinnikov,S. and
Steinegger,M. (2022) ColabFold: making protein folding accessible
to all. Nat. Methods, 19, 679–682.
60. Pearson,W.R. and Lipman,D.J. (1988) Improved tools for
biological sequence comparison. Proc. Natl. Acad. Sci. U.S.A., 85,
2444–2448.
61. Zhang,S., Krieger,J.M., Zhang,Y., Kaya,C., Kaynak,B.,
Mikulska-Ruminska,K., Doruker,P., Li,H. and Bahar,I. (2021)
ProDy 2.0: increased scale and scope after 10 years of protein
dynamics modelling with Python. Bioinforma., 37, 3657–3659.
62. Ritchie,D.W. (2016) Calculating and scoring high quality multiple
flexible protein structure alignments. Bioinforma, 32, 2650–2658.
63. Zhang,C., Zhang,X., Freddolino,P.L. and Zhang,Y. (2023)
BioLiP2: an updated structure database for biologically relevant
ligand-protein interactions. NucleicAcids Res.,
https://doi.org/10.1093/nar/gkad630.

Received: August 11, 2023. Revised: October 15, 2023. Editorial Decision: October 25, 2023. Accepted: October 30, 2023
© The Author(s) 2023. Published by Oxford University Press on behalf of Nucleic Acids Research.
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse,
distribution, and reproduction in any medium, provided the original work is properly cited.


---

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


---

# MISATO: machine learning dataset of protein–ligand complexes for structure-based drug discovery

**Authors:** Till Siebenmorgen, Filipe Menezes, Sabrina Benassou, Erinc Merdivan, Kieran Didi, André Santos Dias Mourão, Radosław Kitel, Pietro Liò, Stefan Kesselheim, Marie Piraud, Fabian J. Theis, Michael Sattler, Grzegorz M. Popowicz
**Year:** 2024
**Venue:** Nature Computational Science
**DOI:** 10.1038/s43588-024-00627-2
**Source PDF URL:** https://push-zb.helmholtz-munich.de/deliver.php?id=36052 (Helmholtz Munich publication server, hybrid OA copy)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

nature computational science

MISATO: machine learning dataset
of protein–ligand complexes for
structure-based drug discovery
Received: 30 May 2023
Accepted: 11 April 2024
Published online: 10 May 2024

Till Siebenmorgen 1,2,9, Filipe Menezes 1,2,9, Sabrina Benassou3,
Erinc Merdivan4, Kieran Didi 5, André Santos Dias Mourão1,2, Radosław Kitel6,
Pietro Liò5, Stefan Kesselheim 3, Marie Piraud4, Fabian J. Theis 4,7,8,
Michael Sattler 1,2 & Grzegorz M. Popowicz 1,2

Check for updates

Large language models have greatly enhanced our ability to understand
biology and chemistry, yet robust methods for structure-based drug
discovery, quantum chemistry and structural biology are still sparse.
Precise biomolecule–ligand interaction datasets are urgently needed
for large language models. To address this, we present MISATO, a dataset
that combines quantum mechanical properties of small molecules and
associated molecular dynamics simulations of ~20,000 experimental
protein–ligand complexes with extensive validation of experimental
data. Starting from the existing experimental structures, semi-empirical
quantum mechanics was used to systematically refine these structures.
A large collection of molecular dynamics traces of protein–ligand complexes
in explicit water is included, accumulating over 170 μs. We give examples
of machine learning (ML) baseline models proving an improvement of
accuracy by employing our data. An easy entry point for ML experts
is provided to enable the next generation of drug discovery artificial
intelligence models.

In recent years, artificial intelligence (AI) predictions have revolutionized many fields of science. In structural biology, AlphaFold2 (ref. 1)
predicts accurate protein structures from amino-acid sequences only.
Its accuracy nears state-of-the-art experimental data. The success of
AlphaFold2 is made possible due to a rich database of nearly 200,000
protein structures that have been deposited and are available in the
Protein Data Bank (PDB)2. These structures were determined over the
past decades using X-ray crystallography, nuclear magnetic resonance
(NMR) or cryo-electron microscopy. Despite enormous investments,

there are still few new drugs approved yearly, with development costs
reaching several billion dollars3. An ongoing grand challenge is rational,
structure-based drug discovery (DD). Compared with protein structure
prediction, this task is substantially more difficult.
In the early stages of DD, structure-based methods are popular
and efficient approaches. The biomolecule provides the starting point
for rational ligand search. Later, it guides optimization to optimally
explore the chemical combinatorial space4 while still ensuring druglike properties. In silico methods that are in principle able to tackle

Molecular Targets and Therapeutics Center, Institute of Structural Biology, Helmholtz Munich, Neuherberg, Germany. 2TUM School of Natural
Sciences, Department of Bioscience, Bayerisches NMR Zentrum, Technical University of Munich, Garching, Germany. 3Jülich Supercomputing Centre,
Forschungszentrum Jülich, Jülich, Germany. 4Helmholtz AI, Helmholtz Munich, Neuherberg, Germany. 5Computer Laboratory, Cambridge University,
Cambridge, UK. 6Faculty of Chemistry, Jagiellonian University, Krakow, Poland. 7Computational Health Center, Institute of Computational Biology,
Helmholtz Munich, Neuherberg, Germany. 8TUM School of Computation, Information and Technology, Technical University of Munich, Garching,
Germany. 9These authors contributed equally: Till Siebenmorgen, Filipe Menezes.
e-mail: grzegorz.popowicz@helmholtz-munich.de

a

b

Csp3
N+
Car
Car

Csp3

Nar

Semi-empirical
QM

FF MD
simulations

Automated QM
methods

PDB preparation

Calculation of QM
properties

Ligand
parametrization
Solvation and
heating

Csp3

Nar

Car

PDB structures
19,443

MD simulation

Csp3
Csp3

Car
N?

Calculation of
properties

Csp3

MISATO dataset
Data loaders
AI base line
models

Fig. 1 | MISATO combines QM data with MD-derived protein–ligand
dynamics. a, We provide a dataset that combines semi-empirical QM properties
of small molecules with MD-simulated dynamics of the entire set of experimental
protein–ligand complexes. All common errors in protein and ligand

nomenclature, protonation, geometry and so on are fixed. The blue outline of
the molecule describes its electronic density. b, An overview of the dataset and
the applied protocols for semi-empirical QM and FF (force field) MD simulations
including data preparation, preprocessing and AI baseline models.

structure-based DD include semi-empirical quantum mechanical (QM)
methods5, molecular dynamics (MD) simulations6,7, docking8 and
coarse-grained simulations9, which can also be combined to be more
efficient. However, these methods either suffer from generally low
precision or are computationally too expensive while still requiring
substantial experimental validation. Recent examples show that classical, ball-and-stick atomistic model representations of biomolecular
structures might be too inaccurate in certain situations to allow for
correct predictions10–13.
The introduction of AI into the process is still at an early stage.
AI approaches are, in principle, able to learn the fundamental state
variables that describe experimental data14. Thus, they are likely to
abstract from electronic and force field-based descriptions of the
protein–ligand complex. However, so far mostly simple solutions
have been proposed that do not incorporate the available protein–
ligand data to their full extent, such as scoring protein–ligand Gibbs
free energies15,16, ADME (absorption, distribution, metabolism and
excretion) property estimation17 or prediction of synthetic routes18,19.
Most of these approaches are constructed using one-dimensional
SMILES (simplified molecular-input line-entry system)20,21 and only
a few attempts have been made to properly tackle three-dimensional
(3D) biomolecule–ligand data22–24.
Several databases are available that contain raw experimental
structures of protein–ligand complexes, usually extracted from the
PDB (for example, PDBbind25, bindingDB26, Binding MOAD27, Sperrylite28). Only recently a database of MD-derived traces of protein–
ligand structures was reported29,30. Despite these efforts, so far no AI
model has been proposed that convincingly addresses the rational DD
challenge in the way that AlphaFold2 answered the protein structure
prediction problem31,32.
In addition to DD, the structure-based AI models are useful for
biomolecule structure analysis and quantum chemistry. However,
they are severely hindered by several factors: neglecting the conformational flexibility (dynamics and induced fit upon binding); entropic
considerations; inaccuracies in the deposited structural data (incorrect
atom types due to missing hydrogen atoms, incorrect evaluation of
functional group flexibility, inconsistent geometry restraints, fitting
errors); chemical complexity (for example, non-obvious protonation

states); overly simplified atomic properties; highly complex energy
landscapes in molecular recognition by their targets. Attempts to
train AI models currently require inferring this missing information
implicitly. The limited number of publicly available protein–ligand
structures (~20,000) and lack of thermodynamic data cause this inference to fail. This is preventing structure-based models from producing
groundbreaking results31,32.
Here, we propose a protein–ligand structural database, MISATO
(molecular interactions are structurally optimized) that is based on
experimental protein–ligand structures. We show that the database
helps to better train models across fields related to DD and beyond.
This includes quantum chemistry, general structural biology and bioinformatics. We provide quantum-chemical-based structural curation
and refinement, including regularization of the ligand geometry. We
augment this database with missing dynamic and chemical information, including MD on a timescale allowing the detection of transient
and cryptic states for certain systems. The latter are very important for
successful drug design33. Thus, we supplement experimental data with
the maximum number of physical parameters. This eases the burden
on AI models to implicitly learn all this information, allowing focus on
the main learning task. The MISATO database provides a user-friendly
format that can be directly imported into machine learning (ML) codes.
We also provide various preprocessing scripts to filter and visualize the
dataset. Example AI baseline models are supplied for the calculation of
quantum chemical properties (chemical hardness and electron affinity),
for binding affinity calculation and for the prediction of protein
flexibility or induced-fit features to simplify adoption. The QM, MD
and AI baseline models are validated extensively on experimental data.
We wish to transform MISATO into an ambitious community project
with vast implications for the whole field of DD.

Results

MISATO dataset
The basis for MISATO (Fig. 1) is the 19,443 protein–ligand structures
from PDBbind25. These structures were experimentally determined
over the past decades and represent a diverse set of protein–ligand
complexes for which experimental affinities are available. In the context
of AI for DD it is of utmost importance to train the models on a dataset

a

b

Natoms
20.2%
add
Natoms

73.2%

26.9%

26.8%
add
Nhydrogen

73.1%

F
Cl
Br
I

Polarizability a03

rem
Nhydrogen

c

Halogen

1WUG
1.4Å

1.4Å

rem
Natoms

4MDN

20.1%

–0.8

–0.6

–0.4

–0.2

0.2

0.4

Charge

Nprotons

d

e
–0.49
6.4

–0.03
7.0

–0.19
7.4

–0.31
5.9

–0.19
15.7

5GTR

+
–0.39
6.2

+
+

Fig. 2 | Changes applied to the PDBbind database based on our quantum
chemical protocol. a, Statistical overview of changes introduced by our
optimization protocol. Natoms corresponds to total changes in the atom count
when compared with the source database. In most cases atoms were removed
add
Nrem
atoms); in only 27% of cases was the number of atoms increased, Natoms. Similar
considerations apply to protons—light blue; Nprotons. b, D4 polarizability versus
partial charge for all the halogens in the database. The outliers were analyzed to
find possible wrong atom assignments. This was the case for the bromine atom in
the lower right corner, which in reality is a boron. c, Examples of inconsistent

structures: 1WUG contains overly elongated NO bonds; 4MDN contains a
nitrogen in angular violation of VSEPR; 5GTR shows a typical problem in the
protonation state. d,e, Calculated electronic density for ketamine (4G8H) and
tramadol, respectively (dashed green lines). Dashed circles show the sizes of
electronic density around selected atoms. The numbers next to these atoms
represent partial charge (top) and atomic polarizability (bottom). These are
electronic descriptors representing the electronic density around each center.
Color and character keys: N, blue, nitrogen; S, yellow, sulfur; O, red, oxygen;
C, beige, carbon; H, white, hydrogen; Cl, green, chlorine.

with the highest possible correctness and consistency, for several reasons. First, the total number of available structures is much lower than
typical training sizes of other AI targets. Second, ligand association
has a rather complex energy landscape during molecular recognition. Delicate deviations in the protein–ligand structures or atomic
parameters can markedly impair binding. In the PDB, incorrect atom
assignments and inconsistent geometries are not uncommon. More
seriously, hydrogen atoms are highly sensitive to their chemical and
molecular environment and are rarely experimentally accessible. All
these issues have been systematically addressed in our work and are
compiled in our database (Figs. 2 and 3).

associated with the software used for processing the molecular geometries. As well as the absence of hydrogen atoms in crystallographic
structures, resolution affects the heteroatom geometry. Contracted
or elongated bonds are common (Fig. 2). That is, most nitro groups we
examined were heavily distorted: in the 1WUG structure34, NO bonds
are almost 17% larger than reference experimental data35. Another
example is seen in the 4MDN structure36, where an amide was so distorted that it explicitly violated VSEPR (valence shell electron pair
repulsion) theory. Reinspection of the experimental electronic density
hinted that the CÔC angle in the 4-chlorobenzyl phenyl ether moiety
is also larger by almost 20° against anisole, a reference compound for
that bond angle35. Simultaneous relaxation of the two groups leads to
substantial improvement, in particular an amide group very close to
reference structural values. Such errors in the heteroatom skeleton
propagate further when assigning and counting hydrogen atoms. In
the 5GTR structure37, a guanidino group strongly deviates from the
expected planarity. The immediate consequences are incorrect atomic
hybridizations and overassignment of hydrogen atoms, with a local
formal charge of +3 in a radius of one bond around the central carbon.
More examples are described in Supplementary Information.

Typical limitations in structural datasets
Understanding the nature and sources of errors in structural databases
is imperative for improving the quality of the underlying molecular
models.
Macromolecule–ligand interaction strength, the most desired
baseline parameter for DD, is unfortunately also the most inaccurate
metric. The diverse experimental set-ups from experimental entropy/
enthalpy determination (for example, isothermal titration calorimetry)
to cellular phenotypic response are given as ligand strength. These
values are not comparable and their use to train AI models is generally
unreliable. To enable validation of affinity prediction we have prepared
a small subset of ligands with accurately determined affinities to be
used as a benchmark (Supplementary Table 1). We also tested our
example model against it.
As MISATO is founded on experimental data, the two main sources
of structural inaccuracies must be corrected. These are limited spatial
resolution of the experimental structures and problems and biases

Evaluation of the QM-based ligand curation
Employing the protocol defined in Supplementary Section 6 we modified a total of 3,930 structures, which corresponds roughly to 20% of the
original database that needed substantial refinement (Fig. 2). Of these,
3,905 cases involve changes in protonation states, while changes in
heteroatoms involve 97 ligands. These are predominantly the addition
of model functional groups to emulate covalent binding with the protein (20) or the addition of missing hydroxyl groups to boronic acids.

a

b

c

d

e
Ligand

Pocket

Fig. 3 | Overview of events captured by the MD simulations in the binding
pocket. a–c, Reversible opening and closing of the binding pocket can be
captured during the simulations, including cryptic binding sites. a, The structure
of 2AM4 is shown after 2 ns (left panel), 6 ns (middle panel) and 10 ns (right panel)
simulation time (fluorine in beige). b,c, The opening loop region (b, structure
2LKK) is visualized for superimposed timesteps (blue diagram, dark hue, 2 ns;
black diagram, medium dark hue, 6 ns; red diagram, light hue, 10 ns). The protein
pocket opens in structure 8ABP during the simulation (c). d, Protein residues at
the binding site can undergo large adaptations within the simulations, indicating

unstable interactions or possible switches. This is shown for a methionine residue
of 4ZYZ (upper panel) and a tryptophan residue of 1WAW (lower panel). Coloring
as in b after 2 ns and 10 ns. e, MD simulations captured local adaptability of the
binding pocket and ligand. That is, in structure 2IG0 parts of the ligand (licorice,
carbons in ivory) are quite flexible in the protein pocket (gray carbons) when
comparing the first (dark hue) and the last (light hue) frames of the MD run. Color
and character keys, if not indicated differently: N, blue, nitrogen; S, yellow, sulfur;
O, red, oxygen; C, black, carbon; H, white, hydrogen; F, beige, fluorine; P, orange,
phosphorus.

Some ligands were split into several molecules as the original
structures were not binary protein–ligand complexes (one ligand):
1A0T, 1G42, 1G9D, 2L65, 3D4F and 4MNV. 1E55 is supposed to be a
mixture of two entities. However, the closest contact between them
is insufficient to consider them separately, but also too large for a
covalent interaction. Similar considerations apply to 1F4Y, though here
close intramolecular contacts are at stake. In 4AW8 we observed a substantial deformation for the published ligand, PG6. We observed that
the reference affinity is related to the metal ion in the system, Zn(ii),
and not to PG6. The structure was consequently excluded.
As depicted in Fig. 2, the most common adjustment was the
removal of hydrogen atoms from the initial PDBbind geometry. This
amounts to almost 75% of the modifications. It has been pointed out
that libraries such as PDBbind possess biased datasets in terms of
binding configurations31.

chemical hardness, electronegativity, ionization potentials (by definition and using Koopmans’ theorem), static log P and polarizabilities.
The latter were obtained in vacuum, water and wet octanol. Atomic
properties include partial charges from different models, atomic
polarizabilities, bond orders, atomic hybridizations, orbital- and
charge-based reactivity (Fukui) indices and atomic softness. Reactivity
indices and atomic softness are derived for interactions with electrophiles, nucleophiles and radicals. Finally, we also provide tight-binding
electronic densities for all ligands. Partial charges were calculated at
several levels, as these are somewhat method-sensitive quantities. AM1
charges are usually the starting point for charge-correcting schemes
to be used in MD simulations. This is the case for AM1-BCC38. Taking
our AM1 charges and multiplying them by 1.14 (in the case of neutral
molecules) yields 1.14*CM1A-LBCC charges39 used in OPLS-AA simulations40. The main advantage of the charges we provide is that these were
obtained, when required, with a HOMO (highest occupied molecular
orbital)–LUMO (lowest unoccupied molecular orbital) level shift to
ensure convergence to sensible electronic states. Beyond MD simulations, CMx charges41–43 have also been shown to provide good estimates

QM-derived properties
We calculated several molecular and atomic properties for the ligands
(Supplementary Table 2). For the former, we include electron affinities,

QM H5 file

MD H5 file

Atom_names
Bonds
Atom_properties_
names

Atom_element
Atom_properties

10GS

Mol_properties

11GS

Atom_properties_
values

13GS

Atom_number

Atoms_residue

Atom_type

Total_charge
Frames_bSASA
....

Electron_affinity

Frames_distance

Electronegativity
Hardness

9ICD

Ionization_potential
9HVP
Koopman

Frames_
interaction_energy
Frames_
rmsd_ligand
Molecule_begin_
atom_index

Molecular_weight

Trajectory_
coordinates

Polarizability

Molecule property names

Molecule properties

PDBIDs

Molecule properties

Fig. 4 | Data hierarchy of the QM and MD files. The QM data can be accessed via
the PDB ID. The properties are split by atom properties and molecular properties.
Examples of the calculated molecular properties are given. The electronic

densities are provided in a separate file. The MD data are also subdivided by PDB
ID. The properties are calculated either for all atoms, for each timestep (frame),
or for the whole trajectory, as indicated by the name.

of molecular dipole moments, just like tight-binding Mulliken charges44.
From the latter, we infer furthermore the reasonableness of the electronic densities provided.

generalized Born surface area (MMGBSA) scoring (no entropic contributions explicitly considered)45. Moreover, the buried solvent accessible surface area was obtained for the complex. Calculated properties
are stable over the simulations, proving them well equilibrated (Supplementary Fig. 1). For some systems, larger rearrangements of the
binding site were captured that in extreme cases led to an opening of
the whole binding pocket (Fig. 3). These rare events indicate possible
cryptic pockets or transient binding modes. In a small fraction of cases,
dissociation was detected (details given in Supplementary Fig. 2).

MD simulations
Experimental structural data are static snapshots that are assumed
to represent a thermodynamic most stable state trapped in a crystal
but ignore the presence of conformational dynamics. Experimental
description of dynamics in biological macromolecules from nanosecond to millisecond timescales is challenging and requires a combination of different spectroscopic techniques. NMR spectroscopy and
fluorescence-based methods can provide relevant information but are
time consuming, and so far the dynamic information is not well captured in public databases. MD simulations can be performed, starting
from experimental structures, and letting them evolve in time using a
force field that describes the molecular potential energy surface. Typically, periods of nanoseconds to microseconds can be achieved for individual systems, depending on system size. MD traces allow the analysis
of small-range structural fluctuations of the protein–ligand complex,
but in some cases large-scale rare events can be observed (Fig. 3). In
existing DD software these events are mostly neglected. MD simulations
of 16,972 protein–ligand complexes in explicit water were performed
for 10 ns. Structures were disregarded whenever non-standard ligand
atoms or inconsistencies in the protein starting structures were encountered. A variety of metadata were generated from the simulations to
facilitate future AI learning (Fig. 4, Supplementary Table 2 and Supplementary Fig. 1). RMSDLigand (root-mean-square deviation of the ligand
after alignment of the protein) and the root-mean-square deviation of
the whole complex were calculated with respect to the native structure.
Also, binding affinities were estimated using molecular mechanics

AI models
To exemplify possible applications of our dataset, baseline AI models
were trained and evaluated. These are included in the repository as a
template for future community development. For the QM dataset, the
electron affinity and the chemical hardness of the ligand molecules
were predicted (Fig. 5). The Pearson correlation is 0.75 for electron
affinity and 0.77 for chemical hardness. The mean absolute error shows
close predictions to the target values: on average 0.12 eV for electron
affinity and 0.13 eV for chemical hardness. For these two exemplary
QM features, high accuracy was achieved, opening a route to a fast
derivation of QM properties. This is particularly important for larger
molecules, where long calculation times are frequent.
For the MD traces, the induced-fit capability of the protein (adaptability) was predicted (see Methods for an exact definition). The model
was able to identify elements of biomolecule structure likely to adapt
to ligand binding. We achieved a mean Pearson correlation of 0.66.
On average 42 of the top 100 atoms were correctly predicted (Fig. 5).
As shown in Fig. 5d, the model can predict the atoms in the protein
pocket that are mostly flexible during the MD run (large spheres), and
detect the more rigid protein regions (small spheres). This allows a fast

a

b

Electron affinity

12.0

0.08

11.0

Probability

Prediction

11.5

10.5
10.0

9.0

0.04

9.0

9.5

12.5

10.0

10.5

11.0

11.5

12.0

0.2

0.3

0.4

0.5

0.7

0.6

Target

Correlation

Chemical hardness

Mean 42

0.8

0.9

0.10

12.0
11.5

Probability

Prediction

0.06

0.02

9.5

11.0
10.5

0.08
0.06
0.04
0.02

10.0
9.5

Structure correlations mean 0.66

0.10

9.5

10.0

10.5

11.0

11.5

12.0

12.5

Target

Correct top 100

c

d

Adaptability 2ig0—correlation 0.75

Prediction

Target

Target adaptability

Predicted adaptability

Fig. 5 | Performance of the AI baseline models. a, Scatter plot of the predicted
against target values of chemical hardness and electron affinity. The AI baseline
models to predict QM properties have a high correlation of 0.75 and 0.77 for
electron affinity and chemical hardness, respectively. b, Adaptability is a
measure of the per-atom conformational plasticity of the protein. A histogram
of the correlation and the correct top 100 predictions of the adaptability for all
structures in the test set are given. An overall mean correlation of 0.66 can be
achieved and the mean top 100 accuracy was 0.42 for the adaptability predictions
(MD). c, Scatter plot for the adaptability result (as in a) of example structure 2IG0.

The predicted values are more narrowly distributed than the actual values,
but the general trend is correct, as shown by a high correlation value of 0.75.
d, The adaptability of the residues in the protein pocket highly deviates between
the amino acids. The AI model predicts the adaptability given in blue-shaded
(target) and red-shaded (AI-predicted) spheres. The radius is scaled according to
the adaptability value. The model can correctly identify the rigid residues (small
spheres) but also the amino acids with high flexibility. Color and character keys:
N, blue, nitrogen; S, yellow, sulfur; O, red, oxygen; C, beige for ligand atoms and
black for protein atoms, carbon.

examination of the protein pocket without the necessity of a lengthy
MD setup and simulation. The adaptability model gives an innovative
example of how experimental structures can be enhanced from the
MD-based MISATO data.
A binding affinity AI model combines MISATO MD and QM data.
Experimental binding affinities are known to be difficult to compare
across different experimental techniques, experimental conditions
and calculated affinity types. To decrease these effects, our affinity
model predicts a relative affinity of a target structure in relation to a
defined base complex. These pairs have the protein and affinity type
in common. We achieved high correlations for the MISATO binding
affinity benchmark, with improved results using MISATO features when
compared with no MISATO features (Fig. 6).

determined for each structure in the PDB. It is a measure of the thermal
vibration of each atom but usually reflects localized molecular motion
as well46. We achieved a mean correlation of 0.59 of the B factors with the
root-mean-square fluctuation (RMSF) in the MISATO MD trajectories.
To prove the model against more direct experimental flexibility data,
we measured the cap-binding domain of influenza virus polymerase
subunit PB247 as a model system. Heteronuclear Overhauser effect
(hetNOE) NMR measurements, which elucidate flexible protein regions
in solution, were performed on this structure (Supplementary Fig. 3).
We obtained a high correlation between the calculated adaptabilities and both B factors (0.63) and the hetNOE of the protein. A comparison with our adaptability prediction shows that the most flexible
regions and the residues of higher rigidity are correctly identified by
the model. Quantum chemical methods are required to predict reasonable values for ionization potentials and electron affinities48. This
applies not only to DFT (density functional theory) but also to ab initio.
In Supplementary Data 1 we provide a parameter study performed with

Experimental validation
The MISATO database and the adaptability AI model were validated
on experimental data (Fig. 6). In X-ray crystallography a B factor is

MISATO dynamic and QM features
MISATO curation
Not curated
Vina

0.8

9.5
9.0

4,000

Thiaflavans
R2 = 0.974

8.5
8.0
7.5
1.00 1.05 1.10

2,000

–0.2

0.2

0.4

0.6

0.8

Correlation

e

Adaptability

–0.2
–0.4
–0.6
–0.8
–1.0

1.8

Catechins
R2 = 0.6823

10.20
10.18
10.16
10.14
10.12
10.10

Residue count

1.3

0.

0.

0.8

–1*hetNOE

0.3

10.22

–0.2

Oxidation potential (V)

10.24

1.0
0.5

–0.7

0.

1.5

0.

2.5
2.0

Adaptability

2VQZ correlation 0.63

0.

d

1.0

1.20 1.25 1.30 1.35 1.40

R2 = 0.8386
Photocatalysts

1.15

DFT IP (V)

0.

12.0
11.5
11.0
10.5
10.0
9.5
9.0
8.5
8.0
7.5
7.0
–1.2

1,000

0.

0.2

0.

0.4

3,000

Koopman IP (eV)

0.6

Mean 1,043 5A/0 5NJZ 5Q0I 6QQT

B-factor

c 10.0

Correlation of Bfactors per structure: mean
0.59 ± 0.12

Oxidation potential (V)

0.

5,000

b

0.

Correlation to experimental binding affinities

Count

Spearman correlation

1.0

0.

a

Fig. 6 | Experimental validation of QM calculations, MD traces and AI models.
a, Spearman correlation of the affinity GNN model on the binding affinity
benchmark including MISATO features and without features. Moreover, the
results using Vina and non-curated complexes (original PDBbind) are shown.
We achieved a consistently better performance including QM charges and MD
adaptabilities as MISATO features across the affinity benchmark when compared
with all other approaches. b, Histogram of the correlation of experimental
B factors from X-ray crystallography experiments with RMSF calculations from
the MD simulations in MISATO. A correlation of 0.59 over all structures was
achieved. c, High correlations of calculated Koopmans ionization potentials (IP)

from ULYSSES with DFT ionization potentials (upper panel) and experimental
oxidation potentials (middle and lower panels) were found for different molecule
families. d, The cap-binding domain of influenza virus polymerase as a model
system for experimental validation of the predicted adaptability. Values given
by our AI model had a high correlation of 0.63 against the experimentally
determined B factors (which, despite characterizing atom thermal vibration,
usually indicates flexibility). e, Results of the hetNOE experiments of the
cap-binding domain of influenza virus polymerase indicating flexibility of the
protein chain were in high accordance with the results of the adaptability model
(indicated using shaded regions).

data collected from the CCCBDB database35, verifying the generality
of trends reported in the literature48,49. The parameter study shows
furthermore that semi-empirical ionization potentials are of a quality
similar to, if not higher than, the best DFT results. The advantage, however,
is that we systematically apply the same level of theory for all molecules,
small and very large alike. We validated the ULYSSES-based calculations
of Koopmans ionization potentials against experimental oxidation
potentials and DFT-based ionization potentials from the literature
for three molecule families. Our calculations correlated highly for
photocatalysts (0.84, experimental oxidation potential), catechins
(0.68, experimental oxidation potential) and thiaflavans (0.97, calculated DFT data).

Our binding affinity graph convolutional network model was
evaluated on this benchmark set with and without MISATO features.
Additionally, we evaluated the model performance on the original
PDBbind set, and using the Vina scoring function. With MD-derived
adaptabilities and QM charges, we obtained a mean Spearman correlation of 0.64, which was higher than without the MISATO features (0.50),
using Vina (0.51) and using the non-curated database (0.50). Interestingly, an improvement for each of the five sets using the MISATO
features could be achieved.
As confirmation of the given results, we evaluated the affinity
model on a second benchmark set comprising the six largest clusters of
protein structures (clustered on the basis of UniProt ID) of the test set
(Supplementary Table 3). These clusters are substantially larger than
the sets from the MISATO benchmark and do not necessarily originate
from the same publication and the same experimental method within a
set. The absolute correlations decreased for this second, more diverse
benchmark (Supplementary Fig. 4). Still, we see the same trend as for
the first benchmark with a better performance of the MISATO model
including adaptability and QM features than the other approaches.
Finally, consistent improvement of affinity prediction model
accuracy upon inclusion of QM and dynamic features was observed for
the entire curated set as well as selected subsets with high-confidence
affinity values (Fig. 6 and Supplementary Figs. 4 and 5). This emphasizes the importance of curation of ligand data and inclusion of at least
short-term dynamics in the accuracy of affinity predictions.

Binding affinity benchmark and validation
The numerical values describing ligand potency cannot serve as a reliable baseline due to their origin in a wide range of experiments and
conditions. These errors in the ground truth cannot be averaged out
efficiently. Therefore, we collected high-quality affinity data for 127
ligands for five different protein structures for a MISATO binding affinity
benchmark set (Supplementary Table 1 and Supplementary Data 2)50–54.
This set, being too small for training, can be a reliable validation method
for affinity-predicting models. To guarantee reliable affinity data we
filtered it to originate from the same publication for each set. Moreover,
each of the sets had at least 15 entries with a high dynamical range and
few additional occurrences of the protein structure within MISATO.

The given experiments show that adding the features present in
MISATO improves model accuracy over relying on implicit learning
from the bare structure.

Discussion

The great advances over the past years of AI technologies were only
possible due to the huge datasets that are fed into these models. In
structural biology, the protein folding problem was solved recently,
but the DD community still lacks a breakthrough model.
Here, we present MISATO, a database that will open routes in DD
for researchers from chemistry, structural biology, biophysics and
bioinformatics. MISATO contains the quantum-chemically refined
ligand dataset, which permitted the elimination of several structural
inaccuracies and crystallographic artifacts. Our refinement protocol
can be immediately applied by others for quick database augmentation. We enhance the curated dataset following two orthogonal dimensions. On the one hand, a QM approach supplies systematic electronic
properties. On the other hand, a classical approach reveals the system’s
dynamics and includes the binding affinity and conformational
landscape. MISATO contains the largest collection of protein–ligand
MD traces to date. Extensive experimental validation of the QM calculations, MD trajectories and AI baseline models highlights the dataset’s
importance (Fig. 6).
Checkpoint files are made available for potential community
extension of the dynamic traces (Supplementary Table 4). Structural biology datasets until now have been unable to incorporate
entropy-related information about binding sites and the dynamics of
the systems. By conducting MD simulations, it is possible to approximate the conformational space for entropy estimation. A Python interface, built to be intuitively used by anyone, provides preprocessing
scripts and template notebooks.
The current limitations of MISATO include the fact that until now
the QM calculations were only conducted on the ligand molecules.
Moreover, longer timescales of the MD simulations are desirable. These
limitations are related to the availability of computing resources. With
future releases of MISATO these points will be addressed.
The dataset augmentation presented here paves the way for creative
applications of AI models. Our example graph neural network (GNN)
model offers quick access to pocket flexibility, a problem never tackled
before. This is however just a starting point for a whole class of AI models
sprouting from MISATO. Ultimately, we envision models being built
on the best of quantum and Newtonian worlds to obtain high-quality
thermodynamics, innovatively and efficiently matching the quality of
experimental data. With MISATO, AI models will uncover hidden state
variables describing protein–ligand complexes.
Altogether, MISATO is meant to provide sufficient training power
for accurate, next-generation structure-based DD using AI methods.

Methods

Semi-empirical calculations
QM calculations were performed using the ULYSSES library55, our
in-house semi-empirical package. The methods of choice were
GFN2-xTB56, AM1 (ref. 57) and PM6 (ref. 58). Implicit solvation was
included using ALPB59 as parameterized for GFN2-xTB. Selected media
included water and wet octanol. Bond orders and hybridizations were
estimated using distance-based criteria.

QM curation of ligand space
Consistent atomic assignments were determined using a series of
semi-empirical tests. Semi-empirical quantum chemical methods offer
a good compromise between accuracy and computational efficiency60,
which is suitable to refine a collection of almost 20,000 structures of
various chemical natures and dimensions (from 6 to almost 370 atoms
per molecule). The consistency tests we designed were performed in
vacuum to ensure maximum sensitivity of the calculations to structural

inconsistencies. Predicted properties, however, are also obtained using
an implicit solvation model.
It is well documented that molecules with many polar groups
lack convergence in wavefunction optimization61. The same applies
when incorrect charges or protonation states are used. Implicit solvation substantially ameliorates the issue and masks problems. In
fact, after determining the first guess for total molecular charges,
single-point-energy calculations on unrefined ligands using implicit
water required roughly 6 h of computation time. Turning off implicit
solvation increased the calculation time to almost three weeks on the
same machine. This was indicative of severe limitations in proton and
total charge assignment. Alternative protonation algorithms were
tested—for example, Open Babel62. Due to experimental inaccuracies in
the geometries, the results were still faulty (Supplementary Figs. 6–9).
Our refinement protocol started with a search for structures with
strong atomic overlap. Next, we looked for structures with problematic
wavefunction convergence. Vanishing HOMO–LUMO gaps or unpaired
electrons flagged further problems, as did violations of the octet rule
based on QM population analysis. Finally, we searched for changes in
ligand connectivity patterns after QM geometry optimization. This was
particularly useful in determining inconsistent protonation states or
incorrect electron counting, which generated biradicals. Calculated
properties yielded additional testing grounds. Incorrect element
assignments were detected when plotting the partial charges against
D4 polarizabilities63 (Fig. 2b).
Severe structural deformations were also detected, inconsistent
with the chemical structure (see previous section). For the current stage
of the database, we decided to fix only the most extreme cases. This
was done using Avogadro (Supplementary Fig. 10)64. Further structural
refinement is planned.
Whenever our corrections seemed questionable, or the structure
was unclear, we checked the original publication. Oxidation states
were another sensible point for ligands containing transition metals.
Examples of structures we refined are given in the Supplementary
Information (Supplementary Figs. 10–12). To ease the inclusion and
processing of new structures, a heuristics-based program is included
in the database, which performs the basic structural processing (see
Supplementary Information for more details). A detailed schematic for
the protocol used for cleaning and refining the structures is also given
in the Supplementary Information (Supplementary Figs. 13 and 14).

MD simulations
For all MD simulations, we used the Amber20 (ref. 65) software suite.
The protein–ligand complexes were prepared and simulated on the
basis of a standard set-up. We parameterized the ligands calculating
AM1-BCC38 charges using antechamber66 (if the charges did not converge within 1 h we used AM1 charges calculated with ULYSSES). We used
the gaff2 (ref. 66) force field for ligands and ff14SB67 for the proteins.
The complexes were neutralized with Na+ and Cl− ions and solvated in
TIP3P68 explicit water using periodic boundary conditions in an octahedral box (minimum distance between protein and boundary 12 Å).
The complexes were minimized (1,000 steps steepest descent
followed by conjugate gradient) and heated to 300 K in several steps
within 16 ps. We performed production simulations for 10 ns on all
protein–ligand cases in an NVT ensemble. The first 2 ns were discarded
as equilibration phase, so 8 ns are stored over 100 snapshots for each
protein–ligand complex. Using pytraj31 we calculated different proper­
ties of the simulations such as the MMGBSA interaction energy, the
buried solvent accessible surface area, the center-of-mass distance
between ligand and receptor, and root-mean-square deviations from
the native complex.

Access to the database
The database can be downloaded from Zenodo (Supplementary
Table 4). Data are stored in a hierarchical data format. We created two

H5 files, one for the protein–ligand dynamics and one for quantum
chemical data, that can be accessed through our container images or
after installation of the required Python packages. Installation instructions are given in the repository (Supplementary Table 4). Data are split
for each structure using the PDB ID. The feature of interest must also be
specified (Fig. 4 and Supplementary Table 2). Python scripts are given
in the repository showing how to preprocess the MD dataset for specific
cases, only Cα atoms, no hydrogen atoms, only atoms from the binding
pocket, and the inclusion of new features. Instructions on how to run
inference on new PDB files and visualize the baseline models are given.
Checkpoint files for continuing the MD simulations and the electronic
densities are provided separately.

AI applications
For the baseline model for QM predictions, we followed the GNN
architecture for small-molecule property prediction in ATOM3D69.
This model is based on graph convolutions proposed by Kipf and
Welling70 and was adapted for the simultaneous prediction of electron
affinity and chemical hardness as essential parameters to describe
the ligand. The architecture for the baseline model was a dense layer
followed by three sequential layers of NNConv and GRU followed by
two dense layers. The model is available via our GitHub repository.
The performance of the ML model was evaluated using correlation
and the mean absolute error.
We encode each molecule using the atom positions, the atom type
and the bond between the atoms. Each atom corresponds to a node.
The atom types are one-hot encoded and edges are defined by selecting the nearest neighbors with a distance of 4.5 Å for each atom. Edges
are weighted inversely by the distance between the atoms. We removed
outliers straying more than 20 s.d. from the mean values (PDB IDs given
in Supplementary Information). All outliers corresponded to molecules
containing negatively charged groups and alkyl chains. In other words,
these are highly saturated molecules from the electronic viewpoint.
Because of their electronic structure, acceptance of an electron is highly
unlikely, resulting in very low-to-negative electron affinities. Inaccuracies
in the geometries further exacerbate the calculated electron affinities.
The results on these systems indicate that some electronic properties are
not quantitative; instead, they simply reflect the system’s behavior. We
trained the GNN with four NVIDIA A100 graphics processing units (GPUs)
and 96 CPUs (from 48 physical cores) and for 200 epochs. We used a batch
size of 128 and applied a random translation on each node of 0.05 Å.
For the MD task, we modified the GNN architecture from ATOM3D69
for the node regression task by removing the aggregation of node features into graph features. The architecture for the baseline model was
five sequential GCNConv layers70 followed by two linear layers, summing to 370,000 trainable parameters. The dataset was split into a train
(80%), a test (10%) and a validation set (10%) (Supplementary Table 5
and Supplementary Fig. 15) by clustering the amino-acid sequences of
the proteins using BlastP71 to make sure to not have a leakage of similar
structural motifs between the splits. We train the GNN with four NVIDIA
A100 GPUs and 96 CPUs and for 15 epochs. We use a batch size of eight
and a random translation of 0.05 Å. With our model, we calculated the
adaptability of each atom during the MD simulation. To this end, we
performed an alignment of the coordinates of each simulation with
reference to the first frame. To calculate the adaptability γx for each
atom x we take the mean distance of each atom over all timesteps i from
the initial position of the atom rref,x:
γx =

N

frames
∑ |(rref,x − ri,x )| .
Nframes i

Hydrogen atoms were omitted to reduce the size of the model. For
the evaluation, the mean over the results for each structure was calculated. Adaptability gives results very similar to those of RMSF evaluations. We evaluated the performance of our training using Pearson

correlation and the average accuracy of the 100 most flexible atoms
of each complex.
For the binding affinity task, the data processing, training
procedure and GNN architecture were modified. For data processing,
all protein–ligand complexes (excluding 1,192 protein–peptide complexes) with known binding affinity were clustered at 30% sequence
similarity to avoid data leakage between training (82%), validation (9%)
and test (9%) sets (Supplementary Fig. 15). The MISATO affinity benchmark was a holdout part of the test set. Next, clusters were defined on
the basis of the UniProt identifier and affinity type, so that each cluster
contained only affinity values of the same protein and one of the three
affinity types present in the dataset (Ki, Kd, IC50).
The model predicts the ratio of binding affinities between a pair
of protein–ligand complexes. For each cluster, one base molecule
was defined that built a pair with each entry of the cluster. The protein–ligand complexes for which no cluster with at least two entries
could be defined were discarded (2,259 entries). The atom types were
one-hot encoded (omitting hydrogen atoms), and edges were defined
following the adaptability model.
One training step consisted of one forward pass for each of the
two complexes and mean squared error loss calculation based on the
logarithmic ratio of the affinities for each pair. We trained a model
including MISATO features and without MISATO features. MISATO
atom features comprised calculated adaptabilities (MD) and GFN2-xTB
charges in water (QM) for the ligands.
For the GNN architecture, five sequential GCNConv layers were
followed by a separate pooling operation for the ligand and protein,
respectively. These representations were then further processed via
three linear layers with ReLU nonlinearities.
We trained the GNN with four GPUs, 90 CPUs, a batch size of 50 and
for 50 epochs. We evaluated the best models on the MISATO affinity
benchmark using Spearman correlation on each set.
We used PyTorch v.1.14 to train the models. To code the data loaders and the GNN, we used PyTorch Geometric 2.3.0.

Scoring of ligands with AutoDock Vina
We calculated an AutoDock Vina9 score for the MISATO refined protein–ligand complexes of both benchmark sets. We followed a standard
preprocessing procedure of generating pdbqt files (see ref. 72 to follow
the exact steps). For the receptors we used the prepare_receptor tool on
the protonated protein structure from ADFR Suite73,74. For the ligands
we converted the structures from MOL2 format to pdbqt format using
the mk_prepare_ligand.py script. We computed the Vina scores from
the generated pdbqt files using the score function from the Python
interface of Vina (all scripts can be found via the GitHub page of Vina).

Correlation with experimental B factors
The experimental B factors were parsed from published PDB files of
crystal structures. For data cleaning, we omitted structures for which
80% of the published B factor values had the same entry. Additionally,
for some structures, it was not possible to parse the B factors correctly
due to inconsistencies in the underlying PDB files. The RMSF of each
atom of the MD simulation was calculated after superposition to the
first frame using pytraj31.

Binding affinity benchmark
The benchmark was created by identifying structures in MISATO that
originated from the same publication with at least 15 entries. The
benchmark was carefully evaluated by assessment of the publication
for each of the sets. Only high-quality experimental techniques and
data were considered. We further removed sets with a small dynamic
range of the affinity data, high coexistence of structures of the same
protein within MISATO, and sets with cofactors or metals interacting
at the binding site. We obtained a benchmark consisting of five protein
sets and 127 bound ligands.

Protein purification and NMR spectroscopy
The influenza PB2 domain was expressed and purified as previously
published47. NMR data were acquired at 298 K using a 0.8 mM 13C15
N-PB2 sample on an AV600 spectrometer equipped with a cryoprobe.
The sample buffer contained 20 mM sodium phosphate at pH 6.5, and
100 mM NaCl. Standard NMR experiments were used for chemical shift
assignments, mainly HNCA, HNCACB, CBCACONH, HNCO, CCONH and
HCCH/TOCSY (total correlation spectroscopy). Spectra were processed
with the nmrDraw/NMRPipe package75 and analyzed with NMRView76.

Statistics and reproducibility
The splits for train, test and validation were randomized for the different ML models. The exact procedure for each model is given in Supplementary Fig. 15. No statistical method was used to predetermine sample
size. For MD, structures were disregarded whenever non-standard
ligand atoms (metal ions) or inconsistencies in the protein starting
structures were encountered. For the QM model (Supplementary
Section 3), a small number (30) of structures were omitted due to the
inability of the current algorithm to provide correct predictions for
them. This does not introduce a bias to the observation and does not
change our observations.
The investigators were not blinded to allocation during experiments or outcome assessment.

Reporting summary
Further information on research design is available in the Nature
Portfolio Reporting Summary linked to this article.

Data availability

MISATO is publicly accessible and can be downloaded from Zenodo77
(https://zenodo.org/records/7711953). We provide instructions for
usage, data loaders via our GitHub repository, and a container image
with all relevant packages installed for GPU usage (Supplementary
Table 4). MISATO was built from the PDBbind database (release 2022).
Source Data are provided with this paper.

Code availability

The code can be accessed from our GitHub repository and on Zenodo78
(https://github.com/t7morgen/misato-dataset). The dataset is accessible via a Python interface using a simple PyTorch data loader. Special
attention was given to code modularity, which makes it easy to adjust
the AI architecture (Fig. 4 and Supplementary Section 7). We have
implemented our dataset according to the ATOM3D69 code base, a
comprehensive suite of ML methods for molecular applications.

References
1.

2.
3.

4.
5.
6.
7.

8.

Jumper, J. et al. Highly accurate protein structure prediction with
AlphaFold. Nature 596, 583–589 (2021).
Berman, H., Henrick, K. & Nakamura, H. Announcing the
worldwide Protein Data Bank. Nat. Struct. Mol. Biol. 10, 980 (2003).
Mohs, R. C. & Greig, N. H. Drug discovery and development: role
of basic biological research. Alzheimer’s Dement. Transl. Res. Clin.
Interv. 3, 651–657 (2017).
Sliwoski, G., Kothiwale, S., Meiler, J. & Lowe, E. W. Computational
methods in drug discovery. Pharm. Rev. 66, 334–395 (2014).
Thiel, W. Semiempirical quantum-chemical methods.
WIREs Comput. Mol. Sci. 4, 145–157 (2014).
Hollingsworth, S. A. & Dror, R. O. Molecular dynamics simulation
for all. Neuron 99, 1129–1143 (2018).
Siebenmorgen, T. & Zacharias, M. Computational prediction of
protein–protein binding affinities. WIREs Comput. Mol. Sci. 10,
e1448 (2020).
Trott, O. & Olson, A. J. AutoDock Vina: improving the speed and
accuracy of docking with a new scoring function, efficient optimi­
zation, and multithreading. J. Comput. Chem. 31, 455–461 (2010).

9.

Kmiecik, S. et al. Coarse-grained protein models and their
applications. Chem. Rev. 116, 7898–7936 (2016).
10. Spicher, S. & Grimme, S. Robust atomistic modeling of materials,
organometallic, and biochemical systems. Angew. Chem. Int. Ed.
59, 15665–15673 (2020).
11. Vandenbrande, S., Waroquier, M., Speybroeck, V. V. & Verstraelen,
T. The monomer electron density force field (MEDFF): a physically
inspired model for noncovalent interactions. J. Chem. Theory
Comput. 13, 161–179 (2017).
12. Wang, J. & Dokholyan, N. V. Yuel: improving the generalizability of
structure-free compound–protein interaction prediction. J. Chem.
Inf. Model. 62, 463–471 (2022).
13. Ponder, J. W. et al. Current status of the AMOEBA polarizable force
field. J. Phys. Chem. B 114, 2549–2564 (2010).
14. Chen, B. et al. Automated discovery of fundamental variables
hidden in experimental data. Nat. Comput Sci. 2, 433–442 (2022).
15. Durrant, J. D. & McCammon, J. A. NNScore: a
neural-network-based scoring function for the characterization
of protein−ligand complexes. J. Chem. Inf. Model. 50, 1865–1871
(2010).
16. Wang, X., Terashi, G., Christoffer, C. W., Zhu, M. & Kihara, D. Protein
docking model evaluation by 3D deep convolutional neural
networks. Bioinformatics 36, 2113–2118 (2020).
17. Wang, N.-N. et al. ADME properties evaluation in drug discovery:
prediction of Caco-2 cell permeability using a combination of
NSGA-II and boosting. J. Chem. Inf. Model. 56, 763–773 (2016).
18. Ishida, S., Terayama, K., Kojima, R., Takasu, K. & Okuno, Y.
AI-driven synthetic route design incorporated with retrosynthesis
knowledge. J. Chem. Inf. Model. 62, 1357–1367 (2022).
19. Karpov, P., Godin, G. & Tetko, I. V. A transformer model for
retrosynthesis. In Artificial Neural Networks and Machine
Learning—ICANN 2019: Workshop and Special Sessions
(eds Tetko, I. V. et al.) 817–830 (Springer, 2019).
20. Öztürk, H., Özgür, A. & Ozkirimli, E. DeepDTA: deep drug–target
binding affinity prediction. Bioinformatics 34, i821–i829 (2018).
21. Karimi, M., Wu, D., Wang, Z. & Shen, Y. DeepAffinity: interpretable
deep learning of compound–protein affinity through unified
recurrent and convolutional neural networks. Bioinformatics 35,
3329–3338 (2019).
22. Hassan-Harrirou, H., Zhang, C. & Lemmin, T. RosENet: improving
binding affinity prediction by leveraging molecular mechanics
energies with an ensemble of 3D convolutional neural networks.
J. Chem. Inf. Model. 60, 2791–2802 (2020).
23. Feinberg, E. N. et al. PotentialNet for molecular property
prediction. ACS Cent. Sci. 4, 1520–1530 (2018).
24. Li, Y., Rezaei, M. A., Li, C. & Li, X. DeepAtom: a framework
for protein–ligand binding affinity prediction. In 2019 IEEE
International Conference on Bioinformatics and Biomedicine
(BIBM) 303–310 (IEEE, 2019).
25. Wang, R., Fang, X., Lu, Y., Yang, C.-Y. & Wang, S. The PDBbind
database: methodologies and updates. J. Med. Chem. 48,
4111–4119 (2005).
26. Liu, T., Lin, Y., Wen, X., Jorissen, R. N. & Gilson, M. K. BindingDB:
a web-accessible database of experimentally determined
protein–ligand binding affinities. Nucleic Acids Res. 35,
D198–D201 (2007).
27. Hu, L., Benson, M. L., Smith, R. D., Lerner, M. G. & Carlson, H. A.
Binding MOAD (Mother Of All Databases). Proteins Struct. Funct.
Bioinform. 60, 333–340 (2005).
28. Friedrich, N.-O., Simsir, M. & Kirchmair, J. How diverse are the
protein-bound conformations of small-molecule drugs and
cofactors? Front. Chem. 6, 68 (2018).
29. Korlepara, D. B. et al. PLAS-5k: dataset of protein–ligand affinities
from molecular dynamics for machine learning applications.
Sci. Data 9, 548 (2022).

30. Korlepara, D. B. et al. PLAS-20k: extended dataset of protein–
ligand affinities from MD simulations for machine learning
applications. Sci. Data 11, 180 (2024).
31. Yang, J., Shen, C. & Huang, N. Predicting or pretending: artificial
intelligence for protein–ligand interactions lack of sufficiently
large and unbiased datasets. Front. Pharmacol. 11, 69 (2020).
32. Volkov, M. et al. On the frustration to predict binding affinities
from protein–ligand structures with deep neural networks.
J. Med. Chem. 65, 7946–7958 (2022).
33. Vajda, S., Beglov, D., Wakefield, A. E., Egbert, M. & Whitty, A.
Cryptic binding sites on proteins: definition, detection, and
druggability. Curr. Opin. Chem. Biol. 44, 1–8 (2018).
34. Zeng, L. et al. Selective small molecules blocking HIV-1 Tat and
coactivator PCAF association. J. Am. Chem. Soc. 127, 2376–2377
(2005).
35. Johnson, R. D. III (ed). Computational Chemistry Comparison and
Benchmark Database Standard Reference Database Number 101
Release 22 (NIST, accessed 12 Jul 2022); http://cccbdb.nist.gov/
36. Bista, M. et al. Transient protein states in designing inhibitors of
the MDM2–p53 interaction. Structure 21, 2143–2151 (2013).
37. Xie, M. et al. Structural basis of inhibition of ERα–coactivator
interaction by high-affinity N-terminus isoaspartic acid tethered
helical peptides. J. Med. Chem. 60, 8731–8740 (2017).
38. Jakalian, A., Jack, D. B. & Bayly, C. I. Fast, efficient generation of
high-quality atomic charges. AM1-BCC model: II. Parameterization
and validation. J. Comput. Chem. 23, 1623–1641 (2002).
39. Dodda, L. S., Vilseck, J. Z., Tirado-Rives, J. & Jorgensen, W. L.
1.14*CM1A-LBCC: localized bond-charge corrected CM1A
charges for condensed-phase simulations. J. Phys. Chem. B 121,
3864–3870 (2017).
40. Jorgensen, W. L., Maxwell, D. S. & Tirado-Rives, J. Development
and testing of the OPLS all-atom force field on conformational
energetics and properties of organic liquids. J. Am. Chem. Soc.
118, 11225–11236 (1996).
41. Storer, J. W., Giesen, D. J., Cramer, C. J. & Truhlar, D. G. Class
IV charge models: a new semiempirical approach in quantum
chemistry. J. Comput. Aided Mol. Des. 9, 87–110 (1995).
42. Li, J., Zhu, T., Cramer, C. J. & Truhlar, D. G. New class IV charge
model for extracting accurate partial charges from wave
functions. J. Phys. Chem. A 102, 1820–1831 (1998).
43. Thompson, J. D., Cramer, C. J. & Truhlar, D. G. Parameterization of
charge model 3 for AM1, PM3, BLYP, and B3LYP. J. Comput. Chem.
24, 1291–1304 (2003).
44. Grimme, S. & Bannwarth, C. Ultra-fast computation of electronic
spectra for large systems by tight-binding based simplified
Tamm–Dancoff approximation (sTDA-xTB). J. Chem. Phys. 145,
054103 (2016).
45. Wang, E. et al. End-point binding free energy calculation with
MM/PBSA and MM/GBSA: strategies and applications in drug
design. Chem. Rev. 119, 9478–9508 (2019).
46. Sun, Z., Liu, Q., Qu, G., Feng, Y. & Reetz, M. T. Utility of B factors
in protein science: interpreting rigidity, flexibility, and internal
motion and engineering thermostability. Chem. Rev. 119,
1626–1665 (2019).
47. Guilligay, D. et al. The structural basis for cap binding by influenza
virus polymerase subunit PB2. Nat. Struct. Mol. Biol. 15, 500–506
(2008).
48. Rayne, S. & Forest, K. Benchmarking semiempirical, Hartree–
Fock, DFT, and MP2 methods against the ionization energies and
electron affinities of short- through long-chain [n]acenes and [n]
phenacenes. Can. J. Chem. 94, 251–258 (2016).
49. Zhan, C.-G., Nichols, J. A. & Dixon, D. A. Ionization potential,
electron affinity, electronegativity, hardness, and electron
excitation energy: molecular properties from density functional
theory orbital energies. J. Phys. Chem. A 107, 4184–4195 (2003).

50. Lange, G. et al. Requirements for specific binding of low affinity
inhibitor fragments to the SH2 domain of pp60Src are identical
to those for high affinity binding of full length inhibitors. J. Med.
Chem. 46, 5184–5195 (2003).
51. Öster, L., Tapani, S., Xue, Y. & Käck, H. Successful generation
of structural information for fragment-based drug discovery.
Drug Discov. Today 20, 1104–1111 (2015).
52. Heinzlmeir, S. et al. Chemoproteomics-aided medicinal chemistry
for the discovery of EPHA2 inhibitors. ChemMedChem 12,
999–1011 (2017).
53. Gaieb, Z. et al. D3R Grand Challenge 2: blind prediction
of protein–ligand poses, affinity rankings, and relative
binding free energies. J. Comput. Aided Mol. Des. 32, 1–20
(2018).
54. Whitehouse, A. J. et al. Development of inhibitors against
Mycobacterium abscessus tRNA (m1G37) methyltransferase
(TrmD) using fragment-based approaches. J. Med. Chem. 62,
7210–7232 (2019).
55. Menezes, F. & Popowicz, G. M. ULYSSES: an efficient and easy
to use semiempirical library for C. J. Chem. Inf. Model. 62,
3685–3694 (2022).
56. Bannwarth, C., Ehlert, S. & Grimme, S. GFN2-xTB—an accurate and
broadly parametrized self-consistent tight-binding quantum
chemical method with multipole electrostatics and densitydependent dispersion contributions. J. Chem. Theory Comput. 15,
1652–1671 (2019).
57. Dewar, M. J. S., Zoebisch, E. G., Healy, E. F. & Stewart, J. J. P.
Development and use of quantum mechanical molecular
models. 76. AM1: a new general purpose quantum mechanical
molecular model. J. Am. Chem. Soc. 107, 3902–3909
(1985).
58. Stewart, J. J. P. Application of the PM6 method to modeling
proteins. J. Mol. Model. 15, 765–805 (2009).
59. Sigalov, G., Fenley, A. & Onufriev, A. Analytical electrostatics
for biomolecules: beyond the generalized Born approximation.
J. Chem. Phys. 124, 124902 (2006).
60. Christensen, A. S., Kubař, T., Cui, Q. & Elstner, M. Semiempirical
quantum mechanical methods for noncovalent interactions
for chemical and biochemical applications. Chem. Rev. 116,
5301–5337 (2016).
61. Dixon, S. L. & Merz, K. M. Fast, accurate semiempirical molecular
orbital calculations for macromolecules. J. Chem. Phys. 107,
879–893 (1997).
62. O’Boyle, N. M. et al. Open Babel: an open chemical toolbox.
J. Cheminform. 3, 33 (2011).
63. Caldeweyher, E. et al. A generally applicable atomic-charge
dependent London dispersion correction. J. Chem. Phys. 150,
154122 (2019).
64. Hanwell, M. D. et al. Avogadro: an advanced semantic chemical
editor, visualization, and analysis platform. J. Cheminform. 4, 17
(2012).
65. Case, D. A. et al. Amber 2021 (Univ. of California, San Francisco,
2021).
66. Wang, J., Wolf, R. M., Caldwell, J. W., Kollman, P. A. & Case, D. A.
Development and testing of a general Amber force field.
J. Comput. Chem. 25, 1157–1174 (2004).
67. Maier, J. A. et al. ff14SB: improving the accuracy of protein side
chain and backbone parameters from ff99SB. J. Chem. Theory
Comput. 11, 3696–3713 (2015).
68. Jorgensen, W. L., Chandrasekhar, J., Madura, J. D., Impey, R. W. &
Klein, M. L. Comparison of simple potential functions for
simulating liquid water. J. Chem. Phys. 79, 926–935 (1983).
69. Townshend, R. J. L. et al. ATOM3D: tasks on molecules in
three dimensions. Preprint at https://doi.org/10.48550/
arXiv.2012.04035 (2022).

70. Kipf, T. N. & Welling, M. Semi-supervised classification with graph
convolutional networks. Preprint at https://doi.org/10.48550/
arXiv.1609.02907 (2017).
71. Huang, Y., Niu, B., Gao, Y., Fu, L. & Li, W. CD-HIT Suite: a web
server for clustering and comparing biological sequences.
Bioinformatics 26, 680–682 (2010).
72. Forli, S. et al. Computational protein–ligand docking and virtual
drug screening with the AutoDock suite. Nat. Protoc. 11, 905–919
(2016).
73. Zhao, Y., Stoffler, D. & Sanner, M. Hierarchical and multi-resolution
representation of protein flexibility. Bioinformatics 22, 2768–2774
(2006).
74. Ravindranath, P. A., Forli, S., Goodsell, D. S., Olson, A. J. &
Sanner, M. F. AutoDockFR: advances in protein–ligand docking
with explicitly specified binding site flexibility. PLoS Comput. Biol.
11, e1004586 (2015).
75. Delaglio, F. et al. NMRPipe: a multidimensional spectral
processing system based on UNIX pipes. J. Biomol. NMR 6,
277–293 (1995).
76. Johnson, B. A. & Blevins, R. A. NMR View: a computer program
for the visualization and analysis of NMR data. J. Biomol. NMR 4,
603–614 (1994).
77. Siebenmorgen, T. et al. MISATO—machine learning dataset for
structure-based drug discovery. Zenodo https://doi.org/10.5281/
zenodo.7711953 (2023).
78. t7morgen/misato-dataset: release for publication. Zenodo
https://doi.org/10.5281/zenodo.10926008 (2024).

Acknowledgements

This work received funding from BMWi ZIM KK 5197901TS0 (T.S.,
F.M., G.M.P.) and BMBF, SUPREME, 031L0268 (T.S., F.M., G.M.P.). This
work was supported by the Helmholtz Association’s Initiative and
Networking Fund on the HAICORE@FZJ partition.
The funders had no role in study design, data collection and analysis,
decision to publish or preparation of the manuscript.

Author contributions

T.S. and F.M. created and refined the dataset, designed the ML
experiments, performed the ML experiments, analyzed the data and
wrote the paper. S.B., E.M. and K.D. performed the ML experiments,
analyzed the data and contributed to the paper writing. A.S.D.M.
performed the NMR experiments and analysis and wrote the
NMR section. R.K. selected and validated the affinity benchmark.
P.L., S.K., M.P., F.J.T. and M.S. contributed to study design, paper

writing and funding of the project. G.M.P. conceived and designed the
ML experiments, analyzed the data and wrote the paper.

Funding

Open access funding provided by Helmholtz Zentrum München Deutsches Forschungszentrum für Gesundheit und Umwelt (GmbH).

Competing interests

The authors declare no competing interests.

Additional information

Supplementary information The online version contains supplementary
material available at https://doi.org/10.1038/s43588-024-00627-2.
Correspondence and requests for materials should be addressed to
Grzegorz M. Popowicz.
Peer review information Nature Computational Science thanks
Martin Zacharias and the other, anonymous, reviewer(s) for their
contributions to the peer review of this work. Primary Handling Editor:
Kaitlin McCardle, in collaboration with the Nature Computational
Science team. Peer reviewer reports are available.
Reprints and permissions information is available at
www.nature.com/reprints.
Publisher’s note Springer Nature remains neutral with regard to
jurisdictional claims in published maps and institutional affiliations.
Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit http://creativecommons.
org/licenses/by/4.0/.
© The Author(s) 2024


---

# PED in 2024: improving the community deposition of structural ensembles for intrinsically disordered proteins

**Authors:** Hamidreza Ghafouri, Tamas Lazar, Alessio Del Conte, Luiggi G Tenorio Ku, PED Consortium, et al.
**Year:** 2024
**Venue:** Nucleic Acids Research
**DOI:** 10.1093/nar/gkad947
**Source PDF URL:** https://europepmc.org/articles/PMC10767937?pdf=render (Europe PMC copy of PMC10767937; gold OA, Nucleic Acids Research)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Nucleic Acids Research, 2024, 52, D536–D544
https://doi.org/10.1093/nar/gkad947
Advance access publication date: 30 October 2023
Database issue

PED in 2024: improving the community deposition of
structural ensembles for intrinsically disordered proteins
Hamidreza Ghafouri 1 ,† , Tamas Lazar 2 ,3 ,† , Alessio Del Conte 1 , Luiggi G Tenorio Ku1 , PED
Consortium, Peter Tompa 2 ,3 ,4 , Silvio C.E. Tosatto 1 ,* and Alexander Miguel Monzon 5 ,*

Department of Biomedical Sciences, University of Padova, Padova, Italy
VIB-VUB Center for Structural Biology, Vlaams Instituut voor Biotechnologie (VIB), Brussels, Belgium
Structural Biology Brussels, Department of Bioengineering, Vrije Universiteit Brussel (VUB), Brussels, Belgium
Institute of Enzymology, Research Centre for Natural Sciences (RCNS), Budapest, Hungary
Department of Information Engineering, University of Padova, Padova, Italy

*

To whom correspondence should be addressed. Tel: +39 049 827 6269; Email: alexander.monzon@unipd.it
Correspondence may also be addressed to Silvio C.E. Tosatto. Email: silvio.tosatto@unipd.it
†
The authors wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors.

Abstract
The Protein Ensemble Database (PED) (URL: https://proteinensemble.org) is the primary resource for depositing structural ensembles of intrinsically disordered proteins. This updated version of PED reflects advancements in the field, denoting a continual expansion with a total of
461 entries and 538 ensembles, including those generated without explicit experimental data through novel machine learning (ML) techniques.
With this significant increment in the number of ensembles, a few yet-unprecedented new entries entered the database, including those also
determined or refined by electron paramagnetic resonance or circular dichroism data. In addition, PED was enriched with several new features,
including a novel deposition service, improved user interface, new database cross-referencing options and integration with the 3D-Beacons
network—all representing efforts to improve the FAIRness of the database. Foreseeably, PED will keep growing in size and expanding with
new types of ensembles generated by accurate and fast ML-based generative models and coarse-grained simulations. Therefore, among future
efforts, priority will be given to further develop the database to be compatible with ensembles modeled at a coarse-grained level.

Graphical abstract

Received: September 15, 2023. Revised: October 10, 2023. Editorial Decision: October 11, 2023. Accepted: October 13, 2023
© The Author(s) 2023. Published by Oxford University Press on behalf of Nucleic Acids Research.
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/),
which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

D537

Introduction
Intrinsically disordered proteins or regions (IDPs/IDRs) lack a
specific, stable structure and instead exist as rapidly interconverting conformers. This arises from their relatively uniform
free-energy landscape, resulting in their highly dynamic and
heterogeneous nature (1). IDPs/IDRs play significant roles
in various essential functions such as cell signaling, regulation and recognition. Furthermore, their involvement in numerous human diseases renders them highly attractive targets for therapeutic drug discovery (2). While binding modes
of some IDPs/IDRs that fold upon interaction offer valuable structural insights (3), gaining a thorough comprehension
of the complex mechanisms governing the function of IDPs
also requires knowledge of their structural dynamics in the
unbound state, and many IDPs/IDRs form fuzzy complexes
(3). Given their extreme conformational dynamics, modeling
IDPs/IDRs in terms of ensembles is the only valid strategy for
structurally studying IDP function. By definition, a conformational ensemble consists of multiple structures, each with their
statistical weights representing their relative populations and
transition rates that quantify their dynamics (4). Despite the
steady expansion of experimentally determined protein structures in the Protein Data Bank (5) and the recent AlphaFold
Protein Structure Database (6), which contains accurate structural models of millions of proteins, the information they offer
about the dynamic nature of proteins remains limited, especially in the context of ensemble representation of IDPs. In
2014, the Protein Ensemble Database (PED) (7) was established to bridge this gap, and over time, it has consistently
evolved, enhancing the quantity and quality of deposited ensembles.
Generally, conformational ensembles are determined by integrating experimental and computational methods. This involves a diverse range of experimental techniques, including
nuclear magnetic resonance (NMR) spectroscopy, small angle
X-ray scattering (SAXS), single-molecule Förster resonance
energy transfer (smFRET), electron paramagnetic resonance
(EPR) and circular dichroism (CD) (4,8). These experimental measurements serve as global and/or local constraints, enabling the resampling and reweighting of a pool of conformers
generated through statistical conformer generators or molecular dynamics (MD)/Monte Carlo (MC) simulations. Moreover, the advent of AlphaFold2 (9), RoseTTAFold (10) and
the advancements in machine learning approaches have fostered the development of various pipelines aimed at effectively
modeling multiple conformational states or predicting conformational ensembles (11–13). Nevertheless, despite recent
progress in the field, modeling conformational ensembles, especially for IDRs/IDPs, remains challenging. On the computational front, a significant obstacle arises from the lack of a precise energy function to guide MD or MC simulations (14,15),
coupled with limited computational resources for thorough
sampling of the conformational space (16). On the other hand,
from an experimental standpoint, a major challenge is accurately quantifying all sources of errors and uncertainties in
both the experimental data and the predictors (forward models). Additionally, the observable data are averaged over all
members of the ensemble, leading to a reduction in information content. Because of these limitations, resolving structural
ensembles has persisted as an ‘underdetermined’ challenge.
This viewpoint arises from the fact that the number of degrees of freedom in the ensembles significantly surpasses the

available experimental restraints, leading to multiple potential solutions for the problem without a distinct ‘best’ option.
In such a context, having comprehensive and manually curated IDP-related databases, e.g. PED (17), DisProt (18), MobiDB (19), FuzDB (3) and IDEAL (20), can serve multiple purposes. First and foremost, they can serve as a foundational
reference and a valuable resource for establishing a validation
pipeline to assess the reliability of IDP conformational ensembles. Furthermore, they function as extensive training datasets
for upcoming machine learning (ML) models (21). Since the
latest PED publication in 2021 (17), a strong emphasis has
been given by the scientific community to predict IDP conformational ensembles from sequence by combining ML approaches and MD simulations (22,23), as well as to compare
conformational ensembles of flexible proteins (24,25). In this
article, we present the new version of the PED (Protein Ensemble Database, https://proteinensemble.org), aimed at addressing the evolving challenges and advancements in the field
of IDPs/IDRs. Our primary goal has consistently been to enhance the size of our database. In this updated release of PED,
we have now accumulated a total of 461 entries and 538 ensembles. This time, we also included IDP ensembles generated
without experimental data by novel ML and sampling methods from sequences. A new restyled website with an improved
user interface and novel features is presented, as well as a dedicated web-server for the ensemble’s deposition and curation.

Progress and new features
Database growth
PED aims to be the gold-standard primary deposition
database for conformational ensembles of non-globular proteins (NGPs) or regions. Therefore, the main goal of PED is to
provide an ever-growing platform of structural ensemble entries with a user-friendly deposition pipeline while maintaining high standards for data quality and the FAIR data principles. PED is cross-linked with the main resources to deposit
ensembles’ primary experimental data, including BRMB (26),
SASBDB (27) and PCDDB (28).
In this new release, the number of PED entries has increased
almost three times compared to the version presented in the
last publication (461 versus 162) (17). The source of this data
increment comes from depositions from data owners (42 entries in this release), ensembles generated without experimental data (61 entries in this release) and ensemble identification
by the PED biocurator team from databases and publications.
As detailed below, a larger number of NMR ensemble entries
were identified by an automated computational pipeline applied to BMRB (1409 protein structures), which were then
subsequently revised, filtered and published by the biocurators (totalling 189 entries).
New entries
Novel ensembles
As in previous releases, new PED ensembles were predominantly modeled using SAXS, NMR spectroscopy, FRET
data and their combinations (Figure 1A). NMR data included chemical shifts (CSs), nuclear Overhauser effects
(NOEs), J-couplings, residual dipolar couplings (RDCs), relaxation data and paramagnetic relaxation enhancements
(PREs) (29). On top of these, for a few new entries, methods such as electron paramagnetic resonance (EPR) spec-

D538

Figure 1. Experimental techniques and ensemble generation methods. (A) Matrix layout quantifies the combinations of experimental techniques for
PED entries, sorted by size. Filled circles in the matrix indicate which experimental measurement is part of the intersection. (B) Distribution of ensemble
generation methods and auxiliary software applied in PED. The X axis represents the number of PED entries.

troscopy techniques (e.g. double electron–electron resonance
(DEER)) and CD were also used to characterize the protein ensembles (30,31); often in combination with other techniques.
These combinations included EPR + NMR, EPR + SAXS,
EPR + NMR + SAXS, CD + NMR (30–32). NMR data have
already been cross-referenced from BMRB (26) and SAXS
data from SASBDB (27), but now CD data can also be crossreferenced from PCDDB (28), which will enable PED depositors during submission to reference their CD data already deposited in its primary resource.
Besides these experimental datasets, several PED depositions also used computationally expensive MD simulations to
perform integrative structural modeling by reweighting the ensembles. These MD simulations comprised among others trajectories generated by a CHARMM force field and the EEF1
implicit solvent model in a replica-exchange MD setup (33), or
AMBER03w force field with TIP4P/2005s water model (34),
or replica-exchange Discrete MD (DMD) using the MEDUSA
force field in implicit water (35), or coarse-grained Langevin
MD in multiple replicas (36), or AMBER99SB-disp force field
with it own water model using replica exchange with solute
tempering (37). Furthermore, the repertoire of ensemble generation methods and auxiliary software is continuously expanding to encompass state-of-the-art techniques in the field
(Figure 1B).

It is often emphasized that IDPs have a high-degree of conformational heterogeneity, which is harder to capture by a single technique. Therefore the integration of simulations and
various experiments can better characterize the highly dynamic nature of IDPs (38). Now, there is an increasing number
of IDP ensembles in PED determined by different combinations of techniques under the same or slightly different conditions, e.g. hnRNPA1, alpha-synuclein, Tau. We envisage that
these ensemble data will reveal not only how sensitive IDPs are
to environmental conditions but also the strengths and weaknesses of methods in capturing certain structural aspects.
NMR structural ensembles
A significant upgrade in the new PED version involves the inclusion of a large number of NMR structural ensembles comprising IDRs sourced from the PDB. These NMR ensembles
represent collections of different conformations (models) that
individually satisfy the experimentally derived constraints (8).
To achieve this, we systematically searched the MobiDB
(19) to identify NMR ensembles containing IDRs/IDPs. As
a starting point, we identified a subset of 2064 proteins containing large RMSD regions defined as ‘mobile’ in MobiDB.
Mobile regions are calculated for all NMR ensembles using
the Mobi software (39); it is an analogous definition to the

D539

presence of missing residues in X-ray structures. This feature
represents highly flexible regions based on structural superposition that change their local conformation in the NMR ensembles.
To further refine our dataset, we also consider the disorder content percentage of the proteins based on two criteria:
AlphaFold-disorder (40) and MobiDB-lite predictions (41).
Initially, we focused on proteins for which both predictors indicated a disorder content percentage exceeding 50%. In the
subsequent phase, we expanded our inclusion criteria to cover
proteins where at least one of these two predictors indicated
a disorder content percentage above 50%. During this stage,
we also verified the availability of experimental NMR data for
each protein in the BMRB database (26).
We then established three key criteria to determine the eligibility of NMR ensembles for inclusion in PED: (i) publication availability: we confirmed the existence of a corresponding publication; (ii) consistency in disorder prediction:
we ensured that a minimum of ten consecutive residues within
the mobile region were classified as disordered by AlphaFolddisorder and/or MobiDB-lite, the cutoff representing the minimum length of IDRs in DisProt; (iii) sufficient conformational
coverage: the NMR ensemble had to consist of at least ten distinct structures.
Ensembles without explicit experimental data
Given the recent advancements in ML algorithms for modeling protein structural dynamics (42) and in new methods for sampling IDP conformational ensembles (43,44), we
expanded PED and its controlled vocabulary (CV) (https:
//proteinensemble.org/about) to accommodate ensembles calculated without incorporating specific experimental data constraints.
The idpGAN generative model (22) was trained on coarsegrained molecular dynamics (MD) simulations (45) of IDRs
from the DisProt database. It is capable of rapidly generating
ensembles for arbitrary IDR sequences. IdpGAN does not incorporate experimental data in the ensemble-generation process and, for this update, we did not adopt any reweighting
scheme (4) to improve compatibility with the experimental
data of the entries. idpGAN was applied to a specific set of
sequences from the PED database, involving the careful selection of 47 entries meeting both idpGAN’s technical prerequisites and exhibiting a significant fraction of disorder. In
this context, idpGAN generated 1000 Cα-only conformers for
each selected entry, which were then converted into full allatom structures using the cg2all neural network (46). These
resulting structures underwent an energy minimization relaxation process similar to the one in AF predictions. For reproducibility, the entire pipeline was made accessible at https:
//github.com/feiglab/idpgan_ped.
We have also included fourteen ensembles generated with
the new IDPConformerGenerator software suite, which allows statistical or experimentally (chemical shift) biased sampling of torsion angles from the PDB to create all-atom
IDPs and IDRs (tails, linkers and loops) in the context of
full-length proteins containing folded domains (43,44). IDPConformerGenerator allows exploration of multiple torsionangle sampling methods that enrich the ensembles’ conformational diversity and account for post-translational modifications, multi-chain protein complexes, non-protein ligands
such as nucleic acids and lipid bilayers around membranebound proteins containing IDRs. The ensembles deposited

were assessed in the original publications (43,44). IDPConformerGenerator is open-source, fully documented with examples, and is accessible at https://github.com/julie-formankay-lab/IDPConformerGenerator.
PEDdeposition service
PED introduces a dedicated deposition user interface accessible to everyone. This service allows depositors to upload ensembles and metadata, calculate and visualize structural features, and assess ensemble quality through automated validation. Deposition of new ensembles into the PED can be described in three main stages: ensemble deposition by the user,
calculation of ensemble properties, and finally, manual curation by PED expert curators (Figure 2).
The initial step in submitting an ensemble involves user authentication through ORCID ID credentials. Within the deposition service, users encounter two primary sections: one
for creating a new ensemble draft and another for managing existing drafts. Additionally, the service offers an example
ensemble draft to help users become acquainted with the required deposition information. After creating a new draft, the
user can begin depositing information, which is organized into
three main tabs: description, ensemble upload and construct
definition.
Ensemble description
In the ‘Experimental procedure’ section, users can provide a
brief overview of the experimental techniques employed to determine the protein’s structural characteristics. The ‘Structural
ensemble calculation’ field captures computational methods, including software for pool generation, forward models and tools for fitting experimental observables with backcalculated measurements from predicted models, as well as
validation efforts on the ensemble. For ensembles generated
through MD/MC simulations, there is a specific section to detail simulation parameters like software, force field and water model, simulation duration, enhanced sampling, clustering of frames, etc. Additionally, the database offers a controlled vocabulary (CV) organized into an ontology to enhance searchability and standardize keywords describing experimental methodologies, ensemble generation and MD/MC
simulations. The last two sections in the ensemble description
focus on specifying the NCBI taxonomy ID of the expression
organism and providing cross-references to other databases,
including the BMRB, SASBDB, PCDDB, DisProt and IntAct
(47).

Upload
The upload section of the PEDdeposition service facilitates efficient submission of ensembles. Users can upload multiplemodel PDB files that contain the ensemble. Additionally, if
available, they can upload a tab-separated file containing
weights. These weights indicate the percentage contribution
of each conformer to the ensemble. The PED deposition service initiates a validation pipeline to ensure accurate data formatting. External tools like DSSP (48) and MolProbity (49)
are employed to compute essential parameters, including secondary structure propensity, accessible surface area, radius of
gyration, Ramachandran outliers and steric clash analysis. All
resultant data are made available for download.

D540

Figure 2. PEDdeposition service workflow. The workflow begins with the submission of an ensemble, which includes the description of both
experimental and computational components, the deposition of conformers and the specification of the protein construct via UniProt accessions and/or
protein sequence. The next step involves running the validation pipeline to evaluate the uploaded structures and generating insightful statistics through
tools such as MolProbity, DSSP and calculating the radius of gyration. At the final stage, the submitted ensemble entry undergoes a final review by
biocurators who determine whether to accept or reject it. Ultimately, approved ensembles are subsequently published on PED for public access.

Construct
Here, users define constructs corresponding to the deposited
protein or region. Constructs are assembled from ‘fragments’
which can be defined using UniProt accession numbers, isoform identifiers and regions. For engineered constructs, manual input of the sequence is also an option. The feature viewer
highlights deviations and modifications in the sequence, aiding in accurate definition.

Manual curation and validation
The final stage involves expert review and validation. The
PED deposition service distinguishes between general depositors and expert biocurators. Biocurators have access to a dashboard where all deposited ensembles are organized based on
their review status. Upon submission, deposited information
undergoes thorough review and validation. If accepted, the ensemble draft is prepared for release in the PED database; if not,

depositors are promptly informed of the reasons for rejection.
This automated process significantly reduces the time between
ensemble deposition and publication, streamlining the entire
workflow.

Implementation
The newly re-designed user interface (UI) provides a more
enriched user experience and notable features. A prominent
new addition to this UI version is a feature allowing users
to access supplementary data from the ensemble’s deposition
phase. This represents a departure from the traditional report in PDF format, as users can now leverage a multitude of
data assets available in CSV or JSON formats. This transition
empowers users to have more flexibility to access and work
with the ensemble data according to their particular needs.
Furthermore, these data assets are also available on an im-

D541

proved REST API for programmatic access. Constructed using the Django REST framework in Python, this REST API is
meticulously documented according to the OpenAPI 3.0 standard. This documentation is presented using Swagger UI, enabling users to interact with the API on the website (https:
//proteinensemble.org/api). The API allows users to selectively
download specific data of interest, providing programmatic
access to all PED data. PED also introduces a minor redesign
of the browse page by grouping proteins for each entry, mitigating redundancy during the exploration of the database content. Another feature in this new version is the integration of
PED in the 3D-Beacons (50), a network that provides programmatic access to macromolecular data from different data
resources, therefore PED data is now also available through
the 3D-Beacons API.
PED introduces a dedicated deposition interface that is
accessible to all users. This new service enables depositors
to measure the quality of their ensembles through an automated validation process utilizing calculations provided by
tools such as MolProbity and DSSP. These calculations are facilitated by our distributed system, efficiently managing the
computational workload through SLURM, enabling parallel
calculation of multiple ensembles. The results are delivered
in CSV and JSON formats, similar to the main user interface
mentioned earlier. The service is integrated with the ORCID
authentication service, utilizing the OpenID standard to verify user identity. This authentication allows users to track the
status of their uploaded ensembles, which will undergo manual validation by curators before being published in the main
database for public access. During this process, depositors
must provide an accurate description of their ensembles and
cross-reference them with other databases to enhance findability.

integrate coarse-grained (CG) ensembles into PED. Recently,
a pair of IDP force fields have emerged that efficiently generate CG models of random coil-like IDPs/IDRs and capture
the global characteristics of disordered proteins, such as the
radius of gyration (23,51–53). The integration of such models
into PED is long-awaited and has the potential to significantly
expand the number of available ensembles for IDPs/IDRs.
The need for a conceptual categorization of entries within
PED becomes increasingly important as we progress towards
incorporating ab-initio and NMR ensembles, and in the
near future, CG ensembles. Furthermore, by including predicted ensembles by diverse algorithms, we can facilitate the
benchmarking and comparison of various ensemble generation methods for IDPs. Recently, the rapid growth of DisProt enabled the design of two community benchmark efforts,
termed Critical Assessment of Protein Intrinsic Disorder prediction (CAID) challenge (website: https://caid.idpcentral.org/
challenge) (54–56). We envision that the consistent growth of
PED will also facilitate organizing a similar benchmark using
withheld high-quality ensemble data and promote the development of predictors for IDP structural ensembles.
The long-term sustainability of PED is ensured by its central role in various initiatives involving large communities
of bioinformaticians and structural biologists working in
the disordered proteins field. Such communities include the
‘ML4NGP’ COST Action and the ELIXIR IDP Community,
both of which foster collaboration and knowledge exchange
among experts.

Data availability
The data that support the findings of this study are openly
available in PED at https://proteinensemble.org/.

Conclusions and future work
Over the past 3 years, research on IDPs/IDRs has made significant progress, marked by the introduction of a diverse range
of novel computational, experimental and ML-derived techniques for resolving structural ensembles. In alignment with
the most recent advancements in this field, we remain devoted to customizing the database to the community’s needs.
Through a large community effort, the PED has experienced a
substantial increase in its repertoire, with a noteworthy rise in
the number of ensembles, entries and conformers. The repertoire has also expanded with an ever-growing range of different methods and their diverse combinations, recently enriched in EPR spectroscopy. Furthermore, we have integrated
NMR-derived ensembles of IDPs/IDRs into PED and generated structural ensembles using advanced ML and sampling
techniques without biasing them with experimental data.
Another key improvement in this release is the complete reimplementation and redesign of the PED deposition service.
This tool has evolved beyond its previous capabilities, and
now offers depositors a user-friendly, step-by-step workflow
for retaining their structural ensembles. Furthermore, it includes a fully automated validation pipeline that comprehensively assesses the structure file format and generates insightful
statistics. Additionally, the validation pipeline is now accessible as a standalone resource, enabling anyone interested to
assess the quality of structural ensembles independently.
Further developments must be made in the future to address
several key areas. To begin with, there is a need to smoothly

Funding
European Union’s Horizon 2020 research and innovation
programme [778247 MSCA-RISE ‘IDPfun’ and 823886
MSCA-RISE ‘REFRACT’]; ML4NGP CA21160 project
supported by COST (European Cooperation in Science
and Technology) under Horizon Europe; H.G. and M.C.A.
are funded by the European Union—NextGenerationEU
through ‘Italiadomani—PNRR’ projects ‘National Centre for HPC, Big Data and Quantum Computing’ [codice
identificativo MUR CN00000013, C93C22002800006];
‘National Center for Gene Therapy and Drugs based on
RNA Technology’ [codice fiscale 92315700283, codice
identificativo CN00000041]; ELIXIR, the research infrastructure for life-science data, and by the European
Union—NextGenerationEU
through
‘Italiadomani—
PNRR project IR000010 ‘ELIXIR × NextGenerationIT:
Consolidamento dell’Infrastruttura Italiana per i Dati
Omici e la Bioinformatica—ElixirxNextGenIT’ and
project ECS00000017 ‘THE—Tuscany Health Ecosystem’. T.L. is holder of a postdoctoral innovation mandate [HBC.2022.0194] by the Flanders Innovation &
Entrepreneurship Agency (VLAIO). Funding for open access charge: European Union’s Horizon 2020 research and
innovation programme [778247 MSCA-RISE “IDPfun” and
823886 MSCA-RISE “REFRACT”].

D542

Conflict of interest statement
None declared.

References
1. Tompa,P. and Fersht,A. (2009) Structure and Function of
Intrinsically Disordered Proteins. CRC Press.
2. Wang,H., Xiong,R. and Lai,L. (2016) Rational drug design
targeting intrinsically disordered proteins. WIREs Comput. Mol.
Sci., 11, 65–77.
3. Hatos,A., Monzon,A.M., Tosatto,S.C.E., Piovesan,D. and
Fuxreiter,M. (2021) FuzDB: a new phase in understanding fuzzy
interactions. Nucleic Acids Res., 50, D509–D517.
4. Bonomi,M., Heller,G.T., Camilloni,C. and Vendruscolo,M. (2017)
Principles of protein structural ensemble determination. Curr.
Opin. Struct. Biol., 42, 106–116.
5. PDBe-KB consortium (2022) PDBe-KB: collaboratively defining
the biological context of structural data. Nucleic Acids Res., 50,
D534–D542.
6. Varadi,M., Anyango,S., Deshpande,M., Nair,S., Natassia,C.,
Yordanova,G., Yuan,D., Stroe,O., Wood,G., Laydon,A., et al.
(2022) AlphaFold Protein Structure Database: massively
expanding the structural coverage of protein-sequence space with
high-accuracy models. Nucleic Acids Res., 50, D439–D444.
7. Varadi,M., Kosol,S., Lebrun,P., Valentini,E., Blackledge,M.,
Dunker,A.K., Felli,I.C., Forman-Kay,J.D., Kriwacki,R.W.,
Pierattelli,R., et al. (2014) pE-DB: a database of structural
ensembles of intrinsically disordered and of unfolded proteins.
Nucleic Acids Res., 42, D326–D335.
8. Sormanni,P., Piovesan,D., Heller,G.T., Bonomi,M., Kukic,P.,
Camilloni,C., Fuxreiter,M., Dosztanyi,Z., Pappu,R.V., Babu,M.M.,
et al. (2017) Simultaneous quantification of protein order and
disorder. Nat. Chem. Biol., 13, 339–342.
9. Jumper,J., Evans,R., Pritzel,A., Green,T., Figurnov,M.,
Ronneberger,O., Tunyasuvunakool,K., Bates,R., Žídek,A.,
Potapenko,A., et al. (2021) Highly accurate protein structure
prediction with AlphaFold. Nature, 596, 583–589.
10. Baek,M., DiMaio,F., Anishchenko,I., Dauparas,J., Ovchinnikov,S.,
Lee,G.R., Wang,J., Cong,Q., Kinch,L.N., Schaeffer,R.D., et al.
(2021) Accurate prediction of protein structures and interactions
using a three-track neural network. Science, 373, 871–876.
11. Sala,D., Engelberger,F., Mchaourab,H.S. and Meiler,J. (2023)
Modeling conformational states of proteins with AlphaFold. Curr.
Opin. Struct. Biol., 81, 102645.
12. Del Alamo,D., Sala,D., Mchaourab,H.S. and Meiler,J. (2022)
Sampling alternative conformational states of transporters and
receptors with AlphaFold2. eLife, 11, e75751.
13. Stein,R.A. and Mchaourab,H.S. (2022) SPEACH_AF: sampling
protein ensembles and conformational heterogeneity with
Alphafold2. PLoS Comput. Biol., 18, e1010483.
14. Henriques,J., Cragnell,C. and Skepö,M. (2015) Molecular
dynamics simulations of intrinsically disordered proteins: force
field evaluation and comparison with experiment. J. Chem. Theory
Comput., 11, 3420–3431.
15. Rauscher,S., Gapsys,V., Gajda,M.J., Zweckstetter,M., de
Groot,B.L. and Grubmüller,H. (2015) Structural ensembles of
intrinsically disordered proteins depend strongly on force field: a
comparison to experiment. J. Chem. Theory Comput., 11,
5513–5524.
16. Abrams,C. and Bussi,G. (2014) Enhanced sampling in molecular
dynamics using metadynamics, replica-exchange, and
temperature-acceleration. Entropy, 16, 163–199.
17. Lazar,T., Martínez-Pérez,E., Quaglia,F., Hatos,A., Chemes,L.B.,
Iserte,J.A., Méndez,N.A., Garrone,N.A., Saldaño,T.E., Marchetti,J.,
et al. (2021) PED in 2021: a major update of the protein ensemble
database for intrinsically disordered proteins. Nucleic Acids Res.,
49, D404–D411.

18. Hatos,A., Hajdu-Soltész,B., Monzon,A.M., Palopoli,N., Álvarez,L.,
Aykac-Fas,B., Bassot,C., Benítez,G.I., Bevilacqua,M., Chasapi,A.,
et al. (2020) DisProt: intrinsic protein disorder annotation in
2020. Nucleic Acids Res., 48, D269–D276.
19. Piovesan,D., Del Conte,A., Clementel,D., Monzon,A.M.,
Bevilacqua,M., Aspromonte,M.C., Iserte,J.A., Orti,F.E.,
Marino-Buslje,C. and Tosatto,S.C.E. (2023) MobiDB: 10 years of
intrinsically disordered proteins. Nucleic Acids Res., 51,
D438–D444.
20. Fukuchi,S., Amemiya,T., Sakamoto,S., Nobe,Y., Hosoda,K.,
Kado,Y., Murakami,S.D., Koike,R., Hiroaki,H. and Ota,M. (2014)
IDEAL in 2014 illustrates interaction networks composed of
intrinsically disordered proteins and their binding partners.
Nucleic Acids Res., 42, D320–D325.
21. Lindorff-Larsen,K. and Kragelund,B.B. (2021) On the potential of
machine learning to examine the relationship between sequence,
structure, dynamics and function of intrinsically disordered
proteins. J. Mol. Biol., 433, 167196.
22. Janson,G., Valdes-Garcia,G., Heo,L. and Feig,M. (2023) Direct
generation of protein conformational ensembles via machine
learning. Nat. Commun., 14, 774.
23. Tesei,G., Trolle,A.I., Jonsson,N., Betz,J., Pesce,F., Johansson,K.E.
and Lindorff-Larsen,K. (2023) Conformational ensembles of the
human intrinsically disordered proteome: bridging chain
compaction with function and sequence conservation. .
24. González-Delgado,J., Sagar,A., Zanon,C., Lindorff-Larsen,K.,
Bernadó,P., Neuvial,P. and Cortés,J. (2023) WASCO: a
Wasserstein-based statistical tool to compare conformational
ensembles of intrinsically disordered proteins. J. Mol. Biol., 435,
168053.
25. Lazar,T., Guharoy,M., Vranken,W., Rauscher,S., Wodak,S.J. and
Tompa,P. (2020) Distance-based metrics for comparing
conformational ensembles of intrinsically disordered proteins.
Biophys. J., 118, 2952–2965.
26. Romero,P.R., Kobayashi,N., Wedell,J.R., Baskaran,K., Iwata,T.,
Yokochi,M., Maziuk,D., Yao,H., Fujiwara,T., Kurusu,G., et al.
(2020) BioMagResBank (BMRB) as a Resource for Structural
Biology. Methods Mol. Biol. Clifton NJ, 2112, 187–218.
27. Kikhney,A.G., Borges,C.R., Molodenskiy,D.S., Jeffries,C.M. and
Svergun,D.I. (2020) SASBDB: towards an automatically curated
and validated repository for biological scattering data. Protein Sci.,
29, 66–75.
28. Ramalli,S.G., Miles,A.J., Janes,R.W. and Wallace,B.A. (2022) The
PCDDB (Protein Circular Dichroism Data Bank): a Bioinformatics
Resource for Protein Characterisations and Methods
Development. J. Mol. Biol., 434, 167441.
29. Felli,I.C. and Pierattelli,R. (2015) Intrinsically Disordered Proteins
Studied by NMR Spectroscopy. Springer, Cham.
30. Ritsch,I., Lehmann,E., Emmanouilidis,L., Yulikov,M., Allain,F. and
Jeschke,G. (2022) Phase separation of heterogeneous nuclear
ribonucleoprotein A1 upon specific RNA-binding observed by
magnetic resonance. Angew. Chem. Int. Ed. Engl., 61,
e202204311.
31. Galano-Frutos,J.J., Torreblanca,R., García-Cebollada,H. and
Sancho,J. (2022) A look at the face of the molten globule:
structural model of the Helicobacter pylori apoflavodoxin
ensemble at acidic pH. Protein Sci. Publ. Protein Soc., 31, e4445.
32. Rao,J.N., Jao,C.C., Hegde,B.G., Langen,R. and Ulmer,T.S. (2010)
A combinatorial NMR and EPR approach for evaluating the
structural ensemble of partially folded proteins. J. Am. Chem. Soc.,
132, 8657–8668.
33. Fisher,C.K., Huang,A. and Stultz,C.M. (2010) Modeling
intrinsically disordered proteins with bayesian statistics. J. Am.
Chem. Soc., 132, 14919–14927.
34. Chan-Yao-Chong,M., Marsin,S., Quevillon-Cheruel,S., Durand,D.
and Ha-Duong,T. (2020) Structural ensemble and biological
activity of DciA intrinsically disordered region. J. Struct. Biol.,
212, 107573.

D543

35. Chen,J., Zaer,S., Drori,P., Zamel,J., Joron,K., Kalisman,N.,
Lerner,E. and Dokholyan,N.V. (2021) The structural heterogeneity
of α-synuclein is governed by several distinct subpopulations with
interconversion times slower than milliseconds. Structure, 29,
1048–1064.
36. Bjarnason,S., McIvor,J.A.P., Prestel,A., Demény,K.S.,
Bullerjahn,J.T., Kragelund,B.B., Mercadante,D. and
Heidarsson,P.O. (2023) DNA binding redistributes activation
domain ensemble and accessibility in pioneer factor Sox2. bioRxiv
doi: https://doi.org/10.1101/2023.06.16.545083, 16 June 2023,
preprint: not peer reviewed.
37. Zhu,J., Salvatella,X. and Robustelli,P. (2022) Small molecules
targeting the disordered transactivation domain of the androgen
receptor induce the formation of collapsed helical states. Nat.
Commun., 13, 6390.
38. Gomes,G.-N.W., Krzeminski,M., Namini,A., Martin,E.W.,
Mittag,T., Head-Gordon,T., Forman-Kay,J.D. and Gradinaru,C.C.
(2020) Conformational Ensembles of an Intrinsically Disordered
Protein Consistent with NMR, SAXS, and Single-Molecule FRET.
J. Am. Chem. Soc., 142, 15697–15710.
39. Piovesan,D. and Tosatto,S.C.E. (2018) Mobi 2.0: an improved
method to define intrinsic disorder, mobility and linear binding
regions in protein structures. Bioinforma. Oxf. Engl., 34, 122–123.
40. Piovesan,D., Monzon,A.M. and Tosatto,S.C.E. (2022) Intrinsic
protein disorder and conditional folding in AlphaFoldDB. Protein
Sci. Publ. Protein Soc., 31, e4466.
41. Necci,M., Piovesan,D., Clementel,D., Dosztányi,Z. and
Tosatto,S.C.E. (2020) MobiDB-lite 3.0: fast consensus annotation
of intrinsic disorder flavours in proteins. Bioinforma. Oxf. Engl.,
36, 5533–5534.
42. Zheng,L.-E., Barethiya,S., Nordquist,E. and Chen,J. (2023)
Machine learning generation of dynamic protein conformational
ensembles. Mol. Basel Switz., 28, 4047.
43. Teixeira,J.M.C., Liu,Z.H., Namini,A., Li,J., Vernon,R.M.,
Krzeminski,M., Shamandy,A.A., Zhang,O., Haghighatlari,M.,
Yu,L., et al. (2022) IDPConformerGenerator: a flexible software
suite for sampling the conformational space of disordered protein
states. J. Phys. Chem. A, 126, 5985–6003.
44. Liu,Z.H., Teixeira,J.M.C., Zhang,O., Tsangaris,T.E., Li,J.,
Gradinaru,C.C., Head-Gordon,T. and Forman-Kay,J.D. (2023)
Local disordered region sampling (LDRS) for ensemble modeling
of proteins with experimentally undetermined or low confidence
prediction segments. bioRxiv doi:
https://doi.org/10.1101/2023.07.25.550520, 27 July
2023,preprint: not peer reviewed.
45. Valdes-Garcia,G., Heo,L., Lapidus,L.J. and Feig,M. (2023)
Modeling concentration-dependent phase separation processes
involving peptides and RNA via residue-based coarse-graining. J.
Chem. Theory Comput., 19, 669–678.
46. Heo,L. and Feig,M. (2023) One particle per residue is sufficient to
describe all-atom protein structures. bioRxiv doi:
https://doi.org/10.1101/2023.05.22.541652, 23 May 2023,
preprint: not peer reviewed.
47. del Toro,N., Shrivastava,A., Ragueneau,E., Meldal,B., Combe,C.,
Barrera,E., Perfetto,L., How,K., Ratan,P., Shirodkar,G., et al.
(2021) The IntAct database: efficient access to fine-grained
molecular interaction data. Nucleic Acids Res., 50D648–D653.
48. Kabsch,W. and Sander,C. (1983) Dictionary of protein secondary
structure: pattern recognition of hydrogen-bonded and
geometrical features. Biopolymers, 22, 2577–2637.
49. Williams,C.J., Headd,J.J., Moriarty,N.W., Prisant,M.G.,
Videau,L.L., Deis,L.N., Verma,V., Keedy,D.A., Hintze,B.J.,
Chen,V.B., et al. (2018) MolProbity: more and better reference
data for improved all-atom structure validation. Protein Sci. Publ.
Protein Soc., 27, 293–315.
50. Varadi,M., Nair,S., Sillitoe,I., Tauriello,G., Anyango,S., Bienert,S.,
Borges,C., Deshpande,M., Green,T., Hassabis,D., et al. (2022)
3D-Beacons: decreasing the gap between protein sequences and

structures through a federated network of protein structure data
resources. GigaScience, 11, giac118.
51. Klein,F., Barrera,E.E. and Pantano,S. (2021) Assessing SIRAH’s
capability to simulate intrinsically disordered proteins and
peptides. J. Chem. Theory Comput., 17, 599–604.
52. Thomasen,F.E., Pesce,F., Roesgaard,M.A., Tesei,G. and
Lindorff-Larsen,K. (2022) Improving Martini 3 for disordered and
multidomain proteins. J. Chem. Theory Comput., 18, 2033–2041.
53. Fagerberg,E. and Skepö,M. (2023) Comparative performance of
computer simulation models of intrinsically disordered proteins at
different levels of coarse-graining. J. Chem. Inf. Model., 63,
4079–4087.
54. Necci,M., Piovesan,D., Predictors,C.A.I.D., Curators,D.P. and
Tosatto,S.C.E. (2021) Critical assessment of protein intrinsic
disorder prediction. Nat. Methods, 18, 472–481.
55. Conte,A.D., Mehdiabadi,M., Bouhraoua,A., Miguel Monzon,A.,
Tosatto,S.C.E. and Piovesan,D. (2023) Critical assessment of
protein intrinsic disorder prediction (CAID) - Results of round 2.
Proteins Struct. Funct. Bioinforma.,
https://doi.org/10.1002/prot.26582.
56. Del Conte,A., Bouhraoua,A., Mehdiabadi,M., Clementel,D.,
Monzon,A.M. and CAID predictorsCAID predictors,
Tosatto,S.C.E. and Piovesan,D. (2023) CAID prediction portal: a
comprehensive service for predicting intrinsic disorder and binding
regions in proteins. Nucleic Acids Res., 51, W62–W69.

Appendix
PED Consortium
Maria C. Aspromonte1 , Pau Bernadó6 , Belén ChavesArquero7 , Lucia Beatriz Chemes8 , Damiano Clementel1 ,
Tiago N. Cordeiro9 , Carlos A. Elena-Real6 , Michael
Feig10 , Isabella C. Felli11 , Carlo Ferrari5 , Julie D. FormanKay12,13 , Tiago Gomes9,26 , Frank Gondelaud14 , Claudiu
C. Gradinaru15,16 , Tâp Ha-Duong17 , Teresa HeadGordon18,19,20,21 , Pétur O. Heidarsson22 , Giacomo Janson10 ,
Gunnar Jeschke23 , Emanuela Leonardi1 , Zi Hao Liu12,13 ,
Sonia Longhi14 , Xamuel L. Lund6,24 , Maria J Macias25,26 ,
Pau Martin-Malpartida26 , Davide Mercadante27 , Assia
Mouhand6 , Gabor Nagy28 , María Victoria Nugnes1 ,
José Manuel Pérez-Cañadillas29 , Giulia Pesce14 , Roberta
Pierattelli11 , Damiano Piovesan1 , Federica Quaglia1,30 , Sylvie
Ricard-Blum31 , Paul Robustelli32 , Amin Sagar6 , Edoardo
Salladini33 , Lucile Sénicourt6 , Nathalie Sibille6 , João M. C.
Teixeira12 , Thomas E. Tsangaris15,16 , Mihaly Varadi34
Centre de Biologie Structurale (CBS), Université de Montpellier, INSERM, CNRS
Centro de Investigaciones Biológicas Margarita Salas
(CIB), CSIC, 28040 Madrid, Spain
Instituto de Investigaciones Biotecnológicas, Universidad
Nacional de San Martín (UNSAM) – Consejo Nacional de Investigaciones Científicas y Técnicas (CONICET), San Martín,
Argentina
Instituto de Tecnologia Química e Biológica António
Xavier, Universidade Nova de Lisboa, Oeiras, Portugal
Department of Biochemistry and Molecular Biology,
Michigan State University, USA
Department of Chemistry ‘Ugo Schiff’ and Magnetic Resonance Center (CERM), University of Florence, Florence, Italy
Molecular Medicine Program, The Hospital for Sick
Children, Toronto, Ontario Canada
Department of Biochemistry, University of Toronto,
Toronto, Ontario, Canada
Lab. Architecture et Fonction des Macromolécules Biologiques (AFMB), UMR 7257, Aix Marseille University and

D544
Centre National de la Recherche Scientifique (CNRS), 163 Avenue de Luminy, Case 932, 13288, Marseille, FRANCE
Department of Physics, University of Toronto, Toronto,
Ontario M5S 1A7, Canada
Department of Chemical & Physical Sciences, University of Toronto Mississauga, Mississauga, Ontario L5L 1C6,
Canada
BioCIS, CNRS, Université Paris-Saclay, France
Kenneth S. Pitzer Center for Theoretical Chemistry, University of California, Berkeley, California, USA
Department of Chemistry, University of California,
Berkeley, California, USA
Department of Chemical and Biomolecular Engineering,
University of California, Berkeley, California, USA
Department of Bioengineering, University of California,
Berkeley, California, USA
Department of Biochemistry, Science Institute, University
of Iceland, Reykjavík, Iceland
Department of Chemistry and Applied Biosciences, ETH
Zürich, Zürich, Switzerland
Institut Laue-Langevin, 71 avenue de Martyrs, Grenoble
38042, France
Institució Catalana de Recerca i Estudis Avançats
(ICREA), Passeig Lluís Companys 23, Barcelona 08010, Spain

Institute for Research in Biomedicine, The Barcelona
Institute of Science and Technology, Baldiri Reixac, 10,
Barcelona 08028, Spain
School of Chemical Sciences, The University of Auckland, Auckland, New Zealand
Department of Theoretical and Computational Biophysics, Max Planck Institute for Biophysical Chemistry, D37077 Göttingen, Germany
Instituto de Química Física ‘Blas Cabrera’, Consejo Superior de Investigaciones Científicas (CSIC), Madrid, Spain
Institute of Biomembranes, Bioenergetics and Molecular
Biotechnologies, National Research Council (CNR-IBIOM),
Bari, Italy
University Lyon 1, ICBMS, UMR 5246 CNRS, Villeurbanne, France
Department of Chemistry, Dartmouth College, New
Hampshire, USA
Department of Drug Science and Technology, Università
degli Studi di Torino, Torino, Italy
Protein Data Bank in Europe, European Molecular Biology Laboratory, European Bioinformatics Institute (EMBLEBI), Wellcome

Received: September 15, 2023. Revised: October 10, 2023. Editorial Decision: October 11, 2023. Accepted: October 13, 2023
© The Author(s) 2023. Published by Oxford University Press on behalf of Nucleic Acids Research.
This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse,
distribution, and reproduction in any medium, provided the original work is properly cited.


---

# Scalable emulation of protein equilibrium ensembles with generative deep learning

**Authors:** Sarah Lewis, Tim Hempel, José Jiménez-Luna, Michael Gastegger, Yu Xie, Andrew Y. K. Foong, et al.
**Year:** 2025
**Venue:** Science
**DOI:** 10.1126/science.adv9817
**Source PDF URL:** https://www.biorxiv.org/content/10.1101/2024.12.05.626885v1.full.pdf (bioRxiv preprint; Science version is closed access, oa_status=closed per OpenAlex)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Scalable emulation of protein equilibrium ensembles with
generative deep learning
Sarah Lewis1† , Tim Hempel1† , José Jiménez-Luna1† , Michael Gastegger1† , Yu Xie1† ,
Andrew Y. K. Foong1† , Victor Garcı́a Satorras1† , Osama Abdin1† ,
Bastiaan S. Veeling1† , Iryna Zaporozhets1,2 , Yaoyi Chen1,2 , Soojung Yang1 ,
Arne Schneuing1 , Jigyasa Nigam1 , Federico Barbero1 , Vincent Stimper1 ,
Andrew Campbell1 , Jason Yim1 , Marten Lienen1 , Yu Shi1 , Shuxin Zheng1 ,
Hannes Schulz1 , Usman Munir1 , Cecilia Clementi1,2 , Frank Noé1,*
1 AI for Science, Microsoft Research.
2 Freie Universität Berlin, Department of Physics, Arnimallee 12, 14195 Berlin.
* Correspondance to franknoe@microsoft.com.

† These authors contributed equally to this work.

Abstract
Following the sequence and structure revolutions, predicting the dynamical mechanisms of proteins that
implement biological function remains an outstanding scientific challenge. Several experimental techniques
and molecular dynamics (MD) simulations can, in principle, determine conformational states, binding configurations and their probabilities, but suffer from low throughput. Here we develop a Biomolecular Emulator
(BioEmu), a generative deep learning system that can generate thousands of statistically independent samples
from the protein structure ensemble per hour on a single graphical processing unit. By leveraging novel training methods and vast data of protein structures, over 200 milliseconds of MD simulation, and experimental
protein stabilities, BioEmu’s protein ensembles represent equilibrium in a range of challenging and practically
relevant metrics. Qualitatively, BioEmu samples many functionally relevant conformational changes, ranging
from formation of cryptic pockets, over unfolding of specific protein regions, to large-scale domain rearrangements. Quantitatively, BioEmu samples protein conformations with relative free energy errors around
1 kcal/mol, as validated against millisecond-timescale MD simulation and experimentally-measured protein stabilities. By simultaneously emulating structural ensembles and thermodynamic properties, BioEmu
reveals mechanistic insights, such as the causes for fold destabilization of mutants, and can efficiently provide
experimentally-testable hypotheses.

1 Introduction
Proteins and protein complexes constitute the functional building blocks of life and are at the center stage of drug
development, enzymatic catalysis, biotechnological processes and biomaterials. Consequently, understanding
how proteins work and how their function can be regulated or designed is one of the grand challenges in science
and technology. Protein science can be characterized by three pillars of understanding: sequence, structure, and
function. Next-generation sequencing has made it possible to acquire the protein sequences of entire genomes at
low cost, while AlphaFold [1] and similar models [2–4] have built upon the decades of data accumulated in the

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Protein Data Bank (PDB) [5] to predict 3D protein structures that in many cases match experimental accuracy
within minutes. For protein function, unfortunately, methods that are both highly accurate and high-throughput
are missing, and thus our understanding of how proteins work remains anecdotal.
Functional descriptions such as “actin builds up muscle fibers” are human-made attributions that arise from
objectively measurable mechanistic properties: (i) What are the conformational states (i.e., sets of different
structures) a protein can be in? (ii) Which other molecules can a protein bind to in these different conformations?
(iii) What is the probability of these conformational and binding states at a given set of experimental conditions?
For example, actin exists in multiple conformational and binding states that are regulated by its cofactors
ATP/ADP (Fig. 1a), providing the molecular basis of muscle growth.
Available technologies that probe such conformational and binding states and their probabilities at high
accuracy are currently not scalable. Single-molecule experiments can provide the full equilibrium distributions of
observables such as intramolecular distances [6], but require bespoke molecular constructs and time-consuming
data collection. Cryo-electron microscopy can resolve multiple conformational states of biomolecular complexes
along with their probabilities [7], but running these experiments is costly both from a monetary and time
perspective. Molecular Dynamics (MD) simulation is, in principle, a universal tool that allows both structure
and dynamics of biomolecules to be explored at all-atom resolution. However, biomolecular forcefields are far
from perfect and the sampling problem renders the study of protein folding or association via MD a feat of
epic computational costs for small-sized proteins, even if special-purpose supercomputers or enhanced sampling
methods are employed [8, 9]. Machine-learned coarse-grained MD models have an opportunity to achieve similar
accuracy as all-atom MD at 2-3 orders of magnitude lower computational cost [10, 11] but are still under
development.
The grand challenge to complete our understanding of protein function thus motivates the development of a
technology that can help elucidate protein conformational states and binding states, as well as their associated
probabilities. This technology should ideally achieve an accuracy comparable to a converged MD simulation, or a
cryo-EM experiment with multi-conformation analysis, but it should only require a few hours of wall-clock time
and cost no more than a few dollars per experiment. Generative systems, such as Boltzmann Generators [12]
(BGs), which can efficiently sample arbitrarily-defined equilibrium distributions, indicate that such technologies
may be within reach, but are difficult to scale to large proteins. Concurrently, diffusion models and similar
approaches are now widely used in protein structure prediction and design [2, 3]. Such models [13–15], as
well as perturbation-based derivatives of AlphaFold [16, 17] have also been shown to be capable of generating
distinct protein structures and can be combined with MD simulation to alleviate the sampling problem [18].
As yet, generative ML systems have mainly demonstrated an ability to qualitatively sample distinct protein
conformational states. A demonstration that generative ML can quantitatively match equilibrium ensembles
and predict experimental observables is critical going forward [19].
Here we set out to develop a first version of an ML system that can approximately sample from the equilibrium distribution of protein conformations within a few GPU-hours per experiment — a biomolecular
emulator (BioEmu). The biggest challenge in training such a generative model is that no single high-quality
data source for training exists due to the aforementioned challenges with experimental methods and MD. We
therefore train BioEmu by combining data ranging from a large set of static protein structures and vast amounts
of MD simulation to experimental measurements of protein stabilities. We validate the system on a range of
tasks: (i) the prediction of protein conformational changes including large domain motions, local unfolding, and
the formation of cryptic binding pockets, (ii) the emulation of equilibrium distributions that can be generated by
high-throughput MD simulation, and (iii) the prediction of experimentally-measured stabilities of folded states
of small proteins by directly generating equilibrium ensembles and explaining structure-stability relationships
of mutants. We demonstrate that free energies can be predicted with errors below 1 kcal/mol and are therefore
on the order of experimental accuracy.
Given its versatility and efficiency, we believe that BioEmu has a variety of practical use cases, ranging
from helping with current MD simulation workflows, the interpretation of protein experiments, identification of
binding pockets and allosteric mechanisms in drug discovery, and generation of ensembles for dynamical protein
design. Importantly, our demonstration that the large upfront costs of MD simulation and experimental data
generation can be amortized and the prediction error decreases with an increasing amount of diverse training
data indicates a path forward for predicting biomolecular function at genomic scale.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

a) Actin example

ADP

c) Score model

ATP
Free energy landscape

O
pe

ni

ng

Cl
o

s in

Score model
Diffusion
timestep t

g

open

closed

Node feat.

Single Repr.

Invariant
point
attention

Pair Repr.

8 blocks

Net cycle due
to energy input
Dissociation

Node feat.
MLP

Single steps are
equilibrium processes

Binding

Score st

ATP hydrolysis

Backbone
frames xt

SDE Integrator

Backbone
frames xt-dt

b) Biomolecular Emulator (BioEmu)

F S T A V H P L

F S T A V H P L
F A T A V H P L
F S T A I H P L
F T T A V Q P L

Evoformer

MSA

F S T A V H P L

Pairing

blocks

F S T A V H P L

Input sequence S

Genetic
database
search

Equilibrium
distribution

Denoising diffusion model

Protein sequence encoding

q(xt-dt|xt)

Single
Repr.
xT

... x

xt

t-dt

...

Structure-based
drug design

score model
+ noise
s(xt)

x ⇠ p(x|S)
<latexit sha1_base64="TkWXXp5mH4fVRhBAmqY0VBPnUCU=">AAAB+HicbVBNT8JAEJ36ifhB1aOXjcQEL6Q1Bj0SvXjEKB8JNGS7bGHDdtvsbg1Y+SVePGiMV3+KN/+NC/Sg4EsmeXlvJjPz/JgzpR3n21pZXVvf2Mxt5bd3dvcK9v5BQ0WJJLROIh7Jlo8V5UzQumaa01YsKQ59Tpv+8HrqNx+oVCwS93ocUy/EfcECRrA2UtcujFBHsRDFpRF6QnenXbvolJ0Z0DJxM1KEDLWu/dXpRSQJqdCEY6XarhNrL8VSM8LpJN9JFI0xGeI+bRsqcEiVl84On6ATo/RQEElTQqOZ+nsixaFS49A3nSHWA7XoTcX/vHaig0svZSJONBVkvihIONIRmqaAekxSovnYEEwkM7ciMsASE22yypsQ3MWXl0njrOxWypXb82L1KosjB0dwDCVw4QKqcAM1qAOBBJ7hFd6sR+vFerc+5q0rVjZzCH9gff4A3qiR8Q==</latexit>

d) Pretraining
200 M AFDB
structures
Preprocessing
Diffusion
model training

Protein stabilities

Diffusion
model training

Property- prediction
fine-tuning

Finetuned
Model

200 M AFDB struct.
mmseq +
filtering
1.4 M seq. clusters
foldseek +
filtering
50 K seq. clusters
w. diverse structures
multi-struct.
augmentation
Aug. cluster AFDB

Pretrained distribution

Centroid
sequence

xT
predict

xT-k dt

...

Pretrained
Model

Reweighted MD

Predict properties
DG = 3.5 kcal/mol

f) Property-prediction fine-tuning

e) AFDB preprocessing

750 K exp. protein
stabilities
Subsampling

...

Aug. cluster AFDB

Finetuning
> 200 ms MD
simulations
Reweighting

Understand
molecular
mechanisms

x0

p(xt|xt-dt)
Pair
Repr.

Applications

backprop
x0

classify
folded

unfolded

Property
prediction loss

Experimental data
DG = 3.5 kcal/mol

MD distribution Equilibrium distribution

Fig. 1 Overview of model and architecture. a) Actin conformational changes and filament formation / dissociation as an example
for the mechanistic basis of protein function. b) ML model architecture consisting of protein sequence encoder and denoising
diffusion model. The diffusion model samples coarse-grained protein structures from an approximate equilibrium distribution, from
which properties such as free energy differences can be computed. c) Architecture of the score model used in the denoising diffusion
model. d) Data integration and model training pipeline. e) Data processing pipeline for pretraining. f) Experimental property
training for finetuning.

2 Model
BioEmu uses a similar model architecture as Distributional Graphormer [13], but with a significantly different
training approach. Starting from the input protein sequence, single and pair representations of the sequence
are computed using the AlphaFold2 evoformer [1]. These sequence representations serve as input to a denoising
diffusion model that generates protein structures (Fig. 1b,c; Sec. S.2). Sequence encoding is invoked only once per
protein, and using a second-order integration scheme we generate protein structures in as few as 100 denoising
steps (Sec. S.2.3), leading to high sampling efficiency: 10,000 independent protein structures from the learned
equilibrium distribution can be sampled within minutes to a few hours on a single GPU, depending on their size.
For model training and testing we have developed several new benchmarks and training methods to integrate
the heterogeneous data modalities (Sec. S.1, S.3). BioEmu is pretrained on a clustered version of the AlphaFold
database (AFDB), using a data augmentation strategy that incentivizes it to sample diverse conformations
(Fig. 1d,e, Sec. S.3.2). Starting from this pretrained model, we then continue to train on a mixture of MD data
and experimental measurements of protein stability, plus occasional examples from the pretraining data. We
have curated and generated a total of over 200 milliseconds of all-atom MD data for small-to-medium proteins

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

(Sec. S.3). To mitigate the sampling problem, MD data was reweighed towards equilibrium using either Markov
State Models [20], or weights from experimental data (see S.3.5.3), when possible. The reweighed MD data is
used in a second training stage of the model (Fig. 1d). The experimental measurements of protein stability
that we train on are a subset of the MEGAscale dataset [21], which comprises on the order of a million protein
stability measurements (Fig. 1d). As the MEGAscale dataset does not contain structures, we developed an new
algorithm called property-prediction fine-tuning (PPFT) to efficiently incorporate experimental measurements
into diffusion model training (Fig. 1f, Sec. S.3.6). Finally, to evaluate generalization, we filter our training set such
that no protein has more than 40% sequence similarity to any of the reported test proteins of at least 20 residues
or longer. The model name BioEmu denotes the fine-tuned model, trained on AFDB, MD simulations and
experimental measurements of protein stability. Subsequent results use this model unless otherwise described.

3 Sampling conformational changes related to protein function
We regard the ability to sample distinct biologically relevant conformations qualitatively as a basis to build a
quantitative equilibrium sampler. Therefore we first test qualitatively if BioEmu’s samples include known conformational changes and compare this capability with AFCluster [16] and AlphaFlow [14] as two representative
baseline methods. Towards this goal, we defined a challenging test set of conformational changes, called OOD60,
with a maximum of 60% and 40% sequence similarity to the AlphaFold2 monomer model and our training sets,
respectively. Due to the strict sequence similarity constraints, OOD60 only contains 19 proteins, but it features
various challenging cases like large-scale conformational changes caused by binding to other biomolecules (Fig.
S1). While it is uncertain if all of these conformational changes can be predicted by a single-domain model,
the benchmark tests for strong generalization and we find that our model significantly outperforms the two
considered baseline approaches (Fig. S5a).
In order to evaluate the multi-conformation capabilities of our model more exhaustively, we have also curated
a set of around 100 proteins that engage in experimentally-validated domain motions, local unfolding transitions,
or cryptic pocket formation. These include some proteins contained in OOD60 as well as proteins that overlap
with the AlphaFold2 training set. We confirmed that the model’s performance is similar for proteins that overlap
with the AlphaFold2 training set and those that do not, indicating that the benchmark does not test capabilities
that the model trivially extracted from evoformer embeddings (Table S4). Furthermore, BioEmu outperforms
other methods except for the apo states in the cryptic pocket benchmark, and the difference is especially large
for the proteins outside the AlphaFold2 training set (Fig. S5, b-d).
Our curated benchmark furthermore demonstrates that our model qualitatively captures functionally relevant protein conformations. For example, proteins can undergo large-scale domain motions as part of their
functional cycle. In the open-close transition of Adenylate Kinase, the closed state brings the substrates together
to catalyze the ATP + AMP ⇌ 2ADP reaction. Single-molecule experiments have confirmed that opening and
closing occurs reversibly on timescales of tens of microseconds when the substrates are bound [22]. BioEmu predicts a range of open and closed states, including close matches with crystallographic structures (Fig. 2a,i). A
second example is the open-close transition of LAO-binding protein which is required to bind and release lysine,
arginine and ornithine for transport across membranes as part of the ATP-binding cassette protein family (Fig.
2a,ii). Another interesting example of domain motions is that of the receptor module which regulates the concentration of cyclic di-GMP in bacteria. In this case one domain undergoes a large-scale rotation and repacks to
the other domain with a completely different contact pattern (Fig. 2a, iii). See Fig. S2 for 15 further examples.
Overall, BioEmu predicts 85% of the reference experimental structures with ≤3 Å RMSD (Fig. 2a), indicating
the model’s ability to predict which protein regions are more or less flexible, as well as which resulting motions
can occur.
Next we consider local unfolding transitions, in which part of a protein chain unfolds or detaches from its
main structure as part of a signaling pathway. Predicting local unfolding is arguably more challenging than
predicting domain motions, as it requires the model to correctly rank which parts of a protein’s fold are more
stable. A famous example of local unfolding is Ras p21, a conformational switch which signals cell growth and
whose mutants are often linked to cancer development [23] (Fig. 2b,i). In its active state, stabilized by GDP
binding, the Switch II region forms a short alpha-helix, which partially unfolds in the inactive state stabilized
by GTP. Rhomboid intramembrane protease (Fig. 2b,ii) is a much more complex case of domain swapping. Its

1ake
0.1% RMSD: 1.87 A

ii) LAO-binding protein
6ml0

iii) c-di-GMP receptor
module
6pwj

RMSD to 6mlp

i) Adenylate Kinase
RMSD to 4ake

a) Domain motions

RMSD to 6pwj

RMSD to 6ml0

RMSD to 1ake

4ake

b) Local unfolding

RMSD to 6pwk

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

6mlp

i) Ras p21

6pwk

iii) CaM Kinase II

ii) Rhomboid Intramem. Protease

a

c
a

Unfolding

a

b

a

a

b

b

b

a

b

c

b

Folding

Apo

2vn9

iii) Glu PRPP
Amidotransferase

ii) Fascin
3p53

RMSD to 6i11

i) Sialic acid
binding factor

2lep

4hdd

RMSD to 6h76

c) Cryptic pockets

5p21

RMSD to 3p53

RMSD to 2cey

RMSD to 1ecc

1q21

RMSD to 1ecj

6i11
2cey

1ecj

Holo

6h76

1ecc

Fig. 2 BioEmu samples functionally distinct protein conformations. a) Large-scale domain motions such as opening/closing,
rotation, and repacking. b) Local unfolding or unbinding of parts of the protein. c) Formation of cryptic binding pockets that are
not present in the apo ground state. Left column shows coverage, defined as the percentage of reference structures that are sampled
by at least 0.1% of samples (4 kcal/mol) within a given distance of the respective metric. ‘Pretrained’: results after training on only
AFDB data; ‘finetuned’: results using BioEmu. Global and local root mean square deviation (RMSD) is used for domain motions
and cryptic pocket formation benchmarks, respectively, and fraction of native contacts (FNC) for local unfolding. Our defined
success threshold is marked by dashed lines. i), ii), iii) show three examples for each class of evaluated conformational changes, using
BioEmu. All examples shown have less than 40% sequence similarity to BioEmu’s training data. Six references are also not included
in the AlphaFold2 monomer model training set (both in a,ii-iii both references and holo states in c,i-ii). The example shown in a,iii
is also in the OOD60 benchmark set, having less than 60% sequence similarity to any protein in the AlphaFold2 training set.

monomeric form features a globular conformation, while in its dimeric form the central beta-sheet unfolds and
the helices of the two monomers bind to each other. Finally, CaM Kinase II (Fig. 2b,iii) presents an autoinhibition
mechanism, in which the N-terminus binds into the active site. BioEmu predicts these local unfolding transitions

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

correctly, and overall 72% of locally folded and 74% of locally unfolded states across 20 protein examples (Fig.
2b, Fig. S2).
As a third class of conformational changes we consider the formation of pockets that are absent in the apo
state but form upon small-molecule binding. One option to identify such “cryptic” binding pockets is highperformance MD simulation [24], but the millisecond timescales often involved in the spontaneous opening of
such pockets make MD on commercial hardware rarely viable for in-silico drug discovery pipelines. We have
curated 34 cases of experimentally-validated formation of cryptic binding pockets from the literature (Fig. S4).
The sialic acid binding factor (Fig. 2c,i) presents a case where a large opening in the apo state can partially
close and form a binding site for the ligand. Fascin is a four-domain protein where two domains can rotate with
respect to each other, to reveal a binding site (Fig. 2c,ii). In Glu PRPP amidotransferase, part of the chain is
unfolded in the apo site and folds into a structure that completes the binding site for the ligand (Fig. 2c,iii). To
ensure capturing subtle changes, we define success by a very strict 1.5Å RMSD threshold to the apo and holo
reference structures. Surprisingly the model has a strong preference for holo states and successfully predicts the
cryptic pocket in 85% of cases, while it only succeeds in predicting 49% of the apo structures, indicating further
room for improvement.

4 Emulating MD equilibrium distributions
A major motivation for the development of BioEmu is to side-step the infamous MD sampling problem. The
practical MD data requirements for discovering biomolecular conformations and estimating their free energy
differences are often in the range of 100 µs to 10 ms simulation time [8, 9, 26]. Due to the vast computational
costs, exhaustive MD sampling of biomolecules has only been achieved in few cases, either with special purpose
supercomputers [27] or via large-scale distributed simulations integrated via statistical models [9, 28]. Here,
we assess BioEmu’s ability to emulate the equilibrium distribution that would be sampled with extensive MD
simulations. To this end, we have amassed all-atom simulations of proteins with a total aggregated simulation
time of over 200 ms (Table S1), which are used for fine-tuning BioEmu (Fig. 1d).
Before analyzing the model trained on the full dataset, we first test whether BioEmu’s design permits learning
to emulate long-time MD equilibrium distributions, using D. E. Shaw research (DESRES) simulations of 12 fastfolding proteins generated on the special-purpose supercomputer Anton [8]. We train 12 “DESRES-finetuned
models”, each of which is tested on one fast folder and fine-tuned on the others. As expected, the AFDBpretrained model predicts the native state but exhibits poor performance in free energy surface sampling (Fig.
S7). However, fine-tuning on only 11 sequences results in a surprisingly good match in the free energy surfaces
of test proteins (Fig. 3a,i, Fig. S7). For all proteins, the model predicts both native as well as the unfolded states
with similar shapes on the free energy landscape. In many cases, several or all folding intermediates visible on a
two-dimensional free energy surface are predicted (Fig. 3a,i, Fig. S7): For beta-beta-alpha protein (BBA), both
MD and the DESRES-finetuned models predict the existence of an intermediate with the alpha-helix formed
and the beta-sheet broken. For protein G, both MD and the DESRES-finetuned models sample intermediates
with half of the beta-sheet still formed, while the other half and most of the helix are broken. For homeodomain,
the models agree in the prediction of an intermediate with only one helix turn unwound, while the unfolded
states still feature some degree of helical propensity. There is an excellent agreement of the predicted secondary
structure propensities with the MD data (Fig. 3a, i, rightmost column). Quantitatively, the mean average error
between the MD and model 2D free energy landscapes is only 0.74 kcal/mol, ranging from 0.30 kcal/mol for
BBA to 1.63 kcal/mol for λ-repressor, which is on the order of differences expected from two different classical
MD force fields [29, 30].
We compare the computational costs between MD data generation and BioEmu in GPU-hours (here on a
NVIDIA Titan V). For all BioEmu results shown here, we draw 10k samples, which incurs computational costs
of < 1 GPU-minute for Chignolin to around 1 GPU-hour for λ-repressor (Fig. 3a). For MD we consider the cost
for generating the DESRES simulations, whose lengths have been chosen to include roughly 10 folding-unfolding
transitions (Fig. 3a). The MD costs then range from 2,000 GPU-hours for Chignolin to more than 100,000
GPU-hours for NTL9, resulting in a model speedup advantage over MD of four to five orders of magnitude. We
also note that for most proteins shown here, performing sufficiently long MD simulations to directly observe

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

a) Fast folders
Folded structure

partially / unfolded structures

MD

DESRES-finetuned

ii)

2ndary structure

Comp.
cost

Homeodom. Protein G

Ours

MD

BBA

i)

iii)

Errors &
Scores

b) CATH domains

MD

BioEmu

ii)

Errors & Scores

3udcA02

2wg5F02

i)

iii)

4o96A01

Data scaling (CATH-only model)

d) Ace 2

c) Complexin II
helicity

helix gate

gyration

BioEmu
ff03

BioEmu
GLU375

HIS374

ZN
GLU402

HEXXH+E motif
BioEmu
ff03

HIS378

ff99sb-disp

ff14sb

Fig. 3 BioEmu emulates equilibrium distributions of all-atom molecular dynamics (MD) many orders of magnitude faster. a)
Fast-folding proteins simulated by the DESRES Anton supercomputer compared with a model fine-tuned on all DESRES fastfolder except the test protein. i) From left to right: Folded and partially / unfolded structures predicted by our model (green) and
ground truth MD (grey). Free energy surfaces (in kcal/mol) of ground truth MD and our model in the space of the two slowest
time-laged independent components (TICA) [25]. Secondary structure content is compared over the whole ensemble of structures.
ii) Computational cost (in GPU hours) for MD (magenta: full DESRES dataset; yellow: single folding-unfolding roundtrip) and 10k
samples from our model (cyan). iii) mean average error (MAE) of free energy differences of macrostates and fraction of unphysical
model samples due to clashes. b) CATH domains. i) Color-code as in a,i. Additionally, structurally flexible motifs are color-coded
(cyan: helical; magenta: sheet) with reference MD-structures in dark and BioEmu samples in light color. ii) as in a, iii. iii) Macrostate
free energy MAE and state coverage as function of training data of a specialized CATH-only model. MAE of BioEmu is indicated
by a magenta star. c) Intrinsically disordered protein Complexin II: Sampled structure ensemble (left), helix content and radius
of gyration (right) compared betweenBioEmu and two all-atom force fields. d) Conformational flexibility of human angiotensinconverting enzyme 2 (ACE2). Helix gate opening distribution as a function of two distances (magenta and green arrows) of extensive
MD simulation (grey, seeded from magenta PDB-ID 6LZG), homologous PDB structures (black squares) and BioEmu samples
(cyan). Backbone-RMSD to crystal structure of HEXXH+E motif compared between MD and BioEmu.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

folding and unfolding in single trajectories is still not possible on consumer-grade hardware but instead requires
a much more complex methodological framework [28, 31].
The main BioEmu model is fine-tuned on more than 200 ms MD simulations with Amber force fields at or
near a temperature of 300K (Table S1). We choose to combine data from slightly different simulation conditions
as each of these MD models is inherently imperfect, and we regarded experimental data as being more reliable
for weighing between conformations (Fig. 1d, Sec. 5). Differences in the simulation conditions of our own
generated data are intentional, e.g. AMBER ff99sb-disp [32] was chosen to avoid spuriously-misfolded states
produced by other force fields in the context of protein folding (Sec. S.1.5.4). A large fraction of training data,
46 ms, is dedicated to 1100 CATH domains, common building blocks of protein structure [33] (Sec. S.1.5.2,
S.1.5.3). We designate 17 CATH systems with more than 100 µs simulation time as test set and report statistics
comparing MD and model distributions (Fig. 3b, Fig. S8). Similar as for DESRES simulations, BioEmu predicts
the native state with local fluctuations and typically several other substrates and structures sampled by MD.
Most secondary structure propensities match well (Fig. 3b, rightmost column). We observed a free energy mean
average error over the converged test set of 0.91 kcal/mol, again comparable to the differences expected between
different MD force fields.
To understand whether our model’s ability to sample accurate equilibrium distributions is limited by training data or model expressivity, we trained 3 models with the same architecture as BioEmu from scratch, using
only CATH data. We fixed a test set of CATH domains and trained the three models using 1%, 10% and 100%
respectively of the remaining CATH domains. We observed decreased free energy errors and an increased coverage of the conformations sampled by MD as the amount of training proteins increased (Fig. 3b,iii), suggesting
that the model can be further improved by adding more training data.
Finally, we have evaluated BioEmu for two case studies that involve larger proteins: Complexin II (134
aa) and ACE2 (614 aa). Complexin II is an intrinsically disordered protein (IDP) from the neurotransmitter
release apparatus [34]. IDPs tend to be difficult to sample with MD, however, BioEmu can efficiently emulate
a flexible ensemble of complexin II structures (Fig. 3c) while reproducing known secondary structure elements
such as the central and accessory helices [34, 35]. Achieving convergence of IDPs of this size with all-atom MD is
unpractical. At an orders of magnitude higher computational cost than with BioEmu, we have conducted ∼ 5µs
of MD simulations with all-atom MD, which are most likely not converged but already display qualitatively
different behavior: The AMBER ff14sb force field produces a very rigid compact structure with a small radius
of gyration and little to no variation in secondary structure content, whereas AMBER ff99sb-disp tends to
destabilize known secondary structure elements (Fig. 3c). The second case-study is ACE2, a metalloenzyme that
plays an important role in SARS-CoV-2 viral uptake (Fig. 3d) [36]. We show that BioEmu reliably reproduces
a stable HEXXH+E motif, the active enzymatic site of this protein [36], with backbone RMSDs below 1.5Å for
all model samples. The distance distribution of two gate-keeping helices is similar albeit less flexible compared
to a vast set of molecular dynamics simulations (890 µs, Ref. [37]) and compatible to homologue PDB structures
(Fig. 3d).

5 Predicting protein stabilities
Understanding protein stability is crucial for various applications in molecular biology, drug design, and biotechnology. From a modeling point of view, predicting a protein’s stability is a specific case of predicting the
equilibrium probabilities of its different conformational states, and these all arise from the same underlying biophysics. We therefore desire to train BioEmu so that the proportion of samples in folded and unfolded states
matches the experimentally-measured protein stability. We measure prediction errors in terms of the folding
free energy, defined as ∆G = Gfolded − Gunfolded , and classify protein structures as folded or unfolded based on
their fraction of native contacts (Sec. S.3.5.3).
To facilitate protein stability prediction, BioEmu’s training data includes over 750,000 experimental measurements from the MEGAscale dataset (Sec. S.1.7) [21], with a total of 25 ms of all-atom MD simulations of
the folded and unfolded states of 271 wildtype proteins and 21458 mutants (S.1.5.4). To address MD sampling
and force field issues, we weigh the folded and unfolded samples so that they correspond to the experimentallymeasured protein stabilities (Fig. 1d). To speed up training convergence and leverage the large number of
MEGAscale measurements, we developed the Property Prediction Fine-Tuning algorithm (PPFT, Fig. 1f, S.3.6)

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

d) Structural causes for stability changes

a) Folding free energies

Wild type HHH_rd1_0335, Mutation I7P

Wild type 2JWS, Mutation I24D

b) Stable proteins

c) Unstable proteins (IDPs)

Wild type 2ZW1_Y34A, Mutation E57H

Fig. 4 Prediction of experimentally measured protein stabilities. a) Comparison of experimental measurements of folding free
energies [21] with model predictions, generated by direct sampling and counting of folded and unfolded states for train and test
proteins. b) Validation that very stable proteins that are not included in the MEGAscale experimental dataset are consistently
predicted as folded. c) Validated that intrinsically disordered proteins (IDPs) reported in [43] and [45] are predicted as unfolded.
Radius of gyration (Rg ) is compared between model (orange crosses) experimental measurement (blue dots) and Flory scaling [46].
d) Analysis of the effect of three destabilizing mutants on the folded structures as predicted by the model: HHH rd1 0335 with
mutation I7P, 2JWS with mutation I24D, 2ZW1 Y34A with mutation E57H.

that integrates experimental expectation values, such as protein stabilities, into diffusion model training without requiring protein structures. PPFT uses fast approximate sampling with only 8 denoising steps, which
we observed to be sufficient to confidently predict whether each sampled structure will be classified as folded
or unfolded. By comparing the mean foldedness of sampled structures with experimental measurements and
backpropagating the error, our model can be efficiently trained to match experimental protein stabilities.
Our model achieves a mean absolute error below 0.8 kcal/mol and a Spearman correlation coefficient above
0.65 for proteins in the MEGAscale dataset (Fig. 4a). This accuracy outperforms other existing black box
methods that predict ∆G values directly from sequences [38–41]. Interestingly, the errors are similar for both
training and test set, indicating that the model generalizes well but cannot perfectly fit the training data, perhaps
due to inconsistencies between the folded/unfolded state definitions between this work and what the experiment
is sensitive to. To check whether BioEmu makes physically reasonable predictions outside the MEGAscale set
of proteins, we tested it on proteins that are known to be both very stable and unstable. We first selected stable
proteins from ProThermDB [42] with ∆G < −8 kcal/mol (more details in S.5.1). Our model consistently samples
these proteins in their folded states with a fraction of native contacts always exceeding the 0.65 threshold. To
test whether our model systematically predicts intrinsically disordered proteins (IDPs) as unfolded, we used
the CALVADOS test set [43]. Most proteins sampled displayed a radii of gyration (Rg ) similar to random coil
structures and larger than typical folded proteins, with the exception of two cases (Fig. 4c). In contrast to other
works [44, 45], our model has not been directly trained on IDPs; nonetheless, it provides zero-shot predictions
of Rg that correlate well with experimental measurements, albeit with overestimation of Rg values for longer
sequences (Fig. 4c).
In contrast to directly predicting ∆G by supervised learning models, we can analyze the structure ensemble
generated by our model to reveal insights on mutation-caused stability changes. For illustration, we show
mutants of the design protein HHH rd1 0335 and PDB entries 2JWS and 2ZW1 (Fig. 4d). In HHH rd1 0335,

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

the mutation I7P leads to a destabilization of the first helix, as indicated by the model’s prediction of a ∆∆G
of 1.3 kcal/mol compared to the experimental 2.1 kcal/mol. The analysis shows a decrease in average helicity
which particularly affects the helix where the mutation is located. In the case of 2JWS, the mutation I24D in
the middle helix results in its partial unfolding, with the model predicting a ∆∆G of 1.5 kcal/mol against an
experimental value of 2.9 kcal/mol. This mutation replaces a hydrophobic residue with a negatively charged
aspartate, disrupting core stability and leading to a localized structural change. Lastly, for 2ZW1, going from a
single mutant Y34A, to a double mutant Y34A & E57H introduces a positive charge in a region surrounded by
other positively charged residues, leading to a predicted ∆∆G of 1.9 kcal/mol compared to the experimental
1.2 kcal/mol. This mutation significantly disrupts the N-terminal beta-hairpin, a prediction that aligns with our
short MD simulations showing similar destabilization. These analyses highlight BioEmu’s ability to correlate
predictions of thermodynamics with structural causes, which is not possible with black-box prediction models.

6 Conclusion
We have introduced a generative machine learning system to approximately sample the equilibrium distributions
of proteins and through that explore two key aspects of molecular function: protein conformations and their
equilibrium probabilities. The system has been demonstrated to sample experimentally known structures of
proteins undergoing a variety of conformational changes, to approximate the equilibrium distributions of extensive MD simulations, and to predict experimentally-measured protein stabilities within errors of 1 kcal/mol.
The cost of running inference is on the order of one GPU-hour per computational experiment — many orders
of magnitude less than running MD simulations even if enhanced sampling methods are invoked, and orders of
magnitude cheaper than experiments that can provide detailed structure-function relationships.
BioEmu and MD simulation are complementary: our system was trained on large amounts of MD simulation
of soluble proteins, and within this scope, it has shown to be able to approximate MD distributions at a tiny
fraction of the MD simulation costs. However, BioEmu cannot be expected to generalize beyond this scope —
for example membrane environments and small molecule ligands are neither represented in the model nor in the
training, and BioEmu can therefore not be expected to make reliable predictions when membranes or ligands
play a key role in the process. For MD, generalizing to such conditions is straightforward, although obtaining
results will be limited by the sampling problem.
Our system can be used to generate a guess for the equilibrium distribution, and MD trajectories can
be launched from a BioEmu ensemble in order to obtain chemically accurate all-atom structures, refine the
distribution, and even compute dynamical properties. We therefore do not expect that emulators such as BioEmu
will make MD simulation obsolete; however we do expect that the role of MD simulation will shift from a
production tool to a data generation and validation tool, as is already the case for other simulator-emulator
pairs such as quantum chemistry and machine-learned forcefields. We have demonstrated that BioEmu can
be efficiently fine-tuned on experimental data such as folding free energies. This is an important advantage
compared to MD forcefields, which can also be tuned to fit experimental data [47], but the processes that give
rise to the experimental observables must be sampled during the training process — a task that is tedious or
even unfeasible for observables that involve complex rare events, such as folding free energies.
An important limitation of BioEmu is that it generates distributions entirely empirically, while MD simulation uses potential energy functions which are connected to equilibrium distributions and expectation values
by statistical mechanics. If direct access to a potential energy function u(x) was available that is consistent
with the generated distribution by p(x) ∝ eu(x) , it could be used for reweighting and making rigorous enhanced
sampling simulations available through the emulator. Another limitation of the current system is that it only
emulates single protein chains at a fixed thermodynamic condition of 300K. A proper emulator for proteins
requires conditioning on experimentally and biologically relevant parameters such as temperature and pH, and
needs to be able to model multiple interacting molecules, as proteins rarely have a function on their own.
While structure prediction systems for predicting biomolecular complexes already exist [2, 3], a key obstacle
to extending the emulator to other scopes different from proteins, as well as further improving it for the current
scope, is the lack of training data. While we have shown that the ability to accurately emulate the equilibrium
distributions of small proteins increases with more training data, the sampling problem limits MD to generating
data for small fragments of biomolecular systems. For learning changes of conformation and binding state of

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

large biomolecular complexes, as well as learning the subtle binding affinity differences between binding partners,
and ultimately tackle the quest for reliably predicting protein function, highly scalable experimental techniques
that can be incorporated as training data will become key.

Code availability
Release of inference code and model weights is in preparation.

Acknowledgments
We are indebted to the entire Microsoft Research AI for Science team, and thank in particular the following
individuals for valuable support and discussions: Chang Liu, Peiran Jin, Tie-Yan Liu, Chris Bishop, Bonnie
Kruft, Jonas Köhler, Thijs Vogels, Ryota Tomioka, Marwin Segler, Rianne van den Berg, Marco Federici, Stratis
Markou, Maik Riechert. Furthermore, we thank colleagues from FU Berlin for valuable discussions and advice,
in particular Nicholas E. Charron, Katarina Elez, and Aldo Sayeg Pasos Trejo.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

References
[1] Jumper, J. et al. Highly accurate protein structure prediction with AlphaFold. Nature, 596(7873):583–589,
2021.
[2] Abramson, J. et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature,
630:493–500, 2024.
[3] Krishna, R. et al. Generalized biomolecular modeling and design with RoseTTAFold All-Atom. Science,
384:eadl2528, 2024.
[4] Baek, M. et al. Accurate prediction of protein structures and interactions using a three-track neural network.
Science, 373:871–876, 2021.
[5] Berman, H.M. et al. The Protein Data Bank. Nucl. Acids Res., 28:235–242, 2000.
[6] Ritort, F. Single-molecule experiments in biological physics: Methods and applications. J. Phys.: Condens.
Matter, 18:R531–R583, 2006.
[7] Bai, X.C., McMullan, G. and Scheres, S.H. How cryo-EM is revolutionizing structural biology. Trends
Biochem. Sci., 40:49–57, 2015.
[8] Lindorff-Larsen, K., Piana, S., Dror, R.O. and Shaw, D.E. How Fast-Folding Proteins Fold. Science, 334
(6055):517–520, 2011.
[9] Plattner, N., Doerr, S., Fabritiis, G.D. and Noé, F. Complete protein–protein association kinetics in atomic
detail revealed by molecular dynamics simulations and Markov modelling. Nat. Chem., 9(10):1005, 2017.
[10] Wang, J. et al. Machine learning of coarse-grained molecular dynamics force fields. ACS Cent. Sci., 5:
755–767, 2019.
[11] Charron, N.E. et al. Navigating protein landscapes with a machine-learned transferable coarse-grained
model. arXiv:2310.18278, 2023.
[12] Noé, F., Olsson, S., Köhler, J. and Wu, H. Boltzmann Generators - Sampling equilibrium states of manybody systems with deep learning. Science, 365:eaaw1147, 2019.
[13] Zheng, S. et al. Predicting equilibrium distributions for molecular systems with deep learning. Nat. Mach.
Intell., 6:558–567, 2024.
[14] Jing, B., Berger, B. and Jaakkola, T. AlphaFold meets flow matching for generating protein ensembles.
arXiv:2402.04845, 2024.
[15] Qiao, Z., Nie, W., Vahdat, A., III, T.F.M. and Anandkumar, A. State-specific protein–ligand complex
structure prediction with a multiscale deep generative model. Nat. Mach. Intell., 6:195–208, 2024.
[16] Wayment-Steele, H.K. et al. Predicting multiple conformations via sequence clustering and AlphaFold2.
Nature, 625(7996):832–839, 2024.
[17] Bryant, P. and Noé, F. Structure prediction of alternative protein conformations. Nat. Commun., 15:7328,
2024.
[18] Vani, B.P., Aranganathan, A., Wang, D. and Tiwary, P. AlphaFold2-RAVE: From sequence to Boltzmann
ranking. J. Chem. Theory Comput., 19:4351–4354, 2023.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

[19] Aranganathan, A., Gu, X., Wang, D., Vani, B. and Tiwary, P. Modeling boltzmann weighted structural
ensembles of proteins using ai based methods. ChemRxiv, 2024. doi: 10.26434/chemrxiv-2024-6f9h6-v2.
[20] Prinz, J.H. et al. Markov models of molecular kinetics: Generation and validation. J. Chem. Phys., 134:
174105, 2011.
[21] Tsuboyama, K. et al. Mega-scale experimental analysis of protein folding stability in biology and design.
Nature, 620(7973):434–444, 2023.
[22] Aviram, H.Y., Pirchi, M., Mazal, H. and Haran, G. Direct observation of ultrafast large-scale dynamics of
an enzyme under turnover conditions. Proc. Natl. Acad. Sci. USA, 115:3243–3248, 2018.
[23] Fromowitz, F.B. et al. Ras p21 expression in the progression of breast cancer. Human pathology, 18(12):
1268–1275, 1987.
[24] Greisman, J.B. et al. Discovery and validation of the binding poses of allosteric fragment hits to protein
tyrosine phosphatase 1b: From molecular dynamics simulations to X-ray crystallography. J. Chem. Inf.
Model., 63:2644–2650, 2023.
[25] Perez-Hernandez, G., Paul, F., Giorgino, T., D Fabritiis, G. and Noé, F. Identification of slow molecular
order parameters for markov model construction. J. Chem. Phys., 139:015102, 2013.
[26] Lane, T.J., Shukla, D., Beauchamp, K.A. and Pande, V.S. To milliseconds and beyond: Challenges in the
simulation of protein folding. Curr. Opin. Struct. Biol., 23(1):58–65, 2013.
[27] Shaw, D.E. et al. Atomic-Level Characterization of the Structural Dynamics of Proteins. Science, 330
(6002):341–346, 2010.
[28] Chodera, J.D. and Noé, F. Markov state models of biomolecular conformational dynamics. Current Opinion
in Structural Biology, 25:135–144, 2014.
[29] Best, R.B. and Mittal, J. Free-energy landscape of the gb1 hairpin in all-atom explicit solvent simulations
with different force fields: Similarities and differences. Proteins, 79:1318–1328, 2011.
[30] Hahn, D.F., Gapsys, V., de Groot, B.L., Mobley, D.L. and Tresadern, G. Current state of open source
force fields in protein-ligand binding affinity predictions. J. Chem. Inf. Model., 64:5063–5076, 2024.
[31] Laio, A. and Parrinello, M. Escaping free-energy minima. Proc. Natl. Acad. Sci. U.S.A., 99(20):12562–
12566, 2002.
[32] Robustelli, P., Piana, S. and Shaw, D.E. Developing a molecular dynamics force field for both folded and
disordered protein states. Proc. Natl. Acad. Sci. U.S.A., 115(21), 2018.
[33] Sillitoe, I. et al. CATH: Increased structural coverage of functional space. Nucleic Acids Res., 49(D1):
D266–D273, 2021.
[34] Malsam, J. et al. Complexin Suppresses Spontaneous Exocytosis by Capturing the Membrane-Proximal
Regions of VAMP2 and SNAP25. Cell Reports, 32(3):107926, 2020.
[35] Zhou, Q. et al. The primed SNARE–complexin–synaptotagmin complex for neuronal exocytosis. Nature,
548(7668):420–425, 2017.
[36] Towler, P. et al. ACE2 X-Ray Structures Reveal a Large Hinge-bending Motion Important for Inhibitor
Binding and Catalysis. J. Bio. Chem., 279(17):17996–18007, 2004.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

[37] Zimmerman, M.I. et al. SARS-CoV-2 simulations go exascale to predict dramatic spike opening and cryptic
pockets across the proteome. Nat. Chem., 13(7):651–659, 2021.
[38] Ouyang-Zhang, J., Diaz, D., Klivans, A. and Krähenbühl, P. Predicting a protein’s stability under a million
mutations. Advances in Neural Information Processing Systems, 36:76229–76247, 2024.
[39] Cagiada, M., Ovchinnikov, S. and Lindorff-Larsen, K. Predicting absolute protein folding stability using
generative models. bioRxiv, 2024. doi: 10.1101/2024.03.14.584940.
[40] Notin, P. et al. Proteingym: Large-scale benchmarks for protein fitness prediction and design. Advances
in Neural Information Processing Systems, 36:64331–64379, 2024.
[41] Widatalla, T., Rafailov, R. and Hie, B. Aligning protein generative models with experimental fitness via
direct preference optimization. bioRxiv, 2024. doi: 10.1101/2024.05.20.595026.
[42] Nikam, R., Kulandaisamy, A., Harini, K., Sharma, D. and Gromiha, M.M. ProThermDB: Thermodynamic
database for proteins and mutants revisited after 15 years. Nucleic Acids Res., 49(D1):D420–D424, 2021.
[43] Tesei, G. et al. Conformational ensembles of the human intrinsically disordered proteome. Nature, 626
(8000):897–904, 2024.
[44] Tesei, G. and Lindorff-Larsen, K. Improved predictions of phase behaviour of intrinsically disordered
proteins by tuning the interaction range. Open Research Europe, 2:94, 2023.
[45] Zhu, J. et al. Precise generation of conformational ensembles for intrinsically disordered proteins via
fine-tuned diffusion models. bioRxiv, 2024. doi: 10.1101/2024.05.05.592611.
[46] Hofmann, H. et al. Polymer scaling laws of unfolded and intrinsically disordered proteins quantified with
single-molecule spectroscopy. Proc. Natl. Acad. Sci. U.S.A., 109(40):16155–16160, 2012.
[47] Fröhlking, T., Bernetti, M., Calonaci, N. and Bussi, G.
experimental observables. J. Chem. Phys., 152:230902, 2020.

Toward empirical force fields that match

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Supplementary Material
Contents
S.1

S.2

S.3

S.4

S.5

S.6
S.7

Data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.1 AlphaFoldDB processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.2 Protein Data Bank processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.3 Molecular Dynamics simulation data . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.4 MD simulation protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.5 In-house MD datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.5.1
Octapeptides . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.5.2
CATH1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.5.3
CATH2 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.5.4
MEGAsim . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.5.5
Complexin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.6 Public MD datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.1.7 Experimental thermodynamics data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Model architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.2.1 Protein sequence encoder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.2.2 Coarse-grained protein structure representation . . . . . . . . . . . . . . . . . . . . . . .
S.2.3 Diffusion conditional generative model . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.2.4 Score model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Training methodology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.3.1 Data splitting procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.3.2 Pre-training on AFDB . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.3.3 Fine-tuning on CHARMM MD data of fast-folding proteins . . . . . . . . . . . . . . . .
S.3.4 Fine-tuning on Amber MD data and experimental folding free energies . . . . . . . . . .
S.3.5 Reweighting MD with Markov models and experimental data . . . . . . . . . . . . . . .
S.3.5.1
MSM reweighting for small peptide datasets . . . . . . . . . . . . . . . . . . .
S.3.5.2
Connectivity filtering for post-hoc analyses . . . . . . . . . . . . . . . . . . . .
S.3.5.3
Reweighting MD with experimental folding free energies . . . . . . . . . . . . .
S.3.6 Training on folding free energies via property prediction fine-tuning (PPFT) . . . . . . .
Multi-conformation benchmarking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.4.1 Benchmark sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.4.2 Curation of the OOD family of benchmarks . . . . . . . . . . . . . . . . . . . . . . . . .
S.4.3 Measuring multiple conformations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.4.4 Baseline methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Protein stability benchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.5.1 System selection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
S.5.2 Evaluating free energy predictions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Energy landscape MAE . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Supplementary Tables and Figures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

List of Figures
S1
S2
S3
S4
S5
S6
S7

OOD60 multi-conformation benchmark results . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Domain motion multi-conformation benchmark results . . . . . . . . . . . . . . . . . . . . . . . .
Local unfolding multi-conformation benchmark results . . . . . . . . . . . . . . . . . . . . . . . .
Cryptic pocket multi-conformation benchmark results . . . . . . . . . . . . . . . . . . . . . . . .
Multi-conformation benchmarking against baselines . . . . . . . . . . . . . . . . . . . . . . . . . .
Comparison of pretraining datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
DESRES free energy surface results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

S8

CATH free energy surface results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41

List of Tables
S1
S2
S3
S4

Molecular dynamics training datasets details . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
Training hyperparameters in each stage of training . . . . . . . . . . . . . . . . . . . . . . . . . .
Relative MD dataset weights used for model fine-tuning . . . . . . . . . . . . . . . . . . . . . . .
Influence of pretraining split choice on multiconformation results . . . . . . . . . . . . . . . . . .

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

S.1 Data
S.1.1 AlphaFoldDB processing
An AlphaFold database (AFDB) snapshot was downloaded in July 2024 and preprocessed for model pretraining
(Fig. 1d,e). The aim of this preprocessing is to identify sets of similar sequences with heterogeneous predicted
structures, and this is accomplished through a series of steps:
1. We used mmseqs [1] to cluster all sequences at 80% sequence identity and 70% coverage, resulting in a set
containing more than 93 million clusters.
2. To reduce the sequence clusters to a representative set, we clustered the centroids of the these clusters at
30% sequence identity and discarded all but the 80%-sequence-identity cluster containing the centroid of
each 30%-sequence-identity cluster. The result was a set of sequence clusters with 80% sequence similarity
within each cluster and at most 30% sequence similarity between the centroids of different clusters.
3. We discarded sequence clusters with fewer than 10 members, leaving roughly 1.4 million sequence clusters.
4. We performed structure-based clustering within each sequence cluster, using foldseek [2] (version 9.427df8a)
with a sequence identity threshold of 70% at 90% coverage.
5. We discarded everything except the representative member of each structure cluster, leaving a set of sequence
clusters which each contain a few structure representatives.
6. We discarded sequence clusters with only one structure representative and those where all the structure
representatives were disordered (defined as being composed of more than 50% coil in their secondary
structure).
7. To account for structural heterogeneity that was incorrectly flagged due to missing regions in structure
representatives, we performed structural alignments in sequence-aligned regions of proteins, and discarded
structure representatives with a TM-score greater than 0.9 to another structure representative, as computed
by foldseek.
8. Similarly to [3], we removed sequence clusters lacking at least one structure with pLDDT greater than 80,
and with a pLDDT standard deviation lower than 15 across residues
After running this pipeline, we had ∼50k sequence clusters with structural diversity. We utilize the structural
diversity to generate augmented data during the pre-training phase (see section S.3.2).

S.1.2 Protein Data Bank processing
A snapshot of the PDB was downloaded in Nov. 23rd 2023, including all of the available asymmetric units in
the mmCIF format. We use the pdbecif Python package (version 1.5) for mmCIF parsing and consider an
entry for processing if the overall number of residues in the entry was below 2500 with a resolution below 9.5 Å,
when a resolution value was available. All molecular entities per entry were separated according to their type
(i.e., polymer or non-polymer), discarding those associated with other nucleic acids (e.g., RNAs, DNAs). Nonbiologically relevant non-polymer entities (e.g., solvents, ions) were further filtered out by a list provided in [4].
Non-binding polymer chains were then kept on an entry basis if they contained standard amino acid types and
depending on whether other non-binding chains corresponding to the same entity identifier had already been
processed. So as to better capture ligand-binding conformational effects, all binding polymer chains with unique
binders, as determined by a distance threshold of 6 Å between any binder and protein atom, were kept.

S.1.3 Molecular Dynamics simulation data
In the following, we list synthetic all-atom molecular dynamics (MD) data used in this article. An overview of
all publicly available and in-house datasets is given in Tab. S1. In-house datasets are described in detail in S.1.5,
with our standard MD protocol specified in S.1.4. Public datasets are listed under S.1.6. As our model is for
single protein chains and there were several MD simulations of multi-chain systems, we extracted single protein
chains from those and treated them independently. As a consequence, the effective cumulative simulation time
for such multi-chain simulations is reported as a sum over all chains. For datasets curated from the literature,
a reference is provided, whereas details for MD simulations generated specifically for this work can be found
in S.1.5.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Table S1 Molecular dynamics training datasets used in this work, their associated number of systems, number of
individual chains, simulation time, and forcefield used.
Dataset

Sim.
time (ms)

Eff. sim.
time (ms)

DESRES-fastfolders
FAH-DDR1
FAH-SETD8
FAH-sarscov2
FAH-sarscov2-exascale
FUB-MHCII
FUB-barnase-barstar
MSR-cath2
MSR-megasim
MSR-megasim-mutants
ONE-cath1
ONE-octapeptides

8.2
6.8
5.9
4.5
56.5
8.9
2.0
41.0
3.8
21.5
5.2
8.0

8.2
6.8
5.9
4.5
81.0
26.2
4.0
41.0
3.8
21.5
5.2
8.0

Total

172.2

216.0

Force field
charmm22*
amber ff99sb-ildn
amber ff99sb-ildn
amber ff14sb
amber ff03
amber ff99sb
amber ff99sb
amber ff99sb-ildn
amber ff14sb & ff99sb-disp
amber ff99sb-disp
amber ff99sb-ildn
amber ff99sb-ildn

# MD sys.

# ind. chains

Ref.
[5]
[6]
[7]
[8]
[9]
[10]
[11]
S.1.5.3
S.1.5.4
S.1.5.4
S.1.5.2
S.1.5.1

S.1.4 MD simulation protocol
We internally developed code specifically tailored towards running large MD production campaigns on Azure
compute resources. Our code is based on OpenMM [12] as its compute engine, albeit setups are generated using
OpenMM or GROMACS [13] as a backend, depending on each case. Unless noted otherwise, we conform to
the following protocol for running our MD simulations: We use exlicit solvent and the tip3p water model [14],
solvate structures in a cubic box with 1 nm padding and a NaCl buffer of 0.1 M. The solvent is equilibrated
with a harmonic constraint force on the solute heavy atoms for 0.1 ns under constant temperature and volume
(NVT) followed by 0.9 ns of simulation under constant temperature and pressure (NPT). The constraint force
is switched off in multiple steps during another 0.1 ns simulation time. During the equilibration phase, the
integration timestep is set to 2 fs. Production runs are conducted in the NPT ensemble, using hydrogen mass
repartitioning with hydrogen mass of 4 amu [15], with hydrogen bond constraints, and an integration timestep
of 4 fs. The temperature is set to 300 K and the pressure to 1 bar, unless noted otherwise.
Most simulation data described in this work was generated using T4-based (NC4as T4 v3) Azure compute
instances.

S.1.5 In-house MD datasets
S.1.5.1 Octapeptides
The octapeptide dataset consists of 1100 peptides of 8 amino acids length. The selection of systems had been
previously described (see Ref. [16] for details about system selection and initial structure seeding procedures).
We extend this dataset with longer trajectories in order to obtain a better representation of equilibrium. For
each system, 5 new trajectories with 1 µs length were generated using our in-house protocol (S.1.4), using the
same force field as in the original dataset (amber ff99SB-ildn [8]), at 300K. The total simulation time amounts
to 8 ms.

S.1.5.2 CATH1
This data consists of 50 CATH domains as previously described in Ref. [16]. We also extend this dataset,
previously consisting of 4 x 0.5 µs trajectories per system, with longer MD trajectories to better represent longtimescale dynamic behavior of different protein domains. Trajectories between 1 and 5 µs length using the amber
ff99SB-ildn forcefield [8] were produced, totaling 100 µs per CATH domain. Data production was conducted
using an adaptive sampling [17] scheme, where the first trajectory epoch was seeded from a reference PDB
structure, while the following 2 epochs were seeded by extracting frames from previous epochs via a minRMSD
clustering [18] approach. The total simulation time of the combined dataset (original and in-house) amounts to
5.2 ms.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

S.1.5.3 CATH2
The CATH2 dataset focuses on sequence coverage rather than overall simulation length. Similar to CATH1
and to the procedure described in [16], systems were selected from the CATH database [19] (version 4.3.0) by
filtering out non-contiguous structures or sequences, non-standard amino acids, proteins with disulfide bonds,
coil fractions above 50%, and proteins with a relative shape anisotropy ≥ 0.05. Only domains containing between
50 and 200 amino acids were selected, forming a set of ∼1100 domains. Out of those, for 1040 we could generate
valid MD setups using our in-house protocol (S.1.4). 1 µs trajectories for these domains were generated using
the amber99SB-idln [20] forcefield, producing a total of approximately 39 µs per CATH domain, with the exact
amount varying due to compute availability reasons. We used the same adaptive sampling strategy as in the
CATH1 dataset, and 2 epochs of reseeding. The cumulative simulation time for the whole dataset is 41 ms.

S.1.5.4 MEGAsim
The MEGAscale domain simulation dataset (“megasim” in short) is dedicated to including folding-unfolding
transitions in the training data. In total, it consists of extended simulations of 271 wildtypes, and 1 µs simulations
for each of the 22,118 point mutants, including single-residue insertion/deletions. The systems and mutants
in our dataset were taken from the megascale measurements of protein domain stability via cDNA display
proteolysis [21]. To ensure that every sampled system had a corresponding experimental measurement of the
folding free energy ∆G during the folding process, we focused on wildtypes and mutants within the curated
set (“Dataset2 Dataset3”) of the reference publication. Our final dataset consists of a smaller subset of systems
due to finite computational resources and several applied filters, detailed below.
For the wildtype dataset, we tailored the general simulation setup to efficiently sample in both the folded and
unfolded states. The seeding structures included both the folded state as well as less structured decoys. Folded
structures were obtained from the AF2 predictions available on the Zenodo repository of Ref. [21]. Unfolded
(decoy) starting structures were obtained by simulated thermal denaturization in implicit solvent at 400K,
followed by several rounds of adaptive sampling in explicit solvent at an elevated temperature. For both the
equilibration and production phases, two force fields were used: amber ff14sb [22] and amber ff99SB-disp [23].
In comparison to more traditional force fields like ff14sb, ff99sb-disp is specifically designed to model disordered
proteins and does not over-stabilize globular decoy structures [23]. Even though generally reliable, we noticed
that a99sb-disp can destabilize the native fold of a protein after extensive simulations. For those cases we relied
on ff14sb to generate samples of the folded state.
To optimize compute efficiency, we chose a rhombic dodecahedron simulation box with a 1.5 nm padding for
each individual seed. Equilibration was performed with 0.2 ns NVT and 0.6 ns NPT simulations, targeting 295K
and 1 bar with a Langevin integrator and a 4 fs time step. Production simulations were performed for 1.5 µs per
starting structure at 295K in the NVT ensemble and a 4 fs time step. Bond constraints and hydrogen mass were
kept identical to Section S.1.4, and we discarded the first 500 ns of each trajectory to only consider the last 1 µs
in the subsequent analysis. Post processing was carried out with the goal of obtaining a clear separation between
folded and unfolded samples as well as minimizing the effect of mixing samples from two force fields. We used the
fraction of native contacts (FNC) to define the relative foldedness of each MD frame, and built FNC histograms
for all samples from each force field. While, theoretically, for two-state folding-unfolding transitions one can
expect the a bimodal distribution, in practice it can be multimodal. However, we observed that the folded and
unfolded states have well-defined density peaks in the FNC distribution, and thus performed a kernel density
estimation. For each forcefield, we used the FNC with the lowest estimated density as the folding threshold.
For the unfolded state, we picked the samples below the FNC threshold from trajectories simulated with
the ff99sb-disp forcefield, whereas for the folded ones we used samples from the same forcefield, i.e., ff99sb-disp
by default. However, some cases remained where the samples above the FNC threshold from the ff99sb-disp
forcefield were multimodal, that spread over a large range, or that had significant lower FNCs than the samples
from ff14sb. For those systems, we selected ff14sb for the folded state. We discarded systems where neither force
field resulted in a clear density peak in the FNC distribution above 0.8, or where either the folded or unfolded
samples consisted of less than 10% of the entire dataset. In difficult cases, we checked several sample structures
as well as the FNC and RMSD time series and made a decision based on visual inspection. After processing,
the “MSR-megasim-merge” dataset consisted of 271 wildtype systems, out of which 77 had folded states from

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

amber ff14sb and unfolded states from amber ff99sb-disp, while the rest 194 featured both folded and unfolded
samples from amber ff99sb-disp.
Due to the large number of sequences present in the mutant dataset, we could not afford to conduct sampling as thorough as for the wildtypes. Instead, we relied on the presumption that point mutations or single
insertion/deletion mainly affect local interactions in the folded state, and only weakly perturb the sample distribution in the unfolded state. Since our model only considers the protein backbone, we re-used the unfolded
samples from the wildtypes for all point mutants, and generated MD simulations for all mutants in the folded
state. Here we also assumed that the mutant folded state does not deviate completely from the native state of
its wildtype, but would only be involved in local rearrangements, such as side-chain repacking. This assumption
allowed MD simulations of mutant structures to be seeded from their wildtype folded conformation, as well as
the use of the wildtype FNC to probe mutant foldedness. It further means that we can use the FNC defined by
the wildtype native contacts to probe the foldedness of the mutants. In practice, we generated the mutant starting structures from their corresponding wildtype reference structure by exchanging the sidechain accordingly
and by performing energy minimization. This is followed by a 1 µs simulation for each of the mutants using
the amber ff99sb-disp force field. Since we expect the starting structure to be not the exact native structure of
the mutant, we anticipated the need for a burn-in period, in which the system can explore a more stable native
folded state. To select the length of such period, we split the trajectory into two parts so that the difference
of the mean FNCs of each part would be maximized. The part after the burn-in period was then kept for the
folded samples, except for situations where the FNC decreased monotonically throughout the simulation.
To validate the combination of samples of each wildtype with its mutants, we considered the impact of
including mutant folded samples on the folding threshold for FNC computation. In cases where the previously
classified unfolded samples had surpassed the folding threshold, it was no longer possible to define foldedness
for the mutant based on its wildtype native contacts. In all other cases, samples were combined, since those
coming from wildtype simulations only contributed to the unfolded population. After excluding cases violating
the previous two assumptions, we obtained a set containing samples for 21,458 mutants, which we named the
“MSR-megasim-mutants-mosaic-disp” dataset.

S.1.5.5 Complexin
We have generated a small MD dataset for complexin-2 (Uniprot ID Q6PUV4), which has only been used to
qualitatively compare model predictions in Fig. 3c. The simulations were seeded using the AlphaFold2 predicted
structure deposited in Uniprot. First, we produced a 5 µs trajectory with the Amber ff14sb force field [22]
using our standard MD simulation protocol (Sec. S.1.4). Second, we generated dynamics with the Amber ff99sbdisp [23] force field. Here, the setup and equilibration were conducted in GROMACS [13] with initial structures
being solvated in a cubic box with 1.2 nm padding and 0.135 molar KCL buffer and the custom ff99sb-disp
TIP4P water model. After local energy minimization, the system was equilibrated in 0.1 ns (NVT) and 0.1 ns
(NPT). Four production simulations of 1.5 µs were conducted in OpenMM using our standard protocol S.1.4.
We evaluated the simulation speed on NVIDIA TitanV to be 200 ns/day for ff14sb and 60 ns/day for
ff99sb-disp, the latter being reduced to the more expensive 4-point water model.

S.1.6 Public MD datasets
DESRES fast-folding proteins
We use the fast folding protein simulations described in Ref. [8] under license. The dataset consists of 12 systems
simulated with the charmm22* force field [24], with a cumulative simulation time of 8.2 ms. This dataset has
only been used for a separate model whose results are shown in Fig. 3a and S7, but it is not used to obtain any
of the other results presented throughout the manuscript.
DDR1
Simulations of 9 DDR1 kinases published in Ref. [6](https://osf.io/4r8x2/), with the amber ff99sb-idln [20]
forcefield and featuring a cumulative simulation time of 6.8 ms.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

SETD8
Simulations of methyltransferase SETD8 [7](https://osf.io/2h6p4/), excluding data complexed with small
molecules. The dataset consists of 26 systems, has a total simulation length of 5.9 ms and uses the amber
ff99sb-idln force field.
SARS-CoV-2 exascale
We use the publicly available subset of the data published with Ref. [9], which consists of simulations
for 24 systems and uses the amber ff03 force field [25]. The cumulative simulation time is 56.5 ms
(when counting by trajectory), or an effective 81 ms (when treating chains independently). The data was
downloaded from https://registry.opendata.aws/foldingathome-covid19/ (AWS resource name arn:aws:s3:::
fah-public-data-covid19-cryptic-pockets).
SARS-CoV-2 non-exascale
Non-glycosylated SARS-CoV-2 RBD data as published by Ref. [8] and downloaded from https://registry.
opendata.aws/foldingathome-covid19/ (AWS resource name arn:aws:s3:::fah-public-data-covid19-antibodies).
The dataset consists of a single system with 1.9 ms cumulative simulation time and uses the amber ff14sb [22]
forcefield.
MHC2 peptide simulations
We use the dataset of MHC2 in complex with peptides as published by Ref. [10]. It consists of 68 systems
with multiple chains and uses the amber ff99sb forcefield [26]. The cumulative simulation time is 9 ms (when
counting by trajectory) or effectively 27 ms (when treating chains independently).
Barnase-Barstar
Simulations provided by Ref. [11], consisting of one system with two chains using amber ff99sb [26]. The
cumulative simulation time is 2.0 ms (when counting by trajectory) or 4.0 ms effective (when treating chains
indepedently). The dataset was downloaded from https://zenodo.org/records/8252423.

S.1.7 Experimental thermodynamics data
High-throughput experimental measurements of protein stability at ambient temperature were used to finetune
the model in combination with in-house generated datasets. Specifically, we extracted the ∆G (“dG ML”) and
∆∆G values (“ddG ML”) and the corresponding amino acid sequences for wildtypes and mutants within the
curated set (“Dataset2 Dataset3”) from the associated data in Ref. [21], which added up to ∼776,000 entries.

S.2 Model architecture
In this section, we describe the architecture of the proposed model and how it is trained. We define BioEmu
as a conditional generative model. BioEmu receives as input a protein sequence and generates independent
identically-distributed (i.i.d.) samples from the approximated equilibrium distribution over conformations of
that protein. The i.i.d. generation of samples can be parallelized across a batch of random seeds, which allows
us to approximately explore the equilibrium distribution of protein conformations orders of magnitude faster
than standard sequential, correlated molecular dynamics simulations.

S.2.1 Protein sequence encoder
The protein sequence S is encoded through the protein sequence encoder (Fig. 1b) to compute single and pair
representations using a simplified version of AlphaFold2 [27]. Similar to other works [28], we use pre-trained
AlphaFold2 [27] sequence representations. We run the AlphaFold2 container with a few changes; we used only
the Uniclust30 database [29] (as of August 2018) as reference for multiple sequence alignment construction
via hhblits [30], completely excluded templates, and removed the AlphaFold2 recycling iterations. During
generation, we set the random seed to 0 and use the single and pair embeddings generated by model 3.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

As the protein sequence encoder depends on no other variables than the protein sequence S, the single
and pair embeddings for all proteins used in training and inference are pre-computed once and stored for fast
retrieval.

S.2.2 Coarse-grained protein structure representation
BioEmu models 3D protein structures with a coarse-grained representation following [31]. Only the backbone
heavy atoms of the protein are represented via the backbone frame representation introduced in [27]. Similarly
to [31], but unlike [27], side-chains and hydrogen atoms are not explicitly modeled by BioEmu.
To convert an all-atom protein conformation to its backbone frame representation for a given residue, we use
its Cα atom coordinate r ∈ R3 and perform the Gram-Schmidt algorithm on the displacement vectors Cα → N
and Cα → C. This yields an orthonormal basis which can be represented as a rotation matrix Q ∈ SO(3).
Repeating this for each residue, we obtain a sequence of position-orientation tuples, x := {(ri , Qi )}N
i=1 , for
all N protein residues. To recover the Cartesian backbone atom positions from the frame representation, we
start with a reference backbone heavy-atom frame per residue type, with idealized atom positions, similarly to
AlphaFold2 [27] or OpenFold [32]. For example, for alanine, the idealized frame atom positions are:



N
−0.525 1.363 0.000

Cα 
 0.000 0.000 0.000 
.
C 
1.526
0.000
0.000


Cβ  −0.529 −0.774 −1.205 
O
0.627 1.062 0.000
We then apply the rotation matrix Qn to obtain the rotated frame, and add the position vector rn to the
coordinates of all the atoms in the frame. Note that since the Cα is at the origin of the idealized frame, it will
be at exactly location rn upon applying this transformation.

S.2.3 Diffusion conditional generative model
BioEmu acts as a sequence-conditional generative model: given a protein amino acid sequence, the model
parameterizes a distribution of backbone conformational states. Formally, let S = (a1 , a2 , . . . , aN ) be a protein
sequence with N residues ai ∈ R from the set of 20 standard amino acids. BioEmu is a conditional diffusion
model that can be used to sample 3D protein conformations x from a conditional distribution
x0 ∼ pθ (x|S),

(1)

where θ are the learnable weights that parameterize the neural network that acts as a score model sθ (x|S). Note
that since the dimensionality of x depends on the length of the sequence N , the dimensionality of the space
that BioEmu defines a distribution over depends on the length of S. The sampling procedure that characterizes
pθ (x|S) is given by simulating the estimated inverse of a forward diffusion process, defined by a stochastic
differential equation on the space of backbone frame representations x:
dx = f (x, t)dt + G(x, t)dw,

(2)

where w is a standard Wiener process, and f and G, drift and diffusion coefficients respectively, are functional
hyperparameters. We choose f and G such that all residues as well as their positions r and orientations Q are
corrupted independently. Specifically, the positions are corrupted with a variance-preserving SDE and a cosine
noise schedule as described in [33]. We refer the reader to [34] for further details on diffusing over the space
of orientations, SO(3). The orientations are corrupted with a geometric noise schedule so that the marginal
distribution of the change in orientation after time t is:
∞

IG SO(3) (ω, σ 2 ) =

σ 2 sin((l + 1 )ω)
1 − cos(ω) X
(2l + 1)e−l(l+1) 2
,
π
sin( ω2 )
l=0

(3)

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

where ω is the angle between rotations Qt and Q0 computed as:
ω = arccos(trace(Q⊤
t Q0 )/2 − 1/2).

(4)

We use p(x, t) to denote the probability distribution of x at diffusion time t when x is corrupted in the above way,
with the boundary condition that p(x, 0) = p(x) (the target distribution). If the initial positions r0 are bounded
(a reasonable assumption for physical protein structures centered at the origin), then p(x, 1) is close to a simple
prior distribution under which positions have a standard isotropic Gaussian distribution and orientations are
uniformly distributed.
It has been shown that by training on samples x(0) from p(x) together with corresponding samples from
the conditional distribution of x(t) given x(0), a model can approximate the score ∇x p(x, t); furthermore, if
∂
p(x, t) is
we know the score, we can construct SDEs under which the evolution of the probability density ∂t
reversed [35]. Starting by sampling positions r and orientations Q from the prior and gradually ‘denoising’ by
simulating one of these SDEs from t = 1 to t = 0, we can approximately sample from the target distribution.
Model training details are further described in Sec. S.3. For inference purposes, we smoothen the model
weights using an exponential moving average. To sample structures with the trained model, we use the secondorder sampler described in [36] with 100 denoising steps, since we found that this resulted in high-quality
samples with fewer function evaluations.

S.2.4 Score model
The score model (Fig. 1c) takes in single and pair representations of the protein sequence h := {hi }N
i=1 and
N
N
z := {zij }N
,
corrupted
frames
x
:=
{r
,
Q
}
,
relative
sequence
positions
p
:=
{p
}
,
and
a
diffusion
i
i i=1
i i=1
i,j=1
timestep t, and predicts the score sθ (x, h, z, t). It resembles the structure modules of the AlphaFold2 [27] and
Distributional Graphormer [28] models, and uses the invariant point attention (IPA) transformer architecture.
See Fig. 1c for an overview of the architecture and Algorithm 1 for a detailed description. The translation and
rotation scores produced by the score model in Algorithm 1 are defined in the local coordinate frame of each
residue, and are invariant under rotation or translation of the entire structure. During denoising, the updates
to backbone atom positions are therefore equivariant under rotation and translation of the whole structure.
Algorithm 1 Score model sθ (x, h, z, t)
Require: single representations hi , pair representations zij , positions ri , rotations Qi , timestep t, relative
sequence positions pi
1: hi ← Linear(LayerNorm(hi )) + Sinusoidal(t)
2: zij ← LinearNoBias(LayerNorm(zij )) + Embedding(Bucketize(pi ))
3: for layer=1, ..., 8 do
4:
{hi } +=Dropout(IPA({LayerNorm(hi )}, {zij }, {ri }, {Qi })
5:
hi +=Dropout(Linear(Dropout(gelu(Linear(LayerNorm(hi ))))))
6: end for
7: sr = Linear(relu(Linear(LayerNorm(hi ))))
▷ translation score
8: sQ = Linear(relu(Linear(LayerNorm(hi ))))
▷ rotation score
9: return sr , sQ

S.3 Training methodology
We start with a pretrained sequence encoder from AlphaFold2 [27], freeze its weights, and train our own structure
module from scratch. We first train on a synthetic dataset derived from AFDB, with high sequence diversity
and varied conformations for each sequence (‘AFDB pretraining’ in Table S2, se Sec. S.3.2 for details). The
pretrained model can predict diverse conformations for the same protein sequence, but does not quantitatively
match the probabilities of different states. We then fine-tune on 95% MD simulation data and folding free

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

energy measurements, mixed with 5% AFDB structures (‘Amber/∆G finetuning’ in Table S2, see Sec. S.3.4
for details), and it results in the main model BioEmu reported in this paper. We also separately finetuned the
pretrained model on DESRES fast-folders data (Sec. S.3.3), which was used to produce the results in Figures
3a, S7 but not for any other results.
In all stages, we use the standard denoising score-matching loss as in [31]. To train on experimental thermodynamic data, we add a novel loss term described in S.3.6. Table S2 provides a summary of all training settings.
We define a training epoch as the model processing 500K protein structures.
Table S2 Training hyperparameters in each stage of training
Training stage
Optimizer
β1
β2
ε
Initial LR
LR decay factor
LR scheduler patience / epochs
EMA smoothing factor
Max residues per batch per GPU
GPU type
Number of GPUs
Days to train
Training epochs
Number of seen residues

AFDB pretraining
Adam
0.9
0.999
1e-8
1e-3
None
None
0.995
A100
∼5
∼9400M

Amber/∆G finetuning
Adam
0.9
0.999
1e-8
1e-4
0.8
0.999
A100
∼5
∼5900M

DESRES finetuning
Adam
0.9
0.999
1e-8
1e-4
None
None
0.995
A100
∼3
∼4700M

S.3.1 Data splitting procedure
Having defined a list of test proteins, we removed from our training and validation data any protein whose
sequence was similar to any test protein’s sequence. Specifically, we used the mmseqs2 software [1] (version
15.6f452) and removed proteins if they have 40% or higher sequence similarity with any test protein of at least
20 residues in size, using the highest sensitivity parameter supported by the software (8.0).

S.3.2 Pre-training on AFDB
We initially train our model using a dataset derived from AFDB to encourage protein conformational variability
(see S.1.1 for details). To draw training examples from this dataset, we randomly select a sequence cluster, and
then a structure from within that cluster. While the structure is randomly selected, we always use the sequence
associated with the highest pLDDT structure in the cluster as input to the model. This effectively creates a
mapping from a sequence to multiple structures (Fig. 1e). In this stage of training, we use the standard denoising
diffusion loss [31], defined as a sum over residues. We set the loss to zero in positions where there are insertions
or deletions in the sampled structures relative to the representative sequence. The final model checkpoint was
chosen based on the performance obtained on our curated OODVal benchmark (see S.4.1). For exact training
parameters, refer to table S2.
We compared our pre-training strategy to the more straightforward approach of training the model on the
PDB. Additionally, to assess whether the performance of the model was due to an increased diversity in sequence
space, we additionally trained on foldseek [2] cluster representatives of AFDB with a pLDDT greater than 90
[37]. This constituted a set of ∼250k sequences distinct in both sequence and structure space. We found that
models trained on the PDB and the high pLDDT subset of AFDB are significantly worse in its capacity to sample
diverse conformations (Fig. S6), indicating that our curated subset of AFDB is an important contribution to
facilitate multi-conformational learning.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

S.3.3 Fine-tuning on CHARMM MD data of fast-folding proteins
For the results shown in Figs. 3a, S7, we fine-tuned our best pre-trained model (S.3.2) on a set of 12 fastfolding proteins [5] simulated with the charmm22* force field featuring sizes ranging from 10 to 80 residues. For
evaluation, this set is split into training, validation, and test subsets following a 10:1:1 ratio for each protein
(leave-one-out cross-validation). PRB is used as the system used for validation in all splits except in the one
where PRB is the test system. In that case, UVF was used instead. Specific training settings are reported in
Table S2. All fast-folders results are obtained by evaluated using the model trained in the last available training
epoch.

S.3.4 Fine-tuning on Amber MD data and experimental folding free energies
Starting from the best model identified during the pre-training stage, we perform fine tuning using the Amber
MD datasets listed in Table S1 and described in Sec. S.1.5, plus high-throughput experimental measurements of
folding free energies from [21]. In order to retain the performance of the pre-trained models, the fine-tuning data
is further augmented with 5 % of randomly-selected AFDB data, with the same settings as in the pre-training
stage. The fine-tuned model is trained with hyperparameters shown in Table S2. At this stage, in addition to
the standard denoising diffusion loss, for those proteins where this information was available, we also use a novel
loss to match experimental folding free energies by backpropagating through the sampling procedure (see S.3.6).
During each training epoch, 500 000 and 50 000 frames are sampled at with a weighted sampler and used
for training and validation, respectively. The probability weight of each frame is the product of a MD dataset
weight and a normalized frame weight. The dataset weights, given in Tab. S.3.4, were determined based on
accumulated simulation time, sequence diversity and degree of convergence of the different datasets.
Table S3 Relative MD dataset weights used for
model fine-tuning. These weights define the
proportion of samples drawn from a particular
dataset.
MD dataset

weight

FAH-DDR1
FAH-sarscov2
FAH-sarscov2-exascale
FAH-SETD8
FUB-MHCII
FUB-barnase-barstar
ONE-cath1
ONE-octapeptides
MSR-megasim-merge
MSR-cath2
MSR-megasim-mutants-mosaic-disp

0.074
0.001
0.010
0.064
0.010
0.055
0.056
0.087
0.003
0.444
0.197

Most MD datasets use a frame weight of 1, but specific weights are applied for systems belonging to the
following MD datasets:
• Systems in the ONE-octapeptides dataset are reweighted via Markov-State-Models (MSMs) so that each
state (a region of configuration space) is sampled with the frequency determined by the MSM equilibrium
probability (Sec. S.3.5.1).
• Systems in the MSR-megasim-merge and MSR-megasim-mutants-mosaic-disp datasets are reweighted based
on their foldedness so that the training distribution recovers the experimental folding free energies (see S.3.5.3).
In order to deal with systems of varying size, we define batches based on the total number of protein residues
in a batch, up 1024 or 2048 depending on the training stage (Table S2). In order to reduce overhead caused by
zero-padding, systems of similar size are grouped together when generating batches.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

S.3.5 Reweighting MD with Markov models and experimental data
To include information about equilibrium properties of the systems in our MD datasets, we have applied different
kinds of reweighting to this data, either based on Markov state models (MSMs) or experimental folding free
energies.

S.3.5.1 MSM reweighting for small peptide datasets
The data distribution generated by MD is often biased towards the seeding structure since simulations are
usually run in parallel, often starting from the same or a small number of seed structures. MSMs are a common
approach to remedy this problem [38]. In short, the classical approach first projects the 3N -dimensional protein
system into a low-dimensional representation, discretizes this projection using a clustering algorithm such as
k-means, and estimates a transition matrix on these discrete states [39]. This approach gives access to the
equilibrium probabilities via the eigenvector of that matrix that corresponds to eigenvalue 1. Such eigenvector
is then used as a probability distribution to draw samples from the MD simulation accordingly.
This analysis was applied to the ONE-octapeptide dataset, using 2D TICA projections of Cα -Cα distances
and dihedral angles. We used a lag time of 1 ns for both TICA and MSM estimation, and 100 discrete states via
k-means discretization for the MSM. The obtained equilibrium probabilities are used to draw samples during
training.

S.3.5.2 Connectivity filtering for post-hoc analyses
It is common practice to perform MSM analyses on sets of states that are reversibly connected. A connected set
of states is here referred to as one where each state is reachable from each other state via a sequence of trajectory
transitions. Since there can be several connected sets, we choose the connected set with most MD samples in
it. As obtaining a connected set from data is numerically more stable than estimating a converged equilibrium
distribution, this filter can be applied in situations where a converged MSM estimate could not be obtained.
This analysis was conducted for the ONE-cath1 dataset, based on a linear VAMP projection [56] using a
lag-time of 5 ns and residue-residue minimal distances on heavy backbone and Cβ atoms, excluding 1 residue
at each terminal and 2 neighboring residues. Subsequent connectivity analysis was conducted by counting
transitions between discretized states at a lag time of 500 ns based on the first 5 VAMP dimensions and a kmeans clustering approach to obtain 200 states. Data outside of the largest connected set was discarded from
subsequent analyses, which roughly translated to keeping 90-95% of the data on average. Free energy plots of
ONE-cath1 (i.e., CATH domains presented in Fig. 3 and Fig. S8) were based on a secondary TICA projection
obtained from trajectories inside the connected set of states.

S.3.5.3 Reweighting MD with experimental folding free energies
As detailed in S.1.5.4, we have generated MD simulation data for a subset of the sequences that are represented
in the dataset of experimental folding free energies (∆G) provided by [21]. Since the MD simulations are too
short to represent a converged sample of folding and unfolding events, the folding free energies estimated from
histogramming the raw simulation data do not match their corresponding experimental measurements but
mostly correspond to the probability that trajectories were started in folded or unfolded states. To account for
this, we reweigh the MD simulation data of each MEGAscale protein system with the corresponding experimental
∆G. For each system, first we classify all the MD conformations into folded and unfolded states, and then
sample the folded and unfolded structures with different frequencies during training, such that the ratio of folded
versus unfolded states seen by the model during training matches the target ratio given by the experimental
∆G. Specifically, the folding free energy is related to the probability under the Boltzmann distribution that a
protein will be found in a folded state.
The folding free energy ∆G can be defined in either of two directions, here we choose the convention to
define it as the change in free energy when folding, i.e. ∆G = Gfolded − Gunfolded . Then the probability of being

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

in the folded state, pfolded , is related to the folding free energy is ∆G by:



∆G
pfolded
= exp −
,
1 − pfolded
kB T

(5)

where T is the temperature and kB is the Boltzmann constant. The probability of being in the folded state can
be expressed as the expectation value of foldedness pfolded = Ex [f (x)], where f ranges from 0 (unfolded) to 1
(folded). For both our reweighting and model evaluation, we take the form of f as:
fFNC (x) = H (Q(x) − Qthreshold ) ,

(6)

where H is the Heaviside step function, Q(x) the fraction of native contacts, and Qthreshold a system-dependent
threshold. For a given protein structure x, the fraction of native contacts (FNC) is defined from pairs of residues
that are at least 3 residues apart in the amino acid sequence but which are physically within 10 Å of each other
in a reference folded structure. Specifically, we follow notations as in [40]:
Q(x) =

1 X

 ,
0 + δ)
N
1 + exp β rij (x) − λ(rij

(7)

(i,j)

are the contact distances between i and j in the configuration x and the reference conwhere rij (x) and rij
formation (native state). β = 5, λ = 1.2, and δ = 0 are constants, representing the softness of the switching
function, the reference distance tolerance and offset, respectively. For each simulated MEGAscale system, we
use its PDB structure as the reference conformation. Any given sampled structure can then be classified as
folded or unfolded by setting a threshold on the calculated FNC value.
To account for differences in the observed FNC distributions, we set the FNC threshold in a system-dependent
but unsupervised manner. Specifically, considering that we initialized multiple MD trajectories separately starting from folded and unfolded states for every protein, and those are not long enough to observe transitions, the
distribution of FNC for each system is generally separated into peaks near 1 and 0, representing folded and
unfolded states, respectively. In order to obtain a smoother distribution of FNC values for each system, we use
a kernel density estimate and then use its minimum within the range of 0.45-0.9.

S.3.6 Training on folding free energies via property prediction fine-tuning (PPFT)
Although the reweighting method encourages the model to learn the correct experimental folding free energies
with MD simulation data alone, we have empirically found that this convergence is slow, especially for systems
where unfolded states are rare (large negative ∆G). Even more importantly, experimental observables such as
∆G can only be used in a standard diffusion model training approach if folded and unfolded structures are
available, e.g. obtained via MD simulation, whose computational costs would limit us to rather few training
systems. Here we conducted a large number of MD simulations for 22,389 protein sequences from the MEGAscale
dataset, and yet this only corresponds to about 2% of the entire experimental dataset. On the other hand,
directly training diffusion models to sample distributions that match a given set of expectation values via
generation and backpropagation is computationally prohibitive. The training cost would roughly increase over
regular score matching by a factor equal to the number of denoising diffusion steps – in our case that would be
a factor 100.
To avoid these limitations and take advantage of high-throughput experiments such as the ones in [21], we
have developed a novel and efficient method that trains diffusion models to generated distributions that respect
a given set of properties of these distributions, e.g. experimental expectation values. As the method is most
likely effective with a pretrained diffusion model, we call it property-prediction fine-tuning (PPFT).
PPFT leverages that many low-dimensional properties of the distribution can be accurately predicted without performing a complete rollout of the diffusion model. Nonetheless, the training principle follows a simple
prediction and backpropagation scheme. For a given sequence with an associated experimental ∆G, we can roll
out the denoising process to generate a clean sample and compute its foldedness. We rewrite Eq. 5 to relate the

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

sample expectation value of foldedness to the folding free energy:



exp − k∆G
BT

.
Ex [f (x)] =
1 + exp − k∆G
BT

(8)

Then, we define the loss term as:
B

LdG =



1 X
f (x0i ) − ftarget f (x1i ) − ftarget ,
B i=1

(9)

where x0i and x1i are two i.i.d. samples with the same protein sequence, and ftarget is computed from the right
hand side of Eq. 8 using the experimental
∆G of the corresponding sequence. The cross term in Eq. 9 is used to

minimize the expectation Ex0i ,x1i (f (x0i ) − ftarget )(f (x1i ) − ftarget ) = (Ex [f (x)] − ftarget ) . If a standard mean


squared error loss were to be used instead, Ex (f (x) − ftarget )2 = (Ex [f (x)] − ftarget ) + Var[f (x)] would be
minimized, which contains an additional variance term that would encourage mode collapse.
We notice that the definition of foldedness f (x) by Eq. 6 is non-differentiable due to the Heaviside step
function, and the system-dependent threshold adds additional complication. In PPFT, we instead use foldedness
with the following definition:
fdRMSD (x) = σ (k (dRMSD(x) − dRMSDthreshold )) ,

(10)

where dRMSD = RMSD(D(x), D(x0 )) refers to the root mean square distance between distance matrices D(x)
of the current structure x with respect to a reference structure x0 (which is neglected in the notation for
simplicity). We choose k = −24, dRMSDthreshold = 0.4 for all protein systems. To enable backpropagation, we
use a sigmoid function σ, which is differentiable and approaches a Heaviside step function when the slope k is
sufficiently large.
In the model finetuning stage, for those systems with both simulation and experimental ∆G data, we
combined LdG with the usual score matching loss, i.e.:
L = Lscore + wLdG ,

(11)

with a weight w = 2. Even though the simulation data was reweighted using the experimental ∆G based on
the method described in Sec. S.3.4, we find that the inclusion of the LdG loss significantly sped up ∆G model
convergence.
As described above, a key requirement for PPFT to be computationally efficient is to avoid executing full
diffusion model denoising with hundreds of denoising steps. To mitigate this cost, and considering that folding/unfolding are changes easily recognizable at a coarsed-grained level at earlier denoising levels, we considered
reducing the number of integration timesteps, which sacrifices sample quality, but still predicts the foldedness
accurately. In practice, we find that 35 timesteps are sufficient when used alongside the Heun sampler. To further reduce cost, we denoised to a specified intermediate noise level t to then perform clean sample extrapolation
x̂0 using the reparameterization trick [41], with
x̂0 = (xt −

√

√
1 − ᾱt ϵ0 )/ ᾱt .

(12)

The foldedness is then predicted from x̂0 after denoising 8 out of 35 timesteps. We remark that while the coarsegrained nature of foldedness enables us to greatly reduce the number of rollout steps and model evaluations,
this may not be applicable for every properties of interest. In such scenarios the adjoint method may be needed
for computationally-affordable and numerically-stable training [42].
As a final measure towards increasing efficiency we leverage partial backpropagation, which has shown to
effectively reduce computational costs in image-related tasks [43, 44]. Here we apply backpropagation only

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

through the final extrapolation and first 3 denoising steps, i.e., in other denoising steps the score function is
detached from the computational graph. We also perform gradient accumulation to effectively increase batch
size such that the property prediction loss LdG , as an average over the batch, is closer to the actual expectation
value.
To summarize, a combination of techniques contribute to the performance of PPFT:
1. Definition of a differentiable target function,
2. Cross-target matching loss term,
3. Joint training with regular score matching,
4. Gradient accumulation,
5. Use of a higher order sampler to reduce integration timesteps
6. Extrapolation, and
7. Partial backpropagation.
We find that 2-4) are particularly helpful for reducing the mode collapse problem that results from overoptimization of the property prediction loss function, while 5-7) help to greatly reduce the rollout and backprop
steps, such that direct backpropagation is feasible with current compute requirements.

S.4 Multi-conformation benchmarking
We begin by describing which sets, as well as their rationale for inclusion and curation considerations in S.4.1.
Additional details about how we constructed an uncontaminated benchmark for evaluation is provided in S.4.2.
In S.4.3 we provide details on the summary metrics we use in order to evaluate multiconformational capabilities
of our and other competing models. Finally, in S.4.4 we provide insights into the baselines we considered to
compare against our models as well as the parameters that were chosen for them.

S.4.1 Benchmark sets
In order to evaluate the multiconformation sampling capabilities of the pre-trained and fine-tuned models, we
manually curated several sets of examples that are interesting from a structural biology point of view. For
some of the benchmarks, this curation also optionally includes manual labeling of residues where a specific
conformational change of interest happens. Full lists containing PDB and chain identifiers (label asym id), as
well as residue labels for both alignment and metric computation regions, where appropriate, are provided in
the Supplementary Data of this manuscript. Details on each individual benchmark are provided below:
• OOD60: A collection of 19 examples collected from the PDB after the AlphaFold 2 monomer model cutoff
date (Apr. 30th 2018). A 60% sequence similarity cutoff is used to remove anything from this benchmark
that is similar to any chain in the PDB prior to the specified cutoff date. This benchmark represents an
unbiased evaluation of multiconformation sampling, and contains several representative examples of the type
of conformational changes present in other benchmarks. Metric-wise, we use RMSD as defined on either a
local region, or the entirety of the protein, depending on each case.
• Domain motion: 22 examples representing large-scale hinge motions. Only global RMSD is used for
evaluation in this benchmark.
• Cryptic pocket: 34 example pairs featuring a conformational change characterized by the formation of a
binding site that is induced in a holo (bound) structure, but not on its apo (unbound) version. Many of these
examples were further curated from the CryptoSite benchmark [45] or other related works [46]. The binding
site and other parts involved in the conformational changes were manually-defined, and local RMSD was used
as a metric.
• Local unfolding: A set of 21 examples, where a certain chain segment of at least 8 residues undergoes an
unfolding transition, including some examples from the benchmark proposed in [47]. For this benchmark we
defined the segment of the protein that can unfold or detach and measure the fraction of native contacts
between this segment and the entire protein to track whether a sample was folded or unfolded.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

• OODVal: A manually-curated set of 11 examples picked after the AlphaFold 2 monomer model cutoff date
but that is disjoint from the OOD60 set detailed above, which we use for pre-trained model selection purposes.
Only global RMSD is used as a metric in this benchmark.

S.4.2 Curation of the OOD family of benchmarks
As mentioned in S.4.1, we selected pairs of references after the AlphaFold 2 monomer model cutoff date to
account for potential dataset contamination at evaluation time. We first extracted and separated all chains
for all PDB entries after the mentioned cutoff date. Each individual protein entity inside each entry is then
associated with a unique Uniprot segment via SIFTS annotations [48]. A sequence clustering procedure using
mmseqs2 is then applied on all Uniprot segments, using a minimum sequence identity threshold of 0.99. Within
each sequence cluster, we perform a structure clustering procedure on the associated PDB entities, similar to
the one reported in [49]. This included TM-score as the main comparison metric per sequence cluster followed
by an agglomerative clustering procedure as implemented in scikit-learn, with a maximum allowed TM-score
between clusters of 0.7. Benchmark pairs were selected amongst arbitrarily selected cluster representatives, as
long as both members had a minimum resolved sequence length of 50 residues, a maximum fraction of coil
residues of 0.4, a minimum shared sequence identity between resolved sequences of 0.8, and a maximum resolved
sequence length difference of 50 residues.
For the OOD60 benchmark, care was taken that the remaining pairs were at most 60% sequence-similar to
the AFDB training set. OODVal was selected as the set difference between the whole OOD and OOD60 sets.
Both sets underwent significant manual curation to ensure unphysical or unrealistic examples were excluded.
Some of the criteria applied for curation included checking whether an intra-domain conformational transition
was present, whether that occurred in a region that is resolved in both references, or filtering for chains that
formed a single long helix, as we deemed their stability outside a complex unlikely.

S.4.3 Measuring multiple conformations
For most benchmarks we used RMSD on the backbone atoms as our main metric. For the local unfolding benchmark, however, we used a Cα -only version of a contact map between the unfolding region and the
entire protein because the unfolded state has no single reference. When sampling for most multi-conformation
benchmarks, we always used the experimental sequence ( entity poly.pdbx seq one letter code can in the
mmCIF dictionary entry). In cases where the experimental sequence differed between two deposited references,
both were sampled in equal proportion. For the cryptic pocket benchmark, however, only the experimental
sequence of the apo conformation was sampled, as it is the more biologically challenging case. Global pairwise
sequence alignments were used to compute metrics as needed when the sampled sequences differed from the
experimentally-resolved reference sequences in the mmCIF files. For this, we mostly used the default parameters
of BioPython’s PairwiseAligner, apart from manually setting an open gap penalty of 0.5.
We computed two key summary statistics in order to evaluate the multiconformation capabilities of our
model, as well as to compare it against other approaches:
• Coverage: measures the fraction of sampled reference conformations, according to a chosen metric, and as a
function of different metric thresholds. We consider a conformation as covered if at least 0.1% of samples are
within a specific threshold the corresponding reference structure.
• k-recall: defined as the average of a metric for the closest 0.1% samples per reference.
Before metrics were computed, a filtering procedure was undertaken to discard unphysical samples, both
in terms of chain breaks and clashes. Specifically, we looked at Cα-Cα and C-N distances between sequenceadjacent residues and ensured that these do not surpassed 4.5Å and 2.0Å thresholds, respectively. Additionally,
distances were computed between any two backbone atoms of different residues and we ensured that samples
did not contain any such distances below a threshold of 1.0Å. Exhaustive evaluation metrics and summary
statistics for these benchmarks is provided in Figs S2-S4, and Table S4.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

S.4.4 Baseline methods
We chose AFCluster [50] and AlphaFlow [49] as baseline methods for multiple conformation generation. AFCluster is a method that relies on MSA-subsampling techniques in conjunction with AlphaFold2 to generate distinct
samples, whereas AlphaFlow, similar to this work, is a deep-learning-based generative model. For both of these
methods, MSAs were generated via using ColabFold [51] using the default parameters. In the case of AlphaFlow,
the same number of samples were drawn as for our model, whereas for AFCluster, the number of samples was
limited to the number of clustered MSAs generated by the method. AlphaFlow runs included the recommended
--self cond --resample flags when evaluated. Comparisons of our trained models against these baselines on
the proposed benchmarks is provided on Fig. S5.

S.5 Protein stability benchmarks
S.5.1 System selection
We selected proteins from ProThermDB [52] such that their experimental ∆G of unfolding ≥ 6 kcal/mol and
their asymmetric unit contains a single chain. We removed proteins with following conditions, arriving at 26
proteins for the benchmark: several proteins, including two annotated as membrane proteins, one whose sequence
was undetermined, and one that was a nucleic acid-protein complex. The initial selection comprised of 140
systems. Additionally, we curate a smaller subset consisting of 26 proteins after excluding systems with one of
the following conditions:
• proteins annotated as membrane protein
• proteins with a ligand reported under _refine_hist.pdbx_number_atoms_ligand (e.g., 1C52)
• proteins with disulfide bonds as reported under _struct_conn.conn_type_id (e.g., 1LVE)
• oligomeric proteins (e.g., 1ROP, supposedly only stable as a dimer) or proteins in protein-RNA complexes
• proteins with ligands not reported in _refine_hist.pdbx_number_atoms_ligand (e.g., 2LCP)
• proteins with repeated entries due to differing capitalization
We also use the intrinsically disordered proteins (IDPs) of the CALVADOS test set of IDRome [53, 54]
to benchmark stability, which features 65 IDPs. Sequence similarity search indicated that there was only one
protein with a similarity above 40% with respect to the training set of BioEmu.

S.5.2 Evaluating free energy predictions
We compute the ∆∆G of a mutant using the difference between its ∆G with respect to its wild type (∆∆Gmut =
∆Gmut − ∆Gwt ). In order to estimate confidence intervals in the predictions, we used the the Clopper-Pearson
method.

S.6 Energy landscape MAE
Assessing the mean absolute error on protein conformations is a non-trivial task for two reasons. a) Conformational landscapes and corresponding free energy surfaces cannot be directly assessed in 3N -dimensional space
directly, but require a projection space in which the density, and thus the free energy, are computed. b) Free
energy landscapes are often very rough and transitional regions have extremely low probabilities compared to
metastable states. The error that a model makes in predicting the relative probabilities of metastable states
with respect to each other vs. the probabilities of transition regions can be regarded as two different classes of
error. In this paper, our goal was to sample metastable states such as folded or unfolded in the correct ratio,
and therefore we focused on the first error. We have chosen the following approach to quantifying the mean
absolute error (MAE) of protein free energy landscapes over metastable protein states, which are often referred
to as macrostates: First, we parameterized a linear TICA projection (time-lagged independent component analysis [55]). Since TICA, like all dimensionality reduction techniques, is fundamentally limited by availability of
data, we have limited this analysis to a subset of test systems with sufficient MD data and to the trajectories
within the connected sets described in Sec. S.3.5.2. Second, we have chosen macrostates in the 2-dimensional

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

TICA space, and clustered using Hidden Markov models (HMMs) [56], a commonly-used approach in the analysis of MD simulations. HMMs were estimated at comparably short lagtimes of 1ns and with 3 hidden states
as a numerically stable choice.
The macrostate MAE (mMAE) was computed by assessing the relative free energies Gi within each
macrostate i by sample counting:
Gi = −kB T ln(pi ) + const,
(13)
with kB the Boltzmann constant, T the temperature, and pi the normalized histogram count for macrostate i.
As not all macrostates were sampled by our model for the systems considered, a prior count of 1 was assigned
to each macrostate. For a model with 10k samples that corresponds to clamping pi = max(pi , 10−4 ), which can
be regarded as the model resolution boundary. Relative free energies from ground truth MD distribution and
model samples are offset such that mini Gi = 0. The overall mMAE between model prediction (ML) and ground
truth (GT) was then computed as:
N

mMAE =

1 X
abs(GML
− GMD
).
i
i
N i

(14)

To evaluate BioEmu’s performance on MD-generated free energy landscapes, we have applied our mMAE
metric to a random test set from the ONE-cath1 dataset (S.1.5.2). All of these systems have > 100µs MD data.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

S.7 Supplementary Tables and Figures
Table S4 Success rates of multi-conformation benchmark
split by whether the reference was present in the AlphaFold2
monomer model training set, or whether it is a new reference
not explicitly leaked via embedding poisoning. nsuccess is the
expectation value of the number of successful predictions
computed via bootstrap, and success is defined for each type
of conformational change as described in the main text domain motion: RMSD ≤ 3Å, local unfolding: fraction of
native contacts ≤ 0.3 and ≥ 0.7, cryptic pockets RMSD
≤ 1.5Å.

Benchmark
Domain motion
Local folded
Local unfolded
Cryptic apo
Cryptic holo.
Total
Success rate

Pre-AF2 cutoff
nsuccess
N
23.89
13.16
9.00
17.00
26.96
90.01
0.744

Post-AF2 cutoff
nsuccess
N
13.64
1.00
6.30
0.00
2.00
22.94
0.740

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Vibrio cholerae LapD

mouse surfactant protein B

AcrIIC4

HigA E. coli

HzTransib transposase

mannose transporter

STING

mannose transporter

AtaTR

GpsB

BusR

biofilm-related Se0862

Transcr. antiterm. factor Qlambda

Type III secretion substrate AscX

GntR-type sialoregulator NanR

EcoT38I restriction endonuclease

type III secretion pilotin InvH

DEAD-box RNA helicase DDX21

CD9 large extracellular loop

Fig. S1 Multi-conformation benchmark: OOD60, i.e., conformational changes of proteins with sequence similarity ≤ 60% compared
with the AlphaFold2 training set. For each case, the two reference PDB structures are shown in red and yellow. Energy landscapes
show the empirical free energy sampled by the pre-trained and fine-tuned model, respectively, as a function of global Cα root mean
square deviation (RMSD) to each reference. We consider RMSDs below 3Å (dashed lines) as a successful match to the reference
structures.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Penicillin-binding protein 5

Dipeptide Binding Protein

Vibrio cholerae LapD

Biotin carboxylase

Oligopeptide-binding protein A

Pre-protein binding domain in SecA

HzTransib transposase

Hexokinase KIHxk1 (transferase)

D-ribose binding protein

Inorganic Pyrophosphatase

LAO binding protein

HigA E. coli

Transcription antitermination
factor Qlambda

Adenylate Kinase

DNA polymerase beta protein

Beta-Phosphoglucomutase

GntR-type sialoregulator NanR

Lipoprotein CD0873

Glutamine Binding Protein

L-cystine solute receptor

Calmodulin

EcoT38I restriction endonuclease

Fig. S2 Multi-conformation benchmark: Domain motions. For each case, the two reference PDB structures are shown in red
and yellow. Energy landscapes show the empirical free energy sampled by the pre-trained and fine-tuned model, respectively, as a
function of global Cα root mean square deviation (RMSD) to each reference. We consider RMSDs below 3Å (dashed lines) as a
successful match to the corresponding reference structure.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

PaaI Thioesterase

KIX Domain

Porcine OAS1

Nudix hydrolase effector

Bacteriophage T7 capsid

KRT4 binding domain

DCLK1 Kinase

Catechol O-methyltransf.

Human CaM Kinase I

PRDC

RhoA

Titin Kinase

Ras p21

Cyanobact. GAF3 domain

Trp Cage cage

Rhomboid Intram. Protease

Human CaM Kinase II

Trp Cage helix

KIX Domain

Frataxin

Pretrained
Finetuned

Fig. S3 Multi-conformation benchmark: Local unfolding. For each case, the PDB structure used as folded state reference is shown
in red, with the part can unfold highlighted. Energy landscapes show the empirical free energy sampled by the pre-trained (black)
and fine-tuned (blue) model, respectively, as a function of the fraction of native contacts (FNC) between the region that unfolds
with the entire protein. We consider samples with FNCs > 0.7 and < 0.3 as folded and unfolded states, respectively.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Fig. S4 Multi-conformation benchmark: Cryptic pockets. For each case, the two reference PDB structures are shown in red (apo)
and yellow (yellow). The holo state residues in contact with the ligand are colored black. Energy landscapes show the empirical
free energy sampled by the pre-trained and fine-tuned model, respectively, as a function of a local Cα root mean square deviation
(RMSD) of the region undergoing conformational change, to each reference. We consider RMSDs below 1.5Å (dashed lines) as a
successful match to the reference structures.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

a)
OOD60

b)
Domain
motion

c)
Cryptic
pocket
Holo

Cryptic
pocket
Apo

d)
Local
Unfolding
unfolded
state

Local
Unfolding
folded
state

Fig. S5 Multi-conformation benchmarking against AlphaFlow and AFCluster for all cases studied in Fig. 2 plus the OOD60
benchmark. Left column: Percentage of reference states covered at a given distance from the reference (higher is better). Middle
and right columns: comparison of benchmark-specific metrics for individual benchmark entries between our method (horizontal
axis) and AlphaFlow or AFCluster (vertical axis). Note that all comparisons apart from those in the OOD60 benchmark test how
well different models fit the data but it is not fair in terms of generalization. Apart from potential Evoformer embedding leakage,
for our method, all cases are in the test set, whereas for other methods cases before the AF cutoff date were present in the training
set. Our method clearly outperforms AlphaFlow and AFCluster in OOD60, Domain motion and local unfolding, and is particularly
strong when generalization is required (blue bullets). AFCluster, on the other hand, significantly outperforms our method on the
cryptic pocket benchmark, especially for sampling apo states.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Fig. S6 Multi-conformation benchmarking using different pretraining datasets on the OODVal benchmark. Left column: Percentage of reference states covered at a given distance from the reference (higher is better). Middle and right columns: comparison of
RMSD values for individual benchmark entries using Augmented AFDB pretraining (horizontal axis) or PDB/high pLDDT AFDB
training (vertical axis).

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Free energy landscapes
MD

finetuned

2ndary structure

State

pretrained

Folded

partially / unfolded

BBA
Villin
Trp-cage

BBL

α3D
Chignolin
WW domain
NTL9

Protein G
Protein B
Homeodomain λ-repressor

Fig. S7 Free energy surfaces for the DESRES fast folding proteins extracted from MD simulations (left), fine-tuned models
(center), and pre-trained model (right). Representative structures from MD (grey) and their closest counterparts from the finetuned model (green) are shown where BioEmu predicts a state.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

PDB
structure

MD

finetuned

2ndary structure

PDB
structure

MD

finetuned

2ndary structure

Fig. S8 Free energy surfaces for CATH domains of with > 100µs simulation time and their secondary structure assignments.
Energy surfaces are extracted from MD simulations (left column) and fine-tuned model (center column), respectively, secondary
structure assignments (right column) shown as averages.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

References
[1] Steinegger, M. and Söding, J. MMseqs2 enables sensitive protein sequence searching for the analysis of
massive data sets. Nature biotechnology, 35(11):1026–1028, 2017.
[2] van Kempen, M. et al. Fast and accurate protein structure search with Foldseek. Nat. Biotechnol., 42:
243–246, 2024.
[3] Huguet, G. et al. Sequence-augmented SE (3)-flow matching for conditional protein backbone generation.
arXiv:2405.20313, 2024.
[4] Krishna, R. et al. Generalized biomolecular modeling and design with RoseTTAFold All-Atom. Science,
384:eadl2528, 2024.
[5] Lindorff-Larsen, K., Piana, S., Dror, R.O. and Shaw, D.E. How fast-folding proteins fold. Science, 334
(6055):517–520, 2011.
[6] Hanson, S.M. et al. What Makes a Kinase Promiscuous for Inhibitors? Cell Chem. Biol., 26(3):390–399.e5,
2019.
[7] Chen, S. et al. The dynamic conformational landscape of the protein methyltransferase SETD8. eLife, 8:
e45403, 2019.
[8] Thomson, E.C. et al. Circulating SARS-CoV-2 spike N439K variants maintain fitness while evading
antibody-mediated immunity. Cell, 184(5):1171–1187.e20, 2021.
[9] Zimmerman, M.I. et al. SARS-CoV-2 simulations go exascale to predict dramatic spike opening and cryptic
pockets across the proteome. Nat. Chem., 13(7):651–659, 2021.
[10] Abualrous, E.T. et al. MHC-II dynamics are maintained in HLA-DR allotypes to ensure catalyzed peptide
exchange. Nat. Chem. Biol., 19(10):1196–1204, 2023.
[11] Plattner, N., Doerr, S., Fabritiis, G.D. and Noé, F. Complete protein–protein association kinetics in atomic
detail revealed by molecular dynamics simulations and Markov modelling. Nat. Chem., 9(10):1005, 2017.
[12] Eastman, P. et al. OpenMM 7: Rapid development of high performance algorithms for molecular dynamics.
PLOS Comput. Biol., 13(7):e1005659, 2017.
[13] Abraham, M.J. et al. GROMACS: High performance molecular simulations through multi-level parallelism
from laptops to supercomputers. SoftwareX, 1–2:19–25, 2015.
[14] Jorgensen, W.L., Chandrasekhar, J., Madura, J.D., Impey, R.W. and Klein, M.L. Comparison of simple
potential functions for simulating liquid water. J. Chem. Phys., 79(2):926–935, 1983.
[15] Hopkins, C.W., Le Grand, S., Walker, R.C. and Roitberg, A.E. Long-Time-Step Molecular Dynamics
through Hydrogen Mass Repartitioning. J. Chem. Theory Comput., 11(4):1864–1874, 2015.
[16] Charron, N.E. et al. Navigating protein landscapes with a machine-learned transferable coarse-grained
model. arXiv:2310.18278, 2023.
[17] Hruska, E., Abella, J.R., Nüske, F., Kavraki, L.E. and Clementi, C. Quantitative comparison of adaptive
sampling methods for protein dynamics. The Journal of Chemical Physics, 149(24):244119, December 2018.
ISSN 0021-9606, 1089-7690. doi: 10.1063/1.5053582.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

[18] Scherer, M.K. et al. PyEMMA 2: A Software Package for Estimation, Validation, and Analysis of Markov
Models. Journal of Chemical Theory and Computation, 11(11):5525–5542, November 2015. ISSN 1549-9618,
1549-9626. doi: 10.1021/acs.jctc.5b00743.
[19] Sillitoe, I. et al. CATH: Increased structural coverage of functional space. Nucleic Acids Research, 49(D1):
D266–D273, 2021.
[20] Lindorff-Larsen, K. et al. Improved side-chain torsion potentials for the Amber ff99SB protein force field.
Proteins, 78(8):1950–1958, 2010.
[21] Tsuboyama, K. et al. Mega-scale experimental analysis of protein folding stability in biology and design.
Nature, 620(7973):434–444, 2023.
[22] Maier, J.A. et al. ff14SB: Improving the Accuracy of Protein Side Chain and Backbone Parameters from
ff99SB. J. Chem. Theory Comput., 11(8):3696–3713, 2015.
[23] Robustelli, P., Piana, S. and Shaw, D.E. Developing a molecular dynamics force field for both folded and
disordered protein states. Proc. Natl. Acad. Sci. U.S.A., 115(21), 2018.
[24] Piana, S., Lindorff-Larsen, K. and Shaw, D.E. How Robust Are Protein Folding Simulations with Respect
to Force Field Parameterization? Biophys. J., 100(9):L47–L49, 2011.
[25] Duan, Y. et al. A point-charge force field for molecular mechanics simulations of proteins based on
condensed-phase quantum mechanical calculations. J. Comput. Chem., 24(16):1999–2012, 2003.
[26] Hornak, V. et al. Comparison of multiple Amber force fields and development of improved protein backbone
parameters. Proteins, 65(3):712–725, 2006.
[27] Jumper, J. et al. Highly accurate protein structure prediction with AlphaFold. Nature, 596(7873):583–589,
2021.
[28] Zheng, S. et al. Predicting equilibrium distributions for molecular systems with deep learning. Nat. Mach.
Intell., 6:558–567, 2024.
[29] Mirdita, M. et al. Uniclust databases of clustered and deeply annotated protein sequences and alignments.
Nucleic acids research, 45(D1):D170–D176, 2017.
[30] Remmert, M., Biegert, A., Hauser, A. and Söding, J. HHblits: Lightning-fast iterative protein sequence
searching by HMM-HMM alignment. Nat. Meth., 9(2):173–175, 2012.
[31] Yim, J. et al. Se (3) diffusion model with application to protein backbone generation. arXiv:2302.02277,
2023.
[32] Ahdritz, G. et al. Openfold: Retraining AlphaFold2 yields new insights into its learning mechanisms and
capacity for generalization. Nat. Meth., 21:1–11, 2024.
[33] Nichol, A. and Dhariwal, P. Improved denoising diffusion probabilistic models. arXiv:2102.09672, 2021.
[34] Bortoli, V.D. et al. Riemannian score-based generative modelling. arXiv:2202.02763, 2022.
[35] Song, Y. et al. Score-based generative modeling through stochastic differential equations. arXiv:2011.13456,
2020.
[36] Karras, T., Aittala, M., Aila, T. and Laine, S. Elucidating the design space of diffusion-based generative
models. Advances in neural information processing systems, 35:26565–26577, 2022.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

[37] Barrio-Hernandez, I. et al. Clustering predicted structures at the scale of the known protein universe.
Nature, 622(7983):637–645, 2023.
[38] Prinz, J.H. et al. Markov models of molecular kinetics: Generation and validation. The Journal of Chemical
Physics, 134(17):174105, 2011. ISSN 0021-9606, 1089-7690. doi: 10.1063/1.3565032.
[39] Wehmeyer, C. et al. Introduction to Markov state modeling with the PyEMMA software [Article v1.0].
LiveCoMS, 1(1):5965, 2018.
[40] Best, R.B., Hummer, G. and Eaton, W.A. Native contacts determine protein folding mechanisms in
atomistic simulations. Proc. Natl. Acad. Sci. USA, 110(44):17874–17879, 2013.
[41] Luo, C. Understanding diffusion models: A unified perspective. arXiv preprint arXiv:2208.11970, 2022.
[42] Domingo-Enrich, C., Drozdzal, M., Karrer, B. and Chen, R.T. Adjoint matching: Fine-tuning flow and
diffusion generative models with memoryless stochastic optimal control. arXiv:2409.08861, 2024.
[43] Xu, J. et al. Imagereward: Learning and evaluating human preferences for text-to-image generation.
Advances in Neural Information Processing Systems, 36, 2024.
[44] Clark, K., Vicol, P., Swersky, K. and Fleet, D.J. Directly fine-tuning diffusion models on differentiable
rewards. arXiv:2309.17400, 2023.
[45] Cimermancic, P. et al. CryptoSite: Expanding the druggable proteome by characterization and prediction
of cryptic binding sites. J. Mol. Biol., 428(4):709–719, 2016.
[46] Meller, A., Bhakat, S., Solieva, S. and Bowman, G.R. Accelerating cryptic pocket discovery using alphafold.
J. Chem. Theory Comput., 19(14):4355–4363, 2023.
[47] Chakravarty, D. and Porter, L.L. AlphaFold2 fails to predict protein fold switching. Prot. Sci., 31(6):
e4353, 2022.
[48] Dana, J.M. et al. Sifts: updated structure integration with function, taxonomy and sequences resource
allows 40-fold increase in coverage of structure-based annotations for proteins. Nucleic Acids Res., 47(D1):
D482–D489, 2019.
[49] Jing, B., Berger, B. and Jaakkola, T. AlphaFold meets flow matching for generating protein ensembles.
arXiv:2402.04845, 2024.
[50] Wayment-Steele, H.K. et al. Predicting multiple conformations via sequence clustering and AlphaFold2.
Nature, 625(7996):832–839, 2024.
[51] Mirdita, M. et al. Colabfold: Making protein folding accessible to all. Nat. Meth., 19(6):679–682, 2022.
[52] Nikam, R., Kulandaisamy, A., Harini, K., Sharma, D. and Gromiha, M.M. ProThermDB: Thermodynamic
database for proteins and mutants revisited after 15 years. Nucleic Acids Res., 49(D1):D420–D424, 2021.
[53] Tesei, G. et al. Conformational ensembles of the human intrinsically disordered proteome. Nature, 626
(8000):897–904, 2024.
[54] Zhu, J. et al. Precise generation of conformational ensembles for intrinsically disordered proteins via
fine-tuned diffusion models. bioRxiv, 2024. doi: 10.1101/2024.05.05.592611.
[55] Pérez-Hernández, G., Paul, F., Giorgino, T., Fabritiis, G.D. and Noé, F. Identification of slow molecular
order parameters for Markov model construction. J. Chem. Phys., 139(1):015102, 2013.

bioRxiv preprint doi: https://doi.org/10.1101/2024.12.05.626885; this version posted December 5, 2024. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

[56] Hoffmann, M. et al. Deeptime: A Python library for machine learning dynamical models from time series
data. Mach. Learn.: Sci. Technol., 3(1):015009, 2022.


---

# AlphaFold Meets Flow Matching for Generating Protein Ensembles

**Authors:** Bowen Jing, Bonnie Berger, Tommi Jaakkola
**Year:** 2024
**Venue:** arXiv preprint (ICML 2024)
**DOI:** 10.48550/arXiv.2402.04845
**Source PDF URL:** https://arxiv.org/pdf/2402.04845
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Bowen Jing 1 Bonnie Berger 1 2 Tommi Jaakkola 1

arXiv:2402.04845v2 [q-bio.BM] 2 Sep 2024

Abstract

have excelled in the single-state modeling of experimental
protein structures, they fail to account for this conformational heterogeneity (Lane, 2023; Ourmazd et al., 2022).
Hence, a method which builds upon the level of accuracy of
single-structure predictors, but reveals underlying structural
ensembles, would be of great value to structural biologists.

The biological functions of proteins often depend on dynamic structural ensembles. In this
work, we develop a flow-based generative modeling approach for learning and sampling the
conformational landscapes of proteins. We repurpose highly accurate single-state predictors
such as AlphaFold and ESMFold and fine-tune
them under a custom flow matching framework
to obtain sequence-conditioned generative models of protein structure called AlphaF LOW and
ESMF LOW. When trained and evaluated on
the PDB, our method provides a superior combination of precision and diversity compared to
AlphaFold with MSA subsampling. When further trained on ensembles from all-atom MD,
our method accurately captures conformational
flexibility, positional distributions, and higherorder ensemble observables for unseen proteins.
Moreover, our method can diversify a static
PDB structure with faster wall-clock convergence
to certain equilibrium properties than replicate
MD trajectories, demonstrating its potential as a
proxy for expensive physics-based simulations.
Code is available at https://github.com/
bjing2016/alphaflow.

Existing machine learning approaches for generating structural ensembles have focused on inference-time interventions in AlphaFold that modify the multiple sequence
alignment (MSA) input (Del Alamo et al., 2022; Stein &
Mchaourab, 2022; Wayment-Steele et al., 2023), resulting in
a different structure prediction for each version of the MSA.
While these approaches have demonstrated some success,
they suffer from two key limitations. First, by operating on
the MSA, they cannot be generalized to structure predictors
based on protein language models (PLMs) such as ESMFold
(Lin et al., 2023) or OmegaFold (Wu et al., 2022), which
have grown in popularity due to their fast runtime and ease
of use. Secondly, these inference-time interventions do not
provide the capability to train on protein ensembles from
beyond the PDB—for example, ensembles from molecular
dynamics, which are of significant scientific interest but can
be extremely expensive to simulate (Shaw et al., 2010).
To address these limitations, in this work we combine AlphaFold and ESMFold with flow matching, a recent generative modeling framework (Lipman et al., 2022; Albergo &
Vanden-Eijnden, 2022), to propose a principled method for
sampling the conformational landscape of proteins. While
AlphaFold and ESMFold were originally developed and
trained as regression models that predict a single best protein
structure for a given MSA or sequence input, we develop
a strategy for repurposing them as (sequence-conditioned)
generative models of protein structure. This synthesis relies
on the key insight that iterative denoising frameworks (such
as diffusion and flow-matching) provide a general recipe
for converting regression models to generative models with
relatively little modification to the architecture and training
objective. Unlike inference-time MSA ablation, this strategy applies equally well to PLM-based predictors and can
be used to train or fine-tune on arbitrary ensembles.

1. Introduction
Proteins adopt complex three-dimensional structures, often
as members of structural ensembles with distinct states, collective motions, and disordered fluctuations, to carry out
their biological functions. For example, conformational
changes are critical in the function of transporters, channels,
and enzymes, and the properties of equilibrium ensembles
help govern the strength and selectivity of molecular interactions (Meller et al., 2023; Vögele et al., 2023). While deep
learning methods such as AlphaFold (Jumper et al., 2021)

CSAIL, Massachusetts Institute of Technology 2 Department
of Mathematics, Massachusetts Institute of Technology. Correspondence to: Bowen Jing <bjing@mit.edu>.

While flow matching has been well established for images,
its application to protein structures remains nascent (Bose
et al., 2023). Hence, we develop a custom flow matching

Proceedings of the 41 st International Conference on Machine
Learning, Vienna, Austria. PMLR 235, 2024. Copyright 2024 by
the author(s).

A

q(x)

C

AlphaFold2
/ ESMFold

B

D

Figure 1. Conceptual overview of AlphaF LOW / ESMF LOW. (A) Samples are drawn from a harmonic (polymer-like) prior. (B) The
sample is progressively refined or denoised under a flow field controlled by the structure prediction model (AlphaFold or ESMFold). (C)
At each step, the denoised structure prediction parameterizes the direction of the flow and we interpolate the current sample towards it.
(D) The final prediction is a sample from the learned distribution of structures.

framework tailored to the architecture and training practices
of AlphaFold and ESMFold. Our framework leverages the
polymer-structured prior distribution from harmonic diffusion (Jing et al., 2023), but improves over it by defining
a scale-invariant noising process resilient to missing and
cropped residues. These improvements directly result from
the increased modeling flexibility offered by flow matching
and contribute to the performance of our method.

sequence, (2) a MSA of evolutionarily related sequences,
and optionally (3) a template structure of a related protein,
and predicts the all-atom 3D coordinates of single protein
structure. AlphaFold was developed and trained in an endto-end fashion under a regression-like FAPE loss with structures from the PDB. Later works, such as ESMFold (Lin
et al., 2023) and OmegaFold (Wu et al., 2022), modified the
pipeline by substituting the MSA with embeddings from a
protein language model (PLM) and eschewing the template
input, but otherwise kept the same architecture and training
framework as AlphaFold.

We demonstrate the performance of our flow-matching variants of AlphaFold and ESMFold—named AlphaF LOW and
ESMF LOW—in two distinct settings. First, after fine-tuning
these models only on structures from the PDB, we substantially surpass the precision-diversity Pareto frontier of MSA
ablation baselines on a test set of recently deposited conformationally heterogeneous proteins. Second, we showcase
the ability to learn from ensembles beyond the PDB by further training on the ATLAS dataset (Vander Meersche et al.,
2023) of molecular dynamics simulations. When evaluated
on test proteins structurally dissimilar from the training set,
AlphaF LOW substantially surpasses the MSA baselines in
the prediction of conformational flexibility, distributional
modeling of atomic positions, and replication of higherorder ensemble observables such as intermittent contacts
and solvent exposure. Furthermore, when a static PDB structure is provided as a template, sampling from AlphaF LOW
provides faster wall-clock convergence to many equilibrium
properties than running molecular dynamics (MD) simulation starting from that structure. Thus, our method can
be used in place of expensive simulations to diversify and
obtain equilibrium ensembles of solved protein structures.

Modeling protein ensembles. In the post-AlphaFold era,
several works have emphasized diversifying highly accurate
single-structure predictions to reflect underlying conformational heterogeneity (Lane, 2023; Chakravarty & Porter,
2022; Saldaño et al., 2022; Xie & Huang, 2023; Brotzakis et al., 2023; Bryant, 2023; Porter et al., 2023). Most
prominently, Del Alamo et al. (2022) demonstrated that
multiple functional states could be obtained by subsampling
the MSA input to AlphaFold. Since then, MSA subsampling has become the de-facto standard methodology and
has been employed to study conformational states of kinases (Faezov & Dunbrack Jr, 2023; Herrington et al., 2023;
Casadevall et al., 2023), variant effects on conformational
states (da Silva et al., 2023), and to seed molecular dynamics simulations (Vani et al., 2023). Alternative approaches
have also been proposed in the form of point mutations
to the MSA (Stein & Mchaourab, 2022; 2023) and MSA
clustering (Wayment-Steele et al., 2023). .
An emerging line of work seeks to directly train sequenceto-structure generative models of protein ensembles. EigenFold (Jing et al., 2023) and Distributional Graphormer
(Zheng et al., 2023) use harmonic diffusion and SE(3) diffusion (Yim et al., 2023), respectively, to generate ensembles.
SENS (Lu et al., 2023) is a local generative model that diver-

2. Background
Protein structure prediction. The modern approach for
protein structure prediction was pioneered by AlphaFold
(Jumper et al., 2021), which takes as input (1) the protein

sifies single starting structures via local exploration of the
conformational landscape. However, these models have yet
to show convincing validations or comparisons with MSA
subsampling methods on PDB test sets.

Text-to-image generative model

A related but separate line of work has focused on learning
generative models of Boltzmann distributions as proxies for
expensive molecular dynamics simulation. These models
were initially conceived as normalizing flows that provided
exact likelihoods and thus a means to train with energies and
reweigh samples at inference time (Noé et al., 2019; Köhler
et al., 2021; Midgley et al., 2022; Abdin & Kim, 2023; Felardos et al., 2023). However, these normalizing flows have
proven difficult to scale beyond small molecules and toy systems. More recently, the proliferation of diffusion models
has shifted the focus of this line of work towards scalability
and generalization (Arts et al., 2023; Zheng et al., 2023)
rather than exact likelihoods. Our method, when trained
on MD ensembles, can be viewed as belonging to this new
generation of Boltzmann-targeting generative models.

UNet
yorkshire terrier

Sequence-to-structure generative model

AlphaFold
MEEKLKKTKIIFVVGG…

Figure 2. AlphaFold as a denoising model. Just as (diffusionbased) text-to-image generative models are simply neural networks
that denoise images (with text input), a modified AlphaFold that ingests noisy structures and predicts clean structures (with sequence
input) immediately provides a sequence-to-structure generative
model—when trained under an appropriate framework.

Flow matching (Lipman et al., 2022; Albergo & VandenEijnden, 2022; Albergo et al., 2023; Liu et al., 2022) is a
generative modeling paradigm that resembles and builds
upon the significant success of diffusion models (Ho et al.,
2020; Song et al., 2021) in image and molecule domains.
The fundamental object in flow matching is a conditional
probability path pt (x | x1 ), t ∈ [0, 1]: a family of densities
conditioned on a data point x1 ∼ pdata which interpolates
between a shared prior distribution p0 (x | x1 ) = q(x) and
an approximate Dirac p1 (x | x1 ) ≈ δ(x − x1 ). Given a
conditional vector field ut (x | x1 ) that generates the time
evolution of pt (x | x1 ), one then learns the marginal vector
field with a neural network:
v̂(x, t; θ) ≈ v(x, t) := Ex1 ∼pt (x1 |x) [ut (x | x1 )]

solution is to leverage recent conceptual advances in generative modeling in order to simply repurpose AlphaFold—
nearly out of the box—as a generative model.
Consider, for example, the (simplified) architecture of prototypical text-to-image diffusion models (Ho et al., 2020;
Rombach et al., 2022), which aim to model conditional distributions p(x | s) of images x conditioned on text prompt s.
At the heart of these models lies a denoising neural network
(e.g., a UNet) which ingests a noisy image, along with a
text prompt, to predict a clean image. Conditioned on these
inputs, such models are otherwise are trained with simple,
regression-like MSE objectives. Analogously, a protein
structure predictor trained on a regression-like loss—like
AlphaFold or ESMFold—can be converted to a denoising
model simply by supplying an additional, noisy structure input (Figure 2). Not coincidentally, this is reminiscent of the
idea of template structures employed by certain AlphaFold
workflows. Thus, we develop an input embedding module
very similar to AlphaFold’s template embedding stack and
prepend it to the pairwise folding trunks of AlphaFold and
ESMFold (details in Appendix A.1). By doing so, we obtain structure denoising architectures that are thin wrappers
around well-validated single-structure predictors.

(1)

At convergence, the learned vector field v̂(x, t; θ) is a neural
ODE that evolves the prior distribution q(x) to the data
distribution pdata (x). Score-matching in diffusion models
can be seen as a special case of flow matching; however, as
discussed in Section 3.3, flow matching circumvents certain
difficulties that would otherwise arise with diffusion.

3. Method
3.1. AlphaFold as a Denoising Model
Given a protein sequence A of amino acid tokens, our objective is to model the distribution p(x | A) over 3D coordinates x ∈ R3×N which represents the structural ensemble of that protein sequence. Considering the enormous
intellectual efforts that went into a deterministic sequenceto-structure model (i.e., AlphaFold), developing a distributional model of equivalent accuracy and generalization
ability would appear to pose a considerable challenge. Our

With these architectural modifications, we are ready to plug
AlphaFold and ESMFold into any iterative denoising-based
generative modeling framework. Next, we will see how this
concretely applies to flow matching for protein ensembles.
3.2. Flow Matching for Protein Ensembles
Designing a flow-matching generative framework amounts

to the choice of a conditional probability path pt (x | x1 )
and its corresponding vector field ut (x | x1 ). Inspired by
the interpolant-based perspective on flow matching (Albergo
& Vanden-Eijnden, 2022), we define the conditional probability path by sampling noise x0 from the prior q(x0 ) and
interpolating linearly with the data point x1 :
x | x1 , t = (1 − t) · x0 + t · x1 ,

x0 ∼ q(x0 )

correction (Appendix A.2). Finally, (3) the networks obtain best performance (and were orginally trained) with the
SE(3)-invariant Frame Aligned Point Error (FAPE) loss.
To reconcile these issues with the flow-matching framework,
we redefine the space of protein structures to be the quotient
space R3×N /SE(3), with the prior distribution projected to
this space. We redefine the interpolation between two points
in this space to be linear interpolation in R3 after RMSDalignment. Further, because the quotient space is no longer
a vector space, there is no longer a notion of “expectation”
of a distribution; instead, we aim to learn the more general
Fréchet mean of the conditional distribution p(x1 | x):


x̂1 (x, t; θ) ≈ min Ex1 ∼pt (x1 |x) FAPE2 (x1 , x̂1 )
(7)

(2)

This probability path is associated with the vector field
ut (x | x1 ) = (x1 − x)/(1 − t)

(3)

which matches the CondOT path and field proposed in (for
example) Pooladian et al. (2023). Customarily, we then
learn a neural network to approximate the marginal vector
field according to Equation 1. However, if we instead define
a neural network x̂1 (x, t; θ) and reparameterize via
v̂(x, t; θ) = (x̂1 (x, t; θ) − x)/(1 − t)

x̂1

where we leverage the property that FAPE is a valid metric
(Jumper et al., 2021) to define a Fréchet mean. To learn this
target, we use a training loss identical to the original FAPE,
except now squared. The final result for the training and
inference procedures are provided in Algorithms 1 and 2.
An important implication of this modified framework is that
while our model is faithfully supervised on all-atom coordinates, it technically is learning the distribution only over
β-carbon coordinates. These procedures and their subtleties
are more fully discussed in Appendix A.2.

(4)

then rearrangements of Equations 1 and 4 reveal that we can
equivalently learn the expectation of x1 :
x̂1 (x, t; θ) ≈ Ex1 ∼pt (x1 |x) [x1 ]

(5)

This reparameterization is identical—up to the choice of
probability path pt (x1 | x)—to that employed for image
diffusion models (Ho et al., 2020). In our setting, since x1
refers to samples from the data distribution (i.e., protein
structures), this allows the AlphaFold-based architectures
discussed previously to be immediately used as the the denoising model x̂1 (x, t; θ), with x as the noisy input and t as
an additional time embedding.

Algorithm 1 T RAINING
Input: Training examples of structures, sequences, and
MSAs {(Si , Ai , Mi )}
for all (Si , Ai , Mi ) do
Extract x1 ← BetaCarbons(Si )
Sample x0 ∼ HarmonicPrior(length(Ai ))
Align x0 ← RMSDAlign(x0 , x1 )
Sample t ∼ Uniform[0, 1]
Interpolate xt ← t · x1 + (1 − t) · x0
Predict Ŝi ← AlphaFold(Ai , Mi , xt , t)
Optimize loss L = FAPE2 (Ŝi , Si )
end for

To apply flow matching to protein structures, we describe a
structure by the 3D coordinates of its β-carbons (α-carbon
for glycine): x ∈ RN ×3 . (We choose β-carbons because
these are the inputs to the template embedding stack.) We
then define the prior distribution q(x) over the positions of
these β-carbons to be a harmonic prior (Jing et al., 2023):
"
#
N −1
α X
q(x) ∝ exp −
∥xi − xi+1 ∥
(6)
2 i=1

Algorithm 2 I NFERENCE
Input: Sequence and MSA (A, M )
Output: Sampled all-atom structure Ŝ
Sample x0 ∼ HarmonicPrior(length(A))
for n ← 0 to N − 1 do
Let t ← n/N and s ← t + 1/N
Predict Ŝ ← AlphaFold(A, M, xt , t)
if n = N − 1 then
return Ŝ
end if
Extract x̂1 ← BetaCarbons(Ŝ)
Align xt ← RMSDAlign(xt , x̂1 )
s−t
· x̂1 + 1−s
Interpolate xs ← 1−t
1−t · xt
end for

This prior ensures that samples along the conditional probability path, and hence inputs to the neural network, always
remain polymer-like, physically plausible 3D structures.
The parameterization of learning the conditional expectation of x1 (Equation 5) suggests that the neural network
should be trained with an MSE loss. However, there are
several issues with this direct approach. (1) The structure
prediction networks not only predict β-carbon coordinates,
but also all-atom coordinates and residue frames. (2) The
input to the network is SE(3)-invariant by design, which
makes training with MSE loss unsuitable without further

3.3. Comparison with Diffusion

of AlphaFold and ESMFold (up to 10 in our experiments),
which can be somewhat expensive. To accelerate this process, we explore variants of all models where the generative
process is distilled into a single forward pass (details in
Appendix B.1). While distillation has been explored for
diffusion models (Salimans & Ho, 2022; Song et al., 2023;
Yin et al., 2023), this is (to our knowledge) the first demonstration of distillation in a protein or flow-matching setting.

Since our flow matching framework involves defining and
reversing a noising process, it bears a number of similarities
with harmonic diffusion for protein structures (Jing et al.,
2023), which converges to the same prior distribution. However, as a more general framework, flow matching offers
two key advantages. First, harmonic diffusion converges
to the prior distribution only in the infinite-time limit, and
at a rate that depends on the data dimensionality, i.e., protein size. This causes inference-time distributional shifts
when training only on crops of relatively small size, as
is the case with AlphaFold and ESMFold. On the other
hand, in flow matching, the prior distribution is imposed
as a boundary condition at time t = 0 for all dimensionalities. Second, flow matching provides an easy means to deal
with missing (gap) residues—which are very common in
the PDB—by simply omitting them in the interpolation. In
contrast, harmonic diffusion induces dependencies across
atomic positions and hence requires data imputation for
missing residues. We discuss these aspects (with additional
theoretical results) further in Appendix A.3.

4.2. PDB Ensembles
We first examine the ability of AlphaF LOW and ESMF LOW
to sample diverse conformations of proteins deposited in
the Protein Data Bank (PDB). To do, we construct a test
set of 100 proteins deposited after the AlphaFold training
cutoff (May 1, 2018) with multiple chains and evidence of
conformational heterogeneity (details in Appendix B.2). For
each protein, we sample 50 predictions with (1) unmodified AlphaFold/ESMFold (2) AlphaFold with varying degrees of MSA subsampling and (3) AlphaF LOW/ESMF LOW,
with varying degrees of flow truncation in order to tune the
amount of diversity (Appendix B.1). Each set of predictions is evaluated on three metrics: precision—the average
lDDTCα from each prediction to the closest crystal structure;
recall—the average lDDTCα from each crystal structure to
the closest prediction; and diversity—the average dissimilarity (1-lDDTCα ) between pairs of predicted structures.

4. Experiments
4.1. Training Regimen
We fine-tune all weights of AlphaFold and ESMFold on the
PDB with our flow matching framework, starting from their
publicly available pretrained weights. We use OpenFold
(Ahdritz et al., 2022) for the architecture implementation
and training pipeline and OpenProteinSet (Ahdritz et al.,
2023) for training MSAs. Adhering to the original works,
we use a training cutoff of May 1, 2018 and May 1, 2020 for
AlphaFold and ESMFold, respectively. At the conclusion
of this stage of training (1.28M and 720k examples, respectively), we obtain flow-matching variants of AlphaFold and
ESMFold which we call AlphaF LOW and ESMF LOW.

The median results across the 100 test targets are shown
in Figure 3. AlphaF LOW, similar to MSA subsampling,
increases the prediction diversity relative to the unmodified
AlphaFold at the cost of reduced precision. However, the
variants of AlphaF LOW trace a substantially superior Pareto
frontier relative to MSA subsampling. In some cases, PCA
of the ground truth and predicted ensembles (Appendix C.1)
offers an explanation for this result: in MSA subsampling,
the ensembles drift away from the true structures as the
input signal is ablated, whereas the AlphaF LOW predictions
remain clustered around the ground truth conformations
while reaching the same or greater levels of diversity. In
terms of precision and recall, AlphaF LOW exhibits very
similar behavior to MSA subsampling. Somewhat surprisingly, neither method is able to meaningfully improve aggregate recall relative to baseline AlphaFold, showing that
they generally do not succeed in increasing the coverage of
experimentally determined PDB structures, or (more optimistically) that the predicted conformational changes have
yet to be experimentally observed. Selected cases of conformational changes successfully modeled by AlphaF LOW are
visualized in Appendix C.1; Figure 8.

Next, to demonstrate and assess the ability of our method
to learn from MD ensembles, we continue fine-tuning both
models on the ATLAS dataset of all-atom MD simulations
(Vander Meersche et al., 2023), which consists of 1390
proteins chosen for structural diversity by ECOD domain
classification (Schaeffer et al., 2017). Using training and validation cutoffs of May 1, 2018 and May 1, 2019, we obtain
train/val/test splits of 1265/39/82 ensembles (2 excluded
due to length). After 43k and 27k additional training examples, respectively, we obtain MD-specialized variants of our
model which we call AlphaF LOW-MD and ESMF LOWMD. We also train variants of these models (+Templates)
which accept the PDB structure that initialized the simulation as input using a copy of the input embedding module.

Overall (as expected), ESMFold and ESMF LOW exhibit
reduced precision relative to AlphaFold-family methods.
However, ESMF LOW is able to inject substantial diversity
relative to baseline ESMFold—which, unlike AlphaFold, is

Because flow matching is an iterative generative process,
sampling a single structure requires many forward passes

0.25

0.15
0.10

MSA
subsampling
0.05
ESMFold
0.75

0.80
Precision

AlphaFold

0.82
Recall

Diversity

0.20

0.00

0.84

ESMFlow
AlphaFlow

0.80
0.78 ESMFlow
0.76

AlphaFold
0.85

AlphaFlow

MSA
ESMFold
subsampling
0.75

0.80
Precision

0.85

Figure 3. Evaluation on PDB ensembles—precision-diversity (left) and precision-recall (right) curves for all benchmarked methods
(median taken over 100 test targets). The MSA subsampling curve is traced by reducing MSA depth (max 512, min 48) and joins to
AlphaFold as they share the same weights (AlphaFold by default subsamples MSAs to a maximum depth of 1024 and thus has nonzero
diveristy, unlike ESMFold). The AlphaF LOW / ESMF LOW curves are traced by truncating the initial steps of flow matching (described in
Appendix B.1). Distilled models are marked by ▲. Tabular data is shown in Appendix C.1, Table 3

completely deterministic—and increase the recall at little to
no cost in precision. Note that this test set includes some
proteins deposited before the ESMFold cutoff; results on a
later sub-split are similar (Appendix C.1; Table 3).

flexibility in terms of root mean square fluctuation (RMSF),
both when pooled globally and pooled per-target. Remarkably, AlphaF LOW attains a median Pearson correlation of
0.85 between modeled and predicted RMSFs within a target,
while no level of MSA subsampling is able to meaningfully
exceed baseline AlphaFold on this metric.

4.3. Molecular Dynamics Ensembles

Q2: Are the atomic positions distributionally accurate?
To generalize the all-atom RMSD metric to ensembles, define the root mean Wasserstein distance (RMWD) between
ensembles X , Y as
v
u
N
u1 X
RMWD(X , Y) = t
W 2 (N [Xi ], N [Yi ]) (8)
N i=1 2

We next evaluate the ability of AlphaF LOW and ESMF LOW
to generate proxy MD ensembles for the 82 test proteins
in the ATLAS database. These test proteins have minimal
structural overlap with the training ensembles, providing a
stringent test of generalization. For each target, we sample
250 predictions with each method and probe their similarity
to the MD ensembles via a series of assessments, grouped
under three broad categories of increasing difficulty: (1)
predicting flexibility, (2) distributional accuracy, and (3)
ensemble observables. Unless otherwise noted, we focus
on AlphaF LOW ensembles generated with MSA input alone
(i.e., no PDB templates). Main results are presented in
Table 1 and Figure 5; further results (e.g. ESMF LOW, comparisons with normal mode analysis, and ablations) and
ensemble visualizations can be found in Appendix C.2. We
note that our evaluations are inherently limited to phenomena accessible within the ATLAS simulation timescales; we
do not assess if our model captures slower conformational
changes, which remain a key area for future work.

where N [Xi ] are 3D-Gaussians fit to the positional distribution of the ith atom in ensemble X (this reduces to RMSD
with a single structure). By this metric, AlphaF LOW ensembles are more accurate than any level of MSA subsampling.
Decomposition of the RMWD into a translation contribution and variance contribution (Appendix B.3) reveals that
AlphaF LOW slightly improves on AlphaFold in predicting
the mean position of atoms, and substantially outperforms
MSA subsampling in modeling the variance.
The joint distribution of Cα positions reveals collective motions and provides a more stringent test of distributional
accuracy. We project this joint distribution onto the first two
principal components from PCA—computed from the MD
ensemble alone or from equally weighting the MD and predicted ensembles—and compute the W2 -distance (in units
of Å RMSD) between the predicted and true ensembles in
this space. We also compute the (unsigned) cosine similarity between the top principal components of the predicted
and true ensembles and consider the dominant motion to
be successfully modeled if this similarity > 0.5. By all of

Q1: Is ensemble flexibility predictive of true protein
flexibility? For each ensemble, we quantify the protein
flexibility as the average Cα-RMSD between any pair of
conformations. By this metric, the AlphaF LOW ensembles
have the strongest Pearson correlation with the ground truth
and matches the aggregate level of diversity in the MD ensembles. In contrast, MSA subsampling is unable to reach
the same level of diversity while retaining any predictive
power. Similar results hold when considering atomic-level

Table 1. Evaluation on MD ensembles. For each method, we compare the predicted ensemble with the ground truth MD ensemble
according to various metrics, detailed in the main text. For protein flexibility and RMSF, the ground truth values (from the MD ensembles)
are in parenthesis. When applicable, the median across the 82 test ensembles is reported. See Appendix C.2 for ESMF LOW results. r:
Pearson correlation; ρ: Spearman correlation; J: Jaccard similarity; W2 : 2-Wasserstein distance.
AlphaF LOW-MD

MSA subsampling

AFMD+Templates

Full

Distilled

AlphaFold

Full

Distilled

Predicting
flexibility

Pairwise RMSD (= 2.90)
Pairwise RMSD r ↑
All-atom RMSF (=1.70)
Global RMSF r
Per-target RMSF r

2.89
0.48
1.68
0.60
0.85

1.94
0.48
1.28
0.54
0.81

4.40
0.03
5.38
0.13
0.51

2.34
0.12
2.29
0.23
0.52

1.67
0.22
1.17
0.29
0.51

0.72
0.15
0.49
0.26
0.55

0.58
0.10
0.31
0.21
0.52

2.18
0.94
1.31
0.91
0.90

1.73
0.92
1.00
0.89
0.88

Distributional
accuracy

Root mean W2 -dist. ↓
,→ Translation contrib. ↓
,→ Variance contrib. ↓
MD PCA W2 -dist. ↓
Joint PCA W2 -dist. ↓
% PC-sim > 0.5 ↑

2.61
2.28
1.30
1.52
2.25

3.70
3.10
1.52
1.73
3.05

6.15
5.22
3.55
2.44
5.51

5.32
3.92
2.49
2.30
4.51

4.28
3.33
2.24
2.23
3.57

3.62
2.87
2.24
1.88
3.02

3.58
2.86
2.27
1.99
2.86

1.95
1.64
1.01
1.25
1.58

2.18
1.74
1.25
1.41
1.68

Ensemble
observables

Weak contacts J ↑
Transient contacts J ↑
Exposed residue J ↑
Exposed MI matrix ρ ↑

0.62
0.41
0.50
0.25

0.52
0.28
0.48
0.14

0.40
0.23
0.34
0.14

0.40
0.26
0.37
0.11

0.37
0.27
0.37
0.10

0.30
0.27
0.33
0.06

0.27
0.28
0.32
0.02

0.62
0.47
0.50
0.25

0.51
0.42
0.47
0.18

these metrics, AlphaF LOW markedly improves over MSA
subsampling, and in particular nearly doubles the success
rate for obtaining > 0.5 cosine similarity.

Global RMSF r

0.9

2.50

0.8

Q3: Are complex ensemble observables faithfully reproduced? MD ensembles are often intended for downstream
analysis of observables such as intermittent contacts and
solvent exposure, often associated with thermal fluctuations
around the low-energy crystal structure (Vögele et al., 2022).
To probe if we model these properties accurately, for each
ensemble we identify the set of weak contacts and transient
contacts, defined as those Cα pairs which are in contact (respectively, not in contact) in the crystal structure but which
dissociate (respectively, associate) in > 10% of ensemble
structures, with a 8 Å threshold. We then compute the
the Jaccard similarity of the sets produced by each method
with the ground truth sets. We repeat the same analysis
with the set of cryptically exposed residues—those whose
sidechains are buried in the crystal structure but exposed to
solvent in > 10% of ensemble structures—which are a key
feature in the identification of cryptic pockets in drug discovery (Meller et al., 2023). Going further, for each pair of
residues we compute the mutual information (MI) between
their (binary) exposure states, yielding a MI matrix for each
ensemble. Such matrices are an important in the so-called
exposon analysis of protein dynamics, e.g., for collective
motions and allostery (Porter et al., 2019). We then compute the Spearman correlation between the values of MI
matrices from the MD and generated ensembles. Impressively, for all of these analyses, AlphaF LOW substantially
outperforms MSA subsampling; we emphasize that these
are complex properties to emulate involving sidechains and
different parts of the protein (Figure 5 and Appendix C.2).

RMWD

2.75
2.25
2.00

0.7

MD PCA

2-dist

PC sim > 0.5 %

1.8

1.6

1.4

0.01

0.1
GPU-hrs

0.01

0.1
GPU-hrs

Figure 4. Efficiency of AlphaF LOW vs replicate MD simulations. AlphaF LOW+Templates with varying number of samples
with distillation (green) and without distillation (orange); MD with
varying trajectory lengths in blue. See Appendix B.3 for further
experimental details and Appendix C.2 for further results.

Diversifying solved structures. Although we have so far
focused on generating protein ensembles without the use
of experimental structures, there is substantial scientific interest in obtaining ensembles for specific solved structures,
often via molecular dynamics simulation (Hollingsworth &
Dror, 2018). To investigate the utility of our method in this
application setting, we repeat all experiments by providing
the structure which initialized the ATLAS simulations to the
+Templates version of AlphaF LOW-MD. As expected, the
resulting ensembles improve—sometimes substantially—in
their similarity to the ground truth MD ensemble, vastly
surpasssing the performance of MSA subsampling. How7

MD

A

AlphaFlow

MSA subsampling

r = 0.90

6uof_A

r = 0.41

Crystal

AlphaFlow

6q9c_A

19%

12%

6d7y_B

59%

65%

86%

77%

D

E

C

7bwf_B ( = 0.46)

AlphaFlow
MSA subsampling
AlphaFold

MD

1 - CDF

1 B

MD

6oz1_A

F

AlphaFlow

Cosine sim

Figure 5. MD evaluations visualized. (A) Ensembles of PDB ID 6uof A (transcriptional regulator from Streptococcus pneumoniae)
from MD, AlphaF LOW, and MSA subsampling (depth 48), with Cα RMSF by residue index shown in insets. (B) 1 − CDF of the
distribution of (unsigned) cosine similarities between the top principal components of the predicted ensemble versus the MD ensemble. (C)
Solvent exposure mutual information matrices computed from the ground truth MD ensemble and AlphaF LOW ensemble for target PDB
ID 7bwf B (antitoxin from Staphylococcus aureus). (D, E, F) Deviations from the crystal structure in the MD simulation, corresponding
to ensemble observables, which are correctly sampled by AlphaF LOW. The probability of occurence in each ensembles is shown. (D)
solvent exposure of a buried residue in PDB ID 6oz1 A (carboxylate reductase from M. chelonae). (E) association of a transient residue
contact in PDB ID 6q9c A (NADH-quinone oxidoreductase subunit E from Aquifex aeolicus). (F) dissociation of a weak residue contact
in PDB ID 6d7y B (immune protein from Enterobacter cloacae). Additional examples in Appendix C.2 r: Pearson correlation; ρ:
Spearman correlation.

5. Conclusion

ever, in these settings, the appropriate baseline is replicate
simulations (provided in ATLAS) starting from the same
structure rather than MSA subsampling. Since MD is taken
to be the ground truth but is expensive to run to convergence,
we investigate if AlphaF LOW provides better results for an
equivalent limited computational budget, e.g., in terms of
GPU-hrs. To emulate these budgets, we reduce the number
of samples drawn from AlphaF LOW (from 250 to as few as
4) and the length of the MD trajectory (100 ns–160 ps). As
shown in Figure 4, the AlphaF LOW ensembles retain much
of their quality with up to a 10x reduction in samples, while
the MD trajectories require much longer to converge to or
surpass the same quality. The distilled AlphaF LOW model,
despite converging to a lower level of performance, provides
an even greater improvement for short timescales by providing 10x as many samples for the same runtime. Thus, as
measured by these metrics, AlphaF LOW provides a more
efficient means to study the thermodynamic fluctuations of
existing solved structures than short MD simulations and
holds promise for large-scale diversification of the PDB.

We have presented AlphaF LOW and ESMF LOW, which combine AlphaFold and ESMFold with flow-matching towards
the goal of sampling protein ensembles. Compared to existing approaches for obtaining multiple structure predictions,
our method goes beyond inference-time input modifications
and develops a more principled training-time approach to
modeling structural diversity. Comprehensive experimental results demonstrate the utility and performance of our
method in predicting precise and diverse PDB structures and
replicating distributions and properties of MD ensembles,
both with and without initial experimental structures. We
anticipate these capabilities to have broad and exciting applications for structure biology. Further, with the increasing
availability of high-resolution cryo-EM data (Kühlbrandt,
2014) and algorithms for resolving their structural heterogeneity (Zhong et al., 2021), we anticipate the paradigm
of generative training of AlphaFold and ESMFold to have
further applications beyond the settings considered here.

Acknowledgements

Arts, M., Garcia Satorras, V., Huang, C.-W., Zugner, D.,
Federici, M., Clementi, C., Noé, F., Pinsler, R., and
van den Berg, R. Two for one: Diffusion models and force
fields for coarse-grained molecular dynamics. Journal of
Chemical Theory and Computation, 19(18):6151–6159,
2023.

We thank Ruochi Zhang, Hannes Stärk, Samuel Sledzieski,
Soojung Yang, Jason Yim, Rachel Wu, Hannah WaymentSteele, Umesh Padia, Sergey Ovchinnikov, Andrew Campbell, Gabriele Corso, Jeremy Wohlwend, Mateo Reveiz,
Martin Vögele, Daniel Richman, Jessica Karaguesian, Alex
Powers, and anonymous ICML reviewers for helpful feedback and discussions.

Atilgan, A. R., Durell, S., Jernigan, R. L., Demirel, M. C.,
Keskin, O., and Bahar, I. Anisotropy of fluctuation dynamics of proteins with an elastic network model. Biophysical journal, 80(1):505–515, 2001.

This work was supported by the National Institute of General
Medical Sciences of the National Institutes of Health under
award number 1R35GM141861-01 and the U.S. Department
of Energy, Office of Science, Office of Advanced Scientific
Computing Research, Department of Energy Computational
Science Graduate Fellowship under Award Number DESC0022158. We acknowledge support from NSF Expeditions grant (award 1918839: Collaborative Research: Understanding the World Through Code), the Machine Learning
for Pharmaceutical Discovery and Synthesis (MLPDS) consortium, the Abdul Latif Jameel Clinic for Machine Learning in Health, the DTRA Discovery of Medical Countermeasures Against New and Emerging (DOMANE) threats
program, and the DARPA Accelerated Molecular Discovery program. This research used resources of the National
Energy Research Scientific Computing Center (NERSC),
a Department of Energy Office of Science User Facility
using NERSC awards ASCR-ERCAP0027302 and ASCRERCAP0027818.

Bahar, I., Atilgan, A. R., and Erman, B. Direct evaluation of
thermal fluctuations in proteins using a single-parameter
harmonic potential. Folding and Design, 2(3):173–181,
1997.
Bakan, A., Meireles, L. M., and Bahar, I. Prody: protein
dynamics inferred from theory and experiments. Bioinformatics, 27(11):1575–1577, 2011.
Bose, A. J., Akhound-Sadegh, T., Fatras, K., Huguet, G.,
Rector-Brooks, J., Liu, C.-H., Nica, A. C., Korablyov,
M., Bronstein, M., and Tong, A. Se (3)-stochastic flow
matching for protein backbone generation. arXiv preprint
arXiv:2310.02391, 2023.
Brotzakis, Z. F., Zhang, S., and Vendruscolo, M. Alphafold
prediction of structural ensembles of disordered proteins.
bioRxiv, pp. 2023–01, 2023.

References

Bryant, P. Structure prediction of alternative protein conformations. bioRxiv, pp. 2023–09, 2023.

Abdin, O. and Kim, P. M. Pepflow: direct conformational sampling from peptide energy landscapes through
hypernetwork-conditioned diffusion. bioRxiv, pp. 2023–
06, 2023.

Casadevall, G., Duran, C., and Osuna, S. Alphafold2 and
deep learning for elucidating enzyme conformational flexibility and its application for design. JACS Au, 3(6):1554–
1562, 2023.

Ahdritz, G., Bouatta, N., Kadyan, S., Xia, Q., Gerecke, W.,
O’Donnell, T. J., Berenberg, D., Fisk, I., Zanichelli, N.,
Zhang, B., et al. Openfold: Retraining alphafold2 yields
new insights into its learning mechanisms and capacity
for generalization. bioRxiv, pp. 2022–11, 2022.

Chakravarty, D. and Porter, L. L. Alphafold2 fails to predict
protein fold switching. Protein Science, 31(6):e4353,
2022.
Chen, R. T. and Lipman, Y. Riemannian flow matching on
general geometries. arXiv preprint arXiv:2302.03660,
2023.

Ahdritz, G., Bouatta, N., Kadyan, S., Jarosch, L., Berenberg,
D., Fisk, I., Watkins, A. M., Ra, S., Bonneau, R., and
AlQuraishi, M. Openproteinset: Training data for structural biology at scale. arXiv preprint arXiv:2308.05326,
2023.

Chen, T., Zhang, R., and Hinton, G. Analog bits: Generating discrete data using diffusion models with selfconditioning. arXiv preprint arXiv:2208.04202, 2022.

Albergo, M. S. and Vanden-Eijnden, E. Building normalizing flows with stochastic interpolants. In The Eleventh
International Conference on Learning Representations,
2022.

da Silva, G. M., Cui, J. Y., Dalgarno, D. C., Lisi, G. P.,
and Rubenstein, B. M. Predicting relative populations
of protein conformations without a physics engine using
alphafold2. bioRxiv, 2023.

Albergo, M. S., Boffi, N. M., and Vanden-Eijnden, E.
Stochastic interpolants: A unifying framework for flows
and diffusions. arXiv preprint arXiv:2303.08797, 2023.

Dana, J. M., Gutmanas, A., Tyagi, N., Qi, G., O’Donovan,
C., Martin, M., and Velankar, S. Sifts: updated structure integration with function, taxonomy and sequences

resource allows 40-fold increase in coverage of structurebased annotations for proteins. Nucleic acids research,
47(D1):D482–D489, 2019.

Lane, T. J. Protein structure prediction has reached the
single-structure frontier. Nature Methods, 20(2):170–173,
2023.

Del Alamo, D., Sala, D., Mchaourab, H. S., and Meiler, J.
Sampling alternative conformational states of transporters
and receptors with alphafold2. Elife, 11:e75751, 2022.

Larkin, M. A., Blackshields, G., Brown, N. P., Chenna, R.,
McGettigan, P. A., McWilliam, H., Valentin, F., Wallace,
I. M., Wilm, A., Lopez, R., et al. Clustal w and clustal x
version 2.0. bioinformatics, 23(21):2947–2948, 2007.

Diepeveen, W., Esteve-Yagüe, C., Lellmann, J., Öktem,
O., and Schönlieb, C.-B. Riemannian geometry for efficient analysis of protein dynamics data. arXiv preprint
arXiv:2308.07818, 2023.

Lin, Z., Akin, H., Rao, R., Hie, B., Zhu, Z., Lu, W.,
Smetanin, N., Verkuil, R., Kabeli, O., Shmueli, Y., et al.
Evolutionary-scale prediction of atomic-level protein
structure with a language model. Science, 379(6637):
1123–1130, 2023.

Ellaway, J. I., Anyango, S., Nair, S., Zaki, H. A., Nadzirin,
N., Powell, H. R., Gutmanas, A., Varadi, M., and Velankar, S. Identifying protein conformational states in the
pdb and comparison to alphafold2 predictions. bioRxiv,
pp. 2023–07, 2023.

Lipman, Y., Chen, R. T., Ben-Hamu, H., Nickel, M., and
Le, M. Flow matching for generative modeling. In The
Eleventh International Conference on Learning Representations, 2022.

Faezov, B. and Dunbrack Jr, R. L. Alphafold2 models of
the active form of all 437 catalytically-competent typical
human kinase domains. bioRxiv, pp. 2023–07, 2023.

Liu, X., Gong, C., and Liu, Q. Flow straight and fast:
Learning to generate and transfer data with rectified flow.
arXiv preprint arXiv:2209.03003, 2022.

Felardos, L., Hénin, J., and Charpiat, G. Designing losses
for data-free training of normalizing flows on boltzmann
distributions. arXiv preprint arXiv:2301.05475, 2023.

Lu, J., Zhong, B., and Tang, J. Score-based enhanced sampling for protein molecular dynamics. arXiv preprint
arXiv:2306.03117, 2023.

Herrington, N. B., Stein, D., Li, Y. C., Pandey, G., and
Schlessinger, A. Exploring the druggable conformational
space of protein kinases using ai-generated structures.
bioRxiv, pp. 2023–08, 2023.

McGibbon, R. T., Beauchamp, K. A., Harrigan, M. P., Klein,
C., Swails, J. M., Hernández, C. X., Schwantes, C. R.,
Wang, L.-P., Lane, T. J., and Pande, V. S. Mdtraj: a
modern open library for the analysis of molecular dynamics trajectories. Biophysical journal, 109(8):1528–1532,
2015.

Ho, J., Jain, A., and Abbeel, P. Denoising diffusion probabilistic models. Advances in neural information processing systems, 33:6840–6851, 2020.

Meller, A., Ward, M., Borowsky, J., Kshirsagar, M., Lotthammer, J. M., Oviedo, F., Ferres, J. L., and Bowman,
G. R. Predicting locations of cryptic pockets from single protein structures using the pocketminer graph neural
network. Nature Communications, 14(1):1177, 2023.

Hollingsworth, S. A. and Dror, R. O. Molecular dynamics
simulation for all. Neuron, 99(6):1129–1143, 2018.
Jing, B., Erives, E., Pao-Huang, P., Corso, G., Berger, B.,
and Jaakkola, T. S. Eigenfold: Generative protein structure prediction with diffusion models. In ICLR 2023Machine Learning for Drug Discovery workshop, 2023.

Midgley, L. I., Stimper, V., Simm, G. N., Schölkopf, B.,
and Hernández-Lobato, J. M. Flow annealed importance
sampling bootstrap. arXiv preprint arXiv:2208.01893,
2022.

Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M.,
Ronneberger, O., Tunyasuvunakool, K., Bates, R., Žı́dek,
A., Potapenko, A., et al. Highly accurate protein structure
prediction with alphafold. Nature, 596(7873):583–589,
2021.

Noé, F., Olsson, S., Köhler, J., and Wu, H. Boltzmann generators: Sampling equilibrium states of many-body systems
with deep learning. Science, 365(6457):eaaw1147, 2019.
Ourmazd, A., Moffat, K., and Lattman, E. E. Structural
biology is solved—now what? Nature methods, 19(1):
24–26, 2022.

Köhler, J., Krämer, A., and Noé, F. Smooth normalizing
flows. Advances in Neural Information Processing Systems, 34:2796–2809, 2021.

Pooladian, A.-A., Ben-Hamu, H., Domingo-Enrich, C.,
Amos, B., Lipman, Y., and Chen, R. Multisample flow
matching: Straightening flows with minibatch couplings.
arXiv preprint arXiv:2304.14772, 2023.

Kühlbrandt, W. The resolution revolution. Science, 343
(6178):1443–1444, 2014.

Porter, J. R., Moeder, K. E., Sibbald, C. A., Zimmerman,
M. I., Hart, K. M., Greenberg, M. J., and Bowman, G. R.
Cooperative changes in solvent exposure identify cryptic
pockets, switches, and allosteric coupling. Biophysical
Journal, 116(5):818–830, 2019.

Stein, R. A. and Mchaourab, H. S. Rosetta energy analysis
of alphafold2 models: Point mutations and conformational ensembles. bioRxiv, pp. 2023–09, 2023.
Steinegger, M. and Söding, J. Mmseqs2 enables sensitive protein sequence searching for the analysis of massive data sets. Nature biotechnology, 35(11):1026–1028,
2017.

Porter, L. L., Chakravarty, D., Schafer, J. W., and Chen,
E. A. Colabfold predicts alternative protein structures
from single sequences, coevolution unnecessary for afcluster. bioRxiv, pp. 2023–11, 2023.

Tancik, M., Srinivasan, P., Mildenhall, B., Fridovich-Keil,
S., Raghavan, N., Singhal, U., Ramamoorthi, R., Barron, J., and Ng, R. Fourier features let networks learn
high frequency functions in low dimensional domains.
Advances in Neural Information Processing Systems, 33:
7537–7547, 2020.

Rombach, R., Blattmann, A., Lorenz, D., Esser, P., and
Ommer, B. High-resolution image synthesis with latent
diffusion models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp.
10684–10695, 2022.

Vander Meersche, Y., Cretin, G., Gheeraert, A., Gelly, J.-C.,
and Galochkina, T. Atlas: protein flexibility description
from atomistic molecular dynamics simulations. Nucleic
Acids Research, pp. gkad1084, 2023.

Saldaño, T., Escobedo, N., Marchetti, J., Zea, D. J.,
Mac Donagh, J., Velez Rueda, A. J., Gonik, E.,
Garcı́a Melani, A., Novomisky Nechcoff, J., Salas, M. N.,
et al. Impact of protein conformational diversity on alphafold predictions. Bioinformatics, 38(10):2742–2748,
2022.

Vani, B. P., Aranganathan, A., Wang, D., and Tiwary, P.
Alphafold2-rave: From sequence to boltzmann ranking.
Journal of Chemical Theory and Computation, 2023.

Salimans, T. and Ho, J. Progressive distillation for
fast sampling of diffusion models. arXiv preprint
arXiv:2202.00512, 2022.

Vögele, M., Thomson, N. J., Truong, S. T., McAvity, J.,
Zachariae, U., and Dror, R. O. Systematic analysis
of biomolecular conformational ensembles with pensa.
arXiv preprint arXiv:2212.02714, 2022.

Schaeffer, R. D., Liao, Y., Cheng, H., and Grishin, N. V.
Ecod: new developments in the evolutionary classification of domains. Nucleic acids research, 45(D1):D296–
D302, 2017.

Vögele, M., Zhang, B. W., Kaindl, J., and Wang, L. Is
the functional response of a receptor determined by the
thermodynamics of ligand binding? Journal of Chemical
Theory and Computation, 2023.

Shaw, D. E., Maragakis, P., Lindorff-Larsen, K., Piana, S.,
Dror, R. O., Eastwood, M. P., Bank, J. A., Jumper, J. M.,
Salmon, J. K., Shan, Y., et al. Atomic-level characterization of the structural dynamics of proteins. Science, 330
(6002):341–346, 2010.

Wayment-Steele, H. K., Ojoawo, A., Otten, R., Apitz, J. M.,
Pitsawong, W., Hömberger, M., Ovchinnikov, S., Colwell,
L., and Kern, D. Predicting multiple conformations via
sequence clustering and alphafold2. Nature, pp. 1–3,
2023.

Song, Y., Sohl-Dickstein, J., Kingma, D. P., Kumar, A., Ermon, S., and Poole, B. Score-based generative modeling
through stochastic differential equations. In International
Conference on Learning Representations, 2021.

Wu, R., Ding, F., Wang, R., Shen, R., Zhang, X., Luo,
S., Su, C., Wu, Z., Xie, Q., Berger, B., et al. Highresolution de novo structure prediction from primary sequence. BioRxiv, pp. 2022–07, 2022.

Song, Y., Dhariwal, P., Chen, M., and Sutskever, I. Consistency models. arXiv preprint arXiv:2303.01469, 2023.

Xie, T. and Huang, J. Can protein structure prediction
methods capture alternative conformations of membrane
proteins? bioRxiv, pp. 2023–08, 2023.

Stärk, H., Jing, B., Barzilay, R., and Jaakkola, T. Harmonic
self-conditioned flow matching for multi-ligand docking
and binding site design. arXiv preprint arXiv:2310.05764,
2023.

Yim, J., Trippe, B. L., De Bortoli, V., Mathieu, E., Doucet,
A., Barzilay, R., and Jaakkola, T. Se (3) diffusion model
with application to protein backbone generation. arXiv
preprint arXiv:2302.02277, 2023.

Stein, R. A. and Mchaourab, H. S. Speach af: Sampling protein ensembles and conformational heterogeneity with alphafold2. PLOS Computational Biology, 18(8):e1010483,
2022.

Yin, T., Gharbi, M., Zhang, R., Shechtman, E., Durand,
F., Freeman, W. T., and Park, T. One-step diffusion
with distribution matching distillation. arXiv preprint
arXiv:2311.18828, 2023.

Zheng, S., He, J., Liu, C., Shi, Y., Lu, Z., Feng, W., Ju,
F., Wang, J., Zhu, J., Min, Y., et al. Towards predicting
equilibrium distributions for molecular systems with deep
learning. arXiv preprint arXiv:2306.05445, 2023.
Zhong, E. D., Bepler, T., Berger, B., and Davis, J. H. Cryodrgn: reconstruction of heterogeneous cryo-em structures
using neural networks. Nature methods, 18(2):176–185,
2021.

A. Method Details
A.1. Input Embedding Module
Algorithm 3 outlines the architecture of the input embedding module which we attach to AlphaFold and ESMFold to form
AlphaF LOW and ESMF LOW, respectively. The output of the module is added to the input to the Evoformer or folding trunk.
The various subroutines are as defined in AlphaFold (Jumper et al., 2021), whereas the Gaussian Fourier time embeddings
are as previously used in Song et al. (2021); Tancik et al. (2020). For brevity, we have omitted droupout layers.
Algorithm 3 I NPUT E MBEDDING
Input: Beta carbon coordinates x ∈ RN ×3 , time t ∈ [0, 1]
Output: Input pair embedding z ∈ RN ×N ×64
zij ← ∥xi − xj ∥
zij ← Bin(zij , min = 3.25 Å, max = 50.75 Å, Nbins = 39)
zij ← Linear(OneHot(zij ))
for l ← 1 to Nblocks = 4 do
{z}ij += TriangleAttentionStartingNode(zij , c = 64, Nhead = 4)
{z}ij += TriangleAttentionEndingNode(zij , c = 64, Nhead = 4))
{z}ij += TriangleMultiplicationOutgoing(zij , c = 64)
{z}ij += TriangleMultiplicationIncoming(zij , c = 64)
{z}ij += PairTransition(zij , n = 2)
end for
zij += Linear(GaussianFourierEmbedding(t, d = 256))

A.2. Flow Matching on Protein Ensembles
In this subsection, we describe how the final training and inferences Algorithms 1 and 2 are obtained, starting from the
Euclidean flow matching procedure from a harmonic prior provided in Section 3.2, Equations 2–6. We note that other
diffusion or flow matching formulations are also possible and leave further exploration of this design space to future work.
Unsuitability of MSE Loss In standard flow matching over R3N , the denoising network x̂(x, t; θ) is designed to
approximate x̂1 (x, t; θ) ≈ Ex1 ∼pt (x1 |x) [x1 ], which gives rise to the MSE training objective


Lt (θ) = Ex1 ∼pdata ,x∼pt (x|x1 ) ∥x̂1 (x, t; θ) − x1 ∥2


= Ex1 ∼pdata ,x0 ∼q ∥x̂1 (x, t; θ) − x1 ∥2

(9)

where x = (1 − t) · x0 + t · x1 , for each time t ∈ [0, 1]. The harmomic prior density q and the data distribution pdata are
SE(3)-invariant (technically SO(3)-invariant after centering; see for example Yim et al. (2023)). This means that, for each
training pair (x0 , x1 ), there is a corresponding uniform density over R ∈ SO(3) supplying examples (R.x0 , R.x1 ):
"Z
#
∥x̂1 (R.x, t; θ) − R.x1 ∥2 dR

Lt (θ) = Ex1 ∼pdata ,x0 ∼q

(10)

SO(3)

However, because the input embedding takes only a distogram of x, the denoising model x̂1 , i.e., AlphaFold or ESMFold, is
SE(3)-invariant, meaning that
x̂1 (x, t; θ) = x̂1 (R.x, t; θ)
(11)
for any R ∈ SO(3) ⊂ SE(3). Hence, the denoising network is tasked with predicting R.x1 despite having no access to
R. This is impossible and would lead to the network to degenerately predict x̂1 = 0, showing that the MSE loss (or more
broadly any non-SE(3)-invariant) loss is unsuitable with a SE(3)-invariant denoising network.
Flow Matching on the Quotient Space To resolve the issue that AlphaFold and ESMFold are insensitive to SE(3)
transformations of the input, we consider flow matching over the quotient space R3N /SE(3), such that inputs related by
SE(3) transformations are now defined to be identical. This quotient space, when defined with suitable care (Diepeveen

et al., 2023), gives a non-Euclidean, Riemannian manifold. The harmonic prior and data distribution can be straightforwardly
projected to this space by taking the SE(3) equivalency classes of each data point. The theory of flow matching over
Riemmanian manifolds was developed by Chen & Lipman (2023) and closely follows standard flow matching, except the
conditional vector fields and the learned marginal vector fields are elements of the tangent space:
ut (x | x1 ) ∈ Tx M,

v̂(x, t; θ) := Ex1 ∼pt (x1 |x) [ut (x | x1 )] ∈ Tx M

(12)

As in the Euclidean case, to develop a flow matching process, we require a conditional probability path and a corresponding
conditional vector field. Chen & Lipman (2023) propose to generalize the CondOT probability path by defining the
interpolant ψt (x0 | x1 ) to be the geodesic from x0 to x1 , and then specifying pt (x | x0 ) via
x | x1 = ψt (x0 | x1 ),

x0 ∼ q(x0 )

(13)

and the associated conditional vector field as
ut (x | x1 ) =

d
ψt (x0 | x1 )
dt

(14)

Once the marginal vector field is learned, inference is performed by integrating the corresponding ODE over the manifold.
To use this framework with protein structures and AlphaFold or ESMFold as the flow model, we make the following tweaks:
(1) We construct the interpolation between two elements in the quotient space R3N /SE(3) to be given by RMSD alignment
in the ambient space R3N , followed by linear interpolation in ambient space. Thus, as employed in Algorithm 1, the
conditional probability path is sampled via
x0 ∼ q(x0 )
x0 ← RMSDAlign(x0 , x1 )

(15)

x | x1 = (1 − t) · x0 + t · x1
(2) Similar to the Euclidean case, we consider a reparameterization (cf. Equation 4) which allows a denoising model
x̂1 (x, t; θ) such as AlphaFold or ESMFold to give the direction of the learned marginal flow:
v̂(x, t; θ) =

logx x̂1 (x, t; θ)
1−t

(16)

where the logarithmic map gives the direction of the interpolation connecting x to x̂1 (x, t; θ) (discussed next). Unlike the
Euclidean case, however, this expression does not provide a simple training objective for x1 in terms of a denoising loss.
This is because flow matching requires minimizing error in the tangent space, which may not be easily related to distances
on the manifold. Nevertheless, we posit that a model which minimizes denoising error can do a good job of implicitly
learning the vector field. Thus, for some choice of distance metric d over the manifold, we aim to learn the so-called Fréchet
mean of the clean data distribution conditioned on noisy data:


x̂1 (x, t; θ) ≈ arg min Ex1 ∼pt (x1 |x) d2 (x1 , x̂1 )
x̂∈M

(17)

As a sanity check, note that when M is a Euclidean space and d is Euclidean distance, d2 reduces to the usual MSE
denoising loss whose minimizer is the conditional expectation of pt (x1 | x), in agreement with Equation 5.
(3) At inference time, in lieu of repeatedly evaluating the logarithmic map and integrating the vector field with the exponential
map, we observe that such a procedure amounts to moving along the interpolant connecting x to x̂1 :

expx [v̂(x, t; θ) dt] = expx


dt
logx x̂1 (x, t; θ)
1−t

(18)

i.e., a fraction dt/(1 − t) towards x̂1 . Hence, we take an integration step at inference-time via RMSD alignment followed
by linear interpolation in ambient space, as executed in Algorithm 2.

FAPE and All-Atom Structure As defined in Section 3.2, our flow matching framework operates over residue-level
structures; specifically, over Cβ coordinates x ∈ R3N . However, the FAPE loss is defined over structures also containing (1)
all-atom positions and (2) residue frames, and indeed we continue to supervise these outputs to ensure that AlphaF LOW
and ESMF LOW produce meaningful all-atom structures. To reconcile these views, let S denote an all-atom structure, let
[ · ]Cβ be the operator that extracts the Cβ coordinates, and denote the denoising model as Ŝ(x, t; θ). Most of training and
inference proceeds as if all structures were passed through the [ · ]Cβ operator: training points are sampled via x1 = [S]Cβ
before noisy interpolation; and inference proceeds by parameterizing the Cβ denoising model as
h
i
x̂1 (x, t; θ) = Ŝ(x, t; θ)
(19)
Cβ

However, this extraction is not applied to compute the denoising loss—neither to the sampled data nor the prediction.
Instead, the denoising model is trained to approximate (cf. Equation 17):
h
i
Ŝ(x, t; θ) ≈ arg min ES|x FAPE2 (S, Ŝ)
(20)
Ŝ

and thus the reparameterized Cβ denoising model becomes

h
i
x̂1 (x, t; θ) ≈ arg min ES|x FAPE2 (S, Ŝ)
Ŝ

(21)

Cβ

Colloquially, this means that the denoised Cβ structure (towards which we interpolate at inference time) is the Cβ part of
the best all-atom prediction, rather than the best Cβ prediction. In the final inference step, rather than extracting x̂1 from Ŝ
and interpolating the rest of the way towards it, we simply return the all-atom structure Ŝ. However, the model is predicting
the denoised all-atom structure from the Cβ structure alone, and there is no iterative refinement of the non Cβ components.
Hence, our model is best thought of as a generative model over Cβ positions only, which additionally fills in the all-atom
information to minimize the FAPE loss conditioned on the input Cβ positions.
A.3. Comparison with Harmonic Diffusion
In harmonic diffusion, as in flow matching, a conditional probability path p(xt | x0 ) represents a noising process for the
data point x0 (t = 0 for the data by diffusion convention). Unlike flow matching, the path is given by the transition (or
perturbation) kernel of a (Markovian) diffusion process rather than interpolation with the noise. The stationary distribution of
the diffusion is the noisy prior by construction; however, the probability path converges to this prior only in the infinite-time
limit. Instead, the maximum time is chosen such that the KL-divergence between the pt|0 and the stationary distribution is
acceptably low. Unfortunately, in harmonic diffusion:
DKL (pt|0 ||p∞ ) =




3n 
X

e−λi t Ei −
− log 1 − e−λi t
i=1

(22)

where Ei is the (roughly constant) amount of energy in the ith mode (Equation 3 in Jing et al. (2023)). That is, the rate of
convergence not only depends on the number of dimensions, but—more problematically—the smallest eigenvalue λi of
the diffusion drift matrix, which becomes smaller for larger proteins. Hence, it becomes tricky to train a time-conditioned
denoising model for proteins of arbitrary size. In the case of AlphaF LOW and ESMF LOW trained on crops of 256, the model
would not be able to denoise longer proteins from an intermediate state at which the crops have converged to noise, but the
entire protein has not—such states have never been seen during training. Our flow matching framework instead imposes the
noisy prior as a boundary condition at the same t = 0 for all protein lengths and crops, avoiding this issue.
While the fixed convergence time is a desirable quality, our flow matching framework—at least as defined in Equations 2–
6—satisfies an even stronger property, which we call crop invariance (Proposition A.1). Colloquially, this means that the
marginal distribution of a crop of length M at time t is the same as if it were noised independently as an intact sequence of
length M . This property ensures the noisy distributions over isolated crops seen at training time are exactly the same as
those seen at inference time, when those crops are embedded in full-size proteins.
(M )

(N )

Proposition A.1. Let x1 ∈ RN and x1 [i:i+M] ∈ RM be a crop of x1 of length M ≤ N and define pt , pt to be the
(N )
conditional probability paths in dimensionalities N, M . Then for any t, x̃ ∈ RM , pt (x[i:i+M] = x̃ | x1 ) is equal to
(M )
pt (x = x̃ | x1 [i:i+M]).

Proof. Our key claim is that for time t = 0, i.e. in the noise distribution, the density q (N ) (x[i:i+M] = x̃) is equivalent to
q (M ) (x = x̃). The former amounts to marginalizing the density q (N ) (x) over the non-crop variables. For simplicity, we
proceed with i = 0; the more general case is very similar:
Z


q (N ) x[0,M ) = x̃ = q (N ) x[0,M ) = x̃, x[M,N ) dx[M,N )



Z
M
−2
N
−2
X
X
α
∝ exp − 
∥x̃j − x̃j+1 ∥2 + ∥x̃M −1 − xM ∥2 +
∥xj − xj+1 ∥2  dx[M,N )
2 j=0
j=M





Z
M
−2
N
−2
X
X
α
α
∥x̃j − x̃j+1 ∥2  exp − ∥x̃M −1 − xM ∥2 +
∥xj − xj+1 ∥2  dx[M,N )
= exp −
2 j=0
j=M
|
{z
}
constant

∝q

(M )

(x = x̃)

where the constant is an offset Gaussian integral. This equivalence means that—up to some global translation—sampling
noise of dimension N and then cropping to length M is equivalent to sampling noise of dimension M . Then, notice that
linear interpolation of full structures implies linear interpolations of crops:
x = (1 − t) · x0 + t · x1

=⇒

x[i:i+M] = (1 − t) · x0 [i:i+M] + t · x1 [i:i+M]

(N )

Thus, the sampling procedure for pt (x[i:i+M] = x̃ | x1 )—which is to interpolate N -dimensional noise and data and
(M )
then crop to M dimensions—is the same as the sampling procedure for pt (x = x̃ | x1 [i:i+M])—which is to first crop
the data and noise to M dimensions and then interpolate.
We note that crop invariance no longer holds in the final form of flow matching that we use in Algorithms 1 and 2 and
describe in Appendix A.2 due to the RMSD alignment step. Nevertheless, we posit that initial preservation of distributional
alignment helps with generalization to proteins of unseen large sizes at inference time.
The second advantage of our flow matching framework over harmonic diffusion is in the treatment of missing residues. In
harmonic diffusion, the perturbation kernel p(xt | x0 ) is a Gaussian whose mean is given by µ = e−tH/2 x0 , where H is
the drift matrix. This matrix exponential is far from diagonal, meaning that each entry of µ is dependent on all initial entries
of x0 . Hence, if there are missing coordinates in x0 , they must be imputed in order to sample p(xt | x0 ). In contrast, in our
flow matching framework, each coordinate in x at time t is a linear combination of only the same-index coordinates in x0
and x1 . Hence, we can simply omit the missing residues in the RMSD alignment and the subsequent interpolation.

B. Experimental Details
B.1. Training and Inference
Training We use OpenFold (Ahdritz et al., 2022) to train AlphaF LOW and ESMF LOW, as it closely follows the training
best practices described in AlphaFold (Jumper et al., 2021). However, because the OpenFold weights for AlphaFold were
trained with a much later cutoff date, we instead initialize with the original CASP14 weights from DeepMind (version 1).
For PDB training data, we use a January 2023 snapshot of the PDB and apply 40% clustering with MMSeqs2 (Steinegger &
Söding, 2017). We train with crops of size 256, batch size of 64, no recycling, and no templates. AlphaF LOW is trained on
the full set of auxiliary losses, except the structural violation loss and with the FAPE loss squared. ESMF LOW is trained
on the FAPE, pLDDT, distogram, and supervised χ losses. To maintain precision in the initial prediction, we set t = 0
and omit the noisy input in 20% of training examples. Training progress is monitored via the precision and diversity on a
validation set of 183 CAMEO targets deposited Aug–Oct 2022, following Jing et al. (2023). To fine-tune on MD ensembles,
we resume from the selected checkpoints from the PDB training. All the training settings remain unchanged, except the
targets are sampled uniformly at random (with a random conformation), the batch size is set to 8, and t = 0 is set 10% of
the time. Training progress is monitored via the loss on the validation split.
Training Cost All training is done on a machine with 8x NVIDIA A100 GPUs and 2x Intel Xeon(R) Gold 6258R
processors, with the total training cost shown in Table 2.

Table 2. AlphaF LOW and ESMF LOW training cost

Total
hours

Train
examples

Secs per
training pass

AlphaF LOW

PDB
PDB distillation
MD
MD distillation
MD+Templates
MD+Templates distillation

1.28M
160k
43k
38k
38k
51k

5.8
17.4
6.2
17.4
6.3
18.0

ESMF LOW

PDB
PDB distillation
MD
MD distillation
MD+Templates
MD+Templates distillation

720k
64k
27k
51k
51k
38k

4.2
11.9
4.6
12.0
4.7
12.5

Inference We run AlphaF LOW and ESMF LOW with 10 steps by default, evenly spaced from t = 0 to t = 1, where the
first prediction is performed with no noisy input. However, by merging the first K > 1 steps, we can reduce the variance of
the sampled distribution and increase precision, analogous to increasing MSA depth. This is because—after the initial large
step to t = 0.1K—we are effectively starting the flow from a modified intermediate marginal pt (x) which differs from the
pt (x) that would arise from properly following the flow:
x = (1 − t) · x0 + t · x1 ,

x0 ∼ q(x0 ), x1 ∼ pdata (x1 )

x = (1 − t) · x0 + t · Epdata [x1 ],

x0 ∼ q(x0 )

(original)

(23)

(modified)

(24)

i.e., by stepping directly to intermediate time t, we interpolate towards the initial x̂1 prediction, which is a single point
estimate of the unconditional expectation, rather than the full distribution pdata (x1 ). We omit recycling for all methods
following Del Alamo et al. (2022). Note that, by default, AlphaFold accepts a maximum MSA depth equivalent to
subsampling with depth 1024, and exhibits a small level of diversity; on the other hand, ESMFold is completely deterministic.
For AlphaF LOW PDB experiments, we resample the MSA (with depth 1024) for each new sample, but not for each inference
step. At inference time, MSAs for all sequences are computed with the ColabFold MMSeqs pipeline (Porter et al., 2023).
Self-conditioning Although we do not use recycling per se for either our methods or the baselines, we employ selfconditioning (Chen et al., 2022; Stärk et al., 2023) in the PDB experiments to increase the precision of AlphaF LOW. In
particular, at training time, 50% of supervised forward passes are provided the (gradient-detached) outputs from an initial
forward pass of the model; we reuse the recycling embedder of AlphaFold to embed these outputs. At inference time,
every forward pass after the first is provided the outputs of the previous forward pass. Note that unlike Stärk et al. (2023),
we self-condition with the full set of model output states, i.e., including pair embeddings, rather than just the output x̂1
prediction. Self-conditioning is omitted for distillation training and for MD training and inference. Finally, although we also
trained ESMF LOW with self-conditioning, we did not observe any improvements and report results without it.
Distillation Because the inference process is deterministic except for the initial noisy sample, it defines a map from the
noisy distribution to the data distribution. We can aim to learn this map via a model that ingests the noisy sample and
predicts the corresponding fully-denoised output in a single forward pass. To train such a model, for each training example
(still a crop of 256), we run the full inference pipeline with the original flow model and set the result as the training target.
All other training settings are kept the same and training performance is monitored the same way, except the batch size is
always set to 8, and the concepts of sampling t, interpolating, and self-conditioning no longer apply. For AlphaF LOW and
ESMF LOW on the PDB, we train for 160k and 64k training examples, respectively. For distilling the MD models, we start
from the weights of the original AlphaF LOW-MD and ESMF LOW-MD and fine tune for 38k and 51k training examples,
respectively.

B.2. Datasets
PDB Test Set To construct the test set of structurally heterogeneous recent proteins from the PDB, we follow Ellaway et al.
(2023) and identify chains as representing the same protein if they map to the same segment in the same UniProt reference
sequence. We use the SIFTS annotations database (Dana et al., 2019) and its residue-level mappings from PDB chains to
UniProt reference sequences to associate each deposited chain with a segment. Then, we cluster all segments with a Jaccard
similarity threshold of 0.75 and complete linkage, with each resulting cluster regarded as a distinct protein, yielding 75k
proteins. We collect all proteins which (1) are represented by 2–30 chains deposited after the AlphaFold training cutoff and
no chains before the cutoff, (2) have lengths between 256–768 residues, (3) have at least two structural clusters when the
chains are clustered with a threshold of 0.85 symmetrized lDDT-Cα and complete linkage. From the resulting 563 proteins
(represented by 2843 chains), we subsample 100 proteins (represented by 500 chains) to form the test set. At inference
time, we run all models using the sequence given by the UniProt segment. The distribution of sequences lengths is shown in
Figure 6.
MD Dataset The ATLAS dataset (Vander Meersche et al., 2023) consists of all-atom, explicit solvent MD simulations for
1390 non-membrane proteins, chosen as representatives for all eligible ECOD structural classes (Schaeffer et al., 2017). For
each protein, 3 replicate simulations of length 100 ns are provided, each with 10k frames. To train and validate on these
trajectories, we first generate MSAs for all 1390 ATLAS entries using the provided sequence and the ColabFold MMSeqs2
pipeline (Porter et al., 2023). Then, for the train and validation sets, we extract 300 conformations to be randomly sampled
in the training pipeline. The test split consists of all 84 targets whose corresponding PDB entries were deposited after May
1, 2019, minus the two targets with sequence length greater than 1024. The resulting distribution of sequences lengths is
shown in Figure 6.

PDB (n = 100)

PDB (n = 82)

Figure 6. Histogram of sequence lengths in the PDB test set (left) and the ATLAS test set (right).

B.3. Evaluation Procedures
Symmetrized lDDT In the PDB experiments, we often need to compute the similarity (or dissimilarity) between two
structures which may not share identical sequences, and which may differ significantly in length—for example, between two
PDB chains or between a PDB chain and a structure predicted from the UniProt reference sequence. To do so, we define the
symmetrized lDDT as a variant of lDDT-Cα which is (as the name suggests) symmetric and robust to these discrepancies.
We perform a pairwise alignment of the two sequences, and tabulate the Cα pairs (identified by residue index only) which
are within 15 Å of each other in either structure. Then, we score the fraction of these selected pairwise distances that are
consistent within 0.5 Å, 1 Å, 2 Å, and 4 Å in the two structures. The symmetrized lDDT-Cα is the mean of these four scores.
MD Evaluations To compare a generated ensemble with the ground-truth MD ensemble, we first align both ensembles to
the static all-atom structure that initialized the simulation (provided in the ATLAS download). We then perform all analyses
using the Euclidean atomic coordinates in MDTraj (McGibbon et al., 2015). For most procedures, we subsample 1000
random MD frames to reduce the analysis runtime. To compute the RMWD, the Wasserstein distance between two 3D

Gaussians is given by


W22 (N (µ1 , Σ1 ), N (µ2 , Σ2 )) = ∥µ1 − µ2 ∥2 + Tr Σ1 + Σ2 − 2(Σ1 Σ2 )1/2

(25)

which reduces to Euclidean distance in the case of point masses. This squared distance decomposes into a translation term
and a variance term; so the aggregate RMWD (Equation 8) also decomposes as
RMWD2 (X1 , X2 ) =

N
N

1 X
1 X 
∥µ1,i − µ2,i ∥2 +
Tr Σ1,i + Σ2,i − 2(Σ1,i Σ2,i )1/2
N i=1
N i=1
|
{z
} |
{z
}
(translation contribution)2

(26)

(variance contribution)2

We report the translation contribution (which resembles RMSD) and variance contribution in Table 1. In the calculation
of joint W2 distance, we first project to the PCA subspace because thermal fluctuations dominate in the full dimensional
space and make the W2 metric unsuitable without an extremely large number of samples. While it is common to perform
PCA using the MD reference ensemble alone, we note that doing so can obscure deviations of the predicted ensemble along
the orthogonal degrees of freedom. Thus, we repeat the analysis using with the MD ensemble and the equally-weighted
pooling of the MD and predicted ensembles. Finally, in the residue exposure analysis, we compute the solvent-accessible
surface area (SASA) of each sidechain using the Shrake-Rupley algorithm and a probe radius of 2.8 Å. Following Porter
et al. (2019), we use a SASA threshold of 2.0 Å2 to distinguish buried and exposed residues.
Comparison with Replicate MD To compare the performance of our method with replicate MD simulations, we leverage
the fact that ATLAS trajectories are provided in three replicates (100 ns and 10k frames each). In the main experiments,
these three replicates are pooled to collectively represent the MD ensemble; however, such pooling would not be appropriate
if one of these replicates is taken for comparison. Instead, we select the first replicate for comparison and pool the latter two
to represent the ground truth MD ensemble. We emulate different computational budgets by truncating the first trajectory to
its first 4096, 2048, 1024, 512, 256, 128, 64, 32, and 16 frames before analysis, respectively representing simulation lengths
of 40.96 ns, 20.48 ns, 10.24 ns, 5.12 ns, 2.56 ns, 1.28 ns, 640 ps, 320 ps, and 160 ps. When necessary, we subsample or
replicate by the appropriate power of 2 to ensure all analyses operate on 256 frames (important for finite-sample Wasserstein
distances). The computational cost in GPU-hrs is estimated by running 1 minute of MD for each protein on a single NVIDIA
A100 GPU and noting the average performance in hrs/ns. (The average GPU utilization is 62%, indicating efficient usage of
resources.) For the AlphaF LOW and ESMF LOW ensembles, we first generate 250 samples as usual and also subsample 128,
64, 32, 16, 8, and 4 samples for analyses, duplicating by the appropriate power 2 to reach 256 (≈ 250) samples. The runtime
is provided as an average over all test proteins on a single NVIDIA A100 GPU.
Comparison with Normal Mode Analysis We also compare the performance of our method with normal mode analysis
of the PDB protein structures using ProDy (Bakan et al., 2011). We construct Gaussian Network Models (GNM) (Bahar
et al., 1997) and Anisotropic Network Models (ANM) (Atilgan et al., 2001) using the Cα coordinates and draw 250 samples
from each model, keeping all nondegenerate eigenvectors. We use Γ = 0.15 (adjusted from default to match the average
MD RMSF) and default 10 Å and 15 Å cutoffs for GNM and ANM, respectively.

C. Additional Results
C.1. PDB Ensembles
Table 3 provides precision, recall, and diversity results for the experiments on PDB ensembles, with a median taken over the
100 test set targets. For ESMFold and ESMF LOW, the second set of results corresponds to the subset of targets released after
the training cutoff of May 1, 2020 (n = 56). Runtime measurements (per sample) are performed on a single A100 GPU and
reported as a median over 100 targets. Figure 7 shows PCA of the true and generated ensembles for several selected targets
to illustrate the degradation of the MSA subsampling ensembles. Figure 8 highlights conformational changes observed in
the PDB ensembles and correctly sampled by AlphaF LOW. In both figures, the PCA is performed by first aligning all PDB
sequences with the UniProt reference with ClustalW (Larkin et al., 2007) and taking the Cα positions of the common subset
of aligned residues. The structures are then RMSD aligned to a randomly selected PDB structure and the PCA is performed
on the resulting Euclidean coordinates. Sample weights are chosen so that the PDB structures account for half the loading,
regardless of their number. Coordinates are converted to Å RMSD units.
Table 3. Evaluation on PDB ensembles.

Precison

Recall

Diversity

Runtime

AlphaF LOW

Full
5 steps
2 steps
Distilled

0.810
0.821
0.839
0.831

0.801
0.801
0.811
0.810

0.185
0.151
0.082
0.128

69.6
42.1
21.3
7.4

MSA
subsampling

0.849
0.844
0.835
0.795
0.757

0.823
0.818
0.806
0.784
0.760

0.026
0.044
0.053
0.088
0.125

5.5
4.2
3.9
3.6
3.5

0.850

0.823

0.026

7.7

0.777 / 0.777
0.787 / 0.788
0.795 / 0.797
0.775 / 0.774

0.777 / 0.765
0.772 / 0.767
0.774 / 0.760
0.752 / 0.745

0.210 / 0.213
0.166 / 0.174
0.100 / 0.102
0.152 / 0.152

30.4
18.3
9.2
3.1

0.806 / 0.809

0.764 / 0.761

0.000

3.2

AlphaFold
Full
5 steps
2 steps
Distilled

ESMF LOW

ESMFold

G1SVB0
2.5

1.0

0.5
0.0
0.5

P46957

1.5

O34693

2.0

1.0

P0A1J1

Figure 7. PCA of PDB and predicted ensembles from AlphaF LOW (blue) and MSA subsampling (depth 64) (orange), with PDB
structures marked by ▲. The MSA subsampling ensembles have similar diversity as the AlphaF LOW ensembles but drift away from the
true structures.

F0NH89 CRISPR-associated ring nuclease from Sulfolobus islandicus

1 7pq2_AAA

2 7pq3_AAA

3 7pqa_AAA

4 7pq6_AAA

F2NWD3 Card1 nuclease from Treponema succinifaciens
1 6wxw_A

2 6wxx_A

3 6xl1_A

4 6wxy_B

P73953 sodium-dependent bicarbonate transporter SbtA

1 7cye_A

2 7cyf_A

3 7egl_A

4 7egk_A

2.0

1.5
1.0
0.5

0.0
0.5

Figure 8. PDB conformational changes correctly sampled by AlphaF LOW. For each UniProt ID, the PCA plot shows the complete set of
PDB structures (▲) and AlphaF LOW samples (blue). Four random PDB structures (left) and four random AlphaF LOW samples (right) are
visualized, where the numbers label the positions of the selected structures.

C.2. MD Ensembles
Table 4 provides the evaluation of ESMF LOW on MD ensembles. In Table 5, we report the performance of AlphaF LOW-MD
with ablated training procedures, and the comparison of AlphaF LOW with normal mode analysis conducted on the PDB
structure. In Figures 9–12, we provide additional visualizations for the RMSF, transient contacts, weak contacts, and solvent
exposure analyses of AlphaF LOW-MD ensembles. Finally, In Figure 13, we provide additional convergence results for
AlphaF LOW-MD+Templates vs replicate MD simulations.

Table 4. Evaluation of ESMF LOW on MD ensembles
ESMF LOW-MD
EFMD+Templates
Full

Distilled

ESMFold

Full

Distilled

Predicting
flexibility

Pairwise RMSD (=2.90)
Pairwise RMSD r ↑
All-atom RMSF (=1.70)
Global RMSF r ↑
Per-target RMSF r ↑

3.25
0.19
2.16
0.31
0.76

2.76
0.19
2.12
0.33
0.74

0.00
—
0.00
—
—

2.00
0.85
1.07
0.84
0.90

1.42
0.80
0.80
0.79
0.87

Distributional
accuracy

Root mean W2 -dist. ↓
,→ Translation contrib. ↓
,→ Variance contrib. ↓
MD PCA W2 -dist. ↓
Joint PCA W2 -dist. ↓
% PC-sim > 0.5 ↑

3.60
3.13
1.74
1.51
3.19

4.23
3.75
1.90
1.87
3.79

4.60
3.65
2.50
1.69
3.87
—

2.17
1.66
1.07
1.44
1.70

2.27
1.70
1.35
1.48
1.81

Ensemble
observables

Weak contacts J ↑
Transient contacts J ↑
Exposed residue J ↑
Exposure MI matrix ρ ↑

0.55
0.34
0.49
0.20

0.48
0.30
0.43
0.16

0.22
0.15
0.28
—

0.59
0.47
0.50
0.22

0.48
0.41
0.44
0.16

Table 5. Ablations and normal mode analysis on MD ensembles. The ablations verify the importance of the two-step training procedure
for AlphaF LOW+MD. Normal mode analysis (NMA) often fails to outperform baseline AlphaF LOW+MD despite having access to the
ground truth PDB structure, and significantly underperforms AlphaF LOW+MD+Templates when it is provided the same PDB template
structure. ⋆ Note that NMA results for RMSF and RMWD are Cα-only rather than all-atom, which likely overestimates the performance.
GNM: Gaussian Network Model; ANM: Anisotropic Network Model.
Ablations

NMA

Baseline

No ATLAS
finetuning

No PDB
pretraining

AFMD
+Templates

GNM

ANM

Predicting
flexibility

Pairwise RMSD (=2.90)
Pairwise RMSD r ↑
All-atom RMSF (=1.70)
Global RMSF r ↑
Per-target RMSF r ↑

2.89
0.48
1.68
0.60
0.85

2.41
0.34
1.25
0.48
0.82

3.04
0.29
1.81
0.45
0.83

2.18
0.94
1.31
0.91
0.90

1.85
0.71
1.22⋆
0.64⋆
0.72⋆

2.36
0.65
1.35⋆
0.55⋆
0.76⋆

Distributional
accuracy

Root mean W2 -dist. ↓
,→ Translation contrib. ↓
,→ Variance contrib. ↓
MD PCA W2 -dist. ↓
Joint PCA W2 -dist. ↓
% PC-sim > 0.5 ↑

2.61
2.28
1.30
1.52
2.25

2.96
2.52
1.36
1.64
2.60

3.11
2.71
1.44
1.59
2.67

1.95
1.64
1.01
1.25
1.58

2.47⋆
2.07⋆
1.33⋆
1.84
2.44

2.54⋆
2.09⋆
1.27⋆
1.73
2.35

Ensemble
observables

Weak contacts J ↑
Transient contacts J ↑
Exposed residue J ↑
Exposure MI matrix ρ ↑

0.62
0.41
0.50
0.25

0.48
0.36
0.40
0.18

0.60
0.39
0.50
0.25

0.62
0.47
0.50
0.25

0.45
0.25
—
—

0.40
0.25
—
—

MD

7ead_A
AlphaFlow
r = 0.86

MSA subsampling
r = 0.24

MD

MD

6pnv_A
AlphaFlow
r = 0.65

MSA subsampling
r = 0.45

MD

6jpt_A

AlphaFlow
r = 0.99

6l3r_E

AlphaFlow
r = 0.95

MSA subsampling
r = 0.84

MSA subsampling
r = 0.21

5.0
2.5
0.0

Figure 9. Visualization of ensembles and their RMSF plots. For each PDB ID, 10 samples from the MD, AlphaF LOW, and MSA
subsampling (depth 48) ensembles are shown, with RMSF by residue index in insets. For the latter two, the Pearson correlation coefficient
(r) with the MD RMSF is reported.

MD

MD

MD

MD

6d7y_A Toxic C-Terminal Tip of CdiA from Pseudomonas aeruginosa
AlphaFlow

Crystal

MD
27%

6in7_A Sigma factor AlgU negative regulatory protein
AlphaFlow

Crystal

MD
13%

6q9c_A NADH-quinone oxidoreductase subunit E
AlphaFlow

Crystal

MD
19%

6y2x_A E3 ubiquitin-protein ligase DTX2

AlphaFlow

Crystal

MD
21%

AlphaFlow
16%

AlphaFlow
49%

AlphaFlow
12%

AlphaFlow
44%

Figure 10. Visualization of transient contacts. For each PDB ID, the contact maps from MD simulation and AlphaF LOW are shown,
with normal contacts in gray, weak contacts in blue, and transient contacts in red. Among the the transient contacts correctly identified
by AlphaF LOW, one is selected for visualization: the two residues are highlighted in the crystal structure (left), a frame from the MD
simulation (middle) where they are in contact, and an AlphaF LOW sample where they are in contact. The probability of occurence in each
ensemble is shown.

6sms_A Vegetative Insecticidal Protein 1Ac from Bacillus Thuringiensis

MD

AlphaFlow

MD

AlphaFlow

MD

MD

Crystal

MD
89%

6xb3_H AcNPV poxvirus immune nuclease
Crystal

MD
92%

AlphaFlow
85%

AlphaFlow
75%

7ead_A beta-sheet cytochrome c prime from Thermus thermophilus
AlphaFlow

Crystal

MD
77%

6d7y_B immune protein from Enterobacter cloacae
AlphaFlow

Crystal

MD
59%

AlphaFlow
94%

AlphaFlow
65%

Figure 11. Visualization of weak contacts. For each PDB ID, the contact maps from MD simulation and AlphaF LOW are shown, with
normal contacts in gray, weak contacts in blue, and transient contacts in red. Among the the weak contacts correctly identified by
AlphaF LOW, one is selected for visualization: the two residues are highlighted in the crystal structure (left), a frame from the MD
simulation (middle) where they are not in contact, and an AlphaF LOW sample where they are not in contact. The probability of occurence
in each ensemble is shown.

6nl2_A NIS Synthetase DesD from Streptomyces coelicolor
19%

MD

81%

56%

AlphaFlow

44%

6uof_A transcriptional regulator from Streptococcus pneumoniae
69%

MD

38%

MD

31%

9%

AlphaFlow

91%

6xrx_A mosquito protein AEG12
62%

32%

AlphaFlow

68%

7aqx_A surface glycoprotein from Trypanosoma brucei
11%

MD

89%

62%

AlphaFlow

38%

Figure 12. Visualization of cryptic exposed residues. For each PDB ID, in the left pair of structures, the set of true cryptic exposed
residues (from MD) is colored red; in the right pair the set identified from AlphaF LOW ensembles is colored blue. A common identified
residue is selected and highlighted in green. For each pair, the left structures shows the residues buried in the crystal structure whereas the
right structure shows a frame (or sample) where the highlighted residue is exposed to the solvent. The probability of occurence in each
ensemble is shown.

Pairwise RMSD r

Pairwise RMSD
2.5

All-atom RMSF

0.90

1.5

0.85

1.0

2.0
1.5
1.0
0.9

0.01

0.1

Global RMSF r

0.90

0.8
0.7
0.01
2.2

0.1

RMWD (translation)

0.1

Per target RMSF r

2.50

0.80

2.25
0.1

RMWD (variance)

0.1

2-dist

2.2

0.01

0.1

PC sim > 0.5 %

1.8
0.01

0.1

Transient contacts J

0.01

0.1

0.01

0.1

0.01

0.1

2-dist

Weak contacts J

0.7
0.6
0.5
0.01

0.1

Exposed residue J

Exposed MI matrix

0.4

0.7

0.5

0.1

MD PCA

2.0

0.01

1.4

1.00

Joint PCA

1.6

1.25
0.01

RMWD

1.8

1.50

1.8

0.1

2.00
0.01

1.75

0.01
2.75

0.85

2.0

1.6

0.01

0.6
0.4

0.2

0.5
0.01

0.1

0.01

0.1

Figure 13. Efficiency of AlphaF LOW vs replicate MD simulations. AlphaF LOW (with templates) with varying number of samples in
orange; AlphaF LOW distilled into a single forward pass in green; MD with varying trajectory lengths in blue. For Pairwise RMSD and
RMSF, the values from the reference MD (i.e., pooling the remaining two replicates) are shown as horizontal dashed lines. The x-axis
reports runtime in GPU-hrs averaged over targets. For MD, the average runtime is 6.3 mins / ns; for AlphaF LOW, the average runtime per
sample is 38 s without distillation and 3.8 s with distillation. See Appendix B.3 for further benchmarking details.


---

# Predicting equilibrium distributions for molecular systems with deep learning

**Authors:** Shuxin Zheng, Jiyan He, Chang Liu, Yu Shi, Ziheng Lu, Weitao Feng, Fusong Ju, et al.
**Year:** 2024
**Venue:** Nature Machine Intelligence
**DOI:** 10.1038/s42256-024-00837-3
**Source PDF URL:** https://arxiv.org/pdf/2306.05445 (arXiv preprint, posted as "Towards Predicting Equilibrium Distributions for Molecular Systems with Deep Learning"; Nature Machine Intelligence version is hybrid OA with no free PDF location found via OpenAlex)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

arXiv:2306.05445v1 [physics.chem-ph] 8 Jun 2023

Towards Predicting Equilibrium Distributions
for Molecular Systems with Deep Learning
Shuxin Zheng1*† , Jiyan He1† , Chang Liu1*† , Yu Shi1† , Ziheng
Lu1† , Weitao Feng1 , Fusong Ju1 , Jiaxi Wang1 , Jianwei
Zhu1 , Yaosen Min1 , He Zhang1 , Shidi Tang1 , Hongxia
Hao1 , Peiran Jin1 , Chi Chen2 , Frank Noé1 , Haiguang Liu1*†
and Tie-Yan Liu1*
1 Microsoft Research AI4Science.
2 Microsoft Quantum.

https://DistributionalGraphormer.github.io.
*Corresponding author(s). E-mail(s): {shuxin.zheng, chang.liu,
haiguang.liu, tie-yan.liu}@microsoft.com;
† These authors contributed equally to this work.
Abstract
Advances in deep learning have greatly improved structure prediction of molecules. However, many macroscopic observations that are
important for real-world applications are not functions of a single molecular structure, but rather determined from the equilibrium distribution
of structures. Traditional methods for obtaining these distributions,
such as molecular dynamics simulation, are computationally expensive and often intractable. In this paper, we introduce a novel deep
learning framework, called Distributional Graphormer (DiG), in an
attempt to predict the equilibrium distribution of molecular systems.
Inspired by the annealing process in thermodynamics, DiG employs
deep neural networks to transform a simple distribution towards the
equilibrium distribution, conditioned on a descriptor of a molecular system, such as a chemical graph or a protein sequence. This
framework enables efficient generation of diverse conformations and
provides estimations of state densities. We demonstrate the performance of DiG on several molecular tasks, including protein conformation sampling, ligand structure sampling, catalyst-adsorbate sampling,
and property-guided structure generation. DiG presents a significant

advancement in methodology for statistically understanding molecular
systems, opening up new research opportunities in molecular science.
Keywords: Equilibrium Distribution, Statistical Mechanics, Deep Learning,
Molecular States

1 Main

Fig. 1: Predicting conformational distributions with the Distributional Graphormer (DiG) framework. (a) DiG takes the basic descriptor
D of a target molecular system as input, e.g., amino acid sequence, to generate
a probability distribution of structures which aims at approximating the equilibrium distribution and sampling different metastable states or intermediate
states. In contrast, static structure prediction methods, such as AlphaFold [1],
aim at predicting one single high-probability structure of a molecule. (b) The
DiG framework for predicting distributions of molecular structures. A deeplearning model (Graphormer [2]) is used as modules to predict a diffusion
process (→) that gradually transforms a simple distribution towards the target distribution. The model is learned so that the derived distribution pi in
each intermediate diffusion time step i matches the corresponding distribution
qi in a predefined diffusion process (←) that is set to transform the equilibrium distribution to the simple distribution. Supervision can be obtained from
both samples (lower row), and a molecular energy function (upper row).

Deep learning methods are now state of the art to predict structures
of molecular systems with high efficiency. For example, AlphaFold achieves
atomic-level accuracy in protein structure predictions [1], and has enabled new
applications in structural biology [3–5]; fast docking methods based on deep
neural networks have been developed and applied to predict ligand binding
structures [6, 7], supporting virtual screening in drug discovery [8, 9]; deep
learning models predict the relaxed structures of adsorbates on catalyst surfaces [2, 10–12]. All these developments demonstrate the potential of deep
learning approaches in modeling molecular structures and states.

However, accurate prediction of the most probable structure only reveals a
small portion of the information needed to understand a molecular system in
equilibrium. In reality, molecules can be highly flexible and the equilibrium distribution is crucial for studying statistical mechanical properties. For example,
functions of some biomolecules can be inferred from the probabilities associated with structures to identify metastable states; also based on probabilistic
densities in the structure space, thermodynamic properties, such as entropy
and free energies, can be computed by applying statistical mechanics methods.
Fig. 1a illustrates the difference between conventional structure prediction
and the prediction of distributions of molecular structures. Although adenylate kinase has two distinct experimentally known conformations (open and
closed states), a predicted structure usually corresponds to a highly probable metastable state or a low-probability intermediate state (as shown in this
figure). A method is desired to allow us to sample the equilibrium distribution of adenylate kinase structures containing both functional states and their
relative probabilities.
In contrast to the prediction of single structures, the prediction of equilibrium distributions still relies on classical and computationally expensive
simulation methods while the development of deep learning methods for this
task is still in its infancy. Most commonly, equilibrium distributions are sampled with molecule dynamics simulations which are computationally costly or
even intractable [13]. Enhanced sampling simulations [14, 15] and Markov state
modeling [16] can speed up rare event sampling, but rely on system-specific
choices such as collective variables along which the sampling is enhanced, and
is thus not an easily generalizable approach. A popular approach is coarsegrained molecular dynamics [17, 18] for which deep learning approaches have
recently been developed [19, 20] that have shown promising results for individual molecular systems but not yet demonstrated generalization. Boltzmann
Generators [21] are a deep learning approach to generate equilibrium distributions by constructing a probability flow from an easy-to-sample reference
state, but due to the flow architecture [22] this approach is also difficult to generalize to different molecules. Generalization has been demonstrated for flows
generating long timesteps for small peptides, but these methods have not yet
scaled to large proteins [23].
In this work, we develop the Distributional Graphormer (DiG), a new
deep learning approach aiming to approximately predict the equilibrium distribution and efficiently sample diverse and chemically plausible structures of
molecular systems. We show that DiG can generalize across molecular systems
and propose diverse structures for molecules not used during training that
resemble experimentally known structures. DiG draws inspiration from simulated annealing [24–27], which produces a complex distribution by gradually
refining a simple uniform distribution through the simulation of an annealing
process. Following this idea, DiG reduces the difficulty in the equilibrium distribution prediction problem by simulating a diffusion process that gradually

transforms a simple distribution to the target distribution that aims at approximating the equilibrium distribution of the given molecular system [28, 29]
(Fig. 1b, →). The diffusion process is realized by a deep-learning model that
is based upon the Graphormer architecture (Fig. 1b, [2]), and that is conditioned on a descriptor of the target molecule, such as a chemical graph or
an amino acid sequence. DiG can be trained using structure data from MD
simulations and experiments. For cases where such data are not sufficient, we
develop a novel Physics-Informed Diffusion Pre-training (PIDP) method to
train DiG directly under the supervision from energy functions (force fields)
of the systems. In both modes, the model receives a training signal in each diffusion step independently (Fig. 1b, ←), enabling efficient training that avoids
backpropagating through the entire diffusion process.
The performance of DiG is evaluated on three prediction tasks: protein
conformation distribution, ligand conformation distribution, and molecular
adsorption distribution on catalyst surfaces. We demonstrate that DiG is capable of generating realistic and diverse molecular structures in these tasks.
For the proteins shown in this paper, DiG efficiently generated structures
to resemble major functional states, but with orders of magnitude less time
than required for MD simulation. We also demonstrate that DiG can facilitate
inverse design of molecular structures by applying biased distributions that
favor structures with desired properties. This capability has the potential to
broaden the scope of molecular design for properties that lack adequate data to
guide the design process. These results indicate that DiG significantly advances
deep learning methodology for molecules from predicting a single structure
towards predicting probability distributions of molecular structures, paving
the way for efficient prediction of thermodynamic properties of molecules.

2 The Framework of Distributional Graphormer
Deep neural networks have been demonstrated to predict accurate molecular
structures from descriptors D for many molecular systems [1, 2, 6, 7, 10–12].
Here, DiG aims to take one step further to predict not only the most probable
structure, but also diverse structures with probabilities under the equilibrium distribution. To tackle this challenge, inspired by the heating-annealing
paradigm, we break down the difficulty of this problem into a series of simpler
problems. The heating-annealing paradigm can be viewed as a pair of reciprocal stochastic processes on the structure space that simulate the transformation
between the equilibrium distribution and a system-independent simple distribution psimple . Following this idea, we employ an explicit diffusion process
(forward process; Fig. 1b orange arrows) that gradually transforms the target
distribution of the molecule qD,0 , as the initial distribution, towards psimple
through a time period τ . The corresponding reverse diffusion process then
transforms psimple back to the target distribution qD,0 . This is the generation
process of DiG (Fig. 1b, blue arrows). The reverse process is performed by
updates predicted by deep neural networks from the given D, which are trained

to match the forward process. Compared to directly predicting the equilibrium
distribution from D, the heating-annealing paradigm significantly reduces the
difficulty of this problem. As psimple is chosen to enable independent sampling
and have a closed-form density function, DiG enables independent sampling
of the equilibrium distribution by simulating the reverse process started from
psimple , and also provides a density function for the distribution by tracking
the process.
Specifically, we choose psimple := N (0, I) as the standard Gaussian distribution in the state space, and the forward diffusion process as the Langevin
diffusion process targeting this psimple (Ornstein–Uhlenbeck process) [30–32].
A time dilation scheme βt [33] is introduced for approximate convergence to
psimple after a finite time τ . The result is written as the following stochastic
differential equation (SDE):
dRt = −

p
βt
Rt dt + βt dBt ,

(1)

where Bt is the standard Brownian motion (a.k.a Wiener process). Choosing
this forward process leads to a psimple that is more concentrated than a heated
distribution hence it is easier to draw high-density samples, and the form of
the process enables efficient training and sampling.
Following stochastic process theory (e.g., [34]), the reverse process is also
a stochastic process, written as the following SDE:
dRt̄ =

p
βt̄
Rt̄ dt̄ + βt̄ ∇ log qD,t̄ (Rt̄ ) dt̄ + βt̄ dBt̄ ,

(2)

where t̄ := τ − t is the reversed time, qD,t̄ := qD,t=τ −t̄ is the forward-process
distribution at the corresponding time, and Bt̄ is the Brownian motion in
reversed time. To recover qD,0 from psimple by simulating this reverse process,
deep neural networks are employed to construct a score model sθD,t (R), which
is trained to predict the true score function ∇ log qD,t (R) of each instantaneous
distribution qD,t from the forward process. This formulation is called diffusionbased generative model and has been demonstrated to be able to generate
high-quality samples of images and other content [28, 29, 35–37]. As our score
model is defined in molecular conformational space, we employ our previously
developed Graphormer model [2] as the neural network architecture backbone
of DiG, to leverage its capabilities in modeling molecular structures and to
generalize to a range of molecular systems.
With the sθD,t (R) model, drawing a sample R0 from the equilibrium distribution of a system D can be done by simulating the reverse process Eq. (2) on
N + 1 steps that uniformly discretizes [0, τ ] with step size h = τ /N (Fig. 1b,

blue arrows):
RN ∼ psimple ,


Ri + βi sθD,i (Ri ) + N (0, βi I), i = N, · · · , 1,
Ri−1 = √
1 − βi

(3)

where the discrete step index i corresponds to time t = ih, and βi := hβt=ih .
Note that the reverse process does not need to be ergodic. The way that DiG
models the equilibrium distribution is using the instantaneous distribution at
the instant t = 0 (or t̄ = τ ) on the reverse process, but not using a time
average. As RN samples can be drawn independently, DiG can generate statistically independent R0 samples for the equilibrium distribution. In contrast
to Molecular Dynamics (MD) or Markov Chain Monte Carlo (MCMC) simulations, generation of DiG samples does not suffer from rare events, and can
thus be far more computationally efficient.

Physics-Informed Diffusion Pre-training
DiG can be trained by conformation data sampled over a range of molecular
systems. However, collecting sufficient experimental or simulation data to characterize the equilibrium distribution for various systems is extremely costly. To
address this data scarcity problem, we propose a novel pre-training algorithm,
called Physics-Informed Diffusion Pre-training (PIDP), which effectively optimizes DiG on an initial set of candidate structures that need not to be sampled
from the equilibrium distribution. The supervision comes from the energy
function ED of each system D, which defines the equilibrium distribution
qD,0 (R) ∝ exp(− EkDB(R)
T ) at the target temperature T .
The key idea is that the true score function ∇ log qD,t from the forward process Eq. (1) obeys a partial differential equation, known as the Fokker-Planck
equation (e.g., [38]). We then pre-train the score model sθD,t by minimizing the
following loss function that enforces the equation to hold:
N
M
X
1 X
i=1

M

m=1


βi 
(m)
(m) 
(m) 2
(m) 
∇ RD,i · sθD,i (RD,i ) + ∇ sθD,i (RD,i ) + ∇ ∇ · sθD,i (RD,i )
M

−

∂ θ
λ X
(m) 2
sD,i (RD,i ) + 1
∂t
M

m=1

(m)
(m) 2
∇ED (RD,1 ) + sθD,1 (RD,1 ) .
kB T

(4)

Here, the second term, weighted by λ1 , matches the score model at the final
generation step to the score from the energy function, and the first term implicitly propagates the energy-function supervision to intermediate time steps
(m)
(Fig. 1b, upper row). The structures {RD,i }M
m=1 to evaluate the loss are points
on a grid spanning the structure space. What is favorable is that, these structures do not have to obey the equilibrium distribution (as is required by data
structures), since they are only used to discretize functions in the structure
space, therefore the cost of preparing these structures can be much lower. As
structure spaces of molecular systems are often very high-dimensional (e.g.,

thousands for proteins), a regular grid would have intractably many points.
Fortunately, the space of actual interest is only a low-dimensional manifold of
physically reasonable structures (structures with low energy) relevant to the
problem. This allows us to effectively train the model only on these relevant
structures as R0 samples, and pass them through the forward process for Ri
samples. See Supplementary Sec. C.1 for an example on acquiring relevant
structures for protein systems.
We also leverage stochastic estimators including Hutchinson’s estimator [39, 40] to reduce the complexity in calculating derivatives of high-order
and for high-dimensional vector-valued functions. Note that for each step i, the
corresponding model sθD,i receives a training loss independent of other steps
and can be directly back-propagated. This step-by-step supervision pattern
helps to achieve efficient pre-training.

Training DiG with Data
In addition to using the energy function for information on the probability
distribution of the molecular system, DiG can also be trained with molecular structure samples which can be obtained from experimental structure
determination methods, molecular dynamics, or other simulation methods.
See Supplementary Sec. C for data collection details. Even when the simulation data is limited, they still provide information about the regions
the distribution needs to cover and the local shape of the distribution,
hence are helpful to improve a pre-trained DiG. To train DiG on data,
the score model sθD,i (Ri ) is matched to the corresponding score function
∇ log qD,i demonstrated by data samples. This can be done by minimizing
EqD,i (Ri ) sθD,i (Ri ) − ∇ log qD,i (Ri ) for each diffusion time step i. Although
the precise calculation of ∇ log qD,i is impractical, the loss function can be
equivalently reformulated into denoising score-matching form [41, 42]:
N

1 X
Eq (R ) Ep(ϵi ) σi sθD,i (αi R0 + σi ϵi ) + ϵi ,
N i=1 D,0 0

(5)

p
Qi p
where αi := j=1 1 − βj , σi := 1 − αi2 , and p(ϵi ) is the standard Gaussian
distribution. The expectation under qD,0 can be estimated using the simulation
dataset. Note that this function allows direct loss estimation and backpropagation for each i in constant (w.r.t i) cost, recovering the efficient step-by-step
supervision again (Fig. 1b, lower row).

Density Estimation by DiG
Many thermodynamic properties of a molecular system (e.g., free energy,
entropy) also require calculating the density function of the equilibrium distribution, which is another aspect of the distribution besides a sampling method.
DiG allows for this by tracking the distribution change along the diffusion

process [35]:


log pθD,0 (R0 ) = log psimple RθD,τ (R0 )
Z τ
Z

βt
D τ
−
βt dt,
∇ · sθD,t RθD,t (R0 ) dt −

(6)

where D is the dimension of the state space, and RθD,t (R0 ) is the solution to
the ordinary differential equation (ODE):
dRt = −


βt 
Rt + sθD,t (Rt ) dt,

(7)

with initial condition R0 , which can be solved using standard black box ODE
solvers or more efficient specific solvers (Supplementary Sec. A.6).

Property-Guided Structure Generation with DiG
There is a growing demand for inverse design of materials and molecules. The
goal is to find structures with desired properties, such as intrinsic electronic
band gaps, elastic modulus, and ionic conductivity, without going through a
forward searching process. DiG provides a feature to enable such propertyguided structure generation, by directly predicting the conditional structural
distribution given a value c of a microscopic property.
To achieve this, regarding the data-generating process in Eq. (2), we only
need to adapt the score function, from ∇ log qD,t (R) to ∇R log qD,t (R | c).
Using Bayes’ rule, the latter can be reformulated as ∇R log qD,t (R | c) =
∇ log qD,t (R) + ∇R log qD (c | R), where the first term can be approximated
by the learned (unconditioned) score model, i.e. the new score model is:
sθD,i (Ri | c) = sθD,i (Ri ) + ∇Ri log qD (c | Ri ).

(8)

Hence, only a qD (c | R) model is additionally needed [35, 36], which is a
property predictor or classifier that is much easier to train than a generative
model.
It is noted that in a normal workflow for machine-learning (ML) inverse
design, a dataset must be generated to meet the conditional distribution, then
an ML model will be trained on this dataset for structure predictions. The
ability to generate structures for conditional distribution without requiring a
conditional dataset places DiG in an advantageous position when compared to
the normal workflow in terms of efficiency and computational cost.

Interpolation between States
Given two states, DiG can approximate a reaction path that corresponds to
reaction coordinates or collective variables, and find intermediate states along
the transition pathway. This is achieved through the fact that the distribution transformation process described in Eq. (1) is equivalent to the process in

Eq. (7) if sθD,i is well learned, which is deterministic and invertible hence establishes a correspondence between the structure and latent space. We can then
uniquely map the two given states in the structure space to the latent space,
approximate the path in the latent space by linear interpolation, and then map
the path back to the structure space. Since the distribution in the latent space
is Gaussian which has a convex contour, the linearly interpolated path goes
through high-probability or low-energy regions, so it gives an intuitive guess
of the real reaction path.

3 Results
Here, we demonstrate that DiG can be applied to study protein conformations,
protein-ligand interactions, and molecule adsorption on catalysis surfaces. In
addition, we investigate the inverse design capability of DiG, through its
application to carbon polymorph generation for desired electronic band gaps.

3.1 Protein Conformation Sampling
At physiological conditions, most protein molecules exhibit dynamical behaviors, rather than existing as rigid objects in their most energetically favorable
states. The sampling of these conformations is crucial for the comprehensive
understanding of protein properties and their interactions with other molecules
in cells. Recently, it has been reported that AlphaFold [1] can generate alternative conformations for certain proteins, by manipulating input information
such as multiple sequence alignments (MSA) [43]. However, this approach is
developed on the basis of varying the depth of MSA, it is hard to generalize
to all proteins (especially for those with a small number of similar sequences).
Therefore, it is highly desirable to have advanced AI models that can sample
diverse structures consistent with the energy landscape in the conformational
space [43]. Here, we show that DiG is capable of generating diverse and functionally relevant protein structures, which is a key capability for being able to
efficiently sample equilibrium distributions.
It is noted that the equilibrium distribution of protein conformations is
difficult to obtain experimentally or computationally, so in contrast to protein
structure prediction, there is a lack of high-quality data for training or benchmarking. To train this model, we collect experimental and simulated structures
from public databases. In order to mitigate the data scarcity issue, besides
the structures from the protein databank, we also generated an in-house simulation dataset and developed the PIDP training method (See Supplementary
Sec. A.1.1 and D.1 for training procedure and the dataset). The performance
of DiG was assessed at two levels: (1) comparing the conformational distributions against those obtained from extensive (millisecond timescale) atomistic
MD simulations; (2) validating on proteins with multiple known conformations.
As shown in Fig. 2a, the conformational distributions are obtained from MD
simulations for two proteins from the SARS-CoV-2 virus [44] (the receptorbinding-domain (RBD) of spike protein and the main protease, also known as

3CL protease, see Supplementary Sec. A.7 for details on MD simulation data).
These two proteins are the crucial components of the SARS-CoV-2 virus and
key targets for drug development in the treatment of COVID-19 [45, 46]. The
millisecond timescale MD simulations extensively sample conformation space,
and we therefore regard the resulting distribution as a proxy to the equilibrium distribution. Taking protein sequences as the descriptor inputs for DiG,
structures were generated for these two proteins. Although MD simulation

Fig. 2: Distribution and sampling results for protein conformations.

Fig. 2: (a) Structures generated by DiG resemble the diverse conformations of
millisecond MD simulations. MD simulated structures are projected onto the
reduced 2D space spanned by TICA coordinates, and the probability densities
are depicted using contour lines. For RBD protein, MD simulation reveals four
highly populated regions in the 2D space spanned by TICA coordinates (left
panel). Structures generated by DiG are mapped to this 2D space shown as
orange dots, whose distributions are reflected by the color intensity. Below the
distribution map, structures generated by DiG (thin ribbons) are superposed
to representative structures of four clusters. AlphaFold predicted structures (⋆)
are also shown in the plot. Right panel shows the results of the main protease
of SARS-CoV-2, compared with MD simulations and AlphaFold prediction
results. The contour map reveals three clusters, DiG generates highly similar structures in cluster II & III, while structures in cluster-I are accurately
generated. (b) The performance of DiG on generating multiple conformations
of proteins (each structure is labeled by its PDB ID, except the DEERAF, which is AlphaFold predicted model that is consistent with experimental
observations). Structures generated by DiG (thin ribbons) are compared with
the experimentally determined structures (cylindrical cartoons) in each case.
For the four proteins (adenylate kinase, Lmrb membrane protein, human BRaf kinase, and D-ribose binding protein), structures in two functional states
(distinguished by cyan and brown) are well reproduced by DiG (ribbons).
data of these proteins were not used for DiG training, the generated structures resemble the conformational distributions explored by MD in the reduced
dimension space spanned by collective variables (Fig. 2a). In the 2D projection shown here, the MD simulations of RBD populate four regions, which are
also sampled by DiG (see Fig. 2a, left panel). The four representative structures corresponding to the cluster centers are well generated by DiG. Similarly,
three representative structures for main protease were obtained by clustering analysis on MD simulation trajectories, and then the generated structures
were aligned to these three representatives (Fig. 2a). We noticed that conformations in cluster-I region are not well recovered by DiG, indicating room for
improvement. In terms of conformational space coverage, we compared the DiG
sampled regions with those explored by MD simulations in the conformation
manifold spanned by the TICA variables (Fig. 2a). For example, on the 2D
manifold, about 70% of the RBD conformations sampled by millisecond-scale
MD simulations can be covered with just 10,000 DiG-generated structures (see
Supplementary Fig. S1 for details).
Atomistic MD simulations are computationally very expensive, therefore
millisecond time scale simulations of proteins are rarely reported in literature, except for simulations on special-purpose hardware such as the Anton
supercomputer [13] or extensive distributed simulations combined in Markov
state models [16]. In order to get an additional assessment on the diversity of
protein structures generated by DiG, we turn to proteins for which multiple

structures have been experimentally determined. Although it is a less stringent test, the capability of sampling alternative conformations can facilitate
the research of protein dynamics and functional mechanisms. We analyzed
four proteins, each with two distinguishable conformations corresponding to
different functional states (Fig. 2b). Remarkably, the conformations sampled
by DiG have good coverage in the conformational space near the two states
for each protein. The experimentally determined conformations are shown in
cylinder cartoons, each aligned with two structures generated by DiG (shown
in ribbon representations). For example, the adenylate kinase protein has two
conformations (PDB IDs 1ake and 4ake), each with high-quality structures
in their vicinity (backbone RMSD < 1.0 Å for the structure superposed to
the closed state, 1ake; backbone RMSD < 3.0 Å for the structures superposed to the open state, 4ake). Similarly, for the drug transport protein LmrP,
DiG generated structures resembling both states. We note that one structure is experimentally determined, and the other (denoted as DEER-AF) is
the AlphaFold predicted structure [43] supported by double electron electron resonance (DEER) experimental data [47]. For the case of human B-Raf
kinase, the overall RMSD difference between the two experimentally determined states is not as pronounced as in the other three proteins. The major
structural difference is in the A-loop region and a nearby helix (α C-helix,
indicated in the figure) [48]. Structures generated by DiG accurately recover
such regional structural differences in this kinase protein. Another interesting case is the D-Ribose binding protein with two separated domains, which
can be packed in two distinct conformations. DiG correctly generates structures corresponding to both the straight-up conformation (cylinder cartoon)
and the twisted/tilted conformation. It is noted that if we align one domain of
D-ribose binding protein, the other domain only partially matches the twisted
conformation as an ‘intermediate’ state. Furthermore, for a pair of structures
of the same protein, DiG can be applied to generate transition pathways
by latent space interpolations (see demonstration cases in the DiG webpage:
https://DistributionalGraphormer.github.io). The dynamics revealed by such
pathways can inspire hypotheses on molecular mechanisms for experimental
validation. In summary, DiG is capable of generating diverse protein structures
corresponding to different functional states, thus going beyond the capabilities
of current static structure prediction methods.

3.2 Ligand Structure Sampling around Binding Sites
An immediate extension of protein conformational sampling is to predict
protein-ligand interactions, such as ligand binding positions in druggable pockets. To model the interactions between protein and ligand, we mainly use a
simulation dataset of about 1500 complexes for training (See Supplementary
Sec. D.1 for the dataset). We evaluated the performance of DiG in ligand
binding to protein pockets for 409 protein-ligand systems [49, 50] (not in the
training dataset). By providing atomic positions surrounding a pocket and a
ligand descriptor (here, a SMILES string), DiG generates ligand structures to

Fig. 3: Results of DiG for ligand structure sampling around protein
pockets. (a) The results of DiG on poses of ligands bound to protein pockets. DiG generates ligand structures and binding poses, with good accuracy
compared to the crystal structures (reflected by the RMSD statistics shown
in red histogram for the best matching cases, and the green histogram for the
median RMSD statistics). When considering all 50 predicted binding poses for
each system, diversity is observed, as reflected in the RMSD histogram (yellow color, normalized) compared to the references. (b) Representative systems
show that the diversity in ligand binding poses is related to the binding pocket
properties. For deep and narrow binding pocket such as for the Tyk2 protein
(shown in the surface representation, top panel), DiG predicts highly similar
binding poses for the ligand (in atom-bond representations, top panel). For
the P38 protein the binding pocket is relatively flat and shallow and predicted
ligand poses are highly diverse and have large conformational flexibility (bottom panel, in the same representations as in the Tyk2 case).

fit the pocket. During the ligand structure sampling, DiG models the atomic
coordinate distribution of both binding pocket and the ligand. The flexible
binding pockets were observed in the testing, with changes in atomic positions
up to 1.0 Å in terms of RMSD compared to the input atomic positions. For
the ligand structures, the deviation comes from two sources: (1) the conformational difference between generated structures and experimental structures;
and (2) the difference in the binding pose due to ligand translation and rotation. Among all tested cases, the conformational differences are small, with an
RMSD value of 1.74 Å on average, indicating that generated ligand structures
are highly similar to the bound ligands resolved in crystal structures (Fig. 3a).
When including the binding pose deviations originated from ligand positions
and orientations, larger alignment discrepancies are observed for ligand structures. Yet, the DiG is still capable of predicting at least one correct structure
for each ligand out of 50 generated structures. In a retrospective measurement,
the best-matched structure among 50 generated structures for each ligand is
within 2.0 Å RMSD compared to the experimental data for nearly all 409
testing systems (Fig. 3a for the RMSD distribution, with more cases shown
in Supplementary Fig. S3). The accuracy of generated structures for ligand is

related to the characteristic of binding pockets. For example, the ligand binding to the target protein Tyk2 showed an average deviation of 0.91 Å (RMSD)
from the crystal structure (see Fig. 3b, top). In another example for target
P38, the ligand exhibited more diverse binding poses, likely due to the shallow pocket of this target. Under such circumstances, the most stable binding
pose may be less dominant compared to other favorable poses (Fig. 3b, bottom). MD simulations reveal similar trends as DiG-generated structures, with
ligand binding to Tyk2 more tightly than the case of P38 (Supplementary
Fig. S2). Overall, we observed that the generated structures indeed resemble
experimentally observed poses.

3.3 Catalyst-Adsorbate Sampling
Identifying active adsorption sites is a central task in heterogeneous catalysis.
Due to complex surface-molecular interactions, such tasks rely heavily on a
combination of quantum chemistry methods such as density functional theory
(DFT) and sampling techniques such as MD and grid-search. These lead to
large and sometimes intractable computational costs, especially when it comes
to surfaces with complex chemical environments. We evaluate DiG’s capability
for this task by training it on the MD trajectories of catalyst-adsorbate systems from the Open Catalyst Project and carrying out further evaluations on
random combinations of adsorbates and surfaces that are not included in the
training set [10]. By feeding the model with a substrate and a molecular adsorbate, DiG can predict adsorption sites and stable adsorbate configurations,
along with the probability for each configuration (see Supplementary Sec. A.4
for training details and Supplementary Sec. A.7 for evaluation details). Fig. 4ab shows the adsorption configurations of an acyl group on a stepped TiIr alloy
surface. Multiple adsorption sites are predicted by DiG. To test the plausibility
of these predicted configurations and evaluate the coverage of the predictions,
we carry out a grid-search using DFT methods. The results confirm that DiG
predicts all stable sites found by the grid-search and the adsorption configurations are in close agreement with an RMSD of 0.5 ∼ 0.8 Å (Fig. 4b). It should
be noted that the combination of substrate and adsorbate shown in Fig. 4b
is not included in the training data set. Therefore, the result demonstrates
the cross-system generalization capability of DiG in catalyst adsorption predictions. Here we show only the top view, and Fig. S4 in addition shows the
front view of the adsorption configurations.
DiG not only predicts the adsorption sites with correct configurations, but
also provides a probability estimate for each adsorption configuration. This
capability is illustrated in the systems with single-atom adsorbates (including
H, N, and O) on 10 randomly chosen metallic surfaces. For each combination of
adsorbate and catalyst substrate, the DiG is applied to predict the adsorption
sites and the probability distributions. Then for the same systems, grid-search
DFT calculations were carried out to find all adsorption sites and the corresponding energies. Taking the adsorption sites identified by grid-search as
references, DiG achieved 81% site coverage for single-atom adsorbates on the

Fig. 4: Results of DiG for catalyst-adsorbate sampling problems. (a)
The problem setting: prediction of the adsorption configuration distribution of
an adsorbate on a catalyst surface. (b) The adsorption sites and corresponding
configurations of the adsorbate found by DiG (in color), compared with DFT
results (in white). DiG finds all the adsorption sites, with adsorbate structures
close to the DFT baseline. For all adsoprtion sites and configurations, refer to
Appendix E. (c-f) Adsorption prediction results of single N and O atoms on
catalyst surfaces, compared to DFT calculations. Top panels show the catalyst
surface; the probability distribution of adsorbate molecules on the corresponding catalyst surfaces are shown in the middle panels in log-scale; the bottom
panels show the calculated interactions between the adsorbate molecule and
the catalyst using DFT methods. The adsorption sites and predicted probabilities are highly consistent with the energy landscape obtained by DFT
computations.

10 metallic catalyst surfaces. Fig. 4(c-f) show closer examinations on adsorption predictions for four systems, namely C, H, N, and O on TiN, RhTcHf,
AlHf, and TaPd metallic surfaces (top panels). The predicted adsorption probabilities projected on the surface in parallel with the catalyst surface are shown

in the middle panels. The log-scaled heatmaps of the probabilities show excellent accordance with the adsorption energies calculated using DFT methods
(bottom panels). It is worth noting that the speed of DiG is much faster compared to DFT, i.e., it only takes about 1 minute to sample all adsorption sites
for a catalyst-adsorbate system for DiG on a single modern GPU, but at least
2 hours for a single DFT relaxation with VASP, which number will be further
multiplied by a factor of > 100 depending on the resolution of the searching
grid [51]. Such fast and accurate prediction of adsorption sites and the corresponding distributional features can be useful in identifying the catalytic
mechanisms and guiding the search of new catalysts.

3.4 Property-Guided Structure Generation
While DiG by default generates structures following the learned training data
distribution, the output distribution can be biased to steer the structure generation to meet particular requirements. Here we leverage this capability by
employing DiG for inverse design (described in Sec. 2). As a proof-of-concept,
we search for carbon polymorphs with desired electronic band gaps. Similar
tasks are critical to the discovery of novel photovoltaic and semi-conductive
materials [52]. To train this model, we prepared a structure dataset composed
of carbon atoms by carrying out random structure search based on energy
profiles obtained from DFT calculations [53]. The structures corresponding to
energy minima form the dataset used to train DiG, which in turn are applied
to generate carbon structures. We use a neural network model based on the
M3GNet architecture [11] as the property predictor for band gap, which is fed
to the property-guided structure generation of carbon structures.
Fig. 5 shows the distributions of band gaps calculated from generated carbon structures. In the original training dataset, most structures have a band
gap around 0 eV (see Fig. 5a). When the target band gaps are supplied to
DiG, the structures are generated with the desired band gaps. With the guidance of a band gap model in conditional generation, the distribution is biased
towards the targets, showing pronounced peaks around the target band gaps.
Representative structures are shown in Fig. 5. For conditional generation with
a target band gap of 4 eV, DiG generates stable carbon structures similar to
diamond, which has large band gaps. In the case of 0 eV band gap, we obtain
graphite-like structures with low band gaps. In Fig. 5a, we show some structures by unconditional generation. To evaluate the quality of carbon crystal
structures generated by DiG, we calculate the ratio of structures that match
one of the relaxed structures in the dataset by using the StructureMatcher
in the PyMatgen package [54]. For unconditional generation, the match rate is
99.87%, and the average matched normalized RMSD computed from fractional
coordinates over all sampled structures is 0.16. For conditional generation, the
match rate is 99.99%, but with a higher average normalized RMSD of 0.22.
While increasing the possibility of generating structures with target band gap,
conditional generation can influence the quality of the structures (see Supplementary Sec. F.1 for more discussions). This proof-of-concept study shows

Fig. 5: Property-guided structure generation of carbon structures
with particular band gaps. (a) Electronic band gaps of generated structures from trained DiG with no specification on the desired band gap. The
generated structures do not show any obvious preference on band gaps, closely
resembling the distribution of the training dataset. (b) Structure generated for
three band gaps (0, 2, and 4 eV). The distributions of band gaps for generated
structures peak at the desired values. In particular, DiG generates graphitelike structures when desired band gap is 0 eV; while at 4 eV band gap, the
generated structures are most similar to diamonds. Representative structures
are shown in the inset of the plot.

that DiG not only captures the probability distributions with complex features
in large configurational space, but also can be applied for inverse materials
design, when combined with a property quantifier, such as an ML predictor.
Since the training of the property prediction model (e.g., the M3GNet band
gap model) and the diffusion model of DiG are fully decoupled, our approach
can be readily extended to inverse design for other properties.

4 Discussion
Predicting the equilibrium distribution of molecular states is a formidable
challenge in the molecular sciences, with far-reaching implications for deciphering structure-function relationships, computing macroscopic properties,
and designing novel molecules and materials. With existing methods, a
vast number of measurements or simulated samples of single molecules are
required to gather sufficient data for characterizing the equilibrium distribution. We introduce Distributional Graphormer (DiG), a deep generative
framework capable of predicting probability distributions which enables efficiently sampling diverse conformations and estimating their state densities
across molecular systems. Drawing inspiration from the annealing process, DiG
employs a sequence of deep neural networks to progressively transform state
distributions from a simplistic mathematical form to the target distributions
which can be trained to approximate the equilibrium distribution with suitable
training data.
We have applied DiG to several molecular prediction tasks, including
protein conformation sampling, protein-ligand binding structure generation,
molecular adsorption on catalyst surfaces, and property-guided structure generation. The results show that DiG is capable of generating chemically realistic
and diverse structures, and distributions resembling those of extensive MD simulations in low dimensional projections in some cases. By harnessing the power
of advanced deep learning architectures, DiG can learn the representation
of molecular conformations that are transformed from molecular descriptors,
such as amino acid sequences for proteins or chemical formulas for compound
molecules. Furthermore, its capacity to model complex, multimodal distributions using diffusion models enables it to capture equilibrium distributions in
high-dimensional space.
DiG has been demonstrated to be capable to generalize across molecules
within the same class, such as in the case of proteins, small molecules, and
catalyst structures. Consequently, the framework opens the door to a multitude
of research opportunities and applications in molecular science. Thus, when
fed with suitably distributed training data, DiG can provide insights into the
statistical understanding of molecules, enabling the computing of macroscopic
properties, such as free energies and thermodynamic stability. These insights
are critical for investigating the physical and chemical phenomena of molecular
systems.
Finally, with its capability in generating independent and identically distributed (i.i.d.) conformations from equilibrium distributions, DiG offers a
significant computational advantage over traditional sampling or simulation
approaches that suffer from rare events, such as MCMC or MD simulations.
DiG achieves similar conformation space coverage as millisecond-timescale MD
simulations do in the two tested protein cases. Based on the OpenMM benchmark performance of modern GPU devices, it would require about 7-10 GPU
years on Nvidia A100s to complete a simulation of 1.8 ms for RBD of the spike
protein; while generating 50k structures using DiG only takes about 10 days on

a single A100 GPU without any inference acceleration (see more discussion in
Supplementary Sec. A.6). Similar levels of speedup can be achieved in the case
of predicting adsorbate distribution on the catalyst surface, as elaborated in
the result section. If such order-of-magnitude speed-up can be combined with
generating high-accuracy probability distributions, this will be transformative
for molecular simulation and design.
While the quantitative prediction of equilibrium distributions at given thermodynamic states will hinge upon the availability of training data, the capacity
of DiG to explore vast and diverse conformational spaces contributes to the
discovery of novel and functional molecular structures, including protein structures, ligand conformers, and adsorbate configurations. DiG can therefore help
to bridge the gap between microscopic descriptors and macroscopic observations of molecular systems, with potential impact on various areas of molecular
sciences including life sciences, drug design, catalysis research, and materials
sciences.

References
[1] Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger,
O., Tunyasuvunakool, K., Bates, R., Žı́dek, A., Potapenko, A., et al.:
Highly accurate protein structure prediction with alphafold. Nature
596(7873), 583–589 (2021)
[2] Ying, C., Cai, T., Luo, S., Zheng, S., Ke, G., He, D., Shen, Y., Liu,
T.-Y.: Do transformers really perform badly for graph representation?
Advances in Neural Information Processing Systems 34, 28877–28888
(2021)
[3] Cramer, P.: Alphafold2 and the future of structural biology. Nature
structural & molecular biology 28(9), 704–705 (2021)
[4] Akdel, M., Pires, D.E., Pardo, E.P., Jänes, J., Zalevsky, A.O., Mészáros,
B., Bryant, P., Good, L.L., Laskowski, R.A., Pozzati, G., et al.: A structural biology community assessment of alphafold2 applications. Nature
Structural & Molecular Biology, 1–12 (2022)
[5] Pereira, J., Simpkin, A.J., Hartmann, M.D., Rigden, D.J., Keegan,
R.M., Lupas, A.N.: High-accuracy protein structure prediction in casp14.
Proteins: Structure, Function, and Bioinformatics 89(12), 1687–1699
(2021)
[6] Stärk, H., Ganea, O., Pattanaik, L., Barzilay, R., Jaakkola, T.: Equibind:
Geometric deep learning for drug binding structure prediction. In: International Conference on Machine Learning, pp. 20503–20521 (2022).
PMLR

[7] Corso, G., Stärk, H., Jing, B., Barzilay, R., Jaakkola, T.: DiffDock: Diffusion steps, twists, and turns for molecular docking. In: International
Conference on Learning Representations (2023)
[8] Diaz-Rovira, A.M., Martin, H., Beuming, T., Diaz, L., Guallar, V., Ray,
S.S.: Are deep learning structural models sufficiently accurate for virtual screening? application of docking algorithms to alphafold2 predicted
structures. bioRxiv, 2022–08 (2022)
[9] Scardino, V., Di Filippo, J.I., Cavasotto, C.N.: How good are alphafold
models for docking-based virtual screening? Iscience 26(1) (2023)
[10] Chanussot, L., Das, A., Goyal, S., Lavril, T., Shuaibi, M., Riviere, M.,
Tran, K., Heras-Domingo, J., Ho, C., Hu, W., et al.: Open catalyst 2020
(oc20) dataset and community challenges. ACS Catalysis 11(10), 6059–
6072 (2021)
[11] Chen, C., Ong, S.P.: A universal graph deep learning interatomic potential for the periodic table. Nature Computational Science 2(11), 718–728
(2022)
[12] Schaarschmidt, M., Riviere, M., Ganose, A.M., Spencer, J.S., Gaunt,
A.L., Kirkpatrick, J., Axelrod, S., Battaglia, P.W., Godwin, J.: Learned
force fields are ready for ground state catalyst discovery. arXiv preprint
arXiv:2209.12466 (2022)
[13] Lindorff-Larsen, K., Piana, S., Dror, R.O., Shaw, D.E.: How fast-folding
proteins fold. Science 334(6055), 517–520 (2011)
[14] Barducci, A., Bonomi, M., Parrinello, M.: Metadynamics. Wiley Interdisciplinary Reviews: Computational Molecular Science 1(5), 826–843
(2011)
[15] Kästner, J.: Umbrella sampling. Wiley Interdisciplinary Reviews: Computational Molecular Science 1(6), 932–942 (2011)
[16] Chodera, J.D., Noé, F.: Markov state models of biomolecular conformational dynamics. Current opinion in structural biology 25, 135–144
(2014)
[17] Monticelli, L., Kandasamy, S.K., Periole, X., Larson, R.G., Tieleman,
D.P., Marrink, S.-J.: The martini coarse-grained force field: extension
to proteins. Journal of chemical theory and computation 4(5), 819–834
(2008)
[18] Clementi, C.: Coarse-grained models of protein folding: toy models or
predictive tools? Current opinion in structural biology 18(1), 10–15

(2008)

[19] Wang, J., Olsson, S., Wehmeyer, C., Pérez, A., Charron, N.E., De Fabritiis, G., Noé, F., Clementi, C.: Machine learning of coarse-grained
molecular dynamics force fields. ACS central science 5(5), 755–767
(2019)
[20] Arts, M., Satorras, V.G., Huang, C.-W., Zuegner, D., Federici, M.,
Clementi, C., Noé, F., Pinsler, R., Berg, R.v.d.: Two for one: Diffusion
models and force fields for coarse-grained molecular dynamics. arXiv
preprint arXiv:2302.00600 (2023)
[21] Noé, F., Olsson, S., Köhler, J., Wu, H.: Boltzmann generators: Sampling
equilibrium states of many-body systems with deep learning. Science
365(6457), 1147 (2019)
[22] Kingma, D.P., Dhariwal, P.: Glow: Generative flow with invertible 1x1
convolutions. Advances in neural information processing systems 31
(2018)
[23] Klein, L., Foong, A.Y., Fjelde, T.E., Mlodozeniec, B., Brockschmidt,
M., Nowozin, S., Noé, F., Tomioka, R.: Timewarp: Transferable acceleration of molecular dynamics by learning time-coarsened dynamics. arXiv
preprint arXiv:2302.01170 (2023)
[24] Kirkpatrick, S., Gelatt Jr, C.D., Vecchi, M.P.: Optimization by simulated
annealing. science 220(4598), 671–680 (1983)
[25] Neal, R.M.: Annealed importance sampling. Statistics and computing
11(2), 125–139 (2001)
[26] Del Moral, P., Doucet, A., Jasra, A.: Sequential Monte Carlo samplers. Journal of the Royal Statistical Society: Series B (Statistical
Methodology) 68(3), 411–436 (2006)
[27] Doucet, A., Grathwohl, W.S., Matthews, A.G.d.G., Strathmann, H.:
Annealed importance sampling meets score matching. In: ICLR Workshop on Deep Generative Models for Highly Structured Data (2022)
[28] Sohl-Dickstein, J., Weiss, E., Maheswaranathan, N., Ganguli, S.: Deep
unsupervised learning using nonequilibrium thermodynamics. In: International Conference on Machine Learning, pp. 2256–2265 (2015). PMLR
[29] Ho, J., Jain, A., Abbeel, P.: Denoising diffusion probabilistic models.
In: Advances in Neural Information Processing Systems, vol. 33, pp.
6840–6851 (2020)

[30] Langevin, P.: Sur la théorie du mouvement brownien. Compt. Rendus
146, 530–533 (1908)
[31] Uhlenbeck, G.E., Ornstein, L.S.: On the theory of the Brownian motion.
Physical review 36(5), 823 (1930)
[32] Roberts, G.O., Tweedie, R.L., et al.: Exponential convergence of
Langevin distributions and their discrete approximations. Bernoulli 2(4),
341–363 (1996)
[33] Wibisono, A., Wilson, A.C., Jordan, M.I.: A variational perspective
on accelerated methods in optimization. proceedings of the National
Academy of Sciences 113(47), 7351–7358 (2016)
[34] Anderson, B.D.: Reverse-time diffusion equation models. Stochastic
Processes and their Applications 12(3), 313–326 (1982)
[35] Song, Y., Sohl-Dickstein, J., Kingma, D.P., Kumar, A., Ermon, S.,
Poole, B.: Score-based generative modeling through stochastic differential equations. In: International Conference on Learning Representations
(2021)
[36] Dhariwal, P., Nichol, A.: Diffusion models beat GANs on image synthesis. Advances in Neural Information Processing Systems 34, 8780–8794
(2021)
[37] Ramesh, A., Dhariwal, P., Nichol, A., Chu, C., Chen, M.: Hierarchical text-conditional image generation with clip latents. arXiv preprint
arXiv:2204.06125 (2022)
[38] Risken, H.: Fokker-Planck equation. Springer (1996)
[39] Hutchinson, M.F.: A stochastic estimator of the trace of the influence
matrix for Laplacian smoothing splines. Communications in StatisticsSimulation and Computation 18(3), 1059–1076 (1989)
[40] Grathwohl, W., Chen, R.T., Bettencourt, J., Sutskever, I., Duvenaud, D.:
FFJORD: Free-form continuous dynamics for scalable reversible generative models. In: International Conference on Learning Representations
(2019)
[41] Vincent, P.: A connection between score matching and denoising autoencoders. Neural computation 23(7), 1661–1674 (2011)
[42] Alain, G., Bengio, Y.: What regularized auto-encoders learn from the
data-generating distribution. The Journal of Machine Learning Research
15(1), 3563–3593 (2014)

[43] Del Alamo, D., Sala, D., Mchaourab, H.S., Meiler, J.: Sampling alternative conformational states of transporters and receptors with alphafold2.
Elife 11, 75751 (2022)
[44] Zimmerman, M.I., Porter, J.R., Ward, M.D., Singh, S., Vithani, N.,
Meller, A., Mallimadugula, U.L., Kuhn, C.E., Borowsky, J.H., Wiewiora,
R.P., et al.: Sars-cov-2 simulations go exascale to predict dramatic spike
opening and cryptic pockets across the proteome. Nature chemistry
13(7), 651–659 (2021)
[45] Zhang, L., Lin, D., Sun, X., Curth, U., Drosten, C., Sauerhering, L.,
Becker, S., Rox, K., Hilgenfeld, R.: Crystal structure of sars-cov-2 main
protease provides a basis for design of improved α-ketoamide inhibitors.
Science 368(6489), 409–412 (2020)
[46] Tai, W., He, L., Zhang, X., Pu, J., Voronin, D., Jiang, S., Zhou, Y., Du,
L.: Characterization of the receptor-binding domain (rbd) of 2019 novel
coronavirus: implication for development of rbd protein as a viral attachment inhibitor and vaccine. Cellular & molecular immunology 17(6),
613–620 (2020)
[47] Masureel, M., Martens, C., Stein, R.A., Mishra, S., Ruysschaert, J.-M.,
Mchaourab, H.S., Govaerts, C.: Protonation drives the conformational
switch in the multidrug transporter lmrp. Nature chemical biology 10(2),
149–155 (2014)
[48] Nussinov, R., Zhang, M., Liu, Y., Jang, H.: Alphafold, artificial intelligence (ai), and allostery. The Journal of Physical Chemistry B 126(34),
6372–6383 (2022)
[49] Schindler, C.E., Baumann, H., Blum, A., Böse, D., Buchstaller, H.-P.,
Burgdorf, L., Cappel, D., Chekler, E., Czodrowski, P., Dorsch, D., et
al.: Large-scale assessment of binding free energy calculations in active
drug discovery projects. Journal of Chemical Information and Modeling
60(11), 5457–5474 (2020)
[50] Wang, L., Wu, Y., Deng, Y., Kim, B., Pierce, L., Krilov, G., Lupyan,
D., Robinson, S., Dahlgren, M.K., Greenwood, J., et al.: Accurate and
reliable prediction of relative ligand binding potency in prospective drug
discovery by way of a modern free-energy calculation protocol and force
field. Journal of the American Chemical Society 137(7), 2695–2703
(2015)
[51] Hafner, J.: Ab-initio simulations of materials using vasp: Densityfunctional theory and beyond. Journal of computational chemistry
29(13), 2044–2078 (2008)

[52] Lu, Z.: Computational discovery of energy materials in the era of big
data and machine learning: a critical review. Materials Reports: Energy
1(3), 100047 (2021)
[53] Lu, Z.: Autonomous exploration and learning the off-equilibrium materials space for large-scale machine learning force fields. In preparation
(2023)
[54] Ong, S.P., Richards, W.D., Jain, A., Hautier, G., Kocher, M., Cholia, S.,
Gunter, D., Chevrier, V.L., Persson, K.A., Ceder, G.: Python materials
genomics (pymatgen): A robust, open-source python library for materials
analysis. Computational Materials Science 68, 314–319 (2013)
[55] Durmus, A., Moulines, E.: High-dimensional Bayesian inference via the
unadjusted Langevin algorithm. arXiv preprint arXiv:1605.01559 (2016)
[56] Cheng, X., Bartlett, P.: Convergence of Langevin MCMC in KLdivergence. arXiv preprint arXiv:1705.09048 (2017)
[57] Dalalyan, A.S.: Theoretical guarantees for approximate sampling from
smooth and log-concave densities. Journal of the Royal Statistical
Society: Series B (Statistical Methodology) 79(3), 651–676 (2017)
[58] Raissi, M., Perdikaris, P., Karniadakis, G.E.: Physics-informed neural
networks: A deep learning framework for solving forward and inverse
problems involving nonlinear partial differential equations. Journal of
Computational physics 378, 686–707 (2019)
[59] Jordan, M.I., Ghahramani, Z., Jaakkola, T.S., Saul, L.K.: An introduction to variational methods for graphical models. Machine learning
37(2), 183–233 (1999)
[60] Wainwright, M.J., Jordan, M.I., et al.: Graphical models, exponential
families, and variational inference. Foundations and Trends in Machine
Learning 1(1–2), 1–305 (2008)
[61] Kingma, D.P., Welling, M.: Auto-encoding variational bayes. In: Proceedings of the International Conference on Learning Representations
(ICLR 2014), Banff, Canada (2014). ICLR Committee
[62] Rezende, D., Mohamed, S.: Variational inference with normalizing flows.
In: Proceedings of The 32nd International Conference on Machine
Learning (ICML 2015), Lille, France, pp. 1530–1538 (2015). IMLS
[63] Kingma, D.P., Salimans, T., Jozefowicz, R., Chen, X., Sutskever, I.,
Welling, M.: Improved variational inference with inverse autoregressive
flow. In: Advances in Neural Information Processing Systems, Barcelona,

Spain, pp. 4743–4751 (2016). NIPS Foundation

[64] Li, Y., Turner, R.E.: Renyi divergence variational inference. Advances in
neural information processing systems 29 (2016)
[65] Hernandez-Lobato, J., Li, Y., Rowland, M., Bui, T., Hernandez-Lobato,
D., Turner, R.: Black-box alpha divergence minimization. In: International Conference on Machine Learning, pp. 1511–1520 (2016). PMLR
[66] Midgley, L.I., Stimper, V., Simm, G.N., Schölkopf, B., HernándezLobato, J.M.: Flow annealed importance sampling bootstrap. arXiv
preprint arXiv:2208.01893 (2022)
[67] Hyvärinen, A., Dayan, P.: Estimation of non-normalized statistical models by score matching. Journal of Machine Learning Research 6(4)
(2005)
[68] Cappé, O., Moulines, E., Rydén, T.: Inference in hidden Markov models
(2005)
[69] Karras, T., Aittala, M., Aila, T., Laine, S.: Elucidating the design space
of diffusion-based generative models. arXiv preprint arXiv:2206.00364
(2022)
[70] Song, Y., Durkan, C., Murray, I., Ermon, S.: Maximum likelihood training of score-based diffusion models. In: Advances in Neural Information
Processing Systems, vol. 34, pp. 1415–1428 (2021)
[71] Lu, C., Zheng, K., Bao, F., Chen, J., Li, C., Zhu, J.: Maximum likelihood
training for score-based diffusion ODEs by high order denoising score
matching. In: International Conference on Machine Learning, pp. 14429–
14460 (2022). PMLR
[72] Leach, A., Schmon, S.M., Degiacomi, M.T., Willcocks, C.G.: Denoising diffusion probabilistic models on SO(3) for rotational alignment. In:
ICLR 2022 Workshop on Geometrical and Topological Representation
Learning (2022)
[73] Song, Y., Ermon, S.: Generative modeling by estimating gradients of
the data distribution. In: Advances in Neural Information Processing
Systems, vol. 32 (2019)
[74] Eastman, P., Swails, J., Chodera, J.D., McGibbon, R.T., Zhao, Y.,
Beauchamp, K.A., Wang, L.-P., Simmonett, A.C., Harrigan, M.P., Stern,
C.D., et al.: Openmm 7: Rapid development of high performance algorithms for molecular dynamics. PLoS computational biology 13(7),
1005659 (2017)

[75] Wang, R., Fang, X., Lu, Y., Yang, C.-Y., Wang, S.: The pdbbind
database: methodologies and updates. Journal of medicinal chemistry
48(12), 4111–4119 (2005)
[76] Rodrı́guez-Espigares, I., Torrens-Fontanals, M., Tiemann, J.K., ArandaGarcı́a, D., Ramı́rez-Anguita, J.M., Stepniewski, T.M., Worp, N., VarelaRial, A., Morales-Pastor, A., Medel-Lacruz, B., et al.: Gpcrmd uncovers
the dynamics of the 3d-gpcrome. Nature Methods 17(8), 777–787 (2020)
[77] Min, Y., Wei, Y., Wang, P., Wu, N., Bauer, S., Zheng, S., Shi, Y., Wang,
Y., Wang, X., Zhao, D., et al.: Predicting the protein-ligand affinity
from molecular dynamics trajectories. arXiv preprint arXiv:2208.10230
(2022)
[78] He, J., Tian, K., Luo, S., Min, Y., Zheng, S., Shi, Y., He, D., Liu, H.,
Yu, N., Wang, L., et al.: Masked molecule modeling: A new paradigm of
molecular representation learning for chemistry understanding (2022)
[79] Francoeur, P.G., Masuda, T., Sunseri, J., Jia, A., Iovanisci, R.B., Snyder, I., Koes, D.R.: Three-dimensional convolutional neural networks
and a cross-docked data set for structure-based drug design. Journal of
chemical information and modeling 60(9), 4200–4215 (2020)
[80] Shi, Y., Zheng, S., Ke, G., Shen, Y., You, J., He, J., Luo, S., Liu, C.,
He, D., Liu, T.-Y.: Benchmarking graphormer on large-scale molecular
modeling datasets. arXiv preprint arXiv:2203.04810 (2022)
[81] Ho, J., Salimans, T.: Classifier-free diffusion guidance. arXiv preprint
arXiv:2207.12598 (2022)
[82] Song, J., Meng, C., Ermon, S.: Denoising diffusion implicit models. In:
International Conference on Learning Representations (2021)
[83] Bao, F., Li, C., Zhu, J., Zhang, B.: Analytic-dpm: an analytic estimate of the optimal reverse variance in diffusion probabilistic models.
In: International Conference on Learning Representations (2022)
[84] Lu, C., Zhou, Y., Bao, F., Chen, J., Li, C., Zhu, J.: Dpm-solver: A fast
ode solver for diffusion probabilistic model sampling in around 10 steps.
In: Advances in Neural Information Processing Systems
[85] Lu, C., Zhou, Y., Bao, F., Chen, J., Li, C., Zhu, J.: Dpm-solver++:
Fast solver for guided sampling of diffusion probabilistic models. arXiv
preprint arXiv:2211.01095 (2022)
[86] Karras, T., Aittala, M., Aila, T., Laine, S.: Elucidating the design space
of diffusion-based generative models. In: Advances in Neural Information

Processing Systems (2022)

[87] Perez-Hernandez, G., Paul, F., Giorgino, T., De Fabritiis, G., Noé, F.:
Identification of slow molecular order parameters for markov model
construction. The Journal of chemical physics 139(1) (2013)
[88] Schwantes, C.R., Pande, V.S.: Improvements in markov state model
construction reveal many non-native interactions in the folding of ntl9.
Journal of chemical theory and computation 9(4), 2000–2009 (2013)
[89] Scherer, M.K., Trendelkamp-Schroer, B., Paul, F., Pérez-Hernández,
G., Hoffmann, M., Plattner, N., Wehmeyer, C., Prinz, J.-H., Noé, F.:
PyEMMA 2: A Software Package for Estimation, Validation, and Analysis of Markov Models. Journal of Chemical Theory and Computation 11,
5525–5542 (2015). https://doi.org/10.1021/acs.jctc.5b00743. Accessed
2015-10-19
[90] McGibbon, R.T., Beauchamp, K.A., Harrigan, M.P., Klein, C., Swails,
J.M., Hernández, C.X., Schwantes, C.R., Wang, L.-P., Lane, T.J., Pande,
V.S.: Mdtraj: A modern open library for the analysis of molecular
dynamics trajectories. Biophysical Journal 109(8), 1528–1532 (2015).
https://doi.org/10.1016/j.bpj.2015.08.015
[91] Zhang, Y., Skolnick, J.: Scoring function for automated assessment of
protein structure template quality. Proteins: Structure, Function, and
Bioinformatics 57(4), 702–710 (2004)
[92] Xu, J., Zhang, Y.: How significant is a protein structure similarity with
tm-score= 0.5? Bioinformatics 26(7), 889–895 (2010)
[93] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez,
A.N., Kaiser, L., Polosukhin, I.: Attention is all you need. Advances in
neural information processing systems 30 (2017)
[94] Jing, B., Eismann, S., Suriana, P., Townshend, R.J., Dror, R.: Learning
from protein structure with geometric vector perceptrons. arXiv preprint
arXiv:2009.01411 (2020)
[95] Schütt, K., Unke, O., Gastegger, M.: Equivariant message passing for the
prediction of tensorial properties and molecular spectra. In: International
Conference on Machine Learning, pp. 9377–9388 (2021). PMLR
[96] wwPDB Consortium: Protein Data Bank: the single global archive for 3d
macromolecular structure data. Nucleic acids research 47(D1), 520–528
(2019)
[97] Steinegger, M., Söding, J.: Clustering huge protein sequence sets in linear

time. Nature communications 9(1), 2542 (2018)
[98] Zhang, S., Krieger, J.M., Zhang, Y., Kaya, C., Kaynak, B., MikulskaRuminska, K., Doruker, P., Li, H., Bahar, I.: Prody 2.0: increased scale
and scope after 10 years of protein dynamics modelling with python.
Bioinformatics 37(20), 3657–3659 (2021)
[99] Eastman, P., Friedrichs, M.S., Chodera, J.D., Radmer, R.J., Bruns,
C.M., Ku, J.P., Beauchamp, K.A., Lane, T.J., Wang, L.-P., Shukla, D.,
et al.: Openmm 4: a reusable, extensible, hardware independent library
for high performance molecular simulation. Journal of chemical theory
and computation 9(1), 461–469 (2013)
[100] Su, M., Yang, Q., Du, Y., Feng, G., Liu, Z., Li, Y., Wang, R.: Comparative assessment of scoring functions: the casf-2016 update. Journal of
chemical information and modeling 59(2), 895–913 (2018)
[101] Van Der Spoel, D., Lindahl, E., Hess, B., Groenhof, G., Mark, A.E.,
Berendsen, H.J.: Gromacs: fast, flexible, and free. Journal of computational chemistry 26(16), 1701–1718 (2005)
[102] Lindorff-Larsen, K., Piana, S., Palmo, K., Maragakis, P., Klepeis, J.L.,
Dror, R.O., Shaw, D.E.: Improved side-chain torsion potentials for the
amber ff99sb protein force field. Proteins: Structure, Function, and
Bioinformatics 78(8), 1950–1958 (2010)
[103] Sousa da Silva, A.W., Vranken, W.F.: Acpype-antechamber python
parser interface. BMC research notes 5(1), 1–8 (2012)
[104] Van Gunsteren, W.F., Berendsen, H.J.: A leap-frog algorithm for
stochastic dynamics. Molecular Simulation 1(3), 173–185 (1988)
[105] Essmann, U., Perera, L., Berkowitz, M.L., Darden, T., Lee, H., Pedersen,
L.G.: A smooth particle mesh ewald method. The Journal of chemical
physics 103(19), 8577–8593 (1995)
[106] Hess, B., Bekker, H., Berendsen, H.J., Fraaije, J.G.: Lincs: a linear
constraint solver for molecular simulations. Journal of computational
chemistry 18(12), 1463–1472 (1997)
[107] Mongan, J., Case, D.A., McCammon, J.A.: Constant ph molecular
dynamics in generalized born implicit solvent. Journal of computational
chemistry 25(16), 2038–2048 (2004)
[108] Hammer, B., Hansen, L.B., Nørskov, J.K.: Improved adsorption energetics within density-functional theory using revised perdew-burkeernzerhof functionals. Physical review B 59(11), 7413 (1999)

[109] Kresse, G., Furthmüller, J.: Efficient iterative schemes for ab initio totalenergy calculations using a plane-wave basis set. Physical review B
54(16), 11169 (1996)
[110] Ramachandran, G.N., Ramakrishnan, C., Sasisekharan, V.: Stereochemistry of polypeptide chain configurations. Journal of Molecular Biology
7(1), 95–99 (1963). https://doi.org/10.1016/S0022-2836(63)80023-6
[111] Köhler, J., Chen, Y., Kramer, A., Clementi, C., Noé, F.: Flow-Matching:
Efficient coarse-graining of molecular dynamics without forces. Journal
of Chemical Theory and Computation 19(3), 942–952 (2023)

5 Acknowledgements
We thank Nathan A. Baker, Lixin Sun, Bas Veeling, Victor Garcı́a Satorras,
Andrew Foong and Cheng Lu for insightful discussions; Shengjie Luo for helping with dataset preparations; Jingjie Su for managing the project; Jingyun Bai
for helping with figure design; colleagues at Microsoft for their encouragement
and support.

6 Author information
Contributions
S.Zheng and TY.Liu led the research. S.Zheng, J.He, C.Liu, Z.Lu and H.Liu
conceived the project. J.He, C.Liu, Y.Shi, W.Feng and F.Ju and J.Wang developed the diffusion model and training pipeline. J.He, Y.Shi, Z.Lu, J.Zhu, F.Ju,
H.Zhang and H.Liu developed data and analytics systems. H.Liu, Y.Shi, Z.Lu,
Y.Min and S.Tang conducted simulations. H.Hao, P.Jin, C.Chen, and F.Noé
contributed technical advice and ideas. S.Zheng, J.He, C.Liu, Y.Shi, Z.Lu,
F.Noé, H.Zhang and H.Liu wrote the paper with the inputs from all authors.

Corresponding authors
Correspondence to Shuxin Zheng, Chang Liu, Haiguang Liu and Tie-Yan Liu.

Appendix A
A.1

Technical Details

Formulation of DiG

The forward process Eq. (1) is constructed using the Langevin dynamics that
takes the simple distribution psimple := N (0, I) as its stationary distribution:
dRt = 21 ∇ log psimple (Rt ) dt+dBt = − 12 Rt dt+dBt . From any conformational
distribution of any system as the initial distribution qD,0 (R0 ), the distribution
evolves under this process and converges to psimple exponentially [32, 55–57].
For a faster simulation convergence, it is preferred to introduce a time dilation
scheme βt that increases in t [33]. This gives Eq. (1).
To draw structure samples using DiG, we simulate the reverse process
Eq. (2) from samples from psimple the standard Gaussian distribution, which
can be easily drawn independently. Note that this “reverse” is not a samplelevel point-to-point inverse, but a distribution-level inverse: denoting its
induced distribution as pt̄ , if pt̄=0 = qD,τ , then pt̄=τ = qD,0 . When employing a trained score model sθD,t to approximate the score function ∇ log qD,t ,
the reverse process can be simulated by the Euler-Maruyama
discretiza

tion using the step size h up to o(h) local error: Rī+1 = 1 + 12 βī Rī +
βī sθD,ī (Rī ) + N (0, βī I), where the indexed quantities are evaluated at t̄ := īh,
and βī := hβt̄=īh , and “+N (· · · )” denotes adding a randomly drawn sample from the denoted
distribution. In the original step index i, this
 Gaussian

becomes: Ri−1 = 1 + 2 βi Ri + βi sθD,i (Ri ) + N (0, βi I). By design h is chosen small for accurate simulation, so is each βi . Hence we can leverage the
= 1 + 12 βi + o(h) which does not increase the dicretizaapproximation √1−β
i
tion local error. This gives Eq. (3) for generating samples from the equilibrium
distribution.

A.1.1

Physics-Informed Diffusion Pre-training

The goal of the score model sθD,t (Rt ) is to match the corresponding true score
function ∇ log qD,t (Rt ) from the forward process Eq. (1) for each t ∈ [0, τ ].
To better leverage the diffusion-process construction of DiG, we use a partial
differential equation governing the true score function and construct a loss
function that enforces the equation to hold for training the score model.
Under a general diffusion process dRt = ft (Rt ) dt + gt dBt , the instantaneous distribution transformation is given by the Fokker-Planck equation
(FPE; in logarithm form):
∂
log qt (Rt ) = − ∇ · ft (Rt ) − ∇ log qt (Rt ) · ft (Rt )
∂t

g2 
+ t ∇2 log qt (Rt ) + ∥∇ log qt (Rt )∥ ,

(A1)

Table A1: Notations.
General formulation
D
R
(m)

{RD,0 }M
m=1
(n)

N

data
{RD,0 }n=1

D
ED (R)
kB
T
c
I
ı, ȷ ∈ {1, 2, · · · , I}

System descriptor
Molecular structure
Molecular structures of system D in the dataset for
PIDP training
Molecular structures of system D in the dataset for
data-based (denoising score matching) training
Dimension of R
(Potential) Energy function of system D
Boltzmann constant
Temperature
A property of molecular structure
Length of descriptor / number of individual elements
in a system
Index for individual elements in a system
Diffusion process

τ
t ∈ [0, τ ]
N
i ∈ {1, 2, · · · , N }
h (= τ /N )
t̄ or ī
Bt and B̄t
ft (Rt )
gt
qD,0
R0
qD,t or qD,i
Rt or Ri
q(Rt | R0 ) or q(Ri | R0 )
βt or βi
σt or σi
ϵt or ϵi
sθD,t or sθD,i
ϵθD,t or ϵθD,i
psimple
pθD,t or pθD,i

Total time length/duration of the forward diffusion process
Time variable (continuous)
Number of time discretization steps for the diffusion process
Time step (discrete)
Time discretization step size
Reverse time or step
Standard Brownian motion in dimension D and
its reverse process
Drift function in a general diffusion process
Diffusion rate scheme in a general diffusion process
Equilibrium distribution of system D
(under a certain temperature)
Molecular structure variable following
equilibrium distribution qD,0
Distribution of molecular structure in intermediate
time or step in the forward diffusion process
Molecular structure variable in intermediate time or step,
following qD,t or qD,i
Marginal transition kernel of the forward diffusion process
Time dilation scheme.
Note βi := hβti which is different from others
Noise variance scheme
(standard deviation of q(Rt | R0 ) or q(Ri | R0 ))
Standard Gaussian noise variable
Score model for qD,t or qD,i
Noise-predicting model for qD,t or qD,i
The simple distribution to which the forward diffusion
process converges
Distribution of molecular structure in intermediate
time or step in the reverse diffusion process simulated
by sθD,t or sθD,i or ϵθD,t or ϵθD,i

For the specific diffusion process Eq. (1), the evolving
distribution qt from


∂
log qD,t (Rt ) = β2t D + Rt · ∇ log qD,t (Rt ) +
the forward process satisfies: ∂t

∇2 log qD,t (Rt ) + ∥∇ log qD,t (Rt )∥ , where D is the dimension of R. Tak
∂
ing the gradient of the above equation gives: ∂t
∇ log qD,t (Rt ) = β2t ∇ ·



Rt · ∇ log qD,t (Rt ) + ∇ ∇ · ∇ log qD,t (Rt ) + ∇∥∇ log qD,t (Rt )∥ , which

becomes an equation of the score function ∇ log qD,t (Rt ). To well approximate
∇ log qD,t (Rt ), the score model sθD,t (Rt ) also needs to satisfy this equation.
To enforce it, we follow the idea of physics-informed neural networks [58] that
converts a differential equation into a loss function of the to-be-solved function. The loss function is typically taken as the squared norm of the equality
residual, which in our case is:




βt 
∂
∇ · Rt · sθD,t (Rt ) + ∇ ∇ · sθD,t (Rt ) + ∇ sθD,t (Rt )
− sθD,t (Rt ) ,
∂t
for each t. By time discretization and evaluating the loss on a set of samples
(m)
{RD,i }M
m=1 , this gives the first term in Eq. (4).
The FPE does not have (nor need) a boundary condition as long as
each qD,t is normalized. For the initial condition, we know that the score
of the target equilibrium distribution ∇ log qD,0 (R0 ) = −∇ED (R0 )/(kB T )
is exactly given by the gradient of the energy function of the system. This
is where the energy function comes to supervise the model, and this supervision propagates to other time steps via the first term of the loss. To
implement this initial condition, we minimize sθ0 (R0 ) − ∇ log qD,0 (R0 ) =

sθ0 (R0 ) + ∇ED (R0 )/(kB T ) , which leads to the second term in Eq. (4). Note
that in Eq. (4) the loss term is not imposed on t0 = 0 (i.e., i = 0). This
is because in the actual implementation, the score model is expressed using
a noise-predicting model ϵθD,t as sθD,t = −σt ϵθD,t (explained in Supplementary
Sec. A.1.2), which, at t = 0, the vanishing σ0 = 0 causes an ill-defined score
model. This is commonly solved by starting the diffusion simulation from an
infinitesimal initial time step [35], which corresponds to t = h or i = 1 here.
On the other hand, from the data-generation process Eq. (3), the last required
time step for the model is i = 1, where the sample needs to be updated to
follow the equilibrium distribution. So it is reasonable to supervise sθD,i=1 or
ϵθD,i=1 with the energy function.
In comparison, we note that there are other common approaches to train a
generative model using a given energy function, but they cannot leverage the
advantage of the diffusion-process construction of DiG and thus do not enjoy
the step-by-step supervision pattern and are not as effective to train large models. The most popular way is to minimize the reverse Kullback-Leibler (KL)
divergence KL(pθD,0 ∥qD,0 ) between the model-defined equilibrium distribution
and the true equilibrium distribution, which is equivalent to minimizing the

(Helmholtz) free energy:
FreeEngD = EpθD,0 (R0 ) [ED (R0 ) + kB T log pθD,0 (R0 )].
In the expression, no sample from qD,0 is required, so the access to the energy
function ED suffices for training. This approach is known as variational inference [59–63] in machine learning, and the negative (Helmholtz) free energy
is also called evidence lower bound (ELBO). This method is recently used
to train a generative model for the equilibrium distribution of molecular systems [21]. A more modern approach minimizes the alpha divergence between
the model and the equilibrium distributions [64, 65], which generalizes the
reverse KL divergence and ameliorates the mode-collapse tendency to some
extent. It is also applied to molecular systems recently [66]. These methods
can be directly applied to DiG given the density evaluation method Eq. (6),
but it loses step-by-step supervision as it only supervises the end distribution
pθD,0 , which makes training large models hard. Moreover, evaluating the density
function requires an ODE solver, so the optimization requires backpropagation
through the ODE solver, which is very costly.

A.1.2

Training DiG with Data

To develop a method to train the model step-by-step using data from qD,0 , we
start by score matching for each step i, that is to minimize

EqD,i (Ri ) sθD,i (Ri ) − ∇ log qD,i (Ri )

.

Although this loss can be made tractable (i.e., to get rid of the unknown true
score function ∇ log qD,i ) using the standard score matching technique [67], the
resulting loss function involves the divergence of the score model ∇ · sθD,i which
is expensive to evaluate and optimize. Another way to make it tractable is via
the denoising score matching technique [41, 42]. The method first reforms the
intermediate marginal distribution in terms of the marginal transition kernel
q(Ri | R0 ) from the forward process (which
does not depend on a specific
R
system hence no D subscript), qD,i (Ri ) = qD,0 (R0 )q(Ri | R0 ) dR0 , and then
decompose the score function as:
Z
qD,0 (R0 )∇Ri q(Ri | R0 ) dR0
∇ log qD,i (Ri ) =
qD,i (Ri )
Z
q(Ri | R0 )
∇Ri log q(Ri | R0 ) dR0
=
qD,0 (R0 )
qD,i (Ri )
= EqD (R0 |Ri ) [∇Ri log q(Ri | R0 )],
a.k.a Fisher’s identity [68]. The score-matching loss then becomes:

EqD,i (Ri ) sθD,i (Ri ) − ∇ log qD,i (Ri )

(A2)

= EqD,i (Ri ) sθD,i (Ri )



− 2EqD,i (Ri ) sθD,i (Ri ) · ∇ log qD,i (Ri )

+ EqD,i (Ri ) ∥∇ log qD,i (Ri )∥
Eq. (A2)

=

EqD,i (Ri ) Eq(R0 |Ri ) sθD,i (Ri )


− 2EqD,i (Ri ) Eq(R0 |Ri ) sθD,i (Ri ) · ∇Ri log q(Ri | R0 )
+ EqD,i (Ri ) ∥∇ log qD,i (Ri )∥

= EqD,i (Ri ) Eq(R0 |Ri ) sθD,i (Ri ) − ∇Ri log q(Ri | R0 )
− EqD,i (Ri ) Eq(R0 |Ri ) ∥∇Ri log q(Ri | R0 )∥
+ EqD,i (Ri ) ∥∇ log qD,i (Ri )∥

= EqD,0 (R0 ) Eq(Ri |R0 ) sθD,i (Ri ) − ∇Ri log q(Ri | R0 )

2
+ EqD,0 (R0 ) Eq(Ri |R0 ) ∥∇ log qD,i (Ri )∥ − ∥∇Ri log q(Ri | R0 )∥ .
Noting that the second term in the last expression is a constant of θ, optimizing
the score-matching loss for step i is equivalent to minimizing the first term:

EqD,0 (R0 ) Eq(Ri |R0 ) sθD,i (Ri ) − ∇Ri log q(Ri | R0 )

.

(A3)

This is the denoising score matching loss. To explain the name, in the original
context, q(Ri | R0 ) = N (Ri | R0 , σi2 I) which adds noise to the data sample
R0 to get a noisy version Ri , and the resulting loss

EqD,0 (R0 ) Eq(Ri |R0 ) sθD,i (Ri ) +
=

Ri − R0
σi2

Eq (R ) Eq(Ri |R0 ) Ri + σi2 sθD,i (Ri ) − R0
σi2 D,0 0

drives the “decoder” Ri + σi2 sθD,i (Ri ) to recover the original clean data point
R0 by “denoising” Ri .
Optimizing the denoising score matching loss Eq. (A3) is tractable once we
know the conditional distribution q(Ri | R0 ), which is fortunately available in
closed form for the forward process Eq. (1). Under continuous-time, the result
Rt
is q(Rt | R0 ) = N (Rt | αt R0 , σt2 I) [35, 69], where αt := exp(− 12 0 βt′ dt′ )
p
and σt := 1 − αt2 . For a discretized expression, recall that the time interval
[0, τ ] is uniformly divided into N + 1 points with step size h = τ /N , step i
corresponds to time t = ih, and βi := hβt=ih . This leads to

v
v
u
u
i
i
X
Y
u
u
t
αt=ih = exp(−
βj + o(h)) = texp(o(h))
exp(−βj )
j=1

j=1

v
v
u i
u
i
Y
uY
u
t
(1 − βj + o(h)) = t (1 − βj ) + o(h)
= (1 + o(h))
j=1

=

i
Y

j=1

p

1 − βj + o(h),

j=1

p
Qi p
so we can take αi := j=1 1 − βj . Correspondingly, σi = 1 − αi2 . The
required conditional distribution is then:
q(Ri | R0 ) = N (Ri | αi R0 , σi2 I).

(A4)

The loss Eq. (A3) for time step i then becomes EqD,0 (R0 ) Eq(Ri |R0 ) sθD,i (Ri ) +
(Ri − αi R0 ) .
σi2

Using the reparameterization of the Gaussian distribution q(Ri | R0 ) as Ri = αi R0 + σi ϵi where ϵi ∼ p(ϵi ) := N (0, I), the
=
loss is further reformed as: EqD,0 (R0 ) Ep(ϵi ) sθD,i (αi R0 + σi ϵi ) + σ1i ϵi

E
E
σi2 qD,0 (R0 ) p(ϵi )

σi sθD,i (αi R0 + σi ϵi ) + ϵi . To balance the scale of the loss
for different i ∈ {1, · · · , N }, the loss Eq. (A3) for step i is normalized by the
scale of Eq(Ri |R0 ) ∥∇Ri log q(Ri | R0 )∥ = Ep(ϵi ) σϵii = σ12 [35], which finally
i
leads to Eq. (5).
From the expression of this loss Eq. (5), we find that the “model”
−σi sθD,i (αi R0 + σi ϵi ) can be seen as to “predict the noise label” ϵi , whose distribution is well centered and scaled. This is the range that a deep learning
model works the best. So to make a comfortable and friendly learning task, we
implement the model to directly output the vector value for −σi sθD,i , which
we denote as ϵθD,i and call it the noise-predicting model. The score model can
still be recovered by:
sθD,i (Ri ) = −ϵθD,i (Ri )/σi ,

(A5)

as an approximation to the true score function ∇ log qD,i (Ri ). The training
loss Eq. (5) then becomes:
N

1 X
EqD,0 (R0 ) Ep(ϵi ) ϵθD,i (αi R0 + σi ϵi ) − ϵi .
N i=1

(A6)

This recovers the formulation in [29, 35]. To understand the loss, note the
marginal transition kernel Eq. (A4) of the forward process means Ri = αi R0 +
σi ϵi where ϵi ∼ N (0, I). So the ϵθD,i model tries to recover the noise variable
ϵi from Ri that were used to generate Ri .

A.1.3

Density Evaluation using DiG

Viewed in the continuous-time limit, DiG defines a distribution via transforming psimple through the reverse process Eq. (2), where the score function is
approximated by the model. Written in forward time t, this process follows
the following SDE:
dRt = −

p
βt
Rt dt − βt sθD,t (Rt ) dt + βt dB̄t ,

(A7)

where B̄t is the reverse of the Brownian motion. The distribution transformation under this process is given by its FPE in Eq. (A1):
∂
log pθD,t (Rt )
∂t
 β

 β

t
t
= − ∇ · − Rt − βt sθD,t (Rt ) − ∇ log pθD,t (Rt ) · − Rt − βt sθD,t (Rt )

βt  2
θ
θ
−
∇ log pD,t (Rt ) + ∇ log pD,t (Rt )
,
(A8)
where the last term has a negative sign in correspondence to the reverse Brownian motion. When the model is well-learned, sθD,t well approximates ∇ log qD,t
and pθD,t well approximates qD,t , hence we can approximate ∇ log pθD,t also
using sθD,t . This turns Eq. (A8) into: 1

 β

∂
βt
t
log pθD,t (Rt ) = − ∇ · − Rt − sθD,t (Rt )
∂t
 β

βt
t
θ
− ∇ log pD,t (Rt ) · − Rt − sθD,t (Rt ) .

(A9)

Comparing this equation with the general-form FPE in Eq. (A1), we can find
that this equation is exactly the FPE of the “deterministic diffusion process”
defined by the ODE in Eq. (7). In other words, the ODE in Eq. (7), and the
∂
SDE in Eq. (A7), render the same ∂t
log pθD,t (Rt ) hence the same marginal
θ
distribution pD,t (Rt ) in each time step t (since they have the same terminal
distribution pτ = psimple ; note the mentioned requirement sθD,t = ∇ log pθD,t for
this claim to hold). Since the SDE in Eq. (A7) is the same as Eq. (2) and in turn
leads to the sampling/generation process in Eq. (3), this finding indicates that
we can also generate equilibrium-distribution samples by simulating the ODE
in Eq. (7). This kind of deterministic process or ODE sampling process is used
in protein conformation sampling (see the end of Supplementary Sec. A.2.1)
and property-guided structure generation (Supplementary Sec. A.5).
Back to density evaluation using DiG, we can estimate the density function of the model-defined equilibrium distribution pθD,0 by integrating w.r.t
When sθt ̸= ∇ log qD,t or qD,τ ̸= pτ := psimple , Eq. (A8) and Eq. (A9) (or Eq. (A7) and
Eq. (7)) give different evolving densities. See [70, 71] for more discussions.

the diffusion time step t following the above ODE in Eq. (A9), which does
not contain any unknown objects (recall that we made the assumption that
sθD,t = ∇ log pθD,t to use Eq. (A9)). Let Rt be a solution to Eq. (7), which is a
deterministic curve in the state space. Then we find the total derivative w.r.t
time t (a.k.a material/particle derivative) is:
d
∂
dRt
log pθD,t (Rt ) =
log pθD,t (Rt ) + ∇ log pθD,t (Rt ) ·
dt
∂t
dt
 β

βt
∂
t
θ
θ
log pD,t (Rt ) + ∇ log pD,t (Rt ) · − Rt − sθD,t (Rt ) .
=
∂t
Compared with Eq. (A9), we find:

 β
 D
βt
βt
d
t
log pθD,t (Rt ) = −∇ · − Rt − sθD,t (Rt ) = βt + ∇ · sθD,t (Rt ).
dt
By integration w.r.t t, this gives:
log pθD,0 (R0 ) = log pθτ (Rτ ) −

Z τ

βt
D
∇ · sθD,t (Rt ) dt −

Z τ
βt dt,

which gives Eq. (6).
The equivalent deterministic process described by Eq. (7) is called “probabilistic flow ODE” in machine learning literature [35]. Since this deterministic
process produces the same marginal distribution pθD,t (particularly the equilibrium distribution pθD,t ), it can also be used to generate samples. Due to
the deterministic nature, this approach enables more techniques that could
accelerate the sampling process (Supplementary Sec. A.6).

A.2

Protein Conformation Sampling

A.2.1

Diffusion Process on Coarse-Grained Representation
of Protein

Following the practice of successful protein structure prediction methods, e.g.,
AlphaFold [1], we use the coarse-grained representation for protein as the R
variable. With residues treated as rigid bodies, proteins are represented by
the coordinates C in R3 of alpha-carbon atoms and the orientations Q in
the 3-dimensional rotation group (a.k.a special orthogonal group) SO(3) of
all the residues. Following AlphaFold [1] (Supplementary 1.8.1), the coordinates and orientations are constructed using backbone atom positions from
the experimental structure, followed by a Gram–Schmidt process.
For the coordinates C, the standard diffusion modeling can be applied.
However, it is not straightforward for the orientation, as SO(3) is a nonEuclidean manifold. Therefore, the forward and reverse diffusion processes
need to be generalized. For this treatment, we adopted the technique from [7,
72].

Diffusion Process on the Orientations in the Special Orthogonal
Group
Noting that SO(3) is a Lie group (i.e., a manifold that is also an algebraic
group), we can represent its elements in its Lie algebra (i.e., the tangent space
at the identity element) so(3), which is a 3-dimensional linear space where
vector addition and scaling are valid and random sampling is conventional.
Specifically, a 3-dimensional vector q = (x, y, z) ∈ so(3) can be interpreted
as defining the rotation axis and the rotation angle (the amount of rotation)
of the corresponding rotation transformation on R3 by the direction and the
norm of q as a usual vector in R3 . The rotation matrix, as a form to represent
an element in SO(3), can be constructed by:



0 z −y
Q = Exp −z 0 x ∈ SO(3), q = (x, y, z) ∈ so(3),
y −x 0

(A10)

in the conventional sense of a matrix exponential map.
To ease the calculation on SO(3), the forward diffusion process on it is
taken as the corresponding Brownian motion (i.e., no drift term),

r
dQt =

dσt2
dB̃t ,
dt

(A11)

q
dσt2
where B̃t denotes the Brownian motion on SO(3), and
dt (with σt strictly
increasing) is a time-dilation factor. This process converges to the uniform
distribution (maximal entropy distribution on a compact space; SO(3) is compact) as the corresponding psimple . Simulation of the Brownian motion, say,
from time step ti−1 to ti , can be analogously done (up to o(ti −ti−1 ) discretization error) by adding a noise variable from the isotropic Gaussian distribution
on SO(3) with variance σt2i − σt2i−1 , denoted as IG SO(3) (0, σt2i − σt2i−1 ). Drawing samples from IG SO(3) (0, σ 2 ) can be done in so(3) by uniformly sampling a
direction in R3 for q, and sampling the length of q (the length is within [0, π])
from the 1-dimensional distribution with the following density function:
1 − cos ∥q∥
p̃IG,σ2 (∥q∥),
π
∞
X
−l(l+1)(σt2 −σt2
) sin((l + 2 )∥q∥)
i
i−1
where p̃IG,σ2 (∥q∥) :=
(2l + 1)e
.
sin( 21 ∥q∥)
l=0
pIG,σ2 (∥q∥) =

(A12)

The density function written in q under the Lebesgue measure in so(3) is then
IG SO(3) (q | 0, σ 2 ) ∝ pIG,σ2 (∥q∥).
We learn the score model (instead of the noise-predicting model) for this
setting. As a gradient, the output of the score at time t becomes an element
in the tangent space at Qt . Again thanks to the group structure, they can be
mapped to the tangent space at the identity element, i.e. so(3). The norm in

so(3) consistent with the metric on SO(3) (i.e., the amount of rotation) is just
the Euclidean 2-norm on the vector form q. Hence in the Lie algebra so(3),
metric-related objects are the common Euclidean ones, including norm, gradient and divergence, which are to be used in the FPE Eq. (A1) hence the
corresponding PIDP loss Eq. (4) and data-based loss Eq. (5). Nevertheless,
there is a subtlety regarding the measure. To make the score function consistent with the diffusion process via the FPE, the density function should
be taken w.r.t the uniform distribution on SO(3), which does not project to
the Lebesgue measure (“uniform distribution”) in so(3). Instead, the SO(3)
uniform distribution has the density:
pUnif (q) :=

1 − cos ∥q∥
, (∥q∥ ⩽ π)
π

(A13)

under the Lebesgue measure in so(3). Note this is also what psimple takes. So
p(q)
the required score function of a distribution should be ∇ log pUnif
(q) , where
p(q) is the density function of the distribution under the Lebesgue measure in
so(3). In particular, the score function of the isotropic Gaussian on SO(3) is
∇q log p̃IG,σ2 (∥q∥).
With these facts, we are ready to develop PIDP and data-based training
for a diffusion model that involves the SO(3) space. Recall that the coarsegrained representation R for proteins comprises alpha-carbon coordinates C
and the orientations Q of residues. The orientations can be equivalently represented in so(3) as q, so we have R = (C, q). Hence, the score model and
the energy gradient (appearing in PIDP) take both C and q as input, and
output vectors for both C and q. Since the output vectors are in different
(C),θ (q),θ
spaces and have different losses, we split the output: sθD,t = (sD,t , sD,t ), and
∇ED = (∇C ED , ∇q ED ).
(q),θ
Now consider the PIDP loss for sD,t . Following the forward process in
Eq. (A11) and adopting the above definition of score function, the FPE
Eq. (A1) leads to the loss:
2

1 dσt2 
∂ (q),θ
(q),θ
(q),θ
∇ ∇ · sD,t (Ct , qt ) + ∇ sD,t (Ct , qt )
− sD,t (Ct , qt )
2 dt
∂t
(q),θ

+λ sD,0 (C0 , q0 ) + ∇q0 ED (C0 , q0 )/(kB T )

.

(A14)

Following the pattern to run a PIDP loss as introduced in Sec. 2, the sample
(m)
(m)
of (C0 , q0 ) is drawn from relevantly low-energy structures {(CD,0 , qD,0 )}M
m=1
for protein D (not necessarily following the equilibrium distribution), and the
corresponding (Ct , qt ) is sampled by letting (C0 , q0 ) undergo the forward
process. We construct the forward process for Ct and qt independently, so the
marginal transition kernel can be decomposed as:
q(Ct , qt | C0 , q0 ) = q(Ct | C0 ) q(qt | q0 ).

(A15)

Note that in the intermediate marginal distribution qt (Ct , qt ), the two variables are not independent since they are not in the equilibrium distribution.
(C),θ
(q),θ
Hence, both the sD,t model and the sD,t model take both Ct and qt into
their input. For qt in Eq. (A15), recall that it is led by the Brownian motion
on SO(3), whose marginal transition kernel is available in closed form:
q(qt | q0 ) = IG SO(3) (qt | q0 , σt2 ),

(A16)

which turns sampling qt straightforward following the above description to
sample an IG SO(3) . For Ct in Eq. (A15), it is sampled using Eq. (A20) detailed
in the next part.
(q),θ
Data-based loss for sD,t is still based on the denoising score-matching
loss Eq. (A3). The score function to be matched can be simplified as
∇qt log q(Ct , qt | C0 , q0 ) = ∇qt log q(qt | q0 ) from Eq. (A15). This q(qt | q0 )
is an IG SO(3) from Eq. (A16). Recalling the score function of IG SO(3) , the
data-based loss can then be written as:

(q),θ

sD,t (Ct , qt ) − ∇qt log p̃IG,σt2 (∥qt ∥)

.

(A17)

The function p̃IG,σ2 (∥q∥) is introduced in Eq. (A12). The sample (Ct , qt )
for evaluating this loss is drawn following Eq. (A15), which again amounts
to drawing qt following Eq. (A16) and Ct following Eq. (A20) below. The
(n)
(n)
data
required (C0 , q0 ) sample is drawn from the dataset {(CD,0 , qD,0 )}N
n=1 that
follows the equilibrium distribution of system D.
Diffusion Process on the Alpha-Carbon Coordinates
To match the diffusion choice for SO(3) in Eq. (A11), we also adopt the Brownian motion as the forward process in the Euclidean space for the alpha-carbon
coordinates:
r
dσt2
dBt .
(A18)
dCt =
dt
This coincides with the choice in noise-conditioned score network [35, 73].
(C),θ
The PIDP loss for sD,t from the FPE Eq. (A1) then becomes:
2

1 dσt2 
∂ (C),θ
(C),θ
(C),θ
∇ ∇ · sD,t (Ct , qt ) + ∇ sD,t (Ct , qt )
− sD,t (Ct , qt )
2 dt
∂t
(C),θ

+λ sD,0 (C0 , q0 ) + ∇C0 ED (C0 , q0 )/(kB T )

.

(A19)

The sample of (C0 , q0 ) to evaluate the loss is again drawn from relevant
(m)
(m)
structures {(CD,0 , qD,0 )}M
m=1 for protein D, and the sample of qt following

Eq. (A16). For the sample of Ct , it is drawn from the marginal transition kernel of the diffusion process in Eq. (A18), which is a Gaussian distribution thus
easy to draw:
q(Ct | C0 ) = N (Ct | C0 , σt2 I).

(A20)

(C),θ

Data-based loss for sD,t also follows Eq. (A3), where the required score
function is ∇Ct log q(Ct , qt | C0 , q0 ) = ∇Ct log q(Ct | C0 ) due to Eq. (A15),
which leads to:

(C),θ

sD,t (Ct , qt ) − ∇Ct log q(Ct | C0 )

.

(A21)
(n)

(n)

data
The sample of (C0 , q0 ) here is drawn from the dataset {(CD,0 , qD,0 )}N
n=1 that
follows the equilibrium distribution, and sample of (Ct , qt ) is drawn following
Eqs. (A16, A20) . If substituting Eq. (A20) and expressing the loss in terms
of the standard Gaussian sample ϵt ∼ N (0, I) following the style of Eq. (5),

(C),θ

then Eq. (A21) becomes: sD,t (C0 + σt ϵt , qt ) + σϵtt . Nevertheless, such a
reformulation does not easily apply to substitute qt due to the complexity of
IG SO(3) in Eq. (A16).
Structure Sampling Using DiG
To generate structure samples using DiG, we find rather than directly simulating the reverse SDE analogous to Eq. (3), it is better to simulate the equivalent
deterministic process defined by an ODE analogous to Eq. (7). The rationale
of the equivalent ODE is explained in Supplementary Sec. A.1.3. Following the
deduction there, the equivalent ODE for the diffusion processes in Eqs. (A11,
A18) can be derived as:
d

Ct
qt



1 dσt2
=−
2 dt

 (C),θ

sD,t (Ct ,qt )
(q),θ

sD,t (Ct ,qt )



dt = −

 (C),θ

sD,t (Ct ,qt )



(q),θ

sD,t (Ct ,qt )

dσt2 .

(A22)

The simulation on Ct is thus:
(C),θ
Cti−1 = Cti + (σt2i − σt2i−1 )sD,ti (Cti , qti ).

(A23)

The simulation on qt can be done similarly by qti−1 = qti + 12 (σt2i −
(q),θ
σt2i−1 )sD,ti (Cti , qti ). This discretization on so(3) is equivalent to discretization on SO(3) in the sense that their one-step difference is o(ti − ti−1 ), but
the simulation in so(3) directly faces the risk that the discretization error may
lead the q variable going out of the domain (i.e., ∥q∥ > π), as there is no
mechanism to guarantee the constraint. We therefore carry out the simulation

in SO(3) instead:
Qti−1 = Exp

1


(Q),θ
(σt2i − σt2i−1 )sD,ti (Cti , qti ) Qti ,

(A24)

(Q),θ

where Exp is the conventional matrix exponent, and sD,ti denotes the skew(q),θ

symmetric matrix by organizing the outputs of sD,ti in the same way as
converting Q and q Eq. (A10). Note that the matrix exponent of a skewsymmetric matrix is a rotation matrix, Eq. (A24) then guarantees Qti−1 ∈
SO(3) whenever Qti ∈ SO(3). Alg. 5 summarizes the sampling procedure.
Interpolation between Protein States Using DiG
The deterministic nature of the ODE Eq. (A22) establishes a deterministic map
between a real state R0 and the corresponding latent state Rτ . This enables
(A)
(A)
(A)
the complicated interpolation between two given states, R0 = (C0 , q0 )
(B)
(B)
(B)
and R0 = (C0 , q0 ), by a simpler interpolation in the latent space of Rτ
(A)
where the distribution is simple. For the alpha-carbon coordinates C0 and
(B)
(A)
C0 , we apply linear interpolation to their corresponding latent states Cτ
(B)
and Cτ through the ODE, and then transform the line to the real-state space
of C0 by the ODE reversely. Since the coordinate distribution in the latent
space is standard Gaussian, which has a convex contour, linear interpolation
there would pass through high-probability regions. For the residue orientations
(A)
(B)
(A)
(B)
q0 and q0 , as the corresponding latent states qτ and qτ lie in the
product space of so(3) which is non-Euclidean, we leverage spherical linear
interpolation which gives the geodesic in so(3) between two given end states, in
place of the linear interpolation which is the geodesic in the Euclidean space.
Explicitly, the interpolation curves in the latent space are:
(A)
C(η)
+ ηCτ(B) ,
τ = (1 − η)Cτ

(A25)

(B) (A) −1 η (A)
q(η)
) qτ ,
τ = (qτ (qτ )

(A26)

where η ∈ [0, 1] parameterizes the interpolation curve. Subsequently,
(η)
(η)
(Cτ , qτ ) in Eqs. (A25, A26) are taken as the starting state to simulate the
ODEs Eqs. (A23, A24) reversely to generate the interpolated structures at
the parameter η along the transition pathway between state A and B.

A.2.2

Model Specification

Following the practice of AlphaFold [1], we use amino acid sequences as the
molecular descriptor D for proteins. To process the sequence to generate informative abstract representations for the feed into DiG, we follow the data
processing method in the training stage of AlphaFold and leverage the pretrained Evoformer to produce node and pair representations. Conditioned on
representations of proteins, DiG aims to gradually transform random noise

to reasonable protein structures following the equilibrium distribution. Considering that protein simulation trajectories that are long enough and reach
equilibrium distribution are very rare, for protein conformation sampling, as
in Sec. 2, we pre-train DiG with PIDP first, and then further improved the
performance by training the model with a small amount of simulation data.
Algorithm 1 Protein score model PIDP training (single step)
Require: Score model sθD,t (R) to be trained, boundary loss weight λ, randomly sampled system D, full-atom energy function ED for system D, a
(m)
randomly sampled relevant full-atom protein structure R̄D,0 for system D,
randomly sampled time step t ∈ [0, τ ].
(m)
(m)
(m)
(m)
1: Construct RD,0 := (CD,0 , qD,0 ) from the sampled R̄D,0 ;
(m)

(m)

(m)

(m)

Compute the energy gradient ∇C ED (CD,0 , qD,0 ) and ∇q ED (CD,0 , qD,0 )
for the alpha-carbon coordinates and residue orientations, respectively,
from the full-atom energy function ED using Alg. 2;
(m)
(m)
(m)
(m)
3: Sample (CD,t , qD,t ) from (CD,0 , qD,0 ) using Eq. (A20) and Eq. (A16);
4: Evaluate the PIDP loss LPIDP as Eq. (A14) + Eq. (A19);
5: Update the model parameter θ by performing an optimization step on
LPIDP with respect to θ.

2:

Algorithm 2 Compute the energy gradient on orientations and coordinates
Require: Energy function E, full atom protein structure R̄ with I amino acid
residues.
1: Construct R := (C, Q) from R̄;
2: Compute the energy E = E(R̄);
3: for each residue ı in 1, · · · , I do
4:
Set Xı as the coordinates of all Nı atoms in the residue ı;
5:
Xı,rel := (Xı − Cı )Q⊤
ı (c.f. Eq. (A27));
PNı
6:
gCı := a=1
∇Xı,a E (c.f. Eq. (A28));
PNı
X⊤
7:
gqı := a=1
ı,rel,a ∇qı Qı ∇Xı,a E (c.f. Eq. (A29));
8: end for
I
I
9: Return ∇C E := {gCı }ı=1 and ∇q E := {gqı }ı=1 .
We first train DiG by minimizing a PIDP loss that aligns the score model
with the gradients of the energy function and enforces the boundary conditions.
Alg. 1 outlines the training process. The PIDP training requires the energy
gradient label. This is facilitated by an energy function from OpenMM [74] at
the full-atom level. But as we are adopting a coarse-grained representation for
proteins, so the energy gradients w.r.t alpha carbon coordinates and residue

Algorithm 3 Estimate ∇(∇ · sθD,t (Rt )) by Hutchinson’s trace estimator
Require: Score model sθD,t (R), protein structure Rt , number of random
vectors Nest .
 (n) Nest i.i.d.
∼
1: Sample Nest random vectors of the same dimension as R: v
n=1
Rademacher(0.5);
PNest
(n) ⊤
2: g := N
∇Rt (sθD,t (Rt )⊤ v(n) ));
n=1 ∇Rt (v
est
θ
3: Return g as an approximation to ∇(∇ · sD,t (Rt )).
orientations are expected. For this, we leverage the rigid-body assumption and
the chain rule to derive the conversion, as shown in Alg. 2.
Here we briefly explain the derivation in Alg. 2. The rigid-body assumption states that for each residue ı with Nı atoms, the relative coordinates
Xı,rel ∈ RNı ×3 of all its atoms w.r.t its alpha-carbon at Cı ∈ R1×3 in a
standard coordinate system is fixed. Under this assumption, if the coarsegrained representation of this residue is (Cı , Qı ) where Qı is the orientation
of the residue relative to the standard coordinate system, then the absolute
coordinates of these atoms are:
Xı = Cı + Xı,rel Qı ,

(A27)

and if considering a protein with I residues, the full-atom coordinates are
R̄ := {Cı + Xı,rel Qı }Iı=1 . So in this way, we can convert the full-atom energy
function E(R̄) = E({Xı }Iı=1 ) as a function of the coarse-grained coordinates
R = (C, Q) using Eq. (A27). The gradient w.r.t Cı is then:
gCı := ∇Cı E = (∇Cı Xı )⊤ ∇Xı E =

Nı
X

∇Xı,a E,

(A28)

a=1
∂X

where (∇Cı Xı )aµ,ν := ∂Cı,a,µ
is the Jacobian matrix (here µ, ν ∈ {1, 2, 3}
ı,ν
indices the spacial dimension), and the last equality holds since the Jacobian
is (∇Cı Xı )aµ,ν = δµν meaning that this matrix element is one if µ = ν or it is
zero.
As for the gradient w.r.t the orientation, the so(3) representation denoted
as q is finally required. The conversion from q and Q is given by Eq. (A10).
Together with the rigid-body assumption Eq. (A27), the gradient is:
gqı := ∇qı E = (∇qı Xı )⊤ ∇Xı E = (∇Qı Xı ∇qı Qı )⊤ ∇Xı E
=

Nı
X
a=1

X⊤
ı,rel,a ∇qı Qı ∇Xı,a E,

(A29)

Algorithm 4 Protein score model data-based training (single step)
Require: Score model sθD,t (R) to be trained, randomly sampled system D, a
(n)

(n)

(n)

randomly sampled coarse-grained protein structure RD,0 = (CD,0 , qD,0 )
from the MD simulation data for system D, randomly sampled time step
t ∈ [0, τ ].
(n)
(n)
(n)
(n)
1: Sample (CD,t , qD,t ) from (CD,0 , qD,0 ) using Eq. (A20) and Eq. (A16);
2: Evaluate the data-based loss Ldata as Eq. (A17) + Eq. (A21);
3: Update the model parameter θ by performing an optimization step on
Ldata with respect to θ.

PNı

∂Qı
⊤
a=1 Xı,rel,a ∂qı,γ ∇Xı,a E, where γ ∈
∂Qı
{1, 2, 3} indices one of the three dimensions of qı , and ∂q
is the 3 × 3 matrix
ı,γ

where the last term means (gqı )γ =

composed of the partial derivatives from Eq. (A10). In the equation, again
∇qı Xı , ∇Qı Xı and ∇qı Qı are Jacobian matrices, and the second last equality
holds due to the chain rule of differentiation. From the rigid-body assumption
∂X
′
Eq. (A27), (∇Qı Xı )aν ′ ,µν = ∂Qı,a,ν
= Xı,rel,a,µ δνν ′ , so:
ı,µ,ν
[(∇Qı Xı ∇qı Qı )⊤ ∇Xı E]γ =

X

(∇Qı Xı )aν ′ ,µν (∇qı Qı )µν,γ (∇Xı E)aν ′

a,ν ′ ,µ,ν

=

X

Xı,rel,a,µ (∇qı Qı )µν,γ (∇Xı E)aν =

a,µ,ν

X
a

X⊤
ı,rel,a

∂Qı
∇Xı ,a E,
∂qı,γ

which gives the last equality.
Moreover, to avoid costly divergence evaluation, we use Hutchinson’s
trace estimator in Alg. 3 to handle ∇(∇ · sθD,t (Rt )) (recall that sθD,t (Rt ) =
(C),θ

(q),θ

(sD,t (Ct , qt ), sD,t (Ct , qt ))) in Eqs. (A14, A19) .
Optimizing PIDP from random initialization of the deep learning model
is extremely hard due to the complex landscapes of the training objectives
in Eqs. (A14, A19) . Therefore, a good initialization of the model and some
training techniques are necessary to stabilize the optimization of PIDP. To this
end, before performing PIDP, we train DiG on the experimental structures
and use it as a more stable initialization for PIDP. See Supplementary Sec. C
for more details.
Next, we pick about 1000 protein complexes in PDBbind database [75],
and simulate them with GROMACS, together with about 200 proteins in
GPCRmd [76] dataset to perform DiG training with simulation data (See
more details in Supplementary Sec. D.1). We further train the score model
pre-trained by PIDP by minimizing a score matching loss from Eq. (5) that
directly supervises the score model with the empirical data distribution that
(n)
approximates the equilibrium distribution, using protein structures RD,0 for
each system D. See Supplementary Sec. B and C for more details on the model
and training.

Algorithm 5 Protein structure sampling
Require: A trained score model sθD,t (R), target protein system D.
1: Initialize random structure Rτ := (Cτ , qτ ), where Cτ ∼ N (0, στ I), and
qτ ∼ pUnif on so(3) defined in Eq. (A13). tN := τ .
2: for i in N, · · · , 1 do
3:
ti−1 := i−1
N τ;
(C),θ
4:
Cti−1 := Cti + 12 (σt2i − σt2i−1 )sD,ti (Cti , qti ) (c.f. Eq. (A23));
5:

(Q),θ

(q),θ

Construct Qti from qti , and sD,ti (Cti , qti ) from sD,ti (Cti , qti ), using
Eq. (A10);


(Q),θ

Qti−1 := Exp 12 (σt2i − σt2i−1 )sD,ti (Cti , qti ) Qti (c.f. Eq. (A24));
7: end for
8: Return the sampled structure R0 := (C0 , q0 ).

6:

After training, amino acid sequences serve as input descriptors, denoted
as D, for sampling protein conformations via DiG. During the sampling
procedure, an initial random structure is generated, which subsequently is
transformed into a physically plausible conformation, as shown in Alg. 5.

A.3

Ligand Structure Sampling around Binding Sites

In contrast to the coarse-grained representation employed in protein conformation sampling, we train DiG of ligand structure sampling with all-atom (except
hydrogens) representations, which offer a more precise description of atomic
interactions between the binding site (pocket) and ligand during the sampling
of ligand-binding structures with proteins. However, the time complexity and
memory usage associated with attention layers in Transformer-based architectures exhibit a quadratic increase with respect to the number of input nodes.
This becomes impractical when the atom count surpasses one thousand. Consequently, we restrict our model to incorporate only the atoms of the ligand and
the protein atoms in close proximity to the pocket, using a distance threshold.
This threshold is set to 10 Å for the side length.
DiG defines a distribution over the vector space R̄ := (R̄Rec , R̄Lig ), where
R̄Rec and R̄Lig are the absolute coordinates of the near-site receptor and ligand
atoms, respectively. Since the receptor atom coordinates may have different distribution centers for different proteins while the diffusion process always starts
from a zero-centered Gaussian, we use the near-site receptor atom coordinates
R̄⋆Rec from the crystal structure of the protein in the PDBBind database [75]
as a reference structure, and let the model predict the residue. This effectively
shifts the diffusion process to R := (R̄Rec − R̄⋆Rec , R̄Lig ). DiG then generates
the binding structures for the ligand and the protein pocket by reversing the
diffusion process, as shown in Eq. (3).
To train DiG, we reuse the simulation data of protein complexes in
PDBbind, as detailed in Supplementary Sec. C. The data preprocessing and
featurization follows [77, 78]. The atom representations are further embedded

into real-valued embedding vectors for a Graphormer [2]. In this context, performing PIDP is not feasible due to limitations imposed by the energy function.
Specifically, DiG only considers atoms surrounding the binding site, while conventional force fields necessitate the inclusion of all atoms. As such, we sought
to enhance ligand sampling performance within the pocket by conducting a
pre-training task focused on binding structure prediction, utilizing the CrossDocked dataset [79]. Further information regarding model architecture and
training can be found in Supplementary Sec. B and C.

A.4

Catalyst-Adsorbate Sampling

For catalyst-adsorbate sampling, DiG adopts the same input representation
strategy employed in the OC20 dataset [10], employing the descriptor D to
characterize the system. Specifically, besides the atom types Z, also provided
from the OC20 dataset are the absolute coordinates R̄⋆base for non-surface catalyst atoms, R̄⋆Cat for surface catalyst atoms, and the initial absolute coordinates
R̄⋆Ad for adsorbate atoms prior to relaxation. Consequently, the system descriptor for this task was defined as D := (Z, R̄⋆base , R̄⋆Cat , R̄⋆Ad ). The microscopic
state of the system R̄ := (R̄Cat , R̄Ad ) encompasses the absolute coordinates
R̄Cat of surface catalyst atoms and R̄Ad of the adsorbate atoms. Similar to
the ligand-receptor sampling case, to ease the prediction of different distribution centers for different systems, we leverage the absolute coordinates in the
descriptor to define the diffusion-process variable as relative coordinates, i.e.,
R := (RCat , RAd ) where RCat := R̄Cat − R̄⋆Cat and RAd := R̄Ad − R̄⋆Ad , whose
distribution center is largely aligned across different systems.
During the reverse diffusion process, including the initial structure R̄⋆Ad
into the model input is found crucial for stable training. In the Graphormer
model, in addition to the diffusion-variable R in the input, the initial structure
R̄⋆Ad is also encoded as an additional structural attention bias term, as in [80].
More specifically, the pairwise distance between atoms in R̄⋆Ad was calculated,
which is then encoded into a K-dimensional feature using K radial basis function (RBF) kernels with learnable means and variances. Likewise, the initial
positions of the atoms are encoded as extra node features and incorporated into
the node representation. By summing the pairwise features and aggregating
them with the node features, per-atom features are updated and projected into
the atom embedding dimension within the model. Further details regarding
the structural attention bias can be found in Supplementary Sec. B.3.
Catalyst systems in OC20 are inorganic and lack bond information between
atoms. However, adsorbates are organic, and the bonds between atoms in
adsorbates can benefit the model in generating more physically accurate adsorbate structures. Consequently, we explicitly incorporated the 2D topology of
adsorbates, featuring bonds connecting the atoms, within the model. Bonds
are generated using the initial structure of the adsorbate and encoded in the
same manner as Graphormer [2]. The spatial encoding, centrality encoding,
and edge encoding of Graphormer are utilized alongside the encodings derived
from 3D information. It is important to note that, in some instances, bonds

in adsorbates may break upon adsorption to the catalyst surface. Explicitly
encoding bond information does not imply the enforcement of bonded atoms
to remain close in the sampled structures. Instead, the model is allowed to
learn when to separate two bonded atoms.
The training and sampling of DiG adhere to the general description in
the main text (Sec. 2). The training loss is based on Eq. (A6), and Alg. 6
shows the detailed training process. For sampling new structures using DiG,
in accordance with the training process, it is also conducted on the relative
coordinates w.r.t the initial structure. Alg. 7 outlines the sampling process.
Algorithm 6 Catalyst-adsorbate score model training (single step)
Require: Noise-predicting model ϵθD,t (R) to be trained, randomly sampled
time step t ∈ [0, τ ], randomly sampled system
with descriptor D =

(Z, R̄⋆base , R̄⋆Cat , R̄⋆Ad ), let R̄⋆ := R̄⋆Cat , R̄⋆Ad , randomly sampled catalyst(n)
(n)
(n)
adsorbent structure R̄D,0 = (R̄D,Cat,0 , R̄D,Ad,0 ) from the MD simulation
data for this system D.
(n)
(n)
⋆
1: Let RD,0 := R̄D,0 − R̄ ;
(n)

Sample noise variable ϵt ∼ N (0, I) in the same dimension as RD,0 ;
p
(n)
(n)
3: RD,t := αt RD,0 +
1 − αt2 ϵt (c.f. Eq. (A4));

2:

(n)

Evaluate the loss ϵθD,t (RD,t + R̄⋆ ) − ϵt (c.f. Eq. (A6));
5: Update the model parameter θ by performing an optimization step on the
loss with respect to θ.

4:

Algorithm 7 Catalyst-adsorbate structure sampling
Require: A trained noise-predicting model ϵθD,t (R), the descriptor D =

(Z, R̄⋆base , R̄⋆Cat , R̄⋆Ad ) of the target system, let R̄⋆ := R̄⋆Cat , R̄⋆Ad .
1: Sample a noisy structure Rτ ∼ psimple = N (0, I);
2: for i in N, · · · , 1 do
3:
ti−1 := i−1
N τ;
Qi p
τ
4:
Let βi := N
βti , αi := j=1 1 − βj ;
5:
Sample a noisevariable ϵti ∼ N (0, βi I) in the
 same dimension as Rti ;
β
θ
⋆
i
R ti − √
6:
Rti−1 := √
ϵ
(Rti + R̄ ) + ϵti (c.f. Eqs. (3, A5));
2 D,ti
1−βi

1−αi

end for
⋆
8: Return R0 + R̄ .
7:

As catalysts are periodic systems along the x and y directions, DiG expands
the unit cell in these dimensions before feeding a system into the model. Providing an exact descriptor of the infinitely repeated system in the model is
non-trivial; instead, DiG adopts a simple yet effective approach by establishing

a local cutoff for the infinitely repeating system. Specifically, an atom outside
the unit cell is included in the model only if its distance to any atom inside
the unit cell is within a threshold. A distance threshold of 6 Å is used in the
experiments. In each layer of the transformer model, the representation of a
repeated atom outside the unit cell is enforced to be identical to the representation of the corresponding atom in the unit cell. More details about handling
periodic boundary conditions can be found in Supplementary Sec. B.5.
Lastly, to ensure a good initialization for the diffusion model, a model pretrained on the IS2RS task of OC20 is used to initialize the weights, except for
the time step embedding, which is dedicated to the diffusion task.

A.5

Property-Guided Structure Generation

For modeling carbon polymorphs, the structural variable needs to represent
the unit cell which defines a spatial period in the crystal, and the absolute
coordinates X̄ of the carbon atoms in the unit cell. The unit cell is a parallelepiped to guarantee periodicity, so it can be determined by the coordinates
of 4 non-coplanar vertices, say c̄0 , c̄0 + l̄x , c̄0 + l̄y , and c̄0 + l̄z , where c̄0 is
the origin of the unit cell, and L̄ := {l̄x , l̄y , lz } are known as the lattice vectors. (The locations of the other 4 vertices can be determined as c̄0 + l̄x + l̄y ,
c̄0 + l̄x + l̄z , c̄0 + l̄y + l̄z , and c̄0 + l̄x + l̄y + l̄z .) In the structure representation,
the origin c̄0 is fixed as 0, so the unit cell is fully determined by the lattice
vectors L̄.
Similar to the cases of protein-ligand sampling in Supplementary Sec. A.3
and catalyst-adsorbate sampling in Supplementary Sec. A.4, we take the
diffusion-process variable R as relative coordinates to release the burden of
the diffusion model to also predict the distribution center for different systems. For the lattice vectors, we introduce a reference lattice vector set L̄⋆
taken as the mean lattice vector set on the dataset, and diffuse the relative
vectors L := L̄ − L̄⋆ . For the carbon-atom coordinates, we use their relative coordinates w.r.t the unit cell center z̄ := 12 (l̄x + l̄y + l̄z ), which means
X := X̄ − z̄. The diffusion-process variable is then defined as R := (X, L).
The diffusion-variable part of the input to the diffusion model still requires
the corresponding absolute coordinates (X, L) of R. For the descriptor part of
the input, in addition to the number of carbon atoms Natom , we also include
the reference lattice vectors L̄⋆ , which is an informative feature similar to the
discussion in Supplementary Sec. A.4.
The DiG model first learns the (unconditional) distribution of the structures of carbon polymorphs from a dataset created by random structure search
(RSS). We take the noise-prediction form to learn the model (c.f. Eq. (A5)).
The training process is detailed in Alg. 8. The DiG model is then asked to
generate structure samples conditioned on a given property value, specifically
a desired band gap value c in our case. According to Eq. (8), this requires
a property predictor/classifier. For this, we use a GNN model M3GNet [11],
which provides the prediction for the band gap of a given structure in absolute coordinates. To evaluate a probability, we convert the regression task

into a classification task by discretizing an inclusive range of the band gap
value into K intervals of length 1.0, represented by I0 = [a0 , b0 ], · · · , IK−1 =
[aK−1 , bK−1 ]. The property c is then taken as the bin index. Using the predicted band gap value from M3GNet, we define the probability of a given c
as:

c
exp − M3GNet(X̄, L̄) − ac +b
qD (c | X̄, L̄) := PK−1
(A30)
.
ak +bk
k=0 exp − M3GNet(X̄, L̄) −
This equation is used to construct the required conditional score sθD,t (X̄t , L̄t |
c
c) following Eq. (8). The value ac +b
is the target band gap for the interval Ic .
Algorithm 8 Carbon structure score model training (single step)
Require: Noise-predicting model ϵθD,t (X̄, L̄) to be trained, descriptor D =
(Natom , L̄⋆ ), where Natom is the number of carbon atoms, and L̄⋆ =
{l̄⋆x , l̄⋆y , l̄⋆z } is the reference lattice vectors; randomly sampled time step
(n)

(n)

t ∈ [0, τ ], randomly sampled structure (X̄D,0 , L̄D,0 ) from the dataset,
(n)

(n)

where X̄D,0 comprises coordinates of carbon atoms, and L̄D,0

=

4:

(n)
(n)
(n)
{l̄D,0,x , l̄D,0,y , l̄D,0,z } is the collection of lattice vectors.
(n)
(n)
(n)
(n)
Calculate the unit cell center z̄D,0 := 12 (l̄D,0,x + l̄D,0,y + l̄D,0,z );
(n)
(n)
(n)
(n)
(n)
Let XD,0 := X̄D,0 − z̄D,0 , LD,0 := L̄D,0 − L̄⋆ ;
(L)
(X)
Sample the noise variable ϵt ∼ N (0, I3Natom ) and ϵt ∼ N (0, I9 );
p
p
(n)
(n)
(n)
(n)
(X)
(L)
Let XD,t := αt XD,0 + 1 − αt2 ϵt , and LD,t := αt LD,0 + 1 − αt2 ϵt

5:

(c.f. Eq. (A4));
(n)
(n)
(n)
(n)
(n)
Let L̄D,t := LD,t + L̄⋆ which is structured as {l̄D,t,x , l̄D,t,y , l̄D,t,z };

6:

Let z̄D,t := 12 (l̄D,t,x + l̄D,t,y + l̄D,t,z ) and X̄D,t := XD,t + z̄D,t ;

1:
2:
3:

(n)

(n)

(n)

(n)

(n)

(n)

(n)

(X)

(L)

(n)

(n)

Evaluate the loss ϵθD,t (X̄D,t , L̄D,t ) − (ϵt , ϵt ) (c.f. Eq. (A6));
8: Update the model parameter θ by performing an optimization step on the
loss with respect to θ.

7:

The sampling process starts from a standard-Gaussian sample as R, and
in each step R is converted to absolute coordinates using L̄⋆ and the corresponding unit cell center for the input to the model, and finally outputs
the structure sample in absolute coordinates. Similar to the case of protein
structure sampling as explained at the end of Supplementary Sec. A.2.1, for
simulating the sampling process, instead of simulating the SDE in the fashion
of Eq. (3), it achieves better results to simulate the equivalent ODE in Eq. (7).
This is explained in Supplementary Sec. A.1.3. Under discretization, Eq. (7)

Algorithm 9 Sampling for carbon structure inverse design
Require: A trained noise-predicting model ϵθD,t (X̄, L̄) which decomposes as
(X),θ

(L),θ

(ϵD,t , ϵD,t ) according to its output channels, descriptor D = (Natom , L̄⋆ )
of the target system, where Natom is the number of carbon atoms, and
L̄⋆ = {l̄⋆x , l̄⋆y , l̄⋆z } is the reference lattice vectors; a trained property classifier
qD (c | X̄, L̄), the desired property value c, guidance strength λguide .
1: Sample a noisy initial structure Xτ ∼ N (0, I3Natom ), Lτ ∼ N (0, I9 );
2: for i in N, · · · , 1 do
3:
ti−1 := i−1
N τ;
4:
Let L̄ti := Lti + L̄⋆ which is structured as {l̄ti ,x , l̄ti ,y , l̄ti ,z };
5:
Calculate the unit cell center z̄ti := 21 (l̄ti ,x + l̄ti ,y + l̄ti ,z );
atom
6:
Let X̄ti := Xti + z̄ti which is structured as {X̄ti ,a }N
a=1 ;
Qi p
τ
7:
Let βi := N βti , αi := j=1 1 − βj ;
√
(X),θ
8:
Xti−1
:=
(2 −
1 − βi )Xti − √βi 2 ϵD,t (X̄ti , L̄ti ) +

1−αi

i

λguide β2i ∇X̄ti log qD (c | X̄ti , L̄ti ) (c.f. Eqs. (A31, A5, 8));
√
√βi ϵ(L),θ (X̄ti , L̄ti ) +
1 − βi )Lti −
9:
Lti−1
=
(2 −
2 1−α2i D,ti

PNatom
λguide β2i ∇L̄ti log qD (c | X̄ti , L̄ti ) + 12 a=1
∇X̄ti ,a log qD (c | X̄ti , L̄ti )
(c.f. Eqs. (A31, A5, 8));
10: end for
⋆
11: Let L̄0 := L0 + L̄ which is structured as {l̄0,x , l̄0,y , l̄0,z };
12: Calculate the unit cell center z̄0 := 2 (l̄0,x + l̄0,y + l̄0,z );
13: Let X̄0 := X0 + z̄0 ;
14: Return (X̄0 , L̄0 ).
is written as:
Rti−1 = Rti +


βi 
Rti + sθD,ti (R̄ti | c) ,

where h is the discretization step size, R̄t := (X̄t , L̄t ) is the absolute coordinates corresponding to Rt , and the plus sign is due to the simulation is reversed
in time. Also recall βi := hβti . Since h hence βi is an infinitesimal,
√ the weight
for the Rti term can be formulated as: 1+ β2i = 2−(1− β2i ) = 2− 1 − βi +o(h),
which gives an alternative up to o(h) which is acceptable since the disretization itself has o(h) error. This then recovers the ODE simulation in [35]. By
leveraging Eq. (8), the simulation step becomes:
Rti−1 = (2 −


p
βi  θ
1 − βi )Rti +
sD,ti (R̄ti ) + ∇Rti log qD (c | R̄ti ) ,

where qD (c | R̄ti ) is given by Eq. (A30). Finally, by involing Eq. (A5), we can
express the generation process using the noise-prediction model ϵθD,t :
Rti−1 = (2 −

p

βi
βi
ϵθD,ti (R̄ti ) + ∇Rti log qD (c | R̄ti ).
1 − βi )Rti − p
2 1 − αi2
(A31)

Note that the input to the qD (c | R̄ti ) model is absolute coordinates while the
gradient is taken w.r.t the relative coordinates Rti . To conduct this conversion,
note that the conversion is L̄ = L + L̄⋆ , and X̄ = X + z̄ where z̄ := 12 (l̄x + l̄y +
l̄z ) with L̄ = {l̄x , l̄y , l̄z }. So ∇X log qD (c | X̄, L̄) = ∇X̄ log qD (c | X̄, L̄), and
PNatom
∇L log qD (c | X̄, L̄) = ∇L̄ log qD (c | X̄, L̄) + 12 a=1
∇X̄a log qD (c | X̄, L̄).
In practice, the strength of the property guidance can be tuned for better
performance, as is a common practice in machine learning [81]. We hence
introduce a λguide parameter. Alg. 9 details the sampling process.
It is important to note that, in the conditional generation, the classifier
can be fully decoupled from the training of the diffusion model. As a result,
our model can serve to generate any demanded properties when provided
with a corresponding property prediction model. This flexibility allows the
approach to be adapted for various applications and desired properties, given
an appropriate predictive model.

A.6

Accelerating Inference

The inference procedure of DiG can be viewed as gradually removing the
noise from Gaussian random variables to sample clear conformations in an
approximated equilibrium distribution. Although it exhibits several orders of
magnitude speedup for the cases in Sec. 3 compared to traditional simulation
methods, the inference is still potentially expensive since it generally needs to
go over all time steps. Fortunately, the inference time can be further saved
with recently developed methods [82–86]. For example, Ref. [84] shows that the
analytic solution of the diffusion ordinary differential equations (sampling of
DiG can be alternatively viewed as solving the corresponding diffusion ordinary
differential equations) can significantly accelerate the inference, where highquality samples can be drawn in around 10 steps, resulting in a further 50
to 100 folds speedup. These recent advances demonstrate the potential for
even more efficient inference procedures in the context of DiG and similar
models. By combining these methods with the existing framework, it becomes
increasingly feasible to generate desired structures with specific properties in
a faster and more efficient manner.

A.7

Evaluation methods

Protein Conformation Sampling
As detailed in Sec. 3.1, this study aims to demonstrate the applicability of using
the DiG method to sample protein distributions. To this end, simulations of

two proteins from the SARS-CoV-2 virus are used to approximate their actual
distributions in equilibrium states. The molecular dynamics (MD) simulation
trajectories of the receptor-binding domain (RBD) of the spike protein and the
main protease are extracted from a public dataset2 . For RBD, there are 2995
independent MD simulations with 1.8 ms of aggregate simulation time. For
main protease, the aggregated simulation time is 2.6 ms from 5688 independent
trajectories. Both sets of simulations are performed in the constant pressure
and temperature (NPT) conditions at 310 K and 1 atm pressure.
To facilitate the comparison between distributions obtained from MD simulations and DiG generations, time-lagged independent component analysis
(TICA) is utilized to project the simulated structures onto a low-dimensional
manifold [87, 88]. This projection enables the visualization of the conformational distribution in the low-dimension space, such as the one spanned by the
two TICA coordinates (Fig. 2a). The TICA projection analysis is carried out
as the following: first, the backbone conformation is featurized with the cosine
and sine values of backbone torsion angles; then standard TICA projection is
executed using PyEmma [89], with lag times of 10 ns and 2 ns for RBD and
main protease respectively. We first parametrized the TICA transformation
matrix to MD simulation structures to obtain the probability distribution as
references, then the same transformation is applied to structures generated by
DiG. From MD simulation trajectories, about 1.8 million structures of each
system are used for TICA analysis. Furthermore, to reduce the influence of
disordered regions at protein termini, the terminal residues are excluded during this TICA analysis and projection to the low-dimensional conformational
space. For the distribution comparison in the reduced 2D space, we focus on
the populated regions, which correspond to metastable states. The regions
with very low probability in the distribution map are not included for detailed
comparison, in order to focus on the functional relevant conformations.
For a further comparative analysis between DiG and atomistic MD simulation, representative structures for both proteins are obtained from MD
simulations by clustering analysis. Initially, cluster centroid coordinates of all
dominant meta-stable clusters in the 2D TICA space (Fig. 2a) are estimated
for each protein. Following this, 1000 MD simulated structures near cluster
centroids are sampled for each structure cluster. The first 16 TICA components
of these structures are used as features to cluster the simulation structures
into 4 sub-clusters using the K-Means algorithm. Finally, the centroid structure of the largest sub-cluster was extracted by MDTraj [90] and taken as the
representative structure of the respective meta-stable state.
In order to assess the degree of conformity of the distributions, we compute
quantitative metrics on the 2D TICA space. Particularly, we devise a G×G grid
to uniformly cover the populated regions of the 2D TICA space, wherein the
grid is labelled as positive if there exists at least one simulation structure within
the corresponding TICA range. This grid is referred to as the “groundtruth”

https://covid.molssi.org/simulations/

grid. With structures sampled by DiG or other sampling methods, we can
construct a similar “sampled” grid following the same procedure.
In the coverage analysis in Supplementary Sec. E, we employ four distinct
types of metrics, namely:
TP + TN
,
TP + FP + TN + FN
TP
,
Precision =
TP + FP
TP
,
Recall =
TP + FN
2 × Precision × Recall
.
F1 =
Precision + Recall

Accuracy =

In the above equations, the grid labelled as the “groundtruth” is considered
to be true, whereas the one labelled as “sampled” is considered to be predicted.
The values TP, FP, TN, and FN represent the values of true positives, false
positives, true negatives, and false negatives, respectively.
To quantitatively assess the similarity of structures to their reference
conformations, we employ two metrics: the template modeling score (TMscore) [91] and the root mean square deviation (RMSD). TM-score is a
normalized measure of structural similarity between two conformations, with
a score of 1 indicating a perfect match; and RMSD calculates the average distance between the paired atoms of two optimally superimposed structures. In
our evaluations, we restrict our RMSD calculations to the alpha carbon atoms
in protein structure comparison, and for all non-hydrogen atoms for ligand
structure comparison. These metrics provide a quantitative means of gauging
the accuracy of our protein conformation samples relative to their experimental
counterparts.
The quality of DiG-generated structures was assessed using the TM-scores,
by comparing each generated structure against crystal structures (6M0J for
RBD and 6LU7 for main protease). For RBD, the mean value of TM-score
is 0.84 and all structures have TM-score larger than 0.8, indicating highly
similar structures; while in the case of main protease, the TM-score is more
spread, with about 94% structures with TM-score > 0.5. We adopt a criterion
suggested by [92], using TM-score = 0.5 as a cutoff to remove the structures
that are dissimilar to the experimental model. For the downstream analysis,
such as structure distributions, only structures with TM-score > 0.5 are used
to reduce noises from incorrect predictions.
Catalyst-Adsorbate Sampling
After training the model to find different adsorption configurations, we traverse
the initial positions of the adsorbate by shifting the original initial structure of
adsorbate in the dataset along the x and y vectors of the unit cell. Specifically,
we equally divide the unit cell in x and y dimensions into a grid of 15 × 15

points. Without changing the conformation and height in the z dimension of
the initial structure of the adsorbate, we shift its coordinates in the x and y
dimensions to match these 15 × 15 points, thus creating 15 × 15 different initial
structures of the system. For each initial position, we use DiG to sample 10
structures. The sampled structures are then verified by DFT relaxation with
VASP [51]. In VASP, we allow both the catalyst surface and the adsorbate
to move, which is consistent with our model and the dataset. The structures
generated by our model are close to the relaxed structures, as described in
Sec. 3. For some initial positions, we are able to find multiple adsorption sites
within the 10 sampled structures. Fig. 4 shows such a case, where two of the
adsorption configurations are sampled from the same initial structure. Note
that the training dataset contains only very short MD trajectories. The capability of our model is also limited by the dataset. With longer MD trajectories
that traverse more structures, our model should be able to find more adsorption sites from an arbitrary initial structure. More discussions can be found in
Supplementary Sec. F.
The probability density map of DiG is generated with single-atom adsorbates. To plot the map of probability density, we equally divide the unit cell
along x and y dimensions as mentioned previously, resulting in a 20 × 20 grid.
We place the adsorbate above each grid point, creating 20 × 20 structures for
each fixed height of the adsorbate atom. We traverse 10 different heights for
the adsorbate atom, ranging from 0 Å to 1 Å from the surface of the catalyst.
Atoms in the catalyst surface are kept as the initial positions when density
evaluation. In total, we obtain 4000 structures. We calculate the log-likelihood
of our model on these structures, given an initial structure where the adsorbate atom is 2 Å from the catalyst surface above the center of the catalyst
surface in the unit cell. The equation below summarizes the calculation of the
probability density map:
p(xi , yj | x0 , y0 , z0 ) = max pmodel (xi , yj , zk | x0 , y0 , z0 ),
k

where i, j, k ∈ {1, · · · , 20}×{1, · · · , 20}×{1, · · · , 10}, z0 = 2 Å is distance from
the initial position of the atom to the highest point of the catalyst surface,
and (x0 , y0 ) is the center of the catalyst surface in the unit cell. Finally, in the
probability density map, we plot the log values of the probabilities above. In
the energy map from VASP, for each i, j we plot the negative of the energy of
the relaxed structure, with the xi , yj , and the catalyst surface fixed. Starting
from an initial height zk = 2 Å from the catalyst surface, we used DFT to
relax along the z dimension to obtain the minimum energy upon the grid point
(xi , yi ).
Property-Guided Structure Generation
To measure the ability of modeling the carbon polymorph structures, we
use the StructureMatcher in the Pymatgen [54] package to calculate the
ratio that a sampled structure matches a structure in the training dataset.

We use hyperparameters stol=0.5, angle tol=10 and ltol=0.3 for the
StructureMatcher, where stol is the tolerance for the displacement of atom
positions, angle tol controls the difference in lattice vector angles between
the matched structures, and ltol is the tolerance for the difference in matched
lengths of lattice vectors. The get rms dist method is used to calculate the
RMSD, which is normalized by the average free length per atom.

Appendix B
B.1

Model Details

Descriptors of Molecular Systems

We consider four types of molecular systems in previous sections: proteins,
protein-ligand, catalyst-adsorbate, and carbon polymorphs. A descriptor D is
used for each system that captures the relevant features of the molecular structure and can be processed by DiG. The descriptor D in the four systems is first
processed into node representations V describing the feature of each systemspecific individual element, and a pair representation P describing inter-node
features. Note that in some systems, the descriptor D also contains structural
features, which are treated as part of the node representation V. The {V, P}
representation is the direct input from the descriptor part to the Graphormer
model, as illustrated in Fig. 1.
For protein systems, we follow AlphaFold [1] and adopt a coarse-grained
representation that uses the position of the alpha-carbon atom and the orientation of each residue (see Supplementary Sec. A.2.1). The node representation
V is a sequence of feature vectors that are generated by the Evoformer module
in [1], which takes as input the amino acid sequence and the multiple-sequence
alignment (MSA) of the protein. The pair representation P is composed of two
matrices: the first represents all pairwise interactions between residues, which
is also produced by Evoformer, and the second represents the lengths of all
residue pairs on the amino acid sequence. The node and pair representations
are learnable embeddings in [1], but we hold them fixed in this work to avoid
additional computational cost from fine-tuning the Evoformer. See more discussions about the limitation of fixing parameters of Evoformer can be found
in Supplementary Sec. F.
For protein-ligand binding systems, we use an all-atom representation that
includes atoms from both the protein and the ligand. The features are obtained
following the method in [77]. To be specific, the node representation V for the
protein part consists of the types of atoms around the binding pocket and also
the positions of these atoms R̄⋆Rec in the crystal structure of the protein, and
the ligand part consists of a graph of the skeletal formula of the ligand. The
pair representation P is also composed of two parts: one for the intra-molecular
bonds and one for the inter-molecular interactions. The intra-molecular bonds
are represented by feature embeddings of the chemical bonds between the
atoms of the protein or the ligand, and the inter-molecular interactions are
represented by feature embeddings of interactions like the hydrogen bonding
between the protein and the ligand, as defined in [77].

For catalyst systems, we use an all-atomic representation that includes both
the catalyst surface and the adsorbates. The node representation V consists
of the types of atoms of the catalyst and adsorbed molecules as well as their
positions R̄⋆Cat , R̄⋆Ad in the initial structure from the OC20 dataset [10]. The
features of the nodes are only embeddings of the atomic type and position,
following the method in [80]. The pair representation P is only defined for
the adsorbates, which consists of feature embeddings of the chemical bonds
between the atoms of the adsorbates.
For carbon polymorphs, we use an all-atomic representation that only
includes carbon atoms. The node representation V consists of the initial embedding of the carbon element. The only difference among the systems is the
number of carbon atoms. There is no pair representation P for the carbon
polymorphs, as the chemical bonds are not pre-defined and may change during
the diffusion process.

B.2

Backbone Architecture

The deep learning models used in DiG are extended by our previously proposed
Graphormer [2, 80], which is a Transformer-based graph neural network [93],
and could efficiently capture the topological information while keep the powerful expressiveness from the Transformer architecture. The model is composed
of a few concatenated so-called attention layers and feed-forward layers. Each
attention layer takes the hidden node representation H as the input tokens of
the Transformer and uses the pair representation P as a learnable attention
bias for the attention mechanism. Formally, given a hidden node representation
H = {h1 , · · · , hI }, where I is the number of nodes, and a pair representation
P = {Pıȷ }Iı,ȷ=1 , where Pıȷ is the learnable embedding of the edge features from
node ı to node ȷ, Graphormer computes the attention score Aıȷ from node ı
to node ȷ as:

Aıȷ =

(hı W(Q) )(hȷ W(K) )⊤
(P)
√
+ P⊤
,
ıȷ w
d

(B32)

where W(Q) , W(K) are the “query” and “key” linear projections for the node
representation, w(P) is a learnable weight vector for the pair representation,
and d is the dimension of the query and key vectors. The hidden node repre(P)
sentation H in the first layer is V. The attention bias term P⊤
enables
ıȷ w
the model to learn the importance of the pair representation for the attention
mechanism. The attention score is then normalized by a softmax function over
all nodes and used to compute the attention output following the invariant
point attention mechanism in AlphaFold [1] for protein systems, or standard
Transformer architecture [93] for other molecular systems.

Algorithm 10 Equivariant Vector Prediction
Require: Node 3D positions {R1 , · · · , RI }, node representation H =
⊤ ⊤
[h⊤
∈ RI×C , attention bias Eattn ∈ RI×I ; linear projector
1 , · · · , hI ]
(Q)
matrices W , W(K) ∈ RC×d , W(V ) ∈ RC×C , w(F ) ∈ RC ;
rel
1: Calculate the relative positions E
∈ RI×I×3 : Erel
ıȷ := Rı − Rȷ ;
(Q)
(K)
2: Q = HW
, K = HW , V = HW(V ) ;
QK⊤
3: A = √
+ Eattn ;
d
PI
⊤
I×3
4: Calculate F ∈ R
: Fı := ȷ=1 softmax(Aı: )ȷ (w(F ) Vȷ )Erel
ıȷ ;
5: Return F;

B.3

Structural Attention Biases

Besides the descriptor D input of the molecular systems, the Graphormer
model also needs to process the geometric structure input R and produce
a physically finer structure. To more informatively encode the geometric
information during the diffusion process, we also introduce a structural representation for the input R, which is used to help Graphormer to capture
the spatial and rotational relationships among the nodes and refine the noisy
structures to more physically realistic ones.
For all molecular systems in full-atom representation, we follow [80] to
encode the Euclidean distance dıȷ between the positions of node ı and node ȷ
as a bias term bϕ (dıȷ ), where ϕ is a learnable parameter. The distance encoding
bias is added to the attention score in Eq. (B32) to modulate the attention
based on the distance between nodes. For protein systems that use the coarsegrained representation R = (C, Q) (see Supplementary Sec. A.2.1), we adopt
the invariant point attention mechanism in [1] to construct the corresponding
attention score, which has been shown to be indispensable for capturing the
local rotational invariance feature of the protein structures.

B.4

Equivariant Graphormer

Due to the score model interpretation (gradient of log-density function), the
output of the Graphormer model is required to be equivariant w.r.t the R
input, which requires a proper design for processing the R input. To ensure
the rotational equivariance of the Graphormer model, we add one equivariant
attention layer [80] as the 3D vector output head, which produces geometric
vectors that are equivariant to any rotation transformations in 3D Euclidean
space on the input, as detailed in Alg. 10. Specifically, we first compute the
⊤ ⊤
attention matrix A and the transformed invariant features H = [h⊤
1 , · · · , hI ]
as in the previous layers, and then the vector output is obtained by attentively aggregating the relative position information and the invariant features.
Since we only apply scalar multiplication and linear combination operations
on the vector features, the resulting vector F is naturally equivariant to the
SO(3) group of rotations. Moreover, F is translation-invariant because it only
depends on the relative positions between two nodes. This design strategy for

processing vector features is similar to those used in previous works on protein
modeling [94] and quantum chemistry [95].

B.5

Periodic Boundary Condition

In catalyst-adsorbate systems and carbon polymorphs, atoms in a 3D unit cell
are periodically repeated. Therefore, radius graphs with periodic boundary
conditions are constructed to represent the systems, where each atom in one
single cell (the centric cell) will connect with its neighboring atoms within a
pre-defined cutoff distance. Since atoms are periodically repeated, the same
atom in different cells may appear repeatedly in one graph as different nodes.
To avoid that the same atom has different node representations in the network,
typically a multi-graph will be constructed for message-passing neural networks
(MPNNs), where one node represents one atom, and multiple edges between
nodes represent the interactions with the same atom in different cells. In this
way, information on neighboring atoms will be aggregated by MPNNs with
multiple times through each edge.
Differently, message aggregation is done by attentively weighted sum on
full graph in Graphormer, and interactions between atoms are encoded into
spatial distance embeddings acting as attention bias. Multi-graph will lead to a
summation of multiple biases in the distance embedding space, which might be
projected to a new distance, and would not reflect multiple interactions with
the same atom in different cells. Therefore, to reflect the multiple interactions
correctly while enforce one representation for the same atom in different cells,
we use a cross-attention sub-layer to aggregate information from all atoms in
the radius graph into the atoms in the centric cell as shown in Alg. 11.
Algorithm 11 Handling Periodic Boundary Condition
I
Require: Atom positions in the centric unit cell Xe := {e
xı }ı=1 .
Require: Lattice vectors lx , ly , lnz . Cutoff distance
o Dcut .
eı ∈ Xe in current layer.
Require: Atom representation h(xeı ) | x
n
o
Ensure: Atom representation h′ (xeı ) | e
xı ∈ Xe after attention.
o
n
e + llx + mly + nlz | l, m, n ∈ Z, e
x ∈ Xe ;
1: X ← x
n
o
e′ ∈ Xe, ∥x − e
2: XD ← x ∈ X | ∃x
x′ ∥ ⩽ Dcut ;
e ∈ Xe, l, m, n ∈ Z;
3: ∀x ∈ XD , e
x := x + llx + mly + nlz , s.t. x
(Q)
(K) ⊤
(h(xeı )W )(√hȷ (xeȷ )W )
+ bϕ (∥xı − xȷ ∥) , ∀xı , xȷ ∈ XD ;
4: Aıȷ ←
d

P
′
5: h ( e
xı ) ← ȷ softmax(Aı: )ȷ h(xeȷ )W(V ) .

The basic idea is that learnable node embeddings are only assigned to
atoms in the centric cell, and the embeddings for the same atom appearing in
neighboring cells are its replicas. The attention bias encoded from pair-wise

atom distances is used to tell replicas of atoms in different cells. Therefore,
the representation of each node in the centric cell will be updated by the
correlation and interaction with all atoms in the radius graph.
In modeling the carbon polymorphs, with the lattice vectors, we can expand
the unit cell and handle periodic boundary conditions as described in Alg. 11.
However, we find that explicitly encoding the vertices in the unit cell as tokens
in the Graphormer encoder is very helpful for sampling physical structures.
Thus, each vertex of the unit cell is treated as an atom with a special type
in the model. In other words, for a structure with n atoms in the unit cell,
the model will take n + 8 tokens, and expand the tokens according to the
PBC handling method. Alg. 8 and 9 describe the details of the training and
sampling processes, respectively.

Appendix C
C.1

Training Details

Protein Conformation Sampling

Training Pipeline and Dataset
Our training process for the protein system consists of three stages: initialization, physics-informed diffusion pre-training (PIDP), and data-based training
using simulation data. In the first stage which aims to provide a good initialization to stabilize PIDP training, we collect all experimental structures from
the Protein Data Bank (PDB) [96] before December 25, 2020 as training data
and employ Alg. 4 for model training. Such experimental structures are widely
used in structure prediction methods, in which case a dataset is organized following the pattern (D, RD ), where each amino-acid sequence D is paired with
one experimental structure RD . In contrast, to provide distributional information during the training of DiG, we organize the structures to construct
a physical distribution dataset, in which each data point follows the pattern
(n)
data
(D, {RD }N
n=1 ) where each amino acid sequence D is paired with a set of
(n)
data
structures {RD }N
n=1 . To prepare this dataset, we adopt all the sequence identity clusters from PDB obtained by MMSeqs2 [97], and include all the available
experimental structures for each cluster. Following AlphaFold [1], we filter out
structures from PDB that have a resolution worse than 9 Å. This eliminates
about 0.2% of structures. For proteins longer than 256 amino acids, we divide
them into segments of length no longer than 256 amino acids. In each training step, we randomly draw clusters and structures within each drawn cluster
with equal probability. We would like to remark that although this physical
structure distribution is hard to verify to obey the equilibrium distribution, it
can still provide rich information about the different modes of the equilibrium
distribution.
In the second stage, to prepare the relevant structures for evaluating the
PIDP loss, we run short MD simulations for about 1000 proteins, for which
the details can be found in Supplementary Sec. D. We randomly pick 100
simulated structures for each protein as the relevant structures. The training

process follows Alg. 1. In the final stage, we use a simulation dataset consisting
of the above simulation dataset, and 238 simulation trajectories randomly
picked from the GPCRmd dataset [76]. The GPCRmd dataset contains short
simulations of various classes of G protein-coupled receptors (GPCRs). The
training process follows Alg. 4.

PIDP Training
(m)

As mentioned in the main text (Sec. 2), the structures {R0 }M
m=1 for evaluating the PIDP loss are ideally grid points (as in finite-element methods)
spanning the structure space, but this is unaffordable since the number of grid
points increases exponentially with the dimension of the space, which is typically exceedingly high for molecular systems. But we only need to supervise the
model on a low-dimensional manifold of physically relevant structures (with
low energy). Due to the grid point nature, these structures do not have to follow the equilibrium distribution, but only need to demonstrate the manifold.
This then enables a wide range of affordable methods to prepare such structures, such as perturbation around experimentally observed structures [98],
and short MD simulation structures. In practice, we found protein structures
perturbed by [98] lead to overly large energy gradient which hinders effective optimization and cannot be easily mitigated by e.g. gradient clipping (see
Supplementary Sec. F.2 for more details about the limitation of energy function). For this reason, we adopt structure samples from short MD simulation
trajectories for PIDP training. This is much cheaper than generating structures following equilibrium distribution by long enough MD simulations. The
short MD simulations provide structures that can be seen in a physical process
thus demonstrating the relevant manifold, and the information of equilibrium
distribution is provided by the energy function.
For evaluating the energy function (or its gradient, i.e., force field), we
use OpenMM to compute the full-atom force using the Amber force field as
−∇E(R̄), which also serves for calculating the coarse-grained forces −∇C E
and −∇q E through Alg. 2. We use PDBFixer [99] to fix the input protein
structure files before processed by OpenMM to avoid potential failures.
We find that the range of magnitude of the calculated forces varies drastically, which poses a significant challenge in optimizing the PIDP loss in Eq. (4).
We hence retain only the structures that have a force magnitude within the
smallest three orders of magnitude. To further address the optimization challenge, we also modify the loss terms for matching the score model at t = 0 to
the force field in Eqs. (A14, A19) by only matching their directions.
We also find that for loss terms for t > 0 (or i > 0) in the PIDP losses
Eqs. (A14, A19) , different sampling time steps t (or i) result in significant
differences in the scale of the loss, ranging from 0 to 1 × 106 . For stable and
(C)
effective training, we rescale and clip these losses. Specifically, with ℓt and
(Q)
ℓt denoting the PIDP loss terms at time step t of alpha-carbon coordinates
(C)
(Q)
and residue orientations, we find ℓt and ℓt increase exponentially with t,

Table C2: Hyperparameters of protein model. Different hyperparameters are
used in different stages.
Hyperparameter
Model depth
Hidden dim (Single)
Hidden dim (Pair)
Hidden dim (Feed Forward)
Number of Heads
Optimizer
Learning rate schedule
Peak Learning rate
Dropout p
Adam (β1 , β1 )
Adam ϵ
Weight decay
Warmup ratio
Batch size
Diffusion steps N
(C)
(C)
(σmin , σmax )
(Q)
(Q)
[σmin , σmax ]
Boundary weight λ1
Hutchinson Nest

Initialization

PIDP

Data Training

Adam
Inverse Square Root
1E-03
1E-05
1E-05
0.1
0.0
0.1
(0.9, 0.999)
(0.9, 0.999)
(0.9, 0.999)
1E-06
1E-06
1E-06
1E-02
1E-02
1E-02
0.06
0.06
0.06
(0.1, 35)
(0.1, 35)
(0.1, 35)
(0.02, 1.65)
(0.02, 1.65)
(0.02, 1.65)
-

with exponents ρ(C) and ρ(Q) . To avoid an excessively large loss, we scale these
(Q)
(Q)
(C)
(C)
losses by: ℓ̃t := ℓt /(ρ(C) )1−clip(t) , and ℓ̃t := ℓt /(ρ(Q) )1−clip(t) , where
clip(t) := min(0.05τ, t).
Furthermore, we find that a balanced combination of the losses in Eq. (A3)
and Eq. (4) is essential for generating more physical structures after PIDP
training.
These training methods, implemented to ensure more stable optimization,
may compromise the accuracy of the distribution learned by the model. These
limitations will be discussed further in Supplementary Sec. F.

Hyperparameter Choices
In protein training, we discretize the diffusion-process time variable t ∈ [0, τ ]
into i ∈ {0, 1, · · · , N } discrete time steps. The noise scales σi in Eq. (A11)
and Eq. (A18) (or in Algs. 1 and 4 for training, and Alg. 5 for sampling)
at the corresponding discretized time step ti are taken in the form σi =
(C)
(C)
(σmin )(1−ti /τ ) (σmax )ti /τ . The parameters σmin and σmax for the diffusion pro(Q)
(Q)
cess on alpha-carbon coordinates and σmin and σmax for the residue orientation
are detailed in Supplementary Tab. C2, together with all other hyperparameters. To strike a balance between computational efficiency and performance,
we train for at least one epoch at each stage and halt training when the rate
of loss reduction noticeably decelerates.

Table C3: Hyperparameters of protein-ligand binding model used in CrossDocked datasset and MD dataset training.

C.2

Hyperparameter

CrossDocked & MD Training

Model depth
Hidden dim (Model)
Hidden dim (Feed Forward)
Number of Heads
Optimizer
Peak learning rate
Warmup ratio
Learning rate schedule
Dropout p
Adam (β1 , β2 )
Adam ϵ
Weight decay
Batch size
Diffusion steps N
Diffusion β schedule
Diffusion β start
Diffusion β end
EMA decay
EMA fp32
Clip norm

Adam
0.0002
0.06
Linear Decay
0.1
(0.9, 0.98)
1E-08
0.0
Sigmoid
1E-07
0.02
0.9999
true
10.0

Ligand Structure Sampling around Binding Sites

Two-stage training was performed in ligand sampling. The first stage employs
CrossDocked [79] as a binding structure prediction task. The CrossDocked
dataset contains docked conformations of varying quality, so we filter out all
complexes whose RMSD between the docked and the experimental crystal
structures is larger than 2.5 Å. The second stage employs the simulation data
(Sec. D.1), where we set the threshold as 6 Å, and 1 ns as the sampling
stride. For data-based training, we collect data from CrossDocked [79] and
MD simulations to explore the most concerned part in the conformational
space. The CrossDocked dataset contains docked conformations of varying
quality, so we filter out all complexes whose RMSD between the docked and
the experimental crystal structures is larger than 2.5 Å. For MD simulation
data, we set the threshold as 6 Å, and 1 ns as the sampling stride. We conduct
a quality screening on the simulation data, by filtering out trajectories that
there are ligand’s atoms around the protein laying within 5 Å. After filtering,
the MD simulation dataset contains 1157 protein-ligand complex trajectories,
and we split 80% for training, 10% for evaluation, and 10% for testing. All
hyperparameters are listed in Supplementary Tab. C3.

C.3

Catalyst-Adsorbate Sampling

Our model captures the distribution of the structure of an adsorbate on a
catalyst surface. DiG predicts the distribution conditioned on an initial structure, which is the first frame in a relaxation trajectory provided in the OC20
dataset [10]. To train DiG, we use the MD part of the OC20 dataset following Alg. 6. 20,000 systems of the MD dataset are separated for validation.
Before this data-based training, the Graphormer model is first pretrained on
the IS2RS task of OC20. Detailed hyperparameters for the IS2RS pretraining are listed in Supplementary Tab. C4. In the data-based training, we use
a peak learning rate of 2 × 10−4 , maximum number of epochs 300, warm-up
ratio 6%, a batch size of 64, and the number of diffusion steps N = 5000. The
beta schedule follows a sigmoid form:
βi =

(βend − βstart ) + βstart ,
1 + exp (12(0.5 − i/N ))

with βstart = 1 × 10−7 and βend = 2 × 10−3 where i ∈ {0, · · · , N } is the
diffusion time step. The training is stopped after 86 epochs. We use a cutoff
value of 6 Å for PBC handling. Supplementary Tab. C4 summarizes detailed
hyperparameters for training of DiG for catalyst-adsorbate sampling.

Table C4: Hyperparameters of backbone model for pretraining on Open Catalyst IS2RS and training on Open Catalyst MD dataset.
Hyper Parameter
Model depth
Hidden dim (Model)
Hidden dim (Feed Forward)
Number of Heads
Optimizer
Learning rate
Warmup ratio
Learning rate schedule
Dropout p
Adam (β1 , β2 )
Adam ϵ
Weight decay
PBC Cutoff
Batch size
Diffusion steps N
Diffusion β schedule
Diffusion β start
Diffusion β end

IS2RS pretraining

MD training

Adam
0.0002
0.06
Linear Decay
0.1
(0.9, 0.98)
1E-08
0.0
6.0
Sigmoid
1E-07
0.002

C.4

Property-Guided Structure Generation

For training the DiG on an unconditional distribution, we use 15, 697 structures of carbon polymorphs generated from ab initio random structural search
(RSS) at the DFT level (PBE/plane-wave basis, with an energy cutoff of 520
eV) with a range of number of atoms from 2 to 24, following the method
in [52]. Only the relaxed structures, i.e., the final frames in relaxation processes, are taken for training. We remark that for the inverse design task, the
distribution of the structures at local energy minima does not follow an equilibrium distribution. However, the primary goal here is to generate structure
candidates with reasonable stability and targeted properties. In this context,
the relaxed structures from random structure search can well represent the
low energy structure manifold. The number of training epochs is 50, 000, with
a peak learning rate 2 × 10−4 , batch size 4096, and a warm-up ratio 6%. For
the reference lattice vector set L̄⋆ , we use the mean lattice vector set over
the dataset, which is close to three orthogonal vectors with a length of 4 Å.
As the initial structure in the catalyst-adsorbate model, this reference lattice
vector structure is also encoded into the model with an additional attention
bias term. Tab. C5 summarizes the hyperparameters for training the diffusion
model for property-guided structure generation. We use a cutoff value of 20 Å
for PBC handling.

Table C5: Hyperparameters of diffusion model training for property-guided
structure sampling.
Hyperparameter

Data Training

Model depth
Hidden dim (Model)
Hidden dim (Feed Forward)
Number of Heads
Optimizer
Learning rate
Warmup ratio
Learning rate schedule
Dropout p
Adam (β1 , β2 )
Adam ϵ
Weight decay
PBC Cutoff
Batch size
Diffusion steps N
Diffusion β schedule
Diffusion β start
Diffusion β end

Adam
0.0002
0.06
Linear Decay
0.1
(0.9, 0.98)
1E-08
0.0
20.0
Sigmoid
1E-07
0.02

Appendix D
D.1

Molecular Simulation and
Energy Evaluations

Molecular Dynamics Simulation for Protein-Ligand
Complexes

We generate MD simulation data for complex systems selected from the
PDBbind v2020 [100] using an automatic pipeline called protocolGromacs3 .
It utilizes GROMACS [101] as the backend engine with a common simulation setting for all complexes, providing a capability of high-throughput MD
simulations. Specifically, this pipeline comprises four stages: preparation, minimization, equilibration, and production simulations. In the system preparation
stage, a protein topology is generated with pdb2gmx with the amber99sbildn [102] force field with the tip3p explicit water model; the ligand parameter
and topology are generated with acpype [103]. For cases with missing atoms/residues in the PDB files, PDBFixer [99] is applied to complete the molecules.
Then, a cubic simulation box is used with a minimum distance of 1.2 nm
between the protein-ligand complex and the box boundaries. Finally, a preequilibrated system of 216 water molecules is repeated over the simulation box
to provide the solvated environment. To neutralize charged systems, appropriate ions (Na+ or Cl− , depending on the net charge of the solute molecules)
are applied by replacing randomly selected water molecules. Once the simulation box is prepared, an energy minimization process is carried out to remove
the atomic clashes and optimize the geometry of all molecules. In the equilibration simulation stage, a thermostat is applied to heat the system from 0
to 300K within 100 ps. The heated system is then further equilibrated to 1
bar in an NPT ensemble for another 100 ps. During the equilibration stage,
the bonds for molecules are constrained. For the final production, the leapfrog algorithm [104] is used for integrating Newton’s equations of motion and
a Particle Mesh Ewald (PME) [105] method is used for calculating long-range
electrostatic interactions. The LINCS [106] algorithm is adopted for resetting
all bonds to their correct lengths after an unconstrained update. Finally, the
production is performed for 100 ns with an integration time step of 2 fs.
Following the above protocol, we generate MD simulation trajectories for
1500 protein-ligand complexes. To facilitate model training, each 100-ns simulation trajectory from the production run is divided into segments of length 1
ns, resulting in 100 trajectory segments for each complex system. The proteinligand complex is mapped to the center of the primary simulation box by
applying periodic boundary conditions to ensure the integrity and connectivity
of the molecules.

https://github.com/tubiana/protocolGromacs

D.2

Energy Evaluations in Physics-Informed Diffusion
Pre-training

For physics-informed diffusion pre-training (PIDP), the energy and gradients are evaluated using OpenMM [74] following the settings used in
Folding@home [44]. The amber14sb force is used for the ablation study in
Supplementary Sec. E.3. The Generalized Born solvent model [107] is used for
solvation energy calculation.

D.3

Density Functional Theory Computation

We use DFT for the grid search of adsorbate configurations on catalyst surfaces, for verifying the adsorbate configuration distributions predicted by DiG
as shown in Fig. 4. They are carried out using VASP6.3 with setups compatible
with OC20 [10]. Specifically, periodic boundary conditions and projectoraugmented wave pseudopotentials are adopted with plane-wave electron kinetic
energy cut-off of 350 eV. Generalized gradient approximation and the revised
Perdew-Burke-Ernzerhof (RPBE) functional are employed [108, 109]. The
Monkhorst-Pack grid is used to sample the reciprocal space. For the electronic
degree of freedom, the convergence criteria for self-consistent computations
is set to 1 × 10−3 eV/atom. For ionic degree of freedom, the relaxations are
carried out only on the atomic coordinates with the lattice being fixed. Convergence is considered to be reached when the Hellmann-Feynman forces are
smaller than 0.02 eV/Å.

Appendix E
E.1

Additional results

Protein Conformation Sampling

Table E6: Protein systems utilized in this paper. Reference structure 1 is
denoted in cyan, while reference structure 2 is denoted in brown in Fig. 2b.
Protein

Ref. 1

Ref. 2

TMscore

Adenylate Kinase
Lmrb
human B-Raf kinase
D-ribose

4ake (chain A)
DEER-AF
6uan (chain A)
3dri (chain A)

1ake (chain A)
6t1z (chain A)
3skc (chain A)
1urp (chain A)

0.6899
0.7600
0.9235
0.7187

We present a list of proteins employed to demonstrate the efficacy of DiG
in generating multiple conformations in Fig. 2b in Table E6. The table provides a detailed overview of the protein systems utilized in this study, including
the reference structures denoted in cyan and brown, respectively, and the
conformational differences between the two reference structures, measured in
TMscore.

For both RBD and main protease proteins, there are some structures in the
PDB dataset used for DiG model training. We project those structures onto
the reduced 2D space spanned by the first two TICA coordinates, and show
the results in Supplementary Fig. S1. Clearly, multiple states are observed in
the maps indicated by the diamonds, but these structures together only represent a small fraction of the structure space. In contrast, the DiG-generated
structures show much broader overlaps with MD simulations in the structure
space. In the case of RBD, DiG even predicted a new region (lower right,
cluster-IV in the main text), which has no experimental determined structure.
This particular region was significantly sampled by MD simulation. We can
observe clear correspondence for the regions sampled by DiG and MD simulations. The diverse structures reveal more information about the functional
states of proteins.
Besides the qualitative comparison of the distributions generated by DiG
and those sampled by MD simulations. We provide a detailed quantitative
measurement of the overlaps of explored regions by these two methods. Taking
the regions with MD simulation structures as references, the coverage analysis
is carried out following a standard binary classification approach (see Supplementary Fig. S1). The distributions are first converted to masked binary maps
(divided to 50 × 50 regions), then the two sets of binary maps (DiG results
vs. MD simulation results) are compared. The accuracy, precision, recall, and
F1-score are computed for each case, at different sampling data sizes. There
are 50,000 structures generated by DiG for each protein. We see that the coverage (recall) increases as more structures are included for the analysis, while
the precision level is kept at high levels. In order to compare with the MD
simulation data, we took two approaches to draw samplings: (1) take structures consecutively from simulation trajectories; (2) take structures randomly
from all simulation trajectories (i.i.d sampling). We observed that the sampling
coverage and efficiency of DiG are better than MD simulations.
For two representative ligand-protein systems shown in Fig. 3b, structures
from 100 ns MD simulations are superposed to show the variation in ligand
structures (see Supplementary Fig. S2).
The ligand structure generations are carried out for a set of 16 proteins,
each paired with various numbers of ligands. In total, there are 409 ligandprotein systems in this testing dataset. In Supplementary Fig. S3, five proteins,
each with four different ligands, are shown to illustrate the best structures
generated by DiG. The ligand binding poses and atomic structures generated
by DiG exhibit diversity and are correlated with the characteristics of protein
pockets.

E.2

Catalyst-Adsorbate Sampling

Supplementary Fig. S4 shows top and front views of all adsorption configurations generated by DiG, which covers all the adsorption configurations found
by DFT relaxation for this system by traversing initial positions of the adsorbate. Note that for most systems, with a very short MD trajectory as provided

Fig. S1: Protein structure distributions and sampling coverages.

Fig. S1: a. Results for the RBD of SARS-CoV-2 spike protein. Experimentally
determined structures are mapped to the reduced 2D space, indicated using the
purple diamond symbols. On the top right panel, the same space is divided into
50x50 grids, which are classified into explored (blue) and unexplored (white)
sub-regions, depending on the presence of MD simulation structures. The accuracy, precision, recall, and F1-score are shown as a function of sampling size
(or the ratio to the whole dataset). The cluster in the lower-right region has
no experimental structures, indicating a new state revealed DiG, which is consistent with MD simulations. b. Results for the main protease following the
same analysis protocol and representations. In both plots a and b, blue star
symbols indicate the AlphaFold predicted structures in the 2D space, and red
circles show the cluster centers of MD simulation structures.

Fig. S2: Ligand structures observed in MD simulations. a. For the
case of Tyk2 target, the binding pocket is deep and well confined, MD simulations show highly similar ligand structures and binding poses. The RMSD
values compared to the crystal structure is small. b. the MD simulation results
are shown for the case of P38 protein. Similar to the DiG results, the ligand
structure exhibits larger variations compared to the cases of tyk2. For both
proteins, the same ligands shown in Figure 2 in the main text are used in the
simulations, and the simulation duration is 100 ns for both systems.

in the dataset, it can only cover one or two structures close to these relaxed
configurations. Thus, the result shows the ability of DiG to generate to unseen
systems from very short MD trajectories in the training set.

E.3

Ablation Study

We conduct an ablation study to investigate the effect of various components in
the training pipeline of DiG for protein systems. The training pipeline consists
of three stages: (i) initialization from experimental data, (ii) physics-informed
diffusion pre-training (PIDP), and (iii) training with simulation data.
The main protease of SARS-CoV-2 is selected as a case study since it has
long simulation trajectories (2.6 ms) [44] and has been studied in Section 3.1.

Fig. S3: Ligand structure generation in the binding pocket of target
proteins. The target names are indicated in the figure, with each row showing
different ligands with its best binding poses to the same target protein. Here,
best binding poses is defined as the most similar structure to the experimental
observations.

We investigate the importance of each stage of the training pipeline by evaluating the quality of structures sampled at different stages. The quality is
measured by comparing the torsion angle distribution of sampled structures
with that of the simulation trajectories. We use Ramachandran plots to visualize the distribution of torsion angles of the 6 amino acids corresponding to
the first 10 TICA components of the simulation trajectories [110].
Supplementary Fig. S5 summarizes the results of the ablation study. We
obtain approximately 100,000 filtered results from each of the three stages. The
blue area represents the ground-truth simulation distribution, which encompasses a relatively large and diverse range of torsion angles, reflecting the

Fig. S4: Additional Results for catalyst surface adsorption. All adsorption
configurations found by DiG, with the configurations from model in color and
the configurations from grid search with DFT in white. The number of adsorption sites is 6 in total. We divide all the sites into 2 groups in (a)(c) and (b)(d),
and show both the top view in (a)(b) and the front view in (c)(d).

dynamic and flexible nature of the protein. Supplementary Fig. S5a displays
the distribution of structures sampled by DiG initialized from experimental
data, i.e., the PDB protein structure dataset [96] (see Supplementary Sec. C.1).
The distribution is highly concentrated on a single point, indicating that the
sampled structures are only fit to experimental structures and do not capture
the protein’s dynamics. Supplementary Fig. S5b illustrates the distribution of
structures sampled by DiG after PIDP, which improves the generated distribution towards the equilibrium distribution using the energy function. We find
that PIDP training may generate some failure cases with very high RMSDs
or low TMscores compared to the crystal structure. Therefore, we filter out
results with RMSD higher than 10 Å and TMscore lower than 0.6.
However, PIDP alone is still insufficient to fully capture the equilibrium
distribution. Supplementary Fig. S5c displays the distribution of structures
sampled by DiG after further training with simulation data, where simulation
structures serve as direct signals to supervise DiG’s learning. The distribution becomes even more similar to the equilibrium distribution, demonstrating
DiG’s ability to learn from simulation data and generate realistic and diverse
structures.
All sampled structures at various stages of the training pipeline are physically reasonable and are similar to low energy values, as verified by the
structural quality metrics. The results show that DiG can effectively combine information from both energy function and simulation data to produce
high-quality structures reflecting the protein systems’ equilibrium distribution.

E.4

Reproducibility

In this section, we investigate the reproducibility of DiG training, under different initialization, and different random seeds which affect the order of data
batches fed into the model during the training. We conduct this experiment

Fig. S5: Ramachandran plots of the sampled structures at different stages of
the optimization process (initialization, PIDP, and simulation data training)
compared with the reference MD structures.

on the protein-ligand systems and compare the distribution of the generated

Fig. S6: Reproducibility experiments. Taking the ligand structure generation
as an example, different DiG models were trained by varying training parameters. The results of the two trained DiG models show high similarity in terms
of ligand structure differences compared to crystal structures.

ligand structures with respect to the crystal structures. Fig. S6 shows the histograms of RMSD statistics for ligand structures generated by DiG. The left
panel is identical to Fig. 3a, where the results are obtained from the model
checkpoint with the training pipeline described in Supplementary Sec. A.3,
which is used to generate all results for protein-ligand systems in this paper.
The initialization of this model is from pre-training on the CrossDock dataset.
The right panel shows the results from another model checkpoint without any
pre-training but a random initialization. Other hyperparameters except the
random seeds are kept the same in the two training processes. We observe that
the distributions from the two model checkpoints are very similar, suggesting
that DiG training is robustly reproducible.

Appendix F
F.1

Limitations

Limitations on Data Quantity and Quality

One of the major challenges and limitations of DiG is the scarcity of data
for training and evaluating the deep learning models for equilibrium distribution prediction. The ground truth data of equilibrium distribution of different
molecular systems are not easily available, as they require massive computational resources and time to generate by molecular dynamics simulation or
other methods. Therefore, we only have access to very little data for some
molecular systems, and the data quality and quantity may not be sufficient to
support the learning and generalization of DiG.
For example, for the catalyst systems, we use the Open Catalyst
dataset [10], which contains DFT-based molecular dynamics simulations of
catalyst-adsorbate systems for only 80 or 320 femtoseconds. However, this
simulation time is too short to capture the dynamics and transitions of the
systems, and the structures may not move significantly from their initial positions. Thus, we need to traverse initial positions of the adsorbate to find out

all the adsorption configurations within a unit cell. With longer MD trajectories, the model should be able to sample more adsorption configurations from a
single initial position of adsorbate. Moreover, the adsorption configurations in
the MD trajectories, which start from the relaxed configurations, tend to have
low energies, and high-energy configurations are rare in the dataset. Thus, the
density for high-energy configurations estimated by the learned DiG may be
inaccurate.
For property-guided structure generation, we use a dataset of 15,697 carbon
crystal structures [53] to train the model, which is also very limited compared
to the huge space of possible carbon polymorphs. The generative model trained
on such data may not be able to recover all the structures in the dataset, let
alone generalize to unseen carbon polymorphs. For example, our conditionally
generated structures (including 2, 4, 6, 8 carbon atoms per unit cell) only
match 88.33% of the structures in the dataset with the same numbers of atoms,
using the StructureMatcher from Pymatgen.
For the protein conformation sampling, we collect MD simulations of about
only 1000 proteins, each with 100 nanoseconds of simulation time. However,
this amount of data may not be enough to cover the diversity and complexity
of different protein structures and functions, especially for large and complex proteins that may have longer time scales and more energy barriers for
conformational changes. Furthermore, the desired equilibrium distribution for
protein model training is not well represented by the available data. Although
some simulated data have sufficient length to approximate the equilibrium distribution, they are too scarce to support the neural network models with robust
generalization and practical accuracy. Therefore, we resort to using a larger
number of experimental structures, such as the PDB dataset, as the initial
training data for the models. However, these data influence the final distribution learned by the models. We observe that these data lead to more accurate
structures and better generalization, but also to a more concentrated learned
distribution. Besides the issue of simulation length, the accuracy of simulation
may also be problematic. We find that some structures simulated by molecular
dynamics in some systems deviate too much from the experimental structures
in terms of structural accuracy. Moreover, in some systems molecular dynamics is highly sensitive to the initial state, and different initial states can result
in different distributions in practice. These factors compromise the use of simulated data as approximations of the equilibrium distribution and cause the
model to learn inaccurate distributions.
Similar issues also exist in protein-ligand training, where the simulation
time does not warrant equilibrium distributions. The simulation trajectories used for ligand-structure model training are limited to 100 ns. Yet, we
observed ligand dissociation from the pocket in some of the systems, which
were excluded from model training. Moreover, our training set only covers a
small fraction of systems. In the CrossDocked and our self-generated MD simulation datasets, there are about only 1000 unique proteins, which may affect
the generalization of our model.

The data scarcity also affects the evaluation of DiG, as we do not have
enough ground truth data of equilibrium distribution to compare with the
predictions of DiG. Therefore, we have to rely on indirect metrics, such as the
energy function, the structural quality metrics, or properties, to measure the
quality and diversity of the generated structures. However, these metrics may
not fully capture the accuracy and reliability of the equilibrium distribution
prediction, and may have some limitations or biases themselves. For example,
the structural quality metrics may not account for the dynamic and stochastic
nature of the molecular structures, and may have some dependencies on the
reference structures or the alignment methods. The property prediction may
not be sensitive to the subtle changes or variations of the molecular structures,
and may have some noise or uncertainty in the measurements or the models.
Therefore, we acknowledge that data scarcity is a serious limitation for DiG,
and we hope that more and better data of equilibrium distribution of molecular
systems can be generated and shared in the future, to enable more robust
and reliable learning and evaluation of DiG and other equilibrium distribution
prediction methods.
Data limitations also affect the training of the property predicting model
qD (c | R), which guides the structure generation based on properties. In the
sampling process for a desired property value c as described by Eqs. (3, 8) ,
the structures in early stages (i.e., large i or t) are nearly random noise, for
which the predictor model qD (c | R) are not typically trained on, making its
contribution ∇R log qD (c | R) less controlled. This may not be as harmful as
it appears, since even with an oracle property predictor, what the early stage
of sampling does is still refining the random structure to physically reasonable ones in which the predictor model contribution ∇R log qD (c | R) does not
dominate. The effect of this process also largely aligns with the desired property since for which a random structure is unlikely to achieve. However, we do
observe that in some cases small perturbance to the structure causes significant changes in the band gap prediction using the M3GNet predictor, which
makes sampling structures with demanded band gap more challenging. This
also adds to the evidence of overfitting of the predictor to the limited stable
structures. We also find that the model produces more unphysical structures
that violate the geometric or energetic constraints when conditional generation. For example, a conditionally generated structure close to a graphite may
not have perfect bond angles of exactly 120◦ . The band gap predictor model is
trained on stable carbon polymorphs. But structures in the denoising process
can be quite unstable. Thus the gradients from the predictor used to guide
the denoising process may be inaccurate and does not always lead to physical
structures. Adding guidance from an energy prediction model in the conditional generation process may guide to more physical structures. Training the
property predictor with more abundant carbon polymorphs can also improve
the quality of conditionally generated structures. Thus, it would still be helpful to generate labeled data on more noisy structures and train the property

predictor model on them, so that the model could take effect earlier in the
sampling process to better guide the structure to the desired property.

F.2

Limitations on Energy Function

In applications involving proteins, we adopt the common choice of a coarsegrained representation for proteins to reduce the dimensionality of the problem
while maintaining most of the structural features. This nevertheless incurs
challenges from the energy function (equivalently, force field) side: we have to
convert a full-atom force field to the coarse-grained level. This is required in the
PIDP training as shown in Eqs. (A14, A19) , while employing an established
coarse-grained force field is neither suitable since it is unnecessarily the coarsegrained version of the full-atom force field used in the simulation to generate
the dataset. Such a conversion is conducted in Alg. 2, but this is not precise
for coarse-graining for statistical use. Specifically, if denoting the invertible
transformed full-atom coordinate R̄ and energy function as (RCG , RFG ) and
E(RCG , RFG ) where RCG denotes the coarse-grained coordinates ((C, q) in
Alg. 2) and RFG the fine-grained details (X excluding C in Alg. 2), the required
coarse-grained energy (equilibrium free energy) under temperature T would
be:


Z
E(RCG , RFG )
dRFG .
(F33)
ECG (RCG ) = −kB T log exp −
kB T
In practice, this integral is hard to evaluate, and is a long-standing problem
in statistical mechanics and Bayesian statistics. Even in the case of Alg. 2
where we have access to the full-atom coordinates of a query structure, the
estimation is still an approximation. To see this, the gradient (negative force)
of Eq. (F33) can be written as:
∇RCG ECG (RCG ) = EpT (RFG |RCG ) [∇RCG E(RCG , RFG )],
n
o
,RFG )
exp − E(RCG
kB T
n
o
pT (RFG | RCG ) := R
,
E(RCG ,RFG )
exp −
dR
FG
kB T
so in principle, the coarse-grained gradient is an average of the full-atom gradient over samples from pT (RFG | RCG ). Under this perspective, the rigid
body assumption that Alg. 2 is based on can be understood as assuming
pT (RFG | RCG ) only concentrates on one value of RFG (i.e., a Dirac delta
distribution), meaning RFG can be uniquely determined from the given RCG .
In the algorithm, this RFG is provided from the corresponding full-atom
coordinates. This is a good approximation if the true pT (RFG | RCG ) distribution indeed concentrates at the determined RFG value; otherwise (e.g.,
there are very flexible residue or in relatively high temperature), a more precise
coarse-graining method for the energy function is required (e.g. [111]).

(m)

Moreover, in PIDP training Eq. (4), although the samples {RD,0 }M
m=1 for
evaluating the loss can be taken as any that are relevant to the problem in
principle, overly loosely chosen structures may cause numerical difficulties as
the corresponding gradient energy gradient would be too large. This is the
limiting issue from using normal mode perturbed structures hence we have
to resort to MD structures. A possible approach to mitigate this limitation is
using a “milder” energy function, which does not increase its value as steeply
on off-equilibrium structures. For PIDP training, the energy function only
needs to indicate a very small probability, and it does not matter much how
small it is, as all small values almost equally indicate a vacuum.

F.3

Limitations on Model Architecture and Scale

Another crucial limitation of DiG is the model restriction, which is resulted
from the compromise between the model capacity and the required computational resource. The model capacity determines the expressiveness and
generalization ability of the deep learning models for equilibrium distribution
prediction, while the computational resource determines the availability and
speed of the training and inference processes. In this work, we have to face
the constraint of the computational resource and make some choices that may
affect the performance of DiG.
For example, for the protein systems, we use a 12-layer Graphormer with
about 80M learnable parameters, which is relatively small considering the
complexity and diversity of protein structures and distributions. The model
capacity of DiG may not be enough to capture the intricate and highdimensional energy landscapes and distributions of protein systems, and this
can be evidenced by the structural quality of the generated protein structures.
We observe that smaller models are easily outperformed by larger models. For
example, a 4-layer Graphormer with about 10M learnable parameters only
produces a median TM-socre [91] of 0.46 on the PDB validation dataset, while
a 12-layer Graphormer can easily reach more than 0.8.
Besides, we fix the parameters of the pre-trained Evoformer module in
AlphaFold, which is used to extract the features from the protein sequence and
the MSA. Evoformer is a powerful and sophisticated module that can encode
rich and informative features for protein structure prediction, but it is also
computationally expensive and complex, and hasn’t been fine-tuned during
the training of DiG for predicting equilibrium distribution. This may lead to a
significant performance drop since the frozen parameters of Evoformer restrict
the expressiveness of DiG very much. In Supplementary Fig. S1a and S1b, the
high-density regions of MD simulation are perfectly aligned with both known
structures and predicted structures by AlphaFold, but there is an observable
shift of the high-density regions generated by DiG. We suspect that the shift is
due to the limitation of model capacity. Specifically, a fixed Evoformer implemented in DiG does not perform as well as a learnable Evoformer that is used
in AlphaFold. A similar observation is that, although for RBD protein, both
AlphaFold and DiG can generate high-quality structures with TMscores > 0.8

in all cases, their performances are different for the case of main protease,
where AlphaFold could generate high-quality structures, but structures with
TMscores > 0.8 generated by DiG only accounted for about 6.8% of all generated structures (The average TMscore of all generated structures of main
protease by DiG is about 0.64). This performance gap between AlphaFold and
DiG can be possibly caused by the fixed Evoformer. If so, the performance of
DiG could be significantly improved if we can fine-tune the Evoformer module
with the data and objective of DiG.
Moreover, in this work, we mainly focus on algorithm development, but not
on model architecture development. We mainly use the existing deep learning
architectures, such as Graphormer and Evoformer. More advanced and specialized architectures that can better exploit the 3D conformational information
and the physics principles of molecular systems may improve the performance
and efficiency of DiG.
Therefore, we acknowledge that the model architecture restriction is a serious limitation for DiG in the current implementation, and this will be resolved
in the future with enhanced capacity of advanced models.


---

# From possibility to precision in macromolecular ensemble prediction

**Authors:** Stephanie A. Wankowicz, Massimiliano Bonomi
**Year:** 2026
**Venue:** Nature Methods
**DOI:** 10.1038/s41592-026-03084-z
**Source PDF URL:** https://arxiv.org/pdf/2505.01919 (arXiv preprint; green OA per OpenAlex)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

From Possibility to Precision in Macromolecular Ensemble Prediction
Stephanie A. Wankowicz1*, Massimiliano Bonomi2
1) Molecular Physiology and Biophysics, Biochemistry, Center for Applied AI in Protein Dynamics, Center
for Structural Biology, Vanderbilt University, Nashville, TN
2) Institut Pasteur, Université Paris Cité, CNRS UMR 3528, Computational Structural Biology Unit, Paris,
France
*Correspondence: stephanie@wankowiczlab.com

Abstract
Proteins and other macromolecules exist not in a single state but as dynamic ensembles of
interconverting conformations, which are essential for catalysis, allosteric regulation, and molecular
recognition. While AI-based structure predictors like AlphaFold have revolutionized static structure
prediction, they are not yet capable of capturing conformational ensembles. Progress towards the next
generation of AI models capable of ensemble prediction is currently limited by the lack of accurate,
high-resolution ground truth ensembles at the scale required for training and validation. This is due to the
fact that no single experimental technique can fully resolve the atomistic complexity of conformational
landscapes, and fundamental challenges remain in defining, representing, comparing, and validating
structural ensembles. Here, we outline the infrastructure and methodological advances needed to
overcome these barriers. We highlight emerging strategies for integrating heterogeneous experimental
data into unified ensemble encoding representations and how to leverage these new methodologies to
build benchmarks and establish ensemble-specific validation protocols. Finally, we discuss how
ensemble predictions will be an interactive cycle of experimental and computational innovation.
Establishing this ecosystem will allow structural biology to move beyond static snapshots toward a
dynamic understanding of molecular behavior that captures the full complexity of biological systems.

Main
Biology is fundamentally a study of motion and change, where systems, from the environment to atoms,
are never still. While biology relies on these motions to function, we tend to study biology through static
representations, which restricts our understanding of many of its fundamental principles1,2. This limitation
is evident in the study of macromolecules whose functions arise from conformational ensembles3, yet are
often interpreted as a single, static structure4,5. Macroscopic equilibrium properties like binding and
stability emerge from a Boltzmann-weighted ensemble of conformations, where each microstate
contributes to the partition function defining the system’s thermodynamic behavior3,6. However, our
structural interpretations of macromolecules and their macroscopic properties mainly stem from atomistic
static models, often derived from cryo-electron microscopy (cryo-EM) and macromolecular
crystallography, including X-ray, neutron, fiber, and electron diffraction (X-ray crystallography). While
nuclear magnetic resonance (NMR) and molecular dynamics (MD) have provided critical insights into
ensembles of conformational states, each method has its limitations. NMR is primarily constrained by
system size and sensitivity7, whereas MD is limited by force field accuracy and timescale accessible 8.
While static models have offered invaluable insights into structure and function, they represent a limited
subset of the underlying conformational ensemble that drives biological activity. This overemphasis on
static representations is perpetuated in protein structure prediction, limiting these algorithms’ ability to
predict protein functions9–11. Being able to computationally model and ultimately predict macromolecular
conformational ensembles will have transformational impacts across biology by directly connecting
structural models to macroscopic measurements, revealing disease mechanisms, evolutionary
processes, and advancing next-generation therapeutics12–14.
Recognizing the limitations in the static representations of macromolecules, the structural biology
community has begun shifting its focus towards modeling conformational ensembles, details of which are
often encoded in the very experimental data used to derive static structures15–20. This paradigm shift is
also reshaping structure prediction, with growing numbers of efforts to predict conformational
ensembles21–24. While incredibly promising, this shift brings new challenges: unlike static structures,
where high-resolution models serve as widely accepted ground truths25, conformational ensembles lack a
single experimental technique capable of fully capturing the entire landscape at atomistic resolution,
leaving the field without a definitive benchmark or gold standard for prediction validation. As a result, it
remains difficult, if not impossible, for computational methods, including MD and structural ensemble
prediction algorithms, to quantitatively validate predicted ensembles at atomic resolution across the full
range of conformational states. Without a clear standard, the field faces foundational questions: What
exactly are we trying to predict, and how will we know when we have succeeded?

Protein Ensemble Prediction
The advancement in protein structure prediction achieved by AlphaFold2 highlights the transformative
potential of curated biological data, rigorous benchmarks, evaluation metrics, and innovative AI
approaches11,26. The Protein Data Bank (PDB), which primarily houses static macromolecular structural
models, provided an extensive dataset for training predictive models. Simultaneously, the critical
assessment of methods of protein structure prediction (CASP) community developed rigorous
benchmarks and evaluation metrics for assessing structural predictions27–29. Without both of these
contributions, it would have been impossible for the AlphaFold breakthrough of static protein structural
prediction to occur. To replicate breakthroughs in conformational ensembles prediction, it is imperative to
establish equivalent datasets, benchmarks, and evaluation tools, enabling innovations in encoding,

architecture, and training. We see four key issues we need to address to achieve AlphaFold-like
conformational ensemble predictions:
1) Structural ensembles are defined inconsistently across disciplines.
2) No single experimental technique alone can fully capture structural ensembles with the
accuracy and precision needed to reflect their behavior in vivo.
3) Experimental approaches for determining ensembles face major challenges, including
ensemble averaging, data sparsity, and intrinsic measurement errors.
4) Standardized representations, comparison metrics, and uncertainty quantification for structural
ensembles are still lacking.
Here, we identify critical problems limiting our ability to capture macromolecular dynamics and propose
actionable strategies to overcome them, calling on the experimental and computational structural biology
communities to collaboratively advance experimental methods and predictive modeling beyond static
snapshots toward ensemble-based representations.

Defining Macromolecular Structural Ensembles
In statistical thermodynamics, conformational ensembles provide a framework to connect microscopic
structural fluctuations to macroscopic properties. Even within its native, folded state, macromolecules
exist as an ensemble of hierarchy-related substates, ranging from bond vibrations to localized side-chain
rotamer flips to loop fluctuations to large domain rearrangements (Figure 1)30,31. The conformational
ensemble encapsulates a protein's full range of states under a given set of conditions, with each state
described by its Boltzmann factor reflecting its thermodynamic probability at equilibrium3,32–35. Collectively,
these microstates define the protein’s partition function (Z=i∑​e−βEi; Z: partition function, ​e−βEi: Boltzmann
probability density of i-th microstate; Ei: energy of i-th microstate), which governs macroscopic
observable properties. Yet, the practical challenge lies in inferring these Boltzmann weights from
incomplete, heterogeneous data, as we discuss below. Further, to relate these ensembles to function, we
must also understand how the distribution of states’ probabilities changes upon perturbation, such as
ligand binding, mutation, or changes in environmental factors such as pH, temperature, or crowding36,37.

Figure 1. The hierarchical heterogeneity that makes up conformational ensembles, spanning from atomic
vibrations, side-chain fluctuations, loop rearrangements, and large-scale domain motions, is naturally illustrated by
the protein folding free energy landscape, where local valleys and peaks correspond to the vast ensembles of
protein conformations. All changes within the conformational ensemble alter the shape of the free energy
landscape and can have profound functional consequences.

Although some experimental methods and prediction algorithms often aim to represent conformational
ensembles, they typically capture only a limited number of discrete macrostates, groups of microstates
sharing similar structural or energetic properties, such as an active kinase. This oversimplification masks
the full complexity of the ensemble, hindering our ability to accurately understand how the continuum of
microstates contributes to observed macroscopic behavior38. Since every microstate influences the
partition function, it is vital to consider the entire ensemble, despite the challenges in modeling or
measurement.
One striking example of the complexity of determining conformational ensembles comes from the
ribosome39,40. The ribosome’s macro-structural states, such as in the rotated or elongation factor-bound
states, are thermodynamically stabilized, with each conformation governed by a balance of enthalpic and
entropic contributions41–44. Even minor fluctuations in the ribosome’s protein and RNA components can
shift the equilibrium among these states, influencing overall translation speed, fidelity, and
responsiveness to external factors39,40. Oversimplifying the ribosome’s thermodynamic ensemble by
considering only macrostates overlooks key details that can influence evolutionary dynamics, lead to
mistranslation, and affect drug design strategies.
The ribosome represents but one complex example of the ensemble nature of macromolecules. Other
examples include transporters cycle between metastable states, with thermodynamic fluctuations driving
function, as seen in GPCRs45–47, multiple conformational changes enzymes have during their catalytic
cycles, often populating rare but essential transient states that regulate chemical steps48,49. Further,
ligand binding can reshape ensembles, as in nuclear receptors, where conformational changes toggle

the receptor between transcriptionally active and repressed states50. Finally, intrinsically disordered
regions (IDRs) highlight ensembles without a dominant folded structure, often enabling
context-dependent interactions with diverse binding partners51–53. The diversity of systems and biological
questions underscores the importance of modeling and predicting conformational ensembles.

How do we generate ground truth ensembles?
The examples above underscore the potential of integrating experimental methods to unravel how
conformational ensembles govern biological function. The link between ribosomal ensembles and their
properties and functions was derived from many techniques and datasets, emphasizing that no single
experimental or computational method can fully capture a structural ensemble, compelling us to move
beyond the one technique, one structure, one solution mindset54. Constructing a conformational
ensemble requires two key elements: identifying the conformation of each state at an atomistic level of
uncertainty, and quantifying its contribution to the partition function.
First, we need to expand the algorithms pioneered by the integrative structural biology community to
unite statistical analyses on multiple pieces of data from the same data types55–57 (Figure 2A). Different
experimental structural biology techniques provide unique information critical to capture a
macromolecular conformational ensemble, but each has different limitations. Cryo-EM and X-ray
crystallography can reveal high-resolution atomic structures, but are restricted due to their frozen state
and/or crystalline environment. In contrast, NMR provides structural information averaged over multiple
conformational states that interconvert more rapidly than the timescale of the NMR measurement. As a
result, separating this averaged data into distinct conformational states and determining their relative
populations remains a major challenge58. Spectroscopy approaches like FRET or double electron
electron resonance (DEER) help detect rare states, though the sparsity of the data prevents the ability to
resolve detailed macrostates fully59. Combining these concepts can include cryo-EM and X-ray, which
could give us atomistic information on multiplicity of states, with local dynamics supported by NMR, and
large macromolecular motions can be provided by spectroscopy techniques, SAXS, or Atomic Force
Microscopy (AFM)60–62.
Equally important is the use of a rigorous statistical structural biology framework to extract maximal
information on conformational ensembles from any one technique. For example, by mining the wealth of
structural experimental data in the PDB, analyzing multi-temperature or fragment-screening X-ray
datasets, or integrating heterogeneous particle populations in cryo-EM, to reveal rare or otherwise
hidden states20,63–66(Figure 2B). All of this information can be greatly supported by incorporating
computational approaches, such as MD or structure predictions, as discussed below.

Figure 2. Strategies for generating gold-standard conformational ensemble datasets.
(A) Statistical methods applied to multiple datasets from the same technique (e.g., pseudoensembles in crystallography,
heterogeneous cryo-EM particle populations, or replicate NMR measurements) can disentangle hidden states and quantify their
relative populations. (B) Integrative approaches that combine distinct experimental modalities such as high-resolution cryo-EM
or crystallography for atomistic states, NMR for local dynamics, and FRET, DEER, SAXS, or AFM for large-scale
motions—provide complementary information across scales of heterogeneity. Together, these statistical and integrative
strategies enable robust ensemble modeling that captures both common and rare conformational states.

We also must improve our ability to harness currently underutilized raw experimental data. Most
experimental observables reflect time and ensemble averages over millions of conformations; thus, only
conformational ensemble models accurately represent the experimental measurements5. However, most
structural modeling algorithms only tend to model the most likely conformation, discarding the rich
heterogeneity in the raw experimental data that reflects a broader conformational ensemble67,68. While
new algorithms have begun to push the field beyond modeling a singular state, they still likely only
capture a fraction of the accessible states16,69,70. Exciting new progress in determining conformational
ensembles directly from cryo-EM particle stacks and using the often discarded diffuse scattering from
X-ray crystallography can bring even more information about conformational ensembles in structural
biology data into light71–7374. Continuous algorithmic development to model these "hidden" signals will
provide a more comprehensive picture of macromolecular ensembles.

Reliable approaches are also needed to determine the statistical weights of conformations in a manner
consistent with available data from both experiments and theory. For example, in cryo-EM, a key
challenge is accurately fitting atomic models into continuously varying density maps while assigning
appropriate Boltzmann probabilities that reflect the underlying energetic landscape15. While MD is often
used to bridge these gaps74, current biomolecular force fields have notable limitations, and the sampling
problem presents an immense computational burden, particularly for large conformational changes, such
as a domain movement75–78. Enhanced sampling techniques such as metadynamics or replica exchange
could help fill missing conformational states, primarily if experimental data can anchor metastable
states18,79. Yet scaling these approaches to obtain a complete structural ensemble across many biological
systems remains a formidable challenge, requiring advances in high-throughput computation and
potential neural network-based force fields80.
Further, compositional heterogeneity, derived from ligand occupancy, stoichiometry, or assembly state,
must be considered alongside conformational heterogeneity when weighting states81. Because most
structural techniques are ensemble averaged, compositional and conformational variability are conflated;
however, there are initial strategies to work on these. In cryo-EM, a normalized local filter can quantify
per-voxel variance relative to local signal, highlighting regions where compositional differences
dominate82,83. In crystallography, PanDDA event maps reveal low-occupancy ligands that might otherwise
be mistaken for conformational disorder84; however, there are still significant challenges in disentangling
the conformational and compositional heterogeneity outside of the binding site. Finally, time-resolved
techniques or integration with orthogonal data sources such as native mass spectrometry provide an
additional layer of validation, enabling ensemble models that explicitly separate composition from
conformation85,86.
Finally, we must continue advancing hardware and software technologies to enhance our capacity for
collecting and analyzing high-quality structural data at scale. The challenge is twofold: efficiently
generating the vast datasets needed to populate conformational ensembles using techniques we know
can obtain these conformational ensembles, and designing the computational pipelines to integrate and
analyze them in real-time. Examples include real-time cryo-EM data analysis and ongoing efforts to
automate and streamline high-throughput X-ray data processing87–90. Innovations such as robotics for
crystal harvesting, machine learning-assisted data evaluation91,92, and real-time quality metrics offer
promising steps forward. Integrating these noisy datasets with non-structural data, such as
protein-protein interaction networks or genomic data, could further improve ensemble determination by
uncovering hidden states93,94.

Experimental Challenges of Averaging, Sparsity, Errors, and
Encoding
While collecting vast amounts of structural data at high-throughput scales holds great promise for
uncovering conformational ensembles, accurately defining these ensembles remains challenging due to
the ill-posed nature of the underlying inverse problem. Structural biology data typically capture
ensemble-averaged measurements, resulting in an underdetermined scenario where multiple
conformational ensemble models can equally fit the observed data (Figure 3)95.
Furthermore, experimental noise inherently increases uncertainty and reduces the precision and
reliability of reconstructed ensembles, with each experimental technique introducing distinct noise
profiles. Within single techniques, new approaches explicitly account for technique-specific noise, for

example, Maximum Entropy reweighting techniques that integrate cryo-EM with MD ensembles, can
better separate genuine conformational heterogeneity from experimental uncertainty18. Other methods,
such as variational autoencoders, have demonstrated potential for capturing continuous conformational
states from cryo-EM data. Yet, their effectiveness can be limited by noise generated from different
datasets, hindering generalizability across datasets15,96.
Building on these approaches, a growing set of Bayesian inference frameworks addresses sparsity,
averaging, and measurement error more broadly, opening the door to principled integration of data
across multiple experimental modalities78,97–101. Such integrative approaches leverage the complementary
strengths of different modalities, such as NMR or diffuse scattering, to identify correlated motion that can
be connected to atomistic information in X-ray or cryo-EM data. Ultimately, the full potential of integrative
structural biology hinges on developing sophisticated computational methods that accurately reweight
conformational states based on diverse layers of experimental evidence.
Integrating techniques becomes more complex as proteins frequently exhibit differential dynamics across
domains, with rigid cores coexisting alongside highly flexible loops or intrinsically disordered extensions.
This heterogeneity poses additional challenges because of the assumptions underpinning many
ensemble modeling approaches and comparison metrics. For example, global metrics such as root mean
square distance (RMSD) or Jensen–Shannon divergence can overweight highly dynamic regions while
underreporting subtle but functionally important motions in structured domains. Similarly, Bayesian
reweighting or maximum entropy approaches must account for spatially varying uncertainty, as one
domain may be well constrained by experimental data while another domain remains underdetermined.

Figure 3. Modeling a conformational ensemble from a single structural modality is an ill-posed problem. For
example, say you have eight different ‘true’ input conformations that comprise the experimental data (input). All of

this data gets collapsed into ensemble-averaged data. While the model captures much of the structural ensemble, it
overpopulates some conformations (i.e. green) and misses others (i.e. grey). However, it collectively explains much
of the underlying experimental data.

Another complication is that inter-domain coupling can blur the boundary between local and global
heterogeneity. Motions in one domain may allosterically influence the conformational distribution of
another, leading to complex cross-correlations that are difficult to capture with independent models.
Cryo-EM 3D variability analysis often highlights this uneven distribution of motion, but translating those
observations into consistent ensemble encodings requires hierarchical representations that can treat
domains differently while maintaining a unified partition function20.
These challenges underscore that the encoding framework of ensembles often introduces limitations.
The majority of structural data uses static PDBx/mmCIF models, which, while highly effective in encoding
fixed atomic coordinates, fail to represent conformational ensembles adequately102. The current
mechanisms to encode different conformational states within the format, including alternative locations
(altlocs), B-factors, and multimodel encoding, are insufficient for fully capturing the variety of states that
make up an ensemble68,103. Altlocs typically represent a parsimonious model, B-factors or atomic
displacement factors mix genuine structural fluctuations with experimental noise or lattice movements68,
and multimodel encoding lacks crucial weighting information needed to represent conformational
probabilities accurately70.
The encoding of conformational ensembles falls along the spectrum from the maximum parsimony
principle, which aims to explain the underlying data using the fewest parameters16,104, or the maximum
entropy principle, which seeks to create the least biased model distribution consistent with the underlying
data by maximizing the Shannon entropy. Within experimental data modeling, maximum parsimony
models, such as multiconformer models, allow for more direct encoding of occupancy or weights of
different conformations, but are less expressive with subtle anharmonic motions and are limited in
backbone movement. Maximum entropy methods can be advantageous in fitting very low occupancy
states and picking up more subtle anharmonic motion78,105, but the model complexity necessitates
additional methods to extract biologically meaningful insights, such as identifying metastable states and
assigning population weights. Other ensemble methods aim to explain the data collectively, but require
re-weighting to be translated into maximum entropy models70,106. Regardless of the method used, the
experimental data can be overfit if uncertainties are neglected or poorly modeled. Determining the best
method for modeling and encoding ensembles, and how to accurately compare different methodologies,
remains a fundamental challenge.
There is a possibility of taking the best from both approaches, though more expressive encoding of
conformational ensembles in the PDBx/mmCIF format, including hierarchical information to represent
relationships among structural states and separating conformational from compositional heterogeneity to
improve interpretability102. Future work must include integration and encoding across experimental
datasets, such as multiple cryo-EM maps. However, while these encoding approaches facilitate mapping
data into a unified embedding space, they may also obscure signals due to uncertainties or low
signal-to-noise ratios inherent in some techniques. Robust methodologies to compare and evaluate the
effectiveness of different conformational ensemble encodings in resolving the inverse problem and
translating results into biologically meaningful insights are critical, as they will also enable the rapid
creation and testing of new encoding strategies.

Comparing and Evaluating Structural Ensembles

In addition to encoding, we must establish rigorous frameworks for comparing conformational
ensembles. While we have methods to compare coarse-grained ensemble-averaged descriptors of
discrete-state heterogeneity, such as in SAXS or FRET107, we still lack this ability at an atomistic level.
For single static structures, evaluating the agreement between structures often involves
root-mean-square deviation (RMSD), which measures the average atomic distance between two
structures after alignment. Alternatively, specific structural features (e.g., dihedral angles) can be
compared to experimental data, which is often represented by a sharply peaked posterior probability
around the expected value108. However, accurately representing conformational ensembles requires
shifting toward probability distribution functions (PDFs), enabling more physically realistic comparisons to
experimental data. MD methods leverage symmetric divergence measures, such as Jensen-Shannon or
Jeffrey’s divergence, for quantitative PDF comparisons109. However, because PDFs are calculated from
low-dimensional projections, a single PDF can map onto several structurally distinct, and potentially
non-physical, ensembles. Furthermore, metrics based solely on PDFs are thus likely to encounter
challenges when integrated into loss or optimization functions, reminiscent of initial difficulties faced with
RMSD-based evaluations in CASP, leading to the development of alternative metrics, such as the Local
Distance Difference Test (LDDT)29. More work is required to devise projection strategies that conserve
the defining features of high-dimensional conformational spaces while potentially embedding relevant
physical properties in their low-dimensional representations or other embedding strategies similar to
those used with protein language models110.
Alternatively, structural ensembles can be assessed based on their fit to experimental data. Several
methodologies have been developed to compute forward models from MD simulations, which allow
configurations to be constrained by experimental observables. Back-calculating intensities, maps, or raw
particle stacks provides an additional means of evaluating ensemble accuracy111,112. However, multiple
conformational states may satisfy the same experimental data, raising questions about how to determine
the most physically meaningful representation. Considerable work is also needed to develop the best
methods to compare conformational ensembles to single or multiple pieces of experimental data.
A central question in ensemble determination is evaluating whether the states and estimated weights of
conformers are “good enough”. The answer ultimately depends on the intended use of the ensemble. If
the goal is primarily to validate and compare with experimental data, it is crucial to ensure accurate
determination of the weights of conformers that contribute significantly to the measured observables.
This can be particularly challenging when observables depend nonlinearly on structural properties. For
example, in measurements like NMR nuclear Overhauser effect (NOEs) or FRET where signal scales
with inverse sixth power of the distance (1/r6), even sparsely populated conformers with short interatomic
distances can significantly contribute to ensemble averaged observables, and their weights must
therefore be determined with high precision113.
In contrast, for functional applications, such as assessing the effect of a mutation or ligand binding, the
critical issue is whether the inferred populations resolve differences above the level of statistical
uncertainty, which can be quantified using bootstrap or jackknife resampling. Finally, when ensembles
are linked to specific biological functions, the challenge becomes first identifying which structural states
are responsible for specific functions and ensuring that their populations are accurately estimated.

Integrating ML and MD to model conformational ensembles
While experimental data can collectively provide ground truth data to determine conformational
ensembles, modeling these states cannot be done without computational methods, including MD and

ML-based methods. While MD inherently attempts to model conformational ensembles, it is limited by the
accuracy of the force fields and the timescales accessible in unbiased MD simulations8. A new
generation of MD force fields, including machine-learned models, are beginning to enable atomistic
simulations at quantum chemistry accuracy and coarse-grained potentials that retain atomistic predictive
power114–116, allowing longer and more accurate simulations. On the other hand, enhanced-sampling
strategies can help overcome sampling limitations, but often require methodological expertise for each
system, limiting automation and transferability117. Recent machine learning approaches have addressed
these issues and improved enhanced sampling strategies, helping to accelerate MD exploration of
conformational space118.
However, the future is one in which generative ML-driven techniques alone will enable generating
structural ensembles with accuracy comparable to atomistic MD with more biologically relevant time
scales. Boltzmann generators first demonstrate this by using normalizing flows to generate unbiased
conformations from the equilibrium state distribution119. More recently, generative diffusion models have
taken over the static structure prediction space120,121. Using similar approaches, but often training with
static structure, MD simulations, and in some cases, thermodynamic information, models have begun to
predict pieces of conformational ensembles21,24,122–124. Notably, additional models were shown to
efficiently determine the structure of intrinsically disordered proteins and regions125,126.
Despite their promise, current ensemble prediction methods remain far from reliable. Work manipulating
AlphaFold multiple sequence alignments (MSAs) has shown that structural diversity can be induced, but
these approaches lack any notion of the relative probabilities of the resulting conformations22,127. They
often generate thermodynamically unstable or improbable states, and it remains unclear when these
methods fail or how to detect over-conditioning and template leakage, particularly in the absence of
ground-truth ensembles for comparison128. Still, these efforts provide a foundation for building
multimodal, generative AI-driven frameworks that incorporate experimental data at scale. Recent
proof-of-principle studies demonstrate that combining experimental data with AlphaFold-like models,
often with MSA manipulations, can improve static structure prediction and even show some proof of
principles capturing conformational ensembles129–135. Such demonstrations highlight the potential of
generative approaches; however, realizing this vision requires a more robust infrastructure to effectively
integrate experimental datasets with ML methods, including substantial development to build robust
infrastructure and better metrics that evaluate ML-derived ensembles against experimental ground truths
rather than imperfect structural models, ensuring progress toward reliability and interpretability. We see
the future being a tighter integration between machine learning and structural biology that can create a
virtuous cycle: accelerating and improving experimental data processing and model building, while
feeding back into more accurate ensemble predictors, recognizing that all structural data inherently
encode ensembles and deserve to be modeled as such103.

Conclusion
The thermodynamic hypothesis from Christian Anfinsen states that “the native conformation is
determined by the totality of interatomic interactions and hence by the amino acid sequence, in a given
environment”136. Conformational ensembles are driven by the amino acid sequence and the environment,
including any perturbations to the macromolecule. Here, we outline key conceptual and methodological
foundations needed to more accurately predict these ensembles. Advancing our ability to predict
conformational landscapes will expand our understanding of complex biological mechanisms and enable
the development of novel therapeutic strategies. We can design small molecules that stabilize specific

conformations by predicting low-population states or engineer antibodies whose binding depends on a
precisely defined structural ensemble137,138. Likewise, successful enzyme design hinges on accurately
predicting conformational ensembles, as catalysis inherently requires enzymes to traverse complex
conformational landscapes139,140.
It is also important to critically evaluate the current limitations of (static) structure prediction methods.
Current limitations include achieving sub-angstrom accuracy or the “last Angstrom problem”, and the
accurate modeling of non-protein structures, including RNA. Theoretically, both issues may arise from the
lack of ensemble representation. In proteins, many atoms undergo vibrations or subtle conformational
fluctuations that are functionally relevant and may have evolved, while RNA is known to be inherently
flexible141. However, it is also possible that ensemble prediction algorithms will perpetuate or make these
problems worse. Further, existing methods still struggle to predict the effects of mutations,
post-translational modifications, or other perturbations142,143. In principle, predicting ensembles could
bridge this gap by linking perturbations to shifts in state populations, yet proof will require new data and
benchmarks. Finally, many ensemble prediction methods are built off the architecture of static structure
prediction models, which may not be optimal to capture conformational ensembles. Ensemble prediction
will likely demand architectures that model distributions, not points.
Now is the time to build shared infrastructure for defining, collecting, modeling, encoding, and evaluating
conformational ensembles. Such a framework would provide a powerful iterative loop of prediction,
experimental validation, and refinement, bringing us closer to the ability to predict ensembles. This
infrastructure is also necessary for extending conformational ensembles predictions to in-vivo context or
obtaining timescale information. As high-throughput biophysical assays and in-vivo structure
determination continue to provide new information on how ensembles change across conditions144–146, we
need infrastructure in place to incorporate this new data to enable active learning to improve the
prediction of conformational ensembles in different environments and with different perturbations.
Moreover, a unified ecosystem will pave the way for capturing kinetic properties, extending ensemble
modeling from thermodynamic ensembles to temporally resolved protein dynamics. Overall, this shift
promises to move structural biology beyond static snapshots toward a dynamic understanding of
molecular behavior that captures the full complexity of biological systems.

Acknowledgements
We thank Jared Sagendorf, Andrej Sali, Arthur Zalevsky, Frank Noe, and James Fraser for helpful
feedback on this manuscript. S.A.W. is supported by the American Cancer Society. M.B. acknowledges
funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research
and innovation programme (Grant agreement No. 101086685 – bAIes).

References
1.​ Wai, T. & Langer, T. Mitochondrial Dynamics and Metabolic Regulation. Trends Endocrinol Metab 27,
105–117 (2016).
2.​ Medzhitov, R. Recognition of microorganisms and activation of the immune response. Nature 449,
819–826 (2007).
3.​ Hilser, V. J., García-Moreno E, B., Oas, T. G., Kapp, G. & Whitten, S. T. A statistical thermodynamic
model of the protein ensemble. Chem Rev 106, 1545–1558 (2006).
4.​ van den Bedem, H. & Fraser, J. S. Integrative, dynamic structural biology at atomic resolution--it’s
about time. Nat Methods 12, 307–318 (2015).
5.​ Lane, T. J. Protein structure prediction has reached the single-structure frontier. Nat Methods 20,
170–173 (2023).
6.​ Hilser, V. J. et al. Statistical Thermodynamics of the Protein Ensemble: Mediating Function and
Evolution. Annu Rev Biophys (2025) doi:10.1146/annurev-biophys-061824-104900.
7.​ Alderson, T. R. & Kay, L. E. NMR spectroscopy captures the essential role of dynamics in regulating
biomolecular function. Cell 184, 577–595 (2021).
8.​ Piana, S., Klepeis, J. L. & Shaw, D. E. Assessing the accuracy of physical models used in
protein-folding simulations: quantitative evidence from long molecular dynamics simulations. Curr
Opin Struct Biol 24, 98–105 (2014).
9.​ Baek, M. et al. Accurate prediction of protein structures and interactions using a three-track neural
network. Science 373, 871–876 (2021).
10.​ Lin, Z. et al. Evolutionary-scale prediction of atomic-level protein structure with a language model.
Science 379, 1123–1130 (2023).
11.​ Jumper, J. et al. Highly accurate protein structure prediction with AlphaFold. Nature 596, 583–589
(2021).
12.​ Wankowicz, S. A., de Oliveira, S. H., Hogan, D. W., van den Bedem, H. & Fraser, J. S. Ligand
binding remodels protein side-chain conformational heterogeneity. Elife 11, (2022).
13.​ Boehr, D. D., Nussinov, R. & Wright, P. E. The role of dynamic conformational ensembles in

biomolecular recognition. Nat Chem Biol 5, 789–796 (2009).
14.​ Sailer, Z. R. & Harms, M. J. Molecular ensembles make evolution unpredictable. Proc Natl Acad Sci
U S A 114, 11938–11943 (2017).
15.​ Zhong, E. D., Bepler, T., Berger, B. & Davis, J. H. CryoDRGN: reconstruction of heterogeneous
cryo-EM structures using neural networks. Nat Methods 18, 176–185 (2021).
16.​ Wankowicz, S. A. et al. Automated multiconformer model building for X-ray crystallography and
cryo-EM. Elife 12, (2024).
17.​ Stachowski, T. R. & Fischer, M. FLEXR: automated multi-conformer model building using
electron-density map sampling. Acta Crystallogr D Struct Biol 79, 354–367 (2023).
18.​ Hoff, S. E., Thomasen, F. E., Lindorff-Larsen, K. & Bonomi, M. Accurate model and ensemble
refinement using cryo-electron microscopy maps and Bayesian inference. PLoS Comput Biol 20,
e1012180 (2024).
19.​ Włodarski, T. et al. Bayesian reweighting of biomolecular structural ensembles using heterogeneous
cryo-EM maps with the cryoENsemble method. Sci Rep 14, 18149 (2024).
20.​ Punjani, A. & Fleet, D. J. 3D variability analysis: Resolving continuous flexibility and discrete
heterogeneity from single particle cryo-EM. J Struct Biol 213, 107702 (2021).
21.​ Lewis, S. et al. Scalable emulation of protein equilibrium ensembles with generative deep learning.
bioRxiv 2024.12.05.626885 (2025) doi:10.1101/2024.12.05.626885.
22.​ Del Alamo, D., Sala, D., Mchaourab, H. S. & Meiler, J. Sampling alternative conformational states of
transporters and receptors with AlphaFold2. Elife 11, (2022).
23.​ Li, S. et al. Improving AlphaFlow for Efficient Protein Ensembles Generation. (2024).
24.​ Janson, G., Jussupow, A. & Feig, M. Deep generative modeling of temperature-dependent structural
ensembles of proteins. bioRxiv 2025.03.09.642148 (2025) doi:10.1101/2025.03.09.642148.
25.​ Burley, S. K. et al. Protein Data Bank (PDB): The Single Global Macromolecular Structure Archive.
Methods Mol Biol 1607, 627–641 (2017).
26.​ Jumper, J. et al. Applying and improving AlphaFold at CASP14. Proteins 89, 1711–1721 (2021).
27.​ Cozzetto, D. et al. Evaluation of template-based models in CASP8 with standard measures. Proteins

77 Suppl 9, 18–28 (2009).
28.​ Olechnovič, K., Kulberkytė, E. & Venclovas, C. CAD-score: a new contact area difference-based
function for evaluation of protein structural models. Proteins 81, 149–162 (2013).
29.​ Mariani, V., Biasini, M., Barbato, A. & Schwede, T. lDDT: a local superposition-free score for
comparing protein structures and models using distance difference tests. Bioinformatics 29,
2722–2728 (2013).
30.​ Hammes, G. G. Multiple conformational changes in enzyme catalysis. Biochemistry 41, 8221–8228
(2002).
31.​ Lewandowski, J. R., Halse, M. E., Blackledge, M. & Emsley, L. Protein dynamics. Direct observation
of hierarchical protein dynamics. Science 348, 578–581 (2015).
32.​ Popovych, N., Sun, S., Ebright, R. H. & Kalodimos, C. G. Dynamically driven protein allostery.
Nature Structural & Molecular Biology 13, 831–838 (2006).
33.​ Williams, J. C. & McDermott, A. E. Dynamics of the flexible loop of triosephosphate isomerase: the
loop motion is not ligand gated. Biochemistry 34, 8309–8319 (1995).
34.​ McElheny, D., Schnell, J. R., Lansing, J. C., Dyson, H. J. & Wright, P. E. Defining the role of
active-site loop fluctuations in dihydrofolate reductase catalysis. Proc Natl Acad Sci U S A 102,
5032–5037 (2005).
35.​ Pumm, A.-K. et al. A DNA origami rotary ratchet motor. Nature 607, 492–498 (2022).
36.​ Wei, G., Xi, W., Nussinov, R. & Ma, B. Protein Ensembles: How Does Nature Harness
Thermodynamic Fluctuations for Life? The Diverse Functional Roles of Conformational Ensembles
in the Cell. Chem Rev 116, 6516–6551 (2016).
37.​ Cheung, M. S. & Thirumalai, D. Effects of crowding and confinement on the structures of the
transition state ensemble in proteins. J Phys Chem B 111, 8250–8257 (2007).
38.​ Wankowicz, S. & Fraser, J. Making sense of chaos: uncovering the mechanisms of conformational
entropy. ChemRxiv (2024) doi:10.26434/chemrxiv-2023-9b5k7-v3.
39.​ Ray, K. K. et al. Entropic control of the free-energy landscape of an archetypal biomolecular
machine. Proc Natl Acad Sci U S A 120, e2220591120 (2023).

40.​ Steitz, T. A. A structural understanding of the dynamic ribosome machine. Nat Rev Mol Cell Biol 9,
242–253 (2008).
41.​ Fischer, N. et al. Structure of the E. coli ribosome-EF-Tu complex at <3 Å resolution by Cs-corrected
cryo-EM. Nature 520, 567–570 (2015).
42.​ Kaledhonkar, S. et al. Late steps in bacterial translation initiation visualized using time-resolved
cryo-EM. Nature 570, 400–404 (2019).
43.​ Fischer, N., Konevega, A. L., Wintermeyer, W., Rodnina, M. V. & Stark, H. Ribosome dynamics and
tRNA movement by time-resolved electron cryomicroscopy. Nature 466, 329–333 (2010).
44.​ Agirrezabala, X. et al. Structural characterization of mRNA-tRNA translocation intermediates. Proc
Natl Acad Sci U S A 109, 6094–6099 (2012).
45.​ Yang, X. et al. Entropy drives the ligand recognition in G-protein-coupled receptor subtypes. Proc
Natl Acad Sci U S A 121, e2401091121 (2024).
46.​ Dror, R. O. et al. Identification of two distinct inactive conformations of the beta2-adrenergic receptor
reconciles structural and biochemical observations. Proc Natl Acad Sci U S A 106, 4689–4694
(2009).
47.​ Nygaard, R. et al. The dynamic process of β(2)-adrenergic receptor activation. Cell 152, 532–542
(2013).
48.​ Boehr, D. D., McElheny, D., Dyson, H. J. & Wright, P. E. The dynamic energy landscape of
dihydrofolate reductase catalysis. Science 313, 1638–1642 (2006).
49.​ Kerns, S. J. et al. The energy landscape of adenylate kinase during catalysis. Nat Struct Mol Biol 22,
124–131 (2015).
50.​ MacTavish, B. S. et al. Ligand efficacy shifts a nuclear receptor conformational ensemble between
transcriptionally active and repressive states. Nat Commun 16, 2065 (2025).
51.​ Tesei, G. et al. Conformational ensembles of the human intrinsically disordered proteome. Nature
626, 897–904 (2024).
52.​ Hilser, V. J. & Thompson, E. B. Intrinsic disorder as a mechanism to optimize allosteric coupling in
proteins. Proc Natl Acad Sci U S A 104, 8311–8315 (2007).

53.​ Hilser, V. J. & Thompson, E. B. Structural dynamics, intrinsic disorder, and allostery in nuclear
receptors as transcription factors. J Biol Chem 286, 39675–39682 (2011).
54.​ Schwalbe, H. et al. The future of integrated structural biology. Structure 32, 1563–1580 (2024).
55.​ Rout, M. P. & Sali, A. Principles for Integrative Structural Biology Studies. Cell 177, 1384–1403
(2019).
56.​ Braitbard, M., Schneidman-Duhovny, D. & Kalisman, N. Integrative Structure Modeling: Overview
and Assessment. Annu Rev Biochem 88, 113–135 (2019).
57.​ Rieping, W., Habeck, M. & Nilges, M. Inferential structure determination. Science 309, 303–306
(2005).
58.​ Palmer, A. G., 3rd. NMR characterization of the dynamics of biomacromolecules. Chem Rev 104,
3623–3640 (2004).
59.​ Schuler, B. & Hofmann, H. Single-molecule spectroscopy of protein folding dynamics--expanding
scope and timescales. Curr Opin Struct Biol 23, 36–47 (2013).
60.​ Jiang, Y., Wang, Z. & Scheuring, S. A structural biology compatible file format for atomic force
microscopy. Nat Commun 16, 1671 (2025).
61.​ Da Vela, S. & Svergun, D. I. Methods, development and applications of small-angle X-ray scattering
to characterize biological macromolecules in solution. Curr Res Struct Biol 2, 164–170 (2020).
62.​ Tessmer, M. H. & Stoll, S. Protein Modeling with DEER Spectroscopy. Annu Rev Biophys (2024)
doi:10.1146/annurev-biophys-030524-013431.
63.​ Fraser, J. S. et al. Accessing protein conformational ensembles using room-temperature X-ray
crystallography. Proc Natl Acad Sci U S A 108, 16247–16252 (2011).
64.​ Keedy, D. A. et al. An expanded allosteric network in PTP1B by multitemperature crystallography,
fragment screening, and covalent tethering. Elife 7, (2018).
65.​ Creon, A. et al. Statistical crystallography reveals an allosteric network in SARS-CoV-2 Mpro. bioRxiv
(2025) doi:10.1101/2025.01.28.635305.
66.​ Mehlman, T., Ginn, H. M. & Keedy, D. A. An expanded trove of fragment-bound structures for the
allosteric enzyme PTP1B from computational reanalysis of large-scale crystallographic data.

Structure 32, 1231–1238.e4 (2024).
67.​ Bozovic, O. et al. Real-time observation of ligand-induced allosteric transitions in a PDZ domain.
Proc Natl Acad Sci U S A 117, 26031–26039 (2020).
68.​ Kuzmanic, A., Pannu, N. S. & Zagrovic, B. X-ray refinement significantly underestimates the level of
microscopic heterogeneity in biomolecular crystals. Nat Commun 5, 3220 (2014).
69.​ Flowers, J. et al. Expanding Automated Multiconformer Ligand Modeling to Macrocycles and
Fragments. bioRxiv (2024) doi:10.1101/2024.09.20.613996.
70.​ Ploscariu, N., Burnley, T., Gros, P. & Pearce, N. M. Improving sampling of crystallographic disorder
in ensemble refinement. Acta Crystallogr D Struct Biol 77, 1357–1364 (2021).
71.​ Meisburger, S. P., Case, D. A. & Ando, N. Diffuse X-ray scattering from correlated motions in a
protein crystal. Nat Commun 11, 1271 (2020).
72.​ Meisburger, S. P., Thomas, W. C., Watkins, M. B. & Ando, N. X-ray Scattering Studies of Protein
Structural Dynamics. Chem Rev 117, 7615–7672 (2017).
73.​ Dingeldein, L. et al. Amortized template-matching of molecular conformations from cryo-electron
microscopy images using simulation-based inference. bioRxiv (2024)
doi:10.1101/2024.07.23.604154.
74.​ Evans, L. et al. Counting particles could give wrong probabilities in Cryo-Electron Microscopy.
bioRxiv 2025.03.27.644168 (2025) doi:10.1101/2025.03.27.644168.
75.​ Shaw, D. E. et al. Atomic-level characterization of the structural dynamics of proteins. Science 330,
341–346 (2010).
76.​ Wang, J. et al. Gaussian accelerated molecular dynamics (GaMD): principles and applications.
Wiley Interdiscip Rev Comput Mol Sci 11, (2021).
77.​ Singh, S. & Hanson, S. Running and analyzing massively parallel molecular simulations. ChemRxiv
(2024) doi:10.26434/chemrxiv-2024-vwpww.
78.​ Tang, W. S. et al. Ensemble Reweighting Using Cryo-EM Particle Images. J Phys Chem B 127,
5410–5421 (2023).
79.​ Vani, B. P., Aranganathan, A., Wang, D. & Tiwary, P. AlphaFold2-RAVE: From Sequence to

Boltzmann Ranking. J Chem Theory Comput 19, 4351–4354 (2023).
80.​ Wang, J. et al. Machine Learning of Coarse-Grained Molecular Dynamics Force Fields. ACS Cent
Sci 5, 755–767 (2019).
81.​ Rabuck-Gibbons, J. N., Lyumkis, D. & Williamson, J. R. Quantitative mining of compositional
heterogeneity in cryo-EM datasets of ribosome assembly intermediates. Structure 30, 498–509.e4
(2022).
82.​ Forsberg, B. O., Shah, P. N. M. & Burt, A. A robust normalized local filter to estimate compositional
heterogeneity directly from cryo-EM maps. Nat Commun 14, 5802 (2023).
83.​ Levy, A. et al. Mixture of neural fields for heterogeneous reconstruction in cryo-EM. arXiv [cs.LG]
(2024) doi:10.48550/ARXIV.2412.09420.
84.​ Pearce, N. M. et al. A multi-crystal method for extracting obscured crystallographic states from
conventionally uninterpretable electron density. Nat Commun 8, 15123 (2017).
85.​ Mass spectrometry guided structural biology. Current Opinion in Structural Biology 40, 136–144
(2016).
86.​ Papasergi-Scott, M. M. et al. Time-resolved cryo-EM of G-protein activation by a GPCR. Nature 629,
1182–1191 (2024).
87.​ Punjani, A., Rubinstein, J. L., Fleet, D. J. & Brubaker, M. A. cryoSPARC: algorithms for rapid
unsupervised cryo-EM structure determination. Nat Methods 14, 290–296 (2017).
88.​ Wang, C., Mariani, V., Poitevin, F., Avaylon, M. & Thayer, J. End-to-end deep learning pipeline for
real-time Bragg peak segmentation: from training to large-scale deployment. Front. High Perform.
Comput. 3, 1536471 (2025).
89.​ Blaschke, J. P. et al. ExaFEL: extreme-scale real-time data processing for X-ray free electron laser
science. Front. High Perform. Comput. 2, 1414569 (2024).
90.​ Kimanius, D., Dong, L., Sharov, G., Nakane, T. & Scheres, S. H. W. New tools for automated
cryo-EM single-particle analysis in RELION-4.0. Biochem J 478, 4169–4185 (2021).
91.​ Aldama, L. A., Dalton, K. M. & Hekstra, D. R. Correcting systematic errors in diffraction data with
modern scaling algorithms. Acta Crystallogr D Struct Biol 79, 796–805 (2023).

92.​ Dalton, K. M., Greisman, J. B. & Hekstra, D. R. A unifying Bayesian framework for merging X-ray
diffraction data. Nat Commun 13, 7764 (2022).
93.​ Zheng, W. et al. Improving deep learning protein monomer and complex structure prediction using
DeepMSA2 with huge metagenomics data. Nat Methods 21, 279–289 (2024).
94.​ Cong, Q., Anishchenko, I., Ovchinnikov, S. & Baker, D. Protein interaction networks revealed by
proteome coevolution. Science 365, 185–189 (2019).
95.​ Arridge, S., Maass, P., Öktem, O. & Schönlieb, C.-B. Solving inverse problems using data-driven
models. Acta Numerica 28, 1–174 (2019).
96.​ Kinman, L. F., Powell, B. M., Zhong, E. D., Berger, B. & Davis, J. H. Uncovering structural
ensembles from single-particle cryo-EM data using cryoDRGN. Nat Protoc 18, 319–339 (2023).
97.​ Bonomi, M., Heller, G. T., Camilloni, C. & Vendruscolo, M. Principles of protein structural ensemble
determination. Curr Opin Struct Biol 42, 106–116 (2017).
98.​ Bonomi, M., Camilloni, C., Cavalli, A. & Vendruscolo, M. Metainference: A Bayesian inference
method for heterogeneous systems. Sci Adv 2, e1501177 (2016).
99.​ Boomsma, W., Ferkinghoff-Borg, J. & Lindorff-Larsen, K. Combining experiments and simulations
using the maximum entropy principle. PLoS Comput Biol 10, e1003406 (2014).
100.​Hummer, G. & Köfinger, J. Bayesian ensemble refinement by replica simulations and reweighting. J
Chem Phys 143, 243150 (2015).
101.​Bottaro, S. & Lindorff-Larsen, K. Biophysical experiments and biomolecular simulations: A perfect
match? Science 361, 355–360 (2018).
102.​Wankowicz, S. A. & Fraser, J. S. Comprehensive encoding of conformational and compositional
protein structural ensembles through the mmCIF data structure. IUCrJ 11, 494–501 (2024).
103.​Woldeyes, R. A., Sivak, D. A. & Fraser, J. S. E pluribus unum, no more: from one crystal, many
conformations. Curr Opin Struct Biol 28, 56–62 (2014).
104.​Riley, B. T. et al. qFit 3: Protein and ligand multiconformer modeling for X-ray crystallographic and
single-particle cryo-EM density maps. Protein Sci 30, 270–285 (2021).
105.​Shekhar, M. et al. CryoFold: determining protein structures and data-guided ensembles from

cryo-EM density maps. Matter 4, 3195–3216 (2021).
106.​Burnley, B. T., Afonine, P. V., Adams, P. D. & Gros, P. Modelling dynamics in protein crystal
structures by ensemble refinement. Elife 1, e00311 (2012).
107.​Song, J., Gomes, G.-N., Shi, T., Gradinaru, C. C. & Chan, H. S. Conformational Heterogeneity and
FRET Data Interpretation for Dimensions of Unfolded Proteins. Biophys J 113, 1012–1024 (2017).
108.​Ginn, H. M. Torsion angles to map and visualize the conformational space of a protein. Protein Sci
32, e4608 (2023).
109.​Lindorff-Larsen, K. & Ferkinghoff-Borg, J. Similarity measures for protein ensembles. PLoS One 4,
e4203 (2009).
110.​Borthakur, K., Sisk, T. R., Panei, F. P., Bonomi, M. & Robustelli, P. Determining accurate
conformational ensembles of intrinsically disordered proteins at atomic resolution. bioRxiv (2024)
doi:10.1101/2024.10.04.616700.
111.​Jeon, M. et al. CryoBench: Diverse and challenging datasets for the heterogeneity problem in
cryo-EM. (2024).
112.​Urzhumtsev, A. G., Urzhumtseva, L. M. & Lunin, V. Y. Direct calculation of cryo-EM and
crystallographic model maps for real-space refinement. Acta Crystallogr D Struct Biol 78, 1451–1468
(2022).
113.​Vögeli, B. The nuclear Overhauser effect from a quantitative perspective. Prog Nucl Magn Reson
Spectrosc 78, 1–46 (2014).
114.​Sami, S., Menger, M. F. S. J., Faraji, S., Broer, R. & Havenith, R. W. A. Q-Force: Quantum
Mechanically Augmented Molecular Force Fields. J Chem Theory Comput 17, 4946–4960 (2021).
115.​Unke, O. T. et al. Biomolecular dynamics with machine-learned quantum-mechanical force fields
trained on diverse chemical fragments. Sci Adv 10, eadn4397 (2024).
116.​Majewski, M. et al. Machine learning coarse-grained potentials of protein thermodynamics. Nat
Commun 14, 5739 (2023).
117.​Hénin, J., Lelièvre, T., Shirts, M. R., Valsson, O. & Delemotte, L. Enhanced sampling methods for
molecular dynamics simulations. arXiv [cond-mat.stat-mech] (2022)

doi:10.48550/ARXIV.2202.04164.
118.​Mehdi, S., Smith, Z., Herron, L., Zou, Z. & Tiwary, P. Enhanced Sampling with Machine Learning.
Annu Rev Phys Chem 75, 347–370 (2024).
119.​Noé, F., Olsson, S., Köhler, J. & Wu, H. Boltzmann generators: Sampling equilibrium states of
many-body systems with deep learning. Science 365, (2019).
120.​Watson, J. L. et al. De novo design of protein structure and function with RFdiffusion. Nature 620,
1089–1100 (2023).
121.​Abramson, J. et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3.
Nature 630, 493–500 (2024).
122.​Jing, B., Berger, B. & Jaakkola, T. AlphaFold Meets Flow Matching for Generating Protein
Ensembles. (2024).
123.​Yang, Z. et al. Scalable crystal structure relaxation using an iteration-free deep generative model
with uncertainty quantification. Nat Commun 15, 8148 (2024).
124.​Qiao, Z., Nie, W., Vahdat, A., Miller, T. F., III & Anandkumar, A. State-specific protein–ligand complex
structure prediction with a multiscale deep generative model. Nat. Mach. Intell. (2024)
doi:10.1038/s42256-024-00792-z.
125.​Novak, B., Lotthammer, J. M., Emenecker, R. J. & Holehouse, A. S. Accurate predictions of
conformational ensembles of disordered proteins with STARLING. bioRxiv (2025)
doi:10.1101/2025.02.14.638373.
126.​Janson, G. & Feig, M. Transferable deep generative modeling of intrinsically disordered protein
conformations. PLoS Comput Biol 20, e1012144 (2024).
127.​Wayment-Steele, H. K. et al. Predicting multiple conformations via sequence clustering and
AlphaFold2. Nature 625, 832–839 (2024).
128.​Schafer, J. W. et al. Sequence clustering confounds AlphaFold2. Nature 638, E8–E12 (2025).
129.​Li, M., Dalton, K. & Hekstra, D. SFCalculator: connecting deep generative models and
crystallography. bioRxiv (2025) doi:10.1101/2025.01.12.632630.
130.​Fadini, A. et al. AlphaFold as a Prior: Experimental Structure Determination Conditioned on a

Pretrained Neural Network. bioRxiv (2025) doi:10.1101/2025.02.18.638828.
131.​Stahl, K., Graziadei, A., Dau, T., Brock, O. & Rappsilber, J. Protein structure prediction with in-cell
photo-crosslinking mass spectrometry and deep learning. Nat Biotechnol 41, 1810–1819 (2023).
132.​Jamali, K. et al. Automated model building and protein identification in cryo-EM maps. Nature 628,
450–457 (2024).
133.​Levy, A. et al. Solving inverse problems in protein space using diffusion-based priors. arXiv [cs.LG]
(2024) doi:10.48550/ARXIV.2406.04239.
134.​Maddipatla, A. et al. Inverse problems with experiment-guided AlphaFold. arXiv [q-bio.BM] (2025)
doi:10.48550/ARXIV.2502.09372.
135.​Raghu, R., Levy, A., Wetzstein, G. & Zhong, E. D. Multiscale guidance of AlphaFold3 with
heterogeneous cryo-EM data. arXiv [cs.LG] (2025) doi:10.48550/ARXIV.2506.04490.
136.​Anfinsen, C. B. Principles that govern the folding of protein chains. Science 181, 223–230 (1973).
137.​Pitsawong, W. et al. Dynamics of human protein kinase Aurora A linked to drug selectivity. Elife 7,
(2018).
138.​Jin, M. et al. Dynamic allostery drives autocrine and paracrine TGF-β signaling. Cell 187,
6200–6219.e23 (2024).
139.​Broom, A. et al. Ensemble-based enzyme design can recapitulate the effects of laboratory directed
evolution in silico. Nat Commun 11, 4808 (2020).
140.​Rakotoharisoa, R. V. et al. Design of Efficient Artificial Enzymes Using Crystallographically
Enhanced Conformational Sampling. J Am Chem Soc 146, 10001–10013 (2024).
141.​Kretsch, R. C. et al. Functional relevance of CASP16 nucleic acid predictions as evaluated by
structure providers. bioRxiv (2025) doi:10.1101/2025.04.15.649049.
142.​Cheng, J. et al. Accurate proteome-wide missense variant effect prediction with AlphaMissense.
Science 381, eadg7492 (2023).
143.​Bludau, I. et al. The structural context of posttranslational modifications at a proteome-wide scale.
PLoS Biol 20, e3001636 (2022).
144.​Powell, B. M. & Davis, J. H. Learning structural heterogeneity from cryo-electron sub-tomograms

with tomoDRGN. Nat Methods 21, 1525–1536 (2024).
145.​Young, L. N. & Villa, E. Bringing Structure to Cell Biology with Cryo-Electron Tomography. Annu Rev
Biophys 52, 573–595 (2023).
146.​Markin, C. J. et al. Revealing enzyme functional architecture via high-throughput microfluidic enzyme
kinetics. Science 373, (2021).


---

# Benchmarking Generative AI and Physics-Based Molecular Simulation for Sampling Conformational Heterogeneity in T4 Lysozyme

**Authors:** Soumendranath Bhakat
**Year:** 2026
**Venue:** Journal of Chemical Information and Modeling
**DOI:** 10.1021/acs.jcim.6c02044
**Source PDF URL:** https://www.biorxiv.org/content/10.64898/2026.05.10.724101v1.full.pdf (bioRxiv preprint; JCIM version is closed access, oa_status=closed per OpenAlex)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Benchmarking generative AI and physics based molecular simulation for sampling
conformational heterogeneity in T4 Lysozyme
Soumendranath Bhakat
AlloTec Bio Inc., USA
Email: bhakatsoumendranath@gmail.com , sbhakat@allotec.bio

Abstract
Wild-type T4 lysozyme (T4L) is used as a benchmark to evaluate conformational sampling
across generative AI, AI-accelerated molecular simulation (AMS), and physics-based enhanced
molecular dynamics (EMD). A four-state model: exposed/open, exposed/closed, buried/open,
and buried/closed; is defined using physically meaningful collective variables. While generative
AI methods (AF-cluster, MSA subsampling of AlphaFold2, ConforFold, AlphaFlow, ESMFlow,
ConfRover, BioEmu) largely sample only the exposed/open state, AMS integrating generative
ensembles with iterative molecular dynamics, recovering all states and reproducing equilibrium
populations similar to EMD and experimental smFRET signatures.
Introduction
Proteins are molecular machines that govern biological function. They are not static structures
but interconvert between multiple transiently populated metastable states, each capable of
activating distinct signaling pathways. The populations of these states are modulated by
environmental perturbations such as temperature, pH, ligand binding, and mutations. Sampling
the transiently populated states is therefore central to understanding how proteins encode
function, yet it remains one of the hardest problems in structural biology(1–5).
The development of generative AI algorithms such as AlphaFold has enabled accurate prediction
of static protein structures from sequence alone, but these algorithms do not sample transiently
populated alternate conformational states. A growing subfield of machine learning for structural
biology has aimed to address this by predicting conformational ensembles from sequence
alone(1). These approaches fall into two subgroups: MSA-based methods, which perturb
evolutionary coupling information in multiple sequence alignments to generate structural
diversity, and generative models such as diffusion models or flow-matching frameworks, trained
on short MD simulations data, which claim to sample transiently populated alternate states.
Despite rapid growth in both subgroups, systematic benchmarking against physically rigorous
reference data remains absent, making it difficult to assess whether these methods genuinely
capture biologically relevant conformational diversity or simply reproduce structural noise.

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Physics-based enhanced sampling methods such as metadynamics(6–9), adaptive sampling(10),
and replica exchange(11) provide such a reference. They can sample transiently populated
alternate states and their relative populations across a diverse range of biomolecular systems.
Sampling efficiency is assessed by how well these methods capture state populations along
collective variables (CVs) that discriminate transient states from the ground state(12). However,
fair comparisons between physics-based enhanced sampling and generative AI methods are rare
due to three key challenges. An ideal benchmark system must have experimentally validated
transient states with CVs simple enough to distinguish those states from the ground state. It must
have sufficient structural data in the Protein Data Bank so that limited training data cannot be
used as a confounding factor. And system size must not unfairly disadvantage generative AI
methods, which often struggle with larger and more conformationally complex systems.
Wild-type T4 lysozyme (T4L) satisfies all three criteria. It is small (164 residues), has singlemolecule FRET (smFRET) data that directly validates transiently populated alternate states, and
has been extensively studied by physics-based enhanced sampling methods. Yet, no prior study
has systematically compared generative AI methods, AI-accelerated molecular simulation, and
physics-based enhanced sampling on the same system using well characterized CVs. We close
this gap here.
Results
We used two sets of CVs to describe the conformational ensemble of T4L. The first is a twodimensional CV defined by two C distances: d1 (Ser44–Ile150) and d2 (Glu22–Gln141). The
Ser44–Ile150 pair was used in smFRET experiments to probe the opening and closing motion of
T4L, with d1  2.5 nm defining the closed state and d1  2.5 nm defining the open state. The
Glu22–Gln141 distance serves as an orthogonal CV capturing hinge domain motion. The second
CV is the locking coordinate , developed by Stock and co-workers(13), which quantifies the
solvent exposure of Phe4 relative to the hinge helix (see Supplementary Information for full
definition). A positive value (  0) indicates that Phe4 is solvent-exposed, while a negative
value (  0) indicates it is buried within the interdomain interface. Combined with d1, this
defines a four-state model: exposed/closed, exposed/open, buried/closed, and buried/open. This
four-state classification enables quantitative comparison of state populations across all methods.
We benchmarked three classes of methods. The first class comprises generative AI approaches,
divided into two subgroups. The first subgroup consists of MSA-based methods: AF-cluster(14),
which clusters MSA subsamples as input to AlphaFold2(15); reduced MSA subsampling with
AlphaFold2 (rMSA-AF2)(16); and ConforFold(17), a retrained OpenFold2 model designed to
predict alternate conformations. The second subgroup consists of generative models trained on
structural or simulation data: AlphaFlow(18), ESMFlow(18), ConfRover(19), and BioEmu(20).
The second class is AI-accelerated molecular simulation (AMS), a methodological contribution
of this work, in which generative AI ensembles seed multiple rounds of unbiased MD

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

simulations that are combined using a Markov state model (MSM)(21, 22) to recover physically
refined state populations (Figure 1). The third class is physics-based enhanced sampling
repurposed from Miller and co-workers(23), combining 5 µs unbiased MD simulations with
metadynamics-seeded unbiased MD simulations (hereafter enhanced molecular dynamics,
EMD), which serves as the quantitative reference for all comparisons.

Figure 1. Schematic of the AI-accelerated molecular simulation (AMS) workflow. The workflow begins
with the T4L sequence, followed by ensemble generation using multiple generative AI methods,
including AF-cluster, ConforFold, BioEmu, ConfRover, ESMFlow, and AlphaFlow. K-center clustering
was then performed using transformed distance features to select an initial “starting ensemble”
of N=100 structures. Unbiased molecular dynamics simulations of 200 ns were initiated from each
member of this starting ensemble in Round 1. The resulting trajectories were clustered using the K-center
algorithm on transformed distances, yielding a “physics-refined ensemble” of N=80 structures. Additional
unbiased molecular dynamics simulations of 200 ns each were then initiated from the physics-refined
ensemble in Round 2. A Markov state model (MSM) was constructed using RMSD features from the
combined Round 1 and Round 2 simulations. Equilibrium populations were then projected onto different
collective variables to predict conformational populations and heterogeneity in T4L.

AMS successfully sampled all four conformational states: exposed/open, exposed/closed,
buried/open, and buried/closed. The two dominant states, exposed/open (AMS: 38.3%, EMD:
39.1%) and buried/open (AMS: 58.7%, EMD: 54.0%), were recovered with relative populations
comparable to EMD. The transiently populated buried/closed state was also recovered with a
comparable population (AMS: 2.3%, EMD: 2.9%). The exposed/closed state, however, was

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

underrepresented in AMS relative to EMD (AMS: 0.7%, EMD: 3.9%), suggesting that this
particular transient state remains the most challenging to access without explicit enhanced
sampling to seed follow up unbiased simulations (Figure 2).
In contrast, generative AI ensembles alone remained predominantly trapped in the exposed/open
state, failing to access the transiently populated closed and buried states. Projection of generative
AI ensembles onto the d1 and d2 CV space revealed that AF-cluster provided substantially
broader conformational coverage than all other generative AI methods (Figure 3). This suggests
that the enhanced sampling efficiency of AMS is predominantly driven by the ability of AFcluster to populate high-energy intermediate structures that serve as productive seeds for
subsequent MD simulation. To test this hypothesis directly, we repeated the AMS protocol with
AF-cluster excluded from the initial ensemble. The resulting simulations failed to recover the
conformational heterogeneity captured by the full AMS protocol (Figure S1, Supporting
Information).

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Figure 2. Collective variables used to characterize T4 lysozyme conformational heterogeneity and
comparison
of
sampling
across
different
approaches. A: Pictorial
representation
of
the d1 and d2 collective variables, defined as the Cα–Cα distances between Ser44 (S44) and Ile150 (I150)
and between Glu22 (E22) and Gln141 (Q141), respectively. The d1 coordinate distinguishes closed and
open conformations, with d1<2.5nm corresponding to the closed state and d1>2.5nm corresponding to
the open state. B: Definition of the locking coordinate p, which describes the position of the Phe4 (F4)
side chain relative to the hydrophobic cavity. The cavity direction is defined by the Cα atoms
of Lys60 and Phe67, while the position of Phe4 is represented by the center of mass of the carbon atoms
in its phenyl ring. Positive values of p indicate that the Phe4 side chain is solvent-exposed, whereas
negative values indicate that it is buried within the hydrophobic cavity. C–E: Comparison of
conformational sampling by AMS, EMD, and generative AI ensembles alone. AMS and EMD sample the
full spectrum of conformational heterogeneity, whereas the combined generative AI ensembles
predominantly sample a single state. F: Superposition of crystal T4 lysozyme structure shown in dark
gray with representative exposed/closed and buried/closed conformations shown in magenta and blue,

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

respectively. The comparison highlights conformational changes involving Ser44 and Phe4, which
contribute to the observed conformational heterogeneity.

Figure 3. MSM-weighted free-energy landscapes projected onto different collective variables compare
conformational sampling by the AMS and EMD approaches. The upper panels show equilibrium
populations projected along the d1 and d2 collective variables, indicating that both AMS and EMD sample
the closed state of T4 lysozyme, defined by d1 < 2.5 nm. The black dotted line marks the closed–open
boundary at d1 = 2.5 nm. The lower panels show the projection of the locking coordinate p along d1,
demonstrating that both AMS and EMD sample conformations with exposed and buried Phenylalanine 4
side-chain states, corresponding to p > 0 and p < 0, respectively, across both closed and open T4
lysozyme conformations. Data points from the generative AI ensembles are projected onto the physicsrefined free-energy surfaces to assess the conformational coverage of each method. Among the generative
AI approaches, AF-cluster samples a substantially broader conformational landscape than the other
methods.

To further validate AMS against experiment, we computed the MSM-weighted smFRET
distance distribution for the Ser44–Ile150 pair and compared it directly with experimental

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

measurements (Figure S2 in Supporting Information). AMS recovered the transiently populated
closed state in quantitative agreement with experiment. This result is significant because the
EMD simulations of Miller and co-workers(23) were explicitly seeded with the objective of
sampling the closed state using enhanced sampling, yet AMS achieved comparable recovery of
this rare state starting from unbiased MD alone. The ability to reproduce an experimentally
observable transiently populated conformation without prior knowledge of the target state
demonstrates that AMS can access rare conformational events that are inaccessible to generative
AI methods alone.
Conclusions
This work introduces T4L as a community benchmark for evaluating methods that claim to
capture conformational heterogeneity. T4L is uniquely suited to this role: its experimentally
validated transient states, well characterized CVs, and extensive structural coverage in the
Protein Data Bank collectively eliminate the confounding factors that have hampered fair
comparisons in the field. The four-state classification framework presented here provides a
transferable, physically interpretable scoring scheme that can be applied consistently across any
method that generates structural ensembles.
The results presented here draw a clear boundary between what generative AI can and cannot do
in its current form. Majority of the generative AI methods alone reproduce the dominant ground
state (except AF-cluster which samples multiple high energy transient states) but fail to sample
transiently populated closed state in T4L and their relative populations. AMS, by using
generative AI ensembles as seeds rather than as end products, recovers the full conformational
landscape with populations that are quantitatively comparable to those from physics-based
enhanced sampling. Two rounds of unbiased MD simulation, initiated from generative AI
derived starting structures, were sufficient to achieve this. This is a practically important result:
AMS requires no knowledge of the target state and no enhanced sampling bias, yet it matches the
performance of the EMD protocol that was explicitly designed to find the closed state. Further,
the seeding strategy that combines all the conformational ensembles generated by different
generative AI algorithms alleviates the limitations of each one of them and provides a much
wider distribution of conformations as initial seeds, which accelerates sampling when combined
with physics-based molecular simulations
Looking forward, T4L and the benchmarking framework established here are well-positioned to
evaluate the next generation of hybrid methods. These include generative AI-seeded weighted
ensemble simulations(24), inference-time enhanced sampling approaches such as BoltzMetaDiffusion(25), and related methods that either combine generative AI with physics-based
sampling protocols or bias the generative process during inference to access alternate states. The
framework is equally applicable to MSA subsampling strategies applied to newer versions of
foundation models such as AlphaFold3(26) and OpenFold3(27), where the impact of richer

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

training data and improved architecture on conformational diversity remains an open question.
As these methods mature, rigorous benchmarking against experimentally validated populations
along physically meaningful CVs will be essential to distinguish genuine advances in
conformational sampling from improvements in ground-state structure prediction. T4L, with its
tractable size, rich experimental data, and well-defined conformational heterogeneity, provides
the ideal system for that purpose.

Methods
Ensemble generation
Structural ensembles of T4 lysozyme (T4L) were generated from the wild-type T4L sequence
using multiple generative AI-based approaches, as summarized in Table 1. The input amino acid
sequence
used
for
all
methods
was:

MNIFEMLRIDEGLRLKIYKDTEGYYTIGIGHLLTKSPSLNAAKSELDKAIGRNCNGVITKDEAE
KLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRCALINMVFQMGETGVAGFTNSLRMLQQKRWDE
AAVNLAKSRWYNQTPNRAKRVITTFRTGTWDAYKNL
The generated ensembles included both multiple-sequence-alignment-based approaches and
generative models trained to produce conformationally diverse protein structures. For each
method, the number of generated structures and the corresponding codebase or implementation
are listed in Table 1. All structures generated across these methods were pooled into a combined
generative AI ensemble for subsequent transformed-distance analysis, dimensionality reduction,
and clustering.
Table 1. Generative AI methods used for T4L ensemble generation, number of generated
structures, and corresponding codebase or implementation.
Methods
AF-cluster
AlphaFlow

Number of
structures

ConforFold
ConfRover
ESMFlow

BioEmu
rMSA-AF2
rMSA-AF2recyc

Codebase/implementation
https://github.com/HWaymentSteele/AF_Cluster
https://github.com/bjing2016/alphaflow
(model: AlphaFlow-MD)
https://github.com/strauchlab/ConforFold
https://github.com/ByteDance-Seed/ConfRover
https://github.com/bjing2016/alphaflow
(model: ESMFlow-MD)
https://github.com/microsoft/bioemu
Colabfold (MSA: 8:16, num_recycles=6)
AlphaFold2_advanced_v2
(MSA:
8:16,
num_recycles=3)

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

Definitions of collective variables
The opening and closing motion of T4 lysozyme was characterized using the Cα–Cα distance
between Ser44 and Ile150, denoted as d1. Conformations with d1 < 2.5 nm were classified as
closed, whereas conformations with d1> 2.5 nm were classified as open. A second Cα–Cα
distance, measured between Glu22 and Gln141 and denoted as d2, was used as an orthogonal
projection coordinate to describe hinge-domain motion, following the collective-variable
definition proposed by Abou-Hatab and Abrams(28).
The solvent exposure of Phe4 was quantified using the locking coordinate, p. For each trajectory
frame, p was calculated by projecting the vector from the Cα atom of Phe67 to the center of the
Phe4 phenyl ring onto the vector connecting the Cα atoms of Lys60 and Phe67. The center of the
Phe4 phenyl ring was defined as the geometric center of the CG, CD1, CD2, CE1, CE2, and CZ
carbon atoms. The locking coordinate was computed as



 ,    ,
  ,  

where  ,  is the vector from the Lys60 Cα atom to the Phe67 Cα atom, and  , is the vector
from the Phe67 Cα atom to the center of the Phe4 phenyl ring. Positive values of p (p > 0)
indicate that the Phe4 side chain is solvent-exposed, whereas negative values indicate that the
side chain is buried (p < 0) within the hydrophobic cavity.
Feature selection, dimensionality reduction and clustering
To construct a distance-based representation of conformational variability, structures generated
by the different generative AI methods were first pooled into a single all-atom ensemble. For
every structure in this combined ensemble, all Cα–Cα pairwise distances were converted into
continuous contact-like variables using a smooth switching function, following Bhakat et al(29).

 





decay

defines the distance scale over which the contact
Here,  denotes the Cα–Cα distance, 
changes from formed to broken, and  controls the steepness of this transition. Distances much
shorter than 
produce values close to 1, corresponding to a formed contact, whereas
distances much longer than 
produce values close to 0, corresponding to a broken contact.

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

This transformation replaces raw distances with a smooth and noise-tolerant measure of contact
 0.90 nm and   6.
strength. We used 
The same distance-to-contact transformation was used at two stages of the workflow. First, it
was applied to the combined generative AI ensemble to identify structurally diverse starting
conformations for molecular simulation. Second, after the unbiased molecular dynamics
simulations were completed, the resulting trajectories were processed using the same
transformed-distance representation to identify conformations for the physics-refined ensemble.
Thus, both the initial generative AI predicted structures and the MD-derived conformations were
analyzed in a common feature space.
For each Cα–Cα pair, the transformed contact values were evaluated across the relevant
structural dataset, either the pooled generative AI ensemble or the post-processed simulation
trajectories. Contacts were retained only if they showed evidence of both formation and
disruption, according to the criterion:

  0.4 and    0.6.
This filtering step removes distance pairs that remain essentially unchanged, either always
formed or always broken, and keeps only contacts that report meaningful conformational
rearrangements. In this representation, values of   0.6 correspond to formed contacts,
values of   0.4 correspond to broken contacts, and intermediate values describe partially
formed or fluctuating contacts.
The filtered set of transformed distance features was then used for dimensionality reduction with
Slow Feature Analysis (SFA), as introduced for biomolecular simulation data by Vats et al(30).
SFA identifies linear combinations of input features that change slowly over time, thereby
emphasizing collective motions associated with long-timescale conformational rearrangements.
For an input signal  , SFA generates output coordinates     by minimizing
temporal variation:

Δ  "#  $
Applied to the transformed Cα–Cα contact features, SFA identified the slowest collective
distance patterns that distinguish conformationally heterogeneous regions of T4 lysozyme. The
first two slow features were used as the reduced feature space for K-center clustering(31).
Cluster centers selected from the combined generative AI ensemble were saved as PDB
structures and used as starting points for the first round of molecular dynamics simulations. The
same procedure was subsequently applied during post-processing of the simulation trajectories to

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

select the physics-refined ensemble for the next round of simulations. SFA and K-center
clustering
were
performed
using
the
MDML
software
package
(GitHub: https://github.com/svats73/mdml/tree/main)
Molecular dynamics simulations
Each selected structure from starting ensemble or physics-refined ensemble was prepared using
the tleap module in Amber2022(32, 33), following the general simulation protocol described by
Meller et al(34). Protein atoms were parameterized with the AMBER ff14SB(35) force field. Each
system was neutralized with the appropriate counterions and solvated in a truncated-octahedron
box of TIP3P water molecules, with a minimum distance of 10 Å between any protein atom and
the edge of the simulation box.
Energy minimization was carried out in two steps. First, solvent molecules and ions were
minimized while harmonic restraints were applied to the protein atoms using a force constant of
100 kcal mol¹ Å². This was followed by an unrestrained minimization of the full solvated
system. The resulting Amber topology and coordinate files were then converted
to GROMACS format using Acpype(36), and all subsequent equilibration and production
simulations were performed using GROMACS 2022(37).
Systems were gradually heated from 0 to 300 K over 500 ps in the NVT ensemble while
applying positional restraints to backbone heavy atoms with a force constant of 500 kJ mol¹
nm². After heating, each system was equilibrated for 200 ps in the NPT ensemble at 300 K and
1 bar without positional restraints. Temperature was maintained using the velocity-rescale
thermostat, and pressure was controlled using the Parrinello–Rahman barostat(38).
Unbiased production simulations were then performed in the NPT ensemble using a 2 fs
integration time step. Nonbonded interactions were treated with a 1.0 nm cutoff, long-range
electrostatics were calculated using the particle-mesh Ewald method(39), and bonds involving
hydrogen atoms were constrained using the LINCS(40) algorithm. Production trajectories were
initiated from the SFA selected cluster centers and ran for 200 ns each, with coordinates saved
every 10 ps.
Enhanced Molecular Dynamics simulations
The molecular dynamics simulations used in this study were adapted from Miller et al(23).
Briefly, the dataset comprises a 5 μs unbiased MD trajectory, which did not sample the open-toclosed conformational transition. To drive the transition, the authors applied a metadynamics
bias along the Cα–Cα distance between Ser44 and Ile150, extracted snapshots along the resulting
free-energy pathway, and launched short unbiased MD simulations from each. For our analysis,

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

we did not use the metadynamics trajectories themselves; instead, we combined the 5 μs
unbiased trajectory with the short unbiased simulations seeded along the biased pathway.
Markov state model
Markov state models (MSMs) were constructed using the PyEMMA(41) package with RMSDbased featurization of both AMS and EMD trajectories. K-means clustering (K = 200) was
employed to discretize conformational space, and state populations were computed across
multiple lag times to assess convergence and compare the relative equilibrium distributions of
AMS and EMD ensembles (Figure S3 and S4 in Supporting Information).
smFRET prediction
smFRET prediction was carried
out using Enspara(42) software package
(https://enspara.readthedocs.io/en/latest/smFRET.html ). Trajectories from AMS were featurized
by transformed distances followed by SFA (as described in “Feature selection, dimensionality
reduction and clustering” subsection) followed by K-means clustering with k=500. smFRET was
predicted using the protocol described by Miller et al(23).
Competing interests
Authors declares no conflict of interests.
Acknowledgements
The author thanks Justin J. Miller of the University of Pennsylvania for performing the smFRET
calculations and providing the dataset corresponding to the EMD simulations. Further
acknowledgement goes to Prof. Eva M. Strauch and Dr. Raulia Syrlybaeva of Washington
University in St. Louis for providing the ConforFold ensemble, and to Shray Vats of Boston
University for providing the ConfRover ensemble.
Data availability
Generative AI ensembles, closed states of T4L and codes to calculate the distance, RMSD and
locking co-ordinate can be accessed here: https://doi.org/10.5281/zenodo.20111229
References
1.
2.

A. Aranganathan, X. Gu, D. Wang, B. P. Vani, P. Tiwary, Modeling Boltzmann-weighted structural
ensembles of proteins using artificial intelligence–based methods. Curr. Opin. Struct. Biol. 91, 103000
(2025).
A. P. Kornev, S. S. Taylor, Dynamics-Driven Allostery in Protein Kinases. Trends Biochem. Sci. 40, 628–647
(2015).

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

3.
4.
5.
6.
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
18.
19.
20.
21.
22.
23.
24.
25.
26.
27.
28.

N. R. Latorraca, A. J. Venkatakrishnan, R. O. Dror, GPCR Dynamics: Structures in Motion. Chem. Rev. 117,
139–155 (2017).
D. R. Livesay, Protein dynamics: dancing on an ever-changing free energy stage. Curr. Opin. Pharmacol.
[Preprint] (2010).
J. Guo, H.-X. Zhou, Protein Allostery and Conformational Dynamics. Chem. Rev. 116, 6503–6515 (2016).
A. Barducci, M. Bonomi, M. Parrinello, Metadynamics. WIREs Computational Molecular Science 1, 826–843
(2011).
A. Barducci, G. Bussi, M. Parrinello, Well-Tempered Metadynamics: A Smoothly Converging and Tunable
Free-Energy Method. Phys. Rev. Lett. 100, 20603 (2008).
P. Tiwary, M. Parrinello, From Metadynamics to Dynamics. Phys. Rev. Lett. 111, 230602 (2013).
G. Bussi, A. Laio, Using metadynamics to explore complex free-energy landscapes. Nature Reviews Physics
2, 200–212 (2020).
M. I. Zimmerman, G. R. Bowman, FAST Conformational Searches by Balancing Exploration/Exploitation
Trade-Offs. J. Chem. Theory Comput. 11, 5747–5757 (2015).
P. Liu, B. Kim, R. A. Friesner, B. J. Berne, Replica exchange with solute tempering: A method for sampling
biological systems in explicit water. Proceedings of the National Academy of Sciences 102, 13749–13754
(2005).
S. Bhakat, Collective variable discovery in the age of machine learning: reality, hype and everything in
between. RSC Adv. 12, 25010–25024 (2022).
M. Ernst, S. Wolf, G. Stock, Identification and Validation of Reaction Coordinates Describing Protein
Functional Motion: Hierarchical Dynamics of T4 Lysozyme. J. Chem. Theory Comput. 13, 5076–5088 (2017).
H. K. Wayment-Steele, et al., Predicting multiple conformations via sequence clustering and AlphaFold2.
Nature 625, 832–839 (2024).
J. Jumper, et al., Highly accurate protein structure prediction with AlphaFold. Nature 596, 583–589 (2021).
D. del Alamo, D. Sala, H. S. Mchaourab, J. Meiler, Sampling alternative conformational states of
transporters and receptors with AlphaFold2. Elife 11, e75751 (2022).
R. Syrlybaeva, E.-M. Strauch, ConforFold recovers alternative protein conformations beyond MSA
subsampling. Protein Science 35, e70564 (2026).
B. Jing, B. Berger, T. Jaakkola, AlphaFold Meets Flow Matching for Generating Protein Ensembles. ArXiv
(2024). https://doi.org/https://doi.org/10.48550/arXiv.2402.04845.
Y. Shen, et al., ConfRover: Simultaneous Modeling of Protein Conformation and Dynamics via
Autoregression. arXiv preprint arXiv:2505.17478 (2025).
S. Lewis, et al., Scalable emulation of protein equilibrium ensembles with generative deep learning. Science
(1979). 389, eadv9817 (2026).
B. E. Husic, V. S. Pande, Markov State Models: From an Art to a Science. J. Am. Chem. Soc. 140, 2386–2396
(2018).
V. S. Pande, K. Beauchamp, G. R. Bowman, Everything you wanted to know about Markov State Models but
were afraid to ask. Methods 52, 99–105 (2010).
J. J. Miller, et al., Accounting for Fast vs Slow Exchange in Single Molecule FRET Experiments Reveals
Hidden Conformational States. J. Chem. Theory Comput. 20, 10339–10349 (2024).
L. Otten, J. M. Leung, L. T. Chong, D. M. Zuckerman, Rectifying AI-generated protein structure ensembles
for equilibrium using physics-based computations. bioRxiv 2026.03.24.714034 (2026).
https://doi.org/10.64898/2026.03.24.714034.
H. Y. I. Lam, et al., Metadiffusion: inference-time meta-energy biasing of biomolecular diffusion models.
bioRxiv 2026.02.10.704873 (2026). https://doi.org/10.64898/2026.02.10.704873.
Y. Kalakoti, B. Wallner, AFsample3: Generating and selecting multiple conformational states with
Alphafold3. bioRxiv 2026.01.16.699904 (2026). https://doi.org/10.64898/2026.01.16.699904.
M. Lee, et al., ConforNets: Latents-Based Conformational Control in OpenFold3. arXiv preprint
arXiv:2604.18559 (2026).
S. Abou-Hatab, C. F. Abrams, Minimal Collective Variables for Conformational Transitions in Steered and
Temperature-Accelerated MD Simulations: A T4 Lysozyme Case Study. J. Phys. Chem. B 129, 5176–5188
(2025).

bioRxiv preprint doi: https://doi.org/10.64898/2026.05.10.724101; this version posted May 13, 2026. The copyright holder for this preprint
(which was not certified by peer review) is the author/funder, who has granted bioRxiv a license to display the preprint in perpetuity. It is made

29.
30.
31.
32.
33.
34.
35.
36.
37.
38.
39.
40.
41.
42.

S. Bhakat, S. Vats, A. Mardt, A. Degterev, Generalizable Protein Dynamics in Kinases: Physics is the key.
bioRxiv 2025.03.06.641878 (2025). https://doi.org/10.1101/2025.03.06.641878.
S. Vats, R. Bobrovs, P. Söderhjelm, S. Bhakat, AlphaFold-SFA: Accelerated sampling of cryptic pocket
opening, protein-ligand binding and allostery by AlphaFold, slow feature analysis and metadynamics. PLoS
One 19, e0307226 (2024).
T. F. Gonzalez, Clustering to minimize the maximum intercluster distance. Theor. Comput. Sci. 38, 293–306
(1985).
D. A. Case, et al., Amber 2022, University of California, San Francisco. (2022).
R. Salomon-Ferrer, D. A. Case, R. C. Walker, An overview of the Amber biomolecular simulation package.
WIREs Computational Molecular Science 3, 198–210 (2013).
A. Meller, S. Bhakat, S. Solieva, G. R. Bowman, Accelerating Cryptic Pocket Discovery Using AlphaFold. J.
Chem. Theory Comput. 19, 4355–4363 (2023).
J. A. Maier, et al., ff14SB: Improving the Accuracy of Protein Side Chain and Backbone Parameters from
ff99SB. J. Chem. Theory Comput. 11, 3696–3713 (2015).
A. W. Sousa da Silva, W. F. Vranken, ACPYPE - AnteChamber PYthon Parser interfacE. BMC Res. Notes 5,
367 (2012).
M. J. Abraham, et al., GROMACS: High performance molecular simulations through multi-level parallelism
from laptops to supercomputers. SoftwareX 1–2, 19–25 (2015).
M. Parrinello, A. Rahman, Polymorphic transitions in single crystals: A new molecular dynamics method. J.
Appl. Phys. 52, 7182–7190 (1981).
T. Darden, D. York, L. Pedersen, Particle mesh Ewald: An N⋅log(N) method for Ewald sums in large systems.
J. Chem. Phys. 98, 10089–10092 (1993).
B. Hess, H. Bekker, H. J. C. Berendsen, J. G. E. M. Fraaije, LINCS: A linear constraint solver for molecular
simulations. J. Comput. Chem. 18, 1463–1472 (1997).
M. K. Scherer, et al., PyEMMA 2: A Software Package for Estimation, Validation, and Analysis of Markov
Models. J. Chem. Theory Comput. 11, 5525–5542 (2015).
J. R. Porter, M. I. Zimmerman, G. R. Bowman, Enspara: Modeling molecular ensembles with scalable data
structures and parallel computing. J. Chem. Phys. 150, 44108 (2019).


---

# Are We Capturing the Ensemble?

**Authors:** Minhuan Li, F. Emil Thomasen, Pilar Cossio
**Year:** 2026
**Venue:** Reciprocal Space Station (RS Station) blog
**Source URL:** https://rs-station.github.io/2026/08/31/are-we-capturing-the-ensemble.html
**Date converted:** 2026-09-11

Derived from the blog post page; the live web page is the source of record.

---

*31 Aug 2026*

### What structural biology experiments preserve, blur, or discard about molecular distributions

Minhuan Li, F. Emil Thomasen, Pilar Cossio — {minhuanli,fthomasen,pcossio}@flatironinstitute.org

*Figure: Two ways in which an experiment can encode a conformational ensemble. Ensemble-averaged measurements combine contributions from many molecules into each observable. In single-particle measurements, each observation arises from an individual molecule, and the ensemble is represented statistically across many observations.*

Structural biology is increasingly being asked to answer questions about ensembles rather than single structures. But two opposite intuitions can lead us astray. In cryo-electron microscopy (cryo-EM), a fuzzy or weak region of a reconstructed map is sometimes treated as if it were direct evidence of an ensemble: blur becomes heterogeneity. In the other direction, an experiment such as X-ray diffraction may be dismissed as incapable of constraining an ensemble because its measurements average over many molecules.

These intuitions seem contradictory, but they make the same mistake. Both assume what an experiment can tell us about a molecular distribution from the appearance of its final representation, rather than from how the data were generated or processed. A blurred map is not itself an ensemble distribution. But neither does averaging an observable necessarily collapse a distribution to a single structure.

The more useful question is therefore not whether a dataset "contains an ensemble". It is which differences between molecular distributions remain observable after measurement and subsequent data processing. Two distinct ensembles may produce measurably different signals, or they may become indistinguishable once corrupted by experimental noise, limited by partially projected observables or finite sampling, nuisance variables, or distorted by data processing steps.

To make this precise, we first need to distinguish the distribution we ideally would like to learn from the one the experiment actually sees.

### What distribution enters the experiment?

Before asking what information the measurement pipeline preserves, we should first be clear about what distribution is being measured. Let p_target(x) denote a molecular distribution relevant to the scientific question, and p_src(x) the source distribution actually present in the prepared sample when the measurement is made. We refer to p_src as the molecular **ensemble distribution**—the distribution we can, in principle, attempt to measure and infer. Often we hope that p_src faithfully represents p_target, but the two need not be identical.

The distinction is especially concrete in cryo-EM, where vitrification is itself a physical process acting on the ensemble. Recent work by Clark et al. examined how rapid cooling can perturb conformational populations and how equilibrium populations might subsequently be inferred from the vitrified ensemble [6]. More generally, temperature, chemical environment, sample preparation, and experimental timescales can all affect the relationship between the distribution of biological interest and the one presented to the instrument.

The possible difference between p_target and p_src is important, but it is not the problem we will pursue here. We will take the source distribution as the object presented to the experiment and ask what happens next:

p_src → measurements → processed data.

Which distinctions within p_src survive this chain?

### How experiments constrain the source distribution

Different experiments encode p_src in different ways. Broadly, there are two cases. In an ensemble-averaged measurement, each observable combines contributions from many molecules. In a single-molecule measurement, individual observations arise from individual molecules, and the distribution appears statistically across many observations. These are not rankings of how much "ensemble information" an experiment contains. They are different ways of gaining information about the underlying distribution.

For an ensemble-average measurement, in its simplest form, the observable can be written as

y = ∫ m(x, z) π(z) p_src(x) dx dz + ε,

where m(·) is the forward model for the observable, z collects experimental nuisance variables (for example molecule poses) with distribution π(z), and ε represents measurement uncertainty. The experiment doesn't measure the observable for any individual molecule. Instead, it reports the expectation value of that observable over the source distribution and the nuisance variables.

Importantly, averaging in **observable space** is not the same as averaging in **conformational space**. Suppose two conformations, x_A and x_B, occur with probabilities p_A and p_B. Suppressing the nuisance variables, the measured signal is p_A m(x_A) + p_B m(x_B), not, in general, m(p_A x_A + p_B x_B). This distinction matters. If the observable responds differently to the two conformations, their contributions can remain separately constrained even though the measurement averages over many molecules. X-ray diffraction intensities, for example, need not correspond to a fictitious structure halfway between two populated conformations. Spatially distinct states can leave distinct contributions to the measured density. "Averaged" therefore does not mean "only informative about an average structure."

Single-particle experiments preserve a different kind of information. We can describe an individual observation as arising from a latent molecular state,

x_n ~ p_src(x),

together with experimental nuisance variables z_n, followed by a measurement process described by the distribution K,

y_n ~ K(· | x_n, z_n).

In single-molecule FRET, time traces of the same molecule can reveal transitions between coarse conformational states. In single-particle cryo-EM, time is not preserved: each particle contributes a noisy projection of one molecular configuration, and the ensemble appears through variation across many different particles.

For independent observations, their marginal distribution is

p(y) = ∫ K(y | x, z) π(z) p_src(x) dz dx.

Compared with ensemble-averaged experiments, single-particle experiments reports individual samples from this marginal distribution instead of the expectation value of some observables. Because molecule-to-molecule variation has not been collapsed immediately into a small set of ensemble averages, such data can in principle retain rich information about heterogeneity. But molecule-resolved does not mean that the underlying distribution is directly observed. Noise, unknown nuisance variables, limited sampling, and the magnitude and diversity of conformational variation can make distinct molecular states difficult—or impossible—to distinguish.

The important point is therefore not that one class of experiment "measures ensembles" while the other does not. Both impose constraints on p_src, but they preserve different types and levels of distinctions within it.

A next key question is what happens in the downstream analysis: to what extent does subsequent data processing preserve the information encoded in p_src?

### How processing can wash out the source distribution

The physical measurement is not the end of the information chain. Raw observations are subsequently selected, transformed, clustered or averaged, into representations used for interpretation and inference. These operations may be essential for extracting useful signal, but they can also change which information about p_src remains accessible downstream.

Cryo-EM provides a clear example. The standard reconstruction pipeline filters particles, estimates their poses, separates or models heterogeneity, and combines many observations into three-dimensional reconstructions. These steps are often necessary for recovering high-resolution structural detail. But particle filtering can remove observations, classification can partition continuous variation into discrete groups, and a consensus reconstruction can combine heterogeneous particles into a single representation. Information about the populations and variation present across the original particles may therefore no longer be recoverable from the reconstructed map alone.

Processing does not change the physical p_src that generated the observations. **But it changes what information about that distribution survives in the representation we choose to analyze.** Ensemble information can therefore be lost at two stages: when the source distribution is converted into measurements, and again when those measurements are converted into processed data. Understanding what ensemble information is washed out in an experiment requires following that information through the entire pipeline.

### The question of ensemble resolution

Just as spatial resolution asks when nearby features blur together, we can ask when two source distributions become indistinguishable after passing through the measurement and processing pipeline. We suggest *ensemble resolution* to refer to this question: which differences between molecular distributions remain distinguishable, given the uncertainty of the data and the transformations applied to them?

The analogy to spatial resolution is useful, but it only goes so far. Ensembles can differ in more than one way, so there is no reason to expect a single number to summarize their resolution. Two distributions might contain the same major conformations but assign them different populations; one might contain a rare state absent from the other; or they might show similar fluctuations individually but differ in how those motions are correlated. A dataset may distinguish one of these differences while being nearly blind to another. What can be resolved therefore depends not only on the experiment, but also on what aspect of the distribution we are asking it to distinguish.

Cryo-EM makes the distinction between spatial and ensemble resolution especially concrete. **A reconstruction can gain spatial resolution while losing ensemble resolution.** Moreover, weak or fuzzy density should not, by itself, be interpreted as an ensemble. Such density can have many sources, including experimental uncertainty. But even if the blur genuinely comes from conformational heterogeneity, **heterogeneity alone does not specify a distribution**. The same diffuse density could arise from different sets of conformations, populations, or correlated motions across the particles.

In a more controlled inference setting, we are beginning to see how the question of ensemble resolution can be formalized. Ensemble reweighting, for example, starts from a specified set of candidate conformations and asks how experimental measurements constrain their populations. Once the possible states are fixed, one can ask more precisely which differences in population are supported by a given set of measurements and their uncertainties [7]. General ensemble inference is harder: both the conformations themselves and their probabilities may be unknown. How to characterize ensemble resolution in that setting remains a much broader open problem.

### The takeaway

Before arguing for an ensemble-inference method, ask how the data were generated, what transformations they underwent, and which distinctions within the source distribution remain observable. An averaged measurement can still constrain multiple states; a molecule-resolved experiment does not make the ensemble directly visible; and a high-resolution reconstruction may preserve less population information than the observations from which it was built.

Thinking in terms of ensemble resolution shifts the question from whether an experiment "contains an ensemble" to a more useful one: what aspects of the molecular distribution can this dataset actually distinguish?

*Thanks to T.J. Lane and Alisia Fadini for reading earlier drafts and for their thoughtful feedback.*

### Further reading

For readers who want the technical background, the short bibliography below points to work on structural ensemble determination, the limits of averaged data, cryo-EM heterogeneity, Bayesian reconstruction, and image-level ensemble inference.

1. Bonomi et al. *Principles of protein structural ensemble determination*. Current Opinion in Structural Biology, 2017.
2. Ravera et al. *A critical assessment of methods to recover information from averaged data*. Physical Chemistry Chemical Physics, 2016.
3. Tang et al. *Conformational heterogeneity and probability distributions from single-particle cryo-electron microscopy*. Current Opinion in Structural Biology, 2023.
4. Scheres. *A Bayesian view on cryo-EM structure determination*. Journal of Molecular Biology, 2012.
5. Sánchez-Espinosa et al. *Cryo-EM as a stochastic inverse problem*. arXiv, 2025.
6. Clark et al. *Cooling fast and slow: Characterising the effects of vitrification in cryo-EM and the subsequent recovery of equilibrium populations*. bioRxiv, 2026.
7. Mattingly et al. *Measurement-limited learning of conformational heterogeneity in cryo-electron microscopy*. arXiv, 2026.


---

# MDverse, shedding light on the dark matter of molecular dynamics simulations

**Authors:** Johanna KS Tiemann, Magdalena Szczuka, Lisa Bouarroudj, Mohamed Oussaren, Steven Garcia, Rebecca J Howard, Lucie Delemotte, Erik Lindahl, Marc Baaden, Kresten Lindorff-Larsen, Matthieu Chavent, Pierre Poulain
**Year:** 2024
**Venue:** eLife
**DOI:** 10.7554/eLife.90061
**Source PDF URL:** https://europepmc.org/articles/PMC11364437?pdf=render (Europe PMC copy of PMC11364437; gold OA, eLife)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

RESEARCH ARTICLE

MDverse, shedding light on the dark
matter of molecular dynamics simulations
Johanna KS Tiemann1*†, Magdalena Szczuka2, Lisa Bouarroudj3,
Mohamed Oussaren3, Steven Garcia4, Rebecca J Howard5, Lucie Delemotte6,
Erik Lindahl5,6, Marc Baaden7, Kresten Lindorff-­Larsen1, Matthieu Chavent2*,
Pierre Poulain3*

*For correspondence:
johanna.tiemann@gmail.com
(JKST);
matthieu.chavent@ipbs.fr (MC);
pierre.poulain@u-paris.fr (PP)
Present address:
NovozymesA/S, Lyngby,
Denmark

†

Competing interest: See page
Funding: See page 16
Preprint posted
02 May 2023
Sent for Review
28 June 2023
Reviewed preprint posted
20 September 2023
Reviewed preprint revised
01 July 2024
Version of Record published
30 August 2024
Reviewing Editor: Shozeb
Haider, University College
London, United Kingdom
‍ ‍Copyright Tiemann et al. This
article is distributed under the
terms of the Creative Commons
Attribution License, which
permits unrestricted use and
redistribution provided that the
original author and source are
credited.

Linderstrøm-­Lang Centre for Protein Science, Department of Biology, University
of Copenhagen, Copenhagen, Denmark; 2Institut de Pharmacologie et Biologie
Structurale, CNRS, Université de Toulouse, Toulouse, France; 3Université Paris
Cité, CNRS, Institut Jacques Monod, Paris, France; 4Independent researcher,
Amsterdam, Netherlands; 5Department of Biochemistry and Biophysics, Science for
Life Laboratory, Stockholm University, Stockholm, Sweden; 6Department of applied
physics, Science for Life Laboratory, KTH Royal Institute of Technology, Stockholm,
Sweden; 7Laboratoire de Biochimie Théorique, CNRS, Université Paris Cité, Paris,
France

Abstract The rise of open science and the absence of a global dedicated data repository for
molecular dynamics (MD) simulations has led to the accumulation of MD files in generalist data
repositories, constituting the dark matter of MD — data that is technically accessible, but neither
indexed, curated, or easily searchable. Leveraging an original search strategy, we found and indexed
about 250,000 files and 2000 datasets from Zenodo, Figshare and Open Science Framework. With
a focus on files produced by the Gromacs MD software, we illustrate the potential offered by the
mining of publicly available MD data. We identified systems with specific molecular composition and
were able to characterize essential parameters of MD simulation such as temperature and simulation length, and could identify model resolution, such as all-­atom and coarse-­grain. Based on this
analysis, we inferred metadata to propose a search engine prototype to explore the MD data. To
continue in this direction, we call on the community to pursue the effort of sharing MD data, and to
report and standardize metadata to reuse this valuable matter.
eLife assessment
The study presents a valuable tool for searching molecular dynamics simulation data, making such
datasets accessible for open science. The authors provide convincing evidence that it is possible
to identify noteworthy molecular dynamics simulation datasets and that their analysis can produce
information of value to the community.

Introduction
The volume of data available in biology has increased tremendously (Marx, 2013; Stephens et al.,
2015), through the emergence of high-­throughput experimental technologies, often referred to as
-omics, and the development of efficient computational techniques, associated with high-­performance
computing resources. The Open Access (OA) movement to make research results free and available to
anyone (including e.g. the Budapest Open Access Initiative and the Berlin declaration on Open Access
to Knowledge) has led to an explosive growth of research data made available by scientists (Wilson

et al., 2021). The FAIR (Findable, Accessible, Interoperable and Reusable) principles Wilkinson et al.,
2016 have emerged to structure the sharing of these data with the goals of reusing research data and
to contribute to the scientific reproducibility. This leads to a world where research data has become
widely available and exploitable, and consequently new applications based on artificial intelligence
(AI) emerged. One example is AlphaFold (Jumper et al., 2021), which enables the construction of a
structural model of any protein from its sequence. However, it is important to be aware that the development of AlphaFold was only possible because of the existence of extremely well annotated and
cleaned open databases of protein structures (wwPDB Berman et al., 2003) and sequences (UniProt
Consortium, 2022). Similarly, accurate predictions of NMR chemical shifts and chemical-­shift-­driven
structure determination was only made possible via a community-­driven collection of NMR data in the
Biological Magnetic Resonance Data Bank (Hoch et al., 2023). One can easily imagine novel possibilities of AI and deep learning reusing previous research data in other fields, if that data is curated and
made available at a large scale (Fan and Shi, 2022; Mahmud et al., 2021).
Molecular Dynamics (MD) is an example of a well-­established research field where simulations give
valuable insights into dynamic processes, ranging from biological phenomena to material science
(Perilla et al., 2015; Hollingsworth and Dror, 2018; Yoo et al., 2020; Alessandri et al., 2021;
Krishna et al., 2021). By unraveling motions at details and timescales invisible to the eye, this well-­
established technique complements numerous experimental approaches (Bottaro and Lindorff-­
Larsen, 2018; Marklund and Benesch, 2019; Fawzi et al., 2021). Nowadays, large amounts of
MD data could be generated when modelling large molecular systems (Gupta et al., 2022) or when
applying biased sampling methods (Hénin et al., 2022). Most of these simulations are performed
to decipher specific molecular phenomena, but typically they are only used for a single publication.
We have to confess that many of us used to believe that it was not worth the storage to collect
all simulations (in particular since all might not have the same quality), but in hindsight this was
wrong. Storage is exceptionally cheap compared to the resources used to generate simulations data,
and they represent a potential goldmine of information for researchers wanting to reanalyze them
(Antila et al., 2021), in particular when modern machine-­learning methods are typically limited by
the amount of training data. In the era of open and data-­driven science, it is critical to render the
data generated by MD simulations not only technically available but also practically usable by the
scientific community. In this endeavor, discussions started a few years ago (Abraham et al., 2019;
Abriata et al., 2020; Merz et al., 2020) and the MD data sharing trend has been accelerated with
the effort of the MD community to release simulation results related to the COVID-­19 pandemic
(Amaro and Mulholland, 2020; Mulholland and Amaro, 2020) in a centralized database (https://​
covid.bioexcel.eu). Specific databases have also been developed to store sets of simulations related
to protein structures (MoDEL: Meyer et al., 2010), membrane proteins in general (MemProtMD:
Stansfeld et al., 2015; Newport et al., 2019), G-­protein-­coupled receptors in particular (GPCRmd:
Rodríguez-­Espigares et al., 2020), or lipids (Lipidbook:Domański et al., 2010, NMRLipids Databank: Kiirikki et al., 2023).
Albeit previous attempts in the past (Tai et al., 2004; Meyer et al., 2010), there is, as of now, no
central data repository that could host all kinds of MD simulation files. This is not only due to the huge
volume of data and its heterogeneity, but also because interoperability of the many file formats used
adds to the complexity. Thus, faced with the deluge of biosimulation data (Hospital et al., 2020),
researchers often share their simulation files in multiple generalist data repositories. This makes it difficult to search and find available data on, for example, a specific protein or a given set of parameters.
We are qualifying this amount of scattered data as the dark matter of MD, and we believe it is essential
to shed light onto this overlooked but high-­potential volume of data. When unlocked, publicly available MD files will gain more visibility. This will help people to access and reuse these data more easily
and overall, by making MD simulation data more FAIR (Wilkinson et al., 2016), it will also improve the
reproducibility of MD simulations (Elofsson et al., 2019; Porubsky et al., 2020; Bonomi et al., 2019).
In this work, we have employed a search strategy to index scattered MD simulation files deposited
in generalist data repositories. With a focus on the files generated by the Gromacs MD software, we
performed a proof-­of-­concept large-­scale analysis of publicly available MD data. We revealed the
high value of these data and highlighted the different categories of the simulated molecules, as well
as the biophysical conditions applied to these systems. Based on these results and our annotations,
we proposed a search engine prototype to easily explore this dark matter of MD. Finally, building on

Figure 1. Explore and Expand ($Ex^2$) strategy used to index MD-­related files and number of deposited files in generalist data repositories, identified
by this strategy. (A) Explore and Expand (‍Ex2 ‍) strategy used to index and collect MD-­related files. Within the explore phase, we search in the respective
data repositories for datasets that contain specific keywords (e.g. ‘molecular dynamics’, ‘md simulation’, ‘namd’, ‘martini’...) in conjunction with specific
file extensions (e.g. ‘mdp’, ‘psf’, ‘parm7’...), depending on their uniqueness and level of trust to not report false-­positives (i.e. not MD related). In the
expand phase, the content of the identified datasets is fully cataloged, including files that individually could result in false positives (such as e.g. ‘.log’
files). (B) Number of deposited files in generalist data repositories, identified by our ‍Ex2 ‍strategy.

this experience, we provide simple guidelines for data sharing to gradually improve the FAIRness of
MD data.

Results
With the rise of open science, researchers increasingly share their data and deposit them into generalist data repositories, such as Zenodo (https://zenodo.org), Figshare (https://figshare.com), Open
Science Framework (OSF, https://osf.io), and Dryad (https://datadryad.org/). In this first attempt to
find out how many files related to MD are deposited in data repositories, we focused our exploration
on three major data repositories: Figshare (∼3.3 million files, ∼112 TB of data, as of January 2023),
OSF (∼2 million files, as of November 2022) [Figures provided by Figshare and OSF user support
teams.], and Zenodo (∼9.9 million files, ∼1.3 PB of data, as of December 2022; Panero and Benito,
2022).
One immediate strategy to index MD simulation files available in data repositories is to perform a
text-­based Google-­like search. For that, one queries these repositories with keywords such as ‘molecular dynamics’ or ‘Gromacs’. Unfortunately, we experienced many false positives with this search
strategy. This could be explained by the strong discrepancy we observed in the quantity and quality
of metadata (title, description) accompanying datasets and queried in text-­based search. For instance,
a description text could be composed of a couple of words to more than 1200 words. Metadata is
provided by the user depositing the data, with no incentive to issue relevant details to support the
understanding of the simulation. For the three data repositories studied, no human curation other by
that of the providers is performed when submitting data. It is also worth mentioning that title and
description are provided as free-­text and do not abide to any controlled vocabulary such as a specific
MD ontology.

Table 1. Statistics of the MD-­related datasets and files found in the data repositories Figshare, OSF, and Zenodo.
Data repository

datasets

first dataset

latest dataset

files

total size (GB)

zip files

files within zip

total files

Zenodo

19/11/2014

05/03/2023

20,250

12,851

141,304

161,554

Figshare

20/08/2012

03/03/2023

74,720

78,056

OSF

24/05/2017

05/02/2023

Total

–

–

29,732

14,082

216,024

245,756

To circumvent this issue, we developed an original and specific search strategy that we called
Explore and Expand (‍Ex2‍) (see Figure 1A and Materials and methods section) and that relies on a
combination of file types and keywords queries. In the Explore phase, we searched for files based
on their file types (for instance: .xtc, .gro, etc) with MD-­related keywords (for instance: ‘molecular
dynamics’, ‘Gromacs’, ‘Martini’, etc). Each of these hit files belonged to a dataset, which we further
screened in the Expand phase. There, we indexed all files found in a dataset identified in the previous
Explore phase with, this time, no restriction to the collected file types (see Figure 1A and details on
the data scraping procedure in the Materials and methods section).
Globally, we indexed about 250,000 files and 2000 datasets that represented 14 TB of data deposited between August 2012 and March 2023 (see Table 1). One major difficulty were the numerous
files stored in zipped archives, about seven times more than files steadily available in datasets (see
Table 1). While this choice is very convenient for depositing the files (as one just needs to provide
one big zip file to upload to the data repository server), it hinders the analysis of MD files as data
repositories only provide a limited preview of the content of the zip archives and completely inhibits,
for example, data streaming for remote analysis and visualization. Files within zip files are not indexed
and cannot be searched individually. The use of zip archives also hampers the reusability of MD data,
since a specific file cannot be downloaded individually. One has to download the entire zip archive
(sometimes with a size up to several gigabytes) to extract the one file of interest.
The first dataset we found related to MD data that has been deposited in August 2012 in Figshare
and corresponds to the work of Fuller et al., 2012 (see Table 1) but we may consider the start of
more substantial deposition of the MD data to be 2016 with more than 20,000 files deposited, mainly
in Figshare (see Figure 1B). While the number of files deposited in Zenodo was first relatively limited,
the last few years (2020–2022) saw a steep increase, passing from a few thousands files in 2018 to
almost 50,000 files in 2022 (see Figure 1B). In 2018, the number of MD files deposited in OSF was
similar to those in the two other data repositories, but did not take off as much as the other data
repositories. Zenodo seems to be favored by the MD community since 2019, even though Figshare
in 2022 also saw a sharp increase in deposited MD files. The preference for Zenodo could also be
explained by the fact that it is a publicly funded repository developed under the European OpenAIRE
program and operated by CERN (European Organization For Nuclear Research, 2013). Overall,
the trend showed a rise of deposited data with a steep increase in 2022 (Figure 1B). We believe that
this trend will continue in future years, which will lead to a greater amount of MD data available. It is
thus urgent to deploy a strategy to index this vast amount of data, and to allow the MD community
to easily explore and reuse such gigantic resource. The following describes what is already feasible
in terms of meta analysis, in particular what types of data are deposited in data repositories and the
simulation setup parameters used by MD experts that have deposited their data.
With our ‍Ex2‍strategy (see Figure 1A), we assigned the deposited files to the MD packages: AMBER
(Salomon‐Ferrer et al., 2013), DESMOND (Bowers et al., 2006), Gromacs (Berendsen et al., 1995;
Abraham et al., 2015), and NAMD/CHARMM (Phillips et al., 2020; Brooks et al., 2009), based on

Figure 2. Categorization of index files based on their file types and assigned MD engine. (A) Distribution of files among MD simulation engines
(B) Expansion of (A) MD Engine category ‘Unknown’ into the 10 most observed file types.

their corresponding file types (see Materials and methods section). In the case of NAMD/CHARMM,
file extensions were mostly identical, which prevented us from distinguishing the respective files from
these two MD programs. With 87,204 files deposited, the Gromacs program was most represented
(see Figure 2A), followed by NAMD/CHARMM, AMBER, and DESMOND. This statistic is limited as it
does not consider more specific databases related to a particular MD program. For example, the DE
Shaw Research website contains a large amount of simulation data related to SARS-­CoV-­2 that has
been generated using the ANTON supercomputer (https://www.deshawresearch.com/downloads/​
download_trajectory_sarscov2.cgi/) or other extensively simulated systems of interest to the community. However, this in itself might also serve as a good example, since few automated search strategies
will be able to find custom stand-­alone web servers as valuable repositories. Here, our goal was not
to compare the availability of all data related to each MD program but to give a snapshot of the type
of data available at a given time (i.e. March 2023) in generalist data repositories. Interestingly, many
files (>133,000) were not directly associated to any MD program (see Figure 2A label ‘Unknown’).
We categorized these files based on their extensions (see Figure 2B). While 10% of these files were
without file extension (Figure 2B, column none), we found numerous files corresponding to structure coordinates such as .pdb (∼12,000) and .xyz (∼6800) files. We also got images (.tiff files) and
graphics (.xvg files). Finally, we found many text files such as .txt, .dat, and .out which can potentially
hold details about how simulations were performed. Focusing further on files related to the Gromacs
program, being currently most represented in the studied data repositories, we demonstrated in the
following present possibilities to retrieve numerous information related to deposited MD simulations.
First, we were interested in what file types researchers deposited and thereby find potentially of
great value to share. We therefore quantified the types of files generated by Gromacs (Figure 3A).
The most represented file type is t​he.​xtc file (28,559 files, representing 8.6 TB). This compressed
(binary) file is used to store the trajectory of an MD simulation and is an important source of information to characterize the evolution of the simulated molecular system as a function of time. It is thus
logical to mainly find this type of file shared in data repositories, as it is of great value for reusage and
new analyses. Nevertheless, it is not directly readable but needs to be read by a third-­party program,
such as Gromacs itself, a molecular viewer like VMD (Humphrey et al., 1996) or an analysis library
such as MDAnalysis (Gowers et al., 2016; Michaud-­Agrawal et al., 2011). In addition, this trajectory
file can only be of use in combination with a matching coordinates file, in order to correctly access the
dynamics information stored in this file. Thus, as it is, this file is not easily mineable to extract useful
information, especially if multiple .xtc and coordinate files are available in one dataset. Interestingly,
we found 1406 .trr files, which contain trajectory but also additional information such as velocities,
energy of the system, etc. While this file is especially useful in terms of reusability, the large size (can go
up to several 100 GB) limits its deposition in most data repositories. For instance, a file cannot usually
exceed 50 GB in Zenodo, 20 GB in Figshare (for free accounts) and 5 GB in OSF. Altogether, Gromacs
trajectory files represented about 30,000 files in the three explored generalist repositories (34% of
Gromacs files). This is a large number in comparison to existing trajectories stored in known databases
dedicated to MD with 1700 MD trajectories available in MoDEL, 1737 trajectories (as of November
2022) available in GPCRmd, 5971 (as of January 2022) trajectories available in MemProtMD and 726
trajectories (as of March 2023) available in the NMRLipids Databank. Although fewer in count, these
numbers correspond to manually or semi-­automatically curated trajectories of specific systems, mostly
proteins and lipids. Thus, ∼30,000 MD trajectories available in generalist data repositories may represent a wider spectrum of simulated systems but need to be further analyzed and filtered to separate
usable data from less interesting trajectories such as minimization or equilibration runs.
Given the large volume of data represented by .xtc files (see above), we could only scratch the
surface of the information stored in these trajectory files by analyzing a subset of 779 .xtc files - one
per dataset in which this type of file was found. We were able to get the size of the molecular systems
and the number of frames available in these files (Figure 3B). The system size was up to more than one
million atoms for a simulation of the TonB protein (Virtanen et al., 2020). The cumulative distribution
of the number of frames showed that half of the files contain more than 10,000 frames. This conformational sampling can be very useful for other research fields besides the MD community that study, for
instance, protein flexibility or protein engineering where diverse backbones can be of value. We found
an .xtc file containing more than 5 million frames, where the authors probe the picosecond–nanosecond dynamics of T4 lysozyme and guide the MD simulation with NMR relaxation data (Kümmerer

Figure 3. Content analysis of .xtc and .gro files. (A) Number of Gromacs-­related files available in searched data repositories. In red, files used for further
analyses. (B) Simple analyze of a subset of .xtc files with the cumulative distribution of the number of frames (in green) and the system size (in orange).
(C) Cumulative distribution of the system sizes extracted from .gro files. (D) Upset plot of systems grouped by molecular composition, inferred from the
analysis of .gro files. For this figure, 3D structures of representative systems were displayed, including soluble proteins such as TonB and T4 Lysozyme,
membrane proteins such as Kir Channels and the Gasdermin prepore, Protein-/RNA and G-­quadruplex and other non-­protein molecules.

et al., 2021). Extending this analysis to all 28,559 .xtc files detected would be of great interest for a
more holistic view, but this would require an initial step of careful checking and cleaning to be sure
that these files are analyzable. Of note, as .xtc files also contain time stamps, it would be interesting
to study the relationship between the time and the number of frames to get useful information about
the sampling. Nevertheless, this analysis would be possible only for unbiased MD simulations. So, we
would need to decipher if the .xtc file is coming from biased or unbiased simulations, which may not
be trivial.
These results bring a first explanation on why there is not a single special-­purpose repository
for MD trajectory files. Databases dedicated to molecular structures such as the Protein Databank
(Berman et al., 2000; Kinjo et al., 2017; Armstrong et al., 2020), or even the recent PDB-­dev
(Burley et al., 2017), designed for integrative models, cannot accept such large-­size files, even less

if complete trajectories without reducing the number of frames would be uploaded. This would also
require implementing extra steps of data curation and quality control. In addition, the size of the IT
infrastructure and the human skills required for data curation represents a significant cost that could
probably not be supported by a single institution.
Subsequently, our interest shifted towards exploring which systems are being investigated by MD
researchers who deposit their files. We found 9718 .gro files which are text files that contain the
number of particles and the Cartesian coordinates of the system modelled. By parsing the number
of particles and the type of residue, we were able to give an overview of all Gromacs systems deposited (Figure 3C, D). In terms of system size, they ranged from very small - starting with two coarse-­
grain (CG) particles of graphite (Piskorz et al., 2019), followed by coordinates of a water molecule
(3 atoms) (Ivanov et al., 2017), CG model of benzene (3 particles) (Dandekar and Mondal, 2020)
and atomistic model of ammonia (4 atoms) (Kelly and Smith, 2020) — to go up to atomistic and
coarse-­grain systems composed of more than 3 million particles (Duncan et al., 2020; Schaefer and
Hummer, 2022; Figure 3C). Interestingly, the system sizes in .gro files exceeded those of the analyzed
.xtc files (Figure 3B). Even if we cannot exclude that the limited number of .xtc files analyzed (779 .xtc
files selected from 28,559 .xtc files indexed) could explain this discrepancy, an alternate hypothesis is
that the size of an .xtc file also depends on the number of frames stored. To reduce the size of .xtc files
deposited in data repositories, besides removing some frames, researchers might also remove parts
of the system, such as water molecules. As a consequence for reusability, this solvent removal could
limit the number of suitable datasets available for researchers interested in re-­analysing the simulation
with respect to, in this case, water diffusion. While the size of systems extracted from .gro files was
homogeneously spread, we observed a clear bump around system sizes of circa 8500 atoms/particles. This enrichment of data could be explained by the deposition of ∼340 .gro files related to the
simulation of a peptide translocation through a membrane (Figure 3C; Kabelka et al., 2021). Beyond
1 million particles/atoms, the number of systems is, for the moment, very limited.
We then analyzed residues in .gro files and inferred different types of molecular systems (see
Figure 3D). Two of the most represented systems contained lipid molecules. This may be related
to NMRLipids initiative (http://nmrlipids.blogspot.com). For several years, this consortium has been
actively working on lipid modelling with a strong policy of data sharing and has contributed to share
numerous datasets of membrane systems. As illustrated in Figure 3C, a variety of membrane systems,
especially membrane proteins, were deposited. This highlights the vitality of this research field, and
the will of this community to share their data. We also found numerous systems containing solvated
proteins. This type of data, combined with .xtc trajectory files (see above), could be invaluable to
describe protein dynamics and potentially train new artificial intelligence models to go beyond the
current representation of the static protein structure (Lane, 2023). There was also a good proportion of systems containing nucleic acids alone or in interaction with proteins (1237 systems). At this
time, we found only few systems containing carbohydrates that also contained proteins and corresponded to one study to model hyaluronan–CD44 interactions (Vuorio et al., 2017). Maybe a reason
for this limited number is that systems containing sugars are often modelled using AMBER force field
(Salomon‐Ferrer et al., 2013), in combination with GLYCAM (Kirschner et al., 2008). A future study
on the ∼10,200 AMBER files deposited could retrieve more data related to carbohydrate containing
systems. Given the current developments to model glycans (Fadda, 2022), we expect to see more
deposited systems with carbohydrates in the coming years.
Finally, we found 1029 gro files which did not belong to the categories previously described. These
files were mostly related to models of small molecules, or molecules used in organic chemistry (Young
et al., 2020) and material science (Piskorz et al., 2019; Zheng et al., 2022) (see central panel,
Figure 3D). Several datasets contained lists of small molecules used for calculating free energy of
binding (Aldeghi et al., 2016), solubility of molecules (Liu et al., 2016), or osmotic coefficient (Zhu,
2019). Then, we identified models of nanoparticles (Kyrychenko et al., 2012; Pohjolainen et al.,
2016), polymers (Sarkar et al., 2020; Karunasena et al., 2021; Gertsen et al., 2020), and drug molecules like EPI-­7170, which binds disordered regions of proteins (Zhu et al., 2022). Finally, an interesting
case from material sciences was the modelling of the PTEG-­1 molecule, an addition of polar triethylene glycol (TEG) onto a fulleropyrrolidine molecule (see central panel, Figure 3D). This molecule was
synthesized to improve semiconductors (Jahani et al., 2014). We found several models related to this
peculiar molecule and its derivatives, both atomistic (Qiu et al., 2017; Sami et al., 2022) and coarse

grained (Alessandri et al., 2020). With a good indexing of data and appropriate metadata to identify
modelled molecules, a simple search, which was previously to this study missing, could easily retrieve
different models of the same molecule to compare them or to run multi-­scale dynamics simulations.
Beyond .gro files, we would like to analyze the ensemble of the ∼12,000 .pdb extracted in this study
(see Figure 2B) to better characterize the types of molecular structures deposited.
Another important category of deposited files are those containing information about the topology
of the simulated molecules, including file extensions such as .itp and .top. Further, they are often the
results of long parametrization processes (Vanommeslaeghe and MacKerell, 2012; Souza et al.,
2021; Wang et al., 2004) and therefore of significant value for reusability. Based on our analysis,
we indexed almost 20,000 topology files which could spare countless efforts to the MD community
if these files could be easily found, annotated and reused. Interestingly, the number of .itp files was
elevated (13,058 files) with a total size of 2 GB, while there were less .top files (7009 files) with a total
size of 17 GB. Thus, .itp files seemed to contain much less information than the .top files. Among the
remaining file types, .tpr files contain all the information to potentially directly run a simulation. Here,
we found 4987 .tpr files, meaning that it could virtually be possible to rerun almost 5000 simulations
without the burden of setting up the system to simulate. Finally, the 3730 .log files are also a source of
useful information as it is relatively easy to parse this text file to extract details on how MD simulations
were run, such as the version of Gromacs, which command line was used to run the simulation, etc.
Our next step was to gain insight into the parameter settings employed by the MD community,
which may aid us in identifying preferences in MD setups and potential necessity for further education
to avoid suboptimal or outdated configurations. We therefore analyzed 10,055 .mdp files stored in
the different data repositories. These text files contain information regarding the input parameters to
run the simulations such as the integrator, the number of steps, the different algorithms for barostat
and thermostat, etc. (for more details see: https://manual.gromacs.org/documentation/current/user-​
guide/mdp-options.html).
We determined the expected simulation time corresponding to the product of two parameters
found in .mdp files: the number of steps and the time step. Here, we acknowledge that one can set up
a very long simulation time and stop the simulation before the end or, on contrary, use a limited time
(especially when calculations are performed on HPC resources with wall-­time) and then extend the
simulation for a longer duration. Using only the .mdp file, we cannot know if the simulation reached
its term. To do so, comparison with an .xtc file from the same dataset may help to answer this specific
question. However, in this study, we were interested in MD setup practices, in particular what simulation time researchers would set up their system with - likely in the mindset to reach that ending time.
We restricted this analysis to the 4623 .mdp files that used the md or sd integrator, and that have a
simulation time above 1 ns. We found that the majority of the .mdp files were used for simulations of
50 ns or less (see Figure 4A). Further, 697 .mdp files with simulations times set-­up between 50 ns and
1 µs and 585 .mdp files with simulation time above 1 µs were identified. As analyzing .gro files showed
a good proportion of coarse-­grained models (Figure 3B, C), we discriminated simulations setups for
these two types of models using the time step as a simple cutoff. We considered that a time step
greater than 10 fs (i.e. dt = 0.01) corresponded to MD setups for coarse grained models (Ingólfsson
et al., 2014). Globally, we found that over all simulations, the setups for atomistic simulations were
largely dominant. However, for simulations with a simulation time above 1 µs specifically, coarse-­grain
simulations represented 86% of all.
We then looked into the combinations of thermostat and barostat (see Figure 4B) from 9199 .mdp
files. The main thermostat used is by far the V-­rescale (Bussi et al., 2007) often associated with the
Parrinello-­Rahman barostat (Parrinello and Rahman, 1981). This thermostat was also used with the
Berendsen barostat (Berendsen et al., 1984). In a few cases, we observed the use of the V-­rescale
thermostat with the very recently developed C-­rescale barostat (Bernetti and Bussi, 2020). A total of
2021 .mdp files presented neither thermostat nor barostat, which means they would not be used in
production runs. This could correspond to setups used for energy minimization, or to add ions to the
system (with the genion command), or for molecular mechanics with Poisson–Boltzmann and surface
area solvation (MM/PBSA) and molecular mechanics with generalised Born and surface area solvation
(MM/GBSA) calculations (Genheden and Ryde, 2015).
Finally, we analyzed the range of starting temperatures used to perform simulations (see Figure 4C).
We found a clear peak around the temperatures 298 K - 310 K which corresponds to the range

Figure 4. Content analysis of .mdp files. (A) Cumulative distribution of .mdp files versus the simulation time for all-­atom and coarse-­grain simulations.
(B) Sankey graph of the repartition between different values for thermostat and barostat. (C) Temperature distribution, full scale in upper panel and
zoom-­in in lower panel.

between ambient room (298 K - 25 °C) and physiological (310 K - 37 °C) temperatures. Nevertheless,
we also observed lower temperatures, which often relate to studies of specific organic systems or
simulations of Lennard-­Jones models (Jeon et al., 2016). Interestingly, we noticed the appearance
of several pikes at 400 K, 600 K, and 800 K, which were not present before the end of the year 2022.
These peaks corresponded to the same study related to the stability of hydrated crystals (Dybeck
et al., 2023). Overall, this analysis revealed that a wide range of temperatures have been explored,
starting mostly from 100 K and going up to 800 K.
To encourage further analysis of the collected files, we shared our data collection with the community in Zenodo (see Data availability statement). The data scrapping procedure and data analysis is
available on GitHub with a detailed documentation. To let researchers having a quick glance and
explore this data collection, we created a prototype web application called MDverse data explorer
available at https://mdverse.streamlit.app/ and illustrated in Figure 5A. With this web application, it is
easy to use keywords and filters to access interesting datasets for all MD engines, as well as .gro and
.mdp files. Furthermore, when available, a description of the found data is provided and searchable
for keywords (Figure 5A, on the left sidebar). The sets of data found can then be exported as a tab-­
separated values (.tsv) file for further analysis (Figure 5B).

Figure 5. Snapshots of the MDverse data explorer, a prototype search engine to explore collected files and datasets. (A) General view of the web
application. (B) Focus on the .mdp and .gro files sets of data exported as.tsv files. The web application also includes links to their original repository.

Towards a better sharing of MD data
With this work, we have shown that it was possible to not only retrieve MD data from the generalist
data repositories Zenodo, Figshare and OSF, but to shed light onto the dark matter of MD data in
terms of learning current scientific practice, extracting valuable topology information, and analysing
how the field is developing. Our objective was not to assess the quality of the data but only to show
what kind of data was available. The ‍Ex2‍ strategy to find files related to MD simulations relied on
the fact that many MD software output files with specific file extensions. This strategy could not be
applied in research fields where data exhibits non-­specific file types. We experienced this limitation
while indexing zip archives related to MD simulations, where we were able to decide if a zip archive
was pertinent for this work only by accessing the list of files contained in the archive. This valuable
feature is provided by data repositories like Zenodo and Figshare, with some caveats, though.
As of March 2023, we managed to index 245,756 files from 1979 datasets, representing altogether
14 TB of data. This is a fraction of all files stored in data repositories. For instance, as of December
2022, Zenodo hosted about 9.9 million files for ∼1.3 PB of data (Panero and Benito, 2022). All these
files are stored on servers available 24/7. This high availability costs human resources, IT infrastructures and energy. Even if MD data represents only 1% of the total volume of data stored in Zenodo,
we believe it is our responsibility, as a community, to develop a better sharing and reuse of MD
simulation files - and it will neither have to be particularly cumbersome nor expensive. To this end,

we are proposing two solutions. First, improve practices for sharing and depositing MD data in data
repositories. Second, improve the FAIRness of already available MD data notably by improving the
quality of the current metadata.

Guidelines for better sharing of MD simulation data
Without a community-­approved methodology for depositing MD simulation files in data repositories,
and based on the current experience we described here, we propose a few simple guidelines when
sharing MD data to make them more FAIR (Findable, Accessible, Interoperable and Reusable):
Avoid zip or tar archives whose content cannot be properly indexed by data repositories. As
much as possible, deposit original data files directly.
• Describe the MD dataset with extensive metadata. Provide adequate information along your
dataset, such as:
The scope of the study, e.g. investigate conformation dynamics, benchmark force field,...
The method on a basic (e.g. quantum mechanics, all-­atom, coarse-­grain) or advanced (accelerated, metadynamics, well-­tempered) level.
The MD software: name, version (tag) and whether modifications have been made.
The simulation settings (for each of the steps, including minimization, equilibration and
production): temperature(s), thermostat, barostat, time step, total runtime (simulation
length), force field, additional force field parameters.
The composition of the system, with the precise names of the molecules and their numbers,
if possible also PDB, UniProt or Ensemble identifiers and whether the default structure has
been modified.
Give information about any post-­processing of the uploaded files (e.g. truncation or stripping of the trajectory), including before and after values of what has been modified e.g.
number of frames or number of atoms of uploaded files.
Highlight especially valuable data, e.g. excessively QM-­based parameterized molecules, and
their parameter files.
Store this metadata in the description of the dataset. An adaptation of the Minimum Information
About a Simulation Experiment (MIASE) guidelines Waltemath et al., 2011 in the context of MD
simulations would be useful to define required metadata.
•

Link the MD dataset to other associated resources, such as:
The research article (if any) for which these data have been produced. Datasets are usually
mentioned in the research articles, but rarely the other way around, since the deposition has
to be done prior to publication. However, it is eminently possible to submit a revised version,
and providing a link to the related research paper in updated metadata of the MD dataset
will ease the reference to the original publication upon data reuse.
The code used to analyze the data, ideally deposited in the repository to guarantee availability, or in a GitHub or GitLab repository.
Any other datasets that belong to the same study.
• Provide sufficient files to reproduce simulations and use a clear naming convention to make
explicit links between related files. For instance, for the Gromacs MD engine, ​trajectory.​xtc files
could share the same names as ​structure.​gro files (e.g. ​proteinA.​gro and ​proteinA.​xtc).
• Revisit your data deposition after paper acceptance and update information if necessary.
Zenodo and Figshare provide a DOI for every new version of a dataset as well as a ‘master’ DOI
that always refers to the latest version available.
•

These guidelines are complementary to the reliability and reproducibility checklist for molecular
dynamics simulations (Commun Biol, 2023). Eventually, they could be implemented in machine
actionable Data Management Plan (maDMP) (Miksa et al., 2019). So far, MD metadata is formalized
as free text. We advocate for the creation of a standardized and controlled vocabulary to describe artifacts and properties of MD simulations. Normalized metadata will, in turn, enable scientific knowledge
graphs (Auer, 2018; Färber and Lamprecht, 2021) that could link MD data, research articles and MD
software in a rich network of research outputs.
Converging on a set of metadata and format requires a large consensus of different stakeholders,
from users, to MD program developers, and journal editors. It would be especially useful to organize

specific workshops with representatives of all these communities to collectively tackle this specific
issue.

Improving metadata of current MD data
While indexing about 2000 MD datasets, we found that title and description accompanying these
datasets were very heterogeneous in terms of quality and quantity and were difficult for machines to
process automatically. It was sometimes impossible to find even basic information such as the identity
of the molecular system simulated, the temperature or the length of the simulation. Without appropriate metadata, sharing data is pointless, and its reuse is doomed to fail (Musen, 2022). It is thus
important to close the gap between the availability of MD data and its discoverability and description
through appropriate metadata. We could gradually improve the metadata by following two strategies.
First, since MD engines produce normalized and well-­documented files, we could extract parameters
of the simulation by parsing specific files. We already explored this path with Gromacs, by extracting
the molecular size and composition from .gro files and the simulation time (with some limitations),
thermostat and barostat from .mdp files. We could go even further, by extracting for instance Gromacs
version from .log file (if provided) or by identifying the simulated system from its atomic topology
stored i​n.​gro files. This strategy can in principle be applied to files produced by other MD engines.
A second approach that we are currently exploring uses data mining and named entity recognition
(NER) methods (Perera et al., 2020) to automatically identify the molecular system, the temperature,
and the simulation length from existing textual metadata (dataset title and description), providing
they are of sufficient length. Finally, the possibilities afforded by large language models supplemented
by domain-­specific tools (Bran et al., 2023) might help interpret the heterogenous metadata that is
often associated with the simulations.

Future works
In the future, it is desirable to go further in terms of analysis and integrate other data repositories,
such as Dryad and Dataverse instances (for example Recherche Data Gouv in France). The collaborative platform for source code GitHub could also be of interest. Albeit dedicated to source code and
not designed to host large-­size binary files, GitHub handles small to medium-­size text files like tabular
.csv and .tsv data files and has been extensively used to record cases of the Ebola epidemic in 2014
(Perkel, 2016) and the Covid-­19 pandemic (Johns Hopkins University, 2020). Thus, GitHub could
probably host small text-­based MD simulation files. For Gromacs, we already found 70,000 parameter
.mdp files and 55,000 structure .gro files. Scripts found along these files could also provide valuable
insights to understand how a given MD analysis was performed. Finally, GitHub repositories might
also be an entry point to find other datasets by linking to simulation data, such as institutional repositories (see for instance Pesce and Lindorff-­Larsen, 2023). However, one potential point of concern
is that repositories like GitHub or GitLab do not make any promises about long-­term availability of
repositories, in particular ones not under active development. Archiving of these repositories could
be achieved in Zenodo (for data-­centric repositories) or Software Heritage (Di Cosmo and Zacchiroli,
2017; for source-­code-­centric repositories).
An obvious next step is the enrichment of metadata with the hope to render open MD data more
findable, accessible and ultimately reusable. Possible strategies have already been detailed previously in this paper. We could also go further by connecting MD data in the research ecosystem. For
this, two apparent resources need to be linked to MD datasets: their associated research papers to
mine more information and to establish a connection with the scientific context, and their simulated
biomolecular systems, which ultimately could cross-­reference MD datasets to reference databases
such as UniProt Consortium, 2022, the PDB (Berman et al., 2000) or Lipid Maps (Sud et al., 2007).
For already deposited datasets, the enrichment of metadata can only be achieved via systematic
computational approaches, while for future depositions, a clear and uniformly used ontology and
dedicated metadata reference file (as it is used by the PLUMED-­NEST: Bonomi et al., 2019) would
facilitate this task.
Eventually, front-­
end solutions such as the MDverse data explorer tool can evolve to being
more user-­friendly by interfacing the structures and dynamics with interactive 3D molecular viewers
(Tiemann et al., 2017; Kampfrath et al., 2022; Martinez and Baaden, 2021).

Conclusion
In this work, we showed that sharing data generated from MD simulations is now a common practice.
From Zenodo, Figshare and OSF alone, we indexed about 250,000 files from 2000 datasets, and we
showed that this trend is increasing. This data brings incentive and opportunities at different levels.
First, for researchers who cannot access high-­performance computing (HPC) facilities, or do not want
to rerun a costly simulation to save time and energy, simulations of many systems are already available. These simulations could be useful to reanalyze existing trajectories, to extend simulations with
already equilibrated systems or to compare simulations of a dedicated molecular system modelled
with different settings. Second, building annotated and highly curated datasets for artificial intelligence will be invaluable to develop dynamic generative deep-­learning models. Then, improving
metadata along available data will foster their reuse and will mechanically increase the reproducibility
of MD simulations. At last, we see here the occasion to push for good practices in the setup and
production of MD simulations.

Materials and methods
Initial data collection
We searched for MD-­
related files in the data repositories Zenodo, Figshare and Open Science
Framework (OSF). Queries were designed with a combination of file types and optionally keywords,
depending on how a given file type was solely associated to MD simulations. We therefore built a list
of manually curated and cross-­checked file types and keywords (https://github.com/MDverse/mdws/​
blob/main/params/query.yml; Poulain et al., 2023). All queries were automated by Python scripts that
utilized Application Programming Interfaces (APIs) provided by data repositories. Since APIs offered
by data repositories were different, all implementations were performed in dedicated Python (van
Rossum, 1995) (version 3.9.16) scripts with the NumPy (Oliphant, 2007) (version 1.24.2), Pandas
(McKinney, 2010) (version 1.5.3) and Requests (version 2.28.2) libraries.
We made the assumption that files deposited by researchers in data repositories were coherent
and all related to a same research project. Therefore, when an MD-­related file was found in a dataset,
all files belonging to this dataset were indexed, regardless of whether their file types were actually
identified as MD simulation files. This is the core of the Explore and Expand strategy (‍Ex2)‍ we applied
in this work and illustrated in Figure 1. By default, the last version of the datasets was collected.
When a zip file was found in a dataset, its content was extracted from a preview provided by
Zenodo and Figshare. This preview was not provided through APIs, but as HTML code, which we
parsed using the Beautiful Soup library (version 4.11.2). Note that the zip file preview for Zenodo was
limited to the first 1000 files. To avoid false-­positive files collected from zip archives, a final cleaning
step was performed to remove all datasets that did not share at least one file type with the file type
list mentioned above. In the case of OSF, there was no preview for zip files, so their content has not
been retrieved.

Gromacs files
After the initial data collection, Gromacs .mdp and .gro files were downloaded with the Pooch library
(version 1.6.0). When a .mdp or .gro file was found to be in a zip archive, the latter was downloaded
and the targeted .mdp or .gro file was selectively extracted from the archive. The same procedure was
applied for a subset of .xtc files that consisted of about one .xtc file per Gromacs datasets.
Once downloaded, .mdp files were parsed to extract the following parameters: integrator, time
step, number of steps, temperature, thermostat, and barostat. Values for thermostat and barostat
were normalized according to values provided by the Gromacs documentation. For the simulation
time analysis, we selected .mdp files with the md or sd integrator and with simulation time above
1 ns to exclude most minimization and equilibrating simulations. For the thermostat and barostat
analysis, only files with non-­missing values and with values listed in the Gromacs documentation were
considered.
The .gro files were parsed with the MDAnalysis library (Michaud-­Agrawal et al., 2011) to extract
the number of particles of the system. Values found in the residue name column were also extracted
and compared to a list of residues we manually associated to the following categories: protein,

lipid, nucleic acid, glucid and water or ions (https://github.com/MDverse/mdws/blob/main/params/​
residue_names.yml; Poulain et al., 2023).
The .xtc files were analyzed using the gmxcheck command (https://manual.gromacs.org/current/​
onlinehelp/gmx-check.html) to extract the number of particles and the number of frames.

MDverse data explorer web app
The MDverse data explorer web application was built in Python with the Streamlit library. Data was
downloaded from Zenodo (see the Data availability statement).

System visualization and molecular graphics
Molecular graphics were performed with VMD (Humphrey et al., 1996) and Chimera (Pettersen
et al., 2004). For all visualizations, .gro files containing molecular structure were used. In the case of
the two structures in Figure 3B, .xtc files were manually assigned to their corresponding .gro (for the
TonB protein) or .tpr (for the T4 Lysozyme) files based on their names in their datasets.
Origin of the structures displayed in this work:

TonB
Dataset URL: https://zenodo.org/record/3756664
Publication (DOI): https://doi.org/10.1039/D0CP03473H

T4 Lyzozyme
Dataset URL: https://zenodo.org/record/3989044
Publication (DOI): https://doi.org/10.1021/acs.jctc.0c01338

Benzene
Dataset URL: https://figshare.com/articles/dataset/Capturing_Protein_Ligand_Recognition_​
Pathways_in_Coarse-Grained_Simulation/12517490/1
Publication (DOI): https://doi.org/10.1021/acs.jpclett.0c01683

Ammonia
Dataset URL: https://figshare.com/articles/dataset/Alchemical_Hydration_Free-Energy_Calculations_Using_Molecular_Dynamics_with_Explicit_Polarization_and_Induced_Polarity_Decoupling_An_On_the_Fly_Polarization_Approach/11702442
Publication (DOI): https://doi.org/10.1021/acs.jctc.9b01139

Peptide with membrane
Dataset URL: https://zenodo.org/record/4371296
Publication (DOI): https://doi.org/10.1021/acs.jcim.0c01312

Kir channels
Dataset URL: https://zenodo.org/record/3634884
Publication (DOI): https://doi.org/10.1073/pnas.1918387117

Gasdermin
Dataset URL: https://zenodo.org/record/6797842
Publication (DOI): https://doi.org/10.7554/eLife.81432

Protein-RNA
Dataset URL: https://zenodo.org/record/1308045
Publication (DOI): https://doi.org/10.1371/journal.pcbi.1006642

G-quadruplex
Dataset URL: https://zenodo.org/record/5594466
Publication (DOI): https://doi.org/10.1021/jacs.1c11248

Ptb
Dataset URL: https://osf.io/4aghb/
Publication (DOI): https://doi.org/10.1073/pnas.2116543119

EPI-7170
Dataset URL: https://zenodo.org/record/7120845
Publication (DOI): https://doi.org/10.1038/s41467-022-34077-z

Gold nanoparticle
Dataset URL: https://acs.figshare.com/articles/dataset/Fluorescence_Probing_of_Thiol_Functionalized_Gold_Nanoparticles_Is_Alkylthiol_Coating_of_a_Nanoparticle_as_Hydrophobic_as_​
Expected_/2481241
Publication (DOI): https://doi.org/10.1021/jp3060813

Gd(DOTA)
Dataset URL: https://acs.figshare.com/articles/dataset/Modeling_Gd_sup_3_sup_Complexes_​
for_Molecular_Dynamics_Simulations_Toward_a_Rational_Optimization_of_MRI_Contrast_​
Agents/20334621
Publication (DOI): https://doi.org/10.1021/acs.inorgchem.2c01597

Metalo cage
Dataset URL: https://acs.figshare.com/articles/dataset/Rationalizing_the_Activity_of_an_Artificial_Diels-Alderase_Establishing_Efficient_and_Accurate_Protocols_for_Calculating_Supramolecular_Catalysis/11569452
Publication (DOI): https://doi.org/10.1021/jacs.9b10302

AL1
Dataset
URL:
https://acs.figshare.com/articles/dataset/Nucleation_Mechanisms_of_Self-​
Assembled_Physisorbed_Monolayers_on_Graphite/8846045
Publication (DOI): https://doi.org/10.1021/acs.jpcc.9b01234

PTEG-1 (all-atom)
Dataset URL: https://figshare.com/articles/dataset/PTEG-1_PP_and_N-DMBI_atomistic_force_​
fields/5458144
Publication (DOI): https://doi.org/10.1039/C7TA06609K

PTEG-1 (coarse-grain)
Dataset URL: https://figshare.com/articles/dataset/Neat_and_P3HT-Based_Blend_Morphologies_for_PCBM_and_PTEG-1/12338633
Publication (DOI): https://doi.org/10.1002/adfm.202004799

Theophylline
Dataset
URL:
https://figshare.com/articles/dataset/A_Comparison_of_Methods_for_​
Computing_Relative_Anhydrous_Hydrate_Stability_with_Molecular_Simulation/21644393
Publication (DOI): https://doi.org/10.1021/acs.cgd.2c00832

Acknowledgements
We thank Lauri Mesilaakso, Bryan White, Jorge Hernansanz Biel, Zihwei Li and Kirill Baranov for their
participation in the Copenhagen BioHackathon 2020, whose results showcased the need for a more
advanced search strategy. We acknowledge Massimiliano Bonomi, Giovanni Bussi, Patrick Fuchs and
Elise Lehoux for helpful discussions and suggestions. We also thank the Zenodo, Figshare and OSF
support teams for providing figures on the content of their respective data repository and for their
help in using APIs. This work was supported by Institut français du Danemark (Blåtand program, 2021),
the Data Intelligence Institute of Paris (diiP, IdEx Université Paris Cité, ANR-­18-­IDEX-­0001, 2023).
JKST and KL-­L acknowledge funding by the Novo Nordisk Foundation [NNF18OC0033950 to KL-­L],
and workshops funded by The BioExcel Center-­of-­Excellence (grant agreements 823830, 101093290).

Additional information
Competing interests
Lucie Delemotte: Reviewing editor, eLife. The other authors declare that no competing interests exist.
Funding
Funder

Grant reference number

Author

Institut francais du
Danemark

Blatand program 2021

Matthieu Chavent
Pierre Poulain

Data Intelligence Institute
of Paris

IdEx Université Paris Cité
ANR-18-IDEX-0001 2023

Mohamed Oussaren
Pierre Poulain

Novo Nordisk Foundation NNF18OC0033950

Johanna KS Tiemann
Kresten Lindorff-Larsen

BioExcel Center-ofExcellence

Erik Lindahl

BioExcel Center-ofExcellence

101093290

Erik Lindahl

The funders had no role in study design, data collection and interpretation, or the
decision to submit the work for publication.

Author contributions
Johanna KS Tiemann, Conceptualization, Data curation, Software, Formal analysis, Supervision,
Validation, Investigation, Visualization, Methodology, Writing – original draft, Writing – review and
editing; Magdalena Szczuka, Lisa Bouarroudj, Mohamed Oussaren, Data curation, Software, Formal
analysis, Visualization; Steven Garcia, Data curation, Software, Formal analysis; Rebecca J Howard,
Lucie Delemotte, Erik Lindahl, Marc Baaden, Kresten Lindorff-­Larsen, Conceptualization, Writing –
original draft, Writing – review and editing; Matthieu Chavent, Pierre Poulain, Conceptualization, Data
curation, Software, Formal analysis, Supervision, Funding acquisition, Validation, Investigation, Visualization, Methodology, Writing – original draft, Writing – review and editing

Author ORCIDs
Rebecca J Howard ‍ ‍https://orcid.org/0000-0003-2049-3378
Erik Lindahl ‍ ‍https://orcid.org/0000-0002-2734-2794
Marc Baaden ‍ ‍https://orcid.org/0000-0001-6472-0486
Kresten Lindorff-­Larsen ‍ ‍https://orcid.org/0000-0002-4750-6039
Matthieu Chavent ‍ ‍https://orcid.org/0000-0003-4524-4773
Pierre Poulain ‍ ‍https://orcid.org/0000-0003-4177-3619
Peer review material
Reviewer #1 (Public Review): https://doi.org/10.7554/eLife.90061.3.sa1
Reviewer #2 (Public Review): https://doi.org/10.7554/eLife.90061.3.sa2
Reviewer #3 (Public Review): https://doi.org/10.7554/eLife.90061.3.sa3
Author response https://doi.org/10.7554/eLife.90061.3.sa4

Additional files
Supplementary files
•  MDAR checklist
Data availability
Data files produced from the data collection and processing are shared in Parquet format in Zenodo.
They are freely available under the Creative Commons Attribution 4.0 International license (CC-­BY).
Python scripts to search and index MD files, and to download and parse .mdp ​and.​gro files are open-­
source (under the AGPL-­3.0 license), freely available on GitHub and archived in Software Heritage
(Poulain et al., 2023). A detailed documentation is provided along the scripts to easily reproduce the
data collection and processing. Jupyter notebooks used to analyze results and create the figures of
this paper are open-­source (under the BSD 3-­Clause license), freely available on GitHub and archived
in Software Heritage (Poulain, 2023). The code of the MDverse data explorer web application is
open-­source (under the BSD 3-­Clause license), freely available on GitHub and archived in Software
Heritage (Poulain and Oussaren, 2023).
The following dataset was generated:
Author(s)

Year

Dataset title

Dataset URL

Database and Identifier

Johanna KST,
Mathieu C, Pierre P

MDverse datasets

https://​zenodo.​org/​
records/​7856806

Zenodo, 10.5281/
zenodo.7856806

References
Abraham MJ, Murtola T, Schulz R, Páll S, Smith JC, Hess B, Lindahl E. 2015. GROMACS: High performance
molecular simulations through multi-­level parallelism from laptops to supercomputers. SoftwareX 1–2:19–25.
DOI: https://doi.org/10.1016/j.softx.2015.06.001
Abraham M, Apostolov R, Barnoud J, Bauer P, Blau C, Bonvin AMJJ, Chavent M, Chodera J, Čondić-Jurkić K,
Delemotte L, Grubmüller H, Howard RJ, Jordan EJ, Lindahl E, Ollila OHS, Selent J, Smith DGA, Stansfeld PJ,
Tiemann JKS, Trellet M, et al. 2019. Sharing data from molecular simulations. Journal of Chemical Information
and Modeling 59:4093–4099. DOI: https://doi.org/10.1021/acs.jcim.9b00665, PMID: 31525920
Abriata LA, Lepore R, Dal Peraro M. 2020. About the need to make computational models of biological
macromolecules available and discoverable. Bioinformatics 36:2952–2954. DOI: https://doi.org/10.1093/​
bioinformatics/btaa086, PMID: 32053168
Aldeghi M, Heifetz A, Bodkin MJ, Knapp S, Biggin PC. 2016. Accurate calculation of the absolute free energy of
binding for drug molecules. Chemical Science 7:207–218. DOI: https://doi.org/10.1039/c5sc02678d, PMID:
Alessandri R, Sami S, Barnoud J, de Vries AH, Marrink SJ, Havenith RWA. 2020. Resolving donor–acceptor
interfaces and charge carrier energy levels of organic semiconductors with polar side chains. Advanced
Functional Materials 30:2004799. DOI: https://doi.org/10.1002/adfm.202004799
Alessandri R, Grünewald F, Marrink SJ. 2021. The martini model in materials science. Advanced Materials
33:e2008635. DOI: https://doi.org/10.1002/adma.202008635, PMID: 33956373
Amaro RE, Mulholland AJ. 2020. A community letter regarding sharing biomolecular simulation data for
COVID-­19. Journal of Chemical Information and Modeling 60:2653–2656. DOI: https://doi.org/10.1021/acs.​
jcim.0c00319, PMID: 32255648

Antila HS, M Ferreira T, Ollila OHS, Miettinen MS. 2021. Using open data to rapidly benchmark biomolecular
simulations: Phospholipid conformational dynamics. Journal of Chemical Information and Modeling 61:938–
949. DOI: https://doi.org/10.1021/acs.jcim.0c01299, PMID: 33496579
Armstrong DR, Berrisford JM, Conroy MJ, Gutmanas A, Anyango S, Choudhary P, Clark AR, Dana JM,
Deshpande M, Dunlop R, Gane P, Gáborová R, Gupta D, Haslam P, Koča J, Mak L, Mir S, Mukhopadhyay A,
Nadzirin N, Nair S, et al. 2020. PDBe: improved findability of macromolecular structure data in the PDB.
Nucleic Acids Research 48:D335–D343. DOI: https://doi.org/10.1093/nar/gkz990, PMID: 31691821
Auer S. 2018. Towards an open research knowledge graph. Version 1. Zenodo. https://doi.org/10.5281/zenodo.​
Berendsen HJC, Postma JPM, van Gunsteren WF, DiNola A, Haak JR. 1984. Molecular dynamics with coupling to
an external bath. The Journal of Chemical Physics 81:3684–3690. DOI: https://doi.org/10.1063/1.448118
Berendsen HJC, van der Spoel D, van Drunen R. 1995. GROMACS: A message-­passing parallel molecular
dynamics implementation. Computer Physics Communications 91:43–56. DOI: https://doi.org/10.1016/0010-​
4655(95)00042-E
Berman HM, Westbrook J, Feng Z, Gilliland G, Bhat TN, Weissig H, Shindyalov IN, Bourne PE. 2000. The protein
data bank. Nucleic Acids Research 28:235–242. DOI: https://doi.org/10.1093/nar/28.1.235, PMID: 10592235
Berman H, Henrick K, Nakamura H. 2003. Announcing the worldwide protein data bank. Nature Structural
Biology 10:980. DOI: https://doi.org/10.1038/nsb1203-980, PMID: 14634627
Bernetti M, Bussi G. 2020. Pressure control using stochastic cell rescaling. The Journal of Chemical Physics
153:114107. DOI: https://doi.org/10.1063/5.0020514, PMID: 32962386
Bonomi M, Bussi G, Camilloni C, Tribello GA, Banáš P, Barducci A, Bernetti M. 2019. Promoting transparency and
reproducibility in enhanced molecular simulations. Nature Methods 16:670–673. DOI: https://doi.org/10.1038/​
s41592-019-0506-8
Bottaro S, Lindorff-­Larsen K. 2018. Biophysical experiments and biomolecular simulations: A perfect match?
Science 361:355–360. DOI: https://doi.org/10.1126/science.aat4010, PMID: 30049874
Bowers KJ, Chow DE, Xu H, Dror RO, Eastwood MP, Gregersen BA, Klepeis JL, Kolossvary I, Moraes MA,
Sacerdoti FD, Salmon JK, Shan Y, Shaw DE. 2006. Scalable Algorithms for Molecular Dynamics Simulations on
Commodity Clusters. SC 2006 Proceedings Supercomputing. . DOI: https://doi.org/10.1109/SC.2006.54
Bran AM, Cox S, White AD, Schwaller P. 2023 ChemCrow: augmenting large-­language models with chemistry
tools. arXiv. https://arxiv.org/abs/2304.05376
Brooks BR, Brooks CL, Mackerell AD, Nilsson L, Petrella RJ, Roux B, Won Y, Archontis G, Bartels C, Boresch S,
Caflisch A, Caves L, Cui Q, Dinner AR, Feig M, Fischer S, Gao J, Hodoscek M, Im W, Kuczera K, et al. 2009.
CHARMM: the biomolecular simulation program. Journal of Computational Chemistry 30:1545–1614. DOI:
https://doi.org/10.1002/jcc.21287, PMID: 19444816
Burley SK, Kurisu G, Markley JL, Nakamura H, Velankar S, Berman HM, Sali A, Schwede T, Trewhella J. 2017.
PDB-­Dev: A prototype system for depositing integrative/hybrid structural models. Structure 25:1317–1318.
DOI: https://doi.org/10.1016/j.str.2017.08.001, PMID: 28877501
Bussi G, Donadio D, Parrinello M. 2007. Canonical sampling through velocity rescaling. The Journal of Chemical
Physics 126:014101. DOI: https://doi.org/10.1063/1.2408420, PMID: 17212484
Commun Biol. 2023. Reliability and reproducibility checklist for molecular dynamics simulations. Communications
Biology 6:268. DOI: https://doi.org/10.1038/s42003-023-04653-0, PMID: 36918708
Dandekar BR, Mondal J. 2020. Capturing protein-­ligand recognition pathways in coarse-­grained simulation. The
Journal of Physical Chemistry Letters 11:5302–5311. DOI: https://doi.org/10.1021/acs.jpclett.0c01683, PMID:
Di Cosmo R, Zacchiroli S. 2017. Software Heritage: Why and How to Preserve Software Source Code. iPRES
2017 - 14th International Conference on Digital Preservation. 1–10.
Domański J, Stansfeld PJ, Sansom MSP, Beckstein O. 2010. Lipidbook: a public repository for force-­field
parameters used in membrane simulations. The Journal of Membrane Biology 236:255–258. DOI: https://doi.​
org/10.1007/s00232-010-9296-8, PMID: 20700585
Duncan AL, Corey RA, Sansom MSP. 2020. Defining how multiple lipid species interact with inward rectifier
potassium (Kir2) channels. PNAS 117:7803–7813. DOI: https://doi.org/10.1073/pnas.1918387117, PMID:
Dybeck EC, Thiel A, Schnieders MJ, Pickard FC, Wood GPF, Krzyzaniak JF, Hancock BC. 2023. A comparison of
methods for computing relative anhydrous–hydrate stability with molecular simulation. Crystal Growth &
Design 23:142–167. DOI: https://doi.org/10.1021/acs.cgd.2c00832
Elofsson A, Hess B, Lindahl E, Onufriev A, van der Spoel D, Wallqvist A. 2019. Ten simple rules on how to create
open access and reproducible molecular simulations of biological systems. PLOS Computational Biology
15:e1006649. DOI: https://doi.org/10.1371/journal.pcbi.1006649, PMID: 30653494
European Organization For Nuclear Research. 2013. Zenodo. OpenAIRE. https://catalogue.openaire.eu/​
service/openaire.zenodo/overview
Fadda E. 2022. Molecular simulations of complex carbohydrates and glycoconjugates. Current Opinion in
Chemical Biology 69:102175. DOI: https://doi.org/10.1016/j.cbpa.2022.102175, PMID: 35728307
Fan FJ, Shi Y. 2022. Effects of data quality and quantity on deep learning for protein-­ligand binding affinity
prediction. Bioorganic & Medicinal Chemistry 72:117003. DOI: https://doi.org/10.1016/j.bmc.2022.117003
Färber M, Lamprecht D. 2021. The data set knowledge graph: Creating a linked open data source for data sets.
Quantitative Science Studies 2:1324–1355. DOI: https://doi.org/10.1162/qss_a_00161

Fawzi NL, Parekh SH, Mittal J. 2021. Biophysical studies of phase separation integrating experimental and
computational methods. Current Opinion in Structural Biology 70:78–86. DOI: https://doi.org/10.1016/j.sbi.​
2021.04.004, PMID: 34144468
Fuller JC, Jackson RM, Edwards TA, Wilson AJ, Shirts MR. 2012. Modeling of arylamide helix mimetics in the P53
peptide binding site of hDM2 suggests parallel and anti-­parallel conformations are both stable. PLOS ONE
7:e43253. DOI: https://doi.org/10.1371/journal.pone.0043253, PMID: 22916232
Genheden S, Ryde U. 2015. The MM/PBSA and MM/GBSA methods to estimate ligand-­binding affinities. Expert
Opinion on Drug Discovery 10:449–461. DOI: https://doi.org/10.1517/17460441.2015.1032936, PMID:
Gertsen AS, Sørensen MK, Andreasen JW. 2020. Nanostructure of organic semiconductor thin films: Molecular
dynamics modeling with solvent evaporation. Physical Review Materials 4:075405. DOI: https://doi.org/10.​
1103/PhysRevMaterials.4.075405
Gowers R, Linke M, Barnoud J, Reddy T, Melo M, Seyler S, Domański J, Dotson D, Buchoux S, Kenney I,
Beckstein O. 2016. MDAnalysis: A Python Package for the Rapid Analysis of Molecular Dynamics Simulations.
Python in Science Conference. . DOI: https://doi.org/10.25080/Majora-629e541a-00e
Gupta C, Sarkar D, Tieleman DP, Singharoy A. 2022. The ugly, bad, and good stories of large-­scale biomolecular
simulations. Current Opinion in Structural Biology 73:102338. DOI: https://doi.org/10.1016/j.sbi.2022.102338,
PMID: 35245737
Hénin J, Lelièvre T, Shirts MR, Valsson O, Delemotte L. 2022. Enhanced sampling methods for molecular
dynamics simulations [Article v1.0]. Living Journal of Computational Molecular Science 4:1583. DOI: https://​
doi.org/10.33011/livecoms.4.1.1583
Hoch JC, Baskaran K, Burr H, Chin J, Eghbalnia HR, Fujiwara T, Gryk MR, Iwata T, Kojima C, Kurisu G, Maziuk D,
Miyanoiri Y, Wedell JR, Wilburn C, Yao H, Yokochi M. 2023. Biological magnetic resonance data bank. Nucleic
Acids Research 51:D368–D376. DOI: https://doi.org/10.1093/nar/gkac1050, PMID: 36478084
Hollingsworth SA, Dror RO. 2018. Molecular dynamics simulation for all. Neuron 99:1129–1143. DOI: https://​
doi.org/10.1016/j.neuron.2018.08.011, PMID: 30236283
Hospital A, Battistini F, Soliva R, Gelpí JL, Orozco M. 2020. Surviving the deluge of biosimulation data. WIREs
Computational Molecular Science 10:e1449. DOI: https://doi.org/10.1002/wcms.1449
Humphrey W, Dalke A, Schulten K. 1996. VMD: visual molecular dynamics. Journal of Molecular Graphics
14:33–38, . DOI: https://doi.org/10.1016/0263-7855(96)00018-5, PMID: 8744570
Ingólfsson HI, Lopez CA, Uusitalo JJ, de Jong DH, Gopal SM, Periole X, Marrink SJ. 2014. The power of coarse
graining in biomolecular simulations. Wiley Interdisciplinary Reviews. Computational Molecular Science
4:225–248. DOI: https://doi.org/10.1002/wcms.1169, PMID: 25309628
Ivanov P, Mu J, Leay L, Chang SY, Sharrad CA, Masters AJ, Schroeder SLM. 2017. Organic and Third Phase in
HNO3/TBP/n-­Dodecane System: No Reverse Micelles. Solvent Extraction and Ion Exchange 35:251–265. DOI:
https://doi.org/10.1080/07366299.2017.1336048
Jahani F, Torabi S, Chiechi RC, Koster LJA, Hummelen JC. 2014. Fullerene derivatives with increased dielectric
constants. Chemical Communications 50:10645–10647. DOI: https://doi.org/10.1039/c4cc04366a, PMID:
Jeon JH, Javanainen M, Martinez-­Seara H, Metzler R, Vattulainen I. 2016. Protein crowding in lipid bilayers gives
rise to non-­gaussian anomalous lateral diffusion of phospholipids and proteins. Physical Review X 6:021006.
DOI: https://doi.org/10.1103/PhysRevX.6.021006
Johns Hopkins University. 2020. COVID-­19 data repository by the center for systems science and engineering
(CSSE) at johns hopkins university [GitHub]. . https://github.com/CSSEGISandData/COVID-19
Jumper J, Evans R, Pritzel A, Green T, Figurnov M, Ronneberger O, Tunyasuvunakool K, Bates R, Žídek A,
Potapenko A, Bridgland A, Meyer C, Kohl SAA, Ballard AJ, Cowie A, Romera-­Paredes B, Nikolov S, Jain R,
Adler J, Back T, et al. 2021. Highly accurate protein structure prediction with AlphaFold. Nature 596:583–589.
DOI: https://doi.org/10.1038/s41586-021-03819-2, PMID: 34265844
Kabelka I, Brožek R, Vácha R. 2021. Selecting collective variables and free-­energy methods for peptide
translocation across membranes. Journal of Chemical Information and Modeling 61:819–830. DOI: https://doi.​
org/10.1021/acs.jcim.0c01312, PMID: 33566605
Kampfrath M, Staritzbichler R, Hernández GP, Rose AS, Tiemann JKS, Scheuermann G, Wiegreffe D,
Hildebrand PW. 2022. MDsrv: visual sharing and analysis of molecular dynamics simulations. Nucleic Acids
Research 50:W483–W489. DOI: https://doi.org/10.1093/nar/gkac398, PMID: 35639717
Karunasena C, Li S, Heifner MC, Ryno SM, Risko C. 2021. Reconsidering the roles of noncovalent intramolecular
“locks” in π-conjugated molecules. Chemistry of Materials 33:9139–9151. DOI: https://doi.org/10.1021/acs.​
chemmater.1c02335
Kelly BD, Smith WR. 2020. Alchemical hydration free-­energy calculations using molecular dynamics with explicit
polarization and induced polarity decoupling: An on-­the-­fly polarization approach. Journal of Chemical Theory
and Computation 16:1146–1161. DOI: https://doi.org/10.1021/acs.jctc.9b01139, PMID: 31930918
Kiirikki A, Antila H, Bort L, Buslaev P, Fernando F, Mendes Ferreira T, Fuchs P, Garcia-­Fandino R, Gushchin I,
Kav B, Kučerka N, Kula P, Kurki M, Kuzmin A, Madsen J, Miettinen M, Nencini R, Piggot T, Pineiro A,
Suarez-­Leston F, et al. 2023. NMRlipids Databank Makes Data-­Driven Analysis of Biomembrane Properties
Accessible for All. ChemRxiv. DOI: https://doi.org/10.26434/chemrxiv-2023-jrpwm-v2
Kinjo AR, Bekker GJ, Suzuki H, Tsuchiya Y, Kawabata T, Ikegawa Y, Nakamura H. 2017. Protein Data Bank Japan
(PDBj): updated user interfaces, resource description framework, analysis tools for large structures. Nucleic
Acids Research 45:D282–D288. DOI: https://doi.org/10.1093/nar/gkw962, PMID: 27789697

Kirschner KN, Yongye AB, Tschampel SM, González-­Outeiriño J, Daniels CR, Foley BL, Woods RJ. 2008.
GLYCAM06: a generalizable biomolecular force field. Carbohydrates. Journal of Computational Chemistry
29:622–655. DOI: https://doi.org/10.1002/jcc.20820, PMID: 17849372
Krishna S, Sreedhar I, Patel CM. 2021. Molecular dynamics simulation of polyamide-­based materials – A review.
Computational Materials Science 200:110853. DOI: https://doi.org/10.1016/j.commatsci.2021.110853
Kümmerer F, Orioli S, Harding-­Larsen D, Hoffmann F, Gavrilov Y, Teilum K, Lindorff-­Larsen K. 2021. Fitting
side-­chain nmr relaxation data using molecular simulations. Journal of Chemical Theory and Computation
17:5262–5275. DOI: https://doi.org/10.1021/acs.jctc.0c01338, PMID: 34291646
Kyrychenko A, Karpushina GV, Svechkarev D, Kolodezny D, Bogatyrenko SI, Kryshtal AP, Doroshenko AO. 2012.
Fluorescence probing of thiol-­functionalized gold nanoparticles: Is alkylthiol coating of a nanoparticle as
hydrophobic as expected? The Journal of Physical Chemistry C 116:21059–21068. DOI: https://doi.org/10.​
1021/jp3060813
Lane TJ. 2023. Protein structure prediction has reached the single-­structure frontier. Nature Methods 20:170–
173. DOI: https://doi.org/10.1038/s41592-022-01760-4, PMID: 36639584
Liu S, Cao S, Hoang K, Young KL, Paluch AS, Mobley DL. 2016. Using MD simulations to calculate how solvents
modulate solubility. Journal of Chemical Theory and Computation 12:1930–1941. DOI: https://doi.org/10.​
1021/acs.jctc.5b00934, PMID: 26878198
Mahmud M, Kaiser MS, McGinnity TM, Hussain A. 2021. Deep learning in mining biological data. Cognitive
Computation 13:1–33. DOI: https://doi.org/10.1007/s12559-020-09773-x, PMID: 33425045
Marklund EG, Benesch JL. 2019. Weighing-­up protein dynamics: the combination of native mass spectrometry
and molecular dynamics simulations. Current Opinion in Structural Biology 54:50–58. DOI: https://doi.org/10.​
1016/j.sbi.2018.12.011
Martinez X, Baaden M. 2021. UnityMol prototype for FAIR sharing of molecular-­visualization experiences: from
pictures in the cloud to collaborative virtual reality exploration in immersive 3D environments. Acta
Crystallographica. Section D, Structural Biology 77:746–754. DOI: https://doi.org/10.1107/​
S2059798321002941, PMID: 34076589
Marx V. 2013. Biology: The big challenges of big data. Nature 498:255–260. DOI: https://doi.org/10.1038/​
498255a, PMID: 23765498
McKinney W. 2010. Data Structures for Statistical Computing in Python. Python in Science Conference. 56–61.
DOI: https://doi.org/10.25080/Majora-92bf1922-00a
Merz KM, Amaro R, Cournia Z, Rarey M, Soares T, Tropsha A, Wahab HA, Wang R. 2020. Editorial: Method and
data sharing and reproducibility of scientific results. Journal of Chemical Information and Modeling 60:5868–
5869. DOI: https://doi.org/10.1021/acs.jcim.0c01389, PMID: 33378854
Meyer T, D’Abramo M, Hospital A, Rueda M, Ferrer-­Costa C, Pérez A, Carrillo O, Camps J, Fenollosa C,
Repchevsky D, Gelpí JL, Orozco M. 2010. MoDEL (Molecular Dynamics Extended Library): a database of
atomistic molecular dynamics trajectories. Structure 18:1399–1409. DOI: https://doi.org/10.1016/j.str.2010.07.​
013, PMID: 21070939
Michaud-­Agrawal N, Denning EJ, Woolf TB, Beckstein O. 2011. MDAnalysis: A toolkit for the analysis of
molecular dynamics simulations. Journal of Computational Chemistry 32:2319–2327. DOI: https://doi.org/10.​
1002/jcc.21787, PMID: 21500218
Miksa T, Simms S, Mietchen D, Jones S. 2019. Ten principles for machine-­actionable data management plans.
PLOS Computational Biology 15:e1006750. DOI: https://doi.org/10.1371/journal.pcbi.1006750, PMID:
Mulholland AJ, Amaro RE. 2020. COVID19 - Computational Chemists Meet the Moment. Journal of Chemical
Information and Modeling 60:5724–5726. DOI: https://doi.org/10.1021/acs.jcim.0c01395, PMID: 33378852
Musen MA. 2022. Without appropriate metadata, data-­sharing mandates are pointless. Nature 609:222. DOI:
https://doi.org/10.1038/d41586-022-02820-7, PMID: 36064801
Newport TD, Sansom MSP, Stansfeld PJ. 2019. The MemProtMD database: a resource for membrane-­embedded
protein structures and their lipid interactions. Nucleic Acids Research 47:D390–D397. DOI: https://doi.org/10.​
1093/nar/gky1047
Oliphant TE. 2007. Python for scientific computing. Computing in Science & Engineering 9:10–20. DOI: https://​
doi.org/10.1109/MCSE.2007.58
Panero P, Benito J. 2022 OpenAIRE webinar: Zenodo - open digital repository. Version v1. Zenodo. https://doi.​
org/10.5281/zenodo.7417839
Parrinello M, Rahman A. 1981. Polymorphic transitions in single crystals: A new molecular dynamics method.
Journal of Applied Physics 52:7182–7190. DOI: https://doi.org/10.1063/1.328693
Perera N, Dehmer M, Emmert-­Streib F. 2020. Named entity recognition and relation detection for biomedical
information extraction. Frontiers in Cell and Developmental Biology 8:673. DOI: https://doi.org/10.3389/fcell.​
2020.00673, PMID: 32984300
Perilla JR, Goh BC, Cassidy CK, Liu B, Bernardi RC, Rudack T, Yu H, Wu Z, Schulten K. 2015. Molecular dynamics
simulations of large macromolecular complexes. Current Opinion in Structural Biology 31:64–74. DOI: https://​
doi.org/10.1016/j.sbi.2015.03.007, PMID: 25845770
Perkel J. 2016. Democratic databases: science on GitHub. Nature 538:127–128. DOI: https://doi.org/10.1038/​
538127a, PMID: 27708327
Pesce F, Lindorff-­Larsen K. 2023. Combining Experiments and Simulations to Examine the Temperature-­
Dependent Behaviour of a Disordered Protein. bioRxiv. DOI: https://doi.org/10.1101/2023.03.04.531094

Pettersen EF, Goddard TD, Huang CC, Couch GS, Greenblatt DM, Meng EC, Ferrin TE. 2004. UCSF Chimera--A
visualization system for exploratory research and analysis. Journal of Computational Chemistry 25:1605–1612.
DOI: https://doi.org/10.1002/jcc.20084, PMID: 15264254
Phillips JC, Hardy DJ, Maia JDC, Stone JE, Ribeiro JV, Bernardi RC, Buch R, Fiorin G, Hénin J, Jiang W,
McGreevy R, Melo MCR, Radak BK, Skeel RD, Singharoy A, Wang Y, Roux B, Aksimentiev A, Luthey-­Schulten Z,
Kalé LV, et al. 2020. Scalable molecular dynamics on CPU and GPU architectures with NAMD. The Journal of
Chemical Physics 153:044130. DOI: https://doi.org/10.1063/5.0014475, PMID: 32752662
Piskorz TK, Gobbo C, Marrink SJ, De Feyter S, de Vries AH, van Esch JH. 2019. Nucleation mechanisms of
self-­assembled physisorbed monolayers on graphite. The Journal of Physical Chemistry C 123:17510–17520.
DOI: https://doi.org/10.1021/acs.jpcc.9b01234
Pohjolainen E, Chen X, Malola S, Groenhof G, Häkkinen H. 2016. A Unified AMBER-­compatible molecular
mechanics force field for thiolate-­protected gold nanoclusters. Journal of Chemical Theory and Computation
12:1342–1350. DOI: https://doi.org/10.1021/acs.jctc.5b01053, PMID: 26845636
Porubsky VL, Goldberg AP, Rampadarath AK, Nickerson DP, Karr JR, Sauro HM. 2020. Best practices for making
reproducible biochemical models. Cell Systems 11:109–120. DOI: https://doi.org/10.1016/j.cels.2020.06.012,
PMID: 32853539
Poulain P. 2023. MDverse data analysis swh:1:rev:4562c50d1b51a51fdf952ae6e9efaa407dd06e20. Software
Heritage. https://archive.softwareheritage.org/swh:1:dir:fc72ac7a9c9f0489a361cb2b7fcf8ba48898e4ee;origin=​
https://github.com/MDverse/mdda;visit=swh:1:snp:dbfe8b4401ac98d3728ebb00241429274c619beb;anchor=​
swh:1:rev:4562c50d1b51a51fdf952ae6e9efaa407dd06e20
Poulain P, Bouarroudj L, Tiemann JKS, Bussi G. 2023. MDverse web scrapper.
swh:1:rev:0524199041e84be2d69993540ad8e2223d3b4698. Software Heritage. https://archive.​
softwareheritage.org/swh:1:dir:ce91602834cf79e634d26aff585a9fea22b0fea3;origin=https://github.com/​
MDverse/mdws;visit=swh:1:snp:540580756b211c116bd602423e0262d3055b8251;anchor=swh:1:rev:05241990​
41e84be2d69993540ad8e2223d3b4698
Poulain P, Oussaren M. 2023. MDverse data explorer. swh:1:rev:52604906f80f96b27fd61209a78a93cd36be9a45.
Software Heritage. https://archive.softwareheritage.org/swh:1:dir:1fc8b8eaabf4a9087e6d5b0ec5ed9703​
1482bcbf;origin=https://github.com/MDverse/mdde;visit=swh:1:snp:5a3326fd135f604290fb799470f52438​
4a959b04;anchor=swh:1:rev:52604906f80f96b27fd61209a78a93cd36be9a45
Qiu L, Liu J, Alessandri R, Qiu X, Koopmans M, Havenith RWA, Marrink SJ, Chiechi RC, Anton Koster LJ,
Hummelen JC. 2017. Enhancing doping efficiency by improving host-­dopant miscibility for fullerene-­based
n-­type thermoelectrics. Journal of Materials Chemistry A 5:21234–21241. DOI: https://doi.org/10.1039/​
C7TA06609K
Rodríguez-­Espigares I, Torrens-­Fontanals M, Tiemann JKS, Aranda-­García D, Ramírez-­Anguita JM,
Stepniewski TM, Worp N, Varela-­Rial A, Morales-­Pastor A, Medel-­Lacruz B, Pándy-­Szekeres G, Mayol E,
Giorgino T, Carlsson J, Deupi X, Filipek S, Filizola M, Gómez-­Tamayo JC, Gonzalez A, Gutiérrez-­de-­Terán H,
et al. 2020. GPCRmd uncovers the dynamics of the 3D-­GPCRome. Nature Methods 17:777–787. DOI: https://​
doi.org/10.1038/s41592-020-0884-y, PMID: 32661425
Salomon‐Ferrer R, Case DA, Walker RC. 2013. An overview of the Amber biomolecular simulation package.
WIREs Computational Molecular Science 3:198–210. DOI: https://doi.org/10.1002/wcms.1121
Sami S, Alessandri R, W. Wijaya JB, Grünewald F, de Vries AH, Marrink SJ, Broer R, Havenith RWA. 2022.
Strategies for enhancing the dielectric constant of organic materials. The Journal of Physical Chemistry C
126:19462–19469. DOI: https://doi.org/10.1021/acs.jpcc.2c05682
Sarkar A, Sasmal R, Empereur-­mot C, Bochicchio D, Kompella SVK, Sharma K, Dhiman S, Sundaram B, Agasti SS,
Pavan GM, George SJ. 2020. Self-­sorted, random, and block supramolecular copolymers via sequence
controlled, multicomponent self-­assembly. Journal of the American Chemical Society 142:7606–7617. DOI:
https://doi.org/10.1021/jacs.0c01822
Schaefer SL, Hummer G. 2022. Sublytic gasdermin-­D pores captured in atomistic molecular simulations. eLife
11:e81432. DOI: https://doi.org/10.7554/eLife.81432, PMID: 36374182
Souza PCT, Alessandri R, Barnoud J, Thallmair S, Faustino I, Grünewald F, Patmanidis I, Abdizadeh H,
Bruininks BMH, Wassenaar TA, Kroon PC, Melcr J, Nieto V, Corradi V, Khan HM, Domański J, Javanainen M,
Martinez-­Seara H, Reuter N, Best RB, et al. 2021. Martini 3: a general purpose force field for coarse-­grained
molecular dynamics. Nature Methods 18:382–388. DOI: https://doi.org/10.1038/s41592-021-01098-3, PMID:
Stansfeld PJ, Goose JE, Caffrey M, Carpenter EP, Parker JL, Newstead S, Sansom MSP. 2015. MemProtMD:
Automated insertion of membrane protein structures into explicit lipid membranes. Structure 23:1350–1361.
DOI: https://doi.org/10.1016/j.str.2015.05.006, PMID: 26073602
Stephens ZD, Lee SY, Faghri F, Campbell RH, Zhai C, Efron MJ, Iyer R, Schatz MC, Sinha S, Robinson GE. 2015.
Big data: Astronomical or genomical? PLOS Biology 13:e1002195. DOI: https://doi.org/10.1371/journal.pbio.​
1002195, PMID: 26151137
Sud M, Fahy E, Cotter D, Brown A, Dennis EA, Glass CK, Merrill AH Jr, Murphy RC, Raetz CRH, Russell DW,
Subramaniam S. 2007. LMSD: LIPID MAPS structure database. Nucleic Acids Research 35:D527–D532. DOI:
https://doi.org/10.1093/nar/gkl838, PMID: 17098933
Tai K, Murdock S, Wu B, Ng MH, Johnston S, Fangohr H, Cox SJ, Jeffreys P, Essex JW, P. Sansom MS. 2004.
BioSimGrid: towards a worldwide repository for biomolecular simulations. Organic &Biomolecular Chemistry
2:3219. DOI: https://doi.org/10.1039/b411352g

Tiemann JKS, Guixà-González R, Hildebrand PW, Rose AS. 2017. MDsrv: viewing and sharing molecular
dynamics simulations on the web. Nature Methods 14:1123–1124. DOI: https://doi.org/10.1038/nmeth.4497,
PMID: 29190271
UniProt Consortium. 2022. UniProt: The universal protein knowledgebase in 2023. Nucleic Acids Research
51:D523–D531. DOI: https://doi.org/10.1093/nar/gkac1052
Vanommeslaeghe K, MacKerell AD. 2012. Automation of the CHARMM General Force Field (CGenFF) I: bond
perception and atom typing. Journal of Chemical Information and Modeling 52:3144–3154. DOI: https://doi.​
org/10.1021/ci300363c, PMID: 23146088
van Rossum G. 1995. Python Tutorial. Amsterdam, The Netherlands: Centrum voor Wiskunde en Informatica.
https://ir.cwi.nl/pub/5007
Virtanen SI, Kiirikki AM, Mikula KM, Iwaï H, Ollila OHS. 2020. Heterogeneous dynamics in partially disordered
proteins. Physical Chemistry Chemical Physics 22:21185–21196. DOI: https://doi.org/10.1039/d0cp03473h,
PMID: 32929427
Vuorio J, Vattulainen I, Martinez-­Seara H. 2017. Atomistic fingerprint of hyaluronan-­CD44 binding. PLOS
Computational Biology 13:e1005663. DOI: https://doi.org/10.1371/journal.pcbi.1005663, PMID: 28715483
Waltemath D, Adams R, Beard DA, Bergmann FT, Bhalla US, Britten R, Chelliah V, Cooling MT, Cooper J,
Crampin EJ, Garny A, Hoops S, Hucka M, Hunter P, Klipp E, Laibe C, Miller AK, Moraru I, Nickerson D,
Nielsen P, et al. 2011. Minimum Information About a Simulation Experiment (MIASE). PLOS Computational
Biology 7:e1001122. DOI: https://doi.org/10.1371/journal.pcbi.1001122
Wang J, Wolf RM, Caldwell JW, Kollman PA, Case DA. 2004. Development and testing of a general amber force
field. Journal of Computational Chemistry 25:1157–1174. DOI: https://doi.org/10.1002/jcc.20035, PMID:
Wilkinson MD, Dumontier M, Aalbersberg IJJ, Appleton G, Axton M, Baak A, Blomberg N, Boiten JW,
da Silva Santos LB, Bourne PE, Bouwman J, Brookes AJ, Clark T, Crosas M, Dillo I, Dumon O, Edmunds S,
Evelo CT, Finkers R, Gonzalez-­Beltran A, et al. 2016. The FAIR Guiding Principles for scientific data
management and stewardship. Scientific Data 3:160018. DOI: https://doi.org/10.1038/sdata.2016.18, PMID:
Wilson SL, Way GP, Bittremieux W, Armache JP, Haendel MA, Hoffman MM. 2021. Sharing biological data: why,
when, and how. FEBS Letters 595:847–863. DOI: https://doi.org/10.1002/1873-3468.14067, PMID: 33843054
Yoo J, Winogradoff D, Aksimentiev A. 2020. Molecular dynamics simulations of DNA-­DNA and DNA-­protein
interactions. Current Opinion in Structural Biology 64:88–96. DOI: https://doi.org/10.1016/j.sbi.2020.06.007,
PMID: 32682257
Young TA, Martí-Centelles V, Wang J, Lusby PJ, Duarte F. 2020. RAtionalizing the activity of an “artificial
diels-­alderase”: Establishing efficient and accurate protocols for calculating supramolecular catalysis. Journal of
the American Chemical Society 142:1300–1310. DOI: https://doi.org/10.1021/jacs.9b10302, PMID: 31852191
Zheng X, Chan MHY, Chan AKW, Cao S, Ng M, Sheong FK, Li C, Goonetilleke EC, Lam WWY, Lau TC, Huang X,
Yam VWW. 2022. Elucidation of the key role of Pt···Pt interactions in the directional self-­assembly of platinum(II)
complexes. PNAS 119:e2116543119. DOI: https://doi.org/10.1073/pnas.2116543119, PMID: 35298336
Zhu S. 2019. Validation of the Generalized Force Fields GAFF, CGenFF, OPLS-­AA, and PRODRGFF by Testing
Against Experimental Osmotic Coefficient Data for Small Drug-­Like Molecules. Journal of Chemical Information
and Modeling 59:4239–4247. DOI: https://doi.org/10.1021/acs.jcim.9b00552
Zhu J, Salvatella X, Robustelli P. 2022. Small molecules targeting the disordered transactivation domain of the
androgen receptor induce the formation of collapsed helical states. Nature Communications 13:6390. DOI:
https://doi.org/10.1038/s41467-022-34077-z, PMID: 36302916


---

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


---

# Best Practices for Foundations in Molecular Simulations [Article v1.0]

**Authors:** Efrem Braun, Justin Gilmer, Heather B. Mayes, David L. Mobley, Jacob I. Monroe, Samarjeet Prasad, Daniel M. Zuckerman
**Year:** 2019
**Venue:** Living Journal of Computational Molecular Science
**DOI:** 10.33011/livecoms.1.1.5957
**Source PDF URL:** https://livecomsjournal.org/index.php/livecoms/article/download/v1i1e5957/939 (LiveCoMS diamond OA journal, direct PDF)
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Best Practices for Foundations in
Molecular Simulations [Article v1.0]
Efrem Braun1 , Justin Gilmer2 , Heather B. Mayes3 , David L. Mobley4 , Jacob I.
Monroe5 , Samarjeet Prasad6 , Daniel M. Zuckerman7
1 University of California, Berkeley; 2 Vanderbilt University; 3 University of Michigan, Ann

Arbor; 4 University of California, Irvine; 5 University of California, Santa Barbara; 6 National
Institutes of Health; 6 Johns Hopkins University, Baltimore; 7 Oregon Health and Science
University

This LiveCoMS document is
maintained online on
GitHub at https:
//github.com/MobleyLab/
basic_simulation_training;
to provide feedback,
suggestions, or help
improve it, please visit the
GitHub repository and
participate via the issue
tracker.
This version dated
December 29, 2018

Abstract This document provides a starting point for approaching molecular simulations, guiding
beginning practitioners to what issues they need to know about before and while starting their ﬁrst
simulations, and why those issues are so critical. This document makes no claims to provide an
adequate introduction to the subject on its own. Instead, our goal is to help people know what
issues are critical before beginning, and to provide references to good resources on those topics. We
also provide a checklist of key issues to consider before and while setting up molecular simulations
which may serve as a foundation for other best practices documents.

*For correspondence:
efrem.braun@berkeley.edu (EB); justin.b.gilmer@vanderbilt.edu (JG); hbmayes@umich.edu (HM);
dmobley@mobleylab.org (DLM); jimonroe@umail.ucsb.edu (JIM); samarjeet@jhmi.edu (SP);
zuckermd@ohsu.edu (DMZ)

Introduction

Molecular simulation techniques play an important role in
our quest to understand and predict the properties, structure,
and function of molecular systems, and are a key tool as
we seek to enable predictive molecular design. Simulation
methods are useful for studying the structure and dynamics
of complex systems that are too complicated for pen and
paper theory, helping interpret experimental data in terms of
molecular motions. Additionally, they are increasingly used
for quantitative prediction of properties of use in molecular
design and other applications [1–5].
The basic idea of any molecular simulation method is
straightforward; a particle-based description of the system
under investigation is constructed and then the system is
propagated by either deterministic or probabilistic rules to
generate a trajectory describing its evolution over the course

Received: 2 August 2018
Accepted: 9 November 2018

of the simulation [6, 7]. Relevant properties can be calculated
for each “snapshot” (a stored conﬁguration of the system,
also called a “frame”) and averaged over the entire trajectory
to compute estimates of desired properties.
Depending on how the system is propagated, molecular
simulation methods can be divided into two main categories:
Molecular Dynamics (MD) and Monte Carlo (MC). With MD
methods, the equations of motion are numerically integrated
to generate a dynamical trajectory of the system. MD simulations can be used for investigating structural, dynamic, and
thermodynamic properties of the system. With MC methods,
probabilistic rules are used to generate a new conﬁguration
from the present conﬁguration and this process is repeated
to generate a sequence of states that can be used to calculate
structural and thermodynamic properties but not dynamical
properties; indeed, MC simulations lack any concept of time.

Thus, the “dynamics” produced by an MC method are not
the temporal dynamics of the system, but the ensemble of
conﬁgurations that reﬂect those that could be dynamically
sampled. This foundational document will focus on the concepts needed to carry out correct MD simulations that utilize
good practices. Many, but not all, of the concepts here are
also useful for MC simulations and apply there as well. However, there are a number of key differences, which are outside
the scope of this current document.
Either method can be carried out with different underlying
physical theories to describe the particle-based model of the
system under investigation. If a quantum mechanics (QM)
description of matter is used, electrons are explicitly represented in the model and interaction energy is calculated by
solving the electronic structure of the molecules in the system with no (or few) empirical parameters, but with various
approximations to the physics for tractability. In a molecular mechanics (MM) description, molecules are represented
by particles representing atoms or groups of atoms. Each
atom may be assigned an electric charge and a potential energy function with a large number of empirical parameters
(ﬁtted to experiment, QM, or other data) used to calculate
non-bonded and bonded interactions. Unless otherwise speciﬁed, MD simulations employ MM force ﬁelds, which calculate
the forces that determine the system dynamics. MM simulations are much faster than quantum simulations, making
them the methods of choice for vast majority of molecular
simulation studies on biomolecular systems in the condensed
phase. However, typically, they are of lower accuracy than QM
simulations and cannot simulate bond rearrangements. QM
simulations may be too computationally expensive to allow
simulations of the time and length scales required to describe
the system of interest [5]. The size of the system amenable for
to QM simulation also depends on what method is chosen,
from high-level ab initio methods to semi-empirical methods; discussion of these methods are outside the scope of
this article, and useful references are separately available [8].
Computational resources available are also an important consideration in deciding whether QM simulations are tractable.
Roughly, QM simulations might be tractable with hundreds
of atoms or fewer, while MD simulations routinely have tens
or hundreds of thousands of atoms in the system. Much
above that level, coarse-graining methods are used. They
reduce resolution and computational cost. Although many
of the approaches for atomistic simulations discussed here
can apply to coarse-grained simulations, such simulations
are not the focus of this paper and we will not discuss how
coarse-grained simulations are initially built.
Speed is a particular concern when describing condensed
phase systems, as we are often interested in the properties
of molecules (even biomacromolecules) in solution, mean-

ing that systems will consist of thousands to hundreds of
thousands or millions of atoms. While system size alone
does not dictate a classical description, if we are interested
in calculations of free energies or transport properties at ﬁnite (often laboratory) temperatures, these include entropic
contributions (as further discussed below) meaning that ﬂuctuations and correlations of motions within the system affect
computed properties, meaning that simulations must not
only sample single optimal states but instead must sample
the correct distribution of states – requiring simulations of
some length. Furthermore, many systems of interest, such as
polymers (biological and otherwise) have slow motions that
must be captured for accurate calculation of properties. For
example, for proteins, relevant timescales span from nanoseconds to seconds or more, and even rearrangements of buried
amino acid sidechains can in some cases take microseconds
or more, with larger conformational changes and protein folding taking even longer [9, 10]. Recent hardware innovations
have made microsecond-length simulations for biological systems of 50-100,000 atoms relatively routine, and herculean
efforts have pushed the longest simulations out past the millisecond range. However, the ﬁeld would like to reach even
longer timescales, meaning that switching to a more detailed
energy model is only done with some trepidation because
slower energy evaluations mean less time available for sampling. Thus the need for speed limits the use of quantum
mechanical descriptions.
Thus, for the rest of this document we will restrict ourselves to classical MD.
One other important note is that, within classical molecular simulations, bond breaking and forming is generally not
allowed (with notable exceptions such as reactive force ﬁelds),
meaning that the topology or chemistry of a system will remain constant as a function of time. That is, the particles
comprising the system move around, but the chemical identity of each molecule in the system remains a constant over
the course of the simulation (with only partial exceptions,
such as the case of constant pH simulations [11]). This also
means that the notion of pH in molecular simulations primarily refers to the selection of ﬁxed protonation states for the
components of the system.
Here, we ﬁrst discuss the scope of this document, then
go over some of the fundamental concepts or science topics
which provide the underpinnings of molecular simulations,
giving references for further reading. Then, we introduce a
variety of basic simulation concepts and terminology, with
links to further reading. Our goal is not to cover all topics,
but to provide some guidance for the critical issues which
must be considered. We also provide a checklist to assist with
preparing for and beginning a modeling project, highlighting
some key considerations addressed in this work.

• Point particles and rigid bodies
• Holonomic constraints

Scope of this document

There are several excellent textbooks on classical simulation
methods; some we have found particularly helpful are Allen
and Tildesley’s “Computer Simulations of Liquids” [12], Leach’s
“Molecular Modelling” [7], and Frenkel and Smit’s “Understanding Molecular Simulations” [6], though there are many
other sources. Tuckerman’s “Statistical Mechanics: Theory
and Molecular Simulation” [13] may be helpful to a more
advanced audience.
In principle, anyone with adequate prior knowledge
(namely, undergraduate level calculus and physics) should be
able to pick up one of these books and learn the required
skills to perform molecular simulations, perhaps with help
from a good statistical mechanics and thermodynamics
book or two. In practice, due to the interdisciplinary and
somewhat technical nature of this ﬁeld, many newcomers
may ﬁnd it diﬃcult and time consuming to understand all
the methodological issues involved in a simulation study.
The goal of this document is to introduce a new practitioner
to some key basic concepts and bare minimum scientiﬁc
knowledge required for correct execution of these methods.
We also provide a basic set of “best practices” that can be
used to avoid common errors, missteps and confusion in
elementary molecular simulations work. This document
is not meant as a full introduction to the area; rather, it
is intended to help guide further study, and to provide
a foundation for other more specialized best-practices
documents focusing on particular simulation areas.
Modern implementations of classical simulations also rely
on a large body of knowledge from the ﬁelds of computer
science, programming, and numerical methods, which will
not be covered in detail here.

Science topics

A new practitioner does not have to be an expert in all of the
ﬁelds that provide the foundation for our simulation methods and analysis of the data produced by these methods.
However, grasping some key concepts from each of these
disciplines, described below, is essential. This section serves
as a preface for Section 4 and suggestions for further reading
on these subjects are provided throughout the document. In
each subsection, we begin by highlighting some of the critical
topics from the corresponding area, then describe what these
are and why they are important to molecular simulations.

3.1

Classical mechanics

3.1.1

Key concepts

Critical concepts from classical mechanics include:

Molecular simulation methods work on many-particle systems following the rules of classical mechanics. Basic knowledge of key concepts of classical mechanics is important for
understanding simulation methods. Here, we will assume
you are already familiar with Newtonian mechanics.
Classical molecular models typically consist of point particles carrying mass and electric charge with bonded interactions (describing bond lengths, angles, and torsions) and
non-bonded interactions (describing electrostatic and van der
Waals forces). Sometimes it is much more eﬃcient to freeze
the internal degrees of freedom and treat the molecule as
a rigid body where the particles do not change their relative orientation as the whole body moves; this is commonly
done, for example, for rigid models of the water molecule.
The timestep for simulation is determined by the fastest frequency motion. Due to the high frequency of the O-H vibrations, accurately treating water classically would require solving the equations of motion with a small timestep (commonly
1 fs). Thus, for computational eﬃciency water is often instead
treated as a rigid body to allow a larger timestep (often double the length). Keeping speciﬁed objects rigid in a simulation
involves applying holonomic constraints, where the rigidity is
deﬁned by imposing a minimal set of ﬁxed bond lengths and
angles through iterative procedures during the numerical integration of the equation of motion (see Section 4.6 for more
on constraints and integrators).
Classical mechanics has several mathematical formulations, namely the Newtonian, Hamiltonian and Lagrangian
formulations. These formulations are physically equivalent,
but for certain applications one formulation can be more appropriate than the other. Many simulation methods use the
Hamiltonian formulation and therefore basic knowledge of
Hamiltonian mechanics is particularly important.
Classical mechanics has several conserved quantities and
simulators should be familiar with these, for example, the total energy of a system is a constant of motion. These concepts
play an important role in development and proper implementation of simulation methods. For example, a particularly
straightforward check of the correctness of an MD code is to
test whether energy is conserved.
Most books on molecular simulations have a short discussion or appendices on classical mechanics that can serve the
purpose of quick introductions to the basic concepts; Shell’s
book also has a chapter on simulation methods which covers
some of these details [14]. A variety of good books on classical mechanics are also available and give further details on
these concepts.

• Newton’s equations of motion
• Hamilton’s equations

3.2

Thermodynamics

3.2.1

Key concepts

A variety of thermodynamic concepts are important for molecular simulations:
• Temperature and pressure
• Internal energy and enthalpy
• Gibbs and Helmholtz free energy
• Entropy
One of the main objectives of molecular simulations is to
estimate/predict thermodynamic behavior of real systems as
observed in the laboratory. Typically this means we are interested in macroscopic systems, consisting of 1023 particles or
more (i.e. at least a mole of particles). But properties of interest include not only macroscopic, bulk thermodynamic properties, such as density or heat capacity, but also microscopic
properties like speciﬁc free energy differences associated
with, say, changes in the conformation of a molecule. For this
reason, it is important to understand key concepts in thermodynamics, such as temperature, pressure, entropy, internal
energy, various forms of free energy, and the relationships
between them. Paramount, however, is an understanding
of the connection between thermodynamics and statistical
mechanics, which allows us to relate macroscopic, experimental measurements to the behavior of the much smaller
system that is simulated. This topic involves a variety of subtleties and thus can be a confusing and diﬃcult, so we refer
the reader to a more extensive discussion in one of several
books [14, 15].
As an example, consider temperature. In a macroscopic
sense, we understand this quantity intuitively as how hot or
cold something is. The laws of thermodynamics provide us
with a further abstraction, telling us that this is in fact the
derivative of the internal energy with respect to the entropy.
This mathematical deﬁnition itself is not particularly helpful,
but provides a starting point for other derivations. If we
want to understand temperature from the point of view of
understanding molecular behavior, we ﬁnally must turn to
statistical mechanics. Since molecular dynamics is mostly
used to simulate behavior at the molecular or atomistic level,
it is necessary to utilize statistical-mechanical expressions
in computing what would be observed as the macroscopic,
thermodynamic temperature.
This discussion should not provide the impression that
statistical mechanics is more important than thermodynamics. The two are intimately connected and we must rely on
both to successfully conduct and obtain information from
MD simulations. In particular, thermodynamics provides rigid
rules that must be satisﬁed if we are to faithfully reproduce
reality. For instance, if energy is not conserved, the ﬁrst law is
not satisﬁed and we are for sure simulating a system out of

equilibrium (i.e. we are somehow adding or removing energy).
In this sense, the laws of thermodynamics provide us rigorous sanity checks in addition to many useful mathematical
relations for computing properties. Basic thermodynamic
principles thus also dictate proper simulation protocols and
associated best practices.
The concept of the thermodynamic limit is important here.
Speciﬁcally, as the size of a ﬁnite system is increased, keeping
the particle number density roughly constant, at some point it
is said to reach the thermodynamic limit where its behavior is
bulk-like and no longer depends on the extent of the system.
Thus, small systems will exhibit unique behaviors that reﬂect
their microscopic size, but suﬃciently large systems are said
to have reached the thermodynamic limit and macroscopic
thermodynamics applied. This is due to the fact that the effect
of interfaces or boundaries have largely been removed, and,
more importantly, that averages of system properties are
now over a suﬃciently large number of molecules that any
instantaneous snapshot of the system roughly corresponds
to average behavior (i.e. ﬂuctuations in properties become
negligible with increasing system size).
Although we usually think of thermodynamics applying
macroscopically and statistical mechanics applying on the
microsopic level, it is important to remember that the laws of
thermodynamics still hold on average regardless of the length
scale. That is, a molecule in contact with a thermal bath will
exchange energy with the bath, but its average energy is a
well-deﬁned constant. This allows us to deﬁne thermodynamic quantities associated with microscopic events, such as
the binding of a ligand to a protein. This is useful because it
allows us to assign molecular meaning to well-deﬁned thermodynamic processes that can only be indirectly probed by
experiment. Importantly, as long as we have carefully deﬁned
our ensemble and thermodynamic path, we can apply the
powerful relationships of thermodynamics to more easily calculate many properties of interest. For instance, one may use
molecular dynamics to eﬃciently numerically integrate the
Clapeyron equation and construct equations of state along
phase coexistence curves [16, 17].

3.2.2

Books

Equilibrium thermodynamics is taught in most undergraduate programs in physics, chemistry, biochemistry and various
engineering disciplines. Depending on the background, the
practitioner can choose one or more of the following books
to either learn or refresh their basic knowledge of thermodynamics. Here are some works we ﬁnd particularly helpful:

• Atkins and De Paula’s “Physical Chemistry” [18], chapters 1 to 4.
• McQuarrie and Simon’s extensive work, “Physical Chemistry: A Molecular Approach” [19]

• Dill’s “Molecular Driving Forces” [15]
• Kittel and Kroemer’s “Thermal Physics” [20]
• Shell [14]: Chapters 1-15.

3.3

Classical statistical mechanics

3.3.1

Key concepts

Key concepts from statistical mechanics are particularly important and prevalent in molecular simulations:
• Fluctuations
• Deﬁnitions of various ensembles
• Time averages and ensemble averages
• Equilibrium versus non-equilibrium
Traditional discussions of classical statistical mechanics,
especially concise ones, tend to focus ﬁrst or primarily on
macroscopic thermodynamics and microscopic equilibrium
behavior based on the Boltzmann factor, which tells us
that conﬁgurations rN occur with (relative) probability
exp[–U(rN )/(kB T)], based on potential energy function U and
temperature T in absolute units. Dynamical phenomena
and their connection to equilibrium tend to be treated later
in discussion, if at all. However, as the laws of statistical
mechanics arise naturally from dynamical equations, we will
discuss dynamics ﬁrst.
(b)

U‡
A
UA

B
UB

x, configuration [a.u.]

U, potential energy [a.u.]

U, potential energy [a.u.]

(a)

x, configuration [a.u.]

Figure 1. Energy landscapes. (a) A highly simpliﬁed landscape used
to illustrate rate concepts and (b) a schematic of a more complex
landscape with numerous minima and ambiguous state boundaries.

The key dynamical concept to understand is embodied in
the twin characteristics of timescales and rates. The two are
literally reciprocals of one another. In Fig. 1(a), assume you
have started an MD simulation in basin A. The trajectory is
likely to remain in that basin for a period of time – the “dwell”
timescale – which increases exponentially with the barrier
height, (U‡ – UA ). Barriers many times the thermal energy kB T
imply long dwell timescales, approximated as the reciprocal
of exp[(U‡ – UA )/(kB T)]. The rate coeﬃcient kAB relates to the
transition probability per unit time per amount of reactant(s).
All transitions occur in a random, stochastic fashion and are
predictable only in terms of average behavior. More detailed

discussions of rates and rate coeﬃcients can be found in
numerous textbooks (e.g., [15, 21]).
Once you have understood that MD behavior reﬂects system timescales, you must set this behavior in the context
of an extremely complex energy landscape consisting of almost innumerable minima and barriers, as schematized in
Fig. 1(b). Each small basin represents something like a different rotameric state of a protein side chain or perhaps a
tiny part of the Ramachandran spaces (backbone phi-psi angles) for one or a few residues. Observing the large-scale
motion of a protein then would require an MD simulation
longer than the sum of all the timescales for the necessary
hops, bearing in mind that numerous stochastic reversals are
likely during the simulation. Because functional biomolecular timescales tend to be on µs - ms scales and beyond, it is
challenging if not impossible to observe them in traditional
MD simulations. There are numerous enhanced sampling
approaches [22, 23] but these are beyond the scope of this
discussion and they have their own challenges which often
are much harder to diagnose (see [24] and https://github.
com/dmzuckerman/Sampling-Uncertainty).
What is the connection between MD simulation and equilibrium? The most precise statement we can make is that an
MD trajectory is a single sample of a process that is relaxing
to equilibrium from the starting conﬁguration [21, 25]. If the
trajectory is long enough, it should sample the equilibrium
distribution – where each conﬁguration occurs with frequency
proportional to its Boltzmann factor. In such a long trajectory (only), a time average thus will give the same result as a
Boltzmann-factor-weighted, or ensemble, average. We refer
to such a system, where the time and ensemble averages
are equivialent, as “ergodic.” Note that the Boltzmann-factor
distribution implies that every conﬁguration has some probability, and so it is unlikely that a single conformation or even a
single basin dominates an ensemble. Beware that in a typical
MD trajectory it is likely that only a small subset of basins will
be sampled well – those most quickly accessible to the initial
conﬁguration. It is sometimes suggested that multiple MD
trajectories starting structures can aid sampling, but unless
the equilibrium distribution is known in advance, the bias
from the set of starting structures is simply unknown and
harder to diagnose.
A fundamental equilibrium concept that can only be
sketched here is the representation of systems of enormous
complexity (many thousands, even millions of atoms) in
terms of just a small number of coordinates or states. The
conformational free energy of a state, e.g., FA or FB is a
way of expressing the average or summed behavior of all
the Boltzmann factors contained in a state: the deﬁnition
requires that the probability (or population) peq of a state in
equilibrium be proportional to the Boltzmann factor of its

eq

conformational free energy: pA ∼ exp(–FA /kB T). Because
equilibrium behavior is caused by dynamics, there is a
fundamental connection between rates and equilibrium,
eq
eq
namely that pA kAB = pB kBA , which is a consequence of
“detailed balance”. There is a closely related connection for
on- and off-rates with the binding equilibrium constant.
For a continuous coordinate (e.g., the distance between
two residues in a protein), the probability-determining free
energy is called the “potential of mean force” (PMF); the
Boltzmann factor of a PMF gives the relative probability of a
given coordinate. Any kind of free energy implicitly includes
entropic effects; in terms of an energy landscape (Fig. 1),
the entropy describes the width of a basin or the number
of arrangements a system can have within a particular
state. One way to think of this it is that entropy of a state
relates to the volume of 6N-dimensional phase space that
the state occupies, which in the one-dimensional case is
just the width. These points are discussed in textbooks,
as are the differences between free energies for different
thermodynamic ensembles – e.g., A, the Helmholtz free
energy, when T is constant, and G, the Gibbs free energy,
when both T and pressure are constant – which are not
essential to our introduction [15, 21].1
A ﬁnal essential topic is the difference between equilibrium and non-equilibrium systems. We noted above that an
MD trajectory is not likely to represent the equilibrium ensemble because the trajectory is probably too short. However, in
a living cell where there is no shortage of time, biomolecules
may exhibit non-equilibrium behavior for a quite different
reason – because they are driven by the continual addition
and removal of (possibly energy-carrying) substrate and product molecules. In this type of non-equilibrium situation, the
distribution of conﬁgurations will not follow a Boltzmann distribution. Specialized simulation approaches are available
to study such systems [23, 26] but they are not beginnerfriendly. Non-equilibrium molecular concepts pertinent to
cell biology have been discussed at an introductory level
(e.g. http://www.physicallensonthecell.org/). Notably, many
experiments are conducted at non-equilibrium conditions;
for example, membrane diffusion coeﬃcients are commonly
measured by setting up a concentration gradient across the
membrane and measuring the ﬂux. It can be tempting to the
beginner to setup an MD simulation in the same manner as
such an experiment. However, maintaining non-equilibrium
conditions is typically more complicated in an MD simulation than in an experiment as large reservoirs are commonly
required. Frequently, equilibrium methods can provide the
same or similar information as a non-equilibrium experiment;
users should seek to obtain familiarity with such methods

Occasionally F is used to refer to either appropriate free energy, A or G, but
this is not standard.

before choosing to conduct a non-equilibrium MD simulation.

3.3.2

Books

Books which we recommend as particularly helpful in this
area include:
• Reif’s “Fundamentals of Statistical and Thermal
Physics” [27]
• McQuarrie’s “Statistical Mechanics” [28]
• Dill and Bromberg’s “Molecular Driving Forces” [15]
• Hill’s “Statistical Mechanics: Principles and Selected Applications” [29]
• Shell’s “Thermodynamics and Statistical Mechanics” [14]
• Zuckerman’s “Statistical Physics of Biomolecules” [21]
• Chandler’s “Introduction to Modern Statistical Mechanics” [30]

3.3.3

Online resources

Several online resources have been particularly helpful to
people learning this area, including:
• David Kofke’s notes: http://www.eng.buffalo.edu/
~kofke/ce530/Lectures/lectures.html
• Scott Shell’s notes: https://engineering.ucsb.edu/~shell/
che210d/assignments.html

3.4

Classical electrostatics

3.4.1

Key concepts

Key concepts from classical electrostatics include
• The Coulomb interaction and its long-range nature
• Polarizability, dielectric constants, and electrostatic
screening
• When and why we need lattice-sum electrostatics and
similar approaches
Electrostatic interactions are both some of the longestrange interactions in molecular systems and the strongest,
with the interaction (often called “Coulombic” after Coulomb’s
law) between charged particles falling off as 1/r where r is the
distance separating the particles. Atom-atom interactions are
thus necessarily long range compared to other interactions
in these systems (which fall off as 1/r 3 or faster). This means
atoms or molecules separated by considerable distances can
still have quite strong electrostatic interactions, though this
also depends on the degree of shielding of the intervening
medium (or its relative permittivity or dielectric constant).
The static dielectric constant of a medium, or relative permittivity r (relative to that of vacuum), affects the prefactor
for the decay of these long range interactions, with interactions reduced by 1r . Water has a high relative permittivity or
dielectric constant close to 80, whereas non-polar compounds
such as n-hexane may have relative permittivities near 2 or

even lower. This means that interactions in non-polar media
such as non-polar solvents, or potentially even within the relatively non-polar core of a larger molecule such as a protein,
are effectively much longer-range even than those in water.
The dielectric constant of a medium also relates to the degree of its electrostatic response to the presence of a charge;
larger dielectric constants correspond to larger responses to
the presence of a nearby charge.
It turns out that atoms and molecules also have their
own levels of electrostatic response; particularly, their electron distributions polarize in response to their environment,
effectively giving them an internal dielectric constant. This
polarization can be modeled in a variety of ways, such as
(in ﬁxed charge force ﬁelds) building in a ﬁxed amount of
polarization which is thought to be appropriate for simulations in a generic “condensed phase” or by explicitly including
polarizability via QM or by building it into a simpler, classical model which includes polarizability such as via explicit
atomic polarizabilities [31, 32] or via Drude oscillator-type
approaches [33], where inclusion of extra particles attached
to atoms allows for a type of effective polarization.
Because so many interactions in physical systems involve
polarity, and thus signiﬁcant long-range interactions that decay only slowly with distance, it is important to regard electrostatic interactions as fundamentally long-range interactions.
Indeed, contributions to the total energy of a system from
distant objects may be even more important in some cases
than those from nearby objects. Speciﬁcally, since interactions between charges fall off as 1/r, but the volume of space
at a given separation distance increases as r 3 , distant interactions can contribute a great deal to the energies and forces
in molecular systems. In practice, this means that severe
errors often result from neglecting electrostatic interactions
beyond some cutoff distance [7, 34–37]. Thus, we prefer to
include all electrostatic interactions, even out to very long
ranges. Once this is decided, it leaves simulators with two
main options, only one of which is really viable. First, we can
simulate the actual ﬁnite (but large) system which is being
studied in the lab, including its boundaries. But this is impractical, since macroscopic systems usually include far too
many atoms (on the order of at least a mole or more). The
remaining option, then, is to apply periodic boundary conditions (see Section 4.2) to tile all of space with repeating copies
of the system. Once periodic boundary conditions are set
up, deﬁning a periodic lattice, it becomes possible to include
all long-range electrostatic interactions via a variety of different types of sums which can be described as “lattice sum
electrostatics” or Ewald-type electrostatics [37, 38] where the
periodicity is used to make possible an evaluation of all long
range electrostatic interactions, including those of particles
with their own periodic images.

In practice, lattice sum electrostatics introduce far fewer
and less severe artifacts than do cutoff schemes, so these
are used for most classical all-atom simulation algorithms at
present. A variety of different eﬃcient lattice-sum schemes
are available [38]. In general these should be used whenever
long range electrostatic interactions are expected to be signiﬁcant; they may not be necessary in especially nonpolar
systems and/or with extremely high dielectric constant solvents where electrostatic interactions are exclusively short
range, but in general they should be regarded as standard
(see also Section 4.7, below).

3.4.2

Books

On classical electrostatics, we have found the undergraduatelevel work by David J. Griﬃths, “Introduction to Electrodynamics” [39], to be quite helpful. The graduate-level work of
Jackson, “Classical Electrodynamics” [40], is also considered a
classic/standard work, but may prove challenging for those
without a background relatively heavy in mathematics.

3.5

Molecular interactions

3.5.1

Key concepts

Molecular simulations are, to a large extent, about molecular
interactions, so these are particularly key, including:
• Bonded and nonbonded interactions
• The different types of nonbonded interactions and why
they are separated in classical descriptions
• The dividing line between bonded and nonbonded interactions
Key interactions between atoms and within or between
molecules are typically thought of as consisting of two main
types – bonded and non-bonded interactions. While these
arise from similar or related physical effects (ultimately all
tracing back to QM and the basic laws of physics) they are
typically treated in rather distinct manners in molecular simulations so it is important to consider the two categories
separately.
Bonded interactions are those between atoms which are
connected, or nearly so, and relating to the bonds connecting
these atoms. In typical molecular simulations these consist
of bond stretching terms, angle bending terms, and terms
describing the rotation of torsional angles, as shown in Figure
2. Torsions typically involve four atoms and are often of two
types – “proper” torsions, around bonds connecting groups
of atoms, and “improper” torsions which involve neighbors of
a central atom; these are often used to ensure the appropriate degree of planarity or non-planarity around a particular
group (such as planarity of an aromatic ring). It is important
to note that the presence of bonded interactions between

(a)

(b)

energy function or force ﬁeld family. For example, the AMBER
family force ﬁelds usually reduce 1-4 electrostatics to 1.2
of
their original value, and 1-4 Lennard-Jones interactions to 12
of their original value. 1-4 interactions are essentially considered the borderline between the bonded and non-bonded
regions. These short-range interactions can be quite strong
and there is potentially a risk of them overwhelming longerrange interactions, hence their typical reduction.

Figure 2. Standard MM force ﬁelds include terms that represent (a)
bond and angle stretching around equilibrium values, using harmonic
potentials with spring constants ﬁt to the molecules and atoms to
which they are applied; and (b) rotation around dihedral angles (green
arrow) deﬁned using four atoms, typically using a cosine expansion.

atoms does not preclude their also having non-bonded interactions with one another (see discussion of exclusions and
1-4 interactions, below).
Nonbonded interactions between atoms are all interactions which are included in the potential energy of the system
aside from bonded interactions. Commonly these include
at least point-charge Coulomb electrostatic interactions and
“non-polar” interactions modeled by the Lennard-Jones potential or another similar potential which describes short range
repulsion and weak long-range interaction even between nonpolar atoms. Additional terms may also be included, such as
interactions between ﬁxed multipoles, interactions between
polarizable sites, or occasionally explicit potentials for hydrogen bonding or other specialized terms. These are particularly common in polarizable force ﬁelds such as the AMOEBA
model.
Often, the energy functions used by molecular simulations
explicitly neglect nonbonded interactions between atoms
which are immediately bonded to one another, and atoms
which are separated by only one intervening atom, partly to
make it easier to ensure that these atoms have preferred geometries dictated by their deﬁned equilibrium lengths/angles
regardless of the nonbonded interactions which would otherwise be present. This neglect of especially short range
nonbonded interactions between near neighbors is called
“exclusion”, and energy functions typically specify which interactions are excluded.
The transition to torsions, especially proper torsions, is
where exclusions typically end. However, many all-atom energy functions commonly used in biomolecular simulations
retain only partial nonbonded interactions between terminal
atoms involved in a torsion. The atoms involved in a torsion, if numbered beginning with 1, would be 1, 2, 3, and 4,
so the terminal atoms could be called atoms 1 and 4, and
nonbonded interactions between such atoms are called “1-4
interactions”. These interactions are often present but reduced, though the exact amount of reduction differs by the

3.5.2

Books

For a discussion of molecular interactions, we recommend
“Intermolecular and surface forces” by Jacob N. Israelachvili.
A variety of other books discuss these from a simulation
perspective, e.g. Leach [7] and Allen and Tildesley [12].

Basic simulation concepts and
terminology

Above, we covered a variety of fundamental concepts needed
for understanding molecular simulations and the types of
interactions and forces we seek to model; here, we shift our
attention to understanding basics of how molecular simulations actually work.

4.1

Force ﬁelds

The term “force ﬁeld” simply refers to the included terms,
particular form, and speciﬁc implementation details, including
parameter values, of the chosen potential energy function.2
Most of the terms included in potential energy functions
have already been detailed in Section 3.5, with the most
common being Coulombic, Lennard-Jones, bond, angle, and
torsional (dihedral) terms (Figure 2). Here, we very brieﬂy
describe the mathematical forms used to represent such interactions.
Non-bonded interactions of the Lennard-Jones form are
well-described throughout the literature (for instance see Ch.
4 of Leach [7]); these model a short-range repulsion that
scales as 1/r 12 and a long-range attraction that scales as 1/r 6 .
Coulombic interactions, including both short and long-range
components, are described in detail elsewhere in this document. To represent bonded interactions, harmonic potentials
are often employed. The same is true for angles between
It is worth noting there is a occasionally a bit of ambiguity when the term
“force ﬁeld” is used. In some cases it is used to refer to a library of parameters
that could be applied to assign an energy function to a speciﬁc molecular
system via a parameterization process after applying some speciﬁc chemical
perception like atom typing to that system [41]. For example, one might speak
of the AMBER ff15FB [42] protein force ﬁeld, which essentially provides a recipe
for assigning parameters to a protein once atom types are assigned. In other
cases, “force ﬁeld” is used to refer to the speciﬁcs of the potential energy
function after application to a speciﬁc system — what could also be called a
“parameterized system”. For our purposes here, the distinction between a force
ﬁeld library and a parameterized system is not particularly important, but it is
worth noting the potential ambiguity.

three bonded atoms, but the harmonic potential is applied
with respect to the angle formed and not the distance between atoms. Torsional terms are also commonly employed,
usually consisting as sums of cosines, i.e. a cosine expansion.
While the above are perhaps the most common potentials used, there are a variety of common variations as well.
More exotic potentials based on three-body intermolecular
orientations, or terms directly coupling bond lengths and
bending angles are also possible. Some historic force ﬁelds
also added an explicit (non-Coulombic) hydrogen bonding
term, though these are less frequently used in many cases
today. Additionally, other choices of potential function are of
course acceptable, including Buckingham or Morse potentials,
or the use of “improper” dihedral terms to enforce planarity
of cyclic portions of molecules. This may even include empirical corrections based on discrete binning along a particular
set of degrees of freedom [43, 44], as well as applied external ﬁelds (i.e. electric ﬁelds) and force ﬁeld terms describing
the effect of degrees of freedom, such as solvent, that have
been removed from the system via “coarse-graining.” [45]
For a more in-depth discussion of common (as well as less
common) force ﬁeld terms, see Ch. 4 of Leach [7], or for an
in-depth review of those speciﬁc to simulating biomolecules,
see Ponder and Case [31].
Functional forms used to describe speciﬁc terms in a potential energy function may be vastly different in mathematical character even though they seek to describe the same
physics. For instance, the Lennard-Jones potential implements an r –12 term to represent repulsions, while an exponential form is used in the Buckingham potential. This results in very different mathematical behavior at very short
distances and as a result differences in numerical implementation as well as evaluation eﬃciencies via a computer. For
this reason, one functional form may be preferred above another due to enhanced numerical stability or simplicity of
implementation, even though it is not as faithful to the underlying physics. In this regard, force ﬁeld selection is a form of
selecting a model – one should carefully weigh the virtues of
accuracy and convenience or speed, and be ever-conscious
of the limitations introduced by this decision (for instance,
see Becker et al. [46]). It is also important to know that most
MD simulation engines only support a subset of functional
forms. For those forms that are supported, the user manuals
of these software packages are often excellent resources for
learning more about the rationale and limitations of different
potential energy functions and terms (e.g. see Part II of Amber reference manuals[47] and Ch. 4 of the reference manual
for GROMACS [48]).
For practical purposes, most beginning users will not be
ﬁtting a force ﬁeld or choosing a functional form, but will
instead be using an existing force ﬁeld that already relies on a

particular functional form and is available in their simulation
package of choice, so for such users it is more important
to know how the functional form represents the different
interactions involved than to necessarily be able to justify
why that particular functional form was chosen.
Many examples of force ﬁelds abound in the literature —
in fact, too many to provide even a representative sample
or list of citations, as most force ﬁelds are speciﬁcally developed for particular systems or categories of systems under
study. However, reviews are available describing and comparing force ﬁelds for biomolecular simulations [31, 49], solid,
covalently-bonded materials [50], polarizable potentials [51],
and models of water [52, 53], to name just a few. Many force
ﬁelds are open-source and parameter ﬁle libraries may be
found through the citations in the resources above or are often distributed with molecular simulation packages. Limited
databases of force ﬁelds also exist, most notably for simulations of solid materials where interatomic potentials display
a much wider array of mathematical forms [54, 55].
Speciﬁcation of a force ﬁeld involves not just a choice of
functional form, but the details of the speciﬁc parameters
for all of the interacting particles which will be considered
— that is, the speciﬁc parameters governing the interactions
as speciﬁed by the functional form. Parameters are usually
speciﬁc to certain types of atoms, bonds, molecules, etc., and
include point charges on atoms if electrostatic terms are in
use.
Some choices which are often considered auxiliary actually
comprise part of the choice of the force ﬁeld or interaction
model. Speciﬁcally, settings such as the use of constraints,
the treatment of cut-offs and other simulation settings affect
the ﬁnal energies and forces which are applied to the system. Thus, to replicate a particular force ﬁeld as described
previously, such settings should be matched to prior work
such as the work which parameterized the force ﬁeld. The
choice of how to apply a cutoff, such as through direct truncation, shifting of the potential energy function, or through the
use of switching functions, should be maintained if identical
matches to prior work computing the properties of interest
are desired. This is especially important for the purposes of
free energy calculations, where the potential energy itself is
recorded. However, force ﬁelds are in some cases slow to
adapt to changes in protocol, so current best practices seem
to suggest that lattice-sum electrostatics should be used for
Coulomb electrostatics in condensed phase systems, even if
the chosen force ﬁeld was ﬁtted with cutoff electrostatics, and
in many cases long-range dispersion corrections should be
applied to the energy and pressure to account for truncated
Lennard-Jones interactions [56, 57].
For almost all force ﬁelds, many versions, variants, and
modiﬁcations exist, so if you are using a literature force ﬁeld

or one distributed with your simulation package of choice, it
is important to pay particular attention (and make note of)
exactly what version you are using and how you obtained it
so you will be able to accurately detail this in any subsequent
publications.
As clearly described in Becker et al. [46], it is of paramount
importance to understand the capabilities and limitations of
various force ﬁeld models that may seem appropriate for
one’s work. Depending on the physics being simulated and
the computational resources at hand, no force ﬁeld in the
literature may provide results that accurately reproduce experiment. But with so many force ﬁelds to pick from, how is
this possible? The issue lies in what is termed “transferability.” Simply put, a classical description of dynamics, as implemented in MD, cannot universally describe all of chemistry
and physics. At some level of ﬁner detail, all of the potential
functions described above are simply approximations. Due to
this, force ﬁeld developers must often make the diﬃcult decision of sacriﬁcing accuracy or generality. For instance, a force
ﬁeld may have been developed to very accurately describe a
single state point, in which case it is obvious that extensive
testing should be performed to ensure that it is also applicable at other conditions. Even with force ﬁelds developed
to be general and transferable, it is essential to ensure that
the desired level of realism is achieved, especially if applying
such a model to a new system (even more caution is advised
when mixing force ﬁelds!). Either way, it is always a good idea
to check results against previous literature when possible.
This helps ensure that the force ﬁeld is being implemented
properly and, though it may seem laborious on a short-time
horizon, can pay substantial dividends in the long-run.
Because this balance of accuracy versus generality and
transferability can be challenging, some efforts eschew transferability entirely and instead build “bespoke” force ﬁelds,
where each molecule is considered as a unique entity and
assigned parameters independently of any other molecule or
representation of chemical space (e.g. [58]). Such approaches
offer the opportunity to assign all molecules with parameters
assigned in a consistent way; however, they are unsuitable
for applications where speed needs to exceed that of the parameter assignment process – so, for example, for docking of
a large library of potential ligands to a target receptor, if compounds must be screened at seconds or less per molecule,
such approaches may not be suitable.

4.2

Periodic boundary conditions

Periodic boundary conditions allow more accurate estimation of bulk properties from simulations of ﬁnite, essentially
nanoscale systems. More precisely, simulations of comparatively small systems with periodic boundary conditions can be
a good approximation to the behavior of a small subsystem in

simulated
system

periodic box
size

Figure 3. Periodic boundary conditions are shown for a simple 2D
system. Note that the simulated system is a sub-ensemble within an
inﬁnite system of identical, small ensembles.

a larger bulk phase (or at least are a much better approximation than simply simulating a nanodroplet or a ﬁnite system
surrounded by vacuum). Periodic boundary conditions can
alleviate many of the issues with ﬁnite size effects because
each particle interacts with periodic images of particles in
the same system. Clearly, though, it is undesirable for a single particle to interact with the same particle multiple times.
To prevent this, a cut-off of many non-bonded interactions
should be chosen that is less than half the length of the simulation box in any dimension. (However, as noted in Section 3.4
these cut-offs are not normally applied to electrostatic interactions because truncating these interactions induces worse
artifacts than does including interactions with multiple copies
of the same particle. Instead, what are often termed “cutoffs” that are applied to electrostatics are instead a shift from
short-range to long-range treatments.) Such cut-offs impose
a natural lower limit to the size of a periodic simulation box,
as the box must be large enough to capture all of the most
signiﬁcant non-bonded interactions. Further information on
periodic boundary conditions and discussion of appropriate
cut-offs may be found in Leach [7], sections 6.5 and 6.7 and
Shell [59]’s lecture on Simulations of Bulk Phases.
It is very important to note that periodic boundary conditions are simply an approximation to bulk behavior. They
DO NOT effectively simulate an inﬁnitely sized simulation box,
though they do reduce many otherwise egregious ﬁnite-size
effects. This is most easily seen by imagining the placement

of a solute in a periodic simulation box. The solute will be
replicated in all of the surrounding periodic images. The concentration of solute is thus exactly one per the volume of the
box. Although proper selection of non-bonded cutoffs will
guarantee that these solutes do not directly interact (hence
the common claim that such systems are at inﬁnite dilution),
they may indirectly interact through their perturbation of
nearby solvent. If the solvent does not reach a bulk-like state
between solutes, the simulation will still suffer from obvious
ﬁnite-size effects.
Macroscopic, lab-scale systems, or bulk systems, typically
consist of multiple moles of atoms/molecules and thus from
a simulation perspective are effectively inﬁnite systems. We
attempt to simulate these by simulating ﬁnite and fairly small
systems, and, in a sense, the very idea that the simulation
cell is not inﬁnite, but simply periodic, immediately gives rise
to ﬁnite-size effects. Thus, our typical goal is not to remove
these completely but to reduce these to levels that do not
adversely impact the results of our simulations. Finite-size
effects are particularly apparent in the electrostatic components of simulations, as these forces are inherently longer
ranged than dispersion forces, as discussed in Section 3.4.
One should always check that unexpected long-range correlations (i.e. on the length-scale of the simulation box) do not
exist in molecular structure, spatial position, or orientation.
It should also be recognized that periodic boundary conditions innately change the deﬁnition of the system and the
properties calculated from it. Many derivations, especially
those involving transport properties, such as diffusivity [60],
assume inﬁnite and not periodic boundary conditions. The
resulting differences in seemingly well-known expressions for
computing properties of interest are often subtle, yet may
have a large impact on results. Such considerations should
be kept in mind when comparing results between simulations
and with experiment.

4.3

Main steps of a molecular dynamics
simulation

While every system studied will present unique challenges
and considerations, the process of performing a molecular
dynamics simulation generally follows these steps:
1. System preparation
2. Minimization/Relaxation
3. Equilibration
4. Production
Additional explanations of these steps along with procedural details speciﬁc to a given simulation package and
application may be found in a variety of tutorials [61, 62]. It
should be noted that these steps may be diﬃcult to unambiguously differentiate and deﬁne in some cases. Additionally,

it is assumed that prior to performing any of these steps,
an appropriate amount of deliberation has been devoted to
clearly deﬁning the system and determining the appropriate
simulation techniques.

4.3.1

System preparation

System preparation focuses on preparing the starting state
of the desired system for input to an appropriate simulation
package, including building a starting structure, solvating (if
necessary), applying a force ﬁeld, etc. Because this step differs so much depending on the composition of the system
and what information is available about the starting structure,
it is a step which varies a great deal depending on the nature
of the system at hand and as a result may require unique
tools.
Given the variable nature of system preparation, it is highly
recommended that best practices documents speciﬁc to this
issue and to the type of system of interest be consulted. If
such documents do not exist, considerable care should be
exercised to determine best practices from the literature.
Loosely speaking, system preparation can be thought of
as consisting of two logical components which are not necessarily consecutive or separate. One comprises building the
conﬁguration of the system in the desired chemical state and
the other applying force ﬁeld parameters.
For building systems, freely available tools for constructing
systems are available and can be a reasonable option (though
their mention here should not be taken as an endorsement
that they necessarily encapsulate best practices). Examples
include tools for constructing speciﬁc crystal structures, proteins, and lipid membranes, such as Moltemplate [63], Packmol [64], and Atomsk [65].
A key consideration when building a system is that the
starting structure ideally ought to resemble the equilibrium
structure of the system at the thermodynamic state point
of interest. For instance, highly energetically unfavorable
conﬁgurations of the system, such as blatant atomic overlaps,
should be avoided. In some sense, having a good starting
structure is only a convenience to reduce equilibration times
(if the force ﬁeld is adequate); however, for some systems,
equilibration times might otherwise be prohibitively long.
System preparation is arguably the most critical stage of a
simulation and in many cases receives the least attention; if
your system preparation is ﬂawed, such ﬂaws may prove fatal. Potentially the worst possible outcome is if the prepared
system is not what you intended (e.g. it contains incorrect
molecules or protonation states) but is chemically valid and
well described by your force ﬁeld and thus proceeds without error through the remaining steps — and in fact this is
a frequent outcome of problems in system preparation. It
should not be assumed that a system has been prepared cor-

rectly if it is well-behaved in subsequent equilibration steps;
considerable care should be taken here.
Assignment or development of force ﬁeld parameters is
also critical, but is outside the scope of this work. For our
purposes, we will assume you have already obtained or developed force ﬁeld parameters suitable for your system of
interest.

rigid molecules are present, care must be taken to prevent
components of velocities assigned along constraints from
being forced to zero [66]. With a thermostat present, this only
delays system equilibration, but for NVE simulations, such as
might be used in hybrid MC/MD simulations, it can result in
violations of equipartition and large subsequent errors [67].

4.3.4
4.3.2

Minimization

The purpose of minimization, or relaxation, is to ﬁnd a local
energy minimum of the starting structure so that the molecular dynamics simulation does not immediately “blow up” (i.e.
the forces on any one atom are not so large that the atoms
move an unreasonable distance in a single timestep). This
involves standard minimization algorithms such as steepest
descent. For a more involved discussion of minimization algorithms utilized in molecular simulation, see Leach [7], sections
5.1-5.7.

4.3.3

Assignment of velocities

Minimization ideally takes us to a state from which we can
begin numerical integration of the equations of motion without overly large displacements (see Leach [7], section 7.3.4);
however, to begin a simulation, we need not just positions but
also velocities. Minimization, however, provides only a ﬁnal
set of positions. Thus, starting velocities must be assigned;
usually this is done by assigning random initial velocities to
atoms in a way such that the correct Maxwell-Boltzmann distribution at the desired temperature is achieved as a starting
point. The actual assignment process is typically unimportant, as the Maxwell-Boltzmann distribution will quickly arise
naturally from the equations of motion. Since the momentum of the center-of-mass of the simulation box is conserved
by Newtonian dynamics, this quantity is typically set to zero
by removing the center-of-mass velocity from all particles after random assignment, preventing the simulation box from
drifting.
In some cases, we seek to obtain multiple separate and
independent simulations of different instances or realizations
of a particular system to assess error, collect better statistics,
or help gauge dependence of results on the starting structure.
It is worth noting that even very small differences in initial
conﬁguration, such as small changes in the coordinates of a
single atom, lead to exponential divergence of the time evolution of the system [12], meaning that simply running different
simulations starting with different initial velocities will lead to
dramatically different time evolution over long enough times.
An even better way to generate independent realizations is
to begin with different starting conﬁgurations, such as different conformations of the molecule(s) being simulated, as
this leads to behavior which is immediately different. When

Equilibration

Ultimately, we usually seek to run a simulation in a particular
thermodynamic ensemble (e.g. the NVE or NVT ensemble)
at a particular state point (e.g. target energy, temperature,
and pressure) and collect data for analysis which is appropriate for those conditions and not biased depending on our
starting conditions/conﬁguration. This means that usually
we need to invest simulation time in bringing the system to
the appropriate state point as well as relaxing away from any
artiﬁcially induced metastable starting states. In other words,
we are usually interested in sampling the most relevant (or
most probable) conﬁgurations in the equilibrium ensemble of
interest. However, if we start in a less-stable conﬁguration a
large part of our equilibration may be the relaxation time (this
may be very long for biomolecules or systems at phase equilibrium) necessary to reach the more relevant conﬁguration
space.
The most straightforward portion of equilibrium is bringing the system to the target state point. Usually, even though
velocities are assigned according to the correct distribution,
a thermostat will still need to add or remove heat from the
system as it approaches the correct partitioning of kinetic
and potential energies. For this reason, it is advised that
a thermostatted simulation is performed prior to a desired
production simulation, even if the production simulation will
ultimately be done in the NVE ensemble. This phase of equilibration can be monitored by assessing the temperature and
pressure of the system, as well as the kinetic and potential
energy, to ensure these reach a steady state on average. For
example, an NPT simulation is said to have equilibrated to a
speciﬁc volume when the dimensions of the simulation box
ﬂuctuate around constant values with minimal drift. This definition, though not perfectly rigorous, is usually suitable for
assessing the equilibration of energies, temperature, pressure, and box dimensions during equilibration simulations.
A more diﬃcult portion of equilibration is to ensure that
other properties of the system which are likely to be important are also no longer changing systematically with simulation time. At equilibrium, a system may still undergo slow
ﬂuctuations with time, especially if it has slow internal degrees of freedom – but key properties should no longer show
systematic trends away from their starting structure. Thus,
for example, for biomolecular simulations it is common to
examine the root mean squared deviation (RMSD) of the

molecules involved as a function of time, and potentially other
properties like the number of hydrogen bonds between the
biomolecules present and water, as these may be slower to
equilibrate than system-wide properties like the temperature
and pressure.

erally an appropriate equilibration work-ﬂow for common
production ensembles. Clearly, this schematic cannot cover
every case of interest, but should provide some idea of the
general approach. For more information on equilibration procedures, see Leach [7], section 7.4 and Shell [59], lectures on
Molecular dynamics and Computing properties.

4.3.5

Figure 4. Shown are graphs of a hypothetical computed property
(vertical axis) versus simulation time (horizontal axis). For some
system properties, equilibration may be relatively rapid (top panel),
while for others it may be much slower (bottom panel). If it there is
ambiguity as to whether or not a key property is still systematically
changing, as in the bottom panel, equilibration should be extended.

Once the kinetic and potential energies ﬂuctuate around
constant values and other key properties are no longer changing with time, the equilibration period has reached its end.
In general, if any observed properties still exhibit a systematic trend with respect to simulation time (e.g. Figure 4) this
should be taken as a sign that equilibration is not yet complete.
Depending on the target ensemble for production, the
procedure for the end of equilibration is somewhat different. If an NVE simulation is desired, the thermostat may be
removed and a snapshot selected that is simultaneously as
close to the average kinetic and potential energies as possible.
This snapshot, containing both positions and velocities may
be used to then start an NVE simulation that will correspond
to a temperature close to that which is desired. This is necessary due to the fact that only the average temperature is
obtained through coupling to a thermostat (see Section 4.4),
and the temperature ﬂuctuates with the kinetic energy at
each timestep.
If the target is a simulation in the NVT ensemble at a
particular density, equilibration should be done in the NPT
ensemble. In this case, the system may be scaled to the desired average volume before starting a production simulation
(and if rescaling is done, additional equilibration might be
needed).
The schematic below (Figure 5) demonstrates what is gen-

Production

Once equilibration is complete, we may begin collecting data
for analysis. Typically this phase is called “production”. The
main difference between equilibration and production is simply that in the production simulation, we plan to retain and
analyze the collected data. Production must always be preceded by equilibration appropriate for the target production
ensemble, and production data should never be collected immediately after a change in conditions (such as rescaling a box
size, energy minimizing, or suddenly changing the temperature or pressure) except in very speciﬁc applications where
this is the goal.
For bookkeeping purposes, sometimes practitioners
choose to discard some initial production data as additional
equilibration; usually this is simply to allow additional
equilibration time after a change in protocol (such as a
switch from NPT to NVT), and the usual considerations for
equilibration apply in such cases (see Shell [59], lecture on
Computing Properties).
Analysis of production is largely outside the scope of this
work, but requires considerable care in computing observables and assessing the uncertainty in any computed properties. Usually, analysis involves computing expectation values
of particular observables, and a key consideration is to obtain
converged estimates of these properties — that is, estimates
that are based on adequate simulation data so that they no
longer depend substantially on the length of the simulation
which was run or on its initial conditions. This is closely related to the above discussion of equilibration. Depending on
the relaxation timescales involved, one may realize only after
analysis of a “production” trajectory that the system was still
equilibrating in some sense.
A separate Best Practices document addresses
the critical issues of convergence and error analysis; we refer the reader there for more details [68]
(https://github.com/dmzuckerman/Sampling-Uncertainty).
For more speciﬁc details on procedures and parameters used
in production simulations, see the appropriate best practices
document for the system of interest.
One other key consideration in production is what data to
store, and how often. Storing data especially frequently can
be tempting, but utilizes a great deal of storage space and
does not actually provide signiﬁcant value in most situations.
Particularly, observations made in MD simulations are cor-

Suggested equilibration workflow
NVT

Production Ensemble
NVE

(short simulation to
relax to temperature
of interest)

NVE

(short equilibration)

NVT

NVT

(at known, fixed
density)

(short simulation to
relax to temperature
of interest)

NVT

(short simulation to
relax to temperature
of interest)

NVT

(short simulation to
relax to temperature
of interest)

NPT

(short simulation to
relax to density of
interest)

NPT

NVT

(to calculate average
box size)

NVT

(short equilibration)

(for density defined by pressure or
unknown system density distribution,
like a homegeneous system)

NPT

NPT

(short simulation to
relax to density of
interest)

Figure 5. Common equilibration work-ﬂows are shown; these vary depending on the target ensemble for production simulations (right).
Typically, an initial phase of equilibration at constant volume and temperature is needed to bring the system to the desired target temperature
or energy. For stability reasons, this initial phase is usually needed even if the goal is to also bring the system to a target pressure. If the
production ensemble is an NVE ensemble, an initial NVT simulation is usually followed by a short additional NVE equilibration before collection
of production data. If the production ensemble is NVT, protocols may differ depending on whether it is necessary to allow the system to
equilibrate to a particular density/volume or whether the volume is selected a priori (second and third rows). And if production is to be NPT, it is
usually equilibrated ﬁrst at NVT before equilibrating to the target pressure (ﬁnal row).

related in time (e.g. see https://github.com/dmzuckerman/
Sampling-Uncertainty [68]) so storing data more frequently
than the autocorrelation time results in storage of essentially
redundant data. Thus, storing data more frequently than
intervals of the autocorrelation time is generally unnecessary. Of course, the autocorrelation time is not known a priori
which can make it necessary to store some redundant data.
Disk space may also be a limiting factor that dictates the frequency of storing data, and should at least be considered.
Trajectory snapshots can be particularly large. However, if
there are no disk space limitations it may be best to avoid
discarding uncorrelated data so sampling at intervals of the
autocorrelation time may be appropriate.
If disk space proves limiting, various strategies can be used
to reduce storage use, such as storing full-precision trajectory
snapshots only less frequently and storing reduced-precision
ones, or snapshots for only a portion of the system, more
often. However, these choices will depend on the desired
analysis.
For many applications, it will likely be desirable to store

energies and trajectory snapshots at the same time points
in case structural analysis is needed along with analysis of
energies. Since energies typically use far less space, however,
these can be stored more often if desired.

4.4

Thermostats

Here, we discuss why thermostats, which seek to control the
temperature of a simulation, are (often) needed for molecular simulations. We review background information about
thermostats and how they work, introduce some popular
thermostats, and highlight common issues to understand
and avoid when using thermostats in MD simulations.

4.4.1

Thermostats seek to maintain a target
temperature

As mentioned above, molecular dynamics simulations are
used to observe and glean properties of interest from some
system of study. In many cases, to emulate experiments done
in laboratory conditions (exposed to the surroundings), sampling from the canonical (constant temperature) ensemble
is desired [69]. Generally, if the temperature of the system

must be maintained during the simulation, some thermostat
algorithm will be employed.

4.4.2

some of the more popular and historic thermostats used in
MD.

Background and How They Work

The temperature of a molecular dynamics simulation is typically measured using kinetic energies
DPas deﬁned
E using the
N 1
equipartition theorem: 32 NkB T =
m
v
i
i=1 2
i . The angled brackets indicate that the temperature is deﬁned as a
time-averaged quantity. If we use the equipartition theorem
to calculate the temperature for a single snapshot in time
of a molecular dynamics simulation [7, 21] instead of timeaveraging, this quantity is referred to as the instantaneous
temperature. The instantaneous temperature will not always
be equal to the target temperature; in fact, in the canonical
ensemble, the instantaneous temperature should undergo
ﬂuctuations around the target temperature.
Thermostat algorithms work by altering the Newtonian
equations of motion that are inherently microcanonical (constant energy). Thus, it is preferable that a thermostat not be
used if it is desired to calculate dynamical properties such
as diffusion coeﬃcients; instead, the thermostat should be
turned off after equilibrating the system to the desired temperature. However, while all thermostats give non-physical
dynamics, some have been found to have little effect on the
calculation of particular dynamical properties, and they are
commonly used during the production simulation as well [70].
There are several ways to categorize the many thermostatting algorithms that have been developed. For example, thermostats can be either deterministic or stochastic depending
on whether they use random numbers to guide the dynamics,
and they can be either global or local depending on whether
they are coupled to the dynamics of the full system or of a
small subset. Many of the global thermostats can be made
into local “massive” variants by coupling separate thermostats
to each particle in the system rather than having a single thermostat for the whole system. There are also several methods
employed by thermostat algorithms to control the temperature. Some thermostats operate by rescaling velocities outside of the molecular dynamics’ equations of motion, e.g.,
velocity rescaling is conducted after particles’ positions and
momenta have been updated by the integrator. Others include stochastic collisions between the system and an implicit
bath of particles, or they explicitly include additional degrees
of freedom in the equations of motion that have the effect of
an external heat bath.

4.4.3

Popular Thermostats

Within this section, various thermostats will be brieﬂy explored, with a small description of their uses and possible
issues that are associated with each. This is not an exhaustive
study of available thermostats, but is instead a survey of just

1. Gaussian
The goal of the Gaussian thermostat is to ensure
that the instantaneous temperature is exactly equal to
the target temperature. This is accomplished by modifying the force calculation with the form F = Finteraction +
Fconstraint , where Finteraction is the standard interactions
calculated during the simulation and Fconstraint is a Lagrange multiplier that keeps the kinetic energy constant.
The reasoning for the naming of this thermostat is due
to its use of the Gaussian principle of least constraint to
determine the smallest perturbative forces needed to
maintain the instantaneous temperature [69]. Clearly,
this thermostat does not sample the canonical distribution; it instead samples the isokinetic (constant kinetic
energy) ensemble. However, the isokinetic ensemble
samples the same conﬁgurational phase space as the
canonical ensemble, so position-dependent (structural)
equilibrium properties can be obtained equivalently
with either ensemble [71]. However, velocity-dependent
(dynamical) properties will not be equivalent between
the ensembles. This thermostat is used only in certain
advanced applications [71].
2. Simple Velocity Rescaling
The simple velocity rescaling thermostat is one of the
easiest thermostats to implement; however, this thermostat is also one of the most non-physical thermostats.
This thermostat relies on rescaling the momenta of the
particles such that the simulation’s instantaneous temperature exactly matches the target temperature [69].
Similarly to the Gaussian thermosat, simple velocity
rescaling aims to sample the isokinetic ensemble rather
than the canonical ensemble. However, it has been
shown that the simple velocity rescaling fails to properly
sample the isokinetic ensemble except in the limit of
extremely small timesteps [72]. Its usage can lead to
simulation artifacts, so it is not recommended [72, 73].
3. Berendsen
The Berendsen [74] thermostat (also known as the
weak coupling thermostat) is similar to the simple velocity rescaling thermostat, but instead of rescaling velocities completely and abruptly to the target kinetic energy,
it includes a relaxation term to allow the system to more
slowly approach the target. Although the Berendsen
thermostat allows for temperature ﬂuctuations, it samples neither the canonical distribution nor the isokinetic
distribution. Its usage can lead to simulation artifacts,
so it is not recommended [72, 73].
4. Bussi-Donadio-Parrinello
(Canonical
Sampling

through Velocity Rescaling)
The Bussi [75] thermostat is similar to the simple velocity rescaling and Berendsen thermostats, but instead
of rescaling to a single kinetic energy that corresponds
to the target temperature, the rescaling is done to a
kinetic energy that is stochastically chosen from the
kinetic energy distribution dictated by the canonical ensemble. Thus, this thermostat properly samples the
canonical ensemble. Similarly to the Berendsen thermostat, a user-speciﬁed time coupling parameter can be
chosen to vary how abruptly the velocity rescaling takes
place The choice of time coupling constant does not
affect structural properties, and most dynamical properties are fairly independent of the coupling constant
within a broad range [75].
5. Andersen
The Andersen [76] thermostat works by selecting
particles at random and having them “collide” with a
heat bath by giving the particle a new velocity sampled
from the Maxwell-Boltzmann distribution. The number
of particles affected, the time between “collisions”, and
how often it is applied to the system are possible variations of this thermostat. The Andersen thermostat
does reproduce the canonical ensemble. However, it
should only be used to sample structural properties,
as dynamical properties can be greatly affected by the
abrupt collisions.
6. Langevin
The Langevin [77] thermostat supplements the microcanonical equations of motion with Brownian dynamics, thus including the viscosity and random collision effects of an implicit solvent. It uses a general
equation of the form F = Finteraction + Ffriction + Frandom ,
where Finteraction is the standard interactions calculated
during the simulation, Ffriction is the damping used to
tune the “viscosity” of the implicit bath, and Frandom effectively gives random collisions with solvent molecules.
The frictional and random forces are coupled through
a user-speciﬁed friction damping parameter. Careful
consideration must be taken when choosing this parameter; in the limit of a zero damping parameter, both
frictional and random forces go to zero and the dynamics become microcanonical, and in the limit of an inﬁnite
damping parameter, the dynamics are purely Brownian.
7. Nosé-Hoover
The Nosé-Hoover thermostat [69] abstracts away
the thermal bath from the previous thermostats and
condenses it into a single additional degree of freedom.
This ﬁctitious degree of freedom has a “mass” that can
be changed to interact with the particles in the system
in a predictable and reproducible way while maintain-

ing the canonical ensemble. The choice of “mass” of
the ﬁctitious particle (which in many simulation packages is instead expressed as a time damping parameter) can be important as it affects the ﬂuctuations that
will be observed. For many reasonable choices of the
mass, dynamics are well-preserved [70]. This is one of
the most widely implemented and used thermostats.
However, it should be noted that with small systems,
ergodicity can be an issue [69, 78]. This can become
important even in systems with larger numbers of particles if a portion of the system does not interact strongly
with the remainder of the system, such as in alchemical free energy calculations when a solute or ligand
is non-interacting. Martyna et al. [78] discovered that
by chaining thermostats, ergodicity can be enhanced,
and most implementations of this thermostat use NoséHoover chains.

4.4.4

Summary

Table 1 serves as a general summary and guide for exploring the usage of various thermostats. Knowing the system
you are simulating and the beneﬁts and weaknesses to each
thermostat is crucial to successfully and eﬃciently collect
meaningful, physical data. If you are only interested in sampling structural properties such as radial distribution functions, many of the given thermostats can be used, including
the Gaussian, Bussi, Andersen, Langevin, and Nosé-Hoover
thermostats. If dynamical properties will be sampled, it is
preferable to turn off the thermostat before beginning production cycles, but the Bussi and Nosé-Hoover thermostats
(and in cases with implicit solvent, the Langevin thermostat),
can often be used without overly affecting the calculation of
dynamical properties. Since dynamical properties are unimportant during equilibration, faster algorithms like the Andersen or Bussi thermostats can be used, with a switch to the
Nosé-Hoover thermostat for production. Overall, the Bussi
thermostat has been shown to work well for most purposes,
and its use is recommended as a general-purpose thermostat.

4.5

Barostats

Here, we discuss why barostats are used, give their background, discuss roughly how they work, describe some popular options, and summarize with some recommendations.

4.5.1

Motivation

Typically, thermodynamic properties of interest are measured
under open-air conditions in a laboratory, which (for short
timescales) means at they are measured at essentially
constant temperature and pressure. To obtain a nonatmospheric pressure, some device, like a piston, inert gas,

Table 1. Basic summary of popular thermostats. 7 indicates that the thermostat does not fulﬁll the statement, 3 indicates that the thermostat
does fulﬁll the statement, and (3) indicates that the thermostat fulﬁlls the statement under certain circumstances.

Thermostat

None
Gaussian
Simple Velocity Rescaling
Berendsen
Bussi
Andersen
Langevin
Nosé-Hoover

Ensemble

Deterministic/
Stochastic

Global/
Local

Microcanonical
Isokinetic
Undeﬁned
Undeﬁned
Canonical
Canonical
Canonical
Canonical

Deterministic
Deterministic
Deterministic
Deterministic
Stochastic
Stochastic
Stochastic
Deterministic

Global
Global
Global
Global
Local
Local
Global

etc., would be needed to control the pressure and volume of
the system [59, 79]. Such conditions correspond to what is
called the isothermal-isobaric ensemble, probably one of the
most popular ensembles for MD simulations. As is the case
with thermostats, if the pressure must be maintained in a
simulation, a barostat algorithm will be needed to sample
this ensemble.

4.5.2

Background and How They Work

Barostat algorithms control pressure alone, not temperature,
so if the target ensemble is isothermal-isobaric, they must
be applied with a thermostat. If a barostat is applied without
a thermostat, only the number of particles (N), the pressure
(P), and the enthalpy (H) of the system are held constant.
This is known as the isoenthalpic-isobaric ensemble (NPH).
To sample from the isothermal-isobaric ensemble (NPT), a
thermostating algorithm like the ones discussed earlier must
also be applied.
Much of the background information on barostats is analogous to thermostats. The pressure of a molecular dynamics
simulation is commonly measured using the virial theorem
(an expectation value relating to positions and forces) [7, 59].
When pairwise interactions and periodic boundary conditions
are considered, different approaches are often utilized [12,
59, 79]. Regardless, these formulas give pressure as a timeaveraged quantity, similar to the temperature. If we use these
formulas to calculate the pressure for a single snapshot, this
quantity is referred to as the instantaneous pressure. The
instantaneous pressure will not always be equal to the target
pressure; in fact, in the NPH and NPT ensembles, the instantaneous pressure should undergo ﬂuctuations around the
target pressure.
For the purpose of molecular modeling, consider a hypothetical system that is being compressed and/or expanded
by a ﬁctitious piston that has some mass which acts in all

Physical?

Correct
Structural
Properties?

Correct
Dynamical
Properties?

(3)
(3)

directions uniformly. Since the piston is acting on the system
from all directions, it can be considered as applying a uniform
compression or expansion. The mass of the piston can be
tuned to change the compression of the system, which will
change how often the particles in the system will interact with
the system enclosure. These impacts from the particles on
the “enclosure” will impart a stress on the system box from
the surroundings and serve as a type of barostat.
The next section will describe the main differences between the many barostats that are available, and give some
recommendations for proper use. Some barostats work
based on scaling or rescaling the coordinates in the system (the volume and the center-of-mass coordinates of the
molecules involved), whereas others work by modifying the
equations of motion to ensure constant pressure.

4.5.3

Popular Barostats

Here, we introduce a few notable barostats and give a highlevel summary of each, noting some key issues. This is not
an exhaustive list of barostats and barostat algorithms, just a
sampling of popular and historic ones used in MD.

1. Simple volume rescaling
Every time this barostat is executed, the volume of
the system is modiﬁed such that the instantaneous pressure is exactly equal to the target pressure. This does
not sample the proper ensemble and thus cannot be
used for production sampling [59]. This also does not
smoothly approach the target pressure either, which
might cause very unphysical issues with the system during integration.
2. Berendsen
The Berendesen [74] weak coupling barostat is very
similar to the Berendsen thermostat discussed earlier.
It seeks to improve upon the simple volume rescaling
method mentioned above. This is achieved by coupling

the system to a weakly interacting pressure bath [74].
This bath scales the volume periodically by a scaling
factor, which produces more realisitc ﬂuctuations in the
pressure as it slowly approaches the target pressure. In
contrast to volume rescaling, Berendsen will approach
the target pressure more realistically, but the ensemble
it is sampling from is not well deﬁned and cannot be
guaranteed to be NPT or NPH. Berendsen can be useful
for the beginning stages of equilibration, but should
not be used for production sampling.
3. Andersen
First described by Andersen [76] in 1980, the system
is coupled to a ﬁctitious pressure bath, by adding an additional degree of freedom to the equations of motion.
This behaves as if the system is being acted upon by
an isotropic piston. This is similar to the Nosé-Hoover
thermostat, which is also an extended system algorithm.
This barostat does sample the correct ensemble. However, it is isotropic in nature and applying anisotropic
pressures to parts of the system is not possible.
4. Parrinello-Rahman
The Parrinello-Rahman [80] barostat is an extension
to the Andersen barostat. Unlike the Andersen barostat, Parrinello-Rahman supports the anisotropic scaling
of the size and shape of the simulation box [80]. This
can be quite useful in solid simulations, where phase
changes can be shape changes in a crystal lattice, compared to a liquid or gas, which has no well deﬁned shape.
This barostat has essentially the same properties as the
Andersen one, with the additional support anisotropy.
5. Martyna-Tuckerman-Tobias-Klein (MTTK)
The MTTK barostat has substantial similarity to the
Parrinello-Rahman and Andersen barostats. When Parrinello-Rahman’s equations of motion were discovered
to hold true only in the limit of large systems, the MTTK
barostat introduced alternate equations of motion to
correctly sample the ensemble for smaller systems as
well [81, 82]. Thus, MTTK [81, 82] is usually seen as
an improvement over Parrinello-Rahman [80] for such
systems.
6. Monte Carlo
Constant pressure may also be achieved by periodically performing Monte Carlo moves that adjust the system volume. For an explanation of how such moves are
accepted or rejected, see “Monte Carlo simulations in
other ensembles” in Shell [59]. These MC barostats are
computationally advantageous in that the virial need
not be computed, and they may be easily extended
to accommodate anisotropic systems. They rigorously
explore the correct distribution of volumes in the NPT
ensemble. However, they do not preserve dynamic ﬂuc-

tuations. Unlike for extended system barostats, there is
no sense of relaxation time over which the volume of
the system responds. Instead, the rate at which the volume may respond is limited by the frequency with which
MC moves are performed and the maximum allowed
change in volume. Thus, long-time dynamics are not
accurately reproduced in any sense for MC barostats.

4.5.4

Summary

The simple volume rescaling and Berendsen barostats are
not recommended for collection of production data, as they
do not sample from any correct ensemble, nor do they utilize
any “realistic” approach to achieve the target pressure. They
can, however, be used for approaching the target pressure.
The Berendsen barostat acts in a more realistic fashion in
this regard compared to the volume rescaling barostat, which
itself is primarily useful only as a very stable thermostat for
very early simulation stages if other algorithms have trouble beginning from particularly strained starting structures.
(Alternatively, such issues can be avoided by running NVT
equilibration before using a barostat, Figure 5.) Extended
ensemble barostats are suitable for the production runs of
most systems. It is usually not recommended to use these
for the equilibration process, as these barostats do not behave as well when not near the target pressure. These can
be affected by the starting conﬁguration and pressure values
much more than the Berendsen or simple volume rescaling
barostats. MTTK and Parinello-Rahman allow for more ﬂexibility in terms of the shape modulation of the simulation box.
However, not all extended-ensemble barostats have been
implemented all simulation engines, limiting user choice. It
is recommended to begin with the Berendsen barostat to
quickly bring the system to the target pressure, and then
switch to an extended ensemble barostat for ﬁnal equilibration and production.

4.6

Integrators

For systems consisting of more than three interacting bodies
with no constrained degrees of freedom, there is no analytical solution to the equations of motion. Instead, we must
approximate the dynamics in a discrete manner. This is usually termed numerical integration of the equations of motion.
Algorithms to perform this integration take many forms and
are usually called integrators. Here, we explain the need for
integrators, discuss key criteria like energy conservation, and
highlight a number of commonly used integrators.

4.6.1

Desirable integrator properties

So-called “good” integrators contain certain features that are
appealing for molecular simulations. We start with the most
obvious feature, which is that the integrator induces little

error in the dynamics. Since integration is fundamentally
about taking discrete steps to approximate continuous dynamics, this discretization process introduces errors (as can
be observed by comparison to analytically soluble problems,
like the harmonic oscillator). These errors are termed discretization errors, whereas additional errors called truncation
errors are also accumulated through loss of precision during
computer calculations. As will be discussed shortly, there
are many strategies for avoiding discretization errors. For
truncation errors, the only solution is to utilize a higher precision data type during calculations (i.e. use doubles instead of
ﬂoats).
Integrators that minimize discretization error should preserve phase-space volume and conserve energy. If phase
space volume is not preserved, then the sampled ensemble
at a later timestep will not be the same as that in which the
system was initialized. This means that the collected data will
not in fact reﬂect the ensemble of interest. Luckily, this issue
may be avoided simply by guaranteeing that the integrator is
reversible [6]. More details may be found in Tuckerman et al.
[83], but basically if the mathematical operator representing
the integrator preserves phase space volume, it also satisﬁes the deﬁnition of reversibility: if the operator is applied
to propagate forward by ∆t, the starting condition may be
recovered by in turn applying the operator to the result using
–∆t as the timestep.
Energy conservation is also a desirable integrator property and is imperative in simulating the microcanonical (NVE)
ensemble. This is a much trickier property to examine, and
varies with different integrators. For instance, some classes
of integrators better-preserve energy over short times, while
others better-preserve energy at long times. The latter is generally preferred, though it may necessitate other sacriﬁces
such as greater energy ﬂuctuations away from the desired,
exact system energy. When the energy does change over the
course of a simulation, it is said to “drift.” The most common
reason for energy drift is due to a timestep that is overly long.
If the timestep is much too long, the system can become
unstable and blow up (energies become very large) due to
overlap of atoms. Even when the timestep is long enough that
the system is still stable over long times, it may be too long for
the chosen integrator to conserve energy. Other simulation
parameters may also impact energy drift, such as the method
of truncating forces and energies, as well as the choice of
numerical precision. The latter effect, due to truncation errors, will become obvious if two simulations with different
timesteps are compared. Shorter timesteps, and hence more
steps to achieve a simulation of the same length, will result in
more drift, since errors get larger with the number of calculations performed by the computer. This is exactly opposite to
the behavior that is expected for poor energy conservation

associated with discretization error, where a shorter timestep
will reduce energy drift.
Overall, then, integrators do exhibit energy ﬂuctuations
that are timestep-dependent. All Verlet-equivalent integrators
exhibit energy ﬂuctuations which decrease with the square
of the timestep [12], which is often an important check when
assessing the correctness of an implementation. Thus, both
energy drift and energy ﬂuctuations are important criteria to
understand when assessing integrators, and can be useful
measures of simulation quality in the NVE ensemble.
Additionally, it is also desirable that an integrator be computationally eﬃcient. Integrator cost mostly appears in the
length of the timestep that may be taken while still avoiding
discretization error. As discussed further below, the timestep
must be at least an order of magnitude less than the smallest
timescale of motion present in the system. However, depending on the accuracy of the integrator with respect to
reproducing the true dynamics, a smaller timestep might be
necessary. If the integrator requires a very small timestep
to avoid discretization error, then the computational cost
greatly increases. Hence, a truly “good” integrator allows for
long timesteps while still achieving low discretization error.
This has the added beneﬁt of also reducing truncation error, which is proportional to the number of timesteps taken.
It is worth noting that the issue of integrator choice versus
timestep is not always simple; in some cases, a “better” integrator might allow longer timesteps but also carry an additional computational cost that outweighs the beneﬁts of an
increased timestep.

4.6.2

Deterministic integrators

The most commonly used integrators are variants of the Verlet algorithm (e.g. Velocity Verlet or Leapfrog). Such integrators include terms for updating particle positions up to the
order of the square of the timestep (i.e. they include forces).
Inclusion of higher-order terms is favored in other families
of algorithms, but generally leads to greater complexity and
reduced computational eﬃciency at only marginal improvement in accuracy. Detailed discussion and derivation of many
common integrators may be found in section 7.3 of Leach [7]
and 4.3 of Frenkel and Smit [6]. Such integrators are not applicable, however, for simulations involving stochastic dynamics,
as discussed below.

4.6.3

Stochastic integrators

Stochastic dynamics simulations include application of a random force to each particle, and represent discretizations of
either Langevin or Brownian dynamics. A detailed description
of such stochastic dynamics may be found in McQuarrie [28],
Chapter 20. As detailed in Section 4.4, it is common to apply
temperature control through the use of Langevin dynamics.

As a brief aside, this highlights the fact that the choice of
integrator is often tightly coupled to the choice of thermostat
and/or barostat. Different combinations may demonstrate
better performance and for expanded ensemble methods it
is necessary to utilize an integrator speciﬁc to the selected
temperature- or pressure-control algorithm.
With Langevin or other stochastic dynamics, the random
forces usually prevent the integrator from preserving phasespace volume, which ends up dictating the choice of timestep.
Speciﬁcally, despite issues with phase-space volume, some
stochastic integration schemes achieve preservation of part
of the full phase-space (i.e. conﬁgurations or velocities are
preserved) [84] via cancellation of error. In practice these
issues are easily remedied through an appropriate choice of
timestep depending on the integration scheme.
Stochastic dynamics necessarily perturbs dynamics.
Speciﬁcally, with Langevin or Brownian dynamics, calculations
of any dynamic properties with longer timescales than the
application of the random forces will be very different than
those from deterministic trajectories. If one is interested in
only conﬁgurational or thermodynamic properties of the
system, this is of no consequence. If dynamics are of interest,
the dependence of these properties on the integrator
parameters (e.g. friction factor) should be assessed [70].

4.6.4

Choosing an appropriate timestep

The maximum timestep for a molecular dynamics simulation
is dependent on the choice of integrator and the assumptions
used in the integrator’s derivation. For the commonly used
second order integrators, such as the Verlet and Leapfrog
algorithms, the velocities and accelerations should be approximately constant over the timestep. Thus, the timestep is
limited by the highest frequency motion present in the system, which for all-atom simulations is usually bond vibrations.
It is commonly found that using a timestep that is one tenth
of this vibration’s characteristic period is suﬃcient to conserve energy in the microcanonical ensemble. For example,
if hydrogen molecules are present in the simulation box and
the H-H bond vibration is the highest-frequency motion in
the system with its force ﬁeld harmonic force constant set
to 500 N/m, the oscillation period can be calculated
using
q
µ
the equation for simple harmonic motion (T = 2π k , where
µ is the reduced mass and k is the force constant) to be 8
fs; thus, a 0.5 fs timestep can be used. As another example,
if an ab initio MD simulation is being conducted in which
C-H bond vibrations are known to be the highest-frequency
motion, infrared spectra can be consulted to ﬁnd that this
bond vibration frequency will be approximately 3000 cm–1 ,
which is 11 fs; thus, either a 0.5 or 1.0 fs timestep would
be recommended. For all-atom simulations with constraints
on the high-frequency bonds, timesteps can be commonly

increased to 2 fs; coarse-grained simulations with particles
of higher mass and smaller force constants can have much
larger timesteps. After choosing a timestep, a test simulation
should be run in the microcanonical ensemble to ensure that
the choice of timestep yields dynamics that conserve energy.
The timestep should also be short enough that properties
calculated from the simulation, regardless of ensemble, are
independent of the chosen timestep. This is because an inappropriately large timetep can lead to subtle changes to the
ensemble being simulated [7, 12] and alter computed thermodynamic and transport properties, especially in stochastic
simulations or those coupled to thermostats or barostats [84].
Methods also exist to increase the timestep beyond the limit
imposed by the system’s highest-frequency motion. Some
examples of these enhanced timestepping algorithms include
multiple-timestep methods which separately integrate highfrequency motion from low-frequency motion and schemes
which repartition atomic masses to decrease the highestfrequency motion seen in the system[85, 86].

4.7

Long range electrostatics

In view of the long-range nature of Coulombic interactions
(Section 3.4), handling of electrostatics is particularly important in many systems. Here we describe the motivation for
the different treatments of these terms, and give an overview
of the core idea of the basic algorithms typically employed.

4.7.1

Motivation

The calculation of non-bonded interactions is generally the
most time-consuming step of classical energy calculation.
While the number of type of bonded interactions remain
unchanged during an MD simulation, the strength and importance of non-bonded interactions varies substantially as a
simulation proceeds.
Additionally, Coulombic interactions fall off only very
slowly with distance, as r –1 , further complicating handling
of non-bonded interactions in two different ways. First,
calculating all Coulomb interactions over a periodic system
results in needing to compute a sum which is conditionally
convergent — that is, the value of the sum depends on the
order in which it is evaluated [7], meaning we must exercise
extreme care or the result will be ambiguous. Second,
long-range interactions may be relevant, but determining
pairwise distances is an expensive computation that grows
with the square of the number of atoms involved.
As discussed in Section 4.2, simulations designed to represent bulk systems are generally performed under periodic
boundary conditions, so that the electrostatic potential at any
point is due to all the other charges in the system including
all of their periodic copies. Given that this is the goal, a set
of different methods have been developed to eﬃciently com-

pute the electrostatic potential due to this inﬁnite, periodic
system.
In the early days of simulations, electrostatic interactions
were often simply truncated at a particular cutoff radius (rc ).
This, however, creates artiﬁcial boundary effects and other
problems [12], as well as neglecting important long-range
interactions.

4.7.2

Ewald Summation

The Ewald summation technique [87] provides one way to efﬁciently handle long-range electrostatics in periodic systems.
To understand this technique, consider the relationship between the charge distribution and the Coulombic potential
written in the differential form (the Poisson equation):
∇2 φ(x) = – ρ(x)

where φ(x) is the potential at point x, ρ(x) is the charge density
at point x and  is the permittivity of the medium. The standard way to determine the potential from this equation is to
ﬁrst discretize the equation and then solve, but this requires
the functions ρ and φ to be smooth. However, here, because
we use point charge electrostatics, ρ is a set of delta functions.
The Ewald method is based on (temporarily) replacing the
point charge distributions by smooth charge distributions in
order to apply existing numerical techniques to solve this
partial differential equation (PDE). The most common smooth
function used in the Ewald method is the Gaussian distribution, although other distributions have been used as well.
Thus the overall charge distribution is divided into a shortrange or “direct space” component (ρsr ) involving the original
point charges screened by the Gaussian-distributed charge of
the same magnitude (Figure 6) but opposite sign, and a longrange component involving Gaussian-distributed charges of
the original sign (ρlr ). The screening distribution is of opposite
sign to allow the screened interactions to fall off rapidly with
distance, as we will see below. The sum of the short-range ρsr
and the long-range ρlr charge distributions is still the same as
the original charge distribution.
Unlike the original, full potential, the direct space screened
interaction (Figure 6, top) decays rapidly. In fact, it decays
even faster than Van der Waals interactions (1/r 6 ) and hence
relative short cutoffs, comparable to those used for Van der
Waals interactions, can be used for handling direct-space
Coulomb interactions (Figure 7).
The potential due to long-range charge interactions does
not decay rapidly, and thus requires consideration of all periodic copies. This would pose severe problems if calculated
via direct summation, but the smoothness of the charge ρlr
(and hence potential (φlr ) allows the use of fast PDE solvers.
Speciﬁcally, while the sum is long-ranged in real space, taking the Fourier transform converts it into a sum in reciprocal

Figure 6. Screening charge distribution. (Top) The original charge
distribution. (Bottom) Point charges can be split into Direct space
(blue) and Reciprocal space charges (red). The direct space charge
consists of the original charges and Gaussian-distributed screening
charges of opposite sign. The reciprocal space charge is only the
Gaussian-distributed charge of the original sign. Together these sum
to the original charge distribution, but computation of the electrostatic potential due to each component becomes much easier.

space whichis short-ranged
in reciprocal space, damped by

a factor exp –k 2 σ 2 /2 where k is the reciprocal space vector
and σ is the width of the Gaussian.
The ﬁnal term in Ewald summation is a so-called self term
which gets subtracted out of the overall sum; it is calculated
only once at the beginning of the simulation as it depends
only on the charge magnitudes and not their positions. It also
does not contribute to the force.

4.7.3

Grid based Ewald summation

Ewald summation as described in the previous section takes
O(n3/2 ) time, where n is the number of charge sites. Switching to a discrete Fourier transform can reduce the cost to
to O(nlog(n)). Discretization involves spreading the charge
over a grid. Several common grid-based implementations are
available which tackle this problem, including Particle-Particle
Particle Mesh (P3M), Particle Mesh Ewald (PME) and Smooth
Particle Mesh Ewald (SPME). Speciﬁcs are chosen in each case
to combine accuracy, speed and ease of implementation. In
this subsection, we give an overview of the grid-based approach.
Grid-based Ewald summation approaches involve ﬁve general steps:

1. Charge assignment: In this step, charges are interpolated onto the grid. While the original PME method
uses Lagrangian interpolation for charge assignment,
the SPME method uses the smoother cardinal B-splines

Comparison of 1/r, erfc(r) and 1/r^6
1.0

1/r
1/r^6
erfc(r)/r

0.8
Function value

• Direct-space cutoff: This is typically kept at or near the
value used for the van der Waals cutoff. Decreasing
the cutoff improves the direct space performance but
increases the complexity of the reciprocal space calculations.

0.6

In principle, it is possible to optimize settings for handling
of long-range electrostatics in order to achieve considerable
eﬃciency gains while maintaining accuracy, though this can
involve considerable care [90]. For novice users, we suggest
typically using well-validated or default settings for the particular method employed, and only deviating from these with
careful consideration and testing.

0.4
0.2
0.0
1.00

1.25

1.50

1.75

2.00 2.25
distance (r)

2.50

2.75

3.00

Figure 7. Comparison of decay of the original r –1 term for Coulomb
interactions (blue,*), the resulting direct-space term after Gaussian
screening (black,-) and the r –6 in van der Waals term (red, -.). Note:
The value on the vertical axis has been scaled to allow easy visualization of the relative decay of each term.

(hence the name Smooth-PME) to distribute charge onto
the grid.
2. Transformation of the grid to reciprocal space: A Fast
Fourier Transform (FFT) is used to convert the charges
on the grid to their equivalent Fourier space structure
factors.
3. Energy calculation: The reciprocal space potential is
calculated by solving the Poisson equation in Fourier
space, and the reciprocal space potential is then stored
on the grid.
4. Transformation of the grid back to real space: An Inverse FFT is used to convert the reciprocal space potential back to the real space.
5. Force calculation: The force is given by the gradient of
the potential. PME [35], SPME [88] and P3M [89] use
different methods for calculating the force given the
resulting potential.
Optimizing the performance of grid based methods can
be somewhat challenging; many key choices are made in
method implementation and only relative few settings are
exposed to the user. Some typical options include:
• Grid dimensions or spacing: A ﬁne grid would be slower,
requiring interpolation and calculations for more grid
points, but in principle accuracy should be higher.
• Screening function: The width of the Gaussian screening function can often be tuned, but the ideal width
is coupled with the direct space cutoff giving limited
room for tuning. In some cases alternate, non-Gaussian
screening functions are available.

Should you run MD?

A critical question before preparing an MD simulation of your
system is whether you even should use MD for your system
in view of the resources you have and what information you
hope to obtain. MD is a tool, but it may not be the right tool
for your problem. Before beginning any study, it is critical to
sort out what questions you want to answer, what resources
(computational and otherwise) you have at your disposal, and
whether you have any information about your system(s) of
interest that indicate you can realistically expect to answer
those questions given a set of MD simulations. Try to understand basic concepts of statistical uncertainty ([24] and
https://github.com/dmzuckerman/Sampling-Uncertainty [68])
and use these to make an educated guess regarding your
chances of extracting pertinent and reliable information from
your simulation.
As noted above, the frequency of the fastest vibrational
motions in a system of interest sets a fundamental limit on
the timestep which, given ﬁxed computational resources, sets
a limit on how much simulation time can be covered with
any reasonable amount of computer time. Thus, as noted
in Section 1, the longest all-atom MD simulations are on the
microsecond to millisecond timescale. This means that if your
system is complex and answering your questions will require
sampling critical events that have a timescale of seconds or
longer, MD will not be the right tool for the job. You could
invest a huge amount of effort running MD simulations and
ﬁnd that they did not address your questions.
Ideally, you should have some information before beginning that the relevant timescales for your system might be
accessible given the amount of MD you can afford to run, or
you could plan a set of exploratory MD simulations to assess
feasibility. But do not simply plunge in and attempt to run simulations until you ﬁnd the answers to your questions, as the
required timescales could end up being orders of magnitude
longer than what you can afford to spend. Time is only one
consideration out of many; disk storage and computer time

TAKE STOCK OF YOUR PLANS
 Count the cost: Think about what you know about the timescales of what you want to observe and determine whether
it is tractable to simulate this given the size of your system, your computational resources, and the expense of the
simulation. Would the questions you want to answer be better addressed a different way?
 Pick the desired ensemble (NVT, NPT, NVE, µVT)a
 Determine reference states that you are trying to emulate/discover.
 What temperature, pressure, etc. are you interested in?
 What force ﬁeld properly describes your system?
 What is already known in the literature and what data do you wish to compare to?
a
For mixtures, the semi-grand ensemble (or osmotic ensemble) may be of interest, where the number of particles is ﬁxed but their identities can
change [12] allowing, e.g., a constant chemical potential for salt ions to be maintained [91]

PREPARE TO IMPLEMENT YOUR PLANS AND MAKE CRITICAL DECISIONS ABOUT THE SYSTEM
 Choose a simulation package suitable for simulating that ensemble with your target force ﬁeld
 Determine whether you are simulating a bulk (typically periodic) or ﬁnite system and choose the appropriate cutoff
types and periodicity (full periodicity for bulk systems, partial periodicity for interfaces, etc.) as discussed in Section 4.2
 Prepare your system, paying particular attention to ensuring it contains the chemical components you want with the
structures you want, and that force ﬁeld parameters are assigned as intended (it is good practice to ensure that you
properly implemented the force ﬁeld by replicating energies, forces, or other observables from prior publications)

DETERMINE HANDLING OF CUTOFFS
 As a general rule, electrostatics are long-range enough that either the cutoff needs to be larger than the system size (for
ﬁnite systems) or periodicity is needed along with full treatment of long-range electrostatics (Section 3.4)
 Nonpolar interactions can often be safely treated with cutoffs of 1-1.5 nm as long as the system size is at least twice
that, but long-range dispersion corrections may be needed (Section 4.1)

CHOOSE APPROPRIATE SETTINGS FOR THE DESIRED ENSEMBLE
 Pick a thermostat that gives the correct distribution of temperatures, not just the correct average temperature; if
you have a small system or a system with weakly interacting component choose one which works well even in the
small-system limit.
 Pick a barostat that gives the correct distribution of pressures
 Consider the known shortcomings and limitations of certain integrators and thermostats/barostats and whether your
choices will impact the properties you are calculating

CHOOSE AN APPROPRIATE TIMESTEP FOR STABILITY AND AVOIDING ENERGY DRIFT
 Determine the highest-frequency motion in the system (typically bond vibrations unless bond lengths are constrained)
 As a ﬁrst guess, set the timestep to approximately one tenth of the highest-frequency motion’s characteristic period
 Test this choice by running a simulation in the microcanonical ensemble, and ensure that energy is conserved

DETERMINE YOUR RUN PROTOCOL
 Plan how you will minimize and equilibrate your system and test that your equilibration protocol actually allows you to
reach equilibrium in the target ensemble (Section 4.3)
 Determine production settings, how many steps to run, and how often to store data/what data to store
 Ensure you have suﬃcient storage, memory, and computer time to complete the planned calculations

availability can also prove limiting factors, and opportunity
cost, as well, is not to be overlooked.
Ultimately, we ought to be assessing whether MD is the
best tool for the job. For our problem of interest, will it really
be faster to answer your questions using an MD simulation,
or are there experiments which could be done which would
answer the question more quickly? Maslow famously wrote,
“I suppose it is tempting, if the only tool you have is a hammer,
to treat everything as if it were a nail.” We do not want to
end up in a position where we are running MD simulations
not because they are the best tool for the job, but because
they are the only tool available to us. If an experiment could
answer our key questions with far less cost and time, and
the questions are indeed compelling, perhaps our time might
be better spent ﬁnding a suitable experimental collaborator
rather than running a set of simulations. To give a concrete
example, one could imagine using molecular dynamics simulations to screen a library of commercially available compounds for binding to a potential protein target, but if the
compounds are commercially available at an inexpensive rate
and a suitable assay is available, it might be far faster and
cheaper to simply screen the compounds.
So, count the cost of your potential simulations, assess
whether they realistically have a chance of answering the
questions you seek to answer, and then carefully decide
whether the likelihood of success is worth the cost. If not,
don’t tackle that problem with MD.

Use your MD simulations and interpret
the results with care and caution

Analysis of molecular simulations is largely outside the scope
of this work; however, some words of caution are worthwhile.
It is tempting, especially for those new to or outside of the
area, to view simulations as providing “the answer”, giving
full mechanistic insight in atomistic detail into what happens
in a particular situation and why it happens. Instead, MD
results are better thought of as the results of a computational
experiment that results from a particular model (including
force ﬁeld), system composition, and protocol. The resulting
simulation(s) might or might not be statistically meaningful,
relevant to experiment, or useful, but results will be obtained
regardless.
This, then, leads us to one of the real dangers of molecular simulations: A simulation produces results, which tempt
users to interpret or overinterpret them, whether the results
are meaningful or not. For example, even a very short, unequilibrated MD simulation can produce movies which appear interesting and, by virtue of the fact that they result
from MD, reveal the positions of all the atoms in a system
as a function of time. It’s easy to run several short MD sim-

ulations where (for example) the composition of the system
is varied, and conclude that any observed differences are
a result of variations in composition. But as noted in Section 4.3.3, even simulations started from the same structure
but slightly different initial positions or velocities will diverge
over time yielding different results, so perhaps any differences are simply a result of this divergence rather than due
to the change in conditions. Thus, analysis will require great
care and caution to avoid overinterpreting data, and error
analysis becomes particularly critical (as discussed in https:
//github.com/dmzuckerman/Sampling-Uncertainty [68]).
In summary, then, do not use MD simulations simply to
make movies and inspect these. Considerable care must be
exercised to avoid overinterpeting the full atomistic detail
they provide. While movies in some cases can be useful,
proper error analysis is always essential.

Conclusions

Molecular simulations are particularly exciting, because they
provide a detailed view into the structure and function of
systems at a molecular or atomistic level. Additionally, they
allow us to precisely compute thermodynamic and statistical
properties and connect these to underlying motions, structure, and function. Thus MD has played a signiﬁcant role in
our ﬁeld in suggesting new experiments, generating ideas,
and helping to provide mechanistic understanding. Advances
in hardware, software, methods and force ﬁelds also make
MD-based calculations particularly appealing for predictive
molecular design, where simulations could be used to help
guide experiments to develop materials or molecules with
desired properties.
Still, MD simulations require considerable care, as conducting them requires choosing a variety of settings, and the
optimal choice of settings typically depends on the problem
being considered. Thus, it is our hope that this document
provides a helpful overview of some of the fundamental considerations for preparing and conducting MD simulations
and paves the way for more specialized documents which
will focus on calculations of speciﬁc properties or for speciﬁc
classes of systems, since the approach employed will often
need to vary depending on such choices.
This document also provides a checklist covering some of
the key points raised in this work and highlighting particularly
common sources of failure; we encourage readers to follow
this when considering a simulation study.
Our focus here has been on the basics — focusing on
things you need to understand before beginning to prepare
simulations for yourself. Additionally, we have primarily focused on issues relating to how simulations are conducted,
and leave data analysis for a separate treatment. As a start-

ing point relating to data analysis, readers should probably review the Best Practices document on sampling and
uncertainty estimation (https://github.com/dmzuckerman/
Sampling-Uncertainty [68]).
Please remember that this is an updatable work, so we
welcome contributions and suggestions via our GitHub issue
tracker at https://github.com/MobleyLab/basic_simulation_
training.

Author Information

[10] Mobley DL. Let’s Get Honest about Sampling. J Comput Aided
Mol Des. 2012; 26:93–95. https://doi.org/10.1007/s10822-0119497-y.
Recent Devel[11] Chen W, Morrow BH, Shi C, Shen JK.
opment and Application of Constant pH Molecular Dynamics.
Molecular Simulation. 2014; 40(10-11):830–838.
https://doi.org/10.1080/08927022.2014.907492.
[12] Allen MP, Tildesley DJ. Computer Simulation of Liquids. 2 ed.
Oxford Science Publications, New York, NY: Oxford University
Press; 2017.
[13] Tuckerman ME. Statistical Mechanics: Theory and Molecular
Simulation. Oxford Graduate Texts, Oxford, New York: Oxford
University Press; 2010.

ORCID:
Efrem Braun: 0000-0001-5379-7031
Justin Gilmer: 0000-0002-6915-5591
Heather B. Mayes: 0000-0002-6915-5591
David L. Mobley: 0000-0002-6915-5591
Jacob I. Monroe: 0000-0002-7654-2856
Samarjeet Prasad: 0000-0001-8320-6482
Daniel M. Zuckerman: 0000-0001-7662-2031

[14] Shell MS. Thermodynamics and Statistical Mechanics: An Integrated Approach. Cambridge University Press; 2015.
[15] Dill KA, Bromberg S. Molecular Driving Forces: Statistical Thermodynamics in Biology, Chemistry, Physics, and Nanoscience.
Second ed. Garland Science; 2010.
[16] Kofke DA. Direct evaluation of phase coexistence by molecular
simulation via integration along the saturation line. J Chem Phys.
1993; 98(5):4149–4162. https://doi.org/10.1063/1.465023.

References
[1] Nussinov R. The Signiﬁcance of the 2013 Nobel Prize in Chemistry and the Challenges Ahead. PLoS Comput Biol. 2014;
10(1):2013–2014. https://doi.org/10.1371/journal.pcbi.1003423.
[2] Towns J, Cockerill T, Dahan M, Foster I, Gaither K, Grimshaw
A, Hazlewood V, Lathrop S, Lifka D, Peterson GD, Roskies
R, Scott JR, Wilkens-Diehr N.
XSEDE: Accelerating Scientiﬁc Discovery.
Comput Sci Eng. 2014; 16(5):62–74.
https://doi.org/10.1109/MCSE.2014.80.
[3] Kirchmair J, Göller AH, Lang D, Kunze J, Testa B, Wilson ID,
Glen RC, Schneider G. Predicting drug metabolism: experiment
and/or computation? Nat Rev Drug Discov. 2015; 14(6):387–404.
https://doi.org/10.1038/nrd4581.
[4] Sresht V, Lewandowski EP, Blankschtein D, Jusuf A.
Combined Molecular Dynamics Simulation–MolecularThermodynamic Theory Framework for Predicting Surface Tensions.
Langmuir. 2017;
33(33):8319–8329.
https://doi.org/10.1021/acs.langmuir.7b01073.
[5] Bottaro S, Lindorff-Larsen K. Biophysical experiments and
biomolecular simulations: A perfect match? Science. 2018;
360:355–360. http://science.sciencemag.org/content/361/6400/
355/tab-pdf.
[6] Frenkel D, Smit B. Understanding Molecular Simulation: From
Algorithms to Applications. 2nd ed. Academic Press; 2001.

[17] Gonzalez Salgado D, Vega C. Melting point and phase diagram of methanol as obtained from computer simulations
of the OPLS model. J Chem Phys. 2010; 132(9):094505.
https://doi.org/10.1063/1.3328667.
[18] Atkins P, Paula Jd. Atkins’ Physical Chemistry. Tenth revised
edition ed. Oxford University Press; 2014.
[19] McQuarrie DA, Simon JD. Physical Chemistry: A Molecular
Approach. University Science Books; 1997.
[20] Kittel C, Kroemer H. Thermal Physics. 2nd ed. W. H. Freeman;
1980.
[21] Zuckerman DM. Statistical Physics of Biomolecules: An Introduction. CRC Press; 2010.
[22] Zuckerman DM. Equilibrium Sampling in Biomolecular Simulations. Annual Review of Biophysics. 2011; 40(1):41–62.
https://doi.org/10.1146/annurev-biophys-042910-155255.
[23] Chong LT, Saglam AS, Zuckerman DM.
Path-Sampling
Strategies for Simulating Rare Events in Biomolecular Systems. Current Opinion in Structural Biology. 2017; 43:88–94.
https://doi.org/10.1016/j.sbi.2016.11.019.

[7] Leach AR. Molecular Modelling: Principles and Applications.
Second ed. Essex, England: Pearson Education Limited; 2001.

[24] Grossﬁeld A, Zuckerman DM. Quantifying Uncertainty and
Sampling Quality in Biomolecular Simulations. Annu Rep
Comput Chem. 2009; 5:23–48. https://doi.org/10.1016/S15741400(09)00502-7.

[8] Jensen F. Introduction to Computational Chemistry. Second ed.
West Sussex, England: John Wiley & Sons; 2007.

[25] Zuckerman DM, FAQ on Trajectory Ensembles | Statistical Biophysics Blog; 2015.

[9] Schlick T. Molecular Modeling and Simulation: An Interdisciplinary Guide, vol. 21 of Interdisciplinary Applied Mathematics.
2 ed. New York: Springer; 2010.

[26] Zuckerman DM, Chong LT.
Weighted Ensemble Simulation: Review of Methodology, Applications, and Software.
Annual Review of Biophysics. 2017; 46(1):43–57.
https://doi.org/10.1146/annurev-biophys-070816-033834.

[27] Reif F. Fundamentals of Statistical and Thermal Physics. Long
Grove, IL: Waveland Press, Inc.; 2009.
[28] McQuarrie DA. Statistical Mechanics. University Science Books;
2000.
[29] Hill TL. Statistical Mechanics: Principles and Selected Applications. Dover Publications; 1987.
[30] Chandler D. Introduction to Modern Statistical Mechanics. Oxford University Press; 1987.
[31] Ponder JW, Case DA.
Force ﬁelds for protein simulations.
Advances in Protein Chemistry. 2003; 66:27–85.
https://doi.org/10.1016/S0065-3233(03)66002-X.
[32] Ponder JW, Wu C, Ren P, Pande VS, Chodera JD, Schnieders MJ,
Haque I, Mobley DL, Lambrecht DS, DiStasio RA, Head-Gordon
M, Clark GNI, Johnson ME, Head-Gordon T. Current Status of
the AMOEBA Polarizable Force Field. J Phys Chem B. 2010;
114(8):2549–2564. https://doi.org/10.1021/jp910674d.
[33] Lemkul JA, Huang J, Roux B, Mackerell, Jr AD.
An
Empirical Polarizable Force Field Based on the Classical
Drude Oscillator Model: Development History and Recent Applications.
Chem Rev. 2016; 116(9):4983–5013.
https://doi.org/10.1021/acs.chemrev.5b00505.
[34] York DM, Darden TA, Pedersen LG. The Effect of Longrange Electrostatic Interactions in Simulations of Macromolecular Crystals: A Comparison of the Ewald and Truncated List Methods. J Chem Phys. 1993; 99(10):8345–8348.
https://doi.org/10.1063/1.465608.
[35] Darden T, York D, Pedersen L. Particle Mesh Ewald: An N Log( N
) Method for Ewald Sums in Large Systems. J Chem Phys. 1993;
98(12):10089–10092. https://doi.org/10.1063/1.464397.
[36] Piana S, Lindorff-Larsen K, Dirks RM, Salmon JK, Dror
RO, Shaw DE.
Evaluating the Effects of Cutoffs and
Treatment of Long-Range Electrostatics in Protein
Folding Simulations.
PLoS ONE. 2012; 7(6):e39918.
https://doi.org/10.1371/journal.pone.0039918.
[37] Sagui C, Darden TA. MOLECULAR DYNAMICS SIMULATIONS OF
BIOMOLECULES: Long-Range Electrostatic Effects. Annual Review of Biophysics and Biomolecular Structure. 1999; 28(1):155–
179. https://doi.org/10.1146/annurev.biophys.28.1.155.
[38] Cisneros GA, Karttunen M, Ren P, Sagui C. Classical Electrostatics for Biomolecular Simulations. Chemical Reviews. 2014;
114(1):779–814. https://doi.org/10.1021/cr300461d.
[39] Griﬃths DJ. Introduction to Electrodynamics. 4th ed. Cambridge University Press; 2017.
[40] Jackson JD. Classical Electrodynamics. 3rd ed. Wiley; 1998.
[41] Mobley D, Bannan CC, Rizzi A, Bayly CI, Chodera JD, Lim VT,
Lim NM, Beauchamp KA, Shirts MR, Gilson MK, Eastman PK.
Open Force Field Consortium: Escaping Atom Types Using Direct
Chemical Perception with SMIRNOFF v0.1. bioRxiv. 2018; p.
286542. https://doi.org/10.1101/286542.

[42] Wang LP, McKiernan KA, Gomes J, Beauchamp KA, Head-Gordon
T, Rice JE, Swope WC, Martínez TJ, Pande VS. Building a More
Predictive Protein Force Field: A Systematic and Reproducible
Route to AMBER-FB15. J Phys Chem B. 2017; 121(16):4023–4039.
https://doi.org/10.1021/acs.jpcb.7b02320, pMID: 28306259.
[43] Mackerell, Jr AD, Feig M, Brooks, III CL. Extending the
treatment of backbone energetics in protein force ﬁelds:
Limitations of gas-phase quantum mechanics in reproducing protein conformational distributions in molecular dynamics simulations. J Comput Chem. 2004; 25(11):1400–1415.
https://doi.org/10.1002/jcc.20065.
[44] Perez A, MacCallum JL, Brini E, Simmerling C, Dill KA. GridBased Backbone Correction to the ff12SB Protein Force Field
for Implicit-Solvent Simulations. J Chem Theory Comput. 2015;
11(10):4770–4779. https://doi.org/10.1021/acs.jctc.5b00662.
[45] Sanyal T, Shell MS. Coarse-grained models using local-density
potentials optimized with the relative entropy: Application
to implicit solvation. J Chem Phys. 2016; 145(3):034109.
https://doi.org/10.1063/1.4958629.
[46] Becker CA, Tavazza F, Trautt ZT, Buarque De Macedo RA. Considerations for choosing and using force ﬁelds and interatomic
potentials in materials science and engineering. Current Opinion in Solid State and Materials Science. 2013; 17(6):277–283.
https://doi.org/10.1016/j.cossms.2013.10.001.
[47] Case DA, Cerutti DS, Cheatham, III TE, Darden TA, Duke RE,
Giese TJ, Gohlke H, Goetz AW, Greene D, Homeyer N, Izadi S,
Kovalenko A, Lee TS, LeGrand S, Li P, Lin C, Liu J, Luchko T, Luo
R, Mermelstein D, et al., Amber Reference Manuals;. http://
ambermd.org/Manuals.php.
[48] Apol E, Apostolov R, Berendsen HJC, van Buuren A, Bjelkmar
P, van Drunen R, Feenstra A, Fritsch S, Groenhof G, Junghans
C, Hub J, Kasson P, Kutzner C, Lambeth B, Larsson P, Lemkul
JA, Lindahl V, Lundborg M, Marklund E, Meulenhoff P, et al.,
GROMACS Documentation Reference Manual;. http://manual.
gromacs.org/documentation/.
[49] Riniker S. Fixed-Charge Atomistic Force Fields for Molecular
Dynamics Simulations in the Condensed Phase: An Overview.
Journal of Chemical Information and Modeling. 2018; 58(3):565–
578. https://doi.org/10.1021/acs.jcim.8b00042.
[50] Mishra RK, Mohamed AK, Geissbühler D, Manzano H, Jamil
T, Shahsavari R, Kalinichev AG, Galmarini S, Tao L, Heinz
H, Pellenq R, van Duin ACT, Parker SC, Flatt RJ, Bowen
P. cemff: A force ﬁeld database for cementitious materials including validations, applications and opportunities.
Cement and Concrete Research. 2017; 102(October):68–89.
https://doi.org/10.1016/j.cemconres.2017.09.003.
[51] Lopes PEM, Roux B, Mackerell, Jr AD. Molecular modeling and
dynamics studies with explicit inclusion of electronic polarizability: Theory and applications. Theoretical Chemistry Accounts.
2009; 124(1-2):11–28. https://doi.org/10.1007/s00214-009-0617x.
[52] Onufriev AV, Izadi S. Water models for biomolecular simulations. Wiley Interdisciplinary Reviews: Computational Molecular
Science. 2018; 8(2). https://doi.org/10.1002/wcms.1347.

[53] Vega C, Abascal JLF.
Simulating water with rigid nonpolarizable models: A general perspective.
Physical
Chemistry Chemical Physics. 2011; 13(44):19663–19688.
https://doi.org/10.1039/c1cp22168j.
[54] Tadmor EB, Elliott, S R, Sethna JP, Miller RE, Becker CA, Knowledgebase of Interatomic Models (KIM);. https://openkim.org.
[55] Hale L, Trautt Z, Becker C, Interatomic Potentials Repository
Project;. https://www.ctcms.nist.gov/potentials/.
[56] Shirts MR, Mobley DL, Chodera JD, Pande VS. Accurate and Eﬃcient Corrections for Missing Dispersion Interactions in Molecular Simulations. J Phys Chem B. 2007; 111(45):13052–13063.
https://doi.org/10.1021/jp0735987.
[57] Isele-Holder RE, Mitchell W, Ismail AE. Development and Application of a Particle-Particle Particle-Mesh Ewald Method for
Dispersion Interactions. J Chem Phys. 2012; 137(17):174107.
https://doi.org/10.1063/1.4764089.
[58] Dupradeau FY, Pigache A, Zaffran T, Savineau C, Lelong R,
Grivel N, Lelong D, Rosanski W, Cieplak P. The R.E.D. Tools:
Advances in RESP and ESP Charge Derivation and Force Field Library Building. Phys Chem Chem Phys. 2010; 12(28):7821–7839.
https://doi.org/10.1039/C0CP00111B.
[59] Shell MS, Principles of modern molecular simulation methods:
Lecture Notes;. https://engineering.ucsb.edu/~shell/che210d/
assignments.html.

[68] Grossﬁeld A, Patrone PN, Roe DR, Schultz A J, Siderius DW, Zuckerman DM. Best Practices for Quantiﬁcation of Uncertainty and
Sampling Quality in Molecular Simulations [Article v1.0]. Living
Journal of Computational Molecular Science. 2019; 1(1):5067.
https://doi.org/10.33011/livecoms.1.1.5067.
[69] Hünenberger PH. Thermostat algorithms for molecular dynamics simulations. Advanced Computer Simulation. 2005; p.
105–149. https://doi.org/10.1007/b99427.
[70] Basconi JE, Shirts MR. Effects of Temperature Control Algorithms on Transport Properties and Kinetics in Molecular Dynamics Simulations. J Chem Theory Comput. 2013; 9(7):2887–
2899. https://doi.org/10.1021/ct400109a.
[71] Minary P, Martyna GJ, Tuckerman ME. Algorithms and novel
applications based on the isokinetic ensemble. I. Biophysical
and path integral molecular dynamics. J Chem Phys. 2003;
118(6):2510–2526. https://doi.org/10.1063/1.1534582.
[72] Braun E, Moosavi SM, Smit B. Anomalous effects of velocity rescaling algorithms: the ﬂying ice cube effect revisited. J Chem Theory Comput. 2018; 14(10):5262–5272.
https://doi.org/10.1021/acs.jctc.8b00446.
[73] Harvey SC, Tan RKZ, Cheatham TE.
The Flying Ice
Cube: Velocity Rescaling in Molecular Dynamics Leads
to Violation of Energy Equipartition.
J Comp Chem.
1998; 19(7):726–740.
https://doi.org/10.1002/(SICI)1096987X(199805)19:7<726::AID-JCC4>3.0.CO;2-S.

[60] Yeh IC, Hummer G. System-Size Dependence of Diffusion
Coeﬃcients and Viscosities from Molecular Dynamics Simulations with Periodic Boundary Conditions. J Phys Chem B. 2004;
108(40):15873–15879. https://doi.org/10.1021/jp0477147.

[74] Berendsen HJ, Postma Jv, van Gunsteren WF, DiNola A, Haak J.
Molecular dynamics with coupling to an external bath. J Chem
Phys. 1984; 81(8):3684–3690. https://doi.org/10.1063/1.448118.

[61] Lemkul J, GROMACS Tutorials;. http://www.bevanlab.biochem.
vt.edu/Pages/Personal/justin/gmx-tutorials.

[75] Bussi G, Donadio D, Parrinello M.
Canonical sampling
through velocity rescaling. J Chem Phys. 2007; 126(1):014101.
https://doi.org/10.1063/1.2408420.

[62] Madej B, Walker R, AMBER Tutorial B0: An Introduction to Molecular Dynamics Simulations Using AMBER;. http://ambermd.org/
tutorials/basic/tutorial0/index.html.

[76] Andersen HC. Molecular dynamics simulations at constant
pressure and/or temperature. J Chem Phys. 1980; 72(4):2384–
2393. https://doi.org/10.1063/1.439486.

[63] Jewett A, Moltemplate; 2018. https://www.moltemplate.org/.

[77] Schneider T, Stoll E. Molecular-dynamics study of a threedimensional one-component model for distortive phase
transitions.
Physical Review B. 1978; 17(3):1302–1322.
https://doi.org/10.1103/physrevb.17.1302.

[64] Martínez L, Andrade R, Birgin EG, Martínez JM. PACKMOL: A
Package for Building Initial Conﬁgurations for Molecular Dynamics Simulations. J Comp Chem. 2009; 30(13):2157–2164.
https://doi.org/10.1002/jcc.21224.
[65] Hirel P. Atomsk: A Tool for Manipulating and Converting Atomic
Data Files. Computer Physics Communications. 2015; 197:212–
219. https://doi.org/10.1016/j.cpc.2015.07.012.
[66] Joswiak MN, Duff N, Doherty MF, Peters B. Size-Dependent
Surface Free Energy and Tolman-Corrected Droplet Nucleation
of TIP4P/2005 Water. J Phys Chem Letters. 2013; 4(24):4267–
4272. https://doi.org/10.1021/jz402226p, pMID: 26296177.
[67] Palmer JC, Haji-Akbari A, Singh RS, Martelli F, Car R, Panagiotopoulos AZ, Debenedetti PG. Comment on "The putative liquid-liquid transition is a liquid-solid transition in atomistic models of water" [I and II: J. Chem. Phys. 135, 134503
(2011); J. Chem. Phys. 138, 214504 (2013)]. J Chem Phys. 2018;
148(13):137101. https://doi.org/10.1063/1.5029463.

[78] Martyna GJ, Klein ML, Tuckerman M. Nosé–Hoover chains: the
canonical ensemble via continuous dynamics. J Chem Phys.
1992; 97(4):2635–2643. https://doi.org/10.1063/1.463940.
[79] Tuckerman M. Statistical mechanics: theory and molecular
simulation. Oxford university press; 2010.
[80] Parrinello M, Rahman A.
Polymorphic transitions in
single crystals:
A new molecular dynamics method.
Journal of Applied Physics. 1981;
52(12):7182–7190.
https://doi.org/10.1063/1.328693.
[81] Martyna GJ, Tobias DJ, Klein ML. Constant pressure molecular
dynamics algorithms. J Chem Phys. 1994; 101(5):4177–4189.
https://doi.org/10.1063/1.467468.

[82] Martyna GJ, Tuckerman ME, Tobias DJ, Klein ML.
Explicit reversible integrators for extended systems dynamics.
Molecular Physics. 1996; 87(5):1117–1157.
https://doi.org/10.1080/00268979600100761.
[83] Tuckerman M, Berne BJ, Martyna GJ. Reversible multiple time
scale molecular dynamics. J Chem Phys. 1992; 97(3):1990–2001.
https://doi.org/10.1063/1.463137.
[84] Fass J, Sivak D, Crooks GE, Beauchamp KA, Leimkuhler B,
Chodera J. Quantifying conﬁguration-sampling error in Langevin
simulations of complex molecular systems. bioRxiv. 2018; p.
266619. https://doi.org/10.1101/266619.
[85] Berne BJ. Molecular Dynamics in Systems with Multiple Time
Scales: Reference System Propagator Algorithms. In: Deuﬂhard
P, Hermans J, Leimkuhler B, Mark AE, Reich S, Skeel RD, editors.
Computational Molecular Dynamics: Challenges, Methods, Ideas
Berlin: Springer; 1999. p. 297–317.
[86] Hopkins CW, Le Grand S, Walker RC, Roitberg AE. Longtime-step molecular dynamics through hydrogen mass repartitioning. J Chem Theory Comput. 2015; 11(4):1864–1874.
https://doi.org/10.1021/ct5010406.
[87] Ewald PP. Die Berechnung optischer und elektrostatischer
Gitterpotentiale. Annalen der Physik. 1921; 369(3):253–287.
https://doi.org/10.1002/andp.19213690304.
[88] Essmann U, Perera L, Berkowitz ML, Darden T, Lee H, Pedersen
LG. A smooth particle mesh Ewald method. J Chem Phys. 1995;
103(19):8577–8593. https://doi.org/10.1063/1.470117.
[89] Eastwood JW, Hockney RW, Lawrence DN. P3M3DP—The
three-dimensional periodic particle-particle/particle-mesh program. Computer Physics Communications. 1980; 19(2):215–261.
https://doi.org/https://doi.org/10.1016/0010-4655(80)90052-1.
[90] Paliwal H, Shirts MR. Using Multistate Reweighting to Rapidly
and Eﬃciently Explore Molecular Simulation Parameters Space
for Nonbonded Interactions. J Chem Theory Comput. 2013;
9(11):4700–4717. https://doi.org/10.1021/ct4005068.
[91] Ross GA, Rustenburg AS, Grinaway PB, Fass J, Chodera
JD. Biomolecular Simulations under Realistic Macroscopic
Salt Conditions. J Phys Chem B. 2018; 122(21):5466–5486.
https://doi.org/10.1021/acs.jpcb.7b11734.
