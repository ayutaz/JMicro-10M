"""Typed native CE plus training-only scalar progress supervision."""
import copy
import hashlib
import json
import math
from pathlib import Path
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel

from jmicro.document_progress import ARMS,POLICY,COEFFICIENT,ProgressHead,progress_targets,progress_loss
from jmicro.evaluation_boundary import require_digest
from jmicro.model import JMicroModel
from jmicro.training import restore_rng
from base_fim_trainer import finite,valid_rng
from context_likelihood_trainer import validate_material
from natural_context_contrast_corpus import NaturalCorpusTrainer,GENRES
from natural_context_contrast_trainer import host,right_pad,right_padded_hidden,synchronize

KIND = 'native_original_CE_document_progress_scalar_L1_v1'
OPTIMIZER_POLICY = 'fresh_AdamW_original_coordinates_plus_train_only_scalar_head'


def committed_state(state):
    try:
        spec,c,s,opt = (state[k] for k in ('spec','counters','sampler','optimizer'))
        steps,teachers = c['update'],c['supervised_tokens']
        enabled = spec['progress_arm'] == 'document_progress'
        if (state['kind'] != KIND or spec['kind'] != KIND or state['lineage']['kind'] != KIND
                or spec['progress_arm'] not in ARMS or spec['progress_policy'] != POLICY
                or spec['inference_policy'] != 'unchanged_original_native_model_no_progress_head'
                or spec['gradient_clip_policy'] != ('all_native_and_progress_head' if enabled else 'exact_original_coordinate_reduction')
                or state['lineage']['optimizer_policy'] != OPTIMIZER_POLICY
                or state['lineage']['progress_weights_role'] != 'fresh_train_only_never_inference'
                or spec['contrast'] is not False or spec['seed'] != s['seed'] or spec['goals'] != s['goals']
                or spec['original_material_binding'] != s['binding']
                or any(type(c[k]) is not int or c[k] < 0 for k in ('update','supervised_tokens',
                    'CE_input_tokens','physical_input_tokens','original_body_bytes',
                    'progress_label_positions','progress_learning_positions','progress_zero_EOS_labels'))
                or (steps == 0) != (teachers == 0) or steps != state['scheduler']['last_epoch']
                or c['source_teachers'] != s['consumed'] or teachers != sum(c['source_teachers'].values())
                or not c['physical_input_tokens'] >= c['CE_input_tokens'] >= teachers
                or c['auxiliary_pairs'] != 0 or c['auxiliary_input_tokens'] != 0 or c['auxiliary_digest'] != '0'*64
                or c['progress_label_positions'] != teachers
                or c['progress_learning_positions'] != (teachers if enabled else 0)
                or c['progress_source_labels'] != c['source_teachers']
                or c['progress_zero_EOS_labels'] != sum(c['source_EOS'].values())
                or not math.isfinite(c['progress_target_sum']) or not 0 <= c['progress_target_sum'] <= teachers
                or set(c['source_EOS']) != set(GENRES)
                or any(type(c['source_EOS'][g]) is not int or not 0 <= c['source_EOS'][g] <= c['source_teachers'][g] for g in GENRES)
                or (not steps <= s['windows_emitted'] <= steps*spec['batch'] if steps else s['windows_emitted'] != 0)):
            return False
        validate_material(s)
        require_digest(c['token_digest'])
        require_digest(c['progress_target_digest'])
        if any(k.endswith('_research') for k in state['model_config']) or state['model_config']['qk_norm_type'] != 'none':
            return False
        with torch.device('meta'):
            model = JMicroModel(state['model_config'])
            head = ProgressHead(state['model_config']['hidden_size'])
        expected = model.state_dict()
        h = state['progress_head']
        if (set(expected) != set(state['model']) or set(h) != {'weight'}
                or any(not isinstance(state['model'][k],torch.Tensor) or state['model'][k].shape != v.shape
                    or state['model'][k].dtype != v.dtype for k,v in expected.items())
                or h['weight'].shape != head.weight.shape or h['weight'].dtype != torch.float32
                or (not enabled and torch.count_nonzero(h['weight']))
                or sum(p.numel() for p in model.parameters()) != spec['native_parameters']
                or spec['native_parameters'] != state['model_config']['expected_parameter_count']
                or sum(p.numel() for p in head.parameters()) != spec['train_only_parameters']
                or spec['total_training_parameters'] != spec['native_parameters']+spec['train_only_parameters']
                or not torch.equal(state['model']['lm_head.weight'],state['model']['model.embed_tokens.weight'])):
            return False
        groups,parameters = opt['param_groups'],[*model.parameters(),*head.parameters()]
        if len(groups) != 1:
            return False
        group = groups[0]
        identifiers = group['params']
        if (len(identifiers) != len(parameters) or len(set(identifiers)) != len(identifiers)
                or group['lr'] != 1e-5 or group['weight_decay'] != .1
                or tuple(group['betas']) != (.9,.999) or group['eps'] != 1e-8
                or state['scheduler']['_last_lr'] != [1e-5] or state['scheduler']['base_lrs'] != [1e-5]
                or state['scheduler']['_step_count'] != steps+1):
            return False
        if steps:
            if set(opt['state']) != set(identifiers):
                return False
            for identifier,parameter in zip(identifiers,parameters,strict=True):
                adam = opt['state'][identifier]
                if (float(adam['step']) != steps or adam['exp_avg'].shape != parameter.shape
                        or adam['exp_avg_sq'].shape != parameter.shape
                        or adam['exp_avg'].dtype != parameter.dtype or adam['exp_avg_sq'].dtype != parameter.dtype):
                    return False
        elif opt['state']:
            return False
        return valid_rng(state['RNG']) and finite(state)
    except (KeyError,TypeError,ValueError,RuntimeError,OverflowError,AttributeError):
        return False


class DocumentProgressTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,batch=48,device='cuda',seed=42,arm='document_progress'):
        if arm not in ARMS:
            raise ValueError('Explicit original CE or scalar progress arm required')
        super().__init__(parent,sampler,binding,batch=batch,contrast=False,device=device,seed=seed)
        self.progress_head = ProgressHead(self.model.config['hidden_size'],device=self.device).train()
        native = sum(p.numel() for p in self.model.parameters())
        extra = sum(p.numel() for p in self.progress_head.parameters())
        if (binding.get('weights_role') not in ('verification_only','scientific_document_progress25M')
                or (binding['weights_role'] != 'verification_only' and (native != 10001152 or extra != 256
                    or sampler.goals != dict(web=18750000,textbook=5000000,story=1250000)))):
            raise ValueError('Exact declared native10M paired25M scientific role/count/goals required')
        self.all_parameters = [*self.model.parameters(),*self.progress_head.parameters()]
        self.optimizer = torch.optim.AdamW(self.all_parameters,lr=1e-5,weight_decay=.1)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer,lambda _:1.)
        self.spec.update(kind=KIND,progress_arm=arm,progress_policy=copy.deepcopy(POLICY),
            original_material_binding=copy.deepcopy(sampler.binding),native_parameters=native,
            train_only_parameters=extra,total_training_parameters=native+extra,
            gradient_clip_policy=('all_native_and_progress_head' if arm == 'document_progress' else 'exact_original_coordinate_reduction'),
            inference_policy='unchanged_original_native_model_no_progress_head')
        self.lineage.update(kind=KIND,optimizer_policy=OPTIMIZER_POLICY,
            progress_weights_role='fresh_train_only_never_inference')
        self.counters.update(progress_label_positions=0,progress_learning_positions=0,
            progress_zero_EOS_labels=0,progress_source_labels=dict.fromkeys(GENRES,0),
            progress_target_sum=0.,progress_target_digest='0'*64)
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress or not self.model.training or not self.progress_head.training:
            raise ValueError('Train mode and completed-update resume required')
        self._step_in_progress = True
        synchronize(self.device)
        started = time.monotonic()
        rows = self.sampler.take(self.spec['batch'])
        values = progress_targets(rows)
        data_wait = time.monotonic()-started
        ids,_ = right_pad([r['input_ids'] for r in rows],self.device)
        targets = torch.full_like(ids,-100)
        labels = torch.full(ids.shape,-1.,device=self.device,dtype=torch.float32)
        for i,(row,vector) in enumerate(zip(rows,values,strict=True)):
            targets[i,:len(row['target_ids'])] = torch.tensor(row['target_ids'],device=self.device)
            labels[i,:len(vector)] = torch.tensor(vector,device=self.device,dtype=torch.float32)
        self.optimizer.zero_grad(set_to_none=True)
        enabled = self.spec['progress_arm'] == 'document_progress'
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=self.device.type == 'cuda'):
            hidden = right_padded_hidden(self.model,ids)
            selected = targets.ne(-100)
            native_logits = self.model.lm_head(hidden[selected]).float()
            ce = F.cross_entropy(native_logits,targets[selected])
            auxiliary = progress_loss(self.progress_head(hidden[selected]),labels[selected])
            combined = ce+COEFFICIENT*(auxiliary if enabled else auxiliary*0.)
            if not all(torch.isfinite(v) for v in (ce,auxiliary,combined)):
                raise ValueError('Nonfinite original CE/progress loss')
            combined.backward()
        params = self.all_parameters if enabled else list(self.model.parameters())
        gradient = torch.nn.utils.clip_grad_norm_(params,1.,error_if_nonfinite=True)
        head_gradient = float(self.progress_head.weight.grad.abs().max())
        self.optimizer.step()
        self.scheduler.step()
        teachers = sum(r['teacher_tokens'] for r in rows)
        self.counters['update'] += 1
        for key,value in dict(supervised_tokens=teachers,
                CE_input_tokens=sum(len(r['input_ids']) for r in rows),physical_input_tokens=ids.numel(),
                original_body_bytes=sum(r['teacher_body_bytes'] for r in rows),
                progress_label_positions=teachers,progress_learning_positions=teachers if enabled else 0,
                progress_zero_EOS_labels=sum(r['original_EOS_targets'] for r in rows)).items():
            self.counters[key] += value
        for row in rows:
            self.counters['source_teachers'][row['source']] += row['teacher_tokens']
            self.counters['source_EOS'][row['source']] += row['original_EOS_targets']
            self.counters['progress_source_labels'][row['source']] += row['teacher_tokens']
        if self.counters['source_teachers'] != self.sampler.consumed:
            raise ValueError('Completed-update original source quota differs')
        stream = json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        progress_stream = json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['original_body_tokens'],
            r['input_start'],r['target_first'],r['target_end'],r['target_ids'],v) for r,v in zip(rows,values,strict=True)]).encode()
        self.counters['progress_target_digest'] = hashlib.sha256(bytes.fromhex(self.counters['progress_target_digest'])+progress_stream).hexdigest()
        progress_sum = sum(v for row in values for v in row if v >= 0)
        self.counters['progress_target_sum'] += progress_sum
        synchronize(self.device)
        result = dict(**copy.deepcopy(self.counters),CE_loss=float(ce.detach()),progress_loss=float(auxiliary.detach()),
            combined_loss=float(combined.detach()),gradient_norm=float(gradient),
            head_gradient_abs_max_after_clip=head_gradient,head_weight_abs_max=float(self.progress_head.weight.detach().abs().max()),
            CE_targets_this_update=teachers,progress_labels_this_update=teachers,
            progress_learning_positions_this_update=teachers if enabled else 0,progress_target_sum_this_update=progress_sum,
            auxiliary_inputs_this_update=0,auxiliary_pairs_this_update=0,
            physical_inputs_this_update=ids.numel(),original_windows_this_update=len(rows),
            maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),
            seconds=time.monotonic()-started,data_wait_seconds=data_wait,lr=self.optimizer.param_groups[0]['lr'],
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])
        self._step_in_progress = False
        return result

    def _raw_state(self):
        state = super().state_dict()
        state.update(kind=KIND,progress_head=self.progress_head.state_dict())
        return state

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot save interrupted update; restore completed state')
        state = self._raw_state()
        if not committed_state(state):
            raise ValueError('Complete finite native/head/Adam/clock/source state required')
        return state

    def load(self,path):
        state = torch.load(Path(path),map_location=self.device,weights_only=False)
        if (not committed_state(state) or any(state[k] != self._raw_state()[k]
                for k in ('spec','binding','lineage','model_config'))):
            raise ValueError('Matching complete native-plus-progress state required before mutation')
        current = self.sampler.state_dict()
        if any(state['sampler'][k] != current[k] for k in ('kind','binding','seed','goals')):
            raise ValueError('Original material binding required before mutation')
        self.model.load_state_dict(state['model'],strict=True)
        self.progress_head.load_state_dict(state['progress_head'],strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters = copy.deepcopy(state['counters'])
        restore_rng(host(state['RNG']))
        self._step_in_progress = False
