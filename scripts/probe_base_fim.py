"""Owned CPU preparation and one-shot CUDA verification for fresh FIM.

No scientific learning/evaluation/TEST. Never restart this completed probe.
Verification weights and input payload stay in WSL, excluded from Git.
"""
import argparse
import copy
import gc
import hashlib
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import xml.etree.ElementTree as ET

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'src'), str(ROOT/'scripts')]
import torch
from base_fim_sampler import FimOriginalSampler, native_stream_payload, POLICY
from base_fim_trainer import FreshFimTrainer, committed_state
from base_kv_allocation_trainer import CEOnlyOriginalSampler
from base_parallel_residual_trainer import FreshResidualTrainer, committed_state as native_committed
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from probe_base_kv_allocation import worst_shape
from jmicro.experiment import sha256, now
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock
from phase6_performance import identity

PROPOSAL = ROOT/'reports/phase6/fim-feasibility-20261015/fresh_FIM_pilot_proposal.json'
CONFIG = ROOT/'configs/phase6/base_fim_probe_20261015.json'
RUN = ROOT/'reports/phase6/base-fim-probe-20261015'
SOURCES = ('scripts/base_fim_sampler.py','scripts/base_fim_trainer.py','scripts/probe_base_fim.py',
    'src/jmicro/fim_compatibility.py','tests/test_base_fim_training.py','tests/test_base_fim_probe.py','tests/test_fim_compatibility.py',
    'scripts/base_kv_allocation_trainer.py','scripts/base_parallel_residual_trainer.py',
    'scripts/base_parallel_residual_model.py','scripts/natural_context_contrast_corpus.py',
    'scripts/natural_context_contrast_trainer.py','scripts/natural_context_contrast_memory.py',
    'scripts/probe_base_kv_allocation.py','scripts/phase6_performance.py','src/jmicro/model.py',
    'src/jmicro/tokenizer.py','src/jmicro/training.py','uv.lock')


def ref(path): return dict(path=str(path),sha256=sha256(path))


def assert_contract(p):
    if (p['status'] != 'prospective_fresh_FIM_PSM_pilot_selected_CPU_implementation_allowed_science_not_frozen'
            or p['actual_parameter_requirement'] != 10001152 or p['optimizer']['batch'] != 80
            or p['full_recipe_teacher_goals'] != dict(web=1500000000,textbook=400000000,story=100000000)
            or p['pilot']['updates'] != 10000 or p['pilot']['original_teacher_positions'] != 94160195
            or p['pilot']['schedule_total_teachers'] != 2000000000
            or p['pilot']['maximum_new_GPU_seconds_including_probe'] != 3600
            or p['pilot']['probe_GPU_ceiling_seconds'] != 120
            or p['pilot']['required_measured_steady_updates'] != 32
            or p['scientific_budget_frozen'] is not False or p['Base_adopted'] is not False
            or p['quality_criteria_unchanged'] is not True or p['TEST_prepared'] is not False):
        raise ValueError('Exact fresh FIM prospective scope required')
    expected = dict(peak_lr=.002,final_lr=1e-5,warmup_gold=5000000,weight_decay=.1,
                    betas=[.9,.999],eps=1e-8,gradient_clip=1.,seed=42,batch=80)
    if (any(p['optimizer'].get(k) != value for k,value in expected.items())
            or p['FIM_rule']['probability'] != POLICY['probability']
            or p['FIM_rule']['markers'] != POLICY['markers']):
        raise ValueError('Original native optimizer and explicit FIM policy required')


def passed_tests(path, count):
    suites = list(ET.parse(path).getroot().iter('testsuite'))
    if (sum(int(s.attrib.get('tests',0)) for s in suites) != count
            or any(int(s.attrib.get(k,0)) for s in suites for k in ('failures','errors','skipped'))):
        raise ValueError('Actual completed CPU tests required')


def initial_weights_digest(state):
    digest = hashlib.sha256()
    for name, tensor in sorted(state['model'].items()):
        digest.update(name.encode()); digest.update(str(tensor.dtype).encode())
        digest.update(str(tuple(tensor.shape)).encode()); digest.update(tensor.detach().cpu().numpy().tobytes())
    return digest.hexdigest()


