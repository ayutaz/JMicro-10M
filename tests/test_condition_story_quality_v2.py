from jmicro.condition_story_quality_v2 import additional_reasons, exclusion_reasons


def test_stated_intention_denial_requires_change_of_mind():
    bad='太郎は友達を驚かせようと近づきました。母は「驚かせようとしたわけじゃないね」と言いました。太郎は帰りました。'
    assert 'asserted_intention_then_direct_denial' in additional_reasons(bad)
    good=bad.replace('母は', '太郎は考え直してやめました。母は')
    assert 'asserted_intention_then_direct_denial' not in additional_reasons(good)


def test_object_return_requires_recovery_after_throw():
    story='花子はボールを投げました。花子はボールを返しました。花子は帰りました。'
    assert 'thrown_object_return_without_recovery' in additional_reasons(story)
    recovered=story.replace('花子はボールを返', '花子はボールを拾いました。花子はボールを返')
    assert 'thrown_object_return_without_recovery' not in additional_reasons(recovered)


def test_locked_door_guard_preserves_explicit_unlocking():
    story='ドアには鍵がかかっていました。太郎はドアを開けました。太郎は帰りました。'
    assert 'locked_door_opens_without_unlocking' in additional_reasons(story)
    unlocked=story.replace('太郎はドアを開け', '太郎は鍵を回しました。太郎はドアを開け')
    assert 'locked_door_opens_without_unlocking' not in additional_reasons(unlocked)


def test_future_caution_is_not_an_achieved_universal_outcome():
    bad='花子は皿を片付けました。花子は二度と何もこぼさなくなりました。花子は帰りました。'
    assert 'unqualified_never_again_outcome' in additional_reasons(bad)
    factual=bad.replace('こぼさなくなりました', 'こぼさないようになりました')
    assert 'unqualified_never_again_outcome' in additional_reasons(factual)
    good=bad.replace('こぼさなくなりました', 'こぼさないように心がけました')
    assert 'unqualified_never_again_outcome' not in additional_reasons(good)


def test_magic_and_failed_repair_are_not_semantic_errors():
    fantasy='魔法の鳥は月に会いました。鳥は月と一緒に空を飛びました。鳥は家に帰りました。'
    assert not exclusion_reasons(fantasy)
    failure='太郎はベルトで足を治そうとしました。ベルトは切れました。太郎は助けられず悲しみ、家に帰りました。'
    assert 'unqualified_never_again_outcome' not in additional_reasons(failure)
