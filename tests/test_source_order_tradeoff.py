import copy
import math
import sys
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
from diagnose_source_order_tradeoff import pair_bodies,summarize


def body(rows):
    nll=sum(r['body_nll'] for r in rows);size=sum(r['body_bytes'] for r in rows)
    return dict(split='dev',documents=len(rows),body_bytes=size,body_tokens=sum(r['body_tokens'] for r in rows),
        body_nll=nll,eos_nll=sum(r['eos_nll'] for r in rows),bpb=nll/math.log(2)/size,rows=rows)


def test_common_byte_weighting_goldEOS_and_pair_identity():
    rows=[dict(doc_id='a',body_bytes=1,body_tokens=1,scored_body_tokens=1,body_nll=1.,eos_nll=3.),
          dict(doc_id='b',body_bytes=99,body_tokens=30,scored_body_tokens=30,body_nll=99.,eos_nll=1.)]
    changed=copy.deepcopy(rows);changed[0].update(body_nll=2.,eos_nll=1.)
    summary=summarize(pair_bodies(body(rows),body(changed)))
    assert summary['new']['BPB']==pytest.approx(101/math.log(2)/100)
    assert summary['body_worse_EOS_better']==1
    assert summary['body_NLL_change']==dict(improved=0,worsened=1,unchanged=1)
    assert summary['new']['gold_EOS_mean_NLL']==1.
    bad=copy.deepcopy(changed);bad[0]['doc_id']='other'
    with pytest.raises(ValueError):pair_bodies(body(rows),body(bad))
    bad=copy.deepcopy(changed);bad[1]['scored_body_tokens']=29
    with pytest.raises(ValueError):pair_bodies(body(rows),body(bad))
    bad=body(changed);bad['bpb']+=.01
    with pytest.raises(ValueError):pair_bodies(body(rows),bad)
    with pytest.raises(ValueError):pair_bodies(body(rows),dict(body(changed),split='test'))
