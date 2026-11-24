# Dynamics Atlas | Scientific Agent Runtime

An agent for inspecting protein-dynamics evidence. The model proposes a question, action, and draft claim. The runtime checks which data and tools can support that claim, runs authorized work, and keeps the result traceable.

[Engineering case study](https://alex051107.github.io/personal-website/research/dynamics-atlas.html) · [Public literature atlas](https://github.com/alex051107/dynamics-atlas-relaxdb/blob/main/PORTFOLIO.md)

## How the runtime works

```mermaid
flowchart TD
 A[Dataset, question and metadata] --> B[Model proposes an analysis action]
 B --> C{Check inputs, tool contract and authority}
 C -->|Approved action| D[Run registered computation or authorized lookup]
 C -->|Missing evidence or invalid action| H[Record a stop or request a narrower action]
 D --> E[Store a structured evidence result]
 E --> F{Does evidence support this claim scope?}
 F -->|Within scope| G[Record the scoped result]
 F -->|Outside scope| H
 H -->|New admissible evidence| B
```

**Engineering focus.** Action selection stays with the model. Admission rules, tool contracts, and claim limits stay in code. The public demo shows the decision pattern through recorded replay and synthetic checks.

**Two related artifacts.** This repository is the runtime; the separate RelaxDB atlas is a literature evidence product with its own workflow and release snapshots.

[Public synthetic harness](https://github.com/alex051107/projects/tree/main/scientific_evidence_harness) · [Runtime development notes](https://github.com/alex051107/dynamics-atlas-harness/tree/main)
