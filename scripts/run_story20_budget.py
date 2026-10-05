"""Conditional paired500M common-schedule study with actual100M intermediates."""
import argparse
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
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jsonschema import validate
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,seed_all,implementation_hashes
from jmicro.eos_pilot import TrainView
from jmicro.low_lr_pilot import LowLRPilotTrainer
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity,alive,finite_state
import run_story20_low_lr as screen
import run_complete_text_comparison as comparison
import run_eos_short_pilot as pilot
from prepare_story20_budget import POOL

RUN=ROOT/'reports/phase6/story20-low-lr-10b-500m-20261005'
CONFIG=ROOT/'configs/phase6/story20_low_lr_10b_500m.json'
SCHEMA=ROOT/'schemas/configs/phase6/story20_low_lr_10b_500m.schema.json'
SOURCES=tuple(dict.fromkeys(('scripts/run_story20_budget.py','scripts/run_story20_budget.ps1','scripts/prepare_story20_budget.py','scripts/prepare_story20_budget.ps1','scripts/review_story20_budget.py',*screen.SOURCES)))


def budget_plan(base,pool,manifest):
    plan=dict(base)
    plan.update(scope='Plan52 conditional paired500M; common fixed pool/schedule100M intermediate and500M final; judgment and stop',
                output=str(RUN.relative_to(ROOT)),pool=dict(pool=pool,manifest_sha256=manifest),
                arms={'web':dict(pool=pool,manifest_sha256=manifest,short_updates=0),
                      'coherent20':dict(pool=pool,manifest_sha256=manifest,short_updates=3051)},
                updates_per_arm=15259,stable_updates=14500,decay_updates=759,tokens_per_arm=500006912,
                scientific_total_tokens=1000013824,final_update=320435,final_tokens=10500014080,
                intermediate_update=308228,intermediate_tokens=10100015104,intermediate_additional_tokens=100007936,
                screen_gpu_budget_seconds=4200,full_gpu_budget_seconds=3000,total_GPU_budget_seconds=7200)
    return plan


def freeze():
    assert not (RUN/'screen-job.json').exists(),'Started config immutable'
    base=screen.load_config();full=read_json(screen.RUN/'full/review.json')
    assert full['status']=='passed' and all(full['checks'].values()) and full['candidate_passes_all_full_conditions']
    ready=read_json(POOL/'ready.json');content=read_json(POOL/'content-review.json')
    assert content['accepted_for_experiment'] and content['pool_manifest_sha256']==sha256(POOL/'manifest.json')==ready['manifest_sha256']
    assert content['samples_sha256']==sha256(POOL/'samples.json')
    assert ready['source_train_only'] and ready['parent_split_disjoint']
    plan=budget_plan(base,str(POOL),ready['manifest_sha256'])
    plan.update(entry_full_review=dict(path=str(screen.RUN/'full/review.json'),sha256=sha256(screen.RUN/'full/review.json')),
                pool_ready=dict(path=str(POOL/'ready.json'),sha256=sha256(POOL/'ready.json')),
                pool_content=dict(path=str(POOL/'content-review.json'),sha256=sha256(POOL/'content-review.json')),
                tests_sha256=sha256(RUN/'tests.xml'),source_sha256={p:sha256(ROOT/p) for p in SOURCES},created_at=now())
    suites=list(ET.parse(RUN/'tests.xml').getroot().iter('testsuite'))
    assert sum(int(s.attrib['tests']) for s in suites)>=4 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped'))
    write_json(CONFIG,plan);write_json(SCHEMA,dict(type='object',additionalProperties=False,required=list(plan),properties={k:{'const':v} for k,v in plan.items()}))
    print('Frozen common500M schedule; intermediate100M is not a terminal-decayed branch; pool repetition explicitly recorded',flush=True)


