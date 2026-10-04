"""One prespecified lower-LR matched comparison after the ten-percent screen failed."""
import argparse
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
import numpy as np
import torch
from jsonschema import validate
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.training import atomic_json,gpu_lock,seed_all,rng_state,implementation_hashes
from jmicro.eos_pilot import TrainView
from jmicro.low_lr_pilot import LowLRPilotTrainer
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.model import JMicroModel
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.japanese_evaluation import NativeLikelihood,clustered_ci
from phase6_performance import identity,alive,finite_state
import run_story10_comparison as previous
import run_complete_text_comparison as comparison
import run_eos_short_pilot as pilot
from run_eos_5b_finish import evaluate as evaluate_full
from run_eos_complete_100m import adoption_checks
from compare_base_10b import require_alignment,growth_checks
from compare_base_5b import summarize
from review_eos_5b_finish import validate_rows
from evaluate_japanese_base import evaluate_long

CONFIG=ROOT/'configs/phase6/story10_low_lr_10b_100m.json'
SCHEMA=ROOT/'schemas/configs/phase6/story10_low_lr_10b_100m.schema.json'
RUN=ROOT/'reports/phase6/story10-low-lr-10b-100m-20261005'
SOURCES=tuple(dict.fromkeys(('scripts/run_story10_low_lr.py','scripts/run_story10_low_lr.ps1',*previous.SOURCES)))


def lower_plan(base):
    plan=dict(base)
    plan.update(peak_lr=.0001,scientific_total_tokens=200015872,
                arms={'web':dict(pool=base['pool']['pool'],manifest_sha256=base['pool']['manifest_sha256'],short_updates=0),
                      'coherent10':dict(pool=base['pool']['pool'],manifest_sha256=base['pool']['manifest_sha256'],short_updates=305)})
    return plan


def freeze():
    assert not (RUN/'screen-job.json').exists()
    base=previous.load_config();failed=read_json(previous.RUN/'review.json')
    assert failed['status']=='passed' and not failed['selection']['eligible_for_full']
    plan=lower_plan(base)
    plan.update(scope='Plan49 bounded lower-LR alternative; matchedWeb/10%100M then judge/propose; no automatic500M',
                output=str(RUN.relative_to(ROOT)),screen_gpu_budget_seconds=1800,full_gpu_budget_seconds=3000,
                previous_failed_screen=dict(path=str(previous.RUN/'review.json'),sha256=sha256(previous.RUN/'review.json')),
                source_sha256={p:sha256(ROOT/p) for p in SOURCES},tests_sha256=sha256(RUN/'tests.xml'),created_at=now())
    suites=list(ET.parse(RUN/'tests.xml').getroot().iter('testsuite'))
    assert sum(int(s.attrib['tests']) for s in suites)>=7 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped'))
    write_json(CONFIG,plan)
    write_json(SCHEMA,dict(type='object',additionalProperties=False,required=list(plan),properties={k:{'const':v} for k,v in plan.items()}))
    print('Frozen lowerLR .0001 Web/10% each100M; all other conditions preserved',flush=True)


