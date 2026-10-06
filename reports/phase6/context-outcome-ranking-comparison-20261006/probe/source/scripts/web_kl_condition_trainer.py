"""Inherited staged CE plus immutable-parent Web KL; checkpoint both samplers."""
import copy
import hashlib
import math
import os
from pathlib import Path
import time
import numpy as np
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.experiment import ROOT,sha256
from jmicro.model import JMicroModel
from jmicro.training import atomic_json,autocast,implementation_hashes,restore_rng,rng_state,synchronize
import condition_positive_trainer as ce_core
from condition_positive_loss import positive_weighted_ce
from historical_parent_condition_trainer import historical_web_cursor
from source_order_condition_trainer import SourceOrderHistoricalTrainer
from web_kl_preservation import POLICY,WebBodyReplay,body_parent_kl

KIND='historical_parent_staged_CE_frozen_Web_KL_100M'


def sources():
    return {p:sha256(ROOT/p) for p in ('scripts/web_kl_condition_trainer.py','scripts/web_kl_preservation.py')}


def model_digest(model):
    digest=hashlib.sha256()
    for key,value in model.state_dict().items():
        digest.update(key.encode());digest.update(value.detach().cpu().contiguous().numpy().tobytes())
    return digest.hexdigest()


class WebKLTrainer(SourceOrderHistoricalTrainer):
    def __init__(self,parent,pool,original_web,positive,goals,binding,device='cuda',context=1024,batch=32,reference_batch=8):
        super().__init__(parent,pool,original_web,positive,goals,binding,device,context,batch)
        policy=dict(POLICY,reference_context=context,reference_batch=reference_batch)
        self.spec.update(research_kind=KIND,KL_policy=policy,KL_sources=sources())
        self.reference_teacher=JMicroModel(parent['model_config']).to(device).eval()
        self.reference_teacher.load_state_dict(parent['model'],strict=True)
        self.reference_teacher.requires_grad_(False)
        self.teacher_digest=model_digest(self.reference_teacher)
        self.replay=WebBodyReplay(original_web,historical_web_cursor(parent),reference_batch,context)
        self.lineage.update(kind='staged-CE-frozen-parent-Web-KL',KL_policy=policy,
            reference_teacher=copy.deepcopy(binding['parent']),reference_teacher_weight_digest=self.teacher_digest)
        restore_rng(parent['rng'])

    def audit_counters(self):
        super().audit_counters()
        if hasattr(self,'replay'):
            if (self.replay.updates!=self.update-self.lineage['parent_update']
                    or self.replay.physical_input_tokens!=self.replay.updates*self.replay.batch*self.replay.context
                    or self.replay.body_positions+self.replay.ignored_positions!=self.replay.physical_input_tokens):
                raise ValueError('Completed CE and reference replay counters differ')

    def verify_teacher(self):
        if (self.reference_teacher.training or any(p.requires_grad or p.grad is not None for p in self.reference_teacher.parameters())
                or model_digest(self.reference_teacher)!=self.teacher_digest):
            raise ValueError('Frozen parent teacher mode/weights/gradients changed')

    def step(self):
        synchronize(self.device);started=time.perf_counter()
        x,y,byte_count,focused=self.sampler.batch(self.spec['batch'])
        rx,ry=self.replay.next()
        if x.eq(0).any():raise ValueError('Unpadded main input required')
        digest=hashlib.sha256(bytes.fromhex(self.token_digest))
        digest.update(x.numpy().astype('<i8').tobytes());digest.update(y.numpy().astype('<i8').tobytes())
        focus_digest=hashlib.sha256(bytes.fromhex(self.focus_token_digest))
        focus_digest.update(focused.numpy().astype(np.uint8).tobytes())
        data_wait=time.perf_counter()-started
        self.optimizer.zero_grad(set_to_none=True);self.model.train()
        x,y,focused=x.to(self.device),y.to(self.device),focused.to(self.device)
        backend=SDPBackend.FLASH_ATTENTION if self.spec['backend']=='flash' else SDPBackend.MATH
        with sdpa_kernel(backend),autocast(self.device,self.spec['dtype']):
            logits=self.forward(x,training_fast_path=True).logits
            ce,counts=positive_weighted_ce(logits,y,focused,1)
        ce.backward();del logits
        rx,ry=rx.to(self.device),ry.to(self.device)
        with sdpa_kernel(backend),autocast(self.device,self.spec['dtype']):
            with torch.no_grad():target=self.reference_teacher(rx,training_fast_path=True).logits
            prediction=self.forward(rx,training_fast_path=True).logits
            kl,reference_counts=body_parent_kl(prediction,target,ry)
        kl.backward();del target,prediction
        norm=torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        ce_value,kl_value=float(ce.detach()),float(kl.detach())
        if not all(math.isfinite(v) for v in (ce_value,kl_value,float(norm))):raise ValueError('Finite combined gradients/loss required')
        if reference_counts['physical_reference_input_tokens']!=self.replay.batch*self.replay.context:
            raise ValueError('Reference physical positions differ')
        lr=self.optimizer.param_groups[0]['lr'];self.optimizer.step();self.scheduler.step()
        self.update+=1;self.tokens+=x.numel();self.supervised_tokens+=counts['ordinary_teacher_tokens']
        self.body_bytes+=byte_count;self.focus_teacher_tokens+=counts['outcome_focus_teacher_tokens']
        self.weighted_teacher_mass+=counts['weighted_teacher_mass']
        self.token_digest,self.focus_token_digest=digest.hexdigest(),focus_digest.hexdigest()
        self.audit_counters();synchronize(self.device);seconds=time.perf_counter()-started
        return dict(update=self.update,loss=ce_value+kl_value,ordinary_CE_loss=ce_value,reference_KL_loss=kl_value,
            gradient_norm=float(norm),lr=lr,tokens_seen=self.tokens,supervised_tokens=self.supervised_tokens,
            body_bytes_seen=self.body_bytes,token_digest=self.token_digest,focus_token_digest=self.focus_token_digest,
            focus_teacher_tokens=self.focus_teacher_tokens,weighted_teacher_mass=self.weighted_teacher_mass,outcome_weight=1,
            seconds=seconds,data_wait_seconds=data_wait,tokens_per_second=x.numel()/seconds,
            source_teachers=self.sampler.source_teachers.copy(),source_eos=self.sampler.source_eos.copy(),
            source_input_tokens=self.sampler.source_tokens.copy(),source_body_bytes=self.sampler.source_body_bytes.copy(),
            source_focus_teachers=self.sampler.source_focus_teachers.copy(),valid_input_tokens=self.tokens-self.lineage['parent_tokens'],
            physical_input_tokens=self.tokens-self.lineage['parent_tokens'],additional_teacher_tokens=self.supervised_tokens-self.lineage['parent_supervised_tokens'],
            reference_input_tokens=self.replay.physical_input_tokens,reference_soft_target_body_positions=self.replay.body_positions,
            reference_ignored_positions=self.replay.ignored_positions,reference_digest=self.replay.digest,
            combined_student_physical_input_tokens=self.tokens-self.lineage['parent_tokens']+self.replay.physical_input_tokens)

    def save(self,path):
        self.audit_counters();self.verify_teacher();started=time.perf_counter();path.parent.mkdir(parents=True,exist_ok=True)
        state=dict(version=2,spec=self.spec,model_config=self.model.config,model=self.model.state_dict(),
            optimizer=self.optimizer.state_dict(),scheduler=self.scheduler.state_dict(),rng=rng_state(),sampler=self.sampler.state_dict(),
            update=self.update,tokens=self.tokens,supervised_tokens=self.supervised_tokens,body_bytes=self.body_bytes,
            token_digest=self.token_digest,focus_token_digest=self.focus_token_digest,focus_teacher_tokens=self.focus_teacher_tokens,
            weighted_teacher_mass=self.weighted_teacher_mass,shard_manifest_sha256=sha256(self.shard.directory/'manifest.json'),
            implementation_sha256=implementation_hashes(),study_implementation_sha256=sha256(Path(ce_core.__file__)),
            loss_implementation_sha256=sha256(Path(ce_core.__file__).with_name('condition_positive_loss.py')),
            study_binding=self.binding,pilot_binding=self.pilot_binding,lineage=self.lineage,
            branch_updates=self.update-self.lineage['parent_update'],branch_tokens=self.tokens-self.lineage['parent_tokens'],
            KL_state=dict(policy=self.spec['KL_policy'],source_sha256=sources(),reference_teacher=self.binding['parent'],
                teacher_weight_digest=self.teacher_digest,replay=self.replay.state_dict()))
        temporary=path.with_suffix('.tmp')
        with temporary.open('wb') as stream:
            torch.save(state,stream);stream.flush();os.fsync(stream.fileno())
        os.replace(temporary,path)
        atomic_json(path.parent/'latest.json',dict(path=str(path.resolve()),sha256=sha256(path),update=self.update,tokens_seen=self.tokens))
        return time.perf_counter()-started

    def load(self,path):
        state=torch.load(path,map_location='cpu',weights_only=False);extra=state['KL_state']
        if (extra['policy']!=self.spec['KL_policy'] or extra['source_sha256']!=sources()
                or extra['reference_teacher']!=self.binding['parent'] or extra['teacher_weight_digest']!=self.teacher_digest):
            raise ValueError('Immutable reference teacher/auxiliary objective/source differs')
        self.replay.load_state_dict(extra['replay'])
        super().load(path)
        self.verify_teacher();self.audit_counters()
