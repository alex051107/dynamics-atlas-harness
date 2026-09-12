# MDGYM: Benchmarking AI Agents on Molecular Simulations

**Authors:** Vinay Kumar, Satyendra Rajput, Mausam, N. M. Anoop Krishnan
**Year:** 2026
**Venue:** arXiv preprint
**DOI:** 10.48550/arXiv.2605.08941
**Source PDF URL:** https://arxiv.org/pdf/2605.08941
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

                                            MDG YM: Benchmarking AI Agents on Molecular
                                                          Simulations


                                                  Vinay Kumar1 , Satyendra Rajput2 , Mausam1,2 , N. M. Anoop Krishnan1,3
                                                  1
                                                    Yardi School of Artificial Intelligence, Indian Institute of Technology Delhi
                                             2
                                               Department of Computer Science and Engineering, Indian Institute of Technology Delhi
                                            3
                                              Department of Civil and Environmental Engineering, Indian Institute of Technology Delhi
                                                      {vinay.kumar, msz208502, mausam, krishnan}@iitd.ac.in




arXiv:2605.08941v1 [cs.AI] 9 May 2026
                                                                                        Abstract
                                                    The promise of AI-driven scientific discovery hinges on whether AI agents can
                                                    autonomously design and execute the computational workflows that underpin mod-
                                                    ern science. Molecular dynamics (MD) simulation presents a natural test bed to
                                                    stress-test this claim; it requires translating physical intuition into syntactically
                                                    and semantically correct input scripts, reasoning about initial and boundary condi-
                                                    tions, diagnosing numerically unstable trajectories, and interpreting outputs against
                                                    known physical behavior and laws. We introduce MDG YM, a benchmark of 169
                                                    expert-curated MD simulations spanning L AMMPS and G ROMACS, two widely
                                                    used MD packages, across three increasing difficulty levels. We evaluate three
                                                    agentic frameworks—Claude Code, Codex, and OpenHands—with four LLMs,
                                                    and find that all perform poorly: even the strongest agent solves only 21% of
                                                    easy-level tasks, with less than 10% at higher difficulties. Trajectory analysis
                                                    reveals a characteristic pattern of failure—agents successfully invoke simulation
                                                    machinery but produce physically unstable configurations, fabricate numerical out-
                                                    puts without executing the underlying computation, or abandon tasks prematurely
                                                    rather than iterating through simulation-specific errors. These failure modes are
                                                    qualitatively distinct from those observed in general software engineering bench-
                                                    marks, indicating that fluent code generation does not transfer to grounded physical
                                                    reasoning.


                                        1    Introduction
                                        The vision of autonomous scientific discovery, where AI systems independently formulate hypotheses,
                                        design experiments, execute computational workflows, and interpret results against physical theory,
                                        has emerged as one of the frontiers in AI research [Wang et al., 2023, Lu et al., 2024, Boiko et al.,
                                        2023]. Realizing this vision requires agents that can do far more than generate syntactically correct
                                        code. Agents operating in scientific domains must reason about physical validity, choose appropriate
                                        experimental methodology, design experiments grounded on relevant concepts, interpret numerical
                                        outputs against known physical laws, and analyze them to arrive at meaningful conclusions; skills
                                        that present compiler or test suites for coding cannot verify. These demands are qualitatively distinct
                                        from those of general software engineering, where correctness is typically verifiable and errors can
                                        be detected through stack traces.
                                        Molecular dynamics (MD) simulation, central to drug discovery [Ahmed et al., 2023], materials
                                        design [Choi, 2023], and biophysics [Sinha et al., 2022], is a methodology to perform in silico
                                        experiments. MD demands the rigor of live lab experiments and requires a chain of reasoning steps
                                        that stress AI agents in ways that standard coding benchmarks do not. An agent must translate a
                                        physical description of a system into syntactically and semantically correct input scripts, reason
                                        about initial and boundary conditions, select appropriate force fields and integration parameters,

                                        Preprint.
monitor trajectories for numerical instability, and interpret output quantities against known physical
behavior. Crucially, these competencies must be composed across a multi-stage pipeline—system
setup, initialization, energy minimization, equilibration, production, and post-processing—where a
physically incoherent choice at any stage produces not a runtime error but a silently wrong simulation:
the code runs, output is generated, and no exception is raised, yet the result is physically meaningless.
This is categorically different from software engineering benchmarks [Jimenez et al., 2023], where
failing tests, type errors, and stack traces provide immediate, interpretable feedback that agents
can observe and act on during execution. In MD simulation, no such signal exists; a simulation
configured with the wrong force field, wrong ensemble, or wrong integration timestep runs silently
to completion in most cases, and the agent must rely on physical intuition alone to recognize and
recover from errors, without access to any ground truth. This absence of execution-time correctness
feedback, combined with the breadth of domain knowledge required at each pipeline stage, makes
MD simulation a uniquely demanding testbed for the question at the heart of AI-for-science: can AI
agents autonomously design and execute scientific workflows?
To rigorously investigate this question, we introduce MDG YM, an expert-curated benchmark of
169 molecular simulation tasks spanning two widely used MD engines—L AMMPS [Thompson
et al., 2022] and G ROMACS [Hess et al., 2008]—across three increasing difficulty levels. Each task
represents realistic scientific problems encountered in research rather than toy-settings, is developed
and verified by domain experts, and evaluated against physically meaningful reference quantities
with automated scoring. Using MDG YM, we conduct a systematic evaluation of three agentic
frameworks—Claude Code, Codex, and OpenHands—instantiated with four LLMs spanning both
frontier proprietary models and open-source alternatives. Our contributions are as follows.

       • Benchmark: We release MDG YM, a rigorously constructed benchmark for molecular
         simulation that the community can use to track progress toward autonomous scientific
         computing.
       • Evaluation: We provide the comprehensive evaluation of state-of-the-art AI agents on MD
         simulation, revealing a large and consistent performance gap across all model families and
         agentic frameworks with the best one scoring only ∼21% for easy tasks, and < 10% at
         higher difficulties.
       • Diagnosis: We present a taxonomy of simulation-specific failure modes—grounded in
         trajectory analysis and engine-level error classification—that characterizes precisely where
         and why current agents fall short, providing a roadmap for the capabilities that must be
         developed before AI agents can serve as reliable partners in computational science.

2   Background and related works
Molecular Dynamics Simulation. Molecular dynamics simulation is a computational methodology
for studying the time evolution of atomistic systems by numerically integrating the classical equations
of motion. Given a set of N atoms at positions {qi }N                         N
                                                      i=1 and momenta {pi }i=1 , MD propagates the
system forward in time according to Hamilton’s equations,

                                   dqi   ∂H            dpi    ∂H
                                       =     ,             =−     ,                                  (1)
                                    dt   ∂pi            dt    ∂qi
                P 2
where, H =        i pi /2mi + V ({qi }) is the Hamiltonian, mi are atomic masses, and V is the
potential energy surface. In practice, integration is performed using the symplectic integrators (energy
conserving) such as velocity Verlet algorithm with a timestep ∆t on the order of femtoseconds,
and the dominant computational cost is the evaluation of forces Fi = −∂V /∂qi at every step.
The ensemble used in MD simulation should be representative of the thermodynamic conditions of
the real-world phenomenon which is simulated. The basic NVE integrator, where the number of
particles N , volume V , and total energy E are conserved, is extended in most applications through
thermostats to sample the constant-temperature NVT ensemble, barostats to additionally control
pressure in the NPT ensemble, or non-equilibrium protocols— uniaxial loading, planar shear, or
thermal gradients—to compute mechanical and transport properties.
What distinguishes MD from general software engineering is the nature of correctness. In most
software engineering tasks, the expected output is known before the code is written; for instance, a


                                                   2
sorting function should return a sorted array. MD simulation inverts this relationship. The outcome
of the simulation, such as the equilibrium density of a polymer melt or the diffusion coefficient of
ions in solution, is not known before the simulation for systems of realistic complexity. In this sense,
a correctly configured MD simulation is the computational equivalent of a laboratory experiment:
the protocol must be physically consistent, the measurement must be performed appropriately, and
the result is not known in advance. Further, a physically valid simulation must satisfy a hierarchy
of conditions simultaneously, such as energy and momentum conservation, timesteps smaller than
the period corresponding to the highest frequency mode in the system, interactions between atoms
meaningfully approximating quantum mechanical forces through an empirical potential, and system
size large enough to avoid finite-size effects. A detailed discussion on MD simulations along with
additional such conditions is included in App. A.
Benchmarks for Scientific AI Agents. With the rise of AI scientists (see App. B for a discussion),
a growing body of benchmarks evaluates LLM agents on broader scientific tasks. ScienceAgent-
Bench [Chen et al., 2024] extracted 102 tasks from 44 peer-reviewed publications across four disci-
plines, finding that the best agent solves only 34.3% of tasks even when provided expert knowledge.
SciCode [Tian et al., 2024] presented 338 subproblems decomposed from 80 research-level problems
across 16 natural science subfields; Claude 3.5 Sonnet, the strongest model tested at publication time,
solved only 4.6% of problems in the most realistic setting. AILA [Mandal et al., 2025] evaluated
multiple LLMs on live laboratory experiments using atomic force microscopy. BixBench [Mitchener
et al., 2025] introduced 53 real-world bioinformatics analysis scenarios with 296 associated questions,
finding that frontier models achieve only 17% accuracy in the open-answer regime and no better than
random in multiple-choice. LAB-Bench [Laurent et al., 2024] covered over 2,400 multiple-choice
questions for practical biology research tasks, including literature reasoning, database navigation,
and sequence manipulation. SUPER [Bogin et al., 2024] evaluates agents on setting up and executing
tasks from ML and NLP research repositories, comprising 45 expert-curated end-to-end problems.
Most recently, Corral Ríos-García et al. [2026] evaluated AI scientist on eight environments with
over 25,000 runs and found that they exhibit reduced revision beliefs (26% of traces), and ignore
evidences (68%). These benchmarks establish a consistent pattern: LLM agents struggle when tasks
require executable, physically valid outputs within specialized scientific software.
Benchmarks for MD Simulation Agents. Agentic frameworks for MD simulation include: MD-
Crow [Campbell et al., 2025] automates technical MD tasks within a predefined toolspace for protein
simulations, DynaMate [Guilbert et al., 2025] presents a multi-agent framework for end-to-end MD
workflows for protein and protein-ligand systems, and PolyJarvis [Zhao et al., 2026] couples an LLM
with the RadonPy simulation platform for polymer property prediction. However, these frameworks
focused on specific materials or systems, limiting their wider applicability as general-purpose MD
simulation agents. The closest prior work to MDG YM MDAgent2 [Shi et al., 2026], successor of
MDAgent [Shi et al., 2025], targets LAMMPS code generation. They proposed MD-EvalBench,
described as the first benchmark for LAMMPS code generation and question answering, and builds
a multi-agent system integrating code generation, execution, and self-correction. However, MD-
EvalBench is limited to a single simulation engine (LAMMPS) and does not span multiple difficulty
tiers or cover the full simulation pipeline from setting up the system configuration to output extraction
and post-processing. NAMD-Agent [Chandrasekhar and Farimani, 2025] targets NAMD but is
similarly engine-specific and evaluated on a small, internally defined task set. MDG YM substantially
expands this landscape: 169 expert-curated tasks across both L AMMPS and G ROMACS, three difficulty
levels, a modular evaluation harness extensible to additional engines (AMBER, NAMD, OpenMM),
and the first systematic evaluation of frontier coding agents on end-to-end MD simulation.
Benchmarks for Coding Agents. With a rich history of benchmark ecosystem, earlier bench-
marks in the broader coding agent community, such as SWE-bench [Jimenez et al., 2023] and
HumanEval [Zhang et al., 2024], have largely been saturated. Terminal-Bench [Merrill et al., 2026]
evaluates agents on 89 realistic terminal tasks spanning scientific computing, software engineering,
and system administration, finding that even frontier models score below 65%. SUPER [Bogin
et al., 2024] and SciReplicate-Bench [Xiang et al., 2025] target research repository execution and
algorithmic reproduction, respectively. AInsteinBench [Duston et al., 2025] extends this to scientific
repositories, finding that agents struggle with preserving scientific invariants and maintaining correct-
ness in complex scientific algorithms. DevOps-Gym [Tang et al., 2026] benchmarks agents across
the software DevOps cycle. All of these benchmarks share a fundamental characteristic that limits
their relevance to computational science: correctness is syntactic or behavioral that can be verified by



                                                   3
