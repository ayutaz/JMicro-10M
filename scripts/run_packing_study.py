"""Plan68: equal teacher-budget three-arm packing and conditional mixed100M."""
import argparse
import copy
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.condition_diagnostic import make_pairs
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.packing_study import PackingTrainer
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,implementation_hashes,seed_all
from jmicro.training import gpu_lock
from phase6_performance import identity,alive,finite_state
import run_eos_short_pilot as pilot
import run_condition_diagnostic as old
import run_complete_text_comparison as comparison

RUN=ROOT/'reports/phase6/packing-study-20261005'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/packing-study-20261005')
CONFIG=ROOT/'configs/phase6/packing_study.json'
SOURCES=('scripts/run_packing_study.py','scripts/run_packing_study.ps1','src/jmicro/packing_study.py',
    'tests/test_packing_study.py','docs/68_packing_learning_execution.md','scripts/run_condition_diagnostic.py',
    'src/jmicro/condition_diagnostic.py','scripts/run_complete_text_comparison.py','src/jmicro/eos_pilot.py',
    'src/jmicro/low_lr_pilot.py','src/jmicro/japanese_evaluation.py','src/jmicro/evaluation_memory.py')


def prepare():
    if CONFIG.exists():load_config();print('Frozen preparation retained');return
    assert not (RUN/'job.json').exists()
    suites=list(ET.parse(RUN/'tests.xml').getroot().iter('testsuite'))
    assert sum(int(s.attrib['tests']) for s in suites)>=4 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped'))
    base=old.load_config();DATA.mkdir(parents=True,exist_ok=True);RUN.mkdir(parents=True,exist_ok=True)
    previous=read_json(old.DATA/'dev.json');known={r['text'] for r in previous}
    candidates=make_pairs('dev',30,[0,4],202610071);fresh=[]
    for category in ('reference','quantity','negation','time','cause'):
        for template in (0,4):
            chosen=[]
            families={r['family'] for r in candidates if r['category']==category and r['template']==template}
            for family in sorted(families):
                rows=[r for r in candidates if r['family']==family]
                if not any(r['text'] in known for r in rows):chosen.extend(rows)
                if len(chosen)==10:break
            assert len(chosen)==10
            fresh.extend(chosen)
    for r in fresh:r['id']='packing-'+r['id'];r['family']='packing-'+r['family']
    assert len(fresh)==100 and len({r['text'] for r in fresh})==100 and not {r['text'] for r in fresh}&known
    write_json(DATA/'dev.json',fresh);write_json(DATA/'previous-dev.json',previous)
    shutil.copyfile(old.DATA/'compact-train-eval.json',DATA/'compact-train-eval.json')
    detail=base['pools']['compact'];short=Shard(Path(detail['pool']),'train')
    assert max(r['body_tokens']+1 for r in short.index)<=128
    c={k:copy.deepcopy(base[k]) for k in ('parent','web_shards','web_manifest_sha256','dev_shards','dev_manifest_sha256',
        'tokenizer','tokenizer_sha256','suite_sha256','evaluation','implementation','reference','peak_lr','train_goal','dev_goal')}
    c.update(scope='Plan68 authorized stages1–3 and stop',pool=detail,pools=dict(compact=detail),
        diagnostic_teacher_tokens=25000000,mixed_teacher_tokens=100000000,
        diagnostic_train_budget_seconds=300,mixed_train_budget_seconds=600,total_gpu_budget_seconds=2400,
        isolated_batch=256,dev_sha256=sha256(DATA/'dev.json'),previous_dev_sha256=sha256(DATA/'previous-dev.json'),
        train_eval_sha256=sha256(DATA/'compact-train-eval.json'),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        selection='Eligible non-fixed maximum fresh dev accuracy, then both-context accuracy, then shuffle',
        interpretation='Same train material and exact body/EOS teachers; fixed vs epoch document shuffle vs isolated attention with local positions. PAD and physical input separately accounted.',created_at=now())
    write_json(CONFIG,c);write_json(RUN/'ready.json',dict(pool=detail,dev_sha256=c['dev_sha256'],fresh_dev100_disjoint_previous=True,
        maximum_document_input_tokens=max(r['body_tokens']+1 for r in short.index),config_sha256=sha256(CONFIG)))
    print(json.dumps(dict(status='frozen',pool=detail,fresh_dev=100,teacher_tokens_per_arm=25000000)),flush=True)


