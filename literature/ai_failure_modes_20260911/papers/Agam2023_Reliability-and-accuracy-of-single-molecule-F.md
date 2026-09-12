# Reliability and accuracy of single-molecule FRET studies for characterization of structural dynamics and distances in proteins

**Authors:** Ganesh Agam, Christian Gebhardt, Milana Popara, et al.
**Year:** 2023
**Venue:** Nature Methods
**DOI:** 10.1038/s41592-023-01807-0
**Source PDF URL:** https://www.nature.com/articles/s41592-023-01807-0.pdf
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

nature methods

Analysis                                                                                           https://doi.org/10.1038/s41592-023-01807-0


Reliability and accuracy of single-molecule
FRET studies for characterization of
structural dynamics and distances in
proteins

Received: 2 August 2022                            A list of authors and their affiliations appears at the end of the paper

Accepted: 31 January 2023
                                                  Single-molecule Förster-resonance energy transfer (smFRET) experiments
Published online: 27 March 2023
                                                  allow the study of biomolecular structure and dynamics in vitro and in vivo.
   Check for updates                              We performed an international blind study involving 19 laboratories to
                                                  assess the uncertainty of FRET experiments for proteins with respect to
                                                  the measured FRET efficiency histograms, determination of distances,
                                                  and the detection and quantification of structural dynamics. Using two
                                                  protein systems with distinct conformational changes and dynamics, we
                                                  obtained an uncertainty of the FRET efficiency ≤0.06, corresponding to
                                                  an interdye distance precision of ≤2 Å and accuracy of ≤5 Å. We further
                                                  discuss the limits for detecting fluctuations in this distance range and how
                                                  to identify dye perturbations. Our work demonstrates the ability of smFRET
                                                  experiments to simultaneously measure distances and avoid the averaging
                                                  of conformational dynamics for realistic protein systems, highlighting its
                                                  importance in the expanding toolbox of integrative structural biology.


Förster-resonance energy transfer (FRET) studies have become a widely       (dsDNA) that demonstrated a high reproducibility between the dif-
used approach to complement classical structural biology techniques1–4.     ferent laboratories with an uncertainty of ≤6 Å for the FRET-derived
They provide information on the structure and conformational het-           distances18. These results strongly supported the idea that standard-
erogeneity of biomolecules over a distance range of 30 to 120 Å and,        ized smFRET measurements in combination with standardized data
when performed on single molecules, contribute additional informa-          analysis routines are a useful addition to the integrative modeling
tion regarding conformational dynamics on the timescales of nano-           of static biomolecular structures12,19,20.
seconds to seconds1,2,5–10. They also allow for quantitative assessment           Here, we assessed whether the established procedures translate
of structural dynamics and heterogeneity of conformational ensem-           to more flexible biomacromolecules such as proteins that undergo
bles. This information is not easily accessible by X-ray crystallography,   conformational changes. Compared to dsDNA, proteins are more
cryogenic-electron microscopy or cross-linking mass-spectrometry,           challenging systems, because the local environments and flexibility
which provide structural information of solution structures but lack        of the tethered dyes can vary considerably. Site-specific dye labeling
temporal information. FRET can also be used to resolve (parts of) struc-    of proteins usually requires the introduction of point mutations (for
tures in an integrative manner (refs. 11–17) and has the unique ability     example, cysteines or nonnatural amino acids), which can affect its
to provide correlated information on structure and dynamics1,2.             structure and function1. Moreover, proteins require careful handling
     Hellenkamp et al. presented a quantitative multilaboratory             and storage due to sample instability and aggregation, and are sensi-
smFRET blind study assessing the validity of using smFRET for struc-        tive to experimental conditions, buffer composition, pH, temperature,
tural measurements. This study used static double-stranded DNA              surface interactions and so on. In a blind comparison study involving


  e-mail: a.barth@tudelft.nl; cseidel@hhu.de; d.lamb@lmu.de; cordes@bio.lmu.de


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                             523


Analysis                                                                                            https://doi.org/10.1038/s41592-023-01807-0

19 laboratories using diffusion-based confocal smFRET, we investi-         of ALEX or PIE (Supplementary Note 1) was crucial for corrections of
gated the maltose-binding protein (MalE) and the U2 Auxiliary Factor       the photon counts to reflect the actual D and A signal and exclusion
2 (U2AF2), which display conformational dynamics on different time         of single-molecule events from incompletely labeled molecules or ones
and length scales. We addressed two key questions: (1) how consist-        showing photo- blinking and bleaching8,9,18,34,35.
ently can smFRET efficiency histograms (and the derived distances)
be determined by different laboratories for protein samples prepared       MalE
with stochastic fluorophore labeling? (2) How reliably can smFRET          We prepared three double-cysteine variants of MalE with interresidue
measurements detect structural dynamics in these proteins and what         distances that cover a large part of the dynamic range of FRET (Fig. 1b,
are the minimal structural fluctuations detectible?                        Methods and Supplementary Fig. 4). The variants were designed to show
     Our study confirmed the reproducibility of accurate FRET effi-        a decrease (MalE-1, K29C-S352C), an increase (MalE-2, D87C-A186C)
ciency histograms and the ability of smFRET to detect and quantify         or an unaltered interdye distance (MalE-3, A134C-A186C) upon malt-
conformational dynamics on the submillisecond timescale. We dem-           ose binding. All variants of MalE were stochastically labeled in one
onstrate reproducible FRET efficiency values with uncertainties ≤0.06      of the laboratories at the given positions with the donor Alexa Fluor
corresponding to a distance precision of ≤2 Å and an accuracy ≤5 Å         546 (Alexa546) and acceptor Alexa Fluor 647 (Alexa647). Before ship-
in MalE. Moreover, we compare the variability of setup-dependent           ment, we confirmed the functionality of the labeled protein by ligand
parameters and identified the main sources of calibration uncer-           titrations using smFRET and microscale thermophoresis, and verified
tainty. To push the detection limits for structural dynamics, we refined   that maltose did not affect the dye properties (Supplementary Figs.
established experimental and data analysis procedures and stud-            5 and 6). To allow a comparison, participants were asked to provide
ied distinct dye pairs to identify and eliminate dye-specific effects.     mean FRET efficiencies using Gaussian fits for apo and holo FRET
With this, we could detect distance fluctuations on the order of 5 Å       efficiency histograms (Fig. 1c) and to determine a global γ value for
in the FRET-sensitive range. Our work demonstrates that smFRET is          all measurement conditions (Supplementary Note 2 and Supplemen-
able to characterize challenging and realistic protein systems with        tary Fig. 3). For this workflow, participants used custom or publicly
conformational dynamics on timescales from nanoseconds to                  available software packages.
seconds, highlighting its importance in the expanding toolbox of                  FRET efficiency histograms for representative experiments on
integrative structural biology19–21.                                       MalE in the apo (no ligand) and the holo state (1 mM maltose) are shown
                                                                           in Fig. 1c with mean values reported by 16 laboratories. They show very
Results                                                                    good agreement and reproducibility. It was not possible to extract
We chose two protein systems with conformational dynamics on dif-          accurate FRET efficiency values from three laboratories due to, for
ferent timescales. Our first target was the MalE protein of Escherichia    example, missing or suboptimal laser lines (Supplementary Table 1
coli, the periplasmic component of the ATP binding cassette transporter    and Supplementary Note 2). All laboratories observed the expected
MalFGK2-E (refs. 22–24). MalE exhibits a typical periplasmic-binding       changes for MalE-1, MalE-2 and no shift for MalE-3. This indicates that
protein fold25,26 composed of two rigid domains connected by a flex-       the samples did not degrade during shipment on dry ice and storage
ible two-segment ß-stranded hinge (Fig. 1a). This structure enables an     in the laboratories at 4 °C. MalE-1 showed an average FRET efficiency
allosterically driven motion from an open to closed state upon maltose     of 0.49 ± 0.06 in the apo state that increased to 0.67 ± 0.05 in the
binding on the subsecond timescale (Supplementary Fig. 1). As a second     holo state. MalE-2 showed the expected decrease in FRET efficiency
system, we chose the large subunit of U2AF2 from the pre-messenger         from 0.83 ± 0.03 to 0.71 ± 0.05 in the apo and holo states, respectively
RNA (mRNA) splicing machinery27. Its two RNA recognition motif             (Fig. 1c). MalE-3, with both labels on one lobe, showed no significant
domains (RRM1,2) are connected by a long flexible linker and bind          change in FRET efficiency (Eapo = 0.91 ± 0.02, Eholo = 0.92 ± 0.02).
single-stranded Py-tract RNA28. For U2AF2, the two domains fluctu-                The standard deviation of the determined mean FRET efficiency
ate between an ensemble of detached conformations and a compact            over all laboratories was less than ±0.06, similar to the precision found
conformation in the apo state29, whereas ligand binding stabilizes an      for dsDNA previously18 (Extended Data Table 1 and Supplementary
open conformation (Fig. 2a)30.                                             Table 3). We observe the highest standard deviation for MalE-1 and the
      SmFRET experiments were blindly performed by 19 laboratories         lowest values of ±0.02 for MalE-3, which also has the highest FRET
for MalE and by seven laboratories for U2AF2 using different imple-        efficiency. We observed systematic deviations of the reported FRET
mentations of diffusion-based confocal spectroscopy with alternating       efficiency values for the apo and holo states from the mean value.
excitation, that is, microsecond-ALEX (alternating laser excitation        Hence, we analyze the individual FRET efficiency differences,
mode)31 for intensity-based analysis and nsALEX32 or pulsed-interleaved    ⟨Eholo ⟩ − ⟨Eapo ⟩, between the apo and holo states for the different labo-
excitation (PIE)33 for intensity- and lifetime-based analyses (Supple-     ratories (Fig. 1d). The distributions indeed narrow for all samples by
mentary Fig. 2). To avoid additional complexity and to restrict any        approximately twofold because systematic deviations cancel out
preknowledge regarding the samples, the proteins were labeled and          ( σ⟨Eholo ⟩−⟨Eapo ⟩ for MalE-1 ±0.02, MalE-2 ±0.02 and MalE-3 ±0.01: Fig. 1d,
checked for functionality before being delivered to the participants.      Extended Data Table 1 and Supplementary Table 3).
Information regarding the identity of the proteins and ligands, labeling
positions, labeling efficiency, and expected FRET efficiencies and         U2AF2
changes were not provided. The laboratories were informed about            For the second protein, U2AF2, we chose the published double-cysteine
which fluorophores were coupled. We adapted a data analysis rou-           variant L187C-G326C of the minimal RRM1,2 construct, where we
tine similar to ref. 18 to determine setup-independent accurate FRET       previously verified that protein function is not affected by labeling
efficiency E values from the photon counts detected in the donor (D)       (Fig. 2a)36,37. The construct was labeled stochastically on the two RRM
and acceptor (A) detection channels during a single-molecule event.        domains with the dye pair Atto532–Atto643. A subset of seven groups
The procedure is described in the Methods and includes subtraction         measured the sample. To investigate the consistency of the obtained
of background signals from all channels and the determination of           FRET efficiency histograms, we plotted the smFRET histograms
four correction factors: (α) for spectral crosstalk of D fluorescence      from individual laboratories (Fig. 2b,c, row 1) as well as the average
into the A channel, (β) for normalization of direct D and A excitation     distribution illustrated by the mean and standard deviation (row 2).
fluxes, (γ) for differences in D and A quantum yields and detection        All groups found a single broad distribution (Fig. 2b, row 1, apo) with
efficiencies and (δ) for the ratio of indirect and direct A excitation     an average E = 0.74 ± 0.03 (row 2). In the presence of 5 µM ligand (U9
(Supplementary Fig. 3 and Supplementary Tables 1 and 2)34. The use         RNA, Kd of roughly 1.3 µM), a second narrower peak at lower E appears


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                  524


Analysis                                                                                                                                                                                 https://doi.org/10.1038/s41592-023-01807-0


                         a                                                          b                                            Apo                     Maltose                                                  Holo
                                                                                                    90°                 K29C


                                                                            D1

                                                                                              D87C

                                                                                                                                                    +


                                                                            D2

                                                                                               A186C                                               S352C
                                                                                                                    A134C

                         c
                                   Events
                                                    1 K29C-S352C                                                1 D87C-A186C                                                    1 A134C-A186C
                                                        (MalE-1)                                                    (MalE-2)                                                        (MalE-3)
                         Apo

                                (normalized)        0                                                           0                                                               0


                                     Laboratories


                                   Events
                                                    1                                                           1                                                               1

                         Holo

                                (normalized)        0                                                           0                                                               0


                                     Laboratories


                                                        0      0.2      0.4       0.6         0.8         1.0       0          0.2      0.4       0.6         0.8         1.0       0      0.2          0.4       0.6         0.8         1.0

                                                                   FRET efficiency, E                                            FRET efficiency, E                                            FRET efficiency, E
                         d


                                     Laboratories


                                                            –0.2     –0.1     0         0.1         0.2                 –0.2     –0.1         0         0.1         0.2                 –0.2     –0.1         0         0.1         0.2

                                                                      Eholo – Eapo                                               Eholo – Eapo                                             Eholo – Eapo

Fig. 1 | Experimental design of MalE as a protein model system for smFRET                                                             absence and presence of 1 mM maltose (bottom, green) for one exemplary
studies. a, Crystal structure of MalE in its ligand-free apo state (PDB ID 1OMP)                                                      dataset measured in laboratory 1. The distribution is fitted to a Gaussian
with domains D1 and D2 linked by flexible beta sheets (highlighted in blue). b, The                                                   distribution. The reported mean FRET efficiencies for 16 laboratories are shown
crystal structure of MalE (rotated by 90° as compared to a in the apo (gray, PDB ID                                                   below (due to experimental difficulties, the results of three laboratories were
1OMP) and holo (green, PDB ID 1ANF) states with mutations at K29C-S352C                                                               excluded; Supplementary Table 1). The mean FRET efficiency and the standard
(MalE-1), D87C-A186C (MalE-2) and A134C-A186C (MalE-3) indicated in black.                                                            deviation of all 16 laboratories are given by the black line and gray area.
Note, each mutant only contains one cysteine pair and was measured using the                                                          d, Individual FRET efficiency differences for each laboratory, between the apo
Alexa546–Alexa647 FRET pair. The estimated mean position of the fluorophores                                                          and holo states, ⟨Eholo ⟩ − ⟨Eapo ⟩, for MalE-1 (left), MalE-2 (middle) and MalE-3
from AV calculations are shown as red spheres. c, FRET efficiency E histograms                                                        (right). The mean FRET efficiency difference and the standard deviation of all
for three MalE mutants, MalE-1 (left), MalE-2 (middle) and MalE-3 (right), in the                                                     16 laboratories are given by the black line and gray area.


(Fig. 2c, row 1) with an average E = 0.46 ± 0.04 (row 2) as expected for the                                                          agreement to a standard deviation of ±0.008 with no change in mean
open conformation of the holo state30,36. Notably, a fraction of                                                                      E (Fig. 2d,e and Supplementary Table 4). The reanalysis revealed the
around 15% of ligand-free protein remains in the sample at the RNA                                                                    detection correction factor γ to be the main cause of the deviations
concentration used (Supplementary Fig. 7).                                                                                            between the measurements. As a single population of the apo state
      For the apo state, we obtained a similar standard deviation                                                                     did not allow for a robust determination of the γ factor34,35, it was best
of ±0.03 as found for MalE, however, a clear outlier was apparent                                                                     to estimate the γ factor from a global analysis of the apo and holo
(Supplementary Table 4). To test whether user bias affected the                                                                       measurements. This was possible since the quantum yield of the fluo-
reported results, a single person reanalyzed the datasets. This person                                                                rophores remained unchanged upon RNA binding (Supplementary
developed an optimal procedure for determining the correction factors                                                                 Table 5). We also reanalyzed data from the same seven laboratories
for this challenging sample (Supplementary Note 3) and improved the                                                                   for MalE-1 apo and obtained nearly identical mean FRET efficiencies


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                                                                                                               525


Analysis                                                                                                                                             https://doi.org/10.1038/s41592-023-01807-0


                      a                                           b                                                                              c
                                                                                                              Apo


                                                                     Frequency
                       Apo                                                                                                                                   Holo
                                                                                                0.05                                             0.05


                                                                                                      0                                              0


                                                                (average) (individual)
                                                                                                0.05                                             0.05


                                                                                                      0                                              0
                                                                                                          0     0.2     0.4   0.6    0.8   1.0           0      0.2     0.4   0.6    0.8   1.0

                                                                                                                    FRET efficiency, E                              FRET efficiency, E
                                             L187C
                                                                  d                                                                              e
                                                                                                      1                                              1
                                                                                                              Apo                                            Holo

                                                                            Events
                              G326C                                                                   0                                              0


                                                                          Laboratories Laboratories
                                         +
                       RNA


                                                                          (reanalyzed) (submitted)
                       Holo

                                                                                                          0     0.2     0.4   0.6   0.8    1.0           0      0.2     0.4   0.6   0.8    1.0

                                                                                                                    FRET efficiency, E                              FRET efficiency, E

Fig. 2 | The experimental system of U2AF2 (RRM1, 2) and a comparison of                                                The middle shows the reported mean FRET efficiencies reported by seven
FRET efficiency histograms from seven different laboratories. a, Schematic                                             laboratories. The mean value from all datasets is 0.739 ± 0.029, shown above with
of the dynamics of U2AF2. The apo state (in gray, top) undergoes fast exchange                                         the corresponding standard deviation in gray. The bottom shows the extracted
between an ensemble of detached structures of which five representative                                                mean FRET values after reanalysis of the collected data. After reanalysis,
structures are displayed. A slower exchange occurs between the dynamic                                                 the agreement improved to 0.742 ± 0.008. e, SmFRET efficiency histogram
detached ensemble and a compact conformation (PDB ID 2YHO) shown below.                                                comparisons of U2AF2 in the holo state. 5 µM of U9 RNA was used to obtain
The holo state (in green, PDB ID 2YH1) bound to a U9 RNA ligand (in dark gray)                                         the holo state. The top shows a representative 1D FRET efficiency histogram
assumes a well-defined, open conformation. Positions of cysteine mutations                                             of laboratory 1 fitted to two Gaussian distributions to determine the FRET
introduced for labeling (L187 in RRM1 and G326 in RRM2) are depicted as black                                          efficiencies of the different subpopulations, yielding mean FRET efficiencies of
spheres with the mean dye position determined by AV calculations indicated                                             0.44 for RNA-bound and 0.76 for the RNA-free conformation. The middle shows
by red spheres. b,c, SmFRET efficiency histograms reported by the seven                                                the mean FRET efficiencies reported by the seven laboratories. The mean values
participating laboratories for apo (b) and holo (c) measurements of U2AF2. The                                         from all seven of the datasets were 0.45 ± 0.04 for the RNA-bound conformation
top shows the individual FRET efficiency histograms and the bottom shows the                                           (in green) and 0.78 ± 0.04 for the RNA-free conformation (in gray). The bottom
average FRET efficiency histogram (solid line) with standard deviation (light                                          shows the reanalysis of the holo measurements yielding values of 0.42 ± 0.02 and
area). d, SmFRET efficiency E histograms of U2AF2 in the apo state. The top shows                                      0.77 ± 0.03 for RNA-bound and RNA-free fractions, respectively.
a representative 1D FRET efficiency histogram with a Gaussian fit (laboratory 1).


and standard deviations (0.49 ± 0.05 versus 0.47 ± 0.06, Supple-                                                       Fig. 9). On average, participants collected 6,000 bursts (minimum
mentary Fig. 8). This indicates that user bias was less pronounced                                                     500, maximum 21,000) of molecules carrying both fluorophores. The
when a global, well-defined analysis procedure for determining γ                                                       required number of bursts for a smFRET analysis depends on the goal
was provided over several samples covering a substantial fraction                                                      of the experiment. To determine the average FRET efficiency from
of the FRET range (Supplementary Note 2).                                                                              a single population, as performed for MalE, roughly 1,000 bursts of
     For the holo state of U2AF2, good agreement between laboratories                                                  double-labeled molecules may be sufficient. For advanced analysis
