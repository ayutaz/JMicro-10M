"""NEW owned implementation comparison; charges the original cumulative cap.

Reference source/run remain immutable. Only verification states are rebound.
No scientific learning, DEV/TEST or verification-weight reuse for science.
"""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import traceback

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
import torch
from jmicro.experiment import sha256,now
from jmicro.phase5 import equal_state
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock
from jmicro.causal_qkv_contiguous import IMPLEMENTATION
from causal_qkv_contiguous_trainer import ContiguousCausalQKVTrainer,migrate_reference_verification
from causal_qkv_trainer import committed_state as reference_committed_state
from natural_context_contrast_corpus import OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from natural_context_contrast_memory import configure_resident_memory
from phase6_performance import identity,alive
from probe_context_likelihood import ref,weights_digest,passed_tests
from probe_causal_qkv import build as reference_build,check_cache,worst_shape

PREP=ROOT/'reports/phase6/causal-qkv-contiguous-preparation-20261015'
RUN=ROOT/'reports/phase6/causal-qkv-contiguous-probe-20261015'
REFERENCE=ROOT/'reports/phase6/causal-qkv-probe-20261015'
CONFIG=ROOT/'configs/phase6/causal_qkv_contiguous_probe_20261015.json'
REFERENCE_CONFIG=ROOT/'configs/phase6/causal_qkv_probe_20261015.json'
SOURCES=('scripts/probe_causal_qkv_contiguous.py','scripts/probe_causal_qkv_contiguous.ps1',
    'scripts/causal_qkv_contiguous_trainer.py','src/jmicro/causal_qkv_contiguous.py',
    'tests/test_causal_qkv_contiguous.py','tests/test_causal_qkv_contiguous_training.py',
    'tests/test_causal_qkv_contiguous_probe.py')


def assert_scope(c):
    expected=dict(kind='owned_same_math_causal_QKV_contiguous_CUDA_v1',batch=48,seed=42,
        timed_updates=32,continuous_updates=6,split_updates=[3,3],reference_comparison_updates=3,
        reference_start_update=3,capacity_shape=[48,1024],candidate_parameters=10014464,
        main_teacher_goal=100000000,combined_technical_GPU_cap_seconds=180,
        maximum_new_GPU_seconds=4800,scientific_teacher_positions=0,Base_adopted=False,TEST_prepared=False,
        runtime_implementation=IMPLEMENTATION)
    if (any(type(c.get(k)) is not type(v) or c[k]!=v for k,v in expected.items())
            or c.get('prior_reference_GPU_seconds') != 19.769017330021597
            or c.get('current_GPU_ceiling_seconds') != 180-c['prior_reference_GPU_seconds']):
        raise ValueError('Same recipe/count, explicit runtime and ORIGINAL cumulative180/4800 scope required')


def build(c,parent,device='cpu'):
    old=json.loads(Path(c['accepted_config']['path']).read_text())
    codec=Tokenizer(c['tokenizer']['path'])
    source=old['source_binding']
    sampler=OriginalTrainCorpusSampler(source['pool'],source['manifest_sha256'],codec,old['goals'],seed=42)
    if sampler.binding != source:
        raise ValueError('Accepted original material identity differs')
    # Shared semantic verification binding; the NEW kind/spec/lineage explicitly
    # identifies the runtime. This is never a scientific checkpoint conversion.
    binding=dict(parent=c['parent'],source_binding=source,weights_role='verification_only',
                 protocol='causal_QKV_owned_CUDA_technical')
    return ContiguousCausalQKVTrainer(parent,sampler,binding,batch=48,device=device,seed=42)


