import sys
from types import SimpleNamespace
import numpy as np
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
from diagnose_mature_base_distribution import target_counts,span_index,matches


def test_eos_density_denominator_and_bytes_exclude_masked_and_eos():
    lengths=np.arange(64)
    counts=target_counts(np.array([8,9,-100,3,10,3]),lengths)
    assert counts==dict(teachers=5,EOS=2,masked_BOS=1,body_tokens=3,body_bytes=27)
    with pytest.raises(ValueError,match='Expected body'):
        target_counts(np.array([8,2,3]),lengths)


def test_span_references_do_not_cross_document_boundaries():
    a=list(range(8,33));b=list(range(33,58))
    packed=[2,*a,3,2,*b,3]
    view=SimpleNamespace(tokens=np.array(packed),offsets=np.array([0,27]),lengths=np.array([27,27]))
    index=span_index(view,lambda:None)
    assert matches(a[10:]+b[:10],view,index,lambda:None)['matched_windows']==0
    result=matches([80,*a,3,81],view,index,lambda:None)
    assert result['longest_exact_body_span']==dict(generated_offset=1,source_document_index=0,source_body_offset=0,tokens=25)
    assert result['matched_windows']==2


def test_longest_span_checks_all_shared_prefix_representatives():
    shared=list(range(8,32))
    a=[*shared,90,91];b=[*shared,92,93]
    view=SimpleNamespace(tokens=np.array([2,*a,3,2,*b,3]),offsets=np.array([0,28]),lengths=np.array([28,28]))
    result=matches(b,view,span_index(view,lambda:None),lambda:None)
    assert result['longest_exact_body_span']['source_document_index']==1
    assert result['longest_exact_body_span']['tokens']==26
