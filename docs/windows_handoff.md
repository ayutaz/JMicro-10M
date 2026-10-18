# 環境と保存先の引継ぎ

更新: 2026-10-18 JST。

WindowsをGitの正本、WSLを実行・大容量保存先としています。新しいPCでモデルを試すだけなら、[READMEのCPU手順](../README.md#最新モデルをcpuで試す)を使えます。元の学習の厳密再開には公開重み以外の保存物が必要です。

## ローカルの保存先

| 対象 | 場所 |
|---|---|
| Git正本 | `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m` |
| WSL実行コピー | `/home/aihub_ubuntu/src/japanese-tiny-llm-10m` |
| データ | `/home/aihub_ubuntu/jmicro-data` |
| 元Base | `reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt` |
| 最新SFT | `reports/phase7/chat-two-attribute-20261018/model/checkpoint-00000483.pt` |
| Tokenizer | `artifacts/phase2/4096/tokenizer.model` |

元Base SHA256は`410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`、最新SFTは`44128809acccf45fbfddcd8863a72af5a029d43a660e10b06ed73e4157aff553`です。全学習stateはWSLへ、小raw・判定理由・監査記録はWindows/Gitへ保全します。

## Pythonと同期

記録された環境はWSL2/Linux disk/RTX4090、Python3.12.7とuvです。Pythonは`uv run --frozen`から実行し、必要なextraを指定します。依存は`uv sync --frozen`で復元し、既存の学習環境を文書更新のために変更しません。

WindowsとWSLを同期する時は対象を限定し、元の科学source/configのEOLとhashを保持します。WindowsのGit HEADを正とし、WSLで別の履歴を作ったり大容量重みをGitへ追加したりしません。

## 実行状態を確認する

最新SFTは正常終了し、2026-10-18 02:40 UTCの[終端観測](../reports/phase7/chat-two-attribute-20261018/terminal_observation.json)で元Base UI復帰を確認しました。PIDの記録だけで現在生存と断定せず、操作時に実PID/boot/start・HTTP・kernel lockを照合します。

[WebUI操作](43_local_webui.md)を参照し、元Baseと各SFTのモデル名・port・checkpointを区別してください。今回は起動・停止・モデル差替えを行いません。[公開モデルと復元範囲](126_model_archive.md)。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/windows_handoff.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="6-実装済みcliと次回の再開"></a>
<a id="git外で保全する重みと教材"></a>
<a id="windows--wsl-引継ぎ"></a>
<a id="前回chatと旧baseのgit外保全"></a>
<a id="前回chatの閉じたrunと当時のui"></a>
<a id="復元と操作"></a>
<a id="新pc欠損時だけ行う復元"></a>
<a id="明示的な実行再開後の順序"></a>
<a id="最新baseと最後の観測"></a>
<a id="最新の保存と最後の実行観測"></a>
<a id="正本と保存場所"></a>
<a id="閉じた最新runとui"></a>
