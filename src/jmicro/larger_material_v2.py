"""Keep all eligible intact lead blocks, with siblings in one split.

The original whole-body and paragraph quality rules are unchanged. An accepted
whole body is emitted alone so that overlapping paragraph copies are not added.
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
    boundaries = [0]
    boundaries.extend(match.end() for match in re.finditer(r"\n\s*\n", text))
    if len(boundaries) == 1:
        boundaries.extend(match.end() for match in re.finditer(r"\n", text))
    boundaries.append(len(text))
    units = []
    for a, b in list(zip(boundaries, boundaries[1:]))[:4]:
        paragraph = text[a:b]
        if not paragraph.strip():
            continue
        ids = tokenizer.encode(paragraph)
        selected = whole_material(paragraph, len(ids), "web")
        if selected:
            units.append(dict(selected, unit_kind="intact-lead-paragraph",
                source_char_start=a, source_char_end=b, body_tokens=len(ids),
                token_ids=[2, *ids, 3]))
    if units:
        # Keep the first unit's previous family allocation, and assign every
        # sibling to it. A source article cannot straddle train and dev.
        for unit in units:
            unit["source_family"] = units[0]["source_family"]
            unit["split"] = units[0]["split"]
    return units