def load_config():
    c=read_json(CONFIG)
    assert c['implementation']==implementation_hashes() and c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    for path,digest in [(DATA/'dev.json',c['dev_sha256']),(DATA/'previous-dev.json',c['previous_dev_sha256']),
        (DATA/'compact-train-eval.json',c['train_eval_sha256']),(Path(c['pool']['pool'])/'manifest.json',c['pool']['manifest_sha256']),
        (ROOT/c['tokenizer'],c['tokenizer_sha256']),(ROOT/'eval/base.jsonl',c['suite_sha256']),
        (Path(c['web_shards'])/'manifest.json',c['web_manifest_sha256']),(Path(c['dev_shards'])/'manifest.json',c['dev_manifest_sha256'])]:assert sha256(path)==digest
    return c


def resume_gate(parent,web,short,c,binding,check,heartbeat):
    path=RUN/'resume-gate.json'
    if path.exists():
        r=read_json(path);assert r['passed'] and r['binding']==binding;return r
    results={};verification=0;started=time.monotonic()
    for mode in ('fixed','shuffle','isolated'):
        torch.cuda.reset_peak_memory_stats()
        histories=[];states=[]
        for branch in ('continuous','resumed'):
            gate_binding=dict(binding,peak_lr=c['peak_lr'],isolated_batch=c['isolated_batch'],gate=mode)
            trainer=PackingTrainer(parent,web,short,mode,dict(web=0,short=200000),gate_binding)
            history=[]
            for i in range(4):
                check();history.append(trainer.step())
                if branch=='resumed' and i==1:
                    split=RUN/'resume-gate'/mode/'split.pt';trainer.save(split);del trainer;gc.collect();torch.cuda.empty_cache()
                    trainer=PackingTrainer(parent,web,short,mode,dict(web=0,short=200000),gate_binding);trainer.load(split)
            checkpoint=RUN/'resume-gate'/mode/(branch+'.pt');trainer.save(checkpoint)
            verification+=sum(trainer.sampler.source_teachers.values());histories.append(history)
            states.append(torch.load(checkpoint,map_location='cpu',weights_only=False));del trainer;gc.collect();torch.cuda.empty_cache()
        keys=('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','spec','model_config','pilot_binding','lineage','update')
        checks={k:pilot.equal_state(states[0][k],states[1][k]) for k in keys}
        for k in ('loss','gradient_norm','lr','tokens_seen','supervised_tokens','body_bytes_seen','token_digest','source_teachers'):
            checks['history_'+k]=[r[k] for r in histories[0]]==[r[k] for r in histories[1]]
        checks['finite_losses_gradients']=all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for h in histories for r in h)
        checks['teachers_input_padding_exact']=all(sum(s['sampler']['source_teachers'].values())==s['supervised_tokens']-parent['supervised_tokens'] and
            sum(s['sampler']['source_tokens'].values())==s['tokens']-parent['tokens'] for s in states)
        assert all(checks.values()),checks
        results[mode]=dict(checks=checks,histories=histories,peak_allocated_bytes=torch.cuda.max_memory_allocated(),passed=True)
        heartbeat('resume-gate-'+mode);del states
    result=dict(binding=binding,passed=True,arms=results,verification_teacher_tokens=verification,
        GPU_optimizer_updates=24,seconds=time.monotonic()-started,completed_at=now())
    write_json(path,result);return result


