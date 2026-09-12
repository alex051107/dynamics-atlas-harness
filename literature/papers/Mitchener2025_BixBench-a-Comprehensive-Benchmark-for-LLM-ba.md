# BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology

**Authors:** Ludovico Mitchener, Jon M Laurent, Alex Andonian, Benjamin Tenmann, Siddharth Narayanan, Geemi P Wellawatte, Andrew White, Lorenzo Sani, Samuel G Rodriques
**Year:** 2025
**Venue:** arXiv preprint
**DOI:** 10.48550/arXiv.2503.00096
**Source PDF URL:** https://arxiv.org/pdf/2503.00096
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

                                                    BixBench: a Comprehensive Benchmark for LLM-based Agents in
                                                                      Computational Biology


                                              Ludovico Mitchener * 1 Jon M Laurent * 1 Alex Andonian * 1 Benjamin Tenmann 2 Siddharth Narayanan 1
                                                           Geemi P Wellawatte 1 Andrew White 1 Lorenzo Sani 2 Samuel G Rodriques 1


                                                                    Abstract                             1   Introduction




arXiv:2503.00096v3 [q-bio.QM] 8 Oct 2025
                                                                                                         Accelerating scientific discovery across domains is a core
                                                                                                         aspiration for modern AI models and agents, driven by the
                                                Large Language Models (LLMs) and LLM-based               ability of these systems to synthesize information and iden-
                                                agents show great promise in accelerating sci-           tify novel connections across disparate fields (Skarlinski
                                                entific research. Existing benchmarks for mea-           et al., 2024). While significant progress has been made in
                                                suring this potential and guiding future develop-        developing systems for automating certain aspects of the
                                                ment continue to evolve from pure recall and             scientific research process (Lu et al., 2024; Gao et al., 2024;
                                                rote knowledge tasks, towards more practical             Swanson et al., 2024; Schmidgall et al., 2025; Narayanan
                                                work such as literature review and experimen-            et al., 2024), the ultimate realization of fully automated
                                                tal planning. Bioinformatics is a domain where           scientific systems remains elusive.
                                                fully autonomous AI-driven discovery may be
                                                                                                         The analysis of experimental data is fundamental to sci-
                                                near, but no extensive benchmarks for measur-
                                                                                                         entific research (Deshpande et al., 2024). Given the scale
                                                ing progress have been introduced to date. We
                                                                                                         of data being produced by modern technologies and the
                                                therefore present the Bioinformatics Benchmark
                                                                                                         complexity of analytical approaches, disciplines like bioin-
                                                (BixBench), a dataset comprising over 60 real-
                                                                                                         formatics and computational biology have become research
                                                world scenarios of practical biological data anal-
                                                                                                         fields in their own right. These specialties can present a
                                                ysis with over 200 associated open-answer ques-
                                                                                                         microcosm of the scientific process where hypotheses and
                                                tions designed to measure the ability of LLM-
                                                                                                         research questions drive analytical, statistical and computa-
                                                based agents to explore biological datasets, per-
                                                                                                         tional approaches to uncover new knowledge from a variety
                                                form long, multi-step analytical trajectories, and
                                                                                                         of data sources, at times independently from traditional lab-
                                                interpret the nuanced results of those analyses.
                                                                                                         oratory experiments. This disconnect from the physical
                                                We evaluate the performance of two frontier
                                                                                                         laboratory offers an opportunity to develop AI systems for
                                                LLMs (GPT-4o and Claude 3.5 Sonnet) using
                                                                                                         exploring data with the sophistication of expert bioinfor-
                                                a custom agent framework we open source. We
                                                                                                         maticians but at significantly larger scale and more rapid
                                                find that even the latest frontier models achieve
                                                                                                         pace. Hence, bioinformatics stands as one of the first fields
                                                only 21% accuracy in the open-answer regime,
                                                                                                         where fully autonomous scientific systems may become a
                                                and marginally better than random in a multiple-
                                                                                                         reality.
                                                choice setting. By exposing the current limita-
                                                tions of frontier models, we hope BixBench               As with any applied AI system, quantitatively assessing per-
                                                can spur the development of agents capable of            formance on benchmarks serves as a primary measure of
                                                conducting rigorous bioinformatic analysis and           progress (Chang et al., 2023; Huang et al., 2021; Wognum
                                                accelerate scientific discovery.                         et al., 2024). Countless such benchmarks have been cre-
                                                                                                         ated for assessing capabilities such as image segmentation,
                                                                                                         natural language understanding, and protein-ligand bind-
                                                                                                         ing (Zhou et al., 2017; Hendrycks et al., 2020; Quigley
                                                                                                         et al., 2024). More recently, groups have published bench-
                                             *                       1
                                               Equal contribution      FutureHouse, San Francisco,       marking datasets focused on high-complexity tasks with
                                           USA 2 ScienceMachine, London, UK. Correspondence to:          real-world biological research applicability (Laurent et al.,
                                           Samuel G Rodriques <sam@futurehouse.org>, Lorenzo Sani        2024). These real-world benchmarks are already proving
                                           <lorenzo@sciencemachine.ai>.
                                                                                                         their value in driving development of scientific agents, in-
                                           Copyright 2025 by the author(s).                              cluding ones that are surpassing human expert performance

                                                                                                     1
                                                           BixBench




Figure 1: BixBench benchmark creation diagram. (A) To create the initial seed capsules, expert bioinformaticians assembled
a code notebook and provided input data and metadata including a hypothesis, result, etc. Seed capsules were reviewed by
other experts before being merged to final corpus. (B) To generate benchmark tasks, we first asked an LLM to propose
candidate questions for each capsule. These questions were reviewed by multiple experts, yielding the final dataset.


on research activities like literature review and DNA con-           multiple-choice (MCQ) framework using majority voting,
struct engineering (Narayanan et al., 2024; Skarlinski et al.,       performance was no better than random guessing. We also
2024). However, systems capable of truly open-ended scien-           provide extensive validation of our experimental setup, in-
tific exploration and benchmarks for assessing them, remain          vestigating potential data leakage, hyperparameter optimiza-
elusive.                                                             tion, and frontier model choice.
To help bridge this gap, we introduce the Bioinformatics
Benchmark (BixBench). The benchmark is composed of                   1.1       Primary Contributions
61 real-world analytical scenarios, each a pairing of guiding        The primary contributions of our work are as follows:
questions with heterogeneous input data files. These scenar-
ios present a realistic environment in which an autonomous
agent is expected to perform appropriate analyses given               1. An expert-curated set of 61 analytical scenarios and
minimal prompting and context. Performing well on the                    205 open-answer questions in the domain of bioinfor-
benchmark requires being simultaneously skilled in under-                matics and computational biology. 1
standing the subtleties of a research question, exploring data
and understanding how it relates to the question, performing          2. A framework for assessing the performance of AI
multi-step computational analyses, and finally interpreting              agents in biological data analysis, including key met-
the results in the context of the initial research question.             rics and calibrations. 2 .
To assess the capabilities of current AI models for perform-
ing these types of analyses, we present results of two fron-          3. An open-source agent framework for writing and ex-
tier models (GPT-4o from OpenAI (Hurst et al., 2024) and                 ecuting Python, R and bash code in a Jupyter notebook
Claude 3.5 Sonnet from Anthropic (Anthropic, 2024)) in-                  environment.
tegrated into a custom agent framework and evaluated on                    1
                                                                         The benchmark dataset can be found at https:
