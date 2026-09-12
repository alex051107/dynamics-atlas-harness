# A case study of evaluating AI agents on a neuroscience data-to-discovery pipeline

**Authors:** Horstmann, Kai A.
**Year:** 2026
**Venue:** arXiv
**arXiv:** 2606.07718
**Source PDF URL:** https://arxiv.org/pdf/2606.07718
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---
A case study of evaluating AI agents on a neuroscience
data-to-discovery pipeline
Kai A. Horstmann1 , Ethan Lin1 , Alice A. Robie2 , Jennifer J. Sun1 , Kristin Branson2
2 HHMI Janelia Research Campus

1 Cornell University

Abstract
Agentic AI offers a promising path to automating software development
bottlenecks in scientific research pipelines, particularly for stages that take
domain experts days to months to build and where correctness and robustness matter more than implementation details. We present an empirical study of general-purpose coding agents on a fly optogenetics data-todiscovery pipeline. We assess agents on tasks and datasets substantially
larger than existing benchmarks and evaluation criteria grounded in domain expert standards. We show that agents can solve several pipeline
stages, suggesting stage-level automation is tractable. By analyzing agents’
code iterations, we show they struggle most without a pre-defined criterion,
when they must instead use their scientific judgment to assess their current
solution. Mirroring scientists, they sometimes attempt visual inspection
of intermediate outputs for self-evaluation, but largely fail to interpret
what they see or act on it appropriately. Solving the end-to-end pipeline
requires stringing together successes across all stages, which is beyond
agents’ current abilities. We identify challenges largely absent from existing
benchmarks, including computational resource management and generalization to held-out data. Finally, we distill principles for constructing
scientific tasks and rigorous evaluation criteria for open-ended problems.

Introduction

Science is inherently iterative: scientists break complex phenomena into manageable pieces,
understand each with as much rigor as possible, and build on those who came before. In
behavioral neuroscience, modern experiments (Chiu et al., 2025; Robie et al., 2024; Allen
Institute, 2021; The International Brain Laboratory, 2022) rely on tools and methodologies
(Kabra et al., 2013; Branson et al., 2009; Eyjolfsdottir et al., 2014; Pachitariu et al., 2016; 2023;
Mathis et al., 2018) developed over decades. These tools function as trusted modules: they
solve specific problems (e.g., tracking or signal processing) well enough for the community
to treat them as reliable foundations, allowing researchers to move on to harder questions.
These modules represent months to years of effort by scientists with deep, narrow expertise.
This reductive approach—decomposing complex workflows into discrete, trusted modules—
presents unique challenges and opportunities for AI in science. Because scientific validity
relies on the integrity of every step in the chain, any AI-produced solution must be as valid
as that produced by expert scientists. This high bar has made scientists hesitant to adopt
fully automated “AI scientist” or self-driving lab approaches (Lu et al., 2026; Gottweis et al.,
2025; Ghareeb et al., 2025) for which we lack not only evidence of human-level performance,
but even the metrics to assess capabilities like creativity, diversity, and scientific reasoning.
Instead, a more tractable near-term opportunity lies in automating the software development
problems embedded in research pipelines, verifiable stages for which scientists care about
correctness and robustness, but not about implementation details. Building these stages is
increasingly feasible with rapid progress in agentic coding, but they are substantially more
complex than prior AI-for-science benchmarks (Fig. 3): they can take a developer days to
months to build, and must generalize to unseen, possibly out-of-distribution data.
Code available at: https://github.com/kaihorstmann/neuro-d2d-eval

Fly Optogenetics Data-to-Discovery Pipeline
Processed
trajectories

Fly Body

Experimental
variable
time series

classifications

Raw video

time series
Raw trajectories

Task-by-task
End-to-End

Figure 1: Outline of our analysis of a 7-stage fly optogenetics data-to-discovery pipeline. We evaluate
and analyze agents at the task level as well as end-to-end across the entire pipeline.

In this work, we present an empirical study of general-purpose coding agents on a representative end-to-end neuroscience research pipeline: fly optogenetics (Fig. 1). We decompose
this pipeline into 7 tasks spanning the full analysis, from bespoke data handling and
computer vision tracking to feature computation, behavior classification, and statistical
interpretation, and evaluate agents against both expert human annotations and trusted
legacy codebases that define the current scientific standard. We focus on general-purpose
models to assess immediate, off-the-shelf automation potential and to systematically measure the impact of specific design choices on performance. Beyond quantifying success
rates, we manually analyze the agents’ code iterations and solutions to identify major failure
modes and surprising success modes, identifying key directions for future development of
agentic systems for science and benchmarking. We also distill principles of task design, with
particular focus on constructing quantitative evaluation criteria for open-ended problems, a
challenge existing benchmarks acknowledge but rarely address concretely.
Our contributions are:
• Data-to-discovery pipeline tasks. We develop a comprehensive, end-to-end evaluation
framework based on a fly optogenetics data-to-discovery pipeline, designed to evaluate
agents for scientific validity on 7 unique tasks individually and combined.
• Task and data size. Our tasks are substantially larger than those in existing benchmarks in
terms of lines of code (a proxy for human effort), and closer to what scientists actually
want agentic AI to do: solve time-consuming bottlenecks (Fig. 2). Datasets are correspondingly larger, requiring computationally efficient solutions—a constraint small-scale
benchmarks do not impose or measure.
• Generalization. Real scientific data is messy and variable; solutions must generalize
to unseen, potentially out-of-distribution inputs. We examine how agents handle this
challenge and where brittleness to data variability manifests.
• Stages vs. pipelines. We evaluate agents both on individual stages and on the full end-toend pipeline, revealing a gap between stage-level and pipeline-level feasibility.
• Breadth vs. depth. Rather than sampling broadly across domains, we take a depth-first approach on a single pipeline, enabling detailed characterization of task design, evaluation
criteria, and agents’ success and failure modes. We manually examine agents’ solutions
and trajectories, quantifying how often iteration leads to improvement and auditing their
use of data visualization as a self-evaluation mechanism. Tasks range from rigid, fully
specified problems to open-ended steps with a space of acceptable solutions, allowing us
to compare agents and task properties quantitatively.

Related work

LLMs and AI agents in science. There has been rapidly growing interest in leveraging
LLMs and AI agents to accelerate scientific discovery (Amodei, 2024; Gridach et al., 2025).

High:
Low:
Expert-designed
Generic,
pass criteria,
misaligned
Pass consitutes
with scientists'
usability now
requirements
Evaluation Would an expert trust
rigor: the solution?

Stage

Stage

E2E

BLADE DS-1000

Low:
Small tasks,
not a bottleneck

High:
Time-consuming
Bottleneck
Big data

Task realism: Is this a task scientists would
delegate to an AI agent?

Task realism
Input modalities

Fly Body Tracking

Video

Training data

Behavior time series,
Trajectories, behavior
classes, training data
Behavior classes, exp. var.,
behavior time series

Evaluation rigor
Scientist
Scientists
This study
effort
DaysManual, heuristics MOTA > scientist
months
DaysManual, comparison %ile error ≤ (1 + ϵ)·
months
scientist
Hours-days
Manual
Error vs scientist
<ϵ
Hours-days
Matches specs
Error vs GT < ϵ
Daysmonths
Days
Hours

Manual, comparison
Accuracy
≥ (1 − ϵ)·scientist
Manual, comparison Bout-level error vs
scientist < ϵ
Matches specs
Significance tests
match scientist

Figure 2: Left: Comparison of our case study to existing benchmarks. Task realism refers to how well
tasks mirror what scientists would like to delegate to an AI agent. Evaluation rigor refers to whether
criteria are sufficient to convince domain experts that a solution is trustworthy. Right: Properties of
each pipeline stage, organized by task realism and evaluation rigor. For each stage, we describe the
input modalities and estimated expert effort required to implement it, the methods scientists use to
validate solutions in practice, and the corresponding quantitative criteria used in this study.

General-purpose agents with access to diverse scientific tools (Turcan et al., 2025; Aygün
et al., 2025) have demonstrated promising capabilities in biomedicine (Huang et al., 2025),
chemistry (Bran et al., 2023), and biomedical image analysis (Wang et al., 2026), while more
specialized agents have been designed for tasks like gene perturbation (Roohani et al., 2025)
and editing (Qu et al., 2025). Recent work has pushed further toward fully autonomous AI
scientists (Lu et al., 2026; Mitchener et al., 2025; Gottweis et al., 2025; Ghareeb et al., 2025).
Our work complements these efforts by rigorously characterizing where general-purpose
agents succeed and fail within a complex, multi-stage scientific pipeline.
Science benchmarks. Benchmarking AI agents in science remains challenging, with open
questions about how to subdivide the problem space, automatically assess performance on
open-ended problems, and construct representative datasets to support reliable conclusions.
Most closely related to our work is ScienceAgentBench (Chen et al., 2025), which evaluates
agents on software-development tasks across scientific domains and parts of the data-todiscovery pipeline. However, its tasks are on average 10x smaller (41 vs 447 lines of code, a
proxy for expert effort) than the pipeline stages we consider, thus less representative of the
time-consuming bottlenecks scientists actually want to automate. In addition, datasets are
small, on average just 54 MB, over 250x smaller than those in our tasks. While evaluation
criteria are task-specific, the reasoning behind thresholds is not documented. For example,
the cutoff for a cell-counting task was an MAE of 30 cells, despite images containing as few
as 9 cells, a threshold that may reflect insufficient depth of domain expertise, and differs
from the evaluation criterion reported in the source paper for that dataset (Carpenter et al.,
2006). Given the benchmark’s breadth, this may be an unavoidable tradeoff.
DiscoveryBench (Majumder et al., 2024b) and BLADE (Gu et al., 2025b) focus on hypothesis
generation and testing through retrieval from small tabular datasets already abstracted
to concepts. While these tasks require scientific reasoning skills, they would require little
scientist effort (on average 24 and 3 lines of code), and they are not representative of bottlenecks to scientists’ progress. Both approaches rely on LLMs as a judge to measure success,
a measure whose reliability for assessing scientific validity has not been established (Tan
et al., 2025). BLADE is exceptional in that it attempts to characterize the full solution space
rather than a single ground truth, but is restricted to problems where that solution space
is enumerable, limiting its applicability to more open-ended or computationally intensive
stages. Neither benchmark addresses the kind of multi-stage, high-precision computational
pipelines we study, and neither validates with the rigor required for scientific validity.
DS-1000 (Lai et al., 2022) focuses on data science problems drawn from StackOverflow, most
requiring a few lines of code with no data input, useful for measuring general programming
competence but not representative of the complexity of scientific analysis stages.
Data-to-discovery pipelines in neuroscience. The majority of experiments in modern
neuroscience necessitate complex sequences of analyses that have evolved alongside ad3

(a)

AI Scientist
SakanaAI (2026), AI Co-Scientist (2025),
Robin (2025), Kosmos (2025)

Data-to-discovery
pipeline

Literature survey

This work, end-to-end

What is the state of the field?
PaperBench (2025)
LitQA (2024)
ScholarQA (2025)

ScienceAgentBench (2025)

Function 1

Stage 1

Function 2

Research question

Stage 2

..
.

IdeaBench (2024)

..
.

Experiment design

Tool building

BLADE (2025a)

DiscoveryBench (2024a),
BLADE (2025a)

Paper writing

Lines of code

(b)

Conclusion

DS-1000 (2022)

Stage N

rig, reagent building, etc.

Data-to-discovery
pipeline

def fun(mov,ns=10):
nf = mov.nf()
idx = linspace(0,nf,ns)
fs = []
for i in idx:
f = mov.f(int(i))
fs.append(f)
return median(fs)

Function N

DiscoveryWorld (2024)

Data collection

Function

Pipeline stage
This work, single task
ScienceAgentBench (2025)

Lines of code (sqrt scale)

Figure 3: (a) Taxonomy of AI in science benchmarks, mapping existing work to stages of the scientific
workflow from literature survey to paper writing. (b) Distribution of task sizes (lines of code) across
benchmarks on a square-root scale. Our pipeline stages are substantially larger, reflecting the scale of
tasks that would represent significant time savings for an expert scientist if successfully automated.
vancements in data acquisition (Robie et al., 2024; Allen Institute, 2021; The International
Brain Laboratory, 2022; Zheng et al., 2018; Meissner et al., 2023; Winnubst et al., 2019). These
workflows typically require the integration of multiple data modalities, such as microscopy,
neural dynamics, and behavior, where processing any single modality involves a distinct,
multi-stage pipeline. Data-to-discovery pipelines transform raw experimental data into
abstracted representations that scientists can reason about. This transformation involves
two interleaved processes: quantification: extracting measurable signals from raw data,
such as tracking positions from video or counting cells from images—and conceptualization:
iterative decisions about what to measure, how to define it, and what level of abstraction is
appropriate for the scientific question at hand.
Here, we focus on behavioral analysis in fly optogenetics (Chiu et al., 2025; Rubin et al.,
2025; Robie et al., 2024), a modality requiring pipelines that chain together tracking, pose
estimation, feature extraction, behavior classification, and statistical analyses. Ultimately,
many modern experiments aim to synthesize these diverse streams of data into a unified
interpretation (Angelaki et al., 2025), which also significantly increases the complexity of
the underlying computational workflows.

Task design

Designing this case study’s prompts and evaluation criteria was an iterative process:
prompts must be precise without being overly prescriptive, and evaluation must be robust
to valid variation while reflecting the high bar for correctness in science—a standard that
is challenging to automate, given the unreliability of LLM-as-a-judge (Thakur et al., 2025;
Zhang & Branson, 2026). § A details the shared structure of prompts and evaluations across
tasks. Below, we distill observations from this process that may inform future scientific
benchmarks. Each reflects a specific revision we made, which we detail in the Appendix.
• Avoid over-prescription in prompts. When prompts describe a specific algorithm rather
than the problem itself, the task reduces to rote implementation. Early prompts designed
with domain experts often included the scientist’s algorithmic choices, which constrained
agents to particular methods (§ A.5). Including extraneous implementation details can
distract agents from the core task (§ A.1).

• Avoid under-specification in prompts. Ambiguous problem definitions admit multiple
valid interpretations, making evaluation difficult. Under-specified tasks meant solutions
could differ from the reference for arguably valid reasons, requiring iteration on both
prompts and evaluation criteria based on results (§ A.4, § A.6).
• Isolate evaluation from scientist-specific implementation choices. Scientist solutions
may contain incidental choices that are not intrinsic to correctness. Evaluation should not
penalize agents for omitting unstated steps that the scientist happened to include, nor
should they assume agents will make the same implementation decisions. Evaluation
should admit any solution satisfying the core definition (§ A.6).
• Robust evaluation instead of prompt constraints. Rather than adding prompt constraints
to simplify evaluation, invest effort in making evaluation robust to valid variation. This
keeps tasks realistic (§ A.2, § A.4) and avoids over-indexing to evaluation convenience.
• Specify evaluation criteria in the prompt. Agents benefit from knowing how they will
be evaluated. When prompts lacked success criteria, agent solutions tended to not meet
the high bar needed for downstream tasks. Adding explicit metrics and target thresholds
enabled agents to monitor their own performance against the provided data (§ A.3).
• Validate prompts and scientist solutions. Multiple reviewers including domain experts
should verify that prompts contain all necessary information and no extraneous details.
Domain expertise is particularly valuable for identifying implicit assumptions that may
be obvious to specialists but absent from the prompt. This process uncovered bugs in
scientists’ reference implementations that had survived peer review (§ A.2, § A.4).
3.1

Evaluation criteria design

A central challenge in evaluating agent solutions is defining what constitutes “correct.” In
scientific workflows, correctness is rarely binary, and ground truth labels are often unavailable: many tasks require scientists to assess correctness through qualitative inspection and
iterative refinement. Our evaluation criteria aim to answer: would a domain scientist trust
and use the agent’s solution in place of their own? We operationalize this by comparing agents’
solutions to a scientist reference solution derived from published methods (§ D). We employ
two primary evaluation strategies depending on whether ground truth labels are available.
• Ground truth available. For tasks where labeled ground truth exists (Body Tracking,
Keypoint Tracking, Walking Behavior Classification), we compare both the agent’s and
scientist’s solutions against the ground truth. The agent passes if its score is within a
tolerance of the scientist’s: score(agent, GT) ≥ (1 − ϵ) · score(scientist, GT).
• Ground truth unavailable. For tasks where ground truth labels do not exist or are impractical to obtain (Behavior Feature Computation, Registration, Statistical Comparisons),
we treat the scientist’s solution as the reference and measure deviation from it. The agent
passes if all outputs i are sufficiently close: maxi |agenti − scientisti | ≤ ϵ.
Here, ϵ is a task-specific tolerance set in consultation with domain scientists to reflect
variability between valid solutions and the sensitivity of downstream analyses to errors. A
tolerance-sensitivity analysis (§ C) shows that results are robust to reasonable variation in ϵ.
Alternative approaches. A third strategy we did not employ but merits consideration
is measuring inter-scientist agreement: dist(scientist1 , scientist2 ). This would establish a
baseline for acceptable variation by quantifying how much two domain experts differ on
the same task, providing a principled threshold for agent evaluation.
3.2

Task descriptions

We evaluate agents under two settings: single-stage tasks, which isolate individual pipeline
components, and end-to-end tasks, which require executing the full workflow (Fig. 1). Evaluation criteria are detailed in § B, and the scientific abilities tested in § E.
• Body Tracking. Tracks positions and identities of multiple interacting flies over time, a
long-standing computer vision problem. Agents are given no ground truth or optimizable
criterion, and so must devise their own evaluation criteria.
• Registration. Scales and translates trajectories into a common coordinate system, and
cleans frames where tracking is missing. This is a comparatively straightforward step.

• Behavior Feature Computation. From trajectories, computes interpretable behavior
features. We provide equations defining features, but not implementation details.
• Walking Behavior Classification. Classifies whether each fly is walking forward in each
frame, given a labeled training dataset.
• Keypoint Tracking. Estimates positions of 21 keypoints per fly, with pixel-level precision
needed for downstream analyses. The criterion is well-defined, but the approach is not.
• Gait Segmentation. Segments each leg’s motion into swing (lifted off the ground) and
stance (touching the ground) phases, a classical locomotion analysis typically solved with
thresholding heuristics. We provide a small set of labeled examples for tuning.
• Statistical Comparisons. Statistically tests whether optogenetic perturbation affects
stance bout duration for 10 GAL4 lines compared to a genetic control group.
• End-to-End Minimal Prompt. Given the raw data and a description of the final scientific
goal, produces the full analysis. No explicit stage decomposition is given, thus success
can only be measured by the correctness of the final output.
• End-to-End Maximal Prompt. Given the raw data plus all stage-level prompts, produces
the full analysis. This tests whether agents can manage a long-context, multi-step task.
Intermediate stages are evaluated independently, in addition to the final result.

Results

4.1

Quantitative results

Table 1 summarizes agent performance across single-stage and end-to-end tasks. We report
pass (✓) and fail (∼/×) outcomes for three trials per agent-task pair, along with a taskspecific score (higher is better). Trial-to-trial variance is low, with 73% of agent-task pairs
yielding unanimous pass/fail verdicts. Definitions of pass/fail and the task scores are in
§ B, with details on per-trial token counts and wall-clock runtimes in § H.
Single-stage tasks. Agents achieve reliable performance on several individual pipeline
stages. Feature Computation and Behavior Classification are solved consistently across
all agents, with nearly all trials passing in the single-task setting. Keypoint Tracking and
Registration are similarly reliable for most agent configurations, with the exception of
terminus-2/gpt-5.4, which passes zero trials. Two stages prove difficult for all agents.
Body Tracking yields zero passes across all agent configurations, suggesting that this task,
which requires sustained visual reasoning and identity maintenance through occlusions,
remains beyond current capabilities. Gait Segmentation is similarly challenging, with only
terminus-2/claude-opus-4-6 achieving any passes.
End-to-end tasks. Performance degrades markedly in the end-to-end setting. Under the
maximal prompt, stages that agents solve reliably in isolation often fail when composed
into a pipeline. Registration and Keypoint Tracking, which both agents largely pass as
single-stage tasks, see reduced pass rates end-to-end, and Behavior Classification degrades
similarly, though to a lesser degree. Notably, all three stages are evaluated independently
of upstream outputs (e.g., on generalization to held-out test sets) and thus reflect genuine
difficulty in the composed setting rather than propagated errors. Statistical Comparison,
which Opus-4.6-backed agents solve in the single-stage setting, yields zero passes end-toend for all configurations; unlike the stages above, it depends on accumulated outputs
from all prior stages, and its failure reflects both compositional difficulty and prior stage
degradation. The minimal prompt is similarly challenging: neither agent configuration
produces a passing solution for Statistical Comparison, indicating that, for the scale of
tasks studied here, current agents struggle to construct and execute multi-stage workflows
without explicit decomposition. Together, these results suggest that managing long-context
instructions and sustaining attention over extended tasks pose challenges beyond solving
the individual subproblems.
End-to-end oracle ablations. To localize end-to-end failure across stages, we injected ground
truth inputs at two points in the agent-produced E2E Maximal pipelines (Table 1). We
injected gold Body Tracking trajectories to isolate the effect of that stage’s low performance,
with no improvement: the final stage continues to fail in all trials. This shows that the final
stage’s failure is not driven by upstream tracking quality alone. It also allows us to evaluate

