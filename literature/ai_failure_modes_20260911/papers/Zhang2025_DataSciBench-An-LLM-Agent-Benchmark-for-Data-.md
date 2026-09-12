# DataSciBench: An LLM Agent Benchmark for Data Science

**Authors:** Zhang, Dan; Zhoubian, Sining; Cai, Min; Li, Fengzu; Yang, Lekang; Wang, Wei; Dong, Tianjiao; Hu, Ziniu; Tang, Jie; Yue, Yisong
**Year:** 2025
**Venue:** arXiv
**arXiv:** 2502.13897
**Source PDF URL:** https://arxiv.org/pdf/2502.13897
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---
DataSciBench: An LLM Agent Benchmark for Data Science
Dan Zhang1,2,† , Sining Zhoubian1,2,† , Min Cai2,† , Fengzu Li1 , Lekang Yang1
Wei Wang1 , Tianjiao Dong3,† , Ziniu Hu4 , Jie Tang1 , Yisong Yue4
Tsinghua University; 2 Zhipu AI;
University of California, Berkeley; 4 California Institute of Technology
https://datascibench.github.io/

Prompt for Data Science

Abstract

This paper presents DataSciBench, a comprehensive benchmark for evaluating Large
Language Model (LLM) capabilities in data
science. Recent related benchmarks have primarily focused on single tasks, easily obtainable ground truth, and straightforward evaluation metrics, which limits the scope of
tasks that can be evaluated. In contrast,
DataSciBench is constructed based on a
more comprehensive and curated collection of
natural and challenging prompts for uncertain
ground truth and evaluation metrics. We develop a semi-automated pipeline for generating ground truth (GT) and validating evaluation metrics. This pipeline utilizes and implements an LLM-based self-consistency and
human verification strategy to produce accurate GT by leveraging collected prompts, predefined task types, and aggregate functions
(metrics). Furthermore, we propose an innovative Task - Function - Code (TFC) framework to assess each code execution outcome
based on precisely defined metrics and programmatic rules. Our experimental framework involves testing 6 API-based models,
8 open-source general models, and 9 opensource code generation models using the diverse set of prompts we have gathered. This
approach aims to provide a more comprehensive and rigorous evaluation of LLMs in data
science, revealing their strengths and weaknesses. Experimental results demonstrate that
API-based models outperform open-sourced
models on all metrics and Deepseek-Coder33B-Instruct achieves the highest score among
open-sourced models. We release all code and
data at https://github.com/THUDM/
DataSciBench/.

Introduction

Large language models (LLMs) (Achiam et al.,
2023; Team et al., 2023; GLM et al., 2024) are
†

work done while these authors interned at Zhipu AI.

Implement the desired _marketing_expenditure function, which returns the required amount of money that
needs to be invested in a new marketing campaign to sell the desired number of units.

2024/12/16 13:39

Subtasks: Task (1) Expenditure Calculation:\n - Input: Use the model parameters from `model_parameters.csv`
and the desired number of units to sell.\n - Output: Calculate the required marketing expenditure and save the
result as `required_expenditure.txt` containing a single float value. Task (2) ··· Task (3) ···
Marketing Expenditure Calcu... | Open WebUI

Vanilla Response

Expenditure = a + b × (Desired Units)
a

b

Predictive modeling

Task

model_parameters.csv

Function
1 import csv
3 ⌄ def load_model_parameters(filename):
4⌄
with open(filename, mode='r') as file:
csv_reader = csv.DictReader(file)
parameters = {}
7⌄
for row in csv_reader:
parameters[row['Parameter']] = float(row['Value'
return parameters
11 ⌄ def calculate_marketing_expenditure(parameters, desired_unit
a = parameters['a']
b = parameters['b']
expenditure = a + b * desired_units
return expenditure
17 ⌄ def save_expenditure(expenditure, filename='required_expendit
18 ⌄
with open(filename, mode='w') as file:
file.write(f"{expenditure:.2f}")
21 ⌄ def main():
param_file = 'model_parameters.csv'
desired_units = 1000 # You can modify this value as need
# Load model parameters
parameters = load_model_parameters(param_file)
# Calculate required expenditure
expenditure = calculate_marketing_expenditure(parameters
# Save the result

https://chat.glm.ai/c/7c741e60-10eb-4fde-ae85-d2afc35bc4b5

R-squared Value

def model_performance_r_squared(ground_truth):
from sklearn.metrics import r2_score
output = pd.read_csv("model_parameters.csv")
output_gt = pd.read_csv(ground_truth)

Code

# Read cleaned campaign data for actual units sold
cleaned_data = pd.read_csv("cleaned_campaign_data.csv")
X = cleaned_data[['Marketing expenditure']]
y = cleaned_data['Units sold']
# Retrieving model coefficients
coefficients = output.iloc[0].tolist()
model_predictions = X * coefficients[0]
coefficients_gt = output_gt.iloc[0].tolist()
model_predictions_gt = X * coefficients_gt[0]
return bool(r2_score(y, model_predictions) >= r2_score(y,
model_predictions_gt))

1/1

Figure 1: This example compares the vanilla response
and the DataSciBench response for a given prompt.
The vanilla response provides only code, lacking evaluation metrics. In contrast, DataSciBench identifies evaluation tasks, provides evaluation functions, and
generates programmatic code to form a TFC list.

increasingly used in data science and scientific domains, e.g., data analysis (Hong et al., 2024), protein generation (Jumper et al., 2021; Chen et al.,
2024a), and scientific discovery (Lu et al., 2024)
and reasoning (Zhang et al., 2024a,b). For data
science tasks, given a publicly known problem,
LLMs offer the potential to (semi-)autonomously
conduct data analysis (Huang et al., 2023) and
data visualization (Hong et al., 2024) by invoking code interpreters with corresponding Python
libraries. These works are benchmarked on relatively straightforward tasks where ground truth
(GT) labels can be precisely obtained. However,
much of real-world data analysis requires reasoning over more complex scenarios (Chen et al.,
2024b) as shown in Figure 1, such as calculating expenditure, and evaluating the quality of the
images generated by the data visualization task.
Properly evaluating these more complex data science tasks remains an open research direction.
While some existing benchmarks are used to

Table 1: Comparison with related work. LC denotes LeetCode.
Benchmark

Prompt Source

Evaluation Metrics

DS-1000 (Lai et al., 2023)
MLAgentBench (Huang et al., 2023)
LiveCodeBench (Jain et al., 2024)
NaturalCodeBench (Zhang et al., 2024c)
BigCodeBench (Zhuo et al., 2024)

StackOverflow
Kaggle
LC & AtCoder & CodeForces
CodeGeeX
StackOverflow

Test Cases + Surface-Form Constraints
Acc. + Success Rate, Human

Text2Analysis (He et al., 2023)
InfiAgent-DABench (Hu et al., 2024)

Human & LLM
LLM

Executable code ratio, Acc., Regression scores
Acc.

DataSciBench (Ours)

CodeGeeX & BCB & Human

Aggregate Metrics and Programmatic Rules

evaluate LLMs for related challenges (see Table 1), those benchmarks (e.g., MLAgentBench,
Text2Analysis) typically focus on evaluating narrower tasks with easy-to-obtain ground truth and
straightforward evaluation metrics (e.g., Acc.).
For example, MLAgentBench (Huang et al., 2023)
presents a machine learning research benchmark
by building an LLM Agent pipeline. As shown in
Figure 1, the frontier of LLM evaluation is towards
more complex real-world tasks that consist of multiple subtasks. For these challenging prompts, how
to generate GT and define specific evaluation metrics for each subtask in a comprehensive perspective is a question worth exploring.
To address the gap between task selection, evaluation function definition, and automated code execution in data science contexts, we introduce a
new benchmark, called DataSciBench, which
evaluates the data science abilities of LLMs and
provides insights to help LLMs improve their
data analysis and data visualization abilities. Regarding collected prompts, their corresponding responses, and evaluation metrics, we hope that
prompts meet the following characteristics: 1) Require more natural, challenging, and high-quality
prompts to promote the development of LLMs’
improvement; 2) Identify 6 defined data science
tasks, e.g., data preprocessing, statistics, visualization, mining, and interpretability; 3) Require
multiple types of results to perform comprehensive evaluations and distinguish models well.
In this paper, to efficiently generate GT and
the evaluation metric for key tasks, we propose
a novel semi-automated framework called Task Function - Code (TFC) to address critical challenges in the automated evaluation of data science
tasks. Specifically, from a coarse-grained perspective, we first aggregate the scope of task types,
evaluation functions, and corresponding codes.
Then, from a fine-grained perspective, we de-

fine programmatic rules for each function’s output
based on the specific tasks and compare generation results with ground truth to ensure a fair and
consistent assessment.
To validate the effectiveness of LLMs on collected 222 comprehensive prompts with proposed
519 GTs, we experiment with 6 API-based models, 8 open-sourced general models, and 9 opensourced code generation models. We observe
that API-based models greatly outperform opensourced models on average. Specifically, GPT4o surpasses all other models on all metrics and
Deepseek-Coder-33B-Instruct achieves the highest score among open-sourced models. However,
all models have significant room for improvement
in following fine-grained instructions, calling the
appropriate tools, executing accurate plans, and
exporting the required execution outputs.
Overall, our key contributions are as follows:
• We introduce DataSciBench, a comprehensive benchmark designed to assess the performance of LLMs in data science tasks in Figure 2.
We develop a semi-automated pipeline to generate ground truth and evaluate aggregated metrics
using carefully crafted complex questions.
• We propose an innovative Task-Function-Code
(TFC) evaluation framework based on predefined aggregated metrics and programmatic
rules. We then assess 23 large language models
from both coarse-grained and fine-grained perspectives, presenting the results in Table 2.
• Various analyses of comparisons and correlations between ours and existing benchmarks are
performed in Figure 6 and Table 3. Furthermore,
we provide research insights derived from experimental outcomes of the evaluated LLMs that
point to interesting directions for future work.

Data

Large
Language

3. LLM Evaluation

1. Prompt Definition and Collection
1. Prompt Collection
Task Type

Aggregate Function

Prompt
Large Language Models
Task type

Function
𝑹: [(T, F, C), ···]

Code

ü Data cleaning completeness
ü Data Integrity
ü Visualization completeness
ü Predictive modeling
ü Clustering validity

2. Question Filtering

(3) Data
visualization
(4) Predictive
modeling
(5) Data mining &
Pattern recognition

(6) Interpretability
& Report generation

Online platform:
CodeGeeX
Synthesized from
LLMs
Human-Written

Select task type

Filter irrelevant

3. Expert Review

Verify correctness

Format instructions

Collect datasets

Data
Interpreter

(1) Data cleaning
& preprocessing
(2) Data
exploration &
statistics
understand

2. Response Integration and Validation

ü Pattern detection precision
ü Report quality
Directed
Acyclic Graph

Test Case with Ground Truth

Prompt: ***
TFC-list: ***
Input data: ***
Ground truth: ***

Programmatic Rules
Ø Output
Ground truth
Ø Return of initial output：
Boolean: 0 or 1
Decimal: Threshold check
Ø Final output:
Boolean

Figure 2: The overall framework of DataSciBench encompasses three key components aligned with Section 3:
1) Prompt definition and collection, which covers 6 task types, prompt collection, question filtering, and expert
review. 2) Response integration and validation, incorporating the TFC framework (25 aggregated functions and
programmatic rules) and 519 test cases with ground truth. 3) LLM evaluation involving 23 LLMs.

Background on using LLMs for Data

