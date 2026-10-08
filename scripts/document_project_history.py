"""Document saved evidence without training, rerating, or opening corpora/weights.

Run through pinned uv. The inventory covers every tracked source file at the
captured Git revision; detailed extraction covers report metadata, with explicit
size/snapshot exclusions. Native reports are inventoried by metadata only.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET


LIMIT = 2 * 1024 * 1024
METRIC = re.compile(
    r"status|decision|scope|conclusion|interpret|reason|note|limit|hypothes|"
    r"bpb|nll|loss|accuracy|correct|grammar|coher|relev|appropriate|completion|"
    r"eos|repetition|unicode|role_leak|empty|token|teacher|byte|update|step|"
    r"gpu|cpu|second|budget|cap|pass|fail|accept|eligible|closed|adopt|"
    r"seed|check|test|skip|document|pair|sample|prepared|source_accepted|"
    r"scientific|verification|physical|base_complete|training_started",
    re.I,
)
SECRET = re.compile(r"password|access_token|api_key|authorization|credential", re.I)
CATEGORIES = [
    ("01_foundations", "基盤・Tokenizer・保存再開", r"^reports/phase[0-5]/|tokenizer|resume|handoff|export|performance|throughput"),
    ("02_material", "教材・供給・品質・量", r"source|supply|corpus|material|dataset|textbook|quantity|selector|preparation|feasibility|hq_|content_accept|livedoor|wikipedia|aozora|tatoeba|tanaka|sarashina"),
    ("03_learning", "学習量・配合・学習順序", r"base_[125]0?b|amount_learning|story\d|mixture|curriculum|learning|coverage|source_order|historical_parent|mature_base"),
    ("04_objectives", "学習目的・最適化・正則化", r"objective|unlikelihood|contrast|teacher|decay|ademamix|muon|smoothing|confidence|kl_|anchor|gradient|precision|weight_average|parameter_displacement"),
    ("05_architecture", "構成・反復計算・容量", r"architecture|residual|shared|recurrent|context_mixing|headwise|kv_|relu|attention|readout|embedding|capacity|initialization|gated"),
    ("06_evaluation", "評価・生成・意味診断", r"evaluation|japanese|diagnostic|generalization|repetition|semantic|condition|packing|decode|failure_route|intervention_gap"),
    ("07_operations", "実行管理・後続準備・その他", r".*"),
]


def run_git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(
        ["git", "-c", f"safe.directory={root}", "-C", str(root), *args]
    )


def scalar_fields(value, prefix=""):
    """Keep original key paths and scalar values; arrays of outputs stay in source."""
    fields = {}
    if not isinstance(value, dict):
        return fields
    for key, item in value.items():
        path = f"{prefix}.{key}" if prefix else key
        if SECRET.search(key):
            continue
        if isinstance(item, dict):
            fields.update(scalar_fields(item, path))
        elif METRIC.search(path) and (
            item is None or isinstance(item, (str, int, float, bool))
            or isinstance(item, list) and len(item) <= 8
            and all(x is None or isinstance(x, (str, int, float, bool)) for x in item)
        ):
            fields[path] = item
    return fields


def category(path):
    for slug, title, pattern in CATEGORIES:
        if re.search(pattern, path, re.I):
            return slug, title
    raise AssertionError(path)


def escaped(value):
    return html.escape(str(value), quote=False).replace("|", "／").replace("\n", " ").replace("\r", " ")


def link(path):
    return f"[原記録](../../{path})"


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def render_groups(out, records):
    groups = defaultdict(list)
    for row in records:
        groups[row["category"]].append(row)
    for slug, title, _ in CATEGORIES:
        pages, blocks, size = [], [], 0
        for row in groups[slug]:
            header = ["<details>", f"<summary>{escaped(row['path'])} — {escaped(row['status'])}</summary>", "",
                     f"{link(row['path'])} ／ SHA256: `{row['sha256']}` ／ {row['bytes']:,} bytes", "",
                     "| 原キー | 保存値 |", "|---|---|"]
            field_chunks, rows, field_size = [], [], 0
            for key, item in row["original_key_fields"].items():
                line = f"| {escaped(key)} | {escaped(json.dumps(item, ensure_ascii=False))} |"
                if rows and field_size + len(line.encode('utf-8')) > 140000:
                    field_chunks.append(rows)
                    rows, field_size = [], 0
                rows.append(line)
                field_size += len(line.encode('utf-8'))
            field_chunks.append(rows)
            for fields in field_chunks:
                block = "\n".join(header + fields + ["", "</details>", ""])
                if blocks and size + len(block.encode('utf-8')) > 180000:
                    pages.append(blocks)
                    blocks, size = [], 0
                blocks.append(block)
                size += len(block.encode('utf-8'))
        if blocks:
            pages.append(blocks)
        index = [f"# {title}の保存記録", "", f"{len(groups[slug])} JSON記録を{len(pages)}ページに分割。件数は独立実験数ではない。分類はファイル名による検索補助。", "",
                 "原status・キー・値を転記し、採否や因果を再判定していない。生成文・個別採点の配列は原記録を参照。過去のnext_actionは現在の開始指示ではない。", ""]
        for number, chunks in enumerate(pages, 1):
            filename = f"{slug}_{number:03d}.md"
            page = f"# {title} — {number}/{len(pages)}\n\n[分野一覧へ]({slug}.md) ／ [台帳入口](README.md)\n\n" + "\n".join(chunks)
            (out / filename).write_text(page, encoding='utf-8')
            first = re.search(r"<summary>(.*?) —", chunks[0]).group(1)
            last = re.search(r"<summary>(.*?) —", chunks[-1]).group(1)
            index.append(f"- [ページ{number:03d}]({filename}): {first} ～ {last}")
        (out / f"{slug}.md").write_text("\n".join(index) + "\n", encoding='utf-8')
    terminal = [r for r in records if re.search(r'^reports/phase[0-9]/[^/]+(?:completion|complete|judgment|synthesis|comparison_review)\.json$', r['path'])]
    lines = ["# 完了・採否・総合判断の入口", "", "ファイル名で抽出した原記録一覧。statusがcompleteでもBase完成や品質合格を意味しない。重複run・比較・診断を独立件数に足さない。", "",
             "| 原報告 | 保存status |", "|---|---|"]
    lines.extend(f"| [{r['path']}](../../{r['path']}) | {escaped(r['status'])} |" for r in terminal)
    (out/'decisions.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    return groups


def main():
    if sys.version_info[:3] != (3, 12, 7):
        raise RuntimeError("Run with uv Python3.12.7; no interpreter fallback")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, required=True)
    parser.add_argument("--native-reports", type=Path)
    parser.add_argument("--output", type=Path, default=Path("docs/retrospective"), help="New snapshot directory inside repository docs")
    parser.add_argument("--render-existing", action="store_true", help="Paginate the saved extraction without rescanning original evidence")
    args = parser.parse_args()
    root = args.repository.resolve()
    out = (root / args.output).resolve()
    if out.parent != root/'docs':
        raise ValueError('Snapshot output must be a direct child directory of repository docs')
    out.mkdir(parents=True, exist_ok=True)
    if args.render_existing:
        records = json.loads((out/'experiment_records.json').read_text(encoding='utf-8'))
        render_groups(out, records)
        print(json.dumps(dict(rendered_saved_records=len(records),new_experiments=0)))
        return
    if (out / "coverage.json").exists():
        raise ValueError("Preserve this evidence snapshot; use a dated successor")
    commit = run_git(root, "rev-parse", "HEAD").decode().strip()
    timestamp = datetime.now(timezone.utc).isoformat()
    staged = run_git(root, "ls-files", "--stage", "-z").decode().split("\0")
    files = []
    for entry in staged:
        if not entry:
            continue
        metadata, name = entry.split("\t", 1)
        mode, blob, stage = metadata.split()
        if stage != "0":
            raise ValueError("Resolve merge conflicts before documenting")
        path = root / name
        files.append(dict(path=name, git_blob_sha1=blob, bytes=path.stat().st_size,
                          git_mode=mode))
    inventory = "path\tbytes\tgit_blob_sha1\tgit_mode\n" + "".join(
        f"{r['path']}\t{r['bytes']}\t{r['git_blob_sha1']}\t{r['git_mode']}\n" for r in files)
    (out / "tracked_files.tsv").write_text(inventory, encoding="utf-8")
    records, exclusions, xml_rows, documents = [], [], [], []
    for row in files:
        name, size = row["path"], row["bytes"]
        path = root / name
        if name.startswith("docs/") and name.endswith(".md"):
            with path.open(encoding="utf-8-sig") as stream:
                first = stream.readline().strip().lstrip("# ")
            documents.append((name, first, size))
        if name.startswith("reports/") and name.endswith(".xml"):
            try:
                node = ET.parse(path).getroot()
                suites = list(node) if node.tag == "testsuites" else [node]
                for suite in suites:
                    xml_rows.append(dict(path=name, attributes=dict(suite.attrib),
                        observed_testcases=len(suite.findall(".//testcase")),
                        failure_nodes=len(suite.findall(".//failure")),
                        error_nodes=len(suite.findall(".//error")),
                        skipped_nodes=len(suite.findall(".//skipped"))))
            except ET.ParseError as exc:
                exclusions.append(dict(path=name, reason="XML parse error", detail=str(exc)))
        if not name.startswith("reports/") or not name.endswith(".json"):
            continue
        if any(p in name.split("/") for p in ("source", "snapshot", "snapshots")):
            exclusions.append(dict(path=name, reason="Historical source snapshot; listed in full inventory"))
            continue
        if size > LIMIT:
            exclusions.append(dict(path=name, bytes=size, reason="Over2MiB; original retained, not parsed"))
            continue
        try:
            payload = path.read_bytes()
            value = json.loads(payload)
        except (ValueError, UnicodeError) as exc:
            exclusions.append(dict(path=name, reason="JSON parse error", detail=str(exc)))
            continue
        if not isinstance(value, dict):
            exclusions.append(dict(path=name, reason="Non-object JSON; original retained"))
            continue
        selected = scalar_fields(value)
        records.append(dict(path=name, sha256=hashlib.sha256(payload).hexdigest(),
            bytes=size, category=category(name)[0], status=value.get("status"),
            recorded_at=next((value[k] for k in ("created_at", "verified_at", "observed_at", "completed_at") if k in value), None),
            original_key_fields=selected,
            historical_process_snapshot=bool(re.search(r"job|launch|running", path.name)),
            kind="metadata_extraction_not_a_new_experiment_or_review"))
    print(f"Read {len(files)} tracked files as metadata; extracted {len(records)} JSON objects; {len(exclusions)} explicit exclusions", flush=True)
    write_json(out / "experiment_records.json", records)
    write_json(out / "exclusions.json", exclusions)
    write_json(out / "test_results.json", xml_rows)
    groups = render_groups(out, records)
    doc_text = ["# 原文書の一覧", "", "内容は作成当時の計画・結果。現在の指示はAGENTSとstatusを優先する。番号の欠番は未保存文書の存在を意味しない。", "",
                "| 文書 | 表題 | bytes |", "|---|---|---:|"]
    doc_text.extend(f"| [{escaped(name)}](../../{name}) | {escaped(title)} | {size:,} |" for name, title, size in documents)
    (out / "document_map.md").write_text("\n".join(doc_text) + "\n", encoding="utf-8")
    test_text = ["# 保存されたテスト実行結果", "", "XMLのsuite属性と実node数を転記。過去のrunやsnapshotが重複するため、行の合計を独立テスト数・今回実行数とはしない。JSONのCUDA gate等は各分野台帳も参照。新しいテスト・GPU学習は実行していない。", "",
                 "| XML | 原suite属性 | testcase / failure / error / skipped node数 |", "|---|---|---|"]
    test_text.extend(f"| {link(r['path'])} `{r['path']}` | {escaped(json.dumps(r['attributes'], ensure_ascii=False))} | {r['observed_testcases']} / {r['failure_nodes']} / {r['error_nodes']} / {r['skipped_nodes']} |" for r in xml_rows)
    (out / "verification_ledger.md").write_text("\n".join(test_text) + "\n", encoding="utf-8")
    native_rows = []
    if args.native_reports:
        native = args.native_reports.resolve()
        for path in sorted(native.rglob("*")):
            if path.is_file() or path.is_symlink():
                info = path.lstat()
                native_rows.append((str(path.relative_to(native)), info.st_size, path.is_symlink()))
        (out / "native_reports.tsv").write_text(
            "relative_to_native_reports\tbytes_lstat\tsymlink\n" + "".join(
                f"{name}\t{size}\t{str(sym).lower()}\n" for name, size, sym in native_rows), encoding="utf-8")
    report_json = {r['path'] for r in files if r['path'].startswith('reports/') and r['path'].endswith('.json')}
    accounted = {r['path'] for r in records} | {r['path'] for r in exclusions if r['path'].endswith('.json')}
    if report_json != accounted:
        raise AssertionError("Report coverage is incomplete")
    counts = dict(tracked_files=len(files), tracked_report_files=sum(r['path'].startswith('reports/') for r in files),
                  report_json_files=len(report_json), extracted_JSON_objects=len(records),
                  explicit_exclusions=len(exclusions), original_documents=len(documents),
                  recorded_XML_suites=len(xml_rows), native_report_entries=len(native_rows))
    write_json(out / "coverage.json", dict(status="historical_evidence_catalog_complete_with_explicit_exclusions",
        observed_at=timestamp, source_commit=commit, counts=counts,
        report_JSON_coverage_exact=True, parsing_limit_bytes=LIMIT,
        excluded_by_reason=dict(Counter(r['reason'] for r in exclusions)),
        source_report_files_modified=False, new_training_tokens=0, new_GPU_seconds=0,
        new_model_ratings=0, Base_complete=False,
        scope="Snapshot of tracked files before this documentation change; native reports metadata only, not data-root/weights backup. Every report JSON is extracted or explicitly excluded. Original arrays/raw are linked, not rerated. Git blob SHA1 denotes source-index content; SHA256 denotes parsed report bytes. No global corpus/model validation or independent human review claimed."))
    index = ["# 試行錯誤の詳細台帳", "", f"入力Git revision: `{commit}`。観測UTC: {timestamp}。", "",
             "[全体の説明](../125_project_retrospective.md)から読むと経緯を追いやすい。以下は原記録のキーと値を確認するための詳細。", "",
             "## 分野別の記録", ""]
    index.extend(f"- [{title}]({slug}.md): {len(groups[slug]):,} JSON記録" for slug, title, _ in CATEGORIES)
    index.extend(["", "## 網羅範囲と保存", "",
                  "- [coverage.json](coverage.json): 対象件数・除外・限界。JSON全件を抽出か明示的除外で説明。",
                  "- [全Git保存file一覧](tracked_files.tsv): path、bytes、Git blob SHA1。snapshotやrawを含む。",
                  "- [機械可読の抽出値](experiment_records.json): 原キー・値・原SHA256。",
                  "- [抽出対象外一覧](exclusions.json): 大型/非object/原source snapshot等。無視・合格扱いではない。",
                  "- [原文書一覧](document_map.md): 初期調査から最新計画・全履歴への入口。",
                  "- [完了・採否の入口](decisions.md): terminal/reviewの原status一覧。",
                  "- [保存テスト結果](verification_ledger.md)、[suite原属性JSON](test_results.json)。",
                  "- [WSL reportsのfile一覧](native_reports.tsv): 重み/metrics/rawを含むmetadata。bytesの合計はhardlink重複等を除いた占有量ではない。", "",
                  "この台帳は既存の保存記録の集約であり、新しい実験・再採点・独立監査ではない。記録数を独立実験数とせず、重複したGPU時間や教師数を総計しない。processの歴史的なrunning/next_actionを現在の稼働や開始指示と扱わない。", ""])
    (out / "README.md").write_text("\n".join(index), encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False), flush=True)


if __name__ == "__main__":
    main()
