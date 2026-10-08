"""Native fresh updates with only per-teacher decoupled decay exposure changed."""
import copy
import math
from pathlib import Path

import torch
from base_parallel_residual_trainer import FreshResidualTrainer, committed_state, KIND as BASE_KIND
from natural_context_contrast_trainer import host
from jmicro.training import restore_rng

KIND = 'fresh_native_teacher_normalized_decoupled_decay_v1'
REFERENCE_TEACHERS = 32768
BASE_DECAY = .1


def policy():
    return dict(kind=KIND, reference_teachers=REFERENCE_TEACHERS, reference_weight_decay=BASE_DECAY,
                formula='(1-lr*0.1)^(original_teachers_this_update/32768)',
                parameter_scope='same_all_native_parameters', changes_Adam_timing=False)


def effective_decay(lr, teachers):
    if (not math.isfinite(lr) or not 0 < lr*BASE_DECAY < 1
            or type(teachers) is not int or teachers <= 0):
        raise ValueError('Finite positive LR and original teacher count required')
    return -math.expm1(math.log1p(-lr*BASE_DECAY)*(teachers/REFERENCE_TEACHERS))/lr


def committed_decay(state):
    try:
        decay, c = state['decay'], state['counters']
        if (state['kind'] != KIND or state['spec']['arm'] != 'sequential'
                or state['spec']['weight_decay'] != policy()
                or state['lineage']['weight_decay_policy'] != policy()
                or decay['policy'] != policy() or decay['last_update'] != c['update']):
            return False
        n = decay['last_update_teachers']
        if (type(n) is not int or (c['update']==0 and n!=0)
                or (c['update']>0 and not 0<n<=c['supervised_tokens'])):
            return False
        expected = effective_decay(state['scheduler']['last_lr'], n) if c['update'] else BASE_DECAY
        if (decay['last_effective_weight_decay'] != expected
                or state['optimizer']['param_groups'][0]['weight_decay'] != expected):
            return False
        # Reuse the original tensor/sampler/Adam/schedule validator, with its
        # fixed-WD assertion translated only in a detached validation view.
        base = dict(state, kind=BASE_KIND)
        base.pop('decay')
        base['optimizer'] = dict(state['optimizer'], param_groups=[dict(
            state['optimizer']['param_groups'][0], weight_decay=BASE_DECAY)])
        return committed_state(base)
    except (KeyError, TypeError, ValueError, OverflowError, IndexError):
        return False


class TeacherDecayTrainer:
    def __init__(self, native):
        if (not isinstance(native, FreshResidualTrainer) or native.spec['arm']!='sequential'
                or native.counters['update'] or native.optimizer.state or native.spec['weight_decay']!=BASE_DECAY
                or 'weight_decay_policy' in native.lineage
                or any(p.grad is not None for p in native.model.parameters())):
            raise ValueError('Untouched fresh native sequential trainer required')
        self.native = native
        self.last_update_teachers = 0
        self.last_effective_weight_decay = BASE_DECAY
        self.last_update = 0
        native.spec['weight_decay'] = policy()
        native.lineage['weight_decay_policy'] = policy()
        self.hook = native.optimizer.register_step_pre_hook(self._prepare_decay)

    def _prepare_decay(self, optimizer, args, kwargs):
        t = self.native
        if optimizer is not t.optimizer or self.last_update != t.counters['update']:
            raise ValueError('One decay application per native committed update required')
        teachers = sum(t.sampler.consumed.values()) - t.counters['supervised_tokens']
        group = optimizer.param_groups[0]
        if len(optimizer.param_groups)!=1 or group['lr']!=t.scheduler.value(t.scheduler.tokens+teachers):
            raise ValueError('Actual same-update original teachers and prepared LR required')
        self.last_update_teachers = teachers
        self.last_effective_weight_decay = effective_decay(group['lr'], teachers)
        group['weight_decay'] = self.last_effective_weight_decay
        self.last_update = t.counters['update']+1

    def step(self):
        row = self.native.step()
        if (self.last_update!=row['update'] or self.last_update_teachers!=row['CE_targets_this_update']):
            raise ValueError('Completed native update and decay exposure differ')
        row.update(effective_weight_decay=self.last_effective_weight_decay,
                   decay_reference_teachers=REFERENCE_TEACHERS,
                   decay_only_factor_this_update=1-row['lr']*self.last_effective_weight_decay)
        return row

    def state_dict(self):
        t = self.native
        if self.last_update != t.counters['update']:
            raise ValueError('Cannot save an interrupted decay update')
        actual_rate = t.optimizer.param_groups[0]['weight_decay']
        try:
            t.optimizer.param_groups[0]['weight_decay'] = BASE_DECAY
            state = t.state_dict()
        finally:
            t.optimizer.param_groups[0]['weight_decay'] = actual_rate
        # torch optimizer.state_dict returns a separate param-group mapping.
        state['optimizer']['param_groups'][0]['weight_decay'] = actual_rate
        state.update(kind=KIND, decay=dict(policy=policy(),last_update=self.last_update,
            last_update_teachers=self.last_update_teachers,
            last_effective_weight_decay=self.last_effective_weight_decay))
        if not committed_decay(state):
            raise ValueError('Finite committed teacher-normalized decay state required')
        return state

    def save(self,path):
        path = Path(path)
        temporary = path.with_suffix('.tmp')
        torch.save(host(self.state_dict()), temporary)
        temporary.replace(path)

    def load(self,path):
        state = torch.load(path,map_location=self.native.device,weights_only=False)
        t = self.native
        if not committed_decay(state):
            raise ValueError('Matching finite committed teacher-decay checkpoint required')
        expected = dict(spec=t.spec,binding=t.binding,lineage=t.lineage,model_config=t.model.config)
        if any(state[k]!=v for k,v in expected.items()):
            raise ValueError('Teacher-decay recipe/source binding differs')
        t.scheduler.validate(state['scheduler'])
        t.sampler.load_state_dict(state['sampler'])
        t.model.load_state_dict(state['model'],strict=True)
        t.optimizer.load_state_dict(state['optimizer'])
        t.scheduler.load_state_dict(state['scheduler'])
        t.counters = copy.deepcopy(state['counters'])
        decay = state['decay']
        self.last_update, self.last_update_teachers = decay['last_update'], decay['last_update_teachers']
        self.last_effective_weight_decay = decay['last_effective_weight_decay']
        restore_rng(host(state['RNG']))
        t._step_in_progress = False
