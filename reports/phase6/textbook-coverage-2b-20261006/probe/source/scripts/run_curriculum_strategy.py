"""Roadmap stage3: equal100M teachers, continuation vs fresh10M pretraining."""
import argparse
import copy
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
sys.path.insert(0,str(Path(__file__).resolve().parent))
import torch
from jmicro.curriculum_strategy import StrategyTrainer
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import Trainer,atomic_json,gpu_lock,implementation_hashes,seed_all
from phase6_performance import identity,alive,finite_state
import run_packing_study as packing
import run_eos_short_pilot as pilot
import run_complete_text_comparison as comparison
from run_root_cause_diagnostic import teacher,generate
from run_generation_transfer import make_case,summary

RUN=ROOT/'reports/phase6/curriculum-strategy-20261005-v3'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/curriculum-strategy-20261005-v3')
CONFIG=ROOT/'configs/phase6/curriculum_strategy.json'
SOURCES=('scripts/run_curriculum_strategy.py','scripts/run_curriculum_strategy.ps1',
    'scripts/prepare_curriculum_strategy.py','src/jmicro/curriculum_strategy.py',
    'scripts/run_packing_study.py','src/jmicro/natural_learning.py','src/jmicro/packing_study.py',
    'scripts/run_complete_text_comparison.py','scripts/run_generation_transfer.py',
    'scripts/run_root_cause_diagnostic.py')


