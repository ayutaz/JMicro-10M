from jmicro.narrative_diversity import candidate


def test_retains_human_action_and_rejects_fantasy():
    text='男の子は学校から届いた支援物資を仕分けした。支援物資を品物ごとに分けると、必要なものを見つけやすくなった。みんなは男の子にお礼を伝えた。'
    assert candidate(text,110,'story')['text']==text
    assert candidate(text.replace('男の子','魔法を使う男の子'),110,'story') is None
    assert candidate(text.replace('お礼','「ありがとう」'),110,'story') is None


def test_excludes_advertising_without_slicing():
    assert candidate('私は広告のサービスを体験しました。治療により健康になり、美容を楽しみました。',80,'web') is None
    text='私は庭の花壇を片づけました。花壇の草を抜き終えて、机で少し休みました。'
    assert candidate(text,80,'web')['text']==text
    assert candidate(text+'次に',80,'web') is None
