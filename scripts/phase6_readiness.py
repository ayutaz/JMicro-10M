"""Persistent, bounded generation/evaluation/LR and exact-resume readiness job."""
from pathlib import Path
import argparse
import fcntl
import hashlib
import json
import math
import os
import statistics
import subprocess
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from jsonschema import validate
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import evaluate_body, generate_suite, gpu_lock, implementation_hashes, rng_state, seed_all, source_snapshot
from phase6_performance import identity, alive, finite_state


def files(directory):
    return {str(path): sha256(path) for path in directory.iterdir() if path.is_file()}


def model_from_checkpoint(path, device):
    state = torch.load(path, map_location='cpu', weights_only=False)
    model = JMicroModel(state['model_config']).to(device)
    model.load_state_dict(state['model'], strict=True)
    return model, state


def score_worker(plan, checkpoint, destination, full=False, diagnostics=False):
    torch.set_num_threads(2)
    seed_all(plan['seed'])
    with gpu_lock('cuda'), sdpa_kernel([SDPBackend.MATH]):
        torch.cuda.set_per_process_memory_fraction(plan['memory_fraction'])
        model, state = model_from_checkpoint(checkpoint, 'cuda')
        before_rng = rng_state()
        before_model = {key: value.clone() for key, value in model.state_dict().items()}
        before_mode = model.training
        if diagnostics:
            tok = Tokenizer(ROOT/plan['tokenizer'])
            started = time.perf_counter()
            generation = generate_suite(model, tok, 'cuda', 'bf16', limit=plan['generation_cases'], max_new=plan['generation_tokens'], sampling=True)
            seconds = time.perf_counter()-started
            groups = {}
            failures = []
            for item in generation['outputs']:
                group = f"{item['decoding']}-suppressed{int(item['suppressed'])}-seed{item['seed']}"
                rows = groups.setdefault(group, [])
                rows.append(item)
                if not item['valid_utf8']:
                    try:
                        tok.decode_bytes(item['generated_ids']).decode()
                    except UnicodeDecodeError as error:
                        failure = {'case': item['id'], 'group': group, 'start': error.start, 'end': error.end, 'reason': error.reason, 'raw_bytes_hex': tok.decode_bytes(item['generated_ids']).hex(), 'generated_ids': item['generated_ids'], 'max_length_tail_truncation': error.reason == 'unexpected end of data' and item['stop_reason'] == 'max_new_tokens'}
                        failures.append(failure)
                    except ValueError as error:
                        failures.append({'case': item['id'], 'group': group, 'reason': str(error), 'generated_ids': item['generated_ids']})
            rates = {name: {'outputs': len(rows), 'eos': sum(row['stop_reason']=='stop_id' for row in rows), 'repetition': sum(row['repetition'] for row in rows), 'unicode_failure': sum(not row['valid_utf8'] for row in rows), 'role_leak': sum(row['role_leak'] for row in rows), 'empty': sum(row['empty_response'] for row in rows)} for name, rows in groups.items()}
            result = {'status': 'passed_diagnosis', 'checkpoint': str(checkpoint), 'checkpoint_sha256': sha256(checkpoint), 'implementation': implementation_hashes(), 'generation': generation, 'generation_seconds': seconds, 'rates': rates, 'unicode_failures': failures, 'quality_targets_achieved': False, 'human_scoring_performed': False, 'scope': '400 fixed Base dev outputs; integrity diagnosis, all quality failures retained; no forced stop counts as model quality'}
            assert len(generation['outputs']) == 400
            # This checkpoint is evaluated with changed source, never resumed.
            ids = torch.tensor([[2, *tok.encode('今日は晴れです。散歩に行きます。')]], device='cuda')
            with torch.inference_mode():
                expected = model(ids).logits
                prefix = model(ids[:, :7], use_cache=True)
                suffix = model(ids[:, 7:], cache=prefix.cache, use_cache=True)
                delta = (suffix.logits.float()-expected[:, 7:].float()).abs()
                result['cuda_cache_max_abs_error'] = float(delta.max())
                tolerance = read_json(ROOT/'configs/evaluation/protocol.json')['numeric_tolerances']['fp32_reference_logits']
                torch.testing.assert_close(suffix.logits, expected[:, 7:], **tolerance)
                result['cuda_cache_tolerance'] = tolerance
        else:
            dev = Shard(Path(plan['shards']), 'dev')
            limit = None if full else plan['score_documents']
            progress_path = destination.with_suffix('.progress.json')
            last = [0.]
            def progress(done, total):
                if time.monotonic()-last[0] > 5 or done == total:
                    write_json(progress_path, {'status': 'running', **identity(), 'at': now(), 'completed_tasks': done, 'total_tasks': total})
                    last[0] = time.monotonic()
            if full:
                scalar = evaluate_body(model, dev, 'cuda', 'bf16', limit=32)
                sample = evaluate_batched(model, dev, 'cuda', 'bf16', limit=32, batch=plan['evaluation_batch'])
                # Batch kernels can round BF16 logits differently; bind both raw
                # measurements, with a predeclared 0.001 BPB agreement gate.
                assert abs(scalar['bpb']-sample['bpb']) <= plan['evaluation_bpb_tolerance']
                sample_check = {'scalar': scalar, 'batched': sample, 'bpb_abs_difference': abs(scalar['bpb']-sample['bpb']), 'bpb_tolerance_frozen': plan['evaluation_bpb_tolerance']}
            body = evaluate_batched(model, dev, 'cuda', 'bf16', limit=limit, batch=plan['evaluation_batch'], progress=progress)
            result = {'status': 'passed', 'checkpoint': str(checkpoint), 'checkpoint_sha256': sha256(checkpoint), 'implementation': implementation_hashes(), 'body': body, 'peak_allocated': torch.cuda.max_memory_allocated(), 'peak_reserved': torch.cuda.max_memory_reserved()}
            if full:
                result['scalar_batched_gpu_agreement'] = sample_check
                details = dev.manifest['splits']['dev']
                assert body['documents'] == len(dev.index) == 89416 and body['body_bytes'] == 164344743
                assert body['body_tokens'] == sum(document['body_tokens'] for document in dev.index)
        result['evaluation_state_isolated'] = equal_state(before_rng, rng_state()) and before_mode == model.training and equal_state(before_model, model.state_dict())
        assert result['evaluation_state_isolated']
        result['completed_at'] = now()
        write_json(destination, result)
        print(json.dumps({'status': result['status'], 'task': 'diagnostics' if diagnostics else 'full-dev' if full else 'dev-score', 'bpb': result.get('body', {}).get('bpb')}), flush=True)


