# MDCrow: Automating Molecular Dynamics Workflows with Large Language Models

**Authors:** Campbell, Quintina; Cox, Sam; Medina, Jorge; Watterson, Brittany; White, Andrew D.
**Year:** 2025
**Venue:** Machine Learning: Science and Technology
**DOI:** 10.1088/2632-2153/ae4b07 (arXiv:2502.09565)
**Source PDF URL:** https://arxiv.org/pdf/2502.09565
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---
MDC ROW: AUTOMATING M OLECULAR DYNAMICS
W ORKFLOWS WITH L ARGE L ANGUAGE M ODELS

Quintina Campbell†1 , Sam Cox†1,3 , Jorge Medina†1 , Brittany Watterson2 , Andrew D. White∗1,3

Department of Chemical Engineering, University of Rochester, Rochester, New York, USA
Department of Biomedical Engineering, University of Rochester, Rochester, New York, USA
FutureHouse Inc., San Francisco, CA

A BSTRACT
Molecular dynamics (MD) simulations are essential for understanding biomolecular systems but remain challenging to automate. Recent advances in large language models (LLM) have demonstrated
success in automating complex scientific tasks using LLM-based agents. In this paper, we introduce
MDCrow, an agentic LLM assistant capable of automating MD workflows. MDCrow uses chainof-thought over 40 expert-designed tools for handling and processing files, setting up simulations,
analyzing the simulation outputs, and retrieving relevant information from literature and databases.
We assess MDCrow’s performance across 25 tasks of varying required subtasks and difficulty, and
we evaluate the agent’s robustness to both difficulty and prompt style. gpt-4o is able to complete
complex tasks with low variance, followed closely by llama3-405b, a compelling open-source
model. While prompt style does not influence the best models’ performance, it has significant effects on smaller models.

Introduction

Molecular dynamics (MD) simulations is a common method to understand dynamic and complex systems in chemistry
and biology. While MD is now routine, its integration into and impact on scientific workflows has increased dramatically over the past few decades [1–3]. There are two main reasons for this: First, MD provides valuable insights.
Through simulations, scientists can study structural and dynamic phenomena, perturbations, and dynamic processes
in their chemical systems. Second, innovations in hardware and expert-designed software packages have made MD
much more accessible to both experienced and novice users [3].
For a given protein simulation, parameter selection is nontrivial: the user must provide the input structure (such as
a PDB [4] file), select a force field (e.g., CHARMM [5], AMBER [6]), and specify parameters such as temperature,
integrator, simulation length, and equilibration protocols. Simulations also generally require pre- and post-processing
steps, along with various analyses. For instance, a user may need to clean or trim a PDB file, add a solvent, or
analyze the protein’s structure. After simulation, they might examine the protein’s shape throughout the simulation or
assess its stability under different conditions. The choices for pre-processing, analysis, and simulation parameters are
highly specific to any given use case and often require expert intuition. Thus, automating this process is difficult but
beneficial.
Several efforts have been made to automate MD workflows [7–17], focusing largely on specific domains, such as
RadonPy for polymer’s simulations [8], or PyAutoFEP for proteins and small molecules for drug-screening [16].
Other approaches are constrained to a particular combination of simulation software and simulation (e.g. GROMACS
and Free Energy Perturbation). Certainly, there has been significant community-driven improvement in automating
and creating MD toolkits [14, 18–24] and user-friendly interfaces and visualizations [25–32]. While these advances
†
*

These authors contributed equally to this work
Corresponding author: andrew.white@rochester.edu

improve the capabilities and ease of use in many cases, the inherent variability of MD workflows still poses a great
challenge for full automation.
Large-Language Model (LLM) agents [33–36] have gained popularity for their ability to automate technical tasks
through reasoning and tool usage, even surpassing domain-specialized LLMs (e.g., BioGPT [37], Med-PaLM [38])
when programmed for specialized roles [39]. These agents have demonstrated promising results in scientific tasks
within a predefined toolspace, with tools like ChemCrow and Coscientist successfully automating complex workflows
and novel design in chemical synthesis [40–42]. Likewise, LLM-driven automation has been explored in materials research [43–46], literature and data aggregation [47, 48], and more sophisticated tasks [45, 49–55]. Most similar to this
work, ProtAgents [55] is a multi-agent modeling framework tackling protein-related design and analysis, and LLaMP
[45] applies a retrieval-augmented generation (RAG)-based ReAct agent to simulate inorganic materials by interfacing
with literature databases, Wikipedia, and atomistic simulation tools. Although preliminary work has applied agentic
LLMs to MD via a RAG-based agent [45], no fully adaptive and autonomous system exists for biochemical MD or
protein simulations. See Ramos et al.[56] for a recent review on the design, assessment, and applications of scientific
agents.
Here we present MDCrow, an LLM-agent capable of autonomously completing MD workflows. Our main contributions to the field are (1) we assess MDCrow’s performance across 25 tasks with varying difficulty and compare
performance of different LLM models; (2) we measure robustness how agents are prompted and task complexity
based on required number of subtasks we compare with simply equipping an LLM with a python interpreter with the
required packages installed, rather than using a custom built environment. Our main conclusions is that MDCrow with
gpt-4o or llama3-405b is able to perform nearly all of our assessed tasks and is relatively insensitive to how precise
the instructions are given to it. See Figure 1D for an overview of the main results.

Methods

2.1

MDCrow Toolset

MDCrow is an LLM agent, which consists of an environment of tools that emit observations and an LLM that selects
actions (tools + inpnut arguments). MDCrow is built with Langchain [57] and a ReAct style prompt.[35]. The tools
mostly consist of analysis and simulation methods; we use OpenMM [22] and MDTraj [21] packages, but in principle
our findings generalize to any such packages.
MDCrow’s tools can be categorized in four groups: Information Retrieval, PDB & Protein, Simulation, and Analysis
(see Figure 1B).
Information Retrieval Tools These tools enable MDCrow to build context and answer simple questions posed by
the user. Most of the tools serve as wrappers for UniProt API functionalities [58], allowing access to data such as
3D structures, binding sites, and kinetic properties of proteins. Additionally, we include a LiteratureSearch tool,
which uses PaperQA [48] to answer questions and retrieve information from literature. PaperQA accesses a local
database of relevant PDFs, selected specifically for the test prompts, which can be found in SI section C. This realtime information helps the system provide direct answers to user questions and can also assist the agent in selecting
parameters or guiding simulation processes.
PDB & Protein Tools MDCrow uses these tools to interact directly with PDB files, performing tasks such as cleaning structures with PDBFixer [22], retrieving PDBs for small molecules and proteins, and visualizing PDBs through
Molrender [59] or NGLview [60].
Simulation Tools All included simulation tools use OpenMM [22] for simulation and PackMol [19] for solvent addition. These tools are built to manage dynamic simulation parameters, handle errors related to inadequate parameters or
incomplete preprocessing, and address missing forcefield templates efficiently. The agent responds to simulation setup
errors through informative error messages, improving overall robustness. Finally, the simulation tools outputs Python
scripts that can be modified directly by MDCrow whenever the simulation requires additional steps or parameters.
Analysis Tools This group of tools is the largest in the toolset, designed to cover common MD workflow analysis
methods, many of which are built on MDTraj [21] functionalities. Examples include computing the root mean squared
distance (RMSD) with respect to a reference structure, the radius of gyration, analyzing the secondary structure, and
various plotting functions.

