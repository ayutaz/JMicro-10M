"""Plan131: complete Assistant targets, teacher-sized updates and frozen resume.

This adds a separately identified diagnostic path and leaves the native model,
existing Trainer and adopted-Base gates unchanged.
"""
import hashlib
from collections import defaultdict
import json
import math
from pathlib import Path
import time
from types import SimpleNamespace

import numpy as np
import torch
from torch.nn import functional as F
from torch.nn.attention import sdpa_kernel, SDPBackend

from jmicro.assistant_sampler import AssistantSampler
from jmicro.experiment import ROOT, sha256
from jmicro.training import Trainer, autocast, implementation_hashes, synchronize


def teacher_lr(completed, current, budget, peak=1e-4):
    if completed < 0 or current <= 0 or budget <= 0:
        raise ValueError('Invalid teacher progress')
    progress = min(1., (completed + current/2)/budget)
    factor = progress/.05 if progress < .05 else 1. if progress <= .90 else 1.-.9*(progress-.90)/.10
    return peak*factor


class TeacherBudgetSampler(AssistantSampler):
    def __init__(self, records, tokenizer, context, seed, teacher_budget, update_teachers=512, microbatch=32):
        if (type(teacher_budget) is not int or teacher_budget <= 0 or type(update_teachers) is not int
                or update_teachers < 1 or type(microbatch) is not int or microbatch < 1):
            raise ValueError('Positive frozen teacher budget, update threshold and microbatch required')
        super().__init__(records, tokenizer, context, seed)
        selected = {}
        targets_by_document=defaultdict(set)
        for window in self.windows:
            targets_by_document[window['doc_id']].add(window['target_message_index'])
        for record in records:
            if 'target_message_indices' not in record:
                continue
            indices = record['target_message_indices']
            available = targets_by_document[record['doc_id']]
            if (not isinstance(indices,list) or not indices or any(type(i) is not int for i in indices)
                    or len(set(indices)) != len(indices) or not set(indices).issubset(available)):
                raise ValueError('Selected indices must uniquely identify existing Assistant targets')
            selected[record['doc_id']] = set(indices)
        self.windows = [w for w in self.windows if w['doc_id'] not in selected
            or w['target_message_index'] in selected[w['doc_id']]]
        if not self.windows:
            raise ValueError('No selected TRAIN targets')
        digest = hashlib.sha256()
        self.lengths = []
        for window in self.windows:
            teachers = window['labels'][window['labels'] != -100]
            if not 2 <= len(teachers) <= 65:
                raise ValueError('Teacher target must fit frozen 2-65 range')
            self.lengths.append(len(teachers))
            digest.update(json.dumps([window['doc_id'],window['target_message_index']],ensure_ascii=False).encode())
            digest.update(window['ids'].astype('<i8').tobytes())
            digest.update(window['labels'].astype('<i8').tobytes())
        self.binding = digest.hexdigest()
        self.teacher_budget, self.update_teachers, self.microbatch = teacher_budget, update_teachers, microbatch
        self._shuffle()

    def state_dict(self):
        return dict(super().state_dict(), teacher_budget=self.teacher_budget,
            update_teachers=self.update_teachers,microbatch=self.microbatch,
            protocol='teacher-complete-update-v1')

    def load_state_dict(self,state):
        if any(state.get(k) != getattr(self,k) for k in ('teacher_budget','update_teachers','microbatch')):
            raise ValueError('Frozen teacher batching/budget differs')
        if state.get('protocol') != 'teacher-complete-update-v1' or state['teacher_tokens'] > self.teacher_budget+64:
            raise ValueError('Invalid teacher protocol/overshoot')
        super().load_state_dict(state)

    def next_update(self):
        if self.teacher_tokens >= self.teacher_budget:
            raise ValueError('Teacher budget exhausted')
        threshold = min(self.update_teachers,self.teacher_budget-self.teacher_tokens)
        arrays, total, body_bytes = [], 0, 0
        while total < threshold:
            if self.position == len(self.windows):
                self.epoch += 1
                self.position = 0
                self._shuffle()
            window = self.windows[int(self.order[self.position])]
            ids,labels = window['ids'],window['labels']
            teachers = labels[labels != -100]
            arrays.append((ids[:-1],labels[1:]))
            total += len(teachers)
            body_bytes += int(self.byte_lengths[teachers].sum())
            self.series_tokens += len(ids)
            self.input_tokens += len(ids)-1
            self.teacher_tokens += len(teachers)
            self.eot_teachers += 1
            self.examples += 1
            self.removed_turns += window['removed_turns']
            self.position += 1
        batches=[]
        for start in range(0,len(arrays),self.microbatch):
            x = np.zeros((self.microbatch,self.context),dtype=np.int64)
            y = np.full_like(x,-100)
            for row,(inputs,labels) in enumerate(arrays[start:start+self.microbatch]):
                x[row,:len(inputs)],y[row,:len(labels)] = inputs,labels
            batches.append((torch.from_numpy(x),torch.from_numpy(y)))
            self.physical_tokens += x.size
        assert sum(int(y.ne(-100).sum()) for _,y in batches) == total
        assert threshold <= total < threshold+65
        return batches,total,body_bytes


