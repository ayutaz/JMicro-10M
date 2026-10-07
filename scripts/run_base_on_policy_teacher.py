"""Persistent original100M plus sampled-prefix teacher feedback; reuse cached CE."""
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
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
import torch
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.phase5 import equal_state
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from base_on_policy_teacher_trainer import OnPolicyTeacherTrainer
from probe_base_on_policy_teacher import forecast
from base_on_policy_teacher_trainer import committed_state, RECIPE
from phase6_performance import identity, alive
import run_complete_text_comparison as evaluation

CONFIG = ROOT/'configs/phase6/base_on_policy_teacher_comparison.json'
RUN = ROOT/'reports/phase6/base-on-policy-teacher-comparison-20261007'
PROBE = ROOT/'reports/phase6/base-on-policy-teacher-probe-20261007'
CONTROL = ROOT/'reports/phase6/natural-context-contrast-comparison-20261007'
SOURCES = ('scripts/run_base_on_policy_teacher.py', 'scripts/run_base_on_policy_teacher.ps1', 'scripts/review_base_on_policy_teacher.py',
    'scripts/base_on_policy_teacher_trainer.py', 'scripts/base_native_teacher_KD_trainer.py', 'tests/test_base_on_policy_teacher_run.py',
    'scripts/probe_base_on_policy_teacher.py',
    'scripts/natural_context_contrast_corpus.py', 'scripts/natural_context_contrast_trainer.py',
    'scripts/natural_context_contrast_memory.py', 'scripts/run_complete_text_comparison.py',
    'scripts/run_eos_short_pilot.py', 'scripts/evaluate_japanese_base.py', 'scripts/prepare_japanese_evaluation.py',
    'src/jmicro/model.py', 'src/jmicro/training.py', 'src/jmicro/tokenizer.py', 'src/jmicro/shards.py',
    'src/jmicro/japanese_evaluation.py', 'src/jmicro/evaluation_memory.py', 'uv.lock')


def ref(path): return dict(path=str(path),sha256=sha256(path))


def science_budget(probe):
    elapsed = probe['GPU_occupancy_seconds']
    if not math.isfinite(elapsed) or not 0 < elapsed <= 180:
        raise ValueError('Actual bounded probe required')
    budget = forecast(probe['histories']['timing'][3:])
    if budget != probe['science_budget_seconds'] or budget+elapsed > 7200 or not probe['science_budget_eligible']:
        raise ValueError('Fixed100M forecast exceeds7200s total; no cap/teacher rescue')
    return budget


def matched_control_checks(left,right):
    keys = ('update','token_digest','supervised_tokens','source_teachers','source_EOS',
            'CE_input_tokens','original_body_bytes','auxiliary_input_tokens','auxiliary_pairs','physical_input_tokens')
    return {k:equal_state(left['counters'][k],right['counters'][k]) for k in keys} | {'full_sampler':equal_state(left['sampler'],right['sampler'])}


def freeze():
    if CONFIG.exists(): raise ValueError('Preserve frozen OnPolicyTeacher science')
    probe, job = read_json(PROBE/'result.json'), read_json(PROBE/'job.json')
    if (job['status'] != 'complete' or alive(job) or not probe['passed'] or
            not all(probe['initial_checks'].values()) or not all(probe['all_resume_and_source_checks'].values())):
        raise ValueError('Actual exited full on-policy native CUDA/source gate required')
    budget = science_budget(probe)
    p = read_json(ROOT/'configs/phase6/base_on_policy_teacher_probe.json')
    if probe['config_sha256'] != sha256(ROOT/'configs/phase6/base_on_policy_teacher_probe.json'):
        raise ValueError('Actual probe recipe changed')
    for name,digest in p['source_sha256'].items():
        if sha256(ROOT/name) != digest: raise ValueError('Actual verified OnPolicyTeacher implementation changed')
    tests = ROOT/'reports/phase6/base_on_policy_teacher_run_tests.xml'
    suites = list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites) < 5 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Actual runner budget/stream checks required')
    control = read_json(CONTROL/'CE/train-result.json')
    cj = read_json(CONTROL/'job.json')
    if (cj['status'] != 'complete' or alive(cj) or control['scientific_CE_teacher_tokens'] != 100000000
            or control['counters']['update'] != 17698):
        raise ValueError('Actual cached CE100M control required')
    c = dict(**{k:p[k] for k in ('parent','parent_size','parent_mtime_ns','teacher','teacher_size','teacher_mtime_ns','source_binding','goals',
        'tokenizer','tokenizer_sha256','dev_shards','dev_manifest_sha256','suite_sha256','evaluation')},
        created_at=now(), probe_result=ref(PROBE/'result.json'), probe_job=ref(PROBE/'job.json'),
        probe_config=ref(ROOT/'configs/phase6/base_on_policy_teacher_probe.json'), proposal=p['proposal'], control_CE=p['control_CE'],
        CPU_run_tests=ref(tests), source_sha256={s:sha256(ROOT/s) for s in SOURCES},
        batch=48, seed=42, arms=['on_policy_teacher'], scientific_CE_teacher_tokens=100000000,
        reused_control_CE_teacher_tokens=100000000, reused_control_GPU_seconds=0,
        worst_measured_peak_bytes=probe['capacity']['peak_VRAM_bytes'], GPU_budget_seconds=budget,
        probe_GPU_seconds=probe['GPU_occupancy_seconds'], total_GPU_cap_seconds=7200,
        optimizer='fresh_AdamW_lr1e-5_wd0.1_constant',on_policy_teacher_recipe=RECIPE,
        checkpoints_every_updates=250, heartbeat_every_updates=20,
        quality_criteria_unchanged=True, Base_complete=False, Chat_started=False, quantization_started=False,
        completion='Exact original100M/full native state/RNG/full original stream/sampler; separately counted current-student sampled prefixes/frozen-teacher distributions and all extra forwards. Same-byte/all Japanese/all80 raw-bound review and unchanged matched/strong/absolute/historical guards. Qualified candidate only gets independent learningseed/fullDEV/protectedTEST/adoption.',
        failure='One fixed on-policy teacher recipe; no teacher/T/coefficient/schedule/prefixes/decoder/LR/source/parent/batch/cap rescue or automatic extension. Resume only valid completed updates within same cumulative budget.')
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='OnPolicyTeacher_science_frozen_not_started',GPU_budget_seconds=budget,forecast_total_seconds=budget+c['probe_GPU_seconds'])))


