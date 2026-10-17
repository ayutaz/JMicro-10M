"""Owned32-example memorization diagnosis, never a generalization certificate."""
import argparse
from contextlib import contextmanager
from collections import defaultdict,Counter
import gc
import json
import os
from pathlib import Path
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
from answer_learning_common import ROOT,RUN,DATA,OLD_RUN,save,ref,bound,read_json,sha256,now,digest
import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.tokenizer import Tokenizer
from jmicro.teacher_chat_training import TeacherChatTrainer,TeacherBudgetSampler,teacher_lr
from jmicro.training import implementation_hashes,gpu_lock,autocast,isolated_evaluation
from jmicro.chat_evaluation import generate_reply
from jmicro.phase5 import equal_state
from phase6_performance import identity,alive,finite_state

CONFIG=ROOT/'configs/phase7/answer-diagnostic-20261017.json'
DIRECTORY=RUN/'diagnostic'
SOURCES=('scripts/answer_diagnostic.py','scripts/answer_learning_common.py','scripts/run_answer_diagnostic.ps1',
    'src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','src/jmicro/assistant_sampler.py',
    'src/jmicro/teacher_chat_training.py','src/jmicro/chat_evaluation.py')


def prepare():
    assert not CONFIG.exists()
    review=read_json(RUN/'TRAIN_capability_review.json')
    samples={r['id']:r for r in read_json(bound(review['sample']))}
    eligible=[j for j in review['judgments'] if j['neutral_assistant_acceptable'] and samples[j['id']]['teachers']<=32]
    direct=[j for j in eligible if j['direct_answer']]
    remainder=sorted([j for j in eligible if not j['direct_answer']],key=lambda j:digest('answer-diag42:'+j['id']))
    chosen=direct+remainder[:32-len(direct)]
    assert len(chosen)==32 and len(direct)==6
    groups={};cases=[]
    for j in chosen:
        s=samples[j['id']];uid=s['doc_id'];index=s['target_message_index']
        if uid not in groups:groups[uid]=dict(doc_id=uid,split='train',source=s['source'],messages=s['messages'],target_message_indices=[])
        elif len(groups[uid]['messages'])<len(s['messages']):groups[uid]['messages']=s['messages']
        groups[uid]['target_message_indices'].append(index)
        cases.append(dict(id=s['id'],doc_id=uid,target_message_index=index,direct_answer=j['direct_answer'],
            kind=j['kind'],messages=[dict(role=m['role'],content=m['text']) for m in s['messages'][:-1]],
            target=s['messages'][-1]['text'],teachers=s['teachers'],history_binding=s['history_binding']))
    rows=list(groups.values())
    for r in rows:r['target_message_indices']=sorted(r['target_message_indices'])
    save(DATA/'diagnostic_TRAIN.json',rows);save(DATA/'diagnostic_cases.json',cases)
    old=read_json(ROOT/'configs/phase7/chat-natural-sft-20261017.json')
    tok=Tokenizer(bound(old['tokenizer']))
    assert all(tok.chat_prompt(case['messages'],992)[1]==0 for case in cases)
    spec=dict(old['spec'],lr=1e-4)
    sampler=TeacherBudgetSampler(rows,tok,1024,42,250000,512,32)
    assert len(sampler.windows)==32 and max(sampler.lengths)<=32
    history=[];exposures=Counter()
    while sampler.teacher_tokens<250000:
        before=sampler.teacher_tokens
        batches,n,_=sampler.next_update()
        history.append(dict(update=len(history)+1,teachers_this_update=n,teachers=sampler.teacher_tokens,
            microbatches=len(batches),lr=teacher_lr(before,n,250000,1e-4)))
    assert len(history)<=1000 and 250000<=sampler.teacher_tokens<=250031
    dry=dict(status='passed',history=history,sampler_terminal=sampler.state_dict(),sampler_binding=sampler.binding,
        updates=len(history),actual_teachers=sampler.teacher_tokens,teachers_per_pass=sum(sampler.lengths),
        targets=32,direct_targets=6,all_targets_complete=True,all_prompt_histories_fit_without_trimming=True)
    save(RUN/'diagnostic_CPU_replay.json',dry)
    old_gate=read_json(OLD_RUN/'native_gate.json')
    assert old_gate['passed'] and old_gate['arms']['C0']['maximum_shape']['shape']==[32,1024]
    assert old['implementation']==implementation_hashes()
    c=dict(kind='TRAIN_only32_memorization_diagnostic',created_at=now(),parent=old['parent'],tokenizer=old['tokenizer'],
        implementation=old['implementation'],parameter_count=10001152,spec=spec,teacher_budget=250000,
        maximum_updates=1000,maximum_teacher_length=32,max_new_tokens=32,seed=42,
        limits_seconds=dict(probe=600.,train=1800.,evaluation=900.),records=ref(DATA/'diagnostic_TRAIN.json'),
        cases=ref(DATA/'diagnostic_cases.json'),CPU_replay=ref(RUN/'diagnostic_CPU_replay.json'),
        semantic_review=ref(RUN/'TRAIN_capability_review.json'),reused_maximum_shape_evidence=ref(OLD_RUN/'native_gate.json'),
        numerical_protocol='Same frozen TeacherChatTrainer,512 complete teachers/update,32x1024,math,BF16',
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        acceptance=dict(content_minimum=26,direct_answer_minimum=5,direct_answer_denominator=6,natural_stop_minimum=29),
        no_unseen_quality_claim=True,Chat_adopted=False,Base_adopted=False,protected_TEST_used=False,
        rationale='Determine whether six reviewed direct answers and26 other neutral TRAIN responses can be learned; all32 targets<=32',
        LR_rationale='A deliberately small memorization diagnosis uses1e-4, the existing native teacher trainer default, not the later comparative SFT choice')
    save(CONFIG,c)
    print(json.dumps(dict(frozen=ref(CONFIG),updates=len(history),actual_teachers=sampler.teacher_tokens,targets=32,direct=6)))


