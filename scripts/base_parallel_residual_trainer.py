"""Paired fresh residual connections; original TRAIN gold and token-position scheduler only."""
import copy
import math
from pathlib import Path

import torch
from base_kv_allocation_trainer import (CEOnlyOriginalSampler, FreshKVAllocationTrainer,
                                       TargetPositionSchedule, SAMPLER_KIND)
from base_native_teacher_KD_trainer import finite_KD_state
from base_parallel_residual_model import (POLICY, ParallelResidualModel, model_from_config,
                                     native_config)

KIND = 'fresh_equal_parameter_residual_connectivity_original_TRAIN_gold_token_schedule_v1'
ARMS = ('sequential', 'parallel')


def committed_state(state):
    """Check completed-update coupling and actual model/Adam tensor contracts."""
    try:
        spec, c, schedule, opt = (state[k] for k in ('spec', 'counters', 'scheduler', 'optimizer'))
        if (state['kind'] != KIND or spec['kind'] != KIND or spec['arm'] not in ARMS
                or spec['residual_policy'] != POLICY or spec['contrast']
                or state['sampler']['kind'] != SAMPLER_KIND):
            return False
        tagged = 'parallel_residual_research' in state['model_config']
        if tagged != (spec['arm'] == 'parallel'):
            return False
        with torch.device('meta'):
            model = model_from_config(state['model_config'])
        if (spec['model_class'] != type(model).__name__ or state['lineage']['kind'] != KIND
                or state['lineage']['arm'] != spec['arm'] or state['lineage']['parent'] is not None
                or state['lineage']['learned_parent_weights_used'] is not False
                or state['lineage']['probe_weights_used'] is not False):
            return False
        shapes = {k: v.shape for k, v in model.state_dict().items()}
        if (set(shapes) != set(state['model'])
                or any(state['model'][k].shape != shape for k, shape in shapes.items())
                or sum(p.numel() for p in model.parameters()) != spec['actual_unique_parameters']
                or not torch.equal(state['model']['lm_head.weight'], state['model']['model.embed_tokens.weight'])):
            return False
        steps, tokens = c['update'], c['supervised_tokens']
        if (type(steps) is not int or steps < 0 or type(tokens) is not int or tokens < 0
                or (steps == 0) != (tokens == 0)
                or tokens != schedule['tokens'] or tokens != sum(c['source_teachers'].values())
                or c['source_teachers'] != state['sampler']['consumed']
                or schedule['total'] != sum(spec['goals'].values())
                or spec['goals'] != state['sampler']['goals']
                or c['auxiliary_input_tokens'] or c['auxiliary_pairs']
                or not c['physical_input_tokens'] >= c['CE_input_tokens'] >= tokens):
            return False
        if schedule['kind'] != 'original_teacher_end_position_warmup_cosine_v1':
            return False
        if any(schedule[k] != spec['scheduler'][k] for k in ('kind', 'total', 'warmup', 'peak', 'final')):
            return False
        total, warmup, peak, final = (schedule[k] for k in ('total', 'warmup', 'peak', 'final'))
        if not 0 <= tokens <= total or not 0 < warmup < total or not 0 < final <= peak:
            return False
        expected_lr = (peak * tokens / warmup if tokens <= warmup else
            final + (peak - final) * (1 + math.cos(math.pi * ((tokens - warmup) / (total - warmup)))) / 2)
        if schedule['last_lr'] != expected_lr or len(opt['param_groups']) != 1:
            return False
        group = opt['param_groups'][0]
        identifiers = group['params']
        parameters = list(model.parameters())
        if (len(identifiers) != len(parameters) or len(set(identifiers)) != len(identifiers)
                or group['lr'] != expected_lr or group['weight_decay'] != .1
                or tuple(group['betas']) != (.9, .999) or group['eps'] != 1e-8):
            return False
        if not steps:
            if opt['state']:
                return False
        else:
            if set(opt['state']) != set(identifiers):
                return False
            for identifier, parameter in zip(identifiers, parameters, strict=True):
                adam = opt['state'][identifier]
                if (float(adam['step']) != steps or adam['exp_avg'].shape != parameter.shape
                        or adam['exp_avg_sq'].shape != parameter.shape):
                    return False
        return finite_KD_state(state)
    except (KeyError, TypeError, ValueError, OverflowError, RuntimeError):
        return False


class FreshResidualTrainer(FreshKVAllocationTrainer):
    def __init__(self, model_config, sampler, binding, arm, batch=80, device='cuda',
                 seed=42, warmup=5000000, peak=.002, final=1e-5):
        if arm not in ARMS or ('parallel_residual_research' in model_config) != (arm == 'parallel'):
            raise ValueError('Explicit matching fresh residual arm/config required')
        if not isinstance(sampler, CEOnlyOriginalSampler):
            raise ValueError('Original hard-gold CE-only sampler required')
        with torch.device('meta'):
            model_from_config(model_config)
        scaffold = native_config(model_config) if arm == 'parallel' else copy.deepcopy(model_config)
        super().__init__(scaffold, sampler, binding, batch, device, seed, warmup, peak, final)
        if arm == 'parallel':
            self.model = ParallelResidualModel.from_native_fresh(self.model)
            # The original scaffold optimizer has never taken an update. Build
            # the sole fresh optimizer over actual candidate parameters.
            self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=peak, weight_decay=.1)
            self.scheduler = TargetPositionSchedule(self.optimizer, sum(sampler.goals.values()), warmup, peak, final)
        if self.model.config != model_config:
            raise ValueError('Actual residual model config differs')
        self.spec.update(kind=KIND, arm=arm, residual_policy=copy.deepcopy(POLICY),
            model_class=type(self.model).__name__, optimizer='fresh_AdamW_actual_residual_parameters_once')
        self.lineage.update(kind=KIND, arm=arm, residual_initialization='identical_native_initial_weights_no_extra_RNG')
        self._step_in_progress = False

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot save an uncommitted residual update')
        state = super().state_dict()
        state['kind'] = KIND
        if not committed_state(state):
            raise ValueError('Nonfinite or inconsistent residual completed-update state')
        return state

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        if not committed_state(state):
            raise ValueError('Explicit finite committed residual state required')
        super().load(path)
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress:
            raise ValueError('Interrupted residual update requires valid checkpoint resume')
        self._step_in_progress = True
        row = super().step()
        if self.scheduler.tokens != self.counters['supervised_tokens']:
            raise ValueError('residual completed scheduler/gold cursor mismatch')
        self._step_in_progress = False
        row.update(arm=self.spec['arm'], residual_policy=POLICY['kind'], committed_update=True)
        return row
