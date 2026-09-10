# Dynamics Atlas

**Interpreting heterogeneous protein-dynamics evidence with reproducible analysis.**

We compare what molecular simulations and experiments actually support, including where their interpretations differ. The current results cover HSP90, DHFR and adenylate kinase (ADK). A source-linked Rules Table records scientific prerequisites and conclusion limits; its contribution to automated analysis is a separate research question.

## Start here

| Your goal | Read or run |
|---|---|
| Understand the project and current findings | [Scientific results](docs/RESULTS.md) |
| Understand the measurements and assumptions | [Methods and boundaries](docs/METHODS.md) |
| Reproduce the main numerical results | [Reproduction guide](docs/REPRODUCE.md) |
| Understand the Rules Table's research role | [Rules and analysis protocol](docs/RULES.md) |
| Find papers and data sources | [Sources and data provenance](docs/SOURCES.md) |

## What we have learned

- **HSP90:** moving in an open direction is different from agreeing with an open-state NOE reference.
- **DHFR:** corrected local distances distinguish the two inhibitors in these trajectories; coordinate representation must be checked before interpretation.
- **ADK:** the selected domain-distance descriptors do not show joint closure over the first-to-last-window comparison in either apo trajectory.

The calculations below reproduce those numerical summaries from the provided analysed tables. They do not generate new MD trajectories or repeat raw-coordinate preparation.

## Reproduce in a fixed environment

From this directory, with Docker installed:

```bash
docker build -t dynamics-atlas-group:20260910 .
mkdir -p results
docker run --rm --network none --read-only --tmpfs /tmp \
  --mount "type=bind,source=$(pwd)/results,target=/output" \
  dynamics-atlas-group:20260910
```

Open `results/REPORT.html`. A successful run prints `PASS` and writes the report plus `results.json`. The base image is pinned by digest. Building downloads that public base image; the calculation itself runs without network access or an API key. The Python-only alternative and Windows instructions are in the [reproduction guide](docs/REPRODUCE.md).

You can also inspect the [tested example output](example-results/REPORT.html) before running the calculation.

## Package layout

```text
README.md           Project entrypoint
index.html          Offline reading page
Dockerfile          Digest-pinned public Python environment
docs/               Scientific results, methods, reproduction and sources
data/               Small numerical inputs and their provenance manifest
reproduce/          Deterministic analysis script
example-results/    Output from the tested container run
results/            Your regenerated outputs
```

This group package is self-contained. Its numerical inputs come from the recorded September 2026 analyses. Exact source archive identities and transformations are documented in `data/MANIFEST.json`.
