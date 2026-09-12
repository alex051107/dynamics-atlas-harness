# Small-Angle X-ray Scattering Signatures of Conformational Heterogeneity and Homogeneity of Disordered Protein Ensembles

**Authors:** Jianhui Song, Jichen Li, Hue Sun Chan
**Year:** 2021
**Venue:** Journal of Physical Chemistry B (OA copy via arXiv preprint)
**DOI:** 10.1021/acs.jpcb.1c02453
**Source PDF URL:** https://arxiv.org/pdf/2105.13427
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

June 9, 2021


                                                   Small-Angle X-Ray Scattering Signatures of
                                                       Conformational Heterogeneity and
                                                  Homogeneity of Disordered Protein Ensembles


arXiv:2105.13427v2 [q-bio.BM] 9 Jun 2021
                                                            Jianhui SONG1,∗ , Jichen LI1 and Hue Sun CHAN2,∗
                                                        School of Polymer Science and Engineering, Qingdao University of
                                                     Science and Technology, 53 Zhengzhou Road, Qingdao 266042, China;
                                                               Department of Biochemistry, University of Toronto,
                                                                      Toronto, Ontario M5S 1A8, Canada


                                           ∗
                                               Corresponding authors.
                                               Hue Sun Chan. E-mail: chan@arrhenius.med.utoronto.ca
                                               Jianhui Song. E-mail: jhsong@qust.edu.cn


                                           ——————————————————————————————————————–

                                                                                +
                                                                           (εp)ij       I(q)

                                                                              P(r)        q2I(q)


                                                                            TOC Graphics



Abstract

   An accurate account of disordered protein conformations is of central importance to
deciphering the physico-chemical basis of biological functions of intrinsically disordered
proteins and the folding-unfolding energetics of globular proteins. Physically, disordered
ensembles of non-homopolymeric polypeptides are expected to be heterogeneous; i.e.,
they should differ from those homogeneous ensembles of homopolymers that harbor an
essentially unique relationship between average values of end-to-end distance REE and
radius of gyration Rg . It was posited recently, however, that small-angle X-ray scattering
(SAXS) data on conformational dimensions of disordered proteins can be rationalized
almost exclusively by homopolymer ensembles. Assessing this perspective, chain-model
simulations are used to evaluate the discriminatory power of SAXS-determined molecular
form factors (MFFs) with regard to homogeneous versus heterogeneous ensembles.
The general approach adopted here is not bound by any assumption about ensemble
encodability, in that the postulated heterogeneous ensembles we evaluated are not
restricted to those entailed by simple interaction schemes. Our analysis of MFFs for
certain heterogeneous ensembles with more narrowly distributed REE and Rg indicates
that while they deviates from MFFs of homogeneous ensembles, the differences can
be rather small. Remarkably, some heterogeneous ensembles with asphericity and
REE drastically different from those of homogeneous ensembles can nonetheless exhibit
practically identical MFFs, demonstrating that SAXS MFFs do not afford unique
characterizations of basic properties of conformational ensembles in general. In other
words, the ensemble to MFF mapping is practically many-to-one and likely non-smooth.
Heteropolymeric variations of the REE –Rg relationship were further showcased using an
analytical perturbation theory developed here for flexible heteropolymers. Ramifications
of our findings for interpretation of experimental data are discussed.



INTRODUCTION

    A detailed characterization of the conformational properties of disordered protein states
is essential for many areas of biophysical and biomedical research. These include, but are
not limited to, the thermodynamic balance between folded and unfolded states of globular
proteins1–13 and the relationships between myriad biological functions of the increasing
repertoire of intrinsically disordered proteins (IDPs) and the behaviors of their conforma-
tional ensembles.14–24 One basic property of disordered conformational ensembles is their
extent in space. This property, often referred to as conformational dimensions, is of central
importance to protein science because it bears on the very nature of the folding/unfolding
cooperativity of globular proteins25–31 as well as, for example, the spatial ranges and other
configurational features of biomolecular interactions involving IDPs32–34 including those
of highly disordered “fuzzy” dynamic IDP complexes.35–40 Recent advances in the studies
of biomolecular condensates41–43 suggest further that conformational dimensions of indi-
vidual IDP molecules may serve as an indicator of the propensity of the IDP to undergo
liquid-liquid phase separation.40,44–47 Indeed, despite the low-spatial-resolution informa-
tion they provide directly, measures of conformational dimensions of disordered protein
states such as end-to-end distance and radius of gyration (denoted, respectively, as REE
and Rg hereafter) offer fundamental insights into the microscopic physical interactions
underlying protein behaviors48,49 and thus provide critical assessments of the extent to
which current molecular dynamics force fields are adequate for capturing the physics of
these interactions.50–55
    Small-angle X-ray scattering (SAXS) is a commonly utilized technique in
biophysics56–58 to quantify conformational dimensions of disordered proteins by measur-
ing Rg and related ensemble-averaged spatial properties.1,3,6,7,59–65 Because SAXS takes
into account simultaneously many positions along the entire chain molecule, SAXS af-
fords information complementary to techniques such as Förster resonance energy trans-
fer (FRET)9,10,16,20,66–72,72,73 that probe only one or a few relative positions at a time.
Nonetheless, since scattering intensities are averaged over different chain conformations
in an ensemble, SAXS data do not provide detailed spatial information of individual con-
formations. Therefore, models and assumptions often need to be invoked to relate SAXS
data to putative conformational ensembles that likely—though not necessarily—underlie
the experimental data. Recently, the generality of some of these assumptions, or lack
thereof, has been brought into a sharper focus. One of the reasons is that for several
disordered protein states, the Rg s extracted from SAXS using Guinier analysis disagree
significantly with the Rg values inferred from single-molecule FRET (smFRET) data by
assuming that the underlying conformational distribution is Gaussian.59,62,74–76
    As we76,77 and others78,79 have noted, besides improving the treatment of excluded



volume in the underlying baseline homopolymer chain model80–83 used in SAXS and sm-
FRET data analysis84,85 [see, e.g., Eq. (5.6) of ref. 83], the apparent mismatches between
SAXS- and smFRET-inferred Rg s should be fundamentally reconcilable by recognizing
that conformational ensembles of proteins are heterogeneous77,86–89 in that they do not
necessarily resemble those of homopolymers, because proteins are heteropolymeric se-
quences of different amino acid residues. Simply put, proteins are not homopolymers.
Therefore, the relationship between their average REE and their average Rg can differ
from that of homopolymers, i.e., the relation can be different from that posited by Gaus-
sian chain and other homopolymeric models.76,77 It is possible, then, for heterogeneous
conformational ensembles to embody both a smFRET-inferred average REE and a SAXS-
determined average Rg that are not coupled in the same way as for homopolymers.76–78
This conceptual framework has been applied to rationalize experimental data with ap-
parent success.76,78,79,90–92
   In this context, it is notable that recent experimental developments emphasize that
one should be able to glean more structural information about disordered protein ensem-
bles from SAXS data than merely extracting the mean square radius of gyration, hRg2 i,
by using Guinier analysis, which relies on scattering intensity, I(q), at small q values,
with q = |q| being the magnitude of the scattering vector q. In contrast, some of the
recent SAXS studies of disordered protein ensembles consider Kratky plots, or molecular
form factors (MFFs), over a substantially wider range of q (refs. 93–96). Logically, the
more enriched information provided by MFFs, namely the I(q) at larger qs, is expected
to impose more experimental constraints on putative, theoretically constructed conforma-
tional ensembles beyond merely requiring them to have a given hRg2 i. Accordingly, this
recognition raises basic questions as to whether theoretical/computational heterogeneous
conformational ensembles constructed to satisfy a given hRg2 i and a given hREE   i remain
viable when MFFs are taken into account; that is, whether those putative heterogeneous
ensembles are also consistent with the additional information afforded by the larger-q
behaviors of experimental MFFs. To address this and related questions, it should be
recognized first that although MFFs provide more structural information on disordered
protein ensembles than Guinier analysis, MFFs still involve extensive averaging over in-
dividual conformations and therefore an MFF by itself is far from being able to uniquely
define a disordered conformational ensemble. With these considerations in mind, we seek
here to clarify the information content of SAXS-determined MFFs by investigating the
compatibility of various putative conformational ensembles with given MFFs. As will be
apparent below, this delineation is useful toward establishing a more rigorous perimeter
for interpreting SAXS-determined MFFs of disordered proteins in terms of heterogeneous
conformational ensembles.
   To this end, we use explicit-chain simulations of a coarse-grained polypeptide model76



to construct extensive sets of different heterogeneous ensembles with properties selected
systematically for the insights they would provide. We then compare their MFFs with
those of full ensembles of homopolymers embodying varying degrees of uniform intrachain
attractive or repulsive interactions, paying special attention to identify and evaluate sce-
narios in which the MFFs of heterogeneous and homogeneous ensembles are highly simi-
lar. Building on prior advances, we commence this effort with a survey of the (Rg , REE )
subensembles introduced previously to address the apparent SAXS–smFRET mismatches
in Rg measurement.76,77,97 Each of these subensembles is individually a heterogenoues con-
formational ensemble because it is defined to be a small part of a homogeneous ensemble
and therefore not a homogeneous ensemble by itself. Interestingly, while the MFFs of dif-
ferent subensembles sharing the same Rg with the hRg2 i1/2 of the homogeneous ensemble
differ among themselves because the MFF depends on the subensemble’s REE , the MFFs
of some subensembles are quite similar to the MFF of the full homogeneous ensemble.
    Besides the (Rg , REE ) subensembles, other heterogeneous ensembles with more diverse
conformations, i.e., not limited to a very narrow range of Rg , REE values, are also
assessed. Motivated partly by experimental evidence suggesting that disordered protein
ensembles are heterogeneous in a sequence-sensitive manner12,92 (sometimes manifested
by peculiar forms of the inferred Rg distribution17 ) despite their homopolymer-like overall
average Rg values,79,98 we study several physically plausible, conformationally diverse
heterogeneous ensembles with narrower distributions of Rg than that of a homogeneous
ensemble. Quite surprisingly, these heterogeneous ensembles nonetheless lead to MFFs
very similar to that of the corresponding homogeneous ensemble. Indeed, we even come
across other mathematically intriguing cases where heterogeneous ensembles drastically
different from homopolymers yet possess MFFs that are essentially identical to MFFs of
homopolymers. These comparisons indicate that the MFFs of homogeneous ensembles
and some heterogeneous ensembles can be practically indistinguishable when experimen-
tal uncertainties are allowed for, underscoring the desirability of employing additional
experiment techniques complementary to SAXS to better characterize disordered protein
ensembles.78,79,92 Aiming for rudimentary insights into the complex sequence-ensemble
relationship of heteropolymeric disordered proteins, we have also developed an extension
of theoretical perturbative approaches99–109 to calculate hRg2 i1/2 , hREE2
                                                                             i1/2 , scattering
intensity I(q), and MFF(qhRg2 i1/2 ) for heteropolymers. Predictions of this analytical
formulation allow for a preliminary understanding of how sequence-specific interactions
may encode heterogeneous ensembles that share the same hRg2 i1/2 but differ in other
aspects of their conformational distributions such as their root-mean-square end-to-end
distance hREE   i1/2 . Details of these findings are provided below.



MODELS AND METHODS

    The present coarse-grained Cα protein model (one bead per monomer, or per residue)
and the sampling algorithm are based on the formulation used in our previous investi-
gations of smFRET interpretation for disordered proteins.76,77 As before, a polypeptide
chain is modeled as a chain of n beads labeled by i = 1, 2, . . . , n at position Ri , with
Cα –Cα virtual bond length b = |ri,i+1 | ≡ |Ri+1 − Ri | = 3.8 Å between connected beads.
The bond-angle potential energy Ubond ({r}) = n−1                             2
                                                          P
                                                             i=2 θ (θi − θ0 ) , where θ = 10.0kB T ,
θi = cos−1 (ri,i−1 · ri,i+1 /b2 ) is the virtual bond angle at bead i, θ0 = 106.3◦ is the refer-
ence bond angle corresponding to the most populated virtual bond angle in the Protein
Data Bank,110 kB is Boltzmann constant, and T is absolute temperature. The potential
energy for excluded volume is given by USAW ({r}) = (1/2) ni=1 nj=1 (USAW )ij (rij ) where
                                                                      P P

“SAW” stands for self-avoiding walk and (USAW )ij ≡ ex (Rhc /rij )12 . In this expression,
rij ≡ |Rj −Ri | is the distance between beads i and j, and ex = 1.0kB T is the self-avoiding
excluded-volume repulsion strength used in our model. As in many simulation studies of
protein folding27 and in most of the cases we considered in refs. 76 and 77, a hard-core re-
pulsion distance Rhc = 4.0 Å is adopted. In addition to the non-bonded excluded-volume
repulsive term, here we consider also homopolymeric, uniform intrachain non-bonded at-
tractive or repulsive interactions given by Up (p , r0 ; {r}) = ni=1 nj=i+3 (Up )ij (p , r0 ; rij )
                                                                        P P

where (Up )ij (p , r0 ; rij ) ≡ p exp[−(rij /r0 )2 ] to account for polypeptides under different
solvent conditions. For computational efficiency, all non-bonded potential energy terms
are set to zero for rij ≥ 10.0 Å. Illustrative examples of a combination of excluded-volume
and p -dependent attractive or repulsive interactions are provided in Fig. 1. In the anal-
ysis below, we refer to the p = 0 case as the SAW model, and the case with p = 0 as
well as with USAW turned off (effectively setting ex = 0) as the Gaussian chain model.
Theoretical predictions reported in this work are for chain length n = 75, which we have
used77 to address experimental SAXS and smFRET data on Protein L (refs. 59, 62). By
using this chain length, new findings are amenable to comparison with previous results. In
the present context, however, n = 75 is taken merely as an exemplifying case for proteins
of similar lengths because the focus of this study is on general principles rather than any
particular protein.
    Chain conformations are sampled at T = 300 K using standard Metropolis Monte
Carlo techniques111 described before,112 wherein equal a priori probabilities are assigned
to pivot and kink jumps,113,114 with acceptance rate of ≈ 30% for the attempted chain
moves.76,77 For each simulation, the first 107 attempted moves for equilibration are not
used for the calculation of average conformational properties. Subsequently, ∼ 109 moves
are attempted to sample ∼ 107 conformations (snapshots taken every 100 attempted
moves) for further analysis. Among other ensemble properties to be described in the




FIG. 1: Non-bonded interactions in the coarse-grained chain model. The total pairwise potential
energy (solid red or blue curves) between two monomers i, j that are not directly connected
along the polymer chain (|i − j| > 1) is the sum of the repulsive SAW potential (USAW )ij (solid
black curves) and a pairwise attractive (p < 0, blue) or repulsive (p > 0, red) interaction
(Up )ij (p , r0 ; rij ) (r0 = 3.8 Å, dashed curves). This interaction reduces to the SAW potential
when p = 0 (see text for details). (Up )ij (p , r0 ; rij ) is given here for p /kB T = ±1.5 as an
example. The total non-bonded potentials for p /kB T = ±0.5, ±1.0, ±2.0, and ±2.5 are provided
by the inset as further illustrations. An example conformation is shown for the n = 75 model
polymer utilized in the present investigation. The red and blue beads mark the chain termini,
positions corresponding to those of FRET dyes for determining REE in our previous study.77


Results section below, radius of gyration Rg = [n−1 ni=1 |Ri −Rcm |2 ]1/2 (where Rcm is the
                                                         P

center of mass or centroid position, Rcm = n−1 ni=1 Ri ) and end-to-end distance REE =
                                                      P

|Rn − R1 | are computed from the sampled conformations. Examples of the distribution
of Rg , REE populations for several different values of the intrachain interaction energy
parameter p are shown in Fig. 2. As expected, when intrachain interaction is attractive
(p < 0), the distribution shifts to smaller Rg and REE (Fig. 2b,c) relative to the SAW
distribution (p = 0, Fig. 2a), whereas the distribution shifts to larger Rg and REE when
intrachain interaction is repulsive (p > 0, Fig. 2d).
   Fig. 3 provides an overview of the properties of the p -dependent homogeneous con-
formational ensembles that are used as baselines in work. Fig. 3a shows that for these
homogeneous ensemble, hRg2 i/hREE  2
                                     i is essentially constant at ≈ 0.16 for SAW (p = 0)
and ensembles with repulsive interactions (p > 0), and the ratio increases as the en-
sembles become more compact with attractive interactions (p more negative), reaching
≈ 0.36 for p = −5.0. This trend is in line with the simulated hRg i/hREE i values of
≈ 0.41 for SAWs of comparable lengths and a rough estimate of hRg i/hREE i of 0.71 for
conformations in the shape of a compact sphere76 because 0.412 = 0.17 and 0.712 = 0.50
although hRg2 i/hREE
                     i 6= (hRg i/hREE i)2 (h. . . i represents averaging over a given ensemble).
                                                                                 2 1/2
The scaling of intrachain distance rij of these ensembles in the form of hrij      i ∼ |i − j|ν



             (a)     =0          (b)     = −1.8      (c)     = −1.0      (d)    = +2.0


FIG. 2: Radius of gyration and end-to-end distance distributions of p -dependent homopolymers
of various compactness. Joint distributions of Rg and REE (color coded) are shown for n = 75
conformational ensembles at representative p values as indicated (p given in units of kB T
hereafter). The profile of the SAW [p = 0, (a)] distribution is included as a gray background in
the other three p 6= 0 distributions [(b)–(d)] for comparison. For each ensemble, the root-mean-
square hRg2 i1/2 and hREE
                        2 i1/2 are marked by the horizontal and vertical dotted lines respectively.
A total of 10 conformations are sampled for each distribution. Numbers of conformations are
recorded for all Rg –REE bins of 1Å × 1Å and are color-coded as follows. White: 0, blue: [1–200),
cyan: [200–400), green: [400–600), yellow: [600–800), and red: ≥ 800 conformations.


is shown in Fig. 3b and the estimated p -dependent ν exponents are provided in Fig. 3c.
The tendency for the scaling exponents for smaller |i − j| (red diamonds in Fig. 3c) to be
slightly higher than those for larger |i − j| (black circles in Fig. 3c) is in line with that
seen in recent simulation results (e.g., Fig. 3A of ref. 93) and is consistent with excluded-
volume effects leading to a lower contact probability when the contacting monomers are
in the middle of the chain than when the contact is between the two ends of the chain
(with different loop-closure exponents).108,109,115 Because hRg2 i1/2 is determined by p for
these homopolymer ensembles, the essentially one-to-one mapping between p and ν in
Fig. 3c (aside from the small differences for small and large |i − j|s) is translated into
an essentially one-to-one mapping between hRg2 i1/2 and ν in Fig. 3d. Disordered protein
ensembles inferred from experiments have sometimes been characterized by homopoly-
mer scaling exponent ν as a proxy for measured hRg2 i1/2 in recent studies.84,85,93,116,117 It
should be recognized, however, that for real proteins which are heteropolymers, there is
no universal correspondence between hRg2 i1/2 and ν, as exemplified by recent studies of
the N-terminal domain of the ribosomal protein L9 (NTL9)79 and the C-terminal domain
of the same protein.98 In principle, when a conformational ensemble is sufficiently hetero-
geneous, ν may not be well-defined even when the chain dimensions are similar to those
of SAWs (see below).
    The scattering intensity I(q) of the homogeneous and heterogeneous conformational



                   (a)                                           (b)


                   (c)                                           (d)


           ν                                           ν


FIG. 3: Compactness-dependent homopolymer properties. Dimensional features of conforma-
tional ensembles with USAW + Up interactions are obtained as functions of p . (a) Root-mean-
square radius of gyration, hRg2 i1/2 (black squares, left vertical scale), and end-to-end distance,
   2 i1/2 (red circles, right vertical scale). The  -dependent ratio of mean-square R to mean-
hREE                                                  p                                    g
square REE is provided in the inset. (b) Variation of root-mean-square intrachain monomer-
monomer distance hrij  2 i1/2 with sequence separation |i − j|. Averages are based on 105 sampled

conformations for each p . The legend provides the symbols (left column) for different p val-
ues (middle column) together with the scaling exponents, ν (right column), obtained by fitting
  2 i1/2 ∼ |i − j|ν to the plotted data for each  . No ν values are fitted to the hr 2 i1/2 vs |i − j|
hrij                                                p                                  ij
data for p = −3.0 and −4.0 because of their significant deviations from linearity. (c) Scaling
exponents ν from (b) by fitting hrij 2 i1/2 data for all sequence separations (1 ≤ |i − j| ≤ 74, black

circles) and by fitting only part of the data for smaller sequence separations (3 ≤ |i − j| ≤ 30,
red diamonds). (d) Variation of scaling exponents in (c) with root-mean-square Rg .


ensembles considered in this study is computed using the Debye formula58
                                             Z ∞
                                                                 sin(qr)
                                 I(q) = 4π            dr P (r)           ,                         (1)
                                              0                     qr

where q = |q| is the magnitude of the scattering vector q,
                                                  n     n
                                            1 XX
                                  P (r) =              hδ(r − rij )i                               (2)
                                            n2 i=1 j=1

is the pair distance distribution function obtained by averaging over bead-bead distances



              (a)                                       (b)


