"""Conditional full evaluation of the screened candidate and matched control; no learning."""
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
from jmicro.training import atomic_json,gpu_lock,seed_all,rng_state,implementation_hashes
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.evaluation_memory import bound_evaluation_cache
from jmicro.japanese_evaluation import NativeLikelihood
from phase6_performance import identity,alive
from run_complete_text_comparison import RUN,PLAN
from run_eos_5b_finish import evaluate
from run_eos_complete_100m import adoption_checks
from run_eos_short_pilot import equal_state
from evaluate_japanese_base import evaluate_long
from compare_base_10b import require_alignment,growth_checks
from compare_base_5b import summarize

CONFIG=ROOT/'configs/phase6/complete_text_10b_full.json'
OUTPUT=RUN/'conditional-full'
SOURCES=('scripts/evaluate_complete_text_full.py','scripts/evaluate_complete_text_full.ps1',
 'scripts/run_eos_5b_finish.py','scripts/compare_base_10b.py','scripts/compare_base_5b.py',
 'scripts/run_eos_complete_100m.py','scripts/evaluate_japanese_base.py',
 'src/jmicro/japanese_evaluation.py','src/jmicro/evaluation_memory.py','src/jmicro/readiness.py')

def selected_candidate(review):
    assert review['status']=='passed' and all(review['checks'].values())
    eligible=[a for a,c in review['candidate_checks'].items() if c['eligible_for_conditional_full']]
    assert len(eligible)==1,'Only a single fully eligible screened candidate is authorized here'
    return eligible[0]

