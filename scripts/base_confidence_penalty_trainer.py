"""Original next-token CE plus fixed KL(prediction || full-vocabulary uniform).

No softened gold labels, teacher, extra forward, parameter or inference change.
The confidence objective evaluates the same gold positions, not new corpus.
"""
import copy
import hashlib
import json
import math
from pathlib import Path
import time
import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from natural_context_contrast_corpus import NaturalCorpusTrainer
from natural_context_contrast_trainer import right_pad,right_padded_hidden
from jmicro.training import synchronize

KIND='native_original_CE_confidence_penalty_reverse_uniform_KL_v1'
RECIPE=dict(coefficient=.1,temperature=1.,
    target='original_hard_body_and_EOS_targets_unchanged',
    regularizer='mean_KL_student_full_native_vocab_prediction_to_uniform',
    loss='original_mean_CE_plus_0.1_times_log_vocab_minus_mean_prediction_entropy',
    gold_CE_coefficient=1.,mask='only_original_supervised_positions',
    annealing=False,entropy_threshold=None,extra_parameters=0,decoder_forwards=1,
    optimizer='fresh_AdamW_lr1e-5_wd0.1_constant',final_clip_norm=1.,
    inference='unchanged_full_native_depth_greedy')


def uniform_confidence_loss(logits,targets):
    if (logits.ndim!=2 or targets.shape!=(len(logits),) or not len(logits) or
        logits.shape[1]<2 or bool((targets<0).any()) or bool((targets>=logits.shape[1]).any())):
        raise ValueError('Original selected nonempty hard-gold positions required')
    scores=logits.float()
    ce=F.cross_entropy(scores,targets)
    logp=F.log_softmax(scores,dim=-1)
    entropy=-(logp.exp()*logp).sum(-1).mean()
    penalty=math.log(scores.shape[-1])-entropy
    return ce,penalty,ce+RECIPE['coefficient']*penalty,entropy


def confidence_losses(model,ids,targets):
    if ids.shape!=targets.shape or not bool(targets.ne(-100).any()):
        raise ValueError('Aligned nonempty original gold required')
    selected=targets.ne(-100)
    logits=model.lm_head(right_padded_hidden(model,ids)[selected])
    return uniform_confidence_loss(logits,targets[selected])


def committed_state(state):
    if state.get('kind')!=KIND or state['spec'].get('confidence_penalty')!=RECIPE: return False
    c,s=state['counters'],state['confidence_penalty']; steps=c['update']
    if (s!=dict(updates=steps,positions=c['supervised_tokens']) or
        steps!=state['scheduler']['last_epoch'] or
        any(int(v['step'])!=steps for v in state['optimizer']['state'].values()) or
        c['supervised_tokens']!=sum(c['source_teachers'].values()) or
        c['source_teachers']!=state['sampler']['consumed'] or
        c['auxiliary_input_tokens'] or c['auxiliary_pairs'] or c['auxiliary_digest']!='0'*64): return False
    def finite(value):
        if isinstance(value,torch.Tensor): return bool(torch.isfinite(value).all())
        if isinstance(value,dict): return all(finite(v) for v in value.values())
        if isinstance(value,(list,tuple)): return all(finite(v) for v in value)
        return True
    return finite(state['model']) and finite(state['optimizer'])


class ConfidencePenaltyTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,batch=48,contrast=False,device='cuda',seed=42):
        if contrast: raise ValueError('No contrastive or teacher objective')
        super().__init__(parent,sampler,binding,batch,False,device,seed)
        if self.model.config.get('dropout',0)!=0: raise ValueError('Native deterministic dropout0 required')
        self.spec.update(kind=KIND,confidence_penalty=copy.deepcopy(RECIPE))
        self.lineage.update(kind=KIND)
        self.confidence_penalty=dict(updates=0,positions=0)
        self._step_in_progress=False

    def state_dict(self):
        if self._step_in_progress: raise ValueError('Cannot serialize uncommitted confidence update')
        state=super().state_dict(); state.update(kind=KIND,confidence_penalty=copy.deepcopy(self.confidence_penalty))
        return state

    def load(self,path):
        state=torch.load(Path(path),map_location=self.device,weights_only=False)
        if not committed_state(state): raise ValueError('Committed confidence full state required')
        super().load(path); self.confidence_penalty=copy.deepcopy(state['confidence_penalty'])

    def step(self):
        if self._step_in_progress: raise ValueError('Interrupted update requires valid checkpoint resume')
        synchronize(self.device); started=time.monotonic(); self._step_in_progress=True
        rows=self.sampler.take(self.spec['batch']); wait=time.monotonic()-started
        ids,_=right_pad([r['input_ids'] for r in rows],self.device)
        targets=torch.full_like(ids,-100)
        for i,r in enumerate(rows): targets[i,:len(r['target_ids'])]=torch.tensor(r['target_ids'],device=self.device)
        gold=sum(r['teacher_tokens'] for r in rows)
        if int(targets.ne(-100).sum())!=gold: raise ValueError('Exact original gold mask required')
        self.optimizer.zero_grad(set_to_none=True)
        backend=SDPBackend.FLASH_ATTENTION if self.device.type=='cuda' else SDPBackend.MATH
        with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=self.device.type=='cuda'):
            ce,penalty,combined,entropy=confidence_losses(self.model,ids,targets)
        if not all(bool(torch.isfinite(v)) for v in (ce,penalty,combined,entropy)):
            raise ValueError('Nonfinite original CE/confidence KL/entropy')
        combined.backward()
        gradient=torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        self.optimizer.step(); self.scheduler.step(); self.counters['update']+=1
        for k,v in dict(supervised_tokens=gold,CE_input_tokens=sum(len(r['input_ids']) for r in rows),
            physical_input_tokens=ids.numel(),original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items(): self.counters[k]+=v
        for r in rows:
            self.counters['source_teachers'][r['source']]+=r['teacher_tokens']
            self.counters['source_EOS'][r['source']]+=r['original_EOS_targets']
        if self.counters['source_teachers']!=self.sampler.consumed: raise ValueError('Committed source cursor differs')
        stream=json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest']=hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        self.confidence_penalty['updates']+=1; self.confidence_penalty['positions']+=gold
        self._step_in_progress=False; synchronize(self.device)
        return dict(**copy.deepcopy(self.counters),confidence_penalty=copy.deepcopy(self.confidence_penalty),
            CE_loss=float(ce.detach()),confidence_KL_loss=float(penalty.detach()),prediction_entropy=float(entropy.detach()),
            combined_loss=float(combined.detach()),gradient_norm=float(gradient),lr=self.optimizer.param_groups[0]['lr'],
            CE_targets_this_update=gold,confidence_positions_this_update=gold,decoder_forwards_this_update=1,
            physical_inputs_this_update=ids.numel(),seconds=time.monotonic()-started,data_wait_seconds=wait,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),original_windows_this_update=len(rows),
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])