FIG. 4: Compactness-dependent scattering properties of homopolymer ensembles. (a) Log-log
plot of scattering intensity I(q) (normalized by value at q = 0) as a function of the magnitude of
the scattering vector, q, and (b) dimensionless Kratky plots (MFFs) are shown for n = 75 SAW
(solid black curve), Gaussian-chain (dashed black curve), and homopolymer ensembles defined
by various p 6= 0. Results for the latter ensembles are depicted as color dashed curves for p < 0
and color solid curves for p > 0 as indicated by the legend in (a).


rij of sampled conformations, δ denotes the Dirac delta function, and 1/n2 is the normal-
ization factor for the total number of i, j pairs. Because our focus is on general physical
principles, we consider beads in our coarse-grained chain model as simple point-like scat-
tering centers, neglecting complexities arising from atomic form factors and solvation
in computational studies that utilize more atomistic representations of the polypeptide
chain.58,118 Inasmuch as a sufficient large number of conformations are used, our simu-
lated I(q)s are numerically robust, as we have verified by comparing I(q)s computed using
1, 000, 10, 000, or 100, 000 sampled conformations in selected cases. Practically, the upper
limit of ∞ for the integration in Eq. 1 may be replaced by the longest pairwise distance,
rmax , in the system, which is approximately equal to (n − 1)b sin(θ0 /2) ≈ 225.0Å when an
n = 75 chain in our model adopts an all-trans conformation.
    The simulated scattering intensities I(q) of the homopolymer ensembles in Fig. 3 nor-
malized by I(0) ≡ I(q = 0) = 4π are shown in Fig. 4a, the I(q)/I(0) for Gaussian
chains is also included for comparison. These curves are similar to those obtained for
other models for disordered proteins.93 Their corresponding dimensionless Kratky plots
(MFFs) are provided in Fig. 4b. Here the vertical variable I(q)/I(0) is scaled by q 2 hRg2 i
and the horizontal variable q is scaled by hRg2 i1/2 , where hRg2 i is the mean square radius
of gyration determined by the sampled conformations used for the calculation of I(q) for
the same ensemble. By definition, all dimensionless Kratky plots are essentially identical
in the small-q Guinier regime irrespective of hRg2 i1/2 , as can be seen for the examples
in Fig. 4b, because I(q)/I(0) → exp(−q 2 hRg2 i/3) for q → 0 (ref. 58) and therefore the
dimensionless vertical variable always behaves approximately as x2 exp(−x2 /3) for small
x where x = qhRg2 i1/2 is the dimensionless horizontal variable.



    We note that all the I(q)/I(0) curves for models with excluded volume in Fig. 4a (all
except the Gaussian-chain black dashed curve), irrespective of their different p values,
converge in a narrow region around q ≈ 0.3Å−1 (though the I(q)/I(0) values do not
converge at exactly the same q). This behavior of the model may be understood by
recognizing that these models, even for very different p , should share essentially iden-
tical probabilities for two shortest distances dictated by the local bond structure that
are independent of or minimally affected by the global p -dependent conformational com-
pactness. These distances are the virtual bond length between two sequential beads
(ri,i+1 = b = 3.8Å) and the distance between two beads separated by a single bead along
the chain sequence (ri−1,i+1 ≈ 2b sin(θ0 /2) = 6.08Å). The virtual bond length is a constant
in the model, whereas small variations in ri−1,i+1 are possible because the virtual bond an-
gle θi fluctuates around θ0 in accordance with a harmonic potential. The essential identical
probabilities of these short distances among the models translate into a near-coincidence
of their I(q)/I(0) values around q ≈ π/2ri,i+1 = 0.41Å−1 and q ≈ π/2ri,i+2 ≈ 0.26Å−1
in reciprocal space, averaging to q ≈ 0.34Å−1 which is consistent with the approximate
convergence observed in Fig. 4a. An approximate convergence of theoretical I(q)/I(0)
curves has also been seen in other studies, e.g., in Fig. 3B of ref. 93. In the latter case,
the convergence is at ≈ 0.2Å−1 , indicating that there are similarly probable distances
≈ π/(2 × 0.2Å−1 )= 7.9Å between scattering centers among the chain models in ref. 93
for different conformational compactness.
    Examples of the homopolymer pair distance distribution functions P (r) underlying
the I(q) functions in Fig. 4 are shown in Fig. 5. A notable shared feature among the
different P (r) plots in Fig. 5 as well as subsequent P (r) plots in this article is the
local P (r) peaks at small r values corresponding to the ri,i+1 = b = 3.8Å and the
ri−1,i+1 ≈ 2b sin(θ0 /2) = 6.08Å distances discussed above. As expected, aside from these
common local peaks at small rs, the overall peak of the P (r) distribution is shifted to
smaller r for increasingly negative p with a concomitant narrowing of the distribution.
However, the shift to larger r relative to the distribution for our SAW model is quite
small for p > 0 because short-spatial-range contact-like repulsive potentials like those
in our p > 0 models are essentially enhanced excluded volume interactions which,
unsurprisingly, do not expand chain dimensions much beyond those of a SAW that
already possesses a sizable excluded volume repulsion.

RESULTS

   MFFs of heteropolymeric and homopolymeric SAWs are sometimes clearly
distinct; but MFFs of select heterogeneous ensembles with very narrow ranges
of Rg and/or REE can be very similar to MFFs of homopolymeric SAWs. We


                               0.06


                               0.04

                        P(r)

                               0.02


                               0.00
                                      0   20   40         60   80   100
                                                    r/Å
FIG. 5: p -dependent (with excluded volume) and Gaussian-chain distributions of intrachain
monomer-monomer distances for n = 75 homopolymers. As in Fig. 4, solid and dashed black
curves are for, respectively, the SAW (p = 0, ex = 1.0kB T ) and Gaussian-chain (p = ex = 0)
conformational ensembles. The correspondence between color curve styles and p 6= 0 ensembles
is identical to that in Fig. 4 as well; but, for clarity, P (r) is plotted only for p = −2.4, −2.0,
−1.8, −1.0, and +2.0 in the present figure.


begin our analysis with three different hypothetical subensembles put forth previously as
possible heterogeneous model conformational ensembles for Protein L with very narrow
ranges of REE values77 consistent with the experimental FRET efficiencies of E ≈ 0.75 at
[GuHCl] = 1 M and E ≈ 0.45 at [GuHCl] = 7 M (Fig. 6). Two of the MFFs in Fig. 6 are for
two subensembles sharing the same narrow range of Rg ≈ 23.5Å (hRg2 i1/2 ≈ Rg because of
the narrow range) but with significantly different REE s, namely REE ≈ 46.5Å for [GuHCl]
= 1 M (solid magenta curve) and REE ≈ 56.9Å for [GuHCl] = 7 M (solid blue curve).
These subensembles are of interest as examples of Rg –REE decoupling,77,78 in that the
ensembles have the same Rg despite having very different REE . Fig. 6 shows that their
MFFs are distinct but similar in some notable respects. The MFF for the subensemble
with smaller REE (magenta) is more oscillatory than that for the subensemble with larger
REE (blue) for 2 . qhRg2 i1/2 . 7 while the two MFFs converge at larger qhRg2 i1/2 values.
Moreover, the MFFs of both of these subensembles—which are heterogeneous ensembles
by construction—are quite similar to the MFF of a homopolymer ensemble with the same
hRg2 i1/2 and an hREE
                      i1/2 corresponding approximately to the [GuHCl] = 7 M case (black
dashed curve). The differences among the MFFs are small except for 2 . qhRg2 i1/2 . 4
which one may refer to as the “shoulder region” of the dimensionless Kratky curves. These
comparisons indicate that, for some heterogeneous ensembles, different heterogenous and
homogeneous ensembles entail different MFFs. In principle, therefore, these ensembles
are distinguishable by SAXS measurements alone even though the ensembles share the
same average Rg . However, as seen in Fig. 6, the differences among some of the theoretical
MFFs can be subtle. Thus, detectability of such differences may still be limited practically




                           q <Rg > I(q)/I(0)


                                                   0      5        10
                                                           2 1/2
                                                       q<Rg >

FIG. 6: Theoretical MFFs pertinent to the case of Protein L at [GuHCl] = 1 and 7 M analyzed
previously.77 Dimensionless Kratky plots for n = 75 heterogeneous conformational ensembles
with (i) a sharp, δ-function-like distribution with a narrow range of Rg centered at 23.5 Å and
a similarly sharp distribution of REE at 46.5 Å (consistent with FRET efficiency E = 0.745
when Förster radius R0 = 55 Å, solid magenta curve), (ii) a sharp distribution of REE at
46.5 Å (corresponding to E = 0.745) but no restriction on Rg otherwise (hRg2 i1/2 = 21.6 Å,
dashed red curve), and (iii) a sharp distribution of REE at 56.9 Å (consistent with E = 0.447)
but no restriction on Rg otherwise (hRg2 i1/2 = 23.4 Å, solid blue curve) are compared with that
for an p = −0.5 homogeneous conformational ensemble with hRg2 i1/2 = 23.5 Å and hREE  2 i1/2 ≈

59.9 Å (dashed black curve).


by uncertainties in experimental measurements. In contrast, the MFF for a subensemble
with a smaller hRg2 i1/2 ≈ 21.6Å (dashed red curve) is clearly distinguishable from the
other three MFFs because of its substantially lower q 2 hRg2 iI(q)/I(0) for qhRg2 i1/2 & 2.
    Fig. 7 provides a systematic comparison of SAXS signatures of SAW homopolymers
with a broad distribution of Rg and REE on one hand against SAW subensembles each
with a narrow range of Rg and/or a narrow range of REE on the other. Here we fo-
cus on subensembles with an hRg2 i1/2 ≈ 24.5Å (Fig. 7a) equals to the hRg2 i1/2 of the
full homopolymeric SAW ensemble. As emphasized above, these subensembles are, by
construction, heterogeneous conformational ensembles. It is noteworthy that despite the
differences among the subensembles themselves and their drastically different Rg –REE
distributions vis-à-vis that of the full homopolymer ensemble (Fig. 7a), their I(q)/I(0)
versus q plots appear to be quite similar aside from seemingly minor differences around
q ∼ 0.1Å−1 (Fig. 7b). When presented as dimensionless Kratky plots (Fig. 7d), the
differences in the shoulder region of the plots (2 . qhRg2 i1/2 . 4) for the different het-
erogeneous subensembles are more discernible. The subensembles’ different I(q)s are a
reflection of their different pair distance distribution functions (Fig. 7c, Eq. 1). Among
the subensembles with the same narrow range of Rg but different narrow ranges of REE
in Fig. 7c, the peaks of the P (r) of small-REE subensembles (dashed color curves) shift to



larger r values relative to the peak of the P (r) for the homopolymer ensemble (solid black
curve). Interestingly, the P (r) of the subensemble with the largest REE ≈ 88.5Å among
the subensembles considered is almost identical to the P (r) of the homopolymer ensem-
ble. Accordingly, their dimensionless Kratky plots essentially overlap (Fig. 7d, solid black
and dashed dark-purple curves). In other words, quite remarkably, the SAXS signatures
of these two very different disordered conformational ensembles—a highly heterogeneous
ensemble with a narrow range of Rg as well as a narrow range of REE on one hand, and
a homogeneous ensemble with a broad distribution of both Rg and REE on the other—
are practically indistinguishable. Because REE ≈ 88.5Å is substantially larger than the
hREE  i1/2 ≈ 62.5Å for the full homopolymer ensemble, it appears that inasmuch as effects
on P (r) are concerned, narrowing the broad distribution of Rg of the full homopolymer
ensemble to a sharply peaked distribution around its hRg2 i1/2 value can be compensated by
replacing the broad distribution of REE of the full homopolymer ensemble with a sharply
peaked distribution around an REE value that is significantly larger than the hREE  2
                                                                                       i1/2 of
the homopolymer ensemble.
    Aiming to generalize the above analysis to conformations that are more compact or even
more open, we have also compared the SAXS signatures of p = 0 SAW subensembles
with narrow ranges of hRg2 i1/2 ≈ 22.5, 18.5, and 26.5Å, which are equal, respectively,
to the hRg2 i1/2 of the homopolymer ensembles with p = −1.0, −1.8, +2.0 (the Rg –
REE distributions of which are illustrated in Fig. 2). The results of the analysis are
documented in Figs. S1–S3 of the Supporting Information. They indicate that while the
trend observed in Fig. 7c of a shift of the P (r) peak to higher r values relative to that of
the homopolymer ensemble for subensembles with smaller REE persists in Figs. S1c, S2c,
and S3c, none of the subensembles considered—including those with large REE s—has a
P (r) that matches closely with the P (r) of the corresponding homopolymer ensembles.
Consequently, all of these subensembles entail dimensionless Kratky plots that are quite
clearly distinguishable from that of their homopolymer counterparts (Figs. S1d, S2d, and
S3d), thus offering examples for which heterogeneous and homogeneous conformational
ensembles with the same hRg2 i1/2 can be distinguished by SAXS-determined MFFs alone.
At the same time, the observation from Figs. S1–S3 suggests that heterogeneous ensembles
constructed as subensembles of homopolymers with different overall compactness may be
different even if the subensembles themselves feature the same narrow range of Rg and
narrow range of REE . This issue will be further explored below.
    Root-mean-square of intrachain distance rij as a function of contour length separation
|i − j| are shown for representative subensembles in Fig. S4 of Supporting Information.
For subensembles with compact conformational dimensions such as those in Fig. S4d, the
   2 1/2
hrij i versus |i − j| relationship is nonlinear, similiar to the corresponding relationships
                                                                                        2 1/2
exhibited by the homopolymer ensembles with p . −2.4 in Fig. 3b. Indeed, the hrij        i


             (a)                                  (b)


             (c)                                  (d)


FIG. 7: SAXS properties of subensembles of SAW chains. (a) The complete SAW homopolymer
ensemble is represented by the gray area corresponding to the overall profile for p = 0 in Fig. 2;
      2 i1/2 is indicated by the vertical blue solid line. The subensemble with a narrow R range,
its hREE                                                                                  g
24 ≤ Rg /Å < 25, but is otherwise unrestricted, is marked by the horizontal lines. Similarly,
the subensemble with a narrow REE range, 63 ≤ REE /Å < 64, but is otherwise unrestricted, is
marked by the vertical dashed lines. Subensembles defined by narrow ranges for both Rg and
REE are indicated by the small color squares, which are slightly wider than the actual ranges
of REE to enhance legibility. (b) Log-log plot of scattering intensity for the SAW homopolymer
ensemble and various subensembles as specified by the legend. The color code of the dashed lines
for the subensembles with narrow ranges for both Rg and REE (dashed lines) is the same as that
for the small squares in (a). (c) Distributions of intrachain monomer-monomer distances, and (d)
dimensionless Kratky plots (MFFs) for the SAW homopolymer ensemble and the subensembles
in (b), plotted using the same line styles as those in (b).


versus |i − j| relationship can be highly nonlinear for heteropolymers,119–121 in which
cases no ν can be reasonably defined. More recent examples of simulated heteropolymers
                             2 1/2
lacking an approximate hrij   i ∼ |i − j| scaling include results shown in Figs. 2 and 4
of ref. 121 and Fig. S3 of ref. 117 even though usage of ν in lieu of hRg2 i is advocated
in ref. 117. Here, for the subensembles with the same Rg as the relatively open p = 0
                                                 2 1/2
SAW homopolymers studied in Fig. 7, the hrij      i    versus |i − j| plots in Fig. S4a are
largely linear except for |i − j| ≈ n = 75, but they do exhibit other, more minor
variations despite the subensembles sharing the same Rg . The divergent behaviors for
large |i − j|s, which correspond to distances between two ends of the chain, are stemming
from the narrow ranges of REE imposed by the definition of the subensembles. Aside



                                                  ν = 0.71


                                                        ν = 0.62


                                              |i−j|

FIG. 8: Variation of root-mean-square intrachain monomer-monomer distance hrij2 i1/2 with

sequence separation |i − j| for the SAW homopolymer ensemble and various subensembles in
Fig. 7, plotted using the same color code. The maximum and minimum scaling exponents (ν)
obtained from the fitted straight lines are indicated.


from that, variations are also noticeable for |i − j| ∼ 7—40. A zoomed-in version of the
  2 1/2
hrij i ∼ |i−j|ν plots for these subensembles in Fig. 8 indicates that the apparent scaling
exponent ν of the subensembles ranges from ≈ 0.62 to 0.71. While these mathematically
constructed subensembles are hypothetical as to their physical realizability, they do serve
to underscore that for heterogeneous disordered conformational ensembles, the apparent
scaling exponent ν is not necessarily a proxy for hRg2 i1/2 , as has been demonstrated
recently in combined theoretical/experimental studies of real disordered proteins.79,98
As it stands, ν is largely a model parameter that is currently not amenable to direct
experimental determination. Using such a parameter to replace the experimentally
measured hRg2 i as a descriptor of ensemble properties does not appear to be well advised.

   MFFs of select heterogeneous ensembles with very narrow ranges of Rg
and REE can be very similar to MFFs of compact homopolymers. Building
on the initial results in Figs. S1–S3 (Supporting Information) discussed above, we ex-
plore whether and, if so, what heterogeneous ensembles may possess SAXS signatures
practically indistinguishable from those of homopolymer ensembles that are more com-
pact or more open than the p = 0 SAW homopolymers. Now, instead of constructing
heterogeneous ensembles by selecting from the p = 0 homopolymer conformations as in
Figs. S1–S3, we construct heterogeneous ensembles by selecting from the conformations
of an p 6= 0 homopolymer ensemble. Interestingly, among the heterogeneous subensem-
bles constructed in this manner to cover a narrow range of REE and a narrow range of
Rg values around the hRg2 i1/2 of the p 6= 0 homopolymer, some of the heterogeneous
subensembles with relatively large REE s can have P (r)s very similar to the P (r) of the
corresponding homopolymer ensemble with the same p 6= 0. Consequently, their MFFs
are also extremely similar. Examples of such heterogeneous and p 6= 0 homogeneous en-
sembles with closely matching dimensionaless Kratky plots are provided in Figs. 9a,b, and



c between subensembles with REE ≈ 70.5, 65.5, and 84.5Å, respectively, and their corre-
sponding homopolymer ensembles with different compactness as specified by p = −1.0,
−1.8, and +2.0. In line with the p = 0 situation in Fig. 7, the REE of these subensem-
bles in Figs. 9a–c with homopolymeric SAXS signatures are considerably higher than
the hREE  i1/2 ≈ 50.5, 18.5, and 74.5Å, respectively, of their corresponding p = −1.0,
−1.8, and +2.0 homopolymer ensembles. It is instructive to contrast these subensembles
of p 6= 0 homopolymers in Figs. 9a–c exhibiting homopolymeric SAXS signatures with
those subensembles with the same narrow Rg , REE ranges but constructed from p = 0
chains in Figs. S1–S3 (Supporting Information) that do not exhibit similar SAXS sig-
natures. This observation indicates that MFFs of disordered chains can be sensitive to
p -dependent conformational preferences even when variations in Rg and REE in the en-
sembles are highly restricted. In any event, the examples of SAXS signature matching
in Figs. 9a,b affirm that MFFs of at least some highly heterogeneous ensembles can be
practically identical to MFFs of compact homopolymers and therefore these disordered
conformational ensembles cannot be distinguished solely by their SAXS spectra.
    To facilitate systematic computation and evaluation of MFFs of a large number of
                                                           Rx
heterogeneous ensembles (see below), ∆Kratky (1, 2) ≡ 0 max dx|y1 (x) − y2 (x)|, where
y = q 2 hRg2 iI(q)/I(0) and x = qhRg2 i1/2 , is hereby defined (Fig. 9d) to quantify the
difference in SAXS signature between two conformational ensembles (labeled 1 and 2).
As illustrated in Fig. 9d, ∆Kratky may be viewed as a simple measure of mismatch between
two dimensionless Kratky plots. We use xmax = 10 for the present study. Besides the
present application, we note that ∆Kratky may also be useful in future investigations
to optimize the match between experimental MFFs and those computed from inferred
conformational ensembles.92,122

   MFFs of heterogeneous ensembles with significantly less variation in Rg can
still be very similar to MFFs of homopolymeric SAWs. As shown by the above
analysis, subensembles defined by narrow ranges of Rg and REE are instrumental—as in-
dividual heterogeneous ensembles—in identifying scenarios in which the SAXS signatures
of heterogeneous and homogeneous ensembles are clearly distinguishable or remarkably
similar, or somewhere in between. In aggregate, these subensembles may be seen as com-
ponents of a basis set for a “conformational ensemble space” by which other heterogeneous
ensembles can be constructed as weighted combinations of component ensembles. In this
regard, the homopolymer ensemble is a special case of such an ensemble in which the
components are weighted by their fractional populations in the homopolymer ensemble.
Adopting this conceptual framework, we now extend our consideration to heterogeneous
ensembles, constructed as weighted combinations of (Rg , REE ) subensembles, that en-
compass a broader variety of conformations. Instead of restricting to narrow ranges Rg


            (a)                                  (b)
                      = −1.0                              = −1.8


            (c)                                  (d)
                      = +2.0


