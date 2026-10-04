"""Publish compact, corrected statistics from saved evidence; no GPU reruns."""
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from jmicro.japanese_evaluation import clustered_ci
from evaluate_japanese_base import summarize

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "reports/phase6/japanese-base-v2-20261004"
REVISION = ROOT / "reports/phase6/japanese-base-v2-20261004-r1/pilot"


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def validate_sources(directory):
    result = read(directory / "result.json")
    for name, expected in result["source_sha256"].items():
        path = directory / "source" / ("data-manifest.json" if name == "data_manifest" else name)
        if sha(path) != expected:
            raise ValueError(f"Frozen source differs: {path}")
    validation = read(directory / "scorer-validation.json")
    if not validation["finite"] or not validation["manual_target_gather_passed"]:
        raise ValueError("Actual GPU scorer validation failed")
    if max(validation["padded_vs_single_absolute_nll"]) > validation["maximum_allowed_absolute_nll"]:
        raise ValueError("Actual padding validation failed")
    if not result["complete"] or result["gpu_seconds"] > result["budget_seconds"]:
        raise ValueError("Incomplete or over-budget GPU evaluation")
    if result["additional_training_tokens"] or result["protected_test_used"]:
        raise ValueError("Unexpected learning/test evaluation")
    return result


def main():
    original = validate_sources(RAW / "full")
    corrected = validate_sources(REVISION)
    checkpoints = {result["checkpoint_sha256"] for result in (original, corrected)}
    if len(checkpoints) != 1 or original["parameters"] != 10001152:
        raise ValueError("Model identity differs")
    expected = {"semantics":192, "jblimp":331, "jcqa":1119, "jnli_0shot":2434, "jnli_3shot":2434,
                "jcola_in_0shot":865, "jcola_in_2shot":865, "jcola_out_0shot":685, "jcola_out_2shot":685}
    results, evidence = {}, {}
    for name, count in expected.items():
        directory = REVISION if name == "semantics" else RAW / "full"
        path = directory / (name + ".json")
        task = read(path)
        rows = task["rows"]
        if not task["complete"] or len(rows) != count or len({r["id"] for r in rows}) != count:
            raise ValueError(f"Missing/duplicate task rows: {name}")
        for row in rows:
            if not 0 <= row["label"] < len(row["choices"]) or not all(math.isfinite(s) for s in row["scores"]):
                raise ValueError("Nonfinite or invalid candidate score")
            if name.startswith("jnli"):
                row["family"] = row["family"].split("-")[0]
        summary = summarize(rows, task["control"])
        summary["source"] = str(path.relative_to(ROOT))
        summary["source_sha256"] = sha(path)
        if name == "jblimp":
            summary["raw_pair_accuracy"] = sum(row["raw_credit"] for row in rows)/count
            summary["primary_metric"] = "first-2M-train-token sample SLOR, add-one smoothing; not original-paper reproduction"
            for condition in ("primary", "per_token_secondary", "unigram_control"):
                for metric in ("mcc", "macro_f1", "confusion_matrix", "hard_accuracy", "confusion_ties"):
                    summary[condition].pop(metric, None)
        if name == "semantics":
            families = defaultdict(list)
            for row in rows:
                families[row["family"]].append(row)
            if len({row["context"] for row in rows}) != count:
                raise ValueError("Semantic contexts are duplicated")
            if len(families) != 96 or any(len(pair) != 2 or {r["label"] for r in pair} != {0,1} for pair in families.values()):
                raise ValueError("Semantic family counterbalancing differs")
            summary["both_contexts_correct"] = clustered_ci([
                {"id": family, "credit": int(all(row["credit"] == 1 for row in pair))} for family, pair in families.items()])
            summary["constant_candidate_both_correct"] = 0
            summary["independent_random_both_correct_chance"] = .25
            summary["limits"] = "synthetic lexical families share templates; not expert-validated; no unseen-template generalization claim"
        results[name] = summary
        evidence[str(path.relative_to(ROOT))] = sha(path)
    qa_path = RAW / "full/jsquad.json"
    qa = read(qa_path)
    if len(qa["rows"]) != 100: raise ValueError("JSQuAD subset incomplete")
    qa_valid = [row for row in qa["rows"] if not row["excluded"]]
    results["jsquad"] = {**qa["summary"], "normalized_em": clustered_ci(qa_valid, "normalized_em"),
                         "character_f1": clustered_ci(qa_valid, "character_f1"), "source_sha256": sha(qa_path),
                         "empty_answer_em_baseline": 0.0, "scope": "fixed dev100 subset, custom character scoring; not official benchmark score"}
    for name, file in (("external_body", "external-body.json"), ("long_generation", "long-generation.json")):
        path = RAW / "full" / file
        saved = read(path)
        if not saved.get("complete", saved.get("summary", {}).get("complete", False)):
            raise ValueError(name + " incomplete")
        results[name] = {"summary": saved["summary"], "source_sha256": sha(path)}
        evidence[str(path.relative_to(ROOT))] = sha(path)
    content = read(RAW / "cpu/content-review.json")
    if len(content["rows"]) != 160: raise ValueError("Content annotation incomplete")
    results["content_diagnostic"] = {name: summary["all"] for name, summary in content["summary"].items()}
    natural_path = ROOT / "reports/phase6/japanese_base_natural_stop_annotations.json"
    natural = read(natural_path)
    if sha(ROOT / natural["source"]) != natural["source_sha256"] or len(natural["scores"]) != 9:
        raise ValueError("Natural-stop annotation source differs")
    results["natural_completion_diagnostic"] = natural["summary"]
    results["saved_v1_diagnostics"] = read(RAW / "cpu/saved-diagnostics.json")
    tests_path = RAW / "cpu/tests.xml"
    suite = ET.parse(tests_path).getroot().find("testsuite")
    if suite is None or int(suite.attrib["failures"]) or int(suite.attrib["errors"]) or int(suite.attrib["tests"]) != 21:
        raise ValueError("Related CPU contract tests not all passing")
    checks = ["original GPU source snapshots verified", "revision GPU source snapshots verified", "checkpoint identity and parameters match",
              "actual GPU finite/mask/padding validation passed", "GPU runs complete within respective budgets",
              "all 9 choice conditions have complete unique IDs", "all candidate scores finite and labels valid",
              "semantic contexts unique, 96 paired counterbalanced dev families", "JSQuAD fixed100 complete with exclusions explicit",
              "external-body and long-generation stages complete", "all160 saved fixed texts content-scored",
              "all9 original natural stops annotated", "source hashes bind raw evidence",
              "additional training0 and protected test not scored", "v1 quality criteria unchanged"]
    summary = {"version": "2.1", "model": "JMicro-10M final10B Base", "parameters": 10001152,
               "checkpoint_sha256": original["checkpoint_sha256"], "training_tokens": 10000007168,
               "tasks": results, "raw_evidence_sha256": evidence,
               "reanalysis_source_sha256": {name: sha(ROOT/name) for name in (
                   "scripts/review_japanese_base_v2.py", "scripts/evaluate_japanese_base.py", "src/jmicro/japanese_evaluation.py")},
               "gpu_seconds": {"original_pilot": read(RAW/"pilot/result.json")["gpu_seconds"],
                               "full": original["gpu_seconds"], "semantic_revision": corrected["gpu_seconds"]},
               "implementation_review": {"passed": len(checks), "checks": checks, "new_CPU_tests": 8,
                                         "related_CPU_tests": 21, "tests_xml_sha256": sha(tests_path)},
               "corrections": ["initial semantic corpus duplicated some lexical families; superseded by unique-context v2.1 only",
                               "cluster CI now resamples groups but weights point estimate by examples, not equal group means",
                               "JNLI confidence grouping uses image ID rather than complete caption-pair string",
                               "all original raw files/source snapshots retained; no GPU replay of unchanged tasks"],
               "independent_human_blind": "not performed", "external_base_reference": "not run; planned follow-up",
               "JMMLU": "deferred P3", "additional_training_tokens": 0, "protected_test_used": False,
               "v1_quality_criteria_unchanged": True, "Base_practical_quality_passed": False,
               "statistical_limits": "one training seed; prompt/family uncertainty; degenerate bootstrap CI for all0/all1 is not certainty about new inputs"}
    path = ROOT / "reports/phase6/japanese_base_v2_review.json"
    path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    boot = Path("/proc/sys/kernel/random/boot_id").read_text().strip()
    def alive(record):
        stat = Path(f"/proc/{record['pid']}/stat")
        return record["boot_id"] == boot and stat.exists() and stat.read_text().split()[21] == str(record["start_ticks"])
    jobs = {}
    for name, directory in (("pilot", RAW/"pilot"), ("full", RAW/"full"), ("semantic_revision", REVISION)):
        record = read(directory / "job.json")
        if record["status"] != "complete" or alive(record):
            raise ValueError(f"Evaluation job not completed/exited: {name}")
        jobs[name] = {key: record[key] for key in ("status", "pid", "boot_id", "start_ticks", "gpu_seconds")}
    ui = read(ROOT / "reports/local/webui/server.json")
    if ui["status"] != "running" or not alive(ui): raise ValueError("Local UI not restored")
    model_api = json.load(urllib.request.urlopen("http://127.0.0.1:7860/api/model", timeout=8))
    if model_api["checkpoint_sha256"] != original["checkpoint_sha256"] or model_api["busy"]:
        raise ValueError("Restored UI model differs or unexpectedly busy")
    completion = {"status": "complete", "checked_at": datetime.now(timezone.utc).isoformat(), "jobs": jobs,
                  "review_sha256": sha(path), "UI": {key: ui[key] for key in ("status", "pid", "boot_id", "start_ticks", "url")},
                  "UI_model": model_api, "additional_training_tokens": 0, "protected_test_used": False,
                  "stop_boundary": "evaluation/report/local commit complete; UI serving; no new training"}
    (ROOT / "reports/phase6/japanese_base_v2_completion.json").write_text(json.dumps(completion, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Review passed", len(checks), path, flush=True)
    for name in expected:
        result = results[name]
        print(name, result["count"], result["primary"]["accuracy"], flush=True)
    print("JSQuAD", results["jsquad"]["character_f1"], flush=True)


if __name__ == "__main__":
    main()
