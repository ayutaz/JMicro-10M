"""Bounded train-only whole-document preparation with uniform random inspection."""
from collections import Counter
import json
import multiprocessing as mp
import os
from pathlib import Path
import random
import shutil
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
from jmicro.eos_pilot import TrainView, spans
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.training import atomic_json
from jmicro.complete_units import unit_hash
from jmicro.whole_short_text import whole_candidate
from phase6_performance import identity, alive
import prepare_complete_units as decode

DATA = Path('/home/aihub_ubuntu/jmicro-data/phase6/complete-documents-20261005')
POOL = DATA/'shards'
TARGETS = {'story': 30_000_000, 'web': 80_000_000}
MAX_WEB_SCAN = 8_000_000_000
BUDGET = 1800
SEED = 20261005


def worker_batch(task):
    source, batch = task
    result = []
    for start, end in batch:
        ids = decode._TRAIN[start+1:end].tolist()
        if not ids or any(i < 8 for i in ids):
            continue
        try:
            text = b''.join(decode._PIECES[i] for i in ids).decode('utf-8')
        except UnicodeDecodeError:
            continue
        unit = whole_candidate(text, len(ids), source)
        if unit:
            result.append({**unit, 'ids': ids, 'source_start': start, 'source_end': end, 'source': source})
    return result


def limited_batches(view, source, check, counts, start_offset=0):
    previous, batch = -1, []
    limit = min(len(view.tokens), MAX_WEB_SCAN if source == 'web' else len(view.tokens))
    lower, upper = (32,128) if source == 'story' else (64,384)
    if start_offset:
        # Recover the preceding original EOS from one bounded chunk, not a corpus rescan.
        prior_ends=np.flatnonzero(view.tokens[max(0,start_offset-4_000_000):start_offset]==3)
        assert len(prior_ends)
        previous=int(prior_ends[-1])+max(0,start_offset-4_000_000)
    for offset in range(start_offset, limit, 4_000_000):
        check()
        chunk = view.tokens[offset:min(limit, offset+4_000_000)]
        starts, ends, previous = spans(chunk, offset, previous)
        sizes = ends-starts-1
        counts[source+'_scan_tokens'] = offset+len(chunk)
        counts[source+'_scan_documents'] += len(ends)
        for a,b in zip(starts[(sizes>=lower)&(sizes<=upper)], ends[(sizes>=lower)&(sizes<=upper)]):
            assert view.tokens[a] == 2 and view.tokens[b] == 3
            batch.append((int(a),int(b)))
            if len(batch)==256:
                yield source,batch
                batch=[]
    if batch:
        yield source,batch


