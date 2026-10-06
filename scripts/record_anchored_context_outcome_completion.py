"""Persist actual fully reviewed Base pilot, distinct exposure ledgers and raw evidence."""
import os
os.environ['CUDA_VISIBLE_DEVICES']=''
from pathlib import Path
import sys
import tarfile
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json
from phase6_performance import alive
from record_hard_body_web_replay_completion import paired
import run_anchored_context_outcome_comparison as study


def main():
    c,*_=study.inspect(study.CONFIG);probe=study.probe_evidence()
    r=read_json(study.RUN/'compare-result.json');review=read_json(study.RUN/'review.json');job=read_json(study.RUN/'job.json')
    if (job['status']!='complete' or alive(job) or review['result_sha256']!=sha256(study.RUN/'compare-result.json')
            or r['GPU_seconds']!=job['GPU_elapsed_seconds'] or not review['all3068_main_and_reference_input_protocols_equal']
            or not review['ranking_accounting']['all_completed_train_family_order_and_ledger_rows_verified']
            or not review['all3068_main_Web_and_ranking_input_protocols_equal']
            or not review['positive_anchor_accounting']['all_completed_positive_teacher_and_loss_rows_verified']):
        raise ValueError('Actually terminal reviewed full comparison required')
    current_GPU=r['GPU_seconds']+probe['GPU_seconds']
    if current_GPU>study.CEILING:raise ValueError('Preserve original total900second ceiling')
    record=r['checkpoints'][study.ARM];ev=r['evaluations'][study.ARM]
    analysis=ROOT/'reports/phase6/anchored_context_outcome_absolute_likelihood.json'
    a=read_json(analysis)
    if (a['forward_requests'] or a['GPU_seconds'] or a['raw_requests_reused']!=2048
            or a['terminal_result_refs']!=[study.reference(study.MECHANISM_RUN/'compare-result.json'),study.reference(study.RUN/'compare-result.json')]
            or record['positive_anchor_body_teacher_tokens']!=73725
            or record['combined_hard_teacher_positions']!=100073725):
        raise ValueError('Actual same-input anchor teacher and full cached likelihood evidence required')
    report=dict(status='positive_anchor100M_terminal_pilot_fully_reviewed',created_at=now(),
        config=study.reference(study.CONFIG),result=study.reference(study.RUN/'compare-result.json'),
        review=study.reference(study.RUN/'review.json'),proposal=study.reference(study.PROPOSAL),
        checkpoint=dict(path=record['checkpoint'],sha256=record['checkpoint_sha256']),
        actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
        ordinary_CE_teacher_tokens=record['additional_supervised_tokens'],main_input_positions=record['additional_input_tokens'],
        reference_input_positions=record['reference_input_tokens'],reference_body_positions=record['reference_soft_target_body_positions'],
        reference_non_EOS_teacher_probability_mass=record['reference_non_EOS_teacher_probability_mass'],
        reference_omitted_EOS_probability_mass=record['reference_soft_target_body_positions']-record['reference_non_EOS_teacher_probability_mass'],
        main_and_Web_reference_physical_positions=record['main_and_Web_reference_physical_input_tokens'],
        ranking_exposure=record['ranking_exposure'],combined_student_physical_positions=record['combined_student_physical_input_tokens'],
        combined_student_valid_positions=record['combined_student_valid_input_tokens'],
        ranking_ordinary_CE_teacher_tokens=0,ranking_soft_distribution_target_positions=0,
        positive_anchor_body_teacher_tokens=record['positive_anchor_body_teacher_tokens'],
        combined_hard_teacher_positions=record['combined_hard_teacher_positions'],
        positive_anchor_accounting=review['positive_anchor_accounting'],absolute_likelihood_analysis=study.reference(analysis),
        all3068_main_Web_and_ranking_input_protocols_equal=review['all3068_main_Web_and_ranking_input_protocols_equal'],
        verification_CE_teacher_tokens=probe['verification_teacher_tokens'],
        verification_positive_anchor_teacher_tokens=probe['verification_positive_anchor_teacher_tokens'],
        verification_reference_input_positions=probe['verification_reference_input_tokens'],
        verification_reference_body_positions=probe['verification_reference_soft_positions'],
        verification_reference_non_EOS_teacher_probability_mass=probe['verification_reference_non_EOS_teacher_probability_mass'],
        verification_ranking_exposure=probe['verification_ranking'],
        training_seconds=record['training_seconds'],science_GPU_seconds=r['GPU_seconds'],verification_GPU_seconds=probe['GPU_seconds'],
        current_study_all_GPU_seconds=current_GPU,current_study_GPU_ceiling_seconds=900,
        previous_related_study_GPU_seconds=c['previous_related_study_GPU_seconds'],
        cumulative_related_GPU_seconds=current_GPU+c['previous_related_study_GPU_seconds'],
        summaries=review['summaries'],mechanism_summary=review['mechanism_summary'],mechanism_comparison=review['mechanism_comparison'],
        quality_screen_baseline=study.QUALITY_BASELINE,quality_comparison=review['quality_comparison'],
        absolute_dev_screen=review['absolute_dev_screen'],original_Web=review['original_Web'],
        retained_source_checks=review['retained_source_checks'],reference_accounting=review['reference_accounting'],
        ranking_accounting=review['ranking_accounting'],
        all3068_main_and_reference_input_protocols_equal=review['all3068_main_and_reference_input_protocols_equal'],
        bridge_aggregates=review['transfer_aggregates'],retention_aggregates=review['retention_aggregates'],
        paired_likelihood=dict(against_staged_CE=paired(r['evaluations']['control'],ev),
            against_relative_only_ranking=paired(r['mechanism_cached']['evaluations'],ev)),
        eligible_for_final_Base_validation=review['eligible_for_final_Base_validation'],
        all80_individually_read=True,independent_human_blind=False,quality_criteria_unchanged=True,
        new_original_corpus_tokens=0,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        limitations='Same historical parent/fullstate/LR/main100MCE/source order and conditional Web KL input protocol. All main/Web/pair input exposures match the ranking mechanism control; adds73725 positive hard teacher positions. Strong stagedCE remains the quality control; no equality of supervision/time is claimed. Shared local generator/nonblind repeated fixeddev/one learned seed. Strong stagedCE and absolute/historical Web guards unchanged.',
        next_action=('Independent learned seed/full dev validation before protected test and adoption; Base only.' if review['eligible_for_final_Base_validation'] else
            'Preserve rejected100M positive-likelihood anchor hypothesis and all raw language/context/exposure evidence. No coefficient/temperature/margin/order/source/LR/batch sweep, automatic extension or favorable checkpoint scan. Define one distinct bounded Base action from terminal findings separately.'))
    target=ROOT/'reports/phase6/anchored_context_outcome_comparison_completion.json'
    if target.exists():raise ValueError('Preserve terminal scientific record')
    atomic_json(target,report)
    extensions={'.json','.jsonl','.py','.ps1','.xml','.tsv','.md','.toml','.log','.lock'}
    files={p for p in study.RUN.rglob('*') if p.is_file() and p.suffix in extensions}
    files.update(p for p in (ROOT/'reports/phase6').glob('anchored_context_outcome_*') if p.suffix in extensions)
    files.update((ROOT/'configs/phase6').glob('anchored_context_outcome_*.json'))
    files.update((ROOT/'scripts').glob('*anchored_context_outcome*'));files.update((ROOT/'tests').glob('test_anchored_context_outcome*.py'))
    files.add(ROOT/'.python-version')
    files=sorted(p for p in files if (p.suffix in extensions or p.name=='.python-version')
        and p.name!='anchored_context_outcome_comparison_portable.json')
    manifest={p.relative_to(ROOT).as_posix():dict(bytes=p.stat().st_size,sha256=sha256(p)) for p in files}
    archive=ROOT/'reports/phase6/anchored_context_outcome_comparison_evidence.tar.gz'
    if archive.exists():raise ValueError('Preserve terminal evidence archive')
    with tarfile.open(archive,'w:gz',compresslevel=5) as stream:
        for p in files:stream.add(p,arcname=p.relative_to(ROOT).as_posix(),recursive=False)
    atomic_json(ROOT/'reports/phase6/anchored_context_outcome_comparison_portable.json',dict(
        status='terminal_raw_text_and_sources_portable',files=manifest,file_count=len(files),
        raw_bytes=sum(v['bytes'] for v in manifest.values()),archive=study.reference(archive),archive_bytes=archive.stat().st_size,
        checkpoint_tensors_and_data_arrays_excluded=True))
    print({k:report[k] for k in ('status','current_study_all_GPU_seconds','eligible_for_final_Base_validation','ranking_exposure')},flush=True)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
