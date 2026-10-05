from jmicro.wikipedia_curriculum import lead


class Tokens:
    def encode(self,text):return list(range(len(text)))


def row(text,title='温度計'):
    return dict(text=text,title=title,id='123',url='https://ja.wikipedia.org/wiki/'+title)


def test_topic_and_complete_paragraphs_remain_literal():
    text='温度計は、温度を測るための道具です。測る場所に合わせて、さまざまな種類が使われています。数字の目盛りを読んで、温度を確認します。'
    unit=lead(row(text),Tokens())
    assert unit['text']==text and unit['source_family']=='wiki-123' and unit['paragraphs']==1
    assert lead(row(text+'途中で文章が'),Tokens()) is None
    assert lead(row(text,'気圧計'),Tokens()) is None


def test_no_skip_over_header_or_missing_reference_or_empty_parenthetical():
    for text in ['この道具は温度を測ります。測る場所に合わせて種類を選んで使います。',
        '概要\n\n温度計は温度を測ります。測る場所に合わせて種類を選んで使います。',
        '温度計（）は温度を測ります。測る場所に合わせて種類を選んで使います。']:
        assert lead(row(text),Tokens()) is None
