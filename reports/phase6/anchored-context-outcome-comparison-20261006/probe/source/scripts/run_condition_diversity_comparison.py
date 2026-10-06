"""Nested512->2048 ordinary CE25M; reuse the completed512 control exactly."""
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
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,implementation_hashes,gpu_lock
from condition_positive_trainer import PositiveTrainView,ConditionQuotaSampler,ConditionPositiveTrainer
from cached_three_source_index import CachedThreeSourceIndex
from phase6_performance import alive,identity
from run_eos_short_pilot import equal_state
import run_condition_positive_comparison as prior
import run_complete_text_comparison as evaluation

RUN=ROOT/'reports/phase6/condition-diversity-comparison-20261006'
CONFIG=ROOT/'configs/phase6/condition_diversity_comparison.json'
PROBE_CONFIG=ROOT/'configs/phase6/condition_diversity_probe.json'
PREPARATION=ROOT/'reports/phase6/condition_diversity_teacher_preparation.json'
PROPOSAL=ROOT/'reports/phase6/condition_diversity_comparison_proposal.json'
TOTAL=25000000
CEILING=900
ARM='large2048'
GOALS=prior.QUOTAS.copy()
SOURCES=tuple(dict.fromkeys(('scripts/run_condition_diversity_comparison.py','scripts/run_condition_diversity_comparison.ps1',
    'scripts/review_condition_diversity_comparison.py',*prior.SOURCES)))
reference,check_reference=prior.reference,prior.check_reference
latest,reconcile,resume_gate,detail=prior.latest,prior.reconcile,prior.resume_gate,prior.detail


def control_contract():
    c,base,parent=prior.inspect(prior.CONFIG)
    job=read_json(prior.RUN/'job.json'); result=read_json(prior.RUN/'compare-result.json'); review=read_json(prior.RUN/'review.json')
    control=result['checkpoints']['control']; ev=result['evaluations']['control']; summary=review['summaries']['control']
    notes=ROOT/'reports/phase6/condition_positive_control_notes.json'
    if (job['status']!='complete' or alive(job) or result['config_sha256']!=sha256(prior.CONFIG)
            or review['result_sha256']!=sha256(prior.RUN/'compare-result.json')
            or control['additional_supervised_tokens']!=TOTAL or control['outcome_weight']!=1
            or control['source_teachers']!=GOALS or ev['binding']!=control['binding']
            or ev['checkpoint_sha256']!=control['checkpoint_sha256']
            or summary['notes_sha256']!=sha256(notes)
            or summary['generation_sha256']!=sha256(prior.RUN/'evaluation/control/evaluation/generation.json')
            or review['protected_test_used'] or result['protected_test_used']):
        raise ValueError('Actual reviewed same-parent25M weight1 control required')
    check_reference(dict(path=control['checkpoint'],sha256=control['checkpoint_sha256']))
    return c,base,parent,control,ev


def source_contract():
    old,base,parent,control,ev=control_contract(); prep=read_json(PREPARATION); proposal=read_json(PROPOSAL)
    review_path=ROOT/'reports/phase6/condition-diversity-source-20261006/content-review.json'; review=read_json(review_path)
    if (prep['documents']!=2048 or prep['scientific_teacher_tokens']!=0 or prep['actual_GPU_seconds']!=0
            or prep['protected_test_used'] or not all(prep['nested_small_actual_checks'].values())
            or not review['all64_read'] or not review['training_pool_accepted'] or review['weak_pairs']>10
            or review['source_pairs_sha256']!=sha256(review_path.parent/'source-pairs.json')
            or review['notes_sha256']!=sha256(review_path.parent/'content-notes.tsv')
            or proposal['learning']['additional_teachers_each']!=TOTAL
            or proposal['learning']['outcome_weight_each']!=1 or proposal['GPU_ceiling_seconds']!=CEILING
            or proposal['large_manifest_sha256']!=prep['manifest_sha256']):
        raise ValueError('Accepted nested2048 source/unchanged comparison required')
    positive=PositiveTrainView(prep['data_path'],prep['manifest_sha256'])
    small=PositiveTrainView(old['positive_data']['path'],old['positive_data']['manifest_sha256'])
    if (positive.manifest['documents']!=2048 or positive.manifest['nested_small_manifest_sha256']!=small.manifest_sha256
            or not np.array_equal(positive.tokens[:len(small.tokens)],small.tokens)
            or not np.array_equal(positive.focus[:len(small.focus)],small.focus)
            or positive.manifest['metadata'][:512]!=small.manifest['metadata']):
        raise ValueError('Actual nested original512 data changed')
    return old,base,parent,control,ev,prep,review_path,positive,small


