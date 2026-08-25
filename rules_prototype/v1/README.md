# Rules Prototype v1

This directory is the review package for the next Rules Table design. It is not an
active runtime package.

The package is derived from the existing review-led audit in the Dynamics Atlas
workspace. It keeps the fourteen-family methodology map and the complete thirty-three
rule re-audit, then selects exactly eight seed families for human review. The seed
families cover the current reusable core. Two proposed scientific gaps remain deferred
until primary-case replay, and the action router remains a Harness component.

## Files

- `methodology_map_v1.json` records all fourteen reviewed families and their prototype
  disposition.
- `legacy_33_rule_reaudit.csv` is an exact copy of the existing thirty-three-rule audit;
  it preserves lineage and does not become a second authoring authority.
- `seed_rule_registry_v1.json` defines the eight proposed reusable rule families.
- `seed_bindings_v1.json` states when each family would be instantiated against typed
  CASE, SOURCE, or EDGE fields.
- `resolution_policies_v1.json` defines the allowed next-action classes without
  authorizing an operator automatically.
- `evaluation_contracts_v1.json` defines the evidence-result shape and outcome effects
  for each seed family.
- `source_manifest_v1.json` records upstream locators and source identity.

## Deliberate exclusions

- `RF02` sample composition stays `CANDIDATE_PENDING_PRIMARY_CASE`.
- `RF07` claim-conditioned MD sampling stays `CANDIDATE_PENDING_MD_REPLAY`.
- `RF12` action and registered-operator routing stays `SYSTEM_COMPONENT`.

No file here changes the frozen v0.3 selector, bindings, compiled index, or historical
results. A future activation must be a separate reviewed change.
