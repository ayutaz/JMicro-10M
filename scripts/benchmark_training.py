"""Isolated CUDA batch/backend/compile measurements; uv-launched child Python only."""
from pathlib import Path
import argparse
import gc
import json
import statistics
import subprocess
import sys
import time

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import numpy as np
import torch
from jmicro.experiment import ROOT, now, read_json, sha256, write_json
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import Trainer, evaluate_body, generate_suite, gpu_lock


def worker(args):
    torch.set_num_threads(2)
    torch.cuda.set_per_process_memory_fraction(0.94)
    report = {"status": "running", "model": args.model, "batch": args.batch,
        "context": 1024, "accumulation": 1, "effective_batch_tokens": args.batch * 1024,
        "backend": args.backend, "compile": args.compile, "data_kind": args.data_kind,
        "memory_fraction_limit": 0.94, "warmup": args.warmup,
        "measured_updates": args.steps, "created_at": now(), "source_sha256": sha256(Path(__file__))}
    started = time.perf_counter()
    try:
        with gpu_lock("cuda"):
            spec = dict(seed=42, context=1024, batch=args.batch, accumulation=1,
                lr=0.002, weight_decay=0.1, warmup=1,
                schedule_updates=args.warmup + args.steps + 1, dtype="bf16",
                compile=args.compile, backend=args.backend)
            shards = Path(args.data_root) / "shards" / f"{args.model}-pilot"
            trainer = Trainer(read_json(ROOT / f"configs/models/{args.model}.json"), Shard(shards), spec, "cuda")
            if args.data_kind == "synthetic":
                generator = np.random.default_rng(42)
                def batch(size):
                    ids = generator.integers(8, trainer.model.config["vocab_size"], (size,1025), dtype=np.int64)
                    return torch.from_numpy(ids[:,:-1].copy()), torch.from_numpy(ids[:,1:].copy()), 0
                trainer.sampler.batch = batch
            torch.cuda.reset_peak_memory_stats()
            print(json.dumps({"phase": "first_update", "compile": args.compile, "batch": args.batch}), flush=True)
            first = trainer.step()
            report["first_update_seconds"] = first["seconds"]
            for _ in range(max(0, args.warmup-1)):
                trainer.step()
            metrics = []
            for index in range(args.steps):
                metrics.append(trainer.step())
                if (index+1) % 50 == 0:
                    print(json.dumps({"phase": "measuring", "updates": index+1, "total": args.steps,
                                      "tokens_per_second": metrics[-1]["tokens_per_second"]}), flush=True)
            report.update(status="passed", steady_tokens_per_second=statistics.median(r["tokens_per_second"] for r in metrics),
                steady_seconds=sum(r["seconds"] for r in metrics),
                data_wait_seconds=sum(r["data_wait_seconds"] for r in metrics),
                loss_start=first["loss"], loss_end=metrics[-1]["loss"],
                peak_vram_training=torch.cuda.max_memory_allocated(),
                peak_vram_reserved=torch.cuda.max_memory_reserved(), metrics=metrics)
            # Capacity probes include evaluation/greedy generation/save, not just a forward pass.
            if args.data_kind == "real":
                tok = Tokenizer(ROOT / f"artifacts/phase2/{'8192' if args.model == 't8k' else '4096'}/tokenizer.model")
                evaluation_started = time.perf_counter()
                body = evaluate_body(trainer.model, Shard(shards, "dev"), "cuda", "bf16", limit=4)
                generation = generate_suite(trainer.model, tok, "cuda", "bf16", limit=1, max_new=8)
                report.update(evaluation_seconds=time.perf_counter()-evaluation_started,
                              evaluation_bpb=body["bpb"], generation_outputs=len(generation["outputs"]))
            checkpoint = args.output.with_suffix(".pt")
            report["save_seconds"] = trainer.save(checkpoint)
            report["checkpoint_bytes"] = checkpoint.stat().st_size
            report["peak_vram_with_evaluation_save"] = torch.cuda.max_memory_allocated()
            # Capacity checkpoint is reproducible but not a selected training artifact.
            checkpoint.unlink()
            (checkpoint.parent / "latest.json").unlink()
    except torch.cuda.OutOfMemoryError as exc:
        report.update(status="oom", failure=str(exc))
    except Exception as exc:
        report.update(status="failed", failure=f"{type(exc).__name__}: {exc}")
    finally:
        report["wall_seconds"] = time.perf_counter()-started
        write_json(args.output, report)
    print(json.dumps({k:v for k,v in report.items() if k != "metrics"}), flush=True)
    return report["status"] == "passed"


