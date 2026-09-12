# The limits of bio-molecular modeling with large language models: a cross-scale evaluation

**Authors:** Xu, Yaxin; Zhou, Yue; Zhao, Tianyu; An, Fengwei; Ren, Zhixiang
**Year:** 2026
**Venue:** arXiv preprint
**arXiv:** 2604.03361
**Source PDF URL:** https://arxiv.org/pdf/2604.03361
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---
The limits of bio-molecular modeling with large
language models : a cross-scale evaluation
Yaxin Xu1,2† , Yue Zhou2† , Tianyu Zhao

, Fengwei An1 , Zhixiang Ren

Southern University of Science and Technology, Shenzhen, 518055, China.
2*
Pengcheng Laboratory, Shenzhen, 518055, China.
Institute of Mechanics, Chinese Academy of Sciences, Beijing, 100190, China.
*Corresponding author(s). E-mail(s): jason.zhixiang.ren@outlook.com;
Contributing authors: xuyx2024@mail.sustech.edu.cn; zhouy@pcl.ac.cn;
tyzhao@mail.bnu.edu.cn; anfw@sustech.edu.cn;
†
These authors contributed equally to this work.
Abstract
The modeling of bio-molecular system across molecular scales remains a
central challenge in scientific research. Large language models (LLMs) are
increasingly applied to bio-molecular discovery, yet systematic evaluation
across multi-scale biological problems and rigorous assessment of their toolaugmented capabilities remain limited. We reveal a systematic gap between
LLM performance and mechanistic understanding through the proposed crossscale bio-molecular benchmark: BioMol-LLM-Bench, a unified framework
comprising 26 downstream tasks that covers 4 distinct difficulty levels, and
computational tools are integrated for a more comprehensive evaluation. Evaluation on 13 representative models reveals 4 main findings: chain-of-thought data
provides limited benefit and may even reduce performance on biological tasks;
hybrid mamba–attention architectures are more effective for long bio-molecular
sequences; supervised fine-tuning improves specialization at the cost of generalization; and current LLMs perform well on classification tasks but remain
weak on challenging regression tasks. Together, these findings provide practical
guidance for future LLM-based modeling of molecular systems.
Keywords: Bio-molecular Benchmark, Cross-Scale, Large Language Model, Hybrid
Architecture, Tool Integration

2*

1 Introduction
Bio-molecule plays a foundational role across a wide range of biological and chemical
domains[1–3]. Multi-scale bio-molecular modeling has emerged as a critical paradigm, aiming
to bridge different levels of representation from monomer-level molecule to polymer complex.
They underpin applications from bio-materials design to drug delivery systems[4, 5]. However,
effectively integrating and modeling information across these scales remains a significant challenge. With the rapid growth of data availability and computational power, there is an increasing
reliance on large language models (LLMs)[6–13] to accelerate property prediction and model
complex interactions simultaneously. In bio-molecular sciences, these models[14, 15] hold particular promise: the ability to reason about molecules, proteins, and their interactions in natural
language, enable more intuitive exploration of chemical space. Recent years have witnessed
a proliferation of domain-adapted models[16–19], ranging from general-purpose foundation
models fine-tuned on scientific corpora to architectures specifically designed for bio-molecular
understanding, each claiming varying degrees of proficiency on bio-molecular tasks. Notable
examples include TxGemma[16], which specializes in therapeutic tasks by processing diverse
modalities such as small molecules and natural text to predict therapeutic properties.
Yet the rapid development of these models has outpaced our ability to systematically
evaluate their capabilities. General-domain benchmarks[20–27] such as MMLU-Pro[21] and
AI2ARC[24], while useful for assessing broad reasoning capabilities, lack the specialized
knowledge required for meaningful evaluation on bio-molecular tasks. Conversely, domainspecific benchmarks[28–34] often focus on single task types such as molecular reaction outcome
prediction, or protein function annotation, without considering how models perform across the
interconnected scales of bio-molecular problems. These limitations obscure important patterns
in model behavior: a model that excels at predicting small molecule solubility may fail catastrophically on protein-protein interaction tasks, such trade-offs remain poorly characterized.
More significantly, current evaluation frameworks[35, 36] provide limited insight into how different model architectures and training approaches affect model behavior across cross-scale
bio-molecular tasks.
Furthermore, LLM is evolving towards agents and absorbing tool retrieval capabilities.
Existing benchmarks[37–42] lack integration with computational tools and are limited to
task-oriented question answering. But in real-world scientific practice, researchers combine conceptual understanding with specialized software[14, 36, 43–46] for bio-molecular modeling.
Benchmarks that mentioned above typically evaluate models under artificial constraints, requiring direct question answering or chain-of-thought (CoT) thinking, thereby failing to provide a
comprehensive assessment of model capabilities.
To address these gaps, we introduce the cross-scale bio-molecular benchmark (BioMolLLM-Bench), a comprehensive evaluation framework (Figure 1) that aims to help us evaluate
the capabilities of LLMs from the perspective of practical scientific applications. Our benchmark
encompasses 4 hierarchical levels (L0 to L3 ) corresponding to increasing structural and functional complexity. This hierarchical organization enables fine-grained analysis of how model
capabilities scale with problem complexity. We provide an automated evaluation pipeline that
parses model outputs into required formats. Beyond traditional accuracy measures, the pipeline
evaluates output validity, which determines whether model responses conform to required formats. Specialized computational tools are integrated into the evaluation framework. This allows
evaluation of model ability in computational tool orchestrating and argument parsing.
Furthermore, we conducted experiments on 13 general-purpose and domain-specific models,
revealing the benchmark’s discriminative power and utility in guiding future LLM design.

• Training data: On biological tasks, we found that CoT provides a slight improvement and
may even weaken performance. The reasoning process appears sound in linguistics, but
contains self-contradictory description and chemical inconsistency.
• Model Architecture : We identify that hybrid mamba-attention architectures may offer
advantages over pure transformer in bio-molecular sequences processing with long-range
dependencies, which even outperforms models with 10 times more parameters.
• Training strategy: Supervised fine-tuned (SFT) models tend to become narrow specialists
and lack generalization ability, which perform poorly on out-of-distribution tasks.
• Task performance: Although LLMs perform well on several classification tasks, none of the
evaluated models achieves meaningful performance on challenging regression tasks such as
amino acid-level property prediction.
Cross-scale bio-molecular
benchmark

Scientific background
Scientific challenge: Multi-scale biomolecular modeling

L3:
Multiple
molecules

Formatted
questions

chemistry

biology

medicine

physics

Different models:

L1:
Small
molecule
L0:
General
knowledge

Lack of physicochemical reasoning

Metrics

External
tools

LLMs: advantages and limits
Multi-domain knowledge integration

Answer
parsing

LLMs

e.g., “predict solubility”

L2:
Large
molecule

joint modeling

LLM evaluation & Tool integration

e.g., what
happens to the
molecules of a
liquid when the
liquid cools?

Evaluation metrics:

Parameter
scale

Architecture

Classification:
Accuracy,
Validity

Regression:
RMSE, STD,
MEAN

Think mode

Prompt
complexity

Similarity:
Meteor, Lev

Fingerprint:
MACCS, RDK,
MORGAN

