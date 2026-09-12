# Large Language Models Hallucination: A Comprehensive Survey

**Authors:** Aisha Alansari, Hamzah Luqman
**Year:** 2025
**Venue:** arXiv preprint
**DOI:** arXiv:2510.06265
**Source PDF URL:** https://arxiv.org/pdf/2510.06265
**Date converted:** 2026-09-11

Derived from the PDF; the PDF is the source of record.

---

Large Language Models Hallucination: A
                                                           Comprehensive Survey
                                                                          Aisha Alansari, KFUPM and Hamzah Luqman, KFUPM
                                                                           aisha.ansari@kfupm.edu.sa, hluqman@kfupm.edu.sa

                                             Abstract—Large language models (LLMs) have transformed natural language processing, achieving remarkable performance across
                                             diverse tasks. However, their impressive fluency often comes at the cost of producing false or fabricated information, a phenomenon
                                             known as hallucination. Hallucination refers to the generation of content by an LLM that is fluent and syntactically correct but factually
                                             inaccurate or unsupported by external evidence. Hallucinations undermine the reliability and trustworthiness of LLMs, especially in
                                             domains requiring factual accuracy. This survey provides a comprehensive review of research on hallucination in LLMs, with a focus on
                                             causes, detection, and mitigation. We first present a taxonomy of hallucination types and analyze their root causes across the entire


arXiv:2510.06265v3 [cs.CL] 18 Mar 2026
                                             LLM development lifecycle, from data collection and architecture design to inference. We further examine how hallucinations emerge in
                                             key natural language generation tasks. Building on this foundation, we introduce a structured taxonomy of detection approaches and
                                             another taxonomy of mitigation strategies. We also analyze the strengths and limitations of current detection and mitigation approaches
                                             and review existing evaluation benchmarks and metrics used to quantify LLMs hallucinations. Finally, we outline key open challenges
                                             and promising directions for future research, providing a foundation for the development of more truthful and trustworthy LLMs.

                                             Index Terms—LLMs, Hallucination, Hallucination Causes, Hallucination Detection, Hallucination Mitigation, Hallucination Benchmarks,
                                             Hallucination Metrics
                                                                                                                ✦


                                         1   I NTRODUCTION                                                          understand the root causes of hallucinations throughout
                                                                                                                    their pre-training to the generation pathway. It also provides
                                         Natural language generation (NLG) has significantly ad-                    guidance in developing hallucination detection and mitiga-
                                         vanced in recent years due to the progress in transformer-                 tion techniques for LLMs. Based on the standard stages of
                                         based language models (LMs). Large language models                         LLMs’ development, we examine each stage of the develop-
                                         (LLMs), such as ChatGPT [1], Claude [2], and Bard [3], have                ment pipeline to identify the factors that contribute to hal-
                                         revolutionized natural language processing by enabling                     lucinations. We divide the LLM development pipeline into
                                         powerful capabilities across a diverse range of applications.              six distinct stages: data collection and preparation, model
                                         These models have offered substantial enhancements in                      architecture, pre-training, fine-tuning, evaluation, and infer-
                                         efficiency and productivity, which have enhanced progress                  ence. This examination facilitates a thorough understanding
                                         in downstream tasks, such as question answering (QA),                      of the underlying causes of hallucinations at every stage.
                                         abstractive summarization, dialogue generation, and data-                      Moreover, we propose a taxonomy for hallucination
                                         to-text generation. Despite these breakthroughs, a critical                detection techniques. This taxonomy categorizes halluci-
                                         challenge has emerged with LLMs, known as hallucination.                   nation detection techniques into retrieval-, uncertainty-
                                             Hallucination refers to the generation of content by                   , embedding-, learning-, and self-consistency-based tech-
                                         LLMs that is fluent and syntactically correct, but factually               niques. Based on our findings, it is challenging for a single
                                         inaccurate or unsupported by external evidence [4], [5]. It                hallucination detection approach to perform well under all
                                         can result in significant repercussions, including the dis-                circumstances. Retrieval-based detection approaches effec-
                                         semination of misinformation and breaches of privacy. In                   tively deal with factual hallucinations but are extremely
                                         contrast to conventional artificial intelligence (AI) systems,             sensitive to the quality of external knowledge. Similarly,
                                         which are usually trained in data related to a specific task,              learning-based detection approaches are accurate but de-
                                         LLMs have been trained using large amounts of online                       pend on high-quality annotated data. Uncertainty-based
                                         textual data [6]. This broad coverage enables exceptional                  detection addresses the challenge of data dependency us-
                                         coherence and fluency; however, it also increases the risk                 ing model confidence rather than external labeled datasets.
                                         of inaccuracies. LLMs can reflect biases present in their                  However, its effectiveness is highly sensitive to the calibra-
                                         training data, misinterpret unclear prompts, or modify in-                 tion of uncertainty thresholds, and it often fails to detect
                                         formation to align with the perceived intent of input [7].                 hallucinations when the model shows high confidence in
                                         This is particularly concerning when individuals depend                    an incorrect response. Similarly, self-consistency detection
                                         on language generation capabilities for sensitive applica-                 approaches can detect logical and contextual inconsistencies
                                         tions, such as summarizing medical data, customer service                  without relying on external evidence. However, these ap-
                                         dialogues, financial analysis reports, and providing legal                 proaches struggle with subtle factual errors and are highly
                                         counsel.                                                                   dependent on prompt diversity and sampling strategies.
                                             Investigating the stages of LLM development helps to                   Embedding-based detection techniques are robust in cap-



turing semantic discrepancies. Nevertheless, their perfor-             •   Hallucination explainability discussion: The hallu-
mance in detecting hallucination can be degraded in out-                   cination explainability methods is classified in this
of-domain data and low-resource languages. Therefore, the                  survey into model-derived and grounding explain-
combination of complementary approaches (e.g., learning                    ability. Each category includes recent studies to show
with uncertainty or retrieval with learning) is a promising                their potential for hallucination explainability.
direction to improve the overall detection robustness and              •   Datasets and Evaluation Metrics: We review the
accuracy.                                                                  benchmark datasets used for hallucination detection
    Furthermore, we expanded the existing taxonomy of                      and mitigation and identify their limitations. We also
hallucination mitigation techniques derived from prior re-                 discussed the metrics used to evaluate detection and
search [8], [9], [10] by categorizing them into four categories:           mitigation techniques.
prompt-, retrieval-, reasoning-, and model-centric training            •   In-depth Analysis of Reasoning-Aware Solutions:
and adaptation-based approaches. Prompt-based mitiga-                      We provide an in-depth review of recent reasoning-
tion approaches depend on structured prompting strate-                     based mitigation methods, including CoT, itera-
gies to guide models towards generating factual content.                   tive refinement, and chain-of-verification techniques,
Retrieval-based mitigation methods depend on external                      highlighting their roles in reducing hallucination in
knowledge to ground outputs. Reasoning-based mitigation                    complex tasks.
techniques, such as chain-of-thought prompting (CoT) and               •   Multilingual and Low-Resource Emphasis: This
self-consistency, enhance logical coherence and internal con-              survey identifies challenges unique to underrepre-
sistency. Model-centric training and adaptation-based ap-                  sented languages and surveys cross-lingual trans-
proaches involve modifying architectures, adjusting train-                 fer, multilingual fine-tuning, and prompt adaptation
ing objectives, and employing fine-tuning procedures to                    techniques to mitigate hallucinations in low-resource
improve models’ intrinsic factuality and reliability. Based                settings.
on our analysis, we show that no single approach com-                  The remainder of the survey is organized as follows:
pletely mitigates hallucination. Consequently, more effective      Section 2 provides a review of related surveys. Then, a
mitigation is a combination of complementary techniques.           detailed discussion about hallucination, its types, and how
The most promising are hybrid approaches that combine              it appears in diverse NLG tasks is presented in Section 3.
prompting or reasoning-based techniques with retrieval-            Section 4 presents a comprehensive taxonomy of the reasons
based and model-centric training and adaptation strategies.        for hallucination across all stages of the LLM development
    Moreover, we discuss the challenges faced by current           cycle, followed by a detailed classification of detection tech-
hallucination detection and mitigation methodologies, and          niques (Section 5) and mitigation strategies (Section 7). The
propose potential future work directions for detecting and         datasets used to train and evaluate hallucination detection
mitigating hallucinations in LLMs. While prior surveys laid        and mitigation techniques are presented in Section 8, and
critical groundwork, this survey builds upon previous re-          the evaluation metrics are discussed in Section 9. Finally,
search by providing a comprehensive analysis of the causes         Section 10 presents a detailed discussion of the open issues
of hallucinations and techniques that have been proposed           and future research directions, and Section 11 concludes this
for hallucination detection and mitigation. The main contri-       study.
butions of this survey can be summarized as follows:

   •   Hallucination causes analysis: This survey presents         2   R ELATED S URVEYS
       a deep analysis of hallucination causes across all          Given the rapid evolution of LLMs and their expanding
       stages of the LLM development cycle, from data              applications across diverse domains, hallucination detection
       collection and architecture design to inference.            and mitigation techniques have also progressed. Conse-
   •   LLMs hallucination taxonomy: A comprehensive                quently, there is a need to thoroughly analyze the causes
       taxonomy is proposed in this survey for the hal-            of hallucinations, their detection, and their mitigation tech-
       lucination causes, and state-of-the-art (SOTA) ap-          niques to remain up to date. Investigating these factors
       proaches that have been proposed for hallucination          will contribute to diagnosing the root causes of LLM hal-
       detection and mitigation.                                   lucinations and developing more effective detection and
   •   Hallucination detection discussion: We propose a            mitigation techniques. Several surveys have been published
       structured classification of hallucination detection        recently on LLMs hallucination [5], [8], [9], [11], [12]. These
       methods by categorizing them into five main cat-            surveys examine LLMs’ hallucination from multiple points
       egories: retrieval, uncertainty, embedding, learning,       of view and provide significant insights. Ji et al. [5] reviewed
       and self-consistency-based detection approaches.            hallucination across various NLG tasks and outlined the
       Each category have been discussed deeply to show            mitigation methods applied and the evaluation metrics used
       its potential for hallucination detection.                  in each task. Ye et al. [12] extended this work by proposing
   •   Hallucination mitigation discussion: The hallucina-         a new taxonomy for the detection and mitigation of hallu-
       tion mitigation methods is classified in this survey        cination. Zhang et al. [11] highlighted some issues related
       into four main categories: prompt, retrieval, rea-          to LLMs, such as input, context, and fact-conflicting halluci-
       soning, and model-centric training and adaptation-          nations. Tonmoy et al. [8] focused on hallucination mitiga-
       based techniques. Each category have been discussed         tion by presenting a taxonomy that categorizes mitigation
       deeply to show its potential for hallucination mitiga-      techniques into prompt engineering, retrieval-augmented
       tion.                                                       generation (RAG), self-refinement, and decoding strategies.



Huang et al. [9] presented a dual taxonomy of factuality and
faithfulness hallucinations and defined hallucination causes
                                                                                    Hallucination                       Creativity
in the data, training, and inference stages. The survey also
linked detection and mitigation strategies to their founda-                    Unintentional                                Intentional
tional causes to guide robust system development.                            Fabrication of real-
                                                                                                     Generate new
                                                                                                                          Generate novel
                                                                                                      information
    More recently, Saxena and Bhattacharyya [13] provided a                  world information                                ideas
                                                                                   Factual
comprehensive survey on hallucination detection methods,                                            Blur line between
                                                                                                                             Based on
                                                                                                      accuracy and
classifying hallucinations into intrinsic and extrinsic types.                 Contradiction
                                                                                                         novelty
                                                                                                                            imagination

In another study, Cossio [14] offered a taxonomy of hallu-                    Unfaithful to the                            Enhances user
cination types, including factual errors, contextual incon-                    source context                             engagement and
                                                                                                                            satisfaction
sistencies, temporal disorientation, ethical violations, and
domain-specific hallucinations, while categorizing causes
into data, model, and prompt-related factors. Malin et al.
[15] reviewed faithfulness metrics used to evaluate hallu-         Fig. 1: The differences and similarities between hallucination
cinations across summarization, QA, and machine transla-           and creativity in LLM outputs.
tion. They also linked mitigation strategies, such as RAG
and prompting frameworks, with improved faithfulness. Qi
et al. [16] focused on automatic hallucination evaluation.         as GPT [6] and T5 [23], since their capacity to produce fluent
Rahman et al. [17] reviewed fact-checking and factuality           and contextually relevant text has markedly improved [21].
evaluation in LLMs, and analyzed how hallucination affects             However, it is important to distinguish between creativ-
LLM reliability.                                                   ity and hallucination. Hallucinatory outputs can be valued
    Unlike prior surveys, our survey makes several dis-            in creative writing or ideation tasks, which means that there
tinctive contributions as shown in Table 1. Compared to            is a gray zone. Creativity allows LLMs to produce novel
previous work, our survey proposes a detailed taxonomy             and imaginative responses, such as poetry or fictional sto-
of LLM hallucination causes explicitly linked to the LLM           rytelling. In contrast, hallucination involves generating fac-
development cycle and develops more fine-grained tax-              tually incorrect or misleading content. Creativity is known
onomies for both hallucination detection and mitigation.           to be deliberate and goal-driven, while hallucinations are
We further review these techniques in multilingual con-            typically unintended by the model designer or user [18].
texts, addressing language-specific challenges that are often      Moreover, creativity does not inherently violate accuracy,
disregarded in the literature. Our analysis also spans the         whereas hallucination does [18]. Figure 1 explains the simi-
entire LLM lifecycle, from pre-training and fine-tuning to         larities and differences between creativity and hallucination.
inference, which provides a more comprehensive review
than previous studies. In addition, we discuss the limita-
tions of each detection and mitigation category and present        3.2   Types of Hallucination
detailed future research directions to guide advancements          Hallucination in NLG can be classified into two types: in-
in this field. Furthermore, we provide an in-depth review of       trinsic and extrinsic [21]. Intrinsic hallucination occurs when
reasoning-based mitigation methods since these approaches          the output of the LLM contradicts facts present in the source
represent a newer wave of mitigation techniques that differ        document. These errors often arise due to misinterpretation
fundamentally from prompt engineering, as they focus on            of context, entity confusion, or biases in the training data.
structuring and verifying the model’s internal reasoning           Figure 2 shows an example of intrinsic hallucination. As
rather than only modifying input prompts.                          shown in the figure, the LLM erroneously generates ”Charles
                                                                   Dickens”, when a user asks about the author of ’Pride
                                                                   and Prejudice’, which contradicts the information in the
3     LLM S H ALLUCINATION
                                                                   ground truth. On the other hand, extrinsic hallucinations
3.1   Definition of Hallucination                                  are characterized by the inclusion of information in the
In a psychological context, the term ”hallucination” refers        output that is not present in the ground truth. In contrast
to a false perception of objects or events [19]. It involves the   to intrinsic hallucinations, extrinsic hallucinations introduce
experience of seeing, hearing, feeling, smelling, or tasting       additional content that cannot be verified against the source,
stimuli that are not actually present. These sensations are        rather than contradicting it. In such cases, the text appears
often indistinguishable from reality to the one experiencing       plausible; however, it lacks explicit support from the input.
them [20]. In the context of LLMs, hallucination refers to the     It is important to note that extrinsic hallucinations can often
generation of text that appears reasonable, fluent, and coher-     contain factually accurate information that is derived from
ent but lacks grounding in factual or accurate information         external knowledge, despite not being explicitly stated in
[21].                                                              the source. As shown in Figure 2, when a user asks about
    Hallucinations in earlier LMs, such as n-gram models,          the author of Pride and Prejudice, the LLM generates the
were more readily identifiable due to their restricted gen-        correct answer with an extra entity ”completed the manuscript
erative capabilities. Unlike modern LLMs, which produce            in 1797” that is not present in the ground truth data. While
highly fluent text, earlier LMs often generate nonsensical or      this statement may be factually accurate, it is not explicitly
clearly inaccurate outputs, which makes their hallucinations       provided in the ground truth data. This demonstrates how
easier to detect [22]. Conversely, it is more challenging to de-   an LLM might interpolate prior knowledge or generate
tect hallucinations in texts generated by modern LLMs, such        plausible-sounding additions that lack direct verification.



                                    TABLE 1: A comparative analysis of existing LLM hallucination surveys.

                                                                                       Features
Reference              Year
                                          F1           F2                  F3          F4           F5         F6           F7            F8
[5]                  2023           ✓                ✗              ✓              ✗               ✓            ✗            ✓             ✗
[12]                 2023           ✗                ✓              ✓              ✓               ✗            ✗            ✓             ✗
[11]                 2023           ✓                ✗              ✓              ✓               ✓            ✗            ✓             ✗
[9]                  2023           ✓                ✓              ✓              ✓               ✗            ✗            ✓             ✗
[8]                  2024           ✗                ✗              ✓              ✗               ✗            ✗            ✓             ✓
[13]                 2024           ✓                ✓              ✗              ✓               ✗            ✗            ✓             ✗
[16]                 2024           ✗                ✗              ✗              ✓               ✓            ✓            ✓             ✗
[18]                 2024           ✗                ✓              ✓              ✗               ✗            ✗            ✓             ✗
[17]                 2025           ✗                ✗              ✓              ✓               ✓            ✗            ✓             ✗
[15]                 2025           ✗                ✗              ✗              ✓               ✓            ✗             ✗            ✗
[14]                 2025           ✓                ✗              ✓              ✓               ✓            ✗            ✓             ✗
Our Survey           2025           ✓                ✓              ✓              ✓               ✓            ✓            ✓             ✓
F1: Analyzes causes of hallucination; F2: Proposes a new detection taxonomy; F3: Proposes a new mitigation taxonomy; F4: Surveys benchmark
datasets; F5: Surveys evaluation metrics; F6: Covers multilingual or cross-lingual hallucination detection and mitigation techniques; F7: Provides
explicit limitations and future-work directions; F8: Surveys reasoning-based techniques.


                                                                                 sentence, the LLM generates a full paragraph. Context in-
                         Jane Austen                                             consistency refers to cases where the LLM ignores or alters
                        wrote pride and                     Intrinsic            important facts within the original text. For example, if a
                          prejudice
                                                                                 given passage states that ”The Mona Lisa was painted by
                                                   Answer: Charles Dickens
                                                   wrote pride and prejudice     Leonardo da Vinci,” the model incorrectly states that ”The
         Query: Who wrote
                                                                                 Mona Lisa was painted in the 17th century”. Logical incon-
         pride and prejudice                                Extrinsic            sistency refers to cases where the LLM’s internal reasoning
                                                                                 contradicts itself, leading to logically flawed outputs. This
                                                  Answer: Jane Austen wrote
                                                  pride and prejudice in 1979.
                                                                                 may stem from flawed inference or unstable reasoning
                                                                                 chains. Figure 3 presents examples of factuality and faith-
                                                                                 fulness hallucinations in LLMs.
Fig. 2: The difference between intrinsic and extrinsic
hallucination.                                                                   3.3   Hallucination in NLG Tasks
                                                                                 Hallucination in LLMs appears mainly in NLG tasks that
                                                                                 involve generating open-ended text. In contrast, hallucina-
    Huang et al. [9] extended the hallucination classification                   tion occurs less frequently in natural language inference
to factual and faithful. Factuality hallucination describes                      (NLI) tasks, such as entailment classification and sentiment
the divergence between produced content and known real-                          analysis, that require the LLM to select from limited and
world facts, often appearing as a factual contradiction or                       pre-defined options [5]. Consequently, they reduce the pos-
fabrication. It may consist of intrinsic or extrinsic hallucina-                 sibility of fabrication in such tasks compared to NLG tasks.
tions. This problem occurs due to the probabilistic charac-                      This section describes how hallucination can occur in the
teristics of LMs, which prioritize coherence and fluency over                    main NLG tasks.
factual correctness. Factual contradiction describes cases                           Machine Translation involves translating a text from one
where LLMs generate responses that are grounded in real-                         language to another. Models may provide grammatically
world information but contradict each other. This typically                      accurate translations but may convey new or irrelevant
arises due to conflicting training data, entity confusion, or                    meanings, particularly for low-resource languages or am-
errors in context retention. For example, a model states that                    biguous inputs [24].
”The capital of Saudi Arabia is Dammam”, which contradicts                           Text Summarization is generating a concise and coherent
the known fact that it is Riyadh. Factual fabrication de-                        summary that preserves the most important information
scribes cases where LLMs generate responses that cannot                          from one or more source documents. In the literature, two
be verified with real-world information. For instance, the                       main methods for text summarization are followed: ex-
model claims that ”Sarah Collins travelled to the planet Mars”                   tractive and abstractive [25]. Extractive text summarization
when, in reality, no one travelled to Mars.                                      selects and organizes the most important sentences from the
    Faithfulness hallucination occurs when the generated                         source text to form a summary. Abstractive text summariza-
output drifts from the original input or context, violating                      tion, on the other hand, paraphrases the selected sentences
the user’s instructions or violating the logical consistency                     to form a summary. Abstractive text summarization is more
within the response. This type of hallucination is further                       prone to hallucination than extractive text summarization,
categorized into three subtypes: instruction, context, and                       since paraphrasing the text may lead to generating false
logical [9]. Instruction inconsistency refers to cases where                     information [21].
the LLM fails to follow the user’s instruction. For example,                         Generative QA is a type of QA system that generates
if a user asks an LLM to summarize a paragraph in one                            answers to user queries in natural language, rather than




        Factual Hallucination

                    Factual Contradiction                                       Factual Fabrication

         Query: What is the capital of Saudi Arabia?                Query: Who was the first person to travel to the
                                                                    planet Mars?
         Answer: The capital of Saudi Arabia is Jeddah.
                                                                    Answer: Sarah Collins in 2022.


        Faithful Hallucination

                  Instruction Inconsistency                                    Context Inconsistency
         Context: Plastic pollution harms marine life and           Context: Plastic pollution harms marine life and
         disrupts ocean ecosystems.                                 disrupts ocean ecosystems.

         Query: Translate the text in Arabic.                       Query: What are the harms of plastic pollution?

         Answer: Plastic is commonly found in the ocean.            Answer: Plastic pollution disrupts recycling
                                                                    efforts in cities.


                                                   Logical Inconsistency
                                         Query: What is the output of 5+5x5?

                                         Answer: 50.


                              Fig. 3: Examples of various hallucination types in LLM responses.


selecting a predefined answer from a database or document.            task of rewording text while preserving its original meaning.
It constructs its response based on the model’s comprehen-            The model is required to generate text with semantically
sion of the inquiry and the provided context. Generative              equivalent expressions to the source text. Hallucination can
QA systems search for external knowledge from multiple                occur in this task when the model adds information not
sources to formulate a response. These sources may consist            present in the source or omits crucial details. This can distort
of redundant, complementary, or conflicting information               the intended message, resulting in potential misunderstand-
[26], [27]. Therefore, it is highly susceptible to generating         ings [33].
hallucinated text.                                                        Code Generation is an NLG task that generates code
    Dialogue System facilitates human-computer interaction            snippets based on natural language descriptions. This task
through natural conversation. Dialogue systems are broadly            is highly prone to hallucination, resulting in code that ap-
categorized into task-oriented and open-domain systems.               pears plausible but consists of logical, runtime, or syntax
Task-oriented systems help users complete specific goals,             errors [34]. Such hallucinated code can lead to software
such as booking flights or managing appointments using                malfunctions or security vulnerabilities if not identified and
structured databases [28]. Open-domain systems engage in              corrected.
unrestricted conversations across diverse topics [29]. Open-
domain dialogue systems are prone to generating content
that is not necessarily present in the input or knowledge             3.4   Impact of Hallucination in Critical Domains
source, leading to extrinsic hallucinations. Task-oriented            LLMs Hallucination can pose a considerable challenge, par-
systems, while more constrained, can still hallucinate due            ticularly in domains where precise information is essential,
to incomplete or misclassified data [30], [31]                        such as healthcare, legal counsel, finance, and education. In
   Data to Text is a task that entails utilizing structured data,     such domains, LLMs hallucination can directly result into
such as a table, as input to generate text that accurately and        clinical harm, legal liability, and financial loss.
coherently represents this data as natural language text. The             Hallucination in medicine is defined as the generation of
models of this task are prone to hallucination due to the gap         an output that is not supported by authoritative clinical
between structured data and text [32]. Paraphrasing is the            evidence and could alter clinical decisions [35]. One of the



active research areas in employing LLMs in the medical              larly, in financial applications, hallucination mitigation must
domain is clinical documentation and consultation summa-            be coupled with auditability, confidence estimation, and
rization [36]. Asgari et al. [36] found that the most common        traceability. This is to ensure that generated analyses and
hallucination type in this domain is fabricating the planning       summaries can be verified against authoritative sources
section of clinic notes. However, detecting hallucination in        before influencing high-stakes decisions. Moreover, in the
this domain is challenging due to the ambiguity of the              legal domain, LLMs must be integrated into human-in-the-
terms, which leads to diverse errors [35]. Therefore, detect-       loop workflows, where generated outputs serve as assistive
ing hallucination in the medical domain depends highly              drafts rather than final legal judgments. Human oversight
on the level of domain expertise and the level of detail            by qualified legal professionals is essential to validate cita-
in the prompt provided to the detection model. Domain               tions, reasoning chains, and conclusions before use in real-
experts are more likely to identify subtle inaccuracies in          world settings. Moreover, regulatory and ethical consider-
clinical terminology and reasoning, whereas non-experts             ations, including professional responsibility rules, data pri-
may struggle to discern these errors, thereby increasing            vacy laws, and accountability frameworks, necessitate trans-
the risk of misinterpretation [35]. Accordingly, transparency,      parency, traceability, and auditability in legal AI systems.
interpretability, and trustworthiness in medical AI are a           Regulatory considerations further necessitate transparency
necessity for Healthcare professionals to understand how            and accountability, as hallucinated outputs may lead to legal
and why an LLM arrived at its conclusions and thereby im-           liability or regulatory violations. Consequently, effective
prove hallucination detection and mitigation in the medical         hallucination detection and mitigation in real-world systems
domain.                                                             requires a combination of technical safeguards, domain-
    Hallucination in finance raises a critical risk, since hallu-   aware human oversight, and compliance-aware deployment
cinated numbers, mis-summaries of financial statements, or          strategies.
fabricated market events can drive misallocation of capi-
tal [37]. Various specialized LLMs, such as FinBERT [38]
and BloombergGPT [39] have been developed to generate               4     H ALLUCINATION C AUSES
financial-related content. However, hallucination presents a        Several reasons can make LLMs hallucinate when respond-
major challenge to deploy such LLMs in real-world applica-          ing to the user query. These causes can be linked to the
tions [37]. To mitigate hallucination in the financial domain,      LLM development lifecycle, starting from pre-training to the
Kang and Liu [37] demonstrated the effectiveness of RAG             inference pathway. Figure 4 illustrates the main stages of
with prompt-based tools in learning to generate accurate            developing LLMs and the causes of hallucination associated
content. Moreover, Roychowdhury [40] demonstrated the               with each stage. This section discusses hallucination sources
effectiveness of prototyping, scaling, and LLM evolution            at each stage of the LLM development process.
using human feedback to minimize hallucination in the
financial domain.
    Hallucination in law poses a significant risk due to the        4.1   Data Curation
