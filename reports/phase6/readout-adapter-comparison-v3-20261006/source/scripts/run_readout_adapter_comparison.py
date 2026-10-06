"""One measured frozen-readout100M fork, cached ordinary100M control."""
import argparse
import copy
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
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,implementation_hashes,gpu_lock
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from cached_three_source_index import CachedThreeSourceIndex
from condition_relation_language import RelationLanguageTrainView
from readout_adapter_model import POLICY
from readout_adapter_trainer import ReadoutAdapterTrainer,KIND,READOUT_LR
import readout_adapter_evaluation as architecture_evaluation
from phase6_performance import identity,alive,finite_state
from run_eos_short_pilot import equal_state
import probe_readout_adapter as probe
import run_parameter_displacement_anchor_v3 as native
import run_source_order_condition_comparison_v2 as prior
import run_complete_text_comparison as evaluation

RUN=probe.RUN
CONFIG=ROOT/'configs/phase6/readout_adapter_comparison.json'
PROPOSAL=probe.PROPOSAL
ARM='readout_adapter'
GOALS=native.GOALS
TOTAL=100000000
CEILING=900
SOURCES=('scripts/run_readout_adapter_comparison.py','scripts/run_readout_adapter_comparison.ps1',
    'scripts/review_readout_adapter_comparison.py','scripts/record_readout_adapter_content.py',
    'scripts/readout_adapter_evaluation.py','scripts/readout_accounting.py','tests/test_readout_adapter_science.py')
reference,check_reference=probe.reference,probe.check_reference


def probe_evidence():
    c=probe.inspect();job=read_json(RUN/'probe/job.json');r=read_json(RUN/'probe/result.json')
    if (job['status']!='complete' or alive(job) or not r['passed'] or r['GPU_seconds']!=job['GPU_elapsed_seconds']
            or r['GPU_seconds']>120 or r['config_sha256']!=sha256(probe.CONFIG)
            or not all(r['initial_preservation'].values()) or not all(r['resume_gate']['checks'].values())
            or any(not v['passed'] for v in r['architecture']['checks'].values())):
        raise ValueError('Own actually completed architecture/fullstate CUDA gate required')
    timing,estimate=probe.estimate_training(r)
    if r['measured_timing']!=timing or r['estimated_science_GPU_seconds']!=estimate or estimate+r['GPU_seconds']+c['previous_failed_GPU_seconds']>CEILING:
        raise ValueError('Own measured full science plus verification exceeds900s')
    return c,r,timing,estimate


