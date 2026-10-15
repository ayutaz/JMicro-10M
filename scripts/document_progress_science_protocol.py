"""Paired25M typed evidence and original, unchanged quality criteria."""
import math

from jmicro.document_progress import ARMS,POLICY,COEFFICIENT
from jmicro.phase5 import equal_state
from document_progress_trainer import committed_state
from probe_document_progress import scope,forecast,budget_eligible
from independent_map_science_protocol import validate_evaluation,summarize,original_quality
from review_matched_story_study import quality_gates


def science_budget(probe):
    if (probe.get('passed') is not True or probe.get('cumulative_GPU_ledger_closed') is not True
            or probe.get('science_budget_eligible') is not True or probe.get('paired38_stream_clocks_exact') is not True
            or probe.get('actual_parameter_counts') != dict(native=10001152,train_only=256,training=10001408)
            or probe.get('verification_optimizer_updates') != 94
            or probe.get('scientific_teacher_positions') != 0 or probe.get('TEST_opened') is not False
            or probe.get('DEV_opened') is not False or probe.get('Base_adopted') is not False
            or not 0 < probe['GPU_occupancy_seconds']
            or probe['cumulative_technical_GPU_seconds'] != scope()['prior_technical_GPU_seconds']+probe['GPU_occupancy_seconds']
            or probe['cumulative_total_GPU_seconds'] != scope()['prior_total_GPU_seconds']+probe['GPU_occupancy_seconds']):
        raise ValueError('Owned paired CUDA/native/cumulative evidence required')
    native = probe['control_native3_subchecks']
    fields = {'CE_loss','gradient_norm','token_digest','source_teachers','source_EOS','physical_input_tokens',
        'CE_input_tokens','original_body_bytes','draw_trace','lr','original_model_weights_exact',
        'sampler_exact','scheduler_exact','RNG_exact','original_Adam_coordinates_exact','control_head_zero'}
    if len(native) != 3 or any(set(row) != fields or any(value is not True for value in row.values()) for row in native):
        raise ValueError('All actual control/native3 numerical subchecks required')
    forecasts = {}
    for arm in ARMS:
        cap,a = probe['capacities'][arm],probe['arms'][arm]
        cache = a['active_cache']
        if (cap.get('passed') is not True or cap.get('shape') != [48,1024] or cap.get('optimizer_updates') != 0
                or cap.get('main_teachers') != 24576 or cap.get('scalar_labels') != 24576
                or cap.get('weights_RNG_unchanged') is not True or a.get('full_state_history_resume_exact') is not True
                or not a.get('verification6_snapshot',{}).get('sha256') or len(a.get('actual6_history',[])) != 6
                or cache.get('passed') is not True or cache.get('absolute_tolerance') != 3e-5
                or cache.get('relative_tolerance') != 2e-5 or len(cache.get('native_KV',[])) != 26
                or set(cache.get('subchecks',{})) != {'finite_logits','logits_within_original_tolerance',
                    'all_native_KV_within_original_tolerance','real_cache_length','positions_exact','validity_exact','RNG_unchanged'}
                or not all(cache['subchecks'].values())):
            raise ValueError('BOTH capacity/resume/actual6/all original raw cache checks required')
        if arm == 'document_progress' and any(r['head_gradient_abs_max_after_clip'] <= 0
                or r['head_weight_abs_max'] <= 0 for r in a['actual6_history']):
            raise ValueError('Actual dense scalar head learning proof required')
        forecasts[arm] = forecast(a['all32_timings'])
        if forecasts[arm] != a['scientific_forecast_seconds']:
            raise ValueError('All32 per-arm fixed25M teacher-normalized forecast changed')
    if (forecasts != probe['scientific_forecast_each_seconds']
            or sum(forecasts.values()) != probe['scientific_forecast_paired_seconds']
            or not budget_eligible(True,forecasts,probe['GPU_occupancy_seconds'])):
        raise ValueError('BOTH fixed science forecasts and EVERY spent second must fit original4800')
    return forecasts