Figure 1: A. MDCrow workflow. Starting with a user prompt and initialized with a set of MD tools, MDCrow follows
a chain-of-thought process until it completes all tasks in the prompt. The final output includes a response, along
with all resulting analyses and files. B. The tool distribution categorized into 4 types: information retrieval, PDB
and protein handling, simulation, and analysis. A few examples from each category are shown. C. Two example
prompts that MDCrow is tested on. The first is the simplest prompt, containing only 1 subtask. The most complex task
requires 10 subtasks. D. Average subtask completion across all 25 prompts as task complexity (the number of subtasks
per prompt) increases. The top three performing base-LLMs are shown. Among them, gpt-4o and llama3-405b
consistently maintain high stability, staying close to 100% completion even as task complexity increases.

2.2

Chatting with Simulations

A key challenge in developing an automated MD assistant is ensuring it can manage a large number of files, analyses, and long simulations and runtimes. Although MDCrow has been primarily tested with shorter simulations, it is
designed to handle larger workflows as well. Its ability to retrieve and resume previous runs allows users to start a
simulation, step away during the long process, and later continue interactions and analyses without needing to stay
engaged the entire time. An example of this chatting feature is shown in Figure 2.
MDCrow creates an LLM-generated summary of the user prompt and agent trace, which is assigned to a unique run
identifier provided at the end of the run (but accessible at any time during the session). Each run’s files, figures, and
path registry are saved in a unique checkpoint folder linked to the run identifier.

When resuming a chat, the LLM loads the summarized context of previous steps and maintains access to the same
file corpus, as long as the created files remain intact. To resume a run, the user simply provides the checkpoint
directory and run identifier. MDCrow then loads the corresponding memory summaries and retrieves all associated
files, enabling seamless continuation of analyses.

Figure 2: Example Chat Example of chat with MDCrow. The user first asks to download PDB files for two systems.
Then, once MDCrow has completed this task, the user asks for analysis of the files. Next, the user asks for a quick 10
ps simulation of both files, and MDCrow saves all files for later handling. Lastly, the user asks for plots of RMSD for
each simulation over time, and MDCrow responds with each plot.

Results

3.1

MDCrow Performance on Various Tasks

To assess MDCrow’s ability to complete tasks of varying difficulty, we designed 25 prompts with different levels of
complexity and documented the number of subtasks (minimum required steps) needed to complete each task. MDCrow
was not penalized for taking additional steps, but was penalized for omitting necessary ones. For example, the first
prompt in Figure 1C contains a single subtask, whereas the complex task requires 10 subtasks: downloading the PDB
file, performing three simulations, and performing two analyses per simulation. If the agent failed to complete an
earlier step, it was penalized for every subsequent step it could not perform due to that failure.
The 25 prompts require between 1 and 10 subtasks, with their distribution shown in Figure 3B. Each prompt was tested
across three GPT models (gpt-3.5-turbo-0125, gpt-4-turbo-2024-04-09, gpt-4o-2024-08-06) [61, 62],

two Llama models (llama-v3p1-405b-instruct, llama-v3p1-70b-instruct) [63] (accessed via the Fireworks
AI API with 8-bit floating point (8FP) quantization [64]), and two Claude models (claude-3-opus-20240229,
claude-3-5-sonnet-20240620) [65, 66]. A newer Claude Sonnet model, claude-3-5-sonnet-20241022 was
tested in later experiments but was not found to give superior results, so it was not tested on these 25 prompts. All
other parameters were held constant across tests, and each version of MDCrow executed a single run per prompt.
Each run was evaluated by experts recording the number of required subtasks the agent completed and using Boolean
indicators to indicate accuracy, whether the agent triggered a runtime error, and whether the trajectory contained any
hallucinations. Since the agent trajectories for each run are inherently variable, accuracy is defined as the result’s
consistency with the expected trajectory rather than comparing against a fixed reference.
The percentage of tasks that were deemed to have valid solutions for MDCrow with each base-LLM is shown in Figure 3A. The lowest performing model was gpt-3.5. This is not surprising, as this model had some of the highest
hallucination rates (32% of prompt completions contained hallucinations), compared to the absence of documented
hallucinations in the higher performing models, gpt-4o and llama3-405b. However, the discrepancy in accuracy
rates between models cannot solely be attributed to hallucinations, as gpt-3.5 attempted fewer than half of the required subtasks, whereas the higher-performing models, gpt-4o and llama3-405b, attempted 80-90% of the required
subtask, earning accuracy in answering for 72% and 68% of tasks, respectively (Figures 3C, D).
These results indicate that MDCrow can handle complex MD tasks but is limited by the capabilities of the base
model. For gpt-4-turbo, gpt-3.5, and llama3-70b, the number of trajectories with verified results decreases
significantly as task complexity increases (Figure 3C). In contrast, gpt-4o and llama3-405b show only a slight
decline, demonstrating that MDCrow performs well even for complex tasks when paired with more robust base models.

Figure 3: MDCrow Performance across Large Language Models. A. Summary of MDCrow performance dependent
on LLM. Percentage of accuracy is determined by whether it gave acceptable final answer or not. While statistically
indistinguishable from Claude and Llama models, gpt-4o significantly outperforms the rest of GPT models on giving
accurate solutions (t-test, 0.004 ≤ p-value ≤ 0.046). B. The distribution of number of subtasks in each task across 25
prompts. The prompts range from 1-10 steps, with each step count belonging to at least 2 prompts. C. Percentages
of prompts with accurate solutions with respect to LLM used and number of subtasks per task. The correlation
between accuracy and complexity is statistically significant for all LLMs (Spearman correlation, 3.9 × 10−7 ≤ pvalue ≤ 1.1 × 10−2 ) D. Percentage of the subtasks that the agent completed for each base LLM per task.

3.2

MDCrow Robustness

