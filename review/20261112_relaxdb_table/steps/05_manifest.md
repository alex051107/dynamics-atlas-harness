# 列出要读的论文

**谁判断：** 程序　**标准：** 固定　**状态：** 已完成

**规则：** 只收通过身份核对的；封存条目不进清单；已有读论文文件夹的不重复。

## 做什么
把通过身份核对、还没有读过的论文列成清单：正文的文本文件、补充材料的文件、蛋白登记卡（温度、pH、磁场、BMRB 编号）。每 5 篇一批。

## 怎么重跑
`python3 scripts/relaxdb_evidence_table/build_manifest.py OUT.json`

## 输入和输出
- 输入：source_text_status.csv、results.json、drop/
- 输出：source_read/manifest*.json

## 已知限制
再运行一次现在给出 0 篇待读。
