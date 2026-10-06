"""One bounded readonly comparison of frozen DEV document representations."""
import argparse
from collections import Counter
import gc
import hashlib
import json
from pathlib import Path
import signal
import sys
import time

sys.path[:0] = [str(Path(__file__).resolve().parents[1] / 'src'), str(Path(__file__).resolve().parent)]
import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock
from natural_context_contrast_trainer import right_pad, right_padded_hidden
from phase6_performance import alive, identity

RUN = ROOT / 'reports/phase6/natural-context-contrast-dev-transfer-20261007'
CONFIG = ROOT / 'configs/phase6/natural_context_contrast_dev_transfer.json'
SCIENCE = ROOT / 'reports/phase6/natural-context-contrast-comparison-20261007'
RECIPE = ROOT / 'configs/phase6/natural_context_contrast_comparison.json'
PROPOSAL = ROOT / 'reports/phase6/natural_context_contrast_dev_transfer_proposal.json'
SOURCES = ('scripts/run_natural_context_contrast_dev_transfer.py',
           'scripts/run_natural_context_contrast_dev_transfer.ps1',
           'scripts/natural_context_contrast_trainer.py', 'src/jmicro/model.py',
           'src/jmicro/tokenizer.py', 'uv.lock')


def reference(path):
    return dict(path=str(path), sha256=sha256(path))


def fixed_body_rows(cache, checkpoint_sha256, count=256):
    body = cache['body']
    binding = json.loads(cache['binding'])
    if (binding['checkpoint_sha256'] != checkpoint_sha256 or body['split'] != 'dev'
            or body['documents'] != count or len(body['rows']) != count):
        raise ValueError('Exact completed DEV body cache required')
    return body['rows']


def make_pairs(documents, tokens, tok, expected, limit=64, context=1024):
    """Fixed evaluation order; no text editing, truncation or train/test fallback."""
    if len(documents) < len(expected):
        raise ValueError('Incomplete fixed DEV index')
    for row, cached in zip(documents, expected):
        if (row['split'] != 'dev' or
            (row['doc_id'], row['body_tokens'], row['bytes']) !=
            (cached['doc_id'], cached['body_tokens'], cached['body_bytes'])):
            raise ValueError('Fixed DEV IDs/body accounting differ')
    rows, excluded, seen = [], Counter(), set()
    for row in documents[:len(expected)]:
        count = row['body_tokens']
        if count < 16 or count > 2 * (context - 1):
            excluded['body_length_not_executable'] += 1
            continue
        offset = row['offset']
        serial = tokens[offset:offset + count + 2].astype(int).tolist()
        if len(serial) != count + 2 or serial[0] != 2 or serial[-1] != 3:
            raise ValueError('Original DEV serialization differs')
        body = serial[1:-1]
        if min(body) < 8:
            raise ValueError('Unexpected special token in original DEV body')
        raw = tok.decode_bytes(body)
        digest = hashlib.sha256(raw).hexdigest()
        if digest != row['canonical_sha256'] or len(raw) != row['bytes']:
            raise ValueError('Original DEV body bytes differ')
        try:
            raw.decode('utf-8')
        except UnicodeDecodeError:
            excluded['invalid_body_UTF8'] += 1
            continue
        if digest in seen:
            excluded['exact_body_duplicate'] += 1
            continue
        cuts = sorted(range(8, count - 7), key=lambda cut: (abs(2 * cut - count), cut))
        cut = None
        for candidate in cuts:
            if max(candidate, count - candidate) > context - 1:
                continue
            left, right = tok.decode_bytes(body[:candidate]), tok.decode_bytes(body[candidate:])
            try:
                left.decode('utf-8'); right.decode('utf-8')
            except UnicodeDecodeError:
                continue
            if left + right != raw:
                raise ValueError('Original prefix/suffix token bytes differ')
            cut = candidate
            break
        if cut is None:
            excluded['no_executable_UTF8_half_boundary'] += 1
            continue
        seen.add(digest)
        rows.append(dict(doc_id=row['doc_id'], split='dev', original_index=row,
            body_sha256=digest, body_bytes=len(raw), body_tokens=count,
            prefix_ids=body[:cut], suffix_ids=body[cut:], token_cut=cut,
            appended_EOS=False))
        if len(rows) == limit:
            return rows, dict(excluded)
    raise ValueError(f'Only {len(rows)}/{limit} eligible fixed DEV pairs; no substitute source')


