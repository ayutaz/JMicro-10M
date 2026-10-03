"""Measured training on verified shards, completed-update checkpoints and evaluation."""
from contextlib import contextmanager
from pathlib import Path
import argparse
import hashlib
import json
import math
import os
import random
import re
import shutil
import signal
import sys
import time

import numpy as np
import torch
from torch.nn import functional as F
from jsonschema import validate

from jmicro.evaluation import bits_per_byte
from jmicro.experiment import ROOT, capture_environment, git_state, now, read_json, sha256, write_json
from jmicro.model import JMicroModel
from jmicro.shards import BlockSampler, Shard, build_shards
from jmicro.tokenizer import SUPPRESS_IDS, Tokenizer


def rng_state():
    return {"python": random.getstate(), "numpy": np.random.get_state(),
            "torch": torch.get_rng_state(),
            "cuda": torch.cuda.get_rng_state_all() if torch.cuda.is_available() else []}


def restore_rng(state):
    random.setstate(state["python"])
    np.random.set_state(state["numpy"])
    torch.set_rng_state(state["torch"])
    if state["cuda"]:
        torch.cuda.set_rng_state_all(state["cuda"])


@contextmanager
def isolated_evaluation(model):
    state, training = rng_state(), model.training
    try:
        model.eval()
        with torch.inference_mode():
            yield
    finally:
        model.train(training)
        restore_rng(state)


