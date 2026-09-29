# Layer 3 — Stuck-point cases

Nine anonymised cases from published protein-dynamics work. Each has three parts: what the authors saw, what they did and why, and how they wrote it. They show the shape of a good move at a stuck point; they are not templates for a particular system, and the numbers and state counts of the original work are deliberately left out.

---

## Case 1. Every dispersion curve went flat after a required cofactor was removed

**Authors saw.** An enzyme with a large mobile lid showed clear millisecond dispersion around the lid with its metal cofactor present. With the metal removed, every dispersion curve at the working temperature was flat. A separate rapid-mixing kinetics experiment on the metal-free enzyme indicated a very slow step somewhere in the catalytic cycle. The dispersion data were the only NMR dynamics data at that point.

**What they did and why.** They did not read the flat curves as "no motion". They wrote out the readings a flat curve allows: no exchange; exchange slow enough that its contribution is below what the experiment can see; exchange fast with a small shift difference. One temperature cannot separate these, so they measured the temperature dependence of the exchange contribution over a wide range and mapped which residues responded. The contribution rose uniformly on warming, in the same residues that report lid motion with the metal present, which is the behaviour of slow exchange and not of fast exchange. The absence of a second peak set was addressed rather than ignored: a minor state can be invisible from low population or from broadening by a fast return, so its absence was declared compatible with slow exchange. The quantitative rate was taken from the independent kinetics experiment, not from the dispersion.

**How they wrote it.** The dispersion data were stated to give a qualitative call only, with an explicit sentence that they cannot deliver accurate opening and closing rates or populations. The functional assignment of the process rested on the agreement between two independent methods measured under matched conditions, and the paper tabulated the two values side by side with their uncertainties and a footnote saying where each came from.

---

## Case 2. Two experiments on the same residues returned two different exchange processes

**Authors saw.** A small monomeric protein studied by CEST and by CPMG at two fields. CEST profiles of many residues showed one minor dip, and fitting them individually gave a slow process with a few-percent minor state. For such a process the CPMG contribution should have been negligible, yet the same residues showed clear dispersion, and fitting the CPMG data alone gave a process an order of magnitude faster with minor-state shifts unlike the CEST minor state.

**What they did and why.** They fitted each data type on its own first, so that the disagreement was documented as two per-type solutions rather than hidden inside one joint fit. They then wrote two candidate causes: the CPMG dispersion is noise or an artefact; or a second minor state exists that is fast relative to its shift difference and therefore unresolved by CEST. They tested by fitting both data types together with a model containing both minor states attached to the major state, and showed explicitly that a CEST-only global fit and a CPMG-only global fit each returned biased parameters compared with the joint solution. They repeated everything at roughly half the protein concentration to rule out self-association, and found the same profiles and parameters.

**How they wrote it.** The conclusion was stated as "at least" the number of minor states the data required, with the statement that neither experiment alone gives reliable parameters and that the two types must be analysed together, plus the kinetic range that the combination covers. The biased single-type parameters were reported in the paper, not discarded.

---

## Case 3. Freeing a relaxation rate rescued the fit, and that was the alarm

**Authors saw.** A well-studied protein whose earlier CPMG data fit a two-state exchange. New CEST data at several saturation fields, fitted with the minor-state transverse rate constrained equal to the ground state, gave an unsatisfactory chi-squared. Freeing the minor-state rate gave a good fit, with shift differences that agreed with the earlier CPMG values, but some minor-state rates came out far above the ground-state values, and those sites clustered around one structural feature.

**What they did and why.** The good fit and the agreement with CPMG were not taken as validation of the two-state scheme. They listed the candidates: the minor state truly has a much larger intrinsic rate at those sites; the minor-state dip is broadened by exchange with a further, sparsely populated state and the freed rate is absorbing that broadening; a fitting artefact. They compared the freed rates with what molecular size predicts, and generated synthetic CEST data from a scheme with an extra state and fitted it with the two-state model: the synthetic fit recovered the right shifts and returned exactly the elevated minor-state rates seen in the real data. They then fitted the real data with the extended scheme and all rates constrained equal, which fitted well. Because earlier CPMG work had never seen the extra state, they forward-simulated CPMG profiles from the new parameters with the original fields and timing and fitted them with a two-state model; the synthetic CPMG fitted two-state well with parameters like the published ones, so the extra state is invisible to CPMG rather than in contradiction with it.

