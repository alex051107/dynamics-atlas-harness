// Labels for FillTable. Reader: the project owner. Each step says what is checked, who decides, and whether the standard is fixed.
export const readerActions = ["OwnerDrop", "OwnerApprove"];

const TEXT = { None: "全文还没拿到", Abstract: "只有摘要", FullRaw: "拿到文件，身份未核", FullOK: "全文已核对身份", Rejected: "文件被拒（不是这篇或太短）" };
const ROWS = { None: "", Written: "；agent 已写证据行，未核对", AbstractRows: "；摘要行已写，未核对", Checked: "；行已过原文核对", Failed: "；行没过核对，待重做" };

export function state(v) {
	if (v.sealed) return "封存条目：留作最后的测试，不读";
	const p = [TEXT[v.text] + ROWS[v.rows]];
	if (v.merged) p.push(v.label === "Reviewed" ? "已并进总表（标注：已盲评）" : "已并进总表（标注：未盲评）");
	if (v.spot) p.push("主会话抽查过");
	if (v.blind === "Passed") p.push("盲评通过");
	if (v.blind === "Failed") p.push("盲评没过");
	if (v.sent) p.push("已发出");
	if (v.gina) p.push("Gina 已看");
	if (v.claim === "Complete") p.push("表被写成“完整”");
	return p.join("；");
}

export function group(v) {
	if (v.sealed) return "封存";
	if (v.claim === "Complete") return "被称完整";
	if (v.sent) return "已发给合作者";
	if (v.merged) return "已在总表";
	return "处理中";
}
export const groupColors = { "封存": "#e5e7eb", "处理中": "#dbeafe", "已在总表": "#fef3c7", "已发给合作者": "#d1fae5", "被称完整": "#fee2e2" };

const STEPS = {
	FindFree: "找免费合法全文〔程序：Europe PMC、PMC、预印本，不登录；封存条目拒绝〕",
	OwnerDrop: "人工下载 PDF 放进文件夹〔人：用学校账号〕",
	IdentityCheck: "核对身份〔程序：文件里有这篇的 DOI 或标题，正文至少 5,000 字；标准固定〕",
	ReadFull: "读全文和补充材料写证据行〔agent Sonnet，按固定任务书；只读这一篇〕",
	ReadAbstract: "只按摘要写行〔agent Sonnet；摘要里没有的条件不写〕",
	RowCheck: "核对证据行〔程序：引文逐字在原文，数字在原文，空格子有原因；标准固定〕",
	Repair: "按核对结果重写〔agent〕",
	Merge: "并进总表〔程序：只收过核对的行；总表首页注明是否盲评〕",
	SpotCheck: "回原文抽查〔主会话 Fable：打开论文逐值对照；看判断，不是固定标准〕",
	BlindReview: "盲评抽样〔另一个模型先不看表读论文，再由裁判比对；标准按固定评分表〕",
	OwnerApprove: "决定发不发〔人：项目负责人〕",
	Send: "发给 Gina、Soojung〔人：项目负责人〕",
	GinaReads: "Gina 抽查〔人，外部裁判；还没做〕",
	MarkComplete: "把表写成“完整”〔人；今天没有任何程序拦这一步〕",
};
export function step(action) { return STEPS[action] ?? action; }

export function cause(v, facts, invariant) {
	if (invariant === "NoSendUnreviewed") return "没做盲评就能发出：发出前只要求项目负责人同意，没有要求盲评通过";
	if (invariant === "NoCompleteWithoutGina") return "没有科学家看过就能写“完整”：只要程序核对和抽查过了就放行，没有要求 Gina 看过";
	return null;
}
export const legend = { works: "今天的流程下守住了", wrong: "今天的流程下会破", fixed: "加上提议的关卡后守住" };
