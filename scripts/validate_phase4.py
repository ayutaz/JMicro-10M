"""Run Phase 4 gates sequentially, write evidence, and stop before Phase 5."""
from pathlib import Path
import argparse
import json
import os
import subprocess
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from jmicro.experiment import ROOT, now, read_json, write_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--data-root", type=Path, default=Path.home() / "jmicro-data")
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("Use a new validation directory; keep prior evidence")
    args.output.mkdir(parents=True)
    job = {"status": "running", "pid": os.getpid(), "command": sys.argv,
        "started_at": now(), "completed_stages": [], "stop_boundary": "Phase 4; no Phase 5 jobs"}
    job["process_start_ticks"] = Path("/proc/self/stat").read_text().split()[21]
    job["boot_id"] = Path("/proc/sys/kernel/random/boot_id").read_text().strip()
    write_json(args.output / "job.json", job)
    def stage(name, arguments):
        job["active_stage"] = name
        write_json(args.output / "job.json", job)
        with (args.output / f"{name}.log").open("w") as stream:
            subprocess.run([sys.executable, *map(str, arguments)], stdout=stream, stderr=subprocess.STDOUT, check=True)
        job["completed_stages"].append(name)
        write_json(args.output / "job.json", job)
        print(json.dumps({"stage": name, "status": "passed"}), flush=True)
    try:
        for model, vocab in (("t8k",8192), ("t4k",4096)):
            shards = args.data_root / f"shards/{model}-pilot"
            stage(f"resume-{model}", [ROOT / "scripts/verify_training_resume.py", "--shards", shards,
                "--model", ROOT / f"configs/models/{model}.json", "--output", args.output / f"resume-{model}"])
            stage(f"evaluate-{model}", [ROOT / "scripts/train.py", "evaluate", "--checkpoint",
                args.output / f"resume-{model}/continuous/checkpoint-00000200.pt", "--shards", shards,
                "--tokenizer", ROOT / f"artifacts/phase2/{vocab}/tokenizer.model", "--output", args.output / f"evaluation-{model}.json"])
        stage("throughput", [ROOT / "scripts/benchmark_training.py", "--data-root", args.data_root,
            "--output", args.output / "throughput"])
        job.update(status="complete", active_stage=None, completed_at=now())
    except Exception as exc:
        job.update(status="failed", failure=f"{type(exc).__name__}: {exc}", completed_at=now())
        raise
    finally:
        write_json(args.output / "job.json", job)
    print(json.dumps(job), flush=True)


if __name__ == "__main__":
    main()
