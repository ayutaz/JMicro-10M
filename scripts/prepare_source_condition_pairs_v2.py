"""One bounded V2 source selector after recorded lexical failures; train only."""
import hashlib
import json
from pathlib import Path
import re
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.tokenizer import Tokenizer
from cached_three_source_index import CachedThreeSourceIndex

OUT = ROOT / 'reports/phase6/source-condition-pairs-v2-20261006'
SEED = 2026100652
TARGET = 512
MAX_ATTEMPTS = 2000000
CPU_LIMIT = 60
MARKER = re.compile(r'なければ|れば|(?<!なぜ)ならば|(?<!なぜ)なら(?!では)|場合には|場合は|ときには|ときは')
CONTRAST_START = re.compile(r'^[\s「『]*(?:一方|これに対して|それに対して|逆に|しかし|その反対に|対照的に)[、，\s]')


def extract_pair(text):
    clauses = []
    for sentence in re.finditer(r'[^。！？\n]+[。！？]', text):
        original = sentence.group()
        matches = list(MARKER.finditer(original))
        # Leave multi-condition sentences untouched until a finite-clause parser
        # is justified. Do not invent sentence punctuation or rewrite facts.
        if len(matches) != 1:
            continue
        marker = matches[0]
        before = original[:marker.start()]
        tail = original[marker.end():]
        if (before.endswith('もあ')
                or re.search(r'(?:観点|視点|立場).{0,10}見$', before)
                or re.match(r'[^、。]{0,16}ほど', tail)):
            continue
        cut = sentence.start() + marker.end()
        if not 8 <= cut <= 1400 or not 8 <= len(tail.strip()) <= 160:
            continue
        branch = dict(prefix=text[:cut], outcome=text[cut:sentence.end()],
                      cut=cut, end=sentence.end(), condition_sentence=original,
                      sentence_start=sentence.start())
        if CONTRAST_START.match(original) and clauses:
            # The nearest preceding eligible condition replaces V1's earliest
            # generic introduction. A textual contrast is still not a hard negative.
            first = clauses[-1]
            if (sentence.start() - first['end'] <= 160
                    and first['outcome'] != branch['outcome']):
                return dict(branches=[first, branch],
                            choices=[first['outcome'], branch['outcome']],
                            negative_validity='Unreviewed; source-original distinct outcomes do not establish incompatible alternatives.')
        clauses.append(branch)
    return None


