"""Bounded real-train comparison; never change the completed production export."""
from concurrent.futures import ProcessPoolExecutor
import hashlib
import json
from pathlib import Path
import signal
import sqlite3
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[2]/'src'))
from jmicro.corpus_state import read_json, write_json
from jmicro.experiment import ROOT, now, sha256
from jmicro.expanded_data import bounded_map
from jmicro.large_corpus import tokenize_batch

OUTPUT = Path('/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2')
DESTINATION = ROOT/'reports/phase6/corpus-export-speed-probe-20261003'
RECORDS = 262144


def packetize(task):
    encoded = tokenize_batch(task)
    corpus = b''.join((json.dumps(row, ensure_ascii=False)+'\n').encode() for row, _, _ in encoded)
    tokens = b''.join(ids for _, ids, _ in encoded)
    metadata = [(row['doc_id'], row['bucket'], row['canonical_sha256'], length, len(row['text'].encode()))
                for row, _, length in encoded]
    return corpus, tokens, metadata


def run(rows, tokenizer, method, attempt):
    directory = DESTINATION/f'{method}-{attempt}'
    directory.mkdir(parents=True, exist_ok=False)
    size = 128 if method == 'original' else 512
    tasks = ((rows[i:i+size], tokenizer) for i in range(0, len(rows), size))
    started = time.monotonic()
    tokens = documents = body_bytes = 0
    with (directory/'corpus.jsonl').open('wb') as corpus, (directory/'train.bin').open('wb') as stream, \
            (directory/'train.index.json').open('w', encoding='utf-8') as index:
        index.write('[\n')
        with ProcessPoolExecutor(max_workers=16) as executor:
            for batch in bounded_map(executor, tokenize_batch if method == 'original' else packetize, tasks, 32):
                if method == 'original':
                    metadata = []
                    for row, ids, length in batch:
                        corpus.write((json.dumps(row, ensure_ascii=False)+'\n').encode())
                        stream.write(ids)
                        metadata.append((row['doc_id'], row['bucket'], row['canonical_sha256'], length, len(row['text'].encode())))
                else:
                    corpus_bytes, token_bytes, metadata = batch
                    corpus.write(corpus_bytes)
                    stream.write(token_bytes)
                for doc_id, bucket, canonical, length, byte_count in metadata:
                    value = dict(doc_id=doc_id, split='train', kind='web', bucket=bucket,
                                 canonical_sha256=canonical, offset=tokens, body_tokens=length, bytes=byte_count)
                    if documents:
                        index.write(',\n')
                    index.write(json.dumps(value, ensure_ascii=False))
                    tokens += length+2
                    documents += 1
                    body_bytes += byte_count
        index.write('\n]\n')
    seconds = time.monotonic()-started
    result = dict(method=method, attempt=attempt, workers=16, batch_records=size, seconds=seconds,
                  tokens=tokens, documents=documents, body_bytes=body_bytes,
                  hashes={name: sha256(directory/name) for name in ('corpus.jsonl', 'train.bin', 'train.index.json')})
    print(json.dumps(result), flush=True)
    return result


def main():
    started = time.monotonic()
    signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError('180second probe budget exhausted')))
    signal.alarm(180)
    built = read_json(OUTPUT/'manifest.json')
    db = sqlite3.connect(f'file:{OUTPUT/"records.sqlite"}?mode=ro', uri=True)
    settings = {name: db.execute(f'PRAGMA {name}').fetchone()[0]
                for name in ('cache_size', 'mmap_size', 'page_size', 'page_count')}
    db.close()
    rows = []
    ids = hashlib.sha256()
    with (Path(built['artifact_directory'])/'corpus.jsonl').open(encoding='utf-8') as source:
        for line in source:
            row = json.loads(line)
            if row['split'] != 'train':
                continue
            rows.append(row)
            ids.update((row['doc_id']+'\n').encode())
            if len(rows) == RECORDS:
                break
    if len(rows) != RECORDS:
        raise ValueError('Fixed real-train sample unavailable')
    tokenizer = str(ROOT/'artifacts/phase2/4096/tokenizer.model')
    measurements = [run(rows, tokenizer, method, attempt)
                    for method, attempt in [('original', 1), ('packetized', 1), ('packetized', 2), ('original', 2)]]
    for key in ('hashes', 'tokens', 'documents', 'body_bytes'):
        if any(m[key] != measurements[0][key] for m in measurements):
            raise ValueError(f'Complete sample export differs: {key}')
    speedups = [measurements[0]['seconds']/measurements[1]['seconds'],
                measurements[3]['seconds']/measurements[2]['seconds']]
    report = dict(status='passed_all_real_sample_export_bytes', completed_at=now(), records=RECORDS,
                  fixed_train_ids_sha256=ids.hexdigest(), measurements=measurements, speedups=speedups,
                  preset_minimum_speedup=1.2, measured_gate_passed=all(s >= 1.2 for s in speedups),
                  observed_default_read_connection=settings, sqlite_version=sqlite3.sqlite_version,
                  source_sha256=sha256(Path(__file__)), manifest_sha256=sha256(OUTPUT/'manifest.json'),
                  elapsed_seconds=time.monotonic()-started, runtime_budget_seconds=180,
                  active_pipeline_changed=False, full_corpus_validated_by_probe=False,
                  scope='Train-only fixed sample; same Tokenizer and all corpus/token/index bytes; ABBA ordering; no global cache flush')
    write_json(ROOT/'reports/phase6/corpus_10b_export_speed_probe.json', report)
    signal.alarm(0)


if __name__ == '__main__':
    main()
