"""Prepare a frozen direct-10B fork; long training requires explicit --train."""
import argparse
import json
import math
import os
from pathlib import Path
import platform
import shutil
import signal
import subprocess
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import torch
from jsonschema import validate
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, source_snapshot
from phase6_performance import alive, identity, finite_state
from run_base_5b import SOURCES as OLD_SOURCES, cuda_gate, test_counts, train_stage

SOURCES = (*OLD_SOURCES, 'scripts/run_base_10b.py', 'scripts/run_base_10b.sh',
           'scripts/review_base_10b_preparation.py', 'tests/test_base_10b.py',
           'tests/test_stable_extension.py')
PARENT_SHA = '916c4105ba7ab62597334a059cd34839d675fde29bb82b6fca6d30f889df6be5'


def parser():
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument('--plan', type=Path, default=ROOT / 'configs/phase6/base_10b.json')
    modes = result.add_mutually_exclusive_group(required=True)
    modes.add_argument('--freeze', action='store_true')
    modes.add_argument('--verify-only', action='store_true')
    modes.add_argument('--train', action='store_true')
    return result


def sanity(plan):
    unit = plan['spec']['batch'] * plan['spec']['context'] * plan['spec']['accumulation']
    assert unit == 32768
    assert plan['end_update'] == math.ceil(10_000_000_000 / unit)
    assert plan['decay_updates'] == round(.05 * plan['end_update'])
    assert plan['stable_end_update'] + plan['decay_updates'] == plan['end_update']
    assert plan['spec']['schedule_updates'] == plan['stable_end_update']
    assert plan['stable_end_tokens'] == plan['stable_end_update'] * unit
    assert plan['end_tokens'] == plan['end_update'] * unit
    assert plan['additional_training_tokens'] == plan['end_tokens'] - plan['parent']['tokens']
    assert plan['parent']['tokens'] == plan['parent']['update'] * unit == 4750016512
    assert plan['end_tokens'] + 1 < plan['unique_train_tokens']
    assert (plan['data_mixture'], plan['parameters']) == ({'web': 1.0}, 10001152)
    assert plan['output'] == 'reports/phase6/base-10b-20261004'
    assert plan['preparation_gpu_budget_seconds'] <= plan['gpu_budget_seconds']
    assert plan['gpu_budget_seconds'] + plan['reserved_evaluation_gpu_seconds'] == 10800
    assert plan['minimum_lr_ratio'] == .1 and plan['verification_input_tokens'] == 524288
    assert {k:v for k,v in plan['spec'].items() if k != 'schedule_updates'} == {
        k:v for k,v in plan['parent']['spec'].items() if k != 'schedule_updates'}
    assert not plan['quality_targets_achieved'] and not plan['evaluation_started']


def freeze(path):
    previous = read_json(ROOT / 'configs/phase6/base_5b.json')
    parent_path = ROOT / 'reports/phase6/base-5b-20261004/stable/checkpoint-00144959.pt'
    assert sha256(parent_path) == PARENT_SHA
    state = torch.load(parent_path, map_location='cpu', weights_only=False)
    assert state['update'] == 144959 and state['tokens'] == 4750016512
    assert state['implementation_sha256'] == implementation_hashes() == previous['implementation']
    assert state['spec'] == previous['spec'] and state['spec']['scheduler'] == 'wsd'
    assert all(g['lr'] == .002 for g in state['optimizer']['param_groups']) and finite_state(state)
    assert state['sampler']['epoch'] == 0 and state['sampler']['position'] == state['update'] * 32
    assert state['shard_manifest_sha256'] == previous['shard_manifest_sha256']
    parent_review_path = ROOT / 'reports/phase6/base_5b_review.json'
    parent_review = read_json(parent_review_path)
    assert parent_review['stages']['stable']['sha256'] == PARENT_SHA and all(parent_review['checks'].values())
    evidence_path = ROOT / 'reports/phase6/eos_5b_finish_review.json'
    evidence = read_json(evidence_path)
    assert all(evidence['checks'].values()) and all(evidence['growth_checks']['web'].values())
    assert all(evidence['arms']['web']['all400'][k] == 0 for k in ('unicode_failure', 'empty', 'role_leak'))
    tests_path = ROOT / 'reports/phase6/base_10b_tests.xml'
    counts = test_counts(tests_path)
    assert counts['tests'] >= 10
    plan = dict(previous)
    plan.update(version=1, scope='Step1 preparation and CUDA resume verification only now; --train is a separate future action',
        output='reports/phase6/base-10b-20261004',
        parent=dict(path=str(parent_path),sha256=PARENT_SHA,update=state['update'],tokens=state['tokens'],
                    spec=state['spec'],token_digest=state['token_digest']),
        model_config=state['model_config'], spec=dict(state['spec'],schedule_updates=289917),
        stable_end_update=289917, stable_end_tokens=9500000256, decay_updates=15259,
        end_update=305176, end_tokens=10000007168, additional_training_tokens=5249990656,
        decay_fraction_actual=15259/305176, decay_rounding='Nearest completed update to5percent of direct10B',
        gpu_budget_seconds=9000, preparation_gpu_budget_seconds=600, reserved_evaluation_gpu_seconds=1800,
        maximum_output_bytes=32*1024**3, estimated_training_seconds=5249990656/694000,
        estimated_checkpoint_bytes=170*Path(parent_path).stat().st_size,
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        go_evidence=dict(path=str(evidence_path),sha256=sha256(evidence_path),baseline='Web5.1B raw-policy growth gate passed; short20 not adopted'),
        stable_parent_evidence=dict(path=str(parent_review_path),sha256=sha256(parent_review_path)),
        tests=dict(path=str(tests_path),sha256=sha256(tests_path),counts=counts),
        target_comparison=dict(parent5B_BPB=.9644840703259737,bestWeb5_1B_BPB=.9580919810615859,
            maximum_BPB_regression=.001,fixed_repetition_increase_must_be_less_than=8,
            all400_raw_unicode_empty_role_required=0,quality_targets_unchanged=True),
        preparation_stop_boundary='After verified configuration/CUDA save-resume/report/local commit; before scientific10B training',
        training_stop_boundary='After direct10B training; evaluation is a separate command',
        restart_command='bash scripts/run_base_10b.sh --train', created_at=now())
    sanity(plan)
    assert plan['estimated_checkpoint_bytes'] < plan['maximum_output_bytes']
    if path.exists():
        old = read_json(path)
        assert {k:v for k,v in old.items() if k != 'created_at'} == {k:v for k,v in plan.items() if k != 'created_at'}
        return old
    write_json(path,plan)
    schema = ROOT / 'schemas' / path.relative_to(ROOT).with_suffix('.schema.json')
    write_json(schema,dict(**{'$schema':'https://json-schema.org/draft/2020-12/schema'},type='object',
        additionalProperties=False,required=list(plan),properties={k:dict(const=v) for k,v in plan.items()}))
    return plan


