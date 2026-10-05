"""Validate measured masked-shape batch evidence, separate from model quality."""
import math
from pathlib import Path
from jmicro.experiment import ROOT,read_json,sha256
from phase6_performance import alive


def require_batch_evidence(config, kind, data_binding, trainer_path):
    ref = config["batch_evidence"];path = Path(ref["path"])
    assert sha256(path) == ref["sha256"]
    batch = read_json(path);job = read_json(path.parent/"probe-job.json")
    if job["status"] != "complete" or alive(job):
        raise ValueError("Masked batch probe must actually finish before training")
    assert batch["status"] == "complete_masked_CUDA_batch_measurement"
    assert batch["config_sha256"] == job["config_sha256"]
    assert batch["kind"] == kind and batch["actual_CUDA_BF16"] and batch["finite_forward_backward"]
    assert batch["parent_checkpoint_sha256"] == config["parent"]["sha256"]
    assert batch["data_binding"] == data_binding and batch["trainer_sha256"] == sha256(ROOT/trainer_path)
    assert batch["implementation"] == config["implementation"]
    spec = config["spec"]
    assert all(batch["training_shape"][key] == spec[key] for key in ("context","dtype","backend","compile","accumulation","sampler","training_fast_path"))
    assert batch["selected_batch"] == spec["batch"]
    assert batch["selection_metric"] == "median_teacher_tokens_per_second"
    successful = [r for r in batch["candidates"] if r["status"] == "complete" and r["finite_forward_backward"]]
    assert successful and all(math.isfinite(r["median_teacher_tokens_per_second"]) and r["median_teacher_tokens_per_second"] > 0 for r in successful)
    best = max(successful,key=lambda r:r["median_teacher_tokens_per_second"])
    assert best["batch"] == spec["batch"] and batch["selected_measurement"] == best
    assert batch["quality_evaluated"] is False and batch["probe_weights_discarded"] is True
    return batch
