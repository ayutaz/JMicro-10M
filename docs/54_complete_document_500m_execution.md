# 完結文データ構成比較・実行計画

2026-10-05 JST。ユーザー「4まで計画を立てて進めてください」により、報告53の次案と直前に提示した四段階を実行する。旧計画52は完了済みで再実行しない。

1. **教材改善・準備**: 新short pool目標110M（許容100〜120M）tokens。既存train物語から低反復の全文30M、既存Web trainから短い完結文書全文80Mを選ぶ。BOS/body/EOSを丸ごと保持し、途中で切らない。物語の補助devとWeb dev/testを読み出さない。出典・実構成・長さ・EOS密度・露出率を保存し、seed20261005の一様reservoirで40件の全文を確認して開始前に採否を固定する。既存manifest/受入済みloaderを再利用し、新poolのハッシュを検査する。独立全corpus重複・混入監査は未完了のまま明記する。準備上限CPU経過1800秒、Web走査最大8B tokens（全12.23B走査はしない）。100M未満又は内容を確保できなければGPUを開始せず段階4に未成立を報告する。
2. **固定500M一条件**: 元final10BからWeb80%/short20%、追加500,006,912tokens、15259更新（stable14500/decay759）、peakLR0.0001/floor0.00001、既存context1024・batch32を維持。short消費99,975,168、科学とsave/resume検証を分ける。保存済みWeb500M/物語500M対照を再利用し、再学習しない。実save/resume検証・関連CPU checks・実量/config/sourceを凍結後に開始。一次GPU上限1800秒。実PID/boot/start ticks、log、checkpointと再開位置を永続保存。UIはGPU中のみ停止してfinally復帰。
3. **同一評価・採否**: dev本文256、同じ固定80生成、意味192/JBLiMP331/常識1119、全80内容の個別Codex採点（独立人手blindではない）。保存物語500Mの一貫性19/80から8件以上増え、対応95%下限>0、EOS37/80以上・反復18/80以下。原Web比BPB+1%以内・EOS差8以上・反復非悪化・raw失敗0等を維持。一次全通過時だけ新候補の全文89,416/生成400/長文128・512をGPU上限1800秒で実行し、親BPB+0.001以内と原全文条件を確認する。対照全文は再評価しない。未達ならその結果で判断する。gateを緩めない。
4. **報告・保存・停止**: 実データ量/学習量/品質/計算時間と採用又は不採用、限界、次の判断を保存。必要な確認を通しlocal commit、元final10B UI復帰を確認して停止。1B/20B/50B・Chat・protected test・push/publicationは開始しない。

量・内容・再使用割合が同時に変わるため「データ構成全体」の比較であり、品質だけ・独立unique量だけの因果効果とは呼ばない。Webからの抽出は既に用意した学習文書の再配分で、新規取得データではない。500M学習約12分は過去実測で、データ準備・文章確認・実装時間は別。

## 実行記録

開始時: Windows worktree clean、既存科学/evaluation processなし。元UI Linux231106（boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks4964393）だけ稼働、RTX4090使用881MiB、WSL空き509GiB。教材builderを実装して bounded extractionに進む。

初回範囲4Bでは76,773,797 tokens（story30,000,063/Web46,773,734）を44.48秒で準備し、量gate未達でGPUは未開始。CPU準備予算には十分余裕があるため、品質/量の条件を維持して未走査4B以降のみを上限8Bまで継続する。初回job/sourceとpartialを保持し、新pool indexから状態とseed付きreservoirを復元する。既存Web前半の再走査・全量走査は行わない。

段階1完了: pool110,000,202 tokens/668,680文書、story30,000,063/Web80,000,139、本文435,662,538bytes、平均body162.5035 tokens、EOS密度6.0789/1000tokens、short露出0.908863周。実抽出累計73.340秒、Web必要範囲6.84Bで終了（未走査部分だけ継続）。seed20261005の一様reservoir40全文を確認、弱例8を個別記録し、広い原文構成の研究比較として限定受入。事実正確性/全量意味品質/独立uniqueは認証しない。pool manifest SHA2d7b3d0b…、ready/samples/content-reviewをWindowsにも保存。関連CPU12tests成功、configs/phase6/complete_document_500m.json/schemaを実量・全source/参照hash付きで凍結。GPU学習はこの後開始。
