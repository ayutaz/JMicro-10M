"""Literal complete opening paragraphs with an explicit article topic."""
import re
from jmicro.complete_units import balanced,complete_sentences
from jmicro.realistic_curriculum import select_unit
from jmicro.realistic_curriculum_v2 import DEPENDENT_START


def complete_paragraph(text):
    end=0;parts=list(complete_sentences(text))
    if not parts or not balanced(text):return False
    for a,b,_ in parts:
        if text[end:a].strip():return False
        end=b
    return not text[end:].strip()


def lead(record,tok):
    text=record['text'].strip();title=record['title']
    if not text or DEPENDENT_START.search(text) or re.search(r'\(\s*\)|（\s*）|\[\d+\]|\{\{|\}\}',text[:2000]):return None
    # Only consecutive complete paragraphs from the actual beginning.
    collected=[]
    for paragraph in text.split('\n\n',3)[:3]:
        if not complete_paragraph(paragraph):return None
        collected.append(paragraph);candidate='\n\n'.join(collected)
        if len(candidate)>1800:return None
        unit=select_unit(candidate)
        if not unit:continue
        ids=tok.encode(unit['text'])
        if len(ids)>512:return None
        if len(ids)<48:continue
        if title not in unit['text'][:250]:return None
        return dict(unit,ids=ids,group='encyclopedic',paragraphs=len(collected),source_family='wiki-'+record['id'],
            article_id=record['id'],source_url=record['url'],title=title,
            editorial_unit='1-3 whole consecutive opening paragraphs, no mid-sentence slicing',
            source_history='Explicit new source acquisition; overlap with old Web corpus is not independently audited')
    return None
