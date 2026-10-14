# 学習済み10BモデルのローカルWeb UI

2026-10-04、ユーザーの依頼で現在の学習済みモデルを試すWeb UIを作成・起動した。ブラウザは **http://127.0.0.1:7860** を開く。Windowsのlocalhost/IPv6ではPowerShellの接続確認がtimeoutしたため、確認済みIPv4アドレスを使う。

モデルは10,001,152 parameters、総10,000,007,168 tokens学習のfinal checkpoint。文章の書き出しから続きを生成するBaseモデルであり、対話用の学習は未実施。反復・意味の誤り・EOS停止の課題は[品質評価](42_base_10b_quality_evaluation.md)の通り残る。

## 使い方

書き出しを入力し「続きを生成」を押す。サンプリングまたはGreedy、生成量16〜512 tokens、Temperature、Top P、シードを調整できる。生成結果は順次表示され、停止ボタンとコピーを使える。画面に表示するのは入力に続く新しい文章だけ。

サンプリングの初期値はtemperature0.8/top_p0.9/seed42、生成上限128 tokens。入力BOSと生成の合計は1024 tokens以内。超える場合は入力か生成量を減らす案内を表示し、自動切断しない。自然EOSで止まるか上限で止まるかを表示する。上限の未完成UTF8末尾は既存display helperで保留し、raw結果の失敗は免除しない。

## 起動・停止

Windowsのproject rootで実行する。起動scriptは必要なUI fileをWSLへLFで同期し、hidden Windows supervisorからuvで起動する。追加の依存導入は不要。

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/start_webui.ps1
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/stop_webui.ps1
```

起動済みの場合、起動scriptは既存サーバーを案内する。停止scriptは保存PID/boot ID/start ticksの一致を確認してSIGTERMする。PC/WSLを終了した後は起動scriptを再実行する。

WSL側の手動起動は次の通り。Windows rootから直接Pythonで実行しない。

```bash
cd /home/aihub_ubuntu/src/japanese-tiny-llm-10m
uv run --frozen --extra hub --extra data --extra ml --extra export scripts/webui.py --port 7860
```

GPUはWSL2のRTX4090、FP32の学習済み重み＋BF16 autocast/math attention、KV cacheを使用。checkpoint/tokenizer hashと保存tokens/updateを読み込み時に確認する。新たなexport・量子化・学習は行わない。起動中はプロジェクトのGPU lockを保持するため、次回学習時はUIを停止する。

ローカルloopbackのみで待受。画面の外部CDN/APIはなく、入力や生成文をサーバーログへ保存しない。モデルは起動時に一度読み込み、同時生成は一つ。停止操作で切断された生成は終了し、次の生成が可能になる。

## 保存と確認結果

- Windows `reports/local/webui/launcher.json` にWindows PID、`server.log` に運用ログ。
- WSL `reports/local/webui/server.json` にactual Linux PID/boot/start ticks、モデルhash、URL、実状態。
- [動作確認記録](../reports/phase6/local_webui_review.json)に実モデルAPI、ブラウザ、関連11 testsの結果。
- Edgeでdesktop1280×1040/mobile390×844を表示し、生成と停止を操作した。横方向のoverflowなし。画像はWindows `reports/local/webui/{desktop,mobile}.png`。
- 実モデルの同じseedで生成IDが一致。Greedy64 tokensは採用済み10B評価のbase-001とID完全一致。生成切断後のlock解放と次の生成成功、start/stop scriptsの動作を確認。

UIの起動依頼を完了し、サーバーはユーザーが試せるよう稼働したままにする。追加学習tokensは0。品質目標の達成、後続EOS実験やChat学習の開始とは扱わない。