This section discusses the key aspects that underlie
our benchmarking approach.
Ground Truth Generation. Ground truth serves
as the cornerstone for evaluating the performance
of LLMs in data science tasks. For diverse and
challenging data science prompts, we aim to propose a semi-automated pipeline that leverages a
robust LLM to generate GTs and employs selfconsistency and human validation strategies to ensure the accuracy and reliability of generated GTs.
Evaluation Metric Definition. Defining appropriate and meaningful evaluation metrics is essential for effectively comparing and analyzing
the effectiveness of different LLMs in data science tasks. Our study meticulously defines evaluation metrics tailored to the specific tasks and challenges the collected prompts pose. These metrics
are designed to capture the diverse nuances of data
analysis and visualization tasks, enabling a comprehensive assessment of LLMs’ capabilities.
Limitation of Previous Studies. Prior research
in benchmarking LLMs for data science has often been limited by focusing on single tasks, sim-

plistic evaluation metrics, and readily available
ground truth. These shortcomings hinder the thorough evaluation of LLMs and may not fully capture their strengths and weaknesses. By addressing these limitations, our study seeks to provide
a more comprehensive and nuanced assessment of
LLMs in data science. Through the development
of DataSciBench and the implementation of a
rigorous evaluation framework, we aim to push the
boundaries of benchmarking practices in the field
of data science and LLM research.

DataSciBench consists of three important
components as outlined in Figure 2.
• Prompt Definition and Collection which defines 6 task types and collects 222 real, challenging, and high-quality prompts through question
filtering and expert review.
• Response Integration and Validation which
proposes a novel Task - Function - Code (TFC)
that produces 519 test cases to effectively assess
the key tasks of each prompt through defined aggregate functions and programmatic rules.

Dataset Collection

Question Collection.
We collect questions
from four sources: 1) Extensive collection from
a real-world online platform. We collect natural prompts from one online code-generation
platform, CodeGeeX (Zheng et al., 2023). 2)
Extracted and rewritten from a public code
benchmark. We utilize 167 high-quality data
science prompts from BigCodeBench (BCB) and
then refine them to our specified format encompassing input data or file, prompt, and expected
output file with TFC for standardized evaluation.
3) Hand-written by humans. We also write elaborated prompts to increase the difficulty and robustness of the evaluated benchmark by referring
to relative websites1 . 4) Synthesized from LLMs.
We use a few shot examples drawn from humanwritten prompts to ask LLM to generate prompts.
Question Filtering. We filter low-quality questions via the following principles: 1) Choose
questions that include keywords, but are not limited to, “machine learning”, “deep learning”, “data
preprocessing”, and “data visualization”; 2) Filter
questions that require rewriting code, finding errors, and explaining basic concepts.
Expert Review.
We review the prompts we
collect with experts in computer science and data
analysis to ensure their quality. The review process includes three stages: 1) In stage 1, experts

https://ds100.org/course-notes/eda/eda.html

D
Sta ata E
tis xp
tic lo
s U rat
n d i on
ers &
tan
d

Data Valid
ity

ty

Data Cleaning
Completeness

ictive
Pred ling
Mod

Data Uniformity
del
Mo racy
u
Acc
E alu
MAred V g
a r in
squ
R- luste dity
C ali
V

hap
eS
ram ation
F
ta id
Da Val

Da
ta
Pr Cle
ep an
roc in
ess g &
ing

Data Visualization

Interpre
.
& RG
DM
&P
R

Result Comple.
Report
Quality
Repo
rt C
omp
le.
Clu
ster
in
V
Sil alidit g
y
ho
ue
Ve T tte S
co
r if itle
re
ica
tio

tio
za
ali ity
su al
Vi Qu

Task Integration. To increase the difficulty of
prompts, we chose more complex prompts that included multiple defined task types. These sequential tasks can be any combination of six task types.

nte
gri

D
Consi ata
stenc
y

Prompt Definition for Data Science

Task Type. We define six typical data science
tasks in Appendix A.1 that include Data cleaning and preprocessing, Data exploration and statistics understanding, Data visualization, Predictive
modeling, Data mining and Pattern recognition,
and Interpretability and Report generation.

3.2

Data Accuracy

Da
ta I

Vi
Co sual
mp iza
let tion
en
ess

3.1

Data Quality

No
r
Ra mali
nge zat
Ch ion
eck
Co D
m at
pl a
ete
ne
ss

• LLM Evaluation which assesses 6 API-based
models, 8 open-sourced general models, and
9 open-sourced code generation models from
coarse-grained (i.e. success rate, completion
rate) and fine-grained (e.g., Vision-Language
Model (VLM)-as-a-judge, 25 aggregate functions) perspectives.

Plot Validity

Figure 3: Statistics of 6 task types and 25 aggregate
functions in Task-Function-Code (TFC) list. DM & PR
denotes Data Mining & Pattern Recognition. Interpre.
& RG denotes Interpretability & Report Generation.

verify the correctness and adjust the suitability of
prompts. In addition, experts ensure that the responses to the questions are clear and structured
in a way that facilitates assessment. For example, handling missing values in a data frame. 2) In
stage 2, experts format all verified prompts into a
unified instruction that encompasses input data or
file, prompt, and expected output file. 3) In stage
3, experts ensure the availability of input prompt
datasets by collecting public datasets or generating random datasets.
3.3

Response Integration and Validation

Ground Truth Generation and Verification. To
obtain the response of the collected questions, we
propose the following strategy to generate test
cases for each question. Firstly, we generate the
outputs of each prompt by sampling LLMs several times and then execute the generated code to
obtain the final output. Then, we use two different validation methods to determine whether the
LLM-generated answer aligns with the meaning
specified in the aggregate functions to ensure the
reliability of the answer. For questions originating from BCB, where reliable test cases are provided, we validate the generated answer by performing all test cases. Answers that pass all test
cases are re-checked by humans and finally considered ground truth. As for other prompts, we
initially adopt a self-consistency strategy (Wang
et al., 2022) to obtain outputs and then ensure
their reliability and precision by having six authors
of the paper verify the default assigned prompts

and corresponding ground truth elements, including task type, evaluation function, programmatic
code, and final outputs. In cases where uncertainties arise in the generated outputs, we crossvalidate them among three authors.
Evaluation Selection. We introduce a structured
approach to identify and evaluate key tasks across
six established types. We first use GPT-4o-mini to
select several valuable task types, return the corresponding evaluation functions, and generate the
evaluation codes for each prompt to effectively
evaluate the capabilities of LLM and reduce the
evaluation cost. Each group data is simplified as a
tuple (T, F, C) in generated R as follows:
R = {(Ti , Fi , Ci )|N
i },

(1)

where N is the number of valuable task types per
prompt, and this value is different for each question. Then we use the data interpreter (DI) (Hong
et al., 2024) to generate a hierarchical directed
acyclic graph (DAG) for each prompt, in which
each task type is defined as a node at one level in a
DAG, as illustrated in Figure 2. Based on the generated graphs, we take a powerful LLM as a backbone and run all evaluation functions to obtain the
ground truth of each task type. To some extent,
this way of verification can avoid the commonly
used LLM-as-a-Judge black-box assessment.
Function Aggregation. To unify the key functions and improve the scalability of the evaluation, we aggregate all generated functions to the
top-K function category, select top-K functions
for each task type, and finally obtain 25 functions, as shown in Figure 3. Generally, K is set
as 5. For example, the function category for data
cleaning and preprocessing includes Data Cleaning Completeness, DataFrame Shape Validation,
Data Completeness, Normalization Range Check,
and Data Quality Score.
Programmatic Rules.
Regarding aggregate
functions with corresponding codes, we define
unified rules to verify generated code. Specifically, we unify all initial outputs as boolean or
decimal types ranging between 0 and 1. Then,
we obtain the final boolean value by comparing ground truth with prediction output depending on the specific task description of aggregate
functions. For example, regarding Data Cleaning
Completeness, which calculates the final number
of rows/columns after preprocessing, the final output is 1 if the number is the same as the number of

ground truths; otherwise, it is 0. For some specific
tasks whose output type is decimal, we also set a
corresponding threshold to transform the output to
boolean for simplicity. For example, the threshold
is set to 0.5 if the aggregate function is silhouette
score for data mining and pattern recognition.
Summary. Based on the above three submodules, we obtain 222 effective prompts and 519 corresponding test cases for each prompt, 25 aggregated functions, which help evaluations of 6 APIbased and 17 open-sourced models.

Experiments

4.1

Settings

We construct a comprehensive benchmark on our
collected prompts to assess the performance of
23 different models (e.g., API-based models and
open-sourced general/code generation models).
• Six API-based models include o1-mini (Jaech
et al., 2024), GPT-4o-mini (Hurst et al., 2024),
GPT-4o-2024-05-13, GPT-4-Turbo (Achiam
et al., 2023), Claude-3.5-Sonnet2 , and GLM-4Flash (GLM et al., 2024).
• Eight open-sourced general models include Llama3.1-8B-Instruct,
Llama3-8BInstruct, Qwen2.5-7B-Instruct, Qwen2-1.5/7BInstruct (Yang et al., 2024), Gemma2-9Bit (Team et al., 2024), GLM-4-9B-chat, and
Yi-1.5-9B-chat-16k (Young et al., 2024).
• Nine open-sourced code models include
Deepseek-Coder-1.3/6.7/33B-Instruct
(Guo
et
al.,
2024),
CodeLlama-7/13/34BInstruct (Roziere et al., 2023), Qwen2.5Coder-1.5/7B-Instruct (Hui et al., 2024), and
StarCoder2-15B (Lozhkov et al., 2024).
4.2

Evaluation Metrics

Coarse-Grained Metrics. We define the coarsegrained metrics (CR and SR) for evaluating LLMs.
• Completion Rate (CR). Following the CR in
Data Interpreter (Hong et al., 2024), we calculate
the CR for each TFC in R. Specifically, we give
it a completion score, with a minimum score of 0
and a maximum score of 2. The step completion
scores were given as follows: missing (score of 0),
fail (score of 0), success-non-compliant (score of

https://www.anthropic.com/news/claude-3-5-sonnet

Table 2: Overall evaluation results for DataSciBench on all our curated prompts.

SR (%)

VLM

29.77
66.31
50.63
51.93
47.48
30.32

45.26
68.44
57.78
58.87
58.11
34.04

2.87
3.91
3.05
3.09
2.14

44.63
75.93
60.30
62.30
49.07
36.53

19.27
56.14
48.02
36.94
29.42

36.01
69.33
57.84
57.75
55.84
32.57

30.94
71.35
59.24
60.25
52.87
27.64

23.81
57.67
53.54
50.75
46.04
14.44

38.78
64.51
54.18
54.65
52.29
30.74

24.73
2.88
7.07
25.72
43.83
22.84
3.96
38.20

33.89
3.92
11.00
30.38
50.74
25.58
5.46
42.35

1.29
0.52
1.06
1.69
1.16
0.40

38.24
4.18
26.16
31.51
51.18
30.93
4.54
38.14

18.25
1.26
16.90
23.15
36.41
20.78
1.98
36.36

21.98
2.70
23.81
28.07
47.25
28.73
3.26
35.64

22.89
2.67
18.11
27.19
45.24
25.87
5.76
37.08

25.85
1.47
17.15
19.14
34.77
7.52
4.71
27.79

29.69
3.33
12.66
27.57
45.99
23.52
4.78
38.22

0.90
10.49
2.88
2.07
55.86
37.03
15.50
45.18
22.74

1.47
14.64
3.97
2.61
61.23
19.00
53.11
28.64

0.04
0.07
2.29
1.93
0.10
1.48
0.81

1.02
11.67
3.53
2.57
65.66
43.49
13.04
51.58
29.82

0.84
11.34
2.37
1.81
47.11
34.57
14.62
43.21
21.79

1.98
9.43
2.57
1.59
58.17
46.36
13.26
43.87
23.96

1.54
14.43
1.74
3.43
61.65
46.49
16.32
42.50
29.58

1.19
5.15
1.59
1.19
48.60
18.09
7.92
35.23
16.39

12.64
3.31
2.33
56.76
38.45
16.39
47.67
25.87

1), and success-compliant (score of 2). The completion rate is then calculated as follows:
PT

