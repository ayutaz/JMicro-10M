"""Pin and prepare complete public Japanese stories; public train only, via uv."""
import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import sys
import time

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import pyarrow.parquet as pq
from huggingface_hub import HfApi,hf_hub_download
from jmicro.coherent_units import DEPENDENT_START
from jmicro.complete_units import balanced,complete_sentences,unit_hash
from jmicro.evaluation import canonicalize_text
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from jmicro.tokenizer import Tokenizer

REPO='SimpleStories/SimpleStories-JA'
DATA=Path('/home/aihub_ubuntu/jmicro-data/phase6/simple-stories-ja-20261004')
ENDING='帰|戻|仲良|嬉|うれし|喜|幸せ|楽|安心|笑|感じ|学|知|大切|助|ありがとう|終|眠|思|分か|わか|でき|出来|過ご|見つ|満足|決|暮ら|守|成功|解|心|夢'


def story_candidate(text,tok,minimum=32,maximum=128):
    text=canonicalize_text(text).strip()
    if not text or DEPENDENT_START.search(text) or not balanced(text): return None
    if any(term in text for term in ('http','```','続く','つづく','続き','<|')): return None
    sentences=list(complete_sentences(text))
    if not 2<=len(sentences)<=8: return None
    last=0
    for a,b,_ in sentences:
        if text[last:a].strip(): return None
        last=b
    if text[last:].strip(): return None
    import re
    if (not re.search(ENDING,sentences[-1][2]) or re.search(r'[?？][」』]*$',text)
            or re.search(r'わからな|分からな|誰も.*知ら|行方不明|どうなる|始まりだった',sentences[-1][2])): return None
    values=[s[2] for s in sentences]
    if len(set(values))!=len(values) or re.search(r'(.{4,}?)\1\1',text): return None
    grams=[text[i:i+4] for i in range(max(0,len(text)-3))]
    if grams and 1-len(set(grams))/len(grams)>.15: return None
    ids=tok.encode(text)
    if not minimum<=len(ids)<=maximum or any(i<8 for i in ids): return None
    return dict(text=text,ids=ids,sentences=len(sentences),text_sha256=unit_hash(text))


def pin():
    DATA.mkdir(parents=True,exist_ok=True)
    path=DATA/'source.json'
    if path.exists(): return read_json(path)
    info=HfApi(token=False).dataset_info(REPO,files_metadata=True)
    files=[dict(path=s.rfilename,bytes=s.size,lfs_sha256=s.lfs.sha256 if s.lfs else None)
           for s in info.siblings if s.rfilename.endswith('.parquet') and 'train' in s.rfilename]
    assert files,'No official train files'
    card=hf_hub_download(REPO,'README.md',repo_type='dataset',revision=info.sha,token=False)
    payload=Path(card).read_text()
    assert 'license: mit' in payload.lower(),'License must be confirmed'
    (DATA/'README.source.md').write_text(payload)
    source=dict(repo=REPO,revision=info.sha,license='MIT as declared by dataset author',
                card_sha256=sha256(DATA/'README.source.md'),files=files,
                url=f'https://huggingface.co/datasets/{REPO}/tree/{info.sha}',
                generation='gpt-4o-mini per author; already public synthetic text, no paid generation',
                official_validation_or_test_downloaded=False,pinned_at=now())
    write_json(path,source)
    return source


