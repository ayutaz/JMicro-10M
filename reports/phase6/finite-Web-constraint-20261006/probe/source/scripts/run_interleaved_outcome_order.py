"""One missing order-by-target Base cell, own CUDA resume/timing and budget."""
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
from conditional_prefix_mask_trainer import COUNTERS
from interleaved_outcome_trainer import InterleavedOutcomeSampler,InterleavedOutcomeTrainer,KIND,SOURCE_ORDER
from historical_parent_condition_trainer import historical_web_cursor
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state
import run_source_order_condition_comparison_v2 as prior
import run_complete_text_comparison as evaluation

RUN=ROOT/'reports/phase6/interleaved-outcome-order-20261006'
PROPOSAL=ROOT/'reports/phase6/interleaved_outcome_order_proposal.json'
PROBE_CONFIG=ROOT/'configs/phase6/interleaved_outcome_order_probe.json'
CONFIG=ROOT/'configs/phase6/interleaved_outcome_order.json'
LEDGER=ROOT/'reports/phase6/interleaved_outcome_reference_input.json'
ARM='interleaved_outcome_EOS';CEILING=900
SOURCES=('scripts/interleaved_outcome_trainer.py','scripts/run_interleaved_outcome_order.py',
    'scripts/run_interleaved_outcome_order.ps1','tests/test_interleaved_outcome.py',
    'scripts/conditional_prefix_mask_trainer.py','scripts/source_order_condition_trainer.py')
reference,check_reference=prior.reference,prior.check_reference


