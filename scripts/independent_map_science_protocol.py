"""Typed original100M comparison and unchanged Base quality guards."""
import math
from pathlib import Path

from jmicro.phase5 import equal_state
from jmicro.evaluation_boundary import load_dev_suite
from base_fim_pilot_protocol import notes_scores, validate_body, validate_raw
from independent_map_trainer import committed_state, KIND, POLICY as RECIPE
from jmicro.independent_map import native_config, TAG, added_parameters, IMPLEMENTATION
from review_matched_story_study import quality_gates
from run_eos_complete_100m import adoption_checks


def science_budget(probe):
    rows = probe['all32_timings']
    elapsed = probe['cumulative_technical_GPU_seconds']
    activity=probe.get('all52_new_tensors_active',{})
    expected={f'model.layers.{i}.self_attn.{part}' for i in range(13) for part in
              ('independent_raw','independent_down.weight','independent_q.weight','independent_k.weight')}
    disabled=probe.get('disabled_native3_subchecks',[])
    disabled_fields={'CE_loss','gradient_norm','token_digest','source_teachers','source_EOS',
        'physical_input_tokens','CE_input_tokens','original_body_bytes','draw_trace','lr',
        'original_model_weights_exact','sampler_exact','scheduler_exact','RNG_exact',
        'original_Adam_all_coordinates_exact','different_Adam_names'}
    if (probe.get('passed') is not True or probe.get('full_state_history_resume_exact') is not True
            or probe.get('initial_native_function_parity') is not True
            or probe.get('disabled3_original_numeric_state_and_stream_exact') is not True
            or len(disabled)!=3 or any(set(r)!=disabled_fields or r.get('different_Adam_names')!=[] or any(v is not True
                for k,v in r.items() if k!='different_Adam_names') for r in disabled)
            or set(activity)!=expected or any(set(r)!={'change','Adam_moment_abs_max','gradient_abs_max'}
                or any(not math.isfinite(v) or v<=0 for v in r.values()) for r in activity.values())
            or probe.get('cumulative_GPU_ledger_closed') is not True
            or not 0<probe['GPU_occupancy_seconds']
            or not math.isclose(elapsed,72.56365345604718+probe['GPU_occupancy_seconds'],rel_tol=0,abs_tol=1e-12)
            or len(rows) != 32
            or probe.get('candidate_parameters') != 10067764 or probe.get('native_parameters') != 10001152
            or probe.get('capacity', {}).get('passed') is not True
            or probe['capacity'].get('shape')!=[48,1024] or probe['capacity'].get('optimizer_updates')!=0
            or probe['capacity'].get('physical_input_tokens')!=49152 or probe['capacity'].get('teachers')!=24576
            or probe.get('active_cache', {}).get('passed') is not True
            or set(probe['active_cache'].get('subchecks',{}))!={'finite_logits','logits_within_original_tolerance',
                'secondary_K2_within_original_tolerance','positions_exact','validity_exact','RNG_unchanged'}
            or not all(probe['active_cache']['subchecks'].values())
            or probe['active_cache'].get('absolute_tolerance')!=3e-5 or probe['active_cache'].get('relative_tolerance')!=2e-5
            or not probe.get('verification6_snapshot',{}).get('sha256')
            or not 0 < elapsed <= 180 or any(not math.isfinite(r['seconds']) or r['seconds'] <= 0
                or type(r['CE_targets_this_update']) is not int or r['CE_targets_this_update'] <= 0 for r in rows)):
        raise ValueError('Actual owned native timing/resume/scope evidence required')
    budget = math.ceil(17698 / 32 * sum(r['seconds'] for r in rows) * 1.3 + 600)
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
        'unchanged_original_base_config': native_config(candidate['model_config']) == control['model_config'],
        'only_declared_model_difference': (candidate['model_config'][TAG]['policy'] == RECIPE
            and candidate['model_config'][TAG]['arm'] == 'independent_learned'
            and candidate['spec']['actual_unique_parameters'] == candidate['model_config']['expected_parameter_count']
            and candidate['model_config']['expected_parameter_count'] == control['model_config']['expected_parameter_count']
                + added_parameters(control['model_config'])),
        'original_main_physical_inputs': ce_physical == control['counters']['physical_input_tokens']}


def validate_history(rows, state):
    c = state['counters']
    if (not committed_state(state) or state['kind'] != KIND or state['spec']['independent_policy'] != RECIPE
            or len(rows) != c['update'] or [r['update'] for r in rows] != list(range(1, c['update'] + 1))):
        raise ValueError('All completed updates and genuine typed numerical state required')
    if rows and any(rows[-1][key] != value for key, value in c.items()):
        raise ValueError('Terminal metrics/counters differ')
    if any(not all(math.isfinite(r[k]) for k in ('CE_loss', 'contrast_loss', 'combined_loss',
           'gradient_norm', 'auxiliary_gradient_norm', 'independent_coefficient_abs_max', 'independent_coefficient_mean'))
           or r['CE_loss'] < 0 or r['contrast_loss'] != 0 or r['auxiliary_gradient_norm'] != 0
           or r['lr'] != 1e-5 or not 0 <= r['independent_coefficient_abs_max'] < 1
           or r['combined_loss'] != r['CE_loss']
           or r['independent_projection_elements_this_update'] != r['physical_inputs_this_update']
                *(added_parameters(state['model_config'])-state['model_config']['num_hidden_layers']*state['model_config']['num_attention_heads'])
           for r in rows):
        raise ValueError('Finite original CE and declared map-compute metrics required')
    rollup = dict(CE_physical_inputs=sum(r['physical_inputs_this_update'] for r in rows),
                  auxiliary_physical_inputs=0)
    if (sum(rollup.values()) != c['physical_input_tokens']
            or sum(r['CE_targets_this_update'] for r in rows) != c['supervised_tokens']
            or any(r['auxiliary_inputs_this_update'] != 0 or r['auxiliary_pairs_this_update'] != 0 for r in rows)
            or sum(r['independent_projection_elements_this_update'] for r in rows) != c['independent_projection_elements']):
        raise ValueError('Original CE and separately counted map-compute clocks differ')
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
    matched = quality_gates(control, candidate, control_scores, candidate_scores, 'matched_CE_vs_independent_map')
    relative = quality_gates(strong, candidate, strong_scores, candidate_scores, 'content')
    summary = summarize(candidate, candidate_scores)
    absolute = dict(grammar_at_least56=summary['grammar2'] >= 56,
        coherence_at_least27=summary['coherent'] >= 27, appropriate_at_least27=summary['appropriate'] >= 27,
        EOS_at_least37=summary['rates']['eos'] >= 37, repetition_at_most18=summary['rates']['repetition'] <= 18,
        no_empty_role_unicode=all(summary['rates'][k] == 0 for k in ('empty', 'role_leak', 'unicode_failure')))
    web = adoption_checks(historical, candidate)
    return dict(matched=matched, strong=relative, absolute=absolute, historical_Web=web,
                eligible=matched['passed'] and relative['passed'] and all(absolute.values()) and all(web.values()))
