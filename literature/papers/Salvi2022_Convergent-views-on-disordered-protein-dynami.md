# Convergent views on disordered protein dynamics from NMR and computational approaches

**Authors:** Nicola Salvi, Vojtěch Zapletal, Zuzana Jaseňáková, Milan Zachrdla, Petr Padrta, Subhash Narasimhan, Thorsten Marquardsen, Jean-Max Tyburn, Lukáš Žídek, Martin Blackledge, Fabien Ferrage, Pavel Kadeřávek
**Year:** 2022
**Venue:** Biophysical Journal
**DOI:** 10.1016/j.bpj.2022.09.016
**Source PDF URL:** https://europepmc.org/articles/PMC9674986?pdf=render
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Article

Convergent views on disordered protein dynamics
from NMR and computational approaches
Nicola Salvi,1 Vojt                         áková,2 Milan Zachrdla,3 Petr Padrta,4 Subhash Narasimhan,2
                   ech Zapletal,2 Zuzana Jasen
                                                   
Thorsten Marquardsen, Jean-Max Tyburn, Lukás Zı́dek,
                        5                  6               2
                                                             Martin Blackledge,1,* Fabien Ferrage,3,*
and Pavel Kaderávek4,*
  Institut de Biologie Structurale (IBS), CEA, CNRS, University Grenoble Alpes, Grenoble, France; 2National Centre for Biomolecular Research,
Faculty of Science and Central European Institute of Technology, Masaryk University, Brno, Czech Republic; 3Laboratoire des Biomole   cules,
LBM, De   partement de chimie, École normale superieure, PSL University, Sorbonne Universite, CNRS, Paris, France; 4Central European
Institute of Technology, Masaryk University, Brno, Czech Republic; 5Bruker BioSpin GmbH, Rheinstetten, Germany; and 6BioSpin,
Wissembourg Cedex, France

ABSTRACT Intrinsically disordered proteins (IDPs) or intrinsically disordered regions (IDRs) is a class of biologically important
proteins exhibiting specific biophysical characteristics. They lack a hydrophobic core, and their conformational behavior is
strongly influenced by electrostatic interactions. IDPs and IDRs are highly dynamic, and a characterization of the motions of
IDPs and IDRs is essential for their physically correct description. NMR together with molecular dynamics simulations are
the methods best suited to such a task because they provide information about dynamics of proteins with atomistic resolution.
Here, we present a study of motions of a disordered C-terminal domain of the delta subunit of RNA polymerase from Bacillus
subtilis. Positively and negatively charged residues in the studied domain form transient electrostatic contacts critical for the bio-
logical function. Our study is focused on investigation of ps-ns dynamics of backbone of the delta subunit based on analysis of
amide 15N NMR relaxation data and molecular dynamics simulations. In order to extend an informational content of NMR data to
lower frequencies, which are more sensitive to slower motions, we combined standard (high-field) NMR relaxation experiments
with high-resolution relaxometry. Altogether, we collected data reporting the relaxation at 12 different magnetic fields, resulting in
an unprecedented data set. Our results document that the analysis of such data provides a consistent description of dynamics
and confirms the validity of so far used protocols of the analysis of dynamics of IDPs also for a partially folded protein. In addition,
the potential to access detailed description of motions at the timescale of tens of ns with the help of relaxometry data is dis-
cussed. Interestingly, in our case, it appears to be mostly relevant for a region involved in the formation of temporary contacts
within the disordered region, which was previously proven to be biologically important.

  SIGNIFICANCE Dynamics of proteins is essential for their function in biological systems. The importance of the
  dynamics is even more pronounced in the case of intrinsically disordered proteins (IDPs), which lack a stable three-
  dimensional structure and are highly flexible. A combination of analyses of molecular dynamic simulations and NMR
  relaxation data provides detailed information about the motions at the ps-ns timescale, but sampling of slower motions is
  limited. We are presenting an approach overcoming this limitation by employing high-resolution relaxometry as
  demonstrated for a case study of the delta subunit of RNA polymerase from Bacillus subtilis, where it is used to describe
  biologically relevant dynamics of its C-terminal domain involved in regulation of transcription.

                                                                            INTRODUCTION
                                                                            Proteins are dynamic biomolecules that feature motions
Submitted June 11, 2022, and accepted for publication September 15, 2022.
                                                                            occurring on timescales from ps to days. It is widely
*Correspondence: martin.blackledge@ibs.fr or fabien.ferrage@ens.psl.eu      accepted that the problem of describing the functional
or pavel.kaderavek@mail.muni.cz                                             mechanisms of a protein is essentially equivalent to
Nicola Salvi’s present address is Bio Structure and Biophysics (BSB), Sa-   the problem of describing its functional dynamics with
nofi R&D, 94400 Vitry-sur-Seine, France.                                    sufficient accuracy (1). This statement is particularly rele-
Thorsten Marquardsen is deceased.                                           vant in the case of intrinsically disordered regions (IDRs)
Editor: Scott Showalter.                                                    and intrinsically disordered proteins (IDPs), which lack a
https://doi.org/10.1016/j.bpj.2022.09.016
Ó 2022 Biophysical Society.
This is an open access article under the CC BY-NC-ND license (http://
creativecommons.org/licenses/by-nc-nd/4.0/).

                                                                               Biophysical Journal 121, 3785–3794, October 18, 2022 3785
Salvi et al.

well-defined three-dimensional fold and are best described       tribution of correlation times for chain-like motions from
by an ensemble of diverse conformations sampled in solu-         the analysis of relaxation rates measured at high magnetic
tion (2,3). A direct yet often unclear link between the struc-   fields (5). It is still unclear whether the presence of addi-
tural ensemble of an IDP, the dynamics of interconversion        tional motions is masked by the particular range of time-
between conformers within such ensemble, and protein             scales HF spin relaxation is intrinsically most sensitive to,
function exists. The development of approaches to describe       even when multiple HFs are combined. Because the sensi-
this link has been the subject of considerable research effort   tivity of NMR relaxation depends on the available transition
in recent years (4–11).                                          frequencies of the spin system of interest, the range of mag-
   Among the experimental techniques applied to IDPs,            netic fields at which relaxation is measured defines the range
NMR spectroscopy is unique in providing multiple probes          of timescales of the motions that can be probed by a partic-
of dynamics, effectively covering most timescales from ps        ular set of relaxation rates (17–22). Measurements of 15N
to days with atomic resolution. In particular, in the present    relaxation at magnetic fields from 9.4 to 28 T can, in princi-
work, we focus on motions occurring on tens of ps to tens        ple, probe motions in the range of tens of ps to tens of ns,
of ns. Dynamics on these timescales is conveniently probed       with limited sensitivity above a few ns. The accurate and
by nuclear spin relaxation. High magnetic fields are, in gen-    sensitive determination of motions slower than a few ns
eral, required to obtain sufficient spectral resolution and      timescales requires measurement at magnetic fields lower
sensitivity in complex biomolecules, so relaxation is            than those allowed by high magnetic fields. Relaxation mea-
conventionally measured at high (>9.4 T) magnetic field          surements have already been performed over a much
(high-field [HF]) strengths in the case of proteins.             broader range of magnetic fields down to 0.5 mT by sacri-
   More precisely, spin relaxation probes the spectral den-      ficing high-resolution and thus the ability to assign motions
