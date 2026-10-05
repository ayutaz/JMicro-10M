"""Integrate matched CE/sequence-UL updates without altering frozen trainers."""
import copy
import hashlib
import math
from pathlib import Path
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel, SDPBackend

from jmicro.experiment import ROOT,sha256
from jmicro.training import autocast,synchronize
from jmicro.sequence_unlikelihood import greedy_rollout,continuation_logits,repeated_ngram_mask,sequence_unlikelihood_sum
from textbook_quantity_trainer import ThreeSourceTrainer


def train_prefixes(batches,count,width):
    """Take actual complete train-document heads, never packed boundary spans."""
    result=[]
    for x,_,_ in batches:
        for row in x.tolist():
            for start,token in enumerate(row):
                if token != 2 or start+width>len(row):continue
                candidate=row[start:start+width]
                if all(t>=8 for t in candidate[1:]):
                    result.append(candidate)
                    if len(result)==count:return torch.tensor(result,dtype=torch.long)
    return torch.tensor(result,dtype=torch.long) if result else None


def source_binding():
    return {p:sha256(ROOT/p) for p in ("scripts/sequence_objective_trainer.py","src/jmicro/sequence_unlikelihood.py")}


class SequenceObjectiveTrainer(ThreeSourceTrainer):
    def __init__(self,parent,web,pool,mode,goals,binding,device="cuda"):
        objective=copy.deepcopy(binding["sequence_objective"])
        if (parent["update"]<=0 or parent["sampler"].get("kind")!="teacher-learning-curve-v1" or
                parent["sampler"]["source_teachers"]["short"]!=parent["spec"]["curve_schedule"]["teachers"] or
                binding["curve_mode"]!="decay" or binding["optimizer_policy"]!="inherit" or
                binding["warmup_updates"]!=0 or
                binding["peak_lr"]>parent["optimizer"]["param_groups"][0]["lr"]*(1+1e-12)):
            raise ValueError("Objective fork requires a completed actual parent, inherited state, and no LR reheat")
        if (type(objective["alpha"]) not in (int,float) or not math.isfinite(objective["alpha"]) or objective["alpha"]<0 or
                any(type(objective[k]) is not int or objective[k]<=0 for k in
                    ("every_updates","prefixes","prefix_tokens","max_new_tokens","ngram")) or
                objective["prefix_tokens"]<2 or objective["ngram"]<2):
            raise ValueError("Invalid frozen sequence objective")
        # CPU Adam load_state_dict may reuse parent tensors. Own the state so
        # one arm's optimizer updates cannot mutate the other arm's parent.
        super().__init__(copy.deepcopy(parent),web,pool,mode,goals,binding,device)
        self.spec["sequence_objective"]=objective
        self.lineage["kind"]="sequence-objective-comparison"
        self.lineage["sequence_objective"]=dict(source_sha256=source_binding(),
            parent_actual_curve_mode=parent["spec"]["curve_schedule"]["mode"],
            objective=objective,rollout_batches=0,skipped_rollouts=0,generated_continuations=0,
            generated_body_tokens=0,generated_EOS=0,negative_token_positions=0,
            extra_valid_input_tokens=0,extra_physical_input_tokens=0,
            generated_digest=hashlib.sha256(b"").hexdigest())

    def step(self):
        synchronize(self.device);started=time.perf_counter();self._set_token_lr()
        batches=[self.sampler.batch(self.spec["batch"]) for _ in range(self.spec["accumulation"])]
        denominator=sum(int(y.ne(-100).sum()) for _,y,_ in batches)
        if denominator==0:raise ValueError("No CE teacher targets")
        data_wait=time.perf_counter()-started
        self.optimizer.zero_grad(set_to_none=True);self.model.train()
        digest=hashlib.sha256(bytes.fromhex(self.token_digest));CE=0.;UL=0.
        backend={"math":[SDPBackend.MATH],"flash":[SDPBackend.FLASH_ATTENTION],
                 "default":[SDPBackend.FLASH_ATTENTION,SDPBackend.EFFICIENT_ATTENTION,SDPBackend.MATH]}[self.spec.get("backend","default")]
        for x,y,_ in batches:
            if self.spec.get("training_fast_path") and bool(x.eq(0).any()):raise ValueError("PAD cannot enter compiled CE blocks")
            digest.update(x.numpy().astype("<i8").tobytes());digest.update(y.numpy().astype("<i8").tobytes())
            with sdpa_kernel(backend),autocast(self.device,self.spec["dtype"]):
                logits=self.forward(x.to(self.device),training_fast_path=self.spec.get("training_fast_path",False)).logits
                loss=F.cross_entropy(logits.reshape(-1,logits.shape[-1]),y.to(self.device).reshape(-1),ignore_index=-100,reduction="sum")/denominator
            loss.backward();CE+=float(loss.detach())
        local=self.update-self.lineage["parent_update"]+1
        objective=self.spec["sequence_objective"];counts=copy.deepcopy(self.lineage["sequence_objective"])
        if local%objective["every_updates"]==0:
            prefix=train_prefixes(batches,objective["prefixes"],objective["prefix_tokens"])
            if prefix is None:counts["skipped_rollouts"]+=1
            else:
                prefix=prefix.to(self.device)
                # Cache/masked scoring has its own explicit math backend. Both
                # arms execute this same extra path, including control alpha0.
                with sdpa_kernel([SDPBackend.MATH]),autocast(self.device,self.spec["dtype"]):
                    generated=greedy_rollout(self.model,prefix,max_new_tokens=objective["max_new_tokens"])
                    mask=torch.tensor(repeated_ngram_mask(generated.tolist(),n=objective["ngram"]),dtype=torch.bool,device=self.device)
                    body=int(generated.ge(8).sum())
                    scored=continuation_logits(self.model,prefix,generated)
                    auxiliary=sequence_unlikelihood_sum(scored,generated,mask)/max(1,body)
                UL=float(auxiliary.detach());(objective["alpha"]*auxiliary).backward()
                counts["rollout_batches"]+=1;counts["generated_continuations"]+=prefix.shape[0]
                counts["generated_body_tokens"]+=body;counts["generated_EOS"]+=int(generated.eq(3).sum())
                counts["negative_token_positions"]+=int(mask.sum())
                score_ids=torch.cat((prefix,generated),dim=1)[:,:-1]
                counts["extra_physical_input_tokens"]+=prefix.numel()+generated[:,:-1].numel()+score_ids.numel()
                counts["extra_valid_input_tokens"]+=prefix.numel()+int(generated[:,:-1].ne(0).sum())+int(score_ids.ne(0).sum())
                extra_digest=hashlib.sha256(bytes.fromhex(counts["generated_digest"]))
                for value in (prefix,generated,mask):extra_digest.update(value.cpu().numpy().tobytes())
                counts["generated_digest"]=extra_digest.hexdigest()
        norm=torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        if not all(math.isfinite(v) for v in (CE,UL)):raise ValueError("Nonfinite CE or sequence loss")
        lr=self.optimizer.param_groups[0]["lr"];self.optimizer.step();self.scheduler.step();self.update+=1
        physical=sum(x.numel() for x,_,_ in batches);valid=sum(int(x.ne(0).sum()) for x,_,_ in batches)
        self.tokens+=valid;self.supervised_tokens+=denominator;self.body_bytes+=sum(b for _,_,b in batches)
        self.token_digest=digest.hexdigest();self.lineage["sequence_objective"]=counts
        if self.supervised_tokens-self.lineage["parent_supervised_tokens"]!=sum(self.sampler.source_teachers.values()):
            raise ValueError("CE teacher accounting differs; generated negatives are not gold teachers")
        self._set_token_lr();synchronize(self.device);seconds=time.perf_counter()-started
        return dict(update=self.update,loss=CE,sequence_UL=UL,optimization_loss=CE+objective["alpha"]*UL,
            gradient_norm=float(norm),lr=lr,tokens_seen=self.tokens,supervised_tokens=self.supervised_tokens,
            additional_supervised_tokens=sum(self.sampler.source_teachers.values()),
            valid_input_tokens=sum(self.sampler.source_tokens.values()),physical_input_tokens=sum(self.sampler.source_physical_tokens.values()),
            body_bytes_seen=self.body_bytes,token_digest=self.token_digest,source="short",source_teachers=self.sampler.source_teachers.copy(),
            seconds=seconds,data_wait_seconds=data_wait,tokens_per_second=physical/seconds,
            sequence_objective=copy.deepcopy(counts))

    def load(self,path):
        state=torch.load(path,map_location="cpu",weights_only=False)
        if state["lineage"].get("sequence_objective",{}).get("source_sha256")!=source_binding():
            raise ValueError("Sequence objective resume source differs")
        super().load(path)
        counts=self.lineage["sequence_objective"];local=self.update-self.lineage["parent_update"]
        if (counts["objective"]!=self.spec["sequence_objective"] or
                counts["rollout_batches"]+counts["skipped_rollouts"]!=local//self.spec["sequence_objective"]["every_updates"] or
                counts["extra_valid_input_tokens"]>counts["extra_physical_input_tokens"]):
            raise ValueError("Sequence objective completed-update accounting differs")
