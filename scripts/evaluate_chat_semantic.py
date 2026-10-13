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
from chat_semantic_contract import B,RUN,LIMITS,GPU_stage,preflight,load_parent,reference,require_ref,suite_ref,SUITES


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
    if arm=='S0':
        reuse=read_json(require_ref(c['historical_control_evidence']))
        original_job=read_json(require_ref(reuse['original_job']))
        assert original_job['status']=='learning_complete' and not alive(original_job)
        assert original_job['config_sha256']==reuse['original_config']['sha256']
        ref=reuse['checkpoints'][point]
    else:
        job=read_json(RUN/arm/'job.json')
        assert not alive(job) and job['config_sha256']==c['config_sha256']
        ref=read_json(RUN/arm/'checkpoints.json')[point]
    state=torch.load(require_ref(ref),map_location='cpu',weights_only=False)
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
    path=RUN/'NLL'/arm/(point+'.json')
    binding=dict(config_sha256=c['config_sha256'],checkpoint=ref,fixed_targets=c['fixed_NLL'])
    if path.exists():
        result=read_json(path)
        assert result['binding']==binding and result['status']=='complete'
        return
    windows=nll_windows(c,tok)
    from prepare_chat_semantic_reuse import reusable_nll
    reused,provenance=reusable_nll(c,arm,point,ref,windows)
    fresh=[window for window in windows if window[0]['id'] not in reused]
    progress=path.with_suffix('.progress.json')
    saved=read_json(progress) if progress.exists() else dict(binding=binding,rows=[])
    assert saved['binding']==binding
    assert len(saved['rows'])<=len(fresh)
    for original,current in zip(fresh,saved['rows']):
        assert original[0]['id']==current['id'] and original[0]['dataset']==current['dataset']
    for start in range(len(saved['rows']),len(fresh),32):
        if stopped[0] or left()<10:raise InterruptedError('NLL stopped before next complete batch')
        batch=fresh[start:start+32]
        losses=nll_batch(model,batch)
        for (target,_,_),(body,eot) in zip(batch,losses,strict=True):
            saved['rows'].append(dict(id=target['id'],dataset=target['dataset'],body_NLL=body,EOT_NLL=eot,
                body_teachers=target['teachers']-1,EOT_teachers=1,body_bytes=target['body_bytes']))
        atomic_json(progress,saved)
        heartbeat(stage='NLL',arm=arm,point=point,completed=len(saved['rows']))
    indexed=dict(reused)
    for row in saved['rows']:
        assert row['id'] not in indexed
        indexed[row['id']]=row
    assert len(indexed)==2554
    ordered=[indexed[window[0]['id']] for window in windows]
    summaries={}
    for dataset in sorted({row['dataset'] for row in ordered}):
        rows=[row for row in ordered if row['dataset']==dataset]
        sums={key:sum(row[key] for row in rows) for key in ('body_NLL','EOT_NLL','body_teachers','EOT_teachers','body_bytes')}
        summaries[dataset]=dict(sums,targets=len(rows),body_mean_NLL=sums['body_NLL']/sums['body_teachers'],
            EOT_mean_NLL=sums['EOT_NLL']/sums['EOT_teachers'],body_BPB=sums['body_NLL']/sums['body_bytes']/math.log(2))
    atomic_json(path,dict(status='complete',binding=binding,summaries=summaries,targets=ordered,completed_at=now(),
        historical_exact_NLL_reuse=provenance,new_GPU_NLL_targets=len(fresh),
        provided_gold_history=True,own_generated_quality=False,protected_TEST_used=False,
        comparison='Only same fixed target texts/masks/bytes across checkpoints; cross-dataset losses are not quality rankings'))

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
        Chat_adopted=False,requested_six_steps_complete=False,completed_at=now())


def evaluation_binding(c,arm,point,ref,suite,seed=42,decoding='greedy'):
    binding=dict(checkpoint=ref['path'],checkpoint_sha256=ref['sha256'],config_sha256=c['config_sha256'],
        stage=arm+'-'+point,tokenizer_sha256=c['tokenizer']['sha256'],suite_sha256=suite_ref(c,suite)['sha256'],
        max_new_tokens=64,model_context=1024,dtype='bf16',backend='math',decoding=decoding,
        evaluation_seeds=[42] if decoding=='greedy' else [42,43,44],evaluation_seed=seed,
        source_sha256=c['source_sha256'],implementation=c['implementation'],scored_split='dev',protected_test_used=False,
        protocol='provided80 suppressed + provided80 unsuppressed role control +24 own-history2-4turn dialogues')
    if decoding=='sampling':binding['sampling']=dict(seed=seed,temperature=.8,top_p=.9,top_k=50)
    return binding

