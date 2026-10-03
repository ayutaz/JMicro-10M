"""Persist step 1-2 audits; wait only for the identified live data builder."""
from pathlib import Path
import argparse
import fcntl
import json
import os
import subprocess
import sys
import time

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.experiment import ROOT,now,read_json,write_json


def process_alive(record):
    path=Path(f'/proc/{record["pid"]}/stat')
    try:
        return (Path("/proc/sys/kernel/random/boot_id").read_text().strip()==record["boot_id"]
                and path.read_text().split()[21]==record["start_ticks"])
    except FileNotFoundError:
        return False


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--raw",type=Path,required=True)
    p.add_argument("--data",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    record={"status":"running","pid":os.getpid(),"started_at":now(),"command":sys.argv,
            "boot_id":Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
            "start_ticks":Path("/proc/self/stat").read_text().split()[21]}
    with (args.output.parent/"readiness-supervisor.lock").open("a+") as stream:
        fcntl.flock(stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
        try:
            builder=read_json(args.data/"job.json")
            while builder["status"]=="running":
                if not process_alive(builder):
                    # Re-read terminal state after observing the process exit.
                    builder=read_json(args.data/"job.json")
                    if builder["status"]=="running":
                        raise RuntimeError("Identified data builder exited without terminal evidence; inspect before restarting")
                    break
                record.update(stage="waiting_for_identified_data_builder",builder=builder,heartbeat_at=now())
                write_json(args.output/"job.json",record)
                time.sleep(5)
                builder=read_json(args.data/"job.json")
            if builder["status"]!="complete":
                raise RuntimeError("Data build is terminal and failed")
            c=read_json(ROOT/"configs/phase6/preparation.json")
            if read_json(args.data/"manifest.json")["splits"]["train"]["tokens"] < c["minimum_train_stream_tokens"]:
                raise RuntimeError("Acquire additional frozen source files; 500M unique tokens not met")
            gpu=subprocess.run(["/usr/lib/wsl/lib/nvidia-smi","--query-compute-apps=pid","--format=csv,noheader"],capture_output=True,text=True,check=True)
            if gpu.stdout.strip():
                raise RuntimeError("An existing GPU process is present; inspect it before verification")
            tasks=[("data_audit",[sys.executable,str(ROOT/"scripts/audit_phase6_data.py"),"--raw",str(args.raw),"--output",str(args.data)],args.data/"corpus_audit.json","passed"),
                   ("cuda_resume",[sys.executable,str(ROOT/"scripts/verify_phase6_preparation.py"),"--shards",str(args.data/"shards"),"--output",str(args.output/"cuda")],args.output/"cuda/wsd_resume_report.json","passed_exact")]
            children=[]
            for name,command,result,expected in tasks:
                if result.exists() and read_json(result)["status"]==expected:
                    continue
                log=(args.output/f"{name}.log").open("a",buffering=1)
                child=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT)
                children.append((name,child,log,result,expected))
            record.update(stage="full_data_audit_and_cuda_resume",children=[{"name":name,"pid":child.pid} for name,child,_,_,_ in children])
            write_json(args.output/"job.json",record)
            while any(child.poll() is None for _,child,_,_,_ in children):
                record["heartbeat_at"]=now()
                write_json(args.output/"job.json",record)
                time.sleep(5)
            for name,child,log,result,expected in children:
                log.close()
                if child.returncode or not result.exists() or read_json(result)["status"]!=expected:
                    raise RuntimeError(f"{name} failed; inspect its preserved log")
            record.update(status="complete",completed_at=now())
            print(json.dumps({"status":"complete","scope":"data audit and CUDA preparation only"}),flush=True)
        except Exception as exc:
            record.update(status="failed",completed_at=now(),failure=f"{type(exc).__name__}: {exc}")
            raise
        finally:
            write_json(args.output/"job.json",record)


if __name__=="__main__":
    main()
