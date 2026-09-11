// Builds slides/Dynamics_Atlas_flowcharts.pptx: three slides, one flowchart each, every
// box, arrow and label an editable PowerPoint shape. Content comes from
// figures/flowcharts.json (shared with scripts/build_flowcharts.py, which renders the
// PNG and SVG). Geometry is in inches on a 10 x 5.625 in (16:9) slide, y pointing down,
// and mirrors the Python renderer.
//
// Usage (from the worktree root):  node scripts/build_flowcharts.cjs
const fs = require('fs');
const path = require('path');
const NM = process.env.NODE_MODULES_PATH || 'node_modules';
const pptxgen = require(path.join(NM, 'pptxgenjs'));

const ROOT = path.dirname(__dirname);
const SPEC = JSON.parse(fs.readFileSync(path.join(ROOT, 'figures', 'flowcharts.json'), 'utf8'));
const OUT = path.join(ROOT, 'slides', 'Dynamics_Atlas_flowcharts.pptx');
const S = SPEC.style;
const F = S.font;
const PAD_PT = 0.08 * 72; // text inset, same 0.08 in as the Python renderer

function fillFor(kind) {
  if (kind === 'current') return [S.current, S.current_line];
  if (kind === 'grey') return [S.grey, S.grey_line];
  if (kind === 'none') return ['FFFFFF', S.empty_line];
  return [S.box, S.box_line];
}

class Slide {
  constructor(pptx, title) {
    this.pptx = pptx;
    this.s = pptx.addSlide();
    this.s.background = { color: 'FFFFFF' };
    this.text(0.4, 0.22, 9.2, 0.45, title, { size: 18, color: S.heading, bold: true, align: 'left', pad: 0 });
  }
  box(x, y, w, h, fill, line) {
    this.s.addShape(this.pptx.ShapeType.roundRect, {
      x, y, w, h, rectRadius: 0.05, fill: { color: fill }, line: { color: line, width: 0.75 },
    });
  }
  // runs: string or [{text, bold, color}] rendered as separate lines
  text(x, y, w, h, runs, o = {}) {
    const size = o.size || 11;
    const color = o.color || S.body;
    const pad = o.pad === undefined ? PAD_PT : o.pad;
    let body;
    if (typeof runs === 'string') body = runs;
    else body = runs.map((r, i) => ({ text: r.text, options: { bold: !!r.bold, color: r.color || color, breakLine: i < runs.length - 1 } }));
    this.s.addText(body, {
      x, y, w, h, fontSize: size, fontFace: F, color, bold: !!o.bold,
      align: o.align || 'center', valign: o.valign || 'middle', margin: pad, lineSpacingMultiple: 1.05,
    });
  }
  arrow(x0, y0, x1, y1, o = {}) {
    const head = o.head === undefined ? true : o.head;
    const line = { color: o.color || S.arrow, width: o.lw || 1.4 };
    if (head) line.endArrowType = 'triangle';
    this.s.addShape(this.pptx.ShapeType.line, { x: x0, y: y0, w: x1 - x0, h: y1 - y0, line });
  }
  circle(cx, cy, r, fill, line) {
    this.s.addShape(this.pptx.ShapeType.ellipse, { x: cx - r, y: cy - r, w: 2 * r, h: 2 * r, fill: { color: fill }, line: { color: line, width: 1.2 } });
  }
  footer() {
    this.text(0.4, 5.28, 6.0, 0.22, SPEC.footer, { size: 9, color: S.muted, align: 'left', pad: 0 });
  }
}

