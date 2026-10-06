"""Persistent, bounded selected-model CUDA capacity/compile/exact-resume study.

Launch with uv. Every worker reuses that interpreter. No Base scaling run is
started here; all output paths/checkpoints are performance evidence only.
"""
from pathlib import Path
import argparse
import fcntl
import hashlib
import json
import logging
import math
import os
import platform
import statistics
import subprocess
import sys
import time
import traceback

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jsonschema import validate
from jmicro.experiment import ROOT, capture_environment, now, read_json, sha256, write_json
from jmicro.phase5 import equal_state
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import (Trainer, evaluate_body, generate_suite, gpu_lock,
                            implementation_hashes, rng_state, source_snapshot)


def identity(pid=None):
    pid = os.getpid() if pid is None else pid
    return {'pid': pid, 'boot_id': Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
            'start_ticks': Path(f'/proc/{pid}/stat').read_text().split()[21]}


def alive(row):
    try:
        return identity(row['pid']) == {key: row[key] for key in ('pid', 'boot_id', 'start_ticks')}
    except FileNotFoundError:
        return False


def finite_state(state):
    tensors = [*state['model'].values(), *[tensor for row in state['optimizer']['state'].values()
                for tensor in row.values() if isinstance(tensor, torch.Tensor)]]
    return all(torch.isfinite(tensor).all().item() for tensor in tensors)


def spec_for(plan, variant, batch, budget):
    spec = {key: plan[key] for key in ('seed', 'context', 'dtype', 'accumulation', 'lr', 'weight_decay', 'warmup')}
    spec.update(batch=batch, schedule_updates=budget, scheduler='wsd',
                backend=variant['backend'], compile=variant['compile'])
    for key in ('training_fast_path', 'deterministic', 'compile_mode'):
        if variant.get(key):
            spec[key] = variant[key]
    return spec