authoritative tone and persuasive fluency of LLM-generated          The initial stage of LLM development is data collection and
legal text, which may obscure factual or doctrinal inac-            preparation. Large-scale and diverse datasets are usually
curacies. Legal hallucination refers to the generation of           collected from different sources, such as books, websites, so-
incorrect, fabricated, or outdated legal information, such as       cial media, and scientific articles. These datasets encompass
non-existent case law, misquoted statutes, or erroneous legal       diverse domains, languages, and contexts. Once collected,
reasoning, that is not supported by valid legal sources. Such       the data undergoes extensive filtering and cleaning to re-
hallucinations are particularly dangerous because legal de-         move duplicates, irrelevant, and noisy content.
cisions often rely on precise interpretations of jurisdiction-          Although LLMs’ capabilities are significantly improved
specific laws, precedents, and procedural rules [41]. De-           by scaling up pre-training data [42], scaling introduces
tecting hallucination in the legal domain is particularly           persistent challenges in maintaining data quality [43]. The
challenging due to the complexity and evolving nature               utilized data for training LLMs is a significant source of
of legal systems in different countries. Additionally, legal        bias, which LLMs may unintentionally acquire and propa-
validity depends on temporal factors, jurisdictional scope,         gate [44]. Online content, in particular, can reflect societal
and contextual interpretation, all of which are difficult for       imbalances in the representation of gender, race, nationality,
LLMs to model reliably [41]. As a result, hallucination             and other demographic factors [45]. These social biases
detection in legal applications requires access to up-to-date       are inherently linked to hallucinations. Additionally, LLMs
legal corpora, robust citation verification mechanisms, and         may exhibit memorization tendencies, particularly with fre-
domain-aware evaluation criteria that go beyond surface-            quently occurring data points, despite deduplication efforts
level factual consistency.                                          during the data preparation stage. As a result, the model
    Beyond model-level evaluation, hallucination detection          might over-represent high-frequency words, phrases, and
and mitigation in critical domains must be integrated into          concepts from the training data, which creates an imbalance
practical system workflows. In healthcare, LLM outputs              in the generated outputs. Consequently, they exhibit a bias
should be deployed as decision-support tools, with hal-             towards over-represented training data, which results in a
lucination detection techniques serving as real-time safe-          hallucinated output that diverges from the desired content
guards that flag uncertain or unsupported content. Such             [46].
human-in-the-loop designs align with clinical governance                Another source of data-induced hallucination is imi-
requirements and reduce the risk of automation bias. Simi-          tative falsehoods [43]. It arises when a model learns and




               Fig. 4: The main causes of hallucination at different stages of the LLM development pipeline.


reproduces false or misleading information embedded in           produce inaccurate or entirely fabricated responses [50].
its training data, often originating from misconceptions or
misinformation. LLMs are designed to mimic the patterns in
their training distribution, which can accidentally amplify      4.2   Model Architecture
common misconceptions. For instance, if an LLM encoun-           While architectural design primarily aims to enhance learn-
ters incorrect attribution of the creation of the light bulb     ing capabilities and efficiency, some learning strategies
exclusively to Thomas Edison, it is prone to reproduce           or LLM’s architecture components can inadvertently con-
this error upon inquiry. Although Edison played a crucial        tribute to hallucinations. The sources of the hallucination
role in the development and commercialization of the light       related to the model architecture involve attention mech-
bulb, he was not its original inventor. However, due to the      anism, objective function, positional encoding, and unidi-
prevalence of simplistic historical narratives, the model may    rectional contextualization. Attention enables LLMs to dy-
confidently present this misunderstanding as fact, perpetu-      namically focus on different segments of the input when
ating an imitative deception.                                    generating an output [51]. Self-attention helps capture long-
     Furthermore, knowledge conflict is another source of hal-   range dependencies within the same sequence, while cross-
lucination, wherein the model is trained using different         attention enables conditioning on external context, such as
sources that provide contradicting information regarding         retrieved documents. However, the soft attention mecha-
the same subject. These inconsistencies can lead to outputs      nisms in capturing long sequences can result in hallucina-
that reflect conflicting viewpoints or factual errors [47].      tion [52]. As the sequence length increases, the attention
Domain knowledge deficiency can also make LLMs hallucinate.      weights may become more diffuse, leading the model to
Despite the impressive performance of LLMs in zero-shot          distribute the focus between less relevant tokens, which can
scenarios, they struggle with tasks that require specialized     result in degraded reasoning or factual inaccuracies [53].
reasoning or access to confidential data [48]. In fields such        The objective function used during model training can
as healthcare, precision and accuracy of information are         influence the likelihood of LLM hallucination [54]. Most
essential. The lack of domain-specific training data can lead    models use maximum likelihood estimation (MLE), which
to hallucinations, which often appear as factual inaccuracies    encourages generating the most probable token at each step.
[9].                                                             However, this method does not explicitly penalize factual
     Another source of hallucination in LLMs is outdated         inconsistencies, which can lead to hallucinations, especially
factual knowledge. Once LLMs are trained, their internal         when a model confidently fills in missing information based
parametric knowledge remains fixed and does not reflect          on statistical likelihood [54]. Positional encoding also plays
subsequent changes in real-world facts. Therefore, LLMs          a fundamental role in LLMs, as transformers lack intrinsic
often generate fabricated facts or responses that were once      awareness of tokens order. LLMs augment input sequences
accurate but are now outdated when faced with questions          with positional encodings; either using fixed sinusoidal
outside their training time-frame [49]. This temporal mis-       functions, as in the original transformer, or learned position
alignment leads to hallucinated content, which compro-           embeddings, as adopted in models like GPT-3 and T5.
mises the factual reliability of LLM outputs.                    These methods enable LLMs to learn tokens order and
     Additionally, LLMs are especially prone to hallucina-       maintain context for moderate-length texts. However, as
tions when dealing with long-tail knowledge that appears         input sequences become longer, the effectiveness of these
infrequently in the training data [50]. LLMs are trained to      positional representations tends to deteriorate [55]. Conse-
recognize patterns in text based on how often words and          quently, the model may not longer reliably track relative
phrases appear together. As a result, they tend to perform       positions, which results in misinterpreting which tokens are
well on common or frequently discussed topics. However,          related or contextually relevant. As a result, hallucinations
when it comes to rare or obscure entities that are not well      may emerge when the model misinterprets contextual rela-
represented in the training data, LLMs are more likely to        tionships due to position-tracking limitations.



    Lastly, unidirectional contextualization can cause halluci-    example can improve model accuracy up to ten times more
nation. Autoregressive LLMs, such as GPT, process text             than a positive one, as it helps the model sharply reduce the
unidirectionally, in a left-to-right fashion. This behaviour       likelihood of plausible but false answers [63].
inherently limits their capacity to comprehensively capture
and integrate contextual information from both preceding
and subsequent tokens. Thus, driving the model to depend
primarily on local patterns. Consequently, when the model          4.4   LLMs Fine-Tuning
is faced with ambiguous or incomplete input, it may infer or
fabricate content to maintain coherence, thereby introducing       LLMs are usually fine-tuned after the pre-training stage
hallucinations [9].                                                on more specialized datasets related to downstream tasks,
                                                                   such as healthcare reports summarization, QA, and stance
                                                                   detection. Supervised fine-tuning is an iterative process that
4.3   Model pre-training                                           includes re-training the model’s parameters partially until
The following stage of the LLM development process is pre-         the desired capabilities are met. In parallel with supervised
training the model. This stage utilizes massive data to train      fine-tuning, reinforcement learning from human feedback
the model to learn general language representation in an           (RLHF) has emerged as a key strategy for aligning model
unsupervised manner. The model is generally trained with a         output with human preferences. RLHF generally employs a
language modeling objective, where the model learns to pre-        preference model that receives rewards from human evalua-
dict the next token in a sequence given its preceding context.     tors who judge its generated responses based on some crite-
While pre-training significantly improves LM performance           ria, such as factual accuracy and relevance [66]. To conform
and generalization, some strategies employed during this           to human preferences, RLHF guides the LLM to produce
phase may lead to hallucination during inference, such as          outputs that maximize the reward given by the trained
shortcut learning, teacher forcing learning strategy, and a        preference model, usually via a reinforcement learning (RL)
lack of sufficient negative examples.                              [67]. This approach has proven effective in aligning LLMs
    Shortcut learning is a phenomenon where a model tends          with human intent and improving output quality. However,
to learn superficial, non-robust patterns of the data, rather      both supervised fine-tuning and RLHF introduce some risks
than robust features for making predictions [56]. This over-       that can lead to hallucinations during inference.
reliance on certain characteristics or biases can lead to inad-        One reason for hallucination at this stage is overfitting on
equate generalization in out-of-distribution contexts. Some        task-specific data [68]. When models are fine-tuned exclu-
studies indicate that LLMs often exploit shortcuts derived         sively on narrow or domain-specific datasets, they usually
from statistical indicators, such as the word ”not” [57],          become overly sensitive to the patterns and biases present
specific keywords [58], and cues associated with linguis-          in that data. Domain-specific fine-tuning may constrain the
tic variations [59], to formulate predictions. Consequently,       model’s generalization and increase the likelihood of gener-
LLMs often generate dependable results with independent            ating deterministic and biased solutions that misrepresent
and identically distributed samples but may exhibit hal-           the original data distribution [69]. If this model is later
lucinations with out-of-distribution data. Another cause of        exposed to out-of-distribution prompts, it may attempt to
hallucinations is the teacher forcing learning strategy [60]. In   generate answers beyond its learned domain, which in-
the teacher forcing MLE setup, the model learns to predict         creases the risk of hallucination.
the next word in a sequence based on a flawless context.               Another source of hallucination at this stage is the mis-
During inference, the model predicts each following token          alignment between the model’s internal capabilities and the
based on its previously generated tokens, rather than re-          expectations encoded in the alignment data [9]. Alignment
lying on ground truth inputs. This discrepancy, known as           refers to the process of ensuring that the model’s outputs
exposure bias, can cause the model to hallucinate if an early      are aligned with human preferences. Although alignment
token is incorrect or contextually inappropriate [61]. This        significantly improves the quality of LLM responses, it
deviation is further exacerbated by the cascade effect, where      also increases the risk of hallucination [9]. This risk arises
an early mistake leads to a chain reaction of subsequent           when there is a mismatch between the model’s intrinsic
errors, which can compound errors in a ”snowball effect.”          capabilities and the alignment data’s expectations. One of
This can be attributed to the lack of corrective feedback          these misalignments is capability misalignment, which oc-
when the model generates an incorrect token [62]. This             curs when alignment training encourages the model to
issue arises particularly in high-entropy segments where           provide definitive answers even when it lacks sufficient
the model’s confidence is low, increasing the likelihood of        knowledge [9]. Although RLHF encourages the model to
hallucinations.                                                    generate responses that meet human preferences, it may
    Moreover, the lack of sufficient negative examples dur-        prioritize coherence and confidence over factuality, which
ing training can weaken the model’s ability to distinguish         leads to hallucinated responses. Another misalignment cat-
between fact and fiction [63]. While LLMs rapidly attain           egory is belief misalignment, where disparity occurs between
exceptional performance on benchmark tasks, they often             the model’s internal beliefs or knowledge learned from pre-
struggle with simple challenge instances and underperform          training and its output after alignment [70]. This issue often
in real-world situations [64]. Without exposure to diverse         occurs alongside sycophantic behavior, a tendency for the
incorrect or misleading examples during training, models           model to generate responses that evaluators will approve
can fail to recognize and correct common misconceptions            of, regardless of whether those responses are accurate or
[64], [65]. During a critical phase of training, each negative     not [70].



4.5   LLMs Evaluation                                              increases, the model is more likely to draw from the tail of
This stage involves evaluating the model’s generation ac-          the distribution, leading to vivid but potentially inaccurate
curacy and coherence using benchmark datasets for down-            generations.
stream tasks, such as QA and summarization. This assess-               SoftMax activation can also cause hallucinations during
ment is accomplished by both automatic and human eval-             inference [77]. LLMs often use a softMax function to calcu-
uation. One of the automatic metrics used to evaluate the          late word prediction probability to predict the likelihood of
LLM on intrinsic language tasks is perplexity. It evaluates        each next word in the sequence. SoftMax is optimized for
the likelihood of a sequence of words given the model’s            contexts where there is one dominant next word. However,
learned probabilities. Human evaluators assess model re-           in rich contexts with multiple potential meanings, the de-
sponses based on coherence, fluency, faithfulness, and fac-        sired distribution might have multiple peaks corresponding
tuality. Ensuring factual alignment is crucial for mitigating      to different word choices. SoftMax struggles to handle these
hallucination, as models may generate fluent yet misleading        situations, as it cannot easily represent multiple equally
responses. Therefore, the outcomes of these evaluations are        relevant words. This limitation, known as the softMax bot-
then used to improve the model’s factual consistency and           tleneck [77], occurs when the model’s output layer cannot
coherence.                                                         adequately assign high probabilities to multiple diverse yet
    Inadequate evaluation metrics are one of the main reasons      equally relevant words, restricting its ability to represent
for undetected hallucination in this stage [21]. Automatic         them equally well.
metrics, such as ROUGE [71], BertScore [72], and BLEU                  Finally, reasoning limitations pose a substantial challenge
[73], are usually used for evaluating LLMs. However, these         for factuality in LLM outputs [78]. LLMs often fail to pro-
metrics often fail to assess the factuality and faithfulness of    duce accurate responses in scenarios that require multi-hop
the generated text. This can lead to models that perform well      reasoning or logical deduction. Complex reasoning tasks
on such metrics but hallucinate during deployment [21].            involve linking multiple pieces of information or making
                                                                   logical inferences. This can extend beyond simple recall and
                                                                   requires a structured understanding of relationships within
4.6   Inference                                                    the data. In such multi-hop QA scenarios, the model needs
After deployment, LLMs are ready for the inference stage           to connect different pieces of information across multiple
to generate responses to user queries in real-time. During         steps [78]. For instance, if a question requires the use of one
this stage, the model leverages its pre-trained knowledge          fact to understand another, then the LLM must perform the
and fine-tuning to deliver relevant output to the users’ in-       necessary reasoning that bridges these two steps to arrive at
puts. However, despite optimization and alignment efforts,         a correct answer. If the model fails to link the facts properly,
deployed models remain vulnerable to hallucinations, espe-         it will usually hallucinate when generating responses.
cially when encountering ambiguous inputs, randomness in
sampling, architectural limitations, or reasoning challenges.
    One common source of hallucination in the inference            5     H ALLUCINATION D ETECTION
stage is ambiguous input prompts. Ambiguity is a natural part      Hallucination detection involves identifying instances in
of language, which involves multiple alternative meanings          LLM outputs that are inaccurate, nonsensical, or incon-
and contextual relationships for the language unit. Prompts        sistent with the input or context. Unlike traditional fact
that are vague, ambiguous, or prone to speculation are often       verification, which primarily verifies claims against external
a source of hallucinations [74]. A lack of specificity in user     sources, hallucination detection involves a more compre-
queries encourages LLM to rely on its own training data            hensive analysis. It often requires analyzing factuality and
and experience rather than addressing the user’s request.          faithfulness within the model’s responses. In this survey,
For instance, given the vague prompt, “Explain recent break-       we categorize hallucination detection methods present in
throughs in energy,” the LLM might respond with a fabricated       the literature into retrieval, uncertainty, embedding, learn-
claim such as “One recent breakthrough is ‘quantum solar cells,’   ing, and self-consistency-based techniques. The proposed
developed by Dr. Sarah Lin in 2023, which convert sunlight into    taxonomy is illustrated in Figure 5. Table 2 summarizes
energy with 95% efficiency, a revolutionary improvement over       the hallucination detection studies. The results are mainly
traditional solar cells.” This vague prompt led the LLM to         reported using the AUROC metric, which tests the model’s
invent a non-existent breakthrough and research, resulting         ability to distinguish between the hallucination and non-
in a hallucination.                                                hallucination classes across all possible probability thresh-
    Another source of LLM hallucination at this stage is           olds.
inherent sampling randomness [75]. During text generation,
the model selects the next word based on a probability dis-
tribution over possible tokens. While deterministic decod-         5.1   Retrieval-Based Detection
ing strategies (e.g., greedy decoding) favor high-probability      Retrieval-based hallucination detection methods compare
tokens and minimize hallucination risk, they often lead to         an LLM’s output with trusted external knowledge sources,
repetitive or uninspired responses. This is a phenomenon           such as databases and encyclopedias. These methods aim
known as the likelihood trap [76]. In contrast, stochastic         to ensure factual consistency and reduce the risk of un-
decoding methods such as top-k or nucleus sampling in-             supported content by grounding the output in verifiable
troduce creativity. However, these methods also increase           information. RAG is one of the most widely used retrieval-
the chance of selecting low-probability tokens that diverge        based techniques for hallucination detection [79], [80], [81].
from factual or contextual correctness [75]. As randomness         It combines retrieval systems with generative models to




                                            Retrieval                                           [84, 85, 86, 87, 88, 89]

                                                                    Token-level               [92, 93, 94, 95, 96, 97, 98]

                                          Uncertainty             Semantic-based                          [99]

                                                                  Structured-based           [100, 101, 102, 103, 104, 105]


                                                                  Similarity-based                    [106, 107]
               Hallucination
                                           Embedding
                Detection
                                                                  Gradient-based                         [108]

                                                                    Supervised                      [109, 110, 111]

                                            Learning               Unsupervised                     [112, 113, 114]

                                                                    Agent-based                          [115]


                                                                   Answer-based                     [116, 117, 118]
                                              Self-
                                           consistency
                                                                  Question-based                    [119, 120, 121]


                                  Fig. 5: The taxonomy of hallucination detection methods.


fetch relevant documents and compare their content with              including GPT-4, in both span-level and binary halluci-
LLMs-generated outputs [82]. RAG can be followed by fact-            nation detection and in factual editing tasks. KnowHalu
checking models to evaluate the correctness of statements            is another improvement over retrieval-based hallucination
[82], [83].                                                          detection [88]. It first detects non-fabrication hallucination,
    Ajmal et al. [84] detected hallucinations by assessing           then performs a multi-form factual check through step-
the semantic and factual consistency of generated answers            wise reasoning, query decomposition, and knowledge re-
against the source. The approach uses contextual similar-            trieval. By aggregating judgments across multiple knowl-
ity analysis and cross-referencing to identify discrepancies,        edge forms, KnowHalu achieved significant improvements
such as incorrect entities, factual contradictions, or logi-         of 15.7% and 5.5% in QA and summarization tasks, respec-
cally inconsistent statements. The detected discrepancies are        tively. In another study, JointCQ [89] detected hallucination
quantified through a scoring mechanism that reflects the             by extracting factual claims and generating targeted search
magnitude of hallucination. Similarly, Paudel et al. [85] in-        queries from a QA pair. These queries are then used to
troduced a hallucination detector for enterprise applications        retrieve external evidence. A verifier model checks whether
by verifying LLM outputs against the provided context,               each claim is supported, contradicted, or unverifiable based
which is the retrieved document and common knowledge,                on the retrieved contexts. Using HalluQA, it achieved an
which is the LLM’s parametric knowledge. It uses a modular           accuracy of 80.58% and an F1-score of 83.05%.
detector (HDM-2) that checks whether generated statements
contradict the provided context or conflict with common              5.2    Uncertainty-Based Detection
knowledge. Detection is performed at both the response               Probabilistic and uncertainty-based hallucination detection
level and span level, producing hallucination scores and             methods flag low-confidence outputs as potential hallu-
fine-grained annotations.                                            cinations without requiring external knowledge retrieval.
    In order to improve retrieval-based techniques, Wang et          These methods exploit the inherent uncertainty in the model
al. [86] used a Bayesian sequential estimation. Instead of           predictions to identify hallucinated content. The main hy-
retrieving a pre-defined number of documents, one docu-              pothesis in uncertainty estimation is that high uncertainty
ment is retrieved at a time to assess each subclaim’s veracity.      indicates that the model is guessing rather than relying on
After each retrieval, the Bayesian sequential analysis decides       learned patterns [90], [91]. Uncertainty-based hallucination
whether to continue retrieving documents or stop. This               detection techniques can be classified into token-, semantic-,
dynamic stop-or-continue strategy optimizes the balance              and structure-based methods. Examples of the differences
between retrieval costs and accurate hallucination detection,        between these techniques are shown in Figure 6.
which leads to improved efficiency and precision. Building               Token-based Approaches. Several methods have been
on the need for more granular analysis, Mishra et al. [87]           used to quantify token-level uncertainty in LLMs to detect
proposed FAVA, a retrieval-augmented model trained on                hallucination. Guerreiro et al. [92] detected LLM halluci-
synthetic data to detect various types of hallucination using        nation in machine translation tasks using sequence log-
span-level detection. FAVA outperformed baseline models,             probability. This approach measures the confidence of the



model by calculating the normalized log probability of           semantic similarity. Moreover, entropy is computed across
the generated tokens. In another study [93], the log-based       these semantic clusters. A high semantic entropy indicates
uncertainty measure was used to develop an uncertainty-          that the model’s answers vary in meaning, indicating a high
aware framework for hallucination detection. The method          likelihood of hallucination, while a low semantic entropy
relies on token probability scores derived from LLM logit        suggests a consistent meaning across generations, which
outputs to measure uncertainty. Instead of setting a strict      means greater reliability.
threshold, uncertainty is introduced as an intermediary vari-
able to be used adaptively. Accordingly, the model implicitly         Structured-based Approaches. Recent studies proposed
incorporates uncertainty in its decision-making. Although        structured uncertainty detection, which detects hallucina-
token-level uncertainty estimation achieved promising re-        tion by modeling the logical or semantic dependencies be-
sults, this technique is calculated based on lexical variety.    tween claims as a graph or tree and propagating uncertainty
Therefore, responses that give the same meaning but use          across the connected units. Hou et al. [100] proposed de-
different words will not be treated as uncertain. Zhang          tecting hallucination by belief tree propagation (BTPROP).
et al. [94] enhanced uncertainty-based hallucination detec-      Instead of relying solely on token-level uncertainty, BTPROP
tion by improving token probability estimation, reducing         recursively decomposes a statement into logically related
overconfidence, and incorporating focus mechanisms. This         subclaims and builds a tree of beliefs. A hidden Markov
approach focuses on the most informative keywords, un-           tree is then used to integrate the model’s noisy confidence
reliable tokens in historical contexts, and specific token       scores and logical relationships between claims. This ap-
properties. Instead of relying on raw probability, Dasgupta      proach robustly propagates uncertainty and corrects mis-
et al. [95] proposed HalluShift, which detects hallucinations    calibrated beliefs. Expanding on these directions, Chen et
by measuring distribution shifts in internal hidden states       al. [101] introduced a graph-enhanced uncertainty modeling
and attention layers.                                            approach to capture the relations among entity tokens and
    More recent work improves upon this idea by learn-           sentences. The authors also proposed a graph-based uncer-
ing to model token-level uncertainty from internal rep-          tainty calibration technique that accounts for the possibility
resentations rather than relying only on raw probability         of phrase conflicts with neighbors in the semantic graph
values. Instead of treating all tokens equally, these meth-      when calculating uncertainty. This method achieved a no-
ods train auxiliary models to identify which token-level         table improvement in passage-level hallucination detection,
signals, such as hidden states or probability distributions,     increasing the Spearman correlation by 19.78%.
are most indicative of hallucination. Shelmanov et al. [96]
proposed pre-trained uncertainty quantification heads to             Beyond semantic graphs, recent work explores structural
predict claim-level hallucination by leveraging attention        signals directly derived from internal attention patterns.
maps and token probability features within the LLM. These        Lookback Lens [102] is an unsupervised approach that
transformer-based heads are trained on annotated hallu-          analyzes attention for hallucination detection. By measuring
cination data, which outperformed both classical unsu-           the lookback ratio, which quantifies how much the model at-
pervised and prior supervised uncertainty methods, with          tends to prior context versus its own outputs, this approach
strong generalization across domains and languages. Simi-        identifies contextual hallucinations without requiring la-
larly, Niu et al. [97] proposed a multiple instance learning     beled data. This method achieved competitive performance
framework for hallucination detection that adaptively se-        with supervised detectors like RIPA and supports real-time
lects salient token embeddings that are most indicative of       mitigation during decoding, though it incurs higher infer-
factual inaccuracy. The selection is guided by uncertainty       ence time and relies on effective sampling. LapEigvals [103]
metrics such as token-level and sentence-level entropy.          modeled attention maps using a Laplacian graph and spec-
By combining these uncertainty features with deep rep-           tral features. It achieved superior results, with an AUC-ROC
resentation learning, this framework achieved robust and         of 88.9% on the TriviaQA dataset. Likewise, HalluZig [104]
generalizable hallucination detection, outperforming prior       detected hallucinations by training a supervised classifier
supervised and unsupervised uncertainty-based methods.           on topological features extracted from attention dynamics. It
HaluNet [98] detected hallucinations using internal uncer-       models layer-wise attention matrices as graphs and applies
tainty signals extracted in a single forward pass. It combines   zigzag persistence from topological data analysis to capture
token log-likelihoods (confidence), entropy (distributional      how attention structures evolve across layers. Hallucina-
uncertainty), and hidden-state embeddings (semantic un-          tions are identified when these signatures indicate unstable
certainty) through a lightweight multi-branch neural archi-      or short-lived attention patterns associated with flawed
tecture. These uncertainty signals are fused with attention-     reasoning. Similarly, TOHA [105] detected hallucinations
based weighting to learn how different types of uncertainty      by analyzing the topological structure of attention maps
correlate with hallucination. Unlike self-consistency meth-      inside the LLM. It builds attention graphs that links between
ods, it does not require multiple generations, making it         the prompt and response tokens. Then, they compute a
efficient and suitable for real-time QA systems.                 topological divergence score (MTop-DivG) that measures
    Semantic-based Approaches. Farquhar et al. [99] pro-         how structurally different the response is from the prompt.
posed a semantic entropy measure to detect hallucinatory         The method identifies a small set of hallucination-aware
content. Semantic entropy is computed over the sentence’s        attention heads whose divergence consistently separates
meaning rather than relying on the words’ distribution.          hallucinated from grounded outputs. The final detection is
This technique first generates multiple responses to the         performed by averaging the divergence scores across these
same prompt. These responses are then clustered based on         heads, which makes the method computationally efficient.




                                               Initial Response            Technique                 Detection Result

                                                                       Uncertainty calculation
                                                                                                 The capital of Saudi Arabia is                High
                                             The capital of Saudi                                                                   Token
                                             Arabia is Dammam.                                   Dammam.


                                                                                                                                               Model uncertainty bar
                                                                              Clustering
                                                                                                 Riyadh          Central City
                                          Riyadh, It’s Riyadh,                                   It’s Riyadh     Najd
                                            Riyadh,city,
                                          Central    It’s Najd,
                                                           Riyadh,
                                              Riyadh,city,
                                            Central     It’s Najd,
                                                             Riyadh,                                                              Semantic
                                          Dammam,
                                              Central Khobar,
                                                        city,  Najd,                                     Dammam
                                            Dammam,
                                          Jeddah          Khobar,
                                              Dammam,        Khobar,                                     Khobar
                                            Jeddah
                                              Jeddah                                                     Jeddah
 Query: What is the
 capital of Saudi Arabia
                                                                           Attention head

                                           The capital of Saudi                                  Hallucination Likelihood:
                                           Arabia is Dammam.                                     High                             Supervised   Low


Fig. 6: Examples of hallucination detection techniques across three uncertainty-based approaches: token-level uncertainty
calculation, semantic clustering, and structured detection via attention heads.


5.3   Embedding-Based Detection                                        The learning-from-data feature enables these methods to
Embedding-based hallucination detection techniques mea-                generalize to diverse hallucination types across domains
sure the semantic similarity between input, output, and                and tasks.
external references using vector embeddings. These ap-                     Supervised-based Methods. Choi et al. [109] introduced
proaches assume that the output of a faithful model should             RIPA, a token-level hallucination detector trained on syn-
be semantically close to its sources in a shared embedding             thetic examples generated through knowledge shuffle and
space. These approaches can be classified into similarity-,            partial hallucination strategies. In the partial hallucination
gradient-, and spectral-based approaches.                              approach, only certain words or phrases in a sentence that
    Similarity-based Approaches. Dale et al. [106] used                are factually correct are replaced with false information.