Benchmark Construction
Construction Steps:

Collection

Task
Definition

Process

Sampling
Strategy

Verify

Task Distribution

Stratified sampling example

Fig. 1: Overview of BioMol-LLM-Bench. The framework addresses limitations in existing
benchmarks by incorporating specialized bio-chemistry tools and enabling cross-scale evaluation
with 26 tasks across 4 levels. The evaluation pipeline integrates automatic answer extraction and
metrics computation. 13 models are compared under different experiment settings.

2 Results
2.1 Cross-Scale Bio-molecular Benchmark
2.1.1 Benchmark Construction and Data Curation

The construction of BioMol-LLM-Bench followed a multi-stage pipeline designed to aggregate
and refine high-quality bio-molecular data from heterogeneous sources including MMLUPro[21], USPTO-50K[47], DrugBank[48], PDB[49], et. al. During the initial data processing
phase, raw data were subjected to rigorous deduplication and structural validation to ensure the
integrity of SMILES strings and FASTA sequences. This was further refined through a LLM verification process using a specialized prompt to assign confidence scores (0 ≤ c ≤ 1) to eliminate

entries that unrelated to the bio-molecular field. Then, a hierarchical downstream task stratification was implemented, categorizing tasks into 4 levels (L0 to L3 ) according to input data type,
ranging from general molecular text to specialized large-molecule complexes (Table 1). Finally,
a stratified sampling strategy was applied to the curated dataset of each task to mitigate class
imbalance and ensure a representative distribution across the bio-chemical space.
2.1.2 Integration of Computational Tools

Current artificial intelligence models, particularly LLMs, possess varying degrees of capability
in automatically invoking tools and parsing function parameters. To further enhance the evaluation capability of the benchmark for models, we integrated a suite of domain-specific tool
interfaces[43]. This integration allows for an agentic workflow where models can invoke specific
predictive functions, such as solubility lipophilicity hydration() and BBB penetrance(), to
derive ADMETAI (Absorption, Distribution, Metabolism, Excretion, Toxicity, and AI-predicted)
properties.
2.1.3 Evaluation Framework and Metrics

The final stage of the benchmark involves a standardized evaluation pipeline where formatted
questions are processed by models under various experimental configurations. An automatic
answer extraction method was proposed to parse model output, so that the extracted content
could be used to compare with corresponding labels. For different downstream tasks, model
performance is quantified using distinct metric clusters.
2.2 Comparative Performance of LLMs
To demonstrate the utility and discriminability of our benchmark, 13 LLMs (Table 2) are
evaluated with detail prompt instruction (illustrated in Section 4), encompassing a range of architectural designs (dense and sparse, Transformer and Mamba), as well as both domain-specific
and general-purpose models. Table 3 presents a comprehensive ranking of the models. The models are ranked from 1 (best) to 13 (worst) on each individual task, with the overall rank across
all tasks summarized in the bottom row.
NVIDIA-Nemotron-Nano-9B-v2 emerges as the overall top performer with a composite rank
of 1, demonstrating exceptional versatility across task categories. It achieves 4 first-place rankings among others. DeepSeek-V3.1 secures the second overall position, showing particularly
strong performance on General Text task. Moreover, several models exhibit domain-specific
expertise. Phi-4-14B achieves first-place rankings on two L3-level tasks, suggesting particular
strength in interaction prediction tasks. However, NatureLM-8x7B generally falls below average
across tasks, contributing to its overall lower standing.
The ranking demonstrates that no single model dominates across all tasks. The strong performance of NVIDIA-Nemotron-Nano-9B-v2 suggests that the combination of mamba and
attention architecture is more effective at capturing both global and local information simultaneously, offering inherent advantages for bio-molecular tasks, which typically involve long
molecular SMILES strings and protein sequences as inputs. The results of DeepSeek-V3.1 indicate that large-scale models with massive parameters, extensive data, advanced training strategies
possess stronger knowledge retention capabilities compared to smaller models, thereby yielding
broadly applicable representations. The consistent under-performance of Llama-3.1-8B-Instruct
and NatureLM-8x7B indicates their potential limitations for bio-molecular tasks.