t=1 st

Completion Rate (CR) =

,
(2)
T × smax
where the numerator was the sum of the completion scores for each step, and the denominator was
the sum of the maximum possible scores for all
steps (2 × T and T is the number of TFCs).
• Success Rate (SR). Similar to Codex (Chen
et al., 2021), our success rate is defined as the rate
of complete success on a single prompt estimated
under 10 runs. Specifically, if all the TFC in R
have passed within a run of a single prompt, it
will count as a success. Otherwise, it will count
as a failure. Note that for prompts acquired from
BigCodeBench, we compare the completion function’s outputs with the ground truth completion
function’s outputs to determine whether a single
run passes, since R is derived based on demanded
function outputs in this case. The formula for calculating SR is as follows:
#
Success Rate (SR) :=

E

Prompts

1−

n−c
k
k

, (3)

where n = 10 and k = 1 in our case, c denotes the
number of runs that have passed all TFCs in R.

Fine-grained Aggregate Metrics. We also define the fine-grained aggregate metrics for detail
evaluating all LLMs, as shown in Figure 3 and Table 4. It’s worth noting that data visualization is
one of the more challenging tasks. It confirms the
existence of outputs but also validates their accuracy and completeness. Specifically, for tasks like
data visualization, we focus on metrics such as visualization quality and use VLM-as-a-judge to assess the quality of images. Finally, we select six
representative aggregated metrics as follows:
• VLM-as-a-judge assesses the overall score of
two visual inputs based on predefined criteria for progressively adding scores (see Appendix A.10) to write the total score and provide a brief step-by-step reasoning explanation
for its evaluation, with GPT-4o-mini serving as
the VLM.
• Data Quality Score (F1) in Data cleaning and
preprocessing aims to assess the cleanliness of
data post-processing. It yields a boolean output
of 1 if it matches the ground truth or 0 otherwise.
• Plot Validity (F2) in Data visualization pertains
to the accuracy of visual representations, such
as checking whether the shape of an association
matrix is consistent with the ground truth. If

12.84
12.69

4.84
3.40
3.32
2.45

16.55

29.70
27.57
25.89
23.54

38.73

38.42
38.28

47.67
45.99

Different Difficulty Level for Data Science
easy
medium
hard

64.43
API Access

56.74

Open Access

Avg: 37.76

Avg: 3.83

Avg: 23.01

Avg: 6.56

o1

-m
in
G i
GP PT-4
T-4 o
o
GP -mi
T- ni
Cla 4-Tur
ud bo
GL -3-5
M Lla -4-F S
ma las
-3 h
Lla .1-8
m B
ge a-3 -I
mm -8B
GL a-2- -I
M- 9b
4- -i
Qw 9b-C t
en hat
2.
Qw 5-7B
en -I
Yi- Qwe 2-7B
1.5 n2 -I
-9 -1.
Co B-Ch 5B-I
de at
L Co lam 16K
de a-3
Ll 4
Co ama b-I
de -13
L
b
De Star lama -I
ep Co -7
De seek der2 b-I
ep -C -1
o
De seek der- 5b
ep -Co 33
see de b-I
k
Qw -Co r-6.7
e d b
Qw n2.5 er-1 -I
en -Co .3b
2.5 de -I
-Co r-7
de B-I
r-1
.5B
-I

30.75

Avg: 49.15
54.59
54.12
52.26

Ave. CR

gpt-4o
gpt-4-turbo
gpt-4o-mini
claude-3-5-s
GLM-4-flash
Deepseek-Coder-33b-I
Qwen2.5-Coder-7B-I
Qwen2.5-7B-I
Deepseek-Coder-6.7b-I
Llama-3.1-8B-I
GLM-4-9b-chat
Qwen2.5-Coder-1.5B-I
Qwen2-7B-I
Deepseek-Coder-1.3b-I
CodeLlama-13b-I
gemma-2-9b-it
Qwen2-1.5B-I
Llama-3-8B-I
CodeLlama-7b-I
StarCoder2-15b
CodeLlama-34b-I

Pass@1

Figure 4: Overall score results of all tested LLMs.

consistent, the final value is 1, otherwise 0.
• Data Accuracy (F3) in Data Exploration and
Statistics Understand focuses on understanding
data quality and can be quantified using Mean
Squared Error (MSE). The final value is derived
by comparing it against the ground truth with a
predefined threshold.
• Visualization Completeness (F4) in Data visualization evaluates the comprehensiveness of generated images (e.g., PNG, jpeg, PDF) by checking their existence compared to the ground truth.
A score of 1 is assigned if the files exist, and
0 otherwise. Note that we use VLM-as-a-judge
and F2 to assess the quality of generated images.
• Model Accuracy (F5) in Predictive modeling is
utilized to gauge the predictive performance of
models, providing a boolean accuracy value or
decimal ranging between 0 and 1.
Final Score. We calculate the final score through
the following definition:
Score = 0.05×

X

Fi +0.05×SVLM +0.05×SR+0.65×CR,

i=1

(4)

here, the final Score is computed by combining the
weighted sum of five metrics Fi (where i ranges
from 1 to 5), a value VLM score, a value SR, and
a value CR. Each factor is multiplied by its respective weight (0.05 or 0.65).

Results and Analysis

5.1

Overall Performance

We demonstrate overall experiment results in Table 2 and Figure 4. The key findings are: 1) Concerning average performance, API-based models outperform open-sourced models. Among
API-based models, GPT-4o achieves the highest total score of 64.51%, attaining a significant 9.86% advantage over GPT-4-Turbo, which
achieves 54.65% total score. GPT-4o also surpasses all other models on all metrics, indicat-

Model Name

Figure 5: Average Completion Rate results regarding
different difficulty levels.

ing its comprehensive capacity over various aspects. In comparison, the performance variance
between API-based models is smaller than that of
open-sourced models. 2) As for open-sourced
models, the performance gap between general models and code generation models is insignificant. Among those, Deepseek-Coder-33BInstruct achieves the highest score of 56.76%,
even outperforming various API-based models
like o1-mini and GPT-4-Turbo. Other models
like Qwen2.5-Coder-7B-Instruct and Qwen2.57B-Instruct also show fair good capability, attaining total scores of 47.67% and 45.99%, respectively. In contrast, a few models only pass very
few tasks, achieving total scores even lower than
5.0%. Of these, CodeLlama-34B-Instruct unexpectedly achieves a score of 1.33%, even lagging behind its small-scale version CodeLlama7B-Instruct. In this regard, we also present an
analysis of the anomaly in Section 5.4.
5.2

Study with Different Difficulty Levels

To evaluate multiple LLMs on their ability to
complete prompts of varying difficulty, we categorized tasks using BCB and data formatted
in CSV, human handwritten prompts, and data
science-related DL tasks as easy - 167, medium
- 30, and hard levels - 25, respectively. We assessed multiple LLMs by combining different difficulty levels, overall average CR, and the average CR for each difficulty level. From the Figure 5, it can be observed that: 1) Some LLMs,
like GPT-4o, GPT-4o-mini, GPT-4-Turbo, and
Deepseek-Coder-33B-Instruct, exhibit consistent
performance across all difficulty levels, indicating robustness. 2) Models such as GPT-4 series
and Deepseek-Coder-Instruct series are among the
top performers, scoring high average CRs, particularly excelling in complex, data-driven tasks defined as hard. 3) There are noticeable performance
disparities among general models and small-scale

Figure 6: Pass@1 comparison of all tested LLMs
between DataSciBench and HumanEval. Circle
markers denote the API-based models while others denote various open-sourced LLMs. The green dashed areas indicate the LLMs perform well on the two benchmarks and the orange solid areas indicate performances
of the two datasets are relatively mismatched.

models in terms of average metrics, such CR, with
some achieving lower scores overall, suggesting
that general models are less efficient or accurate in
data science tasks.
5.3

Comparison with HumanEval

We compare our proposed DataSciBench with
HumanEval. As shown in Figure 6, we observe
that most LLMs are located in the upper triangular
region of the graph and all tested models are divided into two groups, in which the green-dashedline areas where LLMs perform well on the two
benchmarks and the orange-solid-line area where
performances on the two datasets with the same
model indicate significant discrepancies.
5.4

Deeper Insights into LLMs’ Ability

With curated metrics, we can obtain deeper research insights into LLMs’ ability to plan and execute complex data science tasks. The experiment
results also raise questions that are worth exploring since some results do not conform to conventional perceptions.
Models demonstrate proficiency in reasoning
tasks but may not consistently excel in complex data science tasks that necessitate precise
adherence to detailed instructions, utilization
of existing tools, and strategic planning. Although, indeed, data science coding tasks often involve scheduling and step-by-step execution similar to reasoning scenarios, results show that even
the LLMs proficient in reasoning tasks can still
fail to complete complex data science tasks. For

instance, the o1-mini model, which is commonly
regarded as one of the best reasoning models, unexpectedly failed on many of DataSciBench’s
tasks. The model only achieves a 29.77% overall
success rate, significantly lagging behind the company’s previously introduced models like GPT-4o
and GPT-4-Turbo. After examining the completions generated by o1-mini, we discovered that the
failures are primarily caused by non-compliance
with instructions, incorrect calls, and forgetfulness. While successfully splitting the task into
multiple subtasks, the model often forgets to export required execution outcomes or just outputs
undesired data. In other cases, the model may
falsely call a library function or method that sometimes does not even exist. The main kind of coding
error is an execution error. An example is a hallucination about the column name of a CSV file.
These facts remind us that real-life data science
coding tasks often comprehensively challenge the
model’s ability to follow fine-grained instructions,
utilize existing tools (libraries, APIs. . .), and do
planning. To excel and align effectively with these
tasks, a model must demonstrate competitiveness
across all relevant aspects. We included four bad
examples generated by o1-mini for further clarification in Appendix B.2.
Larger-scale models may encounter challenges
in following simple instructions due to the extensive data utilized during training, potentially leading to difficulties in generating outputs in formats different from those within the
training data. StarCoder2-15B performs worse
than some smaller models, and CodeLlama-34BInstruct even performs worse than 13B and 7B versions. The main reason is that the larger-scale version lacks some other ability like generating formatted text according to prompts. Perhaps a large
amount of data in a certain format is being used to
train a larger version that fails to follow the prompt
to generate another format different from that. We
present some examples in Appendix B.2. Indeed,
the larger-scale model of CodeLlama also fails to
outperform the smaller-scale version in LCB.

Conclusion

This paper introduces DataSciBench, a novel
framework tailored to assess the capabilities of
LLMs in data science tasks. By meticulously curating challenging prompts and leveraging robust
LLMs alongside a self-consistency strategy, we

generate ground truth for all prompts. To efficiently evaluate LLMs’ performance, we aggregate evaluation metrics and synthesize the TFC
list programmatically. Subsequently, we assess 23
API-based and open-source models, offer valuable
research and engineering insights, and present error analyses of the assessed LLMs.

Limitations

