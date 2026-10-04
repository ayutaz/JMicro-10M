"""One bounded low-LR100M pair and eligible evaluation, using existing data only."""
import argparse
import gc
import json
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
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.eos_pilot import TrainView
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.experiment import ROOT, now, read_json, write_json, sha256
from jmicro.low_lr_pilot import LowLRPilotTrainer
from jmicro.model import JMicroModel
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, seed_all, generate_suite
from phase6_performance import identity, alive
import run_eos_short_pilot as pilot
from run_eos_complete_100m import adoption_checks, screen_safe, auxiliary_evaluation


def tests_summary(path):
    result = {k: 0 for k in ('tests', 'failures', 'errors', 'skipped')}
    for suite in ET.parse(path).getroot().iter('testsuite'):
        for key in result:
            result[key] += int(suite.attrib.get(key, 0))
    assert result['tests'] and not any(result[k] for k in ('failures', 'errors', 'skipped'))
    return result


def evaluate(checkpoint, dev, tok, auxiliary, destination, heartbeat, check, full=False, generation=True):
    digest = sha256(checkpoint)
    if destination.exists():
        result = read_json(destination)
        assert result['checkpoint_sha256'] == digest and result['full'] == full
        return result
    state = torch.load(checkpoint, map_location='cpu', weights_only=False)
    model = JMicroModel(state['model_config']).to('cuda')
    model.load_state_dict(state['model'], strict=True)
    model.eval()
    memory = bound_evaluation_cache(model)
    def progress(done, total):
        check()
        if done == total or done % 1024 == 0:
            heartbeat(destination.stem, completed_tasks=done, total_tasks=total, memory=memory)
    with sdpa_kernel([SDPBackend.MATH]):
        body = evaluate_batched(model, dev, 'cuda', 'bf16', limit=None if full else 256, batch=16, progress=progress)
        result = {'checkpoint': str(checkpoint), 'checkpoint_sha256': digest, 'body': body,
                  'full': full, 'memory': memory, 'completed_at': now()}
        if generation:
            heartbeat(destination.stem + '-generation')
            if full:
                # Original generate_suite remains unchanged; fork RNG isolation keeps sampling reproducible.
                generated = generate_suite(model, tok, 'cuda', 'bf16', limit=80, max_new=64, sampling=True)
            else:
                generated = {'outputs': pilot.greedy80(model, tok, heartbeat, check), 'max_new_tokens': 64,
                             'suite_sha256': sha256(ROOT / 'eval/base.jsonl')}
            result.update(generation=generated, greedy_rates=pilot.rate([
                r for r in generated['outputs'] if r['decoding'] == 'greedy' and r['suppressed']]))
            if not full:
                result['auxiliary'] = auxiliary_evaluation(model, tok, auxiliary['cases'], heartbeat, check)
                result['auxiliary_sha256'] = sha256(destination.parent / 'auxiliary-dev.json')
    check()
    write_json(destination, result)
    del model, state
    gc.collect()
    torch.cuda.empty_cache()
    return result


