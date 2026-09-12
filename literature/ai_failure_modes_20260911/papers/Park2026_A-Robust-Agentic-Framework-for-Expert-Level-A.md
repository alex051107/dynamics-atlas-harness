# A Robust Agentic Framework for Expert-Level Automation of Atomistic Simulations

**Authors:** Park, Yutack; Chung, Yeonwoo; You, Jinmu; Kim, Jisu; Ju, Suyeon; Han, Seungwu
**Year:** 2026
**Venue:** arXiv preprint
**arXiv:** 2606.09422
**Source PDF URL:** https://arxiv.org/pdf/2606.09422
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---
A Robust Agentic Framework for Expert-Level Automation of
Atomistic Simulations

Yutack Park1† , Yeonwoo Chung1† , Jinmu You1 , Jisu Kim1 , Suyeon Ju1 , Seungwu Han1,2,3*

Department of Materials Science and Engineering, Seoul National University, Seoul, 08826,
Republic of Korea.
Research Institute of Advanced Materials, Seoul National University, Seoul, 08826, Republic of
Korea.
Center for AI and Natural Sciences, Korea Institute for Advanced Study, Seoul, 02455, Republic of
Korea.

*Corresponding author(s). E-mail(s): hansw@snu.ac.kr;
†
These authors contributed equally to this work.
Abstract
Traditionally, atomistic simulation has been constrained by the computational scaling limits of ab initio methods
and the parameterization overhead of empirical force fields. The recent emergence of universal machine learning
interatomic potentials has significantly mitigated these bottlenecks, offering near-quantum accuracy and generalizability across diverse chemical spaces at a fraction of the computational cost. However, this shift has relocated
the bottleneck to the human dimension: time-consuming mechanical processes, such as input preparation and data
analysis, now dominate the research lifecycle. We introduce Paimon, a Platform for Agentic Integration in Materials
Optimization and Nanoscale-simulations. Through hundreds of trials on an expert-level liquid electrolyte simulation, we show that Paimon substantially improves the reliability of agentic workflows by suppressing silent errors:
plausible yet physically incorrect results. We further demonstrate that Paimon can cooperate with an external
scientific agent and autonomously reproduce simulation methodologies from the literature. As an agent harness
for atomistic simulations, Paimon affords researchers a continuous, science-centric workflow throughout the entire
simulation lifecycle.

1 Introduction

input files, designing workflows, and analyzing data has
become the primary bottleneck in the entire research
pipeline in computational materials science. Automating these processes would accelerate large-scale data
generation and the discovery of novel materials. Furthermore, it would enable less-experienced researchers to
perform simulations with ease, thereby facilitating the
widespread adoption of atomistic-scale modeling.
Efforts to automate atomistic simulations have
gained significant momentum in recent years [9–12].
For instance, frameworks such as Atomate [12] and
AiiDA [10] have proven effective in automating standard
DFT calculation workflows. However, these traditional
rule-based approaches often lack the flexibility required
to handle the nuances of more complex or unconventional
simulations [13]. While recent advancements in artificial intelligence (AI), in particular large language models
(LLMs), have introduced the capability to generate code
and inputs [14] for on-the-fly automation, significant

Atomistic simulations are essential in materials science
because they reveal the fundamental physical mechanisms and structure–property relationships that govern
macroscopic behavior at the most basic level. However,
they are also technically demanding and often require
solid knowledge in physics and chemistry. For example, density functional theory (DFT) calculations require
careful interpretation based on quantum mechanics [1],
while classical simulations based on interatomic potentials demand specialized knowledge to accurately model
large-scale systems and analyze simulation results [2].
Recently, the emergence of universal machinelearning interatomic potentials (uMLIPs) has begun to
lower these barriers, particularly by enabling near-DFTlevel accuracy at significantly lower computational cost
and with reduced manual effort in potential development [3–8]. Consequently, human effort in preparing

challenges remain. Specifically, the probability of failure
increases substantially when LLMs are applied to multistep, long-horizon tasks [15, 16] inherent in atomistic
modeling. Furthermore, the limited parametric knowledge [17, 18] of current LLMs often falls short of the
specialized expertise required to execute sophisticated,
expert-level simulations [19–21].
These challenges, however, are becoming surmountable with the integration of agentic AI [22, 23]. By
adopting advanced workflows such as dynamic task
decomposition [24–26] and self-reflection [27, 28], agentic
AI frameworks can significantly enhance the execution
accuracy of LLMs [22, 23]. Recent studies, including
AtomAgent [29], El Agente [30], and CASCADE [31],
have begun to demonstrate this potential [13, 21, 29, 31–
38]. Nevertheless, many existing applications remain limited to relatively straightforward simulation procedures.
Furthermore, although several reports mention various
errors made by agents [32, 34, 38], current evaluations
remain largely qualitative, with limited quantitative
evaluations and systematic failure analysis.
In this work, we present Paimon (Platform for Agentic Integration in Materials Optimization and Nanoscalesimulations), an agentic AI framework designed for the
end-to-end automation of atomistic simulations where
computational procedures are well-developed. Paimon
translates natural language queries into comprehensive
simulation workflows such as executing tasks, analyzing data, and delivering results with a level of rigor and
expertise comparable to those found in scientific literature. Central to our approach is the modularity. The
architecture of Paimon allows for the seamless integration of domain-specific agents and simulation procedures
developed across diverse research fields. Such a modular
framework ensures that Paimon remains highly scalable,
capable of adapting to an expanding range of complex
simulation modalities. Through systematic evaluations,
we demonstrate that Paimon automates expert-level simulations and that advanced agentic modules are essential
for reliability.

procedures summarized in natural language. The orchestrator interprets the user query and controls the overall
computational workflow based on this expert knowledge
by managing executors. The executors are agents that
handle individual scientific software packages, such as
LAMMPS [41], ASE [39], or PACKMOL [40]. Below, we
discuss each component in more detail.
First, we begin with the orchestrator. The orchestrator serves as the central controller of Paimon by combining user queries with expert knowledge. Specifically, the
orchestrator performs dynamic planning and task decomposition to manage complex simulation workflows. The
detailed role of the orchestrator in Paimon is illustrated
in Fig. 1b. Given the user query, the orchestrator first
retrieves relevant expert knowledge, a natural-language
procedure guide. Specifically, it searches the knowledge
database via vector retrieval [43] or extracts computational methodology if the user provides a reference
research article. Once the relevant knowledge is obtained,
it establishes a workflow outline and subsequently generates subtasks in an on-the-fly manner. The orchestrator
can revisit earlier stages or discard subtasks depending
on intermediate outcomes, allowing the system to manage complex, long-horizon research pipelines by adapting
the workflow based on the specific requirements of each
task.
Each subtask is assigned an executor that carries out
instructions specified by the orchestrator. Upon completion of the subtask, the orchestrator receives a summary
report detailing its outcome. If the orchestrator finds
that the report is missing necessary information, it can
consult with the executor agent for clarification. We note
that orchestrator-executor interactions rely on a shared
set of tools that are independent of executor type, allowing new executors to be added without modification to
the orchestrator.
Each subtask record consists of persistent files,
including the memory of the executor agent. Such records
of completed subtasks constitute an episodic memory [27, 44] of Paimon, comprising a summary of the
entire run and the key simulation scripts produced at
each stage (see Fig. 1c). This memory is automatically
supplied to the orchestrator alongside the expert knowledge, providing contextual awareness of prior execution
history. When generating a new subtask, if the orchestrator judges that it resembles a previously completed one,
it attaches the corresponding record to the executor. The
attached record serves as a concrete example guiding the
executor toward a previously successful history [45].
Second, the executors are agents that handle specialized software packages. Atomistic simulations require
highly sophisticated programming, resulting in a longstanding ecosystem of established packages specialized
in structure generation [39, 40], molecular dynamics
(MD) [41], data analysis [42, 46, 47], etc. A core design
philosophy of Paimon is to fully take advantage of these
established scientific packages, thereby avoiding unreliable re-implementation of functionality. Accordingly,

2 Results
2.1 Architecture of Paimon
Atomistic simulations span diverse application areas,
and these domains continue to expand. Consequently,
it is essential to design an automation system that can
scale easily across these domains. However, many existing agentic systems in atomistic simulations rely on
hard-coded agent hierarchies and tightly scoped domainspecific tools, making their architectures difficult to
extend [35]. Paimon achieves high scalability through
a centralized multi-agent architecture [22, 23, 26]. It
consists of three independent components: expert knowledge, an orchestrator, and executors (see Fig. 1a). Briefly,
the expert knowledge contains detailed computational

What is the Li-ion diffusivity in
EC/EMC (3:7) with LiPF6?

Architecture of Paimon
ASE agent

User

Performs structure relaxation
and auxiliary works

Diffusivity analysis
in liquid electrolyte
# 1. Multiple simulations
Run at least three
independent simulations
each simulation begins
with a freshly generated
structure. [...]
# 2. Structure generation
Adjust molecule counts so
the final system size lies
between 950 and 1150
atoms. [...]
# 3. Equilibration

The diffusivity is
0.425 × 10−6 cm2/s

Literature

Packmol agent
Generates initial molecular
configurations

LAMMPS agent
Writes LAMMPS input script
and runs simulations

Freud agent

Executor agents

Analyzes simulation
trajectories

External agent
Human expert

(e.g. LLaMP, ...)

Episodic memory

Orchestrator interactions
Subtask A
Subtask B
Subtask C
Discarded
Next subtask

Retrieves expert knowledge
Interacts with the user and agents
Plans dynamically

Previous subtasks

Subtask

Query

Summary & Simulation scripts

+ Subtask
User

Report

Answer

Executor

+ Knowledge

LAMMPS agent

Knowledge
d

Tool use

Critic committee

- Complete task
- Submit and wait

Pass

LLM 1
LLM 2

Verdict

Fail

Executor
LLM K

