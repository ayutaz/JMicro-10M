import json
import sys
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/"scripts"))
from prepare_textbook_mixture import cached_groups


def fixtures(tmp_path,choices):
    large,small=tmp_path/"large.jsonl",tmp_path/"small.jsonl"
    rows=[dict(doc_id=f"doc-{i}",canonical_sha256=f"sha-{i}",source_family=f"family-{i}",
        body_tokens=64 if i<4 else 80,source="web" if i<4 else "textbook",unit_kind="intact-paragraph-first32",
        offset=i*100) for i in range(8)]
    large.write_text("".join(json.dumps(r)+"\n" for r in rows))
    small.write_text("".join(json.dumps(dict(rows[i],offset=j*66))+"\n" for j,i in enumerate(choices)))
    return large,small,rows


def test_cached_selection_preserves_actual_nested_members_and_three_source_provenance(tmp_path):
    large,small,rows=fixtures(tmp_path,[3,4])
    result=list(cached_groups(large,small))
    assert result==[(rows[:4],3),(rows[4:],0)]
    assert result[1][0][0]["source"]=="textbook"


def test_recomposition_rejects_silent_selection_from_another_group(tmp_path):
    large,small,_=fixtures(tmp_path,[4,3])
    with pytest.raises(AssertionError):list(cached_groups(large,small))


def test_recomposition_rejects_missing_or_extra_large_group_rows(tmp_path):
    large,small,_=fixtures(tmp_path,[3,4])
    lines=large.read_text().splitlines(keepends=True)
    large.write_text("".join(lines[:-1]))
    with pytest.raises(AssertionError):list(cached_groups(large,small))
    large.write_text("".join(lines)+lines[-1])
    with pytest.raises(AssertionError):list(cached_groups(large,small))
