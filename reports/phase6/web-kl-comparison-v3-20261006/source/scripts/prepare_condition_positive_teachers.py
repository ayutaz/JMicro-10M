"""Reuse original accepted train tokens; mark source-original positive outcomes."""
import hashlib
import json
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.tokenizer import Tokenizer

SOURCE = ROOT / 'reports/phase6/source-condition-pairs-v3-20261006'
OUTPUT = Path('/home/aihub_ubuntu/jmicro-data/phase6/source-condition-positive-20261006')


def outcome_token_mask(text, body_ids, tokenizer, branches):
    spans = [(len(text[:b['cut']].encode('utf-8')), len(text[:b['end']].encode('utf-8')))
             for b in branches]
    sizes = np.fromiter((len(tokenizer.decode_bytes([i])) for i in body_ids), dtype=np.int64)
    ends = np.cumsum(sizes)
    starts = ends - sizes
    if int(ends[-1]) != len(text.encode('utf-8')):
        raise ValueError('Original token byte coverage differs')
    mask = np.zeros(len(body_ids) + 2, dtype=np.uint8)
    for start, end in spans:
        if not 0 <= start < end <= int(ends[-1]):
            raise ValueError('Invalid source-original outcome byte span')
        mask[1:-1] |= ((starts < end) & (ends > start)).astype(np.uint8)
    return mask


def main():
    started = time.monotonic()
    if OUTPUT.exists():
        raise ValueError('Preserve fixed positive teacher preparation; do not overwrite')
    review = read_json(SOURCE / 'content-review.json')
    if (not review['all64_read'] or not review['paired_content_gate_passed']
            or not review['training_pool_accepted'] or review['weak_pairs'] > 10
            or review['source_pairs_sha256'] != sha256(SOURCE / 'source-pairs.json')
            or review['notes_sha256'] != sha256(SOURCE / 'content-notes.tsv')):
        raise ValueError('Accepted raw-bound fixed64 paired-target pilot required')
    config = read_json(ROOT / 'configs/phase6/story_weight_comparison.json')
    base = read_json(Path(config['original_config']['path']))
    if sha256(ROOT / base['tokenizer']) != base['tokenizer_sha256']:
        raise ValueError('Fixed Tokenizer differs')
    tokenizer = Tokenizer(ROOT / base['tokenizer'])
    view = TrainView(config['pool']['pool'], config['pool']['manifest_sha256'])
    rows = read_json(SOURCE / 'source-pairs.json')['rows']
    if len(rows) != 512 or len({r['decoded_body_sha256'] for r in rows}) != 512:
        raise ValueError('Original512 unique selected normalized bodies required')
    weak = {n['id'] for n in review['notes'] if n['weak_pair']}
    tokens = []
    focus = []
    offsets = []
    lengths = []
    metadata = []
    body_tokens = outcome_tokens = body_bytes = 0
    for row in rows:
        count = row['original_body_tokens']
        position = row['train_offset']
        ids = view.tokens[position:position + count + 2].tolist()
        body = tokenizer.decode_bytes(ids[1:-1])
        if (row['split'] != 'train' or row['source'] != 'textbook'
                or ids[0] != 2 or ids[-1] != 3 or any(i < 8 for i in ids[1:-1])
                or hashlib.sha256(body).hexdigest() != row['decoded_body_sha256']
                or body.decode('utf-8') != row['original_text']):
            raise ValueError('Actual original train document binding differs')
        for branch in row['branches']:
            if (branch['prefix'] != row['original_text'][:branch['cut']]
                    or branch['outcome'] != row['original_text'][branch['cut']:branch['end']]):
                raise ValueError('Source-original outcome span differs')
        selected = outcome_token_mask(row['original_text'], ids[1:-1], tokenizer, row['branches'])
        if row['id'] in weak:
            selected[:] = 0
        if selected[0] or selected[-1]:
            raise ValueError('BOS/EOS may not receive an artificial outcome weight')
        offsets.append(len(tokens))
        lengths.append(len(ids))
        tokens.extend(ids)
        focus.extend(selected.tolist())
        outcome_tokens += int(selected.sum())
        body_tokens += count
        body_bytes += len(body)
        metadata.append(dict(id=row['id'], original_document_index=row['document_index'],
                             original_train_offset=position, decoded_body_sha256=row['decoded_body_sha256'],
                             outcome_focus_enabled=row['id'] not in weak))
    if time.monotonic() - started > 30:
        raise TimeoutError('Bounded CPU30s positive teacher preparation exhausted')
    OUTPUT.mkdir(parents=True)
    arrays = OUTPUT / 'train.npz'
    np.savez(arrays, tokens=np.asarray(tokens, dtype='<u2'), focus=np.asarray(focus, dtype=np.uint8),
             offsets=np.asarray(offsets, dtype='<i8'), lengths=np.asarray(lengths, dtype='<i4'))
    manifest = dict(kind='original_train_positive_condition_outcome_spans', created_at=now(),
        documents=512, unique_normalized_bodies=512, original_body_tokens=body_tokens,
        original_body_bytes=body_bytes, serialized_tokens=len(tokens), EOS_targets=512,
        full_CE_targets=body_tokens + 512, outcome_focus_body_targets=outcome_tokens,
        known_weak_pilot_documents_with_focus_disabled=len(weak), focus_enabled_documents=512 - len(weak),
        source_pairs_sha256=review['source_pairs_sha256'], content_review_sha256=sha256(SOURCE / 'content-review.json'),
        original_pool_manifest_sha256=config['pool']['manifest_sha256'],
        tokenizer_sha256=base['tokenizer_sha256'], arrays_sha256=sha256(arrays),
        metadata=metadata, mask_policy='Original full-token bytes overlapping original contiguous outcome byte spans. BOS/EOS never boosted; known weak8 pilot spans disabled. All original full bodies retained as ordinary CE in both proposed arms.',
        newly_prepared_original_tokens=0, copied_existing_serialized_tokens=len(tokens),
        scientific_teacher_tokens=0, actual_GPU_seconds=0, protected_test_used=False,
        hard_negative_labels_created=0, external_fact_certification=False,
        limitations='Selected original train bytes already included in2B; repetition is learning amount, not fresh data. Only64 individually read. No global/source-family/independent near-duplicate certification. Local exact body uniqueness only; source text never retokenized or rewritten.')
    write_json(OUTPUT / 'manifest.json', manifest)
    report = dict(status='positive_condition_teacher_arrays_prepared_training_not_started',
                  created_at=now(), CPU_seconds=time.monotonic() - started, CPU_ceiling_seconds=30,
                  data_path=str(OUTPUT), manifest_sha256=sha256(OUTPUT / 'manifest.json'),
                  script_sha256=sha256(Path(__file__)), **{k: manifest[k] for k in (
                      'documents', 'original_body_tokens', 'original_body_bytes', 'serialized_tokens',
                      'full_CE_targets', 'outcome_focus_body_targets', 'focus_enabled_documents',
                      'newly_prepared_original_tokens', 'scientific_teacher_tokens', 'actual_GPU_seconds',
                      'hard_negative_labels_created', 'protected_test_used')},
                  Base_adopted=False, next_action='Implement matched ordinary CE versus normalized positive-outcome weighted CE on the identical data stream, preserve original body+EOS supervision and counters, then CPU full-state resume and measured CUDA probe before freezing science.')
    write_json(ROOT / 'reports/phase6/source_condition_positive_preparation.json', report)
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
