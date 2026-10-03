"""Bounded, read-only Phase 6 repetition/EOS investigation. Invoke through uv."""
import argparse
from collections import Counter
from contextlib import nullcontext
import gc
import json
import math
import os
from pathlib import Path
import statistics
import sys
import time

os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG', ':4096:8')
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'src'))
import numpy as np
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend

from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.model import JMicroModel
from jmicro.phase5 import equal_state
from jmicro.repetition_diagnosis import consumed_targets, paired_transitions, repeated_ngram_fraction, repetition_details, target_block_counts
from jmicro.shards import Shard
from jmicro.tokenizer import SUPPRESS_IDS, Tokenizer
from jmicro.training import gpu_lock, rng_state, seed_all
from phase6_performance import identity

RUN = ROOT/'reports/phase6/base-20261003'
CHECKPOINTS = {
    '100M': ROOT/'reports/phase5/run-20261003-docoverfit/100m-no-qknorm/checkpoint-00012208.pt',
    'stable131M': RUN/'stable/checkpoint-00004000.pt',
    'stable328M': RUN/'stable/checkpoint-00010000.pt',
    'stable500M': RUN/'stable/checkpoint-00015259.pt',
    'decay500M': RUN/'decay-500M/checkpoint-00016022.pt',
}
GENERATION = {'100M': ROOT/'reports/phase6/generation_diagnostics.json',
              'decay500M': RUN/'evaluation-500M/generation.json'}


def binding(path):
    return {'path': str(path), 'sha256': sha256(path)}


def describe(values):
    values = np.asarray(values, dtype=float)
    return dict(count=len(values), mean=float(values.mean()),
                **{f'p{p}': float(np.percentile(values, p)) for p in (0, 25, 50, 75, 95, 99, 100)})


