# What the Rules Table should do — and what remains undecided

[Back to the research brief](../README.md)

The current evidence does not support a simple choice between “the rules are bad” and “the architecture is bad.” Several distinct failures were observed. They require different remedies, and not all have been isolated experimentally.

## How the rules entered the analysis

The original [33-row source-linked table](../../review/pro_briefing_20260910/rules/rule_registry.tsv) was derived from 11 papers. It is a CSV despite its `.tsv` filename. A typical path was:

**paper-specific finding → project review question → candidate rule → case metadata → selected obligation → rendered text for the Agent.**

The scientific gap can arise at any arrow. A source may justify a requirement only for a particular probe or inverse method. A project may generalize that condition, a selector may apply it to a different operation, or a renderer may present it as mandatory. A rule identifier and a successful match do not verify those steps.

For example, the HSP90 first-round prompt connected an NMR source-parentage question to `C003-RULE-002`, whose text included RMP restraints, a prior ensemble and a fitting objective. Another MD uncertainty obligation received FRET-specific R0/dye/accessibility language. The renderer preserved the original wording and object–check pairing; the problem was scientific applicability, not lost text. [Actual prompt](../../review/hsp90_q01-round-20260910/evidence/ACTIVE_RULES.md)

## Three separate decisions

| Form | Potential use | Current limit |
|---|---|---|
| A readable, source-linked table | Preserve assumptions, applicability and interpretation limits for review | Documentation value does not establish an Agent benefit |
| Guidance selected for an analysis | Remind the Agent of conditions relevant to the operation actually being performed | Family labels such as NMR or MD are too broad by themselves; observed effects differ by case |
| Executable checks | Detect a specific input or claim–evidence conflict with a defined basis | A passing check is not a scientific verdict; unknown applicability and false alarms matter |

These forms need not become four compulsory modules. Nor does a negative result for one checker invalidate all source-linked knowledge or all tool-using Agents.

## What the completed tests let us diagnose

**Applicability problems are directly visible.** The first-round HSP90 prompt transferred specialized conditions without establishing their relevance. In the later method-card pilot, a broad NMR match retrieved BME guidance for a task that did not require new weight fitting. This supports checking the intended operation before presenting method advice; it does not quantify how much of the score difference this mistake caused.

**Delivery can fail before the content is tested.** The warning file was listed but not opened in four runs. This shows a failure to deliver its information through that interface, not that the warning was scientifically useless after being read.

**A weak checker does not test strong scientific judgment.** The conclusion-checker warnings were about numerical traces in tool outputs. The checker did not read the entire Rules Table and decide whether the paper's mechanism was true. The evidence-role branch had no applicable input in that pilot. Its negative result concerns that implemented check-and-revision procedure.

**Question wording changed coverage.** Explicit subquestions increased supported coverage in two cases, but they also made the required content more explicit; HSP90 retained an accuracy cost. This supports clear task specification, not a general claim that the Agent learned to formulate scientific questions.

[Completed component report](../../review/four-layer-20260910/outputs/FOUR_LAYER_VALIDATION_REPORT_EN.md#4-admission-information-did-not-reach-the-agents-analysis) · [Method-card design and limitations](../../review/four-layer-20260910/outputs/METHOD_CARD_DESIGN_ANALYSIS_ZH.md)

## Proposed working form, subject to discussion

Keep a short scientific protocol and the source-linked archive. Let the scientific question and the available evidence determine the established analysis. Present only guidance whose objects, observations and operations match; allow the analyst to challenge it. Put a requirement into code only when its inputs and failure meaning are explicit and its behavior has been checked on valid as well as defective examples.

For example, a data-use relation can support a narrow warning that an observation fitted to a specified result is being called independent validation of that same result. It cannot be established merely by finding the word “validation” in an answer. Likewise, periodic-coordinate handling must follow the intended physical distance; it is not a universal half-box test.

This is a recommendation to reduce unsupported complexity, not a completed comparison proving that the proposed organization is best. A future intervention should target one demonstrated failure, keep the other conditions fixed, and retain the current results if the repair fails.