def load_config():
    config=read_json(CONFIG);validate(config,read_json(SCHEMA))
    assert config['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES} and config['implementation']==implementation_hashes()
    assert sha256(Path(config['previous_failed_screen']['path']))==config['previous_failed_screen']['sha256']
    assert sha256(RUN/'tests.xml')==config['tests_sha256']
    for ref in config['reference'].values():assert sha256(Path(ref['path']))==ref['sha256']
    for p,d in [(ROOT/config['tokenizer'],config['tokenizer_sha256']),
                (ROOT/'eval/base.jsonl',config['suite_sha256']),
                (Path(config['pool']['pool'])/'manifest.json',config['pool']['manifest_sha256']),
                (Path(config['dev_shards'])/'manifest.json',config['dev_manifest_sha256']),
                (ROOT/config['evaluation']['config'],config['evaluation']['config_sha256']),
                (ROOT/config['evaluation']['semantic_suite'],config['evaluation']['semantic_sha256']),
                (Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'),config['evaluation']['data_manifest_sha256'])]:assert sha256(p)==d
    return config


def run_gpu(mode):
    config=load_config();output=RUN if mode=='screen' else RUN/'full';output.mkdir(parents=True,exist_ok=True)
    binding=dict(plan_sha256=sha256(CONFIG),parent=config['parent'],peak_lr=config['peak_lr'],
                 implementation=config['implementation'],source_sha256=config['source_sha256'])
    if mode=='full':
        review=read_json(RUN/'review.json');assert review['status']=='passed' and review['selection']['eligible_for_full']
        binding['review_sha256']=sha256(RUN/'review.json')
    job_path=output/(mode+'-job.json');old=read_json(job_path) if job_path.exists() else {}
    if old:
        assert not alive(old) and old['binding']==binding
        if old['status']=='complete':print('Reuse completed lowerLR job');return
    prior=old.get('gpu_elapsed_seconds',0);start=[None];stopped=[False];budget=config[mode+'_gpu_budget_seconds']
    job=dict(status='starting',**identity(),binding=binding,gpu_elapsed_seconds=prior,started_at=old.get('started_at',now()),
             restart_command=f'scripts/run_story10_low_lr.ps1 -Mode {mode}')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; checkpoints retained')
        if start[0] is not None and prior+time.monotonic()-start[0]>budget:raise TimeoutError('Cumulative lowerLR budget exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(job_path,job)
    try:
        heartbeat('setup')
        for relative in (*SOURCES,str(CONFIG.relative_to(ROOT))):
            target=output/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        dev=Shard(Path(config['dev_shards']),'dev');tok=Tokenizer(ROOT/config['tokenizer'])
        seed_all(42);torch.use_deterministic_algorithms(True);comparison.RUN=RUN
        with gpu_lock('cuda'):
            start[0]=time.monotonic();deadline=start[0]+budget-prior
            if mode=='screen':
                assert sha256(Path(config['parent']['path']))==config['parent']['sha256']
                parent=torch.load(config['parent']['path'],map_location='cpu',weights_only=False)
                web=TrainView(config['web_shards'],config['web_manifest_sha256'])
                pool=TrainView(config['pool']['pool'],config['pool']['manifest_sha256'],check_stream=True)
                pilot.PilotTrainer=LowLRPilotTrainer
                gate=pilot.exact_gate(parent,web,pool,{**binding,'arm':'gate'},RUN,check)
                trained,evaluated={},{}
                for arm in config['arms']:
                    branch=comparison.arm_binding(binding,config,arm)
                    trained[arm]=comparison.train_arm(arm,parent,web,pool,config,branch,heartbeat,check)
                    evaluated[arm]=comparison.evaluate(arm,trained[arm],dev,tok,config,branch,heartbeat,check,deadline)
                result=dict(status='complete_pending_content_review',binding=binding,arms=trained,
                            rates={a:v['greedy_rates'] for a,v in evaluated.items()},BPB={a:v['body']['bpb'] for a,v in evaluated.items()},
                            diagnostics={a:v['diagnostics'] for a,v in evaluated.items()},
                            mixture=adoption_checks(evaluated['web'],evaluated['coherent10']),resume_gate=gate,
                            scientific_tokens=sum(v['additional_input_tokens'] for v in trained.values()),verification_tokens=gate['input_tokens'],
                            protected_test_used=False,GPU_seconds=prior+time.monotonic()-start[0],completed_at=now())
                assert result['scientific_tokens']==200015872
                write_json(RUN/'result.json',result)
            else:
                screen=read_json(RUN/'result.json');full={};long={}
                parent_body=read_json(Path(config['reference']['parent_body']['path']))['body']
                parent_generation=read_json(Path(config['reference']['parent_generation']['path']))['generation']
                for arm,trained in screen['arms'].items():
                    branch={**binding,'arm':arm,'checkpoint_sha256':trained['checkpoint_sha256']}
                    full[arm]=evaluate_full(Path(trained['checkpoint']),dev,tok,None,output/(arm+'-full.json'),branch,heartbeat,check,full=True)
                    require_alignment(full[arm]['body'],full[arm]['generation'],parent_body,parent_generation)
                    state=torch.load(trained['checkpoint'],map_location='cpu',weights_only=False)
                    model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
                    bound_evaluation_cache(model);before=rng_state();hook=model.register_forward_pre_hook(lambda *_:check())
                    with sdpa_kernel(SDPBackend.MATH):
                        long[arm]=evaluate_long(NativeLikelihood(model,tok,batch=16),read_json(ROOT/config['evaluation']['config']),output/arm,json.dumps(branch,sort_keys=True),deadline)
                    hook.remove();assert long[arm]['complete'] and pilot.equal_state(before,rng_state());check()
                    del state,model;gc.collect();torch.cuda.empty_cache()
                summaries={a:summarize(a,10100015104,r['body'],r['generation']) for a,r in full.items()}
                parent=summarize('parent10B',10000007168,parent_body,parent_generation)
                checks=dict(mixture=adoption_checks(full['web'],full['coherent10']),parent_growth=growth_checks(summaries['coherent10'],parent))
                result=dict(status='complete',binding=binding,summary=summaries,parent=parent,long_generation=long,checks=checks,
                            candidate_passes_all_full_conditions=all(checks['mixture'].values()) and all(checks['parent_growth'].values()),
                            additional_training_tokens=0,protected_test_used=False,quality_targets_achieved=False,
                            independent_human_blind='not performed',GPU_seconds=prior+time.monotonic()-start[0],completed_at=now())
                write_json(output/'result.json',result)
            heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps({k:v for k,v in result.items() if k in ('status','rates','BPB','mixture','checks','GPU_seconds')}),flush=True)
    except BaseException as error:
        job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(job_path,job)


def review_screen():
    config=load_config();screen=read_json(RUN/'result.json');job=read_json(RUN/'screen-job.json')
    assert job['status']=='complete' and not alive(job) and screen['GPU_seconds']<=config['screen_gpu_budget_seconds']
    annotations=read_json(RUN/'annotations.json');scores={};evaluated={};summaries={}
    tok=Tokenizer(ROOT/config['tokenizer'])
    for arm in config['arms']:
        generation=RUN/arm/'evaluation/generation.json'
        assert annotations['generation_sha256'][arm]==sha256(generation)
        evaluated[arm]=read_json(RUN/arm/'evaluation/result.json');rows=evaluated[arm]['generation']['outputs']
        validate_rows(rows,tok)
        entries=annotations['scores'][arm]
        scores[arm]={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in entries}
        assert len(scores[arm])==len(entries)==len(rows)==80 and set(scores[arm])=={r['id'] for r in rows}
        for row in rows:
            s=scores[arm][row['id']]
            assert all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) and s['rationale']
            assert not s['completion'] or row['stop_reason']=='stop_id'
        trained=screen['arms'][arm];assert sha256(Path(trained['checkpoint']))==trained['checkpoint_sha256']
        state=torch.load(trained['checkpoint'],map_location='cpu',weights_only=False)
        history=[json.loads(line) for line in (RUN/arm/'metrics.jsonl').read_text().splitlines()]
        assert finite_state(state) and state['pilot_binding']==trained['binding']==evaluated[arm]['binding']
        assert state['update']==308228 and state['tokens']==10100015104 and len(history)==3052
        assert [r['update'] for r in history]==list(range(305177,308229))
        assert all(np.isfinite(r['loss']) and np.isfinite(r['gradient_norm']) for r in history)
        expected_short=config['arms'][arm]['short_updates']*32768
        assert state['sampler']['source_tokens']==dict(web=100007936-expected_short,short=expected_short) and state['sampler']['short']['epoch']==0
        assert all(k in state for k in ('model','optimizer','scheduler','rng','sampler','tokens','token_digest'))
        assert state['spec']['lr']==.0001 and evaluated[arm]['evaluation_RNG_isolated']
        assert all(evaluated[arm]['diagnostics'][t]['complete'] for t in config['evaluation']['tasks'])
        summaries[arm]={k+'_score2':sum(s[k]==2 for s in scores[arm].values()) for k in ('grammar','relevance','coherence')}
        summaries[arm].update(count=80,appropriate_EOS=sum(s['completion'] for s in scores[arm].values()))
    assert screen['resume_gate']['passed'] and all(screen['resume_gate']['checks'].values())
    assert screen['scientific_tokens']==200015872 and screen['verification_tokens']==262144
    selection=previous.selection_checks(evaluated['web'],evaluated['coherent10'],scores['web'],scores['coherent10'])
    paired={}
    for task in config['evaluation']['tasks']:
        a={r['id']:r for r in read_json(RUN/'web/evaluation'/(task+'.json'))['rows']}
        b={r['id']:r for r in read_json(RUN/'coherent10/evaluation'/(task+'.json'))['rows']}
        assert set(a)==set(b)
        paired[task]=clustered_ci([dict(id=k,family=a[k].get('family',k),difference=b[k]['credit']-a[k]['credit']) for k in a],key='difference')
    review=dict(status='passed',checked_at=now(),config_sha256=sha256(CONFIG),screen_sha256=sha256(RUN/'result.json'),
                selection=selection,summary=summaries,paired_diagnostics=paired,scientific_tokens=200015872,verification_tokens=262144,
                protected_test_used=False,quality_targets_achieved=False,independent_human_blind='not performed',
                scored_outputs={a:[dict(row,**scores[a][row['id']]) for row in evaluated[a]['generation']['outputs']] for a in config['arms']},
                reviewer_source_sha256=sha256(Path(__file__)))
    write_json(RUN/'review.json',review)
    print(json.dumps({k:v for k,v in review.items() if k!='scored_outputs'},ensure_ascii=False),flush=True)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('freeze','screen','full','review','probe'),default='screen');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='freeze':freeze()
    elif args.mode=='review':review_screen()
    elif args.mode=='probe':
        load_config()
        for path in (RUN/'screen-job.json',RUN/'full/full-job.json'):
            if path.exists():assert not alive(read_json(path)),'Actual job live; no duplicate'
        print('LowerLR config valid; no live comparison job')
    else:run_gpu(args.mode)


if __name__=='__main__':main()
