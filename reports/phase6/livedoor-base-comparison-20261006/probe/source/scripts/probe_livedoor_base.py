"""Own inherited CUDA gates and both source timings, discarded verification weights."""
import argparse
import copy
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import statistics
import sys
import time
import xml.etree.ElementTree as ET
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.eos_pilot import TrainView
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state
from livedoor_base_trainer import NewsBaseTrainer,KIND,LR
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state

RUN=ROOT/'reports/phase6/livedoor-base-comparison-20261006'
CONFIG=ROOT/'configs/phase6/livedoor_base_probe.json'
PROPOSAL=ROOT/'reports/phase6/livedoor_base_comparison_proposal.json'
SOURCES=('scripts/livedoor_base_trainer.py','scripts/probe_livedoor_base.py','scripts/probe_livedoor_base.ps1','tests/test_livedoor_base_trainer.py')
TRACKED=('model','optimizer','scheduler','rng','sampler','lineage','tokens','supervised_tokens','body_bytes','token_digest','focus_token_digest',
    'focus_teacher_tokens','weighted_teacher_mass','update','spec','model_config','pilot_binding','study_binding')


def reference(q):return dict(path=str(q),sha256=sha256(q))


def check_reference(ref):
    if sha256(Path(ref['path']))!=ref['sha256']:raise ValueError('Original news reference differs: '+ref['path'])


