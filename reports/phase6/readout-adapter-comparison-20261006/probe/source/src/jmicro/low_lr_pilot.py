"""Explicit learning-rate fork of the unchanged, resumable EOS pilot."""
import math

from jmicro.eos_pilot import PilotTrainer, pilot_lr


def set_fork_learning_rate(optimizer, scheduler, spec, peak_lr, update):
    if not math.isfinite(peak_lr) or peak_lr <= 0:
        raise ValueError('Fork learning rate must be finite and positive')
    spec['lr'] = peak_lr
    scheduler.base_lrs = [peak_lr] * len(optimizer.param_groups)
    values = [peak_lr * pilot_lr(spec, update)] * len(optimizer.param_groups)
    for group, value in zip(optimizer.param_groups, values):
        group['initial_lr'], group['lr'] = peak_lr, value
    scheduler._last_lr = values


class LowLRPilotTrainer(PilotTrainer):
    def __init__(self, parent, web, short, routes, schedule, binding, device='cuda'):
        super().__init__(parent, web, short, routes, schedule, binding, device)
        set_fork_learning_rate(self.optimizer, self.scheduler, self.spec,
                               binding['peak_lr'], parent['update'])
        self.lineage['learning_rate_fork'] = {
            'parent_base_lrs': list(parent['scheduler']['base_lrs']),
            'parent_actual_lrs': [g['lr'] for g in parent['optimizer']['param_groups']],
            'new_peak_lr': binding['peak_lr'],
            'moments_weights_RNG_cursors_preserved': True}
