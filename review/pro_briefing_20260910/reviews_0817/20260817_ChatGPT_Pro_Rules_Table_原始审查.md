---
title: ChatGPT Pro 对 Rules Table 与两层验证方案的原始审查
retrieved_at: 2026-08-17T10:51:25.891Z
source_url: https://chatgpt.com/g/g-p-6a3c8b377c5c8191b8a11c68c79cb45b-protein-data/c/6a82dfd3-2a68-83ea-87ca-10c10156de5d
source_role: external_methodology_review
scientific_authority: false
review_status: complete
---

# ChatGPT Pro 对 Rules Table 与两层验证方案的原始审查

> 这份文件保存外部审查的原文。它是方法学意见，不是论文证据、专家共识或科学事实。文中的 ChatGPT 文件引用标记只在原对话上下文中有效，项目采纳决定见同目录的独立裁决文件。

## 1. 总判定

**简化后继续。** 保留 source-linked candidate registry、逐来源 metadata、abstention 与 claim ceiling 的科学骨架；停止把当前 20 栏表、扁平 selector 或 metadata-only 输出当作科学决策器。下一轮只验证一个直接读取 source/edge 的 **review-obligation selector**，并把论文事实或 operator 结果交给独立 evaluator。若一次限定修复后仍不能完整定位关键 obligations，应停止当前 runtime representation，但保留 Rules Table 作为审计账本。现有 baseline 是“安全但未通过”，不是路线已经验证。fileciteturn2file1

## 2. 十项主张审查表

| # | 判定 | 最短理由 | 包内证据 | 最关键反证测试 |
|---|---|---|---|---|
| 1 | **VERIFIED** | 问题的基本单位应是“来源能否发现并支持当前 claim”，而不是把异质来源压成统一距离或总分。 | Stephanie 明确把 event timescale、feature length scale、observable 与 observation window 联系起来，也没有指定 universal metric。fileciteturn3file4 | 对同一组数据分别请求 state、population 与 kinetics claim；若所需检查和 claim ceiling 不随 claim 改变，则该设计失败。 |
| 2 | **VERIFIED** | 20 栏同时混入论文事实、项目解释、选择线索和运行时停止语义；适合作为有来源的候选规则档案，不适合作为直接执行表。 | `paper_title`、全局状态重复，而 `integration_operator`、`validation_route` 又高度自由文本化。fileciteturn3file7 fileciteturn3file15 | 不增加硬编码映射，直接把 20 栏编译为确定性 predicates；若可跨论文稳定运行并保持 provenance，才可推翻。 |
| 3 | **WRONG** | 三种职责需要保留，但不需要三个独立权威层。selector index 应是 registry 的版本化派生视图；“case-local compiled package”还必须拆成 obligation output 与 evidence-evaluation output。 | 当前规则未编译，Gate 又独立硬编码；把所有运行结果塞进一个 package 会继续混淆检索与科学判断。fileciteturn1file11 | 用“两份 source of truth＋派生 index＋两阶段 run receipt”实现相同 trace；若必然丢失停止依据，才恢复三层权威模型。 |
| 4 | **VERIFIED** | 多来源判断必须保留 node 与 edge：一个来源缺 uncertainty，不等于所有来源都缺；一个 edge 缺 bridge，也不等于所有比较都不可行。 | 旧输入只有一个 locator 和三个 case-level Boolean；新 contract 已显式分为 `case`、`evidence_items`、`comparisons`。fileciteturn2file11 fileciteturn2file3 | 构造三来源案例，其中仅一条 comparison 缺 bridge、另一来源发生 role leakage；若扁平表示能分别定位两者，则可压缩。 |
| 5 | **VERIFIED** | alias 命中依赖措辞，top-8 又把展示限制变成科学截断；它们只能形成诊断 baseline。 | X-EISD 漏掉 identifiability obligation，PRE 漏掉 validation-discriminability obligation。fileciteturn2file5 | 对 modalities 做同义词替换、输入排序和无关文本增删；必要 obligations 必须保持不变。 |
| 6 | **WRONG** | 预先冻结 answer-blind reference 是正确的，但比较范围必须分阶段。metadata selector 可验证 obligations、trace 和输入缺口；不能被要求复现依赖论文 observed results 的 terminal route 或最终 next action。 | PRE 的 omitted-label 数据是否能区分 ensemble sizes 是论文观察结果，不能从 method、role 和 bridge metadata 推导。fileciteturn2file1 | 给 selector 完全相同的 metadata、但提供两组相反的 source-fact results；若它仍输出同一科学 route，说明 stage contract 错误。 |
| 7 | **VERIFIED** | 两案足以否定当前 flat selector，并决定是否值得进行一次受限修复；不足以证明 coverage、transfer 或 general validity。 | 两案互补暴露了 lineage、identifiability、left-out role 和 discriminability 缺口，但均为 exposed development。fileciteturn2file14 fileciteturn2file9 | 一次最小修复后，若仍需 case-specific branch、reference access 或第二轮同根因 patch，应停止该表示。 |
| 8 | **VERIFIED** | review/best-practice 适合检查 taxonomy；具体规则、负结果和结论边界仍必须由 primary paper 定位。这样可避免逐篇 primary paper 无边界扩张。 | Thomasen 与 Grossfield 被正确限定为 coverage sources，不计入 selector pass rate。fileciteturn3file6 | 预登记一组新的 primary papers；若持续出现 review 未覆盖的高频 `MUST_HAVE_GAP`，再调整 review-first 顺序。 |
| 9 | **VERIFIED** | 当前接口仍在变化，拆成四五个 Skills 会把尚未稳定的错误边界固化。应先使用执行配方，稳定后仅建立一个 orchestration Skill。 | 包内已经明确现有 search、downloader、PaperForge、AutoResearch、Human Writing 的职责。fileciteturn3file18 | 两次完整流程若反复出现独立、稳定、可复用的子任务接口，再考虑独立 Skill。 |
| 10 | **VERIFIED** | “补 uncertainty”只是缺口类别，不是行动建议。practical guidance 必须绑定 target source/edge、observable 或 validation role，并说明新增证据将区分哪些解释。 | baseline 已显示当前 guidance 无法稳定指向具体 source、edge 或辨别实验。fileciteturn3file13 | 删除任一 source 或 edge 后，建议必须随之改变；若仍输出同一句通用建议，则不合格。 |

