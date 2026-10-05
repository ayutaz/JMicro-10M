# 多様な完結文の準備・同量比較・条件付き拡大

2026-10-05 JST。ユーザーの「3まで進めてください」は結果74の次案①〜③を再開する。今回はモデル10,001,152paramsと元10Bを保持し、32場面の名前置換教材から、場面・語彙・構文の異なる既存の実文書へ移す効果を調べる。

1. 既存complete-documents-20261005の固定Web train全文（元FineWeb2日本語）から、切断せず10,000異なる本文・準備1M tokens以上を新しい小poolへ保存する。source manifest/元span/canonical hashを記録。sourceは元10Bにも含まれるので新取得や初回学習とは呼ばず、短文の再配分。64〜256body tokens、2〜8完結文、日本語比率、案内/広告/一覧の除外、文間の対象/接続の確認proxy、局所exact重複だけ。最大300,000Web文書の単一走査・CPU600秒。全12B照合/旧index独立監査はしない。固定seed75で新poolから64全文を選んで全て読み、対象/否定/時系列/完結の弱例10/64以下を学習前の準備gateとする。再抽選/評価後のselector調整なし。題材/構文の多様性は原文と分布から説明し、10,000種類の構文を独立認証したとは呼ばない。

   専用devは既存Web devから固定80の本文とは別の64文書を用意する。trainは直接引用「」と明示条件（もし/場合/たら/なら）を除外し、devは引用32・明示条件32を別構造として保持する。単なる別名devにしない。devは親の公式trainと分離し、新poolやWeb trainへ混ぜない。構造を選ぶ用途でdevのモデル成績を用いない。全dev64を本文BPBとEOS教師尤度で評価する。この限定的な未学習構造の診断を日本語全般のtestと呼ばない。固定suite/testの本文を教材へ混ぜない。

2. 準備gate合格後、今回の自然1000全文（32場面）対新自然10,000全文を、同じ元10B・Adam引継ぎ・文書単位shuffle・LR0.0001（教師90%stable/10%decay）・Web80M＋short20Mの各100M本文/EOS教師で比較。BOS/PADを教師量へ入れない。元Web cursorと教師量を揃える。source/長さ/EOS密度も変わるため純粋な量だけの効果とは断定しない。新poolで実CUDAの連続4更新対2→保存→2のmixed shuffleを一度確認し、検証8更新の教師は別会計。旧全tests/benchmarksは繰り返さない。各終端で共通dev256BPB、意味192/JBLiMP331/JCQA1119、専用dev64BPB/EOS、固定dev80greedy64を実評価し、全160生成を原文へ結び付け個別採点。GPU占有上限1200秒、各学習600秒。実測参考は結果74の各25M学習39〜51秒・二枝学習評価298秒。

3. 全既存gate（対応一貫性増加8/80・95%下限>0、一貫性/適切完結各27、EOS37、反復18以下、empty/role/UTF8なし、同量対照BPB+1%以内、旧Webadoption_checks）に合格した場合のみ、同じ凍結selectorで未走査Web trainから40,000以上の異なる完結文を追加し、計50,000以上・準備5M tokens以上へ増量する。新64全文の内容gate10弱以下を保ち、不合格なら拡大しない。同じ候補終端からWeb400M＋short100Mの追加500M教師を学習し、同じ日本語/専用dev/80生成/原品質gateを元段階2対照と比較する。GPU上限1800秒、準備追加600秒。科学教師上限700M、検証教師別。量が足りなければ原因と非実行を保存し、名前置換や単なる複製で代替しない。

準備/比較/拡大のいずれかが固定gateを通らなければ、その分岐の採否と残る原因を報告し、結果・local commit・元UI復帰後停止する。教材/gateを結果に合わせて変更しない。品質改善と証拠検証成功を区別し、結果72の数値7失敗を保持する。

新しいrunner/config/関連CPUtestsを作り、旧凍結trainer/evaluationを再利用する。source/config/data/checkpoint SHA、optimizer/scheduler/RNG/sampler、教師/valid/physical/EOS/bytesと実PID/boot/start/logを保存。重複GPU起動なし、完了runは再起動せず、有効checkpointからのみ復旧。各GPU終端で元10B UIへ復帰する。uv Python3.12.7、WSL disk/RTX4090。20B/50B/Chat/保護test/push/公開は対象外。
