"""One fixed500M data-composition candidate; immutable saved controls, no sweep."""
import argparse
import copy
import gc
import json
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
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,seed_all,implementation_hashes,rng_state
from jmicro.eos_pilot import TrainView
from jmicro.low_lr_pilot import LowLRPilotTrainer
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.model import JMicroModel
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.japanese_evaluation import NativeLikelihood
from phase6_performance import identity,alive,finite_state
from prepare_complete_document_pool import POOL
from run_eos_5b_finish import evaluate as evaluate_full
from run_eos_complete_100m import adoption_checks
from compare_base_10b import require_alignment,growth_checks
from compare_base_5b import summarize
from evaluate_japanese_base import evaluate_long
import run_story20_budget as old
import run_complete_text_comparison as comparison
import run_eos_short_pilot as pilot

RUN=ROOT/'reports/phase6/complete-document-500m-20261005'
CONFIG=ROOT/'configs/phase6/complete_document_500m.json'
SCHEMA=ROOT/'schemas/configs/phase6/complete_document_500m.schema.json'
OWN_SOURCES=('scripts/run_complete_document_500m.py','scripts/run_complete_document_500m.ps1',
             'scripts/review_complete_document_500m.py','scripts/prepare_complete_document_pool.py','src/jmicro/whole_short_text.py')
SOURCES=tuple(dict.fromkeys((*OWN_SOURCES,*old.SOURCES)))


def candidate_plan(base,pool,digest):
    plan=copy.deepcopy(base)
    plan.update(scope='Authorized plan54 stages1–4 fixed500M whole-document data comparison and stop',output=str(RUN.relative_to(ROOT)),
                pool=dict(pool=pool,manifest_sha256=digest),arms={'whole20':dict(pool=pool,manifest_sha256=digest,short_updates=3051)},
                scientific_total_tokens=500006912,screen_gpu_budget_seconds=1800,full_gpu_budget_seconds=1800,total_GPU_budget_seconds=3600)
    return plan


def freeze():
    assert not (RUN/'screen-job.json').exists(),'Started config immutable'
    base=old.load_config(); prior=read_json(old.RUN/'review.json'); full=read_json(old.RUN/'full/review.json')
    assert all(prior['checks'].values()) and full['candidate_passes_all_full_conditions']
    ready=read_json(POOL/'ready.json');content=read_json(POOL/'content-review.json')
    assert ready['source_train_only'] and ready['whole_original_documents'] and 100000000<=ready['totals']['tokens']<=120000000
    assert content['accepted_for_experiment'] and content['pool_manifest_sha256']==sha256(POOL/'manifest.json')==ready['manifest_sha256']
    assert content['samples_sha256']==sha256(POOL/'samples.json') and len(content['notes'])==40
    suites=list(ET.parse(RUN/'tests.xml').getroot().iter('testsuite'))
    assert sum(int(s.attrib['tests']) for s in suites)>=8 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped'))
    plan=candidate_plan(base,str(POOL),ready['manifest_sha256'])
    reference={k:base['reference'][k] for k in ('parent_body','parent_generation')}
    for key,path in {'web_screen':old.RUN/'evaluation/result/web/evaluation/result.json',
                     'story_screen':old.RUN/'evaluation/result/coherent20/evaluation/result.json',
                     'prior_review':old.RUN/'review.json','prior_training':old.RUN/'result.json',
                     'web_full':old.RUN/'full/web-full.json','story_full':old.RUN/'full/coherent20-full.json',
                     'prior_full_review':old.RUN/'full/review.json'}.items():
        reference[key]=dict(path=str(path),sha256=sha256(path))
    plan.update(reference=reference,pool_ready=dict(path=str(POOL/'ready.json'),sha256=sha256(POOL/'ready.json')),
                pool_content=dict(path=str(POOL/'content-review.json'),sha256=sha256(POOL/'content-review.json')),
                source_sha256={p:sha256(ROOT/p) for p in SOURCES},tests_sha256=sha256(RUN/'tests.xml'),created_at=now(),
                new_improvement_gates=dict(coherence_gain_over_story=8,paired_CI_lower_above=0,EOS_at_least=37,repetition_at_most=18))
    plan.pop('entry_full_review',None);plan.pop('previous_failed_screen',None)
    write_json(CONFIG,plan);write_json(SCHEMA,dict(type='object',additionalProperties=False,required=list(plan),properties={k:{'const':v} for k,v in plan.items()}))
    print('Frozen one500M candidate; all old controls reused, no new training yet',flush=True)


