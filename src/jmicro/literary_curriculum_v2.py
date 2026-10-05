"""Stricter literal paragraph source; calibrations are excluded from new samples."""
import re
from jmicro.literary_curriculum import paragraphs as original_paragraphs

DEPENDENT=re.compile(r'^(?:と(?:[、，]|[言い思目])|そう|こんな|はっと|さて|乃ち|尚|▲|[二三四五六七八九十]人(?:は|が|も)|ふたり(?:は|が|も)|彼ら|彼女ら)')
ARCHAIC=re.compile(r'〳|〵|ゞ|云|其|於|乃ち|何れ|幇|匪|迚|綜|所謂|エタ|穢多|頽|直きじき|斯く|爾')
FANTASY=re.compile(r'人魚|王さま|お姫さま|観音|(?:木|草|花|影|時計|樽|人形).{0,32}(?:うれし|悲し|話し|大きな声|心を開|煙突.*はえ)|(?:手|足|腕).{0,12}ちぎれ.{0,16}飛')
PROMOTION=re.compile(r'お客様|ご提案|ご案内|ご要望|御社|当金庫|トライアルセット|美容液|スキンケア|シャンプー.*(?:体験|試し)|ご満足|レッスン.*参加|強度な構造')


def accepted_text(text):
    return not (DEPENDENT.search(text.strip()) or ARCHAIC.search(text) or FANTASY.search(text) or PROMOTION.search(text))


def paragraphs(record,tok):
    for unit in original_paragraphs(record,tok):
        if accepted_text(unit['text']):yield unit
