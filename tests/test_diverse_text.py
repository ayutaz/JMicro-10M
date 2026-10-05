from jmicro.diverse_text import candidate,structure


def test_preserves_complete_causal_text():
    text='庭の花壇が乾いていたので、花の根元に水を注いだ。水が土にしみ込むのを確かめ、花壇をもう一度見てからじょうろを片づけた。'
    r=candidate(text,80)
    assert r and r['text']==text and r['structure']=='declarative' and r['linked_transitions']==1
    assert candidate(text+'明日は',80) is None


def test_rejects_noise_and_repeated_document():
    text='庭の土が乾いていたので、花の根元に水を注いだ。水が土にしみ込むのを確かめ、花をもう一度見た。'
    assert candidate(text+'ご予約を受け付けます。',80) is None
    assert candidate(text+text,120) is None
    assert candidate(text,257) is None


def test_structural_holdout_priority():
    assert structure('もし雨なら、傘を持っていく。')=='conditional'
    assert structure('彼は「もし雨なら傘を持とう」と言った。')=='quotation'
    assert structure('雨なので傘を持って出かけた。')=='declarative'
