"""CPU-only v2 diagnostics from immutable saved v1 outputs, no GPU replay."""
from collections import defaultdict
import hashlib
import json
import math
from pathlib import Path
import random
import sys

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from jmicro.japanese_evaluation import clustered_ci, repetition_metrics
from jmicro.phase5 import bootstrap_bpb


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "reports/phase6/japanese-base-v2-20261004/cpu"


def read(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def save(name, data):
    path = OUTPUT / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def summarize_generation(outputs):
    groups = defaultdict(list)
    for row in outputs:
        condition = f"{row['decoding']}-suppressed{int(row['suppressed'])}-seed{row['seed']}"
        metrics = repetition_metrics(row)
        for key in ((condition, "all"), (condition, row["category"])):
            groups[key].append({"id": row["id"], **metrics})
    summary = {}
    for (condition, category), rows in groups.items():
        summary.setdefault(condition, {})[category] = {
            "count": len(rows), "natural_eos": sum(row["natural_eos"] for row in rows),
            "mean_characters": float(np.mean([row["characters"] for row in rows])),
            "mean_tokens": float(np.mean([row["tokens"] for row in rows])),
            "char4_repeat": clustered_ci(rows, "char_4gram_repeat"),
            "token4_repeat": clustered_ci(rows, "token_4gram_repeat"),
            "same_sentence_reappears": sum(row["same_sentence_reappears"] for row in rows),
            "raw_utf8_failure": sum(row["raw_utf8_failure"] for row in rows),
            "role_ids_4_5_6": sum(row["role_ids_4_5_6"] for row in rows),
            "base_eot_id_7": sum(row["base_eot_id_7"] for row in rows),
            "literal_replacement_character": sum(row["literal_replacement_character"] is True for row in rows)}
    return summary


def length_strata(body):
    groups = defaultdict(list)
    for row in body["rows"]:
        n = row["body_tokens"]
        label = "1-63" if n < 64 else "64-255" if n < 256 else "256-1023" if n < 1024 else "1024+"
        groups[label].append(row)
    return {key: {"documents": len(rows), "body_bytes": sum(row["body_bytes"] for row in rows),
                  "body_tokens": sum(row["body_tokens"] for row in rows),
                  "bpb": sum(row["body_nll"] for row in rows)/(math.log(2)*sum(row["body_bytes"] for row in rows))}
            for key, rows in groups.items()}


def main():
    current_body = "reports/phase6/base-10b-comparison-20261004/full-dev.json"
    current_gen = "reports/phase6/base-10b-comparison-20261004/generation.json"
    web = "reports/phase6/eos-5b-finish-100m-20261004/web-full-evaluation.json"
    base5 = "reports/phase6/base-5b-comparison-20261004/full-dev.json"
    sources = {path: hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in (current_body, current_gen, web, base5)}
    bodies = {"base10B": read(current_body)["body"], "web5_1B": read(web)["body"], "base5B": read(base5)["body"]}
    outputs = {"base10B": read(current_gen)["generation"]["outputs"], "web5_1B": read(web)["generation"]["outputs"]}
    diagnostics = {"source_sha256": sources, "additional_training_tokens": 0, "GPU_replay": False,
                   "generation": {name: summarize_generation(rows) for name, rows in outputs.items()},
                   "length_strata": {name: length_strata(body) for name, body in bodies.items()},
                   "paired_bpb": {name: bootstrap_bpb(bodies["base10B"], bodies[name]) for name in ("base5B", "web5_1B")},
                   "statistical_limits": "document/prompt bootstrap; single training seed; sample uncertainty only"}
    save("saved-diagnostics.json", diagnostics)
    packet, mapping = [], {}
    for model, rows in outputs.items():
        for row in rows:
            if row["decoding"] == "greedy" and row["suppressed"]:
                packet.append({"id": row["id"], "category": row["category"], "prefix": row["prefix"],
                               "text": row["text"], "generated_ids": row["generated_ids"],
                               "stop_reason": row["stop_reason"], "source_model": model})
    random.Random(20261004).shuffle(packet)
    for index, row in enumerate(packet):
        review_id = f"review-{index+1:03}"
        mapping[review_id] = {"model": row.pop("source_model"), "id": row["id"]}
        row["review_id"] = review_id
    rubric = {"values": [0, 1, 2], "grammar": "0 unreadable/broken; 1 partially grammatical; 2 fluent local syntax, including an unfinished cap ending",
              "relevance": "0 unrelated/contradicts prefix; 1 connected initially then drifts; 2 maintains prefix facts/topic",
              "coherence": "0 contradictory/incomprehensible/loop; 1 partial sensible sequence with degradation; 2 meaningful consistent development",
              "natural_completion": "appropriate, premature, off_topic, no_eos_cap; semantic completion separate from raw stop",
              "reviewer": "Codex diagnostic; not independent human blind annotation",
              "independent_human": "not performed; original 70% human grammar criterion remains unmeasured"}
    save("content-packet.json", {"shuffle_seed": 20261004, "rubric": rubric, "rows": packet})
    save("content-mapping.json", mapping)
    print("Saved", OUTPUT, "packet", len(packet), flush=True)
    print(json.dumps(diagnostics["paired_bpb"], indent=2), flush=True)


if __name__ == "__main__":
    main()
