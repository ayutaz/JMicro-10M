"""Bind the exact validator-only arithmetic correction to preserved own CUDA proof."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from probe_base_parallel_residual import CONFIG,RUN,passed_tests,validate_contract,ref

REPORT=ROOT/'reports/phase6/base_parallel_residual_validator_bridge.json'
TRAINER='scripts/base_parallel_residual_trainer.py'
TEST='tests/test_base_parallel_residual_trainer.py'
OLD='math.cos(math.pi * (tokens - warmup) / (total - warmup))'
NEW='math.cos(math.pi * ((tokens - warmup) / (total - warmup)))'


def check_source():
    p=read_json(CONFIG)
    for name in ('proposal','CPU_preparation','CPU_workflow_tests','payload'):
        if sha256(Path(p[name]['path']))!=p[name]['sha256']:
            raise ValueError('Original frozen probe reference changed: '+name)
    for reference in p['CPU_tests']:
        if sha256(Path(reference['path']))!=reference['sha256']:
            raise ValueError('Preserved old CPU result changed')
    validate_contract(read_json(Path(p['proposal']['path'])))
    for name,digest in p['source_sha256'].items():
        if name in (TRAINER,TEST):
            old_path=RUN/'source'/name
            if sha256(old_path)!=digest:raise ValueError('Actual GPU snapshot changed: '+name)
            if name==TRAINER:
                old=old_path.read_bytes()
                if old.count(OLD.encode())!=1 or old.replace(OLD.encode(),NEW.encode())!=(ROOT/name).read_bytes():
                    raise ValueError('Only exact check arithmetic alignment is authorized by this bridge')
        elif sha256(ROOT/name)!=digest:
            raise ValueError('Own CUDA-verified training/model/source changed: '+name)
    return p


def verified_probe():
    p=check_source();bridge=read_json(REPORT)
    for row in bridge['current_references'].values():
        if sha256(Path(row['path']))!=row['sha256']:
            raise ValueError('Current validator correction evidence changed')
    return p


def main():
    if REPORT.exists():raise ValueError('Preserve exact validator correction evidence')
    check_source()
    tests=ROOT/'reports/phase6/base_parallel_residual_cosine_tests.xml'
    passed_tests(tests,13)
    atomic_json(REPORT,dict(created_at=now(),
        correction='Align committed-state cosine arithmetic with unchanged TargetPositionSchedule.value. Exact equality remains required; no tolerance, training update, LR, optimizer, sampler, model, budget or quality change.',
        old_trainer=ref(RUN/'source'/TRAINER),
        current_references=dict(trainer=ref(ROOT/TRAINER),trainer_test_source=ref(ROOT/TEST),
            trainer_tests=ref(tests),initial_failed_tests=ref(ROOT/'reports/phase6/base_parallel_residual_cosine_initial_tests.xml'),
            initial_fixture_exhaustion=ref(ROOT/'reports/phase6/base_parallel_residual_cosine_fixture_initial_tests.xml'),
            probe_result=ref(RUN/'result.json'),probe_config=ref(CONFIG),bridge_source=ref(Path(__file__))),
        current_trainer_tests=13,current_total_model_trainer_evaluation_tests=27,
        actual_postwarmup_CPU_gold_each=10000,actual_CPU_postwarmup_save_resume_both=True,
        GPU_training_updates_changed=False,GPU_training_recipe_changed=False,
        additional_GPU_seconds=0,scientific_gold_tokens=0,Base_complete=False,
        Chat_started=False,quantization_started=False))
    print('Exact validator-only correction bound to preserved own CUDA proof; scientific GPU0')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
