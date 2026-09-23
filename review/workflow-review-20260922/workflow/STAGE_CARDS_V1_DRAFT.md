# Finding alternative APO states: stage cards, draft v1

Dynamics Atlas collects functionally relevant conformational states of all kinds. Alternative APO states are the first type we work on; other types, such as active versus inactive, will get their own definition card later. Stages 2 to 8 below are meant to carry over to those types; stage 1 and the definitions are specific to this first type.

Prepared for the 24 Sept meeting with Soojung and Gina · 2026-09-22 · built from nine papers

**Sources.** Gina's five papers (Kerns 2015 AdK, De Paula 2020 IL-2, Hansen 2023 K-Ras, Burmann 2012 and Cai 2025 RfaH) and four we added to cover other kinds of evidence (Fraser 2009 cyclophilin A, Bouvignies 2011 T4 lysozyme L99A, Spoerner 2001 H-Ras, Woodward 2025 IL-2 superkines). An item tagged with papers, for example [De Paula 2020; Woodward 2025], is something those papers actually do. Items tagged [ours] are our inference. The [evidence table](11_Workflow_evidence_table.md) lists the location of every item in every paper. Locations and numbers are still being checked against the originals.

**Gina, what we need most from you:** mark every place where these cards differ from how you actually work, especially the "When stuck, try" rows. Papers rarely write those steps down, and an agent needs them most.

## How the cards are used

A stage card describes one stage of the analysis. It lists the stage's goal, the inputs it needs, the routine moves, how to tell the stage is done, the signals that mean the analysis is stuck, and what scientists try when stuck, cheapest first, each with the explanation it rules out. It also records the weakest claim that can still be written down if nothing works, and the claim the stage can never support.

The agent sees one card at a time. The program around it checks the done criteria, gives the agent the extra analyses one at a time when it is stuck, and stops it from skipping stages or grading its own work. People decide the definitions, the evidence tiers and whether an entry is accepted.

## What changed from v0

- Draft v0 came from Gina's five papers. v1 adds four papers chosen for evidence the first five lack: visible two-peak exchange, crystallographic evidence, an excited-state structure validated by designed mutants, and NMR combined with MD.
- Card 4 now has an explicit fork for when a kinetic model fails to fit. Cai 2025 added hidden states one at a time; Spoerner 2001 read the failure as a different mechanism, because an independent structural fact explained it.
- Card 6 is reframed. The database agent does not run new simulations; it judges the structural and simulation evidence a paper reports, and "no simulation exists" is a valid outcome.
- The claim limit in card 5 now depends on validation. An inferred structure stays "consistent with", unless an independent experiment has confirmed the model, as in Bouvignies 2011.
- New definition questions: engineered variants, generic probe ligands, and states whose relevance is the loss of a binding ability.

## Branches by kind of evidence

The routine moves in stages 4 and 5 differ with the kind of evidence, so the cards branch.

| Kind of evidence | What stage 4 looks at | How stage 5 identifies the state | Papers |
|---|---|---|---|
| Two visible peaks (slow exchange) | Peak positions and intensities give the populations directly | Which peak grows or shrinks when mutants or partners are added | Spoerner 2001 (³¹P); Cai 2025 (states A and B); Burmann 2012 (E48S) |
| Invisible minor state (CPMG, CEST) | A global fit gives exchange rate, population and shift differences; signs need extra experiments | Signed shift differences against reference states; overlap with partner-perturbed residues; mutants that shift populations; shift-based structural models | De Paula 2020; Hansen 2023; Kerns 2015; Woodward 2025; Bouvignies 2011; Cai 2025 (hidden states) |
| Crystallographic evidence | Alternate conformations at room temperature or below the usual density threshold; missing density after ruling out crystal packing | The structure comes from the density itself; a mutant that shifts the equilibrium, checked by solution NMR such as J-couplings, links it to the solution state | Fraser 2009; Spoerner 2001 |
| Fast exchange, one averaged peak | Outside the current "slow motion" definition | Not applicable yet | Tang 2007 (reference only): apo maltose-binding protein, a ~5% partially closed state exchanging in ns–µs. A question for Gina |

## The eight stages

