"""Archive an exited, fully reviewed tagged sigsoftmax study; no Base adoption."""
import json
from pathlib import Path
import sys
import tarfile
import urllib.request
sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, now, sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from base_sigsoftmax_model import LINK
from base_sigsoftmax_trainer import RECIPE
from review_base_sigsoftmax import CONFIG, RUN, POLICY, NOTES, RAW, load_policy


def checked(reference):
    path = Path(reference['path'])
    if sha256(path) != reference['sha256']:
        raise ValueError('Frozen historical evidence changed: ' + path.name)
    return read_json(path)


def exact_rating_reuse(policy):
    """Preserve old exact-text scores after reading current80; expose old differences."""
    refs = policy['references']
    proposal = checked(read_json(CONFIG)['proposal'])
    snapshot = checked(proposal['references']['base_completed_objective_studies_v2_20261007.json'])
    completed = {row['arm']: row['completion'] for row in snapshot['conditions']}
    if len(completed) != 6:
        raise ValueError('Six frozen completed studies required')
    phase = ROOT/'reports/phase6'
    sources = [('cached_CE', Path(refs['cached_control_raw']['path']), Path(refs['cached_control_notes']['path']),
                refs['cached_control_raw']['sha256'], refs['cached_control_notes']['sha256'])]
    order = [('middle_supervision', 'base-middle-supervision-comparison-20261007'),
             ('sam', 'base-sam-comparison-20261007'),
             ('on_policy_teacher', 'base-on-policy-teacher-comparison-20261007'),
             ('confidence_penalty', 'base-confidence-penalty-comparison-20261007'),
             ('native_teacher_KD', 'base-native-teacher-KD-science-comparison-20261007'),
             ('native_hint', 'base-native-hint-comparison-20261007')]
    for arm, folder in order:
        old = checked(completed[arm])
        sources.append((arm, phase/folder/'evaluation'/arm/'evaluation/generation.json',
                        Path(old['notes']['path']), old['generation_sha256'], old['notes']['sha256']))
    candidate, current = read_json(RAW)['outputs'], {r[0]: r[1:5] for r in read_json(NOTES)['notes']}
    if len(candidate) != 80 or len(current) != 80 or set(current) != {r['id'] for r in candidate}:
        raise ValueError('All80 unique current raw-bound ratings required')
    prior, metadata = [], []
    for name, raw, note, raw_sha, note_sha in sources:
        if sha256(raw) != raw_sha or sha256(note) != note_sha:
            raise ValueError('Historical raw/notes changed')
        prior.append((name, {r['id']: r for r in read_json(raw)['outputs']},
                      {r[0]: r[1:5] for r in read_json(note)['notes']}))
        metadata.append(dict(name=name, raw=dict(path=str(raw), sha256=raw_sha),
                             notes=dict(path=str(note), sha256=note_sha)))
    selected, differences = [], []
    for row in candidate:
        matches = [(name, scores[row['id']]) for name, rows, scores in prior
                   if row['id'] in rows and all(rows[row['id']][k] == row[k] for k in ('id','prefix','text','stop_reason'))]
        if not matches:
            continue
        name, scores = matches[0]
        if current[row['id']] != scores:
            raise ValueError('Previously rated identical text score differs: ' + row['id'])
        selected.append(dict(id=row['id'], reference=name, scores=scores))
        differences.extend(dict(id=row['id'], selected_reference=name, selected_scores=scores,
                                other_reference=other, other_scores=old)
                           for other, old in matches[1:] if old != scores)
    return dict(created_at=now(), candidate_raw_sha256=sha256(RAW), candidate_notes_sha256=sha256(NOTES),
        fixed_reference_priority=[r[0] for r in prior], references=metadata, selected=selected,
        legacy_score_differences_preserved=differences, historical_notes_changed=False,
        all_current80_individually_read=True, independent_human_blind=False, GPU_seconds=0,
        scope='Mechanical exact id/prefix/text/stop and score audit after current80 reading; not new human or blind ratings.')


