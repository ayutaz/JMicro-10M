"""Distinct narrative source3M + retained whole Web explanations7M, on ext4."""
from collections import Counter
import gzip
import hashlib
import json
import multiprocessing as mp
import os
from pathlib import Path
import random
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
sys.path.insert(0,str(Path(__file__).resolve().parent))
import numpy as np
from huggingface_hub import hf_hub_download
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.literary_curriculum import paragraphs
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity,alive

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/literary-curriculum-20261006')
WEB=Path('/home/aihub_ubuntu/jmicro-data/phase6/realistic-curriculum-20261006-v2')
RUN=ROOT/'reports/phase6/literary-curriculum-20261006'
_TOK=None


def initialize(path):
    global _TOK
    _TOK=Tokenizer(Path(path))


def process(record):
    meta=record['meta'];family=str(meta.get('人物ID') or meta.get('姓','')+meta.get('名','') or meta['作品ID'])
    units=[]
    for unit in paragraphs(record,_TOK):
        units.append(dict(unit,source_family='aozora-author-'+family,work_id=meta['作品ID'],
            source_metadata=meta,source='aozorabunko_clean',source_previously_in_parent_training=False))
        if len(units)==16:break
    return units


def prepare():
    DATA.mkdir(parents=True,exist_ok=True);RUN.mkdir(parents=True,exist_ok=True)
    jobpath=RUN/'prepare-job.json'
    if jobpath.exists():
        old=read_json(jobpath);assert not alive(old)
        if old['status']=='complete':print('Completed preparation retained');return
        raise ValueError('Retain failed version; no identical retry')
    pin=read_json(ROOT/'reports/phase6/aozora_source_pin.json')
    source=next(f for f in pin['files'] if f['path'].endswith('.jsonl.gz'))
    assert source['size']<=pin['maximum_raw_bytes'] and source['sha256']
    recipe=read_json(ROOT/'configs/phase6/curriculum_strategy.json');tokpath=ROOT/recipe['tokenizer'];assert sha256(tokpath)==recipe['tokenizer_sha256']
    binding=dict(source_pin_sha256=sha256(ROOT/'reports/phase6/aozora_source_pin.json'),web_corpus_sha256=sha256(WEB/'curriculum.jsonl'),
        tokenizer_sha256=recipe['tokenizer_sha256'],train_targets=dict(literary=3000000,explanation=7000000),
        dev_targets=dict(literary=150000,explanation=350000),maximum_per_work_units=16,
        source_sha256={p:sha256(ROOT/p) for p in ('scripts/prepare_literary_curriculum.py','src/jmicro/literary_curriculum.py','src/jmicro/realistic_curriculum.py','src/jmicro/realistic_curriculum_v2.py')},
        download_budget_seconds=300,CPU_budget_seconds=600,workers=8,seed=2026100602,protected_test_used=False)
    start=time.monotonic();cpu_start=[None];totals=Counter();counts=Counter();job=dict(status='running',**identity(),binding=binding,started_at=now())
    def check():
        if time.monotonic()-start>900:raise TimeoutError('900s download+CPU budget exhausted')
        if cpu_start[0] is not None and time.monotonic()-cpu_start[0]>600:raise TimeoutError('600s CPU preparation budget exhausted')
    def heartbeat(stage):
        check();job.update(stage=stage,heartbeat_at=now(),seconds=time.monotonic()-start,counts=dict(counts),tokens=dict(totals));atomic_json(jobpath,job)
    streams={};corpus=None
    try:
        heartbeat('download')
        raw=Path(hf_hub_download(pin['repository'],source['path'],repo_type='dataset',revision=pin['revision'],token=False,local_dir=DATA/'raw'))
        assert raw.stat().st_size==source['size'] and sha256(raw)==source['sha256']
        assert time.monotonic()-start<=300
        cpu_start[0]=time.monotonic();heartbeat('source_verified')
        tok=Tokenizer(tokpath);pool=DATA/'shards';pool.mkdir();index={s:[] for s in ('train','dev','test')};offsets=Counter();records=[]
        seen=set();heads=set();works=Counter();families={'train':set(),'dev':set()}
        streams={s:(pool/(s+'.bin')).open('wb',buffering=1024*1024) for s in index}
        corpus=(DATA/'curriculum.jsonl').open('w',encoding='utf-8',buffering=1024*1024)
        protected=[v for name in ('eval/base.jsonl','eval/japanese_semantics_v2_1.jsonl') for line in (ROOT/name).read_text().splitlines() for k,v in json.loads(line).items() if k in ('prefix','context') and isinstance(v,str) and len(v)>=12]
        def accept(unit,split,group):
            target=binding['train_targets' if split=='train' else 'dev_targets'][group]
            if totals[split+'_'+group]>=target:return
            if unit['canonical_sha256'] in seen or unit['first_sentence_sha256'] in heads:return
            if any(p in unit['text'] for p in protected):return
            family=unit['source_family'];other='dev' if split=='train' else 'train';assert family not in families[other]
            ids=unit.pop('ids');packed=np.asarray([2,*ids,3],dtype='<u2');offset=offsets[split];offsets[split]+=len(packed)
            rec=dict(unit,id='literary-mix-'+unit['canonical_sha256'][:20],doc_id='literary-mix-'+unit['canonical_sha256'][:20],
                kind='web',bucket=group,group=group,split=split,body_tokens=len(ids))
            row=dict(doc_id=rec['doc_id'],split=split,kind='web',bucket=group,canonical_sha256=unit['canonical_sha256'],
                offset=offset,body_tokens=len(ids),bytes=len(unit['text'].encode()),source_family=family)
            streams[split].write(packed.tobytes());index[split].append(row);corpus.write(json.dumps(rec,ensure_ascii=False)+'\n');records.append(rec)
            seen.add(unit['canonical_sha256']);heads.add(unit['first_sentence_sha256']);families[split].add(family);totals[split+'_'+group]+=len(packed)
        # Reuse already extracted accepted whole-source explanations, no2B rescan.
        with (WEB/'curriculum.jsonl').open() as inp:
            for line in inp:
                r=json.loads(line)
                if r['group']!='explanation':continue
                r['ids']=tok.encode(r['text']);accept(r,r['split'],'explanation')
        heartbeat('Web_reused')
        def books():
            with gzip.open(raw,'rt',encoding='utf-8') as inp:
                for line in inp:
                    check();r=json.loads(line);counts['books_read']+=1
                    if r['meta'].get('文字遣い種別')=='新字新仮名' and r['meta'].get('作品著作権フラグ')=='なし':yield r
        with mp.get_context('fork').Pool(8,initializer=initialize,initargs=(str(tokpath),)) as workers:
            for units in workers.imap(process,books(),chunksize=1):
                check()
                for unit in units:
                    family=unit['source_family'];split='dev' if int(hashlib.sha256(family.encode()).hexdigest()[:8],16)%20==0 else 'train'
                    accept(unit,split,'literary')
                if len(records)//1000>counts.get('reported_thousands',0):counts['reported_thousands']=len(records)//1000;heartbeat('literary_extract')
                if all(totals[s+'_literary']>=binding['train_targets' if s=='train' else 'dev_targets']['literary'] for s in ('train','dev')):break
            workers.terminate()
        for stream in streams.values():stream.flush();os.fsync(stream.fileno());stream.close()
        corpus.flush();os.fsync(corpus.fileno());corpus.close();heartbeat('supply')
        assert all(totals[s+'_'+g]>=n for s,t in [('train',binding['train_targets']),('dev',binding['dev_targets'])] for g,n in t.items()),dict(totals)
        assert not families['train']&families['dev']
        write_json(pool/'token_bytes.json',[0 if i<8 else len(tok.decode_bytes([i])) for i in range(tok.vocab_size)])
        manifest=dict(version=1,dtype='<u2',kind='web',corpus_sha256=sha256(DATA/'curriculum.jsonl'),tokenizer_sha256=recipe['tokenizer_sha256'],
            vocab_size=tok.vocab_size,packing='BOS/body/EOS; causal across documents; BOS masked',token_bytes_sha256=sha256(pool/'token_bytes.json'),splits={})
        for s,rows in index.items():
            write_json(pool/(s+'.index.json'),rows)
            manifest['splits'][s]=dict(tokens=offsets[s],documents=len(rows),body_bytes=sum(r['bytes'] for r in rows),stream_sha256=sha256(pool/(s+'.bin')),index_sha256=sha256(pool/(s+'.index.json')))
        write_json(pool/'manifest.json',manifest);rng=random.Random(binding['seed']);sample=[];dev=[]
        for group in ('literary','explanation'):
            sample.extend(rng.sample([r for r in records if r['split']=='train' and r['group']==group],32))
            dev.extend(rng.sample([r for r in records if r['split']=='dev' and r['group']==group],16))
        write_json(DATA/'sample64.json',sample);write_json(DATA/'dev32.json',dev)
        ready=dict(status='prepared_pending_content_review',binding=binding,pool=str(pool),manifest_sha256=sha256(pool/'manifest.json'),splits=manifest['splits'],
            sample_sha256=sha256(DATA/'sample64.json'),dev32_sha256=sha256(DATA/'dev32.json'),tokens_by_group=dict(totals),
            sources=dict(literary=pin,Web=read_json(ROOT/'configs/phase6/corpus_10b.json')),
            editorial='Whole literary paragraphs, whole Web EOS parents; wording retained; no synthetic generation/name variants',
            audit='Local exact/first-sentence matching; literary author family and Web original-parent family splits; cross-original-corpus/site-author near-duplicate audit incomplete',
            limitations='New orthography does not ensure present-day vocabulary or realistic events; source/genre/length/EOS composition changes, not amount-only experiment',
            seconds=time.monotonic()-start,CPU_seconds=time.monotonic()-cpu_start[0],protected_test_used=False,created_at=now())
        write_json(DATA/'ready.json',ready);write_json(RUN/'ready.json',ready);heartbeat('complete');job.update(status='complete',completed_at=now());print(json.dumps(ready,ensure_ascii=False),flush=True)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        for stream in streams.values():
            if not stream.closed:stream.close()
        if corpus and not corpus.closed:corpus.close()
        job['seconds']=time.monotonic()-start;atomic_json(jobpath,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);prepare()
