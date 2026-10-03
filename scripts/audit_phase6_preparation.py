"""Final independent requirement audit for the user-authorized Phase 6 steps 1-2."""
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform
import shutil
import sqlite3
import subprocess
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import torch
from jsonschema import validate
from jmicro.experiment import ROOT,now,read_json,sha256,write_json
from jmicro.phase5 import equal_state
from jmicro.training import implementation_hashes,learning_rate_factor


def alive(record):
    path=Path(f'/proc/{record["pid"]}/stat')
    try:
        return (Path("/proc/sys/kernel/random/boot_id").read_text().strip()==record["boot_id"]
                and path.read_text().split()[21]==str(record["start_ticks"]))
    except FileNotFoundError:
        return False


def audit(args):
    checks={}
    c=read_json(ROOT/"configs/phase6/preparation.json")
    validate(c,read_json(ROOT/"schemas/configs/phase6/preparation.schema.json"))
    checks["frozen_preparation_scope_and_500m_goal"]=c["scope"]=="expanded_corpus_and_wsd_preparation_only" and c["minimum_train_stream_tokens"]==500000000
    data=read_json(args.data/"manifest.json")
    corpus_audit=read_json(args.data/"corpus_audit.json")
    checks["full_real_corpus_audit_passed"]=corpus_audit["status"]=="passed" and all(corpus_audit["all_checks"].values())
    checks["corpus_audit_bound_to_manifest"]=corpus_audit["manifest_sha256"]==sha256(args.data/"manifest.json")
    checks["unique_train_stream_at_least_500m"]=corpus_audit["stream_tokens"]["train"]>=500000000
    checks["dev_test_separate_and_present"]=all(corpus_audit["split_documents"][s]>0 for s in ("dev","test"))
    checks["all_retained_documents_roundtripped"]=corpus_audit["full_round_trip_documents"]==sum(corpus_audit["split_documents"].values())
    checks["raw_all_records_reconstructed"]=corpus_audit["raw_records_reconstructed"]==data["counts"]["raw_records"]
    checks["source_mixture_and_repetition_recorded"]=data["mixture"]==c["mixture"] and all(data["train_exposure"][str(n)]==n/corpus_audit["stream_tokens"]["train"] for n in (500000000,1000000000,10000000000))
    checks["near_dedup_detection_limit_disclosed"]="probabilistic" in data["near_scope"]
    raw=args.data.parent/"raw"
    source=read_json(raw/"sources.json")
    receipt=read_json(raw/"acquisition.json")
    checks["pinned_revision_and_source_conditions"]=source["source"]==c and source["source"]["revision"]=="180ca004c6a89b590daaad86cb062a07a5353c69" and sha256(raw/"README.upstream.md")==source["evidence_sha256"]
    checks["bounded_acquisition"]=1<=len(receipt["files"])<=c["maximum_files"] and sum(r["bytes"] for r in receipt["files"])<=c["maximum_raw_bytes"]
    checks["actual_raw_checksums_match_upstream"]=all(r["sha256"]==r["actual_sha256"]==sha256(raw/Path(r["path"]).name) for r in receipt["files"])
    checks["public_tokenizer_unchanged"]=sha256(ROOT/c["tokenizer"])==c["tokenizer_sha256"]
    review=read_json(args.windows_root/"reports/phase6/quality_review.json")
    db=sqlite3.connect(f'file:{args.data/"records.sqlite"}?mode=ro',uri=True)
    wanted=[sample["doc_id"] for sample in review["samples"]]
    query="SELECT payload,text,split FROM records WHERE json_extract(payload,'$.doc_id') IN ("+",".join("?" for _ in wanted)+")"
    reviewed_records={json.loads(row[0])["doc_id"]:row for row in db.execute(query,wanted)}
    review_ok=len(reviewed_records)==len(wanted)
    for sample in review["samples"]:
        row=reviewed_records.get(sample["doc_id"])
        review_ok &= bool(row and row[2]=="train" and json.loads(row[0])["canonical_sha256"]==sample["canonical_sha256"]
                          and len(row[1])==sample["characters"] and sample["reviewed_characters"]==min(420,len(row[1])) and sample["notes"].strip())
    db.close()
    checks["manual_train_preview_review_and_limits"]=review_ok and len(review["samples"])==len({x["doc_id"] for x in review["samples"]})==24 and review["reviewer_type"]=="assistant_manual_content_review" and bool(review["limitations"])
    cuda=args.run/"cuda"
    resume=read_json(cuda/"wsd_resume_report.json")
    checks["real_cuda_wsd_verification_report"]=resume["status"]=="passed_exact" and len(resume["checks"])>=73 and all(resume["checks"].values()) and resume["verification"]==c["verification"]
    checks["cuda_on_expanded_shards"]=resume["shard_manifest_sha256"]==sha256(args.data/"shards/manifest.json")
    checks["current_core_matches_verified_source"]=resume["implementation_sha256"]==implementation_hashes()
    model=read_json(ROOT/"reports/phase5/candidate_configs.json")["100m-no-qknorm"]["model_config"]
    checkpoint_count=0
    source_count=0
    fields=("model","optimizer","scheduler","rng","sampler","tokens","supervised_tokens","body_bytes","token_digest","spec","model_config","implementation_sha256","update")
    for prefix,a,b in [("stable","stable-continuous","stable-resumed"),("decay","decay-continuous","decay-resumed")]:
        states=[torch.load(cuda/name/"checkpoint-00000200.pt",map_location="cpu",weights_only=False) for name in (a,b)]
        checks[prefix+"_independent_all_state_exact"]=all(equal_state(states[0][key],states[1][key]) for key in fields)
        if prefix=="decay":
            checks["decay_independent_lineage_and_budget"]=all(equal_state(states[0][key],states[1][key]) for key in ("lineage","branch_updates","branch_tokens")) and states[0]["branch_updates"]==100 and states[0]["branch_tokens"]==819200
        rows=[[json.loads(line) for line in (cuda/name/"metrics.jsonl").read_text().splitlines()] for name in (a,b)]
        checks[prefix+"_independent_loss_lr_data_history_exact"]=len(rows[0])==len(rows[1])==(200 if prefix=="stable" else 100) and all([r[key] for r in rows[0]]==[r[key] for r in rows[1]] for key in ("update","loss","lr","tokens_seen","supervised_tokens","body_bytes_seen","token_digest","gradient_norm"))
        for name in (a,b):
            run=cuda/name
            record=read_json(run/"run.json")
            checks[name+"_terminal_and_budget"]=record["status"]=="complete" and record["update"]==200 and record["tokens_seen"]==1638400
            env=read_json(run/"environment.json")
            checks[name+"_wsl_python_cuda_bf16"]=env["platform"]["is_wsl"] and env["platform"]["python"]=="3.12.7" and env["torch_probe"]["cuda_available"] and env["torch_probe"]["bf16_supported"]
            source_hash=record["source_sha256"]
            checks[name+"_frozen_source_snapshot"]=all(sha256(run/"snapshot"/path)==value for path,value in source_hash.items())
            source_count+=len(source_hash)
            metric=[json.loads(line) for line in (run/"metrics.jsonl").read_text().splitlines()]
            checks[name+"_lr_and_finite_metrics"]=all(math.isfinite(r["loss"]) and math.isfinite(r["gradient_norm"]) and r["tokens_seen"]==r["update"]*8192 and r["lr"]==0.002*learning_rate_factor(record["spec"],r["update"]-1) for r in metric)
            latest=read_json(run/"latest.json")
            checks[name+"_latest_binding"]=latest["sha256"]==sha256(Path(latest["path"])) and latest["update"]==200
            finite=True
            bound=True
            for checkpoint in sorted(run.glob("checkpoint-*.pt")):
                checkpoint_count+=1
                state=torch.load(checkpoint,map_location="cpu",weights_only=False)
                bound &= (state["version"]==2 and state["model_config"]==model and state["implementation_sha256"]==implementation_hashes()
                          and state["shard_manifest_sha256"]==sha256(args.data/"shards/manifest.json") and state["spec"]==record["spec"]
                          and state["tokens"]==state["update"]*8192 and state["sampler"]["position"]==state["update"]*8)
                finite &= all(torch.isfinite(t).all().item() for t in state["model"].values())
                finite &= all(torch.isfinite(t).all().item() for row in state["optimizer"]["state"].values() for t in row.values() if isinstance(t,torch.Tensor))
            checks[name+"_all_checkpoints_bound_and_finite"]=bool(bound and finite)
    parent=cuda/"stable-resumed/checkpoint-00000100.pt"
    checks["branch_parent_immutable_and_history_independent"]=sha256(parent)==read_json(cuda/"stable_before_branches.json")[parent.name] and read_json(cuda/"branch_isolation.json")["passed"] and all(s["lineage"]["parent_sha256"]==sha256(parent) for s in [torch.load(cuda/name/"checkpoint-00000200.pt",map_location="cpu",weights_only=False) for name in ("decay-continuous","decay-resumed")])
    checks["actual_cuda_evaluation_state_isolated"]=read_json(cuda/"evaluation_isolation.json")["rng_and_model_preserved"] and resume["checks"]["cuda_evaluation_actual_dev"]
    xml=ET.parse(ROOT/"reports/phase6/tests.xml").getroot()
    cases=list(xml.iter("testcase"))
    checks["all_relevant_tests_pass_no_skip"]=len(cases)>=74 and not any(node.tag in ("failure","error","skipped") for node in xml.iter()) and all(any(case.attrib.get("name","")==name for case in cases) for name in ("test_wsd_resume_branch_and_stable_isolation_all_state","test_expansion_full_pipeline_audit_and_corruption_rejection","test_fast_signature_matches_scalar_hash_and_permutation_reference"))
    historical=read_json(args.windows_root/"reports/phase6/historical_binding.json")
    checks["all_historical_reports_unchanged"]=all(sha256(args.windows_root/path)==expected for path,expected in historical["files"].items())
    checks["dependency_lock_unchanged"]=sha256(args.windows_root/"uv.lock")==historical["dependency_lock_sha256"]==sha256(ROOT/"uv.lock")
    processes=[]
    for job_path in [args.data/"job.json",args.data/"audit_job.json",args.run/"job.json",cuda/"job.json"]:
        record=read_json(job_path)
        processes.append({"path":str(job_path),"status":record["status"],"pid":record["pid"],"alive_matching_identity":alive(record)})
    checks["all_preparation_jobs_terminal_and_exited"]=all(r["status"]=="complete" and not r["alive_matching_identity"] for r in processes)
    gpu=subprocess.run(["/usr/lib/wsl/lib/nvidia-smi","--query-compute-apps=pid,process_name","--format=csv,noheader"],capture_output=True,text=True,check=True)
    checks["gpu_idle_after_preparation"]=not gpu.stdout.strip()
    checks["restart_commands_and_process_identity_persisted"]=(cuda/"commands.json").exists() and all("boot_id" in read_json(p) and "start_ticks" in read_json(p) for p in [args.data/"job.json",args.data/"audit_job.json",args.run/"job.json",cuda/"job.json"])
    checks["pinned_python"]=platform.python_version()=="3.12.7"
    uv=subprocess.run([str(Path.home()/".local/bin/uv"),"--version"],capture_output=True,text=True,check=True).stdout.strip()
    report={"status":"passed" if all(checks.values()) else "failed","scope":"Phase6 steps 1-2 only; stop before step3 batch/speed exploration and long Base training",
            "completed_at":now(),"checks":checks,"data":{"path":str(args.data.resolve()),"split_documents":corpus_audit["split_documents"],"stream_tokens":corpus_audit["stream_tokens"],"body_tokens":corpus_audit["body_tokens"],"body_bytes":corpus_audit["body_bytes"],"planned_exposure":data["train_exposure"],"raw_bytes":sum(r["bytes"] for r in receipt["files"])},
            "cuda":{"path":str(cuda.resolve()),"resume_checks":len(resume["checks"]),"checkpoints_independently_verified":checkpoint_count,"snapshot_files_verified":source_count,"stable_updates":200,"decay_extra_updates":100,"actual_total_training_input_tokens":4915200},
            "tests":len(cases),"historical_report_files":len(historical["files"]),"processes":processes,"uv":uv,"python":platform.python_version(),
            "bindings":{"corpus_audit_sha256":sha256(args.data/"corpus_audit.json"),"data_manifest_sha256":sha256(args.data/"manifest.json"),"wsd_resume_report_sha256":sha256(cuda/"wsd_resume_report.json"),"quality_review_sha256":sha256(args.windows_root/"reports/phase6/quality_review.json"),"tests_sha256":sha256(ROOT/"reports/phase6/tests.xml"),"config_sha256":sha256(ROOT/"configs/phase6/preparation.json")},
            "storage":{"data_apparent_bytes":sum(p.stat().st_size for p in args.data.rglob("*") if p.is_file()),"cuda_apparent_bytes":sum(p.stat().st_size for p in cuda.rglob("*") if p.is_file()),"free_bytes":shutil.disk_usage(args.data).free},
            "not_achieved_or_not_in_scope":["Phase6 full Base/quality completion","maximum stable math batch and compiled/math optimization","500M/10B Base training","multiple-source/Chat mixture","NoNorm HF/GGUF adapter","20B/50B extension"],
            "data_quality_limits":review["limitations"]}
    write_json(args.output,report)
    if not all(checks.values()):
        raise ValueError(f'Preparation completion not proven: {[k for k,v in checks.items() if not v]}')
    print(json.dumps({"status":"passed","checks":len(checks),"train_tokens":corpus_audit["stream_tokens"]["train"],"checkpoints":checkpoint_count}),flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data",type=Path,required=True)
    p.add_argument("--run",type=Path,required=True)
    p.add_argument("--windows-root",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    audit(p.parse_args())


if __name__=="__main__":
    main()