sity function J(u) which is the Fourier transform of the cor-    to any particular region of a protein (23).
relation function, describing the power dissipated by the           Recently, high-resolution relaxometry, which combines
fluctuations as a function of frequency u. Measured spin         relaxation at low magnetic fields and detection at high
relaxation rates depend on the spectral density function         magnetic fields, emerged as a promising tool to expand
evaluated at specific u values dictated by spin physics, usu-    the sampling of the spectral density function to otherwise
ally the interaction of nuclear spins with the strong magnetic   inaccessible u values while preserving the resolution and
field of the NMR magnet. For example, in the case of the         sensitivity of high-field NMR. Applications of high-resolu-
relaxation of 15N spins in the backbone of a protein used        tion relaxometry to small folded proteins have demonstrated
extensively in the present work, measured relaxation rates       enhanced sensitivity to motions with correlations times of
depend on linear combinations of the spectral density func-      hundreds of ps to a few ns, both on the backbone (24,25)
tion evaluated at the following frequencies: 0, the Larmor       and side chains (26,27).
frequency of 15N spins (uN ) and that of 1H spins (uH ). As         Insight into the nature of dynamic fluctuations that is
both uN and uH are proportional to the magnetic field            complementary to experimental NMR studies can be pro-
strength B0 , it is evident that a strategy to maximize the      vided by molecular dynamics (MD) simulations. In fact,
amount of information that can be extracted from relaxation      MD trajectories are used to calculate rotational autocorrela-
studies is to measure relaxation at as many B0 values as         tion functions of NH bond vectors (and consequently J(u)
possible, as availability of instruments, resolution, and        values) describing the reorientational properties of relaxa-
sensitivity requirements allow. It has been shown in a num-      tion-active interactions such as dipole-dipole couplings
ber of systems and experimental conditions (4,5,7,12,13)         and chemical shift anisotropy (CSA), thereby providing a
that HF relaxation data measured on disordered proteins at       direct and quantitative way of comparing simulated dy-
multiple fields can be convincingly interpreted in the frame-    namics with experimental spin relaxation rates. In the case
work of (extended) model-free (MF) analysis (14), whereby        of unfolded proteins, MD simulations have been shown to
the spectral density function is decomposed into the sum of      be largely consistent with the three-timescale model derived
three Lorentzian components, characterized by their ampli-       from MF studies (9,28,29).
tudes (Ai ) and timescales (t i ). These three components are       In this work, we perform high-resolution relaxometry, HF
associated with fast bond librations on tens of ps, intermedi-   spin relaxation measurements, and MD simulations on a
ate sampling of backbone dihedral angles on hundreds of ps,      particularly challenging half structured and half disordered
and slower chain-like motions occurring on timescales of         d subunit of RNA polymerase. The d subunit of RNA poly-
several ns (9,12).                                               merase is a subunit unique for Gram-positive bacteria that
   The timescales of these chain-like motions have been pro-     was shown to be essential for virulency of some pathogens
posed to follow a continuous distribution (15,16). An anal-      like Streptococcus agalactiae and Staphylococcus aureus
ysis based on the interpretation of motions by projection        (30), and it was demonstrated that the d subunit causes a sensi-
onto an array of correlation times (IMPACT), which uses          tivity of RNA polymerase activity to the concentration of initi-
a discretized distribution of correlation times, could not       ating nucleoside triphosphates, making the d subunit essential
identify slower motional modes or a possible tail of the dis-    for rapid changes of gene expression (31). Here, the d subunit

3786 Biophysical Journal 121, 3785–3794, October 18, 2022
                                                                                                                      IDPs dynamics by NMR and MD

of a model Gram-positive bacteria Bacillus subtilis is investi-                nonuniformly sampled (for 15N and 13C dimensions) spectra with varying
gated. The d subunit is composed from two domains: the                         relaxation delays (summarized in Table S1) were acquired for each
                                                                               magnetic field in an interleaved manner as a pseudo-four-dimensional
N-terminal domain has a well-defined structure formed by a                     experiment (experimental relaxometry relaxation rates are available in
core of three a-helices, while the C-terminal domain is disor-                 Tables S2–S4). An in-house program was used to generate the NUS
dered (32), and it does not show any propensity to form any                    schedule using Poisson discs sampling (38) with the Gauss-function used
secondary structure element within its sequence. The C-termi-                  to weight the density of sampled points. A complete set of real and imag-
nal domain is highly negatively charged except a lysine-rich                   inary components for quadrature detection in indirect dimensions were ac-
                                                                               quired, each of them measured with four scans to accumulate the signal.
motif 96KAKKKKAKK104 involved in the formation of tran-                        Additional details about the experimental setup of the high-resolution relax-
sient electrostatic contacts with negatively charged amino                     ometry measurements can be found in Table S1.
acids in the remaining parts of the C-terminal domain (32).                       Experiments for the determination of proton exchange rates with the sol-
   We combine high-resolution relaxometry measurements                         vent were carried out according to the RELAX-EXSY protocol (39) on
with HF spin relaxation data to probe as broad a range of                      samples of the delta subunit with identical composition but different con-
                                                                               tents of D2O (1%, 10%, 30%, and 50% contents of D2O was used). These
correlation times as possible in the disordered domain of                      experiments were carried out on a 600 MHz NMR spectrometer equipped
the d subunit of RNA polymerase. Although the high-field                       with a cryo-cooled 5 mm TCI probe. Relaxation delays of 44.8, 179.2,
dataset analyzed here is relatively sparse, this combination                   380.8, 627.2, and 1,030.4 ms were used.
also provides us with the opportunity to assess whether                           Steady-state nuclear Overhauser effect (NOE) experiment and measure-
low-field measurements can identify additional dynamic                         ment of longitudinal relaxation rates were carried out on an 850 MHz NMR
                                                                               spectrometer equipped with a cryo-cooled 5 mm TCI probe (BMRB: 27245)
processes to those derived from uniquely HF spin relaxation                    using the published pulse sequence for uniformly 15N and 13C labeled disor-
or indeed whether this information can be refined by prob-                     dered proteins (40). The longitudinal relaxation rates were measured with
ing the spectral density function at lower frequencies. We                     relaxation delays 0.0448, 0.0672, 0.112, 0.1792*, 0.2464, 0.3808, 0.784, and
find that all measurements are consistent and mostly report                    1.232 s (the asterisk denotes the spectra repeated twice). The saturation in
on the same three motional processes described above. This                     the steady-state NOE experiment was achieved with 5 s irradiation composed
                                                                               from inversion proton pulses separated by 22.22 ms, and the reference exper-
