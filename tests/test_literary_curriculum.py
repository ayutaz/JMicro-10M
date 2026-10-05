from jmicro.literary_curriculum import paragraphs


class Tokens:
    def encode(self,text):return list(range(len(text)))


def record(text,style='新字新仮名',copyright='なし'):
    return dict(text=text,meta={'文字遣い種別':style,'作品著作権フラグ':copyright})


def test_whole_paragraphs_and_source_metadata_filter():
    text='私は部屋の窓を閉めました。雨の音が小さくなり、静かに本を読みました。'
    unit=list(paragraphs(record(text),Tokens()))[0]
    assert unit['text']==text and unit['paragraph_index']==0
    assert not list(paragraphs(record(text,'旧字旧仮名'),Tokens()))
    assert not list(paragraphs(record(text,copyright='あり'),Tokens()))
    assert not list(paragraphs(record(text+'途中で文章が'),Tokens()))


def test_no_unintroduced_pronoun_or_fantasy():
    assert not list(paragraphs(record('彼は部屋の窓を閉めました。雨の音が小さくなり、静かに本を読みました。'),Tokens()))
    assert not list(paragraphs(record('私は魔法の世界へ行きました。精霊と話しながら花の間を歩きました。'),Tokens()))
