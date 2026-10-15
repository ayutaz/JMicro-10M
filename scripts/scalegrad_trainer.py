"""Typed native one-pass ScaleGrad25M; all original teacher/source clocks."""
import copy
import hashlib
import json
from pathlib import Path
import time
import torch
from torch.nn.attention import SDPBackend,sdpa_kernel
from jmicro.evaluation_boundary import require_digest
from jmicro.model import JMicroModel
from jmicro.scalegrad import ARMS,POLICY,GAMMA,selected_novel_mask,scalegrad_objective
from jmicro.training import restore_rng
from base_fim_trainer import finite,valid_rng
from context_likelihood_trainer import validate_material
from natural_context_contrast_corpus import NaturalCorpusTrainer,GENRES
from natural_context_contrast_trainer import host,right_pad,right_padded_hidden,synchronize

KIND = 'native_original_gold_visible_body_prefix_ScaleGrad25M_v1'


def committed_state(state):
    try:
        spec,c,s,opt = (state[k] for k in ('spec','counters','sampler','optimizer'))
        steps,teachers = c['update'],c['supervised_tokens']
        enabled = spec['scalegrad_arm'] == 'scalegrad'
        integers = ('update','supervised_tokens','CE_input_tokens','physical_input_tokens','original_body_bytes',
            'original_CE_metric_evaluations','modified_loss_evaluations','total_CE_evaluations',
            'novel_gold_positions','novel_body_gold_positions','novel_EOS_gold_positions')
        if (state['kind'] != KIND or spec['kind'] != KIND or state['lineage']['kind'] != KIND
                or state['binding']['weights_role'] not in ('verification_only','scientific_scalegrad25M')
                or state['lineage']['weights_role'] != state['binding']['weights_role']
                or spec['scalegrad_arm'] not in ARMS or spec['scalegrad_policy'] != POLICY
                or type(spec['gamma']) is not float or spec['gamma'] != (GAMMA if enabled else 1.) or spec['contrast'] is not False
                or spec['original_material_binding'] != s['binding'] or spec['seed'] != s['seed'] or spec['goals'] != s['goals']
                or spec['inference_policy'] != 'unchanged_original_native_eval_no_novelty_adjustment'
                or state['lineage']['optimizer_policy'] != 'fresh_equal_AdamW_both_arms'
                or any(type(c[k]) is not int or c[k] < 0 for k in integers)
                or (steps == 0) != (teachers == 0) or steps != state['scheduler']['last_epoch']
                or c['source_teachers'] != s['consumed'] or teachers != sum(c['source_teachers'].values())
                or not c['physical_input_tokens'] >= c['CE_input_tokens'] >= teachers
                or c['auxiliary_pairs'] != 0 or c['auxiliary_input_tokens'] != 0 or c['auxiliary_digest'] != '0'*64
                or c['original_CE_metric_evaluations'] != teachers
                or c['modified_loss_evaluations'] != (teachers if enabled else 0)
                or c['total_CE_evaluations'] != teachers+c['modified_loss_evaluations']
                or c['novel_gold_positions'] != c['novel_body_gold_positions']+c['novel_EOS_gold_positions']
                or c['novel_gold_positions'] > teachers
                or c['novel_EOS_gold_positions'] != sum(c['source_EOS'].values())
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


class ScaleGradTrainer(NaturalCorpusTrainer):
    def __init__(self,parent,sampler,binding,batch=48,device='cuda',seed=42,arm='scalegrad'):
        if arm not in ARMS:
            raise ValueError('Explicit native control or fixed ScaleGrad arm required')
        super().__init__(parent,sampler,binding,batch=batch,contrast=False,device=device,seed=seed)
        count = sum(p.numel() for p in self.model.parameters())
        if (binding.get('weights_role') not in ('verification_only','scientific_scalegrad25M')
                or (binding['weights_role'] != 'verification_only' and (arm != 'scalegrad' or count != 10001152
                    or sampler.goals != dict(web=18750000,textbook=5000000,story=1250000)))):
            raise ValueError('Native fixed25M scientific role or explicit verification required')
        self.spec.update(kind=KIND,scalegrad_arm=arm,scalegrad_policy=copy.deepcopy(POLICY),
            gamma=GAMMA if arm == 'scalegrad' else 1.,original_material_binding=copy.deepcopy(sampler.binding),
            native_parameters=count,training_parameters=count,train_only_parameters=0,
            inference_policy='unchanged_original_native_eval_no_novelty_adjustment')
        self.lineage.update(kind=KIND)
        self.counters.update(original_CE_metric_evaluations=0,modified_loss_evaluations=0,total_CE_evaluations=0,
            novel_gold_positions=0,novel_body_gold_positions=0,novel_EOS_gold_positions=0)
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
        targets = torch.full_like(ids,-100)
        for i,row in enumerate(rows):
            targets[i,:len(row['target_ids'])] = torch.tensor(row['target_ids'],device=self.device)
        novelty = selected_novel_mask(rows,self.model.config['vocab_size'],self.device)
        self.optimizer.zero_grad(set_to_none=True)
        enabled = self.spec['scalegrad_arm'] == 'scalegrad'
        backend = SDPBackend.FLASH_ATTENTION if self.device.type == 'cuda' else SDPBackend.MATH
        with sdpa_kernel(backend),torch.autocast(self.device.type,dtype=torch.bfloat16,enabled=self.device.type == 'cuda'):
            labels = targets[targets.ne(-100)]
            logits = self.model.lm_head(right_padded_hidden(self.model,ids)[targets.ne(-100)]).float()
            losses = scalegrad_objective(logits,labels,novelty,gamma=self.spec['gamma'])
            if not all(torch.isfinite(v) for v in losses.values()):
                raise ValueError('Finite original metric CE and ScaleGrad learning loss required')
            losses['combined_loss'].backward()
        gradient = torch.nn.utils.clip_grad_norm_(self.model.parameters(),1.,error_if_nonfinite=True)
        self.optimizer.step()
        self.scheduler.step()
        teachers = sum(r['teacher_tokens'] for r in rows)
        novel_gold = novelty.gather(-1,labels[:,None]).squeeze(-1)
        novel_count = int(novel_gold.sum())
        novel_EOS = int((novel_gold & labels.eq(3)).sum())
        self.counters['update'] += 1
        for key,value in dict(supervised_tokens=teachers,CE_input_tokens=sum(len(r['input_ids']) for r in rows),
                physical_input_tokens=ids.numel(),original_body_bytes=sum(r['teacher_body_bytes'] for r in rows),
                original_CE_metric_evaluations=teachers,modified_loss_evaluations=teachers if enabled else 0,
                total_CE_evaluations=teachers*(2 if enabled else 1),novel_gold_positions=novel_count,
                novel_body_gold_positions=novel_count-novel_EOS,novel_EOS_gold_positions=novel_EOS).items():
            self.counters[key] += value
        for row in rows:
            self.counters['source_teachers'][row['source']] += row['teacher_tokens']
            self.counters['source_EOS'][row['source']] += row['original_EOS_targets']
        if self.counters['source_teachers'] != self.sampler.consumed:
            raise ValueError('Original main source quota differs')
        stream = json.dumps([(r['index_byte_position'],r['index_record_sha256'],r['input_ids'],r['target_ids']) for r in rows]).encode()
        self.counters['token_digest'] = hashlib.sha256(bytes.fromhex(self.counters['token_digest'])+stream).hexdigest()
        synchronize(self.device)
        result = dict(**copy.deepcopy(self.counters),**{k:float(v.detach()) for k,v in losses.items()},
            gradient_norm=float(gradient),CE_targets_this_update=teachers,novel_gold_positions_this_update=novel_count,
            novel_EOS_gold_positions_this_update=novel_EOS,decoder_forwards_this_update=1,
            physical_inputs_this_update=ids.numel(),auxiliary_inputs_this_update=0,auxiliary_pairs_this_update=0,
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
            raise ValueError('Cannot save interrupted update; restore a completed state')
        state = self._raw_state()
        if not committed_state(state):
            raise ValueError('Complete finite native/Adam/RNG/main/novelty state required')
        return state

    def load(self,path):
        state = torch.load(Path(path),map_location=self.device,weights_only=False)
        if (not committed_state(state) or any(state[k] != self._raw_state()[k]
                for k in ('spec','binding','lineage','model_config'))):
            raise ValueError('Exact typed objective/arm/lineage required before mutation')
        current = self.sampler.state_dict()
        if any(state['sampler'][k] != current[k] for k in ('kind','binding','seed','goals')):
            raise ValueError('Exact original material required before mutation')
        self.model.load_state_dict(state['model'],strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters = copy.deepcopy(state['counters'])
        restore_rng(host(state['RNG']))
        self._step_in_progress = False
