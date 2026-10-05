"""Check diagnostic gradient accounting and raw/allowed probability distinction."""
import math
import sys

import pytest
import torch
from jmicro.experiment import ROOT

sys.path.insert(0,str(ROOT/"scripts"))
from diagnose_sequence_objective import gradient_summary,probability_summary


@pytest.mark.parametrize("aux,cosine,norm",[([3.,0.],1.,3.),([-3.,0.],-1.,3.),([0.,3.],0.,3.)])
def test_gradient_geometry_and_alpha_scaling(aux,cosine,norm):
    report=gradient_summary(dict(p=torch.tensor([2.,0.])),dict(p=torch.tensor(aux)))
    assert report["cosine"]==cosine and report["CE_norm"]==2. and report["UL_norm"]==norm
    assert report["alpha_combinations"]["0.1"]["weighted_UL_to_CE_norm"]==pytest.approx(.15)
    assert report["alpha_combinations"]["0.0"]["combined_norm_before_clip"]==2.
    expected=math.sqrt(4+1.2*cosine+.09)
    assert report["alpha_combinations"]["0.1"]["combined_norm_before_clip"]==pytest.approx(expected)


def test_empty_negative_gradient_has_zero_ratio_and_undefined_cosine():
    report=gradient_summary(dict(p=torch.tensor([1.])),dict(p=torch.tensor([0.])))
    assert report["UL_to_CE_norm"]==0 and report["cosine"] is None


def test_parameter_mismatch_is_not_silently_paired():
    with pytest.raises(ValueError):gradient_summary(dict(a=torch.ones(1)),dict(b=torch.ones(1)))


def test_blocked_special_mass_can_hide_conditional_generated_probability():
    logits=torch.full((1,2,10),-100.)
    logits[0,0,2]=math.log(.9);logits[0,0,3]=math.log(.05);logits[0,0,8]=math.log(.05)
    ids=torch.tensor([[8,0]]);negative=torch.tensor([[True,False]])
    report=probability_summary(logits,ids,negative)
    assert report["blocked_probability_mean"]==pytest.approx(.9)
    assert report["raw_negative_probability_mean"]==pytest.approx(.05)
    assert report["conditional_negative_probability_mean"]==pytest.approx(.5)
    assert report["raw_argmax_blocked_fraction"]==1.