FIG. 9: Comparing MFFs of homogeneous and heterogeneous ensembles sharing essentially the
same hRg2 i1/2 . (a)–(c) Dimensionless Kratky plots (MFFs) of p 6= 0 homogeneous ensembles
are compared with those of subensembles that are subsets of the full ensemble for the given p
with Rg and/or REE ranges specified by the inset legends. (d) Schematic of a pairwise difference
measure for any two dimensionless Kratky plots referred to as ∆Kratky (see text) and defined
as the total area (shaded) between the two plots within a given range of qhRg2 i1/2 (e.g., from
qhRg2 i1/2 = 0 to 10 as in this depiction). The two Kratky plots shown in (d) are hypothetical
and for illustration only. They do not correspond to the simulated Kratky plots in (a)–(c).


and REE , nonzero weights are assigned to all conformations in a homopolymer ensem-
ble in the construction of these ensembles. In particular, we are interested in ensembles
with a tighter distribution of Rg2 than the SAW homopolymer ensemble. Such heteroge-
neous ensembles are apparently less artifical than the individual (Rg , REE ) subensembles.
Intuitively, they are physically plausible, especially when the distribution P (Rg2 ) of the en-
semble is at most moderately tighter than that of a homopolymer ensemble. Conceivably,
sequence-dependent effects of IDPs may encode a tighter P (Rg2 ) for biological function, as
envisioned, e.g., in the proposed polyelectrostatic binding between Sic1 and Cdc4 (ref. 14).
It would be useful, therefore, to ascertain theoretically whether such heterogeneous en-
sembles are distinguishable from homopolymer ensembles by SAXS-measured MFFs alone
or measurements by complementary techniques are needed.
   Toward this aim, reweighted ensembles with the same hRg2 i as the homopolymers but
with a narrower distribution of Rg2 are constructed. Here we let δRg2 ≡ Rg2 − hRg2 i and
introduce α, α0 ≥ 0 as scaling factors for controlling the broadness of the reweighted Rg2
distribution. For a given homopolymeric P (Rg2 ), the reweighted Rg2 distribution is ob-
tained by the modification P (Rg2 ) → N0−1 exp[−α(δRg2 )]P (Rg2 ) for δRg2 < 0 and P (Rg2 ) →




                        (a)                              (b)


FIG. 10: SAXS spectra of conformational ensembles with the same hRg2 i but different Rg2 distri-
butions. (a) MFFs (dimensionless Kratky plots) of the homogeneous SAW (p = 0 homopoly-
mer) ensemble and heteropolymeric reweighted ensembles with α = 0.1, 0.01, and 0.001 (the
corresponding α0 values are, respectively, 0.09351, 0.007153, and 0.0006099). (b) Rg2 distribu-
tions of the ensembles in (a) plotted using the same color code. The standard deviations of Rg2
for the SAW (α = 0), α = 0.001, 0.01, and 0.1 distributions are, respectively, 218.7, 205.8, 117.8,
and 14.8 Å2 , their corresponding square roots are 14.8, 14.3, 10.9, and 3.85 Å.

                                                       R0
N0−1 exp[−α0 (δRg2 )]P (Rg2 ) for δRg2 > 0 where N0 = 2 −∞ dδRg2 exp[−α(δRg2 )]P (Rg2 ) is the
overall normalization factor for the reweighted (modified) P (Rg2 ), and α0 is related to α
                R0                                          R∞
by the equation −∞ dδRg2 exp[−α(δRg2 )]P (Rg2 ) = N0 /2 = 0 dδRg2 exp[−α0 (δRg2 )]P (Rg2 ),
which determines α0 numerically for any given α.
   The dimensionless Kratky plots of the SAW (p = 0) homopolymer ensemble and
three reweighted ensembles—which are heterogeneous ensembles—are shown in Fig. 10a.
Notably, despite the heterogeneous ensembles’ very different P (Rg2 ) distributions, ranging
from being only slightly narrower than that of the homopolymer (α = 0.001) to being
highly peaked (α = 0.1, Fig. 10b), their dimensionless Kratky plots are extremely similar
(Fig. 10a), exhibiting little variation even in the shoulder regions where considerable
variation was observed in Fig. 7d among the dimensionless Kratky plots of the (Rg , REE )
subensembles. Hence, the results in Fig. 10 suggest strongly that certain physically
plausible heterogeneous ensembles of disordered proteins with narrower distributions
of Rg2 can hardly be distinguishable by their SAXS signatures from a homopolymer
ensemble with the same hRg2 i. We will extend the study of similarly reweighted ensembles
to p = −1.0, −1.8, and +2.0 below.

   MFFs of heterogeneous and homogeneous ensembles can be practically
identical despite significant differences in REE , asphericity, and Rg distribu-
tions. We have now demonstrated that homopolymer ensembles and certain subensem-
bles defined by very narrow Rg , REE ranges and relatively large REE s can lead to es-
sentially indistinguishable dimensionless Kratky plots (Figs. 7d and 9a–c). Separately,
high degrees of similarity can also be seen between the dimensionless Kratky plots of



homopolymers and those of conformationally more diverse heterogeneous ensembles with
slightly to significantly narrower Rg2 distributions (Fig. 10). In view of these findings, we
next consider, in a systematic manner, an extensive set of heterogeneous ensembles with
narrower-than-homopolymer distributions of Rg similar to those studied in Fig. 10 and
also narrower-than-homopolymer distributions of REE peaking at different REE values to
catalog these heterogeneous ensembles’ SAXS signatures. As such, these heterogeneous
ensembles may be viewed as “smeared” versions of the (Rg , REE ) subensembles with very
narrow Rg , REE ranges. In this regard, these heterogeneous ensembles are intuitively more
plausible to be physically encodable by heterpolymeric amino acid sequences and therefore
of more immediate relevance to potential experimental situations.
    We construct these ensembles by additional reweighting of the above-described
reweighted ensembles with narrower Rg2 distributions, now applied also to chains with
p 6= 0 [P (Rg2 ) parameterized by p and α], to further bias the final ensembles toward a
select REE value. Let P (Rg2 , REE ) be the fractional population density with square ra-
dius of gyration Rg2 and end-to-end distance REE . By definition, the above α-dependent
reweighted P (Rg2 ) may be written as an integral over P (Rg2 , REE ), viz.,
                                           Z ∞
                              P (Rg2 ) =         dREE P (Rg2 , REE ) .                              (3)


We now reweight each P (Rg2 , REE ) as follows:

            P (Rg2 , REE ) → N (Rg , γ, REE
                                            )−1 P (Rg2 , REE ) exp[−γ(REE − REE
                                                                                )2 ] ,              (4)

where the normalization factor N (Rg , γ, REE ), defined by
 Z ∞                                                                     Z ∞
       dREE P (Rg2 , REE ) exp[−γ(REE − REE
                                            )2 ] = N (Rg , γ, REE
                                                                  )            dREE P (Rg2 , REE ) , (5)
  0                                                                      0


preserves the weight of each individual Rg2 value, and therefore the overall hRg2 i of the
reweighted ensemble remains the same as that of the original ensemble. In Eqs. 4 and 5,
REE  is an input parameter, a reference value of REE toward which the ensemble is biased
to a degree parameterized by γ. It should be noted that the actual hREE i or hREE     i1/2 of
the final reweighted ensemble depends on α, γ as well as the value of Rg2 and is therefore
not expected to be exactly equal to REE    .
    Using the MFF difference measure ∆Kratky defined above (Fig. 9d), we have conducted
an extensive exploration of the α, γ, REE  parameter space to identify heterogeneous ensem-
bles with MFFs closely matching those of homopolymers. Because it is combinatorically
impractical to examine all three parameters exhaustively, we focus on several representa-
tive REE   values. We do so by first examining ∆Kratky between homopolymer ensembles



and an extensive set of heterogeneous ensembles parametrized by combinations of α, γ
values for REE    = 30, 60, and 90Å. As shown in Fig. S5 of Supporting Information, the
results of this calculation suggest that ensembles with REE        = 90Å are more likely to lead
to small ∆Kratky , especially when putative optimal values for γ ≈ 0.05, 0.06, 0.03, and
0.1 that minimize ∆Kratky are chosen, respectively, for chains with intrachain interaction
p = 0, −1.0, −1.8, and +2.0.
    We then proceed to explore the α, REE        parameter space while using these putative
optimal γ values as given (Fig. 11). The variations of the resulting ∆Kratky between
homopolymer ensembles and the heterogeneous ensembles as functions of α and REE               are
depicted by the contour/heat plots in Figs. 11a–d. Interestingly, while minimal ∆Kratky
is found in a region of relatively large REE     ∼ 70–100Å in every case studied here (most
lightly shaded region in Figs. 11a–d)—as one might expected because selection of the γ
parameters used in Fig. 11 is based on ensembles with REE            = 90Å in Fig. S5, a second
minimal-∆Kratky region is also observed in Fig. 11c around REE ≈ 30Å and α ≈ 0.01.
    To quantify the structural differences between the reweighted heterogeneous ensembles
constructed for chains with different intrachain interaction energy p with their corre-
sponding homopolymer ensemble, we compute the asphericity123 for each chain confor-
mation, defined as124
                                         3(λ1 λ2 + λ1 λ3 + λ2 λ3 )
                                A≡1−                               ,                          (6)
                                            (λ1 + λ2 + λ3 )2
where λ1 , λ2 , λ3 (all ≥ 0) are the eigenvalues of the gyration tensor Sµν ≡ n−1 ni=1 (Ri −
                                                                                     P

Rcm )µ (Ri − Rcm )ν , where µ, ν = 1, 2, 3 label the Cartesian axes (the ν index here should
not be confused with the exponent ν for pair distance scaling), and Rg2 = λ1 + λ2 + λ3 .
The asphericity quantity A has been used to analyze folded and disordered states of
proteins,125,126 including recent theoretical applications to better understand smFRET
and SAXS signatures of disordered proteins.76,127 Here we determine the average aspheric-
ity, hAi, for each ensemble of interest by averaging A over the (weighted) conformations in
the ensemble and, as measure for one aspect of structural differences between a heteroge-
neous ensemble and a homopolymer ensemble, we define ∆A as the difference between hAi
of a heterogeneous ensemble and that of a homopolymer ensemble. The variations of ∆A
among the reweighted heterogeneous ensembles as functions of α and REE              are depicted
by the contour/heat plots in Figs. 11e–h.
    Figs. 11a–d show that there are low-∆Kratky regions of considerable extent in (α, REE       )
parameter space, but these regions do not coincide with the low-∆A white regions in
Figs. 11e–h. This observation indicates that there are a wide variety of heterogeneous
ensembles with conformational properties significantly different from those of homopoly-
mers but nonetheless possess SAXS signatures essentially indistinguishable from those of
homopolymers. Examples of how the pair distance distribution function P (r) of some


                      (a)                      (e)


                                                                         =0


                      (b)                      (f)


                                                                         = −1.0


                      (c)                      (g)


                                                                         = −1.8


                      (d)                      (h)


                                                                         = 2.0


                                  α                       α

FIG. 11: Variation of SAXS behaviors and conformational asphericity among heteropolymeric
ensembles with the same hRg2 i. (a)–(d) ∆Kratky and (e)–(h) difference in average asphericity,
∆A , between heteropolymeric (REE0 , α, γ)-defined reweighted ensembles (γ = 0.05, 0.06, 0.03,

and 0.1, respectively, for p = 0, −1.0, −1.8, and +2.0) and the homogeneous ensemble for
the given p values are computed for a 10 × 10 grid of (REE0 , α) values to produce each of the

contour plots. ∆A is the average asphericity of the heteropolymeric ensemble minus that of the
homogeneous ensemble.


of these heterogeneous ensembles with minimal ∆Kratky match closely with the P (r)
of homopolymer ensembles are provided in Fig. 12. As far as MFFs are concerned, it
follows that the dimensionless Kratky plots of the four example heterogeneous ensembles
in Figs. 12a–d, constructed from chains with intrachain interaction energy p = 0, −1.0,
−1.8, and +2.0, and therefore are of different conformational compactness characterized
by hRg2 i1/2 = 24.4, 22.2, 18.5, and 26.5Å, respectively, are hardly distinguishable from
the dimensionless Kratky plots of their homopolymeric counterparts (Fig. 13a). Despite
the near-coincidence of their SAXS signatures of these pairs of heterogeneous and
homogeneous ensembles, their conformational properties are drastically different, as can
be seen by their very different distributions of mean square end-to-end distance (Fig. 13b)
and average asphericity (Fig. 13c). Interestingly, among the four examples highlighted,
the average asphericities of the heterogeneous and homogeneous ensembles are least



                              (a)       =0               (b)     = −1.0


                              (c)      = −1.8            (d)     = 2.0


FIG. 12: Homogeneous and heterogeneous ensembles can have essentially identical distributions
of intrachain monomer-monomer distances. P (r)s are shown for the homogeneous ensembles
(black curves) and the heteropolymeric reweighted ensembles with minimized ∆Kratky deduced
                                                               0 /Å, α, γ) for minimum ∆