was obtained for the peak positions with a standard deviation of ±0.03                                                 methods such as time-correlated single photon counting (TCSPC) for
and ±0.02 for the high- and low-FRET peaks, respectively. A minimal                                                    lifetime analysis, burst-wise fluorescence correlation spectroscopy
improvement resulted from the reanalysis (Supplementary Table 4). In                                                   (FCS) or a photon distribution analysis (PDA) that are applied to sub-
contrast to the agreement in FRET efficiency, we observed variations in                                                ensembles, higher burst numbers of >5,000 are desired. Typical count
the relative amplitudes of the two populations: 0.58 ± 0.08 for the holo                                               rates per single-molecule event were found to be 60 ± 20 kHz, with an
state and 0.42 ± 0.08 for the apo population (Fig. 2c and Supplementary                                                average burst of 90 ± 40 photons and 1.7 ± 0.9 ms duration (Fig. 3a
Table 4). We attribute this to potentially reduced protein activity, degra­                                            and Supplementary Fig. 9). The average count rate and burst dura-
dation of the RNA ligand and sensitivity of conformational dynamics                                                    tion depend on the size of the confocal volume, where smaller sizes
to the experimental conditions, for example, temperature, ligand con-                                                  result in higher count rates but shorter burst durations. We observe a
centration, buffer composition, salt concentration or the presence of                                                  negative correlation between burst duration and average count rate
stabilizers such as bovine serum albumin (BSA) (Supplementary Fig. 7).                                                 (Fig. 3b, Pearson’s r = −0.58 and Supplementary Fig. 10). The large
                                                                                                                       spread of the burst duration arises from the fact that some partici-
Setup-dependent parameters and correction factors                                                                      pants applied a diffraction-limited observation volume, while others
The quality of smFRET experiments is determined by the statistics                                                      underfilled the objective lens to create a larger confocal volume with
of the measurement and the performance of the setup to maximize                                                        a diameter of roughly 1 µm (assuming that the detection pinhole
photon collection and thereby minimize shot noise. To this end, we                                                     corresponds to the excitation volume). We also observed a small
quantified the number of bursts, average photon count rate, burst dura-                                                positive correlation between detected photon numbers and burst
tion and the number of photons in the D and A channels for the MalE                                                    duration (Fig. 3c, Pearson’s r = 0.54 and Supplementary Fig. 10). This
measurements from eight laboratories (Fig. 3a and Supplementary                                                        suggests that larger volumes, in combination with high irradiances,


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                                                                  526


Analysis                                                                                                                                                                                                 https://doi.org/10.1038/s41592-023-01807-0


                 a                                              Setup statistics                                                    d                                                   Correction factors

                  15,000                            120                       6                                 300                 0.10                                      3.0                     1.0              0.4

                 10,000                                80                     4                                 200
                                                                                                                                    0.05                                       1.5                    0.5              0.2
                      5,000                            40                     2                                 100

                                    0                   0                     0                                  0                       0                                      0                        0              0
                                  No. of bursts        Count rate (kHz)       Burst duration                           No. of                    α                                          β                   γ                δ
                                                                                   (ms)                               photons


                 b                                                                   c                                                               e
                                                                                                                                                                             0.12       Calibration
                                   150                                                                250                                                                               uncertainty
                                                                                                            Pearson’s r = 0.54


                                                                                                                                                 Estimated uncertainty, ∆E
                                         Peason’s r = –0.58


                                                                                  Number of photons
                                                                                                                                                                             0.10          ∆γ/γ = 50%


               Count rate (kHz)
                                                                                                                                                                                                                                       MalE-1 apo
                                                                                                                                                                             0.08                  40%                                 MalE-1 holo
                                                                                                                                                                                                                                       MalE-2 apo
                                                                                                      100                                                                                          30%
                                                                                                                                                                                                                                       MalE-2 holo
                                                                                                                                                                             0.06
                                    50                                                                                                                                                                                                 MalE-3 apo
                                                                                                       50                                                                                                                              MalE-3 holo
                                                                                                                                                                             0.04                  20%
                                         0    1    2        3      4      5                                 0     1      2      3    4       5                               0.02                  10%
                                             Burst duration (ms)                                                 Burst duration (ms)                                                               5%
                                                                                                                                                                                    0        0.2         0.4     0.6     0.8     1.0
                                                                                                                                                                                                   FRET efficiency, E

Fig. 3 | Setup-dependent parameters and calibration uncertainty. a, The                                                                      Error bands indicate the 95% confidence intervals of the regression. d, The
distribution of the parameters quantifying the statistics of the measurements                                                                distributions of the four correction factors for the calculation of accurate FRET
and the performance of the setups used for both MalE and U2AF2 measurements                                                                  efficiencies for all the MalE measurements are shown as histograms and violin
are shown as histograms and violin plots for the measurements from eight                                                                     plots for the measurements from all laboratories. The circle and whiskers in the
laboratories. The circle and whiskers in the violin plot indicate the mean and                                                               violin plot indicate the mean and standard deviation (n = 64, averaged over eight
standard deviation (n = 64, averaged over eight samples measured in the                                                                      samples measured in the eight different laboratories). e, A plot of the standard
eight different laboratories). Sample-dependent distributions of the shown                                                                   deviation of the reported FRET efficiencies from 16 laboratories (as a measure
parameters are given in Supplementary Fig. 9. b,c, Pairwise plots of the average                                                             of the experimental uncertainty) against the average FRET efficiency for the
count rate (b) and the number of photons (c) against the burst duration. The                                                                 MalE mutants 1–3 reveals that lower uncertainties are observed for higher FRET
same datasets are plotted as used for a. While the count rate decreases slightly                                                             efficiencies. The black line represents a fit of the estimated uncertainties under
for longer burst durations, a positive correlation is observed for the acquired                                                              the assumption that the variations arise solely due to uncertainty in the γ factor
number of photons per burst and the burst duration, indicating that larger                                                                   (equation (1)). The inferred relative uncertainty of the γ factor is around 23%.
observation volumes result in a higher accumulated signal per molecule.                                                                      Shaded areas indicate relative uncertainties of 5–50%. Error bars indicate 95%
Correlations between all parameters are shown in Supplementary Fig. 10.                                                                      confidence intervals around the average value.


yield the highest number of photons per burst38. Smaller volumes                                                                             acceptor-to-donor ratio of the detection efficiencies, g, and the effec-
generally allow for higher burst collection rates with higher count rates                                                                    tive fluorescence quantum yields, ϕF, as γ = gA ϕF,A /gD ϕF,D (ref. 18).
and thus shorter interphoton times, enabling fast transitions on the                                                                         Similar to crosstalk, γ strongly depends on the emission filters and
sub-µs timescale to be resolved39,40. Longer burst durations offer the                                                                       the type of detectors used. Due to ϕF,A of roughly 0.32 (acceptor) and
benefit that slower dynamics can be studied.                                                                                                 ϕF,D of roughly 0.72 (donor), all laboratories reported γ factors
      For an accurate analysis, the correction factors for donor spectral                                                                    below 1. Despite the large spread in the reported values, we observed
crosstalk (α), excitation flux (β), detection efficiency and quantum                                                                         very good agreement for the reported FRET efficiencies in our blind
yields (γ) and direct acceptor excitation (δ) must be determined (see                                                                        study. Our analysis identified γ as the key factor limiting the consist-
ref. 18, Supplementary Table 5). We plot the distribution of the cor-                                                                        ency, which is supported by the following arguments: (1) in Fig. 1d, the
rection factors used to determine accurate FRET efficiencies for MalE                                                                        spread of ⟨Eholo ⟩ − ⟨Eapo ⟩ is smaller (for example, 0.06 to 0.02 for
in Fig. 3d from 16 laboratories (Supplementary Table 1). Besides fluo-                                                                       MalE-1) than for absolute E values in Fig. 1c, suggesting that errors in
rophore properties, these also depend on setup-specific parameters                                                                           E are systematic rather than random. (2) The observed spread in
including dichroic mirrors, emission filters, detectors, excitation                                                                          reported FRET efficiencies depends on the absolute FRET efficiency
wavelengths and laser power. Nonetheless, we observed a well-defined                                                                         measured for MalE (Fig. 1c,d). (3) We also calculated the uncertainty in
distribution for α of 0.05 ± 0.01, which is determined by the emission                                                                       the FRET efficiency calculation using error propagation for crosstalk,
filters and detectors in both detection channels. A larger spread was                                                                        direct excitation and background correction in the donor and acceptor
observed for β values of 1.6 ± 0.6 and δ of 0.12 ± 0.08. These depend                                                                        channels. The reported uncertainty can be attributed mainly to the γ
on the ratio of the excitation powers, where most participants used                                                                          factor (Fig. 3e and Supplementary Note 4) with the error of the γ
about half the laser power for direct acceptor excitation (45 ± 27 µW)                                                                       factor, Δγ, that propagates into an uncertainty in the reported FRET
in comparison to the donor excitation (78 ± 58 µW), resulting in                                                                             efficiencies, ΔE:
similar count rates after donor and acceptor excitation. The agree-
                                                                                                                                                                                                                                 Δγ
ment between the reported FRET efficiency values clearly shows                                                                                                                                                 ΔE = E (1 − E )                       (1)
                                                                                                                                                                                                                                 γ
that the diverse experimental settings are compensated by the
correction procedure applied here.
      For γ, which is the most difficult factor to determine, we observed                                                                        Notably, the observed experimental ΔE is well described by
an average of 0.4 ± 0.1 (Supplementary Fig. 3b). It depends on the                                                                           equation (1) (black line in Fig. 3e), yielding a relative uncertainty of


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                                                                                                                    527


Analysis                                                                                                 https://doi.org/10.1038/s41592-023-01807-0

Δγ/γ = 23% corresponding to Δγ ≅ 0.07. The improved agreement                   laboratories 1 and 2) shown in gray in Fig. 4e,f (Supplementary Table 8).
between measurements on reanalysis for U2AF2 (Fig. 2d) suggests                 The ds did not exceed that of the static reference when using BVA for
that the accuracy of the analysis could be improved by standardized             all MalE mutants. From the E–τ plots, however, ds was higher than
procedures for the determination of all correction factors, which               for dsDNA, especially for MalE-1. This sample clearly exceeds what is
differ depending on the number of populations in the measure-                   predicted for a static system or even what is predicted for dynamics
ment and whether the FRET efficiency peak is dynamically averaged               between the apo and holo states (Fig. 4f, red lines and Supplemen-
(Supplementary Note 2).                                                         tary Note 6). Hence, some laboratories categorized MalE as dynamic.
                                                                                The cause of this ds, which must originate from FRET dynamics that
Detection and quantification of conformational dynamics                         are faster than around 100 µs, will be discussed in detail below.
Fluorescence trajectories of immobilized molecules provide access                    In contrast to MalE, all groups found U2AF2 to be dynamic as was
to kinetics on the millisecond to second timescales via a dwell-time            expected for two domains connected by a flexible linker (Fig. 4c–f
analysis (Supplementary Fig. 1)41–43. For freely diffusing molecules,           and Supplementary Table 6). The ligand-free apo state shows pro-
millisecond dynamics can be studied in the same fashion when mol-               nounced deviations from the behavior for static molecules both in
ecules diffuse slowly44,45. The detection and quantification of submil-         the BVA and E–τ plots, while the RNA-bound holo state shows a
lisecond conformational dynamics in quickly diffusing molecules (with           notable ds for BVA but not for the E–τ analysis (Fig. 4c–f). It was chal-
the maximum timescale limited by the burst duration) is possible via            lenging to assess whether the holo state is truly static or dynamic since
FRET–FCS44,46,47, filtered-FCS48,49, burst-variance analysis (BVA)50, FRET–     it contained a measurable fraction of apo protein, which overlaps
two-channel kernel-based density distribution estimator51, dynamic              with the holo population. Hence, U2AF2 is a challenging test case, yet,
PDA52, FRET efficiency E versus fluorescence-weighted average donor             dynamics were unambiguously detected in all laboratories demon-
lifetime ⟨τD(A) ⟩F analysis (E–τ plots)52,53, nanosecond-FCS54, recurrence      strating the reliability of smFRET for investigating dynamic systems.
analysis of single particles55, photon-by-photon maximum likelihood
approaches40,56–59 and Monte Carlo diffusion-enhanced photon                    Accuracy of FRET-derived distances and structural modeling
inference (MC-DEPI)60. To assess how consistently dynamics can be               Accurate FRET efficiencies need to be converted into distances for
detected in smFRET measurements, we asked the participants to                   comparison with structures or to use them as distance constraints in
evaluate whether the proteins were static or dynamic on the (sub-)              integrative FRET-assisted structural modeling1,5,7,15,63,64. SmFRET experi­
millisecond timescale and which method they used to come to this                ments yield FRET efficiencies as a result of dynamically, nonlinearly
conclusion (Supplementary Table 6).                                             averaged distances due to the flexible fluorophore linkers. To assess
      BVA and E–τ plots are frequently used techniques to visualize FRET        the accuracy of our measurements, we applied the accessible volumes
dynamics by comparing the measured data to theoretical expectations.            (AV) approach5,6,64,65, which uses a coarse-grained dye model to estimate
BVA detects dynamics by estimating the standard deviation of the FRET           the FRET efficiency averaged model distance Rmodel      ⟨E⟩
                                                                                                                                               between the
