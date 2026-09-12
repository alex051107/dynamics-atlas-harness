# NAMD-Agent: Automating MD simulations for Proteins using Large Language Models

**Authors:** Chandrasekhar, Achuth; Barati Farimani, Amir
**Year:** 2025
**Venue:** arXiv preprint
**arXiv:** 2507.07887
**Source PDF URL:** https://arxiv.org/pdf/2507.07887
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---
Automating MD simulations for Proteins using Large language
Models: NAMD-Agent
Achuth Chandrasekhara , Amir Barati Farimanib,c,d,e,∗

a

Materials Science and Engineering, Carnegie Mellon University, Pittsburgh, 15213, PA, USA
b
Mechanical Engineering, Carnegie Mellon University, Pittsburgh, 15213, PA, USA
c
Biomedical Engineering, Carnegie Mellon University, Pittsburgh, 15213, PA, USA
d
Chemical Engineering, Carnegie Mellon University, Pittsburgh, 15213, PA, USA
e
Machine Learning Department, Carnegie Mellon University, Pittsburgh, 15213, PA, USA

Abstract
Molecular dynamics simulations are an essential tool in understanding protein structure, dynamics, and function at the atomic level. However, preparing high-quality input files for
MD simulations can be a time-consuming and error-prone process. In this work, we introduce an automated pipeline that leverages Large Language Models (LLMs), specifically
Gemini-2.0-Flash, in conjunction with python scripting and Selenium-based web automation to streamline the generation of MD input files. The pipeline exploits CHARMM-GUI’s
comprehensive web-based interface for preparing simulation-ready inputs for NAMD. By integrating Gemini’s code generation and iterative refinement capabilities, simulation scripts
are automatically written, executed, and revised to navigate CHARMM-GUI, extract appropriate parameters, and produce the required NAMD input files. Post-processing is performed
using additional software to further refine the simulation outputs, thereby enabling a complete and largely hands-free workflow. Our results demonstrate that this approach reduces
setup time, minimizes manual errors, and offers a scalable solution for handling multiple protein systems in parallel. This automated framework paves the way for broader application
of LLMs in computational structural biology, offering a robust and adaptable platform for
future developments in simulation automation.

∗

Corresponding author
Email address: barati@cmu.edu (Amir Barati Farimani)

July 11, 2025

1. Introduction
LLMs are an engineering milestone that burst onto the scene in November 2022 with the
announcement of ChatGPT. Their development was inspired by the paper, "Attention Is All
You Need" , published by a team of researchers at Google in 2017 [1]. With vast amounts
of training data at their disposal LLMs are able to generate coherent text as well as perform
agentic tasks at near-human levels of efficiency. [2], [3], [4], [5], [6].
CHARMM-GUI[7] is a web interface designed to simplify the setup of biomolecular simulations by offering a suite of user-friendly builders and tools. These builders guide users through
critical preparatory steps, such as structural refinement, parameter selection, membrane construction, glycan modeling, and ion placement. By automating much of the setup process for
popular MD engines (CHARMM, NAMD, AMBER, and GROMACS)[8], CHARMM-GUI
lowers the barrier to entry for molecular dynamics simulations, reduces human error, and
ensures consistency in system construction. Its step-by-step workflow not only simplifies the
preparation of complex systems like membrane proteins or multi-component assemblies but
also provides detailed documentation that researchers can reference for reproducibility and
methodological rigor.
In this work, we have developed a system that utilises the selenium python web automation library [9] that automates the preparation of input files through CHARMM-GUI for
molecular dynamics simulations and the subsequent execution and post-processing of the
output data. LLMs are used in an agentic AI framework [10, 11, 12, 13, 14] to accept the
human user’s directions as a textual query as well as handling the CHARMM-GUI website
and NAMD3 software using python code.
In this work we have contributed the following to practical AI implementations for computational biology:
1. Giving LLMs freedom to organize and run code.
2. Automating a web user interface that is originally designed for a high degree of automation.

3. An end-to-end pipeline for molecular dynamics simulation utilizing web automation
and LLMs
2. Related Works
2.1. Automated GROMACS-based MD simulations
Automating molecular dynamics (MD) simulation workflows has been a focus of many
recent tools and frameworks. Setting up and running MD for biomolecular systems is a
complex, multi-step process that traditionally demands significant time and expertise. To
alleviate these challenges, a variety of automation tools have been developed to streamline
simulation setup, execution, and analysis. For example, CHAPERONg was introduced as
an automated pipeline for GROMACS MD simulations of proteins and protein–ligand complexes [15]. CHAPERONg integrates with GROMACS modules and third-party programs to
perform up to 20 post-simulation analysis tasks, covering everything from trajectory processing to free energy landscape calculations, thereby making MD workflows more accessible to
non-experts while freeing experienced users to focus on interpreting results. In a similar vein,
Gmx_qk [16] provides a bash-based workflow (with a simple graphical interface via Zenity)
that enables users with minimal command-line experience to run protein or protein–ligand
simulations in GROMACS, automatically carrying out energy minimization, equilibration,
production runs, and even binding free energy analysis (MM/PBSA) with minimal user intervention. Such tools significantly reduce the manual effort and potential for error in MD
setup – for instance, Gmx_qk can launch a complete simulation sequence within seconds of
providing input files and basic parameters, a process that would otherwise take tens of minutes to configure by hand. The agentic system introduced in this work is designed to leverage
CHARMM-GUI to dynamically generate parameter and input files, rather than relying on
pre-existing ones.