def retrieval(left, right, rows):
    if left.shape != right.shape or len(left) != len(rows) or len(rows) < 2:
        raise ValueError('Same complete representation pairs required')
    left, right = F.normalize(left.float(), dim=-1), F.normalize(right.float(), dim=-1)
    cosine = left @ right.T
    if not bool(torch.isfinite(cosine).all()):
        raise ValueError('Nonfinite representation scores')
    positive = cosine.diag()
    mask = ~torch.eye(len(rows), dtype=torch.bool, device=cosine.device)
    distractor = cosine.masked_fill(~mask, -torch.inf)
    records = []
    for i, row in enumerate(rows):
        records.append(dict(doc_id=row['doc_id'], positive_cosine=float(positive[i]),
            prefix_to_suffix_rank=int((cosine[i] > positive[i]).sum()) + 1,
            suffix_to_prefix_rank=int((cosine[:, i] > positive[i]).sum()) + 1,
            prefix_to_suffix_unique_top1=bool(positive[i] > distractor[i].max()),
            suffix_to_prefix_unique_top1=bool(positive[i] > distractor[:, i].max()),
            prefix_positive_ties=int((cosine[i] == positive[i]).sum()),
            suffix_positive_ties=int((cosine[:, i] == positive[i]).sum())))
    labels = torch.arange(len(rows), device=cosine.device)
    return dict(pairs=len(rows), temperature=0.1, rows=records,
        bidirectional_unique_top1=sum(r['prefix_to_suffix_unique_top1'] +
            r['suffix_to_prefix_unique_top1'] for r in records) / (2 * len(rows)),
        symmetric_InfoNCE=float((F.cross_entropy(cosine / .1, labels) +
                                 F.cross_entropy(cosine.T / .1, labels)) / 2),
        mean_positive_cosine=float(positive.mean()),
        mean_distractor_cosine=float(cosine[mask].mean()),
        representation_variance=float(torch.minimum(left.var(0, unbiased=False).mean(),
                                                    right.var(0, unbiased=False).mean())),
        cosine_matrix=cosine.cpu().tolist())


