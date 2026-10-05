"""Bounded literal-document comparison; original frozen training code is reused."""
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
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.eos_pilot import TrainView
from jmicro.natural_learning import NaturalTrainer
from jmicro.narrative_study import structural_summary
from jmicro.model import JMicroModel
from jmicro.readiness import evaluate_batched
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, seed_all
from phase6_performance import identity, alive, finite_state
import run_packing_study as packing
import run_complete_text_comparison as comparison
import run_eos_short_pilot as pilot

RUN=ROOT/'reports/phase6/narrative-diversity-v2-20261005'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/narrative-diversity-v2-20261005')
CONFIG=ROOT/'configs/phase6/narrative_comparison.json'
SOURCES=('scripts/run_narrative_comparison.py','scripts/run_narrative_comparison.ps1',
 'scripts/review_narrative_material.py',
 'scripts/review_narrative_comparison.py','scripts/prepare_narrative_diversity_v2.py',
 'src/jmicro/narrative_diversity.py','src/jmicro/diverse_text.py','src/jmicro/diverse_text_v2.py',
 'src/jmicro/narrative_study.py','tests/test_narrative_study.py','tests/test_narrative_diversity.py',
 'docs/75_diverse_learning_execution.md','docs/77_narrative_diversity_execution.md',
 'docs/78_narrative_supply_execution.md','scripts/run_packing_study.py',
 'src/jmicro/natural_learning.py','src/jmicro/packing_study.py','scripts/run_complete_text_comparison.py',
 'src/jmicro/readiness.py','src/jmicro/eos_pilot.py','src/jmicro/low_lr_pilot.py',
 'src/jmicro/japanese_evaluation.py','src/jmicro/evaluation_memory.py','src/jmicro/tokenizer.py',
 'scripts/review_matched_story_study.py','scripts/run_eos_complete_100m.py')


def freeze():
    if CONFIG.exists():load_config();return
    ready=read_json(DATA/'ready-initial.json');review=read_json(RUN/'content-review.json')
    assert review['sample_sha256']==ready['sample_sha256']==sha256(DATA/'sample-initial.json')
    assert review['weak_documents']<=10 and review['documents']==64 and len(review['reviews'])==64
    assert ready['splits']['train']['documents']>=10000 and ready['splits']['train']['tokens']>=1000000
    suites=list(ET.parse(RUN/'tests.xml').getroot().iter('testsuite'))
    assert sum(int(s.attrib['tests']) for s in suites)>=9
    assert all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped'))
    old=read_json(ROOT/'configs/phase6/natural_learning.json')
    c={k:copy.deepcopy(old[k]) for k in ('parent','web_shards','web_manifest_sha256','dev_shards',
       'dev_manifest_sha256','tokenizer','tokenizer_sha256','suite_sha256','evaluation','reference','peak_lr')}
    c.update(candidate=dict(pool=ready['pool'],manifest_sha256=ready['manifest_sha256'],
           documents=10000,unique_tokens=ready['splits']['train']['tokens']),
       control_pool=old['pools']['natural1000'],dev64_sha256=sha256(DATA/'dev64.json'),
       preparation_sha256=sha256(DATA/'ready-initial.json'),content_review_sha256=sha256(RUN/'content-review.json'),
       tests_sha256=sha256(RUN/'tests.xml'),implementation=implementation_hashes(),
       source_sha256={p:sha256(ROOT/p) for p in SOURCES},
       mixed_train_budget_seconds=600,diagnostic_train_budget_seconds=600,isolated_batch=256,
       comparison_gpu_budget_seconds=1200,expansion_gpu_budget_seconds=1800,
       comparison_teacher_tokens=100000000,comparison_goals=dict(web=80000000,short=20000000),
       expansion_teacher_tokens=500000000,expansion_goals=dict(web=400000000,short=100000000),
       created_at=now(),source_length_EOS_confounded=True,protected_test_used=False,
       scope='Authorized stages1–3; expansion only after all unchanged quality gates; then stop')
    write_json(CONFIG,c)
    print(json.dumps(dict(status='frozen',candidate=c['candidate'],control=c['control_pool'])),flush=True)


