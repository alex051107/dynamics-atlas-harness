# Dynamics Atlas

**Purpose.** Given a protein-dynamics dataset (MD trajectories, NMR, SAXS, FRET), which ensemble quantities can be trusted, and on what evidence? The project answers this in two parts: the science, case by case, with every number traceable to a data file in this repository; and a reusable workflow in which an AI analyst does part of the analysis under explicit rules, with each use of the rules tested against the same setting without them.

Zhenpeng Liu · UNC · September 2026 · last updated 11 September

**New on 11 September.** The rules were turned from text into fixed analysis operators that the AI must call ([section 8](#8-11-september-rules-turned-into-analysis-operators)). This made the AI's numbers checkable: comparing each number with the operator result it should come from caught 6 of 7 known numerical errors, where the earlier check caught none. It did not make the science right: two operators rest on a wrong reference definition, and the comparison with free analysis was confounded. The open questions ([section 9](#9-open-questions)) now include how the HSP90 reference states should be defined.

| Start here | Contents |
|---|---|
| This page | The problem, the approach, the workflow, the results and the open questions, in about ten minutes |
| [RESULTS.md](RESULTS.md) | The four cases one by one: the authors' claim, what we tested, what we found, what it can and cannot support |
| [data/](data/) | The tables behind every number, with a [data guide](data/README.md) |
| [slides/](slides/) | 13 slides plus appendix, with notes. Open `reader.html` in a browser to see each slide with its notes. As of 10 September; section 8 is not yet in the slides |
| [SOURCES.md](SOURCES.md) | The papers and deposited data |

## 1. The scientific problem

Different experiments and simulations see different aspects of the same protein ensemble. MD gives trajectories frame by frame. NMR gives distance restraints, averaged with a strong weight on short distances, and exchange on particular time scales. SAXS gives a scattering profile averaged over every molecule in the sample. FRET gives an efficiency that depends on where the dyes sit and how they move.

Putting these side by side is easy. The hard part is saying what they support together without over-reading any of them:

- Are two results about the same physical quantity?
- Does a result support only a change in structure, or also a population, or a rate?
- What cannot be distinguished with the data at hand?

## 2. The starting hypothesis

Our first hypothesis was that cautions from the methods literature could help an AI analyst do three things: choose the analyses a kind of data needs, notice when evidence is missing, and avoid conclusions the data do not support. We read 11 methods papers and wrote 33 candidate rules, meant to sit in the middle of the workflow:

```text
scientific question → rules → the AI analyst chooses and checks the analysis → calculation → bounded answer
```

## 3. What the Rules Table contains

Every rule has four parts: what the source paper showed, what is to be checked before using that kind of data, where the analysis should stop if the check cannot be made, and how far the lesson carries. For testing, the 33 rules were grouped by the job they do. The full table is in [data/rules/](data/rules/RULES_TABLE.md).

| Group | Rules | What they cover | A real example (source paper) | How it reached the AI in the tests |
|---|---:|---|---|---|
| Framing the question | 6 | claim level; when two measurements are not the same quantity; identifiability | A SAXS radius of gyration and an smFRET dye distance are different observables; matching the system does not make them directly comparable (Fuertes 2017) | sub-questions written by a person |
| Checking the data | 10 | what is measured; calibration; uncertainty; source quality; controls | FRET distance uncertainty must include corrections, R0 and dye motion, not only the spread of the histogram (Hellenkamp 2018) | a warning file placed with the data |
| Method guidance | 11 | forward models; reweighting; combining data; artifacts | Maximum-entropy reweighting combines sources while limiting departure from the MD prior; it does not discover states or rates (Bengtsen 2020) | rule text or short cards added to the question |
| Limits on the conclusion | 6 | fit is not validation; agreement is not proof; missing states | If the candidate structures omit a state, Bayesian SAXS refinement cannot create it (Shevchuk 2017) | one automatic check after the answer |

The 11 source papers are mostly about FRET, SAXS and cryo-EM; none is about MD-only analysis or the proteins studied here. The rules are written as general checklists for a kind of data, not as conditions attached to a specific calculation. No rule has been reviewed by a domain expert.

## 4. The workflow a new system goes through

| | 1 Choose the question | 2 Prepare the data | 3 Frame the question | 4 Analysis | 5 Check the answer | 6 Report |
|---|---|---|---|---|---|---|
| **What happens** | paper, SI, deposited data; the scientific question | per-frame tables, field definitions, physical checks | which difference to resolve; sub-questions; what a correct answer contains | the AI analyst reads the data and paper, writes and runs code, answers | automatic checks; one chance to revise | numbers linked to sources; limits stated |
| **Done by** | person | person + code | person | AI analyst | code | person |
| **Rules entered as** | — | a warning file (data-check rules) | sub-questions (framing rules) | text or cards (method rules) | one check (limit rules) | — |
| **Problems met** | HSP90: first question asked only about direction | DHFR: periodic-image error; ADK: our own check was wrong | none; this helped | FRET conditions applied to an NMR question | tested that a number appears, not that it is right | — |

Two of the problems appeared before the analysis started, where no rule acted.

## 5. The four cases

Each case starts from the authors' claim and tests one reading of their deposited data. Details and figures are in [RESULTS.md](RESULTS.md); the tables are in [data/](data/).

| Case | Authors' claim | What we tested | What we found | Data |
|---|---|---|---|---|
| HSP90 · [Henot 2022](https://doi.org/10.1038/s41467-022-35399-8) | The closed state of the N-terminal domain is transiently populated; about 9 of 20 closed-start runs move toward open | Does a run moving toward the open state also agree with the open-state NOEs? | 10 of 20 move toward open; at 1 Å, 9 of these stay far from both references and none agrees. Direction of change is not agreement with a state | [data/hsp90](data/hsp90/) |
| Nanodisc · [Bengtsen 2020](https://doi.org/10.7554/eLife.56518) | Reweighting MD against NMR, SAXS and SANS together fits all of them | Does fitting SAXS alone also improve NOE agreement? | SAXS disagreement −88 %; amide and methyl NOE +3 % and +15 %. One observable cannot stand in for another | [data/nanodisc](data/nanodisc/) |
| DHFR · [Cetin 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10428214/) | 4′-DTMP restores inhibition of L28R and sits closer to M20 and R28 | Do the deposited runs reproduce those contacts? | Yes, after correcting a periodic-image error in our own input that the AI accepted: M20 distance 8.69 → 4.62 Å (WT), 10.44 → 4.81 Å (L28R) | [data/dhfr](data/dhfr/) |
| ADK · [Orädd 2021](https://doi.org/10.1126/sciadv.abi5514) | ATP triggers partial joint closure of LID and NMP over ~4.3 ms | What can the deposited ligand-free MD say about closure? | Little: no net closure, and the conditions differ. A general distance check written after DHFR was wrong here | [data/adk](data/adk/) |

## 6. Tests of the rules

Each group of rules was tested at its stage against the same setting without it: same model, four runs each, answers scored against what the paper supports without knowing which version produced them. Every score is in [data/rules_test/](data/rules_test/).

| Kind of help | What we asked | What we saw |
|---|---|---|
| Framing: split the question into sub-questions | Does it reduce missed content? | More complete answers on both questions; not more accurate everywhere |
| Data check: a warning file about bad input | Does the AI notice and change its answer? | Listed in all 4 runs, opened in none |
| Method guidance: rule text or short cards | Better than a short protocol? | Better on the nanodisc, worse on HSP90 |
| Limits: one automatic check after answering | Does it correct scientific errors? | Did not reduce errors |

There was no stable benefit from putting the current rules into the AI's workflow, and the failures had different causes:

- **Rule content.** A correct FRET rule about dye models was applied to an NMR question, because rules were selected by the type of data, not by the calculation.
- **Delivery.** The data warning existed but never reached the analysis.
- **Checking.** The automatic check asked whether a number appears in the output, not whether it is right.

The most serious errors happened before any rule could act: in data preparation (DHFR) and in how the question was framed (HSP90).

## 7. What changed

The rules used to be the centre:

```text
rules → organize the analysis → the AI follows the rules
```

The scientific distinction now comes first, with the rules as supporting knowledge at the step where they apply:

```text
what difference must be resolved (structure, population, rate)?
  → what does each measurement actually observe?
  → the right physical and statistical analysis
  → which alternatives remain distinguishable?
  → bounded answer
```

This follows the argument of Li, Thomasen and Cossio in *Are we capturing the ensemble?*: first ask which difference between ensembles a measurement can still distinguish after processing, then choose the method.

## 8. 11 September: rules turned into analysis operators

The tests in section 6 delivered rules as text or as files that the AI could read or ignore. On 11 September we tried the form agreed in August: turn the analyses a question needs into fixed operators, and put the rules inside them.

An operator is a small fixed program with a card. The card states what the operator answers, which inputs it reads, which parameter values are allowed, what must hold before it runs, and the strongest statement its result supports. A rule now enters as one of those preconditions or limits; for example, the NOE operator refuses the pseudo-distance column that an earlier analysis had mixed up with the violation column. For HSP90 we wrote six:

| Operator | Answers | Status |
|---|---|---|
| OP1 direction runs | which sustained direction each run takes first, and whether it later reverses | reproduces the earlier counts exactly (10 of 20; 5 / 4 / 1) |
| OP2 NOE reference crosswalk | how many open-direction points agree with the open-state NOE references | reproduces 0 / 1 / 9, and 18 of 20 open-start runs, at 1 Å |
| OP3 state fractions over time | whether the open / closed / other fractions settle | criterion (window against full run, difference below 0.05) is not calibrated; no run ever returns, so no population can be stated |
| OP4 persistent changes | how many changes and returns | counts the same 5 events as OP1; not an independent result |
| OP5 excursions | stretches outside both NMR references | fails a basic control (below) |
| OP6 reference neighbourhoods | share of frames near the open reference, the closed one, both, or neither | fails a basic control (below) |

The AI now reports calculated numbers only by calling an operator. Each number carries the id of the result it came from, and an answer with a missing operator or an unbound number is sent back once. A fixed pipeline runs the six operators without any AI and produces a table of which quantities can be trusted ([data/operators/](data/operators/)).

**What held.** Numbers became checkable. On the eight earlier AI answers, the old check (does the number appear anywhere in the tool output?) caught 0 of 7 numerical errors. Comparing each number with the operator result it claims to come from caught 6 of 7, with no false alarm on 7 correct statements. The seventh, a wrong NOE bound array in the nanodisc case, has no operator to check against. All eight operator-bound AI runs called the required operators and bound every calculated number.

**What did not.** The comparison with free analysis does not measure what the operators add. Free-analysis answers scored 58 % (HSP90) and 74 % (ADK) of rubric points, against 98 % and 100 % for operator-bound answers, but 7 of the 8 free-analysis answers state that they could not read the question files and give no numbers: limits on tool calls and read length, added to stop runs from exhausting their token budget, cut them off. Two of the six scoring dimensions (operator coverage, numerical binding) also favour the operator arm by construction, and there was one scorer.

Two operators rest on a wrong definition. The open-start runs agree with the open NOE references in 18 of 20 cases, yet OP6 places 99.99 % of their frames outside the open reference. The radius it uses, the spread of the NMR models around their median (1.35 Å for the open ensemble), is compared with the distance from each MD frame to the nearest NMR model; ordinary thermal motion exceeds it. OP5 uses the same radius and marks almost whole runs as excursions. Rows for OP5 and OP6 are withdrawn from the trust table until the definition is redone and passes this control.

**What it means.** Putting rules inside operators solved the delivery problem for numbers. It does not make the science right: an operator executes a wrong definition as reliably as a right one. The weak point is now the scientific definitions inside the operators (state boundaries, reference geometry, convergence criteria), which no domain expert has reviewed. The table even contains the relevant lesson, that quantities with different spatial support cannot be compared directly (C005-RULE-001), but it was not applied to our own definitions. An external review of this round (ChatGPT Pro, 11 September) reached the same conclusions on the comparison and on OP3 to OP6.

## 9. Open questions

### 1. Are the rules themselves not good enough, or is the design around them wrong?

Adding rules did not make the answers better. Two explanations fit the evidence. Up to 10 September our data could not separate them; the operator round fixed the delivery side for numbers, and what remained wrong was in the definitions, which points toward A.

| A. The rules are not good enough | B. The design around them is wrong |
|---|---|
| The sources are mostly FRET, SAXS and cryo-EM; nothing covers MD-only analysis | Correct rules still failed: text the AI may ignore, a warning it never opened, a check that tested the wrong thing |
| They are written as checklists for a kind of data, not as conditions on a specific calculation | The worst errors came in data preparation and framing, where no rule acted |
| No rule has been reviewed by a domain expert, and one check we wrote was wrong | The only use that helped was done by a person |
| **If so:** better rules, from sources that match these systems, tied to specific calculations, reviewed by an expert | **If so:** change where and how knowledge enters the workflow; better rules alone will not help much |

Which explanation dominates, judged from the rules in [data/rules/](data/rules/RULES_TABLE.md) and the four cases? Are these the right kind of rules for systems like HSP90, and what is missing?

### 2. If the rules are kept, in what form and at which stage should they support the analysis?

| Stage | Rules could act as | What we saw |
|---|---|---|
| 2 Prepare the data | checks written as code for the specific quantity | essential, but must fit the quantity (DHFR, ADK) |
| 3 Frame the question | a template: which difference to resolve, what each measurement can say | helped, when written by a person |
| 4 Analysis | (a) text the AI reads; (b) operators with built-in preconditions that the AI must call | (a) no stable gain; (b) tested on 11 September: numbers became checkable, and the result is only as good as the operator's definition (section 8) |
| 5 Check the answer | limits on what may be claimed, checked by code or by a person | checking whether a number appears anywhere failed; checking it against the operator result caught 6 of 7 past errors |
| Outside the workflow | a reviewed reference for people | not tested |

### 3. How should the HSP90 reference states be defined?

Every trust judgment for HSP90 depends on definitions we chose ourselves: agreement with the open state (0.5, 1 or 2 Å on the mean NOE violation; between 0 and 3 of the 10 runs agree over that range), the size of the neighbourhood around each NMR ensemble, which atoms and which alignment are used, and when a state fraction counts as settled. Section 8 shows that a wrong choice is executed as faithfully as a right one. Which definitions are standard for this system, and what positive control should each pass before its result is used? One we now require: the open-start runs must mostly fall inside the open-state neighbourhood.

## Limits

Four AI runs per condition, compared by medians. Three of the four cases were used while the rules were being developed; ADK was new to them. The corrected DHFR distances and the ADK and nanodisc analyses are our own calculations, not AI results. The results support a decision about what to build next, not an accuracy rate. The 11 September comparison had one scorer, a free-analysis arm cut short by tool limits, and runs spanning several revisions of the runtime; it supports the checkability result, not an effect size.

## About this repository

This branch contains only the final results, the data behind them, and the slides. The analysis code, every AI run with its logs, and the development history are on the branch [`feature/luna-runtime-v1`](https://github.com/alex051107/dynamics-atlas-harness/tree/feature/luna-runtime-v1/review); the platform code is on `main`. The operator round of 11 September, with code, every run, scoring and the external review, is on [`feature/operator-plan-review-20260911`](https://github.com/alex051107/dynamics-atlas-harness/tree/feature/operator-plan-review-20260911/review/operator-plan-20260911).
