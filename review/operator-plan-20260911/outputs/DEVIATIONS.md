# 执行偏差与未完成项

## 1. 运行器修复与重开

首次冻结发生在第一次模型调用之前，随后为处理运行器失败建立了 `FREEZE_ATTEMPT_REV2.json` 到 `FREEZE_ATTEMPT_REV5.json`，最终使用 `FREEZE.json` revision 6。失败 pilot 保留在原目录，未把成功 slot 为了好看重跑。失败类型包括 HSP90 O-arm 的 `TOKEN_LIMIT` 和 ADK D/O-arm 的 `RESOURCE_LIMIT`；`FREEZE.json` 的 `reopened_after_runner_failure.prior_pilot_attempts` 是审计记录。

这使 16 个成功答复跨越了已记录的运行器修复版本，而不是单一运行器 revision 的同版比较。初始冻结-before-first-call 条件满足；跨 revision 的影响保留为方法学限制，不被改写为同版严格比较。

## 2. 主张绑定兼容性修复

真实答复中出现了 `type` 代替 `origin`、`result_id` 单数和 `result_ids` 复数两种写法。运行器 gate 增加了兼容解析，并保持 current-calculation 必须绑定实际结果文件的规则。修复后未重跑已成功 slot；揭盲后的 alias-to-result-file 检查对 8 个 O-arm 答案全部通过。早期回执中的 0 unbound 不能单独作为科学正确性证据。

## 3. D-arm 软锁与答案不完整

D-arm 没有 operator 工具，且加入了 16 次工具调用的有界软锁，以避免反复读源和 token/resource 失败。所有 8 个 D-arm receipts 最终为 `COMPLETE`，但部分答复只报告限制、没有题目要求的数值。盲评分按内容实际给分；`COMPLETE` 仅表示运行器回执完成，不表示答案正确或完整。

## 4. 第二评分人缺失

计划要求 PM 或 Claude 进行第二份独立盲评分。本次在当前 Codex-only 执行中没有可用或已授权的第二评分人，因此未生成第二评分表，也未生成 agreement rate 或 fabricated disagreement count。第一评分表在 `outputs/blind/SCORE_SEAL.json` 中先封存，之后才读取私钥并揭盲；这一顺序的第二评分人条件未完成，作为明确限制交付。

## 5. 外部 PR 未创建

计划要求推送 `review/operator-plan-20260911` 草稿 PR。仓库 preflight 显示 `dynamics-atlas-harness` 的机器可读 live status 当前仍把下一允许动作限定为 named human domain source-science review，且 `automatic_code_changes` 为 false；仓库分支政策只列出 `codex/*`、`feature/*` 和 `fix/*`。为遵守该控制面，没有创建分支、没有写入该仓库、没有推送或创建 PR。十节 PR 正文保存在 `outputs/PR_DRAFT.md`，算子包保存在本任务目录，等待 live status/人工批准后再转移。

## 6. 人工时间未仪器化

计划要求记录写卡、写评分依据和事后核对三项人工时间。本任务没有单独计时器，也没有可将 wall-clock 转换为人工小时的可靠记录；报告明确写为“未单独计时”，不估算具体小时数。

## 7. 未做事项

- 未下载新的科学数据，未新建 MD，未启动 GPU/集群任务，未安装依赖。
- 未修改旧实验目录、33 条原始规则或任何 `main`。
- 未把 F/D/O 结果升级为平衡、速率、机制、新状态、独立实验验证、泛化或 production claim。
- 未修改揭盲后的第一评分表。

