"""Recompute three reported scientific summaries from archived analysed tables.

Python standard library only. No network, model API, hidden key or raw-MD execution.
"""
import argparse,collections,csv,gzip,hashlib,html,json,math,statistics,sys
from pathlib import Path

def load(path):
 opener=gzip.open if path.suffix=='.gz' else open
 with opener(path,'rt',newline='')as f:return list(csv.DictReader(f))

def near(value,reference,tol=1e-5):
 if not math.isfinite(value) or abs(value-reference)>tol:raise ValueError(f'Result mismatch: {value} versus expected {reference}; tolerance {tol}')

def run(data):
 manifest=json.loads((data/'MANIFEST.json').read_text())
 for f in manifest['files']:
  p=data/f['file']
  if hashlib.sha256(p.read_bytes()).hexdigest()!=f['sha256']:raise ValueError('Input integrity mismatch: '+f['file'])
 adk={}
 for state,n,deltas in [('open',2253,[.0707211184,2.2904106995]),('closed',1678,[1.0908948441,1.1764212186])]:
  rows=load(data/f'adk_{state}.csv');assert len(rows)==n;k=n//10
  times=[float(x['time_ns'])for x in rows];assert all(abs(t-i*.2)<1e-8 for i,t in enumerate(times))
  values={}
  for domain,expected in zip(['NMP','LID'],deltas):
   a=[float(x[domain+'_CORE_mean_CA_distance_A'])for x in rows];delta=statistics.fmean(a[-k:])-statistics.fmean(a[:k]);near(delta,expected)
   values[domain]={'first_mean_A':statistics.fmean(a[:k]),'last_mean_A':statistics.fmean(a[-k:]),'change_A':delta,'median_A':statistics.median(a)}
  adk[state]={'frames':n,'window_frames':k,'first_window_ns':[times[0],times[k-1]],'last_window_ns':[times[-k],times[-1]],'domains':values}
 dhfr={};groups=collections.defaultdict(list)
 for x in load(data/'dhfr_m20.csv'):groups[x['condition']].append(x)
 expected={'tmpp-wt':8.687677,'d4tmpp-wt':4.622056,'tmpp-l28r':10.435783,'d4tmpp-l28r':4.808910}
 for condition,ref in expected.items():
  all_rows=groups[condition];assert len(all_rows)==1001, 'DHFR source must retain all 1001 frames'
  rows=[x for x in all_rows if int(x['frame_index'])>=11]
  assert len(rows)==990 and [int(x['frame_index'])for x in rows]==list(range(11,1001)), 'DHFR analysis window must be frames11–1000'
  mean=statistics.fmean(float(x['M20_O3P_A'])for x in rows);near(mean,ref);dhfr[condition]={'frames':len(rows),'M20_O3P_mean_A':mean}
 by=collections.defaultdict(list)
 for x in load(data/'hsp90_frames.csv.gz'):by[x['trajectory']].append(x)
 assert len(by)==40
 partition=collections.Counter();sensitivity={};trajectory_results=[]
 for tau in [.5,1.,2.]:
  counts={'closed_seeded':collections.Counter(),'open_seeded':collections.Counter()}
  for tr,rows in by.items():
   assert len(rows)==1001 and [float(x['time_ns'])for x in rows]==list(range(20,1021))
   seed=rows[0]['seed'];mask=[x for x in rows if float(x['geometry_delta_A'])>0 and float(x['contact_margin_A'])>0]
   fraction=lambda predicate:sum(predicate(x)for x in mask)/len(mask)if mask else None
   opened=fraction(lambda x:float(x['V_open_A'])<=tau and float(x['V_closed_A'])>tau)
   far=fraction(lambda x:float(x['V_open_A'])>tau and float(x['V_closed_A'])>tau)
   label='NOT_APPLICABLE'if not mask else('AGREEMENT'if opened>=.8 else('RELATIVE_ONLY'if far>=.5 else'PARTIAL'))
   counts[seed][label]+=1
   if tau==1:
    if seed=='closed_seeded':partition[rows[0]['partition_5']]+=1
    trajectory_results.append({'trajectory':tr,'seed':seed,'open_direction_frames':len(mask),'open_NOE_fraction_within_direction':opened,'both_far_fraction_within_direction':far,'judgment':label})
  sensitivity[str(tau)]={k:dict(v)for k,v in counts.items()}
 assert dict(partition)=={'ONLY_CLOSED':10,'FIRST_OPEN':5,'CLOSED_THEN_OPEN':5}
 assert sensitivity['1.0']['closed_seeded']=={'NOT_APPLICABLE':10,'RELATIVE_ONLY':9,'PARTIAL':1}
 assert sensitivity['1.0']['open_seeded']=={'AGREEMENT':18,'PARTIAL':1,'RELATIVE_ONLY':1}
 return {'status':'PASS','scope':'Recalculation from frozen analysed tables; no new MD or coordinate reconstruction','python':sys.version.split()[0],'HSP90':{'five_point_partition':dict(partition),'sensitivity_A':sensitivity,'trajectories':trajectory_results},'DHFR':dhfr,'ADK':adk}

