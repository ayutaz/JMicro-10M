"""Selection/rejection protocol fixtures, not CUDA or model-quality evidence."""
import sys
import pytest
from jmicro.experiment import ROOT,write_json,sha256

sys.path.insert(0,str(ROOT/"scripts"))
from probe_chat_batch import selection,preflight,SOURCES
from chat_batch_evidence import require_batch_evidence


def test_select_teacher_throughput_not_largest_physical_batch_or_oom():
    candidates = [dict(status="complete",batch=16,finite_forward_backward=True,median_teacher_tokens_per_second=100),
        dict(status="complete",batch=32,finite_forward_backward=True,median_teacher_tokens_per_second=200),
        dict(status="complete",batch=64,finite_forward_backward=True,median_teacher_tokens_per_second=150),
        dict(status="oom",batch=128,finite_forward_backward=False)]
    assert selection(candidates)["batch"] == 32
    with pytest.raises(ValueError,match="No finite"): selection([candidates[-1]])


def test_completed_record_with_live_probe_handle_cannot_start_training(tmp_path):
    from phase6_performance import identity
    report = tmp_path/"batch-report.json";write_json(report,dict(not_actual_GPU_measurement=True))
    write_json(tmp_path/"probe-job.json",dict(status="complete",**identity()))
    c = dict(batch_evidence=dict(path=str(report),sha256=sha256(report)))
    with pytest.raises(ValueError,match="actually finish"):
        require_batch_evidence(c,"sft","fixture-binding","src/jmicro/chat_training.py")


def test_probe_refuses_unadopted_base_without_creating_cuda_context(tmp_path):
    from jmicro.training import implementation_hashes
    from run_chat_sft import SOURCES as TRAIN_SOURCES
    rejected = tmp_path/"rejected.json";write_json(rejected,dict(Base_adopted=False))
    ref = dict(path=str(rejected),sha256=sha256(rejected))
    c = dict(probe_kind="sft",probe_source_sha256={p:sha256(ROOT/p) for p in SOURCES},
        implementation=implementation_hashes(),source_sha256={p:sha256(ROOT/p) for p in TRAIN_SOURCES},
        **{k:ref for k in ("parent","Base_acceptance","Base_evaluation","Base_annotations","tokenizer")})
    config = tmp_path/"config.json";write_json(config,c)
    with pytest.raises(ValueError,match="quality-adopted Base"):preflight(config)