Revise

Feedback

Fig. 1 Architecture of Paimon. a Schematic overview of Paimon. The left panel illustrates the expert knowledge module. The right
panel shows the executor agents employed in this work, from top, ASE [39] agent, PACKMOL [40] agent, LAMMPS [41] agent, Freud [42]
agent, and LLaMP [38] agent. The center panel shows a chat between the user and the orchestrator. b Schematic of orchestrator interactions
with other modules. The orchestrator answers a user query and retrieves expert knowledge. It gives a subtask to the executor agent and
receives a report from it. c Schematic workflow of Paimon using the episodic memory. When the orchestrator retrieves knowledge from the
expert knowledge database, it is informed of a summary of a previous run and corresponding subtasks. The orchestrator then provides one
of the previous subtasks as a reference example to the LAMMPS agent. d Critic committee module. The critic committee is invoked when
the executor agent uses either the complete task or the submit and wait tool. K denotes the number of independent critic LLM calls made,
given the memory of the executor. The responses of the LLMs are aggregated into a verdict. The verdict is one of Pass, Fail, or Revise.
For the Revise verdict, the executor receives feedback.

each executor agent in Paimon specializes in a specific
package. For each subtask, the orchestrator issues an
instruction to an executor, scoped to the capability of its
package. For example, a query to the LAMMPS agent
might be: “Carry out an NVT simulation at 300 K for
1 ns and save the MD trajectory”, where NVT refers to
the isothermal–isochoric ensemble.
The executor agent then autonomously manages the
computational lifecycle. This includes generating input
scripts or program commands, running the software or
submitting jobs, validating result integrity, and postprocessing the outputs. We standardize the output format
to HDF5 [48]. When the agent needs to process data produced by other agents (e.g., the Freud agent analyzes MD
outputs of the LAMMPS agent), this HDF5 file serves as
a communication channel between the agents. We refer
to this mechanism as the file contract. The file contract
decouples individual executors, allowing a new agent
to interoperate with the existing Paimon framework by
conforming to the HDF5 schema.
To perform these functions, each executor is equipped
with dedicated tools for accessing software documentation and managing execution and I/O (see Supplementary Table 1 for tools). Among these, generating simulation scripts via retrieval-augmented generation [49,
50] from official software documentation is particularly
important. This is because the parametric knowledge of
LLMs is reliable primarily for common use cases (e.g.,
plain NVT simulations), whereas it often fails for less
common scenarios [19, 21, 29, 32] (e.g., deposition simulations). To further improve script quality, we use an
annotator LLM that marks the most relevant sections of
the retrieved document, given the subtask context.
Previous frameworks often embed simulation
logic into predefined tool functions, because earlier
LLMs could not reliably generate simulation scripts
autonomously [16, 20, 29]. The resulting systems can
only perform simulations for which a corresponding tool
has been implemented. The executor agents of Paimon
instead generate simulation scripts via retrieval over official documentation, shifting the extensibility bottleneck
from tool implementation to documentation coverage.
We demonstrate in Section 2.3 that this approach is
now feasible for a range of tasks.
Finally, expert knowledge (see Fig. 1a) is structured as a collection of specialized modules that provide
self-consistent, natural-language descriptions of computational procedures to guide the entire simulation
process, which follows the best practices established
among specialists. To respond to the user query even
when it provides minimal details, expert knowledge specifies technical parameters and simulation conditions.
The computational steps are organized into hierarchical sections to improve the comprehension of the overall
workflow structure by the orchestrator.
While the parametric knowledge of frontier LLMs is
often accurate on its own, this explicit expert knowledge
base is necessary for many reasons:

i) Reliable and reproducible trajectories: Native
LLM-based workflow generation is probabilistic, so the
same query can yield different LLM reasoning/planning
trajectories and, consequently, different computational
workflows. This inconsistency in the generated approach
can undermine the reliability of ensemble averages and
comparisons across runs. The expert knowledge improves
reproducibility by providing concrete procedures that
constrain the planning path of the LLM and steer it
toward consistent workflows.
ii) Enhanced accuracy: The expert knowledge modules provide precise technical parameters, such as system
sizes, time steps, and MD durations, that reflect the rigor
of scientific literature.
iii) Computational efficiency: There is know-how
established in each application domain that enhances the
computational efficiency. For instance, pre-equilibration
steps at high temperatures can reduce the equilibration
time. By explicitly applying these techniques, one can
obtain the results more quickly.
Each expert knowledge module focuses on a specific
domain but covers a broad class of materials, such as
Li-ion diffusivity in liquid electrolytes or thermal conductivity in bulk materials. While the knowledge module
can be authored directly by domain experts, it can also
be extracted from scientific literature using LLMs, which
we demonstrate in Section 2.5.
Additionally, Paimon introduces a critic committee
(critic hereafter) module that reviews the overall agent
process at each subtask (Fig. 1d). While prior works have
incorporated similar verification layers at the planning
stage [29] or for convergence checks [13], the critic of
Paimon operates at the subtask level across all executors. The critic aggregates responses from multiple LLMs
through a voting mechanism to obtain a reliable verdict
(see Methods for voting). For each executor, the critic
gates either job submission or task completion, reviewing
scripts before computational resources are consumed or
validating results before a subtask is finalized (Supplementary Fig. 1). The critic returns one of three verdicts:
Pass, Fail, or Revise. Upon the Revise verdict, the critic
provides actionable feedback for iterative refinement [28].

2.2 Failure analysis
When an automated simulation system such as Paimon
fails to deliver accurate results, the root cause typically
falls into one of three categories. First, “LLM Misalignment” occurs when the foundational language model
hallucinates, ignores instructions, or generates incorrect
code. Second, “System Misalignment” happens when the
overarching framework itself fails, such as by lacking
the proper information in the expert knowledge. Finally,
even if the AI components function perfectly, “Fundamental and External Limitations” can cause failures due
to inaccurate data in the original reference literature,
the inherent boundaries of the force fields being used,

2.3 LAMMPS agent evaluation

or natural numerical instabilities that crash the simulation. In practice, the first two categories constitute the
primary sources of errors. We note that the boundary
between LLM misalignment and system misalignment
is often blurred; for instance, inherent LLM hallucinations can frequently be mitigated by providing relevant
domain knowledge within its context.
The above misalignments introduce various errors,
which we categorize into “benign”, “loud”, and
“silent” errors depending on their ultimate impact and
detectability. A benign error represents a minor procedural deviation that does not significantly compromise the
physical validity of the results, such as an agent setting a
simulation time step to 1 fs instead of the requested 2 fs.
Conversely, remaining errors fundamentally disrupt the
simulation pipeline and manifest in two distinct forms.
A loud error is an explicit failure, such as configuring an extreme temperature like 3000 K (instead of the
requested 300 K) that yields obviously unphysical results
or specifying an invalid command option that causes the
MD simulation to crash. In contrast, a silent error is more
deceptive. In this case, the simulation completes without
runtime errors and produces seemingly plausible data,
but the underlying physical meaning is corrupted, such
as misusing an analysis option that silently invalidates
the outcomes.
We note that these severity boundaries form a continuous spectrum depending on the magnitude of deviation.
For example, setting a molecular dynamics time step to
1 fs instead of a requested 2 fs is a benign error, reducing efficiency but preserving validity. However, using
3 fs becomes a silent error, corrupting thermodynamics
without crashing. On the other hand, an extreme 10 fs
becomes a loud error, immediately crashing the simulation. Silent errors are the most concerning, as they leave
no signal in outputs and can only be caught by inspecting
the simulation script itself.
Finally, the stochastic nature of LLMs introduces
run-to-run variance [51]: identical prompts processed by
the Paimon can yield outcomes ranging from flawless
execution to silent failures. Consequently, validating the
reliability of LLM-driven scientific automation necessitates robust statistical analysis through repeated sampling, which in turn yields insights for enhancing system
reliability.
We analyze the reliability of the major executor
agent, the LAMMPS agent, and the whole system. We
apply both the error severity classification and repeated
sampling for their evaluation. Error classification is performed by human experts, who assign each error to one
of the three severity levels. Repeated sampling is carried
out by an automated pipeline in which an LLM checks
each simulation script against a predefined set of binary
pass or fail criteria (e.g., “Is the time step set to 1 fs?”),
which measures how often the intended simulation procedure is correctly executed across N independent trials
with the same prompt.

LAMMPS is a widely used molecular dynamics simulator, and many uMLIPs [4–7, 57] are implemented in
LAMMPS. We develop a LAMMPS agent and evaluate
its performance on three simulation tasks: (i) computing the mean-squared displacement (MSD) of Li-ions in
a liquid electrolyte, (ii) recording the heat flux autocorrelation for the Green–Kubo [52, 53] method, and (iii)
Cu deposition simulation on an a-Ta2 N slab [54]. For
each simulation task, we develop simulation instructions
of increasing complexity. Specifically, the Cu deposition task adapted from ref. [54] is the most complex,
as it requires the agent to spatially partition the slab
and assign different ensembles (see Fig. 2b). The task
instructions and answers are listed in Supplementary
Figs. 2–7.
We conduct ablation studies on the LAMMPS agent
configurations by cumulatively adding the annotator
and the critic to the baseline. The baseline agent uses
the retrieval [49] tool for the LAMMPS document. We
allocate a higher-capacity model (GPT-5 [58]) to the
annotator and critic than to the executor (GPT-5-mini),
because the executor cannot correct erroneous guidance
from these components. The Cu deposition task is evaluated with an extra strong LLMs configuration, which
uses GPT-5.4 [59] for all LLMs involved.
For repeated sampling, we assess LAMMPS scripts
generated by the agent using an LLM that checks
each script against predefined rubrics (Supplementary
Tables 2–4). Each rubric consists of multiple criteria
designed to detect silent and loud errors. A subset of
these scripts (50 in total) is evaluated for error severity
by human experts, who are blinded to the corresponding
rubric results. The human evaluation and the repeated
sampling results agreed on the pass/fail outcome in all
50 scripts.
Across all three tasks, the addition of the annotator
and critic consistently improves the pass rates (Fig. 2a)
while suppressing both loud and silent errors (Fig. 2c–
e). Pass rate breakdown and error severity assignments
are detailed in Supplementary Fig. 8 and Supplementary
Note 1.
For the Li-ion MSD task, the pass rate significantly
increases as we add the annotator, from 1% to 66%.
This gap is attributed to the MSD analysis command.
In the baseline configuration, the agent selects an incorrect option that results in a silent error. Specifically, all
failed scripts in the baseline misuse the com option for
the MSD analysis, which is incorrect because it subtracts the center of mass of the selected atoms, not the
entire system. This behavior likely stems from the task
instruction, which requires removing the center-of-mass
linear momentum from the system. The agent conflates
this condition with the com option. However, this failure
mode becomes rare as the annotator is added.
For the thermal conductivity task, the pass rate
increases from the baseline of 42% to 72% and 95% as

