"""Check paired cost, raw cache failures and control comparison without CUDA."""
import copy
from pathlib import Path
import sys
from types import SimpleNamespace as Row

import pytest
import torch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from probe_document_progress import scope,assert_scope,forecast,budget_eligible,cache_observations,native_subchecks
from jmicro.document_progress import ARMS


def test_scope_and_carried_cost_not_reset_by_new_pilot():
    c = scope()
    assert_scope(c)
    assert c['prior_total_GPU_seconds'] == c['prior_technical_GPU_seconds']+c['prior_completed_science_GPU_seconds']
    a = dict.fromkeys(ARMS,1400)
    assert sum(a.values()) < 4800
    assert not budget_eligible(True,a,1.)
    assert budget_eligible(True,dict.fromkeys(ARMS,1000),1.)
    assert not budget_eligible(False,dict.fromkeys(ARMS,1000),1.)
    assert not budget_eligible(True,dict.fromkeys(ARMS,600),82.)
    assert not budget_eligible(True,{ARMS[0]:1000},1.)


@pytest.mark.parametrize('key,value',[
    ('prior_technical_GPU_seconds',0.),('prior_completed_science_GPU_seconds',0.),
    ('prior_total_GPU_seconds',98.4736015520757),('maximum_cumulative_GPU_seconds',4801),
    ('GPU_ceiling_seconds',181),('main_teacher_goal_each',100000000),('timed_updates_each',31),
    ('capacity_shape',[24,1024]),('capacity_before_any_optimizer',False),
    ('native_parameters',10001408),('training_parameters',10001152),
    ('evaluation_save_reserve_each_seconds',599),('new_matched_control_required',False),
    ('cached100M_is_matched25M_control',True),('control_native_updates',0),
    ('preserve_actual6_and_all_cache_subchecks',False),('scientific_teacher_positions',1),
    ('progress_policy',{}),('TEST_prepared',True),('arms',[ARMS[1]]),
])
def test_frozen_scope_rejects_geometry_target_budget_control_or_gate_rescue(key,value):
    c = copy.deepcopy(scope())
    c[key] = value
    with pytest.raises(ValueError): assert_scope(c)


def test_forecast_ALL32_teacher_normalized_and_two_full_reserves():
    rows = [dict(seconds=.1,CE_targets_this_update=10000) for _ in range(32)]
    assert forecast(rows) == 925
    costly = copy.deepcopy(rows)
    costly[-1]['seconds'] = 10.
    assert forecast(costly) == 1931
    assert not budget_eligible(True,dict.fromkeys(ARMS,forecast(costly)),1.)
    for bad in (rows[:-1],[dict(seconds=0.,CE_targets_this_update=1)]*32,
            [dict(seconds=float('nan'),CE_targets_this_update=1)]*32,
            [dict(seconds=.1,CE_targets_this_update=0)]*32,
            [dict(seconds=.1,CE_targets_this_update=1.)]*32):
        with pytest.raises(ValueError): forecast(bad)


def pair():
    def cache():
        return Row(layers=[(torch.zeros(1,2,4,8),torch.zeros(1,2,4,8))],
            valid=torch.ones(1,4,dtype=torch.bool),positions=torch.arange(4)[None])
    return Row(logits=torch.zeros(1,4,10),cache=cache()),Row(logits=torch.zeros(1,2,10),cache=cache())


def test_combined_cache_precision_and_bounded_raw_error_evidence():
    a,b = pair()
    a.logits[:,-2:] = 10
    b.logits[:] = 10.0001
    assert cache_observations(a,b,True)['passed']
    b.logits[:] = 11
    r = cache_observations(a,b,True)
    assert not r['passed'] and r['outside_original_logit_tolerance'] == 20
    assert len(r['first_eight_outside']) == 8
    assert len(r['native_KV']) == 2


@pytest.mark.parametrize('bad',['K','V','length','positions','valid','RNG'])
def test_every_cache_subcheck_retained(bad):
    a,b = pair()
    if bad == 'K': b.cache.layers[0][0][0,0,0,0] = .01
    elif bad == 'V': b.cache.layers[0][1][0,0,0,0] = .01
    elif bad == 'length':
        a.cache.layers = [(torch.zeros(1,2,5,8),torch.zeros(1,2,5,8))]
        b.cache.layers = copy.deepcopy(a.cache.layers)
    elif bad == 'positions': b.cache.positions[0,0] = 99
    elif bad == 'valid': b.cache.valid[0,0] = False
    r = cache_observations(a,b,bad != 'RNG')
    assert not r['passed'] and sum(not v for v in r['subchecks'].values()) == 1


def test_named_native_Adam_comparison_includes_every_coordinate_and_zero_head():
    row = dict.fromkeys(('CE_loss','gradient_norm','token_digest','source_teachers','source_EOS',
        'physical_input_tokens','CE_input_tokens','original_body_bytes','draw_trace','lr'),0)
    native = dict(model={'x':torch.ones(1)},sampler={},scheduler={},RNG={},
        optimizer=dict(param_groups=[dict(params=[0])],state={0:{'exp_avg':torch.ones(1)}}))
    control = copy.deepcopy(native)
    control['progress_head'] = dict(weight=torch.zeros(1))
    control['optimizer']['param_groups'][0]['params'].append(1)
    control['optimizer']['state'][1] = {'exp_avg':torch.zeros(1)}
    assert all(native_subchecks(control,native,row,row).values())
    control['optimizer']['state'][0]['exp_avg'][0] += 1
    assert not native_subchecks(control,native,row,row)['original_Adam_coordinates_exact']
    control['progress_head']['weight'][0] = .1
    assert not native_subchecks(control,native,row,row)['control_head_zero']


def test_workflow_uses_both_capacity_before_first_update_and_all32_each():
    # This ordering is a safety requirement; model/trainer correctness is
    # independently exercised by their real-autograd fixture suites.
    source = (Path(__file__).resolve().parents[1]/'scripts/probe_document_progress.py').read_text()
    run = source.split('def run(pin):',1)[1]
    assert run.index('capacities[arm] = capacity') < run.index('control_rows.append(learn')
    assert 'timings = [learn(trainer) for _ in range(32)]' in run
    assert run.index('trainer.save(snapshot)') < run.index("cache_gate(trainer.model,ids)")
    assert 'source' not in scope()['progress_policy']
