# Dynamics Atlas

Updated 11 September 2026 · Zhenpeng Liu · UNC

## What we are trying to do

Given a protein-dynamics dataset (MD trajectories, plus NMR, SAXS or FRET where they exist), which quantities about the ensemble can be trusted, and on what evidence? That was the question we settled on in July. The answer should come in two forms: a table, per dataset, of trusted and untrusted quantities with the evidence behind each; and a workflow that produces such a table for a new dataset, with an AI analyst doing part of the work under explicit rules.

The rules were the starting idea. We took 33 cautions from 11 methods papers, expecting them to steer the AI toward the right analyses and away from over-reading the data. This page says what happened when we tested that, where we now think the rules belong, and what we would like a second opinion on.

## Where things stand

| | Status on 11 September |
|---|---|
| Four cases (HSP90, nanodisc, DHFR, ADK) | Each has a bounded result from the authors' deposited data ([RESULTS.md](RESULTS.md)) |
| Rules given to the AI as text (10 September) | No stable gain; one harm, when a FRET rule was applied to an NMR question |
| Rules built into fixed analysis steps (11 September) | The AI's numbers became checkable: 6 of 7 known numerical errors caught, against none with the earlier check |
| The definitions inside those steps | Two failed a basic control. They are listed with the open questions in [DEFINITIONS.md](DEFINITIONS.md) |
| Rules Table | Version 1 (7 August, 33 rules) and version 2 (11 September, the same rules routed to the analyses they govern, plus 9 new ones) are both in [data/rules/](data/rules/RULES_TABLE_V2.md) |
| HSP90 trust table | Two of six rows usable |

## What this week showed

Text did not work as a way of giving the AI the rules. It read them, and it obeyed the wrong ones: a rule about FRET dyes became a requirement on an NMR question. Where a rule would have mattered most, in preparing the data, no rule ever acted.

Building the rules into fixed analysis steps worked better, for one specific thing. Each step has a card: what it answers, which inputs it reads, which parameters are allowed, what must hold before it runs, and the strongest claim its result supports. The AI has to call the steps and to attach each number it reports to the step that produced it. On eight earlier answers, checking numbers this way caught 6 of the 7 errors we knew about; the old check, which only asked whether a number appeared somewhere in the output, caught none.

The same round showed where the problem sits now. A step executes a wrong definition as reliably as a right one. Two of our definitions failed a basic control: open-start HSP90 runs, which agree with the open-state NOE restraints in 18 of 20 cases, were placed outside the open reference by our neighbourhood definition. The AI reported that result faithfully and got full marks for it, because the scoring key was built on the same definition. So far, then, we have measured whether the AI reproduces our definitions, not whether the definitions are right.

Reorganizing the rules around the question each one helps answer (version 2 of the table) made a further gap visible. None of the 33 original rules says when an MD quantity has converged, when a population can be stated, or when a state has been reached. They come from papers on combining experiments. The criteria HSP90 needed had to come from the sampling-quality literature and from our own mistakes.

## How we now think a rule should be chosen

Two readings shaped this: Li, Thomasen and Cossio's *Are we capturing the ensemble?* and Bhakat's T4 lysozyme benchmark ([SOURCES.md](SOURCES.md)). The first argues that the useful question is which differences between distributions a measurement, after its processing, can still tell apart. The second shows that sampling a region is not the same as recovering an experimentally confirmed state, and that coverage, weights and kinetics are separate claims.

Put together, a rule is a relation with four parts: the difference the question needs to resolve (a population, a state reached, a rate, a local fluctuation), the measurement and the processing at hand, the conditions under which they still preserve that difference, and the strongest claim the result may make. A rule is selected because it matches the difference being asked and the data in front of us, not because it matches a data type. It reaches the analysis through a fixed step, never as text the AI may or may not read. And any definition inside a step has to pass a control on the data before its result is used.

Version 2 of the table is the first pass at writing the rules this way. The steps that remain are in [PLAN.md](PLAN.md).

## Four questions

1. Is this the right way to organize and select rules, or does it lose something the original checklist form had?
2. The HSP90 trust table in [RESULTS.md](RESULTS.md): is it the kind of output you had in mind in July, and what is missing from it?
3. The definitions in [DEFINITIONS.md](DEFINITIONS.md) are the part we cannot settle alone. What should count as near the open state, and when has a fraction settled? The authors call about 9 closed-start runs almost compatible with the open NOEs; our 1 Å cutoff counts none of them. Should we calibrate against the authors' own classification, or is there a standard definition you would use?
4. Given all this, where should the AI sit: choosing and running the analysis steps, or only writing up what fixed steps produce?

## How to read this repository

| Time | Read | What it gives you |
|---|---|---|
| 10 min | This page | The state of the project and the questions |
| 15 min | [RESULTS.md](RESULTS.md) | The four cases, and the HSP90 trust table |
| 10 min | [DEFINITIONS.md](DEFINITIONS.md) | Every definition behind the HSP90 judgments, with its control |
| 15 min | [data/rules/RULES_TABLE_V2.md](data/rules/RULES_TABLE_V2.md) | The rules, routed to the analyses they govern; version 1 alongside |
| 5 min | [PLAN.md](PLAN.md) | What we intend to do with the rules next |
| as needed | [WORKFLOW.md](WORKFLOW.md), [data/](data/README.md), [slides/](slides/) | The history, the tables behind every number, the slides of 10 September |

## Limits

Four AI runs per condition, compared by medians. Three of the four cases were used while the rules were being developed; ADK was new to them. The corrected DHFR distances and the ADK and nanodisc analyses are our own calculations, not AI results. The 11 September comparison had one scorer, and its free-analysis arm was cut short by tool limits, so it supports the checkability result and nothing about effect size. No rule or definition has been reviewed by a domain expert.

## About this repository

This branch holds the results, the data behind them, the rules and the slides. The analysis code, every AI run with its logs and the development history are on the branch [`feature/luna-runtime-v1`](https://github.com/alex051107/dynamics-atlas-harness/tree/feature/luna-runtime-v1/review); the platform code is on `main`. The operator round of 11 September, with code, every run, scoring and an external review, is on [`feature/operator-plan-review-20260911`](https://github.com/alex051107/dynamics-atlas-harness/tree/feature/operator-plan-review-20260911/review/operator-plan-20260911).
