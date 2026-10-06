import copy
import math
import sys
from pathlib import Path
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from shared_prefix_web_loss import paired_difference,decompose,validate_body


def body(nll):
    rows=[dict(doc_id=str(i),body_tokens=2,scored_body_tokens=2,body_bytes=size,body_nll=value)
        for i,(value,size) in enumerate(zip(nll,[1,9],strict=True))]
    return dict(rows=rows,documents=2,body_tokens=4,body_bytes=10,body_nll=sum(nll),bpb=sum(nll)/math.log(2)/10)


def test_paired_byte_ratio_is_not_arithmetic_mean_of_document_BPB():
    a,b=body([1,1]),body([2,1]);r=paired_difference(a,b)
    assert r['BPB_change']==pytest.approx(1/math.log(2)/10)
    assert r['BPB_change']!=pytest.approx(1/math.log(2)/2)
    assert r['documents_increased']==1 and r['documents_decreased']==0


def test_additive_prefix_and_suffix_are_separate_from_conditional_causality():
    r=decompose(dict(historical=body([1,1]),shared_prefix=body([2,2]),strong_staged=body([3,4]),masked_suffix=body([2,3])))
    assert r['additivity_verified'] and r['shared_prefix_already_exceeds_historical_guard']
    assert r['comparisons']['strong_minus_historical']['BPB_change']==pytest.approx(5/math.log(2)/10)


def test_reject_changed_document_bytes_incomplete_tokens_duplicate_ids_and_nonfinite():
    original=body([1,1]);wrong=copy.deepcopy(original);wrong['rows'].reverse()
    with pytest.raises(ValueError):paired_difference(original,wrong)
    for field,value in [('body_bytes',5),('scored_body_tokens',1),('doc_id','1'),('body_nll',float('nan'))]:
        wrong=copy.deepcopy(original);wrong['rows'][0][field]=value
        with pytest.raises(ValueError):validate_body(wrong)
