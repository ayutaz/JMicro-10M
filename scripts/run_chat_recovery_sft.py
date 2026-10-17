"""New paired SFT and all7 suites/public100, reusing frozen native arithmetic."""
import argparse
import gc
import json
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import signal
import time
import numpy as np
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from chat_recovery_contract import ROOT,RUN,DATA,CONFIG,BUDGET,SPEC,LIMITS,SUITES,preflight,read_dev,stage,save,ref,bound,read_json,now
from jmicro.training import seed_all
from jmicro.phase5 import equal_state
from jmicro.model import JMicroModel
from jmicro.chat_evaluation import generate_reply
from phase6_performance import identity,alive,finite_state
import run_chat_natural as native
import evaluate_chat_natural as evaluation


def windows(c,tok):
    rows=[]
    for line in bound(c['NLL']).read_text().splitlines():
        row=json.loads(line);assert row['split'] in ('train','dev') and 'TEST' not in row['dataset']
        w=list(tok.sft_windows(row['messages'],1025))[-1];labels=np.asarray(w['labels'][1:])
        assert w['removed_turns']==0 and 2<=int((labels!=-100).sum())<=32
        rows.append((row,np.asarray(w['input_ids'][:-1]),labels))
    assert len(rows)==432;return rows


def wire():
    for module in (native,evaluation):
        for name,value in dict(RUN=RUN,DATA=DATA,BUDGET=BUDGET,SPEC=SPEC,LIMITS=LIMITS,SUITES=SUITES,stage=stage,read_dev=read_dev,require_ref=bound).items():setattr(module,name,value)
    native.read_bound=lambda value:read_json(bound(value))
    evaluation.windows=windows
    native.fixed_nll=evaluation.fixed_nll
    native.diagnostic=evaluation.diagnostic


def release():gc.collect();torch.cuda.empty_cache()


def fixture(rows):
    base=[r for r in rows if 'explicit_repeat_alias' not in r][:8]
    extra=[r for r in rows if r.get('explicit_repeat_alias')==0]
    for family in ('name','preference','correction','quantity','owner','literal','arithmetic','missing'):
        selected=[r for r in extra if r.get('family')==family]
        base.extend([selected[i] for i in (0,4,8,12)])
    for source in ('Dolly_llmjp','Aya_Japanese_TRAIN'):base.extend([r for r in extra if r['source']==source][:4])
    assert len(base)==48 and len({r['doc_id'] for r in base})==48
    return base


def probe(parent,c,tok,arms):
    assert not (RUN/'native_gate.json').exists()
    reports={};updates=0
    with stage('probe',c['config_sha256']) as (left,beat):
        for arm,rows in arms.items():
            selected=fixture(rows);trainer=native.build(parent,c,tok,selected,arm)
            assert not trainer.optimizer.state and equal_state({k:v.cpu() for k,v in trainer.model.state_dict().items()},parent['model'])
            timing=[]
            for _ in range(16):
                assert left()>30
                h=trainer.step();timing.append(h)
                with (RUN/'technical_all_steps.jsonl').open('a') as stream:stream.write(json.dumps(dict(arm=arm,branch='timing',**h),allow_nan=False)+'\n');stream.flush()
                beat(arm=arm,technical_update=trainer.update)
            assert finite_state(dict(model=trainer.model.state_dict(),optimizer=trainer.optimizer.state_dict()))
            dry=read_json(bound(c['arms'][arm]['dry_run']))
            forecast=max(h['seconds']/h['microbatches'] for h in timing)*dry['physical_microbatches']*1.35+300
            save(RUN/f'forecast_{arm}.json',dict(config_sha256=c['config_sha256'],all16_timings=timing,forecast_seconds=forecast,limit=LIMITS['train_'+arm]))
            assert forecast<=LIMITS['train_'+arm],(arm,forecast)
            del trainer;release();updates+=16
            snapshots=[];histories=[];directory=RUN/'native-resume'/arm;directory.mkdir(parents=True,exist_ok=True)
            for branch in ('continuous','resumed'):
                trainer=native.build(parent,c,tok,selected,arm);history=[]
                for i in range(2):
                    assert left()>30;h=trainer.step();history.append(h)
                    with (RUN/'technical_all_steps.jsonl').open('a') as stream:stream.write(json.dumps(dict(arm=arm,branch=branch,**h),allow_nan=False)+'\n');stream.flush()
                    if branch=='resumed' and i==0:
                        trainer.save(directory/'split.pt');del trainer;release();trainer=native.build(parent,c,tok,selected,arm);trainer.load(directory/'split.pt')
                trainer.save(directory/f'{branch}.pt');snapshots.append(torch.load(directory/f'{branch}.pt',map_location='cpu',weights_only=False));histories.append(history)
                updates+=2;del trainer;release()
            assert set(snapshots[0])==set(snapshots[1])
            checks={key:equal_state(snapshots[0][key],snapshots[1][key]) for key in snapshots[0]}
            for key in histories[0][0]:
                if key not in ('seconds','data_wait_seconds','teacher_tokens_per_second'):checks['history:'+key]=[r[key] for r in histories[0]]==[r[key] for r in histories[1]]
            assert all(checks.values()) and finite_state(snapshots[0]) and finite_state(snapshots[1])
            reports[arm]=dict(fixture_ids=[r['doc_id'] for r in selected],all16_timing_updates=timing,forecast_training_seconds=forecast,all_state_checks=checks,
                branch_history=histories,branch_snapshots={name:ref(directory/f'{name}.pt') for name in ('continuous','resumed','split')})
            del snapshots;release()
        trainer=native.build(parent,c,tok,fixture(arms['C0']),'C0');cases,_=read_dev(c['suites']['new'])
        selected=sorted(cases,key=lambda r:len(tok.chat_prompt(r['messages'],992)[0]),reverse=True)[:4];timings=[]
        for case in selected:
            assert left()>30;started=time.monotonic()
            with sdpa_kernel(SDPBackend.MATH):response=generate_reply(trainer.model,tok,case['messages'],'cuda','bf16',32,True)
            torch.cuda.synchronize();timings.append(dict(case_id=case['id'],seconds=time.monotonic()-started,tokens=response['generated_tokens']))
        forecast=max(t['seconds']/t['tokens'] for t in timings)*32*3466*1.5+600
        save(RUN/'evaluation_forecast.json',dict(config_sha256=c['config_sha256'],timings=timings,forecast_seconds=forecast,limit=LIMITS['evaluation'],quality_evidence=False))
        assert forecast<=LIMITS['evaluation'];del trainer;release();beat(passed=True)
    save(RUN/'native_gate.json',dict(passed=True,config_sha256=c['config_sha256'],arms=reports,technical_updates=updates,
        reused_maximum_shape=c['reused_maximum_shape'],evaluation_forecast_seconds=forecast,quality_evidence=False,science_updates=0,created_at=now()))


