"""Additional intact lead paragraphs, with the first whole-body recipe retained."""
import re

from jmicro.nested_material import NestedGroups, whole_material


class UnitGroups(NestedGroups):
    def add(self, record):
        key = (record["source"], record["body_tokens"], record["unit_kind"])
        bucket = self.pending[key]
        bucket.append(record)
        if len(bucket) < 5:
            return None
        group = list(bucket)
        bucket.clear()
        return group, self.rng.randrange(5)


def material_unit(text, original_ids, source, tokenizer):
    whole = whole_material(text, len(original_ids), source)
    if whole:
        return dict(whole, unit_kind="original-whole", source_char_start=0,
                    source_char_end=len(text), body_tokens=len(original_ids))
    if source != "web":
        return None
    # Only the first four paragraph blocks. Keep an entire original paragraph;
    # never collect arbitrary isolated sentences or patch its ending.
    boundaries = [0]
    boundaries.extend(match.end() for match in re.finditer(r"\n\s*\n", text))
    if len(boundaries) == 1:
        boundaries.extend(match.end() for match in re.finditer(r"\n", text))
    boundaries.append(len(text))
    for a, b in list(zip(boundaries, boundaries[1:]))[:4]:
        paragraph = text[a:b]
        if not paragraph.strip():
            continue
        ids = tokenizer.encode(paragraph)
        selected = whole_material(paragraph, len(ids), "web")
        if selected:
            return dict(selected, unit_kind="intact-lead-paragraph", source_char_start=a,
                source_char_end=b, body_tokens=len(ids), token_ids=[2, *ids, 3])
    return None
