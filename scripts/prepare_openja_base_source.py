"""Freeze and run a single bounded source-group preparation; no training."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import signal
import sys
import time
import xml.etree.ElementTree as ET
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import pyarrow.parquet as pq
from jmicro.experiment import ROOT,read_json,now,sha256
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity
from remote_parquet_ranges import RangeBudget,RangeFile
from openja_base_source import candidate,fixed_sample

REPORT=ROOT/'reports/phase6'
CONFIG=ROOT/'configs/phase6/openja_base_source.json'
RUN=REPORT/'openja-base-source-20261007'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/openja-base-source-20261007')
COLUMNS=['text','id','issueID','speechURL']


def ref(path): return dict(path=str(path),sha256=sha256(path))


def freeze():
    if CONFIG.exists() or RUN.exists() or DATA.exists(): raise ValueError('Preserve one frozen group; no reroll')
    proposal_path=REPORT/'openja_base_source_feasibility_proposal.json';proposal=read_json(proposal_path)
    footer_path=REPORT/'openja_base_footer.json';footer=read_json(footer_path)
    if footer['status']!='pinned_metadata_only_footer_observed' or footer['proposal_sha256']!=sha256(proposal_path):
        raise ValueError('Bound prior metadata-only footer required')
    tests=REPORT/'openja_base_source_tests.xml';suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('errors','failures','skipped')):
        raise ValueError('Actual source extraction/codec/split/sample checks required')
    valid=[g['index'] for g in footer['row_groups'] if sum(x['compressed_bytes'] for x in g['columns'] if x['path'] in COLUMNS)+4*1024*1024<=96*1024*1024]
    if not valid: raise ValueError('No actual group fits predeclared ceiling; no full-file fallback')
    group=random.Random(2026100753).choice(valid);g=footer['row_groups'][group]
    old=read_json(ROOT/'configs/phase6/natural_context_contrast_comparison.json');tok=ROOT/old['tokenizer']
    if sha256(tok)!=old['tokenizer_sha256']: raise ValueError('Pinned original codec required')
    atomic_json(CONFIG,dict(created_at=now(),references=dict(proposal=ref(proposal_path),footer=ref(footer_path),
        tokenizer=ref(tok),fixed_suite=ref(ROOT/'eval/base.jsonl'),CPU_tests=ref(tests)),
        source_sha256={p:sha256(ROOT/p) for p in ('scripts/openja_base_source.py','scripts/prepare_openja_base_source.py',
            'scripts/remote_parquet_ranges.py','src/jmicro/tokenizer.py','tests/test_openja_base_source.py','uv.lock')},
        repository=footer['repository'],revision=footer['revision'],file='openja.parquet',file_bytes=footer['file_bytes'],
        upstream_full_blob_SHA256=footer['upstream_full_blob_SHA256'],full_blob_hash_independently_verified=False,
        columns=COLUMNS,fit_groups=valid,group=group,group_seed=2026100753,
        expected_compressed_column_bytes=sum(x['compressed_bytes'] for x in g['columns'] if x['path'] in COLUMNS),
        source_row_offset=sum(x['rows'] for x in footer['row_groups'][:group]),expected_group_rows=g['rows'],
        sample_seed=2026100755,budgets=proposal['next_source_budget'],readiness=proposal['readiness'],
        split=proposal['splits'],body_contract=proposal['body_contract'],failure_policy=proposal['failure_policy'],
        GPU_seconds=0,scientific_teacher_tokens=0,Base_complete=False))
    print(json.dumps(dict(status='one_group_frozen_before_content',group=group,rows=g['rows'],config_sha256=sha256(CONFIG))))


def run():
    if RUN.exists() or DATA.exists(): raise ValueError('Preserve one-shot preparation; no alternate group or reroll')
    c=read_json(CONFIG)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen source changed: '+name)
    for name,reference in c['references'].items():
        if sha256(Path(reference['path']))!=reference['sha256']: raise ValueError('Frozen reference changed: '+name)
    DATA.mkdir();RUN.mkdir()
    job=dict(status='running',stage='source_ranges',created_at=now(),**identity(),config_sha256=sha256(CONFIG),
        GPU_seconds=0,scientific_teacher_tokens=0,restart_command='Inspect terminal/partial records; no blind retry or new source group.')
    atomic_json(RUN/'job.json',job)
    start=time.monotonic();stage='source_ranges';budget=RangeBudget(c['budgets']['maximum_range_bytes'],120)
    def alarm(*args): raise TimeoutError('Fixed '+stage+' wall limit exhausted')
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,120)
    ranges=[];cached=[]
    try:
        url=f"https://huggingface.co/datasets/{c['repository']}/resolve/{c['revision']}/{c['file']}"
        with RangeFile(url,c['file_bytes'],budget) as stream:
            if stream.read(4)!=b'PAR1': raise ValueError('Exact public Parquet header required')
            parquet=pq.ParquetFile(stream,pre_buffer=False)
            footer=read_json(Path(c['references']['footer']['path']))
            if parquet.metadata.num_rows!=footer['rows'] or parquet.metadata.row_group(c['group']).num_rows!=c['expected_group_rows']:
                raise ValueError('Actual source metadata row count changed')
            # Bind re-read small header/footer ranges to original metadata evidence.
            for offset,content in stream.cache:
                known=next((r for r in footer['ranges'] if r['offset']==offset and r['bytes']==len(content)),None)
                if known is None or hashlib.sha256(content).hexdigest()!=known['sha256']: raise ValueError('Original header/footer range changed')
            table=parquet.read_row_group(c['group'],columns=COLUMNS,use_threads=False)
            cached=list(stream.cache)
        network_elapsed=time.monotonic()-start
        for index,(offset,content) in enumerate(cached):
            path=DATA/f'range-{index:03d}-{offset}.bin';path.write_bytes(content)
            ranges.append(dict(offset=offset,bytes=len(content),path=str(path),sha256=hashlib.sha256(content).hexdigest()))
        atomic_json(RUN/'pin.json',dict(created_at=now(),repository=c['repository'],revision=c['revision'],file=c['file'],
            source_group=c['group'],range_pins=ranges,remote_bytes=budget.bytes,HTTP_requests=budget.requests,
            network_wall_seconds=network_elapsed,upstream_full_blob_SHA256=c['upstream_full_blob_SHA256'],
            full_blob_hash_independently_verified=False,scope='Exact HTTP206 ranges at pinned revision/size, matching original metadata ranges. Partial column bytes hashed once, not a full1.86GB hash audit.'))
        stage='CPU_preparation';signal.setitimer(signal.ITIMER_REAL,90);start=time.monotonic()
        job.update(stage=stage,network_wall_seconds=network_elapsed,remote_bytes=budget.bytes);atomic_json(RUN/'job.json',job)
        tok=Tokenizer(Path(c['references']['tokenizer']['path']))
        fixed=[json.loads(line) for line in Path(c['references']['fixed_suite']['path']).read_text().splitlines()]
        protected=[r['prefix'] for r in fixed if r['split']=='dev' and len(r['prefix'])>=12]
        rows=table.to_pylist();accepted={s:[] for s in ('train','dev','test')};rejected=Counter();seen=set();decoded_bytes=0
        for index,source in enumerate(rows):
            if isinstance(source['text'],str): decoded_bytes+=len(source['text'].encode('utf-8',errors='strict'))
            if decoded_bytes>c['budgets']['maximum_decoded_body_bytes']: raise ValueError('Fixed decoded body byte limit exceeded')
            row,reason=candidate(source,c['source_row_offset']+index,c['group'],tok,protected)
            if reason: rejected[reason]+=1
            elif row['body_sha256'] in seen: rejected['exact_body_duplicate']+=1
            else: seen.add(row['body_sha256']);accepted[row['split']].append(row)
            if (index+1)%8192==0:
                job.update(scanned_rows=index+1,heartbeat_at=now(),CPU_seconds=time.monotonic()-start);atomic_json(RUN/'job.json',job)
        sample,indices=fixed_sample(accepted['train'],c['sample_seed']) if len(accepted['train'])>=80 else ([],[])
        atomic_json(RUN/'fixed80.json',dict(created_at=now(),config_sha256=sha256(CONFIG),source_pin_sha256=sha256(RUN/'pin.json'),
            seed=c['sample_seed'],indices=indices,rows=sample,content_read_before_freeze=False,
            method='Uniform eligible TRAIN utterances without replacement within fixed source group. Meeting families cluster utterances;80rows are not80 independent meetings.'))
        counts={};files={}
        for split,items in accepted.items():
            path=DATA/(split+'-source.jsonl');digest=hashlib.sha256();size=0
            with path.open('xb') as f:
                for row in items:
                    encoded=(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n').encode()
                    f.write(encoded);digest.update(encoded);size+=len(encoded)
            counts[split]=dict(documents=len(items),meetings=len({r['meeting'] for r in items}),body_tokens=sum(r['body_tokens'] for r in items),
                serialized_tokens=sum(r['body_tokens']+2 for r in items),body_bytes=sum(r['body_bytes'] for r in items))
            files[split]=dict(path=str(path),sha256=digest.hexdigest(),bytes=size,mtime_ns=path.stat().st_mtime_ns)
        enough=counts['train']['body_tokens']>=c['readiness']['minimum_distinct_TRAIN_body_tokens'];elapsed=time.monotonic()-start
        if elapsed>90: raise TimeoutError('CPU90s exhausted')
        result=dict(status='fixed80_content_review_pending' if enough else 'fixed_group_amount_failed',created_at=now(),
            actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},config_sha256=sha256(CONFIG),source_pin=ref(RUN/'pin.json'),
            source_group=c['group'],source_rows=len(rows),decoded_UTF8_body_bytes=decoded_bytes,network_wall_seconds=network_elapsed,
            remote_bytes=budget.bytes,HTTP_requests=budget.requests,CPU_seconds=elapsed,splits=counts,source_files=files,
            rejections=dict(rejected),fixed80=ref(RUN/'fixed80.json'),amount_screen_passed=enough,content_screen_passed=None,
            eligible_for_training=False,new_distinct_TRAIN_body_tokens=counts['train']['body_tokens'],
            original_codec_preserved=True,old_corpus_scanned=False,protected_test_scored=False,GPU_seconds=0,scientific_teacher_tokens=0,
            optimizer_updates=0,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,
            next_action='If amount passed, individually read all frozen80 and apply prior72 grammar/64 standalone coherence. If not, close one-group condition without retrieval/group/filter/seed/threshold rescue.')
        atomic_json(RUN/'result.json',result);atomic_json(REPORT/'openja_base_source_preparation.json',result)
        job.update(status='complete',ended_at=now(),CPU_seconds=elapsed,scanned_rows=len(rows));atomic_json(RUN/'job.json',job)
        print(json.dumps(dict(status=result['status'],group=c['group'],TRAIN=counts['train'],CPU_seconds=elapsed,network_seconds=network_elapsed,
            remote_bytes=budget.bytes,rejections=dict(rejected))))
    except BaseException as error:
        job.update(status='failed',stage=stage,ended_at=now(),error_type=type(error).__name__,phase_seconds=time.monotonic()-start,
            remote_bytes=budget.bytes,HTTP_requests=budget.requests)
        atomic_json(RUN/'job.json',job);raise RuntimeError('Bounded source preparation failed; sanitized actual job saved') from None
    finally: signal.setitimer(signal.ITIMER_REAL,0)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();parser.add_argument('--freeze',action='store_true');args=parser.parse_args()
    freeze() if args.freeze else run()
