import copy
from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from livedoor_base_trainer import NewsBaseTrainer,NewsQuotaSampler
from parameter_displacement_anchor_trainer import ParameterAnchorTrainer
from test_parameter_displacement_anchor import mixed_fixture
from run_eos_short_pilot import equal_state
from jmicro.training import rng_state
from jmicro.experiment import sha256


def prefix_fixture(tmp_path):
    pool,parent,binding,positive=mixed_fixture(tmp_path)
    old=ParameterAnchorTrainer(parent,pool,pool,positive,dict(web=150,story=1,ordinary_textbook=1,conditional_textbook=1),binding,0.,'cpu',8,3)
    old.step();old.save(tmp_path/'prefix.pt')
    prefix=torch.load(tmp_path/'prefix.pt',weights_only=False)
    # Old tiny mixed fixture lacks this production prefix provenance field.
    # Populate it from this actual CPU TRAIN source, never bypass production checks.
    prefix['spec']['original_web_manifest_sha256']=sha256(pool.directory/'manifest.json')
    return pool,prefix,binding


def test_actual_inherited_fullstate_and_resume_through_Web_news_boundary(tmp_path):
    pool,parent,binding=prefix_fixture(tmp_path);goals=dict(web=11,authored_news=120)
    def build():return NewsBaseTrainer(parent,pool,pool,goals,binding,'cpu',8,3)
    trainer=build()
    assert equal_state(trainer.model.state_dict(),parent['model'])
    assert equal_state(trainer.optimizer.state_dict(),parent['optimizer'])
    assert equal_state(trainer.scheduler.state_dict(),parent['scheduler'])
    assert equal_state(rng_state(),parent['rng'])
    left=[trainer.step() for _ in range(4)];trainer.save(tmp_path/'continuous.pt')
    restarted=build();right=[restarted.step() for _ in range(2)];restarted.save(tmp_path/'split.pt')
    restarted=build();restarted.load(tmp_path/'split.pt');right += [restarted.step() for _ in range(2)];restarted.save(tmp_path/'resumed.pt')
    assert equal_state(torch.load(tmp_path/'continuous.pt',weights_only=False),torch.load(tmp_path/'resumed.pt',weights_only=False))
    assert left[0]['source_teachers']['web']==11 and left[0]['source_teachers']['authored_news']>0
    assert all(row['lr']==.00001 for row in left)
    for key in ('loss','gradient_norm','source_teachers','token_digest','focus_token_digest'):
        assert [r[key] for r in left]==[r[key] for r in right]


def test_exact_tail_teacher_bytes_EOS_and_masked_physical_padding(tmp_path):
    pool,parent,_=prefix_fixture(tmp_path);cursor=parent['sampler']['streams']['web']['sampler']
    sampler=NewsQuotaSampler(pool,pool,cursor,dict(web=1,authored_news=3),8)
    x,y,body_bytes,focus=sampler.batch(3)
    assert sampler.source_teachers==dict(web=1,authored_news=3) and y.ne(-100).sum()==4
    assert int(sampler.source_eos['web']+sampler.source_eos['authored_news'])==int(y.eq(3).sum())
    assert body_bytes==int(pool.byte_lengths[y[y>=8].numpy()].sum()) and not focus.any()
    assert x.numel()==24 and sum(sampler.source_tokens.values())==24
    with pytest.raises(ValueError):sampler.batch(3)
    bad=copy.deepcopy(sampler.state_dict());bad['goals']['web']=2
    with pytest.raises(ValueError):sampler.load_state_dict(bad)


def test_device_normalization_preserves_nested_state_values_and_types():
    from probe_livedoor_base import host_state
    state={'model':torch.tensor([1.,2.],dtype=torch.float64),'optimizer':[{'step':torch.tensor(8,dtype=torch.int64)}],
        'rng':(torch.tensor([3],dtype=torch.uint8),42),'scheduler':{'LR':.00001}}
    normalized=host_state(state)
    assert equal_state(state,normalized)
    assert normalized['model'].dtype==torch.float64 and normalized['optimizer'][0]['step'].dtype==torch.int64
    assert isinstance(normalized['rng'],tuple) and isinstance(normalized['optimizer'],list)
