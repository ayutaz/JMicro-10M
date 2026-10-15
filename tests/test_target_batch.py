"""Original labels stay exact across ragged, quota, overlap, EOS and PAD cases."""
import copy
import pytest
import torch
from jmicro.target_batch import pack_original_targets


@pytest.mark.parametrize('targets,width',[
    ([[8,9,3],[10,3]],3),
    ([[-100,8,-100,3],[-100,3]],4),
    ([[-100,-100],[-100]],4),
    ([[3],[4095,-100,3]],3),
    ([[8]*1024,[9]*512+[-100]*512],1024),
])
def test_tensor_mask_counts_dtype_stride_RNG_and_inputs_exact(targets,width):
    rows=[dict(input_ids=[8]*len(t),target_ids=t) for t in targets]
    saved=copy.deepcopy(rows)
    before=torch.get_rng_state().clone()
    reference=torch.full((len(rows),width),-100,dtype=torch.long)
    for i,r in enumerate(rows):
        reference[i,:len(r['target_ids'])]=torch.tensor(r['target_ids'])
    actual=pack_original_targets(rows,width,'cpu')
    assert torch.equal(reference,actual)
    assert torch.equal(reference.ne(-100),actual.ne(-100))
    assert actual.stride()==reference.stride() and actual.is_contiguous()
    assert actual.dtype==torch.long and actual.device.type=='cpu'
    assert rows==saved and torch.equal(before,torch.get_rng_state())


@pytest.mark.parametrize('rows,width',[
    ([],1),([dict(input_ids=[],target_ids=[])],1),
    ([dict(input_ids=[8],target_ids=[8,3])],2),
    ([dict(input_ids=[8,9],target_ids=[9,3])],1),
    ([dict(input_ids=[8],target_ids=[3])],0),
    ([dict(input_ids=[8],target_ids=[3])],True),
])
def test_bad_geometry_rejected_without_input_or_RNG_mutation(rows,width):
    saved=copy.deepcopy(rows)
    before=torch.get_rng_state().clone()
    with pytest.raises(ValueError): pack_original_targets(rows,width,'cpu')
    assert rows==saved and torch.equal(before,torch.get_rng_state())
