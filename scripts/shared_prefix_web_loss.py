"""Common-byte paired loss accounting at one fixed source-phase boundary."""
import math
import numpy as np


def validate_body(body):
    rows=body['rows']
    if (not rows or body['documents']!=len(rows) or len({r['doc_id'] for r in rows})!=len(rows)
            or any(r['body_tokens']!=r['scored_body_tokens'] or r['body_tokens']<=0 or r['body_bytes']<=0
                or not math.isfinite(r['body_nll']) or r['body_nll']<0 for r in rows)
            or sum(r['body_tokens'] for r in rows)!=body['body_tokens']
            or sum(r['body_bytes'] for r in rows)!=body['body_bytes']
            or not math.isclose(sum(r['body_nll'] for r in rows),body['body_nll'],rel_tol=1e-12)
            or not math.isclose(body['bpb'],body['body_nll']/math.log(2)/body['body_bytes'],rel_tol=1e-12)):
        raise ValueError('Complete finite common-byte body NLL required')
    return rows


def paired_difference(left,right):
    a,b=validate_body(left),validate_body(right)
    if [(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in a]!=[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in b]:
        raise ValueError('Same ordered document IDs/tokens/bytes required')
    differences=np.array([y['body_nll']-x['body_nll'] for x,y in zip(a,b,strict=True)])
    byte_counts=np.array([r['body_bytes'] for r in a])
    draws=np.random.default_rng(42).integers(0,len(a),size=(2000,len(a)))
    bootstrap=differences[draws].sum(axis=1)/math.log(2)/byte_counts[draws].sum(axis=1)
    return dict(BPB_change=float(differences.sum()/math.log(2)/byte_counts.sum()),
        paired_document_bootstrap_CI95=np.quantile(bootstrap,[.025,.975]).tolist(),documents=len(a),
        body_bytes=int(byte_counts.sum()),documents_increased=int((differences>0).sum()),documents_decreased=int((differences<0).sum()),
        rows=[dict(doc_id=x['doc_id'],body_tokens=x['body_tokens'],body_bytes=x['body_bytes'],body_NLL_change=float(d))
            for x,d in zip(a,differences,strict=True)],
        limitations='Document-paired byte-weighted descriptive dev bootstrap; one learned seed, repeated dev use, not independent causal certification.')


def decompose(bodies):
    if set(bodies)!={'historical','shared_prefix','strong_staged','masked_suffix'}:raise ValueError('Only the four fixed stages required')
    pairs={name:paired_difference(bodies[a],bodies[b]) for name,a,b in (
        ('shared_prefix_minus_historical','historical','shared_prefix'),
        ('strong_minus_shared_prefix','shared_prefix','strong_staged'),
        ('masked_minus_shared_prefix','shared_prefix','masked_suffix'),
        ('strong_minus_historical','historical','strong_staged'),
        ('masked_minus_historical','historical','masked_suffix'))}
    for final in ('strong','masked'):
        if not math.isclose(pairs['shared_prefix_minus_historical']['BPB_change']+pairs[final+'_minus_shared_prefix']['BPB_change'],
                pairs[final+'_minus_historical']['BPB_change'],abs_tol=1e-12):raise ValueError('Additive phase decomposition differs')
    return dict(BPB={k:v['bpb'] for k,v in bodies.items()},comparisons=pairs,
        historical_guard_limit=bodies['historical']['bpb']*1.01,
        shared_prefix_already_exceeds_historical_guard=bodies['shared_prefix']['bpb']>bodies['historical']['bpb']*1.01,
        additivity_verified=True,
        interpretation='Shared prefix has zero conditional teachers, but contains story and ordinary teachers. '
            'Suffix still includes159637 ordinary teachers plus conditional. No individual source, amount or capacity cause is isolated.')
