# dynamics-atlas-harness

这是 Dynamics Atlas 的最小 profile/operator bridge。它验证两个接口。模型或 recorded provider 提出的 case profile 必须先通过确定性 admission；selector 已选出的一个 `ReviewObligation` 才能请求已登记的只读 operator。

当前代码只使用 Python 标准库。它没有复制或修改冻结的 33-row Rules Registry、17-binding v0.3 package、compiler 或 selector。测试中的 selector output 是明确标记的 exposed synthetic deterministic fixture。

## 当前数据流

```text
CaseProfileProposal
  -> profile admission
  -> recorded deterministic selector output
  -> one ReviewObligation
  -> ProposalProvider
  -> deterministic operator authorization
  -> OperatorRunReceipt + EvidenceResult
  -> HUMAN_REVIEW_REQUIRED
```

`ProposalProvider` 当前由 `RecordedProposalProvider` 实现。`subagent_resolution_proposal.json` 保存了一次只看单个 synthetic obligation 与 operator summary 的 Codex subagent 输出；它仍要经过同一确定性 validator。未来廉价模型只需要产生相同的 `resolution-proposal/v0.1`，不会获得 rule selection 或 operator authorization 权限。

method-profile approval 不能由 CLI 调用者自由声明。`config/method_profiles.json` 是当前版本化 registry；它现在为空，所以所有 `MD_TRAJECTORY` proposal 都会停在 `NEEDS_METHOD_PROFILE`。将来只有带 reviewer、approval time 和 source artifact 的 `HUMAN_APPROVED` profile 才能进入 admission allowlist。

首版 CLI 固定读取 repo 内的 `config/operators.json`、`config/method_profiles.json` 和 `tests/fixtures` allowed root。调用者不能用命令行替换 allowlist 或扩大文件根。以后接入真实 case 时，应由受信 orchestrator 绑定新的版本化 registry 和 case-owned input root，而不是把这些值重新开放成模型参数。

## Operators

`evidence.json_pointer_lookup.v1` 是 fixture-only 的只读 canary。它只能读取显式 `allowed_root` 下的 JSON，不能越界，不做科学计算，也不输出科学 verdict。

`trajectory.structural_state_projection.v1` 只是 `CANARY_BLOCKED` design proposal。MDAnalysis 被记录为 backend candidate；依赖、输入 fixture、method profile、metric、参数和 scientific scope 都没有冻结，因此代码不会导入或运行它。

## 本地运行

从 repo 根目录运行下面的命令。

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

下面是暴露 fixture 的 CLI 示例。

```bash
PYTHONPATH=src python3 -m dynamics_atlas_harness run-fixture \
  --profile-proposal tests/fixtures/case_profile_valid.json \
  --selector-output tests/fixtures/recorded_selector_output.json \
  --resolution-proposal tests/fixtures/subagent_resolution_proposal.json \
  --output-dir /tmp/dynamics-atlas-harness-fixture
```

成功只表示 contract path 和 receipt behavior 按 fixture 运行。它不证明 Rules 完整、operator 科学有效、HSP90/ADK 结果正确、跨论文 transfer、Agent 增量价值或 production readiness。

## 明确不做

- 不安装依赖，不运行 MDAnalysis、MDTraj、GROMACS 或数值科学 payload；
- 不提供任意 shell、任意 Python、网络、MCP 或路径访问；
- 不建设 DAG、SQLite、LangGraph、FastAPI、WebUI、RAG、swarm 或事务平台；
- 不输出 `SUPPORT`、`CANNOT_SUPPORT` 或最终科学结论。

项目级实时状态仍在上游 workspace 的 `autoresearch/DYNAMICS_ATLAS_STATUS.md`。这个 repo 的 README 只描述代码边界。
