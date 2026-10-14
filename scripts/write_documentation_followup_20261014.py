"""Apply human-authored current explanations; retain technical histories via snapshot."""
import json
from pathlib import Path
import re
import sys

ROOT=Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m')
sys.path.insert(0,str(Path(__file__).resolve().parent))
from documentation_followup_20261014 import RUN,LIVING,WSL,mirror,anchors

SCOPE='更新: 2026-10-14 JST。現在の依頼は全現行文書の最新化と今後の計画作成。Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は再開していない。'
STATE='最新Baseの文書長重み100Mは不採用で閉鎖。一貫性1/80・反復50/80、独立fresh学習seed43/fullDEV/封印TEST/採用は有資格候補なしで未実行。比較・文書の完了はモデルの品質完成ではない。'
TEST='元Base TEST20 promptと元Chat TEST20行は別のCPU解析問題を保存した。学習・GPU TEST採点に使っていないこととCPU未解析は別。将来の有資格最終確認にはreader分離と新しい封印TESTが必要。今回data/TESTを開封・再処理しない。'
PLAN='次は評価の読取り分離を修理し、既存結果から未回答の比較1件を定義する計画。介入・教材量・GPU予算は未選定/未凍結。真にfreshな独立Baseの全pipelineとnative runnerの接続、fullDEV/全440生成、新しい封印TESTを省略しない。'
NUM='同10M・元10B親・同accepted TRAIN/教師/seed/batch/optimizerで、文書長によるCE寄与だけを変更。実17,698更新・100,000,000教師、全80理由付き判断、共通DEV256/Japanese192/331/1119を確認した。新GPUは科学1,474.808693＋技術8.721357＝1,483.530050秒。技術47更新/273,521教師は品質/本学習へ加算しない。'
TOPICS={
'data/README.md':'元Web TRAIN12,225,819,077 tokens、accepted混合2B、後続SFTは別系列。最新Baseはaccepted75/20/5の同100M教師を消費し、新規教材0。dataset実体・sampler全state・重みはWSLに保全、Windows/Gitのportable reportを厳密再開の代替にしない。ChatのTRAIN41,529 target/660,109教師/周と実1,899,557教師は別の量。',
'eval/README.md':'v1 Base/Chat各DEV80/TEST20の原suite/hashは維持する。既存Base greedy80と内容reviewは混在suite全行をJSON解析してからDEVを抽出するため、元Base TEST20 promptを未参照とは呼べない。旧protected_test_used=falseはGPU TEST採点なしの記録で、CPU未開封の証明ではない。旧sourceと結果を保全し、将来のDEV経路はTESTファイルを開かない契約にする。',
'reports/README.md':'最新の完了結果はBase143/144。元10B、teacher-decay2B、文書長100M、各SFTは異なるrunで、教師量を合算しない。最終native checkpointはWSLのdocument_balance/checkpoint-00017698.pt。Windowsには40件のmetadata/source/evaluationを保全し、samplerを省いたportable viewと原native bytesを明確に区別した。結果commit1901564/receipt fc1a3fcの93Git内容照合は当時の保存の証拠。',
'docs/01_project_goal.md':'最終成果物はJMicro-10M-BaseとJMicro-10M-Chat。日本語corpus選別→独自Tokenizer→ランダム初期化/スクラッチBase→Dialogue-oriented mid-training→Assistant本文+EOT SFT→量子化/ローカル利用という元目標を維持する。約10M、日本語Baseと短い会話の原品質・領域を変えない。合格Baseで通知停止し、Chat/量子化は別の再開段階。',
'docs/02_research_summary.md':'現参照はnative10,001,152、Tokenizer4096、NoQK-Norm/SwiGLU/13層/context1024。Layer Sharingの固定比較は不採用、ReLU²は予算gate不成立で本比較未開始のまま閉鎖。過去案を未検証の次候補へ戻さない。SFT低LR141も不採用で、追加SFT・Base単独原因・10M容量限界はいずれも解決の証明がない。外部研究は当時の記録で最新revisionを再調査していない。',
'docs/03_architecture.md':'現参照はnative10,001,152 parameters、4k NoQK-Norm/SwiGLU/13層、hidden256/FFN640、GQA4Q/2KV/context1024。今回144はloss配分だけでarchitectureを変えていない。総trainable9.5M〜10.1Mを維持し、構成配分変更は別proposal・別source・同予算比較を要する。src/jmicro/model.pyのfrozen SHAを上書きしない。下の初期T8K/QK-Norm/ReLU²/共有案は当時の設計記録。',
'docs/04_tokenizer.md':'固定4096 Tokenizerと特殊ID0〜7を維持。4k/8kの既存比較・Phase3変換は基盤の証拠で、再学習や再exportを今回繰り返さない。モデル実験は同Tokenizerとcommon-byte BPBを使う。raw不正UTF8はモデル失敗として保全し、置換表示や制約decodeで免除しない。',
'docs/05_dataset.md':'accepted TRAINとDEV/TESTの分離、元source/manifest/Token量・重複/反復の区別を維持。最新Base100Mは既存accepted2B poolの再利用で、新しい100M教材を増やした実験ではない。全件独立corpus auditは未完了。評価readerの混在TEST解析とcorpus split品質は別の課題で、同じ未開封フラグでは代用しない。',
'docs/06_training_plan.md':'Base/Chat trainer、shard/document sampler、元教師mask、全state保存再開は実装・実GPU実行済み。最新Baseは同accepted TRAIN・fresh AdamW LR1e-5/WD0.1・batch48・BF16/Flash学習、math評価で正確100M。closed条件のLR/量/shapeを次案の推奨値にしない。Dialogue-oriented mid-trainingと正式Chat完成は未実施。独立Baseは別initial weightsと学習/material RNGを含む全pipelineが必要。',
'docs/07_environment.md':'WindowsがGit正本、WSLが実行/weights/sampler/dataの保存先。Python3.12.7/uv、WSL2/Linux/RTX4090を維持。最新Base probeは最大48×1024、peak allocated10,705,060,352bytes、CUDA47技術更新の全state再開一致を確認した。実GPU総1,483.530秒はこのrunの値で、旧Flash/compile694,521入力tokens/秒や次のfresh全pipelineの速度へ読み替えない。driver/package/空き容量/PIDは最後の観測で現在の保証ではない。',
'docs/08_evaluation.md':'最新Baseは全80のprefix/全文をCodex非blindで理由付き採点。文法23、一貫性1、適切完結2、EOS20、反復50（各80）で不採用。原DEV絶対・相対CI・strong/cached/historical保持を維持。Chat141の28セット/6,132判断/NLL7点は別の評価契約。全文DEVとDEV256、独立学習と生成seed、人間blindとCodex判断、TEST CPU解析とGPU採点を区別する。',
'docs/09_prior_art_and_baselines.md':'外部model card/論文は2026-10-02等の調査時点の記録。今回最新revision/規模/利用条件を再調査していない。外部model名の10Mや内部block規模を総trainable予算と混同せず、同条件品質比較は未実施のまま。10M維持、領域/品質維持を前提に、closed比較の機序を原実装まで確認して新案を選ぶ。',
'docs/11_technical_research_gaps.md':'現在の優先課題は、混在DEV/TEST readerの修理、未回答の比較の選定、真にfreshな独立Base全pipeline、native fullDEV/TEST typed接続、全内容レビューの証拠。文書長重みは一貫性2→1/80・反復45→50/80で不採用。データ/目的/最適化の単独原因は未確定。CPU fixturesや準備済みfactoryを品質・独立学習の完了にしない。',
'docs/12_training_implementation_research.md':'現行nativeはNoQK-Norm/SwiGLU/13層/10,001,152。最新Base100Mは同教師stream/digest、元文書の本文+EOS全位置の逆長重み、全updateの重み平均/比率、モデル/Adam/scheduler/RNG/sampler/countersを監査して不採用。native独立学習のfactoryと最終runner接続は別の状態形式で、旧stable+decayへkindを偽装しない。今後必要CLIを実装・CPU/CUDA再開を確認してから学習する。',
'docs/13_tokenizer_dialogue_data_research.md':'Tokenizer4096、構造tokenの挿入、Assistant本文+EOTのみの教師mask/document samplerを維持。SFTは141まで実行・不採用で、今回は追加教材・mid-training・SFTを始めない。ChatのTEST20行解析とBaseのTEST20 prompt解析は別の事故で、将来両方の有資格確認には新しい封印TESTが必要。dataset量の初期案を実準備済み量や開始指示にしない。',
'docs/14_evaluation_deployment_research.md':'正式品質は未採用。最新Base144は100M/全80/共通byte・日本語評価と全guardで不採用、Chat141も全28セットで不採用。Phase3のHF/native float GGUF・量子化型/容量・CPU変換確認は基盤であり、学習済み量子化品質や配布完成ではない。採用floatとの品質退行・実容量・独立環境を別段階で確認する。',
'docs/huggingface_handoff.md':'2026-10-09の主要3Base系列の公開保存は126の当時の記録。後続SFTや文書長重み100Mは未公開。dataset/samplerを含まない公開保存はnative完全再開の代替ではない。最新localBase納品は1901564/fc1a3fcで、旧push許可を今回は引き継がない。pinned pilot/Tokenizerのrevision/hash・復元条件は維持する。',
'docs/base_experiment_lookup.md':'Baseの最新固定不採用は143/144、前回teacher-decayは123。後続Chat136/138/141も不採用。20261008索引は当時の検索補助で、144や後続Chatまでの網羅的な現行監査ではない。今回は索引生成・全corpus scan・旧GPU再評価を実行しない。次案は原proposal/trainer/結果を対応付け、検索語がないことだけで未検証と断定しない。',
'docs/43_local_webui.md':'元10B BaseのURLはhttp://127.0.0.1:7860。新しいBase/Chat候補へ置き換えていない。最後の納品観測は2026-10-14T07:30:16Z、PID338403/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60473641、元親/Tokenizer/10M/idleを確認した。現在の生存保証ではなく、今回の文書作業ではHTTP/GPU診断・生成・再起動をしていない。次の操作時に実identity/HTTP/lockを照合する。',
'docs/124_base_recovery_plan.md':'元の段階0〜5は維持し、実行の詳細は計画145へ接続する。143/144の一巡は不採用で停止、前の「6まで」は未達/blocked後にユーザーが解除。新しい介入は未選定。次の実行契約で一巡か定義済み複数比較か・総予算・ゴールを明記する。今回の文書依頼は新しい研究cycleの再開ではない。',
'docs/125_project_retrospective.md':'このliving総覧は最新Base144と前回Chat141を入口にする。全体Base/Chatは未完成・未採用。「6まで」は有資格候補なしで未達/blocked後に解除。固定retrospective台帳・dated reports・旧SHA/採否は当時のrevisionを保つ。全文の再集計や科学記録の上書きを今回行わず、新結果のscope・未実施を別に追加する。',
'docs/126_model_archive.md':'2026-10-09の主要3Base系列・共通Tokenizer・数値学習状態のpublic/manual-gated保存は当時の記録。dataset/sampler除外でnative厳密再開の代替ではない。後続Chatと文書長重み100M候補は未公開。今回はHub照会・設定変更・push/公開なし。1544files/396038805bytes/revision853d52d2323653331b610249912fbe25615615fcという保存契約は維持する。',
'docs/retrospective/README.md':'固定台帳は生成した当時のGit revisionと実験集合を保持。living入口だけを最新Base144/前回Chat141/計画145へ接続し、fixed coverage/experiment_records/source SHAを現在へ書き換えない。原台帳以後の新しい100Mと未達/blockedを当時の集計へ混ぜない。',
}


