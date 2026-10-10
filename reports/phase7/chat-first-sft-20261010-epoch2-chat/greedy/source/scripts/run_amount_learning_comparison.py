"""Stage4: nested material quantity and uninterrupted stable learning curves."""
import argparse
import copy
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG", ":4096:8")
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import torch
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json, gpu_lock, seed_all, implementation_hashes
from phase6_performance import identity, alive, finite_state
from amount_learning_trainer import CompactIndex, CurveTrainer
import run_curriculum_strategy as strategy
import run_complete_text_comparison as evaluation

RUN = ROOT / "reports/phase6/amount-learning-20261006"
CONFIG = ROOT / "configs/phase6/amount_learning_comparison.json"
DATA = Path("/home/aihub_ubuntu/jmicro-data/phase6/nested-material-20261006-v2")
SOURCE_FILES = (
    "scripts/run_amount_learning_comparison.py", "scripts/run_amount_learning_comparison.ps1",
    "scripts/amount_learning_trainer.py", "src/jmicro/learning_curve.py",
    "scripts/resume_curriculum_strategy.py", "scripts/run_curriculum_strategy.py",
    "scripts/run_complete_text_comparison.py", "src/jmicro/curriculum_strategy.py",
    "src/jmicro/natural_learning.py", "src/jmicro/packing_study.py", "src/jmicro/eos_pilot.py",
    "src/jmicro/low_lr_pilot.py", "src/jmicro/tokenizer.py")


def freeze():
    if CONFIG.exists():
        load_config(); print("Frozen amount/learning recipe retained"); return
    review = read_json(ROOT / "reports/phase6/nested_material_content_review.json")
    assert review["passed"] and review["documents"] == 64 and review["weak_documents"] <= 10
    ready = read_json(DATA / "ready.json")
    assert review["ready_sha256"] == sha256(DATA / "ready.json")
    assert review["sample_sha256"] == sha256(DATA / "sample64.json")
    assert ready["pools"] == review["pools"] and ready["nested_ratio_exact"] == 5
    assert ready["editorial_unit_histograms_exact_ratio"]
    base = read_json(ROOT / "configs/phase6/material_comparison.json")
    parent = torch.load(base["parent"]["path"], map_location="cpu", weights_only=False)
    assert sha256(Path(base["parent"]["path"])) == base["parent"]["sha256"]
    assert parent["update"] == parent["tokens"] == parent["supervised_tokens"] == 0 and not parent["optimizer"]["state"]
    import xml.etree.ElementTree as ET
    tests = {}
    for name in ("learning_curve_tests.xml", "amount_learning_trainer_tests.xml"):
        p = ROOT / "reports/phase6" / name
        suites = list(ET.parse(p).getroot().iter("testsuite"))
        assert suites and all(int(s.attrib[k]) == 0 for s in suites for k in ("errors", "failures", "skipped"))
        tests[str(p.relative_to(ROOT))] = sha256(p)
    c = {k: copy.deepcopy(base[k]) for k in ("parent", "web_shards", "web_manifest_sha256",
        "dev_shards", "dev_manifest_sha256", "tokenizer", "tokenizer_sha256", "suite_sha256", "evaluation", "reference")}
    c.update(version=1, scope="Five items stage4 full amount/learning experiment; stage5 Base/Chat/quantization remains required",
        pools={name: {k: ready["pools"][name][k] for k in ("pool", "manifest_sha256")} for name in ("small", "large")},
        arms=dict(large=dict(teachers=2000000000, boundaries=[100000000,500000000,1000000000,2000000000], evaluate=[100000000,500000000,1000000000,2000000000]),
                  small=dict(teachers=1000000000, boundaries=[100000000,500000000,1000000000], evaluate=[1000000000])),
        peak_lr=.002, warmup_updates=200, decay_teacher_tokens=20000000,
        scientific_teacher_budget=3100000000, stable_teacher_budget=3000000000, decay_teacher_budget=100000000,
        GPU_budget_seconds=7200, checkpoints_every_updates=250,
        prepared_tokens=dict(small=100000157, large=500000785),
        preparation_sha256=sha256(DATA / "ready.json"),
        content_review_sha256=sha256(ROOT / "reports/phase6/nested_material_content_review.json"),
        tests_sha256=tests, implementation=implementation_hashes(), source_sha256={p: sha256(ROOT / p) for p in SOURCE_FILES},
        interpretation="Same original13-layer fresh weights/RNG, same source/length/editorial-unit/EOS distributions; quantity100Mvs500M at stable1B plus identical20M decay. Same500M pool100M/500M/1B/2B stable milestones plus identical20M decay. Branches never overwrite/reheat the stable path",
        unique_exposure_policy="Save actual epoch/block cursors and repeated teachers separately from prepared quantity; partial masked checkpoint updates retain consumed input and skipped teacher suffix. Exact unique token-union not independently measured",
        source_history="Pinned old Web and translated synthetic stories; local exact/family split, global near/site/author overlap not independently audited",
        quality_criteria_unchanged=True,
        protected_test_used=False, requested_five_steps_complete=False, created_at=now())
    write_json(CONFIG, c)
    print("Frozen3B stable+100M equal decay teachers; no GPU started", flush=True)


