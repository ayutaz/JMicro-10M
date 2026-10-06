"""Matched512/2048 source quantity at100M teachers each; immutable25M history."""
import argparse
import copy
import gc
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import signal
import statistics
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.japanese_evaluation import NativeLikelihood
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state,restore_rng
from condition_positive_trainer import PositiveTrainView,ConditionQuotaSampler,ConditionPositiveTrainer
from cached_three_source_index import CachedThreeSourceIndex
from phase6_performance import alive,identity
from run_eos_short_pilot import equal_state
import run_condition_diversity_comparison as prior
import run_condition_source_ranking as ranking
import run_complete_text_comparison as evaluation

RUN=ROOT/'reports/phase6/condition-source-learning-100m-20261006'
CONFIG=ROOT/'configs/phase6/condition_source_learning_100m.json'
PROBE_CONFIG=ROOT/'configs/phase6/condition_source_learning_probe.json'
PROPOSAL=ROOT/'reports/phase6/condition_source_learning_100m_proposal.json'
TOTAL=100000000
CEILING=1200
ARMS=('small512','large2048')
GOALS=dict(web=75000000,story=5000000,ordinary_textbook=10000000,conditional_textbook=10000000)
KIND='nested_condition_source_quantity_at_100M'
SOURCES=tuple(dict.fromkeys(('scripts/run_condition_source_learning.py','scripts/run_condition_source_learning.ps1',
    'scripts/review_condition_source_learning.py',*prior.SOURCES,*ranking.SOURCES)))
reference,check_reference=prior.reference,prior.check_reference
latest,reconcile,resume_gate,detail=prior.latest,prior.reconcile,prior.resume_gate,prior.detail


def source_contract():
    old,base,parent,_,_,_,_,large,small=prior.source_contract()
    job=read_json(prior.RUN/'job.json'); reviewed=read_json(prior.RUN/'review.json'); p=read_json(PROPOSAL)
    rjob=read_json(ranking.RUN/'job.json'); rr=read_json(ranking.RUN/'review.json')
    if (job['status']!='complete' or alive(job) or rjob['status']!='complete' or alive(rjob)
            or reviewed['result_sha256']!=sha256(prior.RUN/'compare-result.json')
            or rr['result_sha256']!=sha256(ranking.RUN/'result.json')
            or p['teachers_each']!=TOTAL or p['new_scientific_teacher_tokens']!=2*TOTAL
            or p['GPU_ceiling_seconds']!=CEILING or p['source_teacher_tokens_each']!=GOALS
            or p['outcome_weight']!=1 or p['peak_lr']!=.0002 or p['parent']!=old['parent']
            or p['data']['small512']!=old['positive_data']
            or p['data']['large2048']!=dict(path=str(large.directory),manifest_sha256=large.manifest_sha256)
            or p['protected_test_used'] or p['Base_adopted'] or p['Chat_started'] or p['quantization_started']):
        raise ValueError('Completed25M/128source diagnostic and finite100M proposal required')
    for key in ('ranking_evidence','fit_evidence','previous25M_review'): check_reference(p[key])
    return old,base,parent,dict(small512=small,large2048=large)


def ordinary_stream_digest(pool,positive,check=lambda:None):
    sampler=ConditionQuotaSampler(pool,positive,GOALS,1024,42); names=('web','story','ordinary_textbook')
    hashes={g:hashlib.sha256() for g in names}; pending=[]
    for genre in names:
        block=sampler.streams[genre].block
        def observed(context,block=block,genre=genre):
            x,y=block(context);pending.append((genre,y));return x,y
        sampler.streams[genre].block=observed
    while sampler.source_teachers!=GOALS:
        check();sampler.batch(32)
        for genre,y in pending: hashes[genre].update(y[y!=-100].astype('<u2').tobytes())
        pending.clear()
    return dict(target_sha256={g:hashes[g].hexdigest() for g in names},teachers={g:sampler.source_teachers[g] for g in names},
        EOS={g:sampler.source_eos[g] for g in names},body_bytes={g:sampler.source_body_bytes[g] for g in names},
        physical_inputs=sampler.source_tokens.copy(),total_updates=sampler.position)