Table 1: Summary of benchmark tasks. The table presents 26 tasks categorized into 4 hierarchical levels (L0-L3) based on input complexity. For each task, the table specifies the task
abbreviation, input modalities, number of test samples (#Num), and the original data sources.
SMILES and AA-Seq. represent sequence strings of molecule and protein, respectively.

Inputs

#Num

Source

L0

Text

GPQA Diamond[20],
MMLU Pro[21],
AI2ARC[24]

L1

AqSolDB[41], esol[50]
freesolv[51]
USPTO-50K[47]
USPTO-50K[47]
QM8[52]
QM9[53]
BBBP[54]
MoleculeNet[31]
PCQM4Mv2[55],
QM9[53]
tox21[31]

L2

PROT Conserve
PROT SSC
PROT Fold

Meltome atlas[56]
Tm262[42], S669[57]
GB1[58], avGFP[59]
ProteinGym[37]
VESPA[34]
DeepLoc[38]
DeepFRI[60]
DeepFRI[60]
CB513[61], CASP12[62]
PDB[49]

L3

Text, Two AA-Seqs.
Text, Two AA-Seqs.
Text, Two SMILES
Text, AA-Seq., SMILES

Text, Three AA-Seqs.

SHS27k[63]
TAGPPI[64]
Drugbank[48]
SKEMPI[65],
bindingdb[66], davis[67]
AbBiBench[40]

2.2.1 Classification tasks

Firstly, we analyze model performance across 8 classification tasks, evaluated in terms of prediction accuracy and output validity. As Figure 2 shows, models achieve higher performance
on text-only (General Text) or easy classification tasks(MOL BBBP and MOL Tox), whereas
performance declines for structurally complexes or biologically nuanced tasks such as protein–protein interaction type prediction. Specifically, due to the deep fine-tuning process of
NatureLM-8x7B, its accuracy on some tasks is zero as the fine-tuning process did not learn it.
Large-parameter models, including Qwen3-235b-a22b-2507 and DeepSeek-v3.1, consistently
rank among the top performers in overall accuracy. Medium-scale models such as Qwen-3-14B
and Gemma-3-12B exhibit greater fluctuations and reduced robustness.

Table 2: Overview of evaluated models. The table lists 13 language models evaluated, models
vary in the number of parameters (#Params), open-source availability (Open), whether the model
has undergone domain-specific fine-tuning (Domain-FT), and the underlying architectural type
(Architecture). MoE denotes Mixture-of-Experts architecture, while D.T. refers to Dense Transformer. Parameter counts marked with ”/” indicate undisclosed model sizes.
Model

#Params

Open

Domain-FT

Architecture

DeepSeek-v3.1[68]
Qwen3-235b-a22b-2507[10]
GPT-5-mini[69]

685B
235B
/

NatureLM-8x7B[18]
TxGemma-Chat-9B[16]

56B
9B

Phi-4-14B[13]
GPT-oss-20B[70]
Gemma-3-12B[8]
Qwen-3-14B[10]
NVIDIA-Nemotron-Nano-9B-v2[12]
Mistral-Nemo-Instruct-2407[71]
Llama-3.1-8B-Instruct[11]
DeepSeek-R1-Distill-Qwen-14B[9]

20B
12B
9B
12B
8B

Mamba

As for output validity (indicated with markers on Figure 2), we measure whether model outputs conform to the required answer format and produce parsable predictions. Validity generally
remains high for the majority of models, while certain models such as GPT-oss-20B demonstrate
reduced validity in complicated tasks. Notably, some high-accuracy models such as Phi-4-14B
occasionally show reduced validity in specific categories, suggesting that raw predictive capability does not necessarily guarantee strict adherence to output constraints. This distinction
underscores the importance of jointly evaluating semantic correctness and formatting reliability
in LLM benchmarking.

Accuracy(%)

46 46

48475050 48 504950
45 45

353334

72 74

General_Text
phi-4-14B
gpt-oss-20B

PROT_EC
gemma-3-12B
qwen-3-14B

12 1212 12
9 11 11 108

52 52 51 53
50 48 5050

50 5150 4951 49

1414 13131315 13 131413

PROT_Location

NVIDIA-Nemotron-Nano-9B-v2
Mistral-Nemo-Instruct-2407

Validity(%)

PPI_Type

PPI_Binary

Llama-3.1-8B-Instruct
DeepSeek-R1-Distill-Qwen-14B

MOL_TOX
TxGemma-Chat-9B
NatureLM-8x7B

MOL_HIV

MOL_BBBP

qwen3-235b-a22b-2507
gpt-5-mini

deepseek-v3.1

Fig. 2: Performance of 13 LLMs among 8 classification tasks. The prediction accuracy are
displayed with bars based on the left axis. The markers represent model output validity based on
the right axis. Larger-parameter models rank among the top performers in overall accuracy.

Table 3: Model rankings on each benchmark tasks. The overall rank is obtained by calculating
the ranking of all models based on the average of each model’s rankings across all tasks. A: Phi4-14B, B: GPT-oss-20B, C: Gemma-3-12B, D: Qwen-3-14B, E: NVIDIA-Nemotron-Nano-9Bv2, F: Mistral-Nemo-Instruct-2407, G: Llama-3.1-8B-Instruct, H: DeepSeek-R1-Distill-Qwen14B, I: TxGemma-Chat-9B, J: NatureLM-8x7B, K: Qwen3-235b-a22b-2507, L: GPT-5-mini,
M: DeepSeek-v3.1.
Tasks

A

B

C

D

E

F

G

H

I

J

K

L

M

Overall Rank

2.2.2 Regression tasks

Figure 3 presents model performance across eleven bio-molecular regression tasks spanning
molecular thermodynamics, quantum properties and protein mutational effects. Overall performance distribution across all tasks exhibits substantial variability. Tasks involving protein-level
stability (PROT Mutation) and thermodynamics (MOL Thermo) exhibit wider numerical ranges
compared to quantum chemical tasks (MOL Excited and MOL HLGap). NVIDIA-NemotronNano-9B-v2 and larger-scale models including DeepSeek-v3.1 generally demonstrate lower
absolute error magnitudes and tighter dispersion across most tasks. Notably, performance
improvements with scale are not uniform across all tasks. While L2-level tasks generally benefits from increased parameter count, L1-level tasks show diminishing returns, indicating that
scaling alone may not resolve biologically complexes inference challenges.
After parsing, Llama-3.1-8B-Instruct and TxGemma-Chat-9B models are unable to produce
prediction results on any tasks, and are therefore not shown in Figure 3. All models perform
poorly on two extremely difficult tasks (MOL Thermo and PROT Mutation), indicating that

future work should investigate ensemble methods to better handle the challenging long-sequence
regression tasks prevalent in bio-molecular domains.
PLI_BA

MOL_Thermo

PROT_Mutation

MOL_Solubility

MOL_Freesolv

PROT_Fitness

PROT_Melt

A: phi-4-14B
B: gpt-oss-20B
C: gemma-3-12B
D: qwen-3-14B
E: NatureLM-8x7B
F: NVIDIA-Nemotron-Nano-9B-v2
G: Mistral-Nemo-Instruct-2407
H: DeepSeek-R1-Distill-Qwen-14B
I: qwen3-235b-a22b-2507
J: gpt-5-mini
K: deepseek-v3.1

CI_AbAg

MOL_HLGap

PROT_Energy

10000

MOL_Excited

5.0
5.0
7.5
10.0
12.5
15.0

Fig. 3: The distributions of prediction results on eleven regression tasks. By calculating the
difference between each model’s predictions and the ground-truth labels across different samples
for each task, the mean and variance are computed, from which the boxplot in each subplot is
generated.

2.2.3 Generation tasks

There are 7 generation tasks in our benchmark, Figure 4 presents a comparative analysis of model
behavior on 4 tasks. As for other 3 extremely hard tasks (PROT Conserve, PROT Location and
PROT Fold), all models are unable to complete, so the results are not shown. As for MOL Syn
task, TxGemma-Chat-9B demonstrates significant advantage over other models, based on the
fingerprint similarity results using MACCS, MORGAN and RDKIT calculation methods. The
results of other models show relatively minor differences. Furthermore, the fingerprint result
distributions obtained from 3 calculation methods are consistent. Similarly, on PROT GO and
DDI Interact tasks (panel b), TxGemma-Chat-9B demonstrates leading performance, highlighting the advantage of this model’s exceptional capabilities on generative tasks after fine-tuning
with domain knowledge.
On the MOL Resyn task, the overall performance of all models is mediocre. Among them,
the Qwen3-series models achieves the best results. Five models including NatureLM-8x7B
and DeepSeek-R1-Distill-Qwen-14B, are completely unable to generate valid molecules for
the task. Notably, DeepSeek-R1-Distill-Qwen-14B, which was fine-tuned with chain-of-thought
(CoT) based on Qwen-3-14B, exhibits weakened generative capabilities compared to its baseline
model. It indicates that the CoT fine-tuning approach does not have a significant improvement
effect on specific tasks in the bio-molecular domain.
2.3 Tool Capability Comparison
We compare benchmark performance between single LLMs using direct prompt and agentic
workflows with tool integration. Figure 5 exhibits the performance of two different backbone
models (DeepSeek-v3.1 and Llama-3.1-8B) on two regression and two classification tasks.
Firstly, across all tasks and regardless of which model, tool-enabled configurations exhibit
greater numerical stability and improved overall performance. The most striking effect is

a)

b)