def load_config():
    c = read_json(CONFIG)
    assert c["implementation"] == implementation_hashes()
    assert c["source_sha256"] == {p: sha256(ROOT / p) for p in SOURCE_FILES}
    assert c["tests_sha256"] == {p: sha256(ROOT / p) for p in c["tests_sha256"]}
    assert c["preparation_sha256"] == sha256(DATA / "ready.json")
    assert c["content_review_sha256"] == sha256(ROOT / "reports/phase6/nested_material_content_review.json")
    for p, digest in ((ROOT / c["tokenizer"], c["tokenizer_sha256"]),
                      (Path(c["parent"]["path"]), c["parent"]["sha256"]),
                      (Path(c["web_shards"]) / "manifest.json", c["web_manifest_sha256"]),
                      (Path(c["dev_shards"]) / "manifest.json", c["dev_manifest_sha256"]),
                      (ROOT / "eval/base.jsonl", c["suite_sha256"])):
        assert sha256(p) == digest
    for p in c["pools"].values():
        assert sha256(Path(p["pool"]) / "manifest.json") == p["manifest_sha256"]
    ev = c["evaluation"]
    for p, digest in ((ROOT / ev["config"],ev["config_sha256"]),
                      (ROOT / ev["semantic_suite"],ev["semantic_sha256"]),
                      (Path("/home/aihub_ubuntu/jmicro-data/evaluation-v2/manifest.json"),ev["data_manifest_sha256"])):
        assert sha256(p) == digest
    for ref in c["reference"].values():
        assert sha256(Path(ref["path"])) == ref["sha256"]
    assert c["scientific_teacher_budget"] == c["stable_teacher_budget"] + c["decay_teacher_budget"] == 3100000000
    return c


def reconcile_metrics(log, update):
    """Retain only completed checkpoint updates, including every decay branch."""
    rows = [json.loads(s) for s in log.read_text().splitlines()] if log.exists() else []
    if rows and rows[-1]["update"] > update:
        shutil.copyfile(log, log.with_name(f"metrics-before-resume-{time.time_ns()}.jsonl"))
        rows = [r for r in rows if r["update"] <= update]
        log.write_text("".join(json.dumps(r,allow_nan=False)+"\n" for r in rows))
    assert all(a["update"]+1 == b["update"] for a,b in zip(rows,rows[1:]))
    return sum(r["seconds"] for r in rows)


def latest_checkpoint(folder):
    if not (folder / "latest.json").exists(): return None
    last = read_json(folder / "latest.json")
    path = Path(last["path"])
    assert sha256(path) == last["sha256"]
    return path