cross-lingual semantic comparison between source and                   This teaches the model to spot hallucinations that appear
translation to detect hallucinations. They evaluated                   in specific parts of a sentence rather than across the whole
embedding-based similarity models such as LaBSE and                    output. RIPA then identifies both the onset, where the first
LASER, as well as an XNLI entailment model that measures               hallucinated token appears, and the span, the consecutive
bidirectional semantic consistency. Low semantic alignment             set of tokens that make up the hallucinated content. In
between source and translation indicates semantic detach-              a related direction, Zhang et al. [110] proposed PRISM,
ment, which corresponds to hallucination. Among exter-                 which leverages prompt-guided internal hidden states as
nal methods, LaBSE performed substantially better than                 features for a supervised hallucination detector. By craft-
LASER. Nonkes et al. [107] extended embedding-based ap-                ing prompts that enhance the truthfulness structure in the
proaches by constructing a semantic similarity graph where             LLM’s internal representations, PRISM achieves good do-
each generated sentence is a node and the edges connect se-            main generalization, outperforming previous internal-state
mantically close outputs. A Graph Attention Network then               and token-probability-based baselines in both accuracy and
performs message passing to learn structural patterns in the           AUROC. In another study, HaluGNN [111] formulates hal-
embedding space, under the hypothesis that hallucinated                lucination detection as a graph classification problem using
generations occupy distinct regions of the latent space.               a supervised GNN. Each QA instance is converted into a
    Gradient-based Approaches. Hu et al. [108] extended                weighted directed graph where nodes are token hidden
embedding-based hallucination detection by incorporating               states and edges are attention weights, preserving both
gradient information, which captures how sensitively the               semantic content and token relationships. A graph neural
model’s output responds to its input. Their method charac-             network is trained on a small labeled set to distinguish
terizes the disparity between conditional and unconditional            factual vs hallucinated responses.
outputs by a Taylor series expansion, capturing both em-                   Unsupervised and Weakly-based Methods. Park et al.
bedding changes and gradient-based uncertainty signals. A              [112] introduced a truthfulness separator vector (TSV) that
multi-layer perception classifier trained on these features            is added to internal LLM activations during inference to
demonstrated SOTA performance across hallucination de-                 reshape the embedding space. TSV aims to increase sepa-
tection benchmarks.                                                    rability between truthful and hallucinated representations
                                                                       without fine-tuning the model. It is trained using a small
                                                                       labeled set and pseudo-labeled unlabeled generations via
5.4   Learning-Based Detection                                         optimal transport alignment and confidence filtering. In
Learning-based detection approaches leverage trained mod-              another study, Yamada and Arase [113] detected hallucina-
els to classify LLM outputs as hallucinated or factual. These          tion by training a lightweight encoder-based model with
models are typically trained on annotated datasets or proxy            contrastive (triplet) learning. The learning objective pulls
labels and aim to capture patterns indicative of halluci-              faithful generations closer to the input in embedding space
nation beyond rule-based or similarity-based techniques.               while pushing hallucinated generations farther away. This



contrastive objective is combined with a standard classi-       relative trustworthiness, aiming to reduce overconfidence
fication loss to improve separability between hallucinated      in incorrect outputs and improve the reliability of the final
and non-hallucinated outputs. At inference time, the model      prediction. Experiments across multiple tasks and LLMs
simply compares the input and generated text to predict         show that T3 substantially improves the AUROC for hal-
whether hallucination is present, without retrieval or ex-      lucination detection and calibration compared to prior self-
ternal knowledge sources. In another study, contextual em-      consistency and confidence-based baselines. More recently,
beddings were utilized to detect hallucinations in a real-      SelfElicit [118] detected hallucination in long-form text by
time, unsupervised manner [114]. The authors proposed           decomposing them into statements and evaluates each one
using the internal hidden states of the LLM during infer-       using calibration-based fact-checking. The model predicts
ence. They introduced MIND, a lightweight hallucination         True/False/Not Sure and the confidence of “False” serves
classifier trained using pseudo-labeled data automatically      as a hallucination score. The approach then elicits reflective
constructed from Wikipedia. The method records contextu-        thoughts conditioned on this evaluation and stores them in a
alized token embeddings produced at each decoding step          knowledge hypergraph, which provides contextual seman-
and feeds them into an MLP to detect hallucination. The         tic information for subsequent statements. A self-consistent,
best results were obtained using the last token’s embedding     NLI-based conflict-resolution mechanism is applied to de-
from the last transformer layer.                                tect and mitigate contradictions, preventing hallucination
    Agent-based Methods. Cheng et al. [115] proposed            snowballing.
HaluAgent, an autonomous hallucination detection agent               Question-based Methods. SAC3 [119] extends self-
built on small open-source LLMs. HaluAgent integrates           consistency by incorporating semantic-aware cross-
a multi-stage detection pipeline. The pipeline consists of      checking, including question perturbation (question
sentence segmentation, tool-based verification, and reflec-     rephrasing) and cross-model verification (output
tive reasoning with external resources, such as web search,     comparison across different LLMs) to detect points
calculators, and code interpreters. It was fine-tuned on        where self-consistency fails. These techniques address
synthetic detection trajectories. HaluAgent’s performance       question-level hallucinations, where a model consistently
was comparable to GPT-4’s on several benchmarks and also        generates incorrect but plausible responses, and model-
maintains strong generalization across domains in hallu-        level hallucinations, where there are inconsistencies
cination detection across different tasks, including open-      between models. Yang et al. [120] further advance self-
domain QA, summarization, and dialogue generation.              consistency-based detection with MetaQA. This approach
                                                                utilizes metamorphic relations, such as synonym and
                                                                antonym prompt mutations, to systematically alter queries
5.5   Self-Consistency-based Detection
                                                                and evaluate LLM responses for factual consistency.
Self-consistency is an unsupervised technique that improves     This technique outperformed SelfCheckGPT in zero-
LLMs’ reasoning by generating multiple responses to a           resource settings. Similarly, Xue et al. [121] present a
single prompt and assessing their internal consistency. Self-   two-stage methodology that integrates self-consistency
consistency does not require ground truth references, mak-      with cross-model consistency. Their approach initially uses
ing it useful in open-ended and low-resource settings. Self-    conventional self-consistency detection. Followed by a
consistency-based techniques can be categorized into an-        verifier LLM to validate ambiguous responses.
swer and question-based methods. Answer-based methods
generate multiple answers to the same query using varied
decoding hyperparameters, such as temperature and top-          5.6   Detection Challenges
k. It then evaluates the model’s consistency across these       Most hallucination detection approaches proposed in the
responses. Question-based methods, on the other hand, gen-      literature depend on either uncertainty estimation or self-
erate answers to paraphrased versions of the same question      consistency verification to detect hallucination. The main
and assess the model’s consistency across these different       hypothesis of uncertainty estimation is that a high uncer-
phrasings. Figure 7 illustrates the difference between answer   tainty indicates that the model is guessing instead of relying
and question-based self-consistency hallucination detection.    on learned patterns. Therefore, the uncertainty-based detec-
     Answer-based Methods. Manakul et al. [116] introduced      tion approaches flag LLMs’ outputs with low confidence
SelfCheckGPT, which utilizes self-consistency to detect         as potential hallucinations. However, multiple uncertainty-
LLMs’ hallucination. This approach examines various tech-       based hallucination detection approaches, especially those
niques, including BERTScore similarity, question-answering      relying on token-level probability or entropy, tend to over-
consistency, n-gram probabilities, NLI, and prompt-based        predict hallucination. Most of these approaches incorrectly
evaluation to assess the consistency of the generated text.     flag too many outputs as hallucinations [122], which leads
The key idea of this approach is that if a response is          to low precision, especially when hallucinations are sparse
factual, repeated queries to the same prompt with slight        or when dealing with informative content, such as named
randomness should yield consistent responses, whereas hal-      entities. Moreover, these approaches fail in capturing hallu-
lucinated content would yield highly variable responses.        cinated responses generated by models with high certainty
Li et al. [117] introduced a comprehensive answer eval-         [123]. Other techniques, such as BTPROP [100], are exten-
uation framework called think twice before trusting (T3).       sive in terms of computational costs due to the recursive
This approach prompts the model to generate multiple            decomposition and multiple model queries.
candidate answers, reflect on each one, and provide jus-            Self-consistency verification is an unsupervised tech-
tifications. It then compares these answers to assess their     nique that enhances the reasoning capabilities of LLMs




                                                                                                            Hallucination
                                            Response 1:
                                                                                                      No

                                            Response 2:


                                                                                                      Yes
                                            Response 3:                                                          No
                                                                                                            Hallucination


                                            Query:                                     Response 1:
 Query:
                               Question
                             Paraphrasing
                                            Paraphrase 1:                               Response 2:


                                            Paraphrase 2:                               Response 3:


          Fig. 7: Examples of answer-based and question-based self-consistency methods for hallucination detection.


by generating multiple responses to a single prompt and          output should be semantically close to its sources in a
evaluating their internal consistency. Self-consistency-based    shared embedding space. Although embedding-based ap-
hallucination detection approaches do not require ground         proaches have demonstrated good hallucination detection
truth references, making them useful in open-ended and           performance, their reliance on internal model states imposes
low-resource settings. However, the effectiveness of self-       several limitations. Performance can be degraded on out-
consistency hallucination detection depends on the diversity     of-domain data, rare linguistic phenomena, or low-resource
of prompts and sampling strategies. These methods may            languages, where embedding models are less robust and
fail to detect inconsistencies that indicate hallucinations      attention structures are less informative [126]. Moreover,
[80] if the sampled responses lack diversity. Similarly, if an   the choice of which model layers or heads to extract em-
LLM is overconfident about a fact, self-consistency methods      beddings from can significantly affect the detection perfor-
will fail to detect hallucination. In these cases, all sampled   mance. Although Oblovatny et al. [127] introduced a robust
responses may agree on the same incorrect information,           method for fine-grained selection of attention heads, it does
leading to high consistency scores for hallucinated con-         not fully solve the challenge of detecting subtle halluci-
tent. Additionally, self-consistency approaches do not verify    nations. Another inherent limitation of embedding-based
outputs against external knowledge or ground truth. As a         detection techniques is their inability to capture halluci-
result, they cannot catch hallucinations that are confidently    nations stemming from external knowledge misalignments
and consistently produced by the model but are factually         with real-world facts, especially if the model’s training data
incorrect in the real world [119].                               are outdated or incomplete.
    In contrast to uncertainty and self-consistency-based hal-       Learning-based hallucination detection approaches
lucination detection approaches that do not require ground       leverage supervised or unsupervised models trained on
truth references, retrieval-based detection approaches de-       annotated data to classify LLM outputs as either halluci-
pend on external knowledge retrieval to verify the gen-          nated or factual. By learning from data, these methods can
erated LLM’s outputs. These approaches aim to enhance            generalize to a wide range of hallucination types across
factual consistency and mitigate the risk of unsupported         different domains and tasks. However, supervised learning
content by grounding model outputs in verifiable informa-        algorithms require an extensive amount of labeled or syn-
tion. However, the effectiveness of retrieval-based detection    thetic data for training. Models trained on specific tasks or
is fundamentally limited by the quality of the retrieved         synthetic hallucination data may not generalize well to un-
documents [124]. If the retrieved documents contain incom-       seen hallucination types or out-of-domain tasks. Although
plete, outdated, or irrelevant information, the detector may     unsupervised learning hallucination detection techniques
either miss hallucinations or incorrectly flag accurate state-   offer advantages in terms of annotation-free operation and
ments. Additionally, LLMs often struggle to select between       potential real-time application, they may struggle to gener-
parametric knowledge and retrieved sources, which can re-        alize across different domains and hallucination cases [102].
sult in hallucinations [125]. Furthermore, incorporating real-       The observed limitations in each category indicate that
time retrieval increases computational cost and response         no single detection paradigm is sufficient in isolation. Hy-
latency, which can pose challenges for interactive and real-     brid strategies that combine internal confidence signals,
time applications [124].                                         consistency checks, and external evidence grounding are in-
    Embedding-based hallucination detection techniques de-       creasingly explored to balance scalability, factual reliability,
pend on measuring the semantic similarity between input,         and robustness across tasks and domains. However, hybrid
output, and external references. The main assumption of          techniques must also be selected carefully, as combining
these embedding-based approaches is that a faithful model        methods with similar failure modes may not necessarily



improve robustness. For example, both uncertainty-based          fails to align with external evidence. Grounding explainabil-
and self-consistency approaches struggle when models pro-        ity is usually based on source documents, factual references,
duce high-confidence but incorrect outputs. This failure         or claim decomposition. They identify hallucinations by re-
mode is also observed in embedding- and attention-based          vealing unsupported statements, contradictions, missing ev-
similarity methods, which rely on internal representations       idence, or broken inference chains, often through evidence
rather than external grounding. The usefulness of the detec-     highlighting, entailment checking, or structured reasoning
tion technique is highly task- and domain-dependent. For         verification. One prominent direction for grounding-based
instance, attention- or embedding-based similarity signals       hallucination explainability is through a relational mapping
tend to be more informative in tasks such as summa-              of evidence to text. HaluCheck [133] provided explainability
rization and context-based QA, where hallucinations often        through evidence-grounded, sentence-level verification. The
manifest as faithfulness errors relative to a given source       proposed technique decomposes model outputs into atomic
document. In contrast, for open-domain QA, hallucinations        facts. Then, it retrieves supporting documents from external
often arise from incorrect world knowledge rather than           knowledge sources, and uses NLI models to determine
source misalignment, making internal similarity or attention     whether each fact is entailed. Hallucinations are highlighted
patterns less reliable indicators of factual correctness. In     directly, which allows users to see which specific state-
such cases, retrieval-based or knowledge-grounded verifi-        ments lack evidence. Likewise, Chen et al. [134] introduced
cation becomes more critical. These observations suggest         HaluMap, which constructs a segment-level matrix of en-
that effective hallucination detection requires complemen-       tailment and contradiction relations between source inputs
tary combinations of methods that address different failure      and generated text using NLI models. HaluMap produces
modes, rather than redundant hybrids that amplify shared         a heatmap-like visualization that highlights which parts of
weaknesses.                                                      the output are unsupported or contradicted by the source.
                                                                 To improve robustness, they further propose SelfHaluMap,
                                                                 which is a calibration mechanism that estimates background
6     H ALLUCINATION E XPLAINABILITY                             inconsistency within the source document itself and reduces
                                                                 noise in the final explanation. In another direction, Hu et
    Hallucination explainability extends hallucination de-
                                                                 al. [135] introduced a two-stage framework that combines a
tection by explaining why they occurred and where they
                                                                 small language model for rapid hallucination detection with
came from. It focuses on generating human-understandable
                                                                 an LLM-based constrained reasoner that generates detailed
reasons for a model’s hallucinations [128]. In this survey,
                                                                 explanations for detected cases. Their approach dramati-
we divide the existing studies into model-internal explain-
                                                                 cally reduces inconsistencies between detection and expla-
ability, which interprets hallucinations through the model’s
                                                                 nation, achieving a high F1 score for identifying inconsistent
internal behavior, and evidence-based explainability, which
                                                                 rationales. In another study, Orshansky et al. [136] focused
grounds explanations in evidence alignment and reasoning
                                                                 on reasoning-structured explanations. They proposed Hal-
structure.
                                                                 luTree, which decomposes summaries into subclaims and
                                                                 organizes verification results into a hierarchical claim tree.
6.1   Model-Derived Explainability
                                                                 Subclaims are categorized as extractive or inferential. Ex-
Model-internal explainability treats hallucinations as a con-    tractive subclaims are directly verifiable against the source,
sequence of model-internal dynamics. These methods ex-           whereas inferential subclaims requires multi-hop reasoning.
plain hallucination using signals extracted from model out-      Extractive claims are checked with lightweight NLI models.
puts or model-inferred quantities. Uncertainty is currently      On the other hand, inferential claims initiate a reasoning
treated as a component of explainability in LLMs [129].          path, where an LLM proposes a set of supporting facts from
Huang et al. [130] introduced RePPL, which attributes hallu-     the source text, logical or mathematical reasoning, or general
cinations to token-level uncertainty derived from instability    knowledge. Later, they are organized into a coherent reason-
in semantic propagation through attention layers and low-        ing chain. An LLM then evaluates the claim’s groundedness
confidence generation decisions. In another direction, the       using CoT reasoning. Both the supporting facts and the rea-
hallucination explanation is learned during hallucination        soning trace are attached into a verification tree to provide
detection. HuDEx [131] is trained to justify its hallucina-      an explicit, explainable rationale. Similarly, Galitsky and
tion judgments directly using natural language, where it         Rybalov [137] leveraged information gain with abductive
provides reasoning behind these judgments. Similarly, Xie        reasoning to explain reasoning-based hallucinations. The
et al. [132] introduced FENCE, which is trained to identify      proposed technique measures how much a model’s claim
factual errors at the claim level. The model classifies claims   shifts the probability distribution away from what is sup-
as supported, contradictory, or unverified and generates         ported by the source. It then checks whether any minimal,
explanatory critiques. Retrieval is used in a supporting role,   plausible hypothesis could logically justify that shift. If no
providing external evidence from search engines, knowl-          simple abductive explanation exists, or only overly complex
edge bases, and knowledge graphs to inform the evaluator’s       ones do, the claim is labeled a hallucination, and the missing
judgments.                                                       or faulty reasoning path is explicitly identified.


6.2   Grounding Explainability                                   6.3   Explainability Challenges
Grounding explainability refers to methods that explain hal-     Despite recent progress in developing explainability meth-
lucinations by examining how generated content aligns or         ods for hallucinations, there remain significant open chal-



TABLE 2: Comparison of hallucination detection techniques. Detection categories include retrieval-based (R.), uncertainty-
based (U.), embedding-based (E.), learning-based (L.), and self-consistency (S.). Results are reported in AUROC metric; *
indicates F1-score, and † indicates Accuracy.

 Ref     Year   Task                                     Detection                                                         Result Per Dataset


                                                                                           TruthfulQA                                   HaluEval-QA    HaluEval-Sum
                                                                                 WikiBio                TriviaQA   SQuAD                                               RagTruth    CNN/DM    HotpotQA
                                               R.   U.      E.       L.    S.                                                 NQ


 [86]    2023   Bio. gen.                      ✓                     ✓          74.2
 [87]    2024   Info-seeking                   ✓                     ✓
 [84]    2025   QA                             ✓                     ✓
 [89]    2025   QA                             ✓                     ✓
 [88]    2024   QA, Summ.                      ✓                     ✓                                                                72.3*           68.5*                                 72.1*
 [85]    2025   QA, Summ., D2T                 ✓                     ✓          83.7*                                                                                 85.0*

 [92]    2023   MT                                  ✓                ✓
 [94]    2023   Summ.                               ✓                ✓          77.7
         2024   Summ.                               ✓                      ✓    90.4*
 [100]
         2025   Summ.                               ✓                           78.3
 [101]
 [93]    2023   QA                                  ✓                ✓
 [96]    2025   QA                                  ✓       ✓        ✓
 [97]    2025   QA                                  ✓                ✓                                  90.3       83.7      86.7
 [98]    2025   QA                                  ✓       ✓        ✓                                  81.1       92.2      81.1
         2025   QA                                  ✓       ✓        ✓                     82.9         88.9       79.5      82.7      87.4
 [103]
         2024   QA, Summ.                                   ✓        ✓
 [102]
 [99]    2024   QA, Summ.                           ✓       ✓
         2026   QA, Summ.                           ✓                           73.3                               73.0
 [104]
         2025   QA, Summ.                           ✓                                                              96.0                                                           60.1
 [105]
 [95]    2025   QA,Summ., Dlg.                      ✓       ✓                              93.0         99.2                 95.0      53.0

         2023   MT                                  ✓       ✓
 [106]
         2024   QA, Summ.                           ✓       ✓                   63.0
 [107]
         2024   QA, Dlg., Summ.                             ✓        ✓          89.8*                                       97.2†     95.1†
 [108]

         2024   QA                                          ✓        ✓
 [110]
         2025   QA                                  ✓       ✓        ✓                     68.8         93.0
 [111]
         2025   QA                                          ✓        ✓                     88.7         87.2                 78.0
 [112]
         2023   Summ., Dlg.                    ✓    ✓                ✓
 [109]
         2024   Text gen.                                   ✓        ✓
 [114]
         2024   QA, Text, Code                 ✓                     ✓     ✓                                                          83.8*
 [115]
         2025   QA, D2T, Summ.                              ✓        ✓                                                                60.4*           63.6*
 [113]

         2023   Bio. gen.                                                  ✓    80.3
 [116]
         2024   QA                                          ✓              ✓
 [117]
         2023   QA                                                         ✓                                                 77.2                                                           88.0
 [119]
         2025   QA                                                         ✓                                                                                                                71.7
 [120]
         2025   QA                                                   ✓     ✓
 [118]
         2025   QA, Bio. gen.                                        ✓     ✓
 [121]


lenges that limit their effectiveness. Unlike classification la-          to the model’s internal mechanisms and those that are inter-
bels, there is no universally agreed-upon correct explanation             pretable to humans, especially non-experts. This is because
for why a model hallucinates in a given instance. Explana-                such techniques can be too technical for end users, while
tions often rely on proxy signals such as attention patterns,             simpler explanations may omit key reasoning details, which
structural irregularities, or alignments with external evi-               reduces transparency. Those techniques are also computa-
dence, which may not fully capture the underlying model’s                 tionally expensive, which limits their practicality for long
reasoning. This makes it difficult to evaluate the quality,               texts, real-time applications, or large corpora. Furthermore,
faithfulness, and completeness of explanations produced by                there is a lack of standardized benchmarks and metrics for
explainability methods. Moreover, in techniques that rely on              evaluating explanation quality. Without agreed standards,
reasoning trees and topological features, there is a gap be-              comparing different methods and measuring improvement
tween producing explanations that are accurate and faithful               is difficult, which slows progress.



7     H ALLUCINATION M ITIGATION                                   ified references, which minimizes reliance on parametric
                                                                   knowledge.
Hallucination mitigation aims to reduce or prevent the                 Instruction-based prompts. Provide explicit and clear
emergence of factually inaccurate, ungrounded, and contex-         instructions to an LLM to guide its output towards the
tually inconsistent responses in LLMs’ outputs. In contrast        intended result using natural language. Studies [145], [146]
to hallucination detection, which focuses on detecting hal-        have shown that instruction-based prompting, when cou-
lucinatory outputs, mitigation seeks to make modifications         pled with techniques such as CoT reasoning or iterative
to LLMs to deliver accurate responses. Mitigating hallucina-       refinement, significantly reduces hallucinations by con-
tions is a crucial priority in the advancement and implemen-       straining model responses to align with facts and ra-
tation of LLM to ensure LLM output remains factual, trust-         tionality. Moreover, LLM fine-tuning on instruction-based
worthy, and safe. As shown in Figure 8, this survey cate-          datasets enhances its ability to follow complex instructions
gorizes the hallucination mitigation techniques proposed in        and reduce errors [147]. Kim et al. [148] proposed SELF-
the literature into prompt-based, retrieval-based, reasoning-      EXPERTISE, a method that generates knowledge-based in-
based, and model-centric training and adaptation-based             struction datasets rather than relying on LLMs’ parametric
techniques. Table 3 summarizes the mitigation studies with         knowledge. It extracts factual knowledge from seed dataset
the datasets used in each study and the metrics employed to        outputs to create structured instruction, input, and output
evaluate their techniques. Moreover, Table 5 presents results      pairs, ensuring factual accuracy. Additionally, system in-
on the four most widely used datasets for hallucination            structions provide explicit guidance for generating logically
mitigation.                                                        sound responses, particularly in specialized domains, such
    Hallucination mitigation is followed by post-repair            as law.
methods, which repair the detected hallucination spans                 Tag-based prompts. These approaches depend on tailor-
with minimal alteration to the rest of the output. Targeted        ing LLMs to perform certain tasks by integrating additional
correction methods operate at the span or entity level. Once       information ”tags” into the input. These tags or markers are
specific tokens, entities, or propositions are flagged as hal-     incorporated into the prompt to direct the model’s focus
lucinated, the model regenerates or edits only those parts,        and response formulation. Feldman et al. [149] conducted a
often under additional constraints or with external evidence       study on the impact of tagged prompting on LLM hallucina-
[138], [139]. On the other hand, partial regeneration methods      tion mitigation. Their research demonstrated a remarkable
relax the granularity from spans to larger segments such           success rate of 98.88% in eliminating fabricated information
as sentences, paragraphs, or specific reasoning steps [138],       when using context-embedded tags. Similarly, Penkov [150]
[140]. The system selectively regenerates only the hallucina-      proposed a method that integrates domain-specific tools,
tion segments, while preserving the rest of the answer.            such as BioBERT and ChEBI, with tagged prompting. Their
                                                                   approach focused on anchoring LLM outputs to verifiable
                                                                   facts, particularly in specialized fields, such as biomedicine.
7.1   Prompt-Based Techniques
                                                                   The study showed that this combination of techniques could
Prompt engineering has emerged as an effective way                 substantially reduce hallucinations by providing a semantic
to guide and regulate LLM behavior. A well-constructed             framework for the model to adhere to during response
prompt can play an essential role in mitigating hallucina-         generation.
tions [141]. The notion of prompt design originated with the           ICL prompts. Refer to an alternative learning paradigm
advent of GPT-2 [142] and GPT-3 [6], when researchers be-          in which the prompt contains some examples for the LLM
gan exploring the capability of pre-trained LLMs to perform        to follow to complete the task given. When combined with
various tasks solely by altering the input prompt, without         other techniques, ICL represents a valuable approach to mit-
the need for task-specific fine-tuning. In his section, we clas-   igating hallucinations in LLMs. By leveraging the model’s
sify prompt design strategies for hallucination mitigation         ability to adapt to new tasks and information without pa-
into four major categories: template, instruction, tag, and        rameter updates, ICL can potentially improve factual accu-
in-context learning (ICL)-based prompts.                           racy and reduce erroneous outputs [151]. Moreover, Zhang
    Template-based prompts. Employ predefined structures           et al. [152] showed that ICL with iterative refinement en-
with placeholders, which allow for standardized input-             hances summary faithfulness, demonstrating its advantages
output formats across different examples. Recent research          in faithfulness, controllability, and overall quality. Similarly,
supports the effectiveness of template-based prompts in            Vu et al. [153] showed that few-shot prompts containing up-
mitigating hallucinations of LLMs [143], [144]. Jiang et al.       to-date information can improve factual accuracy.
[143] introduced a structured prompt-template framework
for AI-generated news articles, where key components, such         7.2   Retrieval-Based Techniques
as introduction, event, and argument, are used to guide            Retrieving external knowledge for LLMs can enhance their
the model in producing factually accurate content. The             factual grounding, contextual relevance, and overall accu-
proposed framework also involves a post-checking process           racy. The information contained in the model parameters
that verifies compliance between the structured input and          during pre-training is known as parametric knowledge. This
output, thereby reducing the occurrence of hallucinated            knowledge is static and may not encompass the most recent
information. Similarly, RefGPT [144] introduced structured         or domain-specific information. To overcome this limitation,
prompting for dialogue generation using three components:          non-parametric knowledge can be incorporated through
reference selection, basic prompting, and dialogue settings.       retrieval-based techniques. In the context of LLMs, knowl-
This setup ensures that the model draws solely from spec-          edge retrieval enables them to dynamically access external,




                                                       Template                    [143, 144]


                                                      Instruction                  [147, 148]
                                      Prompt
                                                         Tag                        [149, 150]

                                                         ICL                     [151, 152, 153]


                                                                                     Before                              [156, 157]


                                                        Stage                        During                                [158]

                                                                                      After                              [159, 160]

                                      Retrieval         RAG                   [161, 164, 165, 166]

                                                                                 Pre-training &
                                                                                                                      [167, 168, 169]
                                                                                  fine-tuning

                                                         KG                         Validation                    [170, 171, 172, 173]
               Hallucination
                Mitigation
                                                                                    Inference           [174, 175, 176, 177, 178, 179, 180, 181]


                                                         CoT                         [182, 183, 184, 185]

                                                        Self-
                                                                                     [186, 187, 188, 189]
                                                     consistency
                                     Reasoning
                                                      Iterative            [146, 190, 191, 192, 193, 194, 195, 196]
                                                     Refinement

                                                         CoX                    [197, 198, 199, 200, 201, 202]


                                                      Decoding              [203, 204, 205, 206, 207]

                                                     Knowledge
                                                                               [209, 210, 211, 212]
                                                     Distillation

                                                                                  Uncertainty-
                                                                                                                       [213, 214, 217]
                                                                                    aware

                                   Model-centric     Fine-tuning                      MTL                                  [218]

                                                                                     Prompt-
                                                                                                                           [219]
                                                                                     guided

                                                     Contrastive                      [222]
                                                      Learning

                                                     Cross-lingual
                                                                              [224, 225, 226, 227]
                                                       Learning


                                Fig. 8: The taxonomy of hallucination mitigation methods.