def old_text(name):
    baseline=json.loads((RUN/'baseline.json').read_text())
    entry=next(r for r in baseline['documents'] if r['path']==name)
    return (ROOT/entry['snapshot']).read_text(encoding='utf-8-sig')


def links(name):
    prefix='../docs/' if not name.startswith('docs/') else ('../' if name.startswith('docs/retrospective/') else '')
    if name=='README.md':prefix='docs/'
    return f'[最新Base結果144]({prefix}144_base_document_balance_results.md) / [前回Chat結果141]({prefix}141_chat_lr_comparison_results.md) / [次の計画145]({prefix}145_post_rejection_next_plan.md) / [今回更新146]({prefix}146_documentation_followup.md)。'


def update_generic(name,topic):
    old=old_text(name)
    title=old.splitlines()[0]
    marker=next((m for m in ('## 当時の資料・保存手順','## 作成時点の資料・契約') if m in old),None)
    if marker:
        tail=old[old.index(marker):]
    else:
        position=old.find('\n## ')
        tail=old[position:].lstrip() if position>=0 else ''
        if tail:tail='## 更新前の本文・契約（当時の記録）\n\n'+tail
    new='\n\n'.join((title,SCOPE,links(name),topic,STATE,TEST,PLAN,tail)).rstrip()+'\n'
    if name=='eval/README.md':
        new=new.replace('元Base TESTはこの事故では解析していない。','元Base TESTはそのChat事故では解析していないが、後続144のBase readerでCPU解析された。')
    if name=='docs/124_base_recovery_plan.md':
        new=new.replace('このBase復旧は未再開・介入未選定。','当時はBase復旧未再開・介入未選定。その後143/144を実行・不採用で閉鎖。')
    write(name,new)


