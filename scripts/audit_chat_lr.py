"""Observe exact existing progress and actual checkpoints; missing work stays pending."""
import argparse
from collections import Counter
import json
import math
import random
from pathlib import Path
import torch
import numpy as np
from jmicro.model import JMicroModel
from chat_lr_contract import RUN, SUITES, B, SPEC, preflight, reference, require_ref, LIMITS, TOTAL
from jmicro.experiment import read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.chat_review import content_review
from phase6_performance import finite_state, alive
from review_chat_lr import get_items


def training(c):
    directory = RUN / 'S1'
    job = read_json(directory / 'job.json')
    assert not alive(job) and job['status'] == 'learning_complete'
    dry = read_json(require_ref(c['candidate_consumption']))
    metrics = [json.loads(line) for line in (directory / 'metrics.jsonl').read_text().splitlines()]
    assert len(metrics) == dry['updates'] == 3646
    previous_metrics = [json.loads(line) for line in require_ref(c['historical_learning_metrics']).read_text().splitlines()]
    assert len(previous_metrics) == len(metrics)
    total = 0
    for actual, expected in zip(metrics, dry['rows'], strict=True):
        assert actual['update'] == expected['update']
        assert actual['teachers_this_update'] == expected['teachers']
        assert actual['microbatches'] == expected['microbatches'] and actual['lr'] == expected['lr']
        assert math.isfinite(actual['loss']) and math.isfinite(actual['gradient_norm'])
        total += actual['teachers_this_update']
        assert actual['assistant_teacher_tokens'] == total
        previous = previous_metrics[actual['update'] - 1]
        assert all(actual[key] == previous[key] for key in
                   ('token_digest', 'valid_input_tokens', 'physical_input_tokens', 'EOT_teachers',
                    'assistant_teacher_tokens', 'microbatches', 'teachers_this_update'))
    assert total == dry['Assistant_teachers'] == 1899557 and total - B == 2
    points = read_json(directory / 'checkpoints.json')
    assert set(points) == {'t1', 't2', 't3'}
    checks = {}
    for i, name in enumerate(('t1', 't2', 't3'), 1):
        ref = points[name]
        state = torch.load(require_ref(ref), map_location='cpu', weights_only=False)
        assert finite_state(state) and state['implementation_sha256'] == c['implementation']
        assert state['lineage']['base_checkpoint'] == c['parent'] and state['lineage']['optimizer_policy'] == 'fresh'
        assert {key: state['spec'][key] for key in SPEC} == SPEC
        assert state['supervised_tokens'] == ref['Assistant_teachers'] and state['update'] == ref['update']
        assert state['sampler']['teacher_tokens'] == state['supervised_tokens']
        assert state['tokens'] == state['sampler']['input_tokens'] == metrics[state['update'] - 1]['valid_input_tokens']
        assert state['sampler']['physical_tokens'] == metrics[state['update'] - 1]['physical_input_tokens']
        assert state['token_digest'] == metrics[state['update'] - 1]['token_digest']
        assert state['spec']['teacher_chat']['data_binding'] == c['sampler_binding']
        threshold = (B * i + 2) // 3
        assert state['supervised_tokens'] >= threshold
        assert state['update'] == 1 or metrics[state['update'] - 2]['assistant_teacher_tokens'] < threshold
        model = JMicroModel(state['model_config'])
        model.load_state_dict(state['model'], strict=True)
        assert sum(p.numel() for p in model.parameters()) == 10001152
        assert state['update'] == state['branch_updates'] and state['branch_tokens'] == state['tokens']
        assert state['body_bytes'] == metrics[state['update'] - 1]['body_bytes_seen']
        assert state['shard_manifest_sha256'] == c['TRAIN_manifest']['sha256']
        assert state['spec']['teacher_chat']['trainer_sha256'] == c['source_sha256']['src/jmicro/teacher_chat_training.py']
        assert state['scheduler']['last_epoch'] == state['update']
        assert state['scheduler']['_last_lr'] == [metrics[state['update'] - 1]['lr']] * len(state['optimizer']['param_groups'])
        assert all(group['lr'] == metrics[state['update'] - 1]['lr'] for group in state['optimizer']['param_groups'])
        assert state['optimizer']['state'] and all(int(row['step'].item()) == state['update'] for row in state['optimizer']['state'].values())
        assert set(state['rng']) == {'python', 'numpy', 'torch', 'cuda'}
        random.Random().setstate(state['rng']['python'])
        np.random.RandomState().set_state(state['rng']['numpy'])
        torch.Generator(device='cpu').set_state(state['rng']['torch'])
        assert len(state['rng']['cuda']) == 1 and all(r.dtype == torch.uint8 and r.numel() > 0 for r in state['rng']['cuda'])
        assert all(key in state for key in ('model', 'optimizer', 'scheduler', 'rng', 'sampler'))
        checks[name] = dict(checkpoint=ref, full_state_finite=True, first_registered_threshold_update=True,
                            padded_input_metrics_digest_verified=True, parent_data_spec_verified=True)
        del state, model
    report = dict(passed=True, config_sha256=c['config_sha256'], checkpoints=checks,
        updates=len(metrics), Assistant_teachers=total, final_overshoot=2, all_steps_finite=True,
        exact_expected_teacher_microbatch_and_LR_order=True, native_parameters=10001152,
        all_update_input_label_digests_identical_to_control=True,
        metrics=reference(directory / 'metrics.jsonl'), observer=reference(Path(__file__)), completed_at=now())
    atomic_json(directory / 'training_audit.json', report)
    print('Actual3646 updates/1899557 teachers and all3 full checkpoints passed CPU audit')


