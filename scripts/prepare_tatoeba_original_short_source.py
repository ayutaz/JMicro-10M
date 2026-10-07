"""Bounded, one-shot official Japanese CC0 recovery and unchanged-body preparation."""
import argparse
import bz2
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import signal
import sys
import time
import urllib.request
from urllib.parse import urlparse
import xml.etree.ElementTree as ET
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
from jmicro.experiment import ROOT,read_json,now,sha256
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity,alive
from tatoeba_original_short_source import parse_line,candidate,fixed_sample

PROPOSAL=ROOT/'reports/phase6/tatoeba_original_short_source_feasibility_proposal.json'
CONFIG=ROOT/'configs/phase6/tatoeba_original_short_source.json'
RUN=ROOT/'reports/phase6/tatoeba-original-short-source-20261007'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/tatoeba-original-short-20261007')
URL='https://downloads.tatoeba.org/exports/per_language/jpn/jpn_sentences_CC0.tsv.bz2'
DOWNLOADS='https://tatoeba.org/en/downloads'
POLICY='https://en.wiki.tatoeba.org/articles/show/cc0-contributions'
SOURCES=('scripts/tatoeba_original_short_source.py','scripts/prepare_tatoeba_original_short_source.py',
    'scripts/prepare_tatoeba_original_short_source.ps1','tests/test_tatoeba_original_short_source.py',
    'src/jmicro/tokenizer.py','src/jmicro/evaluation.py','src/jmicro/training.py','scripts/phase6_performance.py','uv.lock')


def reference(p):return dict(path=str(p),sha256=sha256(p))


def freeze():
    if CONFIG.exists() or DATA.exists() or (RUN/'job.json').exists(): raise ValueError('Preserve existing source pin/attempt; no reroll')
    tests=ROOT/'reports/phase6/tatoeba_original_short_source_tests.xml'
    suites=list(ET.parse(tests).getroot().iter('testsuite'))
    if sum(int(s.attrib['tests']) for s in suites)!=5 or any(int(s.attrib[k]) for s in suites for k in ('failures','errors','skipped')):
        raise ValueError('Five actual successful CPU source-contract checks required')
    proposal=read_json(PROPOSAL)
    if (proposal['budgets']!=dict(network_wall_seconds=60,maximum_compressed_download_bytes=67108864,
        maximum_decompressed_bytes=134217728,CPU_preparation_seconds=90,GPU_seconds=0,scientific_teacher_tokens=0)
        or proposal['readiness_screen']['minimum_distinct_eligible_TRAIN_body_tokens']!=1000000):
        raise ValueError('Keep the predeclared feasibility/amount/quality conditions')
    previous=ROOT/'reports/phase6/base_gradient_precision_completion.json';prior=read_json(previous)
    previous_job=read_json(ROOT/'reports/phase6/base-gradient-precision-20261007/job.json')
    if alive(previous_job) or previous_job['status']!='complete' or prior['precision_training_comparison_supported']:
        raise ValueError('Prior assay must be actually ended and unsupported precision route closed')
    old=read_json(ROOT/'configs/phase6/natural_context_contrast_comparison.json')
    tokenizer=ROOT/old['tokenizer']
    if sha256(tokenizer)!=old['tokenizer_sha256']: raise ValueError('Original pinned tokenizer required')
    evaluation=ROOT/'eval/base.jsonl'
    atomic_json(CONFIG,dict(created_at=now(),proposal=reference(PROPOSAL),CPU_tests=reference(tests),previous_completion=reference(previous),
        source_sha256={n:sha256(ROOT/n) for n in SOURCES},source_url=URL,downloads_page=DOWNLOADS,CC0_original_policy=POLICY,
        expected_fields=['sentence_id','lang','text','date_last_modified'],language='jpn',license='CC0-1.0',
        tokenizer=reference(tokenizer),fixed_suite=reference(evaluation),
        exclusion='Reuse public-magpie source contract: fixed Base DEV prefixes of at least12characters excluded as exact substrings. No protected-test answers/scoring or source-quality selection from generation.',
        split='SHA256 exact original body family, modulo100:90percent TRAIN/5percentDEV/5percentTEST; source IDs provide attribution, exact body duplicates share split',
        sample_seed=2026100747,sample_count=80,budgets=proposal['budgets'],readiness_screen=proposal['readiness_screen'],
        failure_policy=proposal['failure_policy'],GPU_seconds=0,scientific_teacher_tokens=0,Base_complete=False,Chat_started=False,quantization_started=False))
    print(json.dumps(dict(status='official_CC0_source_protocol_frozen',config_sha256=sha256(CONFIG),GPU_seconds=0)))


def inspect():
    c=read_json(CONFIG)
    if DATA.exists() or (RUN/'job.json').exists(): raise ValueError('Inspect existing one-shot acquisition/preparation; never blindly repeat')
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest: raise ValueError('Frozen source changed: '+name)
    for key in ('proposal','CPU_tests','previous_completion','tokenizer','fixed_suite'):
        if sha256(Path(c[key]['path']))!=c[key]['sha256']: raise ValueError('Frozen preparation reference changed: '+key)
    previous=read_json(ROOT/'reports/phase6/base-gradient-precision-20261007/job.json')
    if alive(previous) or previous['status']!='complete': raise ValueError('Prior diagnostic still active')
    return c


