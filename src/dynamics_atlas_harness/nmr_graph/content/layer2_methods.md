# Layer 2 — Method knowledge for stuck points

Each entry states when it applies and what is known. Entries are grouped by the situation you are in so they can be looked up; they are knowledge, not instructions, and they never replace the obligations in Layer 1.

## A. Before any fit

**A1. Conditions ledger.** Applies to every data set. Record species, construct (isolated domain versus full length), ligand, nucleotide or metal state, oligomeric state, concentration, temperature, field, labelling scheme and residue numbering. Data recorded under different conditions can be compared but not pooled without saying so; a rate taken from the literature is a different-condition data set until it has been remeasured under the NMR conditions, because buffer cations, pH, temperature and isotope labelling all move rates. Samples that turn over or decay (hydrolysis, product formation, precipitation) need a spectrum before and after the dynamics experiment, and interleaved acquisition so that drift does not masquerade as dispersion.

**A2. Forward model before comparison.** Applies whenever a model, structure or ensemble is compared with an observable. Each observable has its own averaging (a time window, a distance power law, population weighting) and its own contaminants (transverse rates contain exchange and saturation-transfer terms; proton CEST carries cross-relaxation dips). Compare in observable space after the forward model has been applied; a mismatch seen before that step is not yet a discrepancy.

**A3. Resolvability statement.** Applies when a data set is about to be used as a test of a claim. Write what kinds of difference it can distinguish (a population change, an extra sparse state, the sign of a shift difference, correlation between motions) and what it cannot. The outcome of a test that could not have separated the candidates is not evidence either way.

**A4. Inclusion rules and residue groups.** Applies to any multi-residue or global fit. State the criterion for entering a residue or curve and list what was left out. Compare per-residue against grouped fits: residues that return different rates or populations under the same model may report different processes and must not be forced into one fit; two groups of which only one tracks a functional shift set (ligand binding, a known state) are two processes, and only the relevant one belongs in the mechanism.

## B. Missing or flat signal

**B1. A flat dispersion curve has three readings.** No exchange; exchange slower than the window, so the exchange contribution is too small to see; exchange faster than the window with a small shift difference. One temperature at one field cannot separate them. Temperature dependence of the exchange contribution separates slow from fast exchange (it rises with temperature in slow exchange, where it approaches the leaving rate, and falls in fast exchange); field dependence adds a second handle. Applies when the same residues are followed and buffer and aggregation state are unchanged. The absence of a second peak set does not exclude slow exchange, because minor-state peaks can sit below detection from low population or from broadening by a fast return rate; that is an expected outcome, not evidence against the state.

**B2. Missing or broadened peaks are exchange clues only in a sample shown to be monomeric and stable.** Aggregation, oligomerisation and decay produce the same appearance; size-exclusion with light scattering, diffusion, or concentration dependence of the relaxation rates settle the sample state first.

**B3. Loss of dispersion after a perturbation is qualitative.** Applies to mutations, ligands, cofactor changes and partner swaps. Lost dispersion cannot by itself separate a lower minor population, a rate moved out of the window, and a smaller shift difference. Convergent loss at a second probe or nucleus supports loss of exchange; the alternatives are stated, not dismissed.

## C. One data type: poor fits and degenerate parameters

**C1. Parameter coupling in fast exchange.** In CPMG data near the fast limit, population and shift difference enter together and only their product is well determined; rate and population are poorly determined from featureless curves. A second nucleus with structured curves, a second field, or a technique in another window breaks the coupling. Applies whenever curves lack curvature.

**C2. Sign of the shift difference.** CPMG returns only the magnitude; the sign comes from CEST, from comparing HSQC with HMQC peak positions, or from the temperature dependence of the observed shift. A sign constraint derived while the fit sits in a wrong solution carries that error into everything built on it, including the apparent identity of the minor state.

**C3. Equal intrinsic transverse rates for all states is a starting assumption, not a measurement.** A freed minor-state rate that comes out far above what molecular size predicts, and clusters in one region, is a signature of exchange with a further state that the fit has absorbed; it is not an intrinsic property to report as such. Synthetic data generated from a more complex scheme and fitted with the simpler one show what this signature looks like for the case at hand.

**C4. Map the chi-squared surface before trusting a free multi-parameter fit.** Grid or profile scans reveal shallow directions and multiple minima; a surface without a clear minimum means the parameter is not determined, and no value is reported for it. Fix what independent data fix (a separate ligand-free fit, a binding constant, a thermodynamic cycle) rather than letting everything float, and say which fixed values are assumptions. Joint multi-state fits started from generic values often settle into local solutions with similar chi-squared and different physics; restart from the per-type solutions, scan starting values for weakly determined parameters, and report the family of solutions rather than one point. Uncertainties come from resampling (bootstrap, Monte Carlo, jackknife) or from repeat measurements, and a parameter at a bound is reported as at-bound.

## D. Two data types disagree

**D1. Techniques cover different exchange windows.** CPMG and on-resonance rotating-frame relaxation are most sensitive to exchange on roughly the hundreds-to-few-thousand per second scale; CEST and off-resonance rotating-frame methods reach slower exchange (roughly tens to hundreds per second) and lower populations, and need more than one saturation field for reliable parameters, but miss fast processes with small shift differences; real-time spectra cover seconds to hours. A process seen by one technique can be invisible to the other, or absorbed into a state the other does see. Single-type fits of a multi-process system return biased parameters even when they converge; the bias appears as rates and populations that differ between types for the same residues.

**D2. Before calling two data types contradictory, forward-simulate the second experiment from the first's parameters** with the matching field, pulse timing and relaxation delays, and fit the synthetic data with the simpler model. Agreement shows compatibility; a structured mismatch across many probes is the signature of a missing state or process, not of noise.