Pass rate (%)

Ta

Deposit

N

Cu
NVE

NVT
Fixed

Li-ion MSD

Thermal conductivity

+ Strong LLMs

d

Li-ion MSD

Cu deposition

Thermal conductivity

e

Cu deposition

Error severity

Benign

Loud

Silent

+ Strong LLMs

Fatal

Fig. 2 LAMMPS agent evaluation. a Pass rates of LAMMPS scripts generated by the LAMMPS agent for the Li-ion MSD in liquid
electrolytes task, the thermal conductivity via Green–Kubo [52, 53] task, and the Cu deposition on an a-Ta2 N slab [54] task. Blue, red, and
violet legends denote agent configurations, each added to the previous. The strong LLMs configuration samples 50 LAMMPS scripts, while
others sample 100 scripts. Error bars indicate 95% Wilson confidence intervals [55, 56]. b Schematic diagram of the simulation cell in the
Cu deposition task. NVT and NVE refer to the isothermal–isochoric and microcanonical ensembles. The fixed region contains immobilized
atoms. c–e Human-graded subset with error severity. Five randomly sampled runs are labeled by human experts, for c the Li-ion MSD, d
the thermal conductivity, and e Cu deposition tasks. Red, orange, and green boundaries indicate runs with silent errors, loud errors, and
no or only benign errors, respectively. The overlaid numbers mark cases with more than one distinct error source.

we add the annotator and then the critic, respectively
(Fig. 2a). The most frequent failure arises from heat flux
computation, where the agent omits a command option
(virial) required for the analysis. This case accounts for
all silent errors in Fig. 2d. The critic corrects this failure.
The critic identifies a mismatch between the submitted
LAMMPS script and the heat flux document, returning
a Revise verdict citing the missing virial option. The
agent incorporates this feedback and resubmits a revised
script, which then passes the critic and subsequently the
rubric.
For the Cu deposition task, the baseline does not
pass, but the pass rate increases to 19%, 34%, and 64%

as we add the annotator, critic, and strong LLMs, respectively. The primary failure arises from the deposit region
specification, where relevant guidance is split across two
documents. Specifically, there is a constraint on the
deposition region, which appears not in the “region” document but in the “deposit” document. Consequently, the
agent assigns an incorrect deposition region that yields
a loud error. This dispersal across documents limits the
annotator, as it processes only a single document for
each retrieval. Interestingly, the use of stronger LLMs
alleviates this limitation.
Figure 2c–e illustrates the error severity classified by
human experts. The asymmetry of the detected errors
suggests that the failures are qualitatively different. In

• Equilibration: The agent restores the hydrogen mass
to its physical value and resumes the NPT simulation.
• Production MD: To switch from NPT to NVT, the
agent analyzes the last 0.2 ns of the NPT trajectory. It uses the frame whose density is closest to the
time-averaged value as the starting point for the NVT
simulation.
• Diffusivity: The agent analyzes the NVT trajectory
to compute the Li-ion diffusivity.

the Li-ion MSD task with the baseline configuration,
all five runs contain silent errors (Fig. 2c). In contrast,
the Cu deposition runs with the strong LLMs have
no silent errors but two loud errors (Fig. 2e). If Paimon were deployed to these tasks, the Li-ion MSD runs
would return seemingly plausible but incorrect results.
On the other hand, the Cu deposition runs would crash
before producing complete data, while leaving the failure
observable to the agent and thus recoverable.
The above analysis shows that the stochasticity of
LLMs is not uniform, but it depends on the required
reasoning depth. While explicit, single-step instructions
yield low variance in their execution [60], tasks demanding complex inference or the interpretation of implicit
physical or technical contexts introduce significant runto-run variance. In these scenarios, the same prompt can
yield outcomes ranging from complete success to silent
failures, as characterized in Fig. 2c–e.
Furthermore, the necessity of the annotator highlights a mismatch between human-centric documentation
and LLM processing. Because human reading speed is
limited, these documents are condensed and rely on
implicit domain knowledge of the reader. While LLMs
can process text at far greater speeds, they often struggle to infer these implicit, cross-referenced nuances. The
annotator effectively addresses this mismatch by acting as an interpretative bridge. It translates the implicit
logic of human-centric manuals into the explicit directives required by the agent, thereby significantly reducing
execution errors.

This simulation takes on the order of days, making
repeated sampling impractical. In this regard, we introduce gated evaluation. Each stage has a corresponding
validation gate that Paimon must satisfy to advance.
Once Paimon passes a gate, it receives the precomputed
output, bypassing the expensive MD simulation. Fig. 3b
summarizes the validation gates for each stage, involving script and numerical validation. The script validation
agrees with human grading in 83 of 84 scripts (Supplementary Fig. 9). The rubric for script validation is listed
in Supplementary Tables 5–7, with examples provided in
Supplementary Figs. 10–12. The full simulation result is
discussed later in this section.
Starting from the baseline, we evaluate four agentic
configurations by successively adding file contract, critic,
and episodic memory. For each configuration, we also test
“low” and “medium” reasoning effort, which controls the
extent of internal reasoning in the underlying LLMs [62].
Figure 3a shows the gated evaluation results. At low
effort, the success rate increases from 29.7% in the baseline to 74.7% with episodic memory, and medium effort
further raises this to 90.0%. No notable difference across
solvents is observed (Supplementary Fig. 13). The progressive improvement for each addition of an agentic
component suggests that they are complementary and
address distinct failure modes. In the following, we examine each configuration. To isolate the contribution of
each configuration to each stage, we report conditional
pass rates, defined as the fraction of runs that pass a
given stage among those that reached it (npass /nreach ).
Full results are provided in Supplementary Fig. 14 and
Supplementary Tables 8–12.
The effect of the file contract is concentrated in
the production MD stage, where the conditional pass
rate increases by 30.0% with low effort (Supplementary
Fig. 14a). The most frequently failed criterion is selecting an equilibrium frame for production MD. We find
that the Freud agent, which performs such analysis, commits silent errors that arise from speculative parsing of
simulation data. For example, the Freud agent parses
the upstream LAMMPS log file under a wrong assumption, unknowingly selecting the wrong equilibrium frame
(detailed in Supplementary Note 2). This failure mode is
largely absent under the file contract, where inspecting
the standardized HDF5 file reveals all available data.
In the diffusivity stage, the critic operates with the
Freud agent rather than the previously tested LAMMPS
agent. Notably, the critic increases the conditional pass

2.4 End-to-end evaluation: Li-ion
diffusivity in liquid electrolytes
Having established performance at the executor level, we
next evaluate Paimon at the system level, which involves
the orchestrator, inter-agent cooperation (file contract),
and expert knowledge. The target task is simulating a
liquid electrolyte to compute Li-ion diffusivity, strictly
following the knowledge module.
We construct the knowledge module of Li-ion diffusivity using ref. [61] as a primary source. The user query
to Paimon asks for Li-ion diffusivity with SevenNet0 [7] alongside a solvent molecule structure. The solvent
is one of diethyl carbonate (DEC), dimethyl carbonate
(DMC), or propylene carbonate (PC), which are chosen
for comparison with the reference.
As illustrated in Fig. 3b, we decompose the simulation workflow described in the knowledge module into
five stages (see Methods for computational details).

• Preparation: The agent reconciles the molality (user
query) with the atom count range (expert knowledge)
to determine the molecular composition.
• Pre-equilibration: The agent substitutes the hydrogen mass with that of tritium to accelerate equilibration and performs an isothermal–isobaric (NPT)
simulation.

Fig. 3 Gated evaluation of the Li-ion diffusivity in liquid electrolytes task. a Pass rates at each stage under four cumulative
configurations: baseline, file contract, critic, and episodic memory. Reasoning effort is set to “low” for all LLMs except the orchestrator.
Each configuration is evaluated on 300 runs. Markers show pass rates of “medium” reasoning effort on 100 runs, with counts scaled to 300.
Error bars indicate 95% Wilson confidence intervals [55, 56]. b Schematic of Li-ion diffusivity workflow and validation gates. Each stage
includes a gate with specific criteria. Blue rectangles indicate validation of the LAMMPS script by an LLM against rubrics, whereas orange
rectangles indicate numerical validation of intermediate results.

rate of the diffusivity stage by 15.6% at low effort (Supplementary Fig. 14a). This gain accompanies a reduction
in silent errors, in which the computed diffusivity is
wrong but numerically close to the reference. Specifically,
among runs reaching the diffusivity gate, the fraction
that fail while reporting a diffusivity within a factor
of two of the reference decreases from 18.8% to 7.6%.
The result demonstrates that the critic suppresses silent
errors regardless of the executor.
The episodic memory utilizes previously successful
runs (see Fig. 1c), which we draw from different solvents
than the one under evaluation. The addition of the memory raises the success rates by 9.0% at low effort (Fig. 3a).
Unlike the file contract and the critic, whose gains concentrate at one or two stages, episodic memory yields
modest increases at every stage. This observation aligns
with its role of providing a complete prior trace as an
in-context demonstration.
The success rates at medium effort all surpass their
low-effort counterparts (see diffusivity of Fig. 3a). Both
architectural components and reasoning effort improve
success rates, raising the question of whether a stronger
LLM would make architectural components redundant.
The monotonic decrease of the pass rate along workflow stages suggests otherwise. This decay reflects error

