"""Frozen-backbone rank-four Base adaptation and matched fresh-Adam control.

Checkpoints contain both native merged evaluation weights and the unmerged
training state. Loading always resumes the latter, never a merged backbone.
"""
import copy
import math
import os
from pathlib import Path
import time
import torch
from torch import nn
from torch.nn import functional as F
from jmicro.experiment import sha256
from jmicro.training import atomic_json, implementation_hashes, restore_rng, rng_state
from interleaved_outcome_trainer import InterleavedOutcomeTrainer

KIND = 'matched_fresh_Adam_rank4_frozen_backbone_Base_v1'
TARGETS = ('q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj')
RANK = 4
COUNTERS = ('update', 'tokens', 'supervised_tokens', 'body_bytes', 'token_digest',
            'focus_token_digest', 'focus_teacher_tokens', 'weighted_teacher_mass')


class LowRankLinear(nn.Module):
    def __init__(self, original, generator, rank=RANK):
        super().__init__()
        if original.bias is not None or rank != RANK:
            raise ValueError('Fixed rank-four bias-free projections only')
        self.weight = original.weight
        self.weight.requires_grad_(False)
        # Local CPU generator: initialization cannot advance the parent RNG.
        a = torch.empty(rank, original.in_features)
        a.uniform_(-1 / math.sqrt(original.in_features), 1 / math.sqrt(original.in_features), generator=generator)
        self.A = nn.Parameter(a.to(self.weight.device, self.weight.dtype))
        self.B = nn.Parameter(torch.zeros(original.out_features, rank, device=self.weight.device, dtype=self.weight.dtype))

    def forward(self, x):
        return F.linear(x, self.weight) + F.linear(F.linear(x, self.A), self.B)


def attach(model):
    model.requires_grad_(False)
    generator = torch.Generator(device='cpu').manual_seed(42)
    names = []
    for name, module in sorted(list(model.named_modules())):
        if name.rsplit('.', 1)[-1] in TARGETS:
            if not isinstance(module, nn.Linear):
                raise ValueError('Expected native bias-free linear projection: ' + name)
            parent, leaf = name.rsplit('.', 1)
            setattr(model.get_submodule(parent), leaf, LowRankLinear(module, generator))
            names.append(name)
    if len(names) != len(model.model.layers) * len(TARGETS):
        raise ValueError('Every native attention/MLP projection required exactly once')
    return names


def merged_state(model):
    """FP32 W0+B@A, original state keys/ties; no in-place merge or RNG use."""
    state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()
             if not k.endswith(('.A', '.B'))}
    for name, module in model.named_modules():
        if isinstance(module, LowRankLinear):
            state[name + '.weight'] = (module.weight.detach().float().cpu()
                                      + module.B.detach().float().cpu() @ module.A.detach().float().cpu())
    return state


