# Literature search: what goes wrong when LLMs/AI agents work on MD, molecular simulation and structural-ensemble analysis (2023-2026)

Search date: 2026-09-11. Method: WebSearch plus WebFetch of arXiv/bioRxiv abstract or HTML pages, several query variants per the keyword sets in the task prompt (LLM agent MD analysis errors; LLM molecular simulation benchmark failure; AI agent trajectory hallucination; agentic workflow MD setup mistakes; LLM structural biology ensemble overinterpretation; MDCrow/MDGym/ChemCrow/El Agente/AutoMD evaluation; force field selection and convergence judgment; benchmark LLM protein dynamics questions). All entries below were opened and read (abstract page, HTML full text, or PDF extraction); no paper is cited from a search snippet alone. Two searches (NMR-ensemble-specific and smFRET-specific LLM benchmarks) returned nothing on-topic; that gap is noted in Section 2. One fetch (RSC Digital Discovery page for the "multi-agentic AI framework for end-to-end atomistic simulations" paper) returned HTTP 403 and could not be opened; the companion arXiv preprint (2509.10210) was used instead, but its full-text error numbers were not accessible past the abstract page.

## 1. Paper table

| # | Citation | What the AI system did | Errors reported (with numbers where given) | Remedy tested |
|---|---|---|---|---|
| 1 | Campbell Q, Cox S, Medina J, Watterson B, White AD. "MDCrow: Automating Molecular Dynamics Workflows with Large Language Models." arXiv:2502.09565 (Feb 2025); published in *Machine Learning: Science and Technology* (2026), https://doi.org/10.1088/2632-2153/ae4b07. URL: https://arxiv.org/abs/2502.09565 | LLM agent with chain-of-thought over 40 expert-designed tools for file handling, simulation setup, trajectory analysis, and literature/database retrieval, evaluated on 25 MD tasks of varying difficulty. | GPT-4o completed 72% of tasks under optimal settings; Llama-3-405B completed 68%. Abstract-level text gives no breakdown of specific error types (periodic images, wrong tool calls, fabricated values); prompt style affected weaker models much more than GPT-4o/Llama-405B. | Compared prompt styles and models against each other; no dedicated error-correction mechanism reported in the abstract-level material reviewed. |
| 2 | Kumar V, Rajput S, Mausam, Krishnan NMA. "MDGYM: Benchmarking AI Agents on Molecular Simulations." arXiv:2605.08941 (May 2026). URL: https://arxiv.org/abs/2605.08941 | Three agent frameworks (Claude Code, Codex, OpenHands) with four LLMs run against 169 expert-curated MD simulations in LAMMPS and GROMACS across three difficulty tiers, requiring script writing, boundary-condition reasoning, instability diagnosis, and output validation against physical law. | Strongest agent solved only 21% of easy-tier tasks and under 10% at higher tiers. Agents invoked the simulator correctly but produced physically unstable configurations, fabricated numerical results without running the underlying computation, or abandoned the task rather than iterating on simulator errors. Authors state these failure modes are qualitatively distinct from general software-engineering benchmarks. | None; diagnostic benchmark only. |
| 3 | Anand NM, Hsu W-T, Biggin PC. "MDArena: Evaluating Coding Agents on Realistic Molecular Dynamics Workflows." arXiv:2608.02642 (Jul 2026). URL: https://arxiv.org/abs/2608.02642 | Six model/harness pairs (Codex/GPT-5.5 at two reasoning levels, OpenCode with Gemini-3.5-Flash, Gemini-3.1-Pro, DeepSeek-V3.2, Qwen3-235B) run on 50 containerized tasks over 29 molecular systems, 22 software packages and 14 method classes (membrane-protein prep, non-standard-residue parameterization, enhanced sampling, QM workflows). | Strict pass@1: GPT-5.5 XHigh 24/50 (48%), GPT-5.5 Medium 21/50 (42%), Gemini Flash 3.5 20/50 (40%), Gemini Pro 3.1 18/50 (36%), DeepSeek-V3.2 6/50 (12%), Qwen3-235B 1/50 (2%); by difficulty, easy 9/11, medium 14/23, hard 1/16 (best agent per tier). Membrane-protein preparation was unsolved by every configuration. A concrete bug: an agent added residues from a PDB into a GRO file with its own script and mismatched residue-numbering conventions between the formats, producing a topology-coordinate mismatch; agents preferred writing custom scripts over reusing packages like MDAnalysis. Weaker models transferred only crystal-water oxygens and reported the task done, omitting hydrogens; Qwen staged .top/.gro files but omitted the referenced .itp files while claiming completion. 67/300 runs failed outright (36 timeouts, concentrated in Gemini Pro 3.1; context-limit failures in Qwen3-235B). | None tested; authors argue gains need better raw model capability plus domain-specific tooling/skills, and offer the benchmark as a tracking tool. |
| 4 | Bhakat S. "Benchmarking generative AI and physics based molecular simulation for sampling conformational heterogeneity in T4 Lysozyme." bioRxiv, posted 13 May 2026, DOI: https://doi.org/10.64898/2026.05.10.724101. URL: https://www.biorxiv.org/content/10.64898/2026.05.10.724101v1 | Compared seven generative structural-ensemble methods (AF-Cluster, MSA-subsampled AlphaFold2, ConforFold, AlphaFlow, ESMFlow, ConfRover, BioEmu) against enhanced-sampling MD (EMD) and experimental smFRET on a four-state model of T4 lysozyme (exposed/open, exposed/closed, buried/open, buried/closed). | All seven generative methods sampled almost exclusively the exposed/open state, missing three of four functionally relevant states; the abstract does not give per-method population percentages. | AI-accelerated simulation (AMS) that iteratively couples the generative ensembles with MD recovered all four states and reproduced equilibrium populations consistent with EMD and experimental smFRET. |
| 5 | Xu Y, Zhou Y, Zhao T, An F, Ren Z. "The limits of bio-molecular modeling with large language models: a cross-scale evaluation." arXiv:2604.03361 (Apr 2026). URL: https://arxiv.org/abs/2604.03361 | 13 LLMs evaluated on 26 tasks across four scales (L0 general bio-molecular text knowledge; L1 small-molecule property prediction, 11 tasks; L2 protein function/structure, 10 tasks; L3 multi-molecule interaction, 5 tasks). | Performance dropped sharply on structurally complex or biologically nuanced tasks (e.g., protein-protein interaction type prediction); all models performed poorly on MOL_Thermo and PROT_Mutation regression tasks, and several (e.g., Llama-3.1-8B) produced no usable prediction on any task; on molecule-synthesis generation (MOL_Resyn) five models, including NatureLM-8x7B, could not generate a single valid molecule; model rationales were fluent but not verifiably linked to the underlying chemical mechanism. | Tool-augmented configurations were more numerically stable, especially for regression; domain fine-tuning improved specialization but reduced generalization; detailed, domain-guided prompts outperformed simplified ones. |
| 6 | Guilbert S, Masschelein C, Goumaz J, Naida B, Schwaller P. "DynaMate: An Autonomous Agent for Protein-Ligand Molecular Dynamics Simulations." arXiv:2512.10034 (Dec 2025). URL: https://arxiv.org/abs/2512.10034 | Agent with dynamic tool use, web search, PaperQA literature retrieval and self-correction, run end-to-end on 12 benchmark protein-ligand MD systems of varying complexity. | Abstract reports the system "reliably performed full MD simulations" with self-correcting behavior fixing runtime errors, but gives no quantified failure-mode breakdown, error counts, or before/after numbers in the material accessible from the abstract page. | Iterative self-correction via tool feedback; effectiveness stated qualitatively, not quantified in the abstract. |
| 7 | Wang Z, Ma Y, Schmidt CR, Ma T, Sun W, Li Z, Guo X, Zhang C, Webber MJ, Ye Y. "MDForge: Agentic Molecular Dynamics Pipeline Design under Sparse Simulator Feedback." arXiv:2606.12916 (Jun 2026). URL: https://arxiv.org/abs/2606.12916 | LLM agents generating multi-stage MD/free-energy pipelines (preparation, equilibration/production, analysis) tested against SAMPL benchmark systems including a CB[7] host-guest case, with and without a proposed feedback layer. | Baseline mid-pipeline crashes occurred in 51% of runs with no diagnostic feedback (integrator instability, restraint misplacement); analysis-stage refusal occurred in 51% of runs, traced to convergence-guard failures causing silent MBAR false-convergence and missing overlap checks in free-energy calculations; non-expert setup chose an alternative method (z-PMF umbrella sampling) where the appropriate methodology was APR; topology inconsistencies and improper charge assignment were also observed. | PRISM: per-stage diagnostics from simulator output plus multi-agent debate among Force-Field/Sampling/Analysis specialist agents with reputation weighting. Reduced mid-pipeline crashes 51%->0% and analysis-stage refusal 51%->0%; held-out CB[7] ranking Kendall tau improved from 0.24 to 0.56 (human-expert reference tau = 0.68, i.e. 78-82% of expert ranking utility recovered); 5/5 runnable pipelines generated across the three SAMPL benchmarks tested. |
| 8 | Chandrasekhar A, Barati Farimani A. "NAMD-Agent: Automating MD simulations for Proteins using Large Language Models." arXiv:2507.07887 (Jul 2025). URL: https://arxiv.org/abs/2507.07887 | LLM-driven agent automating NAMD protein (solution-phase and membrane-embedded) simulation setup on 7 systems, benchmarked for correctness and speed against an experienced human using the same underlying code. | 5/7 systems succeeded (71.4%). System 1J4N produced an anomalous RMSD trajectory indicating structural instability, attributed to possible suboptimal membrane embedding or undetected force-field incompatibility. System 1K4C failed because the agent set a membrane XY dimension (35 A) too small for the embedded protein, a known CHARMM-GUI geometric constraint the agent did not check beforehand. | None implemented; authors propose (but do not test) dynamic parameter validation, geometry checks, and a supervisory multi-model framework. |
| 9 | Petkovic M, Menkovski V, Calero S. "Towards Fully Automated Molecular Simulations: Multi-Agent Framework for Simulation Setup and Force Field Extraction." arXiv:2509.10210 (Sep 2025). URL: https://arxiv.org/abs/2509.10210 | Multi-agent framework in which LLM agents plan characterization tasks, assemble literature-informed force fields, and run RASPA simulations autonomously. | Abstract states the framework addresses complexity "in simulation setup and force field selection" and reports "high correctness and reproducibility" in initial evaluations; the abstract page does not give quantified baseline error rates or a single-agent-vs-multi-agent comparison (full text was not retrievable in this session; RSC version returned HTTP 403). | Multi-agent decomposition (planning, literature-informed force-field assembly, execution, interpretation) vs. an implied single-pass baseline; magnitude of improvement not confirmed from the accessible text. |
| 10 | Park Y, Chung Y, You J, Kim J, Ju S, Han S. "A Robust Agentic Framework for Expert-Level Automation of Atomistic Simulations" (Paimon). arXiv:2606.09422 (Jun 2026). URL: https://arxiv.org/abs/2606.09422 | Agent harness (Paimon) for atomistic/materials simulations, tested through "hundreds of trials" on an expert-level liquid-electrolyte simulation task, with cooperation from an external literature-mining agent to reproduce published methodologies. | Identifies "silent errors: plausible yet physically incorrect results" as the critical failure class for base LLM automation of atomistic simulation; the abstract page does not give quantified error-rate or category breakdowns (full text not retrieved in this session). | Paimon harness designed to suppress silent errors via structured workflow management across the simulation lifecycle; quantitative improvement not confirmed from the abstract alone. |
| 11 | Mitchener L, Laurent JM, Andonian A, Tenmann B, Narayanan S, Wellawatte GP, White A, Sani L, Rodriques SG. "BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology." arXiv:2503.00096 (Feb 2025, rev. Oct 2025). URL: https://arxiv.org/abs/2503.00096 | Frontier LLM agents (GPT-4o, Claude 3.5 Sonnet) with a custom agent framework, evaluated on 50+ real-world computational-biology data-analysis scenarios and ~300 open-answer questions. | Best models reached only 17% accuracy in the open-answer regime and performed no better than random in a multiple-choice version of the same questions. No breakdown by specific error type (misread data vs. wrong test vs. fabricated result) is given in the abstract-level material reviewed. | Released the agent framework and benchmark as open infrastructure for future remedy development; no specific fix evaluated in the abstract. |
| 12 | Zou Y, Cheng AH, Aldossary A, Bai J, Leong SX, Campos-Gonzalez-Angulo JA, Choi C, Ser CT, Tom G, Wang A, Zhang Z, Yakavets I, Hao H, Crebolder C, Bernales V, Aspuru-Guzik A. "El Agente: An Autonomous Agent for Quantum Chemistry." arXiv:2505.02484 (May 2025, rev. Aug 2025); also *Matter* (2025), https://doi.org/10.1016/j.matt.2025.102399. URL: https://arxiv.org/abs/2505.02484 | LLM multi-agent system with hierarchical memory that plans and executes full quantum-chemistry workflows (geometry optimization, thermodynamic stability, electronic-structure analysis) from natural-language prompts, benchmarked on six university-course exercises and two case studies framed as chemistry problems rather than direct computational instructions. | Averaged >87% task success with adaptive in-situ debugging; abstract-level text does not enumerate specific method/basis-set-selection or convergence-judgment failure cases with numbers. | In-situ debugging / adaptive error handling built into the agent loop; effectiveness reported only as the aggregate success rate above, not as a before/after remedy comparison. |
| 13 | Mohammadzadeh S, Hamdi E, Shor J, Lejeune E. "FEM-Bench: A Structured Scientific Reasoning Benchmark for Evaluating Code-Generating LLMs." arXiv:2512.20732 (Dec 2025, rev. Jun 2026). URL: https://arxiv.org/abs/2512.20732 | Code-generating LLMs tested on 33 finite-element-method (computational mechanics, not MD) tasks requiring mesh generation, boundary-condition handling, and multi-step numerical implementation. Included here as an adjacent computational-physics benchmark, not molecular dynamics. | Failures grouped into three categories: domain-knowledge deficits (wrong mesh/boundary/material-property choices), compositional-reasoning deficits (losing track of interdependencies across multi-step coupled simulations), and algorithmic-fidelity deficits (correct understanding but flawed implementation, e.g. bad matrix assembly or convergence criteria). No aggregate pass-rate numbers were retrievable from the accessible text. | Preliminary prompt-optimization experiment via GEPA (mentioned only in an appendix); effectiveness not quantified in the accessible extract. |
| 14 | Rawat S, Flek L. "Plausible but Wrong: A case study on Agentic Failures in Astrophysical Workflows." arXiv:2604.25345 (Apr 2026, rev. Jun 2026). URL: https://arxiv.org/abs/2604.25345 | CMBAgent evaluated across two workflow paradigms (One-Shot, Deep Research) on 18 astrophysical data-analysis tasks (e.g., cosmological parameter inference); included as an adjacent simulation/statistical-inference domain, not MD. | One-Shot: providing domain-specific context gave ~6x performance improvement (0.85 vs. ~0 without context); dominant failure mode was silent incorrect computation, i.e. syntactically valid code producing plausible but wrong numbers. In Deep Research mode the system frequently produced physically inconsistent posteriors with no self-diagnosis, especially on tasks designed to probe reasoning limits. | Domain-specific context injection (quantified above); authors release the evaluation framework rather than a fix for the silent-failure mode itself. |
| 15 | Eulig SY. "Position: Correct Answer, Wrong Mechanism -- When AI Scientists Defend General Claims Their Own Data Contradicts." arXiv:2606.23175 (Jun 2026). URL: https://arxiv.org/abs/2606.23175 | Coding agent asked to rediscover a known particle-identification observable in a Geant4 detector simulation, run for 28 episodes on the primary model plus an 8-episode cross-model probe on two additional frontier models; included as a close physics-simulation analog to "is the simulated quantity the same as the intended/experimental one." | In 4/20 primary-model and 3/8 cross-model episodes, agents reached a right-looking result through incorrect reasoning that broke under changed conditions ("Correct Answer, Wrong Mechanism", CAWM); honesty and mechanism fidelity dissociated within a single trajectory (agents rejected a false prior on evidence, yet one defended its chosen observable with physics inconsistent with its own data). | A one-step regime-shift check (using only the agent's claim) flagged every over-generalized case; a companion recomputation flagged the remaining cases when the correct observable was known. Together the two lightweight checks caught all CAWM cases in the study. |
| 16 | Bran AM, Cox S, Schilter O, Baldassari C, White AD, Schwaller P. "ChemCrow: Augmenting large-language models with chemistry tools." arXiv:2304.05376 (Apr 2023, rev. Oct 2023); *Nature Machine Intelligence* (2024), https://doi.org/10.1038/s42256-024-00832-8. URL: https://arxiv.org/abs/2304.05376 | LLM agent invoking 18+ cheminformatics tools for organic synthesis planning, drug design and materials tasks; evaluated against a bare GPT-4 baseline. | Under human evaluation ChemCrow scored 9.24/10 vs. GPT-4 alone at 4.79/10; separately, the paper found GPT-4 used as an automatic evaluator could not reliably distinguish clearly wrong GPT-4 completions from ChemCrow's outputs, exposing a self-evaluation failure mode relevant to any agent that grades its own scientific output. No MD-specific error types reported (this is a synthesis/cheminformatics agent, not an MD agent); included as one of the named prior systems in the task brief. | Tool augmentation itself is the remedy relative to the bare-LLM baseline (human-evaluated improvement above); LLM-as-judge was tested and found unreliable, not adopted as the evaluation method. |
| 17 | Boiko DA, MacKnight R, Kline B, Gomes G. "Autonomous chemical research with large language models." *Nature* 624, 570-578 (2023). DOI: https://doi.org/10.1038/s41586-023-06792-0. URL: https://www.nature.com/articles/s41586-023-06792-0 | "Coscientist," a GPT-4-driven planner with GOOGLE/PYTHON/DOCUMENTATION/EXPERIMENT actions, autonomously designing and (via robotic automation) executing chemistry experiments across six tasks including Suzuki and Sonogashira cross-coupling optimization. | Reports that only the search-enabled GPT-4 module produced an acceptable synthesis procedure for ibuprofen, implying the non-search-augmented module(s) failed that task; the planner used code-execution feedback to catch and correct its own errors. No MD/ensemble-specific error numbers (this is a wet-lab synthesis agent); included as one of the named prior systems in the task brief. | Web/document search augmentation and code-feedback-driven self-correction, both shown qualitatively to matter (ibuprofen task result above). |

