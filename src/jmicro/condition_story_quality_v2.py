"""Observable condition checks and concrete closing proxy, never semantic proof."""
import re
from jmicro.complete_units import complete_sentences
from jmicro.condition_story_quality import exclusion_reasons as previous_reasons

MAGIC = re.compile(r'魔法|不思議な力|空想|夢の中|夢を見')
MORAL = re.compile(r'教訓|この(?:経験|お話).{0,20}学|大切なことを学')
ABSOLUTE = re.compile(r'(?:もう)?二度と[^。！？]{0,35}(?:ない|ありません|なくな)|何でも.{0,20}(?:でき|直せ|治せ)')
INTENTION = re.compile(r'ないように(?:する|した|しよう|[^。！？]{0,12}(?:心がけ|気を|注意|努))|決め|心がけ|願|約束')
ACTION = re.compile(r'帰[りるっ]|戻[りるっ]|返[しすさ]|見つけ|拾[いうっ]|受け取|渡[しすっ]|開[けきくい]|閉[めじ]|作[りるっ]|建[てちつ]|描[きくい]|読[みむん]|書[きくい]|食[べい]|飲[みむん]|眠[りるっ]|寝[たてる]|遊[びぶん]|片付|掃[いく]|洗[いうっ]|助け|抱[きくい]|話[しす]|捕[まえ]|探[しす]|飛[びぶん]|走[りるっ]|歩[きくい]|泳[ぎぐい]')
RECOVERY = re.compile(r'拾|取り戻|取って|受け取|つか|掴|キャッチ|戻ってき|持って(?:帰|戻)|探し.{0,20}見つ')
# Observable common object nouns; no claim to resolve all implicit Japanese roles.
OBJECTS = r'石|小石|ボール|本|鍵|おもちゃ|帽子|手紙|鉛筆|クレヨン|指輪|人形|コイン|貝殻'
THROW = re.compile(r'(' + OBJECTS + r')(?:を|は)[^。！？]{0,20}投げ')


def additional_reasons(text):
    sentences = [r[2] for r in complete_sentences(text)]
    reasons = []
    if MORAL.search(text):
        reasons.append('nonfinal_didactic_generalization_proxy')
    for sentence in sentences:
        if ABSOLUTE.search(sentence) and not INTENTION.search(sentence):
            reasons.append('unqualified_never_again_outcome')
    # A stated intention and its direct denial, without a intervening change of mind.
    for match in re.finditer(r'([一-龯ぁ-ゖァ-ヺー]{2,12})ようと', text):
        stem = re.split(r'[はがをにでと]', match.group(1))[-1]
        if len(stem) < 2:
            continue
        following = text[match.end():]
        denial = re.search(re.escape(stem) + r'(?:ようとした|つもり)(?:わけ)?(?:では|じゃ)?(?:ない|なかった)', following)
        if denial and not re.search(r'気が変|考え直|やめること|誤解|勘違い', following[:denial.start()]):
            reasons.append('asserted_intention_then_direct_denial')
    for match in THROW.finditer(text):
        following = text[match.end():]
        returned = re.search(re.escape(match.group(1)) + r'(?:を|は)[^。！？]{0,20}返', following)
        if returned and not RECOVERY.search(following[:returned.start()]):
            reasons.append('thrown_object_return_without_recovery')
    # Opening a locked door needs an unlocking/retrieval event in ordinary settings.
    locked = re.search(r'鍵がかかって(?:い|いまし|いま|いた|いて)', text)
    if locked and not MAGIC.search(text):
        following = text[locked.end():]
        opened = re.search(r'(?:ドア|扉)(?:を|は).{0,8}開け', following)
        if opened and not re.search(r'鍵を(?:開|使|回)|解錠|鍵が(?:開|外)|開けてもら|鍵を渡|鍵を見つ', following[:opened.start()]):
            reasons.append('locked_door_opens_without_unlocking')
    if not MAGIC.search(text) and re.search(r'風船を(?:放|離)', text) and re.search(r'(?:ゆっくり|ふわふわ).{0,15}地面', text):
        reasons.append('unsupported_slow_descent_after_release')
    for sentence in sentences:
        location = re.search(r'([一-龯ァ-ヶー]{2,16})の近くに置', sentence)
        if location and not re.search(r'それを|これを|[一-龯ァ-ヶー]{2,16}を', sentence):
            if text[:text.find(sentence)].count(location.group(1)) >= 2:
                reasons.append('missing_locative_object_proxy')
    # Only explicit ability restrictions; no attempt to infer general world truth.
    restricted = re.search(r'(飛ぶ|泳ぐ|渡る|登る|出る)(?:こと)?が?でき(?:ませんでした|なかった)', text)
    if restricted and not MAGIC.search(text):
        following = text[restricted.end():]
        support = re.search(r'助け|教え|練習|治[しるっ]|扉を開|鍵を開|手伝|連れて|橋を作|羽が', following)
        roots = {'飛ぶ':r'飛[びぶん]', '泳ぐ':r'泳[ぎぐい]', '渡る':r'渡[りるっ]',
            '登る':r'登[りるっ]', '出る':r'飛び出|外に出|外へ出|出てい'}
        if re.search(roots[restricted.group(1)], following) and not support:
            reasons.append('ability_restriction_changed_without_support_proxy')
    # Restrict this contrast to stories that demonstrate a concrete late action.
    # This composition proxy can reject valid stories; calibration records that.
    ending = ''.join(sentences[-3:])
    if not ACTION.search(ending):
        reasons.append('no_concrete_late_action_proxy')
    return sorted(set(reasons))


def exclusion_reasons(text):
    return sorted(set(previous_reasons(text) + additional_reasons(text)))
