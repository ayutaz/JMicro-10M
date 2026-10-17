"""Plan149 TRAIN-only inventory; protected RPC members are never opened.

This measures availability, not semantic acceptance or a frozen training set.
Magpie project-DEV rows are skipped by their leading numeric identity before
JSON payload decoding. Existing parquet reads are metadata-column projection.
"""
import hashlib
import json
from collections import Counter
from pathlib import Path
import re
import sys
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.data import map_dialogue, normalized, japanese_ratio
from jmicro.tokenizer import Tokenizer
from prepare_chat_natural_sources import DATA, ROOT, RUN, now, save, sha


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def target_issue(user, answer):
    if not answer.strip() or '\ufffd' in user + answer or '\x00' in user + answer:
        return 'empty_or_corrupt'
    if japanese_ratio(answer) < .2:
        return 'not_Japanese'
    if len(answer) > 12 and normalized(user) == normalized(answer):
        return 'full_echo'
    if re.search(r'(?:私|僕|俺)(?:は|の).{0,10}(?:歳|住ん|出身|職業|本名)', answer):
        return 'unsupported_speaker_biography'
    return None


def main():
    receipt = RUN / 'availability.json'
    if receipt.exists():
        raise FileExistsError('Preserve completed inventory; inspect it before any new condition')
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    identities = json.loads((DATA / 'RPC_allowed_identities.json').read_text())
    acquisition = json.loads((RUN / 'acquisition.json').read_text())
    assert acquisition['status'] == 'complete'
    for item in acquisition['files'].values():
        assert sha(Path(item['path'])) == item['sha256']
    allowed = set(identities['train'])
    protected = set(identities['preserved_split']['dev'] + identities['preserved_split']['test'] + identities['new_dev'])
    assert not allowed & protected
    # Only hashes/identities/signatures are read, never the mixed text columns.
    import pyarrow.parquet as pq
    from datasketch import MinHash, MinHashLSH
    columns = ['doc_id', 'split', 'dedup_sha256', 'minhash']
    metadata = pq.read_table(ROOT / 'data/phase1/processed/dataset_manifest.parquet', columns=columns).to_pylist()
    held_hashes = set()
    lsh = MinHashLSH(num_perm=128, params=(32, 4))
    held_mh = {}
    for row in metadata:
        if row['split'] in ('dev', 'test'):
            held_hashes.add(row['dedup_sha256'])
            if row['minhash']:
                mh = MinHash(num_perm=128, seed=42, hashvalues=row['minhash'])
                lsh.insert(row['doc_id'], mh)
                held_mh[row['doc_id']] = mh
    report = dict(started_at=now(), role='availability_only_not_training_acceptance',
                  teacher_lengths_including_EOT=[32, 64], default_generation_cap=32,
                  protected_RPC_members_opened=0, protected_TEST_payloads_opened=0,
                  metadata_columns_read=columns, protected_metadata_hashes=len(held_hashes),
                  limitations=['LSH recall is probabilistic; conservative signature similarity is not exact Jaccard',
                               'No full semantic audit yet; every answer is preserved whole, never cut to length'])
    counts = Counter()
    outputs = {s: (DATA / f'{s}_eligible_inventory.jsonl').open('x', encoding='utf-8') for s in ('RPC', 'magpie')}
    unique = {s: {32: set(), 64: set()} for s in outputs}
    seen_pairs = set()
    def record(source, uid, messages, original_train=False):
        roles = [m['role'] for m in messages]
        if not messages or roles != ['user' if i % 2 == 0 else 'assistant' for i in range(len(roles))]:
            counts[source + ':bad_roles'] += 1
            return
        # Full dialogue fingerprints prevent source-family contamination.
        whole = '\n'.join(m['text'] for m in messages)
        norm = normalized(whole)
        if digest(norm) in held_hashes:
            counts[source + ':protected_exact'] += 1
            return
        lengths = [len(tok.encode(m['text'])) + 2 for m in messages]
        if not any(3 <= n <= 65 and messages[i]['role'] == 'assistant' for i, n in enumerate(lengths)):
            counts[source + ':no_short_target_documents'] += 1
            return
        mh = MinHash(num_perm=128, seed=42)
        mh.update_batch(sorted({norm[i:i+5].encode() for i in range(max(1, len(norm)-4))}))
        if any(mh.jaccard(held_mh[k]) >= .75 for k in lsh.query(mh)):
            counts[source + ':protected_near'] += 1
            return
        prefix = 1
        targets = []
        for i, m in enumerate(messages):
            prefix += lengths[i]
            if m['role'] != 'assistant':
                continue
            n = lengths[i] - 1
            counts[source + ':all_assistant_targets'] += 1
            counts[source + ':target_length:' + ('2-32' if 2 <= n <= 32 else '33-64' if 33 <= n <= 64 else '65+' if n > 64 else 'under2')] += 1
            if not 2 <= n <= 64:
                continue
            issue = target_issue(messages[i-1]['text'], m['text'])
            if issue:
                counts[source + ':reject:' + issue] += 1
                continue
            if prefix > 1025:
                counts[source + ':prefix_over_context'] += 1
                continue
            pair = digest(normalized(messages[i-1]['text']) + '\n' + normalized(m['text']))
            if pair in seen_pairs:
                counts[source + ':duplicate_pair'] += 1
                continue
            seen_pairs.add(pair)
            targets.append(dict(index=i, teachers=n, pair_sha256=pair))
            for cap in (32, 64):
                if n <= cap:
                    counts[f'{source}:eligible{cap}:targets'] += 1
                    counts[f'{source}:eligible{cap}:teachers'] += n
                    unique[source][cap].add(digest(normalized(m['text'])))
                    if original_train:
                        counts[f'C0:eligible{cap}:targets'] += 1
                        counts[f'C0:eligible{cap}:teachers'] += n
        if targets:
            last = targets[-1]['index']
            outputs[source].write(json.dumps(dict(doc_id=uid, source=source, split='train',
                original_RPC_train=original_train, messages=messages[:last+1], targets=targets), ensure_ascii=False) + '\n')
            counts[source + ':eligible_documents'] += 1
    try:
        old_train = set(identities['preserved_split']['train'])
        with zipfile.ZipFile(DATA / 'raw/real_persona_chat.zip') as archive:
            for step, member in enumerate(sorted(allowed)):
                assert member not in protected and member in allowed
                messages, _ = map_dialogue(json.loads(archive.read(member)))
                record('RPC', 'real_persona_chat:' + member, [dict(role=m['role'], text=m['text']) for m in messages], member in old_train)
                counts['RPC:TRAIN_members_opened'] += 1
                if (step+1) % 2000 == 0:
                    print(f'RPC allowed TRAIN dialogues: {step+1}', flush=True)
        # Upstream TRAIN-only public artifact. Reserve project-DEV IDs by a
        # prefix-only parse; no project TEST split is created.
        dev_ids = []
        raw = DATA / 'raw/magpie/magpie-sft-v1.0.jsonl'
        with raw.open() as stream:
            for line in stream:
                match = re.match(r'^\{"id":\s*(\d+),', line)
                if not match:
                    raise ValueError('Unexpected source identity prefix; refuse payload parsing')
                uid = 'magpie:' + match[1]
                if int(digest('natural-dev42:' + uid)[:8], 16) % 10 == 0:
                    dev_ids.append(uid)
                    continue
                row = json.loads(line)
                assert str(row['id']) == match[1]
                messages = [dict(role=m['role'], text=m['content']) for m in row['conversations']]
                record('magpie', uid, messages)
                counts['magpie:TRAIN_rows_parsed'] += 1
        save(DATA / 'magpie_reserved_DEV_identities.json', dict(ids=dev_ids, body_parsed=False, new_TEST_created=False))
    finally:
        for stream in outputs.values():
            stream.close()
    report.update(completed_at=now(), counts=dict(counts),
        distinct_answer_texts={s: {str(k): len(v) for k, v in caps.items()} for s, caps in unique.items()},
        files={s: dict(path=str(DATA / f'{s}_eligible_inventory.jsonl'), sha256=sha(DATA / f'{s}_eligible_inventory.jsonl')) for s in outputs},
        magpie_project_DEV_ids=len(dev_ids), status='measured_unreviewed')
    save(receipt, report)
    print(json.dumps({k: v for k, v in report.items() if k not in ('files',)}, ensure_ascii=False, indent=2), flush=True)


if __name__ == '__main__':
    assert sys.version_info[:3] == (3, 12, 7)
    main()