def matched_original(candidate,control):
    keys = ('update','token_digest','supervised_tokens','source_teachers','source_EOS','CE_input_tokens',
        'physical_input_tokens','original_body_bytes','progress_label_positions','progress_zero_EOS_labels',
        'progress_source_labels','progress_target_sum','progress_target_digest')
    return {k:equal_state(candidate['counters'][k],control['counters'][k]) for k in keys} | {
        'full_original_sampler':equal_state(candidate['sampler'],control['sampler']),
        'actual_original_scheduler':equal_state(candidate['scheduler'],control['scheduler']),
        'RNG':equal_state(candidate['RNG'],control['RNG']),
        'native_model_config':candidate['model_config'] == control['model_config'],
        'declared_only_learning_objective_difference':candidate['spec']['progress_arm'] == 'document_progress'
            and control['spec']['progress_arm'] == 'native_CE_control'
            and candidate['spec']['progress_policy'] == control['spec']['progress_policy'] == POLICY}


def validate_history(rows,state):
    c = state['counters']
    if (not committed_state(state) or len(rows) != c['update']
            or [r['update'] for r in rows] != list(range(1,c['update']+1))
            or (rows and any(rows[-1][key] != value for key,value in c.items()))):
        raise ValueError('ALL completed typed native/head/Adam/source updates required')
    enabled = state['spec']['progress_arm'] == 'document_progress'
    previous_teachers = 0
    for r in rows:
        teachers = r['CE_targets_this_update']
        if (not all(math.isfinite(r[k]) for k in ('CE_loss','progress_loss','combined_loss','gradient_norm',
                'head_gradient_abs_max_after_clip','head_weight_abs_max','progress_target_sum_this_update','seconds'))
                or r['CE_loss'] < 0 or not 0 <= r['progress_loss'] <= 1 or r['seconds'] <= 0 or r['lr'] != 1e-5
                or not math.isclose(r['combined_loss'],r['CE_loss']+COEFFICIENT*(r['progress_loss'] if enabled else 0),rel_tol=1e-6,abs_tol=1e-6)
                or type(teachers) is not int or teachers <= 0 or r['supervised_tokens'] != previous_teachers+teachers
                or r['progress_labels_this_update'] != teachers
                or r['progress_learning_positions_this_update'] != (teachers if enabled else 0)
                or r['progress_label_positions'] != r['supervised_tokens']
                or r['progress_learning_positions'] != (r['supervised_tokens'] if enabled else 0)
                or r['progress_zero_EOS_labels'] != sum(r['source_EOS'].values())
                or r['progress_source_labels'] != r['source_teachers']
                or r['auxiliary_inputs_this_update'] != 0 or r['auxiliary_pairs_this_update'] != 0
                or r['physical_inputs_this_update'] < teachers
                or not 0 <= r['progress_target_sum_this_update'] <= teachers
                or (not enabled and (r['head_weight_abs_max'] != 0 or r['head_gradient_abs_max_after_clip'] != 0))):
            raise ValueError('Finite unchanged CE, actual main/scalar clocks and original source EOS required')
        previous_teachers = r['supervised_tokens']
    rollup = dict(main_teachers=sum(r['CE_targets_this_update'] for r in rows),
        scalar_learning_labels=sum(r['progress_learning_positions_this_update'] for r in rows),
        main_physical_inputs=sum(r['physical_inputs_this_update'] for r in rows))
    if (rollup['main_teachers'] != c['supervised_tokens'] or rollup['scalar_learning_labels'] != c['progress_learning_positions']
            or rollup['main_physical_inputs'] != c['physical_input_tokens']):
        raise ValueError('ALL history rollups and actual terminal counters must match')
    return rollup


def pilot_quality(control,cached,strong,historical,candidate,control_scores,cached_scores,strong_scores,candidate_scores):
    # Preserve all original native100M/strong/historical/absolute criteria and
    # additionally demand the SAME criteria against our own matched25M control.
    original = original_quality(cached,strong,historical,candidate,cached_scores,strong_scores,candidate_scores)
    paired = quality_gates(control,candidate,control_scores,candidate_scores,'matched_CE25M_vs_document_progress')
    return dict(matched25M=paired,original_all_guards=original,
        eligible_for_separately_defined_main_comparison=paired['passed'] and original['eligible'],
        Base_qualified=False,Base_adopted=False)
