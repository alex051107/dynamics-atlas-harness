const path = require('path');
const NM = '/Users/liuzhenpeng/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const pptxgen = require(path.join(NM, 'pptxgenjs'));
const OUT = process.argv[2];

const C = { bg: 'FFFFFF', primary: '1F4E79', accent: '2E75B6', body: '2D2D2D', muted: '777777', rule: 'CCCCCC', hl: 'FFF2CC', red: 'C0392B', green: '2E7D32', pale: 'E8EEF5', grey: 'F2F2F2' };
const F = 'Arial';
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_16x9';
pptx.author = 'Zhenpeng Liu';
pptx.title = 'Dynamics Atlas: the Rules Table, tested on three systems';

let n = 0;
function base(title, notes, source, titleSize) {
  if (!titleSize) titleSize = title.length > 125 ? 19 : 21;
  const s = pptx.addSlide(); n += 1;
  s.background = { color: C.bg };
  s.addText(title, { x: 0.5, y: 0.25, w: 9, h: 0.95, fontSize: titleSize, fontFace: F, bold: true, color: C.primary, valign: 'top' });
  if (source) s.addText(source, { x: 0.5, y: 5.18, w: 8.4, h: 0.3, fontSize: 10.5, fontFace: F, color: C.muted });
  s.addText(String(n), { x: 9.2, y: 5.18, w: 0.3, h: 0.3, fontSize: 10.5, fontFace: F, color: C.muted, align: 'right' });
  if (notes) s.addNotes(notes);
  return s;
}
function bullets(s, items, opt = {}) {
  const arr = items.map(t => (typeof t === 'string' ? { text: t, options: { bullet: true, breakLine: true } } : t));
  s.addText(arr, Object.assign({ x: 0.5, y: 1.3, w: 9, h: 3.7, fontSize: 16, fontFace: F, color: C.body, valign: 'top', paraSpaceAfter: 8 }, opt));
}
function table(s, rows, opt = {}) {
  const head = rows[0].map(t => ({ text: t, options: { bold: true, color: 'FFFFFF', fill: { color: C.primary } } }));
  const body = rows.slice(1).map(r => r.map(c => (typeof c === 'string' ? { text: c } : c)));
  s.addTable([head, ...body], Object.assign({ x: 0.5, y: 1.3, w: 9, fontSize: 12, fontFace: F, color: C.body, border: { type: 'solid', pt: 0.5, color: C.rule }, autoPage: false, valign: 'middle' }, opt));
}
function box(s, x, y, w, h, text, fill, color, size = 12, bold = false) {
  s.addShape(pptx.ShapeType.rect, { x, y, w, h, fill: { color: fill }, line: { color: fill === C.hl ? 'E6D48A' : fill } });
  s.addText(text, { x, y, w, h, fontSize: size, fontFace: F, color, align: 'center', valign: 'middle', bold, margin: 3 });
}
function arrow(s, x, y, w = 0.3) {
  s.addShape(pptx.ShapeType.rightArrow, { x, y, w, h: 0.26, fill: { color: C.rule }, line: { color: C.rule } });
}
function callout(s, x, y, w, h, text, size = 13) {
  s.addShape(pptx.ShapeType.rect, { x, y, w, h, fill: { color: C.hl }, line: { color: 'E6D48A' } });
  s.addText(text, { x, y, w, h, fontSize: size, fontFace: F, color: C.body, valign: 'middle', margin: 8 });
}
function label(s, x, y, w, text, color = C.accent) {
  s.addText(text, { x, y, w, h: 0.42, fontSize: 12, fontFace: F, bold: true, color, valign: 'top' });
}
const KEEP = { text: 'yes', options: { color: C.green, bold: true } };
const NO = { text: 'no', options: { color: C.red, bold: true } };

// ---------- 1 Title
{
  const s = pptx.addSlide(); n += 1;
  s.background = { color: C.primary };
  s.addText('Dynamics Atlas: the Rules Table, tested on three systems', { x: 0.7, y: 1.1, w: 8.6, h: 1.3, fontSize: 30, fontFace: F, color: 'FFFFFF', bold: true, valign: 'top' });
  s.addText('What the table was meant to do, how three real systems went through the workflow,\nwhat each layer measured, and how the system should be built from here', { x: 0.7, y: 2.4, w: 8.6, h: 0.9, fontSize: 15, fontFace: F, color: 'A0BBDD' });
  s.addText('Zhenpeng Liu · discussion with Soojung · 10 September 2026', { x: 0.7, y: 3.5, w: 8.6, h: 0.4, fontSize: 15, fontFace: F, color: 'FFFFFF' });
  s.addText('Idea and workflow (5 min) · three systems through the workflow (10) · what each layer measured (8) · how to build it: discussion (7)', { x: 0.7, y: 4.4, w: 8.6, h: 0.6, fontSize: 12.5, fontFace: F, color: 'A0BBDD' });
  s.addNotes(`SAY: Last time you knew I was building a Rules Table prototype. Today I want to discuss how the whole system should be built. I'll show the original idea, the workflow a new system actually goes through, what happened when three real systems went through it, what each layer of the table measured, and then three design options for the table itself. Headline first: putting rules into the prompt did not help; the errors we made were at data entry and at the numbers going out; the only layer that met its criterion was framing the question explicitly.
GOAL OF THE MEETING: (1) is the workflow reasonable; (2) are the three systems the right ones; (3) which form of the rules table should we build toward.`);
}

