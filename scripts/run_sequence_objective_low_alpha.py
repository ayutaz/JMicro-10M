"""One predeclared alpha0.01 experiment with the unchanged actual CE control."""
import argparse
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

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.eos_pilot import TrainView
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, implementation_hashes, gpu_lock
from phase6_performance import alive, identity, finite_state
from run_eos_short_pilot import equal_state
from sequence_objective_trainer import SequenceObjectiveTrainer
from cached_three_source_index import CachedThreeSourceIndex
import run_sequence_objective_comparison as old
import run_complete_text_comparison as evaluation
from measure_sequence_objective_timing import validate_timing

RUN = ROOT / 'reports/phase6/sequence-objective-low-alpha-20261006'
PROBE_CONFIG = ROOT / 'configs/phase6/sequence_objective_low_alpha_probe.json'
CONFIG = ROOT / 'configs/phase6/sequence_objective_low_alpha.json'
DIAG = ROOT / 'reports/phase6/sequence-objective-diagnostic-20261006'
TOTAL = 25000000
OBJECTIVE = dict(alpha=.01, every_updates=4, prefixes=8, prefix_tokens=32, max_new_tokens=64, ngram=4)
SOURCES = ('scripts/run_sequence_objective_low_alpha.py', 'scripts/run_sequence_objective_low_alpha.ps1',
           'scripts/review_sequence_objective_low_alpha.py', 'scripts/cached_three_source_index.py',
           *old.SOURCES)


def reference(path):
    return dict(path=str(path), sha256=sha256(path))


def source_contract():
    c, base, parent = old.preflight(old.CONFIG)
    job = read_json(old.RUN / 'job.json'); result = read_json(old.RUN / 'compare-result.json')
    review = read_json(old.RUN / 'review.json')
    assert job['status'] == 'complete' and not alive(job)
    assert result['config_sha256'] == sha256(old.CONFIG) and result['scientific_teacher_tokens'] == 50000000
    assert review['result_sha256'] == sha256(old.RUN / 'compare-result.json')
    assert not review['objective_comparison']['passed'] and not review['Base_adopted']
    diagnosis = read_json(DIAG / 'result.json'); dj = read_json(DIAG / 'job.json')
    assert dj['status'] == 'complete' and not alive(dj) and dj['gpu_elapsed_seconds'] <= 60
    assert diagnosis['optimizer_updates'] == diagnosis['scientific_teacher_tokens'] == 0
    assert diagnosis['checkpoints']['parent']['checkpoint'] == c['parent']
    assert all(d['exact_parameters_unchanged'] and d['RNG_restored'] for d in diagnosis['checkpoints'].values())
    control = result['checkpoints']['CE']; ev = result['evaluations']['CE']
    assert control['binding']['sequence_objective'] == dict(OBJECTIVE, alpha=0.)
    assert control['binding']['parent'] == c['parent'] and control['additional_supervised_tokens'] == TOTAL
    assert sha256(Path(control['checkpoint'])) == control['checkpoint_sha256']
    assert ev['checkpoint_sha256'] == control['checkpoint_sha256'] and ev['binding'] == control['binding']
    assert ev['evaluation_RNG_isolated'] and not ev['protected_test_used']
    for relative, digest in c['source_sha256'].items():
        assert sha256(ROOT / relative) == digest, 'Scientific control training/evaluation source changed'
    return c, base, parent, result


