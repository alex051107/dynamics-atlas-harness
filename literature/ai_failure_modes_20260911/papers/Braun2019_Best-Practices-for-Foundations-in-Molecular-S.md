# Best Practices for Foundations in Molecular Simulations [Article v1.0]

**Authors:** Efrem Braun, Justin Gilmer, Heather B. Mayes, David L. Mobley, Jacob I. Monroe, Samarjeet Prasad, Daniel M. Zuckerman
**Year:** 2019
**Venue:** Living Journal of Computational Molecular Science
**DOI:** 10.33011/livecoms.1.1.5957
**Source PDF URL:** https://livecomsjournal.org/index.php/livecoms/article/download/v1i1e5957/939
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


This LiveCoMS document is      Abstract This document provides a starting point for approaching molecular simulations, guiding
maintained online on
                               beginning practitioners to what issues they need to know about before and while starting their ﬁrst
GitHub at https:
//github.com/MobleyLab/        simulations, and why those issues are so critical. This document makes no claims to provide an
basic_simulation_training;     adequate introduction to the subject on its own. Instead, our goal is to help people know what
to provide feedback,
                               issues are critical before beginning, and to provide references to good resources on those topics. We
suggestions, or help
improve it, please visit the   also provide a checklist of key issues to consider before and while setting up molecular simulations
GitHub repository and          which may serve as a foundation for other best practices documents.
participate via the issue
tracker.

This version dated
December 29, 2018
                               *For correspondence:
                               efrem.braun@berkeley.edu (EB); justin.b.gilmer@vanderbilt.edu (JG); hbmayes@umich.edu (HM);
                               dmobley@mobleylab.org (DLM); jimonroe@umail.ucsb.edu (JIM); samarjeet@jhmi.edu (SP);
                               zuckermd@ohsu.edu (DMZ)


1     Introduction                                                    of the simulation [6, 7]. Relevant properties can be calculated
Molecular simulation techniques play an important role in             for each “snapshot” (a stored conﬁguration of the system,
our quest to understand and predict the properties, structure,        also called a “frame”) and averaged over the entire trajectory
and function of molecular systems, and are a key tool as              to compute estimates of desired properties.
we seek to enable predictive molecular design. Simulation                 Depending on how the system is propagated, molecular
methods are useful for studying the structure and dynamics            simulation methods can be divided into two main categories:
of complex systems that are too complicated for pen and               Molecular Dynamics (MD) and Monte Carlo (MC). With MD
paper theory, helping interpret experimental data in terms of         methods, the equations of motion are numerically integrated
molecular motions. Additionally, they are increasingly used           to generate a dynamical trajectory of the system. MD simula-
for quantitative prediction of properties of use in molecular         tions can be used for investigating structural, dynamic, and
design and other applications [1–5].                                  thermodynamic properties of the system. With MC methods,
    The basic idea of any molecular simulation method is              probabilistic rules are used to generate a new conﬁguration
straightforward; a particle-based description of the system           from the present conﬁguration and this process is repeated
under investigation is constructed and then the system is             to generate a sequence of states that can be used to calculate
propagated by either deterministic or probabilistic rules to          structural and thermodynamic properties but not dynamical
generate a trajectory describing its evolution over the course        properties; indeed, MC simulations lack any concept of time.


Received: 2 August 2018                                                                     https://doi.org/10.33011/livecoms.1.1.5957
Accepted: 9 November 2018                                       1 of 28                         Living J. Comp. Mol. Sci. 2019, 1(1), 5957




Thus, the “dynamics” produced by an MC method are not               ing that systems will consist of thousands to hundreds of
the temporal dynamics of the system, but the ensemble of            thousands or millions of atoms. While system size alone
conﬁgurations that reﬂect those that could be dynamically           does not dictate a classical description, if we are interested
sampled. This foundational document will focus on the con-          in calculations of free energies or transport properties at ﬁ-
cepts needed to carry out correct MD simulations that utilize       nite (often laboratory) temperatures, these include entropic
good practices. Many, but not all, of the concepts here are         contributions (as further discussed below) meaning that ﬂuc-
also useful for MC simulations and apply there as well. How-        tuations and correlations of motions within the system affect
ever, there are a number of key differences, which are outside      computed properties, meaning that simulations must not
the scope of this current document.                                 only sample single optimal states but instead must sample
    Either method can be carried out with different underlying      the correct distribution of states – requiring simulations of
physical theories to describe the particle-based model of the       some length. Furthermore, many systems of interest, such as
system under investigation. If a quantum mechanics (QM)             polymers (biological and otherwise) have slow motions that
description of matter is used, electrons are explicitly repre-      must be captured for accurate calculation of properties. For
sented in the model and interaction energy is calculated by         example, for proteins, relevant timescales span from nanosec-
solving the electronic structure of the molecules in the sys-       onds to seconds or more, and even rearrangements of buried
tem with no (or few) empirical parameters, but with various         amino acid sidechains can in some cases take microseconds
approximations to the physics for tractability. In a molecu-        or more, with larger conformational changes and protein fold-
lar mechanics (MM) description, molecules are represented           ing taking even longer [9, 10]. Recent hardware innovations
by particles representing atoms or groups of atoms. Each            have made microsecond-length simulations for biological sys-
atom may be assigned an electric charge and a potential en-         tems of 50-100,000 atoms relatively routine, and herculean
ergy function with a large number of empirical parameters           efforts have pushed the longest simulations out past the mil-
(ﬁtted to experiment, QM, or other data) used to calculate          lisecond range. However, the ﬁeld would like to reach even
non-bonded and bonded interactions. Unless otherwise spec-          longer timescales, meaning that switching to a more detailed
iﬁed, MD simulations employ MM force ﬁelds, which calculate         energy model is only done with some trepidation because
the forces that determine the system dynamics. MM simu-             slower energy evaluations mean less time available for sam-
lations are much faster than quantum simulations, making            pling. Thus the need for speed limits the use of quantum
them the methods of choice for vast majority of molecular           mechanical descriptions.
simulation studies on biomolecular systems in the condensed              Thus, for the rest of this document we will restrict our-
phase. However, typically, they are of lower accuracy than QM       selves to classical MD.
simulations and cannot simulate bond rearrangements. QM                  One other important note is that, within classical molecu-
simulations may be too computationally expensive to allow           lar simulations, bond breaking and forming is generally not
simulations of the time and length scales required to describe      allowed (with notable exceptions such as reactive force ﬁelds),
the system of interest [5]. The size of the system amenable for     meaning that the topology or chemistry of a system will re-
to QM simulation also depends on what method is chosen,             main constant as a function of time. That is, the particles
from high-level ab initio methods to semi-empirical meth-           comprising the system move around, but the chemical iden-
ods; discussion of these methods are outside the scope of           tity of each molecule in the system remains a constant over
this article, and useful references are separately available [8].   the course of the simulation (with only partial exceptions,
Computational resources available are also an important con-        such as the case of constant pH simulations [11]). This also
sideration in deciding whether QM simulations are tractable.        means that the notion of pH in molecular simulations primar-
Roughly, QM simulations might be tractable with hundreds            ily refers to the selection of ﬁxed protonation states for the
of atoms or fewer, while MD simulations routinely have tens         components of the system.
or hundreds of thousands of atoms in the system. Much                    Here, we ﬁrst discuss the scope of this document, then
above that level, coarse-graining methods are used. They            go over some of the fundamental concepts or science topics
reduce resolution and computational cost. Although many             which provide the underpinnings of molecular simulations,
of the approaches for atomistic simulations discussed here          giving references for further reading. Then, we introduce a
can apply to coarse-grained simulations, such simulations           variety of basic simulation concepts and terminology, with
are not the focus of this paper and we will not discuss how         links to further reading. Our goal is not to cover all topics,
coarse-grained simulations are initially built.                     but to provide some guidance for the critical issues which
    Speed is a particular concern when describing condensed         must be considered. We also provide a checklist to assist with
phase systems, as we are often interested in the properties         preparing for and beginning a modeling project, highlighting
of molecules (even biomacromolecules) in solution, mean-            some key considerations addressed in this work.


                                                               2 of 28                        Living J. Comp. Mol. Sci. 2019, 1(1), 5957




2     Scope of this document                                           • Point particles and rigid bodies
There are several excellent textbooks on classical simulation          • Holonomic constraints
methods; some we have found particularly helpful are Allen            Molecular simulation methods work on many-particle sys-
and Tildesley’s “Computer Simulations of Liquids” [12], Leach’s   tems following the rules of classical mechanics. Basic knowl-
“Molecular Modelling” [7], and Frenkel and Smit’s “Under-         edge of key concepts of classical mechanics is important for
standing Molecular Simulations” [6], though there are many        understanding simulation methods. Here, we will assume
other sources. Tuckerman’s “Statistical Mechanics: Theory         you are already familiar with Newtonian mechanics.
and Molecular Simulation” [13] may be helpful to a more               Classical molecular models typically consist of point par-
advanced audience.                                                ticles carrying mass and electric charge with bonded inter-
    In principle, anyone with adequate prior knowledge            actions (describing bond lengths, angles, and torsions) and
(namely, undergraduate level calculus and physics) should be      non-bonded interactions (describing electrostatic and van der
able to pick up one of these books and learn the required         Waals forces). Sometimes it is much more eﬃcient to freeze
skills to perform molecular simulations, perhaps with help        the internal degrees of freedom and treat the molecule as
from a good statistical mechanics and thermodynamics              a rigid body where the particles do not change their rela-
book or two. In practice, due to the interdisciplinary and        tive orientation as the whole body moves; this is commonly
somewhat technical nature of this ﬁeld, many newcomers            done, for example, for rigid models of the water molecule.
may ﬁnd it diﬃcult and time consuming to understand all           The timestep for simulation is determined by the fastest fre-
the methodological issues involved in a simulation study.         quency motion. Due to the high frequency of the O-H vibra-
The goal of this document is to introduce a new practitioner      tions, accurately treating water classically would require solv-
to some key basic concepts and bare minimum scientiﬁc             ing the equations of motion with a small timestep (commonly
knowledge required for correct execution of these methods.        1 fs). Thus, for computational eﬃciency water is often instead
We also provide a basic set of “best practices” that can be       treated as a rigid body to allow a larger timestep (often dou-
used to avoid common errors, missteps and confusion in            ble the length). Keeping speciﬁed objects rigid in a simulation
elementary molecular simulations work. This document              involves applying holonomic constraints, where the rigidity is
is not meant as a full introduction to the area; rather, it       deﬁned by imposing a minimal set of ﬁxed bond lengths and
is intended to help guide further study, and to provide           angles through iterative procedures during the numerical in-
a foundation for other more specialized best-practices            tegration of the equation of motion (see Section 4.6 for more
documents focusing on particular simulation areas.                on constraints and integrators).
    Modern implementations of classical simulations also rely         Classical mechanics has several mathematical formula-
on a large body of knowledge from the ﬁelds of computer           tions, namely the Newtonian, Hamiltonian and Lagrangian
science, programming, and numerical methods, which will           formulations. These formulations are physically equivalent,
not be covered in detail here.                                    but for certain applications one formulation can be more ap-
                                                                  propriate than the other. Many simulation methods use the
3     Science topics                                              Hamiltonian formulation and therefore basic knowledge of
A new practitioner does not have to be an expert in all of the    Hamiltonian mechanics is particularly important.
ﬁelds that provide the foundation for our simulation meth-            Classical mechanics has several conserved quantities and
ods and analysis of the data produced by these methods.           simulators should be familiar with these, for example, the to-
However, grasping some key concepts from each of these            tal energy of a system is a constant of motion. These concepts
disciplines, described below, is essential. This section serves   play an important role in development and proper implemen-
as a preface for Section 4 and suggestions for further reading    tation of simulation methods. For example, a particularly
on these subjects are provided throughout the document. In        straightforward check of the correctness of an MD code is to
each subsection, we begin by highlighting some of the critical    test whether energy is conserved.
topics from the corresponding area, then describe what these          Most books on molecular simulations have a short discus-
are and why they are important to molecular simulations.          sion or appendices on classical mechanics that can serve the
                                                                  purpose of quick introductions to the basic concepts; Shell’s
3.1     Classical mechanics                                       book also has a chapter on simulation methods which covers
3.1.1    Key concepts                                             some of these details [14]. A variety of good books on classi-
Critical concepts from classical mechanics include:               cal mechanics are also available and give further details on
                                                                  these concepts.
    • Newton’s equations of motion
    • Hamilton’s equations


                                                             3 of 28                          Living J. Comp. Mol. Sci. 2019, 1(1), 5957




3.2     Thermodynamics                                               equilibrium (i.e. we are somehow adding or removing energy).
                                                                     In this sense, the laws of thermodynamics provide us rigor-
3.2.1   Key concepts
                                                                     ous sanity checks in addition to many useful mathematical
A variety of thermodynamic concepts are important for molec-
                                                                     relations for computing properties. Basic thermodynamic
ular simulations:
                                                                     principles thus also dictate proper simulation protocols and
   • Temperature and pressure                                        associated best practices.
   • Internal energy and enthalpy                                        The concept of the thermodynamic limit is important here.
   • Gibbs and Helmholtz free energy                                 Speciﬁcally, as the size of a ﬁnite system is increased, keeping
   • Entropy                                                         the particle number density roughly constant, at some point it
     One of the main objectives of molecular simulations is to       is said to reach the thermodynamic limit where its behavior is
estimate/predict thermodynamic behavior of real systems as           bulk-like and no longer depends on the extent of the system.
observed in the laboratory. Typically this means we are inter-       Thus, small systems will exhibit unique behaviors that reﬂect
ested in macroscopic systems, consisting of 1023 particles or        their microscopic size, but suﬃciently large systems are said
more (i.e. at least a mole of particles). But properties of inter-   to have reached the thermodynamic limit and macroscopic
est include not only macroscopic, bulk thermodynamic prop-           thermodynamics applied. This is due to the fact that the effect
erties, such as density or heat capacity, but also microscopic       of interfaces or boundaries have largely been removed, and,
properties like speciﬁc free energy differences associated           more importantly, that averages of system properties are
with, say, changes in the conformation of a molecule. For this       now over a suﬃciently large number of molecules that any
reason, it is important to understand key concepts in thermo-        instantaneous snapshot of the system roughly corresponds
dynamics, such as temperature, pressure, entropy, internal           to average behavior (i.e. ﬂuctuations in properties become
energy, various forms of free energy, and the relationships          negligible with increasing system size).
between them. Paramount, however, is an understanding                    Although we usually think of thermodynamics applying
of the connection between thermodynamics and statistical             macroscopically and statistical mechanics applying on the
mechanics, which allows us to relate macroscopic, experi-            microsopic level, it is important to remember that the laws of
mental measurements to the behavior of the much smaller              thermodynamics still hold on average regardless of the length
system that is simulated. This topic involves a variety of sub-      scale. That is, a molecule in contact with a thermal bath will
tleties and thus can be a confusing and diﬃcult, so we refer         exchange energy with the bath, but its average energy is a
the reader to a more extensive discussion in one of several          well-deﬁned constant. This allows us to deﬁne thermody-
books [14, 15].                                                      namic quantities associated with microscopic events, such as
     As an example, consider temperature. In a macroscopic           the binding of a ligand to a protein. This is useful because it
sense, we understand this quantity intuitively as how hot or         allows us to assign molecular meaning to well-deﬁned ther-
cold something is. The laws of thermodynamics provide us             modynamic processes that can only be indirectly probed by
with a further abstraction, telling us that this is in fact the      experiment. Importantly, as long as we have carefully deﬁned
derivative of the internal energy with respect to the entropy.       our ensemble and thermodynamic path, we can apply the
This mathematical deﬁnition itself is not particularly helpful,      powerful relationships of thermodynamics to more easily cal-
but provides a starting point for other derivations. If we           culate many properties of interest. For instance, one may use
want to understand temperature from the point of view of             molecular dynamics to eﬃciently numerically integrate the
understanding molecular behavior, we ﬁnally must turn to             Clapeyron equation and construct equations of state along
statistical mechanics. Since molecular dynamics is mostly            phase coexistence curves [16, 17].
used to simulate behavior at the molecular or atomistic level,
it is necessary to utilize statistical-mechanical expressions         3.2.2   Books
in computing what would be observed as the macroscopic,               Equilibrium thermodynamics is taught in most undergradu-
thermodynamic temperature.                                            ate programs in physics, chemistry, biochemistry and various
     This discussion should not provide the impression that           engineering disciplines. Depending on the background, the
