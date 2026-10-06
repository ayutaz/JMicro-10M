"""Phase 5 measurements: batched held-out scoring, memorization, exact resume."""
from pathlib import Path
from types import SimpleNamespace
import hashlib
import json
import math
import time

import numpy as np
import torch
from torch.nn import functional as F

from jmicro.experiment import ROOT, read_json, sha256
from jmicro.model import JMicroModel
from jmicro.shards import Shard
from jmicro.tokenizer import SUPPRESS_IDS, Tokenizer
from jmicro.training import Trainer, autocast, isolated_evaluation, scoring_windows


def equal_state(a, b):
    if isinstance(a, torch.Tensor):
        return torch.equal(a, b)
    if isinstance(a, np.ndarray):
        return np.array_equal(a, b)
    if isinstance(a, dict):
        return a.keys() == b.keys() and all(equal_state(a[k], b[k]) for k in a)
    if isinstance(a, (tuple, list)):
        return len(a) == len(b) and all(equal_state(x, y) for x, y in zip(a, b))
    return a == b


def score_body(model, shard, device, dtype="bf16", context=1024, batch=8, limit=None):
    """Same body/EOS contract as serial evaluation, padding-aware batched NLL."""
    started = time.perf_counter()
    documents = shard.index[:limit]
    tasks, rows = [], []
    for index, document in enumerate(documents):
        offset, count = document["offset"], document["body_tokens"]
        ids = np.asarray(shard.tokens[offset:offset+count+2], dtype=np.int64)
        rows.append({"doc_id": document["doc_id"], "body_tokens": count,
                     "body_bytes": document["bytes"], "body_nll": 0.0,
                     "body_correct": 0, "scored": 0, "eos_nll": 0.0, "eos_correct": False})
        for start, end, first, last in scoring_windows(count, context, min(512, context-1)):
            inputs = ids[start:end]
            labels = np.full(len(inputs), -100, dtype=np.int64)
            labels[first-start-1:last-start-1] = ids[first:last]
            tasks.append((index, False, inputs, labels))
        start = max(0, len(ids)-context)
        inputs = ids[start:-1]
        labels = np.full(len(inputs), -100, dtype=np.int64)
        labels[-1] = 3
        tasks.append((index, True, inputs, labels))
    tasks.sort(key=lambda t: len(t[2]))
    with isolated_evaluation(model):
        for offset in range(0, len(tasks), batch):
            group = tasks[offset:offset+batch]
            length = max(len(t[2]) for t in group)
            x = torch.zeros((len(group), length), dtype=torch.long, device=device)
            y = torch.full_like(x, -100)
            valid = torch.zeros_like(x, dtype=torch.bool)
            for i, (_, _, inputs, labels) in enumerate(group):
                x[i, :len(inputs)] = torch.as_tensor(inputs.copy(), device=device)
                y[i, :len(inputs)] = torch.as_tensor(labels, device=device)
                valid[i, :len(inputs)] = True
            with autocast(device, dtype):
                logits = model(x, attention_mask=valid).logits
            losses = F.cross_entropy(logits.transpose(1, 2), y, ignore_index=-100, reduction="none").double()
            mask = y.ne(-100)
            stats = torch.stack((losses.sum(-1), (logits.argmax(-1).eq(y) & mask).sum(-1), mask.sum(-1)), -1).cpu().tolist()
            for (index, eos, _, _), (nll, correct, scored) in zip(group, stats):
                if eos:
                    rows[index].update(eos_nll=nll, eos_correct=bool(correct))
                else:
                    rows[index]["body_nll"] += nll
                    rows[index]["body_correct"] += int(correct)
                    rows[index]["scored"] += int(scored)
    if any(row["scored"] != row["body_tokens"] for row in rows):
        raise ValueError("Body targets must be scored exactly once")
    byte_count = sum(r["body_bytes"] for r in rows)
    tokens = sum(r["body_tokens"] for r in rows)
    nll = sum(r["body_nll"] for r in rows)
    if not byte_count or not math.isfinite(nll):
        raise ValueError("Invalid scoring population")
    return {"split": shard.split, "documents": len(rows), "body_bytes": byte_count,
            "body_tokens": tokens, "body_nll": nll, "eos_nll": sum(r["eos_nll"] for r in rows),
            "bpb": nll/(math.log(2)*byte_count), "nll_per_token": nll/tokens,
            "teacher_forced_accuracy": sum(r["body_correct"] for r in rows)/tokens,
            "eos_argmax_accuracy": sum(r["eos_correct"] for r in rows)/len(rows),
            "context": context, "stride": min(512,context-1), "batch": batch,
            "elapsed_seconds": time.perf_counter()-started, "rows": rows}