In certain visualization tasks, our initial metrics
and evaluation methods (e.g., VLM-as-a-judge)
may lack precision. Further refinement of metrics is required to evaluate data visualization tasks
effectively. One potential approach could involve
employing VLMs to train critic models, enhancing the capability for fine-grained evaluations of
visualizations.

References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al. 2023. Gpt-4 technical report. arXiv preprint arXiv:2303.08774.
Bo Chen, Xingyi Cheng, Pan Li, Yangli-ao Geng,
Jing Gong, Shen Li, Zhilei Bei, Xu Tan, Boyan
Wang, Xin Zeng, et al. 2024a. xtrimopglm: unified 100b-scale pre-trained transformer for deciphering the language of protein. arXiv preprint
arXiv:2401.06199.

Xinyi He, Mengyu Zhou, Xinrun Xu, Xiaojun Ma,
Rui Ding, Lun Du, Yan Gao, Ran Jia, Xu Chen,
Shi Han, Zejian Yuan, and Dongmei Zhang. 2023.
Text2analysis: A benchmark of table question answering with advanced data analysis and unclear
queries.
Sirui Hong, Yizhang Lin, Bangbang Liu, Binhao Wu,
Danyang Li, Jiaqi Chen, Jiayi Zhang, Jinlin Wang,
Lingyao Zhang, Mingchen Zhuge, et al. 2024. Data
interpreter: An llm agent for data science. arXiv
preprint arXiv:2402.18679.
Xueyu Hu, Ziyu Zhao, Shuang Wei, Ziwei Chai, Qianli
Ma, Guoyin Wang, Xuwu Wang, Jing Su, Jingjing
Xu, Ming Zhu, et al. 2024. Infiagent-dabench: Evaluating agents on data analysis tasks. In Forty-first
International Conference on Machine Learning.
Qian Huang, Jian Vora, Percy Liang, and Jure
Leskovec. 2023. Benchmarking large language
models as ai research agents.
arXiv preprint
arXiv:2310.03302.
Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang,
Bowen Yu, Kai Dang, et al. 2024. Qwen2. 5-coder
technical report. arXiv preprint arXiv:2409.12186.
Aaron Hurst, Adam Lerer, Adam P Goucher, Adam
Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford,
et al. 2024. Gpt-4o system card. arXiv preprint
arXiv:2410.21276.
Aaron Jaech, Adam Kalai, Adam Lerer, Adam
Richardson, Ahmed El-Kishky, Aiden Low, Alec
Helyar, Aleksander Madry, Alex Beutel, Alex Carney, et al. 2024. Openai o1 system card. arXiv
preprint arXiv:2412.16720.

Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan,
Henrique Ponde De Oliveira Pinto, Jared Kaplan,
Harri Edwards, Yuri Burda, Nicholas Joseph, Greg
Brockman, et al. 2021. Evaluating large language models trained on code. arXiv preprint
arXiv:2107.03374.

Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando SolarLezama, Koushik Sen, and Ion Stoica. 2024. Livecodebench: Holistic and contamination free evaluation of large language models for code. arXiv
preprint arXiv:2403.07974.

Nan Chen, Yuge Zhang, Jiahang Xu, Kan Ren, and
Yuqing Yang. 2024b. Viseval: A benchmark for data
visualization in the era of large language models.
IEEE Transactions on Visualization and Computer
Graphics.

John Jumper, Richard Evans, Alexander Pritzel,
Tim Green, Michael Figurnov, Olaf Ronneberger,
Kathryn Tunyasuvunakool, Russ Bates, Augustin
Žídek, Anna Potapenko, et al. 2021. Highly accurate
protein structure prediction with alphafold. nature,
596(7873):583–589.

Team GLM, Aohan Zeng, Bin Xu, Bowen Wang,
Chenhui Zhang, Da Yin, Diego Rojas, Guanyu Feng,
Hanlin Zhao, Hanyu Lai, et al. 2024. Chatglm: A
family of large language models from glm-130b to
glm-4 all tools. arXiv preprint arXiv:2406.12793.

Yuhang Lai, Chengxi Li, Yiming Wang, Tianyi Zhang,
Ruiqi Zhong, Luke Zettlemoyer, Wen-tau Yih,
Daniel Fried, Sida Wang, and Tao Yu. 2023. Ds1000: A natural and reliable benchmark for data science code generation. In International Conference
on Machine Learning, pages 18319–18345. PMLR.

Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie,
Kai Dong, Wentao Zhang, Guanting Chen, Xiao
Bi, Yu Wu, YK Li, et al. 2024.
Deepseekcoder: When the large language model meets
programming–the rise of code intelligence. arXiv
preprint arXiv:2401.14196.

Hongxin Li, Jingran Su, Yuntao Chen, Qing Li,
and ZHAO-XIANG ZHANG. 2024. Sheetcopilot: Bringing software productivity to the next level
through large language models. Advances in Neural
Information Processing Systems, 36.

Anton Lozhkov, Raymond Li, Loubna Ben Allal, Federico Cassano, Joel Lamy-Poirier, Nouamane Tazi,
Ao Tang, Dmytro Pykhtar, Jiawei Liu, Yuxiang Wei,
et al. 2024. Starcoder 2 and the stack v2: The next
generation. arXiv preprint arXiv:2402.19173.

Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran, Karthik Narasimhan, and Yuan Cao. 2022.
React: Synergizing reasoning and acting in language
models. arXiv preprint arXiv:2210.03629.

Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foerster, Jeff Clune, and David Ha. 2024. The ai scientist: Towards fully automated open-ended scientific
discovery. arXiv preprint arXiv:2408.06292.

Alex Young, Bei Chen, Chao Li, Chengen Huang,
Ge Zhang, Guanwei Zhang, Heng Li, Jiangcheng
Zhu, Jianqun Chen, Jing Chang, et al. 2024. Yi:
Open foundation models by 01. ai. arXiv preprint
arXiv:2403.04652.

Pingchuan Ma, Rui Ding, Shuai Wang, Shi Han,
and Dongmei Zhang. 2023. Insightpilot: An llmempowered automated data exploration system. In
Proceedings of the 2023 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 346–352.

Dan Zhang, Ziniu Hu, Sining Zhoubian, Zhengxiao
Du, Kaiyu Yang, Zihan Wang, Yisong Yue, Yuxiao Dong, and Jie Tang. 2024a. Sciglm: Training scientific language models with self-reflective
instruction annotation and tuning. arXiv preprint
arXiv:2401.07950.

Baptiste Roziere, Jonas Gehring, Fabian Gloeckle, Sten
Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi,
Jingyu Liu, Romain Sauvestre, Tal Remez, et al.
2023. Code llama: Open foundation models for
code. arXiv preprint arXiv:2308.12950.

Dan Zhang, Sining Zhoubian, Yisong Yue, Yuxiao
Dong, and Jie Tang. 2024b. Rest-mcts*: Llm
self-training via process reward guided tree search.
arXiv preprint arXiv:2406.03816.

Gemini Team, Rohan Anil, Sebastian Borgeaud,
Yonghui Wu, Jean-Baptiste Alayrac, Jiahui Yu,
Radu Soricut, Johan Schalkwyk, Andrew M Dai,
Anja Hauth, et al. 2023. Gemini: a family of
highly capable multimodal models. arXiv preprint
arXiv:2312.11805.
Gemma Team, Thomas Mesnard, Cassidy Hardin,
Robert Dadashi, Surya Bhupatiraju, Shreya Pathak,
Laurent Sifre, Morgane Rivière, Mihir Sanjay Kale,
Juliette Love, et al. 2024. Gemma: Open models
based on gemini research and technology. arXiv
preprint arXiv:2403.08295.
Wei Wang, Dan Zhang, Tao Feng, Boyan Wang, and
Jie Tang. 2024. Battleagentbench: A benchmark for
evaluating cooperation and competition capabilities
of language models in multi-agent systems. arXiv
preprint arXiv:2408.15971.
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc
Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. 2022. Self-consistency improves chain of thought reasoning in language models. arXiv preprint arXiv:2203.11171.
Xiao Xia, Dan Zhang, Zibo Liao, Zhenyu Hou, Tianrui
Sun, Jing Li, Ling Fu, and Yuxiao Dong. 2024. Scenegenagent: Precise industrial scene generation with
coding agent. arXiv preprint arXiv:2410.21909.
Yifan Xu, Xiao Liu, Xueqiao Sun, Siyi Cheng, Hao
Yu, Hanyu Lai, Shudan Zhang, Dan Zhang, Jie Tang,
and Yuxiao Dong. 2024. Androidlab: Training and
systematic benchmarking of android autonomous
agents. arXiv preprint arXiv:2410.24024.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan
Li, Dayiheng Liu, Fei Huang, et al. 2024. Qwen2
technical report. arXiv preprint arXiv:2407.10671.

Shudan Zhang, Hanlin Zhao, Xiao Liu, Qinkai Zheng,
Zehan Qi, Xiaotao Gu, Xiaohan Zhang, Yuxiao
Dong, and Jie Tang. 2024c. Naturalcodebench:
Examining coding performance mismatch on humaneval and natural user prompts. arXiv preprint
arXiv:2405.04520.
Wenqi Zhang, Yongliang Shen, Weiming Lu, and Yueting Zhuang. 2024d. Data-copilot: Bridging billions
of data and humans with autonomous workflow. In
ICLR 2024 Workshop on Large Language Model
(LLM) Agents.
Qinkai Zheng, Xiao Xia, Xu Zou, Yuxiao Dong, Shan
Wang, Yufei Xue, Zihan Wang, Lei Shen, Andi
Wang, Yang Li, et al. 2023. Codegeex: A pretrained model for code generation with multilingual evaluations on humaneval-x. arXiv preprint
arXiv:2303.17568.
Terry Yue Zhuo, Minh Chien Vu, Jenny Chim, Han Hu,
Wenhao Yu, Ratnadira Widyasari, Imam Nur Bani
Yusuf, Haolan Zhan, Junda He, Indraneil Paul, et al.
2024. Bigcodebench: Benchmarking code generation with diverse function calls and complex instructions. arXiv preprint arXiv:2406.15877.

A

Appendix

A.1

Task Definition

We define six typical data science tasks as follows:
1) Data cleaning and preprocessing. This task
detects and processes missing values, outliers, and
duplicate data; and standardizes data formats, such
as a uniform format for dates and times.
2) Data exploration and statistics understanding. This task calculates basic statistical indicators of data (mean, median, standard deviation, etc.), generates data distribution charts (histograms, box plots, etc.), calculates correlations
between variables, and draws correlation matrices
or maps.
3) Data visualization. The goal of this task is
to visualize and analyze data and create interactive
charts so users can freely explore the data.
4) Predictive modeling. The task aims to select
the appropriate machine learning algorithm, such
as linear regression, decision tree, random forest,
etc.; carry out feature engineering, such as feature
selection, feature transformation, feature combination, etc.; the data set is divided into the training set and test set, and the model is trained and
evaluated; and select the corresponding evaluation
indicators for different prediction problems, such
as classification, regression or clustering.
5) Data mining and Pattern recognition. This
task uses association rule mining, frequent item set
mining, and other methods to find interesting patterns in the data; Text mining technology is used
to extract keywords, topics, and other information
from text data; and apply cluster analysis, classification algorithms, etc. to identify underlying patterns and structures. Pattern recognition tasks can
conduct these functions: image recognition, text
clustering, and time series detection.
6) Interpretability and Report generation.
This task aims to provide explanations of model
results, such as feature importance, model parameters, etc., and automatically generate reports and
summaries that present the results of the analysis
in a way that is easy to understand and share.
A.2

Comparison with Existing Benchmarks

