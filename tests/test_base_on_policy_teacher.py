import copy
from pathlib import Path
import sys
from types import SimpleNamespace
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_on_policy_teacher_trainer import (OnPolicyTeacherTrainer,RECIPE,prefixes_from_rows,
    sample_rollout,scoring_batch,committed_state)
from natural_context_contrast_corpus import OriginalTrainCorpusSampler,NaturalCorpusTrainer
from natural_context_contrast_trainer import host
from jmicro.phase5 import equal_state
from test_natural_context_contrast_corpus import fixture_pool,FixtureCodec,parent


def build_factory(tmp_path):
    pool=tmp_path/'pool';manifest=fixture_pool(pool);p=parent();teacher=copy.deepcopy(p)
    def build(control=False):
        sampler=OriginalTrainCorpusSampler(pool,manifest,FixtureCodec(),dict(web=75000,textbook=20000,story=5000))
        binding=dict(parent={'sha256':'fixture'},weights_role='verification_only')
        if control:return NaturalCorpusTrainer(p,sampler,binding,batch=4,contrast=False,device='cpu')
        return OnPolicyTeacherTrainer(p,sampler,binding,teacher,dict(sha256='teacher-fixture'),batch=4,device='cpu')
    return build,teacher


def test_original_heads_only_and_exact_prefix_without_new_source_draw(tmp_path):
    build,_=build_factory(tmp_path);t=build();rows=t.sampler.take(8);before=copy.deepcopy(rows)
    prefixes=prefixes_from_rows(rows)
    assert prefixes and all(p['source'] in ('textbook','story') for p in prefixes)
    assert rows==before
    for p in prefixes:
        r=next(r for r in rows if r['index_byte_position']==p['index_byte_position'])
        assert p['prompt']==r['input_ids'][:min(16,max(1,(len(r['input_ids'])-1)//2))+1]
    shifted=copy.deepcopy(rows)
    for r in shifted:r['target_first']=513;r['original_document_first_window']=False
    assert not prefixes_from_rows(shifted)


def test_generated_position_alignment_first_EOS_and_prompt_padding_mask():
    records=[dict(prompt=[2,8,9],generated=[10,11,3]),dict(prompt=[2,12],generated=[3])]
    ids,targets,counts=scoring_batch(records,'cpu')
    assert ids.tolist()==[[2,8,9,10,11],[2,12,0,0,0]]
    assert targets.tolist()==[[-100,-100,10,11,3],[-100,3,-100,-100,-100]]
    assert targets[targets.ne(-100)].tolist()==[10,11,3,3]
    assert counts==dict(valid_inputs=7,physical_inputs=10)
    with pytest.raises(ValueError):scoring_batch([dict(prompt=[2,8],generated=[3,9])],'cpu')


def test_sampled_EOS_stops_per_row_masks_cache_and_restores_mode(monkeypatch):
    calls=[];draws=iter((torch.tensor([[3],[8]]),torch.tensor([[3]])))
    class Fake(torch.nn.Module):
        def __init__(self):
            super().__init__();self.anchor=torch.nn.Parameter(torch.zeros(()));self.config=dict(max_position_embeddings=1024)
        def forward(self,ids,attention_mask=None,cache=None,use_cache=False):
            assert not self.training and not torch.is_grad_enabled()
            calls.append((ids.tolist(),attention_mask.tolist(),cache))
            return SimpleNamespace(logits=torch.zeros(*ids.shape,16),cache='fixed-cache')
    model=Fake()
    def sample(probabilities,n):
        assert n==1 and probabilities[:,RECIPE['sample_blocked_ids']].count_nonzero()==0
        return next(draws)
    monkeypatch.setattr(torch,'multinomial',sample)
    records,counts=sample_rollout(model,[dict(prompt=[2,8],source='textbook'),dict(prompt=[2,8,9],source='story')])
    assert [r['generated'] for r in records]==[[3],[8,3]] and model.training
    assert calls[1]==([[0],[8]],[[False],[True]],'fixed-cache')
    assert counts==dict(valid_inputs=6,physical_inputs=8)
    assert all(r['EOS_stopped'] for r in records)
    def failed(*args,**kwargs):raise RuntimeError('decode fixture failure')
    monkeypatch.setattr(model,'forward',failed)
    with pytest.raises(RuntimeError):sample_rollout(model,[dict(prompt=[2,8])])
    assert model.training


def test_actual_CPU_random_rollouts_saved16plus16_equal_continuous32(tmp_path):
    build,_=build_factory(tmp_path)
    continuous=build();expected_history=[continuous.step() for _ in range(32)];expected=host(continuous.state_dict())
    split=build();actual_history=[split.step() for _ in range(16)];split.save(tmp_path/'split.pt')
    resumed=build();resumed.load(tmp_path/'split.pt');actual_history.extend(resumed.step() for _ in range(16))
    assert equal_state(expected,host(resumed.state_dict())) and committed_state(expected)
    assert expected['on_policy_teacher']['rollout_batches']==2 and expected['on_policy_teacher']['distribution_positions']>0
    for a,b in zip(expected_history,actual_history,strict=True):
        assert equal_state({k:v for k,v in a.items() if k not in ('seconds','data_wait_seconds')},
            {k:v for k,v in b.items() if k not in ('seconds','data_wait_seconds')})


def test_all_original_gold_and_sampler_unchanged_while_teacher_immutable(tmp_path):
    build,teacher=build_factory(tmp_path);t,control=build(),build(True)
    for _ in range(32):
        a,b=t.step(),control.step()
        assert all(equal_state(a[k],b[k]) for k in (*t.counters,'draw_trace','lr'))
    assert equal_state(t.sampler.state_dict(),control.sampler.state_dict())
    assert equal_state(teacher['model'],host(t.teacher.state_dict())) and all(p.grad is None for p in t.teacher.parameters())
    assert t.on_policy['source_positions']['web']==0 and t.on_policy['teacher_physical_inputs']>0
    assert {id(p) for g in t.optimizer.param_groups for p in g['params']}=={id(p) for p in t.model.parameters()}
    assert t.model.lm_head.weight is t.model.model.embed_tokens.weight


@pytest.mark.parametrize('mutation',['teacher','recipe','positions','scheduled','oldkind'])
def test_wrong_teacher_recipe_and_uncommitted_auxiliary_counts_rejected(tmp_path,mutation):
    build,_=build_factory(tmp_path);t=build()
    for _ in range(16):t.step()
    state=host(t.state_dict())
    if mutation=='teacher':state['spec']['teacher']['sha256']='other'
    if mutation=='recipe':state['spec']['on_policy_teacher']['coefficient']=2.
    if mutation=='positions':state['on_policy_teacher']['distribution_positions']+=1
    if mutation=='scheduled':state['on_policy_teacher']['scheduled_batches']+=1
    if mutation=='oldkind':state['kind']='gold-prefix-KD'
    torch.save(state,tmp_path/'wrong.pt')
    with pytest.raises(ValueError):build().load(tmp_path/'wrong.pt')
