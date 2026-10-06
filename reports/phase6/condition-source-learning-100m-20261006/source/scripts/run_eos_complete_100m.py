"""Execute one frozen complete-unit100M EOS comparison, through uv in WSL."""
import argparse
import gc
import json
import os
from pathlib import Path
import re
import signal
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend

from jmicro.complete_units import JAPANESE
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, now, read_json, write_json, sha256
from jmicro.model import JMicroModel
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import SUPPRESS_IDS, Tokenizer
from jmicro.training import gpu_lock, implementation_hashes, isolated_evaluation, atomic_json
from phase6_performance import identity, alive
from prepare_complete_units import prepare_auxiliary, prepare_pool
from run_eos_short_pilot import exact_gate, train_arm, greedy80, rate, evaluate_checkpoint


def adoption_checks(control, treatment):
    a, b = control['greedy_rates'], treatment['greedy_rates']
    return {'EOS_at_least8_more': b['eos'] >= a['eos'] + 8,
            'repetition_no_worse': b['repetition'] <= a['repetition'],
            'no_empty_role_unicode': all(b[k] == 0 for k in ('empty', 'role_leak', 'unicode_failure')),
            'BPB_degradation_at_most1percent': treatment['body']['bpb'] <= control['body']['bpb'] * 1.01,
            'no_punctuation_only_stops': all(r['stop_reason'] != 'stop_id' or len(JAPANESE.findall(r['text'])) >= 2
                                           for r in treatment['generation']['outputs'])}


def screen_safe(evaluation, baseline):
    current = evaluation['greedy_rates']
    original = baseline['evaluation']['new_generation_rates']['greedy-suppressed1-seed42']
    return current['repetition'] < original['repetition'] + 8 and all(current[k] <= original[k] for k in ('empty', 'role_leak', 'unicode_failure'))


@torch.inference_mode()
def auxiliary_evaluation(model, tok, cases, heartbeat, check):
    rows = []
    with isolated_evaluation(model):
        for case in cases:
            check()
            with torch.autocast('cuda', dtype=torch.bfloat16):
                teacher = model(torch.tensor([[2, *case['body_ids']]], device='cuda')).logits[0, -1].float()
            assert bool(torch.isfinite(teacher).all())
            teacher_nll = float(-teacher.log_softmax(-1)[3])
            teacher_rank = int((teacher > teacher[3]).sum()) + 1
            ids, cache, ranks, nlls = [], None, [], []
            current = torch.tensor([[2, *case['prefix_ids']]], device='cuda')
            for _ in range(64):
                check()
                with torch.autocast('cuda', dtype=torch.bfloat16):
                    result = model(current, cache=cache, use_cache=True)
                cache = result.cache
                scores = result.logits[0, -1].clone()
                assert bool(torch.isfinite(scores).all())
                ranks.append(int((scores > scores[3]).sum()) + 1)
                nlls.append(float(-scores.float().log_softmax(-1)[3]))
                scores[list(SUPPRESS_IDS)] = -torch.inf
                token = int(scores.argmax())
                ids.append(token)
                if token == 3:
                    break
                current = torch.tensor([[token]], device='cuda')
            raw = tok.decode_bytes(ids)
            try:
                text, valid = raw.decode('utf-8'), True
            except UnicodeDecodeError:
                text, valid = raw.decode('utf-8', errors='replace'), False
            rows.append({'id': case['id'], 'prefix': case['prefix'], 'split': 'dev', 'decoding': 'greedy',
                         'suppressed': True, 'generated_ids': ids, 'text': text, 'valid_utf8': valid,
                         'role_leak': any(i in (4, 5, 6, 7) for i in ids), 'empty_response': not text.strip(),
                         'stop_reason': 'stop_id' if ids[-1] == 3 else 'max_new_tokens',
                         'repetition': bool(re.search(r'(.{2,}?)\1\1', text, flags=re.DOTALL)),
                         'generated_tokens': len(ids), 'punctuation_only_stop': ids[-1] == 3 and len(JAPANESE.findall(text)) < 2,
                         'true_end_eos_nll': teacher_nll, 'true_end_eos_rank': teacher_rank,
                         'trajectory_eos_rank_min': min(ranks), 'trajectory_eos_nll_min': min(nlls),
                         'reference_continuation': case['reference_continuation'], 'human_scores': None})
            if len(rows) % 8 == 0:
                heartbeat('auxiliary-generation', completed_cases=len(rows))
    return {'rates': rate(rows), 'outputs': rows, 'max_new_tokens': 64,
            'teacher_mean_eos_nll': sum(r['true_end_eos_nll'] for r in rows) / len(rows),
            'teacher_eos_argmax': sum(r['true_end_eos_rank'] == 1 for r in rows),
            'grammar_scoring': 'Human scores not supplied; generated text remains available for review'}


