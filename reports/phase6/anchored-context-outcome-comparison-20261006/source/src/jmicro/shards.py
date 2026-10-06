"""Checksummed uint16 document streams and resumable, local-RNG block sampling."""
from pathlib import Path
import hashlib
import json

import numpy as np
import torch

from jmicro.evaluation import canonicalize_text
from jmicro.experiment import read_json, sha256, write_json
from jmicro.tokenizer import Tokenizer


def build_shards(corpus: Path, tokenizer: Path, destination: Path, limit=None):
    if destination.exists():
        raise ValueError(f"Shard destination already exists: {destination}")
    destination.mkdir(parents=True)
    tok = Tokenizer(tokenizer)
    if tok.vocab_size > 65536:
        raise ValueError("uint16 vocabulary overflow")
    indexes = {split: [] for split in ("train", "dev", "test")}
    offsets = dict.fromkeys(indexes, 0)
    streams = {s: (destination / f"{s}.bin").open("wb") for s in indexes}
    try:
        with corpus.open(encoding="utf-8") as stream:
            for line in stream:
                record = json.loads(line)
                if record["kind"] != "web":
                    continue  # Dialogue/SA data require a separate, explicit mixture.
                split = record["split"]
                if split not in indexes:
                    raise ValueError("Unknown split")
                if limit is not None and len(indexes[split]) >= limit:
                    continue
                text = canonicalize_text(record["text"])
                body = tok.encode(text)
                if not body:
                    continue
                digest = hashlib.sha256(text.encode()).hexdigest()
                if digest != record["canonical_sha256"]:
                    raise ValueError(f"Canonical hash differs: {record['doc_id']}")
                ids = np.asarray([2, *body, 3], dtype="<u2")
                streams[split].write(ids.tobytes())
                indexes[split].append({"doc_id": record["doc_id"], "split": split,
                    "kind": record["kind"], "bucket": record["bucket"],
                    "canonical_sha256": digest, "offset": offsets[split],
                    "body_tokens": len(body), "bytes": len(text.encode())})
                offsets[split] += len(ids)
    finally:
        for stream in streams.values():
            stream.close()
    manifest = {"version": 1, "dtype": "<u2", "kind": "web", "corpus_sha256": sha256(corpus),
        "tokenizer_sha256": sha256(tokenizer), "vocab_size": tok.vocab_size,
        "packing": "BOS/body/EOS; causal attention across documents; BOS targets masked",
        "limit_per_split": limit, "splits": {}}
    byte_lengths = [0 if i < 8 else len(tok.decode_bytes([i])) for i in range(tok.vocab_size)]
    write_json(destination / "token_bytes.json", byte_lengths)
    manifest["token_bytes_sha256"] = sha256(destination / "token_bytes.json")
    for split, rows in indexes.items():
        write_json(destination / f"{split}.index.json", rows)
        manifest["splits"][split] = {"tokens": offsets[split], "documents": len(rows),
            "body_bytes": sum(r["bytes"] for r in rows),
            "stream_sha256": sha256(destination / f"{split}.bin"),
            "index_sha256": sha256(destination / f"{split}.index.json")}
    write_json(destination / "manifest.json", manifest)
    return manifest


class Shard:
    def __init__(self, directory: Path, split="train"):
        self.directory, self.split = directory, split
        self.manifest = read_json(directory / "manifest.json")
        details = self.manifest["splits"][split]
        for name, digest in ((f"{split}.bin", details["stream_sha256"]),
                             (f"{split}.index.json", details["index_sha256"]),
                             ("token_bytes.json", self.manifest["token_bytes_sha256"])):
            if sha256(directory / name) != digest:
                raise ValueError(f"Shard checksum differs: {name}")
        if (directory / f"{split}.bin").stat().st_size != details["tokens"] * 2:
            raise ValueError("Truncated uint16 stream")
        if details["tokens"] == 0:
            raise ValueError("Empty shard split")
        self.tokens = np.memmap(directory / f"{split}.bin", dtype="<u2", mode="r")
        self.index = read_json(directory / f"{split}.index.json")
        if any(r["split"] != split for r in self.index):
            raise ValueError("Split contamination")
        self.byte_lengths = np.asarray(read_json(directory / "token_bytes.json"))


class BlockSampler:
    def __init__(self, shard: Shard, context: int, seed: int):
        if context < 2 or len(shard.tokens) <= context:
            raise ValueError("Shard must contain at least one context+1 sample")
        self.shard, self.context, self.seed = shard, context, seed
        self.blocks = (len(shard.tokens) - 1) // context
        self.epoch, self.position = 0, 0
        self._shuffle()

    def _shuffle(self):
        self.order = np.random.default_rng(np.random.SeedSequence([self.seed, self.epoch])).permutation(self.blocks)

    def state_dict(self):
        return {"seed": self.seed, "epoch": self.epoch, "position": self.position,
                "context": self.context, "blocks": self.blocks}

    def load_state_dict(self, state):
        if any(state[k] != self.state_dict()[k] for k in ("seed", "context", "blocks")):
            raise ValueError("Sampler configuration differs")
        if state["epoch"] < 0 or not 0 <= state["position"] <= self.blocks:
            raise ValueError("Invalid sampler cursor")
        self.epoch, self.position = state["epoch"], state["position"]
        self._shuffle()

    def batch(self, size):
        samples = []
        for _ in range(size):
            if self.position == self.blocks:
                self.epoch += 1
                self.position = 0
                self._shuffle()
            offset = int(self.order[self.position]) * self.context
            samples.append(self.shard.tokens[offset:offset + self.context + 1])
            self.position += 1
        ids = np.stack(samples).astype(np.int64)
        targets = ids[:, 1:].copy()
        targets[targets == 2] = -100
        body_bytes = int(self.shard.byte_lengths[ids[:, 1:]].sum())
        return torch.from_numpy(ids[:, :-1].copy()), torch.from_numpy(targets), body_bytes
