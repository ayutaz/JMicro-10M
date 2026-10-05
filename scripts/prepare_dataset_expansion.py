"""Plan58 bounded200M expansion: retained stories plus new public translations."""
from collections import Counter
import hashlib
import json
import multiprocessing as mp
import os
from pathlib import Path
import random
import shutil
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from huggingface_hub import hf_hub_download
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.training import atomic_json
from jmicro.tokenizer import Tokenizer
from jmicro.complete_units import unit_hash
from jmicro.expanded_stories import translated_candidate
from phase6_performance import identity, alive
from probe_dataset_expansion_supply import DATA

POOL=DATA/'shards'
TARGET=200_000_000
BUDGET=1800
SEED=20261005
TOK=None

def initialize():
    global TOK
    TOK=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')

def worker(rows):
    accepted=[]
    for number, record in rows:
        family=record['text_hash']
        if int(family[:8],16)%100==0: continue
        result=translated_candidate(record['text_ja'],TOK)
        if result: accepted.append(dict(result, source_row=number, family=family))
    return accepted

def batches(path, check, counts):
    with path.open() as stream:
        batch=[]
        for number,line in enumerate(stream):
            batch.append((number,json.loads(line)))
            counts['new_rows_read']+=1
            if len(batch)==512:
                check();yield batch;batch=[]
        if batch: yield batch

