from pathlib import Path
import json,csv
import numpy as np
p=Path('autoresearch/tasks/dynamics_atlas_paper_result_reproduction_screen_20260904');o=p/'outputs/q01_absolute_paths_v1';r=json.loads((o/'numerical_report.json').read_text());receipt=json.loads((o/'receipt.json').read_text());old=json.loads((p/'outputs/q01_relative_paths_v1/numerical_report.json').read_text());new=json.loads((p/'outputs/q01_relative_replay_v2/numerical_report.json').read_text());assert old==new
assert len(r['rows'])==40 and len({row['trajectory']for row in r['rows']})==40
assert r['relative_summary_unchanged']==old['grouped']
assert receipt['on_operator_calls']==1 and receipt['off_operator_calls']==0 and receipt['new_GROMACS_calls']==0 and receipt['new_optimizations']==0
count=0;identity=set()
with(o/'full_absolute_paths.tsv').open()as f:
 for row in csv.DictReader(f,delimiter='\t'):
  count+=1;key=(row['trajectory'],row['method'],float(row['time_ns']));assert key not in identity;identity.add(key)
assert count==80080
for row in r['rows']:
 data=np.load(o/(row['trajectory']+'.npz'),allow_pickle=False)
 for field,key in [('displacement_from_20ns_A','lid_displacement_from_20ns_A'),('nearest_open_MD_lid_rmsd_A','nearest_open_MD_lid_rmsd_A')]:
  assert np.isclose(np.median(data[field][-20:]),row['absolute_metrics'][key]['first20_to_last20']['after_median'],atol=1e-12,rtol=0)
  assert np.all(np.isfinite(data[field])) and np.all(data[field]>=0)
 assert data['displacement_from_20ns_A'][0]<1e-10
es=next(row for row in r['rows']if '_ES17_'in row['trajectory'])
assert [es['methods'][m]['events_by_persistence']['20'][0]['event_contact_internal_disagreement_frames']for m in ['deposited_uniform','SI_per_contact']]==[41,42]
assert all((o/f).stat().st_size>10000 for f in ['absolute_paths_summary.png','absolute_paths_summary.pdf'])
result={'status':'PASS','trajectories':40,'unique_full_path_rows':count,'old_relative_numerics_identical':True,'ES17_first_event_internal_disagreement':[41,42],'terminal_metrics_checked_from_40_derivative_arrays':True,'new_GROMACS':0,'new_optimizations':0,'full_scientific_acceptance':'PENDING_QUESTION_LEVEL_REVIEW','graphically_reviewed':True,'visual_fix':'Moved annotations clear of data; no scientific recomputation'}
(o/'artifact_validation.json').write_text(json.dumps(result,indent=2)+'\n');(p/'scripts/q01_absolute_artifact_check_v1.py').write_text(Path('/tmp/q01_artifact42.py').read_text());print(json.dumps(result))
