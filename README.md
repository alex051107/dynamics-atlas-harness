# Dynamics Atlas

Updated 11 September 2026 · Zhenpeng Liu · UNC

**Purpose.** Given a protein-dynamics dataset (MD trajectories, with NMR, SAXS or FRET where available), which ensemble quantities can be trusted, and on what evidence? The project has two outputs: the science, case by case, with every number traceable to a file in this repository; and a reusable workflow in which an AI analyst does part of the analysis under explicit rules, with each use of the rules tested against the same setting without them.

## Where things stand

| | Status on 11 September 2026 |
|---|---|
| Four cases: HSP90, nanodisc, DHFR, ADK | Each has a bounded result from the authors' deposited data ([RESULTS.md](RESULTS.md)) |
| Rules Table | Version 1 (7 August): 33 rules from 11 methods papers. Version 2 (11 September): the same rules routed to the analyses they govern, plus rules on MD sampling quality and rules learned from our own data ([data/rules/](data/rules/RULES_TABLE_V2.md)) |
| Rules given to the AI as text (10 September) | No stable gain; one harm, FRET conditions applied to an NMR question |
| Rules built into analysis operators (11 September) | The AI's numbers became checkable: 6 of 7 known numerical errors caught, against none with the earlier check. Two operators rest on a definition that fails a basic control |
| HSP90 trust table | Two of six rows usable; the rest wait on the definitions in [DEFINITIONS.md](DEFINITIONS.md) |

## The question that matters most now

Every trust judgment rests on definitions: when a lid conformation counts as near the open state, when a fraction has settled, what neighbourhood an NMR ensemble defines. So far these definitions are ours. They were not taken from the sampling-quality literature, and no domain expert has checked them. On 11 September two of them failed a basic control: open-start HSP90 runs that agree with the open-state NOEs were placed outside the open reference. The AI still received full marks for reporting that output, because the scoring key was built from the same definitions.

So far we have measured whether an AI reproduces our definitions. Whether the science is right has not been tested. Before asking whether rules or an AI help, the criteria themselves have to be right. We propose to check them in two ways: against established methods for uncertainty and sampling quality in MD (Grossfield et al. 2019), and against the one expert judgment available for HSP90, the authors' own reading of their 20 closed-start runs (7 stable, about 9 moving toward open-like conformations, 4 neither).

The two readings do not agree yet. The authors describe about 9 runs as reaching conformations almost compatible with the open-state NOEs; our 1 Å criterion counts none of them, and 2 Å counts 3.

## What we would like you to judge

A line per question is enough.

1. Order of work: should the trust criteria (definitions and their controls) be validated before any further AI comparison?
2. "Near the open state" in HSP90: a tolerance on the NOE violation (which value?), a lid-RMSD neighbourhood calibrated on the open-start runs, or the authors' clustering? The options and their controls are in [DEFINITIONS.md](DEFINITIONS.md).
3. Populations: no run returns (0 of 40). Is "no population from these runs" the right entry, or should fractions also be reported with block-averaged uncertainty as descriptive numbers?
4. The Rules Table: version 2 shows that none of the 33 original rules gives a criterion for these MD questions; they come from papers on combining experiments (smFRET, SAXS, cryo-EM, DEER). Should the rules for "can this MD quantity be trusted" be built from the sampling-quality literature, with the original 33 kept for comparisons across experiments?
5. The AI comparison: a repaired comparison is ready, with free analysis, the same rules as text, operators with the rules, and operators without them. Run it now, or after the definitions are settled?

## What is in this repository

| File | What it holds |
|---|---|
| [RESULTS.md](RESULTS.md) | The four cases one by one, and the operator results of 11 September |
| [DEFINITIONS.md](DEFINITIONS.md) | Every definition behind the HSP90 trust judgments, with its control and the open question |
| [data/rules/](data/rules/RULES_TABLE_V2.md) | Rules Table version 2, how it differs from version 1, and version 1 itself |
| [WORKFLOW.md](WORKFLOW.md) | How the project got here: the starting idea, the workflow, the tests of the rules on 10 and 11 September |
| [data/](data/) | The tables behind every number, with a [data guide](data/README.md) |
| [slides/](slides/) | Slides with notes, as of 10 September. Open `reader.html` in a browser |
| [SOURCES.md](SOURCES.md) | Papers and deposited data |

## Limits

Four AI runs per condition, compared by medians. Three of the four cases were used while the rules were being developed; ADK was new to them. The corrected DHFR distances and the ADK and nanodisc analyses are our own calculations, not AI results. On 11 September there was one scorer, and the free-analysis arm was cut short by tool limits. The results support decisions about what to build next, not accuracy rates.

## About this repository

This branch holds the results, the data behind them, the rules and the slides. The analysis code, every AI run with its logs and the development history are on the branch [`feature/luna-runtime-v1`](https://github.com/alex051107/dynamics-atlas-harness/tree/feature/luna-runtime-v1/review); the platform code is on `main`. The operator round of 11 September, with code, every run, scoring and an external review, is on [`feature/operator-plan-review-20260911`](https://github.com/alex051107/dynamics-atlas-harness/tree/feature/operator-plan-review-20260911/review/operator-plan-20260911).
