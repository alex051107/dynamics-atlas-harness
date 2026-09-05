"""Inventory deposited Q16 curves; no fitting or state classification."""
import json, math
from pathlib import Path
TASK=Path(__file__).resolve().parents[1]
# Source block start columns. First4 raw, next3 processed, next4 inverse distribution.
BLOCKS=[('Figure5','36_apo','AC'),('Figure5','36_eg50_1mM','AQ'),('Figure5','29_apo','CG'),('Figure5','29_eg50_1mM','CU'),('Figure5','29_eg0_1mM','DI'),('Figure5','36_eg0_1mM','DT'),('SI Figure9','36_eg50_10mM','A'),('SI Figure9','29_eg50_10mM','L'),('SI Figure10','29_eg0_1mM','A'),('SI Figure10','29_gly25_1mM','N'),('SI Figure10','29_eg25_1mM','AA'),('SI Figure10','29_eg50_1mM','AN'),('SI Figure10','36_eg0_1mM','BA'),('SI Figure10','36_eg50_1mM','BN')]
def colnum(s):
 n=0
 for c in s:n=n*26+ord(c)-64
 return n
def col(n):
 s=''
 while n:n,a=divmod(n-1,26);s=chr(65+a)+s
 return s

def main():
 out=TASK/'outputs/q16_condition_inventory_v1';out.mkdir(exist_ok=False)
 sheets={s:{c['cell']:c for c in json.loads((TASK/'outputs/q15_complete_workbook_v1'/f'{s}.source_cells.json').read_text())} for s,_,_ in BLOCKS}
 records=[];arrays={}
 for sheet,condition,start in BLOCKS:
  cells=sheets[sheet];n=colnum(start);key=sheet+':'+condition
  record=dict(key=key,condition=condition,source_label=cells[start+'1']['value'],source_sheet=sheet,roles={})
  arrays[key]={}
  for role,offset,count in [('raw',0,4),('processed',4,3),('distribution',7,4)]:
   columns=[col(n+offset+j) for j in range(count)]; rows=[]
   for i in range(5,3000):
    values=[cells.get(c+str(i)) for c in columns]
    if all(v and v['type']=='n' for v in values):
     row=[float(v['value']) for v in values];assert all(map(math.isfinite,row));rows.append(row)
   assert rows,(key,role)
   grid=[r[0] for r in rows];steps=[b-a for a,b in zip(grid,grid[1:])]
   assert min(steps)>0,(key,role)
   arrays[key][role]=rows
   record['roles'][role]=dict(columns=columns,headers=[cells.get(c+'3',{}).get('value') for c in columns],n=len(rows),grid_min=grid[0],grid_max=grid[-1],step_min=min(steps),step_max=max(steps),rows_start=5)
   if role=='distribution':
    record['roles'][role].update(nonnegative_central=all(r[1]>=0 for r in rows),column_upper_le_lower=sum(r[2]<=r[3] for r in rows),central_inside_unordered_band=sum(min(r[2:])<=r[1]<=max(r[2:]) for r in rows))
  records.append(record)
 duplicates=[]
 for i,a in enumerate(records):
  for b in records[i+1:]:
   if a['condition']==b['condition']:
    duplicates.append(dict(left=a['key'],right=b['key'],equal_by_role={role:arrays[a['key']][role]==arrays[b['key']][role] for role in arrays[a['key']]}))
 report=dict(status='SOURCE_CURVE_INVENTORY_NOT_STATE_VERDICT',source_workbook='41467_2022_31945_MOESM4_ESM.xlsx',records=records,duplicate_checks=duplicates,uncertainty_role='DeerAnalysis validation envelope; not independent repeats or likelihood standard errors',source_conditions='SIphysical9 caption +=1mM,++=10mM maltose; main Fig5 narrative default50percentethylene glycol. SIphysical10 varyingprotector; exactlabels preserved.',fits=0,scientific_verdict=None)
 (out/'report.json').write_text(json.dumps(report,indent=2)+'\n');(out/'source_curves.local.json').write_text(json.dumps(arrays)+'\n')
 for r in records:print(r['key'],r['source_label'],[(k,v['n'],v['grid_min'],v['grid_max']) for k,v in r['roles'].items()])
 print('DUPLICATES',duplicates)
if __name__=='__main__':main()
