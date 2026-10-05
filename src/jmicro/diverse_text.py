"""Whole-source diversity selection; proxies never certify semantic quality."""
import re
from jmicro.whole_short_text import whole_candidate
from jmicro.complete_units import complete_sentences,unit_hash
from jmicro.coherent_units import substantive_anchors

CONDITION=re.compile(r'もし|場合|たら|なら')
NOISE=re.compile(r'お客様|お客さま|御社|株式会社|有限会社|ご予約|ご利用|いただ[くきけ]|致します|いたします|販売|料金|価格|税込|送料|ポイント|サイト|ブログ|メール|ログイン|メニュー|記事|掲載|筆者|転載|予約|受付|営業時間|プロフィール|[©®]|[A-Za-z]{5,}|[0-9０-９]{4}|[◆■★●▼]|(?:^|\n)\s*[・※]')
LINK=re.compile(r'^(?:その|それ|こう|結果|翌|次|すると|そして|しかし|だから|また|一方|彼|二人|みんな|私)')


def structure(text):
    if '「' in text:return 'quotation'
    if CONDITION.search(text):return 'conditional'
    return 'declarative'


def candidate(text,size):
    unit=whole_candidate(text,size,'web')
    if not unit or not 64<=size<=256 or NOISE.search(text):return None
    parts=[r[2] for r in complete_sentences(unit['text'])]
    if not 2<=len(parts)<=8:return None
    meaningful=[c for c in text if not c.isspace()]
    if sum(bool(re.match(r'[ぁ-んァ-ヶ一-龯]',c)) for c in meaningful)/len(meaningful)<.65:return None
    prior=substantive_anchors(parts[0]);linked=0
    for sentence in parts[1:]:
        anchors=substantive_anchors(sentence)
        if prior&anchors or LINK.search(sentence):linked+=1
        prior|=anchors
    if linked*2<len(parts)-1:return None
    # Protect first-sentence continuity across tokenizer boundaries with a newline.
    prefix=unit['text'][:next(complete_sentences(unit['text']))[1]]
    unit.update(structure=structure(text),linked_transitions=linked,prefix=prefix,
        first_sentence_hash=unit_hash(re.sub(r'[0-9０-９]+','N',parts[0])),
        ending_style='polite' if re.search(r'(?:です|ます|でした|ました)[。！？]$',parts[-1]) else 'plain')
    return unit
