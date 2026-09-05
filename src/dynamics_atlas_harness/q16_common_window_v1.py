"""Developmental Q16 obligation: finite matched-window signal comparison.

No DEER inversion, fitted populations or statistical significance. Deposited fit
curves are excluded; raw, observed processed and raw/background signals retain
separate roles. Centering/scaling is an explicit shape-only nuisance convention.
"""
from __future__ import annotations
import hashlib
import json
import math

RULE_ID='Q16R01_COMMON_WINDOW_CONDITION_CONTRAST_V1'
OPERATOR_ID='q16_common_window_contrast_v1'
POLICY={'version':1,'window':'intersection_of_nonnegative_observed_processed_grids_per_pair','alignment':'exact_rounded_9_decimal_us_no_interpolation','shape':'center_and_divide_population_RMS','scientific_ceiling':'DESCRIPTIVE_SIGNAL_CONTRAST_NO_STATE_POPULATIONS'}

def identity(payload):
 return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(',',':'),allow_nan=False).encode()).hexdigest()

def validate_input(payload):
 if payload.get('doi')!='10.1038/s41467-022-31945-6' or payload.get('policy')!=POLICY:
  raise ValueError('SOURCE_OR_POLICY_MISMATCH')
 expected={'29':{'eg50_1mM','eg50_10mM','eg0_1mM','eg25_1mM','gly25_1mM'},'36':{'eg50_1mM','eg50_10mM','eg0_1mM'}}
 if set(payload['pairs'])!=set(expected):raise ValueError('PAIR_COVERAGE')
 for pair,conditions in payload['pairs'].items():
  if set(conditions)!=expected[pair]:raise ValueError('CONDITION_COVERAGE')
  for record in conditions.values():
   if record.get('role')!='AUTHOR_DEPOSITED_OBSERVED_DEER_TRACES':raise ValueError('SOURCE_ROLE')
   for key,width in [('raw',4),('processed',2)]:
    rows=record[key]
    if len(rows)<3 or any(len(row)!=width or not all(math.isfinite(x) for x in row) for row in rows):raise ValueError('INVALID_TRACE')
    if any(b[0]<=a[0] for a,b in zip(rows,rows[1:])):raise ValueError('GRID_ORDER')
   if any(row[2]<=0 for row in record['raw']):raise ValueError('NONPOSITIVE_BACKGROUND')
 return identity(payload)

def stats(x,y):
 n=len(x);mx=sum(x)/n;my=sum(y)/n
 sx=math.sqrt(sum((v-mx)**2 for v in x)/n);sy=math.sqrt(sum((v-my)**2 for v in y)/n)
 if min(sx,sy)<=1e-12:raise ValueError('NO_SHAPE_INFORMATION')
 zx=[(v-mx)/sx for v in x];zy=[(v-my)/sy for v in y]
 return dict(n=n,rmse=math.sqrt(sum((a-b)**2 for a,b in zip(x,y))/n),shape_distance=math.sqrt(sum((a-b)**2 for a,b in zip(zx,zy))/n),correlation=sum(a*b for a,b in zip(zx,zy))/n,reference_rms=sx,comparison_rms=sy)

def calculate(payload):
 input_id=validate_input(payload); results={}
 for pair,conditions in payload['pairs'].items():
  proc={k:{round(r[0],9):r[1] for r in v['processed'] if r[0]>=0} for k,v in conditions.items()}
  common=set.intersection(*(set(v) for v in proc.values()));times=sorted(common)
  if len(times)<20:raise ValueError('COMMON_WINDOW_TOO_SHORT')
  # All observed grid points inside the common support must be represented.
  if any({t for t in v if times[0]<=t<=times[-1]}!=common for v in proc.values()):raise ValueError('MISSING_COMMON_GRID_POINTS')
  signals={}
  for condition,record in conditions.items():
   raw={round(r[0],9):r for r in record['raw']}
   if not common.issubset(raw):raise ValueError('RAW_PROCESSED_GRID_MISMATCH')
   signals[condition]={'raw_real':[raw[t][1] for t in times],'observed_processed':[proc[condition][t] for t in times],'raw_over_deposited_background':[raw[t][1]/raw[t][2] for t in times]}
  reference=signals['eg50_1mM'];comparisons={}
  for c,s in signals.items():
   if c!='eg50_1mM':comparisons[c]={role:stats(reference[role],s[role]) for role in reference}
  ratios={}
  for role in reference:
   dose=comparisons['eg50_10mM'][role]['shape_distance'];protect=comparisons['eg0_1mM'][role]['shape_distance']
   ratios[role]=dict(protector_greater_than_dose=protect>dose,protector_over_dose=protect/dose if dose>1e-12 else None)
  results[pair]=dict(window_us=[times[0],times[-1]],n=len(times),comparisons=comparisons,ordering=ratios)
 return dict(operator_id=OPERATOR_ID,rule_id=RULE_ID,input_id=input_id,policy=POLICY,results=results,new_iterative_fits=0,full_question_answer=False)

def evaluate(payload,evidence=None,enabled=True):
 input_id=validate_input(payload)
 mismatch=any(len({v['processed'][-1][0] for v in c.values()})>1 for c in payload['pairs'].values())
 result=dict(rule_id=RULE_ID,rule_instance_id=RULE_ID+':'+input_id,input_id=input_id,development_adapter=True,status='UNRESOLVED',full_question_answer=False,actions=[],remaining=['STATE_REFERENCE_AND_INVERSION_IDENTIFIABILITY','EXPERIMENTAL_REPLICATION_AND_PREPARATION_UNCERTAINTY'])
 if not enabled:result['obligation']='DISABLED';return result
 if not mismatch:result['obligation']='NOT_TRIGGERED_EQUAL_WINDOWS';return result
 result['trigger_reason']='Observed processed recording durations differ across ligand/preparation conditions.'
 if evidence is None:
  result['obligation']='COMMON_WINDOW_COMPARISON_REQUIRED';result['actions']=[OPERATOR_ID];return result
 if evidence.get('input_id')!=input_id or evidence.get('rule_id')!=RULE_ID or evidence.get('operator_id')!=OPERATOR_ID or evidence.get('policy')!=POLICY or set(evidence.get('results',{}))!={'29','36'}:raise ValueError('EVIDENCE_BINDING_MISMATCH')
 # Validate received evidence against this deterministic, inexpensive operator.
 expected=calculate(payload)
 if evidence!=expected:raise ValueError('EVIDENCE_NUMERIC_MISMATCH')
 result['obligation']='COMMON_WINDOW_COMPARISON_COMPLETED'
 result['signal_ordering']={p:r['ordering'] for p,r in evidence['results'].items()}
 result['partial_claim']='OBSERVED_PREPARATION_SHAPE_CONTRAST_EXCEEDS_TESTED_DOSE_CONTRAST' if all(v['protector_greater_than_dose'] for r in result['signal_ordering'].values() for v in r.values()) else 'NO_CONSISTENT_ORDERING_ACROSS_PAIRS_AND_PROCESSING'
 result['claim_ceiling']='Descriptive within deposited traces; not significance, ligand saturation, causal isolation or closed-state population.'
 return result

def run(payload,enabled=True,operator=calculate):
 before=evaluate(payload,enabled=enabled);evidence=None;calls=0
 if before['actions']:
  evidence=operator(payload);calls=1
 after=evaluate(payload,evidence,enabled=enabled)
 return dict(before=before,evidence=evidence,after=after,operator_calls=calls)
