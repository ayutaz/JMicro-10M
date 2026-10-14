from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import sys

import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from isolated_base_evaluation import generate_isolated_dev,validate_isolated_generation
from test_evaluation_boundary import prepared,guard_reads
from jmicro.evaluation_boundary import CASES_NAME


class Codec:
    def __init__(self,broken=False):self.broken=broken
    def encode(self,text):return [8,9]
    def decode_bytes(self,ids):
        return (b'\xff' if self.broken else b'x')*sum(i>=8 for i in ids)


class StubModel:
    """Deterministic token stub; this is no trained-model quality evidence."""
    def __init__(self,stop=True):self.stop=stop
    def __call__(self,ids,cache=None,use_cache=True):
        scores=torch.zeros((1,ids.shape[1],16))
        # Structural tokens have the largest raw scores and must be suppressed.
        scores[0,-1,4]=100
        scores[0,-1,3 if cache is not None and self.stop else 8]=10
        return SimpleNamespace(logits=scores,cache=object())


def test_actual_generation_and_review_use_only_two_DEV_files(tmp_path):
    path,pin,cases,_=prepared(tmp_path)
    (tmp_path/'base.sealed.test.jsonl').write_text('BROKEN_TEST_MUST_NOT_PARSE')
    (tmp_path/'base.jsonl').write_text('BROKEN_MIXED_SUITE_MUST_NOT_PARSE')
    guarded,observed=guard_reads({path,tmp_path/CASES_NAME})
    beats=[]
    with patch.object(Path,'open',guarded):
        result=generate_isolated_dev(StubModel(),Codec(),path,pin,
            lambda *args,**kw:beats.append(kw['completed_cases']),lambda:None,device='cpu')
        validate_isolated_generation(result,path,pin)
    assert observed==[str(path),str(tmp_path/CASES_NAME)]*2
    assert beats==list(range(8,81,8))
    assert len(result['outputs'])==80
    assert [r['prefix'] for r in result['outputs']]==[c['prefix'] for c in cases]
    assert all(r['generated_ids']==[8,3] and r['text']=='x' and not r['role_leak']
        and r['stop_reason']=='stop_id' for r in result['outputs'])


def test_invalid_UTF8_is_saved_as_failure_with_original_bytes(tmp_path):
    path,pin,_,_=prepared(tmp_path)
    result=generate_isolated_dev(StubModel(),Codec(True),path,pin,lambda *a,**k:None,lambda:None,device='cpu')
    assert all(not r['valid_utf8'] and r['raw_utf8_hex']=='ff' and r['text']=='\ufffd' for r in result['outputs'])


def test_max_length_and_raw_repetition_are_not_repaired(tmp_path):
    path,pin,_,_=prepared(tmp_path)
    result=generate_isolated_dev(StubModel(False),Codec(),path,pin,lambda *a,**k:None,lambda:None,device='cpu')
    assert all(len(r['generated_ids'])==64 and r['repetition'] and r['stop_reason']=='max_new_tokens' for r in result['outputs'])


def test_review_rejects_generation_manifest_substitution(tmp_path):
    path,pin,_,_=prepared(tmp_path)
    result=generate_isolated_dev(StubModel(),Codec(),path,pin,lambda *a,**k:None,lambda:None,device='cpu')
    result['suite_manifest_sha256']='0'*64
    with pytest.raises(ValueError):validate_isolated_generation(result,path,pin)
