"""Shared-ledger raw Chat evaluation and common-target body/EOT NLL."""
import argparse
from collections import defaultdict
import gc
import hashlib
import json
import math
import os
from pathlib import Path
import re
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel,SDPBackend
from jmicro.chat_evaluation import generate_reply,rollout_dialogue,summarize_chat
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.model import JMicroModel
from jmicro.training import atomic_json,autocast,rng_state,seed_all,isolated_evaluation
from run_eos_short_pilot import equal_state
from phase6_performance import identity,alive,finite_state
from chat_improvement_contract import B,RUN,GPU_stage,preflight,load_parent,reference,require_ref


def load_cases(path,tok):
    cases=[]
    for line in Path(path).read_text().splitlines():
        # Do not parse protected TEST objects in the mixed historical suite.
        if not re.search(r'"split"\s*:\s*"dev"',line):continue
        row=json.loads(line);assert row['split']=='dev';cases.append(row)
    assert len(cases)==80 and len({c['family_id'] for c in cases})==80
    contexts=[c for c in cases if 2<=sum(m['role']=='user' for m in c['messages'])<=4]
    assert len(contexts)==24 and sum(sum(m['role']=='user' for m in c['messages']) for c in contexts)==59
    for c in cases:
        _,removed=tok.chat_prompt(c['messages'],960);assert removed==0
    return cases,contexts


def checkpoint(c,arm,point):
    if arm=='parent':return load_parent(c),c['parent']
    job=read_json(RUN/arm/'job.json');assert not alive(job) and job['config_sha256']==c['config_sha256']
    ref=read_json(RUN/arm/'checkpoints.json')[point];require_ref(ref)
    state=torch.load(ref['path'],map_location='cpu',weights_only=False)
    assert state['implementation_sha256']==c['implementation'] and finite_state(state)
    assert state['lineage']['kind']=='teacher-normalized-assistant-sft' and state['lineage']['base_checkpoint']==c['parent']
    contract=state['spec']['teacher_chat']
    assert contract['budget']==B and contract['data_binding']==c['arms'][arm]['sampler_binding']
    assert state['supervised_tokens']==ref['Assistant_teachers'] and state['update']==ref['update']
    return state,ref


def nll_windows(c,tok):
    windows=[]
    for line in require_ref(c['fixed_NLL']).read_text().splitlines():
        r=json.loads(line);w=list(tok.sft_windows(r['messages'],context=1025))[-1]
        assert hashlib.sha256(json.dumps(w,ensure_ascii=False,sort_keys=True).encode()).hexdigest()==r['window_binding']
        labels=np.asarray(w['labels'][1:]);assert int((labels!=-100).sum())==r['teachers']
        windows.append((r,np.asarray(w['input_ids'][:-1]),labels))
    assert len(windows)==2554
    return windows


def nll_batch(model,batch):
    x=np.zeros((32,1024),dtype=np.int64);y=np.full_like(x,-100)
    for i,(_,ids,labels) in enumerate(batch):x[i,:len(ids)]=ids;y[i,:len(labels)]=labels
    tx=torch.from_numpy(x).cuda();ty=torch.from_numpy(y).cuda()
    with isolated_evaluation(model),sdpa_kernel(SDPBackend.MATH),autocast('cuda','bf16'):
        logits=model(tx,attention_mask=tx.ne(0)).logits
        losses=F.cross_entropy(logits.float().reshape(-1,4096),ty.reshape(-1),ignore_index=-100,reduction='none').reshape(32,1024)
    assert torch.isfinite(losses).all()
    return [(float(losses[i][ty[i]>=8].sum()),float(losses[i][ty[i]==7].sum())) for i in range(len(batch))]


def fixed_nll(model,c,tok,arm,point,ref,left,heartbeat,stopped):
    path=RUN/'NLL'/arm/(point+'.json');binding=dict(config_sha256=c['config_sha256'],checkpoint=ref,fixed_targets=c['fixed_NLL'])
    if path.exists():
        result=read_json(path);assert result['binding']==binding and result['status']=='complete';return
    windows=nll_windows(c,tok);progress=path.with_suffix('.progress.json')
    saved=read_json(progress) if progress.exists() else dict(binding=binding,rows=[])
    assert saved['binding']==binding
    for start in range(len(saved['rows']),len(windows),32):
        if stopped[0] or left()<10:raise InterruptedError('NLL stopped before next complete batch')
        batch=windows[start:start+32];losses=nll_batch(model,batch)
        for (r,_,_),(body,eot) in zip(batch,losses,strict=True):
            saved['rows'].append(dict(id=r['id'],dataset=r['dataset'],body_NLL=body,EOT_NLL=eot,
                body_teachers=r['teachers']-1,EOT_teachers=1,body_bytes=r['body_bytes']))
        atomic_json(progress,saved);heartbeat(stage='NLL',arm=arm,point=point,completed=len(saved['rows']))
    summaries={}
    for dataset in sorted({r['dataset'] for r in saved['rows']}):
        rows=[r for r in saved['rows'] if r['dataset']==dataset]
        sums={k:sum(r[k] for r in rows) for k in ('body_NLL','EOT_NLL','body_teachers','EOT_teachers','body_bytes')}
        summaries[dataset]=dict(sums,targets=len(rows),body_mean_NLL=sums['body_NLL']/sums['body_teachers'],
            EOT_mean_NLL=sums['EOT_NLL']/sums['EOT_teachers'],body_BPB=sums['body_NLL']/sums['body_bytes']/math.log(2))
    atomic_json(path,dict(status='complete',binding=binding,summaries=summaries,targets=saved['rows'],completed_at=now(),
        provided_gold_history=True,own_generated_quality=False,protected_TEST_used=False,
        comparison='Compare only same fixed target texts/bytes across checkpoints; cross-dataset loss levels are not quality rankings'))


