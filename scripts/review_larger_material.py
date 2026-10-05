"""Review the unseen64 of the new matched500M/2B material, without training."""
import argparse
from collections import Counter
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.complete_units import unit_hash
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from phase6_performance import alive

DATA=Path("/home/aihub_ubuntu/jmicro-data/phase6/larger-material-20261006-95web-v3")
RUN=ROOT/"reports/phase6/larger-material-20261006-95web-v3"
REVIEW=ROOT/"reports/phase6/larger_material_v3_content_review.json"
NOTES=ROOT/"reports/phase6/larger_material_v3_content_notes.json"


def validate_notes(samples,document,sample_sha):
    assert document["sample_sha256"]==sample_sha and isinstance(document["reviewer"],str) and document["reviewer"].strip()
    assert document["independent_human_blind"] is False
    notes=document["notes"]
    assert len(samples)==len(notes)==64 and {n[0] for n in notes}==set(range(64))
    assert all(type(n[0]) is int and type(n[1]) is bool and isinstance(n[2],str) and len(n[2].strip())>=12 for n in notes)
    return [dict(sample_index=n[0],weak=n[1],rationale=n[2],**samples[n[0]]) for n in notes]


def prepared():
    job=read_json(RUN/"prepare-job.json");ready=read_json(DATA/"ready.json")
    assert job["status"]=="complete" and not alive(job) and job["seconds"]<=job["binding"]["CPU_budget_seconds"]==1800
    assert ready["binding"]==job["binding"] and ready["nested_ratio_exact"]==4
    assert all(ready[k] for k in ("small_subset_of_large","source_length_EOS_histograms_exact_ratio","editorial_unit_histograms_exact_ratio"))
    pools=ready["pools"]; small=pools["small"]["splits"]["train"]; large=pools["large"]["splits"]["train"]
    assert small["tokens"]>=500000000 and large["tokens"]==4*small["tokens"] and large["documents"]==4*small["documents"]
    assert Counter(ready["histograms"]["large"])==Counter({k:4*v for k,v in ready["histograms"]["small"].items()})
    for entry in pools.values(): assert sha256(Path(entry["pool"])/"manifest.json")==entry["manifest_sha256"]
    samples=read_json(DATA/"sample64.json")
    assert sha256(DATA/"sample64.json")==ready["sample_sha256"] and len(samples)==64
    assert Counter(u["source"] for u in samples)==Counter(web=32,story=32)
    assert all(unit_hash(u["text"])==u["canonical_sha256"] and u["split"]=="train" for u in samples)
    return ready,samples


def review(template=False):
    ready,samples=prepared()
    if template:
        assert not NOTES.exists(),"Existing notes retained; never replace completed judgments with a blank template"
        write_json(NOTES,dict(reviewer="Codex nonblind; all64 original documents require individual review",
            independent_human_blind=False,sample_sha256=ready["sample_sha256"],
            notes=[[i,None,""] for i in range(64)]))
        print(f"Unscored64 template: {NOTES}");return
    reviews=validate_notes(samples,read_json(NOTES),ready["sample_sha256"])
    weak=sum(r["weak"] for r in reviews)
    result=dict(status="fixed_content_review_complete",passed=weak<=10,weak_documents=weak,documents=64,
        ready_sha256=sha256(DATA/"ready.json"),sample_sha256=ready["sample_sha256"],notes_sha256=sha256(NOTES),
        pools=ready["pools"],reviews=reviews,independent_human_blind=False,
        method="Codex nonblind all64 raw-bound notes; fiction/opinion/genre alone does not fail content",
        limitations="No independent corpus-wide near-duplicate, site/author or factual audit; material readiness does not prove model quality",
        decision="Eligible for matched quantity research, no Base adoption" if weak<=10 else "Failed unchanged content criterion; preserve all64 and revise prospectively",
        Base_adopted=False,scientific_teacher_tokens=0,protected_test_used=False,
        requested_five_steps_complete=False,old_numerical7_preserved=True,created_at=now())
    write_json(RUN/"content-review.json",result);write_json(REVIEW,result)
    print(dict(passed=result["passed"],weak_documents=weak,small=ready["pools"]["small"]["splits"]["train"]["tokens"],large=ready["pools"]["large"]["splits"]["train"]["tokens"]))


if __name__=="__main__":
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument("--template",action="store_true");review(p.parse_args().template)
