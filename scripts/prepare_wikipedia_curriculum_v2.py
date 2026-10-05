"""Bounded modern explanatory pilot; protected evaluation articles excluded."""
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
import pyarrow.parquet as pq
from huggingface_hub import hf_hub_download
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.wikipedia_curriculum import lead
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity,alive

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/wikipedia-curriculum-20261006-v2')
RUN=ROOT/'reports/phase6/wikipedia-curriculum-20261006-v2'
PRIOR=Path('/home/aihub_ubuntu/jmicro-data/phase6/wikipedia-curriculum-20261006')
PRIOR_RUN=ROOT/'reports/phase6/wikipedia-curriculum-20261006'
_TOK=None


def initialize(path):
    global _TOK
    _TOK=Tokenizer(Path(path))


def process(batch):
    return [unit for r in batch if (unit:=lead(r,_TOK)) is not None]


def prepare():
    DATA.mkdir(parents=True,exist_ok=True);RUN.mkdir(parents=True,exist_ok=True)
    jobpath=RUN/'prepare-job.json'
    if jobpath.exists():
        previous=read_json(jobpath);assert not alive(previous)
        if previous['status']=='complete':print('Completed material retained');return
        raise ValueError('Preserve failed run; inspect and revise, no identical retry')
    pin=read_json(ROOT/'reports/phase6/wikipedia_source_pin_v2.json');recipe=read_json(ROOT/'configs/phase6/curriculum_strategy.json')
    tokpath=ROOT/recipe['tokenizer'];assert sha256(tokpath)==recipe['tokenizer_sha256']
    evaluation=Path('/home/aihub_ubuntu/jmicro-data/evaluation-v2');m=read_json(evaluation/'manifest.json')
    old=read_json(PRIOR_RUN/'prepare-job.json')
    assert old['status']=='failed' and not alive(old) and old['stage']=='supply'
    assert old['binding']['source_sha256']['scripts/prepare_wikipedia_curriculum.py']==sha256(ROOT/'scripts/prepare_wikipedia_curriculum.py')
    protected_path=evaluation/'jsquad_dev.json';assert sha256(protected_path)==m['sources']['jsquad_dev']['sha256']
    protected_titles={r['title'] for r in read_json(protected_path)['data']}
    protected=[]
    for name in ('eval/base.jsonl','eval/japanese_semantics_v2_1.jsonl'):
        for line in (ROOT/name).read_text().splitlines():
            r=json.loads(line);protected.extend(v for k,v in r.items() if k in ('prefix','context') and isinstance(v,str) and len(v)>=12)
    binding=dict(source_pin_sha256=sha256(ROOT/'reports/phase6/wikipedia_source_pin_v2.json'),tokenizer_sha256=recipe['tokenizer_sha256'],
        previous_supply_job_sha256=sha256(PRIOR_RUN/'prepare-job.json'),previous_corpus_sha256=sha256(PRIOR/'curriculum.jsonl'),
        previous_binary_sha256={s:sha256(PRIOR/'shards'/(s+'.bin')) for s in ('train','dev')},
        targets=dict(train=10000000,dev=500000),workers=8,seed=2026100604,
        source_sha256={p:sha256(ROOT/p) for p in ('scripts/prepare_wikipedia_curriculum_v2.py','src/jmicro/wikipedia_curriculum.py','src/jmicro/realistic_curriculum.py','src/jmicro/realistic_curriculum_v2.py')},
        JSQuAD_protected_sha256=sha256(protected_path),JSQuAD_excluded_article_titles=sorted(protected_titles),
        maximum_raw_bytes=5000000000,maximum_files=15,download_budget_seconds=900,CPU_budget_seconds=600,
        scientific_comparison='Same fresh weights/tokenizer, controlv3 vs new10M explanations, each300M teachers in one continuous90stable/10decay path and200-update warmup at.002; source/genre/length/EOS changes are not amount-only',
        future_comparison_GPU_budget_seconds=1800,quality_criteria_unchanged=True,protected_test_evaluated=False)
    start=time.monotonic();cpu=[0.];downloads=[0.];totals=Counter();counts=Counter();job=dict(status='running',**identity(),binding=binding,started_at=now())
    streams={};corpus=None;files=[]
    def check():
        if time.monotonic()-start>1500:raise TimeoutError('1500s combined source preparation budget exhausted')
        if cpu[0]>600:raise TimeoutError('600s measured CPU preparation budget exhausted')
        if downloads[0]>900:raise TimeoutError('900s measured download budget exhausted')
    def heartbeat(stage):
        check();job.update(stage=stage,heartbeat_at=now(),seconds=time.monotonic()-start,CPU_seconds=cpu[0],download_seconds=downloads[0],counts=dict(counts),tokens=dict(totals));atomic_json(jobpath,job)
    try:
        heartbeat('setup');pool=DATA/'shards';pool.mkdir();tok=Tokenizer(tokpath);index={s:[] for s in ('train','dev','test')};records=[];seen=set();heads=set();families={'train':set(),'dev':set()}
        streams={s:(pool/(s+'.bin')).open('wb',buffering=1024*1024) for s in index};corpus=(DATA/'curriculum.jsonl').open('w',encoding='utf-8',buffering=1024*1024)
        def accept(unit):
            family=unit['source_family'];split='dev' if int(hashlib.sha256(family.encode()).hexdigest()[:8],16)%20==0 else 'train'
            if totals[split]>=binding['targets'][split]:return
            if unit['canonical_sha256'] in seen or unit['first_sentence_sha256'] in heads:return
            if any(p in unit['text'] for p in protected):counts['excluded_fixed_prefixes']+=1;return
            other='train' if split=='dev' else 'dev';assert family not in families[other]
            ids=unit.pop('ids');packed=np.asarray([2,*ids,3],dtype='<u2');offset=totals[split]
            r=dict(unit,id='wiki-pilot-'+unit['article_id'],doc_id='wiki-pilot-'+unit['article_id'],kind='web',bucket='encyclopedic',split=split,body_tokens=len(ids),
                source='wikipedia_ja_20231101',source_revision=pin['revision'],license=pin['license'])
            row=dict(doc_id=r['doc_id'],split=split,kind='web',bucket='encyclopedic',canonical_sha256=unit['canonical_sha256'],offset=offset,body_tokens=len(ids),bytes=len(unit['text'].encode()),source_family=family)
            streams[split].write(packed.tobytes());index[split].append(row);corpus.write(json.dumps(r,ensure_ascii=False)+'\n');records.append(r);totals[split]+=len(packed)
            seen.add(unit['canonical_sha256']);heads.add(unit['first_sentence_sha256']);families[split].add(family)
        # Copy verified accepted partial tokens; never re-run its4 parquet files.
        began=time.monotonic();positions=Counter();previous_tokens={s:np.memmap(PRIOR/'shards'/(s+'.bin'),dtype='<u2',mode='r') for s in ('train','dev')}
        with (PRIOR/'curriculum.jsonl').open() as inp:
            for line in inp:
                r=json.loads(line);split=r['split'];position=positions[split];size=r['body_tokens']
                packed=previous_tokens[split][position:position+size+2]
                assert len(packed)==size+2 and packed[0]==2 and packed[-1]==3
                r['ids']=packed[1:-1].tolist();positions[split]+=size+2;accept(r)
        assert dict(totals)==old['tokens']==dict(positions)
        cpu[0]+=time.monotonic()-began;counts.update(old['counts']);files.extend(pin['files'][:4])
        downloaded=sum(f['size'] for f in files);heartbeat('prior_partial_reused')
        for f in pin['files'][4:15]:
            if all(totals[s]>=n for s,n in binding['targets'].items()):break
            assert f['sha256'] and downloaded+f['size']<=binding['maximum_raw_bytes']
            heartbeat('download-'+f['path']);began=time.monotonic()
            path=Path(hf_hub_download(pin['repository'],f['path'],repo_type='dataset',revision=pin['revision'],token=False,local_dir=DATA/'raw'))
            downloads[0]+=time.monotonic()-began;check();assert path.stat().st_size==f['size'] and sha256(path)==f['sha256'];downloaded+=f['size'];files.append(f)
            began=time.monotonic()
            def batches():
                for batch in pq.ParquetFile(path).iter_batches(batch_size=128,columns=['id','url','title','text']):
                    selected=[]
                    for r in batch.to_pylist():
                        counts['source_articles']+=1
                        if r['title'] in protected_titles:counts['excluded_JSQuAD_articles']+=1;continue
                        selected.append(r)
                    if selected:yield selected
            with mp.get_context('fork').Pool(8,initializer=initialize,initargs=(str(tokpath),)) as workers:
                for units in workers.imap(process,batches(),chunksize=1):
                    check()
                    for unit in units:accept(unit)
                    if len(records)//1000>counts.get('reported_thousands',0):
                        counts['reported_thousands']=len(records)//1000;cpu_now=time.monotonic()-began
                        job.update(CPU_seconds=cpu[0]+cpu_now);heartbeat('extract')
                    if time.monotonic()-began+cpu[0]>600:raise TimeoutError('600s measured CPU preparation budget exhausted')
                    if all(totals[s]>=n for s,n in binding['targets'].items()):break
                workers.terminate()
            cpu[0]+=time.monotonic()-began;heartbeat('file_complete')
        for stream in streams.values():stream.flush();os.fsync(stream.fileno());stream.close()
        corpus.flush();os.fsync(corpus.fileno());corpus.close();heartbeat('supply')
        assert all(totals[s]>=n for s,n in binding['targets'].items()),dict(totals)
        assert not families['train']&families['dev']
        write_json(pool/'token_bytes.json',[0 if i<8 else len(tok.decode_bytes([i])) for i in range(tok.vocab_size)])
        manifest=dict(version=1,dtype='<u2',kind='web',corpus_sha256=sha256(DATA/'curriculum.jsonl'),tokenizer_sha256=recipe['tokenizer_sha256'],vocab_size=tok.vocab_size,
            packing='BOS/whole opening paragraphs/EOS; causal across documents; BOS masked',token_bytes_sha256=sha256(pool/'token_bytes.json'),splits={})
        for split,rows in index.items():
            write_json(pool/(split+'.index.json'),rows)
            manifest['splits'][split]=dict(tokens=totals[split],documents=len(rows),body_bytes=sum(r['bytes'] for r in rows),stream_sha256=sha256(pool/(split+'.bin')),index_sha256=sha256(pool/(split+'.index.json')))
        write_json(pool/'manifest.json',manifest);rng=random.Random(binding['seed']);sample=rng.sample([r for r in records if r['split']=='train'],64);dev=rng.sample([r for r in records if r['split']=='dev'],32)
        write_json(DATA/'sample64.json',sample);write_json(DATA/'dev32.json',dev)
        ready=dict(status='prepared_pending_content_review',binding=binding,pool=str(pool),manifest_sha256=sha256(pool/'manifest.json'),splits=manifest['splits'],
            sample_sha256=sha256(DATA/'sample64.json'),dev32_sha256=sha256(DATA/'dev32.json'),source_files=files,source_pin=pin,
            preparation_seconds=time.monotonic()-start,CPU_seconds=cpu[0],download_seconds=downloads[0],raw_bytes=downloaded,
            audit='Local exact and first-sentence, article-family split and JSQuAD article exclusion; old-Web cross-corpus/site-author near-duplicate audit incomplete',
            limitations='Encyclopedic explanations instead of everyday narrative; no current factual certification, no amount-only claim, no independent human blind review',
            protected_test_used=False,created_at=now())
        write_json(DATA/'ready.json',ready);write_json(RUN/'ready.json',ready);heartbeat('complete');job.update(status='complete',completed_at=now());print(json.dumps(ready,ensure_ascii=False),flush=True)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:
        for stream in streams.values():
            if not stream.closed:stream.close()
        if corpus and not corpus.closed:corpus.close()
        job['seconds']=time.monotonic()-start;atomic_json(jobpath,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);prepare()
