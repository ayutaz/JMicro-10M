"""Committed-state and worst-shape fixtures for the fixed context-mixing study."""
import copy
import torch
from base_context_mixing_trainer import KIND


def finite_context_mixing_state(state):
    def finite(value):
        if isinstance(value, torch.Tensor): return bool(torch.isfinite(value).all())
        if isinstance(value, dict): return all(finite(v) for v in value.values())
        if isinstance(value, (tuple, list)): return all(finite(v) for v in value)
        return True
    counts, mixed = state['counters'], state['context_mixing']
    steps = counts['update']
    return (state['kind'] == KIND and finite(state['model']) and finite(state['optimizer']) and
            steps == mixed['updates'] == state['scheduler']['last_epoch'] and
            all(int(v['step']) == steps for v in state['optimizer']['state'].values()) and
            0 <= mixed['changed_positions'] <= mixed['selected_positions'] <= mixed['eligible_positions'] and
            counts['supervised_tokens'] == sum(counts['source_teachers'].values()) and
            counts['source_teachers'] == state['sampler']['consumed'])


class CapacitySampler:
    """One repeated accepted TRAIN window, solely for worst memory measurement."""
    def __init__(self, payload, tokenizer, batch=48):
        window = payload['window']
        if len(window['input_ids']) != 1024 or sum(n != -100 for n in window['target_ids']) != 512:
            raise ValueError('Accepted original1024/512 worst-window fixture required')
        byte_lengths = {n: len(tokenizer.decode_bytes([n])) for n in set(window['target_ids']) if n >= 8}
        source = payload['original_record']['source']
        if source not in ('web', 'textbook', 'story') or payload['original_record']['split'] != 'train':
            raise ValueError('Original accepted TRAIN genre required')
        row = dict(**copy.deepcopy(window), source=source, teacher_tokens=512,
            teacher_body_bytes=sum(int(byte_lengths[n]) for n in window['target_ids'] if n >= 8),
            original_EOS_targets=window['target_ids'].count(3),
            index_byte_position=payload['index_byte_position'], index_record_sha256=payload['index_record_sha256'])
        self.rows = [copy.deepcopy(row) for _ in range(batch)]
        self.goals = dict(web=0, textbook=0, story=0)
        self.goals[source] = batch*512
        self.consumed = dict.fromkeys(self.goals, 0)
        self.used = False

    def take(self, batch):
        if self.used or batch != len(self.rows): raise ValueError('One worst-shape verification update only')
        self.used = True
        self.consumed = self.goals.copy()
        return copy.deepcopy(self.rows)

    def state_dict(self):
        return dict(kind='worst_accepted_TRAIN_window_memory_fixture', used=self.used, consumed=self.consumed.copy())
