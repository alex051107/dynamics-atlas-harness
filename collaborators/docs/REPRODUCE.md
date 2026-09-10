# Reproduce the main scientific numbers

## Requirements

Use Docker Desktop or Docker Engine, or an existing Python 3.11+ installation. The calculation uses only the Python standard library: there is no package installation, API key, provider account, GPU or paid model call. Inputs are included and total about 1.1 MB. The first Docker build requires internet access to obtain the public base image; execution can remain offline.

## Docker: the fixed environment

From the `collaborators` directory, or the root of the standalone group ZIP:

```bash
docker build -t dynamics-atlas-group:20260910 .
mkdir -p results
docker run --rm --network none --read-only --tmpfs /tmp \
  --mount "type=bind,source=$(pwd)/results,target=/output" \
  dynamics-atlas-group:20260910
```

The Dockerfile uses a public Python image pinned by digest. It does not depend on the developer's local image name or filesystem. The container reads `/app/data` and writes `/output`; only your chosen results directory is mounted. No privileged mode or Docker socket is needed.

On Windows PowerShell:

```powershell
docker build -t dynamics-atlas-group:20260910 .
New-Item -ItemType Directory -Force results
docker run --rm --network none --read-only --tmpfs /tmp --mount "type=bind,source=$($PWD.Path)/results,target=/output" dynamics-atlas-group:20260910
```

## Existing Python: no installation

```bash
python3 reproduce/reproduce.py --data data --output results
```

On Windows use `py -3` instead of `python3` if that is your installed interpreter. The fixed Docker environment is preferred when sharing a runtime identity; the Python alternative is tested separately and uses the same script and data.

## Expected outputs

The command must print `PASS: HSP90, DHFR and ADK table-to-report reproduction` and exit with code 0. It creates:

- `results/REPORT.html`: a standalone readable result page.
- `results/REPORT.md`: the same result in Markdown.
- `results/results.json`: exact values, window definitions and per-trajectory HSP90 classifications.

Main checks are HSP90's 5/5/10 direction partition and 9/1/0 versus 1/1/18 native-reference classifications; four DHFR M20 means; and four ADK domain-distance changes. See the methods for denominators and windows. Repeated execution replaces files only in the output directory.

## Troubleshooting

A failed checksum means an input differs from the delivered package. Restore that input rather than changing an expected number. A missing-file error usually means the command was run outside the package root; pass `--data` explicitly. A Docker pull failure affects environment acquisition, not the scientific computation; an existing Python 3.11+ installation can run it without downloads.

If a bind mount cannot be written on Linux, run Docker with your user's IDs (`--user "$(id -u):$(id -g)"`) after creating the results directory. Do not mount your home directory or credentials.

## Raw-coordinate reconstruction is a separate task

The source deposits and prior physical checks are identified in SOURCES.md. This portable route starts from the corrected and frozen analysed tables. It does not install GROMACS or VMD and does not claim to regenerate the tables from raw coordinates. Those extra tools and the original full trajectories would be required for that broader reproduction.