Tracking Computation Classifier Segmentation Comparison

Single-stage tasks

0.017±0.003

1.928±0.125

1.376±0.055

2.281±0.108

0.451±0.387

0.020±0.006

terminus-2/claude-opus-4-6

0.044±0.022

1.371±0.046

1.851±0.006

3.354±1.019

1.201±0.225

∼∼×

terminus-2/gpt-5.4

0.005±0.008

1.999±0.002

1.892±0.090

1.355±0.286

0.464±0.367

✓∼✓

1.167±0.396

1.662±0.334

1.260±0.233

0.929±0.039

∼×✓

∼∼✓

0.682±0.127

+ gold body tracking
+ all gold upstream

∼×∼

0.020±0.002

∼×∼

1.622±0.086

0.247±0.200

0.533±0.252

0.933±0.115

✓∼×

0.039±0.038

+ gold body tracking

✓∼×

1.554±0.472

0.300±0.033

0.333±0.115

+ all gold upstream

0.833±0.153

Table 1: Agents’ performance on single-stage and end-to-end tasks, including oracle ablations for
E2E Maximal. ✓: passed stringent criteria for nearly all test videos/lines; ∼: passed on average; ×:
failed. Numbers are continuous scores (mean ± standard deviation over three trials), 1.0 = passing.
Dashes mark stages not separately evaluable, either because evaluation required correct upstream
Body Tracking or the agent was not required to follow the reference stages. Indented rows inject gold
Body Tracking inputs, or gold inputs at all stages upstream of Statistical Comparison.

the two intermediate stages which could not be compared to the reference unless the tracked
targets match. Both are degraded relative to single-stage performance, consistent with
other stages. Next, to further isolate failures in the final stage, we injected gold outputs
from all upstream stages. Scores improve substantially relative to E2E for both agents,
but remain below single-stage for Claude Code, reflecting both upstream degradation and
weaknesses in the stage implementation itself. For Codex, gold-input and single-stage
scores are comparable within noise, implicating upstream degradation alone.
4.2

Failure modes

To diagnose common failure modes, we manually reviewed the agents’ code and trajectories
to trace their stated reasoning as they iterated on their solutions. Below, we describe
observed failure modes, along with the hypothesized task properties that cause them.
Agents fail to iterate productively when self-evaluation requires scientific judgment.
Tasks that do not provide a clear evaluation metric leave the agent to devise its own
criterion; if unsuccessful, iterations will not improve. We see this in Body Tracking, where
agents are not provided ground truth to compare to (Table 4). Scientists doing this task
visualize intermediate outputs and devise metrics for assessing different types of mistakes.
In Fig. 4, agents perform many iterations and even visualize intermediate results, yet
scores do not reliably improve. The iteration-quality gap analysis (Fig. 5) supports this:
6/8 trials exhibited regret (the agent did not submit its best solution), and 4/8 submitted
solutions worse than their first. Fig. 7 visualizes a submitted solution with major tracking
errors that humans would not ignore: all true detections offset from flies and frequent false
detections. The pattern extends across other tasks lacking a scalar metric (Registration,
Feature Computation, and Statistical Comparison). This stands in contrast to ML-style tasks
(Keypoint Tracking, Behavior Classification), which iteratively improve (§ 4.3).
Agents fail to translate visual evidence into corrective action. Visualizing intermediate outputs is a key part of scientific analysis. Agents mimic this pattern with image-viewing tool
calls, but these rarely yield a sensible update. To study this systematically, we grouped contiguous runs of image-view calls answering one investigative question into distinct episodes,
and manually classified them based on the agent’s code updates and stated reasoning:

Fly body tracking

Keypoint tracking

1.00 0.00

Fraction of trajectory steps (per trial)

Normalized within-trial rank

Visualization action

Figure 4: Per-trial iteration trajectories for Body Tracking and Keypoint Tracking. The two tasks
span contrasting evaluation regimes: Body Tracking requires scientific judgment to assess output
quality, while Keypoint Tracking provides a concrete, pre-defined ML metric. Each bar is one trial,
segmented by iteration in chronological order, with segment width proportional to trajectory steps.
Segment color encodes each iteration’s within-trial rank (dark=worst, bright=best), scored from a code
snapshot at that iteration. Red ticks mark steps where agents visualized an image. Trials are sorted by
final-iteration value per task in descending order. Full seven-task view in Fig. 6.

• Improved: the visualization exposed an implementation issue in the agent’s solution, the
agent correctly diagnosed it, and proceeded to fix it.
• Neutral: the visualization was used to confirm correctness or characterize data, with no
underlying issue to act on.
• Mistargeted: the visualization was uninformative for the agent’s posed question.
• Latent Miss: the visualization surfaced a real implementation issue but the agent misinterpreted it or failed to perceive it.
• Dismissed: the agent perceived the issue but rationalized it as benign.
These failure modes isolate failures of visual perception (Latent Miss) from failures of
reasoning both upstream (Mistargeted) and downstream (Dismissed) of the visualization
itself, all of which cause underlying issues to persist across iterations. In Claude Code and
Codex episodes (Fig. 5), the two agent frameworks that support image viewing, all three
failure modes are common, and failures outnumber improvements across every task with
observed image-view calls. Consistent with this, Body Tracking trials in Fig. 4 accumulate
the densest image-view coverage while solutions do not improve monotonically, with some
visualizations driving active regression. We present a representative Latent Miss episode
per agent (§ G.1.2, § G.1.3), where a visualization exposing a real implementation issue was
misinterpreted. These failures on seemingly straightforward visual reasoning suggest that
vision-based scientific reasoning is a current weakness and an area for future development.
Agents simplify pipeline decompositions. Agents consistently use fewer sub-tasks in the
E2E Minimal task: only the first and last stages survive in every trial, with the rest fused
or replaced by simpler, less accurate implementations. While the most aggressive stage
merging produced the worst score (1/10), closely replicating the canonical decomposition
did not guarantee success when a key stage was replaced by a poor shortcut. Indeed,
even when the decomposition is provided under the maximal prompt, agents perform
no better on the final stage: across all 12 E2E trials, they identify essentially no fly lines
with significant behavioral effects (1/48). This suggests that the bottleneck for minimalprompt E2E performance is not discovering the decomposition but implementing its stages.
These implementations degrade end-to-end relative to the single-stage setting (Table 1); we
attribute this to challenges in long-horizon task management and long-context retrieval.
Attention and effort suffer in maximal end-to-end tasks. The maximal E2E task sees
basic formatting errors absent from single-stage tasks, where each workspace contains
only one model to submit. Across six Maximal trials, nearly half of submitted keypoint
and walking-classifier model files violate the prompt-specified interface and cannot be
evaluated, despite the same information being available in both settings. Maximal E2E
solutions are also systematically simpler than their single-stage counterparts (Claude Code’s
keypoint networks train for fewer epochs; Codex’s Keypoint Tracking trials drop the data
augmentation every Codex single-stage uses; walking classifiers omit rolling-window
features every single-stage submission computes). We thus hypothesize that these agents
perform worse on larger problems, even when it is trivial to decompose the problem.

Per-trial improvement from first to final iteration
n=6
n=11
1 ~4 1 11 0

n=2
1 ~1 0

n=1
1 0

n=4
1 3

By agent

n=1
~1

10 bad

improved

2.74

unchanged

# episodes

score gap

2.4

n=8
4 4

regressed

Prevalence of regret per task

fraction of trials

regret
tied
no regret
g
g
ckin ratio
ckin tatio catio tatio ariso
y Tra Regist oint Tra Compu Classifi egmen l Comp
d
o
Keyp Feature ehavior Gait S tatistica
S

5 bad

ode Codex

eC

ud
Cla

By task

6 bad

2 bad

Improved
Neutral
Latent Miss
Mistargeted
Dismissed

6 bad

1 bad 0 bad

ma inima cking ration cking
axi
M
y Tr Regis oint Tr
d
Bo
p
e

M
E2E

Figure 5: Iteration quality and image-view episode outcomes. Left, top: per-trial change in score
(§ B) from the agent’s first to its submitted solution, for trials with ≥2 iterations; boxes give counts
of improved (↑), regressed (↓), and unchanged (∼) trials. Left, bottom: per-task prevalence of regret:
submitting a solution worse than the best reached at an earlier iteration. Bars give the fraction of
trials with regret (final < best non-final), tied, or no regret. Right: image-view episode outcomes by
agent and by task, classified as Improved, Neutral, Mistargeted, Latent Miss, or Dismissed (§ 4.2).
Terminus-2 trials make no image-view calls and are omitted, as are tasks with zero episodes.
Agents lack consistent judgment about reasonable runtimes. Agents sometimes kill
training processes on weak or fabricated evidence, particularly in tasks involving longrunning scripts. One recurrent failure mode is misinterpreting a process’s aggregate CPU
time as wall-clock time; in 4 instances, the agent prematurely terminated training after
asserting that a script had been running 13× to 42× longer than it had (§ G.1.5). Agents
also reason inconsistently about training budgets within trials. In one Keypoint Tracking
trial (§ G.1.6), the agent killed a heatmap-based training run after 3 epochs, concluding it
had “plateaued,” then switched to coordinate regression, which performed worse initially
but was allowed to continue. These failures suggest the importance of measuring agent
performance on larger tasks, which produce unique types of failure.
Agent framework and model choice impact environment handling. GPT-5.4-based agents
frequently avoid installing new dependencies, at times reimplementing standard library
functionality. They ran pip install in only ∼25% of trials, compared to ∼70% for Opusbased agents. For example, one agent abandoned its initial cv2-based solution for a subpar
NumPy reimplementation, leading to a worse-performing iteration (zZMfrKG in Fig. 6).
For the Terminus-2 framework, 5/42 trials encountered temporarily unresponsive shells,
causing agents to repeatedly emit stuck messages and consume substantial numbers of
tokens (§ G.1.7). Claude Code is vulnerable to a different framework-level failure: in 2/27
trials, the agent terminated its own session by issuing a pkill command whose pattern
matched the agent process itself, ending the trial mid-task (§ G.1.8).
4.3

Success modes

Agents reliably solve ML-style tasks. Two tasks fit a standard supervised learning setup,
wherein labeled training data and a scalar evaluation metric are provided. For these, agents
iterate productively toward the metric. Keypoint Tracking exemplifies this: trials show
progressive within-trial improvement (Fig. 4), with the best iteration reliably at or near
the trajectory end. The iteration-quality analysis (Fig. 5) agrees: all multi-iteration trials
improved from first to final iteration, with 9/11 submitting their best iteration. Notably,
several Keypoint Tracking and Behavior Classification submissions matched or exceeded
the scientist’s solution, while no Body Tracking trials even reached the minimum threshold.
Agents successfully leverage domain knowledge not provided in the prompt. By design,
our prompts do not specify details considered to be in-domain knowledge (e.g. keypoint

names use anatomical terms such as “right hind-leg tarsus” as opposed to “leg tips”). We
find that agents consistently understand and apply relevant domain-specific concepts incontext. In the Gait Segmentation task, the “swing” and “stance” leg phases are defined
conceptually (“the leg is in contact with the ground” / “lifted from the ground”) with no
operational criteria for detecting them from keypoint trajectories; yet, across all trials, agents
demonstrated the biomechanical understanding of fruit flies needed to distinguish them:
8/12 trials’ reasoning traces articulated the kinematic relationship between tarsus motion
and the fly body (§ G.2.1), and 10/12 final implementations constructed a body-aligned
coordinate axis from rigid-segment keypoints to encode the classification (§ G.2.2).
Agents effectively parallelize sub-tasks within complex workflows. When the E2E pipeline
includes a long-running stage, agents consistently identify other work that can proceed
concurrently and pursue it via backgrounded tool calls. Across the 12 E2E trials, 6 show
explicit parallelization, where the agent started one script, developed another part of the
pipeline in parallel, and then returned to it later. All six are Claude Code runs; the six Codex
trials instead execute the same long stages serially in the foreground. The most common
parallelization comprises overlapping Keypoint Tracking training with Body Tracking
development, Behavior Classifier integration, or pipeline-script construction (§ G.2.3).

Discussion

We present a depth-first case study of how well general-purpose AI agents solve stages
of a data-to-discovery pipeline: a subdivision of scientific analysis natural to practicing
scientists and amenable to mixing and matching as workflows evolve. Our findings were
directly observed only in a single pipeline; we hypothesize they will generalize to scientific
tasks sharing a high bar for precision, large-scale data, long multi-stage workflows, and
reliance on data-based or visual validation—structural properties of tasks or agent abilities,
rather than of a science domain. Establishing where these patterns hold across additional
problems and agents is important future work, supported by our released dataset.
Individual pipeline stages in our benchmark are on average 10x larger than those in the
most closely related work (Chen et al., 2025), yet agents solve several of them, suggesting
that stage-level tasks of this complexity are tractable for current agents—an encouraging
signal for near-term automation of scientific bottlenecks. The end-to-end setting, however,
surfaces a qualitatively different failure mode: lapses in sustained attention across the full
task. End-to-end automation thus remains an open challenge that scales non-trivially with
task length. Our pipeline also operated on substantially larger data (>250x bigger than
Chen et al. (2025)), introducing a challenge ubiquitous in real workflows but absent from
small-scale benchmarks: agents must manage time and compute by estimating runtimes
and deciding when to sample, abort, or prioritize. We found mixed evidence of success here,
and agentic frameworks will need to address this explicitly as they scale to realistic settings.
Scientific problems pose distinct challenges for agents beyond general ML or coding. In
science, many problems exist for which no explicit mathematical criterion has yet been
formulated: the scientist intuitively understands what types of errors matter and develops
methods for visualizing outcomes and diagnosing failures. For example, a scientist validating a tracking algorithm will overlay tracked positions on raw video frames, or develop
heuristics for identifying likely tracking failures. Such exploratory, visually-grounded validation is central to scientific practice. Current agents do attempt this behavior but largely
fail to close the loop from inspection to correction. Whether stronger integration of vision
models, targeted training, or prompting can address this gap remains an open question.
Finally, we offer detailed guidelines for constructing tasks and evaluation criteria, favoring
depth over breadth to achieve the rigor necessary for results that practicing scientists
can trust. Breadth matters too, and we hope this work encourages future collaborations
between AI researchers and domain experts to expand the number of pipeline stages
that can be evaluated with this level of rigor. The framework we describe—grounded in
domain standards, attentive to equivalence classes and tolerances, and validated against the
scientists who built the original pipelines—is, we believe, broadly applicable beyond the
specific domain studied here.

Acknowledgments
We thank Adam Taylor for help with the original Fly Disco pipeline code, Goran Ceric for
help running the Harbor framework on the Janelia cluster, and the Branson and Sun labs,
Ranjit Singh, Atharva Sehgal, and John Bogovic for helpful discussions. This work was
supported by the Janelia Visiting Scientists program, the Howard Hughes Medical Institute,
and the National Science Foundation (IIS-2505098).

References
Allen Institute. Allen Brain Observatory: Visual Behavior 2P Technical Whitepaper.
Technical report, Allen Institute for Brain Science, March 2021.
URL
https://brainmapportal-live-4cc80a57cd6e400d854-f7fdcae.divio-media.net/
filer public/4e/be/4ebe2911-bd38-4230-86c8-01a86cfd758e/visual behavior 2p
technical whitepaper.pdf. V1.0.
Dario Amodei. Machines of loving grace: How AI could transform the world for the better.
https://darioamodei.com/essay/machines-of-loving-grace, 2024. Accessed: 2026.
Dora Angelaki, Brandon Benson, Julius Benson, Daniel Birman, Niccolò Bonacchi, Kcénia
Bougrova, Sebastian A Bruijns, Matteo Carandini, Joana A Catarino, et al. A brain-wide
map of neural activity during complex behaviour. Nature, 645(8079):177–191, 2025.
Eser Aygün, Anastasiya Belyaeva, Gheorghe Comanici, Marc Coram, Hao Cui, Jake Garrison,
Renee Johnston Anton Kast, Cory Y. McLean, Peter Norgaard, Zahra Shamsi, David
Smalling, James Thompson, Subhashini Venugopalan, Brian P. Williams, Chujun He, Sarah
Martinson, Martyna Plomecka, Lai Wei, Yuchen Zhou, Qian-Ze Zhu, Matthew Abraham,
Erica Brand, Anna Bulanova, Jeffrey A. Cardille, Chris Co, Scott Ellsworth, Grace Joseph,
Malcolm Kane, Ryan Krueger, Johan Kartiwa, Dan Liebling, Jan-Matthis Lueckmann, Paul
Raccuglia, Xuefei, Wang, Katherine Chou, James Manyika, Yossi Matias, John C. Platt,
Lizzie Dorfman, Shibl Mourad, and Michael P. Brenner. An ai system to help scientists
write expert-level empirical software, 2025. URL https://arxiv.org/abs/2509.06503.
Andres M Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D White, and Philippe
Schwaller. Chemcrow: Augmenting large-language models with chemistry tools, 2023.
URL https://arxiv.org/abs/2304.05376.
Kristin Branson, Alice Robie, John Bender, Pietro Perona, and Michael H. Dickinson. Highthroughput ethomics in large groups of Drosophila. Nature Methods, 6(7):451–457, 2009.
doi: 10.1038/nmeth.1328.
Anne E. Carpenter, Thouis R. Jones, Michael R. Lamprecht, Colin Clarke, In Han Kang, Ola
Friman, David A. Guertin, Joo Han Chang, Robert A. Lindquist, Jason Moffat, Polina
Golland, and David M. Sabatini. Cellprofiler: image analysis software for identifying
and quantifying cell phenotypes. Genome Biology, 7(10):R100, 2006. ISSN 1474-760X. doi:
10.1186/gb-2006-7-10-r100. URL https://doi.org/10.1186/gb-2006-7-10-r100.
Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li,
Zeyi Liao, Chen Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N. Baker, Benjamin
Burns, Daniel Adu-Ampratwum, Xuhui Huang, Xia Ning, Song Gao, Yu Su, and Huan
Sun. Scienceagentbench: Toward rigorous assessment of language agents for data-driven
scientific discovery, 2025. URL https://arxiv.org/abs/2410.05080.
Hui Chiu, Alice A Robie, Kristin Branson, Tanvi Vippa, Samantha Epstein, Gerald M
Rubin, David J Anderson, and Catherine E Schretter. Cell type-specific contributions to a
persistent aggressive internal state in female Drosophila. eLife, 12:RP88598, jul 2025. ISSN
2050-084X. doi: 10.7554/eLife.88598. URL https://doi.org/10.7554/eLife.88598.
Erna Eyjolfsdottir, Steve Branson, Xavier P. Burgos-Artizzu, Eric D. Hoopfer, Jeremy Schor,
David J. Anderson, and Pietro Perona. Detecting social actions of fruit flies. In David
Fleet, Tomas Pajdla, Bernt Schiele, and Tinne Tuytelaars (eds.), Computer Vision – ECCV

