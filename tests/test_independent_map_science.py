"""Measured budgets, original rollups and unchanged pure quality gates."""
import copy
import math
from pathlib import Path
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from independent_map_science_protocol import science_budget, validate_history, original_quality
from test_independent_map_training import builders


def probe():
    rows = [dict(seconds=.05, CE_targets_this_update=5000) for _ in range(32)]
    budget = math.ceil(17698 / 32 * sum(r['seconds'] for r in rows) * 1.3 + 600)
    disabled={key:True for key in ('CE_loss','gradient_norm','token_digest','source_teachers','source_EOS',
        'physical_input_tokens','CE_input_tokens','original_body_bytes','draw_trace','lr',
        'original_model_weights_exact','sampler_exact','scheduler_exact','RNG_exact','original_Adam_all_coordinates_exact')}
    disabled['different_Adam_names']=[]
    activity={f'model.layers.{i}.self_attn.{part}':dict(change=.001,Adam_moment_abs_max=.001,gradient_abs_max=.001)
        for i in range(13) for part in ('independent_raw','independent_down.weight','independent_q.weight','independent_k.weight')}
    return dict(passed=True,full_state_history_resume_exact=True,initial_native_function_parity=True,
        disabled3_original_numeric_state_and_stream_exact=True,disabled_native3_subchecks=[copy.deepcopy(disabled) for _ in range(3)],
        all52_new_tensors_active=activity,cumulative_GPU_ledger_closed=True,
        cumulative_technical_GPU_seconds=82.56365345604718,
        candidate_parameters=10067764,native_parameters=10001152,
        capacity=dict(passed=True,shape=[48,1024],optimizer_updates=0,physical_input_tokens=49152,teachers=24576),
        active_cache=dict(passed=True,subchecks={k:True for k in ('finite_logits','logits_within_original_tolerance',
            'secondary_K2_within_original_tolerance','positions_exact','validity_exact','RNG_unchanged')},absolute_tolerance=3e-5,relative_tolerance=2e-5),
        verification6_snapshot=dict(path='/fixture/6.pt',sha256='a'*64),all32_timings=rows,GPU_occupancy_seconds=10.,
        scientific_forecast_seconds=budget, science_budget_eligible=True)


def test_measured_budget_uses_exact_original_updates_all32_durations_and_reserve():
    p = probe()
    assert science_budget(p) == p['scientific_forecast_seconds']


@pytest.mark.parametrize('bad', ['failed', 'elapsed', 'rows', 'nan', 'forecast', 'overcap', 'count', 'cache'])
def test_bad_technical_evidence_cannot_freeze_science(bad):
    p = probe()
    if bad == 'failed': p['passed'] = False
    elif bad == 'elapsed': p['GPU_occupancy_seconds'] = 181
    elif bad == 'rows': p['all32_timings'].pop()
    elif bad == 'nan': p['all32_timings'][0]['seconds'] = float('nan')
    elif bad == 'forecast': p['scientific_forecast_seconds'] += 1
    elif bad == 'count': p['candidate_parameters'] = 10001152
    elif bad == 'cache': p['active_cache']['passed'] = False
    else:
        for row in p['all32_timings']: row['seconds'] = 1.
        p['scientific_forecast_seconds'] = 26600
    with pytest.raises(ValueError): science_budget(p)


def test_actual_completed_fixture_history_has_separate_physical_rollups(tmp_path):
    _, build = builders(tmp_path)
    trainer = build()
    rows = [trainer.step() for _ in range(3)]
    total = validate_history(rows, trainer.state_dict())
    assert total['CE_physical_inputs'] > 0 and total['auxiliary_physical_inputs'] == 0
    assert sum(total.values()) == trainer.counters['physical_input_tokens']


@pytest.mark.parametrize('bad', ['missing', 'physical'])
def test_incomplete_or_mismatched_update_history_rejected(tmp_path, bad):
    _, build = builders(tmp_path)
    trainer = build()
    rows = [trainer.step() for _ in range(2)]
    if bad == 'missing': rows.pop(0)
    else: rows[0]['physical_inputs_this_update'] += 1
    with pytest.raises(ValueError): validate_history(rows, trainer.state_dict())


def test_original_pairing_requires_exact_original_base_config_and_declared66612_coordinates(tmp_path):
    from independent_map_science_protocol import matched_original
    _, build = builders(tmp_path)
    candidate, control = build(), build(legacy=True)
    for _ in range(2):
        candidate.step()
        control.step()
    checks = matched_original(candidate.state_dict(), control.state_dict(), control.counters['physical_input_tokens'])
    assert all(checks.values())
    assert checks['unchanged_original_base_config'] and checks['only_declared_model_difference']


