"""Generate original DEV400/long40 from isolated inputs; no TEST fallback.

The caller owns checkpoint qualification, GPU lock/budget and persistence.
This adapter returns raw failures; it does not score content or adopt a Base.
"""
import re

import torch
from torch.nn.attention import sdpa_kernel, SDPBackend

from jmicro.continuation_requests import LEGACY_SUPPRESS_IDS, load_requests, preflight_context, validate_outputs
from jmicro.japanese_evaluation import repetition_metrics


def sample_token(scores, generator):
    if generator is None:
        return int(scores.argmax())
    ordered, indexes = (scores / .8).sort(descending=True)
    probabilities = ordered.softmax(-1)
    drop = probabilities.cumsum(-1) - probabilities >= .9
    probabilities[drop] = 0
    return int(indexes[torch.multinomial(probabilities, 1, generator=generator)])


def raw_record(request, ids, tokenizer):
    unknown = 1 in ids
    # Original standard-suite UNK policy: no recoverable byte representation.
    # Preserve all raw IDs and expose this failure rather than replacing UNK.
    raw = b'' if unknown else tokenizer.decode_bytes(ids)
    try:
        text, valid = raw.decode('utf-8'), not unknown
    except UnicodeDecodeError:
        text, valid = raw.decode('utf-8', errors='replace'), False
    return dict(id=request.case_id, category=request.category, prefix=request.prefix, split='dev',
        decoding=request.decoding, suppressed=request.suppressed, seed=request.seed,
        max_new_tokens=request.max_new_tokens, generated_ids=ids, text=text, valid_utf8=valid,
        raw_utf8_hex=raw.hex(), unknown_id_present=unknown,
        role_leak=any(i in (4, 5, 6, 7) for i in ids), empty_response=not text.strip(),
        stop_reason='stop_id' if ids[-1] == 3 else 'max_new_tokens',
        repetition=bool(re.search(r'(.{2,}?)\1\1', text, flags=re.DOTALL)))


@torch.inference_mode()
def generate_isolated_continuations(model, tokenizer, manifest, pin, check, progress, device='cuda'):
    if model.training:
        raise ValueError('Actual eval-mode model required')
    planned, provenance = load_requests(manifest, pin)
    preflight_context(planned, tokenizer, maximum=model.config['max_position_embeddings'])
    standard, long = [], []
    with sdpa_kernel(SDPBackend.MATH):
        for request in planned:
            check()
            prefix = [2] + tokenizer.encode(request.prefix)
            current = torch.tensor([prefix], device=device)
            generator = (torch.Generator(device=device).manual_seed(request.seed)
                         if request.decoding == 'sampling' else None)
            ids, cache = [], None
            for _ in range(request.max_new_tokens):
                check()
                with torch.autocast(str(device).split(':')[0], dtype=torch.bfloat16,
                                    enabled=str(device).startswith('cuda')):
                    result = model(current, cache=cache, use_cache=True)
                cache = result.cache
                scores = result.logits[0, -1].clone()
                if not bool(torch.isfinite(scores).all()):
                    raise ValueError('Nonfinite native continuation logits')
                if request.suppressed:
                    scores[list(LEGACY_SUPPRESS_IDS)] = -torch.inf
                token = sample_token(scores, generator)
                if not 0 <= token < tokenizer.vocab_size:
                    raise ValueError('Raw token outside original vocabulary')
                ids.append(token)
                if token == 3:
                    break
                current = torch.tensor([[token]], device=device)
            row = raw_record(request, ids, tokenizer)
            if request.stage == 'standard400':
                row['human_scores'] = None
                standard.append(row)
            else:
                row.update(metrics=repetition_metrics(row), content_scores=None)
                long.append(row)
            progress(request.stage, len(standard) if request.stage == 'standard400' else len(long),
                     400 if request.stage == 'standard400' else 40)
    validate_outputs(standard, planned, 'standard400')
    validate_outputs(long, planned, 'long40')
    return dict(standard=dict(outputs=standard, split='dev', max_new_tokens=64,
        sampling_evaluated=True, temperature=.8, top_p=.9,
        suite_sha256=provenance['source_legacy_suite_sha256']),
        long=dict(rows=long, complete=True, expected=40), input_provenance=provenance,
        complete=True, TEST_opened=False, Base_qualified=False, content_review_completed=False)
