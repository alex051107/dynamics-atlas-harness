# Rotational Dynamics of Proteins from Spin Relaxation Times and Molecular Dynamics Simulations

**Authors:** O. H. Samuli Ollila, Harri A. Heikkinen, Hideo Iwaï
**Year:** 2018
**Venue:** The Journal of Physical Chemistry B
**DOI:** 10.1021/acs.jpcb.8b02250
**Source PDF URL:** https://europepmc.org/articles/PMC6150695?pdf=render
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

This is an open access article published under a Creative Commons Attribution (CC-BY)
                                                        License, which permits unrestricted use, distribution and reproduction in any medium,
                                                        provided the author and source are cited.

                                                                                                                                                       Article

                                                         Cite This: J. Phys. Chem. B 2018, 122, 6559−6569                                  pubs.acs.org/JPCB

Rotational Dynamics of Proteins from Spin Relaxation Times and
Molecular Dynamics Simulations
O. H. Samuli Ollila,*,†,‡ Harri A. Heikkinen,† and Hideo Iwaï†
†
 Research Program in Structural Biology and Biophysics, Institute of Biotechnology, University of Helsinki, 00014 Helsinki, Finland
‡
 Institute of Organic Chemistry and Biochemistry, Czech Academy of Sciences, 117 20 Prague 6, Czech Republic
    *
    S Supporting Information

    ABSTRACT: Conformational ﬂuctuations and rotational tumbling of proteins can be experimentally accessed with nuclear spin
    relaxation experiments. However, interpretation of molecular dynamics from the experimental data is often complicated,
    especially for molecules with anisotropic shape. Here, we apply classical molecular dynamics simulations to interpret the
    conformational ﬂuctuations and rotational tumbling of proteins with arbitrarily anisotropic shape. The direct calculation of spin
    relaxation times from simulation data did not reproduce the experimental data. This was successfully corrected by scaling the
    overall rotational diﬀusion coeﬃcients around the protein inertia axes with a constant factor. The achieved good agreement with
    experiments allowed the interpretation of the internal and overall dynamics of proteins with signiﬁcantly anisotropic shape. The
    overall rotational diﬀusion was found to be Brownian, having only a short subdiﬀusive region below 0.12 ns. The presented
    methodology can be applied to interpret rotational dynamics and conformation ﬂuctuations of proteins with arbitrary anisotropic
    shape. However, a water model with more realistic dynamical properties is probably required for intrinsically disordered proteins.

■    INTRODUCTION
Conformational ﬂuctuations and the entropy of proteins play a
                                                                                 and the available time scales in the simulations.17−19,28−31 The
                                                                                 main issues have been the overestimated overall rotational
signiﬁcant role in their functionality and interactions with other               diﬀusion of proteins due to inaccuracies in water models19,29,32
biomolecules. Conformational ﬂuctuations and the overall                         and the insuﬃcient accuracy of correlation functions calculated
Brownian tumbling of proteins are experimentally accessible                      from single molecules in MD simulations.30,33
through the spin relaxation times of 15N and 13C nuclei                             In this work, we overcome these issues by assuming that the
measured with nuclear magnetic resonance (NMR) techni-                           overall rotational dynamics of protein follows anisotropic rigid
ques.1−7 The spin relaxation rates have been used to, for                        body diﬀusion. Diﬀusion coeﬃcients around inertia axes are
example, analyze conformational entropies,1,8−11 binding                         directly calculated from angular displacements. The diﬀusion
entropies,1,12 resolve sampled structures,3−5,13 and validate                    coeﬃcients are then used to determine the contribution of the
molecular dynamics (MD) simulations.14−21 These analyses are                     overall rotational tumbling to the rotational correlation
almost exclusively based on the separation of the internal                       functions of N−H bonds in the protein backbone. This
conformational ﬂuctuations and the overall rotational tum-                       reduces the required simulation length for the accurate
bling.22,23 Also, the isotropic overall diﬀusion is often assumed,               determination of the rotational correlation functions. Fur-
whereas analysis of anisotropic molecules is signiﬁcantly more                   thermore, the overestimated overall Brownian tumbling rates
complicated.1,2,24−27 Thus, new approaches are needed to                         due to the inaccurate water model can be corrected during the
interpret spin relaxation times measured from anisotropic or                     correlation function calculation by scaling the diﬀusion
intrinsically disordered molecules.                                              coeﬃcients in all directions with a constant factor. The
   Classical MD simulation methods are promising tools to                        corrected correlation functions can be used to interpret the
interpret spin relaxation experiments for molecules with
signiﬁcantly anisotropic shape or correlations between internal                  Received: March 7, 2018
and overall rotational motions. Practical applications are,                      Revised: May 27, 2018
however, limited by inaccuracies in the force ﬁeld descriptions                  Published: May 29, 2018

                              © 2018 American Chemical Society            6559                                                        DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                            J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                               Article

spin relaxation experiments for proteins with arbitrarily                      where CI(t) and CO(t) are correlation functions for the internal
anisotropic shapes.                                                            dynamics and overall rotations, respectively. Conformational
   The developed approach is demonstrated by interpreting the                  ﬂuctuations can be described in this approximation by using the
experimental spin relaxation data of C-terminal domains of                     square of the order parameter with respect to molecular axes S2,
TonB proteins from Helicobacter pyroli (HpTonB-92)34 and                       which are given by the plateau of the internal rotational
from Pseudomonas aeruginosa (PaTonB-96),35 having 92 and 96                    correlation function. Timescales for the ﬂuctuations can be
residues, respectively. Both proteins have signiﬁcantly aniso-                 characterized by using the eﬀective correlation time
tropic shape, which would complicate the standard spin                                       ∞
relaxation data analysis.1,2,24−27                                                         ∫0 CI′(t )dt
■
                                                                                  τeff =
                                                                                                                                                         (7)
    METHODS
                                                                                                    C(t ) − S 2
   Spin Relaxation Experiments and Rotational Dynam-                           where C I′(t ) =   I
                                                                                                       is the reduced correlation function.23
                                                                                                1 − S2
ics of Molecules. Molecular dynamics of the protein                              The overall rotational correlation function is often described
backbone residues and spin relaxation experiments can be                       by approximating the protein as a rigid body. For arbitrarily
connected by using the spectral density J(ω)                                   anisotropic molecules, the correlation functions can be
                       ∞                                                       presented as a sum of ﬁve exponentials2,24
    J(ω) = 2  ∫0 C(t ) cos(ωt )dt                                 (1)                          5
                                                                                  CO(t ) = ∑ Aj e−t / τj
which is the Fourier transformation of the second-order
rotational correlation function for N−H bond vector                                           j=1                                                        (8)

               3                1                                              where the prefactors Aj depend on the directions of chemical
    C(t ) =      cos2 θt ′+ t −                                                bonds with respect to the molecular axes24,26 and the time
               2                2                                 (2)
                                      t′                                       constants τj are related to the diﬀusion constants around three
where θt′+t is the N−H bond angle between times t′ and t′ + t                  principal axes of a molecule (Dx , Dy , and Dz) through
and angular brackets refer to the ensemble average. Connection                 equations2,24
to the experimentally measured spin relaxation times T1, T2 and
the nuclear Overhauser eﬀect (NOE) relaxation is given by the                     τ1 = (4Dx + Dy + Dz )−1
Redﬁeld equations36,37
                                                                                  τ2 = (Dx + 4Dy + Dz )−1
    1    d N
       = NH H [J(ωH − ω N) + 3J(ω N) + 6J(ω N + ωH)]                              τ3 = (Dx + Dy + 4Dz )−1
    T1    20
              (σω N)2                                                             τ4 = [6(Dav + (Dav 2 − L2)1/2 )]−1
          +           J (ω N )
                15                                                (3)
                                                                                  τ5 = [6(Dav − (Dav 2 − L2)1/2 )]−1                                     (9)
    1     1 dNH NH
        =          [4J(0) + 3J(ω N) + J(ωH − ω N) + 6J(ωH)                     where
    T2    2 20
                          (σω N)2                                                          1                         1
       + 6J(ω N + ωH)] +          [4J(0) + 3J(ω N)]
                                                           (4)                    Dav =      (Dx + Dy + Dz ) and L2 = (Dx Dy + Dx Dz + DyDz)
                            90                                                             3                         3
                       dNH 2NH                             γ T1                   The simplest approach to extract molecular dynamics from
    NOE = 1 +                  [6J(ω N + ωH) + J(ωH − ω N)] H
                         20                                 γN                 the experimental data is the original “model-free analysis”,23
                                                                  (5)          where an isotropic diﬀusion is assumed for the overall rotation
                                                                               of the protein. This reduces eq 8 to a monoexponential form
