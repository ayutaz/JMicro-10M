"""Durable exact-parent teacher-decay continuation to cumulative2B, Base only."""
import argparse
import gc
import json
import os
from pathlib import Path
import signal
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.training import atomic_json,gpu_lock
from jmicro.tokenizer import Tokenizer
from jmicro.shards import Shard
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from base_teacher_decay_trainer import TeacherDecayTrainer,committed_decay,policy,KIND
from base_teacher_decay_2b_protocol import (TOTAL,START,EXTRA,ancestry_binding,compact_update,
                                         common_stream,resume_probe)
from base_parallel_residual_evaluation import typed_native_evaluation
from run_base_parallel_residual import build_trainer
from run_base_residual_seen_train import wait_ui
from phase6_performance import alive,identity
import run_complete_text_comparison as native_evaluation

PHASE=ROOT/'reports/phase6'
CONFIG=ROOT/'configs/phase6/base_teacher_decay_2b.json'
RUN=PHASE/'base-teacher-decay-2b-20261008'
PROPOSAL=PHASE/'base_teacher_decay_2b_proposal.json'
LOCAL=('scripts/run_base_teacher_decay_2b.py','scripts/run_base_teacher_decay_2b.ps1',
       'scripts/base_teacher_decay_2b_protocol.py','scripts/review_base_teacher_decay_2b.py',
       'tests/test_base_teacher_decay_2b.py')


def ref(path): return dict(path=str(path),sha256=sha256(path))


def verified_path(value):
    path=Path(value['path'])
    if sha256(path)!=value['sha256']: raise ValueError('Frozen reference differs: '+str(path))
    return path


def checked(value):
    return read_json(verified_path(value))


def freeze():
    if CONFIG.exists() or RUN.exists(): raise ValueError('Preserve prospective2B continuation')
    p=read_json(PROPOSAL);pilot=checked(p['pilot_config']);completion=checked(p['pilot_completion'])
    if (not completion['exploratory_advance_eligible'] or not all(completion['prospective_advance_screen'].values())
            or p['initial_scientific_teacher_tokens']!=START or p['final_scientific_teacher_tokens']!=TOTAL
            or p['new_scientific_teacher_tokens']!=EXTRA or p['new_GPU_cap_seconds']!=37536
            or p['decay_policy']!=policy() or p['prior_pilot_GPU_seconds']!=completion['GPU_seconds']):
        raise ValueError('Positive fixed pilot and prospectively measured same-condition2B proposal required')
    old=checked(p['pilot_config']);base=checked(old['base_config']);quality=checked(p['original_quality_policy'])
    for name in ('control_training_record','control_evaluation','control_raw','control_notes','related_completed_comparison'):
        checked(p[name])
    cp=Path(p['parent_checkpoint']['path'])
    if sha256(cp)!=p['parent_checkpoint']['sha256']: raise ValueError('Exact learned pilot parent required')
    parent=torch.load(cp,map_location='cpu',weights_only=False)
    binding=ancestry_binding(dict(sha256=p['pilot_config']['sha256'],source_binding=pilot['source_binding']))
    if (not committed_decay(parent) or parent['binding']!=binding or parent['counters']['update']!=10000
            or parent['counters']['supervised_tokens']!=START or parent['scheduler']['total']!=TOTAL
            or parent['spec']['dtype']!='bf16' or parent['spec']['backend']!='flash'):
        raise ValueError('Unchanged finite CUDA pilot parent/state and original2B schedule required')
    tests=PHASE/'base_teacher_decay_2b_tests.xml'
    cases=ET.parse(tests).findall('.//testcase')
    if len(cases)!=7 or any(r.find(tag) is not None for r in cases for tag in ('failure','error','skipped')):
        raise ValueError('Seven actual learned-parent CPU resume/accounting/refusal checks required')
    sources={**pilot['source_sha256'],**quality['helper_sha256'],**{name:sha256(ROOT/name) for name in LOCAL}}
    config=dict(created_at=now(),proposal=ref(PROPOSAL),pilot_config=p['pilot_config'],pilot_completion=p['pilot_completion'],
        base_config=pilot['base_config'],parent_checkpoint=p['parent_checkpoint'],parent_counters=parent['counters'],
        checkpoint_binding=binding,source_binding=pilot['source_binding'],source_sha256=sources,CPU_tests=ref(tests),
        original_quality_policy=p['original_quality_policy'],quality_references=quality['references'],
        initial_teacher_tokens=START,final_teacher_tokens=TOTAL,new_teacher_tokens=EXTRA,decay_policy=policy(),
        GPU_cap_seconds=p['new_GPU_cap_seconds'],prior_pilot_GPU_seconds=p['prior_pilot_GPU_seconds'],
        maximum_combined_GPU_seconds=p['maximum_combined_GPU_seconds'],expected_worst_peak_bytes=pilot['expected_worst_peak_bytes'],
        checkpoint_every_updates=1000,heartbeat_every_updates=20,
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_scored=False)
    config.update({k:p[k] for k in ('control_checkpoint','control_training_record','control_evaluation','control_raw','control_notes','related_completed_comparison')})
    atomic_json(CONFIG,config)
    print(json.dumps(dict(status='same_parent2B_frozen_not_started',new_teachers=EXTRA,GPU_cap_seconds=37536)))