| Stage | Question | Done when |
|---|---|---|
| 1. Frame the question | Which protein, which states, "apo" relative to which ligand, and what hypothesis? | State pair, construct scope, reference ligand, source type and hypothesis are written down with locators |
| 2. Gather evidence | What measurements and structures exist? | Every item is listed with type, accession or locator, conditions, and whether it is public |
| 3. Check conditions | Which pieces can be compared? | Every pair to be compared is marked comparable, comparable with a caveat, or not comparable |
| 4. Is the exchange real? | Is the slow motion conformational exchange, not an artifact? | Exchange rate, population and residues are stated, or what the fit cannot determine is named, and at least one artifact is ruled out |
| 5. What is the alternative state? | Which known state does the minor state resemble? | Two independent lines of evidence point to the same reference, or the missing line is named |
| 6. Structure and simulation | What does the state look like, and how strong is the simulation evidence? | A mapped structure or "unmapped" plus residues; a verdict on simulations: samples the state, does not, cannot tell, or none exist |
| 7. Functional relevance | Does the state matter for binding or activity? | Relevance is stated with the experiment that shows it, or marked "proposed" |
| 8. Write the entry and review | Does the entry go in, and at which tier? | The entry passes checks and has a tier; a person has signed off where required |

## Card 1 · Frame the question

| Field | Content |
|---|---|
| Goal | Name the protein, the construct, the states, the ligand relative to which the protein counts as apo, and the hypothesis being tested |
| Inputs | Title, abstract and figure legends; or the BMRB or PDB entry metadata |
| Routine moves | Write down the state pair and the reference ligand. Classify the source: (a) the paper reports an alternative state, (b) the paper has NMR data but makes no state claim, (c) database data only [ours]. Record the hypothesis being tested, and at the end say whether it held [Woodward 2025] |
| Done when | State pair, construct scope, reference ligand, source type and hypothesis are recorded, each with a locator |
| Stuck signals | The protein is always nucleotide-bound [Hansen 2023; Spoerner 2001]. The "alternative" state was measured with substrate bound [Kerns 2015]. The state is seen only in an isolated domain [Burmann 2012; Cai 2025]. The state belongs to an engineered variant, not the wild type [Bouvignies 2011; Woodward 2025]. The reference ligand is a generic probe, not a physiological partner [Bouvignies 2011]. A contact-based explanation fails because the key residue does not touch the partner [Spoerner 2001] |
| When stuck, try | 1. Record "apo relative to <ligand>" explicitly (rules out a silent change of definition). 2. Scope the claim to the construct that was measured [Cai 2025]. 3. Check the definition: second visible peak, invisible CPMG or CEST state, or fast exchange with one peak? (rules out applying the wrong criterion). 4. Look for a study of the ligand-free, full-length, wild-type protein [ours]. 5. When a structural contact cannot explain an effect, reframe the question as one about dynamics [Spoerner 2001] |
| Fallback claim | "State pair identified; apo status relative to <ligand> needs a human decision" |
| Claim limit | A substrate-bound, isolated-domain or engineered-variant state is recorded with that scope, never as an apo state of the wild-type full-length protein |

## Card 2 · Gather evidence

| Field | Content |
|---|---|
| Goal | List every measurement and structure that bears on the state pair |
| Inputs | DOI, protein name, UniProt ID |
| Routine moves | Open-access full text and supplement; BMRB entries; PDB entries; author deposits such as Dryad, Figshare or Zenodo; existing MD. Search wide first and filter later, for example by comparing all deposited structures of the protein before anything else [Fraser 2009] |
| Done when | An evidence table exists with data type, accession or locator, conditions, and public / figure-only / missing for each item |
| Stuck signals | BMRB has the chemical-shift assignments but none of the exchange data [all papers checked]. The exchange data sit in a general repository instead [Hansen 2023, Dryad; Cai 2025, Figshare]. There is no BMRB entry at all and the shifts are only in the supplement [Bouvignies 2011]. MD trajectories are available only on request [Woodward 2025]. A PDB code printed in the paper resolves to an unrelated structure [Cai 2025 cites "6C6C"]. The BMRB citation still shows a pre-publication title [Kerns 2015, BMRB 19089]. Numbers exist only in figures |
| When stuck, try | 1. Read the data availability statement for author deposits (rules out "no data" when the data are simply outside BMRB). 2. Search BMRB by protein name and look for entries titled "minor state" or "excited state" [Cai 2025, BMRB 52719]. 3. Resolve a mismatched accession by title and method search. 4. Transcribe supplementary tables before digitizing figures, and flag digitized values [ours] |
| Fallback claim | "Evidence available only as values reported in the paper" |
| Claim limit | A missing deposit is not evidence against the state |