def worker(request, destination):
    request_hash = sha256(request)
    args = read_json(request)
    plan, variant = args['plan'], args['variant']
    assert implementation_hashes() == args['implementation_sha256']
    torch.set_num_threads(2)
    run = Path(args['run'])
    run.mkdir(parents=True, exist_ok=True)
    result = {'status': 'running', 'request_sha256': request_hash, 'started_at': now(),
              'variant': variant, 'batch': args['batch'], 'kind': args['kind'], **identity()}
    write_json(destination, result)
    started = time.perf_counter()
    try:
        with gpu_lock('cuda'):
            torch.cuda.set_per_process_memory_fraction(plan['memory_fraction'])
            generated_log = run/'generated_code.log'
            if variant['compile']:
                code_logger = torch._logging.getArtifactLogger('torch._inductor.codecache', 'output_code')
                code_logger.setLevel(logging.DEBUG)
                code_logger.propagate = False
                code_handler = logging.FileHandler(generated_log, mode='a')
                code_logger.addHandler(code_handler)
            model = read_json(ROOT/'reports/phase5/candidate_configs.json')['100m-no-qknorm']['model_config']
            shards = Path(plan['shards'])
            spec = spec_for(plan, variant, args['batch'], args['budget'])
            if args.get('branch_from'):
                parent = torch.load(args['branch_from'], map_location='cpu', weights_only=False)
                spec.update(scheduler='wsd_decay', branch_at=parent['update'],
                            decay_updates=plan['exact_decay_updates'], minimum_lr_ratio=.1)
            trainer = Trainer(model, Shard(shards), spec, 'cuda')
            record = {**identity(), 'status': 'running', 'spec': spec, 'model_config': model,
                      'implementation_sha256': implementation_hashes(), 'request_sha256': request_hash,
                      'command': sys.argv, 'updated_at': now()}
            if (run/'latest.json').exists():
                latest = read_json(run/'latest.json')
                if sha256(Path(latest['path'])) != latest['sha256']:
                    raise ValueError('Checkpoint SHA differs; refuse restart')
                trainer.load(Path(latest['path']))
            elif args.get('branch_from'):
                trainer.load(Path(args['branch_from']), decay_branch=True)
            elif (run/'metrics.jsonl').exists():
                raise ValueError('Partial metrics without valid checkpoint; use a new run')
            if not (run/'environment.json').exists():
                write_json(run/'environment.json', capture_environment(probe_torch=True))
            rows = [json.loads(line) for line in (run/'metrics.jsonl').read_text().splitlines()] if (run/'metrics.jsonl').exists() else []
            rows = [row for row in rows if row['update'] <= trainer.update]
            (run/'metrics.jsonl').write_text(''.join(json.dumps(row)+'\n' for row in rows))
            write_json(run/'run.json', record)
            torch.cuda.reset_peak_memory_stats()
            profile_result = None
            profile_path = run/'attention_profile.json'
            if profile_path.exists():
                profile_result = read_json(profile_path)
            with (run/'metrics.jsonl').open('a', buffering=1) as stream:
                while trainer.update < args['stop_after']:
                    if args['kind'] in ('probe', 'confirmation') and profile_result is None and len(rows) == plan['short_probe_warmup']:
                        with torch.profiler.profile(activities=[torch.profiler.ProfilerActivity.CPU]) as profiler:
                            row = trainer.step()
                        operators = {event.key: event.count for event in profiler.key_averages()}
                        flash = operators.get('aten::_scaled_dot_product_flash_attention', 0)
                        math_bmm = operators.get('aten::bmm', 0)
                        expected = variant['backend']
                        runtime_correct = flash > 0 if expected == 'flash' else flash == 0 and math_bmm > 0
                        compiled_calls = [name for name in operators if name.startswith('## Call CompiledFxGraph ')]
                        generated = generated_log.read_text() if generated_log.exists() else ''
                        generated_flash = 'torch.ops.aten._scaled_dot_product_flash_attention.default(' in generated
                        generated_math = 'extern_kernels.bmm(' in generated
                        generated_correct = generated_flash if expected == 'flash' else not generated_flash and generated_math
                        # CUDA Graph replay omits inner CPU ATen hooks. Require
                        # this worker's emitted code AND real compiled graph calls.
                        correct = runtime_correct or bool(compiled_calls and generated_correct)
                        profile_result = {'requested_backend': expected, 'actual_backend_verified': correct,
                            'flash_forward_count': flash, 'math_bmm_count': math_bmm, 'operators': operators,
                            'profiled_update': row['update'], 'compile_cache': trainer.compile_cache,
                            'compiled_calls': compiled_calls, 'generated_code': str(generated_log) if generated else None,
                            'generated_code_sha256': sha256(generated_log) if generated else None,
                            'generated_flash_call': generated_flash, 'generated_math_bmm_call': generated_math,
                            'method': 'Actual CUDA completed-update CPU ATen trace; CUDA Graph replay also requires emitted backend-specific code plus runtime CompiledFxGraph calls; no kernel-name substring inference'}
                        write_json(profile_path, profile_result)
                        row['profiled'] = True
                        if not correct:
                            raise ValueError(f'Actual attention operators differ from requested backend: {expected}, flash={flash}, bmm={math_bmm}')
                    else:
                        row = trainer.step()
                    rows.append(row)
                    stream.write(json.dumps(row, allow_nan=False)+'\n')
                    if trainer.update == 1 or trainer.update % 50 == 0:
                        print(json.dumps({'variant': variant['name'], 'batch': args['batch'], 'kind': args['kind'], **row}), flush=True)
                    if trainer.update % 50 == 0:
                        trainer.save(run/f'checkpoint-{trainer.update:08d}.pt')
                        record.update(update=trainer.update, tokens=trainer.tokens, heartbeat_at=now())
                        write_json(run/'run.json', record)
            training_peak = torch.cuda.max_memory_allocated()
            training_reserved = torch.cuda.max_memory_reserved()
            checkpoint = run/f'checkpoint-{trainer.update:08d}.pt'
            save_seconds = trainer.save(checkpoint)
            state = torch.load(checkpoint, map_location='cpu', weights_only=False)
            if not finite_state(state) or not all(math.isfinite(row['loss']) and math.isfinite(row['gradient_norm']) for row in rows):
                raise ValueError('Nonfinite training state')
            before_rng = rng_state()
            before_model = {key: tensor.clone() for key, tensor in trainer.model.state_dict().items()}
            before_mode = trainer.model.training
            evaluation_started = time.perf_counter()
            body = evaluate_body(trainer.model, Shard(shards, 'dev'), 'cuda', 'bf16', limit=plan['evaluation_documents'])
            tokenizer = Tokenizer(ROOT/plan['tokenizer'])
            generation = generate_suite(trainer.model, tokenizer, 'cuda', 'bf16', limit=plan['generation_cases'], max_new=plan['generation_tokens'])
            evaluation_seconds = time.perf_counter()-evaluation_started
            isolated = equal_state(before_rng, rng_state()) and equal_state(before_model, trainer.model.state_dict()) and before_mode == trainer.model.training
            if not isolated:
                raise ValueError('Evaluation changed training RNG/model/mode')
            # Release cloned validation weights before measuring total allocation.
            del before_model
            measured = rows[args['measurement_warmup']:] if args['kind'] == 'probe' else rows[min(20, len(rows)//4):]
            measured = [row for row in measured if not row.get('profiled')]
            result.update(status='passed', completed_at=now(), spec=spec, update=trainer.update,
                          checkpoint=str(checkpoint), checkpoint_sha256=sha256(checkpoint), checkpoint_bytes=checkpoint.stat().st_size,
                          finite=True, steady_tokens_per_second=statistics.median(row['tokens_per_second'] for row in measured),
                          p95_update_seconds=sorted(row['seconds'] for row in measured)[int(.95*(len(measured)-1))],
                          first_update_seconds=rows[0]['seconds'], data_wait_seconds=sum(row['data_wait_seconds'] for row in measured),
                          measured_seconds=sum(row['seconds'] for row in measured), update_wall_seconds=sum(row['seconds'] for row in rows),
                          peak_vram_training=training_peak, peak_vram_reserved_training=training_reserved,
                          peak_vram_with_evaluation_save=torch.cuda.max_memory_allocated(),
                          peak_vram_reserved_with_evaluation_save=torch.cuda.max_memory_reserved(), save_seconds=save_seconds,
                          evaluation_seconds=evaluation_seconds, evaluation_bpb=body['bpb'], evaluation_documents=body['documents'],
                          generation_outputs=len(generation['outputs']), evaluation_state_isolated=isolated,
                          deterministic_algorithms=torch.are_deterministic_algorithms_enabled(),
                          cublas_workspace=os.environ.get('CUBLAS_WORKSPACE_CONFIG'), implementation_sha256=implementation_hashes(),
                          attention_profile=profile_result, compile_cache=trainer.compile_cache)
            record.update(status='complete' if trainer.update == args['budget'] else 'paused', update=trainer.update,
                          tokens=trainer.tokens, checkpoint=str(checkpoint), completed_at=now())
            write_json(run/'run.json', record)
    except torch.cuda.OutOfMemoryError as exc:
        result.update(status='oom', failure=str(exc), completed_at=now())
    except Exception as exc:
        result.update(status='failed', failure=f'{type(exc).__name__}: {exc}', completed_at=now())
        traceback.print_exc()
    finally:
        result['worker_wall_seconds'] = time.perf_counter()-started
        if result['status'] in ('oom', 'failed') and (run/'run.json').exists():
            failed_record = read_json(run/'run.json')
            failed_record.update(status=result['status'], failure=result.get('failure'), completed_at=now())
            write_json(run/'run.json', failed_record)
        write_json(destination, result)
    print(json.dumps({key: result.get(key) for key in ('status', 'kind', 'batch', 'steady_tokens_per_second', 'failure')}), flush=True)


def exact_report(directory, batch):
    checks = {}
    fields = ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'tokens', 'supervised_tokens', 'body_bytes', 'token_digest', 'spec', 'model_config', 'implementation_sha256', 'update')
    for prefix in ('stable', 'decay'):
        runs = [directory/f'{prefix}-{suffix}' for suffix in ('continuous', 'resumed')]
        states = [torch.load(run/'checkpoint-00000200.pt', map_location='cpu', weights_only=False) for run in runs]
        for key in fields+ (('lineage', 'branch_updates', 'branch_tokens') if prefix == 'decay' else ()):
            checks[f'{prefix}_{key}_exact'] = equal_state(states[0][key], states[1][key])
        rows = [[json.loads(line) for line in (run/'metrics.jsonl').read_text().splitlines()] for run in runs]
        checks[f'{prefix}_metrics_complete'] = len(rows[0]) == len(rows[1]) == (200 if prefix == 'stable' else 100)
        for key in ('update', 'loss', 'lr', 'gradient_norm', 'tokens_seen', 'supervised_tokens', 'body_bytes_seen', 'token_digest'):
            checks[f'{prefix}_{key}_history_exact'] = [row[key] for row in rows[0]] == [row[key] for row in rows[1]]
        checks[f'{prefix}_budget'] = all(state['tokens'] == 200*batch*1024 and state['update'] == 200 for state in states)
        checks[f'{prefix}_finite'] = all(finite_state(state) for state in states)
    before = read_json(directory/'parent-before-branches.json')
    checks['parent_checkpoint_and_run_immutable'] = read_json(directory/'branch-isolation.json')['passed'] and all(sha256(Path(path)) == expected for path, expected in before.items() if Path(path).name.startswith('checkpoint-'))
    checks['branch_budget'] = states[0]['branch_tokens'] == 100*batch*1024 and states[0]['branch_updates'] == 100
    report = {'status': 'passed_exact' if all(checks.values()) else 'failed', 'checks': checks, 'batch': batch, 'completed_at': now()}
    write_json(directory/'exact_report.json', report)
    return report


def study(plan_path, output):
    plan = read_json(plan_path)
    validate(plan, read_json(ROOT/'schemas/configs/phase6/performance.schema.json'))
    assert platform.python_version() == '3.12.7'
    assert sha256(ROOT/plan['tokenizer']) == plan['tokenizer_sha256']
    assert sha256(Path(plan['shards'])/'manifest.json') == plan['shard_manifest_sha256']
    output.mkdir(parents=True, exist_ok=True)
    with (output/'supervisor.lock').open('a+') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX|fcntl.LOCK_NB)
        if (output/'job.json').exists() and read_json(output/'job.json')['status'] == 'complete':
            print('Performance study already complete; not launching duplicate GPU work', flush=True)
            return
        gpu = subprocess.run(['/usr/lib/wsl/lib/nvidia-smi', '--query-compute-apps=pid,process_name', '--format=csv,noheader'], text=True, capture_output=True, check=True)
        if gpu.stdout.strip():
            raise RuntimeError('Existing CUDA process; inspect its recorded identity before starting/resuming')
        source = implementation_hashes()
        binding = {'implementation': source, 'plan_sha256': sha256(plan_path), 'runner_sha256': sha256(Path(__file__)), 'shards_sha256': plan['shard_manifest_sha256']}
        if (output/'binding.json').exists() and read_json(output/'binding.json') != binding:
            raise ValueError('Frozen performance study source/config changed; preserve old run and use a new output')
        write_json(output/'binding.json', binding)
        if not (output/'source_sha256.json').exists():
            write_json(output/'source_sha256.json', source_snapshot(output/'snapshot'))
        job = {**identity(), 'status': 'running', 'started_at': now(), 'stage': 'initial probes',
               'restart_command': ['uv', 'run', '--frozen', '--extra', 'hub', '--extra', 'data', '--extra', 'ml', '--extra', 'export', 'scripts/phase6_performance.py', '--plan', str(plan_path), '--output', str(output)]}
        results = []
        def run(variant, batch, label, kind='probe', steps=None, run_dir=None, stop_after=None, branch_from=None):
            if steps is None:
                steps = plan['short_probe_updates']
            budget = (plan['short_probe_warmup']+steps) if kind == 'probe' else 200
            request = dict(plan=plan, variant=variant, batch=batch, kind=kind, budget=budget,
                           stop_after=budget if stop_after is None else stop_after,
                           measurement_warmup=plan['short_probe_warmup'], implementation_sha256=source,
                           run=str(run_dir or output/'runs'/label), branch_from=str(branch_from) if branch_from else None)
            request_path = output/'requests'/f'{label}.json'
            result_path = output/'results'/f'{label}.json'
            if request_path.exists() and read_json(request_path) != request:
                raise ValueError('Frozen worker request changed')
            write_json(request_path, request)
            if result_path.exists():
                cached = read_json(result_path)
                if cached['status'] in ('passed', 'oom', 'failed'):
                    assert cached['request_sha256'] == sha256(request_path)
                    results.append(cached | {'report': str(result_path)})
                    return cached
                if alive(cached):
                    raise RuntimeError('Recorded worker is still alive; do not duplicate it')
            command = [sys.executable, str(Path(__file__).resolve()), '--worker-request', str(request_path), '--worker-output', str(result_path)]
            log = output/'logs'/f'{label}.log'
            log.parent.mkdir(parents=True, exist_ok=True)
            with log.open('a') as stream:
                child = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT)
                job.update(stage=label, worker=identity(child.pid), command=command, log=str(log), heartbeat_at=now())
                write_json(output/'job.json', job)
                launched = time.monotonic()
                telemetry = []
                while child.poll() is None:
                    time.sleep(2)
                    sample = subprocess.run(['/usr/lib/wsl/lib/nvidia-smi', '--query-gpu=utilization.gpu,memory.used,memory.total,power.draw', '--format=csv,noheader,nounits'], text=True, capture_output=True)
                    telemetry.append({'at': now(), 'gpu_util_memory_mib_power_w': sample.stdout.strip(), 'exit_code': sample.returncode})
                    job['heartbeat_at'] = now()
                    write_json(output/'job.json', job)
                    if time.monotonic()-launched > plan['worker_timeout_seconds']:
                        child.terminate()
                        try:
                            child.wait(timeout=30)
                        except subprocess.TimeoutExpired:
                            child.kill()
                            child.wait()
                        raise TimeoutError(f'Worker timed out; preserve log/checkpoint: {label}')
                write_json(output/'telemetry'/f'{label}.json', telemetry)
            if child.returncode or not result_path.exists():
                raise RuntimeError(f'Worker exited without complete report: {label}; see {log}')
            result = read_json(result_path)
            results.append(result | {'report': str(result_path)})
            write_json(output/'progress.json', {'status': 'running', 'results': results})
            print(json.dumps({'probe': label, 'status': result['status'], 'speed': result.get('steady_tokens_per_second'), 'peak_gib': result.get('peak_vram_training', 0)/1024**3, 'failure': result.get('failure')}), flush=True)
            return result
        try:
            initial = []
            for variant in plan['variants']:
                result = run(variant, 8, f"initial-{variant['name']}-b8")
                if result['status'] == 'passed':
                    initial.append((variant, result))
            if not initial:
                raise ValueError('No finite candidate')
            # Include both attention families: batch-8 speed cannot predict the
            # speed or memory advantage of Flash at larger batches.
            baseline = next(pair for pair in initial if pair[0]['name'] == 'reference-math')
            best_math = max((pair for pair in initial if pair[0]['backend'] == 'math'), key=lambda pair: pair[1]['steady_tokens_per_second'])
            fastest = max(initial, key=lambda pair: pair[1]['steady_tokens_per_second'])
            best_flash = max((pair for pair in initial if pair[0]['backend'] == 'flash'), key=lambda pair: pair[1]['steady_tokens_per_second'], default=None)
            variants = {pair[0]['name']: pair[0] for pair in (baseline, best_math, best_flash, fastest) if pair is not None}
            capacity, eligible = {}, []
            def verify(variant, batch, label):
                directory = output/'exact'/label
                if (directory/'exact_report.json').exists():
                    # Parent run files intentionally change during the final
                    # stable continuation. Re-audit completed results directly,
                    # rather than comparing them to the pre-branch manifest.
                    return exact_report(directory, batch)
                stages = [('stable-continuous', 200, None), ('stable-resumed', 100, None),
                          ('decay-continuous', 200, directory/'stable-resumed/checkpoint-00000100.pt'),
                          ('decay-resumed', 150, directory/'stable-resumed/checkpoint-00000100.pt'),
                          ('decay-resumed', 200, directory/'stable-resumed/checkpoint-00000100.pt')]
                for index, (name, stop, parent) in enumerate(stages):
                    if index == 2:
                        parent_run = directory/'stable-resumed'
                        if not (directory/'parent-before-branches.json').exists():
                            write_json(directory/'parent-before-branches.json', {str(path): sha256(path) for path in parent_run.iterdir() if path.is_file()})
                    result = run(variant, batch, f'{label}-verify-{index}', kind='verify', run_dir=directory/name, stop_after=stop, branch_from=parent)
                    if result['status'] != 'passed':
                        return {'status': 'failed', 'failed_worker': result}
                # Check parent before continuing it, then compare continuous final state.
                before = read_json(directory/'parent-before-branches.json')
                continued = (directory/'stable-resumed/checkpoint-00000200.pt').exists()
                if continued and not (directory/'branch-isolation.json').exists():
                    raise ValueError('Stable continuation exists without parent isolation evidence')
                if not continued and not all(sha256(Path(path)) == value for path, value in before.items()):
                    raise ValueError('Decay branch changed parent files')
                if not continued:
                    write_json(directory/'branch-isolation.json', {'passed': True, 'checked_at': now(), 'before': before,
                        'after': {path: sha256(Path(path)) for path in before}})
                result = run(variant, batch, f'{label}-verify-5', kind='verify', run_dir=directory/'stable-resumed', stop_after=200)
                if result['status'] != 'passed':
                    return {'status': 'failed', 'failed_worker': result}
                return exact_report(directory, batch)
            pending = list(variants.values())
            for variant in pending:
                first_exact = verify(variant, 8, f"{variant['name']}-b8")
                if first_exact['status'] != 'passed_exact':
                    capacity[variant['name']] = {'status': 'rejected_exact_resume', 'verification': first_exact}
                    alternatives = [(v, r) for v, r in initial if v['backend'] == variant['backend'] and v['name'] not in {item['name'] for item in pending}]
                    if alternatives:
                        pending.append(max(alternatives, key=lambda pair: pair[1]['steady_tokens_per_second'])[0])
                    continue
                low, high, batch, points = 8, None, 16, 0
                candidates = {8: next(result for v, result in initial if v['name'] == variant['name'])}
                while batch <= plan['maximum_batch_probe'] and points < plan['maximum_capacity_points_per_variant']:
                    result = run(variant, batch, f"capacity-{variant['name']}-b{batch}")
                    points += 1
                    if result['status'] == 'passed':
                        low, candidates[batch] = batch, result
                        batch *= 2
                    elif result['status'] == 'oom':
                        high = batch
                        break
                    else:
                        raise RuntimeError(f'Unexpected capacity failure: {result.get("failure")}')
                if high is not None:
                    while high-low > 1 and points < plan['maximum_capacity_points_per_variant']:
                        middle = (low+high)//2
                        result = run(variant, middle, f"capacity-{variant['name']}-b{middle}")
                        points += 1
                        if result['status'] == 'passed':
                            low, candidates[middle] = middle, result
                        elif result['status'] == 'oom':
                            high = middle
                        else:
                            raise RuntimeError(f'Unexpected boundary failure: {result.get("failure")}')
                fastest_batch = max(candidates, key=lambda size: candidates[size]['steady_tokens_per_second'])
                confirmed = {}
                for size in sorted({low, fastest_batch}):
                    exact = first_exact if size == 8 else verify(variant, size, f"{variant['name']}-b{size}")
                    confirmations = [run(variant, size, f"confirm-{variant['name']}-b{size}-{repeat}", kind='confirmation') for repeat in range(plan['confirmation_repeats'])] if exact['status'] == 'passed_exact' else []
                    if confirmations and all(row['status'] == 'passed' for row in confirmations):
                        item = {'variant': variant, 'batch': size, 'exact': exact, 'confirmations': confirmations,
                                'median_tokens_per_second': statistics.median(row['steady_tokens_per_second'] for row in confirmations),
                                'peak_vram_bytes': max(row['peak_vram_with_evaluation_save'] for row in confirmations)}
                        confirmed[size] = item
                        eligible.append(item)
                if low not in confirmed:
                    raise ValueError('Capacity endpoint failed final verification; do not declare stable maximum')
                capacity[variant['name']] = {'status': 'verified', 'maximum_stable_batch': low, 'first_oom_batch': high,
                    'bounded_range': plan['maximum_batch_probe'], 'boundary_exact': high == low+1 if high else False,
                    'fastest_short_probe_batch': fastest_batch, 'confirmed': confirmed}
            if not eligible:
                raise ValueError('No fully verified performance configuration')
            selected = max(eligible, key=lambda row: row['median_tokens_per_second'])
            report = {'status': 'passed', 'scope': plan['scope'], 'completed_at': now(), 'binding': binding,
                      'selected': selected, 'capacity': capacity, 'initial_probes': [result for _, result in initial],
                      'results': results, 'not_achieved': ['Base/Chat quality', 'long Base training', 'long-run effective batch/LR/WSD budget freeze'],
                      'limits': 'Bounded CUDA study, 94% allocator cap, exact same-runtime resume and branch, 3x200 completed updates, dev sample only; capacity and fastest speed are separate'}
            write_json(output/'batch_performance_report.json', report)
            job.update(status='complete', completed_at=now(), worker=None, selected_batch=selected['batch'], selected_variant=selected['variant'])
        except Exception as exc:
            job.update(status='failed', completed_at=now(), failure=f'{type(exc).__name__}: {exc}')
            raise
        finally:
            write_json(output/'job.json', job)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT/'configs/phase6/performance.json')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--worker-request', type=Path)
    parser.add_argument('--worker-output', type=Path)
    args = parser.parse_args()
    if args.worker_request:
        if not args.worker_output:
            parser.error('--worker-output is required')
        worker(args.worker_request, args.worker_output)
    elif args.output:
        study(args.plan, args.output.resolve())
    else:
        parser.error('--output is required')


if __name__ == '__main__':
    main()
