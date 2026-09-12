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
