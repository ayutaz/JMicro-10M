import copy
import sys
import pytest
from jmicro.experiment import ROOT
sys.path.insert(0,str(ROOT/"scripts"))
import run_larger_material_comparison as runner
from review_larger_material import validate_notes


def recipe():
    return dict(arms={name:dict(teachers=1000000000,boundaries=[1000000000],evaluate=[1000000000]) for name in ("small","large")},
        stable_teacher_budget=2000000000,decay_teacher_tokens=20000000,decay_teacher_budget=40000000,
        scientific_teacher_budget=2040000000,prepared_tokens=dict(small=500000005,large=2000000020),
        source_ratio=dict(web=.95,story=.05),peak_lr=.002,warmup_updates=200,GPU_budget_seconds=5000,
        quality_criteria_unchanged=True,protected_test_used=False,requested_five_steps_complete=False)


def test_matched_budget_refuses_different_learning_or_rounded_material_ratio():
    c=recipe();runner.validate_plan(c)
    changed=copy.deepcopy(c);changed["arms"]["large"]["teachers"]=2000000000
    with pytest.raises(AssertionError):runner.validate_plan(changed)
    changed=copy.deepcopy(c);changed["prepared_tokens"]["large"]-=1
    with pytest.raises(AssertionError):runner.validate_plan(changed)
    changed=copy.deepcopy(c);changed["source_ratio"]=dict(web=.8,story=.2)
    with pytest.raises(AssertionError):runner.validate_plan(changed)


def test_unseen_material_notes_require_all64_raw_binding_and_real_boolean_judgments():
    samples=[dict(text=f"original{i}") for i in range(64)]
    notes=dict(sample_sha256="raw",reviewer="Codex nonblind",independent_human_blind=False,
        notes=[[i,False,"原文の対象と文の終わりを全て確認しました。"] for i in range(64)])
    assert len(validate_notes(samples,notes,"raw"))==64
    for change in (lambda d:d["notes"].pop(),lambda d:d["notes"][0].__setitem__(1,None),
                   lambda d:d.__setitem__("sample_sha256","another_raw")):
        invalid=copy.deepcopy(notes);change(invalid)
        with pytest.raises(AssertionError):validate_notes(samples,invalid,"raw")


def test_preflight_refuses_specific_live_scientific_job_before_UI_actions(monkeypatch,tmp_path):
    from jmicro.experiment import write_json
    monkeypatch.setattr(runner,"RUN",tmp_path)
    monkeypatch.setattr(runner,"load_config",lambda:recipe())
    monkeypatch.setattr(runner,"alive",lambda _:True)
    write_json(tmp_path/"job.json",dict(pid=123,config_sha256="unused"))
    with pytest.raises(AssertionError,match="still live"):runner.preflight()


def test_model_notes_keep_raw_failures_and_cannot_count_length_limit_as_EOS():
    from review_larger_material_comparison import validate_notes as model_notes
    rows=[dict(id=str(i),stop_reason="stop_id") for i in range(80)]
    notes=dict(generation_sha256="raw",independent_human_blind=False,reviewer="Codex nonblind",
        notes=[[str(i),2,2,2,1,"提示した話題と対象を保持し、EOSで完結しています。"] for i in range(80)])
    assert len(model_notes(rows,notes,"raw"))==80
    changed=copy.deepcopy(rows);changed[0]["stop_reason"]="max_new_tokens"
    with pytest.raises(AssertionError):model_notes(changed,notes,"raw")
    changed=copy.deepcopy(notes);changed["notes"][0][1]=True
    with pytest.raises(AssertionError):model_notes(rows,changed,"raw")
    with pytest.raises(AssertionError):model_notes(rows,notes,"different_generation")
