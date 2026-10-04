from types import SimpleNamespace
from pathlib import Path
import sys

import numpy as np
import pytest

from jmicro.eos_pilot import MixtureSampler, pilot_lr, spans
from jmicro.shards import BlockSampler

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_eos_short_pilot import sentence_complete


def view(body):
    return SimpleNamespace(tokens=np.tile([2, *body, 3], 40).astype('<u2'),
                           byte_lengths=np.array([0]*8+[1]*8))


def test_mixed_sampler_resume_replays_both_sources_and_eos_targets():
    web, short = view([8,8]), view([9,10])
    parent = BlockSampler(web,4,42).state_dict()
    sampler = MixtureSampler(web,short,4,42,[False,True,False,True],parent)
    for _ in range(2):
        x,y,_ = sampler.batch(2)
        assert int(y.eq(3).sum())==2 and not y.eq(2).any()
        assert int(y.eq(-100).sum())==2
    saved=sampler.state_dict()
    expected=[sampler.batch(2) for _ in range(2)]
    restored=MixtureSampler(web,short,4,42,[False,True,False,True],parent)
    restored.load_state_dict(saved)
    actual=[restored.batch(2) for _ in range(2)]
    for left,right in zip(expected,actual):
        assert np.array_equal(left[0].numpy(),right[0].numpy())
        assert np.array_equal(left[1].numpy(),right[1].numpy()) and left[2]==right[2]
    assert restored.state_dict()==sampler.state_dict()
    assert sampler.source_tokens=={'web':16,'short':16}
    assert sampler.source_eos=={'web':4,'short':4}
    with pytest.raises(ValueError):
        sampler.batch(2)


def test_changed_route_is_not_an_ordinary_resume():
    web,short=view([8,8]),view([9,10])
    parent=BlockSampler(web,4,42).state_dict()
    original=MixtureSampler(web,short,4,42,[False,True],parent)
    changed=MixtureSampler(web,short,4,42,[True,False],parent)
    with pytest.raises(ValueError):
        changed.load_state_dict(original.state_dict())


def test_document_boundaries_crossing_extraction_chunks_are_not_truncated():
    ids=np.array([2,8,9,3,2,8,3],dtype='<u2')
    starts,ends,previous=spans(ids[:3],0,-1)
    assert len(ends)==0 and previous==-1
    starts,ends,previous=spans(ids[3:5],3,previous)
    assert starts.tolist()==[0] and ends.tolist()==[3]
    starts,ends,previous=spans(ids[5:],5,previous)
    assert starts.tolist()==[4] and ends.tolist()==[6] and previous==6


def test_pilot_schedule_stable_then_decay_without_budget_extension():
    spec={'pilot_schedule':{'parent_update':100,'stable_updates':2,'decay_updates':2}}
    assert pilot_lr(spec,100)==1 and pilot_lr(spec,102)==1
    assert pilot_lr(spec,103)==pytest.approx(.55)
    assert pilot_lr(spec,104)==pytest.approx(.1) and pilot_lr(spec,110)==pytest.approx(.1)


def test_sentence_filter_rejects_obvious_source_truncation():
    for text in ('これはソーラー...', '続きは…', '本文……。', '本文。続きを読む。', '本文。Read more.'):
        assert not sentence_complete(text)
    for text in ('散歩に行きました。', '「終わりです。」', 'すべて完了しました！\n', 'This is complete.'):
        assert sentence_complete(text)
