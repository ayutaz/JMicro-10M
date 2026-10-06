"""One fixed coefficient, two matched100M forks, own measured CUDA gates."""
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
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import torch
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,implementation_hashes,gpu_lock,rng_state
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from condition_relation_language import RelationLanguageTrainView
from cached_three_source_index import CachedThreeSourceIndex
from parameter_displacement_anchor_trainer import ParameterAnchorTrainer,KIND
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state
import run_source_order_condition_comparison_v2 as prior
import run_complete_text_comparison as evaluation

RUN=ROOT/'reports/phase6/parameter-displacement-anchor-v3-20261006'
PROPOSAL=ROOT/'reports/phase6/parameter_displacement_anchor_proposal.json'
PROBE_CONFIG=ROOT/'configs/phase6/parameter_displacement_anchor_probe_v3.json'
CONFIG=ROOT/'configs/phase6/parameter_displacement_anchor_v3.json'
ARMS=('matched_staged_CE','parameter_anchor')
GOALS=prior.GOALS;TOTAL=100000000;CEILING=1800
SOURCES=('scripts/parameter_displacement_anchor_trainer.py','scripts/run_parameter_displacement_anchor_v3.py',
    'scripts/run_parameter_displacement_anchor_v3.ps1','tests/test_parameter_displacement_anchor.py')
reference,check_reference=prior.reference,prior.check_reference


