# Can AI Validate Science? Benchmarking LLMs for Accurate Scientific Claim to Evidence Reasoning

**Authors:** Shashidhar Reddy Javaji, Yupeng Cao, Haohang Li, Yangyang Yu, Nikhil Muralidhar, Zining Zhu
**Year:** 2025
**Venue:** arXiv preprint
**DOI:** arXiv:2506.08235
**Source PDF URL:** https://arxiv.org/pdf/2506.08235
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Can AI Validate Science ?
                                                                Benchmarking LLMs for Accurate Scientific
                                                                     Claim → Evidence Reasoning
                                                       Shashidhar Reddy Javaji, Yupeng Cao, Haohang Li, Yangyang Yu
                                                                      Nikhil Muralidhar, Zining Zhu
                                                                       Stevens Institute of Technology

                                                               Abstract                                   impressive capabilities such as automating com-
                                                                                                          prehensive literature reviews, facilitating innova-
                                            Large language models (LLMs) are increas-                     tive idea generation, and aiding experimental de-


arXiv:2506.08235v1 [cs.CL] 9 Jun 2025
                                            ingly being used for complex research tasks
                                                                                                          sign. These advancements promise significant im-
                                            such as literature review, idea generation, and
                                            scientific paper analysis, yet their ability to               provements in research productivity, creativity, and
                                            truly understand and process the intricate rela-              efficiency, fueling excitement about the transfor-
                                            tionships within complex research papers, such                mative potential of AI-driven methodologies in
                                            as the logical links between claims and support-              science. However, as researchers increasingly as-
                                            ing evidence remains largely unexplored. In                   sign critical tasks to these models—from content
                                            this study, we present CLAIM-BENCH, a com-                    summarization and hypothesis generation to au-
                                            prehensive benchmark for evaluating LLMs’                     tomated peer review (Checco et al., 2021; Agar-
                                            capabilities in scientific claim-evidence extrac-
                                                                                                          wal et al., 2025; Lu et al., 2024)—a fundamen-
                                            tion and validation, a task that reflects deeper
                                            comprehension of scientific argumentation.                    tal yet overlooked question emerges: how deeply
                                            We systematically compare three approaches                    do these models truly understand scientific knowl-
                                            which are inspired by divide and conquer ap-                  edge beyond surface-level pattern recognition? De-
                                            proaches, across six diverse LLMs, highlight-                 spite their widespread use and promising outcomes,
                                            ing model-specific strengths and weaknesses                   there remains uncertainty about the depth and ac-
                                            in scientific comprehension. Through evalua-                  curacy of their reasoning capabilities, particularly
                                            tion involving over 300 claim-evidence pairs
                                                                                                          in complex scientific contexts.
                                            across multiple research domains, we reveal
                                            significant limitations in LLMs’ ability to pro-                 Scientific papers are characterized by intricate
                                            cess complex scientific content. Our results                  relationships, primarily structured around claims
                                            demonstrate that closed-source models like                    supported by corresponding evidence. The ability
                                            GPT-4 and Claude consistently outperform                      to accurately identify and reason about these claim-
                                            open-source counterparts in precision and re-                 evidence pairs is essential for validating scientific
                                            call across claim-evidence identification tasks.              findings and ensuring research integrity, making
                                            Furthermore, strategically designed three-pass                it a critical test of LLMs’ comprehension depth.
                                            and one-by-one prompting approaches signif-
                                                                                                          Unlike surface-level tasks such as summarization
                                            icantly improve LLMs’ abilities to accurately
                                            link dispersed evidence with claims, although                 or question answering, claim-evidence identifica-
                                            this comes at increased computational cost.                   tion requires global reasoning across paper sec-
                                            CLAIM-BENCH sets a new standard for evalu-                    tions, synthesis of dispersed information, and a
                                            ating scientific comprehension in LLMs, offer-                nuanced understanding of logical dependencies.
                                            ing both a diagnostic tool and a path forward                 While existing works have assessed LLMs’ capa-
                                            for building systems capable of deeper, more                  bilities in related research tasks such as summa-
                                            reliable reasoning across full-length papers. 1
                                                                                                          rization (Agarwal et al., 2025), literature synthe-
                                                                                                          sis (Lu et al., 2024), and hypothesis generation
                                        1   Introduction
                                                                                                          (Vladika and Matthes, 2023), none have explicitly
                                        Large Language Models (LLMs) have become im-                      benchmarked LLM performance on systematically
                                        portant tool in academic research, demonstrating                  extracting and validating claims with supporting
                                                                                                          evidence, leaving this area of scientific comprehen-
                                              To facilitate future research and standardize evalua-
                                        tion in this area, we release CLAIM-BENCH at the                  sion underexplored.
                                        CLAIM_BENCH GitHub repository.                                       Despite the importance of accurately reasoning



about claims and supporting evidence, no existing             2   Related Work
benchmarks explicitly assess LLM capabilities for
                                                              AI for Science Large Language Models (LLMs)
this specific type of high-level scientific reasoning.
                                                              have significantly advanced scientific workflows,
Benchmarks such as LongGenBench (Wu et al.,
                                                              facilitating tasks such as peer review and hypothe-
2025) and XL2Bench (Ni et al., 2024) have high-
                                                              sis generation. Tools like ReviewerGPT (Liu and
lighted persistent limitations in LLMs’ abilities
                                                              Shah, 2023) and ReviewFlow (Sun et al., 2024a)
to process long-context inputs and maintain logi-
                                                              have streamlined peer review processes, while
cal coherence. Similarly, peer review frameworks
                                                              AGENTREVIEW (Jin et al., 2024) simulates col-
like MetaWriter (Sun et al., 2024b) and AGEN-
                                                              laborative review systems to improve research eval-
TREVIEW (Jin et al., 2024) evaluate LLMs in au-
                                                              uation workflows. In parallel, fact-checking frame-
tomated review contexts but do not specifically
                                                              works, such as Scientific Fact-Checking (Vladika
test their capability to validate logical relationships
                                                              and Matthes, 2023) and Exploring Multidimen-
such as claims and evidence, a task crucial for rig-
                                                              sional Checkworthiness (Liu et al., 2025), em-
orous scientific evaluation. Findings from Chain of
                                                              phasize validating claims in scientific literature.
Evidence (CoE) frameworks (Chang et al., 2024)
                                                              However, these systems primarily focus on local-
underscore the complexity of structured, multi-
                                                              ized tasks or prioritization mechanisms, leaving
hop reasoning required to integrate and validate
                                                              the broader challenge of understanding the con-
information dispersed across documents. All these
                                                              nections across entire documents by LLMs unad-
works evaluate reasoning in the general domains,
                                                              dressed. Additional work such as AI-assisted peer
but the scientific reasoning capability, which im-
                                                              review (Checco et al., 2021) explores the feasibility
poses unique challenges, is not benchmarked.
                                                              of algorithmically approximating peer-review judg-
   Within scientific reasoning, The AI Scientist (Lu
                                                              ments, raising key ethical and practical concerns.
et al., 2024), LitLLM (Agarwal et al., 2025), and
ChatCite (Li et al., 2025) benchmark LLMs on                  Benchmarks Long-context benchmarks, such as
tasks such as literature review and hypothesis gener-         SCBENCH (LI et al., 2025), MMLongBench-Doc
ation, while ScienceAgentBench (Chen et al., 2025)            (Ma et al., 2024), and LongGenBench (Wu et al.,
and SCBENCH (LI et al., 2025) probe multi-step                2025), have assessed LLMs’ ability to process ex-
reasoning and long-context understanding. How-                tended inputs and maintain coherence, focusing
ever, none of these frameworks explicitly measure             primarily on tasks like document summarization
the finer-grained ability to verify whether the evi-          and long-form generation. Specialized benchmarks
dence presented in a full scientific paper truly sup-         like U-MATH (Chernyshev et al., 2025) and Leave
ports its claims—precisely the claim-and-evidence             No Document Behind (Godbole et al., 2024) exam-
(C-E) reasoning capability our benchmark targets.             ine domain-specific reasoning and multi-document
   To address these gaps, we present CLAIM-                   synthesis but address relatively structured and local-
