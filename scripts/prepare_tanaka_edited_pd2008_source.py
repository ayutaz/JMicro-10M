"""One-pass, CPU-only preparation of a pinned exact archival source."""
import argparse
from collections import Counter
import gzip
import hashlib
import json
from pathlib import Path
import signal
import sys
import time
import xml.etree.ElementTree as ET
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,now,sha256
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity
from tanaka_edited_pd2008_source import parse_line,candidate,fixed_sample

REPORT=ROOT/'reports/phase6'
CONFIG=ROOT/'configs/phase6/tanaka_edited_pd2008_source.json'
RUN=REPORT/'tanaka-edited-pd2008-source-20261007'


def ref(path): return dict(path=str(path),sha256=sha256(path))


def freeze():
    if CONFIG.exists() or RUN.exists(): raise ValueError('Preserve one-shot preparation')
    pin=read_json(REPORT/'tanaka_edited_pd2008_source_pin.json')
    proposal=read_json(REPORT/'tanaka_edited_pd2008_source_proposal.json')
    if pin['status']!='exact_official_edited_PD2008_archive_pinned_CPU_preparation_pending': raise ValueError('Actual pinned official source required')
    if proposal['budgets']['CPU_preparation_seconds']!=90 or proposal['readiness_screen']['minimum_distinct_eligible_TRAIN_body_tokens']!=1000000:
        raise ValueError('Fixed prior budgets and minimum amount required')
    tests=REPORT/'tanaka_edited_pd2008_source_tests.xml'
    suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=4 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Actual four CPU contract checks required')
    old=read_json(ROOT/'configs/phase6/natural_context_contrast_comparison.json')
    tok=ROOT/old['tokenizer']
    if sha256(tok)!=old['tokenizer_sha256']: raise ValueError('Pinned original tokenizer required')
    refs={k:ref(path) for k,path in dict(proposal=REPORT/'tanaka_edited_pd2008_source_proposal.json',
        pin=REPORT/'tanaka_edited_pd2008_source_pin.json',format=REPORT/'tanaka_edited_pd2008_format.json',
        tokenizer=tok,fixed_suite=ROOT/'eval/base.jsonl',CPU_tests=tests).items()}
    sources={n:sha256(ROOT/n) for n in ('scripts/tanaka_edited_pd2008_source.py','scripts/prepare_tanaka_edited_pd2008_source.py',
        'tests/test_tanaka_edited_pd2008_source.py','src/jmicro/tokenizer.py','uv.lock')}
    atomic_json(CONFIG,dict(created_at=now(),references=refs,source_sha256=sources,
        source_url=pin['source_url'],schema='strict lossless EUC-JP, alternating A: Japanese TAB English CRLF and B: indexing CRLF; Japanese only',
        sample_seed=2026100751,sample_count=80,budgets=proposal['budgets'],readiness_screen=proposal['readiness_screen'],
        prior_schema_discovery_CPU_seconds=read_json(REPORT/'tanaka_edited_pd2008_format.json')['CPU_seconds'],
        split='Exact-body SHA256 family modulo100;90/5/5; no semantic family independence claim',
        limitations=proposal['hypothesis'],GPU_seconds=0,scientific_teacher_tokens=0))
    print(json.dumps(dict(status='CPU_preparation_frozen',sha256=sha256(CONFIG))))


