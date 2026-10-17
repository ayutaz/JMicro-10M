# Base再開: 評価入力の分離修理

2026-10-15 JST。ユーザーの「4まで進めてください」は、直前の4項目（評価の分離修理→新仮説の同10M比較→合格候補の独立学習/全文DEV→新封印TEST/採用）を指す実行再開。全体の到達範囲はBase最終判定までで、修理や一つの比較の完了だけを目標完了としない。Chat/SFT・量子化・大型化・公開は今回の範囲外。

## 最初に修理した範囲

新`evaluation_boundary`は固定hashでpinしたDEV専用manifestとそのDEV専用caseファイルだけを読む。混在`eval/base.jsonl`やTEST manifestを入口にせず、symlink・誤path・schema・split・hash・case数・identity不一致を拒否する。内容reviewも同じDEV専用入力へ照合し、旧混在全行解析へfallbackしない。

新`isolated_base_evaluation`は、そのreaderを使う将来のDEV80 greedy生成とreview provenance照合を実装。元の最大64token・特殊token抑制・raw EOS/反復/Unicode判定を維持し、不正UTF8は元bytesをhexでも保全する。CPUのdeterministic stubで検証し、実モデル能力の評価とは数えない。

旧model/training/greedy80/contentのfrozen sources、混在suite、過去の採点・数値・TEST事故は変更していない。閉じた143/144の再学習・再生成を修理の検証に使わない。旧readerは依然として旧記録の実装であり、新比較から呼んではならない。新しい実行CLIのsource/manifest pinへ接続してから次の科学比較を行う。

## 実際のDEV入力

既に全件採点・hash確認した144の保存済みDEV80 generationから、id/category/prefix/splitだけを取り出す。生成した答えを新教材や評価入力へ移さない。元の混在suite/元TESTは開かず、元DEV80の入力identity/orderを確認する。

DEV manifest SHA `6198b43df8f4cf389e9de74c038e2e93d18665413477b27359ab352a02f69fa7`、case SHA `327a76058a67b459684bdc338156e7ef09081d764e4becb8d2675685a22bf284`。場所は`eval/isolated-base-dev-v1/`。[出力記録](../reports/phase6/evaluation-boundary-20261015/dev_export.json)。

これは既知DEVの読取り隔離で、未知DEVや新しい未参照TESTを作った証拠ではない。新しい最終TESTの実体は有資格モデルと条件封印ができてから準備する。

## 確認したことと未完了

- reader CPU17 checks、生成/review接続を含む計21 checksがpassed。壊したTEST fixtureやTEST読取りの例外監視の下でDEV経路が動く。誤pin/schema/split・改変case・symlinkを拒否した。
- 生成stubで全80、EOS/role抑制、不正UTF8のraw bytes、最大長・反復を保全する動作を確認。実10Mモデルの生成や品質証拠ではない。
- 保存済み本物DEV80と新artifactの照合では、実read-setを3ファイルへ限定し、混在suite/TESTを開かないことを確認する。[読取り監査](../reports/phase6/evaluation-boundary-20261015/actual_DEV_read_boundary_audit.json)。

次の比較の介入・教師量・GPU予算・評価CLIは未選定/未凍結。Base/Chat未完成・未採用。前の不採用を取り消さず、10,001,152参照・9.5M〜10.1Mと元品質・日本語領域を維持する。

## 次の作業

既存proposal/trainer/全件notes/結果から未回答の失敗を特定し、新しい比較を1件ずつ定義する。旧条件の係数/seed/親/予算だけを救済として変えない。実行前に新source/manifest・対照・教師・指標・時間上限・採否を固定し、実CUDAのfinite/全state再開・安定batchを通す。独立学習/全文DEV/封印TESTは有資格候補ができた場合のみ。

新しい条件の閉鎖と全体のBase到達目標を区別する。実測と根拠で実行契約を定義し、routine判断に再開許可を繰り返し求めない。必要な外部判断・hardware/credentials・範囲や資源の変更が発生した場合は、具体的な証拠と理由を示す。

## 2026-10-15 全文DEV集計と440生成の接続部品

[CPU完了記録](../reports/phase6/isolated-full-dev-preparation-20261015/completion.json)。`src/jmicro/isolated_full_dev.py`はDEV専用manifest/本文shardを固定して全本文を採点し、既存400+長文40の生成adapterを呼ぶ。本文損失は共通の総バイト数でBPBへ換算し、EOS損失は分ける。全件数に加え、元索引の各文書ID・本文token・bytesを照合する。実プロジェクトの全文identityは89416文書/42003934本文token/164344743bytesに固定し、合成fixtureや256件では全文実行を主張できない。

合成2文書と決定的CPUモデルの36 checksが合格。1100token文書で元1024/512窓を越える採点と解析NLL/EOS oracle、全440 raw、同fixtureの固定80照合、偽TEST/train/従来の混在sibling読取りと評価中書込みの拒否、部分集計/重複/改変/失敗隠蔽の拒否、期限/乱数/モード/forward hook復旧を確認した。読取りガードはPythonのopen監査で、native libraryを含むOS sandboxとは主張しない。初回29passとsource/XML、拡充後36passを保全した。

全suiteの六ID抑制と新pilotのEOT7も含む七ID抑制は維持。固定80の違いは失敗情報と全rawを返し、decoderを揃えて一致を作らない。文字不正/UNK/role/停止失敗も保存する。固定80の一致だけで品質合格にはしない。

これはraw評価の部品である。資格と真の独立全pipeline学習を検証する永続native runner、GPU lock/実測予算/保存と内容reviewへの接続は未完成。実model/checkpoint・実DEV本文/cases・TESTを開いた評価、実440生成、独立学習、新TEST/採用は実施していない。新GPU/学習0、元10M/既存生成sources不変、元UIの現在生存はこのCPU作業では確認しない。次のGPU比較は未選定で、元総/技術台帳を引き継ぎ、根拠と実測予算が成立してから別契約を凍結する。元4項目goalは未達である。