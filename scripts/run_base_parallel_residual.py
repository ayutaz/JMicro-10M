"""Durable fresh sequential/parallel residual, exact each2B original gold, Base only."""
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
from base_parallel_residual_model import ARMS,POLICY
from base_parallel_residual_trainer import FreshResidualTrainer,committed_state,CEOnlyOriginalSampler
from base_parallel_residual_evaluation import evaluate,validate_record
from probe_base_parallel_residual import paired_budget,source_checks,passed_tests
from verify_base_parallel_residual_validator import verified_probe
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive

CONFIG=ROOT/'configs/phase6/base_parallel_residual_comparison.json'
RUN=ROOT/'reports/phase6/base-parallel-residual-comparison-20261007'
PROBE=ROOT/'reports/phase6/base-parallel-residual-probe-20261007'
CONTROL=ROOT/'reports/phase6/natural-context-contrast-comparison-20261007'
SOURCES=('scripts/run_base_parallel_residual.py','scripts/run_base_parallel_residual.ps1',
    'scripts/review_base_parallel_residual.py','scripts/probe_base_parallel_residual.py',
    'scripts/base_parallel_residual_model.py','scripts/base_parallel_residual_trainer.py',
    'scripts/base_parallel_residual_evaluation.py','tests/test_base_parallel_residual_run.py',
    'scripts/base_kv_allocation_trainer.py','scripts/base_native_teacher_KD_trainer.py',
    'scripts/verify_base_parallel_residual_validator.py',
    'scripts/natural_context_contrast_corpus.py','scripts/natural_context_contrast_trainer.py',
    'scripts/natural_context_contrast_memory.py','scripts/run_complete_text_comparison.py',
    'scripts/run_eos_short_pilot.py','scripts/evaluate_japanese_base.py','scripts/prepare_japanese_evaluation.py',
    'src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','src/jmicro/shards.py',
    'src/jmicro/japanese_evaluation.py','src/jmicro/evaluation_memory.py','uv.lock')


def ref(path):return dict(path=str(path),sha256=sha256(path))


def science_budget(probe):
    budgets,eligible=paired_budget(probe['timing'],probe['GPU_seconds'])
    if (not eligible or not probe['science_budget_eligible'] or budgets!=probe['forecast_arm_seconds']
            or sum(budgets.values())+probe['GPU_seconds']!=probe['forecast_all_new_GPU_seconds']):
        raise ValueError('Actual paired2B forecast exceeds86400 or differs; no rescue')
    return budgets


def study_binding(c,digest):
    return dict(source_binding=c['source_binding'],config_sha256=digest,
        weights_role='scientific_fresh_paired_residual',sources=c['source_sha256'],
        learned_parent_weights_used=False,probe_weights_used=False)


def build_trainer(c,codec,binding,arm,device='cuda'):
    b=c['source_binding'];sampler=CEOnlyOriginalSampler(b['pool'],b['manifest_sha256'],codec,c['goals'])
    if sampler.binding!=b:raise ValueError('Accepted original source differs')
    o=c['optimizer']
    return FreshResidualTrainer(c['variants'][arm],sampler,binding,arm,batch=o['batch'],device=device,
        seed=o['seed'],warmup=o['warmup_gold'],peak=o['peak_lr'],final=o['final_lr'])