def seed_all(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    torch.backends.cuda.matmul.allow_tf32 = False
    torch.backends.cudnn.allow_tf32 = False


def learning_rate_factor(spec, step):
    """LR for the next completed update; WSD stable is independent of its budget."""
    if step < spec["warmup"]:
        return (step + 1) / max(1, spec["warmup"])
    mode = spec.get("scheduler", "cosine")
    if mode == "wsd":
        return 1.0
    if mode == "wsd_decay":
        progress = min(1.0, max(0.0, (step-spec["branch_at"]) / spec["decay_updates"]))
        floor = spec["minimum_lr_ratio"]
    elif mode == "cosine":
        progress = min(1.0, (step-spec["warmup"]) / max(1, spec["schedule_updates"]-spec["warmup"]))
        floor = 0.1
    else:
        raise ValueError("Unknown scheduler")
    return floor + (1-floor) * (1+math.cos(math.pi*progress)) / 2


def validate_schedule(spec):
    mode = spec.get("scheduler", "cosine")
    if mode not in ("cosine", "wsd", "wsd_decay"):
        raise ValueError("Unknown scheduler")
    if not 0 <= spec["warmup"] < spec["schedule_updates"]:
        raise ValueError("Invalid warmup or update budget")
    if mode == "wsd_decay":
        if (spec["branch_at"] < spec["warmup"] or spec["decay_updates"] < 1
                or spec["schedule_updates"] != spec["branch_at"]+spec["decay_updates"]
                or not 0 <= spec["minimum_lr_ratio"] < 1):
            raise ValueError("Invalid decay branch schedule")


def implementation_hashes():
    # Ignore checkout newline conversions, preserve every other source byte.
    names = ("src/jmicro/model.py", "src/jmicro/shards.py", "src/jmicro/training.py", "uv.lock")
    return {name: hashlib.sha256((ROOT / name).read_bytes().replace(b"\r\n", b"\n")).hexdigest()
            for name in names}


def atomic_json(path, value):
    temporary = path.with_suffix(path.suffix + ".tmp")
    write_json(temporary, value)
    os.replace(temporary, path)


def synchronize(device):
    if str(device).startswith("cuda"):
        torch.cuda.synchronize()


def autocast(device, dtype):
    return torch.autocast(device_type=torch.device(device).type,
                          dtype=torch.bfloat16, enabled=dtype == "bf16")


def scoring_windows(body_tokens, context=1024, stride=512):
    """(input start/end, first/last target): every body target exactly once."""
    if not 1 <= stride < context:
        raise ValueError("Stride must be smaller than context")
    for first in range(1, body_tokens + 1, stride):
        end = min(first + stride, body_tokens + 1)
        start = max(0, end - context)
        yield start, end, first, end


class DocumentSampler(BlockSampler):
    """Train-only, document-local body/EOS windows for memorization checks.

    Each epoch teaches every body token and EOS exactly once. Padding and
    overlapping context are ignored in labels; no preceding document is visible.
    """
    def __init__(self, shard, context, seed):
        if shard.split != "train" or context < 2:
            raise ValueError("Document sampler requires train and context >= 2")
        self.shard, self.context, self.seed = shard, context, seed
        self.tasks = []
        for document in shard.index:
            offset, count = document["offset"], document["body_tokens"]
            for start, end, first, last in scoring_windows(count, context, min(512, context-1)):
                self.tasks.append((offset, start, end, first, last))
            end = count + 1
            self.tasks.append((offset, max(0, end+1-context), end, end, end+1))
        self.blocks = len(self.tasks)
        if not self.blocks:
            raise ValueError("Empty document sampler")
        self.epoch, self.position = 0, 0
        self._shuffle()

    def state_dict(self):
        return dict(super().state_dict(), mode="document")

    def load_state_dict(self, state):
        if state.get("mode") != "document":
            raise ValueError("Sampler mode differs")
        super().load_state_dict(state)

    def batch(self, size):
        inputs = np.zeros((size, self.context), dtype=np.int64)
        targets = np.full_like(inputs, -100)
        for row in range(size):
            if self.position == self.blocks:
                self.epoch += 1
                self.position = 0
                self._shuffle()
            offset, start, end, first, last = self.tasks[int(self.order[self.position])]
            self.position += 1
            ids = np.asarray(self.shard.tokens[offset+start:offset+end], dtype=np.int64)
            inputs[row, :len(ids)] = ids
            targets[row, first-start-1:last-start-1] = self.shard.tokens[offset+first:offset+last]
        body_bytes = int(self.shard.byte_lengths[np.where(targets >= 0, targets, 0)].sum())
        return torch.from_numpy(inputs), torch.from_numpy(targets), body_bytes


def evaluate_body(model, shard, device, dtype="fp32", limit=None, context=1024):
    rows, body_nll, eos_nll, byte_count = [], 0.0, 0.0, 0
    with isolated_evaluation(model):
        for document in shard.index[:limit]:
            offset, count = document["offset"], document["body_tokens"]
            ids = torch.tensor(np.asarray(shard.tokens[offset:offset + count + 2], dtype=np.int64), device=device)
            nll, scored = 0.0, 0
            for start, end, first, last in scoring_windows(count, context, min(512, context - 1)):
                with autocast(device, dtype):
                    logits = model(ids[start:end][None]).logits[0]
                value = F.cross_entropy(logits[first-start-1:last-start-1], ids[first:last], reduction="sum")
                nll += float(value)
                scored += last - first
            start = max(0, len(ids) - context)
            with autocast(device, dtype):
                logits = model(ids[start:-1][None]).logits[0, -1]
            eos = float(F.cross_entropy(logits[None], ids[-1:]))
            if scored != count:
                raise ValueError("Body targets were not scored exactly once")
            rows.append({"doc_id": document["doc_id"], "body_tokens": count,
                         "body_bytes": document["bytes"], "body_nll": nll, "eos_nll": eos})
            body_nll += nll
            eos_nll += eos
            byte_count += document["bytes"]
    return {"split": shard.split, "limit_documents": limit, "documents": len(rows),
            "body_nll": body_nll, "eos_nll": eos_nll, "body_bytes": byte_count,
            "bpb": bits_per_byte(body_nll, byte_count), "context": context,
            "stride": min(512, context - 1), "rows": rows}


def generate_suite(model, tok, device, dtype, split="dev", limit=None, max_new=64, sampling=False):
    cases = [json.loads(line) for line in (ROOT / "eval/base.jsonl").read_text().splitlines()]
    cases = [case for case in cases if case["split"] == split][:limit]
    outputs = []
    with isolated_evaluation(model):
        for case in cases:
            prompt = [2, *tok.encode(case["prefix"])]
            if len(prompt) + max_new > model.config["max_position_embeddings"]:
                raise ValueError("Generation prompt exceeds context budget")
            modes = [(True, None), (False, None)] + ([(True, seed) for seed in (42,43,44)] if sampling else [])
            for suppressed, seed in modes:
                generator = torch.Generator(device=device).manual_seed(seed) if seed is not None else None
                cache, generated = None, []
                current = torch.tensor([prompt], device=device)
                reason = "max_new_tokens"
                for _ in range(max_new):
                    with autocast(device, dtype):
                        result = model(current, cache=cache, use_cache=True)
                    cache = result.cache
                    scores = result.logits[0, -1].clone()
                    if suppressed:
                        scores[list(SUPPRESS_IDS)] = -torch.inf
                    if generator is None:
                        next_id = int(scores.argmax())
                    else:
                        ordered, indexes = (scores / 0.8).sort(descending=True)
                        probabilities = ordered.softmax(-1)
                        drop = probabilities.cumsum(-1) - probabilities >= 0.9
                        probabilities[drop] = 0
                        next_id = int(indexes[torch.multinomial(probabilities, 1, generator=generator)])
                    generated.append(next_id)
                    if next_id == 3:
                        reason = "stop_id"
                        break
                    current = torch.tensor([[next_id]], device=device)
                raw = tok.decode_bytes(generated) if 1 not in generated else b""
                try:
                    text, valid = raw.decode(), 1 not in generated
                except UnicodeDecodeError:
                    text, valid = raw.decode(errors="replace"), False
                outputs.append({"id": case["id"], "category": case["category"],
                    "prefix": case["prefix"], "split": split, "suppressed": suppressed,
                    "decoding": "sampling" if seed is not None else "greedy", "seed": seed if seed is not None else 42,
                    "generated_ids": generated, "text": text, "valid_utf8": valid,
                    "role_leak": any(i in (4,5,6,7) for i in generated),
                    "empty_response": not text.strip(), "stop_reason": reason,
                    "repetition": bool(re.search(r"(.{2,}?)\1\1", text, flags=re.DOTALL)),
                    "human_scores": None})
    return {"suite_sha256": sha256(ROOT / "eval/base.jsonl"), "split": split,
            "limit_cases": limit, "max_new_tokens": max_new, "decoding": "greedy",
            "sampling_evaluated": sampling, "temperature": 0.8 if sampling else None,
            "top_p": 0.9 if sampling else None, "outputs": outputs}


class Trainer:
    def __init__(self, model_config, shard, spec, device="cpu"):
        validate_schedule(spec)
        if shard.split != "train":
            raise ValueError("Only train records may be used for learning")
        if spec["context"] > model_config["max_position_embeddings"]:
            raise ValueError("Training context exceeds model")
        if model_config["vocab_size"] != shard.manifest["vocab_size"]:
            raise ValueError("Tokenizer/model vocabulary differs")
        if spec["dtype"] == "bf16" and str(device).startswith("cuda") and not torch.cuda.is_bf16_supported():
            raise ValueError("CUDA BF16 unavailable")
        self.spec, self.shard, self.device = spec, shard, device
        seed_all(spec["seed"])
        self.model = JMicroModel(model_config).to(device)
        decay, no_decay = [], []
        for parameter in self.model.parameters():
            (decay if parameter.ndim >= 2 else no_decay).append(parameter)
        self.optimizer = torch.optim.AdamW([
            {"params": decay, "weight_decay": spec["weight_decay"]},
            {"params": no_decay, "weight_decay": 0.0}], lr=spec["lr"],
            betas=(0.9, 0.95), eps=1e-8, fused=str(device).startswith("cuda"))
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda step: learning_rate_factor(spec, step))
        sampler_mode = spec.get("sampler", "block")
        if sampler_mode not in ("block", "document"):
            raise ValueError("Unknown sampler mode")
        sampler_class = DocumentSampler if sampler_mode == "document" else BlockSampler
        self.sampler = sampler_class(shard, spec["context"], spec["seed"])
        self.update = self.tokens = self.supervised_tokens = self.body_bytes = 0
        self.token_digest = "00" * 32
        self.lineage = None
        self.forward = torch.compile(self.model) if spec.get("compile") else self.model

    def step(self):
        synchronize(self.device)
        started = time.perf_counter()
        batches = [self.sampler.batch(self.spec["batch"]) for _ in range(self.spec["accumulation"])]
        denominator = sum(int(y.ne(-100).sum()) for _, y, _ in batches)
        if denominator == 0:
            raise ValueError("No supervised targets")
        data_wait = time.perf_counter() - started
        self.optimizer.zero_grad(set_to_none=True)
        nll = 0.0
        self.model.train()
        digest = hashlib.sha256(bytes.fromhex(self.token_digest))
        for x, y, _ in batches:
            digest.update(x.numpy().astype("<i8").tobytes())
            digest.update(y.numpy().astype("<i8").tobytes())
            x, y = x.to(self.device), y.to(self.device)
            from torch.nn.attention import sdpa_kernel, SDPBackend
            backend = self.spec.get("backend", "default")
            selected = {"math": [SDPBackend.MATH], "flash": [SDPBackend.FLASH_ATTENTION],
                        "default": [SDPBackend.FLASH_ATTENTION, SDPBackend.EFFICIENT_ATTENTION, SDPBackend.MATH, SDPBackend.CUDNN_ATTENTION]}[backend]
            with sdpa_kernel(selected), autocast(self.device, self.spec["dtype"]):
                kwargs = {"attention_mask": x.ne(0)} if self.spec.get("sampler") == "document" else {}
                logits = self.forward(x, **kwargs).logits
                loss = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), y.reshape(-1),
                                       ignore_index=-100, reduction="sum") / denominator
            loss.backward()
            nll += float(loss.detach())
        norm = torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0, error_if_nonfinite=True)
        if not math.isfinite(nll):
            raise ValueError("Nonfinite loss")
        lr = self.optimizer.param_groups[0]["lr"]
        self.optimizer.step()
        self.scheduler.step()
        self.update += 1
        tokens = sum(x.numel() for x, _, _ in batches)
        self.tokens += tokens
        self.supervised_tokens += denominator
        self.body_bytes += sum(b for _, _, b in batches)
        self.token_digest = digest.hexdigest()
        synchronize(self.device)
        duration = time.perf_counter() - started
        return {"update": self.update, "loss": nll, "gradient_norm": float(norm), "lr": lr,
                "tokens_seen": self.tokens, "supervised_tokens": self.supervised_tokens,
                "body_bytes_seen": self.body_bytes, "token_digest": self.token_digest,
                "seconds": duration, "data_wait_seconds": data_wait, "tokens_per_second": tokens / duration}

    def save(self, path):
        started = time.perf_counter()
        path.parent.mkdir(parents=True, exist_ok=True)
        state = {"version": 2, "spec": self.spec, "model_config": self.model.config,
            "model": self.model.state_dict(), "optimizer": self.optimizer.state_dict(),
            "scheduler": self.scheduler.state_dict(), "rng": rng_state(),
            "sampler": self.sampler.state_dict(), "update": self.update, "tokens": self.tokens,
            "supervised_tokens": self.supervised_tokens, "body_bytes": self.body_bytes,
            "token_digest": self.token_digest, "shard_manifest_sha256": sha256(self.shard.directory / "manifest.json"),
            "implementation_sha256": implementation_hashes()}
        if self.lineage is not None:
            state["lineage"] = self.lineage
            state["branch_updates"] = self.update-self.lineage["parent_update"]
            state["branch_tokens"] = self.tokens-self.lineage["parent_tokens"]
        temporary = path.with_suffix(".tmp")
        with temporary.open("wb") as stream:
            torch.save(state, stream)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
        atomic_json(path.parent / "latest.json", {"path": str(path.resolve()), "sha256": sha256(path),
                    "update": self.update, "tokens_seen": self.tokens})
        return time.perf_counter() - started

    def load(self, path, *, decay_branch=False):
        state = torch.load(path, map_location="cpu", weights_only=False)
        if state.get("implementation_sha256") != implementation_hashes():
            raise ValueError("Resume implementation differs or checkpoint predates source binding")
        if state["model_config"] != self.model.config:
            raise ValueError("Resume configuration differs")
        if decay_branch:
            mutable = {"scheduler", "schedule_updates", "branch_at", "decay_updates", "minimum_lr_ratio"}
            if (state["spec"].get("scheduler") != "wsd" or self.spec.get("scheduler") != "wsd_decay"
                    or state["update"] != self.spec["branch_at"] or state["update"] < state["spec"]["warmup"]
                    or {k:v for k,v in state["spec"].items() if k not in mutable}
                    != {k:v for k,v in self.spec.items() if k not in mutable}):
                raise ValueError("Decay branch must fork a completed stable WSD update with identical training settings")
        elif state["spec"] != self.spec:
            raise ValueError("Resume configuration differs; scheduler/budget must remain frozen")
        if state["shard_manifest_sha256"] != sha256(self.shard.directory / "manifest.json"):
            raise ValueError("Resume data differs")
        self.model.load_state_dict(state["model"])
        self.optimizer.load_state_dict(state["optimizer"])
        if decay_branch:
            # Preserve Adam moments and the global update counter, install only the
            # explicit branch schedule. The first branch update starts at peak LR.
            self.scheduler.last_epoch = state["update"]
            self.scheduler._step_count = state["scheduler"]["_step_count"]
            self.scheduler.base_lrs = state["scheduler"]["base_lrs"]
            values = [base*learning_rate_factor(self.spec, state["update"]) for base in self.scheduler.base_lrs]
            for group, value in zip(self.optimizer.param_groups, values):
                group["lr"] = value
            self.scheduler._last_lr = values
            self.lineage = {"kind": "wsd_decay", "parent_checkpoint": str(path.resolve()),
                "parent_sha256": sha256(path), "parent_update": state["update"], "parent_tokens": state["tokens"],
                "parent_spec": state["spec"], "parent_token_digest": state["token_digest"]}
        else:
            self.scheduler.load_state_dict(state["scheduler"])
            self.lineage = state.get("lineage")
        self.sampler.load_state_dict(state["sampler"])
        self.update, self.tokens = state["update"], state["tokens"]
        self.supervised_tokens, self.body_bytes = state["supervised_tokens"], state["body_bytes"]
        self.token_digest = state["token_digest"]
        restore_rng(state["rng"])