compounding, where the success rate scales as the product of conditional pass rates. Consequently, reliability
at a given workflow length does not transfer to longer
ones. We therefore expect both architectural design and
LLM improvements to remain essential, each extending
the task length over which an agentic system operates
reliably.
We now deploy Paimon on the same workflow without
gates, executing the actual MD simulation. We run Paimon 30 times with the file contract and critic, at medium
effort. We assign a single error severity to each run based
on the result delivered to the user.
As shown in Fig. 4a, 22 runs complete without errors,
4 produce benign errors, and 4 produce silent errors, with
no loud errors (e.g., unphysical diffusivity). The success
rate is 87%, roughly consistent with the gated evaluation
(85%). The reported diffusivity values fall in the same
range as the source of the expert knowledge (Fig. 4b).
Four out of the eight erroneous runs fall within
the criteria of the gated evaluation (detailed in Supplementary Note 3). The remaining errors arise from a
borderline condition where the response of the orchestrator varies. According to the knowledge module, the
production MD should be extended for another 1 ns if
the R2 of the MSD fit, which is required for diffusivity

researchers, is internal to the agent and can be narrowed
by refining the specification. A complementary approach
is allowing user intervention, which we demonstrate in
the following section.

Solvent

DEC
DMC
PC

Runs

No error

Benign

2.5 Extensibility
Paimon achieves extensibility through two properties.
First, all agents, including the orchestrator, communicate through a shared interface, so introducing a new
executor requires no modification to the rest of the
system. Second, the simulation procedure is consolidated into a knowledge module rather than embedded
in the agents. Therefore, teaching Paimon a new simulation workflow amounts to obtaining its natural-language
description.
As demonstrated in Sections 2.3 and 2.4, run-to-run
variance inherent in an agentic system makes reliable
simulation execution challenging. However, this can be
mitigated through multi-turn refinement, where a user
provides corrective feedback to an agent [66].
We demonstrate the extensibility and multi-turn
refinement by applying Paimon to compute the Li-ion
diffusivity of Li6PS5Cl argyrodite, aiming to reproduce
the results of ref. [65]. Without modifying existing
agents, we integrate an externally developed LLaMP [38]
agent for crystalline structure retrieval (Fig. 5a). The
knowledge module of the argyrodite simulation is distilled from the reference by the extraction tool, which
uses an LLM (GPT-5).
Figure 5b summarizes the result. Given the reference article, the orchestrator autonomously extracts the
simulation method and follows it (see yellow box). The
user points out the absence of anion disorder in the
argyrodite structure, and the orchestrator incorporates
this feedback. Finally, it reports the diffusivities with
analysis figures (Fig. 5c), consistent with the reference
(Supplementary Fig. 15).
The extensibility of Paimon is qualitatively different
from that of rule-based automation. While rule-based
systems also support modular composition, integration
typically requires reconciling input and output schemas.
In contrast, integrating two agentic systems, in principle,
reduces to establishing a conversation channel between
them. For example, as demonstrated with LLaMP [38],
Paimon can serve as a computational scientist within a
general-purpose co-scientist [67]. Another natural extension is to delegate knowledge extraction to an agent
specialized in scientific literature. We expect such compositions to become common as the community converges
on standardized interfaces such as the Model Context
Protocol [68].

Silent

Success

Li-ion diffusivity (cm2/s)

Reference
Paimon

DEC

DMC
Solvent

PC

Fig. 4 Li-ion diffusivities reported by Paimon. a Error
severity across 30 independent runs (10 per solvent). Error severity
is assigned per run based on the potential effect of the delivered
result on the user. No loud errors are observed. b Li-ion diffusivities of DEC, DMC, and PC as reported by Paimon. Paimon results
aggregate runs without errors, comprising 7, 8, and 7 runs for DEC,
DMC, and PC, respectively. The reference values are taken from
ref. [61]. Error bars indicate standard deviations (the reference uses
five samples).

estimation, is below 0.97. In these runs, the initial MD
yields an R2 slightly below this criterion.
In three runs, the orchestrator reports the unconverged diffusivity but explicitly notes that the MSD fit
is inadequate and recommends extending the simulation.
We classify these as benign errors. In the remaining run,
the orchestrator omits such a note. We classify it as a
silent error because the user has no indication that the
diffusivity is unconverged. These behaviors may be influenced by the user query, as the orchestrator cited the
user request for a “quick” simulation.
In three error-free runs, the orchestrator
autonomously extends the simulation and reports a converged diffusivity. This shows that the agent can act on
a conditional branch described only in natural language.
The varying behavior of the orchestrator invites a
methodological observation. The round-robin study of
MD simulation [63] reports that researchers solving
the same task can produce results deviating beyond
statistical uncertainty, with the systematic component
attributed to procedural choices. The variance we
observe follows a similar pattern at the agent level.
The knowledge module specifies the criterion and the
corrective action, whereas the system prompt of the
orchestrator leaves the reporting behavior underspecified. Consequently, the orchestrator resolves this gap
differently across runs. This variance, unlike that among

3 Methods
3.1 Orchestrator
The orchestrator operates in two phases: planning and
execution (Supplementary Fig. 1a). Both phases use a

Paimon

Literature
New executor
+ Solid electrolyte simulation
+ Crystal structure retrieval

LLaMP agent

Calculate the Li+ diffusion coefficient in Li6PS5Cl argyrodite at 800, 1000, and 1200 K.
Obtain activation energy of Li+ diffusion. [...] Follow the protocol from the given paper.
supporting_information.pdf

paper.pdf

Tool call: extract paper methodology
- paper: paper.pdf
- supporting info: supporting_information.pdf

- task: [....]

# Protocol: Li+ Diffusion in Li6PS5Cl (Argyrodite) via Atomistic MD
MD: NVT (Nose-Hoover), 2 fs, 100 ps at 800/1000/1200 K, 5 replicas
MSD: time-averaged; discard MSD < 4.5 Å2 and last 30% of trajectory [...]

Plan to proceed, following the paper's protocol with your constraints: [...]
- MD: NVT (Nose-Hoover), timestep 2 fs, 100 ps per run at 800, 1000, 1200 K; 5 independent [...]
- Analysis: Time-averaged MSD; discard MSD < 4.5 Å2 and last 30% of each trajectory [...]
Please confirm: [...] If no changes, I will proceed with the defaults above.
All in default options.

Milestone: Geometry optimization complete. Final cubic lattice parameter a = 10.2795 Å. Ready to
start NVT production MD. [...] Proceed?
I'm looking at the structure, but no anion disorder has been applied.
Apply the anion disorder and re-run the relaxation.

Update; Applied explicit anion disorder [...] and re-relaxed with SevenNet-0.
Final lattice parameter a = 10.1071 Å. Ready to start NVT MD [...] proceed?
Proceed.

Results - Li+ diffusion coefficients (mean across 5 replicas):
- 800 K: 3.98 × 10−5 cm²/s
- 1000 K: 7.35 × 10−5 cm²/s
- Activation energy (Arrhenius, 800–1200 K): Ea = 0.204 eV [...]
Deliverables: msd_1200K.png, arrhenius_plot.png, [...]

- 1200 K: 1.06 × 10−4 cm²/s

Fig. 5 Extensibility demonstrated by the Li-ion diffusivity in solid electrolyte. a Schematic extension procedure. LLaMP [38]
is integrated as the executor. This agent retrieves a crystalline structure from Materials Project [64]. The expert knowledge module of solid
electrolyte simulation is extracted from ref. [65]. b Multi-turn interaction. Dotted boxes indicate the internal process of Paimon. Texts are
lightly edited for clarity. c Figures generated by Paimon during the workflow. The left and right panels show the MSD plot from the MD
simulation at 1200 K and the Arrhenius plot, respectively.

set of tools to manage the simulation workflow (see
Supplementary Table 1 for tools). In the planning
phase, the orchestrator gathers necessary knowledge and
requests clarification of the user query when needed.
The knowledge includes an expert knowledge module
and uMLIP knowledge, the latter covering available
pretrained models within a specific family (e.g., SevenNet [7, 8]) and their usage details, such as the DFT
functional of the training set and computational cost.
Once enough information is gathered, the orchestrator calls the outline plan tool, which forwards the
workflow to the execution phase.
In the execution phase, the orchestrator gains access
to the subtask management tools. When creating a
subtask, the orchestrator specifies the instruction, dependent subtasks, an executor, and required outputs. Once
a subtask is created, these inputs are consolidated into
a single prompt and dispatched to the corresponding
executor.
Upon completion of a subtask, the orchestrator
receives a report. For a successful subtask, the report
includes a message from the executor, the requested output values, and a summary of output structural files.
This summary enumerates the composition, cell volume, and the presence of unphysically close atomic pairs
(below 0.55 Å). These quantities are computed deterministically by the framework rather than by an agent, and
serve as a lightweight check on the output structure.
Unless stated otherwise, the subtask retry budget
is set to one. If a subtask fails but the retry budget
remains, the framework automatically retries the same
subtask after resetting the executor memory. Otherwise,
the orchestrator receives a failure report whose content
depends on the failure mode. If the executor aborts the
task on its own, the report contains the rationale of the
executor; if the critic rejects the subtask, a summary of
the last critic feedback is delivered. As a safeguard, the
executor also terminates if it reaches a fixed iteration
limit.
Paimon is built on LlamaIndex [69]. Although we use
only GPT models in this work, other language models
are interchangeable through LlamaIndex.