def report(x):
 lines=['# Reproduced scientific summaries','', '**PASS: all three table-to-report comparisons match the published reference values.**','', 'This run recalculates results from the provided analysed tables. It does not regenerate coordinates, perform new MD, or establish independent experimental validation.','', '## HSP90','', 'At the five-point persistence setting, the 20 closed-start trajectories split into 5 initially open-direction, 5 later open-direction and 10 never open-direction.','', '| Native NOE tolerance / Å | Start group | Consistent | Partial | Relative only | No open-direction frames |','|---|---|---:|---:|---:|---:|']
 for tau,groups in x['HSP90']['sensitivity_A'].items():
  for group,c in groups.items():lines.append(f"| {tau} | {group} | {c.get('AGREEMENT',0)} | {c.get('PARTIAL',0)} | {c.get('RELATIVE_ONLY',0)} | {c.get('NOT_APPLICABLE',0)} |")
 lines+=['','The classification is conditional on frames with an open direction. Direction alone does not establish absolute reference agreement.','', '## DHFR','', '| Condition | Frames | Mean M20–O3P distance / Å |','|---|---:|---:|']
 for k,v in x['DHFR'].items():lines.append(f"| {k} | {v['frames']} | {v['M20_O3P_mean_A']:.6f} |")
 lines+=['','Each condition has one trajectory. Local proximity does not by itself establish hydrogen bonding, a unique mechanism or a dissociation rate.','', '## ADK','', '| Start | Domain | Frames per window | Last minus first window / Å |','|---|---|---:|---:|']
 for k,v in x['ADK'].items():
  for domain,a in v['domains'].items():lines.append(f"| {k} | {domain} | {v['window_frames']} | {a['change_A']:.6f} |")
 lines+=['','Positive changes indicate greater separation for the project-defined descriptors. Apo MD does not reproduce the ATP-photorelease experiment.','', '## Provenance','', 'The input manifest records the exact frozen archive, selected columns and checksums. See docs/METHODS.md and docs/SOURCES.md in the group package.','']
 return '\n'.join(lines)

def render_html(md):
 parts=[];table=[]
 def flush():
  if not table:return
  rows=[r for r in table if not all(c in '|-: ' for c in r)]
  parts.append('<table>'+''.join('<tr>'+''.join(('<th>' if i==0 else '<td>')+html.escape(c.strip())+('</th>' if i==0 else '</td>') for c in r.strip('|').split('|'))+'</tr>' for i,r in enumerate(rows))+'</table>');table.clear()
 for line in md.splitlines():
  if line.startswith('|'):table.append(line);continue
  flush()
  if line.startswith('# '):parts.append('<h1>'+html.escape(line[2:])+'</h1>')
  elif line.startswith('## '):parts.append('<h2>'+html.escape(line[3:])+'</h2>')
  elif line:parts.append('<p>'+html.escape(line.replace('**',''))+'</p>')
 flush()
 return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Dynamics Atlas reproduced results</title><style>body{max-width:1000px;margin:40px auto;padding:24px;font:16px/1.65 system-ui;color:#183247}table{border-collapse:collapse;width:100%;font-size:14px}th,td{border-bottom:1px solid #ccd7df;padding:10px;text-align:left}th{background:#edf3f7}h2{margin-top:32px}</style>'+''.join(parts)+'</html>'

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--data',type=Path,default=Path(__file__).resolve().parents[1]/'data');p.add_argument('--output',type=Path,default=Path('results'));a=p.parse_args()
 try:x=run(a.data)
 except (OSError,ValueError,AssertionError,KeyError)as e:print('Reproduction failed: '+str(e),file=sys.stderr);return 1
 a.output.mkdir(parents=True,exist_ok=True);(a.output/'results.json').write_text(json.dumps(x,indent=2)+'\n');md=report(x);(a.output/'REPORT.md').write_text(md)
 # A readable standalone result page requires no browser plugin or web service.
 (a.output/'REPORT.html').write_text(render_html(md))
 print('PASS: HSP90, DHFR and ADK table-to-report reproduction. Outputs: '+str(a.output));return 0
if __name__=='__main__':sys.exit(main())
