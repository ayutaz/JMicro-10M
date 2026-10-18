"""Owned new curriculum pipeline; reuse frozen native training/evaluation arithmetic."""
import argparse
import gc
import json
import os
import signal
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import numpy as np
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from answer_learning_common import ROOT,save,ref,bound,read_json,now
import answer_curriculum_contract as contract
from answer_curriculum_contract import RUN,DATA,CONFIG,BUDGET,SPEC,LIMITS,SUITES,stage,preflight,read_dev
from jmicro.training import seed_all
from jmicro.phase5 import equal_state
from phase6_performance import identity,alive,finite_state
import run_chat_natural as native
import evaluate_chat_natural as evaluation


def windows(c,tok):
    rows=[]
    for i,line in enumerate(bound(c['NLL']).read_text().splitlines()):
        row=json.loads(line);assert row['split'] in ('train','dev') and 'TEST' not in row['dataset']
        if i<208 and row['dataset']=='new_DEV':row=dict(row,dataset='previous_new_DEV')
        w=list(tok.sft_windows(row['messages'],1025))[-1];y=np.asarray(w['labels'][1:])
        assert w['removed_turns']==0 and 2<=int((y!=-100).sum())<=32
        rows.append((row,np.asarray(w['input_ids'][:-1]),y))
    assert len(rows)==320;return rows


def wire_reuse():
    # Explicitly scoped adapters. No old files, weights, config or runtime process
    # is changed; these imports exist only in this new process.
    for module in (native,evaluation):
        for key,value in dict(RUN=RUN,DATA=DATA,BUDGET=BUDGET,SPEC=SPEC,LIMITS=LIMITS,SUITES=SUITES,
            stage=stage,read_dev=read_dev,require_ref=bound).items():setattr(module,key,value)
    evaluation.windows=windows
    native.preflight=preflight
    native.read_bound=lambda value:read_json(bound(value))


def build(parent,c,tok,rows):return native.build(parent,c,tok,rows,'new')


def release():gc.collect();torch.cuda.empty_cache()


def fixture(rows,arm):
    if arm=='C0':return rows[:48]
    baseline=[r for r in rows if 'explicit_repeat_alias' not in r][:8]
    extra=[r for r in rows if r.get('explicit_repeat_alias')==0]
    result=list(baseline)
    for family in ('name','preference','correction','quantity','owner','literal','arithmetic','missing'):
        result.extend([r for r in extra if r.get('family')==family][:4])
    for source in ('Dolly_llmjp','Aya_Japanese_TRAIN'):result.extend([r for r in extra if r['source']==source][:4])
    assert len(result)==48 and len({r['doc_id'] for r in result})==48
    return result


def probe(parent,c,tok,arms):
    target=RUN/'native_gate.json';assert not target.exists(),'Never reopen a closed probe'
    reports={};updates=0
    with stage('probe',c['config_sha256']) as (left,beat):
        for arm,rows in arms.items():
            selected=fixture(rows,arm);t=build(parent,c,tok,selected)
            assert not t.optimizer.state and sum(p.numel() for p in t.model.parameters())==10001152
            assert equal_state({k:v.cpu() for k,v in t.model.state_dict().items()},parent['model'])
            timing=[]
            for _ in range(16):
                assert left()>30
                timing.append(t.step());beat(arm=arm,technical_update=t.update)
            assert finite_state(dict(model=t.model.state_dict(),optimizer=t.optimizer.state_dict()))
            dry=read_json(bound(c['arms'][arm]['dry_run']))
            rate=max(h['seconds']/h['microbatches'] for h in timing)
            forecast=rate*dry['physical_microbatches']*1.35+300.
            assert forecast<=LIMITS['train_'+arm],(arm,forecast)
            updates+=16;del t;release()
            histories=[];states=[];directory=RUN/'native-resume'/arm;directory.mkdir(parents=True,exist_ok=True)
            for branch in ('continuous','resumed'):
                t=build(parent,c,tok,selected);history=[]
                for i in range(2):
                    assert left()>30;history.append(t.step())
                    if branch=='resumed' and i==0:
                        t.save(directory/'split.pt');del t;release();t=build(parent,c,tok,selected);t.load(directory/'split.pt')
                t.save(directory/f'{branch}.pt');states.append(torch.load(directory/f'{branch}.pt',map_location='cpu',weights_only=False))
                histories.append(history);updates+=2;del t;release()
            assert set(states[0])==set(states[1])
            checks={key:equal_state(states[0][key],states[1][key]) for key in states[0]}
            excluded={'seconds','data_wait_seconds','teacher_tokens_per_second'}
            for key in histories[0][0]:
                if key not in excluded:checks['history:'+key]=[r[key] for r in histories[0]]==[r[key] for r in histories[1]]
            assert all(checks.values()) and finite_state(states[0]) and finite_state(states[1]),checks
            reports[arm]=dict(fixture_doc_ids=[r['doc_id'] for r in selected],all16_timing_updates=timing,
                rate_worst_all16=rate,forecast_training_seconds=forecast,resume_all_fields=checks,
                history_excluded_only=sorted(excluded),resume_histories=histories,
                snapshots={branch:ref(directory/f'{branch}.pt') for branch in ('continuous','resumed')})
            del states;release();beat(arm=arm,resume_passed=True)
        # Existing same-native max32x1024 backward is reused, no redundant maximum fixture.
        # Evaluation forecast uses fresh own-gate actual replies, no quality selection.
        t=build(parent,c,tok,fixture(arms['C0'],'C0'));cases,_=read_dev(c['suites']['new'])
        selected=sorted(cases,key=lambda r:len(tok.chat_prompt(r['messages'],992)[0]),reverse=True)[:4]
        timings=[]
        for case in selected:
            assert left()>30;started=time.monotonic()
            with sdpa_kernel(SDPBackend.MATH):row=evaluation.generate_reply(t.model,tok,case['messages'],'cuda','bf16',32,True)
            torch.cuda.synchronize();timings.append(dict(seconds=time.monotonic()-started,tokens=row['generated_tokens']))
        assert all(r['tokens']>0 for r in timings)
        estimate=max(r['seconds']/r['tokens'] for r in timings)*32*2628*1.5+600.
        assert estimate<=LIMITS['evaluation'];del t;release()
        beat(passed=True)
    save(target,dict(passed=True,config_sha256=c['config_sha256'],arms=reports,technical_updates=updates,
        reused_maximum_shape=c['reused_maximum_shape'],evaluation_timings=timings,evaluation_forecast_seconds=estimate,
        quality_evidence=False,science_updates=0,created_at=now()))
    print(json.dumps(dict(probe='passed',technical_updates=updates,forecasts={k:v['forecast_training_seconds'] for k,v in reports.items()},evaluation=estimate)),flush=True)


