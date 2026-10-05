"""Repair known metadata leakage; preserve complete text and unseen review."""
import re
from jmicro.diverse_text import candidate as original

META=re.compile(r'一覧|リスト|広告|画像|図表|このページ|詳細ページ|次のとおり|次のトピック|ドキュメント|ご連絡|貴社|ご提供|お待ち|お役立て|お役立|事業所|当施設|ご希望|オプション|法律事務所|インスパイア|ご投稿|ご参加|お申し込|連絡ください|紹介頂|表として|取り組み 原子|予防など|\s[・※]|ご用意|会社の玄関')
FORWARD=re.compile(r'(?:考察しよう|説明することができます|扱います|お応えします|表す)[。！？]$')
INLINE=re.compile(r'^.{3,35}\s+.{2,25}\s+.{2,35}\s+[^。]{2,25}')


def candidate(text,size):
    unit=original(text,size)
    if not unit or META.search(text) or FORWARD.search(text.rstrip()):return None
    if INLINE.search(text.strip()):return None
    return unit