def prepare():
    if os.environ.get('CUDA_VISIBLE_DEVICES') != '' or CONFIG.exists() or (RUN/'job.json').exists():
        raise ValueError('Fresh CPU-only implementation-comparison preparation required')
    started=time.monotonic()
    torch.set_num_threads(2)
    proposal=json.loads((PREP/'proposal.json').read_text())
    for path,pin in proposal['reference_evidence_sha256'].items():
        if sha256(ROOT/path)!=pin:
            raise ValueError('Preserve the immutable reference evidence: '+path)
    receipt=json.loads((PREP/'CPU_equivalence.json').read_text())
    for path,pin in receipt['source_and_evidence_sha256'].items():
        if sha256(ROOT/path)!=pin:
            raise ValueError('CPU equivalence evidence changed: '+path)
    reference=json.loads(REFERENCE_CONFIG.read_text())
    result=json.loads((REFERENCE/'result.json').read_text())
    job=json.loads((REFERENCE/'job.json').read_text())
    if (alive(job) or job['status']!='complete' or not job['cumulative_GPU_ledger_closed']
            or result['config_sha256']!=sha256(REFERENCE_CONFIG) or not result['passed']
            or result['science_budget_eligible'] is not False
            or result['GPU_occupancy_seconds']!=proposal['previous_GPU_seconds']):
        raise ValueError('Actual closed budget-failed reference technical gate required')
    for path,pin in reference['sources'].items():
        if sha256(ROOT/path)!=pin:
            raise ValueError('Frozen reference implementation differs: '+path)
    tests=((PREP/'CPU_equivalence_tests_v2.xml',11),(PREP/'trainer_CPU_tests.xml',15),
           (PREP/'probe_CPU_tests.xml',11))
    for path,count in tests: passed_tests(path,count)
    for key in ('parent','accepted_config','tokenizer','capacity_payload'):
        if sha256(Path(reference[key]['path']))!=reference[key]['sha256']:
            raise ValueError('Previously accepted input differs: '+key)
    checkpoints={name:ref(REFERENCE/f'verification_{name}.pt') for name in ('zero','split','final')}
    for name,update in (('zero',0),('split',3),('final',38)):
        saved=torch.load(checkpoints[name]['path'],map_location='cpu',weights_only=False)
        if (not reference_committed_state(saved) or saved['counters']['update']!=update
                or saved['binding'].get('weights_role')!='verification_only'):
            raise ValueError('Actual immutable reference verification state required: '+name)
    c=dict(kind='owned_same_math_causal_QKV_contiguous_CUDA_v1',batch=48,seed=42,
        timed_updates=32,continuous_updates=6,split_updates=[3,3],reference_comparison_updates=3,
        reference_start_update=3,capacity_shape=[48,1024],candidate_parameters=10014464,
        main_teacher_goal=100000000,combined_technical_GPU_cap_seconds=180,
        prior_reference_GPU_seconds=result['GPU_occupancy_seconds'],
        current_GPU_ceiling_seconds=180-result['GPU_occupancy_seconds'],maximum_new_GPU_seconds=4800,
        scientific_teacher_positions=0,Base_adopted=False,TEST_prepared=False,runtime_implementation=IMPLEMENTATION,
        parent=reference['parent'],accepted_config=reference['accepted_config'],tokenizer=reference['tokenizer'],
        capacity_payload=reference['capacity_payload'],proposal=ref(PREP/'proposal.json'),
        CPU_equivalence=ref(PREP/'CPU_equivalence.json'),reference_config=ref(REFERENCE_CONFIG),
        reference_result=ref(REFERENCE/'result.json'),reference_completion=ref(REFERENCE/'completion.json'),
        reference_checkpoints=checkpoints,CPU_tests=[dict(**ref(path),expected_tests=count) for path,count in tests],
        sources={**reference['sources'],**{p:sha256(ROOT/p) for p in SOURCES}})
    assert_scope(c)
    parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
    current=build(c,parent)
    zero=host(current.state_dict())
    cpu_reference=reference_build(reference,parent)
    cpu_reference_zero=host(cpu_reference.state_dict())
    old_zero=torch.load(checkpoints['zero']['path'],map_location='cpu',weights_only=False)
    if (not equal_state(migrate_reference_verification(cpu_reference_zero),zero)
            or weights_digest(old_zero)!=weights_digest(zero)):
        raise ValueError('CPU initial state/accepted actual reference weights differ')
    c.update(initial_weights_sha256=weights_digest(zero),CPU_wall_seconds=time.monotonic()-started)
    current.sampler.handle.close()
    cpu_reference.sampler.handle.close()
    if c['CPU_wall_seconds']>30:
        raise TimeoutError('Fixed CPU30s preparation cap exhausted')
    RUN.mkdir(parents=True,exist_ok=True)
    atomic_json(CONFIG,c)
    print(json.dumps(dict(status='new_contiguous_owned_contract_frozen_no_GPU',
        prior_GPU_seconds=c['prior_reference_GPU_seconds'],remaining_technical_GPU_seconds=c['current_GPU_ceiling_seconds'],
        CPU_wall_seconds=c['CPU_wall_seconds'])),flush=True)