def prepare():
    if PROBE_CONFIG.exists():
        inspect(PROBE_CONFIG); return
    c, _, _, _ = source_contract()
    plan = dict(kind='low-alpha-probe', parent=c['parent'], pool=c['pool'], peak_lr=c['peak_lr'],
        CE_teachers=TOTAL, objective=OBJECTIVE, prior_config=reference(old.CONFIG),
        prior_result=reference(old.RUN / 'compare-result.json'), prior_review=reference(old.RUN / 'review.json'),
        diagnosis=reference(DIAG / 'result.json'),
        control_notes=reference(ROOT / 'reports/phase6/sequence_objective_CE_notes.json'),
        control_generation=reference(old.RUN / 'evaluation/CE/evaluation/generation.json'),
        implementation=implementation_hashes(), source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        GPU_budget_seconds=300, total_new_GPU_ceiling_seconds=1800,
        scientific_teacher_tokens=0, new_teacher_tokens_planned=TOTAL, compared_teacher_tokens=2*TOTAL,
        control_reused_without_training_or_evaluation=True, quality_criteria_unchanged=True,
        protected_test_used=False, Base_adopted=False, Chat_adopted=False,
        requested_five_steps_complete=False)
    atomic_json(PROBE_CONFIG, plan)
    print('Actual source-bound alpha0.01 probe frozen; GPU not started', flush=True)


def inspect(path):
    c = read_json(path); original, base, parent, result = source_contract()
    assert c['objective'] == OBJECTIVE and c['CE_teachers'] == TOTAL
    assert c['parent'] == original['parent'] and c['pool'] == original['pool'] and c['peak_lr'] == original['peak_lr']
    for name in ('prior_config', 'prior_result', 'prior_review', 'diagnosis', 'control_notes', 'control_generation'):
        assert sha256(Path(c[name]['path'])) == c[name]['sha256']
    assert c['source_sha256'] == {p:sha256(ROOT/p) for p in SOURCES}
    assert c['implementation'] == implementation_hashes() and c['quality_criteria_unchanged'] and not c['protected_test_used']
    assert c['control_reused_without_training_or_evaluation'] and c['total_new_GPU_ceiling_seconds'] == 1800
    output = RUN / 'probe' if path == PROBE_CONFIG else RUN
    if (output/'job.json').exists() and alive(read_json(output/'job.json')):
        raise ValueError('Actual low-alpha job is live; do not duplicate')
    if path == CONFIG:
        probe = probe_evidence()
        assert c['probe_config_sha256'] == sha256(PROBE_CONFIG)
        assert c['probe_result_sha256'] == sha256(RUN/'probe/result.json')
        assert c['verification_GPU_seconds'] == probe['GPU_seconds']
        assert c['verification_teacher_tokens'] == probe['verification_teacher_tokens']
        timing, estimate = estimate_training(probe['timing'])
        assert c['timings'] == timing and c['estimate_with_margin'] == estimate
        assert math.isclose(c['GPU_budget_seconds']+probe['GPU_seconds'],1800,abs_tol=1e-9)
        assert estimate + probe['GPU_seconds'] <= 1800
    else:
        assert path == PROBE_CONFIG and c['kind'] == 'low-alpha-probe' and c['GPU_budget_seconds'] == 300
    return c, base, parent, result


def probe_evidence():
    job = read_json(RUN/'probe/job.json'); p = read_json(RUN/'probe/result.json')
    assert job['status'] == 'complete' and not alive(job) and p['passed']
    assert p['config_sha256'] == job['config_sha256'] == sha256(PROBE_CONFIG)
    assert all(p['gate']['checks'].values()) and p['gate']['GPU_optimizer_updates'] == 8
    assert p['timing']['GPU_optimizer_updates'] == 16 and len(p['timing']['histories']) == 16
    assert p['GPU_seconds'] == job['gpu_elapsed_seconds'] <= 300
    assert p['scientific_teacher_tokens'] == 0 and p['weights_discarded_for_science']
    assert p['verification_teacher_tokens'] == p['gate']['verification_teacher_tokens'] + p['timing']['verification_teacher_tokens']
    assert sha256(Path(p['timing']['checkpoint'])) == p['timing']['checkpoint_sha256']
    return p


