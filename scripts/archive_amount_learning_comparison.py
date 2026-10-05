"""Preserve completed stage4 text evidence; retain tensors/shards at WSL paths."""
from pathlib import Path
import sys
import tarfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from phase6_performance import alive


def archive():
    run = ROOT/"reports/phase6/amount-learning-20261006"
    job,review = read_json(run/"job.json"),read_json(run/"review.json")
    assert job["status"] == "complete" and not alive(job)
    assert review["status"] == "stage4_learning_and_all400_content_evidence_complete"
    assert review["scientific_stable_teachers"] == 3000000000 and review["scientific_decay_teachers"] == 100000000
    files = {p for p in run.rglob("*") if p.is_file() and p.suffix in (".json",".jsonl",".py",".ps1",".xml")}
    files.update(ROOT/p for p in (
        "configs/phase6/amount_learning_comparison.json",
        "scripts/review_amount_learning_comparison.py","scripts/archive_amount_learning_comparison.py",
        "reports/phase6/learning_curve_tests.xml","reports/phase6/amount_learning_trainer_tests.xml",
        "reports/phase6/nested_material_ready.json","reports/phase6/nested_material_content_review.json",
        "reports/phase6/nested_material_content_notes.json","reports/phase6/nested_material_v1_supply_failure.json",
        "reports/phase6/nested_material_v2_prepare_job.json"))
    files.update(ROOT/f"reports/phase6/amount_learning_{key}_notes.json" for key in review["summaries"])
    files = sorted(files);target = ROOT/"reports/phase6/amount_learning_evidence.tar.gz"
    with tarfile.open(target,"w:gz",compresslevel=3) as bundle:
        for path in files: bundle.add(path,arcname=str(path.relative_to(ROOT)),recursive=False)
    report = dict(path=str(target.relative_to(ROOT)),sha256=sha256(target),bytes=target.stat().st_size,
        members=[dict(path=str(p.relative_to(ROOT)),sha256=sha256(p),bytes=p.stat().st_size) for p in files],
        limitations="Checkpoint tensors and large data streams/indexes remain at their bound WSL paths; source history/global near-duplicate limitations retained",
        created_at=now())
    write_json(ROOT/"reports/phase6/amount_learning_evidence_manifest.json",report)
    print(f"Archived {len(files)} text files, {report['bytes']} bytes",flush=True)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3,12,7);archive()