BixBench. We find that frontier models perform poorly                //huggingface.co/datasets/futurehouse/
overall (∼ 21% accuracy at best) in the primary open-                BixBench
answer evaluation format. When evaluated in a modified                 2
                                                                         An eval harness and reproducible code can be found at
                                                                     https://github.com/Future-House/BixBench

                                                                 2
                                                            BixBench

2     Related Work                                                    In science, most analytical tasks are ambiguous, open-ended,
                                                                      and do not benefit from having a clear optimization metric
2.1   Data Science and Engineering Benchmarks.                        to verify performance. We developed BixBench to bridge
LLMs have become increasingly popular for their code-                 this gap and provide a benchmark that evaluates challenging
writing abilities, and associated benchmarks such as SWE-             multi-step analytical capabilities in complex, ambiguous re-
Bench (Jimenez et al., 2024), BigCodeBench (Zhuo et al.,              search tasks without being artificially constrained to specific
2024), and HumanEval (Chen et al., 2021) have become in-              environments, tools, or tasks.
dispensable for measuring their performance. More applied
benchmarks like ML-Bench (Tang et al., 2024a), MLE-                   3     Methods
Bench (Chan et al., 2024), MLAgentBench (Huang et al.,
2024a), and SUPER (Bogin et al., 2024) for Machine Learn-             3.1     Benchmark creation
ing research and coding are important barometers for the              3.1.1     A NALYST RECRUITMENT
development of agents in specific domains. Similarly, there
has been an explosion in the number of benchmarks aimed               To develop BixBench, we systematically assembled a di-
at evaluating the ability of LLM-based agents to write and            verse collection of analytical trajectories representing canon-
execute increasingly complex analytical workflows (Jing               ical tasks in bioinformatics research (Figure 2). We recruited
et al., 2024; Huang et al., 2024b; Gu et al., 2024; Wijk              expert analysts through multiple channels: our own profes-
et al., 2024). Tasks within these benchmarks range from               sional networks, reaching out to authors of bioinformatics
simple data-frame operations to solving complex research              papers, and recruiting through affiliated research institutions.
engineering tasks. Benchmarks like RE-Bench (Wijk et al.,             Our team of contracted analysts consists exclusively of PhD
2024) require complex, iterative problem-solving, but rely            holders or candidates in bioinformatics and related fields,
on a simple reward function such as training loss to guide            each with extensive experience in biological data analysis
an agent’s performance. On the other end of the spectrum,             as their primary research focus.
benchmarks like BLADE (Gu et al., 2024) present broader
analysis scenarios similar to those introduced here, but are
artificially constrained to producing specific artifacts and
making specific statistical choices.

2.2   Benchmarks for Scientific Agents
As the potential for applying LLMs and agents for scien-
tific discovery has become more and more apparent, several
benchmarking suites have been proposed for measuring the
ability to complete key scientific tasks previously reserved
for humans. These include ChemBench (Mirza et al., 2024),             Figure 2: Histogram of capsules in a broad set of self-
which tests models on a wide range of chemistry tasks, and            selected analytical categories.
LAB-Bench (Laurent et al., 2024) which is composed of a
large set of real-world biology research tasks ranging from
literature review to DNA sequence manipulation and pro-               3.1.2     C APSULE CREATION
tocol troubleshooting, as does BioLPBench (Ivanov, 2024).
Yin et al (Yin et al., 2024) and BioLLMBench (Sarwal et al.,          We refer to our gathered analytical trajectories and asso-
2023) were some of the early attempts at benchmarking                 ciated data as analysis “capsules”. An analysis capsule
LLMs on bioinformatics across several constrained task                consists of three primary components: 1) A hypothesis
types. CORE-Bench (Siegel et al., 2024) assesses a criti-             or research question driving the analysis, 2) input data
cally important aspect of scientific research, reproducibility,       going into the analysis, and 3) code for carrying out the
by assessing agents’ ability to recapitulate published com-           analysis. We also captured a result (a few sentences
putational analyses given all the necessary materials and             describing the primary result of the analysis as it pertains
environment. Closer to BixBench in scope and goal are                 to the hypothesis) and answer, a true/false assessment of
benchmarks like BioCoder (Tang et al., 2024b) that tests              whether or not the hypothesis was supported by the analysis,
bioinformatics code generation and function calling across            as well as some additional metadata.
a defined function set, as well as ScienceAgentBench (Chen            Contract analysts were asked to recapitulate published anal-
et al., 2024) and DiscoveryBench (Majumder et al., 2024),             yses or produce relevant de novo analytical trajectories from
which assess agents’ ability to analyze data and uncover              data they provided. To retain flexibility while maintaining
similar discoveries to published analyses.                            a standardized environment, we captured code in Jupyter

                                                                  3
                                                           BixBench

                                  Table 1: BixBench comparison to related benchmarks

             Benchmark               Time (h)     Task #    Eval              Multi-lang.     Science    Avg lines
             DA-Code                       0.1       500    Verifier          "               %                 85
             DSBench                        17       540    Verifier          %               %                 75
             MLE Bench                     2.5        75    Reward            %               %                  -
             REBench                         8         7    Reward            "               %                650
             BLADE                         1.5       188    MCQ               %               "                 75
             ScienceAgentBench             2.5       102    Verifier          %               "                 58
             BixBench (ours)               4.2       205    Open-ended        "               "                106


notebooks using Google Colab. We provided a user inter-             prompted to flag any duplicated questions. This step was per-
face through which analysts could initiate a new capsule,           formed in triplicate and manually assessed for concordance
providing a template code notebook and a mechanism to up-           across the three responses (we estimated approximately 95%
load and store their capsule data files. Some capsules used         concordance). Duplicates were manually verified and re-
publicly accessible data obtained via code (e.g. with wget),        moved if appropriate, and the duplicate flag request to the
for which we retrieved the data separately for persistence.         LLM was repeated with the trimmed set of questions. This
Analysts were allowed to use Python, R, or bash commands            was repeated until no questions were flagged as duplicates.
inside the notebook environment, and could install any pack-        The final task set consists of 205 questions covering 61
ages necessary for their trajectory.                                analytical capsules, each having one to seven associated
                                                                    questions (averaging 3.8 questions per capsule).
Capsules and their trajectories were thoroughly reviewed by
the authors and in some cases by other analysts, to arrive at
a final approved set of 61 analytical scenarios.

