"""Frozen source-consistency checks. No expected-defect labels or packet-name logic."""
from pathlib import Path
import csv,json,numpy as np

def check(packet,reference):
 d=json.loads((packet/'DECLARED_METADATA.json').read_text());a=json.loads((reference/'SOURCE_AUTHORITY.json').read_text());flags=[];details=[]
 if d['system']!=a['system']:flags.append('object_identity')
 if d['evidence_role']!=a['evidence_role']:flags.append('evidence_role')
 if d['candidate_pool']!=a['candidate_pool']:flags.append('candidate_pool_lineage')
 trusted={t['file']:t for t in a['tables']};assert set(trusted)=={t['file']for t in d['tables']}
 for t in d['tables']:
  expected=trusted[t['file']];rows=list(csv.DictReader((packet/t['file']).open(),delimiter='\t'));ref=list(csv.DictReader((reference/t['file']).open(),delimiter='\t'));local=[]
  for key in ['condition','unit','statistical_unit','independent_replicates','candidate_pool']:
   if t[key]!=expected[key]:local.append(key)
  if len(rows)!=expected['rows'] or len(rows)!=t['rows']:local.append('frame_count')
  tc=t['time_column'];groups={}
  for row in rows:groups.setdefault(row[t['time_group']]if t.get('time_group')else'all',[]).append(float(row[tc]))
  if any(not np.all(np.diff(v)>0)for v in groups.values()):local.append('time_order')
  if len(rows)==len(ref):
   if any(float(x[tc])!=float(y[tc])for x,y in zip(rows,ref)):local.append('time_source_alignment')
   cols=[]
   for col in rows[0]:
    if col==tc or col==t.get('time_group'):continue
    try:np.array([float(z[col])for z in rows]);cols.append(col)
    except ValueError:pass
   matrix=np.array([[float(x[c])for c in cols]for x in rows]);refmatrix=np.array([[float(x[c])for c in cols]for x in ref]);error=np.abs(matrix-refmatrix);maxerr=float(error.max());ncols=int(np.any(error>a['reference_tolerance_A'],axis=0).sum())
   if not np.isfinite(matrix).all():local.append('nonfinite')
   if maxerr>a['reference_tolerance_A']:local.append('observable_differs_from_validated_representation')
  else:maxerr=None;ncols=None
  flags.extend(local);details.append({'file':t['file'],'flags':local,'max_absolute_discrepancy_A':maxerr,'columns_above_tolerance':ncols})
 physical=reference/'PHYSICAL_SOURCE_CHECK.json'
 if physical.exists():
  p=json.loads(physical.read_text());ok=(p.get('status')=='PASS')if 'status'in p else all(x['pass']for x in p['results'])
  if not ok:flags.append('source_physical_validation')
 return {'status':'FAIL'if flags else'PASS','flags':sorted(set(flags)),'details':details,'checks':['object_conditions','time_semantics','statistical_unit','observation_window','evidence_role','candidate_pool_lineage','physical_source_consistency'],'scope':'Verified source-consistency; no biological validity claim; missing authorities are execution error, not automatic PASS'}
if __name__=='__main__':
 import sys
 print(json.dumps(check(Path(sys.argv[1]),Path(sys.argv[2])),indent=2))