def build(p, device='cpu', binding=None):
    codec = Tokenizer(ROOT/p['tokenizer']['path'])
    if sha256(codec.path) != p['tokenizer']['sha256']: raise ValueError('Frozen tokenizer differs')
    source = p['source_binding']; opt = p['optimizer']
    sampler = FimOriginalSampler(source['pool'],source['manifest_sha256'],codec,
                                 p['full_recipe_teacher_goals'],seed=opt['seed'])
    if sampler.binding != source: raise ValueError('Accepted TRAIN identity differs; no rescan fallback')
    return FreshFimTrainer(p['native_model'],sampler,binding or dict(role='verification_only',
        proposal_sha256=sha256(PROPOSAL)),batch=opt['batch'],device=device,seed=opt['seed'],
        warmup=opt['warmup_gold'],peak=opt['peak_lr'],final=opt['final_lr'])


def prepare():
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '': raise ValueError('CPU preparation needs empty CUDA_VISIBLE_DEVICES')
    if CONFIG.exists() or (RUN/'preparation.json').exists() or (RUN/'job.json').exists():
        raise ValueError('Preserve one-shot preparation/probe; inspect existing evidence')
    started = time.monotonic(); torch.set_num_threads(2)
    p = json.loads(PROPOSAL.read_text()); assert_contract(p)
    tests = ROOT/'reports/phase6/fim-feasibility-20261015/CPU_training_tests.xml'
    passed_tests(tests,16)
    workflow_tests = ROOT/'reports/phase6/fim-feasibility-20261015/CPU_probe_workflow_tests.xml'
    passed_tests(workflow_tests,9)
    for path,pin in p['references'].items():
        if sha256(ROOT/path) != pin: raise ValueError('Prospective reference differs: '+path)
    frozen = p['matched_control']['checkpoint']
    if sha256(Path(frozen['path'])) != frozen['sha256']: raise ValueError('Historical control checkpoint differs')
    control = torch.load(frozen['path'],map_location='cpu',weights_only=False)
    if (not native_committed(control) or control['counters']['update'] != 10000
            or control['counters']['supervised_tokens'] != 94160195 or control['spec']['batch'] != 80
            or control['spec']['seed'] != 42 or control['spec']['dtype'] != 'bf16'
            or control['spec']['backend'] != 'flash' or control['spec']['arm'] != 'sequential'
            or control['model_config'] != p['native_model'] or control['sampler']['binding'] != p['source_binding']):
        raise ValueError('Actual fresh native control protocol differs; do not fake compatibility')
    if any(control['scheduler'][k] != value for k,value in
           dict(total=2000000000,warmup=5000000,peak=.002,final=1e-5).items()):
        raise ValueError('Historical control actual schedule differs')
    candidate = build(p)
    opt = p['optimizer']; source = p['source_binding']
    native_sampler = CEOnlyOriginalSampler(source['pool'],source['manifest_sha256'],candidate.sampler.tokenizer,
        p['full_recipe_teacher_goals'],seed=opt['seed'])
    native = FreshResidualTrainer(p['native_model'],native_sampler,dict(role='verification_only'),
        'sequential',batch=80,device='cpu',seed=42,warmup=opt['warmup_gold'],peak=opt['peak_lr'],final=opt['final_lr'])
    a,b = candidate.state_dict(),native.state_dict()
    if not all(equal_state(a[k],b[k]) for k in ('model','optimizer','scheduler','RNG')):
        raise ValueError('Actual10M initial weights/Adam/schedule/training RNG differ')
    # Reuse the accepted full-context technical payload; no source-wide hunt.
    prior_probe = ROOT/'configs/phase6/base_parallel_residual_probe.json'
    old_payload = json.loads(prior_probe.read_text())['payload']
    if sha256(Path(old_payload['path'])) != old_payload['sha256']:
        raise ValueError('Previously fixed full-context TRAIN payload differs')
    capacity_window = json.loads(Path(old_payload['path']).read_text())['window']
    if (len(capacity_window['input_ids']) != 1024
            or len(capacity_window['target_ids']) != 1024
            or sum(t != -100 for t in capacity_window['target_ids']) != 512):
        raise ValueError('Owned worst shape requires existing full1024/512 payload')
    digest = initial_weights_digest(a); native_digest = '0'*64
    for _ in range(32):
        old,new = native_sampler.take(80),candidate.sampler.take(80)
        if time.monotonic()-started > 30: raise TimeoutError('Bounded CPU preparation30s exhausted')
        native_digest = hashlib.sha256(bytes.fromhex(native_digest)+native_stream_payload(old)).hexdigest()
        if len(old) != len(new) or native_digest != candidate.sampler.fim['native_stream_digest']:
            raise ValueError('Original native batch/source identity differs')
        for left,right in zip(old,new):
            for key in ('index_byte_position','index_record_sha256','source','teacher_tokens','teacher_body_bytes','original_EOS_targets'):
                if left[key] != right[key]: raise ValueError('Actual original TRAIN identity differs: '+key)
        if not equal_state(native_sampler.rng.getstate(),candidate.sampler.rng.getstate()):
            raise ValueError('Actual material RNG changed by augmentation')
    if not candidate.sampler.fim['applied_rows']:
        raise ValueError('Actual source lacks active FIM; no reroll')
    if time.monotonic()-started > 30:
        raise TimeoutError('Bounded CPU preparation30s exhausted before freeze')
    RUN.mkdir(parents=True,exist_ok=True)
    payload = RUN/'verification_input.pt'; torch.save(capacity_window,payload)
    prepared = dict(status='actual_native10M_CPU_zero_and32_original_source_batches_verified',
        proposal=ref(PROPOSAL),control_checkpoint=frozen,initial_weights_sha256=digest,
        initial_native_weights_Adam_scheduler_training_RNG_equal=True,
        original_source_batches=32,original_source_rows=2560,original_material_RNG_equal=True,
        source_read_events='Two deterministic matching samplers;2560 rows each, not5120 distinct rows',
        capacity_payload_provenance=old_payload,
        original_stream_digest=native_digest,FIM_counters=copy.deepcopy(candidate.sampler.fim),
        CPU_wall_seconds=time.monotonic()-started,CPU_tests=ref(tests),
        CPU_workflow_tests=ref(workflow_tests),
        input_payload=ref(payload),input_payload_export_to_Git=False,
        native_parameters=10001152,source_sha256={n:sha256(ROOT/n) for n in SOURCES},
        model_learning_updates=0,new_scientific_teacher_positions=0,new_GPU_seconds=0,
        DEV_opened=False,TEST_opened=False,quality_improvement_evidence=False,Base_adopted=False)
    atomic_json(RUN/'preparation.json',prepared)
    c = dict(kind='one_shot_fresh_FIM_owned_CUDA_verification_v1',proposal=ref(PROPOSAL),
        preparation=ref(RUN/'preparation.json'),sources=prepared['source_sha256'],input_payload=ref(payload),
        initial_weights_sha256=digest,batch=80,capacity_shape=[80,1024],GPU_ceiling_seconds=120,
        measured_updates=32,continuous_updates=4,split_updates=[2,2],FIM_policy=POLICY,
        scientific_teacher_positions=0,Base_adopted=False,TEST_prepared=False)
    atomic_json(CONFIG,c)
    print(json.dumps({k:prepared[k] for k in ('status','native_parameters','original_source_rows','CPU_wall_seconds','FIM_counters')}))