observation is confirmed by a detailed analysis of motions                     iment was measured with a 15 s interscan delay (41).
sampled by multi-ms MD simulation. Our results indicate
that small inconsistencies between the analyses of relaxa-
tion data measured at low and high field would be the                          NMR processing and data analysis
hallmark of IDP dynamics more complex than the state-
                                                                               All NMR spectra were processed using NMRpipe (42) software v.9.9 and
of-the-art MF model.                                                           SMILE 2.0beta (43) for the nonuniformly sampled spectra.
                                                                                  No extrapolation (NUS zero-filling) was used in the processing of the
                                                                               nonuniformly sampled data, and the same signal downscaling factor was
MATERIALS AND METHODS                                                          used for the independently processed spectra of various relaxation delays.
                                                                               The spectra were analyzed using the program NMRFAM-Sparky 1.413
Sample preparation
                                                                               (44). The extracted peak intensities of the high-resolution relaxometry
The d subunit of RNA polymerase was prepared as uniformly 15N and 13C          spectra were fitted to mono-exponential decay functions in the Octave
labeled recombinant protein expressed in Escherichia coli BL21(DE3)            3.8.2 program (45) using the function leasqr from the package optim.Errors
strain. The purification protocol is described elsewhere (33). NMR samples     of the fitted relaxation rates were estimated based on the smooth Bootstrap
contain 1.2 mM of the protein in 20 mM phosphate buffer (pH ¼ 6.6; un-         method (46,47). 300 Monte Carlo simulations for each Bootstrap sample
corrected reading) and 10 mM NaCl and 10% D2O.                                 were generated based on the estimated error of the peak intensities from
   Prepared NMR samples were degassed upon mild vacuum and sealed in a         the noise in the spectra. The steady-state NOE was determined from the ra-
special tube (25) for the high-resolution relaxometry experiments. The         tio of the peak intensities in the spectra acquired with saturation and refer-
design of the tube was modified compared with the reported prototype           ence spectra. The error of signal intensities was estimated from the noise.
(25) to increase the active sample volume to 120 mL. HF NMR experiments        The longitudinal relaxation rates were fitted in the Octave 4.0.3 program
were measured in standard 5 mm NMR tubes.                                      (45), and the error was obtained by Bootstrap method.

NMR measurements                                                               Analysis of relaxation rates
All NMR experiments were performed at (300.0 5 0.2) K, which was cali-         The high-resolution relaxometry rates were combined with previously pub-
brated using temperature standards before every measurement.                   lished longitudinal relaxation rates and steady-state NOE acquired at
   High-resolution relaxometry relaxation rates were acquired with a 600       500 MHz spectrometer; longitudinal relaxation rates, steady-state NOE,
MHz spectrometer equipped with a special 3.2 mm room-temperature               and transverse and longitudinal cross-correlated cross-relaxation rates
TXI probe and a shuttling device (25). The shuttling device allows sample      measured at 600 MHz (using a uniformly 15N labeled sample (4)); longitu-
movement along the bore of the magnet in order to reach a position corre-      dinal relaxation rates, steady-state NOE, and longitudinal and transverse
sponding to any desired magnetic field between 0.01 and 14.1 T, at which       cross-correlated cross-relaxation rates acquired with 13C, 15N labeled sam-
relaxation rates are to be measured. The pulse sequence for the measure-       ple at 600 MHz (40); and longitudinal relaxation rates and steady-state
ment of high-resolution relaxometry rates (Fig. S1) is derived from the pre-   NOE measured with the identical 13C, 15N labeled sample at 850 MHz.
viously published pulse sequence for the determination of relaxation rates     Transverse auto-relaxation rates were not used in this analysis due to
at 0.33 T using a two-field NMR spectrometer (34–37). 15N longitudinal         possible contributions of chemical exchange (4), resulting in one single
relaxation rates R1 were measured at nine magnetic fields: 0.10, 0.33,         high-resolution relaxation rate that reports on J(0). Errors of the relaxation
0.67, 1.00, 1.46, 2.00, 2.50, 4.00, and 6.00 T. Three-dimensional HNCO         rates were estimated to be at least 2% of the relaxation rate.

                                                                                   Biophysical Journal 121, 3785–3794, October 18, 2022 3787
Salvi et al.

   The measured relaxometry relaxation rates and high-field relaxation rates         dimensional experiments using the HNCO correlation; the
were analyzed using the IMPACT approach (5). The relaxometry relaxation              benefit of a better resolution is documented in Fig. S2).
rates were corrected via the ICARUS protocol (25,48) to consider the ef-
fects of cross-relaxation during the sample shuttle transfers, stabilization
                                                                                        The ICARUS-IMPACT analysis of the experimental data
delays, and relaxation delays during the measurements. A 1 ms time step              results in a description of the spectral density function in the
was used in the ICARUS correction simulation. The accurate low-field                 form of J(u) ¼ 0.4 Si Bi Ti/(1 þ (u Ti)2) with i ¼ 1–7. The
(0.33 T) relaxation rates measured in a two-field NMR spectrometer (37)              seven Ti values span the range between 11 ps and 70 ns and
were not used in the analysis, so they could serve as an independent verifi-         are equidistant on a logarithmic scale (correlation times
cation of the ICARUS correction procedure.
   The applied IMPACT method follows the originally outlined methodol-
                                                                                     approximately 0.01, 0.05, 0.2, 0.9, 4, 16, and 70 ns). Exper-
ogy (5), but the analysis protocol was extended, and a grid search for the           imental data and back-calculated values are in excellent
optimal ratio (ranging between 200 and 10,000 with steps of 200) between             agreement (Fig. S3–S5). The correction factors applied to
the smallest and the largest correlation time (ranging between 10 and 120 ns         consider the cross-relaxation pathways during the relaxom-
with steps of 10 ns) was included. The analysis was performed using in-              etry experiment range from 3.0% to 11.5% depending on the
house script written in Mathematica 10.1.0 (49). The error of the optimized
parameters of the selected variant of J(u) was estimated based on 4,000
                                                                                     experimental setup (the corrected relaxometry relaxation
Monte Carlo simulations. The IMPACT analysis was also performed for                  rates are in Tables S5–S7). These values are consistent
individual residues separately using high-field data and the corrected relax-        with those previously reported for ubiquitin (25). To further
ometry relaxation rates obtained after the last iteration of the ICARUS-             verify the accuracy of the correction factors derived from
IMPACT analysis.                                                                     the ICARUS procedure, we compared the relaxometry
   MF analysis was carried out as previously described (12). Briefly, exper-
imental relaxation rates were modeled using a spectral density function of
                                                                                     relaxation rates measured at 0.33 T with longitudinal relax-
