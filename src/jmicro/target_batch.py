"""Exactly original right-padded int64 labels, one host tensor/device copy."""
import torch

IMPLEMENTATION = 'original_gold_targets_CPU_single_tensor_single_device_transfer_v1'


def pack_original_targets(rows,width,device):
    if (not rows or type(width) is not int or width <= 0 or any(
            not row['input_ids'] or len(row['target_ids']) != len(row['input_ids'])
            or len(row['input_ids']) > width for row in rows)):
        raise ValueError('Aligned nonempty original input/target rows within original width required')
    padded = [row['target_ids']+[-100]*(width-len(row['target_ids'])) for row in rows]
    return torch.tensor(padded,dtype=torch.long,device='cpu').to(device)