2.2. easyAmber and Admiral
Automation frameworks have also been developed for other MD platforms. easyAmber is
one example targeting the Amber simulation suite, providing a collection of wrapper scripts to
fully automate protein MD protocols [17]. The easyAmber toolkit handles system setup, force
field assignment, equilibration, and both classical and accelerated MD simulations in Amber,
all through highly automated workflows. By encapsulating advanced but routine procedures,
easyAmber lowers the barrier for Amber users and promotes adoption of MD techniques in
everyday research. Beyond general-purpose pipelines, some tools cater to specialized MD
tasks. Admiral (Automated Docking and Molecular Dynamics Informatics and Analysis) is
a platform that automates not only MD simulations but also upstream docking and downstream reporting in a drug discovery context [18]. Developed at a pharmaceutical company,
Admiral can take a proposed compound, perform docking and MD on the protein–ligand
system, then analyze the trajectory and other properties to automatically generate a comprehensive report (including simulation metrics, predicted ADME properties, and even an
animated visualization) for medicinal chemists. Likewise, focusing on free energy calculations, PyAutoFEP automates the setup and execution of alchemical free energy perturbation
simulations in GROMACS [19]. This open-source tool generates the required perturbation
maps and dual-topology inputs, builds the simulation systems, runs enhanced-sampling MD,
and processes the results, thus streamlining what would otherwise be a labor-intensive series
of steps in binding affinity estimation. These examples illustrate the breadth of automation
efforts in MD: from general workflow management to GUI-assisted pipelines and task-specific
tools, the goal is to reduce human effort in simulation preparation and analysis across different
MD engines.
2.3. Large Language Models for MD Simulations
Recent advances in artificial intelligence suggest that large language models (LLMs) can
further enhance automation in MD simulations. Traditional MD automation tools are typically rule-based and limited to predefined protocols, whereas LLMs can interpret flexible user

instructions and make context-dependent decisions. For instance, Campbell et al. introduced
MDCrow, an LLM-driven assistant that uses a chain-of-thought approach with a suite of specialized tools to autonomously carry out MD simulation tasks [20]. Given a high-level goal,
an agent like MDCrow can prepare input files, select force fields and parameters, execute
simulations, analyze trajectory outputs, and even query literature or databases to put the
results in context. Such an LLM-based system effectively acts as a researcher’s “co-pilot,”
capable of generating or optimizing MD inputs on the fly and providing insightful analysis
of outcomes. Another example is the AutoSolvateWeb platform by Gadde et al.[21], which
employs a chatbot interface to guide users through complex QM/MM simulation setups. This
approach demonstrates how natural language interfaces, powered by underlying automation,
can lower the barrier for non-experts in performing multi-step simulations. In the realm of
classical MD, an LLM could similarly take a user’s request (e.g. “simulate protein X in a
solvated membrane for 100 ns”), compose the necessary configuration for a tool like NAMD,
adjust simulation parameters based on best practices or user preferences, and monitor or
analyze the run – all while explaining the choices or results in human-readable terms. By
leveraging their ability to parse and generate domain-specific text, LLMs offer a dynamic layer
of automation that complements existing MD pipelines. They can assist in input generation
(translating high-level descriptions into simulation-ready input files or scripts), optimization
(iteratively tuning parameters or protocols by reasoning about the simulation objectives and
outcomes), and result interpretation (providing summaries of simulation data or comparisons
with known biological knowledge). While MDCrow can set up simple protein-in-solvent simulations and AutoSolvateWeb can handle single organic molecules, NAMD-agent goes further
by supporting complex bilayer simulations. In summary, the integration of LLMs into MD
workflows is a promising frontier that builds upon prior automation efforts. It has the potential to further reduce manual overhead, adapt simulations to user intent in real time, and
enhance the accessibility of MD simulations for the broader scientific community.

3. Methods
3.1. Model
The LLM backbone used in this work is Gemini-2.0-flash, for its capabilities in agentic
interaction. The practical application of AI agents in scientific research possesses great
potential for augmenting productivity and information management [22]. To interface with
the LLM, we employ LlamaIndex [23], a python framework that provides support for LLM
applications. Llamaindex’s architecture simplifies the integration of complex data pipelines
into LLM-driven workflows, enabling efficient access to structured and unstructured research
data. The agent is capable of independently generating, modifying, and executing code,
which makes it highly suitable for automation-heavy environments. With LlamaIndex we can
build streamlined and reproducible AI workflows that require minimal supervision, ultimately
augmenting productivity and adaptability in scientific research settings.
3.2. ReAct Agents: Reasoning and Acting in Interactive Environments

Figure 1: ReAct-based workflow for molecular simulation setup: The AI agent reasons and performs actions to automate system preparation: downloading the 1L2Y PDB file, generating and cleaning a YAML
configuration, and running the CHARMM-GUI builder for a solution system.

This work uses ReAct (Reasoning and Acting) agents, a class of intelligent systems that
interleave explicit reasoning steps with tool-using actions to solve complex tasks efficiently.
The ReAct framework combines the strengths of reasoning-based agents with those that
perform actions in external environments, enabling the agent to think, act, observe outcomes,
and adapt its strategy accordingly [24].
As shown in Figure 1, the ReAct agent begins by interpreting the user’s query. It then
produces a reasoning step labeled as "Thought", selects and executes an appropriate "Action"
using available tools, and uses the action’s result to guide the next reasoning step. For
example, in a molecular dynamics workflow, the agent might download a PDB file, generate
a YML configuration, clean it, and execute a CHARMM-GUI setup for simulations. Each
step is guided by prior reasoning and updated based on observed outcomes.
This approach makes ReAct agents both interpretable and reliable, especially in domains
that require multi-step decision-making and interaction with external tools. As a result,
they are well-suited for applications such as scientific computing, web-based reasoning, and
task-focused dialogue systems [24, 25].
3.3. Agentic Workflow
The operational workflow established in this study integrates LLM supervision with automated computational tools to optimize the setup, simulation, and analysis of biomolecular
systems. At the core of this system is the Gemini framework, which leverages Gemini-2.0Flash, a domain-adapted LLM that provides real-time supervision and intervention capabilities throughout the computational pipeline.
The workflow begins with user input in step 1, where initial queries, system specifications (such as protein structure and membrane composition), and simulation parameters are
collected. These instructions are interpreted by Gemini, ensuring clarity, completeness, and
consistency before proceeding. Prior to system assembly, the agent utilizes PDBFixer [26]
to preprocess downloaded protein structures by resolving common issues such as missing
atoms, incomplete residues, and nonstandard residues, ensuring compatibility with subse7

