const path = require('path');
const NM = '/Users/liuzhenpeng/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules';
const pptxgen = require(path.join(NM, 'pptxgenjs'));
const OUT = process.argv[2];
const FIG = process.argv[3]; // directory with figures

const C = { bg: 'FFFFFF', primary: '1F4E79', accent: '2E75B6', body: '2D2D2D', muted: '777777', rule: 'CCCCCC', hl: 'FFF2CC', red: 'C0392B', green: '2E7D32', pale: 'E8EEF5', grey: 'F2F2F2' };
const F = 'Arial';
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_16x9';
pptx.author = 'Zhenpeng Liu';
pptx.title = 'Dynamics Atlas: the Rules Table, tested on three systems';

let n = 0;
function base(title, notes, source, titleSize) {
  if (!titleSize) titleSize = title.length > 120 ? 19 : 21;
  const s = pptx.addSlide(); n += 1;
  s.background = { color: C.bg };
  s.addText(title, { x: 0.5, y: 0.25, w: 9, h: 0.95, fontSize: titleSize, fontFace: F, bold: true, color: C.primary, valign: 'top' });
  if (source) s.addText(source, { x: 0.5, y: 5.18, w: 8.4, h: 0.3, fontSize: 10, fontFace: F, color: C.muted });
  s.addText(String(n), { x: 9.2, y: 5.18, w: 0.3, h: 0.3, fontSize: 10, fontFace: F, color: C.muted, align: 'right' });
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
function fig(s, file, x, y, w, h, caption) {
  s.addImage({ path: path.join(FIG, file), x, y, w, h, sizing: { type: 'contain', w, h } });
  if (caption) s.addText(caption, { x, y: y + h + 0.02, w, h: 0.42, fontSize: 9, fontFace: F, color: C.muted });
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
  s.addText('The idea and the workflow (6 min) · three systems through it (10) · what each layer measured (7) · how to build it: discussion (7)', { x: 0.7, y: 4.4, w: 8.6, h: 0.6, fontSize: 12.5, fontFace: F, color: 'A0BBDD' });
  s.addNotes(`SAY: Last time you knew I was building a Rules Table prototype. Today I want to discuss how the whole system should be built. I'll show the original idea, the workflow a new system goes through, what happened when three real systems went through it, what each layer of the table measured, and three design options for the table. Headline first: putting rules into the AI's prompt did not help on the two questions where we tried it. Most of the errors we could locate sat at data entry or in the reported numbers; that audit is retrospective, not a controlled test. The one use that met its pre-set criterion was framing the question explicitly, and that part is done by a person.
GOAL: (1) is the workflow reasonable; (2) are the three systems right; (3) which form of the table to build toward.`);
}

// ---------- 2 Original idea + what the table is
{
  const s = base('The original idea: an AI analyst enters the Rules Table and follows the rules to choose operations and extra analyses',
`SAY: This was the idea from July. A question and a data package come in. The AI analyst, I'll call it the Agent, consults a table of rules distilled from methods papers. The rules tell it which operations to run, which extra analyses to add, and where it must stop and abstain. The table has 33 rules from 11 papers, three per paper. Each rule stores what the paper showed, what we must check before using that kind of data, what the check needs, and where to stop. Bottom right is one rule verbatim, from Shevchuk's Bayesian SAXS paper.
GRILL "who wrote them": I did, in August, from deep reads. An external review on 17 August asked to keep the table as a reviewable ledger, not an engine.`,
'rule_registry.tsv v0.1; 11 papers (Hellenkamp 2018 … Wankowicz & Bonomi 2026); external review 17 Aug 2026');
  const y = 1.35;
  box(s, 0.5, y, 1.55, 0.85, 'New system:\nquestion + data', C.pale, C.primary, 11.5);
  arrow(s, 2.1, y + 0.3);
  box(s, 2.45, y, 1.7, 0.85, 'Rules Table\n33 rules / 11 papers', C.hl, C.body, 11.5, true);
  arrow(s, 4.2, y + 0.3);
  box(s, 4.55, y, 1.9, 0.85, 'Agent follows rules:\nwhich operation, what\nextra analysis, when to stop', C.pale, C.primary, 10.5);
  arrow(s, 6.5, y + 0.3);
  box(s, 6.85, y, 1.4, 0.85, 'Analysis +\nnumbers', C.pale, C.primary, 11.5);
  arrow(s, 8.3, y + 0.3);
  box(s, 8.65, y, 0.85, 0.85, 'Bounded\nanswer', C.grey, C.body, 11);
  label(s, 0.5, 2.4, 4, 'What one rule stores');
  table(s, [
    ['Field', 'Meaning'],
    ['paper finding', 'what the paper actually showed'],
    ['project rule', 'what we must check before using this kind of data'],
    ['required items', 'the pieces of information the check needs'],
    ['stop route', 'where to stop if the check cannot be done'],
    ['transfer scope', 'how far the lesson carries'],
  ], { x: 0.5, y: 2.72, w: 4.3, fontSize: 11, rowH: 0.3, colW: [1.5, 2.8] });
  label(s, 5.1, 2.4, 4.4, 'One rule verbatim (C006-RULE-003, Shevchuk 2017)');
  s.addText([
    { text: 'Finding: ', options: { bold: true } }, { text: 'if the candidate structures omit a state, Bayesian SAXS refinement can express uncertainty within the wrong set but cannot create the missing state.', options: { breakLine: true } },
    { text: 'Check: ', options: { bold: true } }, { text: 'coverage of the candidate set · number of states · missing-state audit.', options: { breakLine: true } },
    { text: 'Stop route: ', options: { bold: true } }, { text: 'MISSING_STATE_SUPPORT.', options: { breakLine: true } },
    { text: 'Scope: ', options: { bold: true } }, { text: 'a posterior cannot create a state absent from the candidates.' },
  ], { x: 5.1, y: 2.72, w: 4.4, h: 2.3, fontSize: 11, fontFace: F, color: C.body, valign: 'top', paraSpaceAfter: 5 });
}

// ---------- 3 Workflow for a new system
{
  const s = base('What a new system goes through today: six steps, and the table can act at four of them',
`SAY: Left to right. Intake: download the authors' deposited data and write a source card, a one-page record of paper, SI, README, frame counts, units. Package: derived tables such as per-frame distances, field definitions, physical checks, then freeze. Freezing means hashing question, grading key and code before the first model call so nothing is tuned afterwards. Frame: a person decides which difference the question must distinguish and writes the grading key, the list of what a correct answer must contain. Run: the Agent works in a sealed container. Check: automatic checks on what it submitted. Report: every number linked to source, the claim limit in words. The bottom row shows where the table can act: data checks at step 2, question framing at step 3, method guidance at step 4, conclusion checks at step 5. Before September we tested whether the selector picked the right checks: 41 of 41 pre-registered checks, among 146 generated. That is selection coverage, not scientific help. When the three systems ran, the table reached the Agent only at step 4, as selected rules pasted into the prompt.
GRILL "where is the person": steps 1, 3, 6. Step 3 cannot be delegated: the competing explanations.`,
'Terms: source card = one-page data record; freeze = hash everything before the first model call; grading key = what a correct answer must contain');
  const steps = [
    ['1 Intake', 'authors\' deposition\n+ source card\n(paper, SI, README)'],
    ['2 Package', 'derived tables,\nfield definitions,\nphysical checks, freeze'],
    ['3 Frame', 'sub-questions,\ncompeting explanations,\ngrading key (hidden)'],
    ['4 Run', 'Agent in sealed\ncontainer: reads,\ncomputes, submits'],
    ['5 Check', 'automatic checks\non the submission,\none feedback'],
    ['6 Report', 'numbers linked to\nsource; claim limit\nin words'],
  ];
  const w = 1.38, gap = 0.14, y = 1.35;
  steps.forEach((st, i) => {
    const x = 0.5 + i * (w + gap);
    box(s, x, y, w, 0.34, st[0], C.primary, 'FFFFFF', 11.5, true);
    box(s, x, y + 0.34, w, 1.0, st[1], C.pale, C.body, 9.5);
    if (i < 5) arrow(s, x + w - 0.02, y + 0.5, gap + 0.04);
  });
  const who = ['person + script', 'script + checks', 'person + template', 'Agent', 'code', 'script + person'];
  who.forEach((t, i) => box(s, 0.5 + i * (w + gap), y + 1.42, w, 0.3, t, C.grey, C.muted, 9.5));
  const layer = ['—', 'data checks\n(10 rules)', 'question framing\n(6 rules)', 'method guidance\n(11 rules)', 'conclusion checks\n(6 rules)', '—'];
  label(s, 0.5, 3.2, 5, 'Where the Rules Table can act (four uses; defined on slide 12)');
  layer.forEach((t, i) => box(s, 0.5 + i * (w + gap), 3.55, w, 0.6, t, t === '—' ? 'FFFFFF' : C.hl, t === '—' ? C.muted : C.body, 10.5, t !== '—'));
  s.addText('Before September the tests asked whether the selector picked the right checks (41/41 pre-registered checks selected among 146 generated), not whether answers improved. When the three systems ran, the table reached the Agent only at step 4, as selected rules pasted into the prompt.', { x: 0.5, y: 4.3, w: 9, h: 0.7, fontSize: 12.5, fontFace: F, color: C.body });
}

// ---------- 4 Cases and comparison design
{
  const s = base('How anything here was tested: four cases, a criterion for choosing them, and the same comparison design throughout',
`SAY: Before the systems, the vocabulary. Four cases appear in this talk. HSP90, DHFR and ADK are the systems you named; the nanodisc is a development case from Bengtsen's paper that we used in September to check that the Agent can compute at all, and it reappears in the later tests. The criterion I propose for a system: it needs MD plus an experiment that constrains the very difference the question is about; among the three systems you named only HSP90 fully qualifies; the nanodisc qualifies too but is a development case, and its cross-observable result is in appendix A6. I will come back to this on slide 17. The comparison design is always the same: same question, two or three conditions, four fresh runs per condition. A condition, or arm, differs in exactly one thing, for example rules in the prompt or not. Answers are scored against a grading key written from the public question, the data and the paper, frozen before the first run, never from the rules. Each question has five core units, the pieces a correct answer must contain, and we count units correct, errors, overclaims and omissions. Scoring is done on de-labelled answers and compared as medians of four.
GRILL "why four": enough for an investment decision, not for a rate.`,
'Nanodisc: Bengtsen et al. 2020 eLife, NMR + SAXS + SANS + MD; Q05 = one question on it, exposed during development');
  table(s, [
    ['Case', 'Data we have', 'Experiment that constrains the question?', 'Role in this talk'],
    ['HSP90 (Henot 2022)', '40 × 1 µs MD, two starts', 'yes: two sets of NMR NOE references, CPMG', 'science + all tests'],
    ['DHFR (Cetin 2023)', '4 MD runs, 1 per ligand/variant', 'no: inhibition constants only', 'workflow test'],
    ['ADK (Orädd 2021)', '2 MD runs, no ligand', 'partly: time-resolved scattering, but different conditions', 'only system the rules never saw'],
    ['Nanodisc Q05 (Bengtsen 2020)', 'MD + SAXS + NOE', 'yes: SAXS and two NOE sets on shared weights', 'development case; cross-observable result in A6'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 10.5, rowH: 0.36, colW: [2.0, 2.1, 3.0, 1.9] });
  label(s, 0.5, 3.2, 9, 'The comparison design, used in every test');
  table(s, [
    ['Term', 'Meaning'],
    ['condition (arm)', 'same question, one thing changed, e.g. rules in the prompt or not; 4 fresh runs each; compared as medians of 4'],
    ['grading key', 'what a correct answer must contain; written from question, data and paper, frozen before the first run, not from the rules'],
    ['core unit', 'one of 5 required pieces of content per question; we count correct units, errors, overclaims (too strong) and omissions'],
  ], { x: 0.5, y: 3.55, w: 9, fontSize: 9.5, rowH: 0.28, colW: [1.4, 7.6] });
}

// ---------- 5 HSP90 science
{
  const s = base('HSP90 (Henot 2022): the paper shows a transiently populated closed state; on the same 40 trajectories we asked one narrower question, direction persistence',
`SAY: What the paper is. Henot and colleagues combine NMR with forty one-microsecond MD trajectories, twenty from the open crystal structure and twenty from a closed model, to argue that the closed state of the N-terminal domain is transiently populated. They classify the twenty closed-start runs as seven near-closed, about nine toward open, four neither, using NOE violations and clustering. They report millisecond exchange from CPMG and do not claim populations from MD. What we asked: does a trajectory show a sustained open direction, defined as the sign of two difference readouts staying open for five consecutive saved points, and does it ever reverse. The figure: of twenty closed-start runs, ten show a sustained open direction. For five, the first qualifying segment is already open-direction; that does not mean they were open at time zero. The other five first held a closed direction and turned open later; those are the same five counted as departures from the first sustained direction. Ten never show it. Open-start: none depart. Same data, different question, so our ten need not match their nine.
GRILL "why 5 points": pre-registered 5, 20, 50; the reversal count 5/4/1 falls with the threshold because the threshold also changes which segment counts as the reference.`,
'Henot et al. 2022 Nat Commun 13:7601 (doi:10.1038/s41467-022-35399-8); figure: first-round audited counts, 20–1020 ns window');
  fig(s, 'hsp90_events_10_20.png', 0.5, 1.3, 5.6, 2.2, 'Closed-start: any sustained open-direction segment 10/20; departure from the first sustained direction 5/20 (the same five that turned open later). Not transition rates.');
  table(s, [
    ['', 'Paper', 'Ours'],
    ['method', 'NMR (NOE, CPMG) + MD', 'same MD, direction readouts'],
    ['closed-start 20', '7 near-closed / ~9 toward open / 4 neither', '10 open-direction (5 first segment open + 5 closed then open) / 10 never'],
    ['departures from first direction', 'not asked', '5 / 4 / 1 at 5 / 20 / 50 points; open-start 0'],
    ['populations, rates', 'not from MD (non-ergodic)', 'not claimed'],
  ], { x: 6.3, y: 1.3, w: 3.2, fontSize: 9.5, rowH: 0.42, colW: [0.8, 1.2, 1.2] });
  callout(s, 0.5, 3.95, 9, 0.95, 'Two different partitions of the same twenty runs. Ours asks about persistence and reversal of a direction; the paper asks which reference each run ends near. The next slide connects them.', 12);
}

// ---------- 6 NOE crosswalk
{
  const s = base('HSP90, the measurement that mattered: at 1 Å tolerance, 9 of the 10 open-direction trajectories spend most of their open-direction time far from both NOE references',
`SAY: "Open direction" is the sign of a difference and says nothing about reaching the open state. So we read the authors' deposited NOE violation series for both references, point by point. For each trajectory we asked what share of its open-direction points lies within 1 Å of the open references; if at least half are far from both references, the run is called relative only. Nine of the ten are relative only, ES04 is partial, none reaches agreement. The open-start controls, the squares, agree in eighteen of twenty, which is what validates the tolerance. The scatter is for orientation: each point is the mean of the last hundred points. The runs have clearly left the closed side and several end near the open line. ES15 drops from 9.1 to 1.1 Å between its first and last hundred points, and ES04 and ES15 enter the control band (95th percentile of open-start values, 1.32 Å, held for 50 points) at 188 and 690 ns. So there is real structural change; moving closer is not the same as meeting the open tolerance most of the time. This agrees with the paper's phrase that these runs almost satisfy the open NOEs. System point: the Agent reproduced direction counts; the arrival question was added by a person. That is what the framing use of the table is for.
ASK HER: is a 1 Å tolerance on mean NOE violation a sensible test for being at the open state? What would you use?
GRILL "why 1 Å": pre-registered 0.5, 1, 2. At 0.5 the controls drop to 7 of 20; at 2 Å three candidates become consistent. All three reported. GRILL "did it open or not": some runs show an open direction and locally approach the open reference; they cannot all be counted as complete transitions. The control band is a same-source empirical comparison, not an independent state calibration.`,
'Author-deposited NOE violation series (column 2); classification = share of open-direction points within tolerance; controls 18/20 at 1 Å; control band p95 = 1.32 Å');
  fig(s, 'hsp90_noe_endpoint_scatter.png', 0.5, 1.28, 9, 2.95, 'Left: all 40 trajectories. Right: zoom on the open corner. Position = mean of the last 100 points (orientation only); colour = 1 Å classification by share of open-direction points within tolerance.');
  callout(s, 0.5, 4.68, 9, 0.45, '1 Å: relative only 9 · partial 1 · agreement 0 (controls 1 · 1 · 18). At 2 Å, 3 of 10 agree. Runs move closer to the open reference; none meets the 1 Å tolerance for most of its open-direction time.', 11);
}

// ---------- 7 HSP90 first-round comparison
{
  const s = base('HSP90, first comparison: rules pasted into the prompt did not improve the counts and imported conditions that belong to FRET',
`SAY: This was the first real use of the table, in the form the three systems ran under. Same question, four answers: two with only the data, two with the selected rules rendered into the prompt, seven rules, eight obligations, about 7,600 characters. Three of four got the main counts right; one mixed the five-point and fifty-point thresholds and did no calculation. The two rule answers were not more accurate. One of them, B2, added a useful 10 of 20 count. Both carried RMP-restraint conditions that belong to FRET-assisted modeling. That text reached the prompt because an NMR reference-source check was mapped onto Dimura's FRET-assisted modeling rule, and an MD-uncertainty check onto a smFRET calibration rule with R0 and dye volume. The paper supports those conditions for its own method; making them required fields for any NMR or MD analysis was our addition. Two runs per arm, and both arms shared the hand-written question, tables and field notes, so this cannot separate the selector from the protocol, the curation or the text length. It was enough to stop expanding this form and ask where the errors actually live.`,
'HSP90_Q01_VERIFIED_REPORT_ZH.md; 4 answers, 10 Sep 2026, $0.076; leaked rules C001-RULE-003 (Hellenkamp 2018), C003-RULE-002 (Dimura 2020)');
  table(s, [
    ['Answer', 'Rules in prompt?', 'Main counts (10/20; 5/4/1)', 'Computed anything?', 'Imported conditions not applicable to an NMR + MD question'],
    ['A1', 'no', 'correct', 'yes', 'none'],
    ['A2', 'no', 'mixed 5-pt and 50-pt thresholds', 'no, read tables', 'none'],
    ['B1', 'yes (7 rules, 8 obligations)', 'correct; one local binning wording error', 'yes', 'RMP-restraint conditions'],
    ['B2', 'yes (7 rules, 8 obligations)', 'correct; added a useful 10/20 count', 'yes', 'RMP-restraint conditions'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11.5, rowH: 0.45, colW: [0.8, 1.7, 2.4, 1.4, 2.7] });
  callout(s, 0.5, 3.75, 9, 1.1, 'Where it came from: an NMR reference-source check was mapped onto a FRET-assisted-modeling rule (RMP restraint, prior ensemble, fit objective); an MD-uncertainty check onto a smFRET calibration rule (R0, dye volume). Both texts reached the prompt; the answers carried the RMP terms. A rule can be retrieved correctly and still be wrong for the task.', 12);
}

// ---------- 8 DHFR
{
  const s = base('DHFR (Cetin 2023): the paper links 4′-DTMP\'s recovered inhibition of L28R to closer local contacts; we reproduced the direction, after finding an input artifact',
`SAY: What the paper is. Trimethoprim loses potency against the L28R mutant of DHFR; the analog 4′-DTMP recovers it. Their Table 1 inhibition constants: wild type 4.2 versus 5.1 nanomolar, L28R 65 versus 34. Their MD explanation: 4′-DTMP sits closer to atoms of the M20 loop and arginine 28. What we asked: the specified protein–ligand atom distances, one trajectory per condition, 990 frames. The figure: left is the frozen table, built from stored coordinates; a whole cluster of frames sits between 46 and 94 ångström. That is not a conformation; the ligand copy in a neighbouring periodic image was measured. Both Agent answers used these numbers; one called the tail conformational switching. Right is the corrected table, nearest periodic ligand image, cross-checked with VMD to ten to the minus five. M20 nitrogen to ligand O3P goes from 8.7 to 4.6 in wild type and 10.4 to 4.8 in L28R when TMP becomes 4′-DTMP; all six specified pairs move the same way as the paper's Figure 4. Gap: the paper frames hydrogen bonds; we have mean distances, no angles, one run each. Lesson: no rule text catches an input artifact. The check must sit at step 2, in code, before freezing. This was a preparation defect on my side.`,
'Cetin et al. 2023 J Chem Inf Model (PMC10428214) Table 1, Figs 3–4; PBC_VALIDATION.json (VMD max Δ 1.1 × 10⁻⁵ Å); O3P is an atom name');
  fig(s, 'dhfr_before_after_hist.png', 0.5, 1.3, 6.2, 2.3, 'M20 N – ligand O3P distance, frames 11–1000, four conditions; left frozen table, right corrected.');
  table(s, [
    ['', 'Paper', 'Ours'],
    ['experiment', 'Ki: WT 4.2 / 5.1 nM; L28R 65 / 34 nM', 'quoted as context'],
    ['MD claim', '4′-DTMP closer to M20 loop, R28; H-bonds', 'M20 N–O3P: WT 8.69 → 4.62 Å; L28R 10.44 → 4.81 Å'],
    ['limits', 'authors\' own analysis', 'n = 1 per condition; distance ≠ H-bond'],
  ], { x: 6.85, y: 1.3, w: 2.65, fontSize: 9, rowH: 0.5, colW: [0.65, 1.0, 1.0] });
  callout(s, 0.5, 4.05, 9, 0.85, 'Both Agent answers accepted the 46–94 Å values (defect noticed 0/2). No reminder text catches a wrong input; the check belongs at step 2, in code, before freezing. Original answers kept, not scored as science; corrected numbers are a developer calculation.', 11.5);
}

// ---------- 9 ADK
{
  const s = base('ADK (Orädd 2021): the paper tracks a millisecond ATP-binding response; the deposited ligand-free MD supports only domain-distance descriptions, and it broke my own data check',
`SAY: What the paper is. Photorelease of ATP, time-resolved X-ray solution scattering, a transient of about 4.3 milliseconds, interpreted with MD-derived candidate structures. The deposited MD: two trajectories, open-start 450 nanoseconds and closed-start 335, and no ATP or AMP in the coordinates. What we asked, the one thing computable: mean C-alpha distances between the LID or NMP domain and the CORE, comparing the first and last ten percent of frames, the shaded windows. All four changes are positive and the distributions overlap, so there is no net joint closure between the endpoint windows; this does not exclude closure episodes inside the runs. Gap: no ligand, no scattering recomputed, nanoseconds against milliseconds; this does not test the paper's mechanism. The system lesson concerns my own rule. After DHFR I wrote a data check: any distance above half the box length fails. Open ADK spans 56 ångström along one axis in a 98 to 100 ångström box, so C-alpha distances of 62 and 70 ångström are real, and GROMACS reproduces them. The rule was replaced by a physical criterion. DHFR asked a protein–ligand contact, so the nearest ligand image is right there; ADK asks a distance inside one protein, so the molecule must stay whole. The check has to follow the observable. Framing also helped here: the split version of the ADK question scored five of five.
GRILL "why keep ADK": only system the rules and the selector had never seen; and the one you named.`,
'Orädd et al. 2021 Sci Adv 7:eabi5514; Zenodo 5583119; project domain definitions; GROMACS cross-check max Δ ≈ 0.005 Å');
  fig(s, 'adk_domain_timeseries.png', 0.5, 1.3, 5.2, 2.95, 'LID–CORE and NMP–CORE mean Cα distance per frame; shaded = first/last 10 % windows.');
  table(s, [
    ['', 'Paper', 'Ours'],
    ['experiment', 'TR-XSS after ATP release, with AMP; ~4.3 ms transient', 'not reproducible from this MD'],
    ['MD', 'candidates fitted to scattering', 'window change, Å: open start LID +2.29, NMP +0.07; closed start +1.18, +1.09'],
    ['conditions', 'ATP + AMP, 294 K', 'no ligand, 303 K, ≤ 450 ns'],
  ], { x: 5.9, y: 1.3, w: 3.6, fontSize: 9, rowH: 0.5, colW: [0.75, 1.4, 1.45] });
  callout(s, 5.9, 3.45, 3.6, 1.45, 'DHFR asks a protein–ligand contact: nearest ligand image. ADK asks a distance inside one protein: keep the molecule whole. My half-box rule (49–50 Å) flagged real 62 and 70 Å distances. The check must follow the observable.', 10.5);
}

// ---------- 10 Retrospective
{
  const s = base('Looking back at every answer so far: most of the 13 error observations sit at data entry or in the reported numbers, where reminder text had no obvious hook',
`SAY: Before testing the four uses we audited every answer we had: eight answers, thirteen observations, seven underlying causes, so correlated observations rather than thirteen independent cases. Grouped by the workflow step where each lives: input representation, numbers read from the wrong column or threshold, the sign of a difference read as arrival, imported conditions. Reminder text had no obvious hook in any of them; that is a judgement, not a test. Code before freezing or after submission could plausibly prevent most; two need the question asked better. That was a candidate attribution; the tests on the next slides check it. One detail for later: three of the thirteen were caught when we replayed the DHFR input checks; the conclusion checker on slide 15 caught zero of the seven numeric ones. Different subsets, both true.`,
'E0_RETROSPECTIVE_AUDIT.csv: 13 rows, 7 same-cause groups, 8 answers (HSP90 4, DHFR 2, nanodisc 2)');
  table(s, [
    ['Error group (where observed)', 'Workflow step', 'Reminder text?', 'What could catch it'],
    ['periodic-image artifact taken as real (DHFR × 2)', '2 Package', 'no', 'physical data check in code'],
    ['threshold / column mix-ups in counts (HSP90 A2; DHFR A1 percentages)', '5 Check', 'no', 'recompute each claimed number from its source'],
    ['wrong NOE upper-bound array (nanodisc Q05)', '5 Check', 'no', 'bind each claim to raw quantity, unit and transform'],
    ['"open direction" read as "near open state" (HSP90)', '3 Frame', 'partly', 'split the question: direction / arrival / full transition'],
    ['FRET-only conditions imported (HSP90 B1, B2)', '4 Run', 'text is the cause', 'retrieve guidance by the operation requested, not by method name'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11.5, rowH: 0.5, colW: [3.3, 1.2, 1.5, 3.0] });
  s.addText('Retrospective and not a random sample: the attributions are candidates without paired counterfactuals, which is why each use was then tested separately.', { x: 0.5, y: 4.45, w: 9, h: 0.5, fontSize: 11, fontFace: F, color: C.muted });
}

// ---------- 11 Agent run
{
  const s = base('The Agent step is real analysis: sealed container, read-only data, Python written and run, a structured answer submitted, one to two cents per run',
`SAY: Before the tests, what one run is. A fresh container: no network, data read-only, five tools, and a submit call that ends the answer; ordinary text afterwards never overwrites it. The model is gpt-5.6-luna at medium reasoning. A typical run is twelve to twenty tool calls, about a minute, under two cents. It genuinely computes: it matched all ninety SAXS points in the nanodisc case and reproduced the four ADK window changes to four decimals. So the cost of an experiment is scoring time, not money. Why the Agent stays: goal four asks whether an agent can lower curation cost without adding unsafe claims; it is the last goal and allowed to fail on its own. The open question is not "can it analyse". It is what information given to it produces a measurable gain.`,
'Luna runtime v1; three directories mounted separately (data / hidden grading key / rules); control arm directory has no rule files, asserted by a test');
  table(s, [
    ['What the run gets', 'What it cannot do', 'What is logged'],
    ['read-only data · source card · question', 'reach the network', 'every tool call and its output'],
    ['5 tools: list · read · run Python · note · submit', 'see the hidden grading key or another arm\'s files', 'the submitted structured answer'],
    ['≤ 40 tool calls · ≤ 25 min', 'overwrite a submitted answer with chat text', 'cost per run, settled from provider receipts'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 12.5, rowH: 0.5, colW: [3.3, 2.9, 2.8] });
  callout(s, 0.5, 3.35, 9, 1.4, 'Why the Agent stays in the design: goal 4 asks whether an agent can lower curation cost without adding unsafe claims. It is the last of the four goals and is allowed to fail on its own. The question tested next is not "can it analyse" (it can) but "what information given to it produces a measurable gain".', 13);
}

// ---------- 12 Four uses
{
  const s = base('So the 33 rules were split by job into four uses; the design question became: what information reaches the Agent, in what form, at which step',
`SAY: This is the current design and a direct answer to the original question of how the Agent should use the table. Framing: six rules become sub-questions and the grading key, never shown to the Agent. Data checks: ten rules become code before freezing, reaching the Agent only as a card of results. Method cards: eleven rules become short cards retrieved by method family, the only rule text the Agent reads. Conclusion checks: six rules become an automatic check after submission with one feedback message. Each use changes exactly one thing about what the Agent receives, so each can be tested on its own. The ensemble blog by Li, Thomasen and Cossio motivates the order: decide which difference to distinguish, confirm it survives measurement and processing, then choose the method. The four-way split is our own design hypothesis, not a conclusion of the blog, and the uses overlap: whether a method applies matters in preparation, computation and interpretation alike.
GRILL "is the split arbitrary": it follows the rule_class field in the table; the assignment is in the appendix and can be argued rule by rule.`,
'RULES_TABLE_ROLE_DESIGN_ZH.md §2; assignment by rule_class 6 / 10 / 11 / 6 (A2). The split is our design hypothesis; the uses overlap.');
  table(s, [
    ['Use', 'Question it answers', 'Executed by, when', 'What the Agent receives', 'Rules'],
    ['A Framing', 'which difference must this question distinguish; which sub-questions; what competing explanations', 'person + template, before the run', 'nothing directly: the question text and the hidden grading key', '6'],
    ['B Data checks', 'can these data answer it: object, condition, units, time, role of each dataset, physics', 'code, before freezing', 'a card of PASS / FAIL results in the data directory', '10'],
    ['C Method cards', 'how this kind of data should be computed: forward model, averaging, reweighting prerequisites', 'retrieved by method family, at run time', 'short cards, ≤ 10 lines each, the only rule text it sees', '11'],
    ['D Conclusion checks', 'how far the result can be read: frames ≠ populations, fit ≠ validation, proximity ≠ state', 'code, after submission', 'one feedback message; may revise once', '6'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.7, colW: [1.3, 3.0, 1.7, 2.5, 0.5] });
}

// ---------- 13 Test design
{
  const s = base('Each use got its own test that could fail: what triggered it, the one thing changed, and the pass criterion written down before running',
`SAY: The reasoning behind the three questions we measured. Framing: from HSP90 we knew the Agent answered the direction question but never the arrival question; if framing helps, splitting the question raises supported coverage without adding overclaims. Data checks: from DHFR we knew a bad table passed; the checker was tried on six planted defects and three clean packages, and the Agent was given or not given the card on the defective table; if the card helps, it downgrades its conclusions. Method cards: from HSP90 we knew full rules imported conditions; if cards help, they keep accuracy and stop the imports, judged against a seven-line protocol and the full rules. Conclusion checks: from the threshold mix-up and the nanodisc bound array we knew numbers went out wrong; if the check helps, one automated pass reduces core errors without more omissions. Same model, four runs per condition, frozen, de-labelled scoring, medians of four.
GRILL "who scored": the same agent that prepared the cases, with labels masked, one scorer. Biggest limitation, stated in the report.`,
'FOUR_LAYER_VALIDATION_PLAN_ZH.md v2; 74 runs, $1.20; scorer also prepared the cases (labels masked); nanodisc Q05 is a development case');
  table(s, [
    ['Use', 'Trigger (what we had seen)', 'The one thing changed', 'Questions · runs', 'Pass criterion (pre-set)'],
    ['A Framing', 'HSP90: direction answered, arrival never asked', 'original question vs explicit sub-questions', 'HSP90, ADK · 16', 'coverage up on 2/2 questions, overclaims not up'],
    ['B Data checks', 'DHFR: wrapped table passed into the run', 'data-check card present vs absent; checker on 6 planted defects + 3 clean packages', 'DHFR defective · 8', 'checker ≥ 5/6, 0 false alarms; Agent downgrades more with card'],
    ['C Method cards', 'HSP90 B1/B2: FRET conditions imported', '7-line protocol vs full rules vs scoped cards', 'HSP90 NOE, nanodisc Q05 · 24', 'cards at least as good as both on both questions; 0 inapplicable terms'],
    ['D Conclusion checks', 'A2 thresholds; Q05 wrong NOE bound', 'no feedback vs one automated review pass', 'HSP90, DHFR fixed, ADK · 24', 'fewer core errors on ≥ 2/3 questions, omissions not up'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 10.5, rowH: 0.62, colW: [1.2, 2.1, 2.3, 1.5, 1.9] });
  s.addText('Coverage is counted over 3 pre-registered sub-questions per question; correct units over the 5 core units. Answers de-labelled; scores sealed before the condition mapping was revealed.', { x: 0.5, y: 4.55, w: 9, h: 0.5, fontSize: 11, fontFace: F, color: C.muted });
}

// ---------- 14 Results
{
  const s = base('Result: only explicit sub-questions met its criterion; the data-check card, method cards and one feedback pass did not',
`SAY: Four rows. Framing: coverage HSP90 2 to 2.5 of 3, ADK 2 to 3 of 3, no new overclaims; keep. Two caveats: HSP90's total errors across four runs went 1 to 2, so the gain is completeness, not uniformly accuracy; and the sub-questions were written by a person, so this is a gain of the person-plus-Agent workflow, not of the Agent alone. Data checks: the checker caught all six planted defects, but the Agent detected the DHFR defect zero of four times with the card and zero of four without. Method cards: on HSP90 the plain protocol scored 4.5 of 5, full rules 2, cards 2.5; on the nanodisc question 4.5, 5, 4.5. Cards failed. The exception to keep on record: full rules were best on the nanodisc question, all four answers covered all five units. Feedback: only ADK improved, and that difference already existed in the initial drafts; no revision reduced its own error count; three lost content.
GRILL "so rules are useless": the prompt form is not supported. The library is still the raw material for checks and cards, and Q05 is one case where the full text helped. What cannot be claimed is a stable increment.`,
'UNBLINDED_SCORES.csv, medians of 4; FINAL_DECISIONS.json; RULES_TABLE_VERDICT_EN.md', 20);
  table(s, [
    ['Use', 'Observed (median of 4 unless stated)', 'Met?', 'Decision'],
    ['A Framing', 'coverage HSP90 2 → 2.5 /3, ADK 2 → 3 /3; overclaims 0 → 0; HSP90 total errors 1 → 2 over 4 runs. Sub-questions were written by a person.', KEEP, 'keep: ask direction, magnitude and limits separately'],
    ['B Data checks', 'checker 6/6 planted defects, 0/3 false alarms; Agent detected the defect 0/4 with card, 0/4 without; all 4 card runs listed the file, none read it', NO, 'run data checks inside preparation; never rely on the Agent finding a warning file'],
    ['C Method cards', 'correct units /5 — HSP90: protocol 4.5 · full rules 2 · cards 2.5; nanodisc: 4.5 · 5 · 4.5', NO, 'pause; retrieve by operation, not method family; keep the nanodisc full-rule benefit on record'],
    ['D Conclusion checks', '1/3 questions improved (ADK), already better in initial drafts; 0/12 revisions reduced errors; 3 lost content (one had no warning); 0/9 warnings hit a real error', NO, 'pause; matching numbers to logs cannot catch numbers already wrong in the logs'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.74, colW: [1.3, 4.2, 0.7, 2.8] });
}

// ---------- 15 Why each failed
{
  const s = base('Why each use failed matters more than that it failed: delivery, applicability and traceability are three different problems',
`SAY: Three mechanisms, each pointing at a specific repair. The card was available but never opened: a file is not a channel. Retrieval by method family gave HSP90 one card, a BME reweighting card, for a task that compares deposited violations and fits nothing; BME, Bayesian maximum entropy, adjusts the weights of existing conformations to match experiment, and reading deposited NOE violations creates no such obligation; DHFR and ADK retrieved zero cards, because the eleven papers do not cover pure-MD questions. The conclusion checker asks whether a number appears in the tool output; in the nanodisc case the wrong bound array was written to the log first, so the wrong 4.35 ångström passed; on eight historical answers it caught zero of seven known numeric errors and raised one false alarm on the minus one in inverse ångström.
GRILL "why not a stronger model": the worst errors are in inputs the model cannot see, and number errors need recomputation from raw quantities; both are pipeline problems.`,
'E1B_CARD_ACCESS_AUDIT.json; E3_CARD_RETRIEVAL.json; METHOD_CARD_DESIGN_ANALYSIS_ZH.md; E0_CEILING_REPLAY_REVIEW_ZH.md');
  table(s, [
    ['Use', 'Mechanism observed', 'Repair it points to'],
    ['B Data-check card', 'tool logs: card file listed in 4/4 runs, contents read in 0/4', 'block bad tables at step 2; a warning file is not a channel'],
    ['C Method cards', 'HSP90 retrieved 1 card, a BME reweighting card, for a task that fits no weights; nanodisc retrieved 4 incl. FRET-specific; DHFR and ADK retrieved 0', 'index cards by the operation being performed and its prerequisites; cover MD-only operations'],
    ['D Conclusion check', 'checks whether a number appears in tool output; the wrong nanodisc bound array was already in the log, so 4.35 Å passed; replay on 8 answers: 0/7 numeric errors caught, 1 false alarm (the −1 in Å⁻¹)', 'recompute each claim from raw quantity, unit and transform; do not match strings'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11.5, rowH: 0.85, colW: [1.6, 4.4, 3.0] });
}

// ---------- 16 Three forms
{
  const s = base('How the Rules Table should be built from here: three forms, what each assumes, and what this round\'s evidence says about each',
`SAY: Back to the original idea: an Agent that enters the table and follows rules to choose operations and extra analyses. Three forms of that. Form one: keep the four uses and repair each with the mechanism from the previous slide, then retest on new questions; it assumes the failures were implementation, not concept. Form two: the rules serve the people who write the protocol and the grading key; the Agent gets a seven-line protocol only. This has the strongest evidence today, the protocol arm was never worse, but it gives up the original idea. Form three: each rule becomes the configuration of a deterministic operator, a data check, a computation, a claim-limit test; the Agent proposes which operator to call, code executes it and bounds the claim, and the Agent never reads rule text. The bridge from evidence to this form is the mechanisms: the checks that actually mattered, DHFR and ADK, were physical and executable, and the failures were all about text, delivery, applicability, string matching. It is closest to the original idea and to that lesson, but none of it has been built or tested. My lean: build toward three, keep two as the baseline every version must beat on new questions. Your call.`,
'Evidence: slides 14–15. Authority split in SYSTEM.md: Agent proposes; deterministic code validates, computes and bounds; a person owns competing explanations', 19);
  table(s, [
    ['Form', 'What the Agent gets', 'Assumes', 'Evidence today', 'Not yet tested'],
    ['1  Repair the four uses', 'card delivered inside the question; operation-indexed cards; recompute-based check', 'failures were implementation, not concept', 'A supported; B, C, D failed in current form; mechanisms identified', 'every repair'],
    ['2  Rules serve the protocol writer', 'a 7-line protocol only; rules used by people for grading key and data checks', 'a human-written protocol captures what matters', 'strongest: protocol arm never worse (HSP90 4.5/5, nanodisc 4.5/5)', 'whether it scales past three systems'],
    ['3  Rules as operator configuration', 'a catalogue of callable, registered operators; Agent proposes which to call, code executes and bounds the claim', 'every useful rule can be made executable', 'indirect: the checks that mattered (DHFR, ADK) were physical and executable; all failures were about text', 'the whole form'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 10.5, rowH: 0.78, colW: [1.7, 2.5, 1.6, 2.2, 1.0] });
  callout(s, 0.5, 4.55, 9, 0.5, 'My lean: build toward 3, keep 2 as the baseline every version must beat on new questions. Your call.', 12.5);
}

// ---------- 17 Systems verdict
{
  const s = base('Are the three systems the right ones? By the criterion from slide 4, only HSP90 fully qualifies; DHFR and ADK earned their place as workflow tests',
`SAY: Back to the criterion: MD plus an experiment that constrains the difference the question is about. HSP90 has two NOE references and CPMG; it fully qualifies, and together with the nanodisc development case it is where we have a cross-source result. DHFR has kinetics only; it tested the workflow, not the science, and exposed the missing data check. ADK has time-resolved scattering, but the deposited MD is ligand-free and nanoseconds against milliseconds; it broke my data check, framing helped on it, and it is the only system the rules had never seen. Question for you: is this the right criterion, and is there a fourth system with MD plus NMR, SAXS or single-molecule FRET data that constrains populations, ideally from the group's own work?
GRILL "drop DHFR": as a science system yes; as a workflow regression test it earned its keep.`,
'Slides 5–9; 24 Aug meeting: HSP90 first, one system at a time', 19);
  table(s, [
    ['System', 'Paper\'s result', 'Our result', 'Experiment constrains the question?', 'What it tested', 'Keep?'],
    ['HSP90', 'transient closed state; 7/9/4; ms exchange', '10/20 direction; 9/10 relative only at 1 Å; no populations', 'yes: two NOE references, CPMG', 'science, framing, prompt form', { text: 'yes, deepen', options: { color: C.green, bold: true } }],
    ['DHFR', '4′-DTMP recovers L28R inhibition; closer local contacts', 'same direction, 8.69 → 4.62 Å (WT), n = 1', 'no: Ki only', 'workflow: exposed the missing data check', { text: 'as regression test', options: { color: C.muted, bold: true } }],
    ['ADK', 'ms ATP-binding response by TR-XSS; MD candidates', 'ligand-free domain distances overlap; LID +2.29 Å (open start)', 'partly: TR-XSS exists, but MD is ligand-free, ns', 'data-check rule (broke it); framing; only unseen system', { text: 'keep as unseen control', options: { color: C.accent, bold: true } }],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 10.5, rowH: 0.7, colW: [0.8, 2.0, 2.0, 1.9, 1.5, 0.8] });
  callout(s, 0.5, 4.3, 9, 0.7, 'Ask: a fourth system with MD plus an experiment that constrains populations (NMR / SAXS / smFRET)? Any candidate from the group\'s own work?', 12.5);
}

// ---------- 18 Conclusions + asks
{
  const s = base('Conclusions, and the three things I need from you',
`SAY: Three sentences. The three systems produced bounded, checkable results; HSP90 is the strongest and a real cross-source comparison. The table as prompt text did not earn its place; its content is still the raw material for executable checks and operation-indexed guidance, and framing the question explicitly, by a person, is the one use that measurably helped. The next build should put physical data checks inside preparation, make rules executable where they can be, and be tested against the seven-line protocol on new questions with independent scoring. Three decisions from you: is the workflow on slide 3 reasonable; which form of the table should we build toward; are these the right three systems, and is there a fourth. And one science question: in HSP90, is 1 Å on mean NOE violation the right test for being at the open state?
Leave this slide up for discussion.`,
'Full evidence and all 74 runs: github.com/alex051107/dynamics-atlas-harness/pull/27');
  bullets(s, [
    'Workflow (slide 3): intake → package → frame → run → check → report; the table can act at steps 2–5. So far the evidence points to step 3 (framing, by a person) and to physical checks at step 2 (from the DHFR and ADK lessons, not from the card test).',
    'Three systems: HSP90 gave a real cross-source result (direction ≠ arrival); DHFR and ADK are single-source MD descriptions that exposed two data-check defects, one of them in my own rule.',
    'Four-use test, 74 runs: only explicit sub-questions met its criterion; card delivery, method-family retrieval and number matching each failed for an identified reason.',
  ], { y: 1.3, h: 2.05, fontSize: 13.5 });
  callout(s, 0.5, 3.4, 9, 1.68, 'Decisions for today\n1. Is the workflow on slide 3 reasonable? What would you reorder, cut or add?\n2. Which form of the table (slide 16): repair the four uses, rules for the protocol writer, or rules as operator configuration?\n3. Are HSP90 / DHFR / ADK the right systems (criterion on slide 4), and is there a fourth with MD plus a population-constraining experiment?\n4. Science: in HSP90, is 1 Å on mean NOE violation the right test for being at the open state?', 12);
}

// ---------- 19 References
{
  const s = base('References', null, null);
  bullets(s, [
    'Henot F. et al. (2022) Visualizing the transiently populated closed-state of human HSP90 ATP binding domain. Nat Commun 13, 7601. doi:10.1038/s41467-022-35399-8',
    'Cetin E. et al. (2023) DHFR L28R / TMP and 4′-DTMP study. J Chem Inf Model; PMC10428214; data Zenodo 7966540; authors\' code github.com/midstlab/JCIM_Cetin_etal_2023',
    'Orädd F. et al. (2021) Tracking the ATP-binding response in adenylate kinase in real time. Sci Adv 7, eabi5514. doi:10.1126/sciadv.abi5514; data Zenodo 5583119',
    'Bengtsen T. et al. (2020) Structure and dynamics of a nanodisc by integrating NMR, SAXS and SANS experiments with MD. eLife 9, e56518',
    'Li, Thomasen, Cossio (2026) Are we capturing the ensemble? RS Station blog, 31 Aug 2026',
    'Bhakat S. (2026) Benchmarking generative AI and physics-based simulation for conformational heterogeneity in T4 lysozyme. J Chem Inf Model. doi:10.1021/acs.jcim.6c02044',
    'Rule sources (11): Hellenkamp 2018; Agam 2023; Dimura 2020; Fuertes 2017; Shevchuk 2017; Bengtsen 2020; Hoff 2024; Peter 2022; Sanabria 2020; Steffen 2021; Wankowicz & Bonomi 2026 — locators in rule_registry.tsv',
  ], { fontSize: 11.5, paraSpaceAfter: 5 });
}

// ---------- Appendix
{
  const s = pptx.addSlide(); n += 1;
  s.background = { color: C.primary };
  s.addText('Appendix', { x: 0.7, y: 2.1, w: 8.6, h: 0.8, fontSize: 30, fontFace: F, color: 'FFFFFF', bold: true });
  s.addText('A1 what the evidence can and cannot support · A2 all 33 rules by use · A3 scores per condition · A4 cost · A5 HSP90 example trajectories · A6 nanodisc cross-observable result · A7 terms', { x: 0.7, y: 2.9, w: 8.6, h: 0.5, fontSize: 13, fontFace: F, color: 'A0BBDD' });
}
{
  const s = base('A1. What this evidence can and cannot support', null, 'METHODS_AND_LIMITS_ZH.md; DEVIATIONS.md');
  table(s, [
    ['Can say', 'Cannot say'],
    ['pasting rules into the prompt showed no gain on 2 questions and one concrete harm', 'that rules are useless in general'],
    ['explicit sub-questions raised coverage on 2/2 questions without new overclaims', 'that the Agent discovers sub-questions on its own'],
    ['the current checker and card retrieval did not meet pre-set criteria; mechanisms identified', 'a population-level correctness rate for any condition'],
    ['HSP90: leaving closed ≠ reaching open, at three tolerances', 'populations or rates for HSP90; H-bonds or mechanism for DHFR; anything about ADK\'s ATP response'],
    ['most located errors sat at data entry or in reported numbers', 'that this is the general distribution of errors (retrospective audit, not a random sample)'],
    ['scores measure delivery of pre-defined content', 'that scores capture all scientific content (bundled units can drop partial credit)'],
    ['74 runs, $1.20, all preserved with logs and sealed scores', 'that scoring was independent of case preparation; that human time was saved (not measured)'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.42, colW: [4.5, 4.5] });
}
{
  const s = base('A2. All 33 rules, grouped by the use they now belong to', null, 'rule_registry.tsv; RULES_TABLE_ROLE_DESIGN_ZH.md §2');
  table(s, [
    ['Use', 'Rule IDs (rule_class)'],
    ['A Framing (6)', 'C010-001 claim_ladder · C010-002 state_semantics · C005-001 estimand_non_equivalence · C009-003 estimand_non_equivalence · C012-001 benchmark_contract · C012-002 identifiability'],
    ['B Data checks (10)', 'C001-001 measurement_semantics · C002-001 measurement_semantics · C001-002 uncertainty_provenance · C001-003 measurement_quality · C008-001 source_quality · C007-001 multi_source_semantics · C009-001 cross_validation · C009-002 diagnostic_controls · C003-001 candidate_design · C003-003 held_out_validation'],
    ['C Method cards (11)', 'C002-002, C006-001, C008-003 forward_bridge · C011-001 forward_implementation · C005-003 inverse_model · C003-002 reweighting · C007-002 integration_operator · C006-002 uncertainty_integration · C011-002 uncertainty_decomposition · C002-003, C008-002 artifact_exclusion'],
    ['D Conclusion checks (6)', 'C006-003, C011-003, C012-003 claim_ceiling · C005-002 complementary_evidence · C007-003 integration_validation · C010-003 functional_validation'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.8, colW: [1.7, 7.3] });
}
{
  const s = base('A3. Median scores per question and condition (n = 4 each)', null, 'UNBLINDED_SCORES.csv; medians recomputed locally from the unblinded table');
  table(s, [
    ['Test', 'Question', 'Condition', 'Correct /5', 'Errors', 'Overclaims', 'Omissions /5', 'Coverage /3'],
    ['Data checks', 'DHFR defective', 'no card / card', '3 / 2', '1 / 2.5', '1 / 2', '1 / 0', '—'],
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
    ['Data-check card comparison', '8', '0.1469', '0.20'],
    ['Plain ADK', '2', '0.0233', '0.15'],
    ['One-feedback comparison', '24', '0.3858', '0.55'],
    ['Method-guidance comparison', '24', '0.4158', '0.55'],
    ['Question decomposition', '16', '0.2312', '0.40'],
    ['Four-use total', '74', '1.2029', '1.85'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 12.5, rowH: 0.4, colW: [5.2, 0.9, 1.7, 1.2] });
  s.addText('Model wall time for the 74 runs ≈ 90 minutes. Scoring, cross-checks and report writing were the actual cost.', { x: 0.5, y: 4.6, w: 9, h: 0.4, fontSize: 11.5, fontFace: F, color: C.muted });
}
{
  const s = base('A5. HSP90: three example trajectories against both NOE references', null, 'v4 native NOE crosswalk, author-deposited violation series; shaded = sustained open-direction segments; dotted = 1 Å tolerance');
  fig(s, 'hsp90_noe_examples.png', 0.5, 1.3, 4.7, 3.75, 'ES15: reaches open reference band; ES03: open direction, stays ~1 Å; ES01: leaves closed late, arrives nowhere.');
  bullets(s, [
    'Orange: violation of closed-state NOEs; teal: violation of open-state NOEs; both in Å.',
    'ES15 (top) drops to the open tolerance quickly and stays: the one closed-start run that clearly arrives.',
    'ES03 (middle) is open-direction for most of the run but hovers near, not within, the open tolerance.',
    'ES01 (bottom) never shows a sustained open direction; both violations stay large.',
    'This is why direction and arrival are scored separately.',
  ], { x: 5.4, y: 1.3, w: 4.1, h: 3.7, fontSize: 12.5 });
}
{
  const s = base('A6. Nanodisc (development case): reweighting to fit SAXS improved the SAXS fit but not the agreement with either NOE set',
`SAY if asked: this is the most direct cross-observable result we have. Same MD ensemble, weights adjusted to fit SAXS only. The SAXS penalty falls from 10.0 to 1.2, while the penalties for both NOE sets, computed with the same weights, get worse. A better fit to one observable does not bring agreement with another. It is a conditional answer, not proof that the experiments contradict each other; restraint reuse, error model, candidate construction and NOE averaging still limit it. The analysis was designed by the developer; Agent runs on this case carried the result through, they did not discover the method.`,
'Bengtsen et al. 2020 eLife; Q05 frozen analysis, main setting θ = 6; 90 SAXS points, 292 amide and 40 methyl NOE restraints; developer-designed, exposed during development');
  table(s, [
    ['Quantity (same weights applied to all three)', 'Before reweighting', 'After SAXS-only reweighting', 'Direction'],
    ['SAXS mean penalty (90 points)', '10.0188', '1.1707', { text: 'better', options: { color: C.green, bold: true } }],
    ['amide NOE penalty (292 restraints)', '0.9334', '0.9647', { text: 'slightly worse', options: { color: C.red, bold: true } }],
    ['methyl NOE penalty (40 restraints)', '3.8931', '4.4695', { text: 'worse', options: { color: C.red, bold: true } }],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 12.5, rowH: 0.45, colW: [3.6, 1.7, 2.3, 1.4] });
  bullets(s, [
    'A better fit to one observable does not imply agreement with another: SAXS averages intensity linearly; NOE upper bounds need r⁻⁶ averaging and one-sided treatment.',
    'Conditional answer, not proof that the two experiments contradict each other: restraint reuse, error model, candidate construction and NOE averaging still limit it.',
    'Developer-designed analysis; Agent runs on this case carried the result through, they did not show independent method discovery.',
  ], { x: 0.5, y: 3.35, w: 9, h: 1.7, fontSize: 12.5 });
}
{
  const s = base('A7. Terms as used in this deck', null, null);
  table(s, [
    ['Term', 'Meaning here'],
    ['Rule', 'one caution from one methods paper: finding, required check, stop route, transfer scope'],
    ['Selector', 'code that matches rules to a question by method family and renders them as required checks'],
    ['Agent run', 'one sealed container session of the LLM: reads data, writes Python, submits a structured answer'],
    ['Condition / arm', 'one variant of a comparison; same question, one thing changed; 4 fresh runs each'],
    ['Frozen', 'question, grading key, code and run order hashed before the first model call; changes void the test'],
    ['Core unit', 'one of five predefined pieces of scientific content the grading key expects; scored correct / wrong / missing'],
    ['Overclaim', 'a stated conclusion stronger than the evidence supports (e.g. frame fraction as population)'],
    ['Exposed case', 'a question or dataset already used during development; cannot serve as an independent test'],
    ['Data checks (admission)', 'checks that the data can answer the question: object, condition, units, time, role of each dataset, physics'],
  ], { x: 0.5, y: 1.3, w: 9, fontSize: 11, rowH: 0.36, colW: [1.8, 7.2] });
}

pptx.writeFile({ fileName: OUT }).then(f => console.log('wrote', f, 'slides', n));