def train(parent,web,short,c,binding,arm,mode,goals,heartbeat,check):
    directory=RUN/arm;directory.mkdir(parents=True,exist_ok=True)
    binding=dict(binding,arm=arm,peak_lr=c['peak_lr'],isolated_batch=c['isolated_batch'],mode=mode,goals=goals)
    if (directory/'result.json').exists():
        r=read_json(directory/'result.json');assert r['binding']==binding and sha256(Path(r['checkpoint']))==r['checkpoint_sha256'];return r
    torch.cuda.reset_peak_memory_stats()
    trainer=PackingTrainer(parent,web,short,mode,goals,binding)
    logpath=directory/'metrics.jsonl'
    if (directory/'latest.json').exists():
        last=read_json(directory/'latest.json');assert sha256(Path(last['path']))==last['sha256'];trainer.load(last['path'])
        if logpath.exists():
            rows=[json.loads(line) for line in logpath.read_text().splitlines()]
            if rows and rows[-1]['update']>trainer.update:
                shutil.copyfile(logpath,directory/f'metrics-before-resume-{time.time_ns()}.jsonl')
                logpath.write_text(''.join(json.dumps(r)+'\n' for r in rows if r['update']<=trainer.update))
    prior=read_json(directory/'progress.json').get('training_seconds',0) if (directory/'progress.json').exists() else 0
    started=time.monotonic();budget=c['mixed_train_budget_seconds'] if arm.startswith('mixed') else c['diagnostic_train_budget_seconds']
    def save():
        path=directory/f'checkpoint-{trainer.update:08d}.pt';trainer.save(path);return path
    with logpath.open('a',buffering=1) as log:
        while sum(trainer.sampler.source_teachers.values())<sum(goals.values()):
            try:
                check()
                if prior+time.monotonic()-started>budget:raise TimeoutError(arm+' frozen train GPU budget exhausted')
                row=trainer.step()
            except BaseException:save();raise
            assert math.isfinite(row['loss']) and math.isfinite(row['gradient_norm'])
            log.write(json.dumps(row,allow_nan=False)+'\n');local=trainer.update-parent['update']
            if local==1 or local%100==0:
                seconds=prior+time.monotonic()-started
                heartbeat(arm+'-train',updates_completed=local,teachers=sum(trainer.sampler.source_teachers.values()),teacher_budget=sum(goals.values()),loss=row['loss'])
                write_json(directory/'progress.json',dict(training_seconds=seconds,updates_completed=local));print(json.dumps(dict(arm=arm,update=local,teachers=sum(trainer.sampler.source_teachers.values()),loss=row['loss'])),flush=True)
            if local%250==0:save()
    path=save()
    result=dict(status='complete',binding=binding,checkpoint=str(path),checkpoint_sha256=sha256(path),mode=mode,
        update=trainer.update,tokens=trainer.tokens,additional_input_tokens=trainer.tokens-parent['tokens'],
        additional_supervised_tokens=trainer.supervised_tokens-parent['supervised_tokens'],
        physical_input_tokens=sum(trainer.sampler.source_physical_tokens.values()),source_teachers=trainer.sampler.source_teachers.copy(),
        source_tokens=trainer.sampler.source_tokens.copy(),source_eos_teachers=trainer.sampler.source_eos.copy(),sampler=trainer.sampler.state_dict(),
        body_bytes=trainer.body_bytes-parent['body_bytes'],training_seconds=prior+time.monotonic()-started,
        completed_at=now(),peak_allocated_bytes=torch.cuda.max_memory_allocated())
    assert result['source_teachers']==goals
    write_json(directory/'result.json',result);del trainer;gc.collect();torch.cuda.empty_cache();return result


