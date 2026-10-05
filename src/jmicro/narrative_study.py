"""Held-out structural diagnostics for the literal-document comparison."""
import math


def structural_summary(body, documents):
    kinds = {r['doc_id']: r['structure'] for r in documents}
    rows = body['rows']
    if len(kinds) != len(documents) or {r['doc_id'] for r in rows} != set(kinds) or len(rows) != len(kinds):
        raise ValueError('Every held-out document must be scored once')
    result = {}
    for kind in sorted(set(kinds.values())):
        group = [r for r in rows if kinds[r['doc_id']] == kind]
        if any(r['scored_body_tokens'] != r['body_tokens'] for r in group):
            raise ValueError('Incomplete body scoring')
        byte_count = sum(r['body_bytes'] for r in group)
        result[kind] = dict(documents=len(group), body_bytes=byte_count,
            BPB=sum(r['body_nll'] for r in group) / math.log(2) / byte_count,
            mean_EOS_NLL=sum(r['eos_nll'] for r in group) / len(group))
    return result
