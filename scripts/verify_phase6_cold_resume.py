"""Verify the selected CUDA configuration resumes with an empty compiler cache.

This bounded 100-update check uses a new run and preserves the study checkpoint.
Launch through uv after the main performance study and its processes finish.
"""
from pathlib import Path
import argparse
import fcntl
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.phase5 import equal_state
from jmicro.training import implementation_hashes


def identity(pid=None):
    pid = os.getpid() if pid is None else pid
    return {'pid': pid, 'boot_id': Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
            'start_ticks': Path(f'/proc/{pid}/stat').read_text().split()[21]}


def verify(study, output):
    torch.set_num_threads(2)
    report = read_json(study/'batch_performance_report.json')
    assert read_json(study/'job.json')['status'] == 'complete' and report['status'] == 'passed'
    assert implementation_hashes() == report['binding']['implementation']
    assert sha256(ROOT/'scripts/phase6_performance.py') == report['binding']['runner_sha256']
    selected = report['selected']
    label = f"{selected['variant']['name']}-b{selected['batch']}"
    original = study/'exact'/label
    parent = original/'stable-resumed/checkpoint-00000100.pt'
    continuous = original/'stable-continuous/checkpoint-00000200.pt'
    output.mkdir(parents=True, exist_ok=True)
    with (output/'supervisor.lock').open('a+') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX|fcntl.LOCK_NB)
        if (output/'cold_resume_report.json').exists() and read_json(output/'cold_resume_report.json')['status'] == 'passed_exact':
            print('Cold-cache check complete; not duplicating GPU work', flush=True)
            return
        if (output/'job.json').exists():
            previous = read_json(output/'job.json').get('worker')
            if previous is not None:
                try:
                    still_alive = identity(previous['pid']) == previous
                except FileNotFoundError:
                    still_alive = False
                if still_alive:
                    raise RuntimeError('Recorded cold-cache worker still alive; do not duplicate it')
        gpu = subprocess.run(['/usr/lib/wsl/lib/nvidia-smi', '--query-compute-apps=pid,process_name', '--format=csv,noheader'], text=True, capture_output=True, check=True)
        if gpu.stdout.strip():
            raise RuntimeError('Existing CUDA compute job; do not duplicate it')
        binding = {'study_report_sha256': sha256(study/'batch_performance_report.json'),
                   'parent_sha256': sha256(parent), 'implementation': implementation_hashes(),
                   'verifier_sha256': sha256(Path(__file__)), 'cache_root': str(output/'empty-cache')}
        if (output/'binding.json').exists():
            assert read_json(output/'binding.json') == binding
        else:
            write_json(output/'binding.json', binding)
            cache = Path(binding['cache_root'])
            if cache.exists() and any(cache.iterdir()):
                raise ValueError('Cold-cache root must be empty before first launch')
            write_json(output/'cache_initial_state.json', {'empty': True, 'observed_at': now(), 'root': str(cache)})
            write_json(output/'parent_before.json', {str(path): sha256(path) for path in parent.parent.iterdir() if path.is_file()})
        request = read_json(study/'requests'/f'{label}-verify-1.json')
        request.update(run=str(output/'run'), stop_after=200, kind='verify', branch_from=None)
        request_path, result_path = output/'request.json', output/'worker_result.json'
        if request_path.exists():
            assert read_json(request_path) == request
        write_json(request_path, request)
        run = Path(request['run'])
        run.mkdir(exist_ok=True)
        if not (run/'latest.json').exists():
            assert not (run/'metrics.jsonl').exists()
            write_json(run/'latest.json', {'path': str(parent), 'sha256': binding['parent_sha256'], 'update': 100})
        job = {**identity(), 'status': 'running', 'started_at': now(), 'stage': 'cold-cache-resume', 'binding': binding}
        if result_path.exists() and read_json(result_path)['status'] in ('failed', 'oom'):
            raise ValueError('Failed cold-cache worker is preserved; diagnose before a new run')
        if not result_path.exists() or read_json(result_path)['status'] != 'passed':
            # An interrupted compilation cannot become cold-cache evidence by
            # retrying from the parent against its newly warmed cache. Resume
            # only a completed-update checkpoint of the actual cold trajectory.
            cache = Path(binding['cache_root'])
            latest = read_json(run/'latest.json')
            if (output/'first_attempt.json').exists() and cache.exists() and any(cache.iterdir()) and Path(latest['path']) == parent:
                raise ValueError('Interrupted before cold trajectory checkpoint; preserve this attempt and use a new empty output')
            if not (output/'first_attempt.json').exists():
                write_json(output/'first_attempt.json', {'started_at': now(), 'cache_empty': not cache.exists() or not any(cache.iterdir())})
            environment = dict(os.environ, JMICRO_COMPILE_CACHE_ROOT=binding['cache_root'])
            command = [sys.executable, str(ROOT/'scripts/phase6_performance.py'), '--worker-request', str(request_path), '--worker-output', str(result_path)]
            with (output/'worker.log').open('a') as log:
                child = subprocess.Popen(command, env=environment, stdout=log, stderr=subprocess.STDOUT)
                job.update(worker=identity(child.pid), command=command, log=str(output/'worker.log'))
                write_json(output/'job.json', job)
                launched = time.monotonic()
                while child.poll() is None:
                    time.sleep(2)
                    job['heartbeat_at'] = now()
                    write_json(output/'job.json', job)
                    if time.monotonic()-launched > request['plan']['worker_timeout_seconds']:
                        child.terminate()
                        try:
                            child.wait(timeout=30)
                        except subprocess.TimeoutExpired:
                            child.kill()
                            child.wait()
                        job.update(status='failed', failure='Worker timeout; retain checkpoint for diagnosis')
                        write_json(output/'job.json', job)
                        raise TimeoutError(job['failure'])
                if child.returncode:
                    raise RuntimeError(f'Cold-cache worker exit {child.returncode}; inspect its log')
        result = read_json(result_path)
        if result['status'] != 'passed':
            job.update(status='failed', worker=None, completed_at=now(), failure=result.get('failure'))
            write_json(output/'job.json', job)
            raise RuntimeError(result.get('failure'))
        states = [torch.load(path, map_location='cpu', weights_only=False) for path in (continuous, Path(result['checkpoint']))]
        fields = ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'tokens', 'supervised_tokens', 'body_bytes',
                  'token_digest', 'spec', 'model_config', 'implementation_sha256', 'update')
        checks = {f'{key}_exact': equal_state(states[0][key], states[1][key]) for key in fields}
        before = read_json(output/'parent_before.json')
        checks['all_parent_files_immutable'] = all(sha256(Path(path)) == value for path, value in before.items())
        checks['cache_was_empty_before_first_worker'] = read_json(output/'cache_initial_state.json')['empty']
        checks['cache_namespace_isolated'] = Path(result['compile_cache']).is_relative_to(Path(binding['cache_root'])) if selected['variant']['compile'] else result['compile_cache'] is None
        checks['checkpoint_sha256_exact'] = sha256(Path(result['checkpoint'])) == result['checkpoint_sha256']
        rows = [[json.loads(line) for line in path.read_text().splitlines()] for path in (original/'stable-continuous/metrics.jsonl', run/'metrics.jsonl')]
        rows[0] = [row for row in rows[0] if row['update'] > 100]
        checks['100_completed_resumed_updates'] = len(rows[0]) == len(rows[1]) == 100
        for key in ('update', 'loss', 'lr', 'gradient_norm', 'tokens_seen', 'supervised_tokens', 'body_bytes_seen', 'token_digest'):
            checks[f'{key}_history_exact'] = [row[key] for row in rows[0]] == [row[key] for row in rows[1]]
        status = 'passed_exact' if all(checks.values()) else 'failed'
        write_json(output/'cold_resume_report.json', {'status': status, 'checks': checks, 'binding': binding,
            'selected_variant': selected['variant'], 'batch': selected['batch'], 'completed_at': now(),
            'worker_result': result, 'compared_continuous_checkpoint': str(continuous),
            'extra_input_tokens': 100*selected['batch']*1024, 'limits': 'Same WSL/GPU/version, empty local compiler cache; not cross-platform determinism.'})
        job.update(status='complete' if status == 'passed_exact' else 'failed', worker=None, completed_at=now())
        write_json(output/'job.json', job)
        print(json.dumps({'status': status, 'checks': len(checks), 'failed': [name for name, passed in checks.items() if not passed]}), flush=True)
        if status != 'passed_exact':
            raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--study', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    arguments = parser.parse_args()
    verify(arguments.study.resolve(), arguments.output.resolve())
