"""Reuse closed matched partial streams without accepting a failed preparation."""
from collections import Counter
import json
from pathlib import Path
import shutil

from jmicro.eos_pilot import TrainView
from jmicro.experiment import read_json, sha256, ROOT
from jmicro.tokenizer import Tokenizer
from phase6_performance import alive

PARENT = Path("/home/aihub_ubuntu/jmicro-data/phase6/nested-material-20261006")
JOB = ROOT / "reports/phase6/nested-material-20261006/prepare-job.json"


def pin_prefix(sources):
    parent = read_json(JOB)
    assert parent["status"] == "failed" and not alive(parent)
    assert parent["binding"]["sources"] == sources
    assert parent["binding"]["builder_sha256"] == sha256(ROOT / "scripts/prepare_nested_material.py")
    assert parent["binding"]["selector_sha256"] == sha256(ROOT / "src/jmicro/nested_material.py")
    streams = {name: dict(stream_sha256=sha256(PARENT / name / "train.partial.bin"),
                         index_sha256=sha256(PARENT / name / "train.index.partial.jsonl"))
               for name in ("small", "large", "dev")}
    return dict(job_path=str(JOB), job_sha256=sha256(JOB), streams=streams,
                policy="Failed parent remains failed; only closed source/length-matched prefix reused")


def restore_prefix(data, pinned, sources, streams, indexes, offsets, documents,
                   body_bytes, totals, histograms, seen, reservoirs, sample_counts, rng):
    assert pinned["job_sha256"] == sha256(JOB) and not alive(read_json(JOB))
    tokenizer = Tokenizer(ROOT / "artifacts/phase2/4096/tokenizer.model")
    views = {s: TrainView(r["pool"], r["manifest_sha256"]) for s, r in sources.items()}
    small_ids, large_ids = set(), set()
    for name in ("small", "large", "dev"):
        original = PARENT / name
        assert sha256(original / "train.partial.bin") == pinned["streams"][name]["stream_sha256"]
        assert sha256(original / "train.index.partial.jsonl") == pinned["streams"][name]["index_sha256"]
        with (original / "train.partial.bin").open("rb") as source:
            shutil.copyfileobj(source, streams[name], length=8*1024*1024)
        for line in (original / "train.index.partial.jsonl").open():
            row = json.loads(line)
            assert row["offset"] == offsets[name]
            assert row["source_manifest_sha256"] == sources[row["source"]]["manifest_sha256"]
            assert row["split"] == ("dev" if name == "dev" else "train")
            row["unit_kind"] = "original-whole"
            row["source_char_start"] = 0
            row["source_char_end"] = None  # Original index retained byte count, not char count.
            indexes[name].write(json.dumps(row, ensure_ascii=False)+"\n")
            count = row["body_tokens"] + 2
            offsets[name] += count
            documents[name] += 1
            body_bytes[name] += row["bytes"]
            totals[name+"_"+row["source"]] += count
            histograms[name][row["source"]+":"+str(row["body_tokens"])+":original-whole"] += 1
            digest = row["canonical_sha256"]
            if name == "small":
                small_ids.add(digest)
            elif name == "large":
                assert digest not in large_ids
                large_ids.add(digest)
                seen.add(digest)
            else:
                assert digest not in seen
                seen.add(digest)
            if name in reservoirs:
                key = name+"_"+row["source"]
                sample_counts[key] += 1
                limit = 32 if name == "large" else 16
                selected = reservoirs[name][row["source"]]
                slot = len(selected) if len(selected) < limit else rng.randrange(sample_counts[key])
                if slot < limit:
                    view = views[row["source"]]
                    text = tokenizer.decode_bytes(view.tokens[row["source_start"]+1:row["source_end"]].tolist()).decode("utf-8")
                    assert len(text.encode()) == row["bytes"]
                    sample = dict(row, text=text)
                    if slot == len(selected):
                        selected.append(sample)
                    else:
                        selected[slot] = sample
        assert offsets[name] * 2 == (original / "train.partial.bin").stat().st_size
    assert small_ids <= large_ids
    assert offsets["large"] == 5 * offsets["small"] and documents["large"] == 5 * documents["small"]
    assert histograms["large"] == Counter({k: 5*v for k,v in histograms["small"].items()})
