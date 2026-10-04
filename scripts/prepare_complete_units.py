"""Bounded train-only complete-unit extraction and frozen dev diagnostics."""
import json
import multiprocessing as mp
import os
from pathlib import Path
import shutil
import signal
import time

import numpy as np

from jmicro.complete_units import complete_units, unit_hash
from jmicro.eos_pilot import TrainView, spans
from jmicro.experiment import read_json, write_json, sha256
from jmicro.tokenizer import Tokenizer

_TOK, _TRAIN, _PIECES = None, None, None


def worker_init(tokenizer, train_file):
    global _TOK, _TRAIN, _PIECES
    # Pool.terminate must kill idle workers even when the parent handles SIGTERM cooperatively.
    signal.signal(signal.SIGTERM, signal.SIG_DFL)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    _TOK = Tokenizer(tokenizer)
    _TRAIN = np.memmap(train_file, dtype='<u2', mode='r')
    _PIECES = [_TOK.decode_bytes([i]) if i != 1 else b'' for i in range(_TOK.vocab_size)]


def worker_batch(batch):
    results = []
    for start, end in batch:
        text = b''.join(_PIECES[i] for i in _TRAIN[start + 1:end].tolist()).decode('utf-8')
        for unit in complete_units(text, _TOK):
            results.append({**unit, 'source_start': start, 'source_end': end})
    return results


def batches(view, check):
    previous, batch = -1, []
    for offset in range(0, len(view.tokens), 4_000_000):
        check()
        starts, ends, previous = spans(view.tokens[offset:offset + 4_000_000], offset, previous)
        for start, end in zip(starts, ends):
            if 32 <= end - start - 1 <= 4096:
                batch.append((int(start), int(end)))
                if len(batch) == 32:
                    yield batch
                    batch = []
    if batch:
        yield batch


