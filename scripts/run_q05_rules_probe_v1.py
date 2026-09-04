"""Q05-only factual intake probe into unchanged active Draft Rules.

This new local entry reuses the existing admission and projector. It does not
alter run-case's two-case registry, select Rules, or execute scientific actions.
The original rejected run-case baseline must remain separately recorded.
"""
from __future__ import annotations

import argparse
from collections import Counter
import datetime
import json
from pathlib import Path
import subprocess
import sys

from dynamics_atlas_harness.paper_blind_exposed_v1 import (
    build_agent_visible_packet,
    load_public_packet,
    project_admitted_proposal_to_rules_casegraph,
    validate_agent_proposal,
)
from dynamics_atlas_harness.real_case_vertical_slice_v1 import load_rules_v1_bundle
from dynamics_atlas_harness.rules_prototype_v1 import evaluate_active_rules

REPO = Path(__file__).resolve().parents[1]
CASE_ID = 'q05_nanodisc_saxs_noe_20260904'
PACKET = REPO / 'evidence/paper_blind_exposed_v1/public/q05_public_fact_packet_v1.json'
PROPOSAL = REPO / 'research/paper_result_reproduction_screen_v1/q05_fact_proposal_v1.json'


def admit_q05(original_facts: dict, proposal: dict) -> tuple[dict, dict, dict]:
    if original_facts.get('case_id') != CASE_ID or proposal.get('case_id') != CASE_ID:
        raise ValueError('Q05_ONLY_ENTRY')
    packet = load_public_packet(PACKET)
    prefix = 'Original answer-free fact packet: '
    preserved = [json.loads(fact[len(prefix):]) for source in packet['source_materials']
                 for fact in source['permitted_facts'] if fact.startswith(prefix)]
    if preserved != [original_facts]:
        raise ValueError('Q05_FACT_PACKET_DIFFERS_FROM_SOURCE_RECORD')
    admission = validate_agent_proposal(PACKET, proposal)
    graph = project_admitted_proposal_to_rules_casegraph(PACKET, admission)
    return packet, admission, graph


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fact-packet', type=Path, required=True)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    original = json.loads(args.fact_packet.read_text())
    proposal = json.loads(PROPOSAL.read_text())
    packet, admission, graph = admit_q05(original, proposal)
    args.output_dir.mkdir(parents=True, exist_ok=False)
    out = args.output_dir

    def save(name: str, value: object) -> None:
        (out / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

    save('original_facts.json', original)
    save('public_packet.json', packet)
    save('profiler_visible_input.json', build_agent_visible_packet(PACKET))
    save('recorded_proposal.json', proposal)
    save('admission.json', admission)
    save('projected_casegraph.json', graph)
    bundle = load_rules_v1_bundle(REPO / 'registries/rules_v1')
    save('rules_bundle_snapshot.json', bundle)
    results = evaluate_active_rules(case_graph=graph, **bundle)
    save('raw_rule_results.json', results)
    routes = Counter(item['claim_effect']['route'] for item in results)
    receipt = {
        'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'entry': 'NEW_Q05_FACT_PROBE_USING_EXISTING_ADMISSION_AND_ACTIVE_DRAFT_EVALUATOR',
        'source_head': subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', 'HEAD'], text=True).strip(),
        'local_adapter_uncommitted': True,
        'command': [sys.executable, str(Path(__file__).resolve()), *sys.argv[1:]],
        'cwd': str(Path.cwd()),
        'python': sys.version,
        'rules_loaded': True,
        'active_rule_instance_count': len(results),
        'statuses': dict(Counter(item['status'] for item in results)),
        'routes': dict(routes),
        'numeric_actions_executed': 0,
        'scientific_verdict': 'NOT_EMITTED',
        'original_run_case_registry_modified': False,
        'projection_boundary': 'The existing projection preserves declaration strings but has no dedicated numerical BME configuration, NOE propagation, or matrix payload slots. Full original facts are retained separately; no claim that text preservation means numerical evaluation.',
        'stop': 'Inspect actual routes before any obligation adapter. SOURCE_LOOKUP is not a numerical extra-calculation obligation.',
    }
    save('receipt.json', receipt)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