BENCH, a novel benchmark designed to system-                  ized relationships. The LCFO benchmark (Costa-
atically evaluate LLMs’ abilities to identify and             jussà et al., 2024a) targets summary expansion
validate claim-evidence relationships in scientific           with varying granularities of content compression,
papers. CLAIM-BENCH challenges LLMs to pro-                   revealing limits in semantic retention. The Y-
cess entire scientific papers, connect ideas across           NQ dataset (Costa-jussà et al., 2024b) exposes
sections, and reason about them on a high level. In           disparities in open-book comprehension across
this work, we evaluate six state-of-the-art LLMs              low- & high-resource languages, hinting at deeper
across diverse research domains. Our experiments              weaknesses in cross-lingual and low-resource long-
indicate that larger models (e.g., GPT-4-Turbo,               context understanding. Data Interpreter (Hong
Claude 3.5) maintain high recall even with lengthy            et al., 2024) showcases long-term data analysis
documents, especially when using iterative prompt-            workflows with LLM agents, but primarily focuses
ing, whereas smaller models (e.g., LLaMA, Minis-              on task planning and execution rather than deep tex-
tral) experience significant performance drops with           tual reasoning. In neuroscience, (Luo et al., 2025)
increasing document length specially under Single-            show LLMs surpassing expert predictions in future
Pass prompting. These findings highlight crucial              experimental outcomes, yet such success doesn’t
areas for enhancing long-context comprehension                imply comprehension of reasoning chains. In con-
and inform the development of reliable AI-driven              trast, our work focuses specifically on research pa-
tools for scientific research and peer review.                pers, which are characterized by more complex and



dispersed relationships, such as claims supported            papers according to specific guidelines (Appendix
by evidence across multiple sections. CLAIM-                 B.1) to ensure relevance and diversity. Selection
BENCH evaluates the ability of LLMs to synthe-               criteria included: papers from the year 2024, non-
size these intricate connections, testing their capac-       math-intensive subjects, length between 0 to 20
ity for global reasoning and coherence in a way              pages. The aim was to represent a broad spectrum
that reflects the unique demands of scientific texts.        of current AI/ML research topics within the dataset.
                                                                To facilitate easier annotations, we developed
Collaborative Reasoning Collaborative reason-
                                                             a PDF annotation tool, it lets users load a paper,
ing frameworks offer a complementary perspective,
                                                             drag a pointer over any sentence or paragraph to
with multi-agent systems like Two Heads Are Bet-
                                                             mark it as a claim, then click-add evidence addi-
ter Than One (Su et al., 2025) and iterative feed-
                                                             tional spans as linked evidence for that claim; each
back mechanisms such as CYCLERESEARCHER
                                                             claim–evidence pair is stored in a one-to-many
(Weng et al., 2025) showing promise in enhanc-
                                                             structure and exported as JSON. (see Appendix
ing reasoning capabilities. While these approaches
                                                             B.3).
address some limitations of Single-Pass LLM sys-
tems, their primary focus remains on generating              Annotation Quality Check After compiling the
and refining content rather than validating com-             initial annotations (100 papers), these were set
plex logical relationships. Similarly, tools like            aside before evaluating the models to ensure an
AIGS (Liu et al., 2024) and LLM-Assisted Hy-                 unbiased assessment of their capabilities. To en-
pothesis Generation (Vladika and Matthes, 2023)              hance the reliability of our dataset as ground truth,
explore reasoning and hypothesis testing but do not          we conducted a validation phase where a different
directly tackle the problem of scientific comprehen-         set of annotators re-annotated a subset of 30 pa-
sion. (Leng et al., 2024) introduce a graph-based            pers.We measured inter–annotator agreement with
approach for hypothesis generation and evaluation,           two metrics. (1) F1: Averaging symmetric F1
demonstrating potential for structured creativity,           across annotator pairs gives substantial agreement
yet falling short of validating interlinked arguments        for claims (0.755) and moderate agreement for ev-
at scale.                                                    idence (0.659) and claim–evidence links (0.617).
                                                             (2) Cohen’s κ: Averaging κ across pairs yields
Ethical AI Finally, ethical considerations have
                                                             0.66 for claims (substantial) and 0.30 for evidence
been raised in works like Ethical Use of LLMs
                                                             (fair). Together, these scores confirm that CLAIM-
(Lissack and Meagher, 2024), which stresses the
                                                             BENCH is a reliable yet challenging benchmark
need for transparency and accountability in AI-
                                                             (details in Appendix B.2).
driven research, and multimodal benchmarks like
MileBench (Dingjie et al., 2024), which expand               3.2   Evaluation Metrics
the scope of LLM evaluation to include visual and
                                                             In this study, we employ four metrics to evaluate
textual data. These efforts, while addressing impor-
                                                             the LLM performance: three established metrics
tant aspects of AI integration in research, highlight
                                                             in information retrieval, precision, recall, F1-score,
the absence of targeted benchmarks that evaluate
                                                             and a novel metric, sentence_gap, to evaluate LLM
claim-evidence validation across long, complex sci-
                                                             performance in claim-evidence retrieval tasks and
entific texts—a gap CLAIM-BENCH aims to fill.
                                                             the effectiveness of our various prompting tech-
3     Methodology                                            niques.

In this section, we present the design of CLAIM-             Precision (P) Used to measure the proportion of
BENCH, our benchmark for evaluating how well                 spans the model predicts that are identified by the
LLMs identify and analyze claim–evidence rela-               annotators, reflecting their effectiveness in respond-
tionships in full-length research papers.                    ing to precise and carefully structured prompts.

3.1    Dataset                                                                        TP
                                                                              P =           ,                  (1)
                                                                                    TP + FP
Dataset Curation The dataset for this study was
curated by 4 PhD students with research experience.          where TP (true positive) is the number of correctly
Each annotator had at least one first-author confer-         retrieved claim/evidence, and FP (false positive)
ence publication, ensuring familiarity with scien-           is the number of retrieved “claim”/“evidence” that
tific writing standards. These researchers selected          are not claims/evidences.



 Single-Pass
                        single
                       prompt                   Claims
                                 Æ             ✓ Evidence
  @Research Paper
                                 LLM
                                              ⋆ Conclusions


 Three-Pass
                       claims                           evidence                                conclusion
                       prompt                            prompt                                   prompt
                                 Æ                                 Æ                                         Æ
  @Research Paper                             Claims                           ✓ Evidence                             ⋆ Conclusions
                                 LLM                               LLM                                       LLM


 One-by-One Pass
                       claims
                       prompt
                                 Æ
  @Research Paper                             Claims
                                 LLM


               Phase 1: Extract All Claims

                   evidence                                                              conclusion
                    prompt                                                                 prompt
                              Æ                                                                       Æ
      Claim 1                            ✓ Evidence. 1                  _ Claim-Evi 1                             ⋆ Conc. 1
                        LLM                                                                           LLM
         ..       ..       ..          ..       ..      ..
               evidence                                                                  conclusion
          .        .
                prompt
                            .           .        .       .                                 prompt
                        Æ                                                                             Æ
      Claim n                            ✓ Evidence. n                  _ Claim-Evi n                             ⋆ Conc. n
                              LLM                                                                     LLM


                     Phase 2: Extract Evidence & Form C-E Pairs                               Phase 3: Generate Conclusions


