# Dynamics Atlas

**What can different measurements tell us about the same protein?**

Dynamics Atlas studies how molecular simulations, nuclear magnetic resonance (NMR), scattering and fluorescence data can support a useful scientific answer. A structure moving toward a reference, a state population and a transition rate are different claims. We aim to make the evidence, calculations and limits of each comparison explicit.

The Rules Table began as a source-linked record of scientific assumptions and method requirements. Whether putting those rules into an Agent workflow improves its answers is a separate, testable question—not the project's definition of success.

## Start here — no installation needed

| Read | What it answers |
|---|---|
| **[Collaborator briefing](collaborators/README.md)** | The research question, current position and questions for discussion |
| **[12-slide results presentation — PDF](review/four-layer-20260910/outputs/COLLABORATOR_REPORT_EN.pdf)** · [PowerPoint](review/four-layer-20260910/outputs/COLLABORATOR_REPORT_EN.pptx) | A visual overview of the scientific examples and completed pilot |
| **[Authors' claims and our findings](collaborators/docs/RESULTS.md)** | What the papers reported, what we actually analysed and what remains unresolved |
| **[Research stages and results](collaborators/docs/PROGRESS.md)** | Why the work changed direction and where we are now |
| **[What the Rules Table does—and does not do](collaborators/docs/RULES.md)** | The four tested forms of assistance, their results and their limits |

**Current position:** the case analyses and the component pilot have been delivered. The pilot was scored and unblinded; it is not awaiting unblinding. The next research step is a scientific interpretation and investment decision, not an automatically continuing experiment.

## The main findings

| Case | What the current analysis supports | Important limit |
|---|---|---|
| HSP90 | Sustained open-direction readings need not imply agreement with the open-state NOE reference. | The direction criterion, reference tolerance and full physical transition are not interchangeable. |
| DHFR | After correcting periodic-coordinate representation, selected protein–ligand distances are smaller with 4′-DTMP in both studied backgrounds. | One trajectory per condition; these are proximity results, not an independently established inhibition mechanism. |
| ADK | The selected domain-distance descriptors increase between the first and last windows in both apo trajectories. | This does not exclude local closure events or test the paper's ATP-triggered scattering experiment. |

[Read the definitions, numbers, author comparisons and sources.](collaborators/docs/RESULTS.md)

The completed Agent pilot found **task-dependent effects, not a stable general advantage from the current rule selector or conclusion checker**. Full rules performed better on the nanodisc task but worse on HSP90. Explicit subquestions improved supported coverage in both tested cases, without uniformly improving accuracy. The warning-card and feedback results also exposed differences between providing information, delivering it to the Agent, and correcting a scientific error. [Results and evaluation limits](collaborators/docs/RULES.md).

## Where the work stands

1. **Scientific knowledge:** literature-derived prerequisites and source links have been collected. They remain reviewable proposals, not scientific verdicts.
2. **Concrete analyses:** HSP90, DHFR and ADK now have bounded results; the earlier nanodisc work provides a cross-observable development example.
3. **Automation pilot:** the specified component comparisons are complete. Their raw answers, failures and sealed scores remain available.
4. **Next decision:** identify the next useful scientific question and retain only workflow components that help answer it. No new study is authorized by this README.

The scientific goals are reliability and cross-source interpretation. Reusable workflows serve those goals; limited AI automation can fail independently. [Stage-by-stage evidence](collaborators/docs/PROGRESS.md).

## Methods and numerical reproduction

Read [methods and boundaries](collaborators/docs/METHODS.md) and [primary sources](collaborators/docs/SOURCES.md). The [reproduction guide](collaborators/docs/REPRODUCE.md) provides an offline Docker route and a dependency-free Python alternative.

The small replay starts from **supplied analysed tables**. It does not regenerate MD, reconstruct the raw-coordinate preparation, rerun the Agent pilot or independently validate a physical model. A replay `PASS` means the declared numerical checks matched—not that the scientific conclusions have received domain approval.

The [10 September numerical replay ZIP](collaborators/downloads/Dynamics_Atlas_Group_Package_20260910.zip) is a preserved, standalone reproduction snapshot. The current GitHub briefing above includes later presentation edits and links to slides and pilot evidence; those additions are not retroactively inserted into that ZIP.

## Evidence without the clutter

The collaborator pages are the reading path. [Research records](research/README.md) provide the audit path to raw answers, frozen inputs, scores, source history and earlier reviews. Superseded plans and failed results remain at their original paths so that citations and comparisons are not broken. They are not presented as current instructions or current conclusions.

This delivery is on `feature/luna-runtime-v1` in [Draft PR #27](https://github.com/alex051107/dynamics-atlas-harness/pull/27), not on `main`. Share this branch's README or the collaborator briefing, rather than the repository's default-branch homepage. Existing access to the private repository is required.
