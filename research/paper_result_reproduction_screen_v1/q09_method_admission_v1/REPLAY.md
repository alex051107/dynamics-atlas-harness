# Replay scope

The two Q09 scripts are source snapshots, not registered Operators. To replay, use a task directory with scripts/, inputs/q09_author/unpacked/eTCSPC/, and outputs/. Obtain the exact author ZIP listed in input_manifest.json, verify its published MD5, and extract under the stated input directory. Place source_snapshot.py as scripts/q09_decay_admission_v1.py and mapping_source.py as scripts/q09_method_mapping_v1.py. Create outputs/q09_method_admission_v1/ before the mapping script. Run with Python standard library. No author final distances or populations are inputs. Raw payloads/PDFs are not republished here.

The Q05 geometry files are conditional preparation only. Its check_source.py assumes the task-layout topology path and imports q05_shape_geometry_v1; rename geometry_source.py accordingly in scripts/. Neither script reads a trajectory.
