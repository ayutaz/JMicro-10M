"""Same original CE stream; one full-batch SAM perturbation and AdamW update.

Original teacher positions are counted once. The second evaluation of the
same positions and inputs is separately counted; it is not new corpus.
Checkpoints contain exactly restored, completed-update weights.
"""
import copy
import hashlib
import json
from pathlib import Path
import time
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from natural_context_contrast_corpus import NaturalCorpusTrainer
from natural_context_contrast_trainer import right_pad, right_padded_hidden
from jmicro.training import synchronize

KIND = 'native_original_CE_same_batch_full_parameter_SAM_AdamW_v1'
RECIPE = dict(rho=.05, epsilon=1e-12, adaptive=False,
    perturbation='rho_times_unclipped_global_CE_gradient_over_global_L2_norm_plus_epsilon',
    second_batch='identical_original_ids_targets_masks',
    restore='exact_copy_original_FP32_parameters_before_single_AdamW_update',
    optimizer='fresh_AdamW_lr1e-5_wd0.1_constant', final_clip_norm=1.)


def sam_backward(model, optimizer, closure):
    """Return finite losses and second-pass clipped gradient; never update here."""
    parameters = list(model.parameters())  # tied vocabulary appears once
    optimizer.zero_grad(set_to_none=True)
    first = closure()
    if not torch.isfinite(first): raise ValueError('Nonfinite SAM first CE')
    first.backward()
    if any(p.grad is None for p in parameters):
        raise ValueError('Full native parameter CE gradient required')
    norm = torch.stack([p.grad.detach().float().norm() for p in parameters]).norm()
    if not torch.isfinite(norm) or norm <= 0: raise ValueError('Finite nonzero first gradient required')
    originals = [p.detach().clone() for p in parameters]
    scale = RECIPE['rho'] / (norm + RECIPE['epsilon'])
    first_loss = float(first.detach())
    del first
    try:
        with torch.no_grad():
            for p in parameters: p.add_(p.grad * scale)
            actual_norm = torch.stack([(p-old).float().norm() for p,old in zip(parameters, originals, strict=True)]).norm()
        optimizer.zero_grad(set_to_none=True)
        second = closure()
        if not torch.isfinite(second): raise ValueError('Nonfinite SAM perturbed CE')
        second.backward()
        second_loss = float(second.detach())
        del second
        second_norm = torch.nn.utils.clip_grad_norm_(parameters, 1., error_if_nonfinite=True)
        if not torch.isfinite(actual_norm) or not 0 < actual_norm <= .05001:
            raise ValueError('Realized finite global perturbation exceeds fixed radius')
        return dict(CE_loss=first_loss, perturbed_CE_loss=second_loss,
            first_gradient_norm=float(norm), gradient_norm=float(second_norm),
            perturbation_L2=float(actual_norm))
    finally:
        # Subtracting epsilon introduces rounding drift. Restore exact originals.
        with torch.no_grad():
            for p,old in zip(parameters, originals, strict=True): p.copy_(old)


def committed_state(state):
    if state.get('kind') != KIND or state['spec'].get('SAM') != RECIPE: return False
    c,s = state['counters'],state['SAM']; steps=c['update']
    if (s != dict(updates=steps, repeated_teacher_positions=c['supervised_tokens'],
            repeated_valid_inputs=c['CE_input_tokens'], repeated_physical_inputs=c['physical_input_tokens']) or
        steps != state['scheduler']['last_epoch'] or
        any(int(v['step']) != steps for v in state['optimizer']['state'].values()) or
        c['supervised_tokens'] != sum(c['source_teachers'].values()) or
        c['source_teachers'] != state['sampler']['consumed'] or
        c['auxiliary_input_tokens'] or c['auxiliary_pairs'] or c['auxiliary_digest'] != '0'*64): return False
    def finite(value):
        if isinstance(value,torch.Tensor): return bool(torch.isfinite(value).all())
        if isinstance(value,dict): return all(finite(v) for v in value.values())
        if isinstance(value,(list,tuple)): return all(finite(v) for v in value)
        return True
    return finite(state['model']) and finite(state['optimizer'])


class SAMTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, contrast=False, device='cuda', seed=42):
        if contrast: raise ValueError('No contrastive/teacher auxiliary objective in SAM comparison')
        super().__init__(parent,sampler,binding,batch,False,device,seed)
        if self.model.config.get('dropout',0) != 0: raise ValueError('Fixed deterministic dropout0 model required')
        self.spec.update(kind=KIND,SAM=copy.deepcopy(RECIPE))
        self.lineage.update(kind=KIND)
        self.SAM = dict(updates=0,repeated_teacher_positions=0,repeated_valid_inputs=0,repeated_physical_inputs=0)
        self._step_in_progress = False

    def state_dict(self):
        if self._step_in_progress: raise ValueError('Cannot serialize uncommitted or perturbed SAM update')
        state=super().state_dict(); state.update(kind=KIND,SAM=copy.deepcopy(self.SAM)); return state

    def load(self,path):
        state=torch.load(Path(path),map_location=self.device,weights_only=False)
        if not committed_state(state): raise ValueError('Completed SAM full state/counters required')
        super().load(path); self.SAM=copy.deepcopy(state['SAM'])

    def step(self):
        if self._step_in_progress: raise ValueError('Interrupted update requires a fresh valid checkpoint resume')
        synchronize(self.device); started=time.monotonic(); self._step_in_progress=True
        rows=self.sampler.take(self.spec['batch']); wait=time.monotonic()-started
        ids,_=right_pad([r['input_ids'] for r in rows],self.device)
        targets=torch.full_like(ids,-100)
        for i,r in enumerate(rows): targets[i,:len(r['target_ids'])]=torch.tensor(r['target_ids'],device=self.device)
        mask=targets.ne(-100); gold=sum(r['teacher_tokens'] for r in rows)
        if int(mask.sum()) != gold: raise ValueError('Exact original supervised mask required')
        backend=SDPBackend.FLASH_ATTENTION if self.device.type=='cuda' else SDPBackend.MATH
        def closure():
            with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=self.device.type=='cuda'):
                hidden=right_padded_hidden(self.model,ids)
                return F.cross_entropy(self.model.lm_head(hidden[mask]).float(),targets[mask])
        measures=sam_backward(self.model,self.optimizer,closure)
        self.optimizer.step(); self.scheduler.step(); self.counters['update']+=1
        valid=sum(len(r['input_ids']) for r in rows)
        for k,v in dict(supervised_tokens=gold,CE_input_tokens=valid,physical_input_tokens=ids.numel(),
            original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items(): self.counters[k]+=v
        for r in rows:
            self.counters['source_teachers'][r['source']]+=r['teacher_tokens']
            self.counters['source_EOS'][r['source']]+=r['original_EOS_targets']
        if self.counters['source_teachers'] != self.sampler.consumed: raise ValueError('Committed source cursor differs')
        stream=json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest']=hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        for k,v in dict(updates=1,repeated_teacher_positions=gold,repeated_valid_inputs=valid,repeated_physical_inputs=ids.numel()).items(): self.SAM[k]+=v
        self._step_in_progress=False; synchronize(self.device)
        return dict(**copy.deepcopy(self.counters),SAM=copy.deepcopy(self.SAM),**measures,
            combined_loss=measures['perturbed_CE_loss'],lr=self.optimizer.param_groups[0]['lr'],
            CE_targets_this_update=gold,physical_inputs_this_update=ids.numel(),
            repeated_teacher_positions_this_update=gold,repeated_valid_inputs_this_update=valid,
            repeated_physical_inputs_this_update=ids.numel(),seconds=time.monotonic()-started,data_wait_seconds=wait,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),original_windows_this_update=len(rows),
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])