def ordinary_stream_digest(pool, positive, check=lambda:None):
    """Replay sampler only; hash every original ordinary label after terminal masks."""
    sampler=ConditionQuotaSampler(pool,positive,GOALS,1024,42)
    names=('web','story','ordinary_textbook'); hashes={g:hashlib.sha256() for g in names}; pending=[]
    for genre in names:
        block=sampler.streams[genre].block
        def observed(context, block=block, genre=genre):
            x,y=block(context); pending.append((genre,y)); return x,y
        sampler.streams[genre].block=observed
    while sampler.source_teachers!=GOALS:
        check(); sampler.batch(32)
        for genre,y in pending: hashes[genre].update(y[y!=-100].astype('<u2').tobytes())
        pending.clear()
    return dict(target_sha256={g:hashes[g].hexdigest() for g in names},
        teachers={g:sampler.source_teachers[g] for g in names},EOS={g:sampler.source_eos[g] for g in names},
        body_bytes={g:sampler.source_body_bytes[g] for g in names},physical_inputs=sampler.source_tokens.copy(),
        total_updates=sampler.position)


def prepare_probe():
    if PROBE_CONFIG.exists(): inspect(PROBE_CONFIG); return
    old,base,parent,control,ev,prep,review_path,positive,small=source_contract()
    check_reference(old['accepted_compact_index']); pool=TrainView(old['pool']['pool'],old['pool']['manifest_sha256'])
    pool.index=CachedThreeSourceIndex(pool)
    if not pool.index.cache_reused: raise ValueError('Original index may not be reparsed')
    started=time.monotonic()
    def check():
        if time.monotonic()-started>30: raise TimeoutError('CPU30s common ordinary-stream audit exhausted')
    audit_path=RUN/'ordinary-stream-audit.json'
    if audit_path.exists(): raise ValueError('Partial preparation/audit retained; inspect before repairing')
    left=ordinary_stream_digest(pool,small,check); right=ordinary_stream_digest(pool,positive,check)
    checks={k:left[k]==right[k] for k in ('target_sha256','teachers','EOS','body_bytes')}
    if not all(checks.values()): raise ValueError('Expanded source changed an ordinary supervised stream')
    atomic_json(audit_path,dict(small=left,large=right,checks=checks,CPU_seconds=time.monotonic()-started,
        CPU_limit_seconds=30,small_manifest_sha256=small.manifest_sha256,large_manifest_sha256=positive.manifest_sha256,
        scientific_teacher_tokens=0,actual_GPU_seconds=0,script_sha256=sha256(Path(__file__))))
    c=dict(research_kind='nested_condition_source_quantity',phase='probe',parent=old['parent'],
        original_config=old['original_config'],pool=old['pool'],accepted_compact_index=old['accepted_compact_index'],
        small_data=old['positive_data'],positive_data=dict(path=prep['data_path'],manifest_sha256=prep['manifest_sha256']),
        arms={ARM:GOALS},outcome_weights={ARM:1},teachers_per_new_arm=TOTAL,total_comparison_teachers=2*TOTAL,
        peak_lr=.0002,optimizer_policy='inherit',shapes=old['shapes'],GPU_budget_seconds=120,total_new_GPU_ceiling_seconds=CEILING,
        sampler_policy='Same ordinary3 supervised target sequences; nested2048 conditional shuffle replaces512; same seed42, quotas, original full body+EOS CE. Batch interleaving/conditional IDs intentionally differ.',
        loss='ordinary original body+EOS CE, outcome weight1',probe_updates=dict(resume=8,continuous_timing=32,timing_warmup=8),
        references=dict(preparation=reference(PREPARATION),proposal=reference(PROPOSAL),content_review=reference(review_path),
            ordinary_stream_audit=reference(audit_path),control_config=reference(prior.CONFIG),control_result=reference(prior.RUN/'compare-result.json'),
            control_review=reference(prior.RUN/'review.json'),control_notes=reference(ROOT/'reports/phase6/condition_positive_control_notes.json')),
        reused_control_checkpoint=dict(path=control['checkpoint'],sha256=control['checkpoint_sha256']),
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},implementation=implementation_hashes(),
        quality_criteria_unchanged=True,old_numerical7_preserved=True,Base_adopted=False,Chat_adopted=False,
        protected_test_used=False,requested_five_steps_complete=False,scientific_teacher_tokens=0,created_at=now())
    scope(c); atomic_json(PROBE_CONFIG,c); inspect(PROBE_CONFIG)
    print(json.dumps(dict(status='probe_frozen_CPU_ordinary_streams_identical',audit=checks,CPU_seconds=time.monotonic()-started)),flush=True)


