"""Prepare a finite literal story/diary pool, preserving both failed Web attempts."""
import argparse
from collections import Counter
import json
from pathlib import Path
import random
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from jmicro.narrative_diversity import candidate
from jmicro.complete_units import unit_hash
from jmicro.evaluation import canonicalize_text
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.shards import build_shards
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity,alive

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/narrative-diversity-v2-20261005')
RUN=ROOT/'reports/phase6/narrative-diversity-v2-20261005'
SEED=202610077


def prepare(expand=False):
    base=read_json(ROOT/'configs/phase6/natural_learning.json');story=read_json(ROOT/'configs/phase6/amount_story_study.json')['pool']
    sources=dict(story=dict(directory=story['pool'],manifest_sha256=story['manifest_sha256']),web=dict(directory='/home/aihub_ubuntu/jmicro-data/phase6/complete-documents-20261005/shards',manifest_sha256='2d7b3d0b21fa9267c8f3bf8121f1a156f68f843c9676c2b2b004b01ab77d30de'))
    stage='growth' if expand else 'initial';targets=dict(story=49000,web=1000) if expand else dict(story=9000,web=1000)
    DATA.mkdir(parents=True,exist_ok=True);RUN.mkdir(parents=True,exist_ok=True);path=RUN/('prepare-'+stage+'-job.json')
    binding=dict(sources=sources,targets=targets,seed=SEED,selector_sha256=sha256(ROOT/'src/jmicro/narrative_diversity.py'),builder_sha256=sha256(Path(__file__)),contract_sha256=sha256(ROOT/'docs/78_narrative_supply_execution.md'),CPU_budget_seconds=600,max_index_rows_per_source=600000)
    if path.exists():
        previous=read_json(path);assert not alive(previous) and previous['binding']==binding
        if previous['status']=='complete':print('Completed preparation retained');return
        raise RuntimeError('Preserved incomplete preparation requires diagnosis')
    if expand:assert read_json(RUN/'review.json')['eligible_for_expansion']
    start=time.monotonic();job=dict(status='running',**identity(),binding=binding,started_at=now());counts=Counter()
    def heartbeat(stage):
        if time.monotonic()-start>600:raise TimeoutError('600s preparation budget exhausted')
        job.update(stage=stage,counts=dict(counts),seconds=time.monotonic()-start,heartbeat_at=now());atomic_json(path,job)
    records=[];seen=set();heads=set();totals=Counter();next_bytes={}
    for folder in ('diverse-learning-20261005','diverse-learning-v2-20261005'):
        seen.update(r['canonical_sha256'] for r in read_json(DATA.parent/folder/'sample-initial.json'))
    if expand:
        records=[json.loads(line) for line in (DATA/'candidate.jsonl').read_text().splitlines() if json.loads(line)['split']=='train']
        seen.update(r['canonical_sha256'] for r in records);heads.update(r['first_sentence_hash'] for r in records);totals.update(r['source'] for r in records)
        prior=read_json(DATA/'ready-initial.json')['next_index_bytes']
    else:prior={}
    try:
        heartbeat('setup');tok=Tokenizer(ROOT/base['tokenizer']);assert sha256(tok.path)==base['tokenizer_sha256']
        protected=[]
        for p in (ROOT/'eval/base.jsonl',ROOT/'eval/japanese_semantics_v2_1.jsonl'):
            for line in p.read_text().splitlines():
                r=json.loads(line);protected.extend(v for k,v in r.items() if k in ('prefix','context') and isinstance(v,str) and len(v)>12)
        for source,entry in sources.items():
            directory=Path(entry['directory']);assert sha256(directory/'manifest.json')==entry['manifest_sha256']
            tokens=np.memmap(directory/'train.bin',dtype='<u2',mode='r')
            with (directory/'train.index.jsonl').open('rb') as stream:
                stream.seek(prior.get(source,0))
                while line:=stream.readline():
                    counts[source+'_index_rows']+=1
                    if counts[source+'_index_rows']>600000:break
                    row=json.loads(line)
                    if source=='web' and row['source']!='web':continue
                    if not (100<=row['body_tokens']<=128 if source=='story' else 64<=row['body_tokens']<=256):continue
                    ids=tokens[row['offset']+1:row['offset']+1+row['body_tokens']].tolist();text=tok.decode_bytes(ids).decode('utf-8')
                    unit=candidate(text,row['body_tokens'],source)
                    if not unit:continue
                    digest=unit_hash(text)
                    if digest in seen or unit['first_sentence_hash'] in heads or any(p in text for p in protected):continue
                    text=canonicalize_text(text);seen.add(digest);heads.add(unit['first_sentence_hash'])
                    r=dict(doc_id='narrative-'+digest[:16],id='narrative-'+digest[:16],kind='web',split='train',bucket='literal-'+source,
                        text=text,canonical_sha256=digest,source=source,source_manifest=entry['manifest_sha256'],
                        origin_offset=row['offset'],source_metadata=row,body_tokens=row['body_tokens'],structure='declarative',
                        first_sentence_hash=unit['first_sentence_hash'],sentences=unit['sentences'],ending_style=unit['ending_style'])
                    records.append(r);totals[source]+=1;counts['accepted']=len(records)
                    if len(records)%1000==0:heartbeat(source);print(json.dumps(dict(counts)),flush=True)
                    if totals[source]>=targets[source]:break
                next_bytes[source]=stream.tell()
            assert totals[source]==targets[source],f'Actual {source} supply{totals[source]}<{targets[source]}; no duplicate/name substitute'
        dev=read_json(DATA.parent/'diverse-learning-v2-20261005/dev64.json');assert len(dev)==64 and not seen&{r['canonical_sha256'] for r in dev}
        write_json(DATA/'dev64.json',dev);label='expanded' if expand else 'candidate';corpus=DATA/(label+'.jsonl')
        corpus.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records+dev));heartbeat('shards')
        manifest=build_shards(corpus,tok.path,DATA/label)
        assert manifest['splits']['train']['tokens']>=(5000000 if expand else 1000000)
        sample=random.Random(SEED+(1 if expand else 0)).sample(records[10000:] if expand else records,64);write_json(DATA/('sample-'+stage+'.json'),sample)
        ready=dict(status='prepared_pending_content_review',binding=binding,pool=str(DATA/label),manifest_sha256=sha256(DATA/label/'manifest.json'),corpus_sha256=sha256(corpus),
            sample_sha256=sha256(DATA/('sample-'+stage+'.json')),splits=manifest['splits'],by_source=dict(totals),next_index_bytes=next_bytes,
            unique_first_sentences=len(heads),styles=dict(Counter(r['ending_style'] for r in records)),sentence_counts=dict(Counter(r['sentences'] for r in records)),
            dev_structures=dict(Counter(r['structure'] for r in dev)),literal_public_documents=True,independent_human_certification=False,
            overlap_audit='local exact and first sentence only; not whole old corpora',CPU_seconds=time.monotonic()-start,created_at=now())
        write_json(DATA/('ready-'+stage+'.json'),ready);write_json(RUN/('ready-'+stage+'.json'),ready);heartbeat('complete');job.update(status='complete',completed_at=now());print(json.dumps(ready,ensure_ascii=False),flush=True)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:job['seconds']=time.monotonic()-start;atomic_json(path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);p=argparse.ArgumentParser();p.add_argument('--expand',action='store_true');a=p.parse_args();prepare(a.expand)