**How they wrote it.** The elevated minor-state rate was written as the signature of an undetected state, with the sentence that agreement of fitted shifts with CPMG does not validate an assumed kinetic scheme. The relation to the earlier CPMG work was written as "consistent, and CPMG could not have detected it", with the simulation shown. The topology of the extra state was reported with the alternatives that fit equally well, a chi-squared scan over the weakly determined rate, and a statement that the preference among them rests on external simulation evidence.

---

## Case 4. Two topologies fit every probe equally well

**Authors saw.** Methyl dispersion and CEST on a homodimeric enzyme. For most probes in a shared slow process a two-state model fitted poorly and a three-state model better. Two three-state topologies, one linear and one bifurcated, fitted every probe equally well. Under the bifurcated model all probes returned the same rate and population for the slow process while the faster process varied from probe to probe; under the linear model the probes disagreed with each other.

**What they did and why.** They did not pick a topology on chi-squared, because chi-squared did not distinguish them. They compared the fitted parameters across probes under each topology and used consistency as the criterion: probes that share one concerted process should return the same rate and population, and the bifurcated model produced that agreement while the linear model would require the agreement to be a coincidence.

**How they wrote it.** The paper stated that the two models provide equally good fits, that the choice was made on the consistency of shared parameters across probes and not on fit quality, and treated the choice as a preference from a consistency argument. Quantities shared by both topologies were the ones carried into the functional interpretation.

---

## Case 5. A bound-like minor state in a sample that was purified on a ligand column

**Authors saw.** A ligand-binding domain with a shallow, exposed binding groove, studied by CPMG without added ligand. Groove residues shared one exchange process with a few-percent minor state whose fitted shift differences correlated closely with the free-to-bound shift changes. The protein had been eluted from an affinity column with a high ligand concentration and then buffer-exchanged repeatedly; the dissociation constant was known from calorimetry.

**What they did and why.** The attractive reading, that the free protein transiently samples a binding-competent conformation, was set beside the mundane one: residual ligand, so that the exchange is between free and ligand-bound protein. They back-calculated from the dissociation constant and the residual ligand concentration what bound fraction the contamination could produce, and found it orders of magnitude below the fitted minor population. They then removed remaining ligand by a further large factor with repeated ultrafiltration and repeated the dispersion measurement. Fewer residues gave usable data because of protein loss, but the groove residues gave the same exchange rate and population within error.

**How they wrote it.** The residual-ligand hypothesis was named in the text as the thing to be refuted, the calculation and the repeat measurement were both reported, and the conclusion was that the exchange is intrinsic and that binding can therefore proceed by conformational selection "in principle", with the question of whether it does so stated as a separate question answered later by a flux calculation.

---

## Case 6. Is the excited state a dissociated complex, and can literature rates be used?

**Authors saw.** An enzyme–product–cofactor complex whose loop residues fitted a global two-site exchange with a small minor population. The minor-state shift differences resembled the shifts of the product-free binary complex, so the excited state might simply be the complex with the product dissociated. The product concentration in the sample was high. Product off-rates had been published, but in a different buffer with a different cation, a different pH and a different temperature, for unlabelled protein.

**What they did and why.** Two candidates were written: the excited state is the physically dissociated binary complex; or it is a closed-like conformation with the product still bound. To test, they needed rates under the NMR conditions, and they did not borrow the published ones: they remeasured product dissociation by stopped-flow with the isotope-labelled protein in the NMR buffer at the NMR temperature, and found the rates differ from the literature values, with the cation the likely cause. With matched rates they estimated the equilibrium population of the product-free complex at the sample's product concentration, which was far below the fitted minor population; they recalled earlier data showing the exchange parameters independent of product concentration, as physical dissociation would not allow; and they simulated the full kinetic scheme with the measured rates.

