"""Poll actual PID/boot/start identities; status files alone are not liveness."""
from pathlib import Path
import json
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, now
from jmicro.training import atomic_json
from chat_semantic_contract import RUN, reference
from phase6_performance import alive, identity


def main():
    ledger = read_json(RUN / 'GPU_ledger.json')
    stages = []
    for row in ledger['entries']:
        stages.append(dict(category=row['category'], name=row['name'], status=row['status'],
                           currently_alive=alive(row), pid=row['pid'], boot_id=row['boot_id'],
                           start_ticks=row['start_ticks'], charged_seconds=row['charged_seconds'],
                           update=row.get('update'), Assistant_teachers=row.get('Assistant_teachers'),
                           stage=row.get('stage'), completed=row.get('completed')))
    output = dict(observed_at=now(), observer=identity(), ledger=reference(RUN / 'GPU_ledger.json'),
                  stages=stages, overall_goal_complete=False)
    atomic_json(RUN / 'job_observations' / ('observation-' + now().replace(':', '') + '.json'), output)
    print(json.dumps(output, ensure_ascii=False))


if __name__ == '__main__':
    main()
