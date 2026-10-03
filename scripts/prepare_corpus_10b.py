"""Persistent, exclusive 10B data preparation; never starts model training."""
import argparse
import fcntl
import json
import os
from pathlib import Path
import shutil
import signal
import importlib.util
import sys
import time

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.experiment import ROOT,now,sha256
from jmicro.corpus_state import read_json,write_json
from jmicro.large_corpus import ingest,deduplicate,export
from jsonschema import Draft202012Validator


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config",type=Path,default=ROOT/"configs/phase6/corpus_10b.json")
    p.add_argument("--raw",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--workers",type=int,default=16)
    p.add_argument("--wait-for-acquisition",action="store_true")
    args=p.parse_args()
    c=read_json(args.config)
    Draft202012Validator(read_json(ROOT/"schemas/configs/phase6/corpus_10b.schema.json")).validate(c)
    args.output.mkdir(parents=True,exist_ok=True)
    with (args.output/"pipeline.lock").open("a+") as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        prior=read_json(args.output/"job.json") if (args.output/"job.json").exists() else {}
        if prior.get("config_sha256",sha256(args.config))!=sha256(args.config):
            raise ValueError("Persistent pipeline configuration changed")
        used=prior.get("cumulative_seconds",0)
        record={"status":"running","pid":os.getpid(),"started_at":now(),"command":sys.argv,
                "config_sha256":sha256(args.config),
                "boot_id":Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
                "start_ticks":Path("/proc/self/stat").read_text().split()[21]}
        started=time.monotonic()
        def timeout(signum,frame):
            raise TimeoutError("Cumulative preparation runtime budget exhausted; preserve checkpoints")
        signal.signal(signal.SIGALRM,timeout)
        signal.alarm(max(1,int(c["runtime_budget_seconds"]-used)))
        try:
            snapshot=args.output/"source_snapshot"
            sources=["src/jmicro/large_corpus.py","scripts/prepare_corpus_10b.py",
                     "src/jmicro/corpus_state.py",
                     "scripts/audit_corpus_10b.py","scripts/run_corpus_10b.sh",
                     "src/jmicro/expanded_data.py","src/jmicro/data.py","src/jmicro/evaluation.py",
                     "src/jmicro/tokenizer.py","uv.lock","configs/phase6/corpus_10b.json",
                     "schemas/configs/phase6/corpus_10b.schema.json"]
            hashes={}
            for relative in sources:
                original=ROOT/relative
                target=snapshot/relative
                if target.exists() and sha256(target)!=sha256(original):
                    raise ValueError(f"Source snapshot changed: {relative}")
                target.parent.mkdir(parents=True,exist_ok=True)
                if not target.exists():
                    shutil.copyfile(original,target)
                hashes[relative]=sha256(target)
            write_json(args.output/"source_snapshot.json",hashes)
            if shutil.disk_usage(args.output).free<c["minimum_free_bytes"]:
                raise RuntimeError("Insufficient disk reserve for raw, intermediate, export and audit")
            if args.wait_for_acquisition:
                while True:
                    acquisition=read_json(args.raw/"acquire_job.json")
                    if acquisition["status"]=="complete":
                        break
                    if acquisition["status"]!="running":
                        raise RuntimeError("Acquisition failed; inspect preserved log")
                    try:
                        live=(Path("/proc/sys/kernel/random/boot_id").read_text().strip()==acquisition["boot_id"] and
                              Path(f'/proc/{acquisition["pid"]}/stat').read_text().split()[21]==acquisition["start_ticks"])
                    except FileNotFoundError:
                        live=False
                    if not live:
                        final=read_json(args.raw/"acquire_job.json")
                        if final["status"]=="complete":
                            break
                        raise RuntimeError("Identified acquisition process exited without completion")
                    record.update(stage="waiting_for_identified_acquisition",heartbeat_at=now(),
                                  acquisition_pid=acquisition["pid"])
                    write_json(args.output/"job.json",record)
                    time.sleep(5)
            for stage,function in [("ingest",lambda:ingest(args.config,args.raw,args.output,args.workers)),
                                   ("dedup",lambda:deduplicate(args.output)),
                                   ("export",lambda:export(args.config,args.output,args.workers))]:
                completed=args.output/({"ingest":"ingest_complete.json","dedup":"dedup_complete.json",
                                       "export":"manifest.json"}[stage])
                if completed.exists():
                    continue
                if time.monotonic()-started>c["runtime_budget_seconds"]:
                    raise TimeoutError("Preparation reached measured-budget ceiling")
                record.update(stage=stage,heartbeat_at=now())
                write_json(args.output/"job.json",record)
                function()
            result=read_json(args.output/"manifest.json")
            if not result["target_met"]:
                raise RuntimeError("Prepared train is below10B; preserve partial results and reassess bounded acquisition")
            audit_path=args.output/"corpus_audit.json"
            if not audit_path.exists():
                record.update(stage="full_independent_audit",heartbeat_at=now())
                write_json(args.output/"job.json",record)
                spec=importlib.util.spec_from_file_location("corpus_10b_audit",ROOT/"scripts/audit_corpus_10b.py")
                auditor=importlib.util.module_from_spec(spec)
                spec.loader.exec_module(auditor)
                auditor.audit(args.config,args.raw,args.output,args.workers)
            if read_json(audit_path)["status"]!="passed":
                raise RuntimeError("Independent corpus audit has not passed")
            record.update(status="complete",completed_at=now())
            print(json.dumps({"status":record["status"],"train_tokens":result["splits"]["train"]["tokens"]}),flush=True)
        except Exception as exc:
            record.update(status="failed",completed_at=now(),failure=f"{type(exc).__name__}: {exc}")
            raise
        finally:
            record["cumulative_seconds"]=used+time.monotonic()-started
            signal.alarm(0)
            write_json(args.output/"job.json",record)


if __name__=="__main__":
    main()
