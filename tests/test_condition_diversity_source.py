"""Nested data comparison must retain its exact control records."""
import copy
import sys
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/'scripts'))
from prepare_condition_diversity_source import nested


def test_retains_exact_small_records_and_rejects_duplicate_document_or_body():
    small=[dict(document_index=10,decoded_body_sha256='a',original_text='original')]
    large=small+[dict(document_index=11,decoded_body_sha256='b',original_text='additional')]
    nested(large,small)
    changed=copy.deepcopy(large); changed[0]['original_text']='rewritten'
    for invalid in (large[::-1],changed,large+[large[1]],
                    large+[dict(document_index=12,decoded_body_sha256='b')]):
        with pytest.raises(ValueError): nested(invalid,small)
