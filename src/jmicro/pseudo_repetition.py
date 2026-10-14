"""Prospective TRAIN sentence repetition decay, separate from ordinary CE.

DITTO-inspired probability matching, https://arxiv.org/abs/2206.02369.
Repeated copies are synthetic conditioning inputs, not new human documents or
gold teachers. This module never opens corpora or changes the native model.
"""
import hashlib
import re

import torch
from torch.nn import functional as F

DECAY = .5
COEFFICIENT = .1
MAXIMUM = 512
MAX_COPIES = 16
MAX_ROWS = 8
SENTENCE_END = re.compile(r'[。！？](?:[」』）)]*)')


def sentence_repeat_row(row, tokenizer):
    """Use original joint-body IDs at complete punctuation boundaries.

    Only fully supervised complete first windows qualify. Pick the first
    subsequent sentence with 8..128 tokens, original preceding context 8..256
    tokens and at least four whole copies fitting 512 prediction inputs.
    Long/partial units stay in ordinary CE unchanged. No re-encoding of parts,
    RNG, generated text, stored dataset, or quality-dependent selection.
    """
    if (not row['original_document_first_window']
            or row['original_body_tokens'] + 1 > 512
            or row['teacher_tokens'] != row['original_body_tokens'] + 1):
        return None
    body = row['input_ids'][1:]
    if (row['input_ids'][:1] != [2] or len(body) != row['original_body_tokens']
            or row['target_ids'] != body + [3]
            or any(type(i) is not int or not 8 <= i < 4096 for i in body)):
        raise ValueError('Original complete native body and EOS required')
    raw = tokenizer.decode_bytes(body)
    text = raw.decode('utf-8')
    if (hashlib.sha256(raw).hexdigest() != row['full_original_body_sha256']
            or tokenizer.encode(text) != body):
        raise ValueError('Original complete body byte/token identity differs')
    offsets, cursor = {0: 0}, 0
    for index, token in enumerate(body):
        piece = tokenizer.decode_bytes([token])
        if not piece:
            raise ValueError('Nonempty plain-body token bytes required')
        cursor += len(piece)
        offsets[cursor] = index + 1
    if cursor != len(raw):
        raise ValueError('Additive original codec byte offsets required')
    start_char = 0
    for match in SENTENCE_END.finditer(text):
        end_char = match.end()
        start_bytes = len(text[:start_char].encode('utf-8'))
        end_bytes = len(text[:end_char].encode('utf-8'))
        start_char = end_char
        if start_bytes not in offsets or end_bytes not in offsets:
            continue
        first, end = offsets[start_bytes], offsets[end_bytes]
        width = end - first
        if not 8 <= first <= 256 or not 8 <= width <= 128:
            continue
        copies = min(MAX_COPIES, (MAXIMUM - first) // width)
        if copies < 4:
            continue
        sentence, prefix = body[first:end], body[:first]
        sequence = [2] + prefix + sentence * copies
        # Position t predicts sequence[t+1]; original BOS is never repeated.
        inputs, targets = sequence[:-1], sequence[1:]
        current = list(range(first + width, first + width * copies))
        previous = [position - width for position in current]
        return dict(input_ids=inputs, target_ids=targets,
            current_positions=current, previous_positions=previous,
            source=row['source'], source_family=row['source_family'],
            original_body_sha256=row['full_original_body_sha256'],
            sentence_sha256=hashlib.sha256(tokenizer.decode_bytes(sentence)).hexdigest(),
            prefix_tokens=first, sentence_tokens=width, copies=copies,
            original_target_positions_used_as_references=width,
            pseudo_target_comparisons=len(current))
    return None


def repeat_rows(rows, tokenizer):
    """First eight eligible different families/bodies in existing batch order."""
    selected, families, bodies = [], set(), set()
    for row in rows:
        if row['source_family'] in families or row['full_original_body_sha256'] in bodies:
            continue
        built = sentence_repeat_row(row, tokenizer)
        if built is None:
            continue
        selected.append(built)
        families.add(row['source_family'])
        bodies.add(row['full_original_body_sha256'])
        if len(selected) == MAX_ROWS:
            break
    return selected


def repetition_decay_loss(logits, targets, current_positions, previous_positions):
    """Mean -log(1-|p_current-.5*stopgrad(p_previous)|), stably in logits.

    Inputs are a single unpadded synthetic row. Adjacent occurrences must
    predict identical body IDs. Compute 1-p from other vocabulary logits,
    retaining a corrective gradient even when exp(logp) rounds to one.
    The first occurrence only supplies detached references. EOS/PAD/roles,
    prefix and BOS are never negative targets. No probability clamping.
    """
    if (logits.ndim != 2 or logits.shape[-1] != 4096
            or targets.dtype != torch.long or targets.shape != logits.shape[:1]
            or targets.device != logits.device or not current_positions
            or len(current_positions) != len(previous_positions)
            or len(set(current_positions)) != len(current_positions)
            or any(type(i) is not int or type(j) is not int
                   or not 0 <= j < i < logits.shape[0]
                   for i, j in zip(current_positions, previous_positions))
            or not torch.isfinite(logits).all()):
        raise ValueError('Finite native4096 aligned pseudo repetition positions required')
    current = torch.tensor(current_positions, device=logits.device)
    previous = torch.tensor(previous_positions, device=logits.device)
    current_ids, previous_ids = targets[current], targets[previous]
    if (not torch.equal(current_ids, previous_ids)
            or bool(((current_ids < 8) | (current_ids >= 4096)).any())):
        raise ValueError('Identical plain-body IDs at adjacent copies required')
    scores = logits if logits.dtype == torch.float64 else logits.float()

    def chosen_logs(positions, ids):
        values = scores[positions]
        chosen = values.gather(-1, ids[:, None]).squeeze(-1)
        others = values.scatter(-1, ids[:, None], -torch.inf).logsumexp(-1)
        return -F.softplus(others - chosen), -F.softplus(chosen - others)

    logp, log_one_minus_p = chosen_logs(current, current_ids)
    prior_logp, _ = chosen_logs(previous, previous_ids)
    logq = prior_logp.detach() + torch.tensor(DECAY, device=logits.device,
                                             dtype=scores.dtype).log()
    # q <= .5: log(1-q) is stable with log1p, unlike current p near one.
    log_one_minus_q = torch.log1p(-logq.exp())
    downward = -torch.logaddexp(log_one_minus_p, logq)
    upward = -torch.logaddexp(log_one_minus_q, logp)
    loss = torch.where(logp > logq, downward,
           torch.where(logp < logq, upward, logp * 0))
    if not torch.isfinite(loss).all():
        raise ValueError('Nonfinite pseudo repetition decay loss')
    return loss.mean()