verified sources of data, such as search engines, databases,         Hallucinations are mitigated by restricting the generated
and specific text corpora. By interacting with these reliable        summarization to use only the retrieved reports. The system
sources, models can consult up-to-date and domain-specific           uses carefully designed queries to retrieve relevant content
data during generation, which in turn improves the fac-              from the reports and prompts the LLM to summarize it in
tual accuracy of their outputs [154], [155]. Retrieval-based         alignment with the guidelines. Peng et al. [157] introduced
techniques can be classified into three categories based on          LLM-AUGMENTER that mitigates hallucination in GPT-
the phase of accessing external resources: before, during,           3.5 for information-seeking dialogue and open-domain QA.
and after generation [9]. We used these knowledge retrieval          It incorporates external knowledge and refines prompts
stages to categorize retrieval-based techniques proposed for         before generation. The LLM-AUGMENTER optimizes the
hallucination mitigation.                                            policy module using RL to retrieve and consolidate external
    Retrieving knowledge before generation involves                  knowledge, refine prompts, and iteratively improve the
querying external resources to find relevant information             quality of the answers based on utility input.
related to the user’s query before generating the response.              Knowledge retrieval during generation involves query-
This approach helps mitigate hallucination by constrain-             ing external knowledge during the process where an LLM
ing the model to generate responses based on verified                is generating the response. The retrieved information is
sources rather than relying solely on its internal knowledge.        combined with the original query to provide context for
This ensures that the generated content is grounded in               the LLM. Nathani et al. [158] proposed a technique that
factual data. Ni et al. [156] developed a framework for              iteratively refines hallucinated text and reasoning errors
summarizing sustainability reports aligned with the Task             using multiple feedback sources. The framework begins
Force on Climate-related Financial Disclosures guidelines.           with a base model that generates an initial response. This



response then undergoes an iterative refinement process,         utilizes pre-trained components that are already loaded
where feedback from various modules is applied across            with extensive knowledge. Consequently, it can immedi-
multiple iterations. The feedback modules are designed to        ately access and integrate a broad range of data without
address specific error categories, including factual inaccura-   the need for additional training.
cies, commonsense mistakes, and redundancy. Feedback can             RAG-HAT [161], a hallucination-aware tuning pipeline,
be provided by pre-trained LLMs or external tools. Then, a       employs a three-step process: detection, rewriting, and mit-
refiner model, which is the same as the base model, utilizes     igation. It uses a fine-tuned detection model to identify
the feedback to refine its response.                             hallucinations and provide detailed descriptions, which are
    Knowledge retrieval after generation involves engaging       then used to guide GPT-4 in revising the RAG output.
in a fact-checking or validation process by cross-referencing    The revised outputs are used to create a preference dataset
the initial response against a knowledge source. Gao et al.      for direct preference optimization training, resulting in re-
[159] aimed to detect and mitigate hallucinations in LLMs        duced hallucination rates and improved answer quality.
after generation by finding attribution and post-editing un-     TRAQ [164] combines RAG with conformal prediction to
supported content. The authors introduced RARR, a system         provide statistical correctness guarantees for QA. It applies
that extracts evidence from external sources to validate the     conformal prediction to both the retrieval and LMs, which
output text’s dependability. The RARR framework consists         generates sets of passages that contain relevant information
of two main phases: research and revision. In the research       and answers to generate the correct response. Furthermore,
phase, a query generator formulates inquiries regarding          Ayala et al. [165] demonstrated that using a well-trained
various aspects of the text, while a retriever seeks support-    retriever can significantly decrease hallucination rates, par-
ing evidence. In the revision phase, an agreement model          ticularly in out-of-domain settings. This approach allows
identifies discrepancies between the text and the evidence,      for the deployment of smaller LLMs without compromising
followed by an edit model that revises the text if necessary.    performance, which makes it especially useful for enterprise
The process concludes with an attribution report linking         applications with resource constraints. In another study,
the revised content to its sources. Similarly, Huo et al.        Rowen et al. [166] proposed a framework that enhances
[160] proposed a validation method that enables an LLM           LLMs with an adaptive retrieval augmentation process
to cross-check its generated answers against retrieved evi-      tailored to address hallucinated outputs. The authors em-
dence. The authors suggested a retrieval pipeline consisting     ployed a consistency-based hallucination detection module,
of sparse retrieval, dense retrieval, and neural re-rankers.     which assesses the model’s uncertainty regarding the input
This pipeline has been employed in two ways. First, the          query by evaluating the semantic inconsistencies in various
generated response and query were used to retrieve external      responses generated across different languages or models.
evidence, which was then employed to validate the output.        When high uncertainties in the responses are detected, it
In the second way, the LLM extracted multiple factual state-     activates the retrieval of external information to rectify the
ments from the response, each of which was independently         model outputs.
verified against retrieved evidence.
    Recent approaches [83], [161], [162], [163] that depend      7.2.2 Knowledge Graph
on retrieving knowledge after generation have significantly      KG, also known as semantic networks, systematically ar-
integrated RAG and KG for hallucination mitigation in            ranges information in a structured manner to establish rela-
LLMs. RAG and KG represent effective solutions in helping        tionships among real-world entities [162]. It serves as a pow-
LLMs avoid hallucinations by grounding their responses on        erful tool for storing and querying complex information in
reliable and fact-checked information. RAG enhances the          a way that mirrors how humans conceptualize knowledge.
output of an LLM with dynamic retrieval and incorpora-           KG has been used by researchers to mitigate hallucination
tion of external and up-to-date knowledge, which decreases       by incorporating it with pre-training and fine-tuning, vali-
dependency on static, parametric knowledge and improves          dation, and inference stages of the LLM development cycle
adaptability in real-world applications. KGs, on the other       [163].
hand, offer structured, relationship-centric representations         Pre-training and fine-tuning stages. KG helps miti-
of facts that capture entities and their relations. They can     gate hallucinations introduced during pre-training and fine-
be integrated at various stages from LLMs’ pre-training and      tuning stages by providing LLMs with access to accu-
fine-tuning to inference and validation. This technique en-      rate, structured, and up-to-date factual information, thereby
ables models to navigate complex relationships and facts ac-     grounding generation in verifiable knowledge. It provides
curately. Both techniques complement each other to improve       structured data about entities and their relationships, which
LLM capabilities and contribute to more reliable factual         enhances LLMs’ comprehension and helps them generate
consistency outputs, which enables LLMs to generate text         language that accurately reflects real-world complexities.
with better accuracy in various tasks.                           ERNIE 3.0 [167] integrates KGs by linking words to entities
                                                                 through knowledge masking, allowing the model to capture
7.2.1 Retrieval Augmented Generation                             both contextual and relational information more effectively.
RAG enhances LLMs by retrieving relevant external docu-          Similarly, KGLM [168] leverages KG triples in pre-training
ments at inference time, which enables the LLM to ground         and fine-tuning stages using an additional entity-relation-
its responses in factual evidence beyond its parametric          type embedding layer. This layer strengthens the model’s
training data [83]. It consists of two components, a retriever   ability to understand KG structures, recall factual data, and
and a generator, which work together in a retrieve-then-         improve accuracy in knowledge-based tasks. KG-Adapter
read pipeline. Unlike traditional retrieval techniques, RAG      [169] integrates KGs through parameter-efficient fine-tuning



using dual-perspective adapter modules. This approach en-       methods that rely solely on user input to query the knowl-
codes node-centered and relation-centered KG structures         edge graph, KGR retrofits LLM initial draft responses using
while reducing knowledge conflicts by 38% compared to           factual knowledge stored in KGs. The framework lever-
prompt-based methods, which require only 28M trained            ages LLMs to extract, select, validate, and retrofit factual
parameters for 7B-scale LLMs.                                   statements in model-generated responses, enabling an au-
    Validation stage. KGs can add a fact-checking layer,        tonomous knowledge-verification and refinement process
which provides a comprehensive explanation to justify the       without additional manual effort.
LLM’s decision. FOLK [170] is a fact-verification method
that employs KGs using first-order-logic predicates to verify
                                                                7.3   Reasoning-Based Techniques
claims in online misinformation. It can also provide expla-
nations of its findings to help human fact-checkers compre-     Reasoning-based mitigation techniques in LLMs aim to ad-
hend and evaluate the model’s outputs. Emerging directions      dress complex tasks that require logical and step-by-step
include neuro-symbolic integration [171], which combines        thinking. Traditional LLMs often struggle with intricate rea-
neural retrieval with logical KG reasoning, and autonomous      soning and may produce factually inaccurate or misleading
retrofitting [172], which iteratively aligns LLM outputs with   outputs when handling tasks that require multi-step think-
KG-derived constraints. An approach for generating faithful     ing or inference. To mitigate this, several reasoning-based
text from KGs with noisy reference text has been introduced     methods, such as CoT reasoning, self-consistency, iterative
in [173]. This method incorporates contrastive learning to      refinement, and Chain-of-X (CoX) prompting, were used to
enhance the model’s ability to differentiate between faithful   improve reasoning accuracy and reduce hallucinations.
and hallucinated information. It encourages the decoder to          CoT Reasoning. CoT is an improved version of few-
generate text that aligns with the input graph. Additionally,   shot prompting [145] that follows a step-by-step approach
it employs a controllable text generation technique that        in natural language to decompose multi-step problems into
allows the decoder to manage the level of hallucination in      intermediate steps. This method provides an interpretable
the generated text.                                             view of the model’s reasoning process, which enables better
    Inference stage. KGs can also mitigate hallucinations in    insight into how the model arrives at its conclusions. Zhao
the inference stage by employing KG-augmented retrieval.        et al. [182] proposed a zero-shot CoT reasoning method
This allows LLMs to retrieve the appropriate subgraph for       by incorporating logical thoughts (LoT), which employs
answering a query grounded by real-world facts. KAPING          symbolic logic to validate and revise each step. Therefore, it
[174] retrieves related triples from KGs for zero-shot QA       addresses and mitigates hallucinations arising from logical
by matching entities in questions. Similarly, StructGPT [175]   flaws directly. Sultan et al. [183] introduced Structured CoT
enhances LLM responses using data from KGs, tables, and         (SCoT), which uses a structured state-machine methodology
databases and employing structured queries for informa-         to systematically oversee content reading, utterance genera-
tion retrieval. In another study, KG is used to enhance         tion, and hallucination mitigation phases. This method im-
evidence acquisition [176]. CuriousLLM [176] is proposed,       proves the model’s faithfulness and reduces hallucinations
which builds and traverses a passage-level KG where nodes       in content-grounded tasks. Li et al. [184] further adapted
represent documents and edges reflect learned semantic          the SCoT approach specifically for code generation tasks,
connections. The LLM agent generates follow-up questions        introducing programming structures, such as sequential,
that guide traversal over this graph to locate missing evi-     branching, and looping steps, as intermediate representa-
dence across documents. The proposed technique actively         tions. Their approach explicitly guides LLMs to follow struc-
identifies what information is still missing and continues      tured programming logic, which enhances the logical cor-
retrieval until sufficient support is found, or terminates      rectness, clarity, and readability of the generated code. This
early when evidence is complete.                                structured reasoning substantially mitigates hallucinations
    For complex reasoning tasks, IRCoT [177] integrates         and improves code accuracy, outperforming traditional CoT
KGs with CoT to iteratively guide retrieval and reasoning       prompting by a considerable margin across multiple pro-
for multi-step questions. Likewise, RoG [178] uses KGs to       gramming benchmarks. Li et al. [185] improved the causal
construct reliable reasoning pathways grounded in diverse       reasoning capabilities of LLMs by introducing CDCR-SFT.
relationships to improve accuracy. Moreover, PoG [179] re-      The authors fine-tune LLMs to explicitly construct causal
trieves a question-specific subgraph for each query, explores   graphs and reason over them before producing answers. By
multi-hop reasoning paths between relevant entities, and        shifting reasoning from surface token patterns to structured
feeds these structured paths into the LLM as evidence for       causal relationships, the model reduces logically inconsis-
answer generation. Hallucinations are mitigated by con-         tent hallucinations that arise from flawed reasoning chains.
straining the model to reason over verifiable KG paths,             Self-Consistency. Building on the success of CoT, Wang
pruning noisy or irrelevant branches, and verifying whether     et al. [186] introduced a self-consistency approach, which
the retrieved paths provide sufficient support before pro-      replaces the decoding strategy of CoT. Unlike the original
ducing an answer. For real-time applications, FactGenius        CoT method, the authors proposed the concept of gen-
[180] combines LLM-based connection filtering with Leven-       erating multiple reasoning chains for a certain topic. The
shtein distance validation, which improved fact verification    final answer is determined by conducting a majority vote
F1-scores by 12% on the FactKG benchmark through fuzzy          or by selecting the most consistent response from several
relation mining. Moreover, KG-based retrofitting (KGR)          chains. Li et al. [187] extended self-consistency by propos-
[181] incorporates LLMs with KGs to mitigate factual hal-       ing DIVERSE. This method generates multiple reasoning
lucination during the reasoning process. Unlike previous        pathways through diverse prompts, systematically validates



each reasoning step, and utilizes weighted voting according        based feedback. A2R employs natural language feedback
to step consistency. The step-aware approach significantly         from metric assessments, which progressively enhances re-
reduces hallucinations by isolating and rectifying errors          sponses according to metrics like accuracy, fluency, and
at the step level rather than the whole chain. Similarly,          citation precision to reduce hallucination. In another study,
Liang et al. [188] proposed an RL from knowledge feedback          Zhang et al. [194] introduced PREFER, a refinement-focused
(RLKF) technique, which integrates self-consistency and            ensemble method, which works by continuously merging
internal knowledge state assessments. RLKF enhances the            and refining prompts through identifying the limitations of
model’s ability to resist factual hallucinations by reinforcing    previous iterations, enhancing model stability and overall
the consistency between the internal knowledge state and           output quality. In addition, Huang et al. [195] demonstrated
external outputs. Xu et al. [189] proposed SaySelf, a method       that LLMs can enhance their reasoning capabilities by gener-
for training LLMs to produce self-reflective rationales condi-     ating high-confidence rationale-augmented responses. Their
tioned on inconsistencies across multiple sampled reasoning        approach integrates unsupervised iterative refinement with
trajectories. SaySelf explicitly prompts the model to provide      self-consistency and feedback-based fine-tuning, which sig-
precise confidence estimates and rationales that detail its        nificantly improved reasoning performance. Cheng et al.
knowledge gaps and uncertainty. This method substantially          [196] proposed HaluSearch models generation as a slow,
improves confidence calibration and effectively mitigates          step-by-step reasoning search using tree search (e.g., MCTS).
hallucinations.                                                    Each intermediate reasoning step is scored by a reward
    Iterative Refinement. CoT has substantially improved           model that estimates hallucination risk, and the model
the reasoning abilities of LLMs, thus reducing hallucination.      dynamically switches between fast and slow thinking. This
Nevertheless, if CoT initiates the sequence with erroneous         prevents early reasoning errors from propagating and pro-
reasoning, it fails to rectify the reasoning errors or factual     motes more reliable reasoning paths.
inaccuracies that may occur during the reasoning process.              CoX Reasoning. The sequential thought structure of
This limitation often leads to hallucinations. Inspired by the     CoT served as the inspiration for several techniques re-
way people edit their written content, Madaan et al. [146]         ferred to as CoX techniques in this survey. They have
proposed Self-Refine to enhance the generated output by            been designed to tackle problems in various tasks and
an LLM through iterative refinement, which depends on              domains by merging with other techniques, such as iter-
domain-specific data, external supervision, and RL. How-           ative refinement and knowledge retrieval, to mitigate hal-
ever, these techniques require large annotated datasets that       lucination. These techniques include chain-of-verification
are unavailable for several domains. Self-Refine leverages         (CoVE), chain-of-natural language inference (CoNLI), chain-
the concept of LLMs as self-reviewers by using a single            of-question (CoQ), chain-of-knowledge (CoK), and chain-of-
LLM that acts as a generator, refiner, and feedback provider,      notes (CoN).
relying solely on prompt designs without the need for fine-            The CoVE prompting approach, inspired by the notable
tuning. Self-Refine depends on an appropriate LLM and              success of the reasoning chains and self-refine paradigms,
three prompts (for initial response generation, feedback, and      aims to mitigate hallucination by enabling an LLM to formu-
refinement). It works by generating an initial output based        late verifiable questions to authenticate its reasoning [197].
on an input sequence, providing feedback on the output,            The model initially produces a baseline response to serve as
then subsequently refining the output in accordance with           a reference for further improvements. The LLM then gen-
the self-generated feedback. It alternates between feedback        erates verification questions to check the factual accuracy
and refining until a specified condition is achieved. Sim-         of its statements. Several verification execution strategies
ilarly, Shinn et al. [190] proposed Reflexion method that          have been proposed, such as joint, 2-step, factored, and
involves finding the subsequent optimal solution in plan-          factor+revise methods. In the joint execution technique, the
ning using ReAct [191]. The Reflexion uses a long-lasting          LLM generates verification questions and answers within a
memory that allows an agent to recognize its own mistakes          single prompt, while the 2-step method generates them in
and autonomously derive insights from its mistakes and             two separate prompts. Conversely, the factored technique
iteratively adapt its behavior over time. Instead of using RL,     handles each verification question in a separate prompt,
Reflexion leverages an external verbal feedback mechanism.         while factor+revise assesses the coherence between the base-
This technique operates by employing an actor that gener-          line response and the verification answers to produce the
ates an output and an evaluator to evaluate the generated          final verified response. The reported results show that the
output. The process continues until the evaluator thinks the       factor+revise method yields the strongest overall factuality
agent’s output is correct or when a maximum number of tri-         score compared with other techniques.
als is reached. In contrast to Self-Refine, Reflexion explicitly       The CoNLI prompting approach uses a hierarchical
integrates external evaluations and memory mechanisms,             inference-based framework to detect and mitigate un-
which enhances learning effectiveness over both short-term         grounded hallucinations in LLMs [198]. A detection agent
and long-term experiences. Paul et al. [192] developed RE-         breaks down the baseline response into claims at the sen-
FINER by applying structured intermediate criticism from           tence and entity levels. Each sentence or entity is treated as
a critic model. The critic model critiques single reasoning        a hypothesis, which is then verified using NLI against the
steps and allows iterative refinement by identifying and cor-      original text. A mitigation agent subsequently corrects de-
recting inaccuracies throughout the reasoning process. Like-       tected hallucinations by post-editing the baseline output to
wise, Lee et al. [193] introduced the Ask, Assess, and Refine      address inconsistencies. The results show that CoNLI-GPT-4
(A2R) methodology, which methodically assesses outputs             consistently outperforms other approaches across multiple
for factual accuracy and hallucinations through metric-            datasets in both hallucination detection and mitigation.



The CoQ prompting approach enhances CoT by breaking             and fact-based. This survey categorizes the model-centric
down complex questions into multiple sub-questions and          training and adaptation-based approaches for hallucination
incorporating a knowledge retrieval mechanism [199]. CoQ        mitigation into four main strategies: optimizing decoding
requires that each reasoning step be supported by at least      methods, leveraging knowledge distillation, applying su-
one retrieved knowledge source. This approach prevents          pervised fine-tuning, and adopting self-learning techniques.
hallucination during reasoning and ensures the model’s              Decoding Strategies. Decoding is the mechanism used
cognitive steps are grounded in factual information. On         to convert encoded representations of the LLMs’ output
average, results show that CoQ reduces factual inaccuracies     into comprehensible text. During decoding, the model it-
by 31% compared to CoT alone and by 38% relative to the         eratively selects tokens from its vocabulary, which build
two most prevalent LLMs.                                        contextually relevant and syntactically accurate sentences.
     The CoK prompting approach uses KGs to enable LLMs         However, decoding strategies may contribute to the genera-
to perform knowledge reasoning [200]. CoK employs two           tion of hallucinated text [76]. Selecting an effective decoding
methodologies: data building and model learning. Data           technique can help the model generate output that is more
building involves three steps: rule mining, which derives       grounded in context and aligned with user expectations.
rules from KG triples; knowledge selection, which selects       Recent studies have shown promising results in mitigating
appropriate knowledge for CoK data construction; and            hallucinations by building upon the on-the-shelf decoding
sample generation, which converts knowledge into natural        strategies. Chen et al. [203] introduced DoLa to mitigate
language. Model learning uses both conventional behavior        hallucination in LLMs without the need for fine-tuning
cloning and a trial-and-error approach to mitigate rule over-   or external retrieval mechanisms. DoLa enhances factual
fitting, which can cause hallucination. This trial-and-error    accuracy by exploiting differences between mature (higher)
mechanism enables the model to explore various reasoning        and premature (lower) transformer layers. Evaluated on the
paths and apply alternative rules when critical information     TruthfulQA benchmark, DoLa attained a 12–17% improve-
is absent. In out-of-domain evaluation, CoK demonstrated        ment in the truthfulness scores in various LLMs. Similarly,
superior performance in knowledge reasoning compared            Shi et al. [204] enhanced the contextual faithfulness of text
to baseline methods. Another CoK technique [201] miti-          generation by reducing the influence of prior knowledge
gates hallucination by dynamically incorporating knowl-         during the decoding process. They proposed a contrastive
edge from heterogeneous sources, including structured and       decoding technique that modifies output probabilities to
unstructured data. This framework comprises three stages:       enhance the influence of the given context. The context-
reasoning preparation, dynamic knowledge adaptation, and        aware decoding strategy operates by contrasting the output
answer unification. Initially, CoK formulates several ra-       probabilities of the model when the context is included and
tionales and selects answers lacking majority consensus         excluded from the prompt. This ensures that the model
for further processing using CoT with self-consistency. An      gives more weight to contextually relevant tokens, which
adaptive query generator dynamically formulates queries         reduces reliance on outdated or incorrect prior knowledge.
tailored for various knowledge sources to refine the ratio-     This approach has been evaluated on a summarization
nales, correcting each step to address error propagation. Ex-   task and reported an enhancement of factuality by 14.3%.
periments on knowledge-intensive tasks, including factual,      Waldendorf et al. [205] applied contrastive decoding in
medical, physics, and biological domains, show that this        multilingual machine translation settings. Their approach
CoK framework substantially improves LLM performance.           maximizes the log-likelihood difference between an expert
     The CoN prompting approach is an approach to improve       model and a deliberately source-detached amateur model,
the relevancy of retrieval-augmented LMs (RALMs) [202].         which significantly enhances translation fidelity and miti-
CoN addresses two primary challenges: handling noisy            gates hallucinations. Furthermore, Sennrich et al. [206] pro-
and irrelevant information and recognizing the absence of       posed source-contrastive and language-contrastive decod-
sufficient knowledge. This enables RALMs to assess their        ing methods, contrasting the correct input segment with
knowledge sufficiency and reply with ”unknown” when in-         randomly selected or incorrect segments. This approach
formation is lacking. The main innovation of CoN is the gen-    substantially reduced severe hallucinations, which is de-
eration of brief reading notes for each document retrieved      fined by a chrF2 score below 10, by 67–83% and oscillatory
by the model. These notes summarize key points in each          hallucinations by 75–92% across various language pairs. In
document, allowing the model to evaluate their relevance        order to reduce the response latency of existing methods,
to the input query. When retrieved documents lack relevant      Chang et al. [207] introduced monitoring decoding, which
details, CoN can instruct the model to acknowledge its limi-    monitors token-by-token generation using a factuality mon-
tations by answering ”unknown” or providing justifications      itor that evaluates partial responses during decoding. When
based on available data. Evaluations across open-domain         a token or span is predicted to cause hallucination, the
QA datasets show significant improvements, with a 7.9%          model intervenes immediately using a tree-based resam-
average increase in exact match scores for noisy retrieved      pling strategy to revise only the risky tokens instead of
documents and a 10.5% increase in rejection rates for out-of-   regenerating the whole answer. This reduces the number
scope questions.                                                of overconfident hallucinated tokens at their source during
                                                                generation.
7.4   Model-centric Training and Adaptation                         Knowledge Distillation. It is a method by which a
These processes involve refining model architectures, ad-       smaller model, the student, learns to replicate the per-
justing training strategies, and integrating advanced tech-     formance of a larger, well-performing model, the teacher,
niques that make outputs coherent, contextually relevant,       without significant performance loss [208]. Recent stud-



ies have shown that knowledge distillation is effective in        uncertainty-aware fusion (UAF), which reduces hallucina-
mitigating LLM hallucinations. McDonald et al. [209] used         tion using an ensemble of multiple LLMs combined through
knowledge distillation with the Mistral LLM, demonstrating        uncertainty estimation. Each model provides both an an-
substantial improvements in factual accuracy and signifi-         swer and a confidence signal about the factual correctness.
cant reductions in hallucination rates on the MMLU bench-         A fusion module then selects or combines responses from
mark. The proposed approach used temperature scaling              models that are both accurate and self-aware. The proposed
and intermediate layer matching, which enables a compact          approach enhanced factuality while also maintaining effi-
student model to emulate a larger teacher model. Therefore,       ciency.
the approach ensures more contextually accurate outputs               Multi-task Learning. The hallucination issue may stem
without compromising computational efficiency. Similarly,         from the dependence of the training process on a single
Nguyen et al. [210] proposed a smoothed knowledge dis-            dataset, which limits the model’s ability to grasp the true
tillation method, where soft labels from a teacher model          features of the task. Incorporating appropriate auxiliary
replaced traditional hard labels, to reduce the model’s over-     tasks alongside the primary task during fine-tuning helps
confidence and encourage better factual grounding. This           reduce the model’s susceptibility to hallucination issues
method was evaluated on summarization benchmarks, such            [5]. The process of fine-tuning a model on several tasks
as CNN/Daily Mail and XSUM, and it successfully lowered           concurrently is known as MTL. Learning multiple tasks
hallucination rates while maintaining robust performance          simultaneously enables models to gather general informa-
across general natural language processing tasks. Liu et          tion beyond task-specific properties. Consequently, learning
al. [211] designed a multi-task learning (MTL) paradigm           performance can improve by sharing information across
to distill self-evaluation capabilities from the GPT-3.5-turbo    tasks rather than learning each task separately. For example,
into smaller models such as the T5-base. This approach            in an MTL framework, encompassing abstractive summa-
uses few-shot CoT prompts and self-assessment output to           rization and fact-checking makes the model learn to produce
create rationales and pseudo-labels for training. The results     coherent summaries and to validate the factual accuracy of
in the SVAMP and ANLI datasets demonstrated significant           the information it generates. The fact-checking task helps to
improvements in accuracy. Elaraby et al. [212] introduced         prevent the model from producing erroneous or fabricated
HALO, a framework addressing hallucinations in smaller            statements by explicitly instructing it to assess and verify
LLMs such as BLOOM 7B through HALOCHECK, which is                 factual assertions. However, it is essential to carefully select
a BlackBox knowledge-free metric to evaluate hallucination        tasks for concurrent learning to avoid the risk of negative
severity. HALOCHECK uses entailment-based methods to              transfer, which occurs when learning conflicting features
assess consistency, which outperformed existing metrics in        [218].
detecting contradictions. To mitigate hallucinations, the au-         Prompt-guided Learning. Prompt retrieval and selection
thors proposed knowledge injection, fine-tuning the model         techniques integrated with fine-tuning have further ex-
with domain-specific knowledge, and a teacher-student ap-         panded the capabilities of LLMs to mitigate hallucinations
proach in which GPT-4 provided detailed guidance selec-           [219]. Cheng et al. [219] proposed UPRISE, which is a
tively triggered by HALOCHECK. These techniques signif-           method of detecting and mitigating hallucinations by en-
icantly improved factual consistency and reduced halluci-         hancing the retrieval of relevant prompts that help the LLM
nations, demonstrating HALO’s effectiveness in enhancing          in making more accurate conclusions. The authors fine-
weak LLMs’ reliability in domain-specific tasks.                  tuned a lightweight model to autonomously extract prompts
     Supervised Fine-Tuning. Although supervised fine-            from a pool of prompts based on a zero-shot task input. The