def binding_for(plan,path):
    return dict(plan_sha256=sha256(path),implementation=plan['implementation'],
                source_sha256=plan['source_sha256'],parent=plan['parent'])


def require_prepared(output,binding):
    prepared = read_json(output / 'preparation.json')
    gate = read_json(output / 'cuda-resume-gate.json')
    assert prepared['status'] == 'ready_for_explicit_training' and prepared['binding'] == binding
    assert prepared['scientific_training_input_tokens'] == 0
    assert gate['binding'] == binding and gate['passed'] and all(gate['checks'].values())
    assert prepared['verification_input_tokens'] == gate['input_tokens'] == 524288
    assert sha256(output / 'cuda-resume-gate.json') == prepared['cuda_gate_sha256']
    for name,digest in gate['checkpoint_sha256'].items():
        assert sha256(Path(name)) == digest
    return prepared


def inspect_jobs(output):
    for path in (ROOT / 'reports').rglob('*job.json'):
        record = read_json(path)
        if all(k in record for k in ('pid','boot_id','start_ticks')) and record['pid'] != os.getpid() and alive(record):
            raise RuntimeError(f'Identified live job: {path}')
    check = subprocess.run(['nvidia-smi','--query-compute-apps=pid','--format=csv,noheader'],
                           check=True,capture_output=True,text=True)
    if check.stdout.strip():
        raise RuntimeError('GPU compute process exists; do not duplicate')


