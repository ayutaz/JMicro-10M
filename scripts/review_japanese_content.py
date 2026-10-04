"""Show anonymized texts and validate independently recorded Codex diagnoses."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from jmicro.japanese_evaluation import clustered_ci

OUTPUT = Path("reports/phase6/japanese-base-v2-20261004/cpu")


def finalize(annotation_path):
    packet_path = OUTPUT / "content-packet.json"
    packet = json.loads(packet_path.read_text())
    annotations = json.loads(annotation_path.read_text())
    mapping = json.loads((OUTPUT / "content-mapping.json").read_text())
    expected = {row["review_id"] for row in packet["rows"]}
    scores = {row[0]: row for row in annotations["scores"]}
    if len(scores) != len(annotations["scores"]) or set(scores) != expected:
        raise ValueError("Annotation IDs missing, duplicate or extra")
    if annotations["packet_sha256"] != hashlib.sha256(packet_path.read_bytes()).hexdigest():
        raise ValueError("Annotation packet hash differs")
    groups, reviewed = defaultdict(list), []
    for row in packet["rows"]:
        _, grammar, relevance, coherence, note = scores[row["review_id"]]
        if any(value not in (0, 1, 2) for value in (grammar, relevance, coherence)) or not note:
            raise ValueError("Invalid rubric value or empty rationale")
        source = mapping[row["review_id"]]
        record = {**row, **source, "grammar": grammar, "relevance": relevance, "coherence": coherence,
                  "rationale": note, "reviewer": "Codex; single non-independent diagnostic",
                  "completion": "no_eos_cap" if row["stop_reason"] != "stop_id" else "requires_separate_ending_review"}
        reviewed.append(record)
        groups[(source["model"], "all")].append(record)
        groups[(source["model"], row["category"])].append(record)
    summary = {}
    for (model, category), rows in groups.items():
        result = {"count": len(rows)}
        for metric in ("grammar", "relevance", "coherence"):
            result[metric + "_mean"] = sum(row[metric] for row in rows)/len(rows)
            result[metric + "_full_score"] = clustered_ci([dict(row, credit=int(row[metric] == 2)) for row in rows])
        result["all_three_full_score"] = clustered_ci([dict(row, credit=int(all(row[key] == 2 for key in ("grammar", "relevance", "coherence")))) for row in rows])
        summary.setdefault(model, {})[category] = result
    result = {"packet_sha256": annotations["packet_sha256"], "rubric": packet["rubric"], "rows": reviewed,
              "summary": summary, "independent_human_blind": "not performed", "v1_grammar_acceptance": "unmeasured; Codex scores not substituted"}
    (OUTPUT / "content-review.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({model: rows["all"] for model, rows in summary.items()}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--annotations", type=Path)
    args = parser.parse_args()
    if args.annotations:
        finalize(args.annotations)
    else:
        packet = json.loads((OUTPUT / "content-packet.json").read_text())
        for row in packet["rows"][args.start:args.start+args.count]:
            print(json.dumps({key: row[key] for key in ("review_id", "category", "prefix", "text", "stop_reason")}, ensure_ascii=False))
