"""Prepare and publish a data-free, manual-gated research model archive.

No training, corpus read, full checkpoint publication, or credential logging.
Run through the project's pinned uv environment. Preparation is the default;
--publish uploads a prepared, verified folder and checks remote file hashes.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
REPO = "japanese-data-analyze/JMicro-10M-research-archive"
DEFAULT = ROOT / "artifacts/model-archive-20261009"
EXPECTED_TOKENIZER = "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318"
MODELS = (
    ("web-10b", "reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt",
     "410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290"),
    ("staged-10p6b", "reports/phase6/source-order-condition-comparison-v2-20261006/source_order/training/checkpoint-00323503.pt",
     "fb43f2618c0679ca6c6f7a0c5b9faf1b336be8985271c8513f2e4bbfde3cd7ae"),
    ("teacher-decay-2b", "reports/phase6/base-teacher-decay-2b-20261008/latest.pt",
     "03ebf266853541759054ee7100903fa175815adfcfc8e62e559ccdb1ce657442"),
)


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def source_git(source, *args):
    return subprocess.check_output(
        ["git", "-c", f"safe.directory={source}", "-C", str(source), *args])


def prepare(out, source):
    import torch
    from jmicro.model import JMicroModel
    from jmicro.tokenizer import Tokenizer

    if out.exists():
        raise FileExistsError(f"Refusing to overwrite prepared archive: {out}")
    torch.set_num_threads(2)
    torch.manual_seed(42)
    out.mkdir(parents=True)
    tokenizer = ROOT / "artifacts/phase2/4096/tokenizer.model"
    assert sha(tokenizer) == EXPECTED_TOKENIZER
    (out / "tokenizer").mkdir()
    for name in ("tokenizer.model", "tokenizer.vocab", "tokenizer_wrapper.json", "special_tokens.json"):
        shutil.copyfile(tokenizer.parent / name, out / "tokenizer" / name)
    tok = Tokenizer(out / "tokenizer/tokenizer.model")
    for text in ("静かな午後。\n今日は晴れ。", "▁ <|assistant|>\t日本語🙂"):
        assert tok.decode(tok.encode(text)) == text
    entries = []
    for name, relative, expected in MODELS:
        path = ROOT / relative
        assert sha(path) == expected, f"Original checkpoint hash mismatch: {relative}"
        state = torch.load(path, map_location="cpu", weights_only=False)
        model = JMicroModel(state["model_config"]).eval()
        model.load_state_dict(state["model"], strict=True)
        count = sum(p.numel() for p in model.parameters())
        assert count == 10001152
        folder = out / "models" / name
        model.save(folder)
        restored = JMicroModel.load(folder).eval()
        assert all(torch.equal(t, restored.state_dict()[k]) for k, t in model.state_dict().items())
        ids = torch.tensor([[2, *tok.encode("日本語の文章。")]])
        with torch.inference_mode():
            before, after = model(ids).logits, restored(ids).logits
            assert torch.isfinite(after).all() and torch.equal(before, after)
        # Whitelist only numerical learning state. Samplers can contain tokenized
        # documents and are deliberately excluded together with corpus payloads.
        keys = ("optimizer", "scheduler", "rng", "RNG", "counters", "update",
                "tokens", "supervised_tokens", "body_bytes", "token_digest", "decay")
        numerical = {k: state[k] for k in keys if k in state}
        numerical["archive_scope"] = "No model/sampler/dataset; exact resume requires original data and sampler state."
        torch.save(numerical, folder / "training_state.pt")
        counters = state.get("counters") or {k: state.get(k) for k in ("update", "tokens", "supervised_tokens", "body_bytes")}
        entry = dict(name=name, parameters=count, original_checkpoint_path=relative,
                     original_checkpoint_sha256=expected, counters=counters,
                     weights_sha256=sha(folder / "model.safetensors"),
                     tokenizer_sha256=EXPECTED_TOKENIZER, exact_weight_reload=True,
                     CPU_forward_finite_and_identical=True, dataset_included=False,
                     original_sampler_included=False, exact_training_resume_standalone=False)
        write_json(folder / "provenance.json", entry)
        entries.append(entry)
        print(json.dumps(dict(prepared=name, parameters=count)), flush=True)

    # Explicit source directories only: no .git, caches, credentials, data, eval
    # corpora, report snapshots, raw generations or original checkpoint pickles.
    tracked = source_git(source, "ls-files", "-z").decode().split("\0")
    allowed = ("src/", "scripts/", "configs/", "schemas/", "docs/")
    source_files = [n for n in tracked if n and (n.startswith(allowed) or n in
                   ("pyproject.toml", "uv.lock", ".python-version", "AGENTS.md"))]
    source_files += ["docs/125_project_retrospective.md", "docs/retrospective/coverage.json",
                     "docs/retrospective/experiment_records.json", "docs/retrospective/exclusions.json",
                     "docs/retrospective/tracked_files.tsv", "scripts/archive_hub_models.py"]
    secret = re.compile(rb"(?:hf_[A-Za-z0-9]{25,}|ghp_[A-Za-z0-9]{30,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----)")
    for name in sorted(set(source_files)):
        data = (source / name).read_bytes()
        if secret.search(data):
            raise ValueError(f"Credential-like literal in source; not publishing: {name}")
        target = out / "project" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    completion = read(ROOT / "reports/phase6/base_teacher_decay_2b_completion.json")
    original = read(ROOT / "reports/phase6/base_10b_comparison_review.json")
    write_json(out / "research/evaluation_summary.json", dict(
        original_web_10b=original["conditions"]["base10B"] if "base10B" in original["conditions"] else
        {k: v for k, v in original["conditions"].items() if "10" in k},
        staged_10p6b=completion["summaries"]["strong_staged"],
        teacher_decay_2b=completion["summaries"]["candidate"],
        limitations="Existing nonblind evaluations, differing histories and DEV denominators; not rerated; Base not adopted."))
    # Retain decisions, not embedded examples or raw dataset records.
    write_json(out / "research/decision.json", dict(
        status=completion["status"], quality_comparisons=completion["quality_comparisons"],
        paired_differences=completion["paired_differences"], Base_adopted=False,
        training_paused=True, Chat_started=False, quantization_started=False))
    readme = '''---
language:
- ja
pipeline_tag: text-generation
library_name: pytorch
tags:
- jmicro
- research
- experimental
- gated
inference: false
---
# JMicro-10M 研究モデル保存版

約1,000万パラメータの日本語Baseモデルをスクラッチ学習した研究の保存版です。
今後、改善案を思いついたときに重み・実装・設定・評価・失敗理由を確認するために残しています。
**Baseの品質目標は未達です。完成した会話モデルではありません。学習は停止中です。**

リポジトリはpublic、ファイルへのアクセス申請はmanual（手動承認）です。
承認はモデルの品質保証や利用・再配布ライセンスの自動付与を意味しません。

## 保存したモデル

すべて10,001,152 parameters、語彙4096、context1024の同じnative構成です。
10Mはモデルの重みの数で、10B/2Bは各系列の学習量です。別系列の学習量を合算しません。

| フォルダ | 何を残したか | 注意点 |
|---|---|---|
| `models/web-10b` | 元のローカルWebUIで使用した10B入力tokensモデル | 反復・一貫性・停止に課題あり |
| `models/staged-10p6b` | 約10.6B入力tokensのsource-order研究系列 | 一貫性23/80、適切完結26/80。採用基準未達 |
| `models/teacher-decay-2b` | 最後の教師量正規化weight decay、正確に2B教師 | BPB改善でも一貫性3/80。固定条件は不採用 |

各フォルダにnative `model.safetensors`、`jmicro_config.json`、`training_state.pt`、
出所・元checkpoint SHA256・正確な学習量を記録した`provenance.json`があります。
training_stateはoptimizer・scheduler・RNG等の学習状態です。samplerとデータは除いています。
モデル重みは元checkpointから無損失で保存し、CPU再読込・全重み一致・forward一致を確認しています。
HF Transformers形式への変換・量子化・追加学習は今回行っていません。

## 調査と試行錯誤を読む

- [全体記録](project/docs/125_project_retrospective.md): データ、Tokenizer、WSL、学習高速化、EOS、反復、日本語評価、目的関数、構成、最新不採用まで。
- [最新の状態](project/docs/autonomous_status.md)、[最新比較](project/docs/123_base_teacher_decay_2b_results.md)。
- [将来の再開計画](project/docs/124_base_recovery_plan.md)、[文書一覧](project/docs/README.md)。
- [実験値の機械可読記録](project/docs/retrospective/experiment_records.json): 保存済み4,815 JSON報告の原キー・指標・採否・SHA256。記録数は独立実験数ではありません。
- [評価の要約](research/evaluation_summary.json)、[不採用判断](research/decision.json)。
- `project/src`、`project/scripts`、`project/configs`、`project/schemas`、`project/uv.lock`: 当時の実装と固定環境。

原文書中のreports/data/artifactsへのリンクとローカル絶対pathは元研究環境の参照です。
この保存版はraw報告・生成全件・全実験のcheckpoint・データセットを複製するものではありません。
過去文書の「実行中」「次は」は当時の記録であり、現在の開始指示ではありません。

## ローカルでモデルを読み込む

手動承認後、Hugging Faceのローカル認証を設定し、Pythonはuvから実行してください。
まず`huggingface_hub.snapshot_download("japanese-data-analyze/JMicro-10M-research-archive")`で
このリポジトリを取得します。認証tokenはコードへ直接書かないでください。
取得したフォルダの`project`へ移動し、固定環境を復元します。

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
uv run --frozen --extra hub --extra data --extra ml --extra export ../inspect_model.py --model staged-10p6b
```

`inspect_model.py`はCPUでモデルとTokenizerを読み込み、短い入力のforwardを確認します。
native `jmicro.model.JMicroModel.load`と`jmicro.tokenizer.Tokenizer`を使用してください。
generic AutoTokenizerやraw SentencePieceだけではprotected-byte契約を再現できません。

## 保存範囲と未達

データセット・shard・tokenized stream・sampler内の文書は含めていません。
新しい教材での学習や重みの調査は可能ですが、元と厳密に同じ地点から再開するには
元データ、sampler状態、実行環境の復元が必要です。`training_state.pt`はその完全な代替ではありません。
最終採用Base、独立学習seed確認、最新候補の全文DEV/protectedTEST、Chat、最終量子化は未完了です。
繰り返し確認したDEVとCodexの非blind評価を、独立人間評価とは扱いません。

モデル・Tokenizerに一括した新しいライセンスを付与していません。
教材の出所・条件は保存した文書と設定へ残しています。FineWeb2 Edu Japanese/
FineWeb2/Common Crawl、物語・textbook等の出所を保持し、データのライセンスをモデルの
権利全般の保証として扱いません。既公開pilot/Tokenizer bundleと今回のモデル保存版は別です。

全公開ファイルのサイズとSHA256は`archive_manifest.json`と`SHA256SUMS`に記録しています。
'''
    (out / "README.md").write_text(readme, encoding="utf-8")
    inspect_code = '''"""CPU-only native model inspection; launch through uv from project/."""
import argparse
from pathlib import Path
import sys
import torch
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "project/src"))
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
p = argparse.ArgumentParser()
p.add_argument("--model", choices=("web-10b", "staged-10p6b", "teacher-decay-2b"), default="staged-10p6b")
a = p.parse_args()
torch.set_num_threads(2)
m = JMicroModel.load(ROOT / "models" / a.model).eval()
t = Tokenizer(ROOT / "tokenizer/tokenizer.model")
with torch.inference_mode():
    y = m(torch.tensor([[2, *t.encode("静かな午後。")]])).logits
assert torch.isfinite(y).all()
print(dict(model=a.model, parameters=sum(p.numel() for p in m.parameters()), logits_shape=list(y.shape), finite=True))
'''
    (out / "inspect_model.py").write_text(inspect_code, encoding="utf-8")
    files = {str(p.relative_to(out)): dict(bytes=p.stat().st_size, sha256=sha(p))
             for p in sorted(out.rglob("*")) if p.is_file()}
    manifest = dict(created_at=datetime.now(timezone.utc).isoformat(), repository=REPO,
                    source_commit=source_git(source, "rev-parse", "HEAD").decode().strip(),
                    scope="Three major model lineages, native weights, numerical learning state, code/docs/metadata; no datasets or sampler payloads.",
                    source_worktree_snapshot=True, models=entries, files=files,
                    new_training_tokens=0, new_GPU_seconds=0, Base_adopted=False)
    write_json(out / "archive_manifest.json", manifest)
    sums = {**files, "archive_manifest.json": dict(sha256=sha(out / "archive_manifest.json"))}
    (out / "SHA256SUMS").write_text("".join(f"{r['sha256']}  {n}\n" for n, r in sorted(sums.items())), encoding="utf-8")
    print(json.dumps(dict(status="prepared", files=len(files) + 2,
                          bytes=sum(p.stat().st_size for p in out.rglob("*") if p.is_file()))), flush=True)


def token():
    from huggingface_hub import get_token
    value = get_token()
    if value:
        return value
    saved = Path("/mnt/c/Users/AiHUB/.cache/huggingface/token")
    if saved.is_file():
        return saved.read_text().strip()
    raise RuntimeError("Hugging Face credentials unavailable; run uv run --frozen --extra hub hf auth login")


def publish(out):
    from huggingface_hub import HfApi
    from huggingface_hub.errors import RepositoryNotFoundError
    manifest = read(out / "archive_manifest.json")
    expected = manifest["files"]
    for name, row in expected.items():
        assert sha(out / name) == row["sha256"], f"Prepared file changed: {name}"
    api = HfApi(token=token())
    try:
        before = api.model_info(REPO)
    except RepositoryNotFoundError:
        api.create_repo(REPO, repo_type="model", private=True)
    else:
        # A repeat may verify our own uploaded snapshot, but cannot overwrite
        # an unrelated existing repository or weaken its access settings.
        names = set(api.list_repo_files(REPO))
        if names - {".gitattributes"} and "archive_manifest.json" not in names:
            raise ValueError("Existing repository is not this archive")
        if not before.private and before.gated != "manual":
            raise ValueError("Existing public repository is not manually gated")
    api.update_repo_settings(REPO, gated="manual", repo_type="model")
    info = api.model_info(REPO)
    assert info.gated == "manual"
    commit = api.upload_folder(repo_id=REPO, repo_type="model", folder_path=out,
                               commit_message="Archive three 10M research lineages without datasets")
    info = api.model_info(REPO, revision=commit.oid, files_metadata=True)
    checks = []
    local = {str(p.relative_to(out)): p for p in out.rglob("*") if p.is_file()}
    remote = {p.rfilename: p for p in info.siblings}
    assert set(remote) == set(local) | {".gitattributes"}
    for name, path in local.items():
        item = remote[name]
        assert item.size == path.stat().st_size, f"Remote size mismatch: {name}"
        if item.lfs:
            assert item.lfs.sha256 == sha(path), f"Remote LFS checksum mismatch: {name}"
            algorithm = "sha256"
        else:
            data = path.read_bytes()
            blob = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
            assert item.blob_id == blob, f"Remote Git blob mismatch: {name}"
            algorithm = "git-blob-sha1"
        checks.append(dict(path=name, bytes=item.size, algorithm=algorithm, matched=True))
    # Expose only after the complete uploaded archive has been verified while gated.
    api.update_repo_settings(REPO, gated="manual", private=False, repo_type="model")
    info = api.model_info(REPO)
    public = HfApi(token=False).model_info(REPO, token=False)
    assert info.sha == commit.oid and not info.private and info.gated == "manual"
    assert not public.private and public.gated == "manual"
    import httpx
    response = httpx.get(f"https://huggingface.co/{REPO}/resolve/main/models/web-10b/model.safetensors",
                         follow_redirects=False, timeout=30)
    assert response.status_code in (401, 403), "Anonymous download unexpectedly allowed"
    result = dict(status="published_and_verified", repository=REPO, url=f"https://huggingface.co/{REPO}",
                  revision=info.sha, private=info.private, gated=info.gated,
                  anonymous_weight_http_status=response.status_code, files=checks,
                  archive_manifest_sha256=sha(out / "archive_manifest.json"),
                  models=manifest["models"], dataset_included=False, new_training_tokens=0,
                  new_GPU_seconds=0, Base_adopted=False)
    destination = ROOT / "reports/publication/model_archive_20261009.json"
    write_json(destination, result)
    print(json.dumps({k: v for k, v in result.items() if k not in ("files", "models")}), flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=Path, default=DEFAULT)
    p.add_argument("--source", type=Path, default=Path("/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m"))
    p.add_argument("--publish", action="store_true")
    a = p.parse_args()
    if a.publish:
        publish(a.output.resolve())
    else:
        prepare(a.output.resolve(), a.source.resolve())


if __name__ == "__main__":
    main()
