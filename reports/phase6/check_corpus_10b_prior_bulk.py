"""Read-only preservation check against the earlier, retained review evidence."""
import json
from pathlib import Path
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))
from jmicro.corpus_state import read_json, write_json
from jmicro.experiment import ROOT, now, sha256


def objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from objects(child)


def check():
    started = time.monotonic()
    sources = [ROOT / "reports/phase6/base_500m_review.json",
               ROOT / "reports/phase6/repetition_diagnosis_review.json",
               ROOT / "configs/phase6/corpus_10b.json"]
    reviews = [read_json(path) for path in sources[:2]]
    config = read_json(sources[2])
    expected = {}

    def bind(path, digest):
        path = Path(path)
        previous = expected.setdefault(path, digest)
        if previous != digest:
            raise ValueError(f"Historical bindings disagree: {path}")

    for review in reviews:
        for obj in objects(review):
            path = obj.get("path", "")
            digest = obj.get("sha256")
            if digest and (path.endswith(".pt") or
                           ("/shards/" in path and path.endswith("/manifest.json"))):
                bind(path, digest)
    bind(config["protected_corpus"], config["protected_corpus_sha256"])
    bind(ROOT / config["tokenizer"], config["tokenizer_sha256"])
    checked = []

    def verify(path, digest):
        if time.monotonic() - started > 180:
            raise TimeoutError("Read-only preservation check exceeded 180 seconds")
        actual = sha256(path)
        if actual != digest:
            raise ValueError(f"Historical artifact differs: {path}")
        checked.append({"path": str(path), "sha256": actual, "bytes": path.stat().st_size})

    for path, digest in expected.items():
        verify(path, digest)
        if path.name == "manifest.json":
            manifest = read_json(path)
            verify(path.parent / "token_bytes.json", manifest["token_bytes_sha256"])
            for split, details in manifest["splits"].items():
                verify(path.parent / f"{split}.bin", details["stream_sha256"])
                if (path.parent / f"{split}.bin").stat().st_size != details["tokens"] * 2:
                    raise ValueError(f"Historical uint16 size differs: {split}")
                verify(path.parent / f"{split}.index.json", details["index_sha256"])
    if len([p for p in expected if p.suffix == ".pt"]) < 19:
        raise ValueError("Expected all retained Base checkpoints plus the pilot checkpoint")
    if len([p for p in expected if p.name == "manifest.json"]) != 2:
        raise ValueError("Expected both pilot and expanded shard manifests")
    result = {"status": "passed_prior_bulk_preserved", "completed_at": now(),
              "evidence_bindings": {str(p): sha256(p) for p in sources},
              "checker_sha256": sha256(Path(__file__)), "files": checked,
              "files_checked": len(checked), "bytes_checked": sum(x["bytes"] for x in checked),
              "checkpoints_checked": len([p for p in expected if p.suffix == ".pt"]),
              "elapsed_seconds": time.monotonic() - started,
              "scope": "All scheduled stable/decay Base checkpoints, pilot checkpoint, both old shard manifests and all train/dev/test streams/indexes/token byte tables, protected expanded corpus and pinned T4K Tokenizer; byte preservation only",
              "training_updates": 0, "model_or_heldout_scoring": False,
              "new_corpus_audit_completed": False}
    write_json(ROOT / "reports/phase6/corpus_10b_prior_bulk_preserved.json", result)
    print(json.dumps({k: v for k, v in result.items() if k != "files"}), flush=True)


if __name__ == "__main__":
    check()
