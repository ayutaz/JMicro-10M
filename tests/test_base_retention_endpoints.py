import copy
import math
import sys
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
from diagnose_base_retention_endpoints import endpoint,paired_documents


def test_terminal_utf8_and_internal_corruption_are_separate():
    assert endpoint('楓'.encode())['kind']=='complete_UTF8'
    assert endpoint('楓'.encode()[:2])==dict(kind='unfinished_terminal_character',valid_prefix_bytes=0,
        trailing_bytes_hex='e6a5',pending_bytes=2)
    assert endpoint(b'ok\xe6\xa5 ')['kind']=='invalid_byte_sequence'
    assert endpoint('\ufffd'.encode())['kind']=='complete_UTF8'


def test_paired_byte_contributions_use_pooled_bytes_and_preserve_targets():
    old=[dict(doc_id=str(i),body_bytes=i+1,body_tokens=1,scored_body_tokens=1,body_nll=2*(i+1),eos_nll=.5) for i in range(256)]
    new=copy.deepcopy(old);new[0]['body_nll']=1;new[-1]['body_nll']=0
    r=paired_documents(old,new,old)
    expected=(-1-512)/math.log(2)/sum(range(1,257))
    assert math.isclose(r['paired_BPB_difference'],expected)
    assert math.isclose(sum(v['global_BPB_difference_contribution'] for v in r['quartiles']),expected)
    assert r['original_Web_documents_improved']==2 and all(v['documents']==64 for v in r['quartiles'])
    new[-1]['doc_id']='different'
    with pytest.raises(ValueError,match='ordered body'):paired_documents(old,new,old)
