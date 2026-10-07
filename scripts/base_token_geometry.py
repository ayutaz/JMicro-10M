"""Read-only native token geometry; a severe-marker screen is not a quality gate."""
import torch
from torch.nn import functional as F

SOURCES = ('web','textbook','story')
COSINE_THRESHOLD = .95
PAIR_FRACTION_THRESHOLD = .25
MIN_SEPARATION = 4


def token_statistics(hidden, ids):
    if (hidden.ndim != 2 or ids.ndim != 1 or len(hidden) != len(ids)
            or not torch.isfinite(hidden).all()):
        raise ValueError('Finite matching token states and original input IDs required')
    body = ids.ge(8)
    states, tokens = hidden[body].float(), ids[body]
    positions = torch.arange(len(ids),device=ids.device)[body]
    if len(states) < 2 or (states.norm(dim=-1) == 0).any():
        raise ValueError('At least two nonzero original body states required')
    unit = F.normalize(states, dim=-1)
    cosine = unit @ unit.T
    all_pairs = ~torch.eye(len(states),device=ids.device,dtype=torch.bool)
    primary = all_pairs & tokens[:,None].ne(tokens[None,:]) & (
        positions[:,None]-positions[None,:]).abs().ge(MIN_SEPARATION)
    def summary(mask):
        values = cosine[mask]
        count = int(mask.sum())
        return dict(ordered_pairs=count, cosine_sum=float(values.double().sum()),
            cosine_mean=float(values.double().mean()) if count else None,
            cosine_above095_pairs=int(values.gt(COSINE_THRESHOLD).sum()))
    return dict(body_states=len(states), all_body_offdiagonal=summary(all_pairs),
                primary_distinct_ID_separated4=summary(primary))


def pool_source(rows):
    if len(rows) != 4:
        raise ValueError('Exactly four fixed TRAIN units per source required')
    result = {}
    for name in ('all_body_offdiagonal','primary_distinct_ID_separated4'):
        pairs = sum(row[name]['ordered_pairs'] for row in rows)
        if pairs <= 0:
            raise ValueError('Nonempty prespecified pair denominator required')
        high = sum(row[name]['cosine_above095_pairs'] for row in rows)
        result[name] = dict(ordered_pairs=pairs, cosine_above095_pairs=high,
            cosine_mean=sum(row[name]['cosine_sum'] for row in rows)/pairs,
            fraction_above095=high/pairs)
    result.update(documents=4, body_states=sum(row['body_states'] for row in rows),
        marker=result['primary_distinct_ID_separated4']['fraction_above095'] >= PAIR_FRACTION_THRESHOLD)
    return result


def severe_marker(models):
    if set(models) != {'parent','cached_CE','strong_staged'} or any(set(v) != set(SOURCES) for v in models.values()):
        raise ValueError('All three frozen models and same three fixed sources required')
    marked = {name:[source for source in SOURCES if model[source]['marker']]
              for name,model in models.items()}
    overlap = sorted(set(marked['parent']) & set(marked['cached_CE']))
    return dict(passed=len(overlap) >= 2, parent_and_CE_shared_marked_sources=overlap,
        marked_sources=marked,
        rule='FP32 normalized final native states; body IDs>=8; distinct input IDs; absolute position separation>=4; cosine>.95 in>=25percent ordered eligible pairs; same>=two sources in both original parent and cached CE',
        causal_proof=False, Base_quality_gate=False, global_isotropy_proof=False,
        limitation='Twelve fixed short TRAIN units; pooled pairs are correlated, not independent samples. A negative rules out this prespecified severe marker here, not all geometry effects. A positive only permits implementing one independent matched study.')
