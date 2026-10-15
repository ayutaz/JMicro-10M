"""Normalized two-view vocabulary consistency; both probability paths learn."""
import torch
from torch.nn import functional as F

ARMS = ('disabled_native','normalized_rdrop')
POLICY = dict(kind='normalized_original_gold_two_view_RDrop_v1',dropout_probability=.1,
    sites=['token_embedding','attention_output_before_residual','MLP_output_before_residual'],
    attention_probability_dropout=0.,temperature=1.,symmetric_KL_coefficient=.5,
    objective='mean_two_view_CE_plus_half_mean_symmetric_KL',views=2,
    passes='two_sequential_retained_graphs_one_joint_backward',
    mask='exact_original_selected_body_and_EOS',both_distributions_have_gradient=True,
    inference='unchanged_native_eval_no_dropout_no_head')


def two_view_objective(first,second,targets):
    """Eq4/2 with alpha1: mean CE + .25*(KL(p||q)+KL(q||p))."""
    if (first.ndim != 2 or not len(first) or first.shape[1] < 2 or first.shape != second.shape
            or targets.shape != first.shape[:1] or targets.dtype != torch.long
            or first.device != second.device or first.device != targets.device
            or not first.is_floating_point() or not second.is_floating_point()
            or not torch.isfinite(first).all() or not torch.isfinite(second).all()
            or (targets < 0).any() or (targets >= first.shape[1]).any()):
        raise ValueError('Two finite selected vocabulary logits and unmasked original gold required')
    a,b = first.float(),second.float()
    first_ce,second_ce = F.cross_entropy(a,targets),F.cross_entropy(b,targets)
    lp,lq = F.log_softmax(a,dim=-1),F.log_softmax(b,dim=-1)
    # Jeffreys identity evaluates both directions, without detaching a teacher.
    symmetric = .5*((lp.exp()-lq.exp())*(lp-lq)).sum(-1).mean()
    ce = .5*(first_ce+second_ce)
    return dict(CE_view1_loss=first_ce,CE_view2_loss=second_ce,CE_loss=ce,
        symmetric_KL=symmetric,combined_loss=ce+.5*symmetric)