the form J(u) ¼ 0.4 Si Ai ti/(1 þ (u ti)2), in which i ¼ 1–3, the sum of the         ation rates measured at the same field (37) with a two-field
three amplitudes Ai is constrained to 1, and t1 is fixed to 45 ps. Three Lor-        NMR spectrometer (34,35), in which the effect of cross-
entzian terms have been used because this number provided the best fit for           relaxation pathways can be removed by means of 13C and
all residues in previous studies of disordered proteins (7,12). Thus, the            proton inversion pulses during the relaxation delay (36).
model effectively contains only four parameters to be determined (two am-
plitudes and two timescales). Monte Carlo simulations were used to quan-
                                                                                     While uncorrected high-resolution relaxometry rates are
tify the error bars on fitted parameters. Chemical shielding tensor of amide         systematically lower than the values acquired suppressing
   N was defined following published analysis (50) with the angle between            cross-relaxation pathways (Fig. 1 a), the correction factors
the main tensor component and 15N-1H bond set to 21 (4).                            derived from the ICARUS protocol effectively restore a
                                                                                     quantitative agreement with the data measured at a two-field
MD simulations                                                                       NMR spectrometer (Fig. 1 b). Therefore, these correction
                                                                                     factors are used throughout this work.
MD simulations were performed with the software Gromacs 5.0 (51) using the              The result of IMPACT analysis provides insight into the
force-field Amber99SB_ILDN (52). The simulations were run with explicit
                                                                                     distribution of timescales of motions. Of the seven fixed
solvent water molecules TIP4P-D (6). The choice of the setup reflected previ-
ous analysis of the effect of the force-field and water molecule models (53).        timescales, only four appear to contribute significantly to
Thirteen MD trajectories were calculated with various initial conformations          the spectral density function. The fastest motions on the or-
of the C-terminal domain. The starting structures are representative of the          der of several tens of ps B1 and B2 have a cumulated ampli-
structural flexibility of the C-terminal domain, and they covered both extended      tude of about 0.3, with little if any sequence dependence
conformations of the C-terminal domain and a more compact state that fea-
                                                                                     (Fig. 2 a shows the joint amplitudes B1þB2; separated plots
tures transient electrostatic interactions between the IDR and the folded N-ter-
minal domain. The charge of the system was neutralized using sodium and              for B1 and B2 can be found in Fig. S6). B4 amplitudes, asso-
chloride ions, and additional Naþ and Cl ions were added to match the exper-        ciated with a timescale close to 1 ns (Fig. 2 c), are the largest
imental NaCl concentration (10 mM). The appropriate protonation of side              contribution to relaxation for most residues and appear to
chains in the MD simulations was checked experimentally by pH titration in           monotonically increase from the end of the N-terminal
the range 8 to 5.4 and analysis of the chemical shifts of side-chain carbons (54).
                                                                                     folded domain to the C-terminus, indicating a gradual
   Each trajectory was divided into 22 nonoverlapping segments of variable
length (100–120 ns). For each segment, the rotational correlation function           reduction of the effect of the folded domain on the dynamics
of each NH bond vector was calculated and fitted to a predefined grid of             of the IDR, despite the presence of long-range contacts of
timescales as previously described (8).                                              electrostatic nature (55). Finally, the fifth component associ-
                                                                                     ated with a timescale of the order of several ns (Fig. 2 d) is
                                                                                     an important driver of relaxation for the residues close to the
RESULTS AND DISCUSSION
                                                                                     folded domain and those including and surrounding the
