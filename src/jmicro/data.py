"""Bounded, pinned data pilot. No tokenizer, training, or dataset publication."""

from collections import Counter, defaultdict
from dataclasses import dataclass
from importlib.metadata import version
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit
from urllib.request import urlopen
import argparse
import hashlib
import json
import math
import platform
import re
import unicodedata
import zipfile

from jsonschema import Draft202012Validator

from jmicro.evaluation import canonicalize_text
from jmicro.experiment import ROOT, read_json, sha256, write_json


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode("utf-8")).hexdigest()


def normalized(text):
    """Only for duplicate detection; never rewrite the learning text this way."""
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKC", text).casefold()).strip()


def japanese_ratio(text):
    chars = [c for c in text if not c.isspace()]
    return sum("\u3040" <= c <= "\u30ff" or "\u3400" <= c <= "\u9fff" for c in chars) / max(1, len(chars))


def url_key(url):
    """Group exact URLs, ignoring fragment; do not discard semantic queries."""
    p = urlsplit(url)
    return urlunsplit((p.scheme.lower(), p.netloc.lower(), p.path, p.query, ""))


def config(root=ROOT):
    c = read_json(root / "configs/data/pilot.json")
    Draft202012Validator(read_json(root / "schemas/configs/data/pilot.schema.json")).validate(c)
    if sum(c["split"].values()) != 100:
        raise ValueError("Split percentages must sum to 100")
    if c["dedup"]["bands"] * c["dedup"]["rows_per_band"] != c["dedup"]["num_perm"]:
        raise ValueError("LSH bands must cover the MinHash signature")
    for s in c["sources"]:
        if s["revision"] not in s["url"] or s["revision"] not in s["evidence_url"]:
            raise ValueError("Source and evidence URLs must pin their revision")
        if s["bucket"] == "excluded":
            raise ValueError("Excluded sources cannot be acquired for this pilot")
    return c


def download(url, path, limit, expected=None):
    part = path.with_suffix(path.suffix + ".part")
    if path.exists() and expected and sha256(path) == expected:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urlopen(url, timeout=90) as response, part.open("wb") as out:
            if int(response.headers.get("Content-Length", "0")) > limit:
                raise ValueError("Download exceeds configured capacity")
            count = 0
            while chunk := response.read(1024 * 1024):
                count += len(chunk)
                if count > limit:
                    raise ValueError("Download exceeds configured capacity")
                out.write(chunk)
        if expected and sha256(part) != expected:
            raise ValueError(f"Source checksum mismatch: {path.name}")
        part.replace(path)
    finally:
        part.unlink(missing_ok=True)


def fetch(raw, root=ROOT):
    c = config(root)
    old = read_json(raw / "acquisition.json") if (raw / "acquisition.json").exists() else {"sources": []}
    previous = {s["id"]: s for s in old["sources"]}
    sources = []
    for s in c["sources"]:
        print(f"Fetching {s['id']} @ {s['revision']}", flush=True)
        cached = previous.get(s["id"], {})
        # An archive lacking an upstream digest is reusable only against its receipt.
        expected = s["expected_sha256"] or (cached.get("sha256") if cached.get("url") == s["url"] else None)
        download(s["url"], raw / s["artifact"], s["max_download_bytes"], expected)
        download(s["evidence_url"], raw / s["evidence_artifact"], 1000000, s["evidence_sha256"])
        sources.append({"id": s["id"], "url": s["url"], "revision": s["revision"],
                        "artifact": s["artifact"], "sha256": sha256(raw / s["artifact"]),
                        "bytes": (raw / s["artifact"]).stat().st_size,
                        "evidence_artifact": s["evidence_artifact"], "evidence_sha256": s["evidence_sha256"]})
        # Write after each completed source so retries can reuse valid completed artifacts.
        write_json(raw / "acquisition.json", {"schema_version": 1, "sources": sources})
    return sources


