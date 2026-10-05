"""Plan73: persistent natural memorization, two-arm comparison and gated growth."""
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
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.natural_learning import material,NaturalTrainer
from jmicro.model import JMicroModel
from jmicro.shards import Shard,build_shards
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,implementation_hashes,seed_all,isolated_evaluation
from phase6_performance import identity,alive,finite_state
import run_packing_study as packing
import run_complete_text_comparison as comparison
import run_eos_short_pilot as pilot
from run_root_cause_diagnostic import teacher,generate

RUN=ROOT/'reports/phase6/natural-learning-20261005'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/natural-learning-20261005')
CONFIG=ROOT/'configs/phase6/natural_learning.json'
SOURCES=('scripts/run_natural_learning.py','scripts/run_natural_learning.ps1','src/jmicro/natural_learning.py',
    'tests/test_natural_learning.py','docs/73_natural_learning_execution.md','src/jmicro/packing_study.py',
    'scripts/run_packing_study.py','scripts/run_root_cause_diagnostic.py','scripts/run_complete_text_comparison.py',
    'src/jmicro/eos_pilot.py','src/jmicro/low_lr_pilot.py','src/jmicro/tokenizer.py',
    'src/jmicro/japanese_evaluation.py','src/jmicro/evaluation_memory.py')


def prepare():
    if CONFIG.exists():load_config();print('Frozen preparation retained');return
    assert not (RUN/'job-diagnostic.json').exists()
    base=read_json(ROOT/'configs/phase6/packing_study.json')
    DATA.mkdir(parents=True,exist_ok=True);RUN.mkdir(parents=True,exist_ok=True)
    tok=Tokenizer(ROOT/base['tokenizer']);assert sha256(tok.path)==base['tokenizer_sha256']
    natural=material('train',1000);memory=natural[:64];dev=material('dev',128)
    expanded=natural+material('expanded',8192)
    train_text={r['text'] for r in expanded}
    assert len(train_text)==9192 and not train_text&{r['text'] for r in dev}
    protected=[]
    for p in (ROOT/'eval/base.jsonl',ROOT/'eval/japanese_semantics_v2_1.jsonl'):
        for line in p.read_text().splitlines():
            r=json.loads(line);protected.extend(v for k,v in r.items() if k in ('prefix','context') and isinstance(v,str) and len(v)>12)
    assert not any(p in r['text'] for p in protected for r in expanded)
    for records in (expanded,dev):
        for row in records:
            assert tok.decode(tok.encode(row['text']))==row['text']
            assert len(tok.encode(row['text']))+1<=128
            assert tok.encode(row['text'])[:len(tok.encode(row['prefix']))]==tok.encode(row['prefix'])
    pools={}
    for label,rows in [('memory64',memory),('natural1000',natural),('expanded9192',expanded)]:
        corpus=DATA/(label+'.jsonl');corpus.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
        manifest=build_shards(corpus,tok.path,DATA/label)
        pools[label]=dict(pool=str(DATA/label),manifest_sha256=sha256(DATA/label/'manifest.json'),
            documents=len(rows),unique_tokens=manifest['splits']['train']['tokens'],corpus_sha256=sha256(corpus))
    for label,rows in [('train64',memory),('dev128',dev)]:write_json(DATA/(label+'.json'),rows)
    c={k:copy.deepcopy(base[k]) for k in ('parent','web_shards','web_manifest_sha256','dev_shards','dev_manifest_sha256',
        'tokenizer','tokenizer_sha256','suite_sha256','evaluation','reference','peak_lr')}
    c.update(pools=pools,control_pool=base['pool'],implementation=implementation_hashes(),
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},created_at=now(),
        train64_sha256=sha256(DATA/'train64.json'),dev128_sha256=sha256(DATA/'dev128.json'),
        diagnostic_train_budget_seconds=600,mixed_train_budget_seconds=600,total_gpu_budget_seconds=1200,
        isolated_batch=256,diagnostic_teacher_tokens=8000000,comparison_teacher_tokens=25000000,
        expansion_teacher_tokens=100000000,diagnostic_gpu_budget_seconds=600,comparison_gpu_budget_seconds=1200,
        expansion_gpu_budget_seconds=1200,memorization_goal=.9,new_init_peak_lr=.001,
        selection='Passing maximum exact EOS gold, then teacher accuracy, then inherit; C only if neither A/B passes',
        scope='authorized four stages; stop at failed prerequisite or final bounded growth; no20B/Chat/test/push',
        preparation_content_review='Codex reviewed32 concrete everyday action/outcome templates and64 memory instances, not blind human certification',
        source_length_EOS_confounded=True,precision_contract_failures_preserved='result72 seven numeric failures unchanged')
    write_json(CONFIG,c);write_json(RUN/'ready.json',dict(config_sha256=sha256(CONFIG),pools=pools,
        train64=memory,heldout_documents=128,all_expanded_train_disjoint_dev=True,
        maximum_input_tokens=max(len(tok.encode(r['text']))+1 for r in expanded),protected_test_used=False))
    print(json.dumps(dict(status='prepared',pools=pools)),flush=True)


