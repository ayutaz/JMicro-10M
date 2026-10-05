from jmicro.realistic_curriculum import select_unit,literal_units


def test_quotes_condition_negation_and_numbers_remain_literal():
    examples=['雨が降った場合は傘を持って行きます。雨が降らない場合は傘を家に置きます。',
        '私はりんごを三個買いました。一個を食べたので二個残っています。',
        '母が「窓を閉めて」と言いました。私は窓を閉めました。']
    for text in examples:assert select_unit(text)['text']==text


def test_promotion_external_reference_and_fantasy_are_separate_rejections():
    for text in ['私は魔法の世界へ行きました。精霊に会って話しました。',
        '雨の状態は図1を参照します。図1を見ると水量がわかります。',
        'この品は期間限定で販売中です。ご購入は公式サイトからお願いします。']:
        assert select_unit(text) is None
    assert select_unit('私は傘を買いました。代金は千円でした。') is not None
    assert select_unit('そして家に帰りました。母とご飯を食べました。') is None


def test_units_are_contiguous_source_spans_without_trailing_fragments():
    class Tokens:
        def encode(self,text):return list(range(len(text)))
    text='私は玄関で靴を履きました。母と一緒に出かけました。途中で文章が'
    units=list(literal_units(text,Tokens(),minimum=10))
    assert len(units)==1 and units[0]['text']==text[units[0]['char_start']:units[0]['char_end']]
    assert '途中' not in units[0]['text']