def freeze():
    assert not (OUTPUT/'job.json').exists(),'Do not refreeze a started evaluation'
    plan=read_json(PLAN); review=read_json(RUN/'review.json'); screen=read_json(RUN/'result.json')
    candidate=selected_candidate(review)
    parent=ROOT/'reports/phase6/base-10b-comparison-20261004'
    config=dict(version=1,scope='Conditional evaluation within stages1–3; no additional training',
      primary_config_sha256=sha256(PLAN),review_sha256=sha256(RUN/'review.json'),
      arms={a:{'checkpoint':screen['arms'][a]['checkpoint'],'sha256':screen['arms'][a]['checkpoint_sha256']} for a in ('web',candidate)},
      candidate=candidate,output=str(OUTPUT.relative_to(ROOT)),gpu_budget_seconds=plan['conditional_full_evaluation_budget_seconds'],
      dev_shards=plan['dev_shards'],dev_manifest_sha256=plan['dev_manifest_sha256'],
      tokenizer=plan['tokenizer'],tokenizer_sha256=plan['tokenizer_sha256'],suite_sha256=plan['suite_sha256'],
      long_config=plan['evaluation']['config'],long_config_sha256=plan['evaluation']['config_sha256'],
      parent_body={'path':str(parent/'full-dev.json'),'sha256':sha256(parent/'full-dev.json')},
      parent_generation={'path':str(parent/'generation.json'),'sha256':sha256(parent/'generation.json')},
      implementation=implementation_hashes(),source_sha256={p:sha256(ROOT/p) for p in SOURCES},
      rules={'maximum_candidate_control_full_BPB_ratio':1.01,'maximum_candidate_parent_BPB_regression':.001,
             'fixed_repetition_increase_must_be_less_than':8,'all400_raw_failures_zero':True},
      protected_test_used=False,created_at=now())
    write_json(CONFIG,config)
    write_json(ROOT/'schemas/configs/phase6/complete_text_10b_full.schema.json',
      dict(type='object',additionalProperties=False,required=list(config),properties={k:{'const':v} for k,v in config.items()}))
    print('Conditional full protocol frozen; zero additional learning',flush=True)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--freeze',action='store_true');args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7);torch.set_num_threads(2)
    if args.freeze:freeze();return
    config=read_json(CONFIG);validate(config,read_json(ROOT/'schemas/configs/phase6/complete_text_10b_full.schema.json'))
    assert sha256(PLAN)==config['primary_config_sha256'] and sha256(RUN/'review.json')==config['review_sha256']
    assert selected_candidate(read_json(RUN/'review.json'))==config['candidate']
    assert config['source_sha256']=={p:sha256(ROOT/p) for p in SOURCES} and config['implementation']==implementation_hashes()
    for p,d in [(ROOT/config['tokenizer'],config['tokenizer_sha256']),(ROOT/'eval/base.jsonl',config['suite_sha256']),
                (Path(config['dev_shards'])/'manifest.json',config['dev_manifest_sha256']),
                (ROOT/config['long_config'],config['long_config_sha256'])]:assert sha256(p)==d
    for value in (*config['arms'].values(),config['parent_body'],config['parent_generation']):
        assert sha256(Path(value.get('checkpoint',value.get('path'))))==value['sha256']
    binding={'config_sha256':sha256(CONFIG),'source_sha256':config['source_sha256']}
    OUTPUT.mkdir(parents=True,exist_ok=True);job_path=OUTPUT/'job.json'
    old=read_json(job_path) if job_path.exists() else {}
    if old:
        assert not alive(old),'Actual job is still live'
        assert old['binding']==binding
        if old['status']=='complete':print('Reuse completed conditional evaluation');return
    prior=old.get('gpu_elapsed_seconds',0);started=[None];stopped=[False]
    job=dict(status='running',**identity(),binding=binding,started_at=old.get('started_at',now()),
             gpu_elapsed_seconds=prior,restart_command='scripts/evaluate_complete_text_full.ps1',additional_training_tokens=0)
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Evaluation interrupted; completed stages retained')
        if started[0] is not None and prior+time.monotonic()-started[0]>config['gpu_budget_seconds']:
            raise TimeoutError('Cumulative conditional evaluation budget exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(job_path,job)
    try:
        heartbeat('setup')
        for relative in (*SOURCES,str(CONFIG.relative_to(ROOT))):
            dest=OUTPUT/'source'/relative;dest.parent.mkdir(parents=True,exist_ok=True)
            if dest.exists():assert dest.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,dest)
        seed_all(42);torch.use_deterministic_algorithms(True)
        dev=Shard(Path(config['dev_shards']),'dev');tok=Tokenizer(ROOT/config['tokenizer'])
        full,long={},{}
        with gpu_lock('cuda'):
            started[0]=time.monotonic();deadline=started[0]+config['gpu_budget_seconds']-prior
            for arm,value in config['arms'].items():
                branch={**binding,'arm':arm,'checkpoint_sha256':value['sha256']}
                heartbeat(arm+'-full')
                full[arm]=evaluate(Path(value['checkpoint']),dev,tok,None,OUTPUT/(arm+'-full.json'),branch,heartbeat,check,full=True)
                current=full[arm]
                require_alignment(current['body'],current['generation'],read_json(config['parent_body']['path'])['body'],read_json(config['parent_generation']['path'])['generation'])
                fixed={r['id']:r for r in current['generation']['outputs'] if r['decoding']=='greedy' and r['suppressed']}
                assert all(fixed[r['id']]['generated_ids']==r['generated_ids'] for r in read_json(RUN/arm/'evaluation/generation.json')['outputs'])
                state=torch.load(value['checkpoint'],map_location='cpu',weights_only=False)
                model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
                bound_evaluation_cache(model);before=rng_state()
                hook=model.register_forward_pre_hook(lambda *_:check())
                heartbeat(arm+'-long128512')
                with sdpa_kernel(SDPBackend.MATH):
                    long[arm]=evaluate_long(NativeLikelihood(model,tok,batch=16),read_json(ROOT/config['long_config']),OUTPUT/arm,json.dumps(branch,sort_keys=True),deadline)
                hook.remove();assert long[arm]['complete'] and equal_state(before,rng_state());check()
                del model,state;gc.collect();torch.cuda.empty_cache()
            candidate=config['candidate']
            summaries={a:summarize(a,10100015104,v['body'],v['generation']) for a,v in full.items()}
            parent=summarize('parent10B',10000007168,read_json(config['parent_body']['path'])['body'],read_json(config['parent_generation']['path'])['generation'])
            mixture=adoption_checks(full['web'],full[candidate])
            checks=dict(original_full_mixture=mixture,parent_growth=growth_checks(summaries[candidate],parent),
                        all400_candidate_raw_failures_zero=all(summaries[candidate]['all400'][k]==0 for k in ('empty','role_leak','unicode_failure')))
            passed=all(mixture.values()) and all(checks['parent_growth'].values()) and checks['all400_candidate_raw_failures_zero']
            result=dict(status='complete',binding=binding,summary=summaries,parent=parent,long_generation=long,checks=checks,
                candidate_passes_all_full_conditions=passed,quality_targets_achieved=False,independent_human_blind='not performed',
                additional_training_tokens=0,protected_test_used=False,GPU_seconds=prior+time.monotonic()-started[0],completed_at=now())
            write_json(OUTPUT/'result.json',result);heartbeat('complete');job.update(status='complete',completed_at=now())
            print(json.dumps(result,ensure_ascii=False),flush=True)
    except BaseException as error:
        job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        if started[0] is not None:job['gpu_elapsed_seconds']=prior+time.monotonic()-started[0]
        atomic_json(job_path,job)

if __name__=='__main__':main()
