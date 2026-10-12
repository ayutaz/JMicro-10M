"""Versioned Japanese Base diagnostics, independent of the frozen v1 runner."""
from collections import Counter, defaultdict
import math
import re

import numpy as np
import torch
import torch.nn.functional as F

from jmicro.evaluation import canonicalize_text
from jmicro.tokenizer import SUPPRESS_IDS


def encode_request(tokenizer, context, continuation, maximum=1024):
    context, continuation = canonicalize_text(context), canonicalize_text(continuation)
    prefix = tokenizer.encode(context)
    joint = tokenizer.encode(context + continuation)
    if joint[:len(prefix)] != prefix:
        raise ValueError("Unstable token boundary: terminate context with protected newline")
    target = joint[len(prefix):]
    if not target:
        raise ValueError("Empty continuation")
    if tokenizer.decode_bytes(joint) != (context + continuation).encode("utf-8"):
        raise ValueError("Codec does not preserve the canonical request")
    ids = [2, *joint]
    if len(ids) - 1 > maximum:
        raise ValueError("Context overflow: never silently truncate a target")
    return {"ids": ids, "context_tokens": len(prefix) + 1, "target_ids": target,
            "target_bytes": len(continuation.encode("utf-8"))}


class NativeLikelihood:
    """BOS-conditioned native scorer; no Chat roles, EOS, or decoding suppression.

    Exact stable boundaries are required. Corpus rolling likelihood uses BOS,
    unlike harness's EOT convention; this class is not registered as harness LM.
    """
    def __init__(self, model, tokenizer, device="cuda", dtype="bf16", batch=16):
        self.model, self.tokenizer, self.device = model, tokenizer, device
        self.dtype, self.batch = dtype, batch
        self.maximum = model.config["max_position_embeddings"]
        self.forward_tokens = 0

    @torch.inference_mode()
    def score_encoded(self, encoded):
        results = []
        for start in range(0, len(encoded), self.batch):
            rows = encoded[start:start + self.batch]
            width = max(len(row["ids"]) - 1 for row in rows)
            inputs = torch.zeros((len(rows), width), dtype=torch.long, device=self.device)
            labels = torch.zeros_like(inputs)
            valid = torch.zeros_like(inputs, dtype=torch.bool)
            targets = torch.zeros_like(valid)
            for index, row in enumerate(rows):
                count = len(row["ids"]) - 1
                inputs[index, :count] = torch.tensor(row["ids"][:-1], device=self.device)
                labels[index, :count] = torch.tensor(row["ids"][1:], device=self.device)
                valid[index, :count] = True
                targets[index, row["context_tokens"] - 1:count] = True
                self.forward_tokens += count
            with torch.autocast(device_type="cuda", dtype=torch.bfloat16,
                                enabled=self.device.startswith("cuda") and self.dtype == "bf16"):
                logits = self.model(inputs, attention_mask=valid).logits
            losses = F.cross_entropy(logits.float().transpose(1, 2), labels, reduction="none")
            greedy = logits.argmax(-1).eq(labels)
            for index, row in enumerate(rows):
                selected = losses[index][targets[index]].double().cpu().tolist()
                if len(selected) != len(row["target_ids"]) or not all(math.isfinite(nll) for nll in selected):
                    raise ValueError("Nonfinite loss or target-mask mismatch")
                results.append({"log_likelihood": -sum(selected), "target_tokens": len(selected),
                                "target_bytes": row["target_bytes"], "target_ids": row["target_ids"],
                                "token_nll": selected, "is_greedy": bool(greedy[index][targets[index]].all())})
        return results

    def score(self, pairs):
        return self.score_encoded([encode_request(self.tokenizer, a, b, self.maximum) for a, b in pairs])

    def loglikelihood(self, requests):
        pairs = [request.args if hasattr(request, "args") else request for request in requests]
        return [(row["log_likelihood"], row["is_greedy"]) for row in self.score(pairs)]

    def loglikelihood_rolling(self, requests):
        results = []
        for request in requests:
            text = (request.args if hasattr(request, "args") else request)[0]
            ids = [2, *self.tokenizer.encode(text)]
            windows = []
            # Each body token scored exactly once; 512-token lookback thereafter.
            for target_start in range(1, len(ids), 512):
                left = max(0, target_start - 512)
                right = min(len(ids), target_start + 512)
                windows.append({"ids": ids[left:right], "context_tokens": target_start-left,
                                "target_ids": ids[target_start:right], "target_bytes": 0})
            results.append((sum(row["log_likelihood"] for row in self.score_encoded(windows)),))
        return results

    @torch.inference_mode()
    def generate(self, prefix, max_new=128):
        prompt = [2, *self.tokenizer.encode(prefix)]
        if len(prompt) + max_new > self.maximum:
            raise ValueError("Generation context overflow")
        current = torch.tensor([prompt], device=self.device)
        cache, generated, reason = None, [], "max_new_tokens"
        for _ in range(max_new):
            with torch.autocast(device_type="cuda", dtype=torch.bfloat16,
                                enabled=self.device.startswith("cuda") and self.dtype == "bf16"):
                output = self.model(current, cache=cache, use_cache=True)
            cache = output.cache
            logits = output.logits[0, -1].clone()
            logits[list(SUPPRESS_IDS)] = -torch.inf
            token = int(logits.argmax())
            generated.append(token)
            if token == 3:
                reason = "stop_id"
                break
            current = torch.tensor([[token]], device=self.device)
        raw = self.tokenizer.decode_bytes(generated)
        try:
            text, valid = raw.decode("utf-8"), True
        except UnicodeDecodeError:
            text, valid = raw.decode("utf-8", errors="replace"), False
        return {"prefix": prefix, "text": text, "generated_ids": generated,
                "valid_utf8": valid, "stop_reason": reason, "max_new_tokens": max_new}


