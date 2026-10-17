from pathlib import Path
import sys
import pytest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from inspect_chat_natural_observed import verify_resource_observation


def test_empty_nvml_is_explicitly_unknown_and_requires_direct_evidence():
    assert verify_resource_observation([],123,2,30,20)=='NVML_empty_ownership_not_established'
    with pytest.raises(ValueError):verify_resource_observation([],123,0,30,20)
    with pytest.raises(ValueError):verify_resource_observation([],123,2,19,20)


def test_foreign_reported_peer_remains_a_rejection():
    assert verify_resource_observation([123],123,2,30,20)=='UI_reported_by_NVML'
    with pytest.raises(ValueError):verify_resource_observation([123,456],123,2,30,20)