def fetch(url,path,maximum,deadline):
    if path.exists() or path.with_suffix(path.suffix+'.partial').exists(): raise ValueError('Never overwrite/redownload a source snapshot')
    temporary=path.with_suffix(path.suffix+'.partial');digest=hashlib.sha256();size=0;began=time.monotonic()
    remaining=deadline-began
    if remaining<=0: raise TimeoutError('Acquisition network budget exhausted')
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'JMicro-10M source feasibility'}),timeout=min(20,remaining)) as response:
        if urlparse(response.url).hostname!=urlparse(url).hostname:
            raise ValueError('No unverified download mirror')
        headers={k:response.headers.get(k) for k in ('Content-Length','Last-Modified','ETag','Content-Type')}
        if headers['Content-Length'] and int(headers['Content-Length'])>maximum: raise ValueError('Pinned source exceeds predeclared byte limit')
        with temporary.open('wb') as output:
            while True:
                if time.monotonic()>deadline: raise TimeoutError('Fixed network wall budget exhausted')
                chunk=response.read(65536)
                if not chunk: break
                size+=len(chunk)
                if size>maximum: raise ValueError('Compressed/source-page byte limit exceeded')
                output.write(chunk);digest.update(chunk)
        final_url=response.url
    temporary.replace(path);st=path.stat()
    return dict(url=url,final_url=final_url,path=str(path),sha256=digest.hexdigest(),bytes=size,
        mtime_ns=st.st_mtime_ns,HTTP_metadata=headers,wall_seconds=time.monotonic()-began,completed_at=now())