def detail(trainer, path, binding, seconds):
    return dict(status="complete", checkpoint=str(path), checkpoint_sha256=sha256(path), binding=binding,
        update=trainer.update, tokens=trainer.tokens, supervised_tokens=trainer.supervised_tokens,
        additional_supervised_tokens=trainer.supervised_tokens-trainer.lineage["parent_supervised_tokens"],
        additional_input_tokens=trainer.tokens-trainer.lineage["parent_tokens"],
        physical_input_tokens=sum(trainer.sampler.source_physical_tokens.values()),
        source_eos_teachers=trainer.sampler.source_eos.copy(), sampler=trainer.sampler.state_dict(),
        genre_teachers=trainer.sampler.genre_teachers.copy(), genre_eos=trainer.sampler.genre_eos.copy(),
        training_step_seconds=seconds, timing_policy="Sum completed metric update seconds; compile within step included, constructor/saving/evaluation excluded; total occupancy separately recorded",
        peak_allocated_bytes=torch.cuda.max_memory_allocated())


def run():
    c = load_config(); RUN.mkdir(parents=True, exist_ok=True)
    job_path = RUN / "job.json"; previous = read_json(job_path) if job_path.exists() else {}
    if previous:
        assert previous["config_sha256"] == sha256(CONFIG) and not alive(previous)
        if previous["status"] == "complete":
            print("Completed research retained"); return
    prior = previous.get("gpu_elapsed_seconds", 0.); started = [None]; stop = [False]
    job = dict(status="running", **identity(), config_sha256=sha256(CONFIG), started_at=previous.get("started_at", now()),
        gpu_elapsed_seconds=prior, restart_command="scripts/run_amount_learning_comparison.ps1 -Worker", requested_scope_complete=False)
    signal.signal(signal.SIGTERM, lambda *_: stop.__setitem__(0, True))
    signal.signal(signal.SIGINT, lambda *_: stop.__setitem__(0, True))
    def check():
        if stop[0]: raise InterruptedError("Stop requested; completed-update state preserved")
        if started[0] is not None and prior+time.monotonic()-started[0] > c["GPU_budget_seconds"]:
            raise TimeoutError("Cumulative7200s amount/learning GPU budget exhausted")
    def heartbeat(stage, **values):
        check(); job.update(stage=stage, heartbeat_at=now(), **values)
        if started[0] is not None: job["gpu_elapsed_seconds"] = prior+time.monotonic()-started[0]
        atomic_json(job_path, job)
    def save(trainer, folder):
        path = folder / f"checkpoint-{trainer.update:08d}.pt"; trainer.save(path); return path
    results = read_json(RUN / "progress-result.json") if (RUN / "progress-result.json").exists() else dict(stable={}, decay={}, evaluations={})
    try:
        heartbeat("setup"); torch.set_num_threads(2); seed_all(42); torch.use_deterministic_algorithms(True)
        for p in (*SOURCE_FILES, str(CONFIG.relative_to(ROOT))):
            target = RUN / "source" / p; target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists(): assert target.read_bytes() == (ROOT / p).read_bytes()
            else: shutil.copyfile(ROOT / p, target)
        web = TrainView(c["web_shards"], c["web_manifest_sha256"])
        dev = Shard(Path(c["dev_shards"]), "dev"); tok = Tokenizer(ROOT / c["tokenizer"])
        parent = torch.load(c["parent"]["path"], map_location="cpu", weights_only=False)
        assert finite_state(parent)
        pools = {}
        for arm, ref in c["pools"].items():
            heartbeat("index-"+arm)
            view = TrainView(ref["pool"], ref["manifest_sha256"], check_stream=True)
            view.index = CompactIndex(view); pools[arm] = view
        strategy.RUN = RUN; strategy.StrategyTrainer = CurveTrainer
        evaluation.RUN = RUN / "evaluation"
        with gpu_lock("cuda"):
            started[0] = time.monotonic()
            for arm, plan in c["arms"].items():
                pool = pools[arm]; folder = RUN / arm / "stable"; folder.mkdir(parents=True, exist_ok=True)
                binding = dict(config_sha256=sha256(CONFIG), parent=c["parent"], arm=arm,
                    peak_lr=c["peak_lr"], warmup_updates=c["warmup_updates"], optimizer_policy="fresh", initialization="new-random",
                    curve_mode="stable", curve_boundaries=plan["boundaries"], short_manifest_sha256=c["pools"][arm]["manifest_sha256"])
                strategy.resume_gate(parent, web, pool, binding, check, heartbeat)
                trainer = CurveTrainer(parent, web, pool, "shuffle", dict(web=0, short=plan["teachers"]), binding)
                last = latest_checkpoint(folder)
                if last is not None: trainer.load(last)
                log = folder / "metrics.jsonl"
                seconds = reconcile_metrics(log,trainer.update)
                point = trainer.sampler.source_teachers["short"]
                if point in plan["boundaries"] and arm+"-"+str(point) not in results["stable"]:
                    assert last is not None
                    results["stable"][arm+"-"+str(point)] = detail(trainer,last,binding,seconds)
                    write_json(RUN / "progress-result.json",results)
                def evaluate_point(point, stable_path):
                    nonlocal trainer
                    key = arm+"-"+str(point)
                    if key in results["evaluations"]: return
                    # An old unevaluated milestone must not rewind a newer
                    # stable checkpoint on restart. Release the compiled model
                    # before constructing any fork/evaluation on the GPU.
                    restore_path = latest_checkpoint(folder)
                    assert restore_path is not None
                    del trainer; trainer = None; gc.collect(); torch.cuda.empty_cache()
                    branch_folder = RUN / key / "decay"; branch_folder.mkdir(parents=True, exist_ok=True)
                    assert sha256(stable_path) == results["stable"][key]["checkpoint_sha256"]
                    state = torch.load(stable_path, map_location="cpu", weights_only=False)
                    assert state["sampler"]["source_teachers"]["short"] == point and state["pilot_binding"] == binding
                    assert finite_state(state)
                    branch_binding = dict(binding, arm=key, curve_mode="decay", curve_boundaries=[c["decay_teacher_tokens"]], warmup_updates=0,
                        optimizer_policy="inherit", initialization="stable-fork", parent=dict(path=str(stable_path), sha256=sha256(stable_path),
                        update=state["update"], tokens_seen=state["tokens"], supervised_tokens=state["supervised_tokens"]))
                    if not (RUN / "resume-gate" / "equal-decay" / "result.json").exists():
                        strategy.resume_gate(state, web, pool, dict(branch_binding, arm="equal-decay"), check, heartbeat)
                    branch = CurveTrainer(state, web, pool, "shuffle", dict(web=0, short=c["decay_teacher_tokens"]), branch_binding)
                    last_branch = latest_checkpoint(branch_folder)
                    if last_branch is not None: branch.load(last_branch)
                    branch_log = branch_folder / "metrics.jsonl"
                    branch_seconds = reconcile_metrics(branch_log,branch.update)
                    with (branch_folder / "metrics.jsonl").open("a", buffering=1) as stream:
                        while branch.sampler.source_teachers["short"] < c["decay_teacher_tokens"]:
                            try: check()
                            except (InterruptedError,TimeoutError): save(branch, branch_folder); raise
                            row = branch.step()  # Never save partially failed optimizer/sampler state.
                            assert math.isfinite(row["loss"]) and math.isfinite(row["gradient_norm"])
                            branch_seconds += row["seconds"]
                            stream.write(json.dumps(row, allow_nan=False)+"\n")
                            if branch.sampler.position % 100 == 0: heartbeat(key+"-decay", teachers=branch.sampler.source_teachers["short"], teacher_budget=c["decay_teacher_tokens"], loss=row["loss"])
                            if branch.sampler.position % 250 == 0: save(branch, branch_folder)
                    path = save(branch, branch_folder); record = detail(branch, path, branch_binding, branch_seconds)
                    results["decay"][key] = record
                    write_json(RUN / "progress-result.json", results)
                    del branch, state; gc.collect(); torch.cuda.empty_cache()
                    ev = evaluation.evaluate(key, record, dev, tok, c, branch_binding, heartbeat, check, started[0]+c["GPU_budget_seconds"]-prior)
                    results["evaluations"][key] = ev
                    write_json(RUN / "progress-result.json", results)
                    trainer = CurveTrainer(parent,web,pool,"shuffle",dict(web=0,short=plan["teachers"]),binding)
                    trainer.load(restore_path)  # Restore the actual latest stable path, never the decay or an older pending point.
                # Recover points whose stable checkpoint was saved immediately
                # before interruption. The stable metadata names that exact path.
                for point in plan["evaluate"]:
                    key = arm+"-"+str(point)
                    if key in results["stable"] and key not in results["evaluations"]:
                        evaluate_point(point, Path(results["stable"][key]["checkpoint"]))
                with log.open("a", buffering=1) as stream:
                    while trainer.sampler.source_teachers["short"] < plan["teachers"]:
                        try: check()
                        except (InterruptedError,TimeoutError): save(trainer, folder); raise
                        row = trainer.step()
                        assert math.isfinite(row["loss"]) and math.isfinite(row["gradient_norm"])
                        seconds += row["seconds"]
                        stream.write(json.dumps(row, allow_nan=False)+"\n")
                        if trainer.update % 100 == 0:
                            heartbeat(arm+"-stable", teachers=trainer.sampler.source_teachers["short"], teacher_budget=plan["teachers"], updates_completed=trainer.update, loss=row["loss"])
                            print(json.dumps(dict(arm=arm, teachers=trainer.sampler.source_teachers["short"], loss=row["loss"])), flush=True)
                        point = trainer.sampler.source_teachers["short"]
                        if point in plan["boundaries"]:
                            path = save(trainer, folder); key = arm+"-"+str(point)
                            results["stable"][key] = detail(trainer, path, binding, seconds)
                            write_json(RUN / "progress-result.json", results)
                            if point in plan["evaluate"]: evaluate_point(point, path)
                        elif trainer.update % 250 == 0: save(trainer, folder)
                del trainer; gc.collect(); torch.cuda.empty_cache()
            gates = [read_json(p) for p in (RUN / "resume-gate").glob("*/result.json")]
            result = dict(results, status="complete_pending_all400_content_reviews", config_sha256=sha256(CONFIG),
                scientific_stable_teachers=sum(results["stable"][arm+"-"+str(p["teachers"])]["additional_supervised_tokens"] for arm,p in c["arms"].items()),
                scientific_decay_teachers=sum(r["additional_supervised_tokens"] for r in results["decay"].values()),
                verification_teacher_tokens=sum(r["verification_teacher_tokens"] for r in gates),
                gpu_seconds=prior+time.monotonic()-started[0], requested_five_steps_complete=False, protected_test_used=False, completed_at=now())
            assert len(result["evaluations"]) == len(result["decay"]) == 5 and result["scientific_decay_teachers"] == 100000000
            assert result["scientific_stable_teachers"] == c["stable_teacher_budget"]
            assert result["scientific_stable_teachers"]+result["scientific_decay_teachers"] == c["scientific_teacher_budget"]
            assert len(gates) == 3 and all(g["passed"] for g in gates)
            write_json(RUN / "compare-result.json", result); heartbeat("complete"); job.update(status="complete", completed_at=now())
    except BaseException as error:
        job.update(status="failed", error=repr(error)); raise
    finally:
        if started[0] is not None: job["gpu_elapsed_seconds"] = prior+time.monotonic()-started[0]
        atomic_json(job_path, job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    parser = argparse.ArgumentParser(); parser.add_argument("--freeze", action="store_true"); args = parser.parse_args()
    freeze() if args.freeze else run()