Figure 1: Three methods to prompt LLMs to analyze the papers. Single-Pass: Full paper processing with one
prompt. Three-Pass: Sequential claim → evidence → conclusion extraction. One-by-One Pass: Individual
evidence retrieval per claim.


Recall (R) Quantifying the portion of claim/evi-                         comprehension and is instrumental as we explore
dence that are retrieved. Recall assesses the ability                    how increasing LLM context length capabilities
to capture pertinent data, a measure of the model’s                      enhance performance in realistic scenarios.
responsiveness to exhaustive prompt inquiries                                              1     X
                                                                          sentence_gap =                 s(p) − s(g) , (3)
                                TP                                                        |M|
                                                                                                             (p,g)∈M
                     R=               ,                      (2)
                              TP + FN                                    where M is the set of matched evidence pairs (us-
where FN (false negative) is the number of claim-                        ing Intersection over Union matching rule). s(·)
s/evidences that are incorrectly missed.                                 returns the sentence index of a span inside the doc-
                                                                         ument. The sentence_gap metric is therefore the
F1-score This is the harmonic mean of P and R.                           average absolute sentence-level distance between
The F1-score provides a balanced measure of ac-                          each predicted claim span p and its evidence span
curacy, crucial for evaluating the efficacy of the                       g, capturing how far a model must reason across
prompting techniques in eliciting detailed and rele-                     the paper to link claims with supporting evidence.
vant responses.
                                                                         Secondary metrics Additionally, we consider
sentence_gap The sentence_gap metric mea-                                secondary metrics that focus on operational aspects
sures the distance between a retrieved claim and                         of model performance: the time to generate out-
each of its associated retrieved evidence. It is par-                    puts and how each model’s recall changes as input
ticularly valuable for evaluating long-range con-                        length (token count) increases. These metrics are
textual comprehension by quantitatively assess-                          crucial for understanding efficiency and scalability.
ing models’ ability to handle textual relationships                      They help compare how models manage computa-
over extended contexts. This assessment is crucial                       tional resources and handle large input sizes under
for complex prompts designed to challenge such                           varying conditions.



                                                    Models                                                                                Strategies                                                                             Content Type & F1 Score
                    GPT-4-Turbo                              Llama-3.1-Nemotron-70B-Instruct-HF                   Single-Pass               Three-Pass                 One-by-One                                      Claim (dark outline)                      F1 = 0.5
                    Claude-3-5-sonnet-20241022               Ministral-8B-Instruct-2410                                                                                                                                Evidence (transparent, no outline)        F1 = 0.7
                    Gemini-1.0-pro                           Phi-3.5-MoE-instruct                                                                                                                                      F1 = 0.3


            0.7

                                                                                 GPT
                                                                                                                                                                                                                               F1=0
                                                                                                                                                                                                                                   .7
                                                                                                                                     Claude
            0.6                                                                                                                 LLaMA


                                                                                                                                                                           F1=0
                                                                                                                                                                               .6


            0.5
                                                                                                                                                                   Gemini
                                                                             GPT (E)                               F1=0
                                                                                                                          .5


Precision
                                                                             LLaMA (E)                                                                                                  LLaMA
            0.4
                                                                                                                                                           Ministral    Claude (E)
                                                                                                                                                                                                                 Phi       GPT          Claude

                                                                                                                                Claude (E)                                                                                                                  Claude
                                                                                                                                               LLaMA (E)                                              GPT (E)
                                                                                                                                                                                         Gemini
                                                                                                                                                                                     Gemini
                                                                                                               Gemini (E)                                                                                                                                                   GPT
                                                                                              Ministral (E)         F1=0.4
            0.3


                                                                                                                                                                 Phi (E)
                                                                                                                                                                                         Gemini (E)                               Phi
                                       Gemini (E)                                                                                                                                                                           LLaMA
                                                                                                                                                                                                                       Ministral GPT (E)          Phi
            0.2                                                                                                                  F1=0.3
                                                                                                              Ministral (E)          Phi (E)
                                                                                                                                                                                                        Claude (E)

                                                                                                                                                                   LLaMA (E)

                                                                                                         Phi (E)
            0.1
                                 0.4                                                   0.5                                                     0.6                                                0.7                                             0.8
                                                                                                                                          Recall

Figure 2: Precision vs. Recall for claim (solid markers) and evidence (transparent markers) identification across
models and strategies (shapes: Single-Pass •, Three-Pass ▲, One-by-One ■). Models show higher precision for
claims, higher recall for evidence, with most results below F1 = 0.7.


4                 Experimental Setup                                                                                                                 stage, where separate prompts elicit correspond-
                                                                                                                                                     ing evidences. Finally, we combine the identified
We evaluate six state-of-the-art LLMs, chosen
                                                                                                                                                     claims and evidences, using another prompt to ex-
to span both licensing regimes and architec-
                                                                                                                                                     tract conclusions (Appendix A.2).
tural families while sharing a ≥128K-token con-
text window. Open-source include Ministral-8B                                                                                                        One-by-One Pass We adopt a more granular ap-
(Mistral AI, 2024), Phi-3.5-MoE (Abdin et al.,                                                                                                       proach where each claim is processed individually
2024), and LLaMA-70B (Wang et al., 2025) and                                                                                                         to retrieve evidence. This means for n claims, the
Closed-source includes GPT-4 (OpenAI, 2024),                                                                                                         model runs n times to gather evidence for each, and
Gemini-Exp_1114 (Gemini Team, 2024), and                                                                                                             similarly for conclusions. Although this approach
Claude 3.5 Sonnet (Anthropic, 2025).                                                                                                                 provides detailed analysis, it significantly increases
                                                                                                                                                     the demand on computational resources and time
4.1                Analysis Methods
                                                                                                                                                     (Appendix A.3). These methods combine care-
As illustrated in Figure 1, we explore three dis-                                                                                                    ful prompting with our annotated claim–evidence
tinct prompting methods to assess and enhance                                                                                                        dataset, allowing us to benchmark each model’s ex-
model performance on claim-evidence identifica-                                                                                                      traction accuracy and probe how different prompt
tion tasks.                                                                                                                                          strategies improve performance.
Single-Pass Initially, we present the models with
a research paper, instructing (Appendix A.1) them
                                                                                                                                                     5        Results
to identify claims, evidences, and conclusions in a                                                                                                  The following section details the experimental re-
single comprehensive prompt.                                                                                                                         sults, highlighting comparative model performance
Three-Pass Building on the “divide and conquer”                                                                                                      and strategic impacts.
strategy from prior research, we then deconstruct
                                                                                                                                                     5.1          Precision vs Recall
the task into sequential stages. In the first stage, the
model identifies claims using a dedicated prompt.                                                                                                    As shown in Figure 2, models exhibit a clear
Subsequently, these claims are supplied to the next                                                                                                  precision-recall trade-off: settings that achieve



Figure 3: Sentence distance distribution (box plots) between claims and linked evidence vs. Human baseline
(leftmost). LLMs, especially with iterative strategies, link over longer distances than humans, showing capability
but potential noise.


higher recall often incur reduced precision. For in-          5.2   Smaller vs Larger Models
stance, Claude and LLaMA achieve high recall but
at the cost of extracting numerous false positives,
                                                              Larger models, such as GPT-4-Turbo, Claude,
which is evident from their large maximum linking
                                                              Gemini, and LLaMA, generally exhibit strong
distances (Figure 7), exceeding 2,200 sentences in
                                                              recall in identifying claims, with GPT-4-Turbo
