"""Typed factory recovery and changed residual metadata refusal."""
import copy
from pathlib import Path
import sys
import pytest
sys.path[:0]=[str(Path(__file__).resolve().parents[1]/'scripts')]
from base_parallel_residual_model import POLICY,parallel_config,model_from_config
from base_parallel_residual_trainer import KIND
from base_parallel_residual_evaluation import validate_record,typed_native_evaluation,native
from test_base_parallel_residual_model import config


def test_factory_scope_restored_after_error(tmp_path):
    factory,folder=native.JMicroModel,native.RUN
    with pytest.raises(RuntimeError):
        with typed_native_evaluation(tmp_path):
            assert native.JMicroModel is model_from_config and native.RUN==tmp_path
            raise RuntimeError('Evaluation fixture failure')
    assert native.JMicroModel is factory and native.RUN==folder


@pytest.mark.parametrize('arm',['sequential','parallel'])
def test_exact_tagged_record_and_changed_class_policy_count_refused(config,arm):
    name='ParallelResidualModel' if arm=='parallel' else 'JMicroModel'
    trained=dict(arm=arm,residual_policy=copy.deepcopy(POLICY),residual_model_class=name,
        model_config=parallel_config(config) if arm=='parallel' else config,
        spec=dict(kind=KIND,arm=arm,residual_policy=copy.deepcopy(POLICY),model_class=name,
                  actual_unique_parameters=config['expected_parameter_count']))
    validate_record(arm,trained)
    bad=copy.deepcopy(trained);bad['residual_model_class']='WrongModel'
    with pytest.raises(ValueError):validate_record(arm,bad)
    bad=copy.deepcopy(trained);bad['residual_policy']['residual_gain']=.5
    with pytest.raises(ValueError):validate_record(arm,bad)
    bad=copy.deepcopy(trained);bad['spec']['actual_unique_parameters']+=1
    with pytest.raises(ValueError):validate_record(arm,bad)
