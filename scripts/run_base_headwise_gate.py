"""Durable new static-half and query-headwise100M comparison, Base only."""
import argparse
import gc
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT,now,read_json,sha256
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock
from base_headwise_gate_model import ARMS,POLICY
from base_headwise_gate_trainer import HeadwiseGateTrainer,finite_tree
from base_headwise_gate_evaluation import evaluate,validate_record
from probe_base_headwise_gate import paired_budget,source_checks,passed_tests
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive

CONFIG=ROOT/'configs/phase6/base_headwise_gate_comparison.json'
RUN=ROOT/'reports/phase6/base-headwise-gate-comparison-20261007'
PROBE=ROOT/'reports/phase6/base-headwise-gate-probe-20261007'
CONTROL=ROOT/'reports/phase6/natural-context-contrast-comparison-20261007'
SOURCES=('scripts/run_base_headwise_gate.py','scripts/run_base_headwise_gate.ps1',
    'scripts/review_base_headwise_gate.py','scripts/probe_base_headwise_gate.py',
    'scripts/base_headwise_gate_model.py','scripts/base_headwise_gate_trainer.py',
    'scripts/base_headwise_gate_evaluation.py','tests/test_base_headwise_gate_run.py',
    'scripts/natural_context_contrast_corpus.py','scripts/natural_context_contrast_trainer.py',
    'scripts/natural_context_contrast_memory.py','scripts/run_complete_text_comparison.py',
    'scripts/run_eos_short_pilot.py','scripts/evaluate_japanese_base.py','scripts/prepare_japanese_evaluation.py',
    'src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','src/jmicro/shards.py',
    'src/jmicro/japanese_evaluation.py','src/jmicro/evaluation_memory.py','uv.lock')


def ref(path):return dict(path=str(path),sha256=sha256(path))


def science_budget(probe):
    budgets,eligible=paired_budget(probe['arms'],probe['GPU_occupancy_seconds'])
    if not eligible or not probe['science_budget_eligible'] or budgets!=probe['science_budget_seconds']:
        raise ValueError('Actual paired100M forecast exceeds9000 or differs; no rescue')
    return budgets


def freeze():
    if CONFIG.exists():raise ValueError('Preserve frozen paired gate science')
    probe,job=read_json(PROBE/'result.json'),read_json(PROBE/'job.json')
    if (job['status']!='complete' or alive(job) or not probe['passed']
            or not all(probe['initial_checks'].values()) or not all(probe['common_source_checks'].values())
            or not all(all(probe['arms'][arm]['resume_checks'].values()) for arm in ARMS)):
        raise ValueError('Own exited paired CUDA/fullstate/source proof required')
    budgets=science_budget(probe)
    pc=ROOT/'configs/phase6/base_headwise_gate_probe.json';p=read_json(pc)
    if probe['config_sha256']!=sha256(pc):raise ValueError('Actual probe config differs')
    for name,digest in p['source_sha256'].items():
        if sha256(ROOT/name)!=digest:raise ValueError('Own verified gate source changed: '+name)
    tests=ROOT/'reports/phase6/base_headwise_gate_run_tests.xml';passed_tests(tests,7)
    fields=('parent','parent_size','parent_mtime_ns','source_binding','goals','tokenizer',
            'tokenizer_sha256','dev_shards','dev_manifest_sha256','suite_sha256','evaluation','control_CE')
    atomic_json(CONFIG,dict(**{k:p[k] for k in fields},created_at=now(),
        probe_result=ref(PROBE/'result.json'),probe_job=ref(PROBE/'job.json'),probe_config=ref(pc),
        preparation=p['preparation'],proposal=p['proposal'],CPU_run_tests=ref(tests),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},gate_policy=POLICY,
        batch=48,seed=42,arms=list(ARMS),scientific_CE_teacher_tokens_each=100000000,
        scientific_CE_teacher_tokens_total=200000000,reused_control_CE_teacher_tokens=100000000,
        reused_control_GPU_seconds=0,arm_forecast_seconds=budgets,GPU_budget_seconds=sum(budgets.values()),
        probe_GPU_seconds=probe['GPU_occupancy_seconds'],total_GPU_cap_seconds=9000,
        worst_measured_peak_bytes=max(a['capacity']['peak_VRAM_bytes'] for a in probe['arms'].values()),
        optimizer='fresh_all_parameter_AdamW_lr1e-5_wd0.1_betas0.9_0.999_eps1e-8_globalclip1_constant',
        checkpoints_every_updates=250,heartbeat_every_updates=20,
        quality_criteria_unchanged=True,Base_complete=False,Chat_started=False,quantization_started=False,
        completion='Both exited exact100M/fullstate/common original sampler, same bytes/Japanese/all160 individual contents; unchanged matched/strong/absolute/historical guards. Independent learnedseed/fullDEV/protectedTEST/adoption only if qualified.',
        failure='No gate/init/gain/parent/source/teacher/LR/batch/backend/decoder/cap rescue. Resume only verified completed updates with a closed cumulative GPU ledger.'))
    print(json.dumps(dict(status='paired_gate_science_frozen_not_started',budgets=budgets)))