def main():
    started = time.monotonic()
    if OUT.exists():
        raise ValueError('Fixed V2 run exists; do not resample or overwrite')
    inspection = ROOT / 'reports/phase6/conditional-content-pilot-20261006'
    prior = ROOT / 'reports/phase6/source-condition-pairs-20261006'
    review = read_json(inspection / 'content-review.json')
    prior_review = read_json(prior / 'content-review.json')
    if (not review['all96_content_review_complete']
            or review['notes_sha256'] != sha256(inspection / 'content-notes.json')
            or not prior_review['all48_read'] or prior_review['training_pool_accepted']
            or prior_review['observations_sha256'] != sha256(prior / 'observations.tsv')
            or prior_review['source_pairs_sha256'] != sha256(prior / 'source-pairs.json')):
        raise ValueError('Recorded96+48 inspection and rejected V1 required')
    config = read_json(ROOT / 'configs/phase6/story_weight_comparison.json')
    cache = Path(config['accepted_compact_index']['path'])
    if not cache.exists() or sha256(cache) != config['accepted_compact_index']['sha256']:
        raise ValueError('Compact cache absent; refuse original-index rescan')
    view = TrainView(config['pool']['pool'], config['pool']['manifest_sha256'])
    index = CachedThreeSourceIndex(view)
    if not index.cache_reused:
        raise ValueError('Original corpus may not be reparsed')
    base = read_json(Path(config['original_config']['path']))
    if sha256(ROOT / base['tokenizer']) != base['tokenizer_sha256']:
        raise ValueError('Fixed Tokenizer differs')
    tokenizer = Tokenizer(ROOT / base['tokenizer'])
    inspected = read_json(inspection / 'source-sample.json')['rows']
    previous = read_json(prior / 'source-pairs.json')['rows']
    excluded = {r['document_index'] for r in inspected + previous}
    excluded_bodies = {r['decoded_body_sha256'] for r in inspected + previous}
    rng = np.random.default_rng(SEED)
    seen = set()
    bodies = set()
    rows = []
    decoded_documents = decoded_tokens = 0
    stop_reason = 'attempt_limit'
    for attempts in range(1, MAX_ATTEMPTS + 1):
        if time.monotonic() - started >= CPU_LIMIT:
            stop_reason = 'CPU_limit'
            break
        document = int(rng.integers(len(index.lengths)))
        if document in excluded or document in seen or int(index.sources[document]) != 2:
            continue
        seen.add(document)
        length = int(index.lengths[document])
        if not 64 <= length <= 512:
            continue
        offset = int(index.offsets[document])
        ids = view.tokens[offset:offset + length + 2].tolist()
        if ids[0] != 2 or ids[-1] != 3 or any(i < 8 for i in ids[1:-1]):
            raise ValueError('Whole train body boundaries differ')
        body = tokenizer.decode_bytes(ids[1:-1])
        text = body.decode('utf-8')
        decoded_documents += 1
        decoded_tokens += length
        pair = extract_pair(text)
        if pair is None:
            continue
        digest = hashlib.sha256(body).hexdigest()
        if digest in excluded_bodies or digest in bodies:
            continue
        bodies.add(digest)
        rows.append(dict(id=f'condition-v2-{len(rows):04d}', source='textbook', split='train',
                         document_index=document, train_offset=offset, original_body_tokens=length,
                         decoded_body_sha256=digest, original_text=text, **pair))
        if len(rows) == TARGET:
            stop_reason = 'target_reached'
            break
    OUT.mkdir(parents=True)
    write_json(OUT / 'source-pairs.json', dict(rows=rows))
    write_json(OUT / 'content-pilot.json', dict(rows=rows[:64]))
    result = dict(status='bounded_V2_supply_unreviewed', created_at=now(), seed=SEED,
        target_pairs=TARGET, pairs=len(rows), supply_target_met=len(rows) == TARGET,
        content_pilot_pairs=min(64, len(rows)), CPU_seconds=time.monotonic() - started,
        CPU_ceiling_seconds=CPU_LIMIT, attempt_ceiling=MAX_ATTEMPTS, attempts=attempts,
        stop_reason=stop_reason, decoded_documents=decoded_documents,
        inspected_existing_body_tokens=decoded_tokens, excluded_document_indices=len(excluded),
        excluded_reviewed_body_hashes=len(excluded_bodies), unique_selected_body_hashes=len(bodies),
        pool_manifest_sha256=config['pool']['manifest_sha256'], accepted_index=config['accepted_compact_index'],
        tokenizer_sha256=base['tokenizer_sha256'], script_sha256=sha256(Path(__file__)),
        prior_review_sha256=sha256(prior / 'content-review.json'),
        inspection_review_sha256=sha256(inspection / 'content-review.json'),
        source_pairs_sha256=sha256(OUT / 'source-pairs.json'),
        content_pilot_sha256=sha256(OUT / 'content-pilot.json'),
        original_index_rescan=False, newly_prepared_original_tokens=0,
        actual_GPU_seconds=0, scientific_teacher_tokens=0, training_pool_accepted=False,
        protected_test_used=False, Base_adopted=False, source='textbook', split='train',
        completion_condition='Read fixed first64 full original texts and both branches; weak<=10 unchanged. No training until adequate supply and a defined comparison. No hard-negative labels inferred.',
        limitations='Selected normalized train documents, local exact body exclusion only; original source-family independence, global deduplication, factual certification and corpus representativeness are unmeasured. Multi-condition sentences remain excluded. Base only; Chat/quantization deferred.')
    write_json(OUT / 'result.json', result)
    print(json.dumps({k: result[k] for k in ('pairs', 'attempts', 'CPU_seconds', 'stop_reason', 'supply_target_met')}), flush=True)


if __name__ == '__main__':
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError('Pinned uv Python3.12.7 required')
    main()
