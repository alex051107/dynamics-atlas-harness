# Soojung Meeting 8.24：共识、提议与待确认项

## 一句话结论

这次会议确认的下一步不是扩大 Rules Table，也不是先做一个通用 Agent 平台。双方认可的路线是：保留可追溯的规则层，冻结已经存在的分析方法，用一个最小 prototype 展示系统能做什么，再让 Alex／Soojung 和具体 domain experts 分两层审查并迭代。

## 已形成的共同方向

| 共同方向 | 会议证据 | 对研究方案的影响 |
|---|---|---|
| Rules Table 应服务于具体科学问题和 heterogeneous data comparison | Alex 在 03:20–13:41 解释完整设想；Soojung 在 13:41–14:03 表示总体认可 | Rules Table 是 review-planning 与 routing 层，不是论文摘要集合 |
| 规则、分析方法和工具权限要预先冻结 | Alex 在 09:08–10:38 主张 rule-specific tools；Soojung 在 14:03–14:55 认可 established Python packages／frozen skills | Agent 不自由发明分析 pipeline，只能提出 profile、evidence lookup 或已登记 operator request |
| 用现成包，不重复开发科学分析工具 | 14:12–14:55，Soojung 以 MD 和 NMR packages 为例 | Prototype 优先复用现有 HSP90 harness、MDAnalysis 或专家维护包；新算法不在 V2 范围 |
| 新规则需要人和 domain expert 迭代 | 14:55–16:50 | Alex／Soojung 做第一层过滤；实验／模拟专家做第二层过滤；每轮 prototype 暴露具体问题 |
| 先给专家看 minimum prototype | 15:35–16:50 | 交付标准是可理解、可批评、可定位错误，不是一次覆盖全部方法 |
| HSP90 是合适的第一案例 | 15:55–16:20 和 25:49–30:10 | V2 以已暴露的 HSP90 NMR–MD capsule 为主，不包装成 held-out test |
| Prototype 不需要一开始又广又深 | 28:14–28:37 | DHFR 和 ADK 放入 expansion queue；先完成 HSP90 端到端 contract |
| 系统问题具有跨领域价值 | 20:56–21:57 | 可把 generalization 写成长期研究意义，不能变成 V2 的当前验收范围 |
| Private repository 可以先邀请协作者，不必立即公开 | 30:10–30:32 | 公开发布不是 prototype 的前置条件；本任务也不执行邀请或公开操作 |

## Alex 提出的研究设想

这些想法有研究价值，但会议没有把它们全部冻结成第一版验收标准。

| 设想 | 时间 | 当前处理 |
|---|---|---|
| 用一到两篇大综述把 protein dynamics 拆成多个阶段，再为每一阶段寻找 primary／cross-domain papers | 04:47–05:51 | 已与 review-led 七层框架一致，保留为 rule-development 方法 |
| 低成本 Agent 帮助收集或整理 candidate rules | 10:44–13:41 | 可作为 authoring assistant；每条规则仍需 source locator、去重、boundary fixture 和 human freeze |
| 用 80–85% coverage 作为停止点 | 16:51–18:14 | 不采用为正式阈值，因为 denominator 未定义；改为 expert-reviewed empirical saturation |
| 建立 Agent harness／benchmark，研究没有完整输出 oracle 时的 semantic error | 18:14–20:56 | 保留为后续独立研究问题；不进入 V2 prototype 的必须功能 |
| 一到两周测试 10–20 cases | 24:26–26:29 | 后移。先完成一个 HSP90 V2 和一个后续 system 的重复性检查，再决定是否扩展 |
| 连接现有分析 tools，返回更快的进一步分析 | 25:18–25:49 | V2b 最多连接一个已存在、只读、固定输入输出的 operator |

## Soojung 给出的关键修正

1. Rule saturation 不能只靠开发者自己判断。需要持续找 domain experts 讨论哪些检查真正有用。
2. Expert feedback 需要看得见的 prototype，不能只讨论 architecture。
3. Prototype 先做最小版本，逐步扩展；HSP90、E. coli DHFR 和 ADK 是候选系统，不要求同时完成。
4. Established packages 应被封装为 frozen skills／operators，Agent 不应该现场生成新的分析流程。
5. Collaboration、repository sharing 和 FutureHouse／Stephanie／NMR expert 参与可以帮助扩大项目，但它们是协作安排，不是当前科学结果。

## 尚未真正确定的事项

| Open question | 为什么还不能写死 | 建议的决策点 |
|---|---|---|
| 第一位正式审查 Rules Table 的 domain expert 是谁 | Stephanie、Gina 和其他 experts 都被提到，但没有确认具体 review assignment | V2 review packet 完成后，由 Soojung 指定第一位 reviewer |
| 第一个 registered operator 是哪个 | 会议举了 MDAnalysis／NMR package 例子，没有指定 exact function、input 或 output | 先看 HSP90 selected obligation，再选择一项已存在分析 |
| 何时停止加规则 | 80–85% 是 Alex 的讨论性建议；Soojung强调迭代与 expert feedback | 使用下文的 empirical saturation gate |
| 第二个系统选 DHFR 还是 ADK | 两者只被列为候选，数据可用性尚未核对 | HSP90 V2 通过后做一次只读 data/source inventory |
| 下一次 meeting 的确切日期 | 结尾只讨论 next week／one or two weeks，没有冻结日期 | 单独协调，不从录音推断日程 |

## 双方行动项

### Alex

- 整理现有 scripts 与 Rules Table prototype，形成一条可运行、可解释的 V2 路径。
- 保留 private repository；如需邀请 Soojung，先核对 repository 与权限范围后再执行。
- 以 HSP90 为第一 prototype case，明确 question、inputs、selected rules、unresolved evidence、allowed claim 和 next step。
- 在需要新规则之前先定位是 method profile、binding、predicate、evidence 还是 operator 问题。

### Soojung

- 与 FutureHouse、Stephanie 和其他 domain experts 沟通项目与后续合作可能。
- 帮助确认 prototype 应向哪位 domain expert 展示，以及什么输出对实验者有用。
- 提供或核对可能用于 NMR analysis 的 established package 与适用边界。

