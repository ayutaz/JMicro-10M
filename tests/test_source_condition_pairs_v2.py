import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from prepare_source_condition_pairs_v2 import extract_pair


def test_lexical_causal_progressive_and_recipient_false_conditions_rejected():
    for text in (
        '楽しさならではのときめきを忘れます。一方、急げば大事なものを失います。',
        'なぜなら弱い家は壊れやすいからです。一方、家が頑丈なら被害は小さくなります。',
        '巻数が増えれば増えるほど磁場が強くなります。一方、向きが逆なら磁場も反転します。',
        '楽しげな曲もあればゆったりした曲もあります。一方、急げば踊り方も変わります。',
        '心理学的観点から見れば独特の知見が得られます。一方、記録を辿れば別の歴史が見えます。',
        '処分に不服があれば不服を申し立てられます。申立ての場合は都道府県に対して請求します。',
    ):
        assert extract_pair(text) is None


def test_nearest_condition_and_exact_original_spans_preserved():
    text = ('曲を選ぶなら多様な踊り方があります。速い曲なら軽快な踊りが楽しめます。'
            '一方、遅い曲なら落ち着いた踊りが楽しめます。')
    pair = extract_pair(text)
    assert pair is not None
    assert pair['choices'] == ['軽快な踊りが楽しめます。', '落ち着いた踊りが楽しめます。']
    for branch in pair['branches']:
        assert branch['prefix'] == text[:branch['cut']]
        assert branch['outcome'] == text[branch['cut']:branch['end']]


def test_multicondition_sentence_is_not_rewritten():
    text = '先を尖らせれば細い線が描けますし、丸くすれば柔らかい線が描けます。'
    assert extract_pair(text) is None
