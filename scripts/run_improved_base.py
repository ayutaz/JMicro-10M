"""One measured stable extension and equal decay evaluation; quality remains separate."""
import argparse
import gc
import json
import math
import os
from pathlib import Path
import shutil
import signal
import sys
import time
os.environ.setdefault("CUBLAS_WORKSPACE_CONFIG",":4096:8")
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jmicro.eos_pilot import TrainView
from jmicro.experiment import ROOT,read_json,sha256,now
from jmicro.shards import Shard
from jmicro.tokenizer import Tokenizer
from jmicro.training import atomic_json,gpu_lock,implementation_hashes
from amount_learning_trainer import CompactIndex,CurveTrainer
from extend_amount_learning_trainer import ExtendedCurveTrainer
from phase6_performance import alive,identity,finite_state
from review_eos_5b_finish import validate_rows
from review_matched_story_study import quality_gates
from run_eos_short_pilot import equal_state,rate
from run_amount_learning_comparison import CONFIG as ORIGINAL_CONFIG,load_config,latest_checkpoint,reconcile_metrics,detail
import run_complete_text_comparison as evaluation

SOURCES = ("scripts/run_improved_base.py","scripts/run_improved_base.ps1",
    "scripts/extend_amount_learning_trainer.py","scripts/amount_learning_trainer.py",
    "src/jmicro/learning_curve.py","scripts/run_amount_learning_comparison.py",
    "scripts/review_matched_story_study.py","scripts/run_complete_text_comparison.py")