3.1.3   TASK GENERATION
To generate the MCQ-based tasks comprising BixBench,
we devised a multi-stage generation and review process. We
employed an LLM, specifically Claude 3.5 Sonnet from
Anthropic (20241022 release), to generate initial drafts of
multiple-choice questions (MCQs) related to the analysis
in the capsule. We provided a modified version of the code
notebook, the hypothesis and result, and a specially crafted
prompt to produce MCQs. We generated question drafts
for each capsule in two rounds of four questions each, for a
total of eight MCQ drafts per capsule.
The second stage of task generation was human expert re-
view. Our analysts were provided the model-generated ques-
tions and answer options, and allowed full edit access for
each. They were provided review instructions to Approve             Figure 3: BixBench evaluation. An agent is provided a task
or Reject, with or without editing. They were also able to          capsule, consisting of data and associated questions. The
see and re-review previously reviewed questions to identify         agent environment contains an empty code notebook in a
mistakes in the review process itself. To provide complete          docker environment pre-loaded with many popular bioin-
context for the questions, the reviewers were also provided         formatics packages, with three tools to manipulate the en-
access to the original capsules, including notebooks and            vironment. In the open-response regime (A) the agent’s
data files.                                                         submitted answer is compared directly to the ground truth
                                                                    answer by a separate LLM call. In the MCQ regime (B) a
Because we generated MCQs in two separate rounds, the
                                                                    second LLM is given the agent notebook and answer, and
final stage of task generation after expert review was dupli-
                                                                    asked to choose from the available options.
cate filtering. The set of Approved questions for a capsule
were provided to an LLM (Claude 3.5 Sonnet) which was


                                                                4
                                                          BixBench

3.2     Benchmark Evaluation                                        tools:
3.2.1     OVERVIEW
BixBench was developed to serve as a benchmark for real-               • edit cell: Allows the agent to select, modify and
world bioinformatics capabilities. As such, we aimed to                  execute a cell within a Jupyter Notebook.
present realistic scenarios that a bioinformatician or com-
putational biologist might face. Thus, at evaluation time,             • list workdir: Enables the model to inspect its
we present an agent with an empty Jupyter notebook, a set                own workspace directory recursively to ascertain the
of input data files, and several relevant questions for the              structure and format of the dataset.
agent to answer. The agent thus has free reign to explore the
data, make its own assumptions and plan its own analyses
                                                                       • submit answer: Used by the model to finalize and
in order to answer the questions presented. This approach
                                                                         submit an open-answer.
addresses key challenges in evaluating complex scientific
tasks: the need for iterative analysis, access to specialized
software environments, and open-answering. In practice,             At each timestep, the model must decide which tool to in-
bioinformaticians do not have access to multiple-choice op-         voke. The agent then receives observations from the tool’s
tions and so open-answer is our preferred evaluation method.        execution. Each code modification triggers a full rerun of
However, we are also able to perform multiple-choice eval-          the notebook, allowing the model to view results in tabular
uations with options to determine how that may influence            or plot formats as well as debug tracebacks. Prompt en-
performance in answering the questions.                             gineering was explored extensively as a means to improve
                                                                    performance. An example of the final prompt used to initiate
3.2.2     AGENT I NFRASTRUCTURE                                     an agent trajectory is shared in the Appendix A.
We implemented our agent framework using Aviary, an ex-
tensible gymnasium for language agents (Narayanan et al.,           3.2.4    E VALUATION
2024). Aviary was selected for its ability to provide a con-        Open-answer To more fully mimic evaluation of a real-
trolled environment supporting tool use and multi-step rea-         world scenario of an autonomous analysis agent, we are pri-
soning. The framework enables reproducible evaluation by            marily interested in open-answer responses to the prompted
maintaining consistent software environments and tool ac-           questions rather than the more popular MCQ paradigm.
cess across different model evaluations. The agentic prompt-        During the agent analysis trajectory, it is able to call the
ing approach we used is based on the SimpleAgent approach           submit answer tool when it is ready to answer the ques-
in Aviary.                                                          tions, which triggers the end of the trajectory. The final
To ensure reproducibility and isolate model evalua-                 submitted answer is then automatically evaluated by a judge
tion from environment setup complexity, all analy-                  LLM (Claude 3.5 Sonnet) by comparing the agent-generated
ses are executed within a pre-built Docker container                response against a ground-truth solution, with correctness
(BixBench-env:v1.0). This container includes exten-                 assigned as a binary score (1 if correct, 0 otherwise). To
sive Python, R, and Bash packages commonly used in bioin-           account for stochastic trajectories, we run each analysis in
formatics workflows. This ensures that evaluation remains           parallel five times to calculate overall performance.
focused on problem-solving capabilities rather than on soft-        Multiple-choice Due to the challenging nature of the open-
ware installation or dependency resolution—mimicking real-          answer benchmark, we also provide the option to evaluate
world bioinformatics workflows, where researchers often             agents’ performance via MCQ. We believe this will serve
operate within standardized, pre-configured environments.           as a useful proxy evaluation on the journey to building a
Agents must still identify and load packages necessary for          truly autonomous bioinformatician. Specifically, after the
the analyses they want to carry out.                                analyses are complete, we can pass the complete analy-
                                                                    sis notebooks to an LLM, along with the initial question
3.2.3     N OTEBOOK A NALYSIS WITH AGENTIC                          now provided with the multiple-choice answer options, and
          E XECUTION                                                the open-answer response from the initial agent run. This
Given that bioinformatics tasks involve complex computa-            second LLM is prompted to choose the most appropriate
tions requiring specialized software environments, we im-           answer option. Importantly, we also provide an “opt-out“
plement an agentic scaffold within a controlled execution           for the model in answering the MCQ by providing an “Insuf-
environment. This scaffold allows the LLM to iteratively            ficient information“ refusal option. To evaluate performance
refine its analysis in a structured manner. We leverage the         on the MCQs, we further employ majority voting over the
Aviary framework to provide the agent with three distinct           five runs to derive a majority-based consensus across the
                                                                    iterations.

                                                                5
                                                            BixBench




Figure 4: Overall model performance. Models perform poorly in the purely open-answer regime (left bars) and display
increasing performance in the MCQ with refusal regime and further increased performance with MCQs without a refusal
option. Performance does not surpass a baseline assessed as performance on the questions given to the model without access
to any analysis notebook to base answers in (i.e. pure model recall.)


3.2.5     M ODEL S ELECTION AND E VALUATION                           of current frontier models to perform open-ended analytical
                                                                      tasks in the BixBench benchmark, we open-source a con-
We have restricted our current evaluation to GPT-4o and
                                                                      figurable agentic notebook environment based on Aviary, a
Claude due to their demonstrated capabilities in structured
                                                                      public agent scaffold (Narayanan et al., 2024). Using our
output generation and handling of extended contexts, pre-
                                                                      framework, we evaluate SOTA performance on BixBench
requisites for complex analytical workflows. During our
                                                                      with two frontier AI models, GPT-4o from OpenAI and
preliminary tests we found that reasoning models such as
                                                                      Claude 3.5 Sonnet from Anthropic.
o1 and DeepSeek R1 struggled to perform such tasks due
to the long contexts and the structured outputs required for          We also assess the impact of scaling inference-time com-
agentic tool use.                                                     pute, by performing five parallel iterations of each capsule
                                                                      resulting in the collection of 305 trajectories across two dif-
                                                                      ferent models (4o and Claude) and two different modalities
4     Results
                                                                      (with and without images) resulting in 1,220 total trajec-
4.1     Benchmark assembly and description                            tories. Performance on a question is primarily calculated
                                                                      as accuracy, the fraction of correct answers given across
