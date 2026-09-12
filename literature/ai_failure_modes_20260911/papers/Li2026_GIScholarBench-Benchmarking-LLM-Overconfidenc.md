# GIScholarBench: Benchmarking LLM Overconfidence in GIS Research

**Authors:** Li, Zongrng; Yang, Mingzheng; Zou, Lei; Ma, Hongxu; Tian, Hao; Zhou, Siqi; Gong, Wenjing; Zhang, Kaili; Chen, Bingqian; Zhang, Mitch; Yang, Yifan
**Year:** 2026
**Venue:** arXiv
**arXiv:** 2606.08036
**Source PDF URL:** https://arxiv.org/pdf/2606.08036
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---
GIScholarBench: Benchmarking LLM Overconfidence in GIS
Research [Experiment]
Zongrong Li∗

Mingzheng Yang∗

Lei Zou†

zongrong@tamu.edu

ymz2020@tamu.edu

lzou@tamu.edu

Hongxu Ma

Hao Tian

Siqi Zhou

hxma@google.com
Google
Mountain View, CA, USA

haotian@tamu.edu

siqizhou1107@tamu.edu

Wenjing Gong

Kaili Zhang

Bingqian Chen

wenjinggong@tamu.edu
Department of Landscape
Architecture and Urban Planning

kelly_zhang@tamu.edu
Department of Landscape
Architecture and Urban Planning

bingqc@tamu.edu

Mitch Zhang

Yifan Yang

mzhang22@tamu.edu

yyang295@tamu.edu

Abstract
Large language models (LLMs) are increasingly embedded in academic research workflows, yet the high factual precision required
in scholarly tasks makes them especially vulnerable to overconfidence. We use this term in a behavioral sense—the tendency to produce confident, assertive, and well-formatted outputs even when
the underlying knowledge is incomplete or unverifiable—rather
than in the calibration sense of a measured mismatch between a
model’s self-reported confidence and its accuracy. To systematically
evaluate this problem, we present GIScholarBench, a benchmark
constructed from 10,865 papers collected from 25 core GIScience
journals published between 2020 and 2025. The benchmark includes
three tasks of increasing cognitive complexity: metadata retrieval,
literature linking, and research direction generation. We evaluate
Claude Sonnet 4.5, Gemini 3, and ChatGPT 5.3 through their native
web interfaces under real-world user-facing conditions. The results
reveal consistent overconfidence across all three tasks. In metadata
retrieval, ChatGPT 5.3 achieves the highest accuracy (0.61–0.87),
yet all models continue generating definitive titles and DOIs even
when predictions are incorrect. In literature linking, Claude Sonnet
4.5 recovers the most references (Avg Hits = 10.3, P@20 = 0.53), but
all models exhibit a large divergence between Hit@1 (0.70–0.97)
and Hit@10 (0.08–0.61), indicating that citation lists are extended
∗ Both authors contributed equally to this research.
† Corresponding author.

beyond reliable retrieval capacity. In research direction generation,
AI-generated directions achieve substantially lower Topic Coverage
(0.09–0.12) than real future-citing papers (0.22), with Novel Miss
Rates of 0.88–0.91 and lower semantic diversity. These findings suggest that LLM overconfidence is task-invariant but form-varying,
appearing as factual overgeneration in retrieval, unreliable citation expansion in literature linking, and overconfidence in output
completeness in research ideation.

CCS Concepts
• Computing methodologies → Natural language processing;
Machine learning; • Information systems → Information retrieval;
Geographic information systems; • General and reference → Evaluation.

Keywords
Large language models; Overconfidence; GIScience; Benchmark
evaluation; Citation hallucination; Research direction generation

Introduction

Large language models (LLMs) have become increasingly embedded
in scientific research workflows. Recent large-scale analysis of over
one million preprints and journal articles finds that LLM-modified
content appears in up to 22% of computer science papers by late
2024, with adoption rates rising steadily across disciplines [13].

Researchers now routinely use systems such as Claude, Gemini, and
ChatGPT to locate papers, retrieve bibliographic metadata, draft
literature reviews, generate citation lists, and identify research
directions [3, 15, 20]. However, scholarly work requires a level
of factual precision that differs from general-purpose language
generation. A fabricated DOI, an incorrect citation, or a plausible but
unverified research direction can propagate through manuscripts,
databases, and reviews, creating errors that are difficult to detect
and costly to correct [22].
The key failure mode examined in this study is overconfidence.
Unlike hallucination in the narrow sense of outright fabrication,
overconfidence refers to the tendency of models to produce complete, assertive, and well-formatted outputs even when the required
knowledge is incomplete or unreliable. We adopt this term in a
deliberately behavioral sense: we treat overconfidence as an observable property of model outputs—assertive, authoritative presentation under conditions where the content is in fact incorrect or
unsupported—rather than in the calibration sense, which compares
a model’s explicitly elicited confidence against its empirical accuracy. Because our benchmark does not prompt models to report
confidence scores, we do not claim to measure calibration error
directly, and we treat the relationship between self-reported confidence and accuracy as an important complementary direction for
future work.
Prior studies have documented this overconfidence problem in
academic writing. For instance, Alkaissi and McFarlane [1] show
that ChatGPT can generate structurally valid but fictitious references, Walters and Wilder [23] quantify fabrication and attribution errors across generated bibliographies, and Mugaanyi et al.
[19] evaluate LLM citation reliability across multiple disciplines,
finding consistent accuracy limitations in reference generation.
Broader studies of LLM calibration further show that models have
limited awareness of their own uncertainty boundaries [10], and
that prompting models to express uncertainty does not reliably
improve calibration across knowledge-intensive tasks [24]. Despite
this evidence, systematic evaluation of overconfidence across multiple academic workflow tasks remains limited, particularly under
real-world user-facing conditions.
GIScience provides a suitable domain for evaluating this problem. The field has a well-defined journal landscape, established
bibliometric structure, strict metadata conventions, and dense citation networks across subfields [2, 9]. These characteristics make
it possible to construct objective ground truth for metadata retrieval, citation linking, and research direction generation using
Scopus records. Some existing LLM benchmarks, such as HELM [12]
and SciEval [21], have attempted to tackle this challenge, but they
mainly focus on factual question answering or domain knowledge
recall under controlled settings, rather than open-ended scholarly
workflow tasks under real user-facing conditions.
To address these gaps, we introduce GIScholarBench, a largescale benchmark for evaluating LLM academic capabilities and
overconfidence in GIScience. The benchmark is constructed from
10,865 papers collected from 25 core GIScience journals published
between 2020 and 2025. It includes three tasks of increasing cognitive complexity: metadata retrieval, literature linking, and research
direction generation. We evaluate Claude Sonnet 4.5, Gemini 3,
and ChatGPT 5.3 through their native web interfaces using an

