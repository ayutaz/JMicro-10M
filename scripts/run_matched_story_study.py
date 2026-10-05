"""Plan56: matched content contrast, then required constant-LR learning budget study."""
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
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from jsonschema import validate
from torch.nn.attention import sdpa_kernel,SDPBackend
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
from run_eos_5b_finish import evaluate as evaluate_full
from run_eos_complete_100m import adoption_checks
from compare_base_10b import require_alignment,growth_checks
from compare_base_5b import summarize
from evaluate_japanese_base import evaluate_long
import run_story20_budget as old
import run_complete_text_comparison as comparison
import run_eos_short_pilot as pilot

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/matched-story-content-20261005')
OLD_RUN=old.RUN
SOURCES=tuple(dict.fromkeys(('scripts/run_matched_story_study.py','scripts/run_matched_story_study.ps1',
    'scripts/review_matched_story_study.py','scripts/prepare_matched_story_pools.py','src/jmicro/story_quality.py',*old.SOURCES)))

def paths(stage):
    name='matched-story-content-500m' if stage=='content' else 'story-constant-lr-1b'
    return ROOT/f'reports/phase6/{name}-20261005',ROOT/f'configs/phase6/{stage}_story_study.json',ROOT/f'schemas/configs/phase6/{stage}_story_study.schema.json'

def budget_settings(stage):
    return dict(updates_per_arm=15259 if stage=='content' else 30518,stable_updates=14500 if stage=='content' else 30518,
        decay_updates=759 if stage=='content' else 1,tokens_per_arm=500006912 if stage=='content' else 1000013824,
        final_update=320435 if stage=='content' else 335694,final_tokens=10500014080 if stage=='content' else 11000020992,
        scientific_total_tokens=1000013824,screen_gpu_budget_seconds=2400,full_gpu_budget_seconds=1800 if stage=='content' else 3000,
        short_updates=3051 if stage=='content' else 6102,midpoint_update=320435 if stage=='amount' else None)

def freeze(stage):
    run,config_path,schema=paths(stage);assert not (run/'screen-job.json').exists(),'Started config immutable'
    base=old.load_config();plan=copy.deepcopy(base);ready=read_json(DATA/'ready.json')
    content=read_json(DATA/'content-review.json')
    assert ready['matched_quantity_length_sequence_EOS_positions'] and ready['source_train_only'] and ready['whole_original_stories']
    assert ready['totals']['control']==ready['totals']['refined'] and ready['totals']['control']['tokens']>=20000000
    assert abs(ready['body_tokens_mean']/ready['old_body_tokens_mean']-1)<=.05
    assert content['accepted_for_experiment'] and content['ready_sha256']==sha256(DATA/'ready.json')
    for arm in ready['pools']:
        detail=content['arms'][arm];directory=Path(ready['pools'][arm]['pool'])
        assert detail['manifest_sha256']==sha256(directory/'manifest.json') and detail['samples_sha256']==sha256(directory/'samples.json') and len(detail['notes'])==40
    pools=ready['pools'];selection=None
    if stage=='amount':
        prior=read_json(paths('content')[0]/'review.json');assert prior['status']=='passed'
        selected=prior['eligible_for_full'] and read_json(paths('content')[0]/'full/review.json')['candidate_passes_all_full_conditions']
        chosen=ready['pools']['refined'] if selected else base['pool']
        pools={'fixed20':chosen}
        selection=dict(reason='Matched content passes all primary/full gates' if selected else 'Content condition not adopted; retained accepted story59.96M',
            content_review=dict(path=str(paths('content')[0]/'review.json'),sha256=sha256(paths('content')[0]/'review.json')),selected_refined=selected)
        if selected:selection['full_review']=dict(path=str(paths('content')[0]/'full/review.json'),sha256=sha256(paths('content')[0]/'full/review.json'))
    suites=list(ET.parse(run/'tests.xml').getroot().iter('testsuite'))
    assert sum(int(s.attrib['tests']) for s in suites)>=8 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped'))
    settings=budget_settings(stage);short=settings.pop('short_updates')
    plan.update(settings,scope='Authorized plan56 stages1–3; '+stage,stage=stage,output=str(run.relative_to(ROOT)),
        arms={a:dict(p,short_updates=short) for a,p in pools.items()},selection=selection,
        pool_ready=dict(path=str(DATA/'ready.json'),sha256=sha256(DATA/'ready.json')),
        pool_content=dict(path=str(DATA/'content-review.json'),sha256=sha256(DATA/'content-review.json')),
        tests_sha256=sha256(run/'tests.xml'),source_sha256={p:sha256(ROOT/p) for p in SOURCES},created_at=now())
    plan['pool']=next(iter(pools.values()))
    plan['reference']={k:base['reference'][k] for k in ('parent_body','parent_generation')}
    for label,path in {'old_review':OLD_RUN/'review.json','old_training':OLD_RUN/'result.json',
        'web_screen':OLD_RUN/'evaluation/result/web/evaluation/result.json','story_screen':OLD_RUN/'evaluation/result/coherent20/evaluation/result.json',
        'web_full':OLD_RUN/'full/web-full.json','story_full':OLD_RUN/'full/coherent20-full.json','old_full_review':OLD_RUN/'full/review.json'}.items():
        plan['reference'][label]=dict(path=str(path),sha256=sha256(path))
    for k in ('entry_full_review','previous_failed_screen','intermediate_update','intermediate_tokens','intermediate_additional_tokens','new_improvement_gates'):
        plan.pop(k,None)
    plan['total_GPU_budget_seconds']=settings['screen_gpu_budget_seconds']+settings['full_gpu_budget_seconds']
    write_json(config_path,plan);write_json(schema,dict(type='object',additionalProperties=False,required=list(plan),properties={k:{'const':v} for k,v in plan.items()}))
    print(json.dumps(dict(stage=stage,status='frozen',selection=selection,pools=pools)),flush=True)

