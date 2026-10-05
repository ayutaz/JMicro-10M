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

DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/condition-v2-20261005')
RUN = ROOT / 'reports/phase6/condition-v2-100m-20261005'
PARENT = '410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290'
SOURCES = ('scripts/review_condition_v2_calibration.py',
    'scripts/prepare_condition_story_pools_v2.py', 'scripts/review_condition_v2_data.py',
    'src/jmicro/condition_story_quality_v2.py', 'tests/test_condition_story_quality_v2.py',
    'scripts/prepare_matched_story_pools.py', 'scripts/prepare_complete_units.py',
    'src/jmicro/complete_units.py', 'src/jmicro/story_quality.py', 'src/jmicro/tokenizer.py',
    'src/jmicro/condition_story_quality.py', 'scripts/prepare_condition_v2.py')


def data_review():
    assert sys.version_info[:3] == (3, 12, 7)
    started = time.monotonic()
    ready = read_json(DATA / 'ready.json')
    job = read_json(DATA / 'prepare-job.json')
    diagnosis = read_json(DATA / 'calibration-review.json')
    notes_path = ROOT / 'reports/phase6/condition_v2_source_notes.json'
    supplied = read_json(notes_path)
    checks = {}

    def require(name, value):
        checks[name] = bool(value)
        assert value, name

    require('actual_builder_complete_exited_within1800',
        job['status'] == 'complete' and not alive(job)
        and ready['seconds'] <= job['elapsed_seconds'] <= 1800
        and ready['binding'] == job['binding'])
    require('disjoint_fixed32_calibration_review_completed',
        diagnosis['status'] == 'calibration_completed' and len(diagnosis['rows']) == 32
        and diagnosis['additional_scientific_training_tokens'] == 0
        and diagnosis['selector_sha256'] == ready['binding']['selector_sha256'])
    require('frozen_builder_selector_diagnosis_hashes',
        ready['binding']['builder_sha256'] == sha256(ROOT / SOURCES[1])
        and ready['binding']['selector_sha256'] == sha256(ROOT / SOURCES[3])
        and ready['binding']['source_calibration_sha256'] == sha256(DATA / 'calibration-review.json')
        and ready['binding']['calibration_sha256'] == sha256(DATA / 'calibration.json'))
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
            and not hashes[arm].intersection(ready['binding']['excluded_inspected_hashes'])
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
        and summaries['control']['tokens'] == summaries['refined']['tokens'] == ready['totals']['control']['tokens']
        and summaries['control']['tokens'] >= 20000000)
    require('declared_length_density_overlap_recomputed',
        summaries['control']['body_tokens_mean'] == ready['body_tokens_mean']
        and summaries['control']['body_length_quantiles'] == ready['body_length_quantiles']
        and summaries['control']['EOS_per_1000_tokens'] == ready['EOS_per_1000_tokens']
        and len(hashes['control'] & hashes['refined']) == ready['control_candidate_shared_documents'])
    require('unchanged_quality_interpretation_and_incomplete_audits',
        not ready['independent_full_corpus_audit'] and not ready['independent_human_blind'])
    tests = ET.parse(RUN / 'selector-tests.xml').getroot()
    suites = tests.findall('testsuite')
    require('selector_related_five_CPU_tests_pass', len(suites) == 1
        and int(suites[0].get('tests')) == 5 and all(int(suites[0].get(k)) == 0 for k in ('failures', 'errors')))
    gates = dict(quantity_at_least20M_each=summaries['control']['tokens'] >= 20000000,
        quantity_mean_length_EOS_distribution_matched=checks['paired_exact_quantity_length_sequence_EOS_positions'],
        candidate_weak_less_than_control=summaries['refined']['weak_examples'] < summaries['control']['weak_examples'],
        candidate_weak_at_most10_of40=summaries['refined']['weak_examples'] <= 10)
    result = dict(status='evidence_audit_passed', checks=checks, preparation_gates=gates,
        accepted_for_experiment=all(gates.values()), summaries=summaries, individual_reviews=reviewed,
        notes_sha256=sha256(notes_path), ready_sha256=sha256(DATA / 'ready.json'),
        calibration_review_sha256=sha256(DATA / 'calibration-review.json'), job_sha256=sha256(DATA / 'prepare-job.json'),
        plan_sha256=sha256(ROOT / 'docs/64_condition_selector_v2_execution.md'),
        reviewer_sha256=sha256(Path(__file__)), source_sha256={p: sha256(ROOT / p) for p in SOURCES},
        review_seconds=time.monotonic() - started, preparation_seconds=job['elapsed_seconds'],
        reviewer=supplied['reviewer'], rubric=supplied['rubric'], checked_at=now(),
        shared_documents=ready['control_candidate_shared_documents'],
        scientific_training_tokens=0, verification_tokens=0, protected_test_used=False,
        interpretation=ready['interpretation'], independent_full_corpus_audit=False)
    write_json(RUN / 'data-review.json', result)
    print(json.dumps(dict(status=result['status'], accepted_for_experiment=result['accepted_for_experiment'],
        weak={a: s['weak_examples'] for a, s in summaries.items()}, checks=len(checks), seconds=result['review_seconds'])))



if __name__ == '__main__':
    data_review()