def freeze():
    if CONFIG.exists():load_config();print('Frozen comparison retained');return
    base=read_json(ROOT/'configs/phase6/narrative_comparison.json')
    ready=read_json(DATA/'ready.json');review=read_json(RUN/'content-review.json')
    assert review['sample_sha256']==ready['sample_sha256'] and review['documents']==64
    assert review['weak_documents']<=10 and len(review['reviews'])==64
    assert ready['splits']['train']['tokens']>=10000000
    c={k:copy.deepcopy(base[k]) for k in ('parent','web_shards','web_manifest_sha256',
        'dev_shards','dev_manifest_sha256','tokenizer','tokenizer_sha256','suite_sha256','evaluation','reference')}
    c.update(curriculum=dict(pool=ready['pool'],manifest_sha256=ready['manifest_sha256']),
        preparation_sha256=sha256(DATA/'ready.json'),content_review_sha256=sha256(RUN/'content-review.json'),
        dev32_sha256=sha256(DATA/'dev32.json'),goals=dict(web=0,short=100000000),
        strategies=dict(continuation=dict(peak_lr=.0001,warmup_updates=0,optimizer_policy='inherit',initialization='original10B'),
            fresh=dict(peak_lr=.002,warmup_updates=200,optimizer_policy='fresh',initialization='new-random')),
        diagnostic_train_budget_seconds=600,mixed_train_budget_seconds=600,isolated_batch=256,
        gpu_budget_seconds=1800,implementation=implementation_hashes(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        contract_sha256=sha256(ROOT/'docs/80_generation_transfer_plan.md'),created_at=now(),protected_test_used=False,
        interpretation='Learning strategy comparison, not isolated capacity/LR/amount experiment; curriculum input mix approximately1M short/4M narrative/5M Web; exact total body/EOS teachers100M each')
    write_json(CONFIG,c);print(json.dumps(dict(status='frozen',curriculum=c['curriculum'],goals=c['goals'])),flush=True)


def load_config():
    c=read_json(CONFIG)
    assert c['implementation']==implementation_hashes()
    assert c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    for path,digest in [(DATA/'ready.json',c['preparation_sha256']),(DATA/'dev32.json',c['dev32_sha256']),
        (RUN/'content-review.json',c['content_review_sha256']),(Path(c['curriculum']['pool'])/'manifest.json',c['curriculum']['manifest_sha256']),
        (ROOT/'docs/80_generation_transfer_plan.md',c['contract_sha256'])]:assert sha256(path)==digest
    return c


def fresh_parent(parent,web):
    path=RUN/'initial-fresh.pt'
    if not path.exists():
        spec=dict(parent['spec']);spec.update(scheduler='wsd',schedule_updates=100000,lr=.002,warmup=200)
        for k in ('branch_at','decay_updates','minimum_lr_ratio','pilot_schedule','teacher_schedule'):spec.pop(k,None)
        trainer=Trainer(parent['model_config'],web,spec,'cuda');trainer.save(path)
        assert trainer.update==trainer.tokens==trainer.supervised_tokens==0
        del trainer;gc.collect();torch.cuda.empty_cache()
    state=torch.load(path,map_location='cpu',weights_only=False)
    assert state['update']==state['tokens']==state['supervised_tokens']==0
    assert not state['optimizer']['state'] and state['model_config']==parent['model_config'] and finite_state(state)
    return state


def resume_gate(parent,web,short,binding,check,heartbeat):
    path=RUN/'resume-gate'/binding['arm']/'result.json'
    if path.exists():
        r=read_json(path);assert r['binding']==binding and r['passed'];return r
    states=[];histories=[];verification=0
    for branch in ('continuous','resumed'):
        trainer=StrategyTrainer(parent,web,short,'shuffle',dict(web=0,short=200000),binding)
        history=[]
        for i in range(4):
            check();history.append(trainer.step())
            if branch=='resumed' and i==1:
                split=path.parent/'split.pt';trainer.save(split);del trainer;gc.collect();torch.cuda.empty_cache()
                trainer=StrategyTrainer(parent,web,short,'shuffle',dict(web=0,short=200000),binding);trainer.load(split)
        endpoint=path.parent/(branch+'.pt');trainer.save(endpoint)
        verification+=sum(trainer.sampler.source_teachers.values());histories.append(history)
        states.append(torch.load(endpoint,map_location='cpu',weights_only=False));del trainer;gc.collect();torch.cuda.empty_cache()
    checks={k:pilot.equal_state(states[0][k],states[1][k]) for k in ('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','spec','model_config','pilot_binding','lineage','update')}
    for k in ('loss','gradient_norm','lr','source_teachers'):checks['history_'+k]=[r[k] for r in histories[0]]==[r[k] for r in histories[1]]
    checks['finite']=all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for h in histories for r in h)
    assert all(checks.values()),checks
    result=dict(passed=True,binding=binding,checks=checks,histories=histories,verification_teacher_tokens=verification)
    write_json(path,result);heartbeat(binding['arm']+'-resume-verified');return result


def auxiliary(detail,c,arm,heartbeat,check):
    path=RUN/arm/'auxiliary-dev32.json'
    if path.exists():
        r=read_json(path);assert r['checkpoint_sha256']==detail['checkpoint_sha256'];return r
    state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
    model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model']);del state
    tok=Tokenizer(ROOT/c['tokenizer']);cases=[make_case(r,tok,'dev') for r in read_json(DATA/'dev32.json')]
    rows=[];gold=[]
    for offset in range(0,32,16):
        check();heartbeat(arm+'-auxiliary32');gold.extend(teacher(model,cases[offset:offset+16]))
        rows.extend(generate(model,cases[offset:offset+16],tok,None,64))
    result=dict(checkpoint_sha256=detail['checkpoint_sha256'],cases_sha256=c['dev32_sha256'],teacher=gold,generation=rows,
        summary=dict(documents=32,EOS=sum(r['stop_reason']=='eos' for r in rows),
            repeated4gram=sum(r['first_repeated_4gram'] is not None for r in rows),
            teacher_NLL=sum(r['teacher_nll_mean'] for r in gold)/32,
            teacher_top1_fraction=sum(r['teacher_top1_fraction'] for r in gold)/32),
        source_history='Some auxiliary Web docs were seen in original10B train; this is not wholly unseen-parent generalization')
    write_json(path,result);del model;gc.collect();torch.cuda.empty_cache();return result