def progress(c):
    reviews, nlls, pending = {}, {}, []
    for arm, points in (('parent', ('t0',)), ('S0', ('t1', 't2', 't3')), ('S1', ('t1', 't2', 't3'))):
        for point in points:
            for suite in SUITES:
                path = RUN / 'evaluation' / arm / point / suite / 'greedy/result.json'
                key = '-'.join((arm, point, suite))
                if not path.exists() or not path.with_name('notes.json').exists():
                    pending.append(key + ' complete raw and219 judgments')
                    continue
                evaluation, items = get_items(path)
                notes = read_json(path.with_name('notes.json'))
                report = content_review(evaluation, sha256(path), notes, items)
                assert len(items) == len(notes['judgments']) == 219
                reviews[key] = dict(raw=reference(path), notes=reference(path.with_name('notes.json')),
                                    summaries=report['summaries'], judgments=219)
            path = RUN / 'NLL' / arm / (point + '.json')
            if not path.exists():
                pending.append(arm + '-' + point + ' fixed NLL')
            else:
                nll = read_json(path)
                assert nll['status'] == 'complete' and nll['binding']['config_sha256'] == c['config_sha256']
                assert len(nll['targets']) == len({r['id'] for r in nll['targets']}) == 2634
                assert dict(Counter(row['dataset'] for row in nll['targets'])) == dict(
                    historical_TRAIN=112, TRAIN=112, semantic_DEV=80, new_DEV=80, RPC_DEV=2250)
                for dataset, summary in nll['summaries'].items():
                    rows = [r for r in nll['targets'] if r['dataset'] == dataset]
                    for name in ('body_NLL', 'EOT_NLL', 'body_teachers', 'EOT_teachers', 'body_bytes'):
                        assert math.isclose(summary[name], sum(r[name] for r in rows), rel_tol=1e-12, abs_tol=1e-8)
                    assert summary['EOT_teachers'] == summary['targets'] == len(rows)
                    assert math.isclose(summary['body_mean_NLL'], summary['body_NLL'] / summary['body_teachers'], rel_tol=1e-12)
                nlls[arm + '-' + point] = dict(source=reference(path), summaries=nll['summaries'])
    for filename in ('S1/training_audit.json', 'selection.json', 'conditional_branches.json', 'completion.json'):
        if not (RUN / filename).exists():
            pending.append(filename)
    ledger = read_json(RUN / 'GPU_ledger.json') if (RUN / 'GPU_ledger.json').exists() else dict(entries=[])
    total = sum(row['charged_seconds'] for row in ledger['entries'])
    assert total <= TOTAL
    for key, limit in LIMITS.items():
        assert sum(row['charged_seconds'] for row in ledger['entries'] if row['category'] == key) <= limit
    output = dict(observed_at=now(), config=reference(c['config_path']), reviewed_suites=len(reviews), required_suites=28,
        content_judgments=sum(r['judgments'] for r in reviews.values()), required_judgments=6132,
        fixed_NLL_points=len(nlls), required_NLL_points=7, reviews=reviews, fixed_NLL=nlls, pending=pending,
        GPU_charged_seconds=total, model_quality_complete=False, goal_complete=False, status='continue',
        original_Chat_TEST_preparation_exposure=reference(RUN / 'protected_split_incident.json'))
    atomic_json(RUN / 'progress_audit.json', output)
    print(json.dumps({key: output[key] for key in ('reviewed_suites', 'content_judgments', 'fixed_NLL_points', 'pending', 'goal_complete')}))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--training', action='store_true')
    args = p.parse_args()
    c, _, _ = preflight()
    training(c) if args.training else progress(c)