tuning can produce hallucinated text, it can be an effective      model has two encoders: one for processing the task input
hallucination mitigation strategy when specific factors are       and the other for processing the prompt. During training,
carefully considered. Incorporating grounded input into the       the model maximizes the similarity between task inputs
fine-tuning dataset enables the model to prioritize accurate      and positive prompts while minimizing the similarity to
factual content over speculative knowledge [213]. For exam-       negative prompts through contrastive learning. UPRISE
ple, if the model frequently hallucinates in text summariza-      evaluates retrieval scores according to the LLM’s accuracy in
tion tasks, fine-tuning with a dataset containing grounded        anticipating the proper label. Upon fine-tuning the retriever,
content is beneficial, since it guides the model in aligning      the fine-tuned retriever is employed to extract the most
generated summaries closely with the original content.            relevant prompts from the prompt pool for a certain input.
     Uncertainty-aware Learning. Training the model to asso-      The prompts obtained are combined with the task inputs
ciate uncertainty with lower confidence scores is helpful         and forwarded to the LLM to produce the final output.
in uncertain situations [214]. For instance, while summa-         The proposed method was evaluated using ChatGPT, and
rizing a detailed medical article with specialized terms and      UPRISE outperformed vanilla zero-shot prompting on fact-
domain-specific information, the model can be trained to          checking tasks.
flag areas of uncertainty. As a result, the model may either          Self-learning via Contrastive Learning. Contrastive
omit this information from the summary or openly indicate         learning is a self-supervised technique that aims to acquire
limitations (e.g., ”certain details were not specified”). Simi-   valuable data representations by differentiating between
larly, instructional supervision can support this approach by     positive and negative samples. The fundamental concept
teaching the model that disclaiming uncertain information is      is to reduce the proximity of representations of similar
preferable to generating incorrect data. This method allows       positive pairs while increasing the distance between rep-
the model to respond with ”I don’t know” when informa-            resentations of dissimilar pairs [220]. In hallucination mit-
tion is unavailable [215], [216]. Dey et al. [217] introduced     igation, contrastive learning enhances models’ ability to



acquire precise representations by focusing on what makes          suitable high-resource language, translates the query into
data points factually or contextually consistent. By train-        the selected language, generates a response in the selected
ing on positive pairs (e.g., grounded factual content) and         language, and replaces or integrates the answer back into
negative pairs (e.g., mismatched or hallucinated content),         the original language. Experiments on six LLMs and five
a model can better distinguish between factual and non-            bilingual datasets show performance gains and reduced
factual information [5]. For example, contrastive learning         cross-language disparities.
can be applied to train a model for text summarization,
with positive samples representing reference summaries
                                                                   7.5   Mitigation Challenges
and negative samples indicating hallucinated summaries.
Contrastive learning helps to differentiate between them,          Hallucination mitigation techniques aim to prevent LLMs
thereby aiding in the reduction of hallucination [221]. Sun        from producing responses that are factually inaccurate,
et al. [222] introduced MixCL, a mixed contrastive learning        ungrounded, or contextually inconsistent. Most halluci-
approach specifically designed to mitigate hallucination in        nation mitigation approaches proposed in the literature
conversational language models. By employing a combina-            fall into two categories: retrieval and reasoning-based.
tion of hard negative sampling strategies and span-level           Retrieval-based approaches leverage external knowledge,
mixing of positive and negative knowledge samples, MixCL           while reasoning-based approaches employ logical, step-by-
significantly improved the models’ abilities to distinguish        step reasoning to improve the factual grounding, contextual
factual content from hallucinated information. However, the        relevance, and overall accuracy of LLM outputs. Despite
selection of positive and negative pairs, while beneficial,        substantial progress in retrieval-based hallucination miti-
must be monitored to prevent the emergence of suboptimal           gation, these approaches still face several challenges. The
representations.                                                   effectiveness of these methods is fundamentally constrained
    Cross-Lingual Learning. Cross-lingual transfer learn-          by the coverage, timeliness, and quality of the external
ing enables LLMs to exploit knowledge that is richer or            knowledge sources. Therefore, if relevant information is
more complete in one language, often English, to generate          missing, outdated, or inconsistent, hallucination mitigation
responses in another low-resource language. Pre-training           may fail or even introduce new errors [124]. Furthermore,
a bi-lingual or multi-lingual model, then fine-tuning it on        integrating retrieval results with LLMs often introduces ad-
limited data from a low-resource language can speed up             ditional latency and complexity into the generation pipeline,
model convergence and improve performance [223]. How-              which can limit scalability and real-time applicability [163].
ever, it can also increase the risk of hallucination if the data       Similarly, reasoning-based mitigation techniques, such
contains a language mismatch or noisy tokens. Cross-lingual        as CoT, self-consistency, and iterative refinement, have some
learning can contribute to mitigating hallucination in the         limitations. The computational cost of deploying reasoning-
pre-training, fine-tuning, and inference stages.                   based methods can be substantial, since these methods de-
    During cross-lingual continual pre-training, noisy to-         pend on generating multiple reasoning chains or perform-
kens, such as artifacts and emojis, can distort the learned        ing step-by-step refinements to mitigate hallucination [196].
distribution of the data in the new language, which leads          Moreover, iterative and self-correction strategies cannot
to hallucination. Fan et al. [224] proposed InfoLoss, which        fully guarantee error removal, even when supported by self-
augments cross-entropy with normalized pointwise mutual            verification and multi-turn feedback [228]. Additionally, if
information weights over local context. This is to down-           initial reasoning chains are flawed, subsequent refinements
weight tokens with low co-occurrence support and thereby           may amplify rather than correct errors, which underscores
limit their influence. Continual pre-training Llama-2-7B           the fragility of self-improvement strategies when the under-
with InfoLoss over a bi-lingual corpus improved cross-             lying logic is unsound [229].
lingual transfer on 12 benchmarks and reduced hallucina-               Mitigating hallucination through designing well-crafted
tions relative to size-matched baselines. Zheng et al. [225]       prompts has been investigated in some studies. Although
developed curriculum-based contrastive learning, which             prompt designs effectively guide the model to the desired
aligns multilingual semantic spaces during continued pre-          output, they have several drawbacks. Designing and re-
training.                                                          fining high-quality domain-specific prompts that maximize
    Qiu et al. [226] proposed mFACT, a multilingual fac-           accuracy and minimize errors can be resource-intensive, re-
tuality metric designed to evaluate hallucinations beyond          quiring both human expertise and iterative testing. Prompt
English. Instead of building separate evaluators for each lan-     designs may also be constrained to specific tasks, which
guage, mFACT leverages existing English factuality metrics         limits their generalization to a wide range of applications.
by translating their supervision signals into the target lan-      While recent advances in automatic prompt optimization,
guage. When applied to summarization tasks, incorporating          such as prompt tuning [230], [231] and prefix-tuning [232],
mFACT into loss-weighted training allowed the model to             show promise in reducing manual effort, integrating these
down-weight unfaithful examples, which reduced halluci-            approaches with hallucination mitigation techniques needs
nations and improved overall summary quality across six            to be investigated.
languages. Zheng et al. [225] developed a cross-lingual COT            Other researchers have proposed some enhancements
that reasons in a high-resource language before producing          to the model architecture or fine-tuning strategies to mit-
the final answer in the target low-resource language.              igate hallucinations in the LLMs outputs. Despite notable
    Huang et al. [227] developed a low-resource knowl-             progress in model development and fine-tuning strategies
edge detector that flags the query contents that are written       for hallucination mitigation in LLMs, several challenges
in a low-resourced language. The system then selects a             remain. Decoding strategies, such as contrastive, source-



aware, and DoLa methods, have improved contextual faith-         On the other hand, hallucination mitigation datasets place
fulness but can still struggle with generalization across        an emphasis on providing high-quality, factually correct,
domains and sensitivity to parameter tuning [203], [204],        and contextually grounded input-output pairs. They often
[206]. Knowledge distillation approaches are constrained by      include external references or grounding information, such
the quality of teacher models and can inadvertently transfer     as retrieval-based support documents that foster models to
biases or hallucinations. Moreover, their reliance on com-       produce outputs that are more reliable and faithful.
putationally intensive methods and high-quality data can             Hallucination detection datasets can be used for miti-
limit scalability, especially for multilingual or specialized    gation by repurposing the annotated data to guide model
domains [209], [210]. Supervised fine-tuning requires large,     training or refinement processes that directly address hal-
reliably annotated datasets, which are often unavailable         lucination. They can be used to fine-tune the model with
or costly to produce for low-resource tasks. Furthermore,        explicit negative examples, create contrastive learning tasks,
MTL can result in negative transfer and overfitting if aux-      or analyze hallucinated outputs to design more effective
iliary and primary tasks are not well-aligned [5], [213].        prompts. It can also be integrated into the generation
Contrastive learning is powerful for distinguishing factual      pipeline to flag or reject hallucinated outputs before present-
from hallucinated content, but is sensitive to the choice and    ing them to the user. Table 4 compares the publicly available
quality of positive and negative samples [221], [222]. Cross-    datasets for hallucination detection and mitigation.
lingual learning offers promise but suffers from increased           Table 4 indicates that QA and summarization NLG tasks
hallucination rates in low-resource or syntactically diver-      are predominant, being the principal tasks for which hal-
gent languages, which requires extensive resources and           lucination detection and mitigation have been evaluated.
careful parameter sharing [233], [234].                          English remains the leading language in detecting and miti-
    The observed limitations across mitigation strategies in-    gating hallucination. This is due to its high resources in sev-
dicate that no single approach can address all hallucination     eral domains. Other languages are starting to emerge, such
failure modes, underscoring the need for domain-aware,           as German (WMT18, Absinth), Arabic (Halwasa), Chinese
task-adaptive pipelines that combine complementary tech-         (UbgEval), and multi-lingual datasets (HalOmi). Moreover,
niques. Retrieval-based approaches tend to be more ben-          it is shown that most of the proposed datasets support
eficial in knowledge-intensive domains, such as medicine,        both hallucination detection and mitigation experiments,
law, and finance. However, retrieval-based mitigation is less    which provide reliable benchmarks for evaluating different
reliable in low-resource languages or rapidly evolving do-       techniques. In addition, the ground-truth labels are predom-
mains, where trustworthy sources are scarce or inconsistent.     inantly derived from human evaluation or human-curated
In contrast, reasoning-based strategies are more helpful for     references, ensuring high-quality factual annotations even
multi-step reasoning tasks, such as math logical QA, but         when the initial source material comes from Wikipedia,
may not be useful in domains where hallucinations arise          news articles, or model-generated text.
from missing or incorrect world knowledge rather than                Tables 2 and 5 show that hallucination detection and mit-
from flawed reasoning chains. Prompt-based and decoding-         igation remain highly task- and benchmark-dependent. No
based mitigation techniques often show gains in structured       single detection or mitigation method consistently outper-
or well-defined tasks, such as summarization or informa-         forms others across all datasets. The performance of detec-
tion extraction, where instructions can more tightly control     tion and mitigation techniques fluctuates under domain and
faithfulness to input. However, their effectiveness declines     task shifts. Furthermore, the diversity of benchmarks and
in open-ended generation settings, where hallucinations          evaluation setups complicates direct comparisons, which
arise from broad knowledge gaps rather than instruction-         underscores the need for standardized evaluation protocols
following failures. Similarly, model-centric approaches such     and hybrid approaches tailored to specific task characteris-
as fine-tuning, contrastive learning, and distillation tend to   tics.
perform well in domain-specific deployments with curated             While most existing benchmarks focus on evaluating
training data, but they struggle to generalize to unseen         the performance of hallucination detection and mitigation
domains and may even amplify domain-specific biases or           methods rather than measuring how frequently halluci-
misconceptions. This highlights the need for domain-aware,       nations occur in LLMs, recent community efforts provide
task-adaptive mitigation pipelines that combine retrieval,       useful empirical data on hallucination rates across systems.
reasoning control, and model-level adaptation tailored to        One such resource is the Hallucination Leaderboard [235],
the deployment setting.                                          which aggregates model performance on grounded summa-
                                                                 rization tasks and reports hallucination rates computed by
                                                                 the Hughes Hallucination Evaluation Model (HHEM) [235].
8   B ENCHMARK DATASETS                                          Some state-of-the-art models achieve hallucination rates
Although LLM hallucination detection and mitigation is a         below a few percentage points on this task. This indicates
recent research area, substantial work has been directed         that in narrow, constrained settings, such as summariza-
toward curating datasets for detecting and mitigating hal-       tion, hallucinations are relatively infrequent compared with
lucination in varied NLG tasks. Hallucination datasets can       unconstrained generation. However, substantial variation
be used for hallucination detection, mitigation, or both.        remains across model families and prompt behaviors, which
Hallucination detection datasets are typically paired in-        demonstrates that hallucination is neither uniform nor neg-
puts with outputs, with explicit annotation of instances         ligible even under strict grounding conditions. While such
of hallucination that allow researchers to assess a model’s      task-specific benchmarks do not yet provide a unified, cross-
tendency toward producing false or fabricated information.       task hallucination frequency metric, the emerging leader-



TABLE 3: Summary of the surveyed hallucination mitigation techniques. Columns indicate whether the approach uses
prompt engineering (P), retrieval (R), self-refine/reasoning (S), or model-centric (M).

                                       Mitigation Method
Ref     Year     Task / Domain                             Dataset(s)                    Metric(s)
                                       P   R    S    M

[143]   2023     News generation       ✓             ✓     Private                       MAUVE, Topic consistency, Core consis-
                                                                                         tency
[144]   2023         Dialogue          ✓   ✓               RefGPT-Fact, RefGPT-Code      Human evaluation, LLM-as-a-judge
[148]   2024   Legal instruction gen   ✓   ✓         ✓     Private                       Accuracy, Fluency
[149]   2023       QA citation         ✓                   Private                       Accuracy
[152]   2023     Summarization         ✓        ✓    ✓     CNN/DM, XSum, NEWTS           Rouge, G-eval, Human
[153]   2023            QA             ✓   ✓         ✓     FRESHQA                       Accuracy
[150]   2024   QA, Summarization       ✓   ✓               Private                       –

[158]   2023           QA                  ✓    ✓    ✓     DROP, GSM-IC, Entailment-     Accuracy
                                                           Bank
[160]   2023           QA              ✓   ✓    ✓          MS MARCO                      Accuracy, Human
[164]   2024           QA                  ✓         ✓     NQ, TriviaQA, SQuAD, BioASQ   Coverage rate
[166]   2024           QA                  ✓    ✓    ✓     TruthfulQA, StrategyQA, NQ,   GPT-judge, BLEU, Rouge
                                                           TriviaQA
[169]   2024           QA                  ✓         ✓     OBQA, CSQA, WQSP, CWQ         Accuracy, Hits@1
[171]   2024           QA                  ✓    ✓    ✓     WebQSP, CWQ                   F1, Hits@1
[174]   2023           QA              ✓   ✓               WebQuestionsSP, Mintaka       MRR, Top-K Accuracy
[177]   2023           QA                  ✓    ✓          HotpotQA, 2WikiMultihopQA     Recall, F1
[181]   2024           QA                  ✓    ✓    ✓     Mintaka, HotpotQA             EM, F1
[176]   2025           QA                  ✓    ✓          Follow-up QA                  Accuracy, EM
[179]   2025           QA                  ✓    ✓    ✓     CWQ, WebQSP, GrailQA          EM

[159]   2023     QA, Dialogue          ✓   ✓    ✓    ✓     NQ, SQA, QReCC                Human, Attrauto
[161]   2024   QA, Summarization       ✓   ✓         ✓     RAGTruth                      Precision, Recall, F1
[183]   2024        Dialogue           ✓   ✓    ✓    ✓     DoQA, QuAC                    F1, Accuracy
[199]   2024          QA                   ✓    ✓          HotpotQA                      F1, Human
[200]   2024          QA                   ✓    ✓    ✓     CommonsenseQA, ARC            EM
[201]   2023          QA               ✓   ✓    ✓    ✓     FEVER, HotpotQA               Accuracy, EM
[202]   2024          QA                   ✓    ✓    ✓     NQ, TriviaQA                  F1, EM
[196]   2025          QA                        ✓    ✓     TruthfulQA, HaluEval          Accuracy

[205]   2023   Machine translation                   ✓     FLORES-101                    COMET
[206]   2024   Machine translation                   ✓     HLMT                          SpBLEU, ChrF2
[204]   2024    Summarization                        ✓     CNN-DM, XSUM                  ROUGE-L, FactKB
[210]   2025    Summarization                        ✓     CNNDM, XSUM                   ROUGE-L
[221]   2024    Summarization          ✓             ✓     XSum, CNN/DM                  QuestEval, FactCC
[226]   2023    Summarization                        ✓     XLSum                         mFact, Rouge
[203]   2023          QA               ✓        ✓    ✓     TruthfulQA                    Accuracy
[212]   2023          QA               ✓   ✓    ✓    ✓     Private                       HALOCHECK
[213]   2024          QA               ✓   ✓         ✓     HaluEval, TruthfulQA          Accuracy
[207]   2025          QA                             ✓     TruthfulQA, TriviaQA          Accuracy
[217]   2025          QA                             ✓     TruthfulQA, TriviaQA          Accuracy
[222]   2023       Dialogue                ✓         ✓     WoW                           F1, Rouge, BLEU
[219]   2024     Multiple tasks        ✓   ✓         ✓     Multiple datasets             Accuracy


board results represent one of the first systematic efforts to       Statistical metrics compute hallucination scores by mea-
quantify hallucination prevalence and offer the community        suring mismatches between the generated content and ref-
a common reference point for comparing models on factual         erences [5]. Statistical metrics include token overlap met-
consistency.                                                     rics, such as BLEU and Rouge, semantic similarity metrics,
                                                                 such as BERTScore, and uncertainty-based metrics, such as
                                                                 perplexity. These approaches are widely adopted due to
9 H ALLUCINATION D ETECTION AND M ITIGATION                      simplicity, but often lack robustness in aligning with human
M ETRICS                                                         judgments of hallucination [21].
Hallucination evaluation metrics are essential to objectively        Data-driven metrics use curated datasets or other models’
measure the truthfulness of LLMs on different NLG tasks.         outputs for hallucination detection by measuring content
Hallucination evaluation metrics can be categorized into         mismatching. SelfCheckGPT [116] is a reference-free metric
statistical, data-driven, human-based, and mixed metrics         that evaluates consistency across multiple LLM outputs. By
[258]. Each provides unique insights and exhibits limitations    generating and comparing paraphrased outputs, it identi-
in terms of faithfulness, factuality, and generalizability.      fies unsupported information. Similarly, FactCC [245] is a



                           TABLE 4: Benchmark Datasets for Hallucination Detection and Mitigation.

 Ref     Name           Year           Lang.        Detect           Mitigate          Domain               Source                          Size                       GT Source

 [153]   FreshQA        2023                        ✓                ✓                 QA                   Human                           600                        Human
 [236]   RealtimeQA     2022                        ✓                ✓                 QA, MCQ              Human                           Dynamic                    Human
 [237]   WikiFact       2019                        ✓                                  Summ.                Wikipedia                       36.9M                      Wikipedia
 [238]   XSum           2020                        ✓                ✓                 Summ.                BBC                             226,711                    BBC article
 [239]   HotpotQA       2018                        ✓                ✓                 QA                   Wikipedia                       112,779                    Human
 [240]   HaluEval       2023                        ✓                ✓                 QA, Summ., Di-       Human, Model-gen                35,000                     Human
                                       English
                                                                                       alogue
 [241]   DefAn          2024                        ✓                ✓                 QA                   Human                           68K public, 7.5K hidden    Human
 [242]   ToTTo          2020                        ✓                ✓                 Data2Text            Wikipedia tables                136,161                    Human
 [243]   TriviaQA       2017                        ✓                ✓                 QA                   Wikipedia and web search        78.8K (Wiki); 95K (Web);   Human
                                                                                                                                            1,975 (Clean)
 [244]   DialFact       2022                        ✓                ✓                 Dialogue             WoW convos, Wikipedia           22,245                     Human,
                                                                                                                                                                       Wikipedia
 [245]   FactCC         2020                        ✓                                  Summ.                CNN/DailyMail                   >1M                        Human
 [246]   MedHallu       2025                        ✓                ✓                 QA                   PubMedQA                        10K                        PubMedQA

 [247]   WMT18          2018           German-      ✓                ✓                 MT                   News translations               3.4K annotations, 1.3M     Human
                                       English                                                                                              sentences
 [248]   Absinth        2024           German       ✓                                  Summ.                20Minuten news, model-          4,314                      Human
                                                                                                            gen

 [249]   Halwasa        2024                        ✓                ✓                 Text gen.            Model-gen                       10K                        Human
 [250]   IslamicEval    2025                        ✓                ✓                 QA                                                   1,506
                                       Arabic
 [251]   AraHalluEval   2025                        ✓                                  QA, Summ.                                            200QA, 100Sum.             Human
 [252]   Aftina         2025                                         ✓                 QA                                                   18k

 [253]   UHGEval        2024                        ✓                ✓                 Text gen.            Chinese news                    5,141                      GPT-4, Human
                                       Chinese
 [254]   HaluQA         2023                        ✓                ✓                 QA                   Human, Model-gen                450                        Human

 [255]   Med-Halt       2023                        ✓                ✓                 MCQ QA               Human, Model-gen                4,916                      Human
 [256]   HalOmi         2023           Multi        ✓                                  MT                   NLLB-200      translations,     ∼3.5K–4K                   Human
                                                                                                            Wikipedia
 [257]   Mu-Shroom      2025                        ✓                                  General              Wikipedia, Model-gen            ∼5.7K                      Human


             TABLE 5: Benchmark results for hallucination mitigation techniques using the most utilized datasets.

                               Ref          TriviaQA                NQ                 HotpotQA                 XSum            TruthfulQA          CNN/DM
                                           EM      F1        EM          F1     RL        EM    F1               RL             RL     Acc            RL
                               [152]                                                                             17.6                                 26.9
                               [166]       69.0   78.5       40.0        57.3                                                   31.2
                               [177]                                            49.3        60.7
                               [181]                                            34.0        47.2
                               [159]                                     57.0
                               [199]                                                                 90.3
                               [201]                                                        35.4
                               [204]                                                                             20.0                                  27.1
                               [210]                                            7.4                              20.0                                  27.8
                               [221]                                                                             38.2
                               [207]       80.8              47.4
                               [196]                                                                                                      45.1
                               [217]                                                                                                      48.4
                               [207]                         31.0                                                                         50.2
                               [202]       76.3   82.6       57.5        48.9                                                             50.2


supervised NLI classifier trained on synthetically perturbed                                       contradictions within the output; relevancy, appropriateness
data to detect factual inconsistencies between source and                                          of the response to the input query; and adequacy, complete-
generated text. G-eval [259] is an LLM-as-a-judge evaluation                                       ness of the conveyed information. Another human-based
framework that uses CoT prompting. It transforms user-                                             technique to detect hallucination is by using eye tracking,
defined evaluation criteria into structured reasoning steps,                                       where a reader’s gaze patterns, such as prolonged fixations,
which are then executed by LLMs, typically GPT-4, to score                                         regressions, and pupil dilation, are monitored to identify
outputs in a form-filling paradigm. Evaluation using LLMs                                          text segments that cause unexpected cognitive load and may
like GPT-4 achieves the best overall alignment with human                                          therefore contain hallucinated or unfaithful content. [261].
judgment [260]. Moreover, mFACT [226] enhances cross-                                              However, this approach is time-consuming and resource-
lingual hallucination detection by translating non-English                                         intensive [21].
outputs into English and applying multiple English-trained
faithfulness metrics.

   Human annotation remains a gold standard method for                                                To harness the strengths of automated and manual
assessing hallucination. Several studies employ human an-                                          assessments, mixed approaches, including factor analysis of
notators to detect LLM hallucination [21], [160], [199], [212],                                    mixed data (FAMD) [260], and advanced datasets including
[221], [251]. Human evaluation is typically conducted along                                        HalluLens [262], combine multiple signals, such as semantic
multiple dimensions such as faithfulness, the degree to                                            similarity, QA-based judgment, and consistency scores, with
which generated content aligns with source facts; factuality,                                      human annotations or domain expertise. These methods
the correctness of the information with respect to real-world                                      provide comprehensive, context-aware analysis of halluci-
knowledge or verified ground truth; consistency, absence of                                        nations across varied domains and use cases.



10     O PEN I SSUES AND F UTURE D IRECTIONS                      and development of detection methods for diverse linguistic
Despite a large number of previously proposed approaches,         settings.
a multitude of challenges remain unsolved in the LLMs’
hallucination detection and mitigation methods. This sec-         10.2   Hallucination Mitigation
tion categorizes these issues into detection, mitigation, and     Limitations of Attention Mechanisms. Attention mech-
resource issues.                                                  anisms, while being the core of transformer architectures,
                                                                  usually fail to properly distinguish between useful context
10.1   Hallucination Detection                                    and noisy information due to the softmax bottleneck. Cur-
                                                                  rent attention mechanisms may improperly weigh context
Generalization. Most of the current hallucination detection       and self-generated content, causing contextually irrelevant
methods are trained and evaluated on particular datasets          hallucinations [264]. Future work should investigate en-
and tasks, resulting in inadequate generalization across          hancing attention mechanisms to dynamically emphasize
diverse datasets and tasks. Additionally, the inconsistency       key contexts with adaptive uncertainty measures, boosting
in model training and prompting techniques hinders the de-        context faithfulness, and reducing hallucination [265].
velopment of universal hallucination detection frameworks
                                                                  Suboptimal Exploration in Reasoning Tasks. The current
[103]. As a result, detecting the hallucination of different
                                                                  exploration strategies, such as prompt-based Monte Carlo
LLMs will require adapting multiple methods based on
                                                                  Tree Search, lack adaptive adjustment, which leads to ei-
the characteristics of the target LLM and downstream task,
                                                                  ther insufficient or excessive exploration. This imbalance
which complicates real-time and resource-limited deploy-
                                                                  can result in premature convergence or overlooking correct
ment.
                                                                  reasoning pathways, thus failing to adequately mitigate hal-
