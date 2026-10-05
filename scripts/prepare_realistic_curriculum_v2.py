"""WSL-only bounded parallel extraction from accepted Web train; literal10M."""
import argparse
from collections import Counter
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
from jmicro.realistic_curriculum_v2 import literal_units
from jmicro.eos_pilot import TrainView,spans
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity,alive
import prepare_complete_units as decode

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/realistic-curriculum-20261006-v2')
RUN=ROOT/'reports/phase6/realistic-curriculum-20261006-v2'


def process(batch):
    results=[]
    for start,end in batch:
        ids=decode._TRAIN[start+1:end].tolist()
        if not ids or any(i<8 for i in ids):continue
        try:text=b''.join(decode._PIECES[i] for i in ids).decode('utf-8')
        except UnicodeDecodeError:continue
        for unit in literal_units(text,decode._TOK):
            results.append(dict(unit,source_start=start,source_end=end))
    return results


def batches(view,counts,check,max_scan):
    previous=-1;batch=[]
    for offset in range(0,min(max_scan,len(view.tokens)),4000000):
        check();chunk=view.tokens[offset:min(offset+4000000,max_scan,len(view.tokens))]
        starts,ends,previous=spans(chunk,offset,previous);counts['scanned_tokens']=offset+len(chunk)
        for a,b in zip(starts,ends):
            if 64<=b-a-1<=4096:
                batch.append((int(a),int(b)))
                if len(batch)==64:yield batch;batch=[]
    if batch:yield batch


