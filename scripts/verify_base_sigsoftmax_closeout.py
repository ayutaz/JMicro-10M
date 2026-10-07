"""Check live-job refusal and rating lineage with an actual historical fixture.

No current generated content is rated and no scientific completion is created.
"""
from copy import deepcopy
from pathlib import Path
import sys

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from phase6_performance import alive
import complete_base_sigsoftmax as closeout


def main():
    phase = ROOT / 'reports/phase6'
    output = phase / 'base_sigsoftmax_closeout_preparation.json'
    if output.exists():
        raise ValueError('Preserve existing preparation evidence')
    c, policy = closeout.load_policy()
    job = read_json(closeout.RUN / 'job.json')
    if not alive(job) or job['status'] != 'running':
        raise ValueError('Actual same scientific job must be live for this check')
    protected = [phase / f'base_sigsoftmax_{name}' for name in (
        'comparison_completion.json', 'comparison_evidence.tar.gz',
        'comparison_evidence_manifest.json', 'rating_reuse.json')]
    if any(p.exists() for p in protected):
        raise ValueError('Unexpected scientific terminal evidence')
    try:
        closeout.main()
    except ValueError as error:
        refusal = str(error)
        if refusal != 'Scientific process must finish and exit before archive':
            raise
    else:
        raise ValueError('Live scientific closeout was accepted')
    if any(p.exists() for p in protected):
        raise ValueError('Live refusal wrote completion artifacts')

    # Reuse the already-read native-hint80 as a historical protocol fixture.
    # This is not reading or rating the current sigsoftmax80.
    original_raw, original_notes = closeout.RAW, closeout.NOTES
    original_read = closeout.read_json
    proposal = closeout.checked(c['proposal'])
    old = closeout.checked(proposal['references']['base_native_hint_comparison_completion.json'])
    closeout.RAW = phase/'base-native-hint-comparison-20261007/evaluation/native_hint/evaluation/generation.json'
    closeout.NOTES = Path(old['notes']['path'])
    try:
        fixture = closeout.exact_rating_reuse(policy)
        if len(fixture['selected']) != 80 or fixture['historical_notes_changed']:
            raise ValueError('Historical full80 lineage check failed')
        edited = deepcopy(read_json(closeout.NOTES))
        edited['notes'][0][1] = (edited['notes'][0][1] + 1) % 3
        # The historical fixture intentionally shares candidate/prior file paths.
        # Change only the first candidate read, keeping prior ratings immutable.
        candidate_notes_read = False
        def candidate_only_edit(path):
            nonlocal candidate_notes_read
            if Path(path) == closeout.NOTES and not candidate_notes_read:
                candidate_notes_read = True
                return edited
            return original_read(path)
        closeout.read_json = candidate_only_edit
        try:
            closeout.exact_rating_reuse(policy)
        except ValueError as error:
            changed_refusal = str(error)
            if not changed_refusal.startswith('Previously rated identical text score differs: '):
                raise
        else:
            raise ValueError('Changed identical historical score accepted')
    finally:
        closeout.RAW, closeout.NOTES = original_raw, original_notes
        closeout.read_json = original_read

    atomic_json(output, dict(
        created_at=now(), status='closeout_preparation_verified_not_scientific_completion',
        source=dict(path=str(Path(closeout.__file__)), sha256=sha256(Path(closeout.__file__))),
        verifier=dict(path=str(Path(__file__)), sha256=sha256(Path(__file__))),
        config_sha256=sha256(closeout.CONFIG),
        actual_live_identity={k: job[k] for k in ('pid', 'boot_id', 'start_ticks')},
        live_closeout_rejected=refusal, no_terminal_artifacts_written=True,
        historical_fixture_selected=len(fixture['selected']),
        historical_fixture_differences=len(fixture['legacy_score_differences_preserved']),
        fixed_priority=fixture['fixed_reference_priority'], historical_fixture_refs=fixture['references'],
        changed_identical_historical_rating_rejected=changed_refusal,
        historical_ratings_changed=False, new_candidate80_read=0, GPU_seconds=0,
        Base_complete=False, Chat_started=False, quantization_started=False))
    print('Actual live closeout rejected; historical80 lineage preserved; modified score rejected; GPU0')


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