def run():
    c=inspect();RUN.mkdir(parents=True,exist_ok=True);DATA.mkdir(parents=True,exist_ok=False)
    job=dict(status='starting',**identity(),created_at=now(),config_sha256=sha256(CONFIG),GPU_seconds=0,scientific_teacher_tokens=0,
        restart_command='One-shot source pin and preparation; inspect existing terminal/partial evidence, no blind redownload or sample reroll.')
    atomic_json(RUN/'job.json',job);stage='network';started=time.monotonic();pins={}
    def alarm(*args): raise TimeoutError('Predeclared source '+stage+' wall budget exhausted')
    try:
        signal.signal(signal.SIGALRM,alarm);signal.alarm(c['budgets']['network_wall_seconds'])
        deadline=started+c['budgets']['network_wall_seconds']
        for name,url in (('downloads',DOWNLOADS),('CC0_policy',POLICY)):
            pins[name]=fetch(url,DATA/(name+'.html'),1048576,deadline)
        page=Path(pins['downloads']['path']).read_text(encoding='utf-8')
        policy=Path(pins['CC0_policy']['path']).read_text(encoding='utf-8')
        plain=re.sub(r'<[^>]*>',' ',policy);plain=' '.join(plain.split())
        if URL not in page or 'Contains all the sentences available under CC0' not in page:
            raise ValueError('Actual official Japanese CC0 download URL/description not verified')
        if 'original sentences' not in plain or 'currently usable only' not in plain:
            raise ValueError('Official original-only CC0 contribution policy not verified')
        pins['Japanese_CC0']=fetch(URL,DATA/'jpn_sentences_CC0.tsv.bz2',c['budgets']['maximum_compressed_download_bytes'],deadline)
        network_elapsed=time.monotonic()-started
        if network_elapsed>c['budgets']['network_wall_seconds']: raise TimeoutError('Acquisition network budget exhausted')
        signal.alarm(0);atomic_json(RUN/'pin.json',dict(created_at=now(),files=pins,network_wall_seconds=network_elapsed,
            verified_Japanese_CC0_URL_in_actual_official_page=True,verified_original_only_policy=True,
            independently_verified_authorship=False,no_audio_or_translation_links=True))
        stage='CPU_preparation';started=time.monotonic();signal.alarm(c['budgets']['CPU_preparation_seconds'])
        job.update(status='running',stage=stage,heartbeat_at=now());atomic_json(RUN/'job.json',job)
        tokenizer=Tokenizer(Path(c['tokenizer']['path']))
        fixed=[json.loads(line) for line in Path(c['fixed_suite']['path']).read_text().splitlines()]
        protected=[r['prefix'] for r in fixed if r['split']=='dev' and len(r['prefix'])>=12]
        rejected=Counter();records=0;decompressed=0;families=set();source_ids=set();accepted={s:[] for s in ('train','dev','test')}
        with bz2.open(Path(pins['Japanese_CC0']['path']),'rb') as source:
            while True:
                raw=source.readline(131073)
                if not raw: break
                decompressed+=len(raw);records+=1
                if decompressed>c['budgets']['maximum_decompressed_bytes'] or len(raw)>131072:
                    raise ValueError('Fixed decompressed/record size limit exceeded')
                record=parse_line(raw)
                if record['source_id'] in source_ids: raise ValueError('Unexpected duplicate official sentence ID')
                source_ids.add(record['source_id'])
                row,reason=candidate(record,tokenizer,protected)
                if reason: rejected[reason]+=1
                elif row['family'] in families: rejected['exact_body_duplicate']+=1
                else: families.add(row['family']);accepted[row['split']].append(row)
                if records%4096==0:
                    if time.monotonic()-started>c['budgets']['CPU_preparation_seconds']: raise TimeoutError('Fixed CPU90s exhausted')
                    job.update(scanned_rows=records,heartbeat_at=now(),CPU_seconds=time.monotonic()-started)
                    atomic_json(RUN/'job.json',job)
        sample,indices=fixed_sample(accepted['train'],c['sample_seed']) if len(accepted['train'])>=80 else ([],[])
        # Freeze all80 before any content judgment; short source amount failure
        # remains a failure even if individual sentences look good.
        atomic_json(RUN/'fixed80.json',dict(created_at=now(),config_sha256=sha256(CONFIG),source_pin_sha256=sha256(RUN/'pin.json'),
            seed=c['sample_seed'],method='Uniform eligible TRAIN document sample without replacement; sorted drawn positions',
            indices=indices,rows=sample,content_read_before_freeze=False,source_amount_not_a_quality_score=True))
        files={};counts={}
        for split,rows in accepted.items():
            target=DATA/(split+'-source.jsonl');digest=hashlib.sha256();size=0
            with target.open('wb') as stream:
                for row in rows:
                    line=(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n').encode()
                    stream.write(line);digest.update(line);size+=len(line)
            files[split]=dict(path=str(target),sha256=digest.hexdigest(),bytes=size,mtime_ns=target.stat().st_mtime_ns)
            counts[split]=dict(documents=len(rows),body_tokens=sum(r['body_tokens'] for r in rows),
                serialized_tokens=sum(r['body_tokens']+2 for r in rows),body_bytes=sum(r['body_bytes'] for r in rows))
        enough=counts['train']['body_tokens']>=c['readiness_screen']['minimum_distinct_eligible_TRAIN_body_tokens']
        elapsed=time.monotonic()-started
        if elapsed>c['budgets']['CPU_preparation_seconds']: raise TimeoutError('Fixed CPU90s exhausted')
        signal.alarm(0)
        result=dict(status='source_pinned_prepared_content_review_pending' if enough else 'source_pinned_prepared_amount_screen_failed',
            created_at=now(),config_sha256=sha256(CONFIG),actual_identity={k:job[k] for k in ('pid','boot_id','start_ticks')},
            source_pin=reference(RUN/'pin.json'),source_pin_files=pins,network_wall_seconds=network_elapsed,CPU_seconds=elapsed,
            compressed_bytes=pins['Japanese_CC0']['bytes'],decompressed_bytes=decompressed,source_rows=records,
            splits=counts,source_files=files,rejections=dict(rejected),fixed80=reference(RUN/'fixed80.json'),
            amount_screen_passed=enough,content_screen_passed=None,eligible_for_training=False,
            source='Tatoeba official Japanese CC0 text',license='CC0-1.0',new_distinct_TRAIN_body_tokens=counts['train']['body_tokens'],
            fixed_DEV_exclusion_prefixes=len(protected),GPU_seconds=0,scientific_teacher_tokens=0,optimizer_updates=0,
            old_corpus_scanned=False,tokenizer_retrained=False,protected_test_scored=False,Base_complete=False,
            Base_adopted=False,Chat_started=False,quantization_started=False,quality_criteria_unchanged=True,
            limitations='Original status inferred from official CC0 export/workflow policy, not independent contributor verification. Exact bodies share splits; semantic paraphrase/near-template families are not certified independent. Old Base DEV prefix exclusion is reused; it is not comprehensive semantic decontamination. Uniform source sentence sample does not establish model quality.',
            next_action='Amount passed: read fixed80 and apply frozen72 grammar/64 coherent-original screen before any training. Amount failed: close this fixed CC0 condition; no data/license/filter/seed/threshold/epoch rescue or GPU.')
        atomic_json(RUN/'result.json',result);atomic_json(ROOT/'reports/phase6/tatoeba_original_short_source_preparation.json',result)
        job.update(status='complete',ended_at=now(),network_wall_seconds=network_elapsed,CPU_seconds=elapsed,scanned_rows=records)
        atomic_json(RUN/'job.json',job)
        print(json.dumps(dict(status=result['status'],network_seconds=network_elapsed,CPU_seconds=elapsed,
            source_rows=records,TRAIN=counts['train'],amount_screen_passed=enough)))
    except BaseException as error:
        signal.alarm(0);job.update(status='failed',ended_at=now(),stage=stage,error=repr(error),phase_wall_seconds=time.monotonic()-started)
        atomic_json(RUN/'job.json',job);raise


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group()
    group.add_argument('--freeze',action='store_true');group.add_argument('--inspect',action='store_true');args=parser.parse_args()
    if args.freeze: freeze()
    elif args.inspect: inspect();print('Frozen official CC0 source preflight passed; GPU0')
    else: run()
