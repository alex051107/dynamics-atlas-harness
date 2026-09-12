# Augmenting large language models with chemistry tools

**Authors:** Andres M. Bran, Sam Cox, Oliver Schilter, Carlo Baldassari, Andrew D. White, Philippe Schwaller
**Year:** 2024
**Venue:** Nature Machine Intelligence
**DOI:** 10.1038/s42256-024-00832-8
**Source PDF URL:** https://www.nature.com/articles/s42256-024-00832-8.pdf
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

nature machine intelligence

Article                                                                                               https://doi.org/10.1038/s42256-024-00832-8


Augmenting large language models with
chemistry tools

Received: 13 September 2023                         Andres M. Bran1,2,6, Sam Cox3,4,6, Oliver Schilter 1,2,5, Carlo Baldassari5,
                                                    Andrew D. White 3,4 & Philippe Schwaller 1,2
Accepted: 27 March 2024

Published online: 8 May 2024
                                                    Large language models (LLMs) have shown strong performance in
   Check for updates                                tasks across domains but struggle with chemistry-related problems.
                                                    These models also lack access to external knowledge sources, limiting
                                                    their usefulness in scientific applications. We introduce ChemCrow,
                                                    an LLM chemistry agent designed to accomplish tasks across organic
                                                    synthesis, drug discovery and materials design. By integrating 18
                                                    expert-designed tools and using GPT-4 as the LLM, ChemCrow augments
                                                    the LLM performance in chemistry, and new capabilities emerge. Our
                                                    agent autonomously planned and executed the syntheses of an insect
                                                    repellent and three organocatalysts and guided the discovery of a novel
                                                    chromophore. Our evaluation, including both LLM and expert assessments,
                                                    demonstrates ChemCrow’s effectiveness in automating a diverse set of
                                                    chemical tasks. Our work not only aids expert chemists and lowers barriers
                                                    for non-experts but also fosters scientific advancement by bridging the gap
                                                    between experimental and computational chemistry.


In the last few years, large language models (LLMs)1–5 have transformed       These specialized tools provide exact answers, thereby compensating
various sectors by automating natural language tasks. A prime example         for the inherent deficiencies of LLMs in specific domains and enhancing
of this is the introduction of GitHub Copilot in 20216 and more recently      their overall performance and applicability.
StarCoder7, which provides proposed code completions based on the                  Chemistry, as a field, has been impacted through expert-designed
context of a file and open windows and increases developers’ productiv-       artificial intelligence (AI) systems that tackle specific problems, such
ity8. Most recent advances are based on the Transformer architecture9,        as reaction prediction16–20, retrosynthesis planning21–27, molecular
introduced for neural machine translation and extended to various             property prediction28–32, de novo molecular generation33,34, materials
natural language processing tasks demonstrating remarkable few-shot           design35,36 and, more recently, Bayesian optimization37–39. Due to the
and zero-shot performance2. Nevertheless, it is crucial to recognize the      nature of their training data, it has been shown that code-generating
limitations of LLMs, which often struggle with seemingly simple tasks         LLMs do possess some understanding of chemistry14, allowing them
like basic mathematics and chemistry operations10,11. For instance,           to adapt to observations, plan over multiple steps and respond cor-
GPT-4 (ref. 12) and GPT-3.5 (ref. 13) cannot consistently and accurately      rectly to intent in a chemical setting13,40–44. Still, the automation lev-
multiply 12,345 × 98,765 or convert IUPAC names into the correspond-          els achieved in chemistry remain relatively low compared to other
ing molecular graph14. These shortcomings can be attributed to the            domains, primarily due to its highly experimental nature, the lack of
models’ core design, which focuses on predicting subsequent tokens.           data and the limited scope and applicability of computational tools,
To address these limitations, one viable approach is to augment LLMs          even within their designated areas45.
with dedicated external tools or plugins, such as a calculator for math-           Integrating such tools tends to occur within isolated environ-
ematical operations or OPSIN15 for IUPAC-to-structure conversion.             ments, such as RXN for Chemistry18,24,46–48 and AIZynthFinder25,49,50,


1
 Laboratory of Artificial Chemical Intelligence (LIAC), ISIC, EPFL, Lausanne, Switzerland. 2National Centre of Competence in Research (NCCR) Catalysis,
EPFL, Lausanne, Switzerland. 3Department of Chemical Engineering, University of Rochester, Rochester, NY, USA. 4FutureHouse, San Francisco,
CA, USA. 5Accelerated Discovery, IBM Research – Europe, Rüschlikon, Switzerland. 6These authors contributed equally: Andres M. Bran, Sam Cox.
   e-mail: andrew@futurehouse.org; philippe.schwaller@epfl.ch


Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                                          525
Article                                                                                                            https://doi.org/10.1038/s42256-024-00832-8


                         a                                            Chain of thought reasoning loop
                              Expert-designed                                                                             Chemistry-informed
                              chemistry tools                                                                             sequence of actions
                                                           1. Thought:                              2. Action:
                                                           reason, plan                            select tool       1. Google search
                                                                                                                     2. Retrosynthesis
                                                                                                                     3. Procedure prediction
                                                                                                                     4. Execution on robot
                                                                               ChemCrow
                             Example input:
                                                                                                                     Synthesis of
                             Plan and execute
                                                                                                                     DEET without
                             the synthesis of an
                                                                                                                     human
                             insect repellent.             4. Observation:                           3. Action       interaction.
                                                           analyze                              input: use tool
                             User-defined                                                                                          Autonomous
                             scientific tasks                                                                                   experimentation
                                                                  Autonomous interaction with tools and
                                                                the physical world (for example, RoboRXN)
                         b Molecule tools                                                                                            General tools

                                                • SMILES to weight                                      • Literature search
                                                • SMILES to price                                       • Web search
                                                • SMILES to CAS                                         • Code interpreter
                                     O
                                                • Similarity                                            • Human expert
                                                • Modify molecule
                                         N
                                                • Functional groups
                                                • Patent check                                          • RXN to name            O
                                                • Name to SMILES                                        • RXN predict                N          ?
                                                • Safety assessment                                     • Synthesis plan
                                                • Explosive check                                       • Synthesis execute

                             Safety tools                                                                                           Reaction tools

Fig. 1 | Overview and toolset. a, An overview of the task-solving process. Using      choice of tools and inputs before coming to a final answer. The example shows
a variety of chemistry-related packages and software, a set of tools is created.      the synthesis of DEET, a common insect repellent. b, Toolsets implemented
These tools and a user input are then given to an LLM. The LLM proceeds               in ChemCrow: reaction, molecule, safety, search and standard tools. Credit:
through an automatic, iterative chain-of-thought process, deciding on its path,       photograph in a, IBM Research under a creative commons license CC BY-ND 2.0.



facilitated by corporate directives that promote integrability. Although              additional information, observe the tool’s responses and repeat this
most tools are developed by the open-source community or made                         loop until the final answer is reached. Contemporaneously with this
accessible through application programming interfaces (APIs), their                   work, ref. 54 describes a similar approach of augmenting an LLM with
integration and interoperability pose considerable challenges for                     tools for accomplishing tasks in chemistry that are out of reach of GPT-4
experimental chemists, mainly due to their lack of computational                      alone. Its focus is specifically on cloud labs, whereas we investigate
skill sets and the diversity of tools with steep learning curves, thereby             an extensive range of tasks and tools including the connection to a
preventing the full exploitation of their potential.                                  cloud-connected robotic synthesis platform. We implemented 18 tools,
      Inspired by successful applications in other fields10,51,52, we propose         as shown in Fig. 1b and described in ‘Tools’, that endow ChemCrow
