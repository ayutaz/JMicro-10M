"""Native hard-gold CE with a typed, full-state dual-gradient-EMA optimizer."""
import copy
import math
from pathlib import Path
import torch
from natural_context_contrast_corpus import NaturalCorpusTrainer, OriginalTrainCorpusSampler
from natural_context_contrast_trainer import host
from jmicro.training import restore_rng

KIND = 'native_original_CE_all_parameter_AdEMAMix_half_life_warmup_v1'
OPT_KIND = 'dense_synchronous_fast_corrected_slow_uncorrected_AdEMAMix_v1'
POLICY = dict(lr=1e-5, weight_decay=.1, betas=(.9, .999, .9999), alpha=2., eps=1e-8, warmup=1000)


def coefficients(step, betas, alpha, warmup):
    if type(step) is not int or step < 1:
        raise ValueError('Positive completed-update position required')
    if step >= warmup:
        return alpha, betas[2]
    fraction = step / warmup
    # Official A.1 half-life interpolation, including the reference epsilon.
    initial = math.log(.5) / math.log(betas[0] + 1e-8) - 1
    final = math.log(.5) / math.log(betas[2] + 1e-8) - 1
    beta = .5 ** (1 / ((1-fraction)*initial + fraction*final + 1))
    return fraction * alpha, beta


class DenseAdEMAMix(torch.optim.Optimizer):
    """All parameters receive dense gradients each update, as native training does."""
    def __init__(self, parameters, lr=1e-5, weight_decay=.1, betas=(.9, .999, .9999),
                 alpha=2., eps=1e-8, warmup=1000):
        if (not all(math.isfinite(x) for x in (lr, weight_decay, alpha, eps, *betas))
                or lr <= 0 or weight_decay < 0 or alpha < 0 or eps <= 0
                or len(betas) != 3 or not all(0 < b < 1-1e-8 for b in betas)
                or type(warmup) is not int or warmup < 1):
            raise ValueError('Finite valid dual-EMA recipe required')
        super().__init__(parameters, dict(lr=lr, weight_decay=weight_decay,
            betas=tuple(betas), alpha=alpha, eps=eps, warmup=warmup))
        parameters = [p for group in self.param_groups for p in group['params']]
        if len({id(p) for p in parameters}) != len(parameters):
            raise ValueError('Every actual parameter exactly once required')
        self.recipe = [{k: copy.deepcopy(v) for k, v in group.items() if k != 'params'}
                       for group in self.param_groups]
        self.completed_steps, self.poisoned = 0, False

    @torch.no_grad()
    def step(self, closure=None):
        if self.poisoned or closure is not None:
            raise ValueError('Explicit dense gradients and valid checkpoint resume required')
        # Validate all gradients before any moment/weight mutation.
        for group in self.param_groups:
            for parameter in group['params']:
                gradient = parameter.grad
                if (gradient is None or gradient.is_sparse or parameter.dtype not in (torch.float32, torch.float64)
                        or gradient.dtype != parameter.dtype or not torch.isfinite(gradient).all()):
                    raise ValueError('Finite dense FP32/FP64 gradient for every parameter required')
        self.poisoned = True
        step = self.completed_steps + 1
        for group in self.param_groups:
            b1, b2, _ = group['betas']
            alpha, b3 = coefficients(step, group['betas'], group['alpha'], group['warmup'])
            for parameter in group['params']:
                state = self.state[parameter]
                if not state:
                    state.update(step=0, fast=torch.zeros_like(parameter),
                                 slow=torch.zeros_like(parameter), variance=torch.zeros_like(parameter))
                if state['step'] != self.completed_steps:
                    raise ValueError('Dense parameter moment cursor differs')
                gradient = parameter.grad
                state['fast'].mul_(b1).add_(gradient, alpha=1-b1)
                state['slow'].mul_(b3).add_(gradient, alpha=1-b3)
                state['variance'].mul_(b2).addcmul_(gradient, gradient, value=1-b2)
                denominator = (state['variance'] / (1-b2**step)).sqrt().add_(group['eps'])
                direction = state['fast'] / (1-b1**step) + alpha * state['slow']
                # Decoupled decay of the pre-update parameter, then EMA update.
                parameter.mul_(1-group['lr']*group['weight_decay'])
                parameter.addcdiv_(direction, denominator, value=-group['lr'])
                state['step'] = step
        self.completed_steps = step
        self.poisoned = False

    def state_dict(self):
        if self.poisoned:
            raise ValueError('Cannot save a partial dual-EMA optimizer update')
        state = super().state_dict()
        state.update(kind=OPT_KIND, completed_steps=self.completed_steps)
        return state

    def validate(self, state):
        if (state.get('kind') != OPT_KIND or type(state.get('completed_steps')) is not int
                or state['completed_steps'] < 0 or len(state['param_groups']) != len(self.param_groups)):
            raise ValueError('Explicit synchronous AdEMAMix state required')
        steps, seen = state['completed_steps'], set()
        for saved, actual, recipe in zip(state['param_groups'], self.param_groups, self.recipe, strict=True):
            if ({k: v for k, v in saved.items() if k not in ('params', 'initial_lr')} != recipe
                    or saved.get('initial_lr', recipe['lr']) != recipe['lr']):
                raise ValueError('Frozen dual-EMA recipe differs')
            for key, parameter in zip(saved['params'], actual['params'], strict=True):
                if key in seen:
                    raise ValueError('Duplicate optimizer parameter identifier')
                seen.add(key)
                if not steps:
                    continue
                moments = state['state'][key]
                if (set(moments) != {'step', 'fast', 'slow', 'variance'}
                        or type(moments['step']) is not int or moments['step'] != steps):
                    raise ValueError('Committed fast/slow/variance cursor differs')
                for name in ('fast', 'slow', 'variance'):
                    tensor = moments[name]
                    if (not isinstance(tensor, torch.Tensor) or tensor.shape != parameter.shape
                            or tensor.dtype != parameter.dtype or not torch.isfinite(tensor).all()):
                        raise ValueError('Moment shape/dtype/finite state differs')
                if (moments['variance'] < 0).any():
                    raise ValueError('Nonnegative second moment required')
        if set(state['state']) != (seen if steps else set()):
            raise ValueError('Every committed parameter has exactly three moments')

    def load_state_dict(self, state):
        self.validate(state)
        clean = {k: copy.deepcopy(state[k]) for k in ('state', 'param_groups')}
        super().load_state_dict(clean)
        self.completed_steps, self.poisoned = state['completed_steps'], False