def evaluate_all(c,tok,stopped):
    from jmicro.model import JMicroModel
    with stage('evaluation',c['config_sha256']) as (left,beat):
        def check():
            if stopped[0] or left()<20:raise InterruptedError('Stop at completed output boundary')
        for arm in ('C0','C1'):
            result=read_json(RUN/arm/'result.json');assert result['status']=='learning_complete'
            value=result['checkpoint'];state=torch.load(bound(value),map_location='cpu',weights_only=False)
            assert BUDGET<=state['supervised_tokens']<=BUDGET+31 and state['implementation_sha256']==c['implementation']
            assert state['spec']['teacher_chat']['data_binding']==c['arms'][arm]['sampler_binding']
            model=JMicroModel(state['model_config']).cuda();model.load_state_dict(state['model'],strict=True);model.eval().requires_grad_(False)
            assert sum(p.numel() for p in model.parameters())==10001152 and all(bool(torch.isfinite(p).all()) for p in model.parameters())
            del state
            with sdpa_kernel(SDPBackend.MATH):
                for suite in SUITES:evaluation.final_suite(model,c,tok,arm,suite,value,check,beat)
            del model;release()
    save(RUN/'evaluation_raw_complete.json',dict(status='all2628_raw_complete_pending_individual_content_review',
        config_sha256=c['config_sha256'],responses=2628,protected_TEST_used=False,Chat_adopted=False,whole_five_stage_goal_complete=False,created_at=now()))


def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['inspect','run']);args=p.parse_args()
    c,tok,arms=preflight(load_records=args.mode=='run')
    if args.mode=='inspect':
        windows(c,tok);print('New contract/prepared manifest/all6 DEV/NLL320/source bindings pass; CUDA not initialized');return
    path=RUN/'pipeline.json'
    if path.exists():
        old=read_json(path);assert not alive(old) and old['status']=='signal_interrupted' and old['config_sha256']==c['config_sha256']
    torch.set_num_threads(2);torch.use_deterministic_algorithms(True);seed_all(42)
    assert torch.cuda.is_available() and '4090' in torch.cuda.get_device_name(0)
    stopped=[False];signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    wire_reuse();job=dict(**identity(),status='running',config_sha256=c['config_sha256'],started_at=now());save(path,job)
    try:
        parent=native.load_parent(c)
        if not (RUN/'native_gate.json').exists():probe(parent,c,tok,arms)
        else:
            gate=read_json(RUN/'native_gate.json');assert gate['passed'] and gate['config_sha256']==c['config_sha256']
        for arm,rows in arms.items():native.train(parent,c,tok,rows,arm,stopped)
        del parent;gc.collect();evaluate_all(c,tok,stopped)
        job.update(status='complete_raw_pending_all_content_and_UI',ended_at=now())
    except BaseException as error:
        job.update(status='signal_interrupted' if stopped[0] and isinstance(error,InterruptedError) else 'failed',error=repr(error),ended_at=now());raise
    finally:save(path,job)


if __name__=='__main__':main()