some cases. Although valuable, such long-range
                                                              achieving high precision (0.68) and recall (0.81),
links raise the risk of false claim–evidence pairs.
                                                              demonstrating effective balance at different strate-
Conversely, models like GPT prioritize precision,
                                                              gies. Claude also shows strong recall (0.83), al-
maintaining moderate linking distances (around
                                                              beit with a moderate precision drop (0.61). Also,
658–708 sentences) with fewer spurious matches,
                                                              LLaMA achieves similar recall (0.76) but compara-
though this approach slightly limits recall. Minis-
                                                              tive precision (0.60), indicating a tendency to iden-
tral offers a balanced precision-recall profile, char-
                                                              tify extensive and highly precise connections, con-
acterized by consistent, shorter linking distances.
                                                              sidering the best cases of each model.
                                                                 Smaller models, such as Ministral and Phi, typi-
   Comparing the precision-recall tradeoff trends             cally exhibit lower recall and precision. Ministral
between open- and closed-source models, we see                shows modest recall (0.60) with precision around
that closed-source models balance precision and               0.38, reflecting a conservative approach to claim-
recall better. Overall, GPT often balances high pre-          evidence linking. Phi demonstrates similar preci-
cision and moderate recall; Claude achieves higher            sion (approximately 0.39) but notably higher recall
recall rates but exhibits noticeable trade-offs in pre-       (around 0.7) in the best cases. These observations
cision. Gemini remains stable across strategies.              highlight a clear trade-off: larger models generally
Among open-source models, LLaMA came close                    identify broader and more nuanced claim–evidence
to matching closed-source recall but with some out-           relationships but often at the cost of precision,
liers, also shows variability in precision; Ministral         whereas smaller models maintain more consistent
is moderate in both coverage & precision; Phi ex-             precision with significantly reduced recall. In both
hibits the widest swings, at times matching larger            the cases similar pattern holds in evidence extrac-
models but also dropping in accuracy.                         tion as well.



                                       Prompt Strategy
                                            3-pass
                                            1-pass                            2036s                                                     1395s                                      2642s
                                            1-by-1
                                            Overall mean: 548.5s


   Execution Time (seconds)

                                                     814s
                                                                       682s
                                                                                                            613s                                                     615s


                              400                                                                                                               333s
                                                               303s                                                      307s                                 300s          296s

                              200    163s                                                                                        161s
                                                                                                                                                       111s
                                              60s                                            46s    31s
                                0            GPT                      Gemini                       Claude                       LLaMA              Ministral                Phi
       Note: Plot capped at 1600 seconds. 117 extreme outliers were filtered.
                                                                                                               Model

Figure 4: Execution time comparison (box plots): Single-Pass (■) is fastest, One-by-One (■) is slowest. Models
vary greatly in speed (e.g., Claude consistently fast; LLaMA/Phi often requiring >1000s).


5.3                       Claims vs Evidence Extraction                                                            approach.

                                              Best C Performances             Best E Performances                  5.4      Impact of Strategy
 Model
                                               F1     P      R                 F1     P      R
 GPT-4-Turbo                                  0.56      0.66    0.57          0.47    0.34         0.69
                                                                                                                   The Single-pass strategy is highly efficient but has
 Claude 3.5                                   0.59      0.62    0.60          0.42    0.33         0.66            limited coverage, e.g., GPT-4 produces 152 pairs
 Gemini-Exp_1114                              0.54      0.48    0.64          0.40    0.30         0.52
 LLaMA-70B                                    0.58      0.60    0.56          0.45    0.42         0.49            with a 98.5 average sentence_gap, while Ministral
 Ministral-8B                                 0.48      0.39    0.61          0.39    0.31         0.52            generates 166 pairs (average gap: 64.2). Mean-
 Phi-3.5-MoE                                  0.50      0.40    0.72          0.35    0.25         0.63
                                                                                                                   while, the Three-pass strategy enhances recall and
Table 1: The highest performance (across all strategies)                                                           coverage at moderate computational cost. Claude
for Claim (C) and Evidence (E) extraction; “P@R” de-                                                               yields 174 pairs (average gap: 122.2), and Phi
notes precision at the corresponding recall.                                                                       captures 279 pairs, albeit with significant vari-
                                                                                                                   ance (11,490.2) in sentence_gap. Finally, the One-
   Analyzing claim versus evidence extraction sep-                                                                 by-One strategy maximizes recall but increases
arately reveals distinct performances among LLMs                                                                   computational demand significantly. Claude and
(see Table 1). Across all models, precision is con-                                                                LLaMA produce the highest counts (639 and 659
sistently higher for claims than for evidence, in-                                                                 pairs, respectively), with substantial gaps (Claude:
dicating the models more readily detect explicit                                                                   119.4, LLaMA: 95.1) and high variance (Claude:
claims compared to the contextually dispersed evi-                                                                 33,673.9, LLaMA: 34,207.0). Phi also achieves
dence. Also, the evidence extraction of all models                                                                 substantial coverage (347 pairs) with notable vari-
yields higher recall than precision. In addition to                                                                ance (13,188.2).
the common trends, the models exhibit distinct
patterns. For instance, Claude and LLaMA ex-                                                                       5.5      Impact of Token Length on Recall
hibit high recall in evidence extraction but with                                                                  We observed how the documents’ token length af-
substantial variability in linking distances (Claude:                                                              fected the models’ recall performances. In long
mean gap of 119.4 sentences, variance of 33,674;                                                                   documents, we expected performance drops, but
LLaMA: mean 95.1 sentences, variance of 34,207),                                                                   these observed drops are tied to the prompting strat-
suggesting increased noise and inconsistent perfor-                                                                egy. With the Single-pass strategy, the recall perfor-
mance. Conversely, Ministral maintains lower link-                                                                 mances dropped as the document length increased.
ing distances (mean 75.9 sentences) with minimal                                                                   With the iterative prompting strategies (Three-pass
variance, signifying a more cautious and controlled                                                                or One-by-One), the performance drops are less



significant, indicating that the iterative prompting        applications leveraging the capabilities of LLMs
imposes less “processing load” onto the LLMs. Ad-           in scientific claim-evidence reasoning. Improv-
ditionally, the recall drops differ by the sizes of         ing LLMs’ ability to accurately validate claim-
the models. Relatively smaller models (LLaMA                evidence pairs could enhance their practical use
70B and Ministral 8B) showed more notable de-               in designing experiments and generating scientif-
clines, especially with Single-pass, whereas the            ically valid hypotheses. Furthermore, improved
larger models (Claude and GPT-4) maintained rel-            claim identification and validation methods provide
atively high recalls, underlining the advantage of          a foundation for developing sophisticated claim
their long context capabilities. Additional details         quality scoring tools that can greatly enhance peer-
in Appendix C.                                              review processes. The capability to systemati-
   Claude and LLaMA frequently produce the high-            cally link and integrate evidence across multiple
est pair counts (up to 639 and 659), reflecting broad       scientific papers could lead to powerful retrieval-
coverage. This can coincide with their large context        augmented laboratory assistants and cross-paper
window sizes—helpful for capturing distant rela-            evidence graphs, accelerating knowledge discovery.
tionships—yet also introduces potential noise. GPT          These advancements would not only strengthen the
and Gemini keep moderate distances, suggesting              robustness of scientific validations but also facil-
they discovered fewer links. Ministral remains con-         itate the creation of more sophisticated scientific
servative with fewer pairs with shorter distances,          QA systems, thus laying foundational benchmarks
while Phi’s extreme variance indicates inconsistent         for future scientific text generation and evaluation
linking across long contexts. We include the details        methods. This research thus serves as a pivotal
in Figure 7 (in Appendix C).                                foundation for transformative applications in scien-
                                                            tific inquiry and discourse.