Figure 2: Workflow diagram illustrating the automated molecular dynamics simulation pipeline managed by
the GEMINI-2.0-FLASH agent. The process begins with a user job request (1), which triggers the CHARMMGUI tool (2) for system setup. The user then navigates the solution/membrane builder interface (3) to define
the system components, followed by the generation of simulation-ready input files (4). These files are used in
NAMD to perform molecular dynamics simulations (5). The resulting trajectories are subsequently analyzed
using post-processing tools (6). The GEMINI-2.0-FLASH agent orchestrates the entire workflow, ensuring
seamless integration and execution of each stage.

quent modeling steps. After this, the workflow employs CHARMM-GUI in step 2 and 3
[7, 27, 8], a well-established web-based platform that facilitates the automated assembly of
complex biomolecular systems such as proteins embedded in lipid bilayers, solvated boxes,
or membrane-protein complexes. The automation of the CHARMM-GUI pipeline is accomplished using the Gemini model’s agentic capabilities with reference to the Auto CGUI
github repository[28] as a structured and reliable codebase. Only the Solution Builder and
Membrane Builder modules are considered in the scope of this work.
Following system construction, files generated by CHARMM-GUI, including topology,
coordinate, and simulation parameter files, are organized systematically in structured directories in step 4. This organization enables easier tracking and management, and it also
ensures reproducibility and scalability of the simulation attempts [29].
Selenium, a headless browser automation tool [9], is used to automate interactions with

web-based services such as CHARMM-GUI, ensuring efficient form submissions, parameter
selection, and download management. This automation reduces manual input errors and
accelerates the setup process, particularly for high-throughput simulation preparation.
Once the system is equilibrated, production simulations are initiated using NAMD3
[30, 31], in step 5. NAMD3 is a highly scalable molecular dynamics engine that supports parallel computing architectures and is designed for large biological systems. Post-processing,
including the computation of structural stability metrics such as Root Mean Square Deviation (RMSD), Radius of Gyration (Rg), and Potential Energy profiles is performed in step
6.
Visualization of the evolving system is conducted using molecular graphics programs
like VMD [32], enabling detailed inspection of structural changes, membrane dynamics, and
solvent behavior.
By embedding LLM oversight into all stages from setup to analysis, this operational workflow significantly enhances robustness, efficiency, and reproducibility in molecular simulation
research.
3.4. NAMD-Agent Toolset
Preprocessing Tools
NAMD-Agent begins its workflow by applying structure preprocessing techniques to ensure
high-quality simulation input. The system utilizes a protein repair module in PDBFixer [26]
that automatically addresses missing heavy atoms, incomplete residues, and nonstandard
residues in PDB files. This step ensures compatibility with subsequent modeling tools and
significantly reduces failure points during simulation setup.
Simulation Setup Tools
For molecular system construction, NAMD-Agent automates interactions with CHARMMGUI, specifically its Solution Builder and Membrane Builder modules. This process includes
assembling protein systems, solvating boxes, building membranes, and inserting ions according to user specifications. The agent uses a Selenium-driven browser automation layer to

execute each step of the CHARMM-GUI workflow by submitting forms, handling downloads, and selecting parameters in a consistent and reproducible manner. Output files such
as topologies, coordinates, and parameter sets are organized into structured directories to
simplify downstream processing and ensure traceability.
Execution Tools
Once the system is constructed, production simulations are executed using NAMD. The
agent dynamically manages simulation configuration files, allowing real-time adjustment of
parameters such as temperature control, minimization steps, and boundary conditions.
Analysis and Visualization Tools
Post-processing and trajectory analysis are central features of NAMD-Agent. The agent
automatically performs analyses including RMSD, RMSF, solvent accessible surface area
(SASA), radius of gyration, and hydrogen-bond profiling. These analyses are implemented
using domain-specific Python scripts that draw from MDTraj [33] and OpenMM [34] packages
and tools such as VMD [32] for trajectory parsing and visualization. Outputs include plots
and simulation videos, all saved in standardized formats for easy interpretation and reporting.
Automation and Orchestration Framework
At the core of the system is the Gemini-2.0-Flash model, a large language model designed
for automation in scientific workflows. The model is integrated using a retrieval-augmented
generation framework that fetches code templates, API patterns, and parameter settings
from a curated repository. This setup enables the agent to compose, modify, and execute
simulation workflows based on natural language prompts and evolving simulation states. The
framework supports adaptive behavior, enhances reproducibility, and minimizes the need for
manual coding across all stages of the molecular dynamics pipeline.
3.5. Retrieval-Augmented Generation (RAG) in Code-Aware Simulation Pipelines
Retrieval-Augmented Generation (RAG) is an emerging paradigm that enhances the capabilities of LLMs by coupling them with retrieval mechanisms. This hybrid architecture
addresses a fundamental limitation of LLMs: their inability to recall specific, up-to-date,

Figure 3: Overview of a retrieval-augmented generation (RAG) pipeline for molecular dynamics simulation:
User input and simulation parameters are encoded and processed by a language model. The model retrieves
relevant information, including force fields and solvation settings for the protein, and outputs structured
simulation instructions. These are converted into numerical representations and used to drive simulations,
with results analyzed and visualized for user interpretation.

or domain-constrained knowledge from external sources. RAG achieves this by allowing the
model to query an indexed corpus, such as documentation, academic papers, or code repositories, before generating output conditioned on the retrieved results. Originally introduced
for knowledge-intensive natural language processing tasks such as open-domain question answering [35], RAG has found increasing application in technical and scientific fields where
precision, reproducibility, and grounding in external knowledge are essential.
In this work, we deploy a RAG-based approach for step 2 of our agentic workflow, specifically adapted to the MD simulation domain, where the retrieval corpus is restricted to a
collection of specific automation scripts in the code repository. This repository includes
Python scripts, configuration files, and automation pipelines relevant to setting up and
running simulations via CHARMM-GUI and NAMD. Our setup integrates the LlamaIndex

