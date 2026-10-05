"""Independent frozen eligible full/long500M evaluation; original gates unchanged."""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jsonschema import validate
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,seed_all,rng_state
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.model import JMicroModel
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.japanese_evaluation import NativeLikelihood
from phase6_performance import identity,alive
from run_eos_5b_finish import evaluate as evaluate_full
from run_eos_short_pilot import equal_state
from run_eos_complete_100m import adoption_checks
from compare_base_10b import require_alignment,growth_checks
from compare_base_5b import summarize
from evaluate_japanese_base import evaluate_long
import run_story20_budget as study

CONFIG=ROOT/'configs/phase6/story20_low_lr_500m_full.json'
SCHEMA=ROOT/'schemas/configs/phase6/story20_low_lr_500m_full.schema.json'
SOURCES=('scripts/evaluate_story20_budget_full.py','scripts/evaluate_story20_budget_full.ps1','scripts/review_story20_execution.py')


def freeze():
    config=study.load_config();review=read_json(study.RUN/'review.json');job=read_json(study.RUN/'screen-job.json')
    assert review['status']=='passed' and all(review['checks'].values()) and review['eligible_for_full']
    assert job['status']=='complete' and not alive(job)
    assert not (study.RUN/'full/full-job.json').exists()
    plan=dict(scientific_config_sha256=sha256(study.CONFIG),review_sha256=sha256(study.RUN/'review.json'),
              result_sha256=sha256(study.RUN/'result.json'),GPU_budget_seconds=config['full_gpu_budget_seconds'],
              sources={p:sha256(ROOT/p) for p in SOURCES},additional_training_tokens=0,protected_test_used=False,created_at=now())
    write_json(CONFIG,plan);write_json(SCHEMA,dict(type='object',additionalProperties=False,required=list(plan),properties={k:{'const':v} for k,v in plan.items()}))
    print('Frozen eligible500M full/long; zero additional learning',flush=True)


def load_config():
    config=study.load_config();plan=read_json(CONFIG);validate(plan,read_json(SCHEMA))
    assert plan['scientific_config_sha256']==sha256(study.CONFIG) and plan['review_sha256']==sha256(study.RUN/'review.json')
    assert plan['result_sha256']==sha256(study.RUN/'result.json') and plan['sources']=={p:sha256(ROOT/p) for p in SOURCES}
    return config,plan


def execute():
    config,plan=load_config();output=study.RUN/'full';output.mkdir(parents=True,exist_ok=True)
    binding=dict(plan_sha256=sha256(study.CONFIG),full_plan_sha256=sha256(CONFIG),review_sha256=plan['review_sha256'],
                 parent=config['parent'],source_sha256=plan['sources'])
    path=output/'full-job.json';old=read_json(path) if path.exists() else {}
    if old:
        assert old['binding']==binding and not alive(old)
        if old['status']=='complete':print('Reuse completed full500M job');return
    prior=old.get('gpu_elapsed_seconds',0);started=[None];stopped=[False];budget=plan['GPU_budget_seconds']
    job=dict(status='starting',**identity(),binding=binding,started_at=old.get('started_at',now()),gpu_elapsed_seconds=prior,
             restart_command='scripts/evaluate_story20_budget_full.ps1')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; partial evaluation retained')
        if started[0] is not None and prior+time.monotonic()-started[0]>budget:raise TimeoutError('Cumulative500M full budget exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)
    try:
        heartbeat('setup')
        for relative in (*SOURCES,str(CONFIG.relative_to(ROOT))):
            target=output/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        dev=Shard(Path(config['dev_shards']),'dev');tok=Tokenizer(ROOT/config['tokenizer']);seed_all(42);torch.use_deterministic_algorithms(True)
        trained=read_json(study.RUN/'result.json')['arms'];full={};long={}
        parent_body=read_json(Path(config['reference']['parent_body']['path']))['body']
        parent_generation=read_json(Path(config['reference']['parent_generation']['path']))['generation']
        with gpu_lock('cuda'):
            started[0]=time.monotonic();deadline=started[0]+budget-prior
            for arm,detail in trained.items():
                branch={**binding,'arm':arm,'checkpoint_sha256':detail['checkpoint_sha256']}
                full[arm]=evaluate_full(Path(detail['checkpoint']),dev,tok,None,output/(arm+'-full.json'),branch,heartbeat,check,full=True)
                require_alignment(full[arm]['body'],full[arm]['generation'],parent_body,parent_generation)
                state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
                model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True);bound_evaluation_cache(model)
                before=rng_state();hook=model.register_forward_pre_hook(lambda *_:check())
                with sdpa_kernel(SDPBackend.MATH):
                    long[arm]=evaluate_long(NativeLikelihood(model,tok,batch=16),read_json(ROOT/config['evaluation']['config']),output/arm,json.dumps(branch,sort_keys=True),deadline)
                hook.remove();assert long[arm]['complete'] and equal_state(before,rng_state());check()
                del state,model;gc.collect();torch.cuda.empty_cache()
            summaries={a:summarize(a,d['tokens'],full[a]['body'],full[a]['generation']) for a,d in trained.items()}
            parent=summarize('parent10B',10000007168,parent_body,parent_generation)
            checks=dict(mixture=adoption_checks(full['web'],full['coherent20']),parent_growth=growth_checks(summaries['coherent20'],parent))
            result=dict(status='complete',binding=binding,summary=summaries,parent=parent,long_generation=long,checks=checks,
                        candidate_passes_all_full_conditions=all(checks['mixture'].values()) and all(checks['parent_growth'].values()),
                        additional_training_tokens=0,protected_test_used=False,quality_targets_achieved=False,independent_human_blind='not performed',
                        GPU_seconds=prior+time.monotonic()-started[0],completed_at=now())
            write_json(output/'result.json',result);heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps({k:v for k,v in result.items() if k!='long_generation'},ensure_ascii=False),flush=True)
    except BaseException as error:job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('freeze','run','probe','review'),default='run');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='freeze':freeze()
    elif args.mode=='review':
        load_config();from review_story20_execution import full_review;full_review(study)
    elif args.mode=='probe':
        load_config()
        if (study.RUN/'full/full-job.json').exists():assert not alive(read_json(study.RUN/'full/full-job.json'))
        print('Frozen500M full config valid; no live full job')
    else:execute()
