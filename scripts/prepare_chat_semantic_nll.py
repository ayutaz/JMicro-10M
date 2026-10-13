"""Freeze common NLL targets; reuse accepted S0/RPC target definitions."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from jmicro.experiment import ROOT, now, read_json, sha256
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json
from prepare_chat_improvement_train import dump_jsonl
from prepare_chat_semantic_train import RUN, DATA, CONTROL, WEIGHTS


def main():
    assert not (DATA / 'nll_fixed.jsonl').exists()
    manifest = read_json(DATA / 'manifest.json')
    assert sha256(DATA / 'train.jsonl') == manifest['train']['sha256']
    old_path = CONTROL / 'nll_fixed.jsonl'
    old_prep = read_json(ROOT / 'reports/phase7/chat-generalization-20261013/nll_preparation.json')
    assert sha256(old_path) == old_prep['sha256']
    old = [json.loads(line) for line in old_path.read_text().splitlines()]
    fixed = []
    for row in old:
        if row['dataset'] == 'D1_TRAIN':
            fixed.append(dict(row, id='semantic-S0-' + row['id'], dataset='S0_TRAIN',
                              historical_target=dict(id=row['id'], source_sha256=sha256(old_path))))
    train = [json.loads(line) for line in (DATA / 'train.jsonl').read_text().splitlines()]
    for category in WEIGHTS:
        rows = [row for row in train if row['category'] == category]
        selected = random.Random('semantic-fixed-NLL-' + category).sample(rows, 16)
        for row in selected:
            fixed.append(dict(id='semantic-S1-' + row['doc_id'], dataset='S1_TRAIN', split='train', category=category,
                              source_doc_id=row['doc_id'], source_target_message_index=row['target_message_indices'][0],
                              messages=row['messages']))
    authored = read_json(DATA / 'dev_authored.json')
    for target in authored['targets']:
        fixed.append(dict(id='semantic-newDEV-' + target['id'], dataset='new_DEV', split='dev',
                          source_doc_id=target['id'], messages=target['messages'] +
                          [dict(role='assistant', content=target['gold_body'])]))
    fixed += [row for row in old if row['dataset'] == 'RPC_DEV']
    assert dict(Counter(row['dataset'] for row in fixed)) == dict(S0_TRAIN=112, S1_TRAIN=112, new_DEV=80, RPC_DEV=2250)
    assert len({row['id'] for row in fixed}) == 2554
    tok = Tokenizer(ROOT / 'artifacts/phase2/4096/tokenizer.model')
    stats = {name: Counter() for name in ('S0_TRAIN', 'S1_TRAIN', 'new_DEV', 'RPC_DEV')}
    for row in fixed:
        window = list(tok.sft_windows(row['messages'], context=1025))[-1]
        selected = [label for label in window['labels'] if label != -100]
        body = row['messages'][-1].get('text', row['messages'][-1].get('content'))
        assert selected[-1] == 7 and 2 <= len(selected) <= 65 and tok.decode(selected[:-1]) == body
        digest = hashlib.sha256(json.dumps(window, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        if row['dataset'] in ('S0_TRAIN', 'RPC_DEV'):
            assert row['window_binding'] == digest
        row.update(teachers=len(selected), body_bytes=len(body.encode('utf-8')), window_binding=digest)
        stats[row['dataset']].update(body_teachers=len(selected) - 1, EOT_teachers=1,
                                    body_bytes=row['body_bytes'], valid_inputs=len(window['input_ids']) - 1,
                                    removed_prior_turns=window['removed_turns'])
    dump_jsonl(DATA / 'nll_fixed.jsonl', fixed)
    report = dict(created_at=now(), status='common_targets_frozen', path=str(DATA / 'nll_fixed.jsonl'),
                  sha256=sha256(DATA / 'nll_fixed.jsonl'), source_sha256=sha256(Path(__file__)),
                  historical_target_source=dict(path=str(old_path), sha256=sha256(old_path)),
                  counts=dict(Counter(row['dataset'] for row in fixed)), statistics={key: dict(value) for key, value in stats.items()},
                  independent_target_ID_order=True, body_and_EOT_separate=True,
                  diagnostic_TRAIN_sample_not_whole_TRAIN=True, new_DEV_training=False,
                  protected_TEST_used=False, GPU_learning_updates=0)
    atomic_json(RUN / 'nll_preparation.json', report)
    print('2554 common NLL targets frozen; old target definitions preserved')


if __name__ == '__main__':
    main()
