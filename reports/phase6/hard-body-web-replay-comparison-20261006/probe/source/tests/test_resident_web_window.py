import sys
import copy
import hashlib
import numpy as np
import pytest
from jmicro.experiment import ROOT
from jmicro.shards import BlockSampler
sys.path.insert(0,str(ROOT/'scripts'))
from resident_web_window import build,ResidentWebTokens
from test_original_web_retention_trainer import setup
from run_eos_short_pilot import equal_state


def test_all_original_targets_cursors_and_epoch_crossing_survive_resident_reads(tmp_path):
    view,parent,_,_=setup(tmp_path);cursor=copy.deepcopy(parent['sampler'])
    # Give the legacy toy view the actual train-manifest shape expected by the
    # new cache, without relaxing the production source identity contract.
    view.manifest=copy.deepcopy(view.manifest)
    view.manifest['splits']={'train':{'stream_sha256':hashlib.sha256(np.asarray(view.tokens,dtype='<u2').tobytes()).hexdigest()}}
    # Cover an epoch boundary: repeated blocks still have the same original IDs.
    count=cursor['blocks']+3
    record=build(view,cursor,count,tmp_path/'cache',workers=2)
    resident=ResidentWebTokens(view,cursor,count,tmp_path/'cache')
    original=BlockSampler(view,8,42);cached=BlockSampler(resident.view(view),8,42)
    original.load_state_dict(cursor);cached.load_state_dict(cursor)
    for _ in range(count):
        assert equal_state(original.batch(1),cached.batch(1))
    assert original.state_dict()==cached.state_dict()
    assert record['binding']['newly_prepared_source_tokens']==0
    with pytest.raises(ValueError):resident[1:10]
    bad=copy.deepcopy(cursor);bad['position']=(bad['position']+1)%bad['blocks']
    with pytest.raises(ValueError):ResidentWebTokens(view,bad,count,tmp_path/'cache')
