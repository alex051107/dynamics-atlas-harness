# Q01：现有资料可用，原入口在规则运行前拒收

当前新问题没有进入 Rules。现行 run-case 只接收已登记开发案例，对 Q01 返回 CASE_NOT_IN_EXPOSED_DEVELOPMENT_REGISTRY；保留命令和完整输出。不能把接入拒收计作规则漏判，也没有新增科学答案。

本地已有 40 条轨迹的 Cα 坐标，各 1021 帧、213 个残基；另有 NMR 参照和逐帧距离序列。此次只核 NPZ 文件/数组头，未重算轨迹、重复校验历史哈希或下载数据。完整列表见 source_inventory.json。

现有 HSP90 Operator 精确绑定旧开发案例，以已有帧状态/路线表输出时间分块描述；它没有自动覆盖这个新问题。不能换用旧 case_id 冒充 Q01 接入。

方法事实另有明确差距：论文以各接触在 NMR bundle 中的均值加两倍标准差定义距离阈值；存档 Violation.zsh 没有传 -ref，实际分支使用 ITP up1。当前读取 ITP 记录证实 open 19 个接触均 10 Å，closed 5 个均 8.5 Å。这要求保留两种方法的语义，尚不能据此认定论文原运行执行了哪一种。

历史终末 120 帧路线分类与全程稳定性不是同一个统计量；已有闭合/开放路线重构和图中分类均留在复核侧，不写入下一轮 Rules 的目标输入。20 条 open-seeded 与 20 条 closed-seeded 的独立轨迹是比较单位，连续帧不是独立重复；不能升级为平衡人口、速率、自由能或功能活性。

来源：hsp90_acquisition_20260725 的 NPZ 和 data/contract/MD/Tools/VIOLATION；hsp90_paper_comparison_20260729/outputs/HSP90_PAPER_ATLAS_CLAIM_COMPARISON.md；已读原文文本 tmp/pdfs/henot_2022_article.txt 和 SI。原资料保持不变。

下一步：新增明确 Q01 事实适配，复用现行通用 admission/projector 和未改动的 Draft Rules，保存原始方法事实及实际规则反应，再设计真正由义务控制的补算。该适配必须标为新入口，不改写本次拒收结果。

验证：预检 1 次格式失败（小于号被当作占位符）后修复并 PASS；现行入口实际尝试 1 次；源/方法核查及产物断言各 1 类。零优化、零新哈希、零下载/安装、零新测试套件，Pro13仍在生成，不重复发问。