def tied_prediction(scores, label):
    best = max(scores)
    winners = [i for i, value in enumerate(scores) if value == best]
    return {"prediction": winners[0], "credit": 1 / len(winners) if label in winners else 0.0,
            "ties": len(winners)}


def clustered_ci(rows, key="credit", repetitions=2000, seed=42):
    groups = defaultdict(list)
    for row in rows:
        groups[row.get("family", row["id"])].append(float(row[key]))
    sums = np.array([sum(group) for group in groups.values()])
    counts = np.array([len(group) for group in groups.values()])
    if not len(sums):
        return {"point": None, "ci95": None, "units": 0}
    rng = np.random.default_rng(seed)
    draws = rng.integers(0, len(sums), (repetitions, len(sums)))
    statistics = sums[draws].sum(1) / counts[draws].sum(1)
    return {"point": float(sums.sum()/counts.sum()), "ci95": np.quantile(statistics, [.025, .975]).tolist(),
            "units": len(sums), "examples": int(counts.sum()), "unit": "family/prompt",
            "seed": seed, "repetitions": repetitions,
            "note": "cluster resampling; example-weighted ratio; all-identical outcomes yield degenerate bootstrap CI"}


def classification_summary(rows, classes):
    matrix = np.zeros((classes, classes), dtype=np.int64)
    for row in rows:
        matrix[row["label"], row["prediction"]] += 1
    tp = matrix.diagonal()
    denominators = matrix.sum(0) + matrix.sum(1)
    f1 = np.divide(2*tp, denominators, out=np.zeros(classes, dtype=float), where=denominators != 0)
    n, correct = int(matrix.sum()), int(tp.sum())
    actual, predicted = matrix.sum(1), matrix.sum(0)
    denominator = math.sqrt(float((n*n-(actual*actual).sum()) * (n*n-(predicted*predicted).sum())))
    return {"count": n, "hard_accuracy": correct/n if n else None,
            "macro_f1": float(f1.mean()), "mcc": float((correct*n-(actual*predicted).sum())/denominator) if denominator else 0.0,
            "confusion_matrix": matrix.tolist(), "confusion_ties": "first maximum; accuracy CI uses fractional credit"}


def repetition_metrics(row):
    text, ids = row["text"], row["generated_ids"]
    def fraction(sequence, n):
        grams = [tuple(sequence[i:i+n]) for i in range(max(0, len(sequence)-n+1))]
        return (len(grams)-len(set(grams)))/len(grams) if grams else 0.0
    sentences = [part.strip() for part in re.split(r"[。！？\n]+", text) if len(part.strip()) >= 4]
    match = re.search(r"(.{2,}?)\1\1", text, re.DOTALL)
    return {"characters": len(text), "tokens": len(ids), "char_4gram_repeat": fraction(text, 4),
            "token_4gram_repeat": fraction(ids, 4), "same_sentence_reappears": len(sentences) != len(set(sentences)),
            "first_adjacent_triple_repeat_char": match.start() if match else None,
            "role_ids_4_5_6": any(token in (4, 5, 6) for token in ids), "base_eot_id_7": 7 in ids,
            "raw_utf8_failure": not row["valid_utf8"],
            "literal_replacement_character": "\ufffd" in text if row["valid_utf8"] else None,
            "natural_eos": row["stop_reason"] == "stop_id", "empty": not text.strip()}


def answer_metrics(prediction, answers):
    """Explicit Japanese character F1, NOT official morphological-token F1."""
    def normalize(text):
        return re.sub(r"[\s。、！？,.!?]", "", text.lower())
    prediction = normalize(prediction)
    best = 0.0
    for answer in answers:
        answer = normalize(answer)
        overlap = sum((Counter(prediction) & Counter(answer)).values())
        f1 = 2*overlap/(len(prediction)+len(answer)) if prediction or answer else 1.0
        best = max(best, f1)
    return {"normalized_em": float(any(prediction == normalize(answer) for answer in answers)),
            "character_f1": best}