where ωN and ωH are the Larmor angular frequencies of 15N                      and the overall rotational dynamics can be described with a
and 1H, respectively, and the number of bound protons NH = 1                   single time constant τc. Also, the internal correlation functions
for N−H bonds. The dipolar coupling constant is given by                       for each residue are assumed to decay exponentially with a
               μ0 ℏγHγN                                                        single time constant τeff toward to the square of the order
    dNH = −                                                                    parameter S2. The three parameters (τc, τeff, and S2) can be then
              4π ⟨rNH 3⟩
                                                                               successfully resolved from a ﬁt to the experimental data.
where μ0 is the magnetic constant or vacuum permeability, ℏ is                 However, the number of parameters to be ﬁtted increases if the
the reduced Planck constant, and γN and γH are the                             protein experiences an anisotropic overall diﬀusion or has
gyromagnetic constants of 15N and 1H, respectively. The                        several timescales for internal motions. In this case, the ﬁtting
average cubic length is calculated as ⟨rNH3⟩ = (0.101 nm), and                 becomes often ambiguous, even if the experimental data would
the value of Δσ = −160 ppm is used for the chemical shift                      be measured with multiple magnetic ﬁeld strengths.1,26,40 The
anisotropy of N−H bonds in proteins.37,38                                      anisotropic rotational diﬀusion is sometimes described with
  Spin relaxation experiments are typically interpreted for                    hydrodynamical calculations but they are sensitive to the
proteins by assuming that the motions related to the overall                   estimation of the hydration shell around the protein.41
Brownian tumbling and conformational ﬂuctuations are                              A rough estimate for the timescale of overall rotational
independent.39 The rotational correlation function for each                    dynamics is often given by using the T1/T2 ratio.37 This is
N−H bond can be then written as1,2,22,23,39                                    based on the assumptions that T1 and T2 are independent of
                                                                               the internal motions and that the overall dynamics is isotropic.
    C(t ) = C I(t )CO(t )                                         (6)          The spectral density then reduces to
                                                                        6560                                                     DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                       J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                            Article

                     τc′                                                     and the correlation time describing the overall rotational
   J ′(ω) = S2                                                               motion, τ′c, can be estimated by numerically minimizing the
                 1 + (ωτc′)2                                  (10)           equation

                   1 dNH NH                                                                                  (σω )2
          T1                [4J ′(0) + 3J ′(ω Ν) + J ′(ωH − ω N) + 6J ′(ωH) + 6J ′(ω N + ωH)] + 90N [4J ′(0) + 3J ′(ω N)]
             ≈ 2       20
          T2                           dNH 2NH                                                        (σω N)2
                                               [J ′( ω H − ω N ) + 3J ′( ω N ) + 6J ′( ω N + ω H )] +   15
                                                                                                              J ′(ω N)                              (11)

with respect to the experimentally measured T1/T2 ratio.                       (4) The mean square angle deviations of rotation around
    Rotational Dynamics from MD Simulations. A classical                           protein inertia axes are calculated from the MD
MD simulation gives a trajectory for each atom in the system as                    simulation trajectory.
a function of time. Rotational correlation functions for each                  (5) rotational diﬀusion constants Dx, Dy, and Dz around
bond can be then directly calculated from the trajectories by eq                   inertia axes are calculated by ﬁtting a straight line to the
2 and used to calculate the spin relaxation times through eqs                      mean square angle deviations
1−5. The resulting values can be compared to experimental
data to assess simulation model quality14−21,31,42 and to                       ⟨Δαt ′+ t 2⟩t ′ = 2Dx t
interpret experiments.21,42,43                                                   ⟨Δβt ′+ t 2⟩t ′ = 2Dyt
   The direct comparison with experiments is, however, often
complicated by the insuﬃcient statistics for the calculated                      ⟨Δγt ′+ t 2⟩t ′ = 2Dz t                                            (12)
correlation functions and the overestimated rotational diﬀusion
due to inaccuracies in the used water models.29,30,32 Here, we               where ⟨Δαt′+t ⟩t′, ⟨Δβt′+t ⟩t′, and ⟨Δγt′+t ⟩t′ are the mean square
                                                                                             2             2          2

show that the statistical accuracy of the contribution of the                angle deviations of the rotation around inertia axes from the
overall tumbling to the correlation functions, CO(t), in eq 6, can           longest protein inertia axis to the shortest, respectively.
be increased for rigid proteins by directly calculating the                    (6) contribution of the overall rotational tumbling to all
diﬀusion coeﬃcients of the inertia axes. The rotational diﬀusion                   correlation functions is assumed to follow eq 8 with the
coeﬃcients can be related to the timescales τj of the correlation                  timescales τj calculated from the rotational diﬀusion
function for anisotropic rigid body rotation in eq 8 by using the                  constants by using the relations in eq 9. Weighting
relations in eq 9.24                                                               factors Aj are determined by ﬁtting the equation to the
   The rotational diﬀusion coeﬃcients are calculated by ﬁtting a                   overall rotational correlation functions calculated from
linear slope to the square angle deviation of the inertia axes (see                MD simulations in step 3.
below). Lag times up to one hundredth of the total simulation                  (7) The new correlation functions are calculated by
length were used. This is expected to be the maximum lag time                      substituting internal correlation functions, CI(t), from
for the good statistics of rotational dynamics analyzed from a                     step 2 and anisotropic rigid body rotational correlation
single molecule in MD simulations.33 Error bars for the                            functions, CO(t), from step 6 to eq 6 giving
diﬀusion coeﬃcients were deﬁned to include results when the                                         5
lag time was varied with ±1 ns. This requires less simulation                   C N(t ) = C I(t )∑ Aj e−t / τj
data for the good statistics than a direct ﬁt of the                                               j=1                                              (13)
multiexponential sum in eq 8 to the rotational correlation
function calculated from MD simulation. In addition, the                        These correlation functions are then used to calculate spin
overestimated rotational diﬀusion due to the water                           relaxation times from eqs 1−5. The incorrect overall rotational
model19,29,32 can be corrected by scaling the diﬀusion                       diﬀusion due to a water model can be corrected at this point by
coeﬃcients around all inertia axes by a constant factor. This                scaling the rotational diﬀusion coeﬃcients, that is, timescales τj,
approach takes into account the anisotropic shape of the                     with a constant factor before calculating new correlation
molecule. This is a signiﬁcant advancement to the previous                   functions from eq 13. Here, we determine the optimal scaling
studies, which assume isotropic rotational diﬀusion with a                   factors separately for each system. Scaling factors between 1
                                                                             and 4 are explored with the spacing of 0.1 and the value giving
single exponential rotational correlation function10,15−17,44 or
                                                                             the best agreement with the experimental spin relaxation data is
use order parameters to compare simulations with experimental
                                                                             selected to be the optimal scaling factor.
data.14,17,18,44                                                                Simulation and Analysis Details. All simulations were
   The practical analysis can be divided into seven steps as                 performed using Gromacs 554 software and Amber ﬀ99SB-