def inspect():
    c = read_json(CONFIG)
    if (RUN/'job.json').exists() and alive(read_json(RUN/'job.json')): raise ValueError('Actual OnPolicyTeacher science already live')
    for name in ('probe_result','probe_job','probe_config','proposal','control_CE','CPU_run_tests'):
        if sha256(Path(c[name]['path'])) != c[name]['sha256']: raise ValueError('Frozen gate/control changed')
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name) != digest: raise ValueError('Frozen scientific source changed: '+name)
    for name in ('parent','teacher'):
        st=Path(c[name]['path']).stat()
        if (st.st_size,st.st_mtime_ns)!=(c[name+'_size'],c[name+'_mtime_ns']):raise ValueError('Audited checkpoint changed: '+name)
    for path,digest in ((ROOT/c['tokenizer'],c['tokenizer_sha256']), (ROOT/'eval/base.jsonl',c['suite_sha256']),
                        (Path(c['dev_shards'])/'manifest.json',c['dev_manifest_sha256']),
                        (ROOT/c['evaluation']['config'],c['evaluation']['config_sha256'])):
        if sha256(path) != digest: raise ValueError('Fixed native DEV/codec differs')
    policy = ROOT/'configs/phase6/base_on_policy_teacher_review.json'
    if not policy.exists() or read_json(policy)['config_sha256'] != sha256(CONFIG): raise ValueError('Freeze native quality review policy before science')
    return c


