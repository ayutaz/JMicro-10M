from jmicro.realistic_curriculum_v2 import literal_units


class Tokens:
    def encode(self,text):return list(range(len(text)))


def test_entire_parent_and_everyday_action_remain_literal():
    text='私は玄関で靴を履きました。母と一緒に出かけました。'
    unit=list(literal_units(text,Tokens(),minimum=10))[0]
    assert unit['text']==text and unit['char_start']==0 and unit['char_end']==len(text)
    assert unit['editorial_unit']=='whole original EOS parent'
    assert unit['group']=='daily'
    assert list(literal_units(text+'途中で文章が',Tokens(),minimum=10))==[]


def test_unresolved_context_and_noise_are_rejected_without_removing_local_references():
    for text in ['その同僚に話しました。次のように発表しています。',
        'この映画を見ました。面白かったです。',
        'Sat今日から大会が始まりました。七校での大会です。']:
        assert not list(literal_units(text,Tokens(),minimum=10))
    text='母が「窓を閉めて」と言いました。私はその窓を閉めました。'
    assert list(literal_units(text,Tokens(),minimum=10))[0]['text']==text
