"""Bind the completed nonblind source reading to every original text hash."""
from collections import Counter
import csv
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.data import digest
from jmicro.experiment import ROOT, now, sha256
from jmicro.training import atomic_json

SAMPLE = Path('/home/aihub_ubuntu/jmicro-data/phase6/base-hq-sample-20261007/source-sample.json')
OBSERVATIONS = ROOT / 'reports/phase6/base_hq_source_observations.tsv'
OUT = ROOT / 'reports/phase6/base_hq_source_content_review.json'
BODY_ENDINGS = {'sentence', 'question', 'explicit_close', 'closed_quote', 'biographical_nominal', 'closed_list_item'}


def main():
    if OUT.exists(): raise ValueError('Preserve completed source review')
    start = time.monotonic()
    actual = json.loads((ROOT/'reports/phase6/base_hq_source_sample.json').read_text())
    if sha256(SAMPLE) != actual['sample']['sha256'] or actual['selected_rows'] != 64:
        raise ValueError('The unchanged original fixed64 sample is required')
    rows = json.loads(SAMPLE.read_text())['rows']
    with OBSERVATIONS.open(encoding='utf-8', newline='') as stream:
        notes = list(csv.DictReader(stream, delimiter='\t'))
    if len(notes) != 64 or [int(n['index']) for n in notes] != list(range(64)):
        raise ValueError('All64 individual notes in original source order required')
    bound = []
    for row, note in zip(rows, notes):
        if row['index'] != int(note['index']) or digest(row['text']) != row['original_text_sha256']:
            raise ValueError('Original sample index or original text changed')
        scores = {key: int(note[key]) for key in ('grammar', 'coherence', 'boilerplate')}
        if any(v not in (0,1,2) for v in scores.values()) or not note['note'].strip():
            raise ValueError('Original source rubric/individual reason required')
        bound.append(dict(index=row['index'], original_text_sha256=row['original_text_sha256'],
            source_id=row['source_id'], source_file=row['source_file'], source_row=row['source_row'],
            native_body_tokens=row['native_body_tokens'],body_UTF8_bytes=row['body_UTF8_bytes'],
            **scores,ending_type=note['ending_type'],natural_prose_body_last=note['ending_type'] in BODY_ENDINGS,
            flags=note['flags'].split(','),reason=note['note'],full_original_body_read=True))
    endings = Counter(n['ending_type'] for n in bound)
    flags = Counter(flag for n in bound for flag in n['flags'])
    summary = dict(documents=64,full_individual_original_body_read=64,
        grammar2=sum(n['grammar']==2 for n in bound),coherence2=sum(n['coherence']==2 for n in bound),
        natural_prose_body_last=sum(n['natural_prose_body_last'] for n in bound),
        boilerplate_dominant=sum(n['boilerplate']==2 for n in bound),
        terminal_kinds=dict(endings),issue_flags=dict(flags),
        natural_complete_prose_and_coherent=sum(n['natural_prose_body_last'] and n['grammar']==2 and n['coherence']==2 and n['boilerplate']<2 for n in bound))
    report = dict(status='all64_original_HQ_source_bodies_individually_read',created_at=now(),
        sample_sha256=sha256(SAMPLE),observations=dict(path=str(OBSERVATIONS),sha256=sha256(OBSERVATIONS)),
        rubric=dict(grammar='0 unintelligible;1 recurring broken constructions/extraction damage;2 generally grammatical prose or legitimate structured forms',
            coherence='0 unrelated scraps;1 incoherent entity mapping or site fragments without one body;2 connected topic and progression, including structured lists/poems/questions',
            boilerplate='0 absent;1 appended/local interface or metadata;2 operation/booking/website template dominates or a large share',
            ending='Distinguish complete prose/list/quote/question from intended bibliography/byline, empty headings, site chrome and actually truncated text. A reference/attribution is not proof of a wrong EOS label.',
            natural_prose_body_last='Last unit is original prose, purposeful question/nominal/list closure or closed quote; UI/metadata/source references are separate categories. This is target-style suitability, not a factual/overall quality benchmark.'),
        reviewer='Codex nonblind linguistic source inspection; not independent human evaluation',
        summary=summary,notes=bound,source_accepted_for_learning=False,Base_complete=False,
        prepared_training_tokens=0,scientific_teacher_tokens=0,GPU_seconds=0,protected_test_bodies_read=False,
        Chat_started=False,quantization_started=False,CPU_seconds=time.monotonic()-start,
        decision='Do not adopt unmodified HQ documents solely from the published classifier score. Many coherent bodies coexist with truncated reviews, UI/booking text, empty headings and mixed scraps. The actual fixed sample supports a bounded original-prose extraction calibration, followed by new untouched source-family acceptance and unique-supply measurement before any controlled training.',
        next_action='Calibrate one frozen structural extractor on these64 original sources only; retain exact original byte spans and punctuation, no text rewriting or invented EOS punctuation. Measure all retained unit lengths/tokens/families under CPU30s without any remote retrieval. Then evaluate a fixed unseen source sample with source-family/evaluation exclusions before preparing a large pool. Do not replay old small CE/DPO/news recipes.',
        limitations='A chosen eligible sample from four groups of one file, after known old exact/URL exclusions; not a global corpus estimate, independent seed, trained model quality or near-family protection proof. No acceptance threshold was predeclared for this HQ content review; descriptive counts are not a retrospective pass. Facts, medical/legal instructions, religious/political claims are not certified by linguistic ratings. Shared ancestry/global near overlap remain pending.')
    atomic_json(OUT,report)
    print(summary)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