def load_config():
    c=read_json(CONFIG)
    assert c['implementation']==implementation_hashes()
    assert c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    assert sha256(DATA/'train64.json')==c['train64_sha256'] and sha256(DATA/'dev128.json')==c['dev128_sha256']
    for entry in c['pools'].values():assert sha256(Path(entry['pool'])/'manifest.json')==entry['manifest_sha256']
    return c


def evaluate_memory(detail,c,arm,heartbeat,check):
    path=RUN/arm/'memory-evaluation.json'
    if path.exists():
        result=read_json(path);assert result['checkpoint_sha256']==detail['checkpoint_sha256'];return result
    state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
    model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model']);del state
    tok=Tokenizer(ROOT/c['tokenizer']);results={}
    with isolated_evaluation(model):
        for split,file in [('train',DATA/'train64.json'),('dev',DATA/'dev128.json')]:
            check();heartbeat(arm+'-'+split+'-natural')
            rows=read_json(file);cases=[]
            for row in rows:
                body,prefix=tok.encode(row['text']),tok.encode(row['prefix'])
                cases.append(dict(row,source=split,body_ids=body,prefix_ids=[2,*prefix],gold_ids=[*body[len(prefix):],3]))
            t=teacher(model,cases);g=generate(model,cases,tok,None,64)
            assert len(t)==len(g)==len(rows)
            targets=sum(len(r['gold_ids']) for r in cases)
            correct=sum(sum(s['target_rank']==1 for s in row['teacher_steps']) for row in t)
            exact=sum(row['exact_gold'] for row in g);eos=sum(row['stop_reason']=='eos' for row in g)
            results[split]=dict(summary=dict(documents=len(rows),teacher_targets=targets,teacher_correct=correct,
                teacher_accuracy=correct/targets,exact_gold=exact,exact_fraction=exact/len(rows),
                eos=eos,appropriate_gold_eos=exact,appropriate_fraction=exact/len(rows)),teacher=t,generation=g)
    summary=results['train']['summary'];goal=c['memorization_goal']
    result=dict(checkpoint_sha256=detail['checkpoint_sha256'],results=results,
        passed=summary['teacher_accuracy']>=goal and summary['exact_fraction']>=goal and summary['appropriate_fraction']>=goal,
        goal=goal,interpretation='train memorization threshold; heldout distinct128 is diagnostic, not Base quality gate',completed_at=now())
    write_json(path,result);print(json.dumps(dict(arm=arm,passed=result['passed'],train=summary,dev=results['dev']['summary'])),flush=True)
    del model;gc.collect();torch.cuda.empty_cache();return result