def run():
    c = inspect(); path = RUN/'job.json'
    previous = read_json(path) if path.exists() else {}
    if previous:
        if previous['config_sha256'] != sha256(CONFIG): raise ValueError('Saved scientific job recipe differs')
        if previous['status'] == 'complete': print('Completed OnPolicyTeacher science retained'); return
    RUN.mkdir(parents=True,exist_ok=True)
    prior = previous.get('GPU_occupancy_seconds',0); started = None; stopped = False; t = None
    job = dict(status='starting',**identity(),started_at=now(),config_sha256=sha256(CONFIG),GPU_occupancy_seconds=prior,
        restart_command='scripts/run_base_on_policy_teacher.ps1 -Worker; inspect PID/boot/start and valid completed checkpoint first; same cumulative budget',
        Base_complete=False,Chat_started=False,quantization_started=False)
    atomic_json(path,job)
    def stop(*_):
        nonlocal stopped
        stopped = True
    signal.signal(signal.SIGTERM,stop); signal.signal(signal.SIGINT,stop)
    def check():
        if stopped: raise InterruptedError('Stop requested; retain completed update')
        if started is not None and prior+time.monotonic()-started > c['GPU_budget_seconds']:
            raise TimeoutError('Frozen cumulative scientific GPU budget exhausted')
    def beat(stage,**values):
        check(); job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None: job['GPU_occupancy_seconds'] = prior+time.monotonic()-started
        atomic_json(path,job)
    folder = RUN/'on_policy_teacher'; folder.mkdir(parents=True,exist_ok=True)
    def save():
        cp = folder/f"checkpoint-{t.counters['update']:08d}.pt"
        t.save(cp); job['latest_checkpoint'] = str(cp); return cp
    try:
        torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
        memory = configure_resident_memory(c['worst_measured_peak_bytes'])
        parent = torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
        teacher = torch.load(c['teacher']['path'],map_location='cpu',weights_only=False)
        tok = Tokenizer(ROOT/c['tokenizer']); dev = Shard(Path(c['dev_shards']),'dev')
        for name in (*SOURCES,CONFIG.relative_to(ROOT).as_posix()):
            destination = RUN/'source'/name; destination.parent.mkdir(parents=True,exist_ok=True); shutil.copyfile(ROOT/name,destination)
        binding = dict(parent=c['parent'],source_binding=c['source_binding'],config_sha256=sha256(CONFIG),
            weights_role='scientific_on_policy_teacher',sources=c['source_sha256'])
        with gpu_lock('cuda'):
            started = time.monotonic(); job['status'] = 'running'; job['memory_policy'] = memory
            terminal = folder/'train-result.json'
            if terminal.exists():
                record = read_json(terminal)
                if record['binding'] != binding or record['scientific_CE_teacher_tokens'] != 100000000: raise ValueError('Saved training terminal differs')
            else:
                sampler = OriginalTrainCorpusSampler(c['source_binding']['pool'],c['source_binding']['manifest_sha256'],tok,c['goals'],42)
                if sampler.binding != c['source_binding']: raise ValueError('Accepted original source changed')
                t = OnPolicyTeacherTrainer(parent,sampler,binding,teacher,c['teacher'],batch=48)
                paths = list(folder.glob('checkpoint-*.pt'))
                if paths: t.load(max(paths,key=lambda p:int(p.stem.split('-')[-1])))
                with (folder/f"metrics-{job['pid']}-{job['start_ticks']}.jsonl").open('x',buffering=1) as log:
                    beat('on_policy_teacher-training',completed_updates=t.counters['update'],original_teachers=t.counters['supervised_tokens'])
                    while t.counters['supervised_tokens'] < 100000000:
                        check(); row = t.step(); log.write(json.dumps(row,allow_nan=False)+'\n')
                        if row['update'] % 250 == 0: save()
                        if row['update'] % 20 == 0: beat('on_policy_teacher-training',completed_updates=row['update'],original_teachers=row['supervised_tokens'],CE_loss=row['CE_loss'])
                cp = save(); state = host(t.state_dict())
                if not committed_state(state) or state['counters']['source_teachers'] != c['goals']: raise ValueError('Finite exact native on-policy feedback100M state required')
                teacher_checks=dict(weights_unchanged=equal_state(teacher['model'],host(t.teacher.state_dict())),
                    eval_no_grad=not t.teacher.training and all(not p.requires_grad and p.grad is None for p in t.teacher.parameters()),
                    student_only_optimizer={id(p) for g in t.optimizer.param_groups for p in g['params']}=={id(p) for p in t.model.parameters()})
                if not all(teacher_checks.values()) or not state['on_policy_teacher']['rollout_batches']:
                    raise ValueError('Actual sampled prefixes and immutable frozen teacher required')
                record = dict(status='complete',binding=binding,checkpoint=str(cp),checkpoint_sha256=sha256(cp),
                    scientific_CE_teacher_tokens=100000000,counters=state['counters'],sampler=state['sampler'],spec=state['spec'],lineage=state['lineage'],
                    on_policy_teacher=state['on_policy_teacher'],teacher_immutable_checks=teacher_checks,
                    scientific_distribution_positions=state['on_policy_teacher']['distribution_positions'],new_corpus_tokens=0)
                atomic_json(terminal,record); del t; t = None; gc.collect(); torch.cuda.empty_cache()
            control = read_json(Path(c['control_CE']['path']))
            matched = matched_control_checks(record,control)
            if not all(matched.values()): raise ValueError('Same original CE stream/full sampler differs')
            evaluation.RUN = RUN/'evaluation'
            evaluated = evaluation.evaluate('on_policy_teacher',record,dev,tok,c,binding,beat,check,started+c['GPU_budget_seconds']-prior)
            check(); elapsed = prior+time.monotonic()-started
            result = dict(status='complete',training=record,evaluation=evaluated,common_CE_checks=matched,
                scientific_CE_teacher_tokens=100000000,reused_control_CE_teachers=100000000,reused_control_GPU_seconds=0,
                GPU_occupancy_seconds=elapsed,total_GPU_seconds_including_probe=elapsed+c['probe_GPU_seconds'],
                actual_identity=identity(),config_sha256=sha256(CONFIG),Base_complete=False,Chat_started=False,quantization_started=False,
                next_action='Read all80; reuse cached CE80 and unchanged native quality/retention gates; do not adopt on code or training completion alone.')
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',stage='complete',ended_at=now(),GPU_occupancy_seconds=elapsed); atomic_json(path,job)
            print(json.dumps(dict(status='OnPolicyTeacher_science_complete_content_review_pending',GPU_seconds=elapsed)))
    except BaseException as error:
        if t is not None and t.counters['source_teachers'] == t.sampler.consumed and committed_state(host(t.state_dict())):
            save()
        job.update(status='failed_or_interrupted',error=repr(error),ended_at=now(),GPU_occupancy_seconds=prior+time.monotonic()-started if started else prior)
        atomic_json(path,job); raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(); group=parser.add_mutually_exclusive_group()
    group.add_argument('--freeze',action='store_true'); group.add_argument('--inspect',action='store_true'); args=parser.parse_args()
    if args.freeze: freeze()
    elif args.inspect: inspect(); print('Frozen OnPolicyTeacher science inspected; GPU0')
    else: run()