python framework, with the Gemini-2.0-flash LLM agent which supports codebase awareness
through RAG. Unlike traditional RAG pipelines that rely on natural language corpora, our
implementation retrieves function definitions, API usage patterns, shell scripts, and simulation templates. This code-aware RAG mechanism enables the generation of accurate and
executable automation scripts with minimal human intervention.
Using a code-indexed retrieval framework offers several advantages. First, it ensures that
the LLM-generated code adheres to syntactic and semantic conventions consistent with prior
workflows. Second, retrieval reduces hallucinations by grounding the output in real, tested
examples. This is especially important in domains like computational biology, where an
incorrectly placed file path, parameter mismatch, or missing configuration can invalidate an
entire simulation. Third, code retrieval facilitates faster prototyping by allowing the system
to reuse and adapt existing modules, significantly reducing development time.
Recent research highlights the promise of retrieval-based methods in scientific computing.
For example, projects like Toolformer [36], CodeXGLUE [37], and ReAct-style agent systems
[24, 38] show that LLMs perform better on reasoning and planning tasks when allowed to
consult external code or documentation during generation [39, 40]. Additionally, domainspecific adaptations of RAG have been used in chemistry [41], software engineering [42], and
code generation [43], indicating the broad applicability of this approach.
In our implementation, queries from the user, phrased in natural language, are interpreted by the LLM to identify the goal (e.g., solvate a protein-membrane complex and prepare NAMD input files). Gemini’s agent then analyzes and revises relevant code from the
repository. The Gemini model supervises the entire process and ensures smooth, sequential
execution. As part of our workflow, this RAG-enabled loop continues iteratively, enabling
dynamic refinement and error correction based on the simulation context.
Overall, our RAG framework demonstrates that retrieval from structured code repositories significantly improves the automation, interpretability, and reproducibility of molecular
simulation pipelines. It paves the way for future agentic systems that use not only static

retrieval but also semantic code understanding to assist in scientific computing tasks.
3.6. Devices and Codebase
We deployed the Gemini-2.0-flash model through google’s API. For public benefit and
further research the code is available at the following link: https://github.com/BaratiLab/
NAMD_AGENT. All simulations were performed using a GeForce GTX 1080 Ti GPU with 11
GBs of memory.

4. NAMD-Agent post-processing and trajectory analyses
4.1. Root Mean Square Deviation (RMSD)
The root-mean-square deviation provides a global measure of structural drift by comparing the instantaneous Cartesian coordinates of a trajectory frame (ri (t)) with a reference
structure (riref ) after optimal superposition:
v
u
N
u1 X
t
RMSD(t) =
ri (t) − riref .
N i=1
Because the least-squares fit removes overall translation and rotation, RMSD isolates internal
conformational changes [44]. When interpreted alongside potential energy or secondarystructure timelines, plateaus in the RMSD trace often signal equilibration, while sudden
spikes may indicate domain motions or unfolding events [45]. Ensemble-averaged RMSD
distributions are also useful for clustering structurally similar substates in long trajectories.
4.2. Root Mean Square Fluctuation (RMSF)
Per-residue root-mean-square fluctuations

RMSF(i) =

q

∥ri (t) − ⟨ri ⟩ ⟩t

quantify local flexibility around each atom or residue’s time-averaged position. Mapping
RMSF values onto the three-dimensional structure highlights flexible loops versus rigid cores,
complements B-factors from crystallography, and pinpoints potential epitope or allosteric
sites [46, 47]. Combining RMSF with essential-dynamics or principal-component projections
helps distinguish concerted collective motions from high-frequency local vibrations.
4.3. Solvent Accessible Surface Area (SASA)
SASA integrates the area traced by a probe sphere (typically 1.4 Å) rolling over the vander-Waals surface of a biomolecule [48, 49]. Tracking total and per-residue SASA along the

trajectory illuminates folding/unfolding transitions, burial of hydrophobic patches, or ligandinduced shielding of active-site residues. Decomposition into polar and apolar contributions
is frequently correlated with changes in hydration free energy or binding enthalpy in MMPBSA/GBSA schemes.
4.4. Radius of Gyration (Rg )
The radius of gyration monitors global chain compactness:
v
u
N
u1 X
t
Rg (t) =
mi ∥ri (t) − rCOM (t)∥2 ,
M i=1
where M =

P

i mi and rCOM is the center-of-mass.

In protein folding simulations, a mono-

tonic decrease of Rg toward native-state values indicates collapse, whereas intrinsically disordered proteins maintain larger, fluctuating Rg values that scale with residue number according to Flory’s polymer theory [50, 51]. Plotting Rg against RMSD yields a two-dimensional
free-energy surface that helps distinguish molten-globule intermediates from misfolded offpathway states.
4.5. Hydrogen-Bond Analysis
Hydrogen bonds (H-bonds) are detected via geometric criteria—commonly a donor–acceptor
distance ≤ 3.5 Å and a donor–H–acceptor angle ≥ 120◦ —and enumerated over time [52, 53].
Persistency plots reveal which secondary-structure H-bonds stabilize helices or β-sheets, while
interfacial H-bond lifetimes delineate key hotspots in protein–ligand or protein–protein complexes. Time-correlation functions of H-bond existence allow estimation of exchange kinetics
and water-mediated bridging networks.

5. Results and Discussion
Table 1: Outcome summary of all MD system set-ups

Simulation system

Run status

1UBQ (Solution Builder Run 1)
1L2Y (Solution Builder Run 2)
1AFO (Membrane Builder Run 1)
1CRN (Membrane Builder Run 2)
1J4N (Membrane Builder Run 3)
1AFO (Membrane Builder Run 4)
1K4C (Membrane Builder Run 5)

✗
✗

Remarks

