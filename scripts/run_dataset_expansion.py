"""Plan58: frozen paired1B training, Japanese diagnostics, gated full evaluation."""
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
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
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
import run_matched_story_study as matched
import run_complete_text_comparison as comparison
import run_eos_short_pilot as pilot
import run_story20_budget as original
from probe_dataset_expansion_supply import DATA

RUN=ROOT/'reports/phase6/dataset-expansion-1b-20261005'
CONFIG=ROOT/'configs/phase6/dataset_expansion_1b.json'
SCHEMA=ROOT/'schemas/configs/phase6/dataset_expansion_1b.schema.json'
SOURCES=tuple(dict.fromkeys(('scripts/run_dataset_expansion.py','scripts/run_dataset_expansion.ps1',
    'scripts/review_dataset_expansion.py','scripts/review_dataset_expansion_data.py','scripts/prepare_dataset_expansion.py',
    'scripts/probe_dataset_expansion_supply.py','scripts/inspect_dataset_expansion_source.py',
    'src/jmicro/expanded_stories.py','tests/test_expanded_stories.py','tests/test_dataset_expansion_budget.py',*matched.SOURCES)))

def settings():
    return dict(stage='content',updates_per_arm=30518,stable_updates=29000,decay_updates=1518,
        tokens_per_update=32768,tokens_per_arm=1000013824,scientific_total_tokens=2000027648,
        final_update=335694,final_tokens=11000020992,midpoint_update=320435,
        screen_gpu_budget_seconds=4800,full_gpu_budget_seconds=1800,total_GPU_budget_seconds=6600)

def freeze():
    assert not (RUN/'screen-job.json').exists(),'Started config immutable'
    base=original.load_config();ready=read_json(DATA/'shards/ready.json');content=read_json(DATA/'content-review.json')
    assert ready['totals']['tokens']>=200000000 and ready['new_source_tokens']>=140000000
    assert ready['source_train_only'] and ready['whole_original_documents'] and not ready['official_validation_test_acquired']
    assert content['accepted_for_experiment'] and content['ready_sha256']==sha256(DATA/'shards/ready.json')
    assert content['manifest_sha256']==sha256(DATA/'shards/manifest.json')==ready['manifest_sha256']
    assert content['samples_sha256']==sha256(DATA/'shards/samples.json') and len(content['notes'])==40
    suites=list(ET.parse(RUN/'tests.xml').getroot().iter('testsuite'))
    assert sum(int(s.attrib['tests']) for s in suites)>=5 and all(int(s.attrib[k])==0 for s in suites for k in ('errors','failures','skipped'))
    c=copy.deepcopy(base);c.update(settings());c.update(scope='Authorized plan58 stages1–3; dataset expansion paired1B and stop',
        output=str(RUN.relative_to(ROOT)),arms=dict(control=dict(base['pool'],short_updates=6102),
            refined=dict(pool=str(DATA/'shards'),manifest_sha256=ready['manifest_sha256'],short_updates=6102)),selection=None,
        pool_ready=dict(path=str(DATA/'shards/ready.json'),sha256=sha256(DATA/'shards/ready.json')),
        pool_content=dict(path=str(DATA/'content-review.json'),sha256=sha256(DATA/'content-review.json')),
        comparison_interpretation='Amount plus new translated-story source/length/EOS density; not a pure amount-only causal estimate',
        actual_data=dict(old_pool_tokens=59963449,new_pool_tokens=ready['totals']['tokens'],new_source_tokens=ready['new_source_tokens'],
            retained_source_tokens=ready['copied_old_tokens'],body_tokens_mean=ready['body_tokens_mean'],old_body_tokens_mean=ready['old_body_tokens_mean'],
            EOS_per_1000_tokens=ready['EOS_per_1000_tokens'],old_EOS_per_1000_tokens=ready['old_EOS_per_1000_tokens'],
            length_and_EOS_density_within5percent=ready['length_and_EOS_density_within5percent']),
        tests_sha256=sha256(RUN/'tests.xml'),source_sha256={p:sha256(ROOT/p) for p in SOURCES},created_at=now())
    c['reference']={k:base['reference'][k] for k in ('parent_body','parent_generation')}
    for label,path in {'web_screen':original.RUN/'evaluation/result/web/evaluation/result.json',
        'story_screen':original.RUN/'evaluation/result/coherent20/evaluation/result.json',
        'web_full':original.RUN/'full/web-full.json','story_full':original.RUN/'full/coherent20-full.json'}.items():
        c['reference'][label]=dict(path=str(path),sha256=sha256(path))
    for k in ('entry_full_review','previous_failed_screen','intermediate_update','intermediate_tokens','intermediate_additional_tokens','new_improvement_gates'):
        c.pop(k,None)
    write_json(CONFIG,c);write_json(SCHEMA,dict(type='object',additionalProperties=False,required=list(c),properties={k:{'const':v} for k,v in c.items()}))
    print(json.dumps(dict(status='frozen',settings=settings(),data=c['actual_data'])),flush=True)

