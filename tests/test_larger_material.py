from collections import Counter
from jmicro.larger_material import FourGroups


def test_four_groups_match_units_lengths_sources_and_preserve_unique_subset():
    groups = FourGroups(42)
    small, large = [], []
    for i in range(96):
        record = dict(id=i, source="web" if i%2 else "story", body_tokens=64+i%3,
            unit_kind="original-whole" if i%4 else "intact-lead-paragraph")
        result = groups.add(record)
        if result:
            members, slot = result
            large.extend(members); small.append(members[slot])
    assert len(large) == 4*len(small) and small
    assert len({r["id"] for r in large}) == len(large)
    assert {r["id"] for r in small} <= {r["id"] for r in large}
    key = lambda r:(r["source"],r["body_tokens"],r["unit_kind"])
    assert Counter(map(key, large)) == Counter({k:4*v for k,v in Counter(map(key, small)).items()})
    assert sum(r["body_tokens"]+2 for r in large) == 4*sum(r["body_tokens"]+2 for r in small)
    other = FourGroups(42); again = []
    for i in range(96):
        record = dict(id=i, source="web" if i%2 else "story", body_tokens=64+i%3,
            unit_kind="original-whole" if i%4 else "intact-lead-paragraph")
        result = other.add(record)
        if result: again.append(result[0][result[1]])
    assert again == small
