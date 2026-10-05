"""Plan52: one20% lower-LR100M fork, immutable matched control, eligible full evaluation."""
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
import run_story10_low_lr as saved
import run_story10_comparison as selection
import run_complete_text_comparison as comparison
import run_eos_short_pilot as pilot
from run_eos_5b_finish import evaluate as evaluate_full
from run_eos_complete_100m import adoption_checks
from compare_base_10b import require_alignment,growth_checks
from compare_base_5b import summarize
from review_eos_5b_finish import validate_rows
from evaluate_japanese_base import evaluate_long

CONFIG=ROOT/'configs/phase6/story20_low_lr_10b_100m.json'
SCHEMA=ROOT/'schemas/configs/phase6/story20_low_lr_10b_100m.schema.json'
RUN=ROOT/'reports/phase6/story20-low-lr-10b-100m-20261005'
SOURCES=tuple(dict.fromkeys(('scripts/run_story20_low_lr.py','scripts/run_story20_low_lr.ps1',*saved.SOURCES)))


def next_plan(base):
    plan=dict(base)
    plan.update(arms={'coherent20':dict(pool=base['pool']['pool'],manifest_sha256=base['pool']['manifest_sha256'],short_updates=610)},
                scientific_total_tokens=100007936,scope='Authorized plan52 stages1–4:20% lowerLR100M, eligible full, conditional500M, judgment and stop',
                output=str(RUN.relative_to(ROOT)),screen_gpu_budget_seconds=900,full_gpu_budget_seconds=3000)
    return plan


def freeze():
    assert not (RUN/'screen-job.json').exists(),'Started config is immutable'
    base=saved.load_config();review=read_json(saved.RUN/'review.json')
    assert review['status']=='passed' and not review['selection']['eligible_for_full']
    plan=next_plan(base)
    plan['reference']={k:v for k,v in base['reference'].items() if k in ('parent_body','parent_generation')}
    for key,path in {'screen':saved.RUN/'web/evaluation/result.json','content':saved.RUN/'review.json',
                     'control_training':saved.RUN/'result.json','control_config':saved.CONFIG}.items():
        plan['reference'][key]=dict(path=str(path),sha256=sha256(path))
    assert read_json(Path(plan['reference']['screen']['path']))['checkpoint_sha256']==read_json(saved.RUN/'result.json')['arms']['web']['checkpoint_sha256']
    plan.update(source_sha256={p:sha256(ROOT/p) for p in SOURCES},tests_sha256=sha256(RUN/'tests.xml'),created_at=now())
    suites=list(ET.parse(RUN/'tests.xml').getroot().iter('testsuite'))
    assert sum(int(s.attrib['tests']) for s in suites)>=4 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped'))
    write_json(CONFIG,plan)
    write_json(SCHEMA,dict(type='object',additionalProperties=False,required=list(plan),properties={k:{'const':v} for k,v in plan.items()}))
    print('Frozen20% lowerLR100M; matched lowerLR Web reused; original gates unchanged',flush=True)