automated browser-based collection workflow, ensuring that the
observed behavior reflects real-world user-facing conditions rather
than controlled API environments.
Based on prior evidence on LLM overconfidence and the increasing cognitive demands of the three tasks, we propose and examine
three hypotheses, each corresponding to one task. First, in metadata
retrieval, models are expected to produce definitive answers rather
than abstain, even when the correct metadata is uncertain. Verification instructions may reduce some errors, but may also encourage
models to rewrite outputs for surface consistency rather than rejecting unreliable answers. Second, in literature linking, models are
expected to identify one or a few plausible references but struggle to
maintain accuracy across a full citation list once reliable retrieval capacity is exhausted. Third, in research direction generation, models
are expected to concentrate on mainstream topic clusters and underrepresent frontier or cross-domain directions. Examining these
hypotheses is expected to demonstrate that LLM overconfidence is
not task-specific but exists across academic workflows, while its
form shifts from factual, to relational, to generative overconfidence
as task complexity increases.
The contributions of this work are three-fold. First, it introduces a
GIScience-focused benchmark for evaluating LLM performance and
overconfidence across multiple academic workflow tasks. Second,
it provides a systematic evaluation of the performance and overconfidence of deployed LLM systems under realistic user-facing conditions using a web-interface-based approach. Third, it characterizes
overconfidence as a task-invariant but form-varying phenomenon,
ranging from factual errors in metadata retrieval, to relational errors in citation linking and conservative and mainstream-biased
outputs in research direction generation.

2 Related Work
2.1 LLM Hallucination and Overconfidence in
Knowledge-Intensive Tasks
The tendency of LLMs to generate plausible but factually incorrect outputs, commonly referred to as hallucination, has received
substantial research attention. Prior studies distinguish between
factual hallucinations, which contradict verifiable knowledge, and
faithfulness hallucinations, which diverge from provided context
or source material [6]. Beyond hallucination itself, recent work has
identified overconfidence as a related but distinct issue. Rather than
simply fabricating information, overconfident models continue to
produce authoritative and highly certain responses even when operating beyond their reliable knowledge boundary. Kadavath et al.
[10] show that LLMs possess limited and inconsistent awareness of
their own uncertainty, while Xiong et al. [24] demonstrate that explicitly prompting models to express uncertainty does not reliably
improve calibration across knowledge-intensive tasks.
These problems become particularly critical in academic and scientific workflows. Alkaissi and McFarlane [1] report that ChatGPT
frequently generates fabricated academic references that appear
structurally valid despite being nonexistent. Walters and Wilder
[23] further quantify citation fabrication and attribution errors
across large-scale generated bibliographies, demonstrating that AIassisted citation generation remains unreliable without manual
verification. More broadly, factual evaluation frameworks such as

TruthfulQA [14] and FActScore [18] introduce systematic methods
for measuring factual correctness in open-ended generation. However, these benchmarks primarily target general-domain factuality
rather than scholarly literature tasks. In contrast, this study focuses
on overconfidence within academic workflows, particularly metadata retrieval, citation generation, and future research direction
prediction in GIScience literature.

records and entries without a resolvable DOI or abstract, the final
corpus contains 10,865 articles. For each article, we collect ten structured metadata fields: title, author list, author affiliations, source
journal, DOI, publication year, citation count, author-assigned keywords, abstract, and reference list. These metadata fields provide the
basis for evaluating different dimensions of academic intelligence,
particularly literature linking and research direction generation,
which rely on both semantic and citation-based contextual information.
The resulting corpus exhibits substantial disciplinary diversity
and publication imbalance across journals, reflecting the heterogeneous nature of GIScience research. As illustrated in Figure 2,
journals such as the International Journal of Geographical Information Science and the ISPRS Journal of Photogrammetry and Remote
Sensing contribute a large proportion of the collected articles, while
smaller domain-specific venues provide complementary coverage
of specialized research topics. The keyword distribution further
demonstrates the interdisciplinary characteristics of the dataset,
spanning themes related to geographic information science, environmental studies, spatial analysis, machine learning, remote
sensing, urban planning, and computational methods.

2.2

Benchmarking LLMs for Scientific
Literature and Domain Knowledge

