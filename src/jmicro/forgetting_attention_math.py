"""CPU reference algebra for a proposed architecture, not a model or trainer.

FoX equation11: causal key weights decay by the product of intervening
sigmoid gates. Padding does not advance that product. A future model must
still define a typed cache and safe handling of entirely invalid query rows.
"""
import torch
from torch.nn import functional as F


def forgetting_bias(gate_logits, valid, query_start=0):
    """Return [batch, heads, current_queries, all_keys] log decay and mask.

    Logits contain the complete physical history, including any cached prefix.
    Invalid query rows are all -inf; callers must not softmax those rows.
    Float64 is retained for independent CPU derivative checks. This reference
    intentionally makes no CUDA performance or runtime-cache claim.
    """
    if (gate_logits.ndim != 3 or not gate_logits.is_floating_point()
            or gate_logits.shape[-1] == 0 or gate_logits.shape[0] == 0
            or gate_logits.shape[1] == 0):
        raise ValueError('Nonempty floating batch/head/history gate logits required')
    batch, _, length = gate_logits.shape
    if (valid.dtype != torch.bool or valid.shape != (batch, length)
            or valid.device != gate_logits.device
            or type(query_start) is not int or not 0 <= query_start < length
            or not torch.isfinite(gate_logits).all()):
        raise ValueError('Finite gates, exact bool history mask and query offset required')
    logs = torch.where(valid[:, None], F.logsigmoid(gate_logits), 0.)
    cumulative = logs.cumsum(-1)
    bias = cumulative[:, :, query_start:, None] - cumulative[:, :, None, :]
    qpos = torch.arange(query_start, length, device=valid.device)
    kpos = torch.arange(length, device=valid.device)
    allowed = (valid[:, query_start:, None] & valid[:, None, :]
               & (kpos[None, :] <= qpos[:, None]))
    return bias.masked_fill(~allowed[:, None], -torch.inf)