test suites, stack traces, or output matching, and errors surface as observable signals that agents can
act on; features that make them qualitatively different from MDG YM.


3   Construction of MDG YM

MDG YM architecture. To enable systematic and reproducible evaluation, MDG YM is built as a
modular evaluation harness designed around three independently extensible layers: agents, engines,
and validators. The agent layer provides a unified interface for plugging in any CLI-accessible coding
agent. Each agent implementation wraps the corresponding tool as a subprocess, streams its output to
a structured trajectory log, and returns control to the orchestrator upon completion or timeout. The
orchestration layer coordinates a single evaluation episode—building the task prompt, invoking the
agent, and passing its output to the validator—and is fully decoupled from the details of any specific
agent or engine. The validator layer handles scoring: each MD engine has a corresponding validator
that reads the agent’s reported output, compares it against ground-truth reference values within a
5% relative tolerance, and returns both a binary pass/fail flag and a partial-credit score reflecting the
fraction of metrics correctly reported. Each layer is governed by a well-defined abstract interface,
enabling extension to new agents, MD engines such as AMBER, NAMD, or OpenMM, or scoring
metrics straightforward by implementing a single class with no changes to any other component.
Dataset construction and curation. The MDG YM dataset is manually developed and curated by
experts in the field of MD simulations with the goal of constructing a realistic, domain-specific
dataset that corresponds research-level simulations beyond toy examples. Task descriptions for the
simulations were drawn from research publications, tutorials, and from scratch based on domain-
expertise. G ROMACS tasks use files sourced from the G ROMACS repository, Rajput et al. [2023],
Koch et al. [2025], Lemkul [2018], and Gravelle et al. [2025], with the remainder constructed from
scratch; the L AMMPS tasks draw from the official L AMMPS repository [Thompson et al., 2022],
and tutorials Gravelle et al. [2025]. All sourced files were subsequently modified, for instance by
substituting a different material, ensemble, or loading condition, so that no task reduces to running an
existing example verbatim. It was ensured that the tasks were beyond toy examples and represented
research-level questions.
Both engines follow the same simulation protocol: energy minimization, NVT and NPT equilibration,
and a production run from which all observables are extracted by post-processing. The answers were
obtained by executing the corresponding simulations using G ROMACS and L AMMPS, and the values
are considered as the ground truth. Python scripts were used to compute relevant observables, while
additional quantities were derived using built-in commands and analysis tools within these simulation
packages. Finally, a JSON file was prepared, which is used as the input for each task (App. C.2).
Quality Control. All drafted questions underwent a rigorous multi-stage review process. Initially,
ensemble of LLMs (Claude and GPT) were employed to identify ambiguities, incomplete specifi-
cations, and potential errors in the prepared questions. The questions were then manually refined
based on the feedback. This iterative review-and-refinement cycle continued until each question met
three key criteria: (i) correctness, ensuring sufficient and accurate details for reproducibility; (ii)
credibility, ensuring the question reflects realistic materials science research scenarios and appropriate
domain complexity; and (iii) clarity, ensuring the expected output format and evaluation criteria are
well-defined. To ensure benchmark quality, each simulation was further validated through visual
inspection of the output trajectories using VMD or OVITO, confirming that simulated systems exhibit
physically realistic behavior with proper structural evolution and equilibration dynamics.
Dataset analysis. The MDG YM benchmark dataset comprises a total of 169 independent problems
(or simulations) and 303 tasks (such as computing specific quantities from the simulation), evaluated
on 95 distinct properties (such as density, Young’s modulus, or radial distribution). See Fig. 1 for
the detailed statistics of the datasets generated in MDG YM. These problems utilize two widely
used MD simulation packages: G ROMACS and L AMMPS. G ROMACS is generally preferred for
biomolecular simulations (proteins, lipids, nucleic acids), while L AMMPS is a more flexible, versatile
framework ideal for materials science, polymers, and coarse-grained systems (see App. C.3). The
dataset encompasses a diverse range of materials and systems, including biomolecules, metals and
alloys, and polymers, carbon-based nanomaterials, covering multiple states of matter such as solids
(crystalline and amorphous), liquids, and gases. The evaluated properties are categorized into six
major classes: thermodynamic (25), structural (25), mechanical (30), transport (6), magnetic (2),


                                                    4
and other/numerical (7), where the numbers in parentheses indicate the count of unique properties.
MD simulations are most used to study thermodynamic properties of solids, which is reflected in
our dataset as well (Fig. 1). The questions in the dataset ask for multiple properties (≥ 1); we
formulate questions that produce an unambiguous numerical answer for each property. (see App. C.4
for example). The distribution of analytical question types is provided in App. C.6. The questions are
divided into three levels of difficulty. Level 1 (Easy) corresponds to thermodynamic properties such
as temperature, pressure, and total energy per particle that require only minimal post-processing to
the native output from the simulation. Level 2 (Medium) comprises properties that require substantial
post-processing of the simulation output, such as coordination numbers, average radius of gyration,
hydrogen bond tracking, and any energy component other than potential or total energy. Note that
these quantities can also be obtained at run time via intermediate logic within the MD engine prior to
output. Level 3 (Hard) encompasses complex properties that require specialized simulations, beyond
simple equilibration runs, such as non-equilibrium physical setups (such as deformation, shear, or
tensile protocols), complex multi-stage runs, or post-processing of the simulation output through
curve fitting (e.g., using a Python script to calculate a slope from mean-squared displacement).
Examples include Young’s modulus, shear viscosity, diffusion coefficients, thermal conductivity, and
magnetic properties.
Validation by human experts. To ensure the reliability of the dataset, we conducted a validation
study involving five human experts. Each expert simulated 10 systems (five using G ROMACS and five
using L AMMPS), with an equal distribution across different difficulty levels, resulting in a total of
50 evaluated systems and 95 physical quantities. For this purpose, the experts were provided with
the corresponding structure and topology files and were asked to perform the simulations, and their
results were compared against the ground truth. Based on this evaluation, we obtained 87/95 correct
responses from the human experts (91.6% accuracy), where 8 entries exceeded the 5% error threshold,
demonstrating high overall reasonable accuracy.

                                                                   Biomacromolecules 24.9%
(a)                                            (b)                 Abstract LJ / CG 23.7%
                       Solid Amorphous 38.5%                       Organic Solvents & Small Molecules 10.7%
                       Gases 1.2%                                  Aqueous Systems 9.5%
                       Solid Crystal 26.0%                         Metals & Alloys 9.5%
                       Liquid 34.3%                                Polymers 8.3%
                                                                   Semiconductors & Ceramics 7.7%
                                                                   Carbon Nanomaterials 5.9%

(c)                                            (d)                 Thermodynamic Properties 58.1%
                       Biomolecular 39.6%                          Structural Properties 22.4%
                       Pair Potential 34.5%                        Mechanical Properties 13.5%
                       Metals 14.6%                                Other / Numerical 3.0%
                       Other 11.1%                                 Transport Properties 2.0%
                                                                   Magnetic Properties 1.0%

Figure 1: Statistical overview of the molecular dynamics simulation dataset across four classification
dimensions. Donut charts showing the distribution of simulations by (a) physical state, (b) materi-
al/system type, (c) force field category, and (d) computed property type.

4     Evaluation Setup

Models. We evaluated three state-of-the-art coding agents, OpenHands, Codex, and Claude Code,
with different LLM backbones on MDG YM. For OpenHands Wang et al. [2024], an open-source
multi-agent system designed for autonomous software development, we experiment with open-source
LMs that possess agentic capabilities, that is, gpt-oss-20B OpenAI [2025], and Qwen3-Coder Qwen
[2025]. For proprietary agents, we evaluate OpenAI Codex (gpt-5.2-codex) and Anthropic Claude
Code (claude-4.6-sonnet), each run with its default configuration. While the implementation
details of these proprietary agents are not publicly available, we ensure that all agents have access
to the necessary tools, such as shell execution and file operations, for task execution. Models with
configurable reasoning capabilities are run with the provider’s default. All the open-source models
were run with their respective maximum context lengths. Open-source models are used with their
maximum supported context length via vLLM Kwon et al. [2023] using 4 × A100 80GB GPUs,
while closed-source models are accessed through their respective first-party APIs.


                                                     5
Environment. All agents are evaluated in headless mode with yolo execution enabled, allowing fully
autonomous operation without per-command permission. The computing environment is preloaded
with L AMMPS and G ROMACS modules, as well as other required Python packages. We provide the
agent with the starting files, such as the potential and structure files.
Task Prompting. Each problem is presented as a single structured prompt derived from the problem’s
JSON specification as mentioned in Sec. 3. The prompt contains: the problem ID, the target MD
engine (L AMMPS or G ROMACS), a natural-language description of the simulation, the list of required
output metrics, and paths to any pre-supplied input files. Agents are instructed to write all simulation
scripts to a dedicated working directory and to produce a final_answer.json file containing metric
names as keys and unitless numerical values as values. Problems for which this file is absent or
cannot be parsed are automatically scored as zero.
Time Budget. To prevent agents from entering unbounded error-correction loops, each problem is
assigned a dynamic time budget of 300 + 3 × tsim seconds, where tsim is the wall-clock runtime of the
reference simulation. The fixed 300-second overhead allows the agent to parse the task and formulate
a plan, while the 3× multiplier affords approximately three full simulation attempts. If the agent
process exceeds this budget, it is forcibly terminated, and the problem is marked as failed.
Evaluation Metric. We evaluate each submission using a partial-credit metric that rewards agents
for correctly computing individual output quantities, even when the full task is P  not solved. Formally,
                                                                                1
for a problem with the required metric set M , the per-problem score is s = |M    |   k∈M 1 [passed(k)]
where passed(k) is 1 if the agent’s reported value for metric k falls within a 5% relative tolerance
of the reference value, and 0 otherwise. This tolerance accounts for natural numerical variation
arising from different integrator settings, random seeds, or platform-level floating-point differences.
A problem is considered a complete success only if s = 1.0, i.e., all required metrics pass. We report
both total partial score and full success rate across all problems, disaggregated by difficulty level and
MD engine. In addition to automated scoring, we conduct complementary automated analyses to
characterise agent failure modes: a trajectory analysis using a rule-based classifier derived from a
domain-expert-curated taxonomy and a simulation-level error analysis using LLM-as-judge with a
predefined engine-specific error categories for L AMMPS and G ROMACS. Full details of both analyses
are provided in App. D. We manually check if the agents guessed the answer or gave an answer based
on the simulation results; we penalise the agents for such behaviours and mark the task as failed. The
experiments were performed from 25 April 2026 to 5 May 2026.


5   Results and Discussion

Overall Performance. Figure 2 presents the
overall performance of all the agents on
MDG YM. Claude Code and Codex achieve
only 21% full-success rate on Easy tasks, al-
ready a low ceiling for the simpler problems in
the benchmark. Performance degrades sharply
with difficulty: Claude Code drops to 7% on
medium and 4% on hard, while Codex falls to Figure 2: Overall performance of all agents across
4% on both. The open-source models via Open- all MDG YM tasks. (a) Full-success rate (%) by
Hands collapse further. Qwen [OH] achieves difficulty level. (b) Total partial-credit score by
only 2% on easy tasks and near-zero thereafter, difficulty level. Performance degrades sharply with
while GPT-OSS [OH] scores 0% at every dif- difficulty for all agents.
ficulty level. The partial-credit total score (Figure 2b) reinforces this picture. Claude Code and
Codex each score 13.5 points on Easy tasks, while Qwen [OH] and GPT-OSS [OH] score 1.0 and 0.5
respectively, with all models, converging toward zero on hard tasks.
The consistent failure across agents and LLMs suggests that the difficulty is intrinsic to the domain
rather than an artifact of any particular model or design. Disaggregating by engine (App. Figures E.2
and E.3) reveals similar patterns across L AMMPS and G ROMACS, with marginal differences in
ranking. Codex slightly edges Claude Code on G ROMACS easy tasks (24% vs 20%), while Claude
Code leads slightly on L AMMPS (22% vs 19%), indicating that the bottleneck is not engine-specific
syntax knowledge but the deeper challenge of fundamental deficit in physically coherent experiment
design. Statistical significance of the results are reported in App. F.


                                                   6
