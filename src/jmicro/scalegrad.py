"""One-pass ScaleGrad-inspired hard-label loss; inference remains native.

Paper Eq4-6: https://proceedings.mlr.press/v139/lin21b/lin21b.pdf
This adaptation uses the visible original BODY input prefix, not a flat
target stream. Logit shifting omits the official probability code's epsilon.
"""
import math
import torch
from torch.nn import functional as F

GAMMA = .2
ARMS = ('native_CE_control','scalegrad')
POLICY = dict(kind='original_visible_body_prefix_ScaleGrad_logit_shift_0p2_v1',
    gamma=GAMMA,history='same_window_BODY_input_IDs_at_columns_le_current_prediction_column',
    special_history='IDs0to7_never_enter_BODY_history_EOS3_remains_novel',
    target='unchanged_original_selected_hard_body_and_EOS',
    normalization='cross_entropy_of_logits_plus_log_gamma_times_novel_mask',
    original_CE='metric_only_when_active_not_added_twice',
    decoder_passes=1,dropout=0.,extra_parameters=0,
    inference='unchanged_native_logits_softmax_cache_and_decoder')


def selected_novel_mask(rows,vocab_size,device):
    """Causal row-major selected mask without [batch,time,vocab] allocation.

    First occurrences can inspect the row once because a token becomes seen
    only after its first occurrence's position is reached. Masked overlap
    inputs still count as history. Rows/windows have independent histories.
    """
    if (not isinstance(rows,list) or not rows or type(vocab_size) is not int
            or vocab_size < 9):
        raise ValueError('Nonempty original rows and native body vocabulary required')
    first,coordinates = [],[]
    for row_index,row in enumerate(rows):
        ids,targets = row['input_ids'],row['target_ids']
        if (not isinstance(ids,list) or not isinstance(targets,list)
                or not 0 < len(ids) == len(targets) <= 1024
                or any(type(t) is not int or not (t == 2 or 8 <= t < vocab_size) for t in ids)
                or any(type(t) is not int or not (t in (-100,3) or 8 <= t < vocab_size) for t in targets)):
            raise ValueError('Aligned original BODY/BOS inputs and hard BODY/EOS/-100 labels required')
        positions = [1024]*vocab_size
        for column,token in enumerate(ids):
            if token >= 8 and positions[token] == 1024:
                positions[token] = column
            if targets[column] != -100:
                coordinates.append((row_index,column))
        first.append(positions)
    if not coordinates:
        raise ValueError('Nonempty original selected teachers required')
    first = torch.tensor(first,dtype=torch.int32,device=device)
    coordinate = torch.tensor(coordinates,dtype=torch.long,device=device)
    return first[coordinate[:,0]] > coordinate[:,1,None]


def scalegrad_objective(logits,targets,novel_mask,gamma=GAMMA):
    """Original CE metric plus the separately named hard-label learning loss."""
    if (logits.ndim != 2 or not len(logits) or logits.shape[1] < 9
            or not logits.is_floating_point() or targets.dtype != torch.long
            or targets.shape != (len(logits),) or targets.device != logits.device
            or novel_mask.dtype != torch.bool or novel_mask.shape != logits.shape
            or novel_mask.device != logits.device or type(gamma) not in (int,float)
            or not math.isfinite(gamma) or not 0 < gamma <= 1
            or bool(((targets < 0) | (targets >= logits.shape[1])).any())):
        raise ValueError('Aligned selected native logits/labels/novelty and gamma in(0,1] required')
    values = logits if logits.dtype == torch.float64 else logits.float()
    if gamma == 1:
        ce = loss = F.cross_entropy(values,targets)
    else:
        with torch.no_grad():
            ce = F.cross_entropy(values,targets)
        shifted = values+novel_mask.to(values.dtype)*math.log(gamma)
        loss = F.cross_entropy(shifted,targets)
    return dict(CE_loss=ce,ScaleGrad_loss=loss,combined_loss=loss)
