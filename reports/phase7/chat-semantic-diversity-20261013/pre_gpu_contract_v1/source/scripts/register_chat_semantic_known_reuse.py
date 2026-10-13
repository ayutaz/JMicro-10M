"""Rebind8 exactly matching known suites; preserve original raw/notes/jobs."""
import copy
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.training import atomic_json
from jmicro.chat_review import content_review, review_items, RUBRIC
from chat_semantic_contract import RUN, OLD, preflight, reference, require_ref, suite_ref
from evaluate_chat_semantic import load_cases, evaluation_binding
from review_chat_generalization import get_items as old_get_items
from review_chat_generalization import fingerprint
from phase6_performance import alive


def terminal_job(raw_path, evaluation):
    path = raw_path.with_name('job.json')
    job = read_json(path)
    assert job['status'] == 'complete' and job['binding'] == evaluation['binding']
    chain = [reference(path)]
    if 'pid' not in job:
        assert job['historical_reuse'] is True and job['new_GPU_work'] == 0
        provenance = evaluation['historical_reuse']
        assert provenance['identical_actual_history_and_raw_output'] and provenance['new_generated_responses'] == 0
        original_path = require_ref(provenance['raw'])
        require_ref(provenance['notes'])
        original = read_json(original_path)
        assert original['binding'] == provenance['original_binding']
        assert original['binding']['checkpoint_sha256'] == evaluation['binding']['checkpoint_sha256']
        path = original_path.with_name('job.json')
        job = read_json(path)
        chain += [provenance['raw'], reference(path)]
        assert job['status'] == 'complete' and job['binding'] == original['binding']
        if 'pid' not in job:
            reuse = job['reuse_provenance']
            assert reuse['new_GPU_generation_seconds'] == 0 and reuse['all219_raw_history_ID_bytes_verified']
            path = require_ref(reuse['original_job'])
            job = read_json(path)
            chain.append(reuse['original_job'])
    assert job['status'] == 'complete' and 'pid' in job and not alive(job)
    return reference(path), chain


def main():
    path = RUN / 'historical_control_registration.json'
    assert not path.exists(), 'Completed exact known reuses retained'
    c, tok, _ = preflight(ROOT / 'configs/phase7/chat-semantic-diversity-20261013.json')
    reuse = read_json(require_ref(c['historical_control_evidence']))
    records = []
    for arm, points in (('parent', ('t0',)), ('S0', ('t1', 't2', 't3'))):
        old_arm = 'parent' if arm == 'parent' else 'D1'
        for point in points:
            ref = c['parent'] if arm == 'parent' else reuse['checkpoints'][point]
            for suite, original_suite in (('previous', 'new'), ('old', 'old')):
                directory = OLD / 'evaluation' / old_arm / point / original_suite / 'greedy'
                original_path, original_notes_path = directory / 'result.json', directory / 'notes.json'
                original, original_items = old_get_items(original_path)
                original_notes = read_json(original_notes_path)
                original_review = content_review(original, sha256(original_path), original_notes, original_items)
                assert json.loads(json.dumps(original_review)) == read_json(directory / 'review.json')
                assert original['binding']['checkpoint_sha256'] == ref['sha256']
                assert original['binding']['suite_sha256'] == suite_ref(c, suite)['sha256']
                new_binding = evaluation_binding(c, arm, point, ref, suite)
                stable = ('checkpoint_sha256', 'tokenizer_sha256', 'suite_sha256', 'max_new_tokens', 'model_context',
                          'dtype', 'backend', 'decoding', 'evaluation_seed', 'protocol', 'implementation')
                assert all(original['binding'][key] == new_binding[key] for key in stable)
                source_job, job_chain = terminal_job(original_path, original)
                evaluation = copy.deepcopy(original)
                evaluation['binding'] = new_binding
                evaluation['historical_generation_reuse'] = dict(original_result=reference(original_path),
                                                                 original_terminal_job=source_job,
                                                                 original_terminal_chain=job_chain,
                                                                 new_GPU_generation_outputs=0,
                                                                 exact_raw_and_actual_history=True)
                target = RUN / 'evaluation' / arm / point / suite / 'greedy'
                target_path = target / 'result.json'
                assert not target_path.exists()
                atomic_json(target_path, evaluation)
                cases, _ = load_cases(suite_ref(c, suite)['path'], tok)
                current_items = review_items(evaluation, cases, tok, 1024)
                assert set(current_items) == set(original_items)
                assert all(fingerprint(current_items[key]) == fingerprint(original_items[key]) for key in current_items)
                notes = copy.deepcopy(original_notes)
                assert notes['rubric'] == RUBRIC
                notes['evaluation_sha256'] = sha256(target_path)
                notes['historical_actual_review_reuse'] = dict(original_notes=reference(original_notes_path),
                                                              original_raw=reference(original_path),
                                                              same_complete_raw_and_histories=True,
                                                              newly_authored_judgments=0,
                                                              independent_confirmation=False)
                review = content_review(evaluation, sha256(target_path), notes, current_items)
                atomic_json(target / 'notes.json', notes)
                atomic_json(target / 'review.json', review)
                atomic_json(target / 'recipe.json', new_binding)
                atomic_json(target / 'job.json', dict(status='historical_generation_reused',
                                                      original_job=source_job, binding=new_binding,
                                                      original_raw=reference(original_path), new_GPU_outputs=0,
                                                      completed_at=now()))
                records.append(dict(arm=arm, point=point, suite=suite, outputs=219,
                                    original_raw=reference(original_path), original_notes=reference(original_notes_path),
                                    original_job=source_job, current_raw=reference(target_path),
                                    original_terminal_chain=job_chain,
                                    current_notes=reference(target / 'notes.json'),
                                    new_GPU_generation=0, newly_read_judgments=0))
    assert len(records) == 8 and sum(record['outputs'] for record in records) == 1752
    atomic_json(path, dict(passed=True, created_at=now(), config_sha256=c['config_sha256'],
                           known_suite_judgments_reused=1752, suites_reused=8, records=records,
                           score_values_changed=False, original_sources_modified=False,
                           independent_quality_confirmation=False))
    print('Exactly bound8 known suites/1752 historical judgments; new generation0')


if __name__ == '__main__':
    main()
