import copy
from types import SimpleNamespace

import numpy as np
import pytest
import torch

from jmicro.experiment import ROOT, read_json, sha256, write_json
from jmicro.tokenizer import Tokenizer
from jmicro.training import Trainer
from jmicro.teacher_chat_training import TeacherBudgetSampler, TeacherChatTrainer, teacher_lr
from test_chat_training import dialogues, same


def test_teacher_schedule_and_whole_target_terminal():
    assert teacher_lr(0,10,1000) == pytest.approx(1e-5)
    assert teacher_lr(495,10,1000) == pytest.approx(1e-4)
    assert teacher_lr(995,10,1000) == pytest.approx(1e-5)
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    s=TeacherBudgetSampler(dialogues(),tok,128,42,55,update_teachers=20,microbatch=2)
    totals=[]
    while s.teacher_tokens < 55:
        prior=s.teacher_tokens
        batches,n,_=s.next_update();totals.append(n)
        assert min(20,55-prior) <= n <= min(20,55-prior)+64
        assert sum(int(y.ne(-100).sum()) for _,y in batches)==n
        assert all(int(y.eq(7).sum()) <= 2 for _,y in batches)
        assert all(x[y.eq(-100) & x.eq(0)].eq(0).all() for x,y in batches)
    assert sum(totals)==s.teacher_tokens and 55 <= s.teacher_tokens <= 119
    restored=TeacherBudgetSampler(dialogues(),tok,128,42,55,update_teachers=20,microbatch=2)
    restored.load_state_dict(s.state_dict())
    with pytest.raises(ValueError,match='exhausted'):restored.next_update()
    for indices in ([],[0],[1,1],[1,99],[True]):
        records=copy.deepcopy(dialogues());records[0]['target_message_indices']=indices
        with pytest.raises(ValueError,match='Selected indices'):
            TeacherBudgetSampler(records,tok,128,42,100)


def test_teacher_optimizer_full_state_resume_and_global_microbatch_mean(tmp_path):
    torch.set_num_threads(2)
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    directory=tmp_path/'data';directory.mkdir();write_json(directory/'manifest.json',dict(vocab_size=4096))
    config=read_json(ROOT/'configs/models/t4k.json')
    config.update(hidden_size=32,num_attention_heads=2,num_key_value_heads=1,head_dim=16,
        rotary_dim=16,num_hidden_layers=1,intermediate_size=48,attention_scale=.25,qk_norm_type='none')
    shard=SimpleNamespace(directory=directory,split='train',manifest=dict(vocab_size=4096),
        tokens=np.asarray([2,8,9,10,11,3]*32,dtype='<u2'),
        index=[dict(offset=i*6,body_tokens=4) for i in range(32)],byte_lengths=np.asarray([0]*8+[1]*4088))
    spec=dict(seed=42,context=128,batch=2,accumulation=1,lr=1e-4,weight_decay=.01,
        warmup=0,schedule_updates=100,dtype='fp32',compile=False,backend='math',scheduler='wsd',
        sampler='document',training_fast_path=False,update_teachers=30)
    base=Trainer(config,shard,spec);base.step();base.save(tmp_path/'base.pt')
    parent=torch.load(tmp_path/'base.pt',map_location='cpu',weights_only=False)
    ref=dict(path=str(tmp_path/'base.pt'),sha256=sha256(tmp_path/'base.pt'))
    def build(batch=2):return TeacherChatTrainer(parent,ref,dialogues(),tok,directory,dict(spec,batch=batch),1000)
    a=build();assert same(a.model.state_dict(),parent['model']) and not a.optimizer.state
    a.step();a.save(tmp_path/'split.pt');a.step();a.step();a.save(tmp_path/'continuous.pt')
    b=build();b.load(tmp_path/'split.pt');b.step();b.step();b.save(tmp_path/'resumed.pt')
    first=torch.load(tmp_path/'continuous.pt',map_location='cpu',weights_only=False)
    second=torch.load(tmp_path/'resumed.pt',map_location='cpu',weights_only=False)
    for key in ('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','lineage','update'):
        assert same(first[key],second[key]),key
    # Same complete-target update split into one-row versus two-row microbatches.
    one,two=build(1),build(2);r1,r2=one.step(),two.step()
    assert r1['teachers_this_update']==r2['teachers_this_update']
    assert r1['microbatches'] > r2['microbatches']
    assert r1['loss']==pytest.approx(r2['loss'],abs=2e-6)
    for key,value in one.model.state_dict().items():
        torch.testing.assert_close(value,two.model.state_dict()[key],rtol=2e-4,atol=2e-7)
    assert b.tokens < b.sampler.physical_tokens
    assert b.supervised_tokens==b.sampler.teacher_tokens and b.update==3
    interrupted=build();interrupted.load(tmp_path/'split.pt');calls=[0]
    def stop_mid_update():
        calls[0]+=1
        if calls[0]==2:raise InterruptedError('test stop after data consumption')
    with pytest.raises(InterruptedError):interrupted.step(stop_mid_update)
    with pytest.raises(ValueError,match='partially completed'):interrupted.save(tmp_path/'invalid.pt')
    assert not (tmp_path/'invalid.pt').exists()
    with pytest.raises(ValueError,match='Restore'):interrupted.step()
    interrupted.load(tmp_path/'split.pt');interrupted.step();interrupted.step()
    assert same(interrupted.model.state_dict(),a.model.state_dict())
    assert same(interrupted.optimizer.state_dict(),a.optimizer.state_dict())
    assert interrupted.token_digest==a.token_digest