from Fig. 11 (red curves). The reweighting parameters (REE                                  Kratky are:
(a) (90.0, 0.04, 0.05), (b) (80.0, 0.08, 0.06), (c) (30.0, 0.01, 0.03), and (d) (110.0, 0.1, 0.1).


dissimilar for the p = −1.8 case (hRg2 i1/2 = 18.5, Fig. 13, third row from top). This
feature may be a result of contraints imposed by the overall conformational compactness,
or it may be related to our choice of this particular heterogeneous ensemble with an REE
distribution peak that coincides approximately with that of the homopolymer ensemble,
though the REE   distribution itself is much narrower for the heterogeneous ensemble than
for the homopolymer ensemble. In any event, the above extensive cataloging of SAXS
signatures of heterogeneous ensembles (Fig. 11) and the explicit examples in Figs. 12 and
13 demonstrate that, across conformational ensembles of different overall compactness,
certain heterogeneous ensembles with conformational properties dramatically different
from those of homopolymers can nonetheless exhibit essentially identical SAXS signatures
as homopolymers.

    Approximate analytical theory for sequence-dependent MFFs of disordered
heteropolymers. The heterogeneous ensembles considered above are tools for logically
delineating the information content of SAXS signatures. To serve as examples and coun-
terexamples, it suffices to define these ensembles mathematically, as long as the ensembles
are in principle physically realizable, without demonstrating how the presumed protein
ensembles might be encoded exactly by amino acid sequences. Nonetheless, it is intu-
itively plausible that disordered protein ensembles similar to some—though not all—of
these constructs, such as the reweighted ensembles encompassing diverse conformations
but with distributions of Rg2 somewhat narrower than those of homopolymers (Fig. 10),


                     (a)                 (b)                  (c)                            24
                           =0


                           = −1.0


                           = −1.8


                           = 2.0


                                                                     A


FIG. 13: Drastically different disordered conformational ensembles can lead to essentially iden-
tical MFFs. (a) Dimensionless Kratky plots (MFFs), (b) distributions of square end-to-end
distances REE2 , and (c) distributions of conformational asphericity A are shown for the ho-

mogeneous ensembles (black curves) and heteropolymeric minimum-∆Kratky reweighted ensem-
bles (red curves) in Fig. 12. The standard deviation of the Rg2 distribution (in units of Å2 ),
   2 i1/2 /Å, and hAi for the homogeneous  = 0 ensemble are 218.7, 62.5, 0.461, respectively;
hREE                                         p
whereas the corresponding values for the p = 0 minimum-∆Kratky ensemble are 42.8, 87.3,
0.610. For p = −1.0, the corresponding numbers are 190.1, 56.0, 0.442; 19.0, 78.1, 0.566. For
p = −1.8: 149.8, 45.1, 0.386; 70.1, 31.1, 0.331, and for p = +2.0: 248.8, 68.6, 0.473; 31.9,
105.0, 0.696. The 102 (b) and 1/50 (c) in the vertical variables are normalization factors.


may be encodable by specific amino acid sequences. Given the current inadequate under-
standing of the physical interactions governing conformational properties of disordered
proteins,49 few insights, if any, exist as to the encodability of heterogeneous disordered
protein ensembles, i.e., there is very little knowledge about what ensembles are phys-
ically realizable and what ensembles are not. In this light, while a recent analysis of
computed MFFs of heteropolymers with hydrophobicity-like interactions led the authors
to conclude that “Rg and REE remain coupled even for heteropolymers”,116 it should be
noted that their study covered only a limited regime of heteropolymeric interactions, leav-
ing the likely vast possibilities of disordered conformational heterogeneity allowable by
polypeptide sequences unsurveyed. Here we take a rudimentary step to further explore
these possibilities by developing an extension of the perturbative techniques in polymer
theory for treating excluded volume effects99–109 to incorporate heterogeneous pairwise
intrachain interactions. Although our analytical formulation is restricted to contact-like



interactions with a short spatial range and thus subtle effects of polypeptide interac-
tions cannot be addressed, results below from this computationally efficient approach are
instructive in offering a glimpse of how various properties of heterogeneous disordered
ensembles—including decoupling of Rg and REE in some cases—might be encoded.
   Our analytical formulation is based on the path-integral representation of the polymer
partition function                      Z
                               Q(N, {ṽ}) =     [DR]e−H(N,{ṽ},{R}) ,                                      (7)

where N is the total contour length of the polymer and R(τ ) is the spatial position of the
point labeled by the contour length variable τ along the polymer. If a bond connecting
two monomer beads is identified with a chain segment of length l, the total number of
beads in each chain modeled by Eq. 7 is equal to n = N/l + 1. For notational convenience,
l is set to unity (l = 1) unless specified otherwise. The Hamiltonian H is given by
                          Z N                   Z N        Z τ −a
                    1              dR(τ ) 2
  H(N, {ṽ}, {R}) =             dτ          +         dτ            dτ 0 ṽ(τ, τ 0 )δ[R(τ ) − R(τ 0 )] ,   (8)
                    2      0        dτ           a          0


where ṽ(τ, τ 0 ) is the pairwise interaction energy between the points labeled by τ and τ 0
along the polymer chain, and a ∼ 1 is a cutoff in contour length to remove unphysical
self interaction of any chain segment with itself. In general, the energy function ṽ(τ, τ 0 )
depends on τ, τ 0 and thus the formulation describes a heteropolymer. In the special case
when ṽ(τ, τ 0 ) = ṽ0 > 0, i.e., when ṽ is independent of τ and τ 0 , Eqs. 7 and 8 reduce to those
for a homopolymer with uniform excluded volume interactions [see, e.g., Eqs. (5.1) and
(5.2) of ref. 108 and Eqs. (4.1) and (4.2) of ref. 109]. It should also be noted that although
we allow individual pairwise interactions in Eq. 8 to be neutral, attractive or repulsive,
for simplicity, we do not employ a three-body repulsion term (as in some other analytical
formulations, see, e.g., ref. 121) to account for excluded volume when ṽ is attractive in
the present perturbative treatment.
    Diagrammatic perturbation expansions in the present heteropolymer formulation pro-
ceed largely along the description in ref. 108 except v0 in this reference is now replaced by
ṽ(τ, τ 0 ) which is then placed inside the dτ dτ 0 integrals as a factor of the integrand. As
                                               R   R
                     √
well, the c(τ ) = dR(τ ) rescaling of the spatial coordinates in ref. 108 is not applied here
because it offers no advantage for our present applications which are all for d = 3 spatial
dimensions. As a result, the propagator given by Eq. (5.10) of ref. 108 is now replaced
by (3/2π)3/2 (1/|τ − τ 0 |)3/2 exp[−3|R − R0 |2 /(2|τ − τ 0 |)]. To simplify the expressions to
be presented below, we define v(τ, τ 0 ) ≡ (3/2π)3/2 ṽ(τ, τ 0 ) and v0 ≡ (3/2π)3/2 ṽ0 . After all
these notational modifications are taken into account, the “v0 ” in ref. 109 is seen to be
equivalent to (2π)3/2 v0 in the present formulation.
    In the present notation, the standard perturbative formula for mean square end-to-end




                                            sR
                                               q
                                       vij
                                                 R’
                                  0    τi τj     s’ N


FIG. 14: Diagrams for perturbative calculations of scattering intensities for heteropolymers.
vij is the interaction energy between contour positions τi and τj . Contour positions s and s0
at spatial positions R and R0 (connected by a dashed line) are associated with the scattering
vector q.


distance99,107 is now generalized to
                                      Z N          Z τj −a
                                                                  vij
                      hREE i=N+              dτj             dτi p     + O(vij2 )            (9)
                                       a            0             ∆τij

for heteropolymer, where ∆τij ≡ τj − τi is the contact order108,109 of the τi , τj contact, and
vij = v(τi , τj ). For vij = v0 , i.e., for the special case in which the chain is a homopolymer,
the above expression reduces to

                                       4√     √   2a3/2
                                                     
                 hREE i=N     1 + v0     N − 2 a−           + O(v02 ) ,                     (10)
                                       3           3N

as in refs. 99 and 107. For heteropolymers with discrete sequences, we replace the integral
in Eq. 9 by summing over a discrete interaction matrix vij —which may be viewed as
containing the net energetic effects of “hard-core” excluded volume repulsions and short-
spatial-ranged sequence-dependent attractive or repulsive interactions, viz.,

                                                n Xj−1
                                               X        v
                            hREE i=N+                  p ij + O(vij2 )                      (11)
                                               j=2 i=1
                                                         ∆ij

where ∆ij ≡ j − i, and a = 1 is used for the double summations here in Eq. 11.
   Application of the above-described perturbative formalism to the Feynman-type di-
agrams in Fig. 14 for heteropolymer scattering intensities (which correspond to the six
diagrams in Fig. 1 of Ohta etal.106 for homopolymer scattering intensities) leads to the



following perturbative expression for the scattering intensity:
                                  
            2        1  −αN
     I(q) =     N+       e     −1
            α        α
                Z N     Z τj −a          ( 
                                     vij    1                1  −α(N −∆τij )   
            −2      dτj         dτi 3/2        N − ∆τij +       e             −1
                 a        0        ∆τij     α               α
                                                          p             )
                       1                              ∆τ ij        α∆τ  ij
                                                                           
              +∆τij         2 − e−ατi − e−α(N −τj ) +        F                 + O(vij2 )
                       α                               2            2
                                                                                                   (12)

where α ≡ q 2 /6, and
                                                          2   Z z
                                               e−z                         2
                                        F(z) ≡                      dt et                          (13)
                                                z              0

is plotted in Fig. S6a of the Supporting Information. We have verified by a rather involved
algebraic comparison of the expressions in Eqs. (12) and (13) for the vij = v0 special case
of homopolymers against the results provided by Eqs. (3.3)–(3.8) in Ohta et al.106 that
our first-order perturbative results for I(q) are consistent with theirs except for several
likely typographical errors in ref. 106, as described in the Supporting Information of the
present article. In this regard, we should also note that the subject matter and goals of the
two efforts are different: whereas ref. 106 studies universal homopolymeric behaviors in
the limit of infinite chain length through renormalization group analysis128 (see the “RN”
Kratky plot in Fig. S2A of ref. 93 and the I(x) curve in Fig. 2 of ref. 106), the main focus
of the present work is on sequence-specific properties of finite-length heteropolymers.
    Proceeding now from Eq. 12 above, as q → 0, i.e., in the α → 0 limit, the expression
in Eq. 12 becomes
                                           Z N         Z τj −a                   
                               2                                           vij
                    I(0) = N           1−         dτj               dτi     3/2
                                                                                      + O(vij2 )   (14)
                                             a           0                ∆τij
                                                            p
because F(z) = 1−2z 2 /3+4z 4 /15−8z 6 /105+O(z 8 ), thus F( α∆τij /2) = 1−α∆τij /6+
                                            p
α2 (∆τij )2 /60 + O(α3 ) and hence limα→0 F( α∆τij /2) = 1. It follows that
                                   
    I(q)    2         1  −αN
         =       1+       e      −1
    I(0)   αN       αN
              Z N     Z τj −a          (
                                  vij     1 h ∆τij       1  −α(N −∆τij )        i
           −2     dτj         dτi 3/2         −       +       e           − e−αN
                a      0         ∆τij    αN        N    αN
                                                          p          )
               ∆τij 1                                 ∆τ ij     α∆τ  ij
                                                                         
             +              2 − e−ατi − e−α(N −τj ) +        F               + O(vij2 ).(15)
                 N αN                                  2N         2



Using the standard formula for Guinier’s approximation,58

                                       d                       1 d
                    hRg2 i = −3          2
                                           [I(q)/I(0)]|q=0 = −      [I(q)/I(0)]|α=0                    (16)
                                      dq                       2 dα

as well as the expansion dF(z)/dz = −4z/3 + 16z 3 /15 − 16z 5 /35 + O(z 7 )
             p
and thus dF( α∆τij /2)/dα = −∆τij /6 + α(∆τij )2 /30 + O(α2 ) and therefore
          p
limα→0 dF( α∆τij /2)/dα = −∆τij /6, we obtain, in (implicit) units of l2 :
                                Z τj −a
                                                                                         2∆τij2   ∆τij3
                   Z N
                                                              ∆τij τi2 + (N − τj )2
                                                                                                     
             N                                    vij
  hRg2 i   =   −          dτj              dτi      3/2
                                                                                    −1 +        −
             6      a            0               ∆τij          2          N2              3N      4N 2
            +O(vij2 ) .                                                                                (17)

For the special case of homopolymer, vij = v0 , and this expression reduces to

                           134 √     √   2a3/2   a5/2   a7/2
                                                          
              N
     hRg2 i =     1 + v0        N − 2 a−       +      +          + O(v02 ) ,                           (18)
               6           105            3N     5N 2 7N 3

which is consistent with the result of Fixman.99 For heteropolymers, combining Eq. 9 with
Eq. 17 yields
                                Z τj −a
   hRg2 i                                                                                2∆τij2   ∆τij3
                   Z N
                                                              ∆τij τi2 + (N − τj )2
                                                                                                     
           1                                       vij
          = −             dτj              dτi      3/2
                                                                                    +1 +        −
  hREE i   6        a             0              ∆τij         2N          N2              3N 2    4N 3
             +O(vij2 ) .                                                                               (19)

The corresponding expression for homopolymers is obtained by combining Eq. 10 and
Eq. 18:
               hRg2 i                2√
                                            5/2
                                                   a7/2
                                                      
                         1                  a
                       =    1 − v0      N+       +          + O(v02 ) .       (20)
              hREE   i   6           35     5N 2 7N 3
For heteropolymers with discrete sequences, the integrals in Eq. 15 for I(q)/I(0), Eq. 17
for hRg2 i, and Eq. 19 for hRg2 i/hREE
                                       i are replaced by summmations with a discrete pairwise
interaction matrix vij that replaces the vij = v(τi , τj ) in the continuum, viz.,

                                      Z N         Z τj −a              n j−a
                                                                       X X
                                            dτj               dτi ←→               ,                   (21)
                                       a            0                  j=a+1 i=1

where, in most cases, we take a = 1 as in Eq. 11 for hREE         i. Practically, the same
discretization is also used for numerical calculations of I(q)/I(0) for homopolymers when



vij = v0 . In general, it follows from Eq. 15 that
                                    
                       I(q)     I(q)    e2 (N, {vij }, q; a) + O(v 2 ) ,
                            =          +G                         ij                       (22)
                       I(0)     I(0) 0

where104                                               
                           I(q)        2       1  −αN
                                  =        1+     e    −1                          (23)
                           I(0) 0 αN          αN
                                     RN
follows from the P (r) = (8πr2 /N 2 ) 0 dx(N − x)(3/2πx)3/2 exp(−3r2 /2x) pair distance
distribution function for Gaussian chains, and

                                     j−a
                                   n
                                                  ( 
                               2   X X   vij       1          1                         
                                                                   −α(N −∆τ    )    −αN
     e2 (N, {vij }, q; a) ≡ −
     G                                        3/2
                                                      −∆ij +     e          ij
                                                                                 −e
                              N 2 j=a+1 i=1 ∆ij    α          α
                                                                     p             )
                                     1                            ∆ ij          α∆ ij
                                                                                      
                              +∆ij       2 − e−αi − e−α(N −j) +         F                   (24)
                                     α                             2             2

in the discretized form. The continuum form for Ge2 (N, {vij }, q; a) is readily obtainable
by replacing the double summations by the double integrals in Eq. 24 in accordance
with the correspondence specified in Eq. 21. To show I(q)/I(0) in a logarithmic scale,
which is a common practice as in Figs. 4a and 7b, we use the standard expansion of
ln(1 + x) = x + O(x2 ) to recast Eq. 22 as
                                    
                         I(q)     I(q)
                     ln        =         + Fe2 (N, {vij }, q; a) + O(vij2 )                (25)
                         I(0)     I(0) 0

where

                                                   e2 (N, {vij }, q; a)
                                                   G
                           Fe2 (N, {vij }, q; a) ≡                      .                  (26)
                                                     [I(q)/I(0)]0
For the special case of homopolymers, vij = v0 , we have
                                      
                         I(q)     I(q)
                              =          + v0 G2 (N, q; a) + O(v02 ) ,                     (27)
                         I(0)     I(0) 0

where
                            G2 (N, q; a) ≡ G
                                           e2 (N, {vij }, q; a)|v =1
                                                                 ij
                                                                                           (28)

is the expression given by Eq. 24 with all vij set to unity, and
                                      
                           I(q)     I(q)
                       ln        =         + v0 F2 (N, q; a) + O(v02 )                     (29)
                           I(0)     I(0) 0


            (a)                                    (b)


                                                    I(q)/I(0)
                                                                             increasing


                                                                     q


FIG. 15: Perturbation theory-predicted and explicit-chain model simulated conformational and
SAXS properties of homogeneous ensembles. (a) Plotted v0 values are obtained by fitting per-
turbation theory results calculated using effective chain length Ñ = 43, effective Kuhn length
b̃ = l = 6.46 Å, and a = 1 to explicit-chain simulated hRg2 i (black squares), hREE
                                                                                  2 i (red circles),

hRg2 i/hREE
         2 i (blue triangles), and I(q)/I(0) (black diamonds) for homopolymers with excluded

volume (ex = 1.0kB T , Figs. 3 and 4) and p = −5.0, −4.0, −3.0, −2.4, −2.2, −2.0, −1.8,
−1.6, −1.4, −1.2, −1.0, 0.0, +2.0, +4.0, +6.0, +8.0, and +10.0. Lines joining data points are
merely guides for the eye. (b) The explicit-chain simulated I(q)/I(0) (solid curves, from Fig. 4a)
are compared with their fitted perturbation theory-predicted I(q)/I(0) calculated using Eq. 27
(dashed curves, same color code). As indicated by the vertical arrow, p increases monotonically
(becoming less attractive or more repulsive) from the highest to the lowest I(q)/I(0) curves
plotted. The inset shows the function G2 (q) = G2 (Ñ = 43, q; a = 1) in Eq. 28.


where
                                                    G2 (N, q; a)
                                  F2 (N, q; a) ≡                 .                             (30)
                                                   [I(q)/I(0)]0
   To compare these theoretical predictions with our simulated explicit-chain model re-
sults, it is necessary to determine the effective Kuhn length, referred to as b̃ below, of
the explicit-chain model because the polypeptide-mimicking bond-angle potential of the
model (see Models and Methods) entails b̃ 6= b where b = 3.8 Å is the Cα –Cα virtual bond
length. Here, we determine b̃ and the effective chain length Ñ of the polypeptide model
by equating the the mean-square radius of gyration, hRg2 i0 , of the Gaussian (ex = 0)
version of our model with Ñ b̃2 /6 while keeping the total contour length Ñ b̃ = N b un-
                                                                1/2
changed. For our Gaussian chain model, N = n−1 = 74, hRg2 i0 = 17.4 Å (corresponding
   2   1/2
hREE  i0 = 42.6 Å, hRg2 i0 /hREE
                                  i0 = 6.0). This calculation yields b̃ = 1.7b = 6.46 Å and
Ñ = 43.5. Based on this determination, we use N → Ñ → bÑ c = 43 and n → Ñ +1 = 44
in the applications of our discretized formulation below.
   We first compare predictions of our analytical formulation for homopolymers with the
corresponding explicit-chain simulation results. Setting the chain length N to Ñ = 43
and the length unit l from unity to l = b̃ = 6.46 Å in Eq. 10 for hREE   i, Eq. 18 for hRg2 i,
Eq. 20 for hRg2 i/hREE
                       i, and Eqs. 24, 27, and 28 for I(q)/I(0), we obtain, separately for
each of these v0 -dependent quantities, the v0 values in the analytical formulation that



optimize fitting to the corresponding explicit-chain simulated results for these quantities
in Figs. 3 and 4 (Fig 15a). The relationship between the p in the explicit-chain model
(horizontal variable in Fig. 15a) and the optimized v0 in the analytical formulation (ver-
tical variable in Fig. 15a) is monotonic, as one would expect, but is clearly nonlinear,
exhibiting a sigmoidal-like increase around p ≈ −2.0 and v0 ≈ 0. The trends for the four
conformational properties tested are largely consistent, supporting, at least to a degree,
the effectiveness of the theory. But the optimally fitted v0 values for I(q)/I(0) are ap-
preciably lower than those for hREE        i, hRg2 i, and hRg2 i/hREE
                                                                      i, indicating that more subtle
structural and energetic features of the explicit-chain models are not captured by the
analytical formulation. Nonetheless, with the optimized v0 values for I(q)/I(0), Fig. 15b
shows that the analytical predictions fit the explicit-chain results quite well overall. The
G2 (q) = G2 (N = Ñ = 43, q; a = 1) function (Eq. 28) used for computing the theoretical
scattering curves is shown in the inset. The fit in Fig. 15b is excellent for I(q)/I(0) & 0.2
(q . 0.9–2.0). Mismatches appear for I(q)/I(0) . 0.2 in that the explicit-chain-simulated
curves converge but the analytical curves do not, for the simple reason that the analyti-
cal formulation—unlike the explicit-chain model (see discussion of the results in Fig. 4a
above)—does not entail a near-universal minimum nonzero intrachain pairwise distance
for all the chain conformations in any given ensemble. For a more extensive survey of
the theoretical formulation developed here, the G2 (N, q; a) and F2 (N, q; a) (Eq. 30) for
several other N and a values are provided in Figs. S6b,c of the Supporting Information.
   In Fig. 15a, we notice that the optimally fitted v0 excluded-volume parameters for
the explicit-chain simulated hREE         i, hRg2 i, hRg2 i/hREE
                                                                 i, and I(q)/I(0) of p = 0 SAW
homopolymers, all in the neighborhood of v0 ∼ 0.2, are considerably larger than the
corresponding optimally fitted theoretical excluded-volume parameter for intrachain
contact probabilities obtained previously [see, e.g., Eq. (4.4) of ref. 109]. As an example,
the simulated hRg2 i/hREE  2
                               i ≈ (24.4Å/62.5Å)2 = 0.1524 for p = 0 SAW homopolymers
of length N → Ñ = 43, which according to Eq. 20 yields a fitted v0 = 0.228 for a = 1.
For intrachain probabilities, a value of v0 ≃ 0.41 was estimated,109 which translates, as
explained above, into a much smaller v0 → v0 /(2π)3/2 ≈ 0.026 in the present unit for v0 .
A possible cause of this difference—which deserves to be studied further—is that the per-
turbative terms for the quantities in Fig. 15a is of order v0 N 1/2 whereas the perturbative
terms for the contact reduction factors in ref. 109 is of order v0 N 0 = v0 . Interestingly,
while the simulated hRg2 i/hREE   2
                                    i ratio of ≈ 0.1524 is less than the Gaussian-chain value of
1/6 = 0.1667 as one would expect from Eq. 20, our simulated ratio for an effective SAW
chain length of Ñ = 43 is also less than the renormalization-group-predicted universal
ratio of hRg2 i/hREE2
                       i ≈ (1/6)(95/96) = 0.1649 for SAWs. The latter ratio follows from
                106,129
the expansion           hRg2 i/hREE
                                    i = (1/6)(1 − /96) + O(2 ) [Eq. (4.6) of ref. 106], where
 = 4 − d, and the number of spatial dimensions, d, is equal to 3 for our model systems



and thus  = 1 (the dimensional parameter  here is not to be confused with an energy
parameter).

   Explicit-chain simulations of heteropolymers with theory-inspired interac-
tions exemplify hRg2 i–hREE   2
                                 i decoupling in heterogeneous ensembles. We are
now in a position to apply the analytical formulation to explore heteropolymer sequences
that would likely lead to significant decoupling of hRg2 i and hREE       i, beginning with a class
of heteropolymeric interactions that leads to pairs of heteropolymers predicted by our
perturbation theory to have the same hREE         i but different hRg2 is.
   Consider the O(vij ) term for hREE   i in Eq. 9. By changing the contour variables τi , τj
to τi , ∆τij and thus rewriting vij = v(τi , τj ) = v(τi , ∆τij ), the O(vij ) term for hREE i may
be expressed in the equivalent form
                           Z N                   Z N −∆τij
                                 d∆τij p                     dτi v(τi , ∆τij ) .                  (31)
                             a          ∆τij       0

                                                                                          R N −∆τij
It follows that for a given ∆τij , all variations of v(τi , ∆τij ) over τi that leave the 0         dτi
integral over v(τi , ∆τij ) in Eq. 31 unchanged would result in the same predicted hREE i.
However, according to Eq. 17, such variations can change hRg2 i. Therefore, different
heteropolymers represented by different v(τi , ∆τij ) functions that nevertheless yield the
       R N −∆τij                                                                    2
same 0           dτi v(τi , ∆τij ) for all ∆τij are predicted to have the same hREE    i but they can
have different hRg i values. In other words, by Eq. 19, heteropolymers can share the same
hREE  i but have different hRg2 i/hREE     2
                                             i. As an illustration, consider two heteropolymers
with model interaction schemes vij = v1+ and v1− defined by

                                 v1± (τi , ∆τij ) = v0 + u± (τi , ∆τij ) ,                        (32)

where
                    
                    ±v[4τ /(N − ∆τ ) − 1] , for 0 ≤ τ ≤ (N − ∆τ )/2;
    ±                     i         ij                  i             ij
   u (τi , ∆τij ) =                                                                               (33)
                    ∓v[4τi /(N − ∆τij ) − 3] , for (N − ∆τij )/2 ≤ τi ≤ N − ∆τij .


Here v1+ and v1− are given, respectively, by the above expressions carrying the upper and
                                                    R N −∆τij
lower signs, and v is a constant. Because 0                   dτi u± (τi , ∆τij ) = 0 and therefore
R N −∆τij
          dτi v1± (τi , ∆τij ) = (N − ∆τij )v0 , the hREE2
                                                           i values predicted by Eq. 9 for these
                              2          2                                 2          2
two heteropolymers, hREE iv1+ and hREE iv1− , are identical, i.e., hREE      iv1+ = hREE iv1− for any
value of v. However, the hRg i values predicted by Eq. 17 for these two heteropolymers,



                      (a)                      (b)                        (c)


          I(q)/I(0)


FIG. 16: Comparing heteropolymer perturbation theory-predicted and explicit-chain simulated
scattering intensities in the v1± and (p )±
                                           1 interaction schemes. Here I(q)/I(0) is computed using
v1 and (p )1 (blue curves) as well as v1− and (p )−
  +          +
                                                        1 (red curves), with v > 0. Perturbation
theory-predicted results (dashed curves) are calculated according to Eq. 25 using effective chain
length Ñ = 43, effective Kuhn length b̃ = 6.46 Å, a = 1, and Eqs. 32 and 33 with (a) v0 = 0,
v = 0.1 for v1± , (b) v0 = 0, v = 0.5 for v1± , and (c) v0 = 0.1121—which is the background
repulsion corresponding to the p = 0 SAW according to the I(q)/I(0)-fitting in Fig. 15a—
together with v = 2.5 for v1+ and v = 0.5 for v1− . Explicit-chain simulation results (solid curves)
                                                                                                ±
are obtained using Eq. 35, with (a) ex = 0, v = 0.1 for (p )±
                                                              1 , (b) ex = 0, v = 0.5 for (p )1 , and
                                                                                                    −
(c) ex = 1.0kB T (full excluded volume) together with v = 2.5 for (p )+  1 and v = 0.5 for (p )1 .


hRg2 iv1+ and hRg2 iv1− , are not identical, as it can readily be shown that
                                                                              
                                                                  8      p
                            hRg2 iv1+ − hRg2 iv1− = vN 3/2           + O( a/N ) .                 (34)

A discrete version of the model heteropolymer interaction schemes in Eq. 33 for an explicit
chain model with a background excluded-volume interaction (corresponding to v0 > 0)
may be implemented by assigning the additional pairwise interaction energies between
monomers i, j as follows:
               
               
               
                ±v{2(i − 1)/[(n − ∆ij )/2 − 1] − 1} ,
               
                          for (n − ∆ij ) even & 1 ≤ i ≤ (n − ∆ij )/2 ;
               
               
               
               
               
               
                 ∓v{2[i − (n − ∆ij )/2 − 1]/[(n − ∆ij )/2 − 1] − 1} ,
               
               
               
               
               
                          for (n − ∆ij ) even & {[(n − ∆ij )/2] + 1} ≤ i ≤ (n − ∆ij ) ;
               
               
  [(p )± ]
        1 ij =                                                                          (35)
               
               
                ±v{2(i −  1)/[(n − ∆ ij − 1)/2] − 1} ,
               
               
               
               
               
                         for (n − ∆ij ) odd & 1 ≤ i ≤ (n − ∆ij + 1)/2 ;
               
                 ∓v{2[i − (n − ∆ij + 1)/2]/[(n − ∆ij − 1)/2] − 1} ,
               
               
               
               
               
               
                          for (n − ∆ij ) odd & [(n − ∆ij + 1)/2)] ≤ i ≤ (n − ∆ij )
               


for ∆ij = |j − i| ≥ 3; (p )±                             ±             ±
                            ij = 0 for ∆ij < 3, and [(p )1 ]ij = [(p )1 ]ji by definition.
   Comparisons of theory-predicted and explicit-chain-simulated scattering intensities are



