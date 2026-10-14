"""Measured budgets, original rollups and unchanged pure quality gates."""
import copy
import math
from pathlib import Path
import sys
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from pseudo_repetition_science_protocol import science_budget, validate_history, original_quality
from test_pseudo_repetition_training import builders


def probe():
    rows = [dict(seconds=.05, CE_targets_this_update=5000) for _ in range(32)]
    budget = math.ceil(17698 / 32 * sum(r['seconds'] for r in rows) * 1.3 + 600)
    return dict(passed=True, all_state_and_history_resume_equal=True, actual_auxiliary_active=True,
        all32_timings=rows, GPU_occupancy_seconds=10., scientific_forecast_seconds=budget, science_budget_eligible=True)


def test_measured_budget_uses_exact_original_updates_all32_durations_and_reserve():
    p = probe()
    assert science_budget(p) == p['scientific_forecast_seconds']


@pytest.mark.parametrize('bad', ['failed', 'elapsed', 'rows', 'nan', 'forecast', 'overcap'])
def test_bad_technical_evidence_cannot_freeze_science(bad):
    p = probe()
    if bad == 'failed': p['passed'] = False
    elif bad == 'elapsed': p['GPU_occupancy_seconds'] = 181
    elif bad == 'rows': p['all32_timings'].pop()
    elif bad == 'nan': p['all32_timings'][0]['seconds'] = float('nan')
    elif bad == 'forecast': p['scientific_forecast_seconds'] += 1
    else:
        for row in p['all32_timings']: row['seconds'] = 1.
        p['scientific_forecast_seconds'] = 26600
    with pytest.raises(ValueError): science_budget(p)


def test_actual_completed_fixture_history_has_separate_physical_rollups(tmp_path):
    _, build = builders(tmp_path)
    trainer = build()
    rows = [trainer.step() for _ in range(3)]
    total = validate_history(rows, trainer.state_dict())
    assert total['CE_physical_inputs'] > 0 and total['auxiliary_physical_inputs'] > 0
    assert sum(total.values()) == trainer.counters['physical_input_tokens']


@pytest.mark.parametrize('bad', ['missing', 'physical'])
def test_incomplete_or_mismatched_update_history_rejected(tmp_path, bad):
    _, build = builders(tmp_path)
    trainer = build()
    rows = [trainer.step() for _ in range(2)]
    if bad == 'missing': rows.pop(0)
    else: rows[0]['CE_physical_inputs_this_update'] += 1
    with pytest.raises(ValueError): validate_history(rows, trainer.state_dict())


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
    import review_pseudo_repetition as reviewer
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
