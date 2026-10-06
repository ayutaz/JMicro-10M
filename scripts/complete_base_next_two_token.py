"""Preserve an exited, reviewed next-two study and the original local UI."""
import json
from pathlib import Path
import sys
import tarfile
import urllib.request

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, read_json, now, sha256
from jmicro.training import atomic_json
from phase6_performance import alive
from review_base_next_two_token import CONFIG, RUN, POLICY, NOTES, RAW, load_policy, audit_terminal


def main():
    phase = ROOT / 'reports/phase6'
    target = phase / 'base_next_two_token_comparison_completion.json'
    bundle = phase / 'base_next_two_token_comparison_evidence.tar.gz'
    manifest = phase / 'base_next_two_token_comparison_evidence_manifest.json'
    temporary = bundle.with_suffix('.tmp')
    if any(p.exists() for p in (target, bundle, manifest, temporary)):
        raise ValueError('Preserve existing completion or interrupted archive; inspect before retrying')
    c, _ = load_policy()
    job, result = read_json(RUN / 'job.json'), read_json(RUN / 'result.json')
    audit_terminal(job, result, c, sha256(CONFIG), alive(job))
    review_path = phase / 'base_next_two_token_comparison_review.json'
    review = read_json(review_path)
    if (review != read_json(RUN / 'review.json')
            or review['config_sha256'] != sha256(CONFIG)
            or review['review_policy_sha256'] != sha256(POLICY)
            or review['result_sha256'] != sha256(RUN / 'result.json')
            or review['GPU_occupancy_seconds'] != result['GPU_occupancy_seconds']
            or review['new_scientific_CE_teacher_tokens'] != 100000000
            or review['new80_individually_read'] is not True
            or review['reused80_individually_read'] is not True
            or review['quality_criteria_unchanged'] is not True
            or any(review[k] is not False for k in (
                'Base_complete', 'Base_adopted', 'Chat_started', 'quantization_started', 'protected_test_used'))
            or read_json(NOTES)['generation_sha256'] != sha256(RAW)):
        raise ValueError('Unchanged complete raw-bound review required; this does not adopt Base')
    ui = read_json(ROOT / 'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=10) as response:
        model = json.load(response)
    if (not alive(ui) or model['busy']
            or model['checkpoint_sha256'] != c['parent']['sha256']):
        raise ValueError('Actual original idle UI process and HTTP parent identity required')
    eligible = review['eligible_for_final_Base_validation']
    files = [CONFIG, POLICY, NOTES, review_path, Path(__file__),
             phase / 'base_next_two_token_content_review.json',
             phase / 'base_next_two_token_proposal.json',
             phase / 'base_next_two_token_science_start.json',
             phase / 'base_next_two_token_probe_completion.json',
             phase / 'base_next_two_token_trainer_tests.xml',
             phase / 'base_next_two_token_run_tests.xml',
             phase / 'base_next_two_token_review_tests.xml']
    files.extend(p for p in sorted(RUN.rglob('*')) if p.is_file()
                 and p.suffix in ('.json', '.jsonl', '.py', '.ps1', '.xml', '.log', '.lock', '.txt'))
    launcher = phase / 'base-next-two-token-comparison-launcher-20261007'
    files.extend(p for p in sorted(launcher.glob('*')) if p.is_file() and p.suffix in ('.json', '.log'))
    files = list(dict.fromkeys(files))
    if any(not p.is_file() for p in files):
        raise ValueError('Required portable experiment evidence is missing')
    entries = [dict(path=p.relative_to(ROOT).as_posix(), bytes=p.stat().st_size, sha256=sha256(p)) for p in files]
    atomic_json(manifest, dict(created_at=now(), files=entries, tensor_or_corpus_included=False,
                              full_checkpoints_preserved_native=True))
    with tarfile.open(temporary, 'w:gz') as archive:
        for path in [*files, manifest]:
            archive.add(path, arcname=path.relative_to(ROOT).as_posix(), recursive=False)
    temporary.replace(bundle)
    trained = result['results']['next_two']['training']
    record = dict(created_at=now(),
        status='next_two100M_review_complete_final_validation_pending' if eligible else 'next_two100M_review_complete_rejected',
        actual_identity=result['actual_identity'], actual_process_absent_verified=True,
        scientific_CE_teacher_tokens=100000000,
        scientific_next_two_positions=review['scientific_next_two_positions'],
        total_scientific_label_positions=review['total_scientific_label_positions'],
        scientific_updates=review['accounting']['completed_updates'],
        GPU_occupancy_seconds=result['GPU_occupancy_seconds'], GPU_cap_seconds=c['GPU_budget_seconds'],
        checkpoint=trained['checkpoint'], checkpoint_sha256=trained['checkpoint_sha256'],
        config_sha256=sha256(CONFIG), review=dict(path=str(review_path), sha256=sha256(review_path)),
        notes=dict(path=str(NOTES), sha256=sha256(NOTES)), generation_sha256=sha256(RAW),
        all80_individually_read=True, reused80_control_scores_unchanged=True, independent_human_blind=False,
        reused_control_GPU_seconds=0, new_unique_corpus=0, accounting=review['accounting'],
        summaries=review['summaries'], eligible_for_final_Base_validation=eligible,
        fixed_next_two_condition_closed=not eligible,
        UI_restored=dict(identity={k:ui[k] for k in ('pid', 'boot_id', 'start_ticks')}, actual_alive=True, model=model),
        archive=dict(files=len(entries), bytes=sum(e['bytes'] for e in entries),
                     manifest=dict(path=str(manifest), sha256=sha256(manifest)),
                     compressed_bundle=dict(path=str(bundle), bytes=bundle.stat().st_size, sha256=sha256(bundle))),
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        quality_criteria_unchanged=True, protected_test_used=False,
        final_seed_full_dev_test_adoption_pending=True, next_action=review['next_action'])
    atomic_json(target, record)
    print(json.dumps(dict(status=record['status'], GPU_seconds=record['GPU_occupancy_seconds'],
                          archive_files=len(entries), UI_pid=ui['pid']), ensure_ascii=False))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
