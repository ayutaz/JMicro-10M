"""Record all64 original/span readings against the predeclared source contract."""
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src')]
from jmicro.experiment import ROOT, now, sha256
from jmicro.training import atomic_json

CONFIG = ROOT / 'configs/phase6/base_hq_acceptance.json'
CONFIG_SHA = 'ac2acc4e7f17c6a2bf21b6d46282bbe9857d2205f16ea278ca07e6242afb3b4d'
ACTUAL = ROOT / 'reports/phase6/base_hq_acceptance_sample.json'
NOTES = ROOT / 'reports/phase6/base_hq_acceptance_observations.tsv'
OUT = ROOT / 'reports/phase6/base_hq_acceptance_review.json'


def byte_sha(value):
    return hashlib.sha256(value).hexdigest()


def main():
    if OUT.exists():
        raise ValueError('Preserve completed acceptance; no result-based rerating')
    started = time.process_time()
    if sha256(CONFIG) != CONFIG_SHA:
        raise ValueError('Use the contract frozen before unseen content')
    config = json.loads(CONFIG.read_text())
    actual = json.loads(ACTUAL.read_text())
    sample = Path(actual['sample']['path'])
    job = json.loads((sample.parent / 'job.json').read_text())
    if (actual['config_sha256'] != CONFIG_SHA or sha256(sample) != actual['sample']['sha256']
            or actual['selected_rows'] != 64 or job['status'] != 'complete'
            or job['config_sha256'] != CONFIG_SHA):
        raise ValueError('An unchanged, fully completed fixed64 source retrieval is required')
    stat = Path(f"/proc/{job['pid']}/stat")
    if (Path('/proc/sys/kernel/random/boot_id').read_text().strip() == job['boot_id']
            and stat.exists()
            and stat.read_text().rsplit(')', 1)[1].split()[19] == job['start_ticks']):
        raise ValueError('The source producer is still live')
    rows = json.loads(sample.read_text())['rows']
    with NOTES.open(encoding='utf-8', newline='') as stream:
        notes = list(csv.DictReader(stream, delimiter='\t'))
    if len(rows) != 64 or len(notes) != 64 or [int(n['index']) for n in notes] != list(range(64)):
        raise ValueError('All64 individual reasons required in original order')
    if (Counter(r['source_file'] for r in rows) != Counter({f: 16 for f in config['files']})
            or len({r['URL_family_sha256'] for r in rows}) != 64):
        raise ValueError('Frozen four source files and64 distinct families required')
    bound = []
    for index, (row, note) in enumerate(zip(rows, notes)):
        original = row['original_document_text']
        raw = original.encode('utf-8')
        body = row['text'].encode('utf-8')
        if (row['index'] != index or byte_sha(raw) != row['original_document_sha256']
                or byte_sha(body) != row['original_span_sha256']
                or original[row['char_start']:row['char_end']] != row['text']
                or raw[row['byte_start']:row['byte_end']] != body
                or len(original[:row['char_start']].encode('utf-8')) != row['byte_start']
                or len(original[:row['char_end']].encode('utf-8')) != row['byte_end']
                or len(body) != row['original_body_UTF8_bytes']
                or len(row['body_ids']) != row['native_body_tokens']):
            raise ValueError(f'Original parent/span or accounting changed at row{index}')
        scores = {key: int(note[key]) for key in ('grammar', 'coherence', 'complete', 'boilerplate')}
        if any(v not in (0, 1, 2) for v in scores.values()) or not note['note'].strip():
            raise ValueError('Individual rubric scores and reasons are mandatory')
        usable = (scores['grammar'] == scores['coherence'] == scores['complete'] == 2
                  and scores['boilerplate'] < 2)
        bound.append(dict(index=index, source_file=row['source_file'], source_row=row['source_row'],
            source_id=row['source_id'], URL_family_sha256=row['URL_family_sha256'],
            original_document_sha256=row['original_document_sha256'],
            original_span_sha256=row['original_span_sha256'],
            char_start=row['char_start'], char_end=row['char_end'],
            byte_start=row['byte_start'], byte_end=row['byte_end'],
            native_body_tokens=row['native_body_tokens'], original_body_UTF8_bytes=len(body),
            full_original_parent_and_retained_body_read=True, **scores, usable=usable,
            flags=note['flags'].split(','), reason=note['note']))
    usable = sum(n['usable'] for n in bound)
    contract = config['acceptance']
    passed = usable >= contract['minimum_usable'] and 64 - usable <= contract['maximum_weak']
    summary = dict(documents=64, original_parents_and_retained_bodies_read=64,
        grammar2=sum(n['grammar'] == 2 for n in bound), coherence2=sum(n['coherence'] == 2 for n in bound),
        complete2=sum(n['complete'] == 2 for n in bound),
        dominant_boilerplate=sum(n['boilerplate'] == 2 for n in bound),
        usable=usable, weak=64-usable, minimum_usable=contract['minimum_usable'],
        maximum_weak=contract['maximum_weak'], content_acceptance_passed=passed,
        rejected_indices=[n['index'] for n in bound if not n['usable']],
        issue_flags=dict(Counter(flag for n in bound for flag in n['flags'])))
    atomic_json(OUT, dict(status='unseen64_content_passed_supply_pending' if passed else 'unseen64_content_failed_fixed_extractor_branch_closed',
        created_at=now(), config_sha256=CONFIG_SHA, sample_sha256=sha256(sample),
        actual_report_sha256=sha256(ACTUAL), observations=dict(path=str(NOTES), sha256=sha256(NOTES)),
        producer_identity=job, actual_producer_absent=True,
        reviewer='Codex nonblind linguistic inspection; not independent human or learned model evaluation',
        rubric=dict(grammar='2 generally grammatical prose or legitimate structured forms;1 recurring broken constructions;0 unintelligible',
            coherence='2 connected topic/progression with locally understandable references;1 unresolved references, incompatible events or mixed fragments;0 unrelated scraps',
            complete='2 locally complete original article/abstract/entry/list;1 missing promised core content or explicit partial article;0 interrupted clause/quote',
            boilerplate='0 absent;1 local metadata/interface/advertising;2 website operation or other junk dominates',
            usable='grammar2 AND coherence2 AND complete2 AND boilerplate<2, implementing the unchanged predeclared contract; no text repair'),
        summary=summary, notes=bound, source_accepted_for_learning=False,
        fixed_extractor_branch_closed=not passed, no_outcome_resampling_or_selector_tuning=True,
        new_prepared_training_tokens=0, scientific_teacher_tokens=0, GPU_seconds=0,
        Base_complete=False, Chat_started=False, quantization_started=False,
        protected_test_bodies_read=False, CPU_seconds=time.process_time()-started,
        decision='Content screen only; measure distinct supply/protected families before training.' if passed else
            'Reject this frozen article extraction branch. Retain all64 outcomes; no reroll, post-outcome selector/threshold tuning or large training from these candidates.',
        next_action='Measure bounded unique supply and protected-family exclusions.' if passed else
            'Choose a genuinely different source-quality mechanism with a bounded completion condition before any new GPU run; do not continue old small CE/DPO/news or failed HQ extraction recipes.',
        limitations='Four eligible source groups, not a global quality rate. Nonblind ratings are not independent quality or factual certification. Near-family/fixed-suite exclusion and useful large-pool supply remain unmeasured. Original/selected exact byte checks do not prove semantic completion; individual readings supply that evidence. A failed source screen does not establish a10M model capacity limit.'))
    print(summary)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