5.6    Execution Time Analysis
As shown in Figure 4, the execution times differ
                                                            7   Conclusion
considerably across models and strategies. GPT
is highly efficient in the Single-Pass (under 200s)
and relatively moderate in one-by-one approaches            Motivated by the limited evaluation in prior litera-
(∼500s). Gemini exhibits intermediate execu-                ture of LLMs’ abilities in scientific reasoning, we
tion times across all strategies, notably higher            introduced CLAIM-BENCH, a novel benchmark
for the three-pass (∼600s). Claude consistently             specifically designed to evaluate LLMs’ capabili-
achieves the fastest execution across all strate-           ties in identifying and validating claim-evidence
gies, maintaining execution times under 200 sec-            relationships within scientific texts. We system-
onds. LLaMA shows extensive variability, espe-              atically explored diverse LLM architectures and
cially with one-by-one strategies frequently exceed-        prompting strategies. Our results demonstrate
ing 1,200 seconds, reflecting significant computa-          significant limitations in LLMs’ comprehension,
tional demands. Ministral shows relatively bal-             specifically in their precision and recall balance
anced execution times, with three-pass and one-             when processing complex scientific documents.
by-one strategies averaging around 600–900 sec-             Notably, models showed higher precision in extract-
onds. Phi demonstrates the highest computational            ing explicit claims, whereas extracting dispersed
intensity, especially in one-by-one strategies, often       evidence proved challenging, yielding higher re-
surpassing 1,200 seconds, highlighting the consid-          call but lower precision and increased sentence
erable resource investment required for thorough            gaps. Moreover, our comparative analysis across 3
analyses. The execution times recorded for Gem-             strategies revealed substantial trade-offs between
ini exhibit some variability, which may partially           computational efficiency, precision, and coverage.
stem from fluctuations in API response latency dur-         Closed-source models generally displayed more
ing our experiments, combined with the necessary            stable performances, while open-source models
sleep() intervals implemented for rate limiting.            offered broad yet inconsistent coverage. CLAIM-
                                                            BENCH provides a framework for the assessment
6     Discussion                                            of LLMs in complex scientific contexts, and our
                                                            study provides useful material and insights for con-
The insights from CLAIM-BENCH emphasize crit-               tinuing the advancement in LLMs’ high-level com-
ical directions for future research and practical           prehension and scientific reasoning capabilities.



8   Limitations                                               Marta R. Costa-jussà, Pierre Andrews, Mariano Co-
                                                               ria Meglioli, Joy Chen, Joe Chuang, David Dale,
While CLAIM-BENCH provides comprehensive                       Christophe Ropers, Alexandre Mourachko, Ed-
insights into the capabilities of LLMs in scientific           uardo Sánchez, Holger Schwenk, Tuan Tran, Arina
claim-evidence reasoning. Despite these insights,              Turkatenko, and Carleigh Wood. 2024a. LCFO:
                                                               Long Context and Long Form Output Dataset and
CLAIM-BENCH has several limitations worth not-                 Benchmarking. arXiv preprint. ArXiv:2412.08268.
ing. First, the benchmark primarily focuses on
recent papers from select domains, which are after            Marta R. Costa-jussà, Joy Chen, Ifeoluwanimi Ade-
                                                               bara, Joe Chuang, Christophe Ropers, and Eduardo
the LLMs’ knowledge cutoff but might limit the                 Sánchez. 2024b. Y-NQ: English-Yorùbá Evaluation
generalizability. Second, the evaluation relies on             dataset for Open-Book Reading Comprehension and
existing LLM architectures. While we leave the                 Text Generation. arXiv preprint. ArXiv:2412.08279.
exploration of the impact of model architecture de-           Song Dingjie, Shunian Chen, Guiming Hardy Chen,
velopment to future works, CLAIM-BENCH could                    Fei Yu, Xiang Wan, and Benyou Wang. 2024.
be a useful material that supports future projects              MileBench: Benchmarking MLLMs in Long Context.
that develop novel LLM architectures that have                  In First Conference on Language Modeling.
enhanced long-context language understanding ca-              Gemini Team. 2024. Gemini 1.5: Unlocking multi-
pabilities and scientific reasoning capabilities.               modal understanding across millions of tokens of
                                                                context. Preprint, arXiv:2403.05530.
                                                              Aditi Godbole, Jabin Geevarghese George, and Smita
References                                                      Shandilya. 2024. Leveraging Long-Context Large
Marah Abdin, Jyoti Aneja, and Hany Awadalla et al.              Language Models for Multi-Document Understand-
 2024. Phi-3 technical report: A highly capable                 ing and Summarization in Enterprise Applications.
 language model locally on your phone. Preprint,                arXiv preprint. ArXiv:2409.18454.
 arXiv:2404.14219.
                                                              Sirui Hong, Yizhang Lin, Bang Liu, Bangbang
Shubham Agarwal, Gaurav Sahu, Abhay Puri, Issam H.               Liu, Binhao Wu, Ceyao Zhang, Chenxing Wei,
  Laradji, Krishnamurthy DJ Dvijotham, Jason Stanley,            Danyang Li, Jiaqi Chen, Jiayi Zhang, Jinlin Wang,
  Laurent Charlin, and Christopher Pal. 2025. LitLLM:            Li Zhang, Lingyao Zhang, Min Yang, Mingchen
  A Toolkit for Scientific Literature Review. arXiv              Zhuge, Taicheng Guo, Tuo Zhou, Wei Tao, Xiangru
  preprint. ArXiv:2402.01788.                                    Tang, Xiangtao Lu, Xiawu Zheng, Xinbing Liang,
                                                                 Yaying Fei, Yuheng Cheng, Zhibin Gou, Zongze
Anthropic. 2025. Claude 3.5 sonnet model card adden-             Xu, and Chenglin Wu. 2024. Data Interpreter:
  dum. PDF file. Accessed 12 Apr. 2025.                          An LLM Agent For Data Science. arXiv preprint.
                                                                 ArXiv:2402.18679.
Zhiyuan Chang, Mingyang Li, Xiaojun Jia, Junjie Wang,
  Yuekai Huang, Qing Wang, Yihao Huang, and Yang              Yiqiao Jin, Qinlin Zhao, Yiyang Wang, Hao Chen, Kai-
  Liu. 2024. What External Knowledge is Preferred               jie Zhu, Yijia Xiao, and Jindong Wang. 2024. Agen-
  by LLMs? Characterizing and Exploring Chain                   tReview: Exploring Peer Review Dynamics with
  of Evidence in Imperfect Context. arXiv preprint.             LLM Agents. arXiv preprint. ArXiv:2406.12708.
  ArXiv:2412.12632.
                                                              Yan Leng, Hao Wang, and Yuan Yuan. 2024. Llm-
Alessandro Checco, Lorenzo Bracciale, Pierpaolo                 Assisted Hypothesis Generation and Graph-Based
  Loreti, Stephen Pinfield, and Giuseppe Bianchi. 2021.         Evaluation.
  AI-assisted peer review. Humanities and Social Sci-
  ences Communications, 8(1):1–11.                            YUCHENG LI, Huiqiang Jiang, Qianhui Wu, Xufang
                                                               Luo, Surin Ahn, Chengruidong Zhang, Amir H. Abdi,
