"""Persist the equal-budget full-dev BPB reference, without redoing generation."""
import gc
import os
from pathlib import Path
import signal
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, seed_all
from phase6_performance import identity, alive


def main():
    config_path = ROOT / 'configs/phase6/eos_complete_100m_full_bpb.json'
    config = read_json(config_path)
    plan_path = ROOT / config['main_plan']
    assert sha256(plan_path) == config['main_plan_sha256']
    plan = read_json(plan_path)
    run = ROOT / plan['output']
    main_job = read_json(run / 'job.json')
    assert main_job['status'] == 'complete' and not alive(main_job), 'Wait for main GPU job; do not duplicate'
    raw = read_json(run / 'review.json')
    assert raw['improvement_gate_passed'] and 'short20' in raw['full_evaluated_arms']
    job_path = run / 'full-bpb-reference-job.json'
    old = read_json(job_path) if job_path.exists() else {}
    if old and alive(old):
        raise RuntimeError('Full BPB reference job still live')
    arm = read_json(run / 'web/result.json')
    binding = {'config_sha256': sha256(config_path), 'plan_sha256': sha256(plan_path),
               'main_job_sha256': sha256(run / 'job.json'), 'web_checkpoint_sha256': arm['checkpoint_sha256'],
               'runner_sha256': sha256(Path(__file__)), 'implementation': implementation_hashes(),
               'readiness_sha256': sha256(ROOT / 'src/jmicro/readiness.py')}
    if old:
        assert old['binding'] == binding
        if old['status'] == 'complete':
            print('BPB reference already complete; not rerunning', flush=True)
            return
    prior = old.get('gpu_elapsed_seconds', 0)
    job = {'status': 'running', **identity(), 'binding': binding, 'started_at': old.get('started_at', now()),
           'stage': 'setup', 'gpu_elapsed_seconds': prior, 'main_GPU_seconds': main_job['gpu_elapsed_seconds'],
           'restart_command': 'bash scripts/run_eos_complete_full_bpb.sh', 'training_tokens': 0}
    stopped, started = [False], [None]
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]:
            raise InterruptedError('Stop requested; trained checkpoints remain preserved')
        if started[0] is not None and main_job['gpu_elapsed_seconds'] + prior + time.monotonic() - started[0] > plan['gpu_budget_seconds']:
            raise TimeoutError('Original cumulative2700-second GPU budget exhausted')
    def heartbeat(done=0, total=0):
        check()
        job.update(heartbeat_at=now(), completed_tasks=done, total_tasks=total)
        if started[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - started[0]
            job['peak_allocated_bytes'] = torch.cuda.max_memory_allocated()
            job['peak_reserved_bytes'] = torch.cuda.max_memory_reserved()
        atomic_json(job_path, job)
    def progress(done, total):
        check()
        if done == total or done % 1024 == 0:
            heartbeat(done, total)
    heartbeat()
    try:
        torch.set_num_threads(2)
        seed_all(42)
        torch.use_deterministic_algorithms(True)
        checkpoint = Path(arm['checkpoint'])
        assert sha256(checkpoint) == arm['checkpoint_sha256']
        dev = Shard(Path(plan['dev_shards']), 'dev')
        state = torch.load(checkpoint, map_location='cpu', weights_only=False)
        assert state['pilot_binding'] == raw['binding']
        with gpu_lock('cuda'):
            started[0] = time.monotonic()
            model = JMicroModel(state['model_config']).to('cuda')
            model.load_state_dict(state['model'], strict=True)
            job['stage'] = 'full-dev-BPB-reference'
            heartbeat()
            with sdpa_kernel([SDPBackend.MATH]):
                body = evaluate_batched(model, dev, 'cuda', 'bf16', batch=16, progress=progress)
            check()
            assert body['documents'] == 89416 and body['body_bytes'] == 164344743
            write_json(run / 'web-reference-full-dev.json', {'checkpoint': str(checkpoint),
                'checkpoint_sha256': arm['checkpoint_sha256'], 'binding': binding, 'body': body,
                'scope': 'Equal100M full-dev BPB reference only; Web screening failed Unicode and is not eligible for5B.',
                'generated_outputs': 0, 'training_tokens': 0, 'completed_at': now()})
            del model, state
            gc.collect()
            torch.cuda.empty_cache()
            job.update(status='complete', completed_at=now(), result=str(run / 'web-reference-full-dev.json'))
            print(f"Full BPB reference complete: {body['bpb']}", flush=True)
    except BaseException as exc:
        job.update(status='interrupted' if isinstance(exc, InterruptedError) else 'failed',
                   failure=f'{type(exc).__name__}: {exc}', finished_at=now())
        raise
    finally:
        if started[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - started[0]
        atomic_json(job_path, job)


if __name__ == '__main__':
    main()
