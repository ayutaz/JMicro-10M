"""Freeze upstream SHA-256 metadata and acquire a bounded expansion through uv."""
from pathlib import Path
import argparse
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from huggingface_hub import HfApi
from jmicro.data import download
from jmicro.experiment import ROOT, now, read_json, sha256, write_json


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", type=Path, default=ROOT / "configs/phase6/preparation.json")
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--files", type=int)
    args = p.parse_args()
    c = read_json(args.config)
    count = args.files or c["initial_files"]
    if not 1 <= count <= c["maximum_files"]:
        raise ValueError("Acquisition exceeds frozen file limit")
    args.output.mkdir(parents=True, exist_ok=True)
    frozen = args.output / "sources.json"
    if frozen.exists():
        manifest = read_json(frozen)
        if manifest["config_sha256"] != sha256(args.config):
            raise ValueError("Acquisition configuration changed")
    else:
        files = list(HfApi().list_repo_tree(c["repository"], path_in_repo=c["subset"],
                     revision=c["revision"], repo_type="dataset", recursive=True))
        files = sorted((r for r in files if r.path.rsplit("/", 1)[-1].startswith("train-")), key=lambda r: r.path)[:c["maximum_files"]]
        if len(files) != c["maximum_files"] or any(not r.lfs for r in files):
            raise ValueError("Pinned source metadata is incomplete")
        rows = [{"path": r.path, "bytes": r.size, "sha256": r.lfs.sha256,
                 "url": f'https://huggingface.co/datasets/{c["repository"]}/resolve/{c["revision"]}/{r.path}'} for r in files]
        if sum(r["bytes"] for r in rows) > c["maximum_raw_bytes"]:
            raise ValueError("Frozen source metadata exceeds raw capacity")
        evidence = f'https://huggingface.co/datasets/{c["repository"]}/resolve/{c["revision"]}/README.md'
        download(evidence, args.output / "README.upstream.md", 1000000,
                 "f08544766b53f3bd592c874768d1367f945380ce5b0ea861ff08018260f1afc6")
        manifest = {"created_at": now(), "config_sha256": sha256(args.config), "source": c,
                    "evidence_sha256": sha256(args.output / "README.upstream.md"), "files": rows}
        write_json(frozen, manifest)
    receipt = []
    for row in manifest["files"][:count]:
        path = args.output / Path(row["path"]).name
        print(json.dumps({"status": "acquiring", "file": path.name, "bytes": row["bytes"]}), flush=True)
        download(row["url"], path, row["bytes"], row["sha256"])
        receipt.append(dict(row, local_path=str(path.resolve()), actual_sha256=sha256(path)))
        write_json(args.output / "acquisition.json", {"status": "running", "config_sha256": sha256(args.config), "files": receipt})
    write_json(args.output / "acquisition.json", {"status": "complete", "config_sha256": sha256(args.config), "files": receipt, "completed_at": now()})
    print(json.dumps({"status": "complete", "files": len(receipt), "raw_bytes": sum(r["bytes"] for r in receipt)}), flush=True)


if __name__ == "__main__":
    main()
