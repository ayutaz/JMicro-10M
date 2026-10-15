"""Original25M/source/history accounting and unchanged Japanese Base gates."""
import math
import torch
from jmicro.phase5 import equal_state
from jmicro.evaluation_boundary import require_digest
from scalegrad_trainer import committed_state
from document_progress_trainer import committed_state as control_committed
from probe_scalegrad import scope,forecast,eligible
from pseudo_repetition_science_protocol import validate_evaluation,summarize,original_quality
from review_matched_story_study import quality_gates

NATIVE_CHECKS = {'CE_loss','gradient_norm','token_digest','source_teachers','source_EOS',
    'physical_input_tokens','CE_input_tokens','original_body_bytes','draw_trace','lr',
    'model_config_exact','original_weights_exact','sampler_exact','scheduler_exact','RNG_exact',
    'original_Adam_coordinates_exact','original_Adam_hyperparameters_exact'}
STREAM_KEYS = ('update','token_digest','supervised_tokens','source_teachers','source_EOS',
    'CE_input_tokens','physical_input_tokens','original_body_bytes','draw_trace','lr')


def science_budget(p):
    s = scope()
    cache = p.get('active_cache',{})
    cap = p.get('capacity',{})
    if (p.get('passed') is not True or p.get('cumulative_GPU_ledger_closed') is not True
            or p.get('science_budget_eligible') is not True or p.get('verification_optimizer_updates') != 53
            or p.get('scientific_teacher_positions') != 0 or p.get('DEV_opened') is not False
            or p.get('TEST_opened') is not False or p.get('native_parameters') != 10001152
            or p.get('training_parameters') != 10001152 or p.get('cached25M_original_coordinate_protocol_exact') is not True
            or p.get('full_state_history_resume_exact') is not True
            or set(p.get('verification6_snapshot',{})) != {'path','sha256'}
            or cap.get('passed') is not True or cap.get('shape') != [48,1024]
            or cap.get('retained_decoder_graphs') != 1 or cap.get('optimizer_updates') != 0
            or cap.get('main_teachers') != 24576 or cap.get('total_physical_input_tokens') != 49152
            or set(cap.get('checks',{})) != {'finite_losses','finite_nonzero_gradient','active_loss_changes',
                'novel_and_seen_candidates','RNG_unchanged','all_weights_unchanged','Adam_zero'}
            or not all(cap['checks'].values()) or cache.get('passed') is not True
            or cache.get('absolute_tolerance') != 3e-5 or cache.get('relative_tolerance') != 2e-5
            or set(cache.get('subchecks',{})) != {'finite_logits','logits_within_original_tolerance',
                'all_native_KV_within_original_tolerance','real_cache_length','positions_exact','validity_exact','RNG_unchanged'}
            or not all(cache['subchecks'].values())):
        raise ValueError('Actual owned one-pass capacity/protocol/resume/saved6/cache evidence required')
    for name,keys in (('native3_subchecks',NATIVE_CHECKS),('cached_zero_head_control3_subchecks',
            NATIVE_CHECKS|{'cached_protocol_head_zero_no_learning','cached_protocol_head_Adam_zero'})):
        rows = p.get(name,[])
        if len(rows) != 3 or any(set(r) != keys or not all(r.values()) for r in rows):
            raise ValueError('ALL original native/cached25M coordinate subchecks required')
    elapsed = p['GPU_occupancy_seconds']
    budget = forecast(p['all32_timings'])
    if (not math.isfinite(elapsed) or elapsed <= 0
            or p['cumulative_technical_GPU_seconds'] != s['prior_technical_GPU_seconds']+elapsed
            or p['prior_completed_science_GPU_seconds'] != s['prior_completed_science_GPU_seconds']
            or p['cumulative_total_GPU_seconds'] != s['prior_total_GPU_seconds']+elapsed
            or budget != p['scientific_forecast_seconds'] or not eligible(True,budget,elapsed)):
        raise ValueError('ALL32 fixed25M+600 forecast and EVERY old/new GPU second must fit original180/4800')
    require_digest(p['verification6_snapshot']['sha256'])
    return budget


