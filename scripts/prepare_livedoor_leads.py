"""Fixed, small authored-Japanese source pilot; original archive stays native."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import re
import sys
import tarfile
import time
import urllib.request
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'src'),str(Path(__file__).resolve().parent)]
import numpy as np
from jmicro.evaluation import canonicalize_text
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.training import atomic_json,implementation_hashes
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity,alive

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/livedoor-leads-20261006')
RUN=ROOT/'reports/phase6/livedoor-leads-20261006'
CONFIG=ROOT/'configs/phase6/livedoor_leads_preparation.json'
SOURCES=('scripts/prepare_livedoor_leads.py','tests/test_livedoor_leads.py')
URL='https://www.rondhuit.com/download/ldcc-20140209.tar.gz'
SEED=2026100652
TOKENIZER_SHA='a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318'


def reference(path):return dict(path=str(path),sha256=sha256(path))


def family_split(article):
    value=int(hashlib.sha256(('livedoor-'+article).encode()).hexdigest()[:16],16)%1000
    return 'train' if value<900 else 'dev' if value<950 else 'test'


def first_lead(text):
    parts=text.split('\n',3)
    if len(parts)!=4 or not re.fullmatch(r'https?://\S+',parts[0].strip()):return None
    body=parts[3].strip()
    if not body:return None
    lead=canonicalize_text(re.split(r'\n[ \t\u3000]*\n',body,maxsplit=1)[0])
    if (not 40<=len(lead)<=1200 or not re.search(r'[。！？][」』）】]*$',lead)
            or lead.startswith(('■','●','#','http://','https://'))):return None
    for opening,closing in (('「','」'),('『','』'),('（','）'),('【','】')):
        depth=0
        for char in lead:
            if char==opening:depth+=1
            elif char==closing:depth-=1
            if depth<0:return None
        if depth:return None
    japanese=sum('\u3040'<=ch<='\u30ff' or '\u4e00'<=ch<='\u9fff' for ch in lead)
    if japanese/len(lead)<.35:return None
    return lead


def freeze():
    if CONFIG.exists():inspect();return
    refs={}
    for relative in ('reports/phase6/readout_source_stage_analysis.json','reports/phase6/readout_source_stages_tests.xml',
                     'reports/phase6/readout_adapter_comparison_completion.json','reports/phase6/livedoor_leads_tests.xml'):
        refs[relative]=reference(ROOT/relative)
    tokenizer=read_json(ROOT/'configs/phase6/textbook_quantity_comparison.json')['tokenizer']
    if sha256(ROOT/tokenizer)!=TOKENIZER_SHA:raise ValueError('Pinned original Tokenizer required')
    c=dict(kind='authored_Japanese_news_first_complete_paragraph_pilot_v1',created_at=now(),URL=URL,
        primary_source='https://www.rondhuit.com/download.html#ldcc',collection='2012-09 / ldcc-20140209',
        license='Publisher states CC BY-ND; original per-category LICENSE files retained with archive, no publication in this work.',
        seed=SEED,source_sha256={s:sha256(ROOT/s) for s in SOURCES},implementation=implementation_hashes(),references=refs,
        tokenizer=tokenizer,tokenizer_sha256=TOKENIZER_SHA,download_wall_seconds=60,maximum_archive_bytes=20000000,
        CPU_preparation_ceiling_seconds=120,minimum_body_tokens=24,maximum_body_tokens=256,
        sample_documents=64,maximum_weak_documents=10,family_split='article ID SHA256 modulo1000: train<900/dev<950/test remainder',
        selector='Only original first nonempty paragraph after URL/date/title; no later-paragraph fallback or added punctuation. Balanced quotes and full terminal punctuation, Japanese fraction>=.35,40..1200chars,24..256original tokens.',
        proposed_comparison='Only if fixed64 content accepted and supply measured: native10M same original d18 parent/inherited Adam/LR1e-5; Web75M+news25M versus cached original full100M mixture. Corpus/EOS/diversity intervention, not quantity-only or same-target causal claim.',
        proposed_scientific_teacher_tokens=100000000,proposed_new_GPU_ceiling_seconds=1800,
        scientific_GPU_frozen=False,science_started=False,Base_complete=False,Base_adopted=False,Chat_started=False,quantization_started=False,protected_test_used=False,
        completion_condition='Record actual raw SHA/provenance, TRAIN-only paragraphs/local exact hashes and heldout article IDs untouched, exact token/byte supply, fixed64 review. Weak>10 ends source branch; no post-review selector/reroll/filter rescue. Only accepted source permits own CUDA/resume/timing and measured-budget science freeze.',
        limitations='Natural dated news paragraphs are not verified facts or everyday fiction. Repeated epochs are learning, not more distinct data. Possible overlap with old Web and benchmark ancestry remains incompletely audited; no claim of corpus-independent novelty.')
    atomic_json(CONFIG,c);inspect();print('Fixed authored-news preparation frozen; GPU0')


def inspect():
    c=read_json(CONFIG)
    if (c['URL']!=URL or c['seed']!=SEED or c['implementation']!=implementation_hashes()
            or c['sample_documents']!=64 or c['maximum_weak_documents']!=10
            or c['CPU_preparation_ceiling_seconds']!=120 or c['download_wall_seconds']!=60
            or c['minimum_body_tokens']!=24 or c['maximum_body_tokens']!=256
            or c['tokenizer_sha256']!=TOKENIZER_SHA or sha256(ROOT/c['tokenizer'])!=TOKENIZER_SHA
            or any(c[k] for k in ('scientific_GPU_frozen','science_started','Base_complete','Base_adopted','Chat_started','quantization_started','protected_test_used'))):
        raise ValueError('Original fixed news preparation contract required')
    for name,digest in c['source_sha256'].items():
        if sha256(ROOT/name)!=digest:raise ValueError('Frozen news source differs: '+name)
    for ref in c['references'].values():
        if sha256(Path(ref['path']))!=ref['sha256']:raise ValueError('News prerequisite differs')
    return c


def prepare():
    c=inspect();DATA.mkdir(parents=True,exist_ok=True);RUN.mkdir(parents=True,exist_ok=True);jp=RUN/'job.json'
    if jp.exists():
        job=read_json(jp)
        if job['status']=='complete' and not alive(job):print('Original prepared news retained');return
        raise ValueError('Preserve live or failed news run; no identical retry')
    job=dict(status='running',**identity(),config_sha256=sha256(CONFIG),started_at=now(),stage='download',GPU_seconds=0)
    atomic_json(jp,job);start=time.monotonic();cpu_start=None;archive=DATA/'ldcc-20140209.tar.gz'
    try:
        request=urllib.request.Request(URL,headers={'User-Agent':'JMicro-10M local research source preparation'})
        headers={};size=0
        with urllib.request.urlopen(request,timeout=30) as response,archive.open('xb') as output:
            headers={k:response.headers.get(k) for k in ('Content-Length','Content-Type','Last-Modified','ETag')}
            while True:
                if time.monotonic()-start>60:raise TimeoutError('Source download60s exhausted')
                part=response.read(262144)
                if not part:break
                size+=len(part)
                if size>c['maximum_archive_bytes']:raise ValueError('Archive byte ceiling exceeded')
                output.write(part)
        download_seconds=time.monotonic()-start;cpu_start=time.monotonic();job.update(stage='extract_original_TRAIN_leads',archive=reference(archive))
        atomic_json(jp,job);tok=Tokenizer(ROOT/c['tokenizer']);counts=Counter();records=[];families=set();digests=set();heldout=[];licences={}
        def check():
            if time.monotonic()-cpu_start>120:raise TimeoutError('News CPU preparation120s exhausted')
        with tarfile.open(archive,'r:*') as source:
            for member in sorted(source.getmembers(),key=lambda m:m.name):
                check()
                name=member.name.removeprefix('./')
                if not member.isfile():continue
                if name.endswith('/LICENSE.txt'):
                    licence=source.extractfile(member).read()
                    target=DATA/'licenses'/Path(name).parent.name/'LICENSE.txt';target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(licence)
                    licences[Path(name).parent.name]=reference(target);continue
                match=re.fullmatch(r'text/([a-z-]+)/[a-z-]+-(\d+)\.txt',name)
                if not match:continue
                category,article=match.groups();counts['source_articles']+=1;split=family_split(article)
                if split!='train':heldout.append(dict(article_id=article,split=split,category=category));counts[split+'_articles_not_decoded']+=1;continue
                if article in families:counts['duplicate_article_family']+=1;continue
                families.add(article);raw=source.extractfile(member).read();original=raw.decode('utf-8-sig');lead=first_lead(original)
                if lead is None:counts['structural_lead_rejected']+=1;continue
                ids=tok.encode(lead)
                if not 24<=len(ids)<=256:counts['token_length_rejected']+=1;continue
                digest=hashlib.sha256(lead.encode()).hexdigest()
                if digest in digests:counts['local_exact_duplicate_lead']+=1;continue
                digests.add(digest);counts['accepted_leads']+=1
                records.append(dict(doc_id='livedoor-'+article,source_family='livedoor-'+article,article_id=article,category=category,
                    split='train',kind='web',bucket='livedoor_news_lead',text=lead,body_tokens=len(ids),body_bytes=len(lead.encode()),
                    canonical_sha256=digest,source_path=name,original_article_sha256=hashlib.sha256(raw).hexdigest(),
                    source_URL=original.splitlines()[0],unit_kind='original_first_paragraph',ids=ids))
        if len(records)<64 or not licences or any(r['category'] not in licences for r in records):raise ValueError('64 original leads and all category licence attestations required')
        pool=DATA/'shards';pool.mkdir();index=[];offset=0
        corpus=DATA/'train.jsonl'
        with (pool/'train.bin').open('xb') as stream,corpus.open('x',encoding='utf-8') as output:
            for record in records:
                check();ids=record.pop('ids');stream.write(np.asarray([2,*ids,3],dtype='<u2').tobytes());output.write(json.dumps(record,ensure_ascii=False)+'\n')
                index.append({k:record[k] for k in ('doc_id','split','kind','bucket','canonical_sha256')}|dict(offset=offset,body_tokens=len(ids),bytes=record['body_bytes']))
                offset+=len(ids)+2
        atomic_json(pool/'train.index.json',index)
        atomic_json(pool/'token_bytes.json',[0 if i<8 else len(tok.decode_bytes([i])) for i in range(tok.vocab_size)])
        splits=dict(train=dict(tokens=offset,documents=len(index),body_bytes=sum(r['bytes'] for r in index),stream_sha256=sha256(pool/'train.bin'),index_sha256=sha256(pool/'train.index.json')))
        for split in ('dev','test'):
            (pool/(split+'.bin')).write_bytes(b'');atomic_json(pool/(split+'.index.json'),[])
            splits[split]=dict(tokens=0,documents=0,body_bytes=0,stream_sha256=sha256(pool/(split+'.bin')),index_sha256=sha256(pool/(split+'.index.json')))
        manifest=dict(version=1,dtype='<u2',kind='web',corpus_sha256=sha256(corpus),tokenizer_sha256=TOKENIZER_SHA,vocab_size=tok.vocab_size,
            packing='BOS/original complete paragraph/EOS; causal across documents, BOS targets masked',token_bytes_sha256=sha256(pool/'token_bytes.json'),splits=splits)
        atomic_json(pool/'manifest.json',manifest);sample=random.Random(SEED).sample(records,64);atomic_json(DATA/'sample64.json',sample);atomic_json(DATA/'heldout_article_ids.json',heldout)
        check();ready=dict(status='prepared_pending_fixed64_content_review',created_at=now(),config_sha256=sha256(CONFIG),archive=reference(archive),
            download_headers=headers,download_seconds=download_seconds,CPU_seconds=time.monotonic()-cpu_start,GPU_seconds=0,
            counts=dict(counts),category_accepted_counts=dict(Counter(r['category'] for r in records)),licenses=licences,
            pool=str(pool),manifest_sha256=sha256(pool/'manifest.json'),splits=splits,distinct_prepared_body_tokens=sum(r['body_tokens'] for r in records),
            EOS_per_supervised_token=len(index)/(offset-len(index)),sample=reference(DATA/'sample64.json'),heldout_article_ids=reference(DATA/'heldout_article_ids.json'),
            source_heldout_bodies_decoded=False,protected_test_used=False,quality_accepted=False,Base_complete=False,Chat_started=False,quantization_started=False,
            limitations=c['limitations'],next_action='Individually read fixed64 original leads and accept only weak<=10; no selector/reroll rescue, no GPU before source acceptance and measured own timing.')
        atomic_json(RUN/'ready.json',ready);atomic_json(DATA/'ready.json',ready);job.update(status='complete',stage='pending_content',completed_at=now(),ready=reference(RUN/'ready.json'))
        print(json.dumps(dict(status=ready['status'],counts=ready['counts'],CPU_seconds=ready['CPU_seconds'],tokens=offset),ensure_ascii=False))
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:job.update(seconds=time.monotonic()-start);atomic_json(jp,job)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7):raise RuntimeError('Pinned uv Python3.12.7 required')
    p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument('--freeze',action='store_true');g.add_argument('--inspect',action='store_true');args=p.parse_args()
    if args.freeze:freeze()
    elif args.inspect:inspect();print('Frozen authored-news source preparation valid; GPU0')
    else:prepare()
