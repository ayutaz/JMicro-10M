"""Finish the fixed experiment using preserved checkpoints and bounded cached-memory evaluation."""
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
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, seed_all, generate_suite
from phase6_performance import identity, alive
from run_eos_complete_100m import adoption_checks, rate


def main():
    config_path = ROOT / 'configs/phase6/eos_complete_evaluation_recovery.json'
    config = read_json(config_path)
    plan_path = ROOT / config['main_plan']
    assert sha256(plan_path) == config['main_plan_sha256']
    plan = read_json(plan_path)
    run = ROOT / plan['output']
    original = read_json(run / 'job.json')
    assert original['status'] in ('interrupted', 'failed') and not alive(original)
    assert original['binding']['plan_sha256'] == sha256(plan_path)
    binding = {'config_sha256': sha256(config_path), 'main_plan_sha256': sha256(plan_path),
               'main_job_sha256': sha256(run / 'job.json'), 'runner_sha256': sha256(Path(__file__)),
               'memory_policy_sha256': sha256(ROOT / 'src/jmicro/evaluation_memory.py'),
               'implementation': implementation_hashes(), 'readiness_sha256': sha256(ROOT / 'src/jmicro/readiness.py')}
    path = run / 'evaluation-recovery-job.json'
    old = read_json(path) if path.exists() else {}
    if old:
        assert old['binding'] == binding and not alive(old)
        if old['status'] == 'complete':
            print('Recovery evaluation already complete', flush=True)
            return
    prior, start, stopped = old.get('gpu_elapsed_seconds', 0), [None], [False]
    job = {'status': 'running', **identity(), 'started_at': old.get('started_at', now()), 'binding': binding,
           'stage': 'setup', 'gpu_elapsed_seconds': prior, 'preserved_main_GPU_seconds': original['gpu_elapsed_seconds'],
           'recovery_budget_seconds': config['GPU_budget_seconds'], 'training_tokens': 0,
           'restart_command': 'bash scripts/run_eos_complete_evaluation_recovery.sh'}
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]:
            raise InterruptedError('Recovery evaluation interrupted; trained checkpoints unchanged')
        if start[0] is not None and prior + time.monotonic() - start[0] > config['GPU_budget_seconds']:
            raise TimeoutError('Bounded recovery1200-second budget exhausted; preserve results')
    def heartbeat(stage, **values):
        check()
        job.update(stage=stage, heartbeat_at=now(), **values)
        if start[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - start[0]
        atomic_json(path, job)
    heartbeat('setup')
    try:
        torch.set_num_threads(2)
        seed_all(42)
        torch.use_deterministic_algorithms(True)
        dev, tok = Shard(Path(plan['dev_shards']), 'dev'), Tokenizer(ROOT / plan['tokenizer'])
        arms = {arm: read_json(run / arm / 'result.json') for arm in ('web', 'short20')}
        screens = {arm: read_json(run / f'{arm}-evaluation.json') for arm in arms}
        checks = adoption_checks(screens['web'], screens['short20'])
        assert all(checks.values())
        with gpu_lock('cuda'):
            start[0] = time.monotonic()
            for arm in ('short20', 'web'):
                destination = run / ('short20-full-evaluation.json' if arm == 'short20' else 'web-reference-full-dev.json')
                if destination.exists():
                    saved = read_json(destination)
                    assert saved['checkpoint_sha256'] == arms[arm]['checkpoint_sha256']
                    continue
                checkpoint = Path(arms[arm]['checkpoint'])
                assert sha256(checkpoint) == arms[arm]['checkpoint_sha256']
                state = torch.load(checkpoint, map_location='cpu', weights_only=False)
                model = JMicroModel(state['model_config']).to('cuda')
                model.load_state_dict(state['model'], strict=True)
                memory = bound_evaluation_cache(model)
                heartbeat(f'{arm}-full-dev')
                def progress(done, total):
                    check()
                    if done == total or done % 1024 == 0:
                        heartbeat(f'{arm}-full-dev', completed_tasks=done, total_tasks=total, memory=memory)
                with sdpa_kernel([SDPBackend.MATH]):
                    body = evaluate_batched(model, dev, 'cuda', 'bf16', batch=16, progress=progress)
                    assert body['documents'] == 89416 and body['body_bytes'] == 164344743
                    heartbeat(f'{arm}-full-generation' if arm == 'short20' else f'{arm}-BPB-reference')
                    generation = generate_suite(model, tok, 'cuda', 'bf16', limit=80, max_new=64, sampling=True) if arm == 'short20' else None
                check()
                result = {'checkpoint': str(checkpoint), 'checkpoint_sha256': arms[arm]['checkpoint_sha256'],
                          'full': True, 'body': body, 'memory': memory, 'recovery_binding': binding,
                          'training_tokens': 0, 'completed_at': now()}
                if generation is not None:
                    result.update(generation=generation, greedy_rates=rate([r for r in generation['outputs'] if r['decoding'] == 'greedy' and r['suppressed']]))
                else:
                    result.update(generated_outputs=0, scope='Same100M full-dev BPB reference only; Web Unicode regression still blocks5B.')
                write_json(destination, result)
                del model, state
                gc.collect()
                torch.cuda.empty_cache()
            heartbeat('finished')
            trainer_binding = arms['web']['binding']
            candidate = read_json(run / 'short20-full-evaluation.json')
            reference = read_json(run / 'web-reference-full-dev.json')
            fixed = [r for r in candidate['generation']['outputs'] if r['decoding'] == 'greedy' and r['suppressed']]
            original_rows = read_json(ROOT / 'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/generation.json')['generation']['outputs']
            full_checks = {'BPB_within1percent_full_control': candidate['body']['bpb'] <= reference['body']['bpb'] * 1.01,
                           'all80_screen_IDs_match': [r['generated_ids'] for r in fixed] == [r['generated_ids'] for r in screens['short20']['generation']['outputs']],
                           'no_new_empty_role_unicode_vs2B': all(rate(candidate['generation']['outputs'])[k] <= rate(original_rows)[k] for k in ('empty', 'role_leak', 'unicode_failure'))}
            content = read_json(run / 'generation-content-review.json')
            summary = {'status': 'completed_two_arm100M_with_separate_evaluation_recovery', 'completed_at': now(),
                       'plan': str(plan_path), 'binding': trainer_binding, 'arms': arms,
                       'improvement_checks': checks, 'improvement_gate_passed': True,
                       'full_adoption_checks': full_checks, 'short_mixture_adopted': all(full_checks.values()) and content['usable_generation_accepted'],
                       'full_evaluated_arms': ['short20'], 'base5B_go_no_go': {}, 'base5B_eligible': False,
                       'scientific_training_input_tokens': sum(a['additional_input_tokens'] for a in arms.values()),
                       'verification_training_input_tokens': read_json(run / 'resume-gate.json')['input_tokens'],
                       'test_split_used': False, 'quality_targets_achieved': False,
                       'decision': 'Natural EOS improvement24/80; generation content still unusable, preserve diagnostic branch.',
                       'evaluation_recovery': {'config': str(config_path), 'binding': binding, 'main_job_terminal_status': original['status'],
                                               'original_GPU_budget_seconds': plan['gpu_budget_seconds'], 'recovery_GPU_budget_seconds': config['GPU_budget_seconds']},
                       'note': 'Original interrupted main job/budget/history remain unchanged; reviewer uses the now-complete paired BPB reference and content review.'}
            write_json(run / 'review-recovered.json', summary)
            job.update(status='complete', completed_at=now(), result=str(run / 'review-recovered.json'))
            print('Recovered full evaluation and equal-budget BPB reference complete', flush=True)
    except BaseException as exc:
        job.update(status='interrupted' if isinstance(exc, InterruptedError) else 'failed', failure=f'{type(exc).__name__}: {exc}', finished_at=now())
        raise
    finally:
        if start[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - start[0]
        atomic_json(path, job)


if __name__ == '__main__':
    main()