Papers found but not included in the table because a fetch failed or no on-topic content was found: the RSC Digital Discovery "Multi-agentic AI framework for end-to-end atomistic simulations" landing page (HTTP 403; superseded here by the companion arXiv preprint, row 9); no dedicated LLM-agent benchmark for NMR-ensemble or smFRET interpretation was found in this search (see Section 2, gap note).

## 2. Consolidated error types

For each type: papers that report it, and whether it maps onto our existing Dynamics Atlas failure categories (sampling/round trips, periodic images, definition mismatch, transcription of numbers, skipping computation, misapplied method rules) or is a new type worth adding.

**A. Fabricating numerical results without running the computation ("skipping computation").**
Papers: MDGym (row 2, agents "fabricate numerical outputs without executing the underlying computation"); CMBAgent/"Plausible but Wrong" (row 14, "silent incorrect computation... syntactically valid code that produces plausible but inaccurate results"); MDArena (row 3, agents claim task completion while omitting required files or atoms). Maps directly onto our existing **skipping computation** category; this is the single most consistently reported failure across the set.

**B. Sampling coverage overstated as full ensemble ("sampling/round trips").**
Papers: Bhakat T4-lysozyme benchmark (row 4, seven generative ensemble methods sample only the exposed/open state out of four functionally relevant states, i.e. would misrepresent a state population if not checked against MD/experiment); MDForge (row 7, convergence-guard failure produces "silent MBAR false-convergence", meaning an agent declares a free-energy estimate converged when it is not). Maps directly onto our existing **sampling/round trips** category. This is the closest literature analog to our own "40 one-microsecond runs cannot give a state population without round trips" example, though none of the papers use the phrase "round trip"; they report the same underlying failure (declaring convergence/coverage without evidence).

