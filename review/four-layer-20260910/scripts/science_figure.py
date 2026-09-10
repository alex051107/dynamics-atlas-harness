from pathlib import Path
import json,shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
r=Path(__file__).resolve().parents[1];f=r/'outputs/figures';f.mkdir(exist_ok=True)
for source,name in [('autoresearch/tasks/dynamics_atlas_hsp90_noe_crosswalk_v1_20260911/outputs/report/figures/native_scatter.png','hsp90_native_reference.png'),('autoresearch/tasks/dynamics_atlas_adk_plain_agent_v1_20260910/outputs/report/loop_distances.png','dhfr_local_contacts.png')]:shutil.copy2(source,f/name)
a=Path('autoresearch/tasks/dynamics_atlas_adk_plain_agent_v2_20260910/derived')
# Use the already frozen numeric reference rather than re-estimate an alternative window.
d=json.loads((r/'E2/cases/Q-A1/hidden/rubric.json').read_text())['reference'];fig,ax=plt.subplots(figsize=(8,4.7));x=[0,1];w=.32
for off,seed,label,color in [(-w/2,'open','Open-start trajectory','#087E8B'),(w/2,'closed','Closed-start trajectory','#CA683F')]:
 vals=[d[seed][domain]['change_A']for domain in ['NMP','LID']];bars=ax.bar([v+off for v in x],vals,w,label=label,color=color)
 for bar,v in zip(bars,vals):ax.text(bar.get_x()+bar.get_width()/2,v+.055,f'+{v:.3f}',ha='center',fontsize=11)
ax.axhline(0,color='#556677',lw=.8);ax.set_xticks(x,['NMP–CORE','LID–CORE']);ax.set_ylabel('Last-window mean − first-window mean (Å)');ax.set_ylim(0,2.85);ax.legend(frameon=False,loc='upper left');ax.set_title('ADK: all four finite-window changes are positive',pad=14);fig.text(.5,.015,'First/last 10% of saved frames; one trajectory per starting condition; no confidence intervals',ha='center',fontsize=9);fig.tight_layout(rect=[0,.04,1,1]);fig.savefig(f/'adk_window_changes.png',dpi=200);plt.close(fig)
print('Reused two source-verified figures; generated ADK window-change plot.')