def resume_gate(parent,web,short,c,binding,heartbeat,check):
    path=RUN/'resume-gate.json'
    if path.exists():r=read_json(path);assert r['passed'] and r['binding']==binding;return r
    results={};verification=0
    for policy in ('inherit','fresh'):
        states=[];histories=[]
        for branch in ('continuous','resumed'):
            b=dict(binding,optimizer_policy=policy,peak_lr=c['peak_lr'],isolated_batch=256,gate=policy)
            trainer=NaturalTrainer(parent,web,short,'isolated',dict(web=0,short=200000),b);history=[]
            for i in range(4):
                check();history.append(trainer.step())
                if branch=='resumed' and i==1:
                    split=RUN/'resume-gate'/policy/'split.pt';trainer.save(split);del trainer;gc.collect();torch.cuda.empty_cache()
                    trainer=NaturalTrainer(parent,web,short,'isolated',dict(web=0,short=200000),b);trainer.load(split)
            checkpoint=RUN/'resume-gate'/policy/(branch+'.pt');trainer.save(checkpoint)
            verification+=sum(trainer.sampler.source_teachers.values());histories.append(history)
            states.append(torch.load(checkpoint,map_location='cpu',weights_only=False));del trainer;gc.collect();torch.cuda.empty_cache()
        keys=('model','optimizer','scheduler','rng','sampler','tokens','supervised_tokens','body_bytes','token_digest','spec','model_config','pilot_binding','lineage','update')
        checks={k:pilot.equal_state(states[0][k],states[1][k]) for k in keys}
        for k in ('loss','gradient_norm','lr','source_teachers'):checks['history_'+k]=[r[k] for r in histories[0]]==[r[k] for r in histories[1]]
        assert all(checks.values()),checks
        assert all(math.isfinite(r['loss']) and math.isfinite(r['gradient_norm']) for h in histories for r in h)
        results[policy]=dict(checks=checks,passed=True,histories=histories);del states
        heartbeat('resume-'+policy)
    result=dict(binding=binding,passed=True,arms=results,verification_teacher_tokens=verification,optimizer_updates=16)
    write_json(path,result);return result


