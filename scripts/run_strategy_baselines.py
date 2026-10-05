"""Read-only before/after auxiliary evidence for optional stage3 budget growth."""
import gc
import json
import math
import os
from pathlib import Path
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import torch
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import gpu_lock,atomic_json
from phase6_performance import identity,alive
from run_curriculum_strategy import RUN,DATA,CONFIG,load_config
from run_generation_transfer import make_case
from run_root_cause_diagnostic import teacher,generate


def run():
    c=load_config();comparison=read_json(RUN/'compare-result.json');job=read_json(RUN/'job.json')
    assert job['status']=='complete' and not alive(job)
    path=RUN/'baselines-job.json'
    if path.exists():
        previous=read_json(path);assert not alive(previous)
        if previous['status']=='complete':print('Completed baseline evidence retained');return
        raise ValueError('Inspect failed baseline evidence before restart')
    start=time.monotonic();record=dict(status='running',**identity(),started_at=now(),scientific_teacher_tokens=0,
        config_sha256=sha256(CONFIG),budget_seconds=min(300,c['gpu_budget_seconds']-job['gpu_elapsed_seconds']))
    # Freeze the optional-extension rule before observing this before/after evidence.
    decision_rule=dict(auxiliary_BPB_relative_improvement_at_least=.01,auxiliary_EOS_gain_at_least=4,
        repetition_nonworsening=True,no_empty_or_unicode=True,
        equal_budget_pair_requires_both_strategies_eligible=True,
        purpose='At most300M cumulative teachers per strategy, not adoption; original quality gates unchanged',
        schedule='If eligible, continue each100M checkpoint for additional200M using inherited optimizer and sampler, original peaks/no repeat warmup, stable90percent then10percent decay. Staged reheating, not uninterrupted300M.',
        max_total_strategy_GPU_seconds=c['gpu_budget_seconds'],created_at=now())
    write_json(RUN/'extension-rule.json',decision_rule);atomic_json(path,record)
    tok=Tokenizer(ROOT/c['tokenizer']);source=read_json(DATA/'dev32.json')
    cases=[make_case(r,tok,'dev') for r in source]
    full_cases=[dict(r,prefix_ids=[2],gold_ids=[*r['body_ids'],3]) for r in cases]
    entries=dict(before_continuation=c['parent'],before_fresh=dict(path=str(RUN/'initial-fresh.pt'),sha256=sha256(RUN/'initial-fresh.pt')))
    for arm,d in comparison['checkpoints'].items():entries['after_'+arm]=dict(path=d['checkpoint'],sha256=d['checkpoint_sha256'])
    results={}
    try:
        torch.set_num_threads(2)
        with gpu_lock('cuda'):
            for name,entry in entries.items():
                if time.monotonic()-start>record['budget_seconds']:raise TimeoutError('Remaining stage3 GPU budget exhausted')
                assert sha256(Path(entry['path']))==entry['sha256']
                state=torch.load(entry['path'],map_location='cpu',weights_only=False)
                model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model']);del state
                gold=[];rows=[]
                for offset in range(0,32,16):
                    record.update(stage=name,heartbeat_at=now(),gpu_seconds=time.monotonic()-start);atomic_json(path,record)
                    gold.extend(teacher(model,full_cases[offset:offset+16]))
                    if name.startswith('before'):rows.extend(generate(model,cases[offset:offset+16],tok,None,64))
                if name.startswith('after'):rows=comparison['auxiliary'][name.removeprefix('after_')]['generation']
                byte_count=sum(len(r['text'].encode()) for r in cases)
                body_nll=sum(sum(s['target_nll'] for s in r['teacher_steps'][:-1]) for r in gold)
                invalid=0
                for r in rows:
                    try:tok.decode_bytes(r['generated_ids']).decode('utf-8')
                    except UnicodeDecodeError:invalid+=1
                results[name]=dict(checkpoint=entry,body_bytes=byte_count,body_NLL=body_nll,BPB=body_nll/math.log(2)/byte_count,
                    EOS=sum(r['stop_reason']=='eos' for r in rows),repeated4gram=sum(r['first_repeated_4gram'] is not None for r in rows),
                    empty=sum(not r['text'].strip() for r in rows),invalid_UTF8=invalid,teacher=gold,generation=rows)
                del model;gc.collect();torch.cuda.empty_cache()
            eligible={}
            for arm in ('continuation','fresh'):
                a,b=[results[p+'_'+arm] for p in ('before','after')]
                checks=dict(BPB=b['BPB']<=a['BPB']*.99,EOS=b['EOS']-a['EOS']>=4,
                    repetition=b['repeated4gram']<=a['repeated4gram'],no_empty_UTF8=b['empty']==b['invalid_UTF8']==0)
                eligible[arm]=dict(checks=checks,eligible=all(checks.values()))
            report=dict(rule=decision_rule,results=results,eligibility=eligible,
                equal300M_pair_eligible=all(r['eligible'] for r in eligible.values()),
                scientific_teacher_tokens=0,GPU_seconds=time.monotonic()-start,
                source_history='Auxiliary Web includes original train; official general quality evaluated separately',
                interpretation='Repetition here is raw repeated4gram presence, not independently judged semantic-loop rate; eligibility is research budget only',
                protected_test_used=False,created_at=now())
            write_json(RUN/'baselines.json',report)
            print(json.dumps(dict(eligibility=eligible,metrics={k:{m:r[m] for m in ('BPB','EOS','repeated4gram','empty','invalid_UTF8')} for k,r in results.items()})),flush=True)
        record.update(status='complete',completed_at=now())
    except BaseException as error:record.update(status='failed',error=repr(error));raise
    finally:record['gpu_seconds']=time.monotonic()-start;atomic_json(path,record)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);run()
