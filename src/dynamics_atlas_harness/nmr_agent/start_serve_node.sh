#!/bin/bash
# Mode (b): hold one multi-core node for several runs. Run on the login node (or: ssh longleaf bash <this>).
# Then export NMR_SERVE_NODE=$(cat .../agent_remote/serve_node.txt) before launching with REMOTE_TOOLS=1.
# Cancel with: scancel -n nmr_serve
R=/work/users/l/i/liualex/dynamics_atlas_nmr/agent_remote
rm -f "$R/serve_node.txt"
sbatch -p general -c "${1:-16}" --mem "${2:-32G}" -t "${3:-12:00:00}" -J nmr_serve -o "$R/serve_node.log" \
  --wrap "hostname > $R/serve_node.txt; sleep infinity"