def load_config():
    c=read_json(CONFIG);validate(c,read_json(SCHEMA))
    assert c['implementation']==implementation_hashes() and c['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES}
    for ref in (*c['reference'].values(),c['pool_ready'],c['pool_content']):assert sha256(Path(ref['path']))==ref['sha256']
    assert sha256(RUN/'tests.xml')==c['tests_sha256']
    for path,digest in ((ROOT/c['tokenizer'],c['tokenizer_sha256']),(ROOT/'eval/base.jsonl',c['suite_sha256']),
        (Path(c['web_shards'])/'manifest.json',c['web_manifest_sha256']),(Path(c['dev_shards'])/'manifest.json',c['dev_manifest_sha256']),
        (ROOT/c['evaluation']['config'],c['evaluation']['config_sha256']),(ROOT/c['evaluation']['semantic_suite'],c['evaluation']['semantic_sha256']),
        (Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'),c['evaluation']['data_manifest_sha256'])):assert sha256(path)==digest
    for ref in c['arms'].values():assert sha256(Path(ref['pool'])/'manifest.json')==ref['manifest_sha256']
    return c

def probe():
    load_config()
    for path in (RUN/'screen-job.json',RUN/'full/full-job.json'):
        if path.exists():assert not alive(read_json(path)),'Actual scientific job still live'
    print('Frozen plan58 valid; no actual duplicate job',flush=True)

def run_gpu(mode):
    c=load_config();output=RUN if mode=='screen' else RUN/'full';output.mkdir(parents=True,exist_ok=True)
    binding=dict(plan_sha256=sha256(CONFIG),parent=c['parent'],implementation=c['implementation'],source_sha256=c['source_sha256'],peak_lr=c['peak_lr'],stage='expansion')
    if mode=='full':
        assert read_json(RUN/'review.json')['eligible_for_full'];binding['review_sha256']=sha256(RUN/'review.json')
    path=output/(mode+'-job.json');previous=read_json(path) if path.exists() else {}
    if previous:
        assert previous['binding']==binding and not alive(previous),'Actual live or different job'
        if previous['status']=='complete':print('Reuse completed GPU stage');return
    prior=previous.get('gpu_elapsed_seconds',0);started=[None];stopped=[False];budget=c[mode+'_gpu_budget_seconds']
    job=dict(status='starting',**identity(),binding=binding,started_at=previous.get('started_at',now()),gpu_elapsed_seconds=prior,
        restart_command='scripts/run_dataset_expansion.ps1 -Mode '+mode)
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; completed updates retained')
        if started[0] is not None and prior+time.monotonic()-started[0]>budget:raise TimeoutError('Frozen cumulative GPU budget exhausted')
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
        seed_all(42);torch.use_deterministic_algorithms(True)
        with gpu_lock('cuda'):
            started[0]=time.monotonic();deadline=started[0]+budget-prior
            if mode=='screen':
                assert sha256(Path(c['parent']['path']))==c['parent']['sha256']
                parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);assert finite_state(parent)
                web=TrainView(c['web_shards'],c['web_manifest_sha256'])
                pools={a:TrainView(ref['pool'],ref['manifest_sha256'],check_stream=True) for a,ref in c['arms'].items()}
                pilot.PilotTrainer=LowLRPilotTrainer;heartbeat('resume-gate')
                gate=pilot.exact_gate(parent,web,pools['refined'],binding,RUN,check)
                trained={a:matched.train(RUN,a,parent,web,pool,c,dict(binding,arm=a,short_manifest_sha256=c['arms'][a]['manifest_sha256']),heartbeat,check) for a,pool in pools.items()}
                dev=Shard(Path(c['dev_shards']),'dev');tok=Tokenizer(ROOT/c['tokenizer']);comparison.RUN=RUN/'evaluation'
                evaluated={a:comparison.evaluate(a,detail,dev,tok,c,detail['binding'],heartbeat,check,deadline) for a,detail in trained.items()}
                result=dict(status='complete_pending_content_review',binding=binding,arms=trained,checkpoints=trained,evaluations=evaluated,
                    scientific_tokens=sum(d['additional_input_tokens'] for d in trained.values()),verification_tokens=gate['input_tokens'],resume_gate=gate,
                    actual_data=c['actual_data'],comparison_interpretation=c['comparison_interpretation'],protected_test_used=False)
                assert result['scientific_tokens']==c['scientific_total_tokens']
            else:
                result=matched.full_evaluation(RUN,c,read_json(RUN/'result.json'),binding,heartbeat,check,deadline)
            result.update(GPU_seconds=prior+time.monotonic()-started[0],completed_at=now());write_json(output/'result.json',result)
            heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps(dict(status=result['status'],GPU_seconds=result['GPU_seconds'])),flush=True)
    except BaseException as error:
        job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(path,job)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--mode',choices=('freeze','probe','screen','full'),default='screen');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.mode=='freeze':freeze()
    elif args.mode=='probe':probe()
    else:run_gpu(args.mode)