follows:                                                                     ILDN55 force ﬁeld for proteins. The protein was solvated to
   (1) The total rotational correlation functions C(t) for N−H               tip3p,56 tip4p,56 or OPC457 water models. Initial structures
       bond vectors in a protein are directly calculated from the            were taken from the lowest-energy NMR structures of
       MD simulation trajectory by applying eq 2.                            HpTonB-92 (PDB code: 5LW8)34 and PaTonB-96 (PDB
   (2) The rotational correlation functions for internal dynam-              code: 6FIP).35 The results from diﬀerent initial conformations
                                                                             of both proteins with the tip3p water model are shown in
       ics CI(t) are calculated from the MD simulation
                                                                             Section S2 in the Supporting Information. The temperature
       trajectory by removing the overall rotation of the protein.           was coupled to the desired value with the v-rescale thermo-
   (3) The overall and internal motions are assumed to be                    stat,58 and the pressure was isotropically set to 1 bar using a
       independent and the overall rotational correlation                    Parrinello−Rahman barostat.59 Time step was 2 fs, Lennard-
       function is calculated from eq 6 as CO(t) = C(t)/CI(t).               Jones interactions were cut oﬀ at 1.0 nm, particle mesh
                                                                      6561                                                    DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                    J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                  Article

Table 1. Simulated Systems and Rotational Diﬀusion Coeﬃcients (rad2·107/s) Calculated from Simulations
      protein         watera        T (K)b   ts (ns)c   ta (ns)d       Dx               Dy             Dz           D∥/D⊥e                Davf            ﬁlesg
    PaTonB-96         tip3p          298      400        300        4.2 ± 0.1        4.4 ± 0.1     10.4 ± 0.1     2.42 ± 0.1          6.4 ± 0.1            45
    PaTonB-96         tip4p          298      400        390       1.81 ± 0.01      2.06 ± 0.03    4.55 ± 0.03    2.35 ± 0.04        2.80 ± 0.02           46
    PaTonB-96         tip4p          310      400        390       2.60 ± 0.02      2.22 ± 0.05     5.0 ± 0.1     2.07 ± 0.09        3.26 ± 0.07           47
    PaTonB-96         OPC4           310      1200       1190      2.01 ± 0.01      2.19 ± 0.01    5.01 ± 0.03    2.39 ± 0.02        3.07 ± 0.01           48
    HpTonB-92         tip3p          310      570        370       8.25 ± 0.05      7.67 ± 0.06    15.9 ± 0.3     1.99 ± 0.06        10.6 ± 0.2            49
    HpTonB-92         tip3p          303      800        790       6.24 ± 0.02      7.04 ± 0.03    11.9 ± 0.2     1.80 ± 0.03        8.40 ± 0.07           50
    HpTonB-92         tip4p          310      470        370        3.6 ± 0.1       3.24 ± 0.01     6.3 ± 0.3      1.8 ± 0.1          4.4 ± 0.2            51
    HpTonB-92         tip4p          303      400        200        2.7 ± 0.1       2.71 ± 0.02     5.6 ± 0.5      2.1 ± 0.2          3.7 ± 0.2            52
    HpTonB-92         OPC4           310      800        790       2.85 ± 0.01      2.70 ± 0.01    5.56 ± 0.01    2.00 ± 0.01        3.70 ± 0.01           53
a                                                                                                                                                1
    Water model used in simulation. bSimulation temperature. cTotal simulation time. dAnalyzed simulation time. eD = Dz ,                D⊥ = 2 (Dx + Dy)
f       1
  Dav = 3 (Dx + Dy + Dz) gCitation to a repository containing the simulation data.

Ewald60,61 was used for electrostatics, and LINCS was used to                       The T1 and T2 relaxation times were measured using the
constrain all bond lengths.62 The simulated systems are listed in                   following series of the delays: 10, 50, 100, 200, 300, 500, 800,
Table 1 with the references giving access to the trajectories and                   1000, 1200, and 2000 ms for T1 and 16, 64, 96, 128, 156, 196,
the related simulation ﬁles. Equilibration of the trajectories was                  224, and 256 ms for T2. Recycle delays of 3.0 and 2.0 s were
followed by monitoring the protein root-mean-square-devia-                          used for T1 and T2 experiments, respectively. The relaxation
tion, inertia tensor eigenvalues, and rotation angles. Suﬃcient                     rates (R1 = 1/T1, R2 = 1/T2) were calculated as an exponential
amount of data was omitted from the beginning of simulation                         ﬁt of a single exponential decay to peak intensity values: I(t) =
trajectories to remove the signiﬁcant ﬂuctuations in these                          I0 exp(−t/T1) or I(t) = I0 exp(−t/T2), where I(t) is the peak
parameters. If such ﬂuctuations were not observed, the ﬁrst 10                      volume at a time t. The 15N{1H}-NOE measurements were
ns of the trajectory was omitted as an equilibration period.                        carried out with a recycling delay of 5.1 s with and without
   The rotational correlation functions are calculated with gmx                     saturation of the amide protons. The 15N{1H}-NOE values
rotacf from Gromacs package.63 The overall rotation was                             were derived from the volumes of the heteronuclear single-
removed for CI(t) calculation by using a ﬁt option of the gmx                       quantum coherence (HSQC) peaks using the equation of ν =
trjconv tool in Gromacs package.63 The order parameters S2                          I/I0. The relaxation data were processed and analyzed using
were determined by averaging the rotational correlation                             Bruker Dynamic Center software (version 2.1.8).

                                                                                    ■
functions from the oriented trajectory, CI(t), over the lag
times above 50 ns. The eﬀective correlation times were then                              RESULTS AND DISCUSSION
calculated by eq 7. Inertia axes of proteins were calculated with
the compute_inertia_tensor function from MDTraj python                                 Global Rotational Dynamics of the Protein. The mean
library.64                                                                          square angle deviations for the rotation of the PaTonB-96
   Spectral density was calculated by ﬁtting a sum of 471                           protein around inertia axes in the simulation with the OPC4
exponentials with timescales from 1 ps to 50 ns with                                water model are shown in Figure 1. This is the longest
logarithmic spacing                                                                 simulation data set in this work (1.2 μs), and the linear
                                                                                    behavior of the mean square angle deviations is observed for
                N
                                                                                    the lag times up to one hundredth of the total simulation length
     C N(t ) = ∑ αi e−t / τi                                                        (12 ns), which is expected to be the maximum lag time for the
                i=1                                                   (14)
                                                                                    good statistics of rotational dynamics analyzed from a single
to the new correlation function from eq 13 by using the                             molecule in MD simulations.33 Deviations from the linear
lsqnonneg routine in MATLAB.65 The Fourier transform was                            behavior are only seen with the lag times longer than this limit,
then calculated by using the analytical function for the sum of                     as also demonstrated for the shorter simulations with tip4p
exponentials                                                                        water at two diﬀerent temperatures in Figures S1 and S2 in the
                 N
                                                                                    Supporting Information. The plots with log−log scale in
                               τi                                                   Figures 1, S1, and S2 reveal a weakly subdiﬀusive region only
      J(ω) = 2∑ αi
                        1 + ω 2τi 2                                   (15)
                                                                                    below very short timescales of approximately 0.12 ns. Thus, we
                i=1
                                                                                    conclude that the protein experiences the Brownian rotational
   A similar approach has been previously used for the lamellar                     tumbling with a good approximation. The diﬀusion coeﬃcients
lipid and surfactant systems in combination with solid-state                        can be then calculated from the slope of the mean square angle
NMR experiments.66,67 All computer programs used for the                            deviations according to eq 12 by using the lag times less than
analysis are available from ref 68.                                                 one hundredth of the total MD simulation length. The error
   Spin Relaxation Experiments. NMR experiments were                                bars were calculated by varying the lag time with 1 ns to both
