"""Paired byte-weighted uncertainty and identity refusal, without GPU fixtures."""
import copy
import math
from pathlib import Path
import sys

import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from review_base_gradient_accumulation_pilot import paired_summary


def pair():
    old=dict(body=dict(bpb=1/math.log(2),rows=[
        dict(doc_id='a',body_tokens=10,body_bytes=100,body_nll=100.),
        dict(doc_id='b',body_tokens=90,body_bytes=900,body_nll=900.)]))
    new=copy.deepcopy(old)
    new['body']['rows'][0]['body_nll']=200.
    new['body']['rows'][1]['body_nll']=800.
    scores={str(i):dict(coherence=1) for i in range(80)}
    return old,new,scores


def test_unequal_bytes_bootstrap_uses_total_bytes_not_mean_document_bpb():
    old,new,scores=pair()
    result=paired_summary(old,new,scores,scores)
    assert result['BPB_difference']==0.
    # The four equally likely two-document draws give changes:
    # aa: 200/200 bits conversion; ab/ba:0; bb:-200/1800.
    assert result['paired_document_BPB_difference95CI']==pytest.approx([-1/(9*math.log(2)),1/math.log(2)])
    assert result['coherence_count_difference']==0
    assert result['coherence_fraction_difference95CI']==[0.,0.]


def test_mismatched_paired_document_identity_is_refused():
    old,new,scores=pair()
    new['body']['rows'][1]['doc_id']='other'
    with pytest.raises(ValueError,match='Same actual256 DEV'):
        paired_summary(old,new,scores,scores)