the first paragraph of its Description section. A selector LLM (GPT-5-mini) chooses the final document from
the top four candidates, and an annotator LLM (GPT-5)
then appends guidance to the selected document, conditioned on the subtask instruction. When the agent uses
the write lammps script tool, the tool automatically
performs a dry run to validate the syntax.
The ASE (Atomic Simulation Environment) [39]
agent handles structure manipulation and relaxation
tasks. It retrieves relevant source code via vector
retrieval [43] using the code search tools adopted from
CASCADE [31]. The PACKMOL [40] agent generates
an atomistic structure, with the full PACKMOL documentation provided in its context. The Freud [42] agent
analyzes simulation outputs, with MDAnalysis [46, 47]
handling trajectory I/O. For documentation access, an
LLM (GPT-5-mini) reads the query together with the
Freud documentation and returns guidance.
The LLaMP agent [38] is integrated for access to
the Materials Project [64] database. An adapter agent is
implemented that uses LLaMP as one of its tools. We
use the original LLaMP source code with only a minor
bug fix.
The file contract is implemented through common
system prompts shared across executors. Executors organize their results into extxyz, dcd, and HDF5 [48]
formats for atomic structures, MD trajectories, and tabular data, respectively. Each HDF5 file includes links to
associated output files and a description written by the
executor. Downstream agents consume these files via the
inspect h5 tool.

3.3 Critic committee
The critic committee serves as a verification layer for
each subtask. It operates in two modes depending on the
executor: a pre-submission gate, invoked when the executor attempts to submit a job, and a completion review,
invoked when the executor attempts to finish a subtask
(see Supplementary Fig. 1b,c for workflow diagram). We
assign the pre-submission gate to the LAMMPS agent
and the completion review to the other executors.
The critic committee consists of multiple LLMs. Each
LLM receives an executor agent memory, which contains
the full history: the subtask instruction, tool invocations,
and their outputs. The LLM is prompted to cast a vote
among four labels: Pass, Concern, Reject, or Malicious.
Pass indicates that the subtask instruction has been
correctly followed, and no errors have been detected.
Concern flags a potential issue that may compromise correctness but is not a definitive error, such as the executor
failing to inspect output files before reporting. Reject
identifies a definitive error that must be corrected before
proceeding. Malicious indicates that the executor recognizes its task has not succeeded, yet attempts to bypass
deterministic checks by fabricating results.
The critic committee aggregates the votes into a verdict. The committee returns a Fail verdict if any vote

3.2 Executors
Each executor is assigned a working directory in a Linux
environment with scientific packages pre-installed. Given
a subtask prompt, the executor iteratively uses its tools
to accomplish the task (see Supplementary Table 1
for tools). It terminates iteration by calling either the
complete task or the abort task tool. Each executor
maintains a short-term memory scoped to its subtask.
The LAMMPS agent generates and executes simulation scripts for LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulation) [41]. The agent
retrieves a document using a hybrid retrieval scheme
that combines BM25 [70] and vector retrieval [43] with
reciprocal-rank fusion [71]. Each document is indexed by

The system is equilibrated for 1 ns in the NPT ensemble at 298 K and 1 atm using a 2 fs time step with
tritium mass assigned to hydrogen atoms. The hydrogen mass is then restored, and the system is further
equilibrated with a 0.4 ns NPT simulation at a 1 fs
time step. The NPT trajectory is saved every 10 steps.
The equilibrium density is determined by averaging the
instantaneous densities over the last 0.2 ns of the NPT
trajectory, and an NVT simulation is initiated from the
frame whose density is closest to this value. The NVT
trajectory is saved every 100 steps. During the NVT simulation, the linear momentum is zeroed every step. The
Nosé–Hoover thermostat [74] and barostat [75, 76] are
applied as implemented in LAMMPS.
The Li-ion diffusivities are computed from the MSD
using the Einstein relation [77], with the MSD averaged
over multiple time origins [78]. The MSD fitting window
is set to 10–67% of the total simulation time, and a fit is
retained if R2 ≥ 0.97. The production trajectory length
is set to 1.1 ns.

is Malicious, a Revise verdict if any vote is Reject or
if the fraction of Concern votes exceeds a threshold.
Otherwise, a Pass verdict is returned, and the job is submitted, or the subtask is completed and reported to the
orchestrator. On a Revise verdict, an LLM summarizes
the feedback from all critic LLMs that issued Reject or
Concern votes. This summary is returned to the executor, which then attempts to address the identified issues
within the same subtask. If a Revise verdict persists after
the retry budget of the critic is exhausted, the subtask
is marked as a failure.
In this work, the critic committee comprises two
GPT-5 critic LLMs, and the summarizer LLM is GPT5-mini. The critic turn budget is set to two, and the
threshold for the ratio of Concern votes is set to 0.5.

3.4 LAMMPS agent evaluation
Each combination of task and configuration samples 100
LAMMPS scripts, except the strong LLMs configuration, which samples 50 scripts. Five scripts are randomly
drawn from each combination, yielding 50 scripts for
the error severity classification. After the classification,
scripts with either a loud or a silent error are mapped
to “fail” and matched against the repeated sampling
results.
The LAMMPS scripts are collected at the point of job
submission. In configurations where the critic is enabled,
scripts are collected after passing the critic. The subtask
retry budget is set to 10. GPT-5 with low reasoning effort
is used to assess scripts against the rubric.
For the thermal conductivity task, the example script
in the official LAMMPS documentation is removed
before building the vector database to avoid trivial
retrieval. The input structure and simulation parameters for the thermal conductivity task are adapted from
ref. [72].
For the Cu deposition task, some scripts use the
jump command. Because the control flow introduced by
this command is not covered in our rubric, we manually
evaluate these scripts. They account for 1, 0, 6, and 2
cases in the baseline, annotator, critic, and strong LLMs
configurations, respectively.

3.6 Gated evaluation
The orchestrator receives the following user query:
“Hi, could you run a quick MD simulation at room
temperature (298 K) and 1 atm for m (±0.1%) molal
LiPF6 in solvent ? A single full trajectory is fine, no
need for replicates. I’m interested in the Li+ diffusion
coefficient. Use SevenNet-0 potential.”
Here, m is the target molality and solvent is one of
DEC, DMC, or PC, followed by its full name in parentheses. The molality and its tolerance (±0.1%) are chosen
such that, given the range of system sizes (950–1150
atoms) specified in the expert knowledge module, the
composition is uniquely determined.
In the low reasoning effort setting, we conduct 100
runs for each of the three solvents, giving 300 runs in
total. Episodic memory records are selected from three
DEC runs of the critic configuration that passed gated
evaluation. For each run with the episodic memory, one
of the three records is randomly selected and supplied to
the orchestrator. With these records, 150 runs are performed for DMC and PC. The medium reasoning effort
setting uses 100 runs on DMC only. Its episodic memory
configuration reuses the same three records sampled at
low reasoning effort.
Each stage in the workflow (Fig. 3) has a corresponding gate. The diffusivity gate is evaluated once
the workflow completes. For the preparation gate, GPT5-mini identifies the subtask that performs structural
relaxation and locates the output structure file. GPT5-mini performs script validation for pre-equilibration,
equilibration, and production MD gates.
The pre-equilibration, equilibration, and production
gates are determined by the job submission count: the
first submission triggers the pre-equilibration gate, the
second the equilibration gate, and the third the production MD gate. Out-of-order cases are handled as follows:

3.5 Li-ion diffusivity in liquid electrolyte
The precomputed outputs and target values for the gated
evaluation are prepared following the liquid electrolyte
knowledge module (Supplementary Note 4 for the full
module). The composition of solvents (DEC, DMC, and
PC) and salts (LiPF6 ) is determined from ref. [61]. The
simulation cells are prepared using PACKMOL [40], with
a tolerance of 3 Å for Li–Li pairs and 2 Å for all other
pairs. The initial cubic box length is determined from the
summed van der Waals volumes [73] of all atoms, V0 , as
1/3
1.1 × V0 . The structure is relaxed until the maximum
atomic force falls below 2.0 eV/Å.

a job submission before the preparation gate has been
exercised counts as a preparation failure, and a fourth
job submission counts as a diffusivity failure.
The preparation gate checks the relaxed structure
against five criteria: (i) periodic boundary conditions
enabled along all three axes, (ii) molecular composition matching the reference, (iii) maximum atomic force
below 2.0 eV/Å, (iv) minimum Li–Li distance above
2.7 Å, (v) cubic box length within 10% of the reference.
Both the production MD and diffusivity gates perform an
exact match within a numerical margin. The production
MD gate passes if the input structure volume matches
the reference within 0.001%. The diffusivity gate requires
the reported diffusivity to match the reference within
0.001 × 10−6 cm2 /s.
When the orchestrator aborts the task, the run is
counted as a failure at the stage of the abort. Technical
failures unrelated to task correctness, such as API errors,
are discarded and rerun.

out at the Center for Advanced Computations (CAC)
at Korea Institute for Advanced Study (KIAS) and
Korea Institute of Science and Technology Information
(KISTI) National Supercomputing Center (KSC-2025CRE-0284).

7 Author contributions
Y.P., Y.C., and S.H. devised and formalized the idea.
Y.P., Y.C., and J.Y. developed the code base. S.J.
authored the expert knowledge module. Y.P., Y.C., J.Y.,
and J.K. contributed to the agent evaluations. Y.P.,
Y.C., and S.H. prepared the manuscript. All authors
contributed to discussions and approved the paper.

8 Competing interests
The authors declare no competing interests.

9 Additional information

3.7 Universal machine learning
interatomic potential

Supplementary information. The online version
contains supplementary material available at doi.org.