Fig. 4: Model performance on generation tasks. Higher values indicate better model performance. a). For MOL Syn and MOL Resyn tasks, fingerprint similarities of the prediction results
were calculated using three methods: MACCS, MORGAN, and RDKIT. These values are displayed as bars corresponding to the left y-axis. The markers that represent the validity of the
output results correspond to right y-axis. b). The results for PROT GO and DDI Interact were
evaluated with Levenshtein similarity and Meteor similarity metric, respectively.
observed in regression tasks, where disabling tools leads to extreme error values, suggesting that
unconstrained language generation is insufficient for precise quantitative estimation. Classification tasks show smaller but consistent performance drops without tools, implying that symbolic
reasoning alone partially supports binary decision-making but lacks reliability.
Secondly, we compare the effect of continual pretraining (CPT). Llama-3.1-8B-Instruct-CPT
is trained with sufficient bio-molecular knowledge. CPT introduces slight improvement in both
regression and classification tasks. This indicates that domain-specific CPT enhances the model’s
ability to interact effectively with structured chemical inputs and tool outputs. Finally, comparing
the results of models of different parameter scales, it is counter-intuitive that although DeepSeekV3.1 has over 50 times more parameters than LLama-3.1-8B, their overall performance is
similar, outperforming each other in two tasks respectively.
2.4 Ablation study of experiment settings
We also examine model sensitivity to different prompts and think mode as minor variations in
phrasing, formatting, or instruction style may lead to performance fluctuations. Qwen3-14B,
NVIDIA-Nemotron-Nano-9B-v2 and DeepSeek-R1-Distill-Qwen-14B are selected because
they support think mode. Simple and detailed prompt template are described in Section 4.
Overall, NVIDIA-Nemotron-Nano-9B-v2 (Figure 6) shows stronger sensitivity and variability
to different think mode and input prompt than Qwen3-14B. And model performance on hard

MOL_Solubility

0.6

Classification Accuracy

0.947

0.8

0.742

0.934

0.868

0.4
0.2

0.209

MOL_BBBP

MOL_Freesolv

Llama-3.1-8B-Instruct w/o tools
Deepseek-V3.1 w/ tools

0.934

0.756

0.460
0.897

0.156

0.916

1.069

0.5

1.046

0.971

0.442

1.5

1.0 1.0 1.0

0.528

2.0

0.947

0.700

0.731

0.840

0.790

0.814

1.0 1.0 1.0

0.781

0.771

0.930

358.19

890.82

3.170

3.0

0.908 0.927

1.004

Regression RMSE

3.5

8.321

4.0

Llama-3.1-8B-Instruct w/ tools
Deepseek-V3.1 w/o tools

MOL_TOX

Llama-3.1-8B-Instruct-CPT w/ tools

Fig. 5: LLM performance with and without tool integration across 4 representative tasks.
(left) For regression-based tasks (MOL Solubility and MOL Freesolv), performance is evaluated using RMSE, where lower value bars indicate better performance. The dashed bars indicate
values exceeding the coordinate range, and the actual value is displayed with white numerical
text. (right) For classification tasks, performance is measured using accuracy. The markers represent model output validity.
tasks such as PPI Binary can be improved by think process On most tasks, DeepSeek-R1Distill-Qwen-14B’s sensitivity to prompt is low, with only significant differences observed on
MOL TOX task. These results indicate that when using LLM to complete domain-specific tasks,
more domain knowledge guidance should be given, and whether to use think mode needs to be
flexibly adjusted according to the difficulty of tasks.
a)

b)

c)

Fig. 6: Model behavior under different input prompt complexity and think mode. Performance is evaluated with accuracy. Detailed prompt with more domain knowledge guidance
generally exhibits better performance, and model performance under think mode varies depending on the task. NVIDIA-Nemotron-Nano-9B-v2 shows higher accuracy and sensitivity to
different experiment settings.

2.5 LLM reasoning ability in scientific problem
To investigate how LLMs solve scientific problem, we analyze their CoT reasoning processes.
Beyond final-answer accuracy, this analysis focuses on whether intermediate reasoning reflects

a principled understanding of biomolecular mechanisms. A representative example arises from
molecular solvation free energy prediction task as follows. At first glance, this reasoning appears
chemically sound. However, the reasoning processing contains some contradictions and chemical inconsistencies: If the molecule is fused and contains two ketones, it is more likely a
naphthoquinone derivative or a dione, but not similar to acetanilide. Similar behavior is observed
across task types and models. In generative tasks such as forward synthesis, models produce
fluent and domain-relevant rationales, but lack a verifiable linkage to the governing chemical
processes. These observations indicate that LLMs solve scientific problems primarily through
a combination of pattern recognition, abstraction, and heuristic reasoning, rather than through
explicit modeling of underlying mechanisms.
Output example of DeepSeek-R1-Distill-Qwen-14B under think mode:
Okay, so I need to predict the free energy of a molecule given its SMILES notation. The
SMILES provided is c1ccc2c(c1)C(=O)c3cccc(c3C2=O)N. Hmm, let me try to figure this
out step by step.
First, [... Omitted for brevity ...]
Putting this together, the molecule might have two benzene rings connected in a
fused manner, with two ketone groups and an amine substituent. This structure could
be similar to acetanilide or something more complex, perhaps a beta-lactam or another
bicyclic compound.

3 Discussion
The cross-scale bio-molecular benchmark introduced in this work provides a comprehensive evaluation framework for assessing large language models on biologically-relevant tasks
spanning multiple scales of molecular complexity. Through systematic evaluation of 13 stateof-the-art models, we have elucidated several important insights regarding model capabilities,
architectural influence, and the value of tool integration in the bio-molecular domain.
Our ranking analysis reveals that NVIDIA-Nemotron-Nano-9B-v2, which employs a hybrid
mamba-attention architecture, achieves the best overall performance across BioMol-LLMBench. This suggests that hybrid architecture appears particularly well-suited for processing
the long-range dependencies inherent in bio-molecular sequences. Poor performance across all
models on 2 challenging tasks (MOL Thermo and PROT Mutation) highlights the difficulty
of long-sequence regression in bio-molecular applications and motivates exploration of model
optimization. Models that underwent extensive domain-specific fine-tuning, such as TxGemmaChat-9B, demonstrate remarkable proficiency on a small portion of tasks yet exhibit significant
degradation on general text understanding. This mechanism reflects a degradation in generalization capability resulting from SFT. Through the analysis of reasoning process, we found that
LLMs may arrive at the correct answer but with wrong mechanistic reasons.
Overall, the consistently high performance on lower-level tasks (L0-L1 levels) suggests
that current LLMs have developed robust representations for small molecular language when
expressed in natural language format. However, the marked performance degradation on L3-level
tasks involving protein-protein interactions indicates a fundamental limitation in current models’
ability to reason about relationships between molecules. The observation that tool-enabled configurations consistently outperform direct prompting, supports a hybrid intelligence paradigm
where LLMs serve as reasoning orchestrators while specialized tools handle quantitative computations. In conclusion, the cross-scale bio-molecular benchmark provides both a standardized

evaluation methodology and empirical insights that are promosing to guide future development
of language model design for bio-molecular discovery.

