"""Plan66: persisted condition-learning diagnostic and conditional mixed100M study."""
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
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.condition_diagnostic import make_pairs, summarize_choice
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.low_lr_pilot import LowLRPilotTrainer
from jmicro.model import JMicroModel
from jmicro.shards import build_shards, Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, seed_all, rng_state
from jmicro.evaluation_memory import bound_evaluation_cache
from phase6_performance import identity, alive, finite_state
import run_eos_short_pilot as pilot
import run_matched_story_study as matched
import run_complete_text_comparison as comparison

RUN = ROOT/'reports/phase6/condition-learning-20261005'
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-learning-20261005-v2')
CONFIG = ROOT/'configs/phase6/condition_learning.json'
SOURCES = ('scripts/run_condition_diagnostic.py','scripts/run_condition_diagnostic.ps1','src/jmicro/condition_diagnostic.py',
           'tests/test_condition_diagnostic.py','docs/66_condition_learning_diagnostic_plan.md')


def prepare():
    if CONFIG.exists():
        load_config(); print('Existing frozen diagnostic retained'); return
    assert not (RUN/'job.json').exists(), 'Do not refreeze after launch'
    suites=list(ET.parse(RUN/'tests.xml').getroot().iter('testsuite'))
    assert sum(int(s.attrib['tests']) for s in suites)>=5
    assert all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped'))
    DATA.mkdir(parents=True,exist_ok=True); RUN.mkdir(parents=True,exist_ok=True)
    base=read_json(ROOT/'configs/phase6/dataset_expansion_1b.json')
    tok=Tokenizer(ROOT/base['tokenizer'])
    assert sha256(ROOT/base['tokenizer'])==base['tokenizer_sha256']
    compact=make_pairs('train',100,[0],202610067)
    expanded=make_pairs('train',500,[0,1,2,3],202610068)
    assert len({r['text'] for r in compact})==len(compact)
    assert len({r['text'] for r in expanded})==len(expanded)
    dev=make_pairs('dev',10,[0,4],202610069)
    all_train={r['text'] for r in compact+expanded}
    assert len(dev)==100 and not all_train & {r['text'] for r in dev}
    protected=[]
    for p in (ROOT/'eval/base.jsonl',ROOT/'eval/japanese_semantics_v2_1.jsonl'):
        for line in p.read_text(encoding='utf-8').splitlines():
            row=json.loads(line)
            protected.extend(v for k,v in row.items() if k in ('prefix','context') and isinstance(v,str) and len(v)>12)
    assert not any(p in r['text'] for p in protected for r in compact+expanded), 'Fixed eval prefix leakage'
    write_json(DATA/'dev.json',dev)
    pools={}
    for arm,rows in [('compact',compact),('expanded',expanded)]:
        corpus=DATA/(arm+'.jsonl')
        corpus.write_text(''.join(json.dumps(dict(r,doc_id=r['id'],kind='web',bucket='authored-condition'),ensure_ascii=False)+'\n' for r in rows),encoding='utf-8')
        directory=DATA/arm
        manifest=build_shards(corpus,ROOT/base['tokenizer'],directory)
        sample=[r for category in ('reference','quantity','negation','time','cause') for r in [x for x in rows if x['category']==category][:20]]
        assert len(sample)==100
        write_json(DATA/(arm+'-train-eval.json'),sample)
        pools[arm]=dict(pool=str(directory),manifest_sha256=sha256(directory/'manifest.json'),
                       unique_tokens=manifest['splits']['train']['tokens'],documents=len(rows),
                       corpus_sha256=sha256(corpus),train_eval_sha256=sha256(DATA/(arm+'-train-eval.json')),
                       mean_body_tokens=(manifest['splits']['train']['tokens']-2*len(rows))/len(rows),
                       EOS_per_1000_tokens=1000*len(rows)/manifest['splits']['train']['tokens'])
    ready=dict(source='Codex-authored closed-world condition templates; not acquired public source',
               pools=pools,dev_documents=len(dev),dev_sha256=sha256(DATA/'dev.json'),
               train_dev_full_text_disjoint=True,dev_names_not_in_train=True,
               structural_dev_template_not_trained=True,fixed_eval_prefixes_not_in_train=True,
               shared_train_documents=len({r['text'] for r in compact}&{r['text'] for r in expanded}),
               limits='Authored mechanistic entailment; no independent human/blind validation; amount, lexical diversity, length and EOS density can differ',
               examples={a:[rows[i*len(rows)//5] for i in range(5)] for a,rows in [('compact',compact),('expanded',expanded)]})
    write_json(DATA/'ready.json',ready);write_json(RUN/'ready.json',ready)
    config={k:copy.deepcopy(base[k]) for k in ('parent','web_shards','web_manifest_sha256','dev_shards','dev_manifest_sha256',
             'tokenizer','tokenizer_sha256','suite_sha256','evaluation','implementation','reference')}
    config.update(version=1,scope='Plan66 stages1–4; diagnostic and conditional100M; stop',
                  pools=pools,dev_sha256=ready['dev_sha256'],ready_sha256=sha256(DATA/'ready.json'),
                  peak_lr=.0001,train_goal=.9,dev_goal=.7,
                  diagnostic_updates=762,diagnostic_tokens_per_arm=24969216,
                  diagnostic_train_budget_seconds=180,mixed_updates=3051,mixed_tokens_per_arm=99975168,
                  mixed_short_updates=610,mixed_train_budget_seconds=300,total_gpu_budget_seconds=1800,
                  source_sha256={p:sha256(ROOT/p) for p in SOURCES},created_at=now(),
                  interpretation='Compact vs expanded authored data changes amount and diversity; mixed study changes source/length/EOS density; no pure quantity causal claim')
    write_json(CONFIG,config)
    print(json.dumps(dict(status='frozen',pools=pools,dev_documents=100)),flush=True)


def load_config():
    c=read_json(CONFIG)
    assert c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}, 'Frozen sources changed'
    assert c['implementation']==implementation_hashes()
    assert sha256(DATA/'ready.json')==c['ready_sha256']
    assert sha256(DATA/'dev.json')==c['dev_sha256']
    for a,p in c['pools'].items():
        assert sha256(Path(p['pool'])/'manifest.json')==p['manifest_sha256']
        assert sha256(DATA/(a+'.jsonl'))==p['corpus_sha256']
        assert sha256(DATA/(a+'-train-eval.json'))==p['train_eval_sha256']
    for path,digest in [(ROOT/c['tokenizer'],c['tokenizer_sha256']),
                        (ROOT/'eval/base.jsonl',c['suite_sha256']),
                        (Path(c['web_shards'])/'manifest.json',c['web_manifest_sha256']),
                        (Path(c['dev_shards'])/'manifest.json',c['dev_manifest_sha256'])]:
        assert sha256(path)==digest
    return c


def evaluate_condition(detail,c,label,heartbeat,check):
    output=RUN/label/'condition-evaluation.json'
    if output.exists():
        result=read_json(output);assert result['checkpoint_sha256']==detail['checkpoint_sha256'];return result
    state=torch.load(detail['checkpoint'],map_location='cpu',weights_only=False)
    model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
    bound_evaluation_cache(model);scorer=NativeLikelihood(model,Tokenizer(ROOT/c['tokenizer']),batch=16)
    before=rng_state();results={}
    train_arm='expanded' if 'expanded' in label or label=='mixed-candidate' else 'compact'
    for split,path in [('train',DATA/(train_arm+'-train-eval.json')),('dev',DATA/'dev.json')]:
        check();heartbeat(label+'-condition-'+split)
        rows=read_json(path);pairs=[(r['prefix'],option) for r in rows for option in r['choices']]
        with sdpa_kernel(SDPBackend.MATH):scores=scorer.score(pairs)
        notes=[]
        for i,r in enumerate(rows):
            values=[scores[2*i+j]['log_likelihood'] for j in (0,1)]
            predicted=0 if values[0]>values[1] else 1 if values[1]>values[0] else None
            correct=predicted==r['label']
            note=dict(r,log_likelihood=values,prediction=predicted,correct=correct,
                      expected_continuation_nll=-values[r['label']],
                      expected_continuation_tokens=scores[2*i+r['label']]['target_tokens'])
            notes.append(note)
        result=dict(summary=summarize_choice(notes),rows=notes)
        result['by_category']={category:summarize_choice([r for r in notes if r['category']==category]) for category in ('reference','quantity','negation','time','cause')}
        if split=='dev':
            result['known_structure']=summarize_choice([r for r in notes if not r['structural_holdout']])
            result['unseen_structure']=summarize_choice([r for r in notes if r['structural_holdout']])
        results[split]=result
    heartbeat(label+'-condition-generation20')
    dev=read_json(DATA/'dev.json');chosen=[]
    for category in ('reference','quantity','negation','time','cause'):
        options=[r for r in dev if r['category']==category]
        chosen.extend(options[:4])
    generated=[]
    for r in chosen:
        check()
        with sdpa_kernel(SDPBackend.MATH):g=scorer.generate(r['prefix'],max_new=48)
        g.update(id=r['id'],category=r['category'],expected=r['choices'][r['label']],alternative=r['choices'][1-r['label']],
                 exact_expected_prefix=g['text'].startswith(r['choices'][r['label']]))
        generated.append(g)
    assert pilot.equal_state(before,rng_state())
    result=dict(checkpoint_sha256=detail['checkpoint_sha256'],checkpoint=detail['checkpoint'],results=results,
                generation=generated,greedy_exact_prefix_correct=sum(r['exact_expected_prefix'] for r in generated),
                diagnostic_pass=results['train']['summary']['accuracy']>=c['train_goal'] and results['dev']['summary']['accuracy']>=c['dev_goal'],
                forward_input_tokens=scorer.forward_tokens,protected_test_used=False,completed_at=now())
    write_json(output,result);del model,state;gc.collect();torch.cuda.empty_cache();return result


def train_configuration(c,arm,mixed=False):
    count=c['mixed_updates'] if mixed else c['diagnostic_updates']
    p=dict(c,stage='condition-mixed' if mixed else 'condition-diagnostic',updates_per_arm=count,
           stable_updates=2898 if mixed else 686,decay_updates=153 if mixed else 76,
           final_update=c['parent']['update']+count,final_tokens=c['parent']['tokens_seen']+count*32768,
           tokens_per_arm=count*32768,midpoint_update=None)
    source=c['pools']['expanded' if 'expanded' in arm or arm=='mixed-candidate' else 'compact']
    if arm=='mixed-control':source=read_json(ROOT/'configs/phase6/dataset_expansion_1b.json')['pool']
    p['arms']={arm:dict(source,short_updates=c['mixed_short_updates'] if mixed else count)}
    return p


def run():
    c=load_config();path=RUN/'job.json';previous=read_json(path) if path.exists() else {}
    binding=dict(plan_sha256=sha256(CONFIG),parent=c['parent'],peak_lr=c['peak_lr'],implementation=c['implementation'])
    if previous:
        assert previous['binding']==binding and not alive(previous), 'Existing actual job or different frozen run'
        if previous['status']=='complete':print('Completed job retained');return
    prior=previous.get('gpu_elapsed_seconds',0);started=None;stopped=[False]
    job=dict(status='starting',**identity(),binding=binding,started_at=previous.get('started_at',now()),gpu_elapsed_seconds=prior,
             restart_command='uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_condition_diagnostic.py --mode run')
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; retain completed updates')
        if started is not None and prior+time.monotonic()-started>c['total_gpu_budget_seconds']:raise TimeoutError('Frozen cumulative GPU budget exhausted')
    def heartbeat(stage,**extra):
        check();job.update(stage=stage,heartbeat_at=now(),**extra)
        if started is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started
        atomic_json(path,job)
    try:
        heartbeat('setup')
        for relative in (*SOURCES,str(CONFIG.relative_to(ROOT))):
            target=RUN/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        seed_all(42);torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            started=time.monotonic()
            assert sha256(Path(c['parent']['path']))==c['parent']['sha256']
            parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);assert finite_state(parent)
            assert parent['tokens']==c['parent']['tokens_seen'] and parent['update']==c['parent']['update']
            web=TrainView(c['web_shards'],c['web_manifest_sha256'])
            pools={a:TrainView(p['pool'],p['manifest_sha256'],check_stream=True) for a,p in c['pools'].items()}
            pilot.PilotTrainer=LowLRPilotTrainer
            heartbeat('resume-gate');gate=pilot.exact_gate(parent,web,pools['compact'],binding,RUN,check)
            results={};conditions={};evaluations={}
            parent_detail=dict(checkpoint=c['parent']['path'],checkpoint_sha256=c['parent']['sha256'])
            conditions['parent']=evaluate_condition(parent_detail,c,'parent',heartbeat,check)
            for arm in ('compact','expanded'):
                p=train_configuration(c,arm);arm_binding=dict(binding,arm=arm,short_manifest_sha256=c['pools'][arm]['manifest_sha256'])
                arm_started=time.monotonic()
                arm_prior=read_json(RUN/arm/'progress.json').get('training_seconds',0) if (RUN/arm/'progress.json').exists() else 0
                def train_check():
                    check()
                    if arm_prior+time.monotonic()-arm_started>c['diagnostic_train_budget_seconds']:raise TimeoutError(arm+' cumulative training budget exhausted')
                results[arm]=matched.train(RUN,arm,parent,web,pools[arm],p,arm_binding,heartbeat,train_check)
                conditions[arm]=evaluate_condition(results[arm],c,arm,heartbeat,check)
                write_json(RUN/'diagnostic-progress.json',dict(checkpoints=results,conditions=conditions))
                summary=conditions[arm]['results']
                print(json.dumps(dict(arm=arm,train=summary['train']['summary'],dev=summary['dev']['summary'],pass_goal=conditions[arm]['diagnostic_pass'])),flush=True)
            eligible=any(conditions[a]['diagnostic_pass'] for a in ('compact','expanded'))
            write_json(RUN/'diagnostic-judgment.json',dict(eligible_for_mixed100m=eligible,conditions={a:conditions[a]['diagnostic_pass'] for a in ('compact','expanded')},
                explanation='Frozen train90/dev70 diagnostic goals; not Base adoption',completed_at=now()))
            if eligible:
                for arm in ('mixed-control','mixed-candidate'):
                    p=train_configuration(c,arm,True);ref=p['arms'][arm]
                    pool=TrainView(ref['pool'],ref['manifest_sha256'],check_stream=True)
                    arm_binding=dict(binding,arm=arm,short_manifest_sha256=ref['manifest_sha256'])
                    arm_started=time.monotonic()
                    arm_prior=read_json(RUN/arm/'progress.json').get('training_seconds',0) if (RUN/arm/'progress.json').exists() else 0
                    def mixed_check():
                        check()
                        if arm_prior+time.monotonic()-arm_started>c['mixed_train_budget_seconds']:raise TimeoutError(arm+' cumulative training budget exhausted')
                    results[arm]=matched.train(RUN,arm,parent,web,pool,p,arm_binding,heartbeat,mixed_check)
                    conditions[arm]=evaluate_condition(results[arm],c,arm,heartbeat,check)
            dev=Shard(Path(c['dev_shards']),'dev');tok=Tokenizer(ROOT/c['tokenizer']);comparison.RUN=RUN/'evaluation'
            for arm,detail in results.items():
                heartbeat(arm+'-japanese-evaluation')
                evaluations[arm]=comparison.evaluate(arm,detail,dev,tok,c,detail['binding'],heartbeat,check,started+c['total_gpu_budget_seconds']-prior)
            result=dict(status='complete_pending_content_review',binding=binding,checkpoints=results,conditions=conditions,evaluations=evaluations,
                        mixed100m_executed=eligible,scientific_tokens=sum(d['additional_input_tokens'] for d in results.values()),verification_tokens=gate['input_tokens'],
                        resume_gate=gate,unique_pools=c['pools'],interpretation=c['interpretation'],GPU_seconds=prior+time.monotonic()-started,
                        protected_test_used=False,completed_at=now())
            write_json(RUN/'result.json',result);heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps(dict(status=result['status'],scientific_tokens=result['scientific_tokens'],GPU_seconds=result['GPU_seconds'])),flush=True)
    except BaseException as error:
        job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        if started is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started
        atomic_json(path,job)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('prepare','probe','run'),default='probe');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='prepare':prepare()
    elif args.mode=='probe':
        load_config()
        if (RUN/'job.json').exists():assert not alive(read_json(RUN/'job.json'))
        print('Frozen diagnostic valid; no actual duplicate job')
    else:run()