## Card 3 · Check conditions

| Field | Content |
|---|---|
| Goal | Decide which pieces of evidence can be compared directly |
| Inputs | The evidence table from card 2 |
| Routine moves | For each item record construct, species, mutations, bound nucleotide or ligand, temperature, pH, buffer, concentration and field strength [ours] |
| Done when | Every pair to be compared is marked comparable, comparable with a caveat, or not comparable, with the reason |
| Stuck signals | Crystal structures and NMR come from different species [Kerns 2015]. Measurements taken at different temperatures are put side by side [De Paula 2020; Hansen 2023; Spoerner 2001]. Papers often do this without comment [Spoerner 2001 compares 5, 10 and 37 °C]; the entry must still say so |
| When stuck, try | 1. Check whether the difference falls in the region the claim is about. 2. Ask whether the difference could change the claim; temperature, for example, shifts populations. 3. Attribute outlier residues to the condition difference and say so [De Paula 2020]. 4. When the paper transfers results across species or constructs, record its justification and how strong it is [Kerns 2015]. 5. If not comparable, split into separate entries |
| Fallback claim | "Conditions not comparable; recorded as separate entries" |
| Claim limit | Numbers from different conditions are never pooled without stating the difference |

## Card 4 · Is the exchange real?

| Field | Content |
|---|---|
| Goal | Decide whether the slow motion is conformational exchange of the protein |
| Inputs | Exchange data or reported fits: peak doubling or broadening, CPMG, CEST, R1ρ, ZZ-exchange; residue list |
| Routine moves | Detect two states directly as two resolved peaks when exchange is slow [Spoerner 2001; Cai 2025; Burmann 2012]. Fit many residues to one global exchange process [De Paula 2020; Hansen 2023; Cai 2025; Woodward 2025; Bouvignies 2011]. Cross-validate with a second method, such as CPMG against CEST, NMR against kinetics, or a crystal rotamer against solution J-couplings [De Paula 2020; Hansen 2023; Kerns 2015; Cai 2025; Fraser 2009]. Measure a control state where no exchange is expected [Hansen 2023]. Name a specific artifact or confound and test it directly, instead of listing it as a caveat [De Paula 2020, aggregation; Hansen 2023, hydrolysis; Spoerner 2001, Mg²⁺ binding] |
| Done when | Exchange is attributed to a global or local conformational process with rate, population and residues, or what the fit cannot determine is named; at least one artifact is ruled out |
| Stuck signals | Amide peaks broadened beyond detection [De Paula 2020]. Dispersion curves are flat [Kerns 2015]. Minor-state peaks too weak or overlapped [Cai 2025]. A kinetic model fits one experiment or variant but fails another [Cai 2025; Spoerner 2001]. Populations cannot be separated from the fit [Woodward 2025; De Paula 2020]. The sample changes chemically during measurement [Hansen 2023]. Harsh destabilization makes the protein precipitate [Burmann 2012]. A single peak cannot tell one fixed conformation from a fast-averaging ensemble [Spoerner 2001]. Data at a single field only [ours]. Doubled peaks next to prolines [ours] |
| When stuck, try | 1. Test the named confound directly (see routine moves). 2. Switch probe, for example from amides to methyls [De Paula 2020]. 3. Choose the temperature that brings the exchange into the window of the method being used, or vary it to tell slow from fast exchange [Kerns 2015; Bouvignies 2011; Fraser 2009]. 4. Assign weak minor-state peaks through exchange cross-peaks [Cai 2025]. 5. Use gentler perturbations, such as an interface mutant or a cleavable linker [Burmann 2012]. 6. **When a model fails new data, choose one of two routes.** Add one hidden state at a time, refit all data jointly and stop on goodness of fit [Cai 2025]; or, if an independent structural fact explains the failure, read it as a different mechanism [Spoerner 2001]. 7. Report only what the fit determines, for example the rate but not the population, and name the rest [Woodward 2025; De Paula 2020]. 8. Resolve a single-peak ambiguity with independent probes such as crystal disorder or generic flexibility mutants [Spoerner 2001]. 9. Use a different dynamics method when standard order parameters miss the motion [Hansen 2023]. 10. Report a bound, not a value, when the instrument or the fit limits the measurement [Kerns 2015; Fraser 2009, population bounded from line broadening]. 11. Check prolines next to doubled peaks and concentration dependence [ours] |
| Fallback claim | "Exchange observed at residues X; origin not established" |
| Claim limit | Exchange alone does not establish a functional state [ours] |