The BixBench dataset comprises 61 real-world analyt-                  all parallel runs over all questions provided. In the MCQ
ical scenarios or “capsules” with 205 associated open-                case, we also conduct majority voting across the five iter-
answer questions. Each capsule is thus composed of input              ations and report precision (questions answered correctly
data files and a set of guiding open-answer questions in-             over all questions answered, i.e. those that were not an-
tended only to be answerable upon completion of a valid               swered with the “Refusal” option.) The evaluation scheme
analysis (Figure 3). In Table 1 we compare BixBench to                is diagrammed in Figure 3. Finally, we conduct ablations on
other similar benchmarks. BixBench differentiates itself              the presence of the refusal option and the use of images/plots
as the first benchmark focused on open-ended scientific data          in the notebooks.
analysis, requiring long and complex multi-step trajectories.
                                                                      Results over all questions and trajectories are presented
Capsules contain data files in various formats, type (e.g. csv,       in Figure 4 (open-answer, left-most bars, MCQ, right two
rds) and directory structure requiring effective workspace            bar pairs.) Overall, BixBench proved very challenging
navigation and appropriate use of libraries to load and pro-          for existing frontier models, even when provided with a
cess heterogeneous data. While frontier models have demon-            custom agent scaffold and associated tools. Claude 3.5
strated proficiency in code writing given user-provided               Sonnet bested GPT-4o with 21% accuracy vs. 15% in the
prompts, they do not typically come pre-built with con-               open-answer evaluation regime. As a further calibration,
figurable code interpreters. Thus, to assess the capabilities         we measure the pure recall performance of both models by


                                                                  6
                                                            BixBench




Figure 5: Performance of models in the MCQ regime relative to number of votes with ablations of refusal (top plot) and
image generation (bottom.) Note that in the vision ablation the refusal option is present and the agents are prompt engineered
to not produce images/plots. In the refusal ablation agents are free to use images/plots.


asking the BixBench questions without any notebook or                 given the option in the context of a complex analysis. When
other context, as indicated by the solid gray line in Figure 4.       only given real answer options without a refusal option,
In the MCQ regime, overall performance between models                 performance is higher and above random (Figure 4.) When
was closer than open-answer (Figure 4,) though Claude 3.5             further evaluating this effect in a majority voting scenario
Sonnet remained the clear higher performer between the                across the five trajectories for each question, we don’t see
two models.                                                           any significant deviation as vote counts accumulate in either
                                                                      refusal or no-refusal regimes (Figure 5), top plot.)
The questions contained in BixBench are intended by
design not to be answerable by model recall, i.e. they should         Interestingly, we noted during question generation and other
require completion of some analysis to answer. During the             testing that the models seemed to do a poor job of inter-
MCQ answering process we prompt engineered the agent to               preting plots in the notebooks generated both by humans
answer only using the analysis notebook. To investigate the           and the agents themselves, something previously observed
“ethics” of the models in this context (i.e. their willingness        in a benchmark of model performance on understanding
to answer even if they don’t like the options), we performed          scientific figures (xxcite lab-benc, figqa). We reasoned that
the MCQ evaluation in two scenarios: with refusal, where              even the multimodal models used here may be able to rea-
the agent is provided an “insufficient information” answer as         son more effectively over the underlying text or data rather
one of the options, and without refusal, where no such option         than plots themselves, and thus performed an ablation where
is provided. Overall, when provided the refusal option, both          the agent was prompted not to generate images during its
models performed very close to random (Figure 4, middle               analysis. However, we did not observe a significant effect
bars) indicating their tendency to opt-out of answering when          on actual benchmark results between being free to generate


                                                                  7
                                                            BixBench

or disallowed to generate images (Figure 5, bottom plot.)             tasks were generated de novo by such human experts, we
                                                                      anticipate that additional human experts would perform
5     Discussion                                                      significantly higher than the agent performance reported
                                                                      here, and thus did not prioritize gathering this data. We are
Biological data analysis and associated domains offer an              currently exploring options for doing so.
opportunity to build the first agents for scientific discovery,
and thus assessing the state of progress is critical. We’ve           5.1.3   E VALUATING ADDITIONAL MODELS
introduced here BixBench, a benchmark and evaluation
                                                                      Reasoning models, introduced recently in (OpenAI et al.,
framework for measuring agent performance on real-world
                                                                      2024; DeepSeek-AI et al., 2025) and others have rapidly
bioinformatics tasks. BixBench presents 61 real-world
                                                                      topped many benchmarks, including MLE-bench. It is still
analytical scenarios, along with a set of 205 associated
                                                                      early to incorporate them into environments, with few details
questions, supporting both open-answer or multiple-choice
                                                                      or results on tool calling. They hold promise for future work
evaluation regimes.
                                                                      due to their ability to improve performance from binary
In measuring the performance of two current frontier models           reward signals, like the capsules we introduce here (Team,
on our benchmark, we find that there is significant devel-            2025; Lambert et al., 2025; DeepSeek-AI et al., 2025).
opment necessary to achieve the goal of an autonomous
bioinformatician. When assessed in an open-answer envi-
                                                                      References
ronment, the models perform at just 21% overall accuracy
in answering questions related to the analyses. When using            Anthropic. Introducing the next generation of claude, March
multiple-choice versions of the same questions to interpret             2024.      URL https://www.anthropic.com/
answers from the analyses, overall performance increases,               news/claude-3-5-sonnet. Accessed: 2024-07-
though not substantially and only marginally above random              11.
(Figure 3). Of note, when removing the option to abstain
from answering the performance again increases, which we              Bogin, B., Yang, K., Gupta, S., Richardson, K., Bransom, E.,
speculate is due in large part to the model relying on answer-          Clark, P., Sabharwal, A., and Khot, T. SUPER: Evaluating
ing via recall rather than the information contained in the             Agents on Setting Up and Executing Tasks from Research
analysis.                                                               Repositories, September 2024. URL http://arxiv.
                                                                        org/abs/2409.07440. arXiv:2409.07440 [cs].
Ultimately, BixBench highlights a fundamental shortcom-
ing in current LLM capabilities for conducting rigorous               Chan, J. S., Chowdhury, N., Jaffe, O., Aung, J., Sherburn,
bioinformatics research, and will thus be a valuable resource           D., Mays, E., Starace, G., Liu, K., Maksin, L., Patward-
to guide development of these capabilities and accelerate               han, T., et al. Mle-bench: Evaluating machine learning
discovery across biology.                                               agents on machine learning engineering. arXiv preprint
                                                                        arXiv:2410.07095, 2024.
5.1     Future Work
                                                                      Chang, Y., Wang, X., Wang, J., Wu, Y., Yang, L., Zhu, K.,
5.1.1     F URTHER SAMPLING OF THE FIELD                                Chen, H., Yi, X., Wang, C., Wang, Y., Ye, W., Zhang,
                                                                        Y., Chang, Y., Yu, P. S., Yang, Q., and Xie, X. A survey
While we consider BixBench to be a highly representa-
                                                                        on evaluation of large language models, 2023. URL
tive benchmark, building a truly comprehensive benchmark
                                                                        https://arxiv.org/abs/2307.03109.
