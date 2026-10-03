"""Verify audited local corpus delivery and actual training-loader usability.

Run after preparation has terminated successfully. This creates no model and
performs no optimizer update, inference or evaluation of the heldout text.
"""
import argparse
import json
from pathlib import Path
import sys
import time

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
import numpy as np
from jmicro.corpus_state import read_json,write_json
from jmicro.experiment import ROOT,now,sha256
from jmicro.shards import Shard,BlockSampler


def check(config,output,report):
    started=time.perf_counter()
    c=read_json(config)
    job=read_json(output/"job.json")
    if job["status"]!="complete":
        raise ValueError("Preparation has not completed")
    process=Path(f'/proc/{job["pid"]}/stat')
    if (process.exists() and Path("/proc/sys/kernel/random/boot_id").read_text().strip()==job["boot_id"] and
        process.read_text().split()[21]==job["start_ticks"]):
        raise ValueError("Preparation process is still live; verify terminal delivery after exit")
    manifest=read_json(output/"manifest.json")
    audit=read_json(output/"corpus_audit.json")
    if (audit["status"]!="passed" or audit["manifest_sha256"]!=sha256(output/"manifest.json") or
        manifest["config_sha256"]!=sha256(config)):
        raise ValueError("Final audit/manifest/config binding differs")
    if manifest["splits"]["train"]["tokens"]<c["minimum_train_stream_tokens"]:
        raise ValueError("Prepared training corpus is below target")
    artifact=Path(manifest["artifact_directory"])
    if str(artifact)!=audit["artifact_directory"]:
        raise ValueError("Audited artifact directory differs")
    shard_manifest=read_json(artifact/"shards/manifest.json")
    if shard_manifest["splits"]!=manifest["splits"]:
        raise ValueError("Delivered shard counts/hashes differ")
    if sha256(ROOT/c["tokenizer"])!=shard_manifest["tokenizer_sha256"]:
        raise ValueError("Training tokenizer binding differs")
    shard=Shard(artifact/"shards","train")
    sampler=BlockSampler(shard,context=1024,seed=42)
    before=sampler.state_dict()
    inputs,labels,body_bytes=sampler.batch(2)
    ids=inputs.numpy()
    targets=labels.numpy()
    if ids.shape!=(2,1024) or targets.shape!=(2,1024):
        raise ValueError("Actual training batch shape differs")
    if np.any(ids<0) or np.any(ids>=shard_manifest["vocab_size"]):
        raise ValueError("Training inputs exceed tokenizer vocabulary")
    if (np.any((targets!=-100)&((targets<0)|(targets>=shard_manifest["vocab_size"]))) or
        np.any(targets==2) or not np.any(targets>=8) or body_bytes<=0):
        raise ValueError("Teacher-mask/body-byte accounting is invalid")
    sampler.load_state_dict(before)
    repeated_inputs,repeated_labels,repeated_bytes=sampler.batch(2)
    if (not np.array_equal(ids,repeated_inputs.numpy()) or
        not np.array_equal(targets,repeated_labels.numpy()) or repeated_bytes!=body_bytes):
        raise ValueError("Actual block sampler replay differs")
    result={"status":"passed_actual_training_loader","completed_at":now(),
            "target_train_tokens":c["minimum_train_stream_tokens"],"prepared_splits":manifest["splits"],
            "artifact_directory":str(artifact),"shards":str(artifact/"shards"),
            "manifest_sha256":sha256(output/"manifest.json"),
            "corpus_audit_sha256":sha256(output/"corpus_audit.json"),
            "shard_manifest_sha256":sha256(artifact/"shards/manifest.json"),
            "loader":"jmicro.shards.Shard/BlockSampler; unchanged production implementation",
            "batch_shape":[2,1024],"sampler_replay_exact":True,"training_updates":0,
            "test_usage":"none; train loader only","elapsed_seconds":time.perf_counter()-started}
    write_json(report,result)
    return result


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--config",type=Path,default=ROOT/"configs/phase6/corpus_10b.json")
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--report",type=Path,required=True)
    args=p.parse_args()
    print(json.dumps(check(args.config,args.output,args.report)),flush=True)