def main():
    assert sys.version_info[:3]==(3,12,7)
    source=read_json(DATA/'supply.json')['sources']['shibatch/TinyStories-JA']
    assert source['license']=='cdla-sharing-1.0' and len(source['files'])==4
    base=read_json(ROOT/'configs/phase6/amount_story_study.json')
    original=Path(base['pool']['pool'])
    assert sha256(original/'manifest.json')==base['pool']['manifest_sha256']
    binding=dict(source={k:v for k,v in source.items() if k!='declared_notes'}, original_pool=base['pool'], target_tokens=TARGET,
        builder_sha256=sha256(Path(__file__)), selector_sha256=sha256(ROOT/'src/jmicro/expanded_stories.py'), budget_seconds=BUDGET, seed=SEED,
        scope='Retain all old whole stories; add distinct train translations, 32–512 body tokens,2–24 sentences,4gram repetition<=0.15')
    DATA.mkdir(parents=True,exist_ok=True);POOL.mkdir(parents=True,exist_ok=True)
    job_path=DATA/'prepare-job.json'
    if job_path.exists():
        previous=read_json(job_path);assert not alive(previous) and previous['binding']==binding
        if previous['status']=='complete': print(json.dumps(read_json(POOL/'ready.json')));return
        raise RuntimeError('Preserved incomplete preparation: inspect before choosing a different attempt')
    earlier=read_json(DATA/'supply.json')['seconds']+read_json(DATA/'source-inspection.json')['seconds']
    started=time.monotonic();counts=Counter();totals=Counter();hist=Counter();by_source={s:Counter() for s in ('retained','translation')}
    rng=random.Random(SEED);samples=[];seen=set();files=[]
    job=dict(status='running',**identity(),binding=binding,started_at=now())
    def check():
        if earlier+time.monotonic()-started>BUDGET: raise TimeoutError('1800s cumulative preparation exhausted; keep partials')
    def heartbeat(stage):
        check();job.update(stage=stage,heartbeat_at=now(),elapsed_seconds=earlier+time.monotonic()-started,
            totals=dict(totals),by_source={k:dict(v) for k,v in by_source.items()},counts=dict(counts))
        atomic_json(job_path,job)
        print(json.dumps({k:job[k] for k in ('stage','elapsed_seconds','totals','by_source')},ensure_ascii=False),flush=True)
    protected=set()
    for suite in (ROOT/'eval/base.jsonl',ROOT/'eval/japanese_semantics_v2_1.jsonl'):
        for line in suite.read_text().splitlines():
            row=json.loads(line)
            protected.update(unit_hash(row[k]) for k in ('prefix','context') if row.get(k))
            protected.update(unit_hash(v) for v in row.get('choices',[]))
    def append_record(record):
        size=record['body_tokens'];amount=dict(tokens=size+2,documents=1,body_bytes=record['bytes'])
        totals.update(amount);by_source[record['source']].update(amount);hist[size]+=1
        if len(samples)<40:samples.append(record)
        else:
            slot=rng.randrange(totals['documents'])
            if slot<40:samples[slot]=record
    try:
        heartbeat('copy-accepted-stories')
        shutil.copyfile(original/'train.bin',POOL/'train.partial.bin')
        with (POOL/'train.index.partial.jsonl').open('w') as index:
            for line in (original/'train.index.jsonl').open():
                record=json.loads(line);seen.add(record['text_sha256'])
                record.update(source='retained',original_manifest_sha256=base['pool']['manifest_sha256'])
                index.write(json.dumps(record,ensure_ascii=False)+'\n');append_record(record)
            heartbeat('new-translations')
            with (POOL/'train.partial.bin').open('ab') as stream:
                for item in source['files']:
                    check();path=Path(hf_hub_download(source['repository'],item['path'],repo_type='dataset',revision=source['revision'],token=False))
                    assert path.stat().st_size==item['bytes'] and sha256(path)==item['sha256']
                    files.append(item);last_report=time.monotonic()
                    with mp.get_context('fork').Pool(12,initializer=initialize) as pool:
                        for units in pool.imap(worker,batches(path,check,counts),chunksize=1):
                            check()
                            for unit in units:
                                if unit['text_sha256'] in protected:counts['protected_exact_excluded']+=1;continue
                                if unit['text_sha256'] in seen:counts['local_duplicates_excluded']+=1;continue
                                seen.add(unit['text_sha256']);ids=unit['ids']
                                record={k:v for k,v in unit.items() if k not in ('text','ids')}
                                record.update(source='translation',source_file=item['path'],source_revision=source['revision'],
                                    offset=totals['tokens'],body_tokens=len(ids),bytes=len(unit['text'].encode()),split='train')
                                stream.write(np.asarray([2,*ids,3],dtype='<u2').tobytes())
                                index.write(json.dumps(record,ensure_ascii=False)+'\n');append_record(record)
                                if totals['tokens']>=TARGET:break
                            if time.monotonic()-last_report>10:heartbeat(item['path']);last_report=time.monotonic()
                            if totals['tokens']>=TARGET:break
                    heartbeat(item['path']+'-done')
                    if totals['tokens']>=TARGET:break
                stream.flush();os.fsync(stream.fileno())
            index.flush();os.fsync(index.fileno())
        assert totals['tokens']>=TARGET,'200M supply not met; do not launch GPU'
        os.replace(POOL/'train.partial.bin',POOL/'train.bin');os.replace(POOL/'train.index.partial.jsonl',POOL/'train.index.jsonl')
        shutil.copyfile(original/'token_bytes.json',POOL/'token_bytes.json')
        initialize();view=np.memmap(POOL/'train.bin',dtype='<u2',mode='r')
        samples=[dict(r,text=TOK.decode_bytes(view[r['offset']+1:r['offset']+1+r['body_tokens']].tolist()).decode('utf-8').strip()) for r in samples]
        original_ready=read_json(original/'ready.json')
        manifest=dict(version=1,dtype='<u2',kind='web',vocab_size=4096,tokenizer_sha256=base['tokenizer_sha256'],
            token_bytes_sha256=sha256(POOL/'token_bytes.json'),binding=binding,files_used=files,
            packing='BOS/whole original source story/EOS; no slicing or truncation',
            splits={'train':dict(totals,stream_sha256=sha256(POOL/'train.bin'),index_sha256=sha256(POOL/'train.index.jsonl'),index_format='jsonl')})
        write_json(POOL/'manifest.json',manifest);write_json(POOL/'samples.json',dict(seed=SEED,method='uniform reservoir over all retained and accepted new train stories',rows=samples))
        mean=(totals['tokens']-2*totals['documents'])/totals['documents'];old_mean=original_ready['body_tokens_mean']
        density=1000*totals['documents']/totals['tokens'];old_density=1000*original_ready['totals']['documents']/original_ready['totals']['tokens']
        ready=dict(status='ready_pending_content_inspection',manifest_sha256=sha256(POOL/'manifest.json'),binding=binding,
            totals=dict(totals),by_source={k:dict(v) for k,v in by_source.items()},histogram=dict(hist),files_used=files,scan=dict(counts),
            body_tokens_mean=mean,old_body_tokens_mean=old_mean,EOS_per_1000_tokens=density,old_EOS_per_1000_tokens=old_density,
            length_and_EOS_density_within5percent=abs(mean/old_mean-1)<=.05 and abs(density/old_density-1)<=.05,
            expected_short_exposure=199950336/totals['tokens'],source_train_only=True,whole_original_documents=True,
            copied_old_tokens=by_source['retained']['tokens'],new_source_tokens=by_source['translation']['tokens'],
            new_source_family_holdout_percent=1,official_validation_test_acquired=False,
            independent_unique_and_overlap_audit='not performed; local exact exclusion only; source is new to this project, broader corpus overlap unknown',
            independent_human_certification=False,seconds=earlier+time.monotonic()-started)
        write_json(POOL/'ready.json',ready);heartbeat('complete');job.update(status='complete',completed_at=now())
        print(json.dumps(ready,ensure_ascii=False),flush=True)
    except BaseException as error:
        job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        job['elapsed_seconds']=earlier+time.monotonic()-started;atomic_json(job_path,job)

if __name__=='__main__':main()
