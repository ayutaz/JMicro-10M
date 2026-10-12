"""Native CUDA gates and two-arm teacher-budget learning, durable/resumable."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.teacher_chat_training import TeacherChatTrainer
from jmicro.training import atomic_json,seed_all
from jmicro.experiment import now,read_json,sha256
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state
from chat_generalization_contract import B,RUN,LIMITS,GPU_stage,load_parent,preflight,remaining


def trainer(parent,c,tok,rows,name,budget=B):
    return TeacherChatTrainer(parent,c['parent'],rows,tok,c['arms'][name]['data_directory'],c['spec'],budget,device='cuda')


def release():
    gc.collect();torch.cuda.empty_cache()


def cuda_probe(parent,c,tok,arms):
    path=RUN/'native_probe.json'
    if path.exists():
        result=read_json(path);assert result['passed'] and result['config_sha256']==c['config_sha256'];return
    reuse=read_json(RUN/'historical_control_preparation.json');assert reuse['passed']
    report={'D0':dict(read_json(Path(reuse['native_probe']['path']))['arms']['C1'],
        historical_reuse=True,source_evidence=reuse['native_probe'])};verification=0
    with GPU_stage('probe','native_changed_teacher_batch',c['config_sha256']) as (left,heartbeat):
        for name,rows in arms.items():
            if name=='D0':continue
            if left()<30:raise TimeoutError('Insufficient probe budget')
            t=trainer(parent,c,tok,rows,name);torch.cuda.reset_peak_memory_stats();history=[]
            for _ in range(8):
                if left()<10:raise TimeoutError('Probe budget reserve reached')
                history.append(t.step());heartbeat(arm=name,completed_updates=t.update)
            assert finite_state(dict(model=t.model.state_dict(),optimizer=t.optimizer.state_dict()))
            rates=sorted(r['seconds']/r['microbatches'] for r in history[2:])
            dry=read_json(RUN/f'{name}_dry_run.json')
            forecast=max(rates)*1.35*dry['microbatches']+60.
            report[name]=dict(history=history,peak_allocated_bytes=torch.cuda.max_memory_allocated(),
                max_steady_seconds_per_microbatch=max(rates),forecast_training_seconds=forecast,
                forecast_limit_seconds=LIMITS['train_D1'],within_limit=forecast<=LIMITS['train_D1'],
                observed_microbatch_counts=sorted({r['microbatches'] for r in history}),
                actual_complete_update_bound=True,finite=True)
            verification+=t.supervised_tokens
            # Force a native final partial frame and the complete target/EOT.
            del t;release();t=trainer(parent,c,tok,rows,name,1);last=t.step()
            assert 2<=t.supervised_tokens<=65 and t.sampler.examples==1 and finite_state(dict(model=t.model.state_dict(),optimizer=t.optimizer.state_dict()))
            report[name]['terminal_budget1_row']=last;verification+=t.supervised_tokens
            del t;release()
        assert all(r['within_limit'] for r in report.values()),'Frozen training allocation cannot fit the measured workload'
    atomic_json(path,dict(passed=True,config_sha256=c['config_sha256'],arms=report,
        verification_Assistant_teachers=verification,GPU_optimizer_updates=9,quality_evidence=False,
        D0_historical_gate_reuse=reference_reuse(reuse,'native_probe'),
        candidate_learning_updates=0,observed_at=now()))


def one_resume_gate(parent,c,tok,rows,name,tag,budget):
    directory=RUN/'native-resume'/f'{name}-{tag}';directory.mkdir(parents=True,exist_ok=True)
    histories=[];states=[]
    for branch in ('continuous','resumed'):
        t=trainer(parent,c,tok,rows,name,budget);history=[]
        for update in range(4):
            history.append(t.step())
            if branch=='resumed' and update==1:
                t.save(directory/'split.pt');del t;release()
                t=trainer(parent,c,tok,rows,name,budget);t.load(directory/'split.pt')
        t.save(directory/f'{branch}.pt');states.append(torch.load(directory/f'{branch}.pt',map_location='cpu',weights_only=False))
        histories.append(history);del t;release()
    keys=('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','lineage','update','spec')
    checks={k:equal_state(states[0][k],states[1][k]) for k in keys}
    for key in ('loss','gradient_norm','lr','assistant_teacher_tokens','EOT_teachers','token_digest'):
        checks['history_'+key]=[r[key] for r in histories[0]]==[r[key] for r in histories[1]]
    checks['finite_history']=all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for h in histories for r in h)
    assert all(checks.values()),checks
    if tag=='epoch-and-terminal':
        assert states[0]['sampler']['epoch']>0 and budget<=states[0]['supervised_tokens']<=budget+64
        assert histories[0][-1]['teachers_this_update']<512
    return dict(passed=True,checks=checks,history=histories,budget=budget,targets_in_fixture=states[0]['sampler']['windows'],
        verification_Assistant_teachers=sum(s['supervised_tokens'] for s in states),GPU_optimizer_updates=8,
        checkpoint_refs={b:dict(path=str(directory/f'{b}.pt'),sha256=sha256(directory/f'{b}.pt')) for b in ('continuous','resumed')})


def reference_reuse(reuse,key):
    return dict(source=reuse[key],new_GPU_optimizer_updates=0,new_learning_updates=0)


def cuda_resume(parent,c,tok,arms):
    path=RUN/'native_resume_gate.json'
    if path.exists():
        result=read_json(path);assert result['passed'] and result['config_sha256']==c['config_sha256'];return
    reuse=read_json(RUN/'historical_control_preparation.json');assert reuse['passed']
    prior=read_json(Path(reuse['native_resume']['path']))['gates']
    gates={'D0-'+tag:dict(prior['C1-'+tag],historical_reuse=True,
        source_evidence=reuse['native_resume']) for tag in ('full-contract','epoch-and-terminal')}
    with GPU_stage('resume','exact_native_all_state',c['config_sha256']) as (left,heartbeat):
        for name,rows in arms.items():
            if name=='D0':continue
            for tag,fixture,budget in (('full-contract',rows,B),('epoch-and-terminal',rows[:3],1777)):
                if left()<30:raise TimeoutError('Native resume gate budget reserve reached')
                gates[f'{name}-{tag}']=one_resume_gate(parent,c,tok,fixture,name,tag,budget)
                heartbeat(completed=list(gates))
    atomic_json(path,dict(passed=True,config_sha256=c['config_sha256'],gates=gates,
        verification_Assistant_teachers=sum(g['verification_Assistant_teachers'] for k,g in gates.items() if k.startswith('D1-')),
        GPU_optimizer_updates=16,D0_historical_gate_reuse=reference_reuse(reuse,'native_resume'),
        quality_evidence=False,candidate_learning_updates=0,completed_at=now()))


def train_arm(parent,c,tok,rows,name,until,stopped):
    directory=RUN/name;directory.mkdir(parents=True,exist_ok=True)
    job_path=directory/'job.json';old=read_json(job_path) if job_path.exists() else {}
    if old:
        assert not alive(old) and old['config_sha256']==c['config_sha256']
        if old['status']=='learning_complete':return
    for gate in ('native_probe.json','native_resume_gate.json','evaluation_forecast.json'):
        g=read_json(RUN/gate);assert g['passed'] and g['config_sha256']==c['config_sha256'],gate
    threshold=(B*until+2)//3
    job=dict(**identity(),status='starting',arm=name,config_sha256=c['config_sha256'],until_savepoint=until,started_at=now())
    atomic_json(job_path,job)
    try:
        with GPU_stage('train_'+name,name,c['config_sha256']) as (left,heartbeat):
            t=trainer(parent,c,tok,rows,name)
            latest=directory/'latest.json'
            if latest.exists():
                ref=read_json(latest);assert sha256(Path(ref['path']))==ref['sha256'];t.load(ref['path'])
            points=read_json(directory/'checkpoints.json') if (directory/'checkpoints.json').exists() else {}
            metrics=directory/'metrics.jsonl'
            # Discard rows beyond last persisted update; never advance the
            # optimizer using a partially persisted/logged sampler state.
            prior=[json.loads(l) for l in metrics.read_text().splitlines()] if metrics.exists() else []
            prior=[r for r in prior if r['update']<=t.update]
            with metrics.open('w') as f:
                for r in prior:f.write(json.dumps(r,allow_nan=False)+'\n')
            max_step=max([r['seconds'] for r in prior] or [2.])
            def save():
                path=directory/f'checkpoint-{t.update:08d}.pt';t.save(path)
                ref=dict(path=str(path),sha256=sha256(path),update=t.update,Assistant_teachers=t.supervised_tokens,
                    valid_inputs=t.tokens,physical_inputs=t.sampler.physical_tokens,EOT_teachers=t.sampler.eot_teachers)
                atomic_json(latest,ref);return ref
            if not latest.exists():save()
            with metrics.open('a',buffering=1) as f:
                while t.supervised_tokens<threshold:
                    # Stop between completed updates. Reserve time for a full
                    # step and checkpoint rather than interrupting a microbatch.
                    if stopped[0] or left()<max(20.,max_step*2+5):
                        save();raise InterruptedError('Whole-update stop or frozen GPU budget reserve')
                    row=t.step();max_step=max(max_step,row['seconds']);f.write(json.dumps(row,allow_nan=False)+'\n')
                    reached=[i for i in (1,2,3) if t.supervised_tokens>=(B*i+2)//3 and f't{i}' not in points]
                    if reached or t.update%250==0:
                        ref=save()
                        for i in reached:points[f't{i}']=dict(ref,requested_teachers=(B*i+2)//3)
                        atomic_json(directory/'checkpoints.json',points)
                    if t.update==1 or t.update%100==0 or reached:
                        heartbeat(update=t.update,Assistant_teachers=t.supervised_tokens,checkpointed_update=read_json(latest)['update'])
                        job.update(status='training',update=t.update,Assistant_teachers=t.supervised_tokens,heartbeat_at=now())
                        atomic_json(job_path,job);print(json.dumps(dict(arm=name,**row),allow_nan=False),flush=True)
            ref=save();assert finite_state(dict(model=t.model.state_dict(),optimizer=t.optimizer.state_dict()))
            if until==3:assert B<=t.supervised_tokens<=B+64 and set(points)=={'t1','t2','t3'}
            result=dict(status='learning_complete' if until==3 else 'saved_for_planned_screen',config_sha256=c['config_sha256'],
                checkpoint=ref,checkpoints=points,actual_sampler=t.sampler.state_dict(),lineage=t.lineage,
                teacher_budget=B,until_savepoint=until,parameter_count=10001152,Base_adopted=False,Chat_adopted=False,
                quality_evaluated=False,requested_stages_0_to_5_complete=False,completed_at=now())
            atomic_json(directory/'result.json',result);job.update(status=result['status'],completed_at=now(),checkpoint=ref)
            del t;release()
    except BaseException as exc:
        job.update(status='stopped_or_failed',error=repr(exc),ended_at=now());raise
    finally:atomic_json(job_path,job)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--config',type=Path,required=True)
    parser.add_argument('--mode',choices=('probe','resume','train'),required=True)
    parser.add_argument('--arm',choices=('both','D0','D1'),default='both')
    parser.add_argument('--until',type=int,choices=(1,2,3),default=1);parser.add_argument('--inspect',action='store_true')
    args=parser.parse_args();c,tok,arms=preflight(args.config.resolve())
    if args.inspect:print('Frozen contract/TRAIN/DEV/NLL CPU preflight passed; no GPU launch');return
    torch.set_num_threads(2);torch.use_deterministic_algorithms(True);seed_all(42)
    assert torch.cuda.is_available() and '4090' in torch.cuda.get_device_name(0)
    stopped=[False];signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    parent=load_parent(c)
    if args.mode=='probe':cuda_probe(parent,c,tok,arms)
    elif args.mode=='resume':cuda_resume(parent,c,tok,arms)
    else:
        for name,rows in arms.items():
            if args.arm in ('both',name):train_arm(parent,c,tok,rows,name,args.until,stopped)

if __name__=='__main__':main()
