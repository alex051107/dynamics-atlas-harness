# Benchmarking Generative AI and Physics-Based Molecular Simulation for Sampling Conformational Heterogeneity in T4 Lysozyme

Source: user-provided acs.jcim.6c02044.pdf. Converter: installed pdftotext -layout fallback; pdf-to-markdown lacked @opendocsg/pdf2md. Original PDF unchanged. Layout extraction may reorder columns or alter equations; use PDF for formal verification.

## PDF page 1

pubs.acs.org/jcim                                                                                                                                 Article



Benchmarking Generative AI and Physics-Based Molecular
Simulation for Sampling Conformational Heterogeneity in T4
Lysozyme
Soumendranath Bhakat*




                                                                                                                                                                 Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026
      Cite This: https://doi.org/10.1021/acs.jcim.6c02044                            Read Online


ACCESS                         Metrics & More                             Article Recommendations               *
                                                                                                                sı Supporting Information


ABSTRACT: Wild-type T4 lysozyme (T4L) is used as a benchmark to
evaluate conformational sampling across generative AI, AI-accelerated
molecular simulation (AMS), and physics-based enhanced molecular
dynamics (EMD). A four-state model�exposed/open, exposed/closed,
buried/open, and buried/closed; is defined using physically meaningful
collective variables. Generative AI methods (AF-cluster, MSA subsampling
of AlphaFold2, ConforFold, AlphaFlow, ESMFlow, ConfRover, BioEmu)
largely sample only the exposed/open state. In contrast, AMS integrates
generative ensembles with physics-based molecular simulations, recovering
all states and reproducing equilibrium populations similar to EMD and
experimental smFRET signatures.




■    INTRODUCTION
Proteins are molecular machines that govern biological function.
                                                                                alternate states and their relative populations across a diverse
                                                                                range of biomolecular systems. Sampling efficiency is assessed
They are not static structures but interconvert between multiple                by how well these methods capture state populations along
transiently populated metastable states, each capable of                        collective variables (CVs) that discriminate transient states from
activating distinct signaling pathways. The populations of                      the ground state.12 However, fair comparisons between physics-
these states are modulated by environmental perturbations                       based enhanced sampling and GenAI methods are rare due to
such as temperature, pH, ligand binding, and mutations.                         three key challenges. A minimal benchmark system must have
Sampling the transiently populated states is therefore central                  experimentally validated transient states with CVs simple
to understanding how proteins encode function, yet it remains                   enough to distinguish those states from the ground state. It
one of the hardest problems in structural biology.1−5                           must have sufficient structural data in the Protein Data Bank so
   The development of generative AI (GenAI) algorithms such                     that limited training data cannot be used as a confounding factor.
as AlphaFold has enabled accurate prediction of static protein                  And system size must not unfairly disadvantage GenAI methods,
structures from sequence alone, but these algorithms do not                     which often struggle with larger and more conformationally
sample transiently populated alternate conformational states. A                 complex systems.
growing subfield of machine learning for structural biology has                    Wild-type T4 lysozyme (T4L) satisfies all three criteria. It is
aimed to address this by predicting conformational ensembles                    small (164 residues), has single-molecule FRET (smFRET) data
from sequence alone.1 These approaches fall into two                            that directly validates transiently populated alternate states, and
subgroups: MSA-based methods, which perturb evolutionary                        has been extensively studied by physics-based enhanced
coupling information in multiple sequence alignments to                         sampling methods. Yet, no prior study has systematically
generate structural diversity, and generative models such as                    compared GenAI methods, AI-accelerated molecular simula-
diffusion models or flow-matching frameworks, trained on short                  tion, and physics-based enhanced sampling on the same system
MD simulations data, which claim to sample transiently                          using well characterized CVs. I close this gap here. Additionally,
populated alternate states. Despite rapid growth in both
subgroups, systematic benchmarking against physically rigorous
reference data remains absent, making it difficult to assess                    Received: June 20, 2026
whether these methods genuinely capture biologically relevant                   Revised: August 26, 2026
conformational diversity or simply reproduce structural noise.                  Accepted: August 27, 2026
   Physics-based enhanced sampling methods such as metady-
namics,6−9 adaptive sampling,10 and replica exchange11 provide
such a reference. They can sample transiently populated

                                       © XXXX American Chemical Society                                               https://doi.org/10.1021/acs.jcim.6c02044
                                                                            A                                         J. Chem. Inf. Model. XXXX, XXX, XXX−XXX


## PDF page 2

Journal of Chemical Information and Modeling                                            pubs.acs.org/jcim                                       Article




                                                                                                                                                               Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026
Figure 1. Schematic of the AI-accelerated molecular simulation (AMS) workflow. The workflow begins with the T4L sequence, followed by ensemble
generation using multiple GenAI methods, including AF-cluster, ConforFold, BioEmu, ConfRover, ESMFlow, and AlphaFlow. K-center clustering was
then performed using transformed distance features to select an initial “starting ensemble” of N = 100 structures. Unbiased molecular dynamics
simulations of 200 ns were initiated from each member of this starting ensemble in Round 1. The resulting trajectories were clustered using the K-
center algorithm on transformed distances, yielding a “physics-refined ensemble” of N = 80 structures. Additional unbiased molecular dynamics
simulations of 200 ns each were then initiated from the physics-refined ensemble in Round 2. A Markov state model (MSM) was constructed using
RMSD features from the combined Round 1 and Round 2 simulations. Equilibrium populations were then projected onto different collective variables
to predict conformational populations and heterogeneity in T4L.

I introduce a new framework called AI-accelerated molecular                 four-state classification enables quantitative comparison of state
simulation (AMS). AMS combines multiple GenAI methods to                    populations across all methods.
construct a highly diverse structural prior, which is then used to             In this paper, I benchmarked three classes of methods. The
seed independent molecular dynamics simulations and capture                 first class comprises GenAI approaches, divided into two
the full scope of conformational dynamics in T4L (Figure 1). By             subgroups. The first subgroup consists of MSA-based methods:
uniting these generative models into a single bucket of ensemble            AF-cluster,16 which clusters MSA subsamples as input to
generator, AMS overcomes the sampling deficiencies inherent to              AlphaFold2;17 reduced MSA subsampling with AlphaFold2
any individual algorithm. This approach yields a significantly              (rMSA-AF2);18 and ConforFold,19 a retrained OpenFold2
broader initial distribution and increases the probability of               model designed to predict alternate conformations. The second
capturing rare conformational events compared to relying on a               subgroup consists of generative models trained on structural or
single GenAI protein ensemble generator augmented by                        simulation data: AlphaFlow,20 ESMFlow,20 ConfRover,21 and
molecular simulations.                                                      BioEmu.22 The second class is AMS, a methodological

