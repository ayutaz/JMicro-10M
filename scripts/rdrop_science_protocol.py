"""Reuse numerical proof, preserve old cost rejection, audit first RDrop science."""
import math
from jmicro.phase5 import equal_state
from jmicro.evaluation_boundary import require_digest
from rdrop_target_batch_trainer import committed_state
from document_progress_trainer import committed_state as control_committed
from probe_rdrop_target_batch import forecast,scope
from jmicro.rdrop_analytic import IMPLEMENTATION
from scalegrad_science_protocol import NATIVE_CHECKS
from pseudo_repetition_science_protocol import validate_evaluation,summarize,original_quality
from review_matched_story_study import quality_gates
import torch

STREAM_KEYS = ('update','token_digest','supervised_tokens','source_teachers','source_EOS',
    'CE_input_tokens','original_body_bytes','draw_trace','lr')


def science_budget(p,authorization):
    if (authorization.get('kind') != 'user_local_GPU_cumulative_time_ceiling_removed_20261016'
            or authorization.get('user_instruction') != '上限はないので無限に使っていいです'
            or authorization.get('prior_total_GPU_seconds') != 3633.252637067926
            or authorization.get('prior_technical_GPU_seconds') != 169.2456279549515
            or authorization.get('prior_completed_science_GPU_seconds') != 3464.0070091129746
            or authorization.get('old180_4800_are_historical_not_future_global_limits') is not True):
        raise ValueError('Explicit new user resource authorization and ALL prior cost required')
    cap,cache = p.get('capacity',{}),p.get('active_cache',{})
    checks = {'finite_losses','finite_nonzero_joint_gradient','two_stochastic_views',
        'positive_symmetric_KL','dropout_RNG_advanced','all_weights_unchanged','Adam_zero'}
    if (p.get('passed') is not True or p.get('cumulative_GPU_ledger_closed') is not True
            or p.get('science_budget_eligible') is not False
            or p.get('verification_optimizer_updates') != 59 or p.get('scientific_teacher_positions') != 0
            or p.get('DEV_opened') is not False or p.get('TEST_opened') is not False
            or p.get('native_parameters') != 10001152 or p.get('training_parameters') != 10001152
            or p.get('loss_runtime') != IMPLEMENTATION
            or p.get('cached25M_original_coordinate_protocol_exact') is not True
            or p.get('full_state_history_resume_exact') is not True
            or cap.get('passed') is not True or cap.get('shape') != [48,1024]
            or cap.get('retained_decoder_graphs') != 2 or cap.get('optimizer_updates') != 0
            or cap.get('main_teachers') != 24576 or cap.get('total_CE_evaluations') != 49152
            or cap.get('consistency_pairs') != 24576 or cap.get('total_physical_input_tokens') != 98304
            or set(cap.get('checks',{})) != checks or not all(cap['checks'].values())
            or cache.get('passed') is not True or cache.get('absolute_tolerance') != 3e-5
            or cache.get('relative_tolerance') != 2e-5
            or set(cache.get('subchecks',{})) != {'finite_logits','logits_within_original_tolerance',
                'all_native_KV_within_original_tolerance','real_cache_length','positions_exact','validity_exact','RNG_unchanged'}
            or not all(cache['subchecks'].values())):
        raise ValueError('Actual original two-graph capacity/resume/cache proof and old cost rejection required')
    for name,keys in (('native3_subchecks',NATIVE_CHECKS),('cached_zero_head_control3_subchecks',
            NATIVE_CHECKS|{'cached_protocol_head_zero_no_learning','cached_protocol_head_Adam_zero'})):
        rows = p.get(name,[])
        if len(rows) != 3 or any(set(r) != keys or not all(r.values()) for r in rows):
            raise ValueError('ALL native/cached25M original-coordinate checks required')
    reference = p.get('reference6_subchecks',{})
    if (set(reference) != {'ALL_numerical_state_exact','ALL_non_time_history_exact'}
            or not all(v is True for v in reference.values())
            or [r['update'] for r in p.get('actual6_history',[])] != list(range(1,7))):
        raise ValueError('Full six-update reference endpoint state/history and actual six rows required')
    for key in ('verification6_snapshot','analytic6_snapshot','reference6_snapshot'):
        if set(p.get(key,{})) != {'path','sha256'}:
            raise ValueError('Both original and actual6 snapshots must be retained')
        require_digest(p[key]['sha256'])
    old = scope()
    elapsed = p['GPU_occupancy_seconds']
    budget = forecast(p['all32_timings'])
    if (not math.isfinite(elapsed) or elapsed <= 0
            or p['cumulative_technical_GPU_seconds'] != old['prior_technical_GPU_seconds']+elapsed
            or p['prior_completed_science_GPU_seconds'] != old['prior_completed_science_GPU_seconds']
            or p['cumulative_total_GPU_seconds'] != old['prior_total_GPU_seconds']+elapsed
            or budget != p['scientific_forecast_seconds'] or budget != 1757):
        raise ValueError('Unchanged ALL32 forecast and original historical ledger required')
    return budget


