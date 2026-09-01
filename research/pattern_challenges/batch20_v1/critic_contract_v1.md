# Batch20 Blind Critic Contract v1

## Purpose

This contract implements the bounded blind spot-check authorized by `DA-20260901-064`.
It asks whether a fresh advisory context can reconstruct a safe family, target,
RuleInstance, status, blocker, route, and claim ceiling from a bounded source-first view.
It is not a scientific review, a canonical-Rules validation, a held-out evaluation, or an
Agent-value test.

## Exact visible inputs

Each fresh Critic receives exactly one case file listed in
[`critic_visible_input_manifest.json`](critic_visible_input_manifest.json), this fixed
instruction, and the output vocabulary in
[`critic_output_schema.json`](critic_output_schema.json). Each case file contains only:

- a sanitised source-first view copied from the frozen Pass A record: source identity and
  exact locators, source objects, atomic supported statements, missing information, and
  authority boundary;
- the frozen seven-family/twelve-Rule inventory, with family status, canonical target kind,
  question, and narrow claim-effect summary.

The Critic must not receive or retrieve the frozen manifest unit, frozen Pass B projection,
analyst family/target/RuleInstances, expected status, case route, case claim ceiling, prior
Critic verdict, candidate repair, full source text, external search result, or another case.
The visible-input manifest records the exact exclusions and a SHA-256 identity for each
case file.

## Fixed Critic instruction

Using only the supplied visible input, independently select one or more applicable frozen
families and RuleInstances, or abstain if no family/rule is supportable. Identify the
canonical target for every selected RuleInstance; give a local status, first blocker, legal
resolution route, and narrow claim ceiling. Flag an unsafe false-PASS risk only when the
visible record would make a PASS unsafe. Do not propose a patch. Do not reveal hidden
reasoning: return one JSON object that conforms to `critic_output_schema.json`.

For Case 018 specifically, family selection is genuinely open: the Critic may select a
family/rule or abstain. The historical Case 018 record is an abstention control, not an
answer key for this reconstruction.

## Execution boundary

There are exactly five fresh, non-persistent, case-isolated advisory contexts: Cases 003,
008, 010, 012, and 018. The only permitted local read is the declared case dossier; external
retrieval and any other repository inspection are forbidden. No automatic retry is allowed. A malformed or unavailable result
is recorded as `PENDING_BLIND_REVIEW`, not repaired by a fallback or a new batch. The model
output is advisory and cannot modify canonical files, H1, scientific dispositions, or
candidate patch eligibility by itself.

## Output handling

Persist the raw JSON object as a case-isolated blind output. Validate only its schema and
visible-input identity before aggregation. Compare its conclusion to the repaired
task-local projection in a separate human-readable audit; do not retrofit the frozen Pass A,
Pass B, or prior Critic object to make the output agree.
