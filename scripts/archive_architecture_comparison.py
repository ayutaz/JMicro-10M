"""Preserve complete text evidence for the matched architecture experiment."""
from pathlib import Path
import sys
import tarfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from phase6_performance import alive


def archive():
    run = ROOT / "reports/phase6/architecture-comparison-20261006"
    job = read_json(run / "job.json")
    assert job["status"] == "complete" and not alive(job)
    review = read_json(run / "review.json")
    assert review["status"] == "stage3_learning_and_content_evidence_complete"
    assert review["scientific_teacher_tokens_new"] == 600000000
    assert review["reused_current_teacher_tokens"] == 300000000
    files = {
        p for p in run.rglob("*")
        if p.is_file() and p.suffix in (".json", ".jsonl", ".py", ".ps1", ".xml", ".md")
    }
    files.update(ROOT / p for p in (
        "configs/phase6/architecture_comparison.json",
        "scripts/review_architecture_comparison.py",
        "scripts/archive_architecture_comparison.py",
        "reports/phase6/architecture_comparison_fewer_layers_more_FFN_notes.json",
        "reports/phase6/architecture_comparison_wider_fewer_layers_notes.json",
        "reports/phase6/material_comparison_review.json",
        "reports/phase6/material_comparison_annotations.json",
        "reports/phase6/material_comparison_evidence_manifest.json",
    ))
    files = sorted(files)
    target = ROOT / "reports/phase6/architecture_comparison_evidence.tar.gz"
    with tarfile.open(target, "w:gz", compresslevel=3) as bundle:
        for path in files:
            bundle.add(path, arcname=str(path.relative_to(ROOT)), recursive=False)
    report = dict(
        path=str(target.relative_to(ROOT)), sha256=sha256(target),
        bytes=target.stat().st_size,
        members=[dict(path=str(p.relative_to(ROOT)), sha256=sha256(p), bytes=p.stat().st_size) for p in files],
        limitations="Checkpoint tensors/shards remain at bound WSL paths; current13-layer raw evidence is in the separately bound material archive",
        created_at=now(),
    )
    write_json(ROOT / "reports/phase6/architecture_comparison_evidence_manifest.json", report)
    print(f"Archived {len(files)} text evidence files, {report['bytes']} bytes", flush=True)


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    archive()
