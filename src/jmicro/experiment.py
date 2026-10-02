"""Portable environment capture and immutable preparation-run records."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import uuid

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[2]
SOURCE_DIRS = ("src", "scripts", "configs", "schemas", "eval", "tests", "docs")
SOURCE_FILES = ("README.md", "AGENTS.md", "pyproject.toml", "uv.lock", ".python-version", ".gitignore", ".gitattributes")
PACKAGES = ("jsonschema", "pytest", "numpy", "sentencepiece", "torch", "transformers", "datasets", "safetensors")


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def command(args: list[str], cwd: Path | None = None, timeout: int = 15) -> dict:
    try:
        result = subprocess.run(args, cwd=cwd, capture_output=True, timeout=timeout, check=False)
        def decode(raw: bytes) -> str:
            return raw.decode("utf-16" if b"\x00" in raw else "utf-8", errors="replace").strip()
        return {"available": result.returncode == 0, "exit_code": result.returncode,
                "stdout": decode(result.stdout), "stderr": decode(result.stderr)}
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"available": False, "exit_code": None, "stdout": "", "stderr": str(exc)}


def git_state(root: Path) -> dict:
    commit = command(["git", "rev-parse", "HEAD"], root)
    status = command(["git", "status", "--porcelain"], root)
    if not commit["available"] or not status["available"]:
        raise ValueError("A readable Git repository with a commit is required")
    return {"commit": commit["stdout"], "dirty": bool(status["stdout"])}


def capture_environment(root: Path = ROOT, probe_torch: bool = False) -> dict:
    versions = {}
    for package in PACKAGES:
        try:
            versions[package] = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            versions[package] = None
    nvidia = command(["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"])
    is_wsl = platform.system() == "Linux" and "microsoft" in platform.release().lower()
    wsl = command(["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", "wsl --version; wsl -l -v"]) if is_wsl else None
    torch_probe = {"performed": False, "cuda_available": None, "cuda_runtime": None, "bf16_supported": None}
    if probe_torch:
        if versions["torch"] is None:
            raise ValueError("Install the ml extra before requesting --probe-torch")
        import torch
        available = torch.cuda.is_available()
        torch_probe = {"performed": True, "cuda_available": available, "cuda_runtime": torch.version.cuda,
                       "bf16_supported": torch.cuda.is_bf16_supported() if available else False}
    disk = shutil.disk_usage(root)
    return {"schema_version": 1, "captured_at": now(), "purpose": "observed_environment",
            "platform": {"system": platform.system(), "release": platform.release(), "machine": platform.machine(),
                         "python": platform.python_version(), "python_executable": sys.executable,
                         "logical_cpu_count": os.cpu_count(), "is_wsl": is_wsl},
            "uv": command(["uv", "--version"]), "packages": versions,
            "git": git_state(root), "dependency_lock_sha256": sha256(root / "uv.lock"),
            "storage": {"root": str(root), "total_bytes": disk.total, "free_bytes": disk.free},
            "nvidia_smi": nvidia, "wsl_observation": wsl, "torch_probe": torch_probe,
            "training_target": {"system": "Windows + WSL/Linux", "gpu": "RTX 4090", "vram_gib": 24,
                                "wsl_package_version_requested": "3.x", "verified": False,
                                "verification_phase": 4, "micro_batch_policy": "largest_stable_measured"}}


def source_files(root: Path) -> list[Path]:
    paths = [root / name for name in SOURCE_FILES if (root / name).is_file()]
    for name in SOURCE_DIRS:
        paths.extend(p for p in (root / name).rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    if any(p.is_symlink() for p in paths):
        raise ValueError("Source snapshots must not include symbolic links")
    return sorted(paths, key=lambda p: p.relative_to(root).as_posix())


def validate_record(record: dict, root: Path = ROOT) -> None:
    Draft202012Validator(read_json(root / "schemas/experiment_schema.json"), format_checker=FormatChecker()).validate(record)


def verify_run(run_dir: Path, root: Path = ROOT, check_ledger: bool = True) -> dict:
    record = read_json(run_dir / "experiment.json")
    validate_record(record, root)
    refs = list(record["artifacts"].values()) + [x for x in record["inputs"].values() if x is not None]
    for ref in refs:
        target = (run_dir / ref["path"]).resolve()
        if not target.is_relative_to(run_dir.resolve()):
            raise ValueError("Artifact path escapes run directory")
        if sha256(target) != ref["sha256"]:
            raise ValueError(f"Artifact checksum mismatch: {ref['path']}")
    source = read_json(run_dir / record["artifacts"]["source_manifest"]["path"])
    for item in source:
        target = (run_dir / "source" / item["path"]).resolve()
        if not target.is_relative_to((run_dir / "source").resolve()) or sha256(target) != item["sha256"]:
            raise ValueError(f"Source checksum mismatch: {item['path']}")
    frozen_schema = run_dir / "source/schemas/experiment_schema.json"
    Draft202012Validator(read_json(frozen_schema), format_checker=FormatChecker()).validate(record)
    if check_ledger:
        entries = [json.loads(line) for line in (run_dir.parent / "experiments.jsonl").read_text(encoding="utf-8").splitlines()]
        matches = [entry for entry in entries if entry["run_id"] == record["run_id"]]
        if len(matches) != 1 or matches[0]["experiment_sha256"] != sha256(run_dir / "experiment.json"):
            raise ValueError("Experiment record differs from ledger")
    return {"run_id": record["run_id"], "verified": True, "source_file_count": len(source),
            "record_kind": record["kind"], "training_tokens_seen": record["counters"]["tokens_seen"]}


def prepare_run(name: str, root: Path = ROOT, output_root: Path | None = None,
                tokenizer_artifact: Path | None = None, dataset_manifest: Path | None = None) -> Path:
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,39}", name):
        raise ValueError("Run name must be 1-40 lowercase letters, digits, or hyphens")
    output_root = output_root or root / "reports"
    run_id = f"p0-{name}-{datetime.now(timezone.utc):%Y%m%dT%H%M%SZ}-{uuid.uuid4().hex[:8]}"
    run_dir = output_root / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    try:
        manifest = []
        for path in source_files(root):
            relative = path.relative_to(root)
            target = run_dir / "source" / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
            manifest.append({"path": relative.as_posix(), "sha256": sha256(target)})
        write_json(run_dir / "source_manifest.json", manifest)
        write_json(run_dir / "environment.json", capture_environment(root))
        artifact = lambda path: {"path": path, "sha256": sha256(run_dir / path)}
        inputs = {"tokenizer_artifact": None, "dataset_manifest": None}
        for key, path in (("tokenizer_artifact", tokenizer_artifact), ("dataset_manifest", dataset_manifest)):
            if path is not None:
                relative = f"inputs/{key}{path.suffix}"
                target = run_dir / relative
                target.parent.mkdir(exist_ok=True)
                shutil.copyfile(path, target)
                inputs[key] = artifact(relative)
        record = {"schema_version": 1, "run_id": run_id, "phase": 0, "kind": "preparation", "status": "prepared",
                  "created_at": now(), "git": git_state(root), "seed": 42,
                  "artifacts": {"source_manifest": artifact("source_manifest.json"), "environment": artifact("environment.json"),
                                "dependency_lock": artifact("source/uv.lock"), "model_config": artifact("source/configs/models/t8k.json"),
                                "comparison_model_config": artifact("source/configs/models/t4k.json"),
                                "training_config": artifact("source/configs/training/baseline.json"),
                                "tokenizer_config": artifact("source/configs/tokenizer/contract.json"),
                                "evaluation_config": artifact("source/configs/evaluation/protocol.json"),
                                "evaluation_manifest": artifact("source/eval/split_manifest.json")},
                  "inputs": inputs, "counters": {"steps": 0, "tokens_seen": 0, "assistant_teacher_tokens": 0,
                                                  "unique_documents": 0, "unique_bytes": 0},
                  "results": None, "failure_reason": None}
        validate_record(record, root)
        write_json(run_dir / "experiment.json", record)
        verify_run(run_dir, root, check_ledger=False)
    except Exception:
        shutil.rmtree(run_dir)
        raise
    ledger = {"run_id": run_id, "path": run_id, "phase": 0, "kind": "preparation", "status": "prepared",
              "created_at": record["created_at"], "experiment_sha256": sha256(run_dir / "experiment.json")}
    with (output_root / "experiments.jsonl").open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(ledger, ensure_ascii=False, allow_nan=False) + "\n")
    return run_dir


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    environment = sub.add_parser("capture-environment")
    environment.add_argument("--output", type=Path, required=True)
    environment.add_argument("--probe-torch", action="store_true")
    prepare = sub.add_parser("prepare-run")
    prepare.add_argument("--name", required=True)
    prepare.add_argument("--output-root", type=Path)
    prepare.add_argument("--tokenizer-artifact", type=Path)
    prepare.add_argument("--dataset-manifest", type=Path)
    verify = sub.add_parser("verify-run")
    verify.add_argument("run_dir", type=Path)
    args = parser.parse_args()
    if args.command == "capture-environment":
        result = capture_environment(probe_torch=args.probe_torch)
        write_json(args.output, result)
        print(f"Environment saved: {args.output}")
    elif args.command == "prepare-run":
        print(prepare_run(args.name, output_root=args.output_root, tokenizer_artifact=args.tokenizer_artifact,
                          dataset_manifest=args.dataset_manifest))
    else:
        print(json.dumps(verify_run(args.run_dir), ensure_ascii=False))


if __name__ == "__main__":
    main()
