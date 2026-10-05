"""Bounded, read-only real-weight diagnostics; never updates an optimizer."""
import argparse
from contextlib import nullcontext
import gc
import json
import os
from pathlib import Path
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel, SDPBackend
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer, SUPPRESS_IDS
from jmicro.training import atomic_json, gpu_lock, implementation_hashes, seed_all, configure_compile_cache

OUT = ROOT / 'reports/phase6/root-cause-20261005'
WEB = Path('/home/aihub_ubuntu/jmicro-data/phase6/ten-billion/prepared-v2/export-001/shards')
STORY = Path('/home/aihub_ubuntu/jmicro-data/phase6/dataset-expansion-20261005/shards')
TOK = ROOT / 'artifacts/phase2/4096/tokenizer.model'


def identity():
    return dict(pid=os.getpid(), boot_id=Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
                start_ticks=int(Path('/proc/self/stat').read_text().split()[21]))


def padded(rows, device):
    x = torch.zeros((len(rows), max(map(len, rows))), dtype=torch.long, device=device)
    mask = torch.zeros_like(x, dtype=torch.bool)
    for i, row in enumerate(rows):
        x[i, :len(row)] = torch.tensor(row, device=device)
        mask[i, :len(row)] = True
    return x, mask


def distribution(logits, target=None):
    """Raw probabilities before suppression/temperature/top-p; EOS rank is 1 based."""
    logits = logits.float()
    p = logits.softmax(-1)
    top = logits.topk(5)
    result = dict(eos_probability=float(p[3]), eos_rank=int((logits > logits[3]).sum()) + 1,
                  eos_margin_to_best=float(logits[3] - logits.max()),
                  entropy_nats=float(-(p * p.clamp_min(1e-30).log()).sum()),
                  top_ids=top.indices.tolist(), top_probabilities=p[top.indices].tolist())
    if target is not None:
        result.update(target=int(target), target_probability=float(p[target]),
                      target_rank=int((logits > logits[target]).sum()) + 1,
                      target_nll=float(-p[target].clamp_min(1e-30).log()))
    return result


def choose(logits, generator=None):
    scores = logits.clone().float()
    scores[list(SUPPRESS_IDS)] = -torch.inf
    if generator is None:
        return int(scores.argmax())
    scores /= .8
    sorted_scores, indices = scores.sort(descending=True)
    probabilities = sorted_scores.softmax(-1)
    sorted_scores[probabilities.cumsum(-1) - probabilities >= .9] = -torch.inf
    return int(indices[torch.multinomial(sorted_scores.softmax(-1), 1, generator=generator)])


def first_repeated_ngram(ids, n=4):
    seen = {}
    for i in range(len(ids) - n + 1):
        key = tuple(ids[i:i+n])
        if key in seen:
            return dict(first=seen[key], repeated=i, end_step=i+n-1, ids=list(key))
        seen[key] = i
    return None


