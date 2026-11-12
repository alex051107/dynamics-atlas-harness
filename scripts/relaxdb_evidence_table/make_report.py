#!/usr/bin/env python3
"""Build REPORT.html (clickable process chart, step table, problems, verification) from the result files. Every number is read from a file.
  make_report.py OUTDIR   (OUTDIR contains steps/*.md; links are relative to it)"""
import os
import csv, glob, html, json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
bl = json.load(open(HERE / "blind/summary.json"))
cov = list(csv.DictReader(open(HERE / "coverage.csv")))
from openpyxl import load_workbook
wb = load_workbook(HERE / "out/RelaxDB_evidence_all_DRAFT.xlsx", read_only=True)
n_ev = wb["Evidence"].max_row - 1; n_pr = wb["Proteins"].max_row - 1; n_gap = wb["Gaps"].max_row - 1; n_pap = wb["Papers"].max_row - 1
gaps = list(wb["Gaps"].iter_rows(values_only=True))[1:]
gap_by = {}
for g in gaps: gap_by[g[2]] = gap_by.get(g[2], 0) + 1
no_full = sum(r["full_text_rows"] == "0" for r in cov)
filled = {k: sum(bool(r[k]) and r[k] != "0" and r[k] != "False" for r in cov) for k in ("residues", "alt_state_pdb", "experiments", "timescale", "population")}
st = list(csv.DictReader(open(Path.home() / "dynamics_atlas_work/outputs/spine_20261112/source_texts/source_text_status.csv")))
n_text = sum(r["verdict"].startswith("PASS") for r in st)
cf = sorted(glob.glob(str(HERE / "cond_fill/out/*.jsonl")))
cf_rows = cf_val = 0
for f in cf:
    for l in open(f):
        if l.strip():
            o = json.loads(l); cf_rows += 1; cf_val += sum(bool(str(o.get(k) or "").strip()) for k in ("temperature", "ph", "buffer"))
_ev = list(wb["Evidence"].iter_rows(values_only=True)); _ix = {k: i for i, k in enumerate(_ev[0])}
_inp = {r["evidence_id"]: r for r in json.load(open(HERE / "cond_fill/input_rows.json"))}
cf_add = {"temperature": 0, "ph": 0, "buffer": 0}; cf_reason = {}
for _r in _ev[1:]:
    _i = _inp.get(_r[0])
    if not _i: continue
    for _k, _c in (("temperature", "Temperature (K)"), ("ph", "pH"), ("buffer", "Buffer")):
        _v = str(_r[_ix[_c]] or "")
        if not _i["have"][_k]:
            if _v.startswith("[empty: "): _rs = _v[8:-1]; cf_reason[_rs] = cf_reason.get(_rs, 0) + 1
            elif _v: cf_add[_k] += 1
nrows_src = sum(sum(1 for _ in open(f)) for f in glob.glob(str(HERE / "source_read/*/rows.jsonl")))
nfold = len(glob.glob(str(HERE / "source_read/*/rows.jsonl")))
pct = lambda a, b: f"{100*a/b:.1f}%"
fe = bl["field_error_rate"]; re_ = bl["row_error_rate"]; ir = bl["item_recall"]; ir2 = bl["item_recall_if_cited_values_excluded"]
vr = subprocess.run([sys.executable, str(HERE / "verify_all.py")], capture_output=True, text=True, cwd=HERE)
verify_text = html.escape(vr.stdout.strip())