Domain-specific benchmarks have become increasingly important
for evaluating whether LLMs satisfy the precision requirements of
professional and scientific fields. Existing benchmarks in medicine,
law, and science—including MedQA [8], LegalBench [4], and SciEval [21]—primarily evaluate question answering, reasoning, and
domain knowledge understanding. Broader frameworks such as
HELM [12] further assess calibration, robustness, and factual accuracy across multiple tasks. Although these benchmarks provide
valuable evaluations of domain knowledge, they rarely examine
open-ended academic workflow tasks such as literature retrieval,
citation linking, or research direction generation.
Within geospatial and GIScience research, prior studies have
explored the ability of foundation models and LLMs to support
spatial reasoning and geographic knowledge tasks. GeoLLM [17]
and StreetviewLLM [11] demonstrate that LLMs encode substantial geospatial knowledge and can be adapted for location-based
prediction tasks; Huang et al. [7] further benchmark LLMs on geometric classification, topological relations, and direction estimation
tasks, revealing systematic gaps in spatial reasoning, while Mai et al.
[16] review the broader opportunities and challenges of foundation
models in geospatial AI. Bibliometric studies have also analyzed the
publication structure and journal landscape of GIScience [2, 9], providing the disciplinary basis for corpus construction in this work.
However, to the best of our knowledge, no existing benchmark has
systematically evaluated LLM’s performance and overconfidence
behavior within GIScience scholarly workflows, particularly under
real-world user-facing web interfaces rather than controlled API
environments. GIScholarBench is poised to address this gap by constructing a large-scale benchmark that evaluates metadata retrieval,
literature linking, and future research direction generation across
deployed LLM systems.

3 Methodology
3.1 Dataset Construction
We construct the benchmark dataset from publications indexed in
the Scopus database. To ensure domain relevance and disciplinary
consistency, we identify 25 core GIScience journals based on prior
bibliometric surveys of the GIScience literature [2, 9]. Journals are
retained if they satisfy three criteria: (1) continuous indexing in
Scopus during the study period, (2) a primary focus on geographic
information science, spatial analysis, remote sensing–GIS integration, or spatial cognition, and (3) uninterrupted publication activity
between 2020 and 2025. The complete journal list and abbreviations
are provided in Table 1.
We retrieve publications published between January 2020 and
December 2025 through the Scopus API. After removing duplicate

3.2

Task Design and Evaluation

3.2.1 Task 1: Metadata Retrieval. We design Task 1 to evaluate
whether LLMs can accurately retrieve fundamental bibliographic
metadata for GIScience publications. The task includes two retrieval
directions: retrieving the article title from a DOI (DOI→Title) and
retrieving the DOI from an article title (Title→DOI). Each direction
is further evaluated under two prompt conditions, Strong and Weak,
resulting in four sub-tasks in total.
For the DOI→Title task, the Strong condition provides the model
with the article DOI, abstract, and keywords, together with an
explicit instruction to verify that the retrieved title is semantically
consistent with the supplied abstract. The Weak condition removes
the verification instruction and only asks the model to retrieve the
corresponding title from bibliographic metadata. For the Title→DOI
task, the Strong condition includes the article title, abstract, and
keywords, whereas the Weak condition reduces the input to the title
and a coarse domain descriptor (“GIScience”). This design enables
us to isolate the influence of contextual richness and instruction
specificity on retrieval performance. Full prompt templates for all
four sub-tasks are provided in the Appendix (Figure 9).
Ground-truth answer pairs are directly constructed from the
Scopus metadata collected in Section 3.1. The canonical title and
DOI associated with each of the 10,865 articles serve as the reference
labels, requiring no additional manual annotation.
For the DOI→Title task, we compare the model-generated title
𝑡ˆ with the ground-truth title 𝑡 ∗ after basic text normalization. Let
𝐾 (·) denote the set of content words after stopword removal. A
prediction is considered correct if:

1 if 𝑡ˆ = 𝑡 ∗
 1 if 𝑡 ⊆ 𝑡ˆ or 𝑡ˆ ⊆ 𝑡
ˆ
correct =
|𝐾 (𝑡 ) ∩ 𝐾 (𝑡 )|
1 if
≥ 0.6
|𝐾 (𝑡 ∗ )|
 0 otherwise


(1)

Figure 1: Overview of the GIScholarBench Construction Pipeline and Evaluation Framework.
Table 1: Core GIScience Journals Included in the Benchmark Dataset
Abbrev.

Full Name

Abbrev.

Full Name

AAG
AGIS
APG
CaGIS
C&G
CEUS
EPB
GEAN
GEIN
G&RS
GSIS
IJDE
IJGIS

Annals of the Association of American Geographers
Annals of GIS
Applied Geography
Cartography and Geographic Information Science
Computers & Geosciences
Computers, Environment and Urban Systems
Environment and Planning B: Urban Analytics and City Science
Geographical Analysis
Geoinformatica
GIScience & Remote Sensing
Geo-spatial Information Science
International Journal of Digital Earth
International Journal of Geographical Information Science

IJGI
JAG
JGS
JGSA
JOSIS
JSS
P&RS
PE&RS
PFG
SCC
TGIS
TSAS

ISPRS International Journal of Geo-Information
International Journal of Applied Earth Observation
Journal of Geographical Systems
Journal of Geovisualization and Spatial Analysis
Journal of Spatial Information Science
Journal of Spatial Science
ISPRS Journal of Photogrammetry and Remote Sensing
Photogrammetric Engineering & Remote Sensing
Photogrammetrie, Fernerkundung, Geoinformation
Spatial Cognition & Computation
Transactions in GIS
ACM Transactions on Spatial Algorithms and Systems

For the Title→DOI task, let 𝐷 (𝑟ˆ) represent the set of DOI strings
extracted from the model response 𝑟ˆ using a regular expression
pattern designed to identify standard DOI formats. A prediction
is considered correct if the ground-truth DOI 𝑑 ∗ appears in the
extracted DOI set:

correct = 1[𝑑 ∗ ∈ 𝐷 (𝑟ˆ)]

(2)

For both retrieval directions, we compute overall accuracy as:

Figure 2: Distribution of Articles and Research Keywords Across the GIScience Benchmark Dataset.

Acc =

𝑁
∑︁

1[correct𝑖 ],
𝑁 𝑖=1

𝑁 = 10,865

(3)

