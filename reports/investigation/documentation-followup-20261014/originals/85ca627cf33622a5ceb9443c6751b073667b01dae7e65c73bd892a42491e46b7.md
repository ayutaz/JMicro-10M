# 条件保持・教材品質比較の実行記録

2026-10-05 JST。ユーザーが[計画61](61_condition_preservation_next_plan.md)の段階1〜4を再開した。保存失敗診断、同source/同量/長さ・EOS密度をそろえる約20M各pool、準備成立時の各100Mと日本語/全160内容、原gateに従う条件付き全文、判断/report/local commit/元10B UI復帰で停止する。準備条件不成立時は学習をせず準備結果を報告する。500M/1B延長・20B/50B/Chat/test/pushは対象外。

段階1実行前にWindows正本clean、元final10B UI actual359102、終了済みplan58科学239609が不在であることを確認した。旧160annotations、40教材と具体的弱例を再利用し、42生成実例を整理した。追加32教材は不要と判断。評価内容は教材へ移していない。既存200M pool内のtranslationレコードだけを入力にし、対照・候補に同じpinned source/base条件を適用した。再取得・再tokenize・主Web全走査を避け、候補だけ診断に基づく追加除外を行った。

## 実行結果と終了分岐

段階2はhidden Windows33132/actual Linux362299で実行し、prepare-jobへboot/start_ticks/bindingを保存。段階1＋builder13.752109秒で完了し、processは不在。同じ翻訳train499,066全文/140,036,743tokensから両20,000,028tokens/71,268全文を用意。長さ全並び/BOS/EOS位置一致、平均278.631251、EOS3.563395/1000tokens、共有10,155文書。

各40の無作為slotを固定し、全80に全文と個別理由を保存した。対照弱例21/40・候補12/40で、候補10/40以下を満たさなかった。CPU4tests/101準備証拠条件/10完了条件成功と、意味品質の受け入れ失敗を区別する。

計画61の準備失敗分岐に従い、段階3の各100M/一次日本語と全160/新CUDA再開、条件付き全文は未起動。科学0/検証0、新GPU評価0。元10B UIは停止せず、actual PID359102/boot53f39671-20b4-4bd5-9b9c-cd6b1e4d1bfe/start_ticks7216365、HTTP親SHA410f975d…/tokens10,000,007,168/busy=falseを完了確認で照合した。

採否・実証拠・次案は[結果63](63_condition_preservation_preparation_results.md)、[review](../reports/phase6/condition_preservation_data_review.json)、[completion](../reports/phase6/condition_preservation_completion.json)。verified local commitで今回停止し、追加選別改修・新sample・学習は開始しない。
