"""Bounded real-source access/geometry measurement; no13GB corpus rescan."""
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1]/'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from natural_context_contrast_corpus import OriginalTrainCorpusSampler

OUT = ROOT/'reports/phase6/natural_context_contrast_corpus_preparation.json'
OLD = ROOT/'reports/phase6/natural_context_contrast_preparation.json'


def main():
    if OUT.exists():
        raise ValueError('Preserve bounded real source measurement; no reroll')
    started = time.monotonic()
    old = json.loads(OLD.read_text())
    review_path = ROOT/'reports/phase6/textbook_mixture_content_review.json'
    if sha256(review_path) != old['accepted_source_review_sha256']:
        raise ValueError('Previously accepted original source review changed')
    tokenizer_path = ROOT/'artifacts/phase2/4096/tokenizer.model'
    if sha256(tokenizer_path) != old['tokenizer_sha256']:
        raise ValueError('Original pinned Tokenizer differs')
    source = OriginalTrainCorpusSampler(old['pool'], old['manifest_sha256'], Tokenizer(tokenizer_path),
        dict(web=75000000, textbook=20000000, story=5000000), seed=42)
    if (source.binding['stream_size'], source.binding['stream_mtime_ns']) != (
            old['train_stream_bytes'], old['train_stream_mtime_ns']):
        raise ValueError('Already accepted original TRAIN stream identity differs')
    summaries = []
    trace = []
    for _ in range(8):
        if time.monotonic()-started > 30:
            raise TimeoutError('Source access/geometry CPU30s exhausted')
        begin = time.monotonic()
        rows = source.take(128)
        summaries.append(dict(windows=len(rows), CPU_seconds=time.monotonic()-begin,
            CE_targets=sum(r['teacher_tokens'] for r in rows),
            CE_inputs=sum(len(r['input_ids']) for r in rows),
            max_CE_input=max(len(r['input_ids']) for r in rows),
            original_EOS=sum(r['original_EOS_targets'] for r in rows),
            eligible_first_window_pairs=sum(bool(r['prefix_ids']) for r in rows)))
        trace.extend(dict(index_byte_position=r['index_byte_position'],
            index_record_sha256=r['index_record_sha256'], source=r['source'],
            source_family=r['source_family'], body_sha256=r['full_original_body_sha256'],
            original_body_tokens=r['original_body_tokens'], input_start=r['input_start'],
            target_first=r['target_first'], target_end=r['target_end'],
            CE_input_tokens=len(r['input_ids']), teacher_tokens=r['teacher_tokens']) for r in rows)
    report = dict(status='bounded_original_full_corpus_sampler_CPU_measurement_complete', created_at=now(),
        previous_preparation=dict(path=str(OLD), sha256=sha256(OLD)),
        source_binding=source.binding, tokenizer_sha256=sha256(tokenizer_path),
        source_sha256={name: sha256(ROOT/name) for name in (
            'scripts/natural_context_contrast_corpus.py','scripts/prepare_natural_context_contrast_corpus.py')},
        fixed_seed=42, summaries=summaries, trace=trace,
        windows_measured=sum(s['windows'] for s in summaries),
        CE_targets_inspected=sum(s['CE_targets'] for s in summaries),
        maximum_CE_input=max(s['max_CE_input'] for s in summaries),
        sampler_documents_drawn=source.documents_drawn, index_records_bounded_decoded=source.draws,
        genre_teacher_progress=source.consumed, auxiliary_eligibility_reasons=dict(source.auxiliary_reasons),
        CPU_seconds=time.monotonic()-started, old_index_or_stream_full_scan=False,
        membership='Only bounded records from accepted TRAIN index and their original token slices; DEV/TEST not opened',
        sampling_policy='Within requested genre, random index-byte draw is record-byte weighted, not uniform documents. Exact teacher quotas Web75/textbook20/story5; same sampler and seed in both arms. Long units get document-local1024/stride512 windows, all original body+EOS targets exactly once per draw except final genre budget masks.',
        scientific_teacher_tokens=0, optimizer_updates=0, GPU_seconds=0, Base_complete=False,
        Chat_started=False, quantization_started=False,
        next_action='Freeze and run one actual real-corpus finite capacity/throughput/4-vs2+2 full-state probe, retaining long-unit/source/auxiliary accounting. Implement long-job runner and freeze scientific budget only after passed actual measurements.',
        limitations='CPU membership/geometry/access speed is not GPU throughput, new dataset supply, content reacceptance or model quality. Repeated draws are training exposures, not new unique documents. Historical broad source acceptance and all Base quality gates unchanged.')
    atomic_json(OUT, report)
    print(json.dumps({k: report[k] for k in ('windows_measured','CE_targets_inspected','maximum_CE_input',
                                            'sampler_documents_drawn','CPU_seconds')}))


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