def inspect():
    c=read_json(CONFIG)
    assert c['implementation']==implementation_hashes() and c['kind']=='TRAIN_only32_memorization_diagnostic'
    assert all(sha256(ROOT/p)==h for p,h in c['source_sha256'].items())
    for key in ('parent','tokenizer','records','cases','CPU_replay','semantic_review','reused_maximum_shape_evidence'):bound(c[key])
    assert not c['protected_TEST_used'] and c['teacher_budget']==250000 and c['spec']['lr']==1e-4
    assert not (DIRECTORY/'job.json').exists(),'Previous diagnosis exists; inspect it, never duplicate or reopen'
    return c


@contextmanager
def stage(c,name):
    started=time.monotonic();p=DIRECTORY/'GPU_ledger.json'
    ledger=read_json(p) if p.exists() else dict(entries=[],limits=c['limits_seconds'])
    assert not any(r['status']=='running' for r in ledger['entries'])
    used=sum(r['seconds'] for r in ledger['entries'] if r['stage']==name)
    cap=c['limits_seconds'][name]-used;assert cap>0
    row=dict(**identity(),stage=name,status='running',seconds=0.,started_at=now(),config=ref(CONFIG))
    ledger['entries'].append(row)
    def check():
        elapsed=time.monotonic()-started
        if elapsed>=cap:raise TimeoutError('Frozen diagnostic stage budget exceeded')
    def beat(**values):
        row.update(values,seconds=time.monotonic()-started,heartbeat_at=now());save(p,ledger)
    beat()
    try:yield check,beat;row['status']='complete'
    except BaseException as error:row.update(status='failed',error=repr(error));raise
    finally:
        row.update(seconds=time.monotonic()-started,ended_at=now());ledger['total_seconds']=sum(r['seconds'] for r in ledger['entries']);save(p,ledger)


def evaluate(t,c,tok,cases,point,check):
    outputs=[];total_nll=0.;teachers=0
    with isolated_evaluation(t.model),torch.inference_mode(),sdpa_kernel(SDPBackend.MATH):
        for w in t.sampler.windows:
            check();x=torch.tensor(w['ids'][:-1],device='cuda').unsqueeze(0)
            y=torch.tensor(w['labels'][1:],device='cuda')
            with autocast('cuda','bf16'):logits=t.model(x,attention_mask=x.ne(0)).logits
            total_nll+=float(F.cross_entropy(logits[0].float(),y,ignore_index=-100,reduction='sum'))
            teachers+=int(y.ne(-100).sum())
        for case in cases:
            check();row=generate_reply(t.model,tok,case['messages'],'cuda','bf16',32,True,check)
            assert row['removed_turns']==0
            outputs.append(dict(case=case,response=row))
    save(DIRECTORY/f'{point}_raw.json',dict(point=point,kind='TRAIN_memorization_only',config=ref(CONFIG),
        outputs=outputs,teachers=teachers,mean_NLL=total_nll/teachers,Chat_adopted=False,protected_TEST_used=False))


