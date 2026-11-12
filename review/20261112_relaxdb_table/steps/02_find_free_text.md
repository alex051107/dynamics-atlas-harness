# 找免费合法全文

**谁判断：** 程序　**标准：** 固定　**状态：** 已完成

**规则：** 封存条目拒绝；一次只发一个请求，站点之间有间隔；任何拦截都停手，不绕过。

## 做什么
对每篇源论文依次查 Europe PMC、PMC、预印本服务器，只取免费合法的版本。不登录、不用代理、遇到 403 或验证页面就停掉那个站点。

## 怎么重跑
`python3 scripts/relaxdb_evidence_table/source_fulltext.py run`

## 输入和输出
- 输入：source_papers.csv
- 输出：source_texts/results.json、source_text_status.csv、staging/

## 已知限制
99 篇缺全文的源论文里，这一步直接拿到 11 篇。PMC 作者稿的补充材料不提供，要人工下载。