def validate_raw(raw, c):
    receipt = read_json(raw / "acquisition.json")
    items = {x["id"]: x for x in receipt["sources"]}
    for s in c["sources"]:
        item = items[s["id"]]
        for key in ("url", "revision", "artifact", "evidence_artifact", "evidence_sha256"):
            if item[key] != s[key]:
                raise ValueError(f"Acquisition provenance mismatch: {s['id']} {key}")
        p = raw / s["artifact"]
        if sha256(p) != item["sha256"] or p.stat().st_size != item["bytes"]:
            raise ValueError("Raw artifact modified")
        if s["expected_sha256"] and item["sha256"] != s["expected_sha256"]:
            raise ValueError("Upstream raw checksum mismatch")
        if item["bytes"] > s["max_download_bytes"] or sha256(raw / s["evidence_artifact"]) != s["evidence_sha256"]:
            raise ValueError("Capacity or source evidence mismatch")
    return items


def map_dialogue(d):
    utterances = d["utterances"]
    speakers = d["interlocutors"]
    if len(set(speakers)) != 2 or not utterances:
        raise ValueError("Dialogue must have exactly two speakers and nonempty utterances")
    user = utterances[0]["interlocutor_id"]
    if user not in speakers:
        raise ValueError("Unknown first speaker")
    mapping = {s: "user" if s == user else "assistant" for s in speakers}
    messages, seen_ids = [], set()
    for u in utterances:
        if u["interlocutor_id"] not in mapping or u["utterance_id"] in seen_ids:
            raise ValueError("Unknown speaker or repeated utterance ID")
        seen_ids.add(u["utterance_id"])
        text = canonicalize_text(u["text"])
        if not text.strip():
            raise ValueError("Empty utterance")
        role = mapping[u["interlocutor_id"]]
        if messages and messages[-1]["role"] == role:
            messages[-1]["text"] += "\n" + text
            messages[-1]["utterance_ids"].append(u["utterance_id"])
        else:
            messages.append({"role": role, "text": text, "utterance_ids": [u["utterance_id"]]})
    if not any(x["role"] == "assistant" for x in messages):
        raise ValueError("No assistant messages")
    return messages, mapping


def load_records(raw, c, receipt):
    import pyarrow.parquet as pq

    records = []
    for s in c["sources"]:
        origins = []
        if s["kind"] == "web":
            pf = pq.ParquetFile(raw / s["artifact"])
            start, end = s["row_start"], s["row_start"] + s["sample_count"]
            if end > pf.metadata.num_rows:
                raise ValueError("Requested source range exceeds shard")
            row_index = 0
            for batch in pf.iter_batches(batch_size=1024):
                if row_index >= end:
                    break
                for offset, row in enumerate(batch.to_pylist()):
                    i = row_index + offset
                    if start <= i < end:
                        origins.append((str(i), row))
                row_index += batch.num_rows
        else:
            with zipfile.ZipFile(raw / s["artifact"]) as archive:
                prefix = f"real-persona-chat-{s['revision']}/real_persona_chat/dialogues/"
                paths = [p for p in archive.namelist() if p.startswith(prefix) and re.fullmatch(r"\d+\.json", p[len(prefix):])]
                if len(paths) < s["sample_count"]:
                    raise ValueError("Insufficient dialogues in pinned archive")
                paths.sort(key=lambda p: digest(f"{c['seed']}:{p}"))
                for p in paths[:s["sample_count"]]:
                    if archive.getinfo(p).file_size > 1000000:
                        raise ValueError("Unexpectedly large dialogue object")
                    origins.append((p, json.loads(archive.read(p).decode("utf-8", errors="strict"))))
        print(f"Read {s['id']}: {len(origins)} source records", flush=True)
        for locator, original in origins:
            uid = s["id"] + ":" + locator
            text, messages, mapping, reason = "", [], {}, None
            try:
                if s["kind"] == "web":
                    text = canonicalize_text(original["text"])
                    f = c["filters"]
                    if not f["web_min_chars"] <= len(text) <= f["web_max_chars"]:
                        reason = "web_length"
                    elif original.get("language") not in ("ja", "jpn") or japanese_ratio(text) < f["min_japanese_ratio"]:
                        reason = "language"
                    elif not math.isfinite(float(original["language_score"])) or original["language_score"] < f["min_language_score"]:
                        reason = "language_score"
                    elif not math.isfinite(float(original["score"])) or original["score"] < f["min_quality_score"]:
                        reason = "quality_score"
                else:
                    messages, mapping = map_dialogue(original)
                    text = "\n".join(m["text"] for m in messages)
                    if len(messages) < c["filters"]["dialogue_min_messages"]:
                        reason = "dialogue_length"
                    elif japanese_ratio(text) < c["filters"]["min_japanese_ratio"]:
                        reason = "language"
            except (ValueError, TypeError, KeyError, UnicodeError):
                reason = "invalid_record"
            metadata = {k: v for k, v in original.items() if k not in ("text", "utterances", "interlocutors")}
            # Explicit whitelist: retain source quality/evaluation only, never persona/demographics.
            if s["kind"] == "dialogue":
                metadata = {k: original[k] for k in ("dialogue_id", "evaluations") if k in original}
            r = {"doc_id": uid, "source": s["id"], "source_subset": s["subset"], "revision": s["revision"],
                 "kind": s["kind"], "license": s["license"], "bucket": s["bucket"], "source_url": s["url"],
                 "source_locator": locator, "raw_artifact_sha256": receipt[s["id"]]["sha256"],
                 "raw_row_sha256": digest(encoded(original)), "canonical_sha256": digest(text),
                 "dedup_sha256": digest(normalized(text)), "canonical_utf8_bytes": len(text.encode("utf-8")),
                 "text": text, "messages_json": encoded(messages).decode(), "speaker_mapping_json": encoded(mapping).decode(),
                 "source_metadata_json": encoded(metadata).decode(), "url": original.get("url", ""),
                 "crawl_date": original.get("date"), "quality_score": original.get("score"),
                 "japanese_ratio": japanese_ratio(text), "status": "excluded" if reason else "candidate", "reason": reason,
                 "duplicate_of": None, "cluster_id": None, "split": "excluded", "minhash": [],
                 "token_count_4k": None, "token_count_8k": None}
            records.append(r)
    return sorted(records, key=lambda r: r["doc_id"])


