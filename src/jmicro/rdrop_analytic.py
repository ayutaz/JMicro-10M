"""Separate first-order loss storage runtime; native decoder is untouched."""
import torch
from torch.nn import functional as F

IMPLEMENTATION = 'FP32_two_logprob_saved_analytic_first_order_RDrop_v1'


class _AnalyticLoss(torch.autograd.Function):
    @staticmethod
    def forward(ctx,first,second,targets):
        a,b = first.float(),second.float()
        ce1,ce2 = F.cross_entropy(a,targets),F.cross_entropy(b,targets)
        lp,lq = F.log_softmax(a,dim=-1),F.log_softmax(b,dim=-1)
        symmetric = .5*((lp.exp()-lq.exp())*(lp-lq)).sum(-1).mean()
        ctx.save_for_backward(lp,lq,targets)
        ctx.first_dtype,ctx.second_dtype = first.dtype,second.dtype
        return ce1,ce2,symmetric

    @staticmethod
    def backward(ctx,ce1_grad,ce2_grad,symmetric_grad):
        if torch.is_grad_enabled():
            raise RuntimeError('This fixed analytic runtime supports first-order gradients only')
        lp,lq,targets = ctx.saved_tensors
        n = lp.shape[0]
        scale = symmetric_grad*.5/n
        # Match the reference product, subtraction, exp and log_softmax chain
        # rule. Only newly owned temporary buffers are changed in-place.
        p,q = lp.exp(),lq.exp()
        t = lp-lq
        t.mul_(scale)
        u = p-q
        u.mul_(scale)
        p.mul_(t).add_(u)
        t.neg_()
        q.mul_(t).sub_(u)
        del t,u
        ga = torch.ops.aten._log_softmax_backward_data(p,lp,-1,torch.float32)
        gb = torch.ops.aten._log_softmax_backward_data(q,lq,-1,torch.float32)
        del p,q
        total = lp.new_tensor(n)
        nll = torch.ops.aten.nll_loss_backward(ce1_grad,lp,targets,None,1,-100,total)
        ce_grad = torch.ops.aten._log_softmax_backward_data(nll,lp,-1,torch.float32)
        ga.add_(ce_grad)
        del nll,ce_grad
        nll = torch.ops.aten.nll_loss_backward(ce2_grad,lq,targets,None,1,-100,total)
        ce_grad = torch.ops.aten._log_softmax_backward_data(nll,lq,-1,torch.float32)
        gb.add_(ce_grad)
        return ga.to(ctx.first_dtype),gb.to(ctx.second_dtype),None


def analytic_two_view_objective(first,second,targets):
    if (first.ndim != 2 or not len(first) or first.shape[1] < 2 or first.shape != second.shape
            or targets.shape != first.shape[:1] or targets.dtype != torch.long
            or first.device != second.device or first.device != targets.device
            or not first.is_floating_point() or not second.is_floating_point()
            or not torch.isfinite(first).all() or not torch.isfinite(second).all()
            or (targets < 0).any() or (targets >= first.shape[1]).any()):
        raise ValueError('Two finite selected vocabulary logits and unmasked original gold required')
    ce1,ce2,symmetric = _AnalyticLoss.apply(first,second,targets)
    ce = .5*(ce1+ce2)
    return dict(CE_view1_loss=ce1,CE_view2_loss=ce2,CE_loss=ce,
        symmetric_KL=symmetric,combined_loss=ce+.5*symmetric)
