# Dynamics Atlas

**Reproducible analysis of heterogeneous protein-dynamics evidence.**

Dynamics Atlas compares what simulations and experiments support about a protein's conformations and dynamics. The goal is a useful scientific answer with explicit assumptions, traceable calculations and clear limits.

## For the research group

**Start with the [clean collaborator package](collaborators/README.md).** It contains English scientific results, methods, primary sources and a small offline reproduction environment.

| Read | Purpose |
|---|---|
| [Scientific results](collaborators/docs/RESULTS.md) | HSP90, DHFR and ADK findings and their interpretation |
| [Methods](collaborators/docs/METHODS.md) | Observables, statistical units, windows and physical representation |
| [Reproduce the results](collaborators/docs/REPRODUCE.md) | Fixed Docker environment or dependency-free Python |
| [Rules Table research](collaborators/docs/RULES.md) | The scientific role of rules and what the pilot established |
| [Primary sources](collaborators/docs/SOURCES.md) | Papers, deposits and numerical provenance |

The tested reproduction route recalculates the main report numbers from supplied analysed tables. It does not generate new MD or rebuild coordinates from raw trajectories. This distinction is explicit in the instructions.

Download the [standalone group package](collaborators/downloads/Dynamics_Atlas_Group_Package_20260910.zip) to read and reproduce the results without navigating the development repository.

## Current scientific findings

- HSP90 open-direction motion and agreement with native NOE references are different outcomes.
- Corrected DHFR local distances show an inhibitor-dependent proximity difference within the deposited trajectories.
- ADK endpoint-window domain descriptors do not show joint closure in either apo trajectory.

Rules remain an auditable scientific knowledge resource. Their automated use showed mixed results in the pilot; a stable incremental benefit has not been established.

## Repository organization

| Area | Audience and contents |
|---|---|
| `collaborators/` | Self-contained group-facing scientific package, entirely in English |
| `src/`, `tests/`, `pyproject.toml` | Prototype implementation and engineering tests |
| [Research records](research/README.md) | Maintainer-only navigation to historical experiments and review evidence |

Historical files retain their original paths and languages to preserve citations and frozen inputs. They are not the group-facing documentation. The current delivery is on the feature branch under draft PR #27; it has not been merged into `main`.