We perform correlation analysis to evaluate the
alignment between DataSciBench and coding
evaluations like BCB and LCB. To achieve correlation analysis, we calculate both Pearson’s r and
Spearman’s p correlation coefficients, which provide insights into the strength and direction of re-

Table 3: Correlation with LCB and BCB.

LiveCodeBench (LCB)
BigCodeBench (BCB)

r

p

0.853
0.823

0.673
0.808

lationships between our benchmark and these established metrics. This analysis not only validates
our results but also ensures robustness across different evaluation dimensions. Our findings indicate strong positive correlations, suggesting that
our benchmark aligns well with these established
coding evaluation metrics.
While DataSciBench does show a correlation with LCB or BCB in Table 3, our benchmark
offers several unique and important contributions:
• Domain-Specific Focus: DataSciBench
specifically targets data science and analytics
tasks. However, existing benchmarks primarily
focus on general programming problems. This
specialization helps evaluate models’ capabilities in handling real-world data analysis scenarios.
• Task Diversity: Our DataSciBench includes
unique task types like data preprocessing, visualization, and statistical analysis. These tasks
are underrepresented in current benchmarks.
This provides deeper insights into models’ data
science-specific capabilities.
• Complementary Insights: While overall correlations exist, we observe meaningful differences in model rankings. For example, models
like Meta-Llama-3-8B-Instruct and CodeLlama34B-Instruct show distinct performance patterns. These differences highlight capabilities
specific to data science tasks that other benchmarks may not capture.
The correlation with existing benchmarks validates our evaluation methodology, while our
domain-specific focus provides valuable new insights for assessing AI models in data science applications.
A.3

Motivation and Example of
Task-Function-Code (TFC)

The TFC framework was developed to address
several critical challenges in automated evaluation
of data science tasks:

Prompt: Complete the code writing task in Python: Create a stacked bar chart of the Types attribute versus other
attributes based on the data.csv dataset. The dataset is the result of a chemical analysis of wines from the same region in
Italy. Store the results in processed_data.csv. Each sample in the dataset contains 14 attributes, which are: Alcohol,
Malic_Acid, Ash, Ash_Alcanity, Magnesium, Total_Phenols, Flavanoids, Nonflavanoid_Phenols, Proanthocyanins,
Color_Intensity, Hue, OD280, Proline, and Types. Save the stacked bar chart as `stacked_bar_chart.png`.

Data cleaning and
preprocessing

Data Completeness

def data_completeness(ground_truth):
output = pd.read_csv(ground_truth)
prediction = pd.read_csv(“processed_data.csv”)
total_cells = output.size
non_null_cells = output.count().sum()
pre_total_cells = prediction.size
pre_non_null_cells = prediction.count().sum()
return bool(non_null_cells / total_cells ==
pre_non_null_cells / pre_total_cells )

T1

C1

Figure 7: An example of TFC tuples.

• Systematic Task Selection: TFC provides a
structured approach to identify and categorize
key tasks across six established types. This
systematic organization ensures comprehensive
coverage of essential data science operations
and helps maintain evaluation consistency and
completeness.
• Standardized Evaluation Metrics: Data science tasks often lack standardized evaluation
criteria. TFC addresses this by explicitly defining appropriate evaluation functions for each
task. For example, data preprocessing tasks require specific metrics that differ from visualization tasks. This standardization ensures fair and
consistent assessment.
• Automated Execution Framework: TFC includes executable code components for both
tasks and evaluation metrics. This automation
significantly improves evaluation efficiency, result reproducibility, and testing scalability.
• Ground Truth Generation: TFC serves as a
crucial foundation for establishing ground truth,
particularly valuable for complex tasks where
ground truth is not readily available, and enables
systematic verification and validation of model
outputs.
Overall, the TFC structure in Figure 7 represents a
novel contribution by providing a comprehensive
framework that bridges the gap between task definition, evaluation criteria, and automated assessment in data science contexts.
A.4

Programmatic Rules

We list all programmatic rules in Table 4.
A.5

Caveats when Using LLMs for Data

Here we list the issues that occurred during testcase generation, most of which have been addressed by modifying the prompts. We notice that
some of the issues may be disruptive to the system

and some may be subtle but important.
1. Be careful when using LLMs on well-known
open source datasets, especially with customized tasks and data split. LLMs may
memorize some open-source datasets. For
example, if we want to use part of the penguin
dataset that does not contain certain columns,
the model (GPT-4o) will still explicitly process those columns in the code.
2. Hallucination during data pre-processing.
For example, when the model is required
to merge two CSV, it may hallucinate on a
common column and not go through all the
columns in the files to find the actual ones.
3. On multilingual tasks. LLMs may not be able
to select the correct encoding. For instance,
when they are required to open a CSV file
that has content in Chinese, they will struggle to choose the correct encoding to open
the file. Even if they are hinted that the file is
in Chinese, they may choose encodings other
than “gbk”, e.g., “latin”.
A.6

Related Works

A.6.1 LLMs for Data Science
With the popularity of large-scale language models, researchers have developed a series of LLMbased agents (Yao et al., 2022; Wang et al., 2024;
Xu et al., 2024; Xia et al., 2024). For data science,
SheetCopilot (Li et al., 2024) designs a tabular
agent, which directly processes natural languagedescribed tasks, and generates and executes a series of operation plans on datasheets to produce
the desired results. Data Copilot (Zhang et al.,
2024d) is an intelligent agent that serves as a
bridge between users and data, which automatically executes data processing, prediction, and visualization tasks based on users’ data needs. InsightPilot (Ma et al., 2023) focuses on exploratory
data analysis and can automatically discover data
insights related to fuzzy questions raised by users.
Data interpreter (Hong et al., 2024) augments
problem-solving in data science with dynamic
planning with hierarchical graph structures, tool
integration, and logical inconsistency identification in feedback. Furthermore, ReAct (Yao et al.,
2022) is quite similar to our backbone agentic
framework, DataInterpreter. Both frameworks offer foundational pipelines rather than specific evaluation metrics tailored for diverse data science

Table 4: Details of programmatic rules.
Aggregate Function

Task

Type

Rule

Comparison

GT

Threshold

Mean Squared Error
Data Cleaning Completeness
Silhouette Score
Model Accuracy
Model Accuracy
R-squared Value
Data Cleaning Completeness
Data Quality Score
Data Accuracy
Data Completeness
Data Quality Score
Association Rule Confidence

Calculate MSE
row/column number
Calculate
Calculate F1
Calculate Accuracy
Calculate
number of nulls
number of outlier
MSE
Null number ratio
Calculate loss
Association rule accuracy

It ≤ to GT is 1, it > GT is 0
If it == 0, returns 1; if it > 0, returns 0
Threshold judgment
It ≤ to GT is 1, it > GT is 0
Threshold judgment

0.5
0.05

tasks. However, the correctness of data analysis in
data science has a significant impact on decisionmaking. Therefore, with the continuous increase
of data science agents, it is urgent to conduct a
comprehensive and in-depth evaluation of data science agents.
A.6.2

LLM Agent Evaluation Benchmarks
for Data Science

Assessing the effectiveness of LLMs in handling
diverse and challenging data science prompts is
essential to push the boundaries of benchmarking
practices in the field of data science and LLM research. Data science agents often solve problems
by generating code, so the capabilities of data science agents are closely related to the code generation capabilities of large models. There are already
many benchmarks for evaluating the code capability of large models. MLAgentBench (Huang
et al., 2023) benchmarks the LLMs’ abilities
on traditional machine learning tasks. NaturalCodeBench (Zhang et al., 2024c) evaluates the capabilities of code generation models on the real
prompts from the CodeGeeX (Zheng et al., 2023)
platform. However, the general code evaluation
benchmark ignores the characteristics of data science tasks and cannot comprehensively and effectively evaluate the capabilities of large models in
data science.
Recently, some evaluation benchmarks for large
language models in data science have been proposed. Text2Analysis (He et al., 2023) constructs
the evaluation benchmark to evaluate the model’s
ability to handle data analysis functions and fuzzy
questions on tabular data. Their prompts are obtained through manual annotation and large model
generation. Furthermore, DAEval (Hu et al.,
2024) is developed as another evaluation benchmark and it contains 257 data analysis questions

on CSV data and questions, which are generated by LLMs. However, the prompts in these
two works often only involve one task, and these
prompts involve relatively simple data analysis operations. In practical data science analysis tasks,
user questions often involve multiple tasks and
involve performing complex data analysis operations. Therefore, we aim to provide a data science
evaluation benchmark that is more in line with
practical scenarios, especially for problems involving multiple subtasks and complex data analysis operations.

A.7

Related Work in Data Science

Recently, some evaluation benchmarks for large
language models in data science have been proposed. Text2Analysis (He et al., 2023) constructs
the evaluation benchmark to evaluate the model’s
ability to handle data analysis functions and fuzzy
questions on tabular data. Their prompts are obtained through manual annotation and large model
generation. Furthermore, DAEval (Hu et al.,
2024) is developed as another evaluation benchmark and it contains 257 data analysis questions
on CSV data and questions, which are generated by LLMs. However, the prompts in these
two works often only involve one task, and these
prompts involve relatively simple data analysis operations. In practical data science analysis tasks,
user questions often involve multiple tasks and
involve performing complex data analysis operations. Therefore, we aim to provide a data science
evaluation benchmark that is more in line with
practical scenarios, especially for problems involving multiple subtasks and complex data analysis operations.

A.8

Results

We present the detailed results for our collected
prompt and BigCodeBench source in Table 5 and
Table 6.
A.9

AI Assistants In Writing

While writing this paper, we employed AI to rectify grammatical errors and revise unreasonable
descriptions.
A.10

VLM-as-a-judge Prompt and Examples

In this section, we define the criteria to measure
the quality of LLM-generated figures/charts.

Table 5: Evaluation results for DataSciBench (our collected prompts).

Success (%)

VLM

13.45
19.82
12.73
17.27
8.00
9.82

15.43
17.89
17.35
17.36
11.12
7.43

2.87
3.91
3.05
3.09
2.14

53.75
71.79
62.86
65.18
32.32
47.14

15.00
10.00

45.50
54.50
50.50
44.50
36.00
22.00

46.25
70.00
69.38
78.12
63.12
24.38

25.79
33.95
43.68
41.05
17.63
3.95

19.41
24.32
24.13
24.24
15.19
10.26

10.00
1.64
5.64
10.55
11.64
6.91
1.82

7.72
5.51
9.96
10.11
5.90
1.60
4.25

1.29
0.52
1.06
1.69
1.16
0.40

45.18
7.86
26.79
55.36
55.36
32.50
3.57
30.36

16.00
4.50
13.00
31.00
36.50
18.00
2.00
16.00

23.12
6.88
22.50
28.75
33.12
21.88
13.12
8.75

8.95
2.89
21.32
18.42
2.37
0.79
3.95

10.24
2.00
7.18
13.91
14.40
7.97
2.13
6.06

0.55
0.18
12.55
12.55

0.03
0.50
0.27
0.20
13.53
13.56
0.61
7.87
7.52

0.04
0.07
2.29
1.93
0.10
1.48
0.81

4.46
1.96
0.54
62.86
63.21
3.39
40.18
38.57

43.00
39.00
27.50
15.50

3.75
0.62
51.88
53.75
1.25
33.75
40.00

21.32
21.05
4.47
10.53

0.02
0.77
0.30
0.20
18.49
18.39
0.67
10.79
10.46

Table 6: Evaluation results for DataSciBench (BigCodeBench source).

Success (%)

35.15
81.62
63.11
63.35
60.48
37.07

55.08
85.09
71.10
72.54
73.59
42.8

77.30
59.46
61.35
54.59
33.04

