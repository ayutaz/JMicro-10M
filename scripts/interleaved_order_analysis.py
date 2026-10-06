"""Paired four-cell descriptive contrasts, with common byte denominators."""
import math
import numpy as np
from shared_prefix_web_loss import validate_body

CELLS=('full_mixed','full_staged','masked_staged','masked_mixed')


def four_cell_contrasts(evaluations,scores):
    if set(evaluations)!=set(CELLS) or set(scores)!=set(CELLS):raise ValueError('Exactly four cells required')
    bodies={k:validate_body(ev['body']) for k,ev in evaluations.items()}
    alignment=[(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in bodies['full_mixed']]
    if any([(r['doc_id'],r['body_tokens'],r['body_bytes']) for r in rows]!=alignment for rows in bodies.values()):
        raise ValueError('Four common ordered body byte contracts required')
    keys=sorted(scores['full_mixed'])
    if any(sorted(s)!=keys for s in scores.values()):raise ValueError('Four common generation IDs required')
    def contrast(weights):
        nll=sum(weights[k]*np.array([r['body_nll'] for r in bodies[k]]) for k in CELLS)
        sizes=np.array([r['body_bytes'] for r in bodies['full_mixed']]);draws=np.random.default_rng(42).integers(0,len(nll),size=(2000,len(nll)))
        bpb=nll.sum()/math.log(2)/sizes.sum();bootstrap=nll[draws].sum(axis=1)/math.log(2)/sizes[draws].sum(axis=1)
        coherent=sum(weights[k]*np.array([int(scores[k][i]['coherence']==2) for i in keys]) for k in CELLS)
        draws=np.random.default_rng(42).integers(0,len(keys),size=(2000,len(keys)))
        return dict(weights=weights,body_BPB_change=float(bpb),body_paired_CI95=np.quantile(bootstrap,[.025,.975]).tolist(),
            coherence_count_change=int(coherent.sum()),coherence_paired_fraction_CI95=np.quantile(coherent[draws].mean(axis=1),[.025,.975]).tolist())
    result={}
    for name,a,b in [('order_effect_full','full_staged','full_mixed'),('order_effect_masked','masked_staged','masked_mixed'),
            ('target_effect_mixed','full_mixed','masked_mixed'),('target_effect_staged','full_staged','masked_staged')]:
        weights=dict.fromkeys(CELLS,0);weights[a]=-1;weights[b]=1;result[name]=contrast(weights)
    result['interaction_mask_effect_mixed_minus_staged']=contrast(dict(full_mixed=-1,full_staged=1,masked_staged=-1,masked_mixed=1))
    return dict(contrasts=result,body_documents=len(alignment),body_bytes=sum(r['body_bytes'] for r in bodies['full_mixed']),generation_examples=len(keys),
        limitations='Descriptive four-cell contrasts; repeated dev use/nonblind content/one learned seed/shared prefix. '
            'Target factor also changes hard teacher count and EOS fraction; no independent causal or human certification.')