provided in Fig. 16 for heteropolymers embodying examples of these v1± or (p )±    1 inter-
actions. Because the baseline (zeroth order term) of our analytical perturbative formula
for I(q)/I(0) is that of a Gaussian chain (Eqs. 23–26), we first compare theoretical pre-
dictions with simulation results of heteropolymers with no hardcore excluded volume
(ex = 0, Figs. 16a,b). In these cases, we find good agreement between theory and sim-
ulation when the heteropolymeric interactions are relatively weak (v = 0.1, Fig. 16a),
indicating that the theoretical formulation is effective at a rudimentary level. However,
an offset between theoretical and simulated results is seen for stronger heteropolymeric
interactions (v = 0.5, Fig. 16b) although the rank orderings of the I(q)/I(0) entailed by
the v1± and (p )±1 interaction schemes are nonetheless consistent (red curves are higher
than blue curves for both the solid and dashed curves in Fig. 16b). This mismatch is
probably related to the nonlinear relationship between the v0 -like and p -like energy pa-
rameters in the theoretical formulation and the explicit-chain model, respectively, as has
been observed for homopolymers in Fig. 15b. In this regard, a sizable theory-simulation
mismatch is also observed in Fig. 16c, where the simulated I(q)/I(0)s are seen to be prac-
tically identical for two different SAW heteropolymers (ex = 10kB T ) with essentially the
same hRg2 i1/2 ≈ 24.1 Å (solid red and blue curves in Fig. 16c), but the theory-predicted
I(q)/I(0)s by assuming a linear relationship between the v0 -like and p -like energy pa-
rameters differ significantly (dashed curves in Fig. 16c). Because the theory-simulation
mismatch in Fig. 16c is still quite small for the smaller v = 0.5 (red curves) and becomes
significant only for the larger v = 2.5 (blue curves), the mismatch here is also likely at-
tributable to a nonlinear relationship between the v0 -like and p -like energy parameters
as suggested above for the results in Fig. 16b. A resolution of this issue will significantly
broaden the utility of the present analytical formulation for heteropolymers and thus
deserves to be further investigated in future efforts.
    An immediately useful application of the present analytical formulation is to iden-
tify explicit-chain models with theory-inspired heteropolymeric interactions that exhibit
significant decoupling of hRg2 i and hREE 2
                                            i. Fig. 17 provides the hRg2 i1/2 and hREE 2
                                                                                         i1/2
values (Fig. 17b) of examples of heteropolymers embodying the (p )±   1 interaction scheme
(Eq. 35) illustrated by the heat maps in Fig. 17a. Consistent with the theoretical pre-
diction in Eq. 34, Fig. 17b shows that for a given |v|, the hRg2 i1/2 (diamonds) of the
v > 0 heteropolymer (blue) is always larger than that of the v < 0 heteropolymer
(red). Moreover, the theoretical prediction that a pair of such (p )±    1 -heteropolymers
                            2   1/2
with ±|v| have equal hREE i         values (blue and red circles) is also realized approxi-
mately by those explicit-chain models in Fig. 17b with small to moderate |v| values—i.e.,
|v| ≤ 3.0 for SAW (ex = 1.0kB T ) heteropolymers and |v| ≤ 0.5 for ex = 0 heteropolymers
without hardcore excluded volume—but not for models with higher |v| values probably
because perturbation theory is less accurate for larger |v|. As anticipated by theory


                 (a)                                        (b)


      Residue Number


                            10   20     30 40 50 60    70
                                      Residue Number

FIG. 17: Variations of explicit-chain-simulated root-mean-square radius of gyration and end-
to-end distance in the heteropolymeric (p )±    1 interaction scheme. (a) An example of the energy
matrices with matrix elements [(p )1 ]ij (lower triangle) and [(p )−
                                       +
                                                                          1 ]ij (upper triangle) depicted
using a color scale (right) for n = 75 and v = 3.0. (b) Root-mean-square radius of gyration
hRg2 i1/2 (diamonds) and root-mean-square end-to-end distance hREE         2 i1/2 (circles) of chains with

full excluded volume (ex = 1.0kB T ) for (p )1 , v = |v| > 0 (blue) and (p )−
                                                     +
                                                                                         1 , v = |v| > 0,
which is equivalent to (p )+1 , v =  −|v|   <  0  (red)  are  plotted slightly  offset to the left and to
the right, respectively, of |v| = 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, and 6.0. For |v| = 0.1, 0.5, 1.0, and 1.5,
corresponding hRg2 i1/2 and hREE 2 i1/2 for  = 0 (i.e., with Gaussian-chain baseline)—which are
                                              ex
always smaller than their counterparts for ex = 1.0kB T —are also included for comparison.


(Eq. 34), some of the (p )±                                                      2 1/2
                               1 -heteropolymers have significantly different hRg i     values de-
                                            2   1/2                           2    2
spite having essentially the same hREE i . Examples of such hRg i–hREE i decoupling
include the two |v| = 3.0 SAW (p )+        1 -heterpolymers with hREE i
                                                                        2   1/2
                                                                                ≈ 54 Å for which
     2     2    1/2                               2     2
(hRg i/hREE i) = 23.6Å/54.8Å = 0.43 (hRg i/hREE i = 0.19) for v = +3.0 (blue symbols)
but (hRg2 i/hREE2
                   i)1/2 = 20.2/53.7 = 0.38 (hRg2 i/hREE  2
                                                            i = 0.14) for v = −3.0 (red symbols),
                                           ±
and the two |v| = 0.5 ex = 0, (p )1 -heteropolymers with hREE         2
                                                                           i1/2 ≈ 24 Å for which
(hRg2 i/hREE
              i)1/2 = 12.6/24.4 = 0.52 (hRg2 i/hREE   2
                                                         i = 0.26) for v = +0.5 (blue symbols)
         2      2    1/2                          2     2
but (hRg i/hREE i) = 9.0/24.1 = 0.37 (hRg i/hREE i = 0.14) for v = −0.5 (red symbols).
    Scenarios exist within the (p )±   1 heteropolymeric interaction scheme in Eq. 35 that
different heteropolymers sharing essentially the same hRg2 i1/2 can exhibit significantly dif-
ferent SAXS signatures. Two examples are shown in Fig. 18. In both examples, the MFF
of the (p )±
            1 -heteropolymer with the smaller |v| (red curve) is practically indistinguishable
from that of a homopolymer (black curve), which, however, is significantly different from
the MFF of the (p )±    1 -heteropolymer with the larger |v| (blue curve). These results rein-
force the above observation (Figs. 6, 7, 9, 10, and 13) that SAXS MFFs can sometimes
but cannot always distinguish between heterogeneous and homogeneous conformational
ensembles.
    We now turn to another class of heteropolymeric interactions which is predicted by
our perturbation theory to yield pairs of heteropolymers that have the same hRg2 i but



                            (a)                                 (b)


FIG. 18: Comparing MFFs of homogeneous and energy-matrix-specified heterogeneous explicit-
chain ensembles with full excluded volume (ex = 1.0kB T ) and essentially the same hRg2 i. (a)
MFFs (dimensionless Kratky plots) of heteropolymer ensembles governed by the (p )+      1 , v = 2.5
                                   −                                    2  1/2
interactions (blue) and the (p )1 , v = 0.5 interactions (red), with hRg i     = 24.1 and 24.2 Å,
respectively, are compared with that of the homogeneous p = −0.1 ensemble with hRg2 i1/2 = 24.2
Å (black). (b) MFFs of heteropolymer ensembles governed by the (p )+     1 , v = 3.0 interactions
                    −                                           2  1/2
(blue) and the (p )1 , v = 1.5 interactions (red), both with hRg i = 23.6 Å, are compared with
that of the homogeneous p = −0.4 ensemble with hRg2 i1/2 = 23.7 Å (black).

different hREE is (in contrast to the above (p )±
                                                 1 scheme for heteropolymers with the same
   2                     2
hREE i but different hRg is). For this purpose, we make use of the change in integration
variable in Eq. 31 to rewrite the O(vij ) term for hRg2 i in Eq. 17 as
                      Z N                       Z N −∆τij
                 1                        1
               − 2                d∆τij p                   dτi v(τi , ∆τij )Z(N, τi , ∆τij ) ,     (36)
                N       a                ∆τij    0


where
                                             ∆τij                            
    Z(N, τi , ∆τij ) ≡ τi2 − (N − ∆τij )τi +                    3∆τij − 4N = (τi − λ)(τi − λ0 ) ,   (37)

with λ = [N − ∆τij + Λ(∆τij )]/2 > 0 and λ0 = [N − ∆τij − Λ(∆τij )]/2 ≤ 0, wherein
             p
Λ(∆τij ) ≡ N (3N − 2∆τij )/3. Within the integration range in Eq. 36, the function
Z(N, τi , ∆τij ) < 0. For a given ∆τij and for τi values within the range [0, N − ∆τij ], the
function takes its maximum (least negative) value of Zmax ≡ λλ0 = ∆τij (3∆τij − 4N )/12
at τi = 0 and N − ∆τij , and its minimum (most negative) value of −Λ(∆τij )2 /4 =
N (2∆τij − 3N )/12 at τi = (N − ∆τij )/2. These considerations indicate that the following
two model heteropolymer interaction schemes, v(τi , ∆τij ) = v2+ and v2− , defined by

                                                                         Zmax
                       v2± (τi , ∆τij ) = v0 + u± (τi , ∆τij )                         ,            (38)
                                                                      Z(N, τi , ∆τij )

where u± (τi , ∆τij ) is from Eq. 33, will give the same hRg2 i in Eq. (17). This property of
v2± is readily verified by using either of them for v(τ, ∆τij ) in Eq. 36 to yield the same



O(vij ) term for hRg2 i. As is the case for v1± , v2± = v0 ∓ v at τi = 0 and τi = N − ∆τij . The
model interactions v2± are of interest because according to Eq. 9 they should lead to two
            2                                    2              2
different hREE i values, denoted here as hREE       iv2+ and hREE iv2− . Their O(vij ) difference is
given by
                                      Z N                        Z N −x
          2           2
                                               √                  u+ (y, x)
        hREE iv2+ − hREE iv2−   = 2          dx x(3x − 4N )               dy
                                     a                 0        Z(N, y, x)
                                     Z N
                                           √
                                                                             
                                                          1       Λ(x) + N − x
                                = 4v     dx x(4N − 3x)        ln
                                       a                 Λ(x)     Λ(x) − N + x
                                                                              
                                                          2        N (3N − 2x)
                                                     −         ln
                                                        N −x       x(4N − 3x)
                                ≈ −1.67(vN 3/2 ) (a → 0) ,                                         (39)

where we have used the variables x and y for ∆τij and τi , respectively. In the same
manner in which we arrived at Eq. 35, a discrete version of v2± may be given by pairwise
interaction energies

                                          ∆ij [3∆ij − 4(n − 1)]/12
                          [(p )±
                                2 ]ij ≡                            [(p )±
                                                                         1 ]ij ,                   (40)
                                            Z(n − 1, i − 1, ∆ij )

where the function Z is now evaluated for N = n − 1 at discrete values of i = 1, 2, . . . , n −
∆ij and [(p )±                                                                 ±
                1 ]ij is defined by Eq. 35 above. An example of the (p )2 interaction scheme
in Eq. 40 is provided by the heat maps in Fig. 19a.
    The SAW examples (ex = 10kB T ) in Fig. 19b of explicit-chain simulated hRg2 i1/2 and
hREE   i1/2 values of heteropolymers embodying the (p )±    2 interaction scheme are largely in
line with the theoretical prediction that a pair of (p )±     2 -heteropolymers with the same
                                   2 1/2
|v| should have the same hRg i (diamonds)—which is essentially the case for |v| ≤ 3.0
and holds approximately for |v| = 6.0—but increasingly different hREE             i1/2 s (circles) with
increasing |v|. (We note, however, that while the sign of the difference in hREE                i1/2 for
the v > 0 and v < 0 (p )+       2 -heterpolymers with the same |v| is consistent with Eq. 39
for |v| ≤ 3.0, the sign is opposite for |v| = 6.0). Therefore, although the theory does
not appear to work well for the ex = 0 chains in Fig. 19b (data points at bottom left),
the simulated data on SAW (p )+                                                              2
                                       2 -heteropolymers provide ample examples of hRg i–hREE i

decoupling, including the case of |v| = 3.0 in which (hRg2 i/hREE   2
                                                                        i)1/2 = 23.7Å/57.5Å = 0.41
(hRg2 i/hREE2
              i = 0.17) for v = +3.0 (blue symbols) but (hRg2 i/hREE     2
                                                                            i)1/2 = 24.2/63.0 = 0.38
(hRg2 i/hREE2
              i = 0.15) for v = −3.0 (red symbols) though the hREE       2
                                                                            i1/2 ∼ 24 Å of these two
heteropolymers are quite similar, and the case of |v| = 6.0 in which (hRg2 i/hREE            2
                                                                                                i)1/2 =
17.4/31.5 = 0.55 (hRg2 i/hREE   2
                                   i = 0.31) for v = +6.0 (blue symbols) but (hRg2 i/hREE     2
                                                                                                i)1/2 =
16.4/16.3 = 1.0 for v = −6.0 (red symbols) though the hREE            i1/2 values of ∼ 17 Å for this


                 (a)                                               (b)


      Residue Number


                            10   20     30 40 50 60    70
                                      Residue Number

FIG. 19: Variations of explicit-chain-simulated hRg2 i1/2 and hREE        2 i1/2 in the heteropolymeric
                                                                                  ±
(p )±
     2 interaction scheme in Eq. 40. (a) Similar to Fig. 17a for (p )1 , here [(p )2 ]ij (lower
                                                                                                 +

triangle) and [(p )− 2 ]ij (upper triangle) are shown for n = 75 and v = 3.0. (b) Using the same
notation as that in Fig. 17b, hRg2 i1/2 (diamonds) and hREE        2 i1/2 (circles) for ( )+ , v = |v| > 0
                                                                                          p 2
(blue) and (p )− 2 ,  v  =  |v|  >  0 (red)  are shown   for full  excluded  volume   (ex  = 1.0kB T ) at
|v| = 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, and 6.0, and also for the ex = 0 (Gaussian-chain baseline) case at
|v| = 0.5, 1.0, and 1.5.


pair of |v| = 6.0 (p )±
                       2 -heteropolymers are also quite similar.
    Another class of heterogeneous interactions predicted by our perturbation theory to
keep hRg2 i unchanged while changing hREE    i is given by vij = v(τi , τj ) = v(∆τij ), which is
a function of ∆τij alone to be defined below. In other words, in this interaction scheme,
all intrachain contacts of the same order have the same energy but intrachain contacts
with different contact orders have different energies. Consider
                                                          p
                                                              ∆τij                           
                            v3± (∆τij ) ≡ v0 ∓ ṽ3                              2∆τij − N − a              (41)
                                                   (N − ∆τij )(2N 2 − ∆τij2 )

where ṽ3 is an adjustable energy scale. Under v3± and for a given |ṽ3 |, hRg2 i is the same
irrespective of whether the minus or plus sign is taken for the ∓ sign in Eq. 41 because
the O(vij ) term for hRg2 i (Eq. 36) with v3± is equal to
                                                                  Z N −∆τij
                                                    v3± (∆τij )
                                         Z N
                                 − 2           d∆τij p                        dτi Z(N, τi , ∆τij ) = 0 .   (42)
                                  N        a             ∆τij      0

In contrast, the sign choice would affect hREE i, as can be readily verifed that the O(vij )


                 (a)                                           (b)


      Residue Number


                            10    20     30 40 50 60    70
                                       Residue Number

FIG. 20: Variations of explicit-chain-simulated hRg2 i1/2 and hREE     2 i1/2 in the heteropolymeric

(p )±
     3 interaction scheme (Eq. 44). (a) Similar to Figs. 17a and 18a, here [(p )3 ]ij (upper
                                                                                              +

triangle) and [(p )−  2 ]ij (lower triangle) are shown for n = 75 and v = 100.0. In this case,
                                                      −
although min{[(p )+    3 ]ij } = −100 and max{[(p )3 ]ij } = +100, a graded color scale for [−3, +3]
                                          −
(with all [(p )+3 ]ij ≤ −3 and all [(p )3 ]ij ≥ +3 depicted, respectively, by the same deepest blue
and red) is used to visualize variation in pairwise energy because |[(p )±    3 ]ij | is relatively small
for most i, j. (b) Using the same notation as that in Figs. 17b and 18b, hRg2 i1/2 (diamonds)
and hREE 2 i1/2 (circles) for ( )+ , v = |v| > 0 (red) and ( )− , v = |v| > 0, which is equivalent
                                   p 3                           p 3
        +
to (p )3 , v = −|v| < 0 (blue), are shown for full excluded volume (ex = 1.0kB T ) at |v| =
0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 6.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 25.0, 50.0, and 100.0. Unlike
Figs. 17b and 18b, no data for the Gaussian-chain, ex = 0 baseline case is shown.

difference in hREE i calculated using v3+ verus that calculated using v3− is given by
                                                                        √
                                                      √
                                                                                
             2           2                      ṽ3                        2+1
           hREE iv3+ − hREE iv3−              = √ [(2 2 + 1) + a/N ] ln √
                                                  2                      2 + a/N
                                                                                 √
                                                              √
                                                                                           
                                                                                     2−1
                                                          +[(2 2 − 1) − a/N ] ln √            , (43)
                                                                                   2 − a/N

which equals −0.140ṽ3 in the a/N → 0 limit. We obtain a discretized version of this
interaction scheme by setting N → n = N + 1 in Eq.41 to arrive at
                                                  p
                                                     ∆ij (2∆ij − n − a)        n2 + 2n − 1
                                                                                              
                                       ±
                                 [(p )3 ]ij = ∓v                           √                        (44)
                                                  (n − ∆ij )(2n2 − ∆2ij )    n − 1 (n − 2 − a)

and by choosing a = 3. Accordingly, the above interaction scheme (p )±      3 in Eq. 44 is
defined for ∆ij = a = 3, 4, . . . , n − 1, where the expression inside the square bracket is
a normalization factor such that |v| is the magnitude of the interaction for the largest
contact order ∆ij = n − 1 (Fig. 20a).
   The SAW examples (ex = 10kB T ) in Fig. 20b of explicit-chain simulated hRg2 i1/2
and hREE  i1/2 values of heteropolymers embodying the (p )±    3 interaction scheme show



little variation for |v| . 12. For |v| & 14, hREE        2
                                                             i1/2 of (p )+
                                                                          3 -heteropolymers with
v > 0 (blue circles) decreases steeply with increasing |v|. Although the corresponding
hRg2 i1/2 (blue diamonds) also decreases concomitantly in a trend that differs from the
perturbation theory prediction of unchanged hRg2 i1/2 , the rate of decrease of hRg2 i1/2
with increasing |v| is more gradual than that of hREE             i1/2 as one might intuitively
anticipate from an approximate theory. In this regard, Fig. 20b provides a few examples
of dramatic hRg2 i–hREE 2
                            i decoupling, including a pair of |v| = 20.0 (p )+ 3 -heteropolymers
                2     2      1/2                               2     2
for which (hRg i/hREE i)         = 20.9Å/41.4Å = 0.50 (hRg i/hREE i = 0.25) for v = +20.0
                                    2                                           2
(blue symbols) but (hRg i/hREE2
                                      i)1/2 = 24.3/62.3 = 0.39 (hRg2 i/hREE        i = 0.15) for
                                                                    +
v = −20.0 (red symbols), and a pair of |v| = 50.0 (p )3 -heteropolymers for which
(hRg2 i/hREE
             i)1/2 = 17.6/3.7 = 4.8 (hRg2 i/hREE  2
                                                    i = 22.6) for v = +50.0 (blue symbols),
which is much higher than that of any homopolymer ensemble shown in the inset of
Fig. 3a, but (hRg2 i/hREE 2
                             i)1/2 = 24.3/62.2 = 0.39 (hRg2 i/hREE  i = 0.15) for v = −50.0 (red
symbols).

DISCUSSION

   The logic of inferring conformational ensembles from MFFs. Considered
in aggregate, the results presented above show that having a homopolymer-like MFF
is insufficient to guarantee an underlying homogeneous conformational distribution,
although having a non-homopolymer-like MFF is a good indication of a heterogeneous
ensemble. Proteins are heteropolymers. Therefore, physically, it is most intuitive to
expect disordered conformational ensembles of proteins to be heterogeneous even if,
somehow, their MFFs turn out to be homopolymer-like. Indeed, recent explicit-chain
simulations using a coarse-grained potential with a simple sidechain representation for
real IDPs have shown that such behavior is possible—as seen also in the mathematically
constructed examples we showcase above—in that conformational ensembles with as-
phericity and another shape parameter significantly different from those of homopolymer
can nonetheless exhibit scattering intensities similar to those of homopolymers127 (though
the simulation-experiment agreement is apparently closer for I(q)/I(0)–vs–q plots than
for q 2 I(q)/I(0)–vs–q (Kratky) plots reported, respectively, in Fig. 2 and Fig. S1 of
this reference). In view of this basic consideration, it would not be prudent to invoke
Occam’s razor and simply infer a homogeneous ensemble as the most parsimonious
interpretation of the SAXS data when confronted with a homopolymer-like MFF for a
disordered protein ensemble when complementary experimental techniques are available
to gain further insight into the structural properties of the ensemble.78,79,98 In this
regard, a recent statistical survey of ensembles of model heteropolymers (which are,
by construction, heterogeneous ensembles) with intrachain hydrohobic-polar (HP)-like