def prepare():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    started=time.monotonic();p=read_json(PROPOSAL);check_reference(p['trigger']);check_reference(p['parent_and_anchor'])
    if (p['GPU_total_ceiling_seconds']!=1800 or p['probe_GPU_ceiling_seconds']!=120
            or p['lambda_fixed']!=.04161064039180984 or p['scientific_teacher_tokens_so_far']
            or p['Chat_started'] or p['quantization_started'] or not p['quality_criteria_unchanged']):
        raise ValueError('Original bounded parameter-anchor hypothesis required')
    suites=list(ET.parse(ROOT/'reports/phase6/parameter_displacement_anchor_tests.xml').getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Four actual analytic/fullstate/budget CPU tests required')
    old,*_=prior.inspect(prior.CONFIG)
    endpoint_job=read_json(prior.RUN/'job.json')
    if endpoint_job['status']!='complete' or alive(endpoint_job):raise ValueError('Prior actual comparison must terminate')
    parent=torch.load(p['parent_and_anchor']['path'],map_location='cpu',weights_only=False)
    if parent['update']!=323503 or not finite_state(parent) or parent['sampler']['source_teachers']!=GOALS:
        raise ValueError('Fixed finite completed mixed fullstate required')
    refs=copy.deepcopy(old['references'])
    refs.update(parameter_proposal=reference(PROPOSAL),finite_assay=reference(ROOT/'reports/phase6/finite_parameter_displacement_completion.json'),
        old_source_config=reference(prior.CONFIG),CPU_tests=reference(ROOT/'reports/phase6/parameter_displacement_anchor_tests.xml'),
        v1_preflight_failure_config=reference(ROOT/'configs/phase6/parameter_displacement_anchor_probe.json'))
    failed_job=ROOT/'reports/phase6/parameter-displacement-anchor-v2-20261006/probe/job.json'
    failed=read_json(failed_job)
    if failed['status']!='failed_or_interrupted' or alive(failed):raise ValueError('v2 must actually have terminated')
    refs.update(v2_config=reference(ROOT/'configs/phase6/parameter_displacement_anchor_probe_v2.json'),v2_failed_job=reference(failed_job))
    elapsed=time.monotonic()-started
    if elapsed>30:raise TimeoutError('CPU preparation30s exhausted')
    c=dict(research_kind=KIND,phase='probe',parent=p['parent_and_anchor'],strong_control=p['reference_strong_staged'],
        pool=old['pool'],positive_data=old['positive_data'],original_web=old['original_web'],original_config=old['original_config'],
        accepted_compact_index=old['accepted_compact_index'],references=refs,
        old_source_sha256=old['source_sha256'],source_sha256={s:sha256(ROOT/s) for s in SOURCES},implementation=implementation_hashes(),
        coefficients=dict(matched_staged_CE=0.,parameter_anchor=p['lambda_fixed']),arms=list(ARMS),teacher_goals=GOALS,
        teachers_per_arm=TOTAL,new_scientific_teacher_tokens=2*TOTAL,peak_lr=.00001,source_order=list(prior.SOURCE_ORDER),
        shapes=old['shapes'],GPU_budget_seconds=120-failed['GPU_elapsed_seconds'],failed_probe_GPU_seconds=failed['GPU_elapsed_seconds'],
        total_new_GPU_ceiling_seconds=CEILING,CPU_preparation_seconds=elapsed,
        quality_criteria_unchanged=True,old_numerical7_preserved=True,Base_adopted=False,Base_complete=False,
        protected_test_used=False,Chat_started=False,quantization_started=False,created_at=now())
    atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print(json.dumps(dict(status='own_two_arm_probe_frozen',CPU_preparation_seconds=elapsed)),flush=True)


def inspect(path):
    c=read_json(path)
    if (c['research_kind']!=KIND or c['arms']!=list(ARMS) or c['teacher_goals']!=GOALS or c['teachers_per_arm']!=TOTAL
            or c['new_scientific_teacher_tokens']!=2*TOTAL or c['total_new_GPU_ceiling_seconds']!=CEILING
            or c['coefficients']!=dict(matched_staged_CE=0.,parameter_anchor=.04161064039180984)
            or c['peak_lr']!=.00001 or c['source_order']!=list(prior.SOURCE_ORDER)
            or c['shapes']!=dict(context=1024,batch=32,accumulation=1,backend='flash',compile_mode='reduce-overhead',dtype='bf16')
            or c['Base_complete'] or c['Base_adopted'] or c['Chat_started'] or c['quantization_started']
            or c['protected_test_used'] or not c['quality_criteria_unchanged']):raise ValueError('Original fixed matched comparison differs')
    if c['implementation']!=implementation_hashes():raise ValueError('Frozen normalized core implementation differs')
    for relative,digest in {**c['old_source_sha256'],**c['source_sha256']}.items():
        if sha256(ROOT/relative)!=digest:raise ValueError('Frozen implementation differs: '+relative)
    for ref in (*c['references'].values(),c['parent'],c['strong_control'],c['accepted_compact_index'],c['original_config']):check_reference(ref)
    folder=RUN/'probe' if path==PROBE_CONFIG else RUN
    if (folder/'job.json').exists() and alive(read_json(folder/'job.json')):raise ValueError('Actual live job; no duplicate')
    if path==PROBE_CONFIG:
        if c['phase']!='probe' or c['GPU_budget_seconds']!=120-c['failed_probe_GPU_seconds']:raise ValueError('Own probe ceiling differs')
    elif path==CONFIG:
        r=probe_evidence();timings,estimate=estimate_training(r)
        if (c['phase']!='scientific' or c['probe_config_sha256']!=sha256(PROBE_CONFIG)
                or c['probe_result_sha256']!=sha256(RUN/'probe/result.json') or c['measured_timings']!=timings
                or c['estimated_GPU_seconds_with_margin']!=estimate or estimate+r['GPU_seconds']+c['failed_probe_GPU_seconds']>CEILING
                or c['verification_GPU_seconds']!=r['GPU_seconds']+c['failed_probe_GPU_seconds'] or c['verification_teacher_tokens']!=r['verification_teacher_tokens']
                or not math.isclose(c['GPU_budget_seconds']+r['GPU_seconds']+c['failed_probe_GPU_seconds'],CEILING,abs_tol=1e-9)):
            raise ValueError('Actual measured science cost gate differs')
    else:raise ValueError('Only original two config paths allowed')
    return c


def probe_evidence():
    job=read_json(RUN/'probe/job.json');r=read_json(RUN/'probe/result.json')
    if (job['status']!='complete' or alive(job) or not r['passed'] or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['GPU_seconds']+read_json(PROBE_CONFIG)['failed_probe_GPU_seconds']>120 or r['config_sha256']!=sha256(PROBE_CONFIG)
            or set(r['gates'])!=set(ARMS) or any(not all(g['checks'].values()) for g in r['gates'].values())
            or not all(r['initial_fullstate_preservation'][arm]['all_checks'] for arm in ARMS)):
        raise ValueError('Own actual both-arm fullstate CUDA gates and terminal timings required')
    return r


def estimate_training(r):
    timings={};total=0.
    for arm in ARMS:
        t=r['timings'][arm];rows=t['histories']
        if len(rows)!=32 or any(not math.isfinite(row['seconds']) or row['seconds']<=0 for row in rows):
            raise ValueError('Own32 actual finite timings per arm required')
        step=statistics.median(row['seconds'] for row in rows[8:]);teachers=t['verification_teacher_tokens']/32
        updates=math.ceil(TOTAL/teachers);warm=max(0.,sum(row['seconds'] for row in rows[:8])-8*step)
        saving=(math.ceil(updates/250)+1)*t['terminal_save_seconds'];seconds=updates*step+warm+saving
        timings[arm]=dict(steady_step_seconds=step,teachers_per_update=teachers,estimated_updates=updates,
            warmup_seconds=warm,save_seconds=saving,estimated_training_seconds=seconds);total+=seconds
    return timings,total*1.3+150+50


def freeze():
    if CONFIG.exists():inspect(CONFIG);return
    c=copy.deepcopy(inspect(PROBE_CONFIG));r=probe_evidence();timings,estimate=estimate_training(r)
    if estimate+r['GPU_seconds']+c['failed_probe_GPU_seconds']>CEILING:raise ValueError('Own measured two-arm cost exceeds1800s; no science')
    c.update(phase='scientific',probe_config_sha256=sha256(PROBE_CONFIG),probe_result_sha256=sha256(RUN/'probe/result.json'),
        measured_timings=timings,estimated_GPU_seconds_with_margin=estimate,verification_GPU_seconds=r['GPU_seconds']+c['failed_probe_GPU_seconds'],
        verification_teacher_tokens=r['verification_teacher_tokens'],GPU_budget_seconds=CEILING-r['GPU_seconds']-c['failed_probe_GPU_seconds'],save_every_updates=250)
    atomic_json(CONFIG,c);inspect(CONFIG)
    print(json.dumps(dict(status='own_measured_two100M_science_frozen',timings=timings,estimate_seconds=estimate)),flush=True)


def binding(c,path,arm):
    return dict(config_sha256=sha256(path),arm=arm,parent=c['parent'],teacher_goals=GOALS,
        study_kind=KIND,parameter_coefficient=c['coefficients'][arm],original_web=c['original_web'],
        positive_manifest_sha256=c['positive_data']['manifest_sha256'],optimizer_policy='inherit',peak_lr=.00001)


def resume_gate(build,folder,cfg,check):
    r=prior.resume_gate(build,folder,cfg,check)
    for key in ('CE_loss','parameter_penalty','parameter_coefficient','parameter_penalty_teacher_tokens'):
        r['checks']['history_'+key]=all(a[key]==b[key] for a,b in zip(*r['histories'],strict=True))
    if not all(r['checks'].values()):raise ValueError('Actual penalty resumed trajectory differs')
    atomic_json(folder/'result.json',r);return r


def run(probe=False):
    path=PROBE_CONFIG if probe else CONFIG;c=inspect(path);output=RUN/'probe' if probe else RUN
    output.mkdir(parents=True,exist_ok=True);jp=output/'job.json';old=read_json(jp) if jp.exists() else {}
    if old and old['config_sha256']!=sha256(path):raise ValueError('Original interrupted job binding differs')
    if old.get('status')=='complete':print('Original completed run retained');return
    previous=old.get('GPU_elapsed_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(path),GPU_elapsed_seconds=previous,started_at=now(),
        restart_command=f"scripts/run_parameter_displacement_anchor_v3.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Interrupted; completed scientific updates retained')
        if started[0] is not None and previous+time.monotonic()-started[0]>c['GPU_budget_seconds']:
            raise TimeoutError('Cumulative actual job GPU ceiling exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_elapsed_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);heartbeat('setup')
        for relative in (*c['source_sha256'],*c['old_source_sha256'],*c['implementation'],path.relative_to(ROOT).as_posix()):
            target=output/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/relative).read_bytes():raise ValueError('Snapshot differs')
            if not target.exists():shutil.copyfile(ROOT/relative,target)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        pool=TrainView(c['pool']['pool'],c['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
        if not pool.index.cache_reused:raise ValueError('Accepted compact index must be reused')
        original=TrainView(c['original_web']['path'],c['original_web']['manifest_sha256'])
        positive=RelationLanguageTrainView(c['positive_data']['path'],c['positive_data']['manifest_sha256'])
        base=read_json(Path(c['original_config']['path']))
        with gpu_lock('cuda'):
            started[0]=time.monotonic();heartbeat('GPU')
            progress=output/'progress-result.json';result=read_json(progress) if progress.exists() else dict(gates={},timings={},initial_fullstate_preservation={}) if probe else dict(checkpoints={},evaluations={},transfer={},retention={})
            for arm in ARMS:
                b=binding(c,path,arm)
                def build():return ParameterAnchorTrainer(parent,pool,original,positive,GOALS,b,c['coefficients'][arm])
                if probe:
                    if arm in result['timings']:continue
                    initial=build()
                    preservation=dict(model=equal_state(prior.cpu_state(initial.model.state_dict()),parent['model']),
                        optimizer=equal_state(prior.cpu_state(initial.optimizer.state_dict()),parent['optimizer']),
                        scheduler=equal_state(initial.scheduler.state_dict(),parent['scheduler']),RNG=equal_state(rng_state(),parent['rng']),
                        actual_Web_cursor=equal_state(initial.sampler.streams['web'].sampler.state_dict(),parent['sampler']['streams']['web']['sampler']),
                        parent_sampler_lineage=equal_state(initial.lineage['actual_parent_sampler'],parent['sampler']),
                        actual_LR=[g['lr'] for g in initial.optimizer.param_groups]==[.00001,.00001],
                        anchor_matches=equal_state(prior.cpu_state(initial.anchor),{k:parent['model'][k] for k in initial.anchor}))
                    preservation['all_checks']=all(preservation.values())
                    if not preservation['all_checks']:raise ValueError('Actual initial parent fullstate/anchor differs')
                    result['initial_fullstate_preservation'][arm]=preservation;del initial;gc.collect();torch.cuda.empty_cache()
                    result['gates'][arm]=resume_gate(build,output/arm/'resume-gate',sha256(path),check)
                    folder=output/arm/'timing';folder.mkdir(parents=True,exist_ok=True);trainer=build();cp=prior.latest(folder)
                    if cp is not None:trainer.load(cp)
                    log=folder/'metrics.jsonl';prior.reconcile(log,trainer.update,parent['update'])
                    with log.open('a',buffering=1) as stream:
                        while trainer.update-parent['update']<32:
                            check();row=trainer.step();stream.write(json.dumps(row,allow_nan=False)+'\n')
                            if trainer.sampler.position%8==0:heartbeat(arm+'-timing',completed_updates=trainer.sampler.position)
                    cp=folder/'checkpoint.pt';saved=trainer.save(cp);rows=[json.loads(s) for s in log.read_text().splitlines()]
                    for row,expected in zip(rows[:4],result['gates'][arm]['histories'][0],strict=True):
                        if any(row[k]!=expected[k] for k in ('loss','CE_loss','parameter_penalty','gradient_norm','token_digest','source_teachers')):
                            raise ValueError('Actual probe trajectories differ')
                    if not finite_state(torch.load(cp,map_location='cpu',weights_only=False)):raise ValueError('Actual finite terminal timing state required')
                    result['timings'][arm]=dict(histories=rows,verification_teacher_tokens=trainer.supervised_tokens-parent['supervised_tokens'],
                        terminal_save_seconds=saved,peak_VRAM_bytes=torch.cuda.max_memory_allocated(),checkpoint=reference(cp))
                    atomic_json(progress,result);del trainer;gc.collect();torch.cuda.empty_cache()
                else:
                    if arm not in result['checkpoints']:
                        folder=output/arm/'training';folder.mkdir(parents=True,exist_ok=True);trainer=build();cp=prior.latest(folder)
                        if cp is not None:trainer.load(cp)
                        log=folder/'metrics.jsonl';seconds=prior.reconcile(log,trainer.update,parent['update'])
                        with log.open('a',buffering=1) as stream:
                            while trainer.sampler.source_teachers!=GOALS:
                                try:check()
                                except (InterruptedError,TimeoutError):trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt');raise
                                row=trainer.step();seconds+=row['seconds'];stream.write(json.dumps(row,allow_nan=False)+'\n')
                                if trainer.sampler.position%20==0:heartbeat(arm+'-training',teachers=row['additional_teacher_tokens'],teacher_budget=TOTAL,loss=row['loss'],parameter_penalty=row['parameter_penalty'],source_teachers=row['source_teachers'])
                                if trainer.sampler.position%250==0:trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt')
                        cp=folder/f'checkpoint-{trainer.update:08d}.pt';trainer.save(cp)
                        result['checkpoints'][arm]=dict(prior.detail(trainer,cp,b,seconds),parameter_coefficient=trainer.coefficient,
                            parameter_penalty_teacher_tokens=0,anchor_initial_digest=trainer.anchor_initial_digest,
                            sampler=trainer.sampler.state_dict(),source_body_bytes=trainer.sampler.source_body_bytes.copy(),token_digest=trainer.token_digest)
                        atomic_json(progress,result);del trainer;gc.collect();torch.cuda.empty_cache()
                    if arm not in result['evaluations']:
                        evaluation.RUN=output/'evaluation';dev=Shard(Path(base['dev_shards']),'dev');tok=Tokenizer(ROOT/base['tokenizer'])
                        result['evaluations'][arm]=evaluation.evaluate(arm,result['checkpoints'][arm],dev,tok,base,b,heartbeat,check,started[0]+c['GPU_budget_seconds']-previous)
                        atomic_json(progress,result)
                    prior.RUN=RUN;prior.CONFIG=CONFIG
                    checkpoint=dict(path=result['checkpoints'][arm]['checkpoint'],sha256=result['checkpoints'][arm]['checkpoint_sha256'])
                    for suite,key in (('bridge','transfer'),('retention','retention')):
                        if arm not in result[key]:result[key][arm]=prior.transfer_scores(c,arm,checkpoint,heartbeat,check,suite);atomic_json(progress,result)
            if probe:
                result.update(passed=True,config_sha256=sha256(path),scientific_teacher_tokens=0,weights_discarded_for_science=True,
                    GPU_optimizer_updates=80,verification_teacher_tokens=sum(g['verification_teacher_tokens'] for g in result['gates'].values())+sum(t['verification_teacher_tokens'] for t in result['timings'].values()))
            else:
                a,b=[result['checkpoints'][arm] for arm in ARMS]
                matching=('additional_supervised_tokens','additional_input_tokens','source_teachers','source_eos','source_input_tokens','source_body_bytes','focus_token_digest','token_digest','sampler')
                if any(not equal_state(a[k],b[k]) for k in matching):raise ValueError('Both scientific streams/targets/counters differ')
                result.update(scientific_teacher_tokens=2*TOTAL,all_scientific_input_streams_match=True,config_sha256=sha256(path))
            check();elapsed=previous+time.monotonic()-started[0]
            result.update(status='own_two_arm_probe_complete' if probe else 'two100M_GPU_complete_pending_all160_content_review',
                GPU_seconds=elapsed,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True)
            atomic_json(output/('result.json' if probe else 'compare-result.json'),result)
            job.update(status='complete',GPU_elapsed_seconds=elapsed,completed_at=now())
    except BaseException as error:job.update(status='failed_or_interrupted',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_elapsed_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2)
    parser=argparse.ArgumentParser();modes=parser.add_mutually_exclusive_group()
    for mode in ('prepare','preflight-probe','probe','freeze','inspect'):modes.add_argument('--'+mode,action='store_true')
    args=parser.parse_args()
    if args.prepare:prepare()
    elif args.preflight_probe:inspect(PROBE_CONFIG)
    elif args.freeze:freeze()
    elif args.inspect:inspect(CONFIG)
    else:run(args.probe)