4 Methods
4.1 Benchmark Construction
We proposes a comprehensive benchmark dataset specifically tailored for evaluating the capabilities of LLMs in molecular sciences. The source dataset is carefully derived from multiple
high-quality sources to ensure diversity and reliability. Moreover, tool calling API and unified
evaluation pipeline are integrated to facilitate efficient model comparison.
1. Diverse Raw Open-Source Data Sources. The foundation of the benchmark draws
from a variety of raw open-source data, combining domain-specific benchmarks (e.g.,
MoleculeNet[31] suites including QM9 for quantum properties and Tox21 for toxicity) with general semantic understanding benchmarks (e.g., biomolecule-related questions in MMLU-Pro and
AI2ARC). Detailed descriptions of tasks are given in Table 1 and Supplementary Table A. This
integration ensures the dataset to capture both specialized molecular tasks and broader chemical
knowledge.
2. Standardized Data Processing Workflow. To maintain consistency and quality, a
rigorous standardized workflow is applied.
• Filtering. Removes invalid, incomplete, or noisy entries (e.g., invalid SMILES strings or
duplicate molecules) with RDKIT software and DeepSeek-v3.1 model.
Prompt for sample filtering:
You are an expert in life science.
Please carefully analyze the following question and judge that whether (Yes or No) the
question related to small molecule and protein science, and give the confidence score
(between 0 and 1) about your answer.
Question: {input text}
Please answer in exactly the following format:
Answer:
Confidence:
• Cleaning. Normalizes representation of molecules to canonical SMILES format and resolves
inconsistencies in labels.
• Merging. Integrates data from multiple sources while avoiding overlaps through similarity
checks.
• Length casting. Natural language text with excessive byte counts (more than 1000) or protein
sequence longer than 500 characters were filtered out to reduce computational complexity.
• Sampling. Employs stratified sampling to balance molecular complexity and property distributions.
• Metadata supplement. For complicated tasks such as protein ligand interaction prediction,
additional protein and molecule structure information are provided.
3. Coverage of Diverse Tasks Across Molecular Scales. The benchmark encompasses 4
levels of tasks according to input complexity.
• L0: General bio-molecular knowledge understanding. Input data type of questions in this
level only contains natural language.

• L1: Small-molecule level tasks. Focusing on small molecule property prediction including
chemical and physiological property. Both natural language and SMILES representation of
molecules are provided.
• L2: Large-molecule level task. Focusing on tasks related to protein function and structure.
Input data modalities include natural language and protein sequence.
• L3: Multiple-molecules level task. Incorporating challenging real-world tasks, such as
antibody-antigen binding prediction, with more input data types including molecule SMILES,
protein sequence, and natural language.
Processed datasets for each task were stored in standard JSON format, with columns
including canonical SMILES, protein sequence, task-specific labels, and metadata.
4. Automated Result Parsing and Evaluation Pipeline. To enable fair and reproducible
comparison of LLMs, we proposed automatic output parsing protocol, through which the
extracted type-specific answers of different models were obtained, and the performance of the
model is further evaluated through standard task-specific evaluation metrics.
• Classification tasks contain MOL TOX, MOL HIV, MOL BBBP, PPI Binary, PROT EC,
PROT Location, General Text and PPI Type. Model performance is evaluated through accuracy and answer-type validity.
• Regression tasks contain MOL HLGap, MOL Thermo, MOL Excited, CI AbAg,
PLI BA, PROT Mutation, PROT Fitness, PROT Energy, PROT Melt, MOL Freesolv
and MOL Solubility. Model performance is evaluated through RMSE, MEAN, STD and
answer-type validity.
• Generation tasks contain MOL Resyn, MOL Syn, PROT GO, PROT Conserve, PROT SSC,
PROT Fold and DDI Interact. Model performance is evaluated through similarity metrics
such as MACCS, RDK, MORGAN, Meteor and Levenshtein distance.
5. Tool calling API. Candidate tools were sourced exclusively from ToolUniverse[43],
which standardizes tool specifications in JSON format (including name, description, parameters,
and execution endpoints). The selected tools for this evaluation were:
• ADM ET AI predict solubility lipophilicity hydration: A graph neural network-based
platform for rapid prediction of ADMET properties across large chemical libraries. The output
values of Solubility AqSolDB and HydrationF reeEnergy F reeSolv property represent
results of MOL Solubility and MOL Freesolv task, respectively.
• ADM ET AI predict BBB penetrance: used to execute MOL BBBP task, representing
with BBB M artins property value.
• ADM ET AI predict stress response: used to execute MOL TOX task, representing with
SR − ARE toxicity value.
4.2 LLM Evalution
1. Model Selection and Deployment. Both open-source and closed-source LLMs were selected
to enable transparent and reproducible deployment. The primary models evaluated were listed in
Table 2. The parameter scale, model architecture, and thinking mode of these models vary. For
open-source models, we deployed them with vllm[72]. For closed-source models, batch testing
was conducted by calling the API interface (openai.client) with equivalent prompts. Temperature was set to 0.7, and top-p was fixed at 1.0 by default. Various comparative experiments and
analyses were conducted, including:
• The performance of general-purpose LLMs and domain-specific fine-tuned models on
BioMol-LLM-Bench.

• Based on the same backbone model, compare model performance before and after CoT finetuning (Qwen-3-14B vs. DeepSeek-R1-Distill-Qwen-14B).
• Compare the performance of models with different parameter scales.
• The performance of different architecture models (dense transformer, MoE, Mamba) under
similar parameter scales.
• The impact of input prompt complexity, think mode, and other configurations.
• The impact of external tool assistance on model performance.
2. Prompt definition. Consistent prompts were designed to standardize input for generalpurpose LLMs. Prompts were stored as reusable templates in a configuration file. For each task,
a natural language prompt template was defined, incorporating the molecular representation
and task-specific instructions. Models were prompted in a standardized zero-shot manner. To
compare the prompt complexity influence on model performance, we also define the simplified
prompt template for each task.
Simple prompt template for MOL Freesolv task:
Context: Given the [SMILES] sequence of a molecule, your task is to predict its free energy.
Your response should be in the following format:
Answer: {your answer, representing with a floating-point number.}

Detailed prompt template for MOL Freesolv task:
Instruction: The solvation free energy of a molecule is a thermodynamic measure of how
favorably a molecule dissolves in a solvent (typically water).
Context: Given the [SMILES] sequence of a molecule, your task is to predict its free
energy.
Your response should be in the following format:
Explanation: {your explanation for your answer, this is optional.}
Answer: {your answer, representing with a floating-point number.}
Confidence: {your confidence score between 0% and 100% for your answer.}
For fine-tuned domain-specific models such as NatureLM-8x7B and TxGemma-Chat-9B,
since they have predefined fine-tuning templates, we construct prompts for each task by
referencing the original template.
Prompt template for NatureLM-8x7B:
Instruction: Predict solvation free energy of the molecule. {}
Response:

Prompt template for TxGemma-Chat-9B:
Instructions: Answer the following question about molecular property.

Context: The solvation free energy of a molecule is a thermodynamic measure of how
favorably a molecule dissolves in a solvent (typically water).
Question: Given the [SMILES] sequence of a molecule, predict its free energy.
Answer:

Availability and implementation
Source code is available at https://github.com/AI-HPC-Research-Team/BioMol-LLM-Bench,
and the benchmark dataset is available at https://github.com/AI-HPC-Research-Team/
BioMol-LLM-Bench/tree/main/dataset. The code is released under Apache-2.0 License.