Ziru Chen, Shijie Chen, Yuting Ning, Qianheng Zhang,           Dongsheng Li, Jianfeng Gao, Yuqing Yang, and Lili
   Boshi Wang, Botao Yu, Yifei Li, Zeyi Liao, Chen             Qiu. 2025. SCBench: A KV Cache-Centric Analysis
  Wei, Zitong Lu, Vishal Dey, Mingyi Xue, Frazier N.           of Long-Context Methods. In The Thirteenth Inter-
   Baker, Benjamin Burns, Daniel Adu-Ampratwum,                national Conference on Learning Representations.
   Xuhui Huang, Xia Ning, Song Gao, Yu Su, and Huan
   Sun. 2025. ScienceAgentBench: Toward Rigorous              Yutong Li, Lu Chen, Aiwei Liu, Kai Yu, and Lijie Wen.
   Assessment of Language Agents for Data-Driven Sci-           2025. ChatCite: LLM Agent with Human Workflow
   entific Discovery. In The Thirteenth International           Guidance for Comparative Literature Summary. In
   Conference on Learning Representations.                      Proceedings of the 31st International Conference on
                                                                Computational Linguistics, pages 3613–3630, Abu
Konstantin Chernyshev, Vitaliy Polshkov, Ekaterina              Dhabi, UAE. Association for Computational Linguis-
  Artemova, Alex Myasnikov, Vlad Stepanov, Alexei               tics.
  Miasnikov, and Sergei Tilga. 2025. U-MATH:
  A University-Level Benchmark for Evaluating                 Michael Lissack and Brenden Meagher. 2024. Ethical
  Mathematical Skills in LLMs. arXiv preprint.                  Use of Large Language Models in Academic Re-
  ArXiv:2412.03205.                                             search and Writing: A How-To.



Houjiang Liu, Jacek Gwizdka, and Matthew Lease.                   Wanli Ouyang, Philip Torr, Bowen Zhou, and Nan-
  2025.    Exploring Multidimensional Checkwor-                   qing Dong. 2025. Many Heads Are Better Than
  thiness: Designing AI-assisted Claim Prioritiza-                One: Improved Scientific Idea Generation by A
  tion for Human Fact-checkers. arXiv preprint.                   LLM-Based Multi-Agent System. arXiv preprint.
  ArXiv:2412.08185.                                               ArXiv:2410.09403.

Ryan Liu and Nihar B. Shah. 2023. ReviewerGPT?                Lu Sun, Aaron Chan, Yun Seo Chang, and Steven P.
  An Exploratory Study on Using Large Language                  Dow. 2024a. ReviewFlow: Intelligent Scaffolding to
  Models for Paper Reviewing.     arXiv preprint.               Support Academic Peer Reviewing. In Proceedings
  ArXiv:2306.00622.                                             of the 29th International Conference on Intelligent
                                                                User Interfaces, pages 120–137, Greenville SC USA.
Zijun Liu, Kaiming Liu, Yiqi Zhu, Xuanyu Lei, Zong-             ACM.
   han Yang, Zhenhe Zhang, Peng Li, and Yang
   Liu. 2024. AIGS: Generating Science from AI-               Lu Sun, Stone Tao, Junjie Hu, and Steven P. Dow. 2024b.
   Powered Automated Falsification. arXiv preprint.             MetaWriter: Exploring the Potential and Perils of AI
   ArXiv:2411.11910.                                            Writing Support in Scientific Peer Review. Proceed-
                                                                ings of the ACM on Human-Computer Interaction,
Chris Lu, Cong Lu, Robert Tjarko Lange, Jakob Foer-             8(CSCW1):1–32.
  ster, Jeff Clune, and David Ha. 2024. The AI Scien-
  tist: Towards Fully Automated Open-Ended Scien-             Juraj Vladika and Florian Matthes. 2023. Scientific Fact-
  tific Discovery. arXiv preprint. ArXiv:2408.06292.             Checking: A Survey of Resources and Approaches.
                                                                 arXiv preprint. ArXiv:2305.16859.
Xiaoliang Luo, Akilles Rechardt, Guangzhi Sun,
  Kevin K. Nejad, Felipe Yáñez, Bati Yilmaz, Kangjoo          Zhilin Wang, Alexander Bukharin, Olivier Delal-
  Lee, Alexandra O. Cohen, Valentina Borghesani, An-            leau, Daniel Egert, Gerald Shen, Jiaqi Zeng, Olek-
  ton Pashkov, Daniele Marinazzo, Jonathan Nicholas,            sii Kuchaiev, and Yi Dong. 2025. Helpsteer2-
  Alessandro Salatiello, Ilia Sucholutsky, Pasquale             preference: Complementing ratings with preferences.
  Minervini, Sepehr Razavi, Roberta Rocca, Elkhan               Preprint, arXiv:2410.01257.
  Yusifov, Tereza Okalova, Nianlong Gu, Martin Fe-
                                                              Yixuan Weng, Minjun Zhu, Guangsheng Bao, Hongbo
  rianc, Mikail Khona, Kaustubh R. Patil, Pui-Shee
                                                                Zhang, Jindong Wang, Yue Zhang, and Linyi Yang.
  Lee, Rui Mata, Nicholas E. Myers, Jennifer K. Biz-
                                                                2025. CycleResearcher: Improving Automated Re-
  ley, Sebastian Musslick, Isil Poyraz Bilgin, Guiomar
                                                                search via Automated Review. In The Thirteenth
  Niso, Justin M. Ales, Michael Gaebler, N. Apurva
                                                                International Conference on Learning Representa-
  Ratan Murty, Leyla Loued-Khenissi, Anna Behler,
                                                                tions.
  Chloe M. Hall, Jessica Dafflon, Sherry Dongqi Bao,
  and Bradley C. Love. 2025. Large language mod-              Yuhao Wu, Ming Shan Hee, Zhiqiang Hu, and Roy
  els surpass human experts in predicting neuroscience          Ka-Wei Lee. 2025. LongGenBench: Benchmarking
  results. Nature Human Behaviour, 9(2):305–315.                Long-Form Generation in Long Context LLMs. In
                                                                The Thirteenth International Conference on Learning
Yubo Ma, Yuhang Zang, Liangyu Chen, Meiqi Chen,                 Representations.
  Yizhu Jiao, Xinze Li, Xinyuan Lu, Ziyu Liu, Yan
  Ma, Xiaoyi Dong, Pan Zhang, Liangming Pan, Yu-
  Gang Jiang, Jiaqi Wang, Yixin Cao, and Aixin Sun.
  2024. MMLONGBENCH-DOC: Benchmarking
                                                              A     Prompt Templates
  Long-context Document Understanding with Visual-
  izations. In The Thirty-eight Conference on Neural
  Information Processing Systems Datasets and Bench-
  marks Track.

Mistral AI. 2024. Un Ministral, des Ministraux: In-
  troducing the world’s best edge models. https://
  mistral.ai/news/ministraux. Accessed 19 May
  2025.

Xuanfan Ni, Hengyi Cai, Xiaochi Wei, Shuaiqiang
  Wang, Dawei Yin, and Piji Li. 2024. XL$^2$Bench:
  A Benchmark for Extremely Long Context Under-
  standing with Long-range Dependencies. arXiv
  preprint. ArXiv:2404.05446.

OpenAI. 2024. GPT-4 Technical Report. arXiv preprint.
  ArXiv:2303.08774.

Haoyang Su, Renqi Chen, Shixiang Tang, Zhenfei Yin,
  Xinzhe Zheng, Jinzhe Li, Biqing Qi, Qi Wu, Hui Li,