recorded on a Bruker Avance III HD NMR spectrometer                                 directions. The data from HpTonB-92 protein (not shown) led
operated at 1H frequency of 850.4 MHz equipped with a                               to similar conclusions.
cryogenic probe head. The longitudinal (T1), transverse (T2),                          The resulting rotational diﬀusion constants from diﬀerent
and 1H−15N-heteronuclear NOE spin relaxation times for the                          simulations are summarized in Table 1. As expected, the
backbone 15N atoms of HpTonB-9234 were collected at 303 K                           rotational diﬀusion coeﬃcients increase with the temperature
using the well-established NMR pulse sequences described                            and the decreasing size of a protein. The values are, however,
previously.37,69,70 The similarly detected spin relaxation data for                 larger than expected from the experimental T1/T2 ratio
PaTonB-96 at 298 K are also reported in another publication.35                      analyzed with eq 11 and from the previously reported values
                                                                             6562                                                   DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                          J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                Article

                                                                               Figure 2. Rotational correlation functions calculated from MD
                                                                               simulations of PaTonB-96 with the tip4p water model at 298 K for
                                                                               residues at diﬀerent regions. (Top) Total correlation functions C(t)
Figure 1. Mean square angle deviations of the rotation around inertia          calculated from MD simulation (solid lines) and new correlation
tensor axes calculated from PaTonB-96 simulation with the OPC                  functions determined from eqs 6 and 8 by using rotational diﬀusion
water model. The data are shown with linear (top) and logarithmic              constants and ﬁtted prefactors (dashed lines); (middle) correlation
scale (bottom).                                                                functions for internal motions calculated from simulation with
                                                                               removed overall protein rotation; and (bottom) correlation function
                                                                               for overall motions determined as CO(t) = C(t)/CI(t) (solid lines) and
for proteins with similar sizes,71 especially when tip3p water                 by ﬁtting to eq 8 with timescales from rotational diﬀusion coeﬃcients
model is used. Similar results were previously explained by the                in Table 1 (dashed lines).
overestimated water self-diﬀusion of the tip3p water
model.19,29,32                                                                 simulation. The new correlation functions, determined from
   The analysis leading to the new correlation functions in eq                 eq 13 and shown in Figure 2 (top, dashed lines), are
13 (see Methods section) is exempliﬁed in Figure 2 for three                   indistinguishable from the correlation functions calculated
residues located in diﬀerent domains of PaTonB-96 with                         from the original MD simulations with the lag times shorter
diﬀerent characteristic rotational dynamics. The ﬂexible C-                    than one hundredth of the total simulation time (approximately
terminus is represented by the residue 341, more rigid β-sheet                 4−12 ns), which is the maximum lag time for the good statistics
by the residue 331, and a ﬂexible loop between two β-strands                   in single-molecule MD simulations.33 This suggests that the
by residue 322 (see the labeling in Figure 6). The total                       anisotropic rigid body diﬀusion model (eq 8) and the
correlation functions C(t) of all residues in Figure 2 (top, solid             separation of internal and global motions (eq 6) are good
lines) decay toward zero within ∼10−50 ns. The internal                        approximations for the proteins studied in this work. The
correlation functions CI(t) in Figure 2 (middle) decay to a                    analytical description of the overall rotation with eq 8 in the
plateau value, which deﬁnes the square of the order parameter                  new correlation functions clearly reduces the statistical
S2. As expected, the internal correlation function for residue                 ﬂuctuations with the long lag times in Figure 2. The eﬀect is
331 in the rigid β-sheet rapidly decays to the largest order                   most visible for the ﬂexible C-terminus (residue 341) having
parameter value, whereas the correlation functions of the                      the smallest, thus the least detectable, contribution from the
residues in the loop and C-terminus decay slower to the smaller                overall rotation of the protein due to the small order
order parameter values because of the larger conformational                    parameters.
ensemble sampled by these regions.                                                Global Rotational Dynamics in Simulations and
   The overall rotational correlation functions, CO(t) = C(t)/                 Experiments. Spin relaxation times of HpTonB-92 are
CI(t), are shown in Figure 2 (bottom, solid lines). Also, the                  compared between the experiments and simulations using
correlation functions of anisotropic rigid body rotation from eq               two diﬀerent water models in Figure 3. The simulation with
8 are shown in Figure 2 (bottom, dashed lines). The timescales                 tip3p water model underestimates the T1/T2 ratios, suggesting
for the latter, τi, are given by the rotational diﬀusion coeﬃcients            too fast overall rotational diﬀusion dynamics.72 This is in
from the simulation and the relations in eq 9. The prefactors,                 agreement with the previous study, where the overestimated
Aj, are determined by ﬁtting eq 8 to the overall rotation                      rotational diﬀusion was attributed to the self-diﬀusion of
correlation functions, C O (t), calculated from the MD                         tip3p.19,29,32 On the other hand, simulation results with tip4p
                                                                        6563                                                      DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                        J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                              Article

Figure 3. 15N spin relaxation times for HpTonB-92 from experimental
data (circles) and MD simulations with diﬀerent water models
(squares).

water model show better agreement with the experimental data
in Figure 3.
   To see if the discrepancy in spin relaxation times for
simulations with tip3p water model could be explained by the
overestimated overall diﬀusion of the protein, the diﬀusion
coeﬃcients were divided by the optimal scaling factor before
applying eq 13 to calculate the new correlation functions. The
scaling factor value of 2.9 gave the best agreement with the
experimental spin relaxation data. The spin relaxation times
calculated from the new correlation functions after scaling the
rotational diﬀusion coeﬃcients with the optimal scaling factor
value are shown in Figure 4.
   Similar comparison for the spin relaxation times of PaTonB-
96 between experiments and simulations with tip3p, tip4p, and
OPC4 water models is shown in Figure 5. The experimentation
of the OPC4 water model was inspired by the recent study
reporting signiﬁcant improvements in lipid monolayer simu-
lations when this water model was used.75 The underestimation                Figure 4. (A) Structures of HpTonB-92 from the MD simulations with
of T1/T2 ratio was also observed in the simulations of PaTonB-               tip3p at 303 K (100 structures taken from 400 ns long trajectory).
                                                                             Secondary structures are color-labeled with Visual Molecular
96 with tip4p and OPC4 water models when compared with
                                                                             dynamics;73,74 α-helices are highlighted in red and β-strands in blue.
the experiments. The discrepancy is, however, less severe than               Terminal ends are labeled with N and C. The structure from left is
with tip3p, suggesting that the required scaling factor for the              rotated with approximately 150° to the ﬁgure on right. (B) Spin
overall rotational diﬀusion should be smaller for tip4p and                  relaxation times from experiments (circles) and tip3p simulations
OPC4 water models. Indeed, the spin relaxation times                         (squares) with rotational diﬀusion coeﬃcients divided by a constant
calculated from PaTonB-96 simulation with the tip4p water                    factor of 2.9 at 303 K. Order parameters and eﬀective internal
model were found to be in good agreement with the                            correlation times calculated from simulations.
experiments in Figure 6 when the diﬀusion coeﬃcients were
divided with a constant factor of 1.2, which is smaller than 2.9             Table S1 together with the corresponding coeﬃcients for self-
used for the tip3p simulation of HpTonB-92 above. The scaling                diﬀusion of water.29,57 Notably, the eﬀect of 12 °C temperature
factors used to correct the overall rotational diﬀusion of                   diﬀerence on the spin relaxation times from tip4p simulations
diﬀerent proteins with diﬀerent water models are shown in                    in Figure 5 is signiﬁcantly smaller than the observed diﬀerences
                                                                      6564                                                      DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                      J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                 Article

Figure 5. Plots of experimental (circles) and simulated (squares) spin
relaxation times for PaTonB-96.

between simulations and experiments or the changes due to the
scaling of the diﬀusion coeﬃcient.
   The scaling of the overall rotational diﬀusion coeﬃcients