def summarize(saved,cases,contexts,binding):
    primary=[saved['provided']['suppressed-'+c['id']] for c in cases]
    control=[saved['provided']['unsuppressed-'+c['id']] for c in cases]
    final=[saved['rollouts'][c['id']]['replies'][-1] for c in contexts]
    turns=[r for c in contexts for r in saved['rollouts'][c['id']]['replies']]
    assert len(primary)==len(control)==80 and len(final)==24 and len(turns)==59
    return dict(status='mechanical_evaluation_complete_pending_all_content_judgments',binding=binding,
        primary=summarize_chat(primary),role_control=summarize_chat(control),own_history_final24=summarize_chat(final),
        own_history_all_turns=summarize_chat(turns),outputs=saved['provided'],rollouts=saved['rollouts'],
        grammar_relevance_context_not_scored=True,evaluation_RNG_isolated=True,protected_test_used=False,
        Chat_adopted=False,requested_five_steps_complete=False,completed_at=now())


def chat(model,c,tok,arm,point,ref,suite,seed,decoding,left,heartbeat,stopped):
    cases,contexts=load_cases(c['new_DEV' if suite=='new' else 'old_suite']['path'],tok)
    directory=RUN/'evaluation'/arm/point/suite/('greedy' if decoding=='greedy' else f'seed-{seed}')
    binding=dict(checkpoint=ref['path'],checkpoint_sha256=ref['sha256'],config_sha256=c['config_sha256'],
        stage=arm+'-'+point,tokenizer_sha256=c['tokenizer']['sha256'],suite_sha256=c['new_DEV' if suite=='new' else 'old_suite']['sha256'],
        max_new_tokens=64,model_context=1024,dtype='bf16',backend='math',decoding=decoding,
        evaluation_seeds=[42] if decoding=='greedy' else [42,43,44],evaluation_seed=seed,
        source_sha256=c['source_sha256'],implementation=c['implementation'],scored_split='dev',protected_test_used=False,
        protocol='provided80 suppressed + provided80 unsuppressed role control +24 own-history2-4turn dialogues')
    sampling=None if decoding=='greedy' else dict(seed=seed,temperature=.8,top_p=.9,top_k=50)
    if sampling is not None:binding['sampling']=sampling
    result_path=directory/'result.json';job_path=directory/'job.json';progress_path=directory/'progress.json'
    if result_path.exists():
        result=read_json(result_path);assert result['binding']==binding;return
    previous=read_json(job_path) if job_path.exists() else {}
    if previous:assert not alive(previous) and previous['binding']==binding
    saved=read_json(progress_path) if progress_path.exists() else dict(binding=binding,provided={},rollouts={})
    assert saved['binding']==binding
    job=dict(**identity(),status='running',binding=binding,started_at=now());atomic_json(job_path,job)
    def check():
        if stopped[0] or left()<8:raise InterruptedError('Evaluation stopped; completed cases retained')
    try:
        before=rng_state()
        for suppressed in (True,False):
            mode='suppressed' if suppressed else 'unsuppressed'
            for case in cases:
                key=mode+'-'+case['id']
                if key in saved['provided']:continue
                check();row=generate_reply(model,tok,case['messages'],'cuda','bf16',64,suppressed,check,sampling=sampling)
                row.update({k:case[k] for k in ('id','family_id','category','split','checks','messages')})
                row['history_mode']='provided_assistant_history';assert row['full_history_retained']
                saved['provided'][key]=row;atomic_json(progress_path,saved)
                heartbeat(stage='provided-'+mode,arm=arm,point=point,suite=suite,completed=len(saved['provided']))
        for case in contexts:
            if case['id'] in saved['rollouts']:continue
            check();row=rollout_dialogue(model,tok,case,'cuda','bf16',64,check,sampling=sampling)
            assert row['full_history_retained'];saved['rollouts'][case['id']]=row;atomic_json(progress_path,saved)
            heartbeat(stage='own-history',arm=arm,point=point,suite=suite,completed=len(saved['rollouts']))
        assert equal_state(before,rng_state())
        atomic_json(result_path,summarize(saved,cases,contexts,binding));atomic_json(directory/'recipe.json',binding)
        job.update(status='complete',completed_at=now())
    except BaseException as exc:job.update(status='failed_or_stopped',error=repr(exc));raise
    finally:atomic_json(job_path,job)