25.62
74.63
58.89
52.04
49.11
39.11

32.89
74.21
60.26
62.11
62.37
36.05

25.90
71.79
55.90
54.36
49.49
28.72

23.16
65.48
56.79
53.95
55.39
17.89

47.77
81.81
67.49
68.14
68.08
39.55

29.58
3.29
7.54
30.72
54.43
28.08
4.67
48.74

42.51
4.74
12.81
37.11
64.12
32.06
6.73
54.9

35.95
2.97
25.95
23.65
49.80
30.41
4.86
40.70

24.26
1.67
22.46
30.78
48.40
27.63
2.63
48.34

23.95
27.37
27.11
50.79
32.26
3.68
42.11

22.82
1.28
16.67
26.67
49.23
27.18
3.33
46.41

31.41
1.96
21.84
18.42
40.15
9.21
6.00
35.64

38.16
3.98
15.06
33.84
59.52
30.18
5.97
51.53

1.20
13.71
3.65
2.69
70.12
45.09
20.36
58.02
28.20

1.94
19.3
5.19
3.41
76.94
50.86
25.05
68.01
35.60

1.35
14.05
4.05
3.24
66.58
37.00
16.22
55.34
26.94

1.11
15.07
3.15
2.41
62.63
45.96
19.44
57.44
28.96

2.63
12.53
3.42
63.16
48.79
17.63
49.26
26.74

2.05
17.95
2.31
4.36
64.87
44.10
21.28
45.38
26.15

1.58
6.84
1.58
57.59
17.11
10.53
45.36
18.32

1.85
17.52
4.57
3.21
73.11
47.50
22.81
63.15
32.69

Prompt for VLM-as-a-judge
Above are two figures, which are A and B. The first figure is the ground truth image and the second
figure is the predicted image. The total score is 5. Please score B following the criteria below:
- add 1 point for Data Representation Consistency: Ensure that the underlying data represented by
the two charts is identical. This includes the values for all data points and the range of the data. Any
variation in the dataset used would make the charts different.
- add 1 point for Axis Labels and Scales: Verify that both charts have identical axis labels, units, and
scales. Any difference in how the axes are labeled or scaled, such as using logarithmic vs. linear scales,
can affect the interpretation of the data.
- add 1 point for Graphical Elements: Check if the visual elements (such as lines, bars, markers, etc.) are
represented the same way in both charts. Line thickness, marker styles, and colors should match across
charts for them to be considered visually equal.
- add 1 point for Legend and Annotations: Confirm that any legends, titles, or annotations (e.g., text
labels, arrows, or highlights) are the same in both charts. These elements often provide crucial context
for interpreting the chart.
- add 1 point for Chart Dimensions and Layout: Ensure that the dimensions (height and width), aspect
ratios, and layout of the charts are identical. Even if the content and representation are similar, a different aspect ratio or spacing between elements can change the chart’s overall appearance and interpretation.
Please write down the total score for B based on the criteria above, and provide a brief explanation of your reasoning. If you believe that the two figures are not identical, please explain the differences
you observed.
your explanation here
x/5

Example #1 of VLM-as-a-judge (Model: Claude-3-5-sonnet-20240620)

[Prompt for VLM-as-a-judge]
1. **Data Representation Consistency**: Both charts represent the same underlying data for the years
2022 and 2023, with sales figures of $4,800 for 2022 and $7,800 for 2023. **+1 point**.
2. **Axis Labels and Scales**: Both charts have identical X-axis labels (years) and Y-axis labels (total sales). They both use the same scale on the Y-axis, ranging from 0 to 8000. **+1 point**.
3. **Graphical Elements**: The bars in both charts are red with the same thickness. Thus, the
visual representation matches. **+1 point**.
4. **Legend and Annotations**: The second chart includes dollar amounts on each bar, which
isn’t present in the first chart. This difference impacts the context provided for interpreting the chart,
reducing consistency. **0 points**.
5. **Chart Dimensions and Layout**: Both charts appear similar in terms of layout and dimensions, with no significant visual differences observed. **+1 point**.
Given the above evaluations, the total score for B is calculated as follows:
4/5

Example #2 of VLM-as-a-judge (Model: CodeLlama-13B-Instruct)

[Prompt for VLM-as-a-judge]
1. **Data Representation Consistency**: Both figures (A and B) represent the same underlying data
with identical values for categories A, B, C, and D. Therefore, 1 point is awarded.
2. **Axis Labels and Scales**: The axis labels ("Category" for the x-axis and "Values" for the y-axis)
appear to be identical in both images, and the scale for the y-axis seems consistent. Thus, 1 point is
awarded.
3. **Graphical Elements**: Both charts use blue bars to represent the data, and the thickness and style
of the bars are similar. Therefore, 1 point is awarded.
4. **Legend and Annotations**: There are no legends or additional annotations in either image, and the
titles are the same ("Bar Chart"). Thus, 1 point is awarded.
5. **Chart Dimensions and Layout**: The dimensions and overall layout of the two charts differ. Image
A has a different aspect ratio compared to Image B, which affects the total layout. Hence, 0 points are
awarded.
4/5

Example #3 of VLM-as-a-judge (Model: o1-mini)

Explanation:
1. Data Representation Consistency: Image A represents true values compared to predictions
over a broader date range, while Image B only shows predicted values for a specific date range
(2023-06-01 to 2023-07-19). The data sets are not identical. (Score: 0)
2. Axis Labels and Scales: Both images have similar axis labels ("Date" for x-axis, "Value1"
for y-axis), but Image B lacks clarity on the date range. Image A provides a wider range, with
different intervals. Scales are inconsistent. (Score: 0)

Explanation (cont.):
3. Graphical Elements: Image A uses a dashed red line for predictions, while Image B uses a
solid blue line. This difference affects visual representation. (Score: 0)
4. Legend and Annotations: Image A includes a detailed legend, while Image B only identifies
the predicted values. Titles are also different, affecting context and interpretability. (Score: 0)
5. Chart Dimensions and Layout: Image A has a wider aspect ratio for a broader date range,
while Image B is more condensed. (Score: 0)
Total Score: 0/5

A.11

Qualified Prompts

• Original Prompt 1:
There is a dataset with missing values in a
CSV file, which records the region, height,
weight, age, and salary of 36 individuals.
Please address the following issues:
(a) Calculate the proportion of missing values
in each column and select the rows with at
least two non-missing values in the last three
columns.
(b) Please fill in the weight column reasonably by combining the data from the height
and region columns.

of categorical variables. Use scatter plots and
heatmaps to visualize relationships and correlations between features. Identify patterns in
the data related to terrorist activities. For instance, determine trends over time, geographical hotspots, and common attack methods.
Use clustering techniques ( K-means clustering) to identify patterns and group similar incidents together.

• Qualified Prompt 1:
Qualified Prompt 1:
Given a dataset with missing values
in a file named ’data.csv’which
records the region, height, weight,
age, and salary of 36 individuals,
please address the following issues:
(a) Calculate the proportion of missing values in each column and select
the rows with at least two non-missing
values in the last three columns. Save
your output in a CSV file named
’missing_values_proportion
.csv’.
(b) Fill in the weight column reasonably by combining the data from the
height and region columns. Save this
updated dataset in a CSV file named
’updated_data.csv’.
• Original Prompt 2: You are required to
analyze and visualize the "Global Terrorism
Database" from Kaggle. Please load the
dataset and perform data cleaning by handling missing values, removing duplicates,
and correcting any anomalies. Conduct an
exploratory data analysis (EDA) to understand the distribution and relationships within
the dataset. Calculate basic statistical indicators such as mean, median, standard deviation, and provide summary statistics for key
features like attack type, target type, and region. Generate visualizations to uncover patterns and insights. Create histograms and box
plots to display the distribution of numerical
features, and bar plots to show the frequency

• Qualified Prompt 2:

Qualified Prompt 2:
You are required to analyze and visualize the Global Terrorism Database from Kaggle. Please follow
the steps below:
1. Load the dataset
Input: gtd.csv
Output: loaded_data.csv (This should contain the original data loaded without any modifications.)
2. Data Cleaning
– Handle missing values
– Remove duplicates
– Correct anomalies
Input: loaded_data.csv
Output: cleaned_data.csv (This should reflect the cleaned dataset, ready for analysis.)
3. Exploratory Data Analysis (EDA)
– Calculate basic statistical indicators such as mean, median, and standard deviation
– Provide summary statistics for key features (attack type, target type, region)
Output: eda_summary_statistics.csv (This should include all calculated statistics for key
features.)
4. Generate Visualizations
– Create histograms and box plots for numerical features
– Generate bar plots for categorical variables
– Use scatter plots and heatmaps to visualize relationships and correlations
Output: visualizations.pdf (This should include all visualizations generated in a single
PDF file.)
5. Identify Patterns in Data Related to Terrorist Activities
– Determine trends over time
– Identify geographical hotspots
– Analyze common attack methods
Output: patterns_analysis.csv (This should summarize the identified patterns, trends, and
hotspots.)
6. Clustering Techniques
– Use K-means clustering to identify patterns and group similar incidents
Output: clustering_results.csv (This should include the results of the clustering analysis,
showing which group each incident belongs to.)
Ensure that each output file reflects the quality of the completion of the respective subtask for further
evaluation.

A.12

Modified Prompts

• Original Prompt 1:
Searches a directory for CSV files matching a given regular expression pattern, reads sales data from
these files, and plots the sales data with month on the x-axis and sales on the y-axis.
Note that: Each CSV file contains two columns: Month and Sales.
The function should output with:
A list of matplotlib.axes._axes.Axes objects, each representing a plot of sales data from a
matched CSV file.
import os
import re
def task_func(directory: str, pattern: str) -> list:
• Modified Prompt 1:

Search a directory for CSV files matching a given regular expression pattern, read sales data from these
files, and plot the sales data with month on the x-axis and sales on the y-axis.
Input Requirements:
– Input Directory: data.
– Input Pattern: "csv_\d+\.csv".
Output Requirements:
1. A list of matplotlib.axes._axes.Axes objects representing the plot of sales data from each
matched CSV file.
2. Save each plot as a separate image file:
– File format: PNG
– Output filenames: "sales_plot_<filename>.png" where <filename> is the name
of the CSV file without the extension.
Input File Specification:
– Each CSV file should contain two columns: ’Month’ and ’Sales’. The input files will be
located in the specified directory.
import os
import re
def task_func(directory: str, pattern: str) -> list:

• Original Prompt 2:
Plot a scatter graph of tuples and highlight the tuple with the maximum value at index 1.
The function should output with:
matplotlib.axes.Axes: The Axes object of the plot for further manipulation and testing, with the
title ’Max Tuple Highlighted’, x-axis labeled ’x’, y-axis labeled ’y’, and a legend.
from operator import itemgetter
def task_func(data):

• Modified Prompt 2:
Modified Prompt 2:
Plot a scatter graph of tuples and highlight the tuple with the maximum value at index 1 using the input
data from "data.csv". The function should output the following:
A scatter plot saved as "scatter_plot.png" with the title ’Max Tuple Highlighted’,
x-axis labeled ’x’, y-axis labeled ’y’, and a legend. The highlighted point should signify the tuple
with the maximum value at index 1.
Please write self-contained code starting with:
from operator import itemgetter
def task_func(data):

A.13

Prompt examples of different difficulty levels