function projectMap(pptx, f) {
  const sl = new Slide(pptx, f.title);
  const steps = f.steps, n = steps.length;
  const x0 = 0.4, span = 9.2, gap = 0.22;
  const cw = (span - gap * (n - 1)) / n;
  const yStep = 0.85, hStep = 0.5;
  const yBy = 1.38, hBy = 0.44;
  const yLab2 = 1.92, yRow2 = 2.18, hRow2 = 0.9;
  const yLab3 = 3.22, yRow3 = 3.48, hRow3 = 1.4;
  steps.forEach((st, i) => {
    const x = x0 + i * (cw + gap);
    let [fill, line] = fillFor('box');
    sl.box(x, yStep, cw, hStep, fill, line);
    sl.text(x, yStep, cw, hStep, st.name, { size: 11.5, color: S.heading, bold: true });
    if (i < n - 1) sl.arrow(x + cw + 0.03, yStep + hStep / 2, x + cw + gap - 0.03, yStep + hStep / 2);
    sl.text(x, yBy, cw, hBy, st.by, { size: 11, color: S.muted, valign: 'top', pad: 0.02 * 72 });
    [fill, line] = fillFor(st.rule_kind);
    sl.box(x, yRow2, cw, hRow2, fill, line);
    sl.text(x, yRow2, cw, hRow2, st.rule, { size: 11, color: st.rule_kind === 'none' ? S.muted : S.body });
    [fill, line] = fillFor('grey');
    sl.box(x, yRow3, cw, hRow3, fill, line);
    sl.text(x, yRow3, cw, hRow3, st.happened, { size: 11 });
  });
  sl.text(x0, yLab2, span, 0.24, f.row_labels.rule, { size: 11, color: S.heading, bold: true, align: 'left', pad: 0 });
  sl.text(x0, yLab3, span, 0.24, f.row_labels.happened, { size: 11, color: S.heading, bold: true, align: 'left', pad: 0 });
  sl.footer();
}

function timeline(pptx, f) {
  const sl = new Slide(pptx, f.title);
  const nodes = f.nodes, n = nodes.length;
  const x0 = 0.4, span = 9.2, bw = 1.7;
  const gap = (span - n * bw) / (n - 1);
  const yLine = 1.65;
  const yDate = 1.15, hDate = 0.36;
  const yBox = 2.05, hBox = 1.75;
  const r = 0.11;
  sl.arrow(x0, yLine, x0 + span, yLine, { lw: 2.0 });
  nodes.forEach((nd, i) => {
    const x = x0 + i * (bw + gap);
    const cx = x + bw / 2;
    const [fill, line] = fillFor(nd.current ? 'current' : 'box');
    sl.circle(cx, yLine, r, nd.current ? S.current : S.heading, nd.current ? S.current_line : S.heading);
    sl.text(x, yDate, bw, hDate, nd.date, { size: 12, color: S.heading, bold: true, valign: 'bottom', pad: 0.02 * 72 });
    sl.arrow(cx, yLine + r, cx, yBox, { head: false, lw: 1.2 });
    sl.box(x, yBox, bw, hBox, fill, line);
    sl.text(x, yBox, bw, hBox, nd.text, { size: 11 });
  });
  sl.text(x0, 4.15, span, 0.36, f.caption, { size: 12, color: S.heading, bold: true, pad: 0 });
  sl.footer();
}

function verticalFlow(pptx, f) {
  const sl = new Slide(pptx, f.title);
  const boxes = f.boxes;
  const x = 0.4, w = 5.6, h = 0.7, gap = 0.18, y0 = 0.85;
  const sx = 6.5, sw = 3.1;
  const ys = [];
  boxes.forEach((b, i) => {
    const y = y0 + i * (h + gap);
    ys.push(y);
    const [fill, line] = fillFor('box');
    sl.box(x, y, w, h, fill, line);
    const runs = [];
    if (b.lead) runs.push({ text: b.lead, bold: true, color: S.heading });
    runs.push({ text: b.text, color: S.body });
    sl.text(x, y, w, h, runs, { size: 11, align: 'left' });
    if (i < boxes.length - 1) sl.arrow(x + w / 2, y + h + 0.02, x + w / 2, y + h + gap - 0.02);
  });
  f.side_notes.forEach((sn) => {
    const y = ys[sn.box];
    const [fill, line] = fillFor('grey');
    sl.arrow(x + w, y + h / 2, sx, y + h / 2, { head: false, lw: 1.2 });
    sl.box(sx, y, sw, h, fill, line);
    sl.text(sx, y, sw, h, sn.text, { size: 11, align: 'left' });
  });
  sl.footer();
}

const RENDERERS = { project_map: projectMap, timeline, vertical_flow: verticalFlow };

(async () => {
  const pptx = new pptxgen();
  pptx.layout = 'LAYOUT_16x9';
  pptx.title = 'Dynamics Atlas flowcharts';
  for (const f of Object.values(SPEC.figures)) RENDERERS[f.kind](pptx, f);
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  await pptx.writeFile({ fileName: OUT });
  console.log(`wrote ${path.relative(ROOT, OUT)} (${fs.statSync(OUT).size} bytes), slides: ${Object.keys(SPEC.figures).length}`);
})();