def matched_original(candidate,control):
    group = control['optimizer']['param_groups'][0]
    head = control['optimizer']['state'][group['params'][-1]]
    keys = STREAM_KEYS[:-2]
    return {k:equal_state(candidate['counters'][k],control['counters'][k]) for k in keys} | {
        'full_original_sampler':equal_state(candidate['sampler'],control['sampler']),
        'original_scheduler':equal_state(candidate['scheduler'],control['scheduler']),
        'original_RNG':equal_state(candidate['RNG'],control['RNG']),
        'native_model_config':candidate['model_config'] == control['model_config'],
        'same_original_parent':candidate['binding']['parent'] == control['binding']['parent'],
        'genuine_zero_head_CE_control':control_committed(control) and control['spec']['progress_arm'] == 'native_CE_control'
            and not torch.count_nonzero(control['progress_head']['weight'])
            and not torch.count_nonzero(head['exp_avg']) and not torch.count_nonzero(head['exp_avg_sq'])
            and float(head['step']) == control['counters']['update']}


def paired_history(candidate,control):
    if len(candidate) != len(control) or any(a[k] != b[k]
            for a,b in zip(candidate,control,strict=True) for k in STREAM_KEYS):
        raise ValueError('Every actual candidate/control original source/digest/physical/schedule row must match')
    return True


def validate_history(rows,state):
    c = state['counters']
    if (not committed_state(state) or len(rows) != c['update']
            or [r['update'] for r in rows] != list(range(1,c['update']+1))
            or (rows and any(rows[-1][k] != v for k,v in c.items()))):
        raise ValueError('ALL completed typed model/Adam/RNG/source/novelty updates required')
    enabled = state['spec']['scalegrad_arm'] == 'scalegrad'
    teachers = physical = novel = eos = 0
    for r in rows:
        n = r['CE_targets_this_update']
        if (not all(math.isfinite(r[k]) for k in ('CE_loss','ScaleGrad_loss','combined_loss','gradient_norm','seconds','data_wait_seconds'))
                or min(r['CE_loss'],r['ScaleGrad_loss'],r['gradient_norm']) < 0
                or r['seconds'] <= 0 or r['data_wait_seconds'] < 0 or r['lr'] != 1e-5
                or r['combined_loss'] != r['ScaleGrad_loss'] or (not enabled and r['combined_loss'] != r['CE_loss'])
                or type(n) is not int or n <= 0 or r['supervised_tokens'] != teachers+n
                or r['physical_input_tokens'] != physical+r['physical_inputs_this_update']
                or r['original_CE_metric_evaluations'] != r['supervised_tokens']
                or r['modified_loss_evaluations'] != (r['supervised_tokens'] if enabled else 0)
                or r['total_CE_evaluations'] != r['supervised_tokens']*(2 if enabled else 1)
                or not 0 <= r['novel_EOS_gold_positions_this_update'] <= r['novel_gold_positions_this_update'] <= n
                or r['novel_gold_positions'] != novel+r['novel_gold_positions_this_update']
                or r['novel_EOS_gold_positions'] != eos+r['novel_EOS_gold_positions_this_update']
                or r['novel_gold_positions'] != r['novel_body_gold_positions']+r['novel_EOS_gold_positions']
                or r['novel_EOS_gold_positions'] != sum(r['source_EOS'].values())
                or r['decoder_forwards_this_update'] != 1 or r['auxiliary_inputs_this_update'] != 0
                or r['auxiliary_pairs_this_update'] != 0 or r['physical_inputs_this_update'] < n
                or not 1 <= r['original_windows_this_update'] <= state['spec']['batch']
                or not 1 <= r['maximum_CE_input_tokens_this_update'] <= 1024):
            raise ValueError('Finite one-pass objective/metric and every original/novelty clock required')
        require_digest(r['token_digest'])
        teachers,physical,novel,eos = (r[k] for k in ('supervised_tokens','physical_input_tokens',
            'novel_gold_positions','novel_EOS_gold_positions'))
    return dict(main_teachers=teachers,main_physical_inputs=physical,novel_gold_positions=novel,
        novel_EOS_gold_positions=eos,modified_learning_evaluations=c['modified_loss_evaluations'],
        original_CE_metric_evaluations=c['original_CE_metric_evaluations'])


def pilot_quality(control,cached,strong,historical,candidate,control_scores,cached_scores,strong_scores,candidate_scores):
    original = original_quality(cached,strong,historical,candidate,cached_scores,strong_scores,candidate_scores)
    paired = quality_gates(control,candidate,control_scores,candidate_scores,'matched_CE25M_vs_ScaleGrad')
    return dict(matched25M=paired,original_all_guards=original,
        eligible_for_separately_defined_main_comparison=paired['passed'] and original['eligible'],
        Base_qualified=False,Base_adopted=False)