def load_config():
    config=read_json(CONFIG);validate(config,read_json(SCHEMA))
    assert config['implementation']==implementation_hashes()
    assert config['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    for ref in config['reference'].values():assert sha256(Path(ref['path']))==ref['sha256']
    assert sha256(Path(config['previous_failed_screen']['path']))==config['previous_failed_screen']['sha256']
    for p,d in [(ROOT/config['tokenizer'],config['tokenizer_sha256']),
                (ROOT/'eval/base.jsonl',config['suite_sha256']),
                (Path(config['pool']['pool'])/'manifest.json',config['pool']['manifest_sha256']),
                (Path(config['dev_shards'])/'manifest.json',config['dev_manifest_sha256']),
                (ROOT/config['evaluation']['config'],config['evaluation']['config_sha256']),
                (ROOT/config['evaluation']['semantic_suite'],config['evaluation']['semantic_sha256']),
                (Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'),config['evaluation']['data_manifest_sha256']),
                (RUN/'tests.xml',config['tests_sha256'])]:assert sha256(p)==d
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
        assert not alive(old) and old['binding']==binding,'Inspect actual existing job before resuming'
        if old['status']=='complete':print('Reuse completed job');return
    prior=old.get('gpu_elapsed_seconds',0);start=[None];stopped=[False];budget=config[mode+'_gpu_budget_seconds']
    job=dict(status='starting',**identity(),binding=binding,gpu_elapsed_seconds=prior,started_at=old.get('started_at',now()),
             restart_command=f'scripts/run_story20_low_lr.ps1 -Mode {mode}')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; checkpoints retained')
        if start[0] is not None and prior+time.monotonic()-start[0]>budget:raise TimeoutError('Cumulative frozen GPU budget exhausted')
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
                branch=comparison.arm_binding(binding,config,'coherent20')
                trained=comparison.train_arm('coherent20',parent,web,pool,config,branch,heartbeat,check)
                evaluated=comparison.evaluate('coherent20',trained,dev,tok,config,branch,heartbeat,check,deadline)
                control=read_json(Path(config['reference']['screen']['path']))
                result=dict(status='complete_pending_content_review',binding=binding,trained=trained,
                            rates=evaluated['greedy_rates'],screen_BPB=evaluated['body']['bpb'],diagnostics=evaluated['diagnostics'],
                            mixture=adoption_checks(control,evaluated),resume_gate=gate,scientific_tokens=100007936,
                            verification_tokens=gate['input_tokens'],control_reused=config['reference'],
                            protected_test_used=False,GPU_seconds=prior+time.monotonic()-start[0],completed_at=now())
                write_json(RUN/'result.json',result)
            else:
                trained={'web':read_json(Path(config['reference']['control_training']['path']))['arms']['web'],
                         'coherent20':read_json(RUN/'result.json')['trained']}
                full={};long={}
                parent_body=read_json(Path(config['reference']['parent_body']['path']))['body']
                parent_generation=read_json(Path(config['reference']['parent_generation']['path']))['generation']
                for arm,detail in trained.items():
                    branch={**binding,'arm':arm,'checkpoint_sha256':detail['checkpoint_sha256']}
                    full[arm]=evaluate_full(Path(detail['checkpoint']),dev,tok,None,output/(arm+'-full.json'),branch,heartbeat,check,full=True)
                    require_alignment(full[arm]['body'],full[arm]['generation'],parent_body,parent_generation)
                    state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
                    model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
                    bound_evaluation_cache(model);before=rng_state();hook=model.register_forward_pre_hook(lambda *_:check())
                    with sdpa_kernel(SDPBackend.MATH):
                        long[arm]=evaluate_long(NativeLikelihood(model,tok,batch=16),read_json(ROOT/config['evaluation']['config']),output/arm,json.dumps(branch,sort_keys=True),deadline)
                    hook.remove();assert long[arm]['complete'] and pilot.equal_state(before,rng_state());check()
                    del state,model;gc.collect();torch.cuda.empty_cache()
                summaries={a:summarize(a,d['tokens'],full[a]['body'],full[a]['generation']) for a,d in trained.items()}
                parent=summarize('parent10B',10000007168,parent_body,parent_generation)
                checks=dict(mixture=adoption_checks(full['web'],full['coherent20']),parent_growth=growth_checks(summaries['coherent20'],parent))
                result=dict(status='complete',binding=binding,summary=summaries,parent=parent,long_generation=long,checks=checks,
                            candidate_passes_all_full_conditions=all(checks['mixture'].values()) and all(checks['parent_growth'].values()),
                            additional_training_tokens=0,protected_test_used=False,quality_targets_achieved=False,
                            independent_human_blind='not performed',GPU_seconds=prior+time.monotonic()-start[0],completed_at=now())
                write_json(output/'result.json',result)
            heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps({k:v for k,v in result.items() if k in ('status','rates','screen_BPB','mixture','checks','GPU_seconds')}),flush=True)
    except BaseException as error:
        job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(job_path,job)


def review_screen():
    config=load_config();screen=read_json(RUN/'result.json');job=read_json(RUN/'screen-job.json')
    assert job['status']=='complete' and not alive(job) and screen['GPU_seconds']<=config['screen_gpu_budget_seconds']
    evaluated=read_json(RUN/'coherent20/evaluation/result.json');rows=evaluated['generation']['outputs']
    tok=Tokenizer(ROOT/config['tokenizer']);validate_rows(rows,tok)
    annotations=read_json(RUN/'annotations.json')
    assert annotations['generation_sha256']==sha256(RUN/'coherent20/evaluation/generation.json')
    scores={r[0]:dict(grammar=r[1],relevance=r[2],coherence=r[3],completion=r[4],rationale=r[5]) for r in annotations['scores']}
    assert len(scores)==len(annotations['scores'])==len(rows)==80 and set(scores)=={r['id'] for r in rows}
    for row in rows:
        s=scores[row['id']]
        assert all(s[k] in (0,1,2) for k in ('grammar','relevance','coherence')) and s['completion'] in (0,1) and s['rationale']
        assert not s['completion'] or row['stop_reason']=='stop_id'
    control=read_json(Path(config['reference']['screen']['path']))
    control_scores={r['id']:r for r in read_json(Path(config['reference']['content']['path']))['scored_outputs']['web']}
    checks=selection.selection_checks(control,evaluated,control_scores,scores)
    trained=screen['trained'];assert sha256(Path(trained['checkpoint']))==trained['checkpoint_sha256']
    state=torch.load(trained['checkpoint'],map_location='cpu',weights_only=False)
    history=[json.loads(line) for line in (RUN/'coherent20/metrics.jsonl').read_text().splitlines()]
    assert finite_state(state) and state['pilot_binding']==trained['binding']==evaluated['binding']
    assert state['update']==308228 and state['tokens']==10100015104 and len(history)==3052
    assert [r['update'] for r in history]==list(range(305177,308229))
    assert all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for r in history)
    assert state['sampler']['source_tokens']==dict(web=80019456,short=19988480) and state['sampler']['short']['epoch']==0
    assert all(k in state for k in ('model','optimizer','scheduler','rng','sampler','tokens','token_digest'))
    assert state['spec']['lr']==.0001 and evaluated['evaluation_RNG_isolated']
    assert screen['resume_gate']['passed'] and all(screen['resume_gate']['checks'].values()) and screen['verification_tokens']==262144
    assert all(evaluated['diagnostics'][t]['complete'] for t in config['evaluation']['tasks'])
    diagnostics={};control_directory=Path(config['reference']['screen']['path']).parent
    for task in config['evaluation']['tasks']:
        a={r['id']:r for r in read_json(control_directory/(task+'.json'))['rows']}
        b={r['id']:r for r in read_json(RUN/'coherent20/evaluation'/(task+'.json'))['rows']}
        assert set(a)==set(b)
        diagnostics[task]=clustered_ci([dict(id=k,family=a[k].get('family',k),difference=b[k]['credit']-a[k]['credit']) for k in a],key='difference')
    summary={k+'_score2':sum(s[k]==2 for s in scores.values()) for k in ('grammar','relevance','coherence')}
    summary.update(count=80,appropriate_EOS=sum(s['completion'] for s in scores.values()))
    review=dict(status='passed',checked_at=now(),config_sha256=sha256(CONFIG),screen_sha256=sha256(RUN/'result.json'),selection=checks,
                summary=summary,paired_diagnostics=diagnostics,scientific_tokens=100007936,verification_tokens=262144,
                protected_test_used=False,quality_targets_achieved=False,independent_human_blind='not performed',
                rows=[dict(row,**scores[row['id']]) for row in rows],reviewer_source_sha256=sha256(Path(__file__)))
    write_json(RUN/'review.json',review)
    print(json.dumps({k:v for k,v in review.items() if k!='rows'},ensure_ascii=False),flush=True)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('freeze','screen','full','review','probe'),default='screen');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='freeze':freeze()
    elif args.mode=='review':review_screen()
    elif args.mode=='probe':
        load_config()
        for path in (RUN/'screen-job.json',RUN/'full/full-job.json'):
            if path.exists():assert not alive(read_json(path)),'Actual job live; no duplicate'
        print('Plan52 config valid; no live comparison job')
    else:run_gpu(args.mode)


if __name__=='__main__':main()
