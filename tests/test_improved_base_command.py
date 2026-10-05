import sys
import pytest
from jmicro.experiment import ROOT,write_json

sys.path.insert(0,str(ROOT/"scripts"))
from run_improved_base import preflight


def test_extension_refuses_incomplete_comparison_before_checkpoint_or_gpu(tmp_path):
    run = tmp_path/"comparison";run.mkdir();write_json(run/"job.json",dict(status="running"))
    recipe = tmp_path/"recipe.json";write_json(recipe,dict(source_run=str(run)))
    with pytest.raises(ValueError,match="actually finish"):
        preflight(recipe)


def test_complete_record_with_actually_live_identity_still_refuses_freeze(tmp_path):
    from types import SimpleNamespace
    from phase6_performance import identity
    from run_improved_base import freeze
    run = tmp_path/"comparison";run.mkdir();write_json(run/"job.json",dict(status="complete",**identity()))
    recipe = tmp_path/"recipe.json"
    args = SimpleNamespace(source_run=run,parent_point="large-2000000000",reference_point="large-100000000",target_teachers=5000000000)
    with pytest.raises(ValueError,match="actually finish"):
        freeze(recipe,args)
    assert not recipe.exists()
