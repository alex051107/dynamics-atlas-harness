# Group F: Ensemble comparison, force fields, integrative modelling

6 papers.



---

# Determination of Ensemble-Average Pairwise Root Mean-Square Deviation from Experimental B-Factors

**Authors:** Antonija Kuzmanic, Bojan Zagrovic
**Year:** 2010
**Venue:** Biophysical Journal
**DOI:** 10.1016/j.bpj.2009.11.011
**Source PDF URL:** https://europepmc.org/articles/PMC2830444?pdf=render
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

# Determination of Ensemble-Average Pairwise Root Mean-Square 

# Deviation from Experimental B-Factors 

Antonija Kuzmanic† and Bojan Zagrovic‡*†Laboratory of Computational Biophysics, Mediterranean Institute for Life Sciences, Split, Croatia; and ‡Department of Physics, Faculty ofScience, University of Split, Split, Croatia 

ABSTRACT Root mean-square deviation (RMSD) after roto-translational least-squares fitting is a measure of global structural similarity of macromolecules used commonly. On the other hand, experimental x-ray B-factors are used frequently to study local structural heterogeneity and dynamics in macromolecules by providing direct information about root mean-square fluctuations (RMSF) that can also be calculated from molecular dynamics simulations. We provide a mathematical derivation showing that, given a set of conservative assumptions, a root mean-square ensemble-average of an all-against-all distribution of pairwise RMSD for a single molecular species, <RMSD2>1/2, is directly related to average B-factors (<B>) and <RMSF2>1/2. We show this relationship and explore its limits of validity on a heterogeneous ensemble of structures taken from molecular dynamics simulations of villin headpiece generated using distributed-computing techniques and the Folding@Home cluster. Our results provide a basis for quantifying global structural diversity of macromolecules in crystals directly from x-ray experiments, and we show this on a large set of structures taken from the Protein Data Bank. In particular, we show that the ensemble-average pairwise backbone RMSD for a microscopic ensemble underlying a typical protein x-ray structure is ~1.1 A ̊ , under the assumption that the principal contribution to experimental B-factors is conformational variability. 

## INTRODUCTION 

The most frequently used measure for structure comparison in structural biology is, arguably, the atom-positional root mean-square deviation (RMSD) obtained after roto-translational least-squares fitting (1—5). Its applications are diverse and include monitoring structural changes in simulations of protein folding and dynamics (6—12), evaluating the quality of structure prediction schemes (13—16), comparing the diversity of model structures derived from experiments (17,18), assessing the properties of modeling approaches at different levels of resolution (19,20), and defining highresolution shapes of polymers (21). Furthermore, structural diversity of an ensemble of biomolecular structures obtained through computer simulations is analyzed frequently by calculating an all-against-all distribution of RMSD values (pairwise RMSD) (22,23). Such calculation is also carried out commonly in NMR spectroscopy to assess the mutual similarity of the lowest energy structures in an ensemble produced by the refinement process (24—26). The resulting distribution of pairwise RMSD values captures the degree of structural heterogeneity of a given ensemble that can be due to either the intrinsic flexibility of a given structure or the uncertainties of the refinement procedure. The properties of this distribution, calculated typically for backbone atoms, are often summarized by reporting its arithmetic mean. Even though the calculations of pairwise RMSD values can be computationally demanding for large ensembles, they are 

 also frequently used as an appropriate measure for clustering of structures (7,27—29). A distribution of pairwise RMSD values provides information on the mutual similarity of members of a given ensemble when it comes to their global structure. However, to obtain information on local structural flexibility, thermal stability, and heterogeneity of macromolecules, root mean-square fluctuations (RMSF) are often studied (30—32). Most importantly, RMSF can be obtained through DebyeWaller or temperature factors (B-factors) in x-ray experiments using Eq. 1, where B-factors are usually defined as a measure of spatial fluctuations of atoms around their average position and where their motion is described as an isotropic Gaussian distribution of displacements about the average position (33). The inverse of this equation has often been used in the literature to calculate B-factors from various models (most often molecular dynamics simulations or Gaussian network models) and to compare them to experimental values (34—42): 

 RMSF^2 i ¼^ 

 3 Bi 8 p^2 

## : (1) 

 B-factors have also been used in a variety of studies to predict protein flexibility (43,44), assess their thermal stability (45—47), test for errors in protein structures (48), analyze active sites and binding pockets (49—51), correlate side-chain mobility with conformation (52,53), investigate crystal packing contacts (54), analyze and predict protein disordered regions (55—58), and study protein dynamics (37,40,59). However useful B-factors may be, one should always keep in mind that they include not only the positional variance of macromolecules that is due to local thermal 

Submitted October 12, 2009, and accepted for publication November 3, 2009. *Correspondence: zagrovic@medils.hr Editor: Nathan Andrew Baker. Ó2010 by the Biophysical Society 0006-3495/10/03/0861/11 $2.00 doi: 10.1016/j.bpj.2009.11.011 

motion, but also the effects of noise due to refinement errors, lattice defects, crystal contacts, and rigid-body motions (36,41,60). Furthermore, they also contain components coming from both static and dynamic disorder (61,62) whose separation is nontrivial (36). Finally, RMSF can also be predicted from NMR chemical shifts via a measure called random coil index (63—65). Because pairwise RMSD, B-factors (or RMSF) are all frequently used to give information on different aspects of biomolecular ensembles, we study their relationship. We present a derivation showing that, given a set of conservative assumptions, <RMSD2>1/2 is directly proportional to average experimental B-factors (<B>), i.e., <RMSF2>1/2 for a single molecular species. Our finding is illustrated and its limits of validity probed by calculations made on structures taken from molecular dynamic (MD) simulations of the native and unfolded state of the villin headpiece domain (10,66) generated using worldwide-distributed computing techniques. In particular, we use simulated ensembles to study the effects of the exact method of structure alignment on the derived relationship, and show that the influence is typically only marginal. Finally, the newly derived relation is used to calculate quadratic means of pairwise RMSD distributions for a set of x-ray structures, given the B-factors reported in the Protein Data Bank (PDB), to assess their heterogeneity in the crystal environment. To foreshadow the derivation presented in this study, we would like to introduce a useful analogy between 

 <RMSD2>1/2 and <RMSF2>1/2 on the one hand and the radius of gyration (Rg) on the other. The radius of gyration, a measure often used to describe the dimensions of biopolymers such as proteins (67—69), can be analytically calculated in two ways: one using the pairwise distances between monomers (Eq. 2, Fig. 1 A), and the other using the distances between each monomer and their center of mass, i.e., the average position of all monomers if they have the same mass (Eq. 3, Fig. 1 B). 

 R^2 g ¼ 

## 1 

 2 N^2 m 

 XNm 

 i ¼ 1 

 XNm 

 j ¼ 1 

 k~ri ~rjk^2 ; (2) 

 R^2 g^ ¼ 

## 1 

 Nm 

 XNm 

 i ¼ 1 

 k~ri  h ~rik^2 : (3) 

 Indices i and j refer to different monomers, whereas Nm is a total number of monomers in a chain. Vector ~r represents spatial coordinates of a monomer, whereas h~ri is the average position of Nm monomers. Equations 2 and 3 are shown to be identical by modifications of the Lagrange’s theorem (70). Our derivation of the relationship between <B>, <RMSF2>1/2, and <RMSD2>1/2, which is the main result of this study, mirrors the relationship between these two definitions of the radius of gyration. Namely, the two definitions given for Rg can be applied easily to ensembles of biomolecular structures where monomers are replaced by structures and RMSD is used as a measure of distance between them 

 FIGURE 1 Analogy connecting <RMSD2>1/2^ and <RMSF2>1/2 with the radius of gyration. (A) For a polymer consisting of Nm monomers, the radius of gyration can be calculated as a root mean-square average over all pairwise distances between monomers as shown in Eq. 2. ( B) Another way of calculating the radius of gyration is through distances between monomers and their average position shown in Eq. 3. Analogously to the two ways of calculating Rg, there is equivalence between the root mean-square average of pairwise RMSD for a set of structures (<RMSD2>1/2) ( C) and the root meansquare average deviation from the average structure (<RMSF2>1/2) ( D), as shown in this study. k is a multiplicative factor that is a function of Ns (see Eq. 19). Villin structures in C and D have been prepared by VMD v1.8.6 (85). 

862 Kuzmanic and Zagrovic 

(Eq. 2, Fig. 1, C and D). Following this analogy, there is equivalence between root mean-square average pairwise RMSD, <RMSD2>1/2 (recalling the first definition of Rg, see Eq. 2) and the root mean-square average deviation between each structure and the average structure of the ensemble, <RMSF2>1/2 (recalling the second definition of Rg, see Eq. 3). The exact relationship between <RMSD2>1/2, <RMSF2>1/2, and <B>is explored below, together with an analysis of a novel measure of structural diversity in ensembles, the structural radius (Rstruct), which can be thought of as a structural analog of Rg. 

## MATERIALS AND METHODS 

Molecular dynamics simulations 

Thousands of tens of nanoseconds long, independent trajectories for the villin headpiece domain were generated using a heterogeneous computer cluster as a part of the ongoing Folding@Home distributed computing project (10,66). The folding simulations were initiated from fully extended conformations ( 4 ¼  135 , j¼ 135 ) with N-acetyl and C-amino caps. The equilibrium simulations were started from the experimental NMR structure of the molecule (PDB code 1VII, average structure) (66). The simulations, run using Tinker biomolecular simulation package, involved Langevin dynamics in implicit GB/SA solvent (71) (velocity damping parameter of g¼ 91 ps1) with a 2-fs integration step, at 300 K. Bond lengths were constrained using RATTLE (72). No cutoffs were used for electrostatics. The protein was modeled using the OPLSua force field (73). The molecule in the equilibrium simulations was stable with respect to both secondary and tertiary structure (10,74). The structures were divided into two data sets for calculations: one that included native-like structures (1543 structures taken from the same number of independent equilibrium simulations at t ¼ 20 ns), whereas the other one contained unfolded structures 5213 structures taken from the same number of independent folding trajectories at t ¼ 27 ns). 

RMSD calculations—pairwise alignment 