Easy-level Prompt #1:
"prompt": "Read the dataset (input file: "Fish.csv"). Encode the dataset to divide it into training
and test sets. From the dataset’s four categories of Bream, Roach, Parkki, and Perch, randomly select
2 samples from each category for the test set. The remaining samples will be used as the training
set. Output the number of samples in the training and test sets in a CSV file named "sample_counts.csv".
Next, implement the KNN algorithm with K values of 1, 5, 15, and 100 to classify all samples in the test set. Output the classification results of the test samples to a CSV file named
"classification_results.csv".",
"data_source_type": "2=open source data"

Easy-level Prompt #2:
"prompt": "Using the dataset of house prices and economic indicators provided below, please
complete the following subtasks. Each subtask should generate an output file for evaluation, with
specific input files where applicable.
Dataset: "data.csv"
Subtasks:
1. Gaussian Naive Bayes Training: Train a Gaussian Naive Bayes model on the cleaned dataset
and evaluate its accuracy.
Input: "data.csv"
Output: "gaussian_model_accuracy.csv" (contains accuracy metrics)
2. Multinomial Naive Bayes Training: Train a Multinomial Naive Bayes model on the cleaned
dataset and evaluate its accuracy.
Input: "data.csv"
Output: ‘multinomial_model_accuracy.csv‘ (contains accuracy metrics)
3. Comparison of Models: Generate a comparative analysis of the accuracy of both models in a
visual format.
Input: "gaussian_model_accuracy.csv", "multinomial_model_accuracy.csv"
Output: "model_comparison.png"
Please ensure that the outputs contain necessary details for further evaluation.",
"data_source_type": "3=human written data"

Medium-level Prompt:
"prompt": "Given a DataFrame ’df’ with sales data containing columns: TransactionID, ProductID, Quantity, SaleDate, StoreID, Revenue:
1. Handle missing Revenue values: Impute any missing Revenue values with the median of the
Revenue column.
Input file: ’data.csv’
Output: ’step1_imputed_revenue.csv’ (contains the DataFrame after handling missing values)
2. Detect and replace outliers: Detect and replace outliers in Quantity and Revenue. Outliers are
defined as values below the 1st percentile or above the 99th percentile. Replace them with the
corresponding 1st or 99th percentile value instead of removing them.
Input file: ’step1_imputed_revenue.csv’
Output: ’step2_replaced_outliers.csv’ (contains the DataFrame after outlier replacement)
3. Normalize Quantity and Revenue: Normalize Quantity and Revenue using Z-score normalization.
Input file: ’step2_replaced_outliers.csv’
Output: ’step3_normalized_data.csv’ (contains the DataFrame after normalization)
4. Ensure SaleDate format: Ensure SaleDate is in datetime format.
Input file: ’step3_normalized_data.csv’
Output: ’step4_formatted_dates.csv’ (contains the DataFrame after ensuring datetime
format)
5. Encode ProductID and StoreID: Encode the ProductID and StoreID columns using separate
label encoders to avoid any potential overlap in numerical values between categories from different
columns.
Input file: ’step4_formatted_dates.csv’
Output: ’final_cleaned_data.csv’ (contains the final cleaned DataFrame)
Perform the specified data cleaning and preprocessing tasks and output the cleaned DataFrame as
the final result.",
"data_source_type": "3=human written data"

Hard-level Prompt:
{ "prompt": "Write a Graph Recurrent Neural Network (GRNN) model based on attention mechanisms using Python for processing and analyzing time series data. Ensure to meet the following
requirements:
1. "Graph network design": Create a graph network where each graph represents an aerial formation, and the number of nodes corresponds to the number of vehicles in the formation.
- "Output": Graph structure representation file.
- "Output filename": "graph_structure.json"
2. "Data format": The time series data of aerial target formations is stored in Excel files located
in the ".data/" directory, where each Excel file contains multiple sheets, with each sheet representing
the time series data of a vehicle.
- "Input": Excel files from "..data/" directory.
- "Input filename": from "data_1.xlsx" to "data_5.xlsx"
3. "Data reading": Read all Excel files from the "..data/" directory and extract the sheets for
processing.
- "Output": Combined time series data in a structured format.
- "Output filename": "combined_data.csv"
4. "Data segmentation": Segment the time series data of each vehicle using a sliding window
with length "l" and step size "s".
- "Output": Segmented time series data.
- "Output filename": "segmented_data.csv"
5. "Training and testing set division": Divide the segmented data into training and testing sets
with a 7:3 ratio.
- "Output": Training and testing datasets.
- "Output filenames": "train_data.csv", "test_data.csv"
6. "Labels": The last column of each Excel file contains label data, which should be preserved
during the reading and segmentation process.
7. "Model training": Train the GRNN model using the training set to identify the action intentions of aerial target formations.
- "Output": Trained model file.
- "Output filename": "trained_model.h5"
8. "Training parameters": Set the number of training epochs to 60, and record the loss value,
accuracy, recall, and F1-Score for each epoch.
- "Output": Training metrics log file.
- "Output filename": "training_metrics.csv"
9. "Model evaluation": Evaluate the trained model with the test set and generate a classification
report and confusion matrix.
- "Output": Classification report and confusion matrix visualization.
- "Output filenames": "classification_report.txt", "confusion_matrix.png"
Please provide a complete code implementation and ensure that the code structure is clear and
well-commented for understanding and evaluation.",
"data_source_type": "3=human written data"}

B

Error Analysis and Case Study

We have analyzed the common errors during
problem-solving, summarized them here, and then
studied several cases, including a successful case
and a failure case. The common errors include:
1. Coding errors when solving data science
problems using codes. And based on our observation, the main kind of these is execution
error. It may be due to different reasons. For
example, hallucination on the column name
of a csv file.
2. Json format errors.
These errors come
from the agent framework side, where they
use json format to wrap up actions, e.g.
WriteAnalysis.
B.1

Successful cases

Successful case #1 from Claude-3-5-sonnet-20240620
Prompt: You are given a list of tickers and their daily closing prices for a given period stored in an
input file named "data.csv". Implement the most_corr function that, when given the daily closing prices,
returns the pair of tickers that are the most highly (linearly) correlated by daily percentage change. The
function should follow these specifications:
1. **Input File**: "../data.csv" - A CSV file containing a dataframe with columns representing
each ticker’s daily closing prices.
2. **Output Requirements**: The function should generate the following output:
- **Output Format**: A CSV file.
- **Output Filename**: "most_corr_output.csv" - This file should contain two columns labeled "Ticker
1" and "Ticker 2", representing the pair of tickers that are most correlated by daily percentage change.
Here’s the starter code for your implementation:
‘‘‘python
def most\_corr(prices):
:param prices: (pandas.DataFrame) A dataframe containing
each ticker’s daily closing prices.
:returns: (container of strings) A container, containing
the two tickers that are the most highly (linearly)
correlated by daily percentage change.
return None
# For example, the code below should print: (’FB’, ’MSFT’)
print(most_corr(pd.DataFrame.from_dict({
’GOOG’ : [
742.66, 738.40, 738.22, 741.16,
739.98, 747.28, 746.22, 741.80,
745.33, 741.29, 742.83, 750.50
],
’FB’ : [
108.40, 107.92, 109.64, 112.22,
109.57, 113.82, 114.03, 112.24,
114.68, 112.92, 113.28, 115.40
],
...
[omitted]
})))
‘‘‘

Successful case #2 from Claude-3-5-sonnet-20240620
Output: The following example successfully fulfills the requirement of the given prompt by completing
the function provided in the prompt and write the function to most_corr_output.csv.
[
’task_id’: ’1’,
’dependent_task_ids’: [],
’instruction’: "Load and preprocess the input data from
’data.csv’",
’task_type’: ’preprocessing and cleaning’,
# Load the data from ’data.csv’
prices = pd.read_csv(’../data.csv’)
# Set the first column (assuming it’s a date column) as
the index
prices.set_index(prices.columns[0], inplace=True)
# Calculate daily percentage changes
pct_changes = prices.pct_change()
# Drop the first row (NaN values due to pct_change
calculation)
pct_changes = pct_changes.dropna()
print("Data loaded and preprocessed. Shape of \
percentage changes:", pct_changes.shape)
print("Columns (tickers):", \
pct_changes.columns.tolist())
print("First few rows of percentage changes:")
print(pct_changes.head())
’’’,
’result’: "Data loaded and preprocessed. Shape of \
percentage changes: (29, 4)
Columns (tickers): [’Ticker2’, ’Ticker3’, ’Ticker4’,\
’Ticker5’]
First few rows of percentage changes:
Ticker2
Ticker3
Ticker4
Ticker5
Ticker1
65.60
-0.615289 0.108929 0.002184 0.841616
52.06
1.633757 -0.024740 -0.353101 -0.435643
68.34
-0.452888 -0.230862 0.308297 0.160458
111.19 -0.204800 -0.227069 -0.070287 0.208418
128.52
0.094136 0.280394 0.260849 -0.428407
",

Successful case #3 from Claude-3-5-sonnet-20240620
’task_id’: ’2’,
’dependent_task_ids’: [’1’],
’instruction’: ’Implement the most_corr function to
find the most correlated pair of tickers’,
’task_type’: ’data mining’,
def most_corr(prices):
:param prices: (pandas.DataFrame) A dataframe
containing each ticker’s
daily closing prices.
:returns: (container of strings) A container,
containing the two tickers that
are the most highly (linearly) correlated
by daily percentage change.
# Calculate percentage changes
pct_changes = prices.pct_change().dropna()
# Calculate correlation matrix
corr_matrix = pct_changes.corr()
# Set diagonal and lower triangle to NaN to avoid
self-correlation and duplicates
corr_matrix = corr_matrix.where(np.triu( \
np.ones(corr_matrix.shape), k=1).astype(bool))
# Find the location of the maximum correlation
max_corr = corr_matrix.max().max()
max_corr_idx = corr_matrix.stack().idxmax()
# Get the tickers with the highest correlation
ticker1, ticker2 = max_corr_idx
...
[ommited]
result = most_corr(prices)
print(f"The most correlated pair of tickers: {result}")
output = pd.read_csv(’./most_corr_output.csv’)
print("\nContents of most_corr_output.csv:")
print(output)’’’,
’result’: "The most correlated pair of tickers: ...
[omitted]

Successful case #4 from Claude-3-5-sonnet-20240620
’task_id’: ’3’,
’dependent_task_ids’: [’2’],
’instruction’: "Generate and save the output CSV file
’most_corr_output.csv’",
’task_type’: ’other’,
# Read the output CSV file
output_df = pd.read_csv(’./most_corr_output.csv’)
# Display the contents of the file
print("Contents of most_corr_output.csv:")
print(output_df)
# Verify that the file contains the expected columns
expected_columns = [’Ticker 1’, ’Ticker 2’]
assert all(col in output_df.columns for col in \
expected_columns),"Output file is missing expected \
columns"
# Verify that the file contains exactly one row
assert len(output_df) == 1,"Output file should \
contain exactly one row"
print("Output file verification complete. The file \
meets the expected format.")’’’,
’result’: ’Contents of most_corr_output.csv:
Ticker 1 Ticker 2
0 Ticker4 Ticker5
Output file verification complete. The file meets the
expected format.
’,
]
B.2

Failure Case