## Card 5 · What is the alternative state?

| Field | Content |
|---|---|
| Goal | Say which known state the minor state resembles, and why |
| Inputs | Exchanging residues and parameters from card 4; chemical-shift perturbations caused by partners or mutants; reference states (ligand-bound, other nucleotide, mutant, random coil); structures |
| Routine moves | Determine the sign of the shift differences before comparing them with references [Hansen 2023, from CEST; Bouvignies 2011, sign experiments]. Compare signed shift differences with those between reference states, region by region [Hansen 2023; Cai 2025]. Overlap the exchanging residues with the residues a binding partner perturbs [De Paula 2020]. Compare exchanging residues across variants of the same protein [Woodward 2025]. Read secondary structure from chemical shifts [Burmann 2012; Cai 2025; Hansen 2023]. Mutate a key contact; the exchange or the equilibrium should change [De Paula 2020; Woodward 2025; Spoerner 2001]. Add the binding partner to such a mutant and check that it restores the bound-like state [Spoerner 2001]. Repeat with a second, unrelated perturbation [De Paula 2020] |
| Done when | At least two independent lines of evidence point to the same reference state, or the missing line is named |
| Stuck signals | Chemical shifts alone cannot determine the structure [De Paula 2020; Hansen 2023]. Two metrics prefer different reference states [Hansen 2023, Switch I: R² favors the GDP state, RMSD favors random coil]. Several kinetic models fit equally well [Cai 2025]. No known structure matches the minor state [Bouvignies 2011] |
| When stuck, try | 1. Compare region by region (rules out a global correlation hiding local differences). 2. Try another reference state (rules out a wrong reference). 3. Look at outlier residues one by one for local chemistry [Hansen 2023, residues near the γ-phosphate]. 4. If a mutant fit does not converge, compare presence or absence of exchange [De Paula 2020]. 5. Build a structural model from the minor-state shifts, restricted to the regions that change, after checking the protocol on the ground state; label it a hypothesis [Bouvignies 2011; Cai 2025]. 6. Resolve an ambiguity in the model with an independent measurement on a mutant in which the minor state dominates [Bouvignies 2011]. 7. Report models the data cannot separate as unresolved [Cai 2025]. 8. Name the state by mapping to an earlier measurement of the same system [Hansen 2023] |
| Fallback claim | "Minor state resembles reference X in region Y", or "Structure unknown; differences localized to residues …" |
| Claim limit | Write "consistent with the perturbation pattern of X", never "the structure is X", unless an independent experiment has validated the model [Bouvignies 2011 calls its model "the structure" only after designed mutants and J-couplings confirmed it]. Some papers state identity more directly [Spoerner 2001]; entries keep the stricter wording |

## Card 6 · Structure and simulation

