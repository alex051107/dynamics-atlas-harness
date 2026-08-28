## Plan position

- Plan ID:
- Frozen Plan semantic milestone:
- GitHub delivery PR number:
- Current authorization source:
- Required Exit Gate:

## Review context

- Original objective and why now:
- Actual behavioral change:
- Focused validation:
- Deliberately excluded work:
- Open review invitation: Independently challenge the framing, identify a better or
  smaller solution, flag a missing risk, or recommend stopping/reverting if warranted.

## Observed gap

State the observed repository, evidence, or workflow gap. Separate observation from inference.

## Change made

Describe the bounded change.

## Contracts affected

- [ ] No frozen/public contract changed
- [ ] Profile / CaseGraph
- [ ] Rules workspace adapter or frozen asset manifest
- [ ] Evaluation Contract / RunPlan
- [ ] OperatorSpec / execution authorization
- [ ] Claim boundary or documentation

## Assets kept frozen

List the scientific evidence, rules authority, fixtures, manifests, schemas, or baseline assets deliberately left unchanged.

## Validation actually run

List exact commands, invocation counts, and results.

## Validation intentionally skipped

List duplicate or out-of-scope checks that were skipped and the risk-based reason.

## Claim boundary

- Allowed claim:
- Forbidden upgrade:
- Human decision required:

## Remaining risk

List unresolved evidence, implementation, portability, or scientific risks.

## Next authorized action

State the one next action allowed by the current execution status and the mandatory stop point.

## Data and repository safety

- [ ] No credentials, `.env`, absolute personal paths, raw/derived scientific payload, or `runs/` content
- [ ] Upstream Rules authority was referenced, not copied
- [ ] Frozen asset hashes were updated only when inputs intentionally changed
- [ ] No later frozen-plan stage was started without its prior Exit Gate and human authorization
- [ ] Any plan deviation was appended to `governance/deviations.jsonl`
