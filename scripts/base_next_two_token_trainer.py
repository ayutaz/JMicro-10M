"""Original native CE plus one train-only contextual next-two-token head.

The auxiliary head is absent from inference. Original body/EOS teacher
positions remain the100M denominator; auxiliary positions are separate.
"""
import copy
import hashlib
import json
from pathlib import Path
import time

import torch
from torch import nn
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.model import Block,RMSNorm
from jmicro.training import restore_rng,synchronize
from natural_context_contrast_corpus import NaturalCorpusTrainer,GENRES
from natural_context_contrast_trainer import host,right_pad,right_padded_hidden

KIND='native_original_TRAIN_CE_next_two_contextual_auxiliary_v1'
COEFFICIENT=.1
AUXILIARY_SEED=19042


def next_two_targets(targets):
    if targets.ndim!=2 or targets.shape[1]<1:
        raise ValueError('Original two-dimensional teacher mask required')
    output=torch.full_like(targets,-100)
    eligible=targets[:,:-1].ne(-100)&targets[:,1:].ne(-100)
    output[:,:-1]=torch.where(eligible,targets[:,1:],-100)
    return output


class NextTwoHead(nn.Module):
    def __init__(self,config):
        super().__init__()
        self.block=Block(config)
        self.norm=RMSNorm(config['hidden_size'],config['rms_norm_eps'])

    def forward(self,hidden):
        positions=torch.arange(hidden.shape[1],device=hidden.device)[None].expand(hidden.shape[0],-1)
        transformed,_=self.block(hidden,positions,None,None,causal=True)
        return self.norm(transformed)


class NextTwoTokenTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,batch=48,contrast=False,device='cuda',seed=42):
        if contrast:raise ValueError('No contrastive loss in fixed next-two objective')
        super().__init__(parent,sampler,binding,batch,False,device,seed)
        # CPU-only local initialization preserves both native CPU and CUDA RNG.
        with torch.random.fork_rng(devices=[]):
            self.future_head=NextTwoHead(self.model.config)
            generator=torch.Generator(device='cpu').manual_seed(AUXILIARY_SEED)
            for module in self.future_head.modules():
                if isinstance(module,nn.Linear):
                    nn.init.normal_(module.weight,mean=0,std=self.model.config['initializer_std'],generator=generator)
                elif isinstance(module,RMSNorm):
                    nn.init.constant_(module.weight,self.model.config['norm_initial_gain'])
        self.future_head=self.future_head.to(self.device).train()
        self.all_parameters=[*self.model.parameters(),*self.future_head.parameters()]
        self.optimizer=torch.optim.AdamW(self.all_parameters,lr=1e-5,weight_decay=.1)
        self.scheduler=torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:1.)
        native=sum(p.numel() for p in self.model.parameters())
        auxiliary=sum(p.numel() for p in self.future_head.parameters())
        self.spec.update(kind=KIND,next_two_coefficient=COEFFICIENT,auxiliary_seed=AUXILIARY_SEED,
            auxiliary_policy='one_native_contextual_block_and_final_RMS_on_original_hidden_shared_native_unembedding',
            auxiliary_mask='current_original_target_and_next_original_target_both_unmasked_same_window',
            native_parameters=native,train_only_parameters=auxiliary,total_training_parameters=native+auxiliary,
            inference_policy='original_native_model_only_no_auxiliary_head_no_decode_changes')
        self.lineage.update(kind=KIND,auxiliary_weights_role='fresh_train_only_not_used_at_inference')
        self.counters.update(next_two_teacher_positions=0,next_two_EOS_targets=0,next_two_body_bytes=0,
            next_two_target_mass=0.,auxiliary_physical_hidden_positions=0,
            source_next_two_teachers=dict.fromkeys(GENRES,0),source_next_two_EOS=dict.fromkeys(GENRES,0))

    def state_dict(self):
        state=super().state_dict();state['kind']=KIND
        state['auxiliary_model']=self.future_head.state_dict()
        return state

    def load(self,path):
        state=torch.load(Path(path),map_location=self.device,weights_only=False)
        if any(state[k]!=self.state_dict()[k] for k in ('kind','spec','binding','lineage','model_config')):
            raise ValueError('Original source/parent/fixed next-two objective binding differs')
        if 'auxiliary_model' not in state:
            raise ValueError('Actual saved train-only next-two head is required')
        counters=state['counters']
        if (counters['supervised_tokens']!=sum(counters['source_teachers'].values())
                or counters['source_teachers']!=state['sampler']['consumed']
                or counters['next_two_teacher_positions']!=sum(counters['source_next_two_teachers'].values())
                or counters['next_two_EOS_targets']!=sum(counters['source_next_two_EOS'].values())
                or not 0<=counters['next_two_teacher_positions']<=counters['supervised_tokens']
                or counters['next_two_target_mass']!=COEFFICIENT*counters['next_two_teacher_positions']
                or counters['auxiliary_input_tokens'] or counters['auxiliary_pairs']):
            raise ValueError('Completed original/next-two teacher accounting differs')
        self.model.load_state_dict(state['model'],strict=True)
        self.future_head.load_state_dict(state['auxiliary_model'],strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters=copy.deepcopy(counters)
        restore_rng(host(state['RNG']))

    def step(self):
        if not self.model.training or not self.future_head.training:
            raise ValueError('Native and train-only model.train required')
        synchronize(self.device);started=time.monotonic()
        rows=self.sampler.take(self.spec['batch']);data_wait=time.monotonic()-started
        ids,_=right_pad([r['input_ids'] for r in rows],self.device)
        labels=torch.full(ids.shape,-100,dtype=torch.long)
        for index,row in enumerate(rows):labels[index,:len(row['target_ids'])]=torch.tensor(row['target_ids'])
        future_cpu=next_two_targets(labels)
        labels=labels.to(self.device);future=future_cpu.to(self.device)
        selected=labels.ne(-100);future_selected=future.ne(-100)
        native_teachers=sum(r['teacher_tokens'] for r in rows);next_two_teachers=int(future_selected.sum())
        if int(selected.sum())!=native_teachers:raise ValueError('Original body/EOS teacher count differs')
        self.optimizer.zero_grad(set_to_none=True)
        backend=SDPBackend.FLASH_ATTENTION if self.device.type=='cuda' else SDPBackend.MATH
        with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=self.device.type=='cuda'):
            hidden=right_padded_hidden(self.model,ids)
            ce=F.cross_entropy(self.model.lm_head(hidden[selected]).float(),labels[selected])
            future_loss=ce.new_zeros(())
            if next_two_teachers:
                transformed=self.future_head(hidden)
                future_loss=F.cross_entropy(self.model.lm_head(transformed[future_selected]).float(),future[future_selected])
            total=ce+COEFFICIENT*future_loss
            if not torch.isfinite(total) or not torch.isfinite(ce) or not torch.isfinite(future_loss):
                raise ValueError('Finite original and next-two CE required')
            total.backward()
        auxiliary_gradient=float(torch.stack([p.grad.detach().float().norm() for p in self.future_head.parameters()
            if p.grad is not None]).norm()) if next_two_teachers else 0.
        if next_two_teachers and not 0<auxiliary_gradient<float('inf'):
            raise ValueError('Finite nonzero actual next-two head gradient required')
        gradient=torch.nn.utils.clip_grad_norm_(self.all_parameters,1.,error_if_nonfinite=True)
        self.optimizer.step();self.scheduler.step();self.counters['update']+=1
        for key,value in dict(supervised_tokens=native_teachers,CE_input_tokens=sum(len(r['input_ids']) for r in rows),
            physical_input_tokens=ids.numel(),original_body_bytes=sum(r['teacher_body_bytes'] for r in rows),
            next_two_teacher_positions=next_two_teachers,next_two_EOS_targets=int(future.eq(3).sum()),
            auxiliary_physical_hidden_positions=ids.numel() if next_two_teachers else 0).items():self.counters[key]+=value
        for index,row in enumerate(rows):
            source=row['source'];future_ids=future_cpu[index].tolist()
            self.counters['source_teachers'][source]+=row['teacher_tokens']
            self.counters['source_EOS'][source]+=row['original_EOS_targets']
            self.counters['source_next_two_teachers'][source]+=sum(i!=-100 for i in future_ids)
            self.counters['source_next_two_EOS'][source]+=future_ids.count(3)
            self.counters['next_two_body_bytes']+=sum(self.sampler.byte_lengths[i] for i in future_ids if i>=8)
        if self.counters['source_teachers']!=self.sampler.consumed:raise ValueError('Completed original source quotas differ')
        self.counters['next_two_target_mass']=COEFFICIENT*self.counters['next_two_teacher_positions']
        stream=json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest']=hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters),CE_loss=float(ce.detach()),next_two_CE_loss=float(future_loss.detach()),
            combined_loss=float(total.detach()),next_two_coefficient=COEFFICIENT,next_two_head_gradient_norm=auxiliary_gradient,
            gradient_norm=float(gradient),CE_targets_this_update=native_teachers,next_two_targets_this_update=next_two_teachers,
            auxiliary_inputs_this_update=0,physical_inputs_this_update=ids.numel(),original_windows_this_update=len(rows),
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),seconds=time.monotonic()-started,
            data_wait_seconds=data_wait,lr=self.optimizer.param_groups[0]['lr'],
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])