We evaluated the robustness of MDCrow on complex prompts and different prompt styles. We hypothesized that some
models would excel at completing complex tasks, while others would struggle—either forgetting steps or hallucinating—as the number of required subtasks increased. To test this, we created a sequence of 10 prompts that increased in
complexity. The first prompt required a single subtask, and each subsequent prompt added an additional subtask (see
Figure 4A). Each prompt was tested twice: once in a natural, conversational style and once with explicitly ordered
steps. Example prompts can be seen in Figure 4B.
To quantify robustness, we calculated the coefficient of variation (CV) for the percentage of completed subtasks
across tasks. A lower CV indicates greater consistency in task completion and, therefore, higher robustness. The
analysis revealed clear differences in robustness across models and prompt types. Overall, gpt-4o and llama3-405b
demonstrated moderate to high robustness, while the Claude models showed significantly lower robustness. The
performance comparison is shown in Figure 4C.
We expected that the percentage of subtasks completed by each model would decrease as task complexity increased.
However, with gpt-4o and llama3-405b as base models, MDCrow demonstrated a strong relationship between the
number of required and completed subtasks (Figure 4D) for both prompt types, indicating consistent performance
regardless of task complexity or prompt style. The three included Claude models demonstrated less impressive performance. claude-3-opus followed the linear trend very loosely, becoming more erratic as task complexity increased.
As the tasks required more subtasks, the model consistently misses nuances in the instructions and make logical errors. Both claude-3.5-sonnet models gave poor performance on these tasks, often producing the same error (see
SI section A).

3.3

MDCrow Comparison

We also compared MDCrow to two baselines: a ReAct [35] agent with only a Python REPL tool and a single-query
LLM. MDCrow and the baselines were tested on the same 25 prompts as previously mentioned, all using gpt-4o. We
use different system prompts to accommodate each framework, guiding the LLM to utilize common packages with
MDCrow, and these prompts can be found in SI section B.
The single-query LLM is asked to complete the prompt by writing the code for all subtasks, not unlike what standalone
ChatGPT would be asked to do. We then execute the code ourselves and evaluate the outcomes accordingly. ReAct
with Python REPL can write and execute codes using a chain-of-thought framework. We find that MDCrow outperforms the two baselines significantly, as shown in Figure 5A, on attempting all subtasks and achieving an accurate
solution. Not surprisingly, the two baseline methods struggled with code syntax errors and incorrect handling of PDB
files. There is not a significant difference between the two baselines, indicating that the ReAct framework did not
significantly boost the model’s robustness.
In Figure 5B, we observe that the performance of all three methods generally declines as task complexity increases.
However, both baseline methods drop to zero after just three steps, with performance then fluctuating erratically at
higher complexities. This is not surprising, as proper file processing and simulation setup are crucial for optimal LLM
performance in MD tasks. In contrast, MDCrow demonstrates greater robustness and reliability in handling complex
tasks, thanks to its well-designed system for accurate file processing and simulation setup, as well as its ability to
dynamically adjust to errors.

3.4

MDCrow Extrapolation through Chatting

We further show MDCrow’s ability to harness its chatting feature and extrapolate outside of its toolset to complete
new tasks. This task requires MDCrow to perform an annealing simulation, which is not part of the current toolset.
The agent achieves this by first setting up a simulation to find appropriate system parameters and handle possible early
errors. Then, the agent modifies the script according to the user’s request. Once the simulation is complete, the user
later asks for simulation analyses, shown in Figures 6A, B.
This shows that MDCrow has the ability to generalize outside of its toolset and is capable of completing more complicated and/or user-specific simulations. By utilizing the chatting feature, users can walk MDCrow through new
analyses, reducing the risk of catastrophic mistakes.

Figure 4: A. The number of subtasks in each task, categorized by type. Task 1 begins with a single pre-simulation
subtask (Download a PDB file) and each subsequent task adds a single subtask, adding to a total of 10 tasks with
a maximum of 10 subtasks. B. Example of ”Natural” and ”Ordered” prompt style on a three-step prompt. C. The
robustness of MDCrow built on each model with both prompt types, measured by coefficient of variation (CV). Lower
CV is interpreted as greater consistency. gpt-4o and llama3-405b are the more robust models, as the Claude
models have higher CVs. D. Comparison of subtask completion across models and prompt types. In the 9-subtask
prompt, gpt-4o encountered an error after only one step and gave up without trying to fix it. In general, gpt-4o and
llama3-405b have relatively robust performance with increasing complexity for both prompt types. claude-3-opus
struggles with more complex tasks, making more logical errors for complex tasks. The two claude-3.5-sonnet
models showed fairly poor performance across this experiment.

Discussion

Although LLMs’ scientific abilities are growing [67–69], they cannot yet independently complete MD workflows,
even with a ReAct framework and Python interpreter. However, with frontier LLMs, chain-of-thought, and an expertcurated toolset, MDCrow successfully handles a broad range of tasks. It performs 80% better than gpt-4o in ReAct
workflows at completing subtasks, which is expected due to MD workflows’ need for file handling, error management,
and real-time data retrieval.
In some cases, particularly for complex tasks beyond its explicit toolset, MDCrow’s performance may improve with
human guidance. The system’s chatting feature allows users to continue previous conversations, clarify misunderstandings, and guide MDCrow step-by-step through difficult tasks. This adaptability helps MDCrow recover from
failures, refine its approach based on user intent, and handle more complex workflows. This suggests that, with more
advanced LLM models, targeted feedback, and the addition of specialized tools, MDCrow could tackle an even broader
range of tasks. We did not do a full evaluation of MDCrow’s capabilities through this chatting feature in this work.
For all LLMs, task accuracy and subtask completion are affected by task complexity. Interestingly, while gpt-4o can
handle multiple steps with low variance, llama3-405b is a compelling second best, as an open-source model. Other
models, such as gpt-3.5 and claude-3.5-sonnet, struggle with hallucinations or inability to follow multistep instructions. Performance on these models, however, is improved with explicit prompting or model-specific optimization
(especially for claude-3.5-sonnet).

Figure 5: Performance across LLM Frameworks using the same 25-prompt set: MDCrow, direct LLM with no tools
(single-query), and ReAct agent with only Python REPL tool. All use gpt-4o. A. Performance among LLM frameworks measured by whether accuracy and average percentage of subtasks they complete for each of 25 task prompts.
MDCrow is significantly better at giving accurate solutions than direct LLM (t-test, p = 1 × 10−3 ) and ReAct (ttest, p = 4 × 10−4 ). MDCrow completes significantly more subtasks on average compared to direct LLM (t-test,
p = 1 × 10−6 ) and ReAct (t-test, p = 6 × 10−6 ). B. Percentage of tasks completed with the respect to LLM
framework used and the number of subtasks required for each task. The correlation between accuracy and number of
subtasks required is statistically significant, p = 1 × 10−3 for direct LLM and p = 1 × 10−4 MDCrow. The p value
for ReAct is p = 7 × 10−2 .