@dataclass
class Groups:
    parent: dict

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        self.parent[max(a, b)] = min(a, b)


def shingles(text, size):
    return {text[i:i+size].encode("utf-8") for i in range(max(0, len(text)-size+1))}


def overlap(a, b):
    return len(a & b) / max(1, len(a | b))


def evaluation_patterns(c, root):
    exact, long = set(), set()
    for filename in c["contamination"]["fixed_suites"]:
        for line in (root / filename).read_text().splitlines():
            row = json.loads(line)
            texts = [row["prefix"]] if row["suite"] == "base" else [m["content"] for m in row["messages"]]
            if row["suite"] == "chat":
                texts.append("\n".join(m["content"] for m in row["messages"]))
            # Evaluation messages use content; corpus messages use text.
            for text in texts:
                t = normalized(canonicalize_text(text))
                exact.add(t)
                if len(t) >= c["contamination"]["min_substring_chars"]:
                    long.add(t)
    return exact, long


def contaminated(record, patterns):
    exact, long = patterns
    body = normalized(record["text"])
    return body in exact or any(p in body for p in long)


def cluster_records(records, c, patterns):
    from datasketch import MinHash, MinHashLSH

    active = [r for r in records if r["status"] == "candidate"]
    ids = {r["doc_id"]: r for r in active}
    clusters, duplicates = Groups({k: k for k in ids}), Groups({k: k for k in ids})
    exact, urls, prefixes = {}, {}, {}
    d = c["dedup"]
    lsh = MinHashLSH(num_perm=d["num_perm"], params=(d["bands"], d["rows_per_band"]))
    counts = Counter({k: 0 for k in ("normalized_exact_links", "cross_source_exact_links", "same_url_links",
                                   "shared_dialogue_prefix_links", "lsh_candidate_pairs", "verified_near_links",
                                   "cross_source_near_links", "contaminated_clusters")})
    near_pairs = []
    for i, r in enumerate(active):
        uid, t = r["doc_id"], normalized(r["text"])
        old = exact.setdefault(r["dedup_sha256"], uid)
        if old != uid:
            clusters.union(uid, old)
            duplicates.union(uid, old)
            counts["normalized_exact_links"] += 1
            if ids[old]["source"] != r["source"]:
                counts["cross_source_exact_links"] += 1
        if r["url"]:
            key = url_key(r["url"])
            old = urls.setdefault(key, uid)
            if old != uid:
                clusters.union(uid, old)
                counts["same_url_links"] += 1
        if r["kind"] == "dialogue":
            m = json.loads(r["messages_json"])
            prefix = normalized("\n".join(x["text"] for x in m[:d["shared_prefix_messages"]]))
            if len(prefix) >= d["shared_prefix_min_chars"]:
                old = prefixes.setdefault(prefix, uid)
                if old != uid:
                    clusters.union(uid, old)
                    counts["shared_dialogue_prefix_links"] += 1
        if len(t) >= d["near_min_chars"]:
            f = shingles(t, d["char_ngram"])
            mh = MinHash(num_perm=d["num_perm"], seed=c["seed"])
            mh.update_batch(sorted(f))
            r["minhash"] = [int(x) for x in mh.hashvalues]
            for other in sorted(lsh.query(mh)):
                counts["lsh_candidate_pairs"] += 1
                similarity = overlap(f, shingles(normalized(ids[other]["text"]), d["char_ngram"]))
                if similarity >= d["jaccard_threshold"]:
                    clusters.union(uid, other)
                    duplicates.union(uid, other)
                    counts["verified_near_links"] += 1
                    if ids[other]["source"] != r["source"]:
                        counts["cross_source_near_links"] += 1
                    if len(near_pairs) < 100:
                        near_pairs.append({"left": other, "right": uid, "jaccard": similarity})
            lsh.insert(uid, mh)
        if i % 2000 == 0:
            print(f"Clustered {i}/{len(active)}", flush=True)
    contaminated_clusters = {clusters.find(r["doc_id"]) for r in active if contaminated(r, patterns)}
    counts["contaminated_clusters"] = len(contaminated_clusters)
    for r in records:
        uid = r["doc_id"]
        r["cluster_id"] = digest(clusters.find(uid) if uid in ids else uid)
        if uid not in ids:
            continue
        cluster_root = clusters.find(uid)
        if cluster_root in contaminated_clusters:
            r.update(status="excluded", reason="evaluation_contamination")
            continue
        rep = duplicates.find(uid)
        if rep != uid:
            r.update(status="duplicate", reason="normalized_exact_or_verified_near", duplicate_of=rep)
            continue
        n = int(digest(f"{c['seed']}:{r['cluster_id']}")[:16], 16) % 100
        split = "train" if n < c["split"]["train"] else "dev" if n < c["split"]["train"] + c["split"]["dev"] else "test"
        r.update(status="kept", reason=None, split=split)
    return {"counts": dict(counts), "near_pair_examples": near_pairs}


