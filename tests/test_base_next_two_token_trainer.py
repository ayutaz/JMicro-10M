"""Native inference/original teachers and full next-two training-state checks."""
import copy
from pathlib import Path
import sys

import pytest
import torch

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from base_next_two_token_trainer import NextTwoTokenTrainer,next_two_targets
from natural_context_contrast_corpus import NaturalCorpusTrainer,OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


def builders(tmp_path):
    pool=tmp_path/'pool';manifest=fixture_pool(pool);p=parent()
    binding=dict(parent={'sha256':'fixture'},weights_role='verification_only')
    def build(aux=True):
        s=OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),dict(web=7500,textbook=2000,story=500))
        cls=NextTwoTokenTrainer if aux else NaturalCorpusTrainer
        return cls(p,s,binding,batch=4,contrast=False,device='cpu')
    return p,build


def test_future_targets_never_cross_padding_overlap_or_original_EOS():
    labels=torch.tensor([[-100,65,66,3,-100,-100],[-100,-100,70,71,72,-100]])
    assert next_two_targets(labels).tolist()==[[-100,66,3,-100,-100,-100],[-100,-100,71,72,-100,-100]]
    assert next_two_targets(torch.tensor([[3]])).tolist()==[[-100]]


def test_native_initial_weights_logits_tying_parameters_and_RNG_match_without_aux_inference(tmp_path):
    p,build=builders(tmp_path);control=build(False);control.model.eval()
    ids=torch.tensor([[2,65,66,67]])
    expected=control.model(ids).logits.detach();rng=torch.get_rng_state().clone()
    t=build();t.model.eval()
    assert torch.equal(rng,torch.get_rng_state()) and torch.equal(expected,t.model(ids).logits.detach())
    assert equal_state(p['model'],host(t.model.state_dict()))
    assert t.model.lm_head.weight is t.model.model.embed_tokens.weight
    assert t.spec['native_parameters']==sum(p.numel() for p in control.model.parameters())
    assert t.spec['train_only_parameters']==sum(p.numel() for p in t.future_head.parameters())>0
    assert len(t.optimizer.param_groups[0]['params'])==len(list(t.model.parameters()))+len(list(t.future_head.parameters()))


def test_full_original_source_and_teacher_accounting_matches_cached_ce_protocol(tmp_path):
    _,build=builders(tmp_path);t,control=build(),build(False)
    for _ in range(4):
        a,b=t.step(),control.step()
        for key in ('supervised_tokens','source_teachers','source_EOS','CE_input_tokens','physical_input_tokens',
                'original_body_bytes','token_digest','auxiliary_digest','draw_trace','lr'):
            assert equal_state(a[key],b[key]),key
        assert a['combined_loss']==pytest.approx(a['CE_loss']+.1*a['next_two_CE_loss'],abs=1e-6)
        assert a['next_two_teacher_positions']==sum(a['source_next_two_teachers'].values())<=a['supervised_tokens']
        assert a['next_two_target_mass']==.1*a['next_two_teacher_positions']
        assert a['next_two_head_gradient_norm']>0 and a['auxiliary_input_tokens']==a['auxiliary_pairs']==0
    assert equal_state(t.sampler.state_dict(),control.sampler.state_dict())


def test_native_aux_optimizer_scheduler_RNG_full_sampler_and_history_resume_exact(tmp_path):
    _,build=builders(tmp_path);continuous=build();expected_rows=[continuous.step() for _ in range(4)]
    expected=host(continuous.state_dict());split=build();rows=[split.step() for _ in range(2)]
    split.save(tmp_path/'split.pt');resumed=build();resumed.load(tmp_path/'split.pt')
    rows.extend(resumed.step() for _ in range(2))
    assert equal_state(expected,host(resumed.state_dict()))
    assert all(equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
                          {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})
               for a,b in zip(expected_rows,rows,strict=True))


def test_changed_objective_auxiliary_missing_bad_accounting_old_control_and_eval_rejected(tmp_path):
    _,build=builders(tmp_path);t=build();t.step();original=host(t.state_dict())
    for label in ('coefficient','mass','missing_aux'):
        state=copy.deepcopy(original)
        if label=='coefficient':state['spec']['next_two_coefficient']=.2
        elif label=='mass':state['counters']['next_two_target_mass']+=1
        else:state.pop('auxiliary_model')
        torch.save(state,tmp_path/'bad.pt')
        with pytest.raises((ValueError,KeyError)):build().load(tmp_path/'bad.pt')
    build(False).save(tmp_path/'old.pt')
    with pytest.raises(ValueError,match='binding'):build().load(tmp_path/'old.pt')
    t.model.eval()
    with pytest.raises(ValueError,match='model.train'):t.step()
