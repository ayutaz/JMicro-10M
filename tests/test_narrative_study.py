import math
import pytest
from jmicro.narrative_study import structural_summary


def test_structural_scores_use_bytes_not_document_average():
    docs=[dict(doc_id='a',structure='quotation'),dict(doc_id='b',structure='quotation'),dict(doc_id='c',structure='conditional')]
    rows=[dict(doc_id=k,body_tokens=2,scored_body_tokens=2,body_bytes=n,body_nll=math.log(2)*v,eos_nll=e)
          for k,n,v,e in [('a',1,2,1),('b',3,3,3),('c',2,1,4)]]
    s=structural_summary(dict(rows=rows),docs)
    assert s['quotation']['BPB']==pytest.approx(1.25)
    assert s['quotation']['mean_EOS_NLL']==2
    assert s['conditional']['BPB']==pytest.approx(.5)


def test_structural_scores_reject_missing_or_duplicate_documents():
    docs=[dict(doc_id='a',structure='quotation')]
    with pytest.raises(ValueError):structural_summary(dict(rows=[]),docs)
    r=dict(doc_id='a',body_tokens=2,scored_body_tokens=2,body_bytes=1,body_nll=1,eos_nll=1)
    with pytest.raises(ValueError):structural_summary(dict(rows=[r,r]),docs)
    with pytest.raises(ValueError):structural_summary(dict(rows=[dict(r,scored_body_tokens=1)]),docs)