def load_config():
    config=read_json(CONFIG);validate(config,read_json(SCHEMA))
    assert config['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES} and config['implementation']==implementation_hashes()
    for ref in (*config['reference'].values(),config['entry_full_review'],config['pool_ready'],config['pool_content']):
        assert sha256(Path(ref['path']))==ref['sha256']
    assert sha256(RUN/'tests.xml')==config['tests_sha256']
    for path,digest in [(Path(config['pool']['pool'])/'manifest.json',config['pool']['manifest_sha256']),
                        (ROOT/config['tokenizer'],config['tokenizer_sha256']),
                        (ROOT/'eval/base.jsonl',config['suite_sha256']),
                        (Path(config['dev_shards'])/'manifest.json',config['dev_manifest_sha256']),
                        (ROOT/config['evaluation']['config'],config['evaluation']['config_sha256']),
                        (ROOT/config['evaluation']['semantic_suite'],config['evaluation']['semantic_sha256'])]:assert sha256(path)==digest
    return config


def train_arm(arm,parent,web,pool,config,binding,heartbeat,check):
    directory=RUN/arm;directory.mkdir(parents=True,exist_ok=True);terminal=directory/'result.json'
    if terminal.exists():
        saved=read_json(terminal);assert saved['binding']==binding and sha256(Path(saved['checkpoint']))==saved['checkpoint_sha256'];return saved
    routing=pilot.routes(config['updates_per_arm'],config['arms'][arm]['short_updates'])
    schedule=dict(parent_update=parent['update'],stable_updates=config['stable_updates'],decay_updates=config['decay_updates'])
    trainer=LowLRPilotTrainer(parent,web,pool,routing,schedule,binding)
    log_path=directory/'metrics.jsonl'
    if (directory/'latest.json').exists():
        last=read_json(directory/'latest.json');assert sha256(Path(last['path']))==last['sha256'];trainer.load(last['path'])
        if log_path.exists():
            rows=[json.loads(line) for line in log_path.read_text().splitlines()]
            if rows and rows[-1]['update']>trainer.update:
                shutil.copyfile(log_path,directory/f'metrics-before-resume-{time.time_ns()}.jsonl')
                log_path.write_text(''.join(json.dumps(row)+'\n' for row in rows if row['update']<=trainer.update))
    previous=read_json(directory/'progress.json').get('training_seconds',0) if (directory/'progress.json').exists() else 0
    started=time.monotonic()
    def record_checkpoint(label):
        path=directory/f'checkpoint-{trainer.update:08d}.pt';trainer.save(path)
        local=trainer.update-parent['update'];expected=sum(routing[:local])*32768
        assert trainer.sampler.source_tokens==dict(web=local*32768-expected,short=expected)
        result=dict(status='complete',binding=binding,checkpoint=str(path),checkpoint_sha256=sha256(path),update=trainer.update,tokens=trainer.tokens,
                    additional_input_tokens=trainer.tokens-parent['tokens'],source_tokens=trainer.sampler.source_tokens.copy(),
                    source_eos_teachers=trainer.sampler.source_eos.copy(),sampler=trainer.sampler.state_dict(),
                    training_seconds=previous+time.monotonic()-started,learning_rate_fork=trainer.lineage['learning_rate_fork'],
                    checkpoint_role=label,pool_ready=config['pool_ready'])
        write_json(directory/(label+'.json'),result)
        return result
    with log_path.open('a',buffering=1) as log:
        while trainer.update<config['final_update']:
            try:check()
            except (InterruptedError,TimeoutError):trainer.save(directory/f'checkpoint-{trainer.update:08d}.pt');raise
            row=trainer.step();assert math.isfinite(row['loss']) and math.isfinite(row['gradient_norm'])
            log.write(json.dumps(dict(row,arm=arm),allow_nan=False)+'\n')
            local=trainer.update-parent['update']
            if local==1 or local%100==0:
                heartbeat(arm+'-train',updates_completed=local,loss=row['loss'],tokens_per_second=row['tokens_per_second'])
                write_json(directory/'progress.json',dict(training_seconds=previous+time.monotonic()-started,updates_completed=local))
                print(json.dumps(dict(row,arm=arm)),flush=True)
            if trainer.update==config['intermediate_update']:record_checkpoint('intermediate100M')
            elif local%500==0:trainer.save(directory/f'checkpoint-{trainer.update:08d}.pt')
    result=record_checkpoint('result');assert result['tokens']==config['final_tokens'] and result['additional_input_tokens']==config['tokens_per_arm']
    assert (directory/'intermediate100M.json').exists()
    del trainer;gc.collect();torch.cuda.empty_cache()
    return result


def run_gpu():
    config=load_config();RUN.mkdir(parents=True,exist_ok=True)
    binding=dict(plan_sha256=sha256(CONFIG),parent=config['parent'],peak_lr=config['peak_lr'],implementation=config['implementation'],source_sha256=config['source_sha256'])
    path=RUN/'screen-job.json';old=read_json(path) if path.exists() else {}
    if old:
        assert old['binding']==binding and not alive(old),'Existing live or different job'
        if old['status']=='complete':print('Reuse completed500M job');return
    prior=old.get('gpu_elapsed_seconds',0);started=[None];stopped=[False];budget=config['screen_gpu_budget_seconds']
    job=dict(status='starting',**identity(),binding=binding,started_at=old.get('started_at',now()),gpu_elapsed_seconds=prior,
             restart_command='scripts/run_story20_budget.ps1 -Mode screen')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; checkpoints retained')
        if started[0] is not None and prior+time.monotonic()-started[0]>budget:raise TimeoutError('Cumulative500M scientific/evaluation budget exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)
    try:
        heartbeat('setup')
        for relative in (*SOURCES,str(CONFIG.relative_to(ROOT))):
            target=RUN/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        assert sha256(Path(config['parent']['path']))==config['parent']['sha256']
        parent=torch.load(config['parent']['path'],map_location='cpu',weights_only=False);assert finite_state(parent)
        web=TrainView(config['web_shards'],config['web_manifest_sha256']);pool=TrainView(config['pool']['pool'],config['pool']['manifest_sha256'],check_stream=True)
        dev=Shard(Path(config['dev_shards']),'dev');tok=Tokenizer(ROOT/config['tokenizer']);seed_all(42);torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            started[0]=time.monotonic();deadline=started[0]+budget-prior;pilot.PilotTrainer=LowLRPilotTrainer
            gate=pilot.exact_gate(parent,web,pool,{**binding,'arm':'gate'},RUN,check)
            trained={};evaluated={}
            for arm in config['arms']:
                trained[arm]=train_arm(arm,parent,web,pool,config,comparison.arm_binding(binding,config,arm),heartbeat,check)
            # All intermediate evaluations happen after learning; they cannot alter subsequent training RNG.
            for arm in config['arms']:
                evaluated[arm]={}
                for label in ('intermediate100M','result'):
                    detail=read_json(RUN/arm/(label+'.json'));comparison.RUN=RUN/'evaluation'/label
                    evaluated[arm][label]=comparison.evaluate(arm,detail,dev,tok,config,detail['binding'],heartbeat,check,deadline)
            result=dict(status='complete_pending_content_review',binding=binding,arms=trained,
                        rates={a:{k:v['greedy_rates'] for k,v in stages.items()} for a,stages in evaluated.items()},
                        BPB={a:{k:v['body']['bpb'] for k,v in stages.items()} for a,stages in evaluated.items()},
                        diagnostics={a:{k:v['diagnostics'] for k,v in stages.items()} for a,stages in evaluated.items()},
                        scientific_tokens=sum(d['additional_input_tokens'] for d in trained.values()),verification_tokens=gate['input_tokens'],resume_gate=gate,
                        pool_ready=config['pool_ready'],protected_test_used=False,GPU_seconds=prior+time.monotonic()-started[0],completed_at=now())
            assert result['scientific_tokens']==1000013824
            write_json(RUN/'result.json',result);heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps({k:v for k,v in result.items() if k in ('status','rates','BPB','GPU_seconds')}),flush=True)
    except BaseException as error:job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('freeze','screen','probe'),default='screen');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='freeze':freeze()
    elif args.mode=='probe':
        load_config()
        if (RUN/'screen-job.json').exists():assert not alive(read_json(RUN/'screen-job.json'))
        print('Conditional500M config valid; no live comparison job')
    else:run_gpu()


if __name__=='__main__':main()
