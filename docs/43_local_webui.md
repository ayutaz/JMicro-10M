# 元10B BaseモデルのローカルWebUI

更新: 2026-10-17 JST。ユーザーのチャット動作確認依頼を受け、SFT済みChat用の画面を追加した。Base事前学習と最初のRealPersonaChat SFTは終了済み。品質の正式採用条件は未達だが、短い会話を試せる。

## Chatを試す

**[http://127.0.0.1:7861](http://127.0.0.1:7861)** を開く。元10B親からRealPersonaChatで3周SFTしたモデル（checkpoint-00003785、1,899,555 Assistant教師、10,001,152 parameters）を使う。「新しい会話」で履歴を消し、Enterで送信・Shift+Enterで改行する。文脈に収まらない場合は古い発言を自動削除せず、新しい会話を案内する。

CPU FP32/greedy、既定32生成token、画面で16/32/64を選べる。EOT7/EOS3または指定上限で停止し、上限による打切りを自然な完結とは数えない。短くする設定は反映済みだが、長文で内容が崩れる原因や学習済み能力の改善は未検証。元のSFT評価はCUDA BF16/64tokenだったため、今回のCPU返答を以前のDEV件数へ足さない。サーバーは会話本文を保存せず、履歴はブラウザーのメモリに保持する。

停止中に起動する場合、Windowsのproject rootから実行する。

```powershell
.\scripts\start_chat_demo.ps1
```

新しいGPU学習は起動せず、元のBase画面7860もそのまま利用できる。Chatの起動記録はWSL reports/local/chat-webui/server.json、Windows launcherはreports/local/chat-webui/launcher.json。Chat既存processがある場合は同checkpointを確認して再利用する。

## 今回の実例

5会話10応答すべてを記録した。全応答がEOT終了、有効UTF8、履歴削除なし。[全raw](../reports/phase7/chat-demo-20261017/raw.json)・[個別notes](../reports/phase7/chat-demo-20261017/notes.json)。

| 入力 | 実際の返答 |
|---|---|
| こんにちは。 | こんにちは！ |
| 好きな食べ物は何？ | カレーが好きですね。 |
| 甘いものは好き？ | 甘いもの大好きです。 |
| 名前はモモだよ。 | モモ！かわいいですよね。 |
| うちの猫の名前、覚えてる？ | 覚えてないですね。 |

短い雑談ができる部分と、履歴を内容に使えない部分がある。以前の不採用は正式な品質条件の未達であり、応答そのものが一切できないという意味ではない。今回の操作確認で正式採否や過去の評価基準を変更していない。

## Baseの文章生成画面

[最新結果・更新記録148](148_latest_base_and_documentation.md) / [現在の計画145](145_post_rejection_next_plan.md) / [文書一覧](README.md) / [全件カタログ](document_catalog.md)。

元の10B Baseで文章の続きを試すUI。正式採用Base/Chatではなく、不採用の最新RDrop候補へ置き換えていない。URLは[http://127.0.0.1:7860](http://127.0.0.1:7860)。

RDrop終了記録の観測2026-10-16T15:06:52.7804980Z（JST10月17日）では、科学WSL PID459024/start80531912とWindows32704は終了。元UIはPID459564/start80610052、boot4052bfc5-3850-44e4-9123-d34a9e19f36e、元10B親/Tokenizer/native10M・idle HTTP・kernel FLOCK一致で復帰済み。これは時点付き証拠で現在の生存保証ではない。今回の文書作業ではHTTP/生成/再起動を行っていない。

## 操作

Windowsのproject rootから状態を確認する。

```powershell
Invoke-RestMethod http://127.0.0.1:7860/api/model
```

停止中で実process/lockの競合もない場合だけ起動する。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
```

停止が必要な操作時はscripts/stop_webui.ps1を使用。稼働中の重複起動、旧学習runnerの起動、候補重みへの無断差替えをしない。Git cloneにはcheckpointがないため、欠損時は[引継ぎ](windows_handoff.md)の手順を使う。

最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。

有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。

[RDrop完了記録](../reports/phase6/rdrop-science-20261016/completion.json) / [原採点・全guard](../reports/phase6/rdrop-science-20261016/review.json) / [GPU上限解除記録](../reports/phase6/rdrop-science-preparation-20261016/authorization.json)。

<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->
<a id="使い方"></a>
<a id="保存と確認結果"></a>
<a id="更新前の本文契約当時の記録"></a>
<a id="起動停止"></a>
