# How Robust Are Protein Folding Simulations with Respect to Force Field Parameterization?

**Authors:** Stefano Piana, Kresten Lindorff-Larsen, David E. Shaw
**Year:** 2011
**Venue:** Biophysical Journal
**DOI:** 10.1016/j.bpj.2011.03.051
**Source PDF URL:** https://europepmc.org/articles/PMC3149239?pdf=render
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

# How Robust Are Protein Folding Simulations with Respect to Force Field 

# Parameterization? 

## Stefano Piana,†^6 Kresten Lindorff-Larsen,†^6 and David E. Shaw†‡* 

†D.E.ShawResearch,NewYork,NewYork;and‡CenterforComputationalBiologyandBioinformatics,ColumbiaUniversity,NewYork,NewYork 

### ABSTRACT Molecular dynamics simulations hold the promise of providing an atomic-level description of protein folding that 

### cannot easily be obtained from experiments. Here, we examine the extent to which the molecular mechanics force field used in 

### such simulations might influence the observed folding pathways. To that end, we performed equilibrium simulations of a fast

### folding variant of the villin headpiece using four different force fields. In each simulation, we observed a large number of tran

### sitions between the unfolded and folded states, and in all four cases, both the rate of folding and the structure of the native state 

### were in good agreement with experiments. We found, however, that the folding mechanism and the properties of the unfolded 

### state depend substantially on the choice of force field. We thus conclude that although it is important to match a single, 

### experimentally determined structure and folding rate, this does not ensure that a given simulation will provide a unique and 

### correct description of the full free-energy surface and the mechanism of folding. 

## Received for publication 5 January 2011 and in final form 28 March 2011. 

(^6) Stefano Piana and Kresten Lindorff-Larsen contributed equally to this work. 

### *Correspondence: David.Shaw@DEShawResearch.com 

## By exploiting recent advances in computing hardware, algo

## rithms, software, simulation techniques, and force fields (1), 

## a number of studies have demonstrated that it is now 

## possible to fold proteins to their native states using molec

## ular dynamics (MD) simulations with physics-based force 

## fields and an explicit representation of water molecules 

## (2–8). Such studies are important steps toward the goal of 

## using MD simulations to provide complete, atomistic 

## descriptions of protein folding pathways. There are, 

## however, indications in the literature that the observed 

## pathway leading to the folded state in a simulation may 

## depend on the molecular mechanics force field used 

## (7,9,10). Given that one of the primary goals of such simu

## lations is to obtain atomic-level insight into the folding 

## process, such force field dependencies raise questions as 

## to the utility of MD simulations for studying protein folding. 

## Whenever possible, simulation results should be validated 

## through comparisons with experiments. In addition to 

## comparisons with an experimentally derived native structure, 

## in favorable cases it may also be possible to calculate the 

## folding rate from simulations, and to compare the resulting 

## value with experiments (5,7,10,11). Additional comparisons, 

## beyond those obtained with a single structure and folding 

## rate, are often hampered by a lack of experimental data or 

## by the intrinsic difficulty of calculating experimental observ

## ables from simulations. Indeed, even in the case of folding

## rate comparisons, there has been some debate as to whether 

## the spectroscopic signals used in experiments actually do 

## provide accurate measurements of folding rates (3,5). 

## Given that folding simulations are often validated only by 

## matching a single structure, and sometimes a folding rate, 

## we decided to examine the extent to which the folding path

## ways might vary in a set of MD simulations that accurately 

## reproduce these two properties. In particular, we chose to 

## examine four different force fields in the Amber and 

## CHARMM families: Amber ff03 (13), Amber ff99SB*

## ILDN (2,14,15), CHARMM22 (16) with the CMAP back

## bone correction (17) (herein termed CHARMM27), and 

## CHARMM22 (16) with newly modified backbone torsion 

## potentials (herein termed CHARMM22*; see the Support

## ing Material for additional details). All of these force fields 

## are able to predict both the correct native state and the 

## folding rate of a small helical protein, the villin headpiece 

## C-terminal fragment (12). In each case, we performed the 

## simulation at a temperature at which the folded state is 

## ~30% populated. We used a special-purpose machine for 

## MD simulations called Anton (7,18), and the simulations 

## were 100, 300, 100, and 117 ms long for ff03, ff99SB*

## ILDN, CHARMM27 and CHARMM22*, respectively (see 

## Supporting Material for a description of methods). 

## In each simulation, the protein reversibly folded and 

## unfolded more than 50 times (Fig. 1), which allowed us 

## not only to obtain accurate estimates of the folding rate 