def scope(c):
    if (c['research_kind']!='nested_condition_source_quantity' or c['arms']!={ARM:GOALS} or c['outcome_weights']!={ARM:1}
            or c['teachers_per_new_arm']!=TOTAL or c['total_comparison_teachers']!=2*TOTAL
            or c['total_new_GPU_ceiling_seconds']!=CEILING or c['peak_lr']!=.0002 or c['optimizer_policy']!='inherit'
            or c['shapes']!=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16')
            or c['loss']!='ordinary original body+EOS CE, outcome weight1'
            or c['Base_adopted'] or c['Chat_adopted'] or c['protected_test_used'] or c['requested_five_steps_complete']
            or not c['quality_criteria_unchanged']): raise ValueError('Same-teacher weight1 Base-only comparison differs')


def inspect(path):
    c=read_json(path); scope(c); old,base,parent,control,ev,prep,_,positive,_=source_contract()
    if c['implementation']!=implementation_hashes() or c['source_sha256']!={p:sha256(ROOT/p) for p in SOURCES}:
        raise ValueError('Frozen comparison source differs')
    for ref in (*c['references'].values(),c['parent'],c['original_config'],c['accepted_compact_index'],c['reused_control_checkpoint']): check_reference(ref)
    if (c['parent']!=old['parent'] or c['pool']!=old['pool'] or c['shapes']!=old['shapes']
            or c['small_data']!=old['positive_data'] or c['positive_data']!=dict(path=prep['data_path'],manifest_sha256=prep['manifest_sha256'])
            or c['reused_control_checkpoint']!=dict(path=control['checkpoint'],sha256=control['checkpoint_sha256'])):
        raise ValueError('Actual parent/material/control binding differs')
    folder=RUN/'probe' if path==PROBE_CONFIG else RUN
    if (folder/'job.json').exists() and alive(read_json(folder/'job.json')): raise ValueError('Existing comparison live; do not duplicate')
    if path==PROBE_CONFIG:
        if c['phase']!='probe' or c['GPU_budget_seconds']!=120: raise ValueError('Probe scope differs')
    elif path==CONFIG:
        measured=probe_evidence(); timing,estimate=estimate_training(measured)
        if (c['phase']!='scientific' or c['probe_config_sha256']!=sha256(PROBE_CONFIG)
                or c['probe_result_sha256']!=sha256(RUN/'probe/result.json')
                or c['verification_teacher_tokens']!=measured['verification_teacher_tokens']
                or c['verification_GPU_seconds']!=measured['GPU_seconds'] or c['measured_timing']!=timing
                or c['estimated_GPU_seconds_with_margin']!=estimate
                or not math.isclose(c['GPU_budget_seconds']+measured['GPU_seconds'],CEILING,abs_tol=1e-9)
                or estimate+measured['GPU_seconds']>CEILING): raise ValueError('Actual measured science budget differs')
    else: raise ValueError('Only frozen comparison configs accepted')
    return c,base,parent,control,ev,positive


def probe_evidence():
    job=read_json(RUN/'probe/job.json'); result=read_json(RUN/'probe/result.json')
    if (job['status']!='complete' or alive(job) or not result['passed'] or result['config_sha256']!=sha256(PROBE_CONFIG)
            or result['GPU_seconds']!=job['GPU_elapsed_seconds'] or result['GPU_seconds']>120
            or not result['gate']['passed'] or not all(result['gate']['checks'].values())):
        raise ValueError('Actual2048 CUDA resume/timing incomplete')
    return result


def estimate_training(measured):
    record=measured['timing']; rows=record['histories']
    if len(rows)!=32 or any(not math.isfinite(r['seconds']) or r['seconds']<=0 for r in rows): raise ValueError('Actual32 timing updates required')
    step=statistics.median(r['seconds'] for r in rows[8:]); teachers=record['verification_teacher_tokens']/32
    updates=math.ceil(TOTAL/teachers); warm=max(0.,sum(r['seconds'] for r in rows[:8])-8*step)
    save=(math.ceil(updates/250)+1)*record['terminal_save_seconds']; total=updates*step+warm+save
    return dict(steady_step_seconds=step,teachers_per_update=teachers,estimated_updates=updates,
        warmup_seconds=warm,save_seconds=save,estimated_training_seconds=total),total*1.3+300