def estimate_training(timing):
    rows = timing['histories']
    assert len(rows) == 16 and timing['verification_teacher_tokens'] > 0
    assert all(math.isfinite(r['seconds']) and r['seconds'] > 0 for r in rows)
    steady = rows[4:]
    ordinary = statistics.median(r['seconds'] for i,r in enumerate(steady) if i%4 != 3)
    rollout = statistics.median(r['seconds'] for i,r in enumerate(steady) if i%4 == 3)
    updates = math.ceil(TOTAL/(timing['verification_teacher_tokens']/16)); extra = updates//4
    seconds = (updates-extra)*ordinary + extra*rollout
    return dict(ordinary_seconds=ordinary, rollout_seconds=rollout, updates=updates,
                estimated_training_seconds=seconds, measured_updates=16, warmup_counted=4), seconds*1.3+480


def freeze():
    if CONFIG.exists():
        inspect(CONFIG); return
    c, _, _, _ = inspect(PROBE_CONFIG); probe = probe_evidence()
    timing, estimate = estimate_training(probe['timing'])
    if estimate+probe['GPU_seconds'] > 1800:
        raise ValueError('Measured candidate cannot fit unchanged1800s ceiling')
    c.update(kind='low-alpha-scientific-comparison', probe_config_sha256=sha256(PROBE_CONFIG),
        probe_result_sha256=sha256(RUN/'probe/result.json'), verification_GPU_seconds=probe['GPU_seconds'],
        verification_teacher_tokens=probe['verification_teacher_tokens'],
        GPU_budget_seconds=1800-probe['GPU_seconds'], timings=timing, estimate_with_margin=estimate)
    atomic_json(CONFIG,c); print(json.dumps(dict(status='measured recipe frozen',timings=timing,estimate=estimate)),flush=True)


def binding(c,path):
    return dict(config_sha256=sha256(path), parent=c['parent'], arm='CE_UL', peak_lr=c['peak_lr'],
                warmup_updates=0, optimizer_policy='inherit', initialization='completed-parent-objective-fork',
                curve_mode='decay', curve_boundaries=[TOTAL], short_manifest_sha256=c['pool']['manifest_sha256'],
                sequence_objective=c['objective'])


def resume_gate(build, folder, config_sha, check, control_history):
    record = folder/'result.json'
    if record.exists():
        result=read_json(record); assert result['passed'] and result['config_sha256']==config_sha; return result
    states=[]; histories=[]; teachers=0; inputs=0
    for route in ('continuous','resumed'):
        trainer=build(); before=trainer.supervised_tokens,trainer.tokens; rows=[]
        for i in range(4):
            check(); rows.append(trainer.step())
            if route=='resumed' and i==1:
                split=folder/'split.pt'; trainer.save(split)
                del trainer; gc.collect(); torch.cuda.empty_cache(); trainer=build(); trainer.load(split)
        teachers+=trainer.supervised_tokens-before[0]; inputs+=trainer.tokens-before[1]
        target=folder/(route+'.pt'); trainer.save(target)
        states.append(torch.load(target,map_location='cpu',weights_only=False)); histories.append(rows)
        del trainer; gc.collect(); torch.cuda.empty_cache()
    checks={k:equal_state(states[0][k],states[1][k]) for k in
        ('model','optimizer','scheduler','rng','sampler','lineage','tokens','supervised_tokens','body_bytes',
         'token_digest','update','spec','model_config','pilot_binding')}
    for key in ('loss','sequence_UL','optimization_loss','gradient_norm','lr','token_digest','source_teachers','sequence_objective'):
        checks['history_'+key]=all(equal_state(a[key],b[key]) for a,b in zip(*histories,strict=True))
    checks['finite']=all(finite_state(s) for s in states)
    checks['actual_rollout']=all(h[-1]['sequence_objective']['rollout_batches']==1 and h[-1]['sequence_objective']['skipped_rollouts']==0 for h in histories)
    checks['unchanged_control_input_trajectory']=all(
        equal_state(a[k],b[k]) for a,b in zip(histories[0],control_history,strict=True)
        for k in ('token_digest','source_teachers','valid_input_tokens','physical_input_tokens','lr'))
    assert all(checks.values()),checks
    result=dict(passed=True,checks=checks,histories=histories,config_sha256=config_sha,
                GPU_optimizer_updates=8,verification_teacher_tokens=teachers,verification_input_tokens=inputs)
    atomic_json(record,result); return result


