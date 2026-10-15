"""Original-document progress labels and one training-only scalar head.

No target, document length or head output is supplied to native inference.
Targets describe the original whole body, never the end of a training window.
"""
import torch
from torch import nn
from torch.nn import functional as F

COEFFICIENT = .1
ARMS = ('native_CE_control','document_progress')
POLICY = dict(kind='original_document_remaining_body_fraction_sigmoid_L1_v1',
    target='(original_body_tokens-input_start-physical_column)/original_body_tokens',
    mask='exact_original_main_CE_unmasked_slots',coefficient=COEFFICIENT,
    head='zero_initialized_FP32_no_bias_scalar_linear_final_native_hidden',
    additional_decoder_passes=0,inference='native_model_only_no_head_or_length_hint')


def progress_targets(rows):
    """Return row-aligned fractions, with -1 only at original ignored targets."""
    if not isinstance(rows,list) or not rows:
        raise ValueError('Nonempty original TRAIN rows required')
    result = []
    for row in rows:
        n,start,first,end = (row[k] for k in ('original_body_tokens','input_start','target_first','target_end'))
        ids,targets = row['input_ids'],row['target_ids']
        if (any(type(v) is not int for v in (n,start,first,end)) or n <= 0
                or not 0 <= start < first < end <= n+2
                or not isinstance(ids,list) or not isinstance(targets,list)
                or not 0 < len(ids) == len(targets) == end-1-start <= 1024
                or any(type(t) is not int or not (t == 2 or 8 <= t < 4096) for t in ids)
                or any(type(t) is not int or not (t in (-100,3) or 8 <= t < 4096) for t in targets)):
            raise ValueError('Genuine original full-document/window geometry and IDs required')
        labels = []
        for column,target in enumerate(targets):
            if target == -100:
                labels.append(-1.)
                continue
            absolute = start+column
            if (not first <= absolute+1 < end or not 0 <= absolute <= n
                    or (target == 3) != (absolute == n)):
                raise ValueError('Only original selected body/EOS absolute positions required')
            labels.append((n-absolute)/n)
        selected = sum(t != -100 for t in targets)
        if not selected or ('teacher_tokens' in row and row['teacher_tokens'] != selected):
            raise ValueError('Nonempty exact original selected teacher count required')
        if 'original_EOS_targets' in row and row['original_EOS_targets'] != targets.count(3):
            raise ValueError('Original EOS counter differs')
        result.append(labels)
    return result


class ProgressHead(nn.Module):
    def __init__(self,hidden_size,device='cpu'):
        super().__init__()
        if type(hidden_size) is not int or hidden_size <= 0:
            raise ValueError('Positive original hidden size required')
        self.weight = nn.Parameter(torch.zeros(1,hidden_size,dtype=torch.float32,device=device))

    def forward(self,selected_hidden):
        if (selected_hidden.ndim != 2 or not len(selected_hidden)
                or selected_hidden.shape[1] != self.weight.shape[1]
                or selected_hidden.device != self.weight.device
                or not selected_hidden.is_floating_point() or self.weight.dtype != torch.float32):
            raise ValueError('Original selected hidden and FP32 scalar head required')
        with torch.autocast(device_type=selected_hidden.device.type,enabled=False):
            return F.linear(selected_hidden.float(),self.weight).squeeze(-1)


def progress_loss(logits,labels):
    if (logits.ndim != 1 or not len(logits) or labels.shape != logits.shape
            or labels.device != logits.device or not logits.is_floating_point() or not labels.is_floating_point()
            or not torch.isfinite(logits).all() or not torch.isfinite(labels).all()
            or (labels < 0).any() or (labels > 1).any()):
        raise ValueError('Finite original selected progress labels in[0,1] required')
    return F.l1_loss(logits.float().sigmoid(),labels.float(),reduction='mean')
