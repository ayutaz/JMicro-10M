"""Export the final diagnostic SFT weights and publish a verified public archive.

CPU only. No training, corpus reads, sampler/optimizer export, or token logging.
The historical Base publication script and all scientific records remain intact.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from archive_hub_models import token

REPO = "japanese-data-analyze/JMicro-10M-chat-research-20261018"
BASE = "japanese-data-analyze/JMicro-10M-research-archive"
RUN = ROOT / "reports/phase7/chat-two-attribute-20261018"
OUT = ROOT / "artifacts/chat-sft-public-20261018-v2"
RECEIPTS = ROOT / "reports/publication/chat-sft-public-20261018-v2"
CHECKPOINT_SHA = "44128809acccf45fbfddcd8863a72af5a029d43a660e10b06ed73e4157aff553"
CONFIG_SHA = "32804bb9d68fea46c2df67eec4bdb52ef0c904ec39e3291b413d4dc76c2f5d2b"
TOKENIZER_SHA = "a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318"


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n")


def inventory(folder):
    return {p.relative_to(folder).as_posix(): {"sha256": sha(p), "bytes": p.stat().st_size}
            for p in sorted(folder.rglob("*")) if p.is_file()}


CARD = '''---
language:
- ja
pipeline_tag: text-generation
library_name: pytorch
tags:
- jmicro
- research
- experimental
- text-generation
inference: false
---
# JMicro 10M チャット学習の研究モデル

日本語の約1,000万パラメータBaseモデルに、二つの情報を答える64件の教材で
SFT（教師あり追加学習）を行った最終重みです。**一般会話の品質は改善せず、
今回の候補は不採用です。** 成功した限定課題と失敗した転用を調べるために公開します。
リポジトリと全ファイルはpublicで、アクセス申請・ログインなしで取得できます。

## モデルと学習

10,001,152 parameters、13層、hidden256、FFN640、GQA 4Q/2KV、語彙4096、
context1024。元Baseからfresh Adam、seed42、LR1e-4、BF16/mathで483更新、
250,003 Assistant教師tokenを学習しました。64教材は8組の事実設定の変形です。
親Baseは[研究保存版のweb-10b](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive/tree/main/models/web-10b)です。

## 評価結果

| 固定した評価 | 結果 |
|---|---:|
| 学習済み教材の全文再現 | 64/64 |
| 同じ質問形式で未知の値に回答 | 30/32 |
| 質問表現・配置を変更した回答 | 15/32（二項目は0/16） |
| 自分の過去の返答を使う会話の最終回答 | 9/16 |
| 公開診断100ケースのタスク成立 | 3/100（直前の別SFTモデルは19/100） |

最大32tokenのgreedy、BF16/mathによる固定DEV評価です。全1,973応答を
Codexで非blind判定しており、独立人手評価や一般的な利用全体の精度ではありません。
既存7組の内容成立も全て低下しました。旧モデルと教材・教師量が異なる歴史的比較です。
空応答、同文反復、履歴の訂正失敗、UTF8破損が残ります。
[評価の全文と全回答](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/main/docs/165_chat_two_attribute_diagnosis_results.md) /
[集計JSON](research/final_analysis.json)。

## CPUで試す

[uv](https://docs.astral.sh/uv/)を用意して、この保存版をダウンロードします。

```sh
uvx --from huggingface-hub hf download japanese-data-analyze/JMicro-10M-chat-research-20261018 --local-dir jmicro-chat
cd jmicro-chat
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra ml --extra hub
uv run --frozen --extra ml --extra hub inspect_model.py --prompt 'こんにちは。' --max-new-tokens 32
```

`inspect_model.py`はCPU FP32、nativeモデル、元の対話テンプレートとprotected-byte
Tokenizer、greedy、EOT7/EOS3停止、特殊ID六つの抑制を使います。実際の本文と
停止理由をJSONで返します。CPU FP32の試用は上表のBF16評価と精度条件が異なります。
`AutoModelForCausalLM`や`AutoTokenizer`の標準形式ではありません。

## 保存内容とライセンス

`model.safetensors`と`jmicro_config.json`が重みと構成、`tokenizer/`が共通Tokenizer、
`src/`がnative実装、`provenance.json`が親と最終checkpointのSHA256です。
全ての重みの再読込一致とCPU forward一致を確認しています。
`archive_manifest.json`と`SHA256SUMS`にファイルのhashを記録しています。
データセット、sampler、optimizer、RNG、元のcheckpoint pickleは含みません。
元と厳密に同じ地点からの学習再開を、この保存版だけで再現することはできません。

プロジェクトのコードは[Apache-2.0](LICENSE)です。第三者コードの帰属は
[NOTICE](NOTICE)と`src/jmicro/_vendor/`に保持しています。
モデル重みとTokenizerに、この公開で新しい一括ライセンスを付与していません。
コードのApache-2.0と、重み・元教材の利用条件を区別してください。
'''

INSPECT = '''"""CPU smoke inference using the archived native implementation."""
import argparse
import json
from pathlib import Path
import sys
import torch
from torch.nn.attention import sdpa_kernel, SDPBackend
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
from jmicro.model import JMicroModel
from jmicro.tokenizer import Tokenizer
from jmicro.chat_evaluation import generate_reply
p = argparse.ArgumentParser(description=__doc__)
p.add_argument("--prompt", default="こんにちは。")
p.add_argument("--max-new-tokens", type=int, default=32, choices=range(1, 65))
a = p.parse_args()
torch.set_num_threads(2)
torch.manual_seed(42)
model = JMicroModel.load(ROOT).eval()
tok = Tokenizer(ROOT / "tokenizer/tokenizer.model")
with sdpa_kernel(SDPBackend.MATH):
    result = generate_reply(model, tok, [{"role":"user", "content":a.prompt}],
                            "cpu", "fp32", a.max_new_tokens, True)
print(json.dumps(result, ensure_ascii=False))
'''


def prepare():
    import torch
    from jmicro.model import JMicroModel
    from jmicro.tokenizer import Tokenizer
    if OUT.exists():
        raise FileExistsError("Prepared archive already exists; verify without overwriting")
    checkpoint = Path(read(RUN / "learning_complete.json")["checkpoint"]["path"])
    config = ROOT / "configs/phase7/chat-two-attribute-20261018.json"
    assert sha(checkpoint) == CHECKPOINT_SHA and sha(config) == CONFIG_SHA
    contract = read(config)
    for name, expected in contract["source_sha256"].items():
        assert sha(ROOT / name) == expected, name
    assert read(RUN / "completion.json")["status"] == "all_five_steps_completed_candidate_not_adopted"
    torch.set_num_threads(2)
    torch.manual_seed(42)
    state = torch.load(checkpoint, map_location="cpu", weights_only=False)
    model = JMicroModel(state["model_config"]).eval()
    model.load_state_dict(state["model"], strict=True)
    assert sum(p.numel() for p in model.parameters()) == 10001152
    assert all(torch.isfinite(t).all() for t in model.state_dict().values())
    model.save(OUT)
    restored = JMicroModel.load(OUT).eval()
    assert all(torch.equal(v, restored.state_dict()[k]) for k, v in model.state_dict().items())
    assert restored.lm_head.weight is restored.model.embed_tokens.weight
    for name in ("tokenizer.model", "tokenizer.vocab", "tokenizer_wrapper.json", "special_tokens.json"):
        target = OUT / "tokenizer" / name
        target.parent.mkdir(exist_ok=True)
        shutil.copyfile(ROOT / "artifacts/phase2/4096" / name, target)
    assert sha(OUT / "tokenizer/tokenizer.model") == TOKENIZER_SHA
    tok = Tokenizer(OUT / "tokenizer/tokenizer.model")
    for text in ("静かな午後。\n今日は晴れ。", "▁ <|assistant|>\t日本語🙂"):
        assert tok.decode(tok.encode(text)) == text
        ids = torch.tensor([[2, *tok.encode(text)]])
        with torch.inference_mode():
            first, second = model(ids).logits, restored(ids).logits
        assert torch.isfinite(second).all() and torch.equal(first, second)
    for source in sorted((ROOT / "src/jmicro").rglob("*")):
        if source.is_file() and source.suffix in (".py", ".txt") and "__pycache__" not in source.parts:
            target = OUT / source.relative_to(ROOT)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    for name in ("pyproject.toml", "uv.lock", ".python-version", "LICENSE", "NOTICE"):
        shutil.copyfile(ROOT / name, OUT / name)
    research = OUT / "research"
    research.mkdir()
    for name in ("final_analysis.json", "completion.json"):
        shutil.copyfile(RUN / name, research / name)
    shutil.copyfile(config, research / config.name)
    shutil.copyfile(Path(__file__), research / "publish_latest_sft.py")
    (OUT / "README.md").write_text(CARD, encoding="utf-8")
    (OUT / "inspect_model.py").write_text(INSPECT, encoding="utf-8")
    write(OUT / "provenance.json", dict(
        repository=REPO, original_checkpoint_sha256=CHECKPOINT_SHA,
        original_checkpoint_path=checkpoint.relative_to(ROOT).as_posix(),
        parent=contract["parent"], config_sha256=CONFIG_SHA, tokenizer_sha256=TOKENIZER_SHA,
        parameters=10001152, updates=483, assistant_teacher_tokens=250003,
        state_tensor_count=len(model.state_dict()),
        unique_parameter_tensor_count=len(list(model.parameters())),
        all_state_tensors_reload_exact=True, CPU_forward_finite_and_identical=True,
        training_dataset_included=False, sampler_included=False, optimizer_included=False,
        adopted=False, new_training_tokens=0, new_GPU_seconds=0))
    credential = re.compile(rb"hf_[A-Za-z0-9]{25,}|ghp_[A-Za-z0-9]{30,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----")
    for path in OUT.rglob("*"):
        assert not path.is_symlink(), path
        if path.is_file():
            assert path.suffix not in (".pt", ".jsonl", ".bin"), path
            assert not credential.search(path.read_bytes()), path
    write(OUT / "archive_manifest.json", dict(repository=REPO, files=inventory(OUT)))
    (OUT / "SHA256SUMS").write_text("".join(f"{r['sha256']}  {n}\n" for n,r in inventory(OUT).items()), encoding="utf-8")
    write(RECEIPTS / "prepared.json", dict(repository=REPO, files=inventory(OUT),
        new_training_tokens=0, new_GPU_seconds=0, status="export_verified"))
    print(json.dumps(dict(status="export_verified", files=len(inventory(OUT)), bytes=sum(r["bytes"] for r in inventory(OUT).values()))))


def verify_remote(api, repo, revision, expected):
    info = api.model_info(repo, revision=revision, files_metadata=True)
    remote = {p.rfilename: p for p in info.siblings}
    assert set(remote) - {".gitattributes"} == set(expected), (set(remote), set(expected))
    for name, row in expected.items():
        item = remote[name]
        assert item.size == row["bytes"], name
        if item.lfs:
            assert item.lfs.sha256 == row["sha256"], name
        else:
            data = (OUT / name).read_bytes()
            assert item.blob_id == hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest(), name
    return info


def publish():
    from huggingface_hub import HfApi, hf_hub_download
    from huggingface_hub.errors import RepositoryNotFoundError
    expected = read(RECEIPTS / "prepared.json")["files"]
    assert inventory(OUT) == expected
    api = HfApi(token=token())
    try:
        info = api.model_info(REPO)
    except RepositoryNotFoundError:
        api.create_repo(REPO, repo_type="model", private=True, exist_ok=False)
    else:
        files = set(api.list_repo_files(REPO))
        if files - {".gitattributes"}:
            remote_manifest = hf_hub_download(REPO, "archive_manifest.json", revision=info.sha, token=token())
            assert sha(Path(remote_manifest)) == expected["archive_manifest.json"]["sha256"]
    commit = api.upload_folder(repo_id=REPO, folder_path=OUT,
        commit_message="Publish final diagnostic SFT weights with failed-quality results and native CPU loader")
    info = verify_remote(api, REPO, commit.oid, expected)
    api.update_repo_settings(REPO, gated=False, private=False)
    anonymous = HfApi(token=False)
    visible = anonymous.model_info(REPO, token=False)
    assert not visible.private and not visible.gated and visible.sha == commit.oid
    weights = Path(hf_hub_download(REPO, "model.safetensors", revision=commit.oid, token=False))
    assert sha(weights) == expected["model.safetensors"]["sha256"]
    write(RECEIPTS / "SFT_public.json", dict(repository=REPO, revision=visible.sha,
        private=visible.private, gated=visible.gated, files=expected,
        anonymous_full_weights_download_SHA256_verified=True, status="public_verified"))

    before = api.model_info(BASE, files_metadata=True)
    old_readme = Path(hf_hub_download(BASE, "README.md", revision=before.sha, token=token())).read_text(encoding="utf-8")
    (RECEIPTS / "Base_README_before.md").write_text(old_readme, encoding="utf-8")
    current = old_readme.replace("- gated\n", "")
    current = current.replace("リポジトリはpublic、ファイルへのアクセス申請はmanual（手動承認）です。\n承認はモデルの品質保証や利用・再配布ライセンスの自動付与を意味しません。",
        "リポジトリと全ファイルはpublicで、アクセス申請・ログインなしで取得できます。\n2026-10-18に手動承認を解除しました。公開設定は品質保証や利用ライセンスの変更を意味しません。")
    current = current.replace("手動承認後、Hugging Faceのローカル認証を設定し、Pythonはuvから実行してください。", "ログインは不要です。Pythonはuvから実行してください。")
    current += f"\n2026-10-18の[最新SFT研究モデル](https://huggingface.co/{REPO})も公開しています。一般会話の品質不採用を含む評価結果を添えています。\n"
    commit_base = api.upload_file(repo_id=BASE, path_or_fileobj=current.encode(), path_in_repo="README.md",
        parent_commit=before.sha, commit_message="Document ungated public downloads and link latest SFT research archive")
    after = api.model_info(BASE, revision=commit_base.oid, files_metadata=True)
    old_files = {p.rfilename: (p.blob_id, p.lfs.sha256 if p.lfs else None, p.size) for p in before.siblings if p.rfilename != "README.md"}
    new_files = {p.rfilename: (p.blob_id, p.lfs.sha256 if p.lfs else None, p.size) for p in after.siblings if p.rfilename != "README.md"}
    assert old_files == new_files
    api.update_repo_settings(BASE, gated=False, private=False)
    public_base = anonymous.model_info(BASE, token=False)
    assert not public_base.private and not public_base.gated and public_base.sha == commit_base.oid
    checks = []
    for name in ("web-10b", "staged-10p6b", "teacher-decay-2b"):
        filename = f"models/{name}/model.safetensors"
        target = Path(hf_hub_download(BASE, filename, revision=commit_base.oid, token=False))
        item = next(p for p in after.siblings if p.rfilename == filename)
        assert item.lfs and sha(target) == item.lfs.sha256 and target.stat().st_size == item.size
        checks.append(dict(file=filename, sha256=sha(target), anonymous_full_download_verified=True))
    write(RECEIPTS / "Base_public.json", dict(repository=BASE, previous_revision=before.sha,
        revision=public_base.sha, private=False, gated=False, non_README_files_unchanged=True,
        anonymous_downloads=checks, status="public_verified"))
    all_models = []
    for row in api.list_models(author="japanese-data-analyze"):
        item = anonymous.model_info(row.id, token=False)
        all_models.append(dict(repository=item.id, private=item.private, gated=item.gated))
    assert all(not r["private"] and not r["gated"] for r in all_models)
    write(RECEIPTS / "namespace_public.json", dict(models=all_models, status="all_model_repositories_public_ungated"))
    print(json.dumps(dict(status="all_models_public_verified", repositories=all_models)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("prepare", "publish"))
    args = parser.parse_args()
    prepare() if args.action == "prepare" else publish()