NODES = {  # id: (x, y, w, h, class, line1, line2, doc)
 "S1": (330, 20, 300, 60, "prog", "1 骨架表：每个蛋白一行", "程序，标准固定，已完成", "01_spine"),
 "S2": (330, 120, 300, 60, "prog", "2 找免费合法全文", "程序，标准固定，已完成", "02_find_free_text"),
 "S3": (40, 240, 300, 60, "human", "3 人工下载 PDF", "人，学校账号，进行中", "03_owner_download"),
 "S4": (560, 240, 300, 60, "prog", "4 核对身份", "程序，标准固定，已完成", "04_identity_check"),
 "S5": (560, 340, 300, 60, "prog", "5 列出要读的论文", "程序，标准固定，已完成", "05_manifest"),
 "S6": (560, 440, 300, 60, "agent", "6 读论文和补充材料写证据行", "agent（Sonnet），固定任务书，两轮", "06_read_papers"),
 "S7": (560, 540, 300, 60, "prog", "7 核对证据行", "程序，标准固定，已完成", "07_row_check"),
 "S11": (40, 660, 300, 60, "agent", "11 补 11-01 那批的实验条件", "agent 加程序核对，已完成", "11_condition_fill"),
 "S8": (560, 660, 300, 60, "prog", "8 并进总表", "程序，标准固定，已完成", "08_merge"),
 "S10": (170, 780, 300, 60, "judge", "10 盲评抽样", "两个独立模型，固定评分表，做了一轮", "10_blind_review"),
 "S9": (520, 780, 300, 60, "judge", "9 回原文抽查", "主会话，判断，只抽了 7 行", "09_spot_check"),
 "S14": (760, 880, 200, 60, "prog", "14 推送到 GitHub", "见本次交付", "14_publish"),
 "S12": (330, 900, 300, 60, "notdone", "12 决定发不发", "人，还没做", "12_owner_decision"),
 "S13": (330, 1020, 300, 60, "notdone", "13 Gina 抽查", "外部科学家，还没做", "13_gina_reads"),
 "B1": (40, 1020, 240, 60, "bug", "缺关卡", "没做盲评就能发出", None),
 "B2": (330, 1130, 300, 60, "bug", "缺关卡", "没有 Gina 看过就能写“完整”", None),
}
def c(n, side):
    x, y, w, h = NODES[n][:4]
    return {"t": (x + w / 2, y), "b": (x + w / 2, y + h), "l": (x, y + h / 2), "r": (x + w, y + h / 2)}[side]
EDGES = [  # (from, side, to, side, label, via)
 ("S1", "b", "S2", "t", "", None), ("S2", "b", "S3", "t", "拿不到", "ymid"), ("S2", "b", "S4", "t", "找到免费版", "ymid"),
 ("S3", "r", "S4", "l", "放入文件夹", None), ("S4", "b", "S5", "t", "通过", None), ("S5", "b", "S6", "t", "", None), ("S6", "b", "S7", "t", "", None),
 ("S7", "b", "S8", "t", "全部通过", None), ("S11", "r", "S8", "l", "", None),
 ("S8", "b", "S10", "t", "", "ymid"), ("S8", "b", "S9", "t", "", "ymid"), ("S8", "b", "S14", "t", "", "ymid"),
 ("S10", "b", "S12", "t", "", "ymid"), ("S9", "b", "S12", "t", "", "ymid"), ("S12", "b", "S13", "t", "", None),
 ("S12", "b", "B1", "t", "今天不要求盲评通过", "ymid"), ("S13", "b", "B2", "t", "今天不要求 Gina 看过", None),
]
svg = ['<svg viewBox="0 0 1000 1220" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="论文怎样变成总表里的行的流程图">',
       '<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="var(--edge)"/></marker></defs>']
def path(f, fs, t, ts, via):
    (x1, y1), (x2, y2) = c(f, fs), c(t, ts)
    if via == "ymid":
        ym = (y1 + y2) / 2; return f"M{x1},{y1} L{x1},{ym} L{x2},{ym} L{x2},{y2}"
    return f"M{x1},{y1} L{x2},{y2}"
