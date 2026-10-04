"""Review a completed parameterized paired EOS trial without new GPU inference."""
import argparse
import json
import math
from pathlib import Path
import statistics
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.training import implementation_hashes
from phase6_performance import alive
from run_eos_complete_100m import adoption_checks, rate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, default=ROOT / 'configs/phase6/eos_complete_100m.json')
    args = parser.parse_args()
    torch.set_num_threads(2)
    plan = read_json(args.plan)
    run = ROOT / plan['output']
    raw, job = read_json(run / 'review.json'), read_json(run / 'job.json')
    checks = {}
    def require(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)
    require('job_complete_and_actual_process_exited', job['status'] == 'complete' and not alive(job))
    require('frozen_plan_and_parent', raw['binding']['plan_sha256'] == sha256(args.plan) and raw['binding']['parent'] == plan['parent'])
    require('unchanged_core_implementation', raw['binding']['implementation'] == implementation_hashes())
    require('unchanged_pilot', raw['binding']['module_sha256'] == sha256(ROOT / 'src/jmicro/eos_pilot.py'))
    require('unchanged_runner', raw['binding']['runner_sha256'] == sha256(ROOT / 'scripts/run_eos_complete_100m.py'))
    for name, digest in raw['binding']['new_source'].items():
        require(f'source_{name}', sha256(ROOT / name) == digest)
    require('unchanged_parent_checkpoint', sha256(Path(plan['parent']['path'])) == plan['parent']['sha256'])
    require('GPU_budget', job['gpu_elapsed_seconds'] <= plan['gpu_budget_seconds'])
    gate = read_json(run / 'resume-gate.json')
    require('actual_CUDA_continuous_vs_resumed_all_state', gate['passed'] and all(gate['checks'].values()) and gate['input_tokens'] == 262144)
    baseline = read_json(run / 'generation-baseline-check.json')
    require('baseline8_IDs_reproduced', baseline['passed'] and len(baseline['checks']) == 8 and all(baseline['checks'].values()))
    counts = {k: 0 for k in ('tests', 'failures', 'errors', 'skipped')}
    for suite in ET.parse(run / 'tests.xml').getroot().iter('testsuite'):
        for key in counts:
            counts[key] += int(suite.attrib.get(key, 0))
    require('targeted_tests_no_failures_or_skips', counts['tests'] > 0 and not any(counts[k] for k in ('failures', 'errors', 'skipped')))
    tok = Tokenizer(ROOT / plan['tokenizer'])
    auxiliary = read_json(run / 'auxiliary-dev.json')
    require('auxiliary80_frozen_dev_only', auxiliary['status'] == 'frozen_before_training' and len(auxiliary['cases']) == 80 and
            auxiliary['test_used'] is False and all(c['split'] == 'dev' and 32 <= len(c['body_ids']) <= 64 for c in auxiliary['cases']))
    ready = read_json(Path(plan['short_pool']) / 'ready.json')
    histogram = ready['body_token_histogram']
    require('pool_unique_complete_train_budget', ready['heldout_used'] is False and ready['tokens'] >= plan['short_pool_minimum_tokens'] and
            sum(histogram) == ready['documents'] and sum(histogram[:32]) == 0 and len(histogram) == 65 and
            sum((i + 2) * n for i, n in enumerate(histogram)) == ready['tokens'] and ready['seconds'] <= plan['prepare_budget_seconds'])
    require('pool_auxiliary_binding', ready['auxiliary_sha256'] == sha256(run / 'auxiliary-dev.json') == raw['binding']['auxiliary_sha256'])
    require('pool_manifest_binding', sha256(Path(plan['short_pool']) / 'manifest.json') == ready['manifest_sha256'] == raw['binding']['short_manifest_sha256'])
    content = read_json(run / 'content-review.json')
    require('pretraining_content_review', content['passed'] and content['pool_manifest_sha256'] == ready['manifest_sha256'] and content['auxiliary_sha256'] == ready['auxiliary_sha256'])
    evaluations, arms = {}, {}
    for arm in ('web', 'short20'):
        record = read_json(run / arm / 'result.json')
        checkpoint = Path(record['checkpoint'])
        require(f'{arm}_checkpoint_sha', sha256(checkpoint) == record['checkpoint_sha256'])
        state = torch.load(checkpoint, map_location='cpu', weights_only=False)
        required = ('model', 'optimizer', 'scheduler', 'rng', 'sampler', 'tokens', 'supervised_tokens', 'body_bytes',
                    'token_digest', 'spec', 'model_config', 'implementation_sha256', 'update', 'lineage', 'pilot_binding')
        require(f'{arm}_all_resume_fields', all(k in state for k in required))
        require(f'{arm}_updates_tokens_routes', state['update'] == plan['parent']['update'] + plan['updates_per_arm'] and
                state['tokens'] == plan['parent']['tokens_seen'] + plan['tokens_per_arm'] and state['sampler']['position'] == plan['updates_per_arm'])
        expected_short = plan['short_input_tokens'] if arm == 'short20' else 0
        require(f'{arm}_source_accounting', state['sampler']['source_tokens'] == record['source_tokens'] and
                sum(record['source_tokens'].values()) == plan['tokens_per_arm'] and record['source_tokens']['short'] == expected_short)
        require(f'{arm}_same_parent_schedule', state['pilot_binding'] == raw['binding'] and state['lineage']['parent_checkpoint'] == plan['parent'] and
                state['spec']['pilot_schedule'] == {'parent_update': plan['parent']['update'], 'stable_updates': plan['stable_updates'], 'decay_updates': plan['decay_updates']})
        require(f'{arm}_scheduler_optimizer_RNG', state['scheduler']['last_epoch'] == state['update'] and bool(state['optimizer']['state']) and len(state['rng']['cuda']) == 1)
        require(f'{arm}_short_epoch0', state['sampler']['short']['epoch'] == 0)
        tensors = [*state['model'].values(), *[v for values in state['optimizer']['state'].values() for v in values.values() if isinstance(v, torch.Tensor)]]
        require(f'{arm}_finite_weights_optimizer', all(bool(torch.isfinite(t).all()) for t in tensors))
        history = [json.loads(line) for line in (run / arm / 'metrics.jsonl').read_text().splitlines()]
        require(f'{arm}_all_completed_updates', len(history) == plan['updates_per_arm'] and [r['update'] for r in history] == list(range(plan['parent']['update'] + 1, state['update'] + 1)))
        require(f'{arm}_finite_training', all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history))
        evaluation = read_json(run / f'{arm}-evaluation.json')
        require(f'{arm}_evaluation_checkpoint', evaluation['checkpoint_sha256'] == record['checkpoint_sha256'])
        require(f'{arm}_body256_exact_scoring', evaluation['body']['documents'] == 256 and all(r['body_tokens'] == r['scored_body_tokens'] for r in evaluation['body']['rows']))
        fixed, aux_rows = evaluation['generation']['outputs'], evaluation['auxiliary']['outputs']
        require(f'{arm}_original80_fixed_cases', len(fixed) == 80 and evaluation['generation']['max_new_tokens'] == 64 and evaluation['generation']['suite_sha256'] == plan['suite_sha256'])
        require(f'{arm}_same_auxiliary80', [r['id'] for r in aux_rows] == [c['id'] for c in auxiliary['cases']] and evaluation['auxiliary_sha256'] == ready['auxiliary_sha256'])
        require(f'{arm}_rates_recomputed', rate(fixed) == evaluation['greedy_rates'] and rate(aux_rows) == evaluation['auxiliary']['rates'])
        for name, rows in (('fixed', fixed), ('aux', aux_rows)):
            require(f'{arm}_{name}_naturalEOS_valid64', all(r['split'] == 'dev' and r['decoding'] == 'greedy' and r['suppressed'] and
                    (r['stop_reason'] == 'stop_id') == (r['generated_ids'][-1] == 3) and len(r['generated_ids']) <= 64 for r in rows))
            require(f'{arm}_{name}_decoded_text_matches_IDs', all(tok.decode_bytes(r['generated_ids']).decode('utf-8', errors='replace') == r['text'] for r in rows))
        arms[arm] = {'checkpoint': {'path': str(checkpoint), 'sha256': record['checkpoint_sha256']},
            'additional_input_tokens': record['additional_input_tokens'], 'cumulative_input_tokens': state['tokens'],
            'training_seconds': record['training_seconds'], 'steady_median_tokens_per_second': statistics.median(r['tokens_per_second'] for r in history[24:plan['stable_updates']]),
            'source_tokens': record['source_tokens'], 'source_eos_teachers': record['source_eos_teachers'],
            'dev256_bpb': evaluation['body']['bpb'], 'dev256_mean_eos_nll': evaluation['body']['eos_nll'] / 256,
            'greedy64': evaluation['greedy_rates'], 'auxiliary_greedy64': evaluation['auxiliary']['rates'],
            'auxiliary_teacher_mean_eos_nll': evaluation['auxiliary']['teacher_mean_eos_nll'],
            'auxiliary_teacher_eos_argmax': evaluation['auxiliary']['teacher_eos_argmax']}
        evaluations[arm] = evaluation
        del state, tensors
    require('same_dev256_documents_bytes', [r['doc_id'] for r in evaluations['web']['body']['rows']] == [r['doc_id'] for r in evaluations['short20']['body']['rows']] and
            evaluations['web']['body']['body_bytes'] == evaluations['short20']['body']['body_bytes'])
    require('same_original80_cases', [r['id'] for r in evaluations['web']['generation']['outputs']] == [r['id'] for r in evaluations['short20']['generation']['outputs']])
    require('adoption_gate_independently_recomputed', adoption_checks(evaluations['web'], evaluations['short20']) == raw['improvement_checks'] and raw['improvement_gate_passed'] == all(raw['improvement_checks'].values()))
    require('scientific_and_verification_separate', raw['scientific_training_input_tokens'] == plan['scientific_total_tokens'] == sum(a['additional_input_tokens'] for a in arms.values()) and raw['verification_training_input_tokens'] == gate['input_tokens'])
    full = {}
    for arm in raw['full_evaluated_arms']:
        evidence = read_json(run / f'{arm}-full-evaluation.json')
        require(f'{arm}_full89416_and400', evidence['body']['documents'] == 89416 and evidence['body']['body_bytes'] == 164344743 and len(evidence['generation']['outputs']) == 400)
        require(f'{arm}_full_checkpoint', evidence['checkpoint_sha256'] == arms[arm]['checkpoint']['sha256'])
        full[arm] = {'bpb': evidence['body']['bpb'], 'body_bytes': evidence['body']['body_bytes'], 'documents': evidence['body']['documents'],
                     'greedy_rates': evidence['greedy_rates'], 'all400_rates': rate(evidence['generation']['outputs'])}
    require('conditional_full_short_only_if_screen_passes', ('short20' in full) == raw['improvement_gate_passed'])
    require('full_adoption_gate', raw['short_mixture_adopted'] == (raw['improvement_gate_passed'] and all(raw['full_adoption_checks'].values())))
    report = {'status': 'completed_verified_two_arm_complete_unit100M_comparison', 'completed_at': now(), 'plan': str(args.plan),
        'parent': plan['parent'], 'model_parameters': 10000152, 'arms': arms,
        'scientific_training_input_tokens': raw['scientific_training_input_tokens'], 'verification_training_input_tokens': raw['verification_training_input_tokens'],
        'actual_GPU_seconds': job['gpu_elapsed_seconds'], 'short_pool': ready,
        'common_dev_documents': 256, 'common_dev_body_bytes': evaluations['web']['body']['body_bytes'],
        'short_vs_control_BPB_change_percent': (arms['short20']['dev256_bpb'] / arms['web']['dev256_bpb'] - 1) * 100,
        'improvement_checks': raw['improvement_checks'], 'improvement_gate_passed': raw['improvement_gate_passed'],
        'short_mixture_adopted': raw['short_mixture_adopted'], 'full_adoption_checks': raw['full_adoption_checks'], 'full_evaluations': full,
        'base5B_go_no_go': raw['base5B_go_no_go'], 'base5B_eligible': raw['base5B_eligible'],
        'decision': raw['decision'], 'test_split_used': False, 'quality_targets_achieved': False, 'tests': counts,
        'completion_checks_passed': all(checks.values()), 'completion_checks': checks,
        'raw_run': str(run), 'reviewer_sha256': sha256(Path(__file__)),
        'raw_evidence': {name: {'path': str(run / name), 'sha256': sha256(run / name)} for name in
            ('job.json', 'review.json', 'resume-gate.json', 'generation-baseline-check.json', 'auxiliary-dev.json', 'content-review.json', 'web-evaluation.json', 'short20-evaluation.json', 'tests.xml', 'pipeline.log')},
        'limits': ['Single seed and100M per arm; not a proof about all short-data conditions.',
                   'New unit definition and larger dose both differ from25M; only this equal-budget pair isolates mixture effect.',
                   'Auxiliary short dev diagnostic does not replace failing fixed80.',
                   'No blind human grammar/relevance scores, unused test scores,5B training or Chat completion.',
                   'New unit EOS defines a complete sentence record, not the original article end.']}
    destination = ROOT / 'reports/phase6/eos_complete_100m_review.json'
    write_json(destination, report)
    print(json.dumps({'status': report['status'], 'arms': arms, 'adopted': report['short_mixture_adopted'], 'full': full, 'actual_GPU_seconds': report['actual_GPU_seconds']}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