def write(name,body):
    target=ROOT/name
    target.write_text(body,encoding='utf-8',newline='\n')
    # Preserve original incoming fragment aliases when current headings change.
    original=old_text(name)
    original_slugs=set()
    # Reuse the exact slug contract used by prior document verification.
    entry=next(r for r in json.loads((RUN/'baseline.json').read_text())['documents'] if r['path']==name)
    original_slugs=anchors(ROOT/entry['snapshot'])
    missing=sorted(original_slugs-anchors(target))
    if missing:
        body+='\n<!-- Original heading aliases retained for historical incoming links. -->\n'
        body+='\n'.join('<a id="'+x+'"></a>' for x in missing)+'\n'
        target.write_text(body,encoding='utf-8',newline='\n')
    mirror(target)


def main():
    for name,topic in TOPICS.items():update_generic(name,topic)
    # Main status: preserve actual science, replace current scope/obsolete liveness.
    name='docs/autonomous_status.md';old=old_text(name)
    old=old.replace(old[old.index('更新:'):old.index('\n\n最新の')],SCOPE+'\n\n'+links(name)+'\n\n前の「6まで」は未達でblockedとなり、ユーザーが解除した。今回の新しい目標は文書/計画のみで、学習再開ではない。')
    old=old.replace('ローカル納品検証を終えたら報告停止する。','結果commit1901564/receipt fc1a3fc、93Git内容・40保全file・232local linksの納品照合は完了。元UI確認は当時の観測で現在保証ではない。')
    start=old.index('最新の保存された科学観測2026-10-13')
    end=old.index('\n\n最新S1は',start)
    old=old[:start]+'最後の納品観測2026-10-14T07:30:16Zは元10B UI PID338403/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60473641、元親/Tokenizer/10M/idleを確認。現在の生存保証ではない。文書更新では再診断・再起動していない。'+old[end:]
    old=old.replace('最新S1はWSL','前回Chat S1はWSL')
    old=old.replace('今回の比較・必要な条件分岐・保存結果を報告して停止する。','今回の文書・計画・保存検証を完了して通知する。次の研究の順序と終了範囲は計画145を正とし、再開は別の明示指示。')
    write(name,old)
    name='docs/10_next_steps.md'
    write(name,'# 現在のチェックリスト\n\n'+SCOPE+'\n\n'+links(name)+'\n\n'+STATE+'''\n\n## 完了した最新Base比較

- [x] 同10M・同親/TRAIN/教師/seed/batch/optimizerで文書長重み1条件を凍結。
- [x] CPU21 checks、CUDA47技術更新、最大shape・全state再開を確認。
- [x] 正確100M/17,698更新、全重み・counter・対照sampler/digest・予算を監査。
- [x] 全80理由付き内容、DEV256/Japanese192/331/1119、全原guardを判定。不採用で閉鎖。
- [x] 本比較延長・独立seed/fullDEV/封印TEST/採用の5分岐を未実行・品質未確認と記録。
- [x] Base TEST20 prompt CPU解析問題と、学習/GPU採点なし・TEST shard未開封を区別して保存。
- [x] 結果1901564/receipt fc1a3fcの93Git内容、40保全file、232linksの納品確認。

## 再開後に必要な成果物（今回未実行）

- [ ] DEV/封印TESTの別artifact/reader/manifest、誤読取りを拒否するCPU証拠。
- [ ] 新しい仮説1件または根拠不足の選定メモ。一巡/複数比較・総予算・ゴールの明確化。
- [ ] 必要CLI/最小診断・実CUDA再開・安定batch・同条件pilotと本比較。
- [ ] 原品質/全保持に合格したrecipe。
- [ ] 真にfreshな独立学習seed43と全pipeline/runner接続。
- [ ] fullDEV、全400生成＋長文40、必要な人間blind・corpus監査等の未確認証拠。
- [ ] 選定封印後の新しいBase TEST・全件判定・採用・復旧。
- [ ] 別の再開指示後のChat/Dialogue/SFT・量子化/利用。

## 不変条件と停止境界

9.5M〜10.1M、参照10,001,152、元の日本語Base/Chat品質・領域を維持。大型化・閾値緩和・領域縮小で達成扱いにしない。各不採用条件を閉じ、条件分岐の完了を未実施の独立学習・最終TEST・Base完成にしない。今回の文書作業だけで研究/GPU/data/TESTを開始しない。
''')
    name='docs/codex_automation.md'
    old=old_text(name);tail=old[old.index('## 保存と再開'):]
    tail=tail.replace('終了したpilot/128/131/133/135/139','終了したpilot/128/131/133/135/139/143')
    write(name,'# 自律runnerの現在の運用\n\n'+SCOPE+'\n\n'+links(name)+'\n\n'+STATE+'''\n\n## 実行範囲と目標状態を区別する

文書依頼を研究再開と扱わず、古いrunning/PID/next_actionを起動指示にしない。現在の目標は文書/計画の完了。以前の「6まで」は品質未達でblocked、ユーザーが解除済み。今回をその再開・達成としない。

`continue`は許可範囲の有用な作業が残る、`needs_user`は外部操作が必要、`complete`は依頼範囲が証拠で完了した状態。比較作業の完了とBase/Chatの正式採用は別。有資格候補なしの後続は未実行/品質未確認。

有効な長期process/sessionを実identityで確認したpollはverified wait。終了・handle不在が確認されるまで観測timeoutだけでrestartしない。結果の説明や未実行計画だけのturnは進捗ではない。真の同じ外部blockerが3連続goal turnで確認され、許可範囲で有用な作業ができなければgoalをblockedにする。最初のblockで完了/blocked/自主pauseにしない。userが解除・別目標へ変更したら旧確認を繰り返さない。

再開時の契約で一巡/定義済み複数比較と総予算を明記し、範囲内のroutine判断は再確認せず進める。未承認の新cycle、外部公開/送信、有料cloud、OS昇格等の境界は守る。
\n'''+tail)
    name='docs/evaluation_protocol.md';old=old_text(name)
    title=old.splitlines()[0];tail=old[old.index('## v1契約と後続実験を区別する'):]
    tail=tail.replace('最新139は','前回Chat139は')
    tail=tail.replace('元Base TESTはこの事故では解析していない。','元Base TESTはそのChat事故では解析していないが、後続144のBase readerでTEST20 promptがCPU解析された。未参照とは呼ばない。')
    write(name,title+'\n\n'+SCOPE+'\n\n'+links(name)+'\n\n'+NUM+'\n\n'+TEST+'''\n\n## 現行のBase採否と読取り境界

最新Baseは文法23/80、一貫性1/80、適切完結2/80、EOS20/80、反復50/80で不採用。原DEVの文法56/80・一貫性/適切完結27/80・EOS37/80・反復上限18/80・文字等0、元相対CIと全保持guardを維持する。最終TEST停止95%等の条件はDEV screenで代替しない。

DEV経路で封印TESTファイルを開かない。CPU構文解析・学習使用・GPU採点・人間参照は別の証拠にする。旧混在suite/hashと結果を保存し、新しいfinal TESTは有資格recipeと選定封印後だけ準備する。今回その内容やdataを解析しない。
\n'''+tail)
    for name in ('README.md','docs/README.md','docs/15_project_roadmap.md','docs/windows_handoff.md'):
        old=old_text(name)
        new=old.splitlines()[0]+'\n\n'+SCOPE+'\n\n'+links(name)+'\n\n'+STATE+'\n\n'+PLAN+'\n\n'
        if name=='README.md':
            new=old.splitlines()[0]+'\n\n約1,000万パラメータで、日本語の短い文章を自然に続け、その後に短い会話を行うモデルを目指す研究プロジェクトです。Tokenizer・モデル・学習評価基盤をスクラッチで構築し、10Mの小ささと元の品質目標を維持します。\n\n'+new.split('\n\n',1)[1]
        tail=old[old.find('\n## '):].lstrip()
        if name=='README.md':
            tail=tail.replace('次のBase復旧は[124](docs/124_base_recovery_plan.md)の未再開の別経路です。','Base復旧124の後に143/144を実行し不採用で閉鎖しました。次は[計画145](docs/145_post_rejection_next_plan.md)で、今回の文書依頼は研究の再開ではありません。')
        if name=='docs/README.md':
            tail=tail.replace('6. [全文書カタログ](document_catalog.md)：311既存文書と今回追加2文書の全件区分。','6. [全文書カタログ](document_catalog.md)：更新前626パス・33現行/282履歴/311原文copyと今回追加2文書。')
            tail='## 今回の文書と計画\n\n[145: 次の計画](145_post_rejection_next_plan.md) / [146: 全文書更新記録](146_documentation_followup.md)。旧141/142は前回の結果・更新記録、143/144は最新Baseの凍結計画・結果として保全。\n\n'+tail
        if name=='docs/15_project_roadmap.md':
            tail=tail.replace('最新139の新GPUは','前回Chat139の新GPUは')
            tail=tail.replace('最新の同native2B比較では','以前の同native2B比較では')
            tail=tail.replace('限定Chat診断と教材/低LR比較は141まで完了したが','限定Chat診断と教材/低LR比較は141、Base文書長重みは144まで完了したが')
            tail=tail.replace('次の介入は既存証拠から別の明示再開時に選定・凍結する。','次の介入は計画145の評価隔離修理・既存証拠照合と、別の明示再開時の契約で選定・凍結する。')
        if name=='docs/windows_handoff.md':
            tail=tail.replace('## 閉じた最新runとUI','## 前回Chatの閉じたrunと当時のUI')
            tail=tail.replace('## Git外で保全する重みと教材','## 前回Chatと旧BaseのGit外保全')
            tail='## 最新Baseと最後の観測\n\n'+NUM+'\n\n最終候補はWSL `reports/phase6/base-document-balance-comparison-20261014/document_balance/checkpoint-00017698.pt`、SHA `d89caf23bd7d2d8d81f298cb6f1fcbfe5fbd581105f91be1c3cfc18cefc9f86b`。full state/sampler/metricsはWSL、Windowsはportable viewと40保存file。結果1901564/receipt fc1a3fcの保存確認済み。\n\n最後のUI納品観測2026-10-14T07:30:16ZはPID338403/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60473641、元親/Tokenizer/10M/idle一致。現在保証ではなく、今回はprocess/HTTP/GPUを再診断していない。\n\n'+TEST+'\n\n'+tail
        write(name,new+tail)
    name='AGENTS.md';old=old_text(name)
    tail=old[old.index('## Fixed model-size requirement'):]
    write(name,'''# JMicro-10M development and training

Read docs/autonomous_status.md, docs/15_project_roadmap.md and docs/windows_handoff.md before continuing. Actual latest Base evidence is result144; next plan is docs/145_post_rejection_next_plan.md; document coverage and delivery are in docs/146_documentation_followup.md and docs/document_catalog.md. Plans are not execution authorization.

## Current scope — 2026-10-14 JST: documentation and planning only

The user cleared the blocked, unachieved "6まで進めてください" goal and requested updating all documentation and planning the next work. Inventory every Markdown/RST including provenance copies, update all living explanations, preserve frozen/dated evidence and original bytes, verify local links/Windows-WSL/Git delivery, and commit locally. No research implementation, diagnostics, data/TEST preparation, inference/evaluation, GPU training, old-job restart, dependency/environment work, push/publication or quantization is resumed. Do not repeat the superseded research-resumption question during this documentation goal.

Latest document-length-weighting Base pilot144 completed exact100M/17698 updates, all80 individually reasoned DEV outputs, common-byte/Japanese evaluations, complete-state/update/weight/source/sampler/budget checks and rejected the recipe. Model quality and the former six-stage goal remain unachieved. Main extension, genuinely fresh trainedseed43, fullDEV/400+40, sealedTEST and adoption are unexecuted, passed=false, quality-unconfirmed. Source result1901564/receipt fc1a3fc were verified; stored records describe those revisions, not current living-document hashes.

Preserve the separate original Base TEST20-prompt CPU parsing exposure and prior Chat TEST20-row preparation exposure. Neither was used for learning or GPU TEST scoring, but cannot be called CPU-unopened. Base TEST shards were not opened here. Future qualified final verification requires isolated DEV/TEST readers and fresh sealed cases; do not prepare/parse replacements during documentation or with no eligible candidate.

Original10B WebUI was last verified2026-10-14T07:30:16Z as PID338403/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start60473641, correct parent/Tokenizer/10M/idle. This is recorded evidence, not current liveness. Preserve native full weights/samplers/metrics and all older lineages in WSL; datasets/weights/samplers are not copied into Git. Never relaunch rejected or completed jobs.

Any future Base resumption follows plan145: first repair evaluation reading boundaries, define one evidence-grounded independent comparison and its approved scope/budget. If explicitly authorizing multiple bounded comparisons, continue routine authorized work without renewed approval; otherwise obey the frozen failure boundary. Preserve10M, original quality/domain, independent fresh learning/fullDEV/finalTEST. Finish a qualified Base, notify and stop; Chat/SFT/quantization/publication need separate resumption.

Original operative documents and all current source/provenance paths are preserved in reports/investigation/documentation-followup-20261014/baseline.json. Dated reports and scientific receipts must not be rewritten to make them describe later document changes.

'''+tail)
    assert set(TOPICS)|{'docs/autonomous_status.md','docs/10_next_steps.md','docs/codex_automation.md','docs/evaluation_protocol.md','README.md','docs/README.md','docs/15_project_roadmap.md','docs/windows_handoff.md','AGENTS.md'}==LIVING-{'docs/document_catalog.md'}
    print(json.dumps(dict(living_bodies_updated=32,scientific_data_or_GPU_work=False)))


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7)
    main()