def run():
    if RUN.exists(): raise ValueError('Inspect existing preparation; no resampling/rerun')
    c=read_json(CONFIG)
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen source changed: '+name)
    for name,reference in c['references'].items():
        if sha256(Path(reference['path']))!=reference['sha256']: raise ValueError('Frozen reference changed: '+name)
    pin=read_json(Path(c['references']['pin']['path']));archive=Path(pin['path']);stat=archive.stat()
    if (stat.st_size,stat.st_mtime_ns)!=(pin['file_size'],pin['file_mtime_ns']): raise ValueError('Actual streamed pin stat changed')
    RUN.mkdir();job=dict(status='running',stage='CPU_preparation',created_at=now(),**identity(),
        config_sha256=sha256(CONFIG),GPU_seconds=0,scientific_teacher_tokens=0,
        restart_command='Inspect terminal or partial job; no blind rerun, source redownload or fixed sample reroll.')
    atomic_json(RUN/'job.json',job)
    started=time.monotonic();prior=c['prior_schema_discovery_CPU_seconds']
    def alarm(*args): raise TimeoutError('Fixed cumulative CPU90s exhausted')
    signal.signal(signal.SIGALRM,alarm);signal.setitimer(signal.ITIMER_REAL,90-prior)
    rejected=Counter();lines=0;source_rows=0;decompressed=0
    try:
        tokenizer=Tokenizer(Path(c['references']['tokenizer']['path']))
        fixed=[json.loads(line) for line in Path(c['references']['fixed_suite']['path']).read_text().splitlines()]
        protected=[r['prefix'] for r in fixed if r['split']=='dev' and len(r['prefix'])>=12]
        accepted={s:[] for s in ('train','dev','test')};families=set()
        with gzip.open(archive,'rb') as stream:
            while True:
                raw=stream.readline(131073)
                if not raw: break
                lines+=1;decompressed+=len(raw)
                if decompressed>c['budgets']['maximum_decompressed_bytes'] or len(raw)>131072: raise ValueError('Fixed decompressed/line limit exceeded')
                body=parse_line(raw,'A' if lines%2 else 'B')
                if body is None: continue
                source_rows+=1
                row,reason=candidate(body,lines,tokenizer,protected,pin['compressed_SHA256'])
                if reason: rejected[reason]+=1
                elif row['family'] in families: rejected['exact_body_duplicate']+=1
                else: families.add(row['family']);accepted[row['split']].append(row)
                if source_rows%8192==0:
                    job.update(scanned_records=source_rows,CPU_seconds=prior+time.monotonic()-started,heartbeat_at=now())
                    atomic_json(RUN/'job.json',job)
        if lines%2: raise ValueError('Truncated unpaired A/B source record')
        sample,indices=fixed_sample(accepted['train'],c['sample_seed']) if len(accepted['train'])>=80 else ([],[])
        atomic_json(RUN/'fixed80.json',dict(created_at=now(),config_sha256=sha256(CONFIG),source_pin_sha256=c['references']['pin']['sha256'],
            seed=c['sample_seed'],indices=indices,rows=sample,method='Uniform eligible TRAIN without replacement, sorted drawn positions',
            discovery='First5 raw lines inspected only for byte encoding/record schema; no Japanese bodies displayed or scored, no content selection',
            content_read_before_freeze=False))
        counts={};files={};data=archive.parent
        for split,rows in accepted.items():
            target=data/(split+'-source.jsonl')
            if target.exists(): raise ValueError('Never overwrite prepared source')
            digest=hashlib.sha256();size=0
            with target.open('xb') as f:
                for row in rows:
                    encoded=(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n').encode()
                    f.write(encoded);digest.update(encoded);size+=len(encoded)
            counts[split]=dict(documents=len(rows),body_tokens=sum(r['body_tokens'] for r in rows),
                serialized_tokens=sum(r['body_tokens']+2 for r in rows),body_bytes=sum(r['body_bytes'] for r in rows))
            files[split]=dict(path=str(target),sha256=digest.hexdigest(),bytes=size,mtime_ns=target.stat().st_mtime_ns)
        enough=counts['train']['body_tokens']>=1000000;elapsed=prior+time.monotonic()-started
        if elapsed>90: raise TimeoutError('Fixed cumulative CPU90s exhausted')
        result=dict(created_at=now(),status='prepared_fixed80_review_pending' if enough else 'prepared_amount_screen_failed',
            config_sha256=sha256(CONFIG),actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},source_pin=c['references']['pin'],
            compressed_bytes=pin['file_size'],decompressed_bytes=decompressed,source_rows=source_rows,source_lines=lines,
            source_encoding_verified='euc_jp',source_schema_verified=True,network_wall_seconds=pin['total_network_wall_seconds'],
            cumulative_CPU_seconds=elapsed,splits=counts,source_files=files,rejections=dict(rejected),
            fixed80=ref(RUN/'fixed80.json'),fixed_DEV_exclusion_prefixes=len(protected),amount_screen_passed=enough,
            content_screen_passed=None,eligible_for_training=False,old_corpus_scanned=False,tokenizer_retrained=False,
            GPU_seconds=0,scientific_teacher_tokens=0,optimizer_updates=0,Base_complete=False,Base_adopted=False,
            Chat_started=False,quantization_started=False,protected_test_scored=False,quality_criteria_unchanged=True,
            limitations='Publisher PD edition claim, not independent rights/authorship audit. Edited translations/contrived sentences may remain. Exact dedup is not semantic family independence or complete evaluation decontamination.',
            next_action='Read frozen80 and apply prior grammar72/coherence64 before training. If quantity or quality fails, close fixed source without rescue.')
        atomic_json(RUN/'result.json',result);atomic_json(REPORT/'tanaka_edited_pd2008_source_preparation.json',result)
        job.update(status='complete',ended_at=now(),CPU_seconds=elapsed,scanned_records=source_rows);atomic_json(RUN/'job.json',job)
        print(json.dumps(dict(status=result['status'],CPU_seconds=elapsed,source_rows=source_rows,TRAIN=counts['train'],rejections=dict(rejected))))
    except BaseException as error:
        job.update(status='failed',ended_at=now(),error=repr(error),CPU_seconds=prior+time.monotonic()-started,
            scanned_records=source_rows,scanned_lines=lines,decompressed_bytes=decompressed)
        atomic_json(RUN/'job.json',job);raise
    finally: signal.setitimer(signal.ITIMER_REAL,0)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();parser.add_argument('--freeze',action='store_true');args=parser.parse_args()
    freeze() if args.freeze else run()