2014, volume 8690 of Lecture Notes in Computer Science, pp. 772–787, Cham, 2014. Springer.
doi: 10.1007/978-3-319-10605-2 50.
Ali Essam Ghareeb, Benjamin Chang, Ludovico Mitchener, Angela Yiu, Caralyn J.
Szostkiewicz, Jon M. Laurent, Muhammed T. Razzak, Andrew D. White, Michaela M.
Hinks, and Samuel G. Rodriques. Robin: A multi-agent system for automating scientific
discovery, 2025. URL https://arxiv.org/abs/2505.13400.
Juraj Gottweis, Wei-Hung Weng, Alexander Daryin, Tao Tu, Anil Palepu, Petar Sirkovic,
Artiom Myaskovsky, Felix Weissenberger, Keran Rong, Ryutaro Tanno, Khaled Saab, Dan
Popovici, Jacob Blum, Fan Zhang, Katherine Chou, Avinatan Hassidim, Burak Gokturk,
Amin Vahdat, Pushmeet Kohli, Yossi Matias, Andrew Carroll, Kavita Kulkarni, Nenad
Tomasev, Yuan Guan, Vikram Dhillon, Eeshit Dhaval Vaishnav, Byron Lee, Tiago R D
Costa, José R Penadés, Gary Peltz, Yunhan Xu, Annalisa Pawlosky, Alan Karthikesalingam,
and Vivek Natarajan. Towards an ai co-scientist, 2025. URL https://arxiv.org/abs/
2502.18864.
Mourad Gridach, Jay Nanavati, Khaldoun Zine El Abidine, Lenon Mendes, and Christina
Mack. Agentic ai for scientific discovery: A survey of progress, challenges, and future
directions, 2025. URL https://arxiv.org/abs/2503.08979.
Ken Gu, Ruoxi Shang, Ruien Jiang, Keying Kuang, Richard-John Lin, Donghe Lyu, Yue Mao,
Youran Pan, Teng Wu, Jiaqian Yu, Yikun Zhang, Tianmai M. Zhang, Lanyi Zhu, Mike A.
Merrill, Jeffrey Heer, and Tim Althoff. Blade: Benchmarking language model agents for
data-driven science, 2025a. URL https://arxiv.org/abs/2408.09667.
Ken Gu, Ruoxi Shang, Ruien Jiang, Keying Kuang, Richard-John Lin, Donghe Lyu, Yue Mao,
Youran Pan, Teng Wu, Jiaqian Yu, Yikun Zhang, Tianmai M. Zhang, Lanyi Zhu, Mike A.
Merrill, Jeffrey Heer, and Tim Althoff. Blade: Benchmarking language model agents for
data-driven science, 2025b. URL https://arxiv.org/abs/2408.09667.
Sikun Guo, Amir Hassan Shariatmadari, Guangzhi Xiong, Albert Huang, Eric Xie, Stefan
Bekiranov, and Aidong Zhang. Ideabench: Benchmarking large language models for
research idea generation, 2024. URL https://arxiv.org/abs/2411.02429.
Kexin Huang, Serena Zhang, Hanchen Wang, Yuanhao Qu, Yingzhou Lu, Yusuf Roohani,
Ryan Li, Lin Qiu, Gavin Li, Junze Zhang, et al. Biomni: A general-purpose biomedical ai
agent. biorxiv, 2025.
Peter Jansen, Marc-Alexandre Côté, Tushar Khot, Erin Bransom, Bhavana Dalvi Mishra,
Bodhisattwa Prasad Majumder, Oyvind Tafjord, and Peter Clark.
Discoveryworld: A virtual environment for developing and evaluating automated scientific
discovery agents. In A. Globerson, L. Mackey, D. Belgrave, A. Fan, U. Paquet,
J. Tomczak, and C. Zhang (eds.), Advances in Neural Information Processing Systems, volume 37, pp. 10088–10116. Curran Associates, Inc., 2024. doi: 10.52202/
079017-0324. URL https://proceedings.neurips.cc/paper files/paper/2024/file/
13836f251823945316ae067350a5c366-Paper-Datasets and Benchmarks Track.pdf.
Mayank Kabra, Alice A. Robie, Marta Rivera-Alba, Steven Branson, and Kristin Branson.
JAABA: interactive machine learning for automatic annotation of animal behavior. Nature
Methods, 10(1):64–67, January 2013. ISSN 1548-7105. doi: 10.1038/nmeth.2281. URL
https://www.nature.com/articles/nmeth.2281. Publisher: Nature Publishing Group.
Mayank Kabra, Allen Lee, Alice Robie, Roian Egnor, Stephen Huston, Ivan Felipe Rodriguez,
Austin Edwards, and Kristin Branson. APT: Animal Part Tracker v0.3.4. Zenodo, March
2022.
Yuhang Lai, Chengxi Li, Yiming Wang, Tianyi Zhang, Ruiqi Zhong, Luke Zettlemoyer,
Wen-Tau Yih, Daniel Fried, Sida Wang, and Tao Yu. Ds-1000: A natural and reliable
benchmark for data science code generation. ArXiv, abs/2211.11501, 2022.

Jon M. Laurent, Joseph D. Janizek, Michael Ruzo, Michaela M. Hinks, Michael J. Hammerling, Siddharth Narayanan, Manvitha Ponnapati, Andrew D. White, and Samuel G.
Rodriques. Lab-bench: Measuring capabilities of language models for biology research,
2024. URL https://arxiv.org/abs/2407.10362.
Chris Lu, Cong Lu, Robert Tjarko Lange, Yutaro Yamada, Shengran Hu, Jakob Foerster,
David Ha, and Jeff Clune. Towards end-to-end automation of AI research. Nature, 651
(8107):914–919, 2026. ISSN 1476-4687. doi: 10.1038/s41586-026-10265-5. URL https:
//doi.org/10.1038/s41586-026-10265-5.
Bodhisattwa Prasad Majumder, Harshit Surana, Dhruv Agarwal, Bhavana Dalvi Mishra,
Abhijeetsingh Meena, Aryan Prakhar, Tirth Vora, Tushar Khot, Ashish Sabharwal, and
Peter Clark. Discoverybench: Towards data-driven discovery with large language models,
2024a. URL https://arxiv.org/abs/2407.01725.
Bodhisattwa Prasad Majumder, Harshit Surana, Dhruv Agarwal, Bhavana Dalvi Mishra,
Abhijeetsingh Meena, Aryan Prakhar, Tirth Vora, Tushar Khot, Ashish Sabharwal, and
Peter Clark. Discoverybench: Towards data-driven discovery with large language models,
2024b. URL https://arxiv.org/abs/2407.01725.
Alexander Mathis, Pranav Mamidanna, Kevin M Cury, Taiga Abe, Venkatesh N Murthy,
Mackenzie Weygandt Mathis, and Matthias Bethge. Deeplabcut: markerless pose estimation of user-defined body parts with deep learning. Nature neuroscience, 21(9):1281–1289,
2018.
Geoffrey W Meissner, Aljoscha Nern, Zachary Dorman, Gina M DePasquale, Kaitlyn Forster,
Theresa Gibney, Joanna H Hausenfluck, Yisheng He, Nirmala A Iyer, Jennifer Jeter,
Lauren Johnson, Rebecca M Johnston, Kelley Lee, Brian Melton, Brianna Yarbrough,
Christopher T Zugates, Jody Clements, Cristian Goina, Hideo Otsuna, Konrad Rokicki,
Robert R Svirskas, Yoshinori Aso, Gwyneth M Card, Barry J Dickson, Erica Ehrhardt, Jens
Goldammer, Masayoshi Ito, Dagmar Kainmueller, Wyatt Korff, Lisa Mais, Ryo Minegishi,
Shigehiro Namiki, Gerald M Rubin, Gabriella R Sterne, Tanya Wolff, Oz Malkesman, and
FlyLight Project Team. A searchable image resource of Drosophila gal4 driver expression
patterns with single neuron resolution. eLife, 12:e80660, feb 2023. ISSN 2050-084X. doi:
10.7554/eLife.80660. URL https://doi.org/10.7554/eLife.80660.
Ludovico Mitchener, Angela Yiu, Benjamin Chang, Mathieu Bourdenx, Tyler Nadolski,
Arvis Sulovari, Eric C. Landsness, Daniel L. Barabasi, Siddharth Narayanan, Nicky Evans,
Shriya Reddy, Martha Foiani, Aizad Kamal, Leah P. Shriver, Fang Cao, Asmamaw T.
Wassie, Jon M. Laurent, Edwin Melville-Green, Mayk Caldas, Albert Bou, Kaleigh F.
Roberts, Sladjana Zagorac, Timothy C. Orr, Miranda E. Orr, Kevin J. Zwezdaryk, Ali E.
Ghareeb, Laurie McCoy, Bruna Gomes, Euan A. Ashley, Karen E. Duff, Tonio Buonassisi,
Tom Rainforth, Randall J. Bateman, Michael Skarlinski, Samuel G. Rodriques, Michaela M.
Hinks, and Andrew D. White. Kosmos: An ai scientist for autonomous discovery, 2025.
URL https://arxiv.org/abs/2511.02824.
Marius Pachitariu, Carsen Stringer, Sylvia Schröder, Mario Dipoppa, L Federico Rossi,
Matteo Carandini, and Kenneth D Harris. Suite2p: beyond 10,000 neurons with standard
two-photon microscopy. BioRxiv, pp. 061507, 2016.
Marius Pachitariu, Shashwat Sridhar, and Carsen Stringer. Solving the spike sorting problem
with kilosort. bioRxiv, 2023. doi: 10.1101/2023.01.07.523036. URL https://www.biorxiv.
org/content/early/2023/01/07/2023.01.07.523036.
Yuanhao Qu, Kaixuan Huang, Ming Yin, Kanghong Zhan, Dyllan Liu, Di Yin, Henry C
Cousins, William A Johnson, Xiaotong Wang, Mihir Shah, et al. Crispr-gpt for agentic
automation of gene-editing experiments. Nature Biomedical Engineering, pp. 1–14, 2025.
Alice A. Robie, Jonathan Hirokawa, Austin W. Edwards, Lowell A. Umayam, Allen Lee,
Mary L. Phillips, Gwyneth M. Card, Wyatt Korff, Gerald M. Rubin, Julie H. Simpson,
Michael B. Reiser, and Kristin Branson. Mapping the Neural Substrates of Behavior.
Cell, 170(2):393–406.e28, July 2017. ISSN 0092-8674, 1097-4172. doi: 10.1016/j.cell.2017.

06.032. URL https://www.cell.com/cell/abstract/S0092-8674(17)30716-X. Publisher:
Elsevier.
Alice A. Robie, Adam L. Taylor, Catherine E. Schretter, Mayank Kabra, and Kristin Branson.
The Fly Disco: Hardware and software for optogenetics and fine-grained fly behavior
analysis, November 2024. URL https://www.biorxiv.org/content/10.1101/2024.11.04.
621948v1. Pages: 2024.11.04.621948 Section: New Results.
Yusuf Roohani, Andrew Lee, Qian Huang, Jian Vora, Zachary Steinhart, Kexin Huang,
Alexander Marson, Percy Liang, and Jure Leskovec. Biodiscoveryagent: An ai agent for
designing genetic perturbation experiments, 2025. URL https://arxiv.org/abs/2405.
17631.
Gerald M Rubin, Claire Managan, Marisa Dreher, Elizabeth Kim, Scott Miller, Kaitlyn Boone,
Alice A Robie, Adam L Taylor, Kristin Branson, Catherine E Schretter, et al. Networks
of sexually dimorphic neurons that regulate social behaviors in drosophila. bioRxiv, pp.
2025–10, 2025.
Amanpreet Singh, Joseph Chee Chang, Chloe Anastasiades, Dany Haddad, Aakanksha Naik,
Amber Tanaka, Angele Zamarron, Cecile Nguyen, Jena D. Hwang, Jason Dunkleberger,
Matt Latzke, Smita Rao, Jaron Lochner, Rob Evans, Rodney Kinney, Daniel S. Weld,
Doug Downey, and Sergey Feldman. Ai2 scholar qa: Organized literature synthesis with
attribution, 2025. URL https://arxiv.org/abs/2504.10861.
Giulio Starace, Oliver Jaffe, Dane Sherburn, James Aung, Jun Shern Chan, Leon Maksin,
Rachel Dias, Evan Mays, Benjamin Kinsella, Wyatt Thompson, Johannes Heidecke, Amelia
Glaese, and Tejal Patwardhan. Paperbench: Evaluating ai’s ability to replicate ai research,
2025. URL https://arxiv.org/abs/2504.01848.
Sijun Tan, Siyuan Zhuang, Kyle Montgomery, William Yuan Tang, Alejandro Cuadron,
Chenguang Wang, Raluca Popa, and Ion Stoica. Judgebench: A benchmark for evaluating
LLM-based judges. In The Thirteenth International Conference on Learning Representations,
2025. URL https://openreview.net/forum?id=G0dksFayVq.
Aman Singh Thakur, Kartik Choudhary, Venkat Srinik Ramayapally, Sankaran
Vaidyanathan, and Dieuwke Hupkes. Judging the judges: Evaluating alignment and
vulnerabilities in LLMs-as-judges. In Ofir Arviv, Miruna Clinciu, Kaustubh Dhole, Rotem
Dror, Sebastian Gehrmann, Eliya Habba, Itay Itzhak, Simon Mille, Yotam Perlitz, Enrico
Santus, João Sedoc, Michal Shmueli Scheuer, Gabriel Stanovsky, and Oyvind Tafjord
(eds.), Proceedings of the Fourth Workshop on Generation, Evaluation and Metrics (GEM²), pp.
404–430, Vienna, Austria and virtual meeting, July 2025. Association for Computational
Linguistics. ISBN 979-8-89176-261-9. URL https://aclanthology.org/2025.gem-1.33/.
The International Brain Laboratory.
Data Release – Brainwide Map – Q4 2022.
figshare preprint, 2022. URL https://figshare.com/articles/preprint/Data release
- Brainwide map - Q4 2022/21400815. Version 7, updated 2024-09-19.
Alistair Turcan, Kexin Huang, Lei Li, and Martin Jinye Zhang. Tusoai: Agentic optimization
for scientific methods, 2025. URL https://arxiv.org/abs/2509.23986.
Xuefei Wang, Kai A. Horstmann, Ethan Lin, Jonathan Chen, Alexander R. Farhang, Sophia
Stiles, Atharva Sehgal, Jonathan Light, David Van Valen, Yisong Yue, and Jennifer J. Sun.
Simple agents outperform experts in biomedical imaging workflow optimization. In
Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR),
pp. 13680–13690, June 2026.
Johan Winnubst, Erhan Bas, Tiago A Ferreira, Zhuhao Wu, Michael N Economo, Patrick
Edson, Ben J Arthur, Christopher Bruns, Konrad Rokicki, David Schauder, et al. Reconstruction of 1,000 projection neurons reveals new cell types and organization of long-range
connectivity in the mouse brain. Cell, 179(1):268–281, 2019.
Ling-Qi Zhang and Kristin Branson. Neurodata without boredom: Benchmarking agentic ai
for data reuse, 2026. URL https://arxiv.org/abs/2605.12808.

Zhihao Zheng, J Scott Lauritzen, Eric Perlman, Camenzind G Robinson, Matthew Nichols,
Daniel Milkie, Omar Torrens, John Price, Corey B Fisher, Nadiya Sharifi, et al. A complete
electron microscopy volume of the brain of adult drosophila melanogaster. Cell, 174(3):
730–743, 2018.
LLM usage statement. We used LLMs to assist with iterating on figure design and editing
prose for clarity and concision. All scientific content, analyses, and conclusions are the
authors’ own.

Appendix Contents
• Appendix A: Details on task design
• Appendix B: Task-specific evaluation criteria
• Appendix C: Tolerance sensitivity analysis
• Appendix D: Scientist reference solutions
• Appendix E: Task inputs and abilities evaluated
• Appendix F: Iteration behavior
• Appendix G: Example agent outputs
• Appendix H: Token usage and runtimes
• Appendix I: Measuring task size
• Appendix J: Prompts

A

Details on task design

To ensure consistent prompt composition across tasks, each prompt contains the following
components:
• Time limit for task completion.
• Data specification: Location and structure of input files and required task outputs (data
files, code, and requirements.txt).
• Task description: Main objective of task.
• Domain context: Any domain-specific context or terms required to succeed on the task.
Does not include general domain knowledge.
• Success criteria: Description of how agent solution will be evaluated; e.g. what metrics
will be used.
• Implementation notes: Task-specific notes critical for success, such as different indexing
conventions between different data types.
Tasks are provided with data corresponding to a set of 3 out of a total 44 videos or 3
experimental conditions out of a total 11, depending on the task. They are evaluated on the
full set of data.
For all tasks, evaluation criteria include the following:
• Output existence checks: Checks if all required outputs are present.
• Evaluation on test data: The agent’s solution script is run on a large set of evaluation data,
typically consisting of 44 experimental inputs, of which the agent was given a subset of 3
reference inputs for development.
• Validity checks: Checks that all required output data are created by running the agent’s
code on the test data.
• Task-specific evaluation: rigorous checks that quantitatively assess the correctness of the
agent’s solution.
Below, we describe task-specific design considerations and iterations for each pipeline stage,
which motivated our general task design principles (§ 3).
A.1

The input videos use a custom format (UFMF), requiring helper code to interface with them.
Initial prompts described all helper files provided to the agent, when only the top-level
movie interface needed to be accessed directly; the rest were its dependencies. This led
agents to spend significant effort parsing the details of the UFMF format rather than focusing
on the core tracking task. We updated the prompt to remove explanations of these auxiliary
files, which prevented agents from getting distracted by implementation details irrelevant
to the task objective.

A.2

The registration task produces newly created trajectories that are split from existing ones
when tracking gaps occur. The original prompt required these trajectories to be ordered
temporally in a specific way—a constraint that served no scientific purpose but simplified
evaluation by enabling direct comparison against ground truth. This is not something
a scientist would need, and unnecessarily constrained the task definition. We removed
this restriction from the prompt and instead made evaluation robust by using Hungarian
matching to align agent trajectories with ground truth before comparison. Separately, we
found that agents were consistently failing the evaluation on specific experiments; closer
visual inspection revealed that the ground truth registration itself was incorrect due to
flipped coordinates.
A.3

The original prompt did not specify success or evaluation criteria. Agent solutions tended
to be poor and did not meet the accuracy required for downstream leg movement analysis.
We updated the prompt to include the evaluation metric—Euclidean percentile error—and
a target threshold which corresponded to the evaluation cutoff for passing. After this
change, we observed agents referencing the target in their reasoning and checking their
own performance against it during development.
A.4

Behavior Feature Computation

This task required significant iteration on both prompts and evaluation. Initial prompts
were underspecified in subtle ways: for example, velocity features produce n − 1 frames
of output, but without explicit specification, agents applied different padding conventions.
We added concrete details about expected output array sizes to resolve such ambiguities.
The iteration process also uncovered a bug in the ground truth code where angle flips
were computed incorrectly, as well as errors in the scientist’s feature definitions that had
survived multiple rounds of peer review. On the evaluation side, we found that agents were
consistently failing on certain features (corfrac maj, corfrac min); investigation revealed
that our evaluation criteria were too strict rather than the agent solutions being incorrect.
Similarly, failures on absdv cor stemmed from its dependency on the corfrac features.
We created separate test cases for these features with tailored tolerances to evaluate them
independently. Two independent reviewers checking the prompt and evaluation proved
valuable for catching such issues.
A.5

When designing the task in collaboration with a domain expert, early prompts referenced
the scientist’s specific algorithmic approach of per-leg thresholding with hysteresis. This
had the undesired effect of constraining agents to heuristic methods rather than exploring
alternatives. After removing algorithmic suggestions, agent solutions became more varied,
including learning-based approaches.
A.6

Initial prompts lacked information about what constitutes a sample in the Mann-Whitney
U-test, leaving agents to make varying and sometimes valid choices about how to pool
data. We updated the prompt to specify how samples are constructed for evaluation. On
the evaluation side, we introduced tolerance around p-value boundaries to accommodate
minor numerical differences that do not affect statistical conclusions. We also discovered
that the ground truth made an implicit assumption about filtering bouts not contained in
the OFF/ON stimulation period—an assumption agents tended not to make. We updated
the ground truth to remove this filtering, ensuring agents were not penalized for omitting
an unstated step.

Task-specific evaluation criteria

For each task, we define a per-experiment ratio r (e) ≥ 0 where r (e) ≥ 1 indicates the agent
passes experiment e. We grade each trial using the distribution of ratios across experiments:
• Green (✓): P5 (r ) ≥ 1 — at least 95% of experiments pass.
• Yellow (∼): E[r ] ≥ 1 but P5 (r ) < 1 — passes on average but not consistently.
• Red (×): E[r ] < 1 — fails on average.
where P5 denotes the 5th percentile. For multi-criteria tasks (Registration, Behavior Feature
Computation), the per-experiment ratio is the minimum across all criteria: r (e) = minc rc (e).
The task score reported in Table 1 is Et,e [r ], averaged over trials t and experiments e. For
multi-criteria tasks, the score uses a mean-of-means: each criterion is averaged across
experiments, then averaged across criteria (capped at 2).
Sources of scientist reference solutions and ground-truth labels for each task, where applicable, are detailed in § D.
B.1

For a given experimental video e, the agent passes if
MOTAagent (e) ≥ MOTAbaseline (e).

(1)

Let v(e) = 1 if the agent’s output trajectory file is well-formed (required fields are present
with the expected shapes and the per-target frame counts, offsets, and time deltas are
internally consistent), and v(e) = 0 otherwise. The per-experiment ratio and task score are:
r (e) = v(e) ·
B.2

1 − MOTAbaseline (e)
1 − MOTAagent (e)

score = Et,e [r ].

(2)

