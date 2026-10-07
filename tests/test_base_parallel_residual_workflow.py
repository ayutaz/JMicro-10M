"""Prospective2B forecasts, fixed ceilings and full original stream refusals."""
import copy
import json
import math
from pathlib import Path
import sys
import pytest
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'scripts')]
from probe_base_parallel_residual import forecast, paired_budget, source_checks, validate_contract


def arms(seconds=4, gold=300000):
    return {a: dict(total_seconds=seconds, total_original_gold=gold)
            for a in ('sequential', 'parallel')}


def test_all32_sum_uses_each2B_and_both_arms_plus_own_probe():
    sample = arms()
    sample['parallel']['total_seconds'] = 5
    budgets, eligible = paired_budget(sample, 20)
    assert budgets == dict(sequential=math.ceil(2000000000*4/300000*1.3+900),
                           parallel=math.ceil(2000000000*5/300000*1.3+900))
    assert eligible
    budgets, eligible = paired_budget(arms(6), 20)
    assert sum(budgets.values()) + 20 > 86400 and not eligible


@pytest.mark.parametrize('seconds,gold', [(0, 1), (-1, 2), (float('nan'), 2),
                                       (float('inf'), 2), (1, 0), (1, True)])
def test_invalid_sum_refused(seconds, gold):
    with pytest.raises(ValueError):
        forecast(seconds, gold)


@pytest.mark.parametrize('elapsed', [0, 181, float('nan')])
def test_own_probe_ceiling_not_waived(elapsed):
    with pytest.raises(ValueError):
        paired_budget(arms(), elapsed)


def test_new_sequential_control_required():
    sample = arms()
    del sample['sequential']
    with pytest.raises(ValueError):
        paired_budget(sample, 5)


def test_full_sampler_and_original_counter_and_schedule_compared():
    left = dict(counters=dict(supervised_tokens=10, token_digest='abc', source_EOS=dict(web=1)),
                sampler=dict(prefix=[1], RNG=[2]), scheduler=dict(tokens=10, last_lr=.002))
    right = copy.deepcopy(left)
    assert all(source_checks(left, right).values())
    right['sampler']['prefix'] = [3]
    assert not source_checks(left, right)['full_sampler']
    right['counters']['source_EOS']['web'] = 2
    assert not source_checks(left, right)['full_counters']
    right['scheduler']['tokens'] = 11
    assert not source_checks(left, right)['full_scheduler']


@pytest.mark.parametrize('field', ['gold', 'source', 'model', 'cap', 'batch'])
def test_prospective_recipe_cannot_change(field):
    root = Path(__file__).resolve().parents[1]
    p = json.loads((root / 'reports/phase6/base_parallel_residual_proposal.json').read_text())
    validate_contract(p)
    if field == 'gold':
        p['original_gold_each'] = 300000000
    elif field == 'source':
        p['goals']['web'] -= 1
    elif field == 'model':
        p['variants']['parallel']['parallel_residual_research']['policy']['residual_gain'] = .5
    elif field == 'cap':
        p['resource']['total_GPU_cap_seconds'] += 1
    elif field == 'batch':
        p['optimizer']['batch'] = 48
    with pytest.raises(ValueError):
        validate_contract(p)