def cpu_diagnostics(destination, config, plan):
    started = time.monotonic()
    tok = Tokenizer(ROOT/config['tokenizer'])
    generations = {k: read_json(p)['generation'] for k, p in GENERATION.items()}
    paired = paired_transitions(generations['100M']['outputs'], generations['decay500M']['outputs'])
    output_details = {}
    for name, generation in generations.items():
        rows = []
        for row in generation['outputs']:
            details = repetition_details(row['text'])
            assert details['repetition'] == row['repetition']
            rows.append({**{k: row[k] for k in ('id', 'category', 'decoding', 'suppressed', 'seed', 'stop_reason')},
                         **details, 'tokens': len(row['generated_ids']),
                         'token_4gram_repeat_fraction': repeated_ngram_fraction(row['generated_ids'])})
        output_details[name] = rows
    datasets = {}
    for name, path, checkpoints in (
        ('pilot', Path('/home/aihub_ubuntu/jmicro-data/shards/t4k-pilot'), ['100M']),
        ('expanded', Path(config['shards']), ['stable500M', 'decay500M'])):
        shard = Shard(path)
        lengths = np.fromiter((r['body_tokens'] for r in shard.index), dtype=np.int64)
        starts = np.fromiter((r['offset'] for r in shard.index), dtype=np.int64)
        ends = starts + lengths + 1
        assert np.all(shard.tokens[starts] == 2) and np.all(shard.tokens[ends] == 3)
        special = np.zeros(8, dtype=np.int64)
        for offset in range(0, len(shard.tokens), 16_000_000):
            chunk = shard.tokens[offset:offset+16_000_000]
            special += np.bincount(chunk[chunk < 8], minlength=8)
        assert special[2] == special[3] == len(shard.index)
        assert special[[0, 1, 4, 5, 6, 7]].sum() == 0
        consumed = {}
        for checkpoint_name in checkpoints:
            checkpoint = CHECKPOINTS[checkpoint_name]
            state = torch.load(checkpoint, map_location='cpu', weights_only=False)
            sampler = state['sampler']
            assert state['shard_manifest_sha256'] == sha256(path/'manifest.json')
            bos = consumed_targets(target_block_counts(starts, sampler['blocks'], sampler['context']), sampler)
            eos = consumed_targets(target_block_counts(ends, sampler['blocks'], sampler['context']), sampler)
            assert state['tokens'] == (sampler['epoch']*sampler['blocks']+sampler['position'])*sampler['context']
            assert state['tokens'] - state['supervised_tokens'] == bos
            consumed[checkpoint_name] = {**binding(checkpoint), 'sampler': sampler,
                'tokens': state['tokens'], 'supervised_tokens': state['supervised_tokens'],
                'masked_bos': bos, 'eos_teachers': eos, 'eos_fraction_supervised': eos/state['supervised_tokens'],
                'spec': state['spec'], 'exact_masked_count_verified': True}
            del state
        count = plan['budgets']['content_sample_documents_per_dataset']
        indexes = np.random.default_rng(42).choice(len(shard.index), size=count, replace=False)
        sample = []
        for i in indexes:
            document = shard.index[int(i)]
            body = shard.tokens[document['offset']+1:document['offset']+1+min(document['body_tokens'], 2048)].tolist()
            text = tok.decode_bytes(body).decode(errors='replace')[:plan['budgets']['content_prefix_characters']]
            detail = repetition_details(text)
            sample.append({'doc_id': document['doc_id'], 'body_tokens': document['body_tokens'],
                'prefix_characters': len(text), 'truncated': document['body_tokens'] > len(body) or len(tok.decode_bytes(body).decode(errors='replace')) > len(text),
                **detail, 'char_4gram_repeat_fraction': repeated_ngram_fraction(text),
                'token_4gram_repeat_fraction_first2048': repeated_ngram_fraction(body),
                'prefix': text if detail['repetition'] else None})
        datasets[name] = {'manifest': binding(path/'manifest.json'), 'checksummed_stream_and_index': True,
            'documents': len(shard.index), 'stream_tokens': len(shard.tokens), 'body_tokens': int(lengths.sum()),
            'body_bytes': sum(r['bytes'] for r in shard.index), 'body_length_distribution': describe(lengths),
            'fraction_body_at_most': {str(n): float((lengths <= n).mean()) for n in (64,128,512,1024)},
            'kind_counts': dict(Counter(r['kind'] for r in shard.index)),
            'bucket_counts': dict(Counter(r['bucket'] for r in shard.index)),
            'special_ids_full_stream': special.tolist(), 'eos_density_stream': int(special[3])/len(shard.tokens),
            'consumed': consumed, 'sample_seed': 42, 'sample_count': count,
            'sample_repetitive_prefixes': sum(r['repetition'] for r in sample),
            'sample_char4gram': describe([r['char_4gram_repeat_fraction'] for r in sample]),
            'sample_token4gram_first2048': describe([r['token_4gram_repeat_fraction_first2048'] for r in sample]),
            'sample_rows': sample}
        write_json(destination/f'data-{name}.json', datasets[name])
        print(json.dumps({'stage': 'cpu-data', 'dataset': name, 'seconds': time.monotonic()-started}), flush=True)
        del shard
        gc.collect()
    full_eos = {}
    for name, path in (('100M', ROOT/'reports/phase6/readiness-20261003/expanded_dev_baseline.json'),
                       ('decay500M', RUN/'evaluation-500M/full-dev.json')):
        body = read_json(path)['body']
        full_eos[name] = {'report': binding(path), 'documents': body['documents'], 'eos_nll': body['eos_nll'],
            'mean_eos_nll': body['eos_nll']/body['documents'],
            'geometric_mean_eos_probability': math.exp(-body['eos_nll']/body['documents'])}
    result = {'completed_at': now(), 'seconds': time.monotonic()-started,
        'generation_bindings': {k: binding(p) for k,p in GENERATION.items()},
        'paired_transitions': paired, 'output_details': output_details,
        'data_reports': {k: binding(destination/f'data-{k}.json') for k in datasets},
        'full_dev_eos': full_eos}
    write_json(destination/'cpu.json', result)
    return result


def logit_stats(scores):
    scores = scores.float()
    assert bool(torch.isfinite(scores).all())
    probabilities = scores.softmax(-1)
    return {'eos_probability': float(probabilities[3]), 'eos_rank': int((scores > scores[3]).sum())+1,
        'eos_is_argmax': int(scores.argmax()) == 3, 'top_probability': float(probabilities.max()),
        'entropy_nats': float(-(probabilities*probabilities.clamp_min(1e-30).log()).sum())}


@torch.inference_mode()
def greedy(model, tok, case, deadline):
    prompt = [2, *tok.encode(case['prefix'])]
    ids, cache, trace = [], None, []
    current = torch.tensor([prompt], device='cuda')
    for _ in range(64):
        if time.monotonic() >= deadline:
            raise TimeoutError('Predeclared GPU inference budget exhausted')
        with torch.autocast('cuda', dtype=torch.bfloat16):
            result = model(current, cache=cache, use_cache=True)
        cache = result.cache
        scores = result.logits[0,-1].clone()
        trace.append(logit_stats(scores))
        scores[list(SUPPRESS_IDS)] = -torch.inf
        token = int(scores.argmax())
        ids.append(token)
        if token == 3:
            break
        current = torch.tensor([[token]], device='cuda')
    raw = tok.decode_bytes(ids)
    try:
        text, valid = raw.decode(), True
    except UnicodeDecodeError:
        text, valid = raw.decode(errors='replace'), False
    return {**case, 'generated_ids': ids, 'text': text, **repetition_details(text),
        'valid_utf8': valid, 'eos': ids[-1] == 3, 'trace': trace,
        'token_4gram_repeat_fraction': repeated_ngram_fraction(ids)}