Registration is evaluated on multiple criteria per experiment. For each criterion c, the ratio
is rc (e) = τc /ϵc (e) where τc is the tolerance and ϵc (e) is the agent’s error. The criteria are:
• Scale consistency: r = (δscale · ŝ) / range(ŝ), where ŝ is the estimated pixels-per-mm
and δscale = 10−5 .
• Radius error: r = τradius / | R̂ − RGT |, with τradius = 2.5 px.
• Center consistency (x and y): r = δcenter / rangerel (ĉ), with δcenter = 0.01.
• Center error: r = τcenter / ∥ĉ − cGT ∥, with τcenter = 5.0 px.
• Max/mean residuals (per coordinate field f ∈ { x, y, a, b, θ }): r = τ f / residual f .
Let v(e) = 1 if the registered output is well-formed (required fields present, no NaN values,
array lengths consistent) and its millimeter and pixel coordinate representations agree
under the agent’s reported pixels-per-mm scale, and v(e) = 0 otherwise. The agent passes
experiment e if v(e) · minc rc (e) ≥ 1. The task score uses a mean-of-means:
Ee [v(e) · min(2, rc (e))] .
(3)
score = Et
|C | ∑
c
B.3

The agent trains a keypoint detection model evaluated on held-out test data. The agent
passes if its mean error percentile is within a tolerance of the baseline:
ϵ̄agent ≤ α · ϵ̄baseline ,

(4)

where α = 1.5 is the pass fraction. The ratio and score are:
r=

α · ϵ̄baseline
ϵ̄agent

score = Et [r ].

(5)

B.4

Behavior Feature Computation

Per-frame features are compared against a baseline. For each feature f and experiment e,
the ratio depends on the feature type:
• Standard features (13 features): r f (e) = τ f (e) / MAE f (e), where τ f (e) = δz · σ f (e)
with δz = 0.01.
• Absolute consistency (absdv cor): r = 1 if |absdv cor| = |dv cor| (within floatingpoint tolerance), else r = 0.
• Body-coordinate fraction (corfrac maj, corfrac
min, evaluated jointly): r =

ε / maxi,t max 0, Lagent (i, t) − Lbaseline (i, t) with ε = 10−3 , where L(i, t) is the
squared error of the body-translation reconstruction at frame t of fly i using the
predicted corfrac values and the tracked body axis.
The agent passes experiment e if all features pass: min f r f (e) ≥ 1. The task score uses a
mean-of-means:
h
score = Et
Ee min(2, r f (e)) .
(6)
| F| ∑
f
B.5

Behavior Classifier

The agent trains a walking behavior classifier evaluated on held-out test data. The agent
passes if its balanced accuracy meets a threshold derived from the baseline:
BAagent ≥ α · BAbaseline ,

(7)

where α = 0.95. The ratio and score are:
r=
B.6

1 − α · BAbaseline
1 − BAagent

score = Et [r ].

(8)

For each experimental video e, the agent’s per-frame swing/stance predictions are scored
against the scientist’s reference algorithm output using bout-level balanced accuracy. The
baseline accuracy is the same metric applied to the scientist’s predictions against manually
annotated ground-truth labels, with:

BAagent (e) = bout-BA ŷagent (e), ŷscientist (e) ,
(9)
and

BAbaseline (e) = bout-BA(ŷscientist (e), y∗ (e)) ,

(10)

where ŷagent (e), ŷscientist (e) are the predicted swing/stance labels and y∗ (e) are the manual
labels. Bout-level balanced accuracy averages, over each contiguous label bout (per fly, per
leg), the fraction of frames labeled correctly, then takes the unweighted mean across the two
classes (swing, stance) to balance class frequencies. The agent passes if:
BAagent (e) ≥ α · BAbaseline (e),

(11)

with pass fraction α = 0.95. The ratio and score are:
r (e) =
B.7

1 − α · BAbaseline (e)
1 − BAagent (e)

score = Et,e [r ].

(12)

For each genetic line ℓ, the agent computes p-values for whether a treatment affects walking
speed in slow and fast phases. The agent’s significance calls sℓ,ϕ,α are compared against
the ground truth s∗ℓ,ϕ,α for ϕ ∈ {slow, fast} and α ∈ {0.05, 0.01, 0.001}. To avoid penalizing

borderline cases, a call is judged correct if either the significance flag matches or the submitted
p-value is within 10% of ground truth:




h
pℓ,ϕ pℓ,ϕ
cℓ,ϕ,α = 1 sℓ,ϕ,α = sℓ,ϕ,α ∨ 1 max p∗ , p
≤ 1 + δp ,
(13)
ℓ,ϕ

ℓ,ϕ

with tolerance δp = 0.1. The per-line ratio is
hV
r (ℓ) = 1 ϕ,α cℓ,ϕ,α ,

(14)

i.e., r (ℓ) = 1 iff all phases and all α levels are correct for line ℓ, and r (ℓ) = 0 otherwise.
Grading uses a custom scheme:
• Green: All lines correct for all phases and all α levels (minℓ r (ℓ) = 1).
• Yellow: All lines correct for both phases at α = 0.05.
• Red: Otherwise.
The task score is the fraction of lines correct, averaged over trials:
score = Et,ℓ [r (ℓ)].

(15)

C

Tolerance sensitivity analysis

ϵ-Scale

Tracking*
Tracking Computation Classifier Segmentation Comparison

Single-stage tasks

1.917±0.137

1.101±0.044

1.761±0.000

1.962±0.093

0.352±0.302

0.017±0.003

1.928±0.125

1.376±0.055

2.281±0.108

0.451±0.387

0.061±0.009

1.943±0.099

2.752±0.111

1.933±0.000

2.921±0.139

0.649±0.556

1.985±0.021

1.084±0.229

1.761±0.000

1.004±0.340

0.726±0.030

0.020±0.006

1.999±0.002

1.355±0.286

1.167±0.396

0.929±0.039

0.068±0.015

2.711±0.572

1.933±0.000

1.494±0.507

1.337±0.055

0.767±0.404

1.997±0.000

1.097±0.036

1.756±0.009

2.884±0.876

0.938±0.176

0.044±0.022

1.371±0.046

1.851±0.006

3.354±1.019

1.201±0.225

0.175±0.095

2.742±0.091

1.931±0.004

4.295±1.304

1.728±0.324

1.864±0.088

0.371±0.294

1.598±0.283

1.084±0.201

0.533±0.099

0.005±0.008

1.892±0.090

0.464±0.367

1.662±0.334

1.260±0.233

0.682±0.127

0.016±0.028

1.922±0.086

0.929±0.734

1.717±0.374

1.614±0.299

0.981±0.183

1.862±0.053

0.562±0.512

0.020±0.002

✓××

0.071±0.006

1.970±0.028

1.405±1.280

1.917±0.046

0.197±0.342

✓××

0.039±0.038

0.979±0.848

1.458±1.263

0.966±1.673

0.153±0.160

1.961±0.065

0.493±0.854

1.438±2.491

Table 2: Sensitivity of task grades to evaluation-threshold scaling. Each row evaluates
the same submissions with task-specific ϵ scaled by 0.5×, 1×, or 2×. Symbols show the
outcomes of the three trials in each setting. Here, ✓ indicates P5 (r ) ≥ 1, and × indicates
P5 (r ) < 1. Across all 96 trials, 92% retain the same pass/fail classification when the
tolerance is relaxed from ϵ to 2ϵ, and 88% retain the same classification when tightened
to ϵ/2. Together, these results indicate that most trials are not near the decision boundary
and that the main conclusions are robust to reasonable variation in evaluation thresholds.
Numbers report mean task score ± standard deviation. Dashes indicate stages not evaluated
in the corresponding end-to-end setting. *For Body Tracking, where ϵ = 0 and multiplicative
scaling would leave the threshold unchanged, the 0.5× and 2× settings instead correspond
to ϵ − 0.05 and ϵ + 0.05, respectively.

D

Scientist reference solutions

Scientist reference solution source Additional ground-truth labels

Ctrax fly tracker (Branson et al.,
2009)

Annotations initialized with FlyTracker
(Eyjolfsdottir et al., 2014) and manually
corrected by domain scientists.

Fly Disco (Robie et al., 2024)

Animal Part Tracker (APT) (Kabra
et al., 2022)

MultiFly keypoint dataset (Robie et al.,
2024)

(Robie et al., 2017)

JAABA (Kabra et al., 2013)

Behavior category labels (Robie et al.,
2024)

Fly Disco (Robie et al., 2024)

Written by a domain scientist
author of this paper.

Table 3: Sources of scientist reference solutions and ground-truth labels for each task. As
discussed in § 3.1, task evaluations are based on community-accepted scientist baselines
derived from scientific publications and, where available, additional ground truth labels.
The source for each is detailed here.

Task inputs and abilities evaluated

Goal

Information
provided*

Abilities evaluated

Body Tracking Develop an
algorithm to detect
and track multiple
flies in raw video.

Raw videos, code for
reading video. No
reference algorithm, no
ground-truth labels, no
optimizable criterion.

Image processing, multi-target tracking, evaluation criteria
development. Agents must apply visual knowledge of fly
appearance to detect each fly’s position and orientation
(including when flies touch), and assign consistent
identities across frames. As no criterion or labels are
given, agents must develop their own evaluation criteria.
Their method must generalize to unseen videos.

Develop a method
to spatially align
tracked data to a
canonical
coordinate system,
then clean the data
by removing NaNs.

Tracked trajectories
from Body Tracking,
code for loading
trajectories. Arena
radius in mm. No
labeled examples, no
boundary detection
algorithm.

Image processing, coordinate transformation, data cleaning.
Agents must determine how to detect the boundary of
the arena, an image processing task, then use the given
arena radius to transform the trajectories produced by
Body Tracking from pixels to millimeters, centered on
the arena center. Although agents are provided data for
algorithm development, their algorithms must
generalize to unseen data.

Train a supervised
keypoint detection
model from
provided training
data.

Labeled training
images in COCO
format. Target
accuracy thresholds.
No algorithmic details.

Machine learning, model training, computer vision. Agents
must design and train a machine learning model that
can predict keypoint locations from images given
labeled training data. This is a common computer vision
task, with the marked difference of the high precision
required: sub-precision accuracy on average, and small
error for outliers, as required for downstream analysis
tasks. Agents are provided accuracy goals, and must
design an algorithm tuned to data properties and this
high precision goal.

Implement a
program to
compute
pre-defined
features from
trajectories given
equations.

Feature definitions as
PDF or TeX, code for
loading trajectories.

Implementation, geometry. Agents must translate
equations to code; two features additionally require
geometric reasoning to find a described optimum.

Walking

Train a walking
behavior classifier
from manually
labeled trajectories.

Sparse manual labels,
trajectory and behavior
feature files
(heterogeneous
formats), no
algorithmic details.

Machine learning, action recognition. Agents must design
and train a time-series-based classifier given sparse
labels, and build a data loader that correctly aligns
indices across heterogeneous files.

Segmentation

Develop a method
to segment walking
into swing and
stance gait phases
from tracked poses.

A few manually
labeled swing/stance
examples (too few to
train a generic
classifier), keypoint
definitions in
entomology
terminology. No
algorithmic details.

Domain knowledge, walking gait analysis, parameter tuning.
Agents must apply domain knowledge of gait
definitions, interpret entomological keypoint
terminology, and tune parameters from the provided
examples.

Conduct
Mann-Whitney U
tests to evaluate
whether
optogenetic
perturbation affects
stance duration.

Data from multiple
sources, three p-value
thresholds, statistical
sample definition, type
of statistical test.

Data integration, statistical testing. Agents must combine
and align data across sources, pool across time and flies
to construct pseudo-independent samples, and run
significance tests at the specified thresholds.

Table 4: Expanded description of our tasks, distinguishing the information provided to agents from
the abilities required to obtain a passing solution. *In all tasks, agents are provided the input and
output data format.

F

Iteration behavior

PBRYbga
XjxX8a6

Fly body tracking

zYCQWpQ
F9C4QDk
DE8pkaq
mx8Yptv
HAzrxMV
9ZvtpVs

GzGR3Vz
YxLMfgN
p7Mjj9t
gjskC39

cixXNXE
cWMVTK3

x5uQ63f
vE8kFvZ
tubqmP2
i8uRg2Q
HEPGczK
xNJnk2o
gr4iXxi
zZMfrKG

DYyw822

Normalized within-trial solution rank
(0 = trial worst, 1 = trial best)

dqvAdDy

s5oREo9
gpABbVS

Keypoint tracking

uZnetSw
3kUeHF5
3S6nZBB

R3AQ55X
RimyDJR
FCNJeZh
tZCcc6q
cTfpzyB
ZS6JjBb
aWkDwr8

LTA2Zg6
5xoFcz2

Behavior feature
computation

QPHYpDN
Fv5mcBL
W8mnrtu
TxRKnPW
bQ9TS8w
a9f6fYY
w26tL9D
rA3yuSi
qakL4bM
uBAJ6mM

ftrCd3k
oC4oKt5

Walking behavior
classification

dV3TevZ
jtnQMDa
C7BXMqy
35vwujF
kVSDKMn
gJUy9L5
wbFQS3E
wZuYpGB
y8mCCT4
nQdVKtZ

nTga8kJ

Gait segmentation

FgnndtM
RVYvvV6
R2LhGFW
j66WXwn
iAQRuzc
sL3nLdv
mr6ovRR
YWNPppK
tShGAQy
Xttemp8
5qLnMws

nTiRaLK

Statistical comparison

JCZfPQr
SWbXTW6
GXe27ih
ochidDe
ZGmChcn
aEyMu38
Fcfds8P
7VxaEqH
7bUUZcq
7U63Xxj
CY8jXGv

Fraction of trajectory steps (per trial); red ticks = image-view calls

Visualization action

Figure 6: Per-trial iteration trajectories for all tasks and their respective trials. To obtain the segmentation of a trajectory into individual iterations, each step of each trajectory was classified with the
aid of an LLM judge to identify the steps in which qualitative changes to agent solutions occurred
and were subsequently executed by the agents. A snapshot corresponding to each iteration was then
programmatically extracted and scored according to the respective task’s evaluation suite. Segment
color encodes its within-trial rank ranging from dark/worst (0.0) to bright/best (1.0). Red ticks denote
steps where agents executed a tool call to visualize an image. Trials are sorted by final-iteration value
per task in descending order. Each bar is one agent trial, split into segments for that trial’s iterations in
chronological order.

FN: GT 8 unmatched

GT - Frame 21833

G

Example
agent outputs

G.1

Failure modes

G.1.1 1000
Tracking errors without visualization (claude-code/claude-opus-4-6)

Pred - Frame 386
IDSW: GT 0: pred 2 -> 5

GT - Frame 386

Pred - Frame 20989
IDSW: GT 0: pred 0 -> 6

GT - Frame 20989

Pred - Frame 1
FP: Pred 7 unmatched

GT - Frame 1

Pred - Frame 2
FP: Pred 7 unmatched

GT - Frame 2

Figure 7: Post-hoc visualization of agent’s fly tracking outputs on selected frames (left) compared to
ground truth detections (right) on a reference video supplied to the agent for development, revealing
800 errors unlikely to persist after human visual inspection and iteration. The outputs were
tracking
generated by the agent’s submitted solution from trajectory GzGR3Vz, a trial in which the agent never
attempted to visualize its outputs (see Fig. 6).

G.1.2

Visual Latent Miss (claude-code/claude-opus-4-6)

The agent noticed errors in swing/stance bouts and correctly hypothesized that they might
arise from a keypoint-tracking orientation issue: regardless of fly-crop orientation, the
predicted head keypoint appeared at the same end of the image. To test this, the agent visualized predictions for two crop orientations. However, it misinterpreted both visualizations,
concluding that the fly in the second orientation was pointing down when it was not, and
misidentifying the colors of the tarsus keypoints.
End-to-End Minimal: Trajectory dH6CGNw

130. Bash: Check output directory → stance bouts.pkl
131. I removed the tracks saving in my rewrite. Let me just run the analysis fresh. Actually,
the process experiment function doesn’t save tracks anymore b...
132. Bash: Check orientation of crops and keypoints → Det 3 orient 1:
head y=77, abd y=110, head on top=True
133. Read(crop 0 orient0.png)

134. Read(crop 0 orient1.png)

135. OK interesting - the model predicts head at top in both orientations. So when the orientation is correct (orient 0, fly pointing up), the head keypoint is correctly at the top. When
the orientation is flipped (orient 1, fly pointing down), the model still predicts head at top
of the image, but the actual head is at the bottom. So the model is being ”tricked” by the
flipped orientation.
In orient 0: the fly is pointing up, and the tarsus keypoints (red dots) are correctly placed
around the legs.
In orient 1: the fly is pointing down, but the model still predicts as if the fly is pointing
up...
136. The orientation matters - the model needs the fly pointing up. I need to resolve the 180°
ambiguity. Let me use velocity direction.
137. Read(fly pipeline.py) → 334→def interpolate gaps(arr, max gap=10):
138. Edit(fly pipeline.py) → The file /workspace/fly pipeline.py has been
updated successfully.
G.1.3

Visual Latent Miss (codex/gpt-5.4)

The agent attempted to align fly crops vertically before training a pose model, but a bug in its
rotation code left the crops visibly misaligned. After visualizing a crop, the agent appeared

to notice the poor alignment, but attributed it to silhouette orientation being affected by
the wings rather than to the rotation bug. It then applied a darker-pixel filtering heuristic
and re-visualized the crop, but the alignment did not improve. Despite the unchanged
visualization, the agent judged the crop geometry “acceptable” and proceeded to model
training.
End-to-End Minimal: Trajectory idZtCyE

66. The raw fly size matches the training crop scale more closely than I expected: the ellipse
major axis is about 45 to 56 px, which is in the same ballpark as the annotated head-toabdomen span in the 192 px training crops. I’m checking a rotated crop from the arena
video now to make sure a fixed-size affine crop is sufficient.
67. Bash: python3 - <<’PY’ import cv2, sys, numpy as np from pathlib i... →
saved 6 crops to /workspace/debug crops
68. view image(crop 0.png)

69. A fixed 192 px affine crop is viable, but the raw silhouette orientation is being pulled
around by wings. I’m tightening the ellipse fit to the darker body core so the crop alignment
is closer to the training distribution before I start training the pose model.
70. Bash: python3 - <<’PY’ import cv2, sys, numpy as np from pathlib i... →
saved 6
71. view image(crop 0.png)

72. I’ve got the crop geometry into an acceptable range, so I’m doing the critical viability
check now: a very small coordinate-regression network on the ...

G.1.4

Dependency installation (terminus-2/gpt-5.4)

Registration: Trajectory zZMfrKG

