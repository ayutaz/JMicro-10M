"""Fixed bounded train inspection after the rejected story-weight study."""
import hashlib
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.tokenizer import Tokenizer
from cached_three_source_index import CachedThreeSourceIndex
from phase6_performance import alive

GENRES = ('web', 'story', 'textbook')
SEED = 2026100643
OUTPUT = ROOT / 'reports/phase6/conditional-content-pilot-20261006'


def select_documents(index, count=32, seed=SEED, attempts=50000, deadline=None):
    rng = np.random.default_rng(seed)
    selected = {genre: [] for genre in GENRES}; seen = set()
    for _ in range(attempts):
        if deadline is not None and time.monotonic() > deadline:
            raise TimeoutError('Bounded CPU selection exhausted')
        document = int(rng.integers(len(index.lengths)))
        genre = GENRES[int(index.sources[document])]
        if document in seen or len(selected[genre]) == count or not 64 <= int(index.lengths[document]) <= 512:
            continue
        seen.add(document); selected[genre].append(document)
        if all(len(ids) == count for ids in selected.values()):
            return selected
    raise ValueError('Insufficient fixed length/source sample within bounded attempts')


def main():
    started = time.monotonic()
    if OUTPUT.exists(): raise ValueError('Preserve fixed pilot; inspect it rather than resample')
    run = ROOT / 'reports/phase6/story-weight-comparison-20261006'
    review = read_json(run / 'review.json'); job = read_json(run / 'job.json')
    if (job['status'] != 'complete' or alive(job) or review['result_sha256'] != sha256(run / 'compare-result.json')
            or any(review['eligible_for_final_Base_validation'].values())):
        raise ValueError('Completed rejected comparison required for this branch')
    c = read_json(ROOT / 'configs/phase6/story_weight_comparison.json')
    cache = Path(c['accepted_compact_index']['path'])
    if not cache.exists() or sha256(cache) != c['accepted_compact_index']['sha256']:
        raise ValueError('Accepted compact cache missing; refuse original index rescan')
    view = TrainView(c['pool']['pool'], c['pool']['manifest_sha256'])
    index = CachedThreeSourceIndex(view)
    if not index.cache_reused: raise ValueError('Original corpus must not be rescanned')
    base = read_json(Path(c['original_config']['path']))
    tok = Tokenizer(ROOT / base['tokenizer'])
    if sha256(ROOT / base['tokenizer']) != base['tokenizer_sha256']:
        raise ValueError('Fixed tokenizer differs')
    selected = select_documents(index, deadline=started + 30)
    rows = []
    for genre, documents in selected.items():
        for document in documents:
            offset = int(index.offsets[document]); count = int(index.lengths[document])
            ids = view.tokens[offset:offset + count + 2].tolist()
            if ids[0] != 2 or ids[-1] != 3 or any(token < 8 for token in ids[1:-1]):
                raise ValueError('Complete BOS/body/EOS train document differs')
            body = tok.decode_bytes(ids[1:-1])
            rows.append(dict(id=f'{genre}-{len(rows):03d}', genre=genre, document_index=document,
                train_offset=offset, body_tokens=count, body_bytes=len(body), token_ids=ids,
                decoded_body_sha256=hashlib.sha256(body).hexdigest(), text=body.decode('utf-8')))
    elapsed = time.monotonic() - started
    if elapsed > 30: raise TimeoutError('CPU30s inspection limit exhausted')
    OUTPUT.mkdir(parents=True)
    write_json(OUTPUT / 'source-sample.json', dict(rows=rows))
    write_json(OUTPUT / 'result.json', dict(status='fixed96_train_content_inspection_ready_unreviewed',
        created_at=now(), CPU_seconds=elapsed, CPU_ceiling_seconds=30, seed=SEED,
        documents=len(rows), source_documents={g: len(ids) for g, ids in selected.items()},
        length_range=[64, 512], body_tokens=sum(r['body_tokens'] for r in rows),
        body_bytes=sum(r['body_bytes'] for r in rows), original_index_rescan=False,
        cache_reference=c['accepted_compact_index'], material_manifest_sha256=c['pool']['manifest_sha256'],
        tokenizer_sha256=base['tokenizer_sha256'],
        sample_sha256=sha256(OUTPUT / 'source-sample.json'), script_sha256=sha256(Path(__file__)),
        prior_review_sha256=sha256(run / 'review.json'), actual_GPU_seconds=0,
        scientific_teacher_tokens=0, newly_prepared_tokens=0, content_acceptance_complete=False,
        protected_test_used=False, Base_adopted=False, requested_five_steps_complete=False,
        completion_condition='Personally read all96 normalized train documents and record grammatical completeness, explicit negation/quantity/time/comparison/entity/causal conditions and outcome links. Distinguish absent conditions from broken conditions. Select one supported train-only comparison or record insufficient evidence; never use dev prompts as training examples.',
        limitations='Uniform document draws restricted to64..512 body tokens and fixed32/source. Decoded normalized train bodies, not raw original source bytes. This small nonblind inspection cannot estimate whole-corpus quality, distinct source-family supply or global deduplication. No new data or GPU learning.'))
    print(f'Fixed96 train documents saved; CPU {elapsed:.3f}s; GPU/science/new prepared0; all96 content review pending', flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