def load_config():
    config=read_json(CONFIG);validate(config,read_json(SCHEMA))
    assert config['implementation']==implementation_hashes() and config['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    for ref in (*config['reference'].values(),config['pool_ready'],config['pool_content']): assert sha256(Path(ref['path']))==ref['sha256']
    assert sha256(RUN/'tests.xml')==config['tests_sha256']
    for path,digest in ((ROOT/config['tokenizer'],config['tokenizer_sha256']),(ROOT/'eval/base.jsonl',config['suite_sha256']),
                        (Path(config['pool']['pool'])/'manifest.json',config['pool']['manifest_sha256']),
                        (Path(config['dev_shards'])/'manifest.json',config['dev_manifest_sha256']),
                        (ROOT/config['evaluation']['config'],config['evaluation']['config_sha256']),
                        (ROOT/config['evaluation']['semantic_suite'],config['evaluation']['semantic_sha256']),
                        (Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'),config['evaluation']['data_manifest_sha256'])):
        assert sha256(path)==digest
    return config


def run_gpu(mode):
    config=load_config();output=RUN if mode=='screen' else RUN/'full';output.mkdir(parents=True,exist_ok=True)
    binding=dict(plan_sha256=sha256(CONFIG),parent=config['parent'],implementation=config['implementation'],source_sha256=config['source_sha256'],
                 peak_lr=config['peak_lr'],arm='whole20',short_manifest_sha256=config['pool']['manifest_sha256'])
    if mode=='full':
        review=read_json(RUN/'review.json');assert review['status']=='passed' and review['eligible_for_full']
        binding['review_sha256']=sha256(RUN/'review.json')
    path=output/(mode+'-job.json');previous=read_json(path) if path.exists() else {}
    if previous:
        assert previous['binding']==binding and not alive(previous),'Different binding or actual live job'
        if previous['status']=='complete':print('Reuse completed job');return
    prior=previous.get('gpu_elapsed_seconds',0);started=[None];stopped=[False];budget=config[mode+'_gpu_budget_seconds']
    job=dict(status='starting',**identity(),binding=binding,started_at=previous.get('started_at',now()),gpu_elapsed_seconds=prior,
             restart_command=f'scripts/run_complete_document_500m.ps1 -Mode {mode}')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; completed updates retained')
        if started[0] is not None and prior+time.monotonic()-started[0]>budget:raise TimeoutError('Cumulative frozen GPU budget exhausted')
    def heartbeat(stage,**extra):
        check();job.update(stage=stage,heartbeat_at=now(),**extra)
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)
    try:
        heartbeat('setup')
        for relative in (*SOURCES,str(CONFIG.relative_to(ROOT)),str(SCHEMA.relative_to(ROOT))):
            target=output/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        dev=Shard(Path(config['dev_shards']),'dev');tok=Tokenizer(ROOT/config['tokenizer']);seed_all(42);torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            started[0]=time.monotonic();deadline=started[0]+budget-prior
            if mode=='screen':
                assert sha256(Path(config['parent']['path']))==config['parent']['sha256']
                parent=torch.load(config['parent']['path'],map_location='cpu',weights_only=False);assert finite_state(parent)
                web=TrainView(config['web_shards'],config['web_manifest_sha256']);pool=TrainView(config['pool']['pool'],config['pool']['manifest_sha256'],check_stream=True)
                pilot.PilotTrainer=LowLRPilotTrainer;heartbeat('resume-gate')
                gate=pilot.exact_gate(parent,web,pool,binding,RUN,check)
                # Reuse measured trainer/schedule/checkpoint implementation; only the new RUN is assigned.
                old.RUN=RUN
                trained=old.train_arm('whole20',parent,web,pool,config,binding,heartbeat,check)
                comparison.RUN=RUN
                evaluated=comparison.evaluate('whole20',trained,dev,tok,config,binding,heartbeat,check,deadline)
                result=dict(status='complete_pending_content_review',binding=binding,trained=trained,evaluation=evaluated,
                            scientific_tokens=trained['additional_input_tokens'],verification_tokens=gate['input_tokens'],resume_gate=gate,
                            protected_test_used=False,GPU_seconds=prior+time.monotonic()-started[0],completed_at=now())
                write_json(RUN/'result.json',result)
            else:
                trained=read_json(RUN/'result.json')['trained']
                record=evaluate_full(Path(trained['checkpoint']),dev,tok,None,output/'candidate-full.json',binding,heartbeat,check,full=True)
                control=read_json(Path(config['reference']['web_full']['path']));previous_story=read_json(Path(config['reference']['story_full']['path']))
                parent_body=read_json(Path(config['reference']['parent_body']['path']))['body'];parent_gen=read_json(Path(config['reference']['parent_generation']['path']))['generation']
                for other in (control,previous_story,dict(body=parent_body,generation=parent_gen)):
                    require_alignment(record['body'],record['generation'],other['body'],other['generation'])
                state=torch.load(trained['checkpoint'],map_location='cpu',weights_only=False)
                model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True);bound_evaluation_cache(model)
                before=rng_state();hook=model.register_forward_pre_hook(lambda *_:check())
                with sdpa_kernel(SDPBackend.MATH):
                    long=evaluate_long(NativeLikelihood(model,tok,batch=16),read_json(ROOT/config['evaluation']['config']),output,json.dumps(binding,sort_keys=True),deadline)
                hook.remove();assert long['complete'] and pilot.equal_state(before,rng_state());check()
                summary=summarize('whole20',trained['tokens'],record['body'],record['generation']);parent=summarize('parent10B',config['parent']['tokens_seen'],parent_body,parent_gen)
                checks=dict(mixture=adoption_checks(control,record),parent_growth=growth_checks(summary,parent))
                result=dict(status='complete',binding=binding,summary=summary,parent=parent,long_generation=long,checks=checks,
                            candidate_passes_all_full_conditions=all(checks['mixture'].values()) and all(checks['parent_growth'].values()),
                            additional_training_tokens=0,protected_test_used=False,quality_targets_achieved=False,independent_human_blind='not performed',
                            GPU_seconds=prior+time.monotonic()-started[0],completed_at=now())
                write_json(output/'result.json',result);del state,model;gc.collect();torch.cuda.empty_cache()
            heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps({k:v for k,v in result.items() if k not in ('evaluation','long_generation','trained','resume_gate')},ensure_ascii=False),flush=True)
    except BaseException as error:
        job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('freeze','screen','full','probe'),default='screen');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='freeze':freeze()
    elif args.mode=='probe':
        load_config()
        for path in (RUN/'screen-job.json',RUN/'full/full-job.json'):
            if path.exists():assert not alive(read_json(path))
        print('Frozen candidate valid; no live candidate job')
    else:run_gpu(args.mode)