def inspect(pin):
    if sha256(CONFIG) != pin: raise ValueError('Pinned owned probe config differs')
    c = json.loads(CONFIG.read_text())
    if (c['kind'] != 'one_shot_fresh_FIM_owned_CUDA_verification_v1' or c['GPU_ceiling_seconds'] != 120
            or c['batch'] != 80 or c['capacity_shape'] != [80,1024] or c['FIM_policy'] != POLICY
            or c['measured_updates'] != 32 or c['continuous_updates'] != 4 or c['split_updates'] != [2,2]
            or c['scientific_teacher_positions'] != 0 or c['Base_adopted'] is not False
            or c['TEST_prepared'] is not False): raise ValueError('Exact technical probe scope required')
    for key in ('proposal','preparation','input_payload'):
        if sha256(Path(c[key]['path'])) != c[key]['sha256']: raise ValueError('Probe reference differs: '+key)
    for path,digest in c['sources'].items():
        if sha256(ROOT/path) != digest: raise ValueError('CPU-verified source differs: '+path)
    if (RUN/'job.json').exists() or (RUN/'result.json').exists():
        raise ValueError('One-shot probe already has evidence; inspect actual PID/results, do not relaunch')
    return c,json.loads(PROPOSAL.read_text())


def run(pin):
    c,p = inspect(pin)
    if not torch.cuda.is_available(): raise RuntimeError('Actual CUDA required')
    torch.set_num_threads(2); torch.use_deterministic_algorithms(True)
    job = dict(status='starting',**identity(),config_sha256=pin,started_at=now(),
        scientific_teacher_positions=0,GPU_occupancy_seconds=0,cumulative_GPU_ledger_closed=False)
    atomic_json(RUN/'job.json',job)
    started = None; technical_teachers = updates = 0
    def check(*args):
        if args or (started is not None and time.monotonic()-started > c['GPU_ceiling_seconds']):
            raise TimeoutError('One-shot FIM CUDA120s ceiling exhausted; preserve failure')
    def beat(stage):
        check();job.update(stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json',job)
    def learn(t):
        nonlocal technical_teachers,updates
        check();row=t.step();technical_teachers += row['CE_targets_this_update']; updates += 1
        return row
    def clear(): gc.collect();torch.cuda.empty_cache()
    try:
        with gpu_lock('cuda'):
            started=time.monotonic();signal.signal(signal.SIGTERM,check);signal.signal(signal.SIGINT,check)
            job['status']='running'
            memory=configure_resident_memory(17791499264)
            full=build(p,'cuda');zero=host(full.state_dict())
            if initial_weights_digest(zero) != c['initial_weights_sha256']:
                raise ValueError('Actual CUDA initial native weights differ from CPU/control')
            torch.save(zero,RUN/'verification_zero.pt')
            beat('continuous4')
            full_history=[learn(full) for _ in range(4)];expected=host(full.state_dict())
            if not expected['sampler']['FIM_counters']['applied_rows']:
                raise ValueError('Actual CUDA resume check must include FIM')
            del full;clear();split=build(p,'cuda')
            split_history=[learn(split) for _ in range(2)];split.save(RUN/'verification_split.pt')
            del split;clear();resumed=build(p,'cuda');resumed.load(RUN/'verification_split.pt')
            split_history.extend(learn(resumed) for _ in range(2))
            strip=lambda r:{k:v for k,v in r.items() if k not in ('seconds','data_wait_seconds')}
            if (not equal_state(expected,host(resumed.state_dict()))
                    or not equal_state([strip(r) for r in full_history],[strip(r) for r in split_history])):
                raise ValueError('Actual native CUDA continuous versus resumed full state/history differs')
            beat('capacity80x1024')
            window=torch.load(c['input_payload']['path'],map_location='cpu',weights_only=False)
            capacity=worst_shape(resumed,window,80)
            if capacity['peak_VRAM_bytes'] >= memory['allocator_allowance_bytes']:
                raise ValueError('Actual worst shape exceeds resident allowance')
            beat('steady32')
            timings=[learn(resumed) for _ in range(32)]
            steps=[r['seconds'] for r in timings]
            if any(not math.isfinite(s) or s <= 0 for s in steps): raise ValueError('Actual finite step timings required')
            resumed.save(RUN/'verification_final.pt')
            forecast=math.ceil(10000/32*sum(steps)*1.3+600)
            elapsed=time.monotonic()-started;check()
            result=dict(status='complete',passed=True,config_sha256=pin,actual_identity=identity(),
                GPU_occupancy_seconds=elapsed,memory_policy=memory,capacity=capacity,
                all_state_and_history_resume_equal=True,actual_FIM_active=True,
                all32_timing_seconds=steps,measured_original_teachers=sum(r['CE_targets_this_update'] for r in timings),
                science_forecast_seconds=forecast,science_budget_eligible=forecast+elapsed <= 3600,
                technical_optimizer_updates=updates,technical_teacher_positions=technical_teachers,
                capacity_forward_backward_teacher_positions=capacity['teachers'],
                verification_final=ref(RUN/'verification_final.pt'),
                new_scientific_teacher_positions=0,Base_adopted=False,DEV_opened=False,TEST_opened=False,
                quality_improvement_evidence=False,verification_weights_must_not_initialize_science=True)
            atomic_json(RUN/'result.json',result)
            job.update(status='complete',GPU_occupancy_seconds=elapsed,cumulative_GPU_ledger_closed=True,
                       ended_at=now(),result_sha256=sha256(RUN/'result.json'))
            atomic_json(RUN/'job.json',job)
            print(json.dumps({k:result[k] for k in ('status','passed','GPU_occupancy_seconds',
                'technical_optimizer_updates','science_forecast_seconds','science_budget_eligible')}))
    except BaseException as e:
        elapsed=0 if started is None else time.monotonic()-started
        job.update(status='failed',error=str(e),GPU_occupancy_seconds=elapsed,
                   technical_optimizer_updates=updates,technical_teacher_positions=technical_teachers,
                   cumulative_GPU_ledger_closed=True,ended_at=now())
        atomic_json(RUN/'job.json',job)
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('prepare','run'))
    parser.add_argument('--config-sha256')
    args=parser.parse_args()
    prepare() if args.action=='prepare' else run(args.config_sha256)
