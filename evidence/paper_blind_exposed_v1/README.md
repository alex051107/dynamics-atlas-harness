# HSP90 and ADK paper-blind public packets

This directory prepares two exposed inputs for a later paper-blind scientific
decision exercise. HSP90 provides a permitted NMR context plus an ordered MD
observable and row-aligned trajectory identities. ADK provides two endpoint
coordinate derivatives and their source context. DHFR is absent so its later
first-run role remains intact.

The current code validates three things:

- public packets exclude canonical CaseGraphs, expected Rules/routes, paper or
  expert conclusions, Discussion, and Conclusion;
- each data asset still matches its frozen identity record; and
- an Agent can propose only source references, explicit unknowns, and a rationale.

The Agent-visible packet does not include the platform authority envelope. It
cannot see permitted capabilities, execution constraints, or claim ceilings;
the deterministic platform retains those fields and currently authorizes no
execution.

No numerical analysis runs from these packets. They create no RuleInstance,
RuleResult, EvidenceResult, Operator route, scientific conclusion, or portability
result. The HSP90 trajectory identifiers stay alongside the observable so a later
real analysis cannot silently pool rows without preserving their declared identity.

The frozen arrays and manifest are identity records for future, separately
authorized work. They are not a general capability registry, a hidden reference,
or a paper-conclusion recovery result.
