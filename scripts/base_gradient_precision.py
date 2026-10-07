"""Readonly FP32/BF16 gradient metrics; a diagnostic screen, not a Base gate."""
import torch


def vector_metrics(reference, candidate):
    a, b = reference.detach().double().reshape(-1), candidate.detach().double().reshape(-1)
    if a.shape != b.shape or not a.numel() or not torch.isfinite(a).all() or not torch.isfinite(b).all():
        raise ValueError('Same nonempty finite gradient coordinates required')
    an, bn = a.norm(), b.norm()
    if an == 0:
        return dict(elements=a.numel(), reference_norm=0., candidate_norm=float(bn),
                    cosine=None, relative_L2_error=None, both_zero=bool(bn == 0))
    return dict(elements=a.numel(), reference_norm=float(an), candidate_norm=float(bn),
        cosine=float((a @ b)/(an*bn)) if bn > 0 else 0.,
        relative_L2_error=float((a-b).norm()/an), both_zero=False)


def first_AdamW_direction(gradient, epsilon=1e-8):
    """Data part of fresh AdamW's first update, after native global clip=1.

    This is an ephemeral diagnostic vector; no model/optimizer is updated.
    At update1 both bias corrections cancel beta1/beta2 factors. Decoupled
    decay is identical between paths and omitted from the data direction.
    """
    if epsilon <= 0 or not torch.isfinite(gradient).all():
        raise ValueError('Finite gradient and positive Adam epsilon required')
    g = gradient.detach().double().reshape(-1)
    g = g * min(1., 1./(float(g.norm())+1e-6))
    return g/(g.abs()+epsilon)


def comparison(reference, candidate, names):
    if set(reference) != set(candidate) or set(reference) != set(names):
        raise ValueError('Every distinct native parameter required')
    a = torch.cat([reference[n].reshape(-1) for n in names])
    b = torch.cat([candidate[n].reshape(-1) for n in names])
    groups = {}
    for name in names:
        group = '.'.join(name.split('.')[:3]) if name.startswith('model.layers.') else name.rsplit('.',1)[0]
        groups.setdefault(group, []).append(name)
    return dict(gradient=vector_metrics(a,b),
        fresh_AdamW_data_direction=vector_metrics(first_AdamW_direction(a),first_AdamW_direction(b)),
        groups={g:vector_metrics(torch.cat([reference[n].reshape(-1) for n in ns]),
                                  torch.cat([candidate[n].reshape(-1) for n in ns])) for g,ns in groups.items()})


def severe(metric):
    g, d = metric['gradient'], metric['fresh_AdamW_data_direction']
    if g['reference_norm'] < 1e-6 or g['cosine'] is None or d['cosine'] is None:
        return False
    return (g['cosine'] < .99 or g['relative_L2_error'] > .10
            or d['cosine'] < .98 or d['relative_L2_error'] > .20)


def screen(endpoints):
    """Both fixed endpoints, at least two original genres, same BF16 path."""
    if set(endpoints) != {'parent','CE100M'}:
        raise ValueError('Both predeclared endpoints required')
    result = {}
    for path in ('bf16_math','bf16_flash'):
        marked = {}
        for endpoint, value in endpoints.items():
            if set(value['sources']) != {'web','textbook','story','stress1024'}:
                raise ValueError('All original genres and fixed long window required')
            marked[endpoint] = [g for g in ('web','textbook','story') if severe(value['sources'][g]['comparisons'][path])]
        result[path] = dict(marked_sources=marked, supported=all(len(v)>=2 for v in marked.values()))
    return result