with a constant factor led to a good agreement with the
experimental spin relaxation data for both systems simulated
with diﬀerent water models, as seen in Figures 4 and 6. The
good agreement with experiments suggests that the scaled
rotational diﬀusion coeﬃcients from MD simulations can be
considered as an interpretation of the anisotropic rotational
motion in NMR experiments. The scaled rotational diﬀusion
coeﬃcients from the simulations giving the best agreement with
the experimental data are summarized in Table 2. In contrast to
the unscaled diﬀusion constants in Table 1, these results are in
line with the previously reported values for proteins with similar
sizes.71 Also, the timescales, τc′, estimated from eq 11 are close
to the average diﬀusion coeﬃcient, τc = (6Dav)−1, in Table 1.
   Interpretation of Protein Internal Relaxation from MD
Simulations. The good agreement of the spin relaxation times
between the simulations with the scaled overall rotational
diﬀusion coeﬃcients and the experiments (Figures 4 and 6)                       Figure 6. (A) Structures sampled by PaTonB-96 from MD simulations
suggests that the simulations can be used to interpret the                      with tip4p at 298 K (100 structures from 400 ns long trajectory).
internal mobility of proteins from the experimental data.                       Secondary structures are color-labeled with Visual Molecular
   Only small variations between diﬀerent residues are observed                 dynamics;73,74 α-helixes and β-strands are red and blue, respectively.
for spin relaxation times of HpTonB-92 in Figure 4. This                        Residues 246−251, 320−326, and 338−342 with increased internal
indicates a rather rigid protein structure, which is also seen in               dynamics are yellow and α-helix ﬂuctuations between two orientations
                                                                                (residues 266−270) are violet in the left column. Terminal ends are
the MD simulation snapshots overlayed in Figure 4A. Only few                    labeled with N and C. The structure from left is rotated with
residues in the terminal ends show slightly enhanced                            approximately 100° to the ﬁgure on right. (B) Spin relaxation times
conformational ﬂuctuations in the MD simulation and in spin                     from experiments (circles) and tip4p simulations (squares) with
relaxation data. In addition, some deviations from the average                  rotational diﬀusion coeﬃcients divided by a constant factor of 1.2 at
spin relaxation times are observed in the experimental data                     298 K. Order parameters and eﬀective internal correlation times
close to residues 210−222. Simulations of HpTonB-92 do not                      calculated from simulations.

                                                                         6565                                                      DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                         J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                Article

Table 2. Rotational Diﬀusion Coeﬃcients (rad2·107/s)
Giving the Best Agreement with Experimental Spin
Relaxation dataa
                             HpTonB-92                 PaTonB-96
      Dx                     2.15 ± 0.01              1.51 ± 0.01
      Dy                     2.43 ± 0.01              1.72 ± 0.03
      Dz                     4.10 ± 0.01              3.79 ± 0.03
      Dav                    2.90 ± 0.03              2.30 ± 0.02
      τc (ns)b                5.7 ± 0.1                7.2 ± 0.1
      τ′c (ns)c               5.8 ± 0.1                6.9 ± 0.1
a
  For HpTonB-92 construct, the values calculated from simulation with
tip3p were scaled with 2.9 (spin relaxation data in Figure 4), and for
PaTonB-96, the values from tip4p simulation at 298 K were scaled by
1.2 (spin relaxation data in Figure 6). bτc = (6Dav)−1. cAverage overall
residues given by eq 11.
                                                                                  Figure 7. Prefactors αi corresponding to diﬀerent timescales τi
oﬀer any explanation for this observation; however, the similar                   resulting from a ﬁt of eq 14 to correlation functions from MD
region in PaTonB-96 simulation shows ﬂuctuations between                          simulation of PaTonB-96 at 298 K. The used correlation functions
                                                                                  give a good agreement with experimental spin relaxation times as
two orientations of α-helix.35 Exceptionally low order                            shown in Figure 6.
parameters and long eﬀective correlation times are observed
in simulations for residues 245−250 of HpTonB-92. Moreover,
short T1 times are experimentally observed close to this region,                  the dynamics of residue 341 probably arise from the slow
but the interpretation is not straightforward as the low T1 times                 conformational ﬂuctuations of the N-terminus, rather than the
are not reproduced by MD simulations.                                             overall rotational dynamics. This supports the conclusion that
   PaTonB-96 exhibits more internal mobility and the segments                     the large amount of sampled conformations lead to the small
with enhanced conformational ﬂuctuations are labeled with                         order parameters and large eﬀective correlation times observed
yellow color in Figure 6. The larger number of sampled                            in Figure 5. Although the separation of rotational dynamics of
conformations in both terminal ends is characterized by the low                   individual N−H bonds to diﬀerent components gives intuitively
order parameters and long eﬀective internal correlation times                     understandable results, it should be kept in mind that it is based
observed in the simulations. Enhanced conformational                              on the ﬁtting of a multiexponential sum to the simulation data
ﬂuctuations are also observed for residues 320−326, which                         and the solution of such ﬁt is not unique.
correspond to the loop between two β-strands. MD simulations
predict low order parameters and long internal eﬀective
correlation times also close to residues 266−271, which can
                                                                                  ■    CONCLUSIONS
                                                                                  The experimental spin relaxation data for protein backbone N−
be explained by two diﬀerent orientations sampled by the α-                       H bonds were successfully reproduced by using the classical
helix in this region (color-labeled with violet in Figure 6A). The                MD simulations for two diﬀerent small domains. Thus, the
orientational ﬂuctuations of the similar short helix could also                   simulation trajectories give an atomic resolution interpretation
explain the above mentioned deviations of spin relaxation times                   for protein dynamics measured with NMR experiments.
for residues 210−222 of HpTonB-92.34                                              Interpretation of the overall and internal dynamics was
   MD simulations can be used to analyze diﬀerent components                      demonstrated for two proteins with anisotropic molecular
contributing to the rotational dynamics of individual N−H                         shape and some ﬂexible regions. Interpretation of the 15N spin
bonds. In this work, we have ﬁtted a sum of 471 diﬀerent                          relaxation data measured from such proteins has been very
timescales to the correlation functions according to eq 14. Most                  challenging with the previously available methods.26,69
of the prefactors (αi in eq 14) are zero in all correlation                          The overall rotation of the studied proteins was found to be
functions after the ﬁtting; thus, the timescales τi corresponding                 Brownian, having only a small subdiﬀusive behavior with short
to nonzero prefactors are considered as the components                            timescales below ∼0.12 ns, which could be contrasted with
contributing to the total relaxation process of each N−H bond.                    crowded environments, where anomalous diﬀusion is expected
The prefactors are shown in Figure 7 for the same residues of                     to be more signiﬁcant.76 The direct analysis of classical MD
PaTonB-96, which were used to exemplify the correlation                           trajectories did not, however, reproduce the experimental 15N
functions in Figure 2. As expected for residue 322 in the rigid β-                spin relaxation data. Comparison between the rotational
sheet with large order parameter, the rotational relaxation is                    diﬀusion coeﬃcients and spin relaxation times between
dominated by timescales of ∼5.5 and ∼8 ns, matching with the                      simulations and experiments suggested that the overall
protein overall rotation. Also, the dynamics of residue 322 in                    Brownian tumbling of proteins is too rapid in the simulations,
the ﬂexible loop of PaTonB is dominated by the timescales                         in agreement with the previous report suggesting that the
around ∼8 ns corresponding to the protein overall rotation;                       discrepancy arises from the inaccuracies in water models.19,29,32
however, the fast motions from internal mobility are more                         Scaling down the anisotropic diﬀusion coeﬃcients in the
evident than for the rigid β-sheet residue. This is in agreement                  simulation data led to a good agreement with the experimental
with smaller order parameter observed in the ﬂexible loop                         data. Overall rotational diﬀusion coeﬃcients were over-
residues. On the other hand, the rotational dynamics of residue                   estimated by a factor of ∼3 in the HpTonB-92 simulations
341 in the ﬂexible N-terminus of PaTonB is dominated by                           with the tip3p water model, in line with previous
timescales below 3 ns, most likely related to the internal motion                 studies.28−30,77 Simulations with tip4p and OPC4 water models
of the protein. Contributions from timescales around ∼13 ns to                    gave the spin relaxation times in reasonable agreement with
                                                                           6566                                                   DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                        J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                    Article