Atypical RMSD plot
XY size of 35 is too small

Table 2: Runtime comparison between a human and an AI agent

PDB ID

Human hands-on time (min)

AI agent time (min)

1UBQ
1L2Y
1AFO-1
1CRN
1AFO-4

The performance of the NAMD-Agent framework was evaluated across seven distinct
molecular dynamics (MD) simulation setups, encompassing both solution-phase and membraneembedded protein systems. As detailed in Table 1 and the supplemental information, five of
the seven simulations were successfully completed, yielding an overall accuracy of 71.4% for
the automated pipeline.
The successful runs included two solution systems (1UBQ and 1L2Y) and three membrane systems (1AFO in two configurations, and 1CRN). All successful simulations produced
RMSD, RMSF, SASA, Radius of Gyration, and hydrogen bond profiles consistent with typical behavior for equilibrated systems, as seen in Figures 3–6 and 8. For example, RMSD
traces plateaued after initial fluctuations, and the radius of gyration remained within expected ranges, suggesting stable system configurations. These findings affirm the pipeline’s
capacity to automate complex simulation preparations and conduct meaningful analyses with
minimal human intervention.

Two simulations failed. In Membrane Builder Run 3 (PDB ID: 1J4N), the system showed
an anomalous RMSD trajectory, indicating structural instability, possibly due to suboptimal membrane embedding or force field incompatibilities not caught during automated
preprocessing. Membrane Builder Run 5 (1K4C) failed to initialize due to a membrane
XY dimension (35 Å) that was too small for the embedded protein, a known constraint in
CHARMM-GUI setups that the agent had not been able to detect.
These outcomes highlight both the promise and the current limitations of LLM-supervised
workflows. On the positive side, the successful test cases demonstrate the system’s ability
to generate valid topologies, apply appropriate solvation and ionization strategies, and carry
out brief 1 ns simulations under standard pH and temperature conditions. On the other
hand, failures point to edge cases in membrane packing and stability assessment that would
benefit from either tighter pre-simulation validation or more advanced, context-aware or
human-driven decision-making by the agent.
The agent’s modular design allowed rapid recovery in the successful runs and straightforward error identification in the failed ones. However, the dependency on hard-coded
CHARMM-GUI parameters and assumptions about membrane size constraints suggest areas for future enhancement, including dynamic parameter validation, geometry checks, and
integration of more robust error-correction routines.
In summary, NAMD-Agent achieved a solid accuracy benchmark (71.4%) across a range
of realistic protein systems and configurations. The agent is also 2-4 times faster at implementation, compared to an experienced human with access to the same code. Being fully
autonomous, its performance confirms the feasibility of LLM-driven MD workflows and sets
the stage for expanding capabilities such as adaptive simulation steering and broader engine
compatibility.

6. Conclusions and Future Work
In this work we introduced NAMD-Agent, an end-to-end, retrieval-augmented, largelanguage-model (LLM) pipeline that turns a short natural-language prompt into fully prepared NAMD input decks, launches production simulations, and returns standard structural
analyses, all with negligible human intervention. By coupling Gemini-2.0-Flash with codeaware retrieval and Selenium-driven browser automation, the system successfully navigates
the multifaceted CHARMM-GUI workflow, manages file organisation, and performs postprocessing on five distinct protein and membrane benchmarks. Across these case studies the
agent generated valid topologies, coordinates, and parameter files in minutes, produced stable trajectories whose RMSD, RMSF, SASA, radius of gyration, and hydrogen-bond profiles
matched literature expectations, and consistently avoided common setup errors such as nonorthogonal unit cells or mismatched patch residues. Taken together, these results demonstrate
that LLM-supervised agents can act as reliable "co-pilots" for routine MD tasks, accelerating
exploratory studies, and providing a reproducible scaffold on which more specialised analyses
can be layered.
Limitations
1. Dependency on web interfaces: CHARMM-GUI HTML elements and download
paths are hard-coded in the current scripts; interface changes could break the workflow.
Also, CHARMM-GUI may become unresponsive when saturated with job requests.
2. Engine specificity: While the concepts are engine-agnostic, NAMD-Agent presently
supports only NAMD/CHARMM-GUI combinations.
3. LLM hallucination and error-handling: Although mitigated by code retrieval
and iterative testing, occasional hallucinated parameters (e.g. unsupported thermostat
keywords) still arise and require manual oversight.
4. Scalability: Large, membrane-embedded systems (> 106 atoms) stress both browser
automation and GPU memory, suggesting the need for tighter HPC integration and
resource-aware planning.

5. User Reliability: The user is responsible for ensuring that the simulation parameters
conform with reality, otherwise CHARMM-GUI might terminate the process.
Future Work
Future work aims to enhance the robustness and applicability of the framework across
multiple dimensions. First, expanding multi-engine generalisation by enabling the agent to
generate inputs for GROMACS, AMBER, and OpenMM through an independent API would
improve versatility greatly. Second, incorporating adaptive simulation steering by coupling
online trajectory analysis with reinforcement learning or Bayesian optimisation could allow
dynamic control over parameters such as temperature ramps, bias potentials, and sampling
windows to better explore rare events. Third, ensuring reproducibility and transparency
through end-to-end provenance tracking and packaging the agent within FAIR-compliant
workflow descriptions such as CWL or Nextflow, along with containerised deployments, would
facilitate reliable use across computing environments. Finally, improving reliability through
the integration of multiple specialised language models for tasks including code generation,
domain expertise, and error checking, organised under a voting or supervisory framework,
could reduce hallucinations and support automatic verification of thermodynamic and topological consistency.
By pursuing these avenues, we anticipate that future incarnations of NAMD-Agent will
evolve from a labour-saving assistant into a proactive scientific collaborator, capable not
only of automating established MD protocols but of designing, executing, and interpreting
adaptive simulation campaigns that push the frontier of computational structural biology.
Acknowledgments
References
[1] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser,
I. Polosukhin, Attention is all you need, Advances in neural information processing
systems 30 (2017).

