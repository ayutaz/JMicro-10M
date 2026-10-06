"""Review the completed Base comparison without rerunning GPU inference.

The matched CE comparison diagnoses the new objective. Existing strong Base
and historical Web references still govern qualification; neither a finished
job nor a favorable matched comparison alone adopts a Base.
"""
import argparse
import json
from pathlib import Path
import sys

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'),
                str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.training import atomic_json
from phase6_performance import alive, finite_state
from natural_context_contrast_corpus import KIND
from run_eos_short_pilot import equal_state
from run_eos_complete_100m import adoption_checks
from review_matched_story_study import quality_gates
from review_parameter_displacement_anchor import content

CONFIG = ROOT / 'configs/phase6/natural_context_contrast_comparison.json'
POLICY = ROOT / 'configs/phase6/natural_context_contrast_review.json'
RUN = ROOT / 'reports/phase6/natural-context-contrast-comparison-20261007'
ARMS = ('CE', 'contrast')


def checked_reference(reference):
    path = Path(reference['path'])
    if sha256(path) != reference['sha256']:
        raise ValueError('Review reference changed: ' + str(path))
    return path


def prepare():
    if POLICY.exists():
        raise ValueError('Preserve the existing review policy')
    previous = read_json(ROOT / 'configs/phase6/base_preference_comparison.json')
    original = checked_reference(previous['original_config'])
    base = read_json(original)
    references = {key: previous['references'][key] for key in ('strong_result', 'strong_notes')}
    references['original_config'] = previous['original_config']
    references['historical_Web'] = base['reference']['web_screen']
    for reference in references.values():
        checked_reference(reference)
    strong = read_json(Path(references['strong_result']['path']))
    ev, record = strong['evaluations']['source_order'], strong['checkpoints']['source_order']
    raw = Path(references['strong_result']['path']).parent / 'evaluation/source_order/evaluation/generation.json'
    summary, _ = content('strong_staged', ev, record, base, raw, Path(references['strong_notes']['path']))
    if summary['coherent'] != 23 or summary['rates']['eos'] != 76 or summary['rates']['repetition'] != 2:
        raise ValueError('Existing strong Base baseline differs')
    helpers = ('scripts/review_natural_context_contrast.py', 'scripts/review_matched_story_study.py',
               'scripts/review_parameter_displacement_anchor.py', 'scripts/review_textbook_quantity_comparison.py',
               'scripts/review_eos_5b_finish.py', 'scripts/run_eos_complete_100m.py')
    atomic_json(POLICY, dict(created_at=now(), scientific_config_sha256=sha256(CONFIG), references=references,
        helper_sha256={name: sha256(ROOT / name) for name in helpers},
        criteria='Unchanged strong-baseline relative gates, absolute Base gates and historical Web BPB guard. '
                 'Contrast additionally requires the matched CE quality comparison. All160 individual raw-bound '
                 'notes; independent learned seed/full DEV/protected final TEST/adoption remain necessary.',
        strong_summary=summary, Base_complete=False, Chat_started=False, quantization_started=False))
    print(json.dumps(dict(status='review_policy_prepared', scientific_results_read=False,
                         additional_GPU_seconds=0, strong_coherent=23)))


def load_policy():
    c, policy = read_json(CONFIG), read_json(POLICY)
    if policy['scientific_config_sha256'] != sha256(CONFIG):
        raise ValueError('Frozen scientific config changed')
    for name, digest in {**c['source_sha256'], **policy['helper_sha256']}.items():
        if sha256(ROOT / name) != digest:
            raise ValueError('Frozen source changed: ' + name)
    for reference in policy['references'].values():
        checked_reference(reference)
    return c, policy


def audit_terminal(job, result, c, digest, live):
    if (live or job['status'] != 'complete' or result['status'] != 'complete'
            or job['config_sha256'] != digest or result['config_sha256'] != digest
            or result['actual_identity'] != {k: job[k] for k in ('pid', 'boot_id', 'start_ticks')}
            or not 0 < result['GPU_occupancy_seconds'] == job['GPU_occupancy_seconds'] <= c['GPU_budget_seconds']
            or result['scientific_CE_teacher_tokens'] != 2 * c['CE_tokens_per_arm']
            or set(result['results']) != set(ARMS)
            or set(result['common_CE_checks']) != set(COMMON)
            or not all(v is True for v in result['common_CE_checks'].values())
            or any(result[k] for k in ('Base_complete', 'Chat_started', 'quantization_started'))):
        raise ValueError('Actual completed, exited, bounded Base-only comparison required')


COMMON = ('token_digest', 'supervised_tokens', 'source_teachers', 'source_EOS',
          'CE_input_tokens', 'original_body_bytes')


