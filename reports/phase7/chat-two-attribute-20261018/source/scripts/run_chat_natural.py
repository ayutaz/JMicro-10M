"""Owned native10M SFT: finite CUDA gate, exact resume, two matched fresh arms."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.teacher_chat_training import TeacherChatTrainer
from jmicro.training import atomic_json, autocast, seed_all, rng_state
from jmicro.phase5 import equal_state
from jmicro.experiment import read_json, now
from phase6_performance import identity, alive, finite_state
from chat_natural_contract import ROOT, RUN, DATA, BUDGET, SPEC, LIMITS, preflight, require_ref, read_bound, ref, stage
from evaluate_chat_natural import fixed_nll, diagnostic, evaluate_all, windows, nll_batch
from jmicro.chat_evaluation import generate_reply


def release():
    gc.collect(); torch.cuda.empty_cache()


def build(parent,c,tok,rows,arm,budget=BUDGET):
    return TeacherChatTrainer(parent,c['parent'],rows,tok,DATA,SPEC,budget,device='cuda')


def load_parent(c):
    state=torch.load(require_ref(c['parent']),map_location='cpu',weights_only=False)
    assert state['implementation_sha256']==c['implementation'] and state['update']==305176
    assert state['supervised_tokens']==9978838479 and state['tokens']==10000007168
    assert not state['spec'].get('teacher_chat') and not state['spec'].get('assistant_training')
    assert finite_state(state)
    return state


def probe(parent,c,tok,arms):
    target=RUN/'native_gate.json'
    if target.exists():
        old=read_json(target); assert old['passed'] and old['config_sha256']==c['config_sha256']
        return
    ledger=read_json(RUN/'GPU_ledger.json') if (RUN/'GPU_ledger.json').exists() else {'entries':[]}
    assert not any(r['category']=='probe' for r in ledger['entries']), 'Do not reopen a completed or failed gate'
    reports={}; verification_teachers=0; verification_updates=0
    with stage('probe',c['config_sha256']) as (left,beat):
        for arm,rows in arms.items():
            fixture=rows[:48]
            t=build(parent,c,tok,fixture,arm)
            assert not t.optimizer.state and equal_state({k:v.detach().cpu() for k,v in t.model.state_dict().items()},parent['model'])
            maximum=None
            if arm=='C0':
                # FIRST32x1024 finite joint backward. Borrow known TRAIN body
                # IDs only; this is a synthetic capacity fixture, no Adam step.
                body=tok.encode(fixture[0]['messages'][0]['text'])
                x=torch.tensor(np.resize(np.array(body,dtype=np.int64),(32,1024)),device='cuda')
                y=torch.full_like(x,-100); y[:,-16:]=x[:,-16:]; y[:,-1]=7
                before=rng_state();torch.cuda.reset_peak_memory_stats()
                with sdpa_kernel(SDPBackend.MATH),autocast('cuda','bf16'):
                    logits=t.model(x,attention_mask=x.ne(0)).logits
                    loss=F.cross_entropy(logits.reshape(-1,4096),y.reshape(-1),ignore_index=-100)
                loss.backward()
                assert torch.isfinite(loss) and all(p.grad is not None and bool(torch.isfinite(p.grad).all()) for p in t.model.parameters())
                assert equal_state({k:v.detach().cpu() for k,v in t.model.state_dict().items()},parent['model']) and not t.optimizer.state
                assert equal_state(before,rng_state())
                maximum=dict(shape=[32,1024], finite_joint_backward=True, optimizer_updates=0,
                    peak_allocated_bytes=torch.cuda.max_memory_allocated(), model_unchanged=True, RNG_unchanged=True,
                    synthetic_capacity_fixture=True, labels_borrowed_TRAIN_positions=512)
                del x,y,logits,loss
                t.optimizer.zero_grad(set_to_none=True);torch.cuda.empty_cache()
            history=[]
            with sdpa_kernel(SDPBackend.MATH):
                for _ in range(8):
                    assert left()>30
                    history.append(t.step())
                    beat(arm=arm,verification_update=t.update)
            assert finite_state(dict(model=t.model.state_dict(),optimizer=t.optimizer.state_dict()))
            rate=max(r['seconds']/r['microbatches'] for r in history[2:])
            dry=read_bound(c['arms'][arm]['dry_run'])
            forecast=rate*dry['physical_microbatches']*1.35+180.
            assert forecast <= LIMITS['train_'+arm], 'Do not start an unmeasured over-budget condition'
            verification_teachers+=t.supervised_tokens; verification_updates+=8
            if arm=='C0':
                # Dedicated max-length prompt timing, not a quality comparison.
                from chat_natural_contract import read_dev
                cases,_=read_dev(c['suites']['new'])
                selected=sorted(cases,key=lambda r:len(tok.chat_prompt(r['messages'],992)[0]),reverse=True)[:4]
                timings=[]
                for case in selected:
                    started=time.monotonic()
                    with sdpa_kernel(SDPBackend.MATH):
                        row=generate_reply(t.model,tok,case['messages'],'cuda','bf16',32,True)
                    torch.cuda.synchronize()
                    timings.append(dict(seconds=time.monotonic()-started,tokens=row['generated_tokens']))
                token_rate=max(r['seconds']/r['tokens'] for r in timings)
                estimate=token_rate*32*2190*1.5+600.
                assert estimate <= LIMITS['evaluation']
                atomic_json(RUN/'evaluation_forecast.json',dict(passed=True,config_sha256=c['config_sha256'],
                    timings=timings, forecast_seconds=estimate,limit_seconds=LIMITS['evaluation'],
                    quality_evidence=False,assumes_max32_tokens_all2190=True))
            del t;release()
            # Original native arithmetic is unchanged. Test both changed data
            # paths with actual CUDA all-state2 vs1+save+1, not fixture counts.
            histories=[];states=[]
            directory=RUN/'native-resume'/arm;directory.mkdir(parents=True,exist_ok=True)
            for branch in ('continuous','resumed'):
                t=build(parent,c,tok,fixture,arm); h=[]
                for i in range(2):
                    with sdpa_kernel(SDPBackend.MATH): h.append(t.step())
                    if branch=='resumed' and i==0:
                        t.save(directory/'split.pt'); del t;release()
                        t=build(parent,c,tok,fixture,arm);t.load(directory/'split.pt')
                t.save(directory/f'{branch}.pt')
                states.append(torch.load(directory/f'{branch}.pt',map_location='cpu',weights_only=False))
                histories.append(h);verification_teachers+=t.supervised_tokens;verification_updates+=2
                del t;release()
            keys=('model','optimizer','scheduler','rng','sampler','update','tokens','supervised_tokens','body_bytes','token_digest','lineage','spec')
            checks={k:equal_state(states[0][k],states[1][k]) for k in keys}
            for k in ('loss','gradient_norm','lr','teachers_this_update','assistant_teacher_tokens','EOT_teachers','token_digest'):
                checks['history_'+k]=[r[k] for r in histories[0]]==[r[k] for r in histories[1]]
            assert all(checks.values()),checks
            assert finite_state(states[0]) and finite_state(states[1])
            reports[arm]=dict(maximum_shape=maximum, timing_history=history, rate_seconds_per_microbatch=rate,
                forecast_training_seconds=forecast, resume_checks=checks, resume_histories=histories,
                numerical_snapshots={b:ref(directory/f'{b}.pt') for b in ('continuous','resumed')})
            del states;release()
    atomic_json(target,dict(passed=True,config_sha256=c['config_sha256'],arms=reports,
        verification_optimizer_updates=verification_updates,verification_Assistant_teachers=verification_teachers,
        scientific_learning_updates=0,quality_evidence=False,completed_at=now()))
    print(json.dumps(dict(passed=True,verification_updates=verification_updates,
        forecasts={a:r['forecast_training_seconds'] for a,r in reports.items()})),flush=True)


def train(parent,c,tok,rows,arm,stopped):
    directory=RUN/arm;directory.mkdir(parents=True,exist_ok=True)
    job_path=directory/'job.json'
    old=read_json(job_path) if job_path.exists() else None
    if old:
        assert not alive(old) and old['config_sha256']==c['config_sha256']
        if old['status']=='learning_complete':
            return
        assert old['status']=='signal_interrupted', 'Failed/completed conditions are not relaunched'
    gate=read_json(RUN/'native_gate.json')
    assert gate['passed'] and gate['config_sha256']==c['config_sha256']
    job=dict(**identity(),arm=arm,status='starting',config_sha256=c['config_sha256'],started_at=now())
    atomic_json(job_path,job)
    try:
        with stage('train_'+arm,c['config_sha256']) as (left,beat):
            t=build(parent,c,tok,rows,arm)
            assert t.sampler.binding==c['arms'][arm]['sampler_binding']
            assert sum(p.numel() for p in t.model.parameters())==10001152
            latest=directory/'latest.json'
            if latest.exists():
                value=read_json(latest);require_ref(value);t.load(value['path'])
            points=read_json(directory/'checkpoints.json') if (directory/'checkpoints.json').exists() else {}
            def check():
                if stopped[0] or left()<30:
                    raise InterruptedError('Signal or allocation reserve at completed boundary')
            def save():
                path=directory/f'checkpoint-{t.update:08d}.pt';t.save(path)
                value=dict(ref(path),update=t.update,Assistant_teachers=t.supervised_tokens,
                           valid_inputs=t.tokens,physical_inputs=t.sampler.physical_tokens,EOT_teachers=t.sampler.eot_teachers)
                atomic_json(latest,value)
                return value
            if not latest.exists():
                initial=save()
                if arm=='C0':
                    fixed_nll(t.model,c,tok,'parent','t0',c['parent'],check)
            metrics=directory/'metrics.jsonl'
            if metrics.exists():
                prior=[json.loads(line) for line in metrics.read_text().splitlines()]
                if any(r['update']>t.update for r in prior):
                    metrics.rename(directory/f'unpersisted-metrics-{time.time_ns()}.jsonl')
                    with metrics.open('w') as stream:
                        for r in prior:
                            if r['update']<=t.update:stream.write(json.dumps(r)+'\n')
            with metrics.open('a',buffering=1) as stream:
                while t.supervised_tokens<BUDGET:
                    if stopped[0] or left()<30:
                        save();raise InterruptedError('Stop after a completed update')
                    with sdpa_kernel(SDPBackend.MATH): row=t.step()
                    stream.write(json.dumps(row,allow_nan=False)+'\n')
                    reached=[p for p in (250000,500000,1000000) if t.supervised_tokens>=p and str(p) not in points]
                    if reached or t.update%250==0:
                        value=save()
                        for p in reached:points[str(p)]=dict(value,requested_teachers=p)
                        atomic_json(directory/'checkpoints.json',points)
                        if reached:
                            point=str(reached[-1])
                            fixed_nll(t.model,c,tok,arm,point,value,check)
                            if int(point)<BUDGET:diagnostic(t.model,c,tok,arm,point,value,check)
                    if t.update==1 or t.update%50==0 or reached:
                        beat(update=t.update,Assistant_teachers=t.supervised_tokens,checkpointed_update=read_json(latest)['update'])
                        job.update(status='training',update=t.update,Assistant_teachers=t.supervised_tokens,heartbeat_at=now())
                        atomic_json(job_path,job)
                        print(json.dumps(dict(arm=arm,**row),allow_nan=False),flush=True)
            value=save()
            assert BUDGET<=t.supervised_tokens<=BUDGET+31 and len(points)==3
            assert finite_state(dict(model=t.model.state_dict(),optimizer=t.optimizer.state_dict()))
            expected=read_bound(c['arms'][arm]['dry_run'])
            assert t.sampler.state_dict()==expected['sampler_terminal'] and t.update==expected['updates']
            result=dict(status='learning_complete',config_sha256=c['config_sha256'],checkpoint=value,
                checkpoints=points,sampler=t.sampler.state_dict(),lineage=t.lineage,parameter_count=10001152,
                quality_evaluated=False,Chat_adopted=False,Base_adopted=False,protected_TEST_used=False,completed_at=now())
            atomic_json(directory/'result.json',result)
            job.update(status='learning_complete',checkpoint=value,completed_at=now())
            del t;release()
    except BaseException as error:
        job.update(status='signal_interrupted' if stopped[0] and isinstance(error,InterruptedError) else 'failed',
                   error=repr(error),ended_at=now())
        raise
    finally:
        atomic_json(job_path,job)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--mode',choices=('probe','pipeline','evaluate'),required=True)
    p.add_argument('--inspect',action='store_true')
    args=p.parse_args()
    c,tok,arms=preflight()
    if args.inspect:
        print('Frozen contract, bounded TRAIN, dedicated DEV-only exports: preflight passed; no CUDA execution')
        return
    torch.set_num_threads(2);torch.use_deterministic_algorithms(True);seed_all(42)
    assert torch.cuda.is_available() and '4090' in torch.cuda.get_device_name(0)
    stopped=[False]
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True))
    signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    if args.mode=='evaluate':
        evaluate_all(c,tok,stopped)
        return
    parent=load_parent(c)
    if args.mode=='probe':
        probe(parent,c,tok,arms)
    else:
        for arm,rows in arms.items():
            train(parent,c,tok,rows,arm,stopped)
        del parent;gc.collect()
        evaluate_all(c,tok,stopped)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    main()
