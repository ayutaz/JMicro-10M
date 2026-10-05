from jmicro.wikipedia_curriculum_v2 import lead


class Tokens:
    def encode(self,text):return list(range(len(text)))


def row(text):return dict(text=text,title='温度計',id='123',url='https://example.test/123')


def test_reject_extraction_holes_and_external_article_promises():
    tail='温度を測るための道具です。測る場所に合わせてさまざまな種類を選び、目盛りを読んで温度を確認します。'
    for head in ['温度計（、Thermometer）は、','温度計（おんどけい、）は、',
                 '温度計（おんどけい、、Thermometer）は、','温度計（英：）は、']:
        assert lead(row(head+tail),Tokens()) is None
    assert lead(row('温度計は、'+tail+'本項ではその他の計器にも触れます。'),Tokens()) is None
    assert lead(row('温度計は、'+tail+'（ABC）の研究員が測定しました。'),Tokens()) is None


def test_keep_literal_alias_date_and_causal_explanation():
    text='温度計（おんどけい、Thermometer）は、温度を測るための道具です。熱で液体が膨張するため、液面の位置から温度を読みます。'
    unit=lead(row(text),Tokens())
    assert unit is not None and unit['text']==text and unit['source_family']=='wiki-123'
    text='温度計の研究（1900年 - 1910年）では、液体の性質を詳しく調べました。熱で液体が膨張するため、目盛りを付けて温度を読みます。'
    assert lead(row(text),Tokens()) is not None
