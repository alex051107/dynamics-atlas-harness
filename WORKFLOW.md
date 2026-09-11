# How the project got here

Updated 11 September 2026. The starting idea, the Rules Table, the workflow a new system goes through, and the tests of the rules on 10 and 11 September. The front page ([README.md](README.md)) says where this leaves us; [DEFINITIONS.md](DEFINITIONS.md) lists the definitions under review as of 11 September 2026.

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

Every rule in [version 1](data/rules/RULES_TABLE.md) has four parts: what the source paper showed, what is to be checked before using that kind of data, where the analysis should stop if the check cannot be made, and how far the lesson carries. For testing, the 33 rules were grouped by the job they do. [Version 2](data/rules/RULES_TABLE_V2.md), written on 11 September, routes each rule to the analysis it governs.

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

## 6. Tests of the rules (10 September)

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

As of 11 September 2026, the scientific distinction comes first, with the rules as supporting knowledge at the step where they apply:

```text
what difference must be resolved (structure, population, rate)?
  → what does each measurement actually observe?
  → the right physical and statistical analysis
  → which alternatives remain distinguishable?
  → bounded answer
```

This follows the argument of Li, Thomasen and Cossio in *Are we capturing the ensemble?*: first ask which difference between ensembles a measurement can still distinguish after processing, then choose the method.

## 8. Rules inside analysis operators (11 September)

On 11 September we tried the form agreed in August: turn the analyses a question needs into fixed operators and put the rules inside them. An operator is a small fixed program with a card that states what it answers, which inputs it reads, which parameter values are allowed, what must hold before it runs, and the strongest statement its result supports. The AI reports calculated numbers only by calling an operator, each number carries the id of the result it came from, and an answer with a missing operator or an unbound number is sent back once. A fixed pipeline runs the operators without any AI and produces the HSP90 trust table.

**What held.** Numbers became checkable. On eight earlier AI answers, the old check (does the number appear anywhere in the tool output?) caught 0 of 7 numerical errors; comparing each number with the operator result it claims to come from caught 6 of 7, with no false alarm on 7 correct statements. All eight operator-bound AI runs called the required operators and bound every calculated number.

**What did not.** Free-analysis answers scored 58 % (HSP90) and 74 % (ADK) against 98 % and 100 % for operator-bound answers, but 7 of the 8 free-analysis answers state that they could not read the question files and give no numbers. Limits on tool calls and read length, added to stop runs from exhausting their token budget, cut them off. Two of the six scoring dimensions (operator coverage, numerical binding) favour the operator arm by construction, and there was one scorer. Two operators rest on a wrong reference definition, and the scoring key built from the same definitions gave all four operator-bound answers full marks on that unit. Details and the definitions are in [RESULTS.md](RESULTS.md#rules-as-operators-11-september) and [DEFINITIONS.md](DEFINITIONS.md).

## 9. Two design questions from 10 September

### Are the rules themselves not good enough, or is the design around them wrong?

| A. The rules are not good enough | B. The design around them is wrong |
|---|---|
| The sources are mostly FRET, SAXS and cryo-EM; nothing covers MD-only analysis | Correct rules still failed: text the AI may ignore, a warning it never opened, a check that tested the wrong thing |
| They are written as checklists for a kind of data, not as conditions on a specific calculation | The worst errors came in data preparation and framing, where no rule acted |
| No rule has been reviewed by a domain expert, and one check we wrote was wrong | The only use that helped was done by a person |

The operator round fixed the delivery side for numbers, and what remained wrong was in the definitions. Version 2 of the table shows that none of the 33 original rules gives a criterion for the MD questions HSP90 needed. Both point toward A.

### If the rules are kept, in what form and at which stage should they support the analysis?

| Stage | Rules could act as | What we saw |
|---|---|---|
| 2 Prepare the data | checks written as code for the specific quantity | essential, but must fit the quantity (DHFR, ADK) |
| 3 Frame the question | a template: which difference to resolve, what each measurement can say | helped, when written by a person |
| 4 Analysis | (a) text the AI reads; (b) operators with built-in preconditions that the AI must call | (a) no stable gain; (b) numbers became checkable, and the result is only as good as the operator's definition |
| 5 Check the answer | limits on what may be claimed, checked by code or by a person | checking whether a number appears anywhere failed; checking it against the operator result caught 6 of 7 past errors |
| Outside the workflow | a reviewed reference for people | not tested |
