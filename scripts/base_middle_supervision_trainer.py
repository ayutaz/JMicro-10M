"""Original next-token CE plus one native middle-layer shared-head CE.

One decoder forward, no new parameters. Final inference remains unchanged.
Middle-head evaluations are compute on the same gold, not new corpus tokens.
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
from natural_context_contrast_trainer import right_pad
from jmicro.training import synchronize

KIND = 'native_original_CE_single_middle_shared_head_supervision_v1'
RECIPE = dict(middle_layer='floor_native_depth_over_two', coefficient=.1,
    target='identical_original_shifted_body_and_EOS_with_identical_mask',
    head='shared_native_final_RMSNorm_and_tied_LM_head',
    loss='final_mean_CE_plus_0.1_middle_mean_CE_single_backward',
    optimizer='fresh_AdamW_lr1e-5_wd0.1_constant', final_clip_norm=1.,
    decoder_forwards=1, extra_parameters=0, dropout=0, inference='unchanged_full_native_depth')


def middle_hidden(model, ids):
    if ids.shape[1] > model.config['max_position_embeddings']:
        raise ValueError('Original sequence exceeds context')
    depth = len(model.model.layers)
    if depth < 2: raise ValueError('At least two native layers required')
    positions = torch.arange(ids.shape[1],device=ids.device)[None].expand(ids.shape[0],-1)
    x = model.model.embed_tokens(ids)
    middle = None
    for number, layer in enumerate(model.model.layers,1):
        x,_ = layer(x,positions,None,None,causal=True)
        if number == depth//2: middle = x
    return x,middle


def middle_losses(model, ids, targets):
    if ids.shape != targets.shape or not bool(targets.ne(-100).any()):
        raise ValueError('Aligned nonempty original gold required')
    final,middle = middle_hidden(model,ids)
    selected = targets.ne(-100)
    # RMSNorm is pointwise; gather only supervised positions for both heads.
    gold = targets[selected]
    ce = F.cross_entropy(model.lm_head(model.model.norm(final[selected])).float(),gold)
    auxiliary = F.cross_entropy(model.lm_head(model.model.norm(middle[selected])).float(),gold)
    return ce,auxiliary,ce+RECIPE['coefficient']*auxiliary


def committed_state(state):
    if state.get('kind') != KIND or state['spec'].get('middle_supervision') != RECIPE: return False
    c,s = state['counters'],state['middle_supervision']; steps=c['update']
    if (s != dict(updates=steps,middle_gold_evaluations=c['supervised_tokens']) or
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


class MiddleSupervisionTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,batch=48,contrast=False,device='cuda',seed=42):
        if contrast: raise ValueError('No representation contrast or teacher in middle supervision')
        super().__init__(parent,sampler,binding,batch,False,device,seed)
        if self.model.config.get('dropout',0) != 0 or len(self.model.model.layers)<2:
            raise ValueError('Deterministic dropout0 native depth required')
        self.spec.update(kind=KIND,middle_supervision=copy.deepcopy(RECIPE))
        self.lineage.update(kind=KIND)
        self.middle_supervision = dict(updates=0,middle_gold_evaluations=0)
        self._step_in_progress = False

    def state_dict(self):
        if self._step_in_progress: raise ValueError('Cannot serialize uncommitted middle-supervision update')
        state=super().state_dict()
        state.update(kind=KIND,middle_supervision=copy.deepcopy(self.middle_supervision))
        return state

    def load(self,path):
        state=torch.load(Path(path),map_location=self.device,weights_only=False)
        if not committed_state(state): raise ValueError('Committed middle-supervision full state required')
        super().load(path); self.middle_supervision=copy.deepcopy(state['middle_supervision'])

    def step(self):
        if self._step_in_progress: raise ValueError('Interrupted update requires valid checkpoint resume')
        synchronize(self.device); started=time.monotonic(); self._step_in_progress=True
        rows=self.sampler.take(self.spec['batch']); wait=time.monotonic()-started
        ids,_=right_pad([r['input_ids'] for r in rows],self.device)
        targets=torch.full_like(ids,-100)
        for i,r in enumerate(rows): targets[i,:len(r['target_ids'])]=torch.tensor(r['target_ids'],device=self.device)
        gold=sum(r['teacher_tokens'] for r in rows)
        if int(targets.ne(-100).sum()) != gold: raise ValueError('Exact original gold mask required')
        self.optimizer.zero_grad(set_to_none=True)
        backend=SDPBackend.FLASH_ATTENTION if self.device.type=='cuda' else SDPBackend.MATH
        with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=self.device.type=='cuda'):
            ce,auxiliary,combined=middle_losses(self.model,ids,targets)
        if not all(bool(torch.isfinite(v)) for v in (ce,auxiliary,combined)):
            raise ValueError('Nonfinite final/middle original CE')
        combined.backward()
        gradient=torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
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
        self.middle_supervision['updates']+=1
        self.middle_supervision['middle_gold_evaluations']+=gold
        self._step_in_progress=False; synchronize(self.device)
        return dict(**copy.deepcopy(self.counters),middle_supervision=copy.deepcopy(self.middle_supervision),
            CE_loss=float(ce.detach()),middle_CE_loss=float(auxiliary.detach()),combined_loss=float(combined.detach()),
            gradient_norm=float(gradient),lr=self.optimizer.param_groups[0]['lr'],
            CE_targets_this_update=gold,middle_gold_evaluations_this_update=gold,
            physical_inputs_this_update=ids.numel(),decoder_forwards_this_update=1,
            seconds=time.monotonic()-started,data_wait_seconds=wait,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),original_windows_this_update=len(rows),
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])