References
[1] Kortemme, T., Baker, D.: Computational design of protein–protein interactions. Current
opinion in chemical biology 8(1), 91–97 (2004)
[2] Gibson, D.G., Benders, G.A., Andrews-Pfannkoch, C., Denisova, E.A., Baden-Tillson, H.,
Zaveri, J., Stockwell, T.B., Brownley, A., Thomas, D.W., Algire, M.A., et al.: Complete
chemical synthesis, assembly, and cloning of a mycoplasma genitalium genome. science
319(5867), 1215–1220 (2008)
[3] Powner, M.W., Gerland, B., Sutherland, J.D.: Synthesis of activated pyrimidine ribonucleotides in prebiotically plausible conditions. Nature 459(7244), 239–242 (2009)
[4] Douglas, S.M., Bachelet, I., Church, G.M.: A logic-gated nanorobot for targeted transport
of molecular payloads. Science 335(6070), 831–834 (2012)
[5] Langer, R., Tirrell, D.A.: Designing materials for biology and medicine. Nature 428(6982),
487–492 (2004)
[6] Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F.L., Almeida, D.,
Altenschmidt, J., Altman, S., Anadkat, S., et al.: Gpt-4 technical report. arXiv preprint
arXiv:2303.08774 (2023)
[7] Team, G., Anil, R., Borgeaud, S., Alayrac, J.-B., Yu, J., Soricut, R., Schalkwyk, J., Dai,
A.M., Hauth, A., Millican, K., et al.: Gemini: a family of highly capable multimodal
models. arXiv preprint arXiv:2312.11805 (2023)
[8] Team, G., Mesnard, T., Hardin, C., Dadashi, R., Bhupatiraju, S., Pathak, S., Sifre, L.,
Rivière, M., Kale, M.S., Love, J., et al.: Gemma: Open models based on gemini research
and technology. arXiv preprint arXiv:2403.08295 (2024)
[9] Guo, D., Yang, D., Zhang, H., Song, J., Wang, P., Zhu, Q., Xu, R., Zhang, R., Ma, S., Bi, X.,
et al.: Deepseek-r1 incentivizes reasoning in llms through reinforcement learning. Nature
645(8081), 633–638 (2025)
[10] Bai, J., Bai, S., Chu, Y., Cui, Z., Dang, K., Deng, X., Fan, Y., Ge, W., Han, Y., Huang, F.,
et al.: Qwen technical report. arXiv preprint arXiv:2309.16609 (2023)
[11] Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M.-A., Lacroix, T., Rozière, B.,

Goyal, N., Hambro, E., Azhar, F., et al.: Llama: Open and efficient foundation language
models. arXiv preprint arXiv:2302.13971 (2023)
[12] Basant, A., Khairnar, A., Paithankar, A., Khattar, A., Renduchintala, A., Malte, A.,
Bercovich, A., Hazare, A., Rico, A., Ficek, A., et al.: Nvidia nemotron nano 2: An accurate
and efficient hybrid mamba-transformer reasoning model. arXiv preprint arXiv:2508.14444
(2025)
[13] Abdin, M., Aneja, J., Behl, H., Bubeck, S., Eldan, R., Gunasekar, S., Harrison, M.,
Hewett, R.J., Javaheripi, M., Kauffmann, P., et al.: Phi-4 technical report. arXiv preprint
arXiv:2412.08905 (2024)
[14] Bran, A.M., Cox, S., Schilter, O., Baldassari, C., White, A.D., Schwaller, P.: Chemcrow:
Augmenting large-language models with chemistry tools. arXiv preprint arXiv:2304.05376
(2023)
[15] Beltagy, I., Lo, K., Cohan, A.: Scibert: A pretrained language model for scientific text.
In: Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing and the 9th International Joint Conference on Natural Language Processing
(EMNLP-IJCNLP), pp. 3615–3620 (2019)
[16] Wang, E., Schmidgall, S., Jaeger, P.F., Zhang, F., Pilgrim, R., Matias, Y., Barral, J.,
Fleet, D., Azizi, S.: Txgemma: Efficient and agentic llms for therapeutics. arXiv preprint
arXiv:2504.06196 (2025)
[17] Pei, Q., Wu, L., Gao, K., Liang, X., Fang, Y., Zhu, J., Xie, S., Qin, T., Yan, R.: Biot5+:
Towards generalized biological understanding with iupac integration and multi-task tuning.
In: Findings of the Association for Computational Linguistics: ACL 2024, pp. 1216–1240
[18] Xia, Y., Jin, P., Xie, S., He, L., Cao, C., Luo, R., Liu, G., Wang, Y., Liu, Z., Chen, Y.-J., et
al.: Naturelm: Deciphering the language of nature for scientific discovery. arXiv e-prints,
2502 (2025)
[19] Zhuang, X., Ding, K., Lyu, T., Jiang, Y., Li, X., Xiang, Z., Wang, Z., Qin, M., Feng,
K., Wang, J., et al.: Advancing biomolecular understanding and design following human
instructions. Nature Machine Intelligence 7(7), 1154–1167 (2025)
[20] Rein, D., Hou, B.L., Stickland, A.C., Petty, J., Pang, R.Y., Dirani, J., Michael, J., Bowman, S.R.: Gpqa: A graduate-level google-proof q&a benchmark. In: First Conference on
Language Modeling
[21] Wang, Y., Ma, X., Zhang, G., Ni, Y., Chandra, A., Guo, S., Ren, W., Arulraj, A., He, X.,
Jiang, Z., et al.: Mmlu-pro: A more robust and challenging multi-task language understanding benchmark. Advances in Neural Information Processing Systems 37, 95266–95290
[22] Wang, X., Hu, Z., Lu, P., Zhu, Y., Zhang, J., Subramaniam, S., Loomba, A.R., Zhang, S.,
Sun, Y., Wang, W.: Scibench: Evaluating college-level scientific problem-solving abilities
of large language models. arXiv preprint arXiv:2307.10635 (2023)

[23] Sun, L., Han, Y., Zhao, Z., Ma, D., Shen, Z., Chen, B., Chen, L., Yu, K.: Scieval: A multilevel large language model evaluation benchmark for scientific research. In: Proceedings
of the AAAI Conference on Artificial Intelligence, vol. 38, pp. 19053–19061 (2024)
[24] Olea, C., Tucker, H., Phelan, J., Pattison, C., Zhang, S., Lieb, M., Schmidt, D., White, J.:
Evaluating persona prompting for question answering tasks. In: Proceedings of Th e 10th
International Conference on Artificial Intelligence and Soft Computing, Sydney, Australia
[25] Phan, L., Gatti, A., Han, Z., Li, N., Hu, J., Zhang, H., Zhang, C.B.C., Shaaban, M., Ling,
J., Shi, S., et al.: Humanity’s last exam. arXiv preprint arXiv:2501.14249 (2025)
[26] Saikh, T., Ghosal, T., Mittal, A., Ekbal, A., Bhattacharyya, P.: Scienceqa: A novel resource
for question answering on scholarly articles. International Journal on Digital Libraries
23(3), 289–301 (2022)
[27] Laurent, J.M., Janizek, J.D., Ruzo, M., Hinks, M.M., Hammerling, M.J., Narayanan,
S., Ponnapati, M., White, A.D., Rodriques, S.G.: Lab-bench: Measuring capabilities of
language models for biology research. arXiv preprint arXiv:2407.10362 (2024)
[28] Shen, Y., Chen, Z., Mamalakis, M., He, L., Xia, H., Li, T., Su, Y., He, J., Wang, Y.G.: A
fine-tuning dataset and benchmark for large language models for protein understanding.
In: 2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM), pp.
2390–2395 (2024). IEEE
[29] Walker, T., Grulke, C.M., Pozefsky, D., Tropsha, A.: Chembench: a cheminformatics
workbench. Bioinformatics 26(23), 3000–3001 (2010)
[30] Yu, B., Baker, F.N., Chen, Z., Ning, X., Sun, H.: Llasmol: Advancing large language models for chemistry with a large-scale, comprehensive, high-quality instruction tuning dataset.
arXiv preprint arXiv:2402.09391 (2024)
[31] Wu, Z., Ramsundar, B., Feinberg, E.N., Gomes, J., Geniesse, C., Pappu, A.S., Leswing, K.,
Pande, V.: Moleculenet: a benchmark for molecular machine learning. Chemical science
9(2), 513–530 (2018)
[32] Zhu, Y., Hwang, J., Adams, K., Liu, Z., Nan, B., Stenfors, B., Du, Y., Chauhan, J.,
Wiest, O., Isayev, O., et al.: Learning over molecular conformer ensembles: Datasets and
benchmarks. arXiv preprint arXiv:2310.00115 (2023)
[33] Rao, R., Bhattacharya, N., Thomas, N., Duan, Y., Chen, P., Canny, J., Abbeel, P., Song, Y.:
Evaluating protein transfer learning with tape. Advances in neural information processing
systems 32 (2019)
[34] Dallago, C., Mou, J., Johnston, K.E., Wittmann, B.J., Bhattacharya, N., Goldman, S.,
Madani, A., Yang, K.K.: Flip: Benchmark tasks in fitness landscape inference for proteins.
bioRxiv, 2021–11 (2021)
[35] Gao, S., Zhu, R., Kong, Z., Noori, A., Su, X., Ginder, C., Tsiligkaridis, T., Zitnik, M.:
Txagent: an ai agent for therapeutic reasoning across a universe of tools. arXiv preprint

