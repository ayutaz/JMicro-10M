"""Bounded unchanged-train source supply; proposed paired targets remain unreviewed."""
import hashlib
import json
from pathlib import Path
import re
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, sha256, write_json, now
from jmicro.tokenizer import Tokenizer
from cached_three_source_index import CachedThreeSourceIndex

OUT = ROOT / 'reports/phase6/source-condition-pairs-20261006'
SEED = 2026100651
MARKER = re.compile(r'なければ|れば|ならば|なら|場合は|場合には|ときは|ときには')
CONTRAST = re.compile(r'一方|逆に|対して|しかし|それに対|異な|なければ|ない場合')


def extract_pair(text):
    clauses = []
    for sentence in re.finditer(r'[^。！？\n]+[。！？]', text):
        matches = list(MARKER.finditer(sentence.group()))
        # Multiple conditions in the same sentence cannot yield two independent
        # complete original outcomes with this deliberately simple parser.
        if len(matches) != 1: continue
        cut = sentence.start() + matches[0].end()
        prefix, outcome = text[:cut], text[cut:sentence.end()]
        if not 8 <= len(prefix) <= 1400 or not 8 <= len(outcome.strip()) <= 160:
            continue
        clauses.append(dict(prefix=prefix, outcome=outcome, cut=cut, end=sentence.end(),
                            condition_sentence=sentence.group(), sentence_start=sentence.start()))
    for i, first in enumerate(clauses):
        for second in clauses[i + 1:]:
            if first['outcome'] == second['outcome'] or not CONTRAST.search(second['condition_sentence']):
                continue
            return dict(branches=[first, second], choices=[first['outcome'], second['outcome']],
                        negative_validity='Unreviewed: distinct original continuations are not automatically incompatible; all64 pilot pairs require individual review before learning.')
    return None


def main():
    started = time.monotonic()
    if OUT.exists(): raise ValueError('Fixed supply run exists; inspect, never resample')
    inspection = ROOT / 'reports/phase6/conditional-content-pilot-20261006'
    review = read_json(inspection / 'content-review.json')
    if not review['all96_content_review_complete'] or review['notes_sha256'] != sha256(inspection / 'content-notes.json'):
        raise ValueError('Completed96 raw-bound content inspection required')
    c = read_json(ROOT / 'configs/phase6/story_weight_comparison.json')
    cache = Path(c['accepted_compact_index']['path'])
    if not cache.exists() or sha256(cache) != c['accepted_compact_index']['sha256']:
        raise ValueError('Compact index absent; refuse original corpus rescan')
    view = TrainView(c['pool']['pool'], c['pool']['manifest_sha256'])
    index = CachedThreeSourceIndex(view)
    if not index.cache_reused: raise ValueError('Original index must not be reparsed')
    base = read_json(Path(c['original_config']['path']))
    tok = Tokenizer(ROOT / base['tokenizer'])
    if sha256(ROOT / base['tokenizer']) != base['tokenizer_sha256']: raise ValueError('Tokenizer differs')
    excluded = {r['document_index'] for r in read_json(inspection / 'source-sample.json')['rows']}
    rng = np.random.default_rng(SEED); seen = set(); rows = []; decoded_documents = 0; decoded_tokens = 0
    attempts = 0
    for attempts in range(1, 60001):
        if time.monotonic() - started > 60: raise TimeoutError('CPU60s source supply exhausted')
        document = int(rng.integers(len(index.lengths)))
        if document in excluded or document in seen or int(index.sources[document]) != 2:
            continue
        seen.add(document); length = int(index.lengths[document])
        if not 64 <= length <= 512: continue
        offset = int(index.offsets[document]); ids = view.tokens[offset:offset + length + 2].tolist()
        if ids[0] != 2 or ids[-1] != 3 or any(i < 8 for i in ids[1:-1]): raise ValueError('Whole train body differs')
        body = tok.decode_bytes(ids[1:-1]); text = body.decode('utf-8')
        decoded_documents += 1; decoded_tokens += length
        pair = extract_pair(text)
        if pair is None: continue
        rows.append(dict(id=f'condition-{len(rows):04d}', source='textbook', split='train',
            document_index=document, train_offset=offset, original_body_tokens=length,
            decoded_body_sha256=hashlib.sha256(body).hexdigest(), original_text=text, **pair))
        if len(rows) == 512: break
    if time.monotonic() - started > 60: raise TimeoutError('CPU60s source supply exhausted')
    OUT.mkdir(parents=True)
    write_json(OUT / 'source-pairs.json', dict(rows=rows))
    # Fixed first64, not a model-dependent or quality-selected reroll.
    write_json(OUT / 'content-pilot.json', dict(rows=rows[:64]))
    write_json(OUT / 'result.json', dict(status='bounded_source_condition_pair_supply_unreviewed',
        seed=SEED, created_at=now(), CPU_seconds=time.monotonic() - started, CPU_ceiling_seconds=60,
        attempt_ceiling=60000, attempts=attempts, source='textbook', length_range=[64,512],
        pairs=len(rows), distinct_train_documents=len(rows), target_pairs=512,
        supply_target_met=len(rows) == 512, content_pilot_pairs=min(len(rows), 64),
        decoded_documents=decoded_documents, inspected_existing_body_tokens=decoded_tokens,
        pool_manifest_sha256=c['pool']['manifest_sha256'], accepted_index=c['accepted_compact_index'],
        source_pairs_sha256=sha256(OUT / 'source-pairs.json'), content_pilot_sha256=sha256(OUT / 'content-pilot.json'),
        inspection_review_sha256=sha256(inspection / 'content-review.json'), script_sha256=sha256(Path(__file__)),
        original_index_rescan=False, newly_prepared_original_tokens=0, actual_GPU_seconds=0,
        scientific_teacher_tokens=0, training_pool_accepted=False, protected_test_used=False,
        Base_adopted=False, requested_five_steps_complete=False,
        extraction='Original contiguous prefixes and sentence-ending continuations; no invented/reversed facts. Two distinct outcomes and contrast marker in later sentence, not an automatic proof of negative correctness.',
        completion_condition='Record exact bounded supply then personally read fixed first64 entire original texts and both branches. Keep source/topic/grammar/context and possible alternative-validity failures. Do not launch learning unless a defined comparison and unchanged content/quality conditions are satisfied.',
        limitations='Selected normalized train documents; source-family diversity/global dedup/representative corpus rates/factual certification are unmeasured. Inspection96 excluded, dev/test never read or used. Distinct document indices are not necessarily distinct original source families. No new GPU/learning.'))
    print(json.dumps(dict(pairs=len(rows), decoded_documents=decoded_documents, attempts=attempts,
                         CPU_seconds=time.monotonic() - started, GPU_seconds=0, content_review_pending=True)), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7): raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