Figure 6: A. MDCrow simulating annealing. The user directly instructs MDCrow to simulate an annealing simulation
of protein 1L2Y. Once the simulation is complete, the user utilizes the chatting feature to ask for further analyses. B.
RMSD, RGy, and temperature throughout the simulation, as requested by the user in A.

These tasks were focused on routine applications of MD with short simulation runtimes, limited to proteins, common
solvents, and force fields included in the OpenMM package. We did not explore small-molecule force fields, especially
related to ligand binding. Future work could explore multi-modal approaches [70, 71] for tasks like convergence
analysis or plot interpretations. The current framework relies on human-created tools, but as LLM-agent systems
become more autonomous [72], careful evaluation and benchmarking will be essential.

Conclusion

Running and analyzing MD simulations is non-trivial and typically hard to automate. Here, we explored using LLM
agents to accomplish this. We built MDCrow, an LLM and environment consisting of over 40 tools purpose built for
MD simulation and analysis. We found MDCrow could complete 72% of the tasks with the optimal settings (gpt-4o).
llama-405B was able to complete 68%, providing a compelling open-source model. The best models were relatively
robust to how the instructions are given, although weaker models struggle with unstructured instructions. Simply
using an LLM with a python interpreter and required packages installed had a 28% accuracy. The performance of
MDCrow was relatively stable as well, though dependent on the model. Correct assessment of these complex scientific
workflows is challenging, and had to be done by hand. Chatting with the simulations, via extended conversations, is
even more compelling, but is harder to assess.
This work demonstrates the steps to automate and assess computational scientific workflows. As LLMs continue
improving in performance, and better training methods arise for complex tasks like this, we expect LLM agents to
be increasingly important for accelerating science. MDCrow, for example, can now automatically assess hypotheses
with 72% accuracy with simulation and can scale-out to thousands of simultaneous tasks. The code and tasks are open
source and available at https://github.com/ur-whitelab/MDCrow.

Acknowledgments

Research reported in this work was supported by the National Institute of General Medic al Sciences of the National Institutes of Health under award number R35GM137966, National Science Foundation under grant number of 1751471,
Robert L. and Mary L. Sproull Fellowship gift and U.S. Department of Energy, Grant No. DE-SC0023354. Work at
FutureHouse is supported by the generosity of Eric and Wendy Schmidt. We thank the Center for Integrated Research
Computing (CIRC) at University of Rochester for providing computational resources and technical support.

References
[1] Siddharth Sinha, Benjamin Tam, and San Ming Wang. Applications of molecular dynamics simulation in protein
study. Membranes, 12(9):844, August 2022.
[2] Martin Karplus and J Andrew McCammon. Molecular dynamics simulations of biomolecules. nature structural
biology, 9(9), 2002.
[3] Scott A Hollingsworth and Ron O Dror. Molecular dynamics simulation for all. Neuron, 99(6):1129–1143, 2018.
[4] Sameer Velankar, Stephen K Burley, Genji Kurisu, Jeffrey C Hoch, and John L Markley. The protein data bank
archive. Structural Proteomics: High-Throughput Methods, pages 3–21, 2021.
[5] Bernard R Brooks, Charles L Brooks III, Alexander D Mackerell Jr, Lennart Nilsson, Robert J Petrella, Benoı̂t
Roux, Youngdo Won, Georgios Archontis, Christian Bartels, Stefan Boresch, et al. CHARMM: the biomolecular
simulation program. Journal of computational chemistry, 30(10):1545–1614, 2009.
[6] Jay W Ponder and David A Case. Force fields for protein simulations. Advances in protein chemistry, 66:27–85,
2003.
[7] Matthew P. Baumgartner and Hongzhou Zhang. Building admiral, an automated molecular dynamics and analysis
platform. ACS Medicinal Chemistry Letters, 11(11):2331–2335, November 2020.
[8] Yoshihiro Hayashi, Junichiro Shiomi, Junko Morikawa, and Ryo Yoshida. RadonPy: automated physical property calculation using all-atom classical molecular dynamics simulations for polymer informatics. npj Computational Materials, 8(1):222, November 2022.
[9] Harvinder Singh, Anupam Raja, Ajay Prakash, and Bikash Medhi. Gmx qk: An automated protein proteinligand complex simulation workflow bridged to MM PBSA, based on gromacs and zenity-dependent GUI for
beginners in MD simulation study. Journal of Chemical Information and Modeling, 63(9):2603–2608, May
2023.
[10] Gudrun Gygli and Juergen Pleiss. Simulation foundry: Automated and F.A.I.R. molecular modeling. Journal of
Chemical Information and Modeling, 60(4):1922–1927, April 2020.
[11] Abeeb Abiodun Yekeen, Olanrewaju Ayodeji Durojaye, Mukhtar Oluwaseun Idris, Hamdalat Folake Muritala,
and Rotimi Olusanya Arise. CHAPERONg: A tool for automated GROMACS-based molecular dynamics simulations and trajectory analyses. Computational and Structural Biotechnology Journal, 21:4849–4858, 2023.
[12] Eduardo H. B. Maia, Lucas Rolim Medaglia, Alisson Marques Da Silva, and Alex G. Taranto. Molecular architect: A user-friendly workflow for virtual screening. ACS Omega, 5(12):6628–6640, March 2020.
[13] Abir Ganguly, Hsu-Chun Tsai, Mario Fernández-Pendás, Tai-Sung Lee, Timothy J. Giese, and Darrin M. York.
AMBER drug discovery boost tools: Automated workflow for production free-energy simulation setup and analysis (professa). Journal of Chemical Information and Modeling, 62(23):6069–6083, December 2022.
[14] Celso R. C. Rêgo, Jörg Schaarschmidt, Tobias Schlöder, Montserrat Penaloza-Amion, Saientan Bag, Tobias
Neumann, Timo Strunk, and Wolfgang Wenzel. SimStack: An intuitive workflow framework. Frontiers in
Materials, 9:877597, May 2022.
[15] Derek Groen, Agastya P. Bhati, James Suter, James Hetherington, Stefan J. Zasada, and Peter V. Coveney.
FabSim: Facilitating computational research through automation on large-scale and distributed e-infrastructures.
Computer Physics Communications, 207:375–385, October 2016.
[16] Luan Carvalho Martins, Elio A. Cino, and Rafaela Salgado Ferreira. PyAutoFEP: An automated free energy
perturbation workflow for GROMACS integrating enhanced sampling methods. Journal of Chemical Theory
and Computation, 17(7):4262–4273, July 2021.
[17] Miroslav Suruzhon, Tharindu Senapathi, Michael S. Bodnarchuk, Russell Viner, Ian D. Wall, Christopher B.
Barnett, Kevin J. Naidoo, and Jonathan W. Essex. ProtoCaller: Robust automation of binding free energy calculations. Journal of Chemical Information and Modeling, 60(4):1917–1921, April 2020.
[18] Dmitry Suplatov, Yana Sharapova, and Vytas Švedas. EasyAmber: A comprehensive toolbox to automate the molecular dynamics simulation of proteins. Journal of Bioinformatics and Computational Biology,
18(06):2040011, 2020.
[19] Leandro Martı́nez, Ricardo Andrade, Ernesto G Birgin, and José Mario Martı́nez. PACKMOL: A package
for building initial configurations for molecular dynamics simulations. Journal of computational chemistry,
30(13):2157–2164, 2009.