@torch.inference_mode()
def ending_probes(model, shard, cases, count, deadline):
    endings, prefixes = [], []
    for document in shard.index[:count]:
        if time.monotonic() >= deadline:
            raise TimeoutError('GPU inference budget exhausted')
        start, length = document['offset'], document['body_tokens']
        prompt = shard.tokens[max(start,start+length+1-1024):start+length+1].astype(np.int64)
        assert len(prompt) <= 1024 and shard.tokens[start+length+1] == 3
        with torch.autocast('cuda', dtype=torch.bfloat16):
            logits = model(torch.tensor(prompt[None], device='cuda')).logits[0,-1]
        endings.append({'doc_id': document['doc_id'], 'body_tokens': length, 'context_tokens': len(prompt), **logit_stats(logits)})
    for case in cases:
        with torch.autocast('cuda', dtype=torch.bfloat16):
            logits = model(torch.tensor([case['prompt_ids']], device='cuda')).logits[0,-1]
        prefixes.append({'id': case['id'], 'context_tokens': len(case['prompt_ids']), **logit_stats(logits)})
    return {'method': 'Same first256 dev documents, EOS after last min(1024, BOS+body) tokens; short prefixes are not known true endings',
        'endings': endings, 'prefixes': prefixes,
        'ending_eos_argmax': sum(r['eos_is_argmax'] for r in endings),
        'ending_eos_probability': describe([r['eos_probability'] for r in endings]),
        'ending_eos_rank': describe([r['eos_rank'] for r in endings]),
        'prefix_eos_probability': describe([r['eos_probability'] for r in prefixes]),
        'prefix_eos_argmax': sum(r['eos_is_argmax'] for r in prefixes)}


@torch.inference_mode()
def precision_probes(model, tok, cases, existing, deadline):
    rows = []
    tolerance = read_json(ROOT/'configs/evaluation/protocol.json')['numeric_tolerances']['fp32_reference_logits']
    for case in cases[:8]:
        row = next(r for r in existing if r['id'] == case['id'] and r['decoding'] == 'greedy' and r['suppressed'])
        sequence = [2, *tok.encode(case['prefix']), *row['generated_ids'][:16]]
        tensor = torch.tensor([sequence], device='cuda')
        logits = {}
        for dtype in ('fp32', 'bf16'):
            if time.monotonic() >= deadline:
                raise TimeoutError('GPU inference budget exhausted')
            with torch.autocast('cuda', dtype=torch.bfloat16) if dtype == 'bf16' else nullcontext():
                full = model(tensor).logits
                split = len(sequence)//2
                head = model(tensor[:,:split], use_cache=True)
                tail = model(tensor[:,split:], cache=head.cache, use_cache=True).logits
            assert bool(torch.isfinite(full).all()) and bool(torch.isfinite(tail).all())
            left, right = full[:,split:].float(), tail.float()
            delta = (left-right).abs()
            logits[dtype] = full.float()
            rows.append({'id': case['id'], 'dtype': dtype, 'sequence_tokens': len(sequence), 'split': split,
                'cache_max_abs_error': float(delta.max()),
                'cache_argmax_differences': int((left.argmax(-1) != right.argmax(-1)).sum()),
                'within_original_fp32_tolerance': bool((delta <= tolerance['atol']+tolerance['rtol']*left.abs()).all())})
        rows.append({'id': case['id'], 'comparison': 'full-BF16-versus-FP32-forced-same-prefix',
            'max_abs_error': float((logits['fp32']-logits['bf16']).abs().max()),
            'argmax_differences': int((logits['fp32'].argmax(-1) != logits['bf16'].argmax(-1)).sum())})
    return {'tolerance': tolerance, 'rows': rows, 'scope': '8 short forced prefixes; BF16 has no FP32-equivalence acceptance claim'}