## 3. Rules Table 最小表示

### 已达到与尚未达到的原始目的

当前字段已经覆盖：来源定位、paper finding 与项目解释分界、native observable/estimand、时间和空间语义、不确定性、forward bridge、evidence role、验证要求、停止路线、transfer scope 和结论上限。这些内容与“先判断能否观察，再判断能说到哪里”的原始顺序基本一致。fileciteturn1file9

仍停留在文档意图、尚未进入可执行表示的内容包括：

- 目标事件相对于每个来源的 observability；
- per-source sampling adequacy，尤其是 MD 的 replicate、autocorrelation 与 effective sample size；
- candidate-pool lineage 与 prior-data reuse；
- validation 是否真的能区分 competing models；
- source-fact/operator result；
- case-specific evidence relation、scientific stop、claim ceiling 与 next discriminating action；
- 规则是否真正读取了相关字段，而不仅是被检索出来。

### Observability 最小字段

不能增加一个 `has_observability=true/false` Boolean。最小安全表示是：

```text
case.observability_target
  event_signature
  target_time_scale
  target_spatial_scale

evidence_item.detection_boundary
  status: DOCUMENTED | PARTIAL | MISSING | NOT_APPLICABLE
  sampling_or_sensitivity_basis
  source_locator
```

现有 `observation_window`、`spatial_support` 和 `uncertainty` 可继续使用。`OBSERVABILITY_ADEQUATE / INADEQUATE / UNKNOWN` 应由 evaluator 计算，不能由提交者预填，否则会把结论写进输入。总时长或帧数本身也不能充当 sampling adequacy；Grossfield 等将 sampling quality 与统计不确定性、相关性和具体 observable 联系起来，而不处理 force-field systematic error。citeturn391089search3