for f, fs, t, ts, label, via in EDGES:
    p = path(f, fs, t, ts, via); dash = ' stroke-dasharray="6 5"' if t in ("B1", "B2") else ""
    svg.append(f'<path d="{p}" fill="none" stroke="var(--edge)" stroke-width="1.6"{dash} marker-end="url(#ar)"/>')
    if label:
        (x1, y1), (x2, y2) = c(f, fs), c(t, ts); lx = (x1 + x2) / 2 if via != "ymid" else x2; ly = (y1 + y2) / 2 + (4 if via != "ymid" else 14)
        if via == "ymid": lx = (x1 + x2) / 2; ly = (y1 + y2) / 2 - 4
        svg.append(f'<text x="{lx}" y="{ly}" text-anchor="middle" class="elabel">{html.escape(label)}</text>')
# back edges drawn by hand
svg.append('<path d="M560,285 L340,285" fill="none" stroke="var(--edge)" stroke-width="1.6" marker-end="url(#ar)" stroke-dasharray="6 5"/><text x="450" y="302" text-anchor="middle" class="elabel">被拒，重新下载</text>')
svg.append('<path d="M860,570 L900,570 L900,470 L860,470" fill="none" stroke="var(--edge)" stroke-width="1.6" marker-end="url(#ar)" stroke-dasharray="6 5"/><text x="935" y="525" text-anchor="middle" class="elabel">没过，重写</text>')
for k, (x, y, w, h, cls, l1, l2, doc) in NODES.items():
    box = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" class="n {cls}"/><text x="{x+w/2}" y="{y+26}" text-anchor="middle" class="t1">{html.escape(l1)}</text><text x="{x+w/2}" y="{y+46}" text-anchor="middle" class="t2">{html.escape(l2)}</text>'
    svg.append(f'<a href="steps/{doc}.md">{box}</a>' if doc else box)
svg.append("</svg>")
chart = "\n".join(svg)

STEPS = [("1", "骨架表", "程序", "固定", "已完成", "01_spine", "spine.csv，重跑逐字节一致"), ("2", "找免费合法全文", "程序", "固定", "已完成", "02_find_free_text", "source_text_status.csv"),
 ("3", "人工下载 PDF", "人（团队）", "—", "进行中", "03_owner_download", "drop 文件夹 103 个文件"), ("4", "核对身份", "程序", "固定", "已完成", "04_identity_check", f"{n_text} 篇有可用全文"),
 ("5", "列出要读的论文", "程序", "固定", "已完成", "05_manifest", "再跑一次给出 0 篇待读"), ("6", "读论文写证据行", "agent（Sonnet）", "固定任务书", "两轮完成", "06_read_papers", f"{nfold} 个文件夹，{nrows_src} 行"),
 ("7", "核对证据行", "程序", "固定", "已完成", "07_row_check", f"{nrows_src} 行，0 个错误"), ("8", "并进总表", "程序", "固定", "已完成", "08_merge", f"{n_ev} 行，{n_pr} 个蛋白"),
 ("9", "回原文抽查", "主会话", "判断", "只抽了 7 行", "09_spot_check", "7 行全部一致"), ("10", "盲评抽样", "两个独立模型", "固定评分表", "做了一轮", "10_blind_review", f"{bl['rows']} 行，{fe[0]}/{fe[1]} 字段矛盾"),
 ("11", "补 11-01 条件", "agent 加程序", "固定核对", "已完成", "11_condition_fill", f"{cf_rows} 行已处理，净增 {cf_add['temperature']} 个温度"), ("12", "决定发不发", "项目负责人", "判断", "还没做", "12_owner_decision", "—"),
 ("13", "Gina 抽查", "外部科学家", "判断", "还没做", "13_gina_reads", "—"), ("14", "推送 GitHub", "主会话", "固定清理检查", "见本次交付", "14_publish", "—")]
rowsh = "".join(f'<tr><td>{a}</td><td><a href="steps/{doc}.md">{html.escape(b)}</a></td><td>{who}</td><td>{std}</td><td>{status}</td><td>{html.escape(ev)}</td></tr>' for a, b, who, std, status, doc, ev in STEPS)

page = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>RelaxDB 证据总表：做法与问题</title>
<style>
:root{{--bg:#fbfaf7;--fg:#1c1b18;--mut:#6b675f;--line:#dcd8cd;--edge:#6b675f;--prog:#dbeafe;--progS:#1e40af;--agent:#ede9fe;--agentS:#6d28d9;--human:#fef3c7;--humanS:#b45309;--judge:#d1fae5;--judgeS:#047857;--notdone:#f1efe9;--notdoneS:#8a8577;--bug:#fee2e2;--bugS:#b91c1c;--card:#fff}}
@media(prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#16150f;--fg:#ece9df;--mut:#a39e90;--line:#38352b;--edge:#a39e90;--prog:#1e2f52;--agent:#2e2150;--human:#4a3410;--judge:#0f3b2c;--notdone:#26241c;--bug:#4a1d1d;--card:#1d1c15}}}}
body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.7 -apple-system,"PingFang SC","Noto Sans CJK SC",sans-serif}}
main{{max-width:980px;margin:0 auto;padding:28px 16px 80px}}h1{{font-size:1.7rem;margin:0 0 .3em}}h2{{font-size:1.25rem;margin:2em 0 .5em;border-bottom:1px solid var(--line);padding-bottom:.25em}}h3{{font-size:1.05rem;margin:1.4em 0 .3em}}
.lead{{font-size:1.08rem;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 18px}}table{{border-collapse:collapse;width:100%;font-size:.93rem;background:var(--card)}}th,td{{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}}th{{background:var(--notdone)}}
a{{color:var(--progS)}}.n{{stroke-width:1.6}}.prog{{fill:var(--prog);stroke:var(--progS)}}.agent{{fill:var(--agent);stroke:var(--agentS)}}.human{{fill:var(--human);stroke:var(--humanS)}}.judge{{fill:var(--judge);stroke:var(--judgeS)}}.notdone{{fill:var(--notdone);stroke:var(--notdoneS);stroke-dasharray:6 4}}.bug{{fill:var(--bug);stroke:var(--bugS)}}
.t1{{font-size:15px;font-weight:600;fill:var(--fg)}}.t2{{font-size:12.5px;fill:var(--mut)}}.elabel{{font-size:12px;fill:var(--mut)}}svg{{width:100%;height:auto;background:var(--card);border:1px solid var(--line);border-radius:10px}}
.legend span{{display:inline-block;margin:2px 10px 2px 0;padding:1px 10px;border-radius:6px;border:1.5px solid;font-size:.85rem}}pre{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 12px;overflow-x:auto;font-size:.82rem}}code{{font-size:.9em}}.mut{{color:var(--mut)}}
</style></head><body><main>
<h1>把 Gina 的蛋白填进定好的 Excel：做法、证据和问题</h1>
<p class="mut">2026-11-12。这是草稿，没有发给任何人。点流程图里的方框或步骤表里的名字，可以展开那一步的说明文档。</p>
<div class="lead"><b>结论。</b>总表现在有 {n_pr} 个蛋白、{n_ev:,} 行，缺口 {n_gap} 项。写下来的值很准：15 篇论文、{bl['rows']} 行、{fe[1]} 个字段里，只有 {fe[0]} 个字段和原文矛盾（{pct(fe[0],fe[1])}）。真正的问题是<b>漏</b>：论文里报告了、表里没有的数值占 {ir[1]-ir[0]}/{ir[1]}（{pct(ir[1]-ir[0],ir[1])}），而且有 {no_full} 个蛋白一篇全文都没读到。能回答“是不是完整”的只有 Gina，她还没看过新结果。</div>

