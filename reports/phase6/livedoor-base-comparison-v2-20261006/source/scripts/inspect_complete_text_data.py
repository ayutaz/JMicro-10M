"""Bounded train-only inspection; launch with the pinned uv interpreter."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, write_json, sha256
from jmicro.shards import BlockSampler
from jmicro.tokenizer import Tokenizer
from run_eos_short_pilot import sentence_complete


def sample_documents(view, tok, count, seed):
    rng, seen, rows = np.random.default_rng(seed), set(), []
    attempts = 0
    while len(rows) < count and attempts < count * 100:
        attempts += 1
        probe = int(rng.integers(1, len(view.tokens) - 1))
        left = max(0, probe - 16384)
        local = view.tokens[left:probe + 1]
        beginnings = np.flatnonzero(local == 2)
        if not len(beginnings):
            continue
        start = left + int(beginnings[-1])
        ends = np.flatnonzero(view.tokens[start + 1:start + 16385] == 3)
        if not len(ends) or start in seen:
            continue
        end = start + 1 + int(ends[0])
        seen.add(start)
        ids = view.tokens[start + 1:end].tolist()
        raw = tok.decode_bytes(ids)
        text = raw.decode('utf-8')
        rows.append(dict(offset=start, end=end, body_tokens=len(ids), text=text,
                         punctuation_complete=sentence_complete(text),
                         special_body_ids=[i for i in ids if i < 8]))
    if len(rows) != count:
        raise ValueError('Insufficient bounded inspection sample')
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, default=ROOT / 'reports/phase6/complete-text-10b-100m-20261004/data-inspection')
    args = parser.parse_args()
    assert sys.version_info[:3] == (3, 12, 7)
    old = read_json(ROOT / 'configs/phase6/eos_5b_finish_100m.json')
    tok = Tokenizer(ROOT / old['tokenizer'])
    args.output.mkdir(parents=True, exist_ok=True)
    sources = {}
    for name, directory, digest in (
        ('web', old['web_shards'], old['web_manifest_sha256']),
        ('short', old['short_pool'], old['short_manifest_sha256'])):
        view = TrainView(directory, digest)
        rows = sample_documents(view, tok, 100, 20261004)
        write_json(args.output / (name + '.json'), rows)
        sources[name] = dict(manifest_sha256=digest, count=len(rows),
                             punctuation_complete=sum(r['punctuation_complete'] for r in rows),
                             special_body_ids=sum(bool(r['special_body_ids']) for r in rows),
                             sample_sha256=sha256(args.output / (name + '.json')))
    from types import SimpleNamespace
    fixture = SimpleNamespace(tokens=np.tile([2, 8, 9, 3], 64).astype('<u2'),
                              byte_lengths=np.array([0]*8+[1, 1]))
    x, y, _ = BlockSampler(fixture, 8, 42).batch(2)
    checks = dict(EOS_target_supervised=int(y.eq(3).sum()) == 4,
                  BOS_target_masked=int(y.eq(-100).sum()) == 4,
                  no_BOS_targets=not bool(y.eq(2).any()),
                  packed_next_token_shift=bool(np.array_equal(x[:, 1:].numpy(),
                        np.where(y[:, :-1].numpy() == -100, 2, y[:, :-1].numpy()))))
    assert all(checks.values()), checks
    write_json(args.output / 'result.json', dict(sources=sources, boundary_checks=checks,
        sample_policy='fixed-seed uniform token probes; length-biased document sample; at most16384 tokens backward/forward',
        limitation='sample is not a full-corpus audit; punctuation is not semantic completeness',
        heldout_used=False, GPU_training_started=False))
    print(json.dumps(dict(sources=sources, boundary_checks=checks)), flush=True)


if __name__ == '__main__':
    main()