def main():
    phase = ROOT/'reports/phase6'
    target = phase/'base_sigsoftmax_comparison_completion.json'
    bundle = phase/'base_sigsoftmax_comparison_evidence.tar.gz'
    manifest = phase/'base_sigsoftmax_comparison_evidence_manifest.json'
    reuse_path = phase/'base_sigsoftmax_rating_reuse.json'
    temporary = bundle.with_suffix('.tmp')
    if any(p.exists() for p in (target,bundle,manifest,reuse_path,temporary)):
        raise ValueError('Preserve existing completion/interrupted archive; inspect before retrying')
    c, policy = load_policy()
    job = read_json(RUN/'job.json')
    if alive(job) or job['status'] != 'complete':
        raise ValueError('Scientific process must finish and exit before archive')
    result = read_json(RUN/'result.json')
    if (result['status'] != 'complete' or result['config_sha256'] != job['config_sha256']
            or result['config_sha256'] != sha256(CONFIG)
            or result['actual_identity'] != {k:job[k] for k in ('pid','boot_id','start_ticks')}
            or not 0 < result['GPU_occupancy_seconds'] == job['GPU_occupancy_seconds'] <= c['GPU_budget_seconds']
            or result['total_GPU_seconds_including_probe'] != result['GPU_occupancy_seconds'] + c['probe_GPU_seconds']
            or result['total_GPU_seconds_including_probe'] > 4800 or not all(result['common_CE_checks'].values())):
        raise ValueError('Exited exact-budget same-stream scientific result required')
    review_path = phase/'base_sigsoftmax_comparison_review.json'
    review, notes = read_json(review_path), read_json(NOTES)
    if (review['config_sha256'] != sha256(CONFIG) or review['policy_sha256'] != sha256(POLICY)
            or review['result_sha256'] != sha256(RUN/'result.json') or review['GPU_seconds'] != result['GPU_occupancy_seconds']
            or review['scientific_CE_teacher_tokens'] != 100000000 or review['all80_individually_read'] is not True
            or review['notes_sha256'] != sha256(NOTES) or notes['generation_sha256'] != sha256(RAW)
            or review['quality_criteria_unchanged'] is not True
            or any(review[k] is not False for k in ('Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_scored'))):
        raise ValueError('Complete raw-bound content review required; no Base adoption here')
    trained, ev = result['training'], result['evaluation']
    if (trained['scientific_CE_teacher_tokens'] != 100000000 or trained['scientific_sigsoftmax_positions'] != 100000000
            or review['scientific_sigsoftmax_positions'] != 100000000
            or trained['sigsoftmax_recipe'] != RECIPE or c['sigsoftmax_recipe'] != RECIPE or review['sigsoftmax_recipe'] != RECIPE
            or any(r.get('output_probability_link') != LINK for r in (trained,ev,review))
            or trained['model_config']['output_probability_link'] != LINK
            or ev['linked_head_used_for_full_cache_generation_and_likelihood'] is not True):
        raise ValueError('Exact original100M tagged linked likelihood and evaluation required')
    ui = read_json(ROOT/'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model',timeout=10) as response:
        model = json.load(response)
    if not alive(ui) or model['busy'] or model['checkpoint_sha256'] != c['parent']['sha256']:
        raise ValueError('Original idle UI process and HTTP parent SHA must be restored')
    eligible = review['eligible_for_final_Base_validation']
    if type(eligible) is not bool:
        raise ValueError('Explicit qualified/rejected decision required')
    reuse = exact_rating_reuse(policy)
    launcher = phase/'base-sigsoftmax-comparison-launcher-20261007'
    launched = read_json(launcher/'result.json')
    if launched.get('status') != 'complete' or launched.get('exit_code') != 0:
        raise ValueError('Completed durable launcher result required')
    required_names = ('base_sigsoftmax_proposal.json','base_sigsoftmax_probe_launch.json',
        'base_sigsoftmax_probe_launch_archive.json','base_sigsoftmax_probe_launch_evidence_manifest.json',
        'base_sigsoftmax_tests_v2.xml','base_sigsoftmax_run_tests.xml','base_sigsoftmax_evaluation_tests.xml',
        'base_sigsoftmax_CPU_preparation_v2.json','base_sigsoftmax_closeout_preparation.json',
        'base_sigsoftmax_science_launch_snapshot.json','base_completed_objective_studies_v2_20261007.json')
    files = [CONFIG,POLICY,NOTES,review_path,Path(__file__), *[phase/name for name in required_names],
             *[launcher/name for name in ('launcher.json','result.json','stdout.log','stderr.log')]]
    if notes.get('observations'):
        observation = Path(notes['observations']['path']).resolve()
        if not observation.is_relative_to(phase.resolve()) or sha256(observation) != notes['observations']['sha256']:
            raise ValueError('Individual observation identity changed')
        files.append(observation)
    files.extend(p for p in sorted(RUN.rglob('*')) if p.is_file()
                 and p.suffix in ('.json','.jsonl','.py','.ps1','.xml','.log','.lock','.txt'))
    files = list(dict.fromkeys(files))
    if any(not p.is_file() for p in files):
        raise ValueError('Required portable scientific evidence missing')
    atomic_json(reuse_path,reuse)
    files.append(reuse_path)
    entries = [dict(path=p.relative_to(ROOT).as_posix(),bytes=p.stat().st_size,sha256=sha256(p)) for p in files]
    atomic_json(manifest,dict(created_at=now(),files=entries,tensor_or_corpus_included=False,full_checkpoints_preserved_native=True))
    with tarfile.open(temporary,'w:gz') as archive:
        for path in [*files,manifest]:
            archive.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(bundle)
    record = dict(created_at=now(),status='sigsoftmax100M_review_complete_final_validation_pending' if eligible else 'sigsoftmax100M_review_complete_rejected',
        actual_identity=result['actual_identity'],actual_process_absent_verified=True,
        scientific_CE_teacher_tokens=100000000,scientific_updates=trained['counters']['update'],
        scientific_sigsoftmax_positions=100000000,output_probability_link=LINK,sigsoftmax_recipe=RECIPE,
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'],GPU_cap_seconds=c['GPU_budget_seconds'],
        probe_GPU_seconds=c['probe_GPU_seconds'],total_GPU_seconds_including_probe=result['total_GPU_seconds_including_probe'],
        checkpoint=trained['checkpoint'],checkpoint_sha256=trained['checkpoint_sha256'],config_sha256=sha256(CONFIG),
        review=dict(path=str(review_path),sha256=sha256(review_path)),notes=dict(path=str(NOTES),sha256=sha256(NOTES)),
        exact_text_rating_reuse=dict(path=str(reuse_path),sha256=sha256(reuse_path)),generation_sha256=sha256(RAW),
        all80_individually_read=True,reused80_control_scores_unchanged=True,independent_human_blind=False,
        reused_control_GPU_seconds=0,new_unique_corpus=0,extra_parameters=0,summaries=review['summaries'],
        eligible_for_final_Base_validation=eligible,fixed_sigsoftmax_condition_closed=not eligible,
        UI_restored=dict(identity={k:ui[k] for k in ('pid','boot_id','start_ticks')},actual_alive=True,model=model),
        archive=dict(files=len(entries),bytes=sum(e['bytes'] for e in entries),manifest=dict(path=str(manifest),sha256=sha256(manifest)),
                     compressed_bundle=dict(path=str(bundle),bytes=bundle.stat().st_size,sha256=sha256(bundle))),
        Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
        quality_criteria_unchanged=True,protected_test_scored=False,final_seed_full_dev_test_adoption_pending=True,
        next_action='Qualified: independent trainedseed/fullDEV/protected finalTEST/adoption before Base completion. Rejected: close this fixed output link; no shift/temperature/calibration/variant/parent/LR/source/batch/backend/decoder/cap rescue. No Chat or quantization.')
    atomic_json(target,record)
    print(json.dumps(dict(status=record['status'],GPU_seconds=record['GPU_occupancy_seconds'],archive_files=len(entries),UI_pid=ui['pid'])))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    import argparse
    argparse.ArgumentParser(description=__doc__).parse_args()
    main()