def main():
    assert sys.version_info[:3] == (3,12,7)
    old = read_json(ROOT/'configs/phase6/story20_low_lr_10b_500m.json')
    sources = {'story': dict(directory=old['pool']['pool'], manifest_sha256=old['pool']['manifest_sha256']),
               'web': dict(directory=old['web_shards'], manifest_sha256=old['web_manifest_sha256'])}
    binding = dict(sources=sources, targets=TARGETS, max_web_scan=MAX_WEB_SCAN, budget_seconds=BUDGET,
                   seed=SEED, source_sha256=sha256(Path(__file__)), selector_sha256=sha256(ROOT/'src/jmicro/whole_short_text.py'))
    DATA.mkdir(parents=True, exist_ok=True); POOL.mkdir(parents=True, exist_ok=True)
    path=DATA/'job.json'; prior=read_json(path) if path.exists() else {}
    continuation=False;elapsed_prior=0
    if prior:
        assert not alive(prior), 'Actual builder still live'
        if prior['status']=='complete':
            assert prior['binding']==binding
            ready=read_json(POOL/'ready.json'); assert ready['manifest_sha256']==sha256(POOL/'manifest.json')
            print(json.dumps(ready)); return
        original=prior['binding']
        assert prior['status']=='failed' and prior['error_type']=='AssertionError' and original['max_web_scan']==4_000_000_000
        assert all(original[k]==binding[k] for k in ('sources','targets','seed','selector_sha256','budget_seconds'))
        assert prior['by_source']['story']['tokens']>=TARGETS['story'] and prior['counts']['web_scan_tokens']==4_000_000_000
        assert (POOL/'train.partial.bin').stat().st_size==2*prior['totals']['tokens']
        backup=DATA/'first-4b-job.json'; assert not backup.exists();shutil.copyfile(path,backup)
        binding['continuation']=dict(original_job_sha256=sha256(backup),start_web_offset=4_000_000_000,
            reason='Initial bounded extraction yielded76.77M in44.48s; read unseen remainder without weakening quality or amount gates')
        continuation=True;elapsed_prior=prior['elapsed_seconds']
    counts=Counter(); totals=Counter(); by_source={s:Counter() for s in sources}; hist=Counter()
    rng=random.Random(SEED); samples=[]; seen=set(); started=time.monotonic()
    if continuation:
        counts.update(prior['counts']);totals.update(prior['totals'])
        for source in sources:by_source[source].update(prior['by_source'][source])
        # Rehydrate only the new partial pool index; no old12B corpus index/stream audit.
        reconstructed=Counter()
        for line in (POOL/'train.index.partial.jsonl').open():
            record=json.loads(line);seen.add(record['text_sha256']);hist[record['body_tokens']]+=1
            reconstructed.update(documents=1,tokens=record['body_tokens']+2,body_bytes=record['bytes'])
            if len(samples)<40:samples.append(record)
            else:
                position=rng.randrange(reconstructed['documents'])
                if position<40:samples[position]=record
        assert reconstructed==totals
    job=dict(status='running', **identity(), binding=binding, started_at=now())
    def check():
        if elapsed_prior+time.monotonic()-started>BUDGET:
            raise TimeoutError('Bounded preparation exhausted; partial pool not accepted')
    def heartbeat(stage):
        check(); job.update(stage=stage, heartbeat_at=now(), elapsed_seconds=elapsed_prior+time.monotonic()-started,
                            counts=dict(counts), totals=dict(totals), by_source={k:dict(v) for k,v in by_source.items()})
        atomic_json(path,job)
        print(json.dumps({k:job[k] for k in ('stage','elapsed_seconds','totals','by_source')},ensure_ascii=False),flush=True)
    protected=set()
    for suite in (ROOT/'eval/base.jsonl',ROOT/'eval/japanese_semantics_v2_1.jsonl'):
        for line in suite.read_text().splitlines():
            row=json.loads(line)
            protected.update(unit_hash(row[k]) for k in ('prefix','context') if row.get(k))
            protected.update(unit_hash(v) for v in row.get('choices',[]))
    try:
        heartbeat('setup')
        with (POOL/'train.partial.bin').open('ab' if continuation else 'wb') as stream, (POOL/'train.index.partial.jsonl').open('a' if continuation else 'w') as index:
            for source, ref in sources.items():
                if by_source[source]['tokens']>=TARGETS[source]:continue
                view=TrainView(ref['directory'],ref['manifest_sha256'],check_stream=source=='story')
                with mp.get_context('fork').Pool(12,initializer=decode.worker_init,
                        initargs=(str(ROOT/old['tokenizer']),str(view.directory/'train.bin'))) as workers:
                    last_report=0
                    offset=4_000_000_000 if continuation and source=='web' else 0
                    for units in workers.imap(worker_batch,limited_batches(view,source,check,counts,offset),chunksize=1):
                        check()
                        for unit in units:
                            digest=unit['text_sha256']
                            if digest in protected: counts['protected_exact_excluded']+=1; continue
                            if digest in seen: counts['local_duplicates_excluded']+=1; continue
                            seen.add(digest); ids=unit['ids']; size=len(ids)
                            # Copy original full body IDs; no fragments, re-encoding or truncation.
                            packed=np.asarray([2,*ids,3],dtype='<u2'); stream.write(packed.tobytes())
                            record={k:v for k,v in unit.items() if k not in ('text','ids')}
                            record.update(offset=totals['tokens'],body_tokens=size,bytes=len(unit['text'].encode()),split='train')
                            index.write(json.dumps(record,ensure_ascii=False)+'\n')
                            amount=dict(tokens=len(packed),documents=1,body_bytes=record['bytes'])
                            totals.update(amount);by_source[source].update(amount);hist[size]+=1
                            sample=record
                            if len(samples)<40: samples.append(sample)
                            else:
                                position=rng.randrange(totals['documents'])
                                if position<40: samples[position]=sample
                            if by_source[source]['tokens']>=TARGETS[source]: break
                        if time.monotonic()-last_report>10:
                            heartbeat(source);last_report=time.monotonic()
                        if by_source[source]['tokens']>=TARGETS[source]: break
                heartbeat(source+'-done')
            stream.flush();index.flush();os.fsync(stream.fileno());os.fsync(index.fileno())
        assert 100_000_000<=totals['tokens']<=120_000_000 and all(by_source[s]['tokens']>=TARGETS[s] for s in sources),dict(totals)
        os.replace(POOL/'train.partial.bin',POOL/'train.bin');os.replace(POOL/'train.index.partial.jsonl',POOL/'train.index.jsonl')
        from jmicro.tokenizer import Tokenizer
        tok=Tokenizer(ROOT/old['tokenizer']);packed_view=np.memmap(POOL/'train.bin',dtype='<u2',mode='r')
        samples=[{**row,'text':tok.decode_bytes(packed_view[row['offset']+1:row['offset']+1+row['body_tokens']].tolist()).decode('utf-8').strip()} for row in samples]
        shutil.copyfile(Path(sources['web']['directory'])/'token_bytes.json',POOL/'token_bytes.json')
        manifest=dict(version=1,dtype='<u2',kind='web',vocab_size=4096,tokenizer_sha256=old['tokenizer_sha256'],
                      token_bytes_sha256=sha256(POOL/'token_bytes.json'),binding=binding,
                      packing='BOS/original whole naturally finished document/EOS; never sliced',
                      splits={'train':dict(totals,stream_sha256=sha256(POOL/'train.bin'),index_sha256=sha256(POOL/'train.index.jsonl'),index_format='jsonl')})
        write_json(POOL/'manifest.json',manifest);write_json(POOL/'samples.json',dict(seed=SEED,method='uniform reservoir over all accepted whole documents',rows=samples))
        ready=dict(status='ready_pending_content_inspection',manifest_sha256=sha256(POOL/'manifest.json'),binding=binding,
                   totals=dict(totals),by_source={k:dict(v) for k,v in by_source.items()},scan=dict(counts),
                   histogram=dict(hist),body_tokens_mean=(totals['tokens']-2*totals['documents'])/totals['documents'],
                   EOS_per_1000_tokens=1000*totals['documents']/totals['tokens'],short_exposure_ratio=99975168/totals['tokens'],
                   source_train_only=True,whole_original_documents=True,new_Web_source_tokens=0,
                   independently_unique_tokens='not certified; existing Web is reused and broad overlap audit incomplete',
                   independent_human_certification=False,seconds=elapsed_prior+time.monotonic()-started)
        write_json(POOL/'ready.json',ready);heartbeat('complete');job.update(status='complete',completed_at=now())
        print(json.dumps(ready,ensure_ascii=False),flush=True)
    except BaseException as error:
        job.update(status='failed',error_type=type(error).__name__,error=str(error));raise
    finally:
        job['elapsed_seconds']=elapsed_prior+time.monotonic()-started;atomic_json(path,job)


if __name__=='__main__': main()
