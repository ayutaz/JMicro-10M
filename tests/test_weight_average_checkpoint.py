from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import copy
import pytest
import torch
from weight_average_checkpoint import midpoint, TIED, PARENT_KEYS


def fixture(value):
    return dict(model_config=dict(tie_word_embeddings=True, hidden_size=2),
        model={TIED[0]:torch.full((3,2), value), TIED[1]:torch.full((3,2), value),
               'norm':torch.tensor([value, value + 2]), 'counter':torch.tensor([3])},
        lineage={k:0 for k in PARENT_KEYS}, optimizer={'state':'must not be copied'},
        sampler={'position':4}, scheduler={}, rng={})


def test_midpoint_roundtrip_alias_immutability_and_no_fake_full_state(tmp_path):
    a, b = fixture(2.), fixture(6.)
    original = copy.deepcopy(a)
    merged = midpoint(a, b, [{'sha256':'a'}, {'sha256':'b'}])
    assert torch.equal(merged['model']['norm'], torch.tensor([4.,6.]))
    assert all(torch.equal(a['model'][k], v) for k,v in original['model'].items())
    assert merged['model'][TIED[0]].data_ptr() == merged['model'][TIED[1]].data_ptr()
    assert not set(('optimizer','rng','scheduler','sampler','update','tokens')).intersection(merged)
    assert not merged['resumable_training_state']
    path = tmp_path / 'midpoint.pt'; torch.save(merged, path)
    saved = torch.load(path, weights_only=False)
    assert saved['model'][TIED[0]].data_ptr() == saved['model'][TIED[1]].data_ptr()
    # Deterministic repeated construction from unchanged inputs, including after save/load.
    repeated = midpoint(a,b,merged['lineage']['inputs'])
    assert all(torch.equal(v,repeated['model'][k]) for k,v in saved['model'].items())


def test_refuse_parent_configuration_state_shape_and_integer_disagreement():
    a,b = fixture(2.),fixture(6.)
    for mutate, message in (
        (lambda s:s['lineage'].update(parent_update=1),'actual learned parent'),
        (lambda s:s['model_config'].update(hidden_size=3),'configuration'),
        (lambda s:s['model'].pop('norm'),'State keys'),
        (lambda s:s['model'].update(norm=torch.ones(3)),'shape'),
        (lambda s:s['model'].update(counter=torch.tensor([4])),'Nonfloating')):
        other=copy.deepcopy(b); mutate(other)
        with pytest.raises(ValueError,match=message):midpoint(a,other,[])


def test_refuse_bad_tied_weights_and_nonfinite_or_cast_input():
    a,b = fixture(2.),fixture(6.)
    b['model'][TIED[1]][0,0]=7
    with pytest.raises(ValueError,match='embedding disagreement'):midpoint(a,b,[])
    for bad in (torch.tensor([float('nan'),1]), torch.tensor([float('inf'),1]), torch.ones(2,dtype=torch.bfloat16)):
        b=fixture(6.); b['model']['norm']=bad
        with pytest.raises(ValueError,match='FP32|dtype'):midpoint(a,b,[])