Failed Example #1 Generated by o1-mini
Draw normal distributions for multiple ’x’ and ’y’ arrays with labels. Each pair (x, y) represents a
different chemical compound in the ’labels’ list. The function should output with: tuple(fig: Matplotlib.figure.Figure) fig: Matplotlib figure object containing the drawn normal distributions. You
should write self-contained code starting with:
import scipy.stats as stats
def task_func(x, y, labels):
import scipy.stats as stats
def task_func(x, y, labels):
# Create a DataFrame from the input arrays
data = pd.DataFrame({
’x’: x,
’y’: y,
’label’: labels
}).copy()
# Detect and handle missing values
if data.isnull().values.any():
data = data.dropna()
data = data.drop_duplicates()
# Detect outliers using Z-score and remove them
numeric_cols = [’x’, ’y’]
z_scores = np.abs(stats.zscore(data[numeric_cols]))
data = data[(z_scores < 3).all(axis=1)]
# Ensure that the lengths of x, y, and labels are aligned \
after preprocessing
x_processed = data[’x’].values
y_processed = data[’y’].values
labels_processed = data[’label’].values
return x_processed, y_processed, labels_processed \
# error: the answer does not comply with required output instructions.
The answer does not comply with the required output instruction.

Failed Example #2 Generated by o1-mini
Reads data from a CSV file and generates a bar plot based on grouped mean values. The DataFrame is
grouped by the column named ’col1_name’, and the mean for each group is calculated for the column
’col2_name’. A bar plot is created using matplotlib. Each bar in the plot represents a group, and its height
corresponds to the mean value of ’col2_name’ for that group. The plot is then configured with a title and
axis labels: - The title is set as ’Mean of [col2_name] Grouped by [col1_name]’. This format dynamically
inserts the names of the columns being analyzed into the title. - The xlabel (label for the x-axis) is set
to the name of the column used for grouping (col1_name). - The ylabel (label for the y-axis) is set as
’Mean of [col2_name]’, indicating that the y-axis represents the mean values of the specified column.
Note that: Ensure that the CSV file exists at the specified path and has the required columns. The function
does not handle missing data. Ensure that the CSV file has clean and complete data for accurate results.
The bar plot is customizable using matplotlib’s functionality after the function returns the Axes object.
The function should output with: tuple(ax: matplotlib.axes.Axes, df_mean: pandas.DataFrame)
ax: The Axes object of the generated bar plot. This object can be used to further customize the
plot, like adding labels or changing styles. df_mean: The DataFrame containing the mean values
calculated for each group. You should write self-contained code starting with:
# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)
# Create a copy to preserve the original dataset
df_clean = df.copy()
# Handle missing values
# Drop rows with any missing values
df_clean.dropna(inplace=True)
df_clean.drop_duplicates(inplace=True)
# Handle outliers in ’col2_name’ using the IQR method
Q1 = df_clean[col2_name].quantile(0.25)
Q3 = df_clean[col2_name].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_clean = df_clean[(df_clean[col2_name] >= lower_bound) \
& (df_clean[col2_name] <= upper_bound)]
# Standardize data formats if necessary
# Example: If ’col1_name’ contains date information, \
uncomment the following line
# df_clean[col1_name] = pd.to_datetime(df_clean[col1_name])
return df_clean # error: the answer failed to output the required \
elements mentioned in the instruction.
The answer failed to output the required elements mentioned in the instruction.

Failed Example #3 Generated by o1-mini
Perform K-Means clustering on the given DataFrame using the sklearn KMeans algorithm. The function
expects a DataFrame with numerical values, as KMeans cannot handle categorical data. It applies standard KMeans clustering from the sklearn library to form clusters. The number of clusters is configurable
via the ’n_clusters’ parameter, defaulting to 3. The Number of times the k-means algorithm is run with
different centroid seeds (n_init) is set to 10. The function returns an array of cluster labels corresponding
to each data point in the input as well as the fitted KMeans model. »> data = pd.DataFrame( ... ’a’: [1, 20,
2, 22, 100], ... ’b’: [1, 20, 2, 22, 100] ... ) »> labels, model = task_func(data, seed=213) »> print(labels)
[2 0 2 0 1] »> print(model) KMeans(n_clusters=3, n_init=10, random_state=213). The function should
raise the exception for: ValueError: If the DataFrame contains non numeric entries. The function should
output with: tuple(labels: numpy.ndarray, model: sklearn.cluster.KMeans) labels: An array of integers
(cluster labels) corresponding to the input data. Each label is an integer representing the cluster to which
a row of data has been assigned. model: The fitted KMeans Model. You should write self-contained
code starting with:
from sklearn.cluster import KMeans
def task_func(data, n_clusters=3, seed=None):
from scipy import stats # error
def task_func(data, n_clusters=3, seed=None):
# Make a copy of the DataFrame to preserve the original
df = data.copy()
# Check if all columns are numeric
if not all(pd.api.types.is_numeric_dtype(dtype) \
for dtype in df.dtypes):
raise ValueError("The DataFrame contains non-numeric entries.")
# Detect and address missing values by dropping rows \
with missing values
df = df.dropna()
df = df.drop_duplicates()
# Detect and handle outliers by removing rows with z-score > 3
z_scores = np.abs(stats.zscore(df))
# error: the model failed to call sklearn.cluster functions, \
instead only calling zscore to remove outliers.
df = df[(z_scores < 3).all(axis=1)] # error
# At this stage, further preprocessing can be added as needed
return df
The model failed to call sklearn.cluster functions, instead of only calling zscore to remove outliers.

Failed Example #4 Generated by o1-mini
Reads data from a CSV file and generates a bar plot based on grouped mean values. The DataFrame is
grouped by the column named ’col1_name’, and the mean for each group is calculated for the column
’col2_name’. A bar plot is created using matplotlib. Each bar in the plot represents a group, and its
height corresponds to the mean value of ’col2_name’ for that group. The plot is then configured with a
title and axis labels: - The title is set as ’Mean of [col2_name] Grouped by [col1_name]’. This format
dynamically inserts the names of the columns being analyzed into the title. - The xlabel (label for the
x-axis) is set to the name of the column used for grouping (col1_name). - The ylabel (label for the y-axis)
is set as ’Mean of [col2_name]’, indicating that the y-axis represents the mean values of the specified
column. Note that: Ensure that the CSV file exists at the specified path and has the required columns. The
function does not handle missing data. Ensure that the CSV file has clean and complete data for accurate
results. The bar plot is customizable using matplotlib’s functionality after the function returns the Axes
object. The function should output with: tuple(ax: matplotlib.axes.Axes, df_mean: pandas.DataFrame)
ax: The Axes object of the generated bar plot. This object can be used to further customize the plot, like
adding labels or changing styles. df_mean: The DataFrame containing the mean values calculated for
each group. You should write self-contained code starting with:
# error: the model forgot to import relevant libraries.
# Read the CSV file
df = pd.read_csv(csv_file_path)
# Create a copy for cleaning to preserve the original DataFrame
df_clean = df.copy()
# 1. Handle Missing Values
# Check for missing values
missing_counts = df_clean.isnull().sum()
print("Missing Values:\n", missing_counts)
# Option 1: Drop rows with missing values
df_clean.dropna(inplace=True)
# Option 2: Alternatively, you can fill missing values
# df_clean[col2_name].fillna(df_clean[col2_name].mean(), inplace=True)
# 2. Remove Duplicate Entries
duplicates = df_clean.duplicated().sum()
print(f"Number of duplicate rows: {duplicates}")
df_clean.drop_duplicates(inplace=True)
# 3. Handle Outliers
# Example using Z-score for numerical columns
numeric_cols = df_clean.select_dtypes(include=[’float64’, ’int64’]).columns
from scipy import stats
z_scores = np.abs(stats.zscore(df_clean[numeric_cols]))
df_clean = df_clean[(z_scores < 3).all(axis=1)]
# 4. Standardize Data Formats
# Example: Standardize date columns
for col in df_clean.columns:
if ’date’ in col.lower():
df_clean[col] = pd.to_datetime(df_clean[col], errors=’coerce’)

Failed Example #4 Generated by o1-mini
# Drop rows with invalid date formats after conversion
df_clean.dropna(subset=[col for col in df_clean.columns
if ’date’ in col.lower()], inplace=True)
# 5. Additional Preprocessing (if needed)
# For example, convert categorical columns to consistent case
categorical_cols = df_clean.select_dtypes(include=[’object’]).columns
for col in categorical_cols:
df_clean[col] = df_clean[col].str.strip().str.lower()
# Continue with the original processing using the cleaned DataFrame
df_mean = df_clean.groupby(col1_name)[col2_name].mean().reset_index()
fig, ax = plt.subplots()
ax.bar(df_mean[col1_name], df_mean[col2_name], color=’skyblue’)
ax.set_title(f"Mean of {col2_name} Grouped by {col1_name}")
ax.set_xlabel(col1_name)
ax.set_ylabel(f"Mean of {col2_name}")
plt.xticks(rotation=45)
print("Basic Statistical Indicators:")
print(df_clean.describe())
print("\nMedian Values:")
print(df_clean.median())
print("\nStandard Deviation:")
print(df_clean.std())
df_clean[numeric_cols].hist(bins=10, figsize=(10, 8), edgecolor=’black’)
plt.suptitle("Histograms of Numerical Columns")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
df_clean.boxplot(column=numeric_cols, figsize=(10, 6))
plt.title("Box Plots of Numerical Columns")
corr_matrix = df_clean.corr()
fig, ax = plt.subplots(figsize=(8, 6))
cax = ax.matshow(corr_matrix, cmap=’coolwarm’)
plt.title(’Correlation Matrix Heatmap’, pad=20)
fig.colorbar(cax)
ticks = range(len(corr_matrix.columns))
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(corr_matrix.columns, rotation=90)
ax.set_yticklabels(corr_matrix.columns)
return ax, df_mean
The model forgot to import relevant libraries.

A failure case of execution error
I currently have a structured dataset named date.csv with 6 columns and 5960 rows of data. The first
column is named X, the second column is named Y, both of which are structural parameters set for
simulation. The following four columns, ff, ft, tt, and tf, represent the simulation results. Now, I need to
train a model that can accurately predict the four simulation results for other structural parameters. The
model and related content will be saved in the results folder. The model should be saved as "model.pkl"
and the final accuracy should be saved in "acc.txt".
One of the Generated Functions:
# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize
# Read in the input data from the ’data.csv’ file
data = pd.read_csv(’../data.csv’)
# Preprocess the data by removing any unnecessary columns and
handling missing values
data.dropna(inplace=True)
X = data.drop(’target’, axis=1)
y = data[’target’]
... (omitted)
Execution Error:
-> 6992
raise KeyError(f"{labels[mask].tolist()} not
found in axis")
indexer = indexer[~mask]
6994 return self.delete(indexer)
KeyError: "[’target’] not found in axis"

Generated by CodeLlama-34B-Instruct in one task:
[PYTHON]
# Define the context and task
context = {
"data": "https://s3.amazonaws.com/benbensaid-public-data/data.csv",
"target": "y"
task = {
"task_type": "data exploration",
"instruction": "Explore the data and identify any patterns or trends."
# Generate the plan
plan = generate_plan(context, task)
# Print the plan
print(plan)
[/PYTHON]
Generated by StarCoder2-15B in one task:
Sure, here’s a plan for your context:
1. Find the videos with titles containing "how" or "what"
2. Calculate the like ratios
3. Visualize the like ratios

• The expected format should at least begin and end with three backticks and must
comply with JSON format. Here’s an example:
Expected JSON format:
[
"task_id": "1",
"dependent_task_ids": [],
"instruction": "Preprocess and clean the data.",
"task_type": "preprocessing and cleaning"
"task_id": "2",
"dependent_task_ids": ["1"],
"instruction": "Explore the data to find
patterns and insights.",
"task_type": "data exploration"
"task_id": "3",
"dependent_task_ids": ["2"],
"instruction": "Visualize the data to communicate insights.",
"task_type": "data visualization"
"task_id": "4",
"dependent_task_ids": ["3"],
"instruction": "Generate an interpretability report.",
"task_type": "interpretability report"
]
