"""Measured parallel LSH execution; preserve frozen ingestion and independent audit."""
import argparse
import fcntl
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import sys
import time

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.corpus_state import read_json,write_json
from jmicro.experiment import ROOT,now,sha256
from jmicro.large_corpus import ingest,export
from jmicro.parallel_corpus_dedup import parallel_components
from jsonschema import Draft202012Validator


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config",type=Path,default=ROOT/"configs/phase6/corpus_10b.json")
    p.add_argument("--raw",type=Path,required=True)
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    c=read_json(args.config)
    Draft202012Validator(read_json(ROOT/"schemas/configs/phase6/corpus_10b.schema.json")).validate(c)
    args.output.mkdir(parents=True,exist_ok=True)
    with (args.output/"pipeline.lock").open("a+") as lock:
        fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        prior=read_json(args.output/"job.json")
        if prior["config_sha256"]!=sha256(args.config):
            raise ValueError("Persistent configuration differs")
        if prior["status"]=="running":
            path=Path(f'/proc/{prior["pid"]}/stat')
            if (path.exists() and path.read_text().split()[21]==prior["start_ticks"] and
                Path("/proc/sys/kernel/random/boot_id").read_text().strip()==prior["boot_id"]):
                raise RuntimeError("Another identified pipeline is alive")
        used=prior.get("cumulative_seconds",0)
        record={"status":"running","pid":os.getpid(),"started_at":now(),"command":sys.argv,
                "config_sha256":sha256(args.config),"execution":"parallel_bands_v3",
                "boot_id":Path("/proc/sys/kernel/random/boot_id").read_text().strip(),
                "start_ticks":Path("/proc/self/stat").read_text().split()[21],
                "prior_cumulative_seconds":used}
        started=time.monotonic()

        def interrupted(signum,frame):
            raise InterruptedError(f"Pipeline interrupted by signal{signum}; preserve all checkpoints")

        def budget(signum,frame):
            raise TimeoutError("Cumulative24hour preparation budget exhausted")

        signal.signal(signal.SIGTERM,interrupted)
        signal.signal(signal.SIGINT,interrupted)
        signal.signal(signal.SIGALRM,budget)
        signal.alarm(max(1,int(c["runtime_budget_seconds"]-used)))
        try:
            # Original source/ingestion bindings are retained byte-for-byte.
            original=read_json(args.output/"source_snapshot.json")
            for relative,expected in original.items():
                if sha256(ROOT/relative)!=expected:
                    raise ValueError(f"Original frozen source changed: {relative}")
            probe=read_json(ROOT/"reports/phase6/corpus_10b_parallel_probe.json")
            if (probe["status"]!="passed_exact_components_and_candidate_coverage" or
                not probe["groups_exact"] or not probe["duplicates_exact"] or probe["speedup"]<1.5):
                raise RuntimeError("Measured adoption gate has not passed")
            snapshot=args.output/"execution_v3_snapshot"
            extra=["src/jmicro/parallel_corpus_dedup.py","scripts/prepare_corpus_10b_parallel.py",
                   "scripts/run_corpus_10b_parallel.sh","reports/phase6/corpus_10b_parallel_probe.json"]
            hashes={}
            for relative in extra:
                target=snapshot/relative
                if target.exists() and sha256(target)!=sha256(ROOT/relative):
                    raise ValueError(f"Parallel execution source changed: {relative}")
                target.parent.mkdir(parents=True,exist_ok=True)
                if not target.exists():
                    shutil.copyfile(ROOT/relative,target)
                hashes[relative]=sha256(target)
            write_json(args.output/"execution_v3_snapshot.json",hashes)
            if shutil.disk_usage(args.output).free<c["minimum_free_bytes"]:
                raise RuntimeError("Insufficient disk reserve")
            if not (args.output/"ingest_complete.json").exists():
                record.update(stage="ingest",heartbeat_at=now())
                write_json(args.output/"job.json",record)
                ingest(args.config,args.raw,args.output,c["workers"])
            if not (args.output/"dedup_complete.json").exists():
                record.update(stage="parallel_external_lsh",heartbeat_at=now(),band_workers=8)
                write_json(args.output/"job.json",record)
                n=read_json(args.output/"ingest_complete.json")["records"]
                result=parallel_components(args.output,args.output/"parallel_bands",n,workers=8)
                for name in ("groups.npy","duplicates.npy"):
                    shutil.copyfile(args.output/"parallel_bands"/name,args.output/name)
                write_json(args.output/"dedup_complete.json",{
                    "records":n,"verified_pairs":result["verified_links"],
                    "count_scope":"Sum of within-band spanning verified links; not serial global link count",
                    "groups_sha256":sha256(args.output/"groups.npy"),
                    "duplicates_sha256":sha256(args.output/"duplicates.npy"),
                    "execution":"parallel_bands_v3","parallel_result_sha256":sha256(args.output/"parallel_bands/result.json")})
            if not (args.output/"manifest.json").exists():
                record.update(stage="export",heartbeat_at=now())
                write_json(args.output/"job.json",record)
                export(args.config,args.output,c["workers"])
            result=read_json(args.output/"manifest.json")
            if not result["target_met"]:
                raise RuntimeError("Prepared train remains below10B; preserve partial artifacts")
            if not (args.output/"corpus_audit.json").exists():
                record.update(stage="full_independent_serial_audit",heartbeat_at=now())
                write_json(args.output/"job.json",record)
                spec=importlib.util.spec_from_file_location("corpus_10b_audit",ROOT/"scripts/audit_corpus_10b.py")
                auditor=importlib.util.module_from_spec(spec)
                spec.loader.exec_module(auditor)
                auditor.audit(args.config,args.raw,args.output,c["workers"])
            if read_json(args.output/"corpus_audit.json")["status"]!="passed":
                raise RuntimeError("Full audit is incomplete")
            record.update(status="complete",completed_at=now())
            print(json.dumps({"status":"complete","train_tokens":result["splits"]["train"]["tokens"]}),flush=True)
        except Exception as exc:
            record.update(status="failed",completed_at=now(),failure=f"{type(exc).__name__}: {exc}")
            raise
        finally:
            record["cumulative_seconds"]=used+time.monotonic()-started
            signal.alarm(0)
            write_json(args.output/"job.json",record)


if __name__=="__main__":
    main()