def preflight(path,config=None):
    c = read_json(path) if config is None else config;previous_run = Path(c["source_run"])
    job = read_json(previous_run/"job.json")
    if job["status"] != "complete" or alive(job):
        raise ValueError("Previous scientific job must actually finish before extension selection")
    assert previous_run.resolve().is_relative_to((ROOT/"reports/phase6").resolve())
    assert c["implementation"] == implementation_hashes()
    assert c["source_sha256"] == {p:sha256(ROOT/p) for p in SOURCES}
    assert sha256(ORIGINAL_CONFIG) == c["original_config_sha256"]
    base = load_config()
    source_result = previous_run/"compare-result.json"
    assert sha256(source_result) == c["source_result_sha256"]
    result = read_json(source_result)
    for key in ("source_review","source_annotations"):
        assert sha256(Path(c[key]["path"])) == c[key]["sha256"]
    review = read_json(Path(c["source_review"]["path"]))
    assert review["status"] in ("stage4_learning_and_all400_content_evidence_complete","improved_base_stage_evidence_complete")
    assert review["result_sha256"] == c["source_result_sha256"] and not review["protected_test_used"]
    assert review["annotations_sha256"] == c["source_annotations"]["sha256"]
    annotations = read_json(Path(c["source_annotations"]["path"]))["arms"]
    parent_point,reference = c["parent_point"],c["quality_reference_point"]
    record = result["stable"][parent_point]
    assert record["checkpoint_sha256"] == c["parent"]["sha256"] and record["checkpoint"] == c["parent"]["path"]
    assert sha256(Path(c["parent"]["path"])) == c["parent"]["sha256"]
    state = torch.load(c["parent"]["path"],map_location="cpu",weights_only=False)
    assert finite_state(state) and state["pilot_binding"] == record["binding"]
    assert state["spec"]["curve_schedule"]["mode"] == "stable"
    consumed = state["sampler"]["source_teachers"]["short"]
    assert consumed == state["spec"]["curve_schedule"]["teachers"] == record["additional_supervised_tokens"]
    assert type(c["target_teachers"]) is int and consumed < c["target_teachers"] and c["target_teachers"] in (5000000000,10000000000)
    assert c["decay_teacher_tokens"] == base["decay_teacher_tokens"] == 20000000 and math.isfinite(c["GPU_budget_seconds"]) and c["GPU_budget_seconds"] > 0
    tok = Tokenizer(ROOT/base["tokenizer"])
    cases = {r["id"]:r for r in (json.loads(s) for s in (ROOT/"eval/base.jsonl").read_text().splitlines()) if r["split"] == "dev"}
    scores = {}
    for key in (reference,parent_point):
        ev = result["evaluations"][key];rows = ev["generation"]["outputs"];validate_rows(rows,tok)
        assert len(rows) == 80 and {r["id"] for r in rows} == set(cases)
        assert all(r["prefix"] == cases[r["id"]]["prefix"] for r in rows)
        assert not ev["protected_test_used"] and ev["evaluation_RNG_isolated"] and ev["greedy_rates"] == rate(rows)
        notes = annotations[key]["notes"];scores[key] = {n[0]:dict(grammar=n[1],relevance=n[2],coherence=n[3],completion=n[4]) for n in notes}
        assert len(notes) == len(scores[key]) == 80 and set(scores[key]) == set(cases)
        assert all(all(type(n[i]) is int and n[i] in (0,1,2) for i in (1,2,3)) and type(n[4]) is int and n[4] in (0,1) and len(n[5]) >= 12 for n in notes)
        assert all(not scores[key][r["id"]]["completion"] or r["stop_reason"] == "stop_id" and scores[key][r["id"]]["relevance"] >= 1 and scores[key][r["id"]]["coherence"] >= 1 for r in rows)
        assert ev["checkpoint_sha256"] == result["decay"][key]["checkpoint_sha256"]
    candidate = result["evaluations"][parent_point];s = scores[parent_point];rates = candidate["greedy_rates"]
    bodies = [result["evaluations"][key]["body"] for key in (reference,parent_point)]
    assert all(b["documents"] == len(b["rows"]) == 256 for b in bodies)
    assert [(r["doc_id"],r["body_tokens"],r["body_bytes"]) for r in bodies[0]["rows"]] == [(r["doc_id"],r["body_tokens"],r["body_bytes"]) for r in bodies[1]["rows"]]
    absolute = (sum(v["grammar"] == 2 for v in s.values()) >= 56 and sum(v["coherence"] == 2 for v in s.values()) >= 27
        and sum(v["completion"] for v in s.values()) >= 27 and rates["eos"] >= 37 and rates["repetition"] <= 18
        and all(rates[k] == 0 for k in ("unicode_failure","empty","role_leak")))
    comparison = quality_gates(result["evaluations"][reference],candidate,scores[reference],s,c["comparison_kind"])
    if not (comparison["passed"] or absolute):
        raise ValueError("No unchanged-quality improvement or absolute Base screen supports this research extension")
    assert c["comparison_kind"] in ("amount","content")
    arm = state["pilot_binding"]["arm"]
    assert arm in base["pools"] and state["pilot_binding"]["short_manifest_sha256"] == base["pools"][arm]["manifest_sha256"]
    output = (ROOT/c["output"]).resolve()
    assert output.is_relative_to(ROOT/"reports/phase6") and output != previous_run.resolve()
    return c,base,state,result,dict(relative=comparison,absolute_research_screen=absolute,Base_adopted=False)


