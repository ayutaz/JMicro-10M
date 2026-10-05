"""Restrict genres and agents instead of adding advertising blacklist variants."""
import re
from jmicro.diverse_text import structure
from jmicro.diverse_text_v2 import candidate as web_candidate
from jmicro.whole_short_text import whole_candidate
from jmicro.complete_units import complete_sentences,unit_hash
from jmicro.coherent_units import substantive_anchors

HUMAN=re.compile(r'男の子|女の子|少年|少女|子供|子ども|おじい|おばあ|父|母|友達|友人|生徒|先生|兄|姉|妹|弟|家族|私は|私たち')
FANTASY=re.compile(r'昔々|むかしむかし|魔法|ドラゴン|妖精|王様|海賊|宇宙|怪物|恐竜|サメ|カメ|キツネ|うさぎ|ウサギ|動物|ワニ|ライオン|猫|ネコ|犬|鳥|オオカミ|ロボット|ではなく')
SPECIAL=re.compile(r'医療|医学|医師|治療|患者|がん|癌|疾患|手術|病院|美容|サプリ|青汁|脱毛|健康食品|政治|憲法|国会|政権|議員|企業|会社|株式会社|業界|法律|税金|診療|製品|研究|プログラム|経営|事業|効果|価格|費用|支援します|ご案内|閲覧|クラブ|サポート|セミナー')
PAST=re.compile(r'(?:ました|だった|いた|した|った|んだ|いた|できた)[。！？]$')
LINK=re.compile(r'^(?:その|それ|こう|結果|翌|次|すると|そして|しかし|だから|また|一方|彼|二人|みんな|私|ある日|ついに|最後|友達|友人)')


def candidate(text,size,source):
    if structure(text)!='declarative' or SPECIAL.search(text):return None
    if source=='web':
        unit=web_candidate(text,size)
        if not unit:return None
        first=next(complete_sentences(unit['text']))[2]
        if not PAST.search(first) or not HUMAN.search(text):return None
        return unit
    unit=whole_candidate(text,size,'story')
    if not unit or not 100<=size<=128 or FANTASY.search(text) or not HUMAN.search(text):return None
    parts=[r[2] for r in complete_sentences(unit['text'])]
    if not 3<=len(parts)<=8:return None
    prior=substantive_anchors(parts[0]);links=0
    for sentence in parts[1:]:
        anchors=substantive_anchors(sentence)
        if prior&anchors or LINK.search(sentence):links+=1
        prior|=anchors
    if links*2<len(parts)-1:return None
    unit.update(structure='declarative',linked_transitions=links,
        first_sentence_hash=unit_hash(re.sub(r'[0-9０-９]+','N',parts[0])),
        ending_style='polite' if re.search(r'(?:です|ます|でした|ました)[。！？]$',parts[-1]) else 'plain')
    return unit
