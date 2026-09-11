# Dynamics Atlas — collaborator briefing

**We want to help a researcher say what different protein-dynamics data support, without confusing a useful observation with a complete molecular explanation.**

This page is designed to be read without a meeting or a local software setup. Start with the question and current findings; use the methods and evidence links only as deeply as needed.

## A short reading route

| Time available | Read |
|---|---|
| A few minutes | This page, then the summary table in [Authors' claims and our findings](docs/RESULTS.md) |
| About 15 minutes | [Results slides — PDF](../review/four-layer-20260910/outputs/COLLABORATOR_REPORT_EN.pdf), alongside [Research stages](docs/PROGRESS.md) |
| Detailed review | [Results](docs/RESULTS.md), [Rules experiments](docs/RULES.md), [Methods](docs/METHODS.md) and [Sources](docs/SOURCES.md) |
| Numerical verification | [Reproduction instructions](docs/REPRODUCE.md); no model API key is required |

[Editable slides — PowerPoint](../review/four-layer-20260910/outputs/COLLABORATOR_REPORT_EN.pptx). The existing 12-slide results deck is retained unchanged as a presentation snapshot. In its HSP90 discussion, “initially open-direction” means **the first qualifying persistent segment**, not necessarily the simulation's initial time. Admission enforcement described in the slides is a proposed response to observed defects, not a proven general-purpose validator. The prose below and the results page make these boundaries explicit.

## The question that started the project

A researcher may have a simulation, NMR measurements and a scattering or fluorescence experiment for the same protein. The task is not simply to combine files. It is to identify the quantity each source constrains, determine whether the samples and conditions can be compared, perform the necessary analysis and give a conclusion at the level supported by the evidence.

Our scientific priorities are reliable quantities and meaningful cross-source comparisons. Reusable analysis comes next. Agent automation is a separate hypothesis: an Agent completing a task is not itself evidence that the scientific interpretation is correct.

## What we have learned

**HSP90:** ten of the twenty closed-start trajectories contain sustained open-direction segments under the five-saved-point definition. This does not mean ten complete opening events. At the project's 1 Å NOE tolerance, nine of these ten trajectories fall into the relative-direction-only category, while one is partially consistent. Some individual segments nevertheless approach the open reference. [Definitions and source records](docs/RESULTS.md#hsp90-direction-reference-agreement-and-transition-are-different-claims).

**DHFR:** correcting periodic-coordinate representation changes the local distance analysis. Selected M20–ligand distances are smaller with 4′-DTMP in both WT and L28R. This is a developer-corrected result; the two original Agents did not discover the bad input representation. [Numbers and ownership](docs/RESULTS.md#dhfr-corrected-distances-support-proximity-not-a-unique-inhibition-mechanism).

**ADK:** neither first-to-last-window comparison shows both selected domain distances decreasing. The simulations are apo and do not reproduce the paper's ATP-triggered scattering experiment. [Conditions and limits](docs/RESULTS.md#adk-the-deposited-apo-trajectories-do-not-test-the-atp-triggered-experiment).

These are bounded scientific results. They are not interchangeable with software tests or Agent performance scores.

## Where we are now

**The component pilot is complete and unblinded.** It compared input-warning cards, one round of answer feedback, different method guidance, and explicit subquestions. The evidence supports task-dependent findings, not a generally successful four-layer harness.

Full selected rules helped on the nanodisc task but not on HSP90. More explicit questions improved answer coverage in both tested cases, although HSP90 acquired one additional core error across the four runs. Four warning-card runs listed the file but did not read it; the tested feedback checker did not reduce any of its twelve answers' core-error counts. [What each experiment actually changed](docs/RULES.md).

Most materials had already been used in development. The scorer also helped prepare the cases; masking condition labels was not independent domain-expert review. The original and revised answers are preserved, and no completed experiment is rerun by opening this package.

## What would be useful to discuss

**Scientific interpretation:** are the current observables and limits sufficient for the intended question—particularly the connection between HSP90's direction labels, native NOE violations and a structural-state interpretation?

**Next scientific deliverable:** which unresolved comparison would change a biological interpretation, rather than merely add another plotted quantity? This needs a specific question and available evidence; it does not require completing every historical task.

**Role of Rules:** the current working recommendation is to keep the literature record and concise, applicable guidance, while pausing expansion of the selector and generic conclusion checker. A useful ordinary analysis is allowed to remain ordinary. These are discussion points, not authorization for another experimental campaign.

## Reproduction and audit trail

The [offline replay](docs/REPRODUCE.md) recalculates selected HSP90, DHFR and ADK summaries from provided analysed tables. Coordinate preparation and Agent experiments are outside that replay. The [existing replay ZIP](downloads/Dynamics_Atlas_Group_Package_20260910.zip) remains a fixed numerical package; it does not include these later briefing edits or the linked slide files.

The current reading set is deliberately small: **this briefing, Results, Progress, Rules, Methods, Sources and the reproduction guide**. Nothing in the presentation cleanup changes frozen inputs, scores or scientific results.