■   RESULTS
I used two sets of CVs to describe the conformational ensemble
                                                                            contribution of this work, in which GenAI ensembles seed
                                                                            multiple rounds of unbiased MD simulations that are combined
                                                                            using a Markov state model (MSM)23,24 to recover physically
of T4L. The first is a two-dimensional CV defined by two Cα                 refined state populations (Figure 1). The third class is physics-
distances: d1 (Ser44−Ile150) and d2 (Glu22−Gln141). The                     based enhanced sampling repurposed from Miller and co-
Ser44−Ile150 residue pair was used by Miller and co-workers13 to            workers,13 combining 5 μs unbiased MD simulations with
drive metadynamics simulations, enabling comparison of                      metadynamics-seeded unbiased MD simulations (hereafter
predicted smFRET signals with experimental smFRET data to                   enhanced molecular dynamics, EMD), which serves as the
probe the opening and closing motion of T4, with d1 < 2.5 nm                quantitative reference for all comparisons.
defining the closed state and d1 > 2.5 nm defining the open state.             AMS successfully sampled all four conformational states:
The Glu22−Gln141 distance, introduced by Abou-Hatab and                     exposed/open, exposed/closed, buried/open, and buried/
Abrams,14 serves as an orthogonal CV capturing hinge domain                 closed. The two dominant states, exposed/open (AMS:
motion. The second CV is the locking coordinate p, developed                38.3%, EMD: 39.1%) and buried/open (AMS: 58.7%, EMD:
by Stock and co-workers,15 which quantifies the solvent exposure            54.0%), were recovered with relative populations comparable to
of Phe4 relative to the hinge helix. A positive value (p > 0)               EMD. The transiently populated buried/closed state was also
indicates that Phe4 is solvent-exposed, while a negative value (p           recovered with a comparable population (AMS: 2.3%, EMD:
< 0) indicates it is buried within the interdomain interface.               2.9%). The exposed/closed state, however, was underrepre-
Combined with d1, this defines a four-state model: exposed/                 sented in AMS relative to EMD (AMS: 0.7%, EMD: 3.9%),
closed, exposed/open, buried/closed, and buried/open. This                  suggesting that this particular transient state remains the most
                                                                        B                                           https://doi.org/10.1021/acs.jcim.6c02044
                                                                                                                    J. Chem. Inf. Model. XXXX, XXX, XXX−XXX


## PDF page 3

Journal of Chemical Information and Modeling                                              pubs.acs.org/jcim                                        Article




                                                                                                                                                                  Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026




Figure 2. Collective variables used to characterize T4 lysozyme conformational heterogeneity and comparison of sampling across different approaches.
(A) Pictorial representation of the d1 and d2 collective variables, defined as the Cα−Cα distances between Ser44 (S44) and Ile150 (I150) and between
Glu22 (E22) and Gln141 (Q141), respectively. The d1 coordinate distinguishes closed and open conformations, with d1 < 2.5 nm corresponding to
the closed state and d1 > 2.5 nm corresponding to the open state. (B) Definition of the locking coordinate p, which describes the position of the Phe4
(F4) side chain relative to the hydrophobic cavity. The cavity direction is defined by the Cα atoms of Lys60 and Phe67, while the position of Phe4 is
represented by the center of mass of the carbon atoms in its phenyl ring. Positive values of p indicate that the Phe4 side chain is solvent-exposed,
whereas negative values indicate that it is buried within the hydrophobic cavity. (C−E) Comparison of conformational sampling by AMS, EMD, and
GenAI ensembles alone. AMS and EMD sample the full spectrum of conformational heterogeneity, whereas the combined GenAI ensembles
predominantly sample a single state. (F) Superposition of crystal T4 lysozyme structure shown in dark gray with representative exposed/closed and
buried/closed conformations shown in magenta and blue, respectively. The comparison highlights conformational changes involving Ser44 and Phe4,
which contribute to the observed conformational heterogeneity.

challenging to access without explicit enhanced sampling to seed              EMD suffers from disconnected transition matrices even when
follow up unbiased simulations (Figure 2 and 3, see Figures S6                carefully seeded with short metadynamics runs specifically
and S7 in Supporting Information for error analysis). It is                   chosen to bridge open and closed states and create a fully
important to highlight that populations derived from AMS                      connected MSM (Figure S8 in Supporting Information).
converge robustly across choice of lag times and cluster centers                 In contrast, GenAI ensembles alone remained predominantly
(Figures S2 and S3 in Supporting Information). In contrast,                   trapped in the exposed/open state, failing to access the
                                                                          C                                            https://doi.org/10.1021/acs.jcim.6c02044
                                                                                                                       J. Chem. Inf. Model. XXXX, XXX, XXX−XXX


## PDF page 4

Journal of Chemical Information and Modeling                                              pubs.acs.org/jcim                                       Article




                                                                                                                                                                 Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026
Figure 3. MSM-weighted free-energy landscapes projected onto different collective variables compare conformational sampling by the AMS and EMD
approaches. The upper panels show equilibrium populations projected along the d1 and d2 collective variables, indicating that both AMS and EMD
sample the closed state of T4 lysozyme, defined by d1 < 2.5 nm. The black dotted line marks the closed−open boundary at d1 = 2.5 nm. The lower
panels show the projection of the locking coordinate p along d1, demonstrating that both AMS and EMD sample conformations with exposed and
buried Phenylalanine 4 side-chain states, corresponding to p > 0 and p < 0, respectively, across both closed and open T4 lysozyme conformations. Data
points from the GenAI ensembles are projected onto the physics-refined free-energy surfaces to assess the conformational coverage of each method.
Among the GenAI approaches, AF-cluster samples a substantially broader conformational landscape than the other methods.