def chat(model,c,tok,arm,point,ref,suite,seed,decoding,left,heartbeat,stopped):
    cases,contexts=load_cases(suite_ref(c,suite)['path'],tok)
    directory=RUN/'evaluation'/arm/point/suite/('greedy' if decoding=='greedy' else f'seed-{seed}')
    binding=evaluation_binding(c,arm,point,ref,suite,seed,decoding)
    sampling=binding.get('sampling')
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
    cases,contexts=load_cases(suite_ref(c,'new')['path'],tok);timings=[];raw=[]
    # Actual generator on largest provided prompts plus a worst-length own
    # history frame. Synthetic Assistant filler is timing-only, never quality.
    selected=sorted(cases,key=lambda x:len(tok.chat_prompt(x['messages'],960)[0]),reverse=True)[:4]
    messages=[s['messages'] for s in selected]
    worst=max(contexts,key=lambda x:len(x['messages']))['messages']
    messages.append([dict(m) if m['role']=='user' else dict(role='assistant',content='あ'*64) for m in worst])
    # Prespecified separation: cold startup once per invocation, never charged
    # as the steady token cost of every response. Same worst-case counts and
    # safety factor as the preceding accepted forecast method.
    for index,ms in enumerate([messages[0]]+messages*2):
        if stopped[0] or left()<15:raise InterruptedError('Forecast interrupted')
        started=time.monotonic();r=generate_reply(model,tok,ms,'cuda','bf16',64,True,lambda:None)
        torch.cuda.synchronize();seconds=time.monotonic()-started
        timings.append(dict(phase='cold' if index==0 else 'steady',seconds=seconds,tokens=r['generated_tokens'],seconds_per_token=seconds/r['generated_tokens'],prompt_tokens=r['prompt_tokens']))
        raw.append(dict(messages=ms,response=r,timing_only=True));heartbeat(stage='forecast-generation',completed=len(raw))
    windows=nll_windows(c,tok);nll_times=[]
    for start in (0,0,112,224):
        started=time.monotonic();nll_batch(model,windows[start:start+32]);torch.cuda.synchronize();nll_times.append(time.monotonic()-started)
    #21 required greedy suites minus8 exact known-suite reuses; conditional
    #three sampling seeds on all3 suites are fully reserved, no recovery here.
    reuse=read_json(RUN/'historical_control_registration.json')
    assert reuse['passed'] and reuse['known_suite_judgments_reused']==1752
    outputs=21*219-1752+9*219
    rate=max(r['seconds_per_token'] for r in timings[1:])
    generation_seconds=rate*64*outputs*1.5
    nll_batches=3*math.ceil(2554/32)+4*math.ceil(192/32)
    nll_seconds=max(nll_times[1:])*nll_batches*1.5
    cold=16*(max(0.,timings[0]['seconds']-rate*timings[0]['tokens'])+max(0.,nll_times[0]-max(nll_times[1:])))
    total=generation_seconds+nll_seconds+cold+600.
    r=dict(passed=total<=LIMITS['evaluation'],config_sha256=c['config_sha256'],timings=timings,raw_timing_only=raw,
        NLL_batch_seconds=nll_times,maximum_required_responses=outputs,maximum_tokens_per_response=64,
        conservative_generation_seconds=generation_seconds,conservative_NLL_seconds=nll_seconds,cold_overhead_seconds=cold,
        cold_once_per_invocation=True,planned_maximum_model_invocations=16,
        forecast_evaluation_seconds=total,limit_seconds=LIMITS['evaluation'],includes_all_greedy_savepoints_and_conditional_three_seed_sampling=True,
        verified_historical_outputs_reused=1752,maximum_new_NLL_batches=nll_batches,
        includes_recovery=False,includes_three_regression_suites=True,
        quality_evidence=False,completed_at=now())
    atomic_json(path,r);assert r['passed'],'Required complete evaluation cannot fit frozen budget; no main learning allowed'


def main():
    p=argparse.ArgumentParser();p.add_argument('--config',type=Path,required=True)
    p.add_argument('--mode',choices=('forecast','evaluate'),required=True);p.add_argument('--arm',choices=('parent','S0','S1'),default='parent')
    p.add_argument('--points',nargs='+',choices=('t0','t1','t2','t3'),default=['t0'])
    p.add_argument('--suites',nargs='+',choices=SUITES,default=list(SUITES))
    p.add_argument('--decoding',choices=('greedy','sampling'),default='greedy');p.add_argument('--inspect',action='store_true')
    args=p.parse_args();c,tok,_=preflight(args.config.resolve())
    for suite in args.suites:load_cases(suite_ref(c,suite)['path'],tok)
    if args.inspect:print('Frozen evaluation CPU preflight passed; no GPU launch');return
    torch.set_num_threads(2);torch.use_deterministic_algorithms(True);seed_all(42)
    stopped=[False];signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    if args.decoding=='sampling':
        selection=read_json(RUN/'selection.json');assert selection['eligible_candidate']==args.arm and selection['all_suites_passed']
        assert args.points==['t3']
    with GPU_stage('evaluation',args.mode+'-'+args.arm,c['config_sha256']) as (left,heartbeat),sdpa_kernel(SDPBackend.MATH):
        for point in args.points:
            assert (args.arm=='parent')==(point=='t0')
            state,ref=checkpoint(c,args.arm,point);model=JMicroModel(state['model_config']).cuda().eval();model.load_state_dict(state['model'],strict=True);del state
            assert sum(parameter.numel() for parameter in model.parameters() if parameter.requires_grad)==10001152
            if args.mode=='forecast':forecast(model,c,tok,left,heartbeat,stopped)
            else:
                for suite in args.suites:
                    for seed in ([42] if args.decoding=='greedy' else [42,43,44]):
                        chat(model,c,tok,args.arm,point,ref,suite,seed,args.decoding,left,heartbeat,stopped)
                if args.decoding=='greedy':fixed_nll(model,c,tok,args.arm,point,ref,left,heartbeat,stopped)
            del model;gc.collect();torch.cuda.empty_cache()

if __name__=='__main__':main()
