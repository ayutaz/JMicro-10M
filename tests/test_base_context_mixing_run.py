import copy
from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_base_context_mixing import science_budget, matched_control_checks


def test_measured_speed_requires_fixed_total_budget_and_positive_finite_values():
    valid=dict(median_original_teachers_per_second=50000,GPU_occupancy_seconds=15,
               science_budget_seconds=3500,science_budget_eligible=True)
    assert science_budget(valid)==3500
    for speed in (0,-1,float('nan'),float('inf'),10000):
        bad=valid|{'median_original_teachers_per_second':speed}
        with pytest.raises(ValueError): science_budget(bad)


@pytest.mark.parametrize('field', ['science_budget_seconds','science_budget_eligible','GPU_occupancy_seconds'])
def test_forecast_altered_or_probe_unbounded_rejected(field):
    row=dict(median_original_teachers_per_second=50000,GPU_occupancy_seconds=15,
             science_budget_seconds=3500,science_budget_eligible=True)
    row[field]={'science_budget_seconds':3501,'science_budget_eligible':False,'GPU_occupancy_seconds':181}[field]
    with pytest.raises(ValueError): science_budget(row)


def test_matching_teachers_alone_does_not_hide_changed_digest_or_sampler():
    counters=dict(update=4,token_digest='exact',supervised_tokens=100,source_teachers={'web':75,'textbook':20,'story':5},
        source_EOS={'web':1,'textbook':1,'story':1},CE_input_tokens=110,original_body_bytes=200,
        auxiliary_input_tokens=0,auxiliary_pairs=0,physical_input_tokens=200)
    record=dict(counters=counters,sampler={'consumed':counters['source_teachers'],'RNG':[1,2,3],'pending':[]})
    assert all(matched_control_checks(record,record).values())
    for key in ('token_digest','supervised_tokens'):
        changed=copy.deepcopy(record); changed['counters'][key]='changed'
        assert not all(matched_control_checks(record,changed).values())
    changed=copy.deepcopy(record); changed['sampler']['RNG'].reverse()
    assert not matched_control_checks(record,changed)['full_sampler']


def test_slow_fixed100M_forecast_cannot_expand_the_7200_second_cap():
    # 25k/s fits; 20k/s cannot fit the predeclared two-forward budget.
    from math import ceil
    for speed, allowed in ((25000,True),(20000,False)):
        row=dict(median_original_teachers_per_second=speed,GPU_occupancy_seconds=15,
            science_budget_seconds=ceil(100000000/speed*1.3+900),science_budget_eligible=allowed)
        if allowed: assert science_budget(row)==6100
        else:
            with pytest.raises(ValueError): science_budget(row)


def test_committed_native_state_requires_mixing_optimizer_and_sampler_agreement(tmp_path):
    from base_context_mixing_state import finite_context_mixing_state
    from test_base_context_mixing_trainer import builders
    from natural_context_contrast_trainer import host
    _,build=builders(tmp_path)
    t=build(); t.step(); state=host(t.state_dict())
    assert finite_context_mixing_state(state)
    for key in ('updates','changed_positions'):
        broken=copy.deepcopy(state); broken['context_mixing'][key]=-1
        assert not finite_context_mixing_state(broken)
    broken=copy.deepcopy(state); broken['sampler']['consumed']['web']+=1
    assert not finite_context_mixing_state(broken)
    broken=copy.deepcopy(state); next(iter(broken['optimizer']['state'].values()))['step']+=1
    assert not finite_context_mixing_state(broken)


def test_worst_shape_uses_only_original_TRAIN_targets_and_cannot_repeat():
    from base_context_mixing_state import CapacitySampler
    from test_natural_context_contrast_corpus import FixtureCodec
    window=dict(input_ids=[2]+[65]*1023,target_ids=[-100]*512+[65]*511+[3],
        target_first=513,target_end=1025,input_start=0)
    payload=dict(window=window,original_record=dict(source='textbook',split='train'),
        index_byte_position=123,index_record_sha256='accepted-fixture')
    sampler=CapacitySampler(payload,FixtureCodec(),48)
    rows=sampler.take(48)
    assert sampler.consumed==dict(web=0,textbook=24576,story=0)
    assert all(r['input_ids']==window['input_ids'] and r['target_ids']==window['target_ids'] for r in rows)
    assert sum(r['original_EOS_targets'] for r in rows)==48
    assert sum(r['teacher_body_bytes'] for r in rows)==48*511
    with pytest.raises(ValueError,match='One worst-shape'): sampler.take(48)
    broken=copy.deepcopy(payload); broken['original_record']['split']='dev'
    with pytest.raises(ValueError,match='TRAIN genre'): CapacitySampler(broken,FixtureCodec(),48)
