"""Typed original100M comparison and unchanged Base quality guards."""
import math
from pathlib import Path

from jmicro.phase5 import equal_state
from jmicro.evaluation_boundary import load_dev_suite
from base_fim_pilot_protocol import notes_scores, validate_body, validate_raw
from context_likelihood_trainer import committed_state, KIND, RECIPE
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks


def science_budget(probe):
    rows = probe['all32_timings']
    elapsed = probe['GPU_occupancy_seconds']
    if (probe.get('passed') is not True or probe.get('all_state_and_history_resume_equal') is not True
            or probe.get('actual_auxiliary_active') is not True or len(rows) != 32
            or not 0 < elapsed <= 180 or any(not math.isfinite(r['seconds']) or r['seconds'] <= 0
                or type(r['CE_targets_this_update']) is not int or r['CE_targets_this_update'] <= 0 for r in rows)):
        raise ValueError('Actual owned native timing/resume/scope evidence required')
    budget = math.ceil(100000000 / sum(r['CE_targets_this_update'] for r in rows)
                       * sum(r['seconds'] for r in rows) * 1.3 + 600)
    if (budget != probe['scientific_forecast_seconds'] or budget + elapsed > 4800
            or probe['science_budget_eligible'] is not True):
        raise ValueError('Fixed100M forecast exceeds total4800s; no budget/teacher rescue')
    return budget


def matched_original(candidate, control, ce_physical):
    fields = ('update', 'token_digest', 'supervised_tokens', 'source_teachers',
              'source_EOS', 'CE_input_tokens', 'original_body_bytes')
    return {key: equal_state(candidate['counters'][key], control['counters'][key]) for key in fields} | {
        'full_original_sampler': equal_state(candidate['sampler'], control['sampler']),
        'actual_original_scheduler': equal_state(candidate['scheduler'], control['scheduler']),
        'original_model_config': candidate['model_config'] == control['model_config'],
        'original_main_physical_inputs': ce_physical == control['counters']['physical_input_tokens']}


def validate_history(rows, state):
    c = state['counters']
    if (not committed_state(state) or state['kind'] != KIND or state['spec']['likelihood_recipe'] != RECIPE
            or len(rows) != c['update'] or [r['update'] for r in rows] != list(range(1, c['update'] + 1))):
        raise ValueError('All completed updates and genuine typed numerical state required')
    if rows and any(rows[-1][key] != value for key, value in c.items()):
        raise ValueError('Terminal metrics/counters differ')
    if any(not all(math.isfinite(r[k]) for k in ('CE_loss', 'auxiliary_loss', 'combined_loss',
           'gradient_norm', 'auxiliary_gradient_norm', 'positive_context_margin'))
           or r['CE_loss'] < 0 or r['auxiliary_loss'] < 0 or r['lr'] != 1e-5
           or r['repeated_auxiliary_likelihood_targets_this_update'] < 32 * r['auxiliary_pairs_this_update']
           for r in rows):
        raise ValueError('Finite exact original/auxiliary committed metrics required')
    rollup = dict(CE_physical_inputs=sum(r['CE_physical_inputs_this_update'] for r in rows),
                  auxiliary_physical_inputs=sum(r['auxiliary_physical_inputs_this_update'] for r in rows))
    if (sum(rollup.values()) != c['physical_input_tokens']
            or sum(r['CE_targets_this_update'] for r in rows) != c['supervised_tokens']
            or sum(r['repeated_auxiliary_likelihood_targets_this_update'] for r in rows) != c['auxiliary_target_evaluations']
            or sum(r['auxiliary_pairs_this_update'] for r in rows) != c['auxiliary_pairs']
            or sum(r['eligible_anchors_this_update'] for r in rows) != c['eligible_anchors_committed']):
        raise ValueError('Original and repeated auxiliary input/teacher/FIFO clocks differ')
    return rollup


def validate_evaluation(ev, codec, suite):
    validate_body(ev['body'])
    validate_raw(ev['generation']['outputs'], codec, suite)
    if (ev['generation']['checkpoint_sha256'] != ev['checkpoint_sha256']
            or ev['generation']['binding'] != ev['binding'] or ev['evaluation_RNG_isolated'] is not True
            or ev['TEST_opened'] is not False or ev['legacy_mixed_suite_opened'] is not False):
        raise ValueError('Checkpoint-bound isolated Base evaluation required')
    for task, count in (('semantics', 192), ('jblimp', 331), ('jcqa', 1119)):
        if not ev['diagnostics'][task]['complete'] or ev['diagnostics'][task]['count'] != count:
            raise ValueError('All unchanged fixed Japanese diagnostic tasks required')


def summarize(ev, scores):
    return dict(BPB=ev['body']['bpb'], rates=ev['greedy_rates'],
        grammar2=sum(s['grammar'] == 2 for s in scores.values()),
        relevance2=sum(s['relevance'] == 2 for s in scores.values()),
        coherent=sum(s['coherence'] == 2 for s in scores.values()),
        appropriate=sum(s['completion'] for s in scores.values()),
        Japanese={task: ev['diagnostics'][task]['primary']['accuracy']['point']
                  for task in ('semantics', 'jblimp', 'jcqa')})


def original_quality(control, strong, historical, candidate, control_scores, strong_scores, candidate_scores):
    # Preserve old full-comparison stage semantics: matched BPB cannot rise;
    # strong comparison allows its original1percent, historical Web separately.
    matched = quality_gates(control, candidate, control_scores, candidate_scores, 'matched_CE_vs_context_likelihood')
    relative = quality_gates(strong, candidate, strong_scores, candidate_scores, 'content')
    summary = summarize(candidate, candidate_scores)
    absolute = dict(grammar_at_least56=summary['grammar2'] >= 56,
        coherence_at_least27=summary['coherent'] >= 27, appropriate_at_least27=summary['appropriate'] >= 27,
        EOS_at_least37=summary['rates']['eos'] >= 37, repetition_at_most18=summary['rates']['repetition'] <= 18,
        no_empty_role_unicode=all(summary['rates'][k] == 0 for k in ('empty', 'role_leak', 'unicode_failure')))
    web = adoption_checks(historical, candidate)
    return dict(matched=matched, strong=relative, absolute=absolute, historical_Web=web,
                eligible=matched['passed'] and relative['passed'] and all(absolute.values()) and all(web.values()))