Computational Overhead. Hallucination detection tech-             lucinations [266]. Future research should focus on adaptive
niques, such as self-consistency checks, uncertainty es-          exploration strategies, possibly integrating dynamic thresh-
timation, and retrieval-augmented verification, often re-         old adjustments or feedback-based exploration policies, to
quire multiple inference iterations or access to external         balance exploration and exploitation effectively.
databases, thereby escalating computational expenses. This
                                                                  Cross-Lingual and Multilingual Challenges. Current
poses challenges for real-time applications and deployment
                                                                  cross-lingual and multilingual models face some challenges
in resource-limited settings. Although AGSER [263] reduces
                                                                  in maintaining factual consistency across languages, partic-
computational costs compared to current methods, it still
                                                                  ularly in low-resource settings. Multilingual LLMs typically
requires several inference iterations. Future research should
                                                                  do not cross-learn across languages, especially for implicit
focus on developing efficient and lightweight detection
                                                                  reasoning tasks. For instance, models can correctly answer
mechanisms. Techniques such as knowledge distillation,
                                                                  questions in English but fail in Swahili even with equivalent
quantization, or sparse architectures could help reduce
                                                                  knowledge. Moreover, more training favors high-resource
computational overhead without compromising detection
                                                                  languages, but it leads to unreliable outputs in low-resource
accuracy.
                                                                  languages [267]. Future work should focus on developing
Subtle Hallucination Detection. Subtle factual errors in          adaptive multilingual models that can dynamically scale
LLM-generated responses are often difficult to detect and         representations based on linguistic context.
may require domain expertise or large external resources for
                                                                  Low-Resource Languages. Current hallucination mitigation
identification. Future research should explore methods such
                                                                  techniques perform poorly in low-resource languages due
as diffusion-based contrastive learning models to generate
                                                                  to insufficient data and limited linguistic coverage. Future
both factual and hallucinated versions of an answer. By
                                                                  research should focus on methods tailored to low-resource
learning the semantic distance between them, a model could
                                                                  languages, such as few-shot cross-lingual transfer learning
develop a more nuanced understanding of hallucinations.
                                                                  that leverages high-resource languages to improve per-
Multi-Turn Dialogue and Long-Form Generation. Detect-             formance. In addition, multilingual knowledge distillation
ing hallucinations in conversational agents is more challeng-     should be explored to facilitate knowledge transfer from
ing than in single-turn dialogues due to context propagation      high-resource to low-resource models.
across multiple turns. Hallucinations may emerge gradually,
                                                                  Fine-tuning limitations. Fine-tuning LLMs using tradi-
making post-hoc detection less effective. Future research
                                                                  tional input-output pairs is more likely to lead to overfit-
should focus on techniques such as dynamic context track-
                                                                  ting, catastrophic forgetting, and increased hallucinations,
ing, memory-augmented models, and reinforcement learn-
                                                                  especially when training data is noisy or biased. Fine-tuning
ing with hallucination-specific rewards to address this issue.
                                                                  without critiques or adaptive weighting can lead to over-
Low-Resource Languages. Most hallucination detection              refusal or continued hallucinations [216]. Future research
methods are developed and evaluated on high-resource lan-         should investigate critique-based tuning and uncertainty-
guages like English, leaving low-resource languages under-        weighted adaptive fine-tuning techniques for LLMs halluci-
represented. This limits the applicability of hallucination de-   nation mitigation.
tection methods in multilingual and global contexts. Future
work should focus on extending hallucination detection to
                                                                  10.3   Benchmarks and Evaluation Metrics
low-resource languages by leveraging cross-lingual transfer
learning, multilingual pretraining, and data augmentation         Benchmark Coverage and Diversity. Many existing bench-
techniques. Additionally, creating multilingual datasets and      marks are related to specific tasks, such as QA, summariza-
benchmarks would enable more comprehensive evaluation             tion, or translation, and are limited to particular sources,



including news and Wikipedia. This introduces task and do-          Our review revealed that despite significant progress
main bias, limiting generalization to open-ended or multi-      made in understanding, detecting, and mitigating halluci-
domain generation scenarios. Moreover, benchmarks for           nation, there remain some significant challenges. Current
dialogue and code generation hallucination are still scarce,    methods frequently exhibit limitations in generalizability,
which limits the applications in these domains.                 computational efficiency, handling of multilingual contexts,
Binary or Coarse-Grained Labels. Many hallucination             and interpretability. Directions for future research must fo-
detection benchmarks reduce the output to a binary la-          cus on the development of robust and more generalizable
bel—“hallucinated” vs “non-hallucinated.” This approach         hallucination detection methods that can be easily applied
leads hallucination detection methods to ignore partial hal-    across multiple domains and model architectures. Improv-
lucinations and varying error severity. Therefore, subtle       ing the interpretability of detection and mitigation tech-
factual drifts are not distinguished, which limits diagnostic   niques will be crucial for building trust in AI systems. Addi-
granularity and reduces the benchmark’s value for model         tionally, there is a need for standardized evaluation frame-
improvement.                                                    works and benchmarks that can comprehensively assess
Dependence on Human Annotation. Ground truths in                hallucination across different tasks and languages. Future
many benchmarks depend heavily on human annotators              work will also need to concentrate on enhancing attention
to label hallucinated spans or judge factual correctness.       mechanisms, refining exploration strategies in reasoning
This introduces several issues related to scalability, inter-   tasks, raising cross-lingual and low-resource applicability,
annotator agreement, and bias.                                  and enhancing fine-tuning techniques to balance general-
                                                                ization and specificity to better mitigate hallucination. Be-
Bias of LLM-as-Judge. Recent evidence shows that LLM-
                                                                sides, developing comprehensive benchmarks and datasets
as-a-judge can be influenced by visually appealing for-
                                                                to enable detailed evaluation and promoting scalable, inter-
matting, which leads to large preference shifts even when
                                                                pretable approaches will be essential in the advancement of
the underlying content quality is unchanged [268]. This is
                                                                this field.
particularly concerning for open-ended evaluation where
judges may be convinced by perceived credibility rather             As LLMs continue to evolve, addressing hallucination
than factual correctness [268]. In addition, LLM-as-a-judge     will remain a critical area of study. By combining advances
exhibits positional effects. The same judge may prefer dif-     in model architecture, training techniques, and external
ferent candidates when the order of candidates is swapped,      knowledge integration, researchers can work towards creat-
and this behavior is not explained by random variation          ing more reliable and factually grounded LLMs. Ultimately,
[269]. LLM-as-a-judge also suffers from cognitive-related       mitigating hallucination is critical to unleashing the full
biases. Therefore, it is recommended to avoid using the         potential of LLMs in applications and making sure that
same model to both generate and judge outputs [270]. Fu-        their output remains accurate, reliable, and human values-
ture research should investigate using jury-style aggregation   aligned.
across multiple diverse judges to reduce self-enhancement
and idiosyncratic preferences [270], [271]. It is also recom-
mended to test the judges using format perturbations, fake-     R EFERENCES
reference perturbations, and adversarial phrasing tests as
part of the evaluation protocol.                                [1]    R. OpenAI, “Gpt-4 technical report. arxiv 2303.08774,” View in
                                                                       Article, vol. 2, no. 5, 2023.
Lack of Explainability and Rationale. Most benchmarks           [2]    Anthropic,                “Claude            (version             3),”
consist of only a predicted label without an accompanying              https://www.anthropic.com/claude, 2024, accessed: 2024-12-14.
explanation or rationale. As a result, detection and mitiga-    [3]    Google, “Bard,” https://bard.google.com/, 2024, accessed: 2024-
                                                                       12-14.
tion methods lack transparency, which makes it hard to trace
                                                                [4]    Z. Xu, S. Jain, and M. Kankanhalli, “Hallucination is inevitable:
why a decision was made.                                               An innate limitation of large language models,” arXiv preprint
Cross-Lingual and Low-Resource Language Evaluation.                    arXiv:2401.11817, 2024.
Most existing benchmarks and evaluation metrics focus on        [5]    Z. Ji, N. Lee, R. Frieske, T. Yu, D. Su, Y. Xu, E. Ishii, Y. J. Bang,
                                                                       A. Madotto, and P. Fung, “Survey of hallucination in natural
high-resource languages, especially English, which leaves              language generation,” ACM Computing Surveys, vol. 55, no. 12,
many languages underrepresented. Therefore, models may                 pp. 1–38, 2023.
perform well under English benchmarks but fail catastroph-      [6]    T. B. Brown, “Language models are few-shot learners,” arXiv
                                                                       preprint arXiv:2005.14165, 2020.
ically in other languages.
                                                                [7]    E. M. Bender, T. Gebru, A. McMillan-Major, and S. Shmitchell,
                                                                       “On the dangers of stochastic parrots: Can language models be
11   C ONCLUSION                                                       too big?” in Proceedings of the 2021 ACM conference on fairness,
                                                                       accountability, and transparency, 2021, pp. 610–623.
Hallucination in LLMs remains a critical challenge that         [8]    S. Tonmoy, S. Zaman, V. Jain, A. Rani, V. Rawte, A. Chadha,
undermines the credibility and reliability of AI-generated             and A. Das, “A comprehensive survey of hallucination mit-
content across applications. This survey offers a compre-              igation techniques in large language models,” arXiv preprint
hensive review of the underlying causes of hallucination               arXiv:2401.01313, 2024.
                                                                [9]    L. Huang, W. Yu, W. Ma, W. Zhong, Z. Feng, H. Wang, Q. Chen,
and proposes a taxonomy of five dimensions for detection               W. Peng, X. Feng, B. Qin et al., “A survey on hallucination in
techniques and four dimensions for mitigation strategies.              large language models: Principles, taxonomy, challenges, and
We further review the benchmarks and performance metrics               open questions,” arXiv preprint arXiv:2311.05232, 2023.
used in hallucination detection and mitigation techniques,      [10]   P. Sahoo, P. Meharia, A. Ghosh, S. Saha, V. Jain, and A. Chadha,
                                                                       “A comprehensive survey of hallucination in large language,
and highlight current limitations and promising directions             image, video and audio foundation models,” arXiv preprint
for future research to foster more factual, trustworthy LLMs.          arXiv:2405.09589, 2024.



[11]   Y. Zhang, Y. Li, L. Cui, D. Cai, L. Liu, T. Fu, X. Huang, E. Zhao,      [32]   R. Tian, S. Narayan, T. Sellam, and A. P. Parikh, “Sticking to the
       Y. Zhang, Y. Chen et al., “Siren’s song in the ai ocean: a sur-                facts: Confident decoding for faithful data-to-text generation,”
       vey on hallucination in large language models,” arXiv preprint                 arXiv preprint arXiv:1910.08684, 2019.
       arXiv:2309.01219, 2023.                                                 [33]   S. Witteveen and M. Andrews, “Paraphrasing with large lan-
[12]   H. Ye, T. Liu, A. Zhang, W. Hua, and W. Jia, “Cognitive mirage: A              guage models,” in Proceedings of the 3rd Workshop on Neural
       review of hallucinations in large language models,” arXiv preprint             Generation and Translation, 2019, pp. 215–220.
       arXiv:2309.06794, 2023.                                                 [34]   F. Liu, Y. Liu, L. Shi, H. Huang, R. Wang, Z. Yang, L. Zhang,
[13]   A. Saxena and P. Bhattacharyya, “Hallucination detection in                    Z. Li, and Y. Ma, “Exploring and evaluating hallucinations in
       machine generated text: A survey,” 2024.                                       llm-powered code generation,” arXiv preprint arXiv:2404.00971,
[14]   M. Cossio, “A comprehensive taxonomy of hallucinations in large                2024.
       language models,” arXiv preprint arXiv:2508.01781, 2025.                [35]   Y. Kim, H. Jeong, S. Chen, S. S. Li, C. Park, M. Lu, K. Alhamoud,
[15]   B. Malin, T. Kalganova, and N. Boulgouris, “A review of faith-                 J. Mun, C. Grau, M. Jung et al., “Medical hallucinations in
       fulness metrics for hallucination assessment in large language                 foundation models and their impact on healthcare,” arXiv preprint
       models,” IEEE Journal of Selected Topics in Signal Processing, 2025.           arXiv:2503.05777, 2025.
[16]   S. Qi, L. Gui, Y. He, and Z. Yuan, “A survey of automatic               [36]   E. Asgari, N. Montaña-Brown, M. Dubois, S. Khalil, J. Balloch,
       hallucination evaluation on natural language generation,” arXiv                J. A. Yeung, and D. Pimenta, “A framework to assess clinical
       preprint arXiv:2404.12041, 2024.                                               safety and hallucination rates of llms for medical text summari-
[17]   S. S. Rahman, M. A. Islam, M. M. Alam, M. Zeba, M. A. Rahman,                  sation,” npj Digital Medicine, vol. 8, no. 1, p. 274, 2025.
       S. S. Chowa, M. A. K. Raiaan, and S. Azam, “Hallucination to            [37]   H. Kang and X.-Y. Liu, “Deficiency of large language models
       truth: A review of fact-checking and factuality evaluation in large            in finance: An empirical examination of hallucination,” arXiv
       language models,” arXiv preprint arXiv:2508.03860, 2025.                       preprint arXiv:2311.15548, 2023.
[18]   X. Jiang, Y. Tian, F. Hua, C. Xu, Y. Wang, and J. Guo, “A survey on     [38]   Y. Yang, M. C. S. Uy, and A. Huang, “Finbert: A pretrained
       large language model hallucination via a creativity perspective,”              language model for financial communications,” arXiv preprint
       arXiv preprint arXiv:2402.06647, 2024.                                         arXiv:2006.08097, 2020.
[19]   W. Fish, Perception, hallucination, and illusion. OUP USA, 2009.        [39]   S. Wu, O. Irsoy, S. Lu, V. Dabravolski, M. Dredze,
[20]   A. Shah, N. Banner, C. Heginbotham, and B. Fulford, “7. ameri-                 S. Gehrmann, P. Kambadur, D. Rosenberg, and G. Mann,
       can psychiatric association (2013) diagnostic and statistical man-             “Bloomberggpt: A large language model for finance,” arXiv
       ual of mental disorders, 5th edn. american psychiatric publish-                preprint arXiv:2303.17564, 2023.
       ing, arlington, va. 8. bechara, a., dolan, s. and hindes, a.(2002)      [40]   S. Roychowdhury, “Journey of hallucination-minimized gener-
       decision-making and addiction (part ii): myopia for the future or              ative ai solutions for financial decision makers,” in Proceedings
       hypersensitivity to reward? neuropsychologia, 40, 1690–1705. 9.                of the 17th ACM International Conference on Web Search and Data
       office of public sector information (2005) the mental capacity act             Mining, 2024, pp. 1180–1181.
       2005. http://www.” Substance Use and Older People, vol. 21, no. 5,      [41]   M. Dahl, V. Magesh, M. Suzgun, and D. E. Ho, “Large legal
       p. 9, 2014.                                                                    fictions: Profiling legal hallucinations in large language models,”
[21]   J. Maynez, S. Narayan, B. Bohnet, and R. McDonald, “On faithful-               Journal of Legal Analysis, vol. 16, no. 1, pp. 64–93, 2024.
       ness and factuality in abstractive summarization,” in Proceedings       [42]   J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess,
       of the 58th Annual Meeting of the Association for Computational                R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei,
       Linguistics, 2020, pp. 1906–1919.                                              “Scaling laws for neural language models,” arXiv preprint
[22]   P. Koehn and R. Knowles, “Six challenges for neural machine                    arXiv:2001.08361, 2020.
       translation,” in Proceedings of the First Workshop on Neural Machine    [43]   S. Lin, J. Hilton, and O. Evans, “Truthfulqa: Measuring how mod-
       Translation, 2017, pp. 28–39.                                                  els mimic human falsehoods,” in Proceedings of the 60th Annual
[23]   C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena,               Meeting of the Association for Computational Linguistics (Volume 1:
       Y. Zhou, W. Li, and P. J. Liu, “Exploring the limits of transfer               Long Papers), 2022, pp. 3214–3252.
       learning with a unified text-to-text transformer,” Journal of ma-       [44]   E. Ferrara, “Fairness and bias in artificial intelligence: A brief
       chine learning research, vol. 21, no. 140, pp. 1–67, 2020.                     survey of sources, impacts, and mitigation strategies,” Sci, vol. 6,
[24]   V. Raunak, A. Menezes, and M. Junczys-Dowmunt, “The cu-                        no. 1, p. 3, 2023.
       rious case of hallucinations in neural machine translation,” in         [45]   T. Bolukbasi, K.-W. Chang, J. Y. Zou, V. Saligrama, and A. T. Kalai,
       Proceedings of the 2021 Conference of the North American Chapter               “Man is to computer programmer as woman is to homemaker?
       of the Association for Computational Linguistics: Human Language               debiasing word embeddings,” Advances in neural information pro-
       Technologies, 2021, pp. 1172–1183.                                             cessing systems, vol. 29, 2016.
[25]   U. Hahn, C.-Y. Lin, I. Mani, and D. Radev, “Automatic summa-            [46]   K. Lee, D. Ippolito, A. Nystrom, C. Zhang, D. Eck, C. Callison-
       rization,” in Proceedings of the ANLP/NAACL Workshop, Seattle,                 Burch, and N. Carlini, “Deduplicating training data makes lan-
       WA, 2000.                                                                      guage models better,” in Proceedings of the 60th Annual Meeting
[26]   B. Snyder, M. Moisescu, and M. B. Zafar, “On early detection                   of the Association for Computational Linguistics (Volume 1: Long
       of hallucinations in factual question answering,” in Proceedings               Papers), 2022, pp. 8424–8445.
       of the 30th ACM SIGKDD Conference on Knowledge Discovery and            [47]   Y. Wang, S. Feng, H. Wang, W. Shi, V. Balachandran, T. He, and
       Data Mining, 2024, pp. 2721–2732.                                              Y. Tsvetkov, “Resolving knowledge conflicts in large language
[27]   S. Shaier, A. Kobren, and P. Ogren, “Adaptive question an-                     models,” arXiv preprint arXiv:2310.00935, 2023.
       swering: Enhancing language model proficiency for address-              [48]   E. Topol, Deep medicine: how artificial intelligence can make healthcare
       ing knowledge conflicts with source citations,” arXiv preprint                 human again. Hachette UK, 2019.
       arXiv:2410.04241, 2024.                                                 [49]   S. M. Mousavi, S. Alghisi, and G. Riccardi, “Is your llm outdated?
[28]   Z. Zhang, R. Takanobu, Q. Zhu, M. Huang, and X. Zhu, “Recent                   benchmarking llms & alignment algorithms for time-sensitive
       advances and challenges in task-oriented dialog systems,” Science              knowledge,” arXiv preprint arXiv:2404.08700, 2024.
       China Technological Sciences, vol. 63, no. 10, pp. 2011–2027, 2020.     [50]   N. Kandpal, H. Deng, A. Roberts, E. Wallace, and C. Raffel,
[29]   M. Huang, X. Zhu, and J. Gao, “Challenges in building intelligent              “Large language models struggle to learn long-tail knowledge,”
       open-domain dialog systems,” ACM Transactions on Information                   in Proceedings of the 40th International Conference on Machine Learn-
       Systems (TOIS), vol. 38, no. 3, pp. 1–32, 2020.                                ing, 2023, pp. 15 696–15 707.
[30]   Z. Ji, Z. Liu, N. Lee, T. Yu, B. Wilie, M. Zeng, and P. Fung, “Rho:     [51]   A. Vaswani, “Attention is all you need,” Advances in Neural
       Reducing hallucination in open-domain dialogues with knowl-                    Information Processing Systems, 2017.
       edge grounding,” in Findings of the Association for Computational       [52]   X. Liu, “A survey of hallucination problems based on large
       Linguistics: ACL 2023, 2023, pp. 4504–4522.                                    language models,” Applied and Computational Engineering, vol. 97,
[31]   Y. Pan, D. Cadamuro, and G. Groh, “Exploring hallucinations in                 pp. 24–30, 2024.
       task-oriented dialogue systems with narrow domains,” in Pro-            [53]   B. Liu, J. Ash, S. Goel, A. Krishnamurthy, and C. Zhang, “Ex-
       ceedings of the 38th Pacific Asia Conference on Language, Information          posing attention glitches with flip-flop language modeling,” Ad-
       and Computation, 2024, pp. 609–618.                                            vances in Neural Information Processing Systems, vol. 36, 2024.



[54]   S. Welleck, I. Kulikov, S. Roller, E. Dinan, K. Cho, and J. We-                quantification, and prescriptive remediations,” arXiv preprint
       ston, “Neural text generation with unlikelihood training,” arXiv               arXiv:2310.04988, 2023.
       preprint arXiv:1908.04319, 2019.                                        [75]   N. Dziri, A. Madotto, O. R. Zaiane, and A. J. Bose, “Neural
[55]   S. Banerjee, A. Agarwal, and S. Singla, “Llms will always                      path hunter: Reducing hallucination in dialogue systems via path
       hallucinate, and we need to live with this,” arXiv preprint                    grounding,” in Proceedings of the 2021 Conference on Empirical
       arXiv:2409.05746, 2024.                                                        Methods in Natural Language Processing, 2021, pp. 2197–2214.
[56]   G. Bihani and J. T. Rayz, “Learning shortcuts: On the mis-              [76]   C. Meister, R. Cotterell, and T. Vieira, “If beam search is the
       leading promise of nlu in language models,” arXiv preprint                     answer, what was the question?” in Proceedings of the 2020 Confer-
       arXiv:2401.09615, 2024.                                                        ence on Empirical Methods in Natural Language Processing (EMNLP),
[57]   T. Niven and H.-Y. Kao, “Probing neural network comprehension                  2020, pp. 2173–2185.
       of natural language arguments,” in Proceedings of the 57th Annual       [77]   Z. Yang, Z. Dai, R. Salakhutdinov, and W. W. Cohen, “Breaking
       Meeting of the Association for Computational Linguistics, 2019, pp.            the softmax bottleneck: A high-rank rnn language model,” arXiv
       4658–4664.                                                                     preprint arXiv:1711.03953, 2017.
[58]   M. Du, V. Manjunatha, R. Jain, R. Deshpande, F. Dernoncourt,            [78]   S. Zheng, J. Huang, and K. C.-C. Chang, “Why does chat-
       J. Gu, T. Sun, and X. Hu, “Towards interpreting and mitigating                 gpt fall short in providing truthful answers?” arXiv preprint
       shortcut learning behavior of nlu models,” in Proceedings of the               arXiv:2304.10513, 2023.
       2021 Conference of the North American Chapter of the Association for    [79]   S. Rakin, M. A. Shibly, Z. M. Hossain, Z. Khan, and M. M. Ak-
       Computational Linguistics: Human Language Technologies, 2021, pp.              bar, “Leveraging the domain adaptation of retrieval augmented
       915–929.                                                                       generation models for question answering and reducing halluci-
[59]   D. Nguyen, L. Rosseel, and J. Grieve, “On learning and repre-                  nation,” arXiv preprint arXiv:2410.17783, 2024.
       senting social meaning in nlp: a sociolinguistic perspective,” in       [80]   G. Sriramanan, S. Bharti, V. S. Sadasivan, S. Saha, P. Kattakinda,
       Proceedings of the 2021 Conference of the North American Chapter               and S. Feizi, “Llm-check: Investigating detection of hallucinations
       of the Association for Computational Linguistics: Human language               in large language models,” Advances in Neural Information Process-
       technologies, 2021, pp. 603–612.                                               ing Systems, vol. 37, pp. 34 188–34 216, 2024.
[60]   D. Kang and T. B. Hashimoto, “Improved natural language                 [81]   Z. Zhu, Y. Yang, and Z. Sun, “Halueval-wild: Evaluating hal-
       generation via loss truncation,” in Proceedings of the 58th Annual             lucinations of language models in the wild,” arXiv preprint
       Meeting of the Association for Computational Linguistics, 2020, pp.            arXiv:2403.04307, 2024.
       718–731.                                                                [82]   C. Niu, Y. Wu, J. Zhu, S. Xu, K. Shum, R. Zhong, J. Song, and
[61]   C. Wang and R. Sennrich, “On exposure bias, hallucination and                  T. Zhang, “Ragtruth: A hallucination corpus for developing trust-
       domain shift in neural machine translation,” in Proceedings of the             worthy retrieval-augmented language models,” in Proceedings
       58th Annual Meeting of the Association for Computational Linguistics,          of the 62nd Annual Meeting of the Association for Computational
       2020, pp. 3544–3552.                                                           Linguistics (Volume 1: Long Papers), 2024, pp. 10 862–10 878.
[62]   M. Zhang, O. Press, W. Merrill, A. Liu, and N. A. Smith, “How           [83]   P. Lewis, E. Perez, A. Piktus, F. Petroni, V. Karpukhin, N. Goyal,
       language model hallucinations can snowball,” arXiv preprint                    H. Küttler, M. Lewis, W.-t. Yih, T. Rocktäschel et al., “Retrieval-
       arXiv:2305.13534, 2023.                                                        augmented generation for knowledge-intensive nlp tasks,” in
[63]   S. Hamdan and D. Yuret, “How much do llms learn from nega-                     Proceedings of the 34th International Conference on Neural Information
       tive examples?” arXiv preprint arXiv:2503.14391, 2025.                         Processing Systems, 2020, pp. 9459–9474.
[64]   D. Kiela, M. Bartolo, Y. Nie, D. Kaushik, A. Geiger, Z. Wu,             [84]   R. H. Ajmal, M. U. Sarwar, M. K. Hanif, and M. I. Khan, “Eval-
       B. Vidgen, G. Prasad, A. Singh, P. Ringshia et al., “Dynabench:                uating the effectiveness of advanced language models in de-
       Rethinking benchmarking in nlp,” in Proceedings of the 2021                    tecting and mitigating hallucinations using structured question-
       Conference of the North American Chapter of the Association for                answering, novel metrics, and post-hoc retrieval,” IEEE Access,
       Computational Linguistics: Human Language Technologies, 2021, pp.              2025.
       4110–4124.                                                              [85]   B. Paudel, A. Lyzhov, P. Joshi, and P. Anand, “Hallucinot: Hal-
[65]   Y. Nie, A. Williams, E. Dinan, M. Bansal, J. Weston, and D. Kiela,             lucination detection through context and common knowledge
       “Adversarial nli: A new benchmark for natural language un-                     verification,” arXiv preprint arXiv:2504.07069, 2025.
       derstanding,” in Proceedings of the 58th Annual Meeting of the          [86]   X. Wang, Y. Yan, L. Huang, X. Zheng, and X.-J. Huang, “Hal-
       Association for Computational Linguistics, 2020, pp. 4885–4901.                lucination detection for generative large language models by
[66]   P. F. Christiano, J. Leike, T. Brown, M. Martic, S. Legg, and                  bayesian sequential estimation,” in Proceedings of the 2023 Con-
       D. Amodei, “Deep reinforcement learning from human prefer-                     ference on Empirical Methods in Natural Language Processing, 2023,
       ences,” Advances in neural information processing systems, vol. 30,            pp. 15 361–15 371.
       2017.                                                                   [87]   A. Mishra, A. Asai, V. Balachandran, Y. Wang, G. Neubig,
[67]   J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov,                Y. Tsvetkov, and H. Hajishirzi, “Fine-grained hallucination
       “Proximal policy optimization algorithms,” arXiv preprint                      detection and editing for language models,” arXiv preprint
       arXiv:1707.06347, 2017.                                                        arXiv:2401.06855, 2024.