experiments with scaling factors of ∼1−1.2, which are                              (4) Eisenmesser, E. Z.; Millet, O.; Labeikovsky, W.; Korzhnev, D. M.;
signiﬁcantly less than that for tip3p. The scaling factors for                   Wolf-Watz, M.; Bosco, D. A.; Skalicky, J. J.; Kay, L. E.; Kern, D.
diﬀerent proteins with diﬀerent water models are summarized                      Intrinsic Dynamics of an Enzyme Underlies Catalysis. Nature 2005,
in Table S1.                                                                     438, 117−121.
   The similarity between the correlation functions from the                       (5) Van den Bedem, H.; Fraser, J. S. Integrative, Dynamic Structural
                                                                                 Biology at Atomic Resolution−It’s About Time. Nat. Methods 2015,
original MD trajectory and the new correlation functions from
                                                                                 12, 307−318.
eq 13 suggests that the usage of the inertia axes and the                          (6) Lewandowski, J. R.; Halse, M. E.; Blackledge, M.; Emsley, L.
separation of internal and the overall rotational motions (eq 6)                 Direct Observation of Hierarchical Protein Dynamics. Science 2015,
are good approximations for the above investigated proteins.                     348, 578−581.
This is in line with the previous studies of other proteins with                   (7) Lamley, J. M.; Lougher, M. J.; Sass, H. J.; Rogowski, M.; Grzesiek,
well-deﬁned structure.10,29 However, it remains to be seen how                   S.; Lewandowski, J. R. Unraveling the Complexity of Protein Backbone
well this and other related approaches28,30,78 will succeed for                  Dynamics with Combined 13C and 15N Solid-state NMR Relaxation
intrinsically disordered proteins without the well-deﬁned shape.                 Measurements. Phys. Chem. Chem. Phys. 2015, 17, 21997−22008.
Because the correction of the incorrect overall rotational                         (8) Yang, D.; Kay, L. E. Contributions to Conformational Entropy
diﬀusion due to the water model may become highly                                Arising from Bond Vector Fluctuations Measured from NMR-Derived
complicated for such proteins, it may be necessary to employ                     Order Parameters: Application to Protein Folding. J. Mol. Biol. 1996,
a water model giving correct overall rotational diﬀusion                         263, 369−382.
coeﬃcients for biomolecules.19,32                                                  (9) Kasinath, V.; Sharp, K. A.; Wand, A. J. Microscopic Insights into
                                                                                 the NMR Relaxation-Based Protein Conformational Entropy Meter. J.
   As further demonstrated in ref 35, the approach presented in
                                                                                 Am. Chem. Soc. 2013, 135, 15092−15100.
this work can be used to interpret the rotational dynamics of                      (10) Allnér, O.; Foloppe, N.; Nilsson, L. Motions and Entropies in
proteins with anisotropic shape from 15N spin relaxation data                    Proteins as Seen in NMR Relaxation Experiments and Molecular
measured only with one magnetic ﬁeld strength. This is a                         Dynamics Simulations. J. Phys. Chem. B 2015, 119, 1114−1128.
signiﬁcant advancement over currently available methods,                           (11) Solomentsev, G.; Diehl, C.; Akke, M. Conformational Entropy
which may not be applicable in such cases, even though                           of FK506 Binding to FKBP12 Determined by Nuclear Magnetic
experimental data would be measured with multiple magnetic                       Resonance Relaxation and Molecular Dynamics Simulations. Bio-
ﬁeld strengths.                                                                  chemistry 2018, 57, 1451−1461.

■    ASSOCIATED CONTENT
* Supporting Information
 S
                                                                                   (12) Akke, M.; Brueschweiler, R.; Palmer, A. G. NMR Order
                                                                                 Parameters and Free Energy: an Analytical Approach and Its
                                                                                 Application to Cooperative Calcium(2+) Binding by Calbindin D9k.
                                                                                 J. Am. Chem. Soc. 1993, 115, 9832−9833.
The Supporting Information is available free of charge on the
                                                                                   (13) Sanchez-Medina, C.; Sekhar, A.; Vallurupalli, P.; Cerminara, M.;
ACS Publications website at DOI: 10.1021/acs.jpcb.8b02250.                       Muñoz, V.; Kay, L. E. Probing the Free Energy Landscape of the Fast-
     Mean square angle deviations of PaTonB-96 simulations                       Folding gpW Protein by Relaxation Dispersion NMR. J. Am. Chem.
     with tip4p water model at 310 K and 298 K and accuracy                      Soc. 2014, 136, 7444−7451.
     estimation of the scaling factors for the rotational                          (14) Best, R. B.; Vendruscolo, M. Determination of Protein
     diﬀusion (PDF)                                                              Structures Consistent with NMR Order Parameters. J. Am. Chem.

■
                                                                                 Soc. 2004, 126, 8090−8091.
                                                                                   (15) Showalter, S. A.; Brüschweiler, R. Validation of Molecular
     AUTHOR INFORMATION                                                          Dynamics Simulations of Biomolecules Using NMR Spin Relaxation as
Corresponding Author                                                             Benchmarks: Application to the AMBER99SB Force Field. J. Chem.
*E-mail: samuli.ollila@helsinki.ﬁ.                                               Theory Comput. 2007, 3, 961−975.
ORCID                                                                              (16) Showalter, S. A.; Johnson, E.; Rance, M.; Brüschweiler, R.
                                                                                 Toward Quantitative Interpretation of Methyl Side-Chain Dynamics
O. H. Samuli Ollila: 0000-0002-8728-1006                                         from NMR by Molecular Dynamics Simulations. J. Am. Chem. Soc.
Hideo Iwaï: 0000-0001-7376-5264                                                  2007, 129, 14146−14147.
Notes                                                                              (17) Maragakis, P.; Lindorff-Larsen, K.; Eastwood, M. P.; Dror, R.
The authors declare no competing ﬁnancial interest.                              O.; Klepeis, J. L.; Arkin, I. T.; Jensen, M. Ø.; Xu, H.; Trbovic, N.;

■   ACKNOWLEDGMENTS
Academy of Finland (277335) and Sigrid Jusélius Foundation
                                                                                 Friesner, R. A.; et al. Microsecond Molecular Dynamics Simulation
                                                                                 Shows Effect of Slow Loop Dynamics on Backbone Amide Order
                                                                                 Parameters of Proteins. J. Phys. Chem. B 2008, 112, 6155−6158.
                                                                                   (18) Trbovic, N.; Kim, B.; Friesner, R. A.; Palmer, A. G. Structural
are acknowledged for the ﬁnancial support to complete this                       Analysis of Protein Dynamics by MD Simulations and NMR Spin-
work. The Finnish Biological NMR Center is supported by                          relaxation. Proteins: Struct., Funct., Bioinf. 2008, 71, 684−694.
Biocenter Finland and HiLIFE-INFRA. We acknowledge CSC-                            (19) Debiec, K. T.; Cerutti, D. S.; Baker, L. R.; Gronenborn, A. M.;
IT center for science for computational resources.

■
                                                                                 Case, D. A.; Chong, L. T. Further along the Road Less Traveled:
                                                                                 AMBER ff15ipq, an Original Protein Force Field Built on a Self-
     REFERENCES                                                                  Consistent Physical Model. J. Chem. Theory Comput. 2016, 12, 3926−
 (1) Jarymowycz, V. A.; Stone, M. J. Fast Time Scale Dynamics of                 3947.
Protein Backbones: NMR Relaxation Methods, Applications, and                       (20) Hoffmann, F.; Mulder, F. A. A.; Schäfer, L. V. Accurate Methyl
Functional Consequences. Chem. Rev. 2006, 106, 1624−1671.                        Group Dynamics in Protein Simulations with AMBER Force Fields. J.
 (2) Korzhnev, D. M.; Billeter, M.; Arseniev, A. S.; Orekhov, V. Y.              Phys. Chem. B 2018, 122, 5038−5048, DOI: 10.1021/