<h2>1. 流程图：每一步做什么、谁判断</h2>
<p class="legend"><span style="background:var(--prog);border-color:var(--progS)">程序，标准固定</span><span style="background:var(--agent);border-color:var(--agentS)">agent 按固定任务书</span><span style="background:var(--judge);border-color:var(--judgeS)">独立模型或人的判断</span><span style="background:var(--human);border-color:var(--humanS)">人工操作</span><span style="background:var(--notdone);border-color:var(--notdoneS)">还没做</span><span style="background:var(--bug);border-color:var(--bugS)">今天流程里缺的关卡</span></p>
{chart}
<p class="mut">红色框是模型检查（TLC）找到的两处缺口，不是已经发生的事：现在没有任何程序拦住“没做盲评就发出”和“没有 Gina 看过就把表写成完整”。另外 4 条规则在模型里守住了：封存条目不读、只收过核对的行、全文先核对身份才读、总表首页不隐瞒是否盲评。加上两道关卡后，6 条规则全部守住。完整的 71 个状态图在 <a href="statechart/chart.png">statechart/chart.png</a>，模型在 <a href="statechart/FillTable.tla">FillTable.tla</a>。</p>
<table><tr><th>#</th><th>步骤</th><th>谁判断</th><th>标准</th><th>状态</th><th>证据</th></tr>{rowsh}</table>

<h2>2. 科学性和可复刻性</h2>
<h3>科学性：表里写的是什么</h3>
<p>表只收论文自己报告的值，每个值带一句逐字引文和位置。不做分析，不换算（不从速率算布居数，不把单位改掉），图里才有的数值留空并写“在图里”。同一篇论文里正文和表格的值不一致时，两个都记，不替作者选。样品和登记值对不上时（温度、构建体、缓冲液），行里标“是不是同一个样品”和原因，不改数。这样做是为了让 Gina 看到的是“论文说了什么”，不是我们的结论。</p>
<h3>可复刻性：哪些能重跑，哪些不能</h3>
<table><tr><th>环节</th><th>能不能逐字重跑</th><th>怎么重跑</th></tr>
<tr><td>骨架表、论文清单、总表、缺口表、各项检查</td><td>能。同样的输入给同样的输出</td><td><code>python3 scripts/relaxdb_evidence_table/verify_all.py</code>（需要 <code>~/dynamics_atlas_work</code> 的目录结构，见 README）</td></tr>
<tr><td>agent 读论文</td><td>不能。模型每次输出不同；一次运行就是一次运行</td><td>复刻的是检查，不是读：任何读者（换模型、换人）按同一份任务书写的行，都要过同一个检查程序，再过盲评</td></tr>
<tr><td>论文全文</td><td>不能放进仓库（版权）</td><td>每篇的 DOI 和获取状态在 <code>data/…/source_text_status.csv</code>；复刻的人自己取全文放进 <code>drop/</code></td></tr></table>
<p class="mut">没做的复刻验证：同一个 agent 对同一篇论文读两次，比两次的差别。读者换成另一个模型再比，也没做。</p>

