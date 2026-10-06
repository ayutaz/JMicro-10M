"""Read-only fixed-block recovery and finite-displacement accounting."""
import hashlib
import math
import numpy as np
import torch


def recover_batch(tokens, byte_lengths, row, context=1024):
    xs,ys=[],[]
    for block in row['original_Web_blocks']:
        offset=int(block)*context
        if not 0<=offset<offset+context<len(tokens):
            raise ValueError('Fixed original block is outside TRAIN')
        x=np.asarray(tokens[offset:offset+context],dtype='<i8').copy()
        y=np.asarray(tokens[offset+1:offset+context+1],dtype='<i8').copy()
        y[y==2]=-100
        xs.append(x);ys.append(y)
    x,y=np.stack(xs),np.stack(ys)
    if (hashlib.sha256(x.tobytes()).hexdigest()!=row['input_sha256']
            or hashlib.sha256(y.tobytes()).hexdigest()!=row['target_sha256']
            or np.count_nonzero(y!=-100)!=row['teachers']
            or np.count_nonzero(y>=8)!=row['body_teachers']
            or np.count_nonzero(y==3)!=row['EOS_teachers']
            or int(byte_lengths[y[y>=8]].sum())!=row['body_bytes']
            or np.any(x==0) or np.any((y<8)&(y!=-100)&(y!=3))):
        raise ValueError('Exact original TRAIN input/target hash and counts required')
    return x,y


def directional_dot(gradients, directions):
    if len(gradients)!=len(directions) or not gradients:
        raise ValueError('Aligned nonempty unique parameter directions required')
    terms=[]
    for g,d in zip(gradients,directions,strict=True):
        if g.shape!=d.shape or not torch.isfinite(g).all() or not torch.isfinite(d).all():
            raise ValueError('Finite same-shape gradients/directions required')
        # FP32 forward/autograd, FP64 accumulation to avoid cancellation in the dot.
        terms.append(torch.sum(g.detach().double()*d.detach().double()))
    value=float(torch.stack(terms).sum())
    if not math.isfinite(value):raise ValueError('Nonfinite directional dot')
    return value


def summarize_displacement(loss0, loss_half, loss1, linear):
    if not all(math.isfinite(v) for v in (loss0,loss_half,loss1,linear)):
        raise ValueError('All three actual losses and linear prediction must be finite')
    change=loss1-loss0;residual=change-linear
    fraction=residual/change if change>0 else None
    return dict(actual_body_CE_change=change,first_order_body_CE_change=linear,
        nonlinear_residual=residual,nonlinear_fraction_of_positive_change=fraction,
        finite_difference_statistic=2*(loss1-2*loss_half+loss0),
        midpoint_minus_endpoint_mean=loss_half-(loss0+loss1)/2,
        harm_marker=change>=.02,first_order_predicts_increase=linear>0,
        nonlinear_half_or_more_marker=change>=.02 and fraction>=.5,
        limitations='Signed finite difference at0/.5/1 is not a Hessian or global convexity proof.')