A.1   Single-Pass Prompt


  Comprehensive Evaluation Prompt

  Analyze the research paper and provide a comprehensive evaluation following these guide-
  lines:

      1. Identify ALL claims in the paper where each claim:
            • Makes a specific, verifiable assertion
            • Is supported by concrete evidence
            • Represents findings, contributions, or methodological advantages
            • Can be from any section except abstract

      2. For each identified claim:
            • Extract ALL supporting or contradicting evidence (experimental results, data, or method-
              ology)
            • Evaluate the evidence strength and limitations
            • Assess how well conclusions align with evidence

  Return ONLY the following JSON structure:
  {
       "analysis": [
           {
              "claim_id": number,
              "claim": {
                  "text": "statement of the claim",
                  "type": "methodology/result/contribution/performance",
                  "location": "section/paragraph",
                  "exact_quote": "verbatim text from paper"
              },
              "evidence": [
                  {
                      "evidence_text": "specific experimental result/data",
                      "strength": "strong/moderate/weak",
                      "limitations": "specific limitations",
                      "location": "section/paragraph",
                      "exact_quote": "verbatim text from paper"
                  }
              ],
              "evaluation": {
                  "conclusion_justified": true/false,
                  "robustness": "high/medium/low",
                  "justification": "explanation of evidence-conclusion alignment",
                  "key_limitations": "critical limitations affecting validity",
                  "confidence_level": "high/medium/low"
              }
           }
       ]
  }

  Ensure:

       • ALL substantive claims are captured

       • Evaluations are objective and well-reasoned

       • All locations and quotes are precise

       • Multiple pieces of evidence per claim are included when present



A.2   Three-Pass Prompt
  Claims Extraction Prompt

  Paper text: {text}
  Task: Identify all statements in the text that meet the following criteria for a claim:

      1. Makes a specific, testable assertion about results, methods, or contributions.

      2. Represents a novel finding, improvement, or advancement.

      3. Presents a clear position or conclusion.

  Requirements:

       • Include both major and minor claims.

       • Don’t miss any claims.

       • Present each claim as a separate item.

  Return ONLY the following JSON structure:
  {
       "claims": [
           {
              "claim_id": 1,
              "claim_text": "statement of the claim",
              "location": "section/paragraph where this claim appears",
              "claim_type": "Nature of the claim",
              "exact_quote": "complete verbatim text containing the claim"
           }
       ]
  }


  Evidence Identification Prompt

  Paper text: {text}
  For these claims: {claims_text}
  Please identify relevant evidence that:
      1. Directly supports or contradicts the claim’s specific assertion.

      2. Is presented with experimental results, data, or concrete examples.

      3. Can be traced to specific methods, results, or discussion sections.

      4. Is not from the abstract or introduction.
  Return ONLY the following JSON:
  {
       "evidence_sets": [
           {
              "claim_id": number,
              "evidence": [
                  {
                     "evidence_id": number,
                     "evidence_text": "specific evidence",
                     "strength": "strong/moderate/weak",
                     "limitations": "key limitations",
                     "location": "section/paragraph",
                     "exact_quote": "verbatim text"



                   }
               ]
           }
       ]
  }


  Conclusion Evaluation Prompt

  Analyze these claims and their evidence: {analysis_text}
  For each claim-evidence pair, evaluate:

      1. Whether the evidence justifies the claim.

      2. The overall strength of support.

      3. Any important limitations.

  Return ONLY the following JSON:
  {
       "conclusions": [
           {
              "claim_id": number,
              "conclusion_justified": true/false,
              "robustness": "high/medium/low",
              "key_limitations": "specific limitations",
              "confidence_level": "high/medium/low"
           }
       ]
  }


A.3   One-by-One Prompt
  Claims Extraction Prompt

  Analyze this research paper and extract ALL possible claims made by the authors. Paper text:
  {text}
  Your task is to identify all statements in the text that meet the following criteria for a claim:

      1. Makes a specific, testable assertion about results, methods, or contributions.

      2. Represents a novel finding, improvement, or advancement.

      3. Presents a clear position or conclusion.

  Make sure to:

       • Include both major and minor claims.

       • Don’t miss any claims.

       • Present each claim as a separate item.

  Return ONLY the following JSON structure:
  {
       "claims": [
           {



             "claim_id": 1,
             "claim_text": "statement of the claim",
             "location": "section/paragraph where this claim appears",
             "claim_type": "Nature of the claim",
             "exact_quote": "complete verbatim text containing the claim"
         }
     ]
}


Evidence Analysis Prompt

Paper text: {text}
For the following claim from the paper: "{claim[’claim_text’]}"
Please identify relevant evidence that:

    1. Directly supports or contradicts the claim’s specific assertion.

    2. Is presented with experimental results, data, or methodology.

    3. Can be traced to specific methods, results, or discussion sections.

    4. Is not from the abstract or introduction.

If NO evidence is found for the given Claim, return:
{
     "claim_id": {claim['claim_id']},
     "evidence": [],
     "no_evidence_reason": "Explain why no evidence was found (e.g., 'Claim is unsupported', '
         ,→ Claim is theoretical without empirical evidence', etc.)"
}

ELSE: Return ONLY the following JSON structure:
{
     "claim_id": {claim['claim_id']},
     "evidence": [
         {
            "evidence_id": 1,
            "evidence_text": "specific experimental result/data point",
            "evidence_type": "primary/secondary",
            "strength": "strong/moderate/weak",
            "limitations": "stated limitations or assumptions",
            "location": "specific section & paragraph",
            "exact_quote": "verbatim text from paper"
         }
     ]
}


Conclusion Analysis Prompt

Paper text: {text}
Analyze the following claim and its supporting evidence: {single_claim_analysis}
Provide a comprehensive conclusion analysis following these guidelines:

    1. Evidence Assessment:
          • Evaluate the strength and quality of ALL evidence presented.
          • Consider both supporting and contradicting evidence.
          • Assess the methodology and reliability of evidence.



    2. Conclusion Analysis:
         • Determine what the authors concluded about this specific claim.
         • Evaluate if the conclusion is justified by the evidence.
         • Consider the relationship between evidence quality and conclusion strength.

    3. Robustness Evaluation:
         • Assess how well the evidence supports the conclusion.
         • Consider methodological strengths and weaknesses.
         • Evaluate the consistency of evidence.

    4. Limitations Analysis:
         • Identify specific limitations in both evidence and conclusion.
         • Consider gaps in methodology or data.
         • Note any potential biases or confounding factors.

Return ONLY the following JSON structure:
{
     "conclusions": [
         {
            "claim_id": {claim_id},
            "author_conclusion": "detailed description of authors' conclusion based on evidence
                 ,→ ",
            "conclusion_justified": true/false,
            "justification_explanation": "detailed explanation of why conclusion is/isn't
                 ,→ justified",
            "robustness_analysis": "comprehensive analysis of evidence strength and reliability
                 ,→ ",
            "limitations": "specific limitations and caveats",
            "location": "section/paragraph where conclusion appears",
            "evidence_alignment": "analysis of how well evidence aligns with conclusion",
            "confidence_level": "high/medium/low based on evidence quality"
         }
     ]
}



B     Additional Details on Annotation
B.1     Annotator Guidelines
     • Select one recent research paper in the field of artificial intelligence or machine learning.

     • Prioritize papers published in 2024 to ensure relevance to current developments.

     • When possible, select a paper with fewer than 20 pages to facilitate thorough annotation.

     • Avoid papers with heavily mathematical content to ensure accessibility.

     • Complete all annotation tasks independently, without employing large language models for assistance
       at any stage of the process.

    Task Description
    Your task is to identify all statements in the text that qualify as claims under the following criteria:

    1. Specificity: The statement makes a specific, testable assertion about results, methods, or contribu-
       tions.

    2. Novelty: The statement represents a novel finding, improvement, or advancement.

    3. Clarity: The statement presents a clear position or conclusion.

    Requirements

     • Include both major and minor claims.

     • Ensure no claim is overlooked.

     • Present each claim as a separate item.

    Evidence Identification
    For each identified claim, find and document relevant evidence that:

    1. Relevance: Directly supports or contradicts the claim’s specific assertion.

    2. Concrete Support: Is presented with experimental results, data, or concrete examples.

    3. Traceability: Can be traced to specific methods, results, or discussion sections in the text.

    4. Exclusions: Evidence must not be derived from the abstract or introduction sections of the text.

    Conclusion Analysis

     • Justification: Evaluate whether the conclusions drawn in the text are justified by the evidence
       provided.

    Annotation Format
    Each annotation should be formatted as follows:
{
       "Claim_id": "<unique_identifier>",
       "Claim_text": "<text_of_the_claim>",
       "Evidence_text": "<text_supporting_or_contradicting_the_claim>",
       "Justification_Conclusion": "<evaluator's_comment_on_evidence_justification>"
}



