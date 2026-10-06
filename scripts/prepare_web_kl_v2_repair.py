"""Version CUDA Graph gradient-buffer repair; retain v1 failure and budget cost."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json


def write(relative,text):
    path=ROOT/relative
    if path.exists() and path.read_text()!=text:raise ValueError('Preserve prior own version')
    path.write_text(text,encoding='utf-8',newline='\n')


def main():
    from implement_web_kl_comparison import once
    failure=read_json(ROOT/'reports/phase6/web_kl_initial_CUDA_failure.json')
    if failure['actual_GPU_seconds']<=0 or failure['scientific_teacher_tokens']:
        raise ValueError('Actual failed probe cost required')
    trainer=(ROOT/'scripts/web_kl_condition_trainer.py').read_text()
    trainer=trainer.replace("'scripts/web_kl_condition_trainer.py'","'scripts/web_kl_condition_trainer_v2.py'")
    trainer=once(trainer,"        restore_rng(parent['rng'])", "        # CUDA Graphs must accumulate into storage outside graph-owned outputs.\n        for parameter in self.model.parameters():\n            parameter.grad=torch.zeros_like(parameter)\n        restore_rng(parent['rng'])")
    trainer=once(trainer,'self.optimizer.zero_grad(set_to_none=True)','self.optimizer.zero_grad(set_to_none=False)')
    write('scripts/web_kl_condition_trainer_v2.py',trainer)
    tests=(ROOT/'tests/test_web_kl_condition_trainer.py').read_text().replace('from web_kl_condition_trainer import WebKLTrainer','from web_kl_condition_trainer_v2 import WebKLTrainer')
    write('tests/test_web_kl_condition_trainer_v2.py',tests)
    runner=(ROOT/'scripts/run_web_kl_comparison.py').read_text()
    runner=runner.replace('from web_kl_condition_trainer import WebKLTrainer,KIND','from web_kl_condition_trainer_v2 import WebKLTrainer,KIND')
    runner=runner.replace('web-kl-comparison-20261006','web-kl-comparison-v2-20261006')
    runner=runner.replace('web_kl_comparison.json','web_kl_comparison_v2.json').replace('web_kl_probe.json','web_kl_probe_v2.json')
    runner=once(runner,'SOURCES=tuple(',"FAILED_PROBE=ROOT/'reports/phase6/web_kl_initial_CUDA_failure.json'\nFAILED_GPU=read_json(FAILED_PROBE)['actual_GPU_seconds']\nSOURCES=tuple(")
    runner=once(runner,"'scripts/run_web_kl_comparison.py','scripts/run_web_kl_comparison.ps1',", "'scripts/run_web_kl_comparison_v2.py','scripts/run_web_kl_comparison_v2.ps1','scripts/run_web_kl_comparison.py','scripts/run_web_kl_comparison.ps1',\n    'scripts/web_kl_condition_trainer_v2.py','scripts/review_web_kl_comparison_v2.py','scripts/prepare_web_kl_content_review_v2.py',\n    'tests/test_web_kl_condition_trainer_v2.py','tests/test_web_kl_comparison_v2.py',")
    runner=once(runner,'failed_probe_GPU_seconds=0,','failed_probe_GPU_seconds=FAILED_GPU,')
    runner=once(runner,"c['failed_probe_GPU_seconds']!=0", "c['failed_probe_GPU_seconds']!=FAILED_GPU")
    runner=once(runner,"        KL_preparation=reference(ROOT/'reports/phase6/web_kl_trainer_preparation.json'),", "        failed_probe=reference(FAILED_PROBE),KL_repair=reference(ROOT/'reports/phase6/web_kl_v2_repair.json'),\n        KL_preparation=reference(ROOT/'reports/phase6/web_kl_trainer_preparation.json'),")
    runner=once(runner,"    old,base,parent,_,_,positive,original=cached.source_contract()", "    old,base,parent,_,_,positive,original=cached.source_contract()\n    repair=read_json(ROOT/'reports/phase6/web_kl_v2_repair.json')\n    check_reference(repair['failure'])\n    if repair['failed_probe_GPU_seconds']!=FAILED_GPU or not repair['science_conditions_unchanged']:raise ValueError('Repair budget/scope differs')\n    for path,digest in repair['source_sha256'].items():\n        if sha256(ROOT/path)!=digest:raise ValueError('Own repair source differs')")
    runner=runner.replace('scripts/run_web_kl_comparison.ps1 -Mode','scripts/run_web_kl_comparison_v2.ps1 -Mode')
    write('scripts/run_web_kl_comparison_v2.py',runner)
    ps=(ROOT/'scripts/run_web_kl_comparison.ps1').read_text().replace("'web-kl-'+$Mode", "'web-kl-v2-'+$Mode")
    ps=ps.replace('web-kl-comparison-20261006','web-kl-comparison-v2-20261006').replace('scripts/run_web_kl_comparison.py','scripts/run_web_kl_comparison_v2.py')
    write('scripts/run_web_kl_comparison_v2.ps1',ps)
    review=(ROOT/'scripts/review_web_kl_comparison.py').read_text().replace('import run_web_kl_comparison as study','import run_web_kl_comparison_v2 as study').replace('web_kl_comparison_review.json','web_kl_comparison_v2_review.json')
    write('scripts/review_web_kl_comparison_v2.py',review)
    post=(ROOT/'scripts/prepare_web_kl_content_review.py').read_text().replace('import run_web_kl_comparison as study','import run_web_kl_comparison_v2 as study')
    write('scripts/prepare_web_kl_content_review_v2.py',post)
    scope_tests=(ROOT/'tests/test_web_kl_comparison.py').read_text().replace('import run_web_kl_comparison as study','import run_web_kl_comparison_v2 as study')
    scope_tests=scope_tests.replace('failed_probe_GPU_seconds=0','failed_probe_GPU_seconds=study.FAILED_GPU')
    write('tests/test_web_kl_comparison_v2.py',scope_tests)
    record=ROOT/'reports/phase6/web_kl_v2_repair.json'
    if record.exists():raise ValueError('Preserve existing repair definition')
    paths=('scripts/web_kl_condition_trainer_v2.py','tests/test_web_kl_condition_trainer_v2.py','scripts/prepare_web_kl_v2_repair.py')
    atomic_json(record,dict(status='stable_external_grad_buffers_prepared_actualCUDA_not_rerun',created_at=now(),
        failure=dict(path=str(ROOT/'reports/phase6/web_kl_initial_CUDA_failure.json'),sha256=sha256(ROOT/'reports/phase6/web_kl_initial_CUDA_failure.json')),
        failed_probe_GPU_seconds=failure['actual_GPU_seconds'],total_GPU_ceiling_seconds=900,
        repair='Preallocate zeros_like(parameter) student grad storage before compiled runs; zero_grad(set_to_none=False). Accumulate both existing losses into the same external buffers, then unchanged clip/Adam/scheduler.',
        science_conditions_unchanged=True,source_sha256={p:sha256(ROOT/p) for p in paths},
        old_sources_preserved=True,scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False))
    print('Own v2 prepared; original failure CUDA cost charged; objective/conditions unchanged')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