transiently populated closed and buried states. Interestingly,                recover the conformational heterogeneity captured by the full
unbiased MD simulations (20 independent 1 μs simulations                      AMS protocol. However, it still sampled a broader free energy
initiated from the T4L X-ray crystal structure, PDB: 5LZM)                    surface when compared to unbiased MD simulations (Figures 4
sampled conformational transitions between the exposed/open                   and 5).
and buried/open states (Figure 4). This indicates that although                  To further validate AMS against experiment, I computed the
GenAI ensembles capture conformational heterogeneity along                    MSM-weighted smFRET distance distribution for the Ser44−
distance variables (d1 and d2), they alone cannot sample the                  Ile150 pair and compared it directly with experimental
buried/open state; suggesting that GenAI itself does not capture              measurements (Figure S1 in Supporting Information). AMS
the underlying physics of the conformational transitions in T4L.              recovered the transiently populated closed state in quantitative
   Projection of GenAI ensembles onto the d1 and d2 CV space                  agreement with experiment. This result is significant because the
revealed that AF-cluster provided substantially broader                       EMD simulations of Miller and co-workers13 were explicitly
conformational coverage than all other GenAI methods (Figure                  seeded with the objective of sampling the closed state using
3). This suggests that the enhanced sampling efficiency of AMS                enhanced sampling, yet AMS achieved comparable recovery of
is predominantly driven by the ability of AF-cluster to populate              this rare state starting from unbiased MD alone. The ability to
high-energy intermediate structures that serve as productive                  reproduce an experimentally observable transiently populated
seeds for subsequent MD simulation. To test this hypothesis                   conformation without any explicitly specific target state
directly, I repeated the AMS protocol with AF-cluster excluded                demonstrates that AMS can sample rare conformational events
from the initial ensemble. The resulting simulations failed to                that are inaccessible to GenAI methods alone.
                                                                         D                                            https://doi.org/10.1021/acs.jcim.6c02044
                                                                                                                      J. Chem. Inf. Model. XXXX, XXX, XXX−XXX


## PDF page 5

Journal of Chemical Information and Modeling                                           pubs.acs.org/jcim                                       Article




                                                                                                                                                              Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026
Figure 4. Free energy surfaces projected along d1 vs d2 and along d2 vs p (the locking coordinate) from a combined 20 μs unbiased molecular
dynamics data set (20 independent MD simulations, 1000 ns each), initiated from PDB structure 5LZM (following the approach of Miller et al.), are
compared against AMS round 1 alone (100 × 200 ns each = total 20 μs). This comparison highlights the efficiency of AMS over conventional unbiased
MD simulations starting from a single starting structure in capturing conformational heterogeneity in wild-type T4 lysozyme.

■    CONCLUSIONS
This work introduces T4L as a minimal community benchmark
                                                                           populations. AMS, by using GenAI ensembles as seeds rather
                                                                           than as end products, recovers the full conformational landscape
for evaluating GenAI methods that claim to capture conforma-               with populations that are quantitatively comparable to those
tional heterogeneity from sequence alone. T4L is uniquely                  from physics-based enhanced sampling. Two rounds of unbiased
suited to this role: its experimentally validated transient states,        MD simulation, initiated from GenAI derived starting
well characterized CVs, extensive structural coverage in the               structures, were sufficient to achieve this. In comparison,
Protein Data Bank and availability of enhanced molecular                   unbiased MD simulations of the same length as round 1 of
dynamics simulations data set collectively eliminate the                   AMS starting from the X-ray crystal structure of wild type fails to
confounding factors that have hampered fair comparisons in                 sample the closed state in T4L (Figure 4) Supporting
the field. The four-state classification framework presented here          Information. This is a practically important result: AMS requires
provides a transferable, physically interpretable scoring scheme           no knowledge of the target state and no enhanced sampling bias,
that can be applied consistently across any method that
                                                                           yet it matches the EMD’s population percentages for the
generates structural ensembles of T4L.
   The results presented here draw a clear boundary between                exposed/open, buried/open, and buried/closed states for wild
what GenAI can and cannot do in its current form in context of             type T4L; despite EMD being explicitly designed to find the
T4L. Majority of the GenAI methods alone reproduce the                     closed state. Further, the seeding strategy that combines all the
dominant ground state (except AF-cluster which samples                     conformational ensembles generated by different GenAI
multiple high energy transient states) but fail to sample                  algorithms alleviates the limitations of each one of them and
transiently populated closed state in T4L and their relative               provides a much wider distribution of conformations as initial
                                                                       E                                           https://doi.org/10.1021/acs.jcim.6c02044
                                                                                                                   J. Chem. Inf. Model. XXXX, XXX, XXX−XXX


## PDF page 6

Journal of Chemical Information and Modeling                                                 pubs.acs.org/jcim                                        Article




                                                                                                                                                                     Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026
Figure 5. MSM-weighted free energy surfaces projected along two sets of collective variables show that molecular simulations initiated from the GenAI
ensemble without the AF-cluster fail to sample the closed state. In contrast, AMS simulations that include the AF-cluster successfully capture this state,
as shown in Figures 2 and 3. To generate the simulation data set, 100 cluster centers were selected from a combined conformational ensemble
comprising AlphaFlow, ESMFlow, ConforFold, BioEmu, ConfRover, and rMSA-AF2 structures. For each cluster center, a 200 ns molecular dynamics
simulation was performed, yielding a total of 20 μs of simulation data.

seeds, which accelerates sampling when combined with physics-                   the closed state of T4L. This strategy of seeding the next round
based molecular simulations.                                                    of MD simulations from GenAI augmented molecular
   The success of AMS, and of all generative-AI-seeded                          simulations can be used in the same spirit as adaptive sampling