| Field | Content |
|---|---|
| Goal | Say what the alternative state looks like, and judge the structural and simulation evidence the paper reports. The database agent does not run new simulations |
| Inputs | The identity from card 5; PDB structures; simulations reported in the paper or deposited publicly |
| Routine moves | Map the states to PDB structures and compute the differences, with residue numbering aligned [De Paula 2020; Hansen 2023; Burmann 2012; Cai 2025]. If the paper ran MD, record the engine, length, sampling method and how it was compared with NMR [Woodward 2025; Kerns 2015]. Compare structural variability in MD with NMR exchange, residue by residue [Woodward 2025] |
| Done when | A mapped structure, or "unmapped" plus the residues involved; and a verdict on simulations: samples the state, does not, cannot tell, or none exist |
| Stuck signals | No deposited structure shows the state; frozen crystals can hide it [Fraser 2009]. MD shows only local motion or no transition [Kerns 2015; our HSP90 analysis]. The exchange is too slow for conventional MD [Hansen 2023]. MD and NMR probe different timescales and the paper does not reconcile them [Woodward 2025]. No simulation exists for this system [Spoerner 2001; De Paula 2020; Burmann 2012; Cai 2025]. Electron density is missing in the region of interest [Spoerner 2001] |
| When stuck, try | 1. Compare trajectory length with the exchange time before reading absence as evidence [ours]. 2. Fit a weighted ensemble of existing crystal structures to NMR order parameters [Hansen 2023]. 3. Read missing electron density as disorder only after ruling out crystal packing with lattice contacts and a control structure [Spoerner 2001]. 4. Look for room-temperature or multi-temperature crystal structures, and analyses of density below the usual modeling threshold [Fraser 2009]. Moves the paper itself may have made, which the agent records and weighs but does not repeat: 5. adaptive MD steered by the residues NMR flags [Woodward 2025]; 6. correlated-motion networks used to pick a residue to mutate [Woodward 2025]; 7. a designed mutation that stabilizes the minor state, then inverts the populations so it can be measured directly [Bouvignies 2011; Fraser 2009] |
| Fallback claim | "Existing simulations cannot test this state" or "no simulation exists" |
| Claim limit | An MD cluster selected with the same residues NMR flagged is weaker identity evidence than an independent structure [Woodward 2025]. A short simulation without a transition cannot refute the state [ours; Kerns 2015 and Hansen 2023 both decline to use MD as counter-evidence] |

## Card 7 · Functional relevance

| Field | Content |
|---|---|
| Goal | Decide whether the state matters for binding or activity |
| Inputs | Binding data, mutant activity, co-crystal structures, cellular or in vivo data |
| Routine moves | Determine which state the ligand or partner binds [Bouvignies 2011; Spoerner 2001; De Paula 2020]. Measure binding affinity for variants that shift the population [De Paula 2020; Woodward 2025; Bouvignies 2011]. Measure cellular signaling for those variants [De Paula 2020; Woodward 2025]. Link to phenotype with genetics or reporters [Burmann 2012]. Compare variant dynamics with activity rates from the literature [Hansen 2023] |
| Done when | Relevance is stated with the experiment that shows it, or marked "proposed" |
| Stuck signals | Relevance is only proposed, in wording such as "may be instrumental" [Hansen 2023]. An affinity cannot be measured with the standard assay or by NMR [Burmann 2012; Spoerner 2001] |
| When stuck, try | 1. When an affinity measurement runs out of range, switch readout instead of stopping: NMR peak integrals, then line broadening against ligand concentration [Spoerner 2001], or a functional phenotype [Burmann 2012]. 2. Use control mutations that change something else, such as stability or chemistry, to show the effect comes from the state; add an independent binding measurement to rule out binding [Woodward 2025, V84A; Fraser 2009, Arg55Lys]. 3. Prove that a state does not bind by fitting that rate and testing it against zero [Bouvignies 2011] |
| Fallback claim | "Functional relevance proposed by the authors, not directly tested" |
| Claim limit | A correlation between population and activity across variants does not show cause [Hansen 2023]. Losing a binding ability can be the relevance, not only gaining one [Bouvignies 2011] |

## Card 8 · Write the entry and review

| Field | Content |
|---|---|
| Goal | Decide whether the entry goes in, and at which tier |
| Inputs | The outputs of cards 1 to 7 |
| Routine moves | Fill in the entry and tag every field as from the paper, computed by us, or our inference. A program checks format, units, locators and claim limits. A reviewer agent checks for over-claiming. Stages Gina selects go to a person [ours]. Report null results and failed methods explicitly [Spoerner 2001] |
| Done when | The entry passes the checks and has a tier |
| Stuck signals | The reviewer rejects the entry. Two sources contradict each other |
| When stuck, try | Return to the stage that failed. Keep contradictory sources side by side for a person to decide |
| Fallback claim | Record the entry as a candidate |
| Claim limit | Only a person can mark an entry accepted |

## Draft entry format