## but also to examine enough folding and unfolding transi

## tions to characterize in detail the mechanism of folding. 

## The native structure was calculated as the center of the 

## most populated cluster obtained by clustering (19) with a 

## root-mean-square deviation (RMSD) cutoff of 1.0 A ̊. The 

## calculated Ca-RMSDs (excluding the first two and last 

 Editor: Kathleen B. Hall. Ó2011 by the Biophysical Society doi: 10.1016/j.bpj.2011.03.051 

Biophysical Journal Volume 100 May 2011 L47–L49 L47 

## two residues) from the experimentally determined structure 

## (12) were 1.3 A ̊ , 0.7 A ̊ , 0.6 A ̊ , and 0.7 A ̊ for ff03, ff99SB*

## ILDN, CHARMM27, and CHARMM22*, respectively, thus 

## demonstrating that all four force fields provide an accurate 

## structural description of the native state of villin. We 

## computed the folding rate using a dual-cutoff approach to 

## define the folded and unfolded states. Rates obtained in 

## this way are relatively insensitive to the criteria used to 

## define folding and unfolding, and are consistent with 

## model-free calculations of relaxation times (an observation 

## that also supports the use of fluorescence as a spectroscopic 

## signal to monitor villin folding; see Fig. S2 and Fig. S3). 

## The calculated folding times (Table 1) are all in good agree

## ment with the experimental value of ~1 ms and the relatively 

## modest temperature dependency of the folding rate (12). We 

## conclude that, from a structural and kinetic standpoint, all of 

## the force fields considered here produce a satisfactory 

## picture of villin folding. 

## Some differences were observed at the level of the folding 

## thermodynamics. Indeed, we had to select different temper

## atures to achieve the same thermodynamic stability, with the 

## more helical force fields, ff03 and CHARMM27 (20), 

## having higher thermal stabilities than in experiments (Table 

## 1). Folding enthalpies were calculated as the difference 

## between the average force field energies of the folded and 

## unfolded states (Table 1). The calculated values for three 

## of the force fields (ff99SB*-ILDN, CHARMM22*, and 

## CHARMM27) are in reasonable agreement with the exper

## imental value of ~25 kcal mol1 (12,21), while the value for 

## ff03 is less than half of the experimental value. 

## We now turn our attention to the folding free-energy 

## surface and the folding mechanism, which are the most valu

## able pieces of information provided by the simulations. We 

## first calculated the fraction of time in which the residues 

## that were in helices 1–3 in the native state were also helical 

## in the unfolded state (22) ( Table 1). The results show that 

## the intrinsic stability of the individual secondary structure 

## motifs, which ultimately depends on the underlying folding 

## free-energy landscapes, may be strongly force field–depen

## dent. These differences in helix stabilities also influence 

## the preferential folding pathway, particularly when the 

## Amber and CHARMM force fields are compared. In Fig. 2, 

## we show the relativeflux through various pathways that differ 

## in the order in which the individual helices form. In ff03 and 

## ff99SB*-ILDN, where helix 1 is relatively unstable in the 

## unfolded state, helices 3 and 2 form early during the folding 

## process and helix 1 is nearly always the last to form (Fig. 2). 

## This is not the case in the simulations performed with 

## CHARMM27 and CHARMM22*, where we observe a 

## substantial fraction of folding events with helix 1 formed first 

## or second. The pathways observed in the CHARMM simula

## tions are more consistent with predictions based on an 

## Ising-like model that quantitatively reproduces the equilib

## rium and kinetic properties of wild-type villin (23). The 

## CHARMM22* force field gives rise to the most heteroge

## neous folding mechanism, at least when quantified by the 

## order of helix formation, as we observe non-negligible 

## (>10%) flux through four out of the six possible pathways. 

## This may reflect the smaller differences in stabilities between 

## helices 1 and 3 in CHARMM22*. We note that in the 

## CHARMM27 simulation, two of the helices are essentially 

## fully formed even in the unfolded state (Table 1), and folding 

## mostlyinvolves rearrangingthe loops that connect the helices 

## in such a way as to achieve proper helix orientation, in a 

## manner reminiscent of the diffusion-collision model for 

## folding. In this case, other metrics beyond the formation of 

## individual secondary structure motifs may also prove useful 

## to further characterize the folding mechanism. 

## In summary, the four different force fields investigated 

## here, including a new ‘‘helix-coil-balanced’’ variant of the 

## CHARMM force field (CHARMM22*), were all able to 

## reproduce the experimental native-state structure and 

## folding rate of the villin headpiece C-terminal domain. 

