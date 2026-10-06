"""Keep the weighted conditional non-EOS KL; omit only the Bernoulli EOS term."""
import copy
import torch
from torch.nn import functional as F
from web_kl_preservation import POLICY as ORIGINAL_POLICY, WebBodyReplay as OriginalReplay

POLICY = dict(ORIGINAL_POLICY,kind='frozen-parent-Web-body-conditional-non-EOS-KL-v1',
    masked_targets='labels>=8; ignore EOS/BOS/role/padding target positions. Remove EOS3 from student conditional vocabulary; preserve parent non-EOS mass weight and all remaining vocabulary IDs.',
    objective_component='Full parent-to-student KL minus Bernoulli EOS-mass KL; exact weighted conditional non-EOS component only.')


def body_parent_kl(student_logits,parent_logits,labels):
    if student_logits.shape != parent_logits.shape or student_logits.shape[:-1] != labels.shape:
        raise ValueError('Same vocabulary logits and shifted targets required')
    valid = labels >= 8; positions = int(valid.sum())
    if not positions:
        raise ValueError('At least one train Web body target required')
    parent = parent_logits.detach().float().log_softmax(-1)
    keep = torch.arange(parent.shape[-1],device=parent.device) != 3
    parent_other = parent[...,keep]
    mass_log = parent_other.logsumexp(-1)
    parent_conditional = parent_logits.detach().float()[...,keep].log_softmax(-1)
    # Selecting the student non-EOS logits first gives exactly zero direct EOS-logit gradient.
    student_conditional = student_logits.float()[...,keep].log_softmax(-1)
    loss = F.kl_div(student_conditional,parent_conditional,log_target=True,reduction='none').sum(-1)
    loss = (loss * mass_log.exp())[valid].sum() / positions
    if not torch.isfinite(loss):
        raise ValueError('Finite conditional non-EOS KL required')
    mass = float(mass_log.exp()[valid].sum().detach())
    return loss,dict(soft_target_body_positions=positions,ignored_special_positions=labels.numel()-positions,
        physical_reference_input_tokens=labels.numel(),new_ordinary_CE_teacher_tokens=0,
        non_EOS_teacher_probability_mass=mass)


class WebBodyReplay(OriginalReplay):
    """Version the objective binding while retaining identical replay sampler/counters."""
    def state_dict(self):
        return dict(super().state_dict(),kind=POLICY['kind'])

    def load_state_dict(self,state):
        if state['kind'] != POLICY['kind']:
            raise ValueError('Conditional-KL replay binding required')
        converted = copy.deepcopy(state); converted['kind'] = ORIGINAL_POLICY['kind']
        super().load_state_dict(converted)
