"""Fixed unseen-source acceptance sample, original bodies and strict HTTP ranges."""
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import random
import re
import sqlite3
import sys
import time
import urllib.request

sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import pyarrow.parquet as pq
from base_hq_article_body import select_article
from jmicro.data import digest,normalized,url_key
from jmicro.experiment import ROOT,now,sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from remote_parquet_ranges import RangeBudget,RangeFile

CONFIG=ROOT/'configs/phase6/base_hq_acceptance.json'
OUT=ROOT/'reports/phase6/base_hq_acceptance_sample.json'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/base-hq-acceptance-20261007')
COLUMNS=['text','id','url','quality_score']


def probe_size(url,budget):
    remaining=budget.deadline-time.monotonic()
    if remaining<=0 or budget.bytes+4>budget.maximum_bytes:
        raise TimeoutError('Source header budget exhausted')
    request=urllib.request.Request(url,headers={'Range':'bytes=0-3','User-Agent':'JMicro-10M bounded public source acceptance'})
    budget.requests+=1
    with urllib.request.urlopen(request,timeout=min(15,remaining)) as response:
        match=re.fullmatch(r'bytes 0-3/(\d+)',response.headers.get('Content-Range') or '')
        if response.status!=206 or not match:
            raise ValueError('Strict public Parquet size range required before reading')
        magic=response.read(4);budget.bytes+=len(magic)
        if magic!=b'PAR1':raise ValueError('Pinned actual Parquet magic required')
    return int(match.group(1))