Remarkably, in spite of very limited signal dispersion (32)                          lysine-rich stretch (K-tract, K96–K104), which is involved
and technical challenges associated with the high-resolution                         in charge-mediated interactions (55).
relaxometry setup, resolution and sensitivity of the high-res-                          Of the remaining three timescales, values of B3 ¼ 0.1 are
olution relaxometry experiments were sufficient to probe                             found for all residues outside the K-tract (Fig. 2 b), indi-
dynamics of 68 out of 90 nonproline residues in the disor-                           cating that relatively fast dynamics might be quenched by
dered region of the delta subunit (in order to achieve spectra                       long-range interactions in the K-tract. Similarly, nonzero
with well-resolved peaks suitable for a quantitative analysis,                       values of B6 are found in the proximity of the folded
we performed relaxation measurements as pseudo-four-                                 domain (Fig. 2 e), probably to compensate for the fact that

3788 Biophysical Journal 121, 3785–3794, October 18, 2022
                                                                                                          IDPs dynamics by NMR and MD

          a                                                                deviate from the monotonous dependence of the amplitudes
                                                                           on the correlation times of the Zimm model for polyelectro-
                                                                           lytes (59). It documents a strong effect of electrostatic con-
                                                                           tacts on the conformation of the C-terminal domain of the
                                                                           delta subunit studied previously by small angle X-ray scat-
                                                                           tering and paramagnetic relaxation enhancement (32,55).
                                                                              In order to characterize the extent of slow ns dynamics and
                                                                           quantify their potential contributions to NMR relaxation from
                                                                           a theoretical standpoint, we performed a pool of MD simula-
                                                                           tions as described in the materials and methods section and
                                                                           calculated relaxation rates averaged across the pool (Fig. S8
                                                                           and S9). While the simulation is in good agreement with
                                                                           experimental relaxometry data, longitudinal relaxation rates
                                                                           measured at HF are systematically overestimated by the simu-
                                                                           lation, whereas the only rate that depends on J(0) in our data-
          b
                                                                           set—the CSA/dipole-dipole cross-correlated cross-relaxation
                                                                           rates hxy measured at 600 MHz—is significantly higher in the
                                                                           experiment than in the simulation. Taken together, these two
                                                                           observations indicate that protein dynamics are excessively
                                                                           fast in the simulation compared with in the experiment. We
                                                                           attribute this quantitative disagreement between experiment
                                                                           and simulation to our choice of water model (TIP4P-D),
                                                                           which has been shown to promote excessive flexibility in
                                                                           both folded and unfolded proteins (10).
                                                                              We applied the average block selection using relaxation
                                                                           data (ABSURD) method to select, among the segments of
                                                                           trajectories in our pool, a subset of trajectories minimizing
                                                                           the root-mean-square deviation between experimental and
                                                                           simulated data (8). This approach accounts for conforma-
FIGURE 1 Correlation of the relaxation rates measured at 0.33 T            tional variability across conformers interconverting on time-
(experimental uncertainties are indicated by error bars). Correlation of   scales faster than the coalescence limit while filtering for
the longitudinal relaxation rates R12FNMR measured with two-field NMR      poor sampling of slower motional modes responsible for un-
spectrometer and the relaxometry decay rates R1relaxometry (a) and their
corrected values R1corrected (b).
                                                                           stable averaging of the autocorrelation function. All rates
                                                                           measured at 500, 600, and 850 MHz except heteronuclear
                                                                           NOEs were combined in the ABSURD target function for
T5 ¼ 3.81 ns is smaller than the actual rotational correlation             selection. Somewhat disappointingly, we obtain a suben-
time of the folded N-terminal domain tc ¼ 5 ns based on hy-                semble of four out of a total of 44 segments. In addition,
drodynamical calculations (56,57) (estimated for N-termi-                  simulated relaxation rates evaluated from this subensemble
nal domain of the d subunit alone; the comparison of the                   (Figs. S10 and S11) are very close to those averaged over the
relaxation data acquired for the separated N-terminal                      entire pool, indicating that protein dynamics are accelerated
domain (58) and the full length d subunit (4) shows a negli-               in the entire pool of trajectories to a similar degree,
gible effect of the C-terminal domain on the rotational diffu-             rendering the ABSURD selection process very inefficient.
sion of the N-terminal domain). This effect is similar to the              Although the experimental sequence dependence of relaxa-
one observed in the IMPACT analysis of HF relaxation data                  tion rates presented in Figs. S8–S11 is qualitatively repro-
measured on the partially disordered Engrailed2 (5). Finally,              duced by the ABSURD ensemble of trajectories, there are
the parameter B7 (Fig. 2 f), associated with a correlation                 systematic differences that appear to report on systematic
time on the orders of several tens of ns features very small               errors in the depiction of both ns motions (only one high-
values throughout the sequence. While these values are                     field longitudinal rate is correctly reproduced, the 500 and
significantly different from zero for residues 110 to 135,                 600 MHz R1 values are clearly not) and, most severely,
which might suggest a tail of the distribution of correlation              the unique probe of slower motions (hxy). Under these con-
times with a nonzero density for correlation times t > T6 ¼                ditions, it would be hazardous to over-interpret the fact that
16.3 ns, they never represent more than 1% of the angular                  relaxometry data are, apparently serendipitously, actually
correlation function/spectral density function. Similar con-               quite well reproduced by the simulation.
clusions can be obtained from the analysis done on a per-                     In an attempt to shed further light on the shortcomings of
residue basis (the results are shown in Fig. S7). The results              the simulation, we compare the dynamic fingerprint of the

                                                                              Biophysical Journal 121, 3785–3794, October 18, 2022 3789
Salvi et al.

 a                                                                              b

 c                                                                              d

 e                                                                              f

FIGURE 2 Fitted coefficients Bi (with error bars) used to model the distribution of the timescales. The coefficients are related to the terms of the spectral
density function associated with correlation times 11 and 48 ps taken together (a), 0.2 ns (b), 0.9 ns (c), 3.8 ns (d), 16.3 ns (e), and 70 ns (f).

protein derived from the IMPACT analysis (Fig. 2) with an                           the simulation to be accurate, that the derived timescale of
analog fingerprint extracted from the simulation.                                   50 ps often found in IDPs irrespective of their sequence
    To do so, for each NH bond vector, we average the rota-                         and length (12,13) is in fact a value representative of a dis-
tional correlation functions calculated for each segment and                        tribution of fast dynamics. In the IDR, we find two addi-
fit the averaged autocorrelation function to a predefined grid                      tional motional processes, one around 1 ns and a slower
of 128 timescales as previously described (8). The results of                       one, around 4 ns, that identify with the fourth and fifth
the fit are shown in Fig. 3. Besides a minor component at                           component of the IMPACT analysis, respectively. We note
5 ns, most ns dynamics in the folded domain (residues                              that both these processes appear to occur on timescales
1–90) occur at 3 ns, which is shorter than the expected                            that are close to, but well distinct from, the reorientation
rotational correlation time of the protein, highlighting yet                        of the folded domain. This indicates that slow dynamics in
again that our choice of water model does not reproduce                             IDRs is of segmental nature and decoupled from the rota-
protein hydrodynamics with sufficient accuracy. In both                             tional diffusion of the folded domain beyond the persistence
the folded domain and IDR, the two fastest motional pro-                            length of several residues, implying that the use of ‘‘order
cesses occur around 10 and 100 ps, suggesting, assuming                             parameters’’ is not the most informative for understanding

3790 Biophysical Journal 121, 3785–3794, October 18, 2022
                                                                                                                   IDPs dynamics by NMR and MD

                                                                                                     FIGURE 3 Motional timescales derived from fits
                                                                                                     of average autocorrelation functions to a predefined
                                                                                                     grid of 128 timescales, from 1 ps to 50 ns. The size
                                                                                                     of each dot is proportional to the amplitude of the
                                                                                                     associated timescale.

the dynamic richness of long IDRs. We suggest that a dy-                      ps) displays many features identified above. t2 is close to
namic description in terms of multiple timescales and their                   900–1,000 ps for the entire sequence, with the exception
associated amplitudes is a more natural framework to under-                   of the region broadly centered around the K-tract. This
stand the functional mechanisms of disordered proteins.                       observation is consistent with our interpretation of the third
   We note that, despite a lack of quantitative agreement                     and fourth components of the IMPACT analysis. t3, which
with the high-field data due to excessively fast multi-ns mo-                 appears to be poorly defined because of the scarcity of in-
tions, the simulation, particularly with the use of ABSURD,                   formation on J(0) in our dataset, does not show any evident
reproduces relaxometry rates well. This demonstrates that                     sequence dependence, suggesting again that slow motions
relaxometry data can be described with a model that does                      are segmental chain-like dynamics largely independent of
not include >10 ns motions, as an alternative to the use of                   the rotation of the N-terminal domain. We find that the
the correlation times T6 and T7 of the IMPACT analysis.                       product of A3 and t3 is much more robustly determined
   MF analysis of HF data and high-resolution relaxometry                     in our analysis, in line with decades of applications of
