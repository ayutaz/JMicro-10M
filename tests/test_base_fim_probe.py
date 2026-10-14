"""Owned prospective scope and pre-CUDA one-shot barriers."""
import json
from pathlib import Path
import sys

import pytest
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'scripts')]
import probe_base_fim as probe


def proposal():
    return json.loads(probe.PROPOSAL.read_text())


@pytest.mark.parametrize('field,value', [('updates',9999),('original_teacher_positions',100000000),
    ('maximum_new_GPU_seconds_including_probe',7200),('probe_GPU_ceiling_seconds',180),
    ('schedule_total_teachers',100000000)])
def test_changed_scientific_scope_is_not_a_probe(field,value):
    p = proposal()
    p['pilot'][field] = value
    with pytest.raises(ValueError): probe.assert_contract(p)


def test_marker_or_optimizer_rescue_refused():
    p = proposal();probe.assert_contract(p)
    p['FIM_rule']['probability'] = .9
    with pytest.raises(ValueError):probe.assert_contract(p)
    p = proposal();p['optimizer']['peak_lr'] = .001
    with pytest.raises(ValueError):probe.assert_contract(p)


def test_existing_preparation_is_not_repeated(monkeypatch,tmp_path):
    monkeypatch.setenv('CUDA_VISIBLE_DEVICES','')
    path = tmp_path/'frozen.json';path.write_text('{}')
    monkeypatch.setattr(probe,'CONFIG',path)
    with pytest.raises(ValueError,match='one-shot'):probe.prepare()


def test_wrong_pin_rejected_before_other_references_or_CUDA(monkeypatch,tmp_path):
    path = tmp_path/'config.json';path.write_text('invalid_JSON')
    monkeypatch.setattr(probe,'CONFIG',path)
    with pytest.raises(ValueError,match='Pinned'):probe.inspect('0'*64)


def test_CPU_prepare_rejects_GPU_visibility_before_construction(monkeypatch):
    monkeypatch.setenv('CUDA_VISIBLE_DEVICES','0')
    with pytest.raises(ValueError,match='CPU preparation'):probe.prepare()
