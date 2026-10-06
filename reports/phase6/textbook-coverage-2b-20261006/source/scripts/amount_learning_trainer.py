"""Stable exact-teacher learning curve, with separate equal-length decay forks."""
import copy
import json
import math
from pathlib import Path

import numpy as np

from jmicro.experiment import read_json, sha256
from jmicro.learning_curve import MilestoneMixture, LazyDocumentBlocks, curve_lr
import jmicro.packing_study as packing
from resume_curriculum_strategy import BootstrapStrategyTrainer


class CompactIndex:
    """Keep only offsets/lengths/source tags from millions of JSONL records."""
    def __init__(self, view):
        detail = view.manifest["splits"]["train"]
        path = view.directory / "train.index.jsonl"
        assert sha256(path) == detail["index_sha256"]
        count = detail["documents"]
        self.offsets = np.empty(count, dtype=np.int64)
        self.lengths = np.empty(count, dtype=np.int32)
        self.sources = np.empty(count, dtype=np.uint8)
        offset = 0
        with path.open() as stream:
            for i, line in enumerate(stream):
                row = json.loads(line)
                assert i < count and row["offset"] == offset and row["split"] == "train"
                self.offsets[i], self.lengths[i] = offset, row["body_tokens"]
                self.sources[i] = {"web": 0, "story": 1}[row["source"]]
                offset += row["body_tokens"] + 2
        assert i + 1 == count and offset == len(view.tokens)

    def __len__(self):
        return len(self.offsets)

    def __getitem__(self, index):
        return dict(offset=int(self.offsets[index]), body_tokens=int(self.lengths[index]))


class CurveTrainer(BootstrapStrategyTrainer):
    def __init__(self, parent, web, pool, mode, goals, binding, device="cuda"):
        if mode != "shuffle" or goals["web"] != 0:
            raise ValueError("Curve research uses one shuffled nested whole-material pool")
        self.curve_mode = binding["curve_mode"]
        self.curve_total = goals["short"]
        milestones = [n for n in binding["curve_boundaries"] if n < self.curve_total]
        milestones.append(self.curve_total)
        # The pilot bootstrap expects a plain original-Web cursor. A stable
        # checkpoint contains the full two-source wrapper, which must be kept
        # separately for the actual continuation cursor of the decay fork.
        original = parent
        if parent["sampler"].get("kind") == "teacher-learning-curve-v1":
            parent = dict(parent, sampler=copy.deepcopy(parent["sampler"]["web"]))
        # Constructor-local substitution avoids the legacy bootstrap making a
        # second full shuffled corpus. Restore immediately; old runs unchanged.
        old_sampler = packing.ShuffledDocumentBlocks
        try:
            packing.ShuffledDocumentBlocks = LazyDocumentBlocks
            super().__init__(parent, web, pool, mode, goals, binding, device)
        finally:
            packing.ShuffledDocumentBlocks = old_sampler
        self.sampler = MilestoneMixture(web, pool, parent["sampler"], milestones)
        if self.curve_mode == "decay":
            if (binding["optimizer_policy"] != "inherit" or
                    original["sampler"].get("kind") != "teacher-learning-curve-v1"):
                raise ValueError("Decay must fork the actual trained stable full state")
            self.sampler.short.load_state_dict(original["sampler"]["short"])
        elif self.curve_mode != "stable" or original["update"] != 0:
            raise ValueError("Stable curve must start from the frozen zero-update parent")
        self.spec["curve_schedule"] = dict(mode=self.curve_mode, teachers=self.curve_total,
            boundaries=tuple(milestones), minimum_lr_ratio=.1, no_reheat=True)
        self.lineage.update(kind="amount-learning-curve", curve_mode=self.curve_mode,
            actual_parent_sampler=original["sampler"], parent_supervised_tokens=original["supervised_tokens"])
        self._set_token_lr()

    def _set_token_lr(self):
        consumed = sum(self.sampler.source_teachers.values())
        lr = curve_lr(consumed, self.pilot_binding["peak_lr"], self.curve_mode, self.curve_total)
        if self.curve_mode == "stable":
            warmup = self.pilot_binding["warmup_updates"]
            lr *= min(1., (self.update + 1) / max(1, warmup))
        for group in self.optimizer.param_groups:
            group["lr"] = lr
        self.scheduler._last_lr = [lr] * len(self.optimizer.param_groups)
        return lr