NMR Studies of Brownian Tumbling and Internal Motions in                         acs.jpcb.8b02769.
Proteins. Prog. Nucl. Magn. Reson. Spectrosc. 2001, 38, 197−266.                   (21) Debiec, K. T.; Whitley, M. J.; Koharudin, L. M. I.; Chong, L. T.;
 (3) Mulder, F. A. A.; Mittermaier, A.; Hon, B.; Dahlquist, F. W.; Kay,          Gronenborn, A. M. Integrating NMR, SAXS, and Atomistic
L. E. Studying Excited States of Proteins by NMR Spectroscopy. Nat.              Simulations: Structure and Dynamics of a Two-Domain Protein.
Struct. Mol. Biol. 2001, 8, 932−935.                                             Biophys. J. 2018, 114, 839−855.

                                                                          6567                                                        DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                            J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                                                                     Article

  (22) Wennerstroem, H.; Lindman, B.; Soederman, O.; Drakenberg,                  Selective Order Parameter Analysis of NMR Relaxation Data. J. Chem.
T.; Rosenholm, J. B. Carbon-13 Magnetic Relaxation in Micellar                    Theory Comput. 2017, 13, 3276−3289.
Solutions. Influence of Aggregate Motion on T1. J. Am. Chem. Soc.                   (44) Gu, Y.; Li, D.-W.; Brüschweiler, R. NMR Order Parameter
1979, 101, 6860−6864.                                                             Determination from Long Molecular Dynamics Trajectories for
  (23) Lipari, G.; Szabo, A. Model-Free Approach to the Interpretation            Objective Comparison with Experiment. J. Chem. Theory Comput.
of Nuclear Magnetic Resonance Relaxation in Macromolecules. 1.                    2014, 10, 2599−2607.
Theory and Range of Validity. J. Am. Chem. Soc. 1982, 104, 4546−                    (45) Ollila, O. H. S. MD simulation data for Pseudomonas aeruginosa
4559.                                                                             TonB-CTD. Amber ﬀ99SB-ILDN, tip3p, 298K, Gromacs, 2018, http://
  (24) Woessner, D. E. Nuclear Spin Relaxation in Ellipsoids                      dx.doi.org/10.5281/zenodo.1244108.
Undergoing Rotational Brownian Motion. J. Chem. Phys. 1962, 37,                     (46) Ollila, O. H. S. MD simulation data for Pseudomonas aeruginosa
647−654.                                                                          TonB-CTD. Amber ﬀ99SB-ILDN, tip4p, 298K, Gromacs, 2017, https://
  (25) Shimizu, H. Effect of Molecular Shape on Nuclear Magnetic                  doi.org/10.5281/zenodo.1010415.
Relaxation. J. Chem. Phys. 1962, 37, 765−778.                                       (47) Ollila, O. H. S. MD simulation data for Pseudomonas aeruginosa
  (26) Luginbühl, P.; Pervushin, K. V.; Iwai, H.; Wüthrich, K.                  TonB-CTD. Amber ﬀ99SB-ILDN, tip4p, 310K, Gromacs, 2017, https://
Anisotropic Molecular Rotational Diffusion in 15N Spin Relaxation                 doi.org/10.5281/zenodo.1010405.
Studies of Protein Mobility. Biochemistry 1997, 36, 7305−7312.                      (48) Ollila, O. H. S. MD simulation data for Pseudomonas aeruginosa
  (27) Blake-Hall, J.; Walker, O.; Fushman, D. In Protein NMR                     TonB-CTD. Amber ﬀ99SB-ILDN, OPC4, 310K, Gromacs, 2017,
Techniques; Downing, A. K., Ed.; Humana Press: Totowa, NJ, 2004; pp               https://doi.org/10.5281/zenodo.1010437.
139−159.                                                                            (49) Ollila, O. H. S. MD simulation data for Helicobacter pylori TonB-
  (28) Prompers, J. J.; Brüschweiler, R. General Framework for                   CTD (residues 194-285) (PDB ID: 5LW8; BMRB entry: 34043).
Studying the Dynamics of Folded and Nonfolded Proteins by NMR                     Amber ﬀ99SB-ILDN, tip3p, 310K, Gromacs, 2017, https://doi.org/10.
Relaxation Spectroscopy and MD Simulation. J. Am. Chem. Soc. 2002,                5281/zenodo.1010231.
124, 4522−4534.                                                                     (50) Ollila, O. H. S. MD simulation data for Helicobacter pylori TonB-
  (29) Wong, V.; Case, D. A. Evaluating Rotational Diffusion from                 CTD (residues 194-285) (PDB ID: 5LW8; BMRB entry: 34043).
Protein MD Simulations. J. Phys. Chem. B 2008, 112, 6013−6024.                    Amber ﬀ99SB-ILDN, tip3p, 303K, Gromacs, 2017, https://doi.org/10.
  (30) Anderson, J. S.; LeMaster, D. M. Rotational Velocity Rescaling             5281/zenodo.1010141.
of Molecular Dynamics Trajectories for Direct Prediction of Protein                 (51) Ollila, O. H. S. MD simulation data for Helicobacter pylori TonB-
NMR Relaxation. Biophys. Chem. 2012, 168, 28−39.                                  CTD (residues 194-285) (PDB ID: 5LW8; BMRB entry: 34043).
  (31) Salvi, N.; Abyzov, A.; Blackledge, M. Multi-Timescale Dynamics             Amber ﬀ99SB-ILDN, tip4p, 310K, Gromacs, 2017, https://doi.org/10.
in Intrinsically Disordered Proteins from NMR Relaxation and
                                                                                  5281/zenodo.1010237.
Molecular Simulation. J. Phys. Chem. Lett. 2016, 7, 2483−2489.                      (52) Ollila, O. H. S. MD simulation data for Helicobacter pylori TonB-
  (32) Takemura, K.; Kitao, A. Water Model Tuning for Improved
                                                                                  CTD (residues 194-285) (PDB ID: 5LW8; BMRB entry: 34043).
Reproduction of Rotational Diffusion and NMR Spectral Density. J.
                                                                                  Amber ﬀ99SB-ILDN, tip4p, 303K, Gromacs, 2017, https://doi.org/10.
Phys. Chem. B 2012, 116, 6279−6287.
                                                                                  5281/zenodo.1010351.
  (33) Lu, C.-Y.; Bout, D. A. V. Effect of Finite Trajectory Length on
                                                                                    (53) Ollila, O. H. S.. MD simulation data for Helicobacter pylori
the Correlation Function Analysis of Single Molecule Data. J. Chem.
                                                                                  TonB-CTD (residues 194-285) (PDB ID: 5LW8; BMRB entry:
Phys. 2006, 125, 124701.
  (34) Ciragan, A.; Aranko, A. S.; Tascon, I.; Iwaï, H. Salt-inducible            34043). Amber ﬀ99SB-ILDN, OPC4, 310K, Gromacs, 2017, https://doi.
Protein Splicing in cis and trans by Inteins from Extremely Halophilic            org/10.5281/zenodo.1010356.
Archaea as a Novel Protein-Engineering Tool. J. Mol. Biol. 2016, 428,               (54) Abraham, M. J.; Murtola, T.; Schulz, R.; Páll, S.; Smith, J. C.;
4573−4588.                                                                        Hess, B.; Lindahl, E. GROMACS: High Performance Molecular
  (35) Oeemig, J. S.; Ollila, O. H. S.; Iwaï, H. The NMR structure of             Simulations Through Multi-level Parallelism from Laptops to
the C-terminal domain of TonB protein from Pseudomonas aeruginosa,                Supercomputers. SoftwareX 2015, 1−2, 19−25.
2018, submitted.                                                                    (55) Lindorff-Larsen, K.; Piana, S.; Palmo, K.; Maragakis, P.; Klepeis,
  (36) Abragam, A. The Principles of Nuclear Magnetism; Oxford                    J. L.; Dror, R. O.; Shaw, D. E. Improved Side-chain Torsion Potentials