interactions exhibiting conformational averages of Rg and REE coupled approximately in
a manner similar to the hRg2 i–hREE  i coupling in homopolymers as well as having MFFs
not so dissimilar to those for homopolymers116 provides additional illustrations for our
thesis that MFFs alone are insufficient to clearly distinguish between heterogeneous
and homogeneous ensembles. At the same time, it should be emphasized that HP-like
interactions cover only a subset of intraprotein interactions. In fact, HP-like interactions
alone cannot produce the high degree of folding cooperativity (see below) observed
experimentally for small, single-domain proteins.25,130 As discussed above, using our
analytical theory-inspired heteropolymeric interactions—although that still neglect a
lot of other modes of intraprotein interactions, we are able to provide ample examples
of hRg2 i–hREE i decoupling in heterogeneous ensembles. From a biological/evolutionary
perspective, one should expect that any feature of conformational heterogeneity of
disordered protein ensembles—including hRg2 i–hREE   2
                                                        i decoupling—can be potentially
exploited for biological function. As researchers, it would be unwise to self-impose a
priori boundaries to box in our imagination of conformational possibilities.

   Conformational heterogeneity and physical pictures of folding cooperativity.
SAXS was instrumental in revealing an important aspect of two-state-like folding cooper-
ativity of small, single-domain proteins by observing directly, in a time-resolved manner,
that the unfolded state of Protein L is consisted of relatively open conformations (large
hRg2 i) even under strongly folding conditions.3 This finding was remarkable from a theoret-
ical perspective because common protein chain models at the time predicted a substantial
decrease of hRg2 i of the unfolded conformational ensemble when its solvent environment is
changed from strongly unfolding (as in high denaturant) to strongly folding (as in low or
no denaturant). Two-state folding/unfolding cooperativity has since been found to be in-
timately related25 to contact-order-dependent folding rates131 and linear chevron plots, as
protein chain models with reduced cooperativity—hallmarked by an appreciable decrease
in unfolded-state hRg2 i with increasingly strong folding conditions—failed to reproduce
these experimental features.25,132,133 This early success in applying folding cooperativity—
with unfolded states with large conformational dimensions minimally affected by folding
conditions—as a basic, unifying rationalization of the defining experimentally observed
features in the folding of small, single-domain proteins has led some researchers to an
extreme view of two-state folding cooperativity known as the topomer search model of
protein folding.134 In this view, the unfolded state of a globular protein is envisioned as
behaving like—and thus modeled by—homopolymeric Gaussian chains without excluded
volume, and folding is stipulated to be achieved by random diffusive searching of a “native
topomer” among these conformations.134 Apparently, the rationale of this perspective is
that experimental observations, such as SAXS data, that the authors interpreted as im-



plying a homogeneous ensemble of open unfolded conformations—with excluded volume
or not—should take precedence over any theoretical concern as to how the existence of
such an ensemble may follow from current understanding of the driving forces for pro-
tein folding. In other words, if commonly accepted physical interactions cannot account
for what the authors viewed as experimental facts about the homopolymer-like unfolded-
state ensemble, the fault is with common theoretical understanding; and, therefore, rather
than casting doubt on the topomer search model as physically unrealizable, it is the com-
monly accepted theoretical understanding of protein folding driving forces that needs to
be revised and improved.
   A contrasting philosophy, which might be common among theoreticians, is to place
more trust on current theoretical notions about protein folding driving forces and accept
them as approximately correct. Researchers subscribing to this line of thinking tend to
emphasize interpreting experimental data in terms of what is perceived to be physically
plausible; thus the accuracies of experiments that appear inconsistent with pre-conceived
notions of physical interactions are often questioned. As it stands, explicit-chain het-
eropolymeric protein models embodying current notions of physical interactions—even
when common structurally-specific native-centric models are included—possess less overall
folding cooperativity than that of many real, small, single-domain proteins.135 In partic-
ular, these heteropolymer models entail unfolded conformations with decreased average
Rg with stronger folding conditions.136 While this explicit-chain heteropolymer model-
predicted picture was apparently at odds with inferences from SAXS experiment3 and
in-depth understanding of calorimetric two-state folding cooperativity,25,27,137,138 it was ap-
parently supported by smFRET experiments on Protein L for which decreasing hRg2 i with
decreasing denaturant was inferred using an interpretation of smFRET data (which mea-
sured hREE i but not hRg2 i directly) that assumed homopolymeric hRg2 i–hREE  2
                                                                                 i coupling.9
   In our estimation, an awareness of this historical background is contextually useful for
appreciating the different investigative logic and contrasting conceptual emphases in the
controversy surrounding the apparent mismatch of smFRET- versus SAXS-determined
conformational dimensions of protein disordered states.59,62,66,74,76

    A “near-Levinthal” scenario of cooperative protein folding. A synthesis of the
useful insights from the two above-described approaches needs to consider the following.
First, as a proposed physical mechanism, the topomer search model—which assumes that
an unfolded protein state is a noninteracting homogeneous ensemble—is untenable be-
cause this hypothetical mechanism entails a kinetically impossible Levinthal search when
excluded volume of the chains are (as it should be) taken into account.139 Nonetheless, the
discourse inspired by the model’s emphasis on the high degrees of folding cooperativity
is valuable because a comprehensive theoretical understanding of physical interactions in



protein folding should be able to account for this experimental property. Second, explicit-
chain heteropolymer models of protein disordered states are valuable in underscoring the
sequence-dependent heterogeneous nature of these conformational ensemble. However, it
is important to recognize the limitations of current understanding of the solvent-mediated
protein interactions.48,49 A case in point is that even native-centric models with only pair-
wise interactions cannot reproduce the high degree of folding cooperativity of Protein L,29
and that yet-undiscovered non-parwise-additive many-body effects, such as local-nonlocal
coupling, are possibly implicated in protein folding cooperativity.27,133
    A conceptual picture of cooperative folding that takes all these considerations into
account is referred to as a “near-Levinthal” scenario.140 This picture of folding expects,
because of basic physics, that the unfolded state is a heterogeneous ensemble and that
conformational search during folding must experience a certain bias toward the native
structure because in the absence of any bias, folding would be kinetically impossible
(Levinthal’s paradox). At the same time, it is stipulated that the bias, though not
nonexistent, is relatively weak because if the bias is strong—implying that intrachain
interactions are strongly favorable—the unfolded state under folding conditions would
be a relatively compact conformational ensemble rather than the open conformational
ensemble observed experimentally. Finally, in this “near-Levinthal” picture of folding,
the folded state is envisioned to be thermodynamically stabilized by certain strongly
favorable interactions, perhaps via many-body mechanisms such as the proposed local-
nonlocal coupling effects, that are operative only after the protein has crossed to the
folded side of the transition-state free energy barrier but not in the unfolded state.27
Recent advances in smFRET data interpretation and SAXS experiments lend credence
to this picture: First, it is now recognized that a larger hRg2 i1/2 can be consistent with
smFRET data on protein unfolded state because of possible hRg2 i–hREE        i decoupling in
heterogeneous ensembles. Second, more accurate SAXS measurements indicate a small
contraction of unfolded-state ensembles when denaturant concentration is reduced,93
indicating that denaturant-dependent favorable intrachain interactions are present in the
unfolded state. Given that these interactions should be sequence-dependent, this SAXS
observation is likely indicative of a heterogeneous unfolded-state ensemble.

   Water as solvent for proteins. The SAXS-observed phenomenon that the unfolded
states of many globular proteins remain quite open even under strongly folding conditions
(as in water), which is a hallmark of protein folding cooperativity, has recently been cast
in terms of “water is a good solvent for the unfolded states of many proteins”.141 While
this narrative may serve to highlight the different solvation properties of homopolymeric
versus evolved heteropolymeric disordered protein states and the rhetoric may focus
attention on the important ramifications of folding/unfolding cooperativity as emphasized



in the above discussion (and in references thereof) as well as by the authors of this
review,141 application of “solubility” to a state, i.e., a subpopulation, of a molecular
species rather than the total population of the molecular species as a whole may not
enhance conceptual clarity. In the conventional meaning of the term, solubility of a
solute in a solvent refers to the global miscibility of the solvent and the solute, not
a subpopulation of the solute. While the unfolded chains of a soluble protein is, by
definition, solvated to various degree, only a very small fraction of the chain population
is unfolded under the strongly folding conditions of pure water. Now, if one applies the
same nomenclatural logic in ref. 141 that water is a good solvent of unfolded states of
some proteins to a more mundane system of nonpolar solutes and water, one can arrive
at a tautological, and thus uninformative, proposition that water is a good solvent for the
solvated state of the nonpolar solute (i.e., the minute solvated fraction of the nonpolar
substance) even when the overwhelming population of the substance is not solvated and
the substance is practically insoluble. In this regard, describing the role of hydrophobicity
in protein folding by the traditional dictum “water is a poor solvent for the unfolded
state of globular proteins” is less problematic because, semantically consistent with the
“poor solvent” characterization, an overwhelming majority of the chain population is
folded (i.e., not “solvated” as unfolded chains) in water. Nonetheless, the “poor solvent”
narrative can also be misleading. This is because in this case poor solvation in water
applies only to part of the protein molecule (e.g., nonpolar residues) but not every part
of the heteropolymeric protein chain. In fact, globular proteins are soluble as individual
folded molecules in water. In other words, water is a good—not poor—solvent for
the individual protein molecules as a whole. Unqualified usage of the “poor solvent”
description may therefore mask important biophysical and functional distinctions among
disordered protein states of different compactness,141 differences that are crucial for
categorizing noncooperative and various types of cooperative folding.25,27,137 Taking all
the above into consideration, it is apparent that invocation of aqueous solubility of
subpopulations of a protein’s conformational ensemble risk unnecessary confusion and
such narratives are not always conducive to a clear conceptualization of protein folding.

   Composite ensembles and experimental uncertainties. As emphasized above, in
addition to the cases studied so far by us and by others, one expects that there are many
other scenarios in which heterogeneous ensembles are not readily distinguishable from
homopolymer ensembles by MFFs alone. As a further example, consider a heterogeneous
ensemble which is a superposition of two homogeneous ensembles defined by two different
                          (1)       (2)
p values symbolized as p and p . A situation similar to this hypothetical scenario
readily arise when there is a mixture of folded and unfolded protein conformations in
an overall ensemble,3,98 or when there is a bimodal-like distribution of conformational




                                            (a)                                   (b)


                         C


FIG. 21: MFFs of composite ensembles. (a) Dimensionless Kratky plots of the C =
                                                (1)              (2)
0.1, 0.2, . . . , 0.9 composite ensembles with p = +2.0 and p = −2.0 (Eq. 46) with differ-
ent overall hRg2 i1/2 values (inset) are plotted using the same color code. Dimensionless Kratky
                             (1)                                                        (2)
plots for the homogeneous p = +2.0 (C = 1.0, dark blue) and the homogeneous p = −2.0
(C = 0, red) ensembles are shown by thicker curves. (b) Dimensionless Kratky plot for C = 0.1
(solid curve) heteropolymeric composite ensemble (overall hRg2 i1/2 = 18.3 Å) is compared with
that for the p = −1.8 homogeneous ensemble with hRg2 i1/2 = 18.5 Å (dashed curve). The
I(q)s of the C-dependent heterogeneous ensembles in (a) are also compared using other plotting
formats in Fig. S7 of Supporting Information.


properties of an IDP, as has been suggested computationally.17 Now, let the hRg2 i of
the two component homogeneous ensembles be hRg2 i(1) and hRg2 i(2) , respectively, and the
corresponding be scattering intensities be I (1) (q) and I (2) (q). The hRg2 i of a composite
                                                                      (1)        (2)
conformational ensemble with weights of C and 1 − C for the p - and p -ensembles
(0 ≤ C ≤ 1), respectively, is then given by

                             hRg2 i = ChRg2 i(1) + (1 − C)hRg2 i(2) ,                         (45)

and the corresponding scattering intensity is given by

                              I(q) = CI (1) (q) + (1 − C)I (2) (q) ,                          (46)

and I0 = CI (1) (0) + (1 − C)I (2) (0). The SAXS signatures of such a system are shown
in Fig. 21. A comparison is highlighted in Fig. 21b between the MFF of a C = 0.1
heterogeneous composite ensemble (solid curve) and that of a homopolymer ensemble
with the same hRg2 i1/2 (dashed curve). The result indicates that the two theoretical
MFFs are distinct and therefore distinguishable in principle, especially in situation
where a mixture of conformational species is expected as in the study of protein
folding/unfolding.3,98 At the same time, the similarity between the MFFs also suggests



that the heterogeneous and homogeneous ensembles may not be easily discriminated by
their MFFs alone without prior knowledge of a complex conformational distribution and
in the face of possible experimental uncertainties.136 The theoretical approach we have
taken here is agnostic as to experimental accuracy, using a coarse-grained chain model
without atomistic details and ignoring any explicit consideration of solvation effects
for the purpose of exploring conceptual principles. Nonetheless, it is worth mentioning
that some of the fitted homopolymeric MFFs for disordered protein ensembles reported
in the literature exhibit significant deviations from experimental data for q values
not much larger than those in the shoulder region of the dimensionless Kratky plot
(e.g., the [KCl] = 0.15 M data in Fig. 3C of ref. 93 and Fig. S5 in ref. 116). Other
effects, such as those associated with the hydration shell around the protein,142 may add
further uncertainties in matching simulated and experimental MFFs and thus render the
inference of conformational ensembles from MFFs more challenging.

CONCLUSIONS

   To recapitulate, basic physics stipulates that disordered conformational ensembles of
unfolded proteins and IDPs are, in general, heterogeneous because proteins are heteropoly-
mers of amino acid residues. MFFs obtained from SAXS of disordered protein ensembles
are valuable because they yield more structural information about conformational en-
sembles from higher-q parts of I(q), whereas this information is unavailable from small-q
Guinier analyses which afford only an overall hRg2 i (refs. 93–96). Nonetheless, structural
information from MFFs is still highly averaged. As exemplified by recent simulation of
several IDPs,127 the systematic analysis conducted in the present work has shown that the
MFF of a heterogeneous ensemble is not always distinct from that of a homogeneous en-
semble. In not a few instances, MFFs cannot reliably distinguish between heterogeneous
from homogeneous disordered conformational ensembles with the same hRg2 i. Clearly,
then, the conformational ensemble to MFF correspondence is practically a many-to-one
mapping. Not only that, this mapping is likely not smooth—meaning that while small
changes in conformational ensemble lead to only small changes in MFF, small changes
or experimentally indiscernible minute changes in MFF can map to structurally drasti-
cally different conformational ensembles. We have now demonstrated, mathematically,
the many-to-one and non-smooth features of the (ensemble → MFF) mapping by identi-
fying various heterogeneous ensembles with MFFs very similar to those of homopogeneous
ensembles. These heterogeneous ensembles with homopolymer-like MFFs include some
of the conformationally highly restricted (Rg , REE ) subensembles76,77,97 which may be
viewed as members of a conformational-space basis set (Figs. 7–9), computationally se-
lected reweighted ensembles with exceptionally similar MFFs but significanty different



distributions of Rg2 , REE , and asphericity (Fig. 13) as well as intuitively plausible ensem-
bles with narrower-than-SAW distributions of Rg2 and compact-open composite ensembles
(Figs. 10 and 21). These counterexamples to any preconception or tacit assumption of
a one-to-one ensemble-MFF mapping highlight the intrinsic logical uncertainty when one
attempts to infer a conformational ensemble from a given MFF.
    In view of the limited current knowledge about the effects of the sequence-
dependent15,143 physical interactions on conformational dimensions and other structural
properties of IDPs and unfolded states of cooperatively-folding globular proteins,27,48,49 it
is not possible to determine a priori which ensemble/structural properties of disordered
proteins are physically encodable by amino acid sequences and which properties are not.
As our ability to imagine what is physically possible for disordered protein conformations
is so limited because of this lack of knowledge, aside from obvious cases, one cannot
preclude many of the heterogeous ensembles with homopolymer-like MFFs as physically
unrealizable. Therefore, the logico-mathematical uncertainty that we have established
regarding any inference of conformational ensemble that is based solely on MFFs
translates into a practical uncertainty as well. With this understanding in mind, caution
should be used in not over-emphasizing the intrachain distance scaling exponent ν—
which, as it stands, is a fitting parameter that is not measured directly—as a proxy
for Rg in SAXS data analysis of protein disordered ensembles93 because it may lead to
a misplaced impression that the ensembles in question are homopolymer-like in every
respect (Fig. 8), a view whose validty is physically unlikely if not corroborated by other
measurements.98 Indeed, our simulations presented above of analytical theory-inspired
explicit-chain models with heteropolymeric interactions (Figs. 17–20) have provided
ample examples of Rg –REE decoupling in disordered conformational ensembles,77,78
even though our coarse-grained modeling with only short spatial range contact-like
interactions has not yet explored potentially much more complex and diverse impacts on
conformational preference that may emerge from sidechain sterics, hydrogen bonding,
π-related interactions, electrostatic interactions with longer spatial ranges, and solvation
effects. Taken together, our findings underscore the importance of using multiple
complementary experimental probes to gain insight into disordered protein ensembles,
as exemplified by recent efforts in using combined data from SAXS, NMR and smFRET
to provide more extended structural information about such ensembles which turn
out—according to multiple-probe analyses—to be heterogeneous.64,78,79,92,98 Considering
the vast possibilities of amino acid sequence-encoded conformational ensembles, these
promising advances have only begun to uncover the intricacy of disordered biomolecular
configurations and how they might underpin biological functions.



Supporting Information Description
Relationship between the present heteropolymeric scattering intensity in Eqs. 12, 13 and
previous results for homopolymers, and supporting figures.

The authors declare no competing financial interest.

Acknowledgements
We thank Yawen Bai, Upayan Baul, Robert Best, Osman Bilsel, Patricia Clark, Julie
Forman-Kay, Kingshuk Ghosh, Gregory-Neal Gomes, Claudiu Gradinaru, Elisha Haas,
Alex Holehouse, Ed Lattman, Edward Lemke, Yi-Hsuan Lin, Jeetain Mittal, Rohit
Pappu, Kevin Plaxco, Joshua Riback, Ben Schuler, Andrea Soranno, Tobin Sosnick,
Dev Thirumalai, Sara Vaiana, and Wenwei Zheng for helpful discussions, some over
many years. Part of these fruitful exchanges took place during workshops organized
by the Protein Folding and Dynamics Research Coordination Network funded by the
U.S. National Science Foundation (NSF grant MCB 1516959 to C. R. Matthews) and
Biophysical Society Meetings.144,145 Financial support of this work was provided by
Canadian Institutes of Health Research grants MOP-84281, NJT-155930, Natural Sci-
ences and Engineering Research Council of Canada Discovery grant RGPIN-2018-04351
to H.S.C., and National Natural Science Foundation of China grant 21674055 to J.S. Part
of our computational resources has been afforded generously by Compute/Calcul Canada.


References

 1   Sosnick, T. R.; Trewhella, J. Denatured states of ribonuclease A have compact dimensions
     and residual secondary structure. Biochemistry 1992, 31, 8329–8335.
 2   Zhang, O.; Forman-Kay, J. D. Structural characterization of folded and unfolded states of
     an SH3 domain in equilibrium in aqueous buffer. Biochemistry 1995, 34, 6784–6794.
 3   Plaxco, K. W.; Millet, I. S.; Segel, D. J.; Doniach, S.; Baker, D. Polypeptide chain collapse
     can occur concomitantly with the rate limiting step in protein folding. Nat. Struct. Biol.
     1999, 6, 554–557.
 4   Shortle, D.; Ackerman, M. S. Persistence of native-like topology in a denatured protein in
     8 M urea. Science 2001, 293, 487–489.
 5   Shimizu, S.; Chan, H. S. Origins of protein denatured state compactness and hydrophobic
     clustering in aqueous urea: Inferences from nonpolar potentials of mean force. Proteins
     2002, 49, 560–566.
 6   Jacob, J.; Krantz, B.; Dothager, R. S.; Thiyagarajan, P.; Sosnick, T. R. Early collapse is



     not an obligate step in protein folding. J. Mol. Biol. 2004, 338, 369–382.
7    Kohn, J. E.; Millett, I. S.; Jacob, J.; Zagrovic, B.; Dillon, T. M.; Cingel, N.; Dothager, R.
     S.; Seifert, S.; Thiyagarajan, P.; Sosnick, T. R.; Hasan, M. Z.; Pande, V. S.; Ruczinski, I.;
     Doniach, S.; Plaxco, K. W. Random-coil behavior and the dimensions of chemically unfolded
     proteins. Proc. Natl. Acad. Sci. U.S.A. 2004, 101, 12491–12496.
8    Fitzkee, N. C.; Rose, G. D. Reassessing random-coil statistics in unfolded proteins. Proc.
     Natl. Acad. Sci. U.S.A. 2004, 101, 12497–12502.