def compare_runs(directory, continuous_end, decay_end):
    checks = {}
    fields = ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'tokens', 'supervised_tokens', 'body_bytes', 'token_digest', 'spec', 'model_config', 'implementation_sha256', 'update')
    for prefix, end, count in [('stable', continuous_end, continuous_end), ('decay', decay_end, 100)]:
        runs = [directory/f'{prefix}-{suffix}' for suffix in ('continuous', 'resumed')]
        states = [torch.load(path/f'checkpoint-{end:08d}.pt', map_location='cpu', weights_only=False) for path in runs]
        for key in fields + (('lineage', 'branch_updates', 'branch_tokens') if prefix == 'decay' else ()):
            checks[f'{prefix}_{key}_exact'] = equal_state(states[0][key], states[1][key])
        rows = [[json.loads(line) for line in (path/'metrics.jsonl').read_text().splitlines()] for path in runs]
        checks[f'{prefix}_metrics_complete'] = len(rows[0]) == len(rows[1]) == count
        checks[f'{prefix}_finite_model_optimizer'] = all(finite_state(state) for state in states)
        for key in ('update', 'loss', 'lr', 'gradient_norm', 'tokens_seen', 'supervised_tokens', 'body_bytes_seen', 'token_digest'):
            checks[f'{prefix}_{key}_history_exact'] = [row[key] for row in rows[0]] == [row[key] for row in rows[1]]
    checks['parent_isolated_before_continuation'] = read_json(directory/'branch-isolation.json')['passed']
    result = {'status': 'passed_exact' if all(checks.values()) else 'failed', 'checks': checks, 'completed_at': now(), 'stable_updates': continuous_end, 'decay_additional_updates': 100}
    write_json(directory/'exact_report.json', result)
    assert all(checks.values()), checks
    return result


