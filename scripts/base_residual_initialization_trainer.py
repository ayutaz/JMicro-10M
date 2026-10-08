"""Fresh native learning with only depth-scaled residual-output initialization."""
import copy
import math
from pathlib import Path

import torch
from base_parallel_residual_trainer import FreshResidualTrainer, committed_state, KIND as BASE_KIND
from natural_context_contrast_trainer import host
from jmicro.training import restore_rng

KIND = 'fresh_native_depth_scaled_residual_output_initialization_v1'
LINEAGE = 'same_native_fresh_samples_scaled_residual_outputs_no_extra_RNG'


def policy(config):
    layers = config['num_hidden_layers']
    return dict(kind=KIND, residual_outputs=2*layers, factor=1/math.sqrt(2*layers),
                method='multiply_same_native_fresh_samples_once_before_learning',
                inference_forward_unchanged=True)


def committed_initialization(state):
    try:
        base = dict(state, kind=BASE_KIND)
        base.pop('initialization')
        return (state['kind'] == KIND and state['spec']['arm'] == 'sequential'
                and state['initialization'] == policy(state['model_config'])
                and state['lineage']['residual_initialization'] == LINEAGE
                and committed_state(base))
    except (KeyError, TypeError, ValueError):
        return False


class InitializationTrainer:
    def __init__(self, native):
        if (not isinstance(native, FreshResidualTrainer) or native.spec['arm'] != 'sequential'
                or native.counters['update'] or native.optimizer.state
                or native.lineage['residual_initialization'] != 'identical_native_initial_weights_no_extra_RNG'
                or any(p.grad is not None for p in native.model.parameters())):
            raise ValueError('Untouched fresh native sequential trainer required')
        self.native = native
        self.initialization = policy(native.model.config)
        rng = host(torch.get_rng_state())
        with torch.no_grad():
            for block in native.model.model.layers:
                block.self_attn.o_proj.weight.mul_(self.initialization['factor'])
                block.mlp.down_proj.weight.mul_(self.initialization['factor'])
        if not torch.equal(rng, torch.get_rng_state()):
            raise ValueError('Initialization consumed additional RNG')
        native.lineage['residual_initialization'] = LINEAGE

    def step(self):
        return self.native.step()

    def state_dict(self):
        state = dict(self.native.state_dict(), kind=KIND, initialization=copy.deepcopy(self.initialization))
        if not committed_initialization(state):
            raise ValueError('Finite completed initialization checkpoint required')
        return state

    def save(self, path):
        path = Path(path)
        temporary = path.with_suffix('.tmp')
        torch.save(host(self.state_dict()), temporary)
        temporary.replace(path)

    def load(self, path):
        state = torch.load(path, map_location=self.native.device, weights_only=False)
        t = self.native
        if not committed_initialization(state) or state['initialization'] != self.initialization:
            raise ValueError('Matching finite initialized completed checkpoint required')
        expected = dict(spec=t.spec, binding=t.binding, lineage=t.lineage, model_config=t.model.config)
        if any(state[key] != value for key, value in expected.items()):
            raise ValueError('Initialization recipe/source binding differs')
        t.scheduler.validate(state['scheduler'])
        t.sampler.load_state_dict(state['sampler'])
        t.model.load_state_dict(state['model'], strict=True)
        t.optimizer.load_state_dict(state['optimizer'])
        t.scheduler.load_state_dict(state['scheduler'])
        t.counters = copy.deepcopy(state['counters'])
        restore_rng(host(state['RNG']))
        t._step_in_progress = False
