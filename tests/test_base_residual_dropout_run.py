"""Guard duplicate GPU launches and matched CE compute/stream accounting."""
import copy
import json
from pathlib import Path
import sys

import pytest

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'scripts')]
import run_base_residual_dropout as runner


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value))


def test_terminal_probe_label_cannot_bypass_live_actual_process(tmp_path, monkeypatch):
    monkeypatch.setattr(runner, 'ROOT', tmp_path)
    monkeypatch.setattr(runner, 'CONFIG', tmp_path / 'new.json')
    monkeypatch.setattr(runner, 'PROBE', tmp_path / 'probe')
    monkeypatch.setattr(runner, 'alive', lambda _: True)
    write(tmp_path / 'probe/job.json', {'status': 'complete'})
    write(tmp_path / 'probe/result.json', {'passed': True})
    write(tmp_path / 'configs/phase6/base_residual_dropout_probe.json', {})
    with pytest.raises(ValueError, match='Actual completed'):
        runner.freeze()
    assert not runner.CONFIG.exists()


def test_live_science_rejected_before_UI_or_reference_access(tmp_path, monkeypatch):
    monkeypatch.setattr(runner, 'CONFIG', tmp_path / 'config.json')
    monkeypatch.setattr(runner, 'RUN', tmp_path / 'run')
    monkeypatch.setattr(runner, 'alive', lambda _: True)
    write(runner.CONFIG, {})
    write(runner.RUN / 'job.json', {'status': 'running'})
    with pytest.raises(ValueError, match='already alive'):
        runner.inspect()


def test_same_stream_requires_physical_compute_and_entire_sampler():
    counts = dict(update=3, token_digest='bound', supervised_tokens=100,
                  source_teachers={'web': 100}, source_EOS={'web': 2},
                  CE_input_tokens=110, original_body_bytes=300,
                  auxiliary_input_tokens=0, auxiliary_pairs=0, physical_input_tokens=180)
    baseline = dict(counters=counts, sampler=dict(cursor=9, RNG=[1, 2, 3]))
    assert all(runner.matched_control_checks(baseline, baseline).values())
    changed = copy.deepcopy(baseline)
    changed['counters']['physical_input_tokens'] += 1
    assert not runner.matched_control_checks(changed, baseline)['physical_input_tokens']
    changed = copy.deepcopy(baseline)
    changed['sampler']['RNG'][-1] += 1
    assert not runner.matched_control_checks(changed, baseline)['full_sampler']