[20] Naveen Michaud-Agrawal, Elizabeth J Denning, Thomas B Woolf, and Oliver Beckstein. MDAnalysis: a toolkit
for the analysis of molecular dynamics simulations. Journal of computational chemistry, 32(10):2319–2327,
2011.
[21] Robert T. McGibbon, Kyle A. Beauchamp, Matthew P. Harrigan, Christoph Klein, Jason M. Swails, Carlos X.
Hernández, Christian R. Schwantes, Lee-Ping Wang, Thomas J. Lane, and Vijay S. Pande. MDTraj: A modern
open library for the analysis of molecular dynamics trajectories. Biophysical Journal, 109(8):1528 – 1532, 2015.
[22] Peter Eastman, Jason Swails, John D Chodera, Robert T McGibbon, Yutong Zhao, Kyle A Beauchamp, Lee-Ping
Wang, Andrew C Simmonett, Matthew P Harrigan, Chaya D Stern, et al. OpenMM 7: Rapid development of
high performance algorithms for molecular dynamics. PLoS computational biology, 13(7):e1005659, 2017.
[23] Mark James Abraham, Teemu Murtola, Roland Schulz, Szilárd Páll, Jeremy C Smith, Berk Hess, and Erik
Lindahl. GROMACS: High performance molecular simulations through multi-level parallelism from laptops to
supercomputers. SoftwareX, 1:19–25, 2015.
[24] A. P. Thompson, H. M. Aktulga, R. Berger, D. S. Bolintineanu, W. M. Brown, P. S. Crozier, P. J. in ’t Veld,
A. Kohlmeyer, S. G. Moore, T. D. Nguyen, R. Shan, M. J. Stevens, J. Tranchida, C. Trott, and S. J. Plimpton.
LAMMPS - a flexible simulation tool for particle-based materials modeling at the atomic, meso, and continuum
scales. Comp. Phys. Comm., 271:108171, 2022.
[25] G Goret, B Aoun, and Eric Pellegrini. MDANSE: An interactive analysis environment for molecular dynamics
simulations. Journal of chemical information and modeling, 57(1):1–5, 2017.
[26] João Vieira Ribeiro, Rafael C Bernardi, Till Rudack, Klaus Schulten, and Emad Tajkhorshid. QwikMD - gateway
for easy simulation with VMD and NAMD. Biophysical Journal, 114(3):673a–674a, 2018.
[27] Victor H Rusu, Vitor AC Horta, Bruno AC Horta, Roberto D Lins, and Riccardo Baron. MDWiZ: a platform for
the automated translation of molecular dynamics simulations. Journal of Molecular Graphics and Modelling,
48:80–86, 2014.
[28] Peter W Hildebrand, Alexander S Rose, and Johanna KS Tiemann. Bringing molecular dynamics simulation
data into view. Trends in Biochemical Sciences, 44(11):902–913, 2019.
[29] Xevi Biarnés, Fabio Pietrucci, Fabrizio Marinelli, and Alessandro Laio. METAGUI. a VMD interface for analyzing metadynamics and molecular dynamics simulations. Computer Physics Communications, 183(1):203–211,
2012.
[30] William Humphrey, Andrew Dalke, and Klaus Schulten. VMD: visual molecular dynamics. Journal of molecular
graphics, 14(1):33–38, 1996.
[31] Diamantis Sellis, Dimitrios Vlachakis, and Metaxia Vlassi. Gromita: a fully integrated graphical user interface
to gromacs 4. Bioinformatics and biology insights, 3:BBI–S3207, 2009.
[32] Gerard Martı́nez-Rosell, Toni Giorgino, and Gianni De Fabritiis. PlayMolecule ProteinPrepare: a web application for protein preparation for molecular dynamics simulations. Journal of chemical information and modeling,
57(7):1511–1516, 2017.
[33] Timo Schick, Jane Dwivedi-Yu, Roberto Dessı̀, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola
Cancedda, and Thomas Scialom. Toolformer: Language models can teach themselves to use tools. arXiv preprint
arXiv:2302.04761, 2023.
[34] Ehud Karpas, Omri Abend, Yonatan Belinkov, Barak Lenz, Opher Lieber, Nir Ratner, Yoav Shoham, Hofit Bata,
Yoav Levine, Kevin Leyton-Brown, et al. MRKL systems: A modular, neuro-symbolic architecture that combines
large language models, external knowledge sources and discrete reasoning. arXiv preprint arXiv:2205.00445,
2022.
[35] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. ReAct:
Synergizing reasoning and acting in language models. arXiv preprint arXiv:2210.03629, 2022.
[36] Siddharth Narayanan, James D Braza, Ryan-Rhys Griffiths, Manu Ponnapati, Albert Bou, Jon Laurent, Ori
Kabeli, Geemi Wellawatte, Sam Cox, Samuel G Rodriques, et al. Aviary: training language agents on challenging
scientific tasks. arXiv preprint arXiv:2412.21154, 2024.
[37] Renqian Luo, Liai Sun, Yingce Xia, Tao Qin, Sheng Zhang, Hoifung Poon, and Tie-Yan Liu. BioGPT: generative
pre-trained transformer for biomedical text generation and mining. Briefings in bioinformatics, 23(6):bbac409,
2022.
[38] Karan Singhal, Shekoofeh Azizi, Tao Tu, S Sara Mahdavi, Jason Wei, Hyung Won Chung, Nathan Scales, Ajay
Tanwani, Heather Cole-Lewis, Stephen Pfohl, et al. Large language models encode clinical knowledge. Nature,
620(7972):172–180, 2023.