where 𝑁 is fixed to the full corpus size regardless of the number
of successfully collected responses, thereby proportionally penalizing incomplete response generation or failed retrieval attempts.
3.2.2 Task 2: Literature Linking. We design Task 2 to evaluate
whether large language models (LLMs) can recover the citationnetwork neighborhood of a given GIScience paper by identifying
related academic references. Specifically, models are asked to generate up to 20 real and verifiable papers that are likely to be cited by
the seed paper or to cite the seed paper. Two prompt variants are
evaluated. The Full setting provides the seed paper’s title, abstract,
and keywords, whereas the Short setting includes only the title.
This design enables us to examine how additional bibliographic context influences citation-link prediction performance. Full prompt
templates are provided in the Appendix (Figure 10).
Ground-truth citation sets are constructed from Scopus citation
records for each of the 816 seed papers. For every seed paper, we collect all papers within the benchmark corpus that either cite the seed
paper or are cited by it. The resulting citation neighborhoods range
from 1 to 352 references, with an average of 47.3 references per seed
paper. Note that ground-truth coverage is bounded by the 10,865paper corpus; references outside this set are not included, making
the reported hit metrics conservative lower-bound estimates of true
model recall.
Because model-generated titles may not exactly match the wording of ground-truth references, we adopt a fuzzy title-matching
strategy based on TF-IDF cosine similarity. For each predicted title ˆ𝑠,

we construct a hybrid feature representation combining word-level
TF-IDF features with character-level 𝑛-gram TF-IDF features (𝑛 = 3–
5). The similarity between a predicted title and a ground-truth title
𝑔 is computed as:
sim( ˆ𝑠, 𝑔) = cos(𝜙 ( ˆ𝑠), 𝜙 (𝑔)) ,



𝜙 (·) = 𝜙 word (·) ∥ 𝜙 char (·)

(4)

A prediction is considered successfully matched if the similarity
score exceeds a threshold of 𝜏 = 0.20. Each ground-truth reference
can only be matched once to avoid duplicate counting. Let 𝑀𝑖 denote
the number of successfully matched references for seed paper 𝑖,
and 𝑛ˆ𝑖 denote the number of predicted references. We report four
evaluation metrics over the set Q of 816 seed papers:
𝑀𝑖
𝑀𝑖
P@20 =
min(𝑛ˆ𝑖 , 20)
Hit@𝑘 =
1[𝑀𝑖 ≥ 𝑘], 𝑘 ∈ {1, 10}
Avg Hits =

(5)
(6)
(7)

These metrics jointly evaluate the ability of LLMs to recover
relevant citation relationships, while also measuring the precision
and consistency of the generated literature links.
3.2.3 Task 3: Research Direction Generation. We design Task 3 to
evaluate whether large language models (LLMs) can anticipate future research directions emerging from existing GIScience studies,
following the idea of using subsequent scientific impact to assess
the breadth of AI-generated research directions [5]. Specifically,
models are asked to generate 8–10 concrete and distinct research

directions that could naturally extend a given seed paper. Each
prompt includes the seed paper’s title, journal, publication year,
citation count, keywords, and abstract. Models are instructed to
produce actionable and diverse directions spanning different methods, spatial scales, regions, and research problems while avoiding
simple restatements of the original paper’s conclusions. The full
prompt template is provided in the Appendix (Figure 10, bottom),
and the overall evaluation framework is illustrated in Figure 3.
Ground-truth future research directions are constructed from
subsequent papers that cite each seed paper. For each of the 335 seed
papers, we collect all future-citing papers published after the seed
paper’s publication year. The titles and keywords of these futureciting papers are concatenated into a single ground-truth document
representing the actual research trajectories later pursued by the
GIScience community.
Because both generated directions and ground-truth references
are represented as free-form natural language, direct string matching is not appropriate. Instead, we project both into a shared topic
space derived from the ground-truth corpus. We first fit a TF-IDF
vectorizer with 10,000 features and sublinear term-frequency scaling on all ground-truth documents. We then apply K-Means clustering (𝑘 = 20) to derive 20 topic centroids {𝑐 1, . . . , 𝑐 20 } representing
the global landscape of future GIScience research directions. The
value 𝑘 = 20 was selected based on the elbow method applied
to within-cluster sum of squares, and produces clusters that are
interpretable as distinct GIScience research themes without overfragmenting the topic space.
For each seed paper 𝑖, the ground-truth topic coverage set is
defined as:


𝐶𝑖GT = 𝑗 ∈ {1, . . . , 𝑘} : ∃ 𝑔 ∈ 𝐺𝑖 , cos 𝜙 (𝑔), 𝑐 𝑗 ≥ 𝛿
(8)
where 𝜙 (·) denotes the TF-IDF embedding function and 𝛿 = 0.15
is the cluster assignment threshold. Similarly, the predicted topic
coverage set is:


𝐶𝑖
= 𝑗 ∈ {1, . . . , 𝑘} : ∃ 𝑑 ∈ 𝐷𝑖 , cos 𝜙 (𝑑), 𝑐 𝑗 ≥ 𝛿
(9)
We evaluate model performance using three complementary metrics. Topic Coverage (TC) measures the proportion of ground-truth
research topics successfully recovered by the generated directions:

TC𝑖 =

|𝐶𝑖

∩ 𝐶𝑖GT |

|𝐶𝑖GT |

TC =

TC𝑖

(10)

Novel Miss Rate (NMR) measures the proportion of ground-truth
research directions not captured by the model outputs:

NMR𝑖 =

|𝐶𝑖GT \ 𝐶𝑖

|𝐶𝑖GT |

|

NMR =

NMR𝑖

(11)

To evaluate thematic diversity, we compute the Herfindahl–
Hirschman Index (HHI), which measures the concentration of generated directions across topic clusters:

𝑘 
∑︁
𝑛𝑖 𝑗 2
HHI𝑖 =
HHI =
HHI𝑖
(12)
|𝐷
|
𝑖
𝑗=1

