"""Sequence repetition loss for a separately budgeted research comparison.

Welleck et al. (2019/2020), https://arxiv.org/abs/1908.04319, section 5.2.
This module does not change historical CE training or inference. Candidates
come from decoded continuations, not from gold targets or fixed dev/test text.
"""
from collections.abc import Sequence

import torch
from torch.nn import functional as F


@torch.no_grad()
def greedy_rollout(model, prefixes, *, max_new_tokens=64):
    """Decode a fixed-width batch of train prefixes with native KV caching.

    The native Base special-token policy is explicit: suppress 0/1/2/4/5/6/7,
    retain EOS3, and pad only rows already stopped at an actual EOS. No forced
    end token, repetition blocking, sampling, or gold continuation is used.
    """
    if (prefixes.ndim != 2 or prefixes.numel() == 0 or prefixes.dtype != torch.long or
            bool(prefixes.eq(0).any()) or type(max_new_tokens) is not int or max_new_tokens <= 0 or
            prefixes.shape[1]+max_new_tokens > model.config["max_position_embeddings"]):
        raise ValueError("Expected unpadded fixed-width prefixes within the native context")
    was_training = model.training
    model.eval()
    try:
        out = model(prefixes, use_cache=True)
        finished = torch.zeros(prefixes.shape[0],dtype=torch.bool,device=prefixes.device)
        generated = []
        for step in range(max_new_tokens):
            scores = out.logits[:,-1].clone()
            scores[:,[0,1,2,4,5,6,7]] = -torch.inf
            ids = scores.argmax(-1).masked_fill(finished,0)
            generated.append(ids)
            finished |= ids.eq(3)
            if bool(finished.all()) or step+1 == max_new_tokens:
                break
            out = model(ids[:,None], attention_mask=ids[:,None].ne(0),
                        cache=out.cache,use_cache=True)
        return torch.stack(generated,dim=1)
    finally:
        model.train(was_training)


def continuation_logits(model, prefixes, generated_ids):
    """Differentiably score the exact rollout; position k-1 predicts token k.

    PAD positions of already stopped rows are masked in the native model. This
    is a separate small forward pass; the historical compiled CE path is intact.
    """
    if (prefixes.ndim != 2 or generated_ids.ndim != 2 or
            prefixes.shape[0] != generated_ids.shape[0] or prefixes.shape[1] == 0 or
            generated_ids.shape[1] == 0 or prefixes.dtype != torch.long or
            generated_ids.dtype != torch.long or prefixes.device != generated_ids.device):
        raise ValueError("Expected aligned nonempty prefix/continuation batches")
    ids = torch.cat((prefixes,generated_ids),dim=1)[:,:-1]
    logits = model(ids,attention_mask=ids.ne(0)).logits
    start = prefixes.shape[1]-1
    return logits[:,start:start+generated_ids.shape[1]]


def repeated_ngram_mask(continuations: Sequence[Sequence[int]], *, n: int = 4):
    """Mark all tokens of later repeated n-grams within each continuation.

    Prefix tokens must not be passed here. Overlapping occurrences are counted;
    their later occurrence is marked, and each token is penalized at most once.
    Native special IDs 0..7 break n-grams, and EOS3/EOT7 end the continuation.
    Legitimate repeated gold text is never passed as a generated negative.
    """
    if type(n) is not int or n < 2:
        raise ValueError("Expected an integer n-gram length >= 2")
    result = []
    for tokens in continuations:
        if any(type(token) is not int or token < 0 for token in tokens):
            raise ValueError("Continuations require nonnegative integer token IDs")
        marked = [False] * len(tokens)
        seen = set()
        segment = []
        for end, token in enumerate(tokens):
            if token in (3, 7):
                break
            if token < 8:
                segment.clear()
                seen.clear()
                continue
            segment.append(token)
            if len(segment) < n:
                continue
            gram = tuple(segment[-n:])
            if gram in seen:
                marked[end-n+1:end+1] = [True] * n
            seen.add(gram)
        result.append(marked)
    return result


def sequence_unlikelihood_sum(logits, generated_ids, negative_mask):
    """Sum -log(1-p(generated token)) at selected continuation positions.

    logits[b,t] must predict generated_ids[b,t] under its actual preceding
    prefix and generated history. The caller accounts for the generated input
    and candidates separately from CE teachers and chooses a frozen denominator.
    FP16/BF16 are promoted to FP32. The logit-space identity avoids clamping
    p near one (which would lose the corrective gradient).
    """
    if (logits.ndim != 3 or logits.shape[-1] < 2 or logits.numel() == 0 or
            generated_ids.shape != logits.shape[:2] or
            negative_mask.shape != generated_ids.shape or
            generated_ids.dtype != torch.long or negative_mask.dtype != torch.bool or
            generated_ids.device != logits.device or negative_mask.device != logits.device):
        raise ValueError("Expected aligned [batch,time,vocab] logits and long IDs/bool mask")
    ids = generated_ids[negative_mask]
    if ids.numel() == 0:
        return logits.reshape(-1)[0] * 0
    if bool(((ids < 8) | (ids >= logits.shape[-1])).any()):
        raise ValueError("Special or out-of-vocabulary IDs cannot be negative candidates")
    selected = logits[negative_mask]
    if selected.dtype in (torch.float16, torch.bfloat16):
        selected = selected.float()
    chosen = selected.gather(-1, ids[:, None]).squeeze(-1)
    others = selected.scatter(-1, ids[:, None], float("-inf"))
    return F.softplus(chosen - torch.logsumexp(others, dim=-1)).sum()