**D3. Consistency across probes as evidence.** Independently fitted rates and populations that agree across unrelated probes, nuclei or techniques are evidence for one concerted process, and this consistency can break a topology tie that chi-squared cannot.

## E. Number of states and topology

**E1. Add states one at a time and test every plausible attachment** (to the ground state, to a known minor state, on the path, branched). Compare fits with a criterion that penalises parameters and inspect residual structure, not only chi-squared; stop at the simplest model without systematic residuals.

**E2. Some topologies are statistically indistinguishable** (linear versus branched, alternative connections of minor states). A link between two sparsely populated states is generally unobservable: the data neither require nor exclude it. In these cases report the alternatives, carry forward only the quantities identical under all acceptable models, and label any preference with its external basis (simulation, structure, a consistency argument).

**E3. Shifts of a state with no visible peak are outputs of the chosen scheme.** Their robustness is tested by changing the populations in a predictable way (co-solvent, temperature, pressure, denaturant, mutant), predicting the profile changes from the fitted shifts, and refitting to see whether the shifts move.

## F. Is the exchange real, and what process is it?

**F1. Self-association.** Applies at high protein concentration or for known oligomers. Repeat at a substantially lower concentration; unchanged profiles and parameters argue for intrinsic exchange, and the size of the exchange contribution should not track the association constant across variants.

**F2. A suspect species in the sample** (residual ligand after affinity purification, a dissociated complex, free versus partner-bound protein, a slowly formed product). Back-calculate the expected population of the suspect from known affinities, rates and concentrations and compare it with the fitted minor population; test dependence on the suspect's concentration; compare the fitted exchange rate with the independently measured off-rate. A population far above the expectation, or a rate orders of magnitude away from the off-rate, excludes the suspect; a single control narrows the alternatives without eliminating every handling artefact, and that residue of doubt is written down.

**F3. A mutant phenotype can act through stability, an interface, solubility or aggregation rather than through dynamics.** Structural modelling of the mutant, interface analysis, or measurements under conditions that change the suspected route are checked before a dynamics explanation is accepted; the dynamics-stability correlation is not extended to a variant that does not fit it.

**F4. Assigning an exchange process to a functional step** needs an independently measured rate for that step under matched conditions, and agreement under more than one perturbation (ligand, metal, mutation). Residue location near an active site is suggestive, not sufficient. A timescale mismatch between the process and the function downgrades the link to a hypothesis.

## G. What does the minor state look like?

**G1. Multi-reference, region-by-region comparison.** Compare signed shift differences against several candidate references on the same residue subset: known alternative states, sequence-predicted random coil, locked mutants, shifts predicted from candidate structure models by more than one predictor. Compare globally and by region; the two can disagree, and correlation and RMSD can favour different references. Report both. Residues that deviate most from an otherwise good match may sit next to a chemically different group in the compared states; check proximity before reading a local conformational change.

**G2. Compactness and exposure of a state seen only through exchange.** Denaturant dependence of populations and rates gives m-values; hydrogen-exchange protection factors give an upper bound on how much of the population can be unfolded; solvent paramagnetic relaxation gives exposure; pressure dependence gives volume. These report compactness or exposure, not a structure. Residual dipolar couplings discriminate candidate conformers more strongly than shifts when the state of interest dominates the population, with a control on a state of known structure to calibrate the comparison.

**G3. Structures built only from shifts** (homology, shift-driven modelling, predicted models) are hypotheses about a population-averaged state. A contact or NOE that exists in only one candidate model is the kind of evidence that promotes one of them.

## H. Mechanism: conformational selection, induced fit, pathways

**H1. A pre-existing bound-like minor state is necessary, not sufficient, for conformational selection;** neither the population of that state nor its affinity decides the pathway. A slow motion of the right timescale is likewise a candidate, not the selected mode; locking mutants that shift the candidate equilibrium test it through the affinity they leave behind.

**H2. Concentration dependence of the exchange rate during a titration discriminates mechanisms.** Applies in fast exchange with sub-stoichiometric partner. A rate that decreases with partner concentration supports conformational selection when excitation is slower than unbinding; a rate that increases supports induced fit or plain two-state binding.

**H3. With a fitted multi-state scheme, the dominant pathway is the one carrying the net flux at the working concentration,** computed from the rate constants; the balance can switch with concentration, and a higher-affinity route can carry little flux. The same decomposition separates an intrinsic from an allosteric contribution to a rate when a variant has both a different population and a different intrinsic step.

**H4. On-pathway versus off-pathway.** A perturbation that acts on only one state (an enzyme, a specific binder) changes the overall interconversion rate only if that state lies on the path; which state the perturbation binds is tested separately.

## I. Perturbations and controls

**I1. Predict before you perturb.** Write the expected effect of a mutation, ligand, co-solvent or temperature change on rates, populations and shifts before measuring, and state afterwards whether it was met. A chemically unrelated second perturbation reproducing the same qualitative effect strengthens a single-equilibrium reading.

**I2. A perturbation that co-varies with a structural change** (a mutation at an interface, a ligand that reshapes its pocket, a variant that changes the monomer fraction) confounds the reading. An outlier from an otherwise consistent series is reported separately with its candidate causes, and the correlation is stated for the members it holds for.

## J. Reporting

**J1. Scope.** Conclusions belong to the construct, species, ligand state and condition measured; extension to another construct or species needs equivalence evidence, and conclusions drawn from a variant are marked as drawn from the variant.

**J2. Unresolved is a result.** "Not determinable from these data", "two topologies not distinguished", "one control excludes this artefact but not every one" are written with the analysis or measurement that would resolve them, not replaced by the more convenient option.