def prepare_auxiliary(plan, dev, tok, output):
    path = output / 'auxiliary-dev.json'
    if path.exists():
        result = read_json(path)
        assert result['definition'] == plan['short_selection'] and result['dev_manifest_sha256'] == sha256(dev.directory / 'manifest.json')
        return result
    cases, seen = [], set()
    for doc in dev.index:
        start, count = doc['offset'], doc['body_tokens']
        text = tok.decode_bytes(dev.tokens[start + 1:start + count + 1].tolist()).decode('utf-8')
        for unit in complete_units(text, tok):
            if unit['text_sha256'] in seen:
                continue
            seen.add(unit['text_sha256'])
            # Prefix ends at a character boundary, not inside a UTF-8 token sequence.
            prefix = unit['text'][:max(1, len(unit['text']) // 3)]
            prefix_ids = tok.encode(prefix)
            if not 1 <= len(prefix_ids) <= 24:
                continue
            cases.append({'id': f'aux-short-{len(cases):03d}', 'category': 'complete-dev-unit',
                          'split': 'dev', 'source_doc_id': doc['doc_id'],
                          'source_offset': start, 'char_start': unit['char_start'], 'char_end': unit['char_end'],
                          'text': unit['text'], 'text_sha256': unit['text_sha256'],
                          'body_ids': unit['ids'], 'prefix': prefix, 'prefix_ids': prefix_ids,
                          'reference_continuation': unit['text'][len(prefix):]})
            if len(cases) == 80:
                break
        if len(cases) == 80:
            break
    assert len(cases) == 80
    result = {'status': 'frozen_before_training', 'split': 'dev', 'test_used': False,
              'definition': plan['short_selection'], 'dev_manifest_sha256': sha256(dev.directory / 'manifest.json'),
              'cases': cases, 'metric_scope': 'Supplementary diagnostics; does not replace fixed80 or its gate'}
    write_json(path, result)
    return result


def prepare_pool(plan, tok, auxiliary, heartbeat, check):
    output = Path(plan['short_pool'])
    output.mkdir(parents=True, exist_ok=True)
    protected = {c['text_sha256'] for c in auxiliary['cases']}
    aux_sha = sha256(Path(plan['output']) / 'auxiliary-dev.json')
    ready_path = output / 'ready.json'
    if ready_path.exists():
        ready = read_json(ready_path)
        assert ready['selection'] == plan['short_selection'] and ready['auxiliary_sha256'] == aux_sha
        assert ready['source_manifest_sha256'] == plan['web_manifest_sha256']
        assert sha256(output / 'manifest.json') == ready['manifest_sha256']
        return ready
    started = time.monotonic()
    web = TrainView(plan['web_shards'], plan['web_manifest_sha256'])
    seen, parents, samples = set(), set(), []
    lengths = np.zeros(65, dtype=np.int64)
    count = total = body_bytes = duplicates = protected_excluded = 0
    temporary, index_tmp = output / 'train.partial.bin', output / 'train.index.partial.jsonl'
    workers = min(plan['prepare_workers'], os.cpu_count() or 1)
    with temporary.open('wb') as stream, index_tmp.open('w', encoding='utf-8') as index:
        with mp.get_context('fork').Pool(workers, initializer=worker_init,
                initargs=(str(tok.path) if hasattr(tok, 'path') else plan['tokenizer'], str(web.directory / 'train.bin'))) as pool:
            for units in pool.imap(worker_batch, batches(web, check), chunksize=1):
                check()
                if time.monotonic() - started > plan['prepare_budget_seconds']:
                    write_json(output / 'partial.json', {'status': 'budget_exhausted', 'tokens': total,
                        'documents': count, 'seconds': time.monotonic() - started,
                        'restart_policy': 'Preserve partial files; no training with insufficient pool'})
                    raise TimeoutError('Complete-unit pool preparation budget exhausted')
                for unit in units:
                    digest = unit['text_sha256']
                    if digest in protected:
                        protected_excluded += 1
                        continue
                    if digest in seen:
                        duplicates += 1
                        continue
                    seen.add(digest)
                    size = len(unit['ids'])
                    raw_bytes = len(unit['text'].encode('utf-8'))
                    assert 32 <= size <= 64 and all(i >= 8 for i in unit['ids'])
                    stream.write(np.asarray([2, *unit['ids'], 3], dtype='<u2').tobytes())
                    record = {k: v for k, v in unit.items() if k not in ('ids', 'text')}
                    index.write(json.dumps({**record, 'offset': total, 'body_tokens': size,
                                           'bytes': raw_bytes, 'split': 'train'}, ensure_ascii=False) + '\n')
                    if len(samples) < 16:
                        samples.append({**record, 'text': unit['text'], 'body_tokens': size})
                    parents.add(unit['source_start'])
                    count += 1
                    total += size + 2
                    body_bytes += raw_bytes
                    lengths[size] += 1
                    if total >= plan['short_pool_minimum_tokens']:
                        break
                if count and (count // 5000 != (count - len(units)) // 5000 or total >= plan['short_pool_minimum_tokens']):
                    heartbeat('complete-unit-pool', pool_units=count, pool_tokens=total,
                              parent_documents=len(parents), extraction_seconds=time.monotonic() - started)
                if total >= plan['short_pool_minimum_tokens']:
                    break
        for handle in (stream, index):
            handle.flush()
            os.fsync(handle.fileno())
    if total < plan['short_pool_minimum_tokens']:
        write_json(output / 'partial.json', {'status': 'insufficient_pool', 'tokens': total, 'documents': count})
        raise ValueError('Complete-unit pool smaller than frozen minimum; no training launched')
    os.replace(temporary, output / 'train.bin')
    os.replace(index_tmp, output / 'train.index.jsonl')
    shutil.copyfile(web.directory / 'token_bytes.json', output / 'token_bytes.json')
    manifest = {'version': 1, 'dtype': '<u2', 'kind': 'web', 'vocab_size': tok.vocab_size,
        'tokenizer_sha256': plan['tokenizer_sha256'], 'token_bytes_sha256': sha256(output / 'token_bytes.json'),
        'packing': 'BOS/complete sentence-unit body/EOS; units define new record ends, not original article EOS',
        'source_manifest_sha256': plan['web_manifest_sha256'], 'selection': plan['short_selection'],
        'auxiliary_sha256': aux_sha,
        'splits': {'train': {'tokens': total, 'documents': count, 'body_bytes': body_bytes,
                            'stream_sha256': sha256(output / 'train.bin'),
                            'index_sha256': sha256(output / 'train.index.jsonl'), 'index_format': 'jsonl'}}}
    write_json(output / 'manifest.json', manifest)
    ready = {'status': 'ready_train_only_complete_units', 'source_manifest_sha256': plan['web_manifest_sha256'],
        'manifest_sha256': sha256(output / 'manifest.json'), 'auxiliary_sha256': aux_sha,
        'selection': plan['short_selection'], 'documents': count, 'tokens': total,
        'parent_documents': len(parents), 'duplicates_removed': duplicates, 'protected_units_excluded': protected_excluded,
        'body_token_histogram': lengths.tolist(), 'body_tokens_mean': float(np.dot(lengths, np.arange(65)) / count),
        'seconds': time.monotonic() - started, 'workers': workers, 'samples': samples, 'heldout_used': False,
        'content_limit': 'Conservative complete sentence boundaries; semantic quality is not certified by blind human review'}
    assert ready['seconds'] <= plan['prepare_budget_seconds']
    write_json(ready_path, ready)
    return ready
