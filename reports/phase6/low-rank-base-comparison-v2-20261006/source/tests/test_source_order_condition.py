import copy
import hashlib
import sys
import numpy as np
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
from source_order_condition_trainer import SourceOrderQuotaSampler,SOURCE_ORDER
from original_web_retention_trainer import OriginalWebQuotaSampler
from test_original_web_retention_trainer import setup
from run_eos_short_pilot import equal_state


@pytest.mark.parametrize('goals',[dict(web=83,story=31,ordinary_textbook=29,conditional_textbook=37),
    dict(web=19,story=11,ordinary_textbook=7,conditional_textbook=16)])
def test_order_changes_but_all_actual_per_source_blocks_and_terminal_state_match(tmp_path,goals):
    pool,parent,_,positive=setup(tmp_path)
    def build(kind):return kind(pool,pool,positive,parent['sampler'],goals,8)
    def trace(sampler):
        hashes={g:hashlib.sha256() for g in SOURCE_ORDER};order=[]
        for source in SOURCE_ORDER:
            original=sampler.streams[source].block
            def wrapped(context,source=source,original=original):
                row=original(context);order.append(source)
                for array in row:hashes[source].update(np.asarray(array).tobytes())
                return row
            sampler.streams[source].block=wrapped
        while sampler.source_teachers!=goals:sampler.batch(3)
        return {g:h.hexdigest() for g,h in hashes.items()},order
    mixed,staged=build(OriginalWebQuotaSampler),build(SourceOrderQuotaSampler)
    a,b=trace(mixed),trace(staged)
    assert a[0]==b[0] and a[1]!=b[1]
    for key in ('source_teachers','source_eos','source_tokens','source_body_bytes','source_focus_teachers'):
        assert getattr(mixed,key)==getattr(staged,key),key
    for g in SOURCE_ORDER:assert equal_state(mixed.streams[g].state_dict(),staged.streams[g].state_dict()),g
    assert mixed.position==staged.position
    phases=[SOURCE_ORDER.index(g) for g in b[1]]
    # Only terminal all-masked padding returns to Web after the final phase.
    last=max(i for i,p in enumerate(phases) if p==3)
    assert phases[:last+1]==sorted(phases[:last+1])
    assert all(p==0 for p in phases[last+1:])


def test_resume_across_phase_boundaries_restores_exact_targets_and_cursors(tmp_path):
    pool,parent,_,positive=setup(tmp_path);goals=dict(web=19,story=11,ordinary_textbook=7,conditional_textbook=16)
    def build():return SourceOrderQuotaSampler(pool,pool,positive,parent['sampler'],goals,8)
    continuous,split=build(),build()
    left=[continuous.batch(3) for _ in range(2)]
    right=[split.batch(3) for _ in range(1)]
    state=copy.deepcopy(split.state_dict());resumed=build();resumed.load_state_dict(state)
    right.append(resumed.batch(3))
    while continuous.source_teachers!=goals:
        left.append(continuous.batch(3));right.append(resumed.batch(3))
    assert equal_state(left,right) and equal_state(continuous.state_dict(),resumed.state_dict())
    bad=copy.deepcopy(state);bad['source_order']=list(reversed(SOURCE_ORDER))
    with pytest.raises(ValueError,match='order'):build().load_state_dict(bad)
    with pytest.raises(ValueError):build().load_state_dict(OriginalWebQuotaSampler(pool,pool,positive,parent['sampler'],goals,8).state_dict())