def freeze():
    if CONFIG.exists():raise ValueError('Preserve frozen paired fresh residual science')
    probe,job=read_json(PROBE/'result.json'),read_json(PROBE/'job.json')
    if (job['status']!='complete' or alive(job) or not probe['passed']
            or not all(probe['initial_checks'].values()) or not all(probe['original_stream_checks'].values())
            or not probe['original_stream_parity']
            or not all(all(probe['resume'][arm]['checks'].values()) for arm in ARMS)
            or not all(probe['capacity'][arm]['passed'] and probe['capacity'][arm]['weights_unchanged_by_stress'] for arm in ARMS)
            or probe['scientific_gold_tokens'] or probe['probe_weights_used_for_science']):
        raise ValueError('Own exited paired CUDA/fullstate/source proof required')
    budgets=science_budget(probe)
    pc=ROOT/'configs/phase6/base_parallel_residual_probe.json';p=verified_probe()
    if probe['config_sha256']!=sha256(pc):raise ValueError('Actual probe config differs')
    tests=ROOT/'reports/phase6/base_parallel_residual_run_tests.xml';passed_tests(tests,10)
    old_path=ROOT/'configs/phase6/base_output_mixture_probe.json';old=read_json(old_path)
    fields=('dev_shards','dev_manifest_sha256','suite_sha256','evaluation','control_CE')
    atomic_json(CONFIG,dict(**{k:old[k] for k in fields},created_at=now(),
        evaluation_reference_config=ref(old_path),
        **{k:p[k] for k in ('source_binding','goals','tokenizer','tokenizer_sha256','variants','optimizer')},
        probe_result=ref(PROBE/'result.json'),probe_job=ref(PROBE/'job.json'),probe_config=ref(pc),
        preparation=p['CPU_preparation'],proposal=p['proposal'],CPU_run_tests=ref(tests),
        validator_correction=ref(ROOT/'reports/phase6/base_parallel_residual_validator_bridge.json'),
        source_sha256={s:sha256(ROOT/s) for s in SOURCES},residual_policy=POLICY,
        initialization='identical_fresh_native_seed42_no_learned_parent_or_probe_weights',
        batch=80,seed=42,arms=list(ARMS),scientific_CE_teacher_tokens_each=2000000000,
        scientific_CE_teacher_tokens_total=4000000000,reused_control_CE_teacher_tokens=100000000,
        reused_control_GPU_seconds=0,arm_forecast_seconds=budgets,GPU_budget_seconds=sum(budgets.values()),
        probe_GPU_seconds=probe['GPU_seconds'],total_GPU_cap_seconds=86400,
        worst_measured_peak_bytes=max(a['peak_VRAM_bytes'] for a in probe['capacity'].values()),
        checkpoints_every_updates=2000,heartbeat_every_updates=20,
        quality_criteria_unchanged=True,Base_complete=False,Chat_started=False,quantization_started=False,
        completion='Both fresh exited exact2B/fullstate/common original sampler, same bytes/Japanese/all160 individual contents; unchanged matched/strong/absolute/historical guards. Cached mature100M is additional quality reference only, not an equal2B stream. Independent learnedseed/fullDEV/protectedTEST/adoption only if qualified.',
        failure='No residual/init/gain/parent/source/teacher/LR/batch/backend/decoder/cap rescue. Resume only verified completed updates with a closed cumulative GPU ledger.'))
    print(json.dumps(dict(status='paired_fresh_residual_science_frozen_not_started',budgets=budgets)))


