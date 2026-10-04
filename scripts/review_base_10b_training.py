"""Review completed direct10B training on CPU without quality evaluation."""
import argparse
import json
from pathlib import Path

import torch

from review_base_5b import review
from run_base_10b import binding_for, sanity
from jmicro.experiment import ROOT, read_json, sha256, write_json
from phase6_performance import alive


def review_training(plan_path):
    plan = read_json(plan_path)
    sanity(plan)
    job = read_json(ROOT / plan['output'] / 'job.json')
    assert job['status'] == 'complete' and not alive(job), 'Training must have completed and exited'
    result = review(plan_path)
    assert result['total_training_input_tokens'] == 10_000_007_168
    assert result['scientific_additional_input_tokens'] == 5_249_990_656
    assert result['binding'] == binding_for(plan, plan_path)
    assert result['stages']['stable']['tokens'] == 9_500_000_256
    assert result['stages']['decay']['updates'] == 15_259
    preparation = read_json(ROOT / 'reports/phase6/base_10b_preparation_review.json')
    assert preparation['binding'] == result['binding']
    assert all(preparation['checks'].values())
    assert preparation['verification_input_tokens'] == result['verification_input_tokens']
    # Saved RNG and counters are necessary for an actual resumable artifact.
    for stage, record in result['stages'].items():
        state = torch.load(record['checkpoint'], map_location='cpu', weights_only=False)
        assert set(state['rng']) == {'python', 'numpy', 'torch', 'cuda'}
        assert len(state['rng']['cuda']) == 1
        assert state['rng']['torch'].dtype == torch.uint8
        assert all(r.dtype == torch.uint8 and r.numel() > 0 for r in state['rng']['cuda'])
        assert state['rng']['python'] and state['rng']['numpy']
        assert len(state['token_digest']) == 64
        assert state['tokens'] == record['tokens']
        result['checks'][stage + '_saved_RNG_and_digest_present'] = True
        del state
    result['checks']['total10B_including_decay'] = result['checks'].pop('total5B_including_decay')
    result['checks']['direct10B_parent_and_endpoints'] = True
    result['checks']['previous_preparation_bound_and_reused'] = True
    result['status'] = 'completed_requested_step2_direct10B_training_only'
    result['stop_boundary'] = 'Report/local commit and stop before step3 quality evaluation'
    result['next_action'] = 'Step3 common full-dev and fixed400 generation evaluation; not executed in step2'
    result['reviewer_source_sha256'] = {
        name: sha256(ROOT / name) for name in (
            'scripts/review_base_10b_training.py', 'scripts/review_base_5b.py')
    }
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT / 'configs/phase6/base_10b.json')
    parser.add_argument('--result', type=Path, default=ROOT / 'reports/phase6/base_10b_training_review.json')
    args = parser.parse_args()
    result = review_training(args.plan)
    write_json(args.result, result)
    print(json.dumps({'status': result['status'], 'tokens': result['total_training_input_tokens'],
                      'checks': result['checks']}))