The selection of uMLIPs is modular, and an agent
retrieves potentials as needed. The choice can be specified by an expert knowledge module or by the user. If
it is not specified elsewhere, the orchestrator defaults
to the SevenNet [7] family and autonomously selects a
potential. Once the orchestrator informs the executors,
they access the designated potential, such as SevenNetOmni [8] or MACE-MP-0 [6], using the switch venv
tool. For SevenNet potentials, executors can enable the
FlashTP [79] kernel to accelerate simulations.
The uMLIP is specified in the user query to match
the reference protocol. The liquid electrolyte task uses
SevenNet-0 [7] with Grimme’s D3 dispersion correction
with Becke–Johnson damping applied [80, 81], following ref. [61]. The solid electrolyte task uses SevenNet-0
without the D3 dispersion correction, following ref. [65].

Agent transcript. The full transcript of the agent in
Section 2.5 is available at transcript.

References
[1] Cohen, A.J., Mori-Sánchez, P., Yang, W.: Challenges for density functional theory. Chem. Rev.
112(1), 289–320 (2012)
[2] Frenkel, D., Smit, B.: Understanding Molecular
Simulation: From Algorithms to Applications, 3rd
edn. Academic Press, Amsterdam (2023)
[3] Zhang, Y.-W., Sorkin, V., Aitken, Z.H., Politano,
A., Behler, J., Thompson, A.P., Ko, T.W., Ong,
S.P., Chalykh, O., Korogod, D., Podryabinkin, E.,
Shapeev, A., Li, J., Mishin, Y., Pei, Z., Liu, X.,
Kim, J., Park, Y., Hwang, S., Han, S., Sheriff, K.,
Cao, Y., Freitas, R.: Roadmap for the development of machine learning-based interatomic potentials. Model. Simul. Mater. Sci. Eng. 33(2), 023301
(2025)

4 Data availability
The full agent trajectories, rubric prompts, and precomputed data for gated evaluation are available at https:
//doi.org/10.5281/zenodo.20626167.

5 Code availability

[4] Chen, C., Ong, S.P.: A universal graph deep learning interatomic potential for the periodic table. Nat.
Comput. Sci. 2(11), 718–728 (2022)

The Paimon source code is available at https://github.
com/MDIL-SNU/Paimon.

[5] Deng, B., Zhong, P., Jun, K., Riebesell, J., Han, K.,
Bartel, C.J., Ceder, G.: CHGNet as a pretrained
universal neural network potential for chargeinformed atomistic modelling. Nat. Mach. Intell.
5(9), 1031–1041 (2023)

6 Acknowledgements
This work was supported by Samsung Electronics Co.,
Ltd. (IO250418-12669-01) and the National Research
Foundation of Korea (NRF) grant funded by the
Korea government (MSIT) (No. RS-2023-00247245 and
No. RS-2026-25542918). The computations were carried

[6] Batatia, I., Benner, P., Chiang, Y., Elena, A.M.,
Kovács, D.P., Riebesell, J., Advincula, X.R., Asta,

M., Avaylon, M., Baldwin, W.J., Berger, F., Bernstein, N., Bhowmik, A., Bigi, F., Blau, S.M., Cărare,
V., Ceriotti, M., Chong, S., Darby, J.P., De, S., Pia,
F.D., Deringer, V.L., Elijošius, R., El-Machachi,
Z., Falcioni, F., Fako, E., Ferrari, A.C., Gardner,
J.L.A., Gawkowski, M.J., Genreith-Schriever, A.,
George, J., Goodall, R.E.A., Grandel, J., Grey, C.P.,
Grigorev, P., Han, S., Handley, W., Heenen, H.H.,
Hermansson, K., Holm, C., Ho, C.H., Hofmann, S.,
Jaafar, J., Jakob, K.S., Jung, H., Kapil, V., Kaplan,
A.D., Karimitari, N., Kermode, J.R., Kourtis, P.,
Kroupa, N., Kullgren, J., Kuner, M.C., Kuryla, D.,
Liepuoniute, G., Lin, C., Margraf, J.T., Magdău,
I.-B., Michaelides, A., Moore, J.H., Naik, A.A.,
Niblett, S.P., Norwood, S.W., O’Neill, N., Ortner,
C., Persson, K.A., Reuter, K., Rosen, A.S., Rosset, L.A.M., Schaaf, L.L., Schran, C., Shi, B.X.,
Sivonxay, E., Stenczel, T.K., Svahn, V., Sutton, C.,
Swinburne, T.D., Tilly, J., van der Oord, C., Vargas, S., Varga-Umbrich, E., Vegge, T., Vondrák, M.,
Wang, Y., Witt, W.C., Wolf, T., Zills, F., Csányi,
G.: A foundation model for atomistic materials
chemistry. J. Chem. Phys. 163(18), 184110 (2025)

(2020)
[12] Mathew, K., Montoya, J.H., Faghaninia, A.,
Dwarakanath, S., Aykol, M., Tang, H., Chu, I.-H.,
Smidt, T., Bocklund, B., Horton, M., Dagdelen, J.,
Wood, B., Liu, Z.-K., Neaton, J., Ong, S.P., Persson, K., Jain, A.: Atomate: a high-level interface to
generate, execute, and analyze computational materials science workflows. Comput. Mater. Sci. 139,
140–152 (2017)
[13] Wang, Z., Huang, H., Zhao, H., Xu, C., Zhu,
S., Janssen, J., Viswanathan, V.: DREAMS:
density functional theory based research engine
for agentic materials simulation. Preprint at
https://arxiv.org/abs/2507.14267 (2025)
[14] Chen, M., Tworek, J., Jun, H., Yuan, Q.,
Oliveira Pinto, H.P., Kaplan, J., Edwards, H.,
Burda, Y., Joseph, N., Brockman, G., Ray, A., Puri,
R., Krueger, G., Petrov, M., Khlaaf, H., Sastry,
G., Mishkin, P., Chan, B., Gray, S., Ryder, N.,
Pavlov, M., Power, A., Kaiser, L., Bavarian, M.,
Winter, C., Tillet, P., Such, F.P., Cummings, D.,
Plappert, M., Chantzis, F., Barnes, E., HerbertVoss, A., Guss, W.H., Nichol, A., Paino, A., Tezak,
N., Tang, J., Babuschkin, I., Balaji, S., Jain, S.,
Saunders, W., Hesse, C., Carr, A.N., Leike, J.,
Achiam, J., Misra, V., Morikawa, E., Radford, A.,
Knight, M., Brundage, M., Murati, M., Mayer, K.,
Welinder, P., McGrew, B., Amodei, D., McCandlish, S., Sutskever, I., Zaremba, W.: Evaluating
large language models trained on code. Preprint at
https://arxiv.org/abs/2107.03374 (2021)

[7] Park, Y., Kim, J., Hwang, S., Han, S.: Scalable parallel algorithm for graph neural network interatomic
potentials in molecular dynamics simulations. J.
Chem. Theory Comput. 20(11), 4857–4868 (2024)
[8] Kim, J., You, J., Park, Y., Lim, Y., Kang, Y.,
Kim, J., Jeon, H., Ju, S., Hong, D., Lee, S.Y.,
Choi, S., Kim, Y., Lee, J.W., Han, S.: Optimizing
cross-domain transfer for universal machine learning interatomic potentials. Nat. Commun. 17, 3432
(2026)

[15] Jimenez, C.E., Yang, J., Wettig, A., Yao, S.,
Pei, K., Press, O., Narasimhan, K.R.: SWEbench: can language models resolve real-world
GitHub issues? The 12th International Conference on Learning Representations (2024).
https://openreview.net/forum?id=VTF8yNQM66

[9] Curtarolo, S., Setyawan, W., Hart, G.L.W.,
Jahnátek, M., Chepulskii, R.V., Taylor, R.H.,
Wang, S., Xue, J., Yang, K., Levy, O., Mehl,
M.J., Stokes, H.T., Demchenko, D.O., Morgan,
D.: AFLOW: an automatic framework for highthroughput materials discovery. Comput. Mater.
Sci. 58, 218–226 (2012)

[16] Campbell, Q., Cox, S., Medina, J., Watterson,
B., White, A.D.: MDCrow: automating molecular
dynamics workflows with large language models.
Mach. Learn.: Sci. Technol. 7(2), 025037 (2026)

[10] Huber, S.P., Zoupanos, S., Uhrin, M., Talirz, L.,
Kahle, L., Häuselmann, R., Gresch, D., Müller, T.,
Yakutovich, A.V., Andersen, C.W., Ramirez, F.F.,
Adorf, C.S., Gargiulo, F., Kumbhar, S., Passaro, E.,
Johnston, C., Merkys, A., Cepellotti, A., Mounet,
N., Marzari, N., Kozinsky, B., Pizzi, G.: AiiDA 1.0, a
scalable computational infrastructure for automated
reproducible workflows and data provenance. Sci.
Data 7, 300 (2020)

[17] Wang, Y., Wang, M., Manzoor, M.A., Liu, F.,
Georgiev, G.N., Das, R.J., Nakov, P.: Factuality of
large language models: a survey. Proceedings of the
2024 Conference on Empirical Methods in Natural
Language Processing, pp. 19519–19529 (2024)
[18] Buehler, M.J.: MechGPT, a language-based strategy for mechanics and materials modeling that
connects knowledge across scales, disciplines, and
modalities. Appl. Mech. Rev. 76(2), 021001 (2024)

[11] Youn, Y., Lee, M., Hong, C., Kim, D., Kim, S.,
Jung, J., Yim, K., Han, S.: AMP2 : a fully automated
program for ab initio calculations of crystalline
materials. Comput. Phys. Commun. 256, 107450

[19] Jacobs, P.F., Pollice, R.: Developing large language

Advances in Neural Information Processing Systems, vol. 36, pp. 8634–8652 (2023).
https://openreview.net/forum?id=vAElhFcKW6

