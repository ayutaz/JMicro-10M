"""Literal multi-sentence Japanese Web units; no generated text or name clones."""
from collections import Counter
import re
from jmicro.complete_units import balanced,complete_sentences,unit_hash
from jmicro.evaluation import canonicalize_text

DEPENDENT=re.compile(r'^(?:そして|しかし|また、|その結果|このように|これら|それら|前述|上記|下記|次に、|つまり、|以上の|図\d|写真\d)')
REFERENCE=re.compile(r'画像を(?:見|参照)|写真を(?:見|参照)|図[0-9０-９]|表[0-9０-９]|上記|下記|前述|次のページ|こちらを|ここをクリック|https?://|www\.|続きを読む|続きはこちら|\.{3}|…|⋯')
PROMOTION=re.compile(r'お問い合わせ|ご購入|お申し込み|お申込み|ご来店|送料無料|販売中|公式サイト|当社|弊社|弊店|株式会社|ご予約|特別価格|期間限定|無料相談|キャンペーン|アフィリエイト')
FANTASY=re.compile(r'夢の中|魔法|精霊|妖精|瞬間移動|時間旅行|異世界|不思議な力|光る玉|昔の時代へ|世界に入り込|人形が話|花が話|時計が話')
DAILY=re.compile(r'私[はがのも]|僕[はがのも]|家族|友人|友達|散歩|帰宅|休日|台所|料理|買い物|洗濯|部屋|窓|玄関|学校|お茶|電車|傘|自転車|靴|手袋|誕生日|図書館')


def select_unit(text):
    text=canonicalize_text(text)
    if not text or not balanced(text) or DEPENDENT.search(text) or REFERENCE.search(text) or PROMOTION.search(text) or FANTASY.search(text):return None
    sentences=list(complete_sentences(text))
    if not 2<=len(sentences)<=6:return None
    end=0
    for start,stop,_ in sentences:
        if text[end:start].strip():return None
        end=stop
    if text[end:].strip():return None
    if len({s[2] for s in sentences})!=len(sentences):return None
    grams=Counter(text[i:i+4] for i in range(max(0,len(text)-3)))
    repetition=1-len(grams)/sum(grams.values()) if grams else 0
    if repetition>.10 or re.search(r'(.{4,}?)\1\1',text):return None
    group='daily' if DAILY.search(sentences[0][2]) else 'explanation'
    return dict(text=text,group=group,sentences=len(sentences),canonical_sha256=unit_hash(text),
        first_sentence_sha256=unit_hash(re.sub(r'[0-9０-９]+','N',sentences[0][2])),char4_repetition=repetition)


def literal_units(text,tok,minimum=32,maximum=384):
    """Join contiguous complete sentences, retain character offsets and quote scope."""
    pending=[]
    for start,end,sentence in complete_sentences(text):
        if pending and text[pending[-1][1]:start].strip():pending=[]
        pending.append((start,end,sentence))
        candidate=text[pending[0][0]:end]
        ids=tok.encode(candidate)
        if len(ids)>maximum:
            pending=[(start,end,sentence)]
            continue
        if len(pending)>=2 and len(ids)>=minimum:
            unit=select_unit(candidate)
            if unit:yield dict(unit,ids=ids,char_start=pending[0][0],char_end=end)
            pending=[]
