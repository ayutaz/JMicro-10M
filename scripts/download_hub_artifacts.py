"""Download a pinned public handoff bundle and restore verified original paths."""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import tempfile


ROOT = Path(__file__).resolve().parents[1]


def sha256(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def safe_path(root, name):
    path = PurePosixPath(name)
    if path.is_absolute() or ".." in path.parts or "\\" in name:
        raise ValueError(f"Unsafe artifact path: {name}")
    target = (root / name).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError(f"Artifact path escapes directory: {name}")
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Verify an already downloaded bundle offline")
    parser.add_argument("--destination", type=Path, default=ROOT)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    pin = json.loads((ROOT / "configs/hub/artifacts.json").read_text())
    source = args.source
    if source is None:
        if not pin["revision"]:
            parser.error("Publication is on hold; the Hub commit is not pinned yet. See docs/20_publication_review.md.")
        from huggingface_hub import hf_hub_download, snapshot_download

        download_dir = ROOT / "artifacts/hub-downloads" / pin["revision"]
        source = Path(hf_hub_download(pin["repo_id"], "artifact_manifest.json",
                                     repo_type="dataset", revision=pin["revision"],
                                     local_dir=download_dir, token=False)).parent
    manifest_path = source / "artifact_manifest.json"
    if sha256(manifest_path) != pin["manifest_sha256"]:
        raise ValueError("Artifact manifest SHA-256 differs from the project pin")
    manifest = json.loads(manifest_path.read_text())
    if manifest["schema_version"] != 1 or manifest["repo_id"] != pin["repo_id"]:
        raise ValueError("Artifact manifest identity differs")
    if args.source is None:
        source = Path(snapshot_download(pin["repo_id"], repo_type="dataset", revision=pin["revision"],
                                        local_dir=download_dir, token=False,
                                        allow_patterns=[*manifest["files"], "artifact_manifest.json", "SHA256SUMS"]))
    for name, expected in manifest["files"].items():
        path = safe_path(source, name)
        if path.stat().st_size != expected["size"] or sha256(path) != expected["sha256"]:
            raise ValueError(f"Artifact checksum/size differs: {name}")
    expected_paths = {f"artifacts/phase2/{v}/{n}" for v in (4096, 8192)
                      for n in ("tokenizer.model", "tokenizer.vocab", "tokenizer_wrapper.json",
                                "special_tokens.json", "training_metadata.json")}
    expected_paths.update(f"data/phase1/processed/{n}" for n in
                          ("corpus.jsonl", "dataset_manifest.parquet", "split_manifest.json",
                           "tokenizer_sample.jsonl", "data_pilot_report.json", "dialogue_data_report.json"))
    if set(manifest["restore_paths"]) != expected_paths:
        raise ValueError("Unexpected restore paths in artifact manifest")
    pending = []
    if not args.verify_only:
        for name in manifest["restore_paths"]:
            target = safe_path(args.destination, name)
            if target.exists():
                if sha256(target) != manifest["files"][name]["sha256"]:
                    raise ValueError(f"Refusing to overwrite different local artifact: {name}")
            else:
                pending.append((safe_path(source, name), target))
        for original, target in pending:
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as stream:
                    temporary = Path(stream.name)
                    with original.open("rb") as input_stream:
                        shutil.copyfileobj(input_stream, stream)
                os.replace(temporary, target)
            finally:
                if temporary is not None:
                    temporary.unlink(missing_ok=True)
    print(json.dumps({"status": "passed", "verified_files": len(manifest["files"]),
                      "restored_files": len(pending), "revision": pin["revision"]}))


if __name__ == "__main__":
    main()
