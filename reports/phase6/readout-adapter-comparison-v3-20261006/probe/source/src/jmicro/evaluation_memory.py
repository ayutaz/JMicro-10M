"""Release unused evaluation cache; do not modify weights, tensors or numerics."""
import torch


def bound_evaluation_cache(model):
    state = {'forward_calls': 0, 'cache_releases': 0, 'maximum_observed_allocated_bytes': 0,
             'maximum_observed_reserved_bytes': 0, 'policy': 'Every32 forwards, release unused cache if reserved>8GiB and unused>4GiB'}
    def before_forward(_model, inputs):
        state['forward_calls'] += 1
        if state['forward_calls'] % 32 or inputs[0].device.type != 'cuda':
            return
        allocated, reserved = torch.cuda.memory_allocated(), torch.cuda.memory_reserved()
        state['maximum_observed_allocated_bytes'] = max(state['maximum_observed_allocated_bytes'], allocated)
        state['maximum_observed_reserved_bytes'] = max(state['maximum_observed_reserved_bytes'], reserved)
        if reserved > 8 * 1024**3 and reserved - allocated > 4 * 1024**3:
            torch.cuda.empty_cache()
            state['cache_releases'] += 1
    model.register_forward_pre_hook(before_forward)
    return state