def forecast(model,c,tok,left,heartbeat,stopped):
    path=RUN/'evaluation_forecast.json'
    if path.exists():
        r=read_json(path);assert r['passed'] and r['config_sha256']==c['config_sha256'];return
    cases,contexts=load_cases(c['new_DEV']['path'],tok);timings=[];raw=[]
    # Actual generator on largest provided prompts plus a worst-length own
    # history frame. Synthetic Assistant filler is timing-only, never quality.
    selected=sorted(cases,key=lambda x:len(tok.chat_prompt(x['messages'],960)[0]),reverse=True)[:4]
    messages=[s['messages'] for s in selected]
    worst=max(contexts,key=lambda x:len(x['messages']))['messages']
    messages.append([dict(m) if m['role']=='user' else dict(role='assistant',content='あ'*64) for m in worst])
    for ms in messages:
        if stopped[0] or left()<15:raise InterruptedError('Forecast interrupted')
        started=time.monotonic();r=generate_reply(model,tok,ms,'cuda','bf16',64,True,lambda:None)
        torch.cuda.synchronize();seconds=time.monotonic()-started
        timings.append(dict(seconds=seconds,tokens=r['generated_tokens'],seconds_per_token=seconds/r['generated_tokens'],prompt_tokens=r['prompt_tokens']))
        raw.append(dict(messages=ms,response=r,timing_only=True));heartbeat(stage='forecast-generation',completed=len(raw))
    windows=nll_windows(c,tok);nll_times=[]
    for start in (0,112,224):
        started=time.monotonic();nll_batch(model,windows[start:start+32]);torch.cuda.synchronize();nll_times.append(time.monotonic()-started)
    # Worst-case 64 tokens on every required output, all final eligible sampling
    # seeds included; no saved old-parent outputs assumed reusable in estimate.
    outputs=7*2*219+3*2*219
    generation_seconds=max(r['seconds_per_token'] for r in timings)*64*outputs*1.5
    nll_seconds=max(nll_times)*math.ceil(2554/32)*7*1.5
    total=generation_seconds+nll_seconds+600.
    r=dict(passed=total<=10800.,config_sha256=c['config_sha256'],timings=timings,raw_timing_only=raw,
        NLL_batch_seconds=nll_times,maximum_required_responses=outputs,maximum_tokens_per_response=64,
        conservative_generation_seconds=generation_seconds,conservative_NLL_seconds=nll_seconds,
        forecast_evaluation_seconds=total,limit_seconds=10800.,includes_all_greedy_savepoints_and_conditional_three_seed_sampling=True,
        quality_evidence=False,completed_at=now())
    atomic_json(path,r);assert r['passed'],'Required complete evaluation cannot fit frozen budget; no main learning allowed'


def main():
    p=argparse.ArgumentParser();p.add_argument('--config',type=Path,required=True)
    p.add_argument('--mode',choices=('forecast','evaluate'),required=True);p.add_argument('--arm',choices=('parent','C0','C1'),default='parent')
    p.add_argument('--points',nargs='+',choices=('t0','t1','t2','t3'),default=['t0'])
    p.add_argument('--suites',nargs='+',choices=('new','old'),default=['new','old'])
    p.add_argument('--decoding',choices=('greedy','sampling'),default='greedy');p.add_argument('--inspect',action='store_true')
    args=p.parse_args();c,tok,_=preflight(args.config.resolve())
    for suite in args.suites:load_cases(c['new_DEV' if suite=='new' else 'old_suite']['path'],tok)
    if args.inspect:print('Frozen evaluation CPU preflight passed; no GPU launch');return
    torch.set_num_threads(2);torch.use_deterministic_algorithms(True);seed_all(42)
    stopped=[False];signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    if args.decoding=='sampling':
        selection=read_json(RUN/'selection.json');assert selection['eligible_candidate']==args.arm and selection['both_suites_passed']
        assert args.points==['t3']
    with GPU_stage('evaluation',args.mode+'-'+args.arm,c['config_sha256']) as (left,heartbeat),sdpa_kernel(SDPBackend.MATH):
        for point in args.points:
            assert (args.arm=='parent')==(point=='t0')
            state,ref=checkpoint(c,args.arm,point);model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model'],strict=True);del state
            if args.mode=='forecast':forecast(model,c,tok,left,heartbeat,stopped)
            else:
                for suite in args.suites:
                    for seed in ([42] if args.decoding=='greedy' else [42,43,44]):
                        chat(model,c,tok,args.arm,point,ref,suite,seed,args.decoding,left,heartbeat,stopped)
                if args.decoding=='greedy':fixed_nll(model,c,tok,args.arm,point,ref,left,heartbeat,stopped)
            del model;gc.collect();torch.cuda.empty_cache()

if __name__=='__main__':main()