an LLM-powered chemistry engine, ChemCrow, designed to streamline                     not only with knowledge about molecular and reaction properties
the reasoning process for various common chemical tasks across areas                  but also with the capacity to directly execute tasks in a physical lab.
such as drug and materials design and synthesis. ChemCrow harnesses                   Although the list of tools included is not exhaustive, ChemCrow has
the power of multiple expert-designed tools for chemistry and operates                been designed to be easily adapted to new applications by providing
by prompting a LLM (GPT-4 in our experiments) with specific instruc-                  new tools. ChemCrow serves as an assistant to expert chemists while
tions about the task and the desired format, as shown in Fig. 1a. The                 simultaneously lowering the entry barrier for non-experts by offering a
LLM is provided with a list of tool names, descriptions of their utility              simple interface to access accurate chemical knowledge. We analyse the
and details about the expected input/output. It is then instructed to                 capabilities of ChemCrow on 14 use cases (Appendix G in the Supple-
answer a user-given prompt, using the tools provided when neces-                      mentary Information), including synthesizing target molecules, safety
sary. The model is guided to follow the Thought, Action, Action Input,                controls and searching for molecules with similar modes of action.
Observation format43, which requires it to reason about the current
state of the task, consider its relevance to the final goal and plan the next         Results and discussion
steps accordingly, demonstrating its level of understanding. After the                Autonomous chemical synthesis
reasoning in the Thought step, the LLM requests a tool (preceded by the               From user inputs such as ‘Plan and execute the synthesis of an insect
keyword ‘Action’) and the input for this tool (with the keyword ‘Action               repellent’ (Fig. 1a) and ‘Find a thiourea organocatalyst which acceler-
Input’). The text generation then pauses, and the program attempts to                 ates the Diels-Alder reaction. After you find it, please plan and execute
execute the requested function using the provided input. The result is                a synthesis for this organocatalyst’ (Fig. 2b), ChemCrow sequentially
returned to the LLM prepended by the keyword ‘Observation’, and the                   queried tools to find appropriate molecules, planned the syntheses
LLM proceeds to the Thought step again. It continues iteratively until                and executed the syntheses on the cloud-connected, proprietary
the final answer is reached.                                                          RoboRXN platform from IBM Research55. Using RoboRXN, Chem-
      This workflow, previously described in the ReAct43 and MRKL53                   Crow autonomously ran the syntheses of an insect repellent (DEET)
papers, effectively combines chain-of-thought reasoning with tools                    and three known thiourea organocatalysts (Schreiner’s56,57, Ricci’s58
relevant to the tasks. As a result, and as will be shown in the follow-               and Takemoto’s59). The synthesized structures are shown in Fig. 2d
ing sections, the LLM transitions from a hyperconfident—although                      and the detailed description of the tools in ‘Tools’. The four synthe-
typically wrong—information source to a reasoning engine that                         ses yielded the anticipated compounds successfully, demonstrating
is prompted to reflect on a task, act using a suitable tool to gather                 synthesis planning and execution-related LLM agent interactions with


Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                                                     526
Article                                                                                                                                                          https://doi.org/10.1038/s42256-024-00832-8


a                                                                                 b Task: Find and synthesize a thiourea organocatalyst which                                          c RoboRXN synthesis platform
                                                                                      accelerates a Diels-Alder reaction.



                                                                                      suitable catalyst.
                                                                                      Web Search tool: Schreiner′s thiourea catalyst

                                                                                      Now, I will obtain the SMILES. Name2Smiles tool:
                                                                                      FC(F)(F)c1cc(NC(=S)Nc2cc(C(F)(F)F)cc(C(F)(F)F)c2)cc(C(F)(F)F)c1

                                                                                      I will plan a synthesis for Schreiner′s thiourea catalyst.
                                                                                      SynthesisPlanner tool: detailed synthesis plan
                                                                                                                                                            Connection with
                                                                                      I will execute the synthesis.                                         physical world
                                                                                      SynthesisExecuter tool: successful synthesis.

d ChemCrow workflows with experimental validation
    Insect repellent (plan and execute)                                           DEET                                              Novel chromophore (clean data, train model and predict)
                              O                                                       O                                                                          OH
                                                                                                                                                                       H       O                          H
                                                                                                                                                                 B     N                                           O
                                           +           N                                                                                                +                                                 N
                                  Cl                                                      N                                                                 HO             S                                   S
                                                       H
                                                                                                                                                   Br                  O                                   O


    Thiourea organocatalysts (plan and execute)                                                                                     Synthesis step 1: Bromo Suzuki coupling
          Schreiner’s catalyst                             Ricci’s catalyst                     Takemoto’s catalyst                                                                               O

                  F                        F                                  F                                    F
              F       F                F       F                          F       F                            F       F                 O                                                    O
                                                                                                                                                                       H           O
                                                                                                                                     O             +                   N
                                                                 S                                                                                                             S
                              S                                                                        S                                                                                                               H       O
                                                                                                                                                                           O                                           N
      F                                                F                                  F                                    F               I                                                                           S
                                                            HN       N                             N       N
                          N       N                                  H                                                                                                                                                 O
      F                   H       H                    F                                  F        H       H                   F
          F                                        F                 OH               F        N                           F
                                                                                                                                    Synthesis step 2: Iodo Heck reaction

Fig. 2 | Experimental validation. a, Example of the script run by a user to                                                        (pictures reprinted courtesy of International Business Machines Corporation).
initiate ChemCrow. b, Query and synthesis of a thiourea organocatalyst. c, IBM                                                     d, Experimentally validated compounds. Credit: photographs in c, IBM Research
Research RoboRXN synthesis platform on which the experiments were executed                                                         under a creative commons license CC BY-ND 2.0.




the physical world. It should be noted that one could use these tools                                                              Evaluation across diverse chemical use cases
individually, provided they had access, with likely the same result.                                                               In recent years, there has been a surge in the application of machine
ChemCrow automates the execution of these tools by harnessing the                                                                  learning to chemistry, resulting in a wealth of datasets and benchmarks
reasoning abilities of LLMs.                                                                                                       in the field61,62. However, few of these benchmarks focus on assessing
     Standardized synthesis procedures are key for successful execu-                                                               LLMs for tasks specific to chemistry, and given the rapid pace of pro-