molecular simulation approaches such as AlphaFold-RAVE,25                       to explore the conformational landscape of biomolecules
AlphaFold-SFA,26 AlphaFold-MSM,27 and BioEmu augmented                          whenever the initial round of sampling fails to recover alternate
molecular simulations,28 depends heavily on the diversity of the                states or needs additional data to build fully connected MSM.
initial seed. However, the dependency of GenAI augmented                           Further, MSM generated from the EMD protocol developed
simulations on initial seeds has not been explicitly explored by                by Miller et al.13 failed to form a fully connected MSM, unlike
previous literatures. In this case, I have clearly shown that AMS               AMS round 1 (Figure S8 in Supporting Information). It is also
without structures from AF-cluster fails to sample the closed                   worth highlighting that EMD alone (termed limited sampling by
state of T4L. However, one encouraging factor is that even                      the authors) could not sample the minor state of T4L (closed
though these simulations failed to sample the closed state, they                state) in the context of the smFRET distribution (Figure 3A in
still sampled a wider conformational landscape than unbiased                    Miller et al.13). The authors therefore needed to run additional
MD simulations. One can perform K-center29 clustering on the                    adaptive sampling simulations using FAST10 to build a fully
combined simulation data to generate a diverse seeding                          connected MSM and reach reasonable agreement with the
ensemble for launching a second round of simulations. Figure                    experimental MSM. However, it is not possible to reproduce the
S9 in the Supporting Information shows the data points                          results of Miller et al. for a fair, direct comparison, because the
corresponding to K-center clustering on top of AMS simulations                  authors did not share the predicted FRET data needed for
run without AF-cluster, where one can see that short MD                         recalculation. In our protocol, AMS alone was able to sample this
simulations launched from these seeds would most likely sample                  alternate state.
                                                                            F                                             https://doi.org/10.1021/acs.jcim.6c02044
                                                                                                                          J. Chem. Inf. Model. XXXX, XXX, XXX−XXX


## PDF page 7

Journal of Chemical Information and Modeling                                         pubs.acs.org/jcim                                       Article

   It is also worth noting that experimental FRET efficiency and          local, not global dynamics. This limitation can be addressed by
simulated FRET efficiency are not expected to match exactly.              training any CV discovery algorithm12 of the user’s choice (such
Simulated FRET efficiency depends strongly on the number of               as PCA, TICA, SFA, or autoencoders) on the combined
cluster centers, the choice of feature sets used to build the MSM,        ensemble from GenAI methods, or by running simulations
and the underlying uncertainty introduced by the choice of force          shorter than AMS round 1 (∼50 ns each) and combining them
field and water model. Even so, it is encouraging that AMS was            to train such an algorithm. The resulting CV can then be used
able to sample the minor state corresponding to the closed                with OneOPES33 or a traditional metadynamics-like bias
population of T4L, without requiring the more involved                    potential to enhance sampling and capture conformational
workflow used by Miller et al.: unbiased MD, followed by                  heterogeneity across a wide range of biological systems.
metadynamics, followed by further unbiased MD from                           Overall framework of the AMS protocol is readily transferable
metadynamics-seeded trajectories, followed by FAST adaptive               for sampling conformational heterogeneity across different
sampling and finally connected all the data using MSM. Future             protein classes including kinases, proteases, GPCRs, TNF-




                                                                                                                                                            Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026
work is in progress to examine how the choice of force field,             superfamily members where protein dynamics modulates
water models and feature space affects the agreement with                 downstream signaling pathways implicated in human diseases.
experimental data from smFRET, NMR, and other biophysical                    Looking forward, T4L and the benchmarking framework
techniques.                                                               established here are well-positioned to evaluate the next
   It is worth mentioning that outside the two macrostate                 generation of hybrid methods. These include GenAI seeded
regions (open and closed) highlighted in Figure S1 (see                   weighted ensemble simulations,34 inference-time enhanced
Supporting Information), the AMS derived FRET efficiency                  sampling approaches such as Boltz-MetaDiffusion,35 and related
distribution shows regions of divergence from the experimental            methods that either combine GenAI with physics-based
smFRET signature. These regions correspond to transitional                sampling protocols or bias the generative process during
conformations that are not resolved as distinct free-energy               inference to access alternate states. The framework is equally
minima and are not the focus of the macrostate-level comparison           applicable to MSA subsampling strategies applied to newer
presented here. EMD does show a similar closed-state                      versions of foundation models such as AlphaFold336 and
population, as reported by Miller et al.; however, exact                  OpenFold3,37 where the impact of richer training data and
population weighted comparison of AMS vs EMD is not                       improved architecture on conformational diversity remains an
possible due to the lack of available raw data from EMD                   open question. As these methods mature, rigorous benchmark-
simulations.                                                              ing against experimentally validated populations along physi-
   AMS also compares favorably to existing simulation strategies          cally meaningful CVs will be essential to distinguish genuine
in terms of practicality and accessibility. In principle, AMS is a        advances in conformational sampling from improvements in
moderate-scale unbiased molecular dynamics simulation when                ground-state structure prediction. T4L, with its tractable size,
compared to Folding@Home.30 However, access to Folding@                   rich experimental data, and well-defined conformational
Home is restricted to a small number of researchers and requires          heterogeneity, makes it a minimal benchmark system for that
a specialized software interface to orchestrate the simulations.          purpose.
Enhanced sampling methods such as metadynamics can also
sample conformational heterogeneity; but requires setting up
numerous hyperparameters such as Gaussian height, width, bias
factor, and a reasonable choice of CV, each of which demands
                                                                          ■   METHODS
                                                                          Ensemble Generation
expert judgment and system-specific tuning.6−8 A poorly chosen
CV can also silently bias the resulting free energy landscape in          Structural ensembles of T4 lysozyme (T4L) were generated
ways that are difficult to detect after the fact. Weighted ensemble       from the wild-type T4L sequence using multiple GenAI based
methods are likewise large-scale and unbiased molecular                   approaches, as summarized in Table 1. The input amino acid
dynamics simulations but carry their own significant imple-               sequence used for all methods was:
mentation nuances. Among these approaches, AMS is the most
straightforward to launch and use it requires no additional               Table 1. GenAI Methods Used for T4L Ensemble
hyperparameter tuning or specialized expertise. It also does not          Generation, Number of Generated Structures, and
manipulate the underlying potential energy surface as enhanced            Corresponding Codebase or Implementation
sampling methods such as metadynamics,6 Gaussian accelerated
molecular dynamics (GaMD),31 or replica exchange32 do. Any                                 number of
                                                                              methods      structures           codebase/implementation
research group with access to an HPC cluster equipped with
only a few GPUs can perform AMS, making it one of the most                AF-cluster          132        https://github.com/HWaymentSteele/
                                                                                                           AF_Cluster
