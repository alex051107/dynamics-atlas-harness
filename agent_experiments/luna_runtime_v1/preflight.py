"""Inspect an explicit task preflight; environment creation is controlled by the adopted plan."""
import argparse,json
from pathlib import Path
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--task-root',type=Path,required=True);a=p.parse_args()
    result=json.loads((a.task_root/'outputs/preflight_env.json').read_text())
    if not result.get('common_environment_passed'):raise SystemExit('Common environment not admitted')
    print(json.dumps(result,indent=2))