where 𝑛𝑖 𝑗 denotes the number of generated directions assigned to
cluster 𝑗, and |𝐷𝑖 | denotes the total number of generated directions
for seed paper 𝑖. Higher Topic Coverage and lower Novel Miss

Rate and HHI values indicate stronger performance in anticipating
diverse and realistic future research trajectories.

3.3

Data Collection Strategy

We collect model responses through each platform’s native web
interface rather than through official APIs. This strategy better
reflects the environment used by most real-world users and captures
product-level behaviors such as retrieval augmentation, knowledgecutoff handling, response formatting, and refusal patterns. It also
avoids potential differences between API-based and web-based
model deployments. The three evaluated systems are Claude Sonnet
4.5 (Anthropic), Gemini 3 (Google), and ChatGPT 5.3 (OpenAI),
accessed through their respective web chat interfaces.
To automate response collection at scale, we use the JSONL
Batch Sender (v6.3) browser extension (Figure 4). For each task
and model, we prepare a JSONL prompt file in which each line
contains a unique item identifier and a fully instantiated prompt.
The extension loads this file, submits prompts sequentially through
the chat interface, waits for each model response to complete, and
records the generated output text.
Responses are exported incrementally in JSONL format after
each query, which provides fault-tolerant snapshots and allows
interrupted sessions to be resumed. To reduce the risk of exceeding
platform limits or triggering anti-automation mechanisms, we apply
configurable delays between messages and periodic rest intervals
during collection. This workflow enables reproducible large-scale
response collection across all three tasks and three models using
only their public web interfaces.

4 Results
4.1 Metadata Retrieval Performance
Figure 5 presents the metadata retrieval accuracy across four Task 1
settings. The central finding is not only that models differ in accuracy, but that all three models tend to produce complete and
confident bibliographic answers even when those answers are incorrect. ChatGPT achieves the highest accuracy overall, reaching
0.87 in the Title→DOI Strong setting, while Claude and Gemini
perform lower in several settings. However, none of the models
meaningfully signal uncertainty or abstain from answering when
retrieval fails. This suggests that metadata retrieval is often treated
as a generative task, where models produce plausible titles or DOIs
rather than explicitly recognizing the limits of their knowledge.
The Strong and Weak settings further reveal how overconfidence
appears under different forms of context. In the Title→DOI task,
additional context improves accuracy for all models, indicating that
abstracts and keywords help disambiguate publications. In contrast,
the DOI→Title task shows weaker or inconsistent gains: Claude
decreases from 0.48 to 0.28, ChatGPT remains nearly unchanged,
and only Gemini improves. In these cases, models often generate
titles that are semantically compatible with the supplied abstract
but do not match the actual paper title. This behavior reflects a key
form of overconfidence in scholarly metadata retrieval: models do
not simply fail silently, but often present plausible, well-formed,
and authoritative answers that mask factual errors.

Figure 3: Overall Evaluation Framework for Future Research Direction Generation and Topic-Space Assessment.

4.2

Figure 4: Automated Web-Based Prompt Collection Using
the JSONL Batch Sender Extension.

Citation Linking Performance

Figure 6 summarizes the Task 2 results across Avg Hits, P@20,
Hit@1, and Hit@10. A consistent pattern emerges across all models and prompt settings: models are generally able to retrieve at
least one relevant citation for most seed papers, but performance
declines substantially when generating longer citation lists. This
gap between partial retrieval success and overall citation accuracy
reveals a key characteristic of LLM-based literature linking: models
often continue generating plausible references even after reliable
retrieval capacity has been exhausted.
The contrast between Hit@1 and Hit@10 is particularly notable.
Claude achieves the strongest overall performance, with Hit@1
rates above 0.96 and Hit@10 rates above 0.60 in both prompt settings. Gemini and ChatGPT also achieve relatively strong Hit@1
performance, indicating that the models can usually identify at least
one topically relevant citation. However, Hit@10 drops sharply for
these models, reaching only 0.20 for Gemini Full, 0.08 for ChatGPT
Full, and 0.14 for ChatGPT Short. Precision@20 further highlights
this issue. Gemini achieves P@20 values of only 0.23 and 0.17, implying that most generated references cannot be matched to verified
citation records. ChatGPT achieves higher precision values (approximately 0.52), partly because it tends to generate shorter reference

Figure 5: Metadata Retrieval Accuracy Across Task 1 Settings (content-based matching, denominator = 10,865).

Figure 6: Literature Linking Performance Across Models and Prompt Conditions (content-based matching).
lists rather than fully populating all 20 entries. Even Claude, despite
obtaining the highest Avg Hits and Hit@10 performance, still produces a substantial proportion of unmatched citations. Across all
evaluated settings, no model exceeds a P@20 value of 0.55, indicating that a large fraction of generated references remain unverifiable
despite being presented in fluent and authoritative formats.

4.3

Research Direction Generation Performance

Figures 7 and 8 summarize the Task 3 results from both metricbased and distributional perspectives. Across all models, generated
research directions exhibit substantially narrower topical coverage
than the trajectories observed in real future-citing literature. Although the generated directions are typically presented as concrete
and actionable research ideas, the evaluation results indicate that
the models cover only a limited portion of the broader GIScience
research space.
As shown in Figure 7(a), the Ground Truth baseline achieves
a mean Topic Coverage of approximately 0.22, whereas Claude
reaches 0.12 and both Gemini and ChatGPT remain near 0.09. The
corresponding Novel Miss Rate results in Figure 7(c) show that

