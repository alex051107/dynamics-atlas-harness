# Replay the recorded development sequence

Use the task layout described in ../q09_method_admission_v1/REPLAY.md and the exact public ZIP manifest. No final author fit parameters are inputs. Existing Python NumPy/SciPy required; not a dependency installer or registeredOperator.

Place ../q09_forward_v1/forward_source.py as scripts/q09_forward_v1.py; its check_source.py as scripts/check_q09_forward_v1.py. Place ../q09_pq_joint_v1/forward_source.py as scripts/q09_pq_joint_v1.py and execute it once for the initial output directory and checks. Place each q09_pq_joint_vN/runner_source.py as scripts/run_q09_pq_joint_vN.py. Run v1, v2, v3 in order to preserve the actual diagnostic failures and reuses;v1's intentional nonzero stop must be inspected before continuing. Each runner writes a new outputdirectory. Run with OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 for the recorded bounded CPU configuration.

The v1 donor_gradient_audit.json records an independent local gradient diagnostic. v2 and v3 source snapshots record the numerical repairs;scientific limits remain in REPORT_ZH.md. Per-bin raw/expected CSV is produced by a replay, while portable review output includes20aggregate residual blocks.