of tasks for AI models in bioinformatics and computation
biology would be extraordinarily difficult, and we acknowl-           Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. d. O.,
edge that there are many important workflows, pipelines,                Kaplan, J., Edwards, H., Burda, Y., Joseph, N., Brock-
statistical approaches, data types, and other parameters that           man, G., Ray, A., Puri, R., Krueger, G., Petrov, M.,
are missing from BixBench. These will be important ad-                  Khlaaf, H., Sastry, G., Mishkin, P., Chan, B., Gray, S.,
ditional improvements as related benchmarks and agents                  Ryder, N., Pavlov, M., Power, A., Kaiser, L., Bavarian,
continue to be developed.                                               M., Winter, C., Tillet, P., Such, F. P., Cummings, D.,
                                                                        Plappert, M., Chantzis, F., Barnes, E., Herbert-Voss, A.,
5.1.2     H UMAN BASELINE COMPARISON                                    Guss, W. H., Nichol, A., Paino, A., Tezak, N., Tang,
An important extension of the current work would be the                 J., Babuschkin, I., Balaji, S., Jain, S., Saunders, W.,
additional of a human baseline comparison, where human                  Hesse, C., Carr, A. N., Leike, J., Achiam, J., Misra,
bioinformatics experts are tasked with performing the same              V., Morikawa, E., Radford, A., Knight, M., Brundage,
analyses and answering the same questions as the agents                 M., Murati, M., Mayer, K., Welinder, P., McGrew, B.,
here. As the seed capsules used to generate BixBench                    Amodei, D., McCandlish, S., Sutskever, I., and Zaremba,
                                                                        W. Evaluating Large Language Models Trained on Code,

                                                                  8
                                                            BixBench

  July 2021. URL http://arxiv.org/abs/2107.                             Schwarz, J. R., Ektefaie, Y., Kondic, J., and Zitnik, M.
  03374. arXiv:2107.03374 [cs] version: 2.                              Empowering biomedical discovery with ai agents, 2024.
                                                                        URL https://arxiv.org/abs/2404.02831.
Chen, Z., Chen, S., Ning, Y., Zhang, Q., Wang, B., Yu,
  B., Li, Y., Liao, Z., Wei, C., Lu, Z., Dey, V., Xue,                Gu, K., Shang, R., Jiang, R., Kuang, K., Lin, R.-J., Lyu, D.,
  M., Baker, F. N., Burns, B., Adu-Ampratwum, D.,                       Mao, Y., Pan, Y., Wu, T., Yu, J., et al. Blade: Benchmark-
  Huang, X., Ning, X., Gao, S., Su, Y., and Sun, H. Sci-                ing language model agents for data-driven science. arXiv
  enceAgentBench: Toward Rigorous Assessment of Lan-                    preprint arXiv:2408.09667, 2024.
  guage Agents for Data-Driven Scientific Discovery, Oc-
  tober 2024. URL http://arxiv.org/abs/2410.                          Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika,
  05080. arXiv:2410.05080 [cs].                                         M., Song, D., and Steinhardt, J. Measuring mas-
                                                                        sive multitask language understanding. arXiv preprint
DeepSeek-AI, Guo, D., Yang, D., Zhang, H., Song, J.,                    arXiv:2009.03300, 2020.
  Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X.,
  Zhang, X., Yu, X., Wu, Y., Wu, Z. F., Gou, Z., Shao,                Huang, K., Fu, T., Gao, W., Zhao, Y., Roohani, Y., Leskovec,
  Z., Li, Z., Gao, Z., Liu, A., Xue, B., Wang, B., Wu, B.,              J., Coley, C. W., Xiao, C., Sun, J., and Zitnik, M. Ther-
  Feng, B., Lu, C., Zhao, C., Deng, C., Zhang, C., Ruan,                apeutics data commons: Machine learning datasets and
  C., Dai, D., Chen, D., Ji, D., Li, E., Lin, F., Dai, F., Luo,         tasks for drug discovery and development. arXiv preprint
  F., Hao, G., Chen, G., Li, G., Zhang, H., Bao, H., Xu,                arXiv:2102.09548, 2021.
  H., Wang, H., Ding, H., Xin, H., Gao, H., Qu, H., Li,               Huang, Q., Vora, J., Liang, P., and Leskovec, J. MLA-
  H., Guo, J., Li, J., Wang, J., Chen, J., Yuan, J., Qiu, J.,           gentBench: Evaluating Language Agents on Machine
  Li, J., Cai, J. L., Ni, J., Liang, J., Chen, J., Dong, K.,            Learning Experimentation, April 2024a. URL http://
  Hu, K., Gao, K., Guan, K., Huang, K., Yu, K., Wang, L.,               arxiv.org/abs/2310.03302. arXiv:2310.03302
  Zhang, L., Zhao, L., Wang, L., Zhang, L., Xu, L., Xia,                [cs].
  L., Zhang, M., Zhang, M., Tang, M., Li, M., Wang, M.,
  Li, M., Tian, N., Huang, P., Zhang, P., Wang, Q., Chen,             Huang, Y., Luo, J., Yu, Y., Zhang, Y., Lei, F., Wei, Y., He, S.,
  Q., Du, Q., Ge, R., Zhang, R., Pan, R., Wang, R., Chen,               Huang, L., Liu, X., Zhao, J., et al. Da-code: Agent data
  R. J., Jin, R. L., Chen, R., Lu, S., Zhou, S., Chen, S., Ye,          science code generation benchmark for large language
  S., Wang, S., Yu, S., Zhou, S., Pan, S., Li, S. S., Zhou,             models. arXiv preprint arXiv:2410.07331, 2024b.
  S., Wu, S., Ye, S., Yun, T., Pei, T., Sun, T., Wang, T.,
  Zeng, W., Zhao, W., Liu, W., Liang, W., Gao, W., Yu, W.,            Hurst, A., Lerer, A., Goucher, A. P., Perelman, A., Ramesh,
  Zhang, W., Xiao, W. L., An, W., Liu, X., Wang, X., Chen,              A., Clark, A., Ostrow, A., Welihinda, A., Hayes, A.,
  X., Nie, X., Cheng, X., Liu, X., Xie, X., Liu, X., Yang,              Radford, A., et al. Gpt-4o system card. arXiv preprint
  X., Li, X., Su, X., Lin, X., Li, X. Q., Jin, X., Shen, X.,            arXiv:2410.21276, 2024.
  Chen, X., Sun, X., Wang, X., Song, X., Zhou, X., Wang,              Ivanov, I. BioLP-bench: Measuring understanding of
  X., Shan, X., Li, Y. K., Wang, Y. Q., Wei, Y. X., Zhang,              biological lab protocols by large language models,
 Y., Xu, Y., Li, Y., Zhao, Y., Sun, Y., Wang, Y., Yu, Y.,               October 2024. URL https://www.biorxiv.org/
  Zhang, Y., Shi, Y., Xiong, Y., He, Y., Piao, Y., Wang, Y.,            content/10.1101/2024.08.21.608694v4.
  Tan, Y., Ma, Y., Liu, Y., Guo, Y., Ou, Y., Wang, Y., Gong,            Pages: 2024.08.21.608694 Section: New Results.
 Y., Zou, Y., He, Y., Xiong, Y., Luo, Y., You, Y., Liu, Y.,
  Zhou, Y., Zhu, Y. X., Xu, Y., Huang, Y., Li, Y., Zheng,             Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press,
 Y., Zhu, Y., Ma, Y., Tang, Y., Zha, Y., Yan, Y., Ren, Z. Z.,           O., and Narasimhan, K. SWE-bench: Can Language
  Ren, Z., Sha, Z., Fu, Z., Xu, Z., Xie, Z., Zhang, Z., Hao,            Models Resolve Real-World GitHub Issues?, Novem-
  Z., Ma, Z., Yan, Z., Wu, Z., Gu, Z., Zhu, Z., Liu, Z., Li,            ber 2024. URL http://arxiv.org/abs/2310.
  Z., Xie, Z., Song, Z., Pan, Z., Huang, Z., Xu, Z., Zhang,             06770. arXiv:2310.06770 [cs].
  Z., and Zhang, Z. Deepseek-r1: Incentivizing reasoning
                                                                      Jing, L., Huang, Z., Wang, X., Yao, W., Yu, W., Ma, K.,
  capability in llms via reinforcement learning, 2025. URL
                                                                         Zhang, H., Du, X., and Yu, D. Dsbench: How far are data
  https://arxiv.org/abs/2501.12948.
                                                                         science agents to becoming data science experts? arXiv
