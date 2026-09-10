"""Invoke the existing selector without modifying its registry or source scope."""
import argparse
import subprocess
import sys

def main():
    p=argparse.ArgumentParser()
    for name in ('selector','input','output','receipt','run-id','method-scope'):
        p.add_argument('--'+name, required=True)
    a=p.parse_args()
    command=[sys.executable,a.selector,'--input',a.input,'--output',a.output,'--receipt',a.receipt,'--run-id',a.run_id,'--method-scope',a.method_scope]
    raise SystemExit(subprocess.run(command).returncode)

if __name__=='__main__':main()
