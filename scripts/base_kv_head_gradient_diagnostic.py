"""Read-only attribution of shared K/V gradients to each query head."""
from contextlib import contextmanager
import math
from types import MethodType

import torch
from torch import nn
from torch.nn import functional as F

from jmicro.model import rope
from natural_context_contrast_trainer import right_padded_hidden


def path_statistics(a, b):
    a, b = a.detach().double(), b.detach().double()
    if a.shape != b.shape or a.ndim != 2 or not torch.isfinite(a).all() or not torch.isfinite(b).all():
        raise ValueError('Two finite matching projection gradients required')
    na, nb = float(a.norm()), float(b.norm())
    if not na or not nb:
        raise ValueError('Both query-head gradient paths must be nonzero')
    dot = float((a*b).sum())
    combined = float((a+b).norm())
    return dict(first_head_norm=na, second_head_norm=nb, dot=dot,
                cosine=dot/(na*nb), combined_norm=combined,
                cancellation_ratio=combined/(na+nb))


@contextmanager
def query_head_offsets(model):
    captured = []
    saved = []
    try:
        for layer, block in enumerate(model.model.layers):
            attn = block.self_attn
            saved.append((attn, 'forward' in attn.__dict__, attn.__dict__.get('forward')))

            def forward(self, x, positions, allowed, past, causal=False, layer=layer):
                if past is not None or self.qheads != self.kvheads*2:
                    raise ValueError('Uncached two-query-heads-per-KV diagnostic required')
                batch, length, _ = x.shape
                def project(module, heads):
                    return module(x).view(batch, length, heads, self.dim).transpose(1, 2)
                q = rope(self.q_norm(project(self.q_proj, self.qheads)), positions, self.theta)
                k = project(self.k_proj, self.kvheads)
                v = project(self.v_proj, self.kvheads)
                # Zero offsets expose each query path without detaching shared weights.
                expanded_k, expanded_v = k.repeat_interleave(2, 1), v.repeat_interleave(2, 1)
                leaf_k = torch.zeros_like(expanded_k, requires_grad=True)
                leaf_v = torch.zeros_like(expanded_v, requires_grad=True)
                query_k = rope(expanded_k+leaf_k, positions, self.theta)
                query_v = expanded_v+leaf_v
                attended = F.scaled_dot_product_attention(q, query_k, query_v,
                    attn_mask=None if causal else allowed[:, None], dropout_p=0.,
                    is_causal=causal, scale=self.scale)
                captured.append(dict(layer=layer, x=x.detach(), k=leaf_k, v=leaf_v))
                out = self.o_proj(attended.transpose(1, 2).reshape(batch, length, -1))
                return out, (rope(k, positions, self.theta), v)
            attn.forward = MethodType(forward, attn)
        yield captured
    finally:
        for attn, existed, original in saved:
            if existed:
                attn.forward = original
            else:
                attn.__dict__.pop('forward', None)


def decompose(model, inputs, targets):
    if (model.training or inputs.shape != targets.shape or model.config['qk_norm_type'] != 'none'
            or any(p.grad is not None for p in model.parameters())
            or any(b.self_attn.qheads != 2*b.self_attn.kvheads for b in model.model.layers)):
        raise ValueError('Unmodified eval-mode NoNorm GQA2 and original teacher masks required')
    selected = targets.ne(-100)
    if not selected.any():
        raise ValueError('Original supervised targets required')
    weights = [w for b in model.model.layers for w in (b.self_attn.k_proj.weight, b.self_attn.v_proj.weight)]
    hidden = right_padded_hidden(model, inputs)
    logits = F.linear(hidden[selected], model.lm_head.weight).float()
    loss = F.cross_entropy(logits, targets[selected])
    native = torch.autograd.grad(loss, weights)
    original_logits = logits.detach()
    del hidden, logits
    with query_head_offsets(model) as captured:
        hidden = right_padded_hidden(model, inputs)
        logits = F.linear(hidden[selected], model.lm_head.weight).float()
        split_loss = F.cross_entropy(logits, targets[selected])
        if (len(captured) != len(model.model.layers) or
                [r['layer'] for r in captured] != list(range(len(model.model.layers)))):
            raise ValueError('Exactly one native forward per layer required')
        leaves = [r[key] for r in captured for key in ('k', 'v')]
        grads = torch.autograd.grad(split_loss, [*weights, *leaves])
    logit_error = float((original_logits-logits.detach()).abs().max())
    first, second, groups = [], [], []
    max_error = relative_error = 0.
    for layer, row in enumerate(captured):
        attn = model.model.layers[layer].self_attn
        gk, gv = grads[len(weights)+2*layer:len(weights)+2*layer+2]
        # dW_head = sum_{batch,time} d(projected_K/V)_head outer x.
        dk = torch.einsum('bntd,bth->ndh', gk, row['x'])
        dv = torch.einsum('bntd,bth->ndh', gv, row['x'])
        for group in range(attn.kvheads):
            i, j = group*2, group*2+1
            a, b = torch.cat((dk[i], dv[i]), 0), torch.cat((dk[j], dv[j]), 0)
            expected = torch.cat([native[2*layer+k][group*attn.dim:(group+1)*attn.dim] for k in (0, 1)], 0)
            difference = expected-(a+b)
            max_error = max(max_error, float(difference.abs().max()))
            relative_error = max(relative_error, float(difference.double().norm()/expected.double().norm()))
            first.append(a.detach()); second.append(b.detach())
            groups.append(dict(layer=layer, KV_group=group, query_heads=[i, j],
                combined=path_statistics(a, b), K=path_statistics(dk[i], dk[j]), V=path_statistics(dv[i], dv[j])))
    native_error = max(float((a-b).abs().max()) for a, b in zip(native, grads[:len(weights)], strict=True))
    if (not torch.isfinite(loss) or not torch.isfinite(split_loss) or logit_error != 0.
            or float(loss.detach()) != float(split_loss.detach()) or native_error > 1e-5
            or max_error > 1e-5 or relative_error > 1e-4
            or any(p.grad is not None for p in model.parameters())):
        raise ValueError('Native logits/loss/all shared K/V gradients must match head attribution')
    stats = dict(loss=float(loss.detach()), teachers=int(selected.sum()), EOS_teachers=int(targets.eq(3).sum()),
        valid_inputs=int(inputs.ne(0).sum()), physical_inputs=inputs.numel(), logit_max_error=logit_error,
        native_gradient_max_error=native_error, decomposition_max_error=max_error,
        decomposition_relative_error=relative_error, groups=groups)
    return stats, torch.cat(first, 0), torch.cat(second, 0)


def interference_screen(sources):
    if set(sources) != {'web', 'textbook', 'story'}:
        raise ValueError('All three fixed TRAIN source summaries required')
    for row in sources.values():
        if not math.isfinite(row['cosine']) or not math.isfinite(row['cancellation_ratio']):
            raise ValueError('Finite actual head-gradient aggregates required')
    severe = [name for name, row in sources.items() if row['cosine'] <= -.1 and row['cancellation_ratio'] <= .9]
    return dict(severe_sources=severe, passed=len(severe) >= 2,
        rule='At least two of three source aggregates: cosine<=-0.1 and cancellation<=0.9 across all shared K/V groups.',
        causal_proof=False, Base_quality_gate=False,
        limitation='Failure closes this broad-cancellation screen; it does not prove all GQA capacity or representation choices adequate.')