Failure modes of agentic systems. While the overall performance reveal a sobering picture,
we analyze the failure modes of these systems through a series of research questions (RQs).




Figure 3: Task completion across difficulty levels, showing the percentage of trajectories reaching
each of three stages: Simulation Ran (agent attempted execution within the time budget), Produced
Answer (agent generated a final_answer.json output), and Correct Answer (reported values
within 5% tolerance of reference). (a) Easy tasks. (b) Medium tasks. (c) Hard tasks. A consistent
three-stage drop is observed across all difficulty levels and all agents.


RQ1: Are agents capable of completing a
whole simulation task? Figure 3 decomposes
trajectories across all difficulty levels into three
stages: Simulation Ran, Produced Answer,
and Correct Answer. On Easy tasks, Claude
Code and Codex completed simulations in 84%
and 98% of trajectories, respectively; this in-
cludes both successful and failed simulation
runs, meaning the agent at least attempted ex-
ecution within the time budget. Of these, only Figure 4: Taxonomy of failure modes across all
33% and 37% of trajectories, respectively, pro- agents, expressed as the % of errors attributable to
duced an answer, indicating that the majority each error class within failed trajectories.
of agents that initiated a simulation could not
recover from scripting or configuration errors
within the allotted time budget. Of those that did produce an answer, correct answers were obtained
in only 21% of trajectories for both agents, meaning that even when agents extracted a result, it most
often failed to meet physical correctness criteria, pointing to failures in answer extraction, output
parsing, or post-processing. This three-stage drop compounds across difficulty levels: on hard tasks,
Claude Code and Codex run simulations in 68% and 60% of trajectories, produce answers in only
25% and 24%, and arrive at correct answers in just 4% of cases for both.
The failure modes underlying this drop are not
uniform across agents. Figure 4 presents a tax-
onomy of errors (App. D) within failed trajec-
tories, revealing that agents fail in qualitatively
distinct ways. Notably, Environment Misunder-
standing is near-zero for Claude Code (0%) and
low for Codex (16%), confirming that the bench-
mark environment is not itself a barrier. The
failures are therefore intrinsic to the simulation
task. Syntax errors are the most prevalent error
type for the proprietary agents, constituting 37% Figure 5: Cumulative number of simulations reach-
of errors in Claude Code’s failed trajectories and ing each stage of the MD pipeline—Initialization,
50% in Codex’s. For Qwen [OH], Fabricated Minimization, Equilibration, and Production—for
Answers account for 46% of errors in failed tra- all four agents. (a) L AMMPS tasks. (b) G ROMACS
jectories, consistent with Figure 3, where Qwen tasks. Each bar represents the total number of runs
[OH] produces answers in 58% of easy trajecto- that successfully passed the respective stage.
ries despite running simulations in only 23%, a
production rate that exceeds its simulation execution rate and strongly implicates answer fabrica-
tion rather than genuine computation. Correct answers are achieved in approximately 2% of cases,
confirming these outputs are not grounded in actual simulation results. GPT-OSS [OH] presents a


                                                  7
contrasting pathology: Premature Termination accounts for 82% of errors in its failed trajectories,
consistent with its low answer production rate (16% on easy tasks) despite moderate simulation
execution (47%); the agent abandons the task rather than iterating through errors.
RQ2: Where in the simulation pipeline do agents fail? Figure 5 tracks the cumulative number of
runs reaching each stage of the MD pipeline, namely, Initialization, Minimization, Equilibration, and
Production, for all of the agents. For L AMMPS (Figure 5a), Codex initializes more runs (58 vs 48) but
both agents lose roughly half their runs by the Production stage, with Codex retaining 34 and Claude
Code 25. The drop is more dramatic for G ROMACS (Figure 5b): Claude Code initializes 70 runs but
retains only 33 by Production, while Codex collapses from 55 initialized runs to just 15 exhibiting a
73% drop. This suggests that the agent execution does not break down uniformly, but accelerates
through the stages where the physical demands of the workflow increase such as Equilibration and
Production. Agents often initialize a simulation system, but consistently fail to sustain the execution
once physically meaningful parameter choices, such as thermostat coupling, pressure control, force
field compatibility, determine whether the simulation remains stable. A single error at any of these
stages, such as a malformed topology file, a failed energy minimization, or incompatible equilibration
parameters, invalidates all downstream progress, making the sequential structure of MD workflows a
compounding liability for agents that cannot reason about physical validity.
RQ3: Do agents take physics-grounded steps? Figures 6a, 6b characterize simulation-level errors
within failed trajectories of Claude Code and Codex. For L AMMPS, approximately 75% of errors are
syntax-level for both agents, with the remaining 25% arising at runtime. For G ROMACS, the picture
is more nuanced. Codex errors are 75% preprocessing failures, while Claude Code shows a more
even split with 58% preprocessing and 42% runtime. These results suggest that Claude Code more
frequently succeeds in initiating simulations but then encounters failures from physically incoherent
configurations rather than malformed scripts.
The engine-specific error breakdowns reveal that the underlying failure categories go well beyond
scripting unfamiliarity. In L AMMPS (Figure 6a), Pair/Force Field mis-specification accounts for
17.6% of errors and Lost Atoms for 13.6%. The latter indicates that the simulation geometry or
boundary conditions were physically unstable from the outset, not merely syntactically malformed.
In G ROMACS (Figure 6b), the dominant categories are Coord/Topology Mismatch (29.0%), MDP
Parameter errors (23.2%), and Topology issues (21.7%). These errors reflect failures to maintain
physical consistency between the system’s structure, force field, and simulation protocol. These
errors do not correspond to a wrong syntax, they are errors that arise from not understanding what the
simulation is supposed to do.
This lack of physical grounding is further evidenced by the drop from Produced Answer to Correct
Answer seen in Figure 3. Even when agents successfully extract a numerical result, it is most often
incorrect. Correct post-processing of simulation demands methodological knowledge: the same
simulation trajectory can be used to compute different physical quantities depending on how the
analysis is performed. For example, computing the glass transition temperature Tg from an MD
trajectory requires fitting two linear segments to the density-temperature curve and identifying their
intersection. Choosing different temperature ranges for these fits produces meaningfully different Tg
estimates, rendering the answer incorrect even if the underlying simulation was physically sound.
Agents that pattern-match on syntax without understanding the measurement protocol will apply
the wrong analysis procedure, extract the wrong quantity, or compute over the wrong time window,
producing a numerically plausible but physically incorrect answer. When that pattern-matching
breaks down at the stages that demand physical coherence, they have no grounded basis on which to
recover. Much like a wet-lab experiment where an incorrectly designed measurement protocol yields
a physically meaningless result even from a well-prepared sample, correct simulation output requires
both a physically coherent simulation setup and a methodologically precise post-processing pipeline.
This suggests that agents fail not only at configuring simulations, but at reasoning about how physical
quantities are defined and measured.
RQ4: What do these failures collectively reveal? Our error taxonomy points to three capability
gaps that must be closed before agents can reliably solve MD simulation tasks: physical grounding,
reasoning about whether a simulation configuration is physically coherent before executing it, rather
than pattern matching; domain-aware error recovery, interpreting simulation-specific error messages
and translating them into physically meaningful corrective actions; and methodological precision in
post-processing, understanding which analysis procedure is physically correct for the quantity being



                                                  8
Figure 6: Engine-specific simulation error distributions within failed trajectories of Claude Code and
Codex. (a) L AMMPS errors, spanning 15 categories. The two distributions reveal that agents fail in
domain-specific ways that are qualitatively distinct across engines, and that the majority of failures
in both cases can be attributed to physically incoherent simulation design rather than superficial
scripting mistakes.


measured. These gaps are unlikely to be unique to molecular simulation. Any scientific computing
domain with multi-stage execution pipelines, physically defined correctness criteria, and numerically
silent failures, such as density functional theory, finite element simulation, or computational fluid
dynamics, will expose the same deficits in current agents. The broader implication is that progress on
software engineering benchmarks does not transfer to scientific computing, and that domain-grounded
benchmarks are essential to measure progress.



6   Conclusion

We introduce MDG YM, a benchmark of 169 expert-curated MD simulation tasks spanning L AMMPS
and G ROMACS across three difficulty levels, designed to evaluate whether AI agents can autonomously
execute end-to-end scientific computing workflows. We evaluate three agentic frameworks with four
LLMs and find that all agents fail substantially. Through trajectory and error analysis, we show that
these failures stem from a lack of physical grounding rather than limitations in code generation. We
find that proprietary agents fail differently from open-source models, requiring different interventions
to improve, and that the failure modes observed in MDG YM are largely absent from general software
engineering benchmarks. MDG YM is designed to serve this role for molecular simulation, and we
hope it provides both a diagnostic for current limitations and a concrete roadmap for the capabilities
that agents must develop to become reliable partners in computational science.
Limitations and future works. MDG YM currently spans two widely used MD engines—L AMMPS
and G ROMACS—but does not cover other established packages such as AMBER, NAMD, or
OpenMM. Extending MDG YM to additional engines is an important direction for future work.
All tasks in MDG YM involve classical molecular dynamics and do not cover ab initio MD, coarse-
grained MD, or enhanced sampling methods such as metadynamics or replica exchange. These
methods impose additional layers of physical reasoning and methodological choice, and represent a
natural extension of the benchmark to harder and more specialized tasks. MDG YM does not include
a human expert performance baseline, making it difficult to precisely quantify the gap between
current agents and domain practitioners. Establishing such a baseline, particularly for medium and
hard tasks, would provide a concrete upper bound and help contextualize agent failure rates. Our
dynamic time budget was designed to give agents approximately three full simulation attempts per
task. However, this design may systematically disadvantage agents with different planning styles.
For e.g., agents that spend more time reasoning before acting may have fewer attempts available for
execution. The sensitivity of results to time budget choices is an important confound that future work
should investigate.


                                                   9
References
Mayar Ahmed, Alex M Maldonado, and Jacob D Durrant. From byte to bench to bedside: molecular
 dynamics simulations and drug discovery. BMC biology, 21(1):299, 2023.
Ben Bogin, Kejuan Yang, Shashank Gupta, Kyle Richardson, Erin Bransom, Peter Clark, Ashish
  Sabharwal, and Tushar Khot. SUPER: evaluating agents on setting up and executing tasks
  from research repositories. In Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen, editors,
  Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing,
  EMNLP 2024, Miami, FL, USA, November 12-16, 2024, pages 12622–12645. Association for
  Computational Linguistics, 2024. doi: 10.18653/V1/2024.EMNLP-MAIN.702. URL https:
  //doi.org/10.18653/v1/2024.emnlp-main.702.
Daniil A. Boiko, Robert MacKnight, Ben Kline, and Gabe Gomes. Autonomous chemical research
  with large language models. Nat., 624(7992):570–578, 2023. doi: 10.1038/S41586-023-06792-0.
  URL https://doi.org/10.1038/s41586-023-06792-0.
Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, and Philippe
  Schwaller. Augmenting large language models with chemistry tools. Nat. Mac. Intell., 6
 (5):525–535, 2024. doi: 10.1038/S42256-024-00832-8. URL https://doi.org/10.1038/
  s42256-024-00832-8.
Quintina L. Campbell, Sam Cox, Jorge Medina, Brittany Watterson, and Andrew D. White. Mdcrow:
  Automating molecular dynamics workflows with large language models. CoRR, abs/2502.09565,
  2025. doi: 10.48550/ARXIV.2502.09565. URL https://doi.org/10.48550/arXiv.2502.
  09565.
Achuth Chandrasekhar and Amir Barati Farimani. Automating MD simulations for proteins using
  large language models: Namd-agent. CoRR, abs/2507.07887, 2025. doi: 10.48550/ARXIV.2507.
  07887. URL https://doi.org/10.48550/arXiv.2507.07887.
Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang, Boshi Wang, Botao Yu, Yifei Li, Zeyi
  Liao, Chen Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N. Baker, Benjamin Burns,
  Daniel Adu-Ampratwum, Xuhui Huang, Xia Ning, Song Gao, Yu Su, and Huan Sun. Sci-
  enceagentbench: Toward rigorous assessment of language agents for data-driven scientific
  discovery. CoRR, abs/2410.05080, 2024. doi: 10.48550/ARXIV.2410.05080. URL https:
  //doi.org/10.48550/arXiv.2410.05080.
