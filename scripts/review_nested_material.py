"""Fixed raw-bound64 content judgments; preparation is not model quality."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from jmicro.experiment import ROOT, read_json, write_json, sha256, now
from phase6_performance import alive

DATA = Path("/home/aihub_ubuntu/jmicro-data/phase6/nested-material-20261006-v2")
RUN = ROOT / "reports/phase6/nested-material-20261006-v2"


if __name__ == "__main__":
    assert sys.version_info[:3] == (3, 12, 7)
    job = read_json(RUN / "prepare-job.json")
    ready = read_json(DATA / "ready.json")
    assert job["status"] == "complete" and not alive(job) and job["seconds"] <= 600
    assert ready["binding"] == job["binding"]
    assert ready["pools"]["small"]["splits"]["train"]["tokens"] == 100000157
    assert ready["pools"]["large"]["splits"]["train"]["tokens"] == 500000785
    assert ready["nested_ratio_exact"] == 5 and ready["source_length_EOS_histograms_exact_ratio"]
    assert ready["editorial_unit_histograms_exact_ratio"] and ready["small_subset_of_large"]
    for entry in ready["pools"].values():
        assert sha256(Path(entry["pool"]) / "manifest.json") == entry["manifest_sha256"]
    samples = read_json(DATA / "sample64.json")
    notes_path = ROOT / "reports/phase6/nested_material_content_notes.json"
    notes = read_json(notes_path)["notes"]
    assert len(notes) == len(samples) == 64 and {n[0] for n in notes} == set(range(64))
    assert sha256(DATA / "sample64.json") == ready["sample_sha256"]
    assert all(type(n[1]) is bool and len(n[2]) >= 12 for n in notes)
    reviews = [dict(sample_index=n[0], weak=n[1], rationale=n[2], **samples[n[0]]) for n in notes]
    weak = sum(r["weak"] for r in reviews)
    report = dict(status="fixed_content_review_complete", passed=weak <= 10, weak_documents=weak,
        documents=64, ready_sha256=sha256(DATA / "ready.json"), sample_sha256=ready["sample_sha256"],
        notes_sha256=sha256(notes_path), pools=ready["pools"], reviews=reviews,
        method="Codex nonblind all64 individual raw documents; genre/opinion/fiction alone is not a content failure",
        independent_human_blind=False, numerical_failures72_preserved=True,
        limitations="Historical/political/medical/financial claims independently unverified; fictional/anthropomorphic and some promotional/technical writing remain. Readiness does not certify everyday-only data or useful model generation",
        scientific_teacher_tokens=0, protected_test_used=False, requested_five_steps_complete=False,
        decision="Eligible for frozen amount-vs-learning research; no Base adoption" if weak <= 10 else "Content criterion failed; preserve all64 and revise prospectively with unseen sample",
        created_at=now())
    write_json(RUN / "content-review.json", report)
    write_json(ROOT / "reports/phase6/nested_material_content_review.json", report)
    print(dict(passed=report["passed"], weak_documents=weak, small=100000157, large=500000785), flush=True)
