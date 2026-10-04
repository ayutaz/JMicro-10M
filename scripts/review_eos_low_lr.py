"""Verify the completed low-LR experiment without extra GPU inference."""
import json
import math
from pathlib import Path
import statistics
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes
from phase6_performance import alive
from run_eos_short_pilot import rate
from run_eos_complete_100m import adoption_checks, screen_safe
from run_eos_low_lr import tests_summary


def main():
    torch.set_num_threads(2)
    plan_path = ROOT / 'configs/phase6/eos_low_lr_100m.json'
    plan = read_json(plan_path)
    run, old_run = ROOT / plan['output'], ROOT / plan['previous_run']
    job, raw = read_json(run / 'job.json'), read_json(run / 'result.json')
    old = read_json(ROOT / 'reports/phase6/eos_complete_100m_review.json')
    checks = {}
    def require(name, value):
        checks[name] = bool(value)
        if not value:
            raise AssertionError(name)
    require('actual_process_exited_complete', job['status'] == 'complete' and not alive(job))
    binding = job['binding']
    require('frozen_plan_runner', binding == raw['binding'] and binding['plan_sha256'] == sha256(plan_path) and
            binding['runner_sha256'] == sha256(ROOT / 'scripts/run_eos_low_lr.py'))
    require('unchanged_core', binding['implementation'] == implementation_hashes())
    require('actual_tokenizer_and_fixed_suite_frozen', sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256'] and
            sha256(ROOT / 'eval/base.jsonl') == plan['suite_sha256'])
    for path, digest in binding['new_source'].items():
        require('source_' + path, sha256(ROOT / path) == digest)
    require('cumulative_GPU_budget', job['gpu_elapsed_seconds'] <= plan['gpu_budget_seconds'])
    tests = tests_summary(run / 'tests.xml')
    require('targeted12_tests', tests['tests'] == 12)
    parent_path = Path(plan['parent']['path'])
    require('original2B_parent_sha', sha256(parent_path) == plan['parent']['sha256'])
    parent = torch.load(parent_path, map_location='cpu', weights_only=False)
    require('parent_update_tokens_actual_lr', parent['update'] == 61036 and parent['tokens'] == 2000027648 and
            all(abs(g['lr'] - plan['peak_lr']) < .000001 for g in parent['optimizer']['param_groups']))
    gate = read_json(run / 'resume-gate.json')
    require('CUDA_continuous_vs_resumed_all_state', gate['passed'] and all(gate['checks'].values()) and
            gate['binding'] == binding and gate['GPU_optimizer_updates'] == 8 and gate['input_tokens'] == 262144)
    require('CUDA_gate_used_low_LR', all(0 < r['lr'] <= plan['peak_lr'] for h in gate['histories'] for r in h))
    require('auxiliary_exact_reuse', sha256(run / 'auxiliary-dev.json') == sha256(old_run / 'auxiliary-dev.json') == plan['auxiliary_sha256'])
    ready = read_json(Path(plan['short_pool']) / 'ready.json')
    require('same_accepted_train_pool', ready['manifest_sha256'] == binding['short_manifest_sha256'] == sha256(Path(plan['short_pool']) / 'manifest.json') == old['short_pool']['manifest_sha256'])
    require('pretraining_content_exact_reuse', sha256(run / 'content-review.json') == sha256(old_run / 'content-review.json') and read_json(run / 'content-review.json')['passed'])
    historical = read_json(run / 'historical-analysis.json')
    require('historical_analysis_zero_learning', historical['training_tokens'] == 0 and historical['restart_multiplier'] == 10)
    parent_reference = read_json(run / 'historical-parent-reference.json')
    saved_parent_full = read_json(Path(parent_reference['source']))
    parent_rows = saved_parent_full['body']['rows'][:256]
    require('parent_subset_reference_uses_same2B_saved_evaluation', parent_reference['source_sha256'] == sha256(Path(parent_reference['source'])) and
            parent_reference['checkpoint_sha256'] == plan['parent']['sha256'] and parent_reference['documents'] == 256 and
            math.isclose(parent_reference['bpb'], sum(r['body_nll'] for r in parent_rows) / math.log(2) / sum(r['body_bytes'] for r in parent_rows), rel_tol=1e-12))
    for local in plan['diagnostic_updates']:
        point = read_json(run / f'historical-dev-{local}.json')
        require(f'historical_checkpoint_{local}_frozen_and256', point['checkpoint_sha256'] == plan['diagnostic_checkpoint_sha256'][str(local)] == sha256(Path(point['checkpoint'])) and point['body']['documents'] == 256)
        require(f'historical_checkpoint_{local}_same256_docids', [r['doc_id'] for r in point['body']['rows']] == parent_reference['doc_ids'] and point['body']['body_bytes'] == parent_reference['body_bytes'])
    tok = Tokenizer(ROOT / plan['tokenizer'])
    fixed_cases = [json.loads(line) for line in (ROOT / 'eval/base.jsonl').read_text().splitlines()]
    fixed_cases = [c for c in fixed_cases if c['split'] == 'dev']
    aux_cases = read_json(run / 'auxiliary-dev.json')['cases']
    arms, screens, full = {}, {}, {}
    for arm in ('web', 'short20'):
        record = read_json(run / arm / 'result.json')
        checkpoint = Path(record['checkpoint'])
        require(arm + '_checkpoint_sha', record['checkpoint_sha256'] == sha256(checkpoint))
        state = torch.load(checkpoint, map_location='cpu', weights_only=False)
        expected_spec = dict(parent['spec'])
        expected_spec.update(lr=plan['peak_lr'], scheduler='wsd', schedule_updates=64088,
                             pilot_schedule={'parent_update': 61036, 'stable_updates': 2900, 'decay_updates': 152})
        for key in ('branch_at', 'decay_updates', 'minimum_lr_ratio'):
            expected_spec.pop(key, None)
        require(arm + '_all_settings_match_except_frozen_LR', state['spec'] == expected_spec and state['model_config'] == parent['model_config'])
        require(arm + '_completed_updates_tokens_sources', state['update'] == 64088 and state['tokens'] == 2100035584 and
                state['sampler']['position'] == 3052 and record['additional_input_tokens'] == 100007936 and
                state['sampler']['source_tokens'] == record['source_tokens'] == old['arms'][arm]['source_tokens'] and
                state['sampler']['source_eos'] == old['arms'][arm]['source_eos_teachers'])
        require(arm + '_original_parent_lineage', state['lineage']['parent_checkpoint'] == plan['parent'] and state['lineage']['parent_spec'] == parent['spec'])
        require(arm + '_explicit_low_lr_and_preserved_resume_fields', state['spec']['lr'] == .0002 and
                state['scheduler']['base_lrs'] == [.0002] * len(parent['optimizer']['param_groups']) and
                state['scheduler']['last_epoch'] == 64088 and state['pilot_binding'] == binding and bool(state['optimizer']['state']) and
                len(state['rng']['cuda']) == 1 and state['sampler']['short']['epoch'] == 0)
        require(arm + '_finite_weights_and_optimizer', all(bool(torch.isfinite(t).all()) for t in state['model'].values()) and
                all(bool(torch.isfinite(t).all()) for row in state['optimizer']['state'].values() for t in row.values() if isinstance(t, torch.Tensor)))
        rows = [json.loads(line) for line in (run / arm / 'metrics.jsonl').read_text().splitlines()]
        original = [json.loads(line) for line in (old_run / arm / 'metrics.jsonl').read_text().splitlines()]
        require(arm + '_all3052_finite_updates', len(rows) == 3052 and [r['update'] for r in rows] == list(range(61037, 64089)) and
                all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in rows))
        require(arm + '_same_actual_tokens_digest_as_high_LR', [r['token_digest'] for r in rows] == [r['token_digest'] for r in original])
        require(arm + '_LR_only_changed_by_factor10', all(math.isclose(r['lr'] * 10, p['lr'], rel_tol=1e-12) for r, p in zip(rows, original)))
        screen = read_json(run / f'{arm}-evaluation.json')
        require(arm + '_screen_same_checkpoint256_body', screen['checkpoint_sha256'] == record['checkpoint_sha256'] and screen['body']['documents'] == 256 and
                all(r['body_tokens'] == r['scored_body_tokens'] for r in screen['body']['rows']))
        require(arm + '_screen_original80_cases', [(r['id'], r['prefix']) for r in screen['generation']['outputs']] == [(c['id'], c['prefix']) for c in fixed_cases] and
                screen['generation']['max_new_tokens'] == 64 and screen['generation']['suite_sha256'] == plan['suite_sha256'])
        require(arm + '_screen_same_aux80', [r['id'] for r in screen['auxiliary']['outputs']] == [c['id'] for c in aux_cases] and screen['auxiliary_sha256'] == plan['auxiliary_sha256'])
        require(arm + '_screen_rates_recomputed', rate(screen['generation']['outputs']) == screen['greedy_rates'] and rate(screen['auxiliary']['outputs']) == screen['auxiliary']['rates'])
        require(arm + '_natural_EOS_and_exact_text', all((r['stop_reason'] == 'stop_id') == (r['generated_ids'][-1] == 3) and len(r['generated_ids']) <= 64 and
                tok.decode_bytes(r['generated_ids']).decode('utf-8', errors='replace') == r['text'] for r in screen['generation']['outputs'] + screen['auxiliary']['outputs']))
        arms[arm] = {'checkpoint': {'path': str(checkpoint), 'sha256': record['checkpoint_sha256']},
                     'additional_input_tokens': record['additional_input_tokens'], 'cumulative_input_tokens': state['tokens'],
                     'training_seconds': record['training_seconds'], 'steady_median_tokens_per_second': statistics.median(r['tokens_per_second'] for r in rows[24:2900]),
                     'source_tokens': record['source_tokens'], 'source_eos_teachers': record['source_eos_teachers'],
                     'dev256_bpb': screen['body']['bpb'], 'greedy64': screen['greedy_rates'], 'auxiliary_greedy64': screen['auxiliary']['rates'],
                     'auxiliary_teacher_mean_eos_nll': screen['auxiliary']['teacher_mean_eos_nll'],
                     'auxiliary_teacher_eos_argmax': screen['auxiliary']['teacher_eos_argmax']}
        screens[arm] = screen
        if arm in raw['full_evaluated_arms']:
            measured = read_json(run / f'{arm}-full-evaluation.json')
            require(arm + '_full89416_body_checkpoint', measured['checkpoint_sha256'] == record['checkpoint_sha256'] and
                    measured['body']['documents'] == 89416 and measured['body']['body_bytes'] == 164344743 and
                    all(r['body_tokens'] == r['scored_body_tokens'] for r in measured['body']['rows']))
            full[arm] = {'bpb': measured['body']['bpb'], 'documents': 89416, 'body_bytes': 164344743, 'memory': measured['memory']}
            if 'generation' in measured:
                generated = measured['generation']['outputs']
                fixed = [r for r in generated if r['decoding'] == 'greedy' and r['suppressed']]
                require(arm + '_full400_and_fixed80_exact', len(generated) == 400 and
                        [(r['id'], r['generated_ids']) for r in fixed] == [(r['id'], r['generated_ids']) for r in screen['generation']['outputs']])
                full[arm].update(greedy_rates=rate(fixed), all400_rates=rate(generated))
        del state
    require('same_dev256_common_bytes_docids', screens['web']['body']['body_bytes'] == screens['short20']['body']['body_bytes'] and
            [r['doc_id'] for r in screens['web']['body']['rows']] == [r['doc_id'] for r in screens['short20']['body']['rows']])
    mixture = adoption_checks(screens['web'], screens['short20'])
    require('original_mixture_gate_recomputed', mixture == raw['improvement_checks'] and all(mixture.values()) == raw['improvement_gate_passed'])
    safe = screen_safe(screens['web'], read_json(ROOT / 'reports/phase6/base_2b_10b_data_review.json'))
    require('eligible_full_rules', ('web' in full) == (safe or all(mixture.values())) and ('short20' in full) == all(mixture.values()) and safe == raw['web_full_generation_eligible'])
    original_rows = read_json(ROOT / 'reports/phase6/base-2b-10bdata-20261004/evaluation-2B/generation.json')['generation']['outputs']
    original_rates = rate(original_rows)
    full_checks = {}
    if all(mixture.values()):
        require('full_common_docids', [r['doc_id'] for r in read_json(run / 'web-full-evaluation.json')['body']['rows']] == [r['doc_id'] for r in read_json(run / 'short20-full-evaluation.json')['body']['rows']])
        full_checks = {'BPB_within1percent_full_control': full['short20']['bpb'] <= full['web']['bpb'] * 1.01,
                       'all80_screen_IDs_match': True,
                       'no_new_empty_role_unicode_vs2B': all(full['short20']['all400_rates'][k] <= original_rates[k] for k in ('empty', 'role_leak', 'unicode_failure'))}
    require('full_adoption_gate_recomputed', full_checks == raw['full_adoption_checks'] and raw['automatic_full_gate_passed'] == (all(mixture.values()) and all(full_checks.values())))
    growth = {}
    if safe:
        growth = {'full_BPB_no_major_regression': full['web']['bpb'] <= plan['base2B_full_bpb'] + .001,
                  'fixed_repetition_not8_worse': screens['web']['greedy_rates']['repetition'] < 68,
                  'no_new_empty_role_unicode': all(full['web']['all400_rates'][k] <= original_rates[k] for k in ('empty', 'role_leak', 'unicode_failure')),
                  'all80_screen_IDs_match': True}
    require('original_growth_gate_recomputed', growth == raw['base5B_go_no_go'] and raw['base5B_eligible'] == (bool(growth) and all(growth.values())))
    require('scientific_and_verification_separate', raw['scientific_training_input_tokens'] == 200015872 and raw['verification_training_input_tokens'] == 262144)
    content = read_json(run / 'generation-content-review.json')
    require('content_review_binds_actual_generation', content['blind_human_evaluation'] is False and all(content['screen_sha256'][arm] == sha256(run / f'{arm}-evaluation.json') for arm in arms))
    for example in content['examples']:
        actual = next(r for r in screens[example['arm']]['generation']['outputs'] if r['id'] == example['id'])
        require('content_example_' + example['arm'] + example['id'], actual['text'] == example['text'] and actual['prefix'] == example['prefix'])
    evidence_names = ['job.json', 'result.json', 'tests.xml', 'resume-gate.json', 'auxiliary-dev.json', 'content-review.json', 'historical-analysis.json', 'historical-parent-reference.json', 'generation-content-review.json', 'pipeline.log']
    evidence_names += [f'{arm}-evaluation.json' for arm in arms] + [f'{arm}-full-evaluation.json' for arm in full]
    evidence_names += [f'historical-dev-{n}.json' for n in plan['diagnostic_updates']]
    result = {'status': 'completed_verified_low_lr100M_pair_and_eligible_evaluations', 'completed_at': now(),
              'plan': str(plan_path), 'parent': plan['parent'], 'model_parameters': 10000152,
              'peak_lr': plan['peak_lr'], 'arms': arms, 'full_evaluations': full, 'historical_analysis': historical, 'historical_parent_reference': parent_reference,
              'scientific_training_input_tokens': raw['scientific_training_input_tokens'], 'verification_training_input_tokens': raw['verification_training_input_tokens'],
              'actual_GPU_seconds': job['gpu_elapsed_seconds'], 'GPU_budget_seconds': plan['gpu_budget_seconds'], 'tests': tests,
              'improvement_checks': mixture, 'improvement_gate_passed': all(mixture.values()),
              'full_adoption_checks': full_checks, 'automatic_full_gate_passed': raw['automatic_full_gate_passed'],
              'base5B_go_no_go': growth, 'base5B_eligible': raw['base5B_eligible'],
              'generation_content_review': content, 'short_mixture_adopted': raw['automatic_full_gate_passed'] and content['usable_generation_accepted'],
              'quality_targets_achieved': False, 'test_split_used': False,
              'parent_full_bpb': plan['base2B_full_bpb'],
              'comparison_with_high_LR': {arm: {'dev256_bpb_high': old['arms'][arm]['dev256_bpb'], 'dev256_bpb_low': arms[arm]['dev256_bpb'],
                  'full_bpb_high': old['full_control_BPB_reference']['bpb'] if arm == 'web' else old['full_evaluations'][arm]['bpb'],
                  'full_bpb_low': full.get(arm, {}).get('bpb'),
                  'greedy_high': old['arms'][arm]['greedy64'], 'greedy_low': arms[arm]['greedy64'],
                  'auxiliary_high': old['arms'][arm]['auxiliary_greedy64'], 'auxiliary_low': arms[arm]['auxiliary_greedy64']} for arm in arms},
              'completion_checks_passed': all(checks.values()), 'completion_checks': checks, 'raw_run': str(run),
              'reviewer_sha256': sha256(Path(__file__)),
              'raw_evidence': {name: {'path': str(run / name), 'sha256': sha256(run / name)} for name in evidence_names},
              'limits': ['Single seed and one low-LR candidate; not evidence about all learning rates.',
                         'Entire LR curve is scaled by0.1, including final decay floor; this does not isolate only the first-update rewarming jump.',
                         'Generated content review is Codex observation, not independent blind human scoring.',
                         'Base/Chat criteria remain; no5B/Chat/sweeps/test evaluation.']}
    write_json(ROOT / 'reports/phase6/eos_low_lr_100m_review.json', result)
    print(json.dumps({k: result[k] for k in ('status', 'arms', 'full_evaluations', 'actual_GPU_seconds', 'improvement_gate_passed', 'base5B_eligible', 'short_mixture_adopted')}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
