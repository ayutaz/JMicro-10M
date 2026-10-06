"""Repair metadata-only v1 failure; preserve original actual64 bytes/selection."""
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
from pathlib import Path
import sys
import time
import hashlib
import json

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.training import atomic_json
from jmicro.eos_pilot import TrainView
from jmicro.tokenizer import Tokenizer
from cached_three_source_index import CachedThreeSourceIndex
from phase6_performance import identity, alive
from prepare_natural_story_source import RUN, PROPOSAL, SEED


def reference(path): return dict(path=str(path), sha256=sha256(path))


def main():
    started = time.monotonic(); p = read_json(PROPOSAL); original = read_json(RUN/'job.json')
    path = RUN/'metadata-repair-v2.json'; pilot_path = RUN/'content-pilot.json'
    if path.exists() or (RUN/'manifest.json').exists(): raise ValueError('Preserve actual repair/manifest; no repeat')
    if (original['status'] != 'failed_preserve_fixed_or_partial' or alive(original)
            or original['error'] != 'TypeError("\'dict\' object is not callable")' or original['CPU_seconds'] > 60
            or original['proposal_sha256'] != sha256(PROPOSAL) or not pilot_path.exists()):
        raise ValueError('Only original terminal metadata ref shadowing failure may be repaired')
    pilot = read_json(pilot_path); original_pilot_sha = sha256(pilot_path)
    if p['source_sha256'] != {s: sha256(ROOT/s) for s in p['source_sha256']}:
        raise ValueError('Original frozen source differs')
    for item in p['references'].values():
        if sha256(Path(item['path'])) != item['sha256']: raise ValueError('Original fixed references differ')
    repair = dict(status='repairing_metadata_only', **identity(), started_at=now(), original_job=reference(RUN/'job.json'),
        original_pilot_sha256=original_pilot_sha, source_sha256=sha256(Path(__file__)), proposal_sha256=sha256(PROPOSAL),
        CPU_ceiling_seconds=60, original_failed_CPU_seconds=original['CPU_seconds'], GPU_seconds=0,
        student_scientific_teacher_tokens=0, protected_test_used=False)
    atomic_json(path, repair)
    try:
        source = p['pool']; view = TrainView(source['path'], source['manifest_sha256'])
        cache = view.directory / ('.compact-index-'+source['manifest_sha256'][:16]) / 'ready.json'
        if not cache.exists(): raise ValueError('Refuse original13GB index parse')
        view.index = CachedThreeSourceIndex(view)
        if not view.index.cache_reused: raise ValueError('Existing cache required')
        documents = np.flatnonzero(view.index.sources == 1)
        lengths = view.index.lengths[documents].astype(np.int64); offsets = view.index.offsets[documents]
        selected = np.random.default_rng(SEED).choice(documents, 64, replace=False).tolist()
        if (selected != [r['original_document_index'] for r in pilot['rows']] or pilot['seed'] != SEED
                or np.any(lengths+1 > 1024) or np.any(lengths <= 0)
                or not np.all(view.tokens[offsets] == 2) or not np.all(view.tokens[offsets+lengths+1] == 3)):
            raise ValueError('Exact original64 draw/source boundaries must remain unchanged')
        tok = Tokenizer(ROOT/p['tokenizer']['path'])
        for row in pilot['rows']:
            start, length = row['offset'], row['body_tokens']; doc = row['original_document_index']
            body = view.tokens[start+1:start+length+1].tolist(); raw = tok.decode_bytes(body)
            if (start != int(view.index.offsets[doc]) or length != int(view.index.lengths[doc])
                    or raw != row['text'].encode('utf-8') or len(raw) != row['body_bytes']
                    or hashlib.sha256(raw).hexdigest() != row['text_sha256'] or tok.encode(row['text']) != body
                    or any(i < 8 for i in body)):
                raise ValueError('Metadata repair may not change any actual native body')
        manifest = dict(kind='existing_whole_TRAIN_story_reuse_v1', created_at=now(), pool=source,
            documents=len(documents), body_tokens=int(lengths.sum()), serialized_tokens=int((lengths+2).sum()),
            body_plus_EOS_targets=int((lengths+1).sum()), EOS_targets=len(documents),
            body_length_min=int(lengths.min()), body_length_max=int(lengths.max()),
            original_document_indices_sha256=hashlib.sha256(documents.astype('<i8').tobytes()).hexdigest(),
            original_builder_and_split_provenance=p['references']['accepted_pool_ready'],
            cache=reference(cache), cache_reused=True, original13GB_index_rescanned=False,
            original_corpus_redownloaded=False, new_original_corpus_tokens=0, new_prose_authored=False,
            source_tokens_unchanged=True, full_stream_audit_repeated=False,
            all_story_boundaries_and_context_limit_checked=True, native64_codec_checked=True,
            tokenizer_sha256=p['tokenizer']['sha256'], pilot_sha256=original_pilot_sha,
            proposal_sha256=sha256(PROPOSAL), source_sha256=p['source_sha256'],
            metadata_repair_source_sha256=sha256(Path(__file__)), original_failed_job=reference(RUN/'job.json'),
            original64_draw_and_all_pilot_bytes_exactly_preserved=True,
            training_pool_accepted=False, protected_test_used=False, actual_GPU_seconds=0,
            limitations='Existing TRAIN translations/story material, not new corpus, independent families or human original Japanese. Recorded builder hashes/splits reused; global near/site/author audit incomplete.')
        if sha256(pilot_path) != original_pilot_sha: raise ValueError('Actual pilot unexpectedly changed')
        atomic_json(RUN/'manifest.json', manifest)
        elapsed = time.monotonic()-started
        if elapsed+original['CPU_seconds'] > 60: raise TimeoutError('Combined original+repair CPU60s ceiling exceeded')
        repair.update(status='complete_pending_fixed64_content', CPU_seconds=elapsed,
            cumulative_CPU_seconds=elapsed+original['CPU_seconds'], completed_at=now(),
            manifest_sha256=sha256(RUN/'manifest.json'), documents=len(documents),
            serialized_tokens=manifest['serialized_tokens'], original64_bytes_unchanged=True)
        atomic_json(path, repair)
        print(json.dumps(dict(status=repair['status'], cumulative_CPU_seconds=repair['cumulative_CPU_seconds'],
            documents=len(documents), serialized_tokens=manifest['serialized_tokens'], actual64_bytes_unchanged=True)), flush=True)
    except BaseException as error:
        repair.update(status='failed_preserve_fixed_or_partial', error=repr(error), CPU_seconds=time.monotonic()-started)
        atomic_json(path, repair); raise


if __name__ == '__main__':
    if sys.version_info[:3] != (3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
