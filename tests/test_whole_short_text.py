from jmicro.whole_short_text import whole_candidate


def test_whole_document_accepts_complete_multisentence_text():
    text='公園のベンチに座った。雨が降り始めたので、傘を開いて家に帰った。'
    assert whole_candidate(text,70,'web')['sentences']==2


def test_whole_document_rejects_unfinished_tail_and_non_sentence_heading():
    assert whole_candidate('雨が降った。帰り道で',70,'web') is None
    assert whole_candidate('今日の出来事\n雨が降った。傘を開いた。',70,'web') is None


def test_whole_document_rejects_repetition_and_forward_links():
    assert whole_candidate('公園を歩いた。公園を歩いた。',70,'web') is None
    assert whole_candidate('公園を歩いた。続きはこちらをご覧ください。',70,'web') is None


def test_whole_document_never_shortens_oversized_source():
    assert whole_candidate('雨が降った。傘を開いた。',385,'web') is None
    assert whole_candidate('雨が降った。傘を開いた。',129,'story') is None
