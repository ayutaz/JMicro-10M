"""Nested512->2048 train-only conditional source; keep the accepted V3 selector."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import numpy as np
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, sha256, now
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from cached_three_source_index import CachedThreeSourceIndex
from phase6_performance import alive, identity
from prepare_source_condition_pairs_v3 import extract_pair

OUT = ROOT / 'reports/phase6/condition-diversity-source-20261006'
SMALL = ROOT / 'reports/phase6/source-condition-pairs-v3-20261006'
SEED = 2026100654
TARGET = 2048
CPU_LIMIT = 240
DRAW_LIMIT = 32000000


def nested(rows, small):
    if rows[:len(small)] != small or len({r['document_index'] for r in rows}) != len(rows) or len({r['decoded_body_sha256'] for r in rows}) != len(rows):
        raise ValueError('Exact nested small source and local body/document uniqueness required')


def prepare():
    if OUT.exists(): raise ValueError('Fixed diversity preparation exists; inspect instead of resampling')
    small = read_json(SMALL / 'source-pairs.json')['rows']; reviewed = read_json(SMALL / 'content-review.json')
    diagnostic = ROOT / 'reports/phase6/condition-trainfit-diagnostic-20261006'
    job = read_json(diagnostic / 'job.json'); fitted = read_json(diagnostic / 'result.json')
    if (len(small) != 512 or not reviewed['training_pool_accepted']
            or reviewed['source_pairs_sha256'] != sha256(SMALL / 'source-pairs.json')
            or job['status'] != 'complete' or alive(job) or fitted['evaluated_documents'] != 1536
            or fitted['optimizer_updates'] != 0 or fitted['protected_test_used']):
        raise ValueError('Accepted512 source and completed read-only fit diagnostic required')
    config = read_json(ROOT / 'configs/phase6/condition_positive_comparison.json')
    cache = Path(config['accepted_compact_index']['path'])
    if not cache.exists() or sha256(cache) != config['accepted_compact_index']['sha256']:
        raise ValueError('Existing compact cache required; no full-index rescan')
    OUT.mkdir(parents=True); started = time.monotonic()
    record = dict(status='running', **identity(), started_at=now(), CPU_budget_seconds=CPU_LIMIT,
        attempts=0, documents=512, target_documents=TARGET, new_GPU_seconds=0,
        restart_command='No automatic retry; bounded preparation saves its terminal selected rows.')
    atomic_json(OUT / 'job.json', record)
    rows = list(small); excluded = {r['document_index'] for r in small}; hashes = {r['decoded_body_sha256'] for r in small}
    seen = set(); decoded = tokens = attempts = 0; reason = 'draw_limit'
    try:
        pool = config['pool']; view = TrainView(pool['pool'], pool['manifest_sha256']); index = CachedThreeSourceIndex(view)
        if not index.cache_reused: raise ValueError('Corpus must not be reparsed')
        base = read_json(Path(config['original_config']['path']))
        if sha256(ROOT / base['tokenizer']) != base['tokenizer_sha256']: raise ValueError('Tokenizer changed')
        tokenizer = Tokenizer(ROOT / base['tokenizer']); rng = np.random.default_rng(SEED)
        # Exclude every already reviewed prior pilot, including the rejected sources.
        for folder, name in (('conditional-content-pilot-20261006','source-sample.json'),
                             ('source-condition-pairs-20261006','source-pairs.json'),
                             ('source-condition-pairs-v2-20261006','content-pilot.json')):
            for r in read_json(ROOT / 'reports/phase6' / folder / name)['rows']:
                excluded.add(r['document_index']); hashes.add(r['decoded_body_sha256'])
        while attempts < DRAW_LIMIT and len(rows) < TARGET:
            if time.monotonic()-started >= CPU_LIMIT: reason='CPU_limit'; break
            draws = rng.integers(len(index.lengths), size=min(100000, DRAW_LIMIT-attempts))
            for value in draws:
                attempts += 1; doc = int(value)
                if attempts % 50000 == 0 and time.monotonic()-started >= CPU_LIMIT: reason='CPU_limit'; break
                if doc in excluded or doc in seen or int(index.sources[doc]) != 2: continue
                seen.add(doc); length=int(index.lengths[doc])
                if not 64 <= length <= 512: continue
                offset=int(index.offsets[doc]); ids=view.tokens[offset:offset+length+2].tolist()
                if ids[0]!=2 or ids[-1]!=3 or any(i<8 for i in ids[1:-1]): raise ValueError('Whole original body differs')
                body=tokenizer.decode_bytes(ids[1:-1]); text=body.decode('utf-8'); decoded+=1; tokens+=length
                pair=extract_pair(text)
                if pair is None: continue
                digest=hashlib.sha256(body).hexdigest()
                if digest in hashes: continue
                hashes.add(digest); excluded.add(doc)
                rows.append(dict(id=f'condition-expanded-{len(rows):04d}',source='textbook',split='train',
                    document_index=doc,train_offset=offset,original_body_tokens=length,
                    decoded_body_sha256=digest,original_text=text,**pair))
                if len(rows)==TARGET: reason='target_reached'; break
            record.update(attempts=attempts, documents=len(rows), CPU_seconds=time.monotonic()-started, heartbeat_at=now())
            atomic_json(OUT/'job.json',record)
            print(json.dumps(dict(documents=len(rows),attempts=attempts,CPU_seconds=record['CPU_seconds'])),flush=True)
            if reason in ('CPU_limit','target_reached'): break
        nested(rows, small)
        atomic_json(OUT/'source-pairs.json',dict(rows=rows))
        atomic_json(OUT/'content-pilot.json',dict(rows=rows[512:576]))
        result=dict(status='bounded_nested_condition_supply_unreviewed',seed=SEED,documents=len(rows),
            original_small_documents=512,target_documents=TARGET,supply_target_met=len(rows)==TARGET,
            small_source_sha256=sha256(SMALL/'source-pairs.json'),old512_retained_exactly=True,
            source_pairs_sha256=sha256(OUT/'source-pairs.json'),content_pilot_sha256=sha256(OUT/'content-pilot.json'),
            content_pilot_documents=min(64,len(rows)-512),content_pilot_policy='First64 newly added rows; unchanged weak<=10 gate before any training',
            selector_sha256=sha256(ROOT/'scripts/prepare_source_condition_pairs_v3.py'),selector_changed=False,
            script_sha256=sha256(Path(__file__)),diagnostic_sha256=sha256(diagnostic/'result.json'),
            attempts=attempts,attempt_limit=DRAW_LIMIT,CPU_seconds=time.monotonic()-started,CPU_limit_seconds=CPU_LIMIT,
            stop_reason=reason,decoded_documents=decoded,inspected_existing_body_tokens=tokens,
            selected_original_body_tokens=sum(r['original_body_tokens'] for r in rows),
            pool_manifest_sha256=pool['manifest_sha256'],accepted_index=config['accepted_compact_index'],
            newly_prepared_original_tokens=0,actual_GPU_seconds=0,scientific_teacher_tokens=0,
            protected_test_used=False,Base_adopted=False,Chat_started=False,quantization_started=False,
            training_pool_accepted=False,created_at=now(),
            next_action='Read all fixed64 new full texts/branches, unchanged gate; then original IDs/masks preparation and same-parent/same25M/weight1 comparison vs saved512 control. No weight sweep or automatic long extension.',
            limitations='Local exact body/document uniqueness; no global/family/factual certification. Whole original train reused from existing2B, not new original corpus tokens. V3 selector unchanged; source cardinality comparison, not V4 content reroll. Only64 new examples will be individually read.')
        atomic_json(OUT/'result.json',result); record.update(status='complete',completed_at=now())
    except BaseException as error:
        record.update(status='failed',error=repr(error)); raise
    finally:
        record.update(CPU_seconds=time.monotonic()-started,documents=len(rows),attempts=attempts)
        atomic_json(OUT/'job.json',record)


if __name__=='__main__':
    if sys.version_info[:3]!=(3,12,7): raise RuntimeError('Pinned uv Python3.12.7 required')
    prepare()
