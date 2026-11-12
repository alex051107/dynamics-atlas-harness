# 核对身份

**谁判断：** 程序　**标准：** 固定　**状态：** 已完成

**规则：** 只有通过身份核对的文件才算全文（PASS）。自动检查拒掉、但文件里确有该 DOI 且只因版面检查失败的，记作 PASS_OWNER_FILE；这类放行的理由写在 manual_accept.json。

## 做什么
每个放进 drop 的 PDF，程序先在前两页找它的 DOI；找不到就拿标题和论文标题比对（95% 以上才算）。然后检查正文是否够长、有没有被换成别的论文。

## 怎么重跑
`python3 scripts/relaxdb_evidence_table/source_fulltext.py drop`

## 输入和输出
- 输入：drop/ 里的 PDF、spine 的论文清单
- 输出：source_texts/source_text_status.csv（每篇一行：通过哪种方式、原因）

## 已知限制
99 篇里目前 64 篇有可用全文。有 1 个文件身份没确认，1 个正文太短。
