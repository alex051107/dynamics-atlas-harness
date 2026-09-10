from pathlib import Path
import json,subprocess
r=Path(__file__).resolve().parents[1];d=json.loads((r/'outputs/HALF_BOX_GATE_DIAGNOSIS.json').read_text());report=[]
for state,x in d.items():
 q=x['worst_minimum_image_pair'];out=r/f'outputs/gmx_distance_{state}.xvg';cmd=['gmx','distance','-s',str(r/f'inputs/ORADD_{state}_state.gro'),'-f',str(r/f'inputs/ORADD_{state}_state_traj.xtc'),'-b',str(q['time_ps']),'-e',str(q['time_ps']),'-select',f'atomnr {q["gromacs_atom1"]} {q["gromacs_atom2"]}','-oall',str(out),'-oxyz',str(r/f'outputs/gmx_components_{state}.xvg')]
 if not out.exists():
  p=subprocess.run(cmd,capture_output=True,text=True);(r/f'outputs/gmx_distance_{state}.log').write_text(p.stdout+p.stderr);assert p.returncode==0,p.stderr[-1500:]
 rows=[list(map(float,l.split()))for l in out.read_text().splitlines()if l and l[0]not in '#@'];assert len(rows)==1;v=rows[0][1]*10;err=abs(v-q['distance_A']);assert round(q['distance_A']/10,3)==rows[0][1],(state,v,err)
 report.append({'state':state,'time_ps':q['time_ps'],'residues':[q['residue1'],q['residue2']],'local_minimum_image_A':q['distance_A'],'gromacs_minimum_image_A':v,'error_A':err,'half_box_A':q['half_min_box_A'],'command':cmd,'status':'PASS_AT_GROMACS_TEXT_PRECISION'})
(r/'outputs/GROMACS_GATE_CROSSCHECK.json').write_text(json.dumps({'status':'PASS','software':'GROMACS2025.1-Homebrew','comparison':'exact agreement after rounding local nm value to GROMACS output3decimal nm precision; initial1e-4A test was too strict for text formatting, no scientific data changed','comparisons':report},indent=2));print(json.dumps(report,indent=2))
