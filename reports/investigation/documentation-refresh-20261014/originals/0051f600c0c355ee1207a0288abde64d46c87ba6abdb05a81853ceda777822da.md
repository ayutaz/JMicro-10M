# 自然短文の学習診断から教材比較・条件付き拡大まで

2026-10-05 JST。ユーザーの「4まで進めてください」は直前の四段階を再開する。目的は、記憶用教材だけの成功と自然文への汎化を分け、意味の通る展開と自然停止の改善条件を見つけること。

1. Codex作成の意味/対象/指示/因果を確認した日常32scene、各二人の64全文を固定。続きを一意にするprefixは第一文＋保護newline。未学習の別名128全文は学習へ入れない。展開用train1000全文も同時に固定し、32sceneの語彙置換なので一般日本語の多様性を保証しない。template全文の人手独立認証はなくCodexの内容確認。source/語彙/構文の限界を報告する。全て128input以内、gold続き＋EOS64以内、切断しない。
2. 同じ元10B重み、同じisolated文書256×128、Adam引継ぎA/fresh Bの各8,000,000本文/EOS教師。PAD/BOSを学習量に算入しない。LR1e-4、教師90%stable/末尾10%decayで共通。teacher正答/greedy gold完全再現/EOSで適切に完結するtrain割合が各90%以上で記憶診断合格。64件で最低58件の完全再現が必要。適切完結はこの一意の記憶課題ではgold完全再現＋EOSで保守的に測る。devは参考として別に残す。合格枝は完全再現、teacher正答、同点はinheritの順で選ぶ。両失敗なら新規重み/fresh AdamのCを8M、LR1e-3で陽性対照に使う。Cは重み/LRとも変わり純粋な重みの因果ではない。GPU占有は再開検証/診断/評価含め600秒。
3. 合格したoptimizer方針で元10Bから開始し、従来compact1000全文と自然文1000全文を各25,000,000本文/EOS教師で比較。Web20M/short5Mを同じ元Webcursorから学習、双方whole-document shuffleを使う。重み/教師予算/混合教師比率/境界処理を揃える。短文のsource/長さ/EOS密度/固有tokensは異なるため、量だけ/品質だけの因果とは呼ばない。診断64はnatural1000のsubsetで記憶の持込みを避け、元10Bから新しい二枝。両終端で共通dev256BPB、固定dev80全文、意味192/JBLiMP331/JCQA1119を測り、全160自由生成に個別理由を付ける。GPU占有上限1200秒。
4. 段階3が全既存gate（一貫性差+8/80、対応95%下限>0、coherence/適切完結各27/80、EOS37/80、重度反復18/80以下、empty/role/UTF8なし、比較BPB1%以内、旧Web adoption_checks）を通った場合だけ、固定した自然train1000に、別の氏名256人×32sceneの自然8192全文を追加し、同じchosen checkpointからWeb80M/short20Mの追加100M教師で拡大する。固有教材増量は1000→9192（32sceneは共通で構文の多様性は増えない）と明記し、100Mは消費教師量。一般公開corpus全量の増量とは呼ばない。既存品質gateで元段階3対照と再評価し、採用は原品質基準を保つ。GPU占有上限1200秒。失敗の場合は拡大非実行の採否/次案まで報告して停止する。

計科学教師上限174M（A/B16M+C条件付き8M+比較50M+条件付き拡大100M）。検証更新/教師は別会計。学習コードは旧frozen packing trainerを保持して新subclassで初期Adam stateだけ切替。新optimizer方針の実CUDA連続/再開を各4更新×二走行で照合する。既存全検証/corpushash/dedupは再実行しない。bf16の結果72の許容外は未解決として保持し、今回の数値合格へ書き換えない。

checkpoint/config/data/source SHA、optimizer/scheduler/RNG/sampler教師cursorとphysical/PADを保存。実PID/boot/start/log/lockで単一起動、停止/失敗の両方で元UIへ復帰。途中の失敗は有効completed checkpointから再開し、終端は再実行しない。評価後に内容確認が必要な境界でjobを終端化し、reviewを保存してから段階4を分岐する。教材/条件/gateを結果に合わせて変更しない。local commit後停止、push/20B/Chat/test/外部公開はしない。
