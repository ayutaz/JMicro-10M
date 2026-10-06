"""Batched held-out scoring with the scalar window and body/EOS contracts."""
import time

import numpy as np
import torch
from torch.nn import functional as F

from jmicro.evaluation import bits_per_byte
from jmicro.training import autocast, isolated_evaluation, scoring_windows, synchronize


def evaluate_batched(model, shard, device, dtype='fp32', limit=None, context=1024, batch=16, progress=None):
    if shard.split not in ('dev', 'test') or batch < 1:
        raise ValueError('Batched scoring requires held-out records and positive batch')
    documents = shard.index[:limit]
    tasks, rows = [], []
    for index, document in enumerate(documents):
        count = document['body_tokens']
        rows.append({'doc_id': document['doc_id'], 'body_tokens': count, 'body_bytes': document['bytes'], 'body_nll': 0., 'eos_nll': 0., 'scored_body_tokens': 0})
        for start, end, first, last in scoring_windows(count, context, min(512, context - 1)):
            tasks.append((index, start, end, first, last, False))
        tasks.append((index, max(0, count + 2 - context), count + 1, count + 1, count + 2, True))
    tasks.sort(key=lambda item: item[2] - item[1])
    synchronize(device)
    started = time.perf_counter()
    with isolated_evaluation(model):
        for position in range(0, len(tasks), batch):
            chosen = tasks[position:position + batch]
            width = max(item[2] - item[1] for item in chosen)
            inputs = np.zeros((len(chosen), width), dtype=np.int64)
            targets = np.full_like(inputs, -100)
            mask = np.zeros_like(inputs, dtype=bool)
            for i, (index, start, end, first, last, _) in enumerate(chosen):
                offset = documents[index]['offset']
                inputs[i, :end - start] = shard.tokens[offset + start:offset + end]
                mask[i, :end - start] = True
                targets[i, first - start - 1:last - start - 1] = shard.tokens[offset + first:offset + last]
            x = torch.from_numpy(inputs).to(device)
            valid = torch.from_numpy(mask).to(device)
            y = torch.from_numpy(targets).to(device)
            with autocast(device, dtype):
                logits = model(x, attention_mask=valid).logits
            # FP32 per-token CE avoids BF16 reduction/rounding of whole windows.
            losses = F.cross_entropy(logits.float().transpose(1, 2), y, ignore_index=-100, reduction='none').sum(-1).cpu().tolist()
            for value, (index, _, _, first, last, eos) in zip(losses, chosen, strict=True):
                rows[index]['eos_nll' if eos else 'body_nll'] += value
                if not eos:
                    rows[index]['scored_body_tokens'] += last - first
            if progress is not None:
                progress(min(position + batch, len(tasks)), len(tasks))
    synchronize(device)
    seconds = time.perf_counter() - started
    if any(row['scored_body_tokens'] != row['body_tokens'] for row in rows):
        raise ValueError('Body targets were not scored exactly once')
    body_nll = sum(row['body_nll'] for row in rows)
    body_bytes = sum(row['body_bytes'] for row in rows)
    return {'split': shard.split, 'documents': len(rows), 'limit_documents': limit, 'context': context, 'stride': min(512, context - 1), 'batch': batch, 'body_nll': body_nll, 'eos_nll': sum(row['eos_nll'] for row in rows), 'body_bytes': body_bytes, 'body_tokens': sum(row['body_tokens'] for row in rows), 'bpb': bits_per_byte(body_nll, body_bytes), 'seconds': seconds, 'rows': rows, 'evaluator': 'batched-heldout-fp32-ce-v1', 'teacher_scope': 'body exactly once; BOS/PAD excluded, EOS loss separate'}