9    Sherman, E.; Haran, G. Coil-globule transition in the denatured state of a small protein.
     Proc. Natl. Acad. Sci. U.S.A. 2006, 103, 11539–11543.
10   Merchant, K. A.; Best, R. B.; Louis, J. M.; Gopich, I. V.; Eaton, W. A. Characterizing
     the unfolded states of proteins using single-molecule FRET spectroscopy and molecular
     simulations. Proc. Natl. Acad. Sci. U.S.A. 2007, 104, 1528–1533.
11   Marsh, J. A.; Forman-Kay, J. D. Structure and disorder in an unfolded state under nonde-
     naturing conditions from ensemble models consistent with a large number of experimental
     restraints. J. Mol. Biol. 2009, 391, 359–374.
12   Meng, W.; Lyle, N.; Luan, B.; Raleigh, D. P.; Pappu, R. V. Experiments and simulations
     show how long-range contacts can form in expanded unfolded proteins with negligible sec-
     ondary structure. Proc. Natl. Acad. Sci. U.S.A. 2013, 110, 2123–2128.
13   Stenzoski, N. E.; Luan, B.; Holehouse, A. S.; Raleigh, D. P. The unfolded state of the C-
     terminal domain of L9 expands at low but not at elevated temperatures. Biophys. J. 2018
     115, 655–663.
14   Borg, M.; Mittag, T.; Pawson, T.; Tyers, M.; Forman-Kay, J. D.; Chan, H. S. Polyelectro-
     static interactions of disordered ligands suggest a physical basis for ultrasensitivity. Proc.
     Natl. Acad. Sci. U.S.A. 2007, 104, 9650–9655.
15   Mittag, T.; Orlicky, S.; Choy, W.-Y.; Tang, X.; Lin, H.; Sicheri, F.; Kay, L. E.; Tyers, M.;
     Forman-Kay, J. D. Dynamic equilibrium engagement of a polyvalent ligand with a single-site
     receptor. Proc. Natl. Acad. Sci. U.S.A. 2008, 105, 17772–17777.
16   Müller-Späth, S.; Soranno, A.; Hirschfeld, V.; Hofmann, H.; Rüegger, S.; Reymond, L.;
     Nettels, D.; Schuler, B. Charge interactions can dominate the dimensions of intrinsically
     disordered proteins. Proc. Natl. Acad. Sci. U.S.A. 2010, 107, 14609–14614.
17   Mittag, T., Marsh, J.; Grishaev, A.; Orlicky, S.; Lin, H.; Sicheri, F.; Tyers, M.; Forman-Kay,
     J. D. Structure/function implications in a dynamic complex of the intrinsically disordered
     Sic1 with the Cdc4 subunit of an SCF ubiquitin ligase. Structure 2010, 18, 494–506.
18   Fuxreiter, M.; Tompa, P. Fuzzy complexes: a more stochastic view of protein function. Adv.
     Exp. Med. Biol. 2012, 725, 1–14.
19   Marsh, J. A.; Teichmann, S. A.; Forman-Kay, J. D. Probing the diverse landscape of protein
     flexibility and binding. Curr. Opin. Struct. Biol. 2012, 22, 643–650.



20   Liu, B.; Chia, D.; Csizmok, V.; Farber, P.; Forman-Kay, J. D.; Gradinaru, C. C. The effect
     of intrachin electrostatic repulsion on conformational disorder and dynamics of the Sic1
     protein. J. Phys. Chem. B 2014, 118, 4088–4097.
21   Martin, E. W.; Holehouse, A. S.; Grace, C. R.; Hughes, A.; Pappu, R. V.; Mittag, T.
     Sequence determinants of the conformational properties of an intrinsically disordered protein
     prior to and upon multisite phosphorylation. J. Am. Chem. Soc. 2016, 138, 15323–15335.
22   Li, M.; Liu, Z. Dimensions, energetics, and denaturant effects of the protein unstructured
     state. Protein Sci. 2016, 25, 734–747.
23   Li, M.; Sun, T.; Jin, F.; Yu, D.; Liu, Z. Dimension conversion and scaling of disordered
     protein chains. Mol. Biosyst. 2016, 12, 2932–2940.
24   Holehouse, A. S.; Pappu, R. V. Collapse transitions of proteins and the interplay among
     backbone, sidechain, and solvent interactions. Annu. Rev. Biophys. 2018, 47, 19–39.
25   Chan, H. S.; Shimizu, S.; Kaya, H. Cooperativity principles in protein folding. Methods
     Enzymol. 2004, 380, 350–379.
26   Huang, F.; Ying, L.; Fersht, A. R. Direct observation of barrier-limited folding of BBL by
     single-molecule fluorescence resonance energy transfer. Proc. Natl. Acad. Sci. U.S.A. 2009,
     106, 16239–16244.
27   Chan, H. S.; Zhang, Z.; Wallin, S.; Liu, Z. Cooperativity, local-nonlocal coupling, and
     nonnative interactions: Principles of protein folding from coarse-grained models. Annu.
     Rev. Phys. Chem. 2011, 62, 301–326.
28   Liu, J.; Campos, L. A.; Cerminara, M.; Wang, X.; Ramanathan, R.; English, D. S.; Muñoz,
     V. Exploring one-state downhill protein folding in single molecules. Proc. Natl. Acad. Sci.
     U.S.A. 2012, 109, 179–184.
29   Chen, T.; Chan, H. S. Effects of desolvation barriers and sidechains on local-nonlocal cou-
     pling and chevron behaviors in coarse-grained models of protein folding. Phys. Chem. Chem.
     Phys. 2014, 16, 6460–6479.
30   Maity, H.; Reddy, G. Folding of Protein L with implications for collapse in the denatured
     state ensemble. J. Am. Chem. Soc. 2016, 138, 2609–2616.
31   Thirumalai, D.; Samanta, H. S.; Maity, H.; Reddy, G. Universal nature of collapsibility in
     the context of protein folding and evolution. Trends Biochem. Sci. 2019, 44, 675–687.
32   Shoemaker, B. A.; Portman, J. J.; Wolynes, P. G. Speeding molecular recognition by using
     the folding funnel: The fly-casting mechanism. Proc. Natl. Acad. Sci. U.S.A. 2000, 97,
     8868–8873.
33   Huang, Y.; Liu, Z. Kinetic advantage of intrinsically disordered proteins in coupled folding-
     binding process: a critical assessment of the “fly-casting” mechanism. J. Mol. Biol. 2009,
     393, 1143–1159.
34   Csizmok, V.; Orlicky, S.; Cheng, J.; Song, J.; Bah, A.; Delgoshaie, N.; Lin, H.; Mittag,



     T.; Sicheri, F.; Chan, H. S.; Tyers, M.; Forman-Kay, J. D. An allosteric conduit facilitates
     dynamic multisite substrate recognition by the SCFCdc4 ubiquitin ligase. Nat. Comm. 2017,
     8, 13943.
35   Sigalov, A. B.; Zhuravleva, A. V.; Orekhov, V. Yu. Binding of intrinsically disordered pro-
     teins is not necessarily accompanied by a structural transition to a folded form. Biochimie
     2007, 89, 419–421.
36   Danielsson, J.; Liljedahl, L.; Bárány-Wallje, L.; Sønderby, P.; Kristensen, L. H.; Martinez-
     Yamout, M. A.; Dyson, H. J.; Wright, P. E.; Poulsen, F. M.; Mäler, L.; Gräslund, A.;
     Kragelund, B. B. The intrinsically disordered RNR inhibitor Sml1 is a dynamic dimer.
     Biochemistry 2008, 47, 13428–13437.
37   Nourse, A.; Mittag, T. The cytoplasmic domain of the T-cell receptor zeta subunit does not
     form disordered dimers. J. Mol. Biol., 2014, 426, 62–70.
38   Sigalov, A. B. Structural biology of intrinsically disordered proteins: Revisiting unsolved
     mysteries. Biochimie, 2016, 125, 112–118.
39   Wu, S.; Wang, D.; Liu, J.; Feng, Y.; Weng, J;.; Li, Y.; Gao, X.; Liu, J.; Wang, W. The
     dynamic multisite interactions between two intrinsically disordered proteins. Angew. Chem.
     Int. Ed. 2017, 56, 7515—7519.
40   Amin, A. N.; Lin, Y.-H.; Das, S.; Chan, H. S. Analytical theory for sequence-specific binary
     fuzzy complexes of charged intrinsically disordered proteins. J. Phys. Chem. B 2020, 124,
     6709–6720.
41   Shin, Y.; Brangwynne, C.P. Liquid phase condensation in cell physiology and disease. Sci-
     ence 2017, 357, eaaf4382.
42   Banani, S. F.; Lee, H. O.; Hyman, A. A.; Rosen, M. K. Biomolecular condensates: organizers
     of cellular biochemistry. Nat. Rev. Mol. Cell Biol. 2017, 18, 285–298.
43   Lin, Y.-H.; Forman-Kay, J. D.; Chan, H. S. Theories for sequence-dependent phase behaviors
     of biomolecular condensates. Biochemistry 2018, 57, 2499–2508.
44   Lin, Y.-H.; Chan, H. S. Phase separation and single-chain compactness of charged disordered
     proteins are strongly correlated. Biophys, J. 2017, 112, 2043–2046.
45   Dignon, G. L.; Zheng, W.; Best, R. B.; Kim, Y. C.; Mittal, J. Relation between single-
     molecule properties and phase behavior of intrinsically disordered proteins. Proc. Natl. Acad.
     Sci. U.S.A. 2018, 115, 9929–9934.
46   McCarty, J.; Delaney, K. T.; Danielsen, S. P. O.; Fredrickson, G. H.; Shea, J.-E. Complete
     phase diagram for liquid-liquid phase separation of intrinsically disordered proteins. J. Phys.
     Chem. Lett. 2019, 10, 1644–1652.
47   Zeng, X.; Holehouse, A. S.; Mittag, T.; Chilkoti, A.; Pappu, R. V. Connecting coil-to-
     globule transitions to full phase diagrams for intrinsically disordered proteins. Biophys. J.
     2020, 119, 402–418.



48   Piana, S.; Klepeis, J. L.; Shaw, D. E. Assessing the accuracy of physical models used in
     protein-folding simulations: Quantitative evidence from long molecular dynamics simula-
     tions. Curr. Opin. Struct. Biol. 2014, 24, 98–105.
49   Chen, T.; Song, J.; Chan, H. S. Theoretical perspectives on nonnative interactions and
     intrinsic disorder in protein folding and binding. Curr. Opin. Struct. Biol. 2015, 30, 32–42.
50   Rauscher, S.; Gapsys, V.; Gajda, M. J.; Zweckstetter, M.; de Groot, B. L.; Grubmüller, H.
     Structural ensembles of intrinsically disordered proteins depend strongly on force field: A
     comparison to experiment. J. Chem. Theor. Comput. 2015, 11, 5513–5524.
51   Huang, J.; Rauscher, S.; Nawrocki, G.; Ran, T.; Feig, M.; de Groot, B. L.; Grubmüller, H.;
     MacKerell, A. D. Jr. CHARMM36m: An improved force field for folded and intrinsically
     disordered proteins. Nat. Methods 2017 14, 71–73.
52   Best, R. B. Computational and theoretical advances in studies of intrinsically disordered
     proteins. Curr. Opin. Struct. Biol. 2017, 42, 147–154.
53   Levine, Z. A.; Shea, J.-E. Simulations of disordered proteins and systems with conforma-
     tional heterogeneity. Curr. Opin. Struct. Biol. 2017, 43, 95–103.
54   Robustelli, P.; Piana, S.; Shaw, D. E. Developing a molecular dynamics force field for both
     folded and disordered protein states. Proc. Natl. Acad. Sci. U.S.A. 2018, 115, E4758–E4766.
55   Shea, J.-E.; Best, R. B.; Mittal, J. Physics-based computational and theoretical approaches
     to intrinsically disordered proteins. Curr. Opin. Struct. Biol. 2021, 67, 219–225.
56   Doniach, S. Changes in biomolecular conformation seen by small angle X-ray scattering.
     Chem. Rev. 2001, 101, 1763–1778.
57   Schindler, C. E. M.; de Vries, S. J.; Sasse, A.; Zacharias, M. SAXS data alone can generate
     high-quality models of protein-protein complexes. Structure 2016, 24, 1387–1397.
58   Meisburger, S. P.; Thomas, W. C.; Watkins, M. B.; Ando, N. X-ray scattering studies of
     protein structural dynamics. Chem. Rev. 2017, 117, 7615–7672.
59   Yoo, T. Y.; Meisburger, S. P.; Hinshaw, J.; Pollack, L.; Haran, G.; Sosnick, T. R.; Plaxco,
     K. Small-angle x-ray scattering and single-molecule FRET spectroscopy produce highly
     divergent views of the low-denaturant unfolded state. J. Mol. Biol. 2012, 418, 226–236.
60   Kathuria, S. V.; Kayatekin, C.; Barrea, R.; Kondrashkina, E.; Graceffa, R.; Guo, L.; No-
     brega, R. P.; Chakravarthy, S.; Matthews, C. R.; Irving, T. C.; Bilsel, O. Microsecond
     barrier-limited chain collapse observed by time-resolved FRET and SAXS. J. Mol. Biol.
     2014, 426, 1980–1994.
61   Kikhney, A. G.; Svergun, D. I. A practical guide to small angle X-ray scattering (SAXS) of
     flexible and intrinsically disordered proteins. FEBS Lett. 2015, 589, 2570–2577.
62   Watkins, H. M.; Simon, A. J.; Sosnick, T. R.; Lipman, E. A.; Hjelm, R. P.; Plaxco, K.
     W. Random coil negative control reproduces the discrepancy between scattering and FRET
     measurements of denatured protein dimensions. Proc. Natl. Acad. Sci. U.S.A. 2015, 112,



     6631–6636.
63   Antonov, L. D.; Ollsson, S.; Boomsma, W.; Hamelryck, T. Bayesian inference of protein
     ensembles from SAXS data. Phys. Chem. Chem. Phys. 2016, 18, 5832–5838.
64   Aznauryan, M.; Delgado, L.; Soranno, A.; Nettels, D. ; Huang, J.; Labhardt, A. M.; Grze-
     siek, S.; Schuler, B. Comprehensive structural and dynamical view of an unfolded protein
     from the combination of single-molecule FRET, NMR, and SAXS. Proc. Natl. Acad. Sci.
     U.S.A. 2016, 113, E5389–E5398.
65   Martin, E. W.; Hopkins, J. B.; Mittag, T. Small-angle X-ray scattering experiments of
     monodisperse intrinsically disordered protein samples close to the solubility limit. Methods
     Enzymol. 2021, 646, 185–222.
66   Haran, G. How, when and why protein collapse: The relation to folding. Curr. Opin. Struct.
     Biol. 2012, 22, 14–20.
67   Schuler, B.; Hofmann, H. Single-molecule spectroscopy of protein folding dynamics—
     expanding scope and timescales. Curr. Opin. Struct. Biol. 2013, 23, 36–47.
68   Juette, M. F.; Terry, D. S.; Wasserman, M. R.; Zhou, Z.; Altman, R. B.; Zheng, Q.;
     Blanchard, S. C. The bright future of single-molecule fluorescence imaging. Curr. Opin.
     Struct. Biol. 2014, 20, 103–111.
69   Elbaum-Garfinkle, S.; Cobb, G.; Compton, J. T.; Li, X.-H.; Rhoades E. Tau mutants bind
     tubulin heterodimers with enhanced affinity. Proc. Natl. Acad. Sci. U.S.A. 2014, 111, 6311–
     6316.
70   Banerjee, P. R.; Deniz, A, A. Shedding light on protein folding landscapes by single-molecule
     fluorescence. Chem. Soc. Rev. 2014, 43, 1172–1188.
71   König, I.; Zarrine-Afsar, A.; Aznauryan, M.; Soranno, A.; Wunderlich, B.; Dingfelder, F.;
     Stüber, J. C.; Plückthun, A.; Nettels, D.; Schuler, B. Single-molecule spectroscopy of protein
     conformational dynamics in live eukaryotic cells. Nature Methods 2015, 12, 773–779.
72   Melo, A. M.; Coraor, J.; Alpha-Cobb, G.; Elbaum-Garfinkle, S.; Nath, A.; Rhoades, E.
     A functional role for intrinsic disorder in the tau-tubulin complex. Proc. Natl. Acad. Sci.
     U.S.A. 2016, 113, 14336–14341.
73   Schuler, B., Soranno, A.; Hofmann, H.; Nettels, D. Single-molecule FRET spectroscopy and
     the polymer physics of unfolded and intrinsically disordered proteins. Annu. Rev. Biophys.
     2016, 45, 207–231.
74   O’Brien, E. P.; Morrison, G.; Brooks, B. R.; Thirumalai, D. How accurate are polymer
     models in the analysis of Förster resonance energy transfer experiments on proteins? J.
     Chem. Phys. 2009, 130, 124903.
75   Hofmann, H.; Nettels, D.; Schuler, B. Single-molecule spectroscopy of the unexpected col-
     lapse of an unfolded protein at low pH. J. Chem. Phys. 2013, 139, 121930.
76   Song, J.; Gomes, G.-N.; Gradinaru, C. C.; Chan, H. S. An adequate account of excluded



     volume is necessary to infer compactness and asphericity of disordered proteins by Förster
     resonance energy transfer. J. Phys. Chem. B 2015, 119, 15191–15202.
77   Song, J.; Gomes, G.-N.; Shi, T.; Gradinaru, C. C.; Chan, H. S. Conformational heterogeneity
     and FRET data interpretation for dimenions of unfolded proteins. Biophys. J. 2017, 113,
     1012–1024.
78   Fuertes, G.; Banterle, N.; Ruff, K. M.; Chowdhury, A.; Mercadante, D.; Koehler, C.;
     Kachala, M.; Girona, G. E.; Milles, S.; Mishra, A.; Onck, P. R.; Gräter, F.; Esteban-Martin,
     S.; Pappu, R. V.; Svergun, D. I.; Lemke, E. A. Dcoupling of size and shape fluctuations in
     heteropolymeric sequences reconciles discrepancies in SAXS versus FRET measurements.
     Proc. Natl. Acad. Sci. U.S.A. 2017, 114, E6342–E6351.
79   Peran, I.; Holehouse, A. S.; Carrico, I. S.; Pappu, R. V.; Bilsel, O.; Raleigh, D. P. Unfolded
     states under folding conditions accommodate sequence-specific conformational preferences
     with random coil-like dimensions. Proc. Natl. Acad. Sci. U.S.A. 2019, 116, 12301–12310.
80   Domb, C.; Gillis, J.; Wilmers, G. On the shape and configuration of polymer molecules.
     Proc. Phys. Soc. (London) 1965, 85, 625–645.
81   Fisher, M. E. Shape of a self-avoiding walk or polymer chain. J. Chem. Phys. 1966, 44,
     616–622.
82   des Cloizeaux, J. Lagrangian theory for a self-avoiding random chain. Phys. Rev. A 1974,
     10, 1665–1669.
83   Oono, Y.; Ohta, T.; Freed, K. F. Application of dimensional regularization to single chain
     polymer static properties: Conformational space renormalization of polymers. III. J. Chem.
     Phys. 1981, 74, 6458–6466.
84   Zheng, W.; Zerze, G. H.; Borgia, A.; Mittal, J.; Schuler, B.; Best, R. B. Inferring properties
     of disordered chains from FRET transfer efficiencies. J. Chem. Phys. 2018, 148, 123329.
85   Zheng, W.; Best, R. B. An extended guinier analysis for intrinsically disordered proteins. J.
     Mol. Biol. 2018, 430, 2540–2553.
86   Vendruscolo, M. Determination of conformationally heterogeneous states of proteins. Curr.
     Opin. Struct. Biol. 2007, 17, 15–20.
87   Lyle, N.; Das, R. K.; Pappu, R. V. A quantitative measure for protein conformational
     heterogeneity. J. Chem. Phys. 2013, 139, 121907.
88   Ruff, K. M.; Holehouse, A. S. SAXS versus FRET: A matter of heterogeneity? Biophys. J.
     2017, 113, 971–973.
89   Best, R. B. Emerging consensus on the collapse of unfolded and intrinsically disordered
     proteins in water. Curr. Opin. Struct. Biol. 2020, 60, 27–38.
90   Mazouchi, A.; Zhang, Z.; Bahram, A.; Gomes, G.-N.; Lin, H.; Song, J.; Chan, H. S.; Forman-
     Kay, J. D.; Gradinaru, C, C. Conformations of a metastable SH3 domain characterized by
     smFRET and an excluded-volume polymer model. Biophys. J. 2016, 110, 1510–1522.



91    Gomes, G.-N.; Gradinaru, C. C. Insights into the conformations and dynamics of intrinsically
      disordered proteins using single-molecular fluorescence. Biochim. Biophys. Acta 2017, 1865,
      1696–1706.
92    Gomes, G.-N. W.; Krzeminski, M.; Namini, A.; Martin, E. W.; Mittag, T.; Head-Gordon, T.;
      Forman-Kay, J. D.; Gradinaru, C. C. Conformational ensembles of an intrinsically disordered
      protein consistent with NMR, SAXS, and single-molecule FRET. J. Am. Chem. Soc. 2020,
      142, 15697–15710.
