"""Budget/stream/review integrity for the new durable native comparison."""
import copy
import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from run_base_ademamix import science_budget, matched_control_checks, inspect, RUN
from review_base_ademamix import audit_state
from base_ademamix_trainer import KIND, OPT_KIND, POLICY


def measured():
    return dict(all32_step_seconds=2., all32_original_gold=100000, GPU_occupancy_seconds=15,
                science_budget_seconds=3500, science_budget_eligible=True)


def test_all_step_sum_and_gold_determine_forecast_not_fastest_subset():
    assert science_budget(measured()) == 3500
    changed = measured() | {'all32_step_seconds': 3.}
    with pytest.raises(ValueError): science_budget(changed)


@pytest.mark.parametrize('field,value', [
    ('all32_step_seconds', 0), ('all32_step_seconds', float('nan')),
    ('all32_original_gold', 0), ('all32_original_gold', 100000.),
    ('GPU_occupancy_seconds', 181), ('science_budget_seconds', 3501),
    ('science_budget_eligible', False), ('all32_step_seconds', 5.)])
def test_invalid_measurement_caps_or_recomputed_budget_refused(field, value):
    with pytest.raises(ValueError): science_budget(measured() | {field: value})


def test_same_teacher_count_cannot_hide_changed_rng_masks_stream_or_pending():
    counters = dict(update=4, token_digest='same-mask-and-source', supervised_tokens=100,
        source_teachers=dict(web=75, textbook=20, story=5), source_EOS=dict(web=1, textbook=1, story=1),
        CE_input_tokens=110, original_body_bytes=200, auxiliary_input_tokens=0,
        auxiliary_pairs=0, physical_input_tokens=200)
    record = dict(counters=counters, sampler=dict(RNG=[1,2,3], pending=dict(web=[1], textbook=[], story=[])))
    assert all(matched_control_checks(record, record).values())
    changed = copy.deepcopy(record); changed['counters']['token_digest'] = 'different-mask'
    assert not all(matched_control_checks(record, changed).values())
    changed = copy.deepcopy(record); changed['sampler']['pending']['web'] = [2]
    assert not matched_control_checks(record, changed)['full_sampler']


def test_native_review_rejects_unfinished_actual_teacher_budget():
    state = dict(kind=KIND, binding={'fixture':True},
        spec=dict(optimizer_policy=OPT_KIND, optimizer_recipe=POLICY, batch=48, seed=42, contrast=False),
        model_config=dict(expected_parameter_count=10001152),
        counters=dict(update=4, supervised_tokens=25, source_teachers={'web':25}),
        optimizer=dict(completed_steps=4), sampler=dict(consumed={'web':25}),
        lineage=dict(parent={'fixture':True}))
    with pytest.raises(ValueError):
        audit_state(state, dict(binding={'fixture':True}), dict(goals={'web':100000000}))


def test_finished_result_cannot_be_restarted(monkeypatch, tmp_path):
    import run_base_ademamix as run
    config = tmp_path / 'config.json'; config.write_text('{}')
    folder = tmp_path / 'science'; folder.mkdir(); (folder / 'result.json').write_text('{}')
    monkeypatch.setattr(run, 'CONFIG', config); monkeypatch.setattr(run, 'RUN', folder)
    with pytest.raises(ValueError, match='finished science'): inspect()