def inspect():
    c=read_json(CONFIG)
    if (RUN/'result.json').exists():raise ValueError('Preserve finished science; do not restart')
    if (RUN/'job.json').exists():
        job=read_json(RUN/'job.json')
        if alive(job):raise ValueError('Actual paired fresh residual science already live')
        if job['status']!='failed_or_interrupted' or not job.get('cumulative_GPU_ledger_closed',False):
            raise ValueError('Unclosed GPU ledger; inspect dead process and completed checkpoint before recovery')
    for name in ('probe_result','probe_job','probe_config','preparation','proposal','CPU_run_tests','control_CE','evaluation_reference_config','validator_correction'):
        r=c[name]
        if sha256(Path(r['path']))!=r['sha256']:raise ValueError('Frozen reference changed: '+name)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen science source changed: '+name)
    for path,digest in ((ROOT/c['tokenizer'],c['tokenizer_sha256']),(ROOT/'eval/base.jsonl',c['suite_sha256']),
        (Path(c['dev_shards'])/'manifest.json',c['dev_manifest_sha256']),
        (ROOT/c['evaluation']['config'],c['evaluation']['config_sha256']),
        (ROOT/c['evaluation']['semantic_suite'],c['evaluation']['semantic_sha256']),
        (Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json'),c['evaluation']['data_manifest_sha256'])):
        if sha256(path)!=digest:raise ValueError('Fixed DEV/tokenizer/evaluator differs')
    source=c['source_binding'];codec=Tokenizer(ROOT/c['tokenizer'])
    if CEOnlyOriginalSampler(source['pool'],source['manifest_sha256'],codec,c['goals']).binding!=source:
        raise ValueError('Original accepted TRAIN source changed')
    policy=ROOT/'configs/phase6/base_parallel_residual_review.json'
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
        restart_command='scripts/run_base_parallel_residual.ps1 -Worker; inspect actual PID/boot/start, closed ledger and valid completed checkpoints first',
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
        tok=Tokenizer(ROOT/c['tokenizer']);dev=Shard(Path(c['dev_shards']),'dev')
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix(),'configs/phase6/base_parallel_residual_review.json'):
            destination=RUN/'source'/name;destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,destination)
        binding=study_binding(c,sha256(CONFIG))
        with gpu_lock('cuda'):
            started=time.monotonic();memory=configure_resident_memory(c['worst_measured_peak_bytes'])
            job.update(status='running',memory_policy=memory);results={}
            for arm in ARMS:
                folder=RUN/arm;folder.mkdir(parents=True,exist_ok=True);terminal=folder/'train-result.json'
                if terminal.exists():
                    record=read_json(terminal);validate_record(arm,record)
                    if record['binding']!=binding or record['scientific_CE_teacher_tokens']!=2000000000:
                        raise ValueError('Saved residual training terminal differs')
                    if sha256(Path(record['checkpoint']))!=record['checkpoint_sha256']:
                        raise ValueError('Saved completed residual checkpoint changed')
                else:
                    t=build_trainer(c,tok,binding,arm)
                    checkpoints=list(folder.glob('checkpoint-*.pt'))
                    if checkpoints:t.load(max(checkpoints,key=lambda p:int(p.stem.split('-')[-1])))
                    with (folder/f"metrics-{job['pid']}-{job['start_ticks']}.jsonl").open('x',buffering=1) as log:
                        beat(arm+'-training',residual_arm=arm,completed_updates=t.counters['update'],original_teachers=t.counters['supervised_tokens'])
                        while t.counters['supervised_tokens']<2000000000:
                            check();row=t.step();log.write(json.dumps(row,allow_nan=False)+'\n')
                            if row['update']%c['checkpoints_every_updates']==0:save()
                            if row['update']%20==0:beat(arm+'-training',completed_updates=row['update'],original_teachers=row['supervised_tokens'],CE_loss=row['CE_loss'])
                    cp=save();state=host(t.state_dict())
                    if not committed_state(state) or state['counters']['source_teachers']!=c['goals']:
                        raise ValueError('Exact finite residual2B fullstate required')
                    record=dict(status='complete',binding=binding,checkpoint=str(cp),checkpoint_sha256=sha256(cp),
                        scientific_CE_teacher_tokens=2000000000,counters=state['counters'],sampler=state['sampler'],scheduler=state['scheduler'],
                        spec=state['spec'],lineage=state['lineage'],model_config=state['model_config'],
                        arm=arm,residual_policy=POLICY,residual_model_class=state['spec']['model_class'])
                    atomic_json(terminal,record);del t;t=None;del state;gc.collect();torch.cuda.empty_cache()
                evaluated=evaluate(arm,record,dev,tok,c,binding,beat,check,
                    started+c['GPU_budget_seconds']-prior,RUN/'evaluation')
                results[arm]=dict(training=record,evaluation=evaluated)
            common=source_checks(results[ARMS[0]]['training'],results[ARMS[1]]['training'])
            if not all(common.values()):
                raise ValueError('Paired fresh original2B full stream and sampler mismatch')
            check();elapsed=prior+time.monotonic()-started
            result=dict(status='complete',results=results,common_CE_checks=common,
                cached_CE_stream_matched=False,cached_CE_use='mature100M additional quality reference only',
                scientific_CE_teacher_tokens=4000000000,reused_control_CE_teachers=100000000,reused_control_GPU_seconds=0,
                GPU_occupancy_seconds=elapsed,total_GPU_seconds_including_probe=elapsed+c['probe_GPU_seconds'],
                actual_identity=identity(),config_sha256=sha256(CONFIG),Base_complete=False,Chat_started=False,quantization_started=False,
                next_action='Read all160 individually; unchanged new-sequential/strong/absolute/historical guards before any final validation.')
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=elapsed,cumulative_GPU_ledger_closed=True)
            atomic_json(path,job);print(json.dumps(dict(status='paired_fresh_residual_science_complete_content_review_pending',GPU_seconds=elapsed)))
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
    elif args.inspect:inspect();print('Frozen paired fresh residual science inspected; GPU0')
    else:run()