[2] M. McTear, Conversational ai: Dialogue systems, conversational agents, and chatbots,
Springer Nature, 2022.
[3] Y. Yang, Y. Tan, J. Min, Z. Huang, Automatic text summarization for government
news reports based on multiple features, The Journal of Supercomputing 80 (3) (2024)
3212–3228.
[4] D. Van Veen, C. Van Uden, L. Blankemeier, J.-B. Delbrouck, A. Aali, C. Bluethgen,
A. Pareek, M. Polacin, E. P. Reis, A. Seehofnerová, et al., Adapted large language
models can outperform medical experts in clinical text summarization, Nature medicine
30 (4) (2024) 1134–1142.
[5] N. Team, et al., Scaling neural machine translation to 200 languages, Nature 630 (8018)
(2024) 841.
[6] Z. Durante, Q. Huang, N. Wake, R. Gong, J. S. Park, B. Sarkar, R. Taori, Y. Noda,
D. Terzopoulos, Y. Choi, et al., Agent ai: Surveying the horizons of multimodal interaction, arXiv preprint arXiv:2401.03568 (2024).
[7] S. Jo, T. Kim, V. G. Iyer, W. Im, Charmm-gui: a web-based graphical user interface for
charmm, Journal of computational chemistry 29 (11) (2008) 1859–1865.
[8] J. Lee, X. Cheng, S. Jo, A. D. MacKerell, J. B. Klauda, W. Im, Charmm-gui input
generator for namd, gromacs, amber, openmm, and charmm/openmm simulations using
the charmm36 additive force field, Biophysical journal 110 (3) (2016) 641a.
[9] SeleniumHQ, Contributors, SeleniumHQ/selenium: A suite of tools for web browser
automation, accessed: 2025-01-12 (2025).
URL https://github.com/SeleniumHQ/selenium
[10] Y. Jadhav, P. Pak, A. B. Farimani, Llm-3d print: large language models to monitor and
control 3d printing, arXiv preprint arXiv:2408.14307 (2024).

[11] J. Ock, T. Vinchurkar, Y. Jadhav, A. B. Farimani, Adsorb-agent: Autonomous identification of stable adsorption configurations via large language model agent, arXiv preprint
arXiv:2410.16658 (2024).
[12] A. Raman, C. Merrill, A. George, A. B. Farimani, Llm-drone:

Aerial additive

manufacturing with drones planned using large language models, arXiv preprint
arXiv:2503.17566 (2025).
[13] A. Chaudhari, J. Ock, A. B. Farimani, Modular large language model agents for multitask computational materials science (2025).
[14] T. Zeng, S. Badrinarayanan, J. Ock, C.-K. Lai, A. B. Farimani, Llm-guided chemical process optimization with a multi-agent approach, arXiv preprint arXiv:2506.20921
(2025).
[15] A. A. Yekeen, O. A. Durojaye, M. O. Idris, H. F. Muritala, R. O. Arise, Chaperong:
A tool for automated gromacs-based molecular dynamics simulations and trajectory
analyses, Computational and structural biotechnology journal 21 (2023) 4849–4858.
[16] H. Singh, A. Raja, A. Prakash, B. Medhi, Gmx_qk: an automated protein/protein–
ligand complex simulation workflow bridged to mm/pbsa, based on gromacs and zenitydependent gui for beginners in md simulation study, Journal of Chemical Information
and Modeling 63 (9) (2023) 2603–2608.
[17] D. Suplatov, Y. Sharapova, V. Švedas, Easyamber: A comprehensive toolbox to automate the molecular dynamics simulation of proteins, Journal of Bioinformatics and
Computational Biology 18 (06) (2020) 2040011.
[18] M. P. Baumgartner, H. Zhang, Building admiral, an automated molecular dynamics and
analysis platform, ACS Medicinal Chemistry Letters 11 (11) (2020) 2331–2335.

[19] L. Carvalho Martins, E. A. Cino, R. S. Ferreira, Pyautofep: An automated free energy
perturbation workflow for gromacs integrating enhanced sampling methods, Journal of
Chemical Theory and Computation 17 (7) (2021) 4262–4273.
[20] Q. Campbell, S. Cox, J. Medina, B. Watterson, A. D. White, Mdcrow:

Au-

tomating molecular dynamics workflows with large language models, arXiv preprint
arXiv:2502.09565 (2025).
[21] R. S. Gadde, S. Devaguptam, F. Ren, R. Mittal, L. Dong, Y. Wang, F. Liu, Chatbotassisted quantum chemistry for explicitly solvated molecules, Chemical Science (2025).
[22] M. Gridach, J. Nanavati, K. Z. E. Abidine, L. Mendes, C. Mack, Agentic ai for scientific discovery: A survey of progress, challenges, and future directions, arXiv preprint
arXiv:2503.08979 (2025).
[23] J. Liu, Llamaindex.
URL https://github.com/jerryjliu/llama_index
[24] S. Yao, J. Zhao, K. N. Yu, Y. Cao, React: Synergizing reasoning and acting in language
models, arXiv preprint arXiv:2210.03629 (2022).
[25] T. Chen, J. Li, K. Lin, V. Jain, et al., Agents: An open-source framework for building
llm-based agents, arXiv preprint arXiv:2308.08155 (2023).
[26] P. Eastman, O. Team, Pdbfixer, https://github.com/openmm/pdbfixer, accessed:
2025-06-10 (2024).
[27] E. J. Wu, X. Cheng, S. Jo, H. Rui, K. Song, W. Im, Charmm-gui membrane builder
toward realistic biological membrane simulations, Journal of Computational Chemistry
35 (27) (2014) 1997–2004.
[28] N. Kern, auto_cgui: Automatic charmm-gui browser interaction with python, https:
//github.com/nk53/auto_cgui, version accessed on 2025-06-09, MIT license (2025).

