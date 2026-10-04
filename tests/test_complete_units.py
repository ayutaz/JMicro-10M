import json
from pathlib import Path
import sys
import signal
from types import SimpleNamespace

import numpy as np
import pytest

from jmicro.complete_units import complete_sentences, complete_units, balanced, unit_hash
from jmicro.experiment import ROOT, write_json, sha256, read_json
from jmicro.tokenizer import Tokenizer

sys.path.insert(0, str(ROOT / 'scripts'))
from prepare_complete_units import prepare_pool
from run_eos_complete_100m import adoption_checks, screen_safe


class CharacterTokenizer:
    def encode(self, text):
        return [ord(c) + 8 for c in text]


def test_complete_units_preserve_source_spans_and_do_not_cut_long_sentences():
    text = '今日は晴れです。明日は公園で友達と一緒に散歩する予定です。' + '長' * 70 + '。途中で切れた文章'
    units = list(complete_units(text, CharacterTokenizer(), minimum=20, maximum=64))
    assert units and all(u['text'] == text[u['char_start']:u['char_end']] for u in units)
    assert all('長' not in u['text'] and '途中' not in u['text'] for u in units)


def test_quoted_punctuation_does_not_split_inside_a_balanced_sentence():
    text = '彼は「おはよう。今日は晴れですね。」と話しました。次の文です。'
    sentences = list(complete_sentences(text))
    assert [s[2] for s in sentences] == ['彼は「おはよう。今日は晴れですね。」と話しました。', '次の文です。']


@pytest.mark.parametrize('text', ['本文を紹介します…', '本文……。', '詳しくは続きを読む。', '「引用が途切れました。', '閉じ括弧がおかしい）。', 'https://example.com/を見てください。', '1. 項目の説明です。', 'これは新しいアプリ。', '紹介の見出し\n写真から立体を作成します。', '使えるフリーの営業日報テンプレートまとめ\n\n一覧です。', '| 右は京都の市電の系統図です。'])
def test_fragments_and_obvious_bad_boundaries_are_excluded(text):
    assert not list(complete_sentences(text))


def test_invalid_skipped_sentence_does_not_get_joined_into_a_short_unit():
    text = '短文です。詳しくは続きを読む。今日も家族で仲良く暮らしています。'
    units = list(complete_units(text, CharacterTokenizer(), minimum=15, maximum=64))
    assert [u['text'] for u in units] == ['今日も家族で仲良く暮らしています。']
    assert balanced('「正しい（括弧）です。」') and not balanced('「不正な）括弧です。」')


def test_pool_keeps_train_provenance_dedups_and_excludes_protected_dev_text(tmp_path):
    tok_path = ROOT / 'artifacts/phase2/4096/tokenizer.model'
    tok = Tokenizer(tok_path)
    texts = [f'第{i}回の散歩では近所の公園を歩いて季節の花を見ました。家に帰ってから家族と楽しく話しました。' for i in range(12)]
    ids = []
    for text in [*texts, texts[0]]:
        ids.extend([2, *tok.encode(text), 3])
    web = tmp_path / 'web'
    web.mkdir()
    np.asarray(ids, dtype='<u2').tofile(web / 'train.bin')
    write_json(web / 'token_bytes.json', [0 if i < 8 else len(tok.decode_bytes([i])) for i in range(tok.vocab_size)])
    write_json(web / 'manifest.json', {'vocab_size': tok.vocab_size, 'token_bytes_sha256': sha256(web / 'token_bytes.json'),
                                     'splits': {'train': {'tokens': len(ids)}}})
    protected_unit = next(complete_units(texts[0], tok))
    aux = {'cases': [{'text_sha256': protected_unit['text_sha256']}]}
    run = tmp_path / 'run'
    run.mkdir()
    write_json(run / 'auxiliary-dev.json', aux)
    plan = {'short_pool': str(tmp_path / 'pool'), 'web_shards': str(web), 'web_manifest_sha256': sha256(web / 'manifest.json'),
            'tokenizer': str(tok_path), 'tokenizer_sha256': sha256(tok_path), 'output': str(run),
            'short_selection': {'body_tokens_min': 32, 'body_tokens_max': 64}, 'prepare_workers': 2,
            'short_pool_minimum_tokens': 180, 'prepare_budget_seconds': 30}
    original_handler = signal.getsignal(signal.SIGTERM)
    signal.signal(signal.SIGTERM, lambda *_: None)
    try:
        ready = prepare_pool(plan, tok, aux, lambda *a, **kw: None, lambda: None)
    finally:
        signal.signal(signal.SIGTERM, original_handler)
    pool = np.fromfile(Path(plan['short_pool']) / 'train.bin', dtype='<u2')
    records = [json.loads(line) for line in (Path(plan['short_pool']) / 'train.index.jsonl').read_text().splitlines()]
    assert ready['protected_units_excluded'] > 0 and ready['tokens'] >= 180
    seen = set()
    for row in records:
        body = pool[row['offset'] + 1:row['offset'] + row['body_tokens'] + 1].tolist()
        text = tok.decode_bytes(body).decode('utf-8')
        assert 32 <= len(body) <= 64 and row['split'] == 'train'
        assert row['text_sha256'] == unit_hash(text) and row['text_sha256'] not in seen
        assert row['text_sha256'] != protected_unit['text_sha256']
        source = tok.decode_bytes(ids[row['source_start'] + 1:row['source_end']]).decode('utf-8')
        assert text == source[row['char_start']:row['char_end']]
        assert pool[row['offset']] == 2 and pool[row['offset'] + row['body_tokens'] + 1] == 3
        seen.add(row['text_sha256'])
    assert prepare_pool(plan, tok, aux, lambda *a, **kw: None, lambda: None) == ready


def test_repetition_gain_and_auxiliary_gain_cannot_replace_fixed_eos_adoption_gate():
    control = {'greedy_rates': {'eos': 0, 'repetition': 62, 'empty': 0, 'role_leak': 0, 'unicode_failure': 0}, 'body': {'bpb': 1.0}}
    candidate = {'greedy_rates': {'eos': 0, 'repetition': 54, 'empty': 0, 'role_leak': 0, 'unicode_failure': 0},
                 'body': {'bpb': 1.0006}, 'generation': {'outputs': []}, 'auxiliary': {'eos': 80}}
    checks = adoption_checks(control, candidate)
    assert not checks['EOS_at_least8_more'] and not all(checks.values())
    candidate['greedy_rates']['eos'] = 8
    candidate['generation']['outputs'] = [{'stop_reason': 'stop_id', 'text': '。'}]
    assert not adoption_checks(control, candidate)['no_punctuation_only_stops']


def test_web_screen_regression_prevents_full_evaluation():
    baseline = {'evaluation': {'new_generation_rates': {'greedy-suppressed1-seed42': {'repetition': 60, 'empty': 0, 'role_leak': 0, 'unicode_failure': 0}}}}
    candidate = {'greedy_rates': {'repetition': 67, 'empty': 0, 'role_leak': 0, 'unicode_failure': 0}}
    assert screen_safe(candidate, baseline)
    candidate['greedy_rates']['repetition'] = 68
    assert not screen_safe(candidate, baseline)