### `intended_relation` 的安全语义

旧 `intended_relation` 会直接泄露 `COMPLEMENTARY`、`NOT_COMPARABLE` 等答案，删除是正确的。fileciteturn1file15 最安全的输入仅保留：

```text
left_source_id
right_source_id
shared_claim
comparison_question
bridge_name/status/assumptions
```

其中 `comparison_question` 必须是中性的，例如：“在给定构建体、条件和 bridge 下，这两个来源对 shared claim 支持何种证据关系？”关系枚举只能出现在 evaluator 输出中。`evidence_role` 可以作为输入，但必须是运行前由 Methods/实验设计支持的事实，不能根据结果好坏事后标注为 validation。

### 当前 20 栏的归属

| 类别 | 当前栏目逐项归属与处理 |
|---|---|
| **1. paper fact / provenance** | `rule_id` 保留；`paper_id` 保留；`paper_title` 移入 paper registry；`source_locator` 保留；`source_classification`→`source_inference_level`；`paper_finding`→`source_finding`；`rule_class` 中描述论文语境的部分拆为 `source_rule_class`。 |
| **2. project-derived candidate rule** | `required_fields`→结构化 requirements；`integration_operator`→`operator_family + guidance`；`requires_numeric_threshold` 与 `acceptance_rule_status` 合并为结构化 `criterion_policy`，但不能压成单一 Boolean；`model_or_support_validation_required` 与 `validation_route` 合并为 `validation_obligation{required, mode, guidance}`；`abstain_route` 拆为 `specific_stop_code + stable_stop_category`；`transfer_scope` 保留。 |
| **3. selector tag** | `gate_primary`→`gate_hint`；`rule_class` 中用于检索的部分→`rule_family`。另由 sidecar 补充 `method_tags`、`source_category_tags`、`evidence_role_tags`、`relation_tags`、`failure_mode_tags`、`claim_scope`、`required_input_paths`。 |
| **4. case-local compiled decision** | 当前 20 栏中**没有任何栏目应归入此类**。运行时另存 target source/edge、obligation status、input path、source fact、relation result、stop category、claim ceiling、forbidden upgrade、next action 与 trace。 |
| **5. reader-facing display only** | `gate_path_semantics` 移入全局 Gate protocol；`gate_path` 删除逐行重复，只保留特殊 override；`proposed_project_rule` 由结构化字段生成；`project_status` 移入 registry metadata；`paper_title` 通过 paper registry join 展示。 |

推荐表头为：

```text
papers:
paper_id | title | year | doi | citation

source_rules:
rule_id | paper_id | source_locator | source_finding |
source_inference_level | source_rule_class | rule_family |
requirements | operator_policy | criterion_policy |
validation_obligation | specific_stop_code |
stable_stop_category | transfer_scope | guidance_text

rule_index（派生、可重建）:
rule_id | method_tags | source_category_tags | evidence_role_tags |
relation_tags | failure_mode_tags | gate_hint |
claim_scope | required_input_paths
```

`rule_index` 不应成为新的科学事实来源；它必须可由同版本 registry 重建。

## 4. 当前 selector／SQLite 的最小修复边界

baseline 前保持 selector 不变是正确的，因为它保留了失败归因：projection、registry coverage 和 selection logic 没有被同时修改。fileciteturn2file13 baseline 后，typed sidecar **必要但不充分**。最小修复还必须做到：

1. selector 直接读取 `evidence_items` 与 `comparisons`，不再走 flat projection；
2. 输出的是 mandatory review obligations，而不是 terminal scientific route；
3. 每条 obligation 绑定 `CASE / SOURCE / EDGE` target 和具体 input path；
4. 已有规则全部检索后，再按 Gate 分组展示。

固定 top-8 应删除。后端必须返回全部 mandatory obligations；界面可以展示八张摘要卡，但要同时提供完整清单。展示容量不能参与科学召回。

