"""Preserve native Adam state; append13 fresh gate coordinates and one group."""
import copy
from pathlib import Path
import torch
from jmicro.experiment import sha256
from parameter_displacement_anchor_trainer import ParameterAnchorTrainer
from condition_positive_trainer import ConditionPositiveTrainer
from gated_shared_model import GatedSharedModel, POLICY

KIND = 'function_preserving_initial_gated_immediate_shared_Base_100M_v1'
NATIVE_LR = .00001
GATE_LR = .0001


class GatedSharedTrainer(ParameterAnchorTrainer):
    def __init__(self, parent, pool, original, positive, goals, binding,
                 device='cuda', context=1024, batch=32):
        super().__init__(parent, pool, original, positive, goals, binding, 0., device, context, batch)
        self.model = GatedSharedModel.from_native(self.model)
        options = {k: copy.deepcopy(v) for k, v in self.optimizer.param_groups[1].items() if k != 'params'}
        if options['weight_decay'] != 0 or options['lr'] != NATIVE_LR:
            raise ValueError('Native zero-decay floor group required')
        options.update(params=[self.model.reuse_gates], lr=GATE_LR, initial_lr=GATE_LR/.1)
        self.optimizer.add_param_group(options)
        optimizer_before_scheduler = copy.deepcopy(self.optimizer.state_dict())
        schedule = copy.deepcopy(parent['scheduler'])
        for key, value in (('base_lrs', GATE_LR/.1), ('_last_lr', GATE_LR), ('lr_lambdas', None)):
            schedule[key].append(value)
        self.scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lambda _: .1)
        self.scheduler.load_state_dict(schedule)
        self.optimizer.load_state_dict(optimizer_before_scheduler)
        self.spec.update(research_kind=KIND, gated_shared_reuse=copy.deepcopy(POLICY),
            gated_model_sha256=sha256(Path(__file__).with_name('gated_shared_model.py')),
            gated_trainer_sha256=sha256(Path(__file__)), native_LR=NATIVE_LR, new_gate_LR=GATE_LR,
            native_unique_parameters=sum(p.numel() for _, p in self.model.named_parameters() if p is not self.model.reuse_gates),
            new_gate_parameters=self.model.reuse_gates.numel(), logical_layers=self.model.logical_layers)
        self.lineage.update(kind=KIND, native_optimizer_policy='inherit_exact_native_groups_and_moments',
            new_gate_optimizer_policy='fresh_Adam_for_zero_gates_only', new_gate_LR=GATE_LR,
            parent_native_model_config=copy.deepcopy(parent['model_config']), gated_shared_reuse=copy.deepcopy(POLICY))
        self.forward = torch.compile(self.model, fullgraph=True, dynamic=False,
                                    mode=self.spec['compile_mode']) if self.spec['compile'] else self.model

    def step(self):
        result = ConditionPositiveTrainer.step(self)
        result.update(CE_loss=result['loss'], parameter_penalty=0., parameter_coefficient=0.,
            parameter_penalty_teacher_tokens=0, new_gate_LR=self.optimizer.param_groups[-1]['lr'])
        if [g['lr'] for g in self.optimizer.param_groups] != [NATIVE_LR, NATIVE_LR, GATE_LR]:
            raise ValueError('Fixed native/gate LR policy differs')
        return result
