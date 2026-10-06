"""One original logical update; reduce PAD work with length-grouped forwards.

No reordered sampler or updates: original teachers and the single global
CE denominator, Adam update, clip and token schedule remain the same. Floating
point accumulation can differ; this is not a bit-identical old CUDA kernel.
"""
import copy
import hashlib
import json
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend, sdpa_kernel
from jmicro.training import synchronize
from base_kv_allocation_trainer import FreshKVAllocationTrainer
from natural_context_contrast_trainer import right_pad, right_padded_hidden

KIND = 'fresh_native_KV_allocation_CE_length_grouped_single_update_v1'


def length_groups(rows):
    groups = {}
    for row in rows:
        n = len(row['input_ids'])
        if not 1 <= n <= 1024 or len(row['target_ids']) != n:
            raise ValueError('Matching original context/mask length<=1024 required')
        groups.setdefault(1 << (n-1).bit_length(), []).append(row)
    return [groups[key] for key in sorted(groups)]


def grouped_backward(model, rows, device):
    """Sum group CE over the original entire logical batch denominator."""
    device = torch.device(device)
    denominator = sum(r['teacher_tokens'] for r in rows)
    if denominator <= 0:
        raise ValueError('Nonempty original teacher batch required')
    backend = SDPBackend.FLASH_ATTENTION if device.type == 'cuda' else SDPBackend.MATH
    loss_total, physical, groups = 0.,0,0
    for group in length_groups(rows):
        ids,_ = right_pad([r['input_ids'] for r in group],device)
        targets = torch.full(ids.shape,-100,dtype=torch.long)
        for i,row in enumerate(group):
            targets[i,:len(row['target_ids'])] = torch.tensor(row['target_ids'])
        targets = targets.to(device)
        selected = targets.ne(-100)
        if int(selected.sum()) != sum(r['teacher_tokens'] for r in group):
            raise ValueError('Original group teacher mask count differs')
        with sdpa_kernel(backend),torch.autocast(device.type,dtype=torch.bfloat16,enabled=device.type=='cuda'):
            hidden = right_padded_hidden(model,ids)
            logits = model.lm_head(hidden[selected]).float()
            loss = F.cross_entropy(logits,targets[selected],reduction='sum')/denominator
            if not torch.isfinite(loss):
                raise ValueError('Finite weighted original group CE required')
            loss.backward()
        loss_total += float(loss.detach())
        physical += ids.numel()
        groups += 1
        # Release the last projection before allocating the next group.
        del hidden,logits,loss,ids,targets,selected
    return loss_total,physical,groups


class BucketedKVAllocationTrainer(FreshKVAllocationTrainer):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.spec.update(kind=KIND,forward_policy='original_logical_batch_power_of_two_length_groups',
            loss_reduction='sum_each_group_over_total_original_teachers_before_one_global_clip_and_Adam')
        self.lineage['kind'] = KIND

    def state_dict(self):
        state = super().state_dict()
        state['kind'] = KIND
        return state

    def step(self):
        if not self.model.training:
            raise ValueError('model.train required for original teacher learning')
        synchronize(self.device)
        started = time.monotonic()
        rows = self.sampler.take(self.spec['batch'])
        data_wait = time.monotonic()-started
        if any(r['prefix_ids'] or r['suffix_ids'] for r in rows):
            raise ValueError('No auxiliary pair extraction')
        self.optimizer.zero_grad(set_to_none=True)
        loss,physical,groups = grouped_backward(self.model,rows,self.device)
        supervised = sum(r['teacher_tokens'] for r in rows)
        gradient = torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        if not 0 < float(gradient) < float('inf'):
            raise ValueError('Finite nonzero native gradient required')
        lr = self.scheduler.prepare(supervised)
        self.optimizer.step()
        self.scheduler.commit(supervised)
        self.counters['update'] += 1
        for key,value in dict(supervised_tokens=supervised,CE_input_tokens=sum(len(r['input_ids']) for r in rows),
                physical_input_tokens=physical,original_body_bytes=sum(r['teacher_body_bytes'] for r in rows)).items():
            self.counters[key] += value
        for row in rows:
            self.counters['source_teachers'][row['source']] += row['teacher_tokens']
            self.counters['source_EOS'][row['source']] += row['original_EOS_targets']
        if self.counters['source_teachers'] != self.sampler.consumed or self.scheduler.tokens != self.counters['supervised_tokens']:
            raise ValueError('Original completed teacher/source/schedule accounting differs')
        stream = json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        synchronize(self.device)
        return dict(**copy.deepcopy(self.counters),CE_loss=loss,combined_loss=loss,gradient_norm=float(gradient),
            CE_targets_this_update=supervised,auxiliary_inputs_this_update=0,physical_inputs_this_update=physical,
            original_windows_this_update=len(rows),forward_length_groups=groups,
            original_flat_padded_physical_inputs=len(rows)*max(len(r['input_ids']) for r in rows),
            seconds=time.monotonic()-started,data_wait_seconds=data_wait,lr=lr,
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])