def distribution(values):
    v = sorted(values)
    return {"count": len(v), "min": min(v) if v else None, "mean": sum(v)/len(v) if v else None,
            "p50": v[math.ceil(len(v)*0.5)-1] if v else None,
            "p95": v[math.ceil(len(v)*0.95)-1] if v else None, "max": max(v) if v else None}


def summarize(records):
    return {"documents": len(records), "unique_canonical_utf8_bytes": sum(r["canonical_utf8_bytes"] for r in records),
            "characters": distribution([len(r["text"]) for r in records]),
            "short_at_most_280_chars": sum(len(r["text"]) <= 280 for r in records)}


def write_lines(path, rows):
    with path.open("wb") as f:
        for r in rows:
            f.write(encoded(r) + b"\n")


def tokenizer_sample(records, c):
    chosen, bytes_by_bucket = [], {}
    for bucket, budget in c["tokenizer_sample_bytes"].items():
        candidates = sorted((r for r in records if r["status"] == "kept" and r["split"] == "train" and r["bucket"] == bucket),
                            key=lambda r: digest(f"{c['seed']}:tokenizer:{r['doc_id']}"))
        used = 0
        for r in candidates:
            if used + r["canonical_utf8_bytes"] > budget:
                continue
            used += r["canonical_utf8_bytes"]
            chosen.append({k: r[k] for k in ("doc_id", "bucket", "text", "canonical_sha256", "split")})
        bytes_by_bucket[bucket] = used
    chosen.sort(key=lambda r: digest(f"{c['seed']}:tokenizer-order:{r['doc_id']}"))
    return chosen, bytes_by_bucket


