"""All eligible intact paragraphs in the first32 blocks of a bounded article.

This changes the allowed paragraph position, not the original content filters.
Retain every sibling's first eligible family/split; accepted whole bodies remain
alone. This recipe needs new unseen content review before any GPU learning.
"""
import re

from jmicro.nested_material import whole_material


def material_units(text, original_ids, source, tokenizer):
    whole = whole_material(text, len(original_ids), source)
    if whole:
        return [dict(whole, unit_kind="original-whole", source_char_start=0,
                     source_char_end=len(text), body_tokens=len(original_ids))]
    if source != "web":
        return []
    boundaries=[0]
    boundaries.extend(m.end() for m in re.finditer(r"\n\s*\n",text))
    if len(boundaries)==1:
        boundaries.extend(m.end() for m in re.finditer(r"\n",text))
    boundaries.append(len(text))
    units=[]
    for position,(a,b) in enumerate(list(zip(boundaries,boundaries[1:]))[:32]):
        paragraph=text[a:b]
        if not paragraph.strip(): continue
        ids=tokenizer.encode(paragraph)
        selected=whole_material(paragraph,len(ids),"web")
        if selected:
            units.append(dict(selected,unit_kind="intact-paragraph-first32",
                source_char_start=a,source_char_end=b,paragraph_position=position,
                body_tokens=len(ids),token_ids=[2,*ids,3]))
    if units:
        for unit in units:
            unit["source_family"]=units[0]["source_family"]
            unit["split"]=units[0]["split"]
    return units