def run():
    c=inspect();DIRECTORY.mkdir(parents=True,exist_ok=True)
    job=dict(**identity(),status='running',config=ref(CONFIG),started_at=now());save(DIRECTORY/'job.json',job)
    tok=Tokenizer(bound(c['tokenizer']));rows=read_json(bound(c['records']));cases=read_json(bound(c['cases']))
    parent=torch.load(bound(c['parent']),map_location='cpu',weights_only=False)
    assert finite_state(parent) and parent['implementation_sha256']==c['implementation']
    assert sum(v.numel() for k,v in parent['model'].items() if k!='lm_head.weight')>0
    def build():return TeacherChatTrainer(parent,c['parent'],rows,tok,DATA,c['spec'],250000,'cuda')
    def release():gc.collect();torch.cuda.empty_cache()
    try:
        with gpu_lock('cuda'):
            torch.cuda.set_per_process_memory_fraction(.90)
            with stage(c,'probe') as (check,beat):
                states=[];histories=[]
                for branch in ('continuous','resumed'):
                    t=build();h=[]
                    for i in range(2):
                        check();h.append(t.step(check))
                        if branch=='resumed' and i==0:
                            t.save(DIRECTORY/'probe_split.pt');del t;release()
                            t=build();t.load(DIRECTORY/'probe_split.pt')
                    t.save(DIRECTORY/f'probe_{branch}.pt')
                    states.append(torch.load(DIRECTORY/f'probe_{branch}.pt',map_location='cpu',weights_only=False))
                    histories.append(h);del t;release()
                keys=('model','optimizer','scheduler','rng','sampler','update','tokens','supervised_tokens','body_bytes','token_digest','lineage','spec')
                checks={k:equal_state(states[0][k],states[1][k]) for k in keys}
                for key in ('loss','gradient_norm','lr','teachers_this_update','token_digest'):
                    checks['history_'+key]=[r[key] for r in histories[0]]==[r[key] for r in histories[1]]
                assert all(checks.values()) and finite_state(states[0]) and finite_state(states[1])
                save(DIRECTORY/'native_probe.json',dict(passed=True,checks=checks,histories=histories,
                    reused_shape=c['reused_maximum_shape_evidence'],new_optimizer_updates=6,quality_evidence=False))
                del states;release();beat(passed=True)
            t=build();assert not t.optimizer.state
            with stage(c,'evaluation') as (check,beat):evaluate(t,c,tok,cases,'before',check);beat(responses=32)
            history=[]
            with stage(c,'train') as (check,beat):
                with (DIRECTORY/'metrics.jsonl').open('x') as stream:
                    while t.supervised_tokens<250000:
                        check();assert t.update<1000
                        h=t.step(check);history.append(h);stream.write(json.dumps(h)+'\n');stream.flush()
                        if t.update%25==0:beat(update=t.update,teachers=t.supervised_tokens);print(json.dumps(dict(update=t.update,teachers=t.supervised_tokens,loss=h['loss'])),flush=True)
                        if t.update%100==0:t.save(DIRECTORY/f'checkpoint-{t.update:08d}.pt')
                    t.save(DIRECTORY/'final.pt');beat(update=t.update,teachers=t.supervised_tokens)
                assert finite_state(dict(model=t.model.state_dict(),optimizer=t.optimizer.state_dict()))
            with stage(c,'evaluation') as (check,beat):evaluate(t,c,tok,cases,'after',check);beat(responses=32)
            dry=read_json(bound(c['CPU_replay']))
            assert t.sampler.state_dict()==dry['sampler_terminal'] and len(history)==dry['updates']
            for a,b in zip(history,dry['history'],strict=True):
                assert (a['update'],a['teachers_this_update'],a['microbatches'],a['lr'])==(b['update'],b['teachers_this_update'],b['microbatches'],b['lr'])
            save(DIRECTORY/'result.json',dict(status='diagnostic_training_and_all64_raw_complete_pending_notes',
                config=ref(CONFIG),checkpoint=ref(DIRECTORY/'final.pt'),updates=t.update,teachers=t.supervised_tokens,
                full_state_CPU_replay_exact=True,all_history_and_all119_Adam_states_retained=True,
                quality_pending=True,unseen_generalization_not_tested=True,protected_TEST_used=False,Chat_adopted=False))
            del t;release()
        job.update(status='complete',ended_at=now())
    except BaseException as error:job.update(status='failed',error=repr(error),ended_at=now());raise
    finally:save(DIRECTORY/'job.json',job)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('prepare','inspect','run'));a=p.parse_args()
    if a.mode=='prepare':prepare()
    elif a.mode=='inspect':inspect();print('Frozen diagnostic preflight passed; CUDA not initialized')
    else:run()
