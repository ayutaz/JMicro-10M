"""Check identical held-out populations before comparing Base checkpoints."""
import math


def validate_body(body, expected):
    rows = body['rows']
    if body['split'] != 'dev' or body['documents'] != len(expected) or len(rows) != len(expected):
        raise ValueError('Held-out document count/split differs')
    actual = [(row['doc_id'], row['body_bytes'], row['body_tokens']) for row in rows]
    if actual != expected:
        raise ValueError('Held-out population or order differs')
    if any(row['scored_body_tokens'] != row['body_tokens'] for row in rows):
        raise ValueError('Body targets must be scored exactly once')
    if any(not math.isfinite(row[key]) or row[key] < 0
           for row in rows for key in ('body_nll', 'eos_nll')):
        raise ValueError('Invalid held-out loss')
    for total, key in (('body_bytes', 'body_bytes'), ('body_tokens', 'body_tokens'),
                       ('body_nll', 'body_nll'), ('eos_nll', 'eos_nll')):
        if not math.isclose(body[total], sum(row[key] for row in rows), rel_tol=1e-12, abs_tol=1e-9):
            raise ValueError(f'Held-out {total} sum differs')
    if body['body_bytes'] <= 0 or not math.isclose(
        body['bpb'], body['body_nll'] / (math.log(2) * body['body_bytes']), rel_tol=1e-12):
        raise ValueError('BPB differs from common-byte loss')
    if body['context'] != 1024 or body['stride'] != 512 or body['evaluator'] != 'batched-heldout-fp32-ce-v1':
        raise ValueError('Scoring protocol differs')
    return True
