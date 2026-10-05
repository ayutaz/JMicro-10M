"""Standalone whole original Web documents; preserve boundaries and literal wording."""
import re
from jmicro.complete_units import complete_sentences
from jmicro.realistic_curriculum import select_unit

DEPENDENT_START=re.compile(r'^(?:この|その|それ|これ|ここ|そこ|あれ|あの|もう|でも|もちろん|ところが|しかし|しかも|すると|さらに|また、|先ほど|前回|次に|以上|以下|[0-9０-９]+(?:ノート|[.．]))')
EXTERNAL=re.compile(r'前者|後者|前述|上記|下記|その三点|次のように|これから(?:紹介|説明)|今回は.*見ていき|詳細からです|資料請求|学校選び|お申込|情報を提供して|はじめまして')
ARTIFACT=re.compile(r'[■○●◆◇▶►※]|^[A-Za-z]{1,8}[ぁ-んァ-ヶ一-龯]|(?:食材数|地場産数|メニューコンテスト)')
ACTION=re.compile(r'(?:開け|閉め|歩|出かけ|帰|戻|食べ|買|洗|作|読|借|返|乗|降|拾|探|運|持|掃除|片づ|片付|炊|着|履|書|飲|聞|訪れ|行っ|行き|会っ|見つけ)')
PAST=re.compile(r'(?:ました|だった|でした|[っい]た|[んみし]だ|[しけっ]た)[。！？!？]')


def literal_units(text,tok,minimum=32,maximum=384):
    # Entire original EOS parent, rather than disconnected middle passages.
    if DEPENDENT_START.search(text.strip()) or EXTERNAL.search(text) or ARTIFACT.search(text):return
    unit=select_unit(text)
    if not unit:return
    sentences=list(complete_sentences(text))
    if len(sentences[0][2])>200:return
    ids=tok.encode(unit['text'])
    if not minimum<=len(ids)<=maximum:return
    first=sentences[0][2]
    if unit['group']=='daily' and not (ACTION.search(first) and PAST.search(first)):
        unit['group']='explanation'
    yield dict(unit,ids=ids,char_start=0,char_end=len(text),editorial_unit='whole original EOS parent')
