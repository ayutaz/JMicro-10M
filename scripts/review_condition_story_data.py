"""Audit plan61's fixed data samples and its explicit preparation-failure branch.

Individual semantic labels are supplied in source_notes.json, never inferred here.
The data audit passing does not mean its separate preparation gate passed.
"""
import argparse
from collections import Counter
import json
from pathlib import Path
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.complete_units import unit_hash
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive

DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-preservation-20261005')
RUN = ROOT / 'reports/phase6/condition-preservation-100m-20261005'
PARENT = '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
SOURCES = ('scripts/diagnose_condition_preservation.py',
    'scripts/prepare_condition_story_pools.py', 'scripts/review_condition_story_data.py',
    'src/jmicro/condition_story_quality.py', 'tests/test_condition_story_quality.py',
    'scripts/prepare_matched_story_pools.py', 'scripts/prepare_complete_units.py',
    'src/jmicro/complete_units.py', 'src/jmicro/story_quality.py', 'src/jmicro/tokenizer.py')


def data_review():
    assert sys.version_info[:3] == (3, 12, 7)
    started = time.monotonic()
    ready = read_json(DATA / 'ready.json')
    job = read_json(DATA / 'prepare-job.json')
    diagnosis = read_json(DATA / 'diagnosis.json')
    notes_path = ROOT / 'reports/phase6/condition_preservation_source_notes.json'
    supplied = read_json(notes_path)
    checks = {}

    def require(name, value):
        checks[name] = bool(value)
        assert value, name

    require('actual_builder_complete_exited_within1800',
        job['status'] == 'complete' and not alive(job)
        and ready['seconds'] <= job['elapsed_seconds'] <= 1800
        and ready['binding'] == job['binding'])
    require('saved160_and_source40_diagnosis_completed',
        diagnosis['all160_prior_individual_reviews_reused']
        and diagnosis['source40_prior_individual_reviews_reused']
        and len(diagnosis['examples']) == 42 and diagnosis['scientific_training_tokens'] == 0)
    require('frozen_builder_selector_diagnosis_hashes',
        ready['binding']['builder_sha256'] == sha256(ROOT / SOURCES[1])
        and ready['binding']['selector_sha256'] == sha256(ROOT / SOURCES[3])
        and ready['binding']['source_diagnosis_sha256'] == sha256(DATA / 'diagnosis.json'))
    require('common_pinned_train_only_whole_source_contract',
        ready['binding']['source'] == 'shibatch/TinyStories-JA'
        and ready['binding']['revision'] == '155b4e5842076c90e07a4934d5b68410fe21f65f'
        and ready['source_train_only'] and ready['whole_original_stories']
        and ready['common_base_selection_and_holdout_preserved']
        and not ready['official_validation_test_acquired'])
    # Accepted input hashes are reused. No repeated scan of the old140M or Web12B.
    original = Path(ready['binding']['source_pool'])
    require('accepted_input_manifest_ready_hashes',
        sha256(original / 'manifest.json') == ready['binding']['source_manifest_sha256']
        and sha256(original / 'ready.json') == ready['binding']['source_ready_sha256'])
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    summaries, masks, sizes, hashes, slots, reviewed = {}, {}, {}, {}, {}, {}
    for arm in ('control', 'refined'):
        directory = Path(ready['pools'][arm]['pool'])
        manifest = read_json(directory / 'manifest.json')
        split = manifest['splits']['train']
        require(arm + '_manifest_stream_index_hashes',
            sha256(directory / 'manifest.json') == ready['pools'][arm]['manifest_sha256']
            and sha256(directory / 'train.bin') == split['stream_sha256']
            and sha256(directory / 'train.index.jsonl') == split['index_sha256']
            and manifest['binding'] == ready['binding'])
        ids = np.memmap(directory / 'train.bin', dtype='<u2', mode='r')
        records = [json.loads(line) for line in (directory / 'train.index.jsonl').open()]
        sizes[arm] = [r['body_tokens'] for r in records]
        offsets = np.cumsum([0] + [n + 2 for n in sizes[arm][:-1]]).tolist()
        hashes[arm] = {r['text_sha256'] for r in records}
        require(arm + '_whole_offsets_unique_train_translation_family',
            len(hashes[arm]) == len(records) == split['documents']
            and all(r['slot'] == i and r['offset'] == offsets[i]
                and r['split'] == 'train' and r['source'] == 'translation'
                and int(r['family'][:8], 16) % 100 != 0
                and r['source_manifest_sha256'] == ready['binding']['source_manifest_sha256']
                for i, r in enumerate(records)))
        masks[arm] = np.flatnonzero((ids == 2) | (ids == 3))
        expected = np.asarray([v for r in records for v in (r['offset'], r['offset'] + r['body_tokens'] + 1)])
        require(arm + '_actual_whole_BOS_EOS_positions',
            np.array_equal(masks[arm], expected)
            and np.array_equal(ids[masks[arm]], np.tile([2, 3], len(records))))
        samples_path = directory / 'samples.json'
        samples = read_json(samples_path)
        rows = samples['rows']
        slots[arm] = [r['slot'] for r in rows]
        expected_slots = sorted(np.random.default_rng(ready['binding']['seed'] + 1)
            .choice(len(records), 40, replace=False).tolist())
        require(arm + '_fixed40_random_slots_no_reroll',
            samples['seed'] == ready['binding']['seed'] + 1
            and slots[arm] == expected_slots and len(rows) == 40)
        notes = supplied['arms'][arm]
        require(arm + '_all40_individual_semantic_notes',
            len(notes) == 40 and [r[0] for r in notes] == list(range(40))
            and all(type(r[1]) is bool and isinstance(r[2], str) and len(r[2]) >= 15 for r in notes))
        reviewed[arm] = []
        for sample, (i, weak, reason) in zip(rows, notes):
            record = records[sample['slot']]
            text = tok.decode_bytes(ids[record['offset'] + 1:
                record['offset'] + record['body_tokens'] + 1].tolist()).decode('utf-8').strip()
            require(arm + '_sample' + str(i) + '_raw_and_source_identity',
                text == sample['text'] and unit_hash(text) == sample['text_sha256']
                and all(sample[k] == v for k, v in record.items()))
            reviewed[arm].append(dict(sample_index=i, slot=sample['slot'],
                text_sha256=sample['text_sha256'], text=text, weak_example=weak, rationale=reason))
        totals = dict(tokens=len(ids), documents=len(records), body_bytes=sum(r['bytes'] for r in records))
        require(arm + '_actual_totals_match_ready', totals == ready['totals'][arm]
            and all(totals[k] == split[k] for k in totals))
        summaries[arm] = dict(**totals, body_tokens_mean=sum(sizes[arm]) / len(records),
            body_length_quantiles=np.quantile(sizes[arm], [0, .25, .5, .75, 1]).tolist(),
            EOS_per_1000_tokens=1000 * len(records) / len(ids), weak_examples=sum(r[1] for r in notes),
            samples_sha256=sha256(samples_path), manifest_sha256=sha256(directory / 'manifest.json'))
    require('paired_exact_quantity_length_sequence_EOS_positions',
        sizes['control'] == sizes['refined'] and np.array_equal(masks['control'], masks['refined'])
        and slots['control'] == slots['refined']
        and summaries['control']['tokens'] == summaries['refined']['tokens'] == 20000028)
    require('declared_length_density_overlap_recomputed',
        summaries['control']['body_tokens_mean'] == ready['body_tokens_mean']
        and summaries['control']['body_length_quantiles'] == ready['body_length_quantiles']
        and summaries['control']['EOS_per_1000_tokens'] == ready['EOS_per_1000_tokens']
        and len(hashes['control'] & hashes['refined']) == ready['control_candidate_shared_documents'])
    require('unchanged_quality_interpretation_and_incomplete_audits',
        not ready['independent_full_corpus_audit'] and not ready['independent_human_blind'])
    tests = ET.parse(RUN / 'selector-tests.xml').getroot()
    suites = tests.findall('testsuite')
    require('selector_related_four_CPU_tests_pass', len(suites) == 1
        and int(suites[0].get('tests')) == 4 and all(int(suites[0].get(k)) == 0 for k in ('failures', 'errors')))
    gates = dict(quantity_at_least20M_each=summaries['control']['tokens'] >= 20000000,
        quantity_mean_length_EOS_distribution_matched=checks['paired_exact_quantity_length_sequence_EOS_positions'],
        candidate_weak_less_than_control=summaries['refined']['weak_examples'] < summaries['control']['weak_examples'],
        candidate_weak_at_most10_of40=summaries['refined']['weak_examples'] <= 10)
    result = dict(status='evidence_audit_passed', checks=checks, preparation_gates=gates,
        accepted_for_experiment=all(gates.values()), summaries=summaries, individual_reviews=reviewed,
        notes_sha256=sha256(notes_path), ready_sha256=sha256(DATA / 'ready.json'),
        diagnosis_sha256=sha256(DATA / 'diagnosis.json'), job_sha256=sha256(DATA / 'prepare-job.json'),
        plan_sha256=sha256(ROOT / 'docs/61_condition_preservation_next_plan.md'),
        reviewer_sha256=sha256(Path(__file__)), source_sha256={p: sha256(ROOT / p) for p in SOURCES},
        review_seconds=time.monotonic() - started, preparation_seconds=job['elapsed_seconds'],
        reviewer=supplied['reviewer'], rubric=supplied['rubric'], checked_at=now(),
        shared_documents=ready['control_candidate_shared_documents'],
        scientific_training_tokens=0, verification_tokens=0, protected_test_used=False,
        interpretation=ready['interpretation'], independent_full_corpus_audit=False)
    write_json(RUN / 'data-review.json', result)
    print(json.dumps(dict(status=result['status'], accepted_for_experiment=result['accepted_for_experiment'],
        weak={a: s['weak_examples'] for a, s in summaries.items()}, checks=len(checks), seconds=result['review_seconds'])))