def audit_checkpoint(state, record, c, arm, digest):
    counters, spec, sampler = state['counters'], state['spec'], state['sampler']
    binding = dict(parent=c['parent'], source_binding=c['source_binding'], config_sha256=digest,
                   weights_role='scientific_' + arm, sources=c['source_sha256'])
    if (state['kind'] != KIND or spec['kind'] != KIND or state['binding'] != binding
            or record['status'] != 'complete' or record['binding'] != binding
            or state['counters'] != record['counters'] or not equal_state(sampler, record['sampler'])
            or record['scientific_CE_teacher_tokens'] != c['CE_tokens_per_arm']
            or counters['supervised_tokens'] != c['CE_tokens_per_arm']
            or counters['source_teachers'] != c['goals'] or sampler['consumed'] != c['goals']
            or sampler['goals'] != c['goals'] or sampler['binding'] != c['source_binding']
            or state['lineage']['parent'] != c['parent']
            or state['lineage']['parent_supervised_tokens'] != record['parent_CE_teacher_tokens']
            or state['lineage']['weights_role'] != 'scientific_' + arm
            or spec['batch'] != c['batch'] or spec['seed'] != sampler['seed'] or spec['seed'] != c['seed']
            or spec['contrast'] is not (arm == 'contrast') or spec['temperature'] != c['temperature']
            or spec['coefficient'] != c['coefficient'] or spec['lr'] != 1e-5 or spec['weight_decay'] != .1
            or spec['scheduler'] != 'constant' or spec['optimizer_policy'] != 'fresh_equal_AdamW_both_arms'
            or spec['dtype'] != 'bf16' or spec['backend'] != 'flash'
            or not all(k in state for k in ('model', 'optimizer', 'scheduler', 'RNG', 'sampler'))
            or counters['update'] <= 0 or not finite_state(state)
            or state['scheduler']['last_epoch'] != counters['update']
            or any(g['lr'] != 1e-5 or g['weight_decay'] != .1 for g in state['optimizer']['param_groups'])
            or any(int(v['step']) != counters['update'] for v in state['optimizer']['state'].values())
            or (arm == 'CE' and (counters['auxiliary_pairs'] or counters['auxiliary_input_tokens']))
            or (arm == 'contrast' and (counters['auxiliary_pairs'] <= 0 or counters['auxiliary_input_tokens'] <= 0))):
        raise ValueError('Completed original-source full-state accounting differs: ' + arm)
    return dict(completed_updates=counters['update'], CE_teacher_tokens=counters['supervised_tokens'],
        auxiliary_input_tokens=counters['auxiliary_input_tokens'], auxiliary_pairs=counters['auxiliary_pairs'],
        CE_input_tokens=counters['CE_input_tokens'], physical_input_tokens=counters['physical_input_tokens'],
        source_teachers=counters['source_teachers'], source_EOS=counters['source_EOS'],
        original_body_bytes=counters['original_body_bytes'], original_source_draws=sampler['draws'],
        source_windows=sampler['windows_emitted'], additional_unique_supply_claimed=False)


def notes_path(arm):
    return ROOT / f'reports/phase6/natural_context_contrast_{arm}_notes.json'


def raw_path(arm):
    return RUN / f'evaluation/{arm}/evaluation/generation.json'


def template(arm):
    c, _ = load_policy()
    ev = read_json(RUN / f'evaluation/{arm}/evaluation/result.json')
    record = read_json(RUN / arm / 'train-result.json')
    raw = raw_path(arm)
    if (ev['checkpoint_sha256'] != record['checkpoint_sha256'] or ev['binding'] != record['binding']
            or read_json(raw) != ev['generation'] or len(ev['generation']['outputs']) != 80):
        raise ValueError('Complete checkpoint-bound evaluation required before notes')
    path = notes_path(arm)
    if path.exists():
        raise ValueError('Preserve existing content notes')
    atomic_json(path, dict(reviewer='Codex nonblind; every continuation requires individual reading',
        independent_human_blind=False, generation_sha256=sha256(raw),
        notes=[[r['id'], None, None, None, None, ''] for r in ev['generation']['outputs']]))
    print(json.dumps(dict(arm=arm, unscored=80, path=str(path))))


