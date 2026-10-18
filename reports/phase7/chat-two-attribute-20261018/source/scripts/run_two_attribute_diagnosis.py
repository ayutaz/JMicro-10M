"""New fixed TRAIN64 experiment; native arithmetic and closed sources unchanged."""
import argparse
import gc
import json
import os
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import signal
import time
import torch
from torch.nn.attention import sdpa_kernel,SDPBackend
from two_attribute_contract import ROOT,RUN,DATA,BUDGET,CONFIG,LIMITS,preflight,stage
from answer_learning_common import save,ref,bound,read_json,now
from jmicro.teacher_chat_training import TeacherChatTrainer
from jmicro.training import seed_all
from jmicro.phase5 import equal_state
from jmicro.model import JMicroModel
from jmicro.chat_evaluation import generate_reply
from phase6_performance import identity,alive,finite_state
import run_chat_natural as native
import evaluate_chat_natural as evaluation
from chat_recovery_contract import read_dev
import run_chat_recovery_sft as recovery

def release():gc.collect();torch.cuda.empty_cache()
def build(parent,c,tok,rows):return TeacherChatTrainer(parent,c['parent'],rows,tok,DATA,c['spec'],BUDGET,device='cuda')

def probe(parent,c,tok,rows):
    assert not (RUN/'native_gate.json').exists();checks={}
    with stage('probe',c['config_sha256']) as (left,beat):
        t=build(parent,c,tok,rows);assert not t.optimizer.state
        assert equal_state({k:v.cpu() for k,v in t.model.state_dict().items()},parent['model'])
        timings=[]
        for _ in range(32):
            assert left()>30;timings.append(t.step());beat(update=t.update)
        save(RUN/'all32_technical_timings.json',timings)
        dry=read_json(bound(c['replay']))
        forecast=max(h['seconds']/h['microbatches'] for h in timings)*dry['physical_microbatches']*1.35+180
        assert forecast<LIMITS['training'],forecast
        del t;release();snapshots=[];histories=[]
        for branch in ('continuous','resumed'):
            t=build(parent,c,tok,rows);history=[]
            directory=RUN/'resume-proof';directory.mkdir(parents=True,exist_ok=True)
            for i in range(6):
                assert left()>30;history.append(t.step())
                if branch=='resumed' and i==2:
                    t.save(directory/'split.pt');del t;release();t=build(parent,c,tok,rows);t.load(directory/'split.pt')
            t.save(directory/f'{branch}.pt');snapshots.append(torch.load(directory/f'{branch}.pt',map_location='cpu',weights_only=False));histories.append(history)
            del t;release()
        assert set(snapshots[0])==set(snapshots[1])
        checks.update({k:equal_state(snapshots[0][k],snapshots[1][k]) for k in snapshots[0]})
        for k in histories[0][0]:
            if k not in ('seconds','data_wait_seconds','teacher_tokens_per_second'):checks['history:'+k]=[r[k] for r in histories[0]]==[r[k] for r in histories[1]]
        assert all(checks.values()) and all(finite_state(s) for s in snapshots)
        del snapshots;release()
        model=JMicroModel(parent['model_config']).cuda();model.load_state_dict(parent['model'],strict=True);model.eval().requires_grad_(False)
        cases,_=read_dev(c['suites']['new']);dev=read_json(bound(c['DEV']))
        inputs=[r['messages'][:-1] for r in rows]+[r['messages'] for r in dev['groups']['unseen_structure']]+[r['messages'] for r in cases]
        inputs=sorted(inputs,key=lambda m:len(tok.chat_prompt(m,992)[0]),reverse=True)[:4];eval_timings=[]
        with sdpa_kernel(SDPBackend.MATH):
            for messages in inputs:
                assert left()>30;started=time.monotonic();r=generate_reply(model,tok,messages,'cuda','bf16',32,True);torch.cuda.synchronize()
                eval_timings.append(dict(prompt_tokens=r['prompt_tokens'],tokens=r['generated_tokens'],seconds=time.monotonic()-started))
        rate=max(r['seconds']/r['tokens'] for r in eval_timings)
        diagnosis=rate*32*240*1.5+180;regression=rate*32*1733*1.5+600
        assert diagnosis<LIMITS['diagnosis'] and regression<LIMITS['regression'],(diagnosis,regression)
        save(RUN/'native_gate.json',dict(passed=True,created_at=now(),config_sha256=c['config_sha256'],technical_updates=44,
            all32_timings=timings,resume_checks=checks,resume_histories=histories,training_forecast_seconds=forecast,
            diagnosis_forecast_seconds=diagnosis,regression_forecast_seconds=regression,evaluation_timings=eval_timings,
            original_maximum_shape=c['reused_maximum_shape'],quality_evidence=False))
        del model;release();beat(passed=True)

