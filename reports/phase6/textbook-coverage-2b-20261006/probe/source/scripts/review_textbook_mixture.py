"""All64 raw-bound content acceptance for Web75/textbook20/story5."""
import argparse
from collections import Counter
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from jmicro.complete_units import unit_hash
from jmicro.experiment import ROOT,read_json,write_json,sha256,now
from phase6_performance import alive
from prepare_textbook_mixture import DATA,RUN,QUOTAS
from review_larger_material import validate_notes

NOTES=ROOT/"reports/phase6/textbook_mixture_content_notes.json"
REVIEW=ROOT/"reports/phase6/textbook_mixture_content_review.json"


def review(template=False):
    job=read_json(RUN/"job.json");ready=read_json(DATA/"ready.json")
    assert job["status"]=="complete" and not alive(job) and job["seconds"]<=900
    assert ready["binding"]==job["binding"] and ready["binding"]["source_ratio"]==dict(web=.75,textbook=.20,story=.05)
    assert ready["nested_ratio_exact"]==4
    assert all(ready[k] for k in ("small_subset_of_large","source_length_EOS_histograms_exact_ratio","editorial_unit_histograms_exact_ratio"))
    pools=ready["pools"];small=pools["small"]["splits"]["train"];large=pools["large"]["splits"]["train"]
    assert small["tokens"]>=500000000 and large["tokens"]==4*small["tokens"] and large["documents"]==4*small["documents"]
    assert Counter(ready["histograms"]["large"])==Counter({k:4*v for k,v in ready["histograms"]["small"].items()})
    for ref in pools.values():assert sha256(Path(ref["pool"])/"manifest.json")==ref["manifest_sha256"]
    samples=read_json(DATA/"sample64.json")
    assert len(samples)==64 and Counter(u["source"] for u in samples)==Counter(QUOTAS)
    assert sha256(DATA/"sample64.json")==ready["sample_sha256"]
    assert all(unit_hash(u["text"])==u["canonical_sha256"] and u["split"]=="train" for u in samples)
    if template:
        assert not NOTES.exists(),"Preserve all existing judgments"
        write_json(NOTES,dict(reviewer="Codex nonblind; all64 require individual reading",independent_human_blind=False,
            sample_sha256=ready["sample_sha256"],notes=[[i,None,""] for i in range(64)]))
        print(f"Unscored64 template: {NOTES}");return
    reviews=validate_notes(samples,read_json(NOTES),ready["sample_sha256"]);weak=sum(r["weak"] for r in reviews)
    result=dict(status="fixed_content_review_complete",passed=weak<=10,weak_documents=weak,documents=64,
        ready_sha256=sha256(DATA/"ready.json"),sample_sha256=ready["sample_sha256"],notes_sha256=sha256(NOTES),
        pools=pools,reviews=reviews,source_quota=QUOTAS,independent_human_blind=False,
        method="All64 individually nonblind reviewed; stratified24Web/24textbook/16story, not a population weakness rate",
        limitations="Synthetic facts and global/cross-source near duplicates unverified; no independent human evidence",
        decision="Eligible for matched1B research; no adoption" if weak<=10 else "Failed unchanged weak<=10; preserve and revise prospectively",
        Base_adopted=False,Chat_adopted=False,scientific_teacher_tokens=0,protected_test_used=False,
        old_numerical7_preserved=True,requested_five_steps_complete=False,created_at=now())
    write_json(RUN/"content-review.json",result);write_json(REVIEW,result)
    print(dict(passed=weak<=10,weak_documents=weak,prepared_small=small["tokens"],prepared_large=large["tokens"]))


if __name__=="__main__":
    assert sys.version_info[:3]==(3,12,7)
    p=argparse.ArgumentParser();p.add_argument("--template",action="store_true");review(p.parse_args().template)