def load_config(stage):
    run,path,schema=paths(stage);c=read_json(path);validate(c,read_json(schema))
    assert c['implementation']==implementation_hashes() and c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    references=[*c['reference'].values(),c['pool_ready'],c['pool_content']]
    if c['selection']:references.extend(v for v in c['selection'].values() if isinstance(v,dict) and 'sha256' in v)
    for ref in references:assert sha256(Path(ref['path']))==ref['sha256']
    assert c['tests_sha256']==sha256(run/'tests.xml')
    for p,d in ((ROOT/c['tokenizer'],c['tokenizer_sha256']),(ROOT/'eval/base.jsonl',c['suite_sha256']),
        (Path(c['web_shards'])/'manifest.json',c['web_manifest_sha256']),(Path(c['dev_shards'])/'manifest.json',c['dev_manifest_sha256']),
        (ROOT/c['evaluation']['config'],c['evaluation']['config_sha256']),(ROOT/c['evaluation']['semantic_suite'],c['evaluation']['semantic_sha256']),
        (Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'),c['evaluation']['data_manifest_sha256'])):assert sha256(p)==d
    for p in c['arms'].values():assert sha256(Path(p['pool'])/'manifest.json')==p['manifest_sha256']
    return c

def train(run,arm,parent,web,pool,c,binding,heartbeat,check):
    directory=run/arm;directory.mkdir(parents=True,exist_ok=True)
    if (directory/'result.json').exists():
        result=read_json(directory/'result.json');assert result['binding']==binding and sha256(Path(result['checkpoint']))==result['checkpoint_sha256'];return result
    routing=pilot.routes(c['updates_per_arm'],c['arms'][arm]['short_updates'])
    if c['stage']=='amount':assert routing[:15259]==pilot.routes(15259,3051) and sum(routing[15259:])==3051
    schedule=dict(parent_update=parent['update'],stable_updates=c['stable_updates'],decay_updates=c['decay_updates'])
    trainer=LowLRPilotTrainer(parent,web,pool,routing,schedule,binding)
    log_path=directory/'metrics.jsonl'
    if (directory/'latest.json').exists():
        last=read_json(directory/'latest.json');assert sha256(Path(last['path']))==last['sha256'];trainer.load(last['path'])
        if log_path.exists():
            rows=[json.loads(line) for line in log_path.read_text().splitlines()]
            if rows and rows[-1]['update']>trainer.update:
                shutil.copyfile(log_path,directory/f'metrics-before-resume-{time.time_ns()}.jsonl')
                log_path.write_text(''.join(json.dumps(row)+'\n' for row in rows if row['update']<=trainer.update))
    prior=read_json(directory/'progress.json').get('training_seconds',0) if (directory/'progress.json').exists() else 0;started=time.monotonic()
    def save(label):
        path=directory/f'checkpoint-{trainer.update:08d}.pt';trainer.save(path);local=trainer.update-parent['update'];short=sum(routing[:local])*32768
        assert trainer.sampler.source_tokens==dict(web=local*32768-short,short=short)
        detail=dict(status='complete',binding=binding,checkpoint=str(path),checkpoint_sha256=sha256(path),update=trainer.update,tokens=trainer.tokens,
            additional_input_tokens=trainer.tokens-parent['tokens'],source_tokens=trainer.sampler.source_tokens.copy(),source_eos_teachers=trainer.sampler.source_eos.copy(),
            sampler=trainer.sampler.state_dict(),training_seconds=prior+time.monotonic()-started,learning_rate_fork=trainer.lineage['learning_rate_fork'],
            checkpoint_role=label,pool=c['arms'][arm],schedule=schedule,completed_at=now())
        write_json(directory/(label+'.json'),detail);return detail
    with log_path.open('a',buffering=1) as log:
        while trainer.update<c['final_update']:
            try:check()
            except (InterruptedError,TimeoutError):trainer.save(directory/f'checkpoint-{trainer.update:08d}.pt');raise
            row=trainer.step();assert math.isfinite(row['loss']) and math.isfinite(row['gradient_norm'])
            if c['stage']=='amount':assert math.isclose(row['lr'],c['peak_lr'],rel_tol=1e-12)
            log.write(json.dumps(dict(row,arm=arm),allow_nan=False)+'\n');local=trainer.update-parent['update']
            if local==1 or local%100==0:
                heartbeat(arm+'-train',updates_completed=local,loss=row['loss'],tokens_per_second=row['tokens_per_second'])
                write_json(directory/'progress.json',dict(training_seconds=prior+time.monotonic()-started,updates_completed=local));print(json.dumps(dict(row,arm=arm)),flush=True)
            if trainer.update==c['midpoint_update']:save('midpoint500M')
            elif local%500==0:trainer.save(directory/f'checkpoint-{trainer.update:08d}.pt')
    result=save('result');assert result['tokens']==c['final_tokens'] and result['additional_input_tokens']==c['tokens_per_arm']
    if c['stage']=='amount':assert (directory/'midpoint500M.json').exists()
    del trainer;gc.collect();torch.cuda.empty_cache();return result

def full_evaluation(run,c,result,binding,heartbeat,check,deadline):
    output=run/'full';primary=read_json(run/'review.json');assert primary['status']=='passed' and primary['eligible_for_full']
    binding=dict(binding,review_sha256=sha256(run/'review.json'));dev=Shard(Path(c['dev_shards']),'dev');tok=Tokenizer(ROOT/c['tokenizer'])
    names=['refined'] if c['stage']=='content' else ['constant500M','constant1B'];records={};longs={};summaries={}
    parent_body=read_json(Path(c['reference']['parent_body']['path']))['body'];parent_gen=read_json(Path(c['reference']['parent_generation']['path']))['generation']
    parent=summarize('parent10B',c['parent']['tokens_seen'],parent_body,parent_gen)
    for name in names:
        detail=result['checkpoints'][name];heartbeat(name+'-full')
        record=evaluate_full(Path(detail['checkpoint']),dev,tok,None,output/(name+'-full.json'),binding,heartbeat,check,full=True)
        require_alignment(record['body'],record['generation'],parent_body,parent_gen);records[name]=record
        model=JMicroModel(torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)['model_config']).to('cuda').eval()
        model.load_state_dict(torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)['model'],strict=True);bound_evaluation_cache(model)
        before=rng_state();hook=model.register_forward_pre_hook(lambda *_:check());longdir=output/name
        with sdpa_kernel(SDPBackend.MATH):long=evaluate_long(NativeLikelihood(model,tok,batch=16),read_json(ROOT/c['evaluation']['config']),longdir,json.dumps(binding,sort_keys=True),deadline)
        hook.remove();assert long['complete'] and pilot.equal_state(before,rng_state());longs[name]=long
        summaries[name]=summarize(name,detail['tokens'],record['body'],record['generation']);del model;gc.collect();torch.cuda.empty_cache()
    candidate=names[-1];control=read_json(Path(c['reference']['web_full']['path'])) if c['stage']=='content' else records['constant500M']
    require_alignment(records[candidate]['body'],records[candidate]['generation'],control['body'],control['generation'])
    gates=dict(mixture=adoption_checks(control,records[candidate]),parent_growth=growth_checks(summaries[candidate],parent))
    if c['stage']=='amount':
        # Matched learning-amount comparison asks for nonworsening EOS, not an additional EOS+8 gate.
        gates['matched_growth']=growth_checks(summaries[candidate],summaries['constant500M'])
        gates.pop('mixture')
    return dict(status='complete',binding=binding,summaries=summaries,parent=parent,long=longs,checks=gates,
        candidate_passes_all_full_conditions=all(v for group in gates.values() for v in group.values()),additional_training_tokens=0,protected_test_used=False)

