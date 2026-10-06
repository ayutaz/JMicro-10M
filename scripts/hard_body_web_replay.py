"""Gold Web-body CE on non-EOS vocabulary, weighted by frozen parent mass."""
import copy
import torch
from torch.nn import functional as F
from web_kl_preservation import POLICY as INPUT_POLICY, WebBodyReplay as InputReplay

POLICY = dict(INPUT_POLICY,
    kind='frozen-parent-mass-weighted-gold-Web-body-non-EOS-CE-v1',
    direction='gold_to_student',
    masked_targets='Gold labels>=8; ignore EOS/BOS/role/padding target positions. Exclude EOS3 only from student vocabulary; retain all other vocabulary IDs.',
    reference_teacher='Immutable actual historical10.5B parent supplies detached non-EOS probability mass only, not soft targets.',
    objective='Mean over valid body positions: (1-parent_P(EOS3))*(-log student_P(gold|non-EOS)). Do not divide by probability mass.')


def body_gold_ce(student_logits, parent_logits, labels):
    if (student_logits.shape != parent_logits.shape
            or student_logits.shape[:-1] != labels.shape
            or student_logits.shape[-1] <= 8 or labels.dtype != torch.long):
        raise ValueError('Same vocabulary logits and integer shifted targets required')
    valid = labels >= 8
    positions = int(valid.sum())
    if not positions or (labels[valid] >= student_logits.shape[-1]).any():
        raise ValueError('At least one valid train Web body target required')
    keep = torch.arange(student_logits.shape[-1], device=student_logits.device) != 3
    # Reuse the prior study's exact probability-mass calculation and normalization.
    parent_logp = parent_logits.detach().float().log_softmax(-1)
    mass = parent_logp[..., keep].logsumexp(-1).exp()
    # Remove EOS3 before normalization, then map shifted gold IDs into that vocabulary.
    targets = torch.where(valid, labels - 1, -100)
    nll = F.cross_entropy(student_logits.float()[..., keep].reshape(-1, student_logits.shape[-1] - 1),
        targets.reshape(-1), ignore_index=-100, reduction='none').reshape(labels.shape)
    loss = (mass * nll)[valid].sum() / positions
    if not torch.isfinite(loss):
        raise ValueError('Finite gold-body CE required')
    return loss, dict(hard_body_teacher_tokens=positions,
        ignored_special_positions=labels.numel() - positions,
        physical_reference_input_tokens=labels.numel(), new_main_ordinary_CE_teacher_tokens=0,
        non_EOS_teacher_probability_mass=float(mass[valid].sum().detach()))


class HardBodyReplay(InputReplay):
    """Same input cursor and counters; objective binding prevents soft-target resume."""
    def state_dict(self):
        return dict(super().state_dict(), kind=POLICY['kind'])

    def load_state_dict(self, state):
        if state['kind'] != POLICY['kind']:
            raise ValueError('Hard gold-body replay binding required')
        converted = copy.deepcopy(state)
        converted['kind'] = INPUT_POLICY['kind']
        super().load_state_dict(converted)
