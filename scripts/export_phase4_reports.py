"""Keep small audited Phase 4 reports in Git; retain large raw runs in place."""
from pathlib import Path
import argparse
import json
import shutil
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from jmicro.experiment import ROOT, read_json, sha256, write_json


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", type=Path, required=True)
    args = parser.parse_args()
    report = read_json(args.run / "handoff_report.json")
    if report["status"] != "passed":
        raise ValueError("Export requires the actual Phase 4 audit to pass")
    destination = ROOT / "reports/phase4"
    report["auditor_sha256"] = sha256(ROOT / "scripts/audit_phase4.py")
    report["raw_evidence_sha256"] = {str(path):sha256(path) for path in [
        args.run / "throughput/throughput_report.json",
        *[args.run / f"resume-{model}/resume_report.json" for model in ("t8k","t4k")],
        *[args.run / f"evaluation-{model}.json" for model in ("t8k","t4k")],
        args.run / "common_short_windows.json"]}
    write_json(destination / "handoff_report.json", report)
    write_json(destination / "resume_report.json", {"status":"passed", "models":{
        name:read_json(args.run / f"resume-{name}/resume_report.json") for name in ("t8k","t4k")}})
    throughput = read_json(args.run / "throughput/throughput_report.json")
    for point in throughput["results"]:
        metrics = point.pop("metrics",None)
        if metrics:
            point["loss_range"] = [min(row["loss"] for row in metrics),max(row["loss"] for row in metrics)]
            point["gradient_norm_range"] = [min(row["gradient_norm"] for row in metrics),max(row["gradient_norm"] for row in metrics)]
        point["raw_report_sha256"] = sha256(Path(point["report"]))
    throughput["unsupported_optional_backends"] = report["unsupported_optional_backends"]
    write_json(destination / "throughput_report.json", throughput)
    contract = {"status":"passed", "quality_claim":report["quality_claim"],
        "common_short_windows": read_json(args.run / "common_short_windows.json"),
        "compiled_bf16_logit_parity": report["compiled_bf16_logit_parity"], "models":{}}
    for name in ("t8k","t4k"):
        evaluation = read_json(args.run / f"evaluation-{name}.json")
        body = {k:v for k,v in evaluation["body"].items() if k != "rows"}
        greedy = [r for r in evaluation["generation"]["outputs"] if r["suppressed"] and r["decoding"] == "greedy"]
        contract["models"][name] = {"body":body, "tokens_seen":evaluation["tokens_seen"],
            "generation_cases":len(greedy), "generation_outputs":len(evaluation["generation"]["outputs"]),
            "sampling_seeds":[42,43,44], "test_used":False,
            "diagnostic_greedy_counts":{ "denominator":len(greedy),
                "stop_success":sum(r["stop_reason"] == "stop_id" for r in greedy),
                **{key:sum(bool(r[key]) for r in greedy) for key in ("role_leak","valid_utf8","empty_response","repetition")}},
            "full_evaluation":str((args.run / f"evaluation-{name}.json").resolve())}
    write_json(destination / "base_evaluation_contract_report.json",contract)
    shutil.copyfile(args.run / "resource_budget.md",destination / "resource_budget.md")
    print(json.dumps({"status":"passed","destination":str(destination)}))


if __name__ == "__main__":
    main()