def data(c):
    pool=TrainView(c['pool']['pool'],c['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
    if not pool.index.cache_reused:raise ValueError('Accepted compact index must be reused')
    original=TrainView(c['original_web']['path'],c['original_web']['manifest_sha256'])
    positive=RelationLanguageTrainView(c['positive_data']['path'],c['positive_data']['manifest_sha256'])
    return pool,original,positive


def prepare():
    if PROBE_CONFIG.exists():inspect(PROBE_CONFIG);return
    started=time.monotonic();p=read_json(PROPOSAL)
    if (p['total_new_GPU_ceiling_seconds']!=900 or p['probe_GPU_ceiling_seconds']!=120
            or p['predicted_actual_hard_teachers']!=91641755 or p['new_teacher_tokens_so_far'] or p['GPU_seconds_so_far']
            or p['Base_complete'] or p['Base_adopted'] or p['Chat_started'] or p['quantization_started']):
        raise ValueError('Original fourth-cell order/target hypothesis required')
    for key in ('trigger','frozen_original_fullparent','original_mixed_config'):
        check_reference(p[key])
    for cell in p['cells'].values():
        if 'result' in cell:check_reference(cell['result'])
    suites=list(ET.parse(ROOT/'reports/phase6/interleaved_outcome_tests.xml').getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=3 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Three actual CPU order/mask/fullstate/budget tests required')
    old=read_json(Path(p['original_mixed_config']['path']));staged_config=read_json(prior.CONFIG)
    mixed_run=Path(p['cells']['full_targets_interleaved']['result']['path']).parent
    for folder in (mixed_run,prior.RUN,ROOT/'reports/phase6/conditional-prefix-mask-20261006'):
        job=read_json(folder/'job.json')
        if job['status']!='complete' or alive(job):raise ValueError('Every completed cell must actually terminate')
    parent=torch.load(p['frozen_original_fullparent']['path'],map_location='cpu',weights_only=False)
    staged_result=read_json(Path(p['cells']['full_targets_staged']['result']['path']));record=staged_result['checkpoints']['source_order']
    strong=dict(path=record['checkpoint'],sha256=record['checkpoint_sha256'])
    if not finite_state(parent) or parent['update']!=320435:raise ValueError('Fixed finite original fullstate required')
    c=dict(research_kind=KIND,phase='probe',parent=p['frozen_original_fullparent'],strong_control=strong,
        pool=old['pool'],original_web=old['original_web'],positive_data=old['positive_data'],original_config=old['original_config'],
        accepted_compact_index=old['accepted_compact_index'],old_source_sha256=dict(old['source_sha256'],**staged_config['source_sha256']),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},implementation=implementation_hashes(),references=copy.deepcopy(old['references']),
        teacher_goals=prior.GOALS,shapes=old['shapes'],source_order=list(SOURCE_ORDER),peak_lr=.00001,
        reference_order_policy='progress_balanced_interleaved',
        total_new_GPU_ceiling_seconds=CEILING,GPU_budget_seconds=120,quality_criteria_unchanged=True,protected_test_used=False,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,created_at=now())
    c['references'].update(proposal=reference(PROPOSAL),old_source_config=p['original_mixed_config'],
        control_result=p['cells']['full_targets_staged']['result'],control_notes=reference(ROOT/'reports/phase6/source_order_condition_notes.json'),
        mixed_control_result=p['cells']['full_targets_interleaved']['result'],mixed_control_notes=reference(ROOT/'reports/phase6/historical_parent_condition_notes.json'),
        masked_staged_result=p['cells']['outcome_EOS_targets_staged']['result'],masked_staged_review=p['cells']['outcome_EOS_targets_staged']['review'],
        CPU_tests=reference(ROOT/'reports/phase6/interleaved_outcome_tests.xml'),
        original_metrics=reference(mixed_run/'historical_parent/training/metrics.jsonl'))
    pool,original,positive=data(c)
    cursor=historical_web_cursor(parent)
    sampler=InterleavedOutcomeSampler(pool,original,positive,cursor,prior.GOALS);sampler.reference_token_digest=parent['token_digest']
    rows=[];expected=[json.loads(s) for s in Path(c['references']['original_metrics']['path']).read_text().splitlines()]
    for row in expected:
        if time.monotonic()-started>60:raise TimeoutError('CPU preparation60s exhausted')
        x,y,body_bytes,focus=sampler.batch(32)
        if (row['token_digest']!=sampler.reference_token_digest
                or any(row['source_input_tokens' if k=='source_tokens' else k]!=getattr(sampler,k) for k in COUNTERS)):
            raise ValueError('Exact original mixed reference input/target/source stream differs')
        rows.append(dict(update=row['update'],reference_token_digest=sampler.reference_token_digest,
            actual_teachers=int(y.ne(-100).sum()),actual_body_bytes=body_bytes,
            conditional_sequences=sampler.last_genres.count('conditional_textbook'),actual_source_routes=list(sampler.last_genres)))
    staged=InterleavedOutcomeSampler(pool,original,positive,cursor,prior.GOALS,reference_policy='staged');staged.reference_token_digest=parent['token_digest']
    while staged.source_teachers!=prior.GOALS:
        if time.monotonic()-started>60:raise TimeoutError('CPU preparation60s exhausted')
        staged.batch(32)
    terminal=torch.load(c['strong_control']['path'],map_location='cpu',weights_only=False)
    if (len(rows)!=3068 or sampler.source_teachers!=prior.GOALS
            or not equal_state(staged.reference_state(),terminal['sampler']) or staged.reference_token_digest!=terminal['token_digest']
            or sampler.source_digests!=staged.source_digests or sampler.actual!=staged.actual
            or any(row['actual_teachers']<=0 for row in rows) or sampler.actual['teachers']!=p['predicted_actual_teachers_by_source']):
        raise ValueError('Both original orders must contain identical per-source inputs/reference and masked targets')
    for key in (*COUNTERS,'streams','position'):
        if not equal_state(sampler.reference_state()[key],staged.reference_state()[key]):raise ValueError('Per-source terminal cursors/counts differ')
    ledger=dict(status='original_mixed_reference_full3068_and_both_order_source_hashes_match',parent=c['parent'],control=c['strong_control'],
        original_reference_suffix_teacher_tokens=100000000,
        actual_masked_suffix_teacher_tokens=sum(sampler.actual['teachers'].values()),
        original_reference_token_digest=sampler.reference_token_digest,actual_source_accounting=sampler.actual,
        source_digests=sampler.source_digests,staged_source_digests=staged.source_digests,
        terminal_reference_sampler=sampler.reference_state(),rows=rows,physical_input_tokens=len(rows)*1024*32,
        staged_reference_sampler=staged.reference_state(),all_per_source_input_targets_EOS_cursors_match=True,
        matched_original_mixed_global_input=True,matched_masked_staged_global_input=False,
        original_control_whole100M_is_reused_not_new=True,matched_masked_recipe_hard_teachers=True,protected_test_used=False)
    atomic_json(LEDGER,ledger);c['references']['reference_input_ledger']=reference(LEDGER)
    elapsed=time.monotonic()-started
    if elapsed>60:raise TimeoutError('CPU preparation60s exhausted')
    c.update(CPU_preparation_seconds=elapsed,remaining_updates=len(rows),
        actual_scientific_teacher_tokens_predicted=ledger['actual_masked_suffix_teacher_tokens'],
        reference_suffix_teacher_tokens=ledger['original_reference_suffix_teacher_tokens'])
    atomic_json(PROBE_CONFIG,c);inspect(PROBE_CONFIG)
    print(json.dumps(dict(status='own_interleaved_outcome_probe_frozen',CPU_seconds=elapsed,updates=len(rows),
        predicted_actual_teachers=c['actual_scientific_teacher_tokens_predicted'],reference_teachers=c['reference_suffix_teacher_tokens'])),flush=True)


def inspect(path):
    c=read_json(path);p=read_json(PROPOSAL)
    if (c['research_kind']!=KIND or c['remaining_updates']!=3068 or c['parent']!=p['frozen_original_fullparent']
            or c['reference_order_policy']!='progress_balanced_interleaved'
            or c['teacher_goals']!=prior.GOALS or c['peak_lr']!=.00001 or c['source_order']!=list(SOURCE_ORDER)
            or c['total_new_GPU_ceiling_seconds']!=900 or c['Base_complete'] or c['Base_adopted']
            or c['Chat_started'] or c['quantization_started'] or c['protected_test_used'] or not c['quality_criteria_unchanged']
            or c['implementation']!=implementation_hashes()):raise ValueError('Frozen Base suffix scope differs')
    for relative,digest in {**c['old_source_sha256'],**c['source_sha256']}.items():
        if sha256(ROOT/relative)!=digest:raise ValueError('Frozen source differs: '+relative)
    for ref in (*c['references'].values(),c['parent'],c['strong_control'],c['accepted_compact_index'],c['original_config']):check_reference(ref)
    folder=RUN/'probe' if path==PROBE_CONFIG else RUN
    if (folder/'job.json').exists() and alive(read_json(folder/'job.json')):raise ValueError('Actual live job; no duplicate')
    if path==PROBE_CONFIG:
        if c['phase']!='probe' or c['GPU_budget_seconds']!=120:raise ValueError('Own120s probe required')
    elif path==CONFIG:
        r=probe_evidence();timing,estimate=estimate_training(r,c['remaining_updates'])
        if (c['phase']!='scientific' or c['probe_config_sha256']!=sha256(PROBE_CONFIG)
                or c['probe_result_sha256']!=sha256(RUN/'probe/result.json') or c['measured_timing']!=timing
                or c['estimated_GPU_seconds_with_margin']!=estimate or estimate+r['GPU_seconds']>CEILING
                or c['verification_GPU_seconds']!=r['GPU_seconds']
                or not math.isclose(c['GPU_budget_seconds']+r['GPU_seconds'],CEILING,abs_tol=1e-9)):
            raise ValueError('Own actual measured cumulative budget differs')
    else:raise ValueError('Only the fixed probe and science config paths allowed')
    return c


def estimate_training(r,updates):
    t=r['timing'];rows=t['histories']
    if len(rows)!=32 or any(not math.isfinite(row['seconds']) or row['seconds']<=0 for row in rows):raise ValueError('Own32 timings required')
    step=statistics.median(row['seconds'] for row in rows[8:]);warm=max(0.,sum(row['seconds'] for row in rows[:8])-8*step)
    saving=(math.ceil(updates/250)+1)*t['terminal_save_seconds'];seconds=updates*step+warm+saving
    return dict(steady_step_seconds=step,estimated_updates=updates,warmup_seconds=warm,save_seconds=saving,
        estimated_training_seconds=seconds),seconds*1.3+150+50


def probe_evidence():
    r=read_json(RUN/'probe/result.json');job=read_json(RUN/'probe/job.json')
    if (job['status']!='complete' or alive(job) or not r['passed'] or not all(r['gate']['checks'].values())
            or not all(r['initial_fullstate_preservation'].values()) or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['GPU_seconds']>120 or r['config_sha256']!=sha256(PROBE_CONFIG)):
        raise ValueError('Own actually terminated masked CUDA gate required')
    return r


def freeze():
    if CONFIG.exists():inspect(CONFIG);return
    c=copy.deepcopy(inspect(PROBE_CONFIG));r=probe_evidence();timing,estimate=estimate_training(r,c['remaining_updates'])
    if estimate+r['GPU_seconds']>CEILING:raise ValueError('Actual science plus probe exceeds900s; no science')
    c.update(phase='scientific',probe_config_sha256=sha256(PROBE_CONFIG),probe_result_sha256=sha256(RUN/'probe/result.json'),
        measured_timing=timing,estimated_GPU_seconds_with_margin=estimate,verification_GPU_seconds=r['GPU_seconds'],
        verification_teacher_tokens=r['verification_teacher_tokens'],GPU_budget_seconds=CEILING-r['GPU_seconds'],save_every_updates=250)
    atomic_json(CONFIG,c);inspect(CONFIG);print(json.dumps(dict(status='own_measured_science_frozen',estimate_seconds=estimate,timing=timing)),flush=True)


def resume_gate(build,folder,cfg,check):
    record=folder/'result.json'
    if record.exists():
        r=read_json(record)
        if r['config_sha256']!=cfg or not r['passed']:raise ValueError('Stored gate differs')
        return r
    folder.mkdir(parents=True,exist_ok=True);states=[];histories=[];teachers=0
    for route in ('continuous','resumed'):
        trainer=build();before=trainer.supervised_tokens;rows=[]
        for i in range(8):
            check();rows.append(trainer.step())
            if route=='resumed' and i==3:
                trainer.save(folder/'split.pt');del trainer;gc.collect();torch.cuda.empty_cache()
                trainer=build();trainer.load(folder/'split.pt')
        teachers+=trainer.supervised_tokens-before;trainer.save(folder/(route+'.pt'))
        states.append(torch.load(folder/(route+'.pt'),map_location='cpu',weights_only=False));histories.append(rows)
        del trainer;gc.collect();torch.cuda.empty_cache()
    checks={k:equal_state(states[0][k],states[1][k]) for k in states[0]}
    for key in set(histories[0][0])-{'seconds','data_wait_seconds','tokens_per_second'}:
        checks['history_'+key]=equal_state([r[key] for r in histories[0]],[r[key] for r in histories[1]])
    checks.update(finite=all(finite_state(s) for s in states),no_reheat=all(r['lr']==.00001 for h in histories for r in h),
        mixed_sources_present=all(set(g for row in h for g in row['actual_source_routes'])==set(SOURCE_ORDER) for h in histories),
        actual_conditional_mask_active=all(h[-1]['removed_prefix_targets']['conditional_textbook']>0 for h in histories))
    if not all(checks.values()):raise ValueError('Own masked CUDA resume mismatch: '+repr(checks))
    result=dict(passed=True,checks=checks,histories=histories,config_sha256=cfg,GPU_optimizer_updates=16,verification_teacher_tokens=teachers)
    atomic_json(record,result);return result


def binding(c,path):
    return dict(config_sha256=sha256(path),arm=ARM,parent=c['parent'],study_kind=KIND,
        teacher_goals=c['teacher_goals'],target_rule='conditional outcome+EOS only; original reference quotas stop input',optimizer_policy='inherit',peak_lr=.00001)


def run(probe=False):
    path=PROBE_CONFIG if probe else CONFIG;c=inspect(path);output=RUN/'probe' if probe else RUN
    output.mkdir(parents=True,exist_ok=True);jp=output/'job.json';old=read_json(jp) if jp.exists() else {}
    if old and old['config_sha256']!=sha256(path):raise ValueError('Interrupted job config differs')
    if old.get('status')=='complete':print('Original completed run retained');return
    previous=old.get('GPU_elapsed_seconds',0.);started=[None];stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(path),GPU_elapsed_seconds=previous,started_at=now(),
        restart_command=f"scripts/run_interleaved_outcome_order.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Interrupted; completed suffix updates retained')
        if started[0] is not None and previous+time.monotonic()-started[0]>c['GPU_budget_seconds']:raise TimeoutError('Cumulative GPU ceiling exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started[0] is not None:job['GPU_elapsed_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True);heartbeat('setup')
        for relative in (*c['source_sha256'],*c['old_source_sha256'],*c['implementation'],path.relative_to(ROOT).as_posix()):
            target=output/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/relative).read_bytes():raise ValueError('Frozen snapshot differs')
            if not target.exists():shutil.copyfile(ROOT/relative,target)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False);pool,original,positive=data(c)
        base=read_json(Path(c['original_config']['path']));b=binding(c,path)
        def build():return InterleavedOutcomeTrainer(parent,pool,original,positive,c['teacher_goals'],b)
        with gpu_lock('cuda'):
            started[0]=time.monotonic();heartbeat('GPU');progress=output/'progress-result.json'
            result=read_json(progress) if progress.exists() else {}
            if probe:
                if 'initial_fullstate_preservation' not in result:
                    t=build();checks=dict(model=equal_state(prior.cpu_state(t.model.state_dict()),parent['model']),
                        optimizer=equal_state(prior.cpu_state(t.optimizer.state_dict()),parent['optimizer']),
                        scheduler=equal_state(t.scheduler.state_dict(),parent['scheduler']),RNG=equal_state(rng_state(),parent['rng']),
                        actual_parent_sampler_lineage=equal_state(t.lineage['actual_parent_sampler'],parent['sampler']),
                        actual_Web_cursor=equal_state(t.sampler.streams['web'].sampler.state_dict(),parent['sampler']['web']),
                        new_reference_counters_zero=not any(t.sampler.source_teachers.values()) and t.sampler.position==0,
                        actual_LR=all(g['lr']==.00001 for g in t.optimizer.param_groups))
                    if not all(checks.values()):raise ValueError('Initial fullstate differs')
                    result['initial_fullstate_preservation']=checks;del t;gc.collect();torch.cuda.empty_cache()
                result['gate']=resume_gate(build,output/'resume-gate',sha256(path),check)
                if 'timing' not in result:
                    folder=output/'timing';folder.mkdir(parents=True,exist_ok=True);t=build();cp=prior.latest(folder)
                    if cp is not None:t.load(cp)
                    log=folder/'metrics.jsonl';prior.reconcile(log,t.update,parent['update'])
                    with log.open('a',buffering=1) as stream:
                        while t.update-parent['update']<32:
                            try:check()
                            except (InterruptedError,TimeoutError):t.save(folder/'checkpoint.pt');raise
                            row=t.step();stream.write(json.dumps(row,allow_nan=False)+'\n')
                            if (t.update-parent['update'])%8==0:heartbeat('masked-timing',completed_updates=t.update-parent['update'])
                    cp=folder/'checkpoint.pt';saved=t.save(cp);rows=[json.loads(s) for s in log.read_text().splitlines()]
                    for row,expected in zip(rows[:8],result['gate']['histories'][0],strict=True):
                        if any(not equal_state(row[k],expected[k]) for k in set(row)-{'seconds','data_wait_seconds','tokens_per_second'}):raise ValueError('Probe trajectories differ')
                    if not finite_state(torch.load(cp,map_location='cpu',weights_only=False)):raise ValueError('Finite actual CUDA timing state required')
                    result['timing']=dict(histories=rows,verification_teacher_tokens=t.supervised_tokens-parent['supervised_tokens'],
                        terminal_save_seconds=saved,checkpoint=reference(cp),peak_VRAM_bytes=torch.cuda.max_memory_allocated())
                    del t;gc.collect();torch.cuda.empty_cache()
                result.update(passed=True,GPU_optimizer_updates=48,verification_teacher_tokens=result['gate']['verification_teacher_tokens']+result['timing']['verification_teacher_tokens'],
                    scientific_teacher_tokens=0,weights_discarded_for_science=True)
            else:
                if 'checkpoint' not in result:
                    folder=output/ARM/'training';folder.mkdir(parents=True,exist_ok=True);t=build();cp=prior.latest(folder)
                    if cp is not None:t.load(cp)
                    log=folder/'metrics.jsonl';seconds=prior.reconcile(log,t.update,parent['update'])
                    ledger=read_json(LEDGER)
                    with log.open('a',buffering=1) as stream:
                        while t.sampler.source_teachers!=c['teacher_goals']:
                            try:check()
                            except (InterruptedError,TimeoutError):t.save(folder/f'checkpoint-{t.update:08d}.pt');raise
                            row=t.step();expected=ledger['rows'][t.update-parent['update']-1]
                            if (row['reference_token_digest']!=expected['reference_token_digest']
                                    or row['actual_source_routes']!=expected['actual_source_routes']):raise ValueError('Scientific original input suffix differs')
                            seconds+=row['seconds'];stream.write(json.dumps(row,allow_nan=False)+'\n')
                            if (t.update-parent['update'])%20==0:heartbeat('masked-suffix-training',completed_updates=t.update-parent['update'],total_updates=3068,
                                actual_teachers=row['additional_teacher_tokens'],reference_teachers=row['reference_suffix_teacher_tokens'],loss=row['loss'])
                            if (t.update-parent['update'])%250==0:t.save(folder/f'checkpoint-{t.update:08d}.pt')
                    cp=folder/f'checkpoint-{t.update:08d}.pt';t.save(cp)
                    if (t.update-parent['update']!=3068 or t.supervised_tokens-parent['supervised_tokens']!=ledger['actual_masked_suffix_teacher_tokens']
                            or t.sampler.actual!=ledger['actual_source_accounting']
                            or t.sampler.source_digests!=ledger['source_digests']
                            or not equal_state(t.sampler.reference_state(),ledger['terminal_reference_sampler'])):raise ValueError('Completed scientific original mixed input/masked/source accounting differs')
                    result['checkpoint']=dict(checkpoint=str(cp),checkpoint_sha256=sha256(cp),binding=b,updates=3068,
                        additional_supervised_tokens=t.supervised_tokens-parent['supervised_tokens'],additional_input_tokens=t.tokens-parent['tokens'],
                        actual_body_bytes=t.body_bytes-parent['body_bytes'],reference_suffix_teacher_tokens=c['reference_suffix_teacher_tokens'],
                        actual_source_accounting=t.sampler.actual,sampler=t.sampler.state_dict(),token_digest=t.token_digest,
                        reference_token_digest=t.sampler.reference_token_digest,source_digests=t.sampler.source_digests,training_seconds=seconds)
                    atomic_json(progress,result);del t;gc.collect();torch.cuda.empty_cache()
                if 'evaluation' not in result:
                    evaluation.RUN=output/'evaluation';dev=Shard(Path(base['dev_shards']),'dev');tok=Tokenizer(ROOT/base['tokenizer'])
                    result['evaluation']=evaluation.evaluate(ARM,result['checkpoint'],dev,tok,base,b,heartbeat,check,started[0]+c['GPU_budget_seconds']-previous)
                    atomic_json(progress,result)
                prior.RUN=RUN;prior.CONFIG=CONFIG
                cp=dict(path=result['checkpoint']['checkpoint'],sha256=result['checkpoint']['checkpoint_sha256'])
                for suite in ('bridge','retention'):
                    if suite not in result:result[suite]=prior.transfer_scores(c,ARM,cp,heartbeat,check,suite);atomic_json(progress,result)
                result.update(scientific_teacher_tokens=result['checkpoint']['additional_supervised_tokens'],scientific_optimizer_updates=3068,
                    reused_original100M_control_not_new_exposure=True,matched_original_mixed_global_input=True,
                    matched_masked_staged_global_input=False,matched_masked_recipe_teacher_budget=True,matched_original_hard_teacher_budget=False)
            check();elapsed=previous+time.monotonic()-started[0]
            result.update(status='own_masked_CUDA_probe_complete' if probe else 'masked_suffix_GPU_complete_pending_all80_content_review',
                config_sha256=sha256(path),GPU_seconds=elapsed,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
                protected_test_used=False,quality_criteria_unchanged=True)
            atomic_json(output/('result.json' if probe else 'compare-result.json'),result)
            job.update(status='complete',GPU_elapsed_seconds=elapsed,completed_at=now())
    except BaseException as error:job.update(status='failed_or_interrupted',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['GPU_elapsed_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2);parser=argparse.ArgumentParser();modes=parser.add_mutually_exclusive_group()
    for mode in ('prepare','preflight-probe','probe','freeze','inspect'):modes.add_argument('--'+mode,action='store_true')
    args=parser.parse_args()
    if args.prepare:prepare()
    elif args.preflight_probe:inspect(PROBE_CONFIG)
    elif args.freeze:freeze()
    elif args.inspect:inspect(CONFIG)
    else:run(args.probe)