efficiency over individual bursts, using a predefined photon window             two dyes. For this, all possible positions of the fluorophores are aver-
(typically ≳100 µs depending on the molecular brightness). Due to               aged, taking into account linker conformations and steric hindrances
FRET dynamics, the standard deviation of the FRET signal within a burst         (Fig. 5a–c, Methods and ref. 6). For AV calculations, we assume fast
(red line in Fig. 4a) can be higher than expected from shot noise (black        rotational and slow positional averaging with respect to the fluores-
semicircle in Fig. 4a), which becomes visible as a deviation or apparent        cence lifetime. Prediction of measured distances via FRET values based
dynamic shift, ds50. In the E–τ plots, the observed FRET efficiency             on the flexibility and attachment points of a fluorophore is an area
determined via intensity (Fig. 4b) is a species-weighted average and,           of active research and alternative methods are being developed, for
in the presence of dynamics, the position along the y axis depends on           example, rotamer libraries66 or molecular dynamics simulations67,68.
the fraction of time spent in the respective states. The fluorescence                The average experimental FRET efficiencies from the individual
lifetime of the donor (Fig. 4b, ⟨τD(A) ⟩F, x axis) is a photon-weighted         smFRET histograms ⟨E⟩ for MalE (Fig. 2) were used to determine R⟨E⟩
average, because only a single lifetime is determined. Hence, it is             for each laboratory (Extended Data Table 1 and Supplementary
weighted toward the lifetime of low-FRET states as they emit more               Table 3) using the Förster equation (equation (2)):
donor photons52,53, shifting the data to the right of the ‘static’ FRET line.                                                         1
E–τ plots can detect dynamics on the nanosecond to millisecond time-                                                     1            6
                                                                                                                                                       (2)
                                                                                                           R⟨E⟩ = R0 (         − 1)
scale. Here, we have included an additional correction that considers                                                    ⟨E⟩
distance fluctuations of the flexible dye linkers (6 Å) resulting in a
slightly curved ‘static’ FRET line52,61. To quantify dynamics between two             The Förster radius of Alexa546–Alexa647 on MalE was determined
distinct states, a theoretical ‘dynamic’ FRET line (red, Fig. 4b) is over-      to be R0 = 65 ± 3 Å (Supplementary Note 7). Figure 5d displays the
laid. Again, ds is defined as the deviation of the observed data from the       correlation between the experimental observable R⟨E⟩ and predicted
theoretical static line (Fig. 4b and Supplementary Note 6). It is impor-        Rmodel
                                                                                  ⟨E⟩   using apo and holo structures exhibiting an uncertainty
tant to mention that FRET dynamics, and the related ds, are not always          of 3–5 Å over all variants. In agreement with the predictions by
of conformational origin.                                                       Peulen et al.69, this accuracy is achieved despite stochastic protein
      MalE exhibits slow ligand-driven dynamics on the subsecond                labeling, which could result in different charge environments and
