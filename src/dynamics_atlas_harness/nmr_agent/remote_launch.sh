#!/bin/bash
# Start the NMR MCP tool server on a Longleaf compute node; stdio goes through ssh (see remote_tools.py).
#
# On the login node:  remote_launch.sh CORES MEM <mcp_server args...>
#   default        : srun -p general -c CORES --mem MEM -t 3:00:00 (one allocation per run; exits with the run)
#   NMR_SERVE_NODE : ssh into that already-allocated node instead (mode b; start one with start_serve_node.sh)
# On the node (internal):  remote_launch.sh --on-node <mcp_server args...>
#
# Env passed through from the caller: NMR_CORES, NMR_REMOTE_RUN_DIR, DYNAMICS_ATLAS_POTENCI, NMR_AGENT_WORKFLOW_FILE.
B="${NMR_REMOTE_ROOT:?set NMR_REMOTE_ROOT to the remote dynamics_atlas_nmr directory}"
R=$B/agent_remote
if [ "${1:-}" = "--on-node" ]; then
  shift
  export PYTHONPATH=$R/src PYTHONWARNINGS=ignore PYTHONUNBUFFERED=1
  C=${NMR_CORES:-8}
  export OMP_NUM_THREADS=$C OPENBLAS_NUM_THREADS=$C MKL_NUM_THREADS=$C VECLIB_MAXIMUM_THREADS=$C
  if [ -n "${NMR_REMOTE_RUN_DIR:-}" ]; then
    mkdir -p "$NMR_REMOTE_RUN_DIR"
    echo "node=$(hostname) slurm_job=${SLURM_JOB_ID:-none} cores=$C start=$(date '+%F %T')" >> "$NMR_REMOTE_RUN_DIR/remote_node.txt"
  fi
  exec "$B/venv_agent/bin/python" -m dynamics_atlas_harness.nmr_agent.mcp_server "$@"
fi
CORES=$1; MEM=$2; shift 2
export NMR_CORES=$CORES
if [ -n "${NMR_SERVE_NODE:-}" ]; then
  envs=""
  for v in NMR_CORES NMR_REMOTE_RUN_DIR DYNAMICS_ATLAS_POTENCI NMR_AGENT_WORKFLOW_FILE; do envs="$envs $v=$(printf '%q' "${!v:-}")"; done
  exec ssh -T -o BatchMode=yes -o StrictHostKeyChecking=no "$NMR_SERVE_NODE" "env$envs bash $R/src/dynamics_atlas_harness/nmr_agent/remote_launch.sh --on-node $(printf '%q ' "$@")"
fi
exec srun -p general -c "$CORES" --mem "$MEM" -t 3:00:00 -J nmr_mcp --export=ALL bash "$R/src/dynamics_atlas_harness/nmr_agent/remote_launch.sh" --on-node "$@"
