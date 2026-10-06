"""Own loader-only performance revision, with every earlier GPU second retained."""
from pathlib import Path
import sys
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parents[1]/'scripts')]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json


def write(relative,text):
    path=ROOT/relative
    if path.exists() and path.read_text()!=text:raise ValueError('Preserve own source')
    path.write_text(text,encoding='utf-8',newline='\n')


def ref(path):return dict(path=str(path),sha256=sha256(path))


def main():
    from implement_web_kl_comparison import once
    failure_path=ROOT/'reports/phase6/web_kl_initial_CUDA_failure.json'
    previous=ROOT/'reports/phase6/web-kl-comparison-v2-20261006/probe'
    failure=read_json(failure_path);probe=read_json(previous/'result.json')
    rejected=ROOT/'reports/phase6/web_kl_v2_budget_rejection.json'
    if not probe['passed'] or not all(probe['gate']['checks'].values()) or read_json(rejected)['GPU_ceiling_seconds']!=900:
        raise ValueError('Actual correct but slower v2 and budget rejection required')
    cache_preparation=ROOT/'reports/phase6/web_kl_resident_window_preparation.json';cache=read_json(cache_preparation)
    if cache['actual_GPU_seconds'] or cache['scientific_teacher_tokens'] or cache['cache']['binding']['block_windows']!=73421:
        raise ValueError('Actual cache-only preparation required')
    proposal=ROOT/'reports/phase6/web_kl_resident_repair_proposal.json'
    if proposal.exists():raise ValueError('Preserve existing performance revision')
    atomic_json(proposal,dict(status='loader_only_revision_prepared_CUDA_not_remeasured',created_at=now(),
        initial_CUDA_failure=ref(failure_path),prior_successful_probe=ref(previous/'result.json'),prior_probe_job=ref(previous/'job.json'),
        prior_budget_rejection=ref(rejected),resident_preparation=ref(cache_preparation),
        prior_probe_GPU_seconds=failure['actual_GPU_seconds']+probe['GPU_seconds'],
        prior_GPU_components=dict(failed_first=failure['actual_GPU_seconds'],passed_v2=probe['GPU_seconds']),
        known_prior_verification_teacher_tokens=probe['verification_teacher_tokens'],
        known_prior_verification_reference_input_tokens=probe['verification_reference_input_tokens'],
        unknown_failed_optimizer_updates_preserved=True,total_GPU_ceiling_seconds=900,
        measured_v2_median_step_seconds=.18295786051021423,measured_v2_median_data_wait_seconds=.0981950169953052,
        repair='Only replace BlockSampler source slices with the same parent-selected uint16 context+1 windows held in RAM; keep BlockSampler shifts/BOS mask/seed/cursor, main/reference losses and compiled stable gradients unchanged.',
        required='New actualCUDA full resume and32 timing; compare all32 per-update loss/gradient/token/reference counters with frozen v2 except wall times. Freeze only if all priorGPU + newprobe + fullscience estimate <=900. No margin/budget/teacher/quality relaxation.',
        source_sha256={p:sha256(ROOT/p) for p in ('scripts/resident_web_kl_trainer.py','scripts/prepare_web_kl_v3_resident_repair.py')},
        newly_prepared_source_tokens=0,scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False))
    runner=(ROOT/'scripts/run_web_kl_comparison_v2.py').read_text()
    runner=runner.replace('from web_kl_condition_trainer_v2 import WebKLTrainer,KIND','from resident_web_kl_trainer import WebKLTrainer,KIND')
    runner=runner.replace('web-kl-comparison-v2-20261006','web-kl-comparison-v3-20261006')
    runner=runner.replace('web_kl_comparison_v2.json','web_kl_comparison_v3.json').replace('web_kl_probe_v2.json','web_kl_probe_v3.json')
    runner=runner.replace('FAILED_GPU','PRIOR_GPU').replace('failed_probe_GPU_seconds','prior_probe_GPU_seconds')
    runner=once(runner,"PRIOR_GPU=read_json(FAILED_PROBE)['actual_GPU_seconds']", "RESIDENT_PROPOSAL=ROOT/'reports/phase6/web_kl_resident_repair_proposal.json'\nPRIOR_GPU=read_json(RESIDENT_PROPOSAL)['prior_probe_GPU_seconds']")
    runner=once(runner,"SOURCES=tuple(dict.fromkeys((", "SOURCES=tuple(dict.fromkeys(('scripts/run_web_kl_comparison_v3.py','scripts/run_web_kl_comparison_v3.ps1',\n    'scripts/review_web_kl_comparison_v3.py','scripts/prepare_web_kl_content_review_v3.py','scripts/resident_web_kl_trainer.py',\n    'scripts/resident_web_window.py','tests/test_resident_web_window.py','tests/test_web_kl_comparison_v3.py',")
    # Old v2's repair field retains its original meaning; v3 separately binds all prior cost.
    runner=once(runner,"    if repair['prior_probe_GPU_seconds']!=PRIOR_GPU or not repair['science_conditions_unchanged']:",
        "    if repair['failed_probe_GPU_seconds']!=read_json(FAILED_PROBE)['actual_GPU_seconds'] or not repair['science_conditions_unchanged']:")
    runner=once(runner,"    p=read_json(PROPOSAL)", "    performance=read_json(RESIDENT_PROPOSAL)\n    for ref in (performance['prior_successful_probe'],performance['prior_probe_job'],performance['resident_preparation'],performance['prior_budget_rejection']):check_reference(ref)\n    for path,digest in performance['source_sha256'].items():\n        if sha256(ROOT/path)!=digest:raise ValueError('Loader-only revision differs')\n    if performance['prior_probe_GPU_seconds']!=PRIOR_GPU or performance['total_GPU_ceiling_seconds']!=CEILING:raise ValueError('Prior cost or bound changed')\n    p=read_json(PROPOSAL)")
    runner=once(runner,"        failed_probe=reference(FAILED_PROBE),", "        resident_performance=reference(RESIDENT_PROPOSAL),resident_preparation=performance_reference(),failed_probe=reference(FAILED_PROBE),")
    # Define a reference accessor before use; no loading of any training tensors here.
    pos=runner.index('def inherited_lr_preserved(')
    runner=runner[:pos]+"def performance_reference():\n    return reference(ROOT/'reports/phase6/web_kl_resident_window_preparation.json')\n\n\n"+runner[pos:]
    runner=runner.replace('scripts/run_web_kl_comparison_v2.ps1 -Mode','scripts/run_web_kl_comparison_v3.ps1 -Mode')
    # The v2 timing trajectory is a true same-math comparison, not a performance target.
    old="    return r\n\n\ndef estimate_training"
    new="""    previous=read_json(Path(read_json(RESIDENT_PROPOSAL)['prior_successful_probe']['path']))
    keys=('loss','ordinary_CE_loss','reference_KL_loss','gradient_norm','lr','token_digest','source_teachers','source_eos',
          'source_input_tokens','source_body_bytes','source_focus_teachers','reference_input_tokens','reference_soft_target_body_positions','reference_digest')
    if len(r['timing']['histories'])!=32 or len(previous['timing']['histories'])!=32:
        raise ValueError('All32 same-math update records required')
    if any(not equal_state(a[k],b[k]) for a,b in zip(r['timing']['histories'],previous['timing']['histories'],strict=True) for k in keys):
        raise ValueError('Resident reader changed actual update trajectory')
    return r


def estimate_training"""
    runner=once(runner,old,new)
    write('scripts/run_web_kl_comparison_v3.py',runner)
    ps=(ROOT/'scripts/run_web_kl_comparison_v2.ps1').read_text().replace('web-kl-v2-','web-kl-v3-').replace('web-kl-comparison-v2-','web-kl-comparison-v3-').replace('run_web_kl_comparison_v2.py','run_web_kl_comparison_v3.py')
    write('scripts/run_web_kl_comparison_v3.ps1',ps)
    review=(ROOT/'scripts/review_web_kl_comparison_v2.py').read_text().replace('import run_web_kl_comparison_v2 as study','import run_web_kl_comparison_v3 as study').replace('web_kl_comparison_v2_review.json','web_kl_comparison_v3_review.json')
    review=review.replace('failed_probe_GPU_seconds','prior_probe_GPU_seconds')
    write('scripts/review_web_kl_comparison_v3.py',review)
    post=(ROOT/'scripts/prepare_web_kl_content_review_v2.py').read_text().replace('import run_web_kl_comparison_v2 as study','import run_web_kl_comparison_v3 as study')
    write('scripts/prepare_web_kl_content_review_v3.py',post)
    tests=(ROOT/'tests/test_web_kl_comparison_v2.py').read_text().replace('import run_web_kl_comparison_v2 as study','import run_web_kl_comparison_v3 as study').replace('failed_probe_GPU_seconds=study.FAILED_GPU','prior_probe_GPU_seconds=study.PRIOR_GPU')
    write('tests/test_web_kl_comparison_v3.py',tests)
    print('Loader-only v3 prepared; v1+v2 CUDA cost remains in900-second cap')


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