[29] J. Lee, D. S. Patel, J. Ståhle, S. J. Park, N. R. Kern, S. Kim, J. Lee, X. Cheng,
M. A. Valvano, O. Holst, et al., Charmm-gui membrane builder for complex biological
membrane simulations with glycolipids and lipoglycans, Journal of Chemical Theory
and Computation 15 (1) (2019) 775–786.
[30] J. C. Phillips, R. Braun, W. Wang, J. Gumbart, E. Tajkhorshid, E. Villa, C. Chipot,
R. D. Skeel, L. Kale, K. Schulten, Scalable molecular dynamics with namd, Journal of
Computational Chemistry 26 (16) (2005) 1781–1802.
[31] T. A. Trautman, G. Fiorin, S. Patel, D. J. Hardy, J. E. Stone, R. D. Skeel, J. C. Phillips,
K. Schulten, Namd goes quantum: An integrative suite for hybrid simulations, Journal
of Chemical Theory and Computation 18 (5) (2022) 3062–3079.
[32] W. Humphrey, A. Dalke, K. Schulten, Vmd: visual molecular dynamics, Journal of
Molecular Graphics 14 (1) (1996) 33–38.
[33] R. T. McGibbon, K. A. Beauchamp, M. P. Harrigan, C. Klein, J. M. Swails, C. X.
Hernández, C. R. Schwantes, L.-P. Wang, T. J. Lane, V. S. Pande, Mdtraj: a modern
open library for the analysis of molecular dynamics trajectories, Biophysical journal
109 (8) (2015) 1528–1532.
[34] P. Eastman, J. Swails, J. D. Chodera, R. T. McGibbon, Y. Zhao, K. A. Beauchamp,
L.-P. Wang, A. C. Simmonett, M. P. Harrigan, C. D. Stern, et al., Openmm 7: Rapid development of high performance algorithms for molecular dynamics, PLoS computational
biology 13 (7) (2017) e1005659.
[35] P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal, D. Kiela, V. Moiseev, S. Riedel, V. Stoyanov, Retrieval-augmented generation for knowledge-intensive
nlp tasks, in: Advances in Neural Information Processing Systems, Vol. 33, 2020, pp.
9459–9474.

[36] T. Schick, Y. Dwivedi-Yu, S. Hosseini, D. Sorokin, N. Houlsby, S. Gelly, Toolformer:
Language models can teach themselves to use tools, arXiv preprint arXiv:2302.04761
(2023).
[37] S. Lu, D. Liu, W. Wang, et al., Codexglue: A benchmark dataset and open challenge for
code intelligence, Empirical Methods in Natural Language Processing (EMNLP) (2021).
[38] G. Mialon, T. Scialom, P. Gallinari, J. Staiano, Augmented language models: a survey,
arXiv preprint arXiv:2302.07842 (2023).
[39] A. Chandrasekhar, J. Chan, F. Ogoke, O. Ajenifujah, A. B. Farimani, Amgpt: A large
language model for contextual querying in additive manufacturing, Additive Manufacturing Letters 11 (2024) 100232.
[40] A. Chandrasekhar, O. B. Farimani, O. T. Ajenifujah, J. Ock, A. B. Farimani, Nanogpt:
A query-driven large language model retrieval-augmented generation system for nanotechnology research, arXiv preprint arXiv:2502.20541 (2025).
[41] R. S. Gadde, S. Devaguptam, F. Ren, et al., Chatbot-assisted quantum chemistry for
explicitly solvated molecules, Chemical Science (2025).
[42] M. Chen, J. Tworek, H. Jun, et al., Evaluating large language models trained on code,
in: NeurIPS, 2021.
[43] C. Zhang, et al., Code llama: Open foundation models for code, arXiv preprint
arXiv:2308.12950 (2023).
[44] W. Kabsch, A solution for the best rotation to relate two sets of vectors, Acta Crystallographica Section A 32 (1976) 922–923. doi:10.1107/S0567739476001873.
[45] M. Karplus, J. A. McCammon, Molecular dynamics simulations of biomolecules, Nature
Structural Biology 9 (2002) 646–652. doi:10.1038/nsb0902-646.

[46] A. Amadei, A. B. Linssen, H. J. C. Berendsen, Essential dynamics of proteins, Proteins: Structure, Function and Genetics 17 (4) (1993) 412–425. doi:10.1002/prot.
340170408.
[47] D. Seeliger, B. L. de Groot, Protein thermostability calculations using alchemical free
energy simulations, Biophysical Journal 98 (10) (2010) 2309–2316. doi:10.1016/j.
bpj.2010.01.051.
[48] B. Lee, F. M. Richards, The interpretation of protein structures: Estimation of static
accessibility, Journal of Molecular Biology 55 (3) (1971) 379–400.

doi:10.1016/

0022-2836(71)90324-X.
[49] A. Shrake, J. A. Rupley, Environment and exposure to solvent of protein atoms.
lysozyme and insulin, Journal of Molecular Biology 79 (2) (1973) 351–371.

doi:

10.1016/0022-2836(73)90011-9.
[50] P. J. Flory, Statistical Mechanics of Chain Molecules, Interscience, New York, 1969.
[51] J. E. e. Kohn, Random-coil behavior and the dimensions of chemically unfolded proteins,
Proceedings of the National Academy of Sciences USA 101 (34) (2004) 12491–12496.
doi:10.1073/pnas.0403643101.
[52] E. N. Baker, R. E. Hubbard, Hydrogen bonding in globular proteins, Progress in
Biophysics and Molecular Biology 44 (1984) 97–179. doi:10.1016/0079-6107(84)
90007-5.
[53] I. K. McDonald, J. M. Thornton, Satisfying hydrogen bonding potential in proteins,
Journal of Molecular Biology 238 (5) (1994) 777–793. doi:10.1006/jmbi.1994.1334.