6. The script currently fails because cv2 is not installed in the current environment,
though requirements.txt should handle this during evaluation. However, for local
testing now, relying on cv2 blocks progress. To make the solution more robust and
reduce dependencies, we should remove the OpenCV requirement entirely and
reimplement arena detection using only numpy plus the provided helper Movie
reader...
Bash: cat > /workspace/register.py <<’PY’#!/usr/bin/env python3imp...,
Bash: python /workspace/register.py /workspace/config all.json, Bash:
python - <<’PY’import pickle, numpy as npfor exp in [’exp 1’... → PY
G.1.5

Runtime overestimation (claude-code/claude-opus-4-6)

The agent launched a keypoint-model retrain at step 74. At step 79, it inspects the process
with ps aux | grep python3, which (without -o etime) returns the default TIME column
reporting aggregate CPU time across cores rather than wall-clock elapsed time. At step 80,
the agent overestimated the runtime by a factor of 42, claiming that the training had been
”running for 458 minutes (7.6 hours),” though the process was launched only 11 minutes
earlier. It killed the process at step 81 and relaunched a fresh training run at step 82.
End-to-End Minimal: Trajectory 4U2iuyY

73. 3.54px mean error. That’s reasonable but let me quickly retrain with faster settings to get
better quality.
74. Bash: python3 << ’PYEOF’ # Fast retrain with better settings import
json, os, cv2, numpy as np, ... → Command running in background with ID:
b8zoyk509. Output is being written to: /t...
75. While the model trains, let me build the full pipeline script.
78. Bash: cat /tmp/claude-0/-workspace/6a88d0c7-814d-493d-a268-d994c78e3829/
tasks/b8zoyk509.output 2... → (Bash completed with no output)
79. Bash: ps aux | grep python3 | grep -v grep → root 3578 4273 0.2 26994448
3079604 ? Rl 04:24 458:00 python3
80. The training has been running for 458 minutes (7.6 hours), but it only needs to run 80
epochs. Something seems very slow. Let me check what’s happening. Actually, the process
has been running since 04:24 and it’s currently much later. The issue might...
81. Bash: kill 3578 2>/dev/null; sleep 1; echo "done" → done
82. Bash: python3 << ’PYEOF’ # Quick retrain - images already in memory,
let’s time it properly impo... → Command running in background with ID:
b10fu8xbr. Output is being written to: /t...

G.1.6

Inconsistent time management (terminus-2/gpt-5.4)

Keypoint Tracking: Trajectory cTfpzyB

8. Training has reached epoch 3 and has plateaued around mean percentile error
6.6 px with p50 between 1.3 and 1.6 px. This is far from the target and suggests
the current architecture/loss setup is not adequate. Continuing to 25 epochs
is unlikely to achieve subpixel accuracy. Because the images are standardized
192x192 grayscale fly crops with limited pose variation, a two-stage coordinate
regresso...
Bash: C-c, Bash: cat > /workspace/train pose reg.py <<’PY’import os,
json, ra... → 100.0%
10. The first epoch of the coordinate-regression model is worse than the heatmap
model (mean percentile error ˜7.57 px, p50 ˜2.44 px). This may improve over
more epochs, but the initial result is not promising. We should still gather a few
more epochs before deciding, since pretrained backbones sometimes need several
epochs to settle. No artifacts are ready yet.
Bash → .5":
9.124578475952148,
"mean percentile error":
5.0371910572052006, "sec": 19.1...
11. The regression model is improving rapidly: by epoch 3 it beats the prior heatmap
baseline, reaching mean percentile error ˜5.04 px, p50 ˜1.61 px, p95 ˜6.82 px. This
is still far from target but trending in the right direction. Since training is only
20 epochs and each epoch is ˜19-20 seconds, it’s cheap to let it continue and see
whether it approaches a plateau. We should not interrupt yet.
Bash → 5": 8.04142951965332, "mean percentile error": 4.244452714920044,
"sec": 43.9517...
G.1.7

Infinite looping (terminus-2/claude-opus-4-6)

The agent’s terminal session became stuck for 82 minutes before recovering.

Gait Segmentation: Trajectory R2LhGFW

15. The previous explore6.py script is still running (the smoothed dfwd with min bout
section was slow). Let me wait for explore7.py to finish, or cancel ...
16. The script output seems to be still displaying the file content. Let me wait for it to
finish executing.
17. It seems like the terminal is stuck or the script is taking very long. Let me cancel it
and try a more efficient approach.
Bash: C-c → if result[i] != result[i-1]:
18. The terminal seems stuck. Let me try sending Ctrl+C again more forcefully.
Bash: C-c, Bash: C-c, Bash: → if result[i] != result[i-1]:
19. The terminal is stuck, possibly still in the heredoc or waiting for input. Let me try
to end the heredoc and get back to a prompt.
Bash: PYEOF → if result[i] != result[i-1]:
20. The terminal is completely stuck. Let me try sending Ctrl+D to end input, or try
other escape sequences.
Bash: C-d, Bash: C-c → if result[i] != result[i-1]:
48. I’ve been stuck for an extremely long time. The terminal is completely unresponsive. I need to try a completely different approach. Let me try to see ...
I can see the shell prompt
132. FINALLY! The terminal has recovered!
‘root@39263b0b5319:/workspace#‘. The heredoc for explore7.py was interrupted
by Ctrl+C...
Bash: echo ’numpyscipypandas’ > /workspace/requirements.txt, Bash: cat
/workspace/requirements.txt → root@39263b0b5319:/workspace#
G.1.8

Self-termination (claude-code/claude-opus-4-6)

In two Claude Code trials, the agent terminated its own session by issuing a kill command
(e.g. kill $(pgrep -f fly pipeline)) whose pattern also matched the parent agent process. Because the agent is invoked with the task prompt passed inline as a command-line
argument, any script names mentioned in the prompt appear in the agent’s own argv, so a
pkill -f / pgrep -f pattern intended for a child process matches the agent itself.
End-to-End Minimal: Trajectory 4U2iuyY

151. Bash:
timeout
43200
python3
-u
/workspace/fly pipeline.py
/workspace/test config.json 2>&1 | tee /workspace/pipeline output.lo...
→ Pipeline started in background, PID=6230
162. Let me speed things up by increasing frame skip and optimizing the patch extraction.
163. Bash: kill $(ps aux | grep fly pipeline | grep -v grep | awk ’{print
$2}’) 2>/dev/null; sleep 1; echo "killed"

G.2

Success modes

G.2.1

Understanding fly body kinematics (claude-code/claude-opus-4-6)

Gait Segmentation: Trajectory mr6ovRR

26. OK so the bout-level metric doesn’t really benefit much from smoothing in this
small labeled dataset. Let me think about what else could help. Actually, let me
try a different approach.
...Let me try a few more things: 1. Using body-speed-relative threshold 2. Using
distance from body center (during stance, leg extends backward; during swing,
it’s closer to body) Actually, let me try another approach: looking at tarsus position
relative to body, not speed. During the gait cycle, the tarsus oscillates forward and
backward relative to the body. We can look at this oscillation to identify swing
(forward movement) vs stance (backward movement relative to body). But the
speed approach is already working well. Instead, I should focus on making it
more robust by using the leg velocity relative to the body, projected along the
body axis. During stance, the leg moves backward relative to the body as the
body pushes forward while the foot stays planted. During swing, the leg moves
forward relative to the body. This gives me a signed signal that’s more informative
than just raw speed magnitude.
G.2.2

Body-aligned coordinate frame (terminus-2/claude-opus-4-6)

Gait Segmentation: Trajectory nTga8kJ
def compute_all_features ( trk , fly_idx ):
''' Compute per - frame features for all 6 legs of a fly .
Returns dict mapping leg_i (0 -5) to feature array ( n_features ,
n_frames )
n_frames = trk . shape [2]
# Body center ( midpoint of left / right thorax )
body = ( trk [3 , :, :, fly_idx ] + trk [4 , :, :, fly_idx ]) / 2
# Heading direction ( head to abdomen )
head = trk [0 , :, :, fly_idx ]
abd = trk [6 , :, :, fly_idx ]
heading = head - abd
heading_norm = np . sqrt ( np . sum ( heading **2 , axis =0 , keepdims = True
))
heading_norm [ heading_norm == 0] = 1
heading = heading / heading_norm
# Perpendicular direction
perp = np . array ([ - heading [1] , heading [0]])
return features

G.2.3

Parallel task management (claude-code/claude-opus-4-6)

End-to-End Maximal: Trajectory UNWrmWc

142. Bash: rm -rf /workspace/keypoint tracker && python3 << ’PYEOF’ import
sys, os, pickle, time impo... → Command running in background with ID:
bn3u9gehc. Output is being written to: /t...
150. Still at epoch 10. Let me update the todo list and work on other tasks while waiting.
152. Let me work on improving the fly tracking while the keypoint model trains. Let me read
the current tracking code.
178. Edit(fly pipeline.py) → The file /workspace/fly pipeline.py has been
updated successfully.
181. Bash: python3 -c " import sys sys.path.insert(0, ’helpers’) from
fly pipeline import track flies... → Command running in background with
ID: btsygyjp5. Output is being written to: /t...
190. While tracking runs, let me check on the keypoint training.
193. Let me work on requirements.txt while tracking runs.
195. Write(requirements.txt) → File
created
successfully
at:
/workspace/requirements.txt
198. 15 tracks now, with the top 5 being 10K+ frames (out of 21866). Much better — close to
8-10 real flies. The merge step is working. Now let me run Step 2 on this and continue.

H

Token usage and runtimes

Wall-clock time (hours)

Classifier

Segmentation

Comparison

2.8±0.3

3.9±1.8

0.7±0.0

0.4±0.4

1.0±0.9

0.7±0.0

0.1±0.1

2.0±0.4

0.4±0.1

3.8±0.8

0.2±0.0

1.1±0.5

1.5±0.6

0.2±0.0

Input tokens / output tokens
9.4±0.7M / 78±7K 906±550K / 19±7K 2.6±0.5M / 24±9K 495±123K / 24±6K 434±153K / 7±2K 1.5±0.7M / 32±11K 489±90K / 13±1K
8.0±5.0M / 41±6K 1.1±0.1M / 27±2K 3.4±1.1M / 34±9K 410±52K / 14±1K 2.1±0.7M / 24±9K 1.3±0.5M / 28±4K 692±101K / 16±3K
12.5±3.5M / 109±18K 1.5±0.5M / 39±5K 12.5±4.3M / 50±16K 1.2±0.0M / 31±6K 1.3±1.8M / 24±25K 6.8±4.0M / 73±8K 1.1±0.3M / 32±12K
4.9±7.7M / 20±11K
98±19K / 9±2K
1.0±1.0M / 17±3K
120±53K / 7±2K
45±5K / 5±0K
69±13K / 6±0K
95±22K / 7±0K

Table 5: Single-stage task input and output token counts and wall-clock runtimes. Values
are means ± standard deviation over three trials per agent-task configuration.

Wall-clock time (hours)

5.0±3.6

7.1±2.5

1.0±0.2

0.6±0.3

Input tokens / output tokens
16.5±10.2M / 89±64K 13.3±4.4M / 89±53K
11.5±1.3M / 70±6K
11.2±1.2M / 72±6K

Table 6: End-to-end task input and output token counts and wall-clock runtimes. Values are
means ± standard deviation over three trials per agent-task configuration.

Measuring task size
Data size (MB)

Data types across benchmarks

17062
Data size (MB) (cuberoot scale)

40444

bin
ary
im
ag
es
jso
mo
lec met n
u
mo lar d data
lec yn
ula am
r s ics
tru
ct
seq ures
ue
nc
ing
tab
ula
r
vid
eo
xm
oth
er

ge

ric

ne

I

Data type

Figure 8: Left: Distribution of task dataset sizes across benchmarks on a cube-root scale. Previous
work operates on much smaller datasets, with the majority having small or pre-processed tabular
datasets, or no external data at all in the task. Our pipeline stages operate on the big datasets
common in modern science. Right: Distribution of data types across benchmarks. Prior work is
dominated by tabular data; our pipeline stages span a broader range of modalities representative of
the heterogeneous data common in modern experimental science.
To contextualize our benchmark relative to existing work, we compare task size across
benchmarks along three axes: solution code size, dataset size, and data modality. We
describe how each quantity is measured below.
Lines of code. Source lines of code (SLOC)—non-blank, non-comment lines—are measured using the radon library’s raw analysis.
Dataset size. Total size in megabytes of all data files associated with a task. For benchmarks
where test/evaluation data overlaps with input data, files are deduplicated by comparing
file size and the first 4KB of content.
Data types. Data types are categorized by file extension (e.g., .csv → tabular, .tif → images, .pdb → molecular structures). Each task is assigned to all categories present in its data
files; fractions are normalized so that a task with multiple data types contributes to each.
Per-benchmark details. The source of code and data varies across benchmarks, as not all
provide gold solutions or input data files. Table 7 summarizes these differences.
To contextualize our benchmark relative to existing work, we compare task complexity
across benchmarks along three axes: solution code size, input data size, and data modality.
These measurements characterize the scope of what each benchmark asks of an agent—how
much code must be written, how much data must be processed, and what types of data are
involved. We describe how each quantity is measured below.

Benchmark

Code measured

Data measured

Gold solution (all 102 tasks)

Agent-generated code from GPT-4o
coder runs (real tasks only, train + test
splits)
Median-length sample ground truth program, sampled from the combinatorial space of expert-annotated transform
pipelines and statistical models (all 12
datasets)
Gold reference code snippet (all 1000
tasks)
Median of 12 agent runs per task (agentwritten files only, excluding environment helpers)

Input dataset folder, mapped via
benchmark CSV
CSV files referenced in each
task’s metadata JSON

Dataset CSV per task

None (data is embedded in the
prompt)
Union of input and evaluation
data, deduplicated, excluding
ground truth outputs

Table 7: Source of code and data measurements for each benchmark.

J

Task prompts

J.1

Body Tracking prompt
Fly Body Tracking
(track.py) should be saved here. Input data is located at /data/.
Write a script to track the positions and orientations of the bodies of multiple flies
from video while keeping track of identity.
Reference Experiments
• Location: Three reference experiments are provided for development:
• /data/exp 1/movie.ufmf
• /data/exp 2/movie.ufmf
• /data/exp 3/movie.ufmf
• Each video contains multiple flies in a circular arena
dependencies for movies.py
Implement a fly tracking system as a Python script that can process arbitrary videos.
Required Output: ‘track.py‘
that:

You must produce a script at /workspace/track.py

• Takes a JSON config file path as its only CLI argument: python track.py
config.json
• The config file contains a JSON array of objects, each with:
• "video path": path to a .ufmf video file
• "output path": path where the output trx.pkl should be saved
• Processes each video in the config and saves a trx.pkl at the specified
output path
• Works on any number of videos (not just the 3 reference videos)
Example config:

{" video_path ": "/ data / exp_1 / movie . ufmf " , " output_path ": "/
workspace / out / exp_1 / trx . pkl "},
{" video_path ": "/ data / exp_2 / movie . ufmf " , " output_path ": "/
workspace / out / exp_2 / trx . pkl "}

Example usage:
python track . py config . json

The script should:
• Estimate the position, orientation, and size of the body of each fly (not
including wings) in each frame of each input video
• Keep track of the identities of individual flies across frames
• Output in the trx format described below for each video
To build your algorithm and tune its parameters you should:
• Examine the reference videos and understand their statistical properties
• Use your prior knowledge of what flies look like
• Iterate: try an algorithm, look at statistical properties of its results, and adapt
Script Output Format: trx Dictionary Structure Your tracking output must be a
single dictionary. All frame indices are 0-indexed. It must contain the following
fields:
Required fields:
list of ntargets arrays, each x-coordinate of centroid each anishape (nframes i,)
mal in pixels
list of ntargets arrays, each y-coordinate of centroid each anishape (nframes i,)
mal in pixels
list of ntargets arrays, each Orientation of each animal (from tip
of abdomen to head) in radians
list of ntargets arrays, each 1/4 of the length of the body (tip of
the abdomen to head) in pixels
list of ntargets arrays, each 1/4 of the width of the body (left
side to right side) in pixels
list of ntargets arrays, each Time difference between consecushape (nframes i-1,)
tive frames in seconds
off
list of ntargets arrays, each Offset for computing index:
-firstframe
1D array of shape (ntargets,) Global frame index where each animal’s trajectory begins (0-indexed)
1D array of shape (ntargets,) Global frame index where each animal’s trajectory ends (inclusive, 0indexed)
1D array of shape (ntargets,) Number of frames in each animal’s
trajectory
1D array of shape (to- Timestamp of each frame in sectal frames,)
onds (global, not per-target)

Identity tracking: Each list entry should correspond to the same fly identity. If an
identity is lost, a new entry can be added to the list. The number of entries in the
lists must therefore be at least the number of flies, but could be longer.
Data alignment: All per-target list fields (x, y, theta, a, b, etc.) have an entry
per fly, with x[i][idx] corresponding to the position of the ith fly at frame idx +
firstframe[i]
Coordinate system:
• x = 0 corresponds to the first column (axis = 1) and y = 0 corresponds to
the first row (axis = 0).
• If (x head, y head) and (x abdomen, y abdomen) are the coordinates of the
head and the abdomen, then the orientation theta can be computed with
np.arctan2: theta = np.arctan2(y head-y abdomen,x head-x abdomen)
Example structure:
trx = {
'x ': [ np . array ([...]) , np . array ([...]) ],
arrays for 2 flies
'y ': [ np . array ([...]) , np . array ([...]) ],
'a ': [ np . array ([...]) , np . array ([...]) ],
'b ': [ np . array ([...]) , np . array ([...]) ],
' theta ': [ np . array ([...]) , np . array ([...]) ],
'dt ': [ np . array ([...]) , np . array ([...]) ],
' off ': [ np . array ([0]) , np . array ([0]) ],
' firstframe ': np . array ([0 , 0]) ,
start at frame 0
' endframe ': np . array ([999 , 999]) ,
end at frame 999
' nframes ': np . array ([1000 , 1000]) ,
have 1000 frames
' ntargets ': 2,
' timestamps ': np . array ([0.0 , 0.0067 , ...]) ,
total_frames ,)

# list of 2

# offset = # both flies
# shape (

Accessing data for fly i at frame f:
# Get the index into the per - fly arrays
idx = f - trx [ ' firstframe '][ i]
x_position = trx [ 'x '][ i ][ idx ]
y_position = trx [ 'y '][ i ][ idx ]

Saving output: Your track.py script should save the tracking results for each video
as trx.pkl at the output path from the config:
with open ( output_path , 'wb ') as f:
pickle . dump ( trx , f)

The approach is open-ended, but your implementation must:
1. Estimate the pose of all flies in all frames:
2. Centroid Position (x, y)
3. Abdomen to head orientation (theta)
4. Length and width (a, b)
5. Track identities across frames to maintain consistent fly IDs
6. Output in trx format with all required fields correctly populated
Expected Challenges
• Multiple flies are present (need identity tracking)
• Flies may touch

Your script will be evaluated on multiple unseen videos (beyond the 3 reference
videos provided). Make sure your algorithm generalizes well.
• Downstream analyses will involve measuring properties of precisely how
the flies move (e.g. their velocity, change in orientation).
• They will also involve using body position and orientation as the first stage
of a two-stage (top-down) keypoint detection algorithm.
• We will assess the accuracy of the tracker by measuring both detection and
cross-frame association errors:
• Detection errors: For every frame and fly, detection error will be measured
based on the derived tip of the head and abdomen positions:
x_head = x + 2* a* np . cos ( theta )
y_head = y + 2* a* np . sin ( theta )
x_abdomen = x + 2* a* np . cos ( theta + np . pi )
y_abdomen = y + 2* a* np . sin ( theta + np . pi )

Detection error will be computed as
dist_head = np . sqrt (( x_head_true - x_head_pred ) **2 + (
y_head_true - y_head_pred ) **2)
dist_abdomen = np . sqrt (( x_abdomen_true - x_abdomen_pred ) **2 +
( y_abdomen_true - y_abdomen_pred ) **2)
err = ( dist_head + dist_abdomen ) / a / 2

where true are the groundtruth and pred are your algorithm’s output
predictions.
• Association errors: We also penalize identity switches: when a single
ground-truth fly is assigned to different track predictions over two frames.

J.2

Registration prompt
Fly Trajectory Registration
(register.py) should be saved here. Input data is located at /data/.
Write a script to process raw fly tracking data by:
• Detecting arena boundary
• Converting from pixel coordinates to a common coordinate system defined
by the arena boundary
• Removing bad tracking (indicated by NaNs)
• /data/exp 1/movie.ufmf and /data/exp 1/trx.pkl
• /data/exp 2/movie.ufmf and /data/exp 2/trx.pkl
• /data/exp 3/movie.ufmf and /data/exp 3/trx.pkl
Each experiment contains:

• movie.ufmf: Video file (UFMF - Micro Fly Movie Format) — used for detecting the circular arena boundary
• trx.pkl: Pickle file containing a trajectory dictionary
• Multiple flies present in a circular arena
• Trajectories may contain NaN values where flies were not detected
• Coordinates are in pixel units
• The file may contain * mm fields, but these are placeholders and should be
discarded
Helper: helpers/movies.py provides a Movie class with get frame(frame num) to
read frames
Physical Parameters
• Arena radius: 26.689 mm (physical radius of the circular arena)
• Frame rate: ˜150 FPS (frames per second)
Required Output:
‘register.py‘ You must produce a script at
/workspace/register.py that:
1. Takes a JSON config file path as its only CLI argument: python register.py
config.json
2. The config file contains a JSON array of objects, each with:
3. "video path": path to a .ufmf video file
4. "trx path": path to a trx.pkl trajectory file
5. "output path": path where the output registered trx.pkl should be saved
6. Processes each experiment in the config and saves a registered trx.pkl at
the specified output path
7. Works on any number of experiments (not just the 3 reference experiments)
Example config:

{" video_path ": "/ data / exp_1 / movie . ufmf " , " trx_path ": "/ data / exp_1
/ trx . pkl " , " output_path ": "/ workspace / out / exp_1 / registered_trx
. pkl "},
{" video_path ": "/ data / exp_2 / movie . ufmf " , " trx_path ": "/ data / exp_2
/ trx . pkl " , " output_path ": "/ workspace / out / exp_2 / registered_trx
. pkl "}

Example usage:
python register . py config . json

The script should, for each experiment:
1. Detect the arena boundary from the video
2. Spatially register trajectory coordinates
3. Transform the trajectories so that (0,0) corresponds to the arena center
4. Transform the trajectories so that the units are in millimeters
5. Note: This step ONLY computes the * mm fields; it does NOT modify the
pixel-based fields
6. x mm, y mm: The ellipse center in millimeters
7. a mm, b mm: Ellipse quarter-major and quarter-minor axes in millimeters
8. theta mm: Same as theta (orientation in radians is scale-invariant)
9. Removes NaN gaps from trajectories
10. Interpolate short gaps (≤5 frames) using linear interpolation
11. Crop leading and trailing NaN values
12. Split trajectories at long gaps (¿5 frames) into separate segments
13. Note: This step modifies all relevant pixel-based fields
Script Input Trajectory Format The input trajectory dictionary contains these fields
(all position/size values in pixel units), among others:

x-coordinate in pixels (per fly)
y-coordinate in pixels (per fly)
Orientation in radians (per fly)
1/4 of major-axis length in pixels (per fly)
1/4 of minor-axis length in pixels (per fly)
Global frame index where trajectory begins
Global frame index where trajectory ends
(per fly, inclusive)
Number of frames in trajectory (per fly)
Time difference between consecutive frames
in seconds (per fly)
Note: Arrays may contain NaN values where the fly was not detected.
Script Output Trajectory Format The output must contain all input fields (possibly
modified by NaN removal) plus the registered * mm fields:
list of arrays of shape (1,) Pixels per millimeter conversion factor (per fly, same for all flies)
Important constraints:
• Output trajectories must have no NaN values in any field
• All fields must be internally consistent (e.g., for each fly, array lengths must
match that fly’s nframes)
Saving output: Your register.py script should save the registration results for each
experiment as registered trx.pkl at the output path from the config:
with open ( output_path , 'wb ') as f:
pickle . dump ( registered_trx , f)

Your script will be evaluated on multiple unseen experiments (beyond the 3 reference experiments provided). Make sure your algorithm generalizes well.
• Circular arena correctly detected from video
• No NaN values in output trajectories
• All trajectories have consistent field lengths
• * mm fields correctly computed: translated to arena center and scaled to mm
• Pixel-based fields only modified by NaN interpolation/removal, not by
registration
• Output format matches specification

J.3

Keypoint Tracking prompt
Fly Pose Estimation
Task Description
Train a pose estimation model for flies using the MultiFly Dataset.
Multifly Dataset Description
• Training data is located at /data/train data.
• Images are recorded at approximately 18.9 px / mm from above.
Contents:
Keypoint indices
• The downstream task involves measuring the precise movements of each
keypoint, for example the instantaneous velocity of each keypoint.
• Median error: The median per-keypoint Euclidean error should be well
below 1 pixel (subpixel). Target ≤ 0.5 px.
• Tail error: Outlier percentile errors should also be small. Large outlier
errors will corrupt velocity estimates for multiple surrounding frames, and
scientists will not trust a model that makes large mistakes when the correct

keypoint locations are easy to estimate. Target 95th percentile error ¡= 2 px,
97.5 percentile error ¡= 3.5 px.
• During development, the agent should monitor and report the full error
distribution (50th, 75th, 90th, 95th, and 97.5th percentiles), not just mean
error.
• The model will be evaluated based on the mean over all keypoints of the mean over these percentiles of the Euclidean error:
∗ } N , p ) where x pred is the model’s
− xik
i =1
K ∑k =1 | P| ∑ p∈ P percentile ({∥ xik
ik
∗ is the groundtruth label, and
prediction on example i for keypoint k, xik
P = {50, 75, 90, 95, 97.5}
• Target mean percentile error ≤ 1.7 px.
• Your model will be evaluated on a held-out test set from the same dataset.
1. Load the Multifly Dataset.
2. Train a keypoint tracker or pose estimation model.
3. Save your model class definition to model.py
4. Save the trained model instance to model.pkl
Model Interface
Your model.py must define a class called KeypointTracker with the following interface:
class KeypointTracker :
def __init__ ( self , num_keypoints =21) :
self . model = None # Your trained model
def track ( self , X: np . ndarray ) -> np . ndarray :
Track fly keypoints on a cropped image of a fly .
X: 4D array of shape ( n_frames , H , W , C) - batch of single
- crop images of flies
3D array of shape ( n_frames , num_keypoints , 2) - predicted
keypoint positions (x ,y)
# APPLY PRE - PROCESSING HERE
# Use self . model for inference

Saving the Model
• model.py contains the class definition (the code for KeypointTracker)
• model.pkl contains the trained KeypointTracker instance
tracker = KeypointTracker ()
tracker . model = trained_model

# your trained model

with open ( ' model . pkl ', 'wb ') as f:
pickle . dump ( tracker , f)

with open ( ' model . pkl ', 'rb ') as f:
tracker = pickle . load (f)

You MUST provide a requirements.txt file listing any Python packages your model
Notes
• Remember that each annotation correspond to a single fly.
• Implement any pre-processing code directly into the train function

J.4

Behavior Feature Computation prompt
Fly Per-Frame Feature Computation
(compute features.py) should be saved here. Input data is located at /data/.
Objective
Write a script to compute a set of features from fly tracking data that capture instantaneous properties of how the fly is moving.
• /data/exp 1/registered trx.pkl
• /data/exp 2/registered trx.pkl
• /data/exp 3/registered trx.pkl
Registered Trajectory Data

• Format: Pickle file containing a trajectory dictionary with fields including:
Pixels per millimeter conversion factor (per fly, same for all flies)
Time difference between consecutive
frames in seconds (per fly)
begins (per fly)
ends (per fly)
Number of frames in trajectory (per
x mm, y mm, theta, a mm, and b mm are lists of ndarrays. trx[‘x mm’][fly]
etc. correspond to trajectory fly and is of shape (trx[‘nframes’][fly]).
dt is also a list of per-fly ndarrays. It is one frame shorter (shape
(trx[’nframes’][fly]-1)) because it is based on the difference between
frames.
Feature Documentation
• Location: perframe feature definitions.pdf and corresponding TeX
source perframe feature definitions.tex
• These documents contain detailed definitions for all per-frame features.
Refer to them for exact computation methods.
Physical Parameters
• Arena radius: 26.689 mm
Create a Python script /workspace/compute features.py that:
compute features.py config.json
• The config file contains a list of entries, each specifying a trajectory file and
output directory:

{" trx_path ": "/ path / to / registered_trx . pkl " , " output_dir ":
"/ path / to / output / perframe "},

• For each entry, the script should load the registered trajectory data, compute
all features, and save them to the specified output directory.
Required Features
The script must compute all of the following features. Each feature must be saved as
{output dir}/{feature name}.pkl:

absdtheta
absdv_cor
corfrac_maj
corfrac_min
dphi
dtheta
du_cor
du_ctr
dv_cor
dv_ctr
flipdv_cor
phisideways
velmag
velmag_ctr
velmag_nose
yaw

Each feature file must be a pickle file containing a list of arrays, one array per fly:
# Example : velmag . pkl
np . array ([...]) , # fly 0
np . array ([...]) , # fly 1

Array lengths:
• Position-based features: nframes per fly
• Velocity/derivative features: nframes-1 per fly
1. All 16 feature files are created for each experiment
2. Each file contains a list with ntargets arrays
3. Array lengths match expected dimensions per feature type
4. Feature values match ground truth within numerical tolerance
5. Your script will be evaluated on multiple unseen experiments beyond the
reference data provided

J.5

Walking Behavior Classification prompt
Fly Movement Behavior Classification
• Train a binary classifier to detect ”walking” behavior in fruit flies
(Drosophila) using pre-computed per-frame movement features.
• To define the walking behavior, we provide a training dataset in which
positive labels (1) correspond to walking and negative labels (0) correspond
to not walking.

• Save the classifier class to model.py and the trained instance to model.pkl.
All data is in /data/train data/:
/ data / train_data /
|--- sample_1 /
|--- sample_2 /
|--- sample_3 /
|--- sample_4 /
|--- train_labels . pkl

# Per - frame features (. pkl files )

# Training labels

Per-Frame Features Format
Each sample directory contains 16 .pkl files, one per feature.
Load features using pickle:
# Load a feature for all flies in a sample
with open ( '/ data / train_data / sample_1 / perframe / velmag . pkl ', 'rb ') as
f:
feature_data = pickle . load (f)
# feature_data is a list of arrays , one per fly
# feature_data [ fly_idx ] is a 1D array of feature values for that
fly

Feature lengths: Most features have length equal to the number of tracked frames
for that fly. Some features derived from frame-to-frame differences are one element
shorter.
Fly indexing: Flies are 0-indexed in the perframe arrays (feature data)
Labels Format
with open ( '/ data / train_data / train_labels . pkl ', 'rb ') as f:
labels = pickle . load (f)

Labels is a dict with keys:
• sampleDirs: list of sample directory names [sample 1, sample 2, ...]
• labels: list of lists of arrays, labels[sample idx][fly idx] = label per bout
(1=Walk, 0=None)
Labels are associated with samples, flies, and bouts of frames: Sample:
labels[‘flies’][sample idx], labels[‘t0s’][sample idx], etc.
correspond to the data files in labels[‘sampleDirs’][sample idx] Fly:
labels[‘t0s’][sample idx][fly idx], labels[’labels’][sample idx][fly idx],
etc.
correspond to fly flyid = labels[‘flies’][sample idx][fly idx] 1 Frames: Frames from labels[‘t0s’][sample idx][fly idx][bout idx] to
labels[‘t1s’][sample idx][fly idx][bout idx] (exclusive) all have the label
labels[‘labels’][sample idx][fly idx][bout idx]
Not all frames are labeled
Frame indexing: The t0s and t1s values are 0-indexed frame indices that directly

Fly indexing: Fly id is 0-indexed in perframe arrays but 1-indexed in
labels[‘flies’]. For example, to access the velmag feature data associated with a
label for sample i, fly j and bout k:
sampledir = Path ( labels [ ' sampleDirs '][ i ])
with open ( sampledir / ' perframe ' / ' velmag . pkl ', 'rb ') as f:
velmag_data = pickle . load (f)
t0 = t0s [i ][ j ][ k]
t1 = t1s [i ][ j ][ k]
bout_velmag_data = velmag_data [ fly ][ t0 : t1 ]

Requirements
1. Load the per-frame features and training labels
2. Train a classifier to predict walking behavior (1) vs. not walking (0)
3. Save your classifier class definition to model.py
4. Save the trained model instance to model.pkl
Model Interface
Your model.py must define a class called WalkingClassifier with the following
interface:
class WalkingClassifier :
def __init__ ( self ):
self . model = None # your trained model
self . feature_names = [] # list of feature names used , e.g.
[' velmag ', ' dtheta ', ...]
def predict ( self , X: np . ndarray ) -> np . ndarray :
Predict walking behavior for a single fly 's trajectory .
X: 2D array of shape ( n_frames , n_features ) - full
trajectory for one fly ,
features in order of self . feature_names
1D array of shape ( n_frames ,) - predictions for each
frame (1= walking , 0= not walking )
# Apply any preprocessing , then use self . model to predict

The predict method should include any preprocessing or feature transformations
applied during training.
Saving the Model
• model.py contains the class definition (the code for WalkingClassifier)
• model.pkl contains the trained instance (with self.model and
self.feature names set)
Example workflow:
clf = WalkingClassifier ()
clf . feature_names = [ ' velmag ', ' dtheta ', ...]
clf . model = trained_model # your trained model

with open ( ' model . pkl ', 'wb ') as f:
pickle . dump ( clf , f)

The evaluation code will load and call the model as follows:
EXP_DIR = ...
FLY_ID = ...
with open ( ' model . pkl ', 'rb ') as f:
classifier = pickle . load (f)
feature_names = classifier . feature_names
perframe_dir = EXP_DIR / " perframe "
# Load features for this experiment
features = \{\}
for fname in feature_names :
fpath = perframe_dir / f" \{ fname \}. pkl "
with open ( fpath , " rb ") as f:
features [ fname ] = pickle . load (f)
# Fly index
fly_arr_idx = FLY_ID - 1

# Convert 1- indexed to 0- indexed

# Construct input data
fly_features = []
fly_features = [ feat [ fly_arr_idx ] for feat in features . values () ]
# Truncate to minimum length and stack
min_len = np . min ([ len ( feat ) for feat in fly_features ])
X = np . column_stack ([ f [: min_len ] for f in fly_features ])
# Get predictions
preds = classifier . predict (X)

Success criteria
• Your model will be evaluated on a held-out test set based on balanced
per-frame accuracy.
You MUST provide a requirements.txt file listing any Python packages your model
Notes
• Only a subset of frames are labeled; unlabeled frames should not be used
for training
• Frames within labeled bouts are temporally adjacent

J.6

Gait Segmentation prompt
Fly Swing/Stance Classification
(classify gait.py) should be saved here. Input data is located at /data/.

• Goal: Write a script to segment fruit flies’ leg movements into swing and
stance bouts for frames when the fly is walking:
• Stance phase: The leg is in contact with the ground and propelling the animal
• Swing phase: The leg is lifted from the ground and recovering for the next
propulsion
• Your segmentation will be based on keypoint trajectories derived from video
recorded at 150 fps and 18.9 pixels per millimeter
• A small set of groundtruth labels from a separate video are provided to help
you fine-tune your algorithm.
• The output segmentations will be used to measure the duration of the swing
and stance bouts, thus it is important that your algorithm reproduce the
bout structure.
• A bout is a maximal contiguous run of frames with the same label (swing
or stance), considering only frames where the fly is walking. Non-walking
frames are excluded before determining bout boundaries.
• Your script’s outputs will be evaluated with a bout-level error criterion:

t∗

1 N
̸= y∗t )
∗ ∑ I (yt
2N ∗ b∑
−
b t=t
=1 b +1

N
+
∑ I (y∗t ̸= yt )
2N pred b=1 t pred − t pred

t=tb

where y∗t is the groundtruth label for frame t and yt
is the model’s
prediction, and (t1∗ , ..., t∗N ∗ ) is the groundtruth bout segmentation and

(t1 , ..., t N pred ) is the model’s bout segmentation.
• The sums over bouts are taken across all flies and all legs jointly (not averaged per-fly or per-leg).
• This metric penalizes over-fragmenting true bouts.
• Your script will be evaluated on multiple unseen experiments beyond the
reference data provided.
• /data/exp 1/keypoints.npz and /data/exp 1/walk preds.pkl
• /data/exp 2/keypoints.npz and /data/exp 2/walk preds.pkl
• /data/exp 3/keypoints.npz and /data/exp 3/walk preds.pkl
Per-Experiment Data Files 1. keypoints.npz
• This is the data you should generate swing/stance predictions for
These frames should be treated as not tracked (-1 in the output). Keypoint
indices:

2. walk preds.pkl
• Walking behavior classification for the flies in keypoints.npz
• Only compute swing/stance for frames where the fly is walking
• Pickle file containing a list of length n targets, where each element is a 1D
ndarray of per-frame walking predictions for that fly
• Arrays are globally aligned (index 0 = frame 0), but may be truncated at the
end
• Values:
• np.nan: fly is not tracked on this frame
• 0: fly is not walking
• 1: fly is walking (only compute swing/stance for these frames)
• The number of flies is consistent across keypoints.npz (last dimension of
trk dense) and walk preds.pkl (list length).
Tuning Data (shared across all experiments) 3. keypoints for labels.npz
• Tracking data from a different experiment to be used to fine-tune your
segmentation algorithm
• Same format as keypoints.npz
• Located at /data/keypoints for labels.npz
4. groundcontact labels.csv
• Use these labels along with keypoints for labels.npz to tune your algorithm.
• Located at /data/groundcontact labels.csv
Create a Python script /workspace/classify gait.py that:
classify gait.py config.json
• The config file contains a list of entries, each specifying input data and output
path:

{" keypoints_path ": "/ path / to / keypoints . npz " , "
walk_preds_path ": "/ path / to / walk_preds . pkl " , "
output_path ": "/ path / to / swing_stance . npy "},

• For each entry, the script should load the keypoints and walking predictions,
compute swing/stance classifications, and save the result to the specified
output path.
For each fly in the keypoints data, for each frame when the fly is walking, and for
each of the six legs, the script should compute whether the leg is in swing or stance
phase.
Important:
• Use keypoints for labels.npz and groundcontact labels.csv to tune your
segmentation algorithm.
• The script should apply your algorithm to each experiment’s keypoints.npz
to generate swing/stance predictions.
• The script should only compute swing/stance classifications for frames
where the walking classifier indicates the fly is walking. For all other frames,
use the ”not walking” sentinel value.
Each output file (swing stance.npy) must be a 3D numpy array with shape (n flies,
total frames, n legs) where:
• n flies: number of tracked flies
• total frames: T0 + n tracked frames
• n legs: 6
• Array index corresponds to absolute frame number (e.g., swing stance[fly,
500, leg] is the state at frame 500).
Each element of the array is an integer:
• -1: fly is not walking or frame is not tracked
• The tracking data is in pixel coordinates and frame indices
• Spatial conversion: 18.9 pixels per millimeter
• Temporal conversion: 150 frames per second

J.7

Statistical Comparison prompt
Fly Stance Duration Analysis
(analyze stance.py) should be saved here. Input data is located at /data/.

Write a script to analyze how optogenetic perturbation affects stance duration in
fruit fly locomotion, comparing experimental flies to control flies. Optogenetic
perturbations are controlled by exposing flies to a particular wavelength of light,
and occur when the lights are ON. The script should test whether the difference
in stance duration between lights ON and OFF periods is significantly different
between experimental and control groups, for both slow and fast walking speeds.
Stance duration is the time a leg spends in contact with the ground during a walking
gait cycle. For each experimental line, the script should compute the ON-OFF
difference in mean stance duration for both slow and fast walking, then use statistical
tests to compare these differences between experimental and control flies.
• For each GAL4 line and the control, there are four videos (experiments) each
corresponding to a different group of ˜10 flies.
for development. Your script will be evaluated on 10 GAL4 lines and controls (44
experiments total).
all experimental lines )
|--- velmag_ctr . pkl
|--- velmag_ctr . pkl

# Shared control group ( used for

Each line directory contains 4 experimental replicates from the same GAL4 line.
The control/ directory contains 4 control replicates that are used as the comparison
group for all experimental lines.

Each subdirectory contains the same four files. All data were derived from videos in
which the flies and their leg tips were tracked.
1. swing stance.npy
• Contains swing/stance classifications for all flies, frames, and legs
• Represented as a numpy array with shape (n flies, total frames, n legs)
where:
• n flies: number of trajectories
• total frames: total number of video frames (indexed from frame 0)
• n legs: 6 (in increasing order of keypoint index: 11, 12, 13, 14, 15, 16)
• swing stance[fly, frame, leg] is the classification for trajectory fly, frame
frame of the video, and leg leg (all 0-indexed).
• Values:
• -1: fly is not walking
• Classifications were computed from the velocities of the leg tip.
2. registered trx.pkl
• Trajectory data for each fly
• Contains the following metadata for temporal alignment between different
data files:
• trx[firstframe][fly] is the start of the first frame of trajectory fly
• trx[endframe][fly] is the last frame of trajectory fly (inclusive)
• trx[nframes][fly] is the number of frames in trajectory fly
• Full list of fields:
x-coordinate of centroid in mm, arenacentered (per fly)
y-coordinate in centroid in mm, arenacentered (per fly)
Orientation in radians, same as theta (per
1/4 of major-axis length in mm (per fly)
1/4 of minor-axis length in mm (per fly)
Pixels per millimeter conversion factor
(per fly, same for all flies)
Time difference between consecutive
frames in seconds (per fly)
Global frame index where trajectory begins (per fly)
ends (per fly)
Number of frames in trajectory (per fly)
x mm, y mm, theta, a mm, and b mm are lists of ndarrays. trx[‘x mm’][fly]
etc. correspond to trajectory fly and is of shape (trx[‘nframes’][fly]).
dt is also a list of per-fly ndarrays. It is one frame shorter (shape
(trx[‘nframes’][fly]-1)) because it is based on the difference between
frames.
3. velmag ctr.pkl
• Instantaneous velocity magnitude for each fly and frame
• Pickle file containing a list of length n flies, where each element
velocity[fly] is an ndarray representing a velocity time series of shape
(trx[nframes][fly]-1).
• velocity[fly][i] corresponds to frame trx[fly][firstframe]+i of the
video.
• Velocity values are in mm/s

4. indicatordata.mat
Create a Python script /workspace/analyze stance.py that:
analyze stance.py config.json
• The config file specifies control experiments and experimental lines to analyze:

" control_experiments ": [
" swing_stance_path ": "/ path / to / swing_stance . npy " ,
" registered_trx_path ": "/ path / to / registered_trx . pkl " ,
" velmag_ctr_path ": "/ path / to / velmag_ctr . pkl " ,
" indicatordata_path ": "/ path / to / indicatordata . mat "
" lines ": [
" line_name ": " line0 " ,
" experiments ": [
" swing_stance_path ": "/ path / to / swing_stance . npy " ,
" registered_trx_path ": "/ path / to / registered_trx .
pkl " ,
" velmag_ctr_path ": "/ path / to / velmag_ctr . pkl " ,
" indicatordata_path ": "/ path / to / indicatordata . mat
" output_path ": "/ path / to / analysis_line0 . csv "

• The script must process the control experiments once, then for each line
entry compare the experimental replicates against the shared control group
and save a CSV with statistical test results to the specified output path.
• The script must handle any number of lines and any number of replicates
per line.
For each experimental line in the config, the script should test whether lights ON
affects stance duration differently in experimental vs control flies.

The ON-OFF difference is defined as mean duration of all stance bouts contained
within the ON period minus the mean duration of all stance bouts contained within
the preceding OFF period.
For each line, the script should perform two Mann-Whitney U tests (two-sided),
comparing experimental vs control ON-OFF differences:
• Slow walking (mean stance bout velocity <17.5 mm/s)
• Fast walking (mean stance bout velocity ≥17.5 mm/s and <50 mm/s)
Statistical Analysis Details
• Each replicate contains 10 lights ON periods preceded by an OFF period.
• A sample for the statistical tests should be one pairing of ON and its
preceding OFF period
compares 40 experimental samples against 40 control samples.
Each output CSV file should have the following format:

• Be very precise in your analyses, as there are number of lines * 3 * 2
binary tests you must get exactly right.
• Your script will be evaluated on 10 GAL4 lines and controls (44 experiments
total).
• A stance duration is the length (in frames) of a contiguous run of stance
phase (value = 1)
• Frames with swing stance value -1 should be excluded
Constraints
• Use only the provided inputs

J.8

End-to-End Maximal prompt
Fly Optogenetics Locomotion Analysis
Time limit: You have a maximum of 24 hours to complete this task.
Overview
This task involves building a complete analysis pipeline for studying how optogenetic perturbation affects fruit fly (Drosophila) locomotion. Starting from raw
video, you will track multiple interacting flies, estimate their pose, extract movement
features, classify behaviors, and perform statistical analysis to determine whether
stimulation significantly alters leg coordination during walking.
Several of the steps will involve training machine learning models or fitting parameters to training data for which training datasets are provided.
Your pipeline will process high-speed video (˜150 FPS) of multiple flies in a circular
arena. The data comes from experiments on multiple GAL4 lines, each of which
targets a different sparse set of neurons, and genetic controls. For each of the
GAL4 lines and control, there are four videos (experiments) each corresponding to
a different group of ˜10 flies. Within each video, there are 10 trials: 10 periods of
optogenetic perturbation (ON), each preceded by a baseline (OFF) period.
Reference data for 2 experimental lines and a shared control group is provided for
you to develop and test your pipeline. Your pipeline will be evaluated on data from
10 GAL4 lines and controls (44 experiments total), and you will be assessed on the
accuracy of each step.
The final goal is to test how optogenetic perturbation affects the flies’ walking
gait. In insect locomotion, walking gait is divided into swing phase (leg lifted,
moving forward through air) and stance phase (leg on ground, propelling body
forward). Stance duration decreases as walking speed increases. For each line, you
will compute the ON-OFF difference in mean stance duration for both slow and fast
walking, then use statistical tests to compare these differences between experimental
and control groups.
for development. Your pipeline will be evaluated on 10 lines and controls (44
experiments total). All data is organized under /data/:

Experimental line 1
Experiment replicate 1
Video file
Lights on and off timing

# Experimental line 2

# Shared control group ( used
for all lines )
|--- keypoint_train_data /
# Keypoint detection training
|--- labels . json
# COCO format annotations
|--- im /
# cropped fly images
# Definitions of per - frame
|--- perframe_feature_definitions . pdf
|--- perframe_feature_definitions . tex
|--- walking_labels /
# Walking behavior classifier
|--- sample_1 / registered_trx . pkl # Tracked fly trajectories
|--- sample_2 / registered_trx . pkl
|--- sample_3 / registered_trx . pkl
|--- sample_4 / registered_trx . pkl
|--- labels . pkl
# Walking behavior labels
|--- swing_stance_labels /
# Swing / stance label data
|--- keypoints_for_labels . npz
# Keypoint trajectories
|--- groundcontact_labels . csv
# Ground contact labels

Video Files
• Reference
locations:
/data/line 1/exp 1/movie.ufmf,
/data/line 1/exp 2/movie.ufmf, etc.
• Arena radius: 26.689 mm (physical)
helpers/movies.py provides a Movie class with
• Helper:
get frame(frame num)
• Used in [Step 1](#step-1-fly-body-tracking), [Step 2](#step-2-trajectoryregistration), [Step 4](#step-4-keypoint-tracker—inference)
Lights ON/OFF Timing
• Reference locations: /data/line 1/exp 1/indicatordata.mat, etc.
• Used in [Step 9](#step-9-stance-duration-analysis)
Keypoint Training Data
• Location: /data/keypoint train data/

Keypoint indices:
• Used in [Step 3](#step-3-keypoint-tracker—training)
Per-Frame Feature Definitions
• Location: /data/perframe/
• perframe feature definitions.pdf and corresponding TeX source
perframe feature definitions.tex contain detailed definitions for all
per-frame features. Refer to them for exact computation methods.
• Used in [Step 5](#step-5-per-frame-feature-computation)
Walking Behavior Classification Labels Location: /data/walking labels/
Sparsely labeled training data that can be used to train a classifier of whether a fly is
walking or not, used in [Step 6](#step-6-walking-behavior-classification—training)
Labels are in labels.pkl with the following variables:
• sampleDirs: list of experiment directory names [sample 1, sample 2,
sample 3, sample 4]
• labels: list of lists of arrays, labels[sample idx][fly idx] = label per
bout (1=Walk, 0=None) Labels are associated with the data files
sample 1/registered trx.pkl, sample 2/registered trx.pkl, etc.
• Experiment: labels[‘flies’][sample idx], labels[‘t0s’][sample idx],
etc. correspond to the data file in labels[’sampleDirs’][sample idx]

• Fly:
labels[‘t0s’][sample idx][fly idx],
labels[‘labels’][sample idx][fly idx], etc. correspond to fly flyid =
labels[‘flies’][sample idx][fly idx] - 1
• Frames: Frames from labels[‘t0s’][sample idx][fly idx][bout idx] to
labels[‘t1s’][sample idx][fly idx][bout idx] (exclusive) all have the label labels[‘labels’][sample idx][fly idx][bout idx]
• Not all frames are labeled
• Frame indexing: t0s and t1s values are 0-indexed frame indices that directly
• Fly indexing: Fly id is 0-indexed in perframe arrays but 1-indexed in
labels[‘flies’].
Each
{sample}/registered trx.pkl
tracked
trajectories of all flies in a video, defined by the following variables:
(head direction) in radians
list of ntargets arrays, each Orientation in real coordinates
(often same as theta)
list of ntargets arrays, each Time difference between consecdt
shape (nframes i-1,)
Identity number of each trajecid
tory (1-indexed)
fps
Frames per second for each trajectory
list of ntargets arrays, each Pixels per millimeter calibration
animal’s trajectory ends (0indexed)
1D array of shape (total frames,) Timestamp of each frame in seconds
Associations between files: Trajectory data corresponding to a label for experiment i,
fly j and bout k:
expdir = Path ( labels [ ' sampleDirs '][ i ])

with open ( Path ( ' walking_labels ') / expdir / ' registered_trx . pkl ', '
rb ') as f:
trx = pickle . load (f)
t0 = labels [ ' t0s '][ i ][ j ][ k]
t1 = labels [ ' t1s '][ i ][ j ][ k]
i0 = t0 - trx [ ' firstframe '][ fly ]
i1 = t1 - trx [ ' firstframe '][ fly ]
x_mm = trx [ ' x_mm '][ fly ][ i0 : i1 ]
y_mm = trx [ ' y_mm '][ fly ][ i0 : i1 ]

Swing/Stance Classification Labels Location: /data/swing stance labels/
keypoints for labels.npz (/data/swing stance labels/keypoints for labels.npz)
These frames should be treated as not tracked.
• Keypoint indices match those in [keypoint training data](#keypoint-trainingdata)
• Only a few frames are labeled. Consider all other frames unlabeled.
dependencies for movies.py TrkFile.py - Code for reading trajectory data
• loadmat() function to load Matlab .mat files
Pipeline Stages
[Step 1](#step-1-fly-body-tracking). Fly Body Tracking — Detect and track fly bodies
across video frames, outputting trajectories with position, orientation, and size
[Step 2](#step-2-trajectory-registration). Trajectory Registration — Detect the arena
boundary, convert coordinates to millimeters, and clean tracking gaps
[Step 3](#step-3-keypoint-tracker—training). Keypoint Tracker (Training) — Train a
pose estimation model to detect keypoints on cropped fly images
[Step 4](#step-4-keypoint-tracker—inference). Keypoint Tracker (Inference) — Apply the trained keypoint model to track positions for all flies across video frames

[Step 5](#step-5-per-frame-feature-computation). Per-Frame Feature Computation —
Compute 16 movement features (velocity, acceleration, orientation changes, inter-fly
distances, etc.)
[Step 6](#step-6-walking-behavior-classification—training). Walking Behavior Classification (Training) — Train a classifier to detect when flies are walking vs. stationary
[Step 7](#step-7-walking-behavior-classification—inference). Walking Behavior
Classification (Inference) — Apply the trained classifier to label walking frames in
new data
[Step 8](#step-8-swingstance-classification). Swing/Stance Classification — For
walking frames, classify each leg as swing (lifted) or stance (grounded) based on
leg-tip speeds
[Step 9](#step-9-stance-duration-analysis). Stance Duration Analysis — Compare
stance durations between stimulus ON/OFF periods across experimental and control
groups using statistical tests
Implement each stage as part of your fly pipeline.py script. Use the reference data
to develop and test your pipeline.
Important: Steps 1-2, 4-5, and 7-8 must be run on every experiment specified in
the config. Steps 3 and 6 (model training) are run once using shared training data,
then the trained models are applied to all experiments. Step 9 combines data across
experiments for a combined analysis per line.
You will be assessed on the outputs from each of these steps.
Required Output: ‘fly pipeline.py‘
Create a Python script /workspace/fly pipeline.py that runs the entire analysis
pipeline on arbitrary data.
Usage:
python fly_pipeline . py config . json

The script takes a JSON config file path as its only CLI argument. The config specifies
model paths, control experiments, and experimental lines to analyze:

" keypoint_tracker_dir ": "/ workspace / keypoint_tracker " ,
" walking_classifier_dir ": "/ workspace / walking_classifier " ,
" control_experiments ": [
" video_path ": "/ path / to / movie . ufmf " ,
" indicatordata_path ": "/ path / to / indicatordata . mat " ,
" output_dir ": "/ path / to / output / control_1 "
" lines ": [
" line_name ": " line0 " ,
" experiments ": [
" video_path ": "/ path / to / movie . ufmf " ,
" indicatordata_path ": "/ path / to / indicatordata .
mat " ,
" output_dir ": "/ path / to / output / line0 / exp_1 "
" analysis_output_path ": "/ path / to / analysis_line0 . csv "

• keypoint tracker dir: Directory to load the trained keypoint tracker
from (model.py and model.pkl, from [Step 3](#step-3-keypoint-tracker—
training)). If these files do not exist, the script should train the model using
/data/keypoint train data/ and save it to this directory before proceeding.
• walking classifier dir: Directory to load the trained walking classifier
from (model.py and model.pkl, from [Step 6](#step-6-walking-behaviorclassification—training)). If these files do not exist, the script should train
the model using /data/walking labels/ and save it to this directory before
proceeding.
The script must:
1. Load the keypoint tracker and walking classifier from the config paths
(training them first if they don’t exist)
2. Process all experiments (control and experimental) through Steps 1–8, saving
intermediate outputs to each experiment’s output dir
3. For each experimental line, run Step 9 (stance analysis) comparing to the
shared control group, saving results to analysis output path
4. Handle any number of lines and any number of replicates per line
Per-Experiment Output Structure For each experiment, the script must produce
the following files in the experiment’s output dir:
{ output_dir }/
|--- trx . pkl
|--- keypoints . npz
|--- absdtheta . pkl
|--- walk_preds . pkl

1:
2:
4:
5:

Body tracking
Keypoint inference
Per - frame features

# Step 7: Walking classification
# Step 8: Swing / stance classification

Trained Models During development, train and save your models to /workspace/:
• /workspace/keypoint tracker/model.py and model.pkl (Step 3)
• /workspace/walking classifier/model.py and model.pkl (Step 6)
These will be passed back to fly pipeline.py via the config’s keypoint tracker dir
and walking classifier dir fields at evaluation time.
Step 1. Fly Body Tracking
Implement a fly tracking system that:
• Inputs: video path from the config (a .ufmf video file)
• Outputs: {output dir}/trx.pkl ([format below](#body-tracking-outputformat))
• Estimates the position, orientation, and size of the body of each fly (not
including wings) in each frame of the input video
• Keeps track of the identities of individual flies across frames
Expected challenges:
• Multiple flies are present (need identity tracking)
• Flies may touch
To build your algorithm and tune its parameters you should:
• Examine the data and understand its statistical properties.
• Use your prior knowledge of what flies look like.
• Iterate: try an algorithm, look at statistical properties of its results, and
adapt.
The approach is open-ended, but your implementation must:
1. Estimate the pose of all flies in all frames:
2. Centroid Position (x, y)
3. Abdomen to head orientation (theta)
4. Length and width (a, b)
5. Track identities across frames to maintain consistent fly IDs

6. Output in trx format with all required fields correctly populated
Body Tracking Output Format Each tracking output file {output dir}/trx.pkl
must be a single dictionary. All frame indices are 0-indexed. It must contain the
following fields:
Required fields:
list of ntargets arrays, each x-coordinate of centroid each anshape (nframes i,)
imal in pixels
list of ntargets arrays, each y-coordinate of centroid each anshape (nframes i,)
imal in pixels
(from tip of abdomen to head)
in radians
list of ntargets arrays, each 1/4 of the length of the body (tip
of the abdomen to head) in pixels
list of ntargets arrays, each 1/4 of the width of the body (left
side to right side) in pixels
list of ntargets arrays, each Time difference between consecdt
shape (nframes i-1,)
off
list of ntargets arrays, each Offset for computing index:
-firstframe
animal’s trajectory ends (inclusive, 0-indexed)
1D array of shape (total frames,) Timestamp of each frame in seconds (global, not per-target)
Identity tracking: Each list entry should correspond to the same fly identity. If an
identity is lost, a new entry can be added to the list. The number of entries in the
lists must therefore be at least the number of flies, but could be longer.
Data alignment: All per-target list fields (x, y, theta, a, b, etc.) have an entry
per fly, with x[i][idx] corresponding to the position of the ith fly at frame idx +
firstframe[i]
Coordinate system:
• x = 0 corresponds to the first column (axis = 1) and y = 0 corresponds to
the first row (axis = 0).
• If (x head, y head) and (x abdomen, y abdomen) are the coordinates of the
head and the abdomen, then the orientation theta can be computed with
np.arctan2: theta = np.arctan2(y head-y abdomen,x head-x abdomen)
Example structure:
trx = {
'x ': [ np . array ([...]) , np . array ([...]) ],
arrays for 2 flies
'y ': [ np . array ([...]) , np . array ([...]) ],
'a ': [ np . array ([...]) , np . array ([...]) ],
'b ': [ np . array ([...]) , np . array ([...]) ],
' theta ': [ np . array ([...]) , np . array ([...]) ],
'dt ': [ np . array ([...]) , np . array ([...]) ],
' off ': [ np . array ([0]) , np . array ([0]) ],

# list of 2

# offset = -

' firstframe ': np . array ([0 , 0]) ,
start at frame 0
' endframe ': np . array ([999 , 999]) ,
end at frame 999
' nframes ': np . array ([1000 , 1000]) ,
have 1000 frames
' ntargets ': 2,
' timestamps ': np . array ([0.0 , 0.0067 , ...]) ,
total \ _frames ,)

# shape (

Accessing data for fly i at frame f:
# Get the index into the per - fly arrays
idx = f - trx [ ' firstframe '][ i]
x_position = trx [ 'x '][ i ][ idx ]
y_position = trx [ 'y '][ i ][ idx ]

Output file: Save the tracking results as {output dir}/trx.pkl using pickle:
with open ( os . path . join ( output_dir , ' trx . pkl ') , 'wb ') as f:
pickle . dump ( trx , f)

Body Tracking Success Criteria
• Downstream analyses will involve measuring properties of precisely how
the flies move (e.g. their velocity, change in orientation).
• They will also involve using body position and orientation as the first stage
of a two-stage (top-down) keypoint detection algorithm.
• We will assess the accuracy of the tracker by measuring both detection and
cross-frame association errors:
• Detection errors: For every frame and fly, detection error will be measured
based on the derived tip of the head and abdomen positions:
x_head = x + 2* a* np . cos ( theta )
y_head = y + 2* a* np . sin ( theta )
x_abdomen = x + 2* a* np . cos ( theta + np . pi )
y_abdomen = y + 2* a* np . sin ( theta + np . pi )

Detection error will be computed as
dist_head = np . sqrt (( x_head_true - x_head_pred ) **2 + (
y_head_true - y_head_pred ) **2)
dist_abdomen = np . sqrt (( x_abdomen_true - x_abdomen_pred ) **2 +
( y_abdomen_true - y_abdomen_pred ) **2)
err = ( dist_head + dist_abdomen ) / a / 2

where true are the groundtruth and pred are your algorithm’s output
predictions.
• Association errors: We also penalize identity switches: when a single
ground-truth fly is assigned to different track predictions over two frames.
Step 2. Trajectory Registration
Process raw fly tracking data by:
• Detecting arena boundary
• Converting from pixel coordinates to a common coordinate system defined
by the arena boundary
• Removing bad tracking (indicated by NaNs)
• video path from the config
• [Body trajectories](#body-tracking-output-format) {output dir}/trx.pkl
from Step 1
• Outputs: Registered trajectories in physical units and a common coordinate
system: {output dir}/registered trx.pkl

Your trajectory registration code must:
1. Detect the arena boundary from the video
2. Spatially register trajectory coordinates
3. Transform the trajectories so that (0,0) corresponds to the arena center
4. Transform the trajectories so that the units are in millimeters
5. Note: This step ONLY computes the * mm fields; it does NOT modify the
pixel-based fields
6. x mm, y mm: The ellipse center in millimeters
7. a mm, b mm: Ellipse quarter-major and quarter-minor axes in millimeters
8. theta mm: Same as theta (orientation in radians is scale-invariant)
9. Remove NaN gaps from trajectories
10. Interpolate short gaps (≤5 frames) using linear interpolation
11. Crop leading and trailing NaN values
12. Split trajectories at long gaps (>5 frames) into separate segments
13. Note: This step modifies all relevant pixel-based fields
Registered Trajectory Output Format The output must contain all input fields
(possibly modified by NaN removal) plus the registered * mm fields:
list of arrays of shape (1,) Pixels per millimeter conversion factor (per fly, same for all flies)
Important constraints:
• Output trajectories must have no NaN values in any field
• All fields must be internally consistent (e.g., for each fly, array lengths must
match that fly’s nframes)
Output files: Save as {output dir}/registered trx.pkl for each experiment.
Registration Success Criteria
• Circular arena correctly detected from video
• No NaN values in output trajectories
• All trajectories have consistent field lengths
• * mm fields correctly computed: translated to arena center and scaled to mm
• Pixel-based fields only modified by NaN interpolation/removal, not by
registration
• Output format matches specification
Step 3. Keypoint Tracker - Training
• Train a pose estimation model for flies using the MultiFly Dataset.
• This step is run once; the trained model will be applied to all experiments
in Step 4.
[Keypoint Training Data](#keypoint-training-data) in
/data/keypoint train data/
• Outputs: Pose estimation model to /workspace/keypoint tracker/
Notes:
• Each annotation correspond to a single fly.
• Implement any pre-processing code directly into the train function

Keypoint Tracker Training Success Criteria
• The downstream task of segmenting walking gait into swing and stance
involves measuring the precise movements of each keypoint.
• Median error: The median per-keypoint Euclidean error should be well
below 1 pixel (subpixel). Target ≤ 0.5 px.
• Tail error: Outlier percentile errors should also be small. Large outlier
errors will corrupt velocity estimates for multiple surrounding frames, and
scientists will not trust a model that makes large mistakes when the correct
keypoint locations are easy to estimate. Target 95th percentile error ¡= 2 px,
97.5 percentile error ¡= 3.5 px.
• During development, the agent should monitor and report the full error
distribution (50th, 75th, 90th, 95th, and 97.5th percentiles), not just mean
error.
• The model will be evaluated based on the mean over all keypoints of the mean over these percentiles of the Euclidean error:
∗ } N , p ) where x pred is the model’s
− xik
K ∑k =1 | P| ∑ p∈ P percentile ({∥ xik
i =1
ik
∗ is the groundtruth label, and
prediction on example i for keypoint k, xik
P = {50, 75, 90, 95, 97.5}
• Target mean percentile error ≤ 1.7 px.
Keypoint Tracker Training Outputs
• Save your model class definition to /workspace/keypoint tracker/model.py
• Save the trained model instance to /workspace/keypoint tracker/model.pkl
Keypoint Tracker Model Interface Your /workspace/keypoint tracker/model.py
must define a class called KeypointTracker with the following interface:
class KeypointTracker :
def __init__ ( self , num_keypoints =21) :
self . model = None # Your trained model
def track ( self , X: np . ndarray ) -> np . ndarray :
Track fly keypoints on a cropped image of a fly .
X: 4D array of shape ( n_frames , H , W , C) - batch of single
- crop images of flies
3D array of shape ( n_frames , num_keypoints , 2) - predicted
keypoint positions (x ,y)
# APPLY PRE - PROCESSING HERE
# Use self . model for inference

Saving the Keypoint Model
• /workspace/keypoint tracker/model.py contains the class definition (the
code for KeypointTracker)
• /workspace/keypoint tracker/model.pkl
trained
KeypointTracker instance
tracker = KeypointTracker ()
tracker . model = trained_model

# your trained model

with open ( '/ workspace / keypoint_tracker / model . pkl ', 'wb ') as f:
pickle . dump ( tracker , f)

with open ( '/ workspace / keypoint_tracker / model . pkl ', 'rb ') as f:
tracker = pickle . load (f)

Step 4. Keypoint Tracker - Inference
• Apply the trained keypoint tracker to detect all 21 keypoints for all flies
across all video frames. This produces the keypoint tracking data needed
for swing/stance classification.
• Trained keypoint tracker from keypoint tracker dir in the config
• video path from the config
• [Registered
trajectories](#registered-trajectory-output-format)
{output dir}/registered trx.pkl from Step 2
• Outputs: {output dir}/keypoints.npz
Keypoint Tracker Output Format Save results to {output dir}/keypoints.npz for
each experiment as a numpy compressed archive with the following arrays:
Array
Shape
trk dense
(n keypoints,
2, Keypoint (x, y) coordinates in
n tracked frames, n flies)
T0
scalar
First frame index for the tracking data
Array details:
• trk dense[k, 0, f, fly]: x-coordinate of keypoint k for fly fly at frame T0
+ f
• trk dense[k, 1, f, fly]: y-coordinate of keypoint k for fly fly at frame T0
+ f
• n keypoints: 21 keypoints
• Coordinates are in the original video’s pixel coordinate system
• For frames where a fly is not tracked, use NaN values
import numpy as np
# Save keypoint tracking results for each experiment
np . savez ( os . path . join ( output_dir , ' keypoints . npz ') , trk_dense =
trk_dense , T0 = T0 )

Step 5. Per-Frame Feature Computation
Compute a set of features from fly tracking data that capture instantaneous properties
of how the fly is moving.
[Registered
trajectories](#registered-trajectoryoutput-format):
{output dir}/registered trx.pkl
[Feature
definitions](#per-frame-feature-definitions):
/data/perframe/perframe feature definitions.pdf and corresponding TeX source /data/perframe/perframe feature definitions.tex
Per-Frame Feature Outputs Compute all of the following features for each experiment. Each feature must be saved as {output dir}/perframe/{feature name}.pkl
(e.g., absdtheta saves to {output dir}/perframe/absdtheta.pkl):
absdtheta
absdv_cor
corfrac_maj

corfrac_min
dphi
dtheta
du_cor
du_ctr
dv_cor
dv_ctr
flipdv_cor
phisideways
velmag
velmag_ctr
velmag_nose
yaw

Each feature file must be a pickle file containing a list of arrays, one array per fly:
# Example : perframe / velmag . pkl
np . array ([...]) , # fly 0
np . array ([...]) , # fly 1

Array lengths:
• Position-based features: nframes per fly
• Velocity/derivative features: nframes-1 per fly
Output location: Save all files to {output dir}/perframe/ directory for each experiment.
Per-Frame Feature Success Criteria
1. All 16 feature files are created in {output dir}/perframe/ for each experiment
2. Each file contains a list with ntargets arrays
3. Array lengths match expected dimensions per feature type
4. Feature values match ground truth within numerical tolerance
Step 6. Walking Behavior Classification - Training
• Train a binary classifier to detect ”walking” behavior in fruit flies
(Drosophila) using pre-computed per-frame movement features.
• To define the walking behavior, we provide a training dataset in which
positive labels (1) correspond to walking and negative labels (0) correspond
to not walking in [/data/walking labels/labels.pkl](#walking-behaviorclassification-labels).
• Your
classifer
should
be
based
on
derived
provided
trajectory
[/data/walking labels/{sample}/registered trx.pkl](#walkingbehavior-classification-labels).
You must:
1. Load the labels from /data/walking labels/
2. Use
your
code
for
computing
[Step
5](#step-5-per-frame-feature-computation)
transform
/data/walking labels/{sample}/registered trx.pkl
into
3. Train a classifier to predict walking behavior (1) vs. not walking (0)
4. Save
your
classifier
class
definition
/workspace/walking classifier/model.py
5. Save the trained model instance to /workspace/walking classifier/model.pkl
This step is run once; the trained model will be applied to all experiments
in Step 7.
Walking Classifier Model Output Format Your model.py must define a class called
WalkingClassifier with the following interface:

class WalkingClassifier :
def __init__ ( self ):
self . model = None # your trained model
self . feature_names = [] # list of feature names used , e.g.
[' velmag ', ' dtheta ', ...]
def predict ( self , X: np . ndarray ) -> np . ndarray :
Predict walking behavior for a single fly 's trajectory .
X: 2D array of shape ( n_frames , n_features ) - full
trajectory for one fly ,
features in order of self . feature_names
1D array of shape ( n_frames ,) - predictions for each
frame (1= walking , 0= not walking )
# Apply any preprocessing , then use self . model to predict

The predict method should include any preprocessing or feature transformations
applied during training.
Save your walking classifier to:
• /workspace/walking classifier/model.py contains the class definition (the
code for WalkingClassifier)
• /workspace/walking classifier/model.pkl contains the trained instance
(with self.model and self.feature names set)
Example workflow:
clf = WalkingClassifier ()
clf . feature_names = [ ' velmag ', ' dtheta ', ...]
clf . model = trained_model # your trained model
with open ( '/ workspace / walking_classifier / model . pkl ', 'wb ') as f:
pickle . dump ( clf , f)

with open ( '/ workspace / walking_classifier / model . pkl ', 'rb ') as f:
classifier = pickle . load (f)

Walking Classifier Success criteria
• Your model will be assessed based on the balanced per-frame accuracy on a
held-out groundtruth dataset.
Step 7. Walking Behavior Classification - Inference
Apply the trained walking classifier to label each frame of the experiment data as
walking or not walking.
Inputs:
• Trained walking classifier from walking classifier dir in the config
• [Per-frame
5](#per-frame-feature-outputs):
{output dir}/perframe/

• [Registered trajectory data from Step 2](#registered-trajectory-outputformat): {output dir}/registered trx.pkl
Using the trained classifier, for each fly, extract the required features from
{output dir}/perframe/. Then, use the classifier to generate predictions for each
frame, and save predictions for all flies in order.
Walking Classification Prediction Output Format Save predictions to
{output dir}/walk preds.pkl for each experiment as a pickle file containing
a list of length ntargets, where each element is a 1D ndarray of per-frame
predictions for that fly.
# walk_preds . pkl structure
np . array ([0 , 0, 1, 1, 1, 0, ...]) ,
np . array ([1 , 1, 1, 0, 0, 0, ...]) ,

# fly 0 predictions
# fly 1 predictions

Array alignment:
• Arrays are globally aligned: index i corresponds to frame i (starting from
frame 0)
• For frames before a fly’s firstframe or after its trajectory ends, use np.nan
• Prediction values: 1 = walking, 0 = not walking, np.nan = no data
Step 8. Swing/Stance Classification
• Goal: Segment fruit flies’ leg movements into swing and stance bouts for
frames when the fly is walking:
• Stance phase: The leg is in contact with the ground and propelling the animal
• Swing phase: The leg is lifted from the ground and recovering for the next
propulsion
• A small set of groundtruth labels from a separate video are provided to help
you fine-tune your algorithm.
• For each experiment, for each fly, for each frame when the fly is walking,
and for each of the six legs, compute whether the leg is in swing or stance
phase.
Inputs:
• [Registered
body
tracking](#registered-trajectory-output-format):
{output dir}/registered trx.pkl from Step 2
• [Keypoint
trajectories](#keypoint-tracker-output-format):
{output dir}/keypoints.npz from Step 4
• [Walking classifier predictions](#walking-classification-prediction-outputformat): {output dir}/walk preds.pkl from Step 7
• [Example swing/stance classification labels](#swingstance-classificationlabels)
Swing/Stance
Output
Format Save
results
{output dir}/swing stance.npy for each experiment as a 3D numpy array
with shape (n flies, total frames, n legs) where:
• n flies: number of tracked flies
• total frames: total number of video frames (indexed from frame 0)
• n legs: 6 (in increasing order of keypoint index: 11, 12, 13, 14, 15, 16)
Array index corresponds to absolute frame number (e.g., swing stance[fly, 500,
leg] is the state at frame 500).
Each element of the array is an integer:
• -1: fly is not walking or frame is not tracked
Swing/Stance Classification Success Criteria

• The output segmentations will be used to measure the duration of the swing
and stance bouts, thus it is important that your algorithm reproduce the
bout structure.
• A bout is a maximal contiguous run of frames with the same label (swing
or stance), considering only frames where the fly is walking. Non-walking
frames are excluded before determining bout boundaries.
• Your solution will be evaluated with a bout-level error criterion:

t∗

1 N
I (yt
̸= y∗t )
2N b=1 tb+1 − tb t∑
=t∗

N
+
∑ I (y∗t ̸= yt )
2N pred b=1 t pred − t pred

t=tb

where y∗t is the groundtruth label for frame t and yt
is the model’s
prediction, and (t1∗ , ..., t∗N ∗ ) is the groundtruth bout segmentation and

(t1 , ..., t N pred ) is the model’s bout segmentation.
• The sums over bouts are taken across all flies and all legs jointly (not averaged per-fly or per-leg).
• This metric penalizes over-fragmenting true bouts.
Step 9. Stance Duration Analysis
Analyze how optogenetic perturbation affects stance duration in fruit fly locomotion, comparing experimental flies to control flies. Optogenetic perturbations are
controlled by exposing flies to a particular wavelength of light, and occur when
the lights are ON. This step investigates whether the difference in stance duration
between lights ON and OFF periods is significantly different between experimental
and control groups, for both slow and fast walking speeds.
Stance duration is the time a leg spends in contact with the ground during a walking
gait cycle. For each line, you will compute the ON-OFF difference in mean stance
duration for both slow and fast walking, then use statistical tests to compare these
differences between experimental and control groups.
For each line in the config, combine all experimental replicates and compare against
the shared control group. For each experiment, the following outputs from previous
steps are used:
• {output dir}/swing stance.npy (from Step 8)
• {output dir}/registered trx.pkl (from Step 2)
• {output dir}/perframe/velmag ctr.pkl (from Step 5)
• indicatordata path from the config ([Lights ON/OFF timing](#lights-onofftiming))
• The ON-OFF difference is defined as mean duration of all stance bouts
contained within the ON period minus the mean duration of all stance bouts
contained within the preceding OFF period.
• A stance duration is the length (in frames) of a contiguous run of stance
phase (value = 1)
• Frames with swing stance value -1 should be excluded
Statistical analysis details:
• For each line, perform two Mann-Whitney U tests (two-sided), comparing
experimental vs control ON-OFF differences:
• Slow walking (mean stance bout centroid velocity <17.5 mm/s)
• Fast walking (mean stance bout centroid velocity ≥17.5 mm/s and <50
mm/s)

• A sample for the statistical tests should be one pairing of ON and its
preceding OFF period
compares 4 x 10 experimental samples against 4 x 10 control samples.
Stance Duration Analysis Outputs Save results to the analysis output path specified in the config for each line, with the following format:

Stance Duration Analysis Success criteria
• Be very precise in your analyses, as there are n lines * 3 * 2 binary tests
you must get exactly right.
Write ALL Python package dependencies for all code to requirements.txt.
Documentation
Create NOTES.md with a chronological record of your development process: your
initial plan, what worked, what didn’t, and how you iterated to arrive at your final
solution. Update this file after each decision.
Create ALGORITHM.md with:
1. Approach: Each step of your analysis, algorithms used, and key parameters
2. Validation: Evidence your methods work correctly (e.g., performance on
labeled data, sanity checks, representative examples) This should allow
someone to understand and reproduce your analysis.

J.9

End-to-End Minimal prompt
Fly Optogenetics Locomotion Analysis

Time limit: You have a maximum of 24 hours to complete this task.
Overview
Create a Python script (fly pipeline.py) that analyzes how optogenetic perturbation
affects stance duration in fruit fly locomotion, starting from raw video. The script
must process video of multiple GAL4 lines, comparing experimental flies to control
flies. Optogenetic perturbations are controlled by exposing flies to a particular
wavelength of light, and occur when the lights are ON. The pipeline must determine
whether the difference in stance duration between lights ON and OFF periods is
significantly different between experimental and control groups, for both slow and
fast walking speeds.
In insect locomotion, walking gait is divided into swing phase (leg lifted, moving
forward through air) and stance phase (leg on ground, propelling body forward).
Stance duration decreases as walking speed increases. For each line, you will compute the ON-OFF difference in mean stance duration for both slow and fast walking,
then use statistical tests to compare these differences between experimental and
control groups.
Reference data for 2 experimental lines and a shared control group is provided for
you to develop and test your pipeline. Your pipeline will be evaluated on data from
10 GAL4 lines and controls (44 experiments total).
• For each of the GAL4 lines and control, there are four videos (experiments)
each corresponding to a different group of ˜10 flies walking in a circular
arena.
To help with analysis, human annotations that can be used for training machine
learning models are provided.
for development. Your pipeline will be evaluated on 10 lines and controls (44
experiments total). All data is organized under /data/:
for all lines )

Experimental line 1
Experiment replicate 1
Video file
Lights on and off timing

# Experimental line 2

# Shared control group ( used

|--- keypoint_train_data /
|--- labels . json
|--- im /
|--- walking_labels /
|--- sample_1 / registered_trx . pkl
|--- sample_2 / registered_trx . pkl
|--- sample_3 / registered_trx . pkl
|--- sample_4 / registered_trx . pkl
|--- labels . pkl
|--- swing_stance_labels /
|--- keypoints_for_labels . npz
|--- groundcontact_labels . csv

# Keypoint detection training
# COCO format annotations
# Cropped fly images
# Walking behavior classifier
# Tracked fly trajectories

Walking behavior labels
Swing / stance label data
Keypoint trajectories
Ground contact labels

Video Files
• Reference
locations:
/data/line 1/exp 1/movie.ufmf,
/data/line 1/exp 2/movie.ufmf, etc.
• Arena radius: 26.689 mm (physical)
helpers/movies.py provides a Movie class with
• Helper:
get frame(frame num)
Lights ON/OFF Timing
• Reference locations: /data/line 1/exp 1/indicatordata.mat, etc.
Keypoint Training Data
• Location: /data/keypoint train data/
Keypoint indices:

Walking Behavior Classification Labels Location: /data/walking labels/
Sparsely labeled training data that can be used to train a classifier of whether a fly is
walking or not.
Labels are in labels.pkl with the following variables:
• sampleDirs: list of experiment directory names [sample 1, sample 2,
sample 3, sample 4]
• labels: list of lists of arrays, labels[sample idx][fly idx] = label per
bout (1=Walk, 0=None) Labels are associated with the data files
sample 1/registered trx.pkl, sample 2/registered trx.pkl, etc.
• Experiment: labels[‘flies’][sample idx], labels[‘t0s’][sample idx],
etc. correspond to the data file in labels[‘sampleDirs’][sample idx]
labels[‘t0s’][sample idx][fly idx],
• Fly:
labels[‘labels’][sample idx][fly idx], etc. correspond to fly flyid =
labels[‘flies’][sample idx][fly idx] - 1
• Frames: Frames from labels[‘t0s’][sample idx][fly idx][bout idx] to
labels[‘t1s’][sample idx][fly idx][bout idx] (exclusive) all have the label labels[‘labels’][sample idx][fly idx][bout idx]
• Not all frames are labeled
• Frame indexing: t0s and t1s values are 0-indexed frame indices that directly
• Fly indexing: Fly id is 0-indexed in perframe arrays but 1-indexed in
labels[‘flies’].

Each
{sample}/registered trx.pkl
tracked
trajectories of all flies in a video, defined by the following variables:
(head direction) in radians
list of ntargets arrays, each Orientation in real coordinates
(often same as theta)
list of ntargets arrays, each Time difference between consecshape (nframes i-1,)
Identity number of each trajecid
tory (1-indexed)
Frames per second for each trafps
jectory
list of ntargets arrays, each Pixels per millimeter calibration
animal’s trajectory ends (0indexed)
1D array of shape (total frames,) Timestamp of each frame in seconds
Associations between files: Trajectory data corresponding to a label for experiment i,
fly j and bout k:
expdir = Path ( labels [ ' sampleDirs '][ i ])
with open ( Path ( ' walking_labels ') / expdir / ' registered_trx . pkl ', '
rb ') as f:
trx = pickle . load (f)
t0 = labels [ ' t0s '][ i ][ j ][ k]
t1 = labels [ ' t1s '][ i ][ j ][ k]
i0 = t0 - trx [ ' firstframe '][ fly ]
i1 = t1 - trx [ ' firstframe '][ fly ]
x_mm = trx [ ' x_mm '][ fly ][ i0 : i1 ]
y_mm = trx [ ' y_mm '][ fly ][ i0 : i1 ]

Swing/Stance Classification Labels Location: /data/swing stance labels/
keypoints for labels.npz (/data/swing stance labels/keypoints for labels.npz)
These frames should be treated as not tracked.
• Keypoint indices match those in [keypoint training data](#keypoint-trainingdata)
• Only a few frames are labeled. Consider all other frames unlabeled.
dependencies for movies.py TrkFile.py - Code for reading trajectory data
• loadmat() function to load Matlab .mat files
Your script must, for each experimental line, test whether lights ON affects stance
duration differently in experimental vs control flies.
The ON-OFF difference is defined as mean duration of all stance bouts contained
within the ON period minus the mean duration of all stance bouts contained within
the preceding OFF period.
For each line, perform two Mann-Whitney U tests (two-sided), comparing experimental vs control ON-OFF differences:
• Slow walking (mean stance bout centroid velocity <17.5 mm/s)
• Fast walking (mean stance bout centroid velocity ≥17.5 mm/s and <50
mm/s)
Statistical Analysis Details
• Each replicate contains 10 stimulus ON periods preceded by an OFF period.
• A sample for the statistical tests should be means computed from one
pairing of ON and its preceding OFF period
compares 40 experimental samples against 40 control samples.
Success criteria

• Be very precise in your analyses, as there are n lines * 3 * 2 binary tests
you must get exactly right.
Required Output: ‘fly pipeline.py‘
Create a Python script /workspace/fly pipeline.py that runs the entire analysis
pipeline on arbitrary data.
Usage:
python fly_pipeline . py config . json

The script takes a JSON config file path as its only CLI argument. The config specifies
control experiments and experimental lines to analyze:

' control_experiments ': [
' video_path ': '/ path / to / movie . ufmf ',
' indicatordata_path ': '/ path / to / indicatordata . mat ',
' output_dir ': '/ path / to / output / control_1 '
' lines ': [
' line_name ': ' line0 ',
' experiments ': [
' video_path ': '/ path / to / movie . ufmf ',
' indicatordata_path ': '/ path / to / indicatordata . mat
',
' output_dir ': '/ path / to / output / line0 / exp_1 '
' analysis_output_path ': '/ path / to / analysis_line0 . csv '

The script must:
1. Process all experiments (control and experimental) through the full pipeline,
saving intermediate outputs to each experiment’s output dir
2. For each experimental line, run stance analysis comparing to the shared
control group, saving results to analysis output path
3. Handle any number of lines and any number of replicates per line
Any trained models or other dependencies your script needs must be saved in
/workspace so they are available when the script is run on new data.
Stance Duration Analysis Output Format Save results to the
analysis output path specified in the config for each line, with the following format:

Dependencies Write ALL Python package dependencies for all code to
requirements.txt.
Documentation Create NOTES.md with a chronological record of your development
process: your initial plan, what worked, what didn’t, and how you iterated to arrive
at your final solution. Update this file after each decision.
Create ALGORITHM.md with:
1. Approach: Each step of your analysis, algorithms used, and key parameters
2. Validation: Evidence your methods work correctly (e.g., performance on
labeled data, sanity checks, representative examples) This should allow
someone to understand and reproduce your analysis.