Deshpande, D., Chhugani, K., Ramesh, T., Pellegrini, M.,                 preprint arXiv:2409.07703, 2024.
  Shiffman, S., Abedalthagafi, M. S., Alqahtani, S., Ye, J.,
  Liu, X. S., Leek, J. T., et al. The evolution of compu-             Lambert, N., Morrison, J., Pyatkin, V., Huang, S., Ivison, H.,
  tational research in a data-centric world. Cell, 187(17):             Brahman, F., Miranda, L. J. V., Liu, A., Dziri, N., Lyu, S.,
  4449–4457, 2024.                                                      Gu, Y., Malik, S., Graf, V., Hwang, J. D., Yang, J., Bras,
                                                                        R. L., Tafjord, O., Wilhelm, C., Soldaini, L., Smith, N. A.,
Gao, S., Fang, A., Huang, Y., Giunchiglia, V., Noori, A.,               Wang, Y., Dasigi, P., and Hajishirzi, H. Tulu 3: Pushing

                                                                  9
                                                           BixBench

  frontiers in open language model post-training, 2025.                 F., Sulit, F., Salmon, G., Parascandolo, G., Chabot, G.,
  URL https://arxiv.org/abs/2411.15124.                                 Zhao, G., Brockman, G., Leclerc, G., Salman, H., Bao,
                                                                        H., Sheng, H., Andrin, H., Bagherinezhad, H., Ren, H.,
Laurent, J. M., Janizek, J. D., Ruzo, M., Hinks, M. M.,                 Lightman, H., Chung, H. W., Kivlichan, I., O’Connell,
  Hammerling, M. J., Narayanan, S., Ponnapati, M., White,               I., Osband, I., Gilaberte, I. C., Akkaya, I., Kostrikov, I.,
  A. D., and Rodriques, S. G. Lab-bench: Measuring capa-                Sutskever, I., Kofman, I., Pachocki, J., Lennon, J., Wei,
  bilities of language models for biology research. arXiv               J., Harb, J., Twore, J., Feng, J., Yu, J., Weng, J., Tang, J.,
  preprint arXiv:2407.10362, 2024.                                      Yu, J., Candela, J. Q., Palermo, J., Parish, J., Heidecke,
                                                                        J., Hallman, J., Rizzo, J., Gordon, J., Uesato, J., Ward,
Lu, C., Lu, C., Lange, R. T., Foerster, J., Clune, J., and Ha,
                                                                        J., Huizinga, J., Wang, J., Chen, K., Xiao, K., Singhal,
  D. The ai scientist: Towards fully automated open-ended
                                                                        K., Nguyen, K., Cobbe, K., Shi, K., Wood, K., Rimbach,
  scientific discovery. arXiv preprint arXiv:2408.06292,
                                                                        K., Gu-Lemberg, K., Liu, K., Lu, K., Stone, K., Yu, K.,
  2024.
                                                                        Ahmad, L., Yang, L., Liu, L., Maksin, L., Ho, L., Fedus,
Majumder, B. P., Surana, H., Agarwal, D., Mishra, B. D.,                L., Weng, L., Li, L., McCallum, L., Held, L., Kuhn, L.,
 Meena, A., Prakhar, A., Vora, T., Khot, T., Sabhar-                    Kondraciuk, L., Kaiser, L., Metz, L., Boyd, M., Trebacz,
 wal, A., and Clark, P. DiscoveryBench: Towards                         M., Joglekar, M., Chen, M., Tintor, M., Meyer, M., Jones,
 Data-Driven Discovery with Large Language Models,                      M., Kaufer, M., Schwarzer, M., Shah, M., Yatbaz, M.,
 July 2024. URL http://arxiv.org/abs/2407.                              Guan, M. Y., Xu, M., Yan, M., Glaese, M., Chen, M.,
 01725. arXiv:2407.01725.                                               Lampe, M., Malek, M., Wang, M., Fradin, M., McClay,
                                                                        M., Pavlov, M., Wang, M., Wang, M., Murati, M., Bavar-
Mirza, A., Alampara, N., Kunchapu, S., Rı́os-Garcı́a,                   ian, M., Rohaninejad, M., McAleese, N., Chowdhury,
 M., Emoekabu, B., Krishnan, A., Gupta, T., Schilling-                  N., Chowdhury, N., Ryder, N., Tezak, N., Brown, N.,
 Wilhelmi, M., Okereke, M., Aneesh, A., Elahi, A. M.,                   Nachum, O., Boiko, O., Murk, O., Watkins, O., Chao, P.,
 Asgari, M., Eberhardt, J., Elbeheiry, H. M., Gil, M. V.,               Ashbourne, P., Izmailov, P., Zhokhov, P., Dias, R., Arora,
 Greiner, M., Holick, C. T., Glaubitz, C., Hoffmann, T.,                R., Lin, R., Lopes, R. G., Gaon, R., Miyara, R., Leike, R.,
 Ibrahim, A., Klepsch, L. C., Köster, Y., Kreth, F. A.,                Hwang, R., Garg, R., Brown, R., James, R., Shu, R., Cheu,
 Meyer, J., Miret, S., Peschel, J. M., Ringleb, M., Roesner,            R., Greene, R., Jain, S., Altman, S., Toizer, S., Toyer, S.,
 N., Schreiber, J., Schubert, U. S., Stafast, L. M., Wo-                Miserendino, S., Agarwal, S., Hernandez, S., Baker, S.,
 nanke, D., Pieler, M., Schwaller, P., and Jablonka, K. M.              McKinney, S., Yan, S., Zhao, S., Hu, S., Santurkar, S.,
 Are large language models superhuman chemists?, 2024.                  Chaudhuri, S. R., Zhang, S., Fu, S., Papay, S., Lin, S., Bal-
 URL https://arxiv.org/abs/2404.01475.                                  aji, S., Sanjeev, S., Sidor, S., Broda, T., Clark, A., Wang,
                                                                        T., Gordon, T., Sanders, T., Patwardhan, T., Sottiaux, T.,