[39] Shanghua Gao, Ada Fang, Yepeng Huang, Valentina Giunchiglia, Ayush Noori, Jonathan Richard Schwarz,
Yasha Ektefaie, Jovana Kondic, and Marinka Zitnik. Empowering biomedical discovery with AI agents. Cell,
187:6125–6151, Oct 2024.
[40] Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D White, and Philippe Schwaller. Augmenting large language models with chemistry tools. Nature Machine Intelligence, pages 1–11, 2024.
[41] Daniil A Boiko, Robert MacKnight, Ben Kline, and Gabe Gomes. Autonomous chemical research with large
language models. Nature, 624(7992):570–578, 2023.
[42] Juan Luis Villarreal-Haro, Remy Gardier, Erick J Canales-Rodriguez, Elda Fischi Gomez, Gabriel Girard, JeanPhilippe Thiran, and Jonathan Rafael-Patino. CACTUS: A computational framework for generating realistic
white matter microstructure substrates, 2023.
[43] Kevin Maik Jablonka, Qianxiang Ai, Alexander Al-Feghali, Shruti Badhwar, Joshua D Bocarsly, Andres M Bran,
Stefan Bringuier, L Catherine Brinson, Kamal Choudhary, Defne Circi, et al. 14 examples of how LLMs can
transform materials science and chemistry: a reflection on a large language model hackathon. Digital Discovery,
2(5):1233–1250, 2023.
[44] Yuming Su, Xue Wang, Yuanxiang Ye, Yibo Xie, Yujing Xu, Yibing Jiang, and Cheng Wang. Automation and
machine learning augmented by large language models in catalysis study. Chemical Science, 2024.
[45] Yuan Chiang, Chia-Hong Chou, and Janosh Riebesell. LLaMP: Large language model made powerful for highfidelity materials knowledge retrieval and distillation. arXiv preprint arXiv:2401.17244, 2024.
[46] Seongmin Kim, Yousung Jung, and Joshua Schrier. Large language models for inorganic synthesis predictions.
Journal of the American Chemical Society, 2024.
[47] Wonseok Lee, Yeonghun Kang, Taeun Bae, and Jihan Kim. Harnessing large language model to collect and
analyze metal-organic framework property dataset. arXiv preprint arXiv:2404.13053, 2024.
[48] Michael D Skarlinski, Sam Cox, Jon M Laurent, James D Braza, Michaela Hinks, Michael J Hammerling,
Manvitha Ponnapati, Samuel G Rodriques, and Andrew D White. Language agents achieve superhuman synthesis
of scientific knowledge. arXiv preprint arXiv:2409.13740, 2024.
[49] Michael H. Prince, Henry Chan, Aikaterini Vriza, Tao Zhou, Varuni K. Sastry, Matthew T. Dearing, Ross J.
Harder, Rama K. Vasudevan, and Mathew J. Cherukara. Opportunities for retrieval and tool augmented large
language models in scientific facilities, 2023.
[50] Odhran O’Donoghue, Aleksandar Shtedritski, John Ginger, Ralph Abboud, Ali Essa Ghareeb, Justin Booth, and
Samuel G Rodriques. Bioplanner: Automatic evaluation of llms on protocol planning in biology, 2023.
[51] Kaixuan Huang, Yuanhao Qu, Henry Cousins, William A. Johnson, Di Yin, Mihir Shah, Denny Zhou, Russ
Altman, Mengdi Wang, and Le Cong. CRISPR-GPT: An LLM agent for automated design of gene-editing
experiments, 2024.
[52] Yixiang Ruan, Chenyin Lu, Ning Xu, Jian Zhang, Jun Xuan, Jianzhang Pan, Qun Fang, Hanyu Gao, Xiaodong
Shen, Ning Ye, and et al. Accelerated end-to-end chemical synthesis development with large language models.
ChemRxiv, 2024.
[53] Yeonghun Kang and Jihan Kim. ChatMOF: an artificial intelligence system for predicting and generating metalorganic frameworks using large language models. Nature Communications, 15(1):4705, June 2024.
[54] Tianyidan Xie, Rui Ma, Qian Wang, Xiaoqian Ye, Feixuan Liu, Ying Tai, Zhenyu Zhang, and Zili Yi. Anywhere:
A multi-agent framework for reliable and diverse foreground-conditioned image inpainting, 2024.
[55] A. Ghafarollahi and M. J. Buehler. ProtAgents: Protein discovery via large language model multi-agent collaborations combining physics and machine learning, 2024.
[56] Mayk Caldas Ramos, Christopher J Collison, and Andrew D White. A review of large language models and
autonomous agents in chemistry. Chemical Science, 2025.
[57] Harrison Chase. LangChain, 10 2022.
[58] The UniProt Consortium. UniProt: the Universal Protein Knowledgebase in 2023. Nucleic Acids Research,
51(D1):D523–D531, 11 2022.
[59] Molstar Developers. molrender. https://github.com/molstar/molrender, 2019. Accessed: 2025-02-10.
[60] Hai Nguyen, David A Case, and Alexander S Rose. NGLview–interactive molecular graphics for Jupyter notebooks. Bioinformatics, 34(7):1241–1242, 2018.

[61] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models to follow instructions with human
feedback. Advances in neural information processing systems, 35:27730–27744, 2022.
[62] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo
Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. GPT-4 technical report. arXiv preprint
arXiv:2303.08774, 2023.
[63] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The Llama 3 herd of models. arXiv preprint
arXiv:2407.21783, 2024.
[64] Fireworks AI, Inc. [Accessed 24-01-2025].
[65] www-cdn.anthropic.com. https://www-cdn.anthropic.com/fed9cc193a14b84131812372d8d5857f8f304c52/
Model_Card_Claude_3_Addendum.pdf. [Accessed 10-01-2025].
[66] Anthropic. The Claude 3 model family: Opus, Sonnet, Haiku, Mar 2024.
[67] Aaron Jaech, Adam Kalai, Adam Lerer, Adam Richardson, Ahmed El-Kishky, Aiden Low, Alec Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. OpenAI o1 system card. arXiv preprint arXiv:2412.16720,
2024.
[68] Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila
Welihinda, Alan Hayes, Alec Radford, et al. GPT-4o system card. arXiv preprint arXiv:2410.21276, 2024.
[69] Jon M Laurent, Joseph D Janizek, Michael Ruzo, Michaela M Hinks, Michael J Hammerling, Siddharth
Narayanan, Manvitha Ponnapati, Andrew D White, and Samuel G Rodriques. LAB-Bench: Measuring capabilities of language models for biology research. arXiv preprint arXiv:2407.10362, 2024.
[70] Chenyu Wang, Weixin Luo, Qianyu Chen, Haonan Mai, Jindi Guo, Sixun Dong, Xiaohua, Xuan, Zhengxin Li,
Lin Ma, and Shenghua Gao. MLLM-Tool: A multimodal large language model for tool agent learning, 2024.
[71] Difei Gao, Lei Ji, Luowei Zhou, Kevin Qinghong Lin, Joya Chen, Zihan Fan, and Mike Zheng Shou. AssistGPT:
A general multi-modal assistant that can plan, execute, inspect, and learn, 2023.
[72] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and Anima Anandkumar. Voyager: An open-ended embodied agent with large language models. arXiv preprint
arXiv:2305.16291, 2023.

