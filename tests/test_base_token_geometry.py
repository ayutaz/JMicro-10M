"""Independent small-vector checks; no GPU or language quality evidence."""
from pathlib import Path
import sys
import pytest
import torch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from base_token_geometry import token_statistics, pool_source, severe_marker


def test_pairs_exclude_special_same_token_nearby_and_diagonal_independent_loop():
    ids=torch.tensor([2,8,9,10,8,11,12,3])
    hidden=torch.arange(16,dtype=torch.float32).reshape(8,2)+1
    result=token_statistics(hidden,ids)
    selected=[]
    for i in range(8):
        for j in range(8):
            if ids[i]>=8 and ids[j]>=8 and ids[i]!=ids[j] and abs(i-j)>=4:
                a,b=hidden[i].double(),hidden[j].double()
                selected.append(float(a.dot(b)/(a.norm()*b.norm())))
    primary=result['primary_distinct_ID_separated4']
    assert primary['ordered_pairs']==len(selected)==6
    assert primary['cosine_mean']==pytest.approx(sum(selected)/len(selected),abs=1e-7)
    assert result['all_body_offdiagonal']['ordered_pairs']==30


def test_collapsed_and_orthogonal_states_and_unequal_pair_pool_denominators():
    ids=torch.arange(8,16)
    same=token_statistics(torch.ones(8,2),ids)
    apart=token_statistics(torch.eye(8),ids)
    assert same['primary_distinct_ID_separated4']['cosine_above095_pairs']==20
    assert apart['primary_distinct_ID_separated4']['cosine_mean']==0
    short=token_statistics(torch.ones(6,2),torch.arange(8,14))
    result=pool_source([same,apart,short,short])
    assert result['primary_distinct_ID_separated4']['fraction_above095']==pytest.approx(32/52)
    assert result['marker'] is True


def test_marker_requires_same_two_sources_in_both_failing_models():
    sources=('web','textbook','story')
    def models(marked):
        return {name:{source:dict(marker=source in selected) for source in sources}
                for name,selected in marked.items()}
    positive=models(dict(parent=sources[:2],cached_CE=sources[:2],strong_staged=[]))
    assert severe_marker(positive)['passed'] is True
    negative=models(dict(parent=sources[:2],cached_CE=sources[1:],strong_staged=sources))
    assert severe_marker(negative)['passed'] is False
    with pytest.raises(ValueError):
        severe_marker({'parent':positive['parent']})


def test_zero_nonfinite_malformed_states_and_empty_pool_rejected():
    ids=torch.arange(8,16)
    for states in (torch.zeros(8,2),torch.full((8,2),float('nan')),torch.ones(7,2)):
        with pytest.raises(ValueError): token_statistics(states,ids)
    with pytest.raises(ValueError): pool_source([])
    row=token_statistics(torch.eye(3),torch.arange(8,11))
    with pytest.raises(ValueError): pool_source([row]*4)