@pytest.mark.parametrize('bad', ['base_config', 'map'])
def test_undeclared_architecture_change_cannot_pass_as_original_pairing(tmp_path, bad):
    from independent_map_science_protocol import matched_original
    from natural_context_contrast_trainer import host
    _, build = builders(tmp_path)
    candidate, control = build(), build(legacy=True)
    state = host(candidate.state_dict())
    if bad == 'map':
        state['model_config']['independent_QK_map_research']['policy']['rank'] = 4
        with pytest.raises(ValueError): matched_original(state, control.state_dict(), 0)
    else:
        state['model_config']['intermediate_size'] += 8
        checks = matched_original(state, control.state_dict(), 0)
        assert checks['unchanged_original_base_config'] is False


def evaluations():
    rows = [dict(id=str(i), prefix='fixture', text='文章', stop_reason='stop_id') for i in range(80)]
    rates = dict(eos=80, repetition=0, empty=0, role_leak=0, unicode_failure=0)
    ev = dict(body=dict(bpb=1.), greedy_rates=rates, generation=dict(outputs=rows),
              diagnostics={task: dict(primary=dict(accuracy=dict(point=.5))) for task in ('semantics', 'jblimp', 'jcqa')})
    zero = {str(i): dict(grammar=2, relevance=2, coherence=0, completion=0) for i in range(80)}
    good = {str(i): dict(grammar=2, relevance=2, coherence=2, completion=1) for i in range(80)}
    history = copy.deepcopy(ev)
    history['greedy_rates']['eos'] = 0
    return ev, history, zero, good


def test_original_quality_is_pure_and_preserves_every_gate():
    ev, history, zero, good = evaluations()
    with patch.object(Path, 'open', side_effect=AssertionError('No data or TEST reads in pure quality')):
        result = original_quality(ev, ev, history, ev, zero, zero, good)
    assert result['eligible'] and all(result['absolute'].values()) and all(result['historical_Web'].values())


def test_matched_BPB_guard_keeps_original_stricter_stage_semantics():
    ev, history, zero, good = evaluations()
    candidate = copy.deepcopy(ev)
    candidate['body']['bpb'] = 1.001
    result = original_quality(ev, ev, history, candidate, zero, zero, good)
    assert result['matched']['checks']['BPB_gate'] is False
    assert result['strong']['checks']['BPB_gate'] is True
    assert result['eligible'] is False


def test_cached_reference_accepts_JSON_string_paths_without_legacy_reader(tmp_path, monkeypatch):
    import json
    import review_independent_map as reviewer
    from jmicro.experiment import sha256
    raw = tmp_path / 'known-dev-generation.json'
    notes = tmp_path / 'known-dev-notes.json'
    generation = dict(outputs=[])
    raw.write_text(json.dumps(generation))
    notes.write_text('{}')
    monkeypatch.setattr(reviewer, 'validate_body', lambda *a: None)
    monkeypatch.setattr(reviewer, 'validate_raw', lambda *a: None)
    monkeypatch.setattr(reviewer, 'notes_scores', lambda rows, n, pin: dict(verified_raw_hash=pin))
    result = reviewer.reference_content(dict(generation=generation, body={}), str(raw), str(notes), None, None)
    assert result == dict(verified_raw_hash=sha256(raw))


@pytest.mark.parametrize('bad',['prior_reset','missing_tensor','inactive_projection','disabled_missing_check',
    'initial_function','snapshot','cache_precision'])
def test_new_projection_native_control_and_cumulative_evidence_cannot_be_omitted(bad):
    p=probe()
    if bad=='prior_reset': p['cumulative_technical_GPU_seconds']=10.
    elif bad=='missing_tensor': p['all52_new_tensors_active'].pop(next(iter(p['all52_new_tensors_active'])))
    elif bad=='inactive_projection': next(iter(p['all52_new_tensors_active'].values()))['Adam_moment_abs_max']=0.
    elif bad=='disabled_missing_check': del p['disabled_native3_subchecks'][0]['original_Adam_all_coordinates_exact']
    elif bad=='initial_function': p['initial_native_function_parity']=False
    elif bad=='snapshot': p['verification6_snapshot']={}
    else: p['active_cache']['absolute_tolerance']=1e-3
    with pytest.raises(ValueError): science_budget(p)