def run():
    c=load_config();path=RUN/'job.json';previous=read_json(path) if path.exists() else {}
    binding=dict(plan_sha256=sha256(CONFIG),parent=c['parent'],peak_lr=c['peak_lr'],implementation=c['implementation'])
    if previous:
        assert previous['binding']==binding and not alive(previous),'Actual live or differently bound job'
        if previous['status']=='complete':print('Completed stage retained');return
    prior=previous.get('gpu_elapsed_seconds',0);started=None;stopped=[False]
    job=dict(status='starting',**identity(),binding=binding,gpu_elapsed_seconds=prior,started_at=previous.get('started_at',now()),
        restart_command='scripts/run_packing_study.ps1')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; completed update checkpoint retained')
        if started is not None and prior+time.monotonic()-started>c['total_gpu_budget_seconds']:raise TimeoutError('Frozen cumulative GPU budget exhausted')
    def heartbeat(stage,**extra):
        check();job.update(stage=stage,heartbeat_at=now(),**extra)
        if started is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started
        atomic_json(path,job)
    try:
        heartbeat('setup')
        for p in (*SOURCES,str(CONFIG.relative_to(ROOT))):
            target=RUN/'source'/p;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/p).read_bytes()
            else:shutil.copyfile(ROOT/p,target)
        seed_all(42);torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            started=time.monotonic();assert sha256(Path(c['parent']['path']))==c['parent']['sha256']
            parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);assert finite_state(parent)
            web=TrainView(c['web_shards'],c['web_manifest_sha256']);short=Shard(Path(c['pool']['pool']),'train')
            gate=resume_gate(parent,web,short,c,binding,check,heartbeat)
            old.RUN=RUN;old.DATA=DATA;conditions={};trained={};evaluations={}
            for mode in ('fixed','shuffle','isolated'):
                trained[mode]=train(parent,web,short,c,binding,mode,mode,dict(web=0,short=25000000),heartbeat,check)
                conditions[mode]=old.evaluate_condition(trained[mode],c,mode,heartbeat,check)
                write_json(RUN/'diagnostic-progress.json',dict(checkpoints=trained,conditions=conditions))
                print(json.dumps(dict(mode=mode,train=conditions[mode]['results']['train']['summary'],dev=conditions[mode]['results']['dev']['summary'])),flush=True)
            eligible=[a for a in ('shuffle','isolated') if conditions[a]['diagnostic_pass']]
            selected=max(eligible,key=lambda a:(conditions[a]['results']['dev']['summary']['accuracy'],conditions[a]['results']['dev']['summary']['both_accuracy'],a=='shuffle')) if eligible else None
            write_json(RUN/'selection.json',dict(selected=selected,eligible=eligible,rule=c['selection'],completed_at=now()))
            if selected:
                for arm,mode in [('mixed-fixed','fixed'),('mixed-candidate',selected)]:
                    trained[arm]=train(parent,web,short,c,binding,arm,mode,dict(web=80000000,short=20000000),heartbeat,check)
                    conditions[arm]=old.evaluate_condition(trained[arm],c,arm,heartbeat,check)
            dev=Shard(Path(c['dev_shards']),'dev');tok=Tokenizer(ROOT/c['tokenizer']);comparison.RUN=RUN/'evaluation'
            for arm,d in trained.items():
                heartbeat(arm+'-Japanese')
                evaluations[arm]=comparison.evaluate(arm,d,dev,tok,c,d['binding'],heartbeat,check,started+c['total_gpu_budget_seconds']-prior)
            result=dict(status='complete_pending_content_review',binding=binding,checkpoints=trained,conditions=conditions,evaluations=evaluations,
                selected=selected,mixed100m_executed=selected is not None,scientific_teacher_tokens=sum(d['additional_supervised_tokens'] for d in trained.values()),
                scientific_valid_input_tokens=sum(d['additional_input_tokens'] for d in trained.values()),
                physical_input_tokens=sum(d['physical_input_tokens'] for d in trained.values()),verification_teacher_tokens=gate['verification_teacher_tokens'],
                resume_gate=gate,protected_test_used=False,GPU_seconds=prior+time.monotonic()-started,completed_at=now())
            write_json(RUN/'result.json',result);heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps(dict(status=result['status'],selected=selected,scientific_teacher_tokens=result['scientific_teacher_tokens'],GPU_seconds=result['GPU_seconds'])),flush=True)
    except BaseException as error:job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        if started is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started
        atomic_json(path,job)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--mode',choices=('prepare','probe','run'),default='probe');args=p.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='prepare':prepare()
    elif args.mode=='probe':
        load_config()
        if (RUN/'job.json').exists():assert not alive(read_json(RUN/'job.json'))
        print('Frozen packing study valid; no actual duplicate job')
    else:run()
