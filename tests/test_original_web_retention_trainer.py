import copy
import sys
import hashlib
import numpy as np
import pytest
import torch
from jmicro.experiment import ROOT
from jmicro.training import rng_state
sys.path.insert(0,str(ROOT/'scripts'))
from original_web_retention_trainer import OriginalWebQuotaSampler,OriginalWebRetentionTrainer
from mature_condition_trainer import MatureQuotaSampler
from run_eos_short_pilot import equal_state
from test_story_weight_comparison import fixture
from test_condition_positive_trainer import positive_fixture


def setup(tmp_path):
    pool,parent,binding = fixture(tmp_path)
    positive = positive_fixture(tmp_path)
    # The fixture parent is a real inherited Adam block-trained CPU checkpoint.
    # Its train arrays serve as the distinct block sampler material here.
    return pool,parent,binding,positive


def test_short_targets_and_terminal_cursors_are_identical_despite_Web_sampling(tmp_path):
    pool,parent,_,positive = setup(tmp_path)
    goals=dict(web=200,story=31,ordinary_textbook=29,conditional_textbook=37)
    left=MatureQuotaSampler(pool,positive,goals,8)
    right=OriginalWebQuotaSampler(pool,pool,positive,parent['sampler'],goals,8)
    def trace(sampler):
        # Wrap source blocks to record actual input/target/focus bytes, not just counters.
        digests={g:hashlib.sha256() for g in ('story','ordinary_textbook','conditional_textbook')}
        for source in digests:
            original=sampler.streams[source].block
            def wrapped(context,source=source,original=original):
                row=original(context)
                for array in row:digests[source].update(np.asarray(array).tobytes())
                return row
            sampler.streams[source].block=wrapped
        while sampler.source_teachers!=goals:sampler.batch(3)
        return {g:d.hexdigest() for g,d in digests.items()}
    assert trace(left)==trace(right)
    for source in ('story','ordinary_textbook','conditional_textbook'):
        assert equal_state(left.streams[source].state_dict(),right.streams[source].state_dict())
        for key in ('source_teachers','source_eos','source_body_bytes','source_focus_teachers'):
            assert getattr(left,key)[source]==getattr(right,key)[source]
    assert equal_state(right.streams['web'].state_dict()['sampler'],right.streams['web'].sampler.state_dict())


def test_full_resume_inherits_parent_Web_cursor_model_Adam_RNG(tmp_path):
    pool,parent,binding,positive=setup(tmp_path)
    goals=dict(web=300,story=100,ordinary_textbook=100,conditional_textbook=100)
    def build():return OriginalWebRetentionTrainer(parent,pool,pool,positive,goals,binding,'cpu',8,3)
    trainer=build()
    assert equal_state(trainer.model.state_dict(),parent['model'])
    assert equal_state(trainer.optimizer.state_dict(),parent['optimizer'])
    assert equal_state(rng_state(),parent['rng'])
    assert equal_state(trainer.sampler.streams['web'].sampler.state_dict(),parent['sampler'])
    left=[trainer.step() for _ in range(4)];trainer.save(tmp_path/'continuous/checkpoint.pt')
    split=build();right=[split.step() for _ in range(2)];split.save(tmp_path/'split/checkpoint.pt')
    restarted=build();restarted.load(tmp_path/'split/checkpoint.pt')
    right.extend(restarted.step() for _ in range(2));restarted.save(tmp_path/'resumed/checkpoint.pt')
    a=torch.load(tmp_path/'continuous/checkpoint.pt',map_location='cpu',weights_only=False)
    b=torch.load(tmp_path/'resumed/checkpoint.pt',map_location='cpu',weights_only=False)
    for key in a:assert equal_state(a[key],b[key]),key
    for key in ('loss','gradient_norm','lr','token_digest','source_teachers'):
        assert [r[key] for r in left]==[r[key] for r in right]
    bad=copy.deepcopy(restarted.sampler.state_dict());bad['streams']['web']['manifest_sha256']='changed'
    with pytest.raises(ValueError,match='source identity'):build().sampler.load_state_dict(bad)