def source_snapshot(destination):
    hashes = {}
    for name in ("src", "scripts", "configs", "schemas", "eval"):
        for path in sorted((ROOT / name).rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                relative = path.relative_to(ROOT)
                target = destination / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
                hashes[str(relative)] = sha256(path)
    for name in ("pyproject.toml", "uv.lock", ".python-version", "AGENTS.md"):
        shutil.copyfile(ROOT / name, destination / name)
        hashes[name] = sha256(ROOT / name)
    return hashes


@contextmanager
def gpu_lock(device):
    if not str(device).startswith("cuda"):
        yield
        return
    import fcntl
    root = Path(os.environ.get("JMICRO_DATA_ROOT", str(Path.home() / "jmicro-data")))
    root.mkdir(parents=True, exist_ok=True)
    with (root / "gpu.lock").open("a+") as stream:
        try:
            fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise RuntimeError("Another JMicro GPU job holds the lock")
        stream.seek(0)
        stream.truncate()
        stream.write(json.dumps({"pid": os.getpid(), "started": now(), "command": sys.argv}))
        stream.flush()
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)


def train_command(args):
    spec = {key: getattr(args, key) for key in ("seed", "context", "batch", "accumulation", "lr", "weight_decay", "warmup", "schedule_updates", "dtype", "compile", "backend")}
    if args.sampler != "block":
        spec["sampler"] = args.sampler
    if args.scheduler != "cosine":
        spec["scheduler"] = args.scheduler
    if args.branch_from:
        parent = torch.load(args.branch_from, map_location="cpu", weights_only=False)
        spec.update(scheduler="wsd_decay", branch_at=parent["update"],
                    decay_updates=args.decay_updates, minimum_lr_ratio=args.minimum_lr_ratio)
    elif args.resume:
        prior = torch.load(args.resume, map_location="cpu", weights_only=False)
        if prior["spec"].get("scheduler") == "wsd_decay":
            spec.update({k: prior["spec"][k] for k in ("scheduler", "branch_at", "decay_updates", "minimum_lr_ratio")})
    trainer = Trainer(read_json(args.model), Shard(args.shards), spec, args.device)
    run = args.output
    if args.resume:
        trainer.load(args.resume)
        record = read_json(run / "run.json")
        if record["spec"] != spec:
            raise ValueError("Run configuration differs")
        metrics = [json.loads(line) for line in (run / "metrics.jsonl").read_text().splitlines()]
        if metrics and metrics[-1]["update"] > trainer.update:
            # Retain the abandoned partial interval, then continue from the checkpoint.
            shutil.copyfile(run / "metrics.jsonl", run / f"metrics-before-resume-{time.time_ns()}.jsonl")
            (run / "metrics.jsonl").write_text("".join(json.dumps(row) + "\n" for row in metrics if row["update"] <= trainer.update))
    else:
        if run.exists():
            raise ValueError("Use --resume for an existing run directory")
        run.mkdir(parents=True)
        if args.branch_from:
            if run.resolve() == args.branch_from.parent.resolve():
                raise ValueError("Branch output must differ from parent run")
            trainer.load(args.branch_from, decay_branch=True)
        record = {"version": 1, "kind": "training", "run_id": run.name, "phase": args.phase,
            "status": "running", "created_at": now(), "git": git_state(ROOT),
            "spec": spec, "model_config": trainer.model.config,
            "shard_manifest_sha256": sha256(args.shards / "manifest.json"),
            "source_sha256": source_snapshot(run / "snapshot"),
            "tokens_seen": trainer.tokens, "update": trainer.update, "checkpoint": None, "failure_reason": None}
        if trainer.lineage is not None:
            record["lineage"] = trainer.lineage
        write_json(run / "environment.json", capture_environment(probe_torch=True))
    record.update(status="running", pid=os.getpid(), command=sys.argv, started_at=now())
    if Path("/proc/self/stat").exists():
        record["process_start_ticks"] = Path("/proc/self/stat").read_text().split()[21]
        record["boot_id"] = Path("/proc/sys/kernel/random/boot_id").read_text().strip()
    validate(record, read_json(ROOT / "schemas/training_run.schema.json"))
    atomic_json(run / "run.json", record)
    stopped = False
    def stop(*_):
        nonlocal stopped
        stopped = True
    signal.signal(signal.SIGTERM, stop)
    signal.signal(signal.SIGINT, stop)
    if args.device.startswith("cuda"):
        torch.cuda.reset_peak_memory_stats()
    end = min(args.stop_after or args.schedule_updates, args.schedule_updates)
    checkpoint = args.resume
    try:
        with (run / "metrics.jsonl").open("a", buffering=1) as stream:
            while trainer.update < end and not stopped:
                row = trainer.step()
                stream.write(json.dumps(row, allow_nan=False) + "\n")
                if trainer.update == 1 or trainer.update % args.log_every == 0:
                    print(json.dumps(row), flush=True)
                if trainer.update % args.save_every == 0:
                    checkpoint = run / f"checkpoint-{trainer.update:08d}.pt"
                    row["save_seconds"] = trainer.save(checkpoint)
                    record.update(update=trainer.update, tokens_seen=trainer.tokens, checkpoint=str(checkpoint.resolve()))
                    atomic_json(run / "run.json", record)
        checkpoint = run / f"checkpoint-{trainer.update:08d}.pt"
        save_seconds = trainer.save(checkpoint)
        record.update(status="interrupted" if stopped else ("complete" if trainer.update == args.schedule_updates else "paused"),
            update=trainer.update, tokens_seen=trainer.tokens, supervised_tokens=trainer.supervised_tokens,
            body_bytes_seen=trainer.body_bytes, sampler=trainer.sampler.state_dict(),
            token_digest=trainer.token_digest, checkpoint=str(checkpoint.resolve()), save_seconds=save_seconds,
            peak_vram_bytes=torch.cuda.max_memory_allocated() if args.device.startswith("cuda") else None,
            completed_at=now())
        if trainer.lineage is not None:
            record.update(branch_updates=trainer.update-trainer.lineage["parent_update"],
                          branch_tokens=trainer.tokens-trainer.lineage["parent_tokens"])
    except Exception as exc:
        record.update(status="failed", failure_reason=f"{type(exc).__name__}: {exc}",
                      checkpoint=str(checkpoint.resolve()) if checkpoint else None, completed_at=now())
        raise
    finally:
        atomic_json(run / "run.json", record)
        ledger = ROOT / f"reports/phase{args.phase}/training_runs.jsonl"
        ledger.parent.mkdir(parents=True, exist_ok=True)
        with ledger.open("a") as stream:
            stream.write(json.dumps(record, allow_nan=False) + "\n")
    print(json.dumps({"run": str(run), "status": record["status"], "tokens": trainer.tokens}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build = commands.add_parser("build-shards")
    build.add_argument("--corpus", type=Path, default=ROOT / "data/phase1/processed/corpus.jsonl")
    build.add_argument("--tokenizer", type=Path, required=True)
    build.add_argument("--output", type=Path, required=True)
    build.add_argument("--limit", type=int)
    train = commands.add_parser("train")
    train.add_argument("--model", type=Path, default=ROOT / "configs/models/t8k.json")
    train.add_argument("--shards", type=Path, required=True)
    train.add_argument("--output", type=Path, required=True)
    train.add_argument("--device", choices=["cpu", "cuda"], default="cuda")
    train.add_argument("--dtype", choices=["bf16", "fp32"], default="bf16")
    train.add_argument("--context", type=int, default=1024)
    train.add_argument("--batch", type=int, default=2)
    train.add_argument("--accumulation", type=int, default=1)
    train.add_argument("--seed", type=int, default=42)
    train.add_argument("--lr", type=float, default=0.002)
    train.add_argument("--weight-decay", type=float, default=0.1)
    train.add_argument("--warmup", type=int, default=20)
    train.add_argument("--schedule-updates", type=int, required=True)
    train.add_argument("--stop-after", type=int)
    train.add_argument("--save-every", type=int, default=100)
    train.add_argument("--log-every", type=int, default=20)
    train.add_argument("--phase", type=int, default=4)
    train.add_argument("--compile", action="store_true")
    train.add_argument("--backend", choices=["default", "math", "flash"], default="default")
    train.add_argument("--sampler", choices=["block", "document"], default="block")
    train.add_argument("--resume", type=Path)
    train.add_argument("--scheduler", choices=["cosine", "wsd"], default="cosine")
    train.add_argument("--branch-from", type=Path, help="Fork a stable WSD checkpoint into a new decay run")
    train.add_argument("--decay-updates", type=int)
    train.add_argument("--minimum-lr-ratio", type=float, default=0.1)
    evaluation = commands.add_parser("evaluate")
    evaluation.add_argument("--checkpoint", type=Path, required=True)
    evaluation.add_argument("--shards", type=Path, required=True)
    evaluation.add_argument("--tokenizer", type=Path, required=True)
    evaluation.add_argument("--split", choices=["dev", "test"], default="dev")
    evaluation.add_argument("--device", default="cuda", choices=["cuda", "cpu"])
    evaluation.add_argument("--dtype", default="bf16", choices=["bf16", "fp32"])
    evaluation.add_argument("--limit", type=int)
    evaluation.add_argument("--generation-limit", type=int)
    evaluation.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    torch.set_num_threads(2)
    if args.command == "build-shards":
        print(json.dumps(build_shards(args.corpus, args.tokenizer, args.output, args.limit)))
    elif args.command == "train":
        if min(args.batch, args.context, args.accumulation, args.schedule_updates, args.save_every, args.log_every) < 1 or not 0 <= args.warmup < args.schedule_updates:
            parser.error("Invalid batch/context/update/warmup counts")
        if args.branch_from and args.resume:
            parser.error("Branch creation and resume are separate operations")
        if args.branch_from and (args.scheduler != "wsd" or not args.decay_updates or not 0 <= args.minimum_lr_ratio < 1):
            parser.error("Decay branch requires --scheduler wsd, positive --decay-updates and a floor in [0,1)")
        if args.decay_updates is not None and not args.branch_from:
            parser.error("--decay-updates is only for branch creation; resume uses frozen branch configuration")
        with gpu_lock(args.device):
            train_command(args)
    else:
        with gpu_lock(args.device):
            state = torch.load(args.checkpoint, map_location="cpu", weights_only=False)
            tok, shard = Tokenizer(args.tokenizer), Shard(args.shards, args.split)
            if sha256(tok.path) != shard.manifest["tokenizer_sha256"] or state["shard_manifest_sha256"] != sha256(args.shards / "manifest.json"):
                raise ValueError("Evaluation artifact contract differs")
            model = JMicroModel(state["model_config"]).to(args.device)
            model.load_state_dict(state["model"])
            report = {"checkpoint_sha256": sha256(args.checkpoint), "tokens_seen": state["tokens"],
                "body": evaluate_body(model, shard, args.device, args.dtype, args.limit),
                "generation": generate_suite(model, tok, args.device, args.dtype, args.split, args.generation_limit, sampling=True)}
            write_json(args.output, report)
            print(json.dumps({"output": str(args.output), "bpb": report["body"]["bpb"]}))
