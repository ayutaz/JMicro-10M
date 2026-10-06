"""Bounded, fixed TRAIN-candidate source inspection; no learning or acceptance."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import sqlite3
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import pyarrow.parquet as pq
from jmicro.data import digest, normalized, url_key
from jmicro.experiment import ROOT, now, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from remote_parquet_ranges import RangeBudget, RangeFile, observed_size

OUT = ROOT / 'reports/phase6/base_hq_source_sample.json'
DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/base-hq-sample-20261007')
DB = Path('/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/records.sqlite')
TOKENIZER = ROOT / 'artifacts/phase2/4096/tokenizer.model'
TOKENIZER_SHA = 'a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'
SEED = 2026100723
COLUMNS = ['text', 'id', 'url', 'quality_score']


def main():
    if OUT.exists() or DATA.exists():
        raise ValueError('Preserve frozen sample; no reroll')
    start = time.monotonic(); cpu = time.process_time()
    if sha256(TOKENIZER) != TOKENIZER_SHA:
        raise ValueError('Fixed tokenizer hash required')
    tok = Tokenizer(TOKENIZER)
    source = ROOT / 'reports/phase6/base_hq_source_feasibility.json'
    footer = ROOT / 'reports/phase6/base_hq_footer_inspection.json'
    binding = json.loads(source.read_text()); inspected = json.loads(footer.read_text())
    if inspected['source_sha256'] != sha256(source):
        raise ValueError('Actual pinned footer/source binding changed')
    rng = random.Random(SEED)
    groups = sorted(rng.sample(range(len(inspected['row_groups'])), 4))
    expected_bytes = sum(c['compressed_bytes'] for g in groups for c in inspected['row_groups'][g]['columns'] if c['path'] in COLUMNS)
    if expected_bytes > 90 * 1024 * 1024:
        raise ValueError('Frozen group columns cannot fit bounded retrieval')
    DATA.mkdir(parents=True)
    plan = dict(created_at=now(), source_sha256=sha256(source), footer_sha256=sha256(footer),
        repository=binding['repository'], revision=binding['revision'], file=binding['first_file'],
        seed=SEED, groups=groups, rows_per_group=16, columns=COLUMNS, expected_compressed_column_bytes=expected_bytes,
        wall_limit_seconds=60, CPU_limit_seconds=30, remote_byte_limit=100*1024*1024,
        selection='Four uniform row groups of the previously pinned first Japanese file. Fixed row shuffle per group; first16 unique source ID/URL families assigned TRAIN by URL hash modulo1000<900 and absent from all existing indexed exact/URL entries. No text quality/length/score filter or result reroll.',
        limitations='One source file/dump; source inspection, not globally independent or accepted training data. Old-family near duplicates and fixed suite exclusions must be handled before learning.')
    atomic_json(DATA / 'plan.json', plan)
    budget = RangeBudget(100*1024*1024, max(.1, 60-(time.monotonic()-start)))
    size = observed_size(binding['Content_Range'])
    url = f"https://huggingface.co/datasets/{binding['repository']}/resolve/{binding['revision']}/{binding['first_file']}"
    counts = Counter(); selected = []; seen = set(); decoded = 0
    try:
        # Existing exact/hash and URL indexes include protected records. Query only
        # keys/IDs, never protected payloads/bodies and never scan the old corpus.
        with sqlite3.connect(f'file:{DB}?mode=ro', uri=True) as db, RangeFile(url, size, budget) as stream:
            db.execute('PRAGMA query_only=ON')
            states = dict(db.execute('SELECT key,value FROM state'))
            parquet = pq.ParquetFile(stream, pre_buffer=False)
            if parquet.metadata.num_rows != inspected['rows']:
                raise ValueError('Pinned Parquet row count differs')
            offsets = [sum(g['rows'] for g in inspected['row_groups'][:i]) for i in groups]
            for group, offset in zip(groups, offsets):
                rows = parquet.read_row_group(group, columns=COLUMNS, use_threads=False).to_pylist()
                decoded += len(rows); order = list(range(len(rows))); rng.shuffle(order)
                accepted = 0
                for row_number in order:
                    if time.monotonic()-start > 60 or time.process_time()-cpu > 30:
                        raise TimeoutError('Bounded sample wall/CPU deadline exhausted')
                    counts['candidates_inspected'] += 1
                    row = rows[row_number]; text = row['text']; key = url_key(row['url'] or '')
                    if not text or not row['id'] or not key:
                        counts['missing_source'] += 1; continue
                    if int(hashlib.sha256(key.encode()).hexdigest()[:16], 16) % 1000 >= 900:
                        counts['new_URL_family_holdout'] += 1; continue
                    if row['id'] in seen or key in seen:
                        counts['local_family_duplicate'] += 1; continue
                    normhash = digest(normalized(text))
                    if db.execute('SELECT id FROM exact WHERE hash=?', (normhash,)).fetchone():
                        counts['existing_exact_excluded'] += 1; continue
                    if db.execute('SELECT id FROM urls WHERE url=?', (key,)).fetchone():
                        counts['existing_URL_excluded'] += 1; continue
                    tokens = tok.encode(text)
                    selected.append(dict(index=len(selected), source_id=row['id'], source_file=binding['first_file'],
                        source_row=offset+row_number, row_group=group, URL=row['url'], URL_key=key,
                        URL_family_sha256=hashlib.sha256(key.encode()).hexdigest(), split='TRAIN_candidate_only',
                        quality_score=row['quality_score'], text=text, original_text_sha256=digest(text),
                        normalized_text_sha256=normhash, native_body_tokens=len(tokens), body_UTF8_bytes=len(text.encode('utf-8'))))
                    seen.update((row['id'], key)); accepted += 1
                    if accepted == 16: break
                if accepted != 16:
                    raise ValueError('Frozen source group lacks16 eligible inspection rows')
            samples = DATA / 'source-sample.json'; atomic_json(samples, dict(rows=selected))
            ranges = []
            for index, (offset, content) in enumerate(stream.cache):
                path = DATA / f'range-{index:03d}-{offset}.bin'; path.write_bytes(content)
                ranges.append(dict(offset=offset, bytes=len(content), path=str(path), sha256=sha256(path)))
            values = [r['native_body_tokens'] for r in selected]
            mean = sum(values)/len(values)
            report = dict(status='fixed64_TRAIN_candidate_source_sample_unreviewed', created_at=now(),
                plan=dict(path=str(DATA/'plan.json'), sha256=sha256(DATA/'plan.json')),
                sample=dict(path=str(samples),sha256=sha256(samples)),
                source_sha256=sha256(source), footer_sha256=sha256(footer),
                repository=binding['repository'],revision=binding['revision'],source_file=binding['first_file'],
                seed=SEED,groups=groups,selected_rows=len(selected),decoded_column_rows=decoded,
                exclusions=dict(counts),existing_registry=str(DB), existing_registry_state=states,
                existing_exact_and_URL_lookup_only=True,old_corpus_scan=False,protected_test_bodies_read=False,
                tokenizer_sha256=TOKENIZER_SHA,body_tokens_in_inspection=sum(values),
                body_bytes_in_inspection=sum(r['body_UTF8_bytes'] for r in selected),
                native_body_tokens_min=min(values),native_body_tokens_max=max(values),native_body_tokens_mean=mean,
                first_file_gross_token_extrapolation=mean*inspected['rows'],
                extrapolation_limit='Mean of64 eligible URL families in four groups of one file; selected rather than all rows, no correction for old overlap/quality/split/near duplicates. Not accepted unique supply or a representative global corpus estimate.',
                remote_bytes=budget.bytes,HTTP_range_requests=budget.requests,range_evidence=ranges,
                wall_seconds=time.monotonic()-start,CPU_seconds=time.process_time()-cpu,
                embedding_column_requested=False,prepared_training_tokens=0,scientific_teacher_tokens=0,GPU_seconds=0,
                Base_complete=False,Chat_started=False,quantization_started=False,source_accepted=False,
                next_action='Inspect all64 fixed source bodies with original byte-bound notes, record natural paragraph/document completion and boilerplate/repetition. Do not reroll. Define protected family exclusion and supply bound only if this source is suitable; no training from this sample and no old failed CE/DPO recipe rescue.')
        if report['wall_seconds'] > 60 or report['CPU_seconds'] > 30:
            raise TimeoutError('Final bounded inspection deadline exceeded')
    except Exception as error:
        atomic_json(DATA/'partial-source-sample.json',dict(rows=selected))
        atomic_json(OUT,dict(status='fixed_sample_failure_preserved',error_type=type(error).__name__,
            wall_seconds=time.monotonic()-start,CPU_seconds=time.process_time()-cpu,remote_bytes=budget.bytes,
            HTTP_range_requests=budget.requests,selected_rows=len(selected),exclusions=dict(counts),
            plan_path=str(DATA/'plan.json'),source_accepted=False,prepared_training_tokens=0,GPU_seconds=0,
            next_action='Inspect preserved bounded failure; no identical retry, source reroll or unbounded full-file download.'))
        raise RuntimeError('Bounded source inspection failed; original evidence preserved') from None
    atomic_json(OUT,report)
    print({k:report[k] for k in ('status','selected_rows','body_tokens_in_inspection','remote_bytes','wall_seconds','CPU_seconds')})


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
