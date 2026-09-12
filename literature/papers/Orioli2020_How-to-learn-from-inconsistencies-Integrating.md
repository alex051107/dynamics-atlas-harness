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
