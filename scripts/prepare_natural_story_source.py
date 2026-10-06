"""Reuse immutable whole TRAIN stories and cache; no new prose or corpus scan."""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
from pathlib import Path
import sys
import time
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.eos_pilot import TrainView
from jmicro.tokenizer import Tokenizer
from cached_three_source_index import CachedThreeSourceIndex
from phase6_performance import identity

RUN = ROOT / 'reports/phase6/natural-story-source-20261006'
PROPOSAL = ROOT / 'reports/phase6/natural_story_source_reuse_proposal.json'
SEED = 2026100692


def main():
    started = time.monotonic(); p = read_json(PROPOSAL)
    if (RUN / 'job.json').exists(): raise ValueError('Preserve actual fixed source preparation; no reroll')
    if p['source_sha256'] != {s: sha256(ROOT / s) for s in p['source_sha256']}:
        raise ValueError('Frozen preparation source differs')
    for ref in p['references'].values():
        if sha256(Path(ref['path'])) != ref['sha256']: raise ValueError('Accepted provenance/control reference differs')
    RUN.mkdir(parents=True, exist_ok=True)
    job = dict(status='preparing', **identity(), started_at=now(), proposal_sha256=sha256(PROPOSAL),
        CPU_ceiling_seconds=60, GPU_seconds=0, student_scientific_teacher_tokens=0, protected_test_used=False,
        restart_command='Preserve actual fixed/partial source; do not reroll or alter selection after reading.')
    atomic_json(RUN / 'job.json', job)
    try:
        accepted = read_json(Path(p['references']['accepted_pool_review']['path']))
        source = p['pool']; view = TrainView(source['path'], source['manifest_sha256'])
        if not accepted['passed'] or accepted['weak_documents'] > 10 or accepted['pools']['large']['manifest_sha256'] != source['manifest_sha256']:
            raise ValueError('Existing accepted original mixture required')
        cache = view.directory / ('.compact-index-' + source['manifest_sha256'][:16]) / 'ready.json'
        if not cache.exists(): raise ValueError('Accepted compact cache missing; refuse13GB index parse')
        view.index = CachedThreeSourceIndex(view)
        if not view.index.cache_reused: raise ValueError('Existing cache required')
        documents = np.flatnonzero(view.index.sources == 1)
        lengths = view.index.lengths[documents].astype(np.int64)
        offsets = view.index.offsets[documents]
        if (len(documents) < 64 or np.any(lengths <= 0) or np.any(lengths+1 > 1024)
                or not np.all(view.tokens[offsets] == 2) or not np.all(view.tokens[offsets+lengths+1] == 3)):
            raise ValueError('All source-train whole story boundaries and native context limit required')
        selected = np.random.default_rng(SEED).choice(documents, 64, replace=False)
        tok = Tokenizer(ROOT / p['tokenizer']['path']); rows = []
        for index, doc in enumerate(selected.tolist()):
            start, length = int(view.index.offsets[doc]), int(view.index.lengths[doc])
            body = view.tokens[start+1:start+1+length].tolist(); raw = tok.decode_bytes(body); text = raw.decode('utf-8')
            if tok.encode(text) != body or any(i < 8 for i in body) or not text:
                raise ValueError('Native exact source body required; never repair/filter/reroll')
            rows.append(dict(index=index, id=f'story-train-index-{doc}', original_document_index=doc, split='train',
                offset=start, body_tokens=length, body_bytes=len(raw), text=text,
                text_sha256=__import__('hashlib').sha256(raw).hexdigest(),
                original_source='existing_builder_source_train_whole_story', unchanged_original_native_tokens=True))
        if len({r['text_sha256'] for r in rows}) != 64: raise ValueError('Duplicate pilot bodies; preserve failure, no reroll')
        pilot = dict(rows=rows, seed=SEED, selection='Uniform64 without replacement from ALL existing source-train story document indices, before reading; no content/length filter',
            protected_test_used=False, source_families_not_claimed_independent=True)
        atomic_json(RUN / 'content-pilot.json', pilot)
        manifest = dict(kind='existing_whole_TRAIN_story_reuse_v1', created_at=now(), pool=source,
            documents=len(documents), body_tokens=int(lengths.sum()), serialized_tokens=int((lengths+2).sum()),
            body_plus_EOS_targets=int((lengths+1).sum()), EOS_targets=len(documents),
            body_length_min=int(lengths.min()), body_length_max=int(lengths.max()),
            original_document_indices_sha256=__import__('hashlib').sha256(documents.astype('<i8').tobytes()).hexdigest(),
            original_builder_and_split_provenance=ref(Path(p['references']['accepted_pool_ready']['path'])),
            cache=ref(cache), cache_reused=True, original13GB_index_rescanned=False,
            original_corpus_redownloaded=False, new_original_corpus_tokens=0, new_prose_authored=False,
            source_tokens_unchanged=True, full_stream_audit_repeated=False,
            all_story_boundaries_and_context_limit_checked=True, native64_codec_checked=True,
            tokenizer_sha256=p['tokenizer']['sha256'], pilot_sha256=sha256(RUN/'content-pilot.json'),
            proposal_sha256=sha256(PROPOSAL), source_sha256=p['source_sha256'],
            training_pool_accepted=False, protected_test_used=False, actual_GPU_seconds=0,
            limitations='Reuse of existing source-train translations/story material, not new corpus, new independent families or verified human original Japanese. Prior builder hashes/splits reused; global near/site/author audit remains incomplete.')
        atomic_json(RUN / 'manifest.json', manifest)
        elapsed = time.monotonic()-started
        if elapsed > 60: raise TimeoutError('CPU60s ceiling exceeded; preserve actual failure')
        job.update(status='complete_pending_fixed64_content', CPU_seconds=elapsed, completed_at=now(),
            manifest_sha256=sha256(RUN/'manifest.json'), documents=len(documents), serialized_tokens=manifest['serialized_tokens'])
        atomic_json(RUN/'job.json', job)
        print(json.dumps(dict(status=job['status'], CPU_seconds=elapsed, documents=len(documents), serialized_tokens=manifest['serialized_tokens'])), flush=True)
    except BaseException as error:
        job.update(status='failed_preserve_fixed_or_partial', CPU_seconds=time.monotonic()-started, error=repr(error), ended_at=now())
        atomic_json(RUN/'job.json', job); raise


def ref(path): return dict(path=str(path), sha256=sha256(path))


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