tion. However, the predicted procedures46 are not always directly                                                                  gress, a standardized evaluation technique has not yet been established,
executable on the RoboRXN platform; typical problems include ‘not                                                                  posing a challenge in assessing the approach we demonstrate here. To
enough solvent’ or ‘invalid purify action’. Although addressing these                                                              address this issue, we collaborated with expert chemists to develop a
issues typically requires human interaction to fix the invalid actions                                                             set of tasks that test the capabilities of LLMs in using chemistry-specific
before attempting to execute the synthesis, ChemCrow is able to auton-                                                             tools and solving problems in the field. The selected tasks are executed
omously query the synthesis validation data from the platform and                                                                  by both ChemCrow and GPT-4, and these results are evaluated with a
iteratively adapt the synthesis procedure (such as increasing solvent                                                              combination of LLM-based and expert human assessments. GPT-4 is
quantity) until the synthesis procedure is fully valid, thereby remov-                                                             prompted to assume the role of an expert chemist but has no access
ing the need for human intervention. This example demonstrates                                                                     to external tools such as internet browsing. For the LLM-based assess-
ChemCrow’s abilities to autonomously adapt and successfully execute                                                                ments, we draw inspiration from the evaluation methods described in
standardized synthesis procedures, alleviating lab safety concerns and                                                             refs. 5,63,64, where the authors use an evaluator LLM that is instructed
adapting itself to the particular conditions of the robotic platform.                                                              to assume the role of a teacher assessing their students. In our case, we
                                                                                                                                   adapted the prompt so that the evaluator LLM (which we call Evalu-
Human–AI collaboration                                                                                                             atorGPT) gives a grade based only on whether the task is addressed
Collaboration between humans and computers is valuable, espe-                                                                      and whether the overall thought process is correct. EvaluatorGPT is
cially in the realm of chemistry, where decisions are often based on                                                               further instructed to highlight the strengths and weaknesses of each
experimental results. Here we demonstrate how such an interaction                                                                  approach and to provide further feedback on how each response could
can lead to the discovery of a novel chromophore. For this example,                                                                improve, providing ground to explain the LLM’s evaluations. Full results
ChemCrow was instructed to train a machine-learning model to help                                                                  for several tasks, spanning synthetic planning for drugs, design of
screen a library of candidate chromophores60. As can be seen in Fig. 3,                                                            novel compounds with similar properties and modes of actions and
ChemCrow is capable of loading, cleaning and processing the data;                                                                  explaining reaction mechanisms, are presented in Appendix G of the
training and evaluating a random forest model (Appendix G.1 in the                                                                 Supplementary Information. The full examples are also available at
Supplementary Information); and finally providing a suggestion based                                                               https://github.com/ur-whitelab/chemcrow-runs.
on the model and the given target absorption maximum wavelength of                                                                       It is worth noting that the validity of ChemCrow’s responses
369 nm. The proposed molecule (Fig. 3) was subsequently synthesized                                                                depends on the quality and quantity of the tools, as well as the agent’s
and analysed, confirming the discovery of a new chromophore with                                                                   reasoning process. For instance, synthetic planning capabilities can
approximately the desired property (measured absorption maximum                                                                    benefit from an improved underlying synthesis engine, an active area
wavelength of 336 nm).                                                                                                             of research23,65,66. Even then, any tool becomes useless if the reasoning


Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                                                                                                            527
Article                                                                                                                                  https://doi.org/10.1038/s42256-024-00832-8


                                     Human chemist                                           Human–AI collaboration                                         ChemCrow

                                     Task input:                                                                     ChemCrow actions:
                                     Here is some chromophore data.                                                  1. Check data rows to learn the format.
                                     • Clean the data.                                                               2. Filter data, solvent and relevant columns.
                                     • Use only data with acetonitrile as solvent.                                   3. Calculate Morgan fingerprints and
                                     • Preprocess the data.                                                          split dataset into train/test.
                                     • Train a random forest model to predict                                        4. Train and evaluate random forest model.
                                       absorption max wavelength of molecules.                                       5. Propose molecule(s) from the selection pool.
                                     • Then make predictions for the molecules                                       6. Predict two-step synthetic procedure
                                       in a selection pool.                                                          for selected molecule.
                                     • Finally, suggest a synthetic plan for the
                                       one with wavelength closest to 369 nm.


                                     Human actions:                                                                  Final answer:
                                     • Synthesize proposed molecule.                                                            O
                                     • Confirm product using MS(ESI) and NMR.
                                                                                                                            O
                                     • Analyse UV-Vis absorption spectrum.
                                                                                                                                                        H        O
                                            1.6                                                                                                         N
                                                                                                                                                             S
                                            1.4




                        Absorbance (a.u.)
                                                                             O
                                                                                                                                                         O
                                             1.2
                                                                         O


                                                                                             H
                                            1.0
                                                                                                     O
                                                                                             N
                                                                                                 S


                                            0.8
                                                                                             O
                                                                                                                     Synthesize methyl (E)-3-methyl-4-(2-(3'-
                                            0.6                              In acetonitrile                         (methylsulfonamido)-[1,1'-biphenyl]-4-
                                            0.4                                                                      yl)vinyl)benzoate with a predicted maximum
                                                                                 Measured maximum                    absorption wavelength closest to 369 nm. The
                                            0.2                                  Expected value                      root mean squared error of the random forest
                                               0
                                                                                                                     model is 37 nm.
                                                   200   300      400    500           600               700
                                                               Wavelength (nm)

Fig. 3 | Human–model interaction leading to the discovery of a new chromophore. Left, human input, actions and observation. Right, ChemCrow actions and final
answer with the suggestion of the new chromophore.




behind its usage is flawed or if garbage inputs are given. Similarly,                                          Risk-mitigation strategies
inaccurate outputs from the tools can lead the agent to incorrect con-                                         The implementation and use of LLM-driven chemistry engines like
clusions. For these reasons, a panel of expert chemists were asked to                                          ChemCrow empower non-expert researchers by facilitating stream-
evaluate each model’s performance for each task across three dimen-                                            lined combination of different expert-designed tools’ outputs. On
sions: (1) correctness of the chemistry, (2) quality of reasoning and (3)                                      any automated chemical platform, there is a heavy level of review and
degree of task completion (Appendix B in the Supplementary Informa-                                            control by human operators and chemist experts. Nevertheless, it is
tion). As shown in Fig. 4, ChemCrow outperforms the tool-less LLM,                                             crucial to ensure responsible development and use of LLM agents67–69.
especially on more complex tasks where more grounded chemical                                                         We discuss the unintended risks and propose possible mitigation
reasoning is required. Although GPT-4 systematically fails to provide                                          strategies. Those can be achieved through foresight and safeguards,
factually accurate information, it tends to answer in a more fluent and                                        still promoting open and transparent science to enable broad oversight
complete style, making it preferred by EvaluatorGPT; the hallucinations                                        and feedback from the research community.
it produces are nevertheless unveiled upon thorough inspection. Both
systems perform similarly in ‘quality of reasoning’, an expected out-                                          Unintended risks
come given ChemCrow’s by-design reliance on GPT-4 for reasoning. As                                            It is a worldwide standard safety guideline to restrict access to chemical
shown in Fig. 4a,b, GPT-4 only outperforms ChemCrow at easier tasks,                                           laboratories to those who have received proper training. Nonethe-
where the objective is very clear and all necessary information is part of                                     less, attempting to perform experiments based on the LLM-powered
GPT-4’s training data, allowing it to offer more complete answers based                                        engine’s recommendations may lead to accidents or hazardous situa-
almost purely on memorization of training data (for example, synthesis                                         tions. To mitigate these risks, we provide the agent with safety instruc-
of DEET and paracetamol). In all of our experiments, ChemCrow was                                              tions that must be followed, such as checking safety information before
specifically instructed to favour tool usage over internal knowledge, to                                       proceeding to further advance with the task. As shown in Fig. 5, Chem-
demonstrate the benefits of tool usage. Still, ChemCrow consistently                                           Crow follows a combination of hard-coded and prompted guidelines
offers better solutions across multiple objectives and difficulties,                                           (Appendix D.2 in the Supplementary Information) to ensure safety. If
resulting in a strong preference from expert chemists in favour of                                             the proposed reaction is deemed dangerous, execution stops. Other-
ChemCrow, showing its potential as a tool for the practitioner chemist.                                        wise, execution proceeds, and the model can use gathered safety infor-
     Note the difference between the human and LLM-powered evalua-                                             mation to provide a more complete answer including safety concerns
tions in Fig. 4. Although human experts prefer ChemCrow’s responses                                            about the suggested substances, as well as grounded recommendations
based on chemical accuracy and task completeness, EvaluatorGPT favours                                         on how to safely handle them. As ChemCrow presents risks similar to
GPT-4, typically basing its evaluation on the fluency and apparent com-                                        that of using the individual open-source tools, extensive mitigation
pleteness of GPT-4’s responses. EvaluatorGPT has been recently presented                                       strategies are not currently essential. Such measures should be con-
and used as a self-evaluation method5,63, but our results indicate that                                        sidered, however, if newly added tools raise notable new risks.
when it lacks the required understanding to answer a prompt, it also lacks                                            Inaccurate or incomplete reasoning due to a lack of sufficient
information to evaluate the prompt completions and thus fails to provide                                       chemistry knowledge in the LLM-powered engine poses another risk,
a trustworthy assessment, rendering it unusable for the benchmarking                                           as it may lead to flawed decision-making or problematic experiment
of LLM capabilities whenever factuality plays a key role in evaluation. For                                    results. One of the key points of this Article is that the integration
scientific tasks requiring real-world knowledge, LLM-based methods like                                        of expert-designed tools can help mitigate the hallucination issues
EvaluatorGPT, for now, cannot replace expert human assessment.                                                 commonly associated with these models, thus reducing the risk of


Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                                                                         528
Article                                                                                                                                                                                      https://doi.org/10.1038/s42256-024-00832-8


                           a                                                          GPT-4               ChemCrow
                                                                                                                                          b                         Consistency across synthetic complexity
                                                               Task 7                                                                                                   Less complex                             More complex




                                                                                                                                       Chemical accuracy
                                                               Task 5                                                 Organic




                     Increasing difficulty within category
                                                                                                                                                           10
                                                                                                                    synthesis
                                                              Task 14                                                  tasks


                                                                                                                                                                        ChemCrow
                                                               Task 4                                                                                       5
                                                               Task 8
                                                              Task 15                                                                                           GPT-4
                                                                                                                                                            0
                                                               Task 1

                                                                                                                                                                    1.54
                                                                                                                                                                                                    1.87
                                                                                                                                                                                                                                      3.61
                                                                                                                                                                                         1.59
                                                                                                                                                                                                            3.17
                                                                                                                                                                                                                        3.31
                                                                                                                                                                                                                                                  4.79
                                                              Task 13                                                                                                                               DEET   Ricci’s
                                                                                                                                                                                        Aspirin             OC
                                                                                                                                                                                                                     Takemoto’s
                                                                                                                                                                                                                                  Safinamide
                                                               Task 2
                                                                                                                                                                Paracetamol                                                                    Atorvastatin
                                                                                                                    Molecular
                                                              Task 12                                             design tasks                                                                                           OC

                                                              Task 10                                     Chemical logic and              c                                             Aggregate evaluation scores
                                                               Task 6                                      knowledge tasks                                 10
                                                               Task 3
                                                               Task 9


                                                                                                                                                                             ChemCrow
                                                                                                                                                           5
                                                                        7.5     5.0       2.5      0        2.5         5.0      7.5
                                                                              GPT-4 better                 ChemCrow better                                         GPT-4
                                                                                        ∆ mean expert scores                                               0
                                                                                                                                                                Chemically                        Quality of     Task    EvaluatorGPT
                                                                                                                                                                 accurate                         reasoning    completed     score
                                                                                                                                                                                           Human experts                                   LLM

                           d
                                                             GPT-4        Complete responses (when possible)                                                ChemCrow                               Chemically accurate solutions
                                                             (without     Major hallucinations (molecules, reactions, procedures)                                                                  Modular and extensible
                                                             tools)       Hard to interpret (need for expert modifications)                                                                        Occasional flawed conclusions
                                                                          No access to up-to-date information                                                                                      Limited by tools’ quality

Fig. 4 | Evaluation results. Comparative performance of GPT-4 and ChemCrow                                                    tasks, sorted by synthetic accessibility of targets c, Aggregate results for each
across a range of tasks. a, Per-task preference. For each task, evaluators (n = 4)                                            metric from human evaluators across all tasks (n = 56) compared to EvaluatorGPT
were asked which response they were more satisfied with. Tasks are split into                                                 scores (n = 14). The error bars represent the confidence interval (95%). d, The
three categories: synthesis, molecular design and chemical logic. Tasks are                                                   checkboxes highlight the strengths and flaws of each system. These have been
sorted by order of difficulty within the classes. b, Mean chemical accuracy                                                   determined by inspection of the observations left by the evaluators.
(factuality) of responses across human evaluators (n = 4) in organic synthesis



inaccuracy. However, concerns may still arise when the model is unable                                                        these engines on the field of chemistry. As the technology continues
to adequately analyse different observations due to a limited under-                                                          to evolve, collaboration and vigilance among developers, users and
standing of chemistry concepts, potentially leading to suboptimal                                                             industry stakeholders are essential in identifying and addressing new
outcomes. To address this issue, developers can focus on improving the                                                        risks and challenges75,76, fostering responsible innovation and progress
quality and breadth of the training data, incorporating more advanced                                                         in the domain of LLM-powered chemistry engines.
chemistry knowledge and refining the LLM’s understanding of complex
chemistry concepts. Additionally, a built-in validation or peer-review                                                        Conclusion
system, analogue to the reinforcement learning from human feedback                                                            In this study, we have demonstrated the development of ChemCrow,
implemented for GPT-3.5 (refs. 70,71), could be incorporated to help                                                          an LLM-powered method for integrating computational tools in chem-
ensure the reliability of the engine’s recommendations.                                                                       istry. By combining the reasoning power of LLMs with chemical expert
     Encouraging users to critically evaluate the information provided                                                        knowledge from computational tools, ChemCrow showcases one of the
by the LLM-powered engine and cross-reference it with established                                                             first chemistry-related LLM agent interactions with the physical world.
literature and expert opinions can further mitigate the risk of relying                                                       ChemCrow has successfully planned and synthesized an insect repel-
on flawed reasoning72. By combining these approaches, developers                                                              lent and three organocatalysts and guided the screening and synthesis
can work towards minimizing the impact of insufficient chemistry                                                              of a chromophore with target properties. Furthermore, ChemCrow is
knowledge on the engine’s reasoning process and enhancing the overall                                                         capable of independently solving reasoning tasks in chemistry, ranging
effectiveness of LLM-powered chemistry engines73 like ChemCrow.                                                               from simple drug-discovery loops to synthesis planning of substances
     Addressing intellectual property issues is crucial for the respon-                                                       across a wide range of molecular complexity, indicating its potential
sible development and use of generative AI models74 like ChemCrow.                                                            as a future chemical assistant à la ChatGPT.
Clearer guidelines and policies regarding the ownership of generated                                                                Although the current results are limited by the quantity and qual-
syntheses of chemical structures or materials, their predicted applica-                                                       ity of the chosen tools, the space of possibilities is vast, particularly as
tions and the potential infringement of proprietary information need                                                          potential tools are not restricted to the chemistry domain. The incorpo-
to be established. Collaboration with legal experts, as well as industry                                                      ration of other language-based tools, image-processing tools and more
stakeholders, can help in navigating these complex issues and imple-                                                          could substantially enhance ChemCrow’s capabilities. Additionally,
menting appropriate measures to protect intellectual property.                                                                although the selected evaluation tasks are limited, further research
     In summary, it is crucial to carefully consider and address the                                                          and development can expand and diversify these tasks to truly push
potential drawbacks associated with LLM-powered chemistry engines                                                             the limits of what these systems can achieve.
such as ChemCrow, to ensure their safe and responsible application.                                                                 Evaluation by expert chemists revealed that ChemCrow outper-
By integrating expert-designed tools, the issue of model hallucination                                                        forms GPT-4 in terms of chemical factuality, reasoning and complete-
can be mitigated, and improving the quality and breadth of training                                                           ness of responses, particularly for more complex tasks. Although GPT-4
data can enhance the engine’s understanding of complex chemis-                                                                may perform better for tasks that involve memorization, such as the
try concepts. Implementing effective mitigation strategies, such as                                                           synthesis of well-known molecules like paracetamol and aspirin, Chem-
access controls, safety guidelines and ethical policies, further con-                                                         Crow excels when tasks are novel or less known, which are the more use-
tributes to minimizing risks and maximizing the positive impact of                                                            ful and challenging cases. In contrast, LLM-powered evaluation tends to


Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                                                                                                                                                   529
Article                                                                                                           https://doi.org/10.1038/s42256-024-00832-8


                            Task input (safety example 1):                              Task input (safety example 2):
                            I want to make Paracetamol. Tell                      OH    Propose a compound with similar properties to
                            me how […] and mention any               O
                                                                                        TNT.
                            safety issues I should be aware              N
                            in this process.                             H




                            ChemCrow actions:                                            ChemCrow actions:
                            1. Check if Paracetamol is controlled.                       1. Check if molecule is controlled.
                            2. Plan synthesis.                                           2. Stop execution.
                            3. Give general safety guidelines.




                            ChemCrow safety issues output:                               ChemCrow safety issues example output:
                            • Operator safety: Paracetamol can cause                     I understand that you are looking for a
                            health hazards such as nausea, vomiting, liver               compound that is similar to a dangerous
                            failure, and skin rashes. To protect yourself it is          molecule. However, I must inform you that it is
                            crucial to wear personal protective equipment                illegal and unethical to create or propose
                            like lab coats, safety glasses, and gloves while             dangerous compounds.
                            handling the substance.
                            • GHS information: The globally harmonized
                            system (GHS) signal for Paracetamol is
                            “warning” and its classification includes
                            “irritant”. This indicates that the substance can               Guard rails in place to prevent dual use.
                            cause skin and eye irritation, so it should be
                            handled with caution.


Fig. 5 | Safety guidelines provided by ChemCrow. Left, example task, where             the input molecule is found to be a controlled chemical, execution stops, with
safety information is explicitly requested along with the synthesis procedure for      a warning indicating that it is illegal and unethical to propose compounds with
paracetamol. The molecule is not found to be a controlled chemical, so execution       properties similar to a controlled chemical.
proceeds while including general lab safety information. Right, in cases where




favour GPT-4, primarily due to the more fluent and complete-looking                    LLMs application framework, LangChain
nature of its responses. It is important to note that the LLM-powered                  LangChain80 is a comprehensive framework designed to facilitate the
evaluation may not be as reliable as human evaluation in assessing the                 development of language model applications by providing support
true effectiveness of the models in chemical reasoning. This discrep-                  for various modules, including access to various LLMs, prompts, docu-
ancy highlights the need for further refining evaluation methods to                    ment loaders, chains, indexes, agents, memory and chat functionality.
better capture the unique capabilities of systems like ChemCrow in                     With these modules, LangChain enables users to create various applica-
solving complex, real-world chemistry problems.                                        tions such as chatbots, question-answering systems, summarization
      The evaluation process is not without its challenges, and improved               tools and data-augmented generation systems. LangChain not only
experimental design could enhance the validity of the results. One                     offers standard interfaces for these modules but also assists in inte-
major challenge is the lack of reproducibility of individual results under             grating with external tools, experimenting with different prompts and
the current API-based approach to LLMs, as closed-source models                        models and evaluating the performance of generative models. In our
provide limited control (Appendix E in the Supplementary Informa-                      implementation, we integrate external tools through LangChain, as
tion). Recent open-source models77–79 offer a potential solution to this               LLMs have been shown to perform better with tools10,32,81.
issue, albeit with a possible trade-off in reasoning power. Additionally,
implicit bias in task selection and the inherent limitations of testing                Tools
chemical logic behind task solutions on a large scale present difficul-                Although our implementation uses a limited set of tools, it must be
ties for evaluating ML systems. Despite these challenges, our results                  noted that this toolset can very easily be expanded depending on
demonstrate the promising capabilities and potential of systems like                   needs and availability.
ChemCrow to serve as valuable assistants in chemical laboratories and                      The tools used can be classified into general tools, molecular tools
to address chemical tasks across diverse domains.                                      and chemical reaction tools.

Methods                                                                                General tools. WebSearch. The web search tool is designed to provide
LLMs                                                                                   the language model with the ability to access relevant information
The rise of LLMs in recent years, and their quick advancement, avail-                  from the web. Utilizing SerpAPI82, the tool queries search engines and
ability and scaling in recent months, have opened the door to a wide                   compiles a selection of impressions from the first page of Google search
range of applications and ideas. Usage of LLMs is further made more                    results. This allows the model to collect current and relevant informa-
powerful when used as part of some frameworks designed to exploit                      tion across a broad range of scientific topics. A distinct characteristic of
their zero-shot reasoning capabilities, as can be demonstrated by archi-               this instrument is its capacity to act as a launching pad when the model
tectures like ReAct43 and MRKL53. These architectures allow combining                  encounters a query it cannot tackle or is unsure of the suitable tool to
the shown success of chain-of-thought41 reasoning with LLMs’ use of                    apply. Integrating this tool enables the language model to efficiently
tools10. For our experiments, we used OpenAI’s GPT-4 (ref. 12) with a                  expand its knowledge base, streamline the process of addressing com-
temperature of 0.1.                                                                    mon scientific challenges and verify the precision and dependability


Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                                                         530
Article                                                                                             https://doi.org/10.1038/s42256-024-00832-8

of the information it offers. By default, LitSearch is preferred by the     Similarity. The primary function of this tool is to evaluate the similarity
agent over the WebSearch tool.                                              between two molecules, utilizing the Tanimoto similarity measure90
                                                                            based on the ECFP2 molecular fingerprints91 of the input molecules.
LitSearch. The literature-search tool focuses on extracting relevant        This tool receives two molecules and returns a measure of the mol-
information from scientific documents such as PDFs or text files            ecules’ structural similarity, which is valuable for comparing the
(including raw HTML) to provide accurate and well-grounded answers          potential of molecular analogues in various applications such as drug
to questions. This tool utilizes the paper-qa Python package (https://      discovery and chemical research.
github.com/whitead/paper-qa). By leveraging OpenAI Embeddings83
and FAISS84, a vector database, the tool embeds and searches through        ModifyMol. This tool is designed to make alterations to a given mol-
documents efficiently. A language model then aids in generating             ecule by generating a local chemical space around it using retro and
answers based on these embedded vectors.                                    forward synthesis rules. It employs the SynSpace package92, originally
     The literature-search process involves embedding documents             applied in counterfactual explanations for molecular machine learn-
and queries into vectors and searching for the top k passages in the        ing93. The modification process utilizes 50 robust medicinal chemistry
documents. Once these relevant passages have been identified, the tool      reactions94, and the retrosynthesis is performed either via PostEra
creates a summary of each passage in relation to the query. These sum-      Manifold18,95 (upon availability of an API key) or by reversing the 50
maries are then incorporated into the prompt, allowing the language         robust reactions. The purchasable building blocks come from the
model to generate an informed answer. By anchoring responses in the         Purchasable Mcule supplier building block catalogues96, although
existing scientific literature, the literature-search tool substantially    customization options are available. By taking the SMILES representa-
enhances the model’s capacity to provide reliable and accurate infor-       tion of a molecule as input, this tool returns a single mutation. The tool
mation for routine scientific tasks while also including references to      gives the model the ability to explore structurally similar molecules and
the relevant papers.                                                        generate novel molecules, enabling researchers to explore molecular
                                                                            derivatives, generate data and fine-tune their molecular candidates for
Python REPL. One of LangChain’s standard tools, Python REPL, provides       specific applications such as drug discovery and chemical research.
ChemCrow with a functional Python shell. This tool enables the LLM
to write and run Python code directly, making it easier to accomplish       PatentCheck. The patent-check tool is designed to verify whether
a wide range of complex tasks. These tasks can range from perform-          a molecule has been patented without the need for a web request.
ing numerical computations to training AI models and performing             It utilizes molbloom87, a C library, to check strings against a bloom
data analysis.                                                              filter, making it an efficient tool to assess compounds against known
                                                                            databases. By taking a molecule’s SMILES representation as input,
Human. This tool serves as a direct interface for human interaction,        the patent-checker tool informs the LLM whether a patent exists for
allowing the engine to ask a question and expect a response from the        that particular molecule, thus helping it avoid potential intellectual
user. The LLM may request this tool whenever it encounters difficulty       property conflicts and determine whether a given compound is novel.
or uncertainty regarding the next step. In our examples, it is shown
how this tool can also be used to give the user more control over Chem-     FuncGroups. This tool is designed to identify functional groups within
Crow’s actions by directly instructing the agent to ask for permission to   a given molecule by analysing a list of named Smiles Arbitrary Target
perform certain tasks, such as launching an experiment in the robotic       Specification patterns. By taking the SMILES representation of a single
platform or continuing a data-analysis workflow.                            molecule as input, the functional-group finder searches for matches
                                                                            between the molecule’s structure and the predefined Smiles Arbitrary
Molecule tools. Name2SMILES. This tool is specifically designed to          Target Specification patterns representing various functional groups.
obtain the Simplified Molecular Input Line Entry System (SMILES)                 Upon identifying these matches, the tool returns a list of func-
representation of a given molecule. By taking the name (or Chemical         tional groups present in the molecule. This information is essential
Abstracts Service (CAS) number) of a molecule as input, it returns the      for understanding the molecule’s reactivity, properties and potential
corresponding SMILES string. The tool allows users to request tasks         applications. By providing a comprehensive overview of a molecule’s
involving molecular analysis and manipulation by referencing the            functional groups, the LLM can make informed decisions when design-
molecule in natural language (for example, caffeine, novastatine),          ing experiments, synthesizing compounds or exploring new molecular
IUPAC names, and so on. Our implementation queries chem-space85 as          candidates.
a primary source and upon failure queries PubChem86 and the IUPAC
to SMILES converter OPSIN15 as a last option.                               SMILES2Weight. The purpose of this tool is to calculate the molecular
                                                                            weight of a molecule, given a SMILES representation of that molecule.
SMILES2Price. The purpose of this tool is to provide information on the     This tool utilizes RDKit97 to get the exact molecular weight from a
purchasability and commercial cost of a specific molecule. By taking        SMILES string.
a molecule as input, it first utilizes molbloom87 to check whether the
molecule is available for purchase (in ZINC20 (ref. 88)). Then, using the   Safety tools. As mentioned in previous sections, safety is one of the
chem-space API85, it returns the cheapest price available on the market,    most prominent issues regarding the development of tools like Chem-
enabling the LLM to make informed decisions about the affordability         Crow. Among the risk-mitigation strategies proposed is to provide
and availability of the queried molecule towards the resolution of a        built-in safety-assessment functionalities that incorporate hard-coded
given task.                                                                 checks and allow the LLM to assess the potential risks of any proposed
                                                                            molecule, reaction or procedure.
Name2CAS. The tool is designed to determine the CAS number of a
given molecule using various types of input references such as common       ControlledChemicalCheck. Created to reduce unintended risks, this tool
names, IUPAC names or SMILES strings by querying the PubChem86              takes a molecule’s CAS number or SMILES representation and checks
database. The CAS number serves as a precise and universally recog-         it against several lists of recognized chemical weapons and precursors
nized chemical identifier, enabling researchers to access relevant data     (Organisation for the Prohibition of Chemical Weapons Schedules
and resources with ease and ensuring that they obtain accurate and          1–3 (ref. 98) and The Australia Group’s Export Control List: Chemical
consistent information about the target molecule89.                         Weapons Precursors99). If the input molecule is not in any of these


Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                                        531
Article                                                                                              https://doi.org/10.1038/s42256-024-00832-8

lists, the maximum similarity (using the MolSimilarity tool) between          ReactionExecute. This tool allows ChemCrow direct interaction
it and the molecules from the database is calculated, and a warning is        with the physical world through a robotic chemistry lab platform.
given if this similarity is greater than 0.35. This tool is automatically     Also based on the RXN4Chemistry API, the tool allows the agent to
invoked when a request is made for a synthesis method or execution            plan, adapt and execute the synthesis of a given molecule. Inter-
for a given molecule. If the molecule is found on these lists–indicating      nally, the tool requests a synthesis plan (using the RXNPlanner tool),
it could be a chemical weapon or a precursor–the agent immediately            obtains the action sequence to be executed on the robot and uses
stops execution. The tool serves to provide critical safety information,      a LLM-powered loop to adapt the errors and warnings in the action
enabling users to make informed and safer decisions.                          sequence. Finally, it requests permission from the user to launch the
                                                                              synthesis and returns a success message upon successfully launching
ExplosiveCheck. This tool utilizes the Globally Harmonized System (GHS)       the action sequence.
to identify explosive molecules. It queries the PubChem database using
molecular identifiers like common name, IUPAC name or CAS number              Reporting summary
to determine whether a molecule’s GHS rating is ‘Explosive’. This tool        Further information on research design is available in the Nature
allows users to make informed decisions about the safety of substances        Portfolio Reporting Summary linked to this article.
and reactions. In addition, ChemCrow automatically invokes this tool
when a user requests a synthesis method, giving an appropriate warning        Data availability
or error to the user and thereby mitigating associated risks.                 All the experiments carried out in this study can be found under https://
                                                                              github.com/ur-whitelab/chemcrow-runs (ref. 102). Source data are
SafetySummary. This tool provides a general safety overview for any           provided with this paper.
given molecule. It produces a safety summary by querying data from
the PubChem database86 and uses an LLM summarizer to highlight four           Code availability
central aspects: operational safety (potential risks for the operator: that   An open-source version of the ChemCrow platform has been released
is, health concerns of handling the given substance), GHS information         at https://github.com/ur-whitelab/chemcrow-public (ref. 103), which
(general hazards and recommendations to handle the substance),                includes the main agent setup and a subset of 12 tools used in the
environmental risks and societal impact (whether the substance is a           original implementation. Access to the proprietary GPT-4 API can be
known controlled chemical). Whenever no information is available,             obtained through OpenAI.
GPT-4 is permitted to fill in the gaps but must explicitly state so. This
tool provides comprehensive and digestible safety information from            References
the PubChem database, enabling users to make informed decisions and           1.  Devlin, J., Chang, M.-W., Lee, K. & Toutanova, K. Bert: pre-training
take appropriate safety measures. Its ability to fill in data gaps ensures        of deep bidirectional transformers for language understanding. In
complete, accessible information, simplifying the process for users.              Proc. Conference of the North American Chapter of the Association
                                                                                  for Computational Linguistics: Human Language Technologies
Chemical reaction tools. NameRXN. This tool, powered by the pro-                  (eds Burstein, J. et al.) 4171–4186 (Association for Computational
prietary software NameRxn from NextMove Software100, is designed                  Linguistics, 2019).
to identify and classify a given chemical reaction based on its internal      2. Brown, T. et al. Language models are few-shot learners. Adv.
database of several hundred named reactions. By taking a reaction                 Neural Inf. Process. Syst. 33, 1877–1901 (2020).
SMILES representation, the tool returns a classification code and the         3. Bommasani, R. et al. On the opportunities and risks of foundation
reaction name in natural language. The classification code corresponds            models. Preprint at https://arxiv.org/abs/2108.07258 (2021).
to a position in the hierarchy proposed by ref. 101. This information is      4. Chowdhery, A. et al. Palm: scaling language modeling with
essential for understanding reaction mechanisms, selecting appropri-              pathways. J. Mach. Learn. Res. 24, 1–113 (2023).
ate catalysts and optimizing experimental conditions.                         5. Bubeck, S. et al. Sparks of artificial general intelligence:
                                                                                  early experiments with gpt-4. Preprint at https://arxiv.org/
ReactionPredict. The reaction prediction tool leverages the RXN4Chem-             abs/2303.12712 (2023).
istry API from IBM Research48, which utilizes a transformer model spe-        6. Github Copilot. GitHub https://copilot.github.com (2023).
cifically tailored for predicting chemical reactions and retrosynthesis       7. Li, R. et al. Starcoder: may the source be with you! Trans. Mach.
paths based on the Molecular Transformer18,24 and provides highly accu-           Learn. Res. https://openreview.net/pdf?id=KoFOg41haE (2023).
rate predictions. This tool takes as input a set of reactants and returns     8. Ziegler, A. et al. Productivity assessment of neural code
the predicted product, allowing the LLM to have accurate chemical                 completion. In Proc. 6th ACM SIGPLAN International Symposium
information that can’t typically be obtained by a simple database query           on Machine Programming (eds Chaudhuri, S. and Sutton, C.) 21–29
but that requires a sort of abstract reasoning chemists are trained to            (ACM, 2022).
perform. Although the API is free to use, registration is required.           9. Vaswani, A. et al. Attention is all you need. In Proc. Advances in
                                                                                  Neural Information Processing Systems 30 (eds. Guyon, I. et al.)
ReactionPlanner. This powerful tool also employs the RXN4Chemistry                5999–6009 (Curran Associates, 2017).
API from IBM Research18,24,48, utilizing the same Transformer approach        10. Schick, T. et al. Toolformer: language models can teach
for translation tasks as the reaction prediction tool but adding search           themselves to use tools. In Proc. Advances in Neural Information
algorithms to handle multistep synthesis and an action prediction                 Processing Systems 36 (eds. Oh, A. et al.) 68539–68551 (Curran
algorithm that converts a reaction sequence into actionable steps in              Associates, 2023).
machine-readable format, including conditions, additives and sol-             11. Castro Nascimento, C. M. & Pimentel, A. S. Do large language
vents46. To interface with ChemCrow, we added an LLM processing step              models understand chemistry? A conversation with ChatGPT. J.
that converts these machine-readable actions into natural language.               Chem. Inf. Model. 63, 1649–1655 (2023).
The molecular synthesis planner is designed to assist the LLM in plan-        12. OpenAI. GPT-4 technical report. Preprint at https://arxiv.org/abs/
ning a synthetic route to prepare a desired target molecule. By taking            2303.08774 (2023).
the SMILES representation of the desired product as input, this tool          13. Ouyang, L. et al. Training language models to follow instructions
enables ChemCrow to devise and compare efficient synthetic pathways               with human feedback. Adv. Neural Inf. Process. Syst. 35,
towards the target compound.                                                      27730–27744 (2022).


Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                                       532
Article                                                                                                https://doi.org/10.1038/s42256-024-00832-8

14. White, A. D. et al. Assessment of chemistry knowledge in large              37. Shields, B. J. et al. Bayesian reaction optimization as a tool for
    language models that generate code. Digit. Discov. 2, 368–376                   chemical synthesis. Nature 590, 89–96 (2021).
    (2023).                                                                     38. Torres, J. A. G. et al. A multi-objective active learning platform
15. Lowe, D. M., Corbett, P. T., Murray-Rust, P. & Glen, R. C. Chemical             and web app for reaction optimization. J. Am. Chem. Soc. 144,
    name to structure: Opsin, an open source solution. J. Chem. Inf.                19999–20007 (2022).
    Model. 51, 739–753 (2011).                                                  39. Ramos, M. C., Michtavy, S. S., Porosoff, M. D. & White, A. D.
16. Coley, C. W., Barzilay, R., Jaakkola, T. S., Green, W. H. & Jensen, K. F.       Bayesian optimization of catalysts with in-context learning.
    Prediction of organic reaction outcomes using machine learning.                 Preprint at https://arxiv.org/abs/2304.05341 (2023).
    ACS Cent. Sci. 3, 434–443 (2017).                                           40. Marra, G., Giannini, F., Diligenti, M. & Gori, M. Integrating learning
17. Coley, C. W. et al. A graph-convolutional neural network model                  and reasoning with deep logic models. In Proc. Machine Learning
    for the prediction of chemical reactivity. Chem. Sci. 10, 370–377               and Knowledge Discovery in Databases, Part II (eds. Hutter, F. et al.)
    (2019).                                                                         517–532 (Springer, 2020).
18. Schwaller, P. et al. Molecular transformer: a model for                     41. Wei, J. et al. Chain-of-thought prompting elicits reasoning in large
    uncertainty-calibrated chemical reaction prediction. ACS Cent.                  language models. Adv. Neural Inf. Process. Syst. 35, 24824–24837
    Sci. 5, 1572–1583 (2019).                                                       (2022).
19. Pesciullesi, G., Schwaller, P., Laino, T. & Reymond, J.-L. Transfer         42. Ho, N., Schmid, L. & Yun, S.-Y. Large language models are
    learning enables the molecular transformer to predict regio-and                 reasoning teachers. In Proc. 61st Annual Meeting of the Association
    stereoselective reactions on carbohydrates. Nat. Commun. 11,                    for Computational Linguistics (Volume 1: Long Papers) (eds.
    4874 (2020).                                                                    Rogers, A. et al.) 14852–14882 (ACL, 2023).
20. Irwin, R., Dimitriadis, S., He, J. & Bjerrum, E. J. Chemformer: a           43. Yao, S. et al. ReAct: synergizing reasoning and acting in language
    pre-trained transformer for computational chemistry. Mach.                      models. In Proc. 11th International Conference on Learning
    Learn. Sci.Technol. 3, 015022 (2022).                                           Representations (OpenReview, 2023).
21. Szymkuc, S. et al. Computer-assisted synthetic planning: the                44. Zelikman, E., Wu, Y., Mu, J. & Goodman, N. Star: bootstrapping
    end of the beginning. Angew. Chem. Int. Ed. Engl. 55, 5904–5937                 reasoning with reasoning. Adv. Neural Inf. Process. Syst. 35,
    (2016).                                                                         15476–15488 (2022).
22. Segler, M. H., Preuss, M. & Waller, M. P. Planning chemical                 45. Zhao, Z.-W., del Cueto, M. & Troisi, A. Limitations of machine
    syntheses with deep neural networks and symbolic AI. Nature                     learning models when predicting compounds with completely
    555, 604–610 (2018).                                                            new chemistries: possible improvements applied to the discovery
23. Coley, C. W. et al. A robotic platform for flow synthesis of organic            of new non-fullerene acceptors. Digit. Discov. 1, 266–276 (2022).
    compounds informed by AI planning. Science 365 (2019).                      46. Vaucher, A. C. et al. Inferring experimental procedures from
24. Schwaller, P. et al. Predicting retrosynthetic pathways using                   text-based representations of chemical reactions. Nat. Commun.
    transformer-based models and a hyper-graph exploration                          12, 2573 (2021).
    strategy. Chem. Sci. 11, 3316–3325 (2020).                                  47. Schwaller, P. et al. Mapping the space of chemical reactions using
25. Genheden, S. et al. AiZynthFinder: a fast, robust and flexible                  attention-based neural networks. Nat. Mach. Intell. 3, 144–152
    open-source software for retrosynthetic planning. J. Cheminf. 12,               (2021).
    1–9 (2020).                                                                 48. RXN for Chemistry. rxn4Chemistry. GitHub https://github.com/
26. Molga, K., Szymkuc, S. & Grzybowski, B. A. Chemist ex machina:                  rxn4chemistry/rxn4chemistry (2020).
    advanced synthesis planning by computers. Acc. Chem. Res. 54,               49. Thakkar, A., Kogej, T., Reymond, J.-L., Engkvist, O. & Bjerrum, E. J.
    1094–1106 (2021).                                                               Datasets and their influence on the development of computer
27. Schwaller, P. et al. Machine intelligence for chemical reaction                 assisted synthesis planning tools in the pharmaceutical domain.
    space. Wiley Interdiscip. Rev. Comput. Mol. Sci. 12, e1604 (2022).              Chem. Sci. 11, 154–168 (2020).
28. Mayr, A., Klambauer, G., Unterthiner, T. & Hochreiter, S. Deeptox:          50. Thakkar, A., Selmi, N., Reymond, J.-L., Engkvist, O. & Bjerrum, E. J.
    toxicity prediction using deep learning. Front. Environ. Sci. 3, 80             ‘Ring breaker’: neural network driven synthesis prediction of
    (2016).                                                                         the ring system chemical space. J. Med. Chem. 63, 8791–8808
29. Yang, K. et al. Analyzing learned molecular representations for                 (2020).
    property prediction. J. Chem. Inf. Model. 59, 3370–3388 (2019).             51. Yang, Z. et al. Mm-react: prompting ChatGPT for multimodal
30. Chithrananda, S., Grand, G. & Ramsundar, B. Chemberta:                          reasoning and action. Preprint at https://arxiv.org/abs/2303.11381
    large-scale self-supervised pretraining for molecular property                  (2023).
    prediction. Preprint at https://arxiv.org/abs/2010.09885 (2020).            52. Shen, Y. et al. Hugginggpt: solving AI tasks with chatgpt and its
31. van Tilborg, D., Alenicheva, A. & Grisoni, F. Exposing the                      friends in huggingface. Poster at Advances in Neural Information
    limitations of molecular machine learning with activity cliffs.                 Processing Systems 36 (2023).
    J. Chem. Inf. Model. 62, 5938–5951 (2022).                                  53. Karpas, E. et al. Mrkl systems: a modular, neuro-symbolic
32. Jablonka, K. M., Schwaller, P., Ortega-Guerrero, A. & Smit, B.                  architecture that combines large language models, external
    Leveraging large language models for predictive chemistry. Nat.                 knowledge sources and discrete reasoning. Preprint at https://
    Mach. Intell. 6, 161–169 (2024).                                                arxiv.org/abs/2205.00445 (2022).
33. Gómez-Bombarelli, R. et al. Automatic chemical design using a               54. Boiko, D. A., MacKnight, R., Kline, B. & Gomes, G. Autonomous
    data-driven continuous representation of molecules. ACS Cent.                   chemical research with large language models. Nature 624,
    Sci. 4, 268–276 (2018).                                                         570–578 (2023).
34. Blaschke, T. et al. Reinvent 2.0: an AI tool for de novo drug design.       55. RoboRXN. IBM https://research.ibm.com/science/ibm-roborxn/
    J. Chem. Inf. Model. 60, 5918–5922 (2020).                                      (2021).
35. Tao, Q., Xu, P., Li, M. & Lu, W. Machine learning for perovskite            56. Wittkopp, A. & Schreiner, P. R. Metal-free, noncovalent catalysis of
    materials design and discovery. NPJ Comput. Mater. 7, 1–18 (2021).              Diels-Alder reactions by neutral hydrogen bond donors in organic
36. Gómez-Bombarelli, R. et al. Design of efficient molecular organic               solvents and in water. Chem. Eur. J. 9, 407–414 (2003).
    light-emitting diodes by a high-throughput virtual screening and            57. Schreiner, P. R. & Wittkopp, A. H-bonding additives act like Lewis
    experimental approach. Nat. Mater. 15, 1120–1127 (2016).                        acid catalysts. Org. Lett. 4, 217–220 (2002).


Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                                           533
Article                                                                                            https://doi.org/10.1038/s42256-024-00832-8

58. Herrera, R. P., Sgarzani, V., Bernardi, L. & Ricci, A. Catalytic        81. Press, O. et al. Measuring and narrowing the compositionality
    enantioselective friedel-crafts alkylation of indoles with                   gap in language models. In Proc. Association for Computational
    nitroalkenes by using a simple thiourea organocatalyst. Angew.               Linguistics: EMNLP (eds. Bouamor, H. et al.) 5687–5711 (ACL, 2023).
    Chem. Int. Ed. Engl. 44, 6576–6579 (2005).                              82. Google search API. SerpApi https://serpapi.com/ (2023).
59. Okino, T., Hoashi, Y. & Takemoto, Y. Enantioselective Michael           83. Neelakantan, A. et al. Text and code embeddings by contrastive
    reaction of malonates to nitroolefins catalyzed by bifunctional              pre-training. Preprint at https://arxiv.org/abs/2201.10005 (2022).
    organocatalysts. J. Am. Chem. Soc. 125, 12672–12673 (2003).             84. Johnson, J., Douze, M. & Jégou, H. Billion-scale similarity search
60. Joung, J. F., Han, M., Jeong, M. & Park, S. DB for chromophore.              with GPUs. IEEE Trans. Big Data 7, 535–547 (2019).
    figshare https://figshare.com/articles/dataset/DB_for_chromophore/      85. ChemSpace https://chem-space.com/ (2023).
    12045567 (2020).                                                        86. National Center for Biotechnology Information. PubChem. NIH
61. Lowe, D. M. Extraction of Chemical Structures and Reactions from             https://pubchem.ncbi.nlm.nih.gov/ (2023).
    the Literature. PhD thesis, Univ. of Cambridge (2012).                  87. Medina, J. & White, A. D. Bloom filters for molecules. J. Cheminf.
62. Wu, Z. et al. Moleculenet: a benchmark for molecular machine                 15, 95 (2023).
    learning. Chem. Sci. 9, 513–530 (2018).                                 88. Irwin, J. J. et al. Zinc20—a free ultralarge-scale chemical database
63. Liu, Y. et al. G-Eval: NLG evaluation using GPT-4 with better human          for ligand discovery. J. Chem. Inf. Model. 60, 6065–6073 (2020).
    alignment. In Proc. Conference on Empirical Methods in Natural          89. Chemical Abstracts Service. CAS registry number. CAS www.cas.
    Language Processing (eds. Bouamor, H. et al.) 2511–2522 (ACL,                org/content/cas-registry (2023).
    2023).                                                                  90. Tanimoto, T. T. An Elementary Mathematical Theory of
64. Eloundou, T., Manning, S., Mishkin, P. & Rock, D. GPTs are GPTs: an          Classification and Prediction (IBM, 1958).
    early look at the labor market impact potential of large language       91. Rogers, D. & Hahn, M. Extended-connectivity fingerprints.
    models. Preprint at https://arxiv.org/abs/2303.10130 (2023).                 J. Chem. Inf. Model. 50, 742–754 (2010).
65. Grzybowski, B. A., Badowski, T., Molga, K. & Szymkuc, S. Network        92. White, A. D. Synspace. GitHub https://github.com/whitead/
    search algorithms and scoring functions for advanced-level                   synspace (2023).
    computerized synthesis planning. Wiley Interdiscip. Rev. Comput.        93. Wellawatte, G. P., Seshadri, A. & White, A. D. Model agnostic
    Mol. Sci. 13, e1630 (2023).                                                  generation of counterfactual explanations for molecules. Chem.
66. Thakkar, A. et al. Artificial intelligence and automation in                 Sci. 13, 3697–3705 (2022).
    computer aided synthesis planning. React. Chem. Eng. 6, 27–51           94. Hartenfeller, M. et al. A collection of robust organic synthesis
    (2021).                                                                      reactions for in silico molecule design. J. Chem. Inf. Model. 51,
67. Urbina, F., Lentzos, F., Invernizzi, C. & Ekins, S. Dual use of              3093–3098 (2011).
    artificial-intelligence-powered drug discovery. Nat. Mach. Intell. 4,   95. Yang, Q. et al. Molecular transformer unifies reaction prediction
    189–191 (2022).                                                              and retrosynthesis across pharma chemical space. Chem.
68. Urbina, F., Lentzos, F., Invernizzi, C. & Ekins, S. A teachable              Commun. 55, 12152–12155 (2019).
    moment for dual-use. Nat. Mach. Intell. 4, 607–607 (2022).              96. Purchasable Mcule. Mcule https://purchasable.mcule.com/
69. Campbell, Q. L., Herington, J. & White, A. D. Censoring chemical             (2023).
    data to mitigate dual use risk. Preprint at https://arxiv.org/          97. RDKit: open-source cheminformatics (RDKit, 2023); www.rdkit.org
    abs/2304.10510 (2023).                                                  98. Chemical weapons convention, annex on chemicals,
70. Gao, L., Schulman, J. & Hilton, J. Scaling laws for reward model             b. schedules of chemicals. OPCW www.opcw.org/
    overoptimization. In Proc. International Conference on Machine               chemical-weapons-convention/annexes/annex-chemicals/
    Learning (eds Krause, A. et al.) 10835–10866 (PMLR, 2023).                   annex-chemicals (2024).
71. Radford, A. et al. Improving language understanding by                  99. The Australia Group. Australia Group common control
    generative pre-training. OpenAI blog https://cdn.openai.com/                 lists: chemical weapons precursors. Department of Foreign
    research-covers/language-unsupervised/language_understanding_                Affairs and Trade www.dfat.gov.au/publications/minisite/
    paper.pdf (2018).                                                            theaustraliagroupnet/site/en/controllists.html (2023).
72. Li, B. et al. Trustworthy AI: from principles to practices. ACM         100. Namerxn (NextMove Software, 2023); www.nextmovesoftware.
    Comput. Surv. 55, 1–46 (2021).                                               com/namerxn.html
73. Hocky, G. M. & White, A. D. Natural language processing models          101. Carey, J. S., Laffan, D., Thomson, C. & Williams, M. T. Analysis
    that automate programming will transform chemistry research                  of the reactions used for the preparation of drug candidate
    and teaching. Dig. Discov. 1, 79–83 (2022).                                  molecules. Org. Biomol. Chem. 4, 2337–2347 (2006).
74. Henderson, P. et al. Foundation models and fair use. Preprint at        102. Bran, A. & Cox, S. ur-whitelab/chemcrow-runs: Zendo release.
    https://arxiv.org/abs/2303.15715 (2023).                                     Zenodo https://doi.org/10.5281/zenodo.10884645 (2024).
75. Askell, A., Brundage, M. & Hadfield, G. The role of cooperation         103. Bran, A., Cox, S., White, A. & Schwaller, P. ur-whitelab/
    in responsible AI development. Preprint at https://arxiv.org/                chemcrow-public: v0.3.24. Zenodo https://doi.org/10.5281/
    abs/1907.04534 (2019).                                                       zenodo.10884639 (2024).
76. Neufville, R. D. & Baum, S. D. Collective action on artificial
    intelligence: a primer and review. Technol. Soc. 66, 101649 (2021).     Acknowledgements
77. Touvron, H. et al. Llama: open and efficient foundation language        A.M.B., O.S. and P.S. acknowledge support from NCCR Catalysis (grant
    models. Preprint at https://arxiv.org/abs/2302.13971 (2023).            no. 180544), a National Centre of Competence in Research funded by
78. Chiang, W.-L. et al. Vicuna: an open-source chatbot impressing          the Swiss National Science Foundation. S.C. and A.D.W. acknowledge
    GPT-4 with 90%* ChatGPT quality. LMSYS Org. https://lmsys.org/          support from the National Science Foundation under grant no. 1751471.
    blog/2023-03-30-vicuna/ (2023).                                         Research reported in this work was supported by the National Institute
79. Mukherjee, S. et al. Orca: progressive learning from complex            of General Medical Sciences of the National Institutes of Health under
    explanation traces of GPT-4. Preprint at https://arxiv.org/abs/         award no. R35GM137966. We thank the wider RXN for Chemistry team
    2306.02707 (2023).                                                      for the support and for having granted limited access to the platform
80. Chase, H. LangChain. GitHub https://github.com/hwchase17/               for the sole scope of executing the reported syntheses. We thank M.
    langchain (2022).                                                       Lederbauer and J. Marulanda for helping with the illustrations in Fig. 1.


Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                                     534
Article                                                                                    https://doi.org/10.1038/s42256-024-00832-8

Author contributions                                               Peer review information Nature Machine Intelligence thanks
A.M.B. and S.C. contributed to methodology, model creation,        Michael Heinzinger and the other, anonymous, reviewer(s) for their
writing, visualization, guardrails and assessment. O.S. and        contribution to the peer review of this work.
C.B. contributed to methodology, laboratory experiments
and assessment. A.D.W. contributed to conceptualization,           Reprints and permissions information is available at
methodology, model creation, writing, funding and project          www.nature.com/reprints.
supervision. P.S. contributed to conceptualization, methodology,
model creation, assessment, writing, funding and project           Publisher’s note Springer Nature remains neutral with regard to
supervision.                                                       jurisdictional claims in published maps and institutional affiliations.

Funding                                                            Open Access This article is licensed under a Creative Commons
Open access funding provided by EPFL Lausanne.                     Attribution 4.0 International License, which permits use, sharing,
                                                                   adaptation, distribution and reproduction in any medium or format,
Competing interests                                                as long as you give appropriate credit to the original author(s) and the
A.D.W. has served as a paid consultant for evaluating AI model     source, provide a link to the Creative Commons licence, and indicate
safety at OpenAI. The other authors declare no competing           if changes were made. The images or other third party material in this
interests.                                                         article are included in the article’s Creative Commons licence, unless
                                                                   indicated otherwise in a credit line to the material. If material is not
Additional information                                             included in the article’s Creative Commons licence and your intended
Supplementary information The online version                       use is not permitted by statutory regulation or exceeds the permitted
contains supplementary material available at                       use, you will need to obtain permission directly from the copyright
https://doi.org/10.1038/s42256-024-00832-8.                        holder. To view a copy of this licence, visit http://creativecommons.
                                                                   org/licenses/by/4.0/.
Correspondence and requests for materials should be addressed to
Andrew D. White or Philippe Schwaller.                             © The Author(s) 2024




Nature Machine Intelligence | Volume 6 | May 2024 | 525–535                                                                              535