def main():
    args = parser().parse_args()
    torch.set_num_threads(2)
    assert sys.version_info[:3] == (3,12,7), 'Use pinned uv Python3.12.7'
    if args.freeze:
        plan = freeze(args.plan)
        print(json.dumps(dict(status='frozen10B_preparation',additional_tokens=plan['additional_training_tokens'])))
        return
    plan = read_json(args.plan)
    validate(plan,read_json(ROOT / 'schemas' / args.plan.relative_to(ROOT).with_suffix('.schema.json')))
    sanity(plan)
    assert implementation_hashes() == plan['implementation']
    assert {p:sha256(ROOT/p) for p in SOURCES} == plan['source_sha256']
    for key in ('go_evidence','stable_parent_evidence','tests'):
        assert sha256(Path(plan[key]['path'])) == plan[key]['sha256']
    assert sha256(Path(plan['parent']['path'])) == plan['parent']['sha256']
    assert sha256(ROOT / plan['tokenizer']) == plan['tokenizer_sha256']
    assert shutil.disk_usage(Path(plan['shards'])).free >= plan['minimum_free_bytes']
    output = ROOT / plan['output']
    output.mkdir(parents=True,exist_ok=True)
    binding = binding_for(plan,args.plan)
    job_path = output / ('preparation-job.json' if args.verify_only else 'job.json')
    old = read_json(job_path) if job_path.exists() else {}
    if old:
        assert old['binding'] == binding
        assert not alive(old), 'Exact job identity is still live'
        if old['status'] == 'complete':
            if args.verify_only:
                require_prepared(output,binding)
            else:
                result = read_json(output / 'result.json')
                assert result['binding'] == binding and result['tokens'] == plan['end_tokens']
                assert sha256(Path(result['checkpoint'])) == result['checkpoint_sha256']
            print(json.dumps(dict(status='already_complete',mode='verify' if args.verify_only else 'train')))
            return
    prepared = None if args.verify_only else require_prepared(output,binding)
    inspect_jobs(output)
    prior = old.get('gpu_elapsed_seconds',0) if old else (0 if args.verify_only else prepared['gpu_elapsed_seconds'])
    budget = plan['preparation_gpu_budget_seconds'] if args.verify_only else plan['gpu_budget_seconds']
    assert prior < budget, 'Existing cumulative GPU budget is exhausted'
    job = dict(**identity(),status='running',mode='verify-only' if args.verify_only else 'train',
        started_at=now(),binding=binding,gpu_elapsed_seconds=prior,gpu_budget_seconds=budget,
        command=sys.argv,restart_command='bash scripts/run_base_10b.sh --verify-only' if args.verify_only else plan['restart_command'])
    atomic_json(job_path,job)
    start,stopped = [None],[False]
    signal.signal(signal.SIGTERM,lambda *_:stopped.__setitem__(0,True))
    signal.signal(signal.SIGINT,lambda *_:stopped.__setitem__(0,True))
    def check():
        if stopped[0]:
            raise InterruptedError('Stop requested; completed training update will be saved')
        if start[0] is not None and prior+time.monotonic()-start[0] >= budget:
            raise TimeoutError('Frozen cumulative GPU budget exhausted')
    def heartbeat(stage,**fields):
        job.update(stage=stage,heartbeat_at=now(),**fields)
        if start[0] is not None:
            job['gpu_elapsed_seconds'] = prior+time.monotonic()-start[0]
        atomic_json(job_path,job)
    try:
        web = TrainView(plan['shards'],plan['shard_manifest_sha256'])
        assert len(web.tokens) == plan['unique_train_tokens']
        assert torch.cuda.is_available() and torch.cuda.is_bf16_supported()
        assert '4090' in torch.cuda.get_device_name(0)
        write_json(output / 'environment.json',dict(python=sys.version,executable=sys.executable,
            torch=torch.__version__,torch_cuda=torch.version.cuda,device=torch.cuda.get_device_name(0),
            platform=platform.platform(),mode=job['mode'],recorded_at=now()))
        torch.cuda.set_per_process_memory_fraction(plan['memory_fraction'])
        if not (output / 'source_sha256.json').exists():
            write_json(output / 'source_sha256.json',source_snapshot(output / 'snapshot'))
        with gpu_lock('cuda'):
            start[0] = time.monotonic()
            heartbeat('cuda-resume-gate')
            gate = cuda_gate(plan,web,output,binding,check)
            if args.verify_only:
                assert not any((output/name).exists() for name in ('stable','decay','result.json'))
                preparation = dict(status='ready_for_explicit_training',binding=binding,
                    verification_input_tokens=gate['input_tokens'],verification_optimizer_updates=gate['optimizer_updates'],
                    scientific_training_input_tokens=0,cuda_gate_sha256=sha256(output / 'cuda-resume-gate.json'),
                    gpu_elapsed_seconds=prior+time.monotonic()-start[0],
                    stop_boundary=plan['preparation_stop_boundary'],created_at=now())
                write_json(output / 'preparation.json',preparation)
                heartbeat('verified-stop-before-scientific-training')
            else:
                stages = {}
                for stage in ('stable','decay'):
                    heartbeat(stage)
                    stages[stage] = train_stage(plan,web,output,stage,binding,heartbeat,check)
                assert sum(s['additional_input_tokens'] for s in stages.values()) == plan['additional_training_tokens']
                assert stages['decay']['tokens'] == plan['end_tokens']
                result = dict(status='complete_training_only',binding=binding,stages=stages,
                    checkpoint=stages['decay']['checkpoint'],checkpoint_sha256=stages['decay']['checkpoint_sha256'],
                    tokens=stages['decay']['tokens'],update=stages['decay']['update'],
                    scientific_additional_input_tokens=plan['additional_training_tokens'],
                    verification_input_tokens=gate['input_tokens'],resume_gate_passed=gate['passed'],
                    parent_unchanged=sha256(Path(plan['parent']['path']))==plan['parent']['sha256'],
                    quality_targets_achieved=False,evaluation_started=False,test_split_used=False,completed_at=now())
                assert result['parent_unchanged']
                write_json(output / 'result.json',result)
                heartbeat('finished',tokens=result['tokens'],update=result['update'])
            job.update(status='complete',completed_at=now())
            print(json.dumps(dict(status='ready_for_explicit_training' if args.verify_only else 'complete_training_only',
                                  scientific_training_started=not args.verify_only)),flush=True)
    except BaseException as error:
        job.update(status='interrupted' if isinstance(error,(InterruptedError,TimeoutError)) else 'failed',
                   failure=f'{type(error).__name__}: {error}',finished_at=now())
        raise
    finally:
        if start[0] is not None:
            job['gpu_elapsed_seconds'] = prior+time.monotonic()-start[0]
        atomic_json(job_path,job)


if __name__ == '__main__':
    main()