models for quantum chemistry simulation input
generation. Digit. Discov. 4(3), 762–775 (2025)
[20] Shi, Z., Xin, C., Huo, T., Jiang, Y., Wu, B., Chen,
X., Qin, W., Ma, X., Huang, G., Wang, Z., et al.:
A fine-tuned large language model based molecular
dynamics agent for code generation to obtain material thermodynamic parameters. Sci. Rep. 15(1),
10295 (2025)

[28] Madaan, A., Tandon, N., Gupta, P., Hallinan,
S., Gao, L., Wiegreffe, S., Alon, U., Dziri, N.,
Prabhumoye, S., Yang, Y., Gupta, S., Majumder,
B.P., Hermann, K., Welleck, S., Yazdanbakhsh,
A., Clark, P.: Self-Refine: iterative refinement with
self-feedback. Advances in Neural Information Processing Systems, vol. 36, pp. 46534–46594 (2023).
https://openreview.net/forum?id=S37hOerQLB

[21] Soleymanibrojeni, M., Aydin, R., Guedes-Sobrinho,
D., Dias, A.C., Piotrowski, M.J., Wenzel, W., Rêgo,
C.R.C.: GENIUS: an agentic AI framework for
autonomous design and execution of simulation
protocols. Commun. Mater. 7(1), 115 (2026)

[29] Ghafarollahi, A., Buehler, M.J.: Automating alloy
design and discovery with physics-aware multimodal
multiagent AI. Proc. Natl. Acad. Sci. U.S.A. 122(4),
2414074122 (2025)

[22] Luo, J., Zhang, W., Yuan, Y., Zhao, Y., Yang,
J., Gu, Y., Wu, B., Chen, B., Qiao, Z., Long,
Q., Tu, R., Luo, X., Ju, W., Xiao, Z., Wang, Y.,
Xiao, M., Liu, C., Yuan, J., Zhang, S., Jin, Y.,
Zhang, F., Wu, X., Zhao, H., Tao, D., Yu, P.S.,
Zhang, M.: Large language model agent: a survey on
methodology, applications and challenges. Preprint
at https://arxiv.org/abs/2503.21460 (2025)

[30] Zou, Y., Cheng, A.H., Aldossary, A., Bai, J., Leong,
S.X., Campos-Gonzalez-Angulo, J.A., Choi, C., Ser,
C.T., Tom, G., Wang, A., Zhang, Z., Yakavets, I.,
Hao, H., Crebolder, C., Bernales, V., Aspuru-Guzik,
A.: El Agente: an autonomous agent for quantum
chemistry. Matter 8(7), 102263 (2025)
[31] Huang, X., Chen, J., Fei, Y., Li, Z., Schwaller, P.,
Ceder, G.: CASCADE: cumulative agentic skill creation through autonomous development and evolution. Preprint at https://arxiv.org/abs/2512.23880
(2025)

[23] Guo, T., Chen, X., Wang, Y., Chang, R., Pei, S.,
Chawla, N.V., Wiest, O., Zhang, X.: Large language
model based multi-agents: a survey of progress
and challenges. Proceedings of the 33rd International Joint Conference on Artificial Intelligence, pp.
8048–8057 (2024)

[32] Hu, J., Nawaz, H., Hou, Y.-F., Rui, Y., Chi,
L., Chen, Y., Ullah, A., Dral, P.O.: Aitomia:
your intelligent assistant for AI-driven atomistic
and quantum chemical simulations. Preprint at
https://arxiv.org/abs/2505.08195 (2025)

[24] Wang, L., Xu, W., Lan, Y., Hu, Z., Lan, Y.,
Lee, R.K.-W., Lim, E.-P.: Plan-and-solve prompting: Improving zero-shot chain-of-thought reasoning by large language models. In: Rogers, A.,
Boyd-Graber, J., Okazaki, N. (eds.) Proceedings
of the 61st Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long
Papers), pp. 2609–2634. Association for Computational Linguistics, Toronto, Canada (2023).
https://aclanthology.org/2023.acl-long.147/

[33] Vriza, A., Kornu, U., Koneru, A., Chan, H.,
Sankaranarayanan, S.K.R.S.: Multi-agentic AI
framework for end-to-end atomistic simulations.
Digit. Discov. 5, 440–452 (2026)
[34] Orimo, Y., Kurata, I., Mori, H., Okuno,
R., Sawada, R., Okanohara, D.: PARC: an
autonomous self-reflective coding agent for robust
execution of long-horizon tasks. Preprint at
https://arxiv.org/abs/2512.03549 (2025)

[25] Shen, Y., Song, K., Tan, X., Li, D., Lu, W., Zhuang,
Y.: HuggingGPT: Solving AI tasks with ChatGPT
and its friends in Hugging Face. Advances in Neural
Information Processing Systems, vol. 36, pp. 38154–
38180 (2023)

[35] Yang, F., Evans, J.D.: QUASAR: a universal
autonomous system for atomistic simulation and a
benchmark of its capabilities. J. Chem. Inf. Model.
(2026)

[26] Li, A., Xie, Y., Li, S., Tsung, F., Ding, B.,
Li, Y.: Agent-oriented planning in multi-agent
systems. The 13th International Conference on
Learning Representations, pp. 32933–32955 (2025).
https://openreview.net/forum?id=EqcLAU6gyU

[36] Chaudhari, A., Ock, J., Barati Farimani, A.: Modular large language model agents for multi-task
computational materials science. Commun. Mater.
7, 131 (2026)

[27] Shinn,
N.,
Cassano,
F.,
Gopinath,
A.,
Narasimhan, K., Yao, S.: Reflexion: language
agents with verbal reinforcement learning.

[37] Wang, X., Li, C., Zhang, B., Shi, J., Ran, N., Li,

[45] Brown, T., Mann, B., Ryder, N., Subbiah, M.,
Kaplan, J.D., Dhariwal, P., Neelakantan, A.,
Shyam, P., Sastry, G., Askell, A., Agarwal, S.,
Herbert-Voss, A., Krueger, G., Henighan, T., Child,
R., Ramesh, A., Ziegler, D., Wu, J., Winter, C.,
Hesse, C., Chen, M., Sigler, E., Litwin, M., Gray,
S., Chess, B., Clark, J., Berner, C., McCandlish,
S., Radford, A., Sutskever, I., Amodei, D.: Language models are few-shot learners. In: Larochelle,
H., Ranzato, M., Hadsell, R., Balcan, M.F., Lin, H.
(eds.) Advances in Neural Information Processing
Systems, vol. 33, pp. 1877–1901 (2020)

L., Liu, J., Zeng, D.: S1-MatAgent: a planner driven
multi-agent system for material discovery. Preprint
at https://arxiv.org/abs/2509.14542 (2025)
[38] Chiang, Y., Hsieh, E., Chou, C.-H., Riebesell,
J.: LLaMP: Large language model made powerful for high-fidelity materials knowledge retrieval.
In: Christodoulopoulos, C., Chakraborty, T., Rose,
C., Peng, V. (eds.) Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pp. 25189–25221. Association for
Computational Linguistics, Suzhou, China (2025).
https://aclanthology.org/2025.emnlp-main.1280/

[46] Michaud-Agrawal, N., Denning, E.J., Woolf, T.B.,
Beckstein, O.: MDAnalysis: a toolkit for the analysis of molecular dynamics simulations. J. Comput.
Chem. 32(10), 2319–2327 (2011)

[39] Larsen, A.H., Mortensen, J.J.r., Blomqvist, J.,
Castelli, I.E., Christensen, R., Dulak, M., Friis, J.,
Groves, M.N., Hammer, B.r., Hargus, C., Hermes,
E.D., Jennings, P.C., Jensen, P.B., Kermode, J.,
Kitchin, J.R., Kolsbjerg, E.L., Kubal, J., Kaasbjerg, K., Lysgaard, S., Maronsson, J.B., Maxson, T.,
Olsen, T., Pastewka, L., Peterson, A., Rostgaard,
C., Schiø tz, J., Schütt, O., Strange, M., Thygesen, K.S., Vegge, T., Vilhelmsen, L., Walter, M.,
Zeng, Z., Jacobsen, K.W.: The atomic simulation
environment—a Python library for working with
atoms. J. Phys.:Condens. Matter 29(27), 273002
(2017)

[47] Gowers, R.J., Linke, M., Barnoud, J., Reddy, T.J.E.,
Melo, M.N., Seyler, S.L., Domański, J., Dotson,
D.L., Buchoux, S., Kenney, I.M., Beckstein, O.:
MDAnalysis: a Python package for the rapid analysis of molecular dynamics simulations. Proceedings
of the 15th Python in Science Conference, pp.
98–105 (2016)
[48] Folk, Mike and Cheng, Albert and Yates, Kim:
HDF5: A file format and I/O library for high performance computing applications. Proceedings of
Supercomputing, vol. 99, pp. 5–33 (1999)

[40] Martı́nez, L., Andrade, R., Birgin, E.G., Martı́nez,
J.M.: PACKMOL: a package for building initial configurations for molecular dynamics simulations. J.
Comput. Chem. 30(13), 2157–2164 (2009)

[49] Lewis, P., Perez, E., Piktus, A., Petroni, F.,
Karpukhin, V., Goyal, N., Küttler, H., Lewis,
M., Yih, W.-t., Rocktäschel, T., Riedel, S., Kiela,
D.: Retrieval-augmented generation for knowledgeintensive NLP tasks. Advances in Neural Information Processing Systems, vol. 33, pp. 9459–9474
(2020)

[41] Thompson, A.P., Aktulga, H.M., Berger, R., Bolintineanu, D.S., Brown, W.M., Crozier, P.S., in ’t
Veld, P.J., Kohlmeyer, A., Moore, S.G., Nguyen,
T.D., Shan, R., Stevens, M.J., Tranchida, J., Trott,
C., Plimpton, S.J.: LAMMPS – a flexible simulation tool for particle-based materials modeling at
the atomic, meso, and continuum scales. Comput.
Phys. Commun. 271, 108171 (2022)