Toillustrate the relationship betweenaverage RMSDand RMSFfor ensembles spanning a large range of average RMSD values, we used a clustering procedure on the two villin data sets. The main purpose of this procedure was to derive a set of mutually different distributions of pairwise RMSD to help us illustrate and assess the properties of the derivation provided in this study. Backbone atoms for each pair of structures from both simulated data sets were optimally aligned (pairwise alignment (PA)) before RMSD calculations. Nonweighted pairwise RMSDs were then calculated for the aligned backbone atoms that included C, N, and Caof every residue (108 atoms in total). A distribution of the calculated pairwise RMSD values was plotted and divided into 20 equal segments between the smallest and the largest RMSD value. The structure that appeared in the highest number of pairs in a given segment was chosen as the center of a cluster, and the structures paired with it were assigned to that particular cluster as well. Twenty clusters were obtained through such a procedure for each data set (number of structures in each cluster is listed in Table S1 in the Supporting Material). Nonweighted pairwise RMSD was calculated for each cluster in the same way as described above using backbone-based PA. Quadratic mean of pairwise RMSD for each cluster was calculated as well. We have noticed that the choice of the reference structure for the alignment of all the structures before calculating RMSF does affect its quadratic value in the very heterogeneous data set as shown in the Results. Therefore, RMSF for each cluster was calculated by using every single structure from the cluster for the alignment before the calculations and then quadratically averaging the obtained values to get the RMSF value for each cluster. 

 All the alignments and calculations were done by using GROMACS-3.3 and its routines (75). 

 RMSD calculations—reference structure alignment Backbones of all the structures were aligned to the backbone of the native structure of the villin headpiece domain taken from the PDB (average NMR structure, PDB code 1VII) (reference structure alignment (RSA)) to rule out the alignment effect from the calculations. Fitted structures were then subjected to the same procedure described in the previous section to obtain clusters (number of structures in each cluster is also listed in Table S1) and quadratic averages of RMSD and RMSF values. Structures were aligned to the reference structure using the McLachlan algorithm (76) as implemented in the program ProFit v3.1 (Martin, A.C.R., http://www. bioinf.org.uk/software/profit/). 

## RESULTS 

 Demonstration of a direct proportionality between <RMSD2>1/2 and <RMSF2>1/2 RMSD is defined as the root mean-square-average distance between atoms of two optimally superimposed macromolecules (Si and Sj) and is calculated as a minimum over all rotations and translations of one of the structures being compared (Eq. 4). 

## RMSD 

##  

 Si;Sj 

##  

 ¼ min 

## 1 

 Na 

 XNa 

 k ¼ 1 

 k~rik ~rjkk^2 

## !^12 

 rot;trans 

## ; (4) 

 where Na is the number of atoms in a structure and should not be confused with the Avogadro constant. Indices i and j refer to different structures, whereas the index k refers to the atom position in a given structure. Vector~r represents spatial coordinates of a given atom. To capture the properties of a distribution of pairwise RMSD, in this study we have used its quadratic mean calculated using Eq. 5 as it lends itself to better analytic manipulation compared to the arithmetic mean that is usually reported in NMR studies. 

## RMSD^2 

(^1) = 2 ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 2 NsðNs  1 Þ N Xs 1 i ¼ 1 XNs j>i 

## RMSD^2 

##  

 Si;Sj 

##  

 vu u 

t (^) ; (5) where Ns is the number of structures in an ensemble. Here and in the rest of the derivation we will assume that all the structures are aligned to the same reference structure (therefore, the notation from Eq. 4 was simplified). Note that for the derivation it is not relevant what the exact nature of the reference structure is, as long as the same structure is used for aligning the whole ensemble. This is to be contrasted with typical calculation of pairwise RMSD, where each pair of structures is mutually superimposed. RMSF for a specific number of structures is defined as a root mean-square-average distance between an atom and its average position in a given set of structures (Eq. 6) Determination of Average RMSD from B-Factors 863 

 RMSFk ¼ 

 ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 Ns 

 XNs 

 i ¼ 1 

 k~rik  h~rikk^2 

 v uu 

t (^) ; (6) where h~rik is the average position of the atom k over Ns structures (Eq. 7) h~rik ¼ 

## 1 

 Ns 

 XNs 

 i ¼ 1 

 ~rik: (7) 

In the following, we have used the quadratic mean of RMSF calculated using Eq. 8 

## RMSF^2 

(^1) = 2 ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 Na XNa k ¼ 1 RMSF^2 k vu u t (^) : (8) If Eq. 6 is inserted into Eq. 8, 

## RMSF^2 

(^1) = 2 ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 Na XNa k ¼ 1 

## 1 

 Ns 

 XNs 

 i ¼ 1 

 k~rik  h~rikk^2 

 v u u 

t (^) : (9) On the other hand, if Eq. 4 is inserted into Eq. 5, 

## RMSD^2 

(^1) = 2 ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 2 NsðNs  1 Þ XNs^ ^1 i ¼ 1 XNs j>i 

## 1 

 Na 

 XNa 

 k ¼ 1 

 k~rik ~rjkk^2 

 v u ut : 

## (10) 

The sums in Eq. 10 can be rearranged 

## RMSD^2 

(^1) = 2 ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 Na XNa k ¼ 1 

## 2 

 NsðNs  1 Þ 

 Ns X  1 

 i ¼ 1 

 XNs 

 j>i 

 k~rik ~rjkk^2 

 v u ut : 

## (11) 

The sums over Na can now be written 

## RMSD^2 

(^1) = 2 ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 Na XNa k ¼ 1 2 N^2 s NsðNs  1 Þ 

## 1 

 2 Ns^2 

 XNs 

 i ¼ 1 

 XNs 

 j ¼ 1 

 k~rik ~rjkk^2 

 v u ut : 

## (12) 

For simplicity, let us define a new variable 

 R^2 k ¼ 

## 1 

 Ns 

 XNs 

 i ¼ 1 

 k~rik  h ~rikk^2 ¼ 

## 1 

 Ns 

 XNs 

 i ¼ 1 

##  

 ~r^2 ik  2 ~rikh~rik þ h ~ri^2 k 

##  

 ¼ h ~ri^2 k^ þ 

## 1 

 Ns 

 XNs 

 i ¼ 1 

 ~r^2 ik: ð 13 Þ 

The first term on the right-hand side of Eq. 13 can be separated by applying Eq. 7 and the second term can be represented as a double summation over the number of structures 

R^2 k ¼  

## 1 

 Ns 

 XNs 

 i ¼ 1 

 ~rik 

## ! 

## 1 

 Ns 

 XNs 

 j ¼ 1 

 ~rjk 

## ! 

 þ 

## 1 

 2 N^2 s 

 XNs 

 i ¼ 1 

 XNs 

 j ¼ 1 

##  

 ~r^2 ik þ~r^2 jk 

##  

## : 

## (14) 

 Terms in Eq. 14 can be added 

 R^2 k ¼ 

## 1 

 2 N^2 s 

 XNs 

 i ¼ 1 

 XNs 

 j ¼ 1 

##  

  2 ~rik~rjk þ ~r^2 ik þ ~r^2 jk 

##  

## ¼ 

## 1 

 2 N^2 s 

 XNs 

 i ¼ 1 

 XNs 

 j ¼ 1 

 k~rik ~rjkk^2 : (15) 

 By combining Eqs. 13 and 15, we now see that 

 R^2 k ¼ 

## 1 

 Ns 

 XNs 

 i ¼ 1 

 k~rik  h~rikk^2 ¼ 

## 1 

 2 N^2 s 

 XNs 

 i ¼ 1 

 XNs 

 j ¼ 1 

 k~rik ~rjkk^2 : 

 (16) 

 Using the former definition of R^2 k in Eq. 16, we can express <RMSF2>1/2 (Eq. 9) as 

## RMSF^2 

(^1) = 2 ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 Na XNa k ¼ 1 R^2 k v u u t (^) : (17) Furthermore, we can express <RMSD2>1/2 (Eq. 12) as 

## RMSD^2 

(^1) = 2 ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 Na 2 Ns Ns  1 XNa k ¼ 1 R^2 k v u u t (^) : (18) Finally, combining Eqs. 1, 17, and 18, a formula is derived that proves that <RMSD2>1/2 is directly proportional to <RMSF2>1/2 and, subsequently, B-factors. 

## RMSD^2 

(^1) = 2 ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffi 2 Ns Ns  1 r RMSF^2 (^1) = 2 

## ¼ 

 ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 2 Ns Ns  1 

## 1 

 Na 

 XNa 

 k ¼ 1 

 3 Bk 8 p^2 

 v u ut : (19) 

 Finally, for Ns [1, 

## RMSD^2 

(^1) = 2 z ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 2 Na XNa k ¼ 1 3 Bk 8 p^2 vu u t (^) : (20) Exclusion of the ensemble size effect and the derivation of identity Typical calculations of the average pairwise RMSD for a given ensemble exclude the RMSDs between the same structures (equaling zero). One can show (see below) that this causes the relationship between the average RMSD and RMSF (and subsequently B-factors) to depend on the number of structures in an ensemble as in Eq. 19. This effect, as seen in Eq. 20, vanishes only for a large number of structures in the ensemble. One can define a new measure, Rstruct (that we term structural radius), using the following equation instead of Eq. 5 to eliminate the aforementioned effect: 864 Kuzmanic and Zagrovic 

 Rstruct ¼ 

 ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 2 N^2 s 

 XNs 

 i ¼ 1 

 XNs 

 j ¼ 1 

## RMSD^2 

##  

 Si;Sj 

##  

 v uu 

t (^) : (21) Combining Eqs. 4 and 21, it follows Rstruct ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 2 N^2 s XNs i ¼ 1 XNs j ¼ 1 

## 1 

 Na 

 XNa 

 k ¼ 1 

 k~rik ~rjkk^2 

 v u u 

t (^) : (22) The sums in Eq. 22 can be rearranged Rstruct ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 Na XNa k ¼ 1 

## 1 

 2 N^2 s 

 XNs 

 i ¼ 1 

 XNs 

 j ¼ 1 

 k~rik ~rjkk^2 

 v u u 

t (^) : (23) Equation 16 can be inserted into Eq. 23 Rstruct ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 Na XNa k ¼ 1 R^2 k v uu t (^) : (24) The calculation of the average RMSD and RMSF remains the same as in the previous section, so by combining Eqs. 1, 17, 20, and 24, it follows Rstruct ¼ RMSF^2 (^1) = 2 ¼ ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi 1 Na XNa k ¼ 1 3 Bk 8 p^2 v u ut z 

## 1 

 ffiffiffi 2 

 p RMSD^2 

(^1) = 2 : 

## (25) 

With Eq. 25 we have shown that Rstruct and <RMSF2>1/2 are identical and can be linked directly with both <RMSD2>1/2 and experimental B-factors. In this sense, Rstruct serves as a measure of structural diversity of an ensemble of structures that is in an intuitively clear fashion directly related to B-factors, RMSF, and RMSD. 

 Illustrations of the relationship between the average RMSD and RMSF To demonstrate the derived relationship between the average values of pairwise RMSD and RMSF, structures taken from distributed-computing MD simulations of villin headpiece domain were used to calculate the two measures. Each data set (native and unfolded) was divided into two sets of 20 clusters based on the distributions of pairwise RMSD values for two types of alignment (PA or reference structure alignment (RSA)). For RSA, all structures were first roto-translationally aligned to a common reference structure before their pairwise RMSD values were calculated. For PA, each individual pair of structures was first optimally aligned before calculating their RMSD. Fig. 2 shows these distributions, their arithmetic means and standard deviations. For the native data set, we can see that distributions of pairwise RMSD are very much alike regardless of the type of the alignment. Their arithmetic means and standard deviations are also very similar: 4.02 5 1.95 A ̊ for the PA curve and 4.07 5 2.01 A ̊ for the RSA curve. On the other hand, distributions associated with the unfolded data set and generated with different types of alignment are more different that can be seen from their arithmetic means and standard deviations: 7.38 5 1.23 A ̊ for the PA curve and 7.86 5 1.39 A ̊ for the RSA curve. From the given values, it can be seen that RMSD values calculated after aligning structures to a reference structure are higher than the ones calculated after the pairwise alignment. This is, of course, expected as for each individual pair of structures, PA gives by definition the lowest values over all possible roto-translational fittings. To further demonstrate this point, in the inset of Fig. 2 we compare RMSD values calculated using both types of alignment for several hundred randomly chosen pairs of structures from both data sets. It is clear from the inset of Fig. 2 that none of the RMSD values calculated after pairwise alignment of 

 FIGURE 2 Distributions of backbone pairwise RMSD values of the native and unfolded ensembles of the villin headpiece domain. The dashed black curve represents backbone RMSD values calculated using PA for the native ensemble (<RMSD>¼ 4.02 5 1.95 A ̊ ). Values for the unfolded ensemble are shown with the thin curve (<RMSD>¼ 7.38 5 1.23 A ̊ ). Distributions of the corresponding RMSD values calculated using initial alignment to a reference structure (1VII, average structure) (RSA), are shown with the dashed gray curve for the native ensemble (<RMSD>¼ 4.07 5 2.01 A ̊ ) and with the thick curve for the unfolded ensemble (<RMSD>¼ 7.86 5 1.39 A ̊ ). The average values and standard deviations for every distribution are also given in the figure. All the values were binned in 0.5 A ̊ bins to generate the distributions.Inset: Relationship between pairwise RMSD values calculated using PA and RSA. For clarity, several hundred randomly chosen points whose values have been taken from the native ensemble are shown as solid circles, whereas several hundred points whose values have been taken from the unfolded ensemble are shown as open circles. The identity line is shown in black. 

Determination of Average RMSD from B-Factors 865 

structures is higher than the corresponding values calculated after aligning structures to a reference structure. For every pair of structures belonging to a particular cluster, pairwise RMSD (Eq. 4) was calculated using either PA or RSA, and the quadratic mean of all the RMSD values (Eq. 5) in the given cluster was determined. RSA-calculations were used to study the effect of the optimal alignment on the derived relationship. RMSF for backbone atoms in the cluster was computed as well and its quadratic mean was calculated (Eq. 8). The average values of pairwise RMSD and RMSF for clusters of both data sets and types of alignment are presented in Fig. 3. As can be seen, in the case of RSA, the real data completely agrees with the analytical derivation above (Fig. 3 A). The slope of the trendline shown in Fig. 3 A is in complete agreement with the expected value of 21/2 (seen from the derivation) and its squared correlation 

 coefficient (R2) equals 1. However, in the case of PA (Fig. 3 B), the slope of the trendline (1.2968) deviates from the expected value due to the pairwise alignment of structures before calculations, but the R2 still has a high value of 0.9956. Deviations caused by the pairwise alignment are smaller for the native data set and the trendline applied to it would have a slope of 1.3862 with an R2 of 0.9998 (not shown). The relationship shown between RMSD and RMSF explored in Fig. 3 still depends on the number of structures contained in a cluster. That effect can be eliminated by using the structural radius (Eq. 21) as a measure of structural diversity. The calculated values of the structural radius and <RMSF2>1/2 for clusters of both data sets and types of alignment are presented in Fig. 4. In the case of RSA (Fig. 4 A), both slope of the applied trendline and its squared correlation coefficient equal 1 showing that the two measures 

FIGURE 3 <RMSD2>1/2 versus [Ns/(Ns-1)]1/2<RMSF2>1/2 for native and unfolded state clusters for the villin headpiece domain. <RMSD2>1/2 values were calculated using Eq. 5, whereas <RMSF2>1/2 values using Eq. 8. Ns is the number of structures contained in a given cluster. The values for the native ensemble are shown as solid diamonds, and the values for the unfolded ensemble are shown as open circles. In A, all the values have been calculated using RSA, whereas the values in B have been calculated using PA. Trendlines, their analytic expressions, and R2 are also shown in the figure. 

 FIGURE 4 Rstruct versus <RMSF2>1/2 for native and unfolded state clusters for the villin headpiece domain. Rstruct values were calculated using Eq. 21, whereas <RMSF2>1/2 values using Eq. 8. The values for the native ensemble are shown as solid diamonds, and the values for the unfolded ensemble are shown as open circles. In A, all the values have been calculated using RSA. The values in B have been calculated using PA. Trendlines, their analytic expressions, and R2 are also shown in the figure. 

866 Kuzmanic and Zagrovic 

are identical and confirming the derivation (Eq. 25). The agreement of the two measures is slightly worse in Fig. 4 Bdue to the pairwise alignment of structures before calculations and the slope of the trendline (0.9099) differs from the expected value of 1, but still has a very high R2 of 0.9960. Once more, deviations caused by the pairwise alignment are smaller for the native data set and the trendline applied to it would have a slope of 0.9804 with R2 of 0.9999 (not shown). Altogether, one can claim that the effects of the alignment are negligible (<2%) for ensembles with <RMSD2>1/2 under 4 A ̊. We also examined how the choice of the reference structure for alignment affects the <RMSF2>1/2 values, by using every single structure in a given cluster for the alignment before calculations and comparing the obtained distributions of <RMSF2>1/2 values for every cluster through their arithmetic means and standard deviations. We have also analyzed the maximal and the minimal quadratic means of every cluster to show how extreme the effects of the choice of the reference structure for the alignment can be (Fig. 5). As can be seen from the figure, arithmetic means of both data sets are very close to the minimal values of quadratic means. Their standard deviations are also quite small and they do not exceed the value of 0.26 A ̊ , but they are higher for the unfolded data set. However, for some of the clusters, the difference between the maximal and the minimal value of <RMSF2>1/2 is more than twofold (e.g., clusters 15 and 18 in the native ensemble) that implies that the choice of the structure for the alignment can make a significant difference for a very diverse data set such as this. 

Structural heterogeneity of proteins in crystals 

The above relationship between experimental B-factors, <RMSD2>1/2 and the structural radius provided us with an opportunity to calculate the latter (<RMSD2>1/2 and Rstruct) for an ensemble of structures in a crystal using Eq. 25 and the measured B-factors, thus assessing the heterogeneity of a given crystal. The calculations were made under the assumption that the crystal contains a very large number of structures (Ns [1) that eliminated cluster size effect. Distri

 butions of <RMSD2>1/2 and Rstruct values for backbone and all atoms for a representative set of x-ray structures from the PDB with ~4800 structures are presented in Fig. 6 (see the Supporting Material for selection criteria). <RMSD2>1/2 values for the backbone and all atoms are quite similar: 1.07 5 0.23 A ̊ for the backbone and 1.13 5 0.23 A ̊ for all atoms with the maximum values that are <2.5 A ̊ , but still with >6% of structures with <RMSD2>1/2^ >1.5 A ̊ for all atoms. The structural radius values are lower than <RMSD2>1/2 values, but are still similar: 0.76 5 0.17 A ̊ for the backbone and 0.80 5 0.16 A ̊ for all atoms with the maximum values that do not exceed the value of 1.8 A ̊. 

 DISCUSSION To the best of our knowledge, the heterogeneity of biomolecular ensembles in crystals used in x-ray experiments has never been evaluated previously on the level of pairwise RMSD. Here, we have derived and illustrated a nontrivial relationship between ensemble-average RMSD and RMSF and, subsequently, isotropic B-factors that gave us the opportunity to evaluate the heterogeneity of the microscopic ensembles underlying the typical crystal structures deposited in the PDB. When these values (Fig. 6) are compared to the values for villin headpiece obtained through simulation (Figs. 3 and 4), we can easily see that even the highest values for proteins in a crystal are rather small and coincide with the values for the native data set in the villin graphs, for which the relationship between <RMSD2>1/2 and <RMSF2>1/2 is close to exact, regardless of the alignment. The crystal lattice aligns the protein structures to a significant degree such that the RSA would likely be a valid approximation, but it is reassuring to see that the typical values for <RMSD2>1/2 in crystals occupy the regime in which the choice of alignment makes very little, if any, difference. It is our estimate that if one calculates <RMSD2>1/2 from B-factors as in Eq. 20, the error committed is <2% on average compared to the ideal-case pairwise alignment. Namely, 2% is the average deviation between the <RMSD2>1/2 values obtained using RSA and PA for all villin structures below <RMSD2>1/2 of 4 A ̊ (Fig. 3). It has been proposed recently 

 FIGURE 5 Arithmetic mean, standard deviation and extreme values of quadratic means of RMSF for every cluster. <RMSF2>1/2 values for every cluster were calculated using Eq. 8, using every structure in the cluster for the alignment before calculation. The lower curve shows arithmetic means of the distributions of quadratic means for native structure clusters. The upper line captures the values for the unfolded structures. Standard deviations of the distributions are shown with black bars. Extreme values and their differences are shown with a light gray area for the native ensemble and with a dark gray area for the unfolded one. 

Determination of Average RMSD from B-Factors 867 

that a single crystallographic structure deposited in the PDB is not enough to assess the heterogeneity of a crystal and that an ensemble of models would be a more suitable representation (77). Nevertheless, we feel that the identity we have shown in this study is a good starting point for the assessment of crystal heterogeneity that could be generalized to an ensemble of models in a straightforward manner. Finally, the derivation presented here could in future research potentially be generalized to include anisotropic B-factors as well. Due to the additional information present, the associated <RMSD2>1/2 values would likely be more informative in that case. Given the analogy between the structural radius and the radius of gyration and our derivation, it becomes obvious that the structural radius can be used for an ensemble of macromolecular structures in the same sense as the radius of gyration is used for a single macromolecular structure. Although the radius of gyration provides information on a macromolecule’s size, the structural radius tells how diverse structures in a given ensemble are on a global scale. The structural radius can be calculated either by using pairwise RMSD as a measure of distance between structures (Eq. 21), or by using RMSD values between each structure and the average structure of the ensemble. The latter corresponds to <RMSF2>1/2 as shown in Eq. 9, but with a difference of first summing over the number of atoms (Na), and then over the number of structures (Ns), which is actually identical to Eq. 9 because the sums are interchangeable. Note that if the structural radius is calculated in this way, its usage should be restricted to molecular ensembles whose <RMSD2>1/2 is (6 A ̊ (for which the alignment effects are (3%). For more heterogeneous ensembles, we would advise to either use the PA approach or simply exercise caution when interpreting 

 results because of the potential deviations at high RMSD values. Here, it should be mentioned that it has been shown previously that the sum of squared distances for all atomic pairs equals the sum of squared distances to the average structure (78). Even though the authors suggested that this connection could be used for speeding up RMSD calculations (as the number of RMSD evaluations is reduced from Ns(Ns  1)/2 to Ns) and improving algorithms in multiple structure alignment, they made no explicit link between RMSD, RMSF, and B-factors. An important challenge in quantifying the relationship between RMSF and RMSD is the influence of optimal alignment of two structures on their mutual RMSD value. All the RMSD values calculated after the optimal pairwise alignment of two structures (PA) are lower than the ones calculated after the initial alignment of all the structures to a reference (RSA). Optimal alignment means that roto-translational fitting of the structures is carried out to minimize the RMSD value between them. Now, if one optimally aligns two structures to a reference structure, those two structures will not be optimally aligned with each other and their mutual RMSD will not be minimal, unless all three structures are mutually highly similar. For example, the effect of the optimal alignment is noticeably lesser in the native ensemble of villin than in the unfolded one, because 1), the unfolded ensemble is much more heterogeneous than the native one, and 2), the structure used as a reference is the native form of the villin headpiece domain taken from the PDB. However, as shown here, the effects of the alignment are typically only marginal. Parenthetically, one way of avoiding roto-translational alignment altogether would be to use internal coordinates to represent biomolecules and assess their structural heterogeneity. Nevertheless, as biomolecular structures (including the associated B-factors) are refined in Cartesian coordinates, we believe that the most natural measure for evaluating their global structural diversity directly from experiment should also involve atom-positional Cartesian representation, such as in the case of RMSD. In fact, the mathematical simplicity of the connection between B-factors, RMSF, and RMSD described in this study actually serves as indirect evidence supporting this claim. In addition, RMSF values are also affected by the choice of the reference structure for the alignment. In Fig. 5, we show the arithmetic mean and standard deviation of distributions of <RMSF2>1/2 values calculated for every cluster, but differing in the choice of the structure used for the alignment before calculations. Even though the standard deviations throughout the clusters are quite small and they never exceed the value of 0.26 A ̊ , the differences between the maximal and minimal values of quadratic means in some clusters are twofold (Fig. 5), which suggests that the choice of a reference structure in certain rare cases could indeed influence the outcome significantly. Contrary to this finding, Yang et al. (39) found no major effect of the choice of the alignment structure in their studies where they calculated residual 

FIGURE 6 Distributions of root mean-square pairwise RMSD values calculated for x-ray structures. Rstruct values calculated using Eq. 25 are represented by the thin solid curve for the backbone atoms with the average of 0.76 5 0.17 A ̊ and the thick solid curve for all the atoms in the structure (0.80 5 0.16 A ̊ ). <RMSD2>1/2 values calculated using Eq. 20 are represented by the thin dashed curve for backbone atoms (1.07 5 0.23 A ̊ ) and the thick dashed curve for all the atoms in the structure (1.13 5 0.23 A ̊ ). Average values and standard deviations for every distribution are also shown in the figure. All the values were binned in 0.1 A ̊ bins to generate the distributions. 

868 Kuzmanic and Zagrovic 

RMSD of the ensembles of NMR models. We explain this discrepancy with the greater diversity of structures in our data set compared to most ensembles of NMR models, and we would like to stress the necessity of evaluating the diversity of an ensemble before ruling out the possible effect of the choice of the reference structure. Here, we would like to emphasize that all of our conclusions involving B-factors and other nonprimary data depend on several critical assumptions. The danger of using derived data, such as B-factors, lies in the inaccuracies of the refinement processes linking the primary data from x-ray crystallography and NMR with model structures. All the structures submitted to the PDB are based on time and ensembleaverage signals that undoubtedly affect the nature of the models derived from them and potentially cause different artifacts to appear (79,80). Furthermore, it is hard to tell whether the refinement has been conducted using the stateof-the-art software at the time of deposition and whether the software has been used in an optimal manner (81). For that reason, there have been several re-refinement attempts that yielded improved structural models (81—83). Until all the artifacts are fully resolved and understood, making assumptions based on the comparison of simulations and secondary or derived data can result in overinterpreted or misinterpreted conclusions (84). Nonetheless, we find the interpretation of our results to be useful for determining the <RMSD2>1/2 of an ensemble of structures in a crystal from B-factors as long as the Eq. 1 holds, i.e., as long as the major contribution to the measured B-factors is indeed the structural heterogeneity of molecules. 

## SUPPORTING MATERIAL 

One table is available at [http://www.biophysj.org/biophysj/supplemental/](http://www.biophysj.org/biophysj/supplemental/) S0006-3495(09)01738-X. 

We thank Ivo F. Sbalzarini, Christian L. Mu ̈ller, and the members of the Laboratory of Computational Biophysics at MedILS for useful comments on the manuscript. Contribution of Folding@Home members is gratefully acknowledged. 

This work was supported in part by the National Foundation for Science, Higher Education and Technological Development of Croatia (EMBO Installation grant to B.Z.), the Unity Through Knowledge Fund (UKF 1A to B.Z.), and a National Institutes of Health R01-GM062868 grant (Folding@Home). 

## REFERENCES 

1. McLachlan, A. D. 1972. Mathematical procedure for superimposing     atomic coordinates of proteins. Acta Crystallogr. A. 28:656—657. 

2. Kabsch, W. 1976. A solution for the best rotation to relate two sets of     vectors. Acta Crystallogr. A. 32:922—923. 

3. Kabsch, W. 1978. A discussion of the solution for the best rotation to     relate two sets of vectors. Acta Crystallogr. A. 34:827—828. 

4. Kneller, G. R. 1991. Superposition of molecular structures using quater-     nions. Mol. Simul. 7:113—119. 

5. Kneller, G. R. 2005. Comment on ‘‘Using quaternions to calculate     RMSD’’ [J. Comp. Chem. 25, 1849 (2004)]. J. Comput. Chem.     26:1660—1662. 

6. Duan, Y., and P. A. Kollman. 1998. Pathways to a protein folding inter-     mediate observed in a 1-microsecond simulation in aqueous solution.     Science. 282:740—744. 

7. Daura, X., B. Jaun, ., A. E. Mark. 1998. Reversible peptide folding in     solution by molecular dynamics simulation. J. Mol. Biol. 280:925—932. 

8. Daura, X., W. F. van Gunsteren, and A. E. Mark. 1999. Folding-unfold-     ing thermodynamics of a beta-heptapeptide from equilibrium simula-     tions. Proteins. 34:269—280. 

9. Zagrovic, B., E. J. Sorin, and V. Pande. 2001. Beta-hairpin folding     simulations in atomistic detail using an implicit solvent model.     J. Mol. Biol. 313:151—169. 

10. Zagrovic, B., C. D. Snow, ., V. S. Pande. 2002. Simulation of folding     of a small alpha-helical protein in atomistic detail using worldwide-     distributed computing. J. Mol. Biol. 323:927—937. 

11. Yang, J. S., W. W. Chen, ., E. I. Shakhnovich. 2007. All-atom ab     initio folding of a diverse set of proteins. Structure. 15:53—63. 

12. Verma, A., and W. Wenzel. 2009. A free-energy approach for all-atom     protein simulation. Biophys. J. 96:3483—3494. 

13. Schueler-Furman, O., C. Wang, ., D. Baker. 2005. Progress in     modeling of protein structures and interactions. Science. 310:638—642. 

14. Rangwala, H., and G. Karypis. 2008. fRMSDPred: predicting local     RMSD between structural fragments using sequence information.     Proteins. 72:1005—1018. 

15. Zhang, Y. 2008. Progress and challenges in protein structure prediction.     Curr. Opin. Struct. Biol. 18:342—348. 

16. Bowman, G. R., and V. S. Pande. 2009. The roles of entropy and     kinetics in structure prediction. PLoS One. 4:e5840. 

17. Andrec, M., D. A. Snyder, ., R. M. Levy. 2007. A large data set     comparison of protein structures determined by crystallography and     NMR: statistical test for structural differences and the effect of crystal     packing. Proteins. 69:449—465. 

18. Saccenti, E., and A. Rosato. 2008. The war of tools: how can NMR spec-     troscopists detect errors in their structures? J. Biomol. NMR. 40:251—261. 

19. Sullivan, D. C., and I. D. Kuntz. 2001. Conformation spaces of proteins.     Proteins. 42:495—511. 

20. Sullivan, D. C., and I. D. Kuntz. 2004. Distributions in protein confor-     mation space: implications for structure prediction and entropy.     Biophys. J. 87:113—120. 

21. Mu ̈ller, C. L., I. F. Sbalzarini, ., P. H. Hu ̈nenberger. 2009. In the eye of     the beholder: inhomogeneous distribution of high-resolution shapes     within the random-walk ensemble. J. Chem. Phys. 130:214904—214925. 

22. Bru ̈schweiler, R. 2003. Efficient RMSD measures for the comparison of     two molecular ensembles. Proteins. 50:26—34. 

23. Zagrovic, B., and W. F. van Gunsteren. 2007. Computational analysis     of the mechanism and thermodynamics of inhibition of phosphodies-     terase 5A by synthetic ligands. J. Chem. Theory Comput. 3:301—311. 

24. Laurents, D., J. M. Pe ́rez-Can ̃adillas, ., M. Bruix. 2001. Solution     structure and dynamics of ribonuclease Sa. Proteins. 44:200—211. 

25. Ko ̈ve ́r, K. E., M. Bruix, ., M. Rico. 2008. The solution structure and     dynamics of human pancreatic ribonuclease determined by NMR spec-     troscopy provide insight into its remarkable biological activities and     inhibition. J. Mol. Biol. 379:953—965. 

26. Zhou, Z., H. Q. Feng, ., Y. Bai. 2008. The high-resolution NMR     structure of the early folding intermediate of the Thermus thermophilus     ribonuclease H. J. Mol. Biol. 384:531—539. 

27. Shortle, D., K. T. Simons, and D. Baker. 1998. Clustering of low-energy     conformations near the native structures of small proteins. Proc. Natl.     Acad. Sci. USA. 95:11158—11162. 

28. Betancourt, M. R., and J. Skolnick. 2001. Finding the needle in     a haystack: educing native folds from ambiguous ab initio protein struc-     ture predictions. J. Comput. Chem. 22:339—353. 

Determination of Average RMSD from B-Factors 869 

29. Zhang, Y., and J. Skolnick. 2004. SPICKER: a clustering approach to     identify near-native protein folds. J. Comput. Chem. 25:865—871. 

30. Kro ́l, M., I. Roterman, ., P. Spo ́lnik. 2005. Analysis of correlated     domain motions in IgG light chain reveals possible mechanisms of     immunological signal transduction. Proteins. 59:545—554. 

31. Yin, J., D. Bowen, and W. M. Southerland. 2006. Barnase thermal titra-     tion via molecular dynamics simulations: detection of early denaturation     sites. J. Mol. Graph. Model. 24:233—243. 

32. Sousa, S. F., P. A. Fernandes, and M. J. Ramos. 2009. Molecular     dynamics simulations on the critical states of the farnesyltransferase     enzyme. Bioorg. Med. Chem. 17:3369—3378. 

33. Willis, B. T. M., and A. W. Pryor. 1975. Thermal Vibrations in Crystal-     lography. Cambridge University Press, London; New York. 

34. Phillips, Jr., G. N. 1990. Comparison of the dynamics of myoglobin in     different crystal forms. Biophys. J. 57:381—383. 

35. Halle, B. 2002. Flexibility and packing in proteins. Proc. Natl. Acad.     Sci. USA. 99:1274—1279. 

36. Meinhold, L., and J. C. Smith. 2005. Fluctuations and correlations in     crystalline protein dynamics: a simulation analysis of staphylococcal     nuclease. Biophys. J. 88:2554—2563. 

37. Lu, W. C., C. Z. Wang, ., K. M. Ho. 2006. Dynamics of the trimeric     AcrB transporter protein inferred from a B-factor analysis of the crystal     structure. Proteins. 62:152—158. 

38. Glykos, N. M. 2007. On the application of molecular-dynamics     simulations to validate thermal parameters and to optimize TLS-group     selection for macromolecular refinement. Acta Crystallogr. D Biol.     Crystallogr. 63:705—713. 

39. Yang, L. W., E. Eyal, ., I. Bahar. 2007. Insights into equilibrium     dynamics of proteins from comparison of NMR and x-ray data with     computational predictions. Structure. 15:741—749. 

40. Lu, C. H., S. W. Huang, ., J. K. Hwang. 2008. On the relationship     between the protein structure and protein dynamics. Proteins. 72:     625—634. 

41. Li, D. W., and R. Bru ̈schweiler. 2009. All-atom contact model for     understanding protein dynamics from crystallographic B-factors.     Biophys. J. 96:3074—3081. 

42. Hu, Z., and J. Jiang. 2010. Assessment of biomolecular force fields for     molecular dynamics simulations in a protein crystal. J. Comp. Chem.     31:371—380. 

43. Karplus, P. A., and G. E. Schulz. 1985. Prediction of chain flexibility     in proteins—a tool for the selection of peptide antigens. Naturwissen-     schaften. 72:212—213. 

44. Vihinen, M., E. Torkkila, and P. Riikonen. 1994. Accuracy of protein     flexibility predictions. Proteins. 19:141—149. 

45. Vihinen, M. 1987. Relationship of protein flexibility to thermostability.     Protein Eng. 1:477—480. 

46. Parthasarathy, S., and M. R. N. Murthy. 2000. Protein thermal stability:     insights from atomic displacement parameters (B values). Protein Eng.     13:9—13. 

47. Reetz, M. T., P. Soni, and L. Ferna ́ndez. 2009. Knowledge-guided labo-     ratory evolution of protein thermolability. Biotechnol. Bioeng.     102:1712—1717. 

48. Stroud, R. M., and E. B. Fauman. 1995. Significance of structural     changes in proteins: expected errors in refined protein structures.     Protein Sci. 4:2392—2404. 

49. Carugo, O., and P. Argos. 1998. Accessibility to internal cavities and     ligand binding sites monitored by protein crystallographic thermal     factors. Proteins. 31:201—213. 

50. Yuan, Z., J. Zhao, and Z. X. Wang. 2003. Flexibility analysis of enzyme     active sites by crystallographic temperature factors. Protein Eng.     16:109—114. 

51. Mohan, S., N. Sinha, and S. J. Smith-Gill. 2003. Modeling the binding     sites of anti-hen egg white lysozyme antibodies HyHEL-8 and HyHEL-     26: an insight into the molecular basis of antibody cross-reactivity and     specificity. Biophys. J. 85:3221—3236. 

52. Carugo, O., and P. Argos. 1997. Correlation between side chain mobility     and conformation in protein structures. Protein Eng. 10:777—787. 

53. Eyal, E., R. Najmanovich, ., V. Sobolev. 2003. Protein side-chain     rearrangement in regions of point mutations. Proteins. 50:272—282. 

54. Carugo, O., and P. Argos. 1997. Protein-protein crystal-packing     contacts. Protein Sci. 6:2261—2263. 

55. Altman, R., C. Hughes, ., O. Jardetsky. 1994. Compositional charac-     teristics of relatively disordered regions in proteins. Protein Pept. Lett.     1:120—127. 

56. Romero, P., Z. Obradovic, ., A. K. Dunker. 1997. Identifying disor-     dered regions in proteins from amino acid sequence. The 1997 IEEE     International Conference on Neural Networks Proc, Houston, TX.     1:90—95. 

57. Romero, P., Z. Obradovic, ., A. K. Dunker. 1998. Thousands of     proteins likely to have long disordered regions. Pac. Symp. Biocomput.     3:437—448. 

58. Radivojac, P., Z. Obradovic, ., A. K. Dunker. 2004. Protein flexibility     and intrinsic disorder. Protein Sci. 13:71—80. 

59. Navizet, I., R. Lavery, and R. L. Jernigan. 2004. Myosin flexibility:     structural domains and collective vibrations. Proteins. 54:384—393. 

60. Kuriyan, J., and W. I. Weis. 1991. Rigid protein motion as a model for     crystallographic temperature factors. Proc. Natl. Acad. Sci. USA.     88:2773—2777. 

61. Frauenfelder, H., G. A. Petsko, and D. Tsernoglou. 1979. Temperature-     dependent x-ray diffraction as a probe of protein structural dynamics.     Nature. 280:558—563. 

62. Chong, S. H., Y. Joti, ., F. Parak. 2001. Dynamical transition of     myoglobin in a crystal: comparative studies of x-ray crystallography     and Mo ̈ssbauer spectroscopy. Eur. Biophys. J. 30:319—329. 

63. Berjanskii, M., and D. S. Wishart. 2006. NMR: prediction of protein     flexibility. Nat. Protoc. 1:683—688. 

64. Berjanskii, M. V., and D. S. Wishart. 2007. The RCI server: rapid and     accurate calculation of protein flexibility using chemical shifts. Nucleic     Acids Res. 35(Web Server issue):W531—W537. 

65. Berjanskii, M. V., and D. S. Wishart. 2008. Application of the random     coil index to studying protein flexibility. J. Biomol. NMR. 40:31—48. 

66. McKnight,C. J., P. T. Matsudaira, andP. S. Kim.1997.NMRstructure of     the 35-residue villin headpiece subdomain. Nat. Struct. Biol. 4:180—184. 

67. Eliezer, D., P. A. Jennings, ., H. Tsuruta. 1995. The radius of gyration     of an apomyoglobin folding intermediate. Science. 270:487—488. 

68. Bright, J. N., T. B. Woolf, and J. H. Hoh. 2001. Predicting properties     of intrinsically unstructured proteins. Prog. Biophys. Mol. Biol. 76:     131—173. 

69. Knott, M., and H. S. Chan. 2006. Criteria for downhill protein folding:     calorimetry, chevron plot, kinetic relaxation, and single-molecule radius     of gyration in chain models with subdued degrees of cooperativity.     Proteins. 65:373—391. 

70. Flory, P. J. 1989. Statistical Mechanics of Chain Molecules. Hanser     Publishers, New York. 

71. Qiu, D., P. S. Shenkin, ., W. C. Still. 1997. The GB/SA continuum     model for solvation. A fast analytical method for the calculation of     approximate Born radii. J. Phys. Chem. 101:3005—3014. 

72. Andersen, H. C. 1983. Rattle—a velocity version of the shake algorithm     for molecular-dynamics calculations. J. Comput. Phys. 52:24—34. 

73. Jorgensen, W. L., and J. Tiradorives. 1988. The Opls potential functions     for proteins - energy minimizations for crystals of cyclic-peptides and     crambin. J. Am. Chem. Soc. 110:1657—1666. 

74. Zagrovic, B., C. D. Snow, ., V. S. Pande. 2002. Native-like mean     structure in the unfolded ensemble of small proteins. J. Mol. Biol.     323:153—164. 

75. Lindahl, E., B. Hess, and D. van der Spoel. 2001. GROMACS 3.0:     a package for molecular simulation and trajectory analysis. J. Mol.     Model. 7:306—317. 

76. McLachlan, A. D. 1982. Rapid comparison of protein structures. Acta     Crystallogr. A. 38:871—873. 

870 Kuzmanic and Zagrovic 

77. Furnham, N., T. L. Blundell, ., T. C. Terwilliger. 2006. Is one solution     good enough? Nat. Struct. Mol. Biol. 13:184—185, discussion 185. 

78. Wang, X., and J. Snoeyink. 2006. Multiple structure alignment by     optimal RMSD implies that the average structure is a consensus.     LSS Computational Systems Bioinformatics Conference, Stanford, CA.     79—87. 

79. Bu ̈rgi, R., J. Pitera, and W. F. van Gunsteren. 2001. Assessing the effect     of conformational averaging on the measured values of observables.     J. Biomol. NMR. 19:305—320. 

80. Zagrovic, B., and W. F. van Gunsteren. 2006. Comparing atomistic     simulation data with the NMR experiment: how much can NOEs     actually tell us? Proteins. 63:210—218. 

81. Joosten, R. P., T. Womack, ., G. Bricogne. 2009. Re-refinement from     deposited x-ray data can deliver improved models for most PDB entries.     Acta Crystallogr. D Biol. Crystallogr. 65:176—185. 

82. Nabuurs, S. B., A. J. Nederveen, ., C. A. Spronk. 2004. DRESS:     a database of REfined solution NMR structures. Proteins. 55:483—486. 

83. Joosten, R. P., and G. Vriend. 2007. PDB improvement starts with data     deposition. Science. 317:195—196. 

84. van Gunsteren, W. F., J. Dolenc, and A. E. Mark. 2008. Molecular simu-     lation as an aid to experimentalists. Curr. Opin. Struct. Biol. 18:149—153. 

85. Humphrey, W., A. Dalke, and K. Schulten. 1996. VMD: visual molec-     ular dynamics. J. Mol. Graph. Model. 14:33—38. 

Determination of Average RMSD from B-Factors 871 



---

# Relation between native ensembles and experimental structures of proteins

**Authors:** Robert B. Best, Kresten Lindorff-Larsen, Mark A. DePristo, Michele Vendruscolo
**Year:** 2006
**Venue:** Proceedings of the National Academy of Sciences
**DOI:** 10.1073/pnas.0511156103
**Source PDF URL:** https://europepmc.org/articles/PMC1544146?pdf=render
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

## Relation between native ensembles and experimental 

## structures of proteins 

**Robert B. Best*†, Kresten Lindorff-Larsen‡, Mark A. DePristo§, and Michele Vendruscolo*** 

*Department of Chemistry, Cambridge University, Lensfield Road, Cambridge CB2 1EW, United Kingdom; ‡Department of Biochemistry, Institute of Molecular Biology and Physiology, University of Copenhagen, Universitetsparken 13, DK-2100 Copenhagen fl, Denmark; and §Department of Organismic and Evolutionary Biology, Harvard University, 16 Divinity Street, Cambridge, MA 02138 

Edited by Axel T. Brunger, Stanford University, Stanford, CA, and approved June 5, 2006 (received for review December 23, 2005) 

**Different experimental structures of the same protein or of proteins with high sequence similarity contain many small variations. Here we construct ensembles of ‘‘high-sequence similarity Protein Data Bank’’ (HSP) structures and consider the extent to which such ensembles represent the structural heterogeneity of the native state in solution. We find that different NMR measurements probing structure and dynamics of given proteins in solution, including order parameters, scalar couplings, and residual dipolar couplings, are remarkably well reproduced by their respective high-sequence similarity Protein Data Bank ensembles; moreover, we show that the effects of uncertainties in structure determination are insufficient to explain the results. These results highlight the importance of accounting for native-state protein dynamics in making comparisons with ensemble-averaged experimental data and suggest that even a modest number of structures of a protein determined under different conditions, or with small variations in sequence, capture a representative subset of the true native-state ensemble.** 

NMR order parameters protein dynamics residual dipolar couplings 

# T 

he rapidly growing Protein Data Bank (PDB) (1) is testament to the revolution in structural biology that has occurred over the last 15 years. These newly available protein structures contain a wealth of information that can be used to rationalize and predict the function of proteins. At the same time, however, it has long been realized that native states are best represented as ensembles of similar structures and that the dynamics of proteins are also important for understanding their function (2–5). NMR spectroscopy (4, 6), which can reveal protein dynamics in atomic detail, is thus being applied to characterize protein stability and the effect of mutations (7), the changes upon ligand binding (5, 8, 9), the comparison of homologous proteins (10), and the structure of unfolded states (11). A number of recent studies have analyzed the extent to which the dynamical information is represented by existing protein structures, with the aim of predicting experimental data on dynamics from single structures, using relatively simple models based on structural properties. The prediction of properties arising from essentially harmonic dynamics, such as x-ray crystallographic _B_ -factors (12) and NMR order parameters for the protein backbone (13), has been reasonably successful using contact-based models or normal mode analysis. However, side-chain order parameters, which depend in many cases on anharmonic dynamics (14, 15), have proved more challenging, because they exhibit only limited correlations with structural properties, such as contact density and the solventaccessible surface area (16). Improved prediction has been achieved by combining a contact model with the number of rotatable bonds in the side chain (17). Here we investigate the extent to which the diversity present within different structures of the same protein, or proteins with high sequence identity, in the PDB captures the structural diversity probed by experiments in solution: these different structures arise from the crystallization of mutants, variants from different species, structures of complexes with other biomolecules or drugs, or use of 

 different crystallization conditions. We refer to these structures as ‘‘high-sequence similarity PDB’’ (HSP) ensembles. Because sidechain order parameters, scalar couplings, and residual dipolar couplings (RDCs) report directly on the structural heterogeneity of the native state, it is important to investigate whether these parameters are related to the heterogeneity of HSP ensembles. A recent study by Zoete et al. (18) compared backbone ‘‘fluctuations’’ derived from the different structures of the HIV-1 protease in the PDB with the x-ray B -factors, and multiple crystal structures of T4 lysozyme were analyzed by Matthews and coworkers (19). We compare the properties of HSP ensembles with experimental NMR data describing the structural heterogeneity present in solution, rather than in the crystalline state. Particularly interesting is the comparison of side-chain dynamics data with HSP ensembles, because the motions of atoms in the amino acid side chains are significantly more complex and varied than those in the polypeptide backbone (15). 

 Results NMR Order Parameters from HSP Ensembles. Order parameters of side-chain methyl groups are a sensitive probe of local side-chain motions (6). Specifically, they measure the amplitude of the orientational distribution of the methyl group axis within a reference frame attached to the protein (i.e., excluding overall rotational diffusion of the molecule) on a picosecond to nanosecond time scale (20). One method of generating such a distribution for comparison with experiment is by performing molecular dynamics (MD) simulations (21). By aligning each simulation snapshot with a reference set of coordinates to remove the orientational contribution from molecular diffusion, order parameters may be calculated from the intramolecular variations in orientation. We apply an analogous approach to the HSP ensembles, which are made up of structures with high sequence similarity drawn from the PDB. For example, Fig. 1 shows two Leu side chains taken from such an ensemble for ubiquitin, where the order parameters measure the extent of motion of the C—Cbond. A larger-order parameter generally corresponds to more restricted intramolecular motion. The idea behind the HSP ensembles is that small differences in sequence or crystal environment act as perturbations that cause the protein to populate alternate minima (5, 18, 22, 23); too many differences in sequence would make the comparison meaningless, because the structure also would diverge (24). In practice, for most of the proteins in the HSP ensembles that we considered, the structural alignments have sequence identity of 98% (see Table 1), corresponding to only one or two point mutations in each case. 

 Conflict of interest statement: No conflicts declared. This paper was submitted directly (Track II) to the PNAS office. Abbreviations: PDB, Protein Data Bank; HSP, high-sequence similarity PDB; MD, molecular dynamics; RDC, residual dipolar coupling; rmsd, rms deviation. †To whom correspondence should be sent at the present address: Laboratory of Chemical Physics, National Institute of Diabetes and Digestive and Kidney Diseases, National Institutes of Health, Bethesda, MD 20892-0520. E-mail: best@helix.nih.gov. © 2006 by The National Academy of Sciences of the USA 

[http://www.pnas.orgcgidoi10.1073pnas.0511156103](http://www.pnas.orgcgidoi10.1073pnas.0511156103) PNAS  **July 18, 2006**  vol. 103  no. 29  **10901–10906** 

 BIOPHYSICS 

Because too few structures may not adequately represent the native state heterogeneity, we required at least 10 matches to be found. The side-chain order parameters calculated from the HSP ensembles are plotted in Fig. 2, together with experimental values obtained from deuterium relaxation experiments. There is generally a remarkably good agreement between the experimental and calculated data, given the acknowledged difficulty of quantitatively predicting these data (16, 17, 26), especially for the larger-sized ensembles (e.g., HIV-1 protease). Table 1 summarizes the correlation and rms deviation (rmsd) between experimental and calculated data. We favor the rmsd as a measure of similarity, because some proteins tend to have higher correlations simply because of their residue composition (15). We assess the significance of the results by comparing them to a model in which ‘‘synthetic’’ data sets are generated by drawing order parameters for each residue at random from a pool of real experimental data for that residue type. The model accounts for residue identity but not structural context. From a large number of synthetic data sets, we calculate the probability that a rmsd as good as that obtained from the HSP ensemble could be obtained by using this model: for all proteins this probability is 1%, with the exception of Fyn SH3 and Cdc42Hs where it is 10%. 

Effect of Experimental Uncertainty and Ensemble Size. Variations within the HSP ensembles could come from real differences between the structures, as well as from experimental uncertainty. We use HIV-1 protease (which has the largest HSP ensemble) to 

 investigate the origin of these variations, by comparing order parameters calculated for various structural ensembles of this protein (Fig. 3). A good correlation between the full HSP ensemble and experimental deuterium relaxation data is found (Fig. 3 a ; rmsd 0.17 Å, r p 0.76); for reference, two different experimental data sets (from carbon and deuterium relaxation) are compared in Fig. 3 b (rmsd 0.10 Å, r p 0.94). Degeneracy in the solution of crystal structures has been shown to give local variations of up to 2.0 Å in the refined solutions of HIV-1 protease x-ray diffraction data (27). This contribution to the order parameters may be quantified by calculating order parameters from the model structures. An ensemble of 50 plausible initial structures, generated by the RAPPER procedure (27), gives order parameters that are generally much lower than experiment (Fig. 3 c ). Despite this large variation allowed in the initial structures, refinement against the x-ray data produced an ensemble whose order parameters were much higher than experiment (Fig. 3 d ); therefore, the small degeneracy in solutions underestimates the true variability. The variability within NMR ensembles is similarly related both to the local density of restraints and to true dynamics (28). We find that side-chain order parameters calculated over the NMR ensemble of HIV-1 protease are poorly correlated with the experimental data (Fig. 3 e ; rmsd 0.34 Å; r p 0.13). Similar results are obtained when this same approach is applied to other proteins for which both NMR ensembles with at least 10 members and side-chain order parameters have been determined. The correlations are given in Table 1 and, where there is a corresponding HSP ensemble, are plotted in Fig. 2. Although the correlations vary somewhat from protein to protein, the rmsds from experimental data are consistently better for the HSP ensembles than the NMR ensembles. The data in Table 1 suggest that larger HSP ensemble sizes tend to give more accurate results. We test this hypothesis by calculating both backbone and side-chain order parameters over randomly selected subensembles of the HIV-1 protease HSP ensemble (Fig. 3 f ). An increase in the ensemble size indeed improves the agreement with experiment. Furthermore, although there is little improvement for the backbone order parameters beyond 2 structures and almost none beyond 5, a larger number of structures (20–40) is necessary to capture the side-chain heterogeneity (Fig. 3 f ). The limited improvement beyond 40 structures indicates that the approximations inherent in comparing HSP structures will eventually limit the agreement with experiment. Chou et al. (14) have shown that even a small population of a minor rotamer, e.g., 10%, can have a significant effect on the calculated S 2 value, such that 

**Fig. 1.** Leu side chains from the ubiquitin HSP ensemble with -methyl order parameters of 0.7 (L50) ( _a_ ) and 0.2 (L8) ( _b_ ). 

 Table 1. Comparison between experimental side-chain order parameters and those calculated from HSP and NMR ensembles 

 Protein 

 HSP ensembles NMR ensembles SI,* % Size, Å r p†^ rmsd, Å Structure Size, Å r p†^ rmsd, Å 

 Cdc42Hs 98.3 13 0.53 0.30 1AJE 20 0.11 0.39 HIV-1 Protease 92.1 330 0.74 0.17 1BVE 28 0.13 0.34 Ubiquitin 99.2 13 0.76 0.18 1D3Z 10 0.57 0.29 Eglin c 99.0 10 0.37 0.30 1EGL 25 0.46 0.31 Calmodulin 99.8 28 0.72 0.20 3CLN 25 0.40 0.27 A-LBP 99.4 14 0.73 0.19 Troponin C 98.9 13 0.69 0.19 Fyn SH3 99.7 12 0.74 0.21 FNfn10 1TTF 36 0.50 0.30 PLCC SH2 2PLE 18 0.36 0.32 M-FABP 1G5W 20 0.41 0.35 Average 98.3 0.66 0.22 0.37 0.32 See ref. 25 for more details on experimental side-chain order parameters. *Percentage sequence identity in HSP ensemble.†Pearson correlation coefficient. 

**10902**  [http://www.pnas.orgcgidoi10.1073pnas.0511156103](http://www.pnas.orgcgidoi10.1073pnas.0511156103) Best _et al._ 

ensembles of 20–40 structures might be needed to get sufficient statistical sampling of such minor conformations. We note that restricting the HSP ensemble to consensus sequence structures (49 for HIV-1 protease) does not appreciably change the agreement with experiment, justifying the inclusion of mutants in the ensembles. Although mutants may shift the equilibrium between two free energy minima, the structure selection criteria for HSP ensembles would tend to find structures within the same basin. 

Scalar Couplings and Rotamer Populations. Side-chain scalar couplings report on the 1 dihedral angle and its associated dynamics and provide complementary information to that given by the order parameters. We have back-calculated side-chain scalar couplings from the HSP ensemble of HIV-1 protease, using a recent parameterization of the Karplus equation (14). There is a good correlation with experiment for both NC ( _r_ p 0.90) and CC ( _r_ p 0.96) scalar couplings (see Figs. 6 and 7, which are published as supporting information on the PNAS web site). Notably, the scalar couplings for individual structures vary over a wide range for some residues, whereas the mean values are generally close to experiment. To illustrate this point, we note that although the correlation between calculated scalar couplings and experiment for each structure ranges from 0.19 to 0.94 (mean 0.75) for NC couplings, and from 0.28 to 0.97 (mean 0.88) for CC couplings, the correlation obtained for an average over the whole ensemble is as good as that obtained 

 from the best individual structures. This result is in agreement with the earlier finding that the fitting of the parameters in the Karplus equation using individual crystal structures is likely to be inaccurate (14, 29). The agreement between experimental scalar couplings and those from the HSP ensemble suggests that the latter may be representative of the dihedral angle distribution in solution. We compared the dihedral angle distributions determined independently from RDCs (14) and the dynamic ensemble refinement (DER) method (30) with those calculated from the HSP ensemble of ubiquitin (Fig. 4): comparable results are obtained by using each method (see Table 2, which is published as supporting information on the PNAS web site, for a complete comparison). 

 RDCs. Of the proteins for which RDCs have been measured, hen lysozyme has the largest HSP ensemble (177 structures); the RDCs have been incorporated in a refined structure of the protein (31). We separately fitted each structure in the ensemble to the experimental backbone NH RDCs and also calculated an ensemble average as described (30). The Q -factor [a goodness-of-fit measure for RDCs (32, 33); low Q indicates better agreement] is plotted for each fit in Fig. 5 a. Although the Q -factor for the HSP ensemble (solid line in Fig. 5 a ) is not as low as that for the structure determined by using dipolar 

**Fig. 2.** Methyl group side-chain order parameters, _S_ axis^2 , calculated over HSP ensembles (red lines) and NMR ensembles (blue lines) compared with experimental data (shaded black curves). The number of structures in the HSP and NMR ensembles are reported next to the name of the protein. Data for calmodulin and troponin C correspond to the N-terminal lobe only. The methyl group index on the _x_ -axis is obtained by sorting in increasing order of residue number and methyl number (e.g.,  1 2). 

 Fig. 3. Methyl axis order parameters ( S axis^2 ) for HIV-1 protease. ( a – e ) The following sets of S axis^2 are compared with those determined from 2H relaxation experiments. ( a ) S axis^2 calculated from HSP ensembles. ( b ) A separate set of experimental S axis^2 from 13C relaxation. ( c and d ) S axis^2 from ensembles of 50 structures generated by the RAPPER algorithm (27) before ( c ) and after ( d ) refinement against x-ray data. ( e ) S axis^2 calculated from the NMR ensemble (PDBIDcode1BVE).Solidlinescorrespondtoidealcoincidenceofthetwodata sets; broken lines indicate 0.2 from this value. Data points are color-coded by methyl type as follows: black, Leu 1,2; red, Val 1,2; green, Ile 2; blue, Ile 1; orange, Ala . ( f ) rmsd between HSP and experimental order parameters as a function of HSP ensemble size. 

Best _et al._ PNAS  **July 18, 2006**  vol. 103  no. 29  **10903** 

 BIOPHYSICS 

couplings as restraints (broken line in Fig. 5 _a_ ), it is significantly better than any single experimental structure refined without the couplings. We note that there are a number of remaining outliers that probably indicate real differences between the crystallographic and solution structures (31). Thus, the experimental data can be well reproduced either by a single structure (as for PDB ID code 1E8L) or by an ensemble in which few of the structures are particularly good fits. A similar result was obtained for both backbone and side-chain RDCs in ubiquitin, although with poorer statistics because of the small HSP ensemble (data not shown). To probe the origin of this effect, we have used a harmonic model, derived from the minimized structure in the EEF1 force field (34). An ensemble of 200 structures at a temperature of 300 K was generated by random superposition of normal modes. As for the HSP ensemble, we find that the ensemble average fit to the data are much better than any individual structure (Fig. 5 _b_ ); thus, harmonic fluctuations can give rise to significant deviation of individual structures from the RDCs. 

Discussion 

HSP Ensemble. We have shown that several types of experimental NMR data related to dynamics and structural heterogeneity in the native state can be reproduced by using ensembles of structures of the same protein (or proteins of high sequence similarity) drawn from the PDB. The heterogeneity of such ensembles is similar to that found by MD simulation [average rmsd of 0.91 Å (backbone), 1.50 Å (side chain), 1.24 Å (all-atom)], although in MD the NMR data are often less accurately reproduced (15, 35). These results suggest that the HSP ensemble provides a representative sample of the structural fluctuations of a protein under native conditions, although the available structures only constitute a small fraction of the full native ensemble. The HSP analysis can 

 be related to the fluctuation–dissipation theorem, according to which the equilibrium structural fluctuations are equivalent to the changes caused by small perturbations (22). One can consider each structure in the HSP ensemble as subject to a slightly different perturbation, such as a bound ligand, a mutation, or the effect of crystal packing, which favors a particular minimum on the nativestate energy surface (5, 18, 23). If the perturbations are sufficiently random, the resulting ensemble will be representative of the full ensemble; for example, if some property of the protein, e.g., a bond vector orientation or a side-chain rotamer, is found in a certain fraction of the native energy minima, then it will be found with the same fraction in a sufficiently large randomly selected subset. The quantitative comparison that we present between different experimental structures is complicated by many factors, such as differences in the methodology used (x-ray crystallography vs. NMR spectroscopy) and the inherent uncertainties in each structure due to differences in disorder (x-ray) (27, 36) and density of restraints (NMR) (30). Structural uncertainty will tend to obscure the observed correlations: for example, the HIV-1 protease HSP ensemble of high resolution (better than 1.85 Å) structures improves the agreement with experimental NMR data by 15% with respect to the HSP ensemble of low resolution (2.6 Å or worse; see Table 3, which is published as supporting information on the PNAS web site). Also, the so-called ‘‘model bias’’ (37) resulting from techniques such as molecular replacement in the solution of x-ray structures may be responsible for the poorer agreement in some of the smaller HSP ensembles. For the consensus sequence HIV-1 protease structures, elimination of structures determined by molecular replacement slightly improves the correlation with experimental order parameters, from 0.72 to 0.75. In certain cases, even single point mutations may have a significant impact on structure. This effect also may contribute to the relatively poor agreement with experiment for Eglin c, because changes in experimental side-chain order parameters upon mutation are relatively large (38). For x-ray structures, crystal packing artifacts also will distort 

 Fig. 5. Distributions of RDC Q -factors for fits to NH RDCs from hen lysozyme (31). ( a ) Q factors for fits of individual HSP ensemble members to experimental RDCs. The solid line indicates the fit obtained from an ensemble average and the broken line the fit for the first member of the PDB ID code 1E8L NMR ensemble. ( b ) Q -factors for fits to structures generated from random normal mode displacements at 300 K to a set of synthetic RDCs derived from the minimum energy structure. Solid lines shows the Q -factors for RDCs ensembleaveraged over this set of structures. 

**Fig. 4.** 1 rotamer populations for representative residues in ubiquitin. Fractional populations calculated from RDCs (solid) (14) and from dynamic ensemble refinement (DER; hatched) (30) are compared. Full results are available in Table 2. 

**10904**  [http://www.pnas.orgcgidoi10.1073pnas.0511156103](http://www.pnas.orgcgidoi10.1073pnas.0511156103) Best _et al._ 

the protein energy landscape to some extent with respect to that in solution. The above reasons may all contribute to the observed rmsd between experimental and calculated side-chain order parameters and explain why the rmsd does not decrease significantly on increasing the size of the HIV-1 protease HSP ensemble beyond 40 (Fig. 3 _f_ ). Nonetheless, the fact that the HSP ensembles are close to the experimental data strongly suggests that the differences between crystal structures are largely due to the actual heterogeneity in the native state. HSP ensembles do not directly include the concept of time. NMR measurements, however, correspond to averaging over the states accessed on a particular time scale, from picoseconds to nanoseconds in the case of order parameters. Agreement of order parameters calculated over HSP ensembles with those from NMR relaxation measurements suggests that each side chain samples most of its conformers on a nanosecond time scale. This observation is in harmony with the finding that order parameters calculated from relaxation measurements (averaged over a picosecond–nanosecond scale) are in most cases similar to those calculated from RDCs and scalar couplings (averaged over a microsecond–millisecond scale) (14). 

NMR Order Parameters. The limited improvement that we found in the agreement with experimental backbone order parameters for more than two HSP structures is consistent with the result that an ensemble size of two is sufficient for the refinement of structures against backbone RDCs (39–41). It should be noted, however, that the accuracy of our backbone order parameter calculations may be adversely affected by the absence of hydrogen atoms in most crystal structures, requiring them to be built with standard geometries. Further, energy minimization during experimental refinement procedures will tend to reduce the vibrational contribution to backbone amide order parameters (42), as was found when ensemble-refined ubiquitin structures were minimized (30). Our results indicate that an ensemble size of 20 is required to represent side-chain heterogeneity (represented by order parameters for side-chain methyl groups), as we have also found independently in the application of the dynamic ensemble refinement method to ubiquitin (30). This result is also expected from the greater complexity of side-chain dynamics (15). Given the redundancy in the PDB, this minimum ensemble size suggests that the present approach may be applicable to several proteins, especially those of particular biological interest for which more structures are likely to be determined. We do not suggest that the native state of a protein comprises 20 local minima [e.g., MD simulations (23) and the HIV-1 protease HSP ensemble suggest a much larger number]. Rather, this number seems to provide sufficient heterogeneity to determine order parameters and related quantities that are sensitive to local motions. In principle, sufficiently large HSP ensembles may be used to investigate structural correlations (e.g., covariance of fluctuations; see Fig. 8 and Table 4, which are published as supporting information on the PNAS web site) and could be compared with experiments that probe long-range correlations. 

RDCs. We have found that an ensemble of different experimental structures of the same protein fits backbone RDCs better than any single structure, apart from the one determined by using the couplings as restraints. This result is important given the increasing use of RDCs in structure refinement and structure validation (43), because the quality of a single structure is often assessed by the goodness of fit to the RDC data. In the context of structure refinement, RDC-based backbone restraints are usually imposed on a single copy [although ensemble refinement has also been used (39, 41)], whereas the experimental data represent an ensemble average. A good example of the type of effects resulting from this procedure is provided by the NMR structure of carbonmonoxy 

 hemoglobin, for which the experimental solution structure determined with a single copy was found to be intermediate between two different crystal structures (44). In many cases, excluding situations such as that of the allosteric hemoglobin, which is known to populate several alternative structures (45), this effect should not result in a significant problem for structure refinement of the backbone, especially if one assumes that the structure remains essentially confined within a single energy minimum and that backbone motions are mainly harmonic in nature. If structures derived from a random superposition of normal mode displacements at 300 K are fitted to a set of synthetic RDCs generated from the minimum (average) structure, the Q -factors range from 0.2 to 0.5 for individual structures Fig. 5 b. However, the ensemble fits very well ( Q 0.07) to the data for the minimum structure, except that the dynamics is absorbed into the alignment tensor, scaling it by a factor of 0.92; a similar effect was found in an analysis of MD simulations (46). In this case, using ensemble-averaged RDCs as restraints in a single copy refinement would result in an ‘‘average’’ structure. It is unlikely, however, that such refinement will be successful for modeling side-chain motion, which is known to be dominated by anharmonic effects such as the population of multiple rotameric states (15). 

 Applications of HSP Ensembles. The results that we discussed so far for HSP ensembles suggest an alternative way to parameterize semiempirical relations such as Karplus equations for scalar couplings. The parameterization of these expressions using a number of experimental structures of different proteins has been complicated by the need to account for the effects of dynamics in solution. Methods for addressing this issue include structure-independent cross-validation approaches (14) or dynamic ensemble refinementderived structures (29). Alternatively, comprehensive experimental data sets determined for those proteins for which a very large number of structures are already available can be used in an ensemble-averaged fitting procedure, in which the effects of heterogeneity are included and specific packing effects are expected to be reduced. HSP ensembles also may be useful for drug design calculations. An emerging view is that the bound state of the protein is found within the equilibrium ensemble of the free protein; otherwise, very strong interactions with the drug would be required to offset the cost of adopting such an unfavorable conformation. An increasing amount of experimental evidence, such as the recognition of dissimilar ligands (47) and the enhancement of antibody affinity and specificity by making the unbound state more similar to the bound state (5), supports such a model. The use of ‘‘dynamic’’ pharmacophore models in such calculations has already led to improved results (48); these models have been derived from either MD (48) or several crystal structures chosen in a similar way to the HSP ensembles (49). Hence, HSP ensembles or ensemble-refined experimental structures (30) represent a possible alternative to MD simulations for the purpose of ensemble generation. Conversely, if the bound state corresponds to a different free energy minimum with a different structure, it may not be sampled by this method. 

 Conclusions We have studied the properties of ensembles of structures of proteins with high sequence identity in the PDB and found that they provide a representative sampling of the heterogeneity of protein native states, as probed by various NMR measurements. In particular, these HSP ensembles reproduce side-chain order parameters better than ensembles of NMR structures and also fit RDC data better than individual structures, supporting the view that dynamic heterogeneity is an important contribution to such data. Therefore, the assessment of individual structures using ensemble-averaged experimental measurements requires some caution. 

Best _et al._ PNAS  **July 18, 2006**  vol. 103  no. 29  **10905** 

 BIOPHYSICS 

The present work indicates that it is important to account for the structural diversity of the native state when comparing predictions from homology modeling or _ab initio_ structure predictions with experimental structures and perhaps even that such a diversity is incorporated into the solutions obtained from these calculations. Together, our results suggest that the population of closely related structures that form the native state of a protein and often determine its functionality can be sampled not only by probing the dynamics experimentally, but also by using multiple structure determinations of proteins of highly similar sequences. 

Methods 

Selection of Experimental Data. HSP ensembles were constructed for a previously compiled set of proteins for which both experimental order parameters and structures are available (25), as well as hen lysozyme. For each of these proteins, a search for structural homologues in the PDB with 90% sequence identity and ungapped alignment was performed by using the combinatorial extension (CE) algorithm (50). If at least 10 matches were found, those structures were defined as the HSP ensemble for that protein. In crystal structures where several structurally homologous chains were present in the asymmetric unit and were refined independently, each protein was separately entered into the ensemble. For NMR structures only the minimized average structure was used. For HIV-1 protease, the database was constructed from the online HIV protease structure database (51). Tethered dimers, structures with unresolved disordered residues, low

 resolution structures, computational models, and structures not submitted to the PDB were excluded. In addition, only structures with 10 mutations relative to the consensus were allowed. A complete list of the structures used is available in Tables 5 and 6, which are published as supporting information on the PNAS web site. 

 NMR Order Parameter and Dipolar Coupling Calculations. The HSP ensembles were aligned to the protein studied in the NMR dynamics experiment by least-squares fitting of the corresponding carbons from the combinatorial extension (CE) alignments (all alignments were ungapped because of the high sequence similarity). Order parameters (20) for each methyl group were calculated as described (15), by using all structures in the HSP ensemble having the same type of residue in that position as the reference protein studied in the NMR dynamics experiments. The calculation of order parameters for the NMR structures was done in the same way as for the HSP ensembles. RDCs and scalar couplings were calculated from the aligned ensembles of structures as described (30). Normal mode analysis was performed with the CHARMM package (52) and the EEF1 force field (34). 

 We thank Arthur Lesk for helpful comments on the manuscript and Cyrus Chothia for discussions. M.V. is a Royal Society University Research Fellow. R.B.B. and M.V. were supported by a grant from the Leverhulme Trust. K.L.-L. was supported by the Danish Research Agency and a European Molecular Biology Organization Long-Term Fellowship. M.A.D. is a Damon Runyon Fellow supported by Damon Runyon Cancer Research Foundation Grant DRG-1861-05. 

1. Berman, H. M., Battistuz, T., Bhat, T. N., Bluhm, W. F., Bourne, P. E.,     Burkhardt, K., Feng, Z., Gilliland, G. L., Iype, L., Jain, S., _et al._ (2002) _Acta_     _Crystallogr. D_ **58,** 899–907. 

2. Karplus, M. & McCammon, J. A. (2002) _Nat. Struct. Biol._ **9,** 646–652. 

3. Wand, A. J. (2001) _Nat. Struct. Biol._ **8,** 926–931. 

4. Palmer, A. G., III (2004) _Chem. Rev._ **104,** 3623–3640. 

5. Eisenmesser, E. Z., Millet, O., Labeikovsky, W., Korzhnev, D. M., Wolf-Watz,     M., Bosco, D. A., Skalicky, J. J., Kay, L. E. & Kern, D. (2005) _Nature_ **438,**     117–121. 

6. Kay, L. E. (2005) _J. Magn. Reson._ **173,** 193–207. 

7. Mittermaier, A. & Kay, L. E. (2004) _Protein Sci._ **13,** 1088–1099. 

8. Kay, L. E., Muhandiram, D. R., Wolf, G., Shoelson, S. E. & Forman-Kay, J. D.     (1998) _Nat. Struct. Biol._ **5,** 156–163. 

9. Chaykovski, M. M., Bae, L. C., Cheng, M.-C., Murray, J. H., Tortolani, K. E.,     Zhang, R., Seshadri, K., Findlay, J. H. B. C., Hsieh, S.-Y., Kalverda, A. P., _et_     _al._ (2003) _J. Am. Chem. Soc._ **125,** 15767–15771. 

10. Best, R. B., Rutherford, T. J., Freund, S. M. V. & Clarke, J. (2004) _Biochemistry_     **43,** 1145–1155. 

11. Klein-Seetharaman, J., Oikawa, M., Grimshaw, S. B., Wirmer, J., Duchardt, E.,     Ueda, T., Imoto, T., Smith, L. J., Dobson, C. M. & Schwalbe, H. (2002) _Science_     **295,** 1719–1722. 

12. Halle, B. (2002) _Proc. Natl. Acad. Sci. USA_ **99,** 1274–1279. 

13. Zhang, F. & Bru ̈schweiler, R. (2002) _J. Am. Chem. Soc._ **124,** 12654–12655. 

14. Chou, J. J., Case, D. A. & Bax, A. (2003) _J. Am. Chem. Soc._ **125,** 8959–8966. 

15. Best, R. B., Clarke, J. & Karplus, M. (2004) _J. Mol. Biol._ **349,** 185–203. 

16. Mittermaier, A., Kay, L. E. & Forman-Kay, J. D. (1999) _J. Biomol. NMR_ **13,**     181–185. 

17. Ming, D. & Bru ̈schweiler, R. (2004) _J. Biomol. NMR_ **29,** 363–368. 

18. Zoete, V., Michielin, O. & Karplus, M. (2002) _J. Mol. Biol._ **315,** 21–52. 

19. Zhang, X. J., Wozniak, J. A. & Matthews, B. W. (1995) _J. Mol. Biol._ **250,**     527–552. 

20. Lipari, G. & Szabo, A. (1982) _J. Am. Chem. Soc._ **104,** 4546–4559. 

21. Lipari, G., Szabo, A. & Levy, R. M. (1982) _Nature_ **300,** 197–198. 

22. Chandler, D. (1987) _Introduction to Modern Statistical Mechanics_ (Oxford Univ.     Press, New York). 

23. Levy, R., Sheridan, R., Keepers, J., Dubey, G., Swaminathan, S. & Karplus, M.     (1985) _Biophys. J._ **48,** 509–518. 

24. Chothia, C. & Lesk, A. M. (1986) _EMBO J._ **5,** 823–826. 

25. Best, R. B., Clarke, J. & Karplus, M. (2004) _J. Am. Chem. Soc._ **126,** 7734–7735. 

26. Mittermaier, A., Davidson, A. R. & Kay, L. E. (2003) _J. Am. Chem. Soc._ **125,**     9004–9005. 

27. DePristo, M. A., de Bakker, P. I. W. & Blundell, T. L. (2004) _Structure (London)_     **12,** 831–838. 

28. Bonvin, A. M. J. J. & Bru ̈nger, A. T. (1995) _J. Mol. Biol._ **250,** 80–93. 

29. Lindorff-Larsen, K., Best, R. B. & Vendruscolo, M. (2005) _J. Biomol. NMR_ **32,**     273–280. 

30. Lindorff-Larsen, K., Best, R. B., DePristo, M. A., Dobson, C. M. & Vendr-     uscolo, M. (2005) _Nature_ **433,** 128–132. 

31. Schwalbe, H., Grimshaw, S. B., Spencer, A., Buck, M., Boyd, J., Dobson, C. M.,     Redfield, C. & Smith, L. J. (2001) _Protein Sci._ **10,** 677–688. 

32. Cornilescu, G., Marquardt, J. L., Ottiger, M. & Bax, A. (1998) _J. Am. Chem._     _Soc._ **120,** 6836–6837. 

33. Bax, A., Kontaxis, G. & Tjandra, N. (2001) _Methods Enzymol._ **339,** 127–174. 

34. Lazaridis, T. & Karplus, M. (1999) _Proteins_ **35,** 133–152. 

35. Prabhu, N. V., Lee, A. L., Wand, A. J. & Sharp, K. A. (2003) _Biochemistry_ **42,**     562–570. 

36. Ohlendorf, D. H. (1994) _Acta Crystallogr. D_ **50,** 808–812. 

37. Hodel, A. Kim, S. H. & Brunger, A. T. (1992) _Acta Crystallogr. A_ **48,** 851–858. 

38. Clarkson, M. W. & Lee, A. L. (2004) _Biochemistry_ **43,** 12448–12458. 

39. Clore, G. M. & Schwieters, C. D. (2004) _J. Am. Chem. Soc._ **126,** 2923–2938. 

40. Clore, G. M. & Schwieters, C. D. (2004) _Biochemistry_ **43,** 10678–10691. 

41. Clore, G. M. & Schwieters, C. D. (2006) _J. Mol. Biol._ **355,** 879–886. 

42. Buck, M. & Karplus, M. (1999) _J. Am. Chem. Soc._ **121,** 9645–9658. 

43. Prestegard, J. H., Bougault, C. M. & Kishore, A. L. (2004) _Chem. Rev._ **104,**     3519–3540. 

44. Lukin, J. A., Kontaxis, G., Simplaceanu, V., Yuan, Y., Bax, A. & Ho, C. (2003)     _Proc. Natl. Acad. Sci. USA_ **100,** 517–520. 

45. Perutz, M. F., Wilkinson, A. J., Paoli, M. & Dodson, G. G. (1998) _Annu. Rev._     _Biophys. Biomol. Struct._ **27,** 1–34. 

46. Meiler, J., Prompers, J. J., Peti, W., Griesinger, C. & Bru ̈schweiler, R. (2001)     _J. Am. Chem. Soc._ **123,** 6098–6107. 

47. Ma, B., Shatsky, M., Wolfson, H. J. & Nussinov, R. (2002) _Protein Sci._ **11,**     184–197. 

48. Carlson, H. A., Masukawa, K. M., Rubins, K., Bushman, F. D., Jorgensen,     W. L., Lins, R. D., Briggs, J. M. & McCammon, J. A. (2000) _J. Med. Chem._ **43,**     2100–2114. 

49. Carlson, H. A., Masukawa, K. M. & McCammon, J. A. (1999) _J. Phys. Chem._     _A_ **103,** 10213–10219. 

50. Shindyalov, I. N. & Bourne, P. E. (1998) _Protein Eng._ **11,** 739–747. 

51. Vondrasek, J. & Wlodawer, A. (2002) _Proteins_ **49,** 29–31. 

52. Brooks, B. R., Bruccoleri, R. E., Olafson, B. D., States, D. J., Swaminathan, S.     & Karplus, M. (1983) _J. Comp. Chem._ **4,** 187–217. 

**10906**  [http://www.pnas.orgcgidoi10.1073pnas.0511156103](http://www.pnas.orgcgidoi10.1073pnas.0511156103) Best _et al._ 



---

# Exploring Protein Dynamics Space: The Dynasome as the Missing Link between Protein Structure and Function

**Authors:** Ulf Hensen, Tim Meyer, Jürgen Haas, René Rex, Gert Vriend, Helmut Grubmüller
**Year:** 2012
**Venue:** PLoS ONE
**DOI:** 10.1371/journal.pone.0033931
**Source PDF URL:** https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0033931&type=printable
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

# Exploring Protein Dynamics Space: The Dynasome as the 

# Missing Link between Protein Structure and Function 

## Ulf Hensen1¤a, Tim Meyer1, Ju ¤rgen Haas1¤b, Rene ́^ Rex1¤c, Gert Vriend2, Helmut Grubmu¤ller1* 

1 Theoretische und computergestu¤tzte Biophysik, Max-Planck-Institut fu¤r biophysikalische Chemie, Go¤ttingen, Germany, 2 CMBI, Radboud University Nijmegen Medical Centre, Nijmegen, The Netherlands 

## Abstract 

 Proteins are usually described and classified according to amino acid sequence, structure or function. Here, we develop a minimally biased scheme to compare and classify proteins according to their internal mobility patterns. This approach is based on the notion that proteins not only fold into recurring structural motifs but might also be carrying out only a limited set of recurring mobility motifs. The complete set of these patterns, which we tentatively call the dynasome, spans a multidimensional space with axes, the dynasome descriptors, characterizing different aspects of protein dynamics. The unique dynamic fingerprint of each protein is represented as a vector in the dynasome space. The difference between any two vectors, consequently, gives a reliable measure of the difference between the corresponding protein dynamics. We characterize the properties of the dynasome by comparing the dynamics fingerprints obtained from molecular dynamics simulations of 112 proteins but our approach is, in principle, not restricted to any specific source of data of protein dynamics. We conclude that: 1. the dynasome consists of a continuum of proteins, rather than well separated classes. 2. For the majority of proteins we observe strong correlations between structure and dynamics. 3. Proteins with similar function carry out similar dynamics, which suggests a new method to improve protein function annotation based on protein dynamics. 

 Citation: Hensen U, Meyer T, Haas J, Rex R, Vriend G, et al. (2012) Exploring Protein Dynamics Space: The Dynasome as the Missing Link between Protein Structure and Function. PLoS ONE 7(5): e33931. doi:10.1371/journal.pone.0033931 Editor: Narcis Fernandez-Fuentes, Aberystwyth University, United Kingdom Received September 23, 2011; Accepted February 20, 2012; Published May 11, 2012 Copyright: ß2012 Hensen et al. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited. Funding: This work has been funded by the BioRange programme of the Netherlands Bioinformatics Centre, which is supported by a BSIK grant through the Netherlands Genomics Initiative. Further funding by the Klaus Tschira Foundation (www.klaus-tschira-stiftung.de), and by the EUROCORES-EuroSYNBIO (Pak 529), "NANOCELL" (http://www.esf.org/activities/eurocores/running-programmes/eurosynbio.html), grant number 1590/2-1. The funders had no role in study design, data collection and analysis, decision to publish or preparation of the manuscript. Competing Interests: The authors have declared that no competing interests exist. * E-mail: *hgrubmu@gwdg.de ¤a Current address: D-BSSE, ETH Zu¤rich, Basel, Switzerland ¤b Current address: Swiss Institute of Bioinformatics, Basel, Switzerland ¤c Current address: Abteilung Bioinformatik & Biochemie, TU Braunschweig, Braunschweig, Germany 

## Introduction 

The Anfinsen experiment [1] showed that protein structure, in principle, is determined by its sequence. Later this conclusion was nuanced when chaperones, the amyloidal state, natively unfolded proteins, etc., were discovered, but the concept that sequence determines structure – and ultimately function –, is still generally valid. Indeed, sequence alignments have revolutionized taxonomy and have become invaluable tools to derive phylogenetic trees, to predict domains in proteins for which no structural information is available, and to identify functionally important residues. New sequencing methods discover vast amounts of so far uncharacterized proteins and much effort is spent in the field of bioinformatics to improve existing and develop novel methods for sequence based function annotation [2]. Most of these methods are based on homology concepts. Simply speaking, if two proteins are homologs, they are likely to have highly similar structures and the same or similar functions. Unfortunately, sequences of homologous proteins with similar structure and function can diverge so far that their homology cannot be detected from their sequences alone. Chothia and Lesk showed in 1986 that the structure of a protein remains more conserved during evolution 

 than its sequence [3], and subsequently Sander and Schneider quantified this relation [4]. Accordingly, prediction of protein function from sequence data alone is limited by this rather indirect and complex relationship between sequence and function, and reliable annotations require close homologues with over 40% sequence identity over large enough portions of the sequence [5–7], thus posing a fundamental limit to function prediction from sequence alone. BLAST [8] is by far the most widely used software for sequence similarity detection, and when BLAST fails fails to detect homology scientists tend to resort to PSI-BLAST [9], threading techniques [10,11], hidden Markov models [12], or laboratory experiments. Structure can be seen as an intermediary between sequence and function, as exemplified in Fig. 1. Accordingly, in the absence of detectable sequence similarity, attempts have been made to infer function from structure similarities [13], and thus the classification of structures has become similarly important as sequence analyses for our understanding of protein function. Systems like CATH [14], SCOP [15], and DALI [16] provide a good overview of the protein structure universe. Indeed, the move from the sequence level to the structure level revealed more direct relations to protein 

function, and structure-based protein function predictions have proven more reliable [17]. These studies have, however, also shown that the relation between structure and function does, in the absence of sequence similarity, not permit reliable function predictions. Very different structures can have the same function (proteases, for example, occur in many branches of the classification trees of CATH, SCOP, and DALI) and very similar structures can have very different functions; the TIM-barrel fold, for example, has been observed with nearly all enzymatic functions known. As a result, purely structure-based protein function predictions have so far not been able to predict protein function beyond 30% reliability. Most often, it is protein motion that is required for protein function (Fig. 1). If nothing can move, nothing can function. Perutz described the movements hemoglobin must undergo to fulfill its function shortly after the structure was solved [18], and Frauenfelder pioneered the field by flash photolysis experiments which revealed a hierarchical organization of protein motions from thermal vibration to functional and collective conformational transitions [19] over 25 years ago. Detailed understanding on how dynamics leads to function is nevertheless still limited to few wellstudied cases such as hemo/myoglobin or aquaporin, which selectively controls diffusion of water and small molecules through membranes [20]. Assuming that protein function is determined by protein motions more directly than by protein structure, we here decided to carry the move from sequence space to structure space one step further. Such a general classification scheme for protein dynamics, similar to existing structure classifications, which captures the dynamics-function relationship, should also allow improved function prediction. Dynamics-based protein classification requires i) access to dynamics data of a representative set of proteins and ii) a similarity metric for dynamics of even structurally quite different proteins. Recent studies have, e.g., compared a particular protein in different environments [21–23], or similar proteins in a particular environment [21,24], or the unfolding of a number of different proteins [25–30]. In this study, we carried out molecular dynamics simulations on a set of 112 proteins that represent a sufficiently large fraction of the ‘universe’ of known structures, and developed a systematic and unbiased methodology to quantitatively compare molecular dynamics simulations for very different proteins. To this aim, for each of the 112 trajectories, 34 dynamics observables were calculated, e.g. fluctuation amplitudes and frequencies, the eigenvalue spectrum of principal components etc. These have been chosen such as to characterize the many different aspects of 

 protein dynamics to sufficient extent as to allow characterization of the dynasome and, taken together, yield a 34-dimensional vector for each protein. Each of these 112 vectors served to characterizes the dynamics of the respective protein, which is thereby represented as a point in the 34-dimensional ‘dynamics space’. Subsequent analysis of the distribution and mutual distances of these 112 vectors revealed that 1) the universe of protein dynamics is covered by our subset of 112 proteins rather homogeneously, and in particular does not show pronounced clusters of proteins with highly similar dynamic behaviors, 2) that the two main characteristics that best describe the differences between the molecular dynamics simulations relate to protein thermodynamics and protein kinetics, respectively, and 3) that protein dynamics correlates remarkably well with protein function, allowing straightforward function prediction. 

## Methods 

## Approach and Concepts 

 The core problem of any classification approach is the choice of a proper metric, which discerns similar from different samples. Here, the main question was how to assess whether the dynamics of two different proteins are similar or not. For proteins with similar structure one might use amplitudes, relaxation times etc. of the motion of corresponding structural elements such as helices or loops. For proteins of similar size, principal component analyses of the motions of the backbone may provide quantitative information [31]. For any given pair of possibly quite unrelated proteins, however, there is not even much heuristics available which would allow to quantify the similarity of their dynamics, with the notable exception of two recently proposed methods from Micheletti [32] and Biggin labs [33]. Similarly, it is unclear how putative correlations to protein function can be detected and quantified. In this study, we used 34 dynamics observables that have been selected such as to characterize the many different aspects of protein dynamics in a minimally biased fashion. Some of these quantities, such as fluctuation amplitude and frequencies, the eigenvalue spectrum of principal components, or the fluctuation of the radii of gyration, are widely known and routinely used. Others, such as the ‘entropy’ of the distribution of fluctuations within the protein or the roughness of the energy landscape that governs the principal modes, were developed here for the particular purpose of characterizing aspects of protein dynamics that we felt were not sufficiently covered by the established observables. Very much as for the study of sequence/structure relationships, the used structural observables (e.g., radius of gyration, helical content, packing etc) should not directly depend on the underlying sequence length, also all 34 dynamics observables were be normalized to avoid, as much as possible, any correlation to sequence or structural quantities. 

## Protein Selection 

 Proteins were selected from the pdbfinder database [34] such as to cover a large fraction of known folds and structure classes (Table 1). We only considered wild-type proteins that were categorized monomeric by the protein quaternary structure file server (PQS) [35] and required a resolution better than 1 :8 A, no ligands larger than 6 atoms, and no presence of metals other than Mg2+, Ca + 2 , K +, Na +, Zn +. Further requirements included a structure deposition date after 1987, an acceptable quality according to what check [36], absence of gaps larger than one amino acid, and structural stability during simulations. All structures passing these filters underwent visual inspection and were, if necessary, manually removed. Although, strictly speaking, 

Figure 1. Schematic hierarchy of protein sequence, structure, dynamics, and function. Correlations between the various levels enable predictions. Here we explore the level of protein dynamics, and how it relates to structure and, respectively, protein function. doi:10.1371/journal.pone.0033931.g001 

112 structures (Table S1) will not provide full coverage, we think that this number is large enough characterize the main features of the dynasome. 

## Simulation Setup and Ensemble Production 

Protein structures were examined and corrected by WHAT IF [37], where the WHAG [38] protocol was applied to correct for geometric errors in the backbone and side chains. Symmetry relaxed crystal waters that contact the monomer in the asymmetric unit cell were added. In case alternate atoms were present, the most abundant one was selected, and in case of equal occupancies the one with the alternate atom labeled A was used. Gaps in the structure of length one were filled as well as missing side chain atoms, which were placed by the rotamer library within WHAT IF [37]. The hydrogen bonding network was optimized as described in [39] and used to determine optimal rotamer angles and protonation states for Asn, His, and Gln residues. Aromatic groups with unphysical deviation from planarity were changed into planar conformation. All simulations were carried out with the gromacs simulation suite [40], using the OPLS all-atom force field [41] and periodic boundary conditions. Proteins were solvated with a solvent shell of 1.1 nm TIP4P water and sodium and chloride ions were added (c~ 0 : 15 mol=liter). All systems were subsequently energy-minimized for 100 steps by steepest descent. The solvent was then equilibrated for 500 ps with positional restraints on the protein heavy atoms (force constant 1000 kJ mol{1 nm{^2 ). MD runs were carried out for at least 100 ns for each system generating an isothermic-isobaric (NPT) ensemble, with the protein and solvent coupled separately to a 300 K heat bath (tT ~ 0 : 1 ps ) [42]. The systems were isotropically pressure-coupled at 1 bar (tp~ 1 : 0 ps ) [42]. Application of the LINCS [43] and SETTLE [44] algorithms allowed for an integration time step of 2 fs. Short-range electrostatic and Lennard–Jones interactions were calculated within a cut-off of 1.0 nm, and the neighbor list was updated every 10 steps. The particle mesh Ewald (PME) method was used for the long-range electrostatic interactions [45], with a grid spacing of 0.12 nm. Coordinates were saved to trajectories every 200 fs. 

## Trajectory Analysis and Dynamic Observables 

All proteins were simulated for at least 100 ns, the first 20 ns were discarded as equilibration period, and the remaining 80 ns were analyzed. The 34 dynamics observables that were calculated from each of these trajectories, summarized in Table 2, fall into four groups i-iv: i) Characterization of the eigenvalue spectrum of the proteins. Eigenvalues li and eigenvectors vi were obtained from diagonalization of the covariance matrix of Cafluctuations, 

 following the principal component analysis (PCA) protocol of Amadei et al. [31]. Eigenvalues were normalized to unit sum and the five largest eigenvalues were recorded as the first five (Y 1 ...Y 5 ) of the 34 dynamics observables listed in Table 2. Prompted by the observation that the central part of the eigenvalue spectrum resembles a power law [46], the region between 33% and 66% of the eigenvalue indices i was fitted to the function f (i)~aib:The fit parameter b, and the quality of the fit, quantified by the coefficient of determination (R^2 ), were used as observables Y 6 and Y 7 : ii) Analysis of the Principal Components of the trajectory. Each of the T = 80 9000 frames recorded in the 20 to 100 ns window were projected onto the first five eigenvectors vi~ 1 :: 5 to obtain the essential coordinates pi (t):From these, as a measure for the extent of sampling, the cosine contents [46] of the first five principal modes were calculated as 

 cosi ~ 

### 2 

### T 

### XT 

 t~ 1 

 cos 

 i T { 1 

 pt 

###   

 pi (t) 

### ! 2 

### XT 

 t~ 1 

 p^2 i (t) 

! (^) { 1 and recorded in observables Y 8 to Y 12 :The distribution functions (PDF) of the first three essential coordinates were obtained by binning. From fits of Gaussian functions f (x)~Ae(x{m) (^2) = 2 s 2 to these PDFs, R^2 values were determined and recorded as Y 13 to Y 15 : To gain insight into the time dependence of the dynamics of the 112 proteins, the fluctuations of the essential coordinates pi (t) were described by a Ornstein Uhlenbeck process [47], i.e. by diffusion within a harmonic potential well. Accordingly, the autocorrelation function of this process, F (Dt)~e{bDt=^2 ðÞcos (vDt)zb= 2 vsin (vDt), where Dt denotes the time interval between two frames, was fitted to the one obtained from the essential coordinates, ACFi (Dt)~Spi (t):pi (tzDt)Tl{ i 1 :The fit parameters band v relate to friction and force constants of a harmonic oscillator. They were strongly correlated and we considered only the friction constants f acfi of the first five principal components i~ 1 ... 5 and used them as observables Y 16 to Y 20 : iii) Ruggedness of the free energy landscape. As a further probe of protein dynamics we considered what we termed the (one-dimensional) ruggedness cof the underlying free energy landscape. To that aim, we described the protein dynamics, projected onto the individual PCA eigenvectors in terms of diffusive motion within a potential that is formed by a hierarchy of energy barriers (Fig. 2 [48]). As sketched in the figure, this hierarchy is characterized at each tier by barrier heights DF {and an average distance Dx between the barriers of that height. As can also be seen, we assume the barrier heights to increase logarithmically with their mutual distances, i.e., DF {~c=bln (Dx=L) with a barrier height increment c=band a unit length L, below which we assume free diffusion with a diffusion coefficient D 0 :Hence, as indicated in Fig. 2a, b and c, the ruggedness as defined for the present purpose does not measure the barrier heights as such (a and b), but rather, how fast the barriers grow with increasing mutual separation (c). As a result, the effective diffusion constant Deff (T ) for protein motion within such hierarchical landscape decreases with the time scale T at which diffusion is monitored, and is governed by the rate limiting – i.e., largest – barrier DF (T ) that is overcome by the system at this time scale, Deff (T )~D0 exp ({bDF {(T )), where D 0 is the diffusion constant in the absence of barriers. Table 1. Structure classes in the representative set of 112 proteins used in this study. SCOP class Number of proteins all 2 a 12 all 2 b 33 a/b 27 a+b 30 small 10 doi:10.1371/journal.pone.0033931.t001 

Vice versa, observation of the mean square distance s^2 ~TDef f (T ) travelled by the protein as a function of trajectory length T, hence, provides information on the ruggedness of the underlying hierarchical energy landscape. Combining the above equations, and assuming s&Dx yields the power law 

 s^2 ~(TD 0 Lc)2=(2zc), 

i.e. the eigenvalues lobtained from diagonalizing the covariance matrix of a trajectory of length T increase with trajectory length according to the power law T 2 =(2zc). Hence, cis obtained from the respective exponent 2 =(2zc). As should be expected, for free diffusion, this exponent is one, whereas for increasing ruggedness, diffusion ceases, and the exponent tends towards zero. Using the above power law, the respective ruggedness of each of the 3 N{ 6 eigen-modes of each protein was determined from the (average) slope 2 =(2zc) of the mean squared distance s(obtained from the respective eigenvalue of a PCA) as a function of used trajectory length T, both in logarithmic representation. Accordingly, covariance matrices and their eigenvalues li were calculated for 20 logarithmically spaced time windows ranging from 1 to 10 ns. For each window size, eigenvalues were averaged over 20 uniformly distributed trajectory parts to reduce statistical fluctuations. Fig. 1d shows as a typical ruggedness profile the values obtained for all 3 N{ 6 eigen-modes. Three observables were defined to characterize the overall shape of these ruggedness profiles, namely its average value (Y 21), as well as the skewness (Y 22 ) and kurtosis (Y 23 ). Because the dynamics of the largest eigenmodes is characterized already explicitly by other descriptors such as autocorrelation functions, the respective first 10 ruggedness 

 values were excluded (left purple rectangle). Similarly, the fastest ca. 30% of the eigen-modes were also excluded (in the figure separated by the gap at eigenvalue 555, right purple rectangle), as these arise from essentially harmonic bond vibrations which are very similar for all proteins considered and, therefore, are not expected to provide additional information on their dynamics. iv) Atomic fluctuations. The time-averaged root mean square deviation (RMSD) from the crystal structure mRMSD^ (Y 24 ) and its standard deviation relative to the mean cRMSDv ~sRMSD=mRMSD (Y 25 ) were calculated to quantify the average deviation from starting conditions. The overall flexibility of the protein was described by the RMS fluctuation with respect to the average structure (Y 26 ), and breathing motions were quantified via the standard deviation of the radius of gyration crgv from its mean value (Y 27 ). Secondary structure contents were determined over time using the Kabsch and Sanders algorithm [49] implemented in the ptraj program [50]. Relative fluctuations about the mean content were calculated for the total secondary structure csstructv (Y 28 ) and the secondary structure elements a-helix cav (Y 29 ), b-sheet cbv (Y 30 ) and turn cturnv (Y 31 ). Solvent accessible surface area was calculated along the trajectory using naccess [51] with 1.4 A ̊^ probe radius, the mean polar solvent accessible surface (SAS) mSAS^ and cSASv were used as observables Y 32 and Y 33 : To describe the degree of localization of flexible regions in the protein we calculated the root mean square fluctuations (RMSF) Sri Tfor each residue i of the protein using the ptraj program [50]. The resulting flexibility profile was characterized by its average mRMSF^ value and the entropy SRMSF^ ~{ 

### X 

 Sri T 

  (^) { 1 Xnres i~ 1 Sri^ T ½:ln ðÞSri T zln 

### X 

 Sri T 

###   

 of the distribution, values were recorded in Y 26 and Y 34 : 

 Table 2. These 34 dynamics observables Y 1 to Y 34 have been used to characterize the dynasome. 

 Index Symbol Description 1, ..., 5 l1, ..., l 5 Eigenvalues 1, ... 5 6 ml Slope of the middle third of the eigenvalue spectrum 

(^7) x^2 l R^2 value of the fit to the eigenvalue spectrum 8,...,12 cos1,...,cos5 Cosine content of the principal components 1–5 13, 14, 15 (^) x^2 N,1 ,x^2 N,2,x^2 N,3 Goodness of fit of a Gaussian fit to principal components 1–3 16, ..., 20 (^) f 1 acf , ...,f acf 5 Friction constant derived from a fit to the autocorrelation function of principal components 1–5 21 mc Measure of the average ruggedness of the energy landscape: Average slope of a linear fit to the time dependent eigenvalue spectrum c. 22 skewc Skewness of the distribution of these ruggedness values (6) of each collective degree of freedom. 23 kurtc Kurtosis of the distribution of these ruggedness values. 24 mRMSD^ Average root-mean square deviation from the X-ray structure (^25) cRMSDv Standard deviation (% of mean) of the root-mean square deviation from the X-ray structure 26 mRMSF^ Average residual fluctuations with respect to the average ensemble structure (^27) crgv Standard deviation (% of mean) of the radius of gyration 28, ..., 31 (^) cstructv ,cav ,cbv ,cturnv Standard deviation (% of mean) of secondary structure content: total, a-helix, b-sheet, turn 32 mSAS^ Average solvent accessible surface (^33) cSASv Standard deviation (% of mean) of the solvent accessible surface 34 SRMSF RMSF entropy doi:10.1371/journal.pone.0033931.t002 

## Structure Analysis and Structure Observables 

Similar to the 34 dynamics observables we defined a set of 24 non-redundant observables, listed in Table 2, that characterize protein structure. Structures of the 112 proteins were retrieved from the protein data bank (PDB) and missing atoms were added from the amber residue libraries using the program tleap [50]. Structures were then energy minimized in 100 steepest-descent steps with 25 kcal mol{1A{^2 restraints on heavy atoms using the sander program from the amber10 package [50]. Observables were then calculated for each structure. Radii of gyration and moments of inertia along the three principal axis (g_gyrate [52]) X 1 to X 4 were calculated to characterize the overall shape of the protein. Further, the overall charge distribution was characterized by the proteins principal dipole moments, calculated using the g_dipoles program of gromacs and recorded in X 4 toX 6, because imbalances in charge distribution are often associated to function [53]. Secondary structure content was determined as described above and the numbers of residues in helix, sheet, coil, and g-turn 

 conformation, respectively, were recorded as structural observables X 7 to X 10 : Intramolecular contacts were counted for non-neighboring (7 residues distance in sequence) residues where the d CaCav 7 :0 A (X 11 ); contacts were considered hydrophobic if both residues are of A, I, L, M, F, P, W, or V (X 12 ). Hydrogen bonds were annotated using standard criteria d HAv 3 :5 A and DHAw 120 and counted (X 13 ). Total and hydrophobic solvent accessible surface areas were calculated using naccess [51] and recorded in X 14 and X 15 : To describe protein topology, i.e. the non-local contacts, we generated for each protein its residue adjacency matrix with entries for all residues with at least two atoms closer than 3 :5 A : The matrix defines a network where residues are nodes and connections are drawn between adjacent residues [54], which we characterized by its average path length X 16, cluster coefficient X 17, and network radius X 18 : The number of hydrophobic, hydrophilic basic, acidic, proline, and lysine residues in the sequences were counted to characterize the chemical composition of the proteins, and were recorded as structure observables X 19 to X 24 : 

## De-correlation of Observables 

 Some of the dynamics (Y 1 ...^34 ) and structure (X 1 ...^24 ) observables listed in Tables 1 and 2 were found to correlate markedly with sequence length. Because such correlation would, indirectly, introduce unwanted sequence information into the dynamics and structure observables, these were removed. To that aim, all observables for which correlations were detected were fitted to an appropriate model of the observed length dependence. After subtraction of the fit function, the now sequence-length decorrelated observables were normalized to zero mean and unity standard deviation. All fit functions are described in Table S2 and the pairwise correlations of the processed observables are displayed in Fig. S1. 

## k-means Partitioning of the Dynasome 

 Clusters in the population of the 34-dimensional dynamics space were identified using a k-means algorithm, which iteratively minimizes the sum of distances of dynasome vectors to cluster centroids [55]. As initial guess, the location of the cluster centroids was chosen randomly. From 5000 runs with random initial conditions, the one with the smallest squared distance sum was used for subsequent analysis. 

## De-correlation of Structure-dynamics Similarities 

 To assess to which extent structural similarity of proteins correlates with their dynamics similarity (Section ), the Euclidean distance distruct,j in structure space of all protein pairs (i,j) was plotted vs. their respective distance d idyn,j in dynamics space. The resulting plot was compared with a randomized reference data set, for which all correlations of ddyn^ and dstruct^ were eliminated by randomly permuting the 6216 pairs (i,j) for dstructi,j with respect to ddyn i,j , as sketched schematically in Fig. S2. As can be seen, this procedure eliminates all correlations between ddyn^ and dstruct while preserving their individual distributions. 

## Graphs of Mutual Adjacencies in Dynamics Space, 

## Structure Space and Combined Space 

 The fine structure of the dynasome was represented as a graph of mutual adjacencies in dynamics space (see main text). First, adjacency matrices were obtained by identifying the k nearest neighbors of each protein in a d dimensional subspace of the 34dimensional dynamics space, using the mathematica 7 Nearest 

Figure 2. Illustration of the ruggedness parameter cused as a descriptor in this study. a) – c): Schematic rugged energy landscapes. The ruggedness of a) and b) is identical; although absolute barrier heights differ, the factor by which the barrier heights increase with their distance along the conformational coordinate is the same. In contrast, the energy landscape shown in c) is characterized by a larger ruggedness. d) A typical ruggedness profile of a protein is characterized by a steep increase at small eigenvector indices and a subsequent smooth descent to a characteristic minimum. The ruggedness of each eigenvector is described by ci , and the characteristics of the respective ruggedness profile (average ruggedness, skewness, and kurtosis) are used as descriptors 21, 22, and 23, respectively (Table 2). For the computation of these ruggedness descriptors, the first 10 eigenvectors and all eigenvectors beyond the characteristic minimum (purple shaded areas) were omitted. doi:10.1371/journal.pone.0033931.g002 

function. For the visualization of the graph of the resulting adjacency matrix, we used the GraphPlot function with the spring electrical embedding option and the repulsive force power option set to 2 1. Parameters k and d, required to calculate the adjacency matrix, were chosen as follows. For each pair fk,dgof k~2,:::,6 and d~3, ...,15, the adjacency matrix was computed as described above, the graph of this adjacency matrix was partitioned using the CommunityStructureAssignment module of mathematica, and the partitioning was quantified using the community modularity C (Fig. S3). For further analysis, the pair fk,dgyielding the best partitioned graph was selected for further analysis (black points in Fig. S3). 

## Assignment of Functional Classes 

Proteins were assigned functional classes according to UNIPROT [56]. Table S1 lists the function class assigned to each protein. Poorly covered functional classes were collected as ‘‘Other’’ and ‘‘Other Enzymes’’ and not used for function prediction. 

## Results and Discussion 

## Generation of Dynasome Observables 

We picked (cf. Methods) a set of 112 soluble, single-domain proteins from the protein database (PDB) [57], such that all structure classes were about equally represented. For each protein, explicit solvent all-atom molecular dynamics simulations of 100 ns length were carried out (cf. Methods) to sample the proteins native state dynamics at picosecond to 100 ns timescales. From each of the obtained trajectories, we calculated 34 observables, some of which specifically devised for this study (see Table 2). The combination of these provides a comprehensive characterization of the dynamics of each of these 112 proteins at time scales between picoseconds and 100 ns. In this 34-dimensional ‘‘dynamics space’’, spanned by the 34 observables, each protein is thus represented as a vector, and proteins of similar dynamics appear as nearby points in this space. We will refer to the whole ‘‘point cloud’’ of all proteins as the dynasome. Subsequently, we will investigate the properties and structure the dynasome. 

## Few Collective Dynasome Descriptors Describe Most of 

## the Dynasome 

What are the most important dynamics features of that distinguish the 112 proteins from each other? To address this question, we carried out a principal component analysis (PCA) of the dynasome. Each of the resulting 34 eigenvectors constitutes a collective descriptor consisting of a linear combination of the 34 observables introduced above, very much as normal modes are linear combinations of individual atomic displacements [58,59]. We refer to these linear combinations as dynasome descriptors. The eigenvalue profile (Fig. 3) shows that relatively few of these dynasome descriptors suffice to describe a large fraction of the dynamics seen in our protein set, e.g. the first 15 collective descriptors explain 80% (Fig. 3 inset) of the diversity of the dynamics of the examined proteins. Notably, already the first two dynasome descriptors explain more than 30% of the dynamics variation seen in our protein set (Fig. 3). Table 4 (columns 1 and 2) lists those dynamics observables that contribute most to these two first descriptors. As can be seen, descriptor 1 contains the average deviations from the X-ray structure mRMSD^ (entry 1) and from the ensemble average mRMSF (entry 2), respectively, as (entry 3). All these observables characterize the magnitude of atomic fluctuations. The next two 

 important observables in dynasome descriptor 1 are the average ruggedness m(c) and skewness of the ruggedness spectrum (cf. Fig. 2). Their contribution (7%) to descriptor 1 is marked with ( 2 ) in Table 4, indicating anti-correlation of these two observables to the dynasome descriptor and reveal an interesting correlation: normally, fluctuations tend to be small for proteins for which the dynamics of the essential modes is governed by a rugged free energy landscapes (high skewness skew(c) combined with high average ruggedness m(c)). In contrast, large deviations from the Xray structure are seen for relatively smooth energy landscapes (low m(c)) or if large-scale modes proceed along relatively smooth pathways compared to the small-scale high-frequency modes (low skew(c)). Strikingly, all the observables that dominate the most essential dynasome descriptor quantify ensemble properties. The second dynasome descriptor is composed mainly of the friction coefficients of the diffusion along the first four (protein) eigenvectors f 1 acf , ...,f 4 acf (f 3 acf contributes 6% and is thus not listed in Table 4) and the Gaussianity of the proteins’ first principal component. In contrast to the first descriptor, these observables describe the time evolution of the global, collective motions of the systems, i.e. relate to kinetics. The correlation between friction coefficients at slow motions and deviations from Gaussianity reflects the frequent observation that slow degrees of freedom tend to be anharmonic. It is a remarkable result that purely from an analysis of which observables contribute most to the dynamics diversity of the 112 selected proteins, and without any further input or bias, the above two dynasome descriptors were able to identify and distinguish ensemble properties (thermodynamics) from dynamics properties (kinetics). A few typical examples shall illustrate how these two main collective dynamics descriptors serve to characterize the dynamics of particular proteins. Fig. 4a shows the distribution of the 112 proteins in the plane spanned by the dynamics descriptors 1 and 2. The axes labels indicate the type of dynamics, as summarized above, described by the respective descriptor. As a first example, calmodulin (Fig. 5a) is one of the most flexible structural proteins known to date and thus shows up as an outlier on the right of Fig. 4a. Calmodulin exhibits very large overall deviations from the crystal structure (reflecting its flexibility) and samples a very smooth energy landscape of extraordinarily low average ruggedness m(c):These two aspects are described by the dynasome descriptor 1 (x axis). The second dynasome descriptor (y axis) 

 Figure 3. Eigenvalue spectrum of the collective dynamics descriptors. Eigenvalues li are given as fractions of the sum of all eigenvalues. The inset shows the cumulative distribution. doi:10.1371/journal.pone.0033931.g003 

shows that the timescales on which Calmodulin dynamics take place, described by the friction constants f 1 acf , ..., f 5 acf of diffusion along the first five eigen modes, are not unusual. As a second example, the neurotoxins Erabutoxin A and Erabutoxin B (Fig. 5b) are both characterized by extremely flexible and fast moving loops held, tethered to a rigid core and stabilized by sulfide bridges. Both are outliers in the upper left part of Fig. 4a. The fact that fast and low amplitude motions dominate these proteins is revealed by very high average ruggedness m(c) and large friction constants f 1 acf , ..., f 5 acf , as described by dynasome descriptor 2. 

## Proteins Do not Fall into Well-separated Dynamics 

## Classes 

An interesting observation from Fig. 4a is that the projections on the first two dynasome descriptors show a rather continuous distribution without significant substructure. In light of the seemingly obvious clustering of protein structures that the reader 

 may have in mind, this result is unexpected and will need careful discussion. Before addressing this question in more detail, however, we investigated the extent of the structural classification reflected in the dynamics space. Fig. 4b shows the same projections as in a) with color codes indicating the SCOP structure class. Different structure classes tend to accumulate in different regions of dynamics space. All{a proteins are, for example, predominantly found on the right, whereas most all{b proteins are found to the left. a=b-proteins overlap significantly with all{b, but are shifted slightly towards the bottom. Small proteins cover a large range from the upper left to the right. The standard deviation of the distributions of proteins of each SCOP class (large ellipses in Fig. 4b) show that the distributions overlap significantly. In contrast, the centroids of the different classes (centre of the ellipses) assume significantly different positions in dynamics space, as documented by the standard deviations of the mean (small circles). We conclude that, on average, the dynamics of proteins described by the first two dynasome descriptors show a certain correlation to protein structure. The fact that the dynamics distributions of different structure classes overlap suggests, however, that there is no simple on-to-one mapping between protein structure and dynamics. Therefore, analysis of the dynasome should reveal additional information beyond that already contained in the protein structure. Note that the above result of overlapping SCOP classes in dynamics space (Fig. 4) might also be a consequence of projecting 34-dimensional data onto two dimensions that account for slightly more than 30% but miss 70% of the overall dynamics features. If that was the case, then a non-hierarchical k-means clustering (methods) with a squared Euclidean metric in the full 34dimensional space would reveal any internal structure – in particular, clusters – that might have been lost in the projection. k-Means analyses with 1 to 10 cluster centers have been performed, but the analysis of the resulting clusters in terms of connectivity and variance [60] did not reveal any marked minimum (Fig. S4), which confirms that the absence of apparent clusters in Fig. 4 is not a projection artifact. Hence, also full space analysis did not reveal any natural partitioning, which agrees well with the visual inspection of Fig. 4. Next, k-means clustering served to quantify possible correlations between SCOP and dynamics space. To that aim, we determined the overlap between the SCOP classes and the classification 

Figure 5. Selection of six of the 112 proteins included in this study: a) Calmodulin (PDB code 1OSA [71]), b) Erabutoxin B (PDB code 3EBX [72]), c) Achromobacter protease I (PDB code 1ARB [73]), d) Thioredoxin-2 (PDB code 1THX [74]), e) superantigen (PDB code 3SEB [75]), f) angiogenin (PDB code 1AGI [76]). Pictures were generated using MolScript [77]. doi:10.1371/journal.pone.0033931.g005 

Figure 4. Projection of the dynasome onto descriptors 1 and 2. Each point represents one protein. a) Protein dynamics as described by dynasome descriptors 1 and 2. The axes labels indicate which dynamics properties are mainly described by the respective descriptor. The inset focuses on the lower left region. b) same projection as in a), colored according to SCOP structure classes (see legend). Ellipses indicate the distributions of structure classes; Large thin ellipses denote standard deviations of the distributions, small thick ellipses the standard deviations of their mean. doi:10.1371/journal.pone.0033931.g004 

obtained by k-means clustering. First, to obtain better statistics, we considered only proteins belonging to the SCOP classes all{a, all{b and a=b:Figure 5a shows the distribution of these three SCOP classes into the three partitions of dynamics space identified by k-means clustering. As can be seen, more than 80% of the all{a proteins are found in the first cluster, which contains less than 20% of all{b and less than 30% of the a=bproteins, respectively. The second dynamics cluster, in contrast, contains almost 90% of all all{bproteins and almost 70% of the a=b proteins, but less than 15% of the all{a proteins. Obviously, a and bproteins are separated well in the full dynamics space, whereas all{b and a=bproteins overlap markedly, and to a similar extent as in the two-dimensional projection (ellipses in Fig. 4b). Next, we considered all five SCOP structure classes and determined their distribution into a partitioning obtained from a k-means clustering for five classes. As can be seen from Fig. 6b, a similarly pronounced separation between all{aand all{b/a=b is obtained (Fig. 6a), whereas almost all a +b and small proteins can, purely on the basis of their dynamics fingerprint, not be well distinguished from all{aproteins. Overall, our 112 sample proteins seem to populate dynamics space rather uniformly, without marked clusters or sub-families. Nevertheless, as was already visible in the two-dimensional projection (Fig. 4), the known structural classes tend to accumulate in different regions in dynamics space. This observation shows that structural classes, e.g., all{aand all{b, can be distinguished purely from their dynamics fingerprints. Also from this analysis, the remarkably large but not strict correlation between structure and dynamics points to additional information (or noise) that may be contained within protein dynamics but not within structure alone. The finding that proteins are continuously distributed in dynamics space was actually quite unexpected. Several mechanisms might, alone or combined, explain our findings: First, the SCOP structure classes used here as a reference might suggest a much clearer partitioning of the structure space than would be obtained from an approach not based on discrete descriptors such as secondary structure class, which unavoidably implies a certain 

 partitioning. A number of recent studies [61–63] indeed yield less pronounced partitioning suggesting that this effect might actually play a role. Our own structure-based analysis discussed further below provides further support for this possibility. Alternatively, the protein distribution in dynamics space might become ‘blurred’ with respect to that in structure space by the fact that already slight structural changes might imply quite different dynamics. We will quantify this possibility, referred to as ‘adjoint dynamics’ further below. Vice versa, similar dynamics patterns might arise from quite different structures (‘disjoint dynamics’). We intentionally refrained from the use of the more suggestive terms ‘convergent’ and ‘divergent’ to avoid any direct evolutionary interpretation, which would not be supported by our approach. As a third option, and despite our efforts to cover many different aspects of protein dynamics, we cannot completely rule out the possibility that the 34 dynamics observables we have chosen simply do not suffice to provide a sufficiently complete picture of the dynasome to be able to detect an existing partitioning. To test for this possibility, we repeated the above analysis using different subsets of these dynamics variables, without significant changes of the obtained partitioning. 

## Protein Structure Classes Overlap Significantly 

 We thus asked which of these mechanisms is actually at the root of the observed continuous distribution in dynamics space. The first question we addressed was whether or not natural structure classes are evident if a similarly systematic approach as used above for protein dynamics is applied to protein structures. In other words, are the well-known protein structure classes indeed recovered from our unsupervised approach (also see, e.g. [16,64,65])? To address this question, we described the structure of each of the 112 proteins by a set of 24 different structure observables (Table 3) such as residual contact matrix, secondary structure content, moments of inertia, and solvent accessible surface (see methods for full details). These 24 structure observables span a structure space with each protein being characterized by one vector, similar to dynamics space. These vectors were then subjected to PCA. 

Figure 6. Recovery of structural classes from dynamics. Distribution of three a) and all five b) SCOP classes (colors) onto partitionings of the dynasome (1...5) obtained from k-means clustering. Bar heights denote the fraction of proteins of each structure class found in each partition. doi:10.1371/journal.pone.0033931.g006 

 Table 3. These 24 structure observablesX 1 to X 24 have been used to characterize the protein structure space. 

 Index Symbol Description 1–3 Ix,y,z Principal moments of inertia 4–6 wx,y,z Dipole moments 7–10 na,b,coil,turn^ Secondary structure content 11,12 nall,hydrophobic^ Number of intramolecular contacts 13 nHB^ Number of hydrogen bonds 14,15 sasa,sasahp^ Solvent accessible surface area 16 apl Average path length 17 cc Cluster coefficient 18 r Cluster radius 19 nphob^ Number of hydrophobic residues 20 nphil^ Number of hydrophilic residues 

(^21) nHz Number of acidic residues (^22) nOH{ Number of basic residues 23 nPro^ Number of proline residues 24 nCys^ Number of cysteine residues doi:10.1371/journal.pone.0033931.t003 

Figure 7 shows the distribution of protein structures (points) in the plane spanned by the first two eigenvectors obtained from this PCA. As can be seen from Fig. 7a, no clusters are evident in the space of protein structures, quite similar to our observation in the space of protein dynamics. This result supports our above conjecture that SCOP and CATH suggest a much clearer partitioning of protein structure space than is evident from our unsupervised classification from a set of 24 structural observables, and in fact also from other unsupervised approaches [63,66]. From this point of view, our finding of a rather unstructured dynasome is less surprising. This result also raises the question if (and how) the positions of proteins in this structure space relate to their respective SCOP classes (Fig. 7b). As can be seen, despite marked overlap of the individual classes (large ellipses) the class centroids are statistically significantly separated (small ellipses). This is a remarkable result per se, as it shows that our approach of fully unsupervised structure characterization, which does neither involve sequence information, nor any heuristics, hierarchy, or evolutionary criteria, still recovers the top tier of the hierarchical, manually curated, and evolution-based SCOP classification system. 

## Similar Structures May Show Different Dynamics – and 

## Vice Versa 

One of the goals of this work is to see if protein dynamics information can be used to improved protein function prediction beyond sequence and structure based schemes [67]. This requires that the dynamics fingerprint considered here holds information which – due to the possibly rather indirect relationship between structure and dynamics – can not be extracted from structures alone. This additional information would show up as incomplete correlation between structure and dynamics. We have therefore quantified this correlation using Euclidean distances in structure and dynamics space, respectively, as an appropriate metric. In particular, and relating the second of the three scenarios discussed above, this metric will allow to address the question: Given two structurally similar proteins, how similar are their dynamics? Further, does similar structure necessarily imply similar dynamics or, conversely, can similar motion patterns be generated from quite different structures (adjoint dynamics)? Vice versa, can small structure differences imply large differences of protein dynamics (disjoint dynamics)? As above, structural similarity of each protein pair was measured by its Euclidean distance dstruct in 

 structure space, and these distances were correlated to their respective counterpart ddyn in dynamics space. Fig. 7a shows for each of the 6216 protein pairs i distances as points in the x–y plane. As can be seen, the overall shape does not indicate a particularly strong correlation between structural and dynamics similarities, with a Pearson correlation coefficient of 0.38. This number is difficult to interpret, however, as a priori it is unclear how correlations between the positions of proteins in highdimensional dynamics and structure spaces, respectively, relates to the observed correlation between distances of pairs of proteins in dynamics space and structure space. In particular, it is unclear whether the observed low correlation coefficient actually implies that our dynamics observables are nearly unrelated to the protein structures. To assess the significance of this correlation, we randomized the coordinates of the dynamics vectors to obtain a reference point cloud (Fig. 8b), which, by construction, lacks any correlation between structure and dynamics (see methods). Figure 8c shows the difference of point densities (color code) between the data in Fig. 8a and the randomized reference data in Fig. 8b. Red regions indicate significantly higher densities than expected for uncorrelated data, blue lower densities, and green indicates regions where dynasome and randomized densities are similar or where no data is available. The pronounced structure seen in Fig. 8c reveals and quantifies systematic relationships between structure and dynamics, and suggests its classification into four regions, as denoted by four symbols (white insets in the corners). It is, for instance, mainly along the diagonal where significantly more pairs are found than would be expected by chance. The lower left region contains protein pairs that are similar both in terms of structure and dynamics. There is a significant correlation between structural similarity and dynamics similarity beyond what would be expected by chance, as indicated by the coloring. For a small sample of five proteins with similar fold, such correlation has been suggested previously from a coarse grained elastic network analysis [68]. Further along the diagonal, the upper right region contains pairs of protein pairs which are very different in both structure and dynamics. This quadrant is also significantly more populated than expected by chance showing a systematic trend, that structurally different proteins tend to exhibit different dynamics. Calmodulin, whose dynamics and high flexibility are remarkable in many ways (as also reflected by its position in Fig. 4b), also has an unusual structure (Fig. 5a and Fig. 7) different from most other proteins. 

Figure 7. Distribution of proteins in structure space. Each point represents one protein. a) Protein structures as described by eigenvectors 1 and 2. In plot a) the same proteins as in Fig. 3 are labelled. b) same projection as in a), but colored according to SCOP structure classes (see legend). Distributions of SCOP classes are described by their standard deviations (thin large ellipses) as well as the standard deviation of their respective means (thick small ellipses). doi:10.1371/journal.pone.0033931.g007 

Accordingly, many pairs involving Calmodulin are located in the indicated region in the top-right corner of the red region of Fig. 8c (inset with PDB code 1OSA). The two off-diagonal regions (blue), in contrast, indicate structure-dynamics relationships which are underrepresented. The region below the diagonal contains pairs involving proteins with similar dynamics despite dissimilar structure, which we termed ‘‘adjoint dynamics’’. As an example, consider the two hydrolases with PDB codes 1SAT and 2APR (Fig. 8c, lower left inset), which exhibit similar dynamics despite their quite different structures. The relatively high structural dissimilarity is reflected by high distance in structure space (13.28), and also by undetectable similarity using the pairwise-DALI algorithm [69]. Vice versa, ‘disjoint dynamics’ is seen in the region above the diagonal, where proteins with similar structure display quite different dynamics. Here, the trypsin (1TGN) and the xylanase (1XNB) (Fig. 8c, upper left inset) serve as an example. These two proteins are structurally similar (distance in structure space 6.19), but separated in dynamics space by the large distance of 11.6 units. Comparison of Fig. 8a with c shows that a considerable number of proteins show such remarkable behavior. The latter two regions are particularly interesting, because they reveal relationships between proteins, which purely structure based 

 classification would miss. Although not derived in an evolutionary context, it is tempting to speculate about the implications of these results. For example, the adjoint dynamics of structurally different proteins may in some cases result from convergent evolution, in cases where similar dynamics is required to achieve a particular function. Conversely, disjoint dynamics may have occurred in response to the need to evolve divergent functionality from a common ancestor. In both cases, one would expect that our analysis of the dynasome should improve protein function predictions. The dynamics of e.g. Erabutoxin B is quite unusual, in contrast to its unsuspicious structure (Fig. 7). Accordingly, most pairs involving Erabutoxin B are located in the ‘‘disjoint dynamics’’ region above the diagonal. On the one hand, they need rigidity to escape the proteases of the infected immune system; on the other hand they need pronounced flexibility to account for the differences of certain receptors in all the different prey animals they are supposed to attack. Further below we will give a more systematic account of the relationship between dynamics and function, but first we need to analyze the fine structure of the dynasome. 

## Fine Structure of the Dynasome 

 We have shown above that the dynasome lacks well-separated clusters. Nevertheless, Fig. 4a suggests the existence of some 

Figure 8. Structure dissimilarity vs dynamics dissimilarity. a) Each point displays the structure dissimilarity (x axis) vs. the dynamics dissimilarity (y axis) for one protein pair. Structure and dynamics dissimilarities for each of the 6216 protein pairs were computed as squared Euclidean distance between any two points in structure and dynamics space, respectively, as described in the text. Distances are unit-less. Regions of larger opacity reflect higher point densities. The overall Pearson correlation coefficient between structure and dynamics is 0.38; b) Randomized reference data obtained by removing any correlation between structure and dynamics dissimilarities, as described in methods (cf. Fig. S2); c) difference between point densities a) and b), after smoothing with a Gaussian kernel of width 1. Regions of larger than random density are colored red, those of lower density are colored blue, and regions with equal density or no data are shown in green, as quantified by the color bar. Below the diagonal: adjoint dynamics. Above the diagonal: disjoint dynamics. Inset in the red upper right region: Average position of Calmodulin (PDB code 1OSA), which reflects its dissimilarity both in structure and dynamics from most other proteins. Inset in the top of the disjoint dynamics region: Average position of Erabutoxin B (PDB code 3EBX), reflecting its common structure paired with unusual dynamics. Disjoint dynamics region: Position of the pair of trypsin 1TGN and xylanase 1XNB. These two proteins are structurally quite similar but markedly different in dynamics. Adjoint dynamics region: Position of the pair of the hydrolases 1SAT and 2APR, which have dissimilar structure, but display very similar dynamics. doi:10.1371/journal.pone.0033931.g008 

internal substructure, which should reflect the expected relationship between dynamics and function. The k-means partitioning employed in Figure 6 might not reveal such fine structure, because it rather focuses at spherically shaped, well-separated regions of high point density and is, furthermore, relatively sensitive to outliers. Therefore, as a complementary approach to k-means, we calculated graphs of mutual adjacencies, which are length-scale invariant and do not rely on explicit assumptions about the shape of putative sub-structures. In this approach, two proteins are considered adjacent if they belong to each other’s k nearest neighbors in a properly chosen d-dimensional subspace of the 34dimensional dynamics space. The resulting adjacency matrix is represented as a graph, in which each protein is a vertex and two adjacent proteins are connected by an edge. The parameters d and k were always chosen such that this graph was compact and optimally partitioned, as quantified by the community modularity [70] (see methods). Figure 9a shows the mutual adjacency graph of the dynasome, with k~ 4 and d~ 4 :In this representation, proteins with similar dynamics appear as close-by vertices with high connectivity, and 

 clearly separated from other clusters by vertices with relatively low connectivity. Ten clusters (colors) were identified by maximizing the community modularity (Fig. 9b). Comparing Fig. 9b with our previous analyses of the structure of the dynasome shows that this graph is a faithful representation of the dynasome (Text S1 and Fig. S5). In particular, our graph based clusters group proteins with similar positions in the PCA projection (Fig. 4), as indicated by the arrows representing the position of each protein in the plane spanned by dynasome descriptors 1 and 2. Vice versa, additional structure is revealed, as can be seen from the fact that some groups of proteins have almost identical positions in Fig. 4, but are clearly separated in Fig. 9b. 

## Function Coins Dynamics 

 In the following we will analyze the correlation between dynamics and function. To this aim we classified the 112 proteins according to literature annotations into 9 relatively broad function classes (see methods and Table S1 for details). We first determined the mean position, or centroid, of each of the 9 function classes in the dynasome space. In Fig. 10a, this average position of each function class is represented by a compass diagram. The lengths (and direction) of the four bars labeled 1,..., 4 correspond to the average position on the first four dynasome descriptors. If function classes were randomly distributed, the mean position of each class would fall onto the origin. Instead, we find that each function class has its unique dynamics fingerprint. For example, as indicated by descriptor 1 (black) in the compass plots, esterases (centre, light orange) appear to sample a smoother free energy landscape, according to Table 4, than that of glycosidases (purple), where the respective projection has an opposite sign. Also, esterases tend to fluctuate at slower time scales (descriptor 2 compass plots, cf. Table 4). In contrast, these two functional groups show similar collectivity of the functional modes (descriptor 3, cf. Table 4) and fluctuations of secondary structure elements (descriptor 4). The 

Figure 9. Graph representations of the fine structure of the dynasome. a) Graph of the adjacency matrix of dynasome proteins in the space spanned by the first four dynasome descriptors. Vertices represent proteins, edges represent neighborship. Highlighted are proteins discussed in Fig. 4. b) same graph as a), but colored according to the clustering obtained by maximizing the community modularity. Arrows indicate the position of each protein on the subspace spanned by the dynasome descriptors 1 and 2 (cf. Fig. 4 and Table 4). doi:10.1371/journal.pone.0033931.g009 

 Table 4. Composition of the first four dynasome descriptors: Shown are the five observables that contribute most to the first four descriptors; relative contributions to the descriptor are given in percent, (–) indicates that the respective observable appears in the linear combination defining the descriptor with a negative coefficient. 

 Descriptor 1 Descriptor 2 Descriptor 3 Descriptor 4 

(^1) mRMSF^ 10% f 1 acf 12% l 5 19% (^) cSASv 13% 2 mRMSD^ 9% f 2 acf 8% l 1 15% cturn^ 12% (^3) crgv 9% f 4 acf 7% l 4 11% kurtc11% (–) 4 skewc7% (–) x^2 N,1 7% cRMSDv 9% (–) l 3 9% (–) 5 mc7% (–) kurtc7% (–) crg^ 6% (–) cstructv 7% (–) For a list of the symbols, see Table 2. Descriptor 1: Average root mean square fluctuations from the ensemble average mRMSF^ ;average root mean square deviation from the X-ray structure mRMSD^ ;standard deviation (% of mean) of the radius of gyration crgv ;skewness of the ruggedness distribution of the proteins’ degrees of freedom skewcand average ruggedness (averaged over all collective degrees of freedom in the protein) mc:Descriptor 2: friction constants of the diffusion along collective degrees of freedom f acf^ ;goodness-of-fit of the first principal component to a Gaussian distribution x^2 N,1 ;kurtosis of the ruggedness distribution of the proteins’ degrees of freedom kurtc:Descriptor 3: Eigenvalues of the protein ensembles’ eigenvectors 5, 1 and 4 (2 and 3 appearing further below and are not explicitly shown here); fluctuation of the RMSD from the X-ray structure cRMSDv and of the radius of gyration crgv : Descriptor 4: Fluctuations of solvent accessible surface, turn content and secondary structure content cSASv , cturnv , and cstructv : doi:10.1371/journal.pone.0033931.t004 

most flexible proteins in our set are calcium-binding proteins (deep orange). These exhibit the most pronounced secondary structure fluctuations (descriptor 4) and in that respect differ strongly from typical DNA/transcription related proteins (yellow), which in turn fluctuate on the fastest time scales of all examined proteins. These pronounced differences in the average positions, to which we will refer to as ‘dynamics fingerprint’ of the proteins, should also show up in the graph representations of the dynamics space. Fig. 10b (left; see also Fig. S6 left column), reproduces the dynamics graph introduced in Fig. 9 here with the nodes colored according to their function classification. As can be seen, the clustering identified in Fig. 9, although purely based on dynamics descriptors, reflects the functional classification shown in Fig. 10b (left) to a remarkable extent. For instance, three out of four DNA/ transcription related proteins (yellow) are on the rightmost branch, almost all proteins in the top-left branch are glycosidases (purple), and serine proteinases (magenta) dominate the top branch and the lower left branch. This first visual impression was quantified by comparing the average distance of any two proteins of the same function to the average distance of all protein pairs. Fig. 10b (right) shows the mutual average distance in the graph for each function class (bar heights), i.e. the number of edges connecting two proteins of the same function, as well as the standard deviation of that average. As can be seen, proteins of the same function class are, overall, significantly closer to one another than the average distance of all vertices in the graph (black horizontal line), which one would expect in the absence of any correlation between dynamics and function. Exceptions are the classes DNA/Transcription and Toxins. The fact that functionally similar proteins occupy similar regions of the dynamics space suggests a straightforward way to infer function purely from dynamics similarity by partitioning the dynamics space into ‘function neighborhoods’, i.e. areas of the dynamics space which are occupied preferentially by a given function class. Accordingly, the centroids of these function neighborhoods serve as the reference points, and proteins of unknown function are then predicted to share the function of their closest neighborhood (the function class with the lowest average graph distance). To quantify the predictive power of this approach, we determined if this procedure would have predicted the correct function class. To that aim, the shortest path from each protein to all other proteins of known function was calculated. We then checked whether its known function corresponds to the function of the closest function class, in which case we would have obtained a correct assignment. Remarkably, correct assignments were found in 57% of all cases, as compared to 11% expected in the absence of any correlation between dynamics and function. A detailed comparison by function class (Table S3) suggests different success rates for the different function classes. The dynamics fingerprint of glycosidases (12 correct assignments out of 17) seems to be quite characteristic for this function class, whereas esterases dynamics turned out to be more diffuse, allowing only 4 out of 13 proteins to be assigned correctly. For rigorous cross-validation, the above algorithm was modified such that for each protein assumed unknown, the function centroid was re-calculated from the remaining proteins only. As above, the predictive power was then assessed via similarity of the functional class of each protein with that of the closest centroid. Focussing at the three largest function groups for which sufficient proteins (.10) are available to obtain reasonable statistical accuracy, correct assignments were obt’ained in 46% of all cases (Table S3), which is only slightly below the above correlation, thus establishing remarkable predictive power of this simple approach. 

 For the remaining and quite small function classes, a value of only 7% is obtained due to poor statistics, such that predictive power is not established for these classes. Having established a clear dynamics function correlation we next examined whether, with a similar approach, similar correlations are seen between structure and function. To this end, we computed the adjacency matrix of proteins in structure space. The resulting graph is shown in Fig. 10c (left; and Fig. S6, centre column). Similar to dynamics space, local accumulations of function classes can be seen, also yielding significantly lower than average intra-class distances for most function classes (bar plot Fig. 10c right). This observation corroborates the well-known fact that structural alignments can in many cases improve protein function predictions [7]. With an approach similar to that applied to the dynamics fingerprints above, we found a structure/function correlation of 36%, smaller than the dynamics/function correlation above (Table S3). The cross-correlation test yields 27% correct annotations for the three larger groups, and 39% for the remainder. The overall prediction rate of 32% agrees well with published structure based prediction rates [7]. Similar to the prediction based on dynamics, cross-validated prediction rates are only 2% smaller than the observed correlations for the three largest function classes, but drop by 8% for the small groups for which the statistics is poor. Would one expect to improve the prediction rate even further by using both, structure and dynamics information? At first sight, this should be the case, particularly for those function classes, which form relatively compact clusters in dynamics space, but are structurally quite unrelated (e.g., calcium binding proteins). In these cases, a better prediction rate is expected for a purely dynamics based function prediction than for a purely structure based one. However, other function classes (e.g., peptidases) appear to form compact clusters in structure but not in dynamics space. For these classes, structure based predictions should be superior. Due to this complementarity, it is not clear a priori whether or not the combined use of structure and dynamics actually will improve function prediction rates. To resolve this issue, we combined our structure and dynamics space into a 34+24 = 58 dimensional space. Similarly to the above procedure, a PCA on the respective combined descriptors was carried out, and adjacency relations in the space spanned by the first five (d~5) collective descriptors were obtained from the PCA. Note that this 5-dimensional subspace does not necessarily weight dynamics and structural features equally. Figure 10d (left) shows the resulting graph of the calculated adjacency matrix. Analysis of the underlying adjacency matrix shows that proteins of common function class are, on average, closer to each other in this combined space than they are in dynamics and structure space alone (Fig. 10d right; and Fig. S6, right column), whereas the average distance in this graph is also markedly smaller. Using both structure and dynamics information, 35% correct annotations are achieved, slightly more than structure and dynamics based predictions alone. We note that more elaborate combinations of structure and dynamics space, and optimized choices of k and d are likely to further improve the predictive value of our approach. 

## Conclusions 

 Inspired by the successful classifications of the sequence and structure space covered by proteins, we investigated the dynamics space covered by small, soluble proteins chosen from many structural families and folds. The dynamics of each protein was characterized by a set of 34 dynamics descriptors spanning the 

Figure 10. Dynamics fingerprints and relation to function. a) Compass diagrams indicate the average position of each function class in the dynamics space spanned by dynasome descriptors 1–4 (see Table 3 for composition of descriptors). b–d) Graphs of adjacency matrices (left) in the dynamics space (b), structure space (c) and combined space (d) and corresponding average distances (right) between proteins of the same function classes (bar heights) vs average distance (solid horizontal lines) between all proteins. The colors denote the protein function classes defined in panel a. doi:10.1371/journal.pone.0033931.g010 

dynamics space. We referred to the whole set of protein dynamics patterns as the dynasome. Remarkably, the grand distinction between thermodynamics and kinetics properties of a manyparticle system was found to be already encoded, in terms of the directions of its two largest extensions, within the structure of the dynasome. The first question we addressed was whether or not these proteins naturally fall into dynamics classes, such as seen for the more established sequence and structure classifications. We found that proteins populate the dynamics space continuously, and no canonical partitioning, which would enable an unambiguous classification, was seen. The observation that functionally unusual proteins appear as outliers in this dynamics space provided a first hint towards a close connection between function and dynamics. A systematic analysis of the dynasome indeed revealed remarkably large correlations between dynamics and protein function. Functional classes leave distinct ‘‘fingerprints’’ in the dynasome, which we were able to characterize using only a few collective dynasome descriptors. The finding that proteins of similar function cluster in dynamics space led us to a new and straightforward protein function prediction approach, purely based on protein dynamics similarity. Indeed, already for the relatively small set of proteins considered here, such an approach yielded correct annotations for 46% of the largest functional classes, which is comparable to the performance of the most advanced structure based methods. A second set of questions addressed was how protein structure relates to protein dynamics and, in particular, to which extent structurally similar proteins exhibit similar dynamics. We characterized protein structure using the same unsupervised approach as for protein dynamics. In this case, protein structure was represented by a 24 dimensional vector of structure descriptors. The structural similarity between any two proteins was then quantified by the distance in structure space, different from the usual approach based on RMSDs between subsets of atoms (e.g. Caatoms) according to some domain hierarchy. As one might expect, many structurally similar proteins were found to exhibit similar dynamics and, vice versa, many structurally different proteins tend to perform different dynamics, thus establishing significant structure-dynamics correlation. In a significant number of cases, however, this straightforward structure-dynamics relation was found to be violated. Quite different structures shared similar motion patterns (‘adjoint’), and other very similar structures exhibited quite different dynamics (‘disjoint’). In these cases, dynamics relations offer a viewpoint that is complementary to that derived from structural characterizations. To decide which of the two views is more closely linked to protein function, we also investigated how well function can be determined purely from structure within our framework and obtained a success rate of 32%. Combining structure and dynamics information yielded an intermediate rate of 35%, a slightly higher value than either dynamics or structure based predictions alone. It seems likely, that prediction methods can be devised which combine the information from structure and dynamics in a more elaborate manner, and thus enable even more accurate predictions, e.g. optimizing the parameters d and k for this specific purpose. The findings presented in this study are remarkable in the light of the fact that our dynamics descriptors, being derived from 100 ns simulations, provide a quite limited ‘‘window’’ to the full dynamics. In particular slow dynamics are entirely missed, as are other dynamics features that are not captured by our observables. Despite this fact, however, our limited view seems to suffice, to predict protein function at a remarkable rate, and therefore captures functionally relevant 

 parts of the dynamics. By analogy, to identify a murderer, one does not always require a photograph of his whole body, often a fingerprint suffices. Here, we presented fingerprints of protein dynamics. 

## Supporting Information 

 Figure S1 Observable correlation. Pairwise absolute Pearson’s correlation coefficients (color codes see legend) between the dynamics observables used in this study. Observables indices correspond to main Table 2. (TIFF) Figure S2 Principle of decorrelation between two arbitrary variables xand y. The correlation seen in (a) is removed by applying a random permutation to the y-component (b). (TIFF) Figure S3 Parameter optimization for mutual adjacency graphs. The k nearest neighbors, which define the connectivity of each protein in the d dimensional subspace of the a) dynamics, b) structure, c) combined dynamics and structure space. The partitioning of each resulting graph for each pair {k,d} is quantified by the community modularity C (z-axis). For the subsequent analyses, k and d were chosen such that C was maximized (black points). (TIFF) Figure S4 Determination of natural partitioning of the dynasome. Average Connectivity (x-axis) vs Average Variance (y-axis) for k-means partitioning into 1 ... 10 clusters (numbers). For the optimal number of clusters, both measures are minimal. For the dynasome, no such optimal number could be identified. (TIFF) Figure S5 Graph of a adjacency matrix of dynasome proteins in the dynamics space. Vertex colours indicate (a) kmeans clusters in the whole 34-dimensional dynamics space (same clusters like main text Fig. 6b), (b) SCOP classes of proteins. (TIFF) Figure S6 Co-location of proteins of the same functional class distinct functional classes in the neighborhood plot of the dynamics space (left column), structure space (middle column), and combined dynamics and structure space (right column). Colors indicate function classes according to the colour code in main text Fig. 10. (TIFF) Table S1 Systems (PDB codes) selected for analysis. Functions were obtained as described in methods. Poorly covered function classes were assigned ‘‘Other’’ and ‘‘Other Enzymes’’ and not included in the graph analyses. (TEX) Table S2 Fit functions for Sequence length decorrelation of dynamic (Y 1 {^34 ) and structure (X 1 {^24 ) observables. (TEX) Table S3 Prediction rate by function class. Numbers in brackets indicate the result of a cross validation test, described in the main text. (TEX) TEXT S1 The graphs are a faithful map of the dynasome. (PDF) 

## Acknowledgments 

We thank Bert de Groot, Stephanus Fengler, and Uli Zachariae for helpful discussions, and Serena Donnini, Bela Voß, Uli Zachariae and Andreas Russek for proof reading. 

## Author Contributions 

 Conceived and designed the experiments: UH TM HG. Performed the experiments: TM JH. Analyzed the data: UH TM RR HG. Contributed reagents/materials/analysis tools: UH TM RR JH. Wrote the paper: UH TM GV HG. 

## References 

1. Anfinsen C, Haber E (1961) Studies on the reduction and re-formation of     protein disulfide bonds. J Biol Chem 236: 1361–1363. 

2. Erdin S, Lisewski AM, Lichtarge O (2011) Protein function prediction: towards     integration of similarity metrics. Curr Opinion Struct Biol 21: 180–188. 

3. Chothia C, Lesk A (1986) The relation between the divergence of sequence and     structure in proteins. EMBO J 5: 823–826. 

4. Sander C, Schneider R (1991) Database of homology-derived protein structures     and the structural meaning of sequence alignment. Proteins 9: 56–68. 

5. Wilson C, Kreychman J, Gerstein M (2000) Assessing annotation transfer for     genomics: Quantifying the relations between protein sequence, structure and     function through traditional and probabilistic scores. J Mol Biol 297: 233–249. 

6. Devos D, Valencia A (2000) Practical limits of function prediction. Proteins 41:     98–107. 

7. Whisstock J, Lesk A (2003) Prediction of protein function from protein sequence     and structure. Q Rev Biophys 36: 307–340. 

8. Altschul S, Gish W, Miller W, Myers E, Lipman D (1990) Basic Local Alignment     Search Tool. J Mol Biol 215: 403–410. 

9. Altschul S, Madden T, Schaffer A, Zhang J, Zhang Z, et al. (1997) Gapped     BLAST and PSI-BLAST: A new generation of protein database search     programs. Nucleic Acids Res 25: 3389–3402. 

10. Skolnick J, Kolinski A, Kihara D, Betancourt M, Rotkiewicz P, et al. (2002) Ab     initio protein structure prediction via a combination of threading, lattice folding,     clustering, and structure refinement. Proteins 45: 149–156. 

11. Jones D, Tress M, Bryson K, Hadley C (1999) Successful recognition of protein     folds using threading methods biased by sequence similarity and predicted     secondary structure. Proteins 3: 104–111. 

12. Hildebrand A, Remmert M, Biegert A, So ̈ ding J (2009) Fast and accurate     automatic structure prediction with HHpred. Proteins 77: 128–132. 

13. von Grotthuss M, Plewczynski D, Vriend G, Rychlewski L (2008) 3D-Fun:     predicting enzyme function from structure. Nucleic Acids Res 36: W303–W307. 

14. Pearl F, Bennett C, Bray J, Harrison A, Martin N, et al. (2003) The CATH     database: an extended protein family resource for structural and functional     genomics. Nucleic Acids Res 31: 452–455. 

15. Andreeva A, Howorth D, Brenner S, Hubbard T, Chothia C, et al. (2004)     SCOP database in 2004: refinements integrate structure and sequence family     data. Nucleic Acids Res 32: D226–D229. 

16. Holm L, Sander C (1996) Mapping the protein universe. Science 273: 595–602. 

17. Pascual-Garcia A, Abia D, Mendez R, Nido GS, Bastolla U (2010) Quantifying     the evolutionary divergence of protein structures: The role of function change     and function conservation. Proteins 78: 181–196. 

18. Perutz M (1970) Stereochemistry of cooperative effects in haemoglobin. Nature     228: 726–734. 

19. Ansari A, Berendzen J, Bowne S, Frauenfelder H, Iben I, et al. (1985) Protein     states and proteinquakes. Proceedings of the National Academy of Sciences 82:     5000–5004. 

20. de Groot B, Grubmuller H (2001) Water permeation across biological     membranes: Mechanism and dynamics of aquaporin-1 and glpf. Science 294:     2353–2357. 

21. Pang A, Arinaminpathy Y, Sansom M, Biggin P (2005) Comparative molecular     dynamics - similar folds and similar motions? Proteins 61: 809–822. 

22. Yaneva R, Springer S, Zacharias M (2009) Flexibility of the MHC class II     peptide binding cleft in the bound, partially filled, and empty states: A molecular     dynamics simulation study. Biopolymers 91: 14–27. 

23. Cox K, Sansom M (2009) One membrane protein, two structures and six     environments: a comparative molecular dynamics simulation study of the     bacterial outer membrane protein pagp. Mol Membr Biol 26: 205–214. 

24. Meyer T, de la Cruz X, Orozco M (2009) An atomistic view to the gas phase     proteome. Structure 17: 88–95. 

25. Jonsson AL, Scott KA, Daggett V (2009) Dynameomics: A consensus view of the     protein unfolding/folding transition state ensemble across a diverse set of protein     folds. Biophys J 97: 2958–2966. 

26. Toofanny RD, Jonsson AL, Daggett V (2010) A comprehensive multi-     dimensionalembedded, one-dimensional reaction coordinate for protein unfold-     ing/folding. Biophys J 98: 2671–2681. 

27. van der Kamp MW, Schaeffer RD, Jonsson AL, Scouras AD, Simms AM, et al.     (2010) Dynameomics: A comprehensive database of protein dynamics. Structure     18: 423–435. 

28. Meyer T, D’Abramo M, Hospital A, Rueda M, Ferrer-Costa C, et al. (2010)     MoDEL (Molecular Dynamics Extended Library): A database of atomistic     molecular dynamics trajectories. Structure 18: 1399–1409. 

29. Shaw DE (2009) Anton: A specialized machine for millisecond-scale molecular     dynamics simulations of proteins. Abstr Pap Am Chem S 238: 154-COMP. 

30. Shaw D, Maragakis P, Lindorff-Larsen K, Piana S, Dror R, et al. (2010) Atomic-     level characterization of the structural dynamics of proteins. Science 330:     341–346. 

31. Amadei A, Linssen A, Berendsen H (1993) Essential dynamics of proteins.     Proteins 17: 412–425. 

32. Zen A, Carnevale V, Lesk AM, Micheletti C (2008) Correspondences between     lowenergy modes in enzymes: Dynamics-based alignment of enzymatic     functional families. Protein Sci 17: 918–929. 

33. Munz M, Lyngso R, Hein J, Biggin P (2010) Dynamics based alignment of     proteins: an alternative approach to quantify dynamic similarity. BMC     Bioinformatics 11: 188. 

34. Hooft R, Sander C, Scharf M, Vriend G (1996) The PDBFINDER database: a     summary of PDB, DSSP and HSSP information with added value. Bioinfor-     matics 12: 525–529. 

35. Henrick K, Thornton J (1998) PQS: a protein quaternary structure file server.     Trends Biochem Sci 23: 358–361. 

36. Hooft R, Vriend G, Sander C, Abola E (1996) Errors in protein structures.     Nature 381: 272–272. 

37. Vriend G (1990) WHAT IF: a molecular modeling and drug design program.     J Mol Graph 8: 52–56. 

38. Haas J, Lange O, Vriend G, de Groot B, Grubmuller H WHAG – GROMACS     interface to WHATIF. to be submitted). 

39. Hooft R, Sander C, Vriend G (1996) Positioning hydrogen atoms by optimizing     hydrogen-bond networks in protein structures. Proteins 26: 363–376. 

40. Spoel DVD, Lindahl E, Hess B, Groenhof G, Mark A, et al. (2005) GROMACS:     Fast, flexible, and free. J Comp Chem 26: 1701–1718. 

41. Jorgensen W, Tiradorives J (1988) The OPLS potential functions for proteins –     Energy minimizations for crystals of cyclic peptides and crambin. J Am Chem     Soc 110: 1657–1666. 

42. Berendsen H, Postma J, van Gunsteren W, DiNola A, Haak J (1984) Molecular     dynamics with coupling to an external bath. J Chem Phys 81: 3684–3691. 

43. Hess B, Bekker H, Berendsen H, Fraaije J (1997) LINCS: A linear constraint     solver for molecular simulations. J Comp Chem 18: 1463–1472. 

44. Miyamoto S, Kollman P (1992) SETTLE - An analytical version of the SHAKE     and RATTLE algorithm for rigid water models. J Comp Chem 13: 952–962. 

45. Darden T, York D, Pedersen L (1993) Particle Mesh Ewald - an N.Log(N)     method for Ewald sums in large systems. J Chem Phys 98: 10089–10092. 

46. Hess B (2000) Similarities between principal components of protein dynamics     and random diffusion. Phys Rev E 62: 8438–8448. 

47. Uhlenbeck GE, Ornstein LS (1930) On the theory of the Brownian motion. Phys     Rev 36: 823–841. 

48. Zwanzig R (1988) Diffusion in a rough potential. P Natl Acad Sci Usa 85:     2029–2030. 

49. Kabsch W, Sander C (1983) Dictionary of protein secondary structure –     patternrecognition of hydrogen-bonded and geometrical features. Biopolymers     22: 2577–2637. 

50. Case DA, Darden TA, Cheatham TE, Simmerling CL, Wang J, et al. (2008)     AMBER 10, University of California, San Francisco. 

51. Hubbard, Thornton J (1993) NACCESS - atomic solvent accessible area     calculations – computer program. URL [http://www.bioinf.manchester.ac.uk/](http://www.bioinf.manchester.ac.uk/)     naccess/. Last accessed 2012 Mar 15. 

52. Hess B, Kutzner C, van der Spoel D, Lindahl E (2008) GROMACS 4:     Algorithms for highly efficient, load-balanced, and scalable molecular simula-     tion. J Chem Theory Comput 4: 435–447. 

53. Ahmad S, Sarai A (2011) Analysis of electric moments of RNA-binding proteins:     implications for mechanism and prediction. BMC Structural Biology 11: 8. 

54. Vendruscolo M, Dokholyan N, Paci E, Karplus M (2002) Small-world view of     the amino acids that play a key role in protein folding. Phys Rev E 65: 061910. 

55. Seber GAF (1984) Cluster Analysis, in Multivariate Observations, John Wiley &     Sons, Inc., Hoboken, NJ, USA. 

56. Bairoch A, Bougueleret L, Altairac S, Amendolia V, Auchincloss A, et al. (2008)     The universal protein resource (uniprot). Nucleic Acids Research 36:     D190–D195. 

57. Berman H, Westbrook J, Feng Z, Gilliland G, Bhat T, et al. (2000) The protein     data bank. Nucleic Acids Res 28: 235–242. 

58. Kitao A, Go ̄ N (1991) Conformational dynamics of polypeptides and proteins in     the dihedral angle space and in the cartesian coordinate space: Normal mode     analysis of deca-alanine. J Comput Chem 12: 359–368. 

59. Kitao A, Go N (1999) Investigating protein dynamics in collective coordinate     space. Curr Opinion Struct Biol 9: 164–169. 

60. Handl J, Knowles J, Kell D (2005) Computational cluster validation in post-     genomic data analysis. Bioinformatics 21: 3201–3212. 

61. Sadreyev R, Kim BH, Grishin N (2009) Discrete-continuous duality of protein     structure space. Current opinion in structural biology 19: 321–328. 

62. Skolnick J, Arakaki A, Lee S, Brylinski M (2009) The continuity of protein     structure space is an intrinsic property of proteins. Proceedings of the National     Academy of Sciences 106: 15690–15695. 

63. Pascual-Garcia A, Abia D, Ortiz AR, Bastolla U (2009) Cross-over between     discrete and continuous protein structure space: Insights into automatic     classification and networks of protein structures. PLoS Comput Biol 5:     e1000331. 

64. Holm L, Sander C (1997) New structure – novel fold? Structure 5: 165–171. 

65. Hou J, Jun SR, Zhang C, Kim SH (2005) Global mapping of the protein     structure space and application in structure-based inference of protein function.     Proc Natl Acad Sci USA 102: 3651–3656. 

66. Sadowski M, Taylor W (2010) On the evolutionary origins of "fold space     continuity": A study of topological convergence and divergence in mixed alpha-     beta domains. J Struct Biol 172: 244–252. 

67. Lisewski A, Lichtarge O (2006) Rapid detection of similarity in protein structure     and function through contact metric distances. Nucleic Acids Res 34:     e152–e152. 

68. Keskin O, Jernigan R, Bahar I (2000) Proteins with similar architecture exhibit     similar large-scale dynamic behavior. Biophys J 78: 2093–2106. 

69. Hasegawa H, Holm L (2009) Advances and pitfalls of protein structural     alignment. Curr Opinion Struct Biol 19: 341–348. 

70. Clauset A (2005) Finding local community structure in networks. Phys Rev E 72:     026132. 

71. Ban C, Ramakrishnan B, Ling K, Kung C, Sundaralingam M (1994) Structure     of the recombinant paramecium-tetraurelia calmodulin at 1.68 angstrom     resolution. Acta Crystallogr D 50: 50–63. 

72. Smith J, Corfield P, Hendrickson W, Low B (1988) Refinement at 1.4 A ̊     resolution of a model of erabutoxin-B - treatment of ordered solvent and discrete     disorder. Acta Crystallogr A 44: 357–368. 

73. Tsunawasa S, Masaki T, Hirose M, Soejima M, Skaiyama F (1989) The primary     structure and structural characteristics of achromobacter-lyticus protease-I, a     lysinespecific serine protease. J Biol Chem 264: 3832–3839. 

74. Saarinen M, Gleason F, Eklund H (1995) Crystal structure of thioredoxin-2 from     Anabaena. Structure 3: 1097–1108. 

75. Papageorgiou A, Tranter H, Acharya K (1998) Crystal structure of microbial     superantigen staphylococcal enterotoxin B at 1.5 A ̊^ resolution: implications for     superantigen recognition by mhc class ii molecules and t-cell receptors.     J Molecular Biology 277: 61–79. 

76. Acharya K, Shapiro R, Riordan J, Vallee B (1995) Crystal-structure of bovine     angiogenin at 1.5-angstrom resolution. P Natl Acad Sci USA 92: 2949–2953. 

77. Kraulis P (1991) MOLSCRIPT: a program to produce both detailed and     schematic plots of protein structures. J App Cryst 24: 946–950. 



---

# Structural Ensembles of Intrinsically Disordered Proteins Depend Strongly on Force Field: A Comparison to Experiment

**Authors:** Sarah Rauscher, Vytautas Gapsys, Michal J. Gajda, Markus Zweckstetter, Bert L. de Groot, Helmut Grubmüller
**Year:** 2015
**Venue:** Journal of Chemical Theory and Computation
**DOI:** 10.1021/acs.jctc.5b00736
**Source PDF URL:** https://pure.mpg.de/rest/items/item_2231185_2/component/file_2231188/content
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

## Structural Ensembles of Intrinsically Disordered Proteins Depend 

## Strongly on Force Field: A Comparison to Experiment 

## Sarah Rauscher,*,†Vytautas Gapsys,†Michal J. Gajda,‡Markus Zweckstetter,‡,§,∥Bert L. de Groot,† 

## and Helmut Grubmüller† 

†Department of Theoretical and Computational Biophysics, Max Planck Institute for Biophysical Chemistry, Göttingen 37077, 

Germany ‡Department of NMR-based Structural Biology, Max Planck Institute for Biophysical Chemistry, Göttingen 37077, Germany 

§German Center for Neurodegenerative Diseases (DZNE), Göttingen 37077, Germany 

∥Center for Nanoscale Microscopy and Molecular Physiology of the Brain (CNMPB), University Medical Center, Göttingen 37073, 

 Germany 

### *S Supporting Information 

 ABSTRACT: Intrinsically disordered proteins (IDPs) are notoriously challenging to study both experimentally and computationally. The structure of IDPs cannot be described by a single conformation but must instead be described as an ensemble of interconverting conformations. Atomistic simulations are increasingly used to obtain such IDP conformational ensembles. Here, we have compared the IDP ensembles generated by eight all-atom empirical force fields against primary small-angle X-ray scattering (SAXS) and NMR data. Ensembles obtained with different force fields exhibit marked differences in chain dimensions, hydrogen bonding, and secondary structure content. These differences are unexpectedly large: changing the force field is found to have a stronger effect on secondary structure content than changing the entire peptide sequence. The CHARMM 22*ensemble performs best in this force field comparison: it has the lowest error in chemical shifts and J-couplings and agrees well with the SAXS data. A high population of left-handed α-helix is present in the CHARMM 36 ensemble, which is inconsistent with measured scalar couplings. To eliminate inadequate sampling as a reason for differences between force fields, extensive simulations were carried out (0.964 ms in total); the remaining small sampling uncertainty is shown to be much smaller than the observed differences. Our findings highlight how IDPs, with their rugged energy landscapes, are highly sensitive test systems that are capable of revealing force field deficiencies and, therefore, contributing to force field development. 

# ■ INTRODUCTION 

Intrinsically disordered proteins (IDPs) carry out crucial biological functions in all kingdoms of life.1^ The human proteome is estimated to contain approximately a million disordered motifs, which often act as signals in cellular pathways, including protein degradation, trafficking, and targeting.2^ IDP aggregation is involved in diverse cellular functions including the selective passage of material through the nuclear pore complex3 and the segregation of materials in membrane-less organelles via intracellular phase separation.4,5 A fundamental understanding of the structural properties of IDPs is crucial to understanding the wide range of cellular functions relying on protein disorder. An IDP by definition cannot be described by a single average structure but instead must be described as an ensemble of interconverting conformations. Obtaining accurate structural ensembles of IDPs is the aim of many recent studies, both experimental and computational.6,^7 The protein ensemble 

 database (pE-DB),8^ which is analogous to the PDB for structures of folded proteins, contains a growing collection of IDP ensembles. On the experimental side, nuclear magnetic resonance (NMR), small-angle X-ray scattering (SAXS), and single-molecule spectroscopy have emerged as highly useful and complementary methods for obtaining structural information.6,^9 Fluorescence resonance energy transfer (FRET), fluorescence correlation spectroscopy (FCS), and SAXS provide measurements of overall chain dimensions. NMR spectroscopy provides site-specific information, for example, on secondary structure content and distances between labeled sites as well as measurements of hydrodynamic radius using pulsed field gradient NMR (PFG-NMR).10 On the theory side, a variety of computational methods have been developed to obtain structural ensembles of IDPs. These 

 Received: August 3, 2015 Published: October 9, 2015 

 Article pubs.acs.org/JCTC 

 © 2015 American Chemical Society 5513 DOI: 10.1021/acs.jctc.5b00736 

methods can be broadly classified into two types: (1) those that use experimental data to guide ensemble generation or selection, and (2) those that generate ensembles of IDPs de novo, that is, without using experimental data as an input. An example of the first type of method is the use of experimental data as restraints in simulations. For instance, NMR chemical shift restraints and distance restraints based on paramagnetic relaxation enhancement (PRE) measurements were used in molecular dynamics (MD) simulations of the denatured state of ACBP and α-synuclein, respectively.11−^13 Other computational methods, such as ENSEMBLE14 and ASTEROIDS,15 use experimental data to select ensembles from pregenerated pools of conformations. Ensembles consistent with experimental data have also been selected from conformations obtained using MD simulations.16−18 Ball et al. compared knowledge-based ensemble selection approaches to ensembles obtained using de novo MD simulations.17 Because IDP ensembles are severely underdetermined (that is, there are many degrees of freedom and relatively few experimental observables), cross-validation and care in avoiding overfitting are essential to these approaches.16,^19 ,^20 Computational methods of the second type have been used extensively to obtain ensembles of IDPs de novo. A variety of simulation methods (MD, Monte Carlo, metadynamics, replica exchange) and different levels of representation (coarsegrained, implicit solvent, all-atom with explicit water) have been used to obtain IDP ensembles.7,^21 −29 There are two main challenges encountered in de novo simulations. First, extensive simulations are needed to ensure that relevant regions of conformational space are adequately sampled. Although this requirement applies to all biomolecular simulations, it presents a particularly formidable challenge in the case of IDPs due to their high conformational heterogeneity. Second, and more importantly, the accuracy of modern force fields for IDP simulations is not well-characterized. MD simulations have been used to study the structure and dynamics of folded proteins for decades.30 During this time, substantial effort has been put into the development and improvement of empirical force fields. The accuracy of the description of the structure and dynamics of globular proteins, as well as that of the relative stabilities of different types of secondary structure, were improved in the CHARMM and Amber force fields.31−34 Systematic force field comparison studies have shown that, overall, force field modifications indeed tend to be improvements: simulations with more recently developed force fields produce more accurate ensembles of globular proteins compared to the older force fields on which they are based.35,^36 Some modern force fields describe small, globular proteins quite well: NMR observables computed from these ensembles agree with experimental values within the error expected for the calculation of these observables.36,37 In a recent comparison of force fields for folded proteins, Amber ff99sb*-ildn and CHARMM22*were the only two force fields consistent with experimental data.35 In contrast, force fields have been shown to differ significantly in their ability to fold proteins,38 especially in the challenging task of folding proteins from multiple structural classes.35 A study of villin headpiece aggregation using different force fields and solution conditions suggested that protein−protein interactions generally tend to be overestimated: all of the force fields in this study showed aggregation and are therefore inconsistent with experimental evidence indicating no aggregation.39 

 Many force field modifications have been directed at improving the accuracy of conformational ensembles of globular proteins. In contrast, most force fields have not been developed for simulations of IDPs. Several recent force field modifications have improved the balance of secondary structure propensities to be able to fold proteins of multiple structural classes. It would in fact be somewhat surprising if accurate IDP ensembles could be obtained using a force field optimized only for folded proteins. Nevertheless, all-atom simulations are increasingly being used to obtain ensembles of IDPs (see recent studies 23 , 24 , and 40 − 43 ). It is difficult to draw conclusions on the accuracy of IDP simulations from the contradictory findings reported so far. On the one hand, good agreement between computed and measured experimental observables was observed in some IDP simulations.23−^25 ,^27 ,^28 ,^42 ,^44 −^46 On the other hand, the accuracy of unfolded state and IDP structural ensembles obtained using several widely used force fields has been called into question.25−^27 ,^43 ,^46 −53 Piana et al. suggested that modern force fields, including Amber ff99sb*-ildn and CHARMM 22* in particular, produce IDP and unfolded state ensembles that are on average too compact.48 It has also been suggested that Amber force fields systematically underestimate chain dimensions of IDPs and unfolded states.51 To address these force field deficiencies, a new water model, TIP4P-D,26 and new force field, Amber 03ws,51 were recently introduced. While these recent studies demonstrate a substantial interest in obtaining accurate ensembles of IDPs using all-atom simulations, there is currently no consensus on the most accurate force field or the suitability of any force field for this purpose. Information on the accuracy of IDP ensembles is sparse, anecdotal, and contradictory, which may be due a combination of multiple factors: (1) inadequate conformational sampling of IDP ensembles, (2) comparisons to models derived from primary experimental data rather than the primary data itself, and (3) comparisons to relatively few (and sometimes only one) observables. In the absence of a comprehensive comparison, it is not surprising that a consensus is currently lacking concerning the accuracy of IDP simulations. Here, we aim to evaluate the accuracy of IDP ensembles obtained using de novo molecular simulations. Toward this aim, we compared ensembles obtained using eight all-atom empirical force fields (Table 1) to primary SAXS and NMR data. For reasons of computational feasibility, we included only eight force fields. We addressed the sampling problem using temperature replica exchange54 as well as extensive sampling, accumulating a total sampling time of 964 μs (a detailed list of simulations is provided in Table S1). 

 Table 1. Force Fields Included in the Comparison 

 force field (abbreviation) peptide force field water model Amber ff99sb*-ildn (a99sb) 

 Amber ff99sb*ildn33^ 

 TIP3P55 

 Amber ff03w (a03w) Amber ff03w34^ TIP4P-200556 Amber ff03ws (a03ws) Amber ff03ws51^ TIP4P-200556 ABSINTH (ABS) OPLS-AA/L57^ ABSINTH implicit solvent21 CHARMM 22*(c22*) CHARMM 22*^33 charmm-modified TIP3P31 CHARMM 22*(c22*/ D) 

 CHARMM 22*^33 TIP4P-D26 

 CHARMM 361 (c361) CHARMM 3658^ TIP3P55 CHARMM 362 (c362) CHARMM 3658^ charmm-modified TIP3P31 

 DOI: 10.1021/acs.jctc.5b00736 5514 

For such a comparative study, the choice of model system is crucial. The model system must be small enough to make it possible to obtain adequate sampling for each force field. In addition, and more importantly, experimental data characterizing both local and global structural properties are needed. We chose a set of sequences that cover a broad spectrum of sequence properties from highly charged in the case of a disordered arginine/serine (RS) peptide to uncharged and enriched in polar and hydrophobic residues in the case of FGnucleoporin peptides. The RS peptide is a well-suited IDP for this comparison, it has previously been extensively characterized by multiple NMR experiments by Xiang et al.16 as well as by SAXS experiments in this work. Its small size (24 residues) makes it feasible to perform extensive simulations using multiple force fields with current computational capabilities. The RS peptide undergoes a phosphorylation-induced reduction in conformational entropy, which is thought to be important in modulating protein-RNA interactions.16 Here, we carried out simulations of only the unphosphorylated form. Two FG-nucleoporin peptides with sequences based on the sequence of yeast Nsp1p59 were also studied. These peptides differ in length (16 residues and 50 residues). FG-nucleoporins are a well-studied class of IDPs that are characterized by the presence of FG motifs and are essential for the selectivity of the nuclear pore complex.60 We also studied (AAQAA)3 and the HEWL peptide, which is a 19residue sequence derived from hen egg white lysozyme.58 

# ■ METHODS 

Simulations. The RS peptide was built in a fully extended configuration in PYMOL with protonation states to match experimental conditions (arginine residues as well as the Nand C-termini were simulated in their charged states). The simulation system consisted of the peptide in a rhombic dodecahedral box with water molecules and 0.15 M NaCl for a total of ∼42000 atoms. GROMACS version 4.5.461 was used for all simulations. Prior to the production runs, energy minimization with the steepest descent algorithm was performed. The lengths of bonds with hydrogen atoms were constrained using the LINCS algorithm.62 An integration time step of 2 fs was used. A cutoffof 0.95 nm was used for the Lennard-Jones interactions and short-range electrostatic interactions. Long-range electrostatic interactions were calculated by particle-mesh Ewald summation with a grid spacing of 0.12 nm and a fourth order interpolation.63 The velocity rescaling thermostat was used for all simulations.64 Equilibration was performed at 298 K for 1 ns using Berendsen pressure coupling65 followed by 5 ns of simulation in the NPT ensemble using the Parrinello−Rahman algorithm.66 The configuration from this simulation with a volume closest to the average volume was then used for subsequent replica exchange (RE)54 simulations in the canonical ensemble. A total of 97 temperatures between 298 and 450 K were used with a mean acceptance ratio of 0.35. Temperature exchanges were attempted every 2 ps for a total of 97 μs (1 μs of simulation per temperature). Coordinates were stored before each temperature exchange; a total of 0.5 × 106 configurations were collected per temperature. Simulations with the TIP4P-D water model26 were carried out without replica exchange, consistent with Piana et al.,26 as conformational sampling in this force field is fast, and RE was not needed to obtain sufficient sampling, comparable to the other force fields. Simulations with the ABSINTH21 implicit solvent model were carried out with 

 the CAMPARI software following a similar protocol to Das and Pappu.67 The CAMPARI parameter set abs3.2_opls.prm was used for the peptide, and the ion parameters of Mao and Pappu were used.68 In Table S2, we provide the details of the Monte Carlo move set used. Visual molecular dynamics (VMD) was used for all molecular visualizations.69 Analysis of Structural Ensembles. The GROMACS utilities g_gyrate and g_hbond were used to calculate the radius of gyration, Rg, and number of hydrogen bonds, respectively. Secondary structure was assigned according to the DSSP algorithm.70 Contacts between residue pairs were defined if any two atoms were within a cutoffof 4.5 Å. Left handed α-helix was defined as three or more consecutive residues in the αL basin of the Ramachandran plot. Standard error of the mean was computed using a blocking procedure.71 For each simulation, an equilibration period was delineated on the basis of both Rg and hydrogen bonds; this initial collapse of the peptide to more compact conformations was excluded from analysis. Computing Experimental Observables. SAXS scattering curves were computed individually for every conformation in each ensemble using two different approaches, CRYSOL72 and FOXS.73 Ensemble-averaged scattering curves were computed for each force field. Each of these curves were fit to the experimental curve following the fitting procedure used by Chen et al.74 The software PRIMUS75 was used to compute the Rg from each scattering curve using Guinier analysis. The hydrodynamic radius, Rh, was computed for each configuration using HYDROPRO76 with the parameters of Mao et al.45 Comparison is made to the hydrodynamic radius measured using pulse-field-gradient NMR by Xiang et al.16 The Karplus equation parameters used to calculate scalar couplings are given in Table S3.77−81 RMS errors for the calculation of J couplings are 0.73 Hz (3JHNHα), 0.5 Hz (1JCαCβ), 2 Hz (1JCαHα), 0.38 Hz (3JNCγand 3JCCγ).77−81 Chemical shifts were calculated using both SHIFTX282 and SPARTA+.83 The reported errors for SHIFTX2 are the lowest of any chemical shift predictor (0.4412 ppm for Cαand 0.5330 ppm for C′).82 The RMS errors for SPARTA+ are 0.94 ppm for Cαand 1.09 ppm for C′.83 The errors may be higher when applied to IDPs. All of the computed NMR observables are compared to those reported by Xiang et al. for the unphosphorylated RS peptide.16 Experimental Methods. Small angle scattering data was gathered on the X33 beamline at the EMBL Outstation using the DORIS synchrotron source located in DESY, Hamburg.84 Samples at concentrations of 2 and 0.33 mg/mL or 0.67 mL in buffer at 25 °C were loaded into sample cell using X33 automated sample changer85 and exposed for four frames, 30 s each. The buffer was 50 mM Na-phosphate buffer, 100 mM NaCl, and pH 7.0, which was also used for all RS peptide NMR experiments. Data was recorded on a Pilatus 1 M photon counting detector. After comparing frames for radiation damage, each frame was radially averaged and then 1d-averaged using the AutoPilatus software. I(0) and Rg analysis was done manually to ensure quality in the presence of high noise, using the PRIMUS program, and verified by visual checking of used data ranges.75,^86 

# ■ RESULTS AND DISCUSSION 

 Chain Dimensions Depend Strongly on Force Field. Conformational ensembles of the RS peptide were obtained using eight different force fields (Table 1). As can be seen in Figure 1, peptide chain dimensions depend strongly on the 

 DOI: 10.1021/acs.jctc.5b00736 5515 

force field. This dependence is evident in both the radius of gyration, Rg (Figure 1 A), and mean separation distance between residue pairs (Figure 1B). The ensemble obtained with Amber ff99sb*-ildn is the most compact, resembling a collapsed globule-like ensemble. The most expanded ensemble is obtained with Amber ff03ws. The other six force fields generated a broad spectrum of chain dimensions that fall between these two extreme cases. For illustrating these differences, a selection of structures from each force field are shown in Figure S1. The small statistical uncertainties reported for each structural property and each force field in Figure 1 indicate that sufficient sampling of conformational space was obtained. This is further confirmed by analysis of the contact maps in the first and second halves of the simulations, which are remarkably similar (Figure S2), indicating that the conformational ensembles are well-sampled in all cases. The observed differences therefore must be attributed to inherent force field differences and not to inadequate conformational sampling. We also assessed the effect of the chosen water model. For three of the force fields, we have therefore kept the same force field for the peptide and used two different water models. In each of these cases, the difference in water model has a significant effect on chain compactness (Figure 1A and B). With CHARMM 22*, the TIP4P-D water model produces a more expanded ensemble than charmm-modified TIP3P. The relative expansion of the ensemble in TIP4P-D compared to charmm-modified TIP3P is consistent with results reported for other IDPs.26^ Amber ff03ws produces a more expanded ensemble than Amber ff03w; this is also to be expected given that the depth of the Lennard-Jones potential, ε, between protein atoms and water oxygen atoms is scaled by a factor of 

 1.1 in Amber ff03ws compared to ff03w.51 With CHARMM 36, charmm-modified TIP3P produces a significantly more expanded ensemble than TIP3P. Both of these water models were included in the development of CHARMM 36;58 here, they lead to significant differences in compactness. Because of the strong dependence of chain dimensions on the water model, no simple grouping of Amberand CHARMM-based force fields with respect to compactness is evident. The differences in chain dimensions correlate with marked differences in the balance between chain−chain and chain-water interactions (Figure 1 C and D). Conformations in the CHARMM 361 ensemble have, on average, the highest number of intrapeptide hydrogen bonds. Conformations in the Amber ff99sb*-ildn ensemble have, on average, the fewest hydrogen bonds to water molecules. Intrachain contacts in this ensemble are formed between residues close in sequence (turns) as well as long-range contacts (Figure 2A and Figure S3), consistent with the behavior of a collapsed globule. The ensembles obtained using the other force fields have intrapeptide hydrogen bonds that occur primarily in the form of local turns and helices with relatively few nonlocal contacts (Figure 2 A and Figure S3). Comparing the chain dimensions (Figure 1A and B) of ensembles obtained using different force fields to hydrogen bonding (Figure 1C and D), it can be seen that these structural properties are not perfectly correlated. Specifically, ensembles with significantly different structural properties may have the same mean dimensions. For instance, the chain dimensions CHARMM 22*/TIP4P-D ensemble are nearly the same as those of the ABSINTH ensemble (Figure 1 B), but the ensemble with ABSINTH has a significantly higher population of intrapeptide hydrogen bonds (Figures 1C and 2 A). The 

Figure 1. Chain dimensions and hydrogen bonding in different force fields. (A) Histograms of the radius of gyration, Rg, for the structural ensembles obtained in each force field (the legend applies to all figure panels). CHARMM 22*and CHARMM 22*/D refer to simulations with charmmmodified TIP3P and TIP4P-D, respectively. CHARMM 361 and CHARMM 362 refer to simulations with TIP3P and charmm-modified TIP3P, respectively. (B) Ensemble-averaged distance, <Rij>, between the α-carbon atoms of residue pairs, i and j, vs sequence separation, |i −j|. (C) Histograms of the number of intrapeptide hydrogen bonds. (D) Histograms of the number of peptide-water hydrogen bonds. Shading indicates statistical uncertainty. 

 DOI: 10.1021/acs.jctc.5b00736 5516 

ABSINTH implicit solvent ensemble is unique in another respect: the low Rg peak (centered at 9 Å, Figure 1A) is due to the presence of an arginine claw-type structure (a representative conformation is provided in Figure S4; low Rg (<9.6 Å) conformations were observed in every replica exchange run carried out with ABSINTH). This conformation is reminiscent of the arginine claw observed previously in implicit solvent simulations of a phosphorylated RS peptide in which the phosphoserine residues were pointing outward into the solvent.87,88 The claw-like conformation in the ABSINTH ensemble is actually an inverse arginine claw in which the arginine residues point outward and the serine residues point inward. Secondary Structure Content Depends Strongly on Force Field. Like chain dimensions and hydrogen bonding, secondary structure content also depends strongly on the force field for both the RS peptide (Figure 2 B) and the FGnucleoporin peptide (Figure S5). We compared the secondary structure content of ensembles obtained using different force 

 fields for the same peptide sequence. The RMS difference in secondary structure content between ensembles with the same sequence and different force fields was calculated to be 0.1. We also compared the ensembles of the RS peptide and FGnucleoporin peptide obtained using the same force field. The RMS difference in secondary structure content between ensembles obtained using the same force field and different sequences was calculated to be 0.06. Overall, we find that a change in force field has a stronger effect on secondary structure content than changing the entire peptide sequence. For the two peptides compared here, the change in sequence is quite large. The RS peptide is highly charged, whereas the FG peptide is composed entirely of polar and hydrophobic residues. This result demonstrates how dramatically sensitive IDPs are to force field selection. Their rugged energy landscapes with many iso-energetic minima separated by low barriers make IDPs highly sensitive test systems to assess force field accuracy. 

Figure 2. Secondary structure content in different force fields. (A) Hydrogen-bond contact maps for the ensemble in each force field. Shown are hydrogen bonds between the carbonyl oxygen and amide nitrogen of the polypeptide backbone, which are colored according to their population in the ensemble from black (not observed) to white (present in >20% of configurations). (B) The fraction of residues assigned a particular type of secondary structure according to the DSSP70 algorithm. (C) A representative structure from the CHARMM 36 ensemble containing an extended, left-handed α-helix. 

 DOI: 10.1021/acs.jctc.5b00736 5517 

Ensembles Obtained Using CHARMM 36 Have a Bias toward a Left-Handed α-Helix. As can be seen in Figure 2B, the ensembles in most force fields have substantial content of bends and turns and relatively low α-helix and β-sheet content. There are two notable exceptions: CHARMM 36 with TIP3P and charmm-modified TIP3P; both of these ensembles have an exceptionally high α-helix content. Unexpectedly, this helix does not have the usual handedness expected for proteins; it is left-handed (a representative structure is shown in Figure 2C). Left-handed α-helices are exceedingly rare in structured proteins. Only 31 left-handed α-helices were found in a survey of 7984 structures from the PDB, and only 10 contained no glycines.89 The maximum length of any of these was 6 residues; these helices are actually single helical turns, rather than extended helices. Longer left-handed α-helices, such as those seen in the ensembles with CHARMM 36, are essentially absent from structured proteins, based on known protein structures in the PDB. Figure 3 compares the Ramachandran maps of all eight force fields to that of nonproline, nonglycine coil residues in the Top50090 set of proteins (a nonredundant set of protein structures from the PDB). The population in the αL basin in the Top500 coil set is low (6%). Consistent with this population, most of the force fields also have low populations in αL, except for the CHARMM 36 ensembles, both of which have populations of more than 40%. No other force field has such a strong αL bias. In fact, more than 85% of the conformations in the CHARMM 36 ensemble contain a lefthanded α-helix. Ramachandran maps of ensembles obtained using the same force field for the peptide, but which differ in water model used, are very similar (Figure 3). This result provides further independent support that sufficient conformational sampling has been achieved. Structural Ensembles Obtained Using Different Force Fields Exhibit High Variability. Taken together, the results presented so far indicate the strong dependence of secondary 

 structure and compactness on the choice of force field. For example, the ensemble in Amber ff99sb*-ildn has nearly four times as many intrapeptide hydrogen bonds compared to the Amber ff03ws ensemble. The choice of water model also has a significant effect on compactness, consistent with other studies.26,51 The ensembles with CHARMM 36 are unique in their exceptionally high left-handed α-helix population. Although it is to be expected that the conformational ensemble of an IDP will depend, to some extent, on the chosen force field, the magnitude of the difference between force fields seen for the RS peptide is remarkable, spanning a range from globular to highly expanded. This finding is particularly surprising in light of the fact that many of these force fields have performed well in other benchmark studies.26,^35 ,^51 Therefore, we next asked how well these ensembles compare to a diverse set of experimental data. Assessing the Accuracy of Chain Dimensions: Comparison to Primary Experimental Data. For this aim, we measured SAXS data for the RS peptide, as described in the Experimental Methods. Figure 4a shows the measured SAXS scattering curve, along with the scattering curve calculated from the MD simulations using each force field. The curves of two ensembles, those obtained using CHARMM 22 *and Amber ff03w, agree within error with the experimental data. The mean Rg and RH of each ensemble are shown in Figure 4B and C, respectively. The mean Rg of the CHARMM 22 *ensemble (12.65 ±0.07 Å) is slightly smaller than that of the Amber ff03w ensemble (13.3 ±0.1 Å) and agrees best with the measured Rg (12.62 ±0.07 Å). These results are similar for both approaches to computing scattering curves from structures (results for both CRYSOL and FOXS are shown in Figure S8 and S9). Consistent with the results for radius of gyration, the CHARMM 22*ensemble is in closest agreement with the experimental hydrodynamic radius (11.95 ±0.01 Å compared to the experimentally measured value of 11.9 ±0.1 Å). 

Figure 3. Force field differences in backbone dihedral angles. The potential of mean force (PMF), −log(P(φ,ψ)), with color scale in kT, is shown for each force field. The upper right graph (PDB, coil) corresponds to all non-Pro, non-Gly residues that are not in helix or sheet secondary structure in the TOP50090 structures (a set of nonredundant protein structures from the PDB). The population in the αL basin in each case is Amber ff99sb*ildn = 0.12, Amber ff03w = 0.01, Amber ff03ws = 0.01, ABSINTH = 0.02, CHARMM 22*= 0.05, CHARMM 22*(with TIP4P-D) = 0.04, CHARMM 36 (with TIP3P) = 0.42, CHARMM 36 (with charmm-modified TIP3P) = 0.41, and PDB, coil = 0.06. More than 85% of conformations in the CHARMM 36 ensemble contain left-handed α-helix. Refer to Figures S6 and S7 for the same analysis for arginine and serine residues separately. 

 DOI: 10.1021/acs.jctc.5b00736 5518 

The collapsed globule ensemble of Amber ff99sb*-ildn and the predominantly left-handed α-helix ensemble of CHARMM 36 are both too compact and inconsistent with the SAXS and PFG-NMR data. These results suggest that chain-chain interactions are too favorable compared to chain-water interactions in these force fields, or, alternatively, that the hydrophobic effect is too strong. A combination of these effects is likely, but our results do not allow us to assess the relative contributions of these effects. In contrast, ABSINTH, Amber ff03ws, and CHARMM 22* with the TIP4P-D water model generate ensembles that are too expanded compared to the experimental Rg and RH, suggesting that the balance is shifted too far in favor of chain-water interactions in these force fields. The implicit solvent model, ABSINTH, has previously been found to agree with measurements of RH for other IDPs.45 Amber ff03ws and CHARMM 22 *with TIP4P-D were both developed with the specific aim of matching the experimental chain dimensions of IDPs.26,^51 The TIP4P-D water model has a Lennard-Jones C6 parameter 50% larger than that of other water models and thus has increased dispersion interactions.26 The fact that these force fields result in ensembles that are too expanded in comparison 

 to experimental data for the RS peptide suggests that the problem of obtaining an accurate force field for IDPs may not be solved simply by modified water models parametrized specifically for IDPs. Assessing the Accuracy of Secondary Structure Content: Comparison to 3JHNHα Couplings. The CHARMM 22*and Amber ff03w ensembles agree well with SAXS and PFG-NMR data. These two ensembles are similar in compactness (Figure 1 ), but they differ significantly in secondary structure content (Figure 2). To assess the accuracy of secondary structure content, we compare to measured scalar couplings, which report on ensemble-averaged backbone and side chain dihedral angles. Figure 5 shows 3JHNHα scalar 

 couplings, which report on the φbackbone dihedral angle and are the most-informative (and most-commonly used) for backbone conformation.91 As can be seen, two force fields agree well with the measured couplings, CHARMM 22*with charmm-modified TIP3P and TIP4P-D water models. The3JHNH αscalar couplings for both CHARMM 36 ensembles are outside of experimental error. Because these couplings report on the φdihedral angle, this finding also implies that the high left-handed α-helix population in CHARMM 36 is not consistent with the experimental data. For all three force fields 

Figure 4. Comparison to chain dimensions measured by SAXS and PFG-NMR. (A) Shown are ensemble-averaged scattering curves for each force field (with the same color scheme as Figure 1). The experimental curve is shown with error in gray. The ensembles in two force fields agree with the experimental scattering curve within error: Amber ff03w and CHARMM 22*. (B) The radius of gyration is shown for each force field and the experimental data (black). (C) The hydrodynamic radius is shown for each force field, and the experimentally measured value is shown in black. The shaded gray lines in (B) and (C) indicate the experimental error. Figure 5. Comparison to measured 3JHN‑Hαcouplings. (A) The 3JHN‑Hα couplings are shown for the ensemble obtained using each force field (the color scheme is consistent with Figures 1 and 4 , shading indicates statistical uncertainty, which is on the order of the line thickness, ∼0.01 Hz). The experimental 3JHN‑Hα couplings (with error) are shown in gray shading; arginine and serine residues in the RS repeats have one measured 3JHN‑Hαcoupling. A correction to the 3JHNHαscalar couplings has been suggested in the literature.92 Such a correction would shift the true values of the scalar couplings to higher values compared to the experimentally measured values.77 This additional uncertainty in the experimental values (estimated to be up to 5%17) is indicated in lighter gray. (B) The average unsigned error for the ensemble obtained using each force field is shown. 

 DOI: 10.1021/acs.jctc.5b00736 5519 

for which different water models are tested (CHARMM 22*, Amber ff03w, and CHARMM 36), changing the water model has a relatively small impact on the 3JHNHαscalar couplings. Obviously, the water model has a negligible effect on φ backbone dihedral preferences, which can also be seen in the Ramachandran plots in Figure 3. Next, we compared the RS peptide ensembles to a large set of scalar couplings and chemical shifts as summarized in Figure 6 (raw data for each observable is provided in Figures S10− 

S18). Two more scalar couplings (1JCαCβand 1JCαHα) report on the φbackbone dihedral angle. However, these scalar couplings are less informative than 3JHNHα. 1JCαCβcoupling constants have been found to depend more on amino acid composition than secondary structure preferences.79 Nevertheless, as seen with the 3JHNHαscalar couplings, the ensembles with CHARMM 22* are in closest agreement, and the CHARMM 36 ensembles do not agree well for both 1JCαCβand 1JCαHα. Comparison to side chain scalar couplings are also reported (Figures S12 and S13). The CHARMM 36 ensembles again show the largest errors, whereas the average unsigned errors for the other force fields are low (less than 0.4 Hz, the RMS prediction error). In general, the comparison to the experimental scalar couplings is limited primarily by the accuracy of computing scalar couplings with Karplus relations. The typical statistical uncertainty in the computed scalar couplings is only ∼0.01 Hz (smaller than the line thickness in Figure 5) because of the extensive conformational sampling, which is much smaller than the RMS prediction errors. Thus, the observed deviations do not necessarily imply force field artifacts. With respect to scalar couplings, CHARMM 36 ensembles deviate most from the experimental data, which is likely due to the high left-handed α-helix population. To investigate this further, we calculated the scalar couplings for a subensemble 

 that was generated by selecting all conformations in the CHARMM 36 ensemble that contained no left-handed α-helix (Figure S15). This subensemble has significantly lower error compared to the experimental backbone scalar couplings, providing further evidence that the left-handed α-helix is inconsistent with the experimental data. Comparison to Chemical Shifts. Carbonyl carbon and αcarbon chemical shifts have also been measured for the RS peptide.16 Both of these types of chemical shifts are very sensitive to secondary structure.93 The comparison to these chemical shifts is primarily limited by the expected accuracy of currently available chemical shift predictors. Within the expected error of SPARTA+, the chemical shifts of all of the ensembles agree with the experimental shifts. Chemical shifts calculated with SHIFTX2 have significantly smaller reported RMS errors than SPARTA+.82^ We report chemical shifts computed using both approaches as secondary chemical shifts (with the random coil values subtracted) in Figures S16−S18. Only the ensemble obtained with CHARMM 22* (and charmm-modified TIP3P) agrees well with all available experimental data, except for residual dipolar couplings (RDCs). Consistent with earlier reports,17,^94 ,95 we find that the ensembles in all force fields are in poor agreement with RDCs (see Figure S19). It has been suggested that the conformational ensembles of IDPs may be affected by the presence of alignment media used in measurements of RDCs.96 It is also well-established that IDPs are highly sensitive to solution conditions.97,98 Therefore, it is still unclear from the present set of evidence whether the disagreement with RDCs comes from an effect of the alignment media on the ensembles or due to the force field. We are therefore carrying out a more detailed investigation into these effects. This will be published in a further study, as it goes significantly beyond the scope of the present work. Generality and Causes of the Left-Handed Helix Propensity of CHARMM 36. We next investigated whether only the RS peptide forms a left-handed α-helix with CHARMM 36, or whether this force field has a general propensity for αL. To this end, simulations with (A)3, (AAQAA)3, and the HEWL peptide were performed. The Ramachandran plots for (A)3 and (AAQAA)3 (Figure S20) show a 6-fold lower αL propensity than seen for the RS peptide and are consistent with those reported by Best et al.58 We also carried out microsecond simulations of the HEWL peptide. Approximately 30% of the ensemble of this peptide contains left-handed α-helix (Figure S21). At least 200 ns of simulation were needed before the left-handed helix formed, which is longer than earlier simulations of this peptide.58 Thus, even though these proteins do not fold, long simulation times may be needed to find all highly populated conformational states. The 16-residue FG-nucleoporin peptide (Figure 7a), as well as the longer 50-residue FG-nucleoporin peptide (Figure S22a), also showed a high population in the αL basin for the CHARMM 36 force field. A conformation of the FGnucleoporin peptide containing helices of both handedness is shown (Figure S22b). Thus, the bias of CHARMM 36 toward left-handed α-helix is not limited to the RS peptide but rather seems to be quite general. This leads directly to the question: what causes the CHARMM 36 bias toward left-handed α-helix? Left-handed α-helix is sterically disfavored by the close proximity of the side chain Cβatom with the carbonyl C′atom of the previous residue.99 Comparing CHARMM 36 to its predecessor, CHARMM 22/CMAP, one of the modifications is 

Figure 6. Comparison to NMR and SAXS experimental data: Summary. Average unsigned error (AUE) compared to experimental data in (A) the hydrodynamic radius, Rh, and the radius of gyration, Rg, (in Å), (B) J-couplings (in Hz), and (C) chemical shifts (in ppm) for each force field. 

 DOI: 10.1021/acs.jctc.5b00736 5520 

a change in the Lennard-Jones parameters of aliphatic hydrogen and carbon atoms, including the side chain Cβatom.58,100 In particular, the Lennard-Jones σ parameter was decreased. Because it is precisely a steric clash between this atom and the carbonyl C′atom that precludes the αL conformation in nature, we tested the effect of using the aliphatic LJ parameters of the CHARMM 22/CMAP force field in CHARMM 36, which is here referred to as CHARMM 36, LJ mod. In Figure 7a, Ramachandran plots are shown for the FGnucleoporin peptide with CHARMM 36 as well as CHARMM 36, LJ mod. Indeed, the population in the αL basin is significantly reduced by this modification. Furthermore, the fraction of the ensemble containing left-handed α-helix is reduced from over 40% with CHARMM 36 to below 15% with CHARMM 36, LJ mod, which is even less left-handed α-helix than the CHARMM 22/CMAP ensemble (Figure 7b). It is therefore likely that a combination of a CMAP correction rendering the αL basin too favorable, combined with a decrease in the LJ σparameter of the side chain Cβatom, promotes αL formation. The CHARMM 36 subensemble containing no left handed α-helix has nearly the same radius of gyration as the entire ensemble (Figure S23). This result suggests that further modifications to the CHARMM 36 force field would be needed 

 beyond adjusting the aliphatic LJ parameters; we did not pursue this direction further. 

# ■ CONCLUSIONS 

 Obtaining accurate descriptions of IDPs by means of MD simulations is quite challenging both due to their sensitivity to force field inaccuracies as well as the need for extensive sampling. In addition, it is more demanding to obtain experimental information characterizing the entire ensemble of an IDP than the average structure of a folded protein because more experimental information is needed in the case of IDPs due to their high conformational heterogeneity. Furthermore, most experimental measurements obtained for IDPs are ensemble-averages, which only increases the challenge faced in characterizing IDPs. Here, we assessed the accuracy of ensembles obtained from de novo simulations without the use of experimental information to guide ensemble selection or generation. Experimental data from SAXS and NMR were then used to evaluate the accuracy of the ensembles obtained using eight state-of-the-art force fields. Note that this study is not a comprehensive test of all available force field combinations. Sufficient conformational sampling was obtained using replica exchange. Taken together, our results demonstrate an unexpectedly high sensitivity of IDP conformational ensembles to differences between the force fields. For example, for CHARMM 36, an unexpectedly high propensity for left-handed α-helix was found, which was strongly reduced by relatively small changes in the Lennard-Jones parameters of aliphatic carbons. A comparison of the secondary structure content of the RS and FG peptides showed that, for these two very different IDPs, force field is a stronger determinant of secondary structure content than peptide sequence. Major differences in chain dimensions were also found: ensembles span the entire range from collapsed globule-like to highly expanded. There was consensus, though, among all of the force fields that the studied peptides are disordered (that is, populating many conformations rather than a single, welldefined native structure). Even this similarity is tenuous because the vast majority of the CHARMM 36 ensemble contains stretches of left-handed α-helix. A key finding of this study is that the conformational ensemble obtained using CHARMM 22 * with charmmmodified TIP3P agrees best with all available experimental data. Maintaining the correct balance between solvent−solvent, solvent−solute, and solute−solute interactions has been an optimization criterion in the development of the CHARMM force fields, even in much earlier versions.31,101 With a correct balance of interactions, the quality of water as a solvent for proteins should be well described, and this indeed appears to be the case for the RS peptide. This study provides a systematic benchmark of eight force fields for a set of IDPs. Further computational-experimental studies of other IDPs are a necessary next step to delineate the accuracy of force fields for simulations of IDPs of different length and sequence composition. 

# ■ ASSOCIATED CONTENT 

### *S^ Supporting Information 

 The Supporting Information is available free of charge on the ACS Publications website at DOI: 10.1021/acs.jctc.5b00736. 

Figure 7. Modified aliphatic LJ parameters significantly reduce αL-helix in CHARMM 36. (A) The potential of mean force (PMF), −log(P(φ,ψ)), with color scale in kT, is shown for the FG-nucleoporin peptide in each force field. The population in the αL basin in each case is CHARMM 361 = 0.26; CHARMM 362 = 0.23; CHARMM 22*= 0.09; and CHARMM 36, LJ mod = 0.13. (B) The fraction of the ensemble containing left-handed α-helix is shown for each force field. 

 DOI: 10.1021/acs.jctc.5b00736 5521 

 Force field ensembles, contact maps, example inverse claw conformation, secondary structure content for different sequences and force fields, force field differences in backbone dihedral angles, comparison to SAXS, scalar couplings, chemical shifts and RDCs, Ramachandran plots, list of simulations, Monte Carlo move set, and Karplus relations used to calculate the scalar couplings (PDF) 

# ■ AUTHOR INFORMATION 

Corresponding Author *E-mail: sarah.rauscher@mpibpc.mpg.de. 

Notes The authors declare no competing financial interest. 

# ■ ACKNOWLEDGMENTS 

The authors gratefully acknowledge Robert Best for providing the GROMACS ports for Amber ff03w and Amber ff03ws and Alexander MacKerell and Michael Feig for discussions on CHARMM 36 development. S.R. is supported by a postdoctoral fellowship from the Alexander von Humboldt Foundation. M.Z. was supported by the DFG Collaborative Research Center 860, Project B2. Compute time was provided through an allocation by the Gauss Supercomputing Center on the SuperMUC supercomputer at the Leibniz Rechenzentrum in Garching. 

# ■ REFERENCES 

(1) van der Lee, R.; Buljan, M.; Lang, B.; Weatheritt, R. J.; Daughdrill, G. W.; Dunker, A. K.; Fuxreiter, M.; Gough, J.; Gsponer, J.; Jones, D. T.; et al. Classification of Intrinsically Disordered Regions and Proteins. Chem. Rev. 2014 , 114 , 6589−6631. (2) Tompa, P.; Davey, N. E.; Gibson, T. J.; Babu, M. M. A Million Peptide Motifs for the Molecular Biologist. Mol. Cell 2014 , 55 , 161− 169. (3) Lim, R. Y. H.; Fahrenkrog, B.; Köser, J.; Schwarz-Herion, K.; Deng, J.; Aebi, U. Nanomechanical Basis of Selective Gating by the Nuclear Pore Complex. Science 2007 , 318 , 640−643. (4) Nott, T. J.; Petsalaki, E.; Farber, P.; Jervis, D.; Fussner, E.; Plochowietz, A.; Craggs, T. D.; Bazett-Jones, D. P.; Pawson, T.; Forman-Kay, J. D.; et al. Phase Transition of a Disordered Nuage Protein Generates Environmentally Responsive Membraneless Organelles. Mol. Cell 2015 , 57 , 936−947. (5) Weber, S. C.; Brangwynne, C. P. Getting RNA and Protein in Phase. Cell 2012 , 149 , 1188−1191. (6) Jensen, M. R.; Zweckstetter, M.; Huang, J. R.; Blackledge, M. Exploring Free-Energy Landscapes of Intrinsically Disordered Proteins at Atomic Resolution Using NMR Spectroscopy. Chem. Rev. 2014 , 114 , 6632−6660. (7) Rauscher, S.; Pomès, R. Molecular Simulations of Protein Disorder. Biochem. Cell Biol. 2010 , 88 , 269−290. (8) Varadi, M.; Kosol, S.; Lebrun, P.; Valentini, E.; Blackledge, M.; Dunker, A. K.; Felli, I. C.; Forman-Kay, J. D.; Kriwacki, R. W.; Pierattelli, R.; et al. pE-DB: a Database of Structural Ensembles of Intrinsically Disordered and of Unfolded Proteins. Nucleic Acids Res. 2014 , 42 , D326−D335. (9) Brucale, M.; Schuler, B.; Samorì, B. Single-Molecule Studies of Intrinsically Disordered Proteins. Chem. Rev. 2014 , 114 , 3281−3317. (10) Wilkins, D. K.; Grimshaw, S. B.; Receveur, V.; Dobson, C. M.; Jones, J. A.; Smith, L. J. Hydrodynamic Radii of Native and Denatured Proteins Measured by Pulse Field Gradient NMR Techniques. Biochemistry 1999 , 38 , 16424−16431. (11) Camilloni, C.; Vendruscolo, M. Statistical Mechanics of the Denatured State of a Protein Using Replica-Averaged Metadynamics. J. Am. Chem. Soc. 2014 , 136 , 8982−8991. 

 (12) Dedmon, M. M.; Lindorff-Larsen, K.; Christodoulou, J.; Vendruscolo, M.; Dobson, C. M. Mapping Long-Range Interactions in A-Synuclein Using Spin-Label NMR and Ensemble Molecular Dynamics Simulations. J. Am. Chem. Soc. 2005 , 127 , 476−477. (13) Allison, J. R.; Varnai, P.; Dobson, C. M.; Vendruscolo, M. Determination of the Free Energy Landscape of α-Synuclein Using Spin Label Nuclear Magnetic Resonance Measurements. J. Am. Chem. Soc. 2009 , 131 , 18314−18326. (14) Krzeminski, M.; Marsh, J. A.; Neale, C.; Choy, W. Y.; FormanKay, J. D. Characterization of Disordered Proteins with ENSEMBLE. Bioinformatics 2013 , 29 , 398−399. (15) Salmon, L.; Nodet, G.; Ozenne, V.; Yin, G.; Jensen, M. R.; Zweckstetter, M.; Blackledge, M. NMR Characterization of LongRange Order in Intrinsically Disordered Proteins. J. Am. Chem. Soc. 2010 , 132 , 8407−8418. (16) Xiang, S.; Gapsys, V.; Kim, H. Y.; Bessonov, S.; Hsiao, H. H.; Möhlmann, S.; Klaukien, V.; Ficner, R.; Becker, S.; Urlaub, H.; et al. Phosphorylation Drives a Dynamic Switch in Serine/Arginine-Rich Proteins. Structure 2013 , 21 , 2162−2174. (17) Ball, K. A.; Wemmer, D. E.; Head-Gordon, T. Comparison of Structure Determination Methods for Intrinsically Disordered Amyloid-βPeptides. J. Phys. Chem. B 2014 , 118 , 6405−6416. (18) Gurry, T.; Ullman, O.; Fisher, C. K.; Perovic, I.; Pochapsky, T.; Stultz, C. M. The Dynamic Structure of α-Synuclein Multimers. J. Am. Chem. Soc. 2013 , 135 , 3865−3872. (19) Schwalbe, M.; Ozenne, V.; Bibow, S.; Jaremko, M.; Jaremko, L.; Gajda, M.; Jensen, M. R.; Biernat, J.; Becker, S.; Mandelkow, E.; et al. Predictive Atomic Resolution Descriptions of Intrinsically Disordered hTau40 and α-Synuclein in Solution From NMR and Small Angle Scattering. Structure 2014 , 22 , 238−249. (20) Lange, O. F.; Lakomek, N.-A.; Farès, C.; Schröder, G. F.; Walter, K. F. A.; Becker, S.; Meiler, J.; Grubmülller, H.; Griesinger, C.; de Groot, B. L. Recognition Dynamics Up to Microseconds Revealed From an RDC-Derived Ubiquitin Ensemble in Solution. Science 2008 , 320 , 1471−1475. (21) Vitalis, A.; Pappu, R. V. ABSINTH: a New Continuum Solvation Model for Simulations of Polypeptides in Aqueous Solutions. J. Comput. Chem. 2009 , 30 , 673−699. (22) Smith, W. W.; Schreck, C. F.; Hashem, N.; Soltani, S.; Nath, A.; Rhoades, E.; O’Hern, C. S. Molecular Simulations of the Fluctuating Conformational Dynamics of Intrinsically Disordered Proteins. Phys. Rev. E 2012 , 86 , 041910. (23) Yedvabny, E.; Nerenberg, P. S.; So, C.; Head-Gordon, T. Disordered Structural Ensembles of Vasopressin and Oxytocin and Their Mutants. J. Phys. Chem. B 2015 , 119 , 896−905. (24) Stanley, N.; Esteban-Martin, S.; De Fabritiis, G. Kinetic Modulation of a Disordered Protein Domain by Phosphorylation. Nat. Commun. 2014 , 5 , 5272. (25) Gerben, S. R.; Lemkul, J. A.; Brown, A. M.; Bevan, D. R. Comparing Atomistic Molecular Mechanics Force Fields for a Difficult Target: a Case Study on the Alzheimer’s Amyloid β-Peptide. J. Biomol. Struct. Dyn. 2014 , 32 , 1817−1832. (26) Piana, S.; Donchev, A. G.; Robustelli, P.; Shaw, D. E. Water Dispersion Interactions Strongly Influence Simulated Structural Properties of Disordered Protein States. J. Phys. Chem. B 2015 , 119 , 5113 −5123. (27) Ye, W.; Ji, D.; Wang, W.; Luo, R.; Chen, H.-F. Test and Evaluation of ff99IDPs Force Field for Intrinsically Disordered Proteins. J. Chem. Inf. Model. 2015 , 55 , 1021−1029. (28) Sgourakis, N. G.; Merced-Serrano, M.; Boutsidis, C.; Drineas, P.; Du, Z.; Wang, C.; García, A. E. Atomic-Level Characterization of the Ensemble of the Aβ(1−42) Monomer in Water Using Unbiased Molecular Dynamics Simulations and Spectral Algorithms. J. Mol. Biol. 2011 , 405 , 570−583. (29) Fawzi, N. L.; Phillips, A. H.; Ruscio, J. Z.; Doucleff, M.; Wemmer, D. E.; Head-Gordon, T. Structure and Dynamics of the Aβ 21 − 30 Peptide From the Interplay of NMR Experiments and Molecular Simulations. J. Am. Chem. Soc. 2008 , 130 , 6145−6158. 

 DOI: 10.1021/acs.jctc.5b00736 5522 

(30) McCammon, J. A.; Gelin, B. R.; Karplus, M. Dynamics of Folded Proteins. Nature 1977 , 267 , 585−590. (31) MacKerell, A. D.; Bashford, D.; Bellott, M.; Dunbrack, R. L.; Evanseck, J. D.; Field, M. J.; Fischer, S.; Gao, J.; Guo, H.; Ha, S.; et al. All-Atom Empirical Potential for Molecular Modeling and Dynamics Studies of Proteins. J. Phys. Chem. B 1998 , 102 , 3586−3616. (32) Best, R. B.; Hummer, G. Optimized Molecular Dynamics Force Fields Applied to the Helix−Coil Transition of Polypeptides. J. Phys. Chem. B 2009 , 113 , 9004−9015. (33) Piana, S.; Lindorff-Larsen, K.; Shaw, D. E. How Robust Are Protein Folding Simulations with Respect to Force Field Parameterization? Biophys. J. 2011 , 100 , L47−L49. (34) Best, R. B.; Mittal, J. Protein Simulations with an Optimized Water Model: Cooperative Helix Formation and TemperatureInduced Unfolded State Collapse. J. Phys. Chem. B 2010 , 114 , 14916 −14923. (35) Lindorff-Larsen, K.; Maragakis, P.; Piana, S.; Eastwood, M. P.; Dror, R. O.; Shaw, D. E. Systematic Validation of Protein Force Fields Against Experimental Data. PLoS One 2012 , 7 , e32131. (36) Beauchamp, K. A.; Lin, Y. S.; Das, R.; Pande, V. S. Are Protein Force Fields Getting Better? A Systematic Benchmark on 524 Diverse NMR Measurements. J. Chem. Theory Comput. 2012 , 8 , 1409−1414. (37) Lange, O. F.; van der Spoel, D.; de Groot, B. L. Scrutinizing Molecular Mechanics Force Fields on the Submicrosecond Timescale with NMR Data. Biophys. J. 2010 , 99 , 647−655. (38) Cino, E. A.; Choy, W. Y.; Karttunen, M. Comparison of Secondary Structure Formation Using 10 Different Force Fields in Microsecond Molecular Dynamics Simulations. J. Chem. Theory Comput. 2012 , 8 , 2725−2740. (39) Petrov, D.; Zagrovic, B. Are Current Atomistic Force Fields Accurate Enough to Study Proteins in Crowded Environments? PLoS Comput. Biol. 2014 , 10 , e1003638. (40) Sethi, A.; Tian, J.; Vu, D. M.; Gnanakaran, S. Identification of Minimally Interacting Modules in an Intrinsically Disordered Protein. Biophys. J. 2012 , 103 , 748−757. (41) Levine, Z. A.; Larini, L.; LaPointe, N. E.; Feinstein, S. C.; Shea, J. E. Regulation and Aggregation of Intrinsically Disordered Peptides. Proc. Natl. Acad. Sci. U. S. A. 2015 , 112 , 2758−2763. (42) Pantelopulos, G. A.; Mukherjee, S.; Voelz, V. A. Microsecond Simulations of Mdm2 and Its Complex with p53 Yield Insight Into Force Field Accuracy and Conformational Dynamics. Proteins: Struct., Funct., Genet. 2015 , 83 , 1665−1676. (43) Hoffmann, K. Q.; McGovern, M.; Chiu, C.-C.; de Pablo, J. J. Secondary Structure of Rat and Human Amylin Across Force Fields. PLoS One 2015 , 10 , e0134091. (44) Rosenman, D. J.; Connors, C. R.; Chen, W.; Wang, C.; García, A. E. AβMonomers Transiently Sample Oligomer and Fibril-Like Configurations: Ensemble Characterization Using a Combined MD/ NMR Approach. J. Mol. Biol. 2013 , 425 , 3338−3359. (45) Mao, A. H.; Crick, S. L.; Vitalis, A.; Chicoine, C. L.; Pappu, R. V. Net Charge Per Residue Modulates Conformational Ensembles of Intrinsically Disordered Proteins. Proc. Natl. Acad. Sci. U. S. A. 2010 , 107 , 8183−8188. (46) Fluitt, A. M.; de Pablo, J. J. An Analysis of Biomolecular Force Fields for Simulations of Polyglutamine in Solution. Biophys. J. 2015 , 109 , 1009−1018. (47) Best, R. B.; Mittal, J. Free-Energy Landscape of the GB1 Hairpin in All-Atom Explicit Solvent Simulations with Different Force Fields: Similarities and Differences. Proteins: Struct., Funct., Genet. 2011 , 79 , 1318 −1328. (48) Piana, S.; Klepeis, J. L.; Shaw, D. E. Assessing the Accuracy of Physical Models Used in Protein-Folding Simulations: Quantitative Evidence From Long Molecular Dynamics Simulations. Curr. Opin. Struct. Biol. 2014 , 24 , 98 −105. (49) Skinner, J. J.; Yu, W.; Gichana, E. K.; Baxa, M. C.; Hinshaw, J. R.; Freed, K. F.; Sosnick, T. R. Benchmarking All-Atom Simulations Using Hydrogen Exchange. Proc. Natl. Acad. Sci. U. S. A. 2014 , 111 , 15975 −15980. 

 (50) Lindorff-Larsen, K.; Trbovic, N.; Maragakis, P.; Piana, S.; Shaw, D. E. Structure and Dynamics of an Unfolded Protein Examined by Molecular Dynamics Simulation. J. Am. Chem. Soc. 2012 , 134 , 3787− 3791. (51) Best, R. B.; Zheng, W.; Mittal, J. Balanced Protein−Water Interactions Improve Properties of Disordered Proteins and NonSpecific Protein Association. J. Chem. Theory Comput. 2014 , 10 , 5113− 5124. (52) Mercadante, D.; Milles, S.; Fuertes, G.; Svergun, D. I.; Lemke, E. A.; Gräter, F. Kirkwood−Buff Approach Rescues Overcollapse of a Disordered Protein in Canonical Protein Force Fields. J. Phys. Chem. B 2015 , 119 , 7975−7984. (53) Henriques, J.; Cragnell, C.; Skepö, M. Molecular Dynamics Simulations of Intrinsically Disordered Proteins: Force Field Evaluation and Comparison with Experiment. J. Chem. Theory Comput. 2015 , 11 , 3420−3431. (54) Sugita, Y.; Okamoto, Y. Replica-Exchange Molecular Dynamics Method for Protein Folding. Chem. Phys. Lett. 1999 , 314 , 141−151. (55) Jorgensen, W. L.; Chandrasekhar, J.; Madura, J. D.; Impey, R. W.; Klein, M. L. Comparison of Simple Potential Functions for Simulating Liquid Water. J. Chem. Phys. 1983 , 79 , 926−935. (56) Abascal, J. L. F.; Vega, C. A General Purpose Model for the Condensed Phases of Water: TIP4P/2005. J. Chem. Phys. 2005 , 123 , 234505. (57) Kaminski, G. A.; Friesner, R. A.; Tirado-Rives, J.; Jorgensen, W. L. Evaluation and Reparametrization of the OPLS-AA Force Field for Proteins via Comparison with Accurate Quantum Chemical Calculations on Peptides. J. Phys. Chem. B 2001 , 105 , 6474−6487. (58) Best, R. B.; Zhu, X.; Shim, J.; Lopes, P. E. M.; Mittal, J.; Feig, M.; MacKerell, A. D. Optimization of the Additive CHARMM AllAtom Protein Force Field Targeting Improved Sampling of the Backbone φ, ψand Side-Chain χ1and χ2 Dihedral Angles. J. Chem. Theory Comput. 2012 , 8 , 3257−3273. (59) Nehrbass, U.; Kern, H.; Mutvei, A.; Horstmann, H.; Marshallsay, B.; Hurt, E. C. NSP1: a Yeast Nuclear Envelope Protein Localized at the Nuclear Pores Exerts Its Essential Function by Its Carboxy-Terminal Domain. Cell 1990 , 61 , 979−989. (60) Patel, S. S.; Belmont, B. J.; Sante, J. M.; Rexach, M. F. Natively Unfolded Nucleoporins Gate Protein Diffusion Across the Nuclear Pore Complex. Cell 2007 , 129 , 83 −96. (61) Pronk, S.; Páll, S.; Schulz, R.; Larsson, P.; Bjelkmar, P.; Apostolov, R.; Shirts, M. R.; Smith, J. C.; Kasson, P. M.; van der Spoel, D.; et al. GROMACS 4.5: a High-Throughput and Highly Parallel Open Source Molecular Simulation Toolkit. Bioinformatics 2013 , 29 , 845 −854. (62) Hess, B.; Kutzner, C.; van der Spoel, D.; Lindahl, E. GROMACS 4: Algorithms for Highly Efficient, Load-Balanced, and Scalable Molecular Simulation. J. Chem. Theory Comput. 2008 , 4 , 435−447. (63) Essmann, U.; Perera, L.; Berkowitz, M. L.; Darden, T.; Lee, H.; Pedersen, L. G. A Smooth Particle Mesh Ewald Method. J. Chem. Phys. 1995 , 103 , 8577−8593. (64) Bussi, G.; Donadio, D.; Parrinello, M. Canonical Sampling Through Velocity Rescaling. J. Chem. Phys. 2007 , 126 , 014101. (65) Berendsen, H. J. C.; Postma, J. P. M.; van Gunsteren, W. F.; DiNola, A.; Haak, J. R. Molecular Dynamics with Coupling to an External Bath. J. Chem. Phys. 1984 , 81 , 3684−3690. (66) Parrinello, M.; Rahman, A. Polymorphic Transitions in Single Crystals: a New Molecular Dynamics Method. J. Appl. Phys. 1981 , 52 , 7182 −7190. (67) Das, R. K.; Pappu, R. V. Conformations of Intrinsically Disordered Proteins Are Influenced by Linear Sequence Distributions of Oppositely Charged Residues. Proc. Natl. Acad. Sci. U. S. A. 2013 , 110 , 13392−13397. (68) Mao, A. H.; Pappu, R. V. Crystal Lattice Properties Fully Determine Short-Range Interaction Parameters for Alkali and Halide Ions. J. Chem. Phys. 2012 , 137 , 064104. (69) Humphrey, W.; Dalke, A.; Schulten, K. VMD: Visual Molecular Dyanmics. J. Mol. Graphics 1996 , 14 , 33 −38. 

 DOI: 10.1021/acs.jctc.5b00736 5523 

(70) Kabsch, W.; Sander, C. Dictionary of Protein Secondary Structure: Pattern Recognition of Hydrogen-Bonded and Geometrical Features. Biopolymers 1983 , 22 , 2577−2637. (71) Flyvbjerg, H.; Petersen, H. G. Error Estimates on Averages of Correlated Data. J. Chem. Phys. 1989 , 91 , 461−466. (72) Svergun, D.; Barberato, C.; Koch, M. H. J. CRYSOL a Program to Evaluate X-Ray Solution Scattering of Biological Macromolecules From Atomic Coordinates. J. Appl. Crystallogr. 1995 , 28 , 768−773. (73) Schneidman-Duhovny, D.; Hammel, M.; Tainer, J. A.; Sali, A. Accurate SAXS Profile Computation and Its Assessment by Contrast Variation Experiments. Biophys. J. 2013 , 105 , 962−974. (74) Chen, P.-C.; Hub, J. S. Validating Solution Ensembles From Molecular Dynamics Simulation by Wide-Angle X-Ray Scattering Data. Biophys. J. 2014 , 107 , 435−447. (75) Konarev, P. V.; Volkov, V. V.; Sokolova, A. V.; Koch, M. H. J.; Svergun, D. I. Primus: A Windows PC-Based System for Small-Angle Scattering Data Analysis. J. Appl. Crystallogr. 2003 , 36 , 1277−1282. (76) Ortega, A.; Amorós, D.; García de la Torre, J. Prediction of Hydrodynamic and Other Solution Properties of Rigid Proteins From Atomicand Residue-Level Models. Biophys. J. 2011 , 101 , 892−898. (77) Vuister, G. W.; Bax, A. Quantitative J Correlation: a New Approach for Measuring Homonuclear Three-Bond J(HNHα) Coupling Constants in 15N-Enriched Proteins. J. Am. Chem. Soc. 1993 , 115 , 7772−7777. (78) Cornilescu, G.; Bax, A.; Case, D. A. Large Variations in OneBond 13Cα−13CβJ Couplings in Polypeptides Correlate with Backbone Conformation. J. Am. Chem. Soc. 2000 , 122 , 2168−2171. (79) Schmidt, J. M.; Howard, M. J.; Maestre-Martínez, M.; Perez, C.́ S.; Löhr, F. Variation in Protein Cα-Related One-Bond J couplings. Magn. Reson. Chem. 2009 , 47 , 16 −30. (80) Schmidt, J. M. Asymmetric Karplus Curves for the Protein SideChain 3J Couplings. J. Biomol. NMR 2007 , 37 , 287−301. (81) Vuister, G. W.; Delaglio, F.; Bax, A. The Use of 1JCαHαCoupling Constants as a Probe for Protein Backbone Conformation. J. Biomol. NMR 1993 , 3 , 67 −80. (82) Han, B.; Liu, Y.; Ginzinger, S. W.; Wishart, D. S. SHIFTX2: Significantly Improved Protein Chemical Shift Prediction. J. Biomol. NMR 2011 , 50 , 43 −57. (83) Shen, Y.; Bax, A. SPARTA+: a Modest Improvement in Empirical NMR Chemical Shift Prediction by Means of an Artificial Neural Network. J. Biomol. NMR 2010 , 48 , 13 −22. (84) Roessle, M. W.; Klaering, R.; Ristau, U.; Robrahn, B.; Jahn, D.; Gehrmann, T.; Konarev, P.; Round, A.; Fiedler, S.; Hermes, C.; et al. Upgrade of the Small-Angle X-Ray Scattering Beamline X33 at the European Molecular Biology Laboratory, Hamburg. J. Appl. Crystallogr. 2007 , 40 , s190−s194. (85) Round, A. R.; Franke, D.; Moritz, S.; Huchler, R.; Fritsche, M.; Malthan, D.; Klaering, R.; Svergun, D. I.; Roessle, M. Automated Sample-Changing Robot for Solution Scattering Experiments at the EMBL Hamburg SAXS Station X33. J. Appl. Crystallogr. 2008 , 41 , 913 −917. (86) Petoukhov, M. V.; Franke, D.; Shkumatov, A. V.; Tria, G.; Kikhney, A. G.; Gajda, M.; Gorba, C.; Mertens, H. D. T.; Konarev, P. V.; Svergun, D. I. New Developments in the ATSAS Program Package for Small-Angle Scattering Data Analysis. J. Appl. Crystallogr. 2012 , 45 , 342 −350. (87) Hamelberg, D.; Shen, T.; McCammon, J. A. A Proposed Signaling Motif for Nuclear Import in mRNA Processing via the Formation of Arginine Claw. Proc. Natl. Acad. Sci. U. S. A. 2007 , 104 , 14947 −14951. (88) Sellis, D.; Drosou, V.; Vlachakis, D.; Voukkalis, N.; Giannakouros, T.; Vlassi, M. Phosphorylation of the Arginine/Serine Repeats of Lamin B Receptor by SRPK1Insights From Molecular Dynamics Simulations. Biochim. Biophys. Acta, Gen. Subj. 2012 , 1820 , 44 −55. (89) Novotny, M.; Kleywegt, G. J. A Survey of Left-Handed Helices in Protein Structures. J. Mol. Biol. 2005 , 347 , 231−241. (90) Lovell, S. C.; Davis, I. W.; Arendall, W. B.; de Bakker, P. I. W.; Word, J. M.; Prisant, M. G.; Richardson, J. S.; Richardson, D. C. 

 Structure Validation by CαGeometry: φ, ψ and CβDeviation. Proteins: Struct., Funct., Genet. 2003 , 50 , 437−450. (91) Otten, R.; Wood, K.; Mulder, F. A. A. Comprehensive Determination of 3JHNHα for Unfolded Proteins Using 13C′Resolved Spin-Echo Difference Spectroscopy. J. Biomol. NMR 2009 , 45 , 343−349. (92) Ball, K. A.; Phillips, A. H.; Wemmer, D. E.; Head-Gordon, T. Differences in β-Strand Populations of Monomeric Aβ40 and Aβ42. Biophys. J. 2013 , 104 , 2714−2724. (93) Wang, Y.; Jardetzky, O. Probability-Based Protein Secondary Structure Identification Using Combined NMR Chemical-Shift Data. Protein Sci. 2002 , 11 , 852−861. (94) Wang, Y.; Chu, X.; Longhi, S.; Roche, P.; Han, W.; Wang, E.; Wang, J. Multiscaled Exploration of Coupled Folding and Binding of an Intrinsically Disordered Molecular Recognition Element in Measles Virus Nucleoprotein. Proc. Natl. Acad. Sci. U. S. A. 2013 , 110 , E3743− E3752. (95) Wang, Y.; Longhi, S.; Roche, P.; Wang, J. Reply to Jensen and Blackledge: Dual Quantifications of Intrinsically Disordered Proteins by NMR Ensembles and Molecular Dynamics Simulations. Proc. Natl. Acad. Sci. U. S. A. 2014 , 111 , E1559−E1559. (96) Montalvao, R. W.; De Simone, A.; Vendruscolo, M. Determination of Structural Fluctuations of Proteins From Structure-Based Calculations of Residual Dipolar Couplings. J. Biomol. NMR 2012 , 53 , 281−292. (97) Wuttke, R.; Hofmann, H.; Nettels, D.; Borgia, M. B.; Mittal, J.; Best, R. B.; Schuler, B. Temperature-Dependent Solvation Modulates the Dimensions of Disordered Proteins. Proc. Natl. Acad. Sci. U. S. A. 2014 , 111 , 5213−5218. (98) Soranno, A.; Koenig, I.; Borgia, M. B.; Hofmann, H.; Zosel, F.; Nettels, D.; Schuler, B. Single-Molecule Spectroscopy Reveals Polymer Effects of Disordered Proteins in Crowded Environments. Proc. Natl. Acad. Sci. U. S. A. 2014 , 111 , 4874−4879. (99) Finkelstein, A. V.; Ptitsyn, O. Protein Physics: A Course of Lectures, 1st ed.; Academic Press, 2002. (100) Vorobyov, I. V.; Anisimov, V. M.; MacKerell, A. D. Polarizable Empirical Force Field for Alkanes Based on the Classical Drude Oscillator Model. J. Phys. Chem. B 2005 , 109 , 18988−18999. (101) Mackerell, A. D., Jr.; Wiórkiewicz-Kuczera, J.; Karplus, M. An All-Atom Empirical Energy Function for the Simulation of Nucleic Acids. J. Am. Chem. Soc. 1995 , 117 , 11946−11975. 

 DOI: 10.1021/acs.jctc.5b00736 5524 



---

# Uncertainty in integrative structural modeling

**Authors:** Dina Schneidman-Duhovny, Riccardo Pellarin, Andrej Sali
**Year:** 2014
**Venue:** Current Opinion in Structural Biology
**DOI:** 10.1016/j.sbi.2014.08.001
**Source PDF URL:** https://escholarship.org/content/qt51k92574/qt51k92574.pdf?t=rsy5ld
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

## UCSF 

### UC San Francisco Previously Published Works 

#### Title 

##### Uncertainty in integrative structural modeling 

#### Permalink 

##### https://escholarship.org/uc/item/51k92574 

#### Journal 

##### Current Opinion in Structural Biology, 28(1) 

#### ISSN 

##### 0959-440X 

#### Authors 

##### Schneidman-Duhovny, Dina 

##### Pellarin, Riccardo 

##### Sali, Andrej 

#### Publication Date 

##### 2014-10-01 

#### DOI 

##### 10.1016/j.sbi.2014.08.001 

##### Peer reviewed 

##### eScholarship.org Powered by the California Digital Library 

##### University of California 

## Uncertainty in Integrative Structural Modeling 

 Dina Schneidman-Duhovnya,*, Riccardo Pellarina, and Andrej Salia,b,* aDepartment of Bioengineering and Therapeutic Sciences, University of California, San Francisco, San Francisco, CA 94158, USA bDepartment of Pharmaceutical Chemistry, and California Institute for Quantitative Biosciences (QB3), University of California, San Francisco, San Francisco, CA 94158, USA 

#### Abstract 

 Integrative structural modelling uses multiple types of input information and proceeds in four stages: (i) gathering information, (ii) designing model representation and converting information into a scoring function, (iii) sampling good-scoring models, and (iv) analyzing models and information. In the first stage, uncertainty originates from data that are sparse, noisy, ambiguous, or derived from heterogeneous samples. In the second stage, uncertainty can originate from a representation that is too coarse for the available information or a scoring function that does not accurately capture the information. In the third stage, the major source of uncertainty is insufficient sampling. In the fourth stage, clustering, cross-validation, and other methods are used to estimate the precision and accuracy of the models and information. 

 Keywords macromolecular assemblies; integrative modeling; protein structure; accuracy; precision; uncertainty 

#### Introduction 

 To understand and modulate biological processes, we need their spatiotemporal models. These models can be computed based on input information about the structure and dynamics of the system of interest, including physical theories, statistical inference from databases of known sequences and structures, as well as a large variety of experimental methods. A structural model of a molecule is defined by the relative positions and orientations of its components (eg, atoms, pseudo-atoms, residues, secondary structure elements, domains, and subunits). All structural characterization approaches correspond to finding models that best fit input information, as can be judged by a scoring function; when the scoring function 

 © 2014 Elsevier Ltd. All rights reserved. *Corresponding authors: 1700 4th Street, Byers Hall 503B, University of California, San Francisco, San Francisco, CA 94158; tel 415-514-4227; web http://salilab.org; dina@salilab.org and sali@salilab.org. Publisher's Disclaimer: This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain. 

# NIH Public Access 

## Author Manuscript 

##### Curr Opin Struct Biol. Author manuscript; available in PMC 2015 October 01. 

 Published in final edited form as: Curr Opin Struct Biol. 2014 October ; 0: 96–104. doi:10.1016/j.sbi.2014.08.001. 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 includes experimental data, it quantifies the difference between the observed data and the data computed from the model. Therefore, structural characterization can be described as a four-stage process: (i) gathering input information, (ii) designing model representation and converting information into a scoring function, (iii) sampling good-scoring models, and (iv) analyzing models and information. For example, in X-ray crystallography a model consists of atomic positions, and the scoring function assesses the agreements (i) between the computed and observed structure factors via the Rfree parameter [ 1 ] as well as (ii) between the model geometry and the ideal geometry implied by a molecular mechanics force field via the potential energy of the model. 

 To use a model well, we need to assess its accuracy (stage iv above). Assessment standards and corresponding tools have already been developed for X-ray crystallography [ 2 ] and Nuclear Magnetic Resonance (NMR) spectroscopy [ 3 ], while they are still evolving for electron microscopy (EM) [ 4 ], Small Angle X-ray Scattering [ 5 , 6 ], and comparative modeling [ 7 ]. Standard validation of the crystallographic and NMR entries in the Protein Data Bank (PDB) [ 8 ] includes assessing geometrical features such as stereochemistry and packing, fit of the model to the experimental data, and the quality of the data itself. In the EM field, Fourier Shell Correlation (FSC) is commonly used to estimate map resolution [ 4 , 9 , 10 ]. Recently, new validation methods for EM maps were suggested, including tilt pair analysis [ 11 ], gold-standard FSC curves [ 4 ], high-resolution noise substitution [ 12 , 13 ], and ResLog plots [ 14 • ]. In SAXS data validation, the χ-free criterion was recently proposed [ 15 ••], inspired by Rfree in crystallography. Protein aggregation can be revealed in the Guinier plot, inter-particle interference can be detected by measuring SAXS profiles at multiple concentrations, and conformational heterogeneity is to some degree reflected in the Kratky or Porod-Debye plots [ 16 ]. Estimating the accuracy of comparative models is still challenging, but methods based on a variety of criteria do exist [ 7 , 17 , 18 ]. 

 No single experimental method is guaranteed to produce a satisfactory structure for a given system. Nevertheless, structure determination can often benefit from an integrative (hybrid) approach, where information from multiple experimental datasets is used to compute all structural models that are consistent with the available data [ 19 – 22 ]. Data from X-ray crystallography, EM, NMR spectroscopy, SAXS, cross-linking combined with mass spectrometry (MS), Förster resonance energy transfer (FRET) spectroscopy, double electron-electron resonance (DEER), and hydrogen–deuterium exchange (HDX) is frequently used in integrative structure determination (Table 1). Sometimes integrative models are assessed based on clustering of models, modeling with simulated data, observation of non-random patterns in the models, and modeling with subsets of data [ 20 ]. However, a set of standards for validating integrative models has not yet been developed [ 22 ]. 

 It is essential for appropriate use of a structural model to estimate errors in the model as well as the data used to compute it. Model error is defined as the difference between the model and true structure. It originates from several different sources. First, input data can be sparse, noisy, ambiguous, or incoherent (Glossary). Second, the system representation can be too coarse, resulting in some input information being ignored. Third, the scoring function may not accurately capture the input information or the input information is insufficient to 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 identify the true structure. Fourth, sampling may not find the true structure due to many degrees of freedom used to represent the system. Because the true structure is unknown in real applications, model error is also unknown. However, the lower bound on the model error can often be estimated as the precision of the set of models consistent with the input information. Here, we describe the origins of uncertainty in each stage of integrative modeling, and suggest how to quantify and minimize it. 

#### Stage 1: Gathering information 

 Spatial information about a given system can include data from experiments such as those listed above, statistical propensities such as atomic statistical potentials extracted from known protein structures, and physical laws, such as interatomic interactions approximated by a molecular mechanics force field. This information is used to represent the system as well as to sample and rank its possible configurations. There are four sources of uncertainty in the information, as follows. 

 Data sparseness The data sparseness measures the amount of information in the data relative to the number of degrees of freedom in the model; the amount of information in the data depends on the number of data points and their precision as well as their interdependence. Data sparseness affects the precision of the model [ 23 ]. For example, for a protein-protein complex mapped by a single cross-link, if each protein is represented by a single sphere, the data sparseness is 1 data point per 1 degree of freedom; if the proteins are represented by their rigid atomic structures, the data sparseness is 1 data point per 6 degrees of freedom (3 rotations and 3 translations). In X-ray crystallography, the data sparseness can be quantified by the number of reflections divided by the number of atoms in the unit cell. In NMR spectroscopy, the data sparseness is usually quantified by the number of NOE restraints per residue. In SAXS, the data sparseness of a SAXS profile is defined using the Nyquist-Shannon sampling theorem: given the maximum dimension (dmax), the sampling theorem determines that the number of unique, evenly distributed observations for a maximum scattering vector (qmax) is given by (dmax qmax)/π. The problem with sparse data is that there are more free parameters than observations, which may lead to an over-interpretation of the data (over-fitting). 

 Data error Error of the data is the sum of random and systematic measurement errors. The magnitude of random error can best be assessed by multiple repeated measurements; systematic errors for a given type of data can be estimated by benchmarks relying on known structures. For example, in X-ray crystallography the random error is caused by random variations among the crystals as well as noise in the X-ray flux, detector and electronics, while the systematic error can result from radiation damage, conformational heterogeneity of the sample, and crystal packing defects [ 24 ]. In SAXS, the random error sources are similar to those in crystallography, while the systematic error can result from sample aggregation and radiation damage [ 5 ]. 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 Data ambiguity Data ambiguity is the uncertainty in assigning data points to specific components of the system. For example, it is generally not possible to assign which of the three methyl protons gave rise to an observed NOE signal [ 25 ]. Another example is the ambiguity of assigning a cross-link to a specific instance of a protein when the complex contains multiple instances of it. In contrast, diffraction and scattering data are a function of all components of a system and thus not ambiguous. 

 Data incoherence Data incoherence is a result of compositional or conformational heterogeneity of one or more samples used to generate one or more datasets for modeling; for example, a system may exist as a mixture of two states in an NMR solution experiment or it may exist in different states in X-ray (crystal) and SAXS (solution) experiments. As a result, the measured data will be a mixture of contributions from each state. The ability to disentangle different states depends on the precision and accuracy of the data; for example, conformational differences smaller than the precision of the data may be difficult to detect. 

#### Stages 2 and 3: Converting input information into system representation, 

#### scoring function, and sampling 

 Input information about the structure of the system can be used (i) to select the set of variables that represent the system (system representation), (ii) to rank the different configurations (scoring function), and (iii) to search for good scoring solutions (sampling). It is often most computationally efficient, although not always possible, to encode information into the representation; in contrast it is generally most straightforward, but least efficient, to encode information into the scoring function. For example, in protein-protein docking, maximization of shape complementarity can be encoded into a scoring function that is then optimized by a generic optimization method. Alternatively, maximization of shape complementarity can also be encoded more efficiently through a representation consisting of shape descriptors, such as surface curvature, resulting in faster sampling by generating only configurations of subunits with complementary shape descriptors [ 26 ]. 

#### Representation 

 The representation of a system is defined by all the variables that need to be determined based on input information, including the assignment of the system components to geometric objects, such as points and spheres. A simple example is Cartesian coordinates for points corresponding to the individual atoms. More complex representations can assign a component to other geometric primitives (eg, spheres, ellipsoids, and 3D Gaussian density functions) and include additional degrees of freedom, such as the number of states in the system and their weights. For instance, in a high-resolution representation, a sphere can represent a single atom, while in a coarse-grained representation it may correspond to a residue. Coarse-graining can be used to encode the uncertainty arising from both static and dynamic variability. Moreover, in a “rigid body”, the relative positions of the primitives (eg, atoms in a domain) can be constrained, for example based on a crystallographic structure. In 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 most applications, the representation is determined before any other computations and is not changed. The resolution of the representation should be commensurate with the input information. In some cases, it is beneficial to represent different parts of a structure with different representations or a part may be described with several different inter-linked representations simultaneously (ie, multi-scale representation); in such a case, information can be applied to restrain the model by using the most convenient representation [ 27 ]. 

 When defining the representation, we usually have to balance between the requirements of scoring and sampling. We need a representation that is sufficiently detailed for accurately assessing a match between a model and the input information. For example, when using chemical cross-linking information, we need to choose between representing the cross-linker explicitly with all of its atoms [ 28 ] or implicitly as a function of the distance between the cross-linked residues. To minimize data sparseness, we also need a representation that is sufficiently coarse, given the invariably limited information content of the data. Finally, the representation should also be sufficiently coarse to allow for exhaustive sampling of good scoring models in a feasible timeframe. While it would be best to be able to compute an optimal representation based on the input information, this is not yet possible. 

#### Scoring 

 Most generally, the scoring function ranks alternative models based on the evidence provided by the input information. The scoring function should take into account the uncertainty in the input information, including sparseness, error, ambiguity, and incoherence. For example, a scoring function could evaluate whether or not a given model fits the data within its error bars. Ambiguity in the data assignment should also be accounted for by the scoring function. For example, to address the ambiguity in methyl proton assignment for an observed NOE signal, the signal is often assigned to the center of mass of the three methyl protons [ 25 ]. For a complex with multiple copies of the same protein, a cross-link can be assigned to the copy of the protein that satisfies it best [ 20 ]. When a sample is heterogeneous (ie, data are incoherent), a scoring function should rank instances of a model, each one of which consists of multiple structures (multi-state model). For example, protein heterogeneity in a crystal can be modeled using snapshots of molecular dynamics simulations [ 29 ••]. Protein dynamics in solution, as measured by SAXS and NMR spectroscopy, can be modeled by fitting multiple weighted conformations to the data [ 30 – 34 ]. In EM single particle reconstruction, heterogeneity can be addressed by multi-model reconstruction using multi-stage clustering [ 35 ]. 

 The most objective ranking of models is in principle achieved by a Bayesian scoring function [ 36 ]. The Bayesian approach estimates the probability of a model, given information available about the system, including both prior knowledge and newly acquired experimental data. When modeling heterogeneous systems, model M includes a set of N modeled structures X = {Xi}, their population fractions in the sample {wi}, and potentially additional parameters (eg, the unknown data errors). The posterior probability p(M|D, I) of model M given data D and prior knowledge I is 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 where the likelihood function p(D|M, I) is the probability of observing data D given M and I; and the prior p(M|I) is the probability of model M given I. The likelihood function is based on the forward model f(X) that predicts the data point that would have been observed for structure(s) X in the absence of experimental error, and a noise model that specifies the distribution of the deviation between the experimentally observed and predicted data points. The Bayesian scoring function is defined as S(M) = − log[p(D|M, I)· p(M|I)] which ranks the models the same as the posterior probability. The most probable models are found by selecting the best scoring models sampled from the posterior distribution. 

 The Bayesian scoring function can account for most sources of uncertainty in data without over-fitting. It was successfully adopted for NMR spectroscopy data [ 36 , 37 ], and recently cryo-EM density maps [ 38 , 39 ••]. Bayesian structure determination based on sparse NOE measurements produces more accurate structures and better estimates of precision than standard NMR structure determination methods [ 36 , 37 , 40 ]. In single particle EM reconstruction, the Bayesian approach results in density maps with higher resolution than those from standard reconstruction methods using the same input datasets [ 38 , 39 ]; moreover, high-resolution maps can be obtained from only a few thousand of particles [ 41 – 43 ]. Recently, the BioEM method for Bayesian analysis of individual EM images that can deal with conformational heterogeneity was developed [ 44 ]. Bayesian scoring functions have also been developed for cysteine cross-linking [ 45 ], chemical cross-linking [ 46 ], FRET spectroscopy [ 47 ], and atomic statistical potentials [ 48 ]. 

 The Bayesian approach is more objective than traditional scoring functions in a number of respects: (i) inference of unknown quantities, such as data error and state weights, (ii) combination of different types of information, (iii) inference of multiple structures, (iv) estimate of model precision, and (v) “marginalization” of parameters that are difficult to determine. The main disadvantage is that the model is more elaborate (cf, noise model and priors) and a more exhaustive sampling of structural and parameter space is required. 

#### Sampling 

 A variety of optimization methods (eg, conjugate gradients), sampling algorithms (eg, Monte Carlo), and even exhaustive enumeration (eg, Fast Fourier Transform) can be used to find models consistent with input information. The major source of uncertainty in this stage is insufficient sampling due to the ruggedness and high dimensionality of the scoring function landscape that needs to be sampled. As a result, it is almost never certain that the best scoring models were sampled. For stochastic sampling, such as the Monte Carlo algorithm, the thoroughness of sampling can be indicated by showing that new independent runs (eg, using random starting configurations and different random number generator seeds) do not result in significantly different good-scoring solutions (“convergence test”) [ 49 ]. Passing such a test is a necessary but not sufficient condition for thorough sampling; a positive outcome of the test may be misleading if, for example, the landscape contains only 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 a narrow, and thus difficult to find, pathway to the pronounced minimum corresponding to the native state. 

 For multi-state models, the sampling is often performed in two steps, due to the relatively high number of degrees of freedom involved. First, a large set of possible single configurations is sampled. Second, the sets of configurations in a multi-state model are enumerated, for example by using a genetic algorithm [ 31 , 32 ], a maximum entropy approach [ 33 ], or a deterministic method [ 34 ]. 

#### Stage 4: Analyzing models and information 

 Input information and output models are analyzed in order to estimate model precision and accuracy, to detect inconsistent information and missing information, as well as to suggest most informative future experiments. There are three possible outcomes of modeling, based on the number of clusters of models and consistency between the models and information. The following discussion applies to single-state models, but similar considerations can also be extended to multi-state models. First, if only a single model (or a cluster of similar models) satisfies all restraints and thus all input information, there is probably sufficient information for determining the structure (with the precision corresponding to the variability within the cluster). Second, if two or more different models are consistent with the restraints, the information is insufficient to define the single state or there are multiple significantly populated states. If the number of distinct models is small, the structural differences between the models may suggest additional experiments to narrow down the possible solutions. Third, if no model satisfies all input information, the information or its interpretation in terms of the restraints are incorrect, the representation needs to include additional degrees of freedom, and/or sampling needs to be improved (regardless of the outcome of the convergence test above). 

 If multiple structural states are indicated, care must be taken that the scoring function explicitly allows for this possibility [ 31 – 34 , 45 , 46 ]. When a mixture of states is modeled, the number of states needs to be determined. Frequently, Occam’s razor suggests that the smallest number of states sufficient to explain the input information within some threshold is the optimal choice. An example of this approach is the “minimal ensemble” method in molecular modeling based on SAXS data [ 32 ]. However, sometimes Occam’s razor is not applicable. For example, even though a SAXS profile of an intrinsically disordered protein may be matched by a sum of profiles for the minimal ensemble structures, the system is likely to exist in a large ensemble of many widely different states; such cases are indicated by similarity between distributions of structural properties, such as the radius of gyration, of the minimal and large ensembles [ 31 ]. 

 Once we obtain a model (single or multi-state) that satisfies the input data, we can analyze it to estimate precision and accuracy. It is impossible to know with certainty the accuracy of the proposed structure without knowing the real native structure. However, accuracy can be estimated based on rules derived from benchmark studies that involve modeling of known structures. For example, there is a strong correlation of the accuracy of an X-ray structure with the resolution of the X-ray dataset and Rfree [ 1 ]. In addition to such broad rules, five 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 types of analysis that are indicative of model precision and accuracy in specific cases have been proposed [ 20 ], as follows (the first three tests are examples of statistical resampling [ 50 ]). 

 Estimating model precision based on variability in the ensemble of good-scoring models The model ensemble is analyzed in terms of the precision of its features, such as the protein positions and contacts [ 49 , 51 – 53 ]; the precision is defined by the variability in the ensemble and likely provides the lower bound on its accuracy. Of particular interest are the features that are present in most configurations in the ensemble and have a single maximum in their probability distribution. The spread around the maximum describes how precisely the feature was determined by the input information. A more thorough test is performed by estimation of structural variability in multiple random subsets of the ensemble [ 52 ••, 54 ••]. 

 Self-consistency of the experimental data Inconsistencies in the experimental data or its interpretation are indicated by an ensemble of models containing only frustrated structures that do not satisfy the input data, although such an outcome can also arise from the failure of sampling. If there is a model that satisfies all data, the probability of such a model occurring by chance can be indicated by statistical significance tests; if this probability is low, the model is likely to be correct. In these tests, the labels on the data points are randomized or permuted, followed by re-computing the model; for example, one can assign cross-links to random residue pairs [ 55 ]. 

 Validating models by using random subsets of experimental data The structure can be directly validated against experimental data that was not included in the structure calculation [ 52 ••]. This criterion is similar to the crystallographic Rfree parameter and can be used to assess both the model accuracy and the input data [ 1 ]. Alternatively, modeling can be repeated with random subsets of the data. Common statistical techniques for this validation include cross validation and bootstrapping [ 50 ]. 

 Reproducibility of the model with simulated data In this approach, a native structure is assumed, the restraints to be tested are simulated from this structure, the structure is then reconstructed based only on these restraints, and finally the reconstruction is compared to the original assumed structure [ 49 ]. Using such simulations, the dependence of model accuracy on the amount, quality, and type of information can be mapped for future prediction of accuracy. 

 Patterns unlikely to occur by chance Unlikely patterns emerging from mapping independent and unused data on the structure also increase our confidence in a model, similarly to validation by information not used in modeling. For example, the model of the nuclear pore complex (NPC) revealed an unexpected 16-fold pseudo-symmetry in the arrangement of fold types of the constituent proteins, in addition to the known 8-fold symmetry [ 49 ]. The 16-fold pseudo-symmetry validates the model because the fold types were not used in modeling and the 16-fold pseudo 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 symmetry is unlikely to arise by chance (while it can be reasonably explained by gene duplications in the evolution of the NPC). 

#### Conclusions 

 Integrative structure determination needs de facto standards and tools for assessing the input data and resulting models, following in the footsteps of X-ray crystallography and NMR spectroscopy with established structure validation criteria. 

#### Acknowledgments 

 We acknowledge support from NIH R01 GM083960 and NIH U54 GM103511 (A.S.). 

#### References 

1. Brünger AT. Free R value: a novel statistical quantity for assessing the accuracy of crystal     structures. Nature. 1992; 355:472–475. [PubMed: 18481394] 

2. Read RJ, Adams PD, Arendall WB, Brunger AT, Emsley P, Joosten RP, Kleywegt GJ, Krissinel     EB, Lütteke T, Otwinowski Z, et al. A new generation of crystallographic validation tools for the     protein data bank. Structure. 2011; 19:1395–1412. [PubMed: 22000512] 

3. Montelione GT, Nilges M, Bax A, Güntert P, Herrmann T, Richardson JS, Schwieters CD, Vranken     WF, Vuister GW, Wishart DS, et al. Recommendations of the wwPDB NMR Validation Task     Force. Structure. 2013; 21:1563–1570. [PubMed: 24010715] 

4. Henderson R, Sali A, Baker ML, Carragher B, Devkota B, Downing KH, Egelman EH, Feng Z,     Frank J, Grigorieff N, et al. Outcome of the first electron microscopy validation task force meeting.     2012:205–214. 

5. Jacques DA, Guss JM, Svergun DI, Trewhella J. Publication guidelines for structural modelling of     small-angle scattering data from biomolecules in solution. Acta Crystallogr D Biol Crystallogr.     2012; 68:620–626. [PubMed: 22683784] 

6. Trewhella J, Hendrickson WA, Kleywegt GJ, Sali A, Sato M, Schwede T, Svergun DI, Tainer JA,     Westbrook J, Berman HM. Report of the wwPDB Small-Angle Scattering Task Force: data     requirements for biomolecular modeling and the PDB. Structure. 2013; 21:875–881. [PubMed:     23747111] 

7. Schwede T, Sali A, Honig B, Levitt M, Berman HM, Jones D, Brenner SE, Burley SK, Das R,     Dokholyan NV, et al. Outcome of a workshop on applications of protein models in biomedical     research. 2009:151–159. 

8. Berman HM, Westbrook J, Feng Z, Gilliland G, Bhat TN, Weissig H, Shindyalov IN, Bourne PE.     The Protein Data Bank. Nucleic Acids Research. 2000; 28:235–242. [PubMed: 10592235] 

9. Saxton WO, Baumeister W. The correlation averaging of a regularly arranged bacterial cell     envelope protein. J Microsc. 1982; 127:127–138. [PubMed: 7120365] 

10. Harauz G, van Heel M. Exact filters for general geometry three dimensional reconstruction.     Proceedings of the IEEE Computer Vision and Pattern Recognition. 1986; 78:146–156. 

11. Henderson R, Chen S, Chen JZ, Grigorieff N, Passmore LA, Ciccarelli L, Rubinstein JL, Crowther     RA, Stewart PL, Rosenthal PB. Tilt-pair analysis of images from a range of different specimens in     single-particle electron cryomicroscopy. Journal of Molecular Biology. 2011; 413:1028–1046.     [PubMed: 21939668] 

12. Scheres SHW, Chen S. Prevention of overfitting in cryo-EM structure determination. Nat Methods.     2012; 9:853–854. [PubMed: 22842542] 

13. Chen S, McMullan G, Faruqi AR, Murshudov GN, Short JM, Scheres SHW, Henderson R. High-     resolution noise substitution to measure overfitting and validate resolution in 3D structure     determination by single particle electron cryomicroscopy. Ultramicroscopy. 2013; 135:24–35.     [PubMed: 23872039] 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 •14. Stagg SM, Noble AJ, Spilman M, Chapman MS. ResLog plots as an empirical metric of the quality of cryo-EM reconstructions. Journal of Structural Biology. 2014; 185:418–426. A method for assessing the accuracy of cryo-EM reconstructions is presented. A plot of inverse resolution vs. the logarithm of the number of single particles (a “ResLog” plot) provides metrics for the reliability of the reconstruction and the overall quality of the dataset and processing. [PubMed: 24384117] ••15. Rambo RP, Tainer JA. Accurate assessment of mass, models and resolution by small-angle scattering. Nature. 2013; 496:477–481. A statistical method based on the Nyquist–Shannon sampling and the noisy-channel coding theorems is used for evaluating structural models against SAS data. [PubMed: 23619693] 

16. Rambo RP, Tainer JA. Characterizing flexible and intrinsically unstructured biological     macromolecules by SAS using the Porod-Debye law. Biopolymers. 2011; 95:559–571. [PubMed:     21509745] 

17. Haas J, Roth S, Arnold K, Kiefer F, Schmidt T, Bordoli L, Schwede T. The Protein Model Portal--     a comprehensive resource for protein structure and model information. Database (Oxford). 2013;     2013:bat031–bat031. [PubMed: 23624946] 

18. Kryshtafovych A, Barbato A, Fidelis K, Monastyrskyy B, Schwede T, Tramontano A. Assessment     of the assessment: evaluation of the model quality estimates in CASP10. Proteins. 2014; 82 (Suppl     2):112–126. [PubMed: 23780644] 

19. Sali A, Glaeser R, Earnest T, Baumeister W. From words to literature in structural proteomics.     Nature. 2003; 422:216–225. [PubMed: 12634795] 

20. Alber F, Dokudovskaya S, Veenhoff LM, Zhang W, Kipper J, Devos D, Suprapto A, Karni-     Schmidt O, Williams R, Chait BT, et al. Determining the architectures of macromolecular     assemblies. Nature. 2007; 450:683–694. [PubMed: 18046405] 

21. Russel D, Lasker K, Webb B, Velázquez-Muriel J, Tjioe E, Schneidman-Duhovny D, Peterson B,     Sali A. Putting the Pieces Together: Integrative Modeling Platform Software for Structure     Determination of Macromolecular Assemblies. Plos Biol. 2012; 10:e1001244. [PubMed:     22272186] 

22. Ward AB, Sali A, Wilson IA. Biochemistry. Integrative structural biology. Science. 2013;     339:913–915. [PubMed: 23430643] 

23. Habeck M. Statistical mechanics analysis of sparse data. J Struct Biol. 2011; 173:541–548.     [PubMed: 20869444] 

24. Borek D, Otwinowski Z. Everything Happens at Once – Deconvolving Systematic Effects in X-ray     Data Processing. Advancing Methods for Biomolecular Crystallography. 2013:105–112. 

25. Guentert P, Braun W, Billeter M. Automated stereospecific proton NMR assignments and their     impact on the precision of protein structure determinations in solution. J Am Chem Soc. 1989;     111:3997–4004. 

26. Duhovny, D.; Nussinov, R.; Wolfson, HJ. Efficient Unbound Docking of Rigid Molecules.     Proceedings of the 2’nd Workshop on Algorithms in Bioinformatics (WABI); 2002. p. 185-200. 

27. Murtola T, Bunker A, Vattulainen I, Deserno M, Karttunen M. Multiscale modeling of emergent     materials: biological and soft matter. Phys Chem Chem Phys. 2009; 11:1869–1892. [PubMed:     19279999] 

28. Bahaman A, Malmström L, Aebersold R. Xwalk: computing and visualizing distances in cross-     linking experiments. Bioinformatics. 2011; 27:2163–2164. [PubMed: 21666267] ••29. Burnley BT, Afonine PV, Adams PD, Gros P. Modelling dynamics in protein crystal structures     by ensemble refinement. Elife. 2012; 1:e00311–e00311. An ensemble of structures is used for     refinement of high-resolution X-ray diffraction datasets resulting in a better fit to the data than a     single structure. [PubMed: 23251785] 

30. Lindorff-Larsen K, Best RB, Depristo MA, Dobson CM, Vendruscolo M. Simultaneous     determination of protein structure and dynamics. Nature. 2005; 433:128–132. [PubMed:     15650731] 

31. Bernado P, Mylonas E, Petoukhov MV, Blackledge M, Svergun DI. Structural Characterization of     Flexible Proteins Using Small-Angle X-ray Scattering. J Am Chem Soc. 2007; 129:5656–5664.     [PubMed: 17411046] 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

32. Pelikan M, Hura GL, Hammel M. Structure and flexibility within proteins as identified through     small angle X-ray scattering. Gen Physiol Biophys. 2009; 28:174–189. [PubMed: 19592714] 

33. Różycki B, Kim YC, Hummer G. SAXS Ensemble Refinement of ESCRT-III CHMP3     Conformational Transitions. Structure/Folding and Design. 2011; 19:109–116. 

34. Berlin K, Castañeda CA, Schneidman-Duhovny D, Sali A, Nava-Tudela A, Fushman D.     Recovering a representative conformational ensemble from underdetermined macromolecular     structural data. J Am Chem Soc. 2013; 135:16595–16609. [PubMed: 24093873] 

35. Shatsky M, Hall RJ, Nogales E, Malik J, Brenner SE. Automated multi-model reconstruction from     single-particle electron microscopy data. J Struct Biol. 2010; 170:98–108. [PubMed: 20085819] 

36. Rieping W, Habeck M, Nilges M. Inferential structure determination. Science. 2005; 309:303–306.     [PubMed: 16002620] 

37. Nilges M, Bernard A, Bardiaux B, Malliavin T, Habeck M, Rieping W. Accurate NMR structures     through minimization of an extended hybrid energy. Structure/Folding and Design. 2008;     16:1305–1312. 

38. Scheres SHW. RELION: implementation of a Bayesian approach to cryo-EM structure     determination. J Struct Biol. 2012; 180:519–530. [PubMed: 23000701] ••39. Scheres SHW. A Bayesian view on cryo-EM structure determination. J Mol Biol. 2012;     415:406–418. A Bayesian formulation of cryo-EM structure determination is presented, where     smoothness in the reconstructed density is imposed through a Gaussian prior in the Fourier     domain. The structure and the parameters are determined from the data without user bias.     [PubMed: 22100448] 

40. Rieping W, Nilges M, Habeck M. ISD: a software package for Bayesian NMR structure     calculation. Bioinformatics. 2008; 24:1104–1105. [PubMed: 18310055] 

41. Fernández IS, Bai X-C, Hussain T, Kelley AC, Lorsch JR, Ramakrishnan V, Scheres SHW.     Molecular architecture of a eukaryotic translational initiation complex. Science. 2013;     342:1240585–1240585. [PubMed: 24200810] 

42. Bai X-C, Fernández IS, McMullan G, Scheres SH. Ribosome structures to near-atomic resolution     from thirty thousand cryo-EM particles. Elife. 2013; 2:e00461–e00461. [PubMed: 23427024] 

43. Sauerwald A, Sandin S, Cristofari G, Scheres SHW, Lingner J, Rhodes D. Structure of active     dimeric human telomerase. Nat Struct Mol Biol. 2013; 20:454–460. [PubMed: 23474713] 

44. Cossio P, Hummer G. Bayesian analysis of individual electron microscopy images: towards     structures of dynamic and heterogeneous biomolecular assemblies. J Struct Biol. 2013; 184:427– 

437. [PubMed: 24161733] 

45. Molnar KS, Bonomi M, Pellarin R, Clinthorne GD, Gonzalez G, Goldberg SD, Sali A, DeGrado     WF. Cys-scanning Disulfide crosslinking and Bayesian modeling suggest scissoring motions in the     histidine kinase, PhoQ. Structure. (in press). 

46. Street TO, Zeng X, Pellarin R, Bonomi M, Sali A, Kelly MJS, Chu F, Agard DA. Elucidating the     mechanism of substrate recognition by the bacterial Hsp90 molecular chaperone. J Mol Biol.     2014; 426:2393–404. [PubMed: 24726919] 

47. Bonomi M, Muller EGD, Pellarin R, Kim SJ, Russel D, Ramsden R, Sundin BA, Davis TN, Sali     A. Protein complex structures from Bayesian modeling of in vivo. FRET data. 

48. Dong GQ, Fan H, Schneidman-Duhovny D, Webb B, Sali A. Optimized atomic statistical     potentials: assessment of protein interfaces and loops. Bioinformatics. 2013; 29:3158–3166.     [PubMed: 24078704] 

49. Alber F, Dokudovskaya S, Veenhoff LM, Zhang W, Kipper J, Devos D, Suprapto A, Karni-     Schmidt O, Williams R, Chait BT, et al. The molecular architecture of the nuclear pore complex.     Nature. 2007; 450:695–701. [PubMed: 18046406] 

50. Efron, B.; Efron, B. The jackknife, the bootstrap and other resampling plans. 1982. 

51. Tjong H, Gong K, Chen L, Alber F. Physical tethering and volume exclusion determine higher-     order genome organization in budding yeast. Genome Res. 2012; 22:1295–1305. [PubMed:     22619363] ••52. Lasker K, Förster F, Bohn S, Walzthoeni T, Villa E, Unverdorben P, Beck F, Aebersold R, Sali     A, Baumeister W. Molecular architecture of the 26S proteasome holocomplex determined by an     integrative approach. Proc Natl Acad Sci US A. 2012; 109:1380–1387. The architecture of the 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 26S proteosome is determined using a cryo-EM map and cross-links. The final structural ensemble is validated using new data (cross links from a different species, domain contacts, atomic models) and jack-knifing by omitting one restraint at a time. 

53. Loquet A, Sgourakis NG, Gupta R, Giller K, Riedel D, Goosmann C, Griesinger C, Kolbe M,     Baker D, Becker S, et al. Atomic model of the type III secretion system needle. Nature. 2012;     486:276–279. [PubMed: 22699623] ••54. Murakami K, Elmlund H, Kalisman N, Bushnell DA, Adams CM, Azubel M, Elmlund D, Levi-     Kalisman Y, Liu X, Gibbons BJ, et al. Architecture of an RNA polymerase II transcription pre-     initiation complex. Science. 2013; 342:1238724–1238724. The architecture of an RNA     polymerase II transcription pre-initiation complex is determined using a cryo-EM map and cross-     links. The final ensemble of models is validated using bootstrapping. [PubMed: 24072820] 

55. Kalisman N, Adams CM, Levitt M. Subunit order of eukaryotic TRiC/CCT chaperonin by cross-     linking, mass spectrometry, and combinatorial homology modeling. Proc Natl Acad Sci US A.     2012; 109:2884–2889. 

56. Tosi A, Haas C, Herzog F, Gilmozzi A, Berninghausen O, Ungewickell C, Gerhold CB, Lakomek     K, Aebersold R, Beckmann R, et al. Structure and subunit topology of the INO80 chromatin     remodeler and its nucleosome complex. Cell. 2013; 154:1207–1219. [PubMed: 24034245] 

57. Ciferri C, Lander GC, Maiolica A, Herzog F, Aebersold R, Nogales E. Molecular architecture of     human polycomb repressive complex 2. Elife. 2012; 1:e00005–e00005. [PubMed: 23110252] 

58. Greber BJ, Boehringer D, Leitner A, Bieri P, Voigts-Hoffmann F, Erzberger JP, Leibundgut M,     Aebersold R, Ban N. Architecture of the large subunit of the mammalian mitochondrial ribosome.     Nature. 2014; 505:515–519. [PubMed: 24362565] ••59. Erzberger JP, Stengel F, Pellarin R, Zhang S, Schaefer T, Ayelett CH, Cimermančič P,     Boehringer D, Sali A, Aebersold R, et al. Molecular architecture of the 40S•eIF1•eIF3 translation     initiation complex. Cell. (in press). The architecture of eukaryotic initiation factor 3 (eIF3) in     complex with 40S ribosomal subunit was determined through integration of chemical cross-     linking and crystallographic structures by a Bayesian approach. The model is validated using EM     density map. 

60. Politis A, Stengel F, Hall Z, Hernández H, Leitner A, Walzthoeni T, Robinson CV, Aebersold R. A     mass spectrometry-based hybrid method for structural modeling of protein complexes. Nat     Methods. 201410.1038/nmeth.2841 •61. Boura E, Różycki B, Herrick DZ, Chung HS, Vecer J, Eaton WA, Cafiso DS, Hummer G, Hurley     JH. Solution structure of the ESCRT-I complex by small-angle X-ray scattering, EPR, and FRET     spectroscopy. Proc Natl Acad Sci US A. 2011; 108:9437–9442. A multi-state model consisting of     six conformations of ESCRT-1 is used for interpretation of SAXS and EPR data. The model is     validated using FRET data. 

62. Huang J-R, Warner LR, Sanchez C, Gabel F, Madl T, Mackereth CD, Sattler M, Blackledge M.     Transient electrostatic interactions dominate the conformational equilibrium sampled by multi-     domain splicing factor U2AF65: A combined NMR and SAXS study. J Am Chem Soc.     201410.1021/ja502030n 

63. Deshmukh L, Schwieters CD, Grishaev A, Ghirlando R, Baber JL, Clore GM. Structure and     dynamics of full-length HIV-1 capsid protein in solution. J Am Chem Soc. 2013; 135:16133– 

16147. [PubMed: 24066695] 

64. Baù D, Sanyal A, Lajoie BR, Capriotti E, Byron M, Lawrence JB, Dekker J, Marti-Renom MA.     The three-dimensional folding of the α-globin gene domain reveals formation of chromatin     globules. Nat Struct Mol Biol. 2011; 18:107–114. [PubMed: 21131981] 

65. Baù D, Marti-Renom MA. Structure determination of genomic domains by satisfaction of spatial     restraints. Chromosome Res. 2011; 19:25–35. [PubMed: 21190133] ••66. Kalhor R, Tjong H, Jayathilaka N, Alber F, Chen L. Genome architectures revealed by tethered     chromosome conformation capture and population-based modeling. Nat Biotechnol. 2012;     30:90–98. A structural modeling procedure that computes a population of 3D genome structures     from the TCC data is introduced. [PubMed: 22198700] 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 Box 1 Glossary 

 Input data experimental data used to compute a model 

 Input information experimental data and any additional information 

 Data sparseness a measure of the amount of data relative to the number of degrees of freedom in the model 

 Data error the difference between the measured data and its true value, which can be computed given a forward model and the true structure; data error can be random and/or systematic, affecting the precision and the accuracy of the measured data 

 Data ambiguity a data point is ambiguous when it cannot be assigned to the specific components of the model 

 Data incoherence a dataset is incoherent when it is derived from a compositionally or configurationally heterogeneous sample 

 Single-state model a model that specifies a single structural state and value for any other parameter 

 Multi-state model a model that specifies two or more co-existing structural states and values for any other parameter 

 Ensemble of structural models 

 a set of structural models each one of which is consistent with the data 

 Ensemble precision variability among structural models in the ensemble 

 Error or accuracy of a structural model 

 the difference between the structural model and the true structure(s) 

 Representation resolution 

 a descriptor of the detail in the representation of the structural model (eg, atomic models consist of atoms) 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 Highlights 

- Integrative modeling needs standards and tools for assessing models and input     data 

- Model uncertainty originates from sparse, noisy, ambiguous, or incoherent data 

- Model uncertainty also originates from representation, scoring function and     sampling 

- Some methods for assessing data and models are listed 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 Figure 1. Uncertainty in integrative structure modeling. The four-stage scheme of integrative structure modeling is used to describe how to approach uncertainty in the data and the models. The collected information is converted into a scoring function that accounts for data error, ambiguity, and incoherence. The model representation should reflect data sparseness. After sampling, if good-scoring models satisfy the restraints, they are further evaluated by structural clustering and data validation tests. 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

#### NIH-PA Author Manuscript 

 Table 1 Some of the recent structures solved by an integrative approach. 

 Structure Experimental information Method S. cerevisiae INO80 [ 56 ] Cryo-EM map (17Å resolution), 212 intra-protein and 116 inter-protein cross-links 

 Manual modeling in Chimera Polycomb Repressive Complex 2 [ 57 ] Negative stain EM map (21Å resolution) and ~60 intra-protein and inter-protein cross-links 

 Manual modeling in Chimera 39S large subunit of the porcine mitochondrial ribosome [ 58 ] 

 Cryo-EM map (4.9Å resolution) and ~70 inter-protein crosslinks 

 COOT, O, PHENIX 

 S. pombe 26S holocomplex [ 52 ••] Cryo-EM map (8.4Å resolution) and 35 cross-links from S. pombe and 36 cross links from S. cerevisiae 

 IMP 

 S. cerevisiae RNA polymerase II transcription pre-initiation complex [ 54 ••] 

 Cryo-EM map (16Å resolution), 157 intra-protein and 109 inter-protein cross-links 

 Exhaustive enumeration 

 S. cerevisiae 40S•eIF1•eIF3 translation initiation complex [ 59 ••] 

 965 cross-links, including 126 unique eIF3-eIF3 and 40S•eIF1eIF3 cross links, negative stain EM map (28Å resolution), crystallographic structures of 40S complex, eIF3 domains 

 IMP 

 S. typhimurium Type III secretion system needle [ 53 ] 

 solid-state NMR, cryo-EM (19.5Å resolution) Rosetta 

 Methane monooxygenase hydroxylase (MMOH), toluene/o-xylene monooxygenase hydroxylase (ToMOH), and urease [ 60 ] 

 Composition and stoichiometry from native MS, collision cross section from ion mobility–MS and cross-links 

 IMP 

 ESCRT-I complex [ 61 • ] SAXS, double electron-electron transfer (DEER), and FRET^ EROS Hsp90 substrate recognition [ 46 ] 31 cross-links and NMR spectroscopy IMP Splicing factor U2AF65 [ 62 ] Paramagnetic relaxation enhancement (PRE), residue dipolar couplings (RDCs), and SAXS 

 ASTEROIDS 

 HIV-1 capsid protein [ 63 ] RDCs and SAXS Xplor-NIH 500-kilobase (kb) domain of human chromosome 16 [ 64 , 65 ] 

 Chromosome Conformation Capture Carbon Copy (5C) experiments and excluded volume 

 IMP 

 Human genome architecture [ 66 ••] Tethered chromosome conformation capture (TCC) and population-based modeling 

 IMP 



---

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

