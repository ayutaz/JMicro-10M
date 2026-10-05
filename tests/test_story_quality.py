from jmicro.story_quality import improved_story


def test_accepts_whole_linked_story_and_preserves_text():
    text='太郎は公園で赤い花を見つけました。太郎は花を母に贈りました。母は花を見て喜びました。'
    unit=improved_story(text,70)
    assert unit and unit['text']==text and unit['linked_transitions']>=1


def test_rejects_dependent_start_even_if_the_story_ends():
    assert improved_story('つぎに、太郎は川へ行きました。太郎は魚を見つけて喜びました。',70) is None


def test_rejects_topic_changes_without_linked_entities():
    assert improved_story('太郎は公園を歩きました。宇宙船の扉が開きました。料理は完成しました。',70) is None


def test_does_not_cut_oversized_or_unfinished_story():
    text='太郎は公園で花を見つけました。太郎は花を持ち帰りました。'
    assert improved_story(text,129) is None
    assert improved_story(text+'家では',70) is None