def run(probe=False):
    path=PROBE_CONFIG if probe else CONFIG; c,base,parent,prior_result=inspect(path)
    output=RUN/'probe' if probe else RUN; output.mkdir(parents=True,exist_ok=True)
    jp=output/'job.json'; kept=read_json(jp) if jp.exists() else {}
    if kept:
        assert kept['config_sha256']==sha256(path) and not alive(kept)
        if kept['status']=='complete':print('Completed job retained');return
    previous=kept.get('gpu_elapsed_seconds',0.); started=[None]; stopped=[False]
    job=dict(status='running',**identity(),config_sha256=sha256(path),started_at=kept.get('started_at',now()),
        gpu_elapsed_seconds=previous,Base_adopted=False,protected_test_used=False,
        restart_command=f"scripts/run_sequence_objective_low_alpha.ps1 -Mode {'Probe' if probe else 'Train'} -Worker")
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True))
    signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Stop requested; completed updates retained')
        if started[0] is not None and previous+time.monotonic()-started[0]>c['GPU_budget_seconds']:
            raise TimeoutError('Cumulative low-alpha GPU budget exhausted')
    def heartbeat(stage,**extra):
        check();job.update(stage=stage,heartbeat_at=now(),**extra)
        if started[0] is not None:job['gpu_elapsed_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)
    try:
        heartbeat('index'); torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
        for relative in (*SOURCES,path.relative_to(ROOT).as_posix()):
            target=output/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists():assert target.read_bytes()==(ROOT/relative).read_bytes()
            else:shutil.copyfile(ROOT/relative,target)
        web=TrainView(base['web_shards'],base['web_manifest_sha256'])
        pool=TrainView(c['pool']['pool'],c['pool']['manifest_sha256'])
        pool.index=CachedThreeSourceIndex(pool,lambda **values:heartbeat('index',**values))
        b=binding(c,path)
        def build():return SequenceObjectiveTrainer(parent,web,pool,'shuffle',dict(web=0,short=TOTAL),b)
        with gpu_lock('cuda'):
            started[0]=time.monotonic()
            if probe:
                control=read_json(old.RUN/'probe/resume-gate/CE/result.json')['histories'][0]
                gate=resume_gate(build,output/'resume-gate',sha256(path),check,control)
                heartbeat('resume-verified')
                folder=output/'timing';folder.mkdir(exist_ok=True)
                trainer=build();initial_update=parent['update'];initial_teachers=parent['supervised_tokens']
                latest=old.latest_checkpoint(folder)
                if latest is not None:trainer.load(latest)
                log=folder/'metrics.jsonl';old.reconcile_metrics(log,trainer.update)
                with log.open('a',buffering=1) as stream:
                    while trainer.update-initial_update<16:
                        try:check()
                        except (InterruptedError,TimeoutError):trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt');raise
                        row=trainer.step();stream.write(json.dumps(row,allow_nan=False)+'\n')
                        trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt')
                        heartbeat('continuous-timing',completed_updates=trainer.update-initial_update)
                cp=old.latest_checkpoint(folder);rows=[json.loads(s) for s in log.read_text().splitlines()]
                validate_timing(rows,torch.load(cp,map_location='cpu',weights_only=False),initial_update,initial_teachers)
                timing=dict(histories=rows,GPU_optimizer_updates=16,verification_teacher_tokens=trainer.supervised_tokens-initial_teachers,
                    checkpoint=str(cp),checkpoint_sha256=sha256(cp))
                result=dict(status='actual_low_alpha_resume_and_continuous_timing_complete',passed=True,
                    config_sha256=sha256(path),gate=gate,timing=timing,
                    verification_teacher_tokens=gate['verification_teacher_tokens']+timing['verification_teacher_tokens'],
                    scientific_teacher_tokens=0,weights_discarded_for_science=True)
                del trainer;gc.collect();torch.cuda.empty_cache()
            else:
                progress=output/'progress-result.json'
                result=read_json(progress) if progress.exists() else dict(checkpoints={'CE':prior_result['checkpoints']['CE']},
                    evaluations={'CE':prior_result['evaluations']['CE']},control_reused=True)
                if 'CE_UL' not in result['checkpoints']:
                    trainer=build();folder=output/'CE_UL/training';folder.mkdir(parents=True,exist_ok=True)
                    latest=old.latest_checkpoint(folder)
                    if latest is not None:trainer.load(latest)
                    log=folder/'metrics.jsonl';seconds=old.reconcile_metrics(log,trainer.update)
                    with log.open('a',buffering=1) as stream:
                        while trainer.sampler.source_teachers['short']<TOTAL:
                            try:check()
                            except (InterruptedError,TimeoutError):trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt');raise
                            row=trainer.step();seconds+=row['seconds'];stream.write(json.dumps(row,allow_nan=False)+'\n')
                            if trainer.sampler.position%20==0:heartbeat('CE_UL-training',teachers=trainer.sampler.source_teachers['short'],teacher_budget=TOTAL,loss=row['loss'],sequence_UL=row['sequence_UL'])
                            if trainer.sampler.position%100==0:trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt')
                    cp=folder/f'checkpoint-{trainer.update:08d}.pt';trainer.save(cp)
                    record=old.detail(trainer,cp,b,seconds);record['sequence_objective']=trainer.lineage['sequence_objective']
                    result['checkpoints']['CE_UL']=record;atomic_json(progress,result)
                    del trainer;gc.collect();torch.cuda.empty_cache()
                if 'CE_UL' not in result['evaluations']:
                    evaluation.RUN=output/'evaluation'
                    result['evaluations']['CE_UL']=evaluation.evaluate('CE_UL',result['checkpoints']['CE_UL'],
                        Shard(Path(base['dev_shards']),'dev'),Tokenizer(ROOT/base['tokenizer']),base,b,
                        heartbeat,check,started[0]+c['GPU_budget_seconds']-previous)
                    atomic_json(progress,result)
                result.update(status='matched_low_alpha_learning_complete_pending_all80_content',
                    config_sha256=sha256(path),new_scientific_teacher_tokens=TOTAL,compared_teacher_tokens=2*TOTAL,
                    verification_teacher_tokens=c['verification_teacher_tokens'],verification_GPU_seconds=c['verification_GPU_seconds'],
                    Base_adopted=False,Chat_adopted=False,protected_test_used=False,requested_five_steps_complete=False)
            heartbeat('complete');job.update(status='complete',completed_at=now())
            elapsed=previous+time.monotonic()-started[0]
            if probe:result['GPU_seconds']=elapsed
            else:result['new_scientific_GPU_seconds']=elapsed
            job['gpu_elapsed_seconds']=elapsed
            atomic_json(output/('result.json' if probe else 'compare-result.json'),result)
    except BaseException as error:
        job.update(status='failed',error=repr(error));raise
    finally:
        if started[0] is not None and job['status']!='complete':job['gpu_elapsed_seconds']=previous+time.monotonic()-started[0]
        atomic_json(jp,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group()
    for mode in ('prepare-probe','preflight-probe','probe','freeze','inspect'):group.add_argument('--'+mode,action='store_true')
    args=parser.parse_args()
    if args.prepare_probe:prepare()
    elif args.preflight_probe:inspect(PROBE_CONFIG)
    elif args.freeze:freeze()
    elif args.inspect:inspect(CONFIG)
    else:run(args.probe)
