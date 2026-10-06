import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from base_label_smoothing_trainer import LabelSmoothingTrainer
from natural_context_contrast_corpus import NaturalCorpusTrainer,OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


def builders(tmp_path):
    pool=tmp_path/'pool';manifest=fixture_pool(pool);original=parent()
    binding=dict(parent={'sha256':'CPU-fixture'},weights_role='verification_only')
    def build(smoothed=True):
        source=OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),dict(web=7500,textbook=2000,story=500))
        cls=LabelSmoothingTrainer if smoothed else NaturalCorpusTrainer
        return cls(original,source,binding,batch=4,contrast=False,device='cpu')
    return original,build


def test_same_initial_native_weights_parameters_logits_and_rng(tmp_path):
    original,build=builders(tmp_path);control=build(False);control.model.eval()
    ids=torch.tensor([[2,65,66,67]]);logits=control.model(ids).logits.detach();rng=torch.get_rng_state().clone()
    trainer=build();trainer.model.eval()
    assert torch.equal(rng,torch.get_rng_state()) and torch.equal(logits,trainer.model(ids).logits.detach())
    assert equal_state(original['model'],host(trainer.model.state_dict()))
    assert trainer.model.lm_head.weight is trainer.model.model.embed_tokens.weight
    assert sum(p.numel() for p in trainer.model.parameters())==sum(p.numel() for p in control.model.parameters())


def test_same_gold_source_stream_plus_separate_soft_target_accounting(tmp_path):
    _,build=builders(tmp_path);trainer,control=build(),build(False)
    for _ in range(4):
        actual,baseline=trainer.step(),control.step()
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens','physical_input_tokens',
                'original_body_bytes','token_digest','auxiliary_digest','draw_trace'):
            assert equal_state(actual[key],baseline[key]),key
        n=actual['supervised_tokens']
        assert actual['uniform_soft_target_positions']==n
        assert actual['weighted_original_target_mass']==.9*n and actual['uniform_target_mass']==.1*n
        assert actual['auxiliary_input_tokens']==actual['auxiliary_pairs']==0
        assert actual['combined_loss']==pytest.approx(.9*actual['CE_loss']+.1*actual['uniform_smoothing_loss'],abs=1e-6)
    assert equal_state(trainer.sampler.state_dict(),control.sampler.state_dict())
    assert not equal_state(host(trainer.model.state_dict()),host(control.model.state_dict()))


def test_continuous_vs_resumed_all_state_and_history_exact(tmp_path):
    _,build=builders(tmp_path);continuous=build();expected_rows=[continuous.step() for _ in range(4)]
    expected=host(continuous.state_dict());split=build();rows=[split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt');resumed=build();resumed.load(tmp_path/'split.pt')
    rows.extend(resumed.step() for _ in range(2))
    assert equal_state(expected,host(resumed.state_dict()))
    for a,b in zip(expected_rows,rows,strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
            {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})


def test_reject_changed_distribution_old_ce_checkpoint_or_eval_learning(tmp_path):
    _,build=builders(tmp_path);trainer=build();state=copy.deepcopy(host(trainer.state_dict()))
    state['spec']['label_smoothing']=.2;torch.save(state,tmp_path/'changed.pt')
    with pytest.raises(ValueError,match='binding'):trainer.load(tmp_path/'changed.pt')
    control=build(False);control.save(tmp_path/'ordinary.pt')
    with pytest.raises(ValueError,match='binding'):trainer.load(tmp_path/'ordinary.pt')
    trainer.model.eval()
    with pytest.raises(ValueError,match='model.train'):trainer.step()
