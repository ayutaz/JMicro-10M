"""Persist terminal ablation evidence and text artifacts without adopting a pilot."""
from pathlib import Path
import sys
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import tarfile
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
import run_eos_decoupled_web_kl_comparison as study


def paired(a,b):
    left,right=a['body']['rows'],b['body']['rows']
    if len(left)!=256 or len(right)!=256 or any((x['doc_id'],x['body_bytes'],x['body_tokens'])!=(y['doc_id'],y['body_bytes'],y['body_tokens']) for x,y in zip(left,right,strict=True)):
        raise ValueError('Same fixed common-byte documents required')
    return dict(body_NLL_better=sum(y['body_nll']<x['body_nll'] for x,y in zip(left,right,strict=True)),
        body_NLL_worse=sum(y['body_nll']>x['body_nll'] for x,y in zip(left,right,strict=True)),
        gold_EOS_NLL_better=sum(y['eos_nll']<x['eos_nll'] for x,y in zip(left,right,strict=True)),
        gold_EOS_NLL_worse=sum(y['eos_nll']>x['eos_nll'] for x,y in zip(left,right,strict=True)),
        body_bytes=472055,body_tokens=122343,GPU_seconds=0)


def main():
    c,*_=study.inspect(study.CONFIG);probe=study.probe_evidence()
    r=read_json(study.RUN/'compare-result.json');review=read_json(study.RUN/'review.json');job=read_json(study.RUN/'job.json')
    if job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'compare-result.json'):
        raise ValueError('Actual reviewed terminal comparison required')
    current_GPU=r['GPU_seconds']+probe['GPU_seconds']
    if current_GPU>900:
        raise ValueError('Frozen own900-second ceiling exceeded')
    record=r['checkpoints'][study.ARM];ev=r['evaluations'][study.ARM]
    report=dict(status='conditional_non_EOS_KL_terminal_pilot_fully_reviewed',created_at=now(),
        config=study.reference(study.CONFIG),result=study.reference(study.RUN/'compare-result.json'),
        review=study.reference(study.RUN/'review.json'),proposal=study.reference(study.PROPOSAL),
        checkpoint=dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']),
        actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
        ordinary_CE_teacher_tokens=100000000,main_input_tokens=record['additional_input_tokens'],
        reference_input_tokens=record['reference_input_tokens'],reference_body_positions=record['reference_soft_target_body_positions'],
        reference_non_EOS_teacher_probability_mass=record['reference_non_EOS_teacher_probability_mass'],
        reference_omitted_EOS_teacher_probability_mass=record['reference_soft_target_body_positions']-record['reference_non_EOS_teacher_probability_mass'],
        combined_student_input_tokens=record['combined_student_physical_input_tokens'],
        verification_CE_teacher_tokens=probe['verification_teacher_tokens'],verification_reference_input_tokens=probe['verification_reference_input_tokens'],
        verification_reference_body_positions=probe['verification_reference_soft_positions'],
        verification_reference_non_EOS_teacher_probability_mass=probe['verification_reference_non_EOS_teacher_probability_mass'],
        training_seconds=record['training_seconds'],science_GPU_seconds=r['GPU_seconds'],verification_GPU_seconds=probe['GPU_seconds'],
        current_study_all_GPU_seconds=current_GPU,current_study_GPU_ceiling_seconds=900,
        previous_related_study_GPU_seconds=c['previous_related_study_GPU_seconds'],
        cumulative_related_GPU_seconds=current_GPU+c['previous_related_study_GPU_seconds'],
        summaries=review['summaries'],mechanism_summary=review['mechanism_summary'],mechanism_comparison=review['mechanism_comparison'],
        quality_screen_baseline=study.QUALITY_BASELINE,quality_comparison=review['quality_comparison'],
        absolute_dev_screen=review['absolute_dev_screen'],original_Web=review['original_Web'],
        retained_source_checks=review['retained_source_checks'],reference_accounting=review['reference_accounting'],
        all3068_main_and_reference_input_protocols_equal=review['all3068_main_and_reference_input_protocols_equal'],
        paired_likelihood=dict(against_staged_CE=paired(r['evaluations']['control'],ev),against_full_KL=paired(r['mechanism_cached']['evaluations'],ev)),
        eligible_for_final_Base_validation=review['eligible_for_final_Base_validation'],
        all80_individually_read=True,independent_human_blind=False,quality_criteria_unchanged=True,
        newly_prepared_source_tokens=0,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        limitations='Repeated fixeddev/nonblind one learned seed. CPU EOS decomposition motivated an ablation, not sole-cause proof. Main/reference windows unchanged; removing EOS term changes auxiliary probability mass. Mandatory quality comparator remains stronger stagedCE; fullKL mechanism improvement alone cannot qualify Base.',
        next_action=('Prepare independent learned seed/full dev validation before protected test and adoption; Base only.' if review['eligible_for_final_Base_validation'] else
            'Preserve rejected objective-component hypothesis, common-byte/body/goldEOS and all80 evidence. No coefficient/temperature/order/source/LR/batch sweep, automatic extension or favorable checkpoint scan. Define the next bounded Base action from terminal evidence separately.'))
    target=ROOT/'reports/phase6/eos_decoupled_web_kl_comparison_completion.json'
    if target.exists():raise ValueError('Preserve terminal record')
    atomic_json(target,report)
    extensions={'.json','.jsonl','.py','.ps1','.xml','.tsv','.md','.toml','.log'}
    files={p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in extensions}
    files.update(p for p in (ROOT/'reports/phase6').glob('eos_decoupled_web_kl_*') if p.suffix in extensions)
    files.update((ROOT/'configs/phase6').glob('eos_decoupled_web_kl_*.json'))
    files.update((ROOT/'scripts').glob('*eos_decoupled*'));files.update((ROOT/'tests').glob('test_eos_decoupled_web_kl*.py'))
    files=sorted(p for p in files if p.suffix in extensions and p.name!='eos_decoupled_web_kl_comparison_portable.json')
    manifest={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/eos_decoupled_web_kl_comparison_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve archive')
    with tarfile.open(archive,'w:gz',compresslevel=5) as tar:
        for p in files:tar.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/eos_decoupled_web_kl_comparison_portable.json',dict(status='native_portable_text_complete',
        files=manifest,file_count=len(files),raw_bytes=sum(v['bytes'] for v in manifest.values()),
        archive=study.reference(archive),archive_bytes=archive.stat().st_size,
        checkpoint_tensors_and_data_arrays_excluded=True))
    print({k:report[k] for k in ('status','current_study_all_GPU_seconds','eligible_for_final_Base_validation','paired_likelihood')},flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