def main():
    if OUT.exists() or DATA.exists():raise ValueError('Preserve frozen unseen-source attempt; no resampling')
    c=json.loads(CONFIG.read_text()); start=time.monotonic();cpu=time.process_time()
    for path,expected in c['bindings'].items():
        if sha256(Path(path))!=expected:raise ValueError('Acceptance source/code/calibration binding changed')
    tok=Tokenizer(ROOT/c['tokenizer']);rng=random.Random(c['seed'])
    previous=json.loads(Path(c['calibration_sample']).read_text())['rows']
    old_ids={x['source_id'] for x in previous};old_urls={url_key(x['URL']) for x in previous}
    old_bodies={digest(normalized(x['text'])) for x in previous}
    old_bodies.update(digest(normalized(x['text'])) for x in json.loads(Path(c['calibration_bodies']).read_text())['rows'])
    seen_ids=set();seen_urls=set();seen_bodies=set();selected=[];files=[];counts=Counter()
    DATA.mkdir(parents=True)
    boot=Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    ticks=Path(f'/proc/{os.getpid()}/stat').read_text().rsplit(')',1)[1].split()[19]
    job=dict(status='running',created_at=now(),pid=os.getpid(),boot_id=boot,start_ticks=ticks,
        config_sha256=sha256(CONFIG),stage='public_source_ranges',scientific_teacher_tokens=0,GPU_seconds=0)
    atomic_json(DATA/'job.json',job)
    budget=RangeBudget(c['remote_byte_limit'],c['remote_wall_limit_seconds'])
    try:
        with sqlite3.connect(f"file:{c['existing_registry']}?mode=ro",uri=True) as db:
            db.execute('PRAGMA query_only=ON')
            state=dict(db.execute('SELECT key,value FROM state'))
            for source_file in c['files']:
                if time.process_time()-cpu>c['CPU_limit_seconds']:raise TimeoutError('CPU source budget exhausted')
                url=f"https://huggingface.co/datasets/{c['repository']}/resolve/{c['revision']}/{source_file}"
                size=probe_size(url,budget)
                with RangeFile(url,size,budget) as stream:
                    parquet=pq.ParquetFile(stream,pre_buffer=False)
                    group=rng.randrange(parquet.metadata.num_row_groups)
                    offset=sum(parquet.metadata.row_group(k).num_rows for k in range(group))
                    expected=sum(parquet.metadata.row_group(group).column(k).total_compressed_size
                        for k in range(parquet.metadata.num_columns)
                        if parquet.metadata.row_group(group).column(k).path_in_schema in COLUMNS)
                    if budget.bytes+expected>budget.maximum_bytes:
                        raise ValueError('Frozen selected columns exceed remaining remote byte ceiling')
                    rows=parquet.read_row_group(group,columns=COLUMNS,use_threads=False).to_pylist()
                    order=list(range(len(rows)));rng.shuffle(order);accepted=0
                    for row_number in order:
                        if time.monotonic()>budget.deadline or time.process_time()-cpu>c['CPU_limit_seconds']:
                            raise TimeoutError('Fixed acceptance wall/CPU deadline exhausted')
                        row=rows[row_number];counts['candidates_inspected']+=1
                        text=row['text'];key=url_key(row['url'] or '')
                        if not text or not row['id'] or not key:
                            counts['missing_source']+=1;continue
                        if int(hashlib.sha256(key.encode()).hexdigest()[:16],16)%1000>=900:
                            counts['new_URL_family_holdout']+=1;continue
                        if row['id'] in old_ids or key in old_urls:
                            counts['calibration_family_excluded']+=1;continue
                        if row['id'] in seen_ids or key in seen_urls:
                            counts['local_family_excluded']+=1;continue
                        raw_norm=digest(normalized(text))
                        if raw_norm in old_bodies or db.execute('SELECT id FROM exact WHERE hash=?',(raw_norm,)).fetchone():
                            counts['old_raw_exact_excluded']+=1;continue
                        if db.execute('SELECT id FROM urls WHERE url=?',(key,)).fetchone():
                            counts['old_URL_excluded']+=1;continue
                        body,why=select_article(text,tok,c['minimum_body_tokens'],c['maximum_body_tokens'])
                        if body is None:
                            counts['structural_rejection:'+why]+=1;continue
                        body_norm=digest(normalized(body['text']))
                        if body_norm in old_bodies or body_norm in seen_bodies or db.execute('SELECT id FROM exact WHERE hash=?',(body_norm,)).fetchone():
                            counts['old_or_local_extracted_body_exact_excluded']+=1;continue
                        selected.append(dict(index=len(selected),source_file=source_file,source_row=offset+row_number,
                            row_group=group,source_id=row['id'],URL=row['url'],URL_family_sha256=hashlib.sha256(key.encode()).hexdigest(),
                            split='TRAIN_candidate_only',original_document_text=text,original_document_sha256=digest(text),
                            quality_score=row['quality_score'],**body))
                        seen_ids.add(row['id']);seen_urls.add(key);seen_bodies.add(body_norm);accepted+=1
                        if accepted==c['rows_per_file']:break
                    ranges=[]
                    file_index=len(files)
                    for i,(range_offset,content) in enumerate(stream.cache):
                        path=DATA/f'file-{file_index:02d}-range-{i:02d}-{range_offset}.bin';path.write_bytes(content)
                        ranges.append(dict(offset=range_offset,bytes=len(content),path=str(path),sha256=sha256(path)))
                    files.append(dict(file=source_file,file_bytes=size,file_rows=parquet.metadata.num_rows,
                        row_groups=parquet.metadata.num_row_groups,chosen_group=group,decoded_rows=len(rows),
                        eligible_inspection_selected=accepted,ranges=ranges))
                    atomic_json(DATA/'partial-sample.json',dict(rows=selected))
                    job.update(stage=source_file,selected_rows=len(selected),remote_bytes=budget.bytes,
                        wall_seconds=time.monotonic()-start,updated_at=now())
                    atomic_json(DATA/'job.json',job)
                    if accepted!=c['rows_per_file']:raise ValueError('One frozen source group lacks16 candidates')
            if len(selected)!=64:raise ValueError('All64 frozen candidates required')
            target=DATA/'source-sample.json';atomic_json(target,dict(rows=selected))
            report=dict(status='fixed_unseen64_article_candidates_unreviewed',created_at=now(),
                config_sha256=sha256(CONFIG),repository=c['repository'],revision=c['revision'],seed=c['seed'],
                sample=dict(path=str(target),sha256=sha256(target)),source_files=files,exclusions=dict(counts),
                body_tokens_in_inspection=sum(x['native_body_tokens'] for x in selected),
                original_body_UTF8_bytes=sum(x['original_body_UTF8_bytes'] for x in selected),selected_rows=len(selected),
                distinct_source_families=len(seen_urls),remote_bytes=budget.bytes,HTTP_range_requests=budget.requests,
                wall_seconds=time.monotonic()-start,CPU_seconds=time.process_time()-cpu,existing_registry_state=state,
                all_original_spans_contiguous_and_punctuation_preserved=True,calibration_ID_URL_families_excluded=True,
                whole_parent_and_extracted_body_old_exact_lookup=True,old_corpus_scan=False,
                protected_test_bodies_read=False,embedding_column_requested=False,
                content_reviewed=0,source_accepted=False,Base_complete=False,
                new_prepared_training_tokens=0,scientific_teacher_tokens=0,GPU_seconds=0,
                Chat_started=False,quantization_started=False,
                next_action='Read all64 selected original parents and their exact extracted article spans, bind every independent nonblind grammar/coherence/completeness/boilerplate score to source SHA. Require at least54/64 usable as frozen; no quality-result source reroll or extractor tune. If accepted, measure source supply/protected-family exclusions and freeze a controlled native10M Base training budget before larger prep.',
                limitations='This sample is conditioned on the frozen structural selector and old indexed exclusions. It measures retained-source suitability, not whole-corpus quality, learned quality or global near-family independence. Four uniformly selected source files with one random group each. No raw-versus-cleaned training effect or facts certification yet.')
        if report['wall_seconds']>c['remote_wall_limit_seconds'] or report['CPU_seconds']>c['CPU_limit_seconds']:
            raise TimeoutError('Final acceptance budget exhausted')
        job.update(status='complete',ended_at=now(),selected_rows=64,stage='content_pending')
    except Exception as error:
        atomic_json(DATA/'partial-sample.json',dict(rows=selected))
        report=dict(status='unseen_acceptance_retrieval_failure_preserved',created_at=now(),
            config_sha256=sha256(CONFIG),error_type=type(error).__name__,remote_bytes=budget.bytes,
            HTTP_range_requests=budget.requests,wall_seconds=time.monotonic()-start,
            CPU_seconds=time.process_time()-cpu,selected_rows=len(selected),files=files,exclusions=dict(counts),
            source_accepted=False,Base_complete=False,scientific_teacher_tokens=0,GPU_seconds=0,
            next_action='Inspect preserved bounded retrieval failure and ranges; no result-based resampling, identical retry or full-file fallback.')
        job.update(status='failed',ended_at=now(),error_type=type(error).__name__)
        atomic_json(DATA/'job.json',job);atomic_json(OUT,report)
        raise RuntimeError('Bounded acceptance retrieval failed; original evidence preserved') from None
    atomic_json(DATA/'job.json',job);atomic_json(OUT,report)
    print({k:report[k] for k in ('status','selected_rows','body_tokens_in_inspection','remote_bytes','wall_seconds','CPU_seconds')})


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