def inspect(require_ui=False):
    c=read_json(CONFIG)
    if (RUN/'result.json').exists(): raise ValueError('Completed comparison cannot be rerun')
    if (RUN/'job.json').exists():
        j=read_json(RUN/'job.json')
        if alive(j) or not j['cumulative_GPU_ledger_closed'] or j['config_sha256']!=sha256(CONFIG):
            raise ValueError('Actual live/unclosed/different previous2B job')
        if j['GPU_seconds']>=c['GPU_cap_seconds']: raise ValueError('Fixed cumulative2B budget exhausted')
    for name in ('proposal','pilot_config','pilot_completion','base_config','CPU_tests','original_quality_policy',
                 'control_training_record','control_evaluation','control_raw','control_notes','related_completed_comparison'):
        verified_path(c[name])
    for value in c['quality_references'].values(): checked(value)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen continuation source differs: '+name)
    for value in (c['parent_checkpoint'],c['control_checkpoint']):
        if sha256(Path(value['path']))!=value['sha256']: raise ValueError('Frozen parent/control checkpoint changed')
    base=checked(c['base_config'])
    for path,digest in ((ROOT/base['tokenizer'],base['tokenizer_sha256']),
        (ROOT/'eval/base.jsonl',base['suite_sha256']),
        (Path(base['dev_shards'])/'manifest.json',base['dev_manifest_sha256']),
        (ROOT/base['evaluation']['config'],base['evaluation']['config_sha256']),
        (ROOT/base['evaluation']['semantic_suite'],base['evaluation']['semantic_sha256']),
        (Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'),base['evaluation']['data_manifest_sha256'])):
        if sha256(path)!=digest: raise ValueError('Original fixed DEV/tokenizer/Japanese evaluator differs')
    for folder in Path('/proc').iterdir():
        if not folder.name.isdecimal() or int(folder.name)==os.getpid(): continue
        try:
            args=(folder/'cmdline').read_bytes().split(b'\0')
            if 'python' in Path(args[0].decode()).name and any(arg.startswith((b'scripts/run_',b'scripts/probe_')) for arg in args[1:]):
                raise ValueError('Actual experiment process already exists: '+folder.name)
        except (FileNotFoundError,ProcessLookupError,PermissionError): pass
    if require_ui:
        ui=read_json(ROOT/'reports/local/webui/server.json')
        with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=3) as response: model=json.load(response)
        if not alive(ui) or model['busy'] or model['checkpoint_sha256']!='410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290':
            raise ValueError('Actual idle original10B UI required before planned stop')
    return c,base


def make(c,base,tok,checkpoint):
    trainer=TeacherDecayTrainer(build_trainer(base,tok,c['checkpoint_binding'],'sequential'))
    trainer.load(checkpoint)
    return trainer


def study_binding(c):
    return dict(config_sha256=sha256(CONFIG),parent_checkpoint=c['parent_checkpoint'],
                checkpoint_ancestry_binding=c['checkpoint_binding'],research_kind=KIND,
                role='same_condition_cumulative2B_continuation_no_reheat_no_reset')


def gate(c,base,tok,check):
    path=RUN/'resume-gate.json'
    if path.exists():
        old=read_json(path)
        if (old['config_sha256']!=sha256(CONFIG) or old['parent_checkpoint']!=c['parent_checkpoint']
                or old['initial_counters']!=c['parent_counters'] or not all(old['checks'].values())):
            raise ValueError('Existing actual mid-parent CUDA gate differs or failed')
        return old
    torch.cuda.reset_peak_memory_stats()
    measured=resume_probe(lambda checkpoint:make(c,base,tok,checkpoint),
        c['parent_checkpoint']['path'],RUN/'resume-gate.pt',check)
    peak=torch.cuda.max_memory_allocated()
    measured['checks']['resident_peak_under90percent']=peak<.9*torch.cuda.get_device_properties(0).total_memory
    measured.update(config_sha256=sha256(CONFIG),parent_checkpoint=c['parent_checkpoint'],peak_VRAM_bytes=peak,
                    actual_device='cuda',scope='8 additional verification updates from exact learned parent; weights discarded')
    atomic_json(path,measured)
    if measured['initial_counters']!=c['parent_counters'] or not all(measured['checks'].values()):
        raise ValueError('Actual learned-parent CUDA/full-state/history gate failed')
    return measured


def run():
    c,base=inspect();RUN.mkdir(parents=True,exist_ok=True)
    previous=read_json(RUN/'job.json') if (RUN/'job.json').exists() else {}
    prior=previous.get('GPU_seconds',0);started=None;trainer=None;stopped=False
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),GPU_seconds=prior,
        prior_pilot_GPU_seconds=c['prior_pilot_GPU_seconds'],cumulative_GPU_ledger_closed=False,
        restart_command='scripts/run_base_teacher_decay_2b.ps1 -Worker; first inspect actual identity, closed cumulative ledger and valid committed latest checkpoint',
        Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(RUN/'job.json',job)
    def stop(*_):
        nonlocal stopped
        stopped=True
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    def check():
        if stopped: raise InterruptedError('Stop requested; retain committed continuation checkpoint')
        if started is not None and prior+time.monotonic()-started>=c['GPU_cap_seconds']:
            raise TimeoutError('Fixed cumulative37536-second continuation budget exhausted')
    def beat(stage,**values):
        check();job.update(status='running',stage=stage,heartbeat_at=now(),**values)
        job['GPU_seconds']=prior+time.monotonic()-started
        atomic_json(RUN/'job.json',job)
    latest=RUN/'latest.pt';terminal=RUN/'train-result.json'
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        tok=Tokenizer(ROOT/base['tokenizer']);binding=study_binding(c)
        with gpu_lock('cuda'):
            started=time.monotonic();job['memory_policy']=configure_resident_memory(c['expected_worst_peak_bytes'])
            own_gate=gate(c,base,tok,check)
            if terminal.exists():
                record=read_json(terminal)
                if record['binding']!=binding or record['scientific_CE_teacher_tokens']!=TOTAL:
                    raise ValueError('Existing continuation training record differs')
                if sha256(Path(record['checkpoint']))!=record['checkpoint_sha256']:
                    raise ValueError('Existing complete continuation checkpoint differs')
            else:
                trainer=make(c,base,tok,latest if latest.exists() else c['parent_checkpoint']['path'])
                if not START<=trainer.native.counters['supervised_tokens']<=TOTAL:
                    raise ValueError('Valid learned parent or committed continuation checkpoint required')
                logpath=RUN/f"metrics-{job['pid']}-{job['start_ticks']}.jsonl"
                beat('continuation-learning',latest_checkpoint=str(latest),metrics_path=str(logpath),
                     optimizer_updates=trainer.native.counters['update'],scientific_cumulative_teacher_tokens=trainer.native.counters['supervised_tokens'])
                with logpath.open('x',buffering=1) as log:
                    while trainer.native.counters['supervised_tokens']<TOTAL:
                        check();row=trainer.step();log.write(json.dumps(compact_update(row),allow_nan=False,separators=(',',':'))+'\n')
                        if row['update']%c['checkpoint_every_updates']==0:
                            trainer.save(latest)
                            print(json.dumps(dict(update=row['update'],cumulative_teachers=row['supervised_tokens'],CE_loss=row['CE_loss']),ensure_ascii=False),flush=True)
                        if row['update']%c['heartbeat_every_updates']==0:
                            beat('continuation-learning',optimizer_updates=row['update'],
                                 scientific_cumulative_teacher_tokens=row['supervised_tokens'],
                                 new_scientific_teacher_tokens=row['supervised_tokens']-START,CE_loss=row['CE_loss'])
                trainer.save(latest);state=host(trainer.state_dict())
                if not committed_decay(state) or state['counters']['supervised_tokens']!=TOTAL:
                    raise ValueError('Finite exact cumulative2B continuation state required')
                control=torch.load(c['control_checkpoint']['path'],map_location='cpu',weights_only=False)
                checks=common_stream(state,control)
                if not all(checks.values()): raise ValueError('Same full native2B original stream required')
                record=dict(status='complete',binding=binding,checkpoint_ancestry_binding=state['binding'],
                    parent_checkpoint=c['parent_checkpoint'],research_kind=KIND,checkpoint=str(latest),checkpoint_sha256=sha256(latest),
                    scientific_CE_teacher_tokens=TOTAL,new_scientific_teacher_tokens=EXTRA,
                    counters=state['counters'],sampler=state['sampler'],scheduler=state['scheduler'],spec=state['spec'],
                    lineage=state['lineage'],model_config=state['model_config'],decay=state['decay'],stream_checks=checks)
                atomic_json(terminal,record)
                del trainer;trainer=None;del state,control;gc.collect();torch.cuda.empty_cache()
            dev=Shard(Path(base['dev_shards']),'dev')
            with typed_native_evaluation(RUN/'evaluation'):
                evaluated=native_evaluation.evaluate('candidate',record,dev,tok,base,binding,beat,check,
                    started+c['GPU_cap_seconds']-prior)
            check();elapsed=prior+time.monotonic()-started
            result=dict(status='learning_and_native_evaluation_complete_content_pending',created_at=now(),config=ref(CONFIG),
                identity=identity(),binding=binding,resume_gate=own_gate,training_record=ref(terminal),
                candidate_checkpoint=dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']),
                parent_checkpoint=c['parent_checkpoint'],control_checkpoint=c['control_checkpoint'],counters=record['counters'],
                stream_checks=record['stream_checks'],scientific_cumulative_teacher_tokens=TOTAL,
                new_scientific_teacher_tokens=EXTRA,reused_control_teacher_tokens=TOTAL,
                control_evaluation=c['control_evaluation'],candidate_evaluation=ref(RUN/'evaluation/candidate/evaluation/result.json'),
                GPU_seconds=elapsed,GPU_cap_seconds=c['GPU_cap_seconds'],prior_pilot_GPU_seconds=c['prior_pilot_GPU_seconds'],
                combined_GPU_seconds=elapsed+c['prior_pilot_GPU_seconds'],cumulative_GPU_ledger_closed=True,
                Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_scored=False)
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',ended_at=now(),GPU_seconds=elapsed,cumulative_GPU_ledger_closed=True)
            atomic_json(RUN/'job.json',job)
            print(json.dumps(dict(status=result['status'],GPU_seconds=elapsed,Base_complete=False)),flush=True)
    except BaseException as error:
        if trainer is not None and not trainer.native._step_in_progress: trainer.save(latest)
        if started is not None: torch.cuda.synchronize()
        job.update(status='failed_or_interrupted',error=repr(error),ended_at=now(),
            GPU_seconds=prior if started is None else prior+time.monotonic()-started,cumulative_GPU_ledger_closed=True)
        atomic_json(RUN/'job.json',job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__);group=parser.add_mutually_exclusive_group()
    group.add_argument('--freeze',action='store_true');group.add_argument('--inspect',action='store_true');group.add_argument('--wait-ui',action='store_true')
    args=parser.parse_args()
    if args.freeze: freeze()
    elif args.inspect: inspect(True);print('Frozen2B continuation and actual idle originalUI passed')
    elif args.wait_ui: wait_ui()
    else: run()