def run_gpu(stage,mode):
    c=load_config(stage);run,config_path,schema=paths(stage);output=run if mode=='screen' else run/'full';output.mkdir(parents=True,exist_ok=True)
    binding=dict(plan_sha256=sha256(config_path),parent=c['parent'],implementation=c['implementation'],source_sha256=c['source_sha256'],peak_lr=c['peak_lr'],stage=stage)
    if mode=='full':
        assert read_json(run/'review.json')['eligible_for_full'];binding['review_sha256']=sha256(run/'review.json')
    path=output/(mode+'-job.json');prior_job=read_json(path) if path.exists() else {}
    if prior_job:
        assert prior_job['binding']==binding and not alive(prior_job),'Different binding or actual live job'
        if prior_job['status']=='complete':print('Reuse completed job');return
    prior=prior_job.get('gpu_elapsed_seconds',0);started=[None];stopped=[False];budget=c[mode+'_gpu_budget_seconds']
    job=dict(status='starting',**identity(),binding=binding,started_at=prior_job.get('started_at',now()),gpu_elapsed_seconds=prior,
        restart_command=f'scripts/run_matched_story_study.ps1 -Stage {stage} -Mode {mode}')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; completed checkpoints retained')
        if started[0] is not None and prior+time.monotonic()-started[0]>budget:raise TimeoutError('Cumulative frozen GPU budget exhausted')
    def heartbeat(stage_name,**extra):
        check();job.update(stage=stage_name,heartbeat_at=now(),**extra)
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)
    try:
        heartbeat('setup')
        for relative in (*SOURCES,str(config_path.relative_to(ROOT)),str(schema.relative_to(ROOT))):
            target=output/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        seed_all(42);torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            started[0]=time.monotonic();deadline=started[0]+budget-prior
            if mode=='screen':
                assert sha256(Path(c['parent']['path']))==c['parent']['sha256'];parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);assert finite_state(parent)
                web=TrainView(c['web_shards'],c['web_manifest_sha256']);pools={a:TrainView(p['pool'],p['manifest_sha256'],check_stream=True) for a,p in c['arms'].items()}
                if stage=='content':
                    masks=[np.where(np.isin(view.tokens,[2,3]))[0] for view in pools.values()];assert np.array_equal(*masks),'Actual BOS/EOS positions differ'
                pilot.PilotTrainer=LowLRPilotTrainer;heartbeat('resume-gate')
                if stage=='amount':
                    # Verify the actual new constant schedule/counter boundary with resumed mixed CUDA updates.
                    constant_gate=constant_resume_gate(parent,web,next(iter(pools.values())),binding,run,check)
                    gate=constant_gate
                else:
                    constant_gate=None;gate=pilot.exact_gate(parent,web,next(iter(pools.values())),binding,run,check)
                trained={a:train(run,a,parent,web,pool,c,dict(binding,arm=a,short_manifest_sha256=c['arms'][a]['manifest_sha256']),heartbeat,check) for a,pool in pools.items()}
                details=trained if stage=='content' else {'constant500M':read_json(run/'fixed20/midpoint500M.json'),'constant1B':trained['fixed20']}
                dev=Shard(Path(c['dev_shards']),'dev');tok=Tokenizer(ROOT/c['tokenizer']);comparison.RUN=run/'evaluation'
                evaluated={a:comparison.evaluate(a,d,dev,tok,c,d['binding'],heartbeat,check,deadline) for a,d in details.items()}
                result=dict(status='complete_pending_content_review',binding=binding,arms=trained,checkpoints=details,evaluations=evaluated,
                    scientific_tokens=sum(d['additional_input_tokens'] for d in trained.values()),verification_tokens=gate['input_tokens'],
                    resume_gate=gate,constant_resume_gate=constant_gate,selection=c['selection'],protected_test_used=False)
                assert result['scientific_tokens']==c['scientific_total_tokens']
            else:result=full_evaluation(run,c,read_json(run/'result.json'),binding,heartbeat,check,deadline)
            result.update(GPU_seconds=prior+time.monotonic()-started[0],completed_at=now());write_json(output/'result.json',result)
            heartbeat('complete');job.update(status='complete',completed_at=now());print(json.dumps(dict(status=result['status'],GPU_seconds=result['GPU_seconds'])),flush=True)
    except BaseException as error:job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)

