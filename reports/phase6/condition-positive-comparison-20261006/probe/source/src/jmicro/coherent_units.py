"""Conservative contiguous multi-sentence selection, not a semantic certificate."""
from collections import Counter
import re

from jmicro.complete_units import complete_sentences, unit_hash

DEPENDENT_START = re.compile(r'^(?:そして|しかし|また|さらに|それ|その|これ|この|こちら|そこ|こう|そう|なお|つまり|ところが|したがって|一方|例えば|たとえば|ちなみに|特に|なので|ですが|だが|でも|ただ|では|なぜ|という|で[、,]|続いて|おかげ|上の|下の|以下|上記|前述|[0-9０-９]+つ[目は])')
BOILERPLATE = re.compile(r'お問い合わせ|申し込み|お申し込み|購入[者す]|ご購入|買取|通販|クリック|ランキング|ホームページ|当社|弊社|キャンペーン|アフィリエイト|無料|ご覧ください|下記|次回|次のページ|詳細は|紹介します|紹介する|説明します|解説します|おすすめ|お勧め|本稿|本書|続く|続き|こちら|\b(?:http|HTML|SEO|CVR)\b', re.I)
FORWARD_END = re.compile(r'(?:見て[いみ]きましょう|見てみましょう|チェックしてみましょう|説明して[いみ]きます|始めましょう|つづく|ご紹介します)[。！？!?」]*$|[？?][」』]*$')
GENERIC = {'こと', 'もの', 'ため', 'よう', 'です', 'ます', 'した', 'する', 'して', 'った', 'いる', 'ある', 'なる', 'など', 'から', 'ので', 'れる', 'れた', 'ます'}


def substantive_anchors(text):
    # Shared two-kanji strings are a conservative topic-continuity proxy.
    return set(re.findall(r'(?=([一-龯]{2}))', text)) - GENERIC


def acceptable_sentences(sentences):
    if not 2 <= len(sentences) <= 6:
        return False
    text = ''.join(sentences)
    if (DEPENDENT_START.search(sentences[0]) or BOILERPLATE.search(text) or FORWARD_END.search(text)
            or re.search(r'先[ほ程]ど|先程|下のよう|前の|^\s*[・●]|\n\s*[・●Q]',text)
            or re.search(r'(?:ためです|という話になります|ということである)[。！？!?]*$',sentences[0])):
        return False
    if len(set(sentences)) != len(sentences) or re.search(r'(.{4,}?)\1\1', text):
        return False
    grams = Counter(text[i:i+4] for i in range(max(0, len(text)-3)))
    if grams and 1 - len(grams)/sum(grams.values()) > .18:
        return False
    # The relationship is visible either through topic repetition or an explicit
    # causal/temporal/anaphoric connector after an independently introduced start.
    prior = substantive_anchors(sentences[0])
    for sentence in sentences[1:]:
        anchors = substantive_anchors(sentence)
        connector = re.match(r'^(?:その(?:後|ため|結果|時|日|店|人)|それ(?:で|から|を|に|は)|翌[日朝]|次[の日]|すると|だから|しかし|そして|一方|また[、]|こうして)', sentence)
        if not (prior & anchors or connector):
            return False
        prior |= anchors
    return True


def coherent_units(text, tok, minimum=32, maximum=64):
    sentences = list(complete_sentences(text))
    used_until = -1
    for i, (start, _, _) in enumerate(sentences):
        if start < used_until:
            continue
        pieces, previous_end = [], start
        for a, b, sentence in sentences[i:i+6]:
            if text[previous_end:a].strip():
                break
            pieces.append(sentence)
            previous_end = b
            if len(pieces) < 2 or not acceptable_sentences(pieces):
                continue
            candidate = text[start:b]
            ids = tok.encode(candidate)
            if len(ids) > maximum:
                break
            if len(ids) >= minimum and all(t >= 8 for t in ids):
                yield dict(text=candidate, ids=ids, char_start=start, char_end=b,
                           sentences=len(pieces), text_sha256=unit_hash(candidate))
                used_until = b
                break
