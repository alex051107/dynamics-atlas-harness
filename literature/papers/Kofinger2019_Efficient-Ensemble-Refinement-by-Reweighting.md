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