Joonmyung Choi. A review of the mechanical design of materials based on molecular dynamics
  simulations. Multiscale Science and Engineering, 5(3):86–103, 2023.
Keyan Ding, Jing Yu, Junjie Huang, Yuchen Yang, Qiang Zhang, and Huajun Chen. Scitoola-
  gent: a knowledge-graph-driven scientific agent for multitool integration. Nat. Comput. Sci., 5
  (10):962–972, 2025. doi: 10.1038/S43588-025-00849-Y. URL https://doi.org/10.1038/
  s43588-025-00849-y.
Titouan Duston, Shuo Xin, Yang Sun, Daoguang Zan, Aoyan Li, Shulin Xin, Kai Shen, Yixiao
  Chen, Qiming Sun, Ge Zhang, Jiashuo Liu, Huan Zhou, Jingkai Liu, Zhichen Pu, Yuanheng Wang,
  Bo-Xuan Ge, Xin Tong, Fei Ye, Zhi-Chao Zhao, Wen-Biao Han, Zhoujian Cao, Yueran Zhao,
  Weiluo Ren, Qingshen Long, Yuxiao Liu, Anni Huang, Yidi Du, Yuanyuan Rong, and Jiahao Peng.
  Ainsteinbench: Benchmarking coding agents on scientific repositories. CoRR, abs/2512.21373,
  2025. doi: 10.48550/ARXIV.2512.21373. URL https://doi.org/10.48550/arXiv.2512.
  21373.
Simon Gravelle, Cecilia M. S. Alvares, Jacob R. Gissinger, and Axel Kohlmeyer. A set of tutorials
  for the LAMMPS simulation package [article v1.0]. Living Journal of Computational Molecular
  Science (LiveCoMS), 6(1):3037, 2025. doi: 10.33011/livecoms.6.1.3037.
Salomé Guilbert, Cassandra Masschelein, Jeremy Goumaz, Bohdan Naida, and Philippe Schwaller.
  Dynamate: An autonomous agent for protein-ligand molecular dynamics simulations. CoRR,
  abs/2512.10034, 2025. doi: 10.48550/ARXIV.2512.10034. URL https://doi.org/10.48550/
  arXiv.2512.10034.


                                               10
Berk Hess, Carsten Kutzner, David Van Der Spoel, and Erik Lindahl. Gromacs 4: algorithms for
  highly efficient, load-balanced, and scalable molecular simulation. Journal of chemical theory and
  computation, 4(3):435–447, 2008.
Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and Karthik
  Narasimhan. Swe-bench: Can language models resolve real-world github issues? CoRR,
  abs/2310.06770, 2023. doi: 10.48550/ARXIV.2310.06770. URL https://doi.org/10.48550/
  arXiv.2310.06770.
Leon Koch, Dominik Baier, Satyendra Rajput, Benedikt König, Michael Tiemann, Simon Ebbinghaus,
  Divya Nayar, and Klaus Huber. Disaggregation at high volume exclusion: An “overcrowding”
  effect. The Journal of Physical Chemistry B, 129(40):10213–10228, 2025. doi: 10.1021/acs.jpcb.
  5c01245. URL https://doi.org/10.1021/acs.jpcb.5c01245. PMID: 41026846.
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph
 Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model
 serving with pagedattention. In Jason Flinn, Margo I. Seltzer, Peter Druschel, Antoine Kaufmann,
 and Jonathan Mace, editors, Proceedings of the 29th Symposium on Operating Systems Principles,
 SOSP 2023, Koblenz, Germany, October 23-26, 2023, pages 611–626. ACM, 2023. doi: 10.1145/
 3600006.3613165. URL https://doi.org/10.1145/3600006.3613165.
Jon M. Laurent, Joseph D. Janizek, Michael Ruzo, Michaela M. Hinks, Michael J. Hammerling,
  Siddharth Narayanan, Manvitha Ponnapati, Andrew D. White, and Samuel G. Rodriques. Lab-
  bench: Measuring capabilities of language models for biology research. CoRR, abs/2407.10362,
  2024. doi: 10.48550/ARXIV.2407.10362. URL https://doi.org/10.48550/arXiv.2407.
  10362.
Justin A. Lemkul. From proteins to perturbed hamiltonians: A suite of tutorials for the gromacs-2018
  molecular simulation package [article v1.0]. Living Journal of Computational Molecular Sci-
  ence, page 5068, Oct. 2018. URL https://livecomsjournal.org/index.php/livecoms/
  article/view/v1i1e5068.
Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. The ai scientist:
  Towards fully automated open-ended scientific discovery. arXiv preprint arXiv:2408.06292, 2024.
Indrajeet Mandal, Jitendra Soni, Mohd Zaki, Morten M. Smedskjaer, Katrin Wondraczek, Lothar
  Wondraczek, Nitya Nand Gosvami, and N. M. Anoop Krishnan. Evaluating large language model
  agents for automation of atomic force microscopy. Nature Communications, 16(1):9104, October
  2025. ISSN 2041-1723. doi: 10.1038/s41467-025-64105-7. URL https://www.nature.com/
  articles/s41467-025-64105-7.
Mike A. Merrill, Alexander Glenn Shaw, Nicholas Carlini, Boxuan Li, Harsh Raj, Ivan Bercovich,
 Lin Shi, Jeong Yeon Shin, Thomas Walshe, Estefany Kelly Buchanan, Junhong Shen, Guanghao
 Ye, Haowei Lin, Jason Poulos, Maoyu Wang, Marianna Nezhurina, Jenia Jitsev, Di Lu, Orfeas
 Menis-Mastromichalakis, Zhiwei Xu, Zizhao Chen, Yue Liu, Robert Zhang, Leon Liangyu Chen,
 Anurag Kashyap, Jan-Lucas Uslu, Jeffrey Li, Jianbo Wu, Minghao Yan, Song Bian, Vedang
 Sharma, Ke Sun, Steven Dillmann, Akshay Anand, Andrew Lanpouthakoun, Bardia Koopah,
 Changran Hu, Etash Kumar Guha, Gabriel H. S. Dreiman, Jiacheng Zhu, Karl Krauth, Li Zhong,
 Niklas Muennighoff, Robert Amanfu, Shangyin Tan, Shreyas Pimpalgaonkar, Tushar Aggarwal,
 Xiangning Lin, Xin Lan, Xuandong Zhao, Yiqing Liang, Yuanli Wang, Zilong Wang, Changzhi
 Zhou, David Heineman, Hange Liu, Harsh Trivedi, John Yang, Junhong Lin, Manish Shetty,
 Michael Yang, Nabil Omi, Negin Raoof, Shanda Li, Terry Yue Zhuo, Wuwei Lin, Yiwei Dai,
 Yuxin Wang, Wenhao Chai, Shang Zhou, Dariush Wahdany, Ziyu She, Jiaming Hu, Zhikang Dong,
 Yuxuan Zhu, Sasha Cui, Ahson Saiyed, Arinbjörn Kolbeinsson, Jesse Hu, Christopher Michael
 Rytting, Ryan Marten, Yixin Wang, Alex Dimakis, Andy Konwinski, and Ludwig Schmidt.
 Terminal-bench: Benchmarking agents on hard, realistic tasks in command line interfaces. CoRR,
 abs/2601.11868, 2026. doi: 10.48550/ARXIV.2601.11868. URL https://doi.org/10.48550/
 arXiv.2601.11868.
Ludovico Mitchener, Jon M Laurent, Alex Andonian, Benjamin Tenmann, Siddharth Narayanan,
  Geemi P Wellawatte, Andrew White, Lorenzo Sani, and Samuel G Rodriques. Bixbench:
  a comprehensive benchmark for llm-based agents in computational biology. arXiv preprint
  arXiv:2503.00096, 2025.


                                                11
OpenAI. gpt-oss-120b & gpt-oss-20b model card, 2025. URL https://arxiv.org/abs/2508.
 10925.

Team Qwen. Qwen3 technical report, 2025. URL https://arxiv.org/abs/2505.09388.

Satyendra Rajput, Roland Pollak, Klaus Huber, Simon Ebbinghaus, and Divya Nayar. Ethylene glycol
  energetically disfavours oligomerization of pseudoisocyanine dyestuffs at crowded concentrations.
  Soft Matter, 19(33):6399–6413, 2023.

Martiño Ríos-García, Nawaf Alampara, Chandan Gupta, Indrajeet Mandal, Sajid Mannan, Ali Asghar
 Aghajani, NM Krishnan, and Kevin Maik Jablonka. Ai scientists produce results without reasoning
 scientifically. arXiv preprint arXiv:2604.18805, 2026.

Zhuofan Shi, Chunxiao Xin, Tong Huo, Yuntao Jiang, Bowen Wu, Xingyue Chen, Wei Qin, Xinjian
  Ma, Gang Huang, Zhenyu Wang, et al. A fine-tuned large language model based molecular
  dynamics agent for code generation to obtain material thermodynamic parameters. Scientific
  Reports, 15(1):10295, 2025.

Zhuofan Shi, Yufei Shao, Mengyan Dai, Yadong Yu, Pan Xiang, Dongliang Huang, Hongxu An,
  Chunxiao Xin, Haiyang Shen, Zhenyu Wang, et al. Mdagent2: Large language model for code
  generation and knowledge q&a in molecular dynamics. arXiv preprint arXiv:2601.02075, 2026.

Siddharth Sinha, Benjamin Tam, and San Ming Wang. Applications of molecular dynamics simulation
  in protein study. Membranes, 12(9):844, 2022.

Yuheng Tang, Kaijie Zhu, Bonan Ruan, Chuqi Zhang, Michael Yang, Hongwei Li, Suyue Guo,
  Tianneng Shi, Zekun Li, Christopher Kruegel, Giovanni Vigna, Dawn Song, William Yang Wang,
  Lun Wang, Yangruibo Ding, Zhenkai Liang, and Wenbo Guo. Devops-gym: Benchmarking AI
  agents in software devops cycle. CoRR, abs/2601.20882, 2026. doi: 10.48550/ARXIV.2601.20882.
  URL https://doi.org/10.48550/arXiv.2601.20882.

Aidan P. Thompson, H. Metin Aktulga, Richard Berger, Dan S. Bolintineanu, W. Michael Brown,
  Paul S. Crozier, Pieter J. in ’t Veld, Axel Kohlmeyer, Stan G. Moore, Trung Dac Nguyen, Ray
  Shan, Mark J. Stevens, Julien Tranchida, Christian Trott, and Steven J. Plimpton. LAMMPS - a
  flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum
  scales. Computer Physics Communications, 271, February 2022. doi: 10.1016/j.cpc.2021.108171.
  URL https://www.sciencedirect.com/science/article/pii/S0010465521002836.

Minyang Tian, Luyu Gao, Shizhuo D Zhang, Xinan Chen, Cunwei Fan, Xuefei Guo, Roland Haas,
 Pan Ji, Kittithat Krongchon, Yao Li, et al. Scicode: A research coding benchmark curated by
 scientists. Advances in Neural Information Processing Systems, 37:30624–30650, 2024.

Hanchen Wang, Tianfan Fu, Yuanqi Du, Wenhao Gao, Kexin Huang, Ziming Liu, Payal Chandak,
  Shengchao Liu, Peter Van Katwyk, Andreea Deac, Anima Anandkumar, Karianne Bergen, Carla P.
  Gomes, Shirley Ho, Pushmeet Kohli, Joan Lasenby, Jure Leskovec, Tie-Yan Liu, Arjun K. Manrai,
  Debora S. Marks, Bharath Ramsundar, Le Song, Jimeng Sun, Jian Tang, Petar Velickovic, Max
 Welling, Linfeng Zhang, Connor W. Coley, Yoshua Bengio, and Marinka Zitnik. Scientific
  discovery in the age of artificial intelligence. Nat., 620(7972):47–60, 2023. doi: 10.1038/
  S41586-023-06221-2. URL https://doi.org/10.1038/s41586-023-06221-2.

Xingyao Wang, Boxuan Li, Yufan Song, Frank F Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan,
  Yueqi Song, Bowen Li, Jaskirat Singh, et al. Openhands: An open platform for ai software
  developers as generalist agents. arXiv preprint arXiv:2407.16741, 2024.