93    Riback, J. A.; Bowman, M. A.; Zmyslowski, A. M.; Knoverek. C. R.; Jumper, J. M.;
      Hinshaw, J. R.; Kaye, E. B.; Freed, K. F.; Clark P. L.; Sosnick, T. R. Innovative scattering
      analysis shows that hydrophobic disordered proteins are expanded in water. Science 2017,
      358, 238–241.
94    Best, R. B.; Zheng, W.; Borgia, A.; Buholzer, K.; Borgia, M. B.; Hofmann, H.; Soranno,
      A.; Nettels, D.; Gast, K.; Grishaev, A.; Schuler, B. Comment on “Innovative scattering
      analysis shows that hydrophobic disordered proteins are expanded in water”. Science 2018,
      361, eaar7101.
95    Riback, J. A.; Bowman, M. A.; Zmyslowski, A. M.; Knoverek. C. R.; Jumper, J. M.; Kaye, E.
      B.; Freed, K. F.; Clark P. L.; Sosnick, T. R. Response to comment on “Innovative scattering
      analysis shows that hydrophobic disordered proteins are expanded in water”. Science 2018,
      361, eaar7949.
96    Fuertes, G.; Banterie, N.; Ruff, K. M.; Chowdhury, A.; Pappu, R. V.; Svergun, D. I.; Lemke,
      E. A. Comment on “Innovative scattering analysis shows that hydrophobic disordered pro-
      teins are expanded in water”. Science 2018, 361, eaar8230.
97    Gradinaru Lab and Chan Lab. DICE (Dimensional Inferences from Coarse-grained Ensem-
      bles), 2017. University of Toronto. http://dice.utm.utoronto.ca/
98    Stenzoski, N. E.; Zou, J.; Piserchio, A.; Ghose, R.; Holehouse, A. S.; Raleigh, D. P. The
      cold-unfolded state is expanded but contains long- and medium-range contacts and is poorly
      described by homopolymer models. Biochemistry 2020, 59, 3290–3299.
99    Fixman, M. Excluded volume in polymer chains. J. Chem. Phys. 1955, 23, 1656–1659.
100   Fixman, M. Radius of gyration of polymer chains. J. Chem. Phys. 1962, 36, 306–310.
101   Fixman, M. Radius of gyration of polymer chains. II. Segment density and excluded volume
      effects. J. Chem. Phys. 1962, 36, 3123–3129.
102   Edwards, S. F. The statistical mechanics of polymers with excluded volume. Proc. Phys.
      Soc. 1965, 85, 613–624.
103   Yamakawa, H.; Aoki, A.; Tanaka, G. Second-order perturbation theory of the mean-square
      radius of a linear polymer molecule. J. Chem. Phys. 1966, 45, 1938–1941.
104   Ohta, T.; Oono, Y.; Freed, K. F. Static scattering function for a polymer chain in a good
      solvent. Macromolecules 1981, 14, 1588–1590.



105   Freed, K. F. Renormalization Group Theory of Macromolecules; John Wiley & Sons: New
      York, NY, 1982.
106   Ohta, T.; Oono, Y.; Freed, K. F. Static-coherent-scattering function for a single polymer
      chain: Conformational space renormalization of polymers V. Phys. Rev. A. 1982, 25, 2801–
      2811.
107   Muthukumar, M.; Nickel, B. G. Perturbation theory for a polymer chain with excluded
      volume interaction. J. Chem. Phys. 1984, 80, 5839–5850.
108   Chan, H. S.; Dill, K. A. Intrachain loops in polymers: Effects of excluded volume. J. Chem.
      Phys. 1989, 90, 492–509. Erratum: J. Chem. Phys. 1992, 96, 3361.
109   Chan, H. S.; Dill, K. A. The effects of internal constraints on the configurations of chain
      molecules. J. Chem. Phys. 1990, 92, 3118–3135. Erratum: J. Chem. Phys. 1997, 107, 10353.
110   Levitt, M. A simplified representation of protein conformations for rapid simulation of pro-
      tein folding. J. Mol. Biol. 1976, 104, 59–107.
111   Metropolis, N.; Rosenbluth, A. W.; Rosenbluth, M. N.; Teller, A. H.; Teller, E. Equation of
      state calculation by fast computing machines. J. Chem. Phys. 1953, 21, 1087–1092.
112   Song, J.; Ng, S. C.; Tompa, P.; Lee, K. A. W.; Chan, H. S. Polycation-π interactions are
      a driving force for molecular recognition by an intrinsically disordered oncoprotein family.
      PLoS Comput. Biol. 2013, 9, e1003239.
113   Verdier, P. H.; Stockmayer, W. H. Monte Carlo calculations on dynamics of polymers in
      dilute solution. J. Chem. Phys. 1962, 36, 227–235.
114   Lal, M. Monte Carlo computer simulation of chain molecules. I. Mol. Phys. 1969, 17, 57–64.
115   des Cloizeaux, J. Short range correlation between elements of a long polymer in a good
      solvent. J. Physique (Paris) 1980, 41, 223–238.
116   Riback, J. A.; Bowman, M. A.; Zmyslowski, A. M.; Plaxco, K. W.; Clark P. L.; Sosnick, T.
      R. Commonly used FRET fluorophores promote collapse of an otherwise disordered protein.
      Proc. Natl. Acad. Sci. U.S.A. 2019, 116, 8889–8894.
117   Zheng, W.; Dignon, G.; Brown, M.; Kim, Y. C.; Mittal, J. Hydropathy patterning comple-
      ments charge patterning to describe conformational preferences of disordered proteins. J.
      Phys. Chem. Lett. 2020, 11, 3408–3415.
118   Schneidman-Duhovny, D.; Hammel, M.; Tainer, J. A.; Sali, A. Accurate SAXS profile com-
      putation and its assessment by contrast variation experiments. Biophys. J. 2013, 105, 962–
      974.
119   Das, R. K.; Pappu, R V. Conformations of intrinsically disordered proteins are influenced
      by linear sequence distribution of oppositely charged residues. Proc. Natl. Acad. Sci. U.S.A.
      2013, 110, 13392–13397.
120   Sawle, L.; Ghosh, K. A theoretical method to compute sequence dependent configurational
      properties in charged polymers and proteins. J. Chem. Phys. 2015, 143, 085101.



121   Huihui, J.; Ghosh, K. An analytical theory to describe sequence-specific inter-residue dis-
      tance profiles for polyampholytes and intrinsically disordered proteins. J. Chem. Phys. 2020,
      152, 161102.
122   Choy, W.-Y.; Forman-Kay, J. D. Calculation of ensembles of structures representing the
      unfolded state of an SH3 domain. J. Mol. Biol. 2001, 308, 1011–1032.
123   Kuhn, W. Über die gestalt fadenförmiger moleküle in lösungen. (Concerning the shape of
      thread shapes molecules in solution). Kolloid-Z. 1934, 68, 2–15.
124   Rudnick, J.; Gaspari, G. The asphericity of random walks. J. Phys. A 1986, 19, L191–L193.
125   Dima, R. L.; Thirumalai, D. Asymmetry in the shapes of folded and denatured states of
      proteins. J. Phys. Chem. B 2004, 108, 6564–6570.
126   Tran, H. T.; Pappu, R. V. Toward an accurate theoretical framework for describing ensem-
      bles for proteins under strongly denaturing conditions. Biophys. J. 2006, 91, 1868–1886.
127   Baul, U.; Chakraborty, D.; Mugnai, M. L.; Straub, J. E.; Thirumalai, D. Sequence effects on
      size, shape and structural heterogeneity in intrinsically disordered proteins. J. Phys. Chem.
      B 2019, 123, 3462–3474.
128   Oono, Y.; Freed, K. F. Conformation space renormalization of polymers. I. Single chain
      equilibrium properties using Wilson-type renormalization. J. Chem. Phys. 1981, 75, 993–
      1008.
129   Kosmas, M. K. On the mean radius of gyration of a polymer chain. J. Phys. A: Math. Gen.
      1981, 14, 2779–2788.
130   Chan, H. S. Modeling protein density of states: Additive hydrophobic effects are insufficient
      for calorimetric two-state cooperativity. Proteins 2000, 40, 543–571.
131   Plaxco, K. W.; Simons, K. T.; Baker, D. Contact order, transition state placement and the
      refolding rates of single domain proteins. J. Mol. Biol. 1998, 277, 985-994.
132   Chan, H. S. Protein folding: Matching speed and locality. Nature 1998, 392, 761–763.
133   Kaya, H.; Chan, H. S. Contact order dependent protein folding rates: Kinetic consequences
      of a cooperative interplay between favorable nonlocal interactions and local conformational
      preferences. Proteins 2003, 52, 524–533.
134   Makarov, D. E.; Plaxco, K. W. The topomer search model: A simple, quantitative theory
      of two-state protein folding kinetics. Protein Sci. 2003, 12, 17–26.
135   Kaya, H.; Chan, H. S. Origins of chevron rollovers in non-two-state protein folding kinetics.
      Phys. Rev. Lett. 2003, 90, 258104.
136   O’Brien, E. P.; Ziv, G.; Haran, G.; Brooks, B. R.; Thirumalai, D. Effects of denaturants
      and osmolytes on proteins are accurately predicted by the molecular transfer model. Proc.
      Natl. Acad. Sci. U.S.A. 2008 105, 13403–13408.
137   Kaya, H.; Chan, H. S. Polymer principles of protein calorimetric two-state cooperativity.
      Proteins 2000, 40, 637–661. Erratrum: Proteins 2001, 43, 523.



138   Knott, M.; Chan, H. S. Criteria for downhill protein folding: Calorimetry, chevron plot,
      kinetic relaxation, and single-molecule radius of gyration in chain models with subdued
      degrees of cooperativity. Proteins 2006, 65, 373–391.
139   Wallin, S.; Chan, H. S. A critical assessment of the topomer search model of protein folding
      using a continuum explicit-chain model with extensive conformational sampling. Protein
      Sci. 2005, 14, 1643–1660.
140   Kaya, H.; Chan, H. S. Simple two-state protein folding kinetics requires near-Levinthal
      thermodynamic cooperativity. Proteins 2003, 52, 510–523.
141   Clark, P. L.; Plaxco, K. W.; Sosnick, T. R. Water as a good solvent for unfolded proteins:
      Folding and collapse are fundamentally different. J. Mol. Biol. 2020, 432, 2882–2889.
142   Henriques, J.; Arleth, L.; Lindorff-Larsen, K.; Skepö, K. On the calculation of SAXS profiles
      of folded and intrinsically disordered proteins from computer simulations. J. Mol. Biol. 2018,
      430, 2521–2539.
143   Bowman, M. A.; Riback, J. A.; Rodriguez, A.; Guo, N.; Li, J.; Sosnick, T. R.; Clark, P. L.
      Properties of protein unfolded states suggest broad selection for expanded conformational
      ensembles. Proc. Natl. Acad. Sci. U.S.A. 2020, 117, 23356–23364.
144   Song, J.; Chan, H. S. Theoretical SAXS signatures of conformational heterogeneity and
      homogeneity of disordered protein ensembles. Biophys. J. 2019, 116, 199A.
145   Song, J.; Li, J.; Chan, H. S. SAXS signatures of conformational heterogeneity and homo-
      geneity of disordered protein ensembles. Biophys. J. 2020, 118, 503A.


                                                                      S1


          Supporting Information
                     for
  “Small-Angle X-Ray Scattering Signatures of
      Conformational Heterogeneity and
 Homogeneity of Disordered Protein Ensembles”

         Jianhui SONG1∗ , Jichen LI1 and Hue Sun CHAN2∗
   School of Polymer Science and Engineering, Qingdao University of
Science and Technology, 53 Zhengzhou Road, Qingdao 266042, China;
          Department of Biochemistry, University of Toronto,
                Toronto, Ontario M5S 1A8, Canada

                     ∗
                      Corresponding authors.
        Email: chan@arrhenius.med.utoronto.ca (H.S.C.)
                   jhsong@qust.edu.cn (J.S.)


                                                                                                               S2

Relationship Between The Heteropolymer Results In Eqs. 12 and 13 of the Main Text and
the Homopolymer Results in Ohta et al., Phys. Rev. A 1982, 25 , 2801–2811.


(The reference numbers used in the paragraph below are those in the main text. The cited references are
listed again at the bottom of this page.)


      A detailed comparison of Eq. 12 and Eq. 13 of the main text for the special case of vij = v0 against
Eqs. (3.3)–(3.8) in Ohta et al.106 indicates that the two sets of results are consistent provided that
several possible typographical errors in ref. 106 are corrected, as explained below. In this comparison, we
recognize that the present v0 is defined (see comparison in the main text with refs. 108, 109) to correspond
to v0 /(2π)d/2 = v0 (2π)−2+/2 in ref. 106, where d is the number of spatial dimensions, and  ≡ 4 − d is
a renormalization group expansion parameter, not to be confused with the intrachain interaction energy
p . Moreover, our αN = N q 2 /6 is equivalent to the variable β0 = N0 k 2 /2 in ref. 106 because our chain
length N corresponds to their “bare” chain length N0 before renormalization but our q 2 /6 is equivalent
to their k 2 /2 (k 2 = square of wave vector magnitude) because, as stated in the main text, unlike ref. 106
                                                                                                         √
and also unlike refs. 108 and 109, here we do not rescale the spatial coordinates r(τ ) to c(τ ) = dr(τ ).
The possible typographical errors in ref. 106 are: (i) the term −(~k − ~k0 )z 2 /2 in the third line of Eq. (3.3)
of ref. 106 should read −|~k − ~k0 |2 z 2 /2, (ii) an overall multiplicative factor of −v0 is likely missing in the
expression for µ on the right hand side of the first line of Eq. (3.4) in ref. 106, (iii) an overall multiplicative
factor of x/2 is likely missing in the integrand on the right hand side of Eq. (3.5) for V2 in ref. 106, and
         Rx                                                               R 1−x
(iv) the 0 dy integral in Eq. (3.6) for V31 in ref. 106 should likely be 0 dy. If these four suggested
corrections in Eqs. (3.3)–(3.6) of ref. 106 are made, the term independent of vij (first term) in our
expression for I(q) in the main-text Eq. 12 would be equal to two times the expression given by Eq. (3.2)
of ref. 106; and the vij = v0 case of the term proportional to vij in our main-text Eq. 12 can be verified
by straightforward though somewhat tedious algebra to be equal to 2(U1 + U2 + U3 + U4 + U5 + U6 ) for
d = 3 ( = 1), where the U s are defined in Eq. (3.3) of ref. 106. It should be noted that the overall factor
of 2 in our expression for I(q) arises from counting a pair of scattering positions twice instead of once,
as in Eq. (2) of ref. 104. Such an overall factor is inconsequential in the ratio I(q)/I(0). We have also
verified the linear and logarithmic a → 0 divergent terms in Eq. (3.8) of Ohta et al.106 by considering
the d = 4, vij = v0 version of the O(vij ) term in our main-text Eq. 12—which entails substituting the
         −3/2              −2
                                                             RN     R τ −a     R N −a    R N −τ
single ∆τij    factor by ∆τij —and performing the integrals a dτj 0 j dτi as 0        dτi a i d∆τij .
The resulting a → 0 (N/a → ∞) divergent term is exactly equal to two times the expression given in
Eq. (3.8) of Ohta et al.106 when our v0 corresponds to their u0 /4π 2 for d = 4 ( = 0, see above).
—————————————————————————————————————————————
    Ohta, T.; Oono, Y.; Freed, K. F. Macromolecules 1981, 14, 1588–1590.
    Ohta, T.; Oono, Y.; Freed, K. F. Phys. Rev. A 1982 25, 2801–2811.
    Chan, H. S.; Dill, K. A. J. Chem. Phys. 1989, 90, 492–509; ibid. 1992, 96, 3361.
    Chan, H. S.; Dill, K. A. J. Chem. Phys. 1990, 92, 3118–3135; ibid. 1997, 107, 10353.


                                                                                                 S3

                                 Suppporting Figures


(a)                                                   (b)


(c)                                                   (d)


FIG. S1: Comparing SAXS properties of the p = −1.0 homopolymer ensemble and (Rg , REE )
subensembles of p = 0 SAW chains. (a) The homogeneous (homopolymer) ensemble is rep-
resented by the gray area corresponding to the overall profile for p = −1.0 in Fig. 2c of the
                  2 i1/2 of this ensemble is indicated by the vertical blue solid line; the notation
main text; the hREE
follows that in Fig. 7 of the main text otherwise. Note that the subensembles marked in (a)
and analyzed in (b)–(d) here are sampled from the pure SAW (p = 0) ensemble, not from the
p = −1.0 ensemble.


                                                                                     S4

(a)                                            (b)


(c)                                            (d)


FIG. S2: Comparing SAXS properties of the p = −1.8 homopolymer ensemble and (Rg , REE )
subensembles of p = 0 SAW chains. Same notation as Fig. S1 except the full homogeneous
(homopolymer) ensemble here is for p = −1.8.


                                                                                     S5


(a)                                            (b)


(c)                                            (d)


FIG. S3: Comparing SAXS properties of the p = +2.0 homopolymer ensemble and (Rg , REE )
subensembles of p = 0 SAW chains. Same notation as Fig. S1 except the full homogeneous
(homopolymer) ensemble here is for p = +2.0.


                                                                                                 S6


              (a)          =0                                (b)          = −1.0


              (c)           = −1.8                            (d)           = −2.4


                             |i−j|                                           |i−j|
FIG. S4: Comparing the hrij   2 i1/2 vs |i − j| relationships of homogeneous (homopolymer) ensem-

bles and heteropolymeric (Rg , REE ) subensembles with essentially identical root-mean-square
radii of gyration hRg2 i1/2 . (a) Full p = 0 SAW homopolymer ensemble and its subensembles
considered in Fig. 8 of the main text. Using the same color code for the lines, the present
                       2 i1/2 as functions of |i − j| over a wider range of |i − j| than that of the
plot provides their hrij
main-text figure. (b)–(d) Select full p 6= 0 homogeneous ensembles (from Fig. 3b of the main
text) are compared with select heteropolymeric subensembles sampled from the pure p = 0
SAW homopolymer ensemble (not from an p 6= 0 ensemble) as specified by the legends. Here,
a “1D subensemble” refers to a subensemble with a narrow range of either Rg or REE but not
both, and is unrestricted otherwise; whereas a “2D subensemble” is a subensemble with narrow
ranges of Rg as well as REE .


                                                                                                 S7


        (a)                                             (b)


γ


         (c)                                            (d)


γ


                         α                                             α
FIG. S5: Extensive cataloging of SAXS properties of reweighted heterogeneous ensembles.
∆Kratky between (REE 0 , α, γ)-defined reweighted ensembles (see main text for details) and the

homogeneous SAW (p = 0) homopolymer ensemble is computed for three select REE        0 values: (a)

30 Å, (b) 60 Å, and (c,d) 90 Å, each for a 10 × 10 grid (0.01 increments) of α, γ values. Shown
here (a–d) are the resulting contour plots, with (c) and (d) for the same REE     0   = 90 Å data
plotted with different contour increments. For the systems considered, the (REE /Å, α, γ) at
the minimum ∆Kratky values encountered (approximate minimum ∆Kratky in curly brackets) are
as follows: (30, 0.01, 0.01) {0.30}, (60, 0.01, 0.1) {0.30}, and (90, 0.04, 0.05) {0.14}. Similar
analyses are performed for p = −1.0, −1.8, and +2.0 (contour plots not shown), the result-
ing minimum-∆Kratky (REE   0 /Å, α, γ) parameters and approximate minimum ∆
                                                                                   Kratky values are
(same notation as above): For p = −1.0, (22.7, 0.01, 0.01) {0.36}, (52.7, 0.01, 0.01) {0.31}, and
(82.7, 0.06, 0.06) {0.14}; for p = −1.8, (11.8, 0.02, 0.01) {0.30}, (41.8, 0.01, 0.01) {0.31}, and
(71.8, 0.07, 0.03) {0.16}; and for p = +2.0, (35.0, 0.01, 0.01) {0.30}, (65.0, 0.01, 0.01) {0.30},
and (95.0, 0.04, 0.1) {0.21}.


                                                                                                  S8

                            (a)              (b)                               (c)


                  z                                  q                                q

FIG. S6: Useful mathematical functions in the present perturbative treatment of scattering
intensities. (a) F(z) is the function defined in Eq. 13 of the main text. (b) G2 (q) is the
G2 (N, q; a) function in Eq. 28 of the main text, shown here for a variety of N and a values as
specified by the inset legend. (c) F2 (q) is the F2 (N, q; a) function in Eq. 30 of the main text for
the same set of N and a values in (b) plotted in the same line styles as those in (b).


                            (a)            (b)                              (c)


                   q                                  q                                   q

FIG. S7: SAXS properties of the homogeneous (C = 0, 1) and composite (C 6= 0, 1) ensembles
      (1)                (2)
with p = +2.0 and p = −2.0 in Fig. 21 of the main text. The color code for different C
values is identical to that in the main-text figure.