def public100(model,c,tok,arm,checkpoint,check,beat):
    path=RUN/'public100'/arm/'raw.json'
    cases=read_json(bound(c['public100']))['cases'];assert len(cases)==100
    if path.exists():
        out=read_json(path)
        assert out['config_sha256']==c['config_sha256'] and out['checkpoint']==checkpoint and out['cases']==c['public100']
        if out['status']=='complete_pending_literal_review':assert len(out['responses'])==200;return
        assert out['status']=='failed_partial_preserved' and out['error'].startswith('InterruptedError(')
        # Continue only genuinely interrupted output boundaries, never rerun a
        # failed/completed scientific condition or regenerate an old answer.
        previous=path.with_name('signal_partial_'+str(time.time_ns())+'.json');previous.write_bytes(path.read_bytes())
        out.update(status='running',resumed_at=now(),previous_partial=ref(previous))
    else:
        out=dict(status='running',created_at=now(),config_sha256=c['config_sha256'],checkpoint=checkpoint,cases=c['public100'],
            device='cuda',precision='BF16/math',decoding='greedy',max_new_tokens=32,responses=[])
    completed={(r['id'],r['turn']):r for r in out['responses']};assert len(completed)==len(out['responses'])
    save(path,out)
    try:
        for case in cases:
            history=[dict(m) for m in case['history']]
            for turn,target in enumerate(case['turns'],1):
                check();history.append(dict(role='user',content=target['user']))
                if (case['id'],turn) in completed:
                    prior=completed[case['id'],turn]
                    assert prior['messages']==history and prior['expected']==target['expected']
                    history.append(dict(role='assistant',content=prior['response']['text']));continue
                response=generate_reply(model,tok,history,'cuda','bf16',32,True,check)
                out['responses'].append(dict(id=case['id'],category=case['category'],mode=case['mode'],turn=turn,final=turn==len(case['turns']),
                    objective=target['objective'],expected=target['expected'],messages=[dict(m) for m in history],response=response))
                history.append(dict(role='assistant',content=response['text']));save(path,out)
            beat(arm=arm,public_cases=sum(r['final'] for r in out['responses']))
        assert len(out['responses'])==200
        out.update(status='complete_pending_literal_review',completed_at=now())
    except BaseException as error:out.update(status='failed_partial_preserved',error=repr(error));raise
    finally:save(path,out)


def evaluate(c,tok,stopped):
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
                public100(model,c,tok,arm,value,check,beat)
            del model;release()
    save(RUN/'evaluation_raw_complete.json',dict(status='all3466_raw_pending_literal_review',config_sha256=c['config_sha256'],responses=3466,
        protected_TEST_used=False,Chat_adopted=False,whole_goal_complete=False,created_at=now()))


def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['inspect','run']);a=p.parse_args()
    c,tok,arms=preflight(a.mode=='run')
    if a.mode=='inspect':windows(c,tok);print('New same-answer contract/all7 suites/NLL432 verified; CUDA not initialized');return
    jobpath=RUN/'pipeline.json'
    if jobpath.exists():
        old=read_json(jobpath);assert not alive(old) and old['status']=='signal_interrupted' and old['config_sha256']==c['config_sha256']
    torch.set_num_threads(2);torch.use_deterministic_algorithms(True);seed_all(42)
    assert torch.cuda.is_available() and '4090' in torch.cuda.get_device_name(0)
    stopped=[False]
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    wire();RUN.mkdir(parents=True,exist_ok=True);job=dict(**identity(),status='running',config_sha256=c['config_sha256'],started_at=now());save(jobpath,job)
    try:
        parent=native.load_parent(c)
        if not (RUN/'native_gate.json').exists():probe(parent,c,tok,arms)
        else:assert read_json(RUN/'native_gate.json')['passed'] and read_json(RUN/'native_gate.json')['config_sha256']==c['config_sha256']
        for arm,rows in arms.items():native.train(parent,c,tok,rows,arm,stopped)
        del parent;gc.collect();evaluate(c,tok,stopped)
        job.update(status='complete_raw_pending_content_and_browser',ended_at=now())
    except BaseException as error:
        job.update(status='signal_interrupted' if stopped[0] and isinstance(error,InterruptedError) else 'failed',error=repr(error),ended_at=now());raise
    finally:save(jobpath,job)


if __name__=='__main__':main()
