"""Acquire pinned public Parquet files with checksums and restartable receipts."""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import fcntl
import json
import os
from pathlib import Path
import sys
import time
from urllib.error import URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from huggingface_hub import HfApi
from jmicro.data import download
from jmicro.experiment import ROOT, now, read_json, sha256, write_json


def identity():
    return {"pid": os.getpid(), "boot_id": Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
            "start_ticks": Path("/proc/self/stat").read_text().split()[21]}


def acquire(config, output, count=None, parallel=4):
    c = read_json(config)
    count = count or c["initial_files"]
    if not 1 <= count <= c["maximum_files"]:
        raise ValueError("File count exceeds bounded acquisition")
    output.mkdir(parents=True, exist_ok=True)
    with (output / "acquire.lock").open("a+") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        state = {"status": "running", "started_at": now(), "config_sha256": sha256(config),
                 "requested_files": count, "command": sys.argv, **identity()}
        write_json(output / "acquire_job.json", state)
        started = time.monotonic()
        try:
            frozen = output / "sources.json"
            if frozen.exists():
                manifest = read_json(frozen)
                if manifest["config_sha256"] != sha256(config):
                    raise ValueError("Acquisition config changed; use a separate directory")
            else:
                files = list(HfApi().list_repo_tree(c["repository"], path_in_repo=c["subset"],
                             revision=c["revision"], repo_type="dataset", recursive=True))
                files = sorted((f for f in files if f.path.rsplit("/", 1)[-1].startswith("train-")),
                               key=lambda f: f.path)[:c["maximum_files"]]
                if len(files) != c["maximum_files"] or any(not f.lfs for f in files):
                    raise ValueError("Incomplete pinned upstream metadata")
                rows = [{"path": f.path, "bytes": f.size, "sha256": f.lfs.sha256,
                         "url": f'https://huggingface.co/datasets/{c["repository"]}/resolve/{c["revision"]}/{f.path}'}
                        for f in files]
                if sum(f["bytes"] for f in rows) > c["maximum_raw_bytes"]:
                    raise ValueError("Pinned files exceed total raw limit")
                download(f'https://huggingface.co/datasets/{c["repository"]}/resolve/{c["revision"]}/README.md',
                         output / "README.upstream.md", 1000000,
                         "f08544766b53f3bd592c874768d1367f945380ce5b0ea861ff08018260f1afc6")
                manifest = {"created_at": now(), "source": c, "config_sha256": sha256(config),
                            "evidence_sha256": sha256(output / "README.upstream.md"), "files": rows}
                write_json(frozen, manifest)
            old = Path("/home/aihub_ubuntu/jmicro-data/phase6/raw")

            def fetch(row):
                if time.monotonic() - started > 7200:
                    raise TimeoutError("Acquisition exceeded two-hour stage budget")
                path = output / Path(row["path"]).name
                cached = old / path.name
                if not path.exists() and cached.exists() and sha256(cached) == row["sha256"]:
                    os.link(cached, path)
                for attempt in range(3):
                    try:
                        download(row["url"], path, row["bytes"], row["sha256"])
                        break
                    except (URLError, TimeoutError, ConnectionError):
                        if attempt == 2:
                            raise
                        time.sleep(2 ** (attempt + 1))
                if path.stat().st_size != row["bytes"] or sha256(path) != row["sha256"]:
                    raise ValueError("Acquired size/hash mismatch")
                return dict(row, local_path=str(path.resolve()), actual_sha256=row["sha256"])

            receipt = {}
            with ThreadPoolExecutor(max_workers=parallel) as executor:
                jobs = {executor.submit(fetch, row): row for row in manifest["files"][:count]}
                for job in as_completed(jobs):
                    row = job.result()
                    receipt[row["path"]] = row
                    ordered = [receipt[k] for k in sorted(receipt)]
                    progress = {"status": "running", "config_sha256": sha256(config), "files": ordered,
                                "requested_files": count, "elapsed_seconds": time.monotonic() - started}
                    write_json(output / "acquisition.json", progress)
                    state.update(completed_files=len(receipt), heartbeat_at=now())
                    write_json(output / "acquire_job.json", state)
                    print(json.dumps({"stage": "acquisition", "completed_files": len(receipt),
                                      "requested_files": count, "seconds": progress["elapsed_seconds"]}), flush=True)
            progress.update(status="complete", completed_at=now())
            write_json(output / "acquisition.json", progress)
            state.update(status="complete", completed_at=now())
        except Exception as exc:
            state.update(status="failed", completed_at=now(), failure=f"{type(exc).__name__}: {exc}")
            raise
        finally:
            write_json(output / "acquire_job.json", state)


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config", type=Path, default=ROOT / "configs/phase6/corpus_10b.json")
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--files", type=int)
    p.add_argument("--parallel", type=int, default=4)
    args = p.parse_args()
    acquire(args.config, args.output, args.files, args.parallel)
