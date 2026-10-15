"""Actual owned evidence, real Adam histories and fixed quality advancement."""
import copy
import json
from pathlib import Path
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import document_progress_science_protocol as protocol
from natural_context_contrast_trainer import host
from test_document_progress_training import builders


def actual_probe():
    return json.loads((ROOT/'reports/phase6/document-progress-probe-20261015/result.json').read_text())


def test_actual_owned_pair_gives_both_forecasts_and_all_prior_cost():
    probe = actual_probe()
    assert protocol.science_budget(probe) == dict(native_CE_control=1396,document_progress=1089)
    assert sum(protocol.science_budget(probe).values())+probe['cumulative_total_GPU_seconds'] < 4800
    del probe['control_native3_subchecks'][0]['CE_loss']
    with pytest.raises(ValueError): protocol.science_budget(probe)


@pytest.mark.parametrize('bad',['passed','ledger','eligible','paired','count','updates','teachers','TEST','DEV',
    'capshape','capadam','caplabels','cache','cache_tol','resume','snapshot','timings','forecast','cost'])
def test_own_CUDA_evidence_cannot_be_omitted_or_rebudgeted(bad):
    p = actual_probe()
    arm = 'document_progress'
    if bad == 'passed': p['passed'] = False
    elif bad == 'ledger': p['cumulative_GPU_ledger_closed'] = False
    elif bad == 'eligible': p['science_budget_eligible'] = False
    elif bad == 'paired': p['paired38_stream_clocks_exact'] = False
    elif bad == 'count': p['actual_parameter_counts']['train_only'] = 0
    elif bad == 'updates': p['verification_optimizer_updates'] = 50
    elif bad == 'teachers': p['scientific_teacher_positions'] = 1
    elif bad == 'TEST': p['TEST_opened'] = True
    elif bad == 'DEV': p['DEV_opened'] = True
    elif bad == 'capshape': p['capacities'][arm]['shape'] = [48,512]
    elif bad == 'capadam': p['capacities'][arm]['optimizer_updates'] = 1
    elif bad == 'caplabels': p['capacities'][arm]['scalar_labels'] = 0
    elif bad == 'cache': p['arms'][arm]['active_cache']['passed'] = False
    elif bad == 'cache_tol': p['arms'][arm]['active_cache']['absolute_tolerance'] = .1
    elif bad == 'resume': p['arms'][arm]['full_state_history_resume_exact'] = False
    elif bad == 'snapshot': p['arms'][arm]['verification6_snapshot'] = {}
    elif bad == 'timings': p['arms'][arm]['all32_timings'].pop()
    elif bad == 'forecast': p['arms'][arm]['scientific_forecast_seconds'] -= 600
    else: p['cumulative_total_GPU_seconds'] = p['cumulative_technical_GPU_seconds']
    with pytest.raises(ValueError): protocol.science_budget(p)


def test_real_both_Adam_histories_all_scalar_and_main_clocks_match(tmp_path):
    _,build = builders(tmp_path)
    states = {}
    for arm in ('native_CE_control','document_progress'):
        trainer = build(arm)
        rows = [trainer.step() for _ in range(6)]
        state = host(trainer.state_dict())
        rollup = protocol.validate_history(rows,state)
        assert rollup['main_teachers'] == state['counters']['supervised_tokens']
        assert rollup['scalar_learning_labels'] == (rollup['main_teachers'] if arm == 'document_progress' else 0)
        states[arm] = state
    assert all(protocol.matched_original(states['document_progress'],states['native_CE_control']).values())
    states['document_progress']['counters']['progress_target_digest'] = '0'*64
    assert not protocol.matched_original(states['document_progress'],states['native_CE_control'])['progress_target_digest']


@pytest.mark.parametrize('bad',['loss','combined','labels','source','nonfinite','physical'])
def test_earlier_history_corruption_rejected_even_with_unchanged_terminal_state(tmp_path,bad):
    _,build = builders(tmp_path)
    trainer = build()
    rows = [trainer.step() for _ in range(3)]
    state = host(trainer.state_dict())
    if bad == 'loss': rows[0]['progress_loss'] = 2.
    elif bad == 'combined': rows[0]['combined_loss'] += 1.
    elif bad == 'labels': rows[0]['progress_labels_this_update'] += 1
    elif bad == 'source': rows[0]['progress_source_labels']['web'] += 1
    elif bad == 'nonfinite': rows[0]['head_weight_abs_max'] = float('nan')
    else: rows[0]['physical_inputs_this_update'] = 0
    with pytest.raises(ValueError): protocol.validate_history(rows,state)


def test_pilot_requires_both_matched25M_and_all_original_guards_and_never_adopts(monkeypatch):
    calls = []
    def matched(*args):
        calls.append(args[-1])
        return dict(passed=False)
    monkeypatch.setattr(protocol,'quality_gates',matched)
    monkeypatch.setattr(protocol,'original_quality',lambda *args:dict(eligible=True))
    args = [dict() for _ in range(9)]
    result = protocol.pilot_quality(*args)
    assert not result['eligible_for_separately_defined_main_comparison']
    assert calls == ['matched_CE25M_vs_document_progress']
    monkeypatch.setattr(protocol,'quality_gates',lambda *args:dict(passed=True))
    assert protocol.pilot_quality(*args)['eligible_for_separately_defined_main_comparison']
    monkeypatch.setattr(protocol,'original_quality',lambda *args:dict(eligible=False))
    result = protocol.pilot_quality(*args)
    assert not result['eligible_for_separately_defined_main_comparison']
    assert result['Base_qualified'] is result['Base_adopted'] is False