def inspect(pin):
    if sha256(CONFIG)!=pin: raise ValueError('Externally pinned new technical contract required')
    c=json.loads(CONFIG.read_text())
    assert_scope(c)
    for key in ('parent','accepted_config','tokenizer','capacity_payload','proposal','CPU_equivalence',
                'reference_config','reference_result','reference_completion'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']:
            raise ValueError('Frozen implementation-comparison input differs: '+key)
    for row in (*c['reference_checkpoints'].values(),*c['CPU_tests']):
        if sha256(Path(row['path']))!=row['sha256']:
            raise ValueError('Frozen technical state/CPU evidence differs')
        if 'expected_tests' in row: passed_tests(row['path'],row['expected_tests'])
    for path,pin_value in c['sources'].items():
        if sha256(ROOT/path)!=pin_value: raise ValueError('Frozen reference/new source changed: '+path)
    if (RUN/'job.json').exists() or (RUN/'result.json').exists():
        raise ValueError('Inspect the existing new job; never duplicate or relaunch a terminal probe')
    return c


def strip(row):
    return {k:v for k,v in row.items() if k not in ('seconds','data_wait_seconds')}


def run(pin):
    c=inspect(pin)
    torch.set_num_threads(2)
    torch.use_deterministic_algorithms(True)
    job=dict(status='starting',**identity(),started_at=now(),config_sha256=pin,
        prior_reference_GPU_seconds=c['prior_reference_GPU_seconds'],cumulative_GPU_ledger_closed=False)
    atomic_json(RUN/'job.json',job)
    started=result=None
    updates=teachers=0
    def check(*args):
        if args or (started is not None and time.monotonic()-started>c['current_GPU_ceiling_seconds']):
            raise TimeoutError('ORIGINAL cumulative technical180s exhausted; no extension')
    def beat(stage):
        check()
        job.update(stage=stage,heartbeat_at=now(),GPU_occupancy_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json',job)
    def learn(trainer):
        nonlocal updates,teachers
        check()
        row=trainer.step()
        updates+=1
        teachers+=row['CE_targets_this_update']
        return row
    def clear():
        gc.collect()
        torch.cuda.empty_cache()
    try:
        with gpu_lock('cuda'):
            started=time.monotonic()
            signal.signal(signal.SIGTERM,check)
            signal.signal(signal.SIGINT,check)
            if not torch.cuda.is_available(): raise RuntimeError('Actual local CUDA unavailable')
            job['status']='running'
            memory=configure_resident_memory(0)
            parent=torch.load(c['parent']['path'],map_location='cpu',weights_only=False)
            reference_config=json.loads(Path(c['reference_config']['path']).read_text())
            beat('exact_reference_vs_contiguous_from_saved3')
            old=reference_build(reference_config,parent,'cuda')
            old.load(c['reference_checkpoints']['split']['path'])
            expected_rows=[learn(old) for _ in range(3)]
            expected_state=host(old.state_dict())
            old.sampler.handle.close()
            del old
            clear()
            comparison=build(c,parent,'cuda')
            comparison.load_reference_for_verification(c['reference_checkpoints']['split']['path'])
            actual_rows=[learn(comparison) for _ in range(3)]
            if (not equal_state(migrate_reference_verification(expected_state),host(comparison.state_dict()))
                    or not equal_state([strip(r) for r in expected_rows],[strip(r) for r in actual_rows])):
                raise ValueError('Actual CUDA reference/contiguous FULL state/history not EXACT; close implementation path')
            comparison.sampler.handle.close()
            del comparison
            clear()
            beat('continuous6_fresh_original_parent')
            full=build(c,parent,'cuda')
            zero=host(full.state_dict())
            if weights_digest(zero)!=c['initial_weights_sha256']:
                raise ValueError('Fresh original-parent zero-lag state differs')
            old_zero=torch.load(c['reference_checkpoints']['zero']['path'],map_location='cpu',weights_only=False)
            if not equal_state(migrate_reference_verification(old_zero),zero):
                raise ValueError('Actual CUDA initial numerical/source/RNG state differs from reference')
            torch.save(zero,RUN/'verification_zero.pt')
            expected_rows=[learn(full) for _ in range(6)]
            expected_state=host(full.state_dict())
            groups={name:max(float(t.abs().max()) for key,t in expected_state['model'].items()
                if key.endswith('.'+name)) for name in ('q_lag','k_lag','v_lag')}
            if any(not math.isfinite(v) or v<=0 for v in groups.values()):
                raise ValueError('Actual Q/K/V lag learning required')
            full.sampler.handle.close()
            del full
            clear()
            split=build(c,parent,'cuda')
            actual_rows=[learn(split) for _ in range(3)]
            split.save(RUN/'verification_split.pt')
            if not equal_state(migrate_reference_verification(torch.load(c['reference_checkpoints']['split']['path'],
                    map_location='cpu',weights_only=False)),host(split.state_dict())):
                raise ValueError('Fresh contiguous3 differs from stored actual reference3 numerical state')
            split.sampler.handle.close()
            del split
            clear()
            resumed=build(c,parent,'cuda')
            resumed.load(RUN/'verification_split.pt')
            actual_rows.extend(learn(resumed) for _ in range(3))
            if (not equal_state(expected_state,host(resumed.state_dict()))
                    or not equal_state([strip(r) for r in expected_rows],[strip(r) for r in actual_rows])):
                raise ValueError('New runtime full numerical/history resume mismatch')
            shape=torch.load(c['capacity_payload']['path'],map_location='cpu',weights_only=False)
            before=weights_digest(host(resumed.state_dict()))
            beat('worst48x1024')
            capacity=worst_shape(resumed,shape['window'],48)
            if weights_digest(host(resumed.state_dict()))!=before or capacity['peak_VRAM_bytes']>=memory['allocator_allowance_bytes']:
                raise ValueError('Capacity changed weights or exceeded resident allowance')
            beat('active_raw_cache')
            cache=check_cache(resumed,shape['window'])
            if weights_digest(host(resumed.state_dict()))!=before:
                raise ValueError('Cache check changed weights')
            beat('steady32_same_original_windows')
            timings=[learn(resumed) for _ in range(32)]
            old_result=json.loads(Path(c['reference_result']['path']).read_text())
            if not equal_state([strip(r) for r in timings],[strip(r) for r in old_result['all32_timings']]):
                raise ValueError('All32 recorded reference/contiguous non-time histories must remain EXACT')
            final=host(resumed.state_dict())
            old_final=torch.load(c['reference_checkpoints']['final']['path'],map_location='cpu',weights_only=False)
            if not equal_state(migrate_reference_verification(old_final),final):
                raise ValueError('Contiguous38 full numerical state differs from stored reference38')
            resumed.save(RUN/'verification_final.pt')
            forecast=math.ceil(17698/32*sum(r['seconds'] for r in timings)*1.3+600)
            check()
            result=dict(status='complete',passed=True,config_sha256=pin,actual_identity=identity(),
                memory_policy=memory,reference_vs_contiguous_all_state_history_exact=True,
                stored_reference3_and38_all_numerical_state_exact=True,all32_reference_non_time_history_exact=True,
                all_state_and_history_resume_equal=True,actual_lag_coefficients_learned=True,
                lag_coefficient_group_abs_max=groups,CE_capacity=capacity,active_cache_gate=cache,
                candidate_parameters=10014464,native_parameters=10001152,runtime_implementation=IMPLEMENTATION,
                all32_timings=timings,scientific_forecast_seconds=forecast,
                verification_optimizer_updates=updates,verification_main_CE_positions=teachers,
                scientific_teacher_positions=0,DEV_opened=False,TEST_opened=False,Base_adopted=False)
            resumed.sampler.handle.close()
            del resumed
            clear()
    except Exception as error:
        result=dict(status='failed',passed=False,config_sha256=pin,actual_identity=identity(),
            error_type=type(error).__name__,error=str(error),traceback=traceback.format_exc(),
            verification_optimizer_updates=updates,verification_main_CE_positions=teachers,
            scientific_teacher_positions=0,Base_adopted=False)
    finally:
        elapsed=0 if started is None else time.monotonic()-started
        cumulative=c['prior_reference_GPU_seconds']+elapsed
        if result is None: result=dict(status='failed',passed=False,error='No terminal result')
        if cumulative>180: result.update(status='failed',passed=False,error='Original cumulative180s exceeded')
        result.update(GPU_occupancy_seconds=elapsed,prior_reference_GPU_seconds=c['prior_reference_GPU_seconds'],
            technical_GPU_seconds_including_reference=cumulative,cumulative_GPU_ledger_closed=True,
            science_budget_eligible=bool(result['passed'] and result['scientific_forecast_seconds']+cumulative<=4800))
        job.update(status=result['status'],ended_at=now(),GPU_occupancy_seconds=elapsed,
            technical_GPU_seconds_including_reference=cumulative,cumulative_GPU_ledger_closed=True)
        atomic_json(RUN/'result.json',result)
        atomic_json(RUN/'job.json',job)
    print(json.dumps({k:result.get(k) for k in ('status','passed','GPU_occupancy_seconds',
        'technical_GPU_seconds_including_reference','scientific_forecast_seconds','science_budget_eligible','error')}),flush=True)
    if not result['passed']: raise SystemExit(1)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('prepare','inspect','run'))
    parser.add_argument('--config-sha256')
    args=parser.parse_args()
    if args.action=='prepare': prepare()
    elif args.action=='inspect':
        inspect(args.config_sha256)
        print('New contiguous preflight passed; no CUDA allocation')
    else: run(args.config_sha256)
