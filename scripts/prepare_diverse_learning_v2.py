"""Bounded reuse of actual whole train texts; no corpus audit or GPU use."""
import argparse
from collections import Counter
import json
from pathlib import Path
import random
import sys
import time
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from jmicro.diverse_text import structure
from jmicro.diverse_text_v2 import candidate
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.evaluation import canonicalize_text
from jmicro.complete_units import unit_hash
from jmicro.shards import build_shards
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from phase6_performance import identity,alive

DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/diverse-learning-v2-20261005')
RUN=ROOT/'reports/phase6/diverse-learning-v2-20261005'
ORIGIN=Path('/home/aihub_ubuntu/jmicro-data/phase6/complete-documents-20261005/shards')
SEED=202610076


def prepare(expand=False):
    base=read_json(ROOT/'configs/phase6/natural_learning.json');origin=read_json(ORIGIN/'manifest.json')
    assert sha256(ORIGIN/'manifest.json')=='2d7b3d0b21fa9267c8f3bf8121f1a156f68f843c9676c2b2b004b01ab77d30de'
    DATA.mkdir(parents=True,exist_ok=True);RUN.mkdir(parents=True,exist_ok=True)
    stage='growth' if expand else 'initial';job_path=RUN/('prepare-'+stage+'-job.json')
    binding=dict(source_manifest=sha256(ORIGIN/'manifest.json'),selector_sha256=sha256(ROOT/'src/jmicro/diverse_text_v2.py'),
        builder_sha256=sha256(Path(__file__)),contract_sha256=sha256(ROOT/'docs/76_diverse_preparation_repair.md'),seed=SEED,
        target_documents=50000 if expand else 10000,max_Web_documents=300000,CPU_budget_seconds=600)
    if job_path.exists():
        old=read_json(job_path);assert not alive(old) and old['binding']==binding
        if old['status']=='complete':print('Completed preparation retained');return
        raise RuntimeError('Inspect preserved incomplete preparation; never redraw')
    if expand:assert read_json(RUN/'review.json')['eligible_for_expansion']
    start=time.monotonic();job=dict(status='running',**identity(),binding=binding,started_at=now());counts=Counter()
    def heartbeat(stage):
        if time.monotonic()-start>600:raise TimeoutError('Frozen600s preparation budget exhausted')
        job.update(stage=stage,counts=dict(counts),seconds=time.monotonic()-start,heartbeat_at=now());atomic_json(job_path,job)
    def record(row,text,unit,split):
        text=canonicalize_text(text);digest=unit_hash(text)
        return dict(doc_id='diverse-'+split+'-'+digest[:16],id='diverse-'+split+'-'+digest[:16],kind='web',split=split,
            bucket='diverse-whole-Web',text=text,canonical_sha256=digest,source_span=[row.get('source_start',row['offset']),row.get('source_end',row['offset']+row['body_tokens']+1)],
            source_manifest=binding['source_manifest'] if split=='train' else base['dev_manifest_sha256'],
            body_tokens=row['body_tokens'],structure=unit['structure'],sentences=unit['sentences'],ending_style=unit['ending_style'],
            first_sentence_hash=unit['first_sentence_hash'],linked_transitions=unit['linked_transitions'])
    try:
        heartbeat('setup');tok=Tokenizer(ROOT/base['tokenizer']);assert sha256(tok.path)==base['tokenizer_sha256']
        protected=[]
        for p in (ROOT/'eval/base.jsonl',ROOT/'eval/japanese_semantics_v2_1.jsonl'):
            for line in p.read_text().splitlines():
                r=json.loads(line);protected.extend(v for k,v in r.items() if k in ('prefix','context') and isinstance(v,str) and len(v)>12)
        tokens=np.memmap(ORIGIN/'train.bin',dtype='<u2',mode='r');records=[];seen={r['canonical_sha256'] for r in read_json(Path('/home/aihub_ubuntu/jmicro-data/phase6/diverse-learning-20261005/sample-initial.json'))};heads=set()
        if expand:
            records=[json.loads(line) for line in (DATA/'candidate.jsonl').read_text().splitlines()]
            seen={r['canonical_sha256'] for r in records};heads={r['first_sentence_hash'] for r in records}
            seek=read_json(DATA/'ready-initial.json')['next_index_byte']
        else:seek=0
        with (ORIGIN/'train.index.jsonl').open('rb') as stream:
            stream.seek(seek)
            while line:=stream.readline():
                row=json.loads(line)
                if row['source']!='web':continue
                counts['Web_documents_read']+=1
                if counts['Web_documents_read']>300000:break
                if not 64<=row['body_tokens']<=256:continue
                ids=tokens[row['offset']+1:row['offset']+1+row['body_tokens']].tolist()
                text=tok.decode_bytes(ids).decode('utf-8');unit=candidate(text,row['body_tokens'])
                if not unit or unit['structure']!='declarative':continue
                digest=unit_hash(text)
                if digest in seen or unit['first_sentence_hash'] in heads:continue
                if any(p in text for p in protected):counts['protected_excluded']+=1;continue
                seen.add(digest);heads.add(unit['first_sentence_hash']);records.append(record(row,text,unit,'train'))
                counts['accepted']=len(records)
                if len(records)%1000==0:heartbeat('train-scan');print(json.dumps(dict(counts),ensure_ascii=False),flush=True)
                if len(records)>=binding['target_documents']:break
            next_byte=stream.tell()
        assert len(records)==binding['target_documents'],'Actual unique train supply below fixed target'
        dev=[]
        if not expand:
            directory=Path(base['dev_shards']);assert sha256(directory/'manifest.json')==base['dev_manifest_sha256']
            rows=read_json(directory/'dev.index.json');dtokens=np.memmap(directory/'dev.bin',dtype='<u2',mode='r');groups=Counter()
            for row in rows[256:]:
                if not 64<=row['body_tokens']<=256:continue
                text=tok.decode_bytes(dtokens[row['offset']+1:row['offset']+1+row['body_tokens']].tolist()).decode('utf-8')
                unit=candidate(text,row['body_tokens'])
                if not unit or unit['structure']=='declarative' or groups[unit['structure']]>=32:continue
                if unit_hash(text) in seen or unit['first_sentence_hash'] in heads or any(p in text for p in protected):continue
                dev.append(record(row,text,unit,'dev'));groups[unit['structure']]+=1
                if len(dev)==64:break
            assert groups==dict(quotation=32,conditional=32),'Structural dev64 supply below target'
            write_json(DATA/'dev64.json',dev)
        else:dev=read_json(DATA/'dev64.json')
        label='expanded' if expand else 'candidate';corpus=DATA/(label+'.jsonl')
        corpus.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records+dev))
        heartbeat('write-shards');manifest=build_shards(corpus,tok.path,DATA/label)
        assert manifest['splits']['train']['tokens']>=(5000000 if expand else 1000000)
        sample=random.Random(SEED+(1 if expand else 0)).sample(records[10000:] if expand else records,64)
        write_json(DATA/('sample-'+stage+'.json'),sample)
        ready=dict(status='prepared_pending_individual_content_review',binding=binding,pool=str(DATA/label),manifest_sha256=sha256(DATA/label/'manifest.json'),
            corpus_sha256=sha256(corpus),splits=manifest['splits'],sample_sha256=sha256(DATA/('sample-'+stage+'.json')),next_index_byte=next_byte,
            styles=dict(Counter(r['ending_style'] for r in records)),sentence_counts=dict(Counter(r['sentences'] for r in records)),
            unique_first_sentences=len(heads),dev_structures=dict(Counter(r['structure'] for r in dev)),
            literal_source_documents_not_authored_name_variants=True,broader_overlap_audit_performed=False,parent_may_have_seen_train=True,
            fixed_eval_used_only_for_exclusion=True,protected_test_used=False,created_at=now(),CPU_seconds=time.monotonic()-start)
        write_json(DATA/('ready-'+stage+'.json'),ready);write_json(RUN/('ready-'+stage+'.json'),ready)
        heartbeat('complete');job.update(status='complete',completed_at=now());print(json.dumps(ready,ensure_ascii=False),flush=True)
    except BaseException as error:job.update(status='failed',error=repr(error));raise
    finally:job['seconds']=time.monotonic()-start;atomic_json(job_path,job)


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7);p=argparse.ArgumentParser();p.add_argument('--expand',action='store_true');a=p.parse_args();prepare(a.expand)