def diagnostic(model,c,tok,rows,point,check,beat):
    path=RUN/f'diagnosis/{point}.json';assert not path.exists();dev=read_json(bound(c['DEV']));responses=[]
    groups={'TRAIN':rows}
    if point=='after':groups.update(dev['groups'])
    out=dict(config_sha256=c['config_sha256'],point=point,status='running',precision='BF16/math',max_new_tokens=32,responses=responses)
    save(path,out)
    try:
        for group,cases in groups.items():
            for case in cases:
                check();messages=case['messages'][:-1] if group=='TRAIN' else case['messages']
                r=generate_reply(model,tok,messages,'cuda','bf16',32,True,check)
                responses.append(dict(group=group,id=case.get('id',case.get('doc_id')),case=case,messages=messages,response=r))
                save(path,out)
            beat(diagnosis=point,responses=len(responses))
        if point=='after':
            for case in dev['own']:
                history=[]
                for turn,target in enumerate(case['turns'],1):
                    check();history.append(dict(role='user',content=target['user']))
                    r=generate_reply(model,tok,history,'cuda','bf16',32,True,check)
                    responses.append(dict(group='own',id=case['id'],turn=turn,final=turn==3,case=case,target=target,messages=[dict(m) for m in history],response=r))
                    history.append(dict(role='assistant',content=r['text']));save(path,out)
                beat(diagnosis=point,responses=len(responses))
        assert len(responses)==(64 if point=='before' else 176)
        out.update(status='complete_pending_literal_review',completed_at=now())
    except BaseException as error:out.update(status='failed_partial_preserved',error=repr(error));raise
    finally:save(path,out)

def train(parent,c,tok,rows,stopped):
    with stage('training',c['config_sha256']) as (left,beat):
        t=build(parent,c,tok,rows);dry=read_json(bound(c['replay']))
        assert t.sampler.binding==dry['sampler_binding'] and not t.optimizer.state
        assert equal_state({k:v.cpu() for k,v in t.model.state_dict().items()},parent['model'])
        directory=RUN/'model';directory.mkdir(parents=True,exist_ok=True);metrics=directory/'metrics.jsonl'
        assert not metrics.exists()
        t.save(directory/'initial.pt');save(RUN/'initial.json',ref(directory/'initial.pt'))
        with metrics.open('x',buffering=1) as stream:
            while t.supervised_tokens<BUDGET:
                if stopped[0] or left()<30:
                    t.save(directory/f'checkpoint-{t.update:08d}.pt');raise InterruptedError('Signal or finite allocation boundary')
                h=t.step();stream.write(json.dumps(h,allow_nan=False)+'\n')
                expected=dry['history'][t.update-1]
                for key,expected_key in [('supervised_tokens','teachers'),('token_digest','token_digest'),('microbatches','microbatches'),('lr','lr'),('EOT_teachers','eot_teachers'),('valid_input_tokens','input_tokens'),('physical_input_tokens','physical_tokens')]:
                    assert h[key]==expected[expected_key],(t.update,key)
                if t.update%100==0:t.save(directory/f'checkpoint-{t.update:08d}.pt')
                if t.update==1 or t.update%20==0:beat(update=t.update,teachers=t.supervised_tokens,loss=h['loss']);print(json.dumps(h),flush=True)
        path=directory/f'checkpoint-{t.update:08d}.pt';t.save(path)
        assert t.update==dry['updates'] and t.sampler.state_dict()==dry['sampler_terminal']
        assert finite_state(dict(model=t.model.state_dict(),optimizer=t.optimizer.state_dict()))
        save(RUN/'learning_complete.json',dict(config_sha256=c['config_sha256'],created_at=now(),checkpoint=ref(path),updates=t.update,teachers=t.supervised_tokens,
            sampler=t.sampler.state_dict(),all_CPU_consumption_history_exact=True,finite_state=True,adopted=False))
        del t;release()