def manifest_schema():
    import pyarrow as pa

    strings = ("doc_id source source_subset revision kind license bucket source_url source_locator raw_artifact_sha256 "
               "raw_row_sha256 canonical_sha256 dedup_sha256 text messages_json speaker_mapping_json source_metadata_json "
               "url crawl_date status reason duplicate_of cluster_id split").split()
    return pa.schema([(k, pa.string()) for k in strings] + [("canonical_utf8_bytes", pa.int64()),
                     ("quality_score", pa.float64()), ("japanese_ratio", pa.float64()),
                     ("minhash", pa.list_(pa.uint64())), ("token_count_4k", pa.int64()), ("token_count_8k", pa.int64())])


def audit_near(records, c):
    """Recompute signatures and independently check retained LSH candidates."""
    from datasketch import MinHash, MinHashLSH

    d = c["dedup"]
    lsh = MinHashLSH(num_perm=d["num_perm"], params=(d["bands"], d["rows_per_band"]))
    indexed = {}
    candidates = 0
    for i, r in enumerate(records):
        t = normalized(r["text"])
        if len(t) < d["near_min_chars"]:
            if r["minhash"]:
                raise ValueError("Unexpected signature on a skipped short document")
            continue
        f = shingles(t, d["char_ngram"])
        mh = MinHash(num_perm=d["num_perm"], seed=c["seed"])
        mh.update_batch(sorted(f))
        if [int(x) for x in mh.hashvalues] != r["minhash"]:
            raise ValueError("MinHash signature does not match canonical content")
        for other in lsh.query(mh):
            candidates += 1
            if overlap(f, shingles(normalized(indexed[other]["text"]), d["char_ngram"])) >= d["jaccard_threshold"]:
                raise ValueError("Verified near duplicate remains in retained corpus")
        indexed[r["doc_id"]] = r
        lsh.insert(r["doc_id"], mh)
        if i % 2000 == 0:
            print(f"Audited near signatures {i}/{len(records)}", flush=True)
    return {"recomputed_signatures": len(indexed), "candidate_pairs_checked": candidates, "retained_verified_near_pairs": 0}