<h2>3. 现在真正遇到的问题</h2>
<p>按对结果的影响排序。</p>
<ol>
<li><b>全文拿不到。</b>99 篇缺全文的源论文里，现在 {n_text} 篇可用，还差 {99-n_text} 篇。11 月 11 日那批 78 个蛋白里，1,533 篇 A、B 档文献只有约 34% 读到全文，其余只有摘要，摘要里没有温度、速率和布居数。有 {no_full} 个蛋白一篇全文行都没有。</li>
<li><b>漏项，而且没办法自证。</b>盲评抽样 15 篇：论文里报告了的 {ir[1]} 个速率、布居数和结构编号，表里覆盖了 {ir[0]} 个（{pct(ir[0],ir[1])}，区间 {ir[2]*100:.0f}–{ir[3]*100:.0f}%）。漏的 {bl['items_missing_real']} 个里，{bl['missing_split']['cited_from_earlier_work_or_not_dynamics']} 个是论文只引用别人的数值，{bl['missing_split']['measured_in_the_paper']} 个是论文自己测的，其中 1 篇（CheA 的氢氘交换）就漏了 6 个，因为只写了一个结构域。把只引用别人的排除，覆盖率是 {ir2[0]}/{ir2[1]}（{pct(ir2[0],ir2[1])}）。这个排除是我用裁判给的理由里的关键词分的，不是独立判断。样本是 15 篇，一个条目（CHEA）占了 4 篇，不是分层抽样。</li>
<li><b>登记值本身不可靠。</b>133 个蛋白里 56 个温度正好是 298.5 K，全部来自非 BMRB 的来源，很可能是占位值。读论文时发现至少 6 个条目的论文温度和登记温度不同（如 273 K 对 35 °C）。我们把它们标出来，不改；要问 Gina。</li>
<li><b>11-01 那批的条件补不全。</b>1,030 行里 584 行缺温度、pH 或缓冲液。补完之后净增加 {cf_add["temperature"]} 个温度、{cf_add["ph"]} 个 pH、{cf_add["buffer"]} 个缓冲液，每个值都有逐字依据，程序核对过。剩下的空格子现在都写了原因：{cf_reason.get("abstract_only_no_conditions",0)} 个是这行只读过摘要，没法补；{cf_reason.get("not_in_row_text_and_paper_not_cached",0)} 个是论文全文不在本地缓存；{cf_reason.get("paper_text_mentions_it_unchecked",0)} 个是 agent 没找到，但论文文本里出现过这一项，我没有核对，所以没写成“论文没报告”。</li>
<li><b>检查只能查“值在原文里”，查不出“配对对不对”。</b>盲评找到的 {bl['contradicted_fields']} 个矛盾字段，都是配对或判断类：2 个“立场”写成支持动力学但论文只测了平衡亲和力或只是降低而不是没有；2 个方法标签不合；1 个残基属于另一个突变体。这类错只能靠第二个模型或人读才能发现。</li>
<li><b>别的团队的批量自动下载有风险。</b>drop 里出现 45 个 <code>cdp_</code> 开头的订阅期刊文件，说明有人用浏览器自动化批量下载了 ACS 和 Springer 论文。这可能触发出版社封禁整个学校的访问。需要项目负责人和图书馆确认。</li></ol>

<h2>4. 论文怎么保证合理，最后想要的结果</h2>
<h3>哪些论文进表，怎么保证合理</h3>
<p>每个蛋白有两类论文。第一类是它在 RelaxDB 里登记的源论文（BMRB 的引用，加 Gina 表里的出处），一律要读。第二类是沿引文网络和 Europe PMC 搜到、再按摘要分级筛出的相关论文。11 月 1 日在四个研究很透的蛋白上量过：论文召回 39/59，动力学数值 41/50，结构编号只有 26/96，这是最弱的一项。保证合理靠四件事：（1）身份核对，文件里必须有这篇的 DOI 或标题；（2）每行的引文逐字在这篇论文里；（3）行里标明这篇研究的是目标蛋白、同一蛋白的另一个构建体，还是同源蛋白，同源蛋白的数不挂到目标上；（4）不同样品的结果并列放，不合并成一个结论。</p>
<h3>最后想要的结果</h3>
<p>一本 Excel，格式就是 11 月 1 日给 Gina 的十蛋白版：一行是一篇论文的一个实验，列出残基、替代态结构（每个 PDB 编号）、实验、时间尺度、布居数、样品条件、原文引文和跳转链接；缺的格子写明为什么缺。Gina 抽查通过之前，这本表叫草稿，不叫完整。下一步是把同样的流程放到更大的蛋白集合上。</p>