Supplemental Information
A

Claude-Specific Engineering

While both of Claude’s Sonnet models achieved poor performance during the robustness experiment, it can be noted
that a single common error arose consistently. When running an NPT simulation, MDCrow requires that all parameters
be passed to the simulation tool. However, both Sonnet models consistently neglected to provide a value for pressure,
even when directly prompted to do so. The claude-3-opus made this mistake a single time. This is a relatively
simple fix, providing MDCrow with a default pressure of 1 atm when no pressure is passed.

Figure 7: Performance of MDCrow with three Claude models on 10 tasks. As the number of subtasks increase, we
all subtasks completed for both prompt types. The top row shows MDCrow’s performance as-is, and the bottom row
shows MDCrow’s performance when given a direct fix for missing parameters. There is a clear change in performance
after the fix for both claude-3.5-sonnet-20241022 and claude-3.5-sonnet-20240620.

As can be seen in Figure 7, including this fix drastically improves the performance of these models, with performance
comparable to the top models. However, no other models made this mistake, and no other model-specific optimization
was conducted. Thus, for all experiments shown in this paper, MDCrow does not accommodate this Claude-specific
missing parameter fix.

B

Prompts

MDCrow Prompt
solve the problem to the best of your ability using the provided tools.
You can only respond with a single complete ’Thought, Action, Action Input’ format OR a single
’Final Answer’ format.
Complete format:
Thought: (reflect on your progress and decide what to do next)
Action:
{{
"action": (the action name, it should be the name of a tool),
"action_input": (the input string for the action)
}}
OR
Final Answer: (the final response to the original input
question, once all steps are complete)
You are required to use the tools provided, using the most specific tool available for each
action. Your final answer should contain all information necessary to answer the question and its
subquestions. Before you finish, reflect on your progress and make sure you have addressed the
question in its entirety.
If you are asked to continue or reference previous runs, the context will be provided to you. If
context is provided, you should assume you are continuing a chat.
Here is the input:
Previous Context: {context}
Question: {input}

During the comparison study between MDCrow, GPT-only, and ReAct with Python REPL tool, we used different
system prompts for each of these LLM frameworks.
Direct-LLM Prompt
solve the problem in its entirety to the best of your ability. If any part of the task requires
you to perform an action that you are not capable of completing, please write a runnable Python
script for that step and move on. For literature papers, use and process papers from the
‘paper_collection‘ folder. For .pdb files, download them from the RSCB website using ‘requests‘.
To preprocess PDB files, you will use PDBFixer. To get information about proteins, retrieve data
from the UniProt database. For anything related to simulations, you will use OpenMM, and for
anything related to analyses, you will use MDTraj. At the end, combine any scripts into one script.

ReAct Agent Prompt
solve the problem to the best of your ability. If any part of the task requires you to perform an
action that you are not capable of completing, please write a runnable Python script for that step
and run it. For literature papers, use and process papers from the ‘paper_collection’ folder. For
.pdb files, download them from the RSCB website using ‘requests‘. TO preprocess PDB files, you
will use PDBFixer. To get information about proteins, retrieve data from the UniProt database. For
anything related to simulations, you will use OpenMM, and for anything related to analyzes, you
will use MDTraj.
You can only respond with a single complete ’Thought, Action, Action Input’ format OR a single
’Final Answer’ format.
Complete format:
Thought: (reflect on your progress and decide what to do next)
Action:
{{
"action": (the action name, it should be the name of a tool),
"action_input": (the input string for the action)
}}
OR
Final Answer: (the final response to the original input
question, once all steps are complete)
You are required to use the tools provided,
using the most specific tool available for each action. Your final answer should contain all
information necessary to answer the question and its subquestions. Before you finish, reflect on
your progress and make sure you have addressed the question in its entirety.
Here is the input:
Question: {input}

C

Task Prompts & References Used in Experiments

Table 1: Details of 25 task prompts used in experiments
Prompt ID

Prompt

Simulate PDB ID 1MBN at two different temperatures: 300 K and 400
K for 1 ns each. Plot the RMSD of both over time and compare the final
secondary structures at the end of the simulations. Get information
about this protein, such as the number of residues and chains, etc.
Download the PDB file for protein 1LYZ.
Download the PDB file for protein 1GZX. Then, analyze the secondary
structure of the protein and provide information on how many helices,
sheets, and other components are present. Get the gene names for this
protein.
What are the common parameters used to simulate fibronectin?
Simulate 1VII for 1 ns at a temperature of 300 K. Then, tell me if the
secondary structure changed from the beginning of the simulation to
the end of the simulation.
Simulate 1A3N and 7VDE (two PDB IDs matching hemoglobin) with
identical parameters. Find the appropriate parameters for simulating hemoglobin from the literature. Then, plot the radius of gyration
throughout both simulations.
Simulate 1ZNI for 1 ns at a temperature of 300 K in water. Then,
simulate it again in acetonitrile. Compute the RMSD, final secondary
structure, and PCA for each simulation.
Simulate 4RMB at 100K, 200K, and 300K. Then, for each simulation,
plot the radius of gyration over time and compare the secondary structure before and after the simulation.
Download the PDB file for 1AEE. Then tell me how many chains and
atoms are present in the protein.
Simulate protein 1ZNI at 300 K for 1 ns and calculate the RMSD.

#
subtasks

List of required subtasks

Download PDB
Download PDB, DSSP, GetProteinFunction (or literature)

literature search
DSSP before, DSSP after,
comparison
Download PDB (x2), literature, simulate (x2), RGy (x2)

Download the PDB files for 8PFK and 8PFQ. Then, compare the secondary structures of the two proteins, including the number of atoms,
secondary structures, number of chains, etc.
Simulate fibronectin (PDB ID 1FNF) for 1 ns, using an appropriate
temperature found in the literature. Compute the RMSD and the final
secondary structure. By using the PDB ID to get the Uniprot ID, obtain the subunit structure and the number of beta sheets, helices, etc.
Compare this information to the structure we computed.
Compare the RMSF of 1UBQ under high pressure and low pressure.
Perform the simulation for 1 ns, varying only the pressure. Plot the
moments of inertia over time for both simulations.
Simulate deoxygenated hemoglobin (1A3N) and oxygenated
hemoglobin (6BB5). Plot the PCA of both trajectories.
Simulate trypsin (1TRN) for 1 ns at 300 K and plot eneRGy over time.
Compute SASA, RMSF, and radius of gyration. Get the subunit structure, sequence, active and binding sites.