Yanzheng Xiang, Hanqi Yan, Shuyin Ouyang, Lin Gui, and Yulan He. Scireplicate-bench: Bench-
  marking llms in agent-driven algorithmic reproduction from research papers. arXiv preprint
  arXiv:2504.00255, 2025.

Yutaro Yamada, Robert Tjarko Lange, Cong Lu, Shengran Hu, Chris Lu, Jakob Foerster, Jeff Clune,
  and David Ha. The ai scientist-v2: Workshop-level automated scientific discovery via agentic tree
  search. arXiv preprint arXiv:2504.08066, 2025.


                                                12
Fengji Zhang, Linquan Wu, Huiyu Bai, Guancheng Lin, Xiao Li, Xiao Yu, Yue Wang, Bei Chen, and
  Jacky Keung. Humaneval-v: benchmarking high-level visual reasoning with complex diagrams in
  coding tasks. arXiv preprint arXiv:2410.12381, 2024.
Alexander Zhao, Achuth Chandrasekhar, and Amir Barati Farimani. Polyjarvis: Llm agent for
  autonomous polymer md simulations. arXiv preprint arXiv:2604.02537, 2026.




                                             13
A     Molecular Dynamics Simulation
MD simulation numerically integrates Newton’s equations of motion for a system of N interacting
atoms. Given positions {qi } and momenta {pi }, the dynamics follow Hamilton’s equations,

                                         dqi   ∂H                  dpi    ∂H
                                             =     ,                   =−     ,                              (2)
                                          dt   ∂pi                  dt    ∂qi

where H = i p2i /2mi + V ({qi }). The potential energy V is evaluated at every step; its gradient
             P
gives the forces Fi = −∂V /∂qi that drive the dynamics. Integration is almost universally performed
using the velocity Verlet algorithm,

                                                                   pi
              pi ← pi − 12 ∇qi V ∆t,                 qi ← qi +        ∆t,     pi ← pi − 12 ∇qi V ∆t,         (3)
                                                                   mi
which is symplectic and time-reversible, and therefore conserves a shadow Hamiltonian close to
the true one provided ∆t is sufficiently small. In practice, ∆t must resolve the fastest vibrational
mode in the system — O–H and C–H stretches at roughly 3500 cm−1 impose ∆t ≲ 1 fs in atomistic
biomolecular simulations unless bond constraints are applied. A timestep that violates this condition
breaks the symplectic property and causes energy to drift without bound; marginally unstable choices
may not produce obvious divergence but sample incorrect regions of phase space.

A.1   Force Fields

The empirical potential V ({qi }) approximates the true quantum mechanical potential energy surface
as a sum of bonded and non-bonded terms. For molecular systems, the standard decomposition is

                  X                         X                           X X Vn
            V =           kb (r − r0 )2 +            kθ (θ − θ0 )2 +                     [1 + cos(nϕ − δ)]   (4)
                                                                                     2
                  bonds                     angles                     dihedrals n
                            "                         !              #
                                        12    6
                      X                σij   σij             qi qj
                  +             4εij    12 −  6           +            ,                                     (5)
                      i<j
                                       rij   rij            4πε0 rij

where the parameters {kb , r0 , kθ , θ0 , Vn , εij , σij , qi } constitute the force field constants that are
optimised to reproduce target properties either obtained from experiments or from first principle
simulations. For materials systems, simpler pair potentials (Lennard-Jones, Morse) or many-body
potentials (EAM for metals, Tersoff and AIREBO for covalent systems, ReaxFF for reactive chem-
istry) replace the molecular mechanics decomposition. Each force field is parameterized against
a specific class of systems and a specific range of thermodynamic conditions. Applying a force
field outside its parameterization domain, mixing parameters from incompatible force fields, or
neglecting long-range electrostatics when partial charges are significant, all produce forces that bear
no meaningful relationship to the true interatomic interactions. The engine accepts these inputs
without any error and integrates them providing no feedback to the user about the correctness.

A.2   Thermodynamic Ensembles and Equilibration

The basic velocity Verlet integrator samples the NVE ensemble. Most physical measurements require
NVT or NPT conditions, achieved by coupling the system to a thermostat (V-rescale, Nosé-Hoover)
or barostat (Parrinello-Rahman, Berendsen) with associated coupling time constants τT and τP .
These must be matched to the physical relaxation timescales of the system. Aggressive coupling
suppresses the fluctuations that define the ensemble and introduces artifacts in dynamical properties;
weak coupling prevents equilibration within any practical simulation window. Equilibration itself
proceeds in stages: energy minimization via steepest descent to remove steric clashes, followed by
NVT and NPT runs of sufficient length that the relevant observables, such as potential energy, density,
and pressure, have converged to stable mean values. Insufficient equilibration produces trajectories
that are thermodynamically inconsistent with the intended state, without any engine-level indication
that this has occurred.


                                                              14
A.3     Physical Validity Conditions

Beyond integration stability, a physically valid simulation must satisfy several conditions that the
engine does not enforce. System size must be large enough that periodic images do not introduce
spurious correlations; properties sensitive to long-wavelength fluctuations, such as elastic constants,
transport coefficients, interfacial tensions, converge to their thermodynamic limit only when the box
dimension substantially exceeds the relevant correlation length. For non-equilibrium protocols, such
as uniaxial straining for elastic moduli, planar shear for viscosity, imposed thermal gradients for
conductivity, the applied perturbation must lie within the linear response regime; at high loading
or shear rates the measured response is rate-dependent and does not reflect an intrinsic material
property. Post-processing introduces its own requirements: computing a diffusion coefficient from
mean-squared displacement requires identifying the Fickian regime and fitting over an appropriate
time window; extracting a glass transition temperature requires fitting two linear segments to the
density-temperature curve and locating their intersection; computing a viscosity via the Green-Kubo
relation requires integrating a stress autocorrelation function to convergence. The same trajectory
yields different answers depending on how the analysis is performed, and the engine provides no
guidance on which analysis is physically correct.
Collectively, these requirements—timestep stability, force field validity, ensemble consistency, finite-
size convergence, linear response, and methodological precision in post-processing—must be satisfied
simultaneously. None is enforced automatically. A simulation that violates any one of them runs
to completion, produces output of the expected format, and gives no signal that anything is wrong.
This is the regime that separates MD simulation from software engineering tasks, and the regime that
MDG YM is designed to measure.


B     AI Agents for Scientific Workflows

Early systems based on LLMs demonstrated that agents could autonomously plan and execute
chemical synthesis. For instance, ChemCrow [Bran et al., 2024] integrated 18 expert-designed
tools with GPT-4 to automate tasks across organic synthesis, drug discovery, and materials design,
while Coscientist [Boiko et al., 2023] demonstrated autonomous chemical research in a laboratory
setting. More recent systems have extended this vision further along the discovery pipeline: The
AI Scientist [Lu et al., 2024] demonstrated fully automated hypothesis generation, experimentation,
and paper writing, and its successor [Yamada et al., 2025] produced manuscripts accepted at a peer-
reviewed workshop. In the materials domain, SciToolAgent [Ding et al., 2025] automates hundreds
of scientific tools across biology, chemistry, and materials science via a knowledge-graph-driven
retrieval system.


C     MDG YM: Technical Details

C.1     Architecture

Figure C.1 illustrates the three-layer architecture of the MDG YM evaluation harness. The orches-
tration layer acts as the central coordinator, dispatching task prompts to the agent layer (Step 1),
receiving agent outputs (Step 2), and routing them to the validator layer for automated scoring (Step
3). Each layer is governed by a well-defined abstract interface, making it independently extensible.

C.1.1    Agent Layer

All agents implement a common BaseAgent abstract interface that exposes a single
execute(prompt, working_dir, timeout, engine) method. Each concrete implementation
wraps the corresponding CLI tool as a subprocess, streams output to a trajectory_log.jsonl
file in the problem’s working directory, and returns control to the orchestrator upon com-
pletion or timeout. Currently supported agents and their corresponding implementations are:
ClaudeCodeAgent, CodexAgent, OpenHandsAgent. Registering a new agent requires only sub-
classing BaseAgent, implementing the execute method, and adding a single entry to the agent
registry via AgentFactory.register_agent(AgentType.NEW_AGENT, NewAgentClass).


                                                  15
Figure C.1: Architecture of the MDG YM evaluation framework, showing the three independently
extensible layers — agent, orchestration, and validator — and the data flow between them.


C.1.2     Orchestration Layer
The SimulationOrchestrator coordinates a single evaluation episode. Its responsibilities are:

        1. Build the structured task prompt from the problem JSON specification
        2. Invoke the agent via the BaseAgent interface
        3. Read the agent’s final_answer.json output from the working directory
        4. Pass the output and ground truth to the appropriate validator

The orchestrator is constructed via an OrchestratorBuilder that takes an agent type and an engine
type as the only required inputs, resolving the concrete agent and validator implementations internally
via their respective factories. This keeps the top-level evaluation loop entirely decoupled from the
details of any specific agent or engine.

C.1.3     Validator Layer
Each MD engine has a corresponding BaseValidator subclass that implements a
validate(output, working_dir, ground_truth) method and returns a ValidationResult
containing:

         • A binary pass/fail flag


                                                   16
        • A per-metric breakdown of which quantities passed or failed

        • A scalar score in [0, 1] representing the fraction of required metrics within 5% relative
          tolerance of the ground-truth value

