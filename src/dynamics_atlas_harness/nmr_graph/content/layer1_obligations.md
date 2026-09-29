# Layer 1 — Obligations

These are process obligations. They say what must be done and recorded, not what the answer is. They apply to every analysis of protein-dynamics data, whatever the system or technique. The reviewer (Layer 4) checks only these.

**O1. Fit each data type on its own before any joint fit, and keep the per-type results in the record.**
Each experiment type (for example CPMG, CEST, zz-exchange, real-time spectra, relaxation rates, a second nucleus) is fitted separately and its parameters are reported alongside any joint result. A joint fit may be the final result, but never the only one.

**O2. When two data types are claimed to report the same process, check them against each other and state the outcome as a number.**
Either use the parameters from one type to predict or constrain the other, or place the independently fitted parameters side by side; in both cases record how well they agree. A failed comparison is a discrepancy to be handled under O4. It is not, by itself, a verdict on either data set, on the model, or on the analysis, because the two types may cover different exchange windows.

**O3. Every fit that was run is reported; withdrawing a fitted result needs a stated reason and an analysis that tests that reason.**
A result may be set aside only after a check that could have shown the reason to be wrong (a control, a simulation, a comparison with an independent measurement, a refit under changed constraints). Without such a check the result stays in the record as unresolved, with the untested reason attached to it.

**O4. After any alarm, list at least two candidate causes and run an analysis that separates them; mark which causes were tested and which were only listed.**
Alarms include a poor fit, disagreement between data types or between probes, an outlier, a flat profile where exchange was expected, a parameter at a bound, a value outside what the method can deliver, and a conflict with prior work. Plausibility ranks candidates; it does not settle them.

**O5. Label every conclusion with its evidence level, and carry the label into the summary.**
Three levels: directly observed; conditional on a stated model or assumption; hypothesis (from literature, simulation, modelling, or analogy). When several models fit equally well, the findings are the quantities that agree across all of them; any preference among the models is reported as a labelled judgement together with its basis.

**O6. An identity for a minor state, or a function for an exchange process, needs a second independent line of evidence; with one line only, it is a hypothesis and the discriminating measurement is named.**
Independent means a different technique, nucleus, observable, control, or perturbation, not a refit of the same data. Agreement of independently obtained rates or shifts across probes counts as a second line; a good fit does not.

**O7. Keep an inventory: what data entered each fit, what was excluded and why, under what conditions each data set was recorded, and which control or perturbed samples exist in the data set.**
Mismatched conditions (temperature, buffer, construct, ligand or metal state, labelling, concentration) are flagged before data are combined. Any control or perturbed sample present in the data set is analysed with the same pipeline and its result reported, whether or not it supports the conclusion.
