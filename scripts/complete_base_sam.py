"""Archive an exited, fully reviewed native two-pass SAM study and restored original UI."""
import json
from pathlib import Path
import sys
import tarfile
import urllib.request
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,now,sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from review_base_sam import CONFIG,RUN,POLICY,NOTES,RAW,load_policy


def main():
    phase=ROOT/'reports/phase6'
    target=phase/'base_sam_comparison_completion.json'
    bundle=phase/'base_sam_comparison_evidence.tar.gz'
    manifest=phase/'base_sam_comparison_evidence_manifest.json'
    temporary=bundle.with_suffix('.tmp')
    if any(p.exists() for p in (target,bundle,manifest,temporary)):
        raise ValueError('Preserve existing completion/interrupted archive; inspect before retrying')
    c,_=load_policy()
    job=read_json(RUN/'job.json')
    if alive(job) or job['status']!='complete':
        raise ValueError('Actual scientific process must finish and exit before archive')
    result=read_json(RUN/'result.json')
    if (result['status']!='complete' or result['config_sha256']!=job['config_sha256'] or
        result['config_sha256']!=sha256(CONFIG) or
        result['actual_identity']!={k:job[k] for k in ('pid','boot_id','start_ticks')} or
        not 0<result['GPU_occupancy_seconds']==job['GPU_occupancy_seconds']<=c['GPU_budget_seconds'] or
        result['total_GPU_seconds_including_probe']!=result['GPU_occupancy_seconds']+c['probe_GPU_seconds'] or
        result['total_GPU_seconds_including_probe']>7200 or
        not all(result['common_CE_checks'].values())):
        raise ValueError('Exited exact-budget same-stream native scientific result required')
    review_path=phase/'base_sam_comparison_review.json'
    review,notes=read_json(review_path),read_json(NOTES)
    if (review['config_sha256']!=sha256(CONFIG) or review['policy_sha256']!=sha256(POLICY) or
        review['result_sha256']!=sha256(RUN/'result.json') or review['GPU_seconds']!=result['GPU_occupancy_seconds'] or
        review['scientific_CE_teacher_tokens']!=100000000 or review['all80_individually_read'] is not True or
        review['notes_sha256']!=sha256(NOTES) or notes['generation_sha256']!=sha256(RAW) or
        review['quality_criteria_unchanged'] is not True or
        any(review[k] is not False for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_scored'))):
        raise ValueError('Actual complete raw-bound content review required; no Base adoption here')
    repair=review['reviewer_import_repair']
    repair_record=read_json(Path(repair['path']))
    if (sha256(Path(repair['path']))!=repair['sha256'] or
        repair['wrapper_sha256']!=sha256(ROOT/'scripts/review_base_sam_v2.py') or
        repair['original_reviewer_sha256']!=c['source_sha256']['scripts/review_base_sam.py'] or
        repair['scientific_result_sha256']!=sha256(RUN/'result.json') or
        any(repair_record[k] is not False for k in ('original_frozen_sources_changed','scientific_settings_changed','criteria_changed'))):
        raise ValueError('Preserved original reviewer and missing-import-only repair required')
    trained=result['training']
    if (trained['scientific_repeated_teacher_evaluations']!=100000000 or review['scientific_repeated_teacher_evaluations']!=100000000 or
        review['SAM']!=trained['SAM'] or trained['SAM']!=dict(updates=trained['counters']['update'],
            repeated_teacher_positions=100000000,repeated_valid_inputs=trained['counters']['CE_input_tokens'],
            repeated_physical_inputs=trained['counters']['physical_input_tokens'])):
        raise ValueError('Exact separately counted repeated100M same-batch SAM evaluation required')
    ui=read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:
        model=json.load(response)
    if not alive(ui) or model['busy'] or model['checkpoint_sha256']!=c['parent']['sha256']:
        raise ValueError('Original idle UI process and HTTP parent SHA must be restored')
    eligible=review['eligible_for_final_Base_validation']
    if type(eligible) is not bool: raise ValueError('Explicit qualified/rejected decision required')
    files=[CONFIG,POLICY,NOTES,review_path,Path(__file__),
        phase/'base_sam_proposal.json',phase/'base_sam_probe_launch.json',
        phase/'base_sam_probe_launch_archive.json',phase/'base_sam_probe_launch_evidence_manifest.json',
        phase/'base_sam_trainer_tests.xml',phase/'base_sam_run_tests.xml',
        phase/'base_sam_reviewer_import_repair.json',ROOT/'scripts/review_base_sam_v2.py']
    if notes.get('observations'):
        observation=Path(notes['observations']['path']).resolve()
        if not observation.is_relative_to(phase.resolve()) or sha256(observation)!=notes['observations']['sha256']:
            raise ValueError('Individual observation identity changed')
        files.append(observation)
    files.extend(p for p in sorted(RUN.rglob('*')) if p.is_file() and
        p.suffix in ('.json','.jsonl','.py','.ps1','.xml','.log','.lock','.txt'))
    files.extend(p for p in sorted((phase/'base-sam-comparison-launcher-20261007').glob('*')) if p.is_file() and
        p.suffix in ('.json','.log'))
    files=list(dict.fromkeys(files))
    if any(not p.is_file() for p in files): raise ValueError('Required portable scientific evidence missing')
    entries=[dict(path=p.relative_to(ROOT).as_posix(),bytes=p.stat().st_size,sha256=sha256(p)) for p in files]
    atomic_json(manifest,dict(created_at=now(),files=entries,tensor_or_corpus_included=False,full_checkpoints_preserved_native=True))
    with tarfile.open(temporary,'w:gz') as archive:
        for path in [*files,manifest]: archive.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(bundle)
    trained=result['training']
    record=dict(created_at=now(),
        status='SAM100M_review_complete_final_validation_pending' if eligible else 'SAM100M_review_complete_rejected',
        actual_identity=result['actual_identity'],actual_process_absent_verified=True,
        scientific_CE_teacher_tokens=100000000,scientific_updates=trained['counters']['update'],
        scientific_repeated_teacher_evaluations=trained['scientific_repeated_teacher_evaluations'],
        SAM=trained['SAM'],
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'],GPU_cap_seconds=c['GPU_budget_seconds'],
        probe_GPU_seconds=c['probe_GPU_seconds'],total_GPU_seconds_including_probe=result['total_GPU_seconds_including_probe'],
        checkpoint=trained['checkpoint'],checkpoint_sha256=trained['checkpoint_sha256'],config_sha256=sha256(CONFIG),
        review=dict(path=str(review_path),sha256=sha256(review_path)),notes=dict(path=str(NOTES),sha256=sha256(NOTES)),
        generation_sha256=sha256(RAW),all80_individually_read=True,reused80_control_scores_unchanged=True,
        independent_human_blind=False,reused_control_GPU_seconds=0,new_unique_corpus=0,extra_parameters=0,
        summaries=review['summaries'],eligible_for_final_Base_validation=eligible,fixed_SAM_condition_closed=not eligible,
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        archive=dict(files=len(entries),bytes=sum(e['bytes'] for e in entries),
            manifest=dict(path=str(manifest),sha256=sha256(manifest)),
            compressed_bundle=dict(path=str(bundle),bytes=bundle.stat().st_size,sha256=sha256(bundle))),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,protected_test_scored=False,final_seed_full_dev_test_adoption_pending=True,
        next_action='Qualified: independent trainedseed/fullDEV/protected finalTEST/adoption before Base completion. Rejected: close this fixed two-pass SAM condition; no rho/adaptive/period/optimizer/LR/source/parent/batch/decoder/cap rescue. No Chat or quantization.')
    atomic_json(target,record)
    print(json.dumps(dict(status=record['status'],GPU_seconds=record['GPU_occupancy_seconds'],archive_files=len(entries),UI_pid=ui['pid']),ensure_ascii=False))


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    import argparse
    argparse.ArgumentParser(description=__doc__).parse_args()
    main()