// ---------- 2 Original idea + what the table is
{
  const s = base('The original idea: an Agent enters the Rules Table and follows a set of rules to choose operations and extra analyses',
`SAY: This was the idea from July. A question and a data package come in; the Agent consults a table of rules distilled from methods papers; the rules tell it which operations to run, which extra analyses to add, and where it must abstain. The table has 33 rules from 11 papers, three per paper. Each rule stores the paper's finding, what our project must check, and an abstain route. Bottom-right is one rule verbatim.
GRILL: "Who wrote the rules?" I did in August from deep reads; an external review on 17 Aug asked to keep it as a reviewable ledger split into papers / rules / index.`,
'rule_registry.tsv v0.1; 11 papers (Hellenkamp 2018 … Wankowicz & Bonomi 2026); external review 17 Aug 2026');
  const y = 1.35;
  box(s, 0.5, y, 1.55, 0.85, 'New system:\nquestion + data', C.pale, C.primary, 11.5);
  arrow(s, 2.1, y + 0.3);
  box(s, 2.45, y, 1.7, 0.85, 'Rules Table\n33 rules / 11 papers', C.hl, C.body, 11.5, true);
  arrow(s, 4.2, y + 0.3);
  box(s, 4.55, y, 1.9, 0.85, 'Agent follows rules:\nwhich operation, what\nextra analysis, when to abstain', C.pale, C.primary, 10.5);
  arrow(s, 6.5, y + 0.3);
  box(s, 6.85, y, 1.4, 0.85, 'Analysis +\nnumbers', C.pale, C.primary, 11.5);
  arrow(s, 8.3, y + 0.3);
  box(s, 8.65, y, 0.85, 0.85, 'Bounded\nanswer', C.grey, C.body, 11);
  label(s, 0.5, 2.4, 4, 'What one rule stores');
  table(s, [
    ['Field', 'Meaning'],
    ['paper_finding', 'what the paper actually showed'],
    ['proposed_project_rule', 'what we must check before using this kind of data'],
    ['required_fields', 'the items the check needs'],
    ['abstain_route', 'where to stop if the check cannot be done'],
    ['transfer_scope', 'how far the lesson carries'],
  ], { x: 0.5, y: 2.72, w: 4.3, fontSize: 11, rowH: 0.3, colW: [1.7, 2.6] });
  label(s, 5.1, 2.4, 4.4, 'One rule verbatim (C006-RULE-003, Shevchuk 2017)');
  s.addText([
    { text: 'Finding: ', options: { bold: true } }, { text: 'if the candidate support omits a state, Bayesian SAXS refinement can express uncertainty within the wrong support but cannot create the missing state.', options: { breakLine: true } },
    { text: 'Check: ', options: { bold: true } }, { text: 'candidate-support coverage · state-number adequacy · missing-state audit.', options: { breakLine: true } },
    { text: 'Abstain: ', options: { bold: true } }, { text: 'MISSING_STATE_SUPPORT.', options: { breakLine: true } },
    { text: 'Scope: ', options: { bold: true } }, { text: 'a posterior cannot create a state absent from support.' },
  ], { x: 5.1, y: 2.72, w: 4.4, h: 2.3, fontSize: 11, fontFace: F, color: C.body, valign: 'top', paraSpaceAfter: 5 });
}

// ---------- 3 Workflow for a new system
{
  const s = base('What a new system goes through today, and where the Rules Table acts at each step',
`SAY: This is the workflow as it exists now. Read left to right. Intake: download the authors' deposited data and write a source card. Package: derived tables, field definitions, freeze with hashes. Framing: a person decides which difference the question must distinguish and writes the rubric. Run: the Agent analyses in a sealed container. Check: automatic checks on the submission. Report: every number linked to source, claim ceiling in words. The row underneath shows which layer of the table acts where: framing rules at step 3, admission rules at step 2, method cards at step 4, conclusion rules at step 5. Nothing in the table touches steps 1 and 6 today.
GRILL: "Where does a person sit?" Steps 1, 3 and 6. Step 3 is the only one that cannot be delegated: the competing explanations.`,
'Layers A–D from RULES_TABLE_ROLE_DESIGN_ZH.md; runtime from Luna v1 (PR #27)');
  const steps = [
    ['1 Intake', 'authors\' deposition\n+ source card\n(paper, SI, README)'],
    ['2 Package', 'derived tables,\nfield definitions,\nphysical checks, freeze'],
    ['3 Frame', 'sub-questions,\ncompeting explanations,\nrubric (hidden)'],
    ['4 Run', 'Agent in sealed\ncontainer: reads,\ncomputes, submits'],
    ['5 Check', 'automatic checks\non the submission,\none feedback'],
    ['6 Report', 'numbers linked to\nsource; claim\nceiling in words'],
  ];
  const w = 1.38, gap = 0.14, y = 1.35;
  steps.forEach((st, i) => {
    const x = 0.5 + i * (w + gap);
    box(s, x, y, w, 0.34, st[0], C.primary, 'FFFFFF', 11.5, true);
    box(s, x, y + 0.34, w, 1.0, st[1], C.pale, C.body, 9.5);
    if (i < 5) arrow(s, x + w - 0.02, y + 0.5, gap + 0.04);
  });
  const who = ['person + script', 'script + admission code', 'person + template', 'Agent', 'code', 'script + person'];
  who.forEach((t, i) => box(s, 0.5 + i * (w + gap), y + 1.42, w, 0.3, t, C.grey, C.muted, 9.5));
  const layer = ['—', 'B Admission\n10 rules', 'A Framing\n6 rules', 'C Method cards\n11 rules', 'D Conclusion\n6 rules', '—'];
  label(s, 0.5, 3.2, 5, 'Where the Rules Table acts');
  layer.forEach((t, i) => box(s, 0.5 + i * (w + gap), 3.5, w, 0.6, t, t === '—' ? 'FFFFFF' : C.hl, t === '—' ? C.muted : C.body, 10.5, t !== '—'));
  s.addText('Version one (July–early Sep) used the table only at step 4, as text pasted into the prompt. The three systems on the next slides were run under that version; the four-layer version was then tested layer by layer.', { x: 0.5, y: 4.3, w: 9, h: 0.7, fontSize: 12.5, fontFace: F, color: C.body });
}

