"""Replay only the first committed TRAIN batch and retain six exposed windows."""
import hashlib
import json
from pathlib import Path
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from base_kv_allocation_trainer import CEOnlyOriginalSampler

PHASE = ROOT / 'reports/phase6'
PROPOSAL = PHASE / 'base_residual_seen_train_diagnostic_proposal.json'
OUTPUT = PHASE / 'base_residual_seen_train_preparation.json'


def main():
    start = time.perf_counter()
    if OUTPUT.exists():
        raise ValueError('Preserve actual exposure preparation')
    proposal = read_json(PROPOSAL)
    config_path = ROOT / 'configs/phase6/base_parallel_residual_comparison.json'
    c = read_json(config_path)
    if proposal['comparison_config_sha256'] != sha256(config_path):
        raise ValueError('Exact completed science config required')
    for name in ('scripts/base_kv_allocation_trainer.py', 'scripts/natural_context_contrast_corpus.py', 'src/jmicro/tokenizer.py'):
        if sha256(ROOT / name) != c['source_sha256'][name]:
            raise ValueError('Original sampler/codec source changed')
    completed = read_json(PHASE / 'base_parallel_residual_comparison_completion.json')
    if not completed['fixed_parallel_residual_condition_closed'] or completed['Base_complete']:
        raise ValueError('Closed failed recipe required; this is a separate read-only diagnostic')
    codec = Tokenizer(ROOT / c['tokenizer'])
    sampler = CEOnlyOriginalSampler(c['source_binding']['pool'], c['source_binding']['manifest_sha256'], codec, c['goals'])
    try:
        if sampler.binding != c['source_binding']:
            raise ValueError('Accepted source identity changed')
        rows = sampler.take(c['batch'])
    finally:
        sampler.handle.close()
    run = PHASE / 'base-parallel-residual-comparison-20261007'
    history_path, history = None, None
    for path in sorted((run / 'sequential').glob('metrics-*.jsonl')):
        with path.open() as handle:
            first = json.loads(handle.readline())
        if first['update'] == 1:
            if history is not None:
                raise ValueError('Ambiguous first committed update; inspect instead of selecting')
            history_path, history = path, first
    if history is None:
        raise ValueError('Actual first committed history missing')
    stream = json.dumps([(r['index_byte_position'], r['index_record_sha256'], r['input_ids'], r['target_ids']) for r in rows]).encode()
    digest = hashlib.sha256(bytes(32) + stream).hexdigest()
    trace = [list((r['index_byte_position'], r['index_record_sha256'], r['target_first'], r['target_end'], r['teacher_tokens'])) for r in rows]
    if (digest != history['token_digest'] or trace != history['draw_trace']
            or sum(r['teacher_tokens'] for r in rows) != history['CE_targets_this_update']
            or len(rows) != history['original_windows_this_update']):
        raise ValueError('Reconstructed batch differs from actual committed TRAIN exposure')
    # Fixed first two distinct first-window bodies per source, no selection
    # using loss, generated text or content quality. No additional draws.
    selected, seen = [], {g: set() for g in c['goals']}
    for row in rows:
        genre, body_sha = row['source'], row['full_original_body_sha256']
        if not row['original_document_first_window'] or body_sha in seen[genre] or len(seen[genre]) == 2:
            continue
        seen[genre].add(body_sha)
        gold = [n for n in row['target_ids'] if n != -100]
        if row['input_start'] != 0 or row['input_ids'][0] != 2 or row['target_first'] != 1:
            raise ValueError('Only actual whole-document first windows required')
        serialized = row['input_ids'] + [gold[-1]]
        if serialized[1:] != gold:
            raise ValueError('Actual original next-token shift differs')
        body = gold[:-1] if gold[-1] == 3 else gold
        # A token boundary may split UTF8. Retain raw IDs and report that
        # fact; the replacement display is never claimed as canonical bytes.
        raw = codec.decode_bytes(body)
        try:
            text = raw.decode('utf-8')
            valid_utf8 = True
        except UnicodeDecodeError:
            text, valid_utf8 = raw.decode('utf-8', errors='replace'), False
        cut = None
        for n in range(24, min(48, len(body) - 1) + 1):
            try:
                prefix = codec.decode_bytes(body[:n]).decode('utf-8')
            except UnicodeDecodeError:
                continue
            if codec.encode(prefix) == body[:n]:
                cut = n
                break
        if cut is None:
            raise ValueError('Fixed selected window lacks a stable24–48-token UTF8 prefix; no reroll')
        selected.append(dict(id=f"seen-{genre}-{len(seen[genre]):02d}", source=genre,
            index_byte_position=row['index_byte_position'], index_record_sha256=row['index_record_sha256'],
            full_original_body_sha256=body_sha, source_family=row['source_family'],
            original_body_tokens=row['original_body_tokens'], input_ids=row['input_ids'], gold_targets=row['target_ids'],
            teacher_tokens=row['teacher_tokens'], first_window_has_actual_gold_EOS=gold[-1] == 3,
            original_body_first_window_text=text, first_window_UTF8_valid=valid_utf8,
            actual_first_window_body_bytes_hex=raw.hex(), prefix=prefix, prefix_body_tokens=cut,
            prompt_ids=[2] + body[:cut], continuation_gold_ids=gold[cut:],
            actually_consumed_at_update=1, first_update_teacher_digest=digest))
    if len(selected) != 6 or any(len(v) != 2 for v in seen.values()):
        raise ValueError('First batch lacks fixed two unique bodies per source; record blocker, no new draws')
    elapsed = time.perf_counter() - start
    if elapsed > proposal['CPU_preparation_budget_seconds']:
        raise ValueError('Bounded CPU preparation exhausted')
    result = dict(status='six_actual_first_update_TRAIN_windows_bound_no_model_evaluation', created_at=now(),
        proposal_sha256=sha256(PROPOSAL), source_sha256=sha256(Path(__file__)), CPU_seconds=elapsed,
        first_committed_history=dict(path=str(history_path), first_line_sha256=hashlib.sha256(json.dumps(history, sort_keys=True).encode()).hexdigest(), update=1),
        original_stream_digest=digest, all80_first_draw_trace_exact=True, original_next_token_alignment_verified=True,
        selected=selected, first_batch_original_teachers=history['CE_targets_this_update'],
        TRAIN_exposure_verified=True, fresh_mixture_genuine_quality_certified=False,
        GPU_seconds=0, scientific_teacher_tokens=0, generated_tokens=0, optimizer_updates=0,
        Base_complete=False, Base_adopted=False, Chat_started=False, quantization_started=False,
        limits='First two distinct first-window bodies per source in the actual first update only. This proves exposure, not repeated memorization, diversity, generalization or current model quality. No unconsumed heldout claim; no checkpoint or full-corpus rehash.')
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(dict(status=result['status'], CPU_seconds=elapsed, first_batch_teachers=result['first_batch_original_teachers'],
                         selected=[dict(id=r['id'], body_tokens=r['original_body_tokens'], gold_EOS=r['first_window_has_actual_gold_EOS']) for r in selected])))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
