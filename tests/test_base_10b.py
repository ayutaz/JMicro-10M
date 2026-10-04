"""Scope and budget guards for the direct10B preparation command."""
from pathlib import Path
import sys

import pytest

sys.path.insert(0,str(Path(__file__).resolve().parents[1] / 'scripts'))
from run_base_10b import parser, require_prepared, sanity
from jmicro.experiment import read_json, ROOT


@pytest.mark.parametrize('args',[[],['--train','--verify-only'],['--freeze','--train']])
def test_mode_must_be_explicit_and_exclusive(args):
    with pytest.raises(SystemExit):
        parser().parse_args(args)


def test_verification_mode_never_requests_training():
    args = parser().parse_args(['--verify-only'])
    assert args.verify_only and not args.train and not args.freeze


def plan():
    previous = read_json(ROOT / 'configs/phase6/base_5b.json')
    previous.update(parent=dict(tokens=4750016512,update=144959,spec=previous['spec']),
        spec=dict(previous['spec'],schedule_updates=289917),stable_end_update=289917,
        stable_end_tokens=9500000256,decay_updates=15259,end_update=305176,end_tokens=10000007168,
        additional_training_tokens=5249990656,output='reports/phase6/base-10b-20261004',
        preparation_gpu_budget_seconds=600,gpu_budget_seconds=9000,reserved_evaluation_gpu_seconds=1800)
    return previous


def test_budget_is_direct10B_and_separate_from_verification():
    value = plan()
    sanity(value)
    assert value['additional_training_tokens'] + value['parent']['tokens'] == value['end_tokens']
    assert value['end_tokens'] >= 10_000_000_000
    assert value['verification_input_tokens'] == 524288


@pytest.mark.parametrize('change',[dict(end_tokens=7500005376),dict(output='reports/phase6/base-5b-20261004'),
                                 dict(unique_train_tokens=9_000_000_000)])
def test_rejects_partial_target_historical_output_or_data_wrap(change):
    value = plan()
    value.update(change)
    with pytest.raises(AssertionError):
        sanity(value)


def test_training_requires_saved_successful_preparation(tmp_path):
    with pytest.raises(FileNotFoundError):
        require_prepared(tmp_path,{})
