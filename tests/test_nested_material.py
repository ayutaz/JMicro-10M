from collections import Counter

from jmicro.nested_material import NestedGroups, whole_material


def test_nested_groups_preserve_source_lengths_and_eos_ratio():
    groups = NestedGroups(42)
    small, large = [], []
    for i in range(60):
        row = dict(id=i, source="web" if i % 2 else "story", body_tokens=64 + i % 3)
        result = groups.add(row)
        if result:
            all_rows, selected = result
            large.extend(all_rows)
            small.append(all_rows[selected])
    assert len(large) == 5 * len(small) and len(small) > 0
    assert {r["id"] for r in small} <= {r["id"] for r in large}
    assert len({r["id"] for r in large}) == len(large)
    short_hist = Counter((r["source"], r["body_tokens"]) for r in small)
    full_hist = Counter((r["source"], r["body_tokens"]) for r in large)
    assert full_hist == Counter({k: 5 * v for k, v in short_hist.items()})
    assert sum(r["body_tokens"] + 2 for r in large) == 5 * sum(r["body_tokens"] + 2 for r in small)


def test_whole_text_is_kept_and_fragment_promise_and_missing_metadata_rejected():
    body = "健太は学校から帰った。机に鞄を置いて宿題を始めた。"
    selected = whole_material(body, 64, "story")
    assert selected and selected["text"] == body
    assert whole_material(body + "そのあと", 70, "story") is None
    assert whole_material("図書館は本を借りられる施設である。詳しくは次のページを見てください。", 70, "web") is None
    assert whole_material("健太（、）は学校から帰った。机に鞄を置いた。", 64, "story") is None
    assert whole_material("健太は魔法で学校へ行った。机に鞄を置いた。", 64, "story") is None
