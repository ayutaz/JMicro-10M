"""Conditional train-only story expansion; pin existing source, disclose any pool repetition."""
import hashlib
import json
import os
from pathlib import Path
import sys
import time
from collections import Counter
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import pyarrow.parquet as pq
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.training import atomic_json
from jmicro.complete_units import unit_hash
from jmicro.tokenizer import Tokenizer
from phase6_performance import identity,alive
from prepare_story_text import story_candidate,download
import run_story20_low_lr as screen

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-budget-20261005')
POOL=DATA/'shards'
TARGET=120000000
BUDGET=1800


def main():
    assert sys.version_info[:3]==(3,12,7)
    config=screen.load_config();full=read_json(screen.RUN/'full/review.json')
    assert full['status']=='passed' and all(full['checks'].values()) and full['candidate_passes_all_full_conditions'],'Full entry gates required before new pool'
    source=read_json(Path('/home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-20261004/source.json'))
    binding=dict(screen_config_sha256=sha256(screen.CONFIG),full_review_sha256=sha256(screen.RUN/'full/review.json'),
                 source=source,target_tokens=TARGET,source_sha256=sha256(Path(__file__)))
    DATA.mkdir(parents=True,exist_ok=True);POOL.mkdir(parents=True,exist_ok=True)
    path=DATA/'job.json';old=read_json(path) if path.exists() else {}
    if old:
        assert old['binding']==binding and not alive(old),'Existing live or different builder'
        if old['status']=='complete':
            ready=read_json(POOL/'ready.json');assert sha256(POOL/'manifest.json')==ready['manifest_sha256']
            print(json.dumps(ready));return
    started=time.monotonic();prior=old.get('elapsed_seconds',0)
    job=dict(status='running',**identity(),binding=binding,started_at=now(),elapsed_seconds=prior)
    def heartbeat():
        job.update(elapsed_seconds=prior+time.monotonic()-started,heartbeat_at=now(),counts=dict(counts))
        atomic_json(path,job)
        if job['elapsed_seconds']>BUDGET:raise TimeoutError('Cumulative story preparation budget exhausted')
    counts=Counter();hist=Counter();seen=set();parents=set();samples=[];sample_files=Counter();aux=[];files=[]
    tok=Tokenizer(ROOT/config['tokenizer']);protected=set()
    for suite in (ROOT/'eval/base.jsonl',ROOT/'eval/japanese_semantics_v2_1.jsonl'):
        for line in suite.read_text().splitlines():
            row=json.loads(line);protected.update(unit_hash(row[k]) for k in ('prefix','context') if row.get(k))
            protected.update(unit_hash(v) for v in row.get('choices',[]))
    try:
        heartbeat()
        with (POOL/'train.partial.bin').open('wb') as stream,(POOL/'train.index.partial.jsonl').open('w') as index:
            for item in source['files']:
                source_path,digest=download(source,item);files.append(dict(path=item['path'],sha256=digest,bytes=item['bytes']))
                local_row=0
                for batch in pq.ParquetFile(source_path).iter_batches(batch_size=1024):
                    heartbeat()
                    for record in batch.to_pylist():
                        row_number=local_row;local_row+=1;counts['source_rows']+=1
                        if 'クリフハンガー' in record.get('feature','') or '超現実' in record.get('style',''):continue
                        unit=story_candidate(record['story'],tok)
                        if not unit:continue
                        if unit['text_sha256'] in protected:counts['protected_exact_excluded']+=1;continue
                        if unit['text_sha256'] in seen:counts['local_duplicates_excluded']+=1;continue
                        seen.add(unit['text_sha256']);parent=record['generation_id'].rsplit('-',1)[0]
                        if int(hashlib.sha256(parent.encode()).hexdigest()[:8],16)%100==0:
                            if len(aux)<100:aux.append(dict(parent=parent,generation_id=record['generation_id'],text=unit['text']))
                            continue
                        parents.add(parent);size=len(unit['ids']);byte_count=len(unit['text'].encode())
                        stream.write(np.asarray([2,*unit['ids'],3],dtype='<u2').tobytes())
                        metadata=dict(generation_id=record['generation_id'],parent_id=parent,source_file=item['path'],source_row=row_number,
                                      offset=counts['tokens'],body_tokens=size,bytes=byte_count,sentences=unit['sentences'],text_sha256=unit['text_sha256'],split='train')
                        index.write(json.dumps(metadata,ensure_ascii=False)+'\n')
                        counts.update(tokens=size+2,documents=1,body_bytes=byte_count);hist[size]+=1
                        if sample_files[item['path']]<10:
                            samples.append(dict(metadata,text=unit['text']));sample_files[item['path']]+=1
                        if counts['tokens']>=TARGET:break
                    if counts['tokens']>=TARGET:break
                if counts['tokens']>=TARGET:break
            for handle in (stream,index):handle.flush();os.fsync(handle.fileno())
        assert counts['tokens']>=25000000,'Insufficient accepted source; keep partials and exact blocker'
        os.replace(POOL/'train.partial.bin',POOL/'train.bin');os.replace(POOL/'train.index.partial.jsonl',POOL/'train.index.jsonl')
        lengths=[0 if i<8 else len(tok.decode_bytes([i])) for i in range(4096)];write_json(POOL/'token_bytes.json',lengths)
        manifest=dict(version=1,dtype='<u2',kind='web',vocab_size=4096,tokenizer_sha256=sha256(tok.path),
                      token_bytes_sha256=sha256(POOL/'token_bytes.json'),source=source,files_used=files,
                      packing='BOS/full naturally finished source story/EOS; no slicing or token truncation',
                      selection='same whole2–8sentences/body32–128/resolved end/low repetition/family1percent auxiliary holdout',
                      selection_source_sha256=sha256(ROOT/'scripts/prepare_story_text.py'),builder_source_sha256=sha256(Path(__file__)),
                      splits={'train':dict(tokens=counts['tokens'],documents=counts['documents'],body_bytes=counts['body_bytes'],
                                          stream_sha256=sha256(POOL/'train.bin'),index_sha256=sha256(POOL/'train.index.jsonl'),index_format='jsonl')})
        write_json(POOL/'manifest.json',manifest);write_json(POOL/'samples.json',samples)
        write_json(POOL/'auxiliary-dev.json',dict(split='supplemental-dev',not_used_for_candidate_selection=True,rows=aux))
        ready=dict(status='ready_pending_content_inspection',binding=binding,manifest_sha256=sha256(POOL/'manifest.json'),totals=dict(counts),
                   parent_documents=len(parents),body_tokens_mean=sum(k*v for k,v in hist.items())/counts['documents'],
                   target_tokens=TARGET,target_reached=counts['tokens']>=TARGET,source_exhausted=counts['tokens']<TARGET,
                   source_train_only=True,parent_split_disjoint=True,source_overlap_with_Web='unknown',independent_human_certification=False,
                   planned500M_story_tokens=99975168,expected_story_exposure_ratio=99975168/counts['tokens'],
                   repetition_policy='Explicit deterministic BlockSampler epoch reuse if source exhausted; not new unique data',
                   seconds=prior+time.monotonic()-started)
        write_json(POOL/'ready.json',ready);heartbeat();job.update(status='complete',completed_at=now())
        print(json.dumps(ready,ensure_ascii=False),flush=True)
    except BaseException as error:
        job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        job['elapsed_seconds']=prior+time.monotonic()-started;atomic_json(path,job)


if __name__=='__main__':main()
