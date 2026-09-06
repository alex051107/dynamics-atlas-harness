from pathlib import Path
import csv,json
import numpy as np
from q05_shape_geometry_v1 import selected_backbone,frame_geometry,axis_angle_degrees
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs/q05_shape_preparation_v1';OUT.mkdir(exist_ok=False)
selected,excluded=selected_backbone(ROOT/'inputs/q05_author/molecular_dynamics_simulations/inputs_and_method/topology.pdb')
assert len(selected)==948 and len(excluded)==54
assert {v['chain'] for v in excluded}=={'A','B'}
assert all(55<=v['pdb_residue_number']<=63 for v in excluded)
assert all(not 55<=v['pdb_residue_number']<=63 for v in selected)
fields=['coordinate_index_zero_based','pdb_serial','chain','pdb_residue_number','residue_name','atom_name']
for name,rows in [('selected_atoms.csv',selected),('excluded_tail_atoms.csv',excluded)]:
    with (OUT/name).open('w') as f:
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(rows)
# Known six-point ellipsoid with unambiguous labelled correspondences.
x=np.array([[3.,0,0],[-3.,0,0],[0,2.,0],[0,-2.,0],[0,0,1.],[0,0,-1.]])
reference=x.copy();base=frame_geometry(x,reference)
np.testing.assert_allclose(base['sqrt_acylindricity_A'],np.sqrt(5/3),rtol=1e-12)
angle=.731;R=np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1.]])
rotated=frame_geometry(x@R+np.array([11.,3.,-7.]),reference)
np.testing.assert_allclose(rotated['eigenvalues_A2_ascending'],base['eigenvalues_A2_ascending'],atol=1e-12)
assert axis_angle_degrees(base['axis_unoriented'],rotated['axis_unoriented'])<1e-5
# Internal anisotropic deformation keeps the point labels; it is not a rigid rotation.
y=np.array([[2.,0,0],[-2.,0,0],[0,3.,0],[0,-3.,0],[0,0,1.],[0,0,-1.]])
internal=frame_geometry(y,reference)
assert abs(axis_angle_degrees(base['axis_unoriented'],internal['axis_unoriented'])-90)<1e-8
assert axis_angle_degrees(base['axis_unoriented'],(-np.array(base['axis_unoriented'])).tolist())==0
near_circle=x.copy();near_circle[:2,0]*=2/3*(1+1e-12)
near=frame_geometry(near_circle,reference);assert near['axis_unoriented'] is None
assert axis_angle_degrees(base['axis_unoriented'],near['axis_unoriented']) is None
# No alignment in this counterexample: averaging operations are intentionally distinct.
R90=np.array([[0,-1.,0],[1.,0,0],[0,0,1.]])
z=x@R90;fx=frame_geometry(x);fz=frame_geometry(z)
mean_tensor=(np.array(fx['gyration_tensor_A2'])+np.array(fz['gyration_tensor_A2']))/2
mu=np.linalg.eigvalsh(mean_tensor)
means={'mean_per_frame_sqrt_C':(fx['sqrt_acylindricity_A']+fz['sqrt_acylindricity_A'])/2,
       'sqrt_C_of_mean_tensor':float(np.sqrt(mu[-1]-mu[-2])),
       'sqrt_C_of_mean_coordinates':frame_geometry((x+z)/2)['sqrt_acylindricity_A']}
assert np.isclose(means['mean_per_frame_sqrt_C'],np.sqrt(5/3))
assert means['sqrt_C_of_mean_tensor']==0
assert np.isclose(means['sqrt_C_of_mean_coordinates'],np.sqrt(5/6))
result={'status':'PREPARATION_CHECK_PASS','actual_atom_selection':{'selected':948,'excluded':54,'uses_original_PDB_numbers':True},
        'synthetic_checks':['known_tensor_units','rigid_rotation_translation_invariance','internal_orthogonal_deformation','axis_sign_equivalence','near_circle_axis_abstention','noncommuting_averages'],
        'synthetic_mean_counterexample':means,'actual_trajectory_frames_read':0,'actual_shape_statistics_computed':False,
        'conditional_method':'Equal atom N/CA/C,exclude PDB55-63;fixed labelled reference Kabsch;Angstrom;no author-configuration claim',
        'axis_threshold_scope':'Numerical near-degeneracy guard only;coordinate/noise uncertainty and biological state thresholds not validated',
        'sources':{'gromacs_backbone':'https://manual.gromacs.org/documentation/current/reference-manual/analysis/using-groups.html','mdtraj_numbering':'https://www.mdtraj.org/1.8.0/atom_selection.html','paper':'OriginalPDF18,previouslyrendered;source-matchedMarkdown used for discovery'}}
(OUT/'validation.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'geometry_source.py').write_text((ROOT/'scripts/q05_shape_geometry_v1.py').read_text())
(OUT/'check_source.py').write_text(Path(__file__).read_text())
print(json.dumps(result,indent=2))