[50] Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan,
J., Bi, Y., Dai, Y., Sun, J., Wang, M.,
Wang, H.: Retrieval-augmented generation for
large language models: a survey. Preprint at
https://arxiv.org/abs/2312.10997 (2023)

[42] Ramasubramani, V., Dice, B.D., Harper, E.S.,
Spellings, M.P., Anderson, J.A., Glotzer, S.C.:
freud: a software suite for high throughput analysis of particle simulation data. Comput. Phys.
Commun. 254, 107275 (2020)

[51] Brown, B., Juravsky, J., Ehrlich, R., Clark, R., Le,
Q.V., Ré, C., Mirhoseini, A.: Large language monkeys: scaling inference compute with repeated sampling. Preprint at https://arxiv.org/abs/2407.21787
(2024)

[43] Karpukhin, V., Oğuz, B., Min, S., Lewis, P., Wu,
L., Edunov, S., Chen, D., Yih, W.-t.: Dense passage retrieval for open-domain question answering.
Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing, pp.
6769–6781 (2020)

[52] Green, M.S.: Markoff random processes and the statistical mechanics of time-dependent phenomena. ii.
irreversible processes in fluids available to purchase.
J. Chem. Phys. 22(3), 398–413 (1954)

[44] Sumers, T., Yao, S., Narasimhan, K.R., Griffiths,
T.L.: Cognitive architectures for language agents.
Trans. Mach. Learn. Res. (2024)

[53] Kubo, R.: Statistical-mechanical theory of irreversible processes. i. general theory and simple
applications to magnetic and conduction problems.

J. Phys. Soc. Jpn. 12(6), 570–586 (1957)

Round robin study: molecular simulation of thermodynamic properties from models with internal
degrees of freedom. J. Chem. Theory Comput.
13(9), 4270–4280 (2017)

[54] Choi, J.M., Kim, J., Lee, J.-H., Son, W.-J., Han, S.:
Atomistic insights into Cu/amorphous-Tax N interfacial adhesion via machine learning interatomic
potentials: effects of stoichiometry and interface
construction. ACS Appl. Electron. Mater. 7(24),
11165–11179 (2025)

[64] Jain, A., Ong, S.P., Hautier, G., Chen, W.,
Richards, W.D., Dacek, S., Cholia, S., Gunter, D.,
Skinner, D., Ceder, G., Persson, K.A.: Commentary:
the Materials Project: a materials genome approach
to accelerating materials innovation. APL Mater.
1(1), 011002 (2013)

[55] Wilson, E.B.: Probable inference, the law of succession, and statistical inference. J. Am. Stat. Assoc.
22(158), 209–212 (1927). Accessed 2026-05-22

[65] Kim, J., Lee, J., Oh, S., Park, Y., Hwang, S.,
Han, S., Kang, S., Kang, Y.: An efficient forgettingaware fine-tuning framework for pretrained universal machine-learning interatomic potentials. npj
Comput. Mater. 12, 26 (2026)

[56] Newcombe, R.G.: Two-sided confidence intervals for
the single proportion: comparison of seven methods.
Stat. Med. 17(8), 857–872 (1998)
[57] Wood, B.M., Dzamba, M., Fu, X., Gao, M.,
Shuaibi, M., Barroso-Luque, L., Abdelmaqsoud,
K., Gharakhanyan, V., Kitchin, J.R., Levine,
D.S., Michel, K., Sriram, A., Cohen, T., Das,
A., Sahoo, S.J., Rizvi, A., Ulissi, Z.W., Zitnick, C.L.: UMA: A family of universal models for atoms. The 39th Annual Conference on
Neural Information Processing Systems (2025).
https://openreview.net/forum?id=SvopaNxYWt

[66] Zou, H.P., Huang, W.-C., Wu, Y., Guo, J., Chen,
Y., Miao, C., Nguyen, H., Zhou, Y., Zhang, W.,
Fang, L., Zhang, H., Wang, F., Zhang, P., Wang,
H., He, L., Li, Y., Li, D., Jiang, R., Liu, X.,
Yu, P.S.: LLM-based human-agent collaboration
and interaction systems: a survey. Preprint at
https://arxiv.org/abs/2505.00753 (2025)
[67] Gottweis, J., Weng, W.-H., Daryin, A., Tu, T.,
Palepu, A., Sirkovic, P., Myaskovsky, A., Weissenberger, F., Rong, K., Tanno, R., Saab, K.,
Popovici, D., Blum, J., Zhang, F., Chou, K., Hassidim, A., Gokturk, B., Vahdat, A., Kohli, P.,
Matias, Y., Carroll, A., Kulkarni, K., Tomasev,
N., Guan, Y., Dhillon, V., Vaishnav, E.D., Lee,
B., Costa, T.R.D., Penadés, J.R., Peltz, G., Xu,
Y., Pawlosky, A., Karthikesalingam, A., Natarajan, V.: Towards an AI co-scientist. Preprint at
https://arxiv.org/abs/2502.18864 (2025)

[58] Singh, A. et al.: OpenAI GPT-5 System Card
(2026). https://arxiv.org/abs/2601.03267
[59] OpenAI: GPT-5.4 Thinking System Card. OpenAI Deployment Safety Hub. Accessed: 2026-0522 (2026). https://deploymentsafety.openai.com/
gpt-5-4-thinking
[60] Wang, X., Wei, J., Schuurmans, D., Le, Q.V.,
Chi, E.H., Narang, S., Chowdhery, A., Zhou, D.:
Self-consistency improves chain of thought reasoning in language models. The 11th International
Conference on Learning Representations (2023).
https://openreview.net/forum?id=1PL1NIMMrw

[68] Anthropic: Model Context Protocol: Introduction. Accessed: 2026-05-17 (2024). https:
//modelcontextprotocol.io/docs/getting-started/
intro

[61] Ju, S., You, J., Kim, G., Park, Y., An, H., Han,
S.: Application of pretrained universal machinelearning interatomic potential for physicochemical
simulation of liquid electrolytes in Li-ion batteries.
Digit. Discov. 4(6), 1544–1559 (2025)

[69] Liu, J.: LlamaIndex, (2022). https://github.com/
jerryjliu/llama index
[70] Robertson, S.E., Walker, S.: Some simple effective
approximations to the 2-Poisson model for probabilistic weighted retrieval. In: Croft, B.W., van Rijsbergen, C.J. (eds.) Proceedings of the 17th Annual
International ACM SIGIR Conference on Research
and Development in Information Retrieval, pp. 232–
241. Springer, London (1994)

[62] Snell, C.V., Lee, J., Xu, K., Kumar, A.: Scaling LLM test-time compute optimally can be
more effective than scaling model parameters
for reasoning. The 13th International Conference on Learning Representations (2025).
https://openreview.net/forum?id=4FWAwZtd2n

[71] Cormack, G.V., Clarke, C.L.A., Buettcher, S.:
Reciprocal rank fusion outperforms Condorcet and
individual rank learning methods. Proceedings of
the 32nd Annual International ACM SIGIR Conference on Research and Development in Information

[63] Schappals, M., Mecklenfeld, A., Kröger, L.C.,
Botan, V.A., Köster, A., Stephan, S., Garcia, E.J.,
Rutkai, G., Raabe, G., Klein, P., Leonhard, K.,
Glass, C.W., Lenhard, J., Vrabec, J., Hasse, H.:

Retrieval, pp. 758–759 (2009)
[72] Tai, S.T., Wang, C., Cheng, R., Chen, Y.: Revisiting many-body interaction heat current and thermal
conductivity calculations using the moment tensor potential/lammps interface. J. Chem. Theory
Comput. 21(7), 3649–3657 (2025)
[73] Mantina, M., Chamberlin, A.C., Valero, R., Cramer,
C.J., Truhlar, D.G.: Consistent van der Waals
radii for the whole main group. J. Phys. Chem. A
113(19), 5806–5812 (2009)
[74] Evans, D.J., Holian, B.L.: The Nose–Hoover thermostat. J. Chem. Phys. 83(8), 4069–4074 (1985)
[75] Martyna, G.J., Tobias, D.J., Klein, M.L.: Constant
pressure molecular dynamics algorithms. J. Chem.
Phys. 101(5), 4177–4189 (1994)
[76] Shinoda, W., Shiga, M., Mikami, M.: Rapid estimation of elastic constants by molecular dynamics
simulation under constant stress. Phys. Rev. B 69,
134103 (2004)
[77] Allen, M.P., Tildesley, D.J.: Computer Simulation of
Liquids, 2nd edn. Oxford University Press, Oxford
(2017)
[78] He, X., Zhu, Y., Epstein, A., Mo, Y.: Statistical variances of diffusional properties from ab initio molecular dynamics simulations. npj Comput. Mater. 4(1),
18 (2018)
[79] Lee, S.Y., Kim, H., Park, Y., Jeong, D., Han,
S., Park, Y., Lee, J.W.: FlashTP: Fused, sparsityaware tensor product for machine learning interatomic potentials. In: Singh, A., Fazel, M.,
Hsu, D., Lacoste-Julien, S., Berkenkamp, F.,
Maharaj, T., Wagstaff, K., Zhu, J. (eds.) Proceedings of the 42nd International Conference on
Machine Learning. Proceedings of Machine Learning Research, vol. 267, pp. 33143–33156 (2025).
https://proceedings.mlr.press/v267/lee25l.html
[80] Grimme, S., Antony, J., Ehrlich, S., Krieg, H.: A
consistent and accurate ab initio parametrization
of density functional dispersion correction (DFT-D)
for the 94 elements H-Pu. J. Chem. Phys. 132(15),
154104 (2010)
[81] Grimme, S., Ehrlich, S., Goerigk, L.: Effect of
the damping function in dispersion corrected density functional theory. J. Comput. Chem. 32(7),
1456–1465 (2011)