timescale between high- and low-FRET states (Supplementary Fig. 1)62.           AVs of the fluorophores depending on the labeling positions. This is
Here, we investigated whether the apo and/or holo states undergo                evident by the varying dye behavior at different locations (Fig. 5b).
dynamics faster than the timescale of diffusion. Both techniques reveal         During the study, three laboratories studied additional MalE variants
that MalE exhibits no large FRET-fluctuations on the ms timescale               (MalE-4, K34C-N205C and MalE-5, T36C-N205C) with a larger FRET
(Fig. 4c,d and Supplementary Fig. 11). Almost all groups confirmed              efficiency contrast between the apo and holo states, complementing
this assessment and only three groups concluded that MalE is                    the results of the other variants (Extended Data Table 1).
dynamic without further justification (Supplementary Table 6). To                     Figure 5d reveals the largest deviation between experimental
investigate the presence of potential dynamics in more detail, we               and predicted distances for MalE-1, which also had the highest ds
determined the ds for a subset of the data (eight laboratories for              values (Fig. 4f and Supplementary Fig. 11). Therefore, we investigated
BVA, Fig. 4e and five for E–τ, Fig. 4f, Supplementary Note 5, and               the role of dye–protein interactions using single-cysteine variants of
Supplementary Table 7). As a static control, we determined the ds               MalE by measuring the fluorescence lifetimes, and time-resolved and
of the dsDNA rulers used in ref. 18 (mean ± 1 s.d. as determined from           steady-state anisotropies (Supplementary Note 8, Supplementary


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                     528


Analysis                                                                                                                                                                                                           https://doi.org/10.1038/s41592-023-01807-0


   a                                                                     c                                                                                                                             e

                                                                     Counts
                               Burst variance analysis                                           500                                           500                                                                                                                Apo
                                         BVA                                                                                                                                                                                                    BVA               Holo
                     0.4                                                                         0.4                                           0.4
                                                                                                           MalE-2 apo                                    U2AF2 apo                                                    0.10   n=8
                                                                                                                                                                                                                                                               Predicted
                     0.3                                                                         0.3                                           0.3
                                                    ds


                                                                                                                                                                                                        Apparent ds
                                                                                                                                                                                                                      0.03

σEapp                0.2                                                   σE*                   0.2                                           0.2                                                                    0.02

                                                                                                                                                                                                                      0.01
                     0.1                                                                         0.1                                           0.1
                                                                                                                                                                                                                                                                dsDNA
                      0                                                                           0                                              0
                           0     0.2     0.4       0.6   0.8   1.0                                     0     0.2   0.4       0.6   0.8   1.0         0     0.2     0.4       0.6   0.8   1.0
                                                                                                                                                                                                                              MalE-1   MalE-2         MalE-3    U2AF2
                                           Eapp                                                                      Eapp                                            Eapp

   b                                                                     d                                                                                                                             f
                           FRET efficiency - lifetime


                                                                     FRET efficiency, E Counts
                                                                                                 500                                           500
                                           E–τ                                                                                                                                                                                                  E-τ
                     1.0                                                                         1.0
                                                                                                                                                                                                                             n=5
                                                                                                                                                                                                                      0.15


FRET efficiency, E
                     0.8                                                                         0.8


                                                                                                                                                                                                     Apparent ds
                     0.6                           ds                                            0.6                                                                                                                  0.10

                     0.4                                                                         0.4
                                                                                                                                                                                                                      0.05
                     0.2                                                                         0.2
                                                                                                           MalE-2 apo                                    U2AF2 apo                                                      0
                      0                                                                           0
                           0       1           2         3     4                                       0       1         2         3      4          0       1           2         3      4
                                                                                                                                               500                                             500                            MalE-1   MalE-2         MalE-3    U2AF2
                                       τD(A)F (ns)                                                               τD(A)F (ns)                                 τD(A)F (ns)
                                                                                                                                         Counts                                           Counts

Fig. 4 | Detection and characterization of conformational dynamics on the                                                                                            U2AF2 were determined from a subensemble analysis of the fluorescence decay.
submillisecond timescale in MalE and U2AF2. a,b, Schematic representations                                                                                           e,f, The apparent ds of the peak of the population was determined graphically
of BVA (a) and E–τ (b) plots. The ds is defined as the excess standard deviation                                                                                     from BVA (eight laboratories for MalE and seven laboratories for U2AF2,
compared to the static line (shown in black). Dynamic FRET lines are indicated in                                                                                    respectively) (e) and E–τ (five laboratories) (f) plots (Methods). For U2AF2 in the
red. c, BVA of MalE-2 labeled with Alexa546–Alexa647 without maltose (apo, left)                                                                                     holo state, the ds was assessed only for the low-FRET RNA-bound population.
and U2AF2 labeled with Atto532–Atto643 without RNA (apo, right). Here, the BVA                                                                                       Boxes indicate the median and 25/75% quartiles of the data. Whiskers extend to
is based on a photon binning of five photons. Red diamonds indicate the average                                                                                      the lowest or highest data point within 1.5 times the interquartile range. The gray
standard deviation of all bursts within a FRET efficiency range of 0.05. The mean                                                                                    area indicates the ds obtained for the dsDNA used in a previous study18 based on
positions of the populations (cyan crosses) were determined by fitting a                                                                                             measurements performed in laboratory 1 for BVA (dsDNA = 0.0033 ± 0.0033) and
two-dimensional Gaussian distribution to the data (Supplementary Note 5).                                                                                            laboratory 2 for the E–τ plot (dsDNA = 0.0026 ± 0.0044). The horizontal red lines
d, The plots of the FRET efficiency E versus intensity-weighted average donor                                                                                        indicate the expected ds for a potential conformational exchange between the
lifetime ⟨τD(A) ⟩F of the same measurement as in c. The donor-only population was                                                                                    apo and holo states. We computed the expected change in FRET efficiency using
excluded from the plot. For MalE-2, the population falls on the static FRET line,                                                                                    their structural models in the PDB (Supplementary Note 6 and Supplementary
while a clear ds is observed for U2AF2. The endpoints of the dynamic FRET line for                                                                                   Table 9).


Tables 5, 11 and 12 and Fig. 5b). Labeling at residue 352 promotes dye                                                                                               The dye pair Alexa546–Alexa647 showed the highest combined aniso-
sticking to the protein surface indicated by multiexponential fluores-                                                                                               tropies (Supplementary Fig. 12a and Supplementary Table 13), which
cence lifetimes and a high residual anisotropy, r∞, for both fluorophores                                                                                            is attributed to the donor Alexa546 as the combined anisotropy
(r∞ > 0.25). Labeling at residue 29 only shows sticking for the donor                                                                                                also remains high for Alexa546–AbbSTAR635P but is reduced for
(r∞,D > 0.30, r∞,A roughly 0.12). At other positions (for example, residue                                                                                           Alexa488–Alexa647. To derive a robust and well-defined threshold for
186), free rotation is possible for both dyes (Supplementary Tables 5                                                                                                recognizing measurements with dye artifacts, we determined the
and 11). These position-specific interactions can cause the observed                                                                                                 uncertainty in the FRET-derived distances, ΔRapp(κ2), that originates
deviations between the experiment and structural model (Fig. 5d and                                                                                                  from the uncertainty of the orientation factor κ2. Previous approaches
Extended Data Table 1) and high ds values for MalE-1 (Fig. 4f). By using                                                                                             estimated the uncertainty in κ2 from the residual anisotropy in terms
the accessible contact volume (ACV) approach63, which accounts for                                                                                                   of rotational restrictions (wobbling-in-a-cone model)70–73. Here, we
dye–protein interactions, the root-mean-average deviation between                                                                                                    used a ‘diffusion with traps’ model, which assumes two dye populations
the structural model and experimental values decreased from 3 Å for                                                                                                  (free and trapped) and relates the residual anisotropies to the fraction
AV to 2 Å (Fig. 5c). For protein labeling on opposite sides, dye–protein                                                                                             of dyes interacting with the surface of the biomolecule (Supplementary
interactions in the ACV model result in reduced model distances and                                                                                                  Note 9). Based on the estimated distance uncertainty, we propose a
improved accuracy for all outliers (Fig. 5d and Extended Data Table 1).                                                                                              threshold of ΔRapp(κ2) < 10% to identify measurements with dye-related
      It was suggested to use the combined residual anisotropy of D                                                                                                  artifacts (Fig. 5e, bottom). This threshold corresponds to a combined
and A ( rc,∞ = √r∞,D r∞,A ) for filtering out dye-related artifacts in                                                                                               residual anisotropy of 0.25, similar to the previously suggested
FRET-assisted structural modeling with an empirical threshold of                                                                                                     empirical threshold value of around 0.2 (refs. 13,70).
rc,∞ < 0.2 (refs. 13,70). To further investigate dye-specific sticking, three                                                                                             Next, we investigated whether dye sticking could cause the ds in
laboratories studied MalE mutants with the additional dye pairs                                                                                                      the E–τ plot for MalE-1 with Alexa546–Alexa647 (Fig. 4f). To be observ-
Alexa546–AbbSTAR635P, Atto532–Atto643 and Alexa Fluor 488                                                                                                            able in the E–τ plot, the exchange between the free and trapped dye
(Alexa488)–Alexa647 and determined the residual anisotropies and                                                                                                     species must occur faster than the diffusion time of roughly 1 ms,
distance uncertainties based on the orientation factor κ2 (Fig. 5e, top,                                                                                             otherwise the two species would be observable as individual peaks. We
Supplementary Tables 13 and 14 and Supplementary Notes 8 and 9).                                                                                                     observed a correlation between the laboratory-averaged 〈ds〉 and 〈rc,∞〉


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                                                                                                                                    529


Analysis                                                                                                                                                                                         https://doi.org/10.1038/s41592-023-01807-0


 a                                              b                                                                                                                      d
                                R2   R3                                                             Alexa546-S352C apo                    Alexa647-S352C apo
                         R1                                                 0.4                     Alexa546-K29C apo                     Alexa647-K29C apo                                                                   AV
                                                                                                                                                                                                                              ACV


                                              Anisotropy, r(t)


                                                                            0.2


                                                                                                                                                                      RE experiment (Å)
                                      LLink                                                                                                                                                 60


                        WLink                                                     0
                                                                                      0             5         10           15 0           5        10          15
                                Alexa546-
                                                                                                                         Time, t (ns)
                                maleimide

 c
                        K29C
                                                                                                                                              Donor
                                                                                                     S352C
                                                                                                                                                         AV
                                                                                                                                                         ACV

                                                                                                                                              Acceptor
                                                                                                                                                                                                                   40                  50               60             70
                                                                                                                                                         AV
                                                                                                                                                         ACV                                                                               RE model (Å)

                                                                                                                                                                    Apo
                                                                                                                                                                    Holo
                                                                                                                                                                                        MalE-1            MalE-2                    MalE-3     MalE-4        MalE-5    U2AF2


 e                                                          f                                                                                                                                        g
                  0.4
                                                                                      0.08        Pearson’s r = 0.73                          Pearson’s r = 0.78
                  0.3
                                                                                      0.04

    rc,∞tr,ss   0.2                                                                                                                                                                                                         8


                                                                                                                                                                                                   Distance fluctuation (Å)
                                                         ds over laboratories
                  0.1
                                                                                  –0.04                                                                                                                                       6
                                                                                                                          All dye pairs                   Alexa546–Alexa647
                                                                                                  Pearson’s r = 0.88                          Pearson’s r = 0.82
                                                                                                                                                                                                                                                                            A
                                                                                      0.08                                                                                                                                                                                 DN
                                                                                                                                                                                                                              4                                        ds
                                                                                                                                                                                                                                                                      ds


  ∆Rapp(κ2) (%)
                                                                                      0.04

                  10                                                                                                                                                                                                          2

                                                                                  –0.04
                                                                                                                    Atto532–Atto643                       Alexa488–Alexa647
    ex                                                                                        0         0.1        0.2       0.3        0.4        0.1      0.2      0.3                     0.4                                      40         50          60       70         80
       a5 46
a546  –A
             –A  le xa                                                                                                               rc,∞tr,ss                                                                                              RE experiment (Å)
         bb ST         64 7
     At to      A R6
           53         35 P
 Al           2– At
    ex a4           to 64
          88 –A           3
Al               le xa 64 7
       ex
  Al

Fig. 5 | Assessing the accuracy of smFRET-derived distances in MalE. a–d, AV                                                                  were measured by two laboratories. e, Detection of dye-specific protein
calculations and model-based interdye distances. a, Schematic of Alexa546                                                                     interactions. Top shows the five MalE mutants and U2AF2 labeled with different
attached to MalE (PDB 1OMP) showing the parameters needed for the AV                                                                          dye combinations to determine the donor–acceptor-combined residual
calculations using the AV3 model6 (Supplementary Table 10). b, Fluorescence                                                                   anisotropy, 〈rc,∞〉tr,ss (n = 3 laboratories). Bottom shows the distance uncertainty
anisotropy decays of single-cysteine mutants for the donor (Alexa546, left) and                                                               relating to κ2, ΔRapp (κ2 ), estimated (Supplementary Note 8). A maximum allowed
acceptor (Alexa647, right) at the labeling positions K29C and S352C. Solid lines                                                              distance uncertainty of ≤10% (shaded gray region) in ΔRapp (κ2 ) leads to a
represent fits to a model with two or three rotational components                                                                             dye-independent threshold of 0.25 for 〈rc,∞〉. f, The apparent dynamic shift 〈ds〉
(Supplementary Tables 11 and 12 and Supplementary Note 8). c, AV (light color)                                                                versus the combined residual anisotropy 〈rc,∞〉 is shown for all measured dye pairs
and ACV (dark color) calculations for Alexa546 (cyan) and Alexa647 (pink) at                                                                  (top left) and individually. Error bars of the apparent ds represent the standard
labeling positions 352 and 29. The zoom-ins show the mean positions of the dyes                                                               deviation over n = 3 laboratories. For the combined residual anisotropy, the
based on the AV (light shade) and ACV (darker shade) models. d, Comparison of                                                                 propagated 1σ uncertainty (Supplementary Note 8). g, The structural flexibility
the experimentally obtained FRET-averaged distance R⟨E⟩ with the theoretical                                                                  of MalE estimated after filtering using the distance uncertainty threshold shown
model distances using the AV (filled squares) and ACV (empty squares)                                                                         in e (Supplementary Note 12). Error bars represent the 1σ percentiles averaged
calculations. Errors represent the standard deviation in experimental distances                                                               over all dye pairs (n = 1, MalE-1; n = 7, MalE-2 and MalE-3; n = 4, MalE-4 and n = 5,
(n = 16 laboratories for MalE mutants 1–3, n = 2 laboratories for MalE mutants 4–5,                                                           MalE-5). The residual distance fluctuations obtained from control measurements
n = 7 laboratories for U2AF). The solid line represents a 1:1 relation and the gray                                                           on dsDNA in one laboratory (dsdsDNA = 0.0026 ± 0.0044) are shown as a black line
area indicates an uncertainty of ±3 Å for a Förster radius of R0 = 65 Å. MalE-4 and -5                                                        (gray areas represent confidence intervals of 1σ, 2σ and 3σ).


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                                                                                                                                               530


Analysis                                                                                                                                        https://doi.org/10.1038/s41592-023-01807-0


a                                                              b                                                                                 e                                         Filtered-FCS
                                                                                          Distribution of
                                                                                                                                                     Weighted
           U2AF2 conformational ensemble
                                                                                               COM                                                                0

            Translation                                                                                                                              residuals    –2
                                                Rotation
                                                                                                                                                                2.0
                                                                                                                                                                                              tR,1                tR,2
                                                                                                                                                                 1.5

                                                                                                                                                                 1.0

                                                      ~180°                                                                                      G(tc)          0.5

                                                                                                                                                                                                                         SACF1
                                                                                                                                                               –0.5
                                                                                                                                                                                                                         SACF2
                                                                                                                                                                                                                         SCCF
                                                                                                 COM RRM1
                                                                                                                                                               –1.0
                                                                                                                                                                                     –6           –5         –4            –3
                                                                                                                                                                                   10        10          10               10
    0                FRET efficiency                       1                                                                                                                              Time lag tc (s)


c                                                              d                                    MEM distribution                             f                                 Photon distribution analysis
                    Apo ensemble                                                         Apo                          Alexa546–Alexa647                                    Apo
                                                                                                                      Atto532–Atto643
          Compact                        Detached
                       ~10 ms                                                                                         Alexa488–Alexa647
                                                                                                                      Prior (full ensemble)                    200


                                                               Probability density


                                                                                                                                                 Occurrences
                       >100 ms

                                                                                         + RNA                                                                             + RNA
                    +RNA          –RNA


                           Holo                                                      0         20   40        60       80        100      120                          0         0.2       0.4         0.6           0.8         1.0

                                                                                                            RDA (Å)                                                                       FRET efficiency

Fig. 6 | Structural characterization of U2AF2. a, Structural flexibility of U2AF2                               distance broadening due to the flexible dye linkers of 6 Å. The distribution in
is given by translational (left) and rotational (right) movement of the two                                     the donor–acceptor distance RDA for different dye pairs is shown. e, Filtered-FCS
domains. Representative structures are taken from the ensemble determined                                       reveals conformational dynamics in the U2AF2 apo ensemble on two timescales,
using NMR and SAXS measurements29. b, Degeneracy of structural states in                                        tR,1 = 9 ± 3 and tR,2 = 300 ± 90 µs, average and standard deviation (n = 3, results
FRET measurements. The position of the two domains of U2AF2 is illustrated                                      from laboratory 1 are shown). The two species were defined at the lower and
by the COM of the Cα atoms in RRM2 (residues 260–329, colored) with respect                                     upper edge of the FRET efficiency histogram shown in Fig. 2b, top panel (see
to RRM1 (residues 150–227, black) for the 200 structures of the conformational                                  Methods and Supplementary Note 16 for details). The species autocorrelation
ensemble29. The COM of RRM2 is color-coded according to the FRET efficiency                                     functions (SACFs) and one of the two species cross-correlation functions (SCCFs)
determined using AV3 calculations. c, A schematic of the kinetic model used                                     are shown. The weighted residuals are shown above. f, The PDA analysis was
for the global dynamic PDA of U2AF2 (Supplementary Note 17). d, Distance                                        conducted globally over both apo (top) and holo (bottom) measurements using
distributions obtained from a donor fluorescence decay analysis by a model-                                     time windows of 0.5, 1.0, 1.5 and 2.0 ms (the 1.0 ms time window histograms
free MEM approach (Supplementary Note 15). The distance distribution from                                       are shown). A relaxation time of roughly 10 ms for the dynamics between
the NMR–SAXS ensemble29 (light blue) was used as the prior distribution. The                                    the detached ensemble and compact apo state with a small amplitude was
expected interdye distances for the compact apo and open holo states are shown                                  determined (orange curve) (Supplementary Fig. 16 and Supplementary Note 17).
as red and blue dashed lines (PDB 2YH0 and 2YH1). Shaded areas indicate the


over all dye pairs (Pearson’s r = 0.73), with a stronger correlation when                                       variants after filtering out dye artifacts (Supplementary Note 11,
each dye pair is investigated individually (Fig. 5f). As conformational                                         Supplementary Table 8). To estimate the conformational fluctuations
dynamics should be label independent, dye sticking is likely responsible                                        necessary to generate the observed ds (Fig. 4f and Supplementary
for the observed ds values. The x intercept of the linear fit is between                                        Table 8), we assume that dynamics occur between two nearby states
0.1 and 0.2, suggesting a dye-dependent anisotropy threshold needs                                              with interdye distances of R⟨E⟩ ± δR where δR is the amplitude of the
to be considered. When applying the criteria 〈rc,∞〉 < 0.25 to MalE-1                                            fluctuation61 (Fig. 5g, Supplementary Note 12 and Supplementary
(Supplementary Fig. 12b), only the dye pair Atto532–Atto643 should                                              Table 8). This inferred fluctuation provides an upper bound for the
be used for distance determination, which also showed a markedly                                                conformational flexibility because factors such as calibration errors,
reduced ds (Supplementary Fig. 12c). Lifetime analysis of MalE-1                                                dye blinking or photoisomerization could contribute to the observed
donor-only molecules showed donor quenching only at position 352,                                               ds. We consider the ds obtained from dsDNA as the lower limit (black
which confirms that labeling at this position is problematic (Supple-                                           line in Fig. 5g, dsDNA = 0.0026 ± 0.0044: Supplementary Note 12), which
mentary Fig. 12c, Supplementary Note 10 and Supplementary Table 5).                                             defines the current detection limit for dynamics in smFRET experi-
     Using the above criteria of 〈rc,∞〉 < 0.25 to minimize the influence                                        ments. The MalE variants 1, 4 and 5 exceed the ds for dsDNA by 2–3 Å
of dye artifacts on the ds, we hypothesized that the remaining ds could                                         (Fig. 5g, Supplementary Fig. 13 and Supplementary Table 8). Consistent
be indicative of low-amplitude, fast conformational fluctuations.                                               with the smFRET results, all-atom molecular dynamics simulations of
 A P test analysis between the ds for dsDNA and protein samples                                                 MalE using the ff14SB force field74 (Supplementary Note 13) suggest
(P < 0.05) indicated that the ds is still significant for various protein                                       thermally induced conformational fluctuations with a standard


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                                                                                               531


Analysis                                                                                              https://doi.org/10.1038/s41592-023-01807-0

deviation up to roughly 3 Å at the labeled residues in MalE-1, MalE-4        Discussion
and MalE-5. This is larger than the typical fluctuations of about 1 Å        We show that smFRET can provide accurate distances of conforma-
(ref. 75) and leads to a broadening of the interresidue distance distribu-   tional states and reliable information on conformational dynamics
tions for these FRET pairs. We conclude that the observed ds in the          in proteins. Since all experiments were performed using established
experiments can be explained by a combination of measurement uncer-          techniques and analyzed with freely available software5,6,34,35,77–79, such
tainty and small-scale structural fluctuations. Note that such small-scale   information is accessible to any group with similar expertise. Despite
fluctuations can be amplified in FRET experiments when the dye linker        the challenges of protein samples, we achieved a similar precision in
acts as a lever arm for appropriate labeling positions. A detailed discus-   FRET efficiencies as reported for dsDNA18 (between ±0.02 and ±0.06)
sion of the theoretical limits for detecting dynamics in smFRET experi-      (Extended Data Table 1). The reproducibility in excluding large-scale
ments using BVA or the E–τ is given in Supplementary Note 14.                conformational dynamics for MalE on a timescale <10 ms while detect-
                                                                             ing large-scale submillisecond dynamics in U2AF2 shows that the com-
Quantitative analysis of U2AF2                                               munity can deal with dynamic protein systems. In addition, we could
The structural characterization of U2AF2 is more complex than for            consistently establish the timescales and hierarchy of the exchange
MalE and a simple distance comparison is not possible. Nonetheless,          dynamics in such a complex protein system as U2AF2. The study of com-
we asked what information smFRET measurements could provide for              plex dynamics is improvable by probing additional distances5,13,17,80–83.
such a dynamic system. We first surveyed the structural information                 The high level of agreement is notable given the diversity of the
available on apo U2AF2 from nuclear magnetic resonance (NMR) and             setups (Fig. 3 and Supplementary Fig. 2) and the number of possible
small-angle X-ray scattering (SAXS) data29. The highly flexible linker       pitfalls. A large contribution to the spread in the reported mean FRET
allows for a heterogeneous ensemble of U2AF2 conformations (Fig. 6a).        efficiencies was caused by systematic errors in the data analysis. This
To assess how this translates into a smFRET distribution, we quanti-         is supported by a comparison of the FRET efficiency changes
fied the FRET efficiency using AV calculations for all 200 conformers        (⟨Eholo ⟩ − ⟨Eapo ⟩) instead of absolute FRET efficiency values (Fig. 1d),
from the NMR–SAXS-derived ensemble of apo U2AF2 (ref. 29). Notably,          which reduced the spread of roughly threefold. Having a single person
conformations with similar center-of-mass (COM) distances between            reanalyze the data led to a similar decrease in the uncertainty of the
the domains showed different FRET efficiencies (Fig. 6a,b), because          FRET efficiency for the apo state of U2AF2 (Fig. 2d). Determination of
domain rotations result in distinct interdye distances for identical         γ was most crucial and the optimal approach depends on the details of
COM (Fig. 6a, right). Due to this degeneracy, a single-distance probe        the studied system (Supplementary Note 2). In the intensity-based
is insufficient to capture the full structural complexity.                   approach of Lee et al.34, multiple samples with uniform fluorophore
      The observed ds in the apo state suggests the presence of confor-      properties are required or individual corrections need to be made.
mational dynamics (Fig. 4d–f). To decipher the underlying kinetics           When using the approach of Kudryavtsev et al.35 via E–τ calibration, the
and their temporal hierarchy, we applied three analyses. First, we           system needs to be static and a single population suffices. A protocol
investigated the interdye distance distribution of the apo and holo          with unambiguous instructions for the calibration steps and minimized
states from the donor lifetime using a model-free maximum entropy            number of user-dependent steps would enhance the accuracy of
method (MEM) (Fig. 6c,d and Supplementary Note 15)76. As a prior, we         FRET measurements.
used the NMR–SAXS structural ensemble. This analysis yielded consist-               From accurate FRET efficiencies, we obtained reproducible inter-
ent results for all three dye pairs studied for U2AF2. The MEM analysis      dye distances with a precision of 3 Å and an accuracy of 5 Å against
revealed peaks in the probability density at the expected distances for      structural models of MalE (Extended Data Table 1). This is similar to
the compact apo conformation and RNA-bound holo structure (Fig. 6d,          what was determined for dsDNA samples. This is a very positive out-
dashed lines). We note that the fluorescence lifetime analysis resolves      come, given that dsDNA features a consistent, homogenous chemical
states on the nanosecond timescale and is therefore less sensitive to        environment for each labeling position, in contrast to the variable dye
dynamic averaging.                                                           environment experienced in proteins. The distance determination
      Second, to assess the dynamics on the microsecond timescale,           could be improved by including the interaction of the fluorophores
three groups performed filtered-FCS and found at least two relaxation        with the protein surface using ACV calculations (Fig. 5d and Methods)63.
times (9 ± 3 and 300 ± 90 µs; Fig. 6e, Supplementary Table 15 and Sup-       Furthermore, we give experimental support (Fig. 5f) for only using
plementary Note 16), which were independent of the dyes used (Sup-           dyes with a combined residual anisotropy of rc,∞ < 0.25, as suggested
plementary Fig. 15). We assign the fast process to dynamics within the       previously13,70. Proteins often exist within a family of conformations
detached domains and the slower process to interconversion between           as we observed for U2AF2 (Fig. 6d). Determining how to best deal
compact conformations within the conformational ensemble.                    with distance distributions for conformational ensembles is one of
      Last, we investigated dynamics on the millisecond timescale using      the challenges for structural biology.
a dynamic PDA. A global analysis of the apo and holo measurements was               Investigating different dye pairs allowed us to reduce dye artifacts,
performed using the kinetic model shown in Fig. 6c (Supplementary            leading to more accurate FRET efficiencies and reliable detection
Note 17 and Supplementary Table 16). The apo state was treated as a          of the dynamics. Hence, we investigated the detection limits for ds
two-state system with slow dynamics between a detached ensemble and          and studied its relation to conformational dynamics with a subset of
a well-defined, compact apo conformation. The rapid dynamics within          laboratories. Besides conformational motions, dynamic FRET shifts
the detached ensemble is empirically described using a broad, static         can occur in different directions and have several origins including
distribution. For the holo measurement, we account for the residual          structural instabilities37 or photophysics (as shown in Fig. 5f)44. Thus,
population of apo molecules. Exchange between the holo and apo states        it is advisable to verify the key findings in smFRET measurements with
is irrelevant as the binding and dissociation of RNA occurs on timescales    at least two dye pairs and/or with different residue combinations in the
of more than 100 ms (ref. 36). This model incorporates all information       protein. Once the non-FRET-dynamic contributions are minimized, we
and is sufficient to describe the smFRET efficiency histograms. The          still observed significant residual ds for MalE. Consistent with molecu-
dynamic PDA analysis returned a relaxation time of roughly 10 ms             lar dynamics simulations (Supplementary Note 13), we interpret these
for the dynamics between the detached ensemble and compact apo               shifts as small-scale conformational dynamics and established a cur-
state (Fig. 6f, orange curve, Supplementary Fig. 16 and Supplementary        rent lower limit for the detection of structural changes via smFRET on
Table 16). We also determined an interdye distance of R〈E〉 = 61 Å in the     the order of ≤5 Å. In summary, the consensus of smFRET experiments
RNA-bound holo state, which is in good agreement with 63 Å from the          on two protein systems exhibiting dynamic behavior on different spa-
RNA-bound conformation (Protein Data Bank (PDB) 2YH1).                       tiotemporal scales obtained blindly from 19 laboratories offers strong


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                   532


Analysis                                                                                             https://doi.org/10.1038/s41592-023-01807-0

support for its use as a robust, versatile and quantitative tool for the         RNAP-promoter open complex as an example. J. Chem. Phys. 148,
coming age of dynamic structural biology. In this context, it will be            123315 (2018).
crucial to integrate the correlated structural and dynamic information       17. Craggs, T. D. et al. Substrate conformational dynamics
provided by smFRET1 with structural information provided by other                facilitate structure-specific recognition of gapped DNA by DNA
experimental techniques as well as artificial intelligence-based protein         polymerase. Nucleic Acids Res. 47, 10788–10800 (2019).
structural prediction83. Considering that protein structure predic-          18. Hellenkamp, B. et al. Precision and accuracy of single-molecule
tion has reached the single-structure frontier84, the information from           FRET measurements—a multi-laboratory benchmark study.
smFRET experiments could leverage the power of artificial intelligence           Nat. Methods 15, 669–676 (2018).
to resolve more complex multi-state and ensemble structural models83.        19. Rout, M. P. & Sali, A. Principles for integrative structural biology
Vice versa, the power of artificial intelligence and deep learning can be        studies. Cell 177, 1384–1403 (2019).
used to increase the throughput for the design and analysis of smFRET        20. Sali, A. From integrative structural biology to cell biology. J. Biol.
experiments85–87.                                                                Chem. 296, 100743 (2021).
                                                                             21. Burley, S. K. et al. PDB-Dev: a prototype system for depositing
Online content                                                                   integrative/hybrid structural models. Structure 25, 1317–1318 (2017).
Any methods, additional references, Nature Portfolio reporting sum-          22. Davidson, A. L., Dassa, E., Orelle, C. & Chen, J. Structure, function,
maries, source data, extended data, supplementary information,                   and evolution of bacterial ATP-binding cassette systems.
acknowledgements, peer review information; details of author contri-             Microbiol. Mol. Biol. Rev. 72, 317–364 (2008).
butions and competing interests; and statements of data and code avail-      23. Mächtel, R., Narducci, A., Griffith, D. A., Cordes, T. & Orelle, C. An
ability are available at https://doi.org/10.1038/s41592-023-01807-0.             integrated transport mechanism of the maltose ABC importer.
                                                                                 Res. Microbiol. 170, 321–337 (2019).
References                                                                   24. Malik, A. Protein fusion tags for efficient expression and
1.    Lerner, E. et al. FRET-based dynamic structural biology:                   purification of recombinant proteins in the periplasmic space of
      challenges, perspectives and an appeal for open-science                    E. coli. 3 Biotech 6, 44 (2016).
      practices. eLife 10, e60416 (2021).                                    25. Berntsson, R. P. A., Smits, S. H. J., Schmitt, L., Slotboom, D. J.
2.    Lerner, E. et al. Toward dynamic structural biology: two decades           & Poolman, B. A structural classification of substrate-binding
      of single-molecule Förster resonance energy transfer. Science              proteins. FEBS Lett. 584, 2606–2617 (2010).
      359, eaan1133 (2018).                                                  26. Fukami-Kobayashi, K., Tateno, Y. & Nishikawa, K. Domain
3.    Algar, W. R., Hildebrandt, N., Vogel, S. S. & Medintz, I. L. FRET as       dislocation: a change of core structure in periplasmic binding
      a biomolecular research tool—understanding its potential while             proteins in their evolutionary history. J. Mol. Biol. 286, 279–290
      avoiding pitfalls. Nat. Methods 16, 815–829 (2019).                        (1999).
4.    Hildebrandt, N. in FRET—Förster Resonance Energy Transfer              27. Banerjee, H., Rahn, A., Davis, W. & Singh, R. Sex lethal and U2
      (eds Medintz, I. & Hildebrandt, N.) 105–163 (Wiley, 2013).                 small nuclear ribonucleoprotein auxiliary factor (U2AF65)
5.    Muschielok, A. et al. A nano-positioning system for                        recognize polypyrimidine tracts using multiple modes of binding.
      macromolecular structural analysis. Nat. Methods 5,                        RNA 9, 88–99 (2003).
      965–971 (2008).                                                        28. Sickmier, E. A. et al. Structural basis for polypyrimidine tract
6.    Kalinin, S. et al. A toolkit and benchmark study for FRET-                 recognition by the essential pre-mRNA splicing factor U2AF65.
      restrained high-precision structural modeling. Nat. Methods 9,             Mol. Cell 23, 49–59 (2006).
      1218–1225 (2012).                                                      29. Huang, J. R. et al. Transient electrostatic interactions dominate
7.    Craggs, T. D. & Kapanidis, A. N. Six steps closer to FRET-driven           the conformational equilibrium sampled by multidomain splicing
      structural biology. Nat. Methods 9, 1157–1159 (2012).                      factor U2AF65: a combined NMR and SAXS study. J. Am. Chem.
8.    Voith von Voithenberg, L. & Lamb, D. C. Single pair Förster                Soc. 136, 7068–7076 (2014).
      resonance energy transfer: a versatile tool to investigate protein     30. MacKereth, C. D. et al. Multi-domain conformational selection
      conformational dynamics. BioEssays 40, 1700078 (2018).                     underlies pre-mRNA splicing regulation by U2AF. Nature 475,
9.    Hohlbein, J., Craggs, T. D. & Cordes, T. Alternating-laser                 408–413 (2011).
      excitation: single-molecule FRET and beyond. Chem. Soc. Rev.           31. Kapanidis, A. N. et al. Fluorescence-aided molecule sorting:
      43, 1156–1171 (2014).                                                      analysis of structure and interactions by alternating-laser
10.   Krainer, G., Hartmann, A. & Schlierf, M. FarFRET: extending the            excitation of single molecules. Proc. Natl Acad. Sci. USA 101,
      range in single-molecule FRET experiments beyond 10 nm.                    8936–8941 (2004).
      Nano Lett. 15, 5826–5829 (2015).                                       32. Kapanidis, A. N. et al. Alternating-laser excitation of single
11.   Muschielok, A. & Michaelis, J. Application of the nano-positioning         molecules. Acc. Chem. Res. 38, 523–533 (2005).
      system to the analysis of fluorescence resonance energy transfer       33. Müller, B. K., Zaychikov, E., Bräuchle, C. & Lamb, D. C. Pulsed
      networks. J. Phys. Chem. B. 115, 11927–11937 (2011).                       interleaved excitation. Biophys. J. 89, 3508–3522 (2005).
12.   Sali, A. et al. Outcome of the first wwPDB Hybrid/Integrative          34. Lee, N. K. et al. Accurate FRET measurements within single
      Methods Task Force Workshop. Structure 23, 1156–1167 (2015).               diffusing biomolecules using alternating-laser excitation.
13.   Hellenkamp, B., Wortmann, P., Kandzia, F., Zacharias, M. &                 Biophys. J. 88, 2939–2953 (2005).
      Hugel, T. Multidomain structure and correlated dynamics                35. Kudryavtsev, V. et al. Combining MFD and PIE for accurate
      determined by self-consistent FRET networks. Nat. Methods 14,              single-pair Förster resonance energy transfer measurements.
      176–182 (2017).                                                            Chem. Phys. Chem. 13, 1060–1078 (2012).
14.   Choi, U. B. et al. Single-molecule FRET-derived model of the           36. Von Voithenberg, L. V. et al. Recognition of the 3′ splice site RNA
      synaptotagmin 1-SNARE fusion complex. Nat. Struct. Mol. Biol. 17,          by the U2AF heterodimer involves a dynamic population shift.
      318–324 (2010).                                                            Proc. Natl Acad. Sci. USA 113, E7169–E7175 (2016).
15.   Dimura, M. et al. Automated and optimally FRET-assisted                37. Sánchez-Rico, C., Voith von Voithenberg, L., Warner, L.,
      structural modeling. Nat. Commun. 11, 5394 (2020).                         Lamb, D. C. & Sattler, M. Effects of fluorophore attachment on
16.   Lerner, E., Ingargiola, A. & Weiss, S. Characterizing highly               protein conformation and dynamics studied by spFRET and
      dynamic conformational states: the transcription bubble in                 NMR spectroscopy. Chemistry 23, 14267–14277 (2017).


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                  533


Analysis                                                                                             https://doi.org/10.1038/s41592-023-01807-0

38. Eggeling, C., Widengren, J., Rigler, R. & Seidel, C. A. M.               57. Chung, H. S. & Gopich, I. V. Fast single-molecule FRET
    Photobleaching of fluorescent dyes under conditions used for                 spectroscopy: theory and experiment. Phys. Chem. Chem. Phys.
    single-molecule detection: evidence of two-step photolysis.                  16, 18644–18657 (2014).
    Anal. Chem. 70, 2651–2659 (1998).                                        58. Pirchi, M. et al. Photon-by-photon hidden Markov model analysis
39. Chung, H. S., McHale, K., Louis, J. M. & Eaton, W. A.                        for microsecond single-molecule FRET kinetics. J. Phys. Chem. B.
    Single-molecule fluorescence experiments determine protein                   120, 13065–13075 (2016).
    folding transition path times. Science 335, 981–984 (2012).              59. Harris, P. D. et al. Multi-parameter photon-by-photon hidden
40. Ramanathan, R. & Muñoz, V. A method for extracting the free                  Markov modeling. Nat. Commun. 13, 1000 (2022).
    energy surface and conformational dynamics of fast-folding               60. Ingargiola, A., Weiss, S. & Lerner, E. Monte Carlo
    proteins from single molecule photon trajectories. J. Phys. Chem.            diffusion-enhanced photon inference: distance distributions and
    B. 119, 7944–7956 (2015).                                                    conformational dynamics in single-molecule FRET. J. Phys. Chem.
41. McKinney, S. A., Joo, C. & Ha, T. Analysis of single-molecule                B. 122, 11598–11615 (2018).
    FRET trajectories using hidden Markov modeling. Biophys. J. 91,          61. Barth, A. et al. Unraveling multi-state molecular dynamics in
    1941–1951 (2006).                                                            single-molecule FRET experiments. I. Theory of FRET-lines. J.
42. Liu, Y., Park, J., Dahmen, K. A., Chemla, Y. R. & Ha, T. A comparative       Chem. Phys. 156, 141501 (2022).
    study of multivariate and univariate hidden Markov modelings in          62. De Boer, M. et al. Conformational and dynamic plasticity in
    time-binned single-molecule FRET data analysis. J. Phys. Chem. B.            substrate-binding proteins underlies selective transport in ABC
    114, 5386–5403 (2010).                                                       importers. eLife 8, e44652 (2019).
43. Bronson, J. E., Fei, J., Hofman, J. M., Gonzalez, R. L. &                63. Dimura, M. et al. Quantitative FRET studies and integrative
    Wiggins, C. H. Learning rates and states from biophysical                    modeling unravel the structure and dynamics of biomolecular
    time series: a Bayesian approach to model selection and                      systems. Curr. Opin. Struct. Biol. 40, 163–185 (2016).
    single-molecule FRET data. Biophys. J. 97, 3196–3205 (2009).             64. Sindbert, S. et al. Accurate distance determination of
44. Margittai, M. et al. Single-molecule fluorescence resonance                  nucleic acids via Förster resonance energy transfer: implications
    energy transfer reveals a dynamic equilibrium between closed                 of dye Linker length and rigidity. J. Am. Chem. Soc. 133,
    and open conformations of syntaxin 1. Proc. Natl Acad. Sci. USA              2463–2480 (2011).
    100, 15516–15521 (2003).                                                 65. Steffen, F. D., Sigel, R. K. O. & Börner, R. An atomistic view on
45. Diez, M. et al. Proton-powered subunit rotation in single                    carbocyanine photophysics in the realm of RNA. Phys. Chem.
    membrane-bound F 0F1-ATP synthase. Nat. Struct. Mol. Biol. 11,               Chem. Phys. 18, 29045–29055 (2016).
    135–141 (2004).                                                          66. Klose, D. et al. Resolving distance variations by single-molecule
46. Torres, T. & Levitus, M. Measuring conformational dynamics: a                FRET and EPR spectroscopy using rotamer libraries. Biophys. J.
    new FCS-FRET approach. J. Phys. Chem. B. 111, 7392–7400 (2007).              120, 4842–4858 (2021).
47. Felekyan, S., Sanabria, H., Kalinin, S., Kühnemuth, R. &                 67. Reinartz, I. et al. Simulation of FRET dyes allows quantitative
    Seidel, C. A. M. Analyzing Förster resonance energy transfer with            comparison against experimental data. J. Chem. Phys. 148,
    fluctuation algorithms. Methods Enzymol. 519, 39–85 (2013).                  123321 (2018).
48. Felekyan, S., Kalinin, S., Sanabria, H., Valeri, A. & Seidel, C. A.      68. Hoefling, M. et al. Structural heterogeneity and quantitative FRET
    M. Filtered FCS: species auto- and cross-correlation functions               efficiency distributions of polyprolines through a hybrid atomistic
    highlight binding and dynamics in biomolecules. Chem. Phys.                  simulation and monte carlo approach. PLoS ONE 6, 19791 (2011).
    Chem. 13, 1036–1053 (2012).                                              69. Peulen, T. O., Opanasyuk, O. & Seidel, C. A. M. Combining
49. Olofsson, L. et al. Fine tuning of sub-millisecond conformational            graphical and analytical methods with molecular simulations
    dynamics controls metabotropic glutamate receptors agonist                   to analyze time-resolved FRET measurements of labeled
    efficacy. Nat. Commun. 5, 5206 (2014).                                       macromolecules accurately. J. Phys. Chem. B. 121, 8211–8241
50. Torella, J. P., Holden, S. J., Santoso, Y., Hohlbein, J. &                   (2017).
    Kapanidis, A. N. Identifying molecular dynamics in single-               70. Dale, R. E., Eisinger, J. & Blumberg, W. E. The orientational
    molecule FRET experiments with burst variance analysis.                      freedom of molecular probes. The orientation factor in
    Biophys. J. 100, 1568–1577 (2011).                                           intramolecular energy transfer. Biophys. J. 26, 161–193 (1979).
51. Tomov, T. E. et al. Disentangling subpopulations in                      71. Dale, R. E. & Eisinger, J. Intramolecular distances determined by
    single-molecule FRET and ALEX experiments with photon                        energy transfer. Dependence on orientational freedom of donor
    distribution analysis. Biophys. J. 102, 1163–1173 (2012).                    and acceptor. Biopolymers 13, 1573–1605 (1974).
52. Kalinin, S., Valeri, A., Antonik, M., Felekyan, S. & Seidel, C. A. M.    72. Ivanov, V., Li, M. & Mizuuchi, K. Impact of emission anisotropy on
    Detection of structural dynamics by FRET: a photon distribution              fluorescence spectroscopy and FRET distance measurements.
    and fluorescence lifetime analysis of systems with multiple states.          Biophys. J. 97, 922–929 (2009).
    J. Phys. Chem. B. 114, 7983–7995 (2010).                                 73. Eilert, T., Kallis, E., Nagy, J., Röcker, C. & Michaelis, J. Complete
53. Gopich, I. V. & Szabo, A. Theory of the energy transfer efficiency           kinetic theory of FRET. J. Phys. Chem. B 122, 11677–11694 (2018).
    and fluorescence lifetime distribution in single-molecule FRET.          74. Maier, J. A. et al. ff14SB: improving the accuracy of protein side
    Proc. Natl Acad. Sci. USA 109, 7747–7752 (2012).                             chain and backbone parameters from ff99SB. J. Chem. Theory
54. Nettels, D., Gopich, I. V., Hoffmann, A. & Schuler, B. Ultrafast             Comput. 11, 3696–3713 (2015).
    dynamics of protein collapse from single-molecule photon                 75. Zaccai, G. How soft is a protein? A protein dynamics force
    statistics. Proc. Natl Acad. Sci. USA 104, 2655–2660 (2007).                 constant measured by neutron scattering. Science 288,
55. Hoffmann, A. et al. Quantifying heterogeneity and conformational             1604–1607 (2000).
    dynamics from single molecule FRET of diffusing molecules:               76. Vinogradov, S. A. & Wilson, D. F. Recursive maximum entropy
    recurrence analysis of single particles (RASP). Phys. Chem. Chem.            algorithm and its application to the luminescence lifetime
    Phys. 13, 1857–1871 (2011).                                                  distribution recovery. Appl. Spectrosc. 54, 849–855 (2000).
56. Gopich, I. V. & Szabo, A. Decoding the pattern of photon                 77. Ingargiola, A., Lerner, E., Chung, S. Y., Weiss, S. & Michalet, X.
    colors in single-molecule FRET. J. Phys. Chem. B. 113,                       FRETBursts: an open source toolkit for analysis of freely-diffusing
    10965–10973 (2009).                                                          Single-molecule FRET. PLoS ONE 11, 39198 (2016).


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                 534


Analysis                                                                                               https://doi.org/10.1038/s41592-023-01807-0

78. Schrimpf, W., Barth, A., Hendrix, J. & Lamb, D. C. PAM: a                 86. Thomsen, J. et al. DeepFRET, a software for rapid and automated
    framework for integrated analysis of imaging, single-molecule,                single-molecule FRET data classification using deep learning.
    and ensemble fluorescence data. Biophys. J. 114, 1518–1528                    eLife 9, e60404 (2020).
    (2018).                                                                   87. Wanninger, S. et al. Deep-learning assisted, single-molecule
79. Ambrose, B. et al. The smfBox is an open-source platform for                  imaging analysis (Deep-LASI) of multi-color DNA Origami
    single-molecule FRET. Nat. Commun. 11, 5641 (2020).                           structures. Preprint at bioRxiv https://doi.org/10.1101/2023.
80. Knight, J. L., Mekler, V., Mukhopadhyay, J., Ebright, R. H. &                 01.31.526220 (2023).
    Levy, R. M. Distance-restrained docking of rifampicin and
    rifamycin SV to RNA polymerase using systematic FRET                      Publisher’s note Springer Nature remains neutral with regard to
    measurements: developing benchmarks of model quality and                  jurisdictional claims in published maps and institutional affiliations.
    reliability. Biophys. J. 88, 925–938 (2005).
81. Kapanidis, A. N. et al. Initial transcription by RNA polymerase           Open Access This article is licensed under a Creative Commons
    proceeds through a DNA-scrunching mechanism. Science 314,                 Attribution 4.0 International License, which permits use, sharing,
    1144–1147 (2006).                                                         adaptation, distribution and reproduction in any medium or format,
82. Sanabria, H. et al. Resolving dynamics and function of transient          as long as you give appropriate credit to the original author(s) and the
    states in single enzyme molecules. Nat. Commun. 11, 1231                  source, provide a link to the Creative Commons license, and indicate
    (2020).                                                                   if changes were made. The images or other third party material in this
83. Berman, H. M. et al. Federating structural models and data:               article are included in the article’s Creative Commons license, unless
    outcomes from a workshop on archiving integrative. Structures.            indicated otherwise in a credit line to the material. If material is not
    Structure 27, 1745–1759 (2019).                                           included in the article’s Creative Commons license and your intended
84. Lane, T. J. Protein structure prediction has reached the                  use is not permitted by statutory regulation or exceeds the permitted
    single-structure frontier. Nat. Methods 20, 170–173 (2023).               use, you will need to obtain permission directly from the copyright
85. Li, J., Zhang, L., Johnson-Buck, A. & Walter, N. G. Automatic             holder. To view a copy of this license, visit http://creativecommons.
    classification and segmentation of single-molecule                        org/licenses/by/4.0/.
    fluorescence time traces with deep learning. Nat. Commun. 11,
    5833 (2020).                                                              © The Author(s) 2023


Ganesh Agam 1,33, Christian Gebhardt 2,33, Milana Popara 3,33, Rebecca Mächtel2, Julian Folz 3,
Benjamin Ambrose 4, Neharika Chamachi 5, Sang Yoon Chung6, Timothy D. Craggs 4, Marijn de Boer7,
Dina Grohmann 8, Taekjip Ha 9, Andreas Hartmann 5, Jelle Hendrix 10,11, Verena Hirschfeld12, Christian G. Hübner12,
Thorsten Hugel 13,14, Dominik Kammerer15,16, Hyun-Seo Kang 17, Achillefs N. Kapanidis15,16, Georg Krainer 5,18,
Kevin Kramm8, Edward A. Lemke 19,20,21, Eitan Lerner 22, Emmanuel Margeat 23, Kirsten Martens24, Jens Michaelis 25,
Jaba Mitra9,26, Gabriel G. Moya Muñoz 2, Robert B. Quast 23, Nicole C. Robb15,16,30, Michael Sattler17,27,
Michael Schlierf 5,28, Jonathan Schneider2, Tim Schröder 1, Anna Sefer25, Piau Siong Tan19,20, Johann Thurn 13,31,
Philip Tinnefeld1, John van Noort 24, Shimon Weiss 6,29, Nicolas Wendler 2, Niels Zijlstra2, Anders Barth 3,32 ,
Claus A. M. Seidel 3 , Don C. Lamb 1 & Thorben Cordes 2

 Department of Chemistry, Ludwig-Maximilians University München, München, Germany. 2Physical and Synthetic Biology, Faculty of Biology,
Ludwig-Maximilians University München, Planegg-Martinsried, Germany. 3Molecular Physical Chemistry, Heinrich-Heine University Düsseldorf,
Düsseldorf, Germany. 4Department of Chemistry, University of Sheffield, Sheffield, UK. 5B CUBE – Center for Molecular Bioengineering, Technische
Universität Dresden, Dresden, Germany. 6Department of Chemistry and Biochemistry, University of California, Los Angeles, CA, USA. 7Molecular
Microscopy Research Group, Zernike Institute for Advanced Materials, University of Groningen, AG Groningen, the Netherlands. 8Department of
Biochemistry, Genetics and Microbiology, Institute of Microbiology, Single-Molecule Biochemistry Laboratory, University of Regensburg, Regensburg,
Germany. 9Department of Biophysics and Biophysical Chemistry, Johns Hopkins University School of Medicine and Howard Hughes Medical Institute,
Baltimore, MD, USA. 10Dynamic Bioimaging Laboratory, Advanced Optical Microscopy Center and Biomedical Research Institute, Hasselt University,
Agoralaan C (BIOMED), Hasselt, Belgium. 11Department of Chemistry, KU Leuven, Leuven, Belgium. 12Institute of Physics, University of Lübeck, Lübeck,
Germany. 13Institute of Physical Chemistry, University of Freiburg, Freiburg, Germany. 14Signalling Research Centers BIOSS and CIBSS, University of
Freiburg, Freiburg, Germany. 15Department of Physics, Clarendon Laboratory, University of Oxford, Oxford, UK. 16Kavli Institute of Nanoscience Discovery,
University of Oxford, Oxford, UK. 17Bayerisches NMR Zentrum, Department of Bioscience, School of Natural Sciences, Technical University of München,
Garching, Germany. 18Yusuf Hamied Department of Chemistry, University of Cambridge, Cambridge, UK. 19Biocenter, Johannes Gutenberg University
Mainz, Mainz, Germany. 20Institute of Molecular Biology, Mainz, Germany. 21Structural and Computational Biology Unit, European Molecular Biology
Laboratory, Heidelberg, Germany. 22Department of Biological Chemistry, The Alexander Silberman Institute of Life Sciences, and The Center for
Nanoscience and Nanotechnology, Faculty of Mathematics and Science, The Edmond J. Safra Campus, The Hebrew University of Jerusalem, Jerusalem,
Israel. 23Centre de Biologie Structurale (CBS), University of Montpellier, CNRS, INSERM, Montpellier, France. 24Biological and Soft Matter Physics,
Huygens–Kamerlingh Onnes Laboratory, Leiden University, Leiden, the Netherlands. 25Institute for Biophysics, Ulm University, Ulm, Germany. 26Materials
Science and Engineering, University of Illinois Urbana-Champaign, Urbana, IL, USA. 27Institute of Structural Biology, Molecular Targets and Therapeutics
Center, Helmholtz Center Munich, Munich, Germany. 28Cluster of Excellence Physics of Life, Technische Universität Dresden, Dresden, Germany.
  California NanoSystems Institute, University of California, Los Angeles, CA, USA. 30Present address: Warwick Medical School, The University of Warwick,
Coventry, UK. 31Present address: Institute of Technical Physics, German Aerospace Center (DLR), Stuttgart, Germany. 32Present address: Department
of Bionanoscience, Kavli Institute of Nanoscience, Delft University of Technology, Delft, the Netherlands. 33These authors contributed equally:
Ganesh Agam, Christian Gebhardt, Milana Popara.         e-mail: a.barth@tudelft.nl; cseidel@hhu.de; d.lamb@lmu.de; cordes@bio.lmu.de


Nature Methods | Volume 20 | April 2023 | 523–535                                                                                                    535


Analysis                                                                                                    https://doi.org/10.1038/s41592-023-01807-0

Methods                                                                                    donor emission after donor excitation ∶ i IDem|Dex ,
Sample preparation of proteins
Double-cysteine mutants of MalE were prepared and labeled using
                                                                                  acceptor emission after donor excitation (FRET signal) ∶ i IAem|Dex ,
established protocols62. Human RRM1,2 L187C-G326C mutant (U2AF2-
148-342) was obtained and purified as described in Mackereth et al.30.
                                                                                      and acceptor emission after acceptor excitation ∶ i IAem|Dex .
Fluorescence labeling of proteins
All fluorophores were purchased as maleimide derivatives from
commercial suppliers as listed in Supplementary Table 19. MalE was                The apparent (raw) FRET efficiency is computed as:
stochastically labeled as described previously88 with fluorophores as
                                                                                                                           i
indicated in the text with a combined labeling efficiency higher than                                                          IAem|Dex
                                                                                                           Eapp =                                ,        (3)
                                                                                                                    iI
                                                                                                                      Dem|Dex + IAem|Dex
                                                                                                                               i
70% resulting in a donor–acceptor pairing of at least 20%. Protein stabil-
ity and functionality (ligand binding) was verified by affinity measure-
ments using microscale thermophoresis89. All preparations, that is,              Recorded intensities were corrected for background contribu-
MalE-wildtype, unlabeled cysteine mutants and fluorophore-labeled            tions as:
variants, showed an affinity for maltose between roughly 1 and
                                                                                                     ii                                   (BG)
2 µM (Supplementary Fig. 5) consistent with previously published                                          IDem|Dex = i IDem|Dex − i IDem|Dex ,            (4)
Kdvalues for wildtype MalE90,91. The stability and labeling of the sam-
ple were verified by FCS (Supplementary Fig. 18), which excluded                                                                          (BG)
                                                                                                     ii
                                                                                                           IAem|Dex = i IAem|Dex − IAem|Dex ,             (5)
the presence of larger aggregates in the samples and confirms that
MalE is functional.
     U2AF2 was stochastically labeled as described previously in Voith                                ii                                  (BG)
                                                                                                           IAem|Aex = i IAem|Aex − IAem|Aex ,             (6)
von Voithenberg et al.36. The combined labeling efficiencies for the
labeling reactions were 20 and 14% for the Alexa546–Alexa647 and
                                                                                    (BG)      (BG)         (BG)
Atto532–Atto643 pairs, respectively. For Alexa488–Alexa647, the              where IDem|Dex, IAem|Dex and IAem|Aex are the respective background signals.
combined labeling efficiency was found to be 10%. The functionality          Correction factors for spectral crosstalk, α and direct excitation, δ,
of the labeled U2AF protein was checked with affinity measurements           were determined from the donor- and acceptor-only populations34.
for U9 RNA, which was found to be 1.2 µM (ref. 30), consistent with the      The corrected acceptor fluorescence after donor excitation, FA|D, is
previous reports36 (Supplementary Fig. 7d).                                  computed as:

Sample handling                                                                                FA|D = ii IAem|Dex − α ii IDem|Dex − δ ii IAem|Aex         (7)
Both protein systems required special handling due to sample instabil-
ity or aggregate formation, which are both problematic for long-term              The γ and β factors, correcting for differences in the detec­tion
storage and shipping. The labeled MalE proteins were stored in 50 mM         yield and excitation fluxes of the donor and acceptor dyes, were
Tris-HCl pH 7.4, 50 mM KCl with 1 mg ml−1 BSA at 4 °C for less than          estimated using a global correction procedure following the
7 d. U2AF2 was stored in 20 mM potassium phosphate buffer pH 6.5,            approach of Lee et al. (Supplementary Fig. 3)34. Alternatively, when
50 mM NaCl and kept in the fridge until used. Both samples were loaded       pulsed excitation was used and the sample is known to be static,
in low-binding Eppendorf tubes (Eppendorf Germany, catalog no.               the γ factor can be determined by fitting the measured population
0030108094) and shipped on ice in a cooling box with overnight ship-         to the static FRET line35,92. This allows a robust determination of
ping to avoid unnecessary freezing and thawing. MalE stock solutions         the γ factor when only a single species is present but requires
were on the order of 10 to 100 nM concentration and the sent stock           a static sample and the appropriate static FRET line (Supplementary
solution of U2AF2 was 5–10 µM concentration. Dilution buffers for            Note 2).
apo and holo measurements were provided. SmFRET experiments                       The accurate FRET efficiency E and stoichiometry S values were
were carried out by diluting the labeled proteins to concentrations          then calculated as:
of roughly 50 pM in 50 mM Tris-HCl pH 7.4, 50 mM KCl supplemented
                                                                                                                               FA|D
with the ligand maltose at 1 mM concentration. Labeled U2AF2 protein                                          E=                             ,            (8)
was measured at roughly 40–100 pM in 20 mM potassium phosphate                                                      γ ii IDem|Dex + FA|D
buffer pH 6.5, 50 mM NaCl. Purchased U9 RNA (Biomers.net GmbH and
IBA Solutions for Life Sciences) was dissolved in RNA-free water and                                                γ ii IDem|Dex + FA|D
added directly to the solution at a final concentration of 5 µM for the                           S=                                                 .    (9)
                                                                                                           γ ii IDem|Dex + FA|D + ii IAem|Aex /β
holo measurements. Both proteins were studied on coverslips typically
passivated with 1 mg ml−1 BSA in buffer before adding the sample. The
measurements were performed without any photostabilizer to keep                 Conversion of accurate FRET efficiencies into distances were
the measurements as simple as possible to avoid any further source           done using equation (2) with Förster radii determined as described in
for discrepancies between the groups, for example, degradation of            Supplementary Note 7.
photostabilizer or use of different photostabilizer concentrations.
                                                                             Detection of protein dynamics
SmFRET data acquisition and analysis                                         In this work, we used the following two approaches to detect confor-
Data acquisition and correction procedures were performed for con-           mational dynamics:
focal measurements as described by Hellenkamp et al.18. The samples
were measured using ALEX or PIE on a confocal microscope as sketched         BVA. In BVA, the presence of dynamics is determined by looking for
in Supplementary Fig. 2. A description of the experimental procedures        excess variance in the FRET efficiency data beyond the shot-noise limit.
of all laboratories is given in Supplementary Note 18.                       The standard deviation ( σEapp) of the apparent FRET efficiency (Eapp) is
      Briefly, the three recorded intensity time traces for each             calculated using a fixed photon window of n = 5 over the time period
single-molecule event are:                                                   of the individual bursts given by:


Nature Methods


Analysis                                                                                            https://doi.org/10.1038/s41592-023-01807-0


                          σEapp =
                                        Eapp (1−Eapp )
                                                         ,         (10)
                                                                           Data availability
                                    √         n                            The data for all figures, all supplementary figures, the raw data for MalE
                                                                           measurements from all laboratories (with the exception of one mutant
     The shot-noise limited standard deviation of the apparent FRET        from one laboratory) and the raw data for all U2AF2 measurements have
efficiency is generally described by a semicircle50 (Fig. 4a and Supple­   been uploaded to Zenodo (https://doi.org/10.5281/zenodo.7472900).
mentary Fig. 11a–d). In the presence of dynamics, the standard devia-      PDB IDs used are 1OMP, 1ANF, 2YHO and 2YH1. Source data are provided
tion for the FRET efficiency within a burst becomes higher than that       with this paper.
expected from shot noise. Photophysical effects such as photobleach-
ing and blinking also give rise to the higher standard deviation beyond    Code availability
the shot-noise limit. Typically, BVA is sensitive to fluctuations in       The software used for data analysis are available from the respective
the FRET signal of ≳100 µs, but this depends on the brightness of the      laboratories: laboratory no. 1, PAM (PIE Analysis with MATLAB) soft-
burst and the photon window used.                                          ware package (ref. 79 in the main text); laboratory no. 2, Home-written
                                                                           LabView-based software (ref. 15 in Supplementary Information); Labo-
FRET efficiency versus fluorescence-weighted average donor                 ratory no. 3, FRETBursts toolkit (ref. 14 in Supplementary Information);
lifetime analysis (E–τ plots). Two-dimensional histograms of the FRET      laboratory no. 4, PAM (PIE Analysis with MATLAB) software package;
efficiency E and donor fluorescence lifetime ⟨τD(A) ⟩F (Fig. 4b and Sup-   laboratory no. 5, PAM (PIE Analysis with MATLAB) software package;
plementary Fig. 11e–h) were created for single-molecule measurements       laboratory no. 6, PAM (PIE Analysis with MATLAB) software package;
using multiparameter fluorescence detection (MFD) in combination           laboratory no. 7, PAM (PIE Analysis with MATLAB) software package;
with PIE35, described below. Static FRET lines were calculated using       laboratory no. 8, PAM (PIE Analysis with MATLAB) software package
the following equation:                                                    v.2.0; laboratory no. 9, PAM (PIE Analysis with MATLAB) software
                                                                           package; laboratory no. 11, data were analyzed with the burst analysis
                                          τD(A)
                              E=1−                                  (11)   toolbox (BAT, V2018 and V2019) and filtered and visualized with T3ee
                                          τD(0)
                                                                           (V2018, V2019) (ref. 84 in Supplementary Information); laboratory
                                                                           no. 12: PAM (PIE Analysis with MATLAB) software package; laboratory
and further modified for linker dynamics 61. Deviations of FRET            no. 13, IgorPro 8 (Wavemetrics); laboratory no. 14, PAM (PIE Analysis
populations from the static FRET line can indicate FRET dynamics,          with MATLAB) software package; laboratory no. 15, Software Package
which can be due to conformational fluctuations or photophysical           for Multiparameter Fluorescence Spectroscopy, Full Correlation and
dynamics. In addition, a time-resolved FRET analysis of TCSPC data can     Multiparameter Fluorescence Imaging developed in C.A.M. Seidel’s
accurately resolve the distance heterogeneities by revealing multiple      laboratory (http://www.mpc.uni-duesseldorf.de/seidel/); laboratory
components in the decay curve and recovering their specific species        no. 16, ALEX-suite software package (ref. 88 of Supplementary Infor-
fractions and FRET rate constants69. Dynamics are thus detected from       mation); laboratory no. 17, FRETBursts analysis software (ref. 14 of
the presence of multiple components in the subensemble decay of a          Supplementary Information) and laboratory no. 18, FRETBursts toolkit
single FRET population. In addition, dynamics that are slower than         (ref. 14 of Supplementary Information).
the fluorescence lifetime (roughly 5 ns) are not averaged in the FRET
lifetime analysis leading to the detection of the full conformational      References
distribution.                                                              88. Gouridis, G. et al. Conformational dynamics in substrate-binding
                                                                               domains influences transport in the ABC importer GlnPQ.
MFD with PIE                                                                   Nat. Struct. Mol. Biol. 22, 57–64 (2015).
MFD, introduced by Eggeling et al.93, combines spectral and polarized      89. Jerabek-Willemsen, M. et al. MicroScale thermophoresis:
detection with picosecond pulsed lasers and TCSPC, allowing the                interaction analysis and beyond. J. Mol. Struct. 1077, 101–113
simultaneous detection of intensity, lifetime, anisotropy and spectral         (2014).
range of the fluorescence signal of single molecules. nsALEX or PIE        90. Hall, J. A., Gehring, K. & Nikaido, H. Two modes of ligand binding
additionally provides the acceptor lifetime information35. Due to the          in maltose-binding protein of Escherichia coli: correlation with the
availability of the lifetime information when using pulsed excitation,         structure of ligands and the structure of binding protein. J. Biol.
this approach is well suited for using E–τ-based analyses.                     Chem. 272, 17605–17609 (1997).
                                                                           91. Kim, E. et al. A single-molecule dissection of ligand binding to
Dye simulations (AV and ACV)                                                   a protein with intrinsic dynamics. Nat. Chem. Biol. 9, 313–318
The AV approach uses a simple coarse-grained dye model64 defined               (2013).
by five parameters: the width and length of the linker, and three          92. Sisamakis, E., Valeri, A., Kalinin, S., Rothwell, P. J. & Seidel, C. A.
radii that define the fluorophore volume (Fig. 5a and Supplemen-               M. Accurate single-molecule FRET studies using multiparameter
tary Table 10). Using these parameters, AV simulations for both fluo-          fluorescence detection. Methods Enzymol. 475, 455–514 (2010).
rophores were calculated by considering the linker flexibility and         93. Eggeling, C. et al. Data registration and selective single-
steric hindrances of the labeled molecule (Fig. 5a). In the ACV                molecule analysis using multi-parameter fluorescence detection.
model63, the position of the dyes is biased toward the protein surface,        J. Biotechnol. 86, 163–180 (2001).
resulting in a reduction of the interdye distance for the given labeling
positions. To do this, the residual anisotropy was used to estimate        Acknowledgements
the fraction of sticking dyes. In the computation of the FRET-             Work in the laboratory of T.C. was financed by a European Research
averaged model distances, the occupancy of a thin surface layer            Council (ERC) Starting grant (no. ERC-StG 638536—SM-IMPORT),
(roughly 3 Å) was then increased such that its fraction matches the        German Research Foundation (Deutsche Forschungsgemeinschaft,
amount of interacting dye detected in the experiment (Fig. 5b and          DFG) within grant nos. GRK2062 (project C03) and SFB863 (project
Supplementary Table 10).                                                   A13) and an Alexander von Humboldt postdoctoral fellowship
                                                                           (to N.Z.). T.C., P.T. and D.C.L. acknowledge the support of the
Reporting summary                                                          Center for integrated protein science Munich and the Center for
Further information on research design is available in the Nature          NanoScience. D.C.L. acknowledges the support of the Nanosystems
Portfolio Reporting Summary linked to this article.                        Initiative Munich and LMUinnovative program BioImaging


Nature Methods


Analysis                                                                                             https://doi.org/10.1038/s41592-023-01807-0

Network. We also acknowledge support via the SFB1035 (DFG,                  5 in silico. M.P. and J.F. performed initial measurements on MalE
Sonderforschungsbereich 1035 project no. 201302640, project no. A11         mutants 4 and 5. G.A. reperformed the analysis on the provided raw
to D.C.L. and project no. B03 to M. Sattler). D.C.L. and P.T. acknowledge   data for U2AF2 and MalE-1 from eight laboratories. G.A., A.B. and M.P.
support by the Federal Ministry of Education and Research (BMBF)            performed ds estimation. C.G. performed FCS experiments on MalE
and the Free State of Bavaria under the Excellence Strategy of the          variants, time-resolved anisotropy experiments and R0-determination.
Federal Government and the Länder through the ONE MUNICH                    M.P. performed time-resolved anisotropy analysis of single labeled
Project Munich Multiscale Biofabrication. C.A.M.S. acknowledges             MalE cysteine mutants from ensemble measurements as well of all
the support by the ERC (grant no. 671208 (hybridFRET)) and by the           MalE and U2AF2 dye combinations from smFRET measurements.
DFG (grant nos. SE 1195/17-1 and CRC 1208 (project no. A08)). A.B.          C.G., G.A. and M.P. performed measurements of MalE mutants with
acknowledges funding from the European Union’s Horizon 2020                 additional dye combinations and M.P. and A.B. performed statistical
research and innovation program under the Marie Skłodowska-Curie            analysis of ds and anisotropies. G.A. and A.B. performed estimation
grant agreement no. 101029907. Research in the contributing authors’        of setup-dependent parameters and PDA of U2AF2. G.A. performed
laboratories was financed by the following sources: P.T. acknowledges       the filtered-FCS and A.B. performed TCSPC analysis of U2AF2.
the support by the Deutsche Forschungsgemeinschaft (DFG, German             C.G., G.A. and M.P. performed smFRET measurements on dsDNA
Research Foundation), project ID 201269156, SFB 1032 (A13) and              rulers. M.P. performed AV and ACV modeling of dye distributions for
project ID 267681426. T.D.C. was supported by the Biotechnology             MalE and U2AF2. G.G.M.M. performed microscale thermophoresis
and Biological Sciences Research Council (BBSRC) (grant no. BB/             experiments. M.d.B. performed confocal scanning experiments for
T008032/1) and Engineering and Physical Sciences Research Council           surface-immobilized MalE. All authors were involved in performing
(EPSRC) (grant no. EP/V034804/1), B.A. was supported by an EPSRC            comparison experiments and analyzing smFRET data. G.A. and C.G.
Prize Fellowship. BMBF grant nos. 03Z2EN11 and 03Z22E511 as well            consolidated data collection of participating laboratories. G.A.
as DFG grant no. SCHL 1896/4-1 (to M. Schlierf). SFB960 project A7          and C.G. designed Fig. 1. G.A., C.G. and M.P. designed Fig. 2. A.B.
(to D.G.) US National Institutes of Health grant no. GM122569 (to T.        designed Figs. 3 and 4. A.B. and M.P. designed Figs. 5 and 6. G.A.,
Ha). J.H. acknowledges the Research Foundation Flanders (FWO)               C.G., M.P., A.B., C.A.M.S., D.C.L. and T.C. interpreted data and wrote the
(project nos. G0B4915, G0B9922N and G0H3716N) and is indebted               manuscript in consultation with all authors.
to Johan Hofkens at KU Leuven for the used smFRET infrastructure.
ERC grant agreement no. 681891 (Prosint) and DFG under Germany’s            Competing interests
Excellence Strategy (CIBSS EXC-2189 project ID 390939984) and the           T.D.C. and A.N.K. are founders of different companies selling
SFB1381 program (project ID 403222702) (to T. Hugel). Royal Society         single-molecule fluorescence microscopes (Exciting Instruments,
Dorothy Hodgkin Research Fellowship DKR00620 and a Research                 Oxford Nanoimager). The other authors declare no competing
Grant for Research Fellows no. RGF\R1\180054 (to N.C.R.), by the            interests.
Wellcome Trust (grant no. 110164/Z/15/Z to A.N.K.). The Israel Science
Foundation (grant nos. 556/22 to E.L., 3565/20 to E.L., within the          Additional information
KillCorona – Curbing Coronavirus Research Program), the National            Extended data is available for this paper at
Institutes of Health (grant no. R01 GM130942 to S.W. and to E.L. as a       https://doi.org/10.1038/s41592-023-01807-0.
subaward), by the Milner Fund (to E.L.) and by the Hebrew University
of Jerusalem (start-up funds to E.L.). Agence Nationale pour la             Supplementary information The online version
Recherche (grant nos. ANR 18-CE11-0004-02, ANR-19-CE44-0009-02,             contains supplementary material available at
ANR-21-CE11-0034-01, ANR-21-CE11-0026-03 and ANR-10-INBS-04,                https://doi.org/10.1038/s41592-023-01807-0.
‘Investments for the future’ to E.M.). E.A.L. acknowledges funding
by the ERC ADG MultiOrganelleDesign and the SFB1551 (project ID             Correspondence and requests for materials should be addressed to
464588647).                                                                 Anders Barth, Claus A. M. Seidel, Don C. Lamb or Thorben Cordes.

Author contributions                                                        Peer review information Nature Methods thanks the anonymous
T.C. initiated the study and D.C.L. coordinated the study. G.A., C.G.,      reviewers for their contribution to the peer review of this work. Primary
A.B., C.A.M.S., D.C.L. and T.C. designed research. A.B., C.A.M.S., D.C.L.   Handling Editor: Rita Strack, in collaboration with the Nature Methods
and T.C. supervised the project. R.M. cloned and purified MalE variants.    team.Peer reviewer reports are available.
H.-S.K. and M.S. provided U2AF2. C.G. and G.A. performed labeling of
MalE and U2AF2 variants, respectively, for shipment to participating        Reprints and permissions information is available at
laboratories. M.P., J.F. and C.A.M.S. designed MalE mutants 4 and           www.nature.com/reprints.


Nature Methods


Analysis                                                                                                                                https://doi.org/10.1038/s41592-023-01807-0


Extended Data Table. 1 | Average of mean FRET efficiency and standard deviation for MalE and U2AF2 samples reported by
the participating laboratories


The calculated average μ⟨E⟩ and standard deviation σ⟨E⟩ of the mean FRET efficiency values provided by the participating labs are given for all three studied mutants of MalE labeled with
Alexa546 and Alexa647 under both apo and holo conditions (see Supplementary Table 3). The calculated mean and standard deviation of the difference in the reported mean FRET efficiency
between the apo and holo ( ⟨Eholo ⟩ − ⟨Eapo ⟩) for the three MalE mutants are given by μ⟨Eholo ⟩−⟨Eapo ⟩ and σ⟨Eholo ⟩−⟨Eapo ⟩ respectively (see Supplementary Table 3). The calculated average μR⟨E⟩ and
standard deviation σR⟨E⟩ of the mean distances were derived according to Eq. 2. The modeled distances RAV
                                                                                                       ⟨E⟩
                                                                                                           and RACV
                                                                                                                ⟨E⟩
                                                                                                                    are derived using accessible volume (AV) and accessible contact volume
(ACV) calculations respectively, as described in the Methods. We also give the average and standard deviation for the FRET values determined for U2AF2 labeled with Atto532-Atto643 under
both apo and holo conditions (Supplementary Table 4). *Only studied by two laboratories. **Due to the fast-structural dynamics in the sample, only 7 labs studied this mutant and distances
were not determined. *** Only the holo state under holo condition was considered.


Nature Methods


                                                                                                                                                               nature research | reporting summary
                                                                                               Corresponding author(s): Barth, Seidel, Lamb, Cordes
                                                                                               Last updated by author(s):  , 2022


Reporting Summary
Nature Research wishes to improve the reproducibility of the work that we publish. This form provides structure for consistency and transparency
in reporting. For further information on Nature Research policies, see our Editorial Policies and the Editorial Policy Checklist.


Statistics
For all statistical analyses, confirm that the following items are present in the figure legend, table legend, main text, or Methods section.
n/a Confirmed
         The exact sample size (n) for each experimental group/condition, given as a discrete number and unit of measurement
         A statement on whether measurements were taken from distinct samples or whether the same sample was measured repeatedly
         The statistical test(s) used AND whether they are one- or two-sideE
         Only common tests should be described solely by name; describe more complex techniques in the Methods section.

         A description of all covariates tested
         A description of any assumptions or corrections, such as tests of normality and adjustment for multiple comparisons
         A full description of the statistical parameters including central tendency (e.g. means) or other basic estimates (e.g. regression coefficient)
         AND variation (e.g. standard deviation) or associated estimates of uncertainty (e.g. confidence intervals)

         For null hypothesis testing, the test statistic (e.g. F, t, r) with confidence intervals, effect sizes, degrees of freedom and P value noted
         Give P values as exact values whenever suitable.

         For Bayesian analysis, information on the choice of priors and Markov chain Monte Carlo settings
         For hierarchical and complex designs, identification of the appropriate level for tests and full reporting of outcomes
         Estimates of effect sizes (e.g. Cohen's d, Pearson's r), indicating how they were calculated
                                          Our web collection on statistics for biologists contains articles on many of the points above.


Software and code
Policy information about availability of computer code
  Data collection    Lab#1: SPCM software (Becker & Hickl GmbH) and HydrHarp400 (PicoQuant)
                     Lab#2: HydrHarp400 (PicoQuant)
                     Lab#3: National Instruments-Card PCI-6602 (National Instruments, USA)
                     Lab#4: SymPhoTime64, (PicoQuant)
                     Lab#5: HydraHarp 400 (PicoQuant)
                     Lab#6: HydraHarp 400 and Symphotime 32 software (PicoQuant).
                     Lab#7: National Instruments card PCIe-6353 with acquisition controlled using custom software (see ref. 64 of Supplementary Information)
                     Lab#8: HydraHarp 400 (PicoQuant)
                     Lab#9: Igor-Program (Wavemetrics) (see ref. 64 of Supplementary Information)
                     Lab#10: LabVIEW software (see ref. 63-71 of Supplementary Information)
                     Lab#11: HydraHarp 400 (PicoQuant)
                     Lab#12: SymPhoTime64 software package (PicoQuant)
                     Lab#13: TimeHarp200 (PicoQuant)
                     Lab#14: SPCM software (Becker & Hickl GmbH)


                                                                                                                                                               April 2020
                     Lab#16: National Instruments-Card PCI-6602 (National Instruments, USA).
                     Lab#17: VistaVision software (version 4.2.095, 64-bit, ISSTM, USA) (see ref. 82 of Supplementary Information)
                     Lab#18: TimeHarp 200 (PicoQuant)

  Data analysis      Lab#1: PAM (PIE Analysis with Matlab) software package (see ref. 7 in the main text)
                     Lab#2: Home-written LabView-based software (see ref.  of Supplementary Information)
                     Lab#3: FRETBursts toolkit (see ref.  of Supplementary Information)
                     Lab#4: PAM (PIE Analysis with Matlab) software package
                     Lab#5: PAM (PIE Analysis with Matlab) software package
                     Lab#6: PAM (PIE Analysis with Matlab) software package



                         Lab#7: PAM (PIE Analysis with Matlab) software package
                         Lab#8: PAM (PIE Analysis with Matlab) software package v2.0


                                                                                                                                                                                         nature research | reporting summary
                         Lab#9: PAM (PIE Analysis with Matlab) software package
                         Lab#11:     !" (see ref.  of Supplementary Information)
                         Lab#12: PAM (PIE Analysis with Matlab) software package
                         Lab#13: IgorPro 8 (Wavemetrics, Portland OR, USA).
                         Lab#14: PAM (PIE Analysis with Matlab) software package
                         Lab#15: Software Package for Multiparameter Fluorescence Spectroscopy, Full Correlation and Multiparameter Fluorescence Imaging
                         developed in C.A.M. Seidel’s lab (http:// www.mpc.uni-duesseldorf.de/seidel/).
                         Lab#16: ALEX-suite software package (see ref.  of Supplementary Information)
                         Lab#17: FRET Bursts analysis software (see ref.  of Supplementary Information)
                         Lab#18: FRETBursts toolkit (see ref.  of Supplementary Information)
For manuscripts utilizing custom algorithms or software that are central to the research but not yet described in published literature, software must be made available to editors and
reviewers. We strongly encourage code deposition in a community repository (e.g. GitHub). See the Nature Research guidelines for submitting code & software for further information.


Data
Policy information about availability of data
 All manuscripts must include a data availability statement. This statement should provide the following information, where applicable:
    - Accession codes, unique identifiers, or web links for publicly available datasets
    - A list of figures that have associated raw data
    - A description of any restrictions on data availability

The data for all figures, all supplementary figures, the raw data for all MalE measurements (with the exception of one mutant from one laboratory) and the raw data
for all U2AF2 measurements have been uploaded to Zenodo (https://doi.org/10.5281/zenodo.).$ %*+;   <=>$!?@!JK!JK


Field-specific reporting
Please select the one below that is the best fit for your research. If you are not sure, read the appropriate sections before making your selection.
    Life sciences                        Behavioural & social sciences                  Ecological, evolutionary & environmental sciences
For a reference copy of the document with all sections, see nature.com/documents/nr-reporting-summary-flat.pdf


Life sciences study design
All studies must disclose on these points even when the disclosure is negative.
  Sample size            19 Laboratories. These are the groups that responded to the invitation to participate in the study.

  Data exclusions        Data from three labs were excluded due to excessive photobleaching during the measurement,inappropriate experimental setup for
                         the provided fluorophore! or difficulties with data collection (see notes on TableS1 for more details)

  Replication            Yeplication [; + \ \ ]\;^++ ; ;]  .Y;[ \+ _

  Randomization          Y\`;; [^+^  [; ;]+ ^\\;_

  Blinding               This was a blind study where the individual groups (with the exception of those providing the proteins) were not informed regarding
                         whaprotein sample they were measuring.{  ; were informed regarding the appropriate conditions for the different samples.


Behavioural & social sciences study design
All studies must disclose on these points even when the disclosure is negative.
  Study description                Briefly describe the study type including whether data are quantitative, qualitative, or mixed-methods (e.g. qualitative cross-sectional,
                                   quantitative experimental, mixed-methods case study).

  Research sample                  State the research sample (e.g. Harvard university undergraduates, villagers in rural India) and provide relevant demographic
                                   information (e.g. age, sex) and indicate whether the sample is representative. Provide a rationale for the study sample chosen. For

                                                                                                                                                                                         April 2020
                                   studies involving existing datasets, please describe the dataset and source.

  Sampling strategy                Describe the sampling procedure (e.g. random, snowball, stratified, convenience). Describe the statistical methods that were used to
                                   predetermine sample size OR if no sample-size calculation was performed, describe how sample sizes were chosen and provide a
                                   rationale for why these sample sizes are sufficient. For qualitative data, please indicate whether data saturation was considered, and
                                   what criteria were used to decide that no further sampling was needed.

  Data collection                  Provide details about the data collection procedure, including the instruments or devices used to record the data (e.g. pen and paper,



  Data collection               computer, eye tracker, video or audio equipment) whether anyone was present besides the participant(s) and the researcher, and
                                whether the researcher was blind to experimental condition and/or the study hypothesis during data collection.


                                                                                                                                                                            nature research | reporting summary
  Timing                        Indicate the start and stop dates of data collection. If there is a gap between collection periods, state the dates for each sample
                                cohort.

  Data exclusions               If no data were excluded from the analyses, state so OR if data were excluded, provide the exact number of exclusions and the
                                rationale behind them, indicating whether exclusion criteria were pre-established.

  Non-participation             State how many participants dropped out/declined participation and the reason(s) given OR provide response rate OR state that no
                                participants dropped out/declined participation.

  Randomization                 If participants were not allocated into experimental groups, state so OR describe how participants were allocated to groups, and if
                                allocation was not random, describe how covariates were controlled.


Ecological, evolutionary & environmental sciences study design
All studies must disclose on these points even when the disclosure is negative.
  Study description             Briefly describe the study. For quantitative data include treatment factors and interactions, design structure (e.g. factorial, nested,
                                hierarchical), nature and number of experimental units and replicates.

  Research sample               Describe the research sample (e.g. a group of tagged Passer domesticus, all Stenocereus thurberi within Organ Pipe Cactus National
                                Monument), and provide a rationale for the sample choice. When relevant, describe the organism taxa, source, sex, age range and
                                any manipulations. State what population the sample is meant to represent when applicable. For studies involving existing datasets,
                                describe the data and its source.

  Sampling strategy             Note the sampling procedure. Describe the statistical methods that were used to predetermine sample size OR if no sample-size
                                calculation was performed, describe how sample sizes were chosen and provide a rationale for why these sample sizes are sufficient.

  Data collection               Describe the data collection procedure, including who recorded the data and how.

  Timing and spatial scale Indicate the start and stop dates of data collection, noting the frequency and periodicity of sampling and providing a rationale for
                                these choices. If there is a gap between collection periods, state the dates for each sample cohort. Specify the spatial scale from which
                                the data are taken

  Data exclusions               If no data were excluded from the analyses, state so OR if data were excluded, describe the exclusions and the rationale behind them,
                                indicating whether exclusion criteria were pre-established.

  Reproducibility               Describe the measures taken to verify the reproducibility of experimental findings. For each experiment, note whether any attempts to
                                repeat the experiment failed OR state that all attempts to repeat the experiment were successful.

  Randomization                 Describe how samples/organisms/participants were allocated into groups. If allocation was not random, describe how covariates were
                                controlled. If this is not relevant to your study, explain why.

  Blinding                      Describe the extent of blinding used during data acquisition and analysis. If blinding was not possible, describe why OR explain why
                                blinding was not relevant to your study.

  Did the study involve field work?             Yes           No


Field work, collection and transport
  Field conditions              Describe the study conditions for field work, providing relevant parameters (e.g. temperature, rainfall).

  Location                      State the location of the sampling or experiment, providing relevant parameters (e.g. latitude and longitude, elevation, water depth).

  Access & import/export Describe the efforts you have made to access habitats and to collect and import/export your samples in a responsible manner and in
                                compliance with local, national and international laws, noting any permits that were obtained (give the name of the issuing authority,
                                the date of issue, and any identifying information).

  Disturbance                   Describe any disturbance caused by the study and how it was minimized.


                                                                                                                                                                            April 2020
Reporting for specific materials, systems and methods
We require information from authors about some types of materials, experimental systems and methods used in many studies. Here, indicate whether each material,
system or method listed is relevant to your study. If you are not sure if a list item applies to your research, read the appropriate section before selecting a response.



Materials & experimental systems                                Methods


                                                                                                                                                                           nature research | reporting summary
n/a Involved in the study                                       n/a Involved in the study
          Antibodies                                                      ChIP-seq
          Eukaryotic cell lines                                           Flow cytometry
          Palaeontology and archaeology                                   MRI-based neuroimaging
          Animals and other organisms
          Human research participants
          Clinical data
          Dual use research of concern


Antibodies
  Antibodies used                 Describe all antibodies used in the study; as applicable, provide supplier name, catalog number, clone name, and lot number.

  Validation                      Describe the validation of each primary antibody for the species and application, noting any validation statements on the
                                  manufacturer’s website, relevant citations, antibody profiles in online databases, or data provided in the manuscript.


Eukaryotic cell lines
Policy information about cell lines
  Cell line source(s)                     State the source of each cell line used.

  Authentication                          Describe the authentication procedures for each cell line used OR declare that none of the cell lines used were authenticated.

  Mycoplasma contamination                Confirm that all cell lines tested negative for mycoplasma contamination OR describe the results of the testing for
                                          mycoplasma contamination OR declare that the cell lines were not tested for mycoplasma contamination.

  Commonly misidentified lines            Name any commonly misidentified cell lines used in the study and provide a rationale for their use.
  (See ICLAC register)


Palaeontology and Archaeology
  Specimen provenance             Provide provenance information for specimens and describe permits that were obtained for the work (including the name of the
                                  issuing authority, the date of issue, and any identifying information).

  Specimen deposition             Indicate where the specimens have been deposited to permit free access by other researchers.

  Dating methods                  If new dates are provided, describe how they were obtained (e.g. collection, storage, sample pretreatment and measurement), where
                                  they were obtained (i.e. lab name), the calibration program and the protocol for quality assurance OR state that no new dates are
                                  provided.

      Tick this box to confirm that the raw and calibrated dates are available in the paper or in Supplementary Information.

  Ethics oversight                Identify the organization(s) that approved or provided guidance on the study protocol, OR state that no ethical approval or guidance
                                  was required and explain why not.
Note that full information on the approval of the study protocol must also be provided in the manuscript.


Animals and other organisms
Policy information about studies involving animals; ARRIVE guidelines recommended for reporting animal research
  Laboratory animals              For laboratory animals, report species, strain, sex and age OR state that the study did not involve laboratory animals.

  Wild animals                    Provide details on animals observed in or captured in the field; report species, sex and age where possible. Describe how animals were
                                  caught and transported and what happened to captive animals after the study (if killed, explain why and describe method; if released,
                                  say where and when) OR state that the study did not involve wild animals.


                                                                                                                                                                           April 2020
  Field-collected samples         For laboratory work with field-collected samples, describe all relevant parameters such as housing, maintenance, temperature,
                                  photoperiod and end-of-experiment protocol OR state that the study did not involve samples collected from the field.

  Ethics oversight                Identify the organization(s) that approved or provided guidance on the study protocol, OR state that no ethical approval or guidance
                                  was required and explain why not.
Note that full information on the approval of the study protocol must also be provided in the manuscript.



Human research participants


                                                                                                                                                                        nature research | reporting summary
Policy information about studies involving human research participants
  Population characteristics            Describe the covariate-relevant population characteristics of the human research participants (e.g. age, gender, genotypic
                                        information, past and current diagnosis and treatment categories). If you filled out the behavioural & social sciences study
                                        design questions and have nothing to add here, write "See above."

  Recruitment                           Describe how participants were recruited. Outline any potential self-selection bias or other biases that may be present and
                                        how these are likely to impact results.

  Ethics oversight                      Identify the organization(s) that approved the study protocol.

Note that full information on the approval of the study protocol must also be provided in the manuscript.


Clinical data
Policy information about clinical studies
All manuscripts should comply with the ICMJE guidelines for publication of clinical research and a completed CONSORT checklist must be included with all submissions.

  Clinical trial registration Provide the trial registration number from ClinicalTrials.gov or an equivalent agency.

  Study protocol               Note where the full trial protocol can be accessed OR if not available, explain why.

  Data collection              Describe the settings and locales of data collection, noting the time periods of recruitment and data collection.

  Outcomes                     Describe how you pre-defined primary and secondary outcome measures and how you assessed these measures.


Dual use research of concern
Policy information about dual use research of concern

Hazards
  Could the accidental, deliberate or reckless misuse of agents or technologies generated in the work, or the application of information presented
  in the manuscript, pose a threat to:
  No Yes
           Public health
           National security
           Crops and/or livestock
           Ecosystems
           Any other significant area


Experiments of concern
  Does the work involve any of these experiments of concern:
  No Yes
           Demonstrate how to render a vaccine ineffective
           Confer resistance to therapeutically useful antibiotics or antiviral agents
           Enhance the virulence of a pathogen or render a nonpathogen virulent
           Increase transmissibility of a pathogen
           Alter the host range of a pathogen
           Enable evasion of diagnostic/detection modalities
           Enable the weaponization of a biological agent or toxin
           Any other potentially harmful combination of experiments and agents

                                                                                                                                                                        April 2020
ChIP-seq
Data deposition
      Confirm that both raw and final processed data have been deposited in a public database such as GEO.
      Confirm that you have deposited or provided access to graph files (e.g. BED files) for the called peaks.



 Data access links                        For "Initial submission" or "Revised version" documents, provide reviewer access links. For your "Final submission" document,


                                                                                                                                                                             nature research | reporting summary
 May remain private before publication.   provide a link to the deposited data.

 Files in database submission             Provide a list of all files available in the database submission.

 Genome browser session                   Provide a link to an anonymized genome browser session for "Initial submission" and "Revised version" documents only, to
 (e.g. UCSC)                              enable peer review. Write "no longer applicable" for "Final submission" documents.


Methodology
 Replicates                      Describe the experimental replicates, specifying number, type and replicate agreement.

 Sequencing depth                Describe the sequencing depth for each experiment, providing the total number of reads, uniquely mapped reads, length of reads and
                                 whether they were paired- or single-end.

 Antibodies                      Describe the antibodies used for the ChIP-seq experiments; as applicable, provide supplier name, catalog number, clone name, and lot
                                 number.

 Peak calling parameters Specify the command line program and parameters used for read mapping and peak calling, including the ChIP, control and index files
                                 used.

 Data quality                    Describe the methods used to ensure data quality in full detail, including how many peaks are at FDR 5% and above 5-fold enrichment.

 Software                        Describe the software used to collect and analyze the ChIP-seq data. For custom code that has been deposited into a community
                                 repository, provide accession details.


Flow Cytometry
Plots
 Confirm that:
     The axis labels state the marker and fluorochrome used (e.g. CD4-FITC).
     The axis scales are clearly visible. Include numbers along axes only for bottom left plot of group (a 'group' is an analysis of identical markers).
     All plots are contour plots with outliers or pseudocolor plots.
     A numerical value for number of cells or percentage (with statistics) is provided.

Methodology
 Sample preparation                       Describe the sample preparation, detailing the biological source of the cells and any tissue processing steps used.

 Instrument                               Identify the instrument used for data collection, specifying make and model number.

 Software                                 Describe the software used to collect and analyze the flow cytometry data. For custom code that has been deposited into a
                                          community repository, provide accession details.

 Cell population abundance                Describe the abundance of the relevant cell populations within post-sort fractions, providing details on the purity of the
                                          samples and how it was determined.

 Gating strategy                          Describe the gating strategy used for all relevant experiments, specifying the preliminary FSC/SSC gates of the starting cell
                                          population, indicating where boundaries between "positive" and "negative" staining cell populations are defined.

     Tick this box to confirm that a figure exemplifying the gating strategy is provided in the Supplementary Information.


Magnetic resonance imaging
Experimental design
 Design type                                   Indicate task or resting state; event-related or block design.


                                                                                                                                                                             April 2020
 Design specifications                         Specify the number of blocks, trials or experimental units per session and/or subject, and specify the length of each trial
                                               or block (if trials are blocked) and interval between trials.

 Behavioral performance measures               State number and/or type of variables recorded (e.g. correct button press, response time) and what statistics were used
                                               to establish that the subjects were performing the task as expected (e.g. mean, range, and/or standard deviation across
                                               subjects).



Acquisition


                                                                                                                                                                              nature research | reporting summary
 Imaging type(s)                            Specify: functional, structural, diffusion, perfusion.

 Field strength                             Specify in Tesla

 Sequence & imaging parameters              Specify the pulse sequence type (gradient echo, spin echo, etc.), imaging type (EPI, spiral, etc.), field of view, matrix size,
                                            slice thickness, orientation and TE/TR/flip angle.

 Area of acquisition                        State whether a whole brain scan was used OR define the area of acquisition, describing how the region was determined.

 Diffusion MRI               Used               Not used

Preprocessing
 Preprocessing software               Provide detail on software version and revision number and on specific parameters (model/functions, brain extraction,
                                      segmentation, smoothing kernel size, etc.).

 Normalization                        If data were normalized/standardized, describe the approach(es): specify linear or non-linear and define image types used for
                                      transformation OR indicate that data were not normalized and explain rationale for lack of normalization.

 Normalization template               Describe the template used for normalization/transformation, specifying subject space or group standardized space (e.g.
                                      original Talairach, MNI305, ICBM152) OR indicate that the data were not normalized.

 Noise and artifact removal           Describe your procedure(s) for artifact and structured noise removal, specifying motion parameters, tissue signals and
                                      physiological signals (heart rate, respiration).

 Volume censoring                     Define your software and/or method and criteria for volume censoring, and state the extent of such censoring.


Statistical modeling & inference
 Model type and settings              Specify type (mass univariate, multivariate, RSA, predictive, etc.) and describe essential details of the model at the first and
                                      second levels (e.g. fixed, random or mixed effects; drift or auto-correlation).

 Effect(s) tested                     Define precise effect in terms of the task or stimulus conditions instead of psychological concepts and indicate whether
                                      ANOVA or factorial designs were used.

 Specify type of analysis:         Whole brain              ROI-based              Both
 Statistic type for inference         Specify voxel-wise or cluster-wise and report all relevant parameters for cluster-wise methods.
 (See Eklund et al. 2016)

 Correction                           Describe the type of correction and how it is obtained for multiple comparisons (e.g. FWE, FDR, permutation or Monte Carlo).


Models & analysis
 n/a Involved in the study
           Functional and/or effective connectivity
           Graph analysis
           Multivariate modeling or predictive analysis

 Functional and/or effective connectivity                 Report the measures of dependence used and the model details (e.g. Pearson correlation, partial correlation,
                                                          mutual information).

 Graph analysis                                           Report the dependent variable and connectivity measure, specifying weighted graph or binarized graph,
                                                          subject- or group-level, and the global and/or node summaries used (e.g. clustering coefficient, efficiency,
                                                          etc.).

 Multivariate modeling and predictive analysis Specify independent variables, features extraction and dimension reduction, model, training and evaluation
                                                          metrics.


                                                                                                                                                                              April 2020
