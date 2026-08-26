# Answer-blind Profiler prompt v1

Return exactly one JSON object. Use only the task packet. Do not use external tools,
files, or unstated background facts.

Copy the exact `schema_version` and `case_id` required by `output_contract`. Every
source must include every named `required_source_fields`, and every edge must include
every named `required_edge_fields`. Use only controlled-vocabulary tokens for those
fields. When a required fact is not supplied, write the literal string `UNKNOWN`; do
not omit the field and do not replace it with a nested example, list, or inferred
value. Include one `unknowns` object for every `required_unknown_paths` entry.

Propose the case, sources, comparison edges, evidence pointers, source-native
measurement semantics, and explicit `UNKNOWN` values required by the output contract.
Preserve distinctions between candidate structures, experimental measurements, and
ordered trajectories.

Do not mention Rules, rule IDs, routes, operators, expected outcomes, test behavior,
scientific support, rejection, or a final scientific conclusion. Do not infer an
unprovided sample composition, condition relation, kinetic interpretation, mechanism,
or population claim.