def sample_pool(path, source, tok):
    """Local random-access token windows: no whole stream hash/index/corpus pass."""
    manifest = read_json(path / 'manifest.json')
    assert manifest['tokenizer_sha256'] == sha256(TOK)
    total = manifest['splits']['train']['tokens']
    assert (path / 'train.bin').stat().st_size == total * 2
    stream = np.memmap(path / 'train.bin', dtype='<u2', mode='r')
    rng = np.random.default_rng(7105)
    strata = [[], [], [], []]
    seen = set()
    for attempt in range(4096):
        offset = int(rng.integers(0, total - 65536))
        window = stream[offset:offset+65536]
        starts = np.flatnonzero(window == 2)
        if not len(starts):
            continue
        start = offset + int(starts[0])
        if start in seen:
            continue
        ends = np.flatnonzero(stream[start+1:start+65536] == 3)
        if not len(ends):
            continue
        end = start + 1 + int(ends[0])
        body = stream[start+1:end].astype(int).tolist()
        if not body or min(body) < 8:
            continue
        length = len(body)
        bucket = 0 if length <= 64 else 1 if length <= 128 else 2 if length <= 256 else 3
        if len(strata[bucket]) == 16:
            continue
        seen.add(start)
        text = tok.decode(body)
        import hashlib
        row = dict(id=f'{source}-{start}', source=source, split='train', offset=start,
                   body_ids=body, text=text, body_tokens=length,
                   text_sha256=hashlib.sha256(text.encode()).hexdigest(), length_stratum=bucket,
                   end_ids=[int(stream[end]), int(stream[end+1])] if end+1 < total else [3],
                   roundtrip=tok.decode(tok.encode(text)) == text,
                   original_body_bytes=len(text.encode()),
                   previous_context_ids=stream[max(start-128, (start//1024)*1024):start].astype(int).tolist())
        strata[bucket].append(row)
        if all(len(s) == 16 for s in strata):
            break
    rows = [row for s in strata for row in s]
    if len(rows) < 64:
        # A naturally short pool may have no >256 documents. Keep evidence of absence;
        # fill missing quotas from its other lengths, without filtering on content.
        for attempt in range(4096, 8192):
            start = int(rng.integers(0, total-65536))
            w = stream[start:start+65536]
            bos = np.flatnonzero(w == 2)
            if not len(bos):
                continue
            start += int(bos[0])
            ends = np.flatnonzero(stream[start+1:start+65536] == 3)
            if start in seen or not len(ends):
                continue
            end = start+1+int(ends[0])
            body = stream[start+1:end].astype(int).tolist()
            if not body or min(body) < 8:
                continue
            seen.add(start)
            text = tok.decode(body)
            import hashlib
            length = len(body)
            rows.append(dict(id=f'{source}-{start}', source=source, split='train', offset=start,
                body_ids=body, text=text, body_tokens=length, text_sha256=hashlib.sha256(text.encode()).hexdigest(),
                length_stratum=0 if length<=64 else 1 if length<=128 else 2 if length<=256 else 3,
                quota_fallback=True, end_ids=[3], roundtrip=tok.decode(tok.encode(text))==text,
                original_body_bytes=len(text.encode()),
                previous_context_ids=stream[max(start-128,(start//1024)*1024):start].astype(int).tolist()))
            if len(rows) == 64:
                break
    assert len(rows) == 64
    return rows, dict(path=str(path), manifest_sha256=sha256(path/'manifest.json'),
                     prepared=manifest['splits']['train'], sample_selection='token-offset random; length strata, not uniform document; no source subbucket index scan',
                     raw_stratum_counts=[len(s) for s in strata], scanned_candidates=attempt+1,
                     full_corpus_audit='not repeated; independently incomplete')


def prepare():
    if (OUT/'contract.json').exists():
        raise ValueError('Frozen contract exists: use it, do not resample')
    OUT.mkdir(parents=True, exist_ok=True)
    tok = Tokenizer(TOK)
    corpus, pools = [], {}
    for name, path in [('web', WEB), ('story200m', STORY)]:
        rows, pools[name] = sample_pool(path, name, tok)
        corpus.extend(rows)
    cases = []
    for source in ['web', 'story200m']:
        rows = [r for r in corpus if r['source'] == source and r['body_tokens'] <= 128][:8]
        assert len(rows) == 8
        for row in rows:
            prefix_len = max(4, min(24, len(row['body_ids'])//2))
            cases.append(dict(row, prefix_ids=[2, *row['body_ids'][:prefix_len]],
                              gold_ids=[*row['body_ids'][prefix_len:], 3], prefix_length=prefix_len))
    train_cases_path = Path('/home/aihub_ubuntu/jmicro-data/phase6/packing-study-20261005/compact-train-eval.json')
    train_cases = read_json(train_cases_path)
    # Two complete train pairs in each of four categories; frozen order, not scores.
    categories = list(dict.fromkeys(r['category'] for r in train_cases))[:4]
    for category in categories:
        selected = [r for r in train_cases if r['category'] == category][:4]
        assert len(selected) == 4
        for row in selected:
            assert row['split'] == 'train'
            body, prefix = tok.encode(row['text']), tok.encode(row['prefix'])
            assert body[:len(prefix)] == prefix
            cases.append(dict(row, source='compact', body_ids=body, body_tokens=len(body),
                              prefix_ids=[2, *prefix], gold_ids=[*body[len(prefix):], 3],
                              prefix_length=len(prefix), previous_context_ids=[]))
    assert len(cases) == 32
    codec = {}
    for vocab in (4096, 8192):
        codec_tok = Tokenizer(ROOT / f'artifacts/phase2/{vocab}/tokenizer.model')
        codec[str(vocab)] = dict(tokenizer_sha256=sha256(codec_tok.path),
            samples=[dict(id=r['id'], token_count=len(codec_tok.encode(r['text'])),
                          bytes=len(r['text'].encode()), lossless=codec_tok.decode(codec_tok.encode(r['text']))==r['text']) for r in cases])
    atomic_json(OUT/'corpus.json', corpus)
    atomic_json(OUT/'cases.json', cases)
    atomic_json(OUT/'codec.json', codec)
    ledger = read_json(ROOT/'reports/phase6/packing_study_checkpoint_ledger.json')
    story_result_path = ROOT/'reports/phase6/story20-low-lr-10b-500m-20261005/evaluation/result/coherent20/evaluation/result.json'
    sr = read_json(story_result_path)
    checkpoints = dict(original=ledger['binding']['parent'], mixed=ledger['checkpoints']['mixed-candidate'])
    story_checkpoint = ROOT/'reports/phase6/story20-low-lr-10b-500m-20261005/coherent20/checkpoint-00320435.pt'
    assert sha256(story_checkpoint) == sr['checkpoint_sha256']
    checkpoints['story'] = dict(path=str(story_checkpoint), sha256=sr['checkpoint_sha256'],
                                selection='existing frozen coherent20 branch; no new score selection')
    for name in checkpoints:
        entry = checkpoints[name]
        checkpoints[name] = dict(path=entry.get('path', entry.get('checkpoint')),
            sha256=entry.get('sha256', entry.get('checkpoint_sha256')))
    contract = dict(created_at=now(), checkpoints=checkpoints, pools=pools,
        implementation=implementation_hashes(), source_sha256=sha256(Path(__file__)),
        files={n:sha256(OUT/n) for n in ('cases.json','corpus.json','codec.json')},
        tokenizer_sha256=sha256(TOK), cases=32, corpus_documents=128,
        train_cases_sha256=sha256(train_cases_path),
        scope='User-facing steps1-3 = plan70 internal stages0-2; inference/backward only, no training',
        gpu_budget_seconds=600, seed=42, max_new_tokens=64, sampling_seeds=[42,43,44],
        optional_128='not scheduled; previous512 negative evidence reused',
        precision=read_json(ROOT/'configs/evaluation/protocol.json')['numeric_tolerances'],
        gradient_checks='FP32 math full vs causal atol1e-7 rtol1e-6; BF16 finite only, compare reported norms/cosines without new pass threshold',
        fp32_loss=dict(atol=1e-6,rtol=1e-5), numerical_failures='report unchanged thresholds, investigate error size; no false pass',
        numeric_lengths=[64,1024], existing_story_result=dict(path=str(story_result_path),sha256=sha256(story_result_path)),
        quality_goals_changed=False, scientific_training_tokens=0, protected_test_used=False)
    atomic_json(OUT/'contract.json', contract)
    print(json.dumps(dict(status='prepared',cases=32,corpus_documents=128,contract_sha256=sha256(OUT/'contract.json')), ensure_ascii=False), flush=True)


def compare(a,b,tolerance):
    a,b=a.detach().float(),b.detach().float()
    delta=(a-b).abs()
    close=torch.isclose(a,b,**tolerance)
    return dict(passed=bool(close.all()), finite=bool(torch.isfinite(a).all() and torch.isfinite(b).all()),
                max_abs=float(delta.max()), mean_abs=float(delta.mean()),
                outside_tolerance=int((~close).sum()), elements=a.numel(), tolerance=tolerance)


def numeric(model,cases,contract,check_budget):
    report = dict(checks={},gradients={}, labels={}, implementation=implementation_hashes())
    tol=contract['precision']['fp32_reference_logits']
    bf_tol=contract['precision']['bf16_logits']
    # All32 actual teacher sequences, PAD masking, exactly one target shift.
    rows=[[2,*r['body_ids'],3] for r in cases]
    x,valid=padded([r[:-1] for r in rows],'cuda')
    y,_=padded([r[1:] for r in rows],'cuda')
    y[~valid]=-100
    y[y==2]=-100
    assert not (y==0).any() and not (y==2).any()
    report['labels']=dict(exact_shift=True,bos_targets_masked=True,pad_targets_masked=True,
        eos_targets=int((y==3).sum()), supervised_targets=int((y!=-100).sum()),
        first_example=dict(input=rows[0][:-1],target=rows[0][1:]),
        trainer_calls_internal_model_labels=False)
    with torch.no_grad(),sdpa_kernel([SDPBackend.MATH]):
        ref=model(x,attention_mask=valid).logits
        bf=None
        with torch.autocast('cuda',dtype=torch.bfloat16):
            bf=model(x,attention_mask=valid).logits
        report['checks']['all32_bf16_math_vs_fp32']=compare(ref[valid],bf[valid],bf_tol)
        standalone=[]
        for row in rows:
            z=torch.tensor([row[:-1]],device='cuda')
            standalone.append(model(z).logits[0])
        report['checks']['all32_padding']=compare(ref[valid],torch.cat(standalone),tol)
    del ref,bf,standalone,x,y
    hf=model.hf_reference().to('cuda').eval()
    for length in contract['numeric_lengths']:
        check_budget()
        # Real contiguous stream contains natural document boundaries and EOS/BOS.
        stream=np.memmap(WEB/'train.bin',dtype='<u2',mode='r')
        ids=stream[cases[0]['offset']:cases[0]['offset']+length+1].astype(np.int64)
        x=torch.tensor(ids[:-1][None],device='cuda')
        y=torch.tensor(ids[1:][None],device='cuda'); y[y==2]=-100
        with sdpa_kernel([SDPBackend.MATH]):
            full=model(x).logits
            loss=F.cross_entropy(full.flatten(0,1),y.flatten())
            loss.backward()
            names=['model.embed_tokens.weight','model.layers.0.self_attn.q_proj.weight','model.layers.12.mlp.down_proj.weight']
            gradients={n:p.grad.detach().clone() for n,p in model.named_parameters() if n in names}
            model.zero_grad(set_to_none=True)
            fast=model(x,training_fast_path=True).logits
            fast_loss=F.cross_entropy(fast.flatten(0,1),y.flatten()); fast_loss.backward()
            report['checks'][f'{length}_fp32_full_causal_logits']=compare(full,fast,tol)
            report['checks'][f'{length}_fp32_loss']=compare(loss,fast_loss,contract['fp32_loss'])
            report['gradients'][f'{length}_fp32']= {n:compare(g,p.grad,dict(atol=1e-7,rtol=1e-6)) for n,p in model.named_parameters() if n in gradients for g in [gradients[n]]}
            model.zero_grad(set_to_none=True)
            with torch.no_grad():
                first=model(x[:,:length-8],use_cache=True)
                last=model(x[:,length-8:],cache=first.cache,use_cache=True)
                report['checks'][f'{length}_fp32_cache']=compare(full[:,-8:],last.logits,tol)
                independent=hf(x).logits
                report['checks'][f'{length}_hf_reference']=compare(full,independent,tol)
            with torch.autocast('cuda',dtype=torch.bfloat16):
                bf=model(x).logits
                bf_loss=F.cross_entropy(bf.flatten(0,1),y.flatten()); bf_loss.backward()
            bf_gradients={n:p.grad.detach().clone() for n,p in model.named_parameters() if n in names}
            report['checks'][f'{length}_bf16_vs_fp32']=compare(full,bf,bf_tol)
            model.zero_grad(set_to_none=True)
        with sdpa_kernel([SDPBackend.FLASH_ATTENTION]),torch.autocast('cuda',dtype=torch.bfloat16):
            flash=model(x,training_fast_path=True).logits
            flash_loss=F.cross_entropy(flash.flatten(0,1),y.flatten()); flash_loss.backward()
        report['checks'][f'{length}_bf16_flash_vs_math']=compare(bf,flash,bf_tol)
        report['gradients'][f'{length}_bf16_flash_vs_math']={n:dict(finite=bool(torch.isfinite(p.grad).all()),
            math_norm=float(g.norm()),flash_norm=float(p.grad.norm()),max_abs=float((g-p.grad).abs().max()),
            cosine=float(F.cosine_similarity(g.flatten(),p.grad.flatten(),dim=0))) for n,p in model.named_parameters() if n in bf_gradients for g in [bf_gradients[n]]}
        model.zero_grad(set_to_none=True)
        del full,fast,bf,flash,first,last,independent,loss,fast_loss,bf_loss,flash_loss,gradients,bf_gradients
        atomic_json(OUT/'numeric.json',report)
    # Exact adopted compiled Flash route, same1024 stream, no optimizer step.
    check_budget()
    configure_compile_cache(dict(backend='flash',dtype='bf16',deterministic=False))
    compiled=torch.compile(lambda z:model(z,training_fast_path=True).logits,fullgraph=True,mode='default')
    with sdpa_kernel([SDPBackend.FLASH_ATTENTION]),torch.autocast('cuda',dtype=torch.bfloat16):
        eager=model(x,training_fast_path=True).logits
        loss=F.cross_entropy(eager.flatten(0,1),y.flatten());loss.backward()
        grads={n:p.grad.detach().clone() for n,p in model.named_parameters() if n in names}
        model.zero_grad(set_to_none=True)
        got=compiled(x)
        compiled_loss=F.cross_entropy(got.flatten(0,1),y.flatten()); compiled_loss.backward()
    report['checks']['1024_compiled_flash_logits']=compare(eager,got,bf_tol)
    report['checks']['1024_compiled_flash_loss']=compare(loss,compiled_loss,bf_tol)
    report['gradients']['1024_compiled']={n:dict(finite=bool(torch.isfinite(p.grad).all()),max_abs=float((g-p.grad).abs().max()),
        cosine=float(F.cosine_similarity(g.flatten(),p.grad.flatten(),dim=0))) for n,p in model.named_parameters() if n in grads for g in [grads[n]]}
    model.zero_grad(set_to_none=True)
    atomic_json(OUT/'numeric.json',report)
    del hf,compiled,got,eager,loss,compiled_loss,grads
    torch._dynamo.reset();gc.collect();torch.cuda.empty_cache()
    return report


@torch.no_grad()
def teacher(model,cases):
    rows=[[2,*r['body_ids']] for r in cases]
    x,mask=padded(rows,'cuda')
    with sdpa_kernel([SDPBackend.MATH]),torch.autocast('cuda',dtype=torch.bfloat16):
        logits=model(x,attention_mask=mask).logits
    result=[]
    for i,row in enumerate(cases):
        begin=len(row['prefix_ids'])-1
        scores=[distribution(logits[i,begin+j],target) for j,target in enumerate(row['gold_ids'])]
        context=row.get('previous_context_ids',[])
        contextual=None
        if context:
            ids=[*context,*rows[i]]
            with sdpa_kernel([SDPBackend.MATH]),torch.autocast('cuda',dtype=torch.bfloat16):
                contextual=distribution(model(torch.tensor([ids],device='cuda')).logits[0,-1],3)
        result.append(dict(id=row['id'],source=row['source'],teacher_steps=scores,
            ending=scores[-1],previous_context_ending=contextual,
            teacher_nll_mean=float(np.mean([s['target_nll'] for s in scores])),
            teacher_top1_fraction=float(np.mean([s['target_rank']==1 for s in scores]))))
    return result


@torch.no_grad()
def generate(model,cases,tok,seed,max_new=64):
    rows=[r['prefix_ids'] for r in cases]
    x,mask=padded(rows,'cuda')
    generators=[torch.Generator(device='cuda').manual_seed(seed) for _ in rows] if seed is not None else [None]*len(rows)
    outputs=[dict(id=r['id'],source=r['source'],seed=seed,prefix=tok.decode(r['prefix_ids']),generated_ids=[],steps=[]) for r in cases]
    active=torch.ones(len(rows),dtype=torch.bool,device='cuda')
    with sdpa_kernel([SDPBackend.MATH]),torch.autocast('cuda',dtype=torch.bfloat16):
        prefill=model(x,attention_mask=mask,use_cache=True)
        logits=prefill.logits[torch.arange(len(rows),device='cuda'),mask.sum(-1)-1]
        cache=prefill.cache
        for step in range(max_new):
            next_ids=torch.zeros((len(rows),1),dtype=torch.long,device='cuda')
            for i,out in enumerate(outputs):
                if not active[i]:
                    continue
                chosen=choose(logits[i],generators[i])
                scores=distribution(logits[i],chosen)
                expected=cases[i]['gold_ids'][step] if step<len(cases[i]['gold_ids']) else None
                if expected is not None:
                    p=logits[i].float().softmax(-1)
                    scores.update(expected=expected,expected_probability=float(p[expected]),expected_rank=int((logits[i]>logits[i,expected]).sum())+1)
                out['steps'].append(scores);out['generated_ids'].append(chosen)
                next_ids[i,0]=chosen
                if chosen==3:
                    active[i]=False
            if not active.any() or step==max_new-1:
                break
            got=model(next_ids,attention_mask=active[:,None],cache=cache,use_cache=True)
            cache,logits=got.cache,got.logits[:,0]
    for i,out in enumerate(outputs):
        ids=out['generated_ids'];gold=cases[i]['gold_ids']
        out.update(text=tok.decode(ids,errors='replace'),stop_reason='eos' if ids[-1]==3 else 'max_tokens',
            exact_gold=ids==gold,first_token_departure=next((j for j,(a,b) in enumerate(zip(ids,gold)) if a!=b),None),
            first_repeated_4gram=first_repeated_ngram(ids),
            interpretation='token departure is not semantic error; qualitative review required; raw ranks precede decoding suppression')
    return outputs


def run():
    contract=read_json(OUT/'contract.json')
    assert contract['source_sha256']==sha256(Path(__file__))
    assert contract['implementation']==implementation_hashes()
    for name,digest in contract['files'].items():
        assert sha256(OUT/name)==digest
    tok=Tokenizer(TOK);assert sha256(TOK)==contract['tokenizer_sha256']
    cases=read_json(OUT/'cases.json')
    if (OUT/'job.json').exists():
        raise ValueError('Job record exists; audit saved evidence instead of relaunching')
    seed_all(42);torch.set_num_threads(2)
    start=time.monotonic()
    record=dict(status='starting',identity=identity(),started_at=now(),contract_sha256=sha256(OUT/'contract.json'),
                command='uv run --frozen --extra hub --extra data --extra ml --extra export scripts/run_root_cause_diagnostic.py --run',
                scientific_training_tokens=0,optimizer_updates=0,files=[])
    atomic_json(OUT/'job.json',record)
    def check_budget():
        if time.monotonic()-start>contract['gpu_budget_seconds']:
            raise TimeoutError('Fixed600s GPU budget exhausted; preserve partial evidence, no automatic extension')
    try:
        with gpu_lock('cuda'):
            record['status']='running';atomic_json(OUT/'job.json',record)
            for name,entry in contract['checkpoints'].items():
                check_budget()
                assert sha256(Path(entry['path']))==entry['sha256']
                state=torch.load(entry['path'],map_location='cpu',weights_only=False)
                model=JMicroModel(state['model_config']).cuda().eval()
                model.load_state_dict(state['model'],strict=True)
                tokens,update=state['tokens'],state['update']
                del state
                print(f'{name}: weights verified; numeric/teacher/generation',flush=True)
                if name=='original':
                    numeric(model,cases,contract,check_budget)
                    record['files'].append('numeric.json');atomic_json(OUT/'job.json',record)
                check_budget()
                result=dict(checkpoint=entry,training_tokens=tokens,update=update,
                            teacher=teacher(model,cases),generation={})
                atomic_json(OUT/f'{name}.json',result)
                for seed in [None,*contract['sampling_seeds']]:
                    check_budget()
                    key='greedy' if seed is None else f'sampling-{seed}'
                    result['generation'][key]=generate(model,cases,tok,seed,contract['max_new_tokens'])
                    atomic_json(OUT/f'{name}.json',result)
                    print(f'{name} {key}: {len(cases)} traces saved; elapsed {time.monotonic()-start:.1f}s',flush=True)
                record['files'].append(f'{name}.json');atomic_json(OUT/'job.json',record)
                del model;gc.collect();torch.cuda.empty_cache()
            check_budget()
            record.update(status='complete',completed_at=now(),gpu_job_seconds=time.monotonic()-start,
                peak_allocated=torch.cuda.max_memory_allocated(),peak_reserved=torch.cuda.max_memory_reserved(),
                result_sha256={n:sha256(OUT/n) for n in record['files']})
    except BaseException as error:
        record.update(status='failed',error=repr(error),ended_at=now(),gpu_job_seconds=time.monotonic()-start)
        raise
    finally:
        atomic_json(OUT/'job.json',record)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--prepare',action='store_true');parser.add_argument('--run',action='store_true')
    args=parser.parse_args()
    if args.prepare:prepare()
    elif args.run:run()
    else:parser.error('Choose --prepare or --run')