| Field | What goes in |
|---|---|
| Protein | Name, species, UniProt |
| Construct and conditions | Mutations, labeling, bound nucleotide or cofactor, temperature, pH, buffer |
| Apo relative to | The ligand whose absence defines "apo" here |
| Major state | Description, population, matching structure |
| Alternative state | Description, population, matching structure or "unmapped" |
| Evidence type | Peak doubling, CPMG, CEST, R1ρ, ZZ-exchange, SAXS, alternate conformation in a crystal, MD |
| Exchange parameters | Exchange rate, minor-state population, range of chemical-shift differences |
| Residues | Residues or regions involved |
| Identity basis | Why the minor state is thought to resemble a known state |
| Functional relevance | Which ligand binds which state; activity changes |
| Cross-checks | Structures and MD; whether MD was too short to tell, or none exists |
| Tier | Strong, weak, candidate, or not included (see below) |
| Claim limit | What this entry cannot support |
| Provenance | Figure or table locators, BMRB, PDB, computation receipts |
| Review status | Pending review, reviewed by whom, accepted or returned |
| Workflow record | Stages passed, where it got stuck, which fallback claim was used |

Tiers follow Soojung's preference to search exhaustively and filter later, so uncertain entries are kept at a lower tier instead of dropped.

- **Strong.** The paper reports the alternative state, there are exchange data plus at least one independent line of support (mutant, ligand, second method or structure), and we have checked the numbers.
- **Weak.** Exchange evidence exists, but the identity, origin or functional link is missing one piece; the entry says which.
- **Candidate.** Only a lead, such as peak doubling alone or an author's suggestion; the entry says what to measure next.
- **Not included.** The state pair is not an apo state under the current definition (AdK in Kerns 2015, for example). The reason is recorded so the entry can be revisited if the definition changes.

## Template for recording a manual example

If Soojung and Gina record their hand-analyzed examples this way, each example maps directly onto the cards and can later serve as a reference answer.

```text
Protein / construct / conditions:
Apo relative to which ligand:
Data you looked at (accessions, figures, tables):

Conclusion: alternative apo state?  yes / no / unsure
  States, populations, exchange rate, residues:
  Why you think the minor state is what it is (evidence):
  Functional relevance, and how it was shown:

Stages you went through, in order (one line each, the routine move):

Where you got stuck, and what you did next (the most useful part for us):

What evidence would change your conclusion:
What you would want measured next:
Confidence (high / medium / low), and roughly how long it took:
```

We would also ask you to prepare at least five further examples that we never see: proteins outside the papers above, left out of the workflow report you share with us. They become the blind test set. One or two should be proteins with NMR data but no alternative state, so we can measure false positives.

## Questions for Gina

1. Does an alternative apo state include invisible minor states seen only by CPMG or CEST? What about fast exchange with a single averaged peak, such as the ~5% partially closed state of apo maltose-binding protein (Tang 2007)? Is there a lower limit on population or exchange rate?
2. Do these count: nucleotide-bound Ras, the isolated RfaH C-terminal domain, AdK lid motion measured with substrate bound, engineered variants (T4 lysozyme L99A, IL-2 superkines), and states defined relative to a generic probe such as benzene? What did you want the AdK 2015 paper to illustrate?
3. Which stages above differ from how you work? When you are stuck, what do you usually try first?
4. You mentioned that many papers report experiments that do not support their conclusions. Which mistakes are most common? We want them as stuck signals in card 4.
5. None of these papers put their exchange data in BMRB. Is that typical? What else in BMRB could point to an alternative state?
6. Which stages must a person review, and which can a reviewer agent check?
7. For Switch I in K-Ras, R² and RMSD prefer different references. Which would you trust, and why?
8. When a kinetic model fails to fit, when do you add hidden states (as in Cai 2025) and when do you read the failure as a different mechanism (as in Spoerner 2001)?
9. Papers often compare measurements taken at different temperatures without comment. Should an entry be downgraded for that?
10. After designed mutants confirm a structural model (Bouvignies 2011), may an entry call it "the structure"?
11. If a paper's exchange rate and population come from the authors' own earlier papers, as in Pontiggia 2015 (13,000 s⁻¹ and 15%, cited from their earlier NMR work), is the entry strong or weak? In our pilot the entries split three to one.