def freeze(path,args):
    if path.exists():
        preflight(path);print("Existing frozen extension retained; no GPU started");return
    if any(value is None for value in (args.source_run,args.parent_point,args.reference_point,args.target_teachers)):
        raise ValueError("Freeze needs completed source run, parent/reference points and target teachers")
    source_run = (ROOT/args.source_run).resolve();job = read_json(source_run/"job.json")
    if job["status"] != "complete" or alive(job):
        raise ValueError("Previous scientific job must actually finish before extension selection")
    result = read_json(source_run/"compare-result.json");record = result["stable"][args.parent_point]
    consumed = record["additional_supervised_tokens"]
    measured_teachers = record.get("measured_stage_teachers",consumed)
    throughput = measured_teachers/record["training_step_seconds"]
    remaining = args.target_teachers-consumed
    assert remaining > 0 and math.isfinite(throughput) and throughput > 0
    review = source_run/"review.json";annotations = source_run/"annotations.json"
    c = dict(version=1,source_run=str(source_run),source_result_sha256=sha256(source_run/"compare-result.json"),
        source_review=dict(path=str(review),sha256=sha256(review)),source_annotations=dict(path=str(annotations),sha256=sha256(annotations)),
        parent_point=args.parent_point,quality_reference_point=args.reference_point,comparison_kind=args.comparison_kind,
        parent=dict(path=record["checkpoint"],sha256=record["checkpoint_sha256"]),target_teachers=args.target_teachers,
        decay_teacher_tokens=20000000,GPU_budget_seconds=math.ceil(remaining/throughput*1.3+1800),
        budget_estimate=dict(measured_teacher_tokens=measured_teachers,measured_step_seconds=record["training_step_seconds"],
            teacher_tokens_per_second=throughput,remaining_stable_teachers=remaining,
            rule="Stable remaining/observed step throughput*1.3 +1800s for verification/decay/evaluation/saving; estimate, not measured end-to-end completion"),
        output="reports/phase6/"+path.stem,implementation=implementation_hashes(),original_config_sha256=sha256(ORIGINAL_CONFIG),
        source_sha256={p:sha256(ROOT/p) for p in SOURCES},protected_test_used=False,quality_criteria_unchanged=True,
        scope="One same-material stable extension, equal20M decay, all80 content required afterwards; no automatic next-stage training",
        Base_adopted=False,requested_five_steps_complete=False,created_at=now())
    preflight(path,c)  # Rejected recipes never become frozen config artifacts.
    path.parent.mkdir(parents=True,exist_ok=True);atomic_json(path,c)
    print(json.dumps(dict(config=str(path),GPU_budget_seconds=c["GPU_budget_seconds"],Base_adopted=False)));print("Frozen eligible research continuation; no GPU started")