def run():
    c=load_config();path=RUN/'job.json';previous=read_json(path) if path.exists() else {}
    binding=dict(config_sha256=sha256(CONFIG),parent=c['parent'],implementation=c['implementation'])
    if previous:
        assert previous['binding']==binding and not alive(previous)
        if previous['status']=='complete':print('Completed comparison retained');return
    prior=previous.get('gpu_elapsed_seconds',0);start=[None];stopped=[False]
    job=dict(status='starting',**identity(),binding=binding,started_at=now(),gpu_elapsed_seconds=prior,
        restart_command='scripts/run_curriculum_strategy.ps1 -Worker')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; completed update preserved')
        if start[0] is not None and prior+time.monotonic()-start[0]>c['gpu_budget_seconds']:raise TimeoutError('1800s cumulative GPU budget exhausted')
    def heartbeat(stage,**extra):
        check();job.update(stage=stage,heartbeat_at=now(),**extra)
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(path,job)
    try:
        heartbeat('setup');torch.set_num_threads(2);seed_all(42);torch.use_deterministic_algorithms(True)
        web=TrainView(c['web_shards'],c['web_manifest_sha256']);short=Shard(Path(c['curriculum']['pool']),'train')
        dev=Shard(Path(c['dev_shards']),'dev');tok=Tokenizer(ROOT/c['tokenizer'])
        assert sha256(Path(c['parent']['path']))==c['parent']['sha256']
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);assert finite_state(parent)
        packing.RUN=RUN;packing.PackingTrainer=StrategyTrainer;comparison.RUN=RUN/'evaluation'
        with gpu_lock('cuda'):
            start[0]=time.monotonic();fresh=fresh_parent(parent,web);checkpoints={};evaluations={};extra={};gates={}
            for arm,p in [('continuation',parent),('fresh',fresh)]:
                strategy=c['strategies'][arm]
                actual_parent=c['parent'] if arm=='continuation' else dict(path=str(RUN/'initial-fresh.pt'),
                    sha256=sha256(RUN/'initial-fresh.pt'),update=0,tokens_seen=0)
                b=dict(binding,**strategy,arm=arm,isolated_batch=256,parent=actual_parent,
                    actual_parent_path=actual_parent['path'])
                arm_config=dict(c,peak_lr=strategy['peak_lr'])
                gates[arm]=resume_gate(p,web,short,b,check,heartbeat)
                checkpoints[arm]=packing.train(p,web,short,arm_config,b,arm,'shuffle',c['goals'],heartbeat,check)
                evaluations[arm]=comparison.evaluate(arm,checkpoints[arm],dev,tok,c,checkpoints[arm]['binding'],heartbeat,check,start[0]+c['gpu_budget_seconds']-prior)
                extra[arm]=auxiliary(checkpoints[arm],c,arm,heartbeat,check)
                write_json(RUN/'progress-result.json',dict(checkpoints=checkpoints,evaluations=evaluations,auxiliary=extra))
            result=dict(status='complete_pending_content_review',binding=binding,checkpoints=checkpoints,
                evaluations=evaluations,auxiliary=extra,scientific_teacher_tokens=sum(r['additional_supervised_tokens'] for r in checkpoints.values()),
                valid_input_tokens=sum(r['additional_input_tokens'] for r in checkpoints.values()),
                physical_input_tokens=sum(r['physical_input_tokens'] for r in checkpoints.values()),
                verification_teacher_tokens=sum(r['verification_teacher_tokens'] for r in gates.values()),
                gpu_seconds=prior+time.monotonic()-start[0],protected_test_used=False,completed_at=now())
            write_json(RUN/'compare-result.json',result);heartbeat('complete');job.update(status='complete',completed_at=now())
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument('--freeze',action='store_true');a=p.parse_args()
    freeze() if a.freeze else run()