Currently registered validators are LAMMPSValidator and GROMACSValidator. Adding sup-
port for a new MD engine requires subclassing BaseValidator and a single registration call:
ValidatorFactory.register_validator(MDEngine.AMBER, AmberValidator.
The validator is free to incorporate engine-specific logic, such as reading auxiliary output files,
applying engine-specific unit conversions, or using tighter tolerances for specific property categories,
without affecting any other part of the framework.


C.1.4    Session Management and Logging

In batch mode, the framework processes all problems in a session sequentially, writing per-problem
results to isolated subdirectories under a session root. Each trajectory log (trajectory_log.jsonl)
records all agent actions, tool calls, and outputs at the granularity of individual steps, and is automati-
cally converted to a structured JSON format after each problem to facilitate offline analysis of agent
reasoning and tool-use patterns. A configurable inter-problem delay mitigates API rate limiting when
evaluating cloud-hosted agents. Session-level results are accumulated in a results.csv summary
file containing per-problem scores, pass/fail flags, and metadata for downstream analysis.


C.2     JSON format

The following presents the format of the JSON file in which the tasks are prepared which is passed as
input during evaluation.


         Field                        Description
         id                           Unique problem identifier
         problem_description          Full natural language description of the simulation task
         level                        1 (Easy) / 2 (Medium) / 3 (Hard)
         engine                       G ROMACS or L AMMPS
         metrics                      List of physical observables to compute
         ground_truth                 Expected values for each metric ± estimated error
         time_limit                   Maximum allowed simulation time in seconds


C.3     L AMMPS vs G ROMACS

L AMMPS and G ROMACS are both molecular dynamics simulation packages, but they target different
scientific communities and use cases. G ROMACS was developed primarily for biomolecular simula-
tions and is highly optimized for proteins, nucleic acids, lipid membranes, and solvated biological
systems using fixed-charge force fields like AMBER, CHARMM, GROMOS, and OPLS. Its strength
lies in raw performance on standard biomolecular workflows, with aggressive SIMD vectorization and
efficient GPU offloading for the kinds of homogeneous systems typical in structural biology and drug
discovery. L AMMPS, by contrast, is a general-purpose particle simulator with a much broader scope:
it supports atomistic, coarse-grained, mesoscale, and granular models, and ships with a wide range of
interatomic potentials including reactive (ReaxFF), bond-order (Tersoff, AIREBO), embedded-atom
(EAM), and machine-learning potentials. This makes it the standard tool for materials science, soft
matter, polymers, solid-state systems, and any problem where the physics extends beyond classical
biomolecular force fields. In short, G ROMACS is the default choice when simulating biology with
established force fields, while L AMMPS is preferred when flexibility across potentials, system types,
or custom physics matters more than peak throughput on a narrow class of systems.


                                                    17
C.4    Example Task Prompt



      Prompt Used in MDGym to Perform an Autonomous Simulation

      Description: Compute the average potential energy per particle for a system
          of polyethylene (hydrocarbon polymer) using the AIREBO potential. Model
          the hydrocarbon polymer using atomic units in the metal unit system and
          an atomic atom style. Construct the system with 60 atoms (20 C and 40 H
          atoms). Replicate the polyethylene structure 17 times along the x
          direction, 16 times along y, and 2 times along z to build a sufficiently
          large bulk system. Construct short range neighbour lists using a binning
          method with a neighbour cutoff of 0.5 Angstrom, updated every timestep
          with a delay of five steps. Model interatomic interactions using the
          AIREBO potential with a Lennard Jones cutoff of 3.0 Angstrom and both
          Lennard Jones and torsional interactions enabled, using appropriate
          carbonhydrogen parameterization. Assign initial velocities corresponding
          to a temperature of 300 K. Evolve the system under constant-energy (NVE)
          dynamics with a timestep of 0.0005 ps, and print thermodynamic
          quantities every 10 steps during a short production run of 1000
          timesteps.

      Required Metrics: average_potential_energy_per_particle

      ============================================================
      IMPORTANT INSTRUCTIONS:
      ============================================================
      0. You have a total time limit of 3450 seconds to solve this problem. Plan
           and execute efficiently within this budget.
      1. Generate all necessary code, scripts, and input files for the simulation
           in LAMMPS and write them to the working directory.
      2. Format code blocks with the filename for automatic extraction:
         ‘‘‘language:filename
         code here...
         ‘‘‘
      3. Example formats for LAMMPS:
         - ‘‘‘lammps:simulation.in
         - ‘‘‘python:run_simulation.py
         - ‘‘‘bash:run_simulation.sh
         Example formats for GROMACS:
         - ‘‘‘gromacs:md.mdp
         - ‘‘‘bash:run_gromacs.sh
      4. The potential name is specified in the problem description. You don’t
           need to download the potential file from the internet; you can access
           the potential file from the path: /MDGym/data/potentials/36_airebo/.
      5. You can access the structure file from the path:
           /MDGym/data/structures/36_airebo/. If the structure file is not present
           in that directory, you can make make your own structure file based on
           the information provided in the problem description.
      6. You don’t need to check the compatibility of the environment or install
           the MD engine; always assume that the environment is pre-configured with
           the necessary software and dependencies to run the simulations. Start
           solving the problem right away as we have a time limit to solve the
           problem.
      7. Run the code and perform any required postprocessing to obtain the final
           answer.
      8. Report the quantities asked in the problem description in JSON format,
           where the key is the name of the quantity and the value is its numerical
           value without units.
      9. Pay careful attention to units. All required units are specified in the
           problem description, and the final answer must use those exact units.



                                            18
      10. Your final response must be ONLY a raw JSON object---no markdown, no
          code fences, no backticks, no explanation, and no preamble. The response
          must start with { and end with }.
      11. Write the final JSON object to final_answer.json for automatic
          extraction.
      12. These are the only instructions. There in no AGENTS.md or such files.




C.5    Dataset details

The input files used for the G ROMACS are taken from multiple sources including original research
papers, repositories associated tutorials or examples for these packages, or created from scratch.
Specifically, 14 files from G ROMACS repository were taken and modified (with different material,
ensemble etc.), 1 file each from Rajput et al. [2023], Koch et al. [2025], 3 files from Lemkul [2018],
and 6 files from Gravelle et al. [2025], and the remaining files are developed by the author. The
simulation workflow in G ROMACS typically follow these steps. First, system is energy minimized
using the steepest-descent algorithm. Second, equilibration is performed under NVT and/or NPT
ensembles. Finally, production runs are carried out in the NPT ensemble. All observables are
computed through post-processing of data obtained from either the equilibration or production runs.
For the L AMMPS tasks, 68 input files are taken from the official L AMMPS repository Thompson et al.
[2022], 7 files from Gravelle et al. [2025], and the remaining files are taken from the Mississippi
State University tutorial webpage. All these were subsequently modified with a different material,
simulation ensemble or other conditions such as loading or deformation. The simulation workflow in
L AMMPS follows a similar protocol unless otherwise specified in the problem description. First, the
system is initialized using the provided input parameters. Second, the force field is defined. Third,
energy minimization is performed, followed by velocity initialization and equilibration. Finally,
production runs are carried out. Unless stated otherwise, all observables are computed by post-
processing the production trajectories.


C.6    Property Categories

MDG YM covers a broad range of physical quantities across six property categories, reflecting the
diversity of scientific questions that MD simulation is used to answer. Table C.1 summarises the
distribution of metrics across categories, and Table C.2 lists the most frequently occurring individual
metrics in the benchmark.
The benchmark is dominated by thermodynamic properties, which appear in the largest number of
problems — average temperature, average density, and average potential energy per particle are
among the most common individual metrics, reflecting their centrality to standard MD workflows.
Structural properties constitute the second-largest category, with coordination number and average
radius of gyration being the most frequent. Mechanical properties constitute the most diverse category
by number of distinct metrics, covering quantities such as Young’s modulus, shear modulus, Poisson
ratio, and vacancy formation energy that reflect the breadth of materials science applications targeted
by L AMMPS tasks. Transport properties (diffusion coefficient, viscosity, thermal conductivity, surface
tension) and magnetic properties are represented by a smaller number of problems, providing coverage
of more specialised simulation workflows. A small set of numerical validation metrics, such as
force relative error and Born matrix relative error, is also included to test whether agents correctly
implement numerical verification procedures.


C.7    MD Simulation Details

Molecular dynamics (MD) simulations were carried out using two widely used MD packages:
GROMACS and LAMMPS. Specifically, GROMACS 2021.4 package and LAMMPS (2 Aug 2023
version) were used to perform the simulations. To enable simulation execution through LLM models,
we provided the initial system structures along with the corresponding topological parameters.


                                                  19
         Table C.1: Distribution of output metrics across property categories in MDG YM.

                   Property Category      Distinct Metrics     Total Occurrences
                   Thermodynamic                  25                   176
                   Structural                     25                    68
                   Mechanical                     30                    41
                   Transport                       6                    6
                   Magnetic                        2                    3
                   Other/Numerical                 7                     9
                   Total                          95                   303

                 Table C.2: Most frequently occurring output metrics in MDG YM.

               Metric                                       Category         Problems
               Average temperature                      Thermodynamic            87
               Average density                          Thermodynamic            37
               Coordination number                         Structural            32
               Average potential energy per particle    Thermodynamic            17
               Average radius of gyration                  Structural            15
               Average total energy per particle        Thermodynamic            12
               Average total energy                     Thermodynamic             9
               Average end-to-end distance                 Structural             7
               Young’s modulus                            Mechanical              7
               Average kinetic energy per particle      Thermodynamic             3


D     Error Analysis Methodology

D.1   Trajectory-Level Error Taxonomy

The trajectory-level error taxonomy was developed through iterative manual inspection of failed
agent trajectories. We began by reviewing a random sample of failed runs across all four agents,
identifying recurring patterns in how agents fail. This process yielded five mutually non-exclusive
error categories — a trajectory may exhibit multiple error types simultaneously. For each category,
we define both the operational definition and the rule used for automated classification.

Fabricated Answer. The agent reports numerical output values in final_answer.json without
having executed the underlying simulation, producing plausible-looking but ungrounded results.
Detection rule: The agent produced an answer but either no simulation output files exist in the agent’s
working directory or the simulation log contains error lines, indicating the reported values were not
derived by executing a simulation.

Syntax Error. The agent produces malformed input scripts that prevent the simulation from execut-
ing.
Detection rule: A failed agent action where the action output contains a syntax-indicating key-
word such as syntax error, unknown command, invalid, illegal, unrecognized, or fatal
error alongside an engine-specific marker such as lmp, .in, gmx, .mdp, or .top.

Environment Misunderstanding. The agent fails to correctly interpret the task setup, available
tools, or the pre-configured simulation environment, leading to actions that are irrelevant or counter-
productive to the task.
Detection rule: A failed action whose output contains command not found.

Premature Termination. The agent abandons the task upon encountering domain-specific error
messages, failing to attempt iterative debugging or recovery.
Detection rule: The agent produced no answer and the run did not exhaust the time budget. Timed-out


                                                  20
runs are excluded, as failing to produce an answer under a binding time constraint is expected
behaviour rather than premature Termination.

Incorrect Post-Processing. The agent executes the simulation but applies an incorrect analysis
procedure to extract the required output metric, producing a wrong final value despite a physically
valid simulation.
Detection rule: The agent produced an answer, and the simulation ran without errors, ruling out
fabrication, but the trajectory still failed.

D.2     Simulation-Level Error Classification

The simulation-level error analysis characterizes the specific errors produced by the MD engines
during failed simulation runs, providing a finer-grained view of where and how simulations break
down. Error categories for each engine were predefined by domain experts based on the known
failure modes of L AMMPS and G ROMACS:

L AMMPS categories Command Syntax, Variable/Expression, Pair/Force Field, Data File and Read,
Fix/Compute Incompatibility, Thermo and Output, Unit and Dimension, Region and Geometry,
Package/Partition, Lost Atoms, Energy Divergence, Neighbor List, Timestep, Script Logic Order,
Boundary Condition, Thermostat/Barostat, MPI/Parallel Decomposition, and Constraint Failure.

G ROMACS categories MDP Parameter, Integrator/Thermostat Incompatibility, Topology, Index
Group, Coord/Topology Mismatch, Position Restraint, LINCS/Constraint, Energy Blow-up, Periodic
Boundary/Box Error, PME/Electrostatics, MPI/GPU Parallelisation, Force Field Param Missing,
Velocity/Temperature Initialisation, Pressure Coupling/Barostat, and Output/File Write.
For each failed simulation run, engine error logs were extracted from the trajectory and provided
to gpt-5.4-2026-03-05 along with the predefined category list and their definitions. To improve
robustness, three independent classifications were generated per error and the majority label was
taken as the final category. The system prompts used for L AMMPS and G ROMACS classification are
provided below.

D.3     LLM Classifier Prompts

D.3.1    L AMMPS Error Classifier Prompt

      LAMMPS Error Classifier System Prompt

      You are a LAMMPS simulation error classifier. You will be given a list of
      numbered error messages extracted from a LAMMPS trajectory. For each error,
      classify it into exactly one category from the taxonomy below.

      === SYNTAX / STATIC ERRORS (S1-S9) ===
      These are detected during input script parsing before any timestep runs.

      --- S1: Command Syntax Error ---
      Definition: A misspelled LAMMPS command name, incorrect number of arguments,
      arguments in the wrong order, or use of a keyword that does not exist in the
      installed build. Detected during input script parsing before any timestep
      runs.
      Trigger: Parser fails to recognise the command token or cannot match the
      argument list to any known signature for that command.
      Signals: ’Unknown command’, ’Illegal command’, or ’Expected N arguments’;
      error line references the exact input script line; error occurs before
      timestep 0.
      Classification rule: Classify as S1 if ALL criteria hold: (1) LAMMPS reports
      ’Unknown command’, ’Illegal command’, ’Expected N arguments’, or
      ’Unrecognized keyword’; (2) the error is raised during input script parsing
      before the run starts; (3) the message cites a specific script line.



                                                21
Examples: pair_style lj/cut 2.5 extra_arg # too many args; atom_sytle atomic
# typo in command name

--- S2: Variable & Expression Error ---
Definition: Use of an undefined variable, an invalid mathematical expression
inside a variable definition, or the wrong variable style for a context.
Trigger: LAMMPS tries to evaluate a variable or expression and cannot
resolve the reference or parse the math.
Signals: ’Variable ... is not defined’; ’Invalid math expression’; ’Variable
... has wrong style’.
Classification rule: Classify as S2 if ALL criteria hold: (1) the message
contains ’variable’, ’undefined variable’, ’invalid expression’, or ’wrong
style’; (2) the failure occurs during variable evaluation or preprocessing;
(3) no atom positions or forces are involved.

--- S3: Pair / Force Field Error ---
Definition: Mismatch between pair_style and pair_coeff declarations: missing
coefficients for one or more atom-type pairs, wrong number of parameters,
inconsistent mixing rules, or use of a pair style not compiled into the
LAMMPS binary.
Signals: ’No pair style is defined’; ’Pair coeffs are not set’; ’Incorrect
args for pair_coeff’.
Classification rule: Classify as S3 if ALL criteria hold: (1) the message
references ’pair_style’, ’pair_coeff’, ’pair coeffs’, or ’mixing’; (2) the
error appears before or at the start of the run; (3) it does not reference
lost atoms or energy divergence.

--- S4: Data File & Read Error ---
Definition: Malformed LAMMPS data file: atom count in the header does not
match the Atoms section, a required section is absent, atom type indices are
out of range, or the file format does not match the declared atom_style.
Signals: ’Did not assign all atoms correctly’; ’Unexpected end of data
file’; ’Too many/few lines in ... section’; ’Invalid atom type’.
Classification rule: Classify as S4 if ALL criteria hold: (1) the error is
raised inside or immediately after read_data; (2) it references atom counts,
sections, or file structure; (3) it does not reference pair coefficients or
force constants.

--- S5: Fix / Compute Incompatibility ---
Definition: A fix or compute applied to a group that does not exist,
references a compute/fix ID not yet defined, or has invalid arguments.
Signals: ’Group ID does not exist’; ’Fix requires ... atom style’; ’Compute
ID ... does not exist’.
Classification rule: Classify as S5 if ALL criteria hold: (1) the message
names a fix or compute ID; (2) it references a missing group, missing
dependency, or incompatible atom style; (3) the error is raised before the
first timestep.

--- S6: Thermo & Output Error ---
Definition: Error in thermo_style, dump, or restart configuration:
referencing a compute or fix keyword not defined, or mismatching dump format
arguments.
Signals: ’Unknown keyword in thermo_style’; ’Invalid keyword in dump ...
command’.
Classification rule: Classify as S6 if ALL criteria hold: (1) the message
involves thermo_style, dump, or restart; (2) it references an unrecognised
or undefined keyword/ID; (3) it is not a runtime energy or force error.

--- S7: Unit & Dimension Error ---
Definition: Commands that depend on a unit system issued before the units
command is set, or 2D-specific commands used without declaring dimension 2.
Signals: ’Cannot use ... before units are set’; ’Must use dimension 2 before
...’.



                                     22
Classification rule: Classify as S7 if ALL criteria hold: (1) the message
references ’units’, ’dimension’, or a unit-dependent quantity; (2) the error
appears before the run starts; (3) it does not concern atom types or pair
coefficients.

--- S8: Region & Geometry Error ---
Definition: Wrong keyword for a region shape type, incorrect number of
geometric parameters, invalid simulation box dimensions, or create_atoms
referencing an undefined region.
Signals: ’Illegal region command’; ’Invalid region ID’; ’Box bounds are
invalid’.
Classification rule: Classify as S8 if ALL criteria hold: (1) the message
references ’region’, ’box’, or ’create_atoms’; (2) the error involves
geometric parameters or undefined region IDs; (3) it occurs before the run.

--- S9: Package / Partition Error ---
Definition: Requesting a GPU, KOKKOS, INTEL, or OMP accelerated style not
compiled into the LAMMPS binary, or supplying invalid arguments to the
package command.
Signals: ’Package gpu is not available’; ’Unrecognized package name’; style
suffix /gpu or /kk present but build lacks that suffix.
Classification rule: Classify as S9 if ALL criteria hold: (1) the message
references ’package’, a style suffix (/gpu, /kk, /intel, /omp), or
’partition’; (2) it states the feature is unavailable or the command is
illegal; (3) it occurs at startup before setup.

=== RUNTIME / LOGICAL ERRORS (R1-R9) ===
These occur during a run at timestep > 0.

--- R1: Lost Atoms Error ---
Signals: ’Lost atoms: ...’ during the run; ’Atoms lost in xxx timesteps’.
Classification rule: Classify as R1 if ALL criteria hold: (1) the message
contains ’lost atoms’ or ’atoms lost’; (2) the error is raised during a run
(timestep > 0); (3) a count of lost atoms or a timestep number is reported.

--- R2: Energy Divergence Error ---
Signals: Energy printed as NaN or Inf in thermo output; ’Numerical
instability’ warning.
Classification rule: Classify as R2 if ALL criteria hold: (1) thermo output
shows NaN, Inf, or astronomically large energy values; (2) the error occurs
during a run (timestep > 0); (3) no ’lost atoms’ message appears before the
NaN.

--- R3: Neighbor List Error ---
Signals: ’Dangerous builds’ counted in output; ’Neighbor list overflow’.
Classification rule: Classify as R3 if ALL criteria hold: (1) the message
references ’neighbor’, ’neigh’, ’skin’, or ’dangerous builds’; (2) it
appears during setup or at a rebuild step; (3) it does not report lost atoms.

--- R4: Timestep Error ---
Signals: Energy divergence or lost atoms within the first ~50 steps;
extremely high temperature in the first few steps.
Classification rule: Classify as R4 if ALL criteria hold: (1) the
instability begins within the first ~50 steps; (2) decreasing the timestep
resolves the issue; (3) there is no obvious initial geometry overlap.

--- R5: Ordering / Script Logic Error ---
Signals: ’Pair style not yet defined’; ’Must define atom_style before
read_data’.
Classification rule: Classify as R5 if ALL criteria hold: (1) the message
says a required precondition has not been set; (2) re-ordering the commands
would fix the error; (3) no atom positions or forces are involved.




                                     23
   --- R6: Boundary Condition Error ---
   Signals: ’Pair style requires periodic boundary in all dimensions’; lost
   atoms attributed to non-periodic boundary.
   Classification rule: Classify as R6 if ALL criteria hold: (1) the message
   references ’boundary’, ’periodic’, ’shrink-wrap’, or ’fixed wall’; (2) the
   pair style or ensemble conflicts with the boundary setting; (3) the error
   does not arise from atom geometry or overlaps.

   --- R7: Thermostat / Barostat Error ---
   Signals: ’Fix npt requires ...’; pressure or temperature oscillating wildly.
   Classification rule: Classify as R7 if ALL criteria hold: (1) the message
   references a thermostat or barostat fix; (2) the error involves incompatible
   settings or T/P instability; (3) it is not a lost-atom or energy-divergence
   error.

   --- R8: MPI / Parallel Decomposition Error ---
   Signals: ’Too many processors for simulation’; ’Processor grid does not
   match domain’.
   Classification rule: Classify as R8 if ALL criteria hold: (1) the message
   references ’processors’, ’MPI’, ’domain’, or ’ranks’; (2) the error is
   triggered by the number of MPI processes or processor grid; (3) it does not
   involve pair coefficients or atom types.

   --- R9: Constraint Failure ---
   Signals: ’SHAKE atoms missing’; ’RATTLE failed to converge’; ’Linear
   constraint solver did not converge’.
   Classification rule: Classify as R9 if ALL criteria hold: (1) the message
   contains ’SHAKE’, ’RATTLE’, ’LINCS’, or ’constraint’; (2) it references
   convergence failure or missing atoms; (3) it is a runtime error (timestep >
   0).

   === INSTRUCTIONS ===
   For each numbered error below, return exactly one category ID from: S1 S2 S3
   S4 S5 S6 S7 S8 S9 R1 R2 R3 R4 R5 R6 R7 R8 R9 or "Unclassified".

   Respond with a valid JSON object only - no markdown, no explanation:
   {
     "classifications": [
       {"index": 1, "category_id": "S3", "category_name": "Pair / Force Field
       Error", "category_type": "Syntax"},
       ...
     ]
   }



D.3.2   G ROMACS Error Classifier Prompt

   GROMACS Error Classifier System Prompt

   You are a GROMACS simulation error classifier. You will be given a list of
   numbered error messages extracted from a GROMACS trajectory. For each error,
   classify it into exactly one category from the taxonomy below.

   === PREPROCESSING / STATIC ERRORS (P1-P6) ===
   These are detected by grompp before the simulation starts.

   --- P1: MDP Parameter Error ---
   Definition: An unrecognised, misspelled, or deprecated parameter key in the
   .mdp run-input file, or a value out of the allowed range.
   Signals: Warning: Unknown left-hand ’xyz’ in parameter file; Fatal error:
   Invalid value for mdp option.



                                            24
Classification rule: Classify as P1 if ALL criteria hold: (1) the message
references an .mdp file option by name; (2) it says the option is ’unknown’,
’invalid’, ’deprecated’, or out of range; (3) the error is raised by grompp
before the simulation starts.

--- P2: Integrator / Thermostat Incompatibility ---
Definition: An incompatible combination of integrator and thermostat or
barostat in the .mdp file.
Signals: Fatal error: Integrator ... is not compatible with tcoupl ...;
Fatal error: Cannot use ... with integrator ...
Classification rule: Classify as P2 if ALL criteria hold: (1) the message
names both an integrator and a thermostat or barostat; (2) it says they are
incompatible; (3) the error is raised by grompp.

--- P3: Topology Error ---
Definition: An error in the .top or .itp topology file: broken #include
chain, mismatched moleculetype declarations, wrong atom count, undefined
atom types, or missing force field files.
Signals: Fatal error: No such file or directory (for included .itp); Fatal
error: number of atoms in ... does not match.
Classification rule: Classify as P3 if ALL criteria hold: (1) the message
references a .top or .itp file; (2) it reports a missing include, undefined
atom type, or atom count mismatch; (3) it is raised by grompp.

--- P4: Index Group Error ---
Definition: A group name referenced in the .mdp file does not exist in the
.ndx index file, or the index file is malformed or missing.
Signals: Fatal error: Group ... not found in index file; Error reading index
file.
Classification rule: Classify as P4 if ALL criteria hold: (1) the message
references a group name or index file; (2) it says the group is ’not found’
or the index file is invalid/missing; (3) it is raised by grompp.

--- P5: Coordinate / Topology Mismatch ---
Definition: The number or order of atoms in the coordinate file does not
match what the topology expects.
Signals: Fatal error: number of coordinates in ... does not match topology;
Fatal error: Atom ... not found in residue.
Classification rule: Classify as P5 if ALL criteria hold: (1) the message
compares a coordinate file to the topology; (2) it reports a count or naming
mismatch; (3) it is raised by grompp.

--- P6: Position Restraint Error ---
Definition: The position restraint file does not match the current topology:
wrong number of restrained atoms, mismatched atom indices, or the posre.itp
#include is missing.
Signals: Fatal error: Position restraint file ... has ... entries, expected
...; Fatal error: Atom index ... in position restraints is out of range.
Classification rule: Classify as P6 if ALL criteria hold: (1) the message
references a position restraint file or the posres directive; (2) it reports
a count or index mismatch; (3) it is raised by grompp.

=== RUNTIME / LOGICAL ERRORS (R1-R9) ===
These occur during mdrun at step >= 0.

--- R1: LINCS / Constraint Failure ---
Signals: LINCS WARNING: ... constraints not satisfied; Fatal error: Too many
LINCS warnings.
Classification rule: Classify as R1 if ALL criteria hold: (1) the message
contains ’LINCS’, ’SETTLE’, or ’constraint’; (2) it references
non-convergence or deviation during the run; (3) it occurs at a specific
timestep (step > 0).




                                     25
--- R2: Energy Blow-up / Numerical Instability ---
Signals: Fatal error: Nan or Inf in coordinates or velocities; Step ...: NAN
detected in ...
Classification rule: Classify as R2 if ALL criteria hold: (1) the message
contains ’NaN’, ’Inf’, ’blow-up’, or ’not converging’; (2) it is raised
during an mdrun step (step > 0); (3) no LINCS warning appears before it.

--- R3: Periodic Boundary / Box Error ---
Signals: Fatal error: The box is too small for the largest cut-off; Fatal
error: Atom ... is outside the box.
Classification rule: Classify as R3 if ALL criteria hold: (1) the message
references the simulation box, cutoff, or PBC; (2) it reports atoms outside
the box or box too small; (3) it is a runtime error (step >= 0).

--- R4: PME / Electrostatics Error ---
Signals: Fatal error: The PME grid ... is not compatible with ...; Fatal
error: Cannot use PME with non-periodic boundary.
Classification rule: Classify as R4 if ALL criteria hold: (1) the message
references ’PME’, ’Ewald’, ’grid’, or ’electrostatics’; (2) it reports an
incompatibility or initialisation failure; (3) it does not reference LINCS
or NaN.

--- R5: MPI / GPU Parallelisation Error ---
Signals: Fatal error: Too few ranks ... for domain decomposition; Fatal
error: Cannot use GPU with ...
Classification rule: Classify as R5 if ALL criteria hold: (1) the message
references ’ranks’, ’domain decomposition’, ’GPU’, or ’MPI’; (2) it reports
an incompatibility or setup failure; (3) it occurs at initialisation (before
step 1).

--- R6: Force Field Parameter Missing ---
Signals: Fatal error: No parameters for ... in ...; Fatal error: No default
... parameters.
Classification rule: Classify as R6 if ALL criteria hold: (1) the message
says ’no parameters’, ’no default’, or ’not found’ for a bonded or
non-bonded interaction; (2) it is raised during mdrun (step >= 0); (3) it is
not a topology #include or atom-count error.

--- R7: Velocity / Temperature Initialisation Error ---
Signals: Fatal error: gen-temp must be > 0; WARNING: Velocities were not
generated.
Classification rule: Classify as R7 if ALL criteria hold: (1) the message
references ’gen-vel’, ’gen-temp’, ’velocities’, or temperature
initialisation; (2) it reports an invalid temperature or velocity
incompatibility; (3) it occurs at startup (step 0 or grompp).

--- R8: Pressure Coupling / Barostat Error ---
Signals: WARNING: Step ..., time ...: the box is growing/shrinking rapidly;
Fatal error: Box has collapsed.
Classification rule: Classify as R8 if ALL criteria hold: (1) the message
references ’pressure coupling’, ’barostat’, ’box vectors’, or
’compressibility’; (2) it reports rapid box change, collapse, or
incompatibility; (3) it is a runtime error (step > 0).

--- R9: Output / File Write Error ---
Signals: Fatal error: Cannot write to file ...; Fatal error: Incompatible
checkpoint file.
Classification rule: Classify as R9 if ALL criteria hold: (1) the message
references a file path or file type (.trr, .xtc, .edr, .cpt); (2) it says
the file cannot be written, is corrupt, or is incompatible; (3) it is raised
during mdrun output.

=== INSTRUCTIONS ===



                                     26
For each numbered error below, return exactly one category ID from: P1 P2 P3
P4 P5 P6 R1 R2 R3 R4 R5 R6 R7 R8 R9 or "Unclassified".

Respond with a valid JSON object only - no markdown, no explanation:
{
  "classifications": [
    {"index": 1, "category_id": "P3", "category_name": "Topology Error",
    "category_type": "Preprocessing"},
    ...
  ]
}




Simulation Stage Completion Classifier System Prompt

You are an expert computational materials scientist and an automated
diagnostic engine for molecular dynamics (MD) simulations.

Your task is to analyze the provided simulation log file (which may be from
LAMMPS, GROMACS, or similar engines) and determine the exact stage at which
the simulation ended, whether it completed successfully, or if it failed,
what type of error caused the failure.

### The 4 Stages of MD Simulation (Strict Definitions)
Use the following explicit criteria to classify the progress of the
simulation. Do not guess; rely on these strict physical and textual
signatures:

1. INITIALIZATION (System Setup)
- Definition: The engine is translating inputs into a mathematical state
prior to any particle displacement. Time is strictly at t=0. This includes
parsing topology, applying forcefield parameters (charges, LJ parameters),
building initial neighbor lists, and allocating memory.
- Success Signatures: The log explicitly prints the simulation box
dimensions, total number of atoms/interactions, and successfully evaluates
step 0 (or pre-run) energies without throwing "NaN" (Not a Number) or
infinite force errors.
- Exclusion: If the engine crashes before building the neighbor list or
printing step 0 thermals, Initialization has FAILED.

2. ENERGY MINIMIZATION (Static Relaxation)
- Definition: A purely mathematical optimization to find a local potential
energy minimum and resolve steric clashes. There is no concept of time,
temperature, or kinetic energy in this stage. Algorithms used are typically
Steepest Descent (SD) or Conjugate Gradient (CG).
- Success Signatures: The log explicitly reports "Minimization converged",
the maximum force (F_max) drops below the target tolerance (e.g., ftol), or
the maximum requested iterations are safely reached.
- Exclusion: If atoms move "too far" or forces become infinite here, it is a
Minimization failure.

3. THERMODYNAMIC EQUILIBRATION (NVT / NPT)
- Definition: Time-integration begins (Newton’s equations are solved), but
the primary goal is coupling the system to a heat bath (thermostat) or
pressure bath (barostat) to reach a target macrostate. Trajectory data here
is considered "burn-in" and not meant for final analysis.
- Success Signatures: Completion of the specified NVT/NPT ‘run‘ segments.
The log must show rolling averages of Temperature, Pressure, and Density
oscillating steadily around their target values (e.g., T ~ 300K) with no
exponential drift or sudden spikes.



                                         27
      - Exclusion: If a ‘run‘ command finishes, but the final temperature is
      thousands of degrees away from the target, Equilibration has FAILED due to
      physical blow-up, even if the engine didn’t explicitly crash.

      4. PRODUCTION RUN (Data Acquisition)
      - Definition: The final, stable integration phase where the thermodynamic
      ensemble is maintained, and coordinates/velocities are actively dumped to
      trajectory files for scientific analysis.
      - Success Signatures: The final ‘run‘ command completes entirely. The log
      prints the ultimate timing summary (e.g., "Total wall time", "Performance:
      ns/day", "Loop time of X on Y procs"), signaling a clean exit of the
      simulation loop.
      - Exclusion: Any crash, lost atom, or constraint failure occurring after
      equilibration completes is a Production failure.

      ### Task Instructions
      1. Scan the log file sequentially from top to bottom.
      2. Identify the highest stage that completed successfully. If a stage
      started but crashed before finishing, the *previous* completed stage is the
      last successful one. If it crashes during Initialization, the last
      successful stage is "None".
      3. If the simulation crashed, classify the failure using one of these
      categories: [Syntax/Parsing, Topology/Parameterization, Step-Zero
      Instability, Integration/Dynamics Instability, Hardware/Parallelization].
      4. Extract the specific error message or the line right before the failure.

      ### Output Format
      You must output your analysis as a valid JSON object using the exact schema
      below. Do not include any markdown formatting or conversational text outside
      of the JSON block.

      {
          "last_successful_stage": "None" | "Initialization" | "Minimization" |
          "Equilibration" | "Production",
          "error_category": "String (from the categories listed above, or null if
          Success)",
          "error_evidence": "String (the exact error message or last printed line
          indicating the crash, or null if Success)",
          "reasoning": "A brief, 1-2 sentence explanation justifying the
          classification."
      }




D.4       Agent Behavior Modes


During manual inspection of agent trajectories, we observed recurring behavioral patterns across
agents. We document these here as qualitative observations to complement the automated error
analysis.
Plan Then Execute. The agent produces substantial reasoning about the problem — identifying
required parameters, decomposing sub-tasks, and anticipating potential pitfalls before writing any
simulation files.
Exploratory Probing. The agent begins by exploring the environment, for example, listing files,
checking directory contents, reading existing structure or potential files, before writing any simulation
code.
Code Generation. The agent generates a simulation input script, either writes the first file immedi-
ately after reading the problem or produces all required files in a single batch before executing any of
them.


                                                   28
Iterative Refinement. The agent writes a simulation file, executes it, encounters an error, edits the
file, and retries — repeating this write-run-debug cycle. The same core approach is preserved and
incrementally corrected rather than abandoned.
Trial and Error. The agent makes multiple substantially different attempts to solve the problem,
abandoning one approach for another when it fails. Distinguished from Iterative Refinement by the
scope of change between attempts: the agent rewrites the simulation strategy rather than patching a
specific error.
Verification. The agent explicitly checks whether its simulation output is correct before submitting
a final answer, including parsing output logs to extract specific metric values, cross-referencing
computed results against expected physical ranges, and performing unit conversions on extracted
values.

E     Performance of Agents on Different Simulation Packages




Figure E.2: Performance of all agents on L AMMPS tasks in MDG YM. (a) Full-success rate (%) by
difficulty level. (b) Total partial-credit score by difficulty level. Claude Code leads slightly on easy
tasks (20%) with Codex at 24%; both drop sharply at higher difficulties. Qwen [OH] and GPT-OSS
[OH] achieve 0% across all difficulty levels.




Figure E.3: Performance of all agents on G ROMACS tasks in MDG YM. (a) Full-success rate (%)
by difficulty level, where a problem is counted as a success only if all required metrics are within
tolerance. (b) Total partial-credit score by difficulty level. Claude Code and Codex lead on easy tasks
(20% and 24% respectively), with both collapsing to near-zero on medium and hard tasks. Qwen
[OH] and GPT-OSS [OH] score 0% at all difficulty levels.


F     Statistical Significance of Results
F.1   Tests and Methodology

We conduct three complementary statistical analyses on the per-problem partial credit scores (s ∈
[0, 1]) and binary success rates reported in Section 5. All tests operate on per-problem scores and
are computed using scipy and statsmodels. Raw scores are released alongside the benchmark to
allow independent verification.

Claim 1: Performance degrades monotonically with difficulty. We apply the Kruskal-Wallis test
and Spearman rank correlation between difficulty level (coded ordinally as 1, 2, 3) and per-problem


                                                  29
partial credit score. The Kruskal-Wallis test is the non-parametric equivalent of one-way ANOVA
and makes no normality assumption, appropriate here given the heavy zero-inflation of scores. The
Spearman correlation additionally provides direction and magnitude for the monotonic trend. For
Claude Code (H = 11.28, p = 0.004; ρ = −0.250, p = 0.001) and Codex (H = 12.69, p = 0.002;
ρ = −0.272, p < 0.001), performance degradation across difficulty levels is statistically significant.
Combined across all agents, H = 23.97 and ρ = −0.185 (both p < 0.001). Open-source models via
OpenHands show no significant trend, not because degradation is absent, but due to a floor effect:
scores are already near zero on easy tasks, leaving no statistical power to detect further degradation.

Claim 2: Proprietary agents significantly outperform open-source agents. We apply the Mann-
Whitney U test comparing per-problem scores of proprietary agents (Claude Code, Codex) against
open-source agents (Qwen [OH], GPT-OSS [OH]). The Mann-Whitney test assesses whether scores
from one group tend to be higher than the other on a problem-by-problem basis, without assuming
normality. The difference is highly significant overall (p < 0.001) and at every difficulty level
(Easy p < 0.001, Medium p < 0.001, Hard p = 0.012), with mean scores of 0.121 vs 0.006 for
proprietary and open-source agents respectively. To assess robustness to task selection, we performed
bootstrap resampling with 10,000 resamples of the 169 tasks with replacement, finding the proprietary
advantage was positive in 100% of resamples overall, and in 100%, 100%, and 98.4% of resamples at
easy, medium, and hard difficulty levels respectively. The slight uncertainty at hard difficulty reflects
near-zero scores for all agents rather than genuine ambiguity about the ranking.

Claim 3: The benchmark is genuinely hard. We report Wilson score 95% confidence intervals on
the binary success rates for each agent and difficulty level, shown in Table F.3. The Wilson method
is preferred over the naive Wald interval for small samples and extreme proportions. The upper
confidence bound for the best-performing agents on easy tasks is 33.3%, falling to 11.9% on hard
tasks. All agents at medium and hard difficulty have upper confidence bounds below 18%, confirming
that the observed low success rates are not artefacts of small sample size.

     Table F.3: Wilson 95% confidence intervals on success rates per agent and difficulty level.

            Agent               Difficulty   Successes     Success Rate         95% CI
            Claude Code         Easy            12/57          21.1%         12.5%–33.3%
                                Medium           4/55           7.3%          2.9%–17.3%
                                Hard             2/57           3.5%          1.0%–11.9%
            Codex               Easy            12/57          21.1%         12.5%–33.3%
                                Medium           2/55           3.6%          1.0%–12.3%
                                Hard             2/57           3.5%          1.0%–11.9%
            Qwen [OH]           Easy            1/57            1.8%          0.3%–9.3%
                                Medium          0/55            0.0%          0.0%–6.5%
                                Hard            0/57            0.0%          0.0%–6.3%
            GPT-OSS [OH]        Easy            0/57            0.0%          0.0%–6.3%
                                Medium          0/55            0.0%          0.0%–6.5%
                                Hard            0/57            0.0%          0.0%–6.3%




                                                   30