class LowRankBaseTrainer(InterleavedOutcomeTrainer):
    def __init__(self, parent, pool, original, positive, goals, binding, arm,
                 device='cuda', context=1024, batch=32):
        if arm not in ('full_fresh_Adam', 'rank4_frozen_backbone'):
            raise ValueError('Only the fixed two-arm comparison allowed')
        super().__init__(parent, pool, original, positive, goals, binding, device, context, batch)
        self.arm = arm
        self.targets = attach(self.model) if arm == 'rank4_frozen_backbone' else []
        groups = []
        # Same AdamW hyperparameters and decay classification in both arms.
        # Moment tensors are intentionally fresh in BOTH arms.
        original_groups = parent['optimizer']['param_groups']
        if len(original_groups) != 2:
            raise ValueError('Native matrix/vector optimizer groups required')
        for index, dimensional in enumerate((True, False)):
            params = [p for p in self.model.parameters() if p.requires_grad and (p.ndim >= 2) == dimensional]
            options = {k: copy.deepcopy(v) for k, v in original_groups[index].items()
                       if k not in ('params', 'lr', 'initial_lr')}
            groups.append(dict(params=params, lr=.0001, initial_lr=.0001, **options))
        self.optimizer = torch.optim.AdamW(groups)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda _: .1)
        self.scheduler.load_state_dict(copy.deepcopy(parent['scheduler']))
        for group in self.optimizer.param_groups:
            group['lr'] = .00001
        self.trainable_count = sum(p.numel() for p in self.model.parameters() if p.requires_grad)
        self.native_count = sum(p.numel() for p in self.model.parameters()) - (self.trainable_count if self.targets else 0)
        self.initial_native = {k: v.detach().cpu().clone() for k, v in parent['model'].items()}
        self.spec.update(research_kind=KIND,arm=arm,rank=RANK if self.targets else None,
                         adapter_scale=1 if self.targets else None,adapter_dropout=0,
                         low_rank_trainer_sha256=sha256(Path(__file__)),optimizer_policy='fresh_Adam_both_arms',
                         trainable_parameters=self.trainable_count,native_parameters=self.native_count,
                         target_projections=list(self.targets))
        self.lineage.update(kind=KIND,optimizer_policy='fresh_Adam_both_arms',
                            original_parent_optimizer_preserved_as_lineage_not_active=True,
                            parent_optimizer_hyperparameters=[{k:v for k,v in g.items() if k!='params'} for g in original_groups],
                            frozen_backbone=bool(self.targets),original_parent_model_sha256=binding['parent']['sha256'])
        # The old compiled callable is lazy; bind the final adapter structure.
        self.forward = torch.compile(self.model, mode=self.spec['compile_mode']) if self.spec['compile'] else self.model
        restore_rng(parent['rng'])
        self.audit_parameters()

    def audit_parameters(self):
        if sum(p.numel() for p in self.model.parameters() if p.requires_grad) != self.trainable_count:
            raise ValueError('Trainable parameter set changed')
        if self.targets:
            state = self.model.state_dict()
            if any(not torch.equal(state[k].detach().cpu(), v) for k, v in self.initial_native.items()):
                raise ValueError('Frozen backbone changed')
            if any(p.grad is not None for p in self.model.parameters() if not p.requires_grad):
                raise ValueError('Frozen backbone acquired a gradient')
            if any(p.requires_grad != name.endswith(('.A','.B')) for name,p in self.model.named_parameters()):
                raise ValueError('Only rank-four matrices may learn')

    def step(self):
        row = super().step()
        row.update(arm=self.arm,trainable_parameters=self.trainable_count,native_parameters=self.native_count)
        return row

    def save(self, path):
        self.audit_counters();self.audit_parameters();started=time.perf_counter()
        path.parent.mkdir(parents=True,exist_ok=True)
        state=dict(version=2,spec=self.spec,model_config=self.model.config,model=merged_state(self.model),
            unmerged_training_model={k:v.detach().cpu().clone() for k,v in self.model.state_dict().items()},
            optimizer=self.optimizer.state_dict(),scheduler=self.scheduler.state_dict(),rng=rng_state(),
            sampler=self.sampler.state_dict(),**{k:getattr(self,k) for k in COUNTERS},
            shard_manifest_sha256=sha256(self.shard.directory/'manifest.json'),implementation_sha256=implementation_hashes(),
            study_implementation_sha256=sha256(Path(__file__)),study_binding=self.binding,pilot_binding=self.pilot_binding,
            lineage=self.lineage,branch_updates=self.update-self.lineage['parent_update'],
            branch_tokens=self.tokens-self.lineage['parent_tokens'],merged_for_native_evaluation=True,
            native_parameters=self.native_count,trainable_parameters=self.trainable_count)
        temporary=path.with_suffix('.tmp')
        with temporary.open('wb') as stream:
            torch.save(state,stream);stream.flush();os.fsync(stream.fileno())
        os.replace(temporary,path)
        atomic_json(path.parent/'latest.json',dict(path=str(path.resolve()),sha256=sha256(path),update=self.update,tokens_seen=self.tokens))
        return time.perf_counter()-started

    def load(self,path):
        state=torch.load(path,map_location='cpu',weights_only=False)
        if (state['spec']!=self.spec or state['study_binding']!=self.binding or state['implementation_sha256']!=implementation_hashes()
                or state['study_implementation_sha256']!=sha256(Path(__file__)) or state['model_config']!=self.model.config
                or state['lineage']!=self.lineage or state['shard_manifest_sha256']!=sha256(self.shard.directory/'manifest.json')):
            raise ValueError('Frozen rank-four/full-control identity differs')
        self.model.load_state_dict(state['unmerged_training_model'],strict=True)
        self.audit_parameters()
        merged=merged_state(self.model)
        if set(merged)!=set(state['model']) or any(not torch.equal(merged[k],v) for k,v in state['model'].items()):
            raise ValueError('Native merged evaluation weights differ from training state')
        self.optimizer.load_state_dict(state['optimizer']);self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        for k in COUNTERS:setattr(self,k,state[k])
        self.audit_counters();restore_rng(state['rng'])