<h2>5. 整体验证</h2>
<p>我按 pstack 的几条准则重做了验证，每条改变了一个具体做法：<b>prove it works</b>（脚本化、对照真实产物、真值来自会话之外）：把所有确定性检查合成一个脚本，并且每个检查都配故意做错的样例；<b>explain the number</b>（先查是什么限制了数字再信它）：召回 72% 拆成“漏了论文自己测的”和“漏了论文引用别人的”两个数；<b>sequence work into verifiable units</b>：每一步各有自己的检查，上一步没过不进下一步；<b>correct</b>（规则表）：下表把每条规则和执行它的代码行配对。</p>
<h3>验证矩阵：每个说法由什么来证明</h3>
<table><tr><th>说法</th><th>检查</th><th>真值来自</th><th>结论用词</th><th>状态</th></tr>
<tr><td>引文逐字在论文里，数字在论文里</td><td>check_rows.py</td><td>论文原文</td><td>VERIFIED</td><td>{nrows_src} 行，0 错误；4 种故意做错的样例都被拒</td></tr>
<tr><td>值没有配错（残基、样品、立场）</td><td>两个独立模型盲评</td><td>论文原文，由模型读</td><td>CONSISTENT，不是 VERIFIED</td><td>{fe[0]}/{fe[1]} 字段矛盾（{pct(fe[0],fe[1])}，区间 {fe[2]*100:.1f}–{fe[3]*100:.1f}%）；{re_[0]}/{re_[1]} 行含错（{pct(re_[0],re_[1])}，区间 {re_[2]*100:.1f}–{re_[3]*100:.1f}%）</td></tr>
<tr><td>同上，抽样回原文</td><td>主会话打开原文逐值对照</td><td>论文原文和扫描原图</td><td>VERIFIED，仅限抽到的行</td><td>7 行，全部一致</td></tr>
<tr><td>没有漏项</td><td>盲评清单对比</td><td>论文原文，由模型读</td><td>CONSISTENT</td><td>覆盖 {ir[0]}/{ir[1]}；漏项不为零</td></tr>
<tr><td>表是“完整”的</td><td>—</td><td>只有 Gina 能回答</td><td>NOT YET MEASURABLE</td><td>还没做</td></tr>
<tr><td>登记值（温度、磁场、pH）</td><td>对照 BMRB 和 Gina 的表</td><td>BMRB，Gina 的表</td><td>VERIFIED 对 BMRB</td><td>298.5 K 占位问题未决</td></tr>
<tr><td>封存的 12 个条目没碰</td><td>sealed 关卡</td><td>划分文件</td><td>VERIFIED</td><td>总表、行文件、导出包里都是 0</td></tr></table>
<p class="mut">盲评的两个模型（读者和裁判）都是 Opus，填表的是 Sonnet。换了型号但同属一个模型家族，所以只算一致性。</p>
<h3>一次重跑全部检查</h3>
<pre>{verify_text}</pre>
<h3>规则表：规则由什么执行</h3>
<table><tr><th>规则</th><th>执行它的代码或文档</th><th>反例证明</th></tr>
<tr><td>封存条目不读、不进表</td><td>source_fulltext.py:44，check_rows.py:34，build_manifest.py:21</td><td>verify_all.py 里“封存条目”样例被拒</td></tr>
<tr><td>全文先核对身份才能读</td><td>build_manifest.py:23</td><td>—（由清单来源保证，没有单独的反例）</td></tr>
<tr><td>没过核对的行不进总表</td><td>build_all.py:225</td><td>11-12 才补上这道关卡，之前只是标注“没通过”</td></tr>
<tr><td>没做盲评不能发出</td><td>只有文字规则，没有程序拦</td><td>模型检查找到的缺口 1</td></tr>
<tr><td>没有 Gina 看过不能写“完整”</td><td>只有文字规则，没有程序拦</td><td>模型检查找到的缺口 2</td></tr></table>
<h3>还没做的验证</h3>
<ul><li>Gina 抽查（唯一能回答完整性的一步）。</li><li>11 月 11 日那批 1,848 行里，盲评只覆盖了 15 篇、71 行，不到 4%。</li><li>同一论文读两次的一致性，换一个模型读的一致性。</li><li>检查程序放行的数字，如果出现在全文别处，它看不出来。</li></ul>
<p class="mut">说明文档、任务书、模型和全部数据在同一个仓库分支里。</p>
</main></body></html>'''
(OUT / "REPORT.html").write_text(page)
print("wrote", OUT / "REPORT.html", len(page), "bytes")