def prepare():
    if CONFIG.exists():inspect();return
    start=time.monotonic();p=read_json(PROPOSAL)
    if (p['kind']!=KIND or p['reused_prefix_teacher_tokens']!=73571878 or p['new_scientific_teacher_tokens']!=26428122
            or p['new_teacher_goals']!={'web':1428122,'authored_news':25000000} or p['scientific_GPU_frozen'] or p['new_GPU_seconds']):
        raise ValueError('Actual accepted news/common-prefix definition required')
    refs={k:p[k] for k in ('source_preparation','source_ready','source_content_review','original_parent','cached_control_config','cached_control_result','cached_control_history','shared_prefix')}
    refs.update(proposal=reference(PROPOSAL),CPU_tests=reference(ROOT/'reports/phase6/livedoor_base_trainer_tests.xml'))
    suites=list(ET.parse(refs['CPU_tests']['path']).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=2 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):raise ValueError('Two actual inherited-state/source-budget CPU tests required')
    old=read_json(Path(p['cached_control_config']['path']))
    old_sources={**old.get('old_source_sha256',{}),**old['source_sha256']}
    old_sources.update({s:sha256(ROOT/s) for s in ('scripts/original_web_retention_trainer.py','scripts/condition_positive_trainer.py','scripts/condition_positive_loss.py','scripts/phase6_performance.py','scripts/run_eos_short_pilot.py')})
    parent=torch.load(p['shared_prefix']['path'],map_location='cpu',weights_only=False)
    web=TrainView(p['data']['original_web']['path'],p['data']['original_web']['manifest_sha256'])
    news=TrainView(p['data']['news_pool'],p['data']['news_manifest_sha256'])
    trial=NewsBaseTrainer(parent,web,news,p['new_teacher_goals'],dict(parent=p['shared_prefix'],original_parent=p['original_parent']),'cpu')
    host_rng=lambda state:{k:v for k,v in state.items() if k!='cuda'}
    if (not equal_state(trial.model.state_dict(),parent['model']) or not equal_state(trial.optimizer.state_dict(),parent['optimizer'])
            or not equal_state(trial.scheduler.state_dict(),parent['scheduler']) or not equal_state(host_rng(rng_state()),host_rng(parent['rng']))):
        raise ValueError('Actual CPU prefix/source/initial fullstate preparation differs')
    c=dict(kind=KIND,phase='own_CUDA_verification',parent=p['shared_prefix'],original_parent=p['original_parent'],references=refs,
        data=p['data'],goals=p['new_teacher_goals'],stress_goals=dict(web=1,authored_news=25000000),context=1024,batch=32,LR=LR,
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},old_source_sha256=old_sources,implementation=implementation_hashes(),
        GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=1800,verification_updates=80,
        actual_CPU_model_Adam_scheduler_host_RNG_passed=True,CUDA_RNG_preservation_unverified_until_own_GPU_gate=True,
        news_unsampled_tail_tokens=len(news.tokens)-(((len(news.tokens)-1)//1024)*1024+1),
        CPU_preparation_seconds=time.monotonic()-start,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False)
    if c['CPU_preparation_seconds']>30:raise TimeoutError('News probe CPU freeze30s exhausted')
    atomic_json(CONFIG,c);inspect();print(json.dumps(dict(status='news_own_CUDA_probe_frozen',GPU_seconds=0,CPU_seconds=c['CPU_preparation_seconds'])))


def inspect():
    c=read_json(CONFIG)
    if (c['kind']!=KIND or c['phase']!='own_CUDA_verification' or c['LR']!=LR or c['goals']!={'web':1428122,'authored_news':25000000}
            or c['stress_goals']!={'web':1,'authored_news':25000000} or c['context']!=1024 or c['batch']!=32
            or c['GPU_budget_seconds']!=120 or c['total_new_GPU_ceiling_seconds']!=1800 or c['verification_updates']!=80
            or c['implementation']!=implementation_hashes() or any(c[k] for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_used'))):
        raise ValueError('Original news CUDA contract differs')
    for name,digest in {**c['old_source_sha256'],**c['source_sha256']}.items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen source differs: '+name)
    for ref in c['references'].values():check_reference(ref)
    if (RUN/'probe/job.json').exists() and alive(read_json(RUN/'probe/job.json')):raise ValueError('Actual live news probe; no duplicate')
    return c


def binding(c,route,goals):
    return dict(config_sha256=sha256(CONFIG),arm='authored_news',study_kind=KIND,parent=c['parent'],original_parent=c['original_parent'],
        teacher_goals=goals.copy(),verification_route=route,optimizer_policy='inherit_native',scientific=False)


def resume_gate(build,folder,check,parent):
    folder.mkdir(parents=True,exist_ok=True);states=[];histories=[];teachers=0
    for route in ('continuous','resumed'):
        trainer=build();history=[]
        for i in range(4):
            check();history.append(trainer.step())
            if route=='resumed' and i==1:
                trainer.save(folder/'split.pt');del trainer;gc.collect();torch.cuda.empty_cache();trainer=build();trainer.load(folder/'split.pt')
        teachers+=trainer.supervised_tokens-parent['supervised_tokens'];trainer.save(folder/(route+'.pt'))
        states.append(torch.load(folder/(route+'.pt'),map_location='cpu',weights_only=False));histories.append(history)
        del trainer;gc.collect();torch.cuda.empty_cache()
    checks={k:equal_state(states[0][k],states[1][k]) for k in TRACKED}
    for k in histories[0][0]:
        if k not in ('seconds','data_wait_seconds','tokens_per_second'):checks['history_'+k]=all(equal_state(a[k],b[k]) for a,b in zip(*histories,strict=True))
    checks.update(finite=all(finite_state(s) for s in states),fixed_inherited_LR=all(v['lr']==LR for h in histories for v in h))
    if not all(checks.values()):raise ValueError('Actual news fullstate/history CUDA restart differs: '+repr(checks))
    result=dict(passed=True,checks=checks,histories=histories,verification_teacher_tokens=teachers,GPU_optimizer_updates=8)
    atomic_json(folder/'result.json',result);return result


def estimate_training(result):
    timings=result['timings'];measured={}
    if set(timings)!={'original_Web','news_boundary_stress'}:raise ValueError('Both actual source timings required')
    for name,t in timings.items():
        rows=t['histories']
        if len(rows)!=32 or any(not math.isfinite(r['seconds']) or r['seconds']<=0 or r['lr']!=LR for r in rows):raise ValueError('32 actual finite fixed-LR updates required')
        step=statistics.median(r['seconds'] for r in rows[8:]);teachers=(rows[-1]['additional_teacher_tokens']-rows[7]['additional_teacher_tokens'])/24
        if teachers<=0:raise ValueError('Positive actual teacher denominator required')
        measured[name]=dict(steady_step_seconds=step,teachers_per_update=teachers,warmup_seconds=max(0.,sum(r['seconds'] for r in rows[:8])-8*step),save_seconds=t['terminal_save_seconds'])
    updates=math.ceil(1428122/measured['original_Web']['teachers_per_update'])+math.ceil(25000000/measured['news_boundary_stress']['teachers_per_update'])+2
    steady=max(m['steady_step_seconds'] for m in measured.values());warm=sum(m['warmup_seconds'] for m in measured.values())
    saving=(math.ceil(updates/250)+1)*max(m['save_seconds'] for m in measured.values());cost=updates*steady+warm+saving
    return dict(source_timings=measured,estimated_updates=updates,steady_step_seconds=steady,warmup_seconds=warm,save_seconds=saving,estimated_training_seconds=cost),cost*1.3+300


def run():
    c=inspect();folder=RUN/'probe';folder.mkdir(parents=True,exist_ok=True);jp=folder/'job.json'
    if jp.exists():raise ValueError('Preserve actual one-shot probe; any repair requires documented failure')
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=now(),GPU_elapsed_seconds=0,restart_command='scripts/probe_livedoor_base.ps1 -Worker; terminal probe requires documented repair')
    atomic_json(jp,job);started=None;stopped=[False]
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('News probe interrupted')
        if started is not None and time.monotonic()-started>120:raise TimeoutError('Own news CUDA120s exhausted')
    def heartbeat(stage,**kw):
        check();job.update(stage=stage,heartbeat_at=now(),**kw)
        if started is not None:job['GPU_elapsed_seconds']=time.monotonic()-started
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False
        for name in (*c['source_sha256'],*c['old_source_sha256'],CONFIG.relative_to(ROOT).as_posix()):
            target=folder/'source'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,target)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        web=TrainView(c['data']['original_web']['path'],c['data']['original_web']['manifest_sha256'])
        news=TrainView(c['data']['news_pool'],c['data']['news_manifest_sha256'])
        def build(route,goals):return NewsBaseTrainer(parent,web,news,goals,binding(c,route,goals))
        with gpu_lock('cuda'):
            started=time.monotonic();job['status']='running';heartbeat('initial_actual_inherited_state');initial=build('original_Web',c['goals'])
            preservation=dict(model=equal_state(initial.model.state_dict(),parent['model']),optimizer=equal_state(initial.optimizer.state_dict(),parent['optimizer']),
                scheduler=equal_state(initial.scheduler.state_dict(),parent['scheduler']),RNG=equal_state(rng_state(),parent['rng']),
                Web_cursor=equal_state(initial.sampler.streams['web'].sampler.state_dict(),parent['sampler']['streams']['web']['sampler']),
                native_tied10M=sum(p.numel() for p in initial.model.parameters())==10001152 and initial.model.lm_head.weight is initial.model.model.embed_tokens.weight)
            if not all(preservation.values()):raise ValueError('Actual common-prefix preservation differs')
            del initial;gc.collect();torch.cuda.empty_cache();result=dict(initial_preservation=preservation,gates={},timings={});teachers=0
            for route,goals in (('original_Web',c['goals']),('news_boundary_stress',c['stress_goals'])):
                factory=lambda route=route,goals=goals:build(route,goals)
                heartbeat(route+'-resume');gate=resume_gate(factory,folder/route/'resume-gate',check,parent)
                if route=='news_boundary_stress' and not gate['histories'][0][0]['source_teachers']['authored_news']:raise ValueError('Actual CUDA news transition required')
                result['gates'][route]=gate;teachers+=gate['verification_teacher_tokens'];heartbeat(route+'-32timing');trainer=factory();rows=[];torch.cuda.reset_peak_memory_stats()
                with (folder/route/'metrics.jsonl').open('x',buffering=1) as stream:
                    for i in range(32):
                        check();row=trainer.step();rows.append(row);stream.write(json.dumps(row,allow_nan=False)+'\n')
                        if (i+1)%8==0:heartbeat(route+'-32timing',completed_updates=i+1)
                for a,b in zip(rows[:4],gate['histories'][0],strict=True):
                    if any(not equal_state(a[k],b[k]) for k in ('loss','gradient_norm','token_digest','source_teachers')):raise ValueError('Actual32 and restart trajectories differ')
                path=folder/route/'timing.pt';saved=trainer.save(path)
                if not finite_state(torch.load(path,map_location='cpu',weights_only=False)):raise ValueError('Finite actual source CUDA checkpoint required')
                count=trainer.supervised_tokens-parent['supervised_tokens'];teachers+=count
                result['timings'][route]=dict(histories=rows,verification_teacher_tokens=count,terminal_save_seconds=saved,peak_VRAM_bytes=torch.cuda.max_memory_allocated(),checkpoint=reference(path))
                del trainer;gc.collect();torch.cuda.empty_cache()
            check();elapsed=time.monotonic()-started;measured,forecast=estimate_training(result)
            result.update(passed=True,GPU_seconds=elapsed,verification_teacher_tokens=teachers,verification_updates=80,scientific_teacher_tokens=0,
                stress_weights_discarded_for_science=True,measured_timing=measured,estimated_science_GPU_seconds=forecast,
                estimated_total_GPU_seconds=forecast+elapsed,within1800=forecast+elapsed<=1800,config_sha256=sha256(CONFIG),Base_complete=False)
            atomic_json(folder/'result.json',result);job.update(status='complete',GPU_elapsed_seconds=elapsed,ended_at=now());atomic_json(jp,job)
            print(json.dumps(dict(status='both_source_CUDA_resume_and_timing_complete',GPU_seconds=elapsed,estimated_total_GPU_seconds=forecast+elapsed)))
    except BaseException as exc:
        job.update(status='failed_or_interrupted',error=repr(exc),ended_at=now(),GPU_elapsed_seconds=time.monotonic()-started if started is not None else 0);atomic_json(jp,job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument('--prepare',action='store_true');g.add_argument('--inspect',action='store_true');args=p.parse_args()
    if args.prepare:prepare()
    elif args.inspect:inspect();print('Own news probe frozen; GPU0')
    else:run()