def study(plan_path, output):
    output.mkdir(parents=True, exist_ok=True)
    plan = read_json(plan_path)
    validate(plan, read_json(ROOT/'schemas/configs/phase6/readiness.schema.json'))
    torch.set_num_threads(2)
    binding = {'plan_sha256': sha256(plan_path), 'implementation': implementation_hashes(), 'runner_sha256': sha256(Path(__file__)), 'worker_sha256': sha256(ROOT/'scripts/phase6_performance.py'), 'evaluation_sha256': sha256(ROOT/'src/jmicro/readiness.py')}
    assert sha256(Path(plan['shards'])/'manifest.json') == plan['shard_manifest_sha256']
    assert sha256(ROOT/plan['tokenizer']) == plan['tokenizer_sha256']
    with (output/'supervisor.lock').open('a+') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX|fcntl.LOCK_NB)
        if (output/'binding.json').exists():
            assert read_json(output/'binding.json') == binding, 'Source changed; preserve current run and use new output'
        else:
            write_json(output/'binding.json', binding)
            write_json(output/'source_sha256.json', source_snapshot(output/'snapshot'))
        if (output/'job.json').exists():
            previous = read_json(output/'job.json')
            if previous.get('worker') and alive(previous['worker']):
                raise RuntimeError('Existing identified worker; do not duplicate it')
            if previous['status'] == 'complete':
                print('Readiness complete; not rerunning', flush=True)
                return
        gpu = subprocess.run(['/usr/lib/wsl/lib/nvidia-smi', '--query-compute-apps=pid', '--format=csv,noheader'], text=True, capture_output=True, check=True)
        assert not gpu.stdout.strip(), 'Existing GPU process; do not duplicate it'
        job = {**identity(), 'status': 'running', 'started_at': now(), 'binding': binding, 'restart_command': ['uv', 'run', '--frozen', '--extra', 'hub', '--extra', 'data', '--extra', 'ml', '--extra', 'export', 'scripts/phase6_readiness.py', '--plan', str(plan_path), '--output', str(output)]}
        write_json(output/'job.json', job)
        candidate = read_json(ROOT/'reports/phase5/candidate_configs.json')['100m-no-qknorm']
        checkpoint = Path(candidate['checkpoint'])
        assert sha256(checkpoint) == candidate['checkpoint_sha256']
        results = []
        def command(label, args, result, environment=None):
            if result.exists() and read_json(result)['status'].startswith('passed'):
                return read_json(result)
            if result.exists() and read_json(result)['status'] in ('failed', 'oom'):
                raise RuntimeError(f'Failed stage preserved: {label}; inspect before retry')
            log = output/f'{label}.log'
            with log.open('a') as stream:
                child = subprocess.Popen([sys.executable, *args], stdout=stream, stderr=subprocess.STDOUT, env=environment)
                job.update(stage=label, worker=identity(child.pid), command=[sys.executable, *args], log=str(log), heartbeat_at=now())
                write_json(output/'job.json', job)
                launched = time.monotonic()
                while child.poll() is None:
                    time.sleep(2)
                    job['heartbeat_at'] = now()
                    write_json(output/'job.json', job)
                    if time.monotonic()-launched > plan['worker_timeout_seconds']:
                        child.terminate()
                        try:
                            child.wait(timeout=30)
                        except subprocess.TimeoutExpired:
                            child.kill()
                            child.wait(timeout=30)
                        raise TimeoutError(f'{label}: preserve checkpoints/log before retry')
                if child.returncode or not result.exists() or not read_json(result)['status'].startswith('passed'):
                    raise RuntimeError(f'{label} failed, exit {child.returncode}; inspect {log}')
            value = read_json(result)
            print(json.dumps({'stage': label, 'status': value['status']}), flush=True)
            job['worker'] = None
            return value
        def score(label, path, full=False, diagnostics=False):
            result = output/f'{label}.json'
            flags = ['--full'] if full else ['--diagnostics'] if diagnostics else []
            return command(label, [str(Path(__file__)), '--score-checkpoint', str(path), '--plan', str(plan_path), '--result', str(result), *flags], result)
        def train(label, run, lr, budget, stop, warmup, parent=None, cold=False):
            worker_plan = dict(plan, lr=lr, warmup=warmup, exact_decay_updates=100, short_probe_warmup=8, evaluation_documents=4, generation_cases=1, generation_tokens=8)
            request = {'plan': worker_plan, 'variant': plan['variant'], 'batch': plan['batch'], 'kind': 'confirmation' if budget == 2000 and parent is None else 'verify', 'budget': budget, 'stop_after': stop, 'run': str(run), 'branch_from': str(parent) if parent else None, 'measurement_warmup': 200, 'implementation_sha256': binding['implementation']}
            request_path = output/'requests'/f'{label}.json'
            if request_path.exists():
                assert read_json(request_path) == request
            write_json(request_path, request)
            result = output/'results'/f'{label}.json'
            environment = dict(os.environ, JMICRO_COMPILE_CACHE_ROOT=str(output/'cold-cache')) if cold else None
            value = command(label, [str(ROOT/'scripts/phase6_performance.py'), '--worker-request', str(request_path), '--worker-output', str(result)], result, environment)
            results.append(value)
            return value
        try:
            score('generation_diagnostics', checkpoint, diagnostics=True)
            score('expanded_dev_baseline', checkpoint, full=True)
            lr_results = []
            for lr in plan['learning_rates']:
                label = f'lr-{lr}'
                stable_dir = output/'stability'/label/'stable'
                stable = train(label+'-stable', stable_dir, lr, 2000, 2000, 200)
                before_path = output/'stability'/label/'parent_before.json'
                if not before_path.exists():
                    write_json(before_path, files(stable_dir))
                decay_dir = output/'stability'/label/'decay'
                decay = train(label+'-decay', decay_dir, lr, 2100, 2100, 200, Path(stable['checkpoint']))
                assert files(stable_dir) == read_json(before_path), 'Decay changed parent files'
                score_value = score(label+'-score', Path(decay['checkpoint']))
                lr_results.append({'lr': lr, 'stable': stable, 'decay': decay, 'dev': score_value, 'parent_files_immutable': True})
                write_json(output/'stability_progress.json', {'status': 'running', 'results': lr_results})
            selected = min(lr_results, key=lambda row: row['dev']['body']['bpb'])
            lr = selected['lr']
            directory = output/'exact-selected'
            parent = directory/'stable-resumed/checkpoint-00000200.pt'
            train('exact-stable-continuous', directory/'stable-continuous', lr, 400, 400, 200)
            train('exact-stable-half', directory/'stable-resumed', lr, 400, 200, 200)
            if not (directory/'parent-before-branches.json').exists():
                write_json(directory/'parent-before-branches.json', files(parent.parent))
            train('exact-decay-continuous', directory/'decay-continuous', lr, 300, 300, 200, parent)
            train('exact-decay-half', directory/'decay-resumed', lr, 300, 250, 200, parent)
            train('exact-decay-resumed', directory/'decay-resumed', lr, 300, 300, 200, parent)
            if not (directory/'branch-isolation.json').exists():
                before = read_json(directory/'parent-before-branches.json')
                after = files(parent.parent)
                assert before == after
                write_json(directory/'branch-isolation.json', {'passed': True, 'before': before, 'after': after})
            train('exact-stable-resumed', directory/'stable-resumed', lr, 400, 400, 200)
            exact = compare_runs(directory, 400, 300)
            cold_dir = output/'cold-resumed'
            cold_dir.mkdir(exist_ok=True)
            if not (output/'cold-initial.json').exists():
                assert not (output/'cold-cache').exists()
                write_json(output/'cold-initial.json', {'empty': True, 'before': files(parent.parent)})
                write_json(cold_dir/'latest.json', {'path': str(parent), 'sha256': sha256(parent), 'update': 200})
            if (output/'cold-cache').exists() and not any(cold_dir.glob('checkpoint-*.pt')) and not (output/'results/exact-cold-resume.json').exists():
                raise ValueError('Cold cache warmed before trajectory checkpoint; preserve output and use new cold run')
            cold_result = train('exact-cold-resume', cold_dir, lr, 400, 400, 200, cold=True)
            continuous = torch.load(directory/'stable-continuous/checkpoint-00000400.pt', map_location='cpu', weights_only=False)
            resumed = torch.load(cold_result['checkpoint'], map_location='cpu', weights_only=False)
            keys = ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'tokens', 'supervised_tokens', 'body_bytes', 'token_digest', 'spec', 'model_config', 'implementation_sha256', 'update')
            cold_checks = {f'{key}_exact': equal_state(continuous[key], resumed[key]) for key in keys}
            cold_checks['parent_all_files_immutable'] = files(parent.parent) == read_json(output/'cold-initial.json')['before']
            cold_checks['compiler_cache_was_empty'] = read_json(output/'cold-initial.json')['empty']
            cold_checks['compiler_cache_namespace_separate'] = Path(cold_result['compile_cache']).is_relative_to(output/'cold-cache')
            expected_rows = [json.loads(line) for line in (directory/'stable-continuous/metrics.jsonl').read_text().splitlines() if json.loads(line)['update'] > 200]
            actual_rows = [json.loads(line) for line in (cold_dir/'metrics.jsonl').read_text().splitlines()]
            cold_checks['200_resumed_updates'] = len(expected_rows) == len(actual_rows) == 200
            for key in ('update', 'loss', 'lr', 'gradient_norm', 'tokens_seen', 'supervised_tokens', 'body_bytes_seen', 'token_digest'):
                cold_checks[f'{key}_history_exact'] = [row[key] for row in expected_rows] == [row[key] for row in actual_rows]
            assert all(cold_checks.values()), cold_checks
            write_json(output/'cold_resume_report.json', {'status': 'passed_exact', 'checks': cold_checks, 'worker_result': cold_result, 'completed_at': now()})
            report = {'status': 'passed', 'binding': binding, 'plan': plan, 'lr_results': lr_results, 'selected_lr': lr, 'exact': exact, 'cold_checks': cold_checks, 'full_dev': str(output/'expanded_dev_baseline.json'), 'generation_diagnostics': str(output/'generation_diagnostics.json'), 'training_results': results, 'completed_at': now(), 'scope': 'Bounded readiness comparisons, not a long Base scaling checkpoint; Base quality remains unmet'}
            write_json(output/'readiness_stability_report.json', report)
            job.update(status='complete', completed_at=now(), worker=None, selected_lr=lr)
        except Exception as error:
            job.update(status='failed', failure=f'{type(error).__name__}: {error}', completed_at=now())
            raise
        finally:
            write_json(output/'job.json', job)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT/'configs/phase6/readiness.json')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--score-checkpoint', type=Path)
    parser.add_argument('--result', type=Path)
    parser.add_argument('--full', action='store_true')
    parser.add_argument('--diagnostics', action='store_true')
    args = parser.parse_args()
    if args.score_checkpoint:
        score_worker(read_json(args.plan), args.score_checkpoint, args.result, args.full, args.diagnostics)
    elif args.output:
        study(args.plan.resolve(), args.output.resolve())
    else:
        parser.error('--output or --score-checkpoint is required')
