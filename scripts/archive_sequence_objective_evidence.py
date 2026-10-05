"""Archive completed text evidence, retaining tensor checkpoints in WSL."""
import json
from pathlib import Path
import sys
import tarfile

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.experiment import ROOT,read_json,sha256,write_json,now
from phase6_performance import alive
from run_sequence_objective_comparison import RUN,CONFIG,PROBE_CONFIG,preflight


def archive():
    c,_,_=preflight(CONFIG);job=read_json(RUN/"job.json");review=read_json(RUN/"review.json")
    assert job["status"]=="complete" and not alive(job)
    assert review["status"]=="matched_CE_sequence_UL_learning_and_all160_content_evidence_complete"
    assert review["result_sha256"]==sha256(RUN/"compare-result.json")
    assert review["annotations_sha256"]==sha256(RUN/"annotations.json")
    assert not review["Base_adopted"] and not review["protected_test_used"]
    paths=[p for p in RUN.rglob("*") if p.is_file() and p.suffix in (".json",".jsonl",".py",".ps1",".xml")]
    paths.extend([CONFIG,PROBE_CONFIG,ROOT/"configs/phase6/sequence_objective_timing.json",
                  ROOT/"configs/phase6/sequence_objective_timing_v2.json"])
    for arm in ("CE","CE_UL"):
        paths.extend(ROOT/f"reports/phase6/sequence_objective_{arm}_{suffix}.json"
                     for suffix in ("notes","content_review","candidate_inspection"))
    paths.extend([ROOT/"reports/phase6/sequence_objective_timing_failure.json",
                  ROOT/"reports/phase6/sequence_objective_budget_freeze_rejection.json"])
    paths=sorted(set(paths));assert all(p.is_file() for p in paths)
    manifest=ROOT/"reports/phase6/sequence_objective_evidence_manifest.json"
    entries=[dict(path=p.relative_to(ROOT).as_posix(),bytes=p.stat().st_size,sha256=sha256(p)) for p in paths]
    write_json(manifest,dict(status="completed_text_evidence_archive",entries=entries,text_files=len(entries),
        uncompressed_bytes=sum(e["bytes"] for e in entries),checkpoint_tensors_included=False,
        native_checkpoints_retained=True,scientific_teacher_tokens=50000000,
        verification_teacher_tokens=c["verification_teacher_tokens"],created_at=now()))
    output=ROOT/"reports/phase6/sequence-objective-comparison-20261006_evidence.tar.gz"
    assert not output.exists(),"Completed archive is immutable"
    temporary=output.with_suffix(output.suffix+".tmp")
    with tarfile.open(temporary,"w:gz",compresslevel=1) as stream:
        for path in (*paths,manifest):stream.add(path,arcname=path.relative_to(ROOT).as_posix(),recursive=False)
    temporary.replace(output)
    print(json.dumps(dict(archive=str(output),sha256=sha256(output),bytes=output.stat().st_size,
                          text_files=len(entries),uncompressed_bytes=sum(e["bytes"] for e in entries))))


if __name__=="__main__":
    assert sys.version_info[:3]==(3,12,7)
    archive()
