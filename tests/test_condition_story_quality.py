from jmicro.condition_story_quality import exclusion_reasons

def test_related_action_and_resolution_remain_eligible():
    text='花子はなくした本を探しました。花子は机の下で本を見つけました。見つかった本をかばんに入れ、花子は安心しました。'
    assert not exclusion_reasons(text)

def test_same_speaker_answering_self_is_rejected():
    text='お母さんは「一緒に探しましょう」と言いました。お母さんは「わかったわ」と答えました。二人は本を見つけました。'
    assert 'same_speaker_self_answer' in exclusion_reasons(text)

def test_unbounded_lesson_is_not_an_action_based_ending():
    text='リリーは割れた花瓶を粘土で直しました。リリーは何でも粘土で直せることを学んだのでした。'
    reasons=exclusion_reasons(text)
    assert 'didactic_closing' in reasons and 'unbounded_closing_generalization' in reasons

def test_fictional_setting_alone_is_not_a_defect():
    text='星は空で一人ぼっちでした。星は小さな月に会いました。月は星と一緒に空を散歩し、二人は仲良くなりました。'
    assert not exclusion_reasons(text)