def run(stage):
    c=load_config();path=RUN/('job-'+stage+'.json');previous=read_json(path) if path.exists() else {}
    binding=dict(plan_sha256=sha256(CONFIG),parent=c['parent'],peak_lr=c['peak_lr'],implementation=c['implementation'],source_sha256=c['source_sha256'])
    if previous:
        assert previous['binding']==binding and not alive(previous)
        if previous['status']=='complete':print('Completed stage retained');return
    budget=c[{'diagnostic':'diagnostic_gpu_budget_seconds','compare':'comparison_gpu_budget_seconds','expand':'expansion_gpu_budget_seconds'}[stage]]
    prior=previous.get('gpu_elapsed_seconds',0);start=[None];stopped=[False]
    job=dict(status='starting',**identity(),binding=binding,started_at=previous.get('started_at',now()),gpu_elapsed_seconds=prior,
        restart_command=f'scripts/run_natural_learning.ps1 -Stage {stage}')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; preserve completed update')
        if start[0] is not None and prior+time.monotonic()-start[0]>budget:raise TimeoutError('Frozen '+stage+' GPU budget exhausted')
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
            web=TrainView(c['web_shards'],c['web_manifest_sha256']);tok=Tokenizer(ROOT/c['tokenizer'])
            results={};conditions={};evaluations={}
            if stage=='diagnostic':
                short=Shard(Path(c['pools']['memory64']['pool']),'train')
                gate=resume_gate(parent,web,short,c,binding,heartbeat,check)
                for arm,policy in [('adam-inherit','inherit'),('adam-fresh','fresh')]:
                    b=dict(binding,optimizer_policy=policy)
                    results[arm]=packing.train(parent,web,short,c,b,arm,'isolated',dict(web=0,short=8000000),heartbeat,check)
                    conditions[arm]=evaluate_memory(results[arm],c,arm,heartbeat,check)
                    write_json(RUN/'diagnostic-progress.json',dict(checkpoints=results,conditions=conditions))
                eligible=[arm for arm in results if conditions[arm]['passed']]
                if not eligible:
                    seed_all(42);cold=copy.copy(parent);cold['model']=JMicroModel(parent['model_config']).state_dict()
                    cc=dict(c,peak_lr=c['new_init_peak_lr']);arm='new-init';b=dict(binding,optimizer_policy='fresh',initialization='new-random',peak_lr=cc['peak_lr'])
                    results[arm]=packing.train(cold,web,short,cc,b,arm,'isolated',dict(web=0,short=8000000),heartbeat,check)
                    conditions[arm]=evaluate_memory(results[arm],c,arm,heartbeat,check)
                    # A fresh model is a positive control, not permission to replace the10B parent in the equal-content experiment.
                selected=max(eligible,key=lambda a:(conditions[a]['results']['train']['summary']['exact_fraction'],conditions[a]['results']['train']['summary']['teacher_accuracy'],a=='adam-inherit')) if eligible else None
                selection=dict(selected=selected,optimizer_policy='fresh' if selected=='adam-fresh' else 'inherit' if selected else None,
                    prerequisite_met=bool(selected),new_init_positive_control=conditions.get('new-init'),rule=c['selection'])
                write_json(RUN/'selection.json',selection)
            else:
                selection=read_json(RUN/'selection.json');assert selection['prerequisite_met']
                policy=selection['optimizer_policy'];dev=Shard(Path(c['dev_shards']),'dev')
                if stage=='compare':
                    arms=[('mixed-control',c['control_pool']),('mixed-natural',c['pools']['natural1000'])]
                    goals=dict(web=20000000,short=5000000)
                else:
                    judgment=read_json(RUN/'review.json');assert judgment['eligible_for_expansion']
                    comparison_result=read_json(RUN/'compare-result.json');detail=comparison_result['checkpoints']['mixed-natural']
                    assert sha256(Path(detail['checkpoint']))==detail['checkpoint_sha256']
                    parent=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
                    # Fork from a mixture terminus: its Web cursor is nested in the saved sampler.
                    parent['sampler']=parent['sampler']['web'];binding=dict(binding,growth_parent=detail['checkpoint_sha256'])
                    policy='inherit';arms=[('mixed-expanded',c['pools']['expanded9192'])];goals=dict(web=80000000,short=20000000)
                for arm,pool in arms:
                    short=Shard(Path(pool['pool']),'train');b=dict(binding,optimizer_policy=policy,short_manifest_sha256=pool['manifest_sha256'])
                    results[arm]=packing.train(parent,web,short,c,b,arm,'shuffle',goals,heartbeat,check)
                    conditions[arm]=evaluate_memory(results[arm],c,arm,heartbeat,check)
                    evaluations[arm]=comparison.evaluate(arm,results[arm],dev,tok,c,results[arm]['binding'],heartbeat,check,start[0]+budget-prior)
                    write_json(RUN/(stage+'-progress.json'),dict(checkpoints=results,conditions=conditions,evaluations=evaluations))
            result=dict(status='complete_pending_review',binding=binding,checkpoints=results,conditions=conditions,evaluations=evaluations,
                selected=selection.get('selected'),scientific_teacher_tokens=sum(r['additional_supervised_tokens'] for r in results.values()),
                scientific_valid_input_tokens=sum(r['additional_input_tokens'] for r in results.values()),
                physical_input_tokens=sum(r['physical_input_tokens'] for r in results.values()),
                verification_teacher_tokens=gate['verification_teacher_tokens'] if stage=='diagnostic' else 0,
                gpu_seconds=prior+time.monotonic()-start[0],completed_at=now(),protected_test_used=False)
            write_json(RUN/(stage+'-result.json'),result);heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps(dict(stage=stage,selected=result['selected'],scientific_teacher_tokens=result['scientific_teacher_tokens'],GPU_seconds=result['gpu_seconds'])),flush=True)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if start[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-start[0]
        atomic_json(path,job)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('prepare','probe','run'),default='probe');parser.add_argument('--stage',choices=('diagnostic','compare','expand'),default='diagnostic');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='prepare':prepare()
    elif args.mode=='probe':load_config();print('Frozen config valid')
    else:run(args.stage)