def screen(checkpoint, dev, tok, auxiliary, path, heartbeat, check):
    if path.exists():
        saved = read_json(path)
        assert saved['checkpoint_sha256'] == sha256(checkpoint)
        assert saved['auxiliary_sha256'] == sha256(path.parent / 'auxiliary-dev.json')
        return saved
    state = torch.load(checkpoint, map_location='cpu', weights_only=False)
    model = JMicroModel(state['model_config']).to('cuda')
    model.load_state_dict(state['model'], strict=True)
    def progress(done, total):
        check()
        heartbeat('dev256', completed_tasks=done, total_tasks=total)
    with sdpa_kernel([SDPBackend.MATH]):
        body = evaluate_batched(model, dev, 'cuda', 'bf16', limit=256, batch=16, progress=progress)
        fixed = greedy80(model, tok, heartbeat, check)
        aux = auxiliary_evaluation(model, tok, auxiliary['cases'], heartbeat, check)
    result = {'checkpoint': str(checkpoint), 'checkpoint_sha256': sha256(checkpoint), 'body': body,
              'generation': {'max_new_tokens': 64, 'outputs': fixed, 'suite_sha256': sha256(ROOT / 'eval/base.jsonl')},
              'greedy_rates': rate(fixed), 'auxiliary': aux,
              'auxiliary_sha256': sha256(path.parent / 'auxiliary-dev.json'), 'completed_at': now()}
    write_json(path, result)
    del model, state
    gc.collect()
    torch.cuda.empty_cache()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT / 'configs/phase6/eos_complete_100m.json')
    parser.add_argument('--prepare-only', action='store_true')
    args = parser.parse_args()
    torch.set_num_threads(2)
    plan = read_json(args.plan)
    output = ROOT / plan['output']
    output.mkdir(parents=True, exist_ok=True)
    old = read_json(output / 'job.json') if (output / 'job.json').exists() else {}
    if old and alive(old):
        raise RuntimeError('Identified job still live; do not duplicate')
    binding = {'plan_sha256': sha256(args.plan), 'parent': plan['parent'],
               'module_sha256': sha256(ROOT / 'src/jmicro/eos_pilot.py'),
               'runner_sha256': sha256(Path(__file__)), 'implementation': implementation_hashes(),
               'new_source': {p: sha256(ROOT / p) for p in ('src/jmicro/complete_units.py',
                              'scripts/prepare_complete_units.py', 'scripts/run_eos_short_pilot.py',
                              'src/jmicro/readiness.py')}}
    if old:
        assert old['binding'] == binding, 'Source changed: preserve old run and do not silently resume'
        if old['status'] == 'complete':
            print('100M comparison already complete; not rerunning', flush=True)
            return
    job = {'status': 'running', **identity(), 'started_at': old.get('started_at', now()), 'binding': binding,
           'restart_command': 'bash scripts/run_eos_complete_100m.sh', 'stage': 'setup',
           'gpu_elapsed_seconds': old.get('gpu_elapsed_seconds', 0)}
    stopped, gpu_start = [False], [None]
    prior_gpu = job['gpu_elapsed_seconds']
    signal.signal(signal.SIGINT, lambda *_: stopped.__setitem__(0, True))
    signal.signal(signal.SIGTERM, lambda *_: stopped.__setitem__(0, True))
    def check():
        if stopped[0]:
            raise InterruptedError('Stop requested; completed update checkpoint preserved')
        if gpu_start[0] is not None and prior_gpu + time.monotonic() - gpu_start[0] > plan['gpu_budget_seconds']:
            raise TimeoutError('Cumulative GPU budget exhausted; do not reset the budget')
    def heartbeat(stage, **values):
        job.update(stage=stage, heartbeat_at=now(), **values)
        if gpu_start[0] is not None:
            job['gpu_elapsed_seconds'] = prior_gpu + time.monotonic() - gpu_start[0]
        atomic_json(output / 'job.json', job)
    heartbeat('setup')
    try:
        assert sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256']
        assert sha256(ROOT / 'eval/base.jsonl') == plan['suite_sha256']
        accepted = read_json(ROOT / 'reports/phase6/corpus_10b_loader_ready.json')
        assert accepted['status'] == 'passed_actual_training_loader' and accepted['shard_manifest_sha256'] == plan['web_manifest_sha256']
        tests = {k: 0 for k in ('tests', 'failures', 'errors', 'skipped')}
        for suite in ET.parse(output / 'tests.xml').getroot().iter('testsuite'):
            for key in tests:
                tests[key] += int(suite.attrib.get(key, 0))
        assert tests['tests'] > 0 and not any(tests[k] for k in ('failures', 'errors', 'skipped'))
        tok, dev = Tokenizer(ROOT / plan['tokenizer']), Shard(Path(plan['dev_shards']), 'dev')
        auxiliary = prepare_auxiliary(plan, dev, tok, output)
        heartbeat('complete-unit-pool')
        ready = prepare_pool(plan, tok, auxiliary, heartbeat, check)
        if args.prepare_only:
            job.update(status='prepared', completed_at=now(), pool_manifest_sha256=ready['manifest_sha256'],
                       auxiliary_sha256=sha256(output / 'auxiliary-dev.json'))
            print(json.dumps({'status': 'prepared', 'pool': ready}, ensure_ascii=False), flush=True)
            return
        content = read_json(output / 'content-review.json')
        assert content['passed'] and content['pool_manifest_sha256'] == ready['manifest_sha256']
        assert content['auxiliary_sha256'] == sha256(output / 'auxiliary-dev.json')
        web = TrainView(plan['web_shards'], plan['web_manifest_sha256'])
        short = TrainView(plan['short_pool'], ready['manifest_sha256'], check_stream=True)
        parent_path = Path(plan['parent']['path'])
        assert sha256(parent_path) == plan['parent']['sha256']
        parent_stat = (parent_path.stat().st_size, parent_path.stat().st_mtime_ns)
        parent = torch.load(parent_path, map_location='cpu', weights_only=False)
        assert parent['tokens'] == plan['parent']['tokens_seen'] and parent['update'] == plan['parent']['update']
        assert (parent['spec']['batch'], parent['spec']['context'], parent['spec']['accumulation'], parent['spec']['lr']) == (32, 1024, 1, .002)
        trainer_binding = {**binding, 'short_manifest_sha256': ready['manifest_sha256'],
                           'auxiliary_sha256': sha256(output / 'auxiliary-dev.json')}
        with gpu_lock('cuda'):
            gpu_start[0] = time.monotonic()
            heartbeat('resume-gate')
            gate = exact_gate(parent, web, short, trainer_binding, output, check)
            baseline_path = output / 'generation-baseline-check.json'
            if not baseline_path.exists():
                model = JMicroModel(parent['model_config']).to('cuda')
                model.load_state_dict(parent['model'], strict=True)
                with sdpa_kernel([SDPBackend.MATH]):
                    reproduced = greedy80(model, tok, heartbeat, check, limit=8)
                saved = read_json(ROOT / 'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/generation.json')['generation']['outputs']
                ids_checks = {r['id']: r['generated_ids'] == next(s['generated_ids'] for s in saved if s['id'] == r['id'] and s['decoding'] == 'greedy' and s['suppressed']) for r in reproduced}
                assert all(ids_checks.values())
                write_json(baseline_path, {'binding': trainer_binding, 'checks': ids_checks, 'passed': True})
                del model
                gc.collect()
                torch.cuda.empty_cache()
            else:
                assert read_json(baseline_path)['passed'] and read_json(baseline_path)['binding'] == trainer_binding
            arms, evaluations, full = {}, {}, {}
            for arm in ('web', 'short20'):
                heartbeat(f'{arm}-training')
                arms[arm] = train_arm(arm, parent, web, short, plan, trainer_binding, output, heartbeat, check)
                heartbeat(f'{arm}-screening')
                evaluations[arm] = screen(Path(arms[arm]['checkpoint']), dev, tok, auxiliary,
                                          output / f'{arm}-evaluation.json', heartbeat, check)
            checks = adoption_checks(evaluations['web'], evaluations['short20'])
            promising = all(checks.values())
            base2b = read_json(ROOT / 'reports/phase6/base_2b_10b_data_review.json')
            safe_web = screen_safe(evaluations['web'], base2b)
            for arm in ('web', 'short20'):
                if (arm == 'web' and safe_web) or (arm == 'short20' and promising):
                    heartbeat(f'{arm}-full-evaluation')
                    full[arm] = evaluate_checkpoint(Path(arms[arm]['checkpoint']), dev, tok,
                        output / f'{arm}-full-evaluation.json', heartbeat, check, full=True)
                    check()
            full_checks = {}
            if promising:
                if 'web' not in full:
                    # A candidate is not adopted without its equal-budget full control.
                    full_checks['full_control_available'] = False
                else:
                    full_checks['BPB_within1percent_full_control'] = full['short20']['body']['bpb'] <= full['web']['body']['bpb'] * 1.01
                full_rows = [r for r in full['short20']['generation']['outputs'] if r['decoding'] == 'greedy' and r['suppressed']]
                full_checks['all80_screen_IDs_match'] = [r['generated_ids'] for r in full_rows] == [r['generated_ids'] for r in evaluations['short20']['generation']['outputs']]
                original_rows = read_json(ROOT / 'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/generation.json')['generation']['outputs']
                full_checks['no_new_empty_role_unicode_vs2B'] = all(rate(full['short20']['generation']['outputs'])[k] <= rate(original_rows)[k] for k in ('empty', 'role_leak', 'unicode_failure'))
            adopted = promising and all(full_checks.values())
            growth_checks = {}
            if 'web' in full:
                original_rows = read_json(ROOT / 'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/generation.json')['generation']['outputs']
                growth_checks = {'full_BPB_no_major_regression': full['web']['body']['bpb'] <= plan['base2B_full_bpb'] + .001,
                    'fixed_repetition_not8_worse': full['web']['greedy_rates']['repetition'] < 68,
                    'no_new_empty_role_unicode': all(rate(full['web']['generation']['outputs'])[k] <= rate(original_rows)[k] for k in ('empty', 'role_leak', 'unicode_failure'))}
            assert (parent_path.stat().st_size, parent_path.stat().st_mtime_ns) == parent_stat
            heartbeat('comparison-finished')
            result = {'status': 'completed_two_arm_100M_comparison_pending_review', 'completed_at': now(),
                      'plan': str(args.plan), 'binding': trainer_binding, 'short_pool': ready, 'tests': tests,
                      'resume_gate': gate, 'arms': arms, 'improvement_checks': checks,
                      'improvement_gate_passed': promising, 'full_adoption_checks': full_checks,
                      'short_mixture_adopted': adopted, 'full_evaluated_arms': list(full),
                      'base5B_go_no_go': growth_checks, 'base5B_eligible': bool(growth_checks) and all(growth_checks.values()),
                      'scientific_training_input_tokens': sum(a['additional_input_tokens'] for a in arms.values()),
                      'verification_training_input_tokens': gate['input_tokens'],
                      'gpu_elapsed_seconds': job['gpu_elapsed_seconds'], 'test_split_used': False,
                      'quality_targets_achieved': False, 'parent_stat_unchanged': True,
                      'decision': 'Short mixture passes automatic comparison gates; quality targets still unmet' if adopted else 'Short mixture not adopted; preserve the failed stopping result',
                      'stop_boundary': 'Report/commit after this trial. No5B/Chat/sweeps launched.'}
            write_json(output / 'review.json', result)
            job.update(status='complete', completed_at=now(), result=str(output / 'review.json'))
            print(json.dumps({'status': job['status'], 'checks': checks, 'adopted': adopted, 'base5B_eligible': result['base5B_eligible']}), flush=True)
    except BaseException as exc:
        job.update(status='interrupted' if isinstance(exc, InterruptedError) else 'failed',
                   failure=f'{type(exc).__name__}: {exc}', finished_at=now())
        raise
    finally:
        if gpu_start[0] is not None:
            job['gpu_elapsed_seconds'] = prior_gpu + time.monotonic() - gpu_start[0]
        atomic_json(output / 'job.json', job)


if __name__ == '__main__':
    main()