def gpu_diagnostics(destination, config, plan):
    seed_all(42)
    torch.set_num_threads(2)
    cases = [json.loads(line) for line in (ROOT/'eval/base.jsonl').read_text().splitlines()]
    cases = [r for r in cases if r['split'] == 'dev']
    assert len(cases) == plan['budgets']['trajectory_cases'] == 80
    tok = Tokenizer(ROOT/config['tokenizer'])
    for case in cases:
        case['prompt_ids'] = [2, *tok.encode(case['prefix'])]
    existing = {k: read_json(p)['generation']['outputs'] for k,p in GENERATION.items()}
    started = time.monotonic()
    deadline = started + plan['budgets']['GPU_inference_seconds']
    records = {}
    with gpu_lock('cuda'), sdpa_kernel([SDPBackend.MATH]):
        dev = Shard(Path(config['shards']), 'dev')
        for name, path in CHECKPOINTS.items():
            stage_started = time.monotonic()
            state = torch.load(path, map_location='cpu', weights_only=False)
            record = {**binding(path), 'tokens': state['tokens'], 'update': state['update']}
            model = JMicroModel(state['model_config']).to('cuda')
            model.load_state_dict(state['model'], strict=True)
            model.eval()
            before_rng = rng_state()
            before = {k:v.clone() for k,v in model.state_dict().items()}
            assert all(bool(torch.isfinite(v).all()) for v in before.values())
            if name.startswith('stable'):
                record['trajectory'] = [greedy(model, tok, case, deadline) for case in cases]
                record['repetition'] = sum(r['repetition'] for r in record['trajectory'])
                record['eos'] = sum(r['eos'] for r in record['trajectory'])
            else:
                reproduced = [greedy(model, tok, case, deadline) for case in cases[:8]]
                record['reproduction'] = [{'id': row['id'], 'identical_generated_ids': row['generated_ids'] == next(r['generated_ids'] for r in existing[name] if r['id'] == row['id'] and r['decoding'] == 'greedy' and r['suppressed']), 'diagnostic': row} for row in reproduced]
                record['precision'] = precision_probes(model, tok, cases, existing[name], deadline)
            if name in ('100M', 'stable500M', 'decay500M'):
                record['ending_probes'] = ending_probes(model, dev, cases, plan['budgets']['teacher_dev_documents'], deadline)
            record['state_and_rng_unchanged'] = equal_state(before_rng, rng_state()) and equal_state(before, model.state_dict())
            assert record['state_and_rng_unchanged']
            record['seconds'] = time.monotonic()-stage_started
            record['checkpoint_unchanged'] = sha256(path) == record['sha256']
            assert record['checkpoint_unchanged']
            write_json(destination/f'gpu-{name}.json', record)
            records[name] = binding(destination/f'gpu-{name}.json')
            write_json(destination/'job.json', {'status': 'running', **identity(), 'stage': name,
                'at': now(), 'elapsed_seconds': time.monotonic()-started, 'completed': records})
            print(json.dumps({'stage': name, 'seconds': record['seconds'], 'repetition': record.get('repetition'), 'eos': record.get('eos'), 'end_eos_argmax': record.get('ending_probes',{}).get('ending_eos_argmax')}), flush=True)
            del model, state, before
            gc.collect()
            torch.cuda.empty_cache()
    result = {'seconds': time.monotonic()-started, 'budget_seconds': plan['budgets']['GPU_inference_seconds'],
        'records': records, 'suite': binding(ROOT/'eval/base.jsonl'), 'tokenizer': binding(ROOT/config['tokenizer']),
        'training_updates': 0, 'completed_at': now()}
    assert result['seconds'] <= result['budget_seconds']
    write_json(destination/'gpu.json', result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--phase', choices=['cpu','gpu'], required=True)
    parser.add_argument('--destination', type=Path, default=ROOT/'reports/phase6/repetition-diagnosis-20261003')
    args = parser.parse_args()
    args.destination.mkdir(parents=True, exist_ok=True)
    plan_path = ROOT/'reports/phase6/repetition_diagnosis_plan.json'
    config = read_json(ROOT/'configs/phase6/base_frozen.json')
    plan = read_json(plan_path)
    job = {'status': 'running', **identity(), 'phase': args.phase, 'started_at': now(),
        'plan': binding(plan_path), 'command': sys.argv, 'source': {
            name: sha256(ROOT/name) for name in ('scripts/investigate_repetition.py','src/jmicro/repetition_diagnosis.py')}}
    write_json(args.destination/f'job-{args.phase}.json', job)
    try:
        function = cpu_diagnostics if args.phase == 'cpu' else gpu_diagnostics
        result = function(args.destination, config, plan)
    except BaseException as error:
        write_json(args.destination/f'job-{args.phase}.json', {**job, 'status': 'failed', 'finished_at': now(), 'error': repr(error)})
        raise
    write_json(args.destination/f'job-{args.phase}.json', {**job, 'status': 'complete', 'finished_at': now(), 'seconds': result['seconds']})
    if args.phase == 'gpu':
        write_json(args.destination/'job.json', {**job, 'status': 'complete', 'finished_at': now(), 'seconds': result['seconds'], 'completed': result['records']})
    print(json.dumps({'status': 'complete', 'phase': args.phase, 'seconds': result['seconds']}), flush=True)


if __name__ == '__main__':
    main()