B.2     Inter-Annotator Agreement Methodology
To evaluate the reliability of the CLAIM-BENCH annotations, we calculated Inter-Annotator Agreement
on a subset of 30 papers, each annotated by two different annotators on the Claims and the Evidence. For
each of the claims and the evidences, we take one set (“set A”) as the ground truth and compute the F1-
score of the other set (“set B”). Considering the symmetry, we also computed the F1-score swapping sets
A and B, and reported the averaged F1-score. We chose F1 because our annotation task (identifying and
linking spans) closely parallels standard information extraction tasks, where F1 is a standard evaluation
measure balancing precision and recall; this reflects the need for agreement on both the correctness and
comprehensiveness of annotations.
   Apart from this we also used an LLM assistant (Gemini 2.5) to automate Cohen’s κ on a 30-paper
subset. For every paper the LLM (i) extracted the two raw annotation files, (ii) built binary vectors of
length N (one entry per sentence; 1 = tagged, 0 = untagged) for claims and for evidence, (iii) populated
                                                                o −pe
the 2×2 contingency table (a, b, c, d), and (iv) computed κ = p1−p  e
                                                                      . the procedure was spot-checked on
10 papers and the LLM’s arithmetic matched manual counts exactly.
   The aggregated results are κ = 0.66 for claims (substantial agreement) and κ = 0.30 for evidence
(fair agreement). The lower evidence score is expected: evidence sentences are sparse (< 0.3% of text)
and dispersed, so chance agreement is already high, and even minor boundary or selection differences
depress κ. Moreover, a single claim can legitimately map to several evidence sentences; annotators
often choose different yet valid spans, further reducing overlap. Despite this, both scores confirm that
CLAIM-BENCH offers a dependable—though challenging—ground-truth resource for benchmarking
claim–evidence reasoning.

      Cohen’s κ Agreement Prompt

   Paper filename: {pdf_name} Total sentences in paper: {total_sentences}

   You are given two raw annotation lists for claim identification—one from Annotator 1 and one
   from Annotator 2. Follow the steps below exactly to compute Cohen’s κ:

       1. Vector Construction Build two binary vectors of length N = {total_sentences}:
              • 1 if the sentence was marked as a claim by the annotator.
              • 0 if the sentence was not marked as a claim.

       2. Contingency Table Using the two vectors, populate the 2 × 2 table:

                                                Ann 2 = 1 Ann 2 = 0
                                      Ann 1 = 1     a         b
                                      Ann 1 = 0     c         d

       3. Compute κ
                                      a+d
                                 Po =
                                        N
                                       a + b  a + c     c + d  b + d 
                                 Pe =                    +
                                         N        N            N        N
                                      Po − Pe
                                  κ=
                                       1 − Pe

       4. Return only the JSON below:
          {
              "kappa_claims": 0.00
          }



      Raw Annotations – Annotator 1: {raw_annotations1}
      Raw Annotations – Annotator 2: {raw_annotations2}

      Example Output: Cohen’s κ Calculation

  We compute Cohen’s κ for claim identification on a paper with N = 667 sentences.
      Annotation statistics

          • Annotator 1 marked 5 sentences as claims.

          • Annotator 2 marked 6 sentences as claims.

          • Overlap (both claim = 1): 4 sentences.

      Contingency table

                                         Ann 2 = 1 Ann 2 = 0 Row Tot.
                               Ann 1 = 1     4         1        5
                               Ann 1 = 0     2       660       662
                               Col. Tot.     6       661       667

      Calculations
                                   a+d        4 + 660
                              Po =         =             ≈ 0.9955,
                                     N          667
                                    a + b  a + c       c + d  b + d 
                              Pe =                     +
                                       N       N              N        N
                                        
                                      5     6        662    661
                                 = 667 667 + 667 667 ≈ 0.98375,

                                     Po − Pe   0.99550 − 0.98375
                               κ=            =                   ≈ 0.7231.
                                     1 − Pe       1 − 0.98375
      Result JSON
      {
           "kappa_claim": 0.7231
      }


B.3       Annotation Tool



Figure 5: The custom annotation tool interface used for CLAIM-BENCH dataset creation, enabling direct PDF text
selection and structured labeling (e.g., ’Add as Claim’ button) of claim-evidence pairs.


C     Impact of Documents’ Token Length
Figure 6 plots mean recall for three prompting strategies—Three-Pass, One-by-One, and Single-Pass—
across three document-length buckets (< 15 k, 15–20 k, ≥ 20 k tokens). A closer reading of the bars
yields three key observations:

    1. Performance drops are tied to the strategy more than the model size.

         • For every model, the Single-Pass run shows the steepest decline as documents grow.
         • Example: LLaMA’s recall plunges from about 0.60 in small papers to roughly 0.40 in ≥20
           k-token papers under Single-Pass.

    2. Once an iterative strategy is used, the size-related gap all but disappears.

         • Iterative prompting (Three-Pass or One-by-One) largely neutralises length effects—even for the
           smaller models.
         • LLaMA 70B: In One-by-One mode the large-document group matches or exceeds the small-
           document group (≈ 0.78 vs ≈ 0.76).
         • Ministral 8B: Three-Pass recall stays virtually flat (∼ 0.72–0.75) across all three size buckets;
           the length penalty only appears in Single-Pass.

    3. Larger models still benefit, but their advantage is greatest with fine-grained prompts.

         • Claude 3.5 Sonnet: Recall rises with document size under Three-Pass (≈ 0.72 → 0.85), and
           remains ≥ 0.75 in One-by-One.
         • GPT-4-Turbo: One-by-One keeps recall at or above 0.80 for medium- and large-size papers; the
           drop to ∼ 0.66 for large papers occurs only in Three-Pass, not in Single-Pass.



                   (a) LLAMA Recall                                          (b) Ministral Recall


                   (c) Claude Recall                                           (d) GPT-4 Recall

Figure 6: Mean recall by document size groups (small, medium, large) for different models and prompting strategies,
illustrating performance trends across increasing token counts.


   The figure shows that prompt granularity is the dominant lever for long-context recall. Single-pass
prompting amplifies context-window limits—especially in smaller models—but iterative, claim-level
prompting (Three-Pass and One-by-One) recovers performance, sometimes even improving it as the text
grows. Larger models are naturally more stable, yet they, too, realise their full potential only when given
finer-grained, multi-step instructions.

C.1   Sentence Distance Detailed Analysis



Figure 7: Aggregated statistics of the sentence_gap metric Count, Max, Mean, and Variance (Var)—for each model
under the three prompting strategies (Three-Pass, One-pass, and One-by-One). Larger counts and wider gaps (e.g.,
Claude and LLaMA exceeding 2,200-sentence links in One-by-One) reflect broader retrieval, whereas smaller
models such as Ministral keep distances short and variance low. “N/A” indicates the model-strategy combination
was not executed.