arXiv:2503.10970 (2025)
[36] Ding, K., Yu, J., Huang, J., Yang, Y., Zhang, Q., Chen, H.: Scitoolagent: a knowledgegraph-driven scientific agent for multitool integration. Nature Computational Science
5(10), 962–972 (2025)
[37] Notin, P., Kollasch, A., Ritter, D., Van Niekerk, L., Paul, S., Spinner, H., Rollins, N.,
Shaw, A., Orenbuch, R., Weitzman, R., et al.: Proteingym: Large-scale benchmarks for
protein fitness prediction and design. Advances in neural information processing systems
36, 64331–64379 (2023)
[38] Thumuluri, V., Almagro Armenteros, J.J., Johansen, A.R., Nielsen, H., Winther, O.:
Deeploc 2.0: multi-label subcellular localization prediction using protein language models.
Nucleic acids research 50(W1), 228–234 (2022)
[39] Huang, K., Fu, T., Glass, L.M., Zitnik, M., Xiao, C., Sun, J.: Deeppurpose: a deep learning library for drug–target interaction prediction. Bioinformatics 36(22-23), 5545–5547
(2020)
[40] Zhao, X., Tang, Y.-C., Singh, A., Cantu, V.J., An, K., Lee, J., Stogsdill, A.E., Hamdi,
I.M., Ramesh, A.K., An, Z., et al.: Abbibench: A benchmark for antibody binding affinity
maturation and design. arXiv preprint arXiv:2506.04235 (2025)
[41] Sorkun, M.C., Khetan, A., Er, S.: Aqsoldb, a curated reference set of aqueous solubility
and 2d descriptors for a diverse set of compounds. Scientific data 6(1), 143 (2019)
[42] Li, G., Yao, S., Fan, L.: Prostage: Predicting effects of mutations on protein stability
by using protein embeddings and graph convolutional networks. Journal of Chemical
Information and Modeling 64(2), 340–347 (2024)
[43] Gao, S., Zhu, R., Sui, P., Kong, Z., Aldogom, S., Huang, Y., Noori, A., Shamji, R., Parvataneni, K., Tsiligkaridis, T., et al.: Democratizing ai scientists using tooluniverse. arXiv
preprint arXiv:2509.23426 (2025)
[44] Abramson, J., Adler, J., Dunger, J., Evans, R., Green, T., Pritzel, A., Ronneberger, O., Willmore, L., Ballard, A.J., Bambrick, J., et al.: Accurate structure prediction of biomolecular
interactions with alphafold 3. Nature 630(8016), 493–500 (2024)
[45] Swanson, K., Walther, P., Leitz, J., Mukherjee, S., Wu, J.C., Shivnaraine, R.V., Zou,
J.: Admet-ai: a machine learning admet platform for evaluation of large-scale chemical
libraries. Bioinformatics 40(7), 416 (2024)
[46] Van Kempen, M., Kim, S.S., Tumescheit, C., Mirdita, M., Lee, J., Gilchrist, C.L., Söding,
J., Steinegger, M.: Fast and accurate protein structure search with foldseek. Nature
biotechnology 42(2), 243–246 (2024)
[47] Maziarz, K.: USPTO-50K (2024). https://doi.org/10.6084/m9.figshare.25459573
[48] Knox, C., Wilson, M., Klinger, C.M., Franklin, M., Oler, E., Wilson, A., Pon, A., Cox, J.,
Chin, N.E., Strawbridge, S.A., et al.: Drugbank 6.0: the drugbank knowledgebase for 2024.

Nucleic acids research 52(D1), 1265–1275 (2024)
[49] Berman, H.M., Westbrook, J., Feng, Z., Gilliland, G., Bhat, T.N., Weissig, H., Shindyalov,
I.N., Bourne, P.E.: The protein data bank. Nucleic acids research 28(1), 235–242 (2000)
[50] Delaney, J.S.: Esol: estimating aqueous solubility directly from molecular structure. Journal
of chemical information and computer sciences 44(3), 1000–1005 (2004)
[51] Mobley, D.L., Guthrie, J.P.: Freesolv: a database of experimental and calculated hydration
free energies, with input files. Journal of computer-aided molecular design 28(7), 711–720
(2014)
[52] Ramakrishnan, R., Hartmann, M., Tapavicza, E., Von Lilienfeld, O.A.: Electronic spectra
from tddft and machine learning in chemical space. The Journal of chemical physics 143(8)
(2015)
[53] Ruddigkeit, L., Van Deursen, R., Blum, L.C., Reymond, J.-L.: Enumeration of 166 billion
organic small molecules in the chemical universe database gdb-17. Journal of chemical
information and modeling 52(11), 2864–2875 (2012)
[54] Martins, I.F., Teixeira, A.L., Pinheiro, L., Falcao, A.O.: A bayesian approach to in silico
blood-brain barrier penetration modeling. Journal of chemical information and modeling
52(6), 1686–1697 (2012)
[55] Hu, W., Fey, M., Ren, H., Nakata, M., Dong, Y., Leskovec, J.: Ogb-lsc: A large-scale
challenge for machine learning on graphs. arXiv preprint arXiv:2103.09430 (2021)
[56] Jarzab, A., Kurzawa, N., Hopf, T., Moerch, M., Zecha, J., Leijten, N., Bian, Y., Musiol, E.,
Maschberger, M., Stoehr, G., et al.: Meltome atlas—thermal proteome stability across the
tree of life. Nature methods 17(5), 495–503 (2020)
[57] Pancotti, C., Benevenuta, S., Birolo, G., Alberini, V., Repetto, V., Sanavia, T., Capriotti,
E., Fariselli, P.: Predicting protein stability changes upon single-point mutation: a thorough
comparison of the available tools on a new dataset. Briefings in Bioinformatics 23(2), 555
(2022)
[58] Wu, N.C., Dai, L., Olson, C.A., Lloyd-Smith, J.O., Sun, R.: Adaptation in protein fitness
landscapes is facilitated by indirect paths. elife 5, 16965 (2016)
[59] Sarkisyan, K.S., Bolotin, D.A., Meer, M.V., Usmanova, D.R., Mishin, A.S., Sharonov,
G.V., Ivankov, D.N., Bozhanova, N.G., Baranov, M.S., Soylemez, O., et al.: Local fitness
landscape of the green fluorescent protein. Nature 533(7603), 397–401 (2016)
[60] Gligorijević, V., Renfrew, P.D., Kosciolek, T., Leman, J.K., Berenberg, D., Vatanen, T.,
Chandler, C., Taylor, B.C., Fisk, I.M., Vlamakis, H., et al.: Structure-based protein function prediction using graph convolutional networks. Nature communications 12(1), 3168
(2021)
[61] Zhou, J., Troyanskaya, O.: Deep supervised and convolutional generative stochastic network for protein secondary structure prediction. In: International Conference on Machine