def freeze():
    if CONFIG.exists():inspect();return
    started=time.monotonic();p,r,timing,estimate=probe_evidence();old=copy.deepcopy(p['source'])
    suites=list(ET.parse(ROOT/'reports/phase6/readout_adapter_science_tests.xml').getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=2 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Actual source-match/total-budget CPU test required')
    c=dict(research_kind=KIND,phase='scientific',parent=p['parent'],policy=POLICY,
        readout_LR=READOUT_LR,unique_parameters=10099456,logical_layers=13,
        pool=old['pool'],positive_data=old['positive_data'],original_web=old['original_web'],
        original_config=old['original_config'],accepted_compact_index=old['accepted_compact_index'],strong_control=old['strong_control'],
        teacher_goals=GOALS,teachers_per_arm=TOTAL,new_scientific_teacher_tokens=TOTAL,reused_control_teacher_tokens=TOTAL,
        source_order=list(prior.SOURCE_ORDER),shapes=old['shapes'],coefficients={ARM:0.},
        references=dict(old['references'],**p['references'],own_probe_config=reference(probe.CONFIG),
            own_probe_result=reference(RUN/'probe/result.json'),CPU_science_tests=reference(ROOT/'reports/phase6/readout_adapter_science_tests.xml')),
        old_source_sha256={**p['old_source_sha256'],**p['source_sha256']},source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        implementation=implementation_hashes(),verification_GPU_seconds=r['GPU_seconds']+p['previous_failed_GPU_seconds'],verification_teacher_tokens=r['verification_teacher_tokens'],
        measured_timing=timing,estimated_GPU_seconds_with_margin=estimate,GPU_budget_seconds=CEILING-r['GPU_seconds']-p['previous_failed_GPU_seconds'],
        save_every_updates=250,total_new_GPU_ceiling_seconds=CEILING,CPU_preparation_seconds=time.monotonic()-started,
        quality_criteria_unchanged=True,Base_complete=False,Base_adopted=False,protected_test_used=False,Chat_started=False,quantization_started=False)
    if c['CPU_preparation_seconds']>30:raise TimeoutError('CPU science freeze30s exhausted')
    atomic_json(CONFIG,c);inspect();print(json.dumps(dict(status='readout_adapter100M_science_frozen',estimated_total_GPU_seconds=estimate+c['verification_GPU_seconds'])))


def inspect():
    c=read_json(CONFIG);p,r,timing,estimate=probe_evidence()
    if (c['research_kind']!=KIND or c['phase']!='scientific' or c['parent']!=p['parent'] or c['policy']!=POLICY
            or c['readout_LR']!=READOUT_LR or c['unique_parameters']!=10099456 or c['logical_layers']!=13
            or c['teacher_goals']!=GOALS or c['teachers_per_arm']!=TOTAL or c['new_scientific_teacher_tokens']!=TOTAL
            or c['coefficients']!={ARM:0.} or c['reused_control_teacher_tokens']!=TOTAL or c['source_order']!=list(prior.SOURCE_ORDER)
            or c['shapes']!=p['source']['shapes'] or c['total_new_GPU_ceiling_seconds']!=CEILING
            or c['measured_timing']!=timing or c['estimated_GPU_seconds_with_margin']!=estimate
            or c['verification_GPU_seconds']!=r['GPU_seconds']+p['previous_failed_GPU_seconds'] or c['verification_teacher_tokens']!=r['verification_teacher_tokens']
            or not math.isclose(c['GPU_budget_seconds']+r['GPU_seconds']+p['previous_failed_GPU_seconds'],CEILING,abs_tol=1e-9)
            or c['implementation']!=implementation_hashes() or c['save_every_updates']!=250
            or any(c[k] for k in ('Base_complete','Base_adopted','protected_test_used','Chat_started','quantization_started'))
            or not c['quality_criteria_unchanged']):
        raise ValueError('Frozen sharing scientific scope/budget differs')
    for name,digest in {**c['old_source_sha256'],**c['source_sha256']}.items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen source differs: '+name)
    for ref in (c['parent'],c['strong_control'],c['accepted_compact_index'],c['original_config'],*c['references'].values()):check_reference(ref)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')):raise ValueError('Actual live scientific job; no duplicate')
    return c


def binding(c,path=CONFIG,arm=ARM):
    if path!=CONFIG or arm!=ARM:raise ValueError('Only the frozen sharing candidate binding allowed')
    return dict(config_sha256=sha256(CONFIG),arm=ARM,parent=c['parent'],teacher_goals=GOALS,study_kind=KIND,
        parameter_coefficient=0.,original_web=c['original_web'],positive_manifest_sha256=c['positive_data']['manifest_sha256'],
        policy=POLICY,readout_LR=READOUT_LR,
        optimizer_policy='fresh_readout_only_native_weights_frozen')


def matched_sources(candidate,control):
    keys=('additional_supervised_tokens','additional_input_tokens','source_teachers','source_eos','source_input_tokens',
          'source_body_bytes','focus_token_digest','token_digest','sampler')
    if (not isinstance(candidate,dict) or not isinstance(control,dict)
            or any(k not in candidate or k not in control
                   or type(candidate[k]) is not type(control[k])
                   or not equal_state(candidate[k],control[k]) for k in keys)):
        raise ValueError('New and cached ordinary100M input/target protocols differ')
    return True


def run():
    c=inspect();RUN.mkdir(parents=True,exist_ok=True);jp=RUN/'job.json';previous_job=read_json(jp) if jp.exists() else {}
    if previous_job and previous_job['config_sha256']!=sha256(CONFIG):raise ValueError('Interrupted job recipe differs')
    if previous_job.get('status')=='complete':print('Completed sharing science retained');return
    previous=previous_job.get('GPU_elapsed_seconds',0.);started=None;stopped=[False]
    job=dict(status='setup',**identity(),config_sha256=sha256(CONFIG),started_at=previous_job.get('started_at',now()),GPU_elapsed_seconds=previous,
        restart_command='scripts/run_readout_adapter_comparison.ps1 -Worker')
    for sig in (signal.SIGINT,signal.SIGTERM):signal.signal(sig,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:raise InterruptedError('Sharing science interrupted; completed update checkpoints retained')
        if started is not None and previous+time.monotonic()-started>c['GPU_budget_seconds']:
            raise TimeoutError('Cumulative measured sharing scientific budget exhausted')
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None:job['GPU_elapsed_seconds']=previous+time.monotonic()-started
        atomic_json(jp,job)
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        torch.backends.cuda.matmul.allow_tf32=False;torch.backends.cudnn.allow_tf32=False;heartbeat('setup')
        for relative in (*c['source_sha256'],*c['old_source_sha256'],CONFIG.relative_to(ROOT).as_posix()):
            target=RUN/'source'/relative;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists() and target.read_bytes()!=(ROOT/relative).read_bytes():raise ValueError('Snapshot differs')
            if not target.exists():shutil.copyfile(ROOT/relative,target)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        pool=TrainView(c['pool']['pool'],c['pool']['manifest_sha256']);pool.index=CachedThreeSourceIndex(pool)
        if not pool.index.cache_reused:raise ValueError('Accepted compact cache must be reused')
        original=TrainView(c['original_web']['path'],c['original_web']['manifest_sha256'])
        positive=RelationLanguageTrainView(c['positive_data']['path'],c['positive_data']['manifest_sha256'])
        base=read_json(Path(c['original_config']['path']));b=binding(c)
        with gpu_lock('cuda'):
            started=time.monotonic();job['status']='running';heartbeat('GPU')
            progress=RUN/'progress-result.json';result=read_json(progress) if progress.exists() else dict(checkpoints={},evaluations={},transfer={},retention={})
            if ARM not in result['checkpoints']:
                folder=RUN/ARM/'training';folder.mkdir(parents=True,exist_ok=True)
                trainer=ReadoutAdapterTrainer(parent,pool,original,positive,GOALS,b);checkpoint=prior.latest(folder)
                if checkpoint is not None:trainer.load(checkpoint)
                log=folder/'metrics.jsonl';seconds=prior.reconcile(log,trainer.update,parent['update'])
                with log.open('a',buffering=1) as stream:
                    while trainer.sampler.source_teachers!=GOALS:
                        try:check()
                        except (InterruptedError,TimeoutError):trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt');raise
                        row=trainer.step();seconds+=row['seconds'];stream.write(json.dumps(row,allow_nan=False)+'\n')
                        if trainer.sampler.position%20==0:heartbeat('readout-adapter-Base-training',teachers=row['additional_teacher_tokens'],teacher_budget=TOTAL,
                            loss=row['loss'],source_teachers=row['source_teachers'])
                        if trainer.sampler.position%250==0:trainer.save(folder/f'checkpoint-{trainer.update:08d}.pt')
                checkpoint=folder/f'checkpoint-{trainer.update:08d}.pt';trainer.save(checkpoint)
                if not finite_state(torch.load(checkpoint,map_location='cpu',weights_only=False)):raise ValueError('Finite scientific terminal state required')
                if not probe.native_unchanged(trainer.model,parent):raise ValueError('Frozen native weights changed during science')
                result['checkpoints'][ARM]=dict(prior.detail(trainer,checkpoint,b,seconds),parameter_coefficient=0.,parameter_penalty_teacher_tokens=0,
                    anchor_initial_digest=trainer.anchor_initial_digest,sampler=trainer.sampler.state_dict(),
                    source_body_bytes=trainer.sampler.source_body_bytes.copy(),token_digest=trainer.token_digest,
                    native_weights_unchanged=probe.native_unchanged(trainer.model,parent),unique_parameters=sum(p.numel() for p in trainer.model.parameters()),
                    model_config=trainer.model.config)
                atomic_json(progress,result);del trainer;gc.collect();torch.cuda.empty_cache()
            if ARM not in result['evaluations']:
                evaluation.RUN=RUN/'evaluation';dev=Shard(Path(base['dev_shards']),'dev');tok=Tokenizer(ROOT/base['tokenizer'])
                result['evaluations'][ARM]=architecture_evaluation.evaluate(evaluation,ARM,result['checkpoints'][ARM],dev,tok,base,b,
                    heartbeat,check,started+c['GPU_budget_seconds']-previous)
                atomic_json(progress,result)
            prior.RUN=RUN;prior.CONFIG=CONFIG
            checkpoint=dict(path=result['checkpoints'][ARM]['checkpoint'],sha256=result['checkpoints'][ARM]['checkpoint_sha256'])
            for suite,key in (('bridge','transfer'),('retention','retention')):
                if ARM not in result[key]:
                    result[key][ARM]=architecture_evaluation.transfer_scores(prior,c,ARM,checkpoint,heartbeat,check,suite)
                    atomic_json(progress,result)
            cached=read_json(native.RUN/'compare-result.json')
            matched_sources(result['checkpoints'][ARM],cached['checkpoints']['matched_staged_CE'])
            check();elapsed=previous+time.monotonic()-started
            result.update(status='readout_adapter100M_GPU_complete_pending_all80_content',config_sha256=sha256(CONFIG),GPU_seconds=elapsed,
                scientific_teacher_tokens=TOTAL,reused_control_teacher_tokens=TOTAL,reused_control=reference(native.RUN/'compare-result.json'),
                all_scientific_input_streams_match=True,evaluation_model_class='ReadoutAdapterModel',
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,quality_criteria_unchanged=True)
            atomic_json(RUN/'compare-result.json',result);job.update(status='complete',GPU_elapsed_seconds=elapsed,completed_at=now())
    except BaseException as exc:job.update(status='failed_or_interrupted',error=repr(exc));raise
    finally:
        if started is not None and job['status']!='complete':job['GPU_elapsed_seconds']=previous+time.monotonic()-started
        atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();m=parser.add_mutually_exclusive_group();m.add_argument('--freeze',action='store_true');m.add_argument('--inspect',action='store_true')
    args=parser.parse_args()
    if args.freeze:freeze()
    elif args.inspect:inspect();print('Measured sharing science valid; GPU0')
    else:run()