当前阶段不应迁移 SQLite。使用 versioned JSON input、obligation output 和 run receipt 更小、更容易推翻。若后续获得持久化资格，最小关系结构不是四张表，而是：

```text
cases
evidence_items
comparisons
runs
obligations_or_selection_trace
```

`runs` 不能省略，否则不同 selector/registry 版本的结果可能互相覆盖，重现 McBride 已暴露的 result-identity 假阳性。fileciteturn2file16

继续延后：用户与权限、上传、公网服务、队列、并发 worker、通用 ontology、独立 bridge registry、通用 rule language/compiler、自动 claim 选择、Agent benchmark、云数据库和 production deployment。

## 5. 论文与 Skill 验证方案

四篇论文的角色划分合理：

- X-EISD 与 PRE 继续作为 **exposed development repair cases**，不能称 held-out。
- Thomasen 2022 与 Grossfield 2018 只做 taxonomy/coverage，不进入 pass rate。
- MESMER 暂停；当前两案已经暴露共享的 representation 与 stage-contract 缺陷，第三案只会重复证明同一问题。

外部交叉核验未改变包内定位：Lincoff et al., *Extended experimental inferential structure determination method in determining the structural ensembles of disordered protein states*（2020，DOI `10.1038/s42004-020-0323-0`）明确处理多类实验及 back-calculation uncertainty，并显示 representative candidate conformers 的重要性；Silvestre-Ryan et al., *Average Conformations Determined from PRE Data Provide High-Resolution Maps of Transient Tertiary Interactions in Disordered Proteins*（2013，DOI `10.1016/j.bpj.2013.02.019`）；Thomasen & Lindorff-Larsen（2022，DOI `10.1042/BST20210499`）；Grossfield et al.（2018，DOI `10.33011/livecoms.1.1.5067`）分别适合 primary-case、taxonomy 与 MD sampling 角色。citeturn391089search0turn551613search0turn391089search2turn391089search3

三个候选缺口应区别处理：

- **MD observability/sampling**：真实缺口，主要进入 method profile、observability target 和 per-trajectory evidence item，不应给 Rules Table 再加六个逐行栏目。
- **candidate-pool lineage**：先增加 `CANDIDATE_ENSEMBLE.support_lineage`，并细化现有 candidate-support/identifiability rule；只有来源支持一个独立、可转移 failure mode 时才新增 rule。
- **chemical-species heterogeneity**：目前为 `DATA_INSUFFICIENT`。综述足以触发 primary-source search，但不足以冻结通用 stop rule。

PRE 主文足以派生一条候选规则：

> validation evidence 只有在对预定义 competing models 具有 discriminability 时，才能支持 model selection；否则停止选择，但可保留 source-local consistency。

派生后，PRE 对该概念必须降为 derivation/development source，不能再算通过案例。X-EISD 若用于新增 pool-lineage requirement，同理。

实现上应复用现有 Skills，待流程稳定后只建立一个 orchestration Skill。其最小输入为 paper/source record、exposure role、claim contract、method-scope version、metadata-contract version、registry/index version、selector version 和 operator policy；输出为 Deep Read、frozen reference、answer-blind metadata、targeted obligations、evidence-evaluation receipt、semantic adjudication、failure class 与 run receipt。

合法失败状态至少包括：

```text
PARK_NO_COMPLETE_FULLTEXT
PARK_OPERATOR_REQUIRED
METHOD_UNREGISTERED
REFERENCE_LEAKAGE
INPUT_CONTRACT_GAP
RULE_COVERAGE_GAP
SELECTOR_GAP
EVIDENCE_FACT_MISSING
EVALUATOR_GAP
VALIDATION_NONDISCRIMINATING
UNSAFE_CLAIM_UPGRADE
```

不可越权边界：不得创造阈值、事后修改 reference、把 development 改称 held-out、从 metadata 推导论文 observed result、调用未登记 operator、让同一论文同时充当修规则来源和独立验证，也不得替代领域专家给出最终 biological claim。

## 6. 最短实验路线

