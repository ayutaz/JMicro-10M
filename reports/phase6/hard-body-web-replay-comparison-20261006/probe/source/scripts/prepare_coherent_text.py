"""Prepare a bounded, parent-protected train-only coherent-text subset with uv."""
import argparse
from collections import Counter
import json
import math
import multiprocessing as mp
import os
from pathlib import Path
import shutil
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.coherent_units import coherent_units
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer
import prepare_complete_units as old

BINS = [(32,39), (40,47), (48,55), (56,64)]


def worker_batch(batch):
    result = []
    for start, end in batch:
        text = b''.join(old._PIECES[i] for i in old._TRAIN[start+1:end].tolist()).decode('utf-8')
        for unit in coherent_units(text, old._TOK):
            result.append({**unit, 'source_start': start, 'source_end': end})
    return result


def length_bin(size):
    return next(i for i, (a,b) in enumerate(BINS) if a <= size <= b)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=12)
    parser.add_argument('--budget', type=int, default=1800)
    args = parser.parse_args()
    assert sys.version_info[:3] == (3,12,7)
    base = read_json(ROOT / 'configs/phase6/eos_5b_finish_100m.json')
    source = TrainView(base['web_shards'], base['web_manifest_sha256'])
    tokenizer = ROOT / base['tokenizer']
    output = Path('/home/aihub_ubuntu/jmicro-data/phase6/coherent-text-10b-20261004-r2')
    output.mkdir(parents=True, exist_ok=True)
    binding = dict(source_manifest_sha256=base['web_manifest_sha256'],
                   tokenizer_sha256=sha256(tokenizer),
                   selection_source_sha256=sha256(ROOT / 'src/jmicro/coherent_units.py'),
                   preparation_source_sha256=sha256(Path(__file__)),
                   old_pool_manifest_sha256=base['short_manifest_sha256'])
    if (output / 'ready.json').exists():
        ready = read_json(output / 'ready.json')
        assert ready['binding'] == binding and sha256(output / 'manifest.json') == ready['manifest_sha256']
        print(json.dumps(ready, ensure_ascii=False), flush=True)
        return
    hist = read_json(Path(base['short_pool']) / 'ready.json')['body_token_histogram']
    counts = [sum(hist[a:b+1]) for a,b in BINS]
    mean_size = sum(i*n for i,n in enumerate(hist))/sum(hist) + 2
    #30M leaves room for short-bin selection variations while staying25M–50M.
    target_docs = math.ceil(30_000_000/mean_size)
    quotas = [math.ceil(target_docs*n/sum(counts)) for n in counts]
    protected = set()
    aux = ROOT / base['reused_preparation'] / 'auxiliary-dev.json'
    protected.update(r['text_sha256'] for r in read_json(aux)['cases'])
    # Existing fixed/semantic suites are additional exact-text exclusions.
    for path in (ROOT/'eval/base.jsonl', ROOT/'eval/japanese_semantics_v2_1.jsonl'):
        for line in path.read_text().splitlines():
            row = json.loads(line)
            from jmicro.complete_units import unit_hash
            for key in ('prefix','context'):
                if row.get(key): protected.add(unit_hash(row[key]))
            for text in row.get('choices',[]): protected.add(unit_hash(text))
    started = time.monotonic()
    def check():
        if time.monotonic()-started > args.budget:
            raise TimeoutError('Bounded pool preparation exhausted; partial data not accepted')
    selected = [0]*len(BINS)
    seen, parents, samples, totals = set(), set(), [], Counter()
    read_json(output / 'manifest.json') if (output / 'manifest.json').exists() else None
    def limited_batches():
        for batch in old.batches(source, check):
            # Limit source documents to1024 body IDs to bound worker latency.
            batch = [(a,b) for a,b in batch if b-a-1 <= 1024]
            totals['source_documents_dispatched'] += len(batch)
            if batch: yield batch
    workers = min(args.workers, os.cpu_count() or 1)
    with (output/'train.partial.bin').open('wb') as stream, (output/'train.index.partial.jsonl').open('w') as index:
        with mp.get_context('fork').Pool(workers, initializer=old.worker_init,
                initargs=(str(tokenizer), str(source.directory/'train.bin'))) as pool:
            for units in pool.imap(worker_batch, limited_batches(), chunksize=2):
                check()
                for unit in units:
                    size, digest = len(unit['ids']), unit['text_sha256']
                    bucket = length_bin(size)
                    if selected[bucket] >= quotas[bucket]: continue
                    if digest in protected:
                        totals['protected_exact_excluded'] += 1
                        continue
                    if digest in seen:
                        totals['local_duplicates_excluded'] += 1
                        continue
                    seen.add(digest)
                    packed = np.asarray([2,*unit['ids'],3], dtype='<u2')
                    stream.write(packed.tobytes())
                    record = {k:v for k,v in unit.items() if k not in ('ids','text')}
                    record.update(offset=totals['tokens'], body_tokens=size,
                                  bytes=len(unit['text'].encode()), split='train', length_bin=bucket)
                    index.write(json.dumps(record, ensure_ascii=False)+'\n')
                    if len(samples) < 100: samples.append({**record, 'text':unit['text']})
                    parents.add(unit['source_start'])
                    totals.update(tokens=len(packed), documents=1, body_bytes=record['bytes'])
                    selected[bucket] += 1
                if totals['documents'] and (totals['documents']//10000 != (totals['documents']-len(units))//10000 or selected==quotas):
                    progress = dict(status='building', **binding, totals=dict(totals), selected=selected,
                                    quotas=quotas, seconds=time.monotonic()-started, updated_at=now(), pid=os.getpid())
                    write_json(output/'progress.json', progress)
                    print(json.dumps(progress), flush=True)
                if selected == quotas: break
        for handle in (stream,index):
            handle.flush(); os.fsync(handle.fileno())
    assert selected==quotas and 25_000_000 <= totals['tokens'] <= 50_000_000, (selected,quotas,totals)
    os.replace(output/'train.partial.bin', output/'train.bin')
    os.replace(output/'train.index.partial.jsonl', output/'train.index.jsonl')
    shutil.copyfile(source.directory/'token_bytes.json', output/'token_bytes.json')
    manifest = dict(version=1, dtype='<u2', kind='web', vocab_size=4096,
        tokenizer_sha256=base['tokenizer_sha256'], token_bytes_sha256=sha256(output/'token_bytes.json'),
        packing='BOS/contiguous complete2–6sentence body/EOS; selected unit ends are not original article ends',
        binding=binding, splits={'train':dict(tokens=totals['tokens'], documents=totals['documents'],
            body_bytes=totals['body_bytes'], stream_sha256=sha256(output/'train.bin'),
            index_sha256=sha256(output/'train.index.jsonl'), index_format='jsonl')})
    write_json(output/'manifest.json', manifest)
    write_json(output/'samples.json', samples)
    ready = dict(status='ready_pending_content_inspection', binding=binding, manifest_sha256=sha256(output/'manifest.json'),
                 totals=dict(totals), parent_documents=len(parents), seconds=time.monotonic()-started,
                 workers=workers, bins=BINS, selected=selected, target_proportions=[n/sum(counts) for n in counts],
                 source_train_only=True, new_unique_source_tokens=0,
                 auxiliary_dev='reuse existing protected dev; no supplemental train parent in protected dev',
                 semantic_quality='heuristic selection; sampled Codex inspection required, not independent human certification',
                 existing_full_corpus_independent_audit='incomplete; not repeated')
    write_json(output/'ready.json', ready)
    print(json.dumps({k:v for k,v in ready.items() if k!='binding'}), flush=True)


if __name__ == '__main__':
    main()
