"""One source-bound GROMACS contact-method check; not a Rules execution."""
import csv
import datetime
import json
import math
import statistics
import subprocess
from pathlib import Path

W=Path(__file__).resolve().parents[4]
T=Path(__file__).resolve().parents[1]
A=W/'autoresearch/tasks/dynamics_atlas_hsp90_acquisition_20260725'
O=T/'outputs/q01_contact_method_canary_v2'
RUN='R46A_ES01_2021_11_08_NaCl170mM_GMX_JeanZay'
HYDROGENS={'HB*':['HB1','HB2','HB3'],'HD1*':['HD11','HD12','HD13'],'HD2*':['HD21','HD22','HD23'],'HE*':['HE1','HE2','HE3'],'HG2*':['HG21','HG22','HG23']}

def save(name,value):
    (O/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def rows(p):
    return [[float(v) for v in line.split()] for line in p.read_text().splitlines() if line.strip() and line.lstrip()[0] not in '#@']

def main():
    O.mkdir(exist_ok=False)
    config=json.loads((A/'config/noe_contacts_v0.json').read_text())
    contacts=[dict(c,state=state) for state in ['open','closed'] for c in config[state+'_contacts'] if c['md_used']]
    assert len(contacts)==24 and sum(c['state']=='open' for c in contacts)==19
    gro=A/'data/contract/MD/R46A'/RUN/'processed.gro';xtc=A/'data/trajectories'/(RUN+'.xtc')
    lines=gro.read_text().splitlines();atoms={}
    for idx,line in enumerate(lines[2:2+int(lines[1])],1):
        key=(int(line[:5]),line[5:10].strip(),line[10:15].strip())
        if key in atoms: raise ValueError('DUPLICATE_ATOM_IDENTITY')
        atoms[key]=idx
    selections=[]
    for c in contacts:
        parts=[];c['atom_indices']={}
        for endpoint in ['i','j']:
            names=HYDROGENS[c['pseudoatom_'+endpoint]]
            if c['resname_'+endpoint]=='ILE' and c['pseudoatom_'+endpoint]=='HD1*': names=['HD1','HD2','HD3']
            ids=[atoms[c['residue_'+endpoint],c['resname_'+endpoint],name] for name in names]
            c['atom_indices'][endpoint]=ids
            parts.append('(cog of atomnr '+' '.join(map(str,ids))+')')
        selections.append('"'+c['id']+'" '+' plus '.join(parts)+';')
    save('contacts_and_mapping.json',contacts)
    sf=O/'selections.dat';sf.write_text('\n'.join(selections)+'\n')
    cmd=['/opt/homebrew/bin/gmx','distance','-f',str(xtc),'-s',str(gro),'-sf',str(sf),'-b','20000','-e','1020000','-normpbc','-pbc','-oall',str(O/'distances_nm.xvg'),'-xvg','none']
    save('command.json',{'command':cmd,'cwd':str(O),'source_coordinate_pipeline':'md_0-10_evert1ns_fitBB_protonly.xtc; compare author md_1-10 only after numerical check','units':'GROMACS distance nm, times ps','PBC':True,'additional_make_whole':False,'statistical_unit':'trajectory','numeric_comparison_tolerance_A':0.011})
    proc=subprocess.run(cmd,cwd=O,capture_output=True,text=True,timeout=60)
    (O/'gromacs_stdout.txt').write_text(proc.stdout);(O/'gromacs_stderr.txt').write_text(proc.stderr)
    if proc.returncode:
        save('receipt.json',{'status':'GROMACS_ENTRY_REJECTED','exit_code':proc.returncode,'rules_controlled':False});return proc.returncode
    distance=rows(O/'distances_nm.xvg');assert len(distance)==1001 and all(len(row)==25 for row in distance)
    assert all(abs(row[0]-(20000+i*1000))<1e-6 for i,row in enumerate(distance))
    output=[];uniform_errors={};changes={}
    for state,folder,bound in [('open','GS',10.0),('closed','ES',8.5)]:
        stored=rows(A/'data/contract/MD/ANALYSE/R46A/VIOLATION'/folder/'ES01/avg_up_violations_time.dat');assert len(stored)==1001
        ids=[i for i,c in enumerate(contacts) if c['state']==state]
        uniform=[];paper=[]
        for i,row in enumerate(distance):
            ds=[row[j+1]*10 for j in ids]
            u=statistics.fmean(max(0,d-bound) for d in ds)
            p=statistics.fmean(max(0,d-contacts[j]['dviol_angstrom']) for j,d in zip(ids,ds))
            assert int(stored[i][0])==i+1
            uniform.append(u);paper.append(p)
            output.append({'time_ns':row[0]/1000,'state_reference':state,'uniform_mean_violation_A':u,'SI_table_mean_violation_A':p,'deposited_pseudo_mean_violation_A':stored[i][2],'uniform_minus_deposited_A':u-stored[i][2]})
        uniform_errors[state]=max(abs(u-s[2]) for u,s in zip(uniform,stored))
        changes[state]={'mean_SI_minus_uniform_A':statistics.fmean(p-u for p,u in zip(paper,uniform)),'max_abs_SI_minus_uniform_A':max(abs(p-u) for p,u in zip(paper,uniform))}
    with (O/'per_frame_scores.tsv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(output[0]),delimiter='\t');writer.writeheader();writer.writerows(output)
    valid=all(e<=0.011 for e in uniform_errors.values())
    receipt={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'UNIFORM_SOURCE_PARITY_PASS' if valid else 'SOURCE_PARITY_METHOD_GAP','run':RUN,'frames':1001,'contact_count':24,'uniform_vs_source_max_abs_A':uniform_errors,'SI_vs_uniform_descriptive_changes':changes,'rules_controlled':False,'all40_admitted':False,'scientific_verdict':'NOT_EMITTED','new_gmx_invocations':1,'new_optimizations':0,'SI_thresholds':'Existing method-table transcription, not fitted output targets; exact source precision retained','next':'If parity fails preserve failure and locate method mismatch before dispatch; if passes extend only under explicit source-bound obligation and method checks.'}
    save('receipt.json',receipt);print(json.dumps(receipt,indent=2));return 0

if __name__=='__main__':raise SystemExit(main())