## For ff99SB*-ILDN and CHARMM22*, the melting temper

## ature and folding enthalpy are also in reasonable agreement 

 100Time ( μs) 

#### RMSD (Å) 

 2 040 600 8 0 

FIGURE 1 Reversible folding simulation of the villin headpiece. The Ca-RMSD (excluding the first two and last two residues) with respect to the PDB structure 2F4K is shown for the first 100 ms of a simulation performed with the CHARMM22* force field. Corresponding plots for the ff03, ff99SB*-ILDN, and CHARMM27 force fields are shown in Fig. S1. 

TABLE 1 Kinetic and thermodynamic properties of the villin headpiece 

 T (K) DGf (kcal mol1) DHf (kcal mol1) Folding time (ms) % of helix 1/2/3 

ff03 390 0.21 5 0.1 9.7 51 0.8 5 0.1 30/52/85 ff99SB*-ILDN 380 0.70 5 0.1 19.7 51 3.0 5 0.4 22/17/59 CHARMM27 430 0.51 5 0.1 19.3 5 0.4 0.9 5 0.1 73/33/90 CHARMM22* 360 1.0 5 0.2 17.0 51 2.6 5 0.5 41/9/44 Experiments 370 0.8 25 0.7 Not determined 

Table 1 shows the simulation temperature (T), folding free energy (DGf), folding enthalpy (DHf), average folding time, and fraction of residues that are helical in the unfolded state. Experimental values were taken from Kubelka et al. (12). 

Biophysical Journal 100(9) L47–L49 

L48 Biophysical Letters 

## with experiments. The four force fields differ in their free

## energy surfaces, with CHARMM27 and, to a lesser extent, 

## ff03 favoring a helical unfolded state and a diffusion-colli

## sion-type folding mechanism in which individual helices 

## are rather stable in isolation and dock together to form the 

## folded state. In the two force fields with a more accurate 

## helix-coil balance (ff99SB*-ILDN and CHARMM22*), 

## helix formation and the accretion of tertiary structure appear 

## to be more cooperative. These observations are reminiscent 

## of the experimental finding that, in the case of homeo

## domains, differences in unfolded-state helicity may 

## cause a shift from a nucleation-condensation mechanism 

## to a diffusion-collision mechanism (24). 

## We conclude that caution should be exercised when pre

## dicting folding mechanisms from computer simulations 

## unless a comparison can be performed with experimental 

## data, beyond reproducing the structure and folding rate of 

## just a single protein. Recent simulation results suggest that 

## it is becoming possible to fold proteins with both a-helical 

## and b-sheet structure using a single force field (4,6,7). We 

## expect that such transferable force fields will be better 

## able to accurately reproduce the subtle details of the folding 

## mechanisms of proteins. 

## SUPPORTING MATERIAL 

