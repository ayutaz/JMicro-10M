"""Matched staged CE forks from a completed mixed fullstate, fixed parameter L2."""
import copy
import hashlib
import math
from pathlib import Path
from types import SimpleNamespace
import time
import numpy as np
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import sha256
from jmicro.training import Trainer,autocast,implementation_hashes,restore_rng,synchronize
from condition_positive_trainer import ConditionPositiveTrainer
from condition_positive_loss import positive_weighted_ce
from source_order_condition_trainer import SourceOrderQuotaSampler,SOURCE_ORDER

KIND='mixed_fullstate_matched_staged_parameter_displacement_v1'


def parameter_penalty(named,anchor,coefficient):
    if not math.isfinite(coefficient) or coefficient<0:raise ValueError('Finite nonnegative fixed coefficient required')
    if [k for k,_ in named]!=list(anchor):raise ValueError('All aligned unique parameters required')
    return coefficient/2*torch.stack([(p-anchor[k]).float().square().sum() for k,p in named]).sum()


class ParameterAnchorTrainer(ConditionPositiveTrainer):
    def __init__(self,parent,pool,original,positive,goals,binding,coefficient,device='cuda',context=1024,batch=32):
        if parent['implementation_sha256']!=implementation_hashes():raise ValueError('Parent implementation differs')
        if (parent['sampler'].get('kind')!='original-Web-retention-short-source-quotas-v1'
                or parent['sampler']['source_teachers']!=parent['sampler']['goals']
                or set(parent['sampler']['streams'])!=set(SOURCE_ORDER)):
            raise ValueError('Completed mixed four-source fullstate required')
        cursor=copy.deepcopy(parent['sampler']['streams']['web']['sampler'])
        lrs=[g['lr'] for g in parent['optimizer']['param_groups']]
        if any(not math.isclose(v,.00001,rel_tol=1e-10) for v in lrs):raise ValueError('Preserve actual LR floor')
        spec=dict(seed=42,context=context,batch=batch,accumulation=1,lr=.00001,
            weight_decay=parent['spec']['weight_decay'],warmup=0,schedule_updates=parent['update']+10000,
            scheduler='wsd',dtype='bf16' if device=='cuda' else 'fp32',backend='flash' if device=='cuda' else 'math',
            compile=device=='cuda',compile_mode='reduce-overhead',training_fast_path=True,deterministic=True,
            teacher_goals=dict(goals),research_kind=KIND,outcome_weight=1,source_order=list(SOURCE_ORDER),
            positive_manifest_sha256=positive.manifest_sha256,parameter_coefficient=coefficient,
            anchor_checkpoint=binding['parent'],anchor_trainer_sha256=sha256(Path(__file__)))
        stub=SimpleNamespace(tokens=pool.tokens[:context+1],split='train',manifest=pool.manifest,
            byte_lengths=pool.byte_lengths,directory=pool.directory)
        Trainer.__init__(self,parent['model_config'],stub,spec,device)
        self.shard=pool;self.model.load_state_dict(parent['model'],strict=True)
        self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']))
        if any(not math.isclose(lr/base,.1,rel_tol=1e-10) for lr,base in zip(lrs,parent['scheduler']['base_lrs'],strict=True)):
            raise ValueError('Actual scheduler permanent floor differs')
        self.scheduler=torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:.1)
        self.scheduler.load_state_dict(copy.deepcopy(parent['scheduler']))
        # LambdaLR construction mutates the optimizer LR. Restore its exact parent
        # groups after loading the frozen scheduler; future steps use its base_lrs.
        self.optimizer.load_state_dict(copy.deepcopy(parent['optimizer']))
        self.sampler=SourceOrderQuotaSampler(pool,original,positive,cursor,goals,context,42)
        self.factor=1;self.coefficient=coefficient
        self.anchor={k:p.detach().clone() for k,p in self.model.named_parameters()}
        self.anchor_initial_digest=self.anchor_digest()
        for key in ('update','tokens','supervised_tokens','body_bytes','token_digest'):setattr(self,key,parent[key])
        self.focus_teacher_tokens=self.weighted_teacher_mass=0;self.focus_token_digest='00'*32
        self.binding=copy.deepcopy(binding);self.pilot_binding=dict(parent.get('pilot_binding',{}),**binding)
        self.lineage=dict(kind=KIND,parent=binding['parent'],parent_update=parent['update'],
            parent_tokens=parent['tokens'],parent_supervised_tokens=parent['supervised_tokens'],
            parent_body_bytes=parent['body_bytes'],parent_token_digest=parent['token_digest'],
            actual_parent_sampler=copy.deepcopy(parent['sampler']),actual_parent_Web_cursor=cursor,
            parent_scheduler=copy.deepcopy(parent['scheduler']),optimizer_policy='inherit',no_reheat=True,
            anchor_initial_digest=self.anchor_initial_digest,
            source_sampler_policy='Continue mixed endpoint actual Web cursor; fresh identical seed42 short streams, '
                'new local staged quotas/counters in both arms; original mixed sampler preserved in lineage.')
        restore_rng(parent['rng']);self.audit_counters()

    def anchor_digest(self):
        digest=hashlib.sha256()
        for k,v in self.anchor.items():digest.update(k.encode());digest.update(v.detach().cpu().numpy().tobytes())
        return digest.hexdigest()

    def step(self):
        synchronize(self.device);started=time.perf_counter()
        x,y,byte_count,focused=self.sampler.batch(self.spec['batch'])
        if x.eq(0).any():raise ValueError('Unpadded input required')
        digest=hashlib.sha256(bytes.fromhex(self.token_digest));digest.update(x.numpy().astype('<i8').tobytes());digest.update(y.numpy().astype('<i8').tobytes())
        focus_digest=hashlib.sha256(bytes.fromhex(self.focus_token_digest));focus_digest.update(focused.numpy().astype(np.uint8).tobytes())
        waited=time.perf_counter()-started;self.optimizer.zero_grad(set_to_none=True);self.model.train()
        x,y,focused=x.to(self.device),y.to(self.device),focused.to(self.device)
        with sdpa_kernel(SDPBackend.FLASH_ATTENTION if self.spec['backend']=='flash' else SDPBackend.MATH),autocast(self.device,self.spec['dtype']):
            logits=self.forward(x,training_fast_path=True).logits;ce,counts=positive_weighted_ce(logits,y,focused,1)
        penalty=parameter_penalty(list(self.model.named_parameters()),self.anchor,self.coefficient)
        loss=ce+penalty;loss.backward()
        norm=torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        values=[float(v.detach()) for v in (loss,ce,penalty)]
        if not all(math.isfinite(v) for v in values):raise ValueError('Finite CE/parameter penalty required')
        lr=self.optimizer.param_groups[0]['lr'];self.optimizer.step();self.scheduler.step()
        self.update+=1;self.tokens+=x.numel();self.supervised_tokens+=counts['ordinary_teacher_tokens'];self.body_bytes+=byte_count
        self.focus_teacher_tokens+=counts['outcome_focus_teacher_tokens'];self.weighted_teacher_mass+=counts['weighted_teacher_mass']
        self.token_digest,self.focus_token_digest=digest.hexdigest(),focus_digest.hexdigest();self.audit_counters()
        synchronize(self.device);seconds=time.perf_counter()-started
        return dict(update=self.update,loss=values[0],CE_loss=values[1],parameter_penalty=values[2],
            parameter_coefficient=self.coefficient,gradient_norm=float(norm),lr=lr,tokens_seen=self.tokens,
            supervised_tokens=self.supervised_tokens,body_bytes_seen=self.body_bytes,
            token_digest=self.token_digest,focus_token_digest=self.focus_token_digest,
            focus_teacher_tokens=self.focus_teacher_tokens,weighted_teacher_mass=self.weighted_teacher_mass,outcome_weight=1,
            source_teachers=self.sampler.source_teachers.copy(),source_eos=self.sampler.source_eos.copy(),
            source_input_tokens=self.sampler.source_tokens.copy(),source_body_bytes=self.sampler.source_body_bytes.copy(),
            source_focus_teachers=self.sampler.source_focus_teachers.copy(),seconds=seconds,data_wait_seconds=waited,
            tokens_per_second=x.numel()/seconds,valid_input_tokens=self.tokens-self.lineage['parent_tokens'],
            physical_input_tokens=self.tokens-self.lineage['parent_tokens'],additional_teacher_tokens=self.supervised_tokens-self.lineage['parent_supervised_tokens'],
            parameter_penalty_teacher_tokens=0)

    def save(self,path):
        if self.anchor_digest()!=self.anchor_initial_digest:raise ValueError('Fixed anchor changed')
        return super().save(path)

    def load(self,path):
        super().load(path)
        if self.lineage['anchor_initial_digest']!=self.anchor_initial_digest:raise ValueError('Saved fixed anchor differs')