def analyse_existing(plan, run, dev, tok, heartbeat, check):
    destination = run / 'historical-analysis.json'
    if destination.exists():
        return read_json(destination)
    old_run = ROOT / plan['previous_run']
    rows = [json.loads(line) for line in (old_run / 'web/metrics.jsonl').read_text().splitlines()]
    previous = read_json(ROOT / 'reports/phase6/eos_complete_100m_review.json')
    points = []
    for local in plan['diagnostic_updates']:
        path = old_run / 'web' / f"checkpoint-{plan['parent']['update'] + local:08d}.pt"
        assert sha256(path) == plan['diagnostic_checkpoint_sha256'][str(local)]
        measured = evaluate(path, dev, tok, None, run / f'historical-dev-{local}.json', heartbeat, check, generation=False)
        points.append({'local_updates': local, 'additional_input_tokens': local * 32768,
                       'checkpoint': str(path), 'sha256': measured['checkpoint_sha256'],
                       'dev256_bpb': measured['body']['bpb']})
    points.append({'local_updates': 3052, 'additional_input_tokens': plan['tokens_per_arm'],
                   'dev256_bpb': previous['arms']['web']['dev256_bpb'], 'reused_completed_evaluation': True})
    windows = []
    for start, end in ((0, 25), (25, 200), (200, 1600), (1600, 2900), (2900, 3052)):
        selected = rows[start:end]
        windows.append({'local_update_start': start + 1, 'local_update_end': end,
                        'median_train_loss': statistics.median(r['loss'] for r in selected),
                        'first_lr': selected[0]['lr'], 'last_lr': selected[-1]['lr']})
    result = {'status': 'completed_existing_logs_and_three_saved_checkpoint_probes', 'training_tokens': 0,
              'train_log_sha256': sha256(old_run / 'web/metrics.jsonl'), 'historical_windows': windows,
              'historical_dev256_points': points, 'parent_actual_lr': plan['peak_lr'],
              'previous_first_update_lr': rows[0]['lr'], 'restart_multiplier': rows[0]['lr'] / plan['peak_lr'],
              'previous_full_bpb': {arm: previous['full_control_BPB_reference']['bpb'] if arm == 'web' else previous['full_evaluations'][arm]['bpb'] for arm in ('web', 'short20')},
              'parent_full_bpb': plan['base2B_full_bpb'],
              'limits': ['Train loss uses different batches; do not treat it as heldout quality.',
                         'Three checkpoint probes bound the observed timeline; they do not identify the exact first bad update.',
                         'High LR is a hypothesis until the matching low-LR pair is compared.'], 'completed_at': now()}
    write_json(destination, result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT / 'configs/phase6/eos_low_lr_100m.json')
    args = parser.parse_args()
    plan = read_json(args.plan)
    run = ROOT / plan['output']
    run.mkdir(parents=True, exist_ok=True)
    sources = ('src/jmicro/low_lr_pilot.py', 'src/jmicro/eos_pilot.py', 'src/jmicro/evaluation_memory.py',
               'scripts/run_eos_short_pilot.py', 'scripts/run_eos_complete_100m.py', 'src/jmicro/readiness.py')
    binding = {'plan_sha256': sha256(args.plan), 'parent': plan['parent'], 'peak_lr': plan['peak_lr'],
               'short_manifest_sha256': plan['short_manifest_sha256'], 'auxiliary_sha256': plan['auxiliary_sha256'],
               'module_sha256': sha256(ROOT / 'src/jmicro/eos_pilot.py'), 'runner_sha256': sha256(Path(__file__)),
               'implementation': implementation_hashes(), 'new_source': {p: sha256(ROOT / p) for p in sources}}
    path = run / 'job.json'
    old = read_json(path) if path.exists() else {}
    if old:
        assert not alive(old), 'Actual job is live; do not duplicate'
        assert old['binding'] == binding, 'Source/config differs; do not silently resume'
        if old['status'] == 'complete':
            print('Low-LR comparison already complete; not rerunning', flush=True)
            return
    prior, start, stopped = old.get('gpu_elapsed_seconds', 0), [None], [False]
    job = {'status': 'running', **identity(), 'binding': binding, 'started_at': old.get('started_at', now()),
           'stage': 'setup', 'gpu_elapsed_seconds': prior, 'restart_command': 'bash scripts/run_eos_low_lr.sh'}
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]:
            raise InterruptedError('Stop requested; completed-update checkpoint preserved')
        if start[0] is not None and prior + time.monotonic() - start[0] > plan['gpu_budget_seconds']:
            raise TimeoutError('Cumulative frozen GPU budget exhausted; do not reset')
    def heartbeat(stage, **values):
        check()
        job.update(stage=stage, heartbeat_at=now(), **values)
        if start[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - start[0]
        atomic_json(path, job)
    try:
        torch.set_num_threads(2)
        seed_all(42)
        torch.use_deterministic_algorithms(True)
        tests = tests_summary(run / 'tests.xml')
        old_run = ROOT / plan['previous_run']
        assert sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256']
        assert sha256(ROOT / 'eval/base.jsonl') == plan['suite_sha256']
        for name in ('auxiliary-dev.json', 'content-review.json'):
            target = run / name
            if not target.exists():
                shutil.copyfile(old_run / name, target)
            assert sha256(target) == sha256(old_run / name)
        auxiliary = read_json(run / 'auxiliary-dev.json')
        ready = read_json(Path(plan['short_pool']) / 'ready.json')
        assert ready['auxiliary_sha256'] == sha256(run / 'auxiliary-dev.json')
        assert ready['manifest_sha256'] == plan['short_manifest_sha256']
        assert read_json(run / 'content-review.json')['passed']
        accepted = read_json(ROOT / 'reports/phase6/corpus_10b_loader_ready.json')
        assert accepted['status'] == 'passed_actual_training_loader' and accepted['shard_manifest_sha256'] == plan['web_manifest_sha256']
        web = TrainView(plan['web_shards'], plan['web_manifest_sha256'])
        short = TrainView(plan['short_pool'], ready['manifest_sha256'], check_stream=True)
        dev, tok = Shard(Path(plan['dev_shards']), 'dev'), Tokenizer(ROOT / plan['tokenizer'])
        parent_path = Path(plan['parent']['path'])
        assert sha256(parent_path) == plan['parent']['sha256']
        parent_stat = (parent_path.stat().st_size, parent_path.stat().st_mtime_ns)
        parent = torch.load(parent_path, map_location='cpu', weights_only=False)
        assert parent['update'] == plan['parent']['update'] and parent['tokens'] == plan['parent']['tokens_seen']
        assert all(abs(g['lr'] - plan['peak_lr']) < .000001 for g in parent['optimizer']['param_groups'])
        assert binding['auxiliary_sha256'] == sha256(run / 'auxiliary-dev.json')
        # The same explicit trainer factory drives the CUDA gate and both scientific arms.
        pilot.PilotTrainer = LowLRPilotTrainer
        with gpu_lock('cuda'):
            start[0] = time.monotonic()
            heartbeat('historical-analysis')
            historical = analyse_existing(plan, run, dev, tok, heartbeat, check)
            heartbeat('low-lr-resume-gate')
            gate = pilot.exact_gate(parent, web, short, binding, run, check)
            arms, screens, full = {}, {}, {}
            for arm in ('web', 'short20'):
                heartbeat(arm + '-training')
                arms[arm] = pilot.train_arm(arm, parent, web, short, plan, binding, run, heartbeat, check)
                heartbeat(arm + '-screening')
                screens[arm] = evaluate(Path(arms[arm]['checkpoint']), dev, tok, auxiliary,
                                       run / f'{arm}-evaluation.json', heartbeat, check)
            mixture = adoption_checks(screens['web'], screens['short20'])
            promising = all(mixture.values())
            baseline = read_json(ROOT / 'reports/phase6/base_2b_10b_data_review.json')
            safe_web = screen_safe(screens['web'], baseline)
            # A short candidate always receives an equal-budget full body reference, even if Web generation is ineligible.
            for arm in ('web', 'short20'):
                eligible = safe_web or promising if arm == 'web' else promising
                if eligible:
                    full[arm] = evaluate(Path(arms[arm]['checkpoint']), dev, tok, auxiliary,
                                         run / f'{arm}-full-evaluation.json', heartbeat, check, full=True,
                                         generation=safe_web if arm == 'web' else True)
            original_rows = read_json(ROOT / 'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/generation.json')['generation']['outputs']
            full_checks, growth = {}, {}
            if promising:
                fixed = [r for r in full['short20']['generation']['outputs'] if r['decoding'] == 'greedy' and r['suppressed']]
                full_checks = {'BPB_within1percent_full_control': full['short20']['body']['bpb'] <= full['web']['body']['bpb'] * 1.01,
                               'all80_screen_IDs_match': [r['generated_ids'] for r in fixed] == [r['generated_ids'] for r in screens['short20']['generation']['outputs']],
                               'no_new_empty_role_unicode_vs2B': all(pilot.rate(full['short20']['generation']['outputs'])[k] <= pilot.rate(original_rows)[k] for k in ('empty', 'role_leak', 'unicode_failure'))}
            if safe_web:
                fixed = [r for r in full['web']['generation']['outputs'] if r['decoding'] == 'greedy' and r['suppressed']]
                growth = {'full_BPB_no_major_regression': full['web']['body']['bpb'] <= plan['base2B_full_bpb'] + .001,
                          'fixed_repetition_not8_worse': screens['web']['greedy_rates']['repetition'] < 68,
                          'no_new_empty_role_unicode': all(pilot.rate(full['web']['generation']['outputs'])[k] <= pilot.rate(original_rows)[k] for k in ('empty', 'role_leak', 'unicode_failure')),
                          'all80_screen_IDs_match': [r['generated_ids'] for r in fixed] == [r['generated_ids'] for r in screens['web']['generation']['outputs']]}
            assert (parent_path.stat().st_size, parent_path.stat().st_mtime_ns) == parent_stat
            heartbeat('finished')
            result = {'status': 'completed_low_lr_pair_pending_offline_and_content_review', 'binding': binding,
                      'historical_analysis': historical, 'tests': tests, 'resume_gate': gate, 'arms': arms,
                      'improvement_checks': mixture, 'improvement_gate_passed': promising,
                      'full_adoption_checks': full_checks, 'automatic_full_gate_passed': promising and all(full_checks.values()),
                      'full_evaluated_arms': list(full), 'web_full_generation_eligible': safe_web,
                      'base5B_go_no_go': growth, 'base5B_eligible': bool(growth) and all(growth.values()),
                      'scientific_training_input_tokens': sum(a['additional_input_tokens'] for a in arms.values()),
                      'verification_training_input_tokens': gate['input_tokens'], 'quality_targets_achieved': False,
                      'test_split_used': False, 'completed_at': now(), 'stop_boundary': 'Report/commit, stop before5B/Chat/sweeps.'}
            write_json(run / 'result.json', result)
            job.update(status='complete', completed_at=now(), result=str(run / 'result.json'))
            print(json.dumps({'status': 'complete', 'mixture': mixture, 'growth': growth}), flush=True)
    except BaseException as exc:
        job.update(status='interrupted' if isinstance(exc, InterruptedError) else 'failed', failure=f'{type(exc).__name__}: {exc}', finished_at=now())
        raise
    finally:
        if start[0] is not None:
            job['gpu_elapsed_seconds'] = prior + time.monotonic() - start[0]
        atomic_json(path, job)


if __name__ == '__main__':
    main()
