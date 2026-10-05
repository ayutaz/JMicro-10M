"""Explicit stable teacher-budget extension, retaining the original trajectory."""
import copy
from pathlib import Path

import torch

from amount_learning_trainer import CurveTrainer
from jmicro.experiment import sha256


class ExtendedCurveTrainer(CurveTrainer):
    """Construct from the original zero parent, then explicitly inherit a milestone.

    Ordinary load still requires identical budgets. Only load_extension may
    append future milestones; no weights, Adam, RNG or counters are reset.
    """
    def load_extension(self, path):
        path = Path(path)
        ref = self.pilot_binding["stable_extension"]
        if (self.update != 0 or path.resolve() != Path(ref["path"]).resolve()
                or sha256(path) != ref["sha256"]
                or ref["source_sha256"] != sha256(Path(__file__))):
            raise ValueError("Stable extension parent/source checksum differs or trainer is not fresh")
        parent = torch.load(path, map_location="cpu", weights_only=False)
        old, new = parent["spec"], self.spec
        old_curve, new_curve = old["curve_schedule"], new["curve_schedule"]
        old_boundaries, new_boundaries = tuple(old_curve["boundaries"]), tuple(new_curve["boundaries"])
        mutable = {"curve_schedule", "teacher_schedule"}
        binding_mutable = {"config_sha256", "curve_boundaries", "stable_extension"}
        if (old_curve["mode"] != new_curve["mode"] or new_curve["mode"] != "stable"
                or parent["update"] < old["warmup"] or old_curve["teachers"] >= self.curve_total
                or new_boundaries[:len(old_boundaries)] != old_boundaries
                or {k:v for k,v in old_curve.items() if k not in ("teachers","boundaries")}
                   != {k:v for k,v in new_curve.items() if k not in ("teachers","boundaries")}
                or {k:v for k,v in old.items() if k not in mutable}
                   != {k:v for k,v in new.items() if k not in mutable}
                or {k:v for k,v in old["teacher_schedule"].items() if k != "goals"}
                   != {k:v for k,v in new["teacher_schedule"].items() if k != "goals"}
                or {k:v for k,v in parent["pilot_binding"].items() if k not in binding_mutable}
                   != {k:v for k,v in self.pilot_binding.items() if k not in binding_mutable}
                or parent["sampler"]["source_teachers"] != dict(web=0,short=old_curve["teachers"])
                or tuple(parent["sampler"]["boundaries"]) != old_boundaries
                or parent["sampler"]["goals"] != dict(web=0,short=old_curve["teachers"])):
            raise ValueError("Extension requires completed stable training and only appended teacher milestones")
        # Reuse the established source/model/data/full-state validation while
        # temporarily presenting its exact old budget to the loader. No saved
        # checkpoint or historical binding is rewritten.
        new_binding = self.pilot_binding
        new_goals, new_total = self.sampler.goals, self.curve_total
        self.spec, self.pilot_binding = old, parent["pilot_binding"]
        self.sampler.boundaries, self.sampler.goals = old_boundaries, parent["sampler"]["goals"]
        self.curve_total = old_curve["teachers"]
        try:
            super().load(path)
        finally:
            self.spec, self.pilot_binding = new, new_binding
            self.sampler.boundaries, self.sampler.goals = new_boundaries, new_goals
            self.curve_total = new_total
        self.lineage = copy.deepcopy(self.lineage)
        self.lineage["stable_extension"] = dict(parent_checkpoint=str(path.resolve()),
            parent_sha256=ref["sha256"],parent_update=parent["update"],parent_tokens=parent["tokens"],
            parent_supervised_tokens=parent["supervised_tokens"],parent_binding=parent["pilot_binding"],
            parent_lineage=parent["lineage"],old_boundaries=old_boundaries,new_boundaries=new_boundaries,
            old_teacher_budget=old_curve["teachers"],new_teacher_budget=new_total,
            extension_implementation_sha256=sha256(Path(__file__)),
            policy="Constant stable LR; no repeated warmup, optimizer/RNG/cursor/counter reset or decay-state adoption")
        self._set_token_lr()

    def load(self, path):
        state = torch.load(path, map_location="cpu", weights_only=False)
        extension = state.get("lineage",{}).get("stable_extension",{})
        if (extension.get("extension_implementation_sha256") != sha256(Path(__file__))
                or extension.get("parent_sha256") != self.pilot_binding["stable_extension"]["sha256"]):
            raise ValueError("Stable extension resume provenance differs")
        super().load(path)
