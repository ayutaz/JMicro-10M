# JMicro-10M

日本語短文生成と短い雑談を目指す、Tokenizerからスクラッチ構築した10,001,152パラメータの言語モデル。現在はBaseの品質改善段階です。

**2026-10-08: 累積20億教師トークンの比較学習と全80件の評価が完了し、ユーザー指示で一時停止しています。Baseは未完成・未採用です。** 今回のドキュメント更新では学習を再開していません。Chat・量子化も開始しません。

[現在の状態](docs/autonomous_status.md) / [最新結果123](docs/123_base_teacher_decay_2b_results.md) / [今後の計画124](docs/124_base_recovery_plan.md) / [文書一覧](docs/README.md)

**固定方針: 10Mのサイズを維持し、その小ささを優位性とします。** 品質改善は約10Mの総パラメータ予算内で検討し、大型化を解決策にしません。日本語Baseの品質基準は維持します。

## 最新の成果

同じnative10Mモデル、既存2B TRAIN pool、同じ2B教師予算で、教師数に応じてweight decayを調整する条件を比較しました。データ増量の実験ではありません。

| 指標 | 元native2B | 今回の候補 |
|---|---:|---:|
| 共通DEV256本文BPB ↓ | 1.106386 | 1.090316 |
| 一貫性が良好 /80 ↑ | 3 | 3 |
| 適切に完結 /80 ↑ | 7 | 5 |
| EOS停止 /80 ↑ | 20 | 23 |
| 自動反復 /80 ↓ | 27 | 27 |
| Unicode失敗 /80 ↓ | 0 | 1 |

BPBは約1.45%改善しましたが、文章の一貫性や完結性は改善しませんでした。元の採用条件を満たさないため、今回の条件は不採用として閉じています。全80件の内容評価はCodexによる非blind採点です。

## データ量・学習量・モデル規模

| 区分 | 保存証拠にある量 |
|---|---:|
| モデル規模 | 10,001,152 parameters |
| 一般Web TRAIN準備量 | 12,225,819,077 tokens |
| 短い物語準備量 | 200,000,192 tokens |
| 最新比較のaccepted混合pool | 約2B tokens、Web75%/textbook20%/story5% |
| 最新候補の学習量 | 正確に2,000,000,000 supervised tokens |
| 元WebUIモデルの学習量 | 10,000,007,168 tokens |

別系列の学習量は合算しません。再利用した教材を新規量として二重加算せず、本文教師・入力・padding・bytesを区別します。データ不足、学習不足、10Mの容量限界のいずれも単独原因として確定していません。

## ローカルで試す

[http://127.0.0.1:7860](http://127.0.0.1:7860)で、以前の10Bモデルの続きを生成できます。最新の不採用2B候補へ差し替えていません。推論はWSL/RTX4090です。文書更新時に元checkpointのHTTP応答とidleを確認しています。将来の稼働は起動状態を再確認してください。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/stop_webui.ps1
```

[操作43](docs/43_local_webui.md)。既存processを確認して重複起動を避けます。UIはGPU lockを保持するため、再開されたGPU実験中だけ停止し、終端で元10Bへ復帰します。

## 再開後の計画

既存結果から未解決の比較を最大1件選び、必要な診断だけを行い、短い同条件比較から始めます。生成品質と保持条件が改善した候補だけを本比較へ進めます。その後に独立学習seed、fullDEV、protectedTEST、採用を確認し、Base完成時に通知して停止します。[目的・成果物・進行条件](docs/124_base_recovery_plan.md)。

次の介入条件は未選定・未凍結です。BPB改善だけを理由に10Bへ延長したり、失敗後に別仮説を自動で起動したりしません。

## 環境と保存先

全Pythonはuv管理3.12.7から実行します。依存変更は `uv add`。学習はWSL2/RTX4090/Linux disk。以下は新規環境・欠損時の復元用です。

```sh
uv python install 3.12.7
uv sync --frozen --python 3.12.7 --extra hub --extra data --extra ml --extra export
```

Python commandは `uv run --frozen --extra hub --extra data --extra ml --extra export ...` を使います。system Python/pipへ切り替えません。

Git正本はWindows `C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m`、Linux実行コピーは `/home/aihub_ubuntu/src/japanese-tiny-llm-10m`、dataは `/home/aihub_ubuntu/jmicro-data`。重み・shards・大型metricsはGit外なので別途保全が必要です。[引継ぎ](docs/windows_handoff.md)、[固定pilot/Tokenizer復元](docs/huggingface_handoff.md)。

Git identityは `yousan <ka1357amnbpdr@gmail.com>`。検証済み変更はlocal commitし、自動push・公開は行いません。Phase0〜3や過去の凍結report/source/rawを保持します。

[作業ルール](AGENTS.md) / [ロードマップ](docs/15_project_roadmap.md) / [チェックリスト](docs/10_next_steps.md) / [評価契約](docs/evaluation_protocol.md) / [実験の探し方](docs/base_experiment_lookup.md)