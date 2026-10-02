from copy import deepcopy
from io import BytesIO
import json

import pytest

from jmicro.data import (cluster_records, config, contaminated, digest, distribution,
                         download, map_dialogue, normalized, tokenizer_sample, url_key)


def record(uid, text, kind="web", url="", source="a", messages=None):
    return {"doc_id": uid, "text": text, "dedup_sha256": digest(normalized(text)),
            "canonical_sha256": digest(text), "canonical_utf8_bytes": len(text.encode()),
            "status": "candidate", "source": source, "kind": kind, "url": url,
            "bucket": "sharealike" if kind == "dialogue" else "commercial_web",
            "messages_json": json.dumps(messages or []), "minhash": [], "duplicate_of": None, "split": "excluded"}


def run(rows):
    c = config()
    cluster_records(rows, c, (set(), set()))
    return rows


def test_japanese_cross_source_near_duplicates_are_removed():
    text = "東京の公園で散歩をしました。桜が咲いていて、とても気持ちのよい朝でした。" * 8
    rows = run([record("a", text, source="one"), record("b", text + "今日は晴れ。", source="two")])
    assert rows[0]["status"] == "kept"
    assert rows[1]["status"] == "duplicate" and rows[1]["duplicate_of"] == "a"
    assert rows[0]["cluster_id"] == rows[1]["cluster_id"]


def test_same_url_different_content_is_retained_in_same_split():
    rows = run([record("a", "猫と遊んだ午後。" * 10, url="https://EXAMPLE.jp/a#old"),
                record("b", "新しい電車の乗り換え案内。" * 10, url="https://example.jp/a#new")])
    assert all(r["status"] == "kept" for r in rows)
    assert rows[0]["split"] == rows[1]["split"]
    assert rows[0]["cluster_id"] == rows[1]["cluster_id"]


def test_dialogue_greetings_do_not_merge_unrelated_conversations():
    a = [{"role": "user", "text": "こんにちは"}, {"role": "assistant", "text": "こんにちは"},
         {"role": "user", "text": "料理についての話" * 20}, {"role": "assistant", "text": "野菜のスープ" * 20}]
    b = deepcopy(a)
    b[2]["text"], b[3]["text"] = "旅行についての話" * 20, "山の風景" * 20
    rows = run([record("a", "\n".join(m["text"] for m in a), "dialogue", messages=a),
                record("b", "\n".join(m["text"] for m in b), "dialogue", messages=b)])
    assert all(r["status"] == "kept" for r in rows)
    assert rows[0]["cluster_id"] != rows[1]["cluster_id"]


def test_long_shared_prefix_split_before_windowing():
    prefix = [{"role": "user" if i % 2 == 0 else "assistant", "text": x * 12}
              for i, x in enumerate(("最初の話題", "返事の内容", "二番目の話", "追加の返答"))]
    rows = []
    for uid, tail in (("a", "温かい紅茶"), ("b", "冷たい牛乳")):
        m = prefix + [{"role": "user", "text": tail * 60}]
        rows.append(record(uid, "\n".join(x["text"] for x in m), "dialogue", messages=m))
    run(rows)
    assert all(r["status"] == "kept" for r in rows)
    assert rows[0]["cluster_id"] == rows[1]["cluster_id"]
    assert rows[0]["split"] == rows[1]["split"]


def test_fixed_role_mapping_and_same_speaker_merge_preserve_source_ids():
    d = {"interlocutors": ["A", "B"], "utterances": [
        {"utterance_id": 0, "interlocutor_id": "B", "text": "朝\r\nです"},
        {"utterance_id": 1, "interlocutor_id": "B", "text": "晴れ"},
        {"utterance_id": 2, "interlocutor_id": "A", "text": "こんにちは"},
        {"utterance_id": 3, "interlocutor_id": "B", "text": "散歩する？"}]}
    messages, mapping = map_dialogue(d)
    assert mapping == {"A": "assistant", "B": "user"}
    assert messages[0] == {"role": "user", "text": "朝\nです\n晴れ", "utterance_ids": [0, 1]}
    assert [m["role"] for m in messages] == ["user", "assistant", "user"]
    d["utterances"][2]["text"] = " "
    with pytest.raises(ValueError, match="Empty"):
        map_dialogue(d)


def test_contamination_propagates_to_url_cluster():
    phrase = "これは評価専用の文で学習コーパスには含めないための文章です。"
    rows = [record("a", phrase * 3, url="https://example.jp/a"), record("b", "新しい記事の内容" * 12, url="https://example.jp/a")]
    cluster_records(rows, config(), ({phrase}, {phrase}))
    assert all(r["status"] == "excluded" and r["reason"] == "evaluation_contamination" for r in rows)
    assert contaminated(record("c", "こんにちは"), ({"こんにちは"}, set()))


def test_tokenizer_sample_is_ordered_train_only_whole_documents():
    rows = run([record(str(i), f"これは文書{i}です。" * 10) for i in range(50)])
    a, b = tokenizer_sample(rows, config())
    assert a == tokenizer_sample(list(reversed(rows)), config())[0]
    assert a and all(r["split"] == "train" for r in a)
    assert b["commercial_web"] == sum(len(r["text"].encode()) for r in a)


def test_distribution_empty_and_url_queries():
    assert distribution([])["p95"] is None
    assert distribution([1, 2, 3, 4])["p95"] == 4
    assert url_key("https://EXAMPLE.jp/p?q=1#foo") == "https://example.jp/p?q=1"
    assert normalized("Ａ\t B") == "a b"


def test_duplicate_clusters_do_not_depend_on_input_order():
    rows = [record("z", "短い日本語の文書です。" * 10), record("a", "短い日本語の文書です。" * 10),
            record("m", "別の話題で海に行って泳ぎました。" * 10)]
    left, right = run(deepcopy(rows)), run(list(reversed(deepcopy(rows))))
    fields = ("cluster_id", "status", "split", "duplicate_of")
    assert {r["doc_id"]: tuple(r[k] for k in fields) for r in left} == {r["doc_id"]: tuple(r[k] for k in fields) for r in right}


@pytest.mark.parametrize("limit,checksum,match", [(2, None, "capacity"), (10, "0"*64, "checksum")])
def test_download_rejects_oversize_and_corrupted_input(tmp_path, monkeypatch, limit, checksum, match):
    import jmicro.data as data

    class Response(BytesIO):
        headers = {}
    monkeypatch.setattr(data, "urlopen", lambda *a, **k: Response(b"source"))
    path = tmp_path / "raw.bin"
    with pytest.raises(ValueError, match=match):
        download("https://example.org/pinned", path, limit, checksum)
    assert not path.exists() and not path.with_suffix(".bin.part").exists()


def test_missing_assistant_and_invalid_unicode_are_rejected():
    d = {"interlocutors": ["A", "B"], "utterances": [{"utterance_id": 0, "interlocutor_id": "A", "text": "こんにちは"}]}
    with pytest.raises(ValueError, match="No assistant"):
        map_dialogue(d)
    d["utterances"][0]["text"] = "\ud800"
    with pytest.raises(UnicodeError):
        map_dialogue(d)