def continuation_recall(model, tok, shard, device, dtype="bf16"):
    if shard.split != "train":
        raise ValueError("Memorization may only use train")
    outputs, eos_outputs = [], []
    with isolated_evaluation(model):
        for document in shard.index:
            offset, count = document["offset"], document["body_tokens"]
            ids = np.asarray(shard.tokens[offset:offset+count+2], dtype=np.int64)
            prefix = min(32, max(1, count//2))
            length = min(16, count-prefix)
            if length < 1:
                raise ValueError("Memorization document too short")
            current = torch.tensor(ids[:prefix+1].copy()[None], device=device)
            expected = ids[prefix+1:prefix+1+length].tolist()
            cache, generated = None, []
            for _ in range(length):
                with autocast(device, dtype):
                    result = model(current, cache=cache, use_cache=True)
                cache = result.cache
                scores = result.logits[0, -1].clone()
                scores[list(SUPPRESS_IDS)] = -torch.inf
                next_id = int(scores.argmax())
                generated.append(next_id)
                current = torch.tensor([[next_id]], device=device)
            outputs.append({"doc_id": document["doc_id"], "canonical_sha256": document["canonical_sha256"],
                            "prefix_tokens": prefix, "target_tokens": length,
                            "expected_ids": expected, "generated_ids": generated,
                            "exact": expected == generated})
            tail = torch.tensor(ids[max(0,len(ids)-256):-1].copy()[None], device=device)
            with autocast(device, dtype):
                scores = model(tail).logits[0,-1].clone()
            scores[list(SUPPRESS_IDS)] = -torch.inf
            next_id = int(scores.argmax())
            eos_outputs.append({"doc_id":document["doc_id"],"generated_id":next_id,"stop_reason":"stop_id" if next_id==3 else "not_eos"})
    return {"documents": len(outputs), "exact_rate": sum(r["exact"] for r in outputs)/len(outputs), "outputs": outputs,
            "eos_generation_rate":sum(r['generated_id']==3 for r in eos_outputs)/len(eos_outputs),"eos_outputs":eos_outputs}


def common_windows(tok, count=32):
    texts, index, ids = [], [], []
    with (ROOT/"data/phase1/processed/corpus.jsonl").open(encoding="utf-8") as stream:
        for line in stream:
            row = json.loads(line)
            if row["kind"] != "web" or row["split"] != "dev":
                continue
            text = row["text"][:64]
            body = tok.encode(text)
            if not body or len(body)+2 > 1024:
                raise ValueError("Common text window does not fit")
            index.append({"doc_id": row["doc_id"], "offset": len(ids), "body_tokens": len(body), "bytes": len(text.encode())})
            ids.extend([2, *body, 3])
            texts.append({"doc_id": row["doc_id"], "text": text})
            if len(index) == count:
                break
    if len(index) != count:
        raise ValueError("Missing common windows")
    digest = hashlib.sha256(json.dumps(texts, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    return SimpleNamespace(tokens=np.asarray(ids), index=index, split="dev"), digest


def bootstrap_bpb(left, right, seed=42, repetitions=2000):
    if [r["doc_id"] for r in left["rows"]] != [r["doc_id"] for r in right["rows"]]:
        raise ValueError("Comparison documents differ")
    a, b = np.asarray([r["body_nll"] for r in left["rows"]]), np.asarray([r["body_nll"] for r in right["rows"]])
    sizes = np.asarray([r["body_bytes"] for r in left["rows"]])
    if not np.array_equal(sizes, [r["body_bytes"] for r in right["rows"]]):
        raise ValueError("Comparison bytes differ")
    generator, differences = np.random.default_rng(seed), []
    for _ in range(repetitions):
        selected = generator.integers(0, len(a), len(a))
        differences.append(float((a[selected].sum()-b[selected].sum())/(np.log(2)*sizes[selected].sum())))
    return {"direction": "left_bpb_minus_right_bpb", "point": left["bpb"]-right["bpb"],
            "ci95": np.quantile(differences, [0.025, 0.975]).tolist(), "seed": seed,
            "repetitions": repetitions, "unit": "document"}