def run(path):
    c,base,parent,source,eligibility = preflight(path)
    directory = ROOT/c["output"];directory.mkdir(parents=True,exist_ok=True)
    config_sha = sha256(path);job_path = directory/"job.json"
    previous = read_json(job_path) if job_path.exists() else {}
    if previous:
        assert previous["config_sha256"] == config_sha and not alive(previous)
        if previous["status"] == "complete": print("Completed extension retained");return
    prior = previous.get("GPU_elapsed_seconds",0.);started = None;stop = [False]
    signal.signal(signal.SIGTERM,lambda *_:stop.__setitem__(0,True));signal.signal(signal.SIGINT,lambda *_:stop.__setitem__(0,True))
    job = dict(status="starting",**identity(),config_sha256=config_sha,started_at=previous.get("started_at",now()),
        GPU_elapsed_seconds=prior,restart_command=f"scripts/run_improved_base.ps1 -Config {path.relative_to(ROOT).as_posix()} -Worker",
        Base_adopted=False,requested_five_steps_complete=False)
    def check():
        if stop[0]: raise InterruptedError("Stop requested; only completed updates are saved")
        if started is not None and prior+time.monotonic()-started > c["GPU_budget_seconds"]: raise TimeoutError("Measured cumulative extension GPU budget exhausted")
    def heartbeat(stage,**values):
        check();job.update(stage=stage,heartbeat_at=now(),**values)
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path,job)
    def save(trainer,folder):
        target = folder/f"checkpoint-{trainer.update:08d}.pt";trainer.save(target);return target
    def train(trainer,folder,total,label):
        folder.mkdir(parents=True,exist_ok=True);latest = latest_checkpoint(folder)
        if latest is not None: trainer.load(latest)
        log = folder/"metrics.jsonl";seconds = reconcile_metrics(log,trainer.update)
        with log.open("a",buffering=1) as stream:
            while trainer.sampler.source_teachers["short"] < total:
                try: check()
                except (InterruptedError,TimeoutError): save(trainer,folder);raise
                row = trainer.step()
                assert math.isfinite(row["loss"]) and math.isfinite(row["gradient_norm"])
                seconds += row["seconds"];stream.write(json.dumps(row,allow_nan=False)+"\n")
                if trainer.update%100 == 0: heartbeat(label,teachers=trainer.sampler.source_teachers["short"],teacher_budget=total,loss=row["loss"])
                if trainer.update%250 == 0: save(trainer,folder)
        return detail(trainer,save(trainer,folder),trainer.pilot_binding,seconds)
    def gate(build,name):
        gate_path = directory/"resume-gate"/name/"result.json"
        if gate_path.exists():
            kept = read_json(gate_path);assert kept["passed"] and kept["config_sha256"] == config_sha;return kept
        states,history = [],[];teachers = inputs = 0
        for branch in ("continuous","resumed"):
            trainer = build();initial_teacher = trainer.supervised_tokens;initial_input = trainer.tokens;rows = []
            for index in range(4):
                check();rows.append(trainer.step())
                if branch == "resumed" and index == 1:
                    split = directory/"resume-gate"/name/"split.pt";trainer.save(split)
                    del trainer;gc.collect();torch.cuda.empty_cache();trainer = build();trainer.load(split)
            teachers += trainer.supervised_tokens-initial_teacher;inputs += trainer.tokens-initial_input
            end = directory/"resume-gate"/name/(branch+".pt");trainer.save(end)
            states.append(torch.load(end,map_location="cpu",weights_only=False));history.append(rows)
            del trainer;gc.collect();torch.cuda.empty_cache()
        keys = ("model","optimizer","scheduler","rng","sampler","lineage","tokens","supervised_tokens","body_bytes","token_digest","update")
        checks = {key:equal_state(states[0][key],states[1][key]) for key in keys}
        checks["history"] = all([r[k] for r in history[0]] == [r[k] for r in history[1]] for k in ("loss","gradient_norm","lr","token_digest","source_teachers"))
        checks["finite"] = all(finite_state(s) for s in states)
        assert all(checks.values()),checks
        record = dict(passed=True,checks=checks,config_sha256=config_sha,verification_teacher_tokens=teachers,verification_input_tokens=inputs,GPU_optimizer_updates=8)
        atomic_json(gate_path,record);return record
    try:
        heartbeat("setup");torch.set_num_threads(2);torch.use_deterministic_algorithms(True)
        for file in (*SOURCES,str(path.relative_to(ROOT))):
            target = directory/"source"/file;target.parent.mkdir(parents=True,exist_ok=True)
            if target.exists(): assert target.read_bytes() == (ROOT/file).read_bytes()
            else: shutil.copyfile(ROOT/file,target)
        atomic_json(directory/"selection.json",eligibility)
        web = TrainView(base["web_shards"],base["web_manifest_sha256"])
        arm = parent["pilot_binding"]["arm"];pool = TrainView(base["pools"][arm]["pool"],base["pools"][arm]["manifest_sha256"]);pool.index = CompactIndex(pool)
        dev = Shard(Path(base["dev_shards"]),"dev");tok = Tokenizer(ROOT/base["tokenizer"])
        zero = torch.load(base["parent"]["path"],map_location="cpu",weights_only=False)
        binding = dict(parent["pilot_binding"],config_sha256=config_sha,
            curve_boundaries=[*parent["spec"]["curve_schedule"]["boundaries"],c["target_teachers"]],
            stable_extension=dict(c["parent"],source_sha256=sha256(ROOT/"scripts/extend_amount_learning_trainer.py")))
        def build():
            trainer = ExtendedCurveTrainer(zero,web,pool,"shuffle",dict(web=0,short=c["target_teachers"]),binding)
            trainer.load_extension(c["parent"]["path"]);return trainer
        with gpu_lock("cuda"):
            started = time.monotonic();stable_gate = gate(build,"stable-extension")
            trainer = build();stable_record = train(trainer,directory/"stable",c["target_teachers"],"stable")
            stable_record["measured_stage_teachers"] = c["target_teachers"]-parent["sampler"]["source_teachers"]["short"]
            del trainer;gc.collect();torch.cuda.empty_cache()
            stable = torch.load(stable_record["checkpoint"],map_location="cpu",weights_only=False)
            branch_binding = dict(binding,arm=arm+"-"+str(c["target_teachers"]),curve_mode="decay",curve_boundaries=[c["decay_teacher_tokens"]],
                warmup_updates=0,optimizer_policy="inherit",initialization="stable-fork",parent=dict(path=stable_record["checkpoint"],sha256=stable_record["checkpoint_sha256"],
                update=stable["update"],tokens_seen=stable["tokens"],supervised_tokens=stable["supervised_tokens"]))
            def build_decay(): return CurveTrainer(stable,web,pool,"shuffle",dict(web=0,short=c["decay_teacher_tokens"]),branch_binding)
            decay_gate = gate(build_decay,"decay")
            branch = build_decay();decay_record = train(branch,directory/"decay",c["decay_teacher_tokens"],"decay")
            del branch;gc.collect();torch.cuda.empty_cache()
            evaluation.RUN = directory/"evaluation"
            ev = evaluation.evaluate(branch_binding["arm"],decay_record,dev,tok,base,branch_binding,heartbeat,check,started+c["GPU_budget_seconds"]-prior)
            result = dict(status="complete_pending_all80_content_judgments",config_sha256=config_sha,
                stable={c["parent_point"]:source["stable"][c["parent_point"]],branch_binding["arm"]:stable_record},
                decay={c["parent_point"]:source["decay"][c["parent_point"]],branch_binding["arm"]:decay_record},
                evaluations={c["parent_point"]:source["evaluations"][c["parent_point"]],branch_binding["arm"]:ev},
                scientific_stable_teachers=c["target_teachers"]-parent["sampler"]["source_teachers"]["short"],scientific_decay_teachers=c["decay_teacher_tokens"],
                additional_valid_input_tokens=stable_record["tokens"]-parent["tokens"]+decay_record["additional_input_tokens"],
                additional_physical_input_tokens=stable_record["physical_input_tokens"]-sum(parent["sampler"]["source_physical_tokens"].values())+decay_record["physical_input_tokens"],
                verification_teacher_tokens=stable_gate["verification_teacher_tokens"]+decay_gate["verification_teacher_tokens"],
                resume_gates=[stable_gate,decay_gate],GPU_seconds=prior+time.monotonic()-started,
                Base_adopted=False,protected_test_used=False,requested_five_steps_complete=False,completed_at=now())
            atomic_json(directory/"compare-result.json",result);heartbeat("complete");job.update(status="complete",completed_at=now())
    except BaseException as error: job.update(status="failed",error=repr(error));raise
    finally:
        if started is not None: job["GPU_elapsed_seconds"] = prior+time.monotonic()-started
        atomic_json(job_path,job)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7)
    parser = argparse.ArgumentParser();parser.add_argument("--config",type=Path,required=True)
    mode = parser.add_mutually_exclusive_group();mode.add_argument("--inspect",action="store_true");mode.add_argument("--freeze",action="store_true")
    parser.add_argument("--source-run",type=Path);parser.add_argument("--parent-point");parser.add_argument("--reference-point")
    parser.add_argument("--target-teachers",type=int,choices=(5000000000,10000000000));parser.add_argument("--comparison-kind",choices=("amount","content"),default="amount")
    args = parser.parse_args()
    config = args.config.resolve()
    if not config.is_relative_to(ROOT/"configs/phase6"): raise ValueError("Use a repository frozen Phase6 recipe")
    if args.freeze: freeze(config,args)
    elif args.inspect:
        _,_,_,_,eligibility = preflight(config);print(json.dumps(eligibility));print("Extension preflight passed; no GPU started")
    else: run(config)
