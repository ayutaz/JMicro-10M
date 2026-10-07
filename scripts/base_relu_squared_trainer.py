"""Paired fresh FFNs; original TRAIN gold and token-position scheduler only."""
import copy
import math
from pathlib import Path

import torch
from base_kv_allocation_trainer import (CEOnlyOriginalSampler, FreshKVAllocationTrainer,
                                       TargetPositionSchedule, SAMPLER_KIND)
from base_native_teacher_KD_trainer import finite_KD_state
from base_relu_squared_model import (POLICY, SquaredReLUModel, model_from_config,
                                     native_config)

KIND = 'fresh_equal_parameter_FFN_original_TRAIN_gold_token_schedule_v1'
ARMS = ('SwiGLU', 'ReLU_squared')


def committed_state(state):
    """Check completed-update coupling and actual model/Adam tensor contracts."""
    try:
        spec, c, schedule, opt = (state[k] for k in ('spec', 'counters', 'scheduler', 'optimizer'))
        if (state['kind'] != KIND or spec['kind'] != KIND or spec['arm'] not in ARMS
                or spec['ffn_policy'] != POLICY or spec['contrast']
                or state['sampler']['kind'] != SAMPLER_KIND):
            return False
        tagged = 'ffn_research' in state['model_config']
        if tagged != (spec['arm'] == 'ReLU_squared'):
            return False
        with torch.device('meta'):
            model = model_from_config(state['model_config'])
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
            final + (peak - final) * (1 + math.cos(math.pi * (tokens - warmup) / (total - warmup))) / 2)
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


class FreshFFNTrainer(FreshKVAllocationTrainer):
    def __init__(self, model_config, sampler, binding, arm, batch=80, device='cuda',
                 seed=42, warmup=5000000, peak=.002, final=1e-5):
        if arm not in ARMS or ('ffn_research' in model_config) != (arm == 'ReLU_squared'):
            raise ValueError('Explicit matching fresh FFN arm/config required')
        if not isinstance(sampler, CEOnlyOriginalSampler):
            raise ValueError('Original hard-gold CE-only sampler required')
        scaffold = native_config(model_config) if arm == 'ReLU_squared' else copy.deepcopy(model_config)
        if arm == 'ReLU_squared' and model_config['ffn_research']['initialization_seed'] != seed:
            raise ValueError('Paired fresh initialization seed differs')
        super().__init__(scaffold, sampler, binding, batch, device, seed, warmup, peak, final)
        if arm == 'ReLU_squared':
            self.model = SquaredReLUModel.from_native_fresh(self.model, seed)
            # The original scaffold optimizer has never taken an update. Build
            # the sole fresh optimizer over actual candidate parameters.
            self.optimizer = torch.optim.AdamW(self.model.parameters(), lr=peak, weight_decay=.1)
            self.scheduler = TargetPositionSchedule(self.optimizer, sum(sampler.goals.values()), warmup, peak, final)
        if self.model.config != model_config:
            raise ValueError('Actual FFN model config differs')
        self.spec.update(kind=KIND, arm=arm, ffn_policy=copy.deepcopy(POLICY),
            model_class=type(self.model).__name__, optimizer='fresh_AdamW_actual_FFN_parameters_once')
        self.lineage.update(kind=KIND, arm=arm, FFN_initialization='paired_native_scaffold_and_CPU_fork_seed1000003_plus_layer')
        self._step_in_progress = False

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot save an uncommitted FFN update')
        state = super().state_dict()
        state['kind'] = KIND
        if not committed_state(state):
            raise ValueError('Nonfinite or inconsistent FFN completed-update state')
        return state

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        if not committed_state(state):
            raise ValueError('Explicit finite committed FFN state required')
        super().load(path)
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress:
            raise ValueError('Interrupted FFN update requires valid checkpoint resume')
        self._step_in_progress = True
        row = super().step()
        if self.scheduler.tokens != self.counters['supervised_tokens']:
            raise ValueError('FFN completed scheduler/gold cursor mismatch')
        self._step_in_progress = False
        row.update(arm=self.spec['arm'], ffn_policy=POLICY['kind'], committed_update=True)
        return row