practical choices available for sampling conformational hetero-           AlphaFlow           500        https://github.com/bjing2016/alphaflow
geneity in biomolecules. As an example, completing Round 1 of                                              (model: AlphaFlow-MD)
AMS for T4L (100 independent simulations of 200 ns length)                ConforFold          600        https://github.com/strauchlab/
requires only about 10 days of wall time on a lightweight                                                  ConforFold
compute node equipped with three NVIDIA A100 GPUs (∼650                   ConfRover           500        https://github.com/ByteDance-Seed/
                                                                                                           ConfRover
ns/day per GPU). AMS also provides a straightforward way to
                                                                          ESMFlow             100        https://github.com/bjing2016/
gain intuition about a reasonable CV. A typical practice to build                                          alphaflow(model: ESMFlow-MD)
such intuition is to perform multiple short and independent               BioEmu              499        https://github.com/microsoft/bioemu
unbiased MD simulations from different starting points, but this          rMSA-AF2             80        Colabfold (MSA:8:16,
only works well if the starting points are already diverse. MD                                             num_recycles = 6)
simulations from a single starting structure remain trapped in            rMSA-AF2-           285        AlphaFold2_advanced_v2
local conformational minimum and yields a CV that reflects only            recyc                           (MSA:8:16,num_recycles = 3)

                                                                      G                                          https://doi.org/10.1021/acs.jcim.6c02044
                                                                                                                 J. Chem. Inf. Model. XXXX, XXX, XXX−XXX


## PDF page 8

Journal of Chemical Information and Modeling                                       pubs.acs.org/jcim                                     Article

   MNIFEMLRIDEGLRLKIYKDTEGYYTI-                                            The same distance-to-contact transformation was used at two
GIGHLLTKSPSLNAAKSELDKAIGRNCNGVITK-                                      stages of the workflow. First, it was applied to the combined
DEAEKLFNQDVDAAVRGILRNAKLKPVYDSLDAVRRCA-                                 GenAI ensemble to identify structurally diverse starting
LINMVFQMGETGVAGFTNSLRMLQQKRWDEAAVNLAKSR-                                conformations for molecular simulation. Second, after the
WYNQTPNRAKRVITTFRTGTWDAYKNL                                             unbiased molecular dynamics simulations were completed, the
   The generated ensembles included both multiple-sequence-             resulting trajectories were processed using the same trans-
alignment-based approaches and generative models trained to             formed-distance representation to identify conformations for
produce conformationally diverse protein structures. For each           the physics-refined ensemble. Thus, both the initial GenAI
method, the number of generated structures and the                      predicted structures and the MD-derived conformations were
corresponding codebase or implementation are listed in Table            analyzed in a common feature space.
1. All structures generated across these methods were pooled               For each Cα−Cα pair, the transformed contact values were
into a combined GenAI ensemble for subsequent transformed-              evaluated across the relevant structural data set, either the




                                                                                                                                                        Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026
distance analysis, dimensionality reduction, and clustering.            pooled GenAI ensemble or the postprocessed simulation
Definitions of Collective Variables                                     trajectories. Contacts were retained only if they showed
                                                                        evidence of both formation and disruption, according to the
The opening and closing motion of T4 lysozyme was
                                                                        criterion:
characterized using the Cα−Cα distance between Ser44 and
Ile150, denoted as d1. Conformations with d1 < 2.5 nm were                 min(S) <0.4andmax(S)>0.6                                             (3)
classified as closed, whereas conformations with d1 > 2.5 nm
were classified as open. A second Cα−Cα distance, measured                 This filtering step removes distance pairs that remain
between Glu22 and Gln141 and denoted as d2, was used as an              essentially unchanged, either always formed or always broken,
orthogonal projection coordinate to describe hinge-domain               and keeps only contacts that report meaningful conformational
motion, following the collective-variable definition proposed by        rearrangements. In this representation, values of S(r) ≥ 0.6
Abou-Hatab and Abrams.14                                                correspond to formed contacts, values of S(r) ≤ 0.4 correspond
   The solvent exposure of Phe4 was quantified using the locking        to broken contacts, and intermediate values describe partially
coordinate, p. For each trajectory frame, p was calculated by           formed or fluctuating contacts.
projecting the vector from the Cα atom of Phe67 to the center of           The filtered set of transformed distance features was then used
the Phe4 phenyl ring onto the vector connecting the Cα atoms            for dimensionality reduction with Slow Feature Analysis (SFA),
of Lys60 and Phe67. The center of the Phe4 phenyl ring was              as introduced for biomolecular simulation data by Vats et al.26
defined as the geometric center of the CG, CD1, CD2, CE1,               SFA identifies linear combinations of input features that change
CE2, and CZ carbon atoms. The locking coordinate was                    slowly over time, thereby emphasizing collective motions
computed as                                                             associated with long-time scale conformational rearrangements.
                                                                        For an input signal c(t), SFA generates output coordinates yk(t)
         d 60,67·d67,4                                                  = gk(c(t)) by minimizing temporal variation:
   p=
           |d60,67|2                                         (1)             yk = yk2                                                           (4)