def review():
    c, policy = load_policy()
    job = read_json(RUN / 'job.json')
    live = alive(job)
    if live or job['status'] != 'complete':
        raise ValueError('Scientific process must finish and exit before final review')
    result = read_json(RUN / 'result.json')
    digest = sha256(CONFIG)
    audit_terminal(job, result, c, digest, live)
    probe = read_json(checked_reference(c['probe_result']))
    if not probe['passed'] or not all(g['passed'] and all(g['checks'].values()) for g in probe['gates'].values()):
        raise ValueError('Actual completed CUDA full-state resume gates required')
    base = read_json(Path(policy['references']['original_config']['path']))
    old = read_json(Path(policy['references']['strong_result']['path']))
    strong = old['evaluations']['source_order']
    strong_raw = Path(policy['references']['strong_result']['path']).parent / 'evaluation/source_order/evaluation/generation.json'
    summaries, scores, accounts, states = {}, {}, {}, {}
    summaries['strong_staged'], scores['strong_staged'] = content('strong_staged', strong,
        old['checkpoints']['source_order'], base, strong_raw, Path(policy['references']['strong_notes']['path']))
    if summaries['strong_staged'] != policy['strong_summary']:
        raise ValueError('Historical strong content changed')
    for arm in ARMS:
        record, ev = result['results'][arm]['training'], result['results'][arm]['evaluation']
        if sha256(Path(record['checkpoint'])) != record['checkpoint_sha256']:
            raise ValueError('Terminal checkpoint changed: ' + arm)
        state = torch.load(record['checkpoint'], map_location='cpu', weights_only=False)
        accounts[arm] = audit_checkpoint(state, record, c, arm, digest)
        with torch.random.fork_rng(devices=[]):
            model = JMicroModel(state['model_config'])
        model.load_state_dict(state['model'], strict=True)
        if sum(p.numel() for p in model.parameters()) != 10001152:
            raise ValueError('Original native10M architecture required')
        del model
        summaries[arm], scores[arm] = content(arm, ev, record, c, raw_path(arm), notes_path(arm))
        if ([(r['id'], r['prefix']) for r in ev['generation']['outputs']] !=
                [(r['id'], r['prefix']) for r in strong['generation']['outputs']]
                or [(r['doc_id'], r['body_tokens'], r['body_bytes']) for r in ev['body']['rows']] !=
                [(r['doc_id'], r['body_tokens'], r['body_bytes']) for r in strong['body']['rows']]):
            raise ValueError('Same fixed prefixes/common-byte targets required')
        states[arm] = {'counters': state['counters'], 'sampler': state['sampler']}
        del state
    common = {key: states['CE']['counters'][key] == states['contrast']['counters'][key] for key in COMMON}
    if not all(common.values()) or not equal_state(states['CE']['sampler'], states['contrast']['sampler']):
        raise ValueError('Actual matched CE source digest/cursors/counters differ')
    web = read_json(Path(policy['references']['historical_Web']['path']))
    quality, absolute, original, eligible = {}, {}, {}, {}
    matched = quality_gates(result['results']['CE']['evaluation'], result['results']['contrast']['evaluation'],
                            scores['CE'], scores['contrast'], 'content')
    for arm in ARMS:
        ev, s = result['results'][arm]['evaluation'], summaries[arm]
        quality[arm] = quality_gates(strong, ev, scores['strong_staged'], scores[arm], 'content')
        absolute[arm] = dict(grammar_at_least56=s['grammar2'] >= 56, coherence_at_least27=s['coherent'] >= 27,
            appropriate_at_least27=s['appropriate'] >= 27, EOS_at_least37=s['rates']['eos'] >= 37,
            repetition_at_most18=s['rates']['repetition'] <= 18,
            no_empty_role_unicode=all(s['rates'][k] == 0 for k in ('empty', 'role_leak', 'unicode_failure')))
        original[arm] = adoption_checks(web, ev)
        eligible[arm] = quality[arm]['passed'] and all(absolute[arm].values()) and all(original[arm].values())
    eligible['contrast'] = eligible['contrast'] and matched['passed']
    report = dict(status='all160_context_comparison_reviewed', created_at=now(), config_sha256=digest,
        review_policy_sha256=sha256(POLICY), result_sha256=sha256(RUN / 'result.json'),
        summaries=summaries, strong_relative_quality=quality, matched_objective_quality=matched,
        absolute_dev_screen=absolute, historical_Web=original, eligible_for_final_Base_validation=eligible,
        accounting=accounts, common_CE_checks=common, scientific_CE_teacher_tokens=200000000,
        probe_updates_separate=probe['verification_updates'], GPU_occupancy_seconds=result['GPU_occupancy_seconds'],
        all160_individually_read=True, independent_human_blind=False, protected_test_used=False,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        quality_criteria_unchanged=True, final_seed_full_dev_test_adoption_pending=True,
        limitations='One learned seed and repeated nonblind DEV; source draws are exposure, not unique supply. '
                    'The evaluator marks no protected TEST cases evaluated; its task loader may decode the suite JSON. '
                    'Diagnostic CUDA resume updates and auxiliary input are separate from scientific CE teachers.',
        next_action='Only a qualified fixed candidate advances to independent learning seed/full DEV/protected final '
                    'TEST/adoption. Otherwise close these fixed recipes; no outcome-based source/coefficient/LR/epoch rescue.')
    destination = RUN / 'review.json'
    if destination.exists():
        raise ValueError('Preserve original comparison review')
    atomic_json(destination, report)
    atomic_json(ROOT / 'reports/phase6/natural_context_contrast_comparison_review.json', report)
    print(json.dumps(dict(summaries=summaries, eligible=eligible), ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2)
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--prepare', action='store_true')
    group.add_argument('--template', choices=ARMS)
    args = parser.parse_args()
    if args.prepare:
        prepare()
    elif args.template:
        template(args.template)
    else:
        review()
