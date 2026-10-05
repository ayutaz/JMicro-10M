"""Keep literal whole paragraphs from modern-orthography public-domain books."""
import re
from jmicro.realistic_curriculum import select_unit
from jmicro.realistic_curriculum_v2 import DEPENDENT_START,EXTERNAL,ARTIFACT


def paragraphs(record,tok):
    meta=record['meta']
    if meta.get('文字遣い種別')!='新字新仮名' or meta.get('作品著作権フラグ')!='なし':return
    for i,text in enumerate(re.split(r'\n+',record['text'])):
        text=text.strip()
        if not text or DEPENDENT_START.search(text) or EXTERNAL.search(text) or ARTIFACT.search(text):continue
        if re.match(r'^(?:彼[はがのも]|彼女[はがのも]|あちら|そちら|どちら)',text):continue
        unit=select_unit(text)
        if not unit:continue
        ids=tok.encode(unit['text'])
        if not 32<=len(ids)<=384:continue
        yield dict(unit,ids=ids,paragraph_index=i,editorial_unit='whole paragraph from original cleaned book; no sentence slicing')