def build(raw, output, root=ROOT):
    import pyarrow as pa
    import pyarrow.parquet as pq

    c = config(root)
    receipt = validate_raw(raw, c)
    records = load_records(raw, c, receipt)
    dedup = cluster_records(records, c, evaluation_patterns(c, root))
    output.mkdir(parents=True, exist_ok=True)
    pq.write_table(pa.Table.from_pylist(records, schema=manifest_schema()), output / "dataset_manifest.parquet", compression="zstd")
    kept = [r for r in records if r["status"] == "kept"]
    payloads = [{k: r[k] for k in ("doc_id", "kind", "bucket", "split", "text", "messages_json", "speaker_mapping_json", "canonical_sha256")} for r in kept]
    write_lines(output / "corpus.jsonl", payloads)
    sample, sample_bytes = tokenizer_sample(records, c)
    write_lines(output / "tokenizer_sample.jsonl", sample)
    splits = {s: [r["doc_id"] for r in kept if r["split"] == s] for s in c["split"]}
    inputs = {"config_sha256": sha256(root / "configs/data/pilot.json"), "pipeline_sha256": sha256(Path(__file__)),
              "canonicalization_sha256": sha256(root / "src/jmicro/evaluation.py"),
              "dependency_lock_sha256": sha256(root / "uv.lock"),
              "fixed_suite_sha256": {p: sha256(root / p) for p in c["contamination"]["fixed_suites"]},
              "raw": list(receipt.values())}
    write_json(output / "split_manifest.json", {"schema_version": 1, "seed": c["seed"], "inputs": inputs,
               "split_unit": "URL / exact / verified-near / long shared-dialogue-prefix connected components, before windowing",
               "splits": splits, "cluster_by_doc": {r["doc_id"]: r["cluster_id"] for r in kept},
               "dataset_manifest_sha256": sha256(output / "dataset_manifest.parquet"),
               "corpus_sha256": sha256(output / "corpus.jsonl"), "tokenizer_sample_sha256": sha256(output / "tokenizer_sample.jsonl"),
               "tokenizer_sample": {"documents": len(sample), "bytes_by_bucket": sample_bytes,
                                    "same_input_required_for_vocab_sizes": [4096, 8192], "train_only": True}})
    web = [r for r in kept if r["kind"] == "web"]
    domains = defaultdict(lambda: {"documents": 0, "bytes": 0})
    for r in web:
        item = domains[urlsplit(r["url"]).netloc.lower()]
        item["documents"] += 1
        item["bytes"] += r["canonical_utf8_bytes"]
    limitations = ["MinHash LSH is probabilistic candidate retrieval; exact Jaccard is checked only for returned pairs.",
                   "Character-5-gram matching does not detect semantic paraphrases; near checks skip strings shorter than 64 normalized characters.",
                   "Fixed-evaluation check excludes exact complete bodies and substrings >=24 normalized characters, propagating exclusion across clusters; short common phrases alone do not establish leakage.",
                   "The contiguous first-shard Web sample is not representative of the entire source or the later master corpus.",
                   "Corpus tokens, teacher tokens and context-1024 ratios remain unmeasured until Phase 2.",
                   "Dialogue split is conversation/duplicate-cluster based, not speaker-disjoint; omitted personas do not prove absence of personal information in public utterances."]
    write_json(output / "data_pilot_report.json", {"schema_version": 1, "phase": 1, "inputs": inputs,
               "environment": {"python": platform.python_version(), "platform": platform.platform(),
                               "packages": {p: version(p) for p in ("pyarrow", "datasketch", "numpy", "scipy", "jsonschema", "fsspec", "aiohttp")}},
               "raw_documents": len(records), "status_counts": dict(Counter(r["status"] for r in records)),
               "exclusion_reasons": dict(Counter(r["reason"] for r in records if r["status"] == "excluded")),
               "kept": summarize(kept), "web": summarize(web), "domains": dict(sorted(domains.items())),
               "by_source": {s["id"]: summarize([r for r in kept if r["source"] == s["id"]]) for s in c["sources"]},
               "by_bucket": {b: summarize([r for r in kept if r["bucket"] == b]) for b in sorted({r["bucket"] for r in kept})},
               "by_split": {s: summarize([r for r in kept if r["split"] == s]) for s in splits},
               "dedup": dedup, "limitations": limitations, "quality_review": "quality_review.json required before completion"})
    dialogues = [r for r in kept if r["kind"] == "dialogue"]
    message_sets = [json.loads(r["messages_json"]) for r in dialogues]
    assistants = [m["text"] for messages in message_sets for m in messages if m["role"] == "assistant"]
    response_counts = Counter(assistants)
    write_json(output / "dialogue_data_report.json", {"schema_version": 1, "phase": 1, "dialogues": len(dialogues),
               "unique_canonical_utf8_bytes": sum(r["canonical_utf8_bytes"] for r in dialogues),
               "messages": distribution([len(m) for m in message_sets]),
               "user_turns": distribution([sum(x["role"] == "user" for x in m) for m in message_sets]),
               "assistant_responses": distribution([sum(x["role"] == "assistant" for x in m) for m in message_sets]),
               "assistant_response_characters": distribution([len(t) for t in assistants]),
               "empty_assistant_responses": sum(not t.strip() for t in assistants),
               "last_message_roles": dict(Counter(m[-1]["role"] for m in message_sets)),
               "repeated_assistant_text": [{"text_sha256": digest(t), "count": n} for t, n in response_counts.most_common(20)],
               "split_counts": dict(Counter(r["split"] for r in dialogues)), "role_policy": c["dialogue_policy"],
               "tree_reconstruction": "not applicable: selected source contains linear two-speaker conversations",
               "token_counts_4k": None, "token_counts_8k": None, "assistant_teacher_tokens": None,
               "context_1024_fit_ratio": None, "limitations": limitations[-2:]})
    return {"raw": len(records), "kept": len(kept), "web": len(web), "dialogues": len(dialogues), "sample": len(sample)}