def freeze():
    if CONFIG.exists(): inspect(CONFIG); return
    c,*_=inspect(PROBE_CONFIG); c=copy.deepcopy(c); measured=probe_evidence(); timing,estimate=estimate_training(measured)
    if estimate+measured['GPU_seconds']>CEILING: raise ValueError('Actual study cannot fit900s; retain measurement')
    c.update(phase='scientific',probe_config_sha256=sha256(PROBE_CONFIG),probe_result_sha256=sha256(RUN/'probe/result.json'),
        verification_GPU_seconds=measured['GPU_seconds'],verification_teacher_tokens=measured['verification_teacher_tokens'],
        GPU_budget_seconds=CEILING-measured['GPU_seconds'],measured_timing=timing,estimated_GPU_seconds_with_margin=estimate,save_every_updates=250)
    atomic_json(CONFIG,c); inspect(CONFIG); print(json.dumps(dict(status='measured2048_science_frozen',timing=timing,estimate=estimate)),flush=True)


def binding(c,path):
    return dict(config_sha256=sha256(path),arm=ARM,parent=c['parent'],short_manifest_sha256=c['pool']['manifest_sha256'],
        teacher_goals=GOALS,optimizer_policy='inherit',peak_lr=.0002,loss=c['loss'],study_kind=c['research_kind'],
        sampler_policy=c['sampler_policy'],outcome_weight=1,positive_manifest_sha256=c['positive_data']['manifest_sha256'])


def trainer_for(parent,pool,positive,b,device='cuda',context=1024,batch=32):
    trainer=ConditionPositiveTrainer(parent,pool,positive,GOALS,1,b,device,context,batch)
    trainer.spec['research_kind']='nested_condition_source_quantity'
    trainer.lineage.update(kind='explicit-nested-condition-source-constant-LR-fork',source_sampler_policy='Original ordinary3 teacher sequences retained; expanded conditional source shuffled with seed42; old parent cursor preserved.')
    return trainer


