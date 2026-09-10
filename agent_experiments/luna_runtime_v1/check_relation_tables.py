"""Validate exact answer quotes; absence is explicitly not a quotation."""
import argparse,csv,json,re
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--outputs',type=Path,required=True);a=p.parse_args();seen={};errors=[];count=0
allowed={'AGREE','DISAGREE','PAPER_SILENT','AGENT_ABSTAIN','NOT_MENTIONED','NOT_REQUIRED','UNDETERMINED'}
for f in (a.outputs/'check').glob('*_literature_relation.csv'):
 data=f.read_text();run=f.name.removesuffix('_literature_relation.csv');answer=a.outputs/'AGENT_RAW'/run/'answer.md';lines=answer.read_text().splitlines()
 if data in seen:errors.append(f'identical tables: {run}/{seen[data]}')
 seen[data]=run
 if 'see matching claim audit' in data.lower():errors.append('placeholder '+run)
 for row in csv.DictReader(data.splitlines()):
  count+=1;q=row['agent_claim'];rel=row['relation']
  if rel not in allowed:errors.append('invalid relation '+run)
  if q:
   line=re.search(r':L(\d+)',row['answer_locator'])
   if len(q)>60 or not line or not(0<int(line[1])<=len(lines)) or q not in lines[int(line[1])-1]:errors.append('unlocated quote '+run+': '+q)
  elif rel not in {'NOT_MENTIONED','NOT_REQUIRED'}:errors.append('blank claim not explicitly absent '+run)
print(json.dumps({'pass':not errors,'tables':len(seen),'rows':count,'errors':errors},ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
