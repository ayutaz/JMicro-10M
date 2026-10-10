"""Resumable local SFT counters and complete Assistant-body/EOT targets."""
import math
from pathlib import Path
from types import SimpleNamespace

import numpy as np
import torch

from jmicro.assistant_sampler import AssistantSampler
from jmicro.experiment import ROOT, sha256
from jmicro.training import Trainer, implementation_hashes


class AssistantBudgetSampler(AssistantSampler):
    """Finish the last Assistant window instead of cutting its EOT target.

    Budgets count non-PAD serialized windows, including each final EOT. The
    final whole window can exceed the requested budget by at most context+1.
    Empty rows retain the frozen physical batch shape, with no labels.
    """
    def __init__(self,records,tokenizer,context,seed,series_budget):
        if type(series_budget) is not int or series_budget <= 0:
            raise ValueError("Positive series-token budget required")
        self.series_budget = series_budget
        super().__init__(records,tokenizer,context,seed)

    def state_dict(self):
        return dict(super().state_dict(),series_budget=self.series_budget)

    def load_state_dict(self,state):
        if state.get("series_budget") != self.series_budget:
            raise ValueError("Frozen SFT series budget differs")
        if state["series_tokens"] >= self.series_budget+self.context+1:
            raise ValueError("SFT budget exceeded beyond one complete window")
        super().load_state_dict(state)

    def batch(self,size):
        if self.series_tokens >= self.series_budget:
            raise ValueError("SFT series budget exhausted")
        if type(size) is not int or size <= 0:
            raise ValueError("Positive batch size required")
        x = torch.zeros((size,self.context),dtype=torch.long)
        y = torch.full_like(x,-100)
        byte_count = used = 0
        for row in range(size):
            if self.series_tokens >= self.series_budget: break
            a,b,c = super().batch(1)
            x[row],y[row] = a[0],b[0]
            byte_count += c;used += 1
        self.physical_tokens += (size-used)*self.context
        return x,y,byte_count


class AssistantTrainer(Trainer):
    """Base/mid-trained weights + fresh SFT Adam; preserve both parent lineages.

    Does not certify Base quality or start a GPU job. A future run contract must
    validate the adopted Base, data split, budget and measured hardware batch.
    """
    def __init__(self,parent,parent_ref,records,tokenizer,dataset_directory,spec,series_budget,device="cpu"):
        if parent["implementation_sha256"] != implementation_hashes():
            raise ValueError("Base implementation differs")
        if (spec.get("sampler") != "document" or spec.get("training_fast_path") or
                spec["accumulation"] != 1):
            raise ValueError("SFT requires masked document attention, no unpadded fast path and accumulation1")
        sampler = AssistantBudgetSampler(records,tokenizer,spec["context"],spec["seed"],series_budget)
        # Trainer's constructor only needs a train/vocabulary/source binding;
        # its dummy sampler never enters a forward pass and is replaced below.
        directory = Path(dataset_directory)
        source = SimpleNamespace(directory=directory,split="train",manifest=dict(vocab_size=tokenizer.vocab_size),
            tokens=np.zeros(spec["context"]+1,dtype="<u2"),
            index=[dict(offset=0,body_tokens=spec["context"]-1)],byte_lengths=sampler.byte_lengths)
        assert parent_ref["sha256"] == sha256(Path(parent_ref["path"]))
        actual_spec = dict(spec,assistant_training=dict(series_budget=series_budget,data_binding=sampler.binding,
            base_checkpoint_sha256=parent_ref["sha256"],minimum_lr_ratio=.1,stable_fraction=.9,
            supervision="Assistant body plus EOT; causal shift once; complete final window",
            assistant_sampler_sha256=sha256(ROOT/"src/jmicro/assistant_sampler.py"),
            trainer_sha256=sha256(Path(__file__))))
        super().__init__(parent["model_config"],source,actual_spec,device)
        self.model.load_state_dict(parent["model"],strict=True)
        self.sampler = sampler
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:1.)
        inherited = parent.get("lineage") or {}
        mid_trained = inherited.get("kind") == "dialogue-midtraining-fresh-optimizer"
        root_ref = inherited["base_checkpoint"] if mid_trained else parent_ref
        self.lineage = dict(kind="assistant-sft-fresh-optimizer",parent_update=0,parent_tokens=0,
            local_counter_policy="SFT counters start at zero; Base exposure is recorded separately",
            base_checkpoint=dict(parent_ref),base_update=parent["update"],base_tokens=parent["tokens"],
            base_supervised_tokens=parent["supervised_tokens"],base_token_digest=parent["token_digest"],
            optimizer_policy="fresh",RNG_policy="new frozen SFT seed",
            route="midtraining-sft" if mid_trained else "direct-sft",root_Base_checkpoint=dict(root_ref),
            model_parent_lineage=inherited if mid_trained else None)
        assert not self.optimizer.state and self.update == self.tokens == self.supervised_tokens == 0
        self._set_sft_lr()

    def _set_sft_lr(self):
        progress = max(0.,min(1.,(self.sampler.series_tokens/self.sampler.series_budget-.9)/.1))
        lr = self.spec["lr"]*(.1+.9*(1+math.cos(math.pi*progress))/2)
        lr *= min(1.,(self.update+1)/max(1,self.spec["warmup"]))
        for group in self.optimizer.param_groups: group["lr"] = lr
        self.scheduler._last_lr = [lr]*len(self.optimizer.param_groups)
        return lr

    def step(self):
        self._set_sft_lr()
        before_input,before_physical = self.sampler.input_tokens,self.sampler.physical_tokens
        row = super().step()
        self.tokens -= (self.sampler.physical_tokens-before_physical)-(self.sampler.input_tokens-before_input)
        assert self.tokens == self.sampler.input_tokens and self.supervised_tokens == self.sampler.teacher_tokens
        row.update(tokens_seen=self.tokens,series_tokens=self.sampler.series_tokens,
            assistant_teacher_tokens=self.sampler.teacher_tokens,EOT_teachers=self.sampler.eot_teachers,
            valid_input_tokens=self.sampler.input_tokens,physical_input_tokens=self.sampler.physical_tokens,
            padding_input_tokens=self.sampler.physical_tokens-self.sampler.input_tokens,
            examples=self.sampler.examples,removed_turns=self.sampler.removed_turns,
            requested_series_budget=self.sampler.series_budget,
            final_whole_window_overshoot=max(0,self.sampler.series_tokens-self.sampler.series_budget))
        self._set_sft_lr()
        return row

    def load(self,path,*,decay_branch=False):
        if decay_branch: raise ValueError("SFT recipe must resume unchanged")
        expected_lineage = dict(self.lineage)
        super().load(path)
        if self.lineage != expected_lineage:
            raise ValueError("SFT Base lineage differs")
        if self.tokens != self.sampler.input_tokens or self.supervised_tokens != self.sampler.teacher_tokens:
            raise ValueError("SFT teacher/input accounting differs")
        if self.update <= 0 and self.sampler.examples:
            raise ValueError("Nonzero dialogue cursor without completed update")
        self._set_sft_lr()