Gemini and ChatGPT fail to capture approximately 91% of the topic
space represented by real downstream research. Figure 7(b) further
demonstrates that model-generated directions are substantially
more concentrated than real research trajectories. The Ground
Truth baseline achieves a mean HHI of approximately 0.64, while
Claude increases to 0.70 and both Gemini and ChatGPT approach
0.87, indicating that many generated direction lists collapse into a
small number of highly similar topic clusters rather than spanning
diverse research themes.
Figure 8 reveals a similar pattern at the distributional level. The
Ground Truth occupies a broad and spatially dispersed region of
the GIS semantic space, achieving a kernel entropy (KE) of 0.308.
In contrast, all three AI models produce substantially smaller and
more centrally concentrated distributions, with KE values of 0.196
for Claude, 0.183 for Gemini, and 0.179 for ChatGPT. The modelgenerated distributions overlap heavily with one another but cover
only a limited portion of the broader semantic space occupied by
real future research. Peripheral regions associated with emerging,
cross-domain, or less conventional directions remain largely absent
from the generated outputs.

Figure 7: Comparative Evaluation of AI-Generated and Ground-Truth Research Directions in Task 3 (box plots with mean
diamonds; 𝑛 = 335 for all groups).

Figure 8: Distribution of Ground-Truth and AI-Generated Research Directions in GIS Semantic Space (kernel entropy KE values
shown in legend).

5 Discussion
5.1 Overconfidence as a Task-Invariant but
Form-Varying Phenomenon
The results across all three tasks reveal a consistent pattern: overconfidence persists across different academic workflows, but its
form changes with task structure. In Task 1, overconfidence appears as factual overgeneration. Models continue producing specific bibliographic metadata even when retrieval accuracy is limited,
with little uncertainty or abstention. This is especially clear in the
DOI→Title Strong setting, where added verification instructions
do not consistently improve accuracy. Claude declines from 0.48
to 0.28, and ChatGPT remains nearly unchanged from 0.83 to 0.81.
Instead of rejecting uncertain answers, models often generate titles
that appear semantically aligned with the abstract but differ from
the actual paper title. This suggests that models prioritize coherent
and complete responses over strict factual fidelity.
In Task 2, overconfidence becomes relational. Models can often
identify at least one plausible citation, as shown by high Hit@1
scores ranging from 0.70 to 0.97. However, Hit@10 drops sharply,
especially for Gemini Full (0.20) and ChatGPT Full (0.08), indicating that models struggle to recover multiple verified citation
links. Precision@20 never exceeds 0.55, meaning that a substantial
share of generated references remains unmatched despite fluent
formatting. In Task 3, overconfidence takes a meta-cognitive form.
Model-generated directions have lower Topic Coverage than actual
future-citing papers, with AI models ranging from 0.09 to 0.12 compared with 0.22 for Ground Truth. They also show higher Novel
Miss Rate (0.88–0.91), stronger topic concentration (HHI = 0.70–0.87
vs. 0.64 for Ground Truth), and lower semantic-space diversity (KE
= 0.179–0.196 vs. 0.308 for Ground Truth). Critically, the individual
directions are not factually wrong; rather, the overconfidence lies
in the model’s implicit claim of completeness. Models produce 8–10
directions with no hedging about what might be absent, yet cover
only a small fraction of the topic space occupied by real future
research. This reflects what Kadavath et al. [10] identify as a core
limitation of LLM self-knowledge: models do not know what they
do not know. In Task 3, this manifests as overconfidence about the
coverage and representativeness of the generated output, not about
the correctness of individual items.

5.2

Implications for AI-Assisted GIS Research
Practice

The findings of this study have direct implications for GIScience
researchers who use LLMs in scholarly workflows. Because overconfidence appears across all three tasks and all evaluated models,
the risk is not limited to poor prompts or isolated failure cases. Even
under routine, well-formed queries, models often produce fluent
and authoritative outputs that require verification. For metadata retrieval, even the best-performing model still returns incorrect titles
or DOIs in a nontrivial share of cases, so LLM-generated metadata
should not be directly used in manuscripts, citation records, or database queries without checking authoritative sources such as Scopus,
Crossref, or DOI registries. For literature linking, the high Hit@1
scores (0.70–0.97) suggest that LLMs can help users identify initial
anchor papers and quickly enter an unfamiliar topic. However, the

much lower Hit@10 scores (0.08–0.61) and P@20 values below 0.55
show that complete generated reference lists remain incomplete
and often unverifiable. Therefore, AI-generated citations should
be treated as preliminary leads rather than reliable bibliographic
outputs.
For research direction generation, the risk is less visible because
the outputs are usually coherent, specific, and actionable. However,
our results show that AI-generated ideas cover a much narrower
portion of the GIScience research space than real future-citing papers, with Topic Coverage of only 0.09–0.12 compared with 0.22 for
Ground Truth. This indicates that LLMs tend to reproduce familiar and mainstream directions while underrepresenting emerging,
interdisciplinary, or unconventional trajectories. More productive
AI-assisted GIScience workflows should position LLMs as auxiliary
tools for orientation, filtering, and idea structuring, while relying
on human researchers to verify factual claims, trace citations systematically, and actively search for directions that the model may
overlook.

5.3

Limitations and Future Directions

Several limitations of this study should be acknowledged. First, the
browser-based collection strategy improves ecological validity by
evaluating models through real-world user-facing web interfaces,
but it also introduces reproducibility challenges. Web-deployed
LLM systems are continuously updated through model revisions,
interface changes, and platform-level adjustments that are not always publicly documented. As a result, the behaviors observed in
this study reflect the deployed model versions available during the
collection period, and future replications using identical prompts
may produce different outputs.
Second, the benchmark is constructed entirely from GIScience
literature, and the extent to which these findings generalize to other
scientific domains remains uncertain. GIScience has a distinctive
interdisciplinary structure and relies heavily on domain-specific terminology, spatial reasoning, and geospatial methodologies, which
may influence retrieval accuracy and overconfidence behavior differently from fields such as medicine, law, or the social sciences.
Future work should therefore extend the benchmark to additional
disciplines and model families, including open-weight, domain-finetuned, and retrieval-augmented systems. Such extensions would
help determine whether overconfidence is a general property of
current LLM architectures or whether specialized corpora, retrieval
mechanisms, confidence scoring, and explicit “Not Found” constraints can improve factual reliability, topic coverage, and calibration in scholarly workflows.
Third, our analysis characterizes overconfidence as a behavioral
property of model outputs and does not measure confidence calibration in the strict sense. We do not elicit explicit confidence
estimates from the models, so we cannot quantify the gap between
a model’s self-reported certainty and its empirical accuracy (for
example, via reliability diagrams or expected calibration error). Establishing this calibration relationship—and thereby statistically
validating overconfidence in the calibration sense—is an important
direction that our current design leaves open.