Learning, pp. 745–753 (2014). PMLR
[62] Moult, J., Fidelis, K., Kryshtafovych, A., Schwede, T., Tramontano, A.: Critical assessment of methods of protein structure prediction (CASP)-Round XII. Proteins: Structure,
Function, and Bioinformatics 86, 7–15 (2018) https://doi.org/10.1002/prot.25415
[63] Chen, M., Ju, C.J.-T., Zhou, G., Chen, X., Zhang, T., Chang, K.-W., Zaniolo, C., Wang,
W.: Multifaceted protein–protein interaction prediction based on siamese residual rcnn.
Bioinformatics 35(14), 305–314 (2019)
[64] Song, B., Luo, X., Luo, X., Liu, Y., Niu, Z., Zeng, X.: Learning spatial structures of proteins improves protein–protein interaction prediction. Briefings in bioinformatics 23(2),
558 (2022)
[65] Jankauskaitė, J., Jiménez-Garcı́a, B., Dapkūnas, J., Fernández-Recio, J., Moal, I.H.:
Skempi 2.0: an updated benchmark of changes in protein–protein binding energy, kinetics
and thermodynamics upon mutation. Bioinformatics 35(3), 462–469 (2019)
[66] Liu, T., Hwang, L., Burley, S.K., Nitsche, C.I., Southan, C., Walters, W.P., Gilson, M.K.:
Bindingdb in 2024: a fair knowledgebase of protein-small molecule binding data. Nucleic
acids research 53(D1), 1633–1644 (2025)
[67] Davis, M.I., Hunt, J.P., Herrgard, S., Ciceri, P., Wodicka, L.M., Pallares, G., Hocker,
M., Treiber, D.K., Zarrinkar, P.P.: Comprehensive analysis of kinase inhibitor selectivity.
Nature biotechnology 29(11), 1046–1051 (2011)
[68] DeepSeek-AI: DeepSeek-V3.1-Terminus (2025). https://huggingface.co/deepseek-ai/
DeepSeek-V3.1-Terminus
[69] OpenAI: GPT-5 mini (2025). https://developers.openai.com/api/docs/models/gpt-5-mini
[70] Agarwal, S., Ahmad, L., Ai, J., Altman, S., Applebaum, A., Arbus, E., Arora, R.K., Bai,
Y., Baker, B., Bao, H., et al.: gpt-oss-120b & gpt-oss-20b model card. arXiv preprint
arXiv:2508.10925 (2025)
[71] Team, M.: Mistral-Nemo-Instruct-2407
Mistral-Nemo-Instruct-2407

(2024).

https://huggingface.co/mistralai/

[72] Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu, C.H., Gonzalez, J., Zhang, H.,
Stoica, I.: Efficient memory management for large language model serving with pagedattention. In: Proceedings of the 29th Symposium on Operating Systems Principles, pp.
611–626 (2023)

Appendix A

Supplementary Table.

Supplementary Table: Detailed descriptions of benchmark task.

Description

L0

Domain knowledge understanding with text-input only.

L1

The solubility of a molecule refers to its ability to dissolve in
a solvent (typically water) to form a homogeneous solution.
The solvation free energy of a molecule is a thermodynamic
measure of how favorably a molecule dissolves in a solvent
(typically water).
Predict the forward synthesis production of two molecules.
Given production, predict the reactant molecules.
E1 property of a moleculer refers to the energy of lowest
singlet excited state relative to the ground state. Predict the
energy of lowest singlet excited state relative to ground state
of molecule in eV units.
Predict the heat capacity of molecule in kcal/mol/K scale.
The BBBP (Blood-Brain Barrier Penetration) property represents whether a molecule can cross the blood-brain barrier.
The HIV replication prevention property refers to a molecule’s
ability to inhibit one or more steps in the HIV replication cycle,
thereby preventing viral proliferation.
The HOMO-LUMO gap (Highest Occupied Molecular Orbital
- Lowest Unoccupied Molecular Orbital gap) represents
energy difference between HOMO and LUMO (measured in
eV or kcal/mol).
The SR-ARE (Sulfonamide Reactive - Aryl Ester) toxicity
refers to the adverse effects caused by molecules containing
sulfonamide and aryl ester functional groups.

L2

PROT Conserve

The melting point of a protein is the temperature at which 50%
of the protein unfolds, marking the midpoint of the transition
from the folded (native) state to the unfolded (denatured) state.
The stability of a mutated protein sequence represents the free
energy difference between mutated sequence and its native
sequence.
The fitness landscape represents how mutations affect functionality (e.g., enzymatic activity, binding affinity, stability) of
a protein.
The mutation score of mutated protein quantifies the functional/structural impact of a small fraction of amino acid
changes.
The conservation score measures how evolutionarily conserved a residue across homologs (reflects purifying selection).
The subcellular localization class of a protein refers to its
specific compartment or organelle within a cell where it
predominantly resides and functions.
Continued on next page

Continued from previous page

Description

The Enzyme Commission (EC) system classifies enzymes into
a hierarchical numbering system (e.g., EC 1.1.1.1 for alcohol
dehydrogenase) based on their catalytic reactions. The task is
to predict first-level EC class number of protein.
The Gene Ontology (GO) describes protein functions in three
categories: Molecular Function (MF), Biological Process (BP)
and Cellular Component (CC). The task is to predict the
Molecular Function (MF) properties of protein.
Secondary structure classification typically follows the DSSP
(Define Secondary Structure of Proteins) standard, which categorizes each amino acid of the protein into distinct classes.
Predict the 3D structure of protein.

PROT SSC

PROT Fold
L3

Predict the PPI interaction types between two proteins.
The task of predicting whether two proteins interact or not.
Predict the DDI interaction type between two drugs.
Predict the PLI binding affinity between protein and ligand.
Predict the AbAg binding affinity between antibody (heavy
and light chain) and antigen.
