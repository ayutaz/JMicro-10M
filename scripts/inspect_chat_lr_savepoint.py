"""Read concrete CPU checkpoint fields for a failed observer assertion."""
import argparse
import json
import torch
from chat_lr_contract import RUN, require_ref, reference
from jmicro.experiment import read_json, now
from jmicro.training import atomic_json

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--point', choices=('t1','t2','t3'), required=True)
    args = p.parse_args()
    ref = read_json(RUN / 'S1/checkpoints.json')[args.point]
    state = torch.load(require_ref(ref), map_location='cpu', weights_only=False)
    complete = (RUN / 'S1/metrics.jsonl').read_bytes().split(b'\n')[:-1]
    row = json.loads(complete[state['update'] - 1])
    output = dict(observed_at=now(), checkpoint=ref, update=state['update'], scheduler=state['scheduler'],
        optimizer_groups=[dict(lr=g['lr'], weight_decay=g['weight_decay']) for g in state['optimizer']['param_groups']],
        metric_lr=row['lr'], observer=reference(__file__), GPU_updates=0, quality_evidence=False)
    atomic_json(RUN / ('savepoint-inspection-' + args.point + '.json'), output)
    print(json.dumps(output))
