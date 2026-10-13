"""Audit all raw outputs and NLL before completion of the remaining human-readable notes."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from chat_semantic_contract import RUN, SUITES, preflight, reference, require_ref
from phase6_performance import alive
from review_chat_semantic_observer import get_items
from audit_chat_semantic_progress import validate_generation_binding, validate_nll
from evaluate_chat_semantic import nll_windows


def main():
    config, tok, _ = preflight(ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json')
    control = read_json(require_ref(config['historical_control_evidence']))['checkpoints']
    candidate = read_json(RUN / 'S1/checkpoints.json')
    points = [('parent', 't0', config['parent'])] + [
        (arm, point, refs[point]) for arm, refs in (('S0', control), ('S1', candidate))
        for point in ('t1', 't2', 't3')]
    fixed = nll_windows(config, tok)
    raw_records, nll_records = {}, {}
    for arm, point, checkpoint in points:
        require_ref(checkpoint)
        nll_path = RUN / 'NLL' / arm / (point + '.json')
        nll_records[arm + '-' + point] = dict(reference=reference(nll_path),
            **validate_nll(read_json(nll_path), config, checkpoint, fixed))
        for suite in SUITES:
            path = RUN / 'evaluation' / arm / point / suite / 'greedy/result.json'
            evaluation, items = get_items(path)
            validate_generation_binding(evaluation, config, checkpoint, arm, point, suite)
            assert len(items) == 219
            job = read_json(path.with_name('job.json'))
            assert job['binding'] == evaluation['binding']
            if 'pid' in job:
                assert job['status'] == 'complete' and not alive(job)
            else:
                assert job['status'] == 'historical_generation_reused' and job['new_GPU_outputs'] == 0
                terminal = read_json(require_ref(job['original_job']))
                assert terminal['status'] == 'complete' and not alive(terminal)
                provenance = evaluation['historical_generation_reuse']
                original = read_json(require_ref(provenance['original_result']))
                assert original['outputs'] == evaluation['outputs'] and original['rollouts'] == evaluation['rollouts']
            raw_records[arm + '-' + point + '-' + suite] = dict(raw=reference(path),
                job=reference(path.with_name('job.json')), validated_raw_responses=len(items),
                content_review_present=path.with_name('notes.json').exists())
    assert len(raw_records) == 21 and sum(r['validated_raw_responses'] for r in raw_records.values()) == 4599
    assert len(nll_records) == 7
    result = dict(passed=True, completed_at=now(), config_sha256=config['config_sha256'],
                  observer=reference(Path(__file__)), all21_raw_suites=True, validated_raw_responses=4599,
                  all7_common_NLL_points=True, NLL_targets_per_point=2554, raw=raw_records, NLL=nll_records,
                  pending_content_reviews=[key for key, row in raw_records.items() if not row['content_review_present']],
                  content_grading_performed=False, quality_complete=False, six_stages_complete=False,
                  Base_adopted=False, Chat_adopted=False, protected_TEST_used=False)
    atomic_json(RUN / 'generation_audit.json', result)
    print('All21 raw suites/4599 responses and7 common NLL points verified; content reviews remain')


if __name__ == '__main__':
    main()