Conclusion

This paper presents GIScholarBench, a large-scale benchmark for
evaluating LLM academic capabilities and overconfidence in GIScience scholarly workflows. Built from 10,865 papers from 25 core
GIScience journals published between 2020 and 2025, the benchmark evaluates metadata retrieval, literature linking, and research
direction generation across Claude, Gemini, and ChatGPT through
native web interfaces. The results show that LLMs often produce
fluent and authoritative outputs even when their answers are incorrect, incomplete, or poorly calibrated. In metadata retrieval, models
generate specific titles and DOIs despite factual errors. In literature
linking, they can identify some relevant citations but continue producing unverifiable references, with Precision@20 never exceeding
0.55. In research direction generation, model outputs concentrate
on familiar GIScience themes and show lower topical diversity than
real future-citing papers. These findings suggest that LLMs are
useful as orientation and brainstorming tools, but should not be
treated as authoritative sources for scholarly knowledge. GIScholarBench provides a foundation for evaluating epistemic reliability
in AI-assisted GIScience research.

References
[1] Hussam Alkaissi and Samy McFarlane. 2023. Artificial hallucinations in ChatGPT:
Implications in scientific writing. Cureus 15 (02 2023). doi:10.7759/cureus.35179
[2] Filip Biljecki. 2016. A scientometric analysis of selected GIScience journals.
International Journal of Geographical Information Science 30 (01 2016), 1302–1335.
doi:10.1080/13658816.2015.1130831
[3] Marcel Binz, Stephan Alaniz, Adina Roskies, Balazs Aczel, Carl T. Bergstrom,
Colin Allen, Daniel Schad, Dirk Wulff, Jevin D. West, Qiong Zhang, Richard M.
Shiffrin, Samuel J. Gershman, Vencislav Popov, Emily M. Bender, Marco Marelli,
Matthew M. Botvinick, Zeynep Akata, and Eric Schulz. 2025. How should the
advancement of large language models affect the practice of science? Proceedings
of the National Academy of Sciences 122 (01 2025). doi:10.1073/pnas.2401227121
[4] Neel Guha, Julian Nyarko, Daniel E Ho, Christopher Ré, Adam Chilton, Aditya
Narayana, Alex Chohlas-Wood, Austin Peters, Brandon Waldon, Daniel N Rockmore, Diego Zambrano, Dmitry Talisman, Enam Hoque, Faiz Surani, Frank Fagan,
Galit Sarfaty, Gregory M Dickinson, Haggai Porat, Jason Hegland, Jessica Wu, Joe
Nudell, Joel Niklaus, John Nay, Jonathan H Choi, Kevin Tobia, Margaret Hagan,
Megan Ma, Michael Livermore, Nikon Rasumov-Rahe, Nils Holzenberger, Noam
Kolt, Peter Henderson, Sean Rehaag, Sharad Goel, Shang Gao, Spencer Williams,
Sunny Gandhi, Tom Zur, Varun Iyer, and Zehua Li. 2023. LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language
Models. https://arxiv.org/abs/2308.11462
[5] Qianyue Hao, Fengli Xu, Yong Li, and James Evans. 2026. Artificial intelligence
tools expand scientists’ impact but contract science’s focus. Nature (01 2026).
doi:10.1038/s41586-025-09922-y
[6] Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian
Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, and Ting Liu.
2024. A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions. ACM transactions on office information
systems 43 (11 2024). doi:10.1145/3703155
[7] Yu Chin Huang, Yuhan Ji, and Song Gao. 2025. Evaluating Geospatial Reasoning
Capabilities in Large Language Models: A Benchmark on Geometry Classification,
Topological Relations and Direction Estimation. Proceedings of the 4th ACM
SIGSPATIAL International Workshop on Spatial Big Data and AI for Industrial
Applications (11 2025), 64–71. doi:10.1145/3764919.3770881
[8] Di Jin, Eileen Pan, Nassim Oufattole, Wei-Hung Weng, Hanyi Fang, and Peter
Szolovits. 2021. What Disease Does This Patient Have? A Large-Scale Open
Domain Question Answering Dataset from Medical Exams. Applied Sciences 11
(07 2021), 6421. doi:10.3390/app11146421
[9] Levente Juhász. 2024. Assessing publication trends in selected GIScience journals.
International Journal of Geographical Information Science 38 (05 2024), 1443–1467.
doi:10.1080/13658816.2024.2347306
[10] Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain,
Ethan Perez, Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli TranJohnson, Scott Johnston, Sheer El-Showk, Andy Jones, Nelson Elhage, Tristan
Hume, Anna Chen, Yuntao Bai, Sam Bowman, Stanislav Fort, Deep Ganguli,
Danny Hernandez, Josh Jacobson, Jackson Kernion, Shauna Kravec, Liane Lovitt,
Kamal Ndousse, Catherine Olsson, Sam Ringer, Dario Amodei, Tom Brown, Jack

