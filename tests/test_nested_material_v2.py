from pathlib import Path
from collections import Counter

from jmicro.nested_material_v2 import UnitGroups, material_unit
from jmicro.tokenizer import Tokenizer

ROOT = Path(__file__).resolve().parents[1]


def test_intact_lead_paragraph_preserves_original_bytes_and_complete_end():
    tok = Tokenizer(ROOT / "artifacts/phase2/4096/tokenizer.model")
    paragraph = "図書館では多くの本を読むことができる。静かな閲覧室があり、椅子に座って本を読める。"
    # Keep the existing64token floor; a shorter paragraph is ineligible.
    paragraph += "本を借りるときには利用者のカードを窓口に出す。返却期限を確認して、期限までに本を返す。"
    paragraph += "入口には開館時間を示す看板がある。"
    original = "地域の図書館\n\n" + paragraph + "\n\nこのページの続きは"
    unit = material_unit(original, tok.encode(original), "web", tok)
    assert unit and unit["unit_kind"] == "intact-lead-paragraph"
    assert original[unit["source_char_start"]:unit["source_char_end"]] == unit["text"]
    assert tok.decode(unit["token_ids"][1:-1]) == unit["text"]
    assert unit["text"].strip().endswith("。")
    assert "続きは" not in unit["text"]
    # No unit may be constructed from sentences deeper than the four lead blocks.
    deep = "題名\n\n見出し\n\n見出し\n\n見出し\n\n" + paragraph
    assert material_unit(deep, tok.encode(deep), "web", tok) is None


def test_quantity_groups_match_editorial_unit_as_well_as_length_and_source():
    groups = UnitGroups(42)
    small, large = [], []
    for i in range(20):
        row = dict(source="web", body_tokens=100, unit_kind="original-whole" if i % 2 else "intact-lead-paragraph", id=i)
        result = groups.add(row)
        if result:
            full, index = result
            large.extend(full); small.append(full[index])
    assert Counter(r["unit_kind"] for r in large) == Counter({k: 5*v for k,v in Counter(r["unit_kind"] for r in small).items()})