def inspect():
    c=read_json(CONFIG)
    if (RUN/'result.json').exists():raise ValueError('Preserve finished science; do not restart')
    if (RUN/'job.json').exists():
        job=read_json(RUN/'job.json')
        if alive(job):raise ValueError('Actual paired gate science already live')
        if job['status']!='failed_or_interrupted' or not job.get('cumulative_GPU_ledger_closed',False):
            raise ValueError('Unclosed GPU ledger; inspect dead process and completed checkpoint before recovery')
    for name in ('probe_result','probe_job','probe_config','preparation','proposal','CPU_run_tests','control_CE'):
        r=c[name]
        if sha256(Path(r['path']))!=r['sha256']:raise ValueError('Frozen reference changed: '+name)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen science source changed: '+name)
    st=Path(c['parent']['path']).stat()
    if (st.st_size,st.st_mtime_ns)!=(c['parent_size'],c['parent_mtime_ns']):raise ValueError('Accepted parent changed')
    for path,digest in ((ROOT/c['tokenizer'],c['tokenizer_sha256']),(ROOT/'eval/base.jsonl',c['suite_sha256']),
        (Path(c['dev_shards'])/'manifest.json',c['dev_manifest_sha256']),
        (ROOT/c['evaluation']['config'],c['evaluation']['config_sha256'])):
        if sha256(path)!=digest:raise ValueError('Fixed DEV/tokenizer/evaluator differs')
    policy=ROOT/'configs/phase6/base_headwise_gate_review.json'
    if not policy.exists() or read_json(policy)['config_sha256']!=sha256(CONFIG):
        raise ValueError('Freeze all original quality guards before science')
    for folder in Path('/proc').iterdir():
        if not folder.name.isdecimal() or int(folder.name)==os.getpid():continue
        try:
            cmd=(folder/'cmdline').read_bytes().split(b'\0')
            if 'python' in Path(cmd[0].decode()).name and any(
                    arg.startswith((b'scripts/run_',b'scripts/probe_')) for arg in cmd[1:]):
                raise ValueError('Another actual experiment exists: '+folder.name)
        except (FileNotFoundError,ProcessLookupError,PermissionError):continue
    return c