statistical mechanics is more important than thermodynam-             practitioner can choose one or more of the following books
ics. The two are intimately connected and we must rely on             to either learn or refresh their basic knowledge of thermody-
both to successfully conduct and obtain information from              namics. Here are some works we ﬁnd particularly helpful:
MD simulations. In particular, thermodynamics provides rigid              • Atkins and De Paula’s “Physical Chemistry” [18], chap-
rules that must be satisﬁed if we are to faithfully reproduce               ters 1 to 4.
reality. For instance, if energy is not conserved, the ﬁrst law is        • McQuarrie and Simon’s extensive work, “Physical Chem-
not satisﬁed and we are for sure simulating a system out of                 istry: A Molecular Approach” [19]


                                                                4 of 28                         Living J. Comp. Mol. Sci. 2019, 1(1), 5957




                       • Dill’s “Molecular Driving Forces” [15]                                                      discussions of rates and rate coeﬃcients can be found in
                       • Kittel and Kroemer’s “Thermal Physics” [20]                                                 numerous textbooks (e.g., [15, 21]).
                       • Shell [14]: Chapters 1-15.                                                                       Once you have understood that MD behavior reﬂects sys-
                                                                                                                     tem timescales, you must set this behavior in the context
3.3                           Classical statistical mechanics                                                        of an extremely complex energy landscape consisting of al-
3.3.1                          Key concepts                                                                          most innumerable minima and barriers, as schematized in
Key concepts from statistical mechanics are particularly im-                                                         Fig. 1(b). Each small basin represents something like a dif-
portant and prevalent in molecular simulations:                                                                      ferent rotameric state of a protein side chain or perhaps a
                                                                                                                     tiny part of the Ramachandran spaces (backbone phi-psi an-
                       • Fluctuations                                                                                gles) for one or a few residues. Observing the large-scale
                       • Deﬁnitions of various ensembles                                                             motion of a protein then would require an MD simulation
                       • Time averages and ensemble averages                                                         longer than the sum of all the timescales for the necessary
                       • Equilibrium versus non-equilibrium                                                          hops, bearing in mind that numerous stochastic reversals are
   Traditional discussions of classical statistical mechanics,                                                       likely during the simulation. Because functional biomolecu-
especially concise ones, tend to focus ﬁrst or primarily on                                                          lar timescales tend to be on µs - ms scales and beyond, it is
macroscopic thermodynamics and microscopic equilibrium                                                               challenging if not impossible to observe them in traditional
behavior based on the Boltzmann factor, which tells us                                                               MD simulations. There are numerous enhanced sampling
that conﬁgurations rN occur with (relative) probability                                                              approaches [22, 23] but these are beyond the scope of this
exp[–U(rN )/(kB T)], based on potential energy function U and                                                        discussion and they have their own challenges which often
temperature T in absolute units. Dynamical phenomena                                                                 are much harder to diagnose (see [24] and https://github.
and their connection to equilibrium tend to be treated later                                                         com/dmzuckerman/Sampling-Uncertainty).
in discussion, if at all. However, as the laws of statistical                                                             What is the connection between MD simulation and equi-
mechanics arise naturally from dynamical equations, we will                                                          librium? The most precise statement we can make is that an
discuss dynamics ﬁrst.                                                                                               MD trajectory is a single sample of a process that is relaxing
                                                                                                                     to equilibrium from the starting conﬁguration [21, 25]. If the
                   (a)                                                     (b)                                       trajectory is long enough, it should sample the equilibrium
                                                                                                                     distribution – where each conﬁguration occurs with frequency


 U, potential energy [a.u.]                              U, potential energy [a.u.]
                                                                                                                     proportional to its Boltzmann factor. In such a long trajec-
                                                                                                                     tory (only), a time average thus will give the same result as a
                                                                                                                     Boltzmann-factor-weighted, or ensemble, average. We refer
                                        U‡                                                                           to such a system, where the time and ensemble averages
                               A                                                                                     are equivialent, as “ergodic.” Note that the Boltzmann-factor
                                              B
                                   UA               UB                                                               distribution implies that every conﬁguration has some proba-
                              x, configuration [a.u.]                                 x, configuration [a.u.]        bility, and so it is unlikely that a single conformation or even a
                                                                                                                     single basin dominates an ensemble. Beware that in a typical
Figure 1. Energy landscapes. (a) A highly simpliﬁed landscape used                                                   MD trajectory it is likely that only a small subset of basins will
to illustrate rate concepts and (b) a schematic of a more complex                                                    be sampled well – those most quickly accessible to the initial
landscape with numerous minima and ambiguous state boundaries.
                                                                                                                     conﬁguration. It is sometimes suggested that multiple MD
                                                                                                                     trajectories starting structures can aid sampling, but unless
    The key dynamical concept to understand is embodied in
                                                                                                                     the equilibrium distribution is known in advance, the bias
the twin characteristics of timescales and rates. The two are
                                                                                                                     from the set of starting structures is simply unknown and
literally reciprocals of one another. In Fig. 1(a), assume you
                                                                                                                     harder to diagnose.
have started an MD simulation in basin A. The trajectory is
                                                                                                                          A fundamental equilibrium concept that can only be
likely to remain in that basin for a period of time – the “dwell”
                                                                                                                     sketched here is the representation of systems of enormous
timescale – which increases exponentially with the barrier
                                                                                                                     complexity (many thousands, even millions of atoms) in
height, (U‡ – UA ). Barriers many times the thermal energy kB T
                                                                                                                     terms of just a small number of coordinates or states. The
imply long dwell timescales, approximated as the reciprocal
                                                                                                                     conformational free energy of a state, e.g., FA or FB is a
of exp[(U‡ – UA )/(kB T)]. The rate coeﬃcient kAB relates to the
                                                                                                                     way of expressing the average or summed behavior of all
transition probability per unit time per amount of reactant(s).
                                                                                                                     the Boltzmann factors contained in a state: the deﬁnition
All transitions occur in a random, stochastic fashion and are
                                                                                                                     requires that the probability (or population) peq of a state in
predictable only in terms of average behavior. More detailed
                                                                                                                     equilibrium be proportional to the Boltzmann factor of its


                                                                                                                5 of 28                         Living J. Comp. Mol. Sci. 2019, 1(1), 5957




                                          eq
conformational free energy: pA ∼ exp(–FA /kB T). Because                              before choosing to conduct a non-equilibrium MD simulation.
equilibrium behavior is caused by dynamics, there is a
fundamental connection between rates and equilibrium,                                 3.3.2    Books
                eq          eq                                                        Books which we recommend as particularly helpful in this
namely that pA kAB = pB kBA , which is a consequence of
“detailed balance”. There is a closely related connection for                         area include:
on- and off-rates with the binding equilibrium constant.                                  • Reif’s “Fundamentals of Statistical and Thermal
For a continuous coordinate (e.g., the distance between                                     Physics” [27]
two residues in a protein), the probability-determining free                              • McQuarrie’s “Statistical Mechanics” [28]
energy is called the “potential of mean force” (PMF); the                                 • Dill and Bromberg’s “Molecular Driving Forces” [15]
Boltzmann factor of a PMF gives the relative probability of a                             • Hill’s “Statistical Mechanics: Principles and Selected Ap-
given coordinate. Any kind of free energy implicitly includes                               plications” [29]
entropic effects; in terms of an energy landscape (Fig. 1),                               • Shell’s “Thermodynamics and Statistical Mechanics” [14]
the entropy describes the width of a basin or the number                                  • Zuckerman’s “Statistical Physics of Biomolecules” [21]
of arrangements a system can have within a particular                                     • Chandler’s “Introduction to Modern Statistical Mechan-
state. One way to think of this it is that entropy of a state                               ics” [30]
relates to the volume of 6N-dimensional phase space that
the state occupies, which in the one-dimensional case is                              3.3.3    Online resources
just the width. These points are discussed in textbooks,                              Several online resources have been particularly helpful to
as are the differences between free energies for different                            people learning this area, including:
thermodynamic ensembles – e.g., A, the Helmholtz free
                                                                                          • David Kofke’s notes: http://www.eng.buffalo.edu/
energy, when T is constant, and G, the Gibbs free energy,
                                                                                            ~kofke/ce530/Lectures/lectures.html
when both T and pressure are constant – which are not
                                                                                          • Scott Shell’s notes: https://engineering.ucsb.edu/~shell/
essential to our introduction [15, 21].1
                                                                                            che210d/assignments.html
    A ﬁnal essential topic is the difference between equilib-
