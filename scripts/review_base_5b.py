"""Review saved 5B training evidence without training, generation or corpus scans."""
import argparse
import gc
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.training import implementation_hashes, learning_rate_factor
from phase6_performance import alive, finite_state


def review(plan_path):
    torch.set_num_threads(2)
    plan = read_json(plan_path)
    run = ROOT / plan['output']
    job, result = read_json(run / 'job.json'), read_json(run / 'result.json')
    assert job['status'] == 'complete' and not alive(job), 'Training must have completed and exited'
    assert result['status'] == 'complete_training_only'
    assert result['binding'] == job['binding']
    assert result['binding']['plan_sha256'] == sha256(plan_path)
    assert implementation_hashes() == plan['implementation']
    assert all(sha256(ROOT / name) == digest for name, digest in plan['source_sha256'].items())
    parent_path = Path(plan['parent']['path'])
    assert sha256(parent_path) == plan['parent']['sha256']
    assert sha256(Path(plan['shards']) / 'manifest.json') == plan['shard_manifest_sha256']
    assert sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256']
    gate = read_json(run / 'cuda-resume-gate.json')
    assert gate['passed'] and all(gate['checks'].values())
    assert gate['input_tokens'] == result['verification_input_tokens'] == plan['verification_input_tokens']
    assert gate['binding'] == result['binding']
    assert sha256(Path(plan['tests']['path'])) == plan['tests']['sha256']
    checks = {'terminal_job_exited': True, 'frozen_binding_unchanged': True,
              'immutable_parent_hash': True, 'accepted_train_manifest': True,
              'exact_CUDA_resume': True, 'tests_report_bound': True}
    reports = {}
    parent = torch.load(parent_path, map_location='cpu', weights_only=False)
    before = parent
    for stage in ('stable', 'decay'):
        stage_result = read_json(run / stage / 'result.json')
        assert stage_result == result['stages'][stage]
        latest = read_json(run / stage / 'latest.json')
        path = Path(stage_result['checkpoint'])
        assert latest['path'] == str(path) and latest['sha256'] == stage_result['checkpoint_sha256'] == sha256(path)
        state = torch.load(path, map_location='cpu', weights_only=False)
        assert state['model_config'] == plan['model_config']
        assert state['model'].keys() == parent['model'].keys()
        assert all(state['model'][k].shape == parent['model'][k].shape for k in state['model'])
        assert state['implementation_sha256'] == plan['implementation']
        assert state['shard_manifest_sha256'] == plan['shard_manifest_sha256']
        assert finite_state(state)
        expected_spec = dict(plan['spec'])
        end = plan['stable_end_update'] if stage == 'stable' else plan['end_update']
        if stage == 'decay':
            expected_spec.update(scheduler='wsd_decay', schedule_updates=end,
                                 branch_at=plan['stable_end_update'], decay_updates=plan['decay_updates'],
                                 minimum_lr_ratio=plan['minimum_lr_ratio'])
        assert state['spec'] == expected_spec
        assert state['update'] == end and state['tokens'] == end * 32768
        assert latest['update'] == end and latest['tokens_seen'] == state['tokens']
        lineage = state['lineage']
        assert lineage['parent_update'] == before['update'] and lineage['parent_tokens'] == before['tokens']
        assert lineage['parent_token_digest'] == before['token_digest']
        assert lineage['parent_spec'] == before['spec']
        assert lineage['parent_sha256'] == (plan['parent']['sha256'] if stage == 'stable' else reports['stable']['sha256'])
        assert len(state['optimizer']['param_groups']) == len(before['optimizer']['param_groups']) == 2
        assert state['optimizer']['state'].keys() == before['optimizer']['state'].keys()
        assert all(int(v['step']) == end for v in state['optimizer']['state'].values())
        assert state['scheduler']['last_epoch'] == end
        assert state['scheduler']['_step_count'] == before['scheduler']['_step_count'] + end - before['update']
        assert state['scheduler']['base_lrs'] == before['scheduler']['base_lrs']
        expected_next = plan['spec']['lr'] * learning_rate_factor(expected_spec, end)
        assert all(math.isclose(g['lr'], expected_next, rel_tol=0, abs_tol=1e-14) for g in state['optimizer']['param_groups'])
        rows = [json.loads(line) for line in (run / stage / 'metrics.jsonl').read_text().splitlines()]
        assert [r['update'] for r in rows] == list(range(before['update'] + 1, end + 1))
        assert all(r['tokens_seen'] == r['update'] * 32768 for r in rows)
        assert all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in rows)
        assert all(math.isclose(r['lr'], plan['spec']['lr'] * learning_rate_factor(expected_spec, r['update'] - 1),
                                rel_tol=0, abs_tol=1e-14) for r in rows)
        assert state['token_digest'] == rows[-1]['token_digest']
        assert state['supervised_tokens'] == rows[-1]['supervised_tokens']
        assert state['body_bytes'] == rows[-1]['body_bytes_seen']
        assert 0 < state['supervised_tokens'] - before['supervised_tokens'] <= state['tokens'] - before['tokens']
        assert state['body_bytes'] > before['body_bytes']
        assert all(state['sampler'][k] == before['sampler'][k] for k in ('seed', 'context', 'blocks'))
        assert state['sampler']['epoch'] == before['sampler']['epoch'] == 0
        assert state['sampler']['position'] == before['sampler']['position'] + len(rows) * plan['spec']['batch']
        checkpoints = list((run / stage).glob('checkpoint-*.pt'))
        expected_saves = {u for u in range(before['update'] + 1, end + 1) if u % plan['save_every'] == 0} | {end}
        assert expected_saves <= {int(p.stem.split('-')[1]) for p in checkpoints}
        checks[stage + '_checkpoint_state_and_contiguous_metrics'] = True
        reports[stage] = {'checkpoint': str(path), 'sha256': sha256(path), 'update': end,
                          'tokens': state['tokens'], 'additional_tokens': state['tokens'] - before['tokens'],
                          'updates': len(rows), 'first_loss': rows[0]['loss'], 'last_loss': rows[-1]['loss'],
                          'training_step_seconds': sum(r['seconds'] for r in rows),
                          'steady_tokens_per_second': stage_result['steady_tokens_per_second'],
                          'retained_checkpoint_count': len(checkpoints), 'next_lr': expected_next}
        if before is not parent:
            del before
        before = state
        del rows
        gc.collect()
    assert before['tokens'] == result['tokens'] == plan['end_tokens']
    assert sum(s['additional_tokens'] for s in reports.values()) == result['scientific_additional_input_tokens'] == plan['additional_training_tokens']
    assert not result['evaluation_started'] and not result['test_split_used'] and not result['quality_targets_achieved']
    assert job['gpu_elapsed_seconds'] <= plan['gpu_budget_seconds']
    checks.update(total5B_including_decay=True, scientific_and_verification_separate=True,
                  original_training_settings_and_train_only_cursor=True, GPU_budget_respected=True,
                  no_evaluation_or_quality_claim=True, periodic_checkpoints_retained=True)
    total_bytes = sum(p.stat().st_size for p in run.rglob('*') if p.is_file())
    assert total_bytes <= plan['maximum_output_bytes']
    checks['output_within_frozen_capacity'] = True
    return {'status': 'completed_requested_steps1_2_training_only', 'checks': checks,
            'plan_sha256': sha256(plan_path), 'binding': result['binding'], 'stages': reports,
            'total_training_input_tokens': result['tokens'],
            'scientific_additional_input_tokens': result['scientific_additional_input_tokens'],
            'verification_input_tokens': gate['input_tokens'], 'tests': plan['tests'],
            'gpu_elapsed_seconds': job['gpu_elapsed_seconds'], 'output_bytes': total_bytes,
            'actual_training_process_exited': True, 'quality_targets_achieved': False,
            'evaluation_started': False, 'next_action': 'Protected full dev and fixed generation comparison; not executed in steps1,2',
            'stop_boundary': 'Report/commit and stop before evaluation,10B/Chat/sweeps', 'completed_at': now()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT / 'configs/phase6/base_5b.json')
    parser.add_argument('--result', type=Path, default=ROOT / 'reports/phase6/base_5b_review.json')
    args = parser.parse_args()
    result = review(args.plan)
    write_json(args.result, result)
    print(json.dumps({'status': result['status'], 'tokens': result['total_training_input_tokens'], 'checks': result['checks']}))