where d60,67 is the vector from the Lys60 Cα atom to the Phe67             Applied to the transformed Cα−Cα contact features, SFA
Cα atom, and d67,4 is the vector from the Phe67 Cα atom to the          identified the slowest collective distance patterns that
center of the Phe4 phenyl ring. Positive values of p (p > 0)            distinguish conformationally heterogeneous regions of T4
indicate that the Phe4 side chain is solvent-exposed, whereas           lysozyme. The first two slow features were used as the reduced
negative values indicate that the side chain is buried (p < 0)          feature space for K-center clustering.29 Cluster centers (k = 100)
within the hydrophobic cavity.                                          selected from the combined GenAI ensemble were saved as PDB
Feature Selection, Dimensionality Reduction and                         structures and used as starting points for the first round of
Clustering                                                              molecular dynamics simulations. The same procedure was
To construct a distance-based representation of conformational          subsequently applied during postprocessing of the simulation
variability, structures generated by the different GenAI methods        trajectories to select the physics-refined ensemble for the next
were first pooled into a single all-atom ensemble. For every            round of simulations. SFA and K-center clustering were
structure in this combined ensemble, all Cα−Cα pairwise                 performed using the MDML software package (GitHub:
distances were converted into continuous contact-like variables         https://github.com/svats73/mdml/tree/main)
using a smooth switching function, following Bhakat et al.38            Molecular Dynamics Simulations
                 1                                                      Each selected structure from starting ensemble or physics-
   S(r ) =                 n
                 i r y                                                  refined ensemble was prepared using the tleap module in
           1 + jjj r zzz                                                Amber2022,39,40 following the general simulation protocol
                 k decay {                                   (2)
                                                                        described by Meller et al.27 Protein atoms were parametrized
Here, r denotes the Cα−Cα distance, rdecay defines the distance         with the AMBER f f14SB41 force field. Each system was
scale over which the contact changes from formed to broken,             neutralized with the appropriate counterions and solvated in a
and n controls the steepness of this transition. Distances much         truncated-octahedron box of TIP3P water molecules, with a
shorter than rdecay produce values close to 1, corresponding to a       minimum distance of 10 Å between any protein atom and the
formed contact, whereas distances much longer than rdecay               edge of the simulation box.
produce values close to 0, corresponding to a broken contact.              Energy minimization was carried out in two steps. First,
This transformation replaces raw distances with a smooth and            solvent molecules and ions were minimized while harmonic
noise-tolerant measure of contact strength. I used rdecay = 0.90        restraints were applied to the protein atoms using a force
nm and n = 6.                                                           constant of 100 kcal mol−1 Å−2. This was followed by an
                                                                    H                                        https://doi.org/10.1021/acs.jcim.6c02044
                                                                                                             J. Chem. Inf. Model. XXXX, XXX, XXX−XXX


## PDF page 9

Journal of Chemical Information and Modeling                                         pubs.acs.org/jcim                                     Article

unrestrained minimization of the full solvated system. The
resulting Amber topology and coordinate files were then
                                                                          ■   ASSOCIATED CONTENT
                                                                          Data Availability Statement
converted to GROMACS format using Acpype,42 and all                       GenAI ensembles, closed states of T4L and codes to calculate
subsequent equilibration and production simulations were                  the distance, RMSD and locking coordinate can be accessed
performed using GROMACS 2022.43                                           here: 10.5281/zenodo.20111229, https://osf.io/jcxbs/
   Systems were gradually heated from 0 to 300 K over 500 ps in           overview?view_only=2c9e9b57afe84521bf80950412f0747a
the NVT ensemble while applying positional restraints to                  (OSF entry with Dropbox link which contains RMSD, distance
backbone heavy atoms with a force constant of 500 kJ mol−1                as well as smFRET analyses and corresponding metadata) and
nm−2. After heating, each system was equilibrated for 200 ps in           https://github.com/sbhakat/Gen-AI-t4l-bechmarking
the NPT ensemble at 300 K and 1 bar without positional                    *
                                                                          sı Supporting Information
restraints. Temperature was maintained using the velocity-                The Supporting Information is available free of charge at
rescale thermostat, and pressure was controlled using the




                                                                                                                                                          Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026
                                                                          https://pubs.acs.org/doi/10.1021/acs.jcim.6c02044.
Parrinello−Rahman barostat.44                                                   Conformational state definitions and comparison with
   Unbiased production simulations were then performed in the                   experiment: MSM-weighted FRET efficiency distribu-
NPT ensemble using a 2 fs integration time step. Nonbonded                      tions from AMS benchmarked against experimental
interactions were treated with a 1.0 nm cutoff, long-range                      smFRET, showing sampling of both the open and closed
electrostatics were calculated using the particle-mesh Ewald                    states of T4 lysozyme, including the rare closed-state
method,45 and bonds involving hydrogen atoms were con-                          population previously reported only via EMD simulations
strained using the LINCS46 algorithm. Production trajectories                   (Figure S1); convergence and robustness analysis: lag-
were initiated from the SFA selected cluster centers and ran for                time convergence and MSM-weighted free-energy
200 ns each, with coordinates saved every 10 ps.                                surfaces for AMS and EMD, equilibrium population
                                                                                stability across cluster number (K) and feature choice
Enhanced Molecular Dynamics Simulations
                                                                                (RMSD-based vs TICA-based), Bayesian MSM-weighted
The molecular dynamics simulations used in this study were                      equilibrium populations with 95% confidence intervals for
adapted from Miller et al.13 Briefly, the data set comprises a 5 μs             the four conformational states in both AMS and EMD,
unbiased MD trajectory, which did not sample the open-to-                       and transition count-matrix connectivity analysis compar-
closed conformational transition. To drive the transition, the                  ing network connectivity between AMS and EMD
authors applied a metadynamics bias along the Cα−Cα distance                    (Figures S2−S8); and conformational sampling diversity
between Ser44 and Ile150, extracted snapshots along the                         and seeding strategy: K-center clustering of AMS-sampled
                                                                                conformations on the free-energy surface, illustrating the
resulting free-energy pathway, and launched short unbiased MD
                                                                                diversity of states used to seed round 2 of AMS sampling
simulations from each structural snapshot. Rather than analyzing                of the closed state (Figure S9) (PDF)
the metadynamics trajectories directly, I combined the primary 5
μs unbiased trajectory with a series of short, unbiased
simulations seeded along the biased pathway, yielding a total
simulation time of 27.6 μs. This combined data set included 17
                                                                          ■   AUTHOR INFORMATION
                                                                          Corresponding Author
simulations (1 μs each) initiated from alternate structures and             Soumendranath Bhakat − AlloTec Bio Inc., St. Louis, Missouri
56 simulations (0.1 μs each) initiated from cluster centers                   63116, United States; orcid.org/0000-0002-1184-9259;
extracted from the unbiased trajectory.                                       Email: bhakatsoumendranath@gmail.com, sbhakat@
                                                                              allotec.bio
Markov State Model
                                                                          Complete contact information is available at:
Markov state models (MSMs) were constructed using the                     https://pubs.acs.org/10.1021/acs.jcim.6c02044
PyEMMA47 package with RMSD-based featurization of both
AMS and EMD trajectories. K-means clustering (K = 200) was                Author Contributions
employed to discretize conformational space, and state                    S.B. designed the study, performed all calculations and analyses,
populations were computed across multiple lag times to assess             and wrote the manuscript.
convergence and compare the relative equilibrium distributions            Notes
of AMS and EMD ensembles (Figures S2 and S5 in Supporting                 The author declares no competing financial interest.
Information). Figure S3 and S4 in the Supporting Information
shows the populations of T4L conformational states as a
function of the number of cluster centers, demonstrating the
                                                                          ■   ACKNOWLEDGMENTS
                                                                          The author thanks Justin J. Miller of the University of
apparent convergence of the AMS simulations.                              Pennsylvania for performing the smFRET calculations and
smFRET Prediction                                                         providing the dataset corresponding to the EMD simulations.
                                                                          Further acknowledgment goes to Prof. Eva M. Strauch and Dr.
smFRET prediction was carried out using Enspara48 software
                                                                          Raulia Syrlybaeva of Washington University in St. Louis for
package (https://enspara.readthedocs.io/en/latest/smFRET.                 providing the ConforFold ensemble, and to Shray Vats of
html). Trajectories from AMS were featurized by transformed               Boston University for providing the ConfRover ensemble.
distances followed by SFA (as described in “Feature selection,
dimensionality reduction and clustering” subsection) followed
by K-means clustering with k = 500. smFRET was predicted
                                                                          ■   REFERENCES
                                                                           (1) Aranganathan, A.; Gu, X.; Wang, D.; Vani, B. P.; Tiwary, P.
using the protocol described by Miller et al.13                           Modeling Boltzmann-weighted structural ensembles of proteins using

                                                                      I                                        https://doi.org/10.1021/acs.jcim.6c02044
                                                                                                               J. Chem. Inf. Model. XXXX, XXX, XXX−XXX


## PDF page 10

Journal of Chemical Information and Modeling                                                  pubs.acs.org/jcim                                         Article

artificial intelligence−based methods. Curr. Opin. Struct. Biol. 2025, 91,          (25) Vani, B. P.; Aranganathan, A.; Wang, D.; Tiwary, P. AlphaFold2-
No. 103000.                                                                       RAVE: From Sequence to Boltzmann Ranking. J. Chem. Theory
 (2) Kornev, A. P.; Taylor, S. S. Dynamics-Driven Allostery in Protein            Comput. 2023, 19, 4351−4354.
Kinases. Trends Biochem. Sci. 2015, 40, 628−647.                                    (26) Vats, S.; Bobrovs, R.; Söderhjelm, P.; Bhakat, S. AlphaFold-SFA:
 (3) Latorraca, N. R.; Venkatakrishnan, A. J.; Dror, R. O. GPCR                   Accelerated sampling of cryptic pocket opening, protein-ligand binding
Dynamics: Structures in Motion. Chem. Rev. 2017, 117, 139−155.                    and allostery by AlphaFold, slow feature analysis and metadynamics.
 (4) Livesay, D. R. Protein dynamics: dancing on an ever-changing free            PLoS One 2024, 19, No. e0307226.
energy stage. Curr. Opin. Pharmacol. 2010, 10, 706−708,                             (27) Meller, A.; Bhakat, S.; Solieva, S.; Bowman, G. R. Accelerating
DOI: 10.1016/j.coph.2010.09.015.                                                  Cryptic Pocket Discovery Using AlphaFold. J. Chem. Theory Comput.
 (5) Guo, J.; Zhou, H.-X. Protein Allostery and Conformational                    2023, 19, 4355−4363.
Dynamics. Chem. Rev. 2016, 116, 6503−6515.                                          (28) Bhakat, S.; Strauch, E.-M. Accelerated Sampling of Protein
 (6) Barducci, A.; Bonomi, M.; Parrinello, M. Metadynamics. WIREs                 Dynamics Using BioEmu-Augmented Molecular Simulation. J. Chem.
Computational Molecular Science 2011, 1, 826−843.                                 Inf. Model. 2026, 66, 7168−7178.




                                                                                                                                                                       Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026
 (7) Barducci, A.; Bussi, G.; Parrinello, M. Well-Tempered                          (29) Gonzalez, T. F. Clustering to minimize the maximum intercluster
Metadynamics: A Smoothly Converging and Tunable Free-Energy                       distance. Theor. Comput. Sci. 1985, 38, 293−306.
Method. Phys. Rev. Lett. 2008, 100, 20603.                                          (30) Voelz, V. A.; Pande, V. S.; Bowman, G. R. Folding@home:
 (8) Tiwary, P.; Parrinello, M. From Metadynamics to Dynamics. Phys.              Achievements from over 20 years of citizen science herald the exascale
Rev. Lett. 2013, 111, No. 230602.                                                 era. Biophys. J. 2023, 122, 2852−2863.
 (9) Bussi, G.; Laio, A. Using metadynamics to explore complex free-                (31) Miao, Y.; Feher, V. A.; McCammon, J. A. Gaussian Accelerated
energy landscapes. Nat. Rev. Phys. 2020, 2, 200−212.                              Molecular Dynamics: Unconstrained Enhanced Sampling and Free
 (10) Zimmerman, M. I.; Bowman, G. R. FAST Conformational                         Energy Calculation. J. Chem. Theory Comput. 2015, 11, 3584−3595.
Searches by Balancing Exploration/Exploitation Trade-Offs. J. Chem.                 (32) Qi, R.; Wei, G.; Ma, B.; Nussinov, R. Replica Exchange Molecular
Theory Comput. 2015, 11, 5747−5757.                                               Dynamics: A Practical Application Protocol with Solutions to Common
 (11) Liu, P.; Kim, B.; Friesner, R. A.; Berne, B. J. Replica exchange with       Problems and a Peptide Aggregation and Self-Assembly Example BT -
solute tempering: A method for sampling biological systems in explicit            Peptide Self-Assembly: Methods and Protocols; Nilsson, B. L.; Doran, T.
water. Proc. Natl. Acad. Sci. U.S.A. 2005, 102, 13749−13754.                      M., Eds.; Springer: New York, 2018; pp 101−119.
 (12) Bhakat, S. Collective variable discovery in the age of machine                (33) Rizzi, V.; Aureli, S.; Ansari, N.; Gervasio, F. L. OneOPES, a
learning: reality, hype and everything in between. RSC Adv. 2022, 12,             Combined Enhanced Sampling Method to Rule Them All. J. Chem.
25010−25024.                                                                      Theory Comput. 2023, 19, 5731−5742.
 (13) Miller, J. J.; Mallimadugula, U. L.; Zimmerman, M. I.; et al.                 (34) Otten, L.; Leung, J. M.; Chong, L. T.; Zuckerman, D. M.
Accounting for Fast vs Slow Exchange in Single Molecule FRET                      Rectifying AI-generated protein structure ensembles for equilibrium
Experiments Reveals Hidden Conformational States. J. Chem. Theory                 using physics-based computations. bioRxiv 2026,
Comput. 2024, 20, 10339−10349.                                                    No. 2026.03.24.714034.
 (14) Abou-Hatab, S.; Abrams, C. F. Minimal Collective Variables for                (35) Lam, H. Y. I.; et al. Metadiffusion: inference-time meta-energy
Conformational Transitions in Steered and Temperature-Accelerated                 biasing of biomolecular diffusion models. bioRxiv 2026,
                                                                                  No. 2026.02.10.704873.
MD Simulations: A T4 Lysozyme Case Study. J. Phys. Chem. B 2025,
                                                                                    (36) Kalakoti, Y.; Wallner, B.AFsample3: Generating and selecting
129, 5176−5188.
                                                                                  multiple conformational states with Alphafold3 bioRxiv
 (15) Ernst, M.; Wolf, S.; Stock, G. Identification and Validation of
                                                                                  20262026.01.16.699904.
Reaction Coordinates Describing Protein Functional Motion: Hier-
                                                                                    (37) Lee, M., et al., ConforNets: Latents-Based Conformational
archical Dynamics of T4 Lysozyme. J. Chem. Theory Comput. 2017, 13,
                                                                                  Control in OpenFold3, 2026, arXiv:2604.18559. arXiv.org e-Print
5076−5088.                                                                        archive https://arxiv.org/abs/2604.18559.
 (16) Wayment-Steele, H. K.; Ojoawo, A.; Otten, R.; et al. Predicting               (38) Bhakat, S.; Vats, S.; Mardt, A.; Degterev, A. Generalizable Protein
multiple conformations via sequence clustering and AlphaFold2.                    Dynamics in Kinases: Physics is the key. bioRxiv 2025,
Nature 2024, 625, 832−839.                                                        No. 2025.03.06.641878.
 (17) Jumper, J.; Evans, R.; Pritzel, A.; et al. Highly accurate protein            (39) Case, D. A.et al. Amber 2022; University of California: San
structure prediction with AlphaFold. Nature 2021, 596, 583−589.                   Francisco, 2022.
 (18) del Alamo, D.; Sala, D.; Mchaourab, H. S.; Meiler, J. Sampling                (40) Salomon-Ferrer, R.; Case, D. A.; Walker, R. C. An overview of the
alternative conformational states of transporters and receptors with              Amber biomolecular simulation package. WIREs Computational
AlphaFold2. eLife 2022, 11, No. e75751.                                           Molecular Sci. 2013, 3, 198−210.
 (19) Syrlybaeva, R.; Strauch, E.-M. ConforFold recovers alternative                (41) Maier, J. A.; Martinez, C.; Kasavajhala, K.; et al. ff14SB:
protein conformations beyond MSA subsampling. Protein Sci. 2026, 35,              Improving the Accuracy of Protein Side Chain and Backbone
No. e70564.                                                                       Parameters from ff99SB. J. Chem. Theory Comput. 2015, 11, 3696−
 (20) Jing, B.; Berger, B.; Jaakkola, T. AlphaFold Meets Flow Matching            3713.
for Generating Protein Ensembles, 2024, arXiv:2402.04845. arXiv.org                 (42) Sousa da Silva, A. W.; Vranken, W. F. ACPYPE - AnteChamber
e-Print archive https://arxiv.org/abs/2402.04845.                                 PYthon Parser interfacE. BMC Res. Notes 2012, 5, 367.
 (21) Shen, Y.et al., ConfRover: Simultaneous Modeling of Protein                   (43) Abraham, M. J.; Murtola, T.; Schulz, R.; et al. GROMACS: High
Conformation and Dynamics via Autoregression. 2025,                               performance molecular simulations through multi-level parallelism
arXiv:2505.17478. arXiv.org e-Print archive https://arxiv.org/abs/                from laptops to supercomputers. SoftwareX 2015, 1−2, 19−25.
2505.17478.                                                                         (44) Parrinello, M.; Rahman, A. Polymorphic transitions in single
 (22) Lewis, S.; Hempel, T.; Jiménez-Luna, J.; et al. Scalable emulation          crystals: A new molecular dynamics method. J. Appl. Phys. 1981, 52,
of protein equilibrium ensembles with generative deep learning. Science           7182−7190.
2025, 389, No. eadv9817.                                                            (45) Darden, T.; York, D.; Pedersen, L. Particle mesh Ewald: An N·
 (23) Husic, B. E.; Pande, V. S. Markov State Models: From an Art to a            log(N) method for Ewald sums in large systems. J. Chem. Phys. 1993,
Science. J. Am. Chem. Soc. 2018, 140, 2386−2396.                                  98, 10089−10092.
 (24) Pande, V. S.; Beauchamp, K.; Bowman, G. R. Everything you                     (46) Hess, B.; Bekker, H.; Berendsen, H. J. C.; Fraaije, J. G. E. M.
wanted to know about Markov State Models but were afraid to ask.                  LINCS: A linear constraint solver for molecular simulations. J. Comput.
Methods 2010, 52, 99−105.                                                         Chem. 1997, 18, 1463−1472.

                                                                              J                                             https://doi.org/10.1021/acs.jcim.6c02044
                                                                                                                            J. Chem. Inf. Model. XXXX, XXX, XXX−XXX


## PDF page 11

Journal of Chemical Information and Modeling                             pubs.acs.org/jcim                               Article

 (47) Scherer, M. K.; Trendelkamp-Schroer, B.; Paul, F.; et al.
PyEMMA 2: A Software Package for Estimation, Validation, and
Analysis of Markov Models. J. Chem. Theory Comput. 2015, 11, 5525−
5542.
 (48) Porter, J. R.; Zimmerman, M. I.; Bowman, G. R. Enspara:
Modeling molecular ensembles with scalable data structures and
parallel computing. J. Chem. Phys. 2019, 150, 44108.




                                                                                                                                        Downloaded from pubs.​acs.​org/​jcisd8/​article-pdf/​doi/​10.​1021/​acs.​jcim.​6c02044/​68280815/​acs.​jcim.​6c02044.​pdf by FUDAN UNIV user on 08 September 2026




                                                                     K                       https://doi.org/10.1021/acs.jcim.6c02044
                                                                                             J. Chem. Inf. Model. XXXX, XXX, XXX−XXX