Additional text, four figures, three tables, and references are available at [http://www.biophysj.org/biophysj/supplemental/S0006-3495(11)00409-7.](http://www.biophysj.org/biophysj/supplemental/S0006-3495(11)00409-7.) 

## ACKNOWLEDGMENTS 

We thank R. O. Dror for several helpful suggestions. This research was conducted at D. E. Shaw Research LLC, of which D.E.S. is the sole beneficial owner and serves as Chief Scientist. 

## REFERENCES and FOOTNOTES 

1. Klepeis, J. L., K. Lindorff-Larsen, ., D. E. Shaw. 2009. Long-time-     scale molecular dynamics simulations of protein structure and function.     Curr. Opin. Struct. Biol. 19:120–127. 

2. Hornak, V., R. Abel, ., C. Simmerling. 2006. Comparison of multiple     Amber force fields and development of improved protein backbone     parameters. Proteins. 65:712–725. 

3. Ensign, D. L., P. M. Kasson, and V. S. Pande. 2007. Heterogeneity even     at the speed limit of folding: large-scale molecular dynamics study of     a fast-folding variant of the villin headpiece. J. Mol. Biol. 374:806–816. 

4. Piana, S., A. Laio, ., J. C. Martins. 2008. Predicting the effect of     a point mutation on a protein fold: the villin and advillin headpieces     and their Pro62Ala mutants. J. Mol. Biol. 375:460–470. 

5. Freddolino, P. L., and K. Schulten. 2009. Common structural transi-     tions in explicit-solvent simulations of villin headpiece folding.     Biophys. J. 97:2338–2347. 

6. Mittal, J., and R. B. Best. 2010. Tackling force-field bias in protein     folding simulations: folding of Villin HP35 and Pin WW domains in     explicit water. Biophys. J. 99:L26–L28. 

7. Shaw, D. E., P. Maragakis, ., W. Wriggers. 2010. Atomic-level charac-     terization of the structural dynamics of proteins. Science. 330:341–346. 

8. Piana, S., K. Sarkar, ., D. E. Shaw. 2011. Computational design and     experimental testing of the fastest-folding b-sheet protein. J. Mol. Biol.     405:43–48. 

9. Noe ́, F., C. Schu ̈tte, ., T. R. Weikl. 2009. Constructing the equilibrium     ensemble of folding pathways from short off-equilibrium simulations.     Proc. Natl. Acad. Sci. USA. 106:19011–19016. 

10. Ensign, D. L., and V. S. Pande. 2009. The Fip35 WW domain folds     with structural and mechanistic heterogeneity in molecular dynamics     simulations. Biophys. J. 96:L53–L55. 

11. Snow, C. D., H. Nguyen, ., M. Gruebele. 2002. Absolute comparison     of simulated and experimental protein-folding dynamics. Nature.     420:102–106. 

12. Kubelka, J., T. K. Chiu, ., J. Hofrichter. 2006. Sub-microsecond     protein folding. J. Mol. Biol. 359:546–553. 

13. Duan, Y., C. Wu, ., P. Kollman. 2003. A point-charge force field for     molecular mechanics simulations of proteins based on condensed-phase     quantum mechanical calculations. J. Comput. Chem. 24:1999–2012. 

14. Best, R. B., and G. Hummer. 2009. Optimized molecular dynamics     force fields applied to the helix-coil transition of polypeptides.     J. Phys. Chem. B. 113:9004–9015. 

15. Lindorff-Larsen, K., S. Piana, ., D. E. Shaw. 2010. Improved side-     chain torsion potentials for the Amber ff99SB protein force field.     Proteins. 78:1950–1958. 

16. MacKerell, Jr., A. D., D. Bashford, ., M. Karplus. 1998. All-atom     empirical potential for molecular modeling and dynamics studies of     proteins. J. Phys. Chem. B. 102:3586–3616. 

17. Mackerell, Jr., A. D., M. Feig, and C. L. Brooks, 3rd. 2004. Extending     the treatment of backbone energetics in protein force fields: limitations     of gas-phase quantum mechanics in reproducing protein conforma-     tional distributions in molecular dynamics simulations. J. Comput.     Chem. 25:1400–1415. 

18. Shaw, D. E., R. O. Dror, ., B. Towles. 2009. Millisecond-scale molec-     ular dynamics simulations on Anton. In Proceedings of the ACM/IEEE     Conference on High Performance Computing, Networking, Storage     and Analysis (SC09).. ACM Press, New York. 

19. Daura, X., K. Gademann, ., A. E. Mark. 1999. Peptide folding: when     simulation meets experiment. Angew. Chem. Int. Ed. 38:236–240. 

20. Best, R. B., N. V. Buchete, and G. Hummer. 2008. Are current molec-     ular dynamics force fields too helical? Biophys. J. 95:L07–L09. 

21. Godoy-Ruiz, R., E. R. Henry, ., W. A. Eaton. 2008. Estimating free-     energy barrier heights for an ultrafast folding protein from calorimetric     and kinetic data. J. Phys. Chem. B. 112:5938–5949. 

22. Frishman, D., and P. Argos. 1995. Knowledge-based protein secondary     structure assignment. Proteins. 23:566–579. 

23. Kubelka, J., E. R. Henry, ., W. A. Eaton. 2008. Chemical, physical,     and theoretical kinetics of an ultrafast folding protein. Proc. Natl.     Acad. Sci. USA. 105:18655–18662. 

24. Gianni, S., N. R. Guydosh, ., A. R. Fersht. 2003. Unifying features in     protein-foldingmechanisms. Proc. Natl. Acad. Sci. USA. 100:13286–13291. 

 123 132 213 231 312 321 Order of helix formation 

 0.1 

 0.2 

 0.3 

 0.4 

 0.5 

 0.6 

 Probability 

 ff99SB*-ILDN ff03 CHARMM22* CHARMM27 

FIGURE 2 Order of helix formation during villin folding. The order of helix formation was calculated for each folding and unfolding transition. Unfolding events were analyzed in reverse, and thus the order reported here corresponds to a folding transition. In this analysis we assign each transition a three-number code; for example, the designation 123 means that helix 1 forms first, helix 2 second, and helix 3 last. 

 Biophysical Journal 100(9) L47–L49 

Biophysical Letters L49 

