"""Exact learning checkpoints and common decay budgets, without LR reheating."""
import math
import numpy as np
import torch

from jmicro.packing_study import TeacherBudgetMixture
from jmicro.shards import BlockSampler


class LazyDocumentBlocks(BlockSampler):
    """Exactly the old document/block permutations, without a full epoch copy."""
    def __init__(self, shard, context, seed):
        index = shard.index
        if hasattr(index, "offsets"):
            self.offsets, self.lengths = index.offsets, index.lengths.astype(np.int64) + 2
            self.tags = index.sources
        else:
            self.offsets = np.fromiter((r["offset"] for r in index), dtype=np.int64)
            self.lengths = np.fromiter((r["body_tokens"]+2 for r in index), dtype=np.int64)
            self.tags = np.fromiter((int(r.get("source") == "story") for r in index), dtype=np.uint8)
        assert self.lengths.sum() == len(shard.tokens)
        super().__init__(shard, context, seed)

    def _shuffle(self):
        self.documents = np.random.default_rng(np.random.SeedSequence([self.seed,self.epoch,1])).permutation(len(self.offsets))
        self.ends = np.cumsum(self.lengths[self.documents])
        super()._shuffle()

    def state_dict(self):
        return dict(super().state_dict(), mode="lazy-shuffle-whole-documents-v1")

    def load_state_dict(self, state):
        if state.get("mode") != "lazy-shuffle-whole-documents-v1":
            raise ValueError("Sampler differs")
        super().load_state_dict(state)

    def batch(self, size):
        ids = np.empty((size,self.context+1), dtype=np.int64)
        tags = np.empty((size,self.context), dtype=np.uint8)
        for row in range(size):
            if self.position == self.blocks:
                self.epoch += 1; self.position = 0; self._shuffle()
            positions = int(self.order[self.position])*self.context + np.arange(self.context+1)
            slots = np.searchsorted(self.ends, positions, side="right")
            docs = self.documents[slots]
            starts = self.ends[slots] - self.lengths[docs]
            ids[row] = self.shard.tokens[self.offsets[docs]+positions-starts]
            tags[row] = self.tags[docs[1:]]
            self.position += 1
        targets = ids[:,1:].copy(); targets[targets == 2] = -100
        self.last_target_tags = tags
        body_bytes = int(self.shard.byte_lengths[ids[:,1:]].sum())
        return torch.from_numpy(ids[:,:-1].copy()), torch.from_numpy(targets), body_bytes


def curve_lr(consumed, peak, mode="stable", decay_teachers=None):
    if type(consumed) is not int or consumed < 0 or not math.isfinite(peak) or peak <= 0:
        raise ValueError("Invalid learning curve LR arguments")
    if mode == "stable":
        return peak
    if mode != "decay" or type(decay_teachers) is not int or decay_teachers <= 0:
        raise ValueError("Decay branch needs a positive teacher budget")
    progress = min(1., consumed / decay_teachers)
    return peak * (.1 + .9 * (1 + math.cos(math.pi * progress)) / 2)


class MilestoneMixture(TeacherBudgetMixture):
    """The single nested pool contains both genres; hit every teacher boundary.

    A boundary masks only excess targets in its last completed update. The
    sampler retains the actual subsequent block cursor; it never replays the
    masked batch suffix as if it were a separately consumed update.
    """
    def __init__(self, web, pool, parent_web_state, boundaries, mode="shuffle"):
        if (not boundaries or any(type(n) is not int or n <= 0 for n in boundaries) or
                list(boundaries) != sorted(set(boundaries))):
            raise ValueError("Teacher milestones must be strictly increasing")
        self.boundaries = tuple(boundaries)
        self.mode, self.goals = mode, dict(web=0, short=boundaries[-1])
        self.web = BlockSampler(web,1024,42); self.web.load_state_dict(parent_web_state)
        self.short = LazyDocumentBlocks(pool,1024,42)
        self.position = 0
        for name in ("source_tokens", "source_physical_tokens", "source_teachers", "source_eos"):
            setattr(self,name,dict(web=0,short=0))
        self.genre_teachers, self.genre_eos = dict(web=0,story=0), dict(web=0,story=0)
        self.last_padding, self.last_source = 0, None

    def state_dict(self):
        state = super().state_dict()
        state.update(kind="teacher-learning-curve-v1", boundaries=self.boundaries,
                     genre_teachers=self.genre_teachers.copy(), genre_eos=self.genre_eos.copy())
        return state

    def load_state_dict(self, state):
        if state["kind"] != "teacher-learning-curve-v1" or tuple(state["boundaries"]) != self.boundaries:
            raise ValueError("Learning curve boundaries differ")
        old = dict(state, kind="exact-teacher-packing-study-v1")
        super().load_state_dict(old)
        self.genre_teachers, self.genre_eos = dict(state["genre_teachers"]), dict(state["genre_eos"])
        if sum(self.genre_teachers.values()) != self.source_teachers["short"]:
            raise ValueError("Genre teacher accounting differs")

    def batch(self, size):
        consumed = self.source_teachers["short"]
        next_boundary = next((n for n in self.boundaries if n > consumed), None)
        if next_boundary is None:
            raise ValueError("Teacher budget exhausted")
        frozen_goals = self.goals
        self.goals = dict(web=0, short=next_boundary)
        try:
            result = super().batch(size)
            y = result[1].numpy()
            for tag, genre in enumerate(("web","story")):
                selected = self.short.last_target_tags == tag
                self.genre_teachers[genre] += int(np.count_nonzero(selected & (y != -100)))
                self.genre_eos[genre] += int(np.count_nonzero(selected & (y == 3)))
            assert sum(self.genre_teachers.values()) == self.source_teachers["short"]
            return result
        finally:
            self.goals = frozen_goals