| 步骤 | 输入 | 输出 | 失败条件 | 继续条件 |
|---|---|---|---|---|
| 1. 冻结两阶段合同 | v0.2 contract、registry、两份 reference | Stage-1 obligation schema；Stage-2 evidence schema | 两阶段仍共享 answer-bearing 字段 | paper facts、metadata、operator results 可清楚分离 |
| 2. 做最小修补 | observability target、support lineage、PRE discriminability locator | 一项字段细化、一项 candidate-rule refinement／addition、typed index | 需要无来源阈值或大量新 ontology | 所有改动均有 locator，且不含 case answer |
| 3. 构建 task-local selector | per-source contract＋typed index | 全量 source/edge obligations＋trace | 仍需 alias 搜索、top-k 或 case-specific branch | 无 reference access，输出不含 scientific terminal route |
| 4. 运行两案及反事实 | X-EISD/PRE、删除 lineage、role 置换、缺 bridge/uncertainty | obligation coverage 与字段依赖矩阵 | 任一 mandatory obligation 漏选或 target 错位 | case-local obligations 100% 覆盖 |
| 5. 做不变性测试 | 同义词、排序、无关文本扰动 | invariance receipt | 选择随措辞或顺序变化 | 只有科学字段变化才改变 obligations |
| 6. 冻结修复并重分类 | 修复版本和开发结果 | X-EISD/PRE 的 derivation/development lineage | 必须第二次修同一根因 | 一次修复后全部开发测试通过 |
| 7. 单篇 reserve transfer | 未参与字段／规则修订的 primary paper | transfer adjudication | operator 必需、重复同一 failure mode 或发生 unsafe upgrade | 通过后才考虑 SQLite 与 orchestration Skill |

可删除的步骤是：**要求 metadata-only selector 复现论文 terminal result**。必须提前的是两阶段 contract、source/edge binding 和 observability target。最模糊的停止点是“同一根因修一次仍失败”；应操作化为：一次修复后只要仍有 mandatory concept 漏选、target 错位、同义词敏感、case-specific branch、reference leakage 或 unsafe upgrade，即停止当前 runtime representation。

## 7. 最高风险的三个假阳性

1. **对所有案例安全地 ABSTAIN。** forbidden upgrade 为零，但系统没有定位 source/edge、没有区分缺失原因，也没有实际 utility。

2. **在 X-EISD/PRE 上达到 100% coverage。** 若 tags、rule wording 或 fixtures 直接来自这两份 reference，这只是 exposed-case overfitting，不能算 transfer。

3. **terminal route 与 reference 一致。** 若 route 由硬编码 Gate、adapter 或答案型 metadata 产生，或 selector 没有读取正确字段，即使最终答案一致也是假成功。fileciteturn2file10

## 8. 下一步优先级

1. **先冻结 obligation-selector／evidence-evaluator 边界。** 提前停止：无法把 observed result 从 metadata 中移出。

2. **实现直接读取 per-source/edge 的 typed selector，并移除科学层 top-8。** 提前停止：需要论文名、case ID 或专用 if/else 才能覆盖 obligations。

3. **只做两项有来源的修复：validation discriminability 与 candidate-support lineage；chemical heterogeneity 暂缓。** 提前停止：缺少 locator、与已有规则重复或需要新增通用 ontology。

4. **运行两案、反事实和 invariance batch。** 提前停止：一次修复后仍有任一关键 obligation 漏选、字段扰动不生效或无关文本改变结果。

5. **使用一篇未参与修复的 reserve primary paper 检查 transfer。** 提前停止：需要重跑原始 operator、没有新增 failure mode，或 reference 无法在运行前冻结。此前不迁移 SQLite、不建立新 Skill。

## 9. 仍需人类／领域专家决定的唯一事项

**针对每个真实 biological claim，确定合理的 competing explanations，以及在匹配构建体、条件、时间尺度和空间尺度下，哪一种正交 observable 或实验结果才具有足够 discriminability。** 工程系统可以强制来源追溯、字段完整性、停止与 claim ceiling，却不能仅凭 metadata 决定哪些生物学假设构成正确的竞争集合。
