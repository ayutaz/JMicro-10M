# ローカル画面とモデルの区別

更新: 2026-10-18 JST。

研究用のBase/SFT画面を複数用意しています。最新SFT診断の重みを、既存画面へ採用・差替えしたわけではありません。配布された最新SFTを試す場合は[READMEのCPU手順](../README.md#最新モデルをcpuで試す)を使ってください。

## 各portのモデル

| port | 対象 |
|---|---|
| 7860 | 元10B Base、文章の続きを生成 |
| 7861 | 最初のRealPersonaChat SFT |
| 7862 / 7863 | 自然な会話教材SFTの候補C1 / 対照C0、結果150 |
| 7864 / 7865 | 回答教材SFTの候補C1 / 対照C0、結果156 |
| 7866 / 7867 | 入力配置SFTの候補C1 / 対照C0、結果162 |

これらはローカル環境のport対応表です。現在の生存は保証せず、画面が動いている場合も品質採用済みとは解釈しません。ChatはCPU FP32/greedy、既定32token、16/32/64の選択です。最新64教材SFT用の追加画面はありません。

## 操作と確認

稼働時は`http://127.0.0.1:<port>`へアクセスします。「新しい会話」で履歴を消し、Enterで送信、Shift+Enterで改行します。開始前に`/api/model`で実際のモデル名・checkpointを確認してください。

```powershell
Invoke-RestMethod http://127.0.0.1:7860/api/model
```

停止中の元Baseを起動する既存の入口は`./scripts/start_webui.ps1`です。最初のChatは`./scripts/start_chat_demo.ps1`、自然会話教材のC1/C0は`./scripts/start_natural_chat_demo.ps1 -Arm C1`等を使います。後続画面の固有手順は[当時の実行結果162](162_chat_input_structure_sft_results.md)を確認し、閉じた学習runnerをUI起動に使わないでください。

短い挨拶が返せても、訂正・実履歴・継続会話の品質は未達です。7864での同文固定は[実ブラウザー確認156](156_answer_curriculum_results.md)で再現しています。入力と履歴の送信が正しくてもモデル自身が反復するため、UIの動作と内容の品質を区別します。

[現在の状態](autonomous_status.md) / [最新SFT結果](165_chat_two_attribute_diagnosis_results.md) / [公開モデル](166_public_models_and_oss.md) / [文書一覧](README.md)

前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/JMicro-10M/blob/ed91c002cdfe52c879e275241c58436bfef3e394/docs/43_local_webui.md)に保存しています。過去の「最新」「実行中」はその記載時点の状態です。

<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->
<a id="baseの文章生成画面"></a>
<a id="chatを試す"></a>
<a id="今回の実例"></a>
<a id="使い方"></a>
<a id="保存と確認結果"></a>
<a id="元10b-baseモデルのローカルwebui"></a>
<a id="操作"></a>
<a id="更新前の本文契約当時の記録"></a>
<a id="起動停止"></a>