def prepare():
    started = time.monotonic()
    if CONFIG.exists() or (RUN / 'cases.json').exists():
        raise ValueError('Preserve prepared inputs; no repeated draw')
    job = read_json(SCIENCE / 'job.json')
    if job['status'] != 'complete' or alive(job):
        raise ValueError('Completed scientific process required')
    recipe, proposal = read_json(RECIPE), read_json(PROPOSAL)
    if proposal['GPU_diagnostic_budget_seconds'] != 60:
        raise ValueError('Original bounded proposal required')
    dev = Path(recipe['dev_shards'])
    if sha256(dev / 'manifest.json') != recipe['dev_manifest_sha256']:
        raise ValueError('Fixed DEV manifest differs')
    manifest = read_json(dev / 'manifest.json')
    if sha256(dev / 'dev.index.json') != manifest['splits']['dev']['index_sha256']:
        raise ValueError('Fixed DEV index differs')
    if sha256(ROOT / recipe['tokenizer']) != recipe['tokenizer_sha256']:
        raise ValueError('Pinned tokenizer differs')
    stream = dev / 'dev.bin'
    if stream.stat().st_size != manifest['splits']['dev']['tokens'] * 2:
        raise ValueError('Fixed DEV stream size differs')
    body_path = SCIENCE / 'evaluation/CE/evaluation/body.json'
    expected = fixed_body_rows(read_json(body_path),
        read_json(SCIENCE / 'CE/train-result.json')['checkpoint_sha256'])
    if len(expected) != 256:
        raise ValueError('Fixed DEV256 source required')
    tok = Tokenizer(ROOT / recipe['tokenizer'])
    rows, excluded = make_pairs(read_json(dev / 'dev.index.json'),
        np.memmap(stream, dtype='<u2', mode='r'), tok, expected)
    checkpoints = {'original': recipe['parent']}
    for arm in ('CE', 'contrast'):
        trained = read_json(SCIENCE / arm / 'train-result.json')
        if trained['status'] != 'complete' or trained['scientific_CE_teacher_tokens'] != 100000000:
            raise ValueError('Exact completed100M endpoint required')
        checkpoints[arm] = dict(path=trained['checkpoint'], sha256=trained['checkpoint_sha256'])
    for checkpoint in checkpoints.values():
        path = Path(checkpoint['path'])
        if sha256(path) != checkpoint['sha256']:
            raise ValueError('Documented checkpoint differs')
        checkpoint.update(size=path.stat().st_size, mtime_ns=path.stat().st_mtime_ns)
    if time.monotonic() - started > 30:
        raise TimeoutError('Bounded preparation30s exhausted')
    RUN.mkdir(parents=True, exist_ok=True)
    atomic_json(RUN / 'cases.json', dict(rows=rows, exclusions=excluded))
    config = dict(created_at=now(), proposal=reference(PROPOSAL), recipe=reference(RECIPE),
        reference_body=reference(body_path), cases=reference(RUN / 'cases.json'),
        dev_manifest=reference(dev / 'manifest.json'), checkpoints=checkpoints,
        source_sha256={p:sha256(ROOT / p) for p in SOURCES}, GPU_limit_seconds=60,
        preparation_CPU_seconds=time.monotonic()-started, pairs=64, microbatch_sequences=16,
        selection='Fixed DEV256 order; first64 distinct original bodies,16..2046 tokens, each half8..1023 and valid UTF8. No text rewriting/truncation, outcome-based selection or alternate source.',
        DEV_stream_full_hash_repeated=False, selected_original_body_hashes_verified=True,
        new_teacher_tokens=0, optimizer_updates=0, protected_test_used=False,
        Base_complete=False, Chat_started=False, quantization_started=False)
    atomic_json(CONFIG, config)
    print(json.dumps(dict(status='prepared', pairs=64, exclusions=excluded,
        CPU_seconds=config['preparation_CPU_seconds'])))


def inspect():
    config = read_json(CONFIG)
    for ref in (config['recipe'], config['proposal'], config['cases'], config['dev_manifest']):
        if sha256(Path(ref['path'])) != ref['sha256']:
            raise ValueError('Frozen readonly input differs')
    if any(sha256(ROOT / p) != digest for p,digest in config['source_sha256'].items()):
        raise ValueError('Frozen implementation differs')
    for checkpoint in config['checkpoints'].values():
        stat = Path(checkpoint['path']).stat()
        if (stat.st_size, stat.st_mtime_ns) != (checkpoint['size'], checkpoint['mtime_ns']):
            raise ValueError('Checkpoint changed since exact SHA preparation')
    if (RUN / 'job.json').exists():
        raise ValueError('Preserve terminal or active one-shot; inspect actual identity, do not restart')
    prior = read_json(SCIENCE / 'job.json')
    if prior['status'] != 'complete' or alive(prior):
        raise ValueError('Existing scientific job not actually finished')
    return config