def load_config():
    c=read_json(CONFIG)
    assert c['implementation']==implementation_hashes()
    assert c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    paths=[(ROOT/c['tokenizer'],c['tokenizer_sha256']), (ROOT/'eval/base.jsonl',c['suite_sha256']),
       (DATA/'dev64.json',c['dev64_sha256']),(DATA/'ready-initial.json',c['preparation_sha256']),
       (RUN/'content-review.json',c['content_review_sha256']),(RUN/'tests.xml',c['tests_sha256']),
       (Path(c['web_shards'])/'manifest.json',c['web_manifest_sha256']),
       (Path(c['dev_shards'])/'manifest.json',c['dev_manifest_sha256'])]
    for pool in (c['candidate'],c['control_pool']):paths.append((Path(pool['pool'])/'manifest.json',pool['manifest_sha256']))
    assert all(sha256(path)==digest for path,digest in paths)
    return c


def resume_gate(parent,web,short,c,binding,heartbeat,check):
    path=RUN/'resume-gate.json'
    if path.exists():
        r=read_json(path);assert r['passed'] and r['binding']==binding;return r
    states=[];histories=[];verification=0
    b=dict(binding,optimizer_policy='inherit',peak_lr=c['peak_lr'],isolated_batch=256,gate='new-mixture-shuffle')
    for branch in ('continuous','resumed'):
        trainer=NaturalTrainer(parent,web,short,'shuffle',dict(web=100000,short=100000),b);history=[]
        for i in range(4):
            check();history.append(trainer.step())
            if branch=='resumed' and i==1:
                split=RUN/'resume-gate/split.pt';trainer.save(split);del trainer;gc.collect();torch.cuda.empty_cache()
                trainer=NaturalTrainer(parent,web,short,'shuffle',dict(web=100000,short=100000),b);trainer.load(split)
        checkpoint=RUN/'resume-gate'/(branch+'.pt');trainer.save(checkpoint)
        verification+=sum(trainer.sampler.source_teachers.values());histories.append(history)
        states.append(torch.load(checkpoint,map_location='cpu',weights_only=False));del trainer;gc.collect();torch.cuda.empty_cache()
    keys=('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','spec','model_config','pilot_binding','lineage','update')
    checks={k:pilot.equal_state(states[0][k],states[1][k]) for k in keys}
    for k in ('loss','gradient_norm','lr','source_teachers'):
        checks['history_'+k]=[r[k] for r in histories[0]]==[r[k] for r in histories[1]]
    checks['both_sources_active']=all(all(v>0 for v in s['sampler']['source_teachers'].values()) for s in states)
    checks['finite']=all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for h in histories for r in h)
    assert all(checks.values()),checks
    result=dict(binding=binding,passed=True,checks=checks,histories=histories,
        verification_teacher_tokens=verification,optimizer_updates=8)
    write_json(path,result);heartbeat('new-mixture-resume-gate');return result


def structural_evaluation(detail,c,arm,heartbeat,check):
    path=RUN/arm/'structural-evaluation.json'
    if path.exists():
        r=read_json(path);assert r['checkpoint_sha256']==detail['checkpoint_sha256'];return r
    state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
    model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model']);del state
    check();heartbeat(arm+'-structural-dev64')
    body=evaluate_batched(model,Shard(Path(c['candidate']['pool']),'dev'),'cuda','bf16',64,1024,16)
    groups=structural_summary(body,read_json(DATA/'dev64.json'))
    result=dict(checkpoint_sha256=detail['checkpoint_sha256'],dev64_sha256=c['dev64_sha256'],body=body,groups=groups,
        interpretation='Official held-out Web structural likelihoods; EOS_NLL is not free-generation stopping',protected_test_used=False)
    write_json(path,result);del model;gc.collect();torch.cuda.empty_cache();return result