[68]   Y. Pan, L. Kong, J. Wu, Y. Yang, H. Zuo, Z. Xiu, and X. Wang, “To-      [88]   J. Zhang, C. Xu, Y. Gai, F. Lecue, D. Song, and B. Li, “Knowhalu:
       wards reliable large language models: A survey on hallucination                Hallucination detection via multi-form knowledge based factual
       detection,” in International Conference on Intelligent Computing.              checking,” arXiv preprint arXiv:2404.02935, 2024.
       Springer, 2025, pp. 438–451.                                            [89]   F. Xu, H. Zhang, Z. Zhang, J. Wang, and X. Wan, “Jointcq:
[69]   Z. Gekhman, G. Yona, R. Aharoni, M. Eyal, A. Feder, R. Reichart,               Improving factual hallucination detection with joint claim and
       and J. Herzig, “Does fine-tuning llms on new knowledge encour-                 query generation,” arXiv preprint arXiv:2510.19310, 2025.
       age hallucinations?” arXiv preprint arXiv:2405.05904, 2024.             [90]   M. Xiong, Z. Hu, X. Lu, Y. Li, J. Fu, J. He, and B. Hooi, “Can llms
[70]   M. Sharma, M. Tong, T. Korbak, D. Duvenaud, A. Askell, S. R.                   express their uncertainty? an empirical evaluation of confidence
       Bowman, N. Cheng, E. Durmus, Z. Hatfield-Dodds, S. R. John-                    elicitation in llms,” arXiv preprint arXiv:2306.13063, 2023.
       ston et al., “Towards understanding sycophancy in language              [91]   Y. Huang, J. Song, Z. Wang, S. Zhao, H. Chen, F. Juefei-Xu, and
       models,” arXiv preprint arXiv:2310.13548, 2023.                                L. Ma, “Look before you leap: An exploratory study of uncer-
[71]   C.-Y. Lin, “Rouge: A package for automatic evaluation of sum-                  tainty measurement for large language models,” arXiv preprint
       maries,” in Text summarization branches out, 2004, pp. 74–81.                  arXiv:2307.10236, 2023.
[72]   T. Zhang, V. Kishore, F. Wu, K. Q. Weinberger, and Y. Artzi,            [92]   N. M. Guerreiro, E. Voita, and A. F. Martins, “Looking for a
       “Bertscore: Evaluating text generation with bert,” arXiv preprint              needle in a haystack: A comprehensive study of hallucinations in
       arXiv:1904.09675, 2019.                                                        neural machine translation,” in Proceedings of the 17th Conference of
[73]   K. Papineni, S. Roukos, T. Ward, and W.-J. Zhu, “Bleu: a method                the European Chapter of the Association for Computational Linguistics,
       for automatic evaluation of machine translation,” in Proceedings               2023, pp. 1059–1075.
       of the 40th annual meeting of the Association for Computational         [93]   Y. Yang, H. Li, Y. Wang, and Y. Wang, “Improving the reliability
       Linguistics, 2002, pp. 311–318.                                                of large language models by leveraging uncertainty-aware in-
[74]   V. Rawte, S. Chakraborty, A. Pathak, A. Sarkar, S. Tonmoy,                     context learning,” arXiv preprint arXiv:2310.04782, 2023.
       A. Chadha, A. P. Sheth, and A. Das, “The troubling emergence of         [94]   T. Zhang, L. Qiu, Q. Guo, C. Deng, Y. Zhang, Z. Zhang, C. Zhou,
       hallucination in large language models–an extensive definition,                X. Wang, and L. Fu, “Enhancing uncertainty-based hallucination



      detection with stronger focus,” in Proceedings of the 2023 Confer-             states of large language models,” in Findings of the Association for
      ence on Empirical Methods in Natural Language Processing, 2023, pp.            Computational Linguistics ACL 2024, 2024, pp. 14 379–14 391.
      915–932.                                                                 [115] X. Cheng, J. Li, W. X. Zhao, H. Zhang, F. Zhang, D. Zhang,
[95] S. Dasgupta, S. Nath, A. Basu, P. Shamsolmoali, and S. Das,                     K. Gai, and J.-R. Wen, “Small agent can also rock! empowering
      “Hallushift: Measuring distribution shifts towards hallucination               small language models as hallucination detector,” in Proceedings
      detection in llms,” arXiv preprint arXiv:2504.09482, 2025.                     of the 2024 Conference on Empirical Methods in Natural Language
[96] A. Shelmanov, E. Fadeeva, A. Tsvigun, I. Tsvigun, Z. Xie, I. Kise-              Processing, 2024, pp. 14 600–14 615.
      lev, N. Daheim, C. Zhang, A. Vazhentsev, M. Sachan et al., “A            [116] P. Manakul, A. Liusie, and M. Gales, “Selfcheckgpt: Zero-resource
      head to predict and a head to question: Pre-trained uncertainty                black-box hallucination detection for generative large language
      quantification heads for hallucination detection in llm outputs,”              models,” in Proceedings of the 2023 Conference on Empirical Methods
      arXiv preprint arXiv:2505.08200, 2025.                                         in Natural Language Processing, 2023, pp. 9004–9017.
[97] M. Niu, H. Haddadi, and G. Pang, “Robust hallucination de-                [117] M. Li, W. Wang, F. Feng, F. Zhu, Q. Wang, and T.-S. Chua,
      tection in llms via adaptive token selection,” arXiv preprint                  “Think twice before trusting: Self-detection for large language
      arXiv:2504.07863, 2025.                                                        models through comprehensive answer reflection,” in Findings of
[98] C. Tong, Q. Zhang, J. Gao, L. Jiang, Y. Liu, and N. Sun,                        the Association for Computational Linguistics: EMNLP 2024, 2024,
      “Halunet: Multi-granular uncertainty modeling for efficient hal-               pp. 11 858–11 875.
      lucination detection in llm question answering,” arXiv preprint          [118] Z. Liu, J. Guo, H. Zhang, H. Chen, J. Bu, and H. Wang, “Long-
      arXiv:2512.24562, 2025.                                                        form hallucination detection with self-elicitation,” in Findings of
[99] S. Farquhar, J. Kossen, L. Kuhn, and Y. Gal, “Detecting hallucina-              the Association for Computational Linguistics: ACL 2025, 2025, pp.
      tions in large language models using semantic entropy,” Nature,                4082–4100.
      vol. 630, no. 8017, pp. 625–630, 2024.                                   [119] J. Zhang, Z. Li, K. Das, B. Malin, and S. Kumar, “Sac3: Reli-
[100] B. Hou, Y. Zhang, J. Andreas, and S. Chang, “A probabilistic                   able hallucination detection in black-box language models via
      framework for llm hallucination detection via belief tree prop-                semantic-aware cross-check consistency,” in Findings of the Associ-
      agation,” arXiv preprint arXiv:2406.06950, 2024.                               ation for Computational Linguistics: EMNLP 2023, 2023, pp. 15 445–
[101] K. Chen, Q. Chen, J. Zhou, X. Tao, B. Ding, J. Xie, M. Xie, P. Li, and         15 458.
      Z. Feng, “Enhancing uncertainty modeling with semantic graph             [120] B. Yang, M. A. Al Mamun, J. M. Zhang, and G. Uddin, “Hallu-
      for hallucination detection,” in Proceedings of the AAAI Conference            cination detection in large language models with metamorphic
      on Artificial Intelligence, vol. 39, no. 22, 2025, pp. 23 586–23 594.          relations,” Proceedings of the ACM on Software Engineering, vol. 2,
[102] Y.-S. Chuang, L. Qiu, C.-Y. Hsieh, R. Krishna, Y. Kim, and J. Glass,           no. FSE, pp. 425–445, 2025.
      “Lookback lens: Detecting and mitigating contextual hallucina-           [121] Y. Xue, K. Greenewald, Y. Mroueh, and B. Mirzasoleiman, “Verify
      tions in large language models using only attention maps,” in                  when uncertain: Beyond self-consistency in black box hallucina-
      Proceedings of the 2024 Conference on Empirical Methods in Natural             tion detection,” arXiv preprint arXiv:2502.15845, 2025.
      Language Processing, 2024, pp. 1419–1436.                                [122] M.-H. Yeh, M. Kamachee, S. Park, and Y. Li, “Can your
[103] J. Binkowski, D. Janiak, A. Sawczyn, B. Gabrys, and T. Kajdanow-               uncertainty scores detect hallucinated entity?” arXiv preprint
      icz, “Hallucination detection in llms using spectral features of               arXiv:2502.11948, 2025.
      attention maps,” arXiv preprint arXiv:2502.17598, 2025.                  [123] A. Simhi, I. Itzhak, F. Barez, G. Stanovsky, and Y. Belinkov, “Trust
[104] S. N. Samaga, G. G. Arroyo, and T. K. Dey, “Halluzig: Hal-                     me, i’m wrong: High-certainty hallucinations in llms,” arXiv
      lucination detection using zigzag persistence,” arXiv preprint                 preprint arXiv:2502.12964, 2025.
      arXiv:2601.01552, 2026.                                                  [124] W. Zhang and J. Zhang, “Hallucination mitigation for retrieval-
[105] A. Bazarova, A. Yugay, A. Shulga, A. Ermilova, A. Volodichev,                  augmented large language models: a review,” Mathematics,
      K. Polev, J. Belikova, R. Parchiev, D. Simakov, M. Savchenko et al.,           vol. 13, no. 5, p. 856, 2025.
      “Hallucination detection in llms with topological divergence on          [125] J. Genesis and F. Keane, “Integrating knowledge retrieval with
      attention graphs,” arXiv preprint arXiv:2504.10063, 2025.                      generation: A comprehensive survey of rag models in nlp,” 2025.
[106] D. Dale, E. Voita, L. Barrault, and M. R. Costa-jussà, “Detecting       [126] Y. Tang and Y. Yang, “Do we need domain-specific em-
      and mitigating hallucinations in machine translation: Model in-                bedding models? an empirical investigation,” arXiv preprint
      ternal workings alone do well, sentence similarity even better,”               arXiv:2409.18511, 2024.
      in Proceedings of the 61st Annual Meeting of the Association for         [127] R. Oblovatny, A. Bazarova, and A. Zaytsev, “Attention head em-
      Computational Linguistics (Volume 1: Long Papers), 2023, pp. 36–50.            beddings with trainable deep kernels for hallucination detection
[107] N. Nonkes, S. Agaronian, E. Kanoulas, and R. Petcu, “Leverag-                  in llms,” arXiv preprint arXiv:2506.09886, 2025.
      ing graph structures to detect hallucinations in large language          [128] H. Zhao, H. Chen, F. Yang, N. Liu, H. Deng, H. Cai, S. Wang,
      models,” in Proceedings of TextGraphs-17: Graph-based Methods for              D. Yin, and M. Du, “Explainability for large language models: A
      Natural Language Processing, 2024, pp. 93–104.                                 survey,” ACM Transactions on Intelligent Systems and Technology,
[108] X. Hu, Y. Zhang, R. Peng, H. Zhang, C. Wu, G. Chen, and J. Zhao,               vol. 15, no. 2, pp. 1–38, 2024.
      “Embedding and gradient say wrong: A white-box method for                [129] M. Salvi, S. Seoni, A. Campagner, A. Gertych, U. R. Acharya,
      hallucination detection,” in Proceedings of the 2024 Conference on             F. Molinari, and F. Cabitza, “Explainability and uncertainty: Two
      Empirical Methods in Natural Language Processing, 2024, pp. 1950–              sides of the same coin for enhancing the interpretability of deep
      1959.                                                                          learning models in healthcare,” International Journal of Medical
[109] S. Choi, T. Fang, Z. Wang, and Y. Song, “Kcts: Knowledge-                      Informatics, vol. 197, p. 105846, 2025.
      constrained tree search decoding with token-level hallucination          [130] Y. Huang, J. Zhang, Z. Wang, B. Bie, Y. Qiu, Y. R. Fung, and X. He,
      detection,” in Proceedings of the 2023 Conference on Empirical Meth-           “Reppl: Recalibrating perplexity by uncertainty in semantic prop-
      ods in Natural Language Processing, 2023, pp. 14 035–14 053.                   agation and language generation for explainable qa hallucination
[110] F. Zhang, P. Yu, B. Yi, B. Zhang, T. Li, and Z. Liu, “Prompt-guided            detection,” arXiv preprint arXiv:2505.15386, 2025.
      internal states for hallucination detection of large language mod-       [131] S. Lee, H. Lee, S. Heo, and W. Choi, “Hudex: Integrating hallu-
      els,” arXiv preprint arXiv:2411.04847, 2024.                                   cination detection and explainability for enhancing the reliability
[111] L. Kong, Y. Zhang, X. Zhong, H. Fu, Y. Wang, and H. Liu,                       of llm responses,” arXiv preprint arXiv:2502.08109, 2025.
      “Halugnn: Hallucination detection in large language models               [132] Y. Xie, W. Zhou, P. Prakash, D. Jin, Y. Mao, Q. Fettes, A. Tale-
      using graph neural network,” Expert Systems with Applications,                 bzadeh, S. Wang, H. Fang, C. Rose et al., “Improving model
      p. 130857, 2025.                                                               factuality with fine-grained critique-based evaluator,” in Proceed-
[112] S. Park, X. Du, M.-H. Yeh, H. Wang, and Y. Li, “Steer llm latents              ings of the 63rd Annual Meeting of the Association for Computational
      for hallucination detection,” arXiv preprint arXiv:2503.01917, 2025.           Linguistics (Volume 1: Long Papers), 2025, pp. 8140–8155.
[113] M. Yamada and Y. Arase, “Light-weight hallucination detection            [133] S. Heo, S. Son, and H. Park, “Halucheck: Explainable and veri-
      using contrastive learning for conditional text generation,” in                fiable automation for detecting hallucinations in llm responses,”
      Proceedings of the 63rd Annual Meeting of the Association for Com-             Expert Systems with Applications, vol. 272, p. 126712, 2025.
      putational Linguistics (Volume 4: Student Research Workshop), 2025,      [134] W.-F. Chen, Z. Zhao, A. Karimi, and L. Flek, “Explainable halluci-
      pp. 687–694.                                                                   nation through natural language inference mapping,” in Findings
[114] W. Su, C. Wang, Q. Ai, Y. Hu, Z. Wu, Y. Zhou, and Y. Liu, “Unsu-               of the Association for Computational Linguistics: ACL 2025, 2025, pp.
      pervised real-time hallucination detection based on the internal               1888–1896.



[135] M. Hu, R. Xu, D. Lei, Y. Li, M. Wang, E. Ching, E. Kamal,                      augmented language model pre-training,” in International confer-
      and A. Deng, “Slm meets llm: Balancing latency, interpretabil-                 ence on machine learning. PMLR, 2020, pp. 3929–3938.
      ity and consistency in hallucination detection,” arXiv preprint          [155] K. Lee, M.-W. Chang, and K. Toutanova, “Latent retrieval for
      arXiv:2408.12748, 2024.                                                        weakly supervised open domain question answering,” in Proceed-
[136] D. Orshansky, O. Oomen, N. Agarwal, and R. Lagasse, “Hal-                      ings of the 57th Annual Meeting of the Association for Computational
      lutree: Explainable multi-hop hallucination detection for abstrac-             Linguistics, 2019, pp. 6086–6096.
      tive summarization,” in Proceedings of The 5th New Frontiers in          [156] J. Ni, J. Bingler, C. Colesanti-Senni, M. Kraus, G. Gostlow, T. Schi-
      Summarization Workshop, 2025, pp. 123–134.                                     manski, D. Stammbach, S. A. Vaghefi, Q. Wang, N. Webersinke
[137] B. A. Galitsky and A. Rybalov, “An information-theoretic model                 et al., “Chatreport: Democratizing sustainability disclosure anal-
      of abduction for detecting hallucinations in explanations,” 2025.              ysis through llm-based tools,” in Proceedings of the 2023 Confer-
[138] J. Vladika, I. Soydemir, and F. Matthes, “Correcting hallucinations            ence on Empirical Methods in Natural Language Processing: System
      in news summaries: Exploration of self-correcting llm methods                  Demonstrations, 2023, pp. 21–51.
      with external knowledge,” arXiv preprint arXiv:2506.19607, 2025.         [157] B. Peng, M. Galley, P. He, H. Cheng, Y. Xie, Y. Hu, Q. Huang,
[139] S. Zhang, T. Yu, and Y. Feng, “Truthx: Alleviating hallucinations              L. Liden, Z. Yu, W. Chen et al., “Check your facts and try again:
      by editing large language models in truthful space,” in Proceed-               Improving large language models with external knowledge and
      ings of the 62nd Annual Meeting of the Association for Computational           automated feedback,” arXiv preprint arXiv:2302.12813, 2023.
      Linguistics (Volume 1: Long Papers), 2024, pp. 8908–8949.                [158] D. Nathani, D. Wang, L. Pan, and W. Wang, “Maf: Multi-aspect
[140] R. Kamoi, Y. Zhang, N. Zhang, J. Han, and R. Zhang, “When can                  feedback for improving reasoning in large language models,” in
      llms actually correct their own mistakes? a critical survey of self-           Proceedings of the 2023 Conference on Empirical Methods in Natural
      correction of llms,” Transactions of the Association for Computational         Language Processing, 2023, pp. 6591–6616.
      Linguistics, vol. 12, pp. 1417–1440, 2024.                               [159] L. Gao, Z. Dai, P. Pasupat, A. Chen, A. T. Chaganty, Y. Fan,
[141] P. Sahoo, A. K. Singh, S. Saha, V. Jain, S. Mondal, and                        V. Zhao, N. Lao, H. Lee, D.-C. Juan et al., “Rarr: Researching
      A. Chadha, “A systematic survey of prompt engineering in large                 and revising what language models say, using language models,”
      language models: Techniques and applications,” arXiv preprint                  in Proceedings of the 61st Annual Meeting of the Association for
      arXiv:2402.07927, 2024.                                                        Computational Linguistics (Volume 1: Long Papers), 2023, pp. 16 477–
[142] A. Radford and J. Wu, “Rewon child, david luan, dario amodei,                  16 508.
      and ilya sutskever. 2019,” Language models are unsupervised multi-       [160] S. Huo, N. Arabzadeh, and C. Clarke, “Retrieving supporting
      task learners. OpenAI blog, vol. 1, no. 8, p. 9, 2019.                         evidence for generative question answering,” in Proceedings of
[143] K. Jiang, Q. Zhang, D. Guo, D. Huang, S. Zhang, Z. Wei, F. Ning,               the Annual International ACM SIGIR Conference on Research and
      and R. Li, “Ai-generated news articles based on large language                 Development in Information Retrieval in the Asia Pacific Region, 2023,
      models,” in Proceedings of the 2023 International Conference on                pp. 11–20.
      Artificial Intelligence, Systems and Network Security, 2023, pp. 82–     [161] J. Song, X. Wang, J. Zhu, Y. Wu, X. Cheng, R. Zhong, and
      87.                                                                            C. Niu, “Rag-hat: A hallucination-aware tuning pipeline for llm
[144] D. Yang, R. Yuan, Y. Fan, Y. Yang, Z. Wang, S. Wang, and H. Zhao,              in retrieval-augmented generation,” in Proceedings of the 2024
      “Refgpt: Dialogue generation of gpt, by gpt, and for gpt,” in                  Conference on Empirical Methods in Natural Language Processing:
      Findings of the Association for Computational Linguistics: EMNLP               Industry Track, 2024, pp. 1548–1558.
      2023, 2023, pp. 2511–2535.                                               [162] A. Hogan, E. Blomqvist, M. Cochez, C. d’Amato, G. D. Melo,
[145] J. Wei, X. Wang, D. Schuurmans, M. Bosma, B. Ichter, F. Xia, E. H.             C. Gutierrez, S. Kirrane, J. E. L. Gayo, R. Navigli, S. Neumaier
      Chi, Q. V. Le, and D. Zhou, “Chain-of-thought prompting elicits                et al., “Knowledge graphs,” ACM Computing Surveys (Csur),
      reasoning in large language models,” in Proceedings of the 36th                vol. 54, no. 4, pp. 1–37, 2021.
      International Conference on Neural Information Processing Systems,       [163] G. Agrawal, T. Kumarage, Z. Alghamdi, and H. Liu, “Can
      2022, pp. 24 824–24 837.                                                       knowledge graphs reduce hallucinations in llms?: A survey,” in
[146] A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegr-                 Proceedings of the 2024 Conference of the North American Chapter
      effe, U. Alon, N. Dziri, S. Prabhumoye, Y. Yang et al., “Self-refine:          of the Association for Computational Linguistics: Human Language
      iterative refinement with self-feedback,” in Proceedings of the 37th           Technologies (Volume 1: Long Papers), 2024, pp. 3947–3960.
      International Conference on Neural Information Processing Systems,       [164] S. Li, S. Park, I. Lee, and O. Bastani, “Traq: Trustworthy retrieval
      2023, pp. 46 534–46 594.                                                       augmented question answering via conformal prediction,” in
[147] L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. Wainwright,                         Proceedings of the 2024 Conference of the North American Chapter
      P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray et al., “Train-             of the Association for Computational Linguistics: Human Language
      ing language models to follow instructions with human feed-                    Technologies (Volume 1: Long Papers), 2024, pp. 3799–3821.
      back,” Advances in neural information processing systems, vol. 35,       [165] O. Ayala and P. Bechard, “Reducing hallucination in structured
      pp. 27 730–27 744, 2022.                                                       outputs via retrieval-augmented generation,” in Proceedings of the
[148] M. Kim, H. Jung, and M.-W. Koo, “Self-expertise: Knowledge-                    2024 Conference of the North American Chapter of the Association for
      based instruction dataset augmentation for a legal expert lan-                 Computational Linguistics: Human Language Technologies (Volume 6:
      guage model,” in Findings of the Association for Computational                 Industry Track), 2024, pp. 228–238.
      Linguistics: NAACL 2024, 2024, pp. 1098–1112.                            [166] H. Ding, L. Pang, Z. Wei, H. Shen, and X. Cheng, “Retrieve
[149] P. Feldman, J. R. Foulds, and S. Pan, “Trapping llm hallucinations             only when it needs: Adaptive retrieval augmentation for hal-
      using tagged context prompts,” arXiv preprint arXiv:2306.06085,                lucination mitigation in large language models,” arXiv preprint
      2023.                                                                          arXiv:2402.10612, 2024.
[150] S. Penkov, “Mitigating hallucinations in large language models           [167] Y. Sun, S. Wang, S. Feng, S. Ding, C. Pang, J. Shang, J. Liu,
      via semantic enrichment of prompts: Insights from biobert and                  X. Chen, Y. Zhao, Y. Lu et al., “Ernie 3.0: Large-scale knowledge
      ontological integration,” in Proceedings of the Sixth International            enhanced pre-training for language understanding and genera-
      Conference on Computational Linguistics in Bulgaria (CLIB 2024),               tion,” arXiv preprint arXiv:2107.02137, 2021.
      2024, pp. 272–276.                                                       [168] J. Youn and I. Tagkopoulos, “Kglm: Integrating knowledge graph
[151] M. Liang, A. Arun, Z. Wu, C. Munoz, J. Lutch, E. Kazim,                        structure in language models for link prediction,” in Proceedings
      A. Koshiyama, and P. Treleaven, “Thames: An end-to-end tool                    of the 12th Joint Conference on Lexical and Computational Semantics
      for hallucination mitigation and evaluation in large language                  (* SEM 2023), 2023, pp. 217–224.
      models,” arXiv preprint arXiv:2409.11353, 2024.                          [169] S. Tian, Y. Luo, T. Xu, C. Yuan, H. Jiang, C. Wei, and X. Wang, “Kg-
[152] H. Zhang, X. Liu, and J. Zhang, “Summit: Iterative text summa-                 adapter: Enabling knowledge graph integration in large language
      rization via chatgpt,” in Findings of the Association for Computa-             models through parameter-efficient fine-tuning,” in Findings of
      tional Linguistics: EMNLP 2023, 2023, pp. 10 644–10 657.                       the Association for Computational Linguistics ACL 2024, 2024, pp.
[153] T. Vu, M. Iyyer, X. Wang, N. Constant, J. Wei, J. Wei, C. Tar, Y.-             3813–3828.
      H. Sung, D. Zhou, Q. Le et al., “Freshllms: Refreshing large lan-        [170] H. Wang and K. Shu, “Explainable claim verification via
      guage models with search engine augmentation,” arXiv preprint                  knowledge-grounded reasoning with large language models,” in
      arXiv:2310.03214, 2023.                                                        Findings of the Association for Computational Linguistics: EMNLP
[154] K. Guu, K. Lee, Z. Tung, P. Pasupat, and M. Chang, “Retrieval                  2023, 2023, pp. 6288–6304.



[171] Y. Ji, K. Wu, J. Li, W. Chen, M. Zhong, X. Jia, and M. Zhang,               [189] T. Xu, S. Wu, S. Diao, X. Liu, X. Wang, Y. Chen, and J. Gao,
      “Retrieval and reasoning on kgs: Integrate knowledge graphs                       “Sayself: Teaching llms to express confidence with self-reflective
      into large language models for complex question answering,”                       rationales,” in Proceedings of the 2024 Conference on Empirical
      in Findings of the Association for Computational Linguistics: EMNLP               Methods in Natural Language Processing, 2024, pp. 5985–5998.
      2024, 2024, pp. 7598–7610.                                                  [190] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao,
[172] A. G. Regino and J. C. Dos Reis, “Can llms be knowledge graph                     “Reflexion: Language agents with verbal reinforcement learn-
      curators for validating triple insertions?” in Proceedings of the                 ing,” Advances in Neural Information Processing Systems, vol. 36,
      Workshop on Generative AI and Knowledge Graphs (GenAIK), 2025,                    2024.
      pp. 87–99.                                                                  [191] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and
[173] T. Hashem, W. Wang, D. T. Wijaya, M. E. Ali, and Y.-F. Li,                        Y. Cao, “React: Synergizing reasoning and acting in language
      “Generating faithful text from a knowledge graph with noisy                       models,” arXiv preprint arXiv:2210.03629, 2022.
      reference text,” in Proceedings of the 16th International Natural           [192] D. Paul, M. Ismayilzada, M. Peyrard, B. Borges, A. Bosselut,
      Language Generation Conference, 2023, pp. 106–122.                                R. West, and B. Faltings, “Refiner: Reasoning feedback on inter-
[174] J. Baek, A. F. Aji, and A. Saffari, “Knowledge-augmented lan-                     mediate representations,” in Proceedings of the 18th Conference of
      guage model prompting for zero-shot knowledge graph question                      the European Chapter of the Association for Computational Linguistics
      answering,” in Proceedings of the 1st Workshop on Natural Language                (Volume 1: Long Papers), 2024, pp. 1100–1126.
      Reasoning and Structured Explanations (NLRSE), 2023, pp. 78–106.            [193] D. Lee, E. Park, H. Lee, and H.-S. Lim, “Ask, assess, and refine:
[175] J. Jiang, K. Zhou, Z. Dong, K. Ye, W. X. Zhao, and J.-R. Wen,                     Rectifying factual consistency and hallucination in llms with
      “Structgpt: A general framework for large language model to                       metric-guided feedback learning,” in Proceedings of the 18th Con-
      reason over structured data,” in Proceedings of the 2023 Conference               ference of the European Chapter of the Association for Computational
      on Empirical Methods in Natural Language Processing, 2023, pp.                    Linguistics (Volume 1: Long Papers), 2024, pp. 2422–2433.
      9237–9251.                                                                  [194] C. Zhang, L. Liu, C. Wang, X. Sun, H. Wang, J. Wang, and M. Cai,