// ---------- 4 Agent run
{
  const s = base('The Agent step is real analysis: sealed container, read-only data, Python written and run, a structured answer submitted, for one to two cents',
`SAY: One run is one fresh container: no network, data read-only, five tools, a hard submit call. The model is gpt-5.6-luna through OpenRouter at medium reasoning. Typical run: 12 to 20 tool calls, about a minute, under two cents. It genuinely computes: it matched all 90 SAXS points in the nanodisc case and reproduced the four ADK endpoint changes to four decimals. So the cost of an experiment is scoring time, not money.
GRILL: "Can it see the rubric or the other arm's files?" No. Three directories are mounted separately and a test asserts the control arm's directory has no rule files.`,
'Luna runtime v1; 74 four-layer runs, $1.20 total; ~90 min model time');
  table(s, [
    ['What the run gets', 'What it cannot do', 'What is logged'],
    ['read-only data · source card · question', 'reach the network', 'every tool call and its output'],
    ['5 tools: list · read · run Python · note · submit', 'see the hidden rubric or the other arm\'s files', 'the submitted structured answer'],
    ['≤ 40 tool calls · ≤ 25 min · ≤ 160k input tokens', 'overwrite a submitted answer with chat text', 'cost per run, settled from provider receipts'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 12.5, rowH: 0.5, colW: [3.3, 2.9, 2.8] });
  callout(s, 0.5, 3.35, 9, 1.4, 'Why the Agent stays in the design: G4 asks whether an agent can lower curation cost without adding unsafe claims. It is the last of the four goals and is allowed to fail on its own. The question we are testing is not "can it analyse" (it can) but "what information given to it produces a measurable gain".', 13);
}

// ---------- 5 HSP90 paper vs ours, round 1
{
  const s = base('HSP90 (Henot 2022): the paper visualises a transiently populated closed state; we tested one property, direction persistence in the 40 trajectories, and the rules-in-prompt arm imported FRET conditions',
`SAY: Left: what the paper is. Henot et al. combine NMR with 40 one-microsecond MD trajectories, 20 from the open crystal structure and 20 from a closed model, to argue that the closed state of the HSP90 N-terminal domain is transiently populated. Their classification of the 20 closed-start runs is 7 near-closed, about 9 toward open, 4 neither, using native NOE violations. They report millisecond exchange by CPMG. Right: we chose one property: does a trajectory show a sustained open direction, and does it ever reverse. Result 10 of 20, decomposed 5 initially plus 5 later; reversal candidates 5/4/1 at three run lengths; zero for open-start. Gap: our counts answer a different question than the paper's 7/9/4, so they need not match. Bottom: the rules acted at step 4 as prompt text; three of four answers got the counts right, and the two rule answers imported RMP restraint and FRET calibration conditions from C001-003 and C003-002.
GRILL: "Is 10 consistent with 9?" Different criteria; the crosswalk on the next slide is where the two meet.`,
'Henot et al. 2022 Nat Commun 13:7601; HSP90_Q01_VERIFIED_REPORT_ZH.md; 4 answers, $0.076', 18);
  table(s, [
    ['Paper', 'What we computed (same 40 trajectories)', 'Gap / relation'],
    ['NMR + 40 × 1 µs MD; closed state transiently populated; CPMG exchange ~ms', 'Sustained open-direction classification per trajectory (two difference readouts, 5-point run length)', 'same data, different question'],
    ['Closed-start 20: 7 near-closed / ~9 toward open / 4 neither (native NOE violations + clustering)', 'Closed-start 20: 10 open-direction = 5 initially + 5 later; 10 never; open-start 0/20 reverse', 'not the same partition; counts need not match'],
    ['Authors do not claim populations or rates from MD (non-ergodic)', 'Reversal candidates after first sustained direction: 5 / 4 / 1 at 5 / 20 / 50 points', 'we also do not claim populations or rates'],
  ], { x: 0.5, y: 1.25, w: 9, fontSize: 11, rowH: 0.55, colW: [3.3, 3.6, 2.1] });
  label(s, 0.5, 3.35, 9, 'Where the table acted: step 4, rules rendered as prompt text (7 rules → 8 obligations)');
  table(s, [
    ['Answer', 'Rules in prompt', 'Main counts', 'Imported inapplicable conditions'],
    ['A1 / A2', 'no', 'correct / mixed 5-pt and 50-pt thresholds', 'none'],
    ['B1 / B2', 'yes', 'correct / correct', 'RMP restraint, prior ensemble, fit objective (from C001-003 smFRET calibration, C003-002 FRET-assisted modeling)'],
  ], { x: 0.5, y: 3.7, w: 9, fontSize: 10.5, rowH: 0.4, colW: [1.0, 1.3, 2.7, 4.0] });
}

// ---------- 6 HSP90 NOE crosswalk
{
  const s = base('HSP90, the measurement that mattered: at 1 Å tolerance, 9 of the 10 open-direction trajectories still violate both NOE references; leaving closed is not arriving at open',
`SAY: The first round's "open direction" is the sign of a difference and says nothing about reaching the open state. So we compared every trajectory with the authors' deposited NOE violation series for both references. At 1 Å, 9 of 10 are still far from both; one partial; none consistent. The open-start controls are 18 of 20 consistent, which validates the tolerance. This matches the paper's phrase that the trajectories "almost satisfy" the open NOEs. What the system-level matching shows: the Agent could reproduce direction counts but nothing in the rules made it ask the arrival question; the crosswalk came from a person going back to the authors' raw observable. That is the framing layer.
GRILL: "Why 1 Å?" Pre-registered 0.5 / 1 / 2. At 0.5 the controls drop to 7/20; at 2 Å three candidates become consistent. All three are reported.`,
'Henot 2022; v4 native NOE crosswalk (author-deposited violation series, column 2), tolerance 1 Å, controls 18/20', 18);
  s.addChart(pptx.ChartType.bar, [
    { name: 'Closed-start, open-direction (n=10)', labels: ['Relative only', 'Partial', 'Consistent with open ref.'], values: [9, 1, 0] },
    { name: 'Open-start controls (n=20)', labels: ['Relative only', 'Partial', 'Consistent with open ref.'], values: [1, 1, 18] },
  ], { x: 0.5, y: 1.3, w: 5.4, h: 3.7, barDir: 'col', barGrouping: 'clustered', chartColors: [C.accent, 'B0B0B0'], showValue: true, dataLabelFontSize: 11, catAxisLabelFontSize: 11, valAxisLabelFontSize: 10, showLegend: true, legendPos: 'b', legendFontSize: 10, valAxisMaxVal: 20, valAxisTitle: 'Trajectories', showValAxisTitle: true, valAxisTitleFontSize: 10 });
  table(s, [
    ['', 'Paper', 'Ours'],
    ['observable', 'native NOE violations', 'same series, per trajectory, 3 tolerances'],
    ['toward open', '~9 of 20', '10 of 20 (direction)'],
    ['reached open', '"almost satisfies"', '0 of 10 at 1 Å; 3 at 2 Å'],
    ['populations, rates', 'not from MD', 'not claimed'],
  ], { x: 6.1, y: 1.3, w: 3.4, fontSize: 10.5, rowH: 0.36, colW: [0.9, 1.15, 1.35] });
  callout(s, 6.1, 3.35, 3.4, 1.55, 'What the matching shows: the Agent reproduced direction counts; no rule made it ask "did it arrive". That question was added by a person. This is the framing layer (A).', 11.5);
}

// ---------- 7 DHFR
{
  const s = base('DHFR (Cetin 2023): the paper links 4′-DTMP\'s recovered inhibition of L28R to closer local contacts; we reproduced the distance direction, after finding that our frozen table carried periodic-boundary artifacts',
`SAY: Paper: trimethoprim loses potency against the L28R DHFR mutant; the analog 4′-DTMP recovers it. Their Table 1 Ki values: WT 4.2 vs 5.1 nM, L28R 65 vs 34 nM. Their MD explanation: 4′-DTMP sits closer to M20-loop and R28 atoms. We chose one property: the specified protein-ligand atom distances, one trajectory per condition, 990 frames. First result was wrong: the frozen table used wrapped coordinates, ligand copies in neighbouring periodic images gave 60 to 90 Å distances, and both Agent answers used them; one called the tail conformational switching. After correcting with the nearest ligand image and cross-checking with VMD to 1e-5 Å: M20-N to O3P goes 8.69 to 4.62 Å in WT and 10.44 to 4.81 in L28R, TMP to 4′-DTMP. Direction matches the paper's Figure 4. Gap: the paper frames hydrogen bonds; we have mean distances, one trajectory each, no angles. What the matching shows: no rule text could have caught the input; the check must sit at step 2 in code. This was a curator-side defect.
GRILL: "Why does DHFR have no experimental constraint on the structure?" It does not; the experiment is kinetics. That is why this system tested the workflow more than the science.`,
'Cetin et al. 2023 (PMC10428214) Table 1, Figs 3–4; dhfr_q01-round-20260910 PBC_VALIDATION.json; ligand_comparison.json', 18);
  table(s, [
    ['Paper', 'Ours (deposited trajectories, 1 per condition, 990 frames)', 'Gap / relation'],
    ['Ki (nM): WT TMP 4.2, 4′-DTMP 5.1; L28R TMP 65.0, 4′-DTMP 34.3', 'not re-measured; quoted as context', 'kinetics, not structure'],
    ['MD: 4′-DTMP closer to M20-loop / R28 atoms; hydrogen-bond network discussed', 'M20 N – ligand O3P mean: WT 8.69 → 4.62 Å; L28R 10.44 → 4.81 Å (TMP → 4′-DTMP); 6 specified pairs all closer', 'direction agrees; distance ≠ H-bond; n = 1, no between-run spread'],
    ['authors\' own analysis code, Fig. 4', 'componentwise nearest ligand image; VMD cross-check max Δ 1.1 × 10⁻⁵ Å', 'implementation verified'],
  ], { x: 0.5, y: 1.25, w: 9, fontSize: 11, rowH: 0.58, colW: [3.2, 3.9, 1.9] });
  label(s, 0.5, 3.45, 9, 'Where the table acted: nowhere useful. No physical check at step 2; at step 4 the Agent saw 60–90 Å and did not object (0/2)');
  callout(s, 0.5, 3.9, 9, 1.05, 'What the matching shows: an input defect is invisible to any reminder text. The original two answers are kept and not scored as science; the corrected numbers are a developer calculation. Consequence: admission (layer B) must run in code before freezing.', 12.5);
}

// ---------- 8 ADK
{
  const s = base('ADK (Orädd 2021): the paper tracks a millisecond ATP-binding response by time-resolved scattering; the deposited apo MD only supports domain-distance descriptions, and it broke my own admission rule',
`SAY: Paper: photorelease of ATP, time-resolved X-ray solution scattering, a transient about 4.3 ms, interpreted with MD-derived candidate structures. Deposited MD: two trajectories, open-start 450 ns and closed-start 335 ns, no ATP or AMP. We chose one property we could actually compute: mean Cα distances between LID or NMP and CORE, first versus last 10% of frames. All four changes positive; distributions overlap. Gap: no ligand, no scattering recomputation, no millisecond process. The system-level lesson: the admission rule I wrote after DHFR, any distance above half the box fails, was itself wrong. Open ADK spans 56 Å along one axis in a 98 to 100 Å box, so 62 and 70 Å Cα distances are real and GROMACS reproduces them. The rule was replaced by a physical criterion. Framing was also used here: the ADK question in the framing test was split into distribution separation, magnitude, ordering; the split version scored 5/5.
GRILL: "Why keep ADK?" It is the only system the rules and selector had never seen, so it is the only source of a generalisation signal, and it is the one Soojung named.`,
'Orädd et al. 2021 Sci Adv 7:eabi5514; Zenodo 5583119; ADK_SCIENCE_ZH.md; ADK_INDEPENDENT_RECOMPUTE.json', 18);
  table(s, [
    ['Paper', 'Ours (deposited apo trajectories)', 'Gap / relation'],
    ['TR-XSS after ATP photorelease, with AMP; transient ~4.3 ms; MD candidates fitted to scattering', 'domain-distance descriptors on CORE 1–29/68–115/168–214, NMP 30–67, LID 118–160 (project definitions)', 'no ATP/AMP, 294 vs 303 K, ns vs ms; scattering not recomputed'],
    ['LID and NMP close cooperatively on ATP binding (their interpretation)', 'first→last 10 %: open-start LID–CORE +2.29, NMP–CORE +0.07 Å; closed-start +1.18, +1.09 Å; distributions overlap', 'no joint closure in these windows; not a test of the paper\'s mechanism'],
    ['—', 'GROMACS cross-check of all specified pairs, all frames: max Δ ≈ 0.005 Å; SciPy re-implementation Δ < 1e-10 Å', 'implementation verified'],
  ], { x: 0.5, y: 1.25, w: 9, fontSize: 10.5, rowH: 0.6, colW: [3.1, 3.9, 2.0] });
  label(s, 0.5, 3.5, 9, 'Where the table acted: step 2 (admission rule flagged legitimate 69.8 / 62.2 Å distances; replaced) and step 3 (question split: 4 → 5 correct units)');
  callout(s, 0.5, 3.95, 9, 1.0, 'Half-box 49–50 Å but open-state extent 56 Å: per-pair minimum image would fold real distances. New criterion: whole reconstructed molecule, adjacent Cα ≤ 4.5 Å, GROMACS Δ ≤ 0.01 Å; half-box exceedance only triggers a note.', 12);
}

// ---------- 9 Retrospective
{
  const s = base('Looking back at 13 error observations in 8 answers: none would have been prevented by reminder text; they sit at data entry and at the numbers going out',
`SAY: Before testing the four layers we audited every historical answer: 13 observations, 7 same-cause groups, correlated, not 13 cases. Grouped by where each lives: input representation, numbers read from the wrong column or threshold, sign of a difference read as arrival, imported conditions. Reminder text prevents none. Code before freezing or after submission could plausibly prevent most; two need the question asked better. This was a candidate attribution; the next slides test it rather than trust it.
GRILL: "Selective?" It is every answer we had, including the nine-September nanodisc runs.`,
'E0_RETROSPECTIVE_AUDIT.csv; E0_COUNTS.json (13 rows, 7 same-cause groups, 3 detected on replay)');
  table(s, [
    ['Error group (where observed)', 'Workflow step', 'Reminder text?', 'What could catch it'],
    ['periodic-image artifact taken as real (DHFR × 2)', '2 Package', 'no', 'physical admission check in code'],
    ['threshold / column mix-ups in counts (HSP90 A2; DHFR A1 percentages)', '5 Check', 'no', 'claim-to-source number check'],
    ['wrong NOE upper-bound array (nanodisc Q05)', '5 Check', 'no', 'bind each claim to raw quantity, unit and transform'],
    ['"open direction" read as "near open state" (HSP90)', '3 Frame', 'partly', 'split: direction / arrival / full transition'],
    ['FRET-only conditions imported (HSP90 B1, B2)', '4 Run', 'text is the cause', 'retrieve guidance by operation, not method name'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11.5, rowH: 0.5, colW: [3.3, 1.2, 1.5, 3.0] });
}

// ---------- 10 Four layers: what info the agent gets
{
  const s = base('So the 33 rules were split by job into four layers; the design question became: what information reaches the Agent, in what form, at which step',
`SAY: This is the current design and it is a direct answer to your original question, how the Agent should use the table. Framing: 6 rules become sub-questions and rubric, never shown. Admission: 10 rules become code before freezing, reaching the Agent only as a card of results. Method cards: 11 rules become short cards retrieved by method family, the only text the Agent reads. Conclusion: 6 rules become an automatic check after submission with one feedback. Each layer changes one thing about what the Agent receives, so each can be tested on its own.
GRILL: "Is the split arbitrary?" It follows rule_class in the table; the 6/10/11/6 assignment is in the appendix and can be argued rule by rule.`,
'RULES_TABLE_ROLE_DESIGN_ZH.md §2; classification by rule_class, 6 / 10 / 11 / 6');
  table(s, [
    ['Layer', 'Question it answers', 'Executed by, when', 'What the Agent receives', 'Rules'],
    ['A Framing', 'which difference must this question distinguish; which sub-questions; what competing explanations', 'person + template, before the run', 'nothing directly: the question text and the hidden rubric', '6'],
    ['B Admission', 'can these data answer it: object, condition, units, time, evidence role, physics', 'code, before freezing', 'a card of PASS / FAIL results in the data directory', '10'],
    ['C Method cards', 'how should this kind of data be computed: forward model, averaging, reweighting prerequisites', 'retrieval by method family, at run time', 'short cards, ≤ 10 lines each, the only rule text it sees', '11'],
    ['D Conclusion', 'how far can this result be read: frames ≠ populations, fit ≠ validation, proximity ≠ state', 'code, after submission', 'one feedback message, may revise once', '6'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.7, colW: [1.2, 3.0, 1.7, 2.6, 0.5] });
}

// ---------- 11 What each layer measured and why
{
  const s = base('Each layer got its own falsifiable test: what changed, what we expected to see if the layer helps, and the criterion written down before running',
`SAY: This is the 前因后果 of the three questions we measured. Framing: from HSP90 we knew the Agent answered the direction question but never the arrival question; expected: splitting the question raises supported coverage without adding overclaims. Admission: from DHFR we knew a bad table passed; the checker was tested on six planted defects, and the Agent was given or not given the card on the defective DHFR table; expected: it downgrades its conclusions. Method cards: from HSP90 B1/B2 we knew full rules imported conditions; expected: scoped cards keep accuracy and stop the imports, against a seven-line protocol. Conclusion: from A2 and Q05 we knew numbers went out wrong; expected: one automated pass reduces core errors without more omissions. Same model, four runs per condition, frozen, blinded, medians.
GRILL: "Why medians of four?" Small by design; enough for an investment decision, not for a rate.`,
'FOUR_LAYER_VALIDATION_PLAN_ZH.md v2; frozen before first call; 74 runs, $1.20; scorer = curator (masked labels)', 18);
  table(s, [
    ['Layer', 'Trigger (what we had seen)', 'Only thing that differs', 'Questions · runs', 'Expected if it helps (pre-set criterion)'],
    ['A Framing', 'HSP90: direction answered, arrival never asked', 'original question vs explicit sub-questions', 'HSP90, ADK · 16', 'coverage up on 2/2, overclaims not up'],
    ['B Admission', 'DHFR: wrapped table passed into the run', 'admission card present vs absent; checker on 6 planted defects + 3 clean packages', 'DHFR defective · 8', 'checker ≥ 5/6, 0 false alarms; Agent downgrades more with card'],
    ['C Method cards', 'HSP90 B1/B2: FRET conditions imported', '7-line protocol vs full rules vs scoped cards', 'HSP90 NOE, nanodisc Q05 · 24', 'cards non-inferior to both on both questions; 0 inapplicable terms'],
    ['D Conclusion', 'A2 thresholds; Q05 wrong NOE bound', 'no feedback vs one automated pass', 'HSP90, DHFR fixed, ADK · 24', 'fewer core errors on ≥ 2/3, omissions not up'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 10.5, rowH: 0.62, colW: [1.1, 2.1, 2.3, 1.5, 2.0] });
  s.addText('Scored on five frozen core units per question, plus core errors, overclaims, omissions, defect detection; answers de-labelled, scores sealed before unblinding.', { x: 0.5, y: 4.55, w: 9, h: 0.5, fontSize: 11.5, fontFace: F, color: C.muted });
}

// ---------- 12 Results
{
  const s = base('Result: only explicit sub-questions met its criterion; the admission card, method cards and one feedback pass did not',
`SAY: Framing: coverage HSP90 2 to 2.5 of 3, ADK 2 to 3 of 3, no new overclaims; keep. HSP90's total errors across four runs went 1 to 2, so the gain is completeness, not uniformly accuracy. Admission: checker caught all six planted defects, but the Agent detected the DHFR defect 0 of 4 with the card and 0 of 4 without. Method cards: HSP90 protocol 4.5 of 5, full rules 2, cards 2.5; Q05 4.5, 5, 4.5. Cards failed. The exception to keep on record: full rules were best on Q05, all four answers covered all five units. Feedback: only ADK improved, and that difference already existed in the initial drafts; no revision reduced its own errors; three lost content.
GRILL: "So the table is useless?" The prompt form is not supported. The library is still the raw material for checks and cards, and Q05 is one case where the full text helped. What we cannot claim is a stable increment.`,
'UNBLINDED_SCORES.csv medians of 4; FINAL_DECISIONS.json; RULES_TABLE_VERDICT_EN.md', 20);
  table(s, [
    ['Layer', 'Observed (median of 4 unless stated)', 'Met?', 'Decision'],
    ['A Framing', 'coverage HSP90 2 → 2.5 /3, ADK 2 → 3 /3; overclaims 0 → 0; HSP90 total errors 1 → 2 over 4 runs', KEEP, 'keep: ask direction, magnitude and limits separately'],
    ['B Admission', 'checker 6/6 planted defects, 0/3 false alarms; Agent detected the defect 0/4 with card, 0/4 without; all 4 card runs listed the file, none read it', NO, 'move admission into data preparation; never rely on the Agent finding a warning file'],
    ['C Method cards', 'correct units /5 — HSP90: protocol 4.5 · full rules 2 · cards 2.5; Q05: 4.5 · 5 · 4.5', NO, 'pause; retrieve by operation, not method family; keep the Q05 full-rule benefit on record'],
    ['D Conclusion', '1/3 questions improved (ADK), already better in initial drafts; 0/12 revisions reduced errors; 3 lost content; 0/9 warnings hit a real error', NO, 'pause; number matching cannot catch numbers already wrong in the logs'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.72, colW: [1.2, 4.2, 0.7, 2.9] });
}

// ---------- 13 Why each failed
{
  const s = base('Why each layer failed matters more than that it failed: delivery, applicability and traceability are three different problems',
`SAY: Three mechanisms. The card was available but never opened: a file is not a channel. Retrieval by method family gave HSP90 a BME reweighting card for a task that fits nothing; family membership is not operation applicability; and DHFR and ADK retrieved zero cards, the 11 papers do not cover pure-MD questions. The conclusion checker asks whether a number appears in the tool output; in Q05 the wrong bound array was written to the log first, so the wrong 4.35 Å passed; on 8 historical answers it caught 0 of 7 known errors. Each of these points at a specific repair, which is what slide 14 is about.
GRILL: "Why not a stronger model?" The worst errors are in inputs the model cannot see, and number errors need recomputation from raw quantities; both are pipeline problems.`,
'E1B_CARD_ACCESS_AUDIT.json; E3_CARD_RETRIEVAL.json; METHOD_CARD_DESIGN_ANALYSIS_ZH.md; E0_CEILING_REPLAY_REVIEW_ZH.md');
  table(s, [
    ['Layer', 'Mechanism observed', 'Repair it points to'],
    ['B Admission card', 'tool logs: card file listed in 4/4 runs, contents read in 0/4', 'block bad tables at step 2; a warning file is not a channel'],
    ['C Method cards', 'HSP90 retrieved 1 card, a BME/MaxEnt reweighting card, for a task that fits no weights; Q05 retrieved 4 incl. FRET-specific; DHFR and ADK retrieved 0', 'index cards by the operation being performed and its prerequisites; cover MD-only operations'],
    ['D Conclusion check', 'checks whether a number appears in tool output; the wrong Q05 bound array was already in the log, so 4.35 Å passed; replay on 8 answers: 0/7 caught, 1 false alarm (the −1 in Å⁻¹)', 'bind each claim to raw quantity, unit and transform; recompute, do not string-match'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11.5, rowH: 0.85, colW: [1.6, 4.4, 3.0] });
}

// ---------- 14 Design options
{
  const s = base('How the Rules Table should be built from here: three forms, what each assumes, and what this round\'s evidence says about each',
`SAY: Back to your original idea: an Agent that enters the table and follows rules to choose operations and extra analyses. Three forms of that. Form 1: keep the four layers and repair each with the mechanism from slide 13, then retest on new questions; assumes the failures were implementation, not concept. Form 2: rules serve the people who write the protocol and rubric; the Agent gets a seven-line protocol; this is what the current evidence directly supports, since the protocol arm was never worse, but it gives up the original idea. Form 3: each rule becomes the configuration of a deterministic operator: an admission check, a computation, a claim-ceiling test; the Agent decides which operator to call and never reads rule text. This is closest to the original idea, and closest to what DHFR and ADK taught, but nothing of it has been tested yet.
ASK: which of these is the knowledge form you want the group to accumulate? I lean to 3 with 2 as the fallback baseline that every version must beat.`,
'Original idea: slide 2; evidence: slides 12–13; SYSTEM.md authority split (Agent proposes, deterministic system validates)', 19);
  table(s, [
    ['Form', 'What the Agent gets', 'Assumes', 'This round\'s evidence', 'Untested'],
    ['1  Repair the four layers', 'admission card delivered in the question, operation-indexed cards, recompute-based check', 'failures were implementation, not concept', 'A supported; B, C, D failed in current form; mechanisms identified', 'every repair'],
    ['2  Rules serve the protocol writer', 'a 7-line protocol only; rules used by people for rubric and admission', 'human-written protocol captures what matters', 'protocol arm never worse (HSP90 4.5/5, Q05 4.5/5)', 'whether it scales past three systems'],
    ['3  Rules as operator configuration', 'a catalogue of callable, registered operators; Agent proposes which to call, code executes and bounds the claim', 'every useful rule can be made executable', 'DHFR and ADK: the checks that mattered were physical and executable', 'the whole form'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.78, colW: [1.7, 2.5, 1.7, 2.1, 1.0] });
  callout(s, 0.5, 4.55, 9, 0.5, 'My lean: build toward 3, keep 2 as the baseline every version must beat on new questions. Your call.', 12.5);
}

// ---------- 15 Are the three systems right
{
  const s = base('Are the three systems the right ones? By the criterion "MD plus an experiment that constrains the difference we want to distinguish", only HSP90 fully qualifies',
`SAY: The criterion I propose: a system needs MD and an experimental observable that constrains the difference the question is about. HSP90 has two NOE references and CPMG. DHFR has kinetics only; it tested the workflow, not the science. ADK has time-resolved scattering, but the deposited MD is apo and 300 nanoseconds against a millisecond process. ADK still has one unique value: it was the only system the rules and selector had never seen. The question for you: is this the right criterion, and is there a candidate with MD plus NMR, SAXS or smFRET populations that the group cares about?
GRILL: "Should DHFR be dropped?" As a science system yes; as a workflow regression test it earned its keep by exposing the admission gap.`,
'Slides 5–8; PROJECT_MEMORY G1–G4; 24 Aug meeting: HSP90 first, one system at a time', 19);
  table(s, [
    ['System', 'Paper\'s result', 'Our result', 'Experimental constraint on the question', 'What it tested', 'Keep?'],
    ['HSP90', 'transient closed state; 7/9/4 classification; ms exchange', '10/20 direction; 9/10 relative-only at 1 Å; no populations', 'yes: two NOE references, CPMG', 'science + framing + prompt form', { text: 'yes, deepen', options: { color: C.green, bold: true } }],
    ['DHFR', '4′-DTMP recovers L28R inhibition; closer local contacts', 'same direction, 8.69 → 4.62 Å (WT), n = 1', 'no: Ki only, no structural observable', 'workflow: exposed missing admission', { text: 'as regression test only', options: { color: C.muted, bold: true } }],
    ['ADK', 'ms ATP-binding response by TR-XSS; MD candidates', 'apo domain distances overlap; +2.29 Å LID (open start)', 'partly: TR-XSS exists, but deposited MD is apo, ns', 'admission rule (broke it); framing; only unseen system', { text: 'keep as unseen control', options: { color: C.accent, bold: true } }],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 10.5, rowH: 0.7, colW: [0.8, 2.0, 2.0, 1.9, 1.5, 0.8]});
  callout(s, 0.5, 4.3, 9, 0.7, 'Ask: a fourth system with MD plus an experiment that constrains populations (NMR / SAXS / smFRET)? Any candidate from the group\'s own work?', 12.5);
}

// ---------- 16 Conclusions + asks
{
  const s = base('Conclusions, and the three things I need from you',
`SAY: Three sentences. The three systems produced bounded, checkable results; HSP90 is the strongest and is a real cross-source comparison. The table as prompt text did not earn its place; its content is still the raw material for executable checks and operation-indexed guidance, and framing the question explicitly is the one layer that measurably helped. The next build should put physical admission inside data preparation, make rules executable where they can be, and be tested against the seven-line protocol on new questions with independent scoring.
Leave this slide up for discussion.`,
'Full evidence and all 74 runs: github.com/alex051107/dynamics-atlas-harness/pull/27');
  bullets(s, [
    'Workflow (slide 3): a new system goes intake → package → frame → run → check → report; the table can act at steps 2–5, and the evidence says step 2 (in code) and step 3 (by a person) are where it earns its place.',
    'Three systems: HSP90 gave a real cross-source result (direction ≠ arrival); DHFR and ADK are single-source MD descriptions that exposed two admission defects, one of them in my own rule.',
    'Four-layer test, 74 runs: only explicit sub-questions met its criterion; card delivery, method-family retrieval and number matching each failed for an identified reason.',
  ], { y: 1.3, h: 2.3, fontSize: 14 });
  callout(s, 0.5, 3.65, 9, 1.3, 'Decisions for today\n1. Is the workflow on slide 3 reasonable? What would you reorder, cut or add?\n2. Which form of the table (slide 14) should we build toward: repair the four layers, rules for the protocol writer, or rules as operator configuration?\n3. Are HSP90 / DHFR / ADK the right systems by the criterion on slide 15, and is there a fourth with MD plus population-constraining experiment?', 12.5);
}

// ---------- 17 References
{
  const s = base('References', null, null);
  bullets(s, [
    'Henot F. et al. (2022) Visualizing the transiently populated closed-state of human HSP90 ATP binding domain. Nat Commun 13, 7601. doi:10.1038/s41467-022-35399-8',
    'Cetin E. et al. (2023) DHFR L28R / TMP and 4′-DTMP study. J Chem Inf Model; PMC10428214; data Zenodo 7966540; authors\' code github.com/midstlab/JCIM_Cetin_etal_2023',
    'Orädd F. et al. (2021) Tracking the ATP-binding response in adenylate kinase in real time. Sci Adv 7, eabi5514. doi:10.1126/sciadv.abi5514; data Zenodo 5583119',
    'Bengtsen T. et al. (2020) Structure and dynamics of a nanodisc by integrating NMR, SAXS and SANS experiments with MD. eLife 9, e56518',
    'Li, Thomasen, Cossio (2026) Are we capturing the ensemble? RS Station blog, 31 Aug 2026',
    'Bhakat S. (2026) Benchmarking generative AI and physics-based simulation for conformational heterogeneity in T4 lysozyme. J Chem Inf Model. doi:10.1021/acs.jcim.6c02044',
    'Rule sources (11): Hellenkamp 2018; Agam 2023; Dimura 2020; Fuertes 2017; Shevchuk 2017; Bengtsen 2020; Hoff 2024; Peter 2022; Sanabria 2020; Steffen 2021; Wankowicz & Bonomi 2026 — full locators in rule_registry.tsv',
  ], { fontSize: 11.5, paraSpaceAfter: 5 });
}

// ---------- Appendix
{
  const s = pptx.addSlide(); n += 1;
  s.background = { color: C.primary };
  s.addText('Appendix', { x: 0.7, y: 2.1, w: 8.6, h: 0.8, fontSize: 30, fontFace: F, color: 'FFFFFF', bold: true });
  s.addText('A1 what the evidence can and cannot support · A2 all 33 rules by layer · A3 scores per condition · A4 cost · A5 terms', { x: 0.7, y: 2.9, w: 8.6, h: 0.5, fontSize: 13, fontFace: F, color: 'A0BBDD' });
}
{
  const s = base('A1. What this evidence can and cannot support', null, 'METHODS_AND_LIMITS_ZH.md; DEVIATIONS.md');
  table(s, [
    ['Can say', 'Cannot say'],
    ['pasting rules into the prompt showed no gain on 2 questions and one concrete harm', 'that rules are useless in general'],
    ['explicit sub-questions raised coverage on 2/2 questions without new overclaims', 'that the Agent discovers sub-questions on its own'],
    ['the current checker and card retrieval did not meet pre-set criteria; mechanisms identified', 'a population-level correctness rate for any condition'],
    ['HSP90: leaving closed ≠ reaching open, at three tolerances', 'populations or rates for HSP90; H-bonds or mechanism for DHFR; anything about ADK\'s ATP response'],
    ['74 runs, $1.20, all preserved with logs and sealed scores', 'independent expert scoring (not done); human time saved (not measured); scorer ≠ curator'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 12, rowH: 0.55, colW: [4.5, 4.5] });
}
{
  const s = base('A2. All 33 rules, grouped by the layer they now belong to', null, 'rule_registry.tsv; RULES_TABLE_ROLE_DESIGN_ZH.md §2');
  table(s, [
    ['Layer', 'Rule IDs (rule_class)'],
    ['A Framing (6)', 'C010-001 claim_ladder · C010-002 state_semantics · C005-001 estimand_non_equivalence · C009-003 estimand_non_equivalence · C012-001 benchmark_contract · C012-002 identifiability'],
    ['B Admission (10)', 'C001-001 measurement_semantics · C002-001 measurement_semantics · C001-002 uncertainty_provenance · C001-003 measurement_quality · C008-001 source_quality · C007-001 multi_source_semantics · C009-001 cross_validation · C009-002 diagnostic_controls · C003-001 candidate_design · C003-003 held_out_validation'],
    ['C Method cards (11)', 'C002-002, C006-001, C008-003 forward_bridge · C011-001 forward_implementation · C005-003 inverse_model · C003-002 reweighting · C007-002 integration_operator · C006-002 uncertainty_integration · C011-002 uncertainty_decomposition · C002-003, C008-002 artifact_exclusion'],
    ['D Conclusion (6)', 'C006-003, C011-003, C012-003 claim_ceiling · C005-002 complementary_evidence · C007-003 integration_validation · C010-003 functional_validation'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.8, colW: [1.6, 7.4] });
}
{
  const s = base('A3. Median scores per question and condition (n = 4 each)', null, 'UNBLINDED_SCORES.csv; medians recomputed locally from the unblinded table');
  table(s, [
    ['Test', 'Question', 'Condition', 'Correct /5', 'Errors', 'Overclaims', 'Omissions /5', 'Coverage /3'],
    ['Admission', 'DHFR defective', 'no card / card', '3 / 2', '1 / 2.5', '1 / 2', '1 / 0', '—'],
    ['Feedback', 'ADK', 'none / one pass', '4 / 4', '0.5 / 0', '0 / 0', '1 / 1', '—'],
    ['Feedback', 'DHFR corrected', 'none / one pass', '4 / 3', '0 / 0.5', '0 / 0', '0.5 / 1.5', '—'],
    ['Feedback', 'HSP90 NOE', 'none / one pass', '3 / 3.5', '0 / 0.5', '0 / 0', '1 / 0.5', '—'],
    ['Method guidance', 'HSP90 NOE', 'protocol / full rules / cards', '4.5 / 2 / 2.5', '0 / 1.5 / 0.5', '0 / 0 / 0', '0.5 / 1 / 0.5', '—'],
    ['Method guidance', 'nanodisc Q05', 'protocol / full rules / cards', '4.5 / 5 / 4.5', '0.5 / 0 / 0.5', '0 / 0 / 0', '0 / 0 / 0', '—'],
    ['Framing', 'HSP90 Q01', 'original / split', '2.5 / 3', '0 / 0', '0 / 0', '2 / 1.5', '2 / 2.5'],
    ['Framing', 'ADK', 'original / split', '4 / 5', '0 / 0', '0 / 0', '1 / 0', '2 / 3'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.36, colW: [1.3, 1.4, 1.9, 1.1, 1.0, 0.9, 0.9, 0.5] });
}
{
  const s = base('A4. Cost and run ledger', null, 'CAMPAIGN_PROGRESS.json; COST_RECONCILIATION.json');
  table(s, [
    ['Batch', 'Runs', 'Settled cost (USD)', 'Cap'],
    ['Historical: HSP90 first round (4), DHFR (2), old A/B/C (8), D/P/R pilot (2)', '16', '0.2855', '—'],
    ['Admission card comparison', '8', '0.1469', '0.20'],
    ['Plain ADK', '2', '0.0233', '0.15'],
    ['One-feedback comparison', '24', '0.3858', '0.55'],
    ['Method-guidance comparison', '24', '0.4158', '0.55'],
    ['Question decomposition', '16', '0.2312', '0.40'],
    ['Four-layer total', '74', '1.2029', '1.85'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 12.5, rowH: 0.4, colW: [5.2, 0.9, 1.7, 1.2] });
  s.addText('Model wall time for the 74 runs ≈ 90 minutes. Scoring, cross-checks and report writing were the actual cost.', { x: 0.5, y: 4.6, w: 9, h: 0.4, fontSize: 11.5, fontFace: F, color: C.muted });
}
{
  const s = base('A5. Terms as used in this deck', null, null);
  table(s, [
    ['Term', 'Meaning here'],
    ['Rule', 'one caution from one methods paper: finding, required check, abstain route, transfer scope'],
    ['Selector / obligation', 'code that matches rules to a question by method family and renders them as required checks'],
    ['Agent run', 'one sealed container session of the LLM: reads data, writes Python, submits a structured answer'],
    ['Frozen', 'question, rubric, code and run order hashed before the first model call; changes void the experiment'],
    ['Core unit', 'one of five predefined pieces of scientific content the rubric expects; scored correct / wrong / missing'],
    ['Overclaim', 'a stated conclusion stronger than the evidence supports (e.g. frame fraction as population)'],
    ['Exposed case', 'a question or dataset already used during development; cannot serve as an independent test'],
    ['Admission', 'checks that the data can answer the question: object, condition, units, time, evidence role, physics'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.36, colW: [1.8, 7.2] });
}

pptx.writeFile({ fileName: OUT }).then(f => console.log('wrote', f, 'slides', n));