def finite_tree(value):
    if isinstance(value, torch.Tensor):
        return bool(torch.isfinite(value).all())
    if isinstance(value, float):
        return math.isfinite(value)
    if isinstance(value, dict):
        return all(finite_tree(v) for v in value.values())
    if isinstance(value, (list, tuple)):
        return all(finite_tree(v) for v in value)
    return True


class AdEMAMixTrainer(NaturalCorpusTrainer):
    def __init__(self, parent, sampler, binding, batch=48, device='cuda', seed=42):
        if type(sampler) is not OriginalTrainCorpusSampler:
            raise ValueError('Original buffered TRAIN sampler, including legacy metadata, required')
        super().__init__(parent, sampler, binding, batch, False, device, seed)
        self.optimizer = DenseAdEMAMix(self.model.parameters(), **POLICY)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda _: 1.)
        self.spec.update(kind=KIND, optimizer_policy=OPT_KIND, optimizer_recipe=copy.deepcopy(POLICY),
                         actual_unique_parameters=sum(p.numel() for p in self.model.parameters()))
        self.lineage.update(kind=KIND, optimizer_policy=OPT_KIND)
        self._step_in_progress = False

    def validate_committed(self, state):
        if any(state[k] != self.state_recipe(k) for k in ('kind', 'spec', 'binding', 'lineage', 'model_config')):
            raise ValueError('Native dual-EMA training recipe/source/parent differs')
        self.optimizer.validate(state['optimizer'])
        n, counters = state['counters']['update'], state['counters']
        if (type(n) is not int or n < 0 or state['optimizer']['completed_steps'] != n
                or state['scheduler']['last_epoch'] != n or state['scheduler']['_step_count'] != n+1
                or state['scheduler']['base_lrs'] != [POLICY['lr']]
                or state['scheduler']['_last_lr'] != [POLICY['lr']]
                or counters['supervised_tokens'] != sum(counters['source_teachers'].values())
                or counters['source_teachers'] != state['sampler']['consumed']
                or counters['auxiliary_input_tokens'] or counters['auxiliary_pairs']
                or not finite_tree(state['model']) or not finite_tree(state['optimizer'])):
            raise ValueError('Finite committed optimizer/scheduler/source accounting required')
        actual = self.model.state_dict()
        if (set(actual) != set(state['model'])
                or any(actual[k].shape != v.shape or actual[k].dtype != v.dtype for k, v in state['model'].items())
                or not torch.equal(state['model']['lm_head.weight'], state['model']['model.embed_tokens.weight'])):
            raise ValueError('Exact native tensors and tied head required')
        recipe = self.sampler.state_dict()
        if any(recipe[k] != state['sampler'][k] for k in ('kind', 'binding', 'seed', 'goals')):
            raise ValueError('Full original sampler binding differs')

    def state_recipe(self, key):
        return KIND if key == 'kind' else self.model.config if key == 'model_config' else getattr(self, key)

    def state_dict(self):
        if self._step_in_progress:
            raise ValueError('Cannot save an uncommitted AdEMAMix training update')
        state = super().state_dict()
        state['kind'] = KIND
        self.validate_committed(state)
        return state

    def load(self, path):
        state = torch.load(Path(path), map_location=self.device, weights_only=False)
        self.validate_committed(state)
        self._step_in_progress = True
        self.model.load_state_dict(state['model'], strict=True)
        self.optimizer.load_state_dict(state['optimizer'])
        self.scheduler.load_state_dict(state['scheduler'])
        self.sampler.load_state_dict(state['sampler'])
        self.counters = copy.deepcopy(state['counters'])
        restore_rng(host(state['RNG']))
        self._step_in_progress = False

    def step(self):
        if self._step_in_progress or not self.model.training:
            raise ValueError('Native train mode and valid checkpoint required')
        self._step_in_progress = True
        result = super().step()
        if self.optimizer.completed_steps != self.counters['update']:
            raise ValueError('Completed dual-EMA update differs')
        self._step_in_progress = False
        result.update(optimizer_kind=OPT_KIND, optimizer_completed_steps=self.optimizer.completed_steps,
                      alpha=coefficients(self.optimizer.completed_steps, POLICY['betas'], POLICY['alpha'], POLICY['warmup'])[0],
                      beta3=coefficients(self.optimizer.completed_steps, POLICY['betas'], POLICY['alpha'], POLICY['warmup'])[1])
        return result