[176] Z. Yang, Z. Zhu, and J. Zhu, “Curiousllm: Elevating multi-                        “Prefer: Prompt ensemble learning via feedback-reflect-refine,” in
      document question answering with llm-enhanced knowledge                           Proceedings of the AAAI Conference on Artificial Intelligence, vol. 38,
      graph reasoning,” in Proceedings of the 2025 Conference of the                    no. 17, 2024, pp. 19 525–19 532.
      Nations of the Americas Chapter of the Association for Computa-             [195] J. Huang, S. Gu, L. Hou, Y. Wu, X. Wang, H. Yu, and J. Han,
      tional Linguistics: Human Language Technologies (Volume 3: Industry               “Large language models can self-improve,” in Proceedings of the
      Track), 2025, pp. 274–286.                                                        2023 Conference on Empirical Methods in Natural Language Process-
[177] H. Trivedi, N. Balasubramanian, T. Khot, and A. Sabhar-                           ing, 2023, pp. 1051–1068.
      wal, “Interleaving retrieval with chain-of-thought reasoning for            [196] X. Cheng, J. Li, W. X. Zhao, and J.-R. Wen, “Think more, hallu-
      knowledge-intensive multi-step questions,” in Proceedings of the                  cinate less: Mitigating hallucinations via dual process of fast and
      61st Annual Meeting of the Association for Computational Linguistics              slow thinking,” arXiv preprint arXiv:2501.01306, 2025.
      (Volume 1: Long Papers), 2023, pp. 10 014–10 037.                           [197] S. Dhuliawala, M. Komeili, J. Xu, R. Raileanu, X. Li,
[178] L. Luo, Y.-F. Li, G. Haffari, and S. Pan, “Reasoning on graphs:                   A. Celikyilmaz, and J. Weston, “Chain-of-verification reduces
      Faithful and interpretable large language model reasoning,”                       hallucination in large language models,” in Findings of
      arXiv preprint arXiv:2310.01061, 2023.                                            the Association for Computational Linguistics ACL 2024, L.-
                                                                                        W. Ku, A. Martins, and V. Srikumar, Eds. Bangkok,
[179] X. Tan, X. Wang, Q. Liu, X. Xu, X. Yuan, and W. Zhang, “Paths-
                                                                                        Thailand and virtual meeting: Association for Computational
      over-graph: Knowledge graph empowered large language model
                                                                                        Linguistics, Aug. 2024, pp. 3563–3578. [Online]. Available:
      reasoning,” in Proceedings of the ACM on Web Conference 2025,
                                                                                        https://aclanthology.org/2024.findings-acl.212
      2025, pp. 3505–3522.
                                                                                  [198] D. Lei, Y. Li, M. Hu, M. Wang, V. Yun, E. Ching, and
[180] S. Gautam and R. Pop, “Factgenius: Combining zero-shot
                                                                                        E. Kamal, “Chain of natural language inference for reducing
      prompting and fuzzy relation mining to improve fact verifica-
                                                                                        large language model ungrounded hallucinations,” arXiv preprint
      tion with knowledge graphs,” in Proceedings of the Seventh Fact
                                                                                        arXiv:2310.03951, 2023.
      Extraction and VERification Workshop (FEVER), 2024, pp. 297–306.
                                                                                  [199] Q. Huang, F. Huang, D. Tao, Y. Zhao, B. Wang, and Y. Huang,
[181] X. Guan, Y. Liu, H. Lin, Y. Lu, B. He, X. Han, and L. Sun,                        “Coq: An empirical framework for multi-hop question answer-
      “Mitigating large language model hallucinations via autonomous                    ing empowered by large language models,” in ICASSP 2024-
      knowledge graph-based retrofitting,” in Proceedings of the AAAI                   2024 IEEE International Conference on Acoustics, Speech and Signal
      Conference on Artificial Intelligence, vol. 38, no. 16, 2024, pp. 18 126–         Processing (ICASSP). IEEE, 2024, pp. 11 566–11 570.
      18 134.
                                                                                  [200] Y. Zhang, X. Wang, J. Liang, S. Xia, L. Chen, and Y. Xiao, “Chain-
[182] X. Zhao, M. Li, W. Lu, C. Weber, J. H. Lee, K. Chu, and                           of-knowledge: Integrating knowledge reasoning into large lan-
      S. Wermter, “Enhancing zero-shot chain-of-thought reasoning                       guage models by learning from knowledge graphs,” arXiv
      in large language models through logic,” in Proceedings of the                    preprint arXiv:2407.00653, 2024.
      2024 Joint International Conference on Computational Linguistics,           [201] X. Li, R. Zhao, Y. K. Chia, B. Ding, S. Joty, S. Poria, and L. Bing,
      Language Resources and Evaluation (LREC-COLING 2024), 2024, pp.                   “Chain-of-knowledge: Grounding large language models via dy-
      6144–6166.                                                                        namic knowledge adapting over heterogeneous sources,” arXiv
[183] M. A. Sultan, J. Ganhotra, and R. F. Astudillo, “Structured                       preprint arXiv:2305.13269, 2023.
      chain-of-thought prompting for few-shot generation of content-              [202] W. Yu, H. Zhang, X. Pan, K. Ma, H. Wang, and D. Yu, “Chain-
      grounded qa conversations,” in Findings of the Association for                    of-note: Enhancing robustness in retrieval-augmented language
      Computational Linguistics: EMNLP 2024, 2024, pp. 16 172–16 187.                   models,” arXiv preprint arXiv:2311.09210, 2023.
[184] J. Li, G. Li, Y. Li, and Z. Jin, “Structured chain-of-thought               [203] Y.-S. Chuang, Y. Xie, H. Luo, Y. Kim, J. Glass, and P. He, “Dola:
      prompting for code generation,” ACM Transactions on Software                      Decoding by contrasting layers improves factuality in large lan-
      Engineering and Methodology, vol. 34, no. 2, pp. 1–23, 2025.                      guage models,” arXiv preprint arXiv:2309.03883, 2023.
[185] Y. Li, Y. Shen, Y. Nian, J. Gao, Z. Wang, C. Yu, S. Li, J. Wang, X. Hu,     [204] W. Shi, X. Han, M. Lewis, Y. Tsvetkov, L. Zettlemoyer, and W.-
      and Y. Zhao, “Mitigating hallucinations in large language models                  t. Yih, “Trusting your evidence: Hallucinate less with context-
      via causal reasoning,” arXiv preprint arXiv:2508.12495, 2025.                     aware decoding,” in Proceedings of the 2024 Conference of the North
[186] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang,                         American Chapter of the Association for Computational Linguistics:
      A. Chowdhery, and D. Zhou, “Self-consistency improves chain                       Human Language Technologies (Volume 2: Short Papers), 2024, pp.
      of thought reasoning in language models,” arXiv preprint                          783–791.
      arXiv:2203.11171, 2022.                                                     [205] J. Waldendorf, B. Haddow, and A. Birch, “Contrastive decoding
[187] Y. Li, Z. Lin, S. Zhang, Q. Fu, B. Chen, J.-G. Lou, and W. Chen,                  reduces hallucinations in large multilingual machine translation
      “Making large language models better reasoners with step-aware                    models,” in Proceedings of the 18th Conference of the European
      verifier,” arXiv preprint arXiv:2206.02336, 2022.                                 Chapter of the Association for Computational Linguistics (Volume 1:
[188] Y. Liang, Z. Song, H. Wang, and J. Zhang, “Learning to trust your                 Long Papers), 2024, pp. 2526–2539.
      feelings: Leveraging self-awareness in llms for hallucination miti-         [206] R. Sennrich, J. Vamvas, and A. Mohammadshahi, “Mitigating
      gation,” in Proceedings of the 3rd Workshop on Knowledge Augmented                hallucinations and off-target machine translation with source-
      Methods for NLP, 2024, pp. 44–58.                                                 contrastive and language-contrastive decoding,” in Proceedings



      of the 18th Conference of the European Chapter of the Association for           tion,” in Proceedings of the 2023 Conference on Empirical Methods in
      Computational Linguistics (Volume 2: Short Papers), 2024, pp. 21–33.            Natural Language Processing, 2023, pp. 8914–8932.
[207] Y. Chang, B. Cao, and L. Lin, “Monitoring decoding: Mitigating            [227] Y. Huang, C. Fan, Y. Li, S. Wu, T. Zhou, X. Zhang, and L. Sun,
      hallucination via evaluating the factuality of partial response                 “1+ 1¿ 2: Can large language models serve as cross-lingual
      during generation,” arXiv preprint arXiv:2503.03106, 2025.                      knowledge aggregators?” in Proceedings of the 2024 Conference on
[208] G. Hinton, “Distilling the knowledge in a neural network,” arXiv                Empirical Methods in Natural Language Processing, 2024, pp. 13 394–
      preprint arXiv:1503.02531, 2015.                                                13 412.
[209] D. McDonald, R. Papadopoulos, and L. Benningfield, “Reducing              [228] B. Y. Lin, R. L. Bras, K. Richardson, A. Sabharwal, R. Poovendran,
      llm hallucination using knowledge distillation: A case study with               P. Clark, and Y. Choi, “Zebralogic: On the scaling limits of llms
      mistral large and mmlu benchmark,” Authorea Preprints.                          for logical reasoning,” arXiv preprint arXiv:2502.01100, 2025.
[210] H. Nguyen, Z. He, S. A. Gandre, U. Pasupulety, S. K. Shivaku-             [229] N. Varshney, S. Raj, V. Mishra, A. Chatterjee, R. Sarkar, A. Saeidi,
      mar, and K. Lerman, “Smoothing out hallucinations: Mitigating                   and C. Baral, “Investigating and addressing hallucinations of
      llm hallucination with smoothed knowledge distillation,” arXiv                  llms in tasks involving negation,” arXiv preprint arXiv:2406.05494,
      preprint arXiv:2502.11306, 2025.                                                2024.
[211] W. Liu, G. Li, K. Zhang, B. Du, Q. Chen, X. Hu, H. Xu, J. Chen,           [230] B. Lester, R. Al-Rfou, and N. Constant, “The power of scale for
      and J. Wu, “Mind’s mirror: Distilling self-evaluation capability                parameter-efficient prompt tuning,” in Proceedings of the 2021
      and comprehensive thinking from large language models,” in                      Conference on Empirical Methods in Natural Language Processing,
      Proceedings of the 2024 Conference of the North American Chapter                2021, pp. 3045–3059.
      of the Association for Computational Linguistics: Human Language          [231] X. Liu, K. Ji, Y. Fu, W. Tam, Z. Du, Z. Yang, and J. Tang, “P-
      Technologies (Volume 1: Long Papers), 2024, pp. 6748–6763.                      tuning: Prompt tuning can be comparable to fine-tuning across
[212] M. Elaraby, M. Lu, J. Dunn, X. Zhang, Y. Wang, S. Liu, P. Tian,                 scales and tasks,” in Proceedings of the 60th Annual Meeting of the
      Y. Wang, and Y. Wang, “Halo: Estimation and reduction of hal-                   Association for Computational Linguistics (Volume 2: Short Papers),
      lucinations in open-source weak large language models,” arXiv                   2022, pp. 61–68.
      preprint arXiv:2308.11764, 2023.                                          [232] X. L. Li and P. Liang, “Prefix-tuning: Optimizing continuous
[213] M. Hu, B. He, Y. Wang, L. Li, C. Ma, and I. King, “Mitigating large             prompts for generation,” in Proceedings of the 59th Annual Meeting
      language model hallucination with faithful finetuning,” arXiv                   of the Association for Computational Linguistics and the 11th Inter-
      preprint arXiv:2406.11267, 2024.                                                national Joint Conference on Natural Language Processing (Volume 1:
                                                                                      Long Papers), 2021, pp. 4582–4597.
[214] J. Li, Y. Tang, and Y. Yang, “Know the unknown: An uncertainty-
      sensitive method for llm instruction tuning,” arXiv preprint              [233] J. Hu, S. Ruder, A. Siddhant, G. Neubig, O. Firat, and M. Johnson,
      arXiv:2406.10099, 2024.                                                         “Xtreme: A massively multilingual multi-task benchmark for
                                                                                      evaluating cross-lingual generalisation,” in International Confer-
[215] H. Zhang, S. Diao, Y. Lin, Y. R. Fung, Q. Lian, X. Wang, Y. Chen,
                                                                                      ence on Machine Learning. PMLR, 2020, pp. 4411–4421.
      H. Ji, and T. Zhang, “R-tuning: Teaching large language models
                                                                                [234] A. Ansell, E. Ponti, A. Korhonen, and I. Vulić, “Composable
      to refuse unknown questions,” arXiv preprint arXiv:2311.09677,
                                                                                      sparse fine-tuning for cross-lingual transfer,” in Proceedings of the
      2023.
                                                                                      60th Annual Meeting of the Association for Computational Linguistics
[216] R. Zhu, Z. Jiang, J. Wu, Z. Ma, J. Song, F. Bai, D. Lin, L. Wu,
                                                                                      (Volume 1: Long Papers), 2022, pp. 1778–1796.
      and C. He, “Grait: Gradient-driven refusal-aware instruction
                                                                                [235] Vectara, “Hallucination leaderboard: Leaderboard comparing llm
      tuning for effective hallucination mitigation,” arXiv preprint
                                                                                      performance at producing hallucinations when summarizing
      arXiv:2502.05911, 2025.
                                                                                      short documents,” https://github.com/vectara/hallucination-
[217] P. Dey, S. Merugu, and S. Kaveri, “Uncertainty-aware fusion:                    leaderboard, 2023–2026, accessed: 2026-02-08.
      An ensemble framework for mitigating hallucinations in large
                                                                                [236] J. Kasai, K. Sakaguchi, Y. Takahashi, R. Le Bras, A. Asai, X. V.
      language models,” in Companion Proceedings of the ACM on Web
                                                                                      Yu, D. Radev, N. A. Smith, Y. Choi, and K. Inui, “Realtime
      Conference 2025, 2025, pp. 947–951.
                                                                                      qa: what’s the answer right now?” in Proceedings of the 37th
[218] M. Crawshaw, “Multi-task learning with deep neural networks:                    International Conference on Neural Information Processing Systems,
      A survey,” arXiv preprint arXiv:2009.09796, 2020.                               2023, pp. 49 025–49 043.
[219] D. Cheng, S. Huang, J. Bi, Y. Zhan, J. Liu, Y. Wang, H. Sun, F. Wei,      [237] B. Goodrich, V. Rao, P. J. Liu, and M. Saleh, “Assessing the
      W. Deng, and Q. Zhang, “Uprise: Universal prompt retrieval                      factual accuracy of generated text,” in proceedings of the 25th
      for improving zero-shot evaluation,” in Proceedings of the 2023                 ACM SIGKDD international conference on knowledge discovery &
      Conference on Empirical Methods in Natural Language Processing,                 data mining, 2019, pp. 166–175.
      2023, pp. 12 318–12 337.                                                  [238] S. Narayan, S. B. Cohen, and M. Lapata, “Don’t give me the
[220] S. Chopra, R. Hadsell, and Y. LeCun, “Learning a similarity                     details, just the summary! Topic-aware convolutional neural
      metric discriminatively, with application to face verification,” in             networks for extreme summarization,” in Proceedings of the 2018
      2005 IEEE computer society conference on computer vision and pattern            Conference on Empirical Methods in Natural Language Processing,
      recognition (CVPR’05), vol. 1. IEEE, 2005, pp. 539–546.                         Brussels, Belgium, 2018.
[221] S. Cao and L. Wang, “Cliff: Contrastive learning for improving            [239] Z. Yang, P. Qi, S. Zhang, Y. Bengio, W. Cohen, R. Salakhutdinov,
      faithfulness and factuality in abstractive summarization,” in Pro-              and C. D. Manning, “Hotpotqa: A dataset for diverse, explainable
      ceedings of the 2021 Conference on Empirical Methods in Natural                 multi-hop question answering,” in Proceedings of the 2018 Confer-
      Language Processing, 2021, pp. 6633–6649.                                       ence on Empirical Methods in Natural Language Processing, 2018, pp.
[222] W. Sun, Z. Shi, S. Gao, P. Ren, M. de Rijke, and Z. Ren,                        2369–2380.
      “Contrastive learning reduces hallucination in conversations,” in         [240] J. Li, X. Cheng, W. X. Zhao, J.-Y. Nie, and J.-R. Wen, “Halueval:
      Proceedings of the AAAI Conference on Artificial Intelligence, vol. 37,         A large-scale hallucination evaluation benchmark for large lan-
      no. 11, 2023, pp. 13 618–13 626.                                                guage models,” in Proceedings of the 2023 Conference on Empirical
[223] M. Abdelrahman, “Hallucination in low-resource languages:                       Methods in Natural Language Processing, 2023, pp. 6449–6464.
      Amplified risks and mitigation strategies for multilingual llms,”         [241] A. Rahman, S. Anwar, M. Usman, and A. Mian, “Defan: Defini-
      Journal of Applied Big Data Analytics, Decision-Making, and Predic-             tive answer dataset for llms hallucination evaluation,” arXiv
      tive Modelling Systems, vol. 8, no. 12, pp. 17–24, 2024.                        preprint arXiv:2406.09155, 2024.
[224] Y. Fan, R. Li, G. Zhang, C. Shi, and X. Wang, “A weighted cross-          [242] A. Parikh, X. Wang, S. Gehrmann, M. Faruqui, B. Dhingra,
      entropy loss for mitigating llm hallucinations in cross-lingual                 D. Yang, and D. Das, “Totto: A controlled table-to-text generation
      continual pretraining,” in ICASSP 2025-2025 IEEE International                  dataset,” in Proceedings of the 2020 Conference on Empirical Methods
      Conference on Acoustics, Speech and Signal Processing (ICASSP).                 in Natural Language Processing (EMNLP), 2020, pp. 1173–1186.
      IEEE, 2025, pp. 1–5.                                                      [243] M. Joshi, E. Choi, D. S. Weld, and L. Zettlemoyer, “Triviaqa: A
[225] W. Zheng, R. K.-W. Lee, Z. Liu, K. Wu, A. Aw, and                               large scale distantly supervised challenge dataset for reading
      B. Zou, “Ccl-xcot: An efficient cross-lingual knowledge transfer                comprehension,” in Proceedings of the 55th Annual Meeting of the
      method for mitigating hallucination generation,” arXiv preprint                 Association for Computational Linguistics (Volume 1: Long Papers),
      arXiv:2507.14239, 2025.                                                         2017, pp. 1601–1611.
[226] Y. Qiu, Y. Ziser, A. Korhonen, E. Ponti, and S. B. Cohen, “De-            [244] P. Gupta, C.-S. Wu, W. Liu, and C. Xiong, “Dialfact: A benchmark
      tecting and mitigating hallucinations in multilingual summarisa-                for fact-checking in dialogue,” in Proceedings of the 60th Annual



      Meeting of the Association for Computational Linguistics (Volume 1:             evaluation metrics – the mirage of hallucination detection,” 2025.
      Long Papers), 2022, pp. 3785–3801.                                              [Online]. Available: https://arxiv.org/abs/2504.18114
[245] W. Kryściński, B. McCann, C. Xiong, and R. Socher, “Evaluating          [261] K. Maharaj, A. Saxena, R. Kumar, A. Mishra, and
      the factual consistency of abstractive text summarization,” in                  P. Bhattacharyya, “Eyes show the way: Modelling gaze behaviour
      Proceedings of the 2020 Conference on Empirical Methods in Natural              for hallucination detection,” in Findings of the Association for
      Language Processing (EMNLP), 2020, pp. 9332–9346.                               Computational Linguistics: EMNLP 2023, H. Bouamor, J. Pino,
[246] S. Pandit, J. Xu, J. Hong, Z. Wang, T. Chen, K. Xu, and Y. Ding,                and K. Bali, Eds. Singapore: Association for Computational
      “Medhallu: A comprehensive benchmark for detecting med-                         Linguistics, Dec. 2023, pp. 11 424–11 438. [Online]. Available:
      ical hallucinations in large language models,” arXiv preprint                   https://aclanthology.org/2023.findings-emnlp.764/
      arXiv:2502.14302, 2025.                                                   [262] Y. Bang, Z. Ji, A. Schelten, A. Hartshorn, T. Fowler,
[247] O. r. Bojar, C. Federmann, M. Fishel, Y. Graham, B. Haddow,                     C. Zhang, N. Cancedda, and P. Fung, “HalluLens: LLM
      M. Huck, P. Koehn, and C. Monz, “Findings of the 2018                           hallucination benchmark,” in Proceedings of the 63rd Annual
      conference on machine translation (wmt18),” in Proceedings of                   Meeting of the Association for Computational Linguistics (Volume
      the Third Conference on Machine Translation, Volume 2: Shared                   1: Long Papers), W. Che, J. Nabende, E. Shutova, and M. T.
      Task Papers. Belgium, Brussels: Association for Computational                   Pilehvar, Eds. Vienna, Austria: Association for Computational
      Linguistics, October 2018, pp. 272–307. [Online]. Available:                    Linguistics, Jul. 2025, pp. 24 128–24 156. [Online]. Available:
      http://www.aclweb.org/anthology/W18-6401                                        https://aclanthology.org/2025.acl-long.1176/
[248] L. Mascarell, R. Chalumattu, and A. R. Gonzales, “German also             [263] Q. Liu, X. Chen, Y. Ding, S. Xu, S. Wu, and L. Wang, “Attention-
      hallucinates! inconsistency detection in news summaries with                    guided self-reflection for zero-shot hallucination detection in
      the absinth dataset,” in Proceedings of the 2024 Joint International            large language models,” arXiv preprint arXiv:2501.09997, 2025.
      Conference on Computational Linguistics, Language Resources and           [264] Y. Huang, Y. Zhang, N. Cheng, Z. Li, S. Wang, and J. Xiao,
      Evaluation (LREC-COLING 2024), 2024, pp. 7696–7706.                             “Dynamic attention-guided context decoding for mitigating con-
[249] H. Mubarak, H. Al-Khalifa, and K. S. Alkhalefah, “Halwasa:                      text faithfulness hallucinations in large language models,” arXiv
      Quantify and analyze hallucinations in large language models:                   preprint arXiv:2501.01059, 2025.
      Arabic as a case study,” in Proceedings of the 2024 Joint International   [265] T. Oorloff, Y. Yacoob, and A. Shrivastava, “Mitigating halluci-
      Conference on Computational Linguistics, Language Resources and                 nations in diffusion models through adaptive attention modula-
      Evaluation (LREC-COLING 2024), 2024, pp. 8008–8015.                             tion,” arXiv preprint arXiv:2502.16872, 2025.
[250] H. Mubarak, R. Malhas, W. Mansour, A. Mohamed, M. Fawzi,                  [266] Z. Duan and J. Wang, “Prompt-based monte carlo tree search
      M. Hawasly, T. Elsayed, K. M. Darwish, and W. Magdy, “Islam-                    for mitigating hallucinations in large models,” arXiv preprint
      iceval 2025: The first shared task of capturing llms hallucination              arXiv:2501.13942, 2025.
      in islamic content,” in Proceedings of The Third Arabic Natural           [267] L. Chua, B. Ghazi, Y. Huang, P. Kamath, R. Kumar, P. Manurangsi,
      Language Processing Conference: Shared Tasks, 2025, pp. 480–493.                A. Sinha, C. Xie, and C. Zhang, “Crosslingual capabilities and
[251] A. Alansari and H. Luqman, “Arahallueval: A fine-grained hal-                   knowledge barriers in multilingual large language models,”
      lucination evaluation framework for arabic llms,” arXiv preprint                2025. [Online]. Available: https://arxiv.org/abs/2406.16135
      arXiv:2509.04656, 2025.                                                   [268] G. Chen, S. Chen, Z. Liu, F. Jiang, and B. Wang, “Humans or
                                                                                      llms as the judge? a study on judgement bias,” in Proceedings
[252] M. Y. Mohammed, S. A. Ali, S. K. Ali, A. A. Majeed, and E. H.
                                                                                      of the 2024 Conference on Empirical Methods in Natural Language
      Mohamed, “Aftina: enhancing stability and preventing halluci-
                                                                                      Processing, 2024, pp. 8301–8327.
      nation in ai-based islamic fatwa generation using llms and rag,”
                                                                                [269] L. Shi, C. Ma, W. Liang, X. Diao, W. Ma, and S. Vosoughi,
      Neural Computing and Applications, pp. 1–26, 2025.
                                                                                      “Judging the judges: A systematic study of position bias in llm-
[253] X. Liang, S. Song, S. Niu, Z. Li, F. Xiong, B. Tang, Y. Wang,
                                                                                      as-a-judge,” in Proceedings of the 14th International Joint Conference
      D. He, C. Peng, Z. Wang et al., “Uhgeval: Benchmarking the
                                                                                      on Natural Language Processing and the 4th Conference of the Asia-
      hallucination of chinese large language models via unconstrained
                                                                                      Pacific Chapter of the Association for Computational Linguistics, 2025,
      generation,” in Proceedings of the 62nd Annual Meeting of the
                                                                                      pp. 292–314.
      Association for Computational Linguistics (Volume 1: Long Papers),
                                                                                [270] H. Li, Q. Dong, J. Chen, H. Su, Y. Zhou, Q. Ai, Z. Ye, and
      2024, pp. 5266–5293.
                                                                                      Y. Liu, “Llms-as-judges: a comprehensive survey on llm-based
[254] Q. Cheng, T. Sun, W. Zhang, S. Wang, X. Liu, M. Zhang, J. He,                   evaluation methods,” arXiv preprint arXiv:2412.05579, 2024.
      M. Huang, Z. Yin, K. Chen et al., “Evaluating hallucinations in           [271] K. Chehbouni, M. Haddou, J. C. K. Cheung, and G. Farnadi,
      chinese large language models,” arXiv preprint arXiv:2310.03368,                “Neither valid nor reliable? investigating the use of llms as
      2023.                                                                           judges,” arXiv preprint arXiv:2508.18076, 2025.
[255] A. Pal, L. K. Umapathi, and M. Sankarasubbu, “Med-halt: Medi-
      cal domain hallucination test for large language models,” in Pro-
      ceedings of the 27th Conference on Computational Natural Language
      Learning (CoNLL), 2023, pp. 314–334.
[256] D. Dale, E. Voita, J. Lam, P. Hansanti, C. Ropers, E. Kalbassi,
      C. Gao, L. Barrault, and M. Costa-jussà, “Halomi: A manually
      annotated benchmark for multilingual hallucination and omis-
      sion detection in machine translation,” in Proceedings of the 2023
      Conference on Empirical Methods in Natural Language Processing,
      2023, pp. 638–653.
[257] R. Vázquez, T. Mickus, E. Zosa, T. Vahtola, J. Tiedemann,
      A. Sinha, V. Segonne, F. Sánchez-Vega, A. Raganato, J. Libovickỳ
      et al., “Semeval-2025 task 3: Mu-shroom, the multilingual shared
      task on hallucinations and related observable overgeneration
      mistakes,” arXiv preprint arXiv:2504.11975, 2025.
[258] P. Narayanan Venkit, T. Chakravorti, V. Gupta, H. Biggs,
      M. Srinath, K. Goswami, S. Rajtmajer, and S. Wilson, “An
      audit on the perspectives and challenges of hallucinations
      in NLP,” in Proceedings of the 2024 Conference on Empirical
      Methods in Natural Language Processing, Y. Al-Onaizan, M. Bansal,
      and Y.-N. Chen, Eds. Miami, Florida, USA: Association for
      Computational Linguistics, Nov. 2024, pp. 6528–6548. [Online].
      Available: https://aclanthology.org/2024.emnlp-main.375/
[259] Y. Liu, D. Iter, Y. Xu, S. Wang, R. Xu, and C. Zhu, “G-eval:
      Nlg evaluation using gpt-4 with better human alignment,” 2023.
      [Online]. Available: https://arxiv.org/abs/2303.16634
[260] A. Kulkarni, Y. Zhang, J. R. A. Moniz, X. Ge, B.-H. Tseng,
      D. Piraviperumal, S. Swayamdipta, and H. Yu, “Evaluating
