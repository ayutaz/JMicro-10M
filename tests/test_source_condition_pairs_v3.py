import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from prepare_source_condition_pairs_v3 import extract_pair


def test_recorded_embedded_question_frequency_and_nominarazu_rejected():
    for text in (
        '何を頑張ればよいのか分からず、不安でした。逆に、目標が決まれば明るい気持ちになります。',
        '多くの場合は燃料を燃やして電気を作ります。一方、発電できなければ別の場所から電気を買います。',
        '歴史を振り返れば終末論が見つかります。一方、影響は個人のみならず、社会にも及ぶものです。',
        '同時に試験することができれば費用が減ります。しかし、同時に扱う場合には装置の制約があります。',
    ):
        assert extract_pair(text) is None


def test_quantity_opposition_keeps_original_contiguous_spans():
    text = '流れ込む水の量が多ければ水位は上がります。逆に、出ていく水の量が多ければ水位は下がります。'
    pair = extract_pair(text)
    assert pair is not None
    assert pair['choices'] == ['水位は上がります。', '水位は下がります。']
    for branch in pair['branches']:
        assert branch['prefix'] == text[:branch['cut']]
        assert branch['outcome'] == text[branch['cut']:branch['end']]