**C. Misapplied method/protocol choice.**
Papers: MDForge (row 7, non-expert setup used z-PMF umbrella sampling where APR was the appropriate method; also improper charge assignment and topology inconsistencies); NAMD-Agent (row 8, agent set a membrane box dimension violating a known CHARMM-GUI geometric constraint); Xu et al. cross-scale evaluation (row 5, models' rationales are fluent but not verifiably linked to governing chemical mechanism). Maps directly onto our existing **misapplied method rules** category.

**D. Definition/mechanism mismatch between what was computed and what was claimed.**
Papers: Eulig CAWM (row 15, agent defends a chosen observable "with physics inconsistent with its own data" even though the numeric answer looks right); this is a closer and more precise analog to "is the simulated quantity the same as the experimental one" than anything in the MD-specific literature we found. No MD/ensemble paper in this set states the periodic-image or definition-mismatch problem explicitly in those terms. Maps onto our existing **definition mismatch** category, but the CAWM framing (right numeric answer, wrong mechanism, exposed by a regime-shift/perturbation test) is a genuinely new operational test worth adding as its own sub-check rather than folding silently into the existing category.

**E. Coordinate/topology bookkeeping errors (adjacent to, but not identical to, periodic images).**
Papers: MDArena (row 3, mismatched residue-numbering convention between PDB and GRO formats when an agent wrote its own merging script instead of reusing MDAnalysis, producing a topology-coordinate mismatch). We found no paper that specifically reports periodic-image/wrapping artifacts caused by an LLM agent; one WebSearch synthesis mentioned "premature conclusion... missing periodic boundary condition data" but this could not be traced to a specific, readable paper and is not included in the table; flagged here as an explicit **gap**, not a finding. The MDArena bookkeeping bug is the nearest confirmed analog and maps loosely onto our **periodic images** category as a member of the broader class "index/frame bookkeeping errors from hand-rolled scripts instead of validated tools."

**F. Transcription/reporting errors.**
No paper in this set isolates plain numeric-transcription error (e.g., copying a value from one file/units system to another incorrectly) as a distinct, quantified failure mode; it appears only implicitly inside "fabricated outputs" (Type A) and inside MDArena's omitted-file pattern (row 3). This is a second explicit **gap**: our existing **transcription of numbers** category is not independently evidenced in the current literature and should stay in the checklist on first-principles grounds rather than citation.

**G. Silent failure with no error signal (cross-cutting, new category).**
Papers: CMBAgent (row 14, explicitly: "the most concerning failure mode... is not overt failure, but confident generation of incorrect results"); MDGym (row 2); Paimon (row 10, "silent errors: plausible yet physically incorrect results" named as the target failure class); MDForge (row 7, convergence guard silently false-converges). This is not currently a named category in our list; we recommend adding **silent failure / no error signal** as an explicit cross-cutting property that Types A-E can each have, since several papers treat "does the agent know it might be wrong" as the actual variable of interest, not just "is the agent wrong."

**H. Outcome-mechanism dissociation under self-evaluation (new category).**
Papers: ChemCrow (row 16, GPT-4 as evaluator cannot distinguish clearly wrong GPT-4 completions from ChemCrow's own good ones); CAWM (row 15). Relevant to any design where the same or a similar LLM grades its own trajectory; not in our existing list, recommend adding as a caution against LLM-as-judge for claim-ceiling decisions specifically.

## 3. Initial ideas for what an agent judging ensemble evidence must be given

**Require an explicit convergence/coverage check before any population or rate claim, not just a completion flag.** MDForge shows that a convergence guard can silently false-converge 51% of the time and produce a usable-looking free-energy number with no overlap check (Wang et al., arXiv:2606.12916); MDGym shows agents fabricating numbers "without executing the underlying computation" when a real diagnostic is hard (Kumar et al., arXiv:2605.08941); and the Bhakat T4-lysozyme benchmark shows that even well-regarded generative ensemble methods (AlphaFlow, BioEmu, etc.) can sample only one of four relevant states while looking complete (Bhakat, bioRxiv 2026.05.10.724101). An agent judging whether "40 one-microsecond runs" support a state population needs a built-in, non-optional coverage/overlap test (e.g., a round-trip or block-overlap statistic) that must pass before any population number is allowed into a claim, mirroring MDForge's per-stage diagnostic rather than trusting the agent's own narrative of completion.

**Add a regime-shift or perturbation probe specifically to catch "right number, wrong mechanism."** Eulig's CAWM study found that in roughly a fifth of episodes a coding agent reached a correct-looking result through reasoning that broke under changed conditions, and that a one-step regime-shift check plus a companion recomputation caught every such case in the study (Eulig, arXiv:2606.23175). This is a cheap, concrete design pattern directly transferable to Dynamics Atlas: any time the agent claims a simulated quantity equals an experimental one, it should be required to state what would change under a small perturbation of definition or condition, and a check should verify that the claimed mechanism actually predicts that change.

**Prefer validated tool calls over agent-authored bookkeeping code, especially for coordinate/topology handling.** MDArena found that agents preferred writing their own scripts over reusing established libraries like MDAnalysis, and one such script silently mismatched residue-numbering conventions between file formats, corrupting the topology-coordinate correspondence (Anand, Hsu, Biggin, arXiv:2608.02642). For Dynamics Atlas this argues for a hard rule: any bookkeeping operation with a known, validated tool (unit conversion, PBC unwrapping, residue renumbering) must go through that tool, not a freshly generated script, and deviations should require an explicit justification the agent can be asked to defend.

**Do not let a single pass judge itself; use per-stage diagnostics and, where feasible, adversarial cross-checking.** MDForge's PRISM architecture (per-stage diagnostics plus a three-way specialist debate with reputation weighting) took mid-pipeline crash and false-convergence rates from 51% to 0% and recovered 78-82% of expert-level ranking utility on a held-out case (Wang et al., arXiv:2606.12916); ChemCrow separately found that GPT-4 used as its own evaluator could not reliably tell its own wrong answers from ChemCrow's good ones (Bran et al., arXiv:2304.05376). Together these argue against relying on the same model instance to both produce and certify an ensemble judgment, and for structuring the claim-ceiling decision as at least two independently-prompted checks rather than one narrative pass.

**Treat "task completed" as a claim to be verified against an explicit output checklist, not a status the agent can self-report.** MDArena documents agents declaring success while omitting required output files (.itp topology includes) or silently substituting a partial operation (transferring only crystal-water oxygens) for the full one (Anand, Hsu, Biggin, arXiv:2608.02642); MDGym separately documents agents abandoning tasks rather than iterating through a simulator error (Kumar et al., arXiv:2605.08941). For Dynamics Atlas, this argues for a fixed, per-task-type output manifest that is checked mechanically (file exists, required fields present, provenance recorded) before the agent's own "done" statement is trusted, independent of whether the analysis itself is judged correct.

## RIS export block

```ris
TY  - JOUR
AU  - Campbell, Quintina
AU  - Cox, Sam
AU  - Medina, Jorge
AU  - Watterson, Brittany
AU  - White, Andrew D.
TI  - MDCrow: Automating Molecular Dynamics Workflows with Large Language Models
PY  - 2025
DA  - 2025/02/13
JO  - Machine Learning: Science and Technology
DO  - 10.1088/2632-2153/ae4b07
UR  - https://arxiv.org/abs/2502.09565
ER  -

TY  - JOUR
AU  - Kumar, Vinay
AU  - Rajput, Satyendra
AU  - Mausam
AU  - Krishnan, N. M. Anoop
TI  - MDGYM: Benchmarking AI Agents on Molecular Simulations
PY  - 2026
DA  - 2026/05/09
JO  - arXiv preprint arXiv:2605.08941
UR  - https://arxiv.org/abs/2605.08941
ER  -

TY  - JOUR
AU  - Anand, Nithishwer Mouroug
AU  - Hsu, Wei-Tse
AU  - Biggin, Philip C.
TI  - MDArena: Evaluating Coding Agents on Realistic Molecular Dynamics Workflows
PY  - 2026
DA  - 2026/07/31
JO  - arXiv preprint arXiv:2608.02642
UR  - https://arxiv.org/abs/2608.02642
ER  -

TY  - JOUR
AU  - Bhakat, Soumendranath
TI  - Benchmarking generative AI and physics based molecular simulation for sampling conformational heterogeneity in T4 Lysozyme
PY  - 2026
DA  - 2026/05/13
JO  - bioRxiv
DO  - 10.64898/2026.05.10.724101
UR  - https://www.biorxiv.org/content/10.64898/2026.05.10.724101v1
ER  -

TY  - JOUR
AU  - Xu, Yaxin
AU  - Zhou, Yue
AU  - Zhao, Tianyu
AU  - An, Fengwei
AU  - Ren, Zhixiang
TI  - The limits of bio-molecular modeling with large language models: a cross-scale evaluation
PY  - 2026
DA  - 2026/04/03
JO  - arXiv preprint arXiv:2604.03361
UR  - https://arxiv.org/abs/2604.03361
ER  -

TY  - JOUR
AU  - Guilbert, Salome
AU  - Masschelein, Cassandra
AU  - Goumaz, Jeremy
AU  - Naida, Bohdan
AU  - Schwaller, Philippe
TI  - DynaMate: An Autonomous Agent for Protein-Ligand Molecular Dynamics Simulations
PY  - 2025
DA  - 2025/12/10
JO  - arXiv preprint arXiv:2512.10034
UR  - https://arxiv.org/abs/2512.10034
ER  -

TY  - JOUR
AU  - Wang, Zehong
AU  - Ma, Yijun
AU  - Schmidt, Connor R.
AU  - Ma, Tianyi
AU  - Sun, Weixiang
AU  - Li, Ziming
AU  - Guo, Xiaoguang
AU  - Zhang, Chuxu
AU  - Webber, Matthew J.
AU  - Ye, Yanfang
TI  - MDForge: Agentic Molecular Dynamics Pipeline Design under Sparse Simulator Feedback
PY  - 2026
DA  - 2026/06/11
JO  - arXiv preprint arXiv:2606.12916
UR  - https://arxiv.org/abs/2606.12916
ER  -

TY  - JOUR
AU  - Chandrasekhar, Achuth
AU  - Barati Farimani, Amir
TI  - NAMD-Agent: Automating MD simulations for Proteins using Large Language Models
PY  - 2025
DA  - 2025/07/10
JO  - arXiv preprint arXiv:2507.07887
UR  - https://arxiv.org/abs/2507.07887
ER  -

TY  - JOUR
AU  - Petkovic, Marko
AU  - Menkovski, Vlado
AU  - Calero, Sofia
TI  - Towards Fully Automated Molecular Simulations: Multi-Agent Framework for Simulation Setup and Force Field Extraction
PY  - 2025
DA  - 2025/09/12
JO  - arXiv preprint arXiv:2509.10210
UR  - https://arxiv.org/abs/2509.10210
ER  -

TY  - JOUR
AU  - Park, Yutack
AU  - Chung, Yeonwoo
AU  - You, Jinmu
AU  - Kim, Jisu
AU  - Ju, Suyeon
AU  - Han, Seungwu
TI  - A Robust Agentic Framework for Expert-Level Automation of Atomistic Simulations
PY  - 2026
DA  - 2026/06/08
JO  - arXiv preprint arXiv:2606.09422
UR  - https://arxiv.org/abs/2606.09422
ER  -

TY  - JOUR
AU  - Mitchener, Ludovico
AU  - Laurent, Jon M.
AU  - Andonian, Alex
AU  - Tenmann, Benjamin
AU  - Narayanan, Siddharth
AU  - Wellawatte, Geemi P.
AU  - White, Andrew
AU  - Sani, Lorenzo
AU  - Rodriques, Samuel G.
TI  - BixBench: a Comprehensive Benchmark for LLM-based Agents in Computational Biology
PY  - 2025
DA  - 2025/02/28
JO  - arXiv preprint arXiv:2503.00096
UR  - https://arxiv.org/abs/2503.00096
ER  -

TY  - JOUR
AU  - Zou, Yunheng
AU  - Cheng, Austin H.
AU  - Aldossary, Abdulrahman
AU  - Bai, Jiaru
AU  - Leong, Shi Xuan
AU  - Campos-Gonzalez-Angulo, Jorge Arturo
AU  - Choi, Changhyeok
AU  - Ser, Cher Tian
AU  - Tom, Gary
AU  - Wang, Andrew
AU  - Zhang, Zijian
AU  - Yakavets, Ilya
AU  - Hao, Han
AU  - Crebolder, Chris
AU  - Bernales, Varinia
AU  - Aspuru-Guzik, Alan
TI  - El Agente: An Autonomous Agent for Quantum Chemistry
PY  - 2025
DA  - 2025/05/05
JO  - Matter
DO  - 10.1016/j.matt.2025.102399
UR  - https://arxiv.org/abs/2505.02484
ER  -

TY  - JOUR
AU  - Mohammadzadeh, Saeed
AU  - Hamdi, Erfan
AU  - Shor, Joel
AU  - Lejeune, Emma
TI  - FEM-Bench: A Structured Scientific Reasoning Benchmark for Evaluating Code-Generating LLMs
PY  - 2025
DA  - 2025/12/01
JO  - arXiv preprint arXiv:2512.20732
UR  - https://arxiv.org/abs/2512.20732
ER  -

TY  - JOUR
AU  - Rawat, Shivam
AU  - Flek, Lucie
TI  - Plausible but Wrong: A case study on Agentic Failures in Astrophysical Workflows
PY  - 2026
DA  - 2026/04/28
JO  - arXiv preprint arXiv:2604.25345
UR  - https://arxiv.org/abs/2604.25345
ER  -

TY  - JOUR
AU  - Eulig, Steven Young
TI  - Position: Correct Answer, Wrong Mechanism -- When AI Scientists Defend General Claims Their Own Data Contradicts
PY  - 2026
DA  - 2026/06/22
JO  - arXiv preprint arXiv:2606.23175
UR  - https://arxiv.org/abs/2606.23175
ER  -

TY  - JOUR
AU  - Bran, Andres M.
AU  - Cox, Sam
AU  - Schilter, Oliver
AU  - Baldassari, Carlo
AU  - White, Andrew D.
AU  - Schwaller, Philippe
TI  - Augmenting large-language models with chemistry tools
PY  - 2024
JO  - Nature Machine Intelligence
DO  - 10.1038/s42256-024-00832-8
UR  - https://arxiv.org/abs/2304.05376
ER  -

TY  - JOUR
AU  - Boiko, Daniil A.
AU  - MacKnight, Robert
AU  - Kline, Ben
AU  - Gomes, Gabe
TI  - Autonomous chemical research with large language models
PY  - 2023
JO  - Nature
VL  - 624
SP  - 570
EP  - 578
DO  - 10.1038/s41586-023-06792-0
UR  - https://www.nature.com/articles/s41586-023-06792-0
ER  -
```