def prepare_probe():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    old,_,_,data=source_contract(); check_reference(old['accepted_compact_index'])
    pool=TrainView(old['pool']['pool'],old['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
    if not pool.index.cache_reused:raise ValueError('Original13GB index must not be reparsed')
    audit_path=RUN/'ordinary-stream-audit.json'
    if audit_path.exists():raise ValueError('Preparation exists; inspect partial evidence instead of rerolling')
    started=time.monotonic()
    def check():
        if time.monotonic()-started>30:raise TimeoutError('CPU30s ordinary target audit exhausted')
    left=ordinary_stream_digest(pool,data['small512'],check);right=ordinary_stream_digest(pool,data['large2048'],check)
    checks={k:left[k]==right[k] for k in ('target_sha256','teachers','EOS','body_bytes')}
    if not all(checks.values()):raise ValueError('Expanded source changed ordinary supervised targets')
    atomic_json(audit_path,dict(small=left,large=right,checks=checks,CPU_seconds=time.monotonic()-started,CPU_limit_seconds=30,
        goals=GOALS,small_manifest_sha256=data['small512'].manifest_sha256,large_manifest_sha256=data['large2048'].manifest_sha256,
        scientific_teacher_tokens=0,actual_GPU_seconds=0,script_sha256=sha256(Path(__file__))))
    c=dict(research_kind=KIND,phase='probe',parent=old['parent'],original_config=old['original_config'],pool=old['pool'],
        accepted_compact_index=old['accepted_compact_index'],data={a:dict(path=str(d.directory),manifest_sha256=d.manifest_sha256) for a,d in data.items()},
        arms={a:GOALS for a in ARMS},outcome_weights={a:1 for a in ARMS},teachers_per_arm=TOTAL,new_scientific_teacher_tokens=2*TOTAL,
        peak_lr=.0002,optimizer_policy='inherit',shapes=old['shapes'],GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=CEILING,
        sampler_policy='Fresh explicit four-stream seed42 fork from common2B+20M parent; original3 supervised sequences equal, nested512/2048 conditional IDs/interleaving differ. Prior25M terminal quotas are historical, not new100M control.',
        loss='ordinary original body+EOS CE, outcome weight1',
        references=dict(proposal=reference(PROPOSAL),ordinary_stream_audit=reference(audit_path),
            previous25M_config=reference(prior.CONFIG),previous25M_result=reference(prior.RUN/'compare-result.json'),
            previous25M_review=reference(prior.RUN/'review.json'),source_ranking_config=reference(ranking.CONFIG),
            source_cases=reference(ranking.RUN/'cases.json'),source_ranking_review=reference(ranking.RUN/'review.json'),
            source_fit=reference(ROOT/'reports/phase6/condition_source_ranking_fit_analysis.json')),
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},implementation=implementation_hashes(),
        quality_criteria_unchanged=True,old_numerical7_preserved=True,Base_adopted=False,Chat_adopted=False,protected_test_used=False,
        requested_five_steps_complete=False,scientific_teacher_tokens=0,created_at=now())
    scope(c);atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print(json.dumps(dict(status='both100M_probe_frozen_ordinary_targets_identical',checks=checks,CPU_seconds=time.monotonic()-started)),flush=True)


def scope(c):
    if (c['research_kind']!=KIND or c['arms']!={a:GOALS for a in ARMS} or c['outcome_weights']!={a:1 for a in ARMS}
            or c['teachers_per_arm']!=TOTAL or c['new_scientific_teacher_tokens']!=2*TOTAL or c['total_new_GPU_ceiling_seconds']!=CEILING
            or c['peak_lr']!=.0002 or c['optimizer_policy']!='inherit'
            or c['shapes']!=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16')
            or c['loss']!='ordinary original body+EOS CE, outcome weight1' or c['Base_adopted'] or c['Chat_adopted']
            or c['protected_test_used'] or c['requested_five_steps_complete'] or not c['quality_criteria_unchanged']):
        raise ValueError('Matched100M source-only ordinaryCE Base scope differs')


def inspect(path):
    c=read_json(path);scope(c);old,base,parent,data=source_contract()
    if c['implementation']!=implementation_hashes() or c['source_sha256']!={p:sha256(ROOT/p) for p in SOURCES}:raise ValueError('Frozen source differs')
    for ref in (*c['references'].values(),c['parent'],c['original_config'],c['accepted_compact_index']):check_reference(ref)
    if (c['parent']!=old['parent'] or c['pool']!=old['pool'] or c['shapes']!=old['shapes']
            or any(c['data'][a]!=dict(path=str(data[a].directory),manifest_sha256=data[a].manifest_sha256) for a in ARMS)):
        raise ValueError('Actual same parent/material differs')
    folder=RUN/'probe' if path==PROBE_CONFIG else RUN
    if (folder/'job.json').exists() and alive(read_json(folder/'job.json')):raise ValueError('Existing actual GPU job live; no duplicate')
    if path==PROBE_CONFIG:
        if c['phase']!='probe' or c['GPU_budget_seconds']!=120:raise ValueError('Probe scope differs')
    elif path==CONFIG:
        measured=probe_evidence();timing,estimate=estimate_training(measured)
        if (c['phase']!='scientific' or c['probe_config_sha256']!=sha256(PROBE_CONFIG)
                or c['probe_result_sha256']!=sha256(RUN/'probe/result.json') or c['measured_timings']!=timing
                or c['verification_teacher_tokens']!=measured['verification_teacher_tokens'] or c['verification_GPU_seconds']!=measured['GPU_seconds']
                or c['estimated_GPU_seconds_with_margin']!=estimate or estimate+measured['GPU_seconds']>CEILING
                or not math.isclose(c['GPU_budget_seconds']+measured['GPU_seconds'],CEILING,abs_tol=1e-9)):
            raise ValueError('Actual measured bounded budget differs')
    else:raise ValueError('Only frozen100M study configs allowed')
    return c,base,parent,data


def probe_evidence():
    job=read_json(RUN/'probe/job.json');r=read_json(RUN/'probe/result.json')
    if (job['status']!='complete' or alive(job) or not r['passed'] or r['config_sha256']!=sha256(PROBE_CONFIG)
            or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or r['GPU_seconds']>120 or set(r['gates'])!=set(ARMS)
            or any(not g['passed'] or not all(g['checks'].values()) for g in r['gates'].values())):
        raise ValueError('Actual both100M CUDA resume/timing required')
    return r


def estimate_training(measured):
    timing={};total=0.
    for arm in ARMS:
        record=measured['timings'][arm];rows=record['histories']
        if len(rows)!=32 or any(not math.isfinite(r['seconds']) or r['seconds']<=0 for r in rows):raise ValueError('Both actual32 continuous timing updates required')
        step=statistics.median(r['seconds'] for r in rows[8:]);teachers=record['verification_teacher_tokens']/32
        updates=math.ceil(TOTAL/teachers);warm=max(0.,sum(r['seconds'] for r in rows[:8])-8*step)
        save=(math.ceil(updates/250)+1)*record['terminal_save_seconds'];seconds=updates*step+warm+save;total+=seconds
        timing[arm]=dict(steady_step_seconds=step,teachers_per_update=teachers,estimated_updates=updates,warmup_seconds=warm,
            save_seconds=save,estimated_training_seconds=seconds)
    return timing,total*1.3+600+20  # Two complete evaluations plus fixed source128 requests per weight.


def freeze():
    if CONFIG.exists():inspect(CONFIG);return
    c,*_=inspect(PROBE_CONFIG);c=copy.deepcopy(c);r=probe_evidence();timing,estimate=estimate_training(r)
    if estimate+r['GPU_seconds']>CEILING:raise ValueError('Measured comparison exceeds unchanged1200s; no science launched')
    c.update(phase='scientific',probe_config_sha256=sha256(PROBE_CONFIG),probe_result_sha256=sha256(RUN/'probe/result.json'),
        verification_GPU_seconds=r['GPU_seconds'],verification_teacher_tokens=r['verification_teacher_tokens'],
        GPU_budget_seconds=CEILING-r['GPU_seconds'],measured_timings=timing,estimated_GPU_seconds_with_margin=estimate,save_every_updates=250)
    atomic_json(CONFIG,c);inspect(CONFIG);print(json.dumps(dict(status='measured_both100M_frozen',timings=timing,estimate=estimate)),flush=True)


def binding(c,path,arm):
    return dict(config_sha256=sha256(path),arm=arm,parent=c['parent'],short_manifest_sha256=c['pool']['manifest_sha256'],teacher_goals=GOALS,
        optimizer_policy='inherit',peak_lr=.0002,loss=c['loss'],study_kind=KIND,sampler_policy=c['sampler_policy'],outcome_weight=1,
        positive_manifest_sha256=c['data'][arm]['manifest_sha256'])


def trainer_for(parent,pool,positive,b,device='cuda',context=1024,batch=32):
    trainer=ConditionPositiveTrainer(parent,pool,positive,GOALS,1,b,device,context,batch);trainer.spec['research_kind']=KIND
    trainer.lineage.update(kind='explicit-nested-condition-source-100M-constant-LR-fork',
        source_sampler_policy='New100M four-stream seed42 fork; original3 targets equal across arms, nested conditional differs; common original parent cursor retained, not25M continuation.')
    return trainer


def source_fit(rows,prepared):
    keyed={r['index']:r for r in rows};families={r['index']:r for r in prepared['families']};out={}
    for mode in ranking.MODES:
        out[mode]={}
        for subset in ('all128','nonweak116','old512_fixed64','new1536_fixed64'):
            selected=[c for c in prepared['cases'] if c['mode']==mode and c['candidate']==c['source_matching_label']
                and (subset=='all128' or subset=='nonweak116' and not families[c['family']]['content_annotation']['weak_pair'] or c['group']==subset)]
            scored=[keyed[c['index']] for c in selected];tokens=sum(r['target_tokens'] for r in scored);nll=-sum(r['log_likelihood'] for r in scored)
            out[mode][subset]=dict(outcomes=len(scored),target_tokens=tokens,NLL_sum=nll,token_weighted_mean_NLL=nll/tokens)
    return out


def rank_sources(c,arm,trained,heartbeat,check):
    folder=RUN/'source-ranking'/arm;terminal=folder/'result.json';cfg=sha256(CONFIG);cases_sha=c['references']['source_cases']['sha256']
    check_reference(dict(path=trained['checkpoint'],sha256=trained['checkpoint_sha256']))
    if terminal.exists():
        saved=read_json(terminal)
        if saved['config_sha256']!=cfg or saved['checkpoint_sha256']!=trained['checkpoint_sha256'] or saved['cases_sha256']!=cases_sha:
            raise ValueError('Saved source ranking binding differs')
        return saved
    prepared=read_json(Path(c['references']['source_cases']['path']));before_rng=rng_state()
    state=torch.load(trained['checkpoint'],map_location='cpu',weights_only=False);model=JMicroModel(state['model_config']).to('cuda').eval();model.load_state_dict(state['model'],strict=True)
    before={k:v.detach().cpu().clone() for k,v in model.state_dict().items()};scorer=NativeLikelihood(model,None,'cuda','bf16',16)
    hook=model.register_forward_pre_hook(lambda *_:check());rows=[]
    try:
        with sdpa_kernel(SDPBackend.MATH):
            for start in range(0,1024,16):
                cases=prepared['cases'][start:start+16];path=folder/f'{start:04d}.json';check()
                if path.exists():
                    saved=read_json(path)
                    if saved['config_sha256']!=cfg or saved['checkpoint_sha256']!=trained['checkpoint_sha256'] or saved['cases_sha256']!=cases_sha:
                        raise ValueError('Saved source request binding differs')
                    scored=saved['rows']
                else:
                    scored=[dict(index=case['index'],**r) for case,r in zip(cases,scorer.score_encoded(cases),strict=True)]
                    ranking.validate_scores(scored,cases);atomic_json(path,dict(config_sha256=cfg,checkpoint_sha256=trained['checkpoint_sha256'],cases_sha256=cases_sha,rows=scored))
                ranking.validate_scores(scored,cases);rows.extend(scored);heartbeat(arm+'-source128',completed_requests=len(rows),total_requests=1024)
        checks=dict(weights_unchanged=all(torch.equal(before[k],v.detach().cpu()) for k,v in model.state_dict().items()),no_gradients=all(p.grad is None for p in model.parameters()),eval_mode=not model.training)
    finally:
        hook.remove();restore_rng(before_rng)
    checks['RNG_restored']=equal_state(before_rng,rng_state())
    if not all(checks.values()):raise ValueError('Read-only source scoring changed weights/RNG')
    result=dict(config_sha256=cfg,checkpoint_sha256=trained['checkpoint_sha256'],cases_sha256=cases_sha,checks=checks,
        summary=ranking.summarize([dict(checkpoint=arm,**r) for r in rows],prepared,arms=(arm,)),original_outcome_fit=source_fit(rows,prepared),
        evaluated_requests=1024,optimizer_updates=0,scientific_teacher_tokens=0,protected_test_used=False,
        source_matching_is_not_certified_negative_accuracy=True)
    atomic_json(terminal,result);del state,model,before,scorer;gc.collect();torch.cuda.empty_cache();return result


def run(probe=False):
    path=PROBE_CONFIG if probe else CONFIG;c,base,parent,data=inspect(path);output=RUN/'probe' if probe else RUN;output.mkdir(parents=True,exist_ok=True)
    jp=output/'job.json';old=read_json(jp) if jp.exists() else {}
    if old and old['config_sha256']!=sha256(path):raise ValueError('Prior job binding differs')
    if old.get('status')=='complete':print('Complete job retained; no duplicate GPU');return
    prior_seconds=old.get('GPU_elapsed_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(path),started_at=old.get('started_at',now()),GPU_elapsed_seconds=prior_seconds,
        Base_adopted=False,protected_test_used=False,restart_command=f"scripts/run_condition_source_learning.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Interrupted; completed updates/requests retained')
        if started[0] is not None and prior_seconds+time.monotonic()-started[0]>c['GPU_budget_seconds']:raise TimeoutError('Cumulative GPU1200s comparison budget exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_elapsed_seconds']=prior_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);heartbeat('setup')
        for rel in (*SOURCES,*c['implementation'],path.relative_to(ROOT).as_posix()):
            dest=output/'source'/rel;dest.parent.mkdir(parents=True,exist_ok=True)
            if dest.exists() and dest.read_bytes()!=(ROOT/rel).read_bytes():raise ValueError('Frozen source snapshot differs')
            if not dest.exists():shutil.copyfile(ROOT/rel,dest)
        check_reference(c['accepted_compact_index']);pool=TrainView(c['pool']['pool'],c['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
        if not pool.index.cache_reused:raise ValueError('Index must be reused')
        with gpu_lock('cuda'):
            started[0]=time.monotonic();heartbeat('gpu')
            if probe:
                result=dict(status='actual_both100M_resume_timing_complete',gates={},timings={},config_sha256=sha256(path),scientific_teacher_tokens=0,weights_discarded_for_science=True)
                for arm in ARMS:
                    b=binding(c,path,arm)
                    def build():return trainer_for(parent,pool,data[arm],b)
                    gate=resume_gate(build,output/arm/'resume-gate',sha256(path),check);result['gates'][arm]=gate
                    folder=output/arm/'timing';folder.mkdir(parents=True,exist_ok=True);trainer=build();cp=latest(folder)
                    if cp is not None:trainer.load(cp)
                    log=folder/'metrics.jsonl';reconcile(log,trainer.update,parent['update'])
                    with log.open('a',buffering=1) as stream:
                        while trainer.update-parent['update']<32:
                            try:check()
                            except (InterruptedError,TimeoutError):trainer.save(folder/'checkpoint.pt');raise
                            row=trainer.step();stream.write(json.dumps(row,allow_nan=False)+'\n')
                            if trainer.sampler.position%8==0:heartbeat(arm+'-timing',completed_updates=trainer.sampler.position)
                    cp=folder/'checkpoint.pt';saved_seconds=trainer.save(cp);rows=[json.loads(s) for s in log.read_text().splitlines()]
                    if any(not equal_state(row[k],ref[k]) for row,ref in zip(rows[:4],gate['histories'][0],strict=True) for k in ('loss','gradient_norm','lr','token_digest','source_teachers')):
                        raise ValueError('Gate/timing trajectories differ')
                    result['timings'][arm]=dict(histories=rows,verification_teacher_tokens=trainer.supervised_tokens-parent['supervised_tokens'],terminal_save_seconds=saved_seconds,checkpoint=str(cp),checkpoint_sha256=sha256(cp))
                    del trainer;gc.collect();torch.cuda.empty_cache()
                result.update(passed=True,verification_teacher_tokens=sum(g['verification_teacher_tokens'] for g in result['gates'].values())+sum(t['verification_teacher_tokens'] for t in result['timings'].values()),GPU_optimizer_updates=80)
            else:
                progress=output/'progress-result.json';result=read_json(progress) if progress.exists() else dict(checkpoints={},evaluations={},source_rankings={})
                for arm in ARMS:
                    b=binding(c,path,arm)
                    if arm not in result['checkpoints']:
                        folder=output/arm/'training';folder.mkdir(parents=True,exist_ok=True);trainer=trainer_for(parent,pool,data[arm],b);cp=latest(folder)
                        if cp is not None:trainer.load(cp)
                        log=folder/'metrics.jsonl';seconds=reconcile(log,trainer.update,parent['update'])
                        with log.open('a',buffering=1) as stream:
                            while trainer.sampler.source_teachers!=GOALS:
                                try:check()
                                except (InterruptedError,TimeoutError):trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt');raise
                                row=trainer.step();seconds+=row['seconds'];stream.write(json.dumps(row,allow_nan=False)+'\n')
                                if trainer.sampler.position%20==0:heartbeat(arm+'-training',teachers=row['additional_teacher_tokens'],teacher_budget=TOTAL,source_teachers=row['source_teachers'],loss=row['loss'])
                                if trainer.sampler.position%250==0:trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt')
                        cp=folder/f'checkpoint-{trainer.update:08d}.pt';trainer.save(cp);result['checkpoints'][arm]=detail(trainer,cp,b,seconds);atomic_json(progress,result)
                        del trainer;gc.collect();torch.cuda.empty_cache()
                    if arm not in result['evaluations']:
                        evaluation.RUN=output/'evaluation';dev=Shard(Path(base['dev_shards']),'dev');tok=Tokenizer(ROOT/base['tokenizer'])
                        result['evaluations'][arm]=evaluation.evaluate(arm,result['checkpoints'][arm],dev,tok,base,b,heartbeat,check,started[0]+c['GPU_budget_seconds']-prior_seconds);atomic_json(progress,result)
                    if arm not in result['source_rankings']:
                        result['source_rankings'][arm]=rank_sources(c,arm,result['checkpoints'][arm],heartbeat,check);atomic_json(progress,result)
                result.update(status='actual_both100M_complete_pending_all160_content',config_sha256=sha256(path),scientific_teacher_tokens=2*TOTAL,
                    verification_teacher_tokens=c['verification_teacher_tokens'],verification_GPU_seconds=c['verification_GPU_seconds'],ordinary_stream_audit=c['references']['ordinary_stream_audit'],
                    Base_adopted=False,Chat_adopted=False,protected_test_used=False,requested_five_steps_complete=False)
            check();elapsed=prior_seconds+time.monotonic()-started[0];result['GPU_seconds']=elapsed;job.update(status='complete',stage='complete',completed_at=now(),GPU_elapsed_seconds=elapsed)
            atomic_json(output/('result.json' if probe else 'compare-result.json'),result)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_elapsed_seconds']=prior_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();modes=p.add_mutually_exclusive_group()
    for mode in ('prepare-probe','preflight-probe','probe','freeze','inspect'):modes.add_argument('--'+mode,action='store_true')
    args=p.parse_args()
    if args.prepare_probe:prepare_probe()
    elif args.preflight_probe:inspect(PROBE_CONFIG)
    elif args.freeze:freeze()
    elif args.inspect:inspect(CONFIG)
    else:run(args.probe)
