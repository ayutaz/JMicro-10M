"""Persistent training-only dropout100M Base; reuse completed ordinary CE control."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,sha256,now
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from base_residual_dropout import ResidualDropoutTrainer, KIND, PROBABILITY
from jmicro.phase5 import equal_state
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive,finite_state
import run_complete_text_comparison as evaluation

CONFIG=ROOT/'configs/phase6/base_residual_dropout_comparison.json'
RUN=ROOT/'reports/phase6/base-residual-dropout-comparison-20261007'
PROBE=ROOT/'reports/phase6/base-residual-dropout-probe-20261007'
CONTROL=ROOT/'reports/phase6/natural-context-contrast-comparison-20261007'
SOURCES=('scripts/run_base_residual_dropout.py','scripts/run_base_residual_dropout.ps1',
    'scripts/natural_context_contrast_corpus.py','scripts/natural_context_contrast_trainer.py',
    'scripts/base_residual_dropout.py',
    'scripts/natural_context_contrast_memory.py','src/jmicro/model.py','src/jmicro/training.py',
    'src/jmicro/readiness.py','src/jmicro/shards.py','src/jmicro/tokenizer.py','src/jmicro/japanese_evaluation.py',
    'scripts/run_complete_text_comparison.py','scripts/run_eos_short_pilot.py','scripts/evaluate_japanese_base.py',
    'scripts/prepare_japanese_evaluation.py','src/jmicro/evaluation_memory.py','uv.lock')


def ref(path):return dict(path=str(path),sha256=sha256(path))


def matched_control_checks(left,right):
    return {k:equal_state(left['counters'][k],right['counters'][k]) for k in
        ('update','token_digest','supervised_tokens','source_teachers','source_EOS',
         'CE_input_tokens','original_body_bytes','auxiliary_input_tokens','auxiliary_pairs','physical_input_tokens')} | {'full_sampler':equal_state(left['sampler'],right['sampler'])}


def finite_dropout_state(state):
    return (finite_state(state) and state['kind']==KIND and state['spec']['regularization']['probability']==PROBABILITY
            and state['model_config']['dropout']==0 and state['model_config']['expected_parameter_count']==10001152)


def freeze():
    if CONFIG.exists():raise ValueError('Preserve frozen dropout scientific comparison')
    result=json.loads((PROBE/'result.json').read_text());job=json.loads((PROBE/'job.json').read_text())
    probe=json.loads((ROOT/'configs/phase6/base_residual_dropout_probe.json').read_text())
    if (job['status']!='complete' or alive(job) or not result['passed']
            or not all(result['resume_checks'].values()) or not all(result['initial_checks'].values())):
        raise ValueError('Actual completed dropout source/initialization/CUDA/full-state resume gate required')
    tests=ROOT/'reports/phase6/base_residual_dropout_run_tests.xml'
    suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if not suites or sum(int(s.attrib['tests']) for s in suites)<3 or any(
            int(s.attrib[k]) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('Actual successful runner protocol checks required')
    batch=result['selected_matched_batch']
    if batch!=48 or result['capacity'][str(batch)]['peak_VRAM_bytes']>=result['memory_policy']['allocator_allowance_bytes']:
        raise ValueError('Actual cached-control batch48 must be resident-eligible')
    control_job=json.loads((CONTROL/'job.json').read_text())
    if control_job['status']!='complete' or alive(control_job):raise ValueError('Cached control scientific job must be ended')
    controls={a:json.loads((CONTROL/a/'train-result.json').read_text()) for a in ('CE',)}
    if any(r['status']!='complete' or r['scientific_CE_teacher_tokens']!=100000000 for r in controls.values()):
        raise ValueError('Cached ordinary CE exact100M control required')
    old=json.loads((ROOT/'configs/phase6/natural_context_contrast_comparison.json').read_text())
    if old['parent']!=probe['parent'] or old['source_binding']!=probe['source_binding'] or old['goals']!=probe['goals'] or old['batch']!=batch:
        raise ValueError('Parent/source/goals/batch differs from cached scientific controls')
    estimate=100000000/result['timings'][str(batch)]['median_CE_targets_per_second']
    c=dict(created_at=now(),probe_result=ref(PROBE/'result.json'),probe_job=ref(PROBE/'job.json'),
        proposal=probe['proposal'],control_CE=ref(CONTROL/'CE/train-result.json'),CPU_run_tests=ref(tests),
        parent=probe['parent'],parent_size=probe['parent_size'],parent_mtime_ns=probe['parent_mtime_ns'],
        source_binding=probe['source_binding'],batch=batch,seed=42,goals=probe['goals'],
        arms=['dropout'],scientific_CE_teacher_tokens=100000000,CE_tokens_per_arm=100000000,
        reused_control_CE_teachers=100000000,reused_control_GPU_seconds=0,
        native_parameters=10001152,train_only_parameters=0,training_parameters=10001152,
        resident_allocator_fraction=.90,worst_measured_peak_bytes=result['capacity'][str(batch)]['peak_VRAM_bytes'],
        training_forecast_seconds=estimate,GPU_budget_seconds=math.ceil(1.5*estimate+600),
        checkpoints_every_updates=250,heartbeat_every_updates=20,
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},dev_shards=old['dev_shards'],
        dev_manifest_sha256=old['dev_manifest_sha256'],tokenizer=old['tokenizer'],tokenizer_sha256=old['tokenizer_sha256'],
        suite_sha256=old['suite_sha256'],evaluation=old['evaluation'],
        regularization_probability=.1,optimizer='same_fresh_AdamW_lr1e-5_weight_decay0.1_constant_schedule',
        data_policy='Same accepted2B original TRAIN source/seed/genre quotas/document-local1024_stride512_CE/batch48 as cached ordinary CE control; no auxiliary loss or extra forward passes. Exact final genre teacher masks, original EOS only; training-only inverted0.1 dropout on embeddings and both residual branches; native evaluator loads plain weights.',
        accounting='Same100M teachers/input/source/EOS/full sampler as completed CE; report dropout GPU overhead separately. Repeated draws are exposures, not new unique supply.',
        quality_targets_unchanged=True,Base_complete=False,Chat_started=False,quantization_started=False,
        verification_GPU_seconds=result['GPU_occupancy_seconds'],
        verification_CE_teachers=result['verification_CE_teacher_tokens'],
        completion='One exact100M completed native/Adam/scheduler/RNG/sampler checkpoint; identical source/teachers/EOS/input/physical/digest/cursor to cached ordinary CE control. Native evaluator installs no training hooks for fixed dev256/semantics192/JBLiMP331/JCQA1119/all80. Full individual content review and unchanged strong/matched/absolute/historical Web criteria then decide. Independent learned seed/full DEV/protected final TEST/adoption remain required; no automatic acceptance or extension.',
        failure_policy='Close fixed dropout0.1 and three sites if failed; no probability/sites/LR/source/checkpoint/epoch sweep or automatic extension. Preserve valid completed-update checkpoints; resume only within same frozen budget.')
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='scientific_frozen_not_started',config_sha256=sha256(CONFIG),batch=batch,
                          forecast_seconds=estimate,GPU_budget_seconds=c['GPU_budget_seconds'])))


def inspect():
    c=json.loads(CONFIG.read_text())
    if (RUN/'job.json').exists() and alive(json.loads((RUN/'job.json').read_text())):
        raise ValueError('Actual scientific process is already alive; do not stop UI or duplicate job')
    for name in ('probe_result','probe_job','proposal','control_CE','CPU_run_tests'):
        if sha256(Path(c[name]['path']))!=c[name]['sha256']:raise ValueError('Original gate reference differs: '+name)
    for name,value in c['source_sha256'].items():
        if sha256(ROOT/name)!=value:raise ValueError('Frozen scientific source changed: '+name)
    stat=Path(c['parent']['path']).stat()
    if (stat.st_size,stat.st_mtime_ns)!=(c['parent_size'],c['parent_mtime_ns']):raise ValueError('Original verified parent identity differs')
    if sha256(ROOT/c['tokenizer'])!=c['tokenizer_sha256'] or sha256(ROOT/'eval/base.jsonl')!=c['suite_sha256']:
        raise ValueError('Fixed tokenizer/generation suite differs')
    if sha256(Path(c['dev_shards'])/'manifest.json')!=c['dev_manifest_sha256']:
        raise ValueError('Fixed dev source differs')
    if sha256(ROOT/c['evaluation']['config'])!=c['evaluation']['config_sha256']:
        raise ValueError('Fixed Japanese evaluation config differs')
    return c


def latest_checkpoint(folder):
    paths=list(folder.glob('checkpoint-*.pt'))
    return max(paths,key=lambda p:int(p.stem.split('-')[-1])) if paths else None


def run():
    c=inspect();path=RUN/'job.json';previous=json.loads(path.read_text()) if path.exists() else {}
    if previous:
        if alive(previous):raise ValueError('Same scientific job is already alive')
        if previous['config_sha256']!=sha256(CONFIG):raise ValueError('Previous scientific job binding differs')
        if previous['status']=='complete':print('Completed scientific comparison retained');return
    RUN.mkdir(parents=True,exist_ok=True)
    prior=previous.get('GPU_occupancy_seconds',0);started=None;stopped=False;t=None
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        GPU_occupancy_seconds=prior,Base_complete=False,Chat_started=False,quantization_started=False,
        restart_command='scripts/run_base_residual_dropout.ps1 -Worker; inspect actual PID/boot/start first; resume only valid completed-update checkpoints within same frozen budget')
    atomic_json(path,job)
    def stop(*args):
        nonlocal stopped
        stopped=True
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    def check():
        if stopped:raise InterruptedError('Stop requested; preserve completed update')
        if started is not None and prior+time.monotonic()-started>c['GPU_budget_seconds']:
            raise TimeoutError('Frozen scientific cumulative GPU budget exhausted')
    def beat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None:job['GPU_occupancy_seconds']=prior+time.monotonic()-started
        atomic_json(path,job)
    def save_checkpoint(folder):
        checkpoint=folder/f"checkpoint-{t.counters['update']:08d}.pt"
        t.save(checkpoint);job['latest_checkpoint']=str(checkpoint)
        return checkpoint
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        memory=configure_resident_memory(c['worst_measured_peak_bytes'])
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        tokenizer=Tokenizer(ROOT/c['tokenizer']);dev=Shard(Path(c['dev_shards']),'dev')
        evaluation.RUN=RUN/'evaluation'
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,target)
        results={}
        with gpu_lock('cuda'):
            started=time.monotonic();job['status']='running';job['resident_memory_policy']=memory
            for arm in c['arms']:
                folder=RUN/arm;folder.mkdir(parents=True,exist_ok=True)
                terminal=folder/'train-result.json'
                binding=dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256=sha256(CONFIG),
                    weights_role='scientific_'+arm,sources=c['source_sha256'])
                if terminal.exists():
                    record=json.loads(terminal.read_text())
                    if record['binding']!=binding or record['scientific_CE_teacher_tokens']!=100000000:
                        raise ValueError('Saved scientific terminal differs')
                else:
                    source=OriginalTrainCorpusSampler(c['source_binding']['pool'],c['source_binding']['manifest_sha256'],tokenizer,c['goals'],42)
                    if source.binding!=c['source_binding']:raise ValueError('Original accepted TRAIN source differs')
                    t=ResidualDropoutTrainer(parent,source,binding,batch=c['batch'])
                    last=latest_checkpoint(folder)
                    if last:t.load(last)
                    attempt_id=f"{job['pid']}-{job['start_ticks']}"
                    with (folder/('metrics-'+attempt_id+'.jsonl')).open('x',buffering=1) as log:
                        beat(arm+'-training',scientific_CE_teacher_tokens=t.counters['supervised_tokens'],local_update=t.counters['update'])
                        while not t.sampler.exhausted:
                            check();row=t.step();log.write(json.dumps(row,allow_nan=False)+'\n')
                            if t.counters['update']%250==0:save_checkpoint(folder)
                            if t.counters['update']%20==0:
                                beat(arm+'-training',scientific_CE_teacher_tokens=t.counters['supervised_tokens'],local_update=t.counters['update'],loss=row['combined_loss'])
                    checkpoint=save_checkpoint(folder)
                    if t.counters['supervised_tokens']!=100000000 or t.counters['source_teachers']!=c['goals']:
                        raise ValueError('Exact scientific source teacher budget not achieved')
                    if not finite_dropout_state(torch.load(checkpoint,map_location='cpu',weights_only=False)):
                        raise ValueError('Nonfinite scientific terminal native/Adam')
                    record=dict(status='complete',binding=binding,checkpoint=str(checkpoint),checkpoint_sha256=sha256(checkpoint),
                        scientific_CE_teacher_tokens=100000000,counters=t.counters.copy(),sampler=t.sampler.state_dict(),
                        parent_CE_teacher_tokens=parent['supervised_tokens'],completed_at=now(),Base_complete=False)
                    atomic_json(terminal,record);del t;t=None;gc.collect();torch.cuda.empty_cache()
                beat(arm+'-evaluation')
                evaluated=evaluation.evaluate(arm,record,dev,tokenizer,c,binding,beat,check,
                    started+c['GPU_budget_seconds']-prior)
                results[arm]=dict(training=record,evaluation=evaluated)
                atomic_json(RUN/'partial-result.json',results)
            common={}
            for arm in ('CE',):
                control=json.loads(Path(c['control_'+arm]['path']).read_text())
                common[arm]=matched_control_checks(results['dropout']['training'],control)
            if not all(all(checks.values()) for checks in common.values()):
                raise ValueError('Dropout CE source trace/counters/full sampler differ from cached controls')
            check();elapsed=prior+time.monotonic()-started
            result=dict(status='complete',results=results,common_CE_checks=common,scientific_CE_teacher_tokens=100000000,
                reused_control_CE_teachers=100000000,reused_control_GPU_seconds=0,
                GPU_occupancy_seconds=elapsed,actual_identity=identity(),config_sha256=sha256(CONFIG),
                Base_complete=False,Chat_started=False,quantization_started=False,
                next_action='Read all80 new native generation outputs; reuse existing80 CE control notes. Score unchanged strong/matched/absolute/historical Web Base gates and paired uncertainty. Qualification is still required before independent learned seed/full DEV/protected final TEST/adoption. Chat and quantization remain outside scope.')
            atomic_json(RUN/'result.json',result);job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=elapsed)
            atomic_json(path,job);print(json.dumps(dict(status='scientific_complete_quality_review_pending',GPU_seconds=elapsed)))
    except BaseException as exc:
        if t is not None and t.counters['source_teachers']==t.sampler.consumed:
            save_checkpoint(RUN/arm)
        job.update(status='failed_or_interrupted',error=repr(exc),ended_at=now(),
            GPU_occupancy_seconds=prior+time.monotonic()-started if started is not None else prior)
        atomic_json(path,job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument('--freeze',action='store_true');g.add_argument('--inspect',action='store_true');a=p.parse_args()
    if a.freeze:freeze()
    elif a.inspect:inspect();print('Frozen scientific source/evaluation/parent inspected; no training')
    else:run()