def constant_resume_gate(parent,web,pool,binding,run,check):
    path=run/'constant-resume-gate.json'
    if path.exists():
        result=read_json(path);assert result['passed'] and result['binding']==binding;return result
    states=[];histories=[]
    for resumed in (False,True):
        trainer=LowLRPilotTrainer(parent,web,pool,[False,True,False,True],dict(parent_update=parent['update'],stable_updates=30518,decay_updates=1),binding);history=[]
        for local in range(4):
            check();row=trainer.step();history.append({k:row[k] for k in ('loss','gradient_norm','lr','token_digest','tokens_seen')});assert row['lr']==.0001
            if resumed and local==1:
                checkpoint=run/'constant-gate-split.pt';trainer.save(checkpoint);del trainer;gc.collect();torch.cuda.empty_cache()
                trainer=LowLRPilotTrainer(parent,web,pool,[False,True,False,True],dict(parent_update=parent['update'],stable_updates=30518,decay_updates=1),binding);trainer.load(checkpoint)
        checkpoint=run/f'constant-gate-{resumed}.pt';trainer.save(checkpoint);states.append(torch.load(checkpoint,map_location='cpu',weights_only=False));histories.append(history)
        del trainer;gc.collect();torch.cuda.empty_cache()
    checks={k:pilot.equal_state(states[0][k],states[1][k]) for k in ('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','update','spec','lineage')}
    checks['identical_finite_constant_LR_history']=histories[0]==histories[1] and all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) and r['lr']==.0001 for h in histories for r in h)
    result=dict(passed=all(checks.values()),checks=checks,binding=binding,input_tokens=262144,histories=histories,scope='Actual constant-LR mixed-source CUDA continuous/resumed');write_json(path,result);assert result['passed'];return result

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--stage',choices=('content','amount'),required=True);parser.add_argument('--mode',choices=('freeze','probe','screen','full'),default='screen');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='freeze':freeze(args.stage)
    elif args.mode=='probe':
        load_config(args.stage)
        for _,(run,_,_) in ((s,paths(s)) for s in ('content','amount')):
            for p in (run/'screen-job.json',run/'full/full-job.json'):
                if p.exists():assert not alive(read_json(p))
        print('Frozen study valid; no actual live study job')
    else:run_gpu(args.stage,args.mode)