def load_model(value):
    s=torch.load(bound(value),map_location='cpu',weights_only=False);model=JMicroModel(s['model_config']).cuda();model.load_state_dict(s['model'],strict=True)
    model.eval().requires_grad_(False);assert sum(p.numel() for p in model.parameters())==10001152;del s;return model

def main():
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['inspect','run']);a=p.parse_args();c,tok,rows=preflight()
    if a.mode=='inspect':print('Frozen TRAIN64/DEV64/own16, original numerical sources and finite contract verified; no CUDA initialized');return
    jobpath=RUN/'pipeline.json';assert not jobpath.exists(),'Existing run must be audited; no automatic restart'
    torch.set_num_threads(2);torch.use_deterministic_algorithms(True);seed_all(42)
    assert torch.cuda.is_available() and '4090' in torch.cuda.get_device_name(0)
    stopped=[False]
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    job=dict(**identity(),status='running',config_sha256=c['config_sha256'],started_at=now());save(jobpath,job)
    try:
        parent=native.load_parent(c);probe(parent,c,tok,rows)
        with stage('diagnosis',c['config_sha256']) as (left,beat):
            def check():
                if stopped[0] or left()<20:raise InterruptedError('Stop at output boundary')
            model=JMicroModel(parent['model_config']).cuda();model.load_state_dict(parent['model'],strict=True);model.eval().requires_grad_(False)
            with sdpa_kernel(SDPBackend.MATH):diagnostic(model,c,tok,rows,'before',check,beat)
            del model;release()
        train(parent,c,tok,rows,stopped);del parent;release();checkpoint=read_json(RUN/'learning_complete.json')['checkpoint']
        with stage('diagnosis',c['config_sha256']) as (left,beat):
            def check():
                if stopped[0] or left()<20:raise InterruptedError('Stop at output boundary')
            model=load_model(checkpoint)
            with sdpa_kernel(SDPBackend.MATH):diagnostic(model,c,tok,rows,'after',check,beat)
            del model;release()
        # Frozen old evaluation algorithms are wired only to new output locations.
        evaluation.RUN=RUN;evaluation.stage=stage;evaluation.read_dev=read_dev;evaluation.require_ref=bound
        recovery.RUN=RUN
        with stage('regression',c['config_sha256']) as (left,beat):
            def check():
                if stopped[0] or left()<20:raise InterruptedError('Stop at output boundary')
            model=load_model(checkpoint)
            with sdpa_kernel(SDPBackend.MATH):
                for suite in c['suites']:evaluation.final_suite(model,c,tok,'D',suite,checkpoint,check,beat)
                recovery.public100(model,c,tok,'D',checkpoint,check,beat)
            del model;release()
        job.update(status='complete_raw_pending_review',ended_at=now())
    except BaseException as error:job.update(status='signal_interrupted' if stopped[0] and isinstance(error,InterruptedError) else 'failed',error=repr(error),ended_at=now());raise
    finally:save(jobpath,job)

if __name__=='__main__':main()
