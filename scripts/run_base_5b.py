"""Freeze and execute only steps 1/2: explicit stable extension and total-5B training."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import statistics
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jsonschema import validate
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.phase5 import equal_state
from jmicro.stable_extension import StableExtensionTrainer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, source_snapshot
from phase6_performance import alive, identity, finite_state

SOURCES = ('src/jmicro/stable_extension.py', 'src/jmicro/eos_pilot.py',
           'scripts/run_base_5b.py', 'scripts/run_base_5b.sh', 'scripts/phase6_performance.py')


def test_counts(path):
    counts = {k: 0 for k in ('tests', 'failures', 'errors', 'skipped')}
    for suite in ET.parse(path).getroot().iter('testsuite'):
        for key in counts:
            counts[key] += int(suite.get(key, 0))
    assert counts['tests'] >= 6 and not any(counts[k] for k in ('failures', 'errors', 'skipped'))
    return counts


def freeze(path):
    previous = read_json(ROOT / 'configs/phase6/base_2b_10b_data.json')
    review_path = ROOT / 'reports/phase6/eos_low_lr_100m_review.json'
    review = read_json(review_path)
    assert review['base5B_eligible']
    parent_path = ROOT / 'reports/phase6/base-2b-10bdata-20261004/stable/checkpoint-00057984.pt'
    latest = read_json(parent_path.parent / 'latest.json')
    assert latest['update'] == 57984 and latest['sha256'] == sha256(parent_path)
    state = torch.load(parent_path, map_location='cpu', weights_only=False)
    assert state['update'] == 57984 and state['tokens'] == 1900019712
    assert state['implementation_sha256'] == implementation_hashes()
    assert state['spec']['scheduler'] == 'wsd' and state['spec']['lr'] == .002
    assert all(g['lr'] == .002 for g in state['optimizer']['param_groups'])
    tests = ROOT / 'reports/phase6/base_5b_tests.xml'
    spec = dict(state['spec'], schedule_updates=144959)
    plan = {
        'version': 1, 'scope': 'User-requested steps1,2: total5B training only; evaluation/Chat/10B deferred',
        'output': 'reports/phase6/base-5b-20261004',
        'parent': {'path': str(parent_path), 'sha256': latest['sha256'], 'update': state['update'],
                   'tokens': state['tokens'], 'spec': state['spec'], 'token_digest': state['token_digest']},
        'model_config': state['model_config'], 'parameters': 10001152,
        'spec': spec, 'shards': previous['shards'],
        'shard_manifest_sha256': previous['shard_manifest_sha256'],
        'tokenizer': previous['tokenizer'], 'tokenizer_sha256': previous['tokenizer_sha256'],
        'unique_train_tokens': previous['unique_train_stream_tokens'], 'data_mixture': {'web': 1.0},
        'stable_end_update': 144959, 'stable_end_tokens': 4750016512,
        'decay_updates': 7629, 'end_update': 152588, 'end_tokens': 5000003584,
        'additional_training_tokens': 3099983872, 'verification_input_tokens': 524288,
        'minimum_lr_ratio': .1, 'decay_fraction_actual': 7629 / 152588,
        'decay_rounding': 'Nearest completed update to5percent, per saved5B proposal',
        'save_every': 1000, 'log_every': 50,
        'memory_fraction': .94, 'gpu_budget_seconds': 7200,
        'minimum_free_bytes': 200 * 1024**3, 'maximum_output_bytes': 20 * 1024**3,
        'checkpoint_retention': 'Keep all completed checkpoints and all earlier runs',
        'estimated_training_seconds': 3099983872 / 690619,
        'learning_rate_decision': 'Retain stable-parent actualLR0.002 with no jump; final5percent cosine to0.0002. LowLR100M after completed decay is a different experiment, not a long-run optimum.',
        'implementation': implementation_hashes(),
        'source_sha256': {p: sha256(ROOT / p) for p in SOURCES},
        'go_evidence': {'path': str(review_path), 'sha256': sha256(review_path)},
        'tests': {'path': str(tests), 'sha256': sha256(tests), 'counts': test_counts(tests)},
        'quality_targets_achieved': False, 'evaluation_started': False, 'created_at': now(),
    }
    assert plan['end_tokens'] == plan['end_update'] * 32768
    assert plan['stable_end_tokens'] == plan['stable_end_update'] * 32768
    assert plan['additional_training_tokens'] == plan['end_tokens'] - plan['parent']['tokens']
    assert math.ceil(5e9 / 32768) == plan['end_update']
    assert round(.05 * plan['end_update']) == plan['decay_updates']
    if path.exists():
        old = read_json(path)
        assert {k:v for k,v in old.items() if k != 'created_at'} == {k:v for k,v in plan.items() if k != 'created_at'}
        return old
    write_json(path, plan)
    schema = ROOT / 'schemas' / path.relative_to(ROOT).with_suffix('.schema.json')
    write_json(schema, {'$schema': 'https://json-schema.org/draft/2020-12/schema', 'type': 'object',
                       'additionalProperties': False, 'required': list(plan),
                       'properties': {k: {'const': v} for k,v in plan.items()}})
    return plan


def collect():
    gc.collect()
    torch.cuda.empty_cache()


def cuda_gate(plan, web, output, binding, check):
    result_path = output / 'cuda-resume-gate.json'
    if result_path.exists():
        result = read_json(result_path)
        assert result['passed'] and result['binding'] == binding
        for path, digest in result['checkpoint_sha256'].items():
            assert sha256(Path(path)) == digest
        return result
    gate = output / 'verification'
    checks, histories, checkpoints = {}, {}, []
    for mode in ('stable-extension', 'decay'):
        spec = dict(plan['spec'])
        source = Path(plan['parent']['path'])
        if mode == 'decay':
            # Four-update decay tests the unchanged branch path and its floor;
            # production uses the separately frozen 7,629-update tail.
            source = gate / 'extension-parent/checkpoint.pt'
            seed = StableExtensionTrainer(plan['model_config'], web, spec, 'cuda')
            seed.load_extension(Path(plan['parent']['path']), plan['parent']['sha256'])
            seed.save(source)
            del seed
            collect()
            spec.update(scheduler='wsd_decay', branch_at=plan['parent']['update'],
                        decay_updates=4, schedule_updates=plan['parent']['update'] + 4,
                        minimum_lr_ratio=plan['minimum_lr_ratio'])
        def trainer():
            current = StableExtensionTrainer(plan['model_config'], web, spec, 'cuda')
            if mode == 'stable-extension':
                current.load_extension(source, plan['parent']['sha256'])
            else:
                current.load(source, decay_branch=True)
            return current
        current = trainer()
        history = []
        for _ in range(4):
            check()
            history.append(current.step())
        expected = gate / mode / 'continuous/checkpoint.pt'
        current.save(expected)
        del current
        collect()
        current = trainer()
        actual = []
        for _ in range(2):
            check()
            actual.append(current.step())
        mid = gate / mode / 'paused/checkpoint.pt'
        current.save(mid)
        del current
        collect()
        current = StableExtensionTrainer(plan['model_config'], web, spec, 'cuda')
        current.load(mid)
        for _ in range(2):
            check()
            actual.append(current.step())
        resumed = gate / mode / 'resumed/checkpoint.pt'
        current.save(resumed)
        del current
        collect()
        left = torch.load(expected, map_location='cpu', weights_only=False)
        right = torch.load(resumed, map_location='cpu', weights_only=False)
        for key in left:
            checks[mode + ':' + key] = equal_state(left[key], right[key])
        checks[mode + ':finite'] = finite_state(left) and finite_state(right)
        for key in ('loss', 'lr', 'token_digest', 'tokens_seen'):
            checks[mode + ':history:' + key] = [r[key] for r in history] == [r[key] for r in actual]
        if mode == 'stable-extension':
            parent = torch.load(source, map_location='cpu', weights_only=False)
            initial = torch.load(gate / mode / 'paused/checkpoint.pt', map_location='cpu', weights_only=False)
            checks['stable:first_LR_no_jump'] = history[0]['lr'] == parent['optimizer']['param_groups'][0]['lr'] == .002
            checks['stable:parent_cursor_advances_exactly64_blocks'] = initial['sampler']['position'] == parent['sampler']['position'] + 64
            del parent, initial
        histories[mode] = {'continuous': history, 'resumed': actual}
        checkpoints.extend((expected, mid, resumed))
        del left, right
    result = {'passed': all(checks.values()), 'checks': checks, 'binding': binding,
              'optimizer_updates': 16, 'input_tokens': 524288, 'histories': histories,
              'checkpoint_sha256': {str(p): sha256(p) for p in checkpoints}, 'completed_at': now()}
    write_json(result_path, result)
    assert result['passed'], checks
    return result


def train_stage(plan, web, output, stage, binding, heartbeat, check):
    directory = output / stage
    directory.mkdir(parents=True, exist_ok=True)
    result_path = directory / 'result.json'
    if result_path.exists():
        result = read_json(result_path)
        assert result['binding'] == binding and result['status'] == 'complete'
        assert sha256(Path(result['checkpoint'])) == result['checkpoint_sha256']
        return result
    spec = dict(plan['spec'])
    if stage == 'decay':
        source = output / 'stable' / f"checkpoint-{plan['stable_end_update']:08d}.pt"
        spec.update(scheduler='wsd_decay', schedule_updates=plan['end_update'],
                    branch_at=plan['stable_end_update'], decay_updates=plan['decay_updates'],
                    minimum_lr_ratio=plan['minimum_lr_ratio'])
    else:
        source = Path(plan['parent']['path'])
    trainer = StableExtensionTrainer(plan['model_config'], web, spec, 'cuda')
    latest = directory / 'latest.json'
    metrics = directory / 'metrics.jsonl'
    if latest.exists():
        saved = read_json(latest)
        assert sha256(Path(saved['path'])) == saved['sha256']
        trainer.load(Path(saved['path']))
        if metrics.exists():
            rows = [json.loads(line) for line in metrics.read_text().splitlines()]
            if rows and rows[-1]['update'] > trainer.update:
                shutil.copyfile(metrics, directory / f'metrics-before-resume-{time.time_ns()}.jsonl')
                metrics.write_text(''.join(json.dumps(r) + '\n' for r in rows if r['update'] <= trainer.update))
    elif stage == 'stable':
        trainer.load_extension(source, plan['parent']['sha256'])
    else:
        trainer.load(source, decay_branch=True)
    started = time.monotonic()
    with metrics.open('a', buffering=1) as stream:
        while trainer.update < spec['schedule_updates']:
            try:
                check()
            except (InterruptedError, TimeoutError):
                trainer.save(directory / f'checkpoint-{trainer.update:08d}.pt')
                raise
            row = trainer.step()
            stream.write(json.dumps(row, allow_nan=False) + '\n')
            if trainer.update % plan['log_every'] == 0:
                heartbeat(stage, update=trainer.update, tokens=trainer.tokens, loss=row['loss'],
                          lr=row['lr'], tokens_per_second=row['tokens_per_second'])
                print(json.dumps(dict(stage=stage, **row)), flush=True)
            if trainer.update % plan['save_every'] == 0:
                trainer.save(directory / f'checkpoint-{trainer.update:08d}.pt')
    checkpoint = directory / f'checkpoint-{trainer.update:08d}.pt'
    trainer.save(checkpoint)
    rows = [json.loads(line) for line in metrics.read_text().splitlines()]
    begin = plan['parent']['update'] if stage == 'stable' else plan['stable_end_update']
    assert [r['update'] for r in rows] == list(range(begin + 1, trainer.update + 1))
    assert all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in rows)
    assert trainer.tokens == trainer.update * 32768
    state = torch.load(checkpoint, map_location='cpu', weights_only=False)
    assert finite_state(state)
    assert state['implementation_sha256'] == plan['implementation']
    result = {'status': 'complete', 'stage': stage, 'binding': binding,
              'checkpoint': str(checkpoint), 'checkpoint_sha256': sha256(checkpoint),
              'update': trainer.update, 'tokens': trainer.tokens,
              'additional_input_tokens': (trainer.update - begin) * 32768,
              'training_step_seconds': sum(r['seconds'] for r in rows),
              'steady_tokens_per_second': statistics.median(r['tokens_per_second'] for r in rows[25:]),
              'this_launch_wall_seconds': time.monotonic() - started,
              'first_lr': rows[0]['lr'], 'last_update_lr': rows[-1]['lr'],
              'next_lr': trainer.optimizer.param_groups[0]['lr'],
              'sampler': trainer.sampler.state_dict(), 'lineage': trainer.lineage,
              'finite_weights_and_Adam': True, 'contiguous_completed_updates': len(rows),
              'completed_at': now()}
    write_json(result_path, result)
    del trainer, state
    collect()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT / 'configs/phase6/base_5b.json')
    parser.add_argument('--freeze', action='store_true')
    args = parser.parse_args()
    torch.set_num_threads(2)
    if args.freeze:
        plan = freeze(args.plan)
        print(json.dumps({'status': 'frozen', 'plan': str(args.plan), 'additional_tokens': plan['additional_training_tokens']}))
        return
    plan = read_json(args.plan)
    validate(plan, read_json(ROOT / 'schemas' / args.plan.relative_to(ROOT).with_suffix('.schema.json')))
    assert plan['implementation'] == implementation_hashes()
    assert plan['source_sha256'] == {p: sha256(ROOT / p) for p in SOURCES}
    for field in ('go_evidence', 'tests'):
        assert sha256(Path(plan[field]['path'])) == plan[field]['sha256']
    assert sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256']
    assert sha256(Path(plan['parent']['path'])) == plan['parent']['sha256']
    assert shutil.disk_usage(Path(plan['shards'])).free >= plan['minimum_free_bytes']
    output = ROOT / plan['output']
    output.mkdir(parents=True, exist_ok=True)
    path = output / 'job.json'
    old = read_json(path) if path.exists() else {}
    if old and alive(old):
        raise RuntimeError('Identified job is still live; do not duplicate')
    binding = {'plan_sha256': sha256(args.plan), 'implementation': plan['implementation'],
               'source_sha256': plan['source_sha256'], 'parent': plan['parent']}
    if old:
        assert old['binding'] == binding
        if old['status'] == 'complete':
            result = read_json(output / 'result.json')
            assert result['binding'] == binding
            assert sha256(Path(result['checkpoint'])) == result['checkpoint_sha256']
            print(json.dumps({'status': 'already_complete', 'tokens': result['tokens']}))
            return
    else:
        write_json(output / 'source_sha256.json', source_snapshot(output / 'snapshot'))
    prior = old.get('gpu_elapsed_seconds', 0)
    job = {**identity(), 'status': 'running', 'started_at': now(), 'binding': binding,
           'gpu_elapsed_seconds': prior, 'gpu_budget_seconds': plan['gpu_budget_seconds'], 'command': sys.argv,
           'stop_boundary': 'After total5B training/report/commit, before full evaluation/Chat/10B'}
    atomic_json(path, job)
    stopped = [False]
    start = [None]
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]:
            raise InterruptedError('Requested interruption; completed update is checkpointed')
        if start[0] is not None and prior + time.monotonic() - start[0] >= plan['gpu_budget_seconds']:
            raise TimeoutError('Cumulative frozen GPU budget exhausted')
    def heartbeat(stage, **fields):
        job.update(stage=stage, heartbeat_at=now(), **fields)
        if start[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - start[0]
        atomic_json(path, job)
    try:
        web = TrainView(plan['shards'], plan['shard_manifest_sha256'])
        assert len(web.tokens) == plan['unique_train_tokens']
        torch.cuda.set_per_process_memory_fraction(plan['memory_fraction'])
        with gpu_lock('cuda'):
            start[0] = time.monotonic()
            heartbeat('cuda-resume-gate')
            gate = cuda_gate(plan, web, output, binding, check)
            stages = {}
            for stage in ('stable', 'decay'):
                heartbeat(stage)
                stages[stage] = train_stage(plan, web, output, stage, binding, heartbeat, check)
            assert sum(s['additional_input_tokens'] for s in stages.values()) == plan['additional_training_tokens']
            assert stages['decay']['tokens'] == plan['end_tokens']
            assert sha256(Path(plan['parent']['path'])) == plan['parent']['sha256']
            result = {'status': 'complete_training_only', 'binding': binding, 'stages': stages,
                      'checkpoint': stages['decay']['checkpoint'],
                      'checkpoint_sha256': stages['decay']['checkpoint_sha256'],
                      'tokens': stages['decay']['tokens'], 'update': stages['decay']['update'],
                      'scientific_additional_input_tokens': plan['additional_training_tokens'],
                      'verification_input_tokens': gate['input_tokens'], 'resume_gate_passed': gate['passed'],
                      'parent_unchanged': True, 'quality_targets_achieved': False,
                      'evaluation_started': False, 'test_split_used': False, 'completed_at': now()}
            write_json(output / 'result.json', result)
            heartbeat('finished', tokens=result['tokens'], update=result['update'])
            job.update(status='complete', completed_at=now(), result=str(output / 'result.json'))
            print(json.dumps({'status': 'complete_training_only', 'tokens': result['tokens']}), flush=True)
    except BaseException as exc:
        job.update(status='interrupted' if isinstance(exc, (InterruptedError, TimeoutError)) else 'failed',
                   failure=f'{type(exc).__name__}: {exc}', finished_at=now())
        raise
    finally:
        if start[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - start[0]
        atomic_json(path, job)


if __name__ == '__main__':
    main()