def verify(raw, output, root=ROOT, require_review=True):
    import pyarrow.parquet as pq

    c = config(root)
    validate_raw(raw, c)
    manifest = read_json(output / "split_manifest.json")
    inputs = manifest["inputs"]
    for filename, key in (("configs/data/pilot.json", "config_sha256"), ("src/jmicro/evaluation.py", "canonicalization_sha256"), ("uv.lock", "dependency_lock_sha256")):
        if sha256(root / filename) != inputs[key]:
            raise ValueError("Processing input modified")
    if sha256(Path(__file__)) != inputs["pipeline_sha256"]:
        raise ValueError("Pipeline changed; rebuild required")
    for path, checksum in inputs["fixed_suite_sha256"].items():
        if sha256(root / path) != checksum:
            raise ValueError("Evaluation input modified")
    for filename, key in (("dataset_manifest.parquet", "dataset_manifest_sha256"), ("corpus.jsonl", "corpus_sha256"), ("tokenizer_sample.jsonl", "tokenizer_sample_sha256")):
        if sha256(output / filename) != manifest[key]:
            raise ValueError(f"Output modified: {filename}")
    records = pq.read_table(output / "dataset_manifest.parquet").to_pylist()
    kept = {r["doc_id"]: r for r in records if r["status"] == "kept"}
    row_validator = Draft202012Validator(read_json(root / "schemas/dataset_record.schema.json"))
    for r in records:
        row_validator.validate(r)
    # Independently re-read actual source rows and reconstruct canonical payloads.
    source_records = load_records(raw, c, validate_raw(raw, c))
    source_index = {r["doc_id"]: r for r in source_records}
    if len(records) != len(source_index) or len({r["doc_id"] for r in records}) != len(records):
        raise ValueError("Manifest/source coverage mismatch")
    for r in records:
        original = source_index[r["doc_id"]]
        for k in ("source", "revision", "license", "bucket", "source_locator", "raw_artifact_sha256", "raw_row_sha256",
                  "canonical_sha256", "dedup_sha256", "canonical_utf8_bytes", "text", "messages_json", "speaker_mapping_json", "source_metadata_json"):
            if r[k] != original[k]:
                raise ValueError(f"Source reconstruction mismatch: {r['doc_id']} {k}")
        if r["status"] == "duplicate" and r["duplicate_of"] not in kept:
            raise ValueError("Duplicate representative not kept")
        if r["status"] != "kept" and r["split"] != "excluded":
            raise ValueError("Rejected data must not have a training/evaluation split")
        if r["status"] == "kept" and original["status"] != "candidate":
            raise ValueError("Retained record failed the original source filters")
    cluster_splits, hashes, urls, prefixes = {}, set(), {}, {}
    patterns = evaluation_patterns(c, root)
    for r in kept.values():
        if cluster_splits.setdefault(r["cluster_id"], r["split"]) != r["split"]:
            raise ValueError("Cluster crosses splits")
        if r["dedup_sha256"] in hashes or contaminated(r, patterns):
            raise ValueError("Exact duplicate or evaluation contamination remains")
        hashes.add(r["dedup_sha256"])
        if r["url"] and urls.setdefault(url_key(r["url"]), r["split"]) != r["split"]:
            raise ValueError("URL crosses splits")
        if r["kind"] == "dialogue":
            messages = json.loads(r["messages_json"])
            if [x["role"] for x in messages] != ["user" if i % 2 == 0 else "assistant" for i in range(len(messages))]:
                raise ValueError("Role alternation broken")
            prefix = normalized("\n".join(m["text"] for m in messages[:c["dedup"]["shared_prefix_messages"]]))
            if len(prefix) >= c["dedup"]["shared_prefix_min_chars"] and prefixes.setdefault(prefix, r["split"]) != r["split"]:
                raise ValueError("Shared dialogue prefix crosses splits")
    for s, ids in manifest["splits"].items():
        if ids != [uid for uid, r in kept.items() if r["split"] == s]:
            raise ValueError("Split membership mismatch")
    if manifest["cluster_by_doc"] != {uid: r["cluster_id"] for uid, r in kept.items()}:
        raise ValueError("Cluster manifest mismatch")
    near_audit = audit_near(list(kept.values()), c)
    payloads = [json.loads(line) for line in (output / "corpus.jsonl").read_text().splitlines()]
    payload_keys = ("doc_id", "kind", "bucket", "split", "text", "messages_json", "speaker_mapping_json", "canonical_sha256")
    if payloads != [{k: r[k] for k in payload_keys} for r in kept.values()]:
        raise ValueError("Corpus payload, membership, or ordering mismatch")
    sample = [json.loads(line) for line in (output / "tokenizer_sample.jsonl").read_text().splitlines()]
    expected_sample, expected_bytes = tokenizer_sample(records, c)
    if sample != expected_sample or manifest["tokenizer_sample"]["bytes_by_bucket"] != expected_bytes:
        raise ValueError("Tokenizer sample changed or contains held-out data")
    report = read_json(output / "data_pilot_report.json")
    dialogue_report = read_json(output / "dialogue_data_report.json")
    if report["raw_documents"] != len(records) or report["kept"] != summarize(list(kept.values())) or report["inputs"] != inputs:
        raise ValueError("Pilot report count mismatch")
    if not 1000 <= dialogue_report["dialogues"] <= 10000 or dialogue_report["dialogues"] != sum(r["kind"] == "dialogue" for r in kept.values()):
        raise ValueError("Dialogue pilot does not meet 1k-10k requirement")
    review_count = 0
    if require_review:
        review = read_json(output / "quality_review.json")
        if review["reviewer_type"] != "assistant_manual_content_review":
            raise ValueError("Do not claim an independent human quality review")
        counts = Counter()
        for item in review["samples"]:
            r = kept[item["doc_id"]]
            if item["canonical_sha256"] != r["canonical_sha256"] or not item["notes"].strip():
                raise ValueError("Quality review evidence mismatch")
            counts[r["kind"]] += 1
        if any(counts[k] < 10 for k in ("web", "dialogue")):
            raise ValueError("Inspect at least ten distinct examples from each source kind")
        if len({x["doc_id"] for x in review["samples"]}) != len(review["samples"]):
            raise ValueError("Repeated quality review example")
        review_count = len(review["samples"])
    result = {"schema_version": 1, "phase": 1, "verified": True, "raw_records_reconstructed": len(records),
              "kept_records": len(kept), "dialogues": dialogue_report["dialogues"], "tokenizer_sample_documents": len(sample),
              "split_counts": {s: len(ids) for s, ids in manifest["splits"].items()}, "quality_review_samples": review_count,
              "completion_scope": "full_phase1_verification" if require_review else "preliminary_without_content_review",
              "checks": ["pinned_raw_and_license_checksums", "record_schema", "source_reconstruction", "canonical_payload_hashes",
                         "cluster_url_prefix_split_disjoint", "normalized_exact_unique", "fixed_eval_detected_contamination_absent",
                         "corpus_payload_parity", "tokenizer_train_only_deterministic", "pilot_counts", "retained_near_candidates_absent"],
              "near_audit": near_audit,
              "near_dedup_scope": "LSH candidate recall is probabilistic; build-repeat validation is additionally required",
              "tokenizer_training_done": False, "gpu_verified": False}
    write_json(output / "verification.json", result)
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=("fetch", "build", "verify"))
    p.add_argument("--raw", type=Path, default=ROOT / "data/phase1/raw")
    p.add_argument("--output", type=Path, default=ROOT / "data/phase1/processed")
    p.add_argument("--without-review", action="store_true", help="preliminary verification only")
    args = p.parse_args()
    result = fetch(args.raw) if args.action == "fetch" else build(args.raw, args.output) if args.action == "build" else verify(args.raw, args.output, require_review=not args.without_review)
    print(json.dumps(result, ensure_ascii=False))