def prepare():
    c=read_json(ROOT/'configs/phase6/curriculum_strategy.json')
    provenance=read_json(ROOT/'configs/phase6/corpus_10b.json')
    DATA.mkdir(parents=True,exist_ok=True);RUN.mkdir(parents=True,exist_ok=True)
    path=RUN/'prepare-job.json'
    if path.exists():
        old=read_json(path);assert not alive(old)
        if old['status']=='complete':print('Prepared material retained');return
        raise ValueError('Retain failed material; revise into a separate directory')
    source=TrainView(c['web_shards'],c['web_manifest_sha256']);tok=Tokenizer(ROOT/c['tokenizer'])
    assert sha256(ROOT/c['tokenizer'])==c['tokenizer_sha256']
    targets=dict(daily=3000000,explanation=7000000);dev_targets={g:n//20 for g,n in targets.items()}
    binding=dict(source=c['web_shards'],source_manifest_sha256=c['web_manifest_sha256'],tokenizer_sha256=c['tokenizer_sha256'],
        targets=targets,dev_targets=dev_targets,max_source_tokens=2000000000,max_units_per_parent=1,
        CPU_budget_seconds=600,workers=8,seed=2026100601,selector_sha256=sha256(ROOT/'src/jmicro/realistic_curriculum_v2.py'),
        builder_sha256=sha256(Path(__file__)),protected_test_used=False,
        dependencies_sha256={p:sha256(ROOT/p) for p in ('src/jmicro/realistic_curriculum.py','src/jmicro/complete_units.py','scripts/prepare_complete_units.py')},
        provenance={k:provenance[k] for k in ('repository','revision','license','attribution','terms_url')})
    start=time.monotonic();counts=Counter();totals=Counter();job=dict(status='running',**identity(),binding=binding,started_at=now())
    def check():
        if time.monotonic()-start>600:raise TimeoutError('600s bounded preparation budget exhausted')
    def heartbeat(stage):
        check();job.update(stage=stage,heartbeat_at=now(),seconds=time.monotonic()-start,counts=dict(counts),tokens=dict(totals));atomic_json(path,job)
    heartbeat('setup')
    protected=[]
    for name in ('eval/base.jsonl','eval/japanese_semantics_v2_1.jsonl'):
        for line in (ROOT/name).read_text().splitlines():
            r=json.loads(line);protected.extend(v for k,v in r.items() if k in ('prefix','context') and isinstance(v,str) and len(v)>=12)
    pool=DATA/'shards';pool.mkdir();seen=set();heads=set();families=Counter();indexes={'train':[],'dev':[],'test':[]};records=[]
    streams={s:(pool/(s+'.bin')).open('wb',buffering=1024*1024) for s in indexes}
    corpus=(DATA/'curriculum.jsonl').open('w',encoding='utf-8',buffering=1024*1024)
    try:
        # Workers inherit uv's pinned interpreter; large reads/writes stay on ext4.
        with mp.get_context('fork').Pool(8,initializer=decode.worker_init,
                initargs=(str(ROOT/c['tokenizer']),str(source.directory/'train.bin'))) as workers:
            for units in workers.imap(process,batches(source,counts,check,binding['max_source_tokens']),chunksize=1):
                check()
                for unit in units:
                    family=str(unit['source_start']);split='dev' if int(hashlib.sha256(family.encode()).hexdigest()[:8],16)%20==0 else 'train'
                    group=unit['group'];target=(targets if split=='train' else dev_targets)[group]
                    if totals[split+'_'+group]>=target:continue
                    if unit['canonical_sha256'] in seen or unit['first_sentence_sha256'] in heads or families[family]>=1:continue
                    if any(p in unit['text'] for p in protected):continue
                    ids=unit.pop('ids');size=len(ids);packed=np.asarray([2,*ids,3],dtype='<u2')
                    offset=sum(r['body_tokens']+2 for r in indexes[split][-1:])+(indexes[split][-1]['offset'] if indexes[split] else 0)
                    record=dict(unit,id='realistic-'+unit['canonical_sha256'][:20],doc_id='realistic-'+unit['canonical_sha256'][:20],
                        kind='web',bucket=group,split=split,source_family=family,source='fineweb2_edu_ja',
                        body_tokens=size,source_previously_in_parent_training=True,source_manifest_sha256=c['web_manifest_sha256'])
                    row=dict(doc_id=record['doc_id'],split=split,kind='web',bucket=group,canonical_sha256=unit['canonical_sha256'],
                        offset=offset,body_tokens=size,bytes=len(unit['text'].encode()),source_family=family,
                        source_start=unit['source_start'],char_start=unit['char_start'],char_end=unit['char_end'])
                    streams[split].write(packed.tobytes());indexes[split].append(row);corpus.write(json.dumps(record,ensure_ascii=False)+'\n')
                    records.append(record);totals[split+'_'+group]+=size+2;seen.add(unit['canonical_sha256']);heads.add(unit['first_sentence_sha256']);families[family]+=1
                if len(records)//1000>counts.get('reported_thousands',0):counts['reported_thousands']=len(records)//1000;heartbeat('extract')
                if all(totals[s+'_'+g]>=n for s,t in [('train',targets),('dev',dev_targets)] for g,n in t.items()):break
            workers.terminate()
        for stream in streams.values():stream.flush();os.fsync(stream.fileno());stream.close()
        corpus.flush();os.fsync(corpus.fileno());corpus.close();heartbeat('supply')
        assert all(totals[s+'_'+g]>=n for s,t in [('train',targets),('dev',dev_targets)] for g,n in t.items()),dict(totals)
        assert not {r['source_family'] for r in records if r['split']=='train'} & {r['source_family'] for r in records if r['split']=='dev'}
        write_json(pool/'token_bytes.json',[0 if i<8 else len(tok.decode_bytes([i])) for i in range(tok.vocab_size)])
        manifest=dict(version=1,dtype='<u2',kind='web',corpus_sha256=sha256(DATA/'curriculum.jsonl'),tokenizer_sha256=c['tokenizer_sha256'],
            vocab_size=tok.vocab_size,packing='BOS/body/EOS; causal across documents; BOS masked',token_bytes_sha256=sha256(pool/'token_bytes.json'),splits={})
        for s,rows in indexes.items():
            write_json(pool/(s+'.index.json'),rows)
            manifest['splits'][s]=dict(tokens=sum(r['body_tokens']+2 for r in rows),documents=len(rows),body_bytes=sum(r['bytes'] for r in rows),
                stream_sha256=sha256(pool/(s+'.bin')),index_sha256=sha256(pool/(s+'.index.json')))
        write_json(pool/'manifest.json',manifest)
        rng=random.Random(2026100601);sample=[]
        for group,n in [('daily',32),('explanation',32)]:sample.extend(rng.sample([r for r in records if r['split']=='train' and r['group']==group],n))
        write_json(DATA/'sample64.json',sample);write_json(DATA/'dev32.json',rng.sample([r for r in records if r['split']=='dev'],32))
        report=dict(status='prepared_pending_content_review',binding=binding,pool=str(pool),manifest_sha256=sha256(pool/'manifest.json'),
            splits=manifest['splits'],sample_sha256=sha256(DATA/'sample64.json'),dev32_sha256=sha256(DATA/'dev32.json'),tokens_by_group=dict(totals),
            selection='Whole original EOS parents with2-6complete sentences; no middle extraction; max1 per parent, source offsets retained',
            audit='New local exact/first-sentence and same-parent split only; full old-corpus near duplicates/site-author audit incomplete',
            license=provenance['license'],source_revision=provenance['revision'],provenance=binding['provenance'],
            source_history='Only accepted Webtrain; auxiliary dev can be original10B-known but is held out for future fresh comparisons',
            CPU_seconds=time.monotonic()-start,protected_test_used=False,created_at=now())
        write_json(DATA/'ready.json',report);write_json(RUN/'ready.json',report);heartbeat('complete');job.update(status='complete',completed_at=now())
        print(json.dumps(report,ensure_ascii=False),flush=True)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        for stream in streams.values():
            if not stream.closed:stream.close()
        if not corpus.closed:corpus.close()
        job['seconds']=time.monotonic()-start;atomic_json(path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);prepare()