Download the PDB file for 1C3W and describe the secondary structure.
Then, simulate the protein at 300 K for 1 ns. Plot the RMSD over time
and the radius of gyration over time.
Download the PDB file for 1XQ8, and then save the visualization for
it.
Download the PDB for 2YXF. Tell me about its stability as found in
the literature. Then, simulate it for 1 ns and plot its RMSD over time.

(x2), RMSD (x2), DSSP
(x2), summarize protein

(x2), packmol, RMSD (x2),
SASA (x2), PCA (x2)
(x3), RGy (x3), DSSP (x3)
download PDB, count atoms/chains
RMSD
Download PDB (x2), DSSP
(x2)

Download PDB, literature,
simulate, RMSD, DSSP, get
uniprot, subunit structure, get
beta sheets/helices

(x2), RMSF (x2), MOI (x2)

Download PDB (x2), simulate (x2), PCA (x2)
output
figures,
SASA,
RMSF, RGy, subunit structure, sequence info, all
known sites
Download PDB, DSSP, simulate, RMSD, RGy

Download PDB, visualize

Download PDB, literature
search, simulate, RMSD

Prompt ID

Prompt

Simulate 1MBN in water and methanol solutions.

#
subtasks

Download protein 1ATN.
Download and clean protein 1A3N.
Perform a brief simulation of protein 1PQ2.
Analyze the RDF of the simulation of 1A3N solvated in water.

Simulate oxygenated hemoglobin (1A3N) and deoxygenated
hemoglobin (6BB5). Then analyze the RDF of both.
Simulate 1L6X at pH 5.0 and 8.8, then analyze the SASA and RMSF
under both pH conditions.

List of required subtasks
Download PDB, packmol to
get appropriate non-water
solvent, simulate (x2)
Download PDB
Download PDB, clean
RDF
Download PDB (x2), simulate (x2), RDF (x2)
Download PDB, clean at pH
5.5 and 8.0, simulate(x2),
SASA(x2), RMSF(x2)

List of References Used for Literature Search During the Experiments.
1. The folding space of protein β2-microglobulin is modulated by a single disulfide bridge, 10.1088/
1478-3975/ac08ec
2. Molecular Dynamics Simulation of the Adsorption of a Fibronectin Module on a Graphite Surface, 10.1021/
la0357716
3. Predicting stable binding modes from simulated dimers of the D76N mutant of β2-microglobulin, 10.1016/
j.csbj.2021.09.003
4. Deciphering the Inhibition Mechanism of under Trial Hsp90 Inhibitors and Their Analogues: A Comparative
Molecular Dynamics Simulation, 10.1021/acs.jcim.9b01134
5. Molecular modeling, simulation and docking of Rv1250 protein from Mycobacterium tuberculosis, 10.
3389/fbinf.2023.1125479
6. Molecular Dynamics Simulation of Rap1 Myb-type domain in Saccharomyces cerevisiae, 10.6026/
97320630008881
7. A Giant Extracellular Matrix Binding Protein of Staphylococcus epidermidis Binds Surface-Immobilized
Fibronectin via a Novel Mechanism, 10.1128/mbio.01612-20
8. High Affinity vs. Native Fibronectin in the Modulation of αvβ3 Integrin Conformational Dynamics: Insights
from Computational Analyses and Implications for Molecular Design, 10.1371/journal.pcbi.1005334
9. Forced unfolding of fibronectin type 3 modules: an analysis by biased molecular dynamics simulations,
10.1006/jmbi.1999.2670
10. Adsorption of Fibronectin Fragment on Surfaces Using Fully Atomistic Molecular Dynamics Simulations,
10.3390/ijms19113321
11. Fibronectin Unfolding Revisited: Modeling Cell Traction-Mediated Unfolding of the Tenth Type-III Repeat,
10.1371/journal.pone.0002373
12. Tertiary and quaternary structural basis of oxygen affinity in human hemoglobin as revealed by multiscale
simulations, 10.1038/s41598-017-11259-0
13. Oxygen Delivery from Red Cells, 10.1016/s0006-3495(85)83890-x
14. Molecular Dynamics Simulations of Hemoglobin A in Different States and Bound to DPG: Effector-Linked
Perturbation of Tertiary Conformations and HbA Concerted Dynamics, 10.1529/biophysj.107.114942
15. Theoretical Simulation of Red Cell Sickling Upon Deoxygenation Based on the Physical Chemistry of Sickle
Hemoglobin Fiber Formation, 10.1021/acs.jpcb.8b07638
16. Adsorption of Heparin-Binding Fragments of Fibronectin onto Hydrophobic Surfaces, 10.3390/
biophysica3030027
17. Mechanistic insights into the adsorption and bioactivity of fibronectin on surfaces with varying chemistries by
a combination of experimental strategies and molecular simulations, 10.1016/j.bioactmat.2021.02.021
18. Anti-Inflammatory, Radical Scavenging Mechanism of New 4-Aryl-[1,3]-thiazol-2-yl-2-quinoline Carbohydrazides and Quinolinyl[1,3]-thiazolo[3,2-b][1,2,4]triazoles, 10.1002/slct.201801398
19. Trypsin-Ligand binding affinities calculated using an effective interaction entropy method under polarized
force field, 10.1038/s41598-017-17868-z
20. Ubiquitin: Molecular modeling and simulations, 10.1016/j.jmgm.2013.09.006
21. Valid molecular dynamics simulations of human hemoglobin require a surprisingly large box size, 10.7554/
eLife.35560
22. Multiple Cryptic Binding Sites are Necessary for Robust Fibronectin Assembly: An In Silico Study, 10.
1038/s41598-017-18328-4
23. Computer simulations of fibronectin adsorption on hydroxyapatite surfaces, 10.1039/c3ra47381c
24. An Atomistic View on Human Hemoglobin Carbon Monoxide Migration Processes, 10.1016/j.bpj.2012.
01.011
25. Best Practices for Foundations in Molecular Simulations [v1.0], 10.33011/livecoms.1.1.5957
26. Unfolding Dynamics of Ubiquitin from Constant Force MD Simulation: Entropy-Enthalpy Interplay Shapes
the Free-Energy Landscape, 10.1021/acs.jpcb.8b09318
27. Dissecting Structural Aspects of Protein Stability
28. MACE Release 0.1.0 Documentation
