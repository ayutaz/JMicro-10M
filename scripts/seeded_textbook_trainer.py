"""Independent initialization/training RNG/material order, historical code intact.

These are building blocks for a gated replicate runner. Creating random zero
weights and CPU protocol tests is not independent GPU quality confirmation.
"""
import copy
from pathlib import Path
import torch
from jmicro.experiment import sha256
from jmicro.shards import BlockSampler
from jmicro.training import Trainer
from jmicro.learning_curve import LazyDocumentBlocks
from textbook_quantity_trainer import ThreeSourceTrainer
from run_eos_short_pilot import equal_state


def make_zero_parent(reference, web, path, seed=43, device="cpu"):
    if type(seed) is not int or seed < 0 or seed == reference["spec"]["seed"]:
        raise ValueError("Replicate requires a distinct nonnegative integer training seed")
    if any(reference[k] != 0 for k in ("update", "tokens", "supervised_tokens", "body_bytes")) or reference["optimizer"]["state"]:
        raise ValueError("Replicate initialization requires the original zero-update parent")
    path = Path(path)
    if path.exists():
        raise ValueError("Existing replicate zero parent must be verified/reused, never overwritten")
    spec = dict(reference["spec"], seed=seed)
    trainer = Trainer(reference["model_config"], web, spec, device=device)
    assert not equal_state(trainer.model.state_dict(), reference["model"])
    # Historical bootstrap expects seed42 for its unused Web cursor. This
    # source has zero teachers in the replicate; actual material order uses
    # the independent seed below. No learned cursor or RNG is rewritten.
    trainer.sampler = BlockSampler(web, spec["context"], 42)
    trainer.lineage = dict(kind="independent-seed-zero", parent_update=0, parent_tokens=0, initialization_seed=seed,
        training_RNG_seed=seed, material_shuffle_seed=seed, unused_Web_sampler_seed=42,
        reference_seed=reference["spec"]["seed"], source_sha256=sha256(Path(__file__)),
        limitation="Zero optimizer updates; not GPU learning or model-quality evidence")
    trainer.save(path)
    return torch.load(path, map_location="cpu", weights_only=False)


class SeededThreeSourceTrainer(ThreeSourceTrainer):
    """Use existing exact-teacher learning/decay with an explicit material seed."""
    def __init__(self, parent, web, pool, mode, goals, binding, device="cuda"):
        seed = binding["training_seed"]
        if type(seed) is not int or seed < 0 or seed != parent["spec"]["seed"] or seed == 42:
            raise ValueError("Explicit independent training seed must match the actual parent")
        if goals["web"] != 0:
            raise ValueError("Historical Web bootstrap cursor is unused in this replicate")
        if binding["curve_mode"] == "stable":
            initial = parent.get("lineage") or {}
            if (initial.get("kind") != "independent-seed-zero" or parent["update"] != 0
                    or initial.get("initialization_seed") != seed
                    or initial.get("source_sha256") != sha256(Path(__file__))):
                raise ValueError("Stable replicate must start from its bound independent zero parent")
        elif binding["curve_mode"] == "decay":
            provenance = parent["lineage"].get("independent_training_seed", {})
            if (provenance.get("seed") != seed or parent["sampler"]["short"]["seed"] != seed
                    or provenance.get("source_sha256") != sha256(Path(__file__))
                    or parent["spec"]["curve_schedule"]["mode"] != "stable"
                    or parent["sampler"]["source_teachers"]["short"] != parent["spec"]["curve_schedule"]["teachers"]):
                raise ValueError("Decay must inherit this replicate's actual stable cursor")
        else:
            raise ValueError("Independent replicate supports stable or actual stable-fork decay")
        # All historical constructors validate seed42 dummy samplers. Only
        # constructor-local metadata is adapted, before any batch or update.
        # Real model/Adam/RNG are inherited unmodified; actual parent metadata
        # and independent material cursor are restored before learning.
        bootstrap = dict(parent, spec=dict(parent["spec"], seed=42), sampler=copy.deepcopy(parent["sampler"]))
        if bootstrap["sampler"].get("kind") == "teacher-learning-curve-v1":
            bootstrap["sampler"]["short"]["seed"] = 42
        assert (bootstrap["sampler"].get("web", bootstrap["sampler"]))["seed"] == 42
        super().__init__(bootstrap, web, pool, mode, goals, binding, device)
        self.spec["seed"] = seed
        self.sampler.short = LazyDocumentBlocks(pool, self.spec["context"], seed)
        if self.curve_mode == "decay":
            self.sampler.short.load_state_dict(parent["sampler"]["short"])
        self.lineage["parent_spec"] = copy.deepcopy(parent["spec"])
        self.lineage["actual_parent_sampler"] = copy.deepcopy(parent["sampler"])
        self.lineage["independent_training_seed"] = dict(seed=seed, initialization_seed=seed,
            training_RNG_seed=seed, material_shuffle_seed=seed, unused_Web_sampler_seed=42,
            source_sha256=sha256(Path(__file__)),
            policy="Original recipe; distinct fresh weights/training RNG and material permutation, inherited actual stable cursor for decay")
        self._set_token_lr()

    def load(self, path):
        state = torch.load(path, map_location="cpu", weights_only=False)
        provenance = state.get("lineage", {}).get("independent_training_seed", {})
        if (provenance.get("seed") != self.pilot_binding["training_seed"]
                or provenance.get("source_sha256") != sha256(Path(__file__))):
            raise ValueError("Independent replicate resume seed/source provenance differs")
        super().load(path)
