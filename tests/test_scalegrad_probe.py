"""Fixed one-pass safety, full carried costs and old-control coordinate mapping."""
import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from probe_scalegrad import scope,assert_scope,forecast,eligible,original_match


def test_carried_technical_AND_completed_science_stay_in_original_total():
    c = scope()
    assert_scope(c)
    assert c['prior_total_GPU_seconds'] == c['prior_technical_GPU_seconds']+c['prior_completed_science_GPU_seconds']
    assert eligible(True,1000,1.)
    assert not eligible(False,1000,1.)
    assert not eligible(True,1737,1.)
    assert not eligible(True,1000,63.1)
    assert not eligible(True,599,1.)


@pytest.mark.parametrize('key,value',[
    ('prior_technical_GPU_seconds',0.),('prior_completed_science_GPU_seconds',0.),
    ('prior_total_GPU_seconds',116.9417824720731),('GPU_ceiling_seconds',181),
    ('maximum_cumulative_GPU_seconds',4801),('capacity_shape',[24,1024]),('retained_decoder_graphs',2),
    ('capacity_before_any_optimizer',False),('training_parameters',10001408),('train_only_parameters',256),
    ('timed_updates',31),('continuous_updates',3),('split_updates',[2,4]),
    ('disabled_native_updates',0),('cached_zero_head_control_updates',0),('main_teacher_goal',100000000),
    ('evaluation_save_reserve_seconds',599),('reuse_control_main_teachers',100000000),
    ('cached100M_is_matched25M_control',True),('TEST_prepared',True),('scientific_teacher_positions',1),('policy',{}),('gamma',.5),('decoder_forwards',2),
])
def test_no_geometry_graph_coefficient_teacher_control_or_budget_rescue(key,value):
    c = copy.deepcopy(scope())
    c[key] = value
    with pytest.raises(ValueError): assert_scope(c)


def test_forecast_uses_ALL32_actual_unique_main_teachers_including_slow_row():
    rows = [dict(seconds=.1,CE_targets_this_update=10000) for _ in range(32)]
    assert forecast(rows) == 925
    rows[-1]['seconds'] = 10.
    assert forecast(rows) == 1931
    assert not eligible(True,forecast(rows),1.)
    for bad in (rows[:-1],[dict(seconds=0.,CE_targets_this_update=1)]*32,
            [dict(seconds=float('nan'),CE_targets_this_update=1)]*32,
            [dict(seconds=.1,CE_targets_this_update=0)]*32,
            [dict(seconds=.1,CE_targets_this_update=1.)]*32):
        with pytest.raises(ValueError): forecast(bad)


def states():
    row = dict.fromkeys(('CE_loss','gradient_norm','token_digest','source_teachers','source_EOS',
        'physical_input_tokens','CE_input_tokens','original_body_bytes','draw_trace','lr'),0)
    state = dict(model={'x':torch.ones(1)},model_config={},sampler={},scheduler={},RNG={},counters=dict(update=3),
        optimizer=dict(param_groups=[dict(params=[0],lr=1e-5)],state={0:{'exp_avg':torch.ones(1),'step':torch.tensor(3.)}}))
    return row,state


def test_original_control_checks_every_native_Adam_coordinate_and_hyperparameter():
    row,a = states()
    b = copy.deepcopy(a)
    assert all(original_match(a,b,row,row).values())
    b['optimizer']['state'][0]['exp_avg'][0] += 1
    assert not original_match(a,b,row,row)['original_Adam_coordinates_exact']
    b = copy.deepcopy(a)
    b['optimizer']['param_groups'][0]['lr'] = 1e-4
    assert not original_match(a,b,row,row)['original_Adam_hyperparameters_exact']


def test_cached_control_EXTRA_zero_head_must_never_replace_original_coordinates():
    row,a = states()
    b = copy.deepcopy(a)
    b['progress_head'] = dict(weight=torch.zeros(1))
    b['counters']['progress_learning_positions'] = 0
    b['optimizer']['param_groups'][0]['params'].append(1)
    b['optimizer']['state'][1] = dict(exp_avg=torch.zeros(1),exp_avg_sq=torch.zeros(1),step=torch.tensor(3.))
    assert all(original_match(a,b,row,row).values())
    b['optimizer']['state'][1]['exp_avg'][0] = .1
    assert not original_match(a,b,row,row)['cached_protocol_head_Adam_zero']
    b['progress_head']['weight'][0] = .1
    assert not original_match(a,b,row,row)['cached_protocol_head_zero_no_learning']


@pytest.mark.parametrize('key',['model','sampler','scheduler','RNG','model_config'])
def test_native_state_or_source_differences_are_not_hidden(key):
    row,a = states()
    b = copy.deepcopy(a)
    if key == 'model': b['model']['x'][0] += 1
    else: b[key]['different'] = True
    assert not all(original_match(a,b,row,row).values())


def test_first_capacity_and_saved6_precede_Adam_and_cache_respectively():
    source = (Path(__file__).resolve().parents[1]/'scripts/probe_scalegrad.py').read_text()
    body = source.split('def run(pin):',1)[1]
    assert body.index("job['capacity'] = capacity") < body.index('rows.append(learn')
    assert body.index("trainer.save(RUN/'verification6_before_cache.pt')") < body.index('cache_gate(trainer.model,ids)')
    assert 'timings = [learn(trainer) for _ in range(32)]' in body
    cap = source.split('def capacity(',1)[1].split('def run(',1)[0]
    assert cap.count('right_padded_hidden(trainer.model,ids)') == 1
    assert cap.index('novelty = selected_novel_mask') < cap.index("losses['combined_loss'].backward()")
    assert 'optimizer.step' not in cap