**How they wrote it.** The sentence that it is essential to measure kinetic parameters under identical conditions was placed before the combination of kinetics and dispersion data, and only same-condition rates were combined. The conclusion that the product remains bound in the excited state was supported by the population comparison, the concentration independence and the simulation, each reported.

---

## Case 7. One ligand fell off the line

**Authors saw.** A receptor domain with a series of ligands and a coactivator peptide. For four chemically congeneric ligands, the minor-state population of a regulatory helix, estimated from a single methyl probe, ranked with transcriptional efficacy, and a thermodynamic analysis combining binding affinities with the NMR populations put the four on a straight line. A fifth ligand, of a different chemotype known to open a new pocket in the receptor, had high efficacy but a low apparent population, and its probe shift did not follow the scaling seen for the others.

**What they did and why.** They did not force the fifth ligand onto the line and did not drop it silently. They listed the candidate causes: the single-probe population estimate is unreliable for that complex; the exchanging conformations or their shift difference differ for that ligand, so the observed shift does not scale with population; the ligand rewires the allosteric pathway and gives an alternative active conformation. They examined the shift trend of the probe against the population scaling, analysed the coupling relation with and without the outlier for both peptides and both receptor constructs, and connected the anomaly to the structural rearrangement in its pocket.

**How they wrote it.** The population–efficacy relation was stated for the congeneric ligands only. The fifth ligand was written as a notable exception that probably uses a modified communication pathway, with that reading marked as a suggestion rather than a result. The single-probe population ranking itself was written as semiquantitative and conditional on identical shift differences across complexes.

---

## Case 8. Dispersion disappeared when the partner peptide was swapped

**Authors saw.** The same receptor domain. With the first coactivator peptide, the regulatory-helix probe showed dispersion in every ligand complex and a probe on a neighbouring helix showed weaker dispersion. With a second peptide of different sequence and tighter binding, recorded at one field, the helix probe showed no dispersion in any complex.

**What they did and why.** The two readings of a flat profile were written out: a single helix conformation dominates in these complexes (no exchange); or exchange persists but the shift difference between the states is negligible, or the rate has left the window. They looked at the second probe on the neighbouring helix in the second-peptide complexes: it had also lost its dispersion, whereas it had dispersion with the first peptide. Convergent loss at a second, independent probe favours loss of exchange over a probe-specific zero shift difference.

**How they wrote it.** The paper stated which interpretation the second-probe result supports and said that the alternative is not excluded outright but disfavoured. The consequence, that ligand-dependent variation of the coupling is unobservable in these complexes, was stated as a limit on what could be concluded, and the difference between the two coregulators was written as a difference in how strongly they drive the helix, not as a difference in ligand behaviour.

---

## Case 9. Exchange inside the dimer, or the dimer coming apart?

**Authors saw.** A small homodimeric protein with a moderate association constant, measured at millimolar concentration, studied by CPMG at two fields in a series of point variants. Exchange contributions appeared in three regions, mostly near the dimer interface, and their size differed widely between variants, from almost none to very large. The rotational correlation time matched a dimer, and the association constants were similar across the variants. The interface location fits both motion inside the dimer and monomer-dimer exchange.

**What they did and why.** They wrote down what each reading predicts. Monomer-dimer exchange should change when the total concentration changes, because the monomer fraction changes; it should also follow the association constants across variants. They repeated the dispersion measurement at half the concentration, with a clearly larger monomer fraction, for the variant with the largest contribution and the variant with the smallest, and compared the size of the exchange contribution across variants with the association constants. The residue-specific profiles were essentially identical at the two concentrations and the size of the contribution did not follow the association constants. They also argued that monomer-dimer exchange would be slower than what the dispersion showed; this was an argument, not a measurement, and it was presented as one. No extra species or state was added to the description.

**How they wrote it.** The dispersion was stated to report motion within the dimer, with the concentration series and the missing correlation as the basis. The monomer-dimer reading was reported as tested and not supported, and the description stayed a single species with internal exchange.
