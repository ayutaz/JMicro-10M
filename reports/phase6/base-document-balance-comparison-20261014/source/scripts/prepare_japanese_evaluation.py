"""Fetch small, revision-pinned evaluation-only corpora; never read official test."""
import argparse
import hashlib
import json
from pathlib import Path
import random
import urllib.request

REVISIONS = {
    "osekilab/JBLiMP": "87ea6d2c1b67e5305789f4815f3a06bd1ec37aa2",
    "yahoojapan/JGLUE": "6f071c09316baae89c3d083a90985b4b1cb9968c",
    "osekilab/JCoLA": "736d9eef3af04bb17e4cf59adf01325973234ff9",
}
FILES = {
    "jblimp": ("osekilab/JBLiMP", "data/validated/validated_minimal_pairs.jsonl"),
    "jcqa_dev": ("yahoojapan/JGLUE", "datasets/jcommonsenseqa-v1.3/valid-v1.3.json"),
    "jcqa_train": ("yahoojapan/JGLUE", "datasets/jcommonsenseqa-v1.3/train-v1.3.json"),
    "jnli_dev": ("yahoojapan/JGLUE", "datasets/jnli-v1.3/valid-v1.3.json"),
    "jnli_train": ("yahoojapan/JGLUE", "datasets/jnli-v1.3/train-v1.3.json"),
    "jsquad_dev": ("yahoojapan/JGLUE", "datasets/jsquad-v1.3/valid-v1.3.json"),
    "jcola_in": ("osekilab/JCoLA", "data/jcola-v1.0/in_domain_valid-v1.0.json"),
    "jcola_out": ("osekilab/JCoLA", "data/jcola-v1.0/out_of_domain_valid-v1.0.json"),
    "jcola_train": ("osekilab/JCoLA", "data/jcola-v1.0/in_domain_train-v1.0.json"),
}


def load_records(path):
    text = Path(path).read_text(encoding="utf-8")
    if text.lstrip().startswith("[") or '"data":' in text[:200]:
        return json.loads(text)
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def semantic_suite():
    """Counterbalanced context variants: the same answers are correct once each.

    Families, not variants, are the sampling/split unit. This is a synthetic
    diagnostic, not an independently validated Japanese benchmark.
    """
    names = ["太郎", "花子", "健太", "美咲", "直子", "洋介", "真理", "翔太", "明子", "悠人",
             "拓也", "恵子", "直樹", "遥", "秀樹", "彩", "和也", "陽子", "大輔", "千尋"]
    items = ["りんご", "みかん", "本", "鉛筆", "切手"]
    rows = []
    for category in ("negation", "quantity", "time", "comparison", "coreference", "causality"):
        for i in range(20):
            a, b = names[i], names[(i + 3) % len(names)]
            n, m = i + 2, i % 4 + 1
            item = items[i % 5]
            if category == "negation":
                contexts = [f"{a}は今日、{item}を買った。今日{a}が買った物について言えば、",
                            f"{a}は今日、{item}を買わなかった。今日{a}が買った物について言えば、"]
                answers = [f"{item}を買った。", f"{item}を買わなかった。"]
            elif category == "quantity":
                contexts = [f"箱に{item}が{n}個あった。{m}個を追加した。今、箱の中にある{item}は、",
                            f"箱に{item}が{n+2*m}個あった。{m}個を追加した。今、箱の中にある{item}は、"]
                answers = [f"{n+m}個だ。", f"{n+3*m}個だ。"]
            elif category == "time":
                h = 1 + i % 8
                contexts = [f"{a}は午前{h}時に出発し、ちょうど1時間後に到着した。到着した時刻は、",
                            f"{a}は午前{h+1}時に出発し、ちょうど1時間後に到着した。到着した時刻は、"]
                answers = [f"午前{h+1}時だ。", f"午前{h+2}時だ。"]
            elif category == "comparison":
                contexts = [f"{a}の身長は{b}より高い。この二人のうち身長が高いのは、",
                            f"{a}の身長は{b}より低い。この二人のうち身長が高いのは、"]
                answers = [f"{a}だ。", f"{b}だ。"]
            elif category == "coreference":
                contexts = [f"{a}は{b}に本を貸した。その本を借りた人は、",
                            f"{b}は{a}に本を貸した。その本を借りた人は、"]
                answers = [f"{b}だ。", f"{a}だ。"]
            else:
                contexts = [f"{a}は水を冷凍庫に入れて十分に冷やした。その水は、",
                            f"{a}は水をやかんに入れて十分に加熱した。その水は、"]
                answers = ["凍った。", "沸騰した。"]
            family = f"{category}-{i:02}"
            for polarity, context in enumerate(contexts):
                order = [0, 1] if i % 2 == 0 else [1, 0]
                rows.append({"id": f"{family}-{polarity}", "family": family, "category": category,
                             "split": "test" if i % 5 == 4 else "dev", "context": context + "\n",
                             "choices": [answers[j] for j in order], "label": order.index(polarity)})
    return rows


def prepare(output):
    output.mkdir(parents=True, exist_ok=True)
    sources = {}
    old = json.loads((output / "manifest.json").read_text()) if (output / "manifest.json").exists() else {"sources": {}}
    for name, (repo, file) in FILES.items():
        url = f"https://raw.githubusercontent.com/{repo}/{REVISIONS[repo]}/{file}"
        path = output / (name + ".json")
        cached = old["sources"].get(name, {})
        if path.exists() and cached.get("url") == url and hashlib.sha256(path.read_bytes()).hexdigest() == cached.get("sha256"):
            data = path.read_bytes()
        else:
            data = urllib.request.urlopen(url, timeout=45).read()
        path.write_bytes(data)
        sources[name] = {"url": url, "revision": REVISIONS[repo], "path": str(path),
                         "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data),
                         "license": "CC-BY-SA-4.0", "usage": "evaluation only; never training"}
        print(name, len(data), flush=True)
    suite = semantic_suite()
    semantic_path = Path("eval/japanese_semantics_v2_1.jsonl")
    if semantic_path.exists() and semantic_path.read_text(encoding="utf-8") != "".join(
            json.dumps(row, ensure_ascii=False) + "\n" for row in suite):
        raise ValueError("Frozen semantic suite differs; do not overwrite")
    semantic_path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in suite), encoding="utf-8")
    sources["semantics"] = {"path": str(semantic_path), "sha256": hashlib.sha256(semantic_path.read_bytes()).hexdigest(),
                            "families": 120, "dev_families": 96, "test_families": 24,
                            "variants_per_family": 2, "status": "synthetic diagnostic; expert validation not performed"}
    manifest = {"version": 2, "sources": sources, "official_test_downloaded": False,
                "contamination": "unknown; no full-corpus deduplication scan; benchmarks excluded from new training",
                "pilot_seed": 20261004, "pilot_selection": "shuffle official dev indices; first 200; no score-based selection"}
    (output / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path("/home/aihub_ubuntu/jmicro-data/evaluation-v2"))
    parser.add_argument("--semantics-only", action="store_true")
    args = parser.parse_args()
    if args.semantics_only:
        path = Path("eval/japanese_semantics_v2_1.jsonl")
        path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in semantic_suite()), encoding="utf-8")
        manifest_path = args.output / "manifest.json"
        manifest = json.loads(manifest_path.read_text())
        manifest["sources"]["semantics"] = {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "families": 120, "dev_families": 96, "test_families": 24, "variants_per_family": 2,
            "status": "synthetic diagnostic; unique contexts; expert validation not performed"}
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("Prepared unique-family semantic revision only; official downloads unchanged")
    else:
        prepare(args.output)
