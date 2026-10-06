"""Persist terminal quality, measured cost and portable text; never adopt a pilot."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import math
import tarfile
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_web_kl_comparison_v3 as study


def main():
    c, *_ = study.inspect(study.CONFIG)
    result = read_json(study.RUN / 'compare-result.json')
    review_path = study.RUN / 'review.json'
    review = read_json(review_path)
    job = read_json(study.RUN / 'job.json')
    probe = study.probe_evidence()
    if job['status'] != 'complete' or alive(job) or review['result_sha256'] != sha256(study.RUN / 'compare-result.json'):
        raise ValueError('Reviewed terminal actual science required')
    control, treatment = [result['evaluations'][k] for k in ('control', study.ARM)]
    a, b = control['body']['rows'], treatment['body']['rows']
    if len(a) != 256 or len(b) != 256 or any((x['doc_id'], x['body_bytes'], x['body_tokens']) != (y['doc_id'], y['body_bytes'], y['body_tokens']) for x,y in zip(a,b,strict=True)):
        raise ValueError('Same paired common-byte documents required')
    paired = dict(body_NLL_worse=sum(y['body_nll'] > x['body_nll'] for x,y in zip(a,b,strict=True)),
        body_NLL_better=sum(y['body_nll'] < x['body_nll'] for x,y in zip(a,b,strict=True)),
        gold_EOS_NLL_better=sum(y['eos_nll'] < x['eos_nll'] for x,y in zip(a,b,strict=True)),
        gold_EOS_NLL_worse=sum(y['eos_nll'] > x['eos_nll'] for x,y in zip(a,b,strict=True)),
        body_bytes=472055, body_tokens=122343, GPU_seconds=0,
        note='Existing paired raw likelihoods only; true-end gold EOS is not proof of appropriate generated stopping.')
    total_GPU = result['GPU_seconds'] + probe['GPU_seconds'] + study.PRIOR_GPU
    if total_GPU > study.CEILING:
        raise ValueError('All GPU attempts must fit original ceiling')
    launch = read_json(ROOT / 'reports/phase6/web_kl_comparison_launch.json')
    record = result['checkpoints'][study.ARM]
    report = dict(status='parent_Web_KL_terminal_pilot_reviewed', created_at=now(),
        config=study.reference(study.CONFIG), result=study.reference(study.RUN / 'compare-result.json'),
        review=study.reference(review_path), launch=study.reference(ROOT / 'reports/phase6/web_kl_comparison_launch.json'),
        job=study.reference(study.RUN / 'job.json'), actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
        checkpoint=dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']),
        ordinary_CE_teacher_tokens=study.TOTAL, main_input_tokens=record['additional_input_tokens'],
        reference_input_tokens=record['reference_input_tokens'],
        reference_soft_target_body_positions=record['reference_soft_target_body_positions'],
        combined_student_input_tokens=record['combined_student_physical_input_tokens'],
        known_verification_teacher_tokens=launch['known_verification_teacher_tokens'],
        known_verification_reference_input_tokens=launch['known_verification_reference_input_tokens'],
        known_verification_reference_soft_positions=launch['known_verification_reference_soft_positions'],
        failed_first_executed_update_count=launch['failed_v1_executed_update_count'],
        science_GPU_seconds=result['GPU_seconds'], all_verification_GPU_seconds=c['verification_GPU_seconds'],
        all_GPU_seconds=total_GPU, total_GPU_ceiling_seconds=study.CEILING,
        summaries=review['summaries'], quality_comparison=review['quality_comparison'],
        absolute_dev_screen=review['absolute_dev_screen'], original_Web=review['original_Web'],
        retained_source_checks=review['retained_source_checks'], reference_accounting=review['reference_accounting'],
        paired_likelihood_diagnostic=paired,
        eligible_for_final_Base_validation=review['eligible_for_final_Base_validation'],
        all80_individually_read=True, independent_human_blind=False, quality_criteria_unchanged=True,
        newly_prepared_source_tokens=0, Base_complete=False, Base_adopted=False,
        Chat_started=False, quantization_started=False, protected_test_used=False,
        next_action=('Prepare independent learned seed and fulldev validation before protected-test adoption; Base only.'
            if review['eligible_for_final_Base_validation'] else
            'Record the failed fixed parent-KL hypothesis and paired body/EOS evidence. Do not adopt, sweep coefficient/temperature/order/source/LR, extend training automatically or scan favorable checkpoints. Plan the next evidence-based bounded Base action separately.'))
    target = ROOT / 'reports/phase6/web_kl_comparison_completion.json'
    if target.exists():
        raise ValueError('Preserve existing terminal record')
    atomic_json(target, report)
    extensions = {'.json','.jsonl','.py','.ps1','.xml','.tsv','.log','.toml','.md'}
    paths = set()
    for directory in ('web-kl-comparison-20261006','web-kl-comparison-v2-20261006','web-kl-comparison-v3-20261006'):
        paths.update(p for p in (ROOT / 'reports/phase6' / directory).rglob('*') if p.is_file() and p.suffix in extensions)
    paths.update(p for p in (ROOT / 'reports/phase6').glob('web_kl_*') if p.is_file() and p.suffix in extensions)
    paths.update((ROOT / 'configs/phase6').glob('web_kl_*.json'))
    paths.update((ROOT / 'scripts').glob('*web_kl*'))
    paths.add(ROOT / 'scripts/resident_web_window.py')
    paths.update((ROOT / 'tests').glob('test_web_kl*.py'))
    paths.add(ROOT / 'tests/test_resident_web_window.py')
    paths = sorted(p for p in paths if p.suffix in extensions and p.name != 'web_kl_comparison_portable.json')
    archive = ROOT / 'reports/phase6/web_kl_comparison_evidence.tar.gz'
    if archive.exists():
        raise ValueError('Preserve existing portable archive')
    manifest = {p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in paths}
    with tarfile.open(archive, 'w:gz', compresslevel=5) as tar:
        for p in paths:
            tar.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT / 'reports/phase6/web_kl_comparison_portable.json',dict(status='native_portable_text_complete',
        archive=study.reference(archive),archive_bytes=archive.stat().st_size,files=manifest,
        file_count=len(paths),raw_bytes=sum(v['bytes'] for v in manifest.values()),
        checkpoint_tensors_and_data_arrays_excluded=True,model_stays_native=True))
    print({k:report[k] for k in ('status','all_GPU_seconds','eligible_for_final_Base_validation','paired_likelihood_diagnostic')})


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