def finish_failed_preparation():
    review = read_json(RUN / 'data-review.json')
    assert all(review['checks'].values()) and not review['accepted_for_experiment']
    assert not review['preparation_gates']['candidate_weak_at_most10_of40']
    job = read_json(DATA / 'prepare-job.json')
    ui = read_json(ROOT / 'reports/local/webui/server.json')
    with urllib.request.urlopen('http://127.0.0.1:7860/api/model', timeout=15) as response:
        http = json.load(response)
    assert alive(ui) and http['checkpoint_sha256'] == PARENT and http['training_tokens'] == 10000007168 and not http['busy']
    assert not alive(job)
    assert not any(RUN.glob('**/*.pt')) and not (RUN / 'screen-job.json').exists() and not (RUN / 'full-job.json').exists()
    judgment = dict(decision='preparation_rejected_no_GPU',
        failed_gates=[k for k, v in review['preparation_gates'].items() if not v],
        weak_examples={a: s['weak_examples'] for a, s in review['summaries'].items()},
        review_sha256=sha256(RUN / 'data-review.json'), scientific_training_tokens=0,
        verification_tokens=0, full_evaluation_started=False, candidate_adopted=False,
        model_quality_changed=False, quality_targets_achieved=False,
        interpretation='Sample count21→12 is not evidence of model improvement or all-pool semantic quality. Stage3/full skipped under the unchanged preparation-failure branch.',
        next_proposal='Before any new learning, test a frozen condition-aware selector on disjoint train examples; reusing these inspected40 as validation would bias selection. No new job authorized by this proposal.',
        checked_at=now())
    write_json(RUN / 'judgment.json', judgment)
    report = ROOT / 'docs/63_condition_preservation_preparation_results.md'
    assert report.is_file()
    completion = dict(status='complete_plan61_preparation_failure_branch', checks=dict(
        stage1_saved160_source40_diagnosis=True,
        stage2_actual_matched20M_data_builder_complete_exited=job['status'] == 'complete' and not alive(job),
        stage2_all80_specific_raw_bound_notes=len(review['individual_reviews']['control']) == len(review['individual_reviews']['refined']) == 40,
        stage2_evidence_checks_all_pass=all(review['checks'].values()),
        stage2_unchanged_readiness_condition_failed=not review['accepted_for_experiment'],
        stage3_skipped_per_explicit_preparation_failure_branch=True,
        stage4_judgment_full_not_launched=True,
        original10B_UI_actual_identity_and_HTTP=True,
        scientific_verification_tokens_zero=True,
        results_report_saved=True),
        data_review_sha256=sha256(RUN / 'data-review.json'), judgment_sha256=sha256(RUN / 'judgment.json'),
        report_sha256=sha256(report), reviewer_sha256=sha256(Path(__file__)), original_UI=ui, HTTP_model=http,
        scientific_training_tokens=0, verification_tokens=0, checked_at=now(),
        stop_boundary='Plan61 preparation-failure branch delivered; stop. No100M/full/500M/1B/20B/Chat/test/push.')
    assert all(completion['checks'].values())
    write_json(RUN / 'completion.json', completion)
    print(json.dumps(dict(status=completion['status'], checks=len(completion['checks']), original_UI_PID=ui['pid'])))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--finish', action='store_true')
    args = parser.parse_args()
    if args.finish:
        finish_failed_preparation()
    else:
        data_review()