University Press, 1961.                                                           for the Amber ff99SB Protein Force Field. Proteins: Struct., Funct.,
  (37) Kay, L. E.; Torchia, D. A.; Bax, A. Backbone Dynamics of                   Bioinf. 2010, 78, 1950−1958.
Proteins as Studied by Nitrogen-15 Inverse Detected Heteronuclear                   (56) Jorgensen, W. L.; Chandrasekhar, J.; Madura, J. D.; Impey, R.
NMR Spectroscopy: Application to Staphylococcal Nuclease. Bio-                    W.; Klein, M. L. Comparison of Simple Potential Functions for
chemistry 1989, 28, 8972−8979.                                                    Simulating Liquid Water. J. Chem. Phys. 1983, 79, 926−935.
  (38) Hiyama, Y.; Niu, C. H.; Silverton, J. V.; Bavoso, A.; Torchia, D.            (57) Izadi, S.; Anandakrishnan, R.; Onufriev, A. V. Building Water
A. Determination of 15N Chemical Shift Tensor via 15N-2H Dipolar                  Models: A Different Approach. J. Phys. Chem. Lett. 2014, 5, 3863−
Coupling in Boc-glycylglycyl[15N glycine]benzyl ester. J. Am. Chem.               3871.
Soc. 1988, 110, 2378−2383.                                                          (58) Bussi, G.; Donadio, D.; Parrinello, M. Canonical Sampling
  (39) Halle, B. The Physical Basis of Model-free Analysis of NMR                 Through Velocity Rescaling. J. Chem. Phys. 2007, 126, 014101.
Relaxation Data From Proteins and Complex Fluids. J. Chem. Phys.                    (59) Parrinello, M.; Rahman, A. Polymorphic Transitions in Single
2009, 131, 224507.                                                                Crystals: A New Molecular Dynamics Method. J. Appl. Phys. 1981, 52,
  (40) Dosset, P.; Hus, J.-C.; Blackledge, M.; Marion, D. Efficient               7182−7190.
Analysis of Macromolecular Rotational Diffusion from Heteronuclear                  (60) Darden, T.; York, D.; Pedersen, L. Particle Mesh Ewald: An N·
Relaxation Data. J. Biomol. NMR 2000, 16, 23−28.                                  log(N) Method for Ewald Sums in Large Systems. J. Chem. Phys. 1993,
  (41) de la Torre, J. G.; Huertas, M.; Carrasco, B. HYDRONMR:                    98, 10089−10092.
Prediction of NMR Relaxation of Globular Proteins from Atomic-                      (61) Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.;
Level Structures and Hydrodynamic Calculations. J. Magn. Reson.                   Pedersen, L. G. A Smooth Particle Mesh Ewald Potential. J. Chem.
2000, 147, 138−146.                                                               Phys. 1995, 103, 8577−8593.
  (42) Fisette, O.; Lagüe, P.; Gagné, S.; Morin, S. Synergistic                   (62) Hess, B. P-LINCS: A Parallel Linear Constraint Solver for
Applications of MD and NMR for the Study of Biological Systems.                   Molecular Simulation. J. Chem. Theory Comput. 2008, 4, 116−122.
J. Biomed. Biotechnol. 2012, 2012, 254208.                                          (63) Abraham, M.; van der Spoel, D.; Lindahl, E.; Hess, B. The
  (43) Anderson, J. S.; Hernández, G.; LeMaster, D. M. Prediction of             GROMACS development team, GROMACS user manual. Version
Bond Vector Autocorrelation Functions from Larmor Frequency-                      5.0.7, 2015.

                                                                           6568                                                        DOI: 10.1021/acs.jpcb.8b02250
                                                                                                                             J. Phys. Chem. B 2018, 122, 6559−6569
The Journal of Physical Chemistry B                                                                           Article

  (64) McGibbon, R. T.; Beauchamp, K. A.; Harrigan, M. P.; Klein, C.;
Swails, J. M.; Hernández, C. X.; Schwantes, C. R.; Wang, L.-P.; Lane,
T. J.; Pande, V. S. MDTraj: A Modern Open Library for the Analysis
of Molecular Dynamics Trajectories. Biophys. J. 2015, 109, 1528−
1532.
  (65) MATLAB, R2016a; The MathWorks, Inc., Natick, Massachu-
setts, United States.
  (66) Nowacka, A.; Bongartz, N. A.; Ollila, O. H. S.; Nylander, T.;
Topgaard, D. Signal Intensities in 1H−13C CP and INEPT MAS
NMR of Liquid Crystals. J. Magn. Reson. 2013, 230, 165−175.
  (67) Ferreira, T. M.; Ollila, O. H. S.; Pigliapochi, R.; Dabkowska, A.
P.; Topgaard, D. Model-free Estimation of the Effective Correlation
Time for C-H Bond Reorientation in Amphiphilic Bilayers: 1H-13C
Solid-state NMR and MD Simulations. J. Chem. Phys. 2015, 142,
044905.
  (68) Ollila, O. H. S. ProteinDynamics, 2017, https://doi.org/10.
5281/zenodo.1288573.
  (69) Barbato, G.; Ikura, M.; Kay, L. E.; Pastor, R. W.; Bax, A.
Backbone Dynamics of Calmodulin Studied by Nitrogen-15 Relaxation
Using Inverse Detected Two-dimensional NMR Spectroscopy: The
Central Helix is Flexible. Biochemistry 1992, 31, 5269−5278.
  (70) Farrow, N. A.; Muhandiram, R.; Singer, A. U.; Pascal, S. M.;
Kay, C. M.; Gish, G.; Shoelson, S. E.; Pawson, T.; Forman-Kay, J. D.;
Kay, L. E. Backbone Dynamics of a Free and a Phosphopeptide-
Complexed Src Homology 2 Domain Studied by 15N NMR
Relaxation. Biochemistry 1994, 33, 5984−6003.
  (71) Krishnan, V. V.; Cosman, M. An Empirical Relationship
Between Rotational Correlation Time and Solvent Accessible Surface
Area. J. Biomol. NMR 1998, 12, 177−182.
  (72) Carper, W. R.; Keller, C. E. Direct Determination of NMR
Correlation Times from Spin-Lattice and Spin-Spin Relaxation Times.
J. Phys. Chem. A 1997, 101, 3246−3250.
  (73) Frishman, D.; Argos, P. Knowledge-based Protein Secondary
Structure Assignment. Proteins: Struct., Funct., Bioinf. 1995, 23, 566−
579.
  (74) Humphrey, W.; Dalke, A.; Schulten, K. VMD − Visual
Molecular Dynamics. J. Mol. Graphics 1996, 14, 33−38.
  (75) Javanainen, M.; Lamberg, A.; Cwiklik, L.; Vattulainen, I.; Ollila,
O. H. S. Atomistic Model for Nearly Quantitative Simulations of
Langmuir Monolayers. Langmuir 2018, 34, 2565−2572.
  (76) Höfling, F.; Franosch, T. Anomalous Transport in the Crowded
World of Biological Cells. Rep. Prog. Phys. 2013, 76, 046602.
  (77) Linke, M.; Köfinger, J.; Hummer, G. Fully Anisotropic
Rotational Diffusion Tensor from Molecular Dynamics Simulations.
J. Phys. Chem. B 2018, 122, 5630.
  (78) Chen, P.-c.; Hologne, M.; Walker, O.; Hennig, J. Ab Initio
Prediction of NMR Spin Relaxation Parameters from Molecular
Dynamics Simulations. J. Chem. Theory Comput. 2018, 14, 1009−1019.

                                                                            6569             DOI: 10.1021/acs.jpcb.8b02250
                                                                                   J. Phys. Chem. B 2018, 122, 6559−6569