measurements simultaneously reproduces relaxation rates                       MF analysis to folded proteins. Consistently with B1-B2
measured at low (Fig. S12) and high (Fig. S13) fields                         features in IMPACT, the amplitude of fast motions
with good accuracy. The sequence dependence of fitted pa-                     (Fig. 4 f) increases only slightly going from the N- to the
rameters (Fig. 4, we remind the reader that t1 is fixed to 45                 C-terminus. The amplitudes of intermediate (Fig. 4 e)

 a                                                  b                                                  c

 d                                                  e                                                  f

FIGURE 4 Motional timescales (a and b) and amplitudes (d–f) resulting from the model-free analysis of either the entire dataset comprising both high-
resolution relaxometry and HF spin relaxation data (blue) or HF measurements only (orange). The product of A3 and t3 is better defined than the two in-
dividual parameters (c). Shaded areas represent uncertainties on fitted parameters, estimated by Monte Carlo simulations.

                                                                                  Biophysical Journal 121, 3785–3794, October 18, 2022 3791
Salvi et al.

and slow (Fig. 4 d) motions match B4 and B5 in the                  ysis of the full set of high- and low-field relaxation rates.
IMPACT analysis, respectively. Overall, the results are             We note, however, that it is again difficult to make any
consistent with what was expected for an IDR of similar             meaningful comparison because of the limited size of the
length in the absence of significant partially formed sec-          high-field data set (only 6 rates are available for the determi-
ondary structure elements.                                          nation of 4 independent parameters).
   Recent studies of the dynamics of IDPs have exploited               The region spanning residues 105–140 was shown (55) to
full sets of R1, R2, 1H-15N NOE and cross- correlated               electrostatically interact with the K-tract and with the struc-
CSA-dipole cross-relaxation hxy at three or more magnetic           tured part of the d subunit. The electrostatic interactions
fields. The relative sparsity of experimental data available at     with the K-tract are essential for the role of the d subunit
high field in this study precludes a systematic comparison of       in regulation of RNA polymerase activity by a stabilization
the information content present in high- and low-field relax-       of initiation complexes of RNA polymerase-DNA interac-
ometry data. We have nevertheless repeated the MF analysis          tion (55). The accurate description of the dynamics in this
using only the spin relaxation data measured at 500, 600,           region is therefore of a particular interest. If confirmed by
and 850 MHz. Rates back calculated from the results of              further investigations, motions with an effective timescale
this MF analysis closely match the experimental values              of 10 ns or more, such as the contribution for T7 in the
(Fig. S14). Interestingly, cross-validation of the MF results       ICARUS-IMPACT analysis, could be related to the forma-
using the relaxometry data, which are not actively used in          tion of a temporarily compacted conformation of the part
the fit, reveals that the overall trend of longitudinal relaxa-     of the C-terminal domain involving the positively charged
tion at low field can be predicted with good accuracy from          K-tract and the part of the acidic regions. Yet, the contribu-
the information about dynamics encoded in the high-field            tion of such motions is very small in the ICARUS-IMPACT
data in most cases (Fig. S15). Such overall agreement               analysis and therefore not reflected by MF analysis and not
is expected since high-field relaxation probes the spectral         captured by MD simulations.
density function, a monotonous, decreasing function of the
frequency, down to 50 MHz and at zero frequency. In addi-
                                                                    CONCLUSIONS
tion, the precision of low-field relaxation rates is much
lower than that of high-field rates due to the limited sensi-       We presented a detailed comparison of complementary
tivity of the shuttle and probe apparatus (about 20% of the         NMR- and computational-based approaches to probe and
sensitivity of a room-temperature probe or 7% of the               describe ps-ns dynamics in disordered systems using a
600 MHz spectrometer used for high-field relaxation                 well-characterized model system. Overall, our results indi-
measurements).                                                      cate that three timescales and their associated amplitudes
   The spectral density at zero frequency J(0) obtained from        are in general sufficient to model most observations
high-field measurements probes the slowest motions in a             in vitro and in silico. While this has been shown already
way where amplitude and correlation times are convoluted.           in a number of IDPs, here we add an example of a disordered
The magnetic-field dependence of low-field relaxation rates         region in a partially folded protein, and we show that the
should therefore provide novel information concerning               presence of the folded domain does not increase the
small, but statistically significant, differences between           complexity of the dynamic features, which can be captured
experimental relaxometry relaxation rates and those pre-            by the tools and models developed specifically for IDPs.
dicted by the analysis of high-field relaxation alone. The             Our study combines 15N relaxation measured at atomic
presence of additional information contained in relaxometry         resolution of an IDP over an unprecedented range of mag-
relaxation rates is suggested by a direct comparison of             netic field strengths and therefore a broader spectrum of
the MF parameters obtained by an analysis of high-field             timescales of reorientational modes than has been available
relaxation alone and with the addition of relaxometry data          until now. We observe that the model assuming three major
(Fig. 4), which have different profiles in the region between       contributions to the spectral density function can predict the
105 and 137 (results are listed in Tables S8 and S9, respec-        relaxometry data measured down to 4.26 MHz with good
tively). Both analyses provide similar estimates of the prod-       accuracy in most cases, confirming the overall robustness
uct of A3 and t3, which is just slightly lower in the analysis      of this commonly used framework. The potential for
of the full dataset (Fig. 4 c). Not surprisingly, this product is   refining more complex motional models by including relax-
defined with more precision because of the information              ometry data into such an analysis is, however, self-evident.
about the spectral density values close to 0, due to the higher     Although our study suffers from suboptimal sampling of
number of relaxometry data at the lowest fields reporting on        high-field data and force-field inaccuracies, which have
slower motions. However, overall A3 parameters are lower            been amply discussed in the literature, our analysis never-
and t3 higher in this region when the relaxometry data are          theless provide tantalizing indications of the potential
included (Fig. 4 a and d), which could be numerically               of combining high-field relaxation and high-resolution
similar to the appearance of very small contribution of the         relaxometry to enhance sampling of the spectral density
longest correlation time T7 in the ICARUS-IMPACT anal-              function at frequencies not accessible to HF relaxation

3792 Biophysical Journal 121, 3785–3794, October 18, 2022
                                                                                                                      IDPs dynamics by NMR and MD

measurements, in particular with respect to the details of                       7. Gill, M. L., R. A. Byrd, and A. G. Palmer, III. 2016. Dynamics of
                                                                                    GCN4 facilitate DNA interaction: a model-free analysis of an intrinsi-
slower, possibly functionally important, motions in the                             cally disordered region. Phys. Chem. Chem. Phys. 18:5839–5849.
d subunit of RNA polymerase. We expect that further
                                                                                 8. Salvi, N., A. Abyzov, and M. Blackledge. 2016. Multi-timescale dy-
studies applying high-resolution relaxometry with enhanced                          namics in intrinsically disordered proteins from NMR relaxation and
sensitivity or other techniques will help to further refine mo-                     molecular simulation. J. Phys. Chem. Lett. 7:2483–2489.
tions in this important family of proteins beyond the model                      9. Salvi, N., A. Abyzov, and M. Blackledge. 2017. Analytical description
with three ps-ns effective processes.                                               of NMR relaxation highlights correlated dynamics in intrinsically
                                                                                    disordered proteins. Angew. Chem., Int. Ed. Engl. 56:14020–14024.
                                                                                10. Robustelli, P., S. Piana, and D. E. Shaw. 2018. Developing a molecular
SUPPORTING MATERIAL                                                                 dynamics force field for both folded and disordered protein states.
                                                                                    Proc. Natl. Acad. Sci. USA. 115:E4758–E4766.
Supporting material can be found online at https://doi.org/10.1016/j.bpj.       11. Thomasen, F. E., F. Pesce, ., K. Lindorff-Larsen. 2022. Improving
2022.09.016.                                                                        martini 3 for disordered and multidomain proteins. J. Chem. Theor.
                                                                                    Comput. 18:2033–2041.
                                                                                12. Abyzov, A., N. Salvi, ., M. Blackledge. 2016. Identification of dy-
AUTHOR CONTRIBUTIONS                                                                namic modes in an intrinsically disordered protein using tempera-
                                                                                    ture-dependent NMR relaxation. J. Am. Chem. Soc. 138:6240–6251.
N.S., V.Z., M.B., and P.K. analyzed data; Z.J. and S.N. prepared NMR sam-
ples; V.Z., M.Z., J.-M.T., T.M., L.Z., F.F., and P.K performed NMR exper-       13. Adamski, W., N. Salvi, ., M. Blackledge. 2019. A unified description
iments; V.Z., Z.J., P.P., and P.K. processed and analyzed NMR spectra; N.S.,        of intrinsically disordered protein dynamics under physiological condi-
                                                                                    tions using NMR spectroscopy. J. Am. Chem. Soc. 141:17817–17829.
L.Z., M.B., F.F., and P.K. wrote the manuscript; F.F., M.B., and P.K. ob-
tained funding for the project.                                                 14. Clore, G. M., A. Szabo, ., A. M. Gronenborn. 1990. Deviations from
                                                                                    the simple two-parameter model-free approach to the interpretation of
                                                                                    nitrogen-15 nuclear magnetic relaxation of proteins. J. Am. Chem. Soc.
                                                                                    112:4989–4991.
ACKNOWLEDGMENTS                                                                 15. Buevich, A. V., and J. Baum. 1999. Dynamics of unfolded proteins:
                                                                                    incorporation of distributions of correlation times in the model free
This work was supported by Czech Science Foundation grant no. GJ18-
                                                                                    analysis of NMR relaxation data. J. Am. Chem. Soc. 121:8671–8672.
04197Y (to P.K., V.Z., and Z.J.), from European Regional Development
Fund-Project MSCAfellow2@MUNI, No. CZ.02.2.69/0.0/0.0/18_070/                   16. Hsu, A., F. Ferrage, and A. G. Palmer. 2018. Analysis of NMR spin-
0009846 (to P.P. and P.K.), and grant no. ANR-18-CE29-0003 (NANO-                   relaxation data using an inverse Gaussian distribution function.
DISPRO), provided by Agence Nationale de la Recherche (to F.F. and                  Biophys. J. 115:2301–2309.
M.B.). Short scientific mission of P.K. to perform measurements at the          17. Bloembergen, N., E. M. Purcell, and R. V. Pound. 1948. Relaxation ef-
NMR spectrometer allowing high-resolution relaxometry experiments                   fects in nuclear magnetic resonance absorption. Phys. Rev. 73:679–712.
was supported by a STSM grant from the EURELAX COST Action                      18. Wangsness, R. K., and F. Bloch. 1953. The dynamical theory of nuclear
CA15209. CIISB, Instruct-CZ Centre of Instruct-ERIC EU consortium,                  induction. Phys. Rev. 89:728–739.
funded by MEYS CR infrastructure project LM2018127, is gratefully
                                                                                19. Solomon, I. 1955. Relaxation processes in a system of two spins. Phys.
acknowledged for the financial support of the measurements at the Josef             Rev. 99:559–565.
Dadok National NMR Centre.
                                                                                20. Redfield, A. G. 1957. On the theory of relaxation processes. IBM J.
                                                                                    Res. Dev. 1:19–31.
                                                                                21. Abragam, A. 1961. The Principles of Nuclear Magnetism. Clarendon
DECLARATION OF INTERESTS                                                            Press.
T.M. and J.-M.T. were employees of the Bruker BioSpin. The other authors        22. Smith, A. A., M. Ernst, and B. H. Meier. 2017. Because the light is bet-
declare no other conflict of interest.                                              ter here: correlation-time analysis by NMR spectroscopy. Angew.
                                                                                    Chem., Int. Ed. Engl. 56:13590–13595.
                                                                                23. Parigi, G., N. Rezaei-Ghaleh, ., C. Luchinat. 2014. Long-range corre-
REFERENCES                                                                          lated dynamics in intrinsically disordered proteins. J. Am. Chem. Soc.
                                                                                    136:16201–16209.
 1. Henzler-Wildman, K., and D. Kern. 2007. Dynamic personalities of            24. Clarkson, M. W., M. Lei, ., D. Kern. 2009. Mesodynamics in the
    proteins. Nature. 450:964–972.                                                  SARS nucleocapsid measured by NMR field cycling. J. Biomol.
 2. Dyson, H. J., and P. E. Wright. 2005. Intrinsically unstructured proteins       NMR. 45:217–225.
    and their functions. Nat. Rev. Mol. Cell Biol. 6:197–208.                   25. Charlier, C., S. N. Khan, ., F. Ferrage. 2013. Nanosecond time scale
 3. Jensen, M. R., M. Zweckstetter, ., M. Blackledge. 2014. Exploring               motions in proteins revealed by high-resolution NMR relaxometry.
    free-energy landscapes of intrinsically disordered proteins at atomic           J. Am. Chem. Soc. 135:18665–18672.
    resolution using NMR spectroscopy. Chem. Rev. 114:6632–6660.                26. Cousin, S. F., P. Kaderávek, ., F. Ferrage. 2018. Time-resolved pro-
 4. Kaderávek, P., V. Zapletal, ., L. 
                                        Zı́dek. 2014. Spectral density map-         tein side-chain motions unraveled by high-resolution relaxometry and
    ping protocols for analysis of molecular motions in disordered proteins.        molecular dynamics simulations. J. Am. Chem. Soc. 140:13456–13465.
    J. Biomol. NMR. 58:193–207.                                                 27. Smith, A. A., N. Bolik-Coulon, ., F. Ferrage. 2021. How wide is the
 5. Khan, S. N., C. Charlier, ., F. Ferrage. 2015. Distribution of pico- and        window opened by high-resolution relaxometry on the internal dy-
    nanosecond motions in disordered proteins from nuclear spin relaxa-             namics of proteins in solution? J. Biomol. NMR. 75:119–131.
    tion. Biophys. J. 109:988–999.                                              28. Prompers, J. J., and R. Br€uschweiler. 2002. General framework for
 6. Piana, S., A. G. Donchev, ., D. E. Shaw. 2015. Water dispersion in-             studying the dynamics of folded and nonfolded proteins by NMR relax-
    teractions strongly influence simulated structural properties of disor-         ation spectroscopy and MD simulation. J. Am. Chem. Soc. 124:4522–
    dered protein states. J. Phys. Chem. B. 119:5113–5123.                          4534.

                                                                                    Biophysical Journal 121, 3785–3794, October 18, 2022 3793
Salvi et al.

29. Salvi, N., A. Abyzov, and M. Blackledge. 2019. Solvent-dependent            44. Lee, W., M. Tonelli, and J. L. Markley. 2015. NMRFAM-SPARKY:
    segmental dynamics in intrinsically disordered proteins. Sci. Adv.              enhanced software for biomolecular NMR spectroscopy. Bioinformat-
    5:eaax2348.                                                                     ics. 31:1325–1327.
30. Seepersaud, R., R. H. V. Needham, ., A. L. Jones. 2006. Abundance           45. Eaton, J. W., D. Bateman, and S. Hauberg. 2009. GNU Octave Version
    of the d subunit of RNA polymerase is linked to the virulence of Strep-         3.0.1 Manual: A High-Level Interactive Language for Numerical Com-
    tococcus agalactiae. J. Bacteriol. 188:2096–2105.                               putations. CreateSpace Independent Publishing Platform.
31. Rabatinová, A., H. Sanderová, ., L. Krásný. 2013. The d subunit of     46. Tibshirani, R. 1988. Variance stabilization and the Bootstrap. Bio-
    RNA polymerase is required for rapid changes in gene expression                 metrika. 75:433–444.
    and competitive fitness of the cell. J. Bacteriol. 195:2603–2611.           47. Hall, P. 1988. Theoretical comparison of Bootstrap confidence inter-
                                                                                    vals. Ann. Stat. 16:927–953.
32. Papousková, V., P. Kaderávek, ., L. 
                                            Zı́dek. 2013. Structural study of
    the partially disordered full-length d subunit of RNA polymerase            48. Bolik-Coulon, N., P. Kaderávek, ., S. F. Cousin. 2020. Theoretical
    from Bacillus subtilis. Chembiochem. 14:1772–1779.                              and computational framework for the analysis of the relaxation proper-
                                                                                    ties of arbitrary spin systems. Application to high-resolution relaxom-
33. López de Saro, F. J., A. Y. Woody, and J. D. Helmann. 1995. Structural         etry. J. Magn. Reson. 313:106718.
    analysis of the Bacillus subtilis delta factor: a protein polyanion which
    displaces RNA from RNA polymerase. J. Mol. Biol. 252:189–202.               49. Wolfram Research, Inc. 2015. Mathematica. 10.1. Champaign Illinois.
                                                                                50. Loth, K., P. Pelupessy, and G. Bodenhausen. 2005. Chemical shift
34. Cousin, S. F., P. Kaderávek, ., F. Ferrage. 2016. Recovering invisible
                                                                                    anisotropy tensors of carbonyl, nitrogen, and amide proton nuclei in
    signals by two-field NMR spectroscopy. Angew. Chem., Int. Ed. Engl.
                                                                                    proteins through cross-correlated relaxation in NMR spectroscopy.
    55:9886–9889.
                                                                                    J. Am. Chem. Soc. 127:6062–6068.
35. Cousin, S. F., C. Charlier, ., F. Ferrage. 2016. High-resolution two-       51. Abraham, M. J., T. Murtola, ., E. Lindahl. 2015. GROMACS: high
    field nuclear magnetic resonance spectroscopy. Phys. Chem. Chem.                performance molecular simulations through multi-level parallelism
    Phys. 18:33187–33194.                                                           from laptops to supercomputers. SoftwareX. 1–2:19–25.
36. Kaderávek, P., N. Bolik-Coulon, ., F. Ferrage. 2019. Protein dy-          52. Lindorff-Larsen, K., S. Piana, ., D. E. Shaw. 2010. Improved side-
    namics from accurate low-field site-specific longitudinal and transverse        chain torsion potentials for the Amber ff99SB protein force field. Pro-
    nuclear spin relaxation. J. Phys. Chem. Lett. 10:5917–5922.                     teins. 78:1950–1958.
        náková, Z., V. Zapletal, ., P. Kaderávek. 2020. Boosting the
37. Jase                                                                       53. Zapletal, V., A. Mládek, ., J. Hritz. 2020. Choice of force field for pro-
    resolution of low-field $$^{15}\hbox {N}$$ relaxation experiments               teins containing structured and intrinsically disordered regions.
    on intrinsically disordered proteins with triple-resonance NMR.                 Biophys. J. 118:1621–1633.
    J. Biomol. NMR. 74:139–145.                                                 54. Tollinger, M., J. D. Forman-Kay, and L. E. Kay. 2002. Measurement of
38. Kazimierczuk, K., A. Zawadzka, and W. Kozminski. 2008. Optimiza-              side-chain carboxyl pK(a) values of glutamate and aspartate residues in
    tion of random time domain sampling in multidimensional NMR.                    an unfolded protein by multinuclear NMR spectroscopy. J. Am. Chem.
    J. Magn. Reson. 192:123–130.                                                    Soc. 124:5714–5717.
39. Lopez, J., P. Ahuja, ., G. Lippens. 2014. H/D exchange of a 15N             55. Kubán, V., P. Srb, ., L.  Zı́dek. 2019. Quantitative conformational
    labelled Tau fragment as measured by a simple Relax-EXSY experi-                analysis of functionally important electrostatic interactions in the
    ment. J. Magn. Reson. 249:32–37.                                                intrinsically disordered region of delta subunit of bacterial RNA poly-
                                                                                    merase. J. Am. Chem. Soc. 141:16817–16828.
40. Srb, P., J. Novácek, ., L. 
                                 Zı́dek. 2017. Triple resonance 15N NMR
                                                                                56. Garcı́a de la Torre, J., M. L. Huertas, and B. Carrasco. 2000.
    relaxation experiments for studies of intrinsically disordered proteins.
                                                                                    HYDRONMR: prediction of NMR relaxation of globular proteins
    J. Biomol. NMR. 69:133–146.
                                                                                    from atomic-level structures and hydrodynamic calculations.
41. Ferrage, F., D. Cowburn, and R. Ghose. 2009. Accurate sampling of               J. Magn. Reson. 147:138–146.
    high-frequency motions in proteins by steady-state 15N{1H} nuclear         57. Garcı́a De La Torre, J., M. L. Huertas, and B. Carrasco. 2000. Calcu-
    overhauser effect measurements in the presence of cross-correlated              lation of hydrodynamic properties of globular proteins from their
    relaxation. J. Am. Chem. Soc. 131:6048–6049.                                    atomic-level structure. Biophys. J. 78:719–730.
42. Delaglio, F., S. Grzesiek, ., A. Bax. 1995. NMRPipe: a multidimen-          58. Kaderávek, P., C. Diehl, ., M. Akke. 2011. Complementation of 3D
    sional spectral processing system based on UNIX pipes. J. Biomol.               structure of delta subunit of RNA polymerase from Bacillus subtilis
    NMR. 6:277–293.                                                                 with description of internal motions in terms of reduced spectral den-
43. Ying, J., F. Delaglio, ., A. Bax. 2017. Sparse multidimensional itera-          sity mapping. Mater. Struct. 18:3–5.
    tive lineshape-enhanced (SMILE) reconstruction of both non-uni-             59. Zimm, B. H. 1956. Dynamics of polymer molecules in dilute solution:
    formly sampled and conventional NMR data. J. Biomol. NMR.                       viscoelasticity, flow birefringence and dielectric loss. J. Chem. Phys.
    68:101–118.                                                                     24:269–278.

3794 Biophysical Journal 121, 3785–3794, October 18, 2022