Narayanan, S., Braza, J. D., Griffiths, R.-R., Ponnapati, M.,           Degry, T., Dimson, T., Zheng, T., Garipov, T., Stasi, T.,
  Bou, A., Laurent, J., Kabeli, O., Wellawatte, G., Cox,                Bansal, T., Creech, T., Peterson, T., Eloundou, T., Qi, V.,
  S., Rodriques, S. G., et al. Aviary: training language                Kosaraju, V., Monaco, V., Pong, V., Fomenko, V., Zheng,
  agents on challenging scientific tasks. arXiv preprint                W., Zhou, W., McCabe, W., Zaremba, W., Dubois, Y., Lu,
  arXiv:2412.21154, 2024.                                               Y., Chen, Y., Cha, Y., Bai, Y., He, Y., Zhang, Y., Wang, Y.,
OpenAI, :, Jaech, A., Kalai, A., Lerer, A., Richardson, A.,             Shao, Z., and Li, Z. Openai o1 system card, 2024. URL
  El-Kishky, A., Low, A., Helyar, A., Madry, A., Beu-                   https://arxiv.org/abs/2412.16720.
  tel, A., Carney, A., Iftimie, A., Karpenko, A., Passos,
 A. T., Neitz, A., Prokofiev, A., Wei, A., Tam, A., Bennett,          Quigley, I. K., Blevins, A., Halverson, B. J., and Wilkin-
 A., Kumar, A., Saraiva, A., Vallone, A., Duberstein, A.,               son, N. Belka: The big encoded library for chemical
  Kondrich, A., Mishchenko, A., Applebaum, A., Jiang, A.,               assessment. In NeurIPS 2024 Competition Track, 2024.
  Nair, A., Zoph, B., Ghorbani, B., Rossen, B., Sokolowsky,
  B., Barak, B., McGrew, B., Minaiev, B., Hao, B., Baker,             Sarwal, V., Munteanu, V., Suhodolschi, T., Ciorba,
  B., Houghton, B., McKinzie, B., Eastman, B., Lugaresi,                D., Eskin, E., Wang, W., and Mangul, S. BioLLM-
  C., Bassin, C., Hudson, C., Li, C. M., de Bourcy, C., Voss,           Bench: A Comprehensive Benchmarking of Large
  C., Shen, C., Zhang, C., Koch, C., Orsinger, C., Hesse,               Language Models in Bioinformatics, December 2023.
  C., Fischer, C., Chan, C., Roberts, D., Kappler, D., Levy,            URL https://www.biorxiv.org/content/
  D., Selsam, D., Dohan, D., Farhi, D., Mely, D., Robinson,             10.1101/2023.12.19.572483v1.               Pages:
  D., Tsipras, D., Li, D., Oprica, D., Freeman, E., Zhang,              2023.12.19.572483 Section: New Results.
  E., Wong, E., Proehl, E., Cheung, E., Mitchell, E., Wal-
  lace, E., Ritter, E., Mays, E., Wang, F., Such, F. P., Raso,        Schmidgall, S., Su, Y., Wang, Z., Sun, X., Wu, J., Yu,
  F., Leoni, F., Tsimpourlas, F., Song, F., von Lohmann,                X., Liu, J., Liu, Z., and Barsoum, E. Agent laboratory:

                                                                 10
                                                            BixBench

  Using llm agents as research assistants. arXiv preprint               Zhou, B., Zhao, H., Puig, X., Fidler, S., Barriuso, A., and
  arXiv:2501.04227, 2025.                                                 Torralba, A. Scene parsing through ade20k dataset. In
                                                                          Proceedings of the IEEE conference on computer vision
Siegel, Z. S., Kapoor, S., Nagdir, N., Stroebl, B.,                       and pattern recognition, pp. 633–641, 2017.
  and Narayanan, A. CORE-Bench: Fostering the
  Credibility of Published Research Through a Com-                      Zhuo, T. Y., Vu, M. C., Chim, J., Hu, H., Yu, W., Widyasari,
  putational Reproducibility Agent Benchmark, Septem-                     R., Yusuf, I. N. B., Zhan, H., He, J., Paul, I., Brunner,
  ber 2024. URL http://arxiv.org/abs/2409.                                S., Gong, C., Hoang, T., Zebaze, A. R., Hong, X., Li,
  11363. arXiv:2409.11363 [cs] version: 1.                                W.-D., Kaddour, J., Xu, M., Zhang, Z., Yadav, P., Jain,
                                                                          N., Gu, A., Cheng, Z., Liu, J., Liu, Q., Wang, Z., Lo, D.,
Skarlinski, M. D., Cox, S., Laurent, J. M., Braza, J. D.,                 Hui, B., Muennighoff, N., Fried, D., Du, X., Vries, H. d.,
  Hinks, M., Hammerling, M. J., Ponnapati, M., Rodriques,                 and Werra, L. V. BigCodeBench: Benchmarking Code
  S. G., and White, A. D. Language agents achieve super-                  Generation with Diverse Function Calls and Complex In-
  human synthesis of scientific knowledge. arXiv preprint                 structions, October 2024. URL http://arxiv.org/
  arXiv:2409.13740, 2024.                                                 abs/2406.15877. arXiv:2406.15877.
Swanson, K., Wu, W., Bulaong, N. L., Pak, J. E., and Zou, J.
  The virtual lab: Ai agents design new sars-cov-2 nanobod-
  ies with experimental validation. bioRxiv, pp. 2024–11,
  2024.

Tang, X., Liu, Y., Cai, Z., Shao, Y., Lu, J., Zhang, Y., Deng,
  Z., Hu, H., An, K., Huang, R., Si, S., Chen, S., Zhao, H.,
  Chen, L., Wang, Y., Liu, T., Jiang, Z., Chang, B., Fang,
  Y., Qin, Y., Zhou, W., Zhao, Y., Cohan, A., and Gerstein,
  M. ML-Bench: Evaluating Large Language Models and
  Agents for Machine Learning Tasks on Repository-Level
  Code, August 2024a. URL http://arxiv.org/
  abs/2311.09835. arXiv:2311.09835 [cs].

Tang, X., Qian, B., Gao, R., Chen, J., Chen, X., and Gerstein,
  M. Biocoder: A benchmark for bioinformatics code
  generation with large language models, 2024b. URL
  https://arxiv.org/abs/2308.16458.

Team, N. Sky-t1: Train your own o1 preview model within
  $450. https://novasky-ai.github.io/posts/sky-t1, 2025. Ac-
  cessed: 2025-01-09.

Wijk, H., Lin, T., Becker, J., Jawhar, S., Parikh, N., Broadley,
 T., Chan, L., Chen, M., Clymer, J., Dhyani, J., et al. Re-
 bench: Evaluating frontier ai r&d capabilities of language
 model agents against human experts. arXiv preprint
 arXiv:2411.15114, 2024.

