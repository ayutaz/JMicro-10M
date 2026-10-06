import copy
import sys
from pathlib import Path
import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts'),str(Path(__file__).resolve().parents[1]/'src')]
from historical_parent_condition_trainer import historical_web_cursor


def test_historical_web_cursor_is_copied_without_resetting_or_reheating():
    cursor=dict(seed=42,epoch=0,position=10253920,context=1024,blocks=11939276)
    state=dict(sampler=dict(kind='eos-pilot-mixture-v1',position=2,routes=[False,False],
        source_tokens=dict(web=65536,short=0),source_eos=dict(web=2,short=0),web=cursor,short=dict(position=0)),
        optimizer=dict(param_groups=[dict(lr=.00001),dict(lr=.00001)]))
    original=copy.deepcopy(state)
    got=historical_web_cursor(state)
    assert got==cursor and state==original
    got['position']=0
    assert state==original
    bad=copy.deepcopy(state);bad['optimizer']['param_groups'][0]['lr']=.0002
    with pytest.raises(ValueError):historical_web_cursor(bad)
    bad=copy.deepcopy(state);bad['sampler']['routes'][0]=True
    with pytest.raises(ValueError):historical_web_cursor(bad)
    bad=copy.deepcopy(state);bad['sampler']['source_tokens']['short']=1024
    with pytest.raises(ValueError):historical_web_cursor(bad)
