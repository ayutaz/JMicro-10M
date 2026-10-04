"""Evaluate one saved 5B checkpoint and reuse frozen 2B/low-LR references."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jsonschema import validate
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, generate_suite, gpu_lock, implementation_hashes, rng_state, seed_all, source_snapshot
from phase6_performance import alive, identity
from run_eos_short_pilot import rate

SOURCES = ('scripts/compare_base_5b.py', 'scripts/compare_base_5b.sh',
           'src/jmicro/readiness.py', 'src/jmicro/evaluation_memory.py',
           'scripts/run_eos_short_pilot.py', 'scripts/phase6_performance.py')


def freeze(path):
    training = read_json(ROOT / 'reports/phase6/base_5b_review.json')
    previous = read_json(ROOT / 'configs/phase6/eos_low_lr_100m.json')
    assert all(training['checks'].values())
    references = {
        'base2B_body': 'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/full-dev.json',
        'base2B_generation': 'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/generation.json',
        'lowLR_web': 'reports/phase6/eos-low-lr-100m-20261004/web-full-evaluation.json',
        'short20_reference_only': 'reports/phase6/eos-low-lr-100m-20261004/short20-full-evaluation.json',
    }
    plan = {
        'version': 1, 'scope': 'User requested step3 comparison only; no training, test selection,10B/Chat',
        'output': 'reports/phase6/base-5b-comparison-20261004',
        'checkpoint': training['stages']['decay']['checkpoint'],
        'checkpoint_sha256': training['stages']['decay']['sha256'],
        'checkpoint_tokens': training['total_training_input_tokens'],
        'dev_shards': previous['dev_shards'],
        'dev_manifest_sha256': sha256(Path(previous['dev_shards']) / 'manifest.json'),
        'tokenizer': previous['tokenizer'], 'tokenizer_sha256': previous['tokenizer_sha256'],
        'suite_sha256': previous['suite_sha256'], 'split': 'dev',
        'documents': 89416, 'body_bytes': 164344743, 'body_tokens': 42003934,
        'dtype': 'bf16', 'backend': 'math', 'context': 1024, 'stride': 512, 'evaluation_batch': 16,
        'generation_cases': 80, 'generation_outputs': 400, 'max_new_tokens': 64,
        'sampling_seeds': [42,43,44], 'temperature': .8, 'top_p': .9,
        'memory_fraction': .94, 'GPU_budget_seconds': 1800,
        'references': {k: {'path': str(ROOT / p), 'sha256': sha256(ROOT / p)} for k,p in references.items()},
        'implementation': implementation_hashes(),
        'source_sha256': {p: sha256(ROOT / p) for p in SOURCES},
        'growth_rules': {'maximum_BPB_regression': .001, 'fixed_repetition_increase_must_be_less_than': 8,
                         'no_new_empty_role_unicode': True},
        'quality_criteria_unchanged': True, 'created_at': now(),
    }
    assert sha256(Path(plan['checkpoint'])) == plan['checkpoint_sha256']
    if path.exists():
        old = read_json(path)
        assert {k:v for k,v in old.items() if k != 'created_at'} == {k:v for k,v in plan.items() if k != 'created_at'}
        return old
    write_json(path, plan)
    write_json(ROOT / 'schemas' / path.relative_to(ROOT).with_suffix('.schema.json'), {
        '$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
        'additionalProperties': False, 'required': list(plan),
        'properties': {k: {'const': v} for k,v in plan.items()}})
    return plan


def summarize(label, tokens, body, generation):
    assert body['documents'] == 89416 and body['body_bytes'] == 164344743 and body['body_tokens'] == 42003934
    assert (body['context'], body['stride'], body['batch']) == (1024, 512, 16)
    assert all(r['scored_body_tokens'] == r['body_tokens'] for r in body['rows'])
    rows = generation['outputs']
    assert len(rows) == 400 and generation['max_new_tokens'] == 64
    groups = {}
    for row in rows:
        assert row['split'] == 'dev'
        key = f"{row['decoding']}-suppressed{int(row['suppressed'])}-seed{row['seed']}"
        groups.setdefault(key, []).append(row)
    assert len(groups) == 5 and all(len(g) == 80 for g in groups.values())
    fixed = groups['greedy-suppressed1-seed42']
    return {'label': label, 'training_input_tokens': tokens, 'full_dev_BPB': body['bpb'],
            'fixed80': rate(fixed), 'all400': rate(rows),
            'generation_groups': {k: rate(v) for k,v in groups.items()}}


def comparison(plan, run):
    refs = {k: read_json(Path(v['path'])) for k,v in plan['references'].items()}
    body = read_json(run / 'full-dev.json')['body']
    generation = read_json(run / 'generation.json')['generation']
    conditions = {
        'base2B': (2000027648, refs['base2B_body']['body'], refs['base2B_generation']['generation']),
        'lowLR_web': (2100035584, refs['lowLR_web']['body'], refs['lowLR_web']['generation']),
        'base5B': (plan['checkpoint_tokens'], body, generation),
        'short20_reference_only': (2100035584, refs['short20_reference_only']['body'], refs['short20_reference_only']['generation']),
    }
    keys = lambda rows: [(r['doc_id'], r['body_bytes'], r['body_tokens'], r['scored_body_tokens']) for r in rows]
    generated_keys = lambda rows: [(r['id'], r['prefix'], r['category'], r['decoding'], r['suppressed'], r['seed']) for r in rows]
    for _, old_body, old_generation in conditions.values():
        assert keys(body['rows']) == keys(old_body['rows'])
        assert generated_keys(generation['outputs']) == generated_keys(old_generation['outputs'])
        assert old_generation['suite_sha256'] == plan['suite_sha256']
        assert old_generation['sampling_evaluated'] and old_generation['temperature'] == .8 and old_generation['top_p'] == .9
    table = {k: summarize(k, *v) for k,v in conditions.items()}
    changes, gates = {}, {}
    current = table['base5B']
    for reference in ('base2B', 'lowLR_web'):
        old = table[reference]
        changes[reference] = {'BPB_difference': current['full_dev_BPB'] - old['full_dev_BPB'],
            'BPB_relative_change_percent': 100 * (current['full_dev_BPB'] / old['full_dev_BPB'] - 1),
            'fixed_EOS_difference': current['fixed80']['eos'] - old['fixed80']['eos'],
            'fixed_repetition_difference': current['fixed80']['repetition'] - old['fixed80']['repetition']}
        gates[reference] = {
            'full_BPB_no_major_regression': current['full_dev_BPB'] <= old['full_dev_BPB'] + .001,
            'fixed_repetition_not8_worse': current['fixed80']['repetition'] < old['fixed80']['repetition'] + 8,
            'no_new_empty_role_unicode_all400': all(current['all400'][k] <= old['all400'][k] for k in ('empty','role_leak','unicode_failure')),
        }
    fixed = lambda gen: {r['id']: r for r in gen['outputs'] if r['decoding'] == 'greedy' and r['suppressed']}
    aligned = {k: fixed(v[2]) for k,v in conditions.items() if k != 'short20_reference_only'}
    examples = [{'id': case, 'prefix': aligned['base5B'][case]['prefix'],
                 'outputs': {k: {'text': rows[case]['text'], 'stop_reason': rows[case]['stop_reason'],
                                  'repetition': rows[case]['repetition']} for k,rows in aligned.items()}}
                for case in aligned['base5B']]
    write_json(run / 'aligned-content.json', {'scope': 'All80 same fixed greedy prompts; qualitative review, not blinded human scoring', 'cases': examples})
    return {'status': 'completed_same_protocol_5B_comparison_pending_content_review',
            'conditions': table, 'differences': changes, 'growth_checks': gates,
            'growth_gate_passed_against_both': all(v for g in gates.values() for v in g.values()),
            'BPB_improves_against_both': all(changes[k]['BPB_difference'] < 0 for k in changes),
            'short20_scope': 'Reference only; different mixture, not a pure training-volume comparison',
            'same_full_dev_and400_generation_keys': True, 'quality_targets_achieved': False,
            'test_split_used': False, 'additional_training_tokens': 0, 'completed_at': now()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT / 'configs/phase6/base_5b_comparison.json')
    parser.add_argument('--freeze', action='store_true')
    args = parser.parse_args()
    torch.set_num_threads(2)
    if args.freeze:
        freeze(args.plan)
        print('5B comparison plan frozen; no evaluation started', flush=True)
        return
    plan = read_json(args.plan)
    validate(plan, read_json(ROOT / 'schemas' / args.plan.relative_to(ROOT).with_suffix('.schema.json')))
    assert implementation_hashes() == plan['implementation']
    assert plan['source_sha256'] == {p: sha256(ROOT / p) for p in SOURCES}
    assert sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256']
    assert sha256(ROOT / 'eval/base.jsonl') == plan['suite_sha256']
    assert sha256(Path(plan['dev_shards']) / 'manifest.json') == plan['dev_manifest_sha256']
    for ref in plan['references'].values():
        assert sha256(Path(ref['path'])) == ref['sha256']
    checkpoint = Path(plan['checkpoint'])
    assert sha256(checkpoint) == plan['checkpoint_sha256']
    run = ROOT / plan['output']
    run.mkdir(parents=True, exist_ok=True)
    path = run / 'job.json'
    old = read_json(path) if path.exists() else {}
    binding = {'plan_sha256': sha256(args.plan), 'checkpoint_sha256': plan['checkpoint_sha256'],
               'implementation': plan['implementation'], 'source_sha256': plan['source_sha256']}
    if old:
        assert not alive(old), 'Identified job live; do not duplicate'
        assert old['binding'] == binding
        if old['status'] == 'complete':
            print('Comparison already complete; no GPU rerun', flush=True)
            return
    else:
        write_json(run / 'source_sha256.json', source_snapshot(run / 'snapshot'))
    prior, started, stopped = old.get('gpu_elapsed_seconds', 0), [None], [False]
    job = {'status': 'running', **identity(), 'binding': binding, 'started_at': now(),
           'command': sys.argv, 'gpu_elapsed_seconds': prior, 'restart_command': 'bash scripts/compare_base_5b.sh'}
    atomic_json(path, job)
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]:
            raise InterruptedError('Evaluation interruption requested; completed stage retained')
        if started[0] is not None and prior + time.monotonic() - started[0] > plan['GPU_budget_seconds']:
            raise TimeoutError('Frozen cumulative GPU budget exhausted')
    def heartbeat(stage, **fields):
        check()
        job.update(stage=stage, heartbeat_at=now(), **fields)
        job['gpu_elapsed_seconds'] = prior + (time.monotonic() - started[0] if started[0] is not None else 0)
        atomic_json(path, job)
    try:
        seed_all(42)
        torch.use_deterministic_algorithms(True)
        torch.cuda.set_per_process_memory_fraction(plan['memory_fraction'])
        with gpu_lock('cuda'), sdpa_kernel([SDPBackend.MATH]):
            started[0] = time.monotonic()
            state = torch.load(checkpoint, map_location='cpu', weights_only=False)
            model = JMicroModel(state['model_config']).to('cuda')
            model.load_state_dict(state['model'], strict=True)
            before_rng, before_mode = rng_state(), model.training
            before_weights = {k: v.clone() for k,v in model.state_dict().items()}
            memory = bound_evaluation_cache(model)
            def monitor(_module, _args):
                check()
                if memory['forward_calls'] % 128 == 0:
                    heartbeat(job.get('stage', 'evaluation'), forward_calls=memory['forward_calls'])
            model.register_forward_pre_hook(monitor)
            body_path, generation_path = run / 'full-dev.json', run / 'generation.json'
            if not body_path.exists():
                heartbeat('full-dev')
                dev = Shard(Path(plan['dev_shards']), 'dev')
                def progress(done, total):
                    check()
                    if done % 1024 == 0 or done == total:
                        heartbeat('full-dev', completed_tasks=done, total_tasks=total)
                body = evaluate_batched(model, dev, 'cuda', plan['dtype'], limit=None,
                                        context=plan['context'], batch=plan['evaluation_batch'], progress=progress)
                assert body['documents'] == plan['documents'] and body['body_bytes'] == plan['body_bytes']
                write_json(body_path, {'binding': binding, 'checkpoint_sha256': plan['checkpoint_sha256'], 'body': body,
                                      'memory': dict(memory), 'completed_at': now()})
                print(json.dumps({'stage': 'full-dev-complete', 'BPB': body['bpb'], 'seconds': body['seconds']}), flush=True)
                del dev, body
                gc.collect()
                torch.cuda.empty_cache()
            else:
                assert read_json(body_path)['binding'] == binding
            if not generation_path.exists():
                heartbeat('generation')
                tok = Tokenizer(ROOT / plan['tokenizer'])
                gen_started = time.monotonic()
                generation = generate_suite(model, tok, 'cuda', plan['dtype'], limit=80, max_new=64, sampling=True)
                assert len(generation['outputs']) == plan['generation_outputs']
                write_json(generation_path, {'binding': binding, 'checkpoint_sha256': plan['checkpoint_sha256'],
                                             'generation': generation, 'seconds': time.monotonic() - gen_started,
                                             'memory': dict(memory), 'completed_at': now()})
            else:
                assert read_json(generation_path)['binding'] == binding
            isolated = equal_state(before_rng, rng_state()) and before_mode == model.training and equal_state(before_weights, model.state_dict())
            assert isolated and sha256(checkpoint) == plan['checkpoint_sha256']
            heartbeat('comparison')
            result = comparison(plan, run)
            result.update(binding=binding, evaluation_state_isolated=isolated, checkpoint_unchanged=True,
                          memory=memory, references_reused_without_GPU=True,
                          stop_boundary='Report/commit and stop before10B/Chat/mixture/decoder sweeps')
            write_json(run / 'result.json', result)
            job.update(status='complete', completed_at=now(), result=str(run / 'result.json'))
            print(json.dumps({'status': 'complete', 'conditions': result['conditions']}), flush=True)
    except BaseException as exc:
        job.update(status='interrupted' if isinstance(exc, (InterruptedError, TimeoutError)) else 'failed',
                   failure=f'{type(exc).__name__}: {exc}', finished_at=now())
        raise
    finally:
        if started[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - started[0]
        atomic_json(path, job)


if __name__ == '__main__':
    main()