Clark, Nicholas Joseph, Ben Mann, Sam McCandlish, Chris Olah, and Jared Kaplan.
2022. Language Models (Mostly) Know What They Know. https://arxiv.org/abs/
2207.05221
[11] Zongrong Li, Junhao Xu, Siqin Wang, Yifan Wu, and Haiyang Li. 2024.
StreetviewLLM: Extracting Geographic Information Using a Chain-of-Thought
Multimodal Large Language Model. https://arxiv.org/abs/2411.14476
[12] Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar,
Benjamin Newman, Binhang Yuan, Bobby Yan, Ce Zhang, Christian Cosgrove,
Christopher D. Manning, Christopher Ré, Diana Acosta-Navas, Drew A. Hudson,
Eric Zelikman, Esin Durmus, Faisal Ladhak, Frieda Rong, Hongyu Ren, Huaxiu
Yao, Jue Wang, Keshav Santhanam, Laurel Orr, Lucia Zheng, Mert Yuksekgonul,
Mirac Suzgun, Nathan Kim, Neel Guha, Niladri Chatterji, Omar Khattab, Peter
Henderson, Qian Huang, Ryan Chi, Sang Michael Xie, Shibani Santurkar, Surya
Ganguli, Tatsunori Hashimoto, Thomas Icard, Tianyi Zhang, Vishrav Chaudhary,
William Wang, Xuechen Li, Yifan Mai, Yuhui Zhang, and Yuta Koreeda. 2022.
Holistic Evaluation of Language Models. https://arxiv.org/abs/2211.09110
[13] Weixin Liang, Yaohui Zhang, Zhengxuan Wu, Haley Lepp, Wenlong Ji, Xuandong
Zhao, Hancheng Cao, Sheng Liu, Siyu He, Zhi Huang, Diyi Yang, Christopher
Potts, Christopher D Manning, and James Zou. 2025. Quantifying large language
model usage in scientific papers. Nature Human Behaviour (08 2025). doi:10.1038/
s41562-025-02273-8
[14] Stephanie Lin, Jacob Hilton, and Owain Evans. 2022. TruthfulQA: Measuring
How Models Mimic Human Falsehoods. Proceedings of the 60th Annual Meeting
of the Association for Computational Linguistics (Volume 1: Long Papers) (01 2022).
doi:10.18653/v1/2022.acl-long.229
[15] Ziming Luo, Zonglin Yang, Zexin Xu, Wei Yang, and Xinya Du. 2025. LLM4SR: A
Survey on Large Language Models for Scientific Research. https://arxiv.org/abs/
2501.04306
[16] Gengchen Mai, Weiming Huang, Jin Sun, Suhang Song, Deepak Mishra, Ninghao
Liu, Song Gao, Tianming Liu, Gao Cong, Yingjie Hu, Chris Cundy, Ziyuan Li,
Rui Zhu, and Ni Lao. 2024. On the Opportunities and Challenges of Foundation
Models for GeoAI (Vision Paper). ACM transactions on spatial algorithms and
systems (03 2024). doi:10.1145/3653070
[17] Rohin Manvi, Samar Khanna, Gengchen Mai, Marshall Burke, David Lobell, and
Stefano Ermon. 2023. GeoLLM: Extracting Geospatial Knowledge from Large
Language Models. https://arxiv.org/abs/2310.06213
[18] Sewon Min, Kalpesh Krishna, Xinxi Lyu, Mike Lewis, Wen-tau Yih, Pang Koh,
Mohit Iyyer, Luke Zettlemoyer, and Hannaneh Hajishirzi. 2023. FActScore: Finegrained Atomic Evaluation of Factual Precision in Long Form Text Generation.
In Proceedings of the 2023 Conference on Empirical Methods in Natural Language
Processing (EMNLP 2023) (01 2023). doi:10.18653/v1/2023.emnlp-main.741
[19] Joseph Mugaanyi, Liuying Cai, Sumei Cheng, Caide Lu, and Jing Huang. 2023.
Citations and References in Scholarly Writing: A cross-disciplinary Evaluation
of Large Language Model Performance and Reliability. (Preprint). JMIR. Journal
of medical internet research/Journal of medical internet research 26 (09 2023).
doi:10.2196/52935
[20] Dmitry Scherbakov, Nina Hubig, Vinita Jansari, Alexander Bakumenko, and
Leslie A. Lenert. 2025. The emergence of large language models as tools in
literature reviews: a large language model-assisted systematic review. Journal of
the American Medical Informatics Association 32, 6 (03 2025), 1071–1086. doi:10.
1093/jamia/ocaf063
[21] Liangtai Sun, Yang Han, Zihan Zhao, Da Ma, Zhennan Shen, Baocai Chen, Lu
Chen, and Kai Yu. 2024. SciEval: A Multi-Level Large Language Model Evaluation Benchmark for Scientific Research. Proceedings of the AAAI Conference on
Artificial Intelligence 38 (03 2024), 19053–19061. doi:10.1609/aaai.v38i17.29872
[22] Maxim Topaz, Nir Roguin, Pallavi Gupta, Zhihong Zhang, and Laura-Maria
Peltonen. 2026. Fabricated citations: an audit across 2·5 million biomedical
papers. The Lancet 407 (05 2026), 1779–1781. doi:10.1016/s0140-6736(26)00603-3
[23] William H. Walters and Esther Isabelle Wilder. 2023. Fabrication and errors in
the bibliographic citations generated by ChatGPT. Scientific Reports 13 (09 2023),
14045. doi:10.1038/s41598-023-41032-5
[24] Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie Fu, Junxian He, and Bryan
Hooi. 2023. Can LLMs Express Their Uncertainty? An Empirical Evaluation of
Confidence Elicitation in LLMs. https://arxiv.org/abs/2306.13063

A

Prompt Templates

Figure 9: Prompt Templates for Task 1 Metadata Retrieval Evaluation.

Figure 10: Prompt Templates for Task 2 Literature Linking (top) and Task 3 Research Direction Generation (bottom).