Wognum, C., Ash, J. R., Aldeghi, M., Rodrı́guez-Pérez,
 R., Fang, C., Cheng, A. C., Price, D. J., Clevert, D.-A.,
 Engkvist, O., and Walters, W. P. A call for an industry-
 led initiative to critically assess machine learning for
 real-world drug discovery. Nature Machine Intelligence,
 pp. 1–2, 2024.

Yin, H., Gu, Z., Wang, F., Abuduhaibaier, Y., Zhu, Y., Tu, X.,
  Hua, X.-S., Luo, X., and Sun, Y. An Evaluation of Large
  Language Models in Bioinformatics Research, Febru-
  ary 2024. URL http://arxiv.org/abs/2402.
  13714. arXiv:2402.13714 [q-bio] version: 1.

                                                                   11
                                                      BixBench

A    Appendix
In the appendix we include a number of additional figures and plots displaying other metrics for performance on the
benchmark and evaluation results.




Figure 6: An example of an actual analysis capsule within BixBench and associated question tasks. The primary capsule
consists of a notebook of analysis code generated by an expert analyst, any input data files for the analysis, and some
metadata including a hypothesis, result, and answer. The Questions are initially generated by an LLM, and reviewed and
edited by expert humans. See Methods for a complete description.




                                                          12
                                          BixBench




     Figure 7: Average rate of correct answer (accuracy) per capsule across replicates.




Figure 8: Average rate of correct answer (accuracy) per individual question across replicates.




                                             13
                                                    BixBench

Example prompt used to initialise an agent trajectory

You are an expert bioinformatician and seasoned biological data scientist. Your task
     is to create a comprehensive Jupyter notebook named ’notebook.ipynb’ that
    analyzes data to answer a series of questions.
The notebook should contain all necessary artifacts (plots, tables, print outputs)
    to fully answer these questions, structured in a way that another person could
    use to derive the answers.

Here are the questions you need to address:

<questions>
q1: What percentage of genes differentially expressed in strain 97 are also
    differentially expressed in strain 99?
q2: How many genes are uniquely differentially expressed in strain 98 but not in
    either of strains 97 or 99?
q3: How many genes have a dispersion value below 1e-05 after DEseq analysis?
q4: Which strain and media condition do not cluster together based on pairwise
    correlation after regularized log transformation of the differential expression
    analysis results?
</questions>




                                                        14
                                                    BixBench

Example prompt used to initialise an agent trajectory continued 1

Follow these steps to create your notebook, using chain-of-thought reasoning at each
     stage:
1. List Directory Contents:
<analysis_planning>
- Consider how to use the list_workdir tool to recursively list the directory
    contents.
- Think about how to organize and present this information clearly in the notebook.
- List potential challenges in interpreting the directory structure.
- Consider how the directory structure might inform your approach to the analysis.
</analysis_planning>
Place the output of the list_workdir tool inside <directory_contents> tags.
2. Load Data and Perform Descriptive Statistics:
<analysis_planning>
- Identify which data files are most relevant to answering the questions. List these
     files.
- Plan how to load these files efficiently in R or Python.
- List the specific descriptive statistics you plan to use (e.g., summary(), str(),
    head()).
- Consider potential issues like missing data or unexpected formats. How will you
    handle each?
- Plan how to present this information clearly in the notebook.
- Write down key statistics you expect to see and how you’ll interpret them.
- Consider potential data quality issues and how you’ll address them.
</analysis_planning>
Execute your plan to load data and perform descriptive statistics.
3. Develop Analysis Plan:
<analysis_planning>
- Break down each question into testable components. List these components.
- For each component, list appropriate statistical tests or visualizations.
- Consider alternative approaches for each component and justify your choices.
- Identify potential confounding factors and how to address them.
- Plan the sequence of your analysis steps, explaining the rationale for each.
- Consider how this analysis plan will be documented in the notebook.
- List potential statistical assumptions for your chosen methods and how you’ll test
     them.
- Think about how your analysis plan addresses each of the original questions.
</analysis_planning>
Write out your analysis plan as comments in the notebook.
4. Execute Analysis Plan:
<analysis_planning>
- For each step in your analysis plan, list the R, Python or bash functions and
    libraries you’ll use.
- Think about how to structure your code for readability and efficiency.
- Plan how to document your code with clear comments.
- Consider how to present results clearly, using tables or visualizations where
    appropriate.
- Ensure that all outputs are clearly labeled and explained in the context of the
    questions.
- Plan how you’ll interpret each result in relation to the original questions.
- Consider potential unexpected results and how you’ll handle them.
</analysis_planning>
Execute your analysis plan, creating new cells as needed.
5. Conclude and Submit Answer:
<thought_process>
- Reflect on how your results relate to each question.
- List any limitations or uncertainties in your analysis.
- Plan a concise summary of your findings for each question.
- Think about how to phrase your conclusions as clear statements.
- Ensure that the notebook contains all necessary information for another model to
    derive these answers.
- Consider any additional insights or patterns you’ve noticed during the analysis.
- Think about potential follow-up questions or areas for further investigation.
</thought_process>
Use the submit_answer tool to submit your final answer as a dictionary with keys as
    the question number and a short answer15to the question.
If the question asks for a number, be precise to 2 decimal places.
                                                    BixBench

Example prompt used to initialise an agent trajectory continued 2

General Guidelines:
- Write small to medium-sized cells for easier debugging.
- Edit existing cells by their index number when fixing bugs, rather than creating
    new ones.
- Check dataframe shapes before printing. Use head() for large dataframes.
- Ensure each cell executes successfully before moving to the next.
- Assume you already have the packages you need installed and only install new ones
    if you receive errors.
- If you need to install packages, use mamba or conda.
IMPORTANT: R vs Python vs bash
- You can use either Python, R or bash cells to complete the analysis.
- All cells are by default Python cells. However, you can use both bash and R cells
    by adding %%bash or %%R to the first line of the cell.
- The first cell has already been loaded with %load_ext rpy2.ipython so you can use
    %%R cells from the second cell onwards
- AVOID USING PLOTS. USE TABLES AND PRINT OUTPUTS INSTEAD AS MUCH AS POSSIBLE.


R-Specific Guidelines:
1. Load packages using this format to minimize verbose output:
   ‘‘‘r
   if (!requireNamespace("package_name", quietly = TRUE)) {
     install.packages("package_name")
   }
   suppressPackageStartupMessages(library(package_name))
   ‘‘‘

2. For data operations, suppress messages about column name repairs:
   ‘‘‘r
   variable_name <- read_excel("<fpath>.csv", col_names = FALSE, .name_repair = "
    minimal")
   ‘‘‘

3. When printing dataframes, always wrap them in print() statements:
   ‘‘‘r
   print(head(dataframe))
   ‘‘‘

The final answers to the questions must be submitted using the submit_answer tool.
    You must use the submit_answer tool to end the episode. You must use JSON format
     as follows:

Example output:
‘‘‘
submit_answer({
    "q1": "Short answer to question 1",
    "q2": "Short answer to question 2",
    "q3": "Short answer to question 3",
    "q4": "Short answer to question 4"
})
‘‘‘

YOU MUST ANSWER ALL FOUR QUESTIONS in the json format above.Remember to provide
    clear, concise answers that directly address each question based on your
    analysis.




                                                       16