def run():
    c=inspect();path=RUN/'job.json';previous=read_json(path) if path.exists() else {}
    if previous and previous['config_sha256']!=sha256(CONFIG):raise ValueError('Recovery recipe differs')
    RUN.mkdir(parents=True,exist_ok=True)
    prior=previous.get('GPU_occupancy_seconds',0);started=None;stopped=False;t=None;folder=None
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),
        GPU_occupancy_seconds=prior,cumulative_GPU_ledger_closed=False,
        restart_command='scripts/run_base_headwise_gate.ps1 -Worker; inspect actual PID/boot/start, closed ledger and valid completed checkpoints first',
        Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(path,job)
    def stop(*_):
        nonlocal stopped
        stopped=True
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    def check():
        if stopped:raise InterruptedError('Stop requested; retain completed updates')
        if started is not None and prior+time.monotonic()-started>c['GPU_budget_seconds']:
            raise TimeoutError('Frozen cumulative paired science GPU budget exhausted')
    def beat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None:job['GPU_occupancy_seconds']=prior+time.monotonic()-started
        atomic_json(path,job)
    def save():
        cp=folder/f"checkpoint-{t.counters['update']:08d}.pt"
        t.save(cp);job['latest_checkpoint']=str(cp);return cp
    try:
        torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        tok=Tokenizer(ROOT/c['tokenizer']);dev=Shard(Path(c['dev_shards']),'dev')
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix(),'configs/phase6/base_headwise_gate_review.json'):
            destination=RUN/'source'/name;destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,destination)
        binding=dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256=sha256(CONFIG),
            weights_role='scientific_paired_headwise_gate',sources=c['source_sha256'])
        with gpu_lock('cuda'):
            started=time.monotonic();memory=configure_resident_memory(c['worst_measured_peak_bytes'])
            job.update(status='running',memory_policy=memory);results={}
            for arm in ARMS:
                folder=RUN/arm;folder.mkdir(parents=True,exist_ok=True);terminal=folder/'train-result.json'
                if terminal.exists():
                    record=read_json(terminal);validate_record(arm,record)
                    if record['binding']!=binding or record['scientific_CE_teacher_tokens']!=100000000:
                        raise ValueError('Saved gate training terminal differs')
                    if sha256(Path(record['checkpoint']))!=record['checkpoint_sha256']:
                        raise ValueError('Saved completed gate checkpoint changed')
                else:
                    b=c['source_binding'];sampler=OriginalTrainCorpusSampler(b['pool'],b['manifest_sha256'],tok,c['goals'],42)
                    if sampler.binding!=b:raise ValueError('Accepted original source differs')
                    t=HeadwiseGateTrainer(parent,sampler,binding,arm,batch=48)
                    checkpoints=list(folder.glob('checkpoint-*.pt'))
                    if checkpoints:t.load(max(checkpoints,key=lambda p:int(p.stem.split('-')[-1])))
                    with (folder/f"metrics-{job['pid']}-{job['start_ticks']}.jsonl").open('x',buffering=1) as log:
                        beat(arm+'-training',gate_arm=arm,completed_updates=t.counters['update'],original_teachers=t.counters['supervised_tokens'])
                        while t.counters['supervised_tokens']<100000000:
                            check();row=t.step();log.write(json.dumps(row,allow_nan=False)+'\n')
                            if row['update']%250==0:save()
                            if row['update']%20==0:beat(arm+'-training',completed_updates=row['update'],original_teachers=row['supervised_tokens'],CE_loss=row['CE_loss'])
                    cp=save();state=host(t.state_dict())
                    if not finite_tree(state) or state['counters']['source_teachers']!=c['goals']:
                        raise ValueError('Exact finite gate100M fullstate required')
                    record=dict(status='complete',binding=binding,checkpoint=str(cp),checkpoint_sha256=sha256(cp),
                        scientific_CE_teacher_tokens=100000000,counters=state['counters'],sampler=state['sampler'],
                        spec=state['spec'],lineage=state['lineage'],model_config=state['model_config'],
                        gate_arm=arm,gate_policy=POLICY,gate_model_class='HeadwiseGateModel')
                    atomic_json(terminal,record);del t;t=None;del state;gc.collect();torch.cuda.empty_cache()
                evaluated=evaluate(arm,record,dev,tok,c,binding,beat,check,
                    started+c['GPU_budget_seconds']-prior,RUN/'evaluation')
                results[arm]=dict(training=record,evaluation=evaluated)
            common=source_checks(results[ARMS[0]]['training'],results[ARMS[1]]['training'])
            cached=read_json(Path(c['control_CE']['path']))
            legacy={arm:source_checks(results[arm]['training'],cached) for arm in ARMS}
            if not all(common.values()) or not all(all(v.values()) for v in legacy.values()):
                raise ValueError('Paired/cached original100M full stream and sampler mismatch')
            check();elapsed=prior+time.monotonic()-started
            result=dict(status='complete',results=results,common_CE_checks=common,cached_CE_checks=legacy,
                scientific_CE_teacher_tokens=200000000,reused_control_CE_teachers=100000000,reused_control_GPU_seconds=0,
                GPU_occupancy_seconds=elapsed,total_GPU_seconds_including_probe=elapsed+c['probe_GPU_seconds'],
                actual_identity=identity(),config_sha256=sha256(CONFIG),Base_complete=False,Chat_started=False,quantization_started=False,
                next_action='Read all160 individually; unchanged new-static/strong/absolute/historical gates before any final validation.')
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=elapsed,cumulative_GPU_ledger_closed=True)
            atomic_json(path,job);print(json.dumps(dict(status='paired_gate_science_complete_content_review_pending',GPU_seconds=elapsed)))
    except BaseException as error:
        save_error=None
        if t is not None and not t._step_in_progress:
            try:save()
            except BaseException as exc:save_error=repr(exc)
        job.update(status='failed_or_interrupted',error=repr(error),checkpoint_save_error=save_error,ended_at=now(),
            GPU_occupancy_seconds=prior+time.monotonic()-started if started else prior,cumulative_GPU_ledger_closed=True)
        atomic_json(path,job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__);group=parser.add_mutually_exclusive_group()
    group.add_argument('--freeze',action='store_true');group.add_argument('--inspect',action='store_true');args=parser.parse_args()
    if args.freeze:freeze()
    elif args.inspect:inspect();print('Frozen paired gate science inspected; GPU0')
    else:run()