def run(stage):
    c=load_config();path=RUN/('job-'+stage+'.json');previous=read_json(path) if path.exists() else {}
    binding=dict(plan_sha256=sha256(CONFIG),parent=c['parent'],peak_lr=c['peak_lr'],implementation=c['implementation'],source_sha256=c['source_sha256'])
    if previous:
        assert previous['binding']==binding and not alive(previous)
        if previous['status']=='complete':print('Completed stage retained');return
    budget=c['comparison_gpu_budget_seconds' if stage=='compare' else 'expansion_gpu_budget_seconds']
    prior=previous.get('gpu_elapsed_seconds',0);start=[None];stopped=[False]
    job=dict(status='starting',**identity(),binding=binding,started_at=previous.get('started_at',now()),gpu_elapsed_seconds=prior,
        restart_command=f'scripts/run_narrative_comparison.ps1 -Stage {stage}')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; completed update preserved')
        if start[0] is not None and prior+time.monotonic()-start[0]>budget:raise TimeoutError('Frozen GPU budget exhausted')
    def heartbeat(label,**extra):
        check();job.update(stage=label,heartbeat_at=now(),**extra)
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(path,job)
    try:
        heartbeat('setup');seed_all(42);torch.use_deterministic_algorithms(True)
        for relative in (*SOURCES,str(CONFIG.relative_to(ROOT))):
            target=RUN/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        packing.RUN=RUN;packing.PackingTrainer=NaturalTrainer;comparison.RUN=RUN/'evaluation'
        with gpu_lock('cuda'):
            start[0]=time.monotonic();assert sha256(Path(c['parent']['path']))==c['parent']['sha256']
            parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);assert finite_state(parent)
            web=TrainView(c['web_shards'],c['web_manifest_sha256']);tok=Tokenizer(ROOT/c['tokenizer']);dev=Shard(Path(c['dev_shards']),'dev')
            results={};evaluations={};structures={};gate=None
            if stage=='compare':
                gate=resume_gate(parent,web,Shard(Path(c['candidate']['pool']),'train'),c,binding,heartbeat,check)
                arms=[('mixed-control',c['control_pool']),('mixed-diverse',c['candidate'])];goals=c['comparison_goals']
            else:
                assert read_json(RUN/'review.json')['eligible_for_expansion']
                growth=read_json(DATA/'ready-expanded.json');review=read_json(RUN/'expanded-content-review.json')
                assert growth['splits']['train']['documents']>=50000 and growth['splits']['train']['tokens']>=5000000
                assert review['sample_sha256']==growth['sample_sha256'] and review['weak_documents']<=10
                detail=read_json(RUN/'compare-result.json')['checkpoints']['mixed-diverse']
                assert sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256']
                parent=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False);parent['sampler']=parent['sampler']['web']
                binding=dict(binding,growth_parent=detail['checkpoint_sha256'],growth_preparation_sha256=sha256(DATA/'ready-expanded.json'),growth_review_sha256=sha256(RUN/'expanded-content-review.json'))
                arms=[('mixed-expanded',dict(pool=growth['pool'],manifest_sha256=growth['manifest_sha256']))];goals=c['expansion_goals']
            for arm,pool in arms:
                assert sha256(Path(pool['pool'])/'manifest.json')==pool['manifest_sha256']
                b=dict(binding,optimizer_policy='inherit',short_manifest_sha256=pool['manifest_sha256'])
                results[arm]=packing.train(parent,web,Shard(Path(pool['pool']),'train'),c,b,arm,'shuffle',goals,heartbeat,check)
                evaluations[arm]=comparison.evaluate(arm,results[arm],dev,tok,c,results[arm]['binding'],heartbeat,check,start[0]+budget-prior)
                structures[arm]=structural_evaluation(results[arm],c,arm,heartbeat,check)
                write_json(RUN/(stage+'-progress.json'),dict(checkpoints=results,evaluations=evaluations,structures=structures))
            result=dict(status='complete_pending_review',binding=binding,checkpoints=results,evaluations=evaluations,structures=structures,
                scientific_teacher_tokens=sum(r['additional_supervised_tokens'] for r in results.values()),
                scientific_valid_input_tokens=sum(r['additional_input_tokens'] for r in results.values()),
                physical_input_tokens=sum(r['physical_input_tokens'] for r in results.values()),
                verification_teacher_tokens=gate['verification_teacher_tokens'] if gate else 0,
                gpu_seconds=prior+time.monotonic()-start[0],completed_at=now(),protected_test_used=False)
            write_json(RUN/(stage+'-result.json'),result);heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps(dict(stage=stage,scientific_teacher_tokens=result['scientific_teacher_tokens'],GPU_seconds=result['gpu_seconds'])),flush=True)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(path,job)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('freeze','probe','run'),default='probe');parser.add_argument('--stage',choices=('compare','expand'),default='compare');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='freeze':freeze()
    elif args.mode=='probe':load_config();print('Frozen config valid')
    else:run(args.stage)