def run(probe=False):
    path=PROBE_CONFIG if probe else CONFIG; c,base,parent,control,control_ev,positive=inspect(path)
    output=RUN/'probe' if probe else RUN; output.mkdir(parents=True,exist_ok=True)
    jp=output/'job.json'; old=read_json(jp) if jp.exists() else {}
    if old and old['config_sha256']!=sha256(path): raise ValueError('Prior job binding differs')
    if old.get('status')=='complete': print('Completed comparison retained; no duplicate GPU'); return
    prior_seconds=old.get('GPU_elapsed_seconds',0.); started,stopped=[None],[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(path),started_at=old.get('started_at',now()),
        GPU_elapsed_seconds=prior_seconds,Base_adopted=False,protected_test_used=False,
        restart_command=f"scripts/run_condition_diversity_comparison.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    for sig in (signal.SIGINT,signal.SIGTERM): signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]: raise InterruptedError('Interrupted; completed updates retained')
        if started[0] is not None and prior_seconds+time.monotonic()-started[0]>c['GPU_budget_seconds']: raise TimeoutError('Cumulative comparison GPU budget exhausted')
    def heartbeat(stage,**values):
        check(); job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None: job['GPU_elapsed_seconds']=prior_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True); heartbeat('setup')
        for relative in (*SOURCES,*c['implementation'],path.relative_to(ROOT).as_posix()):
            target=output/'source'/relative; target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/relative).read_bytes(): raise ValueError('Source snapshot differs')
            if not target.exists(): shutil.copyfile(ROOT/relative,target)
        check_reference(c['accepted_compact_index']); pool=TrainView(c['pool']['pool'],c['pool']['manifest_sha256']); pool.index=CachedThreeSourceIndex(pool)
        if not pool.index.cache_reused: raise ValueError('Index must be reused')
        b=binding(c,path)
        def build(): return trainer_for(parent,pool,positive,b)
        with gpu_lock('cuda'):
            started[0]=time.monotonic(); heartbeat('gpu')
            if probe:
                gate=resume_gate(build,output/'resume-gate',sha256(path),check)
                folder=output/'timing'; folder.mkdir(parents=True,exist_ok=True); trainer=build(); cp=latest(folder)
                if cp is not None: trainer.load(cp)
                log=folder/'metrics.jsonl'; reconcile(log,trainer.update,parent['update'])
                with log.open('a',buffering=1) as stream:
                    while trainer.update-parent['update']<32:
                        try: check()
                        except (InterruptedError,TimeoutError): trainer.save(folder/'checkpoint.pt'); raise
                        row=trainer.step(); stream.write(json.dumps(row,allow_nan=False)+'\n')
                        if trainer.sampler.position%8==0: heartbeat('timing',completed_updates=trainer.sampler.position)
                cp=folder/'checkpoint.pt'; saved_seconds=trainer.save(cp); rows=[json.loads(s) for s in log.read_text().splitlines()]
                if any(not equal_state(row[k],reference_row[k]) for row,reference_row in zip(rows[:4],gate['histories'][0],strict=True)
                        for k in ('loss','gradient_norm','lr','token_digest','source_teachers')): raise ValueError('Probe trajectories differ')
                timing=dict(histories=rows,verification_teacher_tokens=trainer.supervised_tokens-parent['supervised_tokens'],
                    terminal_save_seconds=saved_seconds,checkpoint=str(cp),checkpoint_sha256=sha256(cp))
                result=dict(status='actual2048_resume_timing_complete',passed=True,gate=gate,timing=timing,
                    config_sha256=sha256(path),verification_teacher_tokens=gate['verification_teacher_tokens']+timing['verification_teacher_tokens'],
                    GPU_optimizer_updates=40,scientific_teacher_tokens=0,weights_discarded_for_science=True)
                del trainer; gc.collect(); torch.cuda.empty_cache()
            else:
                progress=output/'progress-result.json'
                result=read_json(progress) if progress.exists() else dict(checkpoints=dict(control=control),evaluations=dict(control=control_ev))
                if result['checkpoints']['control']!=control or result['evaluations']['control']!=control_ev: raise ValueError('Reused control changed')
                if ARM not in result['checkpoints']:
                    folder=output/ARM/'training'; folder.mkdir(parents=True,exist_ok=True); trainer=build(); cp=latest(folder)
                    if cp is not None: trainer.load(cp)
                    log=folder/'metrics.jsonl'; seconds=reconcile(log,trainer.update,parent['update'])
                    with log.open('a',buffering=1) as stream:
                        while trainer.sampler.source_teachers!=GOALS:
                            try: check()
                            except (InterruptedError,TimeoutError): trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt'); raise
                            row=trainer.step(); seconds+=row['seconds']; stream.write(json.dumps(row,allow_nan=False)+'\n')
                            if trainer.sampler.position%20==0: heartbeat('training',teachers=row['additional_teacher_tokens'],teacher_budget=TOTAL,source_teachers=row['source_teachers'],loss=row['loss'])
                            if trainer.sampler.position%250==0: trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt')
                    cp=folder/f'checkpoint-{trainer.update:08d}.pt'; trainer.save(cp); result['checkpoints'][ARM]=detail(trainer,cp,b,seconds)
                    atomic_json(progress,result); del trainer; gc.collect(); torch.cuda.empty_cache()
                if ARM not in result['evaluations']:
                    evaluation.RUN=output/'evaluation'; dev=Shard(Path(base['dev_shards']),'dev'); tok=Tokenizer(ROOT/base['tokenizer'])
                    result['evaluations'][ARM]=evaluation.evaluate(ARM,result['checkpoints'][ARM],dev,tok,base,b,heartbeat,check,started[0]+c['GPU_budget_seconds']-prior_seconds)
                    atomic_json(progress,result)
                result.update(status='actual_nested2048_25M_and_reused512_control_complete_pending_new80',config_sha256=sha256(path),
                    scientific_teacher_tokens=TOTAL,reused_control_teacher_tokens=TOTAL,total_comparison_teacher_tokens=2*TOTAL,
                    verification_teacher_tokens=c['verification_teacher_tokens'],verification_GPU_seconds=c['verification_GPU_seconds'],
                    ordinary_stream_audit=c['references']['ordinary_stream_audit'],Base_adopted=False,Chat_adopted=False,
                    protected_test_used=False,requested_five_steps_complete=False)
            check(); elapsed=prior_seconds+time.monotonic()-started[0]; result['GPU_seconds']=elapsed
            job.update(status='complete',stage='complete',completed_at=now(),GPU_elapsed_seconds=elapsed)
            atomic_json(output/('result.json' if probe else 'compare-result.json'),result)
    except BaseException as error:
        job.update(status='failed',error=repr(error)); raise
    finally:
        if started[0] is not None and job['status']!='complete': job['GPU_elapsed_seconds']=prior_seconds+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser(); modes=p.add_mutually_exclusive_group()
    for mode in ('prepare-probe','preflight-probe','probe','freeze','inspect'): modes.add_argument('--'+mode,action='store_true')
    args=p.parse_args()
    if args.prepare_probe: prepare_probe()
    elif args.preflight_probe: inspect(PROBE_CONFIG)
    elif args.freeze: freeze()
    elif args.inspect: inspect(CONFIG)
    else: run(args.probe)