def matched_original(candidate,control):
    group = control['optimizer']['param_groups'][0]
    head = control['optimizer']['state'].get(group['params'][-1])
    core = ('update','token_digest','supervised_tokens','source_teachers','source_EOS',
        'CE_input_tokens','original_body_bytes')
    return {k:equal_state(candidate['counters'][k],control['counters'][k]) for k in core} | {
        'full_original_sampler':equal_state(candidate['sampler'],control['sampler']),
        'original_scheduler':equal_state(candidate['scheduler'],control['scheduler']),
        'native_model_config':candidate['model_config'] == control['model_config'],
        'same_original_parent':candidate['binding']['parent'] == control['binding']['parent'],
        'main_physical_stream':candidate['counters']['main_physical_input_tokens'] == control['counters']['physical_input_tokens'],
        'genuine_zero_head_CE_control':control_committed(control) and control['spec']['progress_arm'] == 'native_CE_control'
            and not torch.count_nonzero(control['progress_head']['weight']) and head is not None
            and not torch.count_nonzero(head['exp_avg']) and not torch.count_nonzero(head['exp_avg_sq'])
            and float(head['step']) == control['counters']['update']}


def paired_history(candidate,control):
    if len(candidate) != len(control) or any(
            any(a[k] != b[k] for k in STREAM_KEYS)
            or a['main_physical_input_tokens'] != b['physical_input_tokens']
            for a,b in zip(candidate,control,strict=True)):
        raise ValueError('Every original main source/digest/physical/schedule row must match')
    return True


def validate_history(rows,state):
    c = state['counters']
    if (not committed_state(state) or len(rows) != c['update']
            or [r['update'] for r in rows] != list(range(1,c['update']+1))
            or (rows and any(rows[-1][k] != v for k,v in c.items()))):
        raise ValueError('ALL complete typed model/Adam/dropout RNG/source history required')
    enabled = state['spec']['rdrop_arm'] == 'normalized_rdrop'
    teachers = main_physical = 0
    for r in rows:
        n = r['CE_targets_this_update']
        ce = .5*(r['CE_view1_loss']+r['CE_view2_loss'])
        combined = r['CE_loss']+.5*r['symmetric_KL'] if enabled else r['CE_loss']
        if (not all(math.isfinite(r[k]) for k in ('CE_view1_loss','CE_view2_loss','CE_loss',
                'symmetric_KL','combined_loss','gradient_norm','seconds','data_wait_seconds'))
                or min(r['CE_loss'],r['gradient_norm']) < 0 or r['symmetric_KL'] < -1e-6
                or not math.isclose(r['CE_loss'],ce,rel_tol=1e-6,abs_tol=1e-6)
                or not math.isclose(r['combined_loss'],combined,rel_tol=1e-6,abs_tol=1e-6)
                or r['seconds'] <= 0 or r['data_wait_seconds'] < 0 or r['lr'] != 1e-5
                or type(n) is not int or n <= 0 or r['supervised_tokens'] != teachers+n
                or r['main_physical_input_tokens'] != main_physical+r['main_physical_inputs_this_update']
                or r['physical_input_tokens'] != r['main_physical_input_tokens']*(2 if enabled else 1)
                or r['second_view_physical_input_tokens'] != (r['main_physical_input_tokens'] if enabled else 0)
                or r['total_CE_teacher_evaluations'] != r['supervised_tokens']*(2 if enabled else 1)
                or r['second_view_gold_evaluations'] != (r['supervised_tokens'] if enabled else 0)
                or r['consistency_pairs'] != (r['supervised_tokens'] if enabled else 0)
                or r['second_view_gold_evaluations_this_update'] != (n if enabled else 0)
                or r['consistency_pairs_this_update'] != (n if enabled else 0)
                or r['physical_inputs_this_update'] != r['main_physical_inputs_this_update']*(2 if enabled else 1)
                or not 0 <= r['different_view_positions_this_update'] <= n
                or r['auxiliary_pairs_this_update'] != 0
                or not 1 <= r['original_windows_this_update'] <= state['spec']['batch']
                or not 1 <= r['maximum_CE_input_tokens_this_update'] <= 1024):
            raise ValueError('Original hardgold/two-view CE and consistency/physical clocks required')
        require_digest(r['token_digest'])
        teachers,main_physical = r['supervised_tokens'],r['main_physical_input_tokens']
    return dict(main_teachers=teachers,main_physical_inputs=main_physical,
        gold_evaluations=c['total_CE_teacher_evaluations'],consistency_pairs=c['consistency_pairs'],
        training_RNG='within-arm exact resume; intentionally not equal to deterministic control')


def pilot_quality(control,cached,strong,historical,candidate,control_scores,cached_scores,strong_scores,candidate_scores):
    original = original_quality(cached,strong,historical,candidate,cached_scores,strong_scores,candidate_scores)
    paired = quality_gates(control,candidate,control_scores,candidate_scores,'matched_CE25M_vs_RDrop')
    return dict(matched25M=paired,original_all_guards=original,
        eligible_for_separately_defined_main_comparison=paired['passed'] and original['eligible'],
        Base_qualified=False,Base_adopted=False)
