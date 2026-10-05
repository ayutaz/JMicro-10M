"""Regression coverage for the metrics/checkpoint finite-value type confusion."""
import copy
import sys

import pytest
import torch

from jmicro.experiment import ROOT

sys.path.insert(0,str(ROOT/"scripts"))
from measure_sequence_objective_timing import validate_timing


def fixture():
    counters=dict(skipped_rollouts=0,rollout_batches=4)
    rows=[dict(update=i,supervised_tokens=i*100,sequence_objective=copy.deepcopy(counters),
               loss=1.,sequence_UL=.2,optimization_loss=1.02,gradient_norm=.3,lr=.0002,
               seconds=.5,data_wait_seconds=.01,tokens_per_second=200.) for i in range(1,17)]
    state=dict(update=16,supervised_tokens=1600,lineage=dict(sequence_objective=counters),
               model=dict(weight=torch.tensor([1.])),optimizer=dict(state={0:dict(exp_avg=torch.tensor([.1]))}))
    return rows,state


def test_metrics_without_model_key_and_finite_full_checkpoint_pass():
    rows,state=fixture()
    validate_timing(rows,state,0,0)


@pytest.mark.parametrize("bad",["metric","model","optimizer","update","teachers","counter","seconds"])
def test_recovered_timing_rejects_nonfinite_and_inconsistent_state(bad):
    rows,state=fixture()
    if bad=="metric":rows[2]["loss"]=float("nan")
    elif bad=="model":state["model"]["weight"][0]=float("inf")
    elif bad=="optimizer":state["optimizer"]["state"][0]["exp_avg"][0]=float("nan")
    elif bad=="update":rows[2]["update"]=99
    elif bad=="teachers":state["supervised_tokens"]+=1
    elif bad=="counter":state["lineage"]["sequence_objective"]["rollout_batches"]+=1
    elif bad=="seconds":rows[3]["seconds"]=0.
    with pytest.raises(AssertionError):validate_timing(rows,state,0,0)
