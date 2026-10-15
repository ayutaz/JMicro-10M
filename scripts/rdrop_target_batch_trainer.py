"""Separate typed target CPU batch runtime; original analytic objective unchanged."""
import copy
import hashlib
import json
import math
from pathlib import Path
import time

import torch
from torch.nn import functional as F
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.rdrop import ARMS,POLICY
from jmicro.rdrop_analytic import IMPLEMENTATION,analytic_two_view_objective as two_view_objective
from jmicro.target_batch import IMPLEMENTATION as INPUT_RUNTIME,pack_original_targets
from jmicro.evaluation_boundary import require_digest
from jmicro.model import JMicroModel
from jmicro.training import restore_rng
from base_fim_trainer import finite,valid_rng
from base_residual_dropout import install_training_dropout
from context_likelihood_trainer import validate_material
from natural_context_contrast_corpus import NaturalCorpusTrainer,GENRES
from natural_context_contrast_trainer import host,right_pad,right_padded_hidden,synchronize

KIND = 'native_original_gold_normalized_RDrop_analytic_target_CPU_batch_v1'


def committed_state(state):
    try:
        spec,c,s,opt = (state[k] for k in ('spec','counters','sampler','optimizer'))
        steps,teachers = c['update'],c['supervised_tokens']
        enabled = spec['rdrop_arm'] == 'normalized_rdrop'
        integer_fields = ('update','supervised_tokens','CE_input_tokens','auxiliary_input_tokens','physical_input_tokens',
            'original_body_bytes','main_physical_input_tokens','second_view_physical_input_tokens',
            'second_view_gold_evaluations','total_CE_teacher_evaluations','consistency_pairs','second_view_EOS_evaluations')
        if (state['kind'] != KIND or spec['kind'] != KIND or state['lineage']['kind'] != KIND
                or spec['rdrop_arm'] not in ARMS or spec['rdrop_policy'] != POLICY or spec['contrast'] is not False
                or spec['loss_runtime'] != IMPLEMENTATION or state['lineage']['loss_runtime'] != IMPLEMENTATION
                or spec['input_runtime'] != INPUT_RUNTIME or state['lineage']['input_runtime'] != INPUT_RUNTIME
                or spec['original_material_binding'] != s['binding'] or spec['seed'] != s['seed'] or spec['goals'] != s['goals']
                or spec['inference_policy'] != 'unchanged_original_native_eval_no_dropout_no_head'
                or spec['gradient_clip_policy'] != 'exact_original_coordinate_reduction'
                or state['lineage']['optimizer_policy'] != 'fresh_equal_AdamW_both_arms'
                or any(type(c[k]) is not int or c[k] < 0 for k in integer_fields)
                or (steps == 0) != (teachers == 0) or steps != state['scheduler']['last_epoch']
                or c['source_teachers'] != s['consumed'] or teachers != sum(c['source_teachers'].values())
                or not c['main_physical_input_tokens'] >= c['CE_input_tokens'] >= teachers
                or c['physical_input_tokens'] != c['main_physical_input_tokens']+c['second_view_physical_input_tokens']
                or c['second_view_physical_input_tokens'] != (c['main_physical_input_tokens'] if enabled else 0)
                or c['auxiliary_input_tokens'] != (c['CE_input_tokens'] if enabled else 0)
                or c['second_view_gold_evaluations'] != (teachers if enabled else 0)
                or c['total_CE_teacher_evaluations'] != teachers+c['second_view_gold_evaluations']
                or c['consistency_pairs'] != (teachers if enabled else 0) or c['auxiliary_pairs'] != 0
                or c['second_view_EOS_evaluations'] != (sum(c['source_EOS'].values()) if enabled else 0)
                or c['auxiliary_digest'] != (c['token_digest'] if enabled else '0'*64)
                or set(c['source_EOS']) != set(GENRES)
                or any(type(c['source_EOS'][g]) is not int or not 0 <= c['source_EOS'][g] <= c['source_teachers'][g] for g in GENRES)
                or (not steps <= s['windows_emitted'] <= steps*spec['batch'] if steps else s['windows_emitted'] != 0)):
            return False
        validate_material(s)
        require_digest(c['token_digest'])
        if any(k.endswith('_research') for k in state['model_config']) or state['model_config']['qk_norm_type'] != 'none':
            return False
        with torch.device('meta'):
            model = JMicroModel(state['model_config'])
        expected = model.state_dict()
        if (set(expected) != set(state['model'])
                or any(not isinstance(state['model'][k],torch.Tensor) or state['model'][k].shape != v.shape
                    or state['model'][k].dtype != v.dtype for k,v in expected.items())
                or sum(p.numel() for p in model.parameters()) != spec['native_parameters']
                or spec['native_parameters'] != spec['training_parameters']
                or spec['native_parameters'] != state['model_config']['expected_parameter_count']
                or spec['train_only_parameters'] != 0
                or not torch.equal(state['model']['lm_head.weight'],state['model']['model.embed_tokens.weight'])):
            return False
        groups,parameters = opt['param_groups'],list(model.parameters())
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


class TargetBatchRDropTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,batch=48,device='cuda',seed=42,arm='normalized_rdrop'):
        if arm not in ARMS:
            raise ValueError('Explicit native verification or fixed normalized RDrop required')
        super().__init__(parent,sampler,binding,batch=batch,contrast=False,device=device,seed=seed)
        count = sum(p.numel() for p in self.model.parameters())
        if (binding.get('weights_role') not in ('verification_only','scientific_rdrop_target_batch25M')
                or (binding['weights_role'] != 'verification_only' and (arm != 'normalized_rdrop' or count != 10001152
                    or sampler.goals != dict(web=18750000,textbook=5000000,story=1250000)))):
            raise ValueError('Fixed original10M/25M scientific role or explicit verification required')
        # Reuse the CLOSED old hook implementation unchanged, not its recipe,
        # optimizer state, learned endpoint or claimed control evidence.
        install_training_dropout(self.model,.1 if arm == 'normalized_rdrop' else 0.)
        self.spec.update(kind=KIND,rdrop_arm=arm,rdrop_policy=copy.deepcopy(POLICY),loss_runtime=IMPLEMENTATION,input_runtime=INPUT_RUNTIME,
            original_material_binding=copy.deepcopy(sampler.binding),native_parameters=count,
            train_only_parameters=0,training_parameters=count,
            gradient_clip_policy='exact_original_coordinate_reduction',
            inference_policy='unchanged_original_native_eval_no_dropout_no_head')
        self.lineage.update(kind=KIND,loss_runtime=IMPLEMENTATION,input_runtime=INPUT_RUNTIME)
        self.counters.update(main_physical_input_tokens=0,second_view_physical_input_tokens=0,
            second_view_gold_evaluations=0,total_CE_teacher_evaluations=0,consistency_pairs=0,second_view_EOS_evaluations=0)
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress or not self.model.training:
            raise ValueError('Train mode and completed-update restore required')
        self._step_in_progress = True
        synchronize(self.device)
        started = time.monotonic()
        rows = self.sampler.take(self.spec['batch'])
        data_wait = time.monotonic()-started
        ids,_ = right_pad([r['input_ids'] for r in rows],self.device)
        targets = pack_original_targets(rows,ids.shape[1],self.device)
        self.optimizer.zero_grad(set_to_none=True)
        enabled = self.spec['rdrop_arm'] == 'normalized_rdrop'
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=self.device.type == 'cuda'):
            selected = targets.ne(-100)
            first = self.model.lm_head(right_padded_hidden(self.model,ids)[selected]).float()
            if enabled:
                second = self.model.lm_head(right_padded_hidden(self.model,ids)[selected]).float()
                losses = two_view_objective(first,second,targets[selected])
                changed = int(first.detach().ne(second.detach()).any(-1).sum())
            else:
                ce = F.cross_entropy(first,targets[selected])
                losses = dict(CE_view1_loss=ce,CE_view2_loss=ce,CE_loss=ce,
                    symmetric_KL=ce.new_zeros(()),combined_loss=ce)
                changed = 0
            if not all(torch.isfinite(v) for v in losses.values()):
                raise ValueError('Finite mean CE and symmetric consistency loss required')
            losses['combined_loss'].backward()
        gradient = torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        self.optimizer.step()
        self.scheduler.step()
        teachers = sum(r['teacher_tokens'] for r in rows)
        valid = sum(len(r['input_ids']) for r in rows)
        eos = sum(r['original_EOS_targets'] for r in rows)
        self.counters['update'] += 1
        for key,value in dict(supervised_tokens=teachers,CE_input_tokens=valid,
                auxiliary_input_tokens=valid if enabled else 0,physical_input_tokens=ids.numel()*(2 if enabled else 1),
                original_body_bytes=sum(r['teacher_body_bytes'] for r in rows),main_physical_input_tokens=ids.numel(),
                second_view_physical_input_tokens=ids.numel() if enabled else 0,
                second_view_gold_evaluations=teachers if enabled else 0,
                total_CE_teacher_evaluations=teachers*(2 if enabled else 1),
                consistency_pairs=teachers if enabled else 0,second_view_EOS_evaluations=eos if enabled else 0).items():
            self.counters[key] += value
        for row in rows:
            self.counters['source_teachers'][row['source']] += row['teacher_tokens']
            self.counters['source_EOS'][row['source']] += row['original_EOS_targets']
        if self.counters['source_teachers'] != self.sampler.consumed:
            raise ValueError('Completed original main source quota differs')
        stream = json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        if enabled:
            self.counters['auxiliary_digest'] = self.counters['token_digest']
        synchronize(self.device)
        result = dict(**copy.deepcopy(self.counters),**{k:float(v.detach()) for k,v in losses.items()},
            gradient_norm=float(gradient),different_view_positions_this_update=changed,
            CE_targets_this_update=teachers,second_view_gold_evaluations_this_update=teachers if enabled else 0,
            consistency_pairs_this_update=teachers if enabled else 0,
            main_physical_inputs_this_update=ids.numel(),auxiliary_inputs_this_update=valid if enabled else 0,
            auxiliary_pairs_this_update=0,physical_inputs_this_update=ids.numel()*(2 if enabled else 1),
            original_windows_this_update=len(rows),maximum_CE_input_tokens_this_update=max(len(r['input_ids']) for r in rows),
            seconds=time.monotonic()-started,data_wait_seconds=data_wait,lr=self.optimizer.param_groups[0]['lr'],
            draw_trace=[(r['index_byte_position'],r['index_record_sha256'],r['target_first'],r['target_end'],r['teacher_tokens']) for r in rows])
        self._step_in_progress = False
        return result

    def _raw_state(self):
        state = super().state_dict()
        state['kind'] = KIND
        return state

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot save interrupted update; restore completed state')
        state = self._raw_state()
        if not committed_state(state):
            raise ValueError('Complete finite native/Adam/torch dropout RNG/main+second clocks required')
        return state

    def load(self,path):
        state = torch.load(Path(path),map_location=self.device,weights_only=False)
        if (not committed_state(state) or any(state[k] != self._raw_state()[k]
                for k in ('spec','binding','lineage','model_config'))):
            raise ValueError('Exact typed objective/arm/lineage required before mutation')
        current = self.sampler.state_dict()
        if any(state['sampler'][k] != current[k] for k in ('kind','binding','seed','goals')):
            raise ValueError('Exact original main material required before mutation')
        self.model.load_state_dict(state['model'],strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters = copy.deepcopy(state['counters'])
        restore_rng(host(state['RNG']))
        self._step_in_progress = False