def run():
    config = inspect()
    rows = read_json(Path(config['cases']['path']))['rows']
    job = dict(status='starting', **identity(), started_at=now(), config_sha256=sha256(CONFIG),
        GPU_limit_seconds=60, GPU_occupancy_seconds=0, new_teacher_tokens=0, optimizer_updates=0,
        Base_complete=False, Chat_started=False, quantization_started=False)
    started = None
    atomic_json(RUN / 'job.json', job)
    def check(*_):
        if started is not None and time.monotonic() - started >= 60:
            raise TimeoutError('Readonly GPU60s exhausted')
    def deadline(*_):
        raise TimeoutError('Readonly hard GPU60s deadline')
    signal.signal(signal.SIGALRM, deadline)
    results = {}
    try:
        with gpu_lock('cuda'):
            started = time.monotonic()
            signal.alarm(60)
            if not torch.cuda.is_available():
                raise RuntimeError('Native CUDA unavailable; no CPU fallback')
            torch.cuda.set_per_process_memory_fraction(.90)
            for arm, checkpoint in config['checkpoints'].items():
                check()
                job.update(status='running', stage=arm)
                atomic_json(RUN / 'job.json', job)
                state = torch.load(checkpoint['path'], map_location='cpu', weights_only=False)
                with torch.random.fork_rng(devices=[]):
                    model = JMicroModel(state['model_config']).to('cuda')
                model.load_state_dict(state['model'], strict=True)
                model.eval()
                if sum(p.numel() for p in model.parameters()) != 10001152:
                    raise ValueError('Original native10M required')
                features = []
                sequences = [[2] + r['prefix_ids'] for r in rows] + [[2] + r['suffix_ids'] for r in rows]
                with torch.inference_mode(), sdpa_kernel(SDPBackend.MATH):
                    for offset in range(0, len(sequences), config['microbatch_sequences']):
                        check()
                        ids, lengths = right_pad(sequences[offset:offset+config['microbatch_sequences']], 'cuda')
                        with torch.autocast('cuda', dtype=torch.bfloat16):
                            hidden = right_padded_hidden(model, ids)
                        features.append(hidden[torch.arange(len(ids), device='cuda'), lengths-1].float().cpu())
                        del hidden, ids
                    features = torch.cat(features)
                    scored = retrieval(features[:64], features[64:], rows)
                check()
                scored.update(checkpoint=checkpoint, input_cases_sha256=config['cases']['sha256'],
                    dtype='bf16', backend='math', parameters=10001152, readonly=True)
                atomic_json(RUN / f'{arm}.json', scored)
                results[arm] = scored
                del model, state, features
                gc.collect(); torch.cuda.empty_cache()
                job.update(completed_models=len(results), GPU_occupancy_seconds=time.monotonic()-started)
                atomic_json(RUN / 'job.json', job)
            check()
            signal.alarm(0)
            elapsed = time.monotonic()-started
            report = dict(status='complete', created_at=now(), actual_identity=identity(),
                config_sha256=sha256(CONFIG), results=results, GPU_occupancy_seconds=elapsed,
                GPU_limit_seconds=60, new_teacher_tokens=0, optimizer_updates=0,
                protected_test_used=False, Base_complete=False, Base_adopted=False,
                Chat_started=False, quantization_started=False, quality_criteria_unchanged=True,
                limitations='One retrospective constructed64 DEV retrieval packet, repeated data and unknown near-family correlations. Other documents are distractors, not certified wrong factual endings. Both retrieval directions share64 cases; do not count128 independent examples. Retrieval success is not generation or next-token quality.',
                next_action='Review same64 matrices/ranks against unchanged failed Base outcomes; close this one-shot diagnostic without automatic training or recipe rescue.')
            atomic_json(RUN / 'result.json', report)
            job.update(status='complete', ended_at=now(), GPU_occupancy_seconds=elapsed)
            atomic_json(RUN / 'job.json', job)
            print(json.dumps(dict(status='complete', GPU_seconds=elapsed,
                retrieval={k:v['bidirectional_unique_top1'] for k,v in results.items()})))
    except BaseException as error:
        signal.alarm(0)
        job.update(status='failed', ended_at=now(), error=repr(error),
            GPU_occupancy_seconds=time.monotonic()-started if started is not None else 0)
        atomic_json(RUN / 'job.json', job)
        raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    torch.set_num_threads(2)
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--prepare', action='store_true')
    group.add_argument('--inspect', action='store_true')
    args = parser.parse_args()
    if args.prepare: prepare()
    elif args.inspect:
        inspect(); print('Frozen readonly diagnostic ready; inspect actual jobs before GPU launch')
    else: run()