Supplemental Information
All of these experiments were run for 1ns at a pH of 7.0 using the NPT ensemble.
6.1. Simulation Details: Solution builder Run 1
The simulation system was prepared using the CHARMM-GUI Solution Builder. The
following parameters were used:
• PDB ID: 1UBQ
• Target temperature: 300 K
• Solvation: Explicit solvent model
• Periodic Boundary Conditions: Enabled
• Force field: CHARMM36m (default as provided by CHARMM-GUI)
Example prompt:

Generate a YML-formatted configuration file for a molecular dy-

namics system labeled 1UBQ solution system. The system uses the protein 1UBQ, sourced
from the file 1ubq.pdb, and is prepared in explicit solvent with periodic boundary conditions. The simulation will be conducted using NAMD with hydrogen mass repartitioning
enabled, at a temperature of 300 K. Use the ion type KCl at a concentration of 0.15 M.
This setup corresponds to a solution case type. Ensure the PDB orientation is not adjusted.
After generating and cleaning the YML file, run the simulation and perform post-processing
analysis.

Figure 4: Structural analysis of the simulation system showing (a) RMSD, (b) RMSF, (c) SASA, (d) Radius

6.2. Simulation Details: Solution Builder Run 2
The simulation system was prepared using the CHARMM-GUI Solution Builder. The
following parameters were used:
• PDB ID: 1L2Y
• Target temperature: 300 K
• Solvation: Explicit solvent model
• Periodic Boundary Conditions: Enabled
• Force field: CHARMM36m (default as provided by CHARMM-GUI)

Example prompt: Generate a YML-formatted configuration file for a molecular dynamics system labeled 1L2Y solution system. The protein used is 1L2Y, sourced from the file
1l2y.pdb. The system is solvated explicitly and periodic boundary conditions are enabled.
NAMD is the simulation engine, with hydrogen mass repartitioning active. Use the ion type
KCl at a concentration of 0.15 M. The simulation will be run at 300 K and categorized under the solution case type. Do not apply orientation from the PDB. Once the YML file is
generated and cleaned, run the simulation and execute post-processing routines.

Figure 5: Structural analysis of the simulation system showing (a) RMSD, (b) RMSF, (c) SASA, (d) Radius

6.3. Simulation Details: Membrane Builder Run 1
Molecular dynamics simulation input files were generated using CHARMM-GUI’s Membrane Builder. The following parameters were specified during system preparation:

• Structure input (PDB ID): 1AFO
• Membrane dimensions (XY): 50
Example prompt: Generate a YML-formatted configuration file for a membrane molecular dynamics system labeled 1AFO membrane system. The structure is taken from 1afo.pdb,
and the orientation is derived from the OPM database. The membrane is composed of POPC
lipids in both upper and lower leaflets in a 1:1 ratio, with XY dimesnions of 50. Solvation and
pore water inclusion are enabled. Use the ion type KCl at a concentration of 0.15 M. Ions are
placed using a Monte Carlo method. The simulation is to be run with NAMD, using hydrogen
mass repartitioning and a temperature of 310 K. The case type is bilayer. After generating
and cleaning the YML file, proceed with running the simulation and post-processing.

Figure 6: Structural analysis of the simulation system showing (a) RMSD, (b) RMSF, (c) SASA, (d) Radius

6.4. Simulation Details: Membrane Builder Run 2
• Structure input (PDB ID): 1CRN
• Membrane dimensions (XY): 60
• System temperature: 303.15 K

Example prompt: Generate a YML-formatted configuration file for a membrane molecular
dynamics system labeled 1CRN membrane system. The input structure is 1crn.pdb, and
orientation should be applied using OPM. The membrane consists of POPC lipids in both
leaflets at a 1:1 ratio, with XY dimesnions of 50. Solvation and pore water are included,
and ions are placed using a Monte Carlo approach. Use the ion type KCl at a concentration
of 0.15 M. The simulation will be executed with NAMD at 303.15 K, with hydrogen mass
repartitioning enabled. This configuration is a bilayer case. Once the YML file is created
and cleaned, run the simulation and carry out post-processing steps.

Figure 7: Structural analysis of the simulation system showing (a) RMSD, (b) RMSF, (c) SASA, (d) Radius

6.5. Simulation Details: Membrane Builder Run 3
• Structure input (PDB ID): 1J4N
• Membrane dimensions (XY): 50
• Force field: CHARMM36m
• Solvation: Enabled
• Boundary conditions: Periodic boundary conditions via extended system configuration
Example prompt: Generate a YML-formatted configuration file for a membrane molecular dynamics system labeled 1J4N membrane system. The protein structure is from 1j4n.pdb.
The membrane includes POPC lipids in both upper and lower layers in a 1:1 ratio, with XY
dimesnions of 50. Solvation is enabled, and ions are positioned using the Monte Carlo approach. Use the ion type KCl at a concentration of 0.15 M. Periodic boundary conditions
should be applied. The system is simulated using NAMD at a temperature of 310 K with
hydrogen mass repartitioning turned on. This is a bilayer case. PDB-based orientation
should not be applied. Clean the YML after generation, run the simulation, and perform
post-processing analysis.

Figure 8: Structural analysis of the simulation system showing (a) RMSD, (b) RMSF, (c) SASA, (d) Radius

6.6. Simulation Details: Membrane Builder Run 4
• Structure input (PDB ID): 1AFO
• Membrane dimensions (XY): 60

Example prompt: Generate a YML-formatted configuration file for a membrane molecular dynamics system labeled 1AFO membrane system. The input structure comes from
1afo.pdb, with membrane orientation set via the OPM database. The bilayer includes POPC
in both leaflets in a 1:1 ratio, with XY dimesnions of 50. Solvation and pore water are included, and ions are added using the Monte Carlo method. Use the ion type KCl at a
concentration of 0.15 M. The simulation engine is NAMD, with hydrogen mass repartitioning enabled and a temperature of 310 K. This is a bilayer case type. After generating and
cleaning the YML file, run the simulation and proceed with post-processing.

Figure 9: Structural analysis of the simulation system showing (a) RMSD, (b) RMSF, (c) SASA, (d) Radius