class TeacherChatTrainer(Trainer):
    def __init__(self,parent,parent_ref,records,tokenizer,dataset_directory,spec,teacher_budget,device='cpu'):
        if parent['implementation_sha256'] != implementation_hashes():
            raise ValueError('Frozen native implementation differs')
        if (spec.get('sampler') != 'document' or spec.get('training_fast_path') or spec.get('compile')
                or spec.get('backend') != 'math' or spec.get('accumulation') != 1):
            raise ValueError('Use masked math/native teacher diagnostic path')
        sampler = TeacherBudgetSampler(records,tokenizer,spec['context'],spec['seed'],teacher_budget,
            spec.get('update_teachers',512),spec['batch'])
        directory=Path(dataset_directory)
        source=SimpleNamespace(directory=directory,split='train',manifest=dict(vocab_size=tokenizer.vocab_size),
            tokens=np.zeros(spec['context']+1,dtype='<u2'),index=[dict(offset=0,body_tokens=spec['context']-1)],
            byte_lengths=sampler.byte_lengths)
        if sha256(Path(parent_ref['path'])) != parent_ref['sha256']:
            raise ValueError('Parent checkpoint hash differs')
        actual_spec=dict(spec,teacher_chat=dict(protocol='teacher-complete-update-v1',budget=teacher_budget,
            data_binding=sampler.binding,parent_sha256=parent_ref['sha256'],
            trainer_sha256=sha256(Path(__file__)),source_sampler_sha256=sha256(ROOT/'src/jmicro/assistant_sampler.py'),
            LR_policy='midpoint_teachers_linear5_stable85_linear10_floor10percent'))
        super().__init__(parent['model_config'],source,actual_spec,device)
        self.model.load_state_dict(parent['model'],strict=True)
        self.sampler=sampler
        self.scheduler=torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:1.)
        self.lineage=dict(kind='teacher-normalized-assistant-sft',parent_update=0,parent_tokens=0,
            base_checkpoint=dict(parent_ref),base_update=parent['update'],base_tokens=parent['tokens'],
            base_supervised_tokens=parent['supervised_tokens'],base_token_digest=parent['token_digest'],
            optimizer_policy='fresh',RNG_policy='new frozen seed',route='direct-sft',
            Base_adopted=False,Chat_adopted=False)
        assert not self.optimizer.state
        self._update_in_progress=False

    def step(self,check=lambda:None):
        if self._update_in_progress:
            raise ValueError('Restore a completed checkpoint before continuing a failed update')
        check();synchronize(self.device);started=time.perf_counter()
        self._update_in_progress=True
        before=self.sampler.teacher_tokens
        batches,denominator,body_bytes=self.sampler.next_update()
        lr=teacher_lr(before,denominator,self.sampler.teacher_budget,self.spec['lr'])
        for group in self.optimizer.param_groups: group['lr']=lr
        data_wait=time.perf_counter()-started
        self.optimizer.zero_grad(set_to_none=True);self.model.train()
        nll=0.;digest=hashlib.sha256(bytes.fromhex(self.token_digest))
        for x,y in batches:
            check()
            digest.update(x.numpy().astype('<i8').tobytes());digest.update(y.numpy().astype('<i8').tobytes())
            x,y=x.to(self.device),y.to(self.device)
            with sdpa_kernel(SDPBackend.MATH),autocast(self.device,self.spec['dtype']):
                logits=self.forward(x,attention_mask=x.ne(0)).logits
                loss=F.cross_entropy(logits.reshape(-1,logits.shape[-1]),y.reshape(-1),
                    ignore_index=-100,reduction='sum')/denominator
            loss.backward();nll+=float(loss.detach())
        norm=torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        if not math.isfinite(nll): raise ValueError('Nonfinite teacher loss')
        self.optimizer.step();self.scheduler.step()
        for group in self.optimizer.param_groups: group['lr']=lr
        self.scheduler._last_lr=[lr]*len(self.optimizer.param_groups)
        self.update+=1;self.tokens=self.sampler.input_tokens;self.supervised_tokens=self.sampler.teacher_tokens
        self.body_bytes+=body_bytes;self.token_digest=digest.hexdigest()
        synchronize(self.device);seconds=time.perf_counter()-started
        self._update_in_progress=False
        return dict(update=self.update,loss=nll,gradient_norm=float(norm),lr=lr,seconds=seconds,
            data_wait_seconds=data_wait,teachers_this_update=denominator,microbatches=len(batches),
            tokens_seen=self.tokens,supervised_tokens=self.supervised_tokens,body_bytes_seen=self.body_bytes,
            token_digest=self.token_digest,series_tokens=self.sampler.series_tokens,
            assistant_teacher_tokens=self.sampler.teacher_tokens,EOT_teachers=self.sampler.eot_teachers,
            valid_input_tokens=self.tokens,physical_input_tokens=self.sampler.physical_tokens,
            padding_input_tokens=self.sampler.physical_tokens-self.tokens,examples=self.sampler.examples,
            removed_turns=self.sampler.removed_turns,teacher_tokens_per_second=denominator/seconds)

    def save(self,path):
        if self._update_in_progress or self.tokens!=self.sampler.input_tokens or self.supervised_tokens!=self.sampler.teacher_tokens:
            raise ValueError('Cannot save a partially completed teacher update')
        return super().save(path)

    def load(self,path,*,decay_branch=False):
        if decay_branch: raise ValueError('Teacher recipe must resume unchanged')
        expected=dict(self.lineage)
        super().load(path)
        if self.lineage != expected or self.tokens != self.sampler.input_tokens or self.supervised_tokens != self.sampler.teacher_tokens:
            raise ValueError('Teacher lineage or completed-update counters differ')
        self._update_in_progress=False