def orchestrate(args):
    args.output.mkdir(parents=True, exist_ok=True)
    results = []
    cache = read_json(args.output / "progress.json")["results"] if args.resume else []
    used = set()
    def run(model, batch, backend="default", compiled=False, kind="real", steps=8, warmup=4):
        for index, cached in enumerate(cache):
            if index in used or cached["status"] not in ("passed","oom"):
                continue
            if all(cached.get(key) == value for key,value in dict(model=model,batch=batch,backend=backend,
                   compile=compiled,data_kind=kind,measured_updates=steps,warmup=warmup).items()):
                used.add(index)
                results.append(cached)
                print(json.dumps({"reused": cached["report"], "status": cached["status"]}), flush=True)
                return cached
        label = f"{model}-b{batch}-{backend}-{'compile' if compiled else 'eager'}-{kind}-{len(results):03d}"
        output = args.output / f"{label}-{time.time_ns()}.json"
        command = [sys.executable, str(Path(__file__).resolve()), "--worker", "--model", model,
            "--batch", str(batch), "--backend", backend, "--data-kind", kind,
            "--data-root", args.data_root, "--output", str(output), "--steps", str(steps), "--warmup", str(warmup)]
        if compiled:
            command.append("--compile")
        with output.with_suffix(".log").open("w") as log:
            try:
                subprocess.run(command, stdout=log, stderr=subprocess.STDOUT, timeout=600, check=False)
            except subprocess.TimeoutExpired:
                write_json(output, {"status": "timeout", "batch": batch, "model": model, "compile": compiled,
                    "backend": backend, "data_kind": kind, "failure": "600 second bounded probe timed out"})
        result = read_json(output)
        result["report"] = str(output.resolve())
        results.append(result)
        write_json(args.output / "progress.json", {"status": "running", "results": results})
        print(json.dumps({"probe": label, "status": result["status"], "tokens_per_second": result.get("steady_tokens_per_second")}), flush=True)
        return result
    selected = {}
    for model in ("t8k", "t4k"):
        batch, low, high = 8, 0, None
        while batch <= 512:
            result = run(model, batch)
            if result["status"] == "passed":
                low = batch
                batch *= 2
            elif result["status"] == "oom":
                high = batch
                break
            else:
                raise RuntimeError(f"Unexpected capacity probe failure: {result['report']}")
        if high is None:
            raise RuntimeError("No capacity boundary within bounded probe range")
        while high - low > 1:
            middle = (low + high) // 2
            result = run(model, middle)
            if result["status"] == "passed":
                low = middle
            elif result["status"] == "oom":
                high = middle
            else:
                raise RuntimeError(f"Unexpected boundary failure: {result['report']}")
        # Three measured runs of 200 updates, each including eval/save at the capacity limit.
        confirmation = [run(model, low, steps=200, warmup=10) for _ in range(3)]
        if not all(r["status"] == "passed" for r in confirmation):
            raise RuntimeError("Capacity confirmation failed; do not declare a stable maximum")
        selected[model] = {"maximum_stable_batch": low, "first_oom_batch": high,
            "capacity_definition": "94% CUDA allocator limit; desktop/evaluation/save headroom; 3 x 200 updates",
            "confirmation_median_tokens_per_second": statistics.median(r["steady_tokens_per_second"] for r in confirmation),
            "confirmation_range_tokens_per_second": [min(r["steady_tokens_per_second"] for r in confirmation), max(r["steady_tokens_per_second"] for r in confirmation)]}
        run(model, low, kind="synthetic", steps=200, warmup=10)
        # Same batch for backend comparison and compile, keeping the capacity series separate.
        for backend in ("math", "flash"):
            run(model, 8, backend=backend, steps=30, warmup=5)
        run(model, 8, compiled=True, steps=200, warmup=10)
        eligible = [r for r in results if r["model"] == model and r["status"] == "passed" and r["data_kind"] == "real"]
        fastest = max(eligible, key=lambda r:r["steady_tokens_per_second"])
        selected[model]["fastest_measured"] = {key:fastest[key] for key in ("batch", "backend", "compile", "steady_tokens_per_second", "report")}
    write_json(args.output / "throughput_report.json", {"status": "passed", "selected": selected, "results": results,
        "limits": "Finite bounded capacity tests; no assertion of indefinite stability or model quality. All measurements are BF16 training at context 1024."})
    print(json.dumps({"status": "passed", "selected": selected}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--data-root", default=str(Path.home() / "jmicro-data"))
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--resume", action="store_true", help="Reuse passed/oom probes after fixing a failed gate")
    parser.add_argument("--model", choices=["t8k", "t4k"], default="t8k")
    parser.add_argument("--batch", type=int, default=8)
    parser.add_argument("--backend", choices=["default", "math", "flash"], default="default")
    parser.add_argument("--data-kind", choices=["real", "synthetic"], default="real")
    parser.add_argument("--compile", action="store_true")
    parser.add_argument("--steps", type=int, default=8)
    parser.add_argument("--warmup", type=int, default=4)
    args = parser.parse_args()
    if args.worker:
        sys.exit(0 if worker(args) else 1)
    else:
        orchestrate(args)


if __name__ == "__main__":
    main()