def download(source,item):
    path=Path(hf_hub_download(REPO,item['path'],repo_type='dataset',revision=source['revision'],token=False))
    digest=sha256(path)
    if item['lfs_sha256']: assert digest==item['lfs_sha256']
    assert path.stat().st_size==item['bytes']
    return path,digest


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--inspect',action='store_true')
    args=parser.parse_args()
    assert sys.version_info[:3]==(3,12,7)
    source=pin()
    tok=Tokenizer(ROOT/'artifacts/phase2/4096/tokenizer.model')
    print(json.dumps(source,ensure_ascii=False),flush=True)
    if args.inspect:
        path,digest=download(source,source['files'][0])
        table=pq.ParquetFile(path)
        batch=next(table.iter_batches(batch_size=1000)).to_pylist()
        accepted=[dict(story_candidate(r['story'],tok),generation_id=r['generation_id']) for r in batch if story_candidate(r['story'],tok)]
        write_json(DATA/'inspection.json',dict(first_train_file_sha256=digest,rows=1000,accepted=len(accepted),
            mean_tokens=float(np.mean([len(r['ids']) for r in accepted])) if accepted else None,
            samples=[{k:v for k,v in r.items() if k!='ids'} for r in accepted[:40]]))
        print(json.dumps(read_json(DATA/'inspection.json'),ensure_ascii=False,indent=2),flush=True)
        return
    output=DATA/'shards'
    output.mkdir(parents=True,exist_ok=True)
    if (output/'ready.json').exists():
        print(json.dumps(read_json(output/'ready.json')),flush=True); return
    started=time.monotonic(); counts=Counter(); hist=Counter(); seen=set(); samples=[]; sources=[]; aux=[]; parent_train=set(); parent_dev=set()
    protected=set()
    for path in (ROOT/'eval/base.jsonl',ROOT/'eval/japanese_semantics_v2_1.jsonl'):
        for line in path.read_text().splitlines():
            row=json.loads(line)
            protected.update(unit_hash(row[k]) for k in ('prefix','context') if row.get(k))
            protected.update(unit_hash(v) for v in row.get('choices',[]))
    with (output/'train.partial.bin').open('wb') as stream,(output/'train.index.partial.jsonl').open('w') as index:
        for item in source['files']:
            path,digest=download(source,item); sources.append(dict(path=item['path'],sha256=digest,bytes=item['bytes']))
            file_row=0
            for batch in pq.ParquetFile(path).iter_batches(batch_size=1024):
                if time.monotonic()-started>1800: raise TimeoutError('Bounded story preparation exhausted')
                for record in batch.to_pylist():
                    counts['source_rows']+=1
                    local_row=file_row; file_row+=1
                    if 'クリフハンガー' in record.get('feature','') or '超現実' in record.get('style',''): continue
                    unit=story_candidate(record['story'],tok)
                    if not unit: continue
                    if unit['text_sha256'] in protected:
                        counts['protected_exact_excluded']+=1; continue
                    if unit['text_sha256'] in seen:
                        counts['local_duplicates_excluded']+=1; continue
                    seen.add(unit['text_sha256'])
                    parent=record['generation_id'].rsplit('-',1)[0]
                    if int(hashlib.sha256(parent.encode()).hexdigest()[:8],16)%100==0:
                        parent_dev.add(parent)
                        if len(aux)<100: aux.append(dict(parent=parent,generation_id=record['generation_id'],text=unit['text']))
                        continue
                    parent_train.add(parent)
                    size=len(unit['ids']); raw_bytes=len(unit['text'].encode())
                    stream.write(np.asarray([2,*unit['ids'],3],dtype='<u2').tobytes())
                    metadata=dict(generation_id=record['generation_id'],parent_id=parent,source_file=item['path'],source_row=local_row,source_global_row=counts['source_rows']-1,
                                  offset=counts['tokens'],body_tokens=size,bytes=raw_bytes,sentences=unit['sentences'],text_sha256=unit['text_sha256'],split='train')
                    index.write(json.dumps(metadata,ensure_ascii=False)+'\n')
                    counts.update(tokens=size+2,documents=1,body_bytes=raw_bytes); hist[size]+=1
                    if len(samples)<100: samples.append(dict(metadata,text=unit['text']))
                    if counts['tokens']>=25_000_000: break
                if counts['documents'] and counts['documents']%10000<1024:
                    print(json.dumps(dict(status='building',counts=dict(counts),seconds=time.monotonic()-started,pid=os.getpid())),flush=True)
                if counts['tokens']>=25_000_000: break
            if counts['tokens']>=25_000_000: break
        for handle in (stream,index): handle.flush(); os.fsync(handle.fileno())
    assert 25_000_000<=counts['tokens']<=50_000_000,counts
    assert not parent_train & parent_dev
    os.replace(output/'train.partial.bin',output/'train.bin'); os.replace(output/'train.index.partial.jsonl',output/'train.index.jsonl')
    byte_lengths=[0 if i<8 else len(tok.decode_bytes([i])) for i in range(4096)]
    write_json(output/'token_bytes.json',byte_lengths)
    manifest=dict(version=1,dtype='<u2',kind='web',vocab_size=4096,
        tokenizer_sha256=sha256(tok.path),token_bytes_sha256=sha256(output/'token_bytes.json'),
        packing='BOS/full naturally finished source story/EOS; no story slicing or token truncation',
        source=source,files_used=sources,selection='whole2–8sentences/body32–128/resolved end/low repetition; family1percent auxiliary holdout',
        selection_source_sha256=sha256(Path(__file__)),
        splits={'train':dict(tokens=counts['tokens'],documents=counts['documents'],body_bytes=counts['body_bytes'],stream_sha256=sha256(output/'train.bin'),index_sha256=sha256(output/'train.index.jsonl'),index_format='jsonl')})
    write_json(output/'manifest.json',manifest)
    write_json(output/'auxiliary-dev.json',dict(split='supplemental-dev',parents_disjoint_from_supplemental_train=True,rows=aux,not_used_for_candidate_selection=True))
    write_json(output/'samples.json',samples)
    ready=dict(status='ready_pending_content_inspection',manifest_sha256=sha256(output/'manifest.json'),totals=dict(counts),
        parent_documents=len(parent_train),seconds=time.monotonic()-started,workers=1,body_token_histogram=dict(hist),
        body_tokens_mean=sum(k*v for k,v in hist.items())/counts['documents'],source_train_only=True,
        new_unique_source_tokens='new public source; overlap with old Web unknown, not guaranteed unique',
        semantic_quality='synthetic public stories, heuristic selection and sampled Codex inspection; no independent human certificate',
        source_sha256=sha256(DATA/'source.json'),parent_split_disjoint=True)
    write_json(output/'ready.json',ready); print(json.dumps(ready,ensure_ascii=False),flush=True)


if __name__=='__main__': main()