rium and non-equilibrium systems. We noted above that an
MD trajectory is not likely to represent the equilibrium ensem-                       3.4     Classical electrostatics
ble because the trajectory is probably too short. However, in                         3.4.1    Key concepts
a living cell where there is no shortage of time, biomolecules                        Key concepts from classical electrostatics include
may exhibit non-equilibrium behavior for a quite different                                • The Coulomb interaction and its long-range nature
reason – because they are driven by the continual addition                                • Polarizability, dielectric constants, and electrostatic
and removal of (possibly energy-carrying) substrate and prod-                               screening
uct molecules. In this type of non-equilibrium situation, the                             • When and why we need lattice-sum electrostatics and
distribution of conﬁgurations will not follow a Boltzmann dis-                              similar approaches
tribution. Specialized simulation approaches are available
to study such systems [23, 26] but they are not beginner-                                 Electrostatic interactions are both some of the longest-
friendly. Non-equilibrium molecular concepts pertinent to                            range interactions in molecular systems and the strongest,
cell biology have been discussed at an introductory level                            with the interaction (often called “Coulombic” after Coulomb’s
(e.g. http://www.physicallensonthecell.org/). Notably, many                          law) between charged particles falling off as 1/r where r is the
experiments are conducted at non-equilibrium conditions;                             distance separating the particles. Atom-atom interactions are
for example, membrane diffusion coeﬃcients are commonly                              thus necessarily long range compared to other interactions
measured by setting up a concentration gradient across the                           in these systems (which fall off as 1/r 3 or faster). This means
membrane and measuring the ﬂux. It can be tempting to the                            atoms or molecules separated by considerable distances can
beginner to setup an MD simulation in the same manner as                             still have quite strong electrostatic interactions, though this
such an experiment. However, maintaining non-equilibrium                             also depends on the degree of shielding of the intervening
conditions is typically more complicated in an MD simula-                            medium (or its relative permittivity or dielectric constant).
tion than in an experiment as large reservoirs are commonly                               The static dielectric constant of a medium, or relative per-
required. Frequently, equilibrium methods can provide the                            mittivity r (relative to that of vacuum), affects the prefactor
same or similar information as a non-equilibrium experiment;                         for the decay of these long range interactions, with interac-
users should seek to obtain familiarity with such methods                            tions reduced by 1r . Water has a high relative permittivity or
                                                                                     dielectric constant close to 80, whereas non-polar compounds
    Occasionally F is used to refer to either appropriate free energy, A or G, but
this is not standard.                                                                such as n-hexane may have relative permittivities near 2 or


                                                                                6 of 28                          Living J. Comp. Mol. Sci. 2019, 1(1), 5957




even lower. This means that interactions in non-polar media              In practice, lattice sum electrostatics introduce far fewer
such as non-polar solvents, or potentially even within the rel-       and less severe artifacts than do cutoff schemes, so these
atively non-polar core of a larger molecule such as a protein,        are used for most classical all-atom simulation algorithms at
are effectively much longer-range even than those in water.           present. A variety of different eﬃcient lattice-sum schemes
The dielectric constant of a medium also relates to the de-           are available [38]. In general these should be used whenever
gree of its electrostatic response to the presence of a charge;       long range electrostatic interactions are expected to be sig-
larger dielectric constants correspond to larger responses to         niﬁcant; they may not be necessary in especially nonpolar
the presence of a nearby charge.                                      systems and/or with extremely high dielectric constant sol-
    It turns out that atoms and molecules also have their             vents where electrostatic interactions are exclusively short
own levels of electrostatic response; particularly, their elec-       range, but in general they should be regarded as standard
tron distributions polarize in response to their environment,         (see also Section 4.7, below).
effectively giving them an internal dielectric constant. This
polarization can be modeled in a variety of ways, such as             3.4.2    Books
(in ﬁxed charge force ﬁelds) building in a ﬁxed amount of            On classical electrostatics, we have found the undergraduate-
polarization which is thought to be appropriate for simula-          level work by David J. Griﬃths, “Introduction to Electrody-
tions in a generic “condensed phase” or by explicitly including      namics” [39], to be quite helpful. The graduate-level work of
polarizability via QM or by building it into a simpler, classi-      Jackson, “Classical Electrodynamics” [40], is also considered a
cal model which includes polarizability such as via explicit         classic/standard work, but may prove challenging for those
atomic polarizabilities [31, 32] or via Drude oscillator-type        without a background relatively heavy in mathematics.
approaches [33], where inclusion of extra particles attached
to atoms allows for a type of effective polarization.                 3.5     Molecular interactions
    Because so many interactions in physical systems involve          3.5.1    Key concepts
polarity, and thus signiﬁcant long-range interactions that de-        Molecular simulations are, to a large extent, about molecular
cay only slowly with distance, it is important to regard electro-     interactions, so these are particularly key, including:
static interactions as fundamentally long-range interactions.
                                                                          • Bonded and nonbonded interactions
Indeed, contributions to the total energy of a system from
                                                                          • The different types of nonbonded interactions and why
distant objects may be even more important in some cases
                                                                            they are separated in classical descriptions
than those from nearby objects. Speciﬁcally, since interac-
                                                                          • The dividing line between bonded and nonbonded in-
tions between charges fall off as 1/r, but the volume of space
                                                                            teractions
at a given separation distance increases as r 3 , distant interac-
tions can contribute a great deal to the energies and forces              Key interactions between atoms and within or between
in molecular systems. In practice, this means that severe             molecules are typically thought of as consisting of two main
errors often result from neglecting electrostatic interactions        types – bonded and non-bonded interactions. While these
beyond some cutoff distance [7, 34–37]. Thus, we prefer to            arise from similar or related physical effects (ultimately all
include all electrostatic interactions, even out to very long         tracing back to QM and the basic laws of physics) they are
ranges. Once this is decided, it leaves simulators with two           typically treated in rather distinct manners in molecular sim-
main options, only one of which is really viable. First, we can       ulations so it is important to consider the two categories
simulate the actual ﬁnite (but large) system which is being           separately.
studied in the lab, including its boundaries. But this is im-             Bonded interactions are those between atoms which are
practical, since macroscopic systems usually include far too          connected, or nearly so, and relating to the bonds connecting
many atoms (on the order of at least a mole or more). The             these atoms. In typical molecular simulations these consist
remaining option, then, is to apply periodic boundary condi-          of bond stretching terms, angle bending terms, and terms
tions (see Section 4.2) to tile all of space with repeating copies    describing the rotation of torsional angles, as shown in Figure
of the system. Once periodic boundary conditions are set              2. Torsions typically involve four atoms and are often of two
up, deﬁning a periodic lattice, it becomes possible to include        types – “proper” torsions, around bonds connecting groups
all long-range electrostatic interactions via a variety of dif-       of atoms, and “improper” torsions which involve neighbors of
ferent types of sums which can be described as “lattice sum           a central atom; these are often used to ensure the appropri-
electrostatics” or Ewald-type electrostatics [37, 38] where the       ate degree of planarity or non-planarity around a particular
periodicity is used to make possible an evaluation of all long        group (such as planarity of an aromatic ring). It is important
range electrostatic interactions, including those of particles        to note that the presence of bonded interactions between
with their own periodic images.


                                                                7 of 28                         Living J. Comp. Mol. Sci. 2019, 1(1), 5957




 (a)                          (b)                                         energy function or force ﬁeld family. For example, the AMBER
                                           1                              family force ﬁelds usually reduce 1-4 electrostatics to 1.2 1
                                                                                                                                        of
                                                                          their original value, and 1-4 Lennard-Jones interactions to 12
                                       2                                  of their original value. 1-4 interactions are essentially consid-
                                                     3                    ered the borderline between the bonded and non-bonded
                                                                          regions. These short-range interactions can be quite strong
                                                                          and there is potentially a risk of them overwhelming longer-
                                                                          range interactions, hence their typical reduction.
Figure 2. Standard MM force ﬁelds include terms that represent (a)
bond and angle stretching around equilibrium values, using harmonic       3.5.2    Books
potentials with spring constants ﬁt to the molecules and atoms to
                                                                         For a discussion of molecular interactions, we recommend
which they are applied; and (b) rotation around dihedral angles (green
arrow) deﬁned using four atoms, typically using a cosine expansion.
                                                                         “Intermolecular and surface forces” by Jacob N. Israelachvili.
                                                                         A variety of other books discuss these from a simulation
                                                                         perspective, e.g. Leach [7] and Allen and Tildesley [12].
atoms does not preclude their also having non-bonded inter-
actions with one another (see discussion of exclusions and                4     Basic simulation concepts and
1-4 interactions, below).
                                                                                terminology
     Nonbonded interactions between atoms are all interac-
                                                                         Above, we covered a variety of fundamental concepts needed
tions which are included in the potential energy of the system
                                                                         for understanding molecular simulations and the types of
aside from bonded interactions. Commonly these include
                                                                         interactions and forces we seek to model; here, we shift our
at least point-charge Coulomb electrostatic interactions and
                                                                         attention to understanding basics of how molecular simula-
“non-polar” interactions modeled by the Lennard-Jones poten-
                                                                         tions actually work.
tial or another similar potential which describes short range
repulsion and weak long-range interaction even between non-
                                                                          4.1     Force ﬁelds
polar atoms. Additional terms may also be included, such as
                                                                         The term “force ﬁeld” simply refers to the included terms,
interactions between ﬁxed multipoles, interactions between
                                                                         particular form, and speciﬁc implementation details, including
polarizable sites, or occasionally explicit potentials for hydro-
                                                                         parameter values, of the chosen potential energy function.2
gen bonding or other specialized terms. These are particu-
                                                                            Most of the terms included in potential energy functions
larly common in polarizable force ﬁelds such as the AMOEBA
                                                                         have already been detailed in Section 3.5, with the most
model.
                                                                         common being Coulombic, Lennard-Jones, bond, angle, and
     Often, the energy functions used by molecular simulations
                                                                         torsional (dihedral) terms (Figure 2). Here, we very brieﬂy
explicitly neglect nonbonded interactions between atoms
                                                                         describe the mathematical forms used to represent such in-
which are immediately bonded to one another, and atoms
                                                                         teractions.
which are separated by only one intervening atom, partly to
                                                                            Non-bonded interactions of the Lennard-Jones form are
make it easier to ensure that these atoms have preferred ge-
                                                                         well-described throughout the literature (for instance see Ch.
ometries dictated by their deﬁned equilibrium lengths/angles
                                                                         4 of Leach [7]); these model a short-range repulsion that
regardless of the nonbonded interactions which would oth-
                                                                         scales as 1/r 12 and a long-range attraction that scales as 1/r 6 .
erwise be present. This neglect of especially short range
                                                                         Coulombic interactions, including both short and long-range
nonbonded interactions between near neighbors is called
                                                                         components, are described in detail elsewhere in this docu-
“exclusion”, and energy functions typically specify which inter-
                                                                         ment. To represent bonded interactions, harmonic potentials
actions are excluded.
                                                                         are often employed. The same is true for angles between
     The transition to torsions, especially proper torsions, is
where exclusions typically end. However, many all-atom en-                    It is worth noting there is a occasionally a bit of ambiguity when the term
                                                                         “force ﬁeld” is used. In some cases it is used to refer to a library of parameters
ergy functions commonly used in biomolecular simulations                 that could be applied to assign an energy function to a speciﬁc molecular
retain only partial nonbonded interactions between terminal              system via a parameterization process after applying some speciﬁc chemical
                                                                         perception like atom typing to that system [41]. For example, one might speak
atoms involved in a torsion. The atoms involved in a tor-
                                                                         of the AMBER ff15FB [42] protein force ﬁeld, which essentially provides a recipe
sion, if numbered beginning with 1, would be 1, 2, 3, and 4,             for assigning parameters to a protein once atom types are assigned. In other
so the terminal atoms could be called atoms 1 and 4, and                 cases, “force ﬁeld” is used to refer to the speciﬁcs of the potential energy
                                                                         function after application to a speciﬁc system — what could also be called a
nonbonded interactions between such atoms are called “1-4
                                                                         “parameterized system”. For our purposes here, the distinction between a force
interactions”. These interactions are often present but re-              ﬁeld library and a parameterized system is not particularly important, but it is
duced, though the exact amount of reduction differs by the               worth noting the potential ambiguity.


                                                                    8 of 28                                Living J. Comp. Mol. Sci. 2019, 1(1), 5957




three bonded atoms, but the harmonic potential is applied          particular functional form and is available in their simulation
with respect to the angle formed and not the distance be-          package of choice, so for such users it is more important
tween atoms. Torsional terms are also commonly employed,           to know how the functional form represents the different
usually consisting as sums of cosines, i.e. a cosine expansion.    interactions involved than to necessarily be able to justify
    While the above are perhaps the most common poten-             why that particular functional form was chosen.
tials used, there are a variety of common variations as well.          Many examples of force ﬁelds abound in the literature —
More exotic potentials based on three-body intermolecular          in fact, too many to provide even a representative sample
orientations, or terms directly coupling bond lengths and          or list of citations, as most force ﬁelds are speciﬁcally devel-
bending angles are also possible. Some historic force ﬁelds        oped for particular systems or categories of systems under
also added an explicit (non-Coulombic) hydrogen bonding            study. However, reviews are available describing and compar-
term, though these are less frequently used in many cases          ing force ﬁelds for biomolecular simulations [31, 49], solid,
today. Additionally, other choices of potential function are of    covalently-bonded materials [50], polarizable potentials [51],
course acceptable, including Buckingham or Morse potentials,       and models of water [52, 53], to name just a few. Many force
or the use of “improper” dihedral terms to enforce planarity       ﬁelds are open-source and parameter ﬁle libraries may be
of cyclic portions of molecules. This may even include empiri-     found through the citations in the resources above or are of-
cal corrections based on discrete binning along a particular       ten distributed with molecular simulation packages. Limited
set of degrees of freedom [43, 44], as well as applied exter-      databases of force ﬁelds also exist, most notably for simula-
nal ﬁelds (i.e. electric ﬁelds) and force ﬁeld terms describing    tions of solid materials where interatomic potentials display
the effect of degrees of freedom, such as solvent, that have       a much wider array of mathematical forms [54, 55].
been removed from the system via “coarse-graining.” [45]               Speciﬁcation of a force ﬁeld involves not just a choice of
For a more in-depth discussion of common (as well as less          functional form, but the details of the speciﬁc parameters
common) force ﬁeld terms, see Ch. 4 of Leach [7], or for an        for all of the interacting particles which will be considered
in-depth review of those speciﬁc to simulating biomolecules,       — that is, the speciﬁc parameters governing the interactions
see Ponder and Case [31].                                          as speciﬁed by the functional form. Parameters are usually
    Functional forms used to describe speciﬁc terms in a po-       speciﬁc to certain types of atoms, bonds, molecules, etc., and
tential energy function may be vastly different in mathemat-       include point charges on atoms if electrostatic terms are in
ical character even though they seek to describe the same          use.
physics. For instance, the Lennard-Jones potential imple-              Some choices which are often considered auxiliary actually
ments an r –12 term to represent repulsions, while an expo-        comprise part of the choice of the force ﬁeld or interaction
nential form is used in the Buckingham potential. This re-         model. Speciﬁcally, settings such as the use of constraints,
sults in very different mathematical behavior at very short        the treatment of cut-offs and other simulation settings affect
distances and as a result differences in numerical implemen-       the ﬁnal energies and forces which are applied to the sys-
tation as well as evaluation eﬃciencies via a computer. For        tem. Thus, to replicate a particular force ﬁeld as described
this reason, one functional form may be preferred above an-        previously, such settings should be matched to prior work
other due to enhanced numerical stability or simplicity of         such as the work which parameterized the force ﬁeld. The
implementation, even though it is not as faithful to the under-    choice of how to apply a cutoff, such as through direct trunca-
lying physics. In this regard, force ﬁeld selection is a form of   tion, shifting of the potential energy function, or through the
selecting a model – one should carefully weigh the virtues of      use of switching functions, should be maintained if identical
accuracy and convenience or speed, and be ever-conscious           matches to prior work computing the properties of interest
of the limitations introduced by this decision (for instance,      are desired. This is especially important for the purposes of
see Becker et al. [46]). It is also important to know that most    free energy calculations, where the potential energy itself is
MD simulation engines only support a subset of functional          recorded. However, force ﬁelds are in some cases slow to
forms. For those forms that are supported, the user manuals        adapt to changes in protocol, so current best practices seem
of these software packages are often excellent resources for       to suggest that lattice-sum electrostatics should be used for
learning more about the rationale and limitations of different     Coulomb electrostatics in condensed phase systems, even if
potential energy functions and terms (e.g. see Part II of Am-      the chosen force ﬁeld was ﬁtted with cutoff electrostatics, and
ber reference manuals[47] and Ch. 4 of the reference manual        in many cases long-range dispersion corrections should be
for GROMACS [48]).                                                 applied to the energy and pressure to account for truncated
    For practical purposes, most beginning users will not be       Lennard-Jones interactions [56, 57].
ﬁtting a force ﬁeld or choosing a functional form, but will            For almost all force ﬁelds, many versions, variants, and
instead be using an existing force ﬁeld that already relies on a   modiﬁcations exist, so if you are using a literature force ﬁeld


                                                              9 of 28                         Living J. Comp. Mol. Sci. 2019, 1(1), 5957




or one distributed with your simulation package of choice, it
is important to pay particular attention (and make note of)
exactly what version you are using and how you obtained it
so you will be able to accurately detail this in any subsequent
publications.
     As clearly described in Becker et al. [46], it is of paramount
importance to understand the capabilities and limitations of
various force ﬁeld models that may seem appropriate for                                           simulated
one’s work. Depending on the physics being simulated and
                                                                                                   system
the computational resources at hand, no force ﬁeld in the
literature may provide results that accurately reproduce ex-
periment. But with so many force ﬁelds to pick from, how is
this possible? The issue lies in what is termed “transferabil-
ity.” Simply put, a classical description of dynamics, as imple-
                                                                                                periodic box
mented in MD, cannot universally describe all of chemistry
                                                                                                    size
and physics. At some level of ﬁner detail, all of the potential
functions described above are simply approximations. Due to
this, force ﬁeld developers must often make the diﬃcult deci-
sion of sacriﬁcing accuracy or generality. For instance, a force
ﬁeld may have been developed to very accurately describe a
single state point, in which case it is obvious that extensive         Figure 3. Periodic boundary conditions are shown for a simple 2D
                                                                       system. Note that the simulated system is a sub-ensemble within an
testing should be performed to ensure that it is also appli-
                                                                       inﬁnite system of identical, small ensembles.
cable at other conditions. Even with force ﬁelds developed
to be general and transferable, it is essential to ensure that
the desired level of realism is achieved, especially if applying       a larger bulk phase (or at least are a much better approxima-
such a model to a new system (even more caution is advised             tion than simply simulating a nanodroplet or a ﬁnite system
when mixing force ﬁelds!). Either way, it is always a good idea        surrounded by vacuum). Periodic boundary conditions can
to check results against previous literature when possible.            alleviate many of the issues with ﬁnite size effects because
This helps ensure that the force ﬁeld is being implemented             each particle interacts with periodic images of particles in
properly and, though it may seem laborious on a short-time             the same system. Clearly, though, it is undesirable for a sin-
horizon, can pay substantial dividends in the long-run.                gle particle to interact with the same particle multiple times.
     Because this balance of accuracy versus generality and            To prevent this, a cut-off of many non-bonded interactions
transferability can be challenging, some efforts eschew trans-         should be chosen that is less than half the length of the simu-
ferability entirely and instead build “bespoke” force ﬁelds,           lation box in any dimension. (However, as noted in Section 3.4
where each molecule is considered as a unique entity and               these cut-offs are not normally applied to electrostatic inter-
assigned parameters independently of any other molecule or             actions because truncating these interactions induces worse
representation of chemical space (e.g. [58]). Such approaches          artifacts than does including interactions with multiple copies
offer the opportunity to assign all molecules with parameters          of the same particle. Instead, what are often termed “cut-
assigned in a consistent way; however, they are unsuitable             offs” that are applied to electrostatics are instead a shift from
for applications where speed needs to exceed that of the pa-           short-range to long-range treatments.) Such cut-offs impose
rameter assignment process – so, for example, for docking of           a natural lower limit to the size of a periodic simulation box,
a large library of potential ligands to a target receptor, if com-     as the box must be large enough to capture all of the most
pounds must be screened at seconds or less per molecule,               signiﬁcant non-bonded interactions. Further information on
such approaches may not be suitable.                                   periodic boundary conditions and discussion of appropriate
                                                                       cut-offs may be found in Leach [7], sections 6.5 and 6.7 and
4.2    Periodic boundary conditions                                    Shell [59]’s lecture on Simulations of Bulk Phases.
Periodic boundary conditions allow more accurate estima-                   It is very important to note that periodic boundary con-
tion of bulk properties from simulations of ﬁnite, essentially         ditions are simply an approximation to bulk behavior. They
nanoscale systems. More precisely, simulations of compara-             DO NOT effectively simulate an inﬁnitely sized simulation box,
tively small systems with periodic boundary conditions can be          though they do reduce many otherwise egregious ﬁnite-size
a good approximation to the behavior of a small subsystem in           effects. This is most easily seen by imagining the placement


                                                                 10 of 28                          Living J. Comp. Mol. Sci. 2019, 1(1), 5957




of a solute in a periodic simulation box. The solute will be        it is assumed that prior to performing any of these steps,
replicated in all of the surrounding periodic images. The con-      an appropriate amount of deliberation has been devoted to
centration of solute is thus exactly one per the volume of the      clearly deﬁning the system and determining the appropriate
box. Although proper selection of non-bonded cutoffs will           simulation techniques.
guarantee that these solutes do not directly interact (hence
the common claim that such systems are at inﬁnite dilution),        4.3.1   System preparation
they may indirectly interact through their perturbation of          System preparation focuses on preparing the starting state
nearby solvent. If the solvent does not reach a bulk-like state     of the desired system for input to an appropriate simulation
between solutes, the simulation will still suffer from obvious      package, including building a starting structure, solvating (if
ﬁnite-size effects.                                                 necessary), applying a force ﬁeld, etc. Because this step dif-
    Macroscopic, lab-scale systems, or bulk systems, typically      fers so much depending on the composition of the system
consist of multiple moles of atoms/molecules and thus from          and what information is available about the starting structure,
a simulation perspective are effectively inﬁnite systems. We        it is a step which varies a great deal depending on the nature
attempt to simulate these by simulating ﬁnite and fairly small      of the system at hand and as a result may require unique
systems, and, in a sense, the very idea that the simulation         tools.
cell is not inﬁnite, but simply periodic, immediately gives rise         Given the variable nature of system preparation, it is highly
to ﬁnite-size effects. Thus, our typical goal is not to remove      recommended that best practices documents speciﬁc to this
these completely but to reduce these to levels that do not          issue and to the type of system of interest be consulted. If
adversely impact the results of our simulations. Finite-size        such documents do not exist, considerable care should be
effects are particularly apparent in the electrostatic compo-       exercised to determine best practices from the literature.
nents of simulations, as these forces are inherently longer              Loosely speaking, system preparation can be thought of
ranged than dispersion forces, as discussed in Section 3.4.         as consisting of two logical components which are not neces-
One should always check that unexpected long-range correla-         sarily consecutive or separate. One comprises building the
tions (i.e. on the length-scale of the simulation box) do not       conﬁguration of the system in the desired chemical state and
exist in molecular structure, spatial position, or orientation.     the other applying force ﬁeld parameters.
It should also be recognized that periodic boundary condi-               For building systems, freely available tools for constructing
tions innately change the deﬁnition of the system and the           systems are available and can be a reasonable option (though
properties calculated from it. Many derivations, especially         their mention here should not be taken as an endorsement
those involving transport properties, such as diffusivity [60],     that they necessarily encapsulate best practices). Examples
assume inﬁnite and not periodic boundary conditions. The            include tools for constructing speciﬁc crystal structures, pro-
resulting differences in seemingly well-known expressions for       teins, and lipid membranes, such as Moltemplate [63], Pack-
computing properties of interest are often subtle, yet may          mol [64], and Atomsk [65].
have a large impact on results. Such considerations should               A key consideration when building a system is that the
be kept in mind when comparing results between simulations          starting structure ideally ought to resemble the equilibrium
and with experiment.                                                structure of the system at the thermodynamic state point
                                                                    of interest. For instance, highly energetically unfavorable
4.3   Main steps of a molecular dynamics                            conﬁgurations of the system, such as blatant atomic overlaps,
                                                                    should be avoided. In some sense, having a good starting
      simulation
                                                                    structure is only a convenience to reduce equilibration times
While every system studied will present unique challenges
                                                                    (if the force ﬁeld is adequate); however, for some systems,
and considerations, the process of performing a molecular
                                                                    equilibration times might otherwise be prohibitively long.
dynamics simulation generally follows these steps:
                                                                         System preparation is arguably the most critical stage of a
  1. System preparation                                             simulation and in many cases receives the least attention; if
  2. Minimization/Relaxation                                        your system preparation is ﬂawed, such ﬂaws may prove fa-
  3. Equilibration                                                  tal. Potentially the worst possible outcome is if the prepared
  4. Production                                                     system is not what you intended (e.g. it contains incorrect
   Additional explanations of these steps along with pro-           molecules or protonation states) but is chemically valid and
cedural details speciﬁc to a given simulation package and           well described by your force ﬁeld and thus proceeds with-
application may be found in a variety of tutorials [61, 62]. It     out error through the remaining steps — and in fact this is
should be noted that these steps may be diﬃcult to unam-            a frequent outcome of problems in system preparation. It
biguously differentiate and deﬁne in some cases. Additionally,      should not be assumed that a system has been prepared cor-


                                                              11 of 28                         Living J. Comp. Mol. Sci. 2019, 1(1), 5957




rectly if it is well-behaved in subsequent equilibration steps;        rigid molecules are present, care must be taken to prevent
considerable care should be taken here.                                components of velocities assigned along constraints from
    Assignment or development of force ﬁeld parameters is              being forced to zero [66]. With a thermostat present, this only
also critical, but is outside the scope of this work. For our          delays system equilibration, but for NVE simulations, such as
purposes, we will assume you have already obtained or de-              might be used in hybrid MC/MD simulations, it can result in
veloped force ﬁeld parameters suitable for your system of              violations of equipartition and large subsequent errors [67].
interest.
                                                                       4.3.4   Equilibration
4.3.2   Minimization                                                   Ultimately, we usually seek to run a simulation in a particular
The purpose of minimization, or relaxation, is to ﬁnd a local          thermodynamic ensemble (e.g. the NVE or NVT ensemble)
energy minimum of the starting structure so that the molecu-           at a particular state point (e.g. target energy, temperature,
lar dynamics simulation does not immediately “blow up” (i.e.           and pressure) and collect data for analysis which is appropri-
the forces on any one atom are not so large that the atoms             ate for those conditions and not biased depending on our
move an unreasonable distance in a single timestep). This              starting conditions/conﬁguration. This means that usually
involves standard minimization algorithms such as steepest             we need to invest simulation time in bringing the system to
descent. For a more involved discussion of minimization algo-          the appropriate state point as well as relaxing away from any
rithms utilized in molecular simulation, see Leach [7], sections       artiﬁcially induced metastable starting states. In other words,
5.1-5.7.                                                               we are usually interested in sampling the most relevant (or
                                                                       most probable) conﬁgurations in the equilibrium ensemble of
4.3.3   Assignment of velocities                                       interest. However, if we start in a less-stable conﬁguration a
Minimization ideally takes us to a state from which we can             large part of our equilibration may be the relaxation time (this
begin numerical integration of the equations of motion with-           may be very long for biomolecules or systems at phase equi-
out overly large displacements (see Leach [7], section 7.3.4);         librium) necessary to reach the more relevant conﬁguration
however, to begin a simulation, we need not just positions but         space.
also velocities. Minimization, however, provides only a ﬁnal               The most straightforward portion of equilibrium is bring-
set of positions. Thus, starting velocities must be assigned;          ing the system to the target state point. Usually, even though
usually this is done by assigning random initial velocities to         velocities are assigned according to the correct distribution,
atoms in a way such that the correct Maxwell-Boltzmann dis-            a thermostat will still need to add or remove heat from the
tribution at the desired temperature is achieved as a starting         system as it approaches the correct partitioning of kinetic
point. The actual assignment process is typically unimpor-             and potential energies. For this reason, it is advised that
tant, as the Maxwell-Boltzmann distribution will quickly arise         a thermostatted simulation is performed prior to a desired
naturally from the equations of motion. Since the momen-               production simulation, even if the production simulation will
tum of the center-of-mass of the simulation box is conserved           ultimately be done in the NVE ensemble. This phase of equili-
by Newtonian dynamics, this quantity is typically set to zero          bration can be monitored by assessing the temperature and
by removing the center-of-mass velocity from all particles af-         pressure of the system, as well as the kinetic and potential
ter random assignment, preventing the simulation box from              energy, to ensure these reach a steady state on average. For
drifting.                                                              example, an NPT simulation is said to have equilibrated to a
     In some cases, we seek to obtain multiple separate and            speciﬁc volume when the dimensions of the simulation box
independent simulations of different instances or realizations         ﬂuctuate around constant values with minimal drift. This def-
of a particular system to assess error, collect better statistics,     inition, though not perfectly rigorous, is usually suitable for
or help gauge dependence of results on the starting structure.         assessing the equilibration of energies, temperature, pres-
It is worth noting that even very small differences in initial         sure, and box dimensions during equilibration simulations.
conﬁguration, such as small changes in the coordinates of a                A more diﬃcult portion of equilibration is to ensure that
single atom, lead to exponential divergence of the time evolu-         other properties of the system which are likely to be impor-
tion of the system [12], meaning that simply running different         tant are also no longer changing systematically with simula-
simulations starting with different initial velocities will lead to    tion time. At equilibrium, a system may still undergo slow
dramatically different time evolution over long enough times.          ﬂuctuations with time, especially if it has slow internal de-
An even better way to generate independent realizations is             grees of freedom – but key properties should no longer show
to begin with different starting conﬁgurations, such as dif-           systematic trends away from their starting structure. Thus,
ferent conformations of the molecule(s) being simulated, as            for example, for biomolecular simulations it is common to
this leads to behavior which is immediately different. When            examine the root mean squared deviation (RMSD) of the


                                                                 12 of 28                         Living J. Comp. Mol. Sci. 2019, 1(1), 5957




molecules involved as a function of time, and potentially other          erally an appropriate equilibration work-ﬂow for common
properties like the number of hydrogen bonds between the                 production ensembles. Clearly, this schematic cannot cover
biomolecules present and water, as these may be slower to                every case of interest, but should provide some idea of the
equilibrate than system-wide properties like the temperature             general approach. For more information on equilibration pro-
and pressure.                                                            cedures, see Leach [7], section 7.4 and Shell [59], lectures on
                                                                         Molecular dynamics and Computing properties.

                                                                         4.3.5   Production
                                                                         Once equilibration is complete, we may begin collecting data
                                                                         for analysis. Typically this phase is called “production”. The
                                                                         main difference between equilibration and production is sim-
                                                                         ply that in the production simulation, we plan to retain and
                                                                         analyze the collected data. Production must always be pre-
                                                                         ceded by equilibration appropriate for the target production
                                                                         ensemble, and production data should never be collected im-
                                                                         mediately after a change in conditions (such as rescaling a box
                                                                         size, energy minimizing, or suddenly changing the tempera-
                                                                         ture or pressure) except in very speciﬁc applications where
                                                                         this is the goal.
Figure 4. Shown are graphs of a hypothetical computed property               For bookkeeping purposes, sometimes practitioners
(vertical axis) versus simulation time (horizontal axis). For some       choose to discard some initial production data as additional
system properties, equilibration may be relatively rapid (top panel),    equilibration; usually this is simply to allow additional
while for others it may be much slower (bottom panel). If it there is
                                                                         equilibration time after a change in protocol (such as a
ambiguity as to whether or not a key property is still systematically
changing, as in the bottom panel, equilibration should be extended.
                                                                         switch from NPT to NVT), and the usual considerations for
                                                                         equilibration apply in such cases (see Shell [59], lecture on
    Once the kinetic and potential energies ﬂuctuate around              Computing Properties).
constant values and other key properties are no longer chang-                Analysis of production is largely outside the scope of this
ing with time, the equilibration period has reached its end.             work, but requires considerable care in computing observ-
In general, if any observed properties still exhibit a system-           ables and assessing the uncertainty in any computed proper-
atic trend with respect to simulation time (e.g. Figure 4) this          ties. Usually, analysis involves computing expectation values
should be taken as a sign that equilibration is not yet com-             of particular observables, and a key consideration is to obtain
plete.                                                                   converged estimates of these properties — that is, estimates
    Depending on the target ensemble for production, the                 that are based on adequate simulation data so that they no
procedure for the end of equilibration is somewhat differ-               longer depend substantially on the length of the simulation
ent. If an NVE simulation is desired, the thermostat may be              which was run or on its initial conditions. This is closely re-
removed and a snapshot selected that is simultaneously as                lated to the above discussion of equilibration. Depending on
close to the average kinetic and potential energies as possible.         the relaxation timescales involved, one may realize only after
This snapshot, containing both positions and velocities may              analysis of a “production” trajectory that the system was still
be used to then start an NVE simulation that will correspond             equilibrating in some sense.
to a temperature close to that which is desired. This is nec-                A separate Best Practices document addresses
essary due to the fact that only the average temperature is              the critical issues of convergence and error analy-
obtained through coupling to a thermostat (see Section 4.4),             sis; we refer the reader there for more details [68]
and the temperature ﬂuctuates with the kinetic energy at                 (https://github.com/dmzuckerman/Sampling-Uncertainty).
each timestep.                                                           For more speciﬁc details on procedures and parameters used
    If the target is a simulation in the NVT ensemble at a               in production simulations, see the appropriate best practices
particular density, equilibration should be done in the NPT              document for the system of interest.
ensemble. In this case, the system may be scaled to the de-                  One other key consideration in production is what data to
sired average volume before starting a production simulation             store, and how often. Storing data especially frequently can
(and if rescaling is done, additional equilibration might be             be tempting, but utilizes a great deal of storage space and
needed).                                                                 does not actually provide signiﬁcant value in most situations.
    The schematic below (Figure 5) demonstrates what is gen-             Particularly, observations made in MD simulations are cor-


                                                                   13 of 28                        Living J. Comp. Mol. Sci. 2019, 1(1), 5957




                           Suggested equilibration workflow                                                  Production Ensemble
          NVT                                                                           NVE                                NVE
   (short simulation to                                                          (short equilibration)
  relax to temperature
       of interest)


          NVT                                                                                                              NVT
   (short simulation to                                                                                               (at known, fixed
  relax to temperature                                                                                                     density)
       of interest)


          NVT                       NPT                      NPT                        NVT                                NVT
   (short simulation to      (short simulation to     (to calculate average      (short equilibration)      (for density defined by pressure or
  relax to temperature        relax to density of            box size)                                     unknown system density distribution,
       of interest)                interest)                                                                   like a homegeneous system)


          NVT                       NPT                                                                                    NPT
   (short simulation to      (short simulation to
  relax to temperature        relax to density of
       of interest)                interest)


Figure 5. Common equilibration work-ﬂows are shown; these vary depending on the target ensemble for production simulations (right).
Typically, an initial phase of equilibration at constant volume and temperature is needed to bring the system to the desired target temperature
or energy. For stability reasons, this initial phase is usually needed even if the goal is to also bring the system to a target pressure. If the
production ensemble is an NVE ensemble, an initial NVT simulation is usually followed by a short additional NVE equilibration before collection
of production data. If the production ensemble is NVT, protocols may differ depending on whether it is necessary to allow the system to
equilibrate to a particular density/volume or whether the volume is selected a priori (second and third rows). And if production is to be NPT, it is
usually equilibrated ﬁrst at NVT before equilibrating to the target pressure (ﬁnal row).


related in time (e.g. see https://github.com/dmzuckerman/                     energies and trajectory snapshots at the same time points
Sampling-Uncertainty [68]) so storing data more frequently                    in case structural analysis is needed along with analysis of
than the autocorrelation time results in storage of essentially               energies. Since energies typically use far less space, however,
redundant data. Thus, storing data more frequently than                       these can be stored more often if desired.
intervals of the autocorrelation time is generally unneces-
sary. Of course, the autocorrelation time is not known a priori               4.4     Thermostats
which can make it necessary to store some redundant data.                     Here, we discuss why thermostats, which seek to control the
Disk space may also be a limiting factor that dictates the fre-               temperature of a simulation, are (often) needed for molec-
quency of storing data, and should at least be considered.                    ular simulations. We review background information about
Trajectory snapshots can be particularly large. However, if                   thermostats and how they work, introduce some popular
there are no disk space limitations it may be best to avoid                   thermostats, and highlight common issues to understand
discarding uncorrelated data so sampling at intervals of the                  and avoid when using thermostats in MD simulations.
autocorrelation time may be appropriate.
    If disk space proves limiting, various strategies can be used             4.4.1   Thermostats seek to maintain a target
to reduce storage use, such as storing full-precision trajectory                      temperature
snapshots only less frequently and storing reduced-precision                  As mentioned above, molecular dynamics simulations are
ones, or snapshots for only a portion of the system, more                     used to observe and glean properties of interest from some
often. However, these choices will depend on the desired                      system of study. In many cases, to emulate experiments done
analysis.                                                                     in laboratory conditions (exposed to the surroundings), sam-
    For many applications, it will likely be desirable to store               pling from the canonical (constant temperature) ensemble
                                                                              is desired [69]. Generally, if the temperature of the system


                                                                     14 of 28                                Living J. Comp. Mol. Sci. 2019, 1(1), 5957




must be maintained during the simulation, some thermostat               some of the more popular and historic thermostats used in
algorithm will be employed.                                             MD.

4.4.2   Background and How They Work                                         1. Gaussian
The temperature of a molecular dynamics simulation is typ-                           The goal of the Gaussian thermostat is to ensure
ically measured using kinetic energies                                          that the instantaneous temperature is exactly equal to
                                        DPas deﬁned       E using the
                                            N 1         2                       the target temperature. This is accomplished by modi-
equipartition theorem: 32 NkB T =           i=1 2 m i vi . The an-
gled brackets indicate that the temperature is deﬁned as a                      fying the force calculation with the form F = Finteraction +
time-averaged quantity. If we use the equipartition theorem                     Fconstraint , where Finteraction is the standard interactions
to calculate the temperature for a single snapshot in time                      calculated during the simulation and Fconstraint is a La-
of a molecular dynamics simulation [7, 21] instead of time-                     grange multiplier that keeps the kinetic energy constant.
averaging, this quantity is referred to as the instantaneous                    The reasoning for the naming of this thermostat is due
temperature. The instantaneous temperature will not always                      to its use of the Gaussian principle of least constraint to
be equal to the target temperature; in fact, in the canonical                   determine the smallest perturbative forces needed to
ensemble, the instantaneous temperature should undergo                          maintain the instantaneous temperature [69]. Clearly,
ﬂuctuations around the target temperature.                                      this thermostat does not sample the canonical distribu-
    Thermostat algorithms work by altering the Newtonian                        tion; it instead samples the isokinetic (constant kinetic
equations of motion that are inherently microcanonical (con-                    energy) ensemble. However, the isokinetic ensemble
stant energy). Thus, it is preferable that a thermostat not be                  samples the same conﬁgurational phase space as the
used if it is desired to calculate dynamical properties such                    canonical ensemble, so position-dependent (structural)
as diffusion coeﬃcients; instead, the thermostat should be                      equilibrium properties can be obtained equivalently
turned off after equilibrating the system to the desired tem-                   with either ensemble [71]. However, velocity-dependent
perature. However, while all thermostats give non-physical                      (dynamical) properties will not be equivalent between
dynamics, some have been found to have little effect on the                     the ensembles. This thermostat is used only in certain
calculation of particular dynamical properties, and they are                    advanced applications [71].
commonly used during the production simulation as well [70].                 2. Simple Velocity Rescaling
    There are several ways to categorize the many thermostat-                        The simple velocity rescaling thermostat is one of the
ting algorithms that have been developed. For example, ther-                    easiest thermostats to implement; however, this ther-
mostats can be either deterministic or stochastic depending                     mostat is also one of the most non-physical thermostats.
on whether they use random numbers to guide the dynamics,                       This thermostat relies on rescaling the momenta of the
and they can be either global or local depending on whether                     particles such that the simulation’s instantaneous tem-
they are coupled to the dynamics of the full system or of a                     perature exactly matches the target temperature [69].
small subset. Many of the global thermostats can be made                        Similarly to the Gaussian thermosat, simple velocity
into local “massive” variants by coupling separate thermostats                  rescaling aims to sample the isokinetic ensemble rather
to each particle in the system rather than having a single ther-                than the canonical ensemble. However, it has been
mostat for the whole system. There are also several methods                     shown that the simple velocity rescaling fails to properly
employed by thermostat algorithms to control the tempera-                       sample the isokinetic ensemble except in the limit of
ture. Some thermostats operate by rescaling velocities out-                     extremely small timesteps [72]. Its usage can lead to
side of the molecular dynamics’ equations of motion, e.g.,                      simulation artifacts, so it is not recommended [72, 73].
velocity rescaling is conducted after particles’ positions and               3. Berendsen
momenta have been updated by the integrator. Others in-                              The Berendsen [74] thermostat (also known as the
clude stochastic collisions between the system and an implicit                  weak coupling thermostat) is similar to the simple veloc-
bath of particles, or they explicitly include additional degrees                ity rescaling thermostat, but instead of rescaling veloci-
of freedom in the equations of motion that have the effect of                   ties completely and abruptly to the target kinetic energy,
an external heat bath.                                                          it includes a relaxation term to allow the system to more
                                                                                slowly approach the target. Although the Berendsen
4.4.3   Popular Thermostats                                                     thermostat allows for temperature ﬂuctuations, it sam-
Within this section, various thermostats will be brieﬂy ex-                     ples neither the canonical distribution nor the isokinetic
plored, with a small description of their uses and possible                     distribution. Its usage can lead to simulation artifacts,
issues that are associated with each. This is not an exhaustive                 so it is not recommended [72, 73].
study of available thermostats, but is instead a survey of just              4. Bussi-Donadio-Parrinello             (Canonical    Sampling


                                                                  15 of 28                            Living J. Comp. Mol. Sci. 2019, 1(1), 5957




   through Velocity Rescaling)                                              ing the canonical ensemble. The choice of “mass” of
       The Bussi [75] thermostat is similar to the simple ve-               the ﬁctitious particle (which in many simulation pack-
   locity rescaling and Berendsen thermostats, but instead                  ages is instead expressed as a time damping parame-
   of rescaling to a single kinetic energy that corresponds                 ter) can be important as it affects the ﬂuctuations that
   to the target temperature, the rescaling is done to a                    will be observed. For many reasonable choices of the
   kinetic energy that is stochastically chosen from the                    mass, dynamics are well-preserved [70]. This is one of
   kinetic energy distribution dictated by the canonical en-                the most widely implemented and used thermostats.
   semble. Thus, this thermostat properly samples the                       However, it should be noted that with small systems,
   canonical ensemble. Similarly to the Berendsen thermo-                   ergodicity can be an issue [69, 78]. This can become
   stat, a user-speciﬁed time coupling parameter can be                     important even in systems with larger numbers of parti-
   chosen to vary how abruptly the velocity rescaling takes                 cles if a portion of the system does not interact strongly
   place The choice of time coupling constant does not                      with the remainder of the system, such as in alchem-
   affect structural properties, and most dynamical prop-                   ical free energy calculations when a solute or ligand
   erties are fairly independent of the coupling constant                   is non-interacting. Martyna et al. [78] discovered that
   within a broad range [75].                                               by chaining thermostats, ergodicity can be enhanced,
5. Andersen                                                                 and most implementations of this thermostat use Nosé-
       The Andersen [76] thermostat works by selecting                      Hoover chains.
   particles at random and having them “collide” with a
   heat bath by giving the particle a new velocity sampled          4.4.4     Summary
   from the Maxwell-Boltzmann distribution. The number              Table 1 serves as a general summary and guide for explor-
   of particles affected, the time between “collisions”, and        ing the usage of various thermostats. Knowing the system
   how often it is applied to the system are possible vari-         you are simulating and the beneﬁts and weaknesses to each
   ations of this thermostat. The Andersen thermostat               thermostat is crucial to successfully and eﬃciently collect
   does reproduce the canonical ensemble. However, it               meaningful, physical data. If you are only interested in sam-
   should only be used to sample structural properties,             pling structural properties such as radial distribution func-
   as dynamical properties can be greatly affected by the           tions, many of the given thermostats can be used, including
   abrupt collisions.                                               the Gaussian, Bussi, Andersen, Langevin, and Nosé-Hoover
6. Langevin                                                         thermostats. If dynamical properties will be sampled, it is
       The Langevin [77] thermostat supplements the mi-             preferable to turn off the thermostat before beginning pro-
   crocanonical equations of motion with Brownian dy-               duction cycles, but the Bussi and Nosé-Hoover thermostats
   namics, thus including the viscosity and random col-             (and in cases with implicit solvent, the Langevin thermostat),
   lision effects of an implicit solvent. It uses a general         can often be used without overly affecting the calculation of
   equation of the form F = Finteraction + Ffriction + Frandom ,    dynamical properties. Since dynamical properties are unim-
   where Finteraction is the standard interactions calculated       portant during equilibration, faster algorithms like the Ander-
   during the simulation, Ffriction is the damping used to          sen or Bussi thermostats can be used, with a switch to the
   tune the “viscosity” of the implicit bath, and Frandom ef-       Nosé-Hoover thermostat for production. Overall, the Bussi
   fectively gives random collisions with solvent molecules.        thermostat has been shown to work well for most purposes,
   The frictional and random forces are coupled through             and its use is recommended as a general-purpose thermo-
   a user-speciﬁed friction damping parameter. Careful              stat.
   consideration must be taken when choosing this param-
   eter; in the limit of a zero damping parameter, both             4.5     Barostats
   frictional and random forces go to zero and the dynam-           Here, we discuss why barostats are used, give their back-
   ics become microcanonical, and in the limit of an inﬁnite        ground, discuss roughly how they work, describe some popu-
   damping parameter, the dynamics are purely Brownian.             lar options, and summarize with some recommendations.
7. Nosé-Hoover
       The Nosé-Hoover thermostat [69] abstracts away               4.5.1     Motivation
   the thermal bath from the previous thermostats and               Typically, thermodynamic properties of interest are measured
   condenses it into a single additional degree of freedom.         under open-air conditions in a laboratory, which (for short
   This ﬁctitious degree of freedom has a “mass” that can           timescales) means at they are measured at essentially
   be changed to interact with the particles in the system          constant temperature and pressure. To obtain a non-
   in a predictable and reproducible way while maintain-            atmospheric pressure, some device, like a piston, inert gas,


                                                              16 of 28                           Living J. Comp. Mol. Sci. 2019, 1(1), 5957




Table 1. Basic summary of popular thermostats. 7 indicates that the thermostat does not fulﬁll the statement, 3 indicates that the thermostat
does fulﬁll the statement, and (3) indicates that the thermostat fulﬁlls the statement under certain circumstances.


Thermostat                          Ensemble            Deterministic/         Global/      Physical?         Correct            Correct
                                                         Stochastic             Local                        Structural        Dynamical
                                                                                                            Properties?        Properties?
None                             Microcanonical          Deterministic                          3                3                   3
Gaussian                           Isokinetic            Deterministic         Global           7                3                   7
Simple Velocity Rescaling          Undeﬁned              Deterministic         Global           7                7                   7
Berendsen                          Undeﬁned              Deterministic         Global           7                7                   7
Bussi                              Canonical              Stochastic           Global           7                3                  (3)
Andersen                           Canonical              Stochastic           Local            7                3                   7
Langevin                           Canonical              Stochastic           Local            7                3                   7
Nosé-Hoover                        Canonical             Deterministic         Global           7                3                  (3)


etc., would be needed to control the pressure and volume of              directions uniformly. Since the piston is acting on the system
the system [59, 79]. Such conditions correspond to what is               from all directions, it can be considered as applying a uniform
called the isothermal-isobaric ensemble, probably one of the             compression or expansion. The mass of the piston can be
most popular ensembles for MD simulations. As is the case                tuned to change the compression of the system, which will
with thermostats, if the pressure must be maintained in a                change how often the particles in the system will interact with
simulation, a barostat algorithm will be needed to sample                the system enclosure. These impacts from the particles on
this ensemble.                                                           the “enclosure” will impart a stress on the system box from
                                                                         the surroundings and serve as a type of barostat.
4.5.2   Background and How They Work                                         The next section will describe the main differences be-
Barostat algorithms control pressure alone, not temperature,             tween the many barostats that are available, and give some
so if the target ensemble is isothermal-isobaric, they must              recommendations for proper use. Some barostats work
be applied with a thermostat. If a barostat is applied without           based on scaling or rescaling the coordinates in the sys-
a thermostat, only the number of particles (N), the pressure             tem (the volume and the center-of-mass coordinates of the
(P), and the enthalpy (H) of the system are held constant.               molecules involved), whereas others work by modifying the
This is known as the isoenthalpic-isobaric ensemble (NPH).               equations of motion to ensure constant pressure.
To sample from the isothermal-isobaric ensemble (NPT), a
thermostating algorithm like the ones discussed earlier must             4.5.3    Popular Barostats
also be applied.                                                         Here, we introduce a few notable barostats and give a high-
    Much of the background information on barostats is anal-             level summary of each, noting some key issues. This is not
ogous to thermostats. The pressure of a molecular dynamics               an exhaustive list of barostats and barostat algorithms, just a
simulation is commonly measured using the virial theorem                 sampling of popular and historic ones used in MD.
(an expectation value relating to positions and forces) [7, 59].
                                                                             1. Simple volume rescaling
When pairwise interactions and periodic boundary conditions
                                                                                    Every time this barostat is executed, the volume of
are considered, different approaches are often utilized [12,
                                                                                the system is modiﬁed such that the instantaneous pres-
59, 79]. Regardless, these formulas give pressure as a time-
                                                                                sure is exactly equal to the target pressure. This does
averaged quantity, similar to the temperature. If we use these
                                                                                not sample the proper ensemble and thus cannot be
formulas to calculate the pressure for a single snapshot, this
                                                                                used for production sampling [59]. This also does not
quantity is referred to as the instantaneous pressure. The
                                                                                smoothly approach the target pressure either, which
instantaneous pressure will not always be equal to the target
                                                                                might cause very unphysical issues with the system dur-
pressure; in fact, in the NPH and NPT ensembles, the instan-
                                                                                ing integration.
taneous pressure should undergo ﬂuctuations around the
                                                                             2. Berendsen
target pressure.
                                                                                    The Berendesen [74] weak coupling barostat is very
    For the purpose of molecular modeling, consider a hypo-
                                                                                similar to the Berendsen thermostat discussed earlier.
thetical system that is being compressed and/or expanded
                                                                                It seeks to improve upon the simple volume rescaling
by a ﬁctitious piston that has some mass which acts in all
                                                                                method mentioned above. This is achieved by coupling


                                                                  17 of 28                           Living J. Comp. Mol. Sci. 2019, 1(1), 5957




   the system to a weakly interacting pressure bath [74].               tuations. Unlike for extended system barostats, there is
   This bath scales the volume periodically by a scaling                no sense of relaxation time over which the volume of
   factor, which produces more realisitc ﬂuctuations in the             the system responds. Instead, the rate at which the vol-
   pressure as it slowly approaches the target pressure. In             ume may respond is limited by the frequency with which
   contrast to volume rescaling, Berendsen will approach                MC moves are performed and the maximum allowed
   the target pressure more realistically, but the ensemble             change in volume. Thus, long-time dynamics are not
   it is sampling from is not well deﬁned and cannot be                 accurately reproduced in any sense for MC barostats.
   guaranteed to be NPT or NPH. Berendsen can be useful
   for the beginning stages of equilibration, but should        4.5.4     Summary
   not be used for production sampling.                         The simple volume rescaling and Berendsen barostats are
3. Andersen                                                     not recommended for collection of production data, as they
        First described by Andersen [76] in 1980, the system    do not sample from any correct ensemble, nor do they utilize
   is coupled to a ﬁctitious pressure bath, by adding an ad-    any “realistic” approach to achieve the target pressure. They
   ditional degree of freedom to the equations of motion.       can, however, be used for approaching the target pressure.
   This behaves as if the system is being acted upon by         The Berendsen barostat acts in a more realistic fashion in
   an isotropic piston. This is similar to the Nosé-Hoover      this regard compared to the volume rescaling barostat, which
   thermostat, which is also an extended system algorithm.      itself is primarily useful only as a very stable thermostat for
   This barostat does sample the correct ensemble. How-         very early simulation stages if other algorithms have trou-
   ever, it is isotropic in nature and applying anisotropic     ble beginning from particularly strained starting structures.
   pressures to parts of the system is not possible.            (Alternatively, such issues can be avoided by running NVT
4. Parrinello-Rahman                                            equilibration before using a barostat, Figure 5.) Extended
        The Parrinello-Rahman [80] barostat is an extension     ensemble barostats are suitable for the production runs of
   to the Andersen barostat. Unlike the Andersen baro-          most systems. It is usually not recommended to use these
   stat, Parrinello-Rahman supports the anisotropic scaling     for the equilibration process, as these barostats do not be-
   of the size and shape of the simulation box [80]. This       have as well when not near the target pressure. These can
   can be quite useful in solid simulations, where phase        be affected by the starting conﬁguration and pressure values
   changes can be shape changes in a crystal lattice, com-      much more than the Berendsen or simple volume rescaling
   pared to a liquid or gas, which has no well deﬁned shape.    barostats. MTTK and Parinello-Rahman allow for more ﬂexi-
   This barostat has essentially the same properties as the     bility in terms of the shape modulation of the simulation box.
   Andersen one, with the additional support anisotropy.        However, not all extended-ensemble barostats have been
5. Martyna-Tuckerman-Tobias-Klein (MTTK)                        implemented all simulation engines, limiting user choice. It
        The MTTK barostat has substantial similarity to the     is recommended to begin with the Berendsen barostat to
   Parrinello-Rahman and Andersen barostats. When Parr-         quickly bring the system to the target pressure, and then
   inello-Rahman’s equations of motion were discovered          switch to an extended ensemble barostat for ﬁnal equilibra-
   to hold true only in the limit of large systems, the MTTK    tion and production.
   barostat introduced alternate equations of motion to
   correctly sample the ensemble for smaller systems as         4.6     Integrators
   well [81, 82]. Thus, MTTK [81, 82] is usually seen as        For systems consisting of more than three interacting bodies
   an improvement over Parrinello-Rahman [80] for such          with no constrained degrees of freedom, there is no analyt-
   systems.                                                     ical solution to the equations of motion. Instead, we must
6. Monte Carlo                                                  approximate the dynamics in a discrete manner. This is usu-
        Constant pressure may also be achieved by periodi-      ally termed numerical integration of the equations of motion.
   cally performing Monte Carlo moves that adjust the sys-      Algorithms to perform this integration take many forms and
   tem volume. For an explanation of how such moves are         are usually called integrators. Here, we explain the need for
   accepted or rejected, see “Monte Carlo simulations in        integrators, discuss key criteria like energy conservation, and
   other ensembles” in Shell [59]. These MC barostats are       highlight a number of commonly used integrators.
   computationally advantageous in that the virial need
   not be computed, and they may be easily extended             4.6.1     Desirable integrator properties
   to accommodate anisotropic systems. They rigorously          So-called “good” integrators contain certain features that are
   explore the correct distribution of volumes in the NPT       appealing for molecular simulations. We start with the most
   ensemble. However, they do not preserve dynamic ﬂuc-         obvious feature, which is that the integrator induces little


                                                          18 of 28                          Living J. Comp. Mol. Sci. 2019, 1(1), 5957




error in the dynamics. Since integration is fundamentally             associated with discretization error, where a shorter timestep
about taking discrete steps to approximate continuous dy-             will reduce energy drift.
namics, this discretization process introduces errors (as can              Overall, then, integrators do exhibit energy ﬂuctuations
be observed by comparison to analytically soluble problems,           that are timestep-dependent. All Verlet-equivalent integrators
like the harmonic oscillator). These errors are termed dis-           exhibit energy ﬂuctuations which decrease with the square
cretization errors, whereas additional errors called truncation       of the timestep [12], which is often an important check when
errors are also accumulated through loss of precision during          assessing the correctness of an implementation. Thus, both
computer calculations. As will be discussed shortly, there            energy drift and energy ﬂuctuations are important criteria to
are many strategies for avoiding discretization errors. For           understand when assessing integrators, and can be useful
truncation errors, the only solution is to utilize a higher preci-    measures of simulation quality in the NVE ensemble.
sion data type during calculations (i.e. use doubles instead of            Additionally, it is also desirable that an integrator be com-
ﬂoats).                                                               putationally eﬃcient. Integrator cost mostly appears in the
    Integrators that minimize discretization error should pre-        length of the timestep that may be taken while still avoiding
serve phase-space volume and conserve energy. If phase                discretization error. As discussed further below, the timestep
space volume is not preserved, then the sampled ensemble              must be at least an order of magnitude less than the smallest
at a later timestep will not be the same as that in which the         timescale of motion present in the system. However, de-
system was initialized. This means that the collected data will       pending on the accuracy of the integrator with respect to
not in fact reﬂect the ensemble of interest. Luckily, this issue      reproducing the true dynamics, a smaller timestep might be
may be avoided simply by guaranteeing that the integrator is          necessary. If the integrator requires a very small timestep
reversible [6]. More details may be found in Tuckerman et al.         to avoid discretization error, then the computational cost
[83], but basically if the mathematical operator representing         greatly increases. Hence, a truly “good” integrator allows for
the integrator preserves phase space volume, it also satis-           long timesteps while still achieving low discretization error.
ﬁes the deﬁnition of reversibility: if the operator is applied        This has the added beneﬁt of also reducing truncation er-
to propagate forward by ∆t, the starting condition may be             ror, which is proportional to the number of timesteps taken.
recovered by in turn applying the operator to the result using        It is worth noting that the issue of integrator choice versus
–∆t as the timestep.                                                  timestep is not always simple; in some cases, a “better” inte-
    Energy conservation is also a desirable integrator prop-          grator might allow longer timesteps but also carry an addi-
erty and is imperative in simulating the microcanonical (NVE)         tional computational cost that outweighs the beneﬁts of an
ensemble. This is a much trickier property to examine, and            increased timestep.
varies with different integrators. For instance, some classes
of integrators better-preserve energy over short times, while         4.6.2   Deterministic integrators
others better-preserve energy at long times. The latter is gen-       The most commonly used integrators are variants of the Ver-
erally preferred, though it may necessitate other sacriﬁces           let algorithm (e.g. Velocity Verlet or Leapfrog). Such integra-
such as greater energy ﬂuctuations away from the desired,             tors include terms for updating particle positions up to the
exact system energy. When the energy does change over the             order of the square of the timestep (i.e. they include forces).
course of a simulation, it is said to “drift.” The most common        Inclusion of higher-order terms is favored in other families
reason for energy drift is due to a timestep that is overly long.     of algorithms, but generally leads to greater complexity and
If the timestep is much too long, the system can become               reduced computational eﬃciency at only marginal improve-
unstable and blow up (energies become very large) due to              ment in accuracy. Detailed discussion and derivation of many
overlap of atoms. Even when the timestep is long enough that          common integrators may be found in section 7.3 of Leach [7]
the system is still stable over long times, it may be too long for    and 4.3 of Frenkel and Smit [6]. Such integrators are not appli-
the chosen integrator to conserve energy. Other simulation            cable, however, for simulations involving stochastic dynamics,
parameters may also impact energy drift, such as the method           as discussed below.
of truncating forces and energies, as well as the choice of
numerical precision. The latter effect, due to truncation er-         4.6.3   Stochastic integrators
rors, will become obvious if two simulations with different           Stochastic dynamics simulations include application of a ran-
timesteps are compared. Shorter timesteps, and hence more             dom force to each particle, and represent discretizations of
steps to achieve a simulation of the same length, will result in      either Langevin or Brownian dynamics. A detailed description
more drift, since errors get larger with the number of calcula-       of such stochastic dynamics may be found in McQuarrie [28],
                                                                      Chapter 20. As detailed in Section 4.4, it is common to apply
tions performed by the computer. This is exactly opposite to
the behavior that is expected for poor energy conservation            temperature control through the use of Langevin dynamics.


                                                                19 of 28                         Living J. Comp. Mol. Sci. 2019, 1(1), 5957




As a brief aside, this highlights the fact that the choice of      increased to 2 fs; coarse-grained simulations with particles
integrator is often tightly coupled to the choice of thermostat    of higher mass and smaller force constants can have much
and/or barostat. Different combinations may demonstrate            larger timesteps. After choosing a timestep, a test simulation
better performance and for expanded ensemble methods it            should be run in the microcanonical ensemble to ensure that
is necessary to utilize an integrator speciﬁc to the selected      the choice of timestep yields dynamics that conserve energy.
temperature- or pressure-control algorithm.                        The timestep should also be short enough that properties
    With Langevin or other stochastic dynamics, the random         calculated from the simulation, regardless of ensemble, are
forces usually prevent the integrator from preserving phase-       independent of the chosen timestep. This is because an in-
space volume, which ends up dictating the choice of timestep.      appropriately large timetep can lead to subtle changes to the
Speciﬁcally, despite issues with phase-space volume, some          ensemble being simulated [7, 12] and alter computed ther-
stochastic integration schemes achieve preservation of part        modynamic and transport properties, especially in stochastic
of the full phase-space (i.e. conﬁgurations or velocities are      simulations or those coupled to thermostats or barostats [84].
preserved) [84] via cancellation of error. In practice these       Methods also exist to increase the timestep beyond the limit
issues are easily remedied through an appropriate choice of        imposed by the system’s highest-frequency motion. Some
timestep depending on the integration scheme.                      examples of these enhanced timestepping algorithms include
    Stochastic dynamics necessarily perturbs dynamics.             multiple-timestep methods which separately integrate high-
Speciﬁcally, with Langevin or Brownian dynamics, calculations      frequency motion from low-frequency motion and schemes
of any dynamic properties with longer timescales than the          which repartition atomic masses to decrease the highest-
application of the random forces will be very different than       frequency motion seen in the system[85, 86].
those from deterministic trajectories. If one is interested in
only conﬁgurational or thermodynamic properties of the             4.7     Long range electrostatics
system, this is of no consequence. If dynamics are of interest,    In view of the long-range nature of Coulombic interactions
the dependence of these properties on the integrator               (Section 3.4), handling of electrostatics is particularly impor-
parameters (e.g. friction factor) should be assessed [70].         tant in many systems. Here we describe the motivation for
                                                                   the different treatments of these terms, and give an overview
4.6.4   Choosing an appropriate timestep                           of the core idea of the basic algorithms typically employed.
The maximum timestep for a molecular dynamics simulation
is dependent on the choice of integrator and the assumptions       4.7.1    Motivation
used in the integrator’s derivation. For the commonly used         The calculation of non-bonded interactions is generally the
second order integrators, such as the Verlet and Leapfrog          most time-consuming step of classical energy calculation.
algorithms, the velocities and accelerations should be approx-     While the number of type of bonded interactions remain
imately constant over the timestep. Thus, the timestep is          unchanged during an MD simulation, the strength and im-
limited by the highest frequency motion present in the sys-        portance of non-bonded interactions varies substantially as a
tem, which for all-atom simulations is usually bond vibrations.    simulation proceeds.
It is commonly found that using a timestep that is one tenth           Additionally, Coulombic interactions fall off only very
of this vibration’s characteristic period is suﬃcient to con-      slowly with distance, as r –1 , further complicating handling
serve energy in the microcanonical ensemble. For example,          of non-bonded interactions in two different ways. First,
if hydrogen molecules are present in the simulation box and        calculating all Coulomb interactions over a periodic system
the H-H bond vibration is the highest-frequency motion in          results in needing to compute a sum which is conditionally
the system with its force ﬁeld harmonic force constant set         convergent — that is, the value of the sum depends on the
to 500 N/m, the oscillation period can be calculated
                                                   q     using     order in which it is evaluated [7], meaning we must exercise
                                                     µ
the equation for simple harmonic motion (T = 2π k , where          extreme care or the result will be ambiguous. Second,
µ is the reduced mass and k is the force constant) to be 8         long-range interactions may be relevant, but determining
fs; thus, a 0.5 fs timestep can be used. As another example,       pairwise distances is an expensive computation that grows
if an ab initio MD simulation is being conducted in which          with the square of the number of atoms involved.
C-H bond vibrations are known to be the highest-frequency              As discussed in Section 4.2, simulations designed to rep-
motion, infrared spectra can be consulted to ﬁnd that this         resent bulk systems are generally performed under periodic
bond vibration frequency will be approximately 3000 cm–1 ,         boundary conditions, so that the electrostatic potential at any
which is 11 fs; thus, either a 0.5 or 1.0 fs timestep would        point is due to all the other charges in the system including
be recommended. For all-atom simulations with constraints          all of their periodic copies. Given that this is the goal, a set
on the high-frequency bonds, timesteps can be commonly             of different methods have been developed to eﬃciently com-


                                                             20 of 28                         Living J. Comp. Mol. Sci. 2019, 1(1), 5957




pute the electrostatic potential due to this inﬁnite, periodic
system.
    In the early days of simulations, electrostatic interactions
were often simply truncated at a particular cutoff radius (rc ).
This, however, creates artiﬁcial boundary effects and other
problems [12], as well as neglecting important long-range
interactions.

4.7.2    Ewald Summation
The Ewald summation technique [87] provides one way to ef-
ﬁciently handle long-range electrostatics in periodic systems.
To understand this technique, consider the relationship be-
tween the charge distribution and the Coulombic potential
written in the differential form (the Poisson equation):

                           ∇2 φ(x) = – ρ(x)                            Figure 6. Screening charge distribution. (Top) The original charge
                                      
where φ(x) is the potential at point x, ρ(x) is the charge density     distribution. (Bottom) Point charges can be split into Direct space
                                                                       (blue) and Reciprocal space charges (red). The direct space charge
at point x and  is the permittivity of the medium. The stan-
                                                                       consists of the original charges and Gaussian-distributed screening
dard way to determine the potential from this equation is to           charges of opposite sign. The reciprocal space charge is only the
ﬁrst discretize the equation and then solve, but this requires         Gaussian-distributed charge of the original sign. Together these sum
the functions ρ and φ to be smooth. However, here, because             to the original charge distribution, but computation of the electro-
                                                                       static potential due to each component becomes much easier.
we use point charge electrostatics, ρ is a set of delta functions.
    The Ewald method is based on (temporarily) replacing the
point charge distributions by smooth charge distributions in
                                                                       space whichis short-ranged   in reciprocal space, damped by
order to apply existing numerical techniques to solve this                                     
                                                                       a factor exp –k 2 σ 2 /2 where k is the reciprocal space vector
partial differential equation (PDE). The most common smooth
                                                                       and σ is the width of the Gaussian.
function used in the Ewald method is the Gaussian distribu-
                                                                           The ﬁnal term in Ewald summation is a so-called self term
tion, although other distributions have been used as well.
                                                                       which gets subtracted out of the overall sum; it is calculated
Thus the overall charge distribution is divided into a short-
                                                                       only once at the beginning of the simulation as it depends
range or “direct space” component (ρsr ) involving the original
                                                                       only on the charge magnitudes and not their positions. It also
point charges screened by the Gaussian-distributed charge of
                                                                       does not contribute to the force.
the same magnitude (Figure 6) but opposite sign, and a long-
range component involving Gaussian-distributed charges of
                                                                       4.7.3    Grid based Ewald summation
the original sign (ρlr ). The screening distribution is of opposite
                                                                       Ewald summation as described in the previous section takes
sign to allow the screened interactions to fall off rapidly with
                                                                       O(n3/2 ) time, where n is the number of charge sites. Switch-
distance, as we will see below. The sum of the short-range ρsr
                                                                       ing to a discrete Fourier transform can reduce the cost to
and the long-range ρlr charge distributions is still the same as
                                                                       to O(nlog(n)). Discretization involves spreading the charge
the original charge distribution.
                                                                       over a grid. Several common grid-based implementations are
    Unlike the original, full potential, the direct space screened
                                                                       available which tackle this problem, including Particle-Particle
interaction (Figure 6, top) decays rapidly. In fact, it decays
                                                                       Particle Mesh (P3M), Particle Mesh Ewald (PME) and Smooth
even faster than Van der Waals interactions (1/r 6 ) and hence
                                                                       Particle Mesh Ewald (SPME). Speciﬁcs are chosen in each case
relative short cutoffs, comparable to those used for Van der
                                                                       to combine accuracy, speed and ease of implementation. In
Waals interactions, can be used for handling direct-space
                                                                       this subsection, we give an overview of the grid-based ap-
Coulomb interactions (Figure 7).
                                                                       proach.
    The potential due to long-range charge interactions does
                                                                           Grid-based Ewald summation approaches involve ﬁve gen-
not decay rapidly, and thus requires consideration of all pe-
                                                                       eral steps:
riodic copies. This would pose severe problems if calculated
via direct summation, but the smoothness of the charge ρlr                  1. Charge assignment: In this step, charges are interpo-
(and hence potential (φlr ) allows the use of fast PDE solvers.                lated onto the grid. While the original PME method
Speciﬁcally, while the sum is long-ranged in real space, tak-                  uses Lagrangian interpolation for charge assignment,
ing the Fourier transform converts it into a sum in reciprocal                 the SPME method uses the smoother cardinal B-splines


                                                                 21 of 28                          Living J. Comp. Mol. Sci. 2019, 1(1), 5957




                                     Comparison of 1/r, erfc(r) and 1/r^6                              • Direct-space cutoff: This is typically kept at or near the
                 1.0                                                            1/r                      value used for the van der Waals cutoff. Decreasing
                                                                                1/r^6                    the cutoff improves the direct space performance but
                                                                                erfc(r)/r
                 0.8                                                                                     increases the complexity of the reciprocal space calcula-
                                                                                                         tions.

                 0.6

Function value
                                                                                                      In principle, it is possible to optimize settings for handling
                                                                                                  of long-range electrostatics in order to achieve considerable
                 0.4                                                                              eﬃciency gains while maintaining accuracy, though this can
                                                                                                  involve considerable care [90]. For novice users, we suggest
                                                                                                  typically using well-validated or default settings for the partic-
                 0.2
                                                                                                  ular method employed, and only deviating from these with
                                                                                                  careful consideration and testing.
                 0.0
                       1.00   1.25     1.50   1.75       2.00 2.25   2.50    2.75   3.00
                                                     distance (r)                                 5     Should you run MD?
                                                                                                  A critical question before preparing an MD simulation of your
Figure 7. Comparison of decay of the original r –1 term for Coulomb                               system is whether you even should use MD for your system
interactions (blue,*), the resulting direct-space term after Gaussian
                                                                                                  in view of the resources you have and what information you
screening (black,-) and the r –6 in van der Waals term (red, -.). Note:
The value on the vertical axis has been scaled to allow easy visualiza-                           hope to obtain. MD is a tool, but it may not be the right tool
tion of the relative decay of each term.                                                          for your problem. Before beginning any study, it is critical to
                                                                                                  sort out what questions you want to answer, what resources
                                                                                                  (computational and otherwise) you have at your disposal, and
                (hence the name Smooth-PME) to distribute charge onto                             whether you have any information about your system(s) of
                the grid.                                                                         interest that indicate you can realistically expect to answer
             2. Transformation of the grid to reciprocal space: A Fast                            those questions given a set of MD simulations. Try to un-
                Fourier Transform (FFT) is used to convert the charges                            derstand basic concepts of statistical uncertainty ([24] and
                on the grid to their equivalent Fourier space structure                           https://github.com/dmzuckerman/Sampling-Uncertainty [68])
                factors.                                                                          and use these to make an educated guess regarding your
             3. Energy calculation: The reciprocal space potential is                             chances of extracting pertinent and reliable information from
                calculated by solving the Poisson equation in Fourier                             your simulation.
                space, and the reciprocal space potential is then stored                              As noted above, the frequency of the fastest vibrational
                on the grid.                                                                      motions in a system of interest sets a fundamental limit on
             4. Transformation of the grid back to real space: An In-                             the timestep which, given ﬁxed computational resources, sets
                verse FFT is used to convert the reciprocal space poten-                          a limit on how much simulation time can be covered with
                tial back to the real space.                                                      any reasonable amount of computer time. Thus, as noted
             5. Force calculation: The force is given by the gradient of                          in Section 1, the longest all-atom MD simulations are on the
                the potential. PME [35], SPME [88] and P3M [89] use                               microsecond to millisecond timescale. This means that if your
                different methods for calculating the force given the                             system is complex and answering your questions will require
                resulting potential.                                                              sampling critical events that have a timescale of seconds or
   Optimizing the performance of grid based methods can                                           longer, MD will not be the right tool for the job. You could
be somewhat challenging; many key choices are made in                                             invest a huge amount of effort running MD simulations and
method implementation and only relative few settings are                                          ﬁnd that they did not address your questions.
exposed to the user. Some typical options include:                                                    Ideally, you should have some information before begin-
                 • Grid dimensions or spacing: A ﬁne grid would be slower,                        ning that the relevant timescales for your system might be
                   requiring interpolation and calculations for more grid                         accessible given the amount of MD you can afford to run, or
                   points, but in principle accuracy should be higher.                            you could plan a set of exploratory MD simulations to assess
                 • Screening function: The width of the Gaussian screen-                          feasibility. But do not simply plunge in and attempt to run sim-
                   ing function can often be tuned, but the ideal width                           ulations until you ﬁnd the answers to your questions, as the
                   is coupled with the direct space cutoff giving limited                         required timescales could end up being orders of magnitude
                   room for tuning. In some cases alternate, non-Gaussian                         longer than what you can afford to spend. Time is only one
                   screening functions are available.                                             consideration out of many; disk storage and computer time


                                                                                            22 of 28                          Living J. Comp. Mol. Sci. 2019, 1(1), 5957




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


                                                                    23 of 28                              Living J. Comp. Mol. Sci. 2019, 1(1), 5957




availability can also prove limiting factors, and opportunity         ulations where (for example) the composition of the system
cost, as well, is not to be overlooked.                               is varied, and conclude that any observed differences are
     Ultimately, we ought to be assessing whether MD is the           a result of variations in composition. But as noted in Sec-
best tool for the job. For our problem of interest, will it really    tion 4.3.3, even simulations started from the same structure
be faster to answer your questions using an MD simulation,            but slightly different initial positions or velocities will diverge
or are there experiments which could be done which would              over time yielding different results, so perhaps any differ-
answer the question more quickly? Maslow famously wrote,              ences are simply a result of this divergence rather than due
“I suppose it is tempting, if the only tool you have is a hammer,     to the change in conditions. Thus, analysis will require great
to treat everything as if it were a nail.” We do not want to          care and caution to avoid overinterpreting data, and error
end up in a position where we are running MD simulations              analysis becomes particularly critical (as discussed in https:
not because they are the best tool for the job, but because           //github.com/dmzuckerman/Sampling-Uncertainty [68]).
they are the only tool available to us. If an experiment could            In summary, then, do not use MD simulations simply to
answer our key questions with far less cost and time, and             make movies and inspect these. Considerable care must be
the questions are indeed compelling, perhaps our time might           exercised to avoid overinterpeting the full atomistic detail
be better spent ﬁnding a suitable experimental collaborator           they provide. While movies in some cases can be useful,
rather than running a set of simulations. To give a concrete          proper error analysis is always essential.
example, one could imagine using molecular dynamics sim-
ulations to screen a library of commercially available com-
                                                                      7    Conclusions
pounds for binding to a potential protein target, but if the
                                                                      Molecular simulations are particularly exciting, because they
compounds are commercially available at an inexpensive rate
                                                                      provide a detailed view into the structure and function of
and a suitable assay is available, it might be far faster and
                                                                      systems at a molecular or atomistic level. Additionally, they
cheaper to simply screen the compounds.
                                                                      allow us to precisely compute thermodynamic and statistical
     So, count the cost of your potential simulations, assess
                                                                      properties and connect these to underlying motions, struc-
whether they realistically have a chance of answering the
                                                                      ture, and function. Thus MD has played a signiﬁcant role in
questions you seek to answer, and then carefully decide
                                                                      our ﬁeld in suggesting new experiments, generating ideas,
whether the likelihood of success is worth the cost. If not,
                                                                      and helping to provide mechanistic understanding. Advances
don’t tackle that problem with MD.
                                                                      in hardware, software, methods and force ﬁelds also make
                                                                      MD-based calculations particularly appealing for predictive
6    Use your MD simulations and interpret                            molecular design, where simulations could be used to help
     the results with care and caution                                guide experiments to develop materials or molecules with
Analysis of molecular simulations is largely outside the scope        desired properties.
of this work; however, some words of caution are worthwhile.              Still, MD simulations require considerable care, as con-
It is tempting, especially for those new to or outside of the         ducting them requires choosing a variety of settings, and the
area, to view simulations as providing “the answer”, giving           optimal choice of settings typically depends on the problem
full mechanistic insight in atomistic detail into what happens        being considered. Thus, it is our hope that this document
in a particular situation and why it happens. Instead, MD             provides a helpful overview of some of the fundamental con-
results are better thought of as the results of a computational       siderations for preparing and conducting MD simulations
experiment that results from a particular model (including            and paves the way for more specialized documents which
force ﬁeld), system composition, and protocol. The resulting          will focus on calculations of speciﬁc properties or for speciﬁc
simulation(s) might or might not be statistically meaningful,         classes of systems, since the approach employed will often
relevant to experiment, or useful, but results will be obtained       need to vary depending on such choices.
regardless.                                                               This document also provides a checklist covering some of
     This, then, leads us to one of the real dangers of molecu-       the key points raised in this work and highlighting particularly
lar simulations: A simulation produces results, which tempt           common sources of failure; we encourage readers to follow
users to interpret or overinterpret them, whether the results         this when considering a simulation study.
are meaningful or not. For example, even a very short, un-                Our focus here has been on the basics — focusing on
equilibrated MD simulation can produce movies which ap-               things you need to understand before beginning to prepare
pear interesting and, by virtue of the fact that they result          simulations for yourself. Additionally, we have primarily fo-
from MD, reveal the positions of all the atoms in a system            cused on issues relating to how simulations are conducted,
as a function of time. It’s easy to run several short MD sim-         and leave data analysis for a separate treatment. As a start-


                                                                24 of 28                          Living J. Comp. Mol. Sci. 2019, 1(1), 5957




ing point relating to data analysis, readers should proba-               [10] Mobley DL. Let’s Get Honest about Sampling. J Comput Aided
bly review the Best Practices document on sampling and                        Mol Des. 2012; 26:93–95. https://doi.org/10.1007/s10822-011-
                                                                              9497-y.
uncertainty estimation (https://github.com/dmzuckerman/
Sampling-Uncertainty [68]).                                              [11] Chen W, Morrow BH, Shi C, Shen JK.           Recent Devel-
    Please remember that this is an updatable work, so we                     opment and Application of Constant pH Molecular Dy-
welcome contributions and suggestions via our GitHub issue                    namics.     Molecular Simulation. 2014; 40(10-11):830–838.
                                                                              https://doi.org/10.1080/08927022.2014.907492.
tracker at https://github.com/MobleyLab/basic_simulation_
training.                                                                [12] Allen MP, Tildesley DJ. Computer Simulation of Liquids. 2 ed.
                                                                              Oxford Science Publications, New York, NY: Oxford University
                                                                              Press; 2017.
Author Information
                                                                         [13] Tuckerman ME. Statistical Mechanics: Theory and Molecular
ORCID:
                                                                              Simulation. Oxford Graduate Texts, Oxford, New York: Oxford
Efrem Braun: 0000-0001-5379-7031                                              University Press; 2010.
Justin Gilmer: 0000-0002-6915-5591
Heather B. Mayes: 0000-0002-6915-5591                                    [14] Shell MS. Thermodynamics and Statistical Mechanics: An Inte-
                                                                              grated Approach. Cambridge University Press; 2015.
David L. Mobley: 0000-0002-6915-5591
Jacob I. Monroe: 0000-0002-7654-2856                                     [15] Dill KA, Bromberg S. Molecular Driving Forces: Statistical Ther-
Samarjeet Prasad: 0000-0001-8320-6482                                         modynamics in Biology, Chemistry, Physics, and Nanoscience.
                                                                              Second ed. Garland Science; 2010.
Daniel M. Zuckerman: 0000-0001-7662-2031
                                                                         [16] Kofke DA. Direct evaluation of phase coexistence by molecular
                                                                              simulation via integration along the saturation line. J Chem Phys.
References                                                                    1993; 98(5):4149–4162. https://doi.org/10.1063/1.465023.
 [1] Nussinov R. The Signiﬁcance of the 2013 Nobel Prize in Chem-
     istry and the Challenges Ahead. PLoS Comput Biol. 2014;             [17] Gonzalez Salgado D, Vega C. Melting point and phase di-
     10(1):2013–2014. https://doi.org/10.1371/journal.pcbi.1003423.           agram of methanol as obtained from computer simulations
                                                                              of the OPLS model. J Chem Phys. 2010; 132(9):094505.
 [2] Towns J, Cockerill T, Dahan M, Foster I, Gaither K, Grimshaw             https://doi.org/10.1063/1.3328667.
     A, Hazlewood V, Lathrop S, Lifka D, Peterson GD, Roskies
     R, Scott JR, Wilkens-Diehr N.      XSEDE: Accelerating Sci-         [18] Atkins P, Paula Jd. Atkins’ Physical Chemistry. Tenth revised
     entiﬁc Discovery.      Comput Sci Eng. 2014; 16(5):62–74.                edition ed. Oxford University Press; 2014.
     https://doi.org/10.1109/MCSE.2014.80.
                                                                         [19] McQuarrie DA, Simon JD. Physical Chemistry: A Molecular
 [3] Kirchmair J, Göller AH, Lang D, Kunze J, Testa B, Wilson ID,             Approach. University Science Books; 1997.
     Glen RC, Schneider G. Predicting drug metabolism: experiment
     and/or computation? Nat Rev Drug Discov. 2015; 14(6):387–404.       [20] Kittel C, Kroemer H. Thermal Physics. 2nd ed. W. H. Freeman;
     https://doi.org/10.1038/nrd4581.                                         1980.

 [4] Sresht V, Lewandowski EP, Blankschtein D, Jusuf A.                  [21] Zuckerman DM. Statistical Physics of Biomolecules: An Intro-
     Combined Molecular Dynamics Simulation–Molecular-                        duction. CRC Press; 2010.
     Thermodynamic Theory Framework for Predicting Sur-
                                                                         [22] Zuckerman DM. Equilibrium Sampling in Biomolecular Sim-
     face Tensions.         Langmuir. 2017;     33(33):8319–8329.
                                                                              ulations. Annual Review of Biophysics. 2011; 40(1):41–62.
     https://doi.org/10.1021/acs.langmuir.7b01073.
                                                                              https://doi.org/10.1146/annurev-biophys-042910-155255.
 [5] Bottaro S, Lindorff-Larsen K. Biophysical experiments and
                                                                         [23] Chong LT, Saglam AS, Zuckerman DM.            Path-Sampling
     biomolecular simulations: A perfect match? Science. 2018;
                                                                              Strategies for Simulating Rare Events in Biomolecular Sys-
     360:355–360. http://science.sciencemag.org/content/361/6400/
                                                                              tems. Current Opinion in Structural Biology. 2017; 43:88–94.
     355/tab-pdf.
                                                                              https://doi.org/10.1016/j.sbi.2016.11.019.
 [6] Frenkel D, Smit B. Understanding Molecular Simulation: From
                                                                         [24] Grossﬁeld A, Zuckerman DM. Quantifying Uncertainty and
     Algorithms to Applications. 2nd ed. Academic Press; 2001.
                                                                              Sampling Quality in Biomolecular Simulations. Annu Rep
 [7] Leach AR. Molecular Modelling: Principles and Applications.              Comput Chem. 2009; 5:23–48. https://doi.org/10.1016/S1574-
     Second ed. Essex, England: Pearson Education Limited; 2001.              1400(09)00502-7.

 [8] Jensen F. Introduction to Computational Chemistry. Second ed.       [25] Zuckerman DM, FAQ on Trajectory Ensembles | Statistical Bio-
     West Sussex, England: John Wiley & Sons; 2007.                           physics Blog; 2015.

 [9] Schlick T. Molecular Modeling and Simulation: An Interdisci-        [26] Zuckerman DM, Chong LT.          Weighted Ensemble Simu-
     plinary Guide, vol. 21 of Interdisciplinary Applied Mathematics.         lation: Review of Methodology, Applications, and Soft-
     2 ed. New York: Springer; 2010.                                          ware.    Annual Review of Biophysics. 2017; 46(1):43–57.
                                                                              https://doi.org/10.1146/annurev-biophys-070816-033834.


                                                                   25 of 28                           Living J. Comp. Mol. Sci. 2019, 1(1), 5957




[27] Reif F. Fundamentals of Statistical and Thermal Physics. Long       [42] Wang LP, McKiernan KA, Gomes J, Beauchamp KA, Head-Gordon
     Grove, IL: Waveland Press, Inc.; 2009.                                   T, Rice JE, Swope WC, Martínez TJ, Pande VS. Building a More
                                                                              Predictive Protein Force Field: A Systematic and Reproducible
[28] McQuarrie DA. Statistical Mechanics. University Science Books;           Route to AMBER-FB15. J Phys Chem B. 2017; 121(16):4023–4039.
     2000.                                                                    https://doi.org/10.1021/acs.jpcb.7b02320, pMID: 28306259.
[29] Hill TL. Statistical Mechanics: Principles and Selected Applica-    [43] Mackerell, Jr AD, Feig M, Brooks, III CL. Extending the
     tions. Dover Publications; 1987.                                         treatment of backbone energetics in protein force ﬁelds:
                                                                              Limitations of gas-phase quantum mechanics in reproduc-
[30] Chandler D. Introduction to Modern Statistical Mechanics. Ox-
                                                                              ing protein conformational distributions in molecular dynam-
     ford University Press; 1987.
                                                                              ics simulations. J Comput Chem. 2004; 25(11):1400–1415.
[31] Ponder JW, Case DA.        Force ﬁelds for protein simula-               https://doi.org/10.1002/jcc.20065.
     tions.    Advances in Protein Chemistry. 2003; 66:27–85.
                                                                         [44] Perez A, MacCallum JL, Brini E, Simmerling C, Dill KA. Grid-
     https://doi.org/10.1016/S0065-3233(03)66002-X.
                                                                              Based Backbone Correction to the ff12SB Protein Force Field
[32] Ponder JW, Wu C, Ren P, Pande VS, Chodera JD, Schnieders MJ,             for Implicit-Solvent Simulations. J Chem Theory Comput. 2015;
     Haque I, Mobley DL, Lambrecht DS, DiStasio RA, Head-Gordon               11(10):4770–4779. https://doi.org/10.1021/acs.jctc.5b00662.
     M, Clark GNI, Johnson ME, Head-Gordon T. Current Status of
                                                                         [45] Sanyal T, Shell MS. Coarse-grained models using local-density
     the AMOEBA Polarizable Force Field. J Phys Chem B. 2010;
                                                                              potentials optimized with the relative entropy: Application
     114(8):2549–2564. https://doi.org/10.1021/jp910674d.
                                                                              to implicit solvation. J Chem Phys. 2016; 145(3):034109.
[33] Lemkul JA, Huang J, Roux B, Mackerell, Jr AD.        An                  https://doi.org/10.1063/1.4958629.
     Empirical Polarizable Force Field Based on the Classical
                                                                         [46] Becker CA, Tavazza F, Trautt ZT, Buarque De Macedo RA. Con-
     Drude Oscillator Model: Development History and Re-
                                                                              siderations for choosing and using force ﬁelds and interatomic
     cent Applications.     Chem Rev. 2016; 116(9):4983–5013.
                                                                              potentials in materials science and engineering. Current Opin-
     https://doi.org/10.1021/acs.chemrev.5b00505.
                                                                              ion in Solid State and Materials Science. 2013; 17(6):277–283.
[34] York DM, Darden TA, Pedersen LG. The Effect of Long-                     https://doi.org/10.1016/j.cossms.2013.10.001.
     range Electrostatic Interactions in Simulations of Macro-
                                                                         [47] Case DA, Cerutti DS, Cheatham, III TE, Darden TA, Duke RE,
     molecular Crystals: A Comparison of the Ewald and Trun-
                                                                              Giese TJ, Gohlke H, Goetz AW, Greene D, Homeyer N, Izadi S,
     cated List Methods. J Chem Phys. 1993; 99(10):8345–8348.
                                                                              Kovalenko A, Lee TS, LeGrand S, Li P, Lin C, Liu J, Luchko T, Luo
     https://doi.org/10.1063/1.465608.
                                                                              R, Mermelstein D, et al., Amber Reference Manuals;. http://
[35] Darden T, York D, Pedersen L. Particle Mesh Ewald: An N Log( N           ambermd.org/Manuals.php.
     ) Method for Ewald Sums in Large Systems. J Chem Phys. 1993;
                                                                         [48] Apol E, Apostolov R, Berendsen HJC, van Buuren A, Bjelkmar
     98(12):10089–10092. https://doi.org/10.1063/1.464397.
                                                                              P, van Drunen R, Feenstra A, Fritsch S, Groenhof G, Junghans
[36] Piana S, Lindorff-Larsen K, Dirks RM, Salmon JK, Dror                    C, Hub J, Kasson P, Kutzner C, Lambeth B, Larsson P, Lemkul
     RO, Shaw DE.        Evaluating the Effects of Cutoffs and                JA, Lindahl V, Lundborg M, Marklund E, Meulenhoff P, et al.,
     Treatment of Long-Range Electrostatics in Protein                        GROMACS Documentation Reference Manual;. http://manual.
     Folding Simulations.        PLoS ONE. 2012; 7(6):e39918.                 gromacs.org/documentation/.
     https://doi.org/10.1371/journal.pone.0039918.
                                                                         [49] Riniker S. Fixed-Charge Atomistic Force Fields for Molecular
[37] Sagui C, Darden TA. MOLECULAR DYNAMICS SIMULATIONS OF                    Dynamics Simulations in the Condensed Phase: An Overview.
     BIOMOLECULES: Long-Range Electrostatic Effects. Annual Re-               Journal of Chemical Information and Modeling. 2018; 58(3):565–
     view of Biophysics and Biomolecular Structure. 1999; 28(1):155–          578. https://doi.org/10.1021/acs.jcim.8b00042.
     179. https://doi.org/10.1146/annurev.biophys.28.1.155.
                                                                         [50] Mishra RK, Mohamed AK, Geissbühler D, Manzano H, Jamil
[38] Cisneros GA, Karttunen M, Ren P, Sagui C. Classical Electro-             T, Shahsavari R, Kalinichev AG, Galmarini S, Tao L, Heinz
     statics for Biomolecular Simulations. Chemical Reviews. 2014;            H, Pellenq R, van Duin ACT, Parker SC, Flatt RJ, Bowen
     114(1):779–814. https://doi.org/10.1021/cr300461d.                       P. cemff: A force ﬁeld database for cementitious mate-
                                                                              rials including validations, applications and opportunities.
[39] Griﬃths DJ. Introduction to Electrodynamics. 4th ed. Cam-                Cement and Concrete Research. 2017; 102(October):68–89.
     bridge University Press; 2017.                                           https://doi.org/10.1016/j.cemconres.2017.09.003.

[40] Jackson JD. Classical Electrodynamics. 3rd ed. Wiley; 1998.         [51] Lopes PEM, Roux B, Mackerell, Jr AD. Molecular modeling and
                                                                              dynamics studies with explicit inclusion of electronic polarizabil-
[41] Mobley D, Bannan CC, Rizzi A, Bayly CI, Chodera JD, Lim VT,              ity: Theory and applications. Theoretical Chemistry Accounts.
     Lim NM, Beauchamp KA, Shirts MR, Gilson MK, Eastman PK.                  2009; 124(1-2):11–28. https://doi.org/10.1007/s00214-009-0617-
     Open Force Field Consortium: Escaping Atom Types Using Direct            x.
     Chemical Perception with SMIRNOFF v0.1. bioRxiv. 2018; p.
     286542. https://doi.org/10.1101/286542.                             [52] Onufriev AV, Izadi S. Water models for biomolecular simula-
                                                                              tions. Wiley Interdisciplinary Reviews: Computational Molecular
                                                                              Science. 2018; 8(2). https://doi.org/10.1002/wcms.1347.


                                                                   26 of 28                            Living J. Comp. Mol. Sci. 2019, 1(1), 5957




[53] Vega C, Abascal JLF.      Simulating water with rigid non-             [68] Grossﬁeld A, Patrone PN, Roe DR, Schultz A J, Siderius DW, Zuck-
     polarizable models: A general perspective.         Physical                 erman DM. Best Practices for Quantiﬁcation of Uncertainty and
     Chemistry Chemical Physics. 2011; 13(44):19663–19688.                       Sampling Quality in Molecular Simulations [Article v1.0]. Living
     https://doi.org/10.1039/c1cp22168j.                                         Journal of Computational Molecular Science. 2019; 1(1):5067.
                                                                                 https://doi.org/10.33011/livecoms.1.1.5067.
[54] Tadmor EB, Elliott, S R, Sethna JP, Miller RE, Becker CA, Knowl-
     edgebase of Interatomic Models (KIM);. https://openkim.org.            [69] Hünenberger PH. Thermostat algorithms for molecular dy-
                                                                                 namics simulations. Advanced Computer Simulation. 2005; p.
[55] Hale L, Trautt Z, Becker C, Interatomic Potentials Repository               105–149. https://doi.org/10.1007/b99427.
     Project;. https://www.ctcms.nist.gov/potentials/.
                                                                            [70] Basconi JE, Shirts MR. Effects of Temperature Control Algo-
[56] Shirts MR, Mobley DL, Chodera JD, Pande VS. Accurate and Eﬃ-                rithms on Transport Properties and Kinetics in Molecular Dy-
     cient Corrections for Missing Dispersion Interactions in Molec-             namics Simulations. J Chem Theory Comput. 2013; 9(7):2887–
     ular Simulations. J Phys Chem B. 2007; 111(45):13052–13063.                 2899. https://doi.org/10.1021/ct400109a.
     https://doi.org/10.1021/jp0735987.
                                                                            [71] Minary P, Martyna GJ, Tuckerman ME. Algorithms and novel
[57] Isele-Holder RE, Mitchell W, Ismail AE. Development and Ap-                 applications based on the isokinetic ensemble. I. Biophysical
     plication of a Particle-Particle Particle-Mesh Ewald Method for             and path integral molecular dynamics. J Chem Phys. 2003;
     Dispersion Interactions. J Chem Phys. 2012; 137(17):174107.                 118(6):2510–2526. https://doi.org/10.1063/1.1534582.
     https://doi.org/10.1063/1.4764089.
                                                                            [72] Braun E, Moosavi SM, Smit B. Anomalous effects of ve-
[58] Dupradeau FY, Pigache A, Zaffran T, Savineau C, Lelong R,                   locity rescaling algorithms: the ﬂying ice cube effect re-
     Grivel N, Lelong D, Rosanski W, Cieplak P. The R.E.D. Tools:                visited. J Chem Theory Comput. 2018; 14(10):5262–5272.
     Advances in RESP and ESP Charge Derivation and Force Field Li-              https://doi.org/10.1021/acs.jctc.8b00446.
     brary Building. Phys Chem Chem Phys. 2010; 12(28):7821–7839.
     https://doi.org/10.1039/C0CP00111B.                                    [73] Harvey SC, Tan RKZ, Cheatham TE.            The Flying Ice
                                                                                 Cube: Velocity Rescaling in Molecular Dynamics Leads
[59] Shell MS, Principles of modern molecular simulation methods:                to Violation of Energy Equipartition.       J Comp Chem.
     Lecture Notes;. https://engineering.ucsb.edu/~shell/che210d/                1998; 19(7):726–740.     https://doi.org/10.1002/(SICI)1096-
     assignments.html.                                                           987X(199805)19:7<726::AID-JCC4>3.0.CO;2-S.
[60] Yeh IC, Hummer G. System-Size Dependence of Diffusion                  [74] Berendsen HJ, Postma Jv, van Gunsteren WF, DiNola A, Haak J.
     Coeﬃcients and Viscosities from Molecular Dynamics Simula-                  Molecular dynamics with coupling to an external bath. J Chem
     tions with Periodic Boundary Conditions. J Phys Chem B. 2004;               Phys. 1984; 81(8):3684–3690. https://doi.org/10.1063/1.448118.
     108(40):15873–15879. https://doi.org/10.1021/jp0477147.
                                                                            [75] Bussi G, Donadio D, Parrinello M.        Canonical sampling
[61] Lemkul J, GROMACS Tutorials;. http://www.bevanlab.biochem.                  through velocity rescaling. J Chem Phys. 2007; 126(1):014101.
     vt.edu/Pages/Personal/justin/gmx-tutorials.                                 https://doi.org/10.1063/1.2408420.
[62] Madej B, Walker R, AMBER Tutorial B0: An Introduction to Molec-        [76] Andersen HC. Molecular dynamics simulations at constant
     ular Dynamics Simulations Using AMBER;. http://ambermd.org/                 pressure and/or temperature. J Chem Phys. 1980; 72(4):2384–
     tutorials/basic/tutorial0/index.html.                                       2393. https://doi.org/10.1063/1.439486.
[63] Jewett A, Moltemplate; 2018. https://www.moltemplate.org/.             [77] Schneider T, Stoll E. Molecular-dynamics study of a three-
                                                                                 dimensional one-component model for distortive phase
[64] Martínez L, Andrade R, Birgin EG, Martínez JM. PACKMOL: A
                                                                                 transitions.    Physical Review B. 1978; 17(3):1302–1322.
     Package for Building Initial Conﬁgurations for Molecular Dy-
                                                                                 https://doi.org/10.1103/physrevb.17.1302.
     namics Simulations. J Comp Chem. 2009; 30(13):2157–2164.
     https://doi.org/10.1002/jcc.21224.                                     [78] Martyna GJ, Klein ML, Tuckerman M. Nosé–Hoover chains: the
                                                                                 canonical ensemble via continuous dynamics. J Chem Phys.
[65] Hirel P. Atomsk: A Tool for Manipulating and Converting Atomic
                                                                                 1992; 97(4):2635–2643. https://doi.org/10.1063/1.463940.
     Data Files. Computer Physics Communications. 2015; 197:212–
     219. https://doi.org/10.1016/j.cpc.2015.07.012.                        [79] Tuckerman M. Statistical mechanics: theory and molecular
                                                                                 simulation. Oxford university press; 2010.
[66] Joswiak MN, Duff N, Doherty MF, Peters B. Size-Dependent
     Surface Free Energy and Tolman-Corrected Droplet Nucleation            [80] Parrinello M, Rahman A.         Polymorphic transitions in
     of TIP4P/2005 Water. J Phys Chem Letters. 2013; 4(24):4267–                 single crystals:     A new molecular dynamics method.
     4272. https://doi.org/10.1021/jz402226p, pMID: 26296177.                    Journal of Applied Physics. 1981;        52(12):7182–7190.
                                                                                 https://doi.org/10.1063/1.328693.
[67] Palmer JC, Haji-Akbari A, Singh RS, Martelli F, Car R, Pana-
     giotopoulos AZ, Debenedetti PG. Comment on "The puta-                  [81] Martyna GJ, Tobias DJ, Klein ML. Constant pressure molecular
     tive liquid-liquid transition is a liquid-solid transition in atom-         dynamics algorithms. J Chem Phys. 1994; 101(5):4177–4189.
     istic models of water" [I and II: J. Chem. Phys. 135, 134503                https://doi.org/10.1063/1.467468.
     (2011); J. Chem. Phys. 138, 214504 (2013)]. J Chem Phys. 2018;
     148(13):137101. https://doi.org/10.1063/1.5029463.


                                                                      27 of 28                           Living J. Comp. Mol. Sci. 2019, 1(1), 5957




[82] Martyna GJ, Tuckerman ME, Tobias DJ, Klein ML.       Ex-
     plicit reversible integrators for extended systems dy-
     namics.        Molecular Physics. 1996; 87(5):1117–1157.
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

[86] Hopkins CW, Le Grand S, Walker RC, Roitberg AE. Long-
     time-step molecular dynamics through hydrogen mass repar-
     titioning. J Chem Theory Comput. 2015; 11(4):1864–1874.
     https://doi.org/10.1021/ct5010406.

[87] Ewald PP. Die Berechnung optischer und elektrostatischer
     Gitterpotentiale. Annalen der Physik. 1921; 369(3):253–287.
     https://doi.org/10.1002/andp.19213690304.

[88] Essmann U, Perera L, Berkowitz ML, Darden T, Lee H, Pedersen
     LG. A smooth particle mesh Ewald method. J Chem Phys. 1995;
     103(19):8577–8593. https://doi.org/10.1063/1.470117.

[89] Eastwood JW, Hockney RW, Lawrence DN. P3M3DP—The
     three-dimensional periodic particle-particle/particle-mesh pro-
     gram. Computer Physics Communications. 1980; 19(2):215–261.
     https://doi.org/https://doi.org/10.1016/0010-4655(80)90052-1.

[90] Paliwal H, Shirts MR. Using Multistate Reweighting to Rapidly
     and Eﬃciently Explore Molecular Simulation Parameters Space
     for Nonbonded Interactions. J Chem Theory Comput. 2013;
     9(11):4700–4717. https://doi.org/10.1021/ct4005068.

[91] Ross GA, Rustenburg AS, Grinaway PB, Fass J, Chodera
     JD. Biomolecular Simulations under Realistic Macroscopic
     Salt Conditions. J Phys Chem B. 2018; 122(21):5466–5486.
     https://doi.org/10.1021/acs.jpcb.7b11734.


                                                                   28 of 28                Living J. Comp. Mol. Sci. 2019, 1(1), 5957
