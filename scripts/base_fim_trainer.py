"""Fresh native CE on original gold identities under the explicit FIM protocol.

Uses a new checkpoint kind. Never forge a legacy trainer/seed/fullDEV kind.
Old model, optimizer and evaluation sources remain untouched.
"""
import copy
import math
from pathlib import Path
import random

import numpy as np
import torch

from base_fim_sampler import FimOriginalSampler, KIND as SAMPLER_KIND, POLICY
from base_kv_allocation_trainer import FreshKVAllocationTrainer
from jmicro.model import JMicroModel
from jmicro.training import restore_rng
from natural_context_contrast_trainer import host

KIND = 'fresh_native_original_gold_FIM_PSM_v1'


def finite(value):
    if isinstance(value, torch.Tensor): return bool(torch.isfinite(value).all())
    if isinstance(value, dict): return all(finite(v) for v in value.values())
    if isinstance(value, (list, tuple)): return all(finite(v) for v in value)
    return True


def valid_rng(state):
    try:
        if set(state) != {'python', 'numpy', 'torch', 'cuda'}:
            return False
        random.Random().setstate(state['python'])
        np.random.RandomState(0).set_state(state['numpy'])
        if not isinstance(state['torch'], torch.Tensor) or state['torch'].dtype != torch.uint8:
            return False
        torch.Generator(device='cpu').set_state(state['torch'].cpu())
        return isinstance(state['cuda'], list) and all(isinstance(v, torch.Tensor)
            and v.dtype == torch.uint8 and v.ndim == 1 and v.numel() > 0 for v in state['cuda'])
    except (ValueError, TypeError, KeyError, RuntimeError):
        return False


def committed_state(state):
    """Prove completed-update coupling, actual native tensors and original clock."""
    try:
        spec, c, schedule, opt, source = (state[k] for k in
            ('spec', 'counters', 'scheduler', 'optimizer', 'sampler'))
        if (state['kind'] != KIND or spec['kind'] != KIND or spec['FIM_policy'] != POLICY
                or source['kind'] != SAMPLER_KIND or source['FIM_policy'] != POLICY
                or spec['contrast'] or spec['optimizer'] != 'fresh_AdamW'
                or state['lineage']['kind'] != KIND or state['lineage']['parent'] is not None
                or state['lineage']['learned_parent_weights_used'] is not False
                or state['lineage']['probe_weights_used'] is not False):
            return False
        with torch.device('meta'):
            model = JMicroModel(state['model_config'])
        shapes = {k:v.shape for k,v in model.state_dict().items()}
        if (set(shapes) != set(state['model'])
                or any(state['model'][k].shape != shape for k,shape in shapes.items())
                or any(state['model'][k].dtype != v.dtype for k,v in model.state_dict().items())
                or sum(p.numel() for p in model.parameters()) != spec['actual_unique_parameters']
                or not torch.equal(state['model']['lm_head.weight'], state['model']['model.embed_tokens.weight'])):
            return False
        steps, tokens = c['update'], c['supervised_tokens']
        if (type(steps) is not int or type(tokens) is not int or steps < 0 or tokens < 0
                or (steps == 0) != (tokens == 0) or spec['seed'] != source['seed']
                or state['lineage']['seed'] != spec['seed']
                or tokens != schedule['tokens'] or tokens != sum(c['source_teachers'].values())
                or c['source_teachers'] != source['consumed'] or spec['goals'] != source['goals']
                or schedule['total'] != sum(spec['goals'].values())
                or c['auxiliary_input_tokens'] or c['auxiliary_pairs']
                or not c['physical_input_tokens'] >= c['CE_input_tokens'] >= tokens):
            return False
        f = source['FIM_counters']
        if (f['rows'] != source['windows_emitted']
                or not steps <= f['rows'] <= steps * spec['batch']
                or not 0 <= f['applied_rows'] <= f['eligible_rows'] <= f['rows']
                or not 0 <= f['selected_original_teachers'] <= tokens
                or f['marker_inputs'] > c['CE_input_tokens'] - tokens):
            return False
        if (schedule['kind'] != 'original_teacher_end_position_warmup_cosine_v1'
                or any(schedule[k] != spec['scheduler'][k] for k in ('kind','total','warmup','peak','final'))):
            return False
        total, warmup, peak, final = (schedule[k] for k in ('total','warmup','peak','final'))
        if not 0 <= tokens <= total or not 0 < warmup < total or not 0 < final <= peak:
            return False
        expected_lr = peak*tokens/warmup if tokens <= warmup else (
            final+(peak-final)*(1+math.cos(math.pi*(tokens-warmup)/(total-warmup)))/2)
        if schedule['last_lr'] != expected_lr or len(opt['param_groups']) != 1:
            return False
        group = opt['param_groups'][0]
        identifiers = group['params']; parameters = list(model.parameters())
        if (len(identifiers) != len(parameters) or len(set(identifiers)) != len(identifiers)
                or group['lr'] != expected_lr or group['weight_decay'] != .1
                or tuple(group['betas']) != (.9,.999) or group['eps'] != 1e-8):
            return False
        if not steps:
            if opt['state']: return False
        else:
            if set(opt['state']) != set(identifiers): return False
            for identifier, parameter in zip(identifiers, parameters, strict=True):
                adam = opt['state'][identifier]
                if (float(adam['step']) != steps or adam['exp_avg'].shape != parameter.shape
                        or adam['exp_avg_sq'].shape != parameter.shape
                        or adam['exp_avg'].dtype != parameter.dtype or adam['exp_avg_sq'].dtype != parameter.dtype):
                    return False
        return valid_rng(state['RNG']) and finite(state)
    except (KeyError, TypeError, ValueError, RuntimeError, OverflowError):
        return False


class FreshFimTrainer(FreshKVAllocationTrainer):
    def __init__(self, model_config, sampler, binding, batch=80, device='cuda', seed=42,
                 warmup=5000000, peak=.002, final=1e-5):
        if not isinstance(sampler, FimOriginalSampler) or sampler.seed != seed:
            raise ValueError('Explicit matching fresh FIM material/model seed required')
        super().__init__(model_config, sampler, binding, batch, device, seed, warmup, peak, final)
        self.spec.update(kind=KIND, FIM_policy=copy.deepcopy(POLICY),
                         CE_policy='same_original_gold_post_quota_permutation_marker_targets_ignored')
        self.lineage.update(kind=KIND)
        self._step_in_progress = False

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot save an interrupted FIM update; resume previous checkpoint')
        state = super().state_dict()
        state['kind'] = KIND
        if not committed_state(state):
            raise ValueError('Finite complete FIM/native/Adam/scheduler/stream state required')
        self.sampler.validate_state(state['sampler'])
        return state

    def step(self):
        if self._step_in_progress:
            raise ValueError('Interrupted FIM update requires valid full-state resume')
        self._step_in_progress = True
        row = super().step()
        self._step_in_progress = False
        row.update(FIM_counters=copy.deepcopy(self.sampler.fim), committed_update=True)
        return row

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        current = self.state_dict() if not self._step_in_progress else super().state_dict()
        if (not committed_state(state) or any(state[k] != current[k]
                for k in ('spec','binding','lineage','model_config'))):
            raise ValueError('Matching committed FIM checkpoint required before any mutation')
        self.sampler.validate_state(state['sampler'])
        self.scheduler.validate(state['scheduler'])
        self.model.load_state_dict(state['model'], strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters = copy.deepcopy(state['counters'])
        restore_rng(host(state['RNG']))
        self._step_in_progress = False
