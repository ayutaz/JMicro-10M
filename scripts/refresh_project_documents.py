"""Inventory, preserve and verify the documentation-only 2026-10-14 delivery.

No training, inference, dataset parsing, model loading or external publication.
Windows is authoritative; use this script through the pinned WSL uv environment.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote

ROOT = Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m')
WSL = Path('/home/aihub_ubuntu/src/japanese-tiny-llm-10m')
RUN = ROOT / 'reports/investigation/documentation-refresh-20261014'
GIT = '/mnt/c/Program Files/Git/cmd/git.exe'
WIN_ROOT = r'C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m'
OPERATIVE = {'AGENTS.md','README.md','data/README.md','eval/README.md','reports/README.md',
    'docs/README.md','docs/autonomous_status.md','docs/15_project_roadmap.md',
    'docs/10_next_steps.md','docs/windows_handoff.md','docs/evaluation_protocol.md',
    'docs/codex_automation.md','docs/huggingface_handoff.md','docs/base_experiment_lookup.md',
    'docs/43_local_webui.md','docs/124_base_recovery_plan.md','docs/125_project_retrospective.md',
    'docs/126_model_archive.md','docs/retrospective/README.md',
    'docs/01_project_goal.md','docs/02_research_summary.md','docs/03_architecture.md',
    'docs/04_tokenizer.md','docs/05_dataset.md','docs/06_training_plan.md',
    'docs/07_environment.md','docs/08_evaluation.md','docs/09_prior_art_and_baselines.md',
    'docs/11_technical_research_gaps.md','docs/12_training_implementation_research.md',
    'docs/13_tokenizer_dialogue_data_research.md','docs/14_evaluation_deployment_research.md'}
NEW_DOCS = {'docs/document_catalog.md','docs/142_documentation_refresh.md'}


def now():
    return datetime.now(timezone.utc).isoformat()


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')


def git(*args):
    result = subprocess.run([GIT,'-C',WIN_ROOT,'-c','core.quotepath=false',*args], check=True, capture_output=True)
    return result.stdout.decode('utf-8').strip()


def tracked_docs():
    # Copies produced by this refresh are provenance artifacts, not additional
    # source documents; every copy is separately bound and checked in baseline.
    prefix='reports/investigation/documentation-refresh-20261014/'
    return sorted(p for p in git('ls-files','-z').split('\0')
                  if Path(p).suffix in ('.md','.rst') and not p.startswith(prefix))


def kind(path):
    if path in OPERATIVE or path in NEW_DOCS:
        return 'current_document'
    if path.startswith('reports/') or path.startswith('docs/retrospective/') or 'history' in path or 'autonomous_status_phase5' in path:
        return 'immutable_history'
    return 'dated_plan_research_or_result'


def anchors(path):
    text=path.read_text(encoding='utf-8-sig')
    found=set(re.findall(r'<a\s+[^>]*id=["\']([^"\']+)',text))
    counts=Counter()
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$',text,re.M):
        heading=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',heading)
        heading=re.sub(r'<[^>]+>','',heading)
        slug=re.sub(r'[^\w -]','',heading.lower()).replace(' ','-')
        suffix='' if counts[slug]==0 else '-'+str(counts[slug])
        found.add(slug+suffix)
        counts[slug]+=1
    return found


def inbound_anchors():
    baseline=json.loads((RUN/'baseline.json').read_text(encoding='utf-8'))
    issues=[]
    checks=0
    for name in sorted({e['path'] for e in baseline['files']}|NEW_DOCS):
        path=ROOT/name
        for href in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',path.read_text(encoding='utf-8-sig')):
            target,_,fragment=href.strip('<>').partition('#')
            if not fragment or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',target):
                continue
            resolved=(path.parent/unquote(target)).resolve() if target else path
            if not resolved.is_relative_to(ROOT.resolve()):
                continue
            relative=str(resolved.relative_to(ROOT))
            if relative not in OPERATIVE|NEW_DOCS:
                continue
            checks+=1
            if unquote(fragment) not in anchors(resolved):
                issues.append(dict(source=name,target=relative,fragment=unquote(fragment)))
    result=dict(observed_at=now(), source_documents=len(baseline['files'])+len(NEW_DOCS),
        incoming_heading_links_checked=checks,issues=issues,
        scope='All source documents pointing to current documents; archived reports keep original text and relative context.')
    save(RUN/'inbound_anchor_checks.json',result)
    print(json.dumps(result,ensure_ascii=False))


def snapshot():
    assert not (RUN / 'baseline.json').exists(), 'Existing baseline must remain immutable'
    assert not git('status','--porcelain','--untracked-files=no'), 'Snapshot requires unchanged tracked files'
    entries = []
    for name in tracked_docs():
        source = ROOT / name
        sha = digest(source)
        archived = RUN / 'originals' / (sha + source.suffix)
        if not archived.exists():
            archived.parent.mkdir(parents=True, exist_ok=True)
            archived.write_bytes(source.read_bytes())
        assert digest(archived) == sha
        text = source.read_text(encoding='utf-8-sig')
        entries.append(dict(path=name, sha256=sha, bytes=source.stat().st_size,
            archive=str(archived.relative_to(ROOT)), category=kind(name),
            title=next((l.lstrip('# ').strip() for l in text.splitlines() if l.startswith('#')),source.stem),
            lines=len(text.splitlines()), local_or_external_links=len(re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',text))))
    save(RUN / 'baseline.json', dict(created_at=now(), baseline_commit=git('rev-parse','HEAD'),
        objective='ドキュメントをすべて最新にして', document_count=len(entries),
        category_counts=dict(Counter(e['category'] for e in entries)), files=entries,
        research_resumed=False, corpus_or_TEST_parsed=False, GPU_work=False))
    print(json.dumps(dict(preserved_documents=len(entries), bytes=sum(e['bytes'] for e in entries)),ensure_ascii=False))


def catalog():
    baseline = json.loads((RUN / 'baseline.json').read_text(encoding='utf-8'))
    names = sorted({e['path'] for e in baseline['files']} | NEW_DOCS)
    lines = ['# 全文書カタログ', '', '更新: 2026-10-14 JST。全追跡文書を棚卸しし、現在の説明と当時の計画・証拠を区別する。', '',
        '[現在の状態](autonomous_status.md)・[最新結果141](141_chat_lr_comparison_results.md)・[今回の更新142](142_documentation_refresh.md)を先に読む。研究・学習は停止中。Base/Chatは未完成・未採用。', '',
        '日付付き計画・結果と固定台帳の原文は変更しない。「次回」「継続中」「未実施」は作成時点の記録であり現在の実行許可ではない。固定台帳の対象revisionと後続実験を混同しない。', '',
        f'棚卸し対象は既存{baseline["document_count"]}文書と今回追加2文書。全件の原byte/hashと区分は[baseline](../reports/investigation/documentation-refresh-20261014/baseline.json)に保存した。', '']
    labels = {'current_document':'現行の説明・運用','dated_plan_research_or_result':'作成時点の計画・調査・結果','immutable_history':'原文を保持する固定台帳・保存証拠'}
    for category, label in labels.items():
        selected = [n for n in names if kind(n) == category]
        lines += [f'## {label}（{len(selected)}文書）','', '| 文書 | 扱い |','|---|---|']
        for name in selected:
            relative = '../' + name
            treatment = '本文・現在の判断を更新' if category == 'current_document' else '原文不変。現在の状態・採否は141と状態へ'
            lines.append(f'| [{name}]({relative}) | {treatment} |')
        lines.append('')
    (ROOT / 'docs/document_catalog.md').write_text('\n'.join(lines),encoding='utf-8',newline='\n')
    print('Complete document catalog written')


def update():
    baseline=json.loads((RUN / 'baseline.json').read_text(encoding='utf-8'))
    def previous(name):
        entry=next(e for e in baseline['files'] if e['path']==name)
        return (ROOT / entry['archive']).read_text(encoding='utf-8-sig').replace('\r\n','\n')
    def write(name,text):
        (ROOT/name).write_text(text.strip()+'\n',encoding='utf-8',newline='\n')
    def retained(name,title,note,start=None):
        old=previous(name)
        if start:
            old=old[old.index(start):]
        else:
            old=old[old.index('\n')+1:].lstrip()
        write(name,title+'\n\n更新: 2026-10-14 JST。'+note+'\n\n## 作成時点の資料・契約\n\n'+old)
    common='[現在の状態](autonomous_status.md)、[最新結果141](141_chat_lr_comparison_results.md)、[ロードマップ](15_project_roadmap.md)が現在の判断の正本。研究・教材準備・診断・生成評価・学習は停止中。'
    write('docs/01_project_goal.md', '''# プロジェクト目的

更新: 2026-10-14 JST。JMicro-10MはTokenizer・モデル・事前学習をスクラッチで構築し、日本語の自然な短い続きを作るBase、その後に短い会話を行うChatとローカル利用一式を目指す研究プロジェクト。**Base/Chatは未完成・未採用。** [最新結果141](141_chat_lr_comparison_results.md)、[現在の状態](autonomous_status.md)。

## 維持する目標

- 総学習可能パラメータ9.5M〜10.1M、現在10,001,152。大型化を改善策にしない。
- 日本語Baseの原品質条件と短文会話の目標を維持する。対象を物語だけへ縮めたり閾値を下げたりしない。
- BaseとChatを別checkpointとして管理する。ChatはBaseへ会話形式を追加学習したモデルで、別のarchitectureではない。
- 挨拶、相づち、感情への短い応答、質問返し、数turnの文脈維持と自然な停止を評価する。
- 高度な数学・コード生成・長文RAG・網羅的知識は当初の成功条件に加えない。
- 学習・保存再開・評価の再現性、Tokenizerの共通byte比較、反復・Unicode・役割混同の原出力を記録する。
- 量子化5〜10MB級は将来の目標。採用済みの学習モデルの量子化品質・実容量・独立環境検証は未達。

## 実績と未達

Phase0〜5の基盤を整備し、元10B Baseと多数の同10M比較を実行した。元Baseの品質採用は未達。Chat-first診断と教材比較128/131/133/135、低学習率比較139も全評価後に不採用で閉鎖した。最新139は全28セット・6,132内容判断・固定NLL7点。技術基盤や実学習の完了をモデル完成へ読み替えない。

独立学習seed43、人間blind、独立corpus監査、正式保持、fullDEV・最終suite、選定封印後TESTと正式採用は未確認。元Chat TEST20行の準備解析事故を保存し、将来の有資格Chat最終確認には新しい封印TESTが必要。

## 進め方と停止境界

通常の順序は基盤→Base→Chat→量子化。未採用Baseからの限定SFTはユーザーが明示再開した診断として実行し、既に閉鎖済み。新しい学習や追加教材へ自動移行しない。

再開するなら[Base復旧124](124_base_recovery_plan.md)等で介入を最大1件に絞り、対照・教師量・変更点・原品質・資源と終了条件を先に定める。Base復旧は必要な品質・独立確認・採用証拠がそろったBaseで通知して停止する。Chat・量子化・公開は別の再開判断。[フェーズ別計画](15_project_roadmap.md)。

初期計画・2024年の約355Mモデルとの比較・当初の概算は[全文書カタログ](document_catalog.md)と[更新前原文](../reports/investigation/documentation-refresh-20261014/baseline.json)へ保全した。
''')
    retained('docs/02_research_summary.md','# 調査要約',common+' 外部研究は当時の資料で、今回全件の外部再調査はしていない。\n\n現参照はnative10,001,152、Tokenizer4096、NoQK-Norm/SwiGLU/context1024。元10B Baseと後続SFTを実行したが品質未達。Layer Sharingの固定比較は実施・不採用、ReLU²の固定比較は予算gate不成立で本比較未開始・終了。これらを単なる未実装の次案へ戻さない。\n\n最新低LR候補は新DEV内容20/80・自己文脈5/24、CI下限−1.25ポイント、反復と文字失敗が残り不採用。SFT TRAIN適合やBPB改善だけでは内容・文脈の達成を示さない。Base単独原因・10M容量限界は未確定。技術採否と後続実績は[全体記録125](125_project_retrospective.md)で追える。',start='## 結論')
    # The old conclusions remain explicitly historical; remove their claim to
    # be present decisions without changing the original stored bytes.
    p=ROOT/'docs/02_research_summary.md'
    text=p.read_text(encoding='utf-8').replace('## 結論','## 初期調査と当時の結論').replace('**現在の決定**','**2026-10-03当時の決定**')
    write('docs/02_research_summary.md',text)
    retained('docs/03_architecture.md','# アーキテクチャ設計',common+'\n\n## 現在の固定参照\n\n語彙4,096、hidden256、13層、FFN640、4Q/2KV、head dim64、SwiGLU、RMSNorm、RoPE、context1024、tied embedding、biasなし、dropout0、QK-Normなし。実parameter数10,001,152。`src/jmicro/model.py` SHA256は `298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83`。元10B・後続教材比較・最新139はこのnative参照を維持しており、品質は未採用。\n\nQK-Norm有無、T8K/T4K、ReLU²、Layer Sharing等の実装・閉じた比較は下の当時の記録と[全体125](125_project_retrospective.md)を参照する。構成変更は9.5M〜10.1M内の別proposalと比較が必要。元frozen sourceは置き換えない。\n\nHF/GGUFの初期変換確認は基盤の証拠で、現在のSFT重みの量子化品質・配布完成ではない。',start='## 初期baseline:')
    retained('docs/04_tokenizer.md','# Tokenizer設計',common+'\n\n現系列は固定4096語彙のSentencePiece Unigram + byte fallbackを使用。SHA256 `a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318`。8192版は初期比較として保全し、同bytes/BPBとモデル配分の条件を区別する。再学習・語彙追加・embedding resizeは不要。\n\n特殊IDはPAD0/UNK1/BOS2/EOS3/System4/User5/Assistant6/EOT7。会話本文を個別encodeしrole/EOTは構造IDで挿入する。CRLF/CR→LFとNUL除去以外のUnicodeを保持し、改行・タブ・literal ▁・<の表現は共通wrapperの契約に従う。raw不正UTF8を表示修正で成功扱いにしない。\n\n[Phase2契約](18_phase2_completion.md)・[固定config](../configs/tokenizer/contract.json)・[復元](huggingface_handoff.md)を参照。下は初期方針と当時の候補で、既に完了した学習の再実行指示ではない。',start='## 方針')
    retained('docs/05_dataset.md','# データ設計',common+'\n\n## 受入データの現在の範囲\n\n元Web TRAINは12,225,819,077 tokensが準備済み。元10B、別staged約10.6B、accepted混合2Bと後続Chatは別系列で、教師量を合算しない。初期pilotの全件監査と後続全corpusの独立意味監査は別で、未完了の監査を完了にしない。50〜100B master全量は未取得。\n\n最新139は前回138のaccepted TRAIN41,529 target・660,109 Assistant本文+EOT教師/周と280sample QAを再利用した。新教材・新QA0。候補実消費1,899,557教師は繰返し学習を含み新規教材量ではない。新DEV80と既知3回帰をTRAINから分離し、固定NLLは共通2,634 target。\n\n元Chat TEST20行を準備時に構文解析した事故は[141](141_chat_lr_comparison_results.md)に保存。学習・GPU評価には使用していないが未参照とは呼ばない。将来の有資格確認には新しい封印Chat TESTが必要。元Base TESTは今回の事故では解析していない。\n\n所在・manifest・受入済み範囲は[data保存先](../data/README.md)と[引継ぎ](windows_handoff.md)。独立意味監査・新教材準備・再dedupを文書更新に追加しない。外部sourceの規模・条件は下の調査時点の記録であり、取得時は固定revisionを確認する。',start='## 中心候補')
    write('docs/06_training_plan.md','''# 学習計画

更新: 2026-10-14 JST。研究・教材準備・診断・生成評価・学習は停止中。[最新結果141](141_chat_lr_comparison_results.md)、[状態](autonomous_status.md)、[ロードマップ](15_project_roadmap.md)。Base/Chat未完成・未採用。

## 実装済みと未確認

BaseのAdamW、warmup/cosine、WSD stable/decay、stable予算の明示fork、全state保存再開は実装・実学習済み。Assistant本文+EOTを教師とするdocument sampler、`TeacherChatTrainer`、固定教師量SFT、自己生成履歴評価も実装・実GPU実行済み。Chat trainer未実装・Chat学習未実施という旧説明は現在には適用しない。

独立学習seed43・人間blind・正式Base保持・fullDEV/最終suite・封印TEST・正式採用は未確認。CPU factoryや保存再開試験を独立学習・品質証拠にしない。nativeを旧stable+decay専用runnerへ偽装して渡さず、有資格時の接続は実装してから実行する。

## 閉じた比較

| 系列 | 実績と採否 |
|---|---|
| 元Web10B | 学習・保存・評価済み、Base品質未達。元WebUIで維持 |
| Base teacher-decay2B | BPB改善でも一貫性・完結・反復が未達、不採用。[123](123_base_teacher_decay_2b_results.md) |
| 教材汎化133 | 全14セット/3,066判断/NLL7点、不採用。[136](136_chat_generalization_results.md) |
| 意味多様性135 | 全21セット/4,599判断/NLL7点、不採用。[138](138_chat_semantic_diversity_results.md) |
| 低LR139 | 同TRAIN/親/seed/教師量で1e-4対3e-5。全28セット/6,132判断/NLL7点、不採用。[141](141_chat_lr_comparison_results.md) |

最新候補はcontext1024、batch32、accumulation1、BF16/math、compile=false、固定padding、学習seed42、fresh AdamW、登録B1,899,555。実3,646更新・1,899,557教師、25検証更新を本学習へ加算しない。上限33,600 GPU秒、実2,658.673秒。これは閉じた条件で、次実験の推奨LR・開始予算ではない。純入力・教師・padding込みphysical tokens/秒を区別する。

## 再開時の進め方

既存証拠から未回答の仮説を1件選び、変更点・対照・TRAIN/DEV/TEST・教師量・原品質・全評価費用・終了条件を凍結する。環境→trainer/evaluation→保存再開→安定batchを満たしてから実行し、一巡を不採用で終えたら報告・停止。終了済みrun、拒否padding、別LR/seed/予算で救済しない。

全stateにはmodel/optimizer/scheduler/Python・NumPy・Torch・CUDA RNG/sampler position/消費カウンタ・digestを保存する。完了updateでatomic保存し、同凍結条件で連続対再開を確認。通常resumeでsource/data/schedule/budgetを変更しない。長期jobはPID/boot/start、logs、GPU lock、累積台帳を保存する。

約10Mと原品質を維持する。Base復旧は[124](124_base_recovery_plan.md)の合格Baseで通知・停止。Chat/Dialogue/SFT、量子化、20B/50B、公開・有料cloudは別の範囲判断。大型モデル比較の過去案は現行の10M制約を変更しない。

Python3.12.7はすべて`uv run --frozen`。通常WSL extrasは`--extra hub --extra data --extra ml --extra export`、依存変更は`uv add`。[実行環境](07_environment.md)。当初の段階量・速度・Vast.ai案は[更新前原文](../reports/investigation/documentation-refresh-20261014/baseline.json)へ保全した。
''')
    retained('docs/07_environment.md','# 実行環境とデータ配置',common+'\n\nWindowsはGit正本 `C:\\Users\\AiHUB\\Desktop\\japanese-tiny-llm-10m`、WSL実行コピー `/home/aihub_ubuntu/src/japanese-tiny-llm-10m`、大容量data `/home/aihub_ubuntu/jmicro-data`。WSL package3.x/WSL2/Linux/RTX4090、Python3.12.7/uvを維持。依存を今回更新・再測定していない。\n\n元10B Baseと後続SFTは学習済みだが未採用。最新139はBF16/math・compile=false・batch32/context1024/固定padding。probe peak allocated16,223,183,360bytes、本学習実1,523.890秒、全GPU2,658.673秒。旧Flash/compileの694,521入力tokens/秒をこの教師速度へ読み替えない。過去の空き容量・PID・driver値は観測時点の値で、現在の生存や容量を保証しない。\n\n最新checkpoint/data/元UIは[引継ぎ](windows_handoff.md)。Pythonは一時処理もuv run --frozen。導入uv python install 3.12.7、復元uv sync --frozen、変更uv add。文書のみの更新にdriver変更・benchmarks・GPU再評価を加えない。',start='## 実機環境')
    retained('docs/08_evaluation.md','# 評価・Checkpoint・検証',common+'\n\n最新139は全28セット・6,132内容判断・共通NLL7点×2,634 targetを監査済み。新DEV80、既知3回帰、各固定履歴80/role抑制なし80/実自己履歴24会話59turnを区別した。内容・文脈・停止・反復・raw Unicodeの原gateを維持し不採用。\n\nChat評価と自己履歴評価は実施済み。独立人間blind、独立学習seed43、正式保持、fullDEV/最終suite、封印TEST、正式採用は未確認。Codex非blind全件判断・機械flag・技術testsを人間blindの合格へ読み替えない。\n\n元Chat TEST20行は準備で解析され、未参照の主張を取り消した。今後の有資格Chat確認は新たな封印TESTが必要。元のsplit/閾値/原失敗を修正しない。[評価契約](evaluation_protocol.md)は凍結v1と実験別の適用を分ける。\n\n全3checkpointと全update入力/label digest、25CUDA検証更新の連続/保存再開を確認済み。検証更新・CPUチェック・再利用判断は新学習や独立能力確認ではない。',start='## 評価原則')
    p=ROOT/'docs/08_evaluation.md'
    text=p.read_text(encoding='utf-8').replace('## 固定生成suite','## v1固定suiteの契約と当時の利用').replace('testとChatは未使用。','このPhase4〜5時点ではtestとChatは未使用だった。').replace('## Dialogue評価','## Dialogue評価の観点')
    write('docs/08_evaluation.md',text)
    print('Core goal/specification/training/evaluation documents updated; historical originals preserved')


def verify(commit=None,receipt_commit=None):
    baseline = json.loads((RUN / 'baseline.json').read_text(encoding='utf-8'))
    names = set(tracked_docs()) | NEW_DOCS
    original_names = {e['path'] for e in baseline['files']}
    assert names == original_names | NEW_DOCS
    current, unchanged, changes, link_failures = [], [], [], []
    for entry in baseline['files']:
        assert digest(ROOT / entry['archive']) == entry['sha256']
        assert digest(WSL / entry['archive']) == entry['sha256']
        name = entry['path']
        same = digest(ROOT / name) == entry['sha256']
        if name not in OPERATIVE:
            assert same, 'Historical evidence changed: '+name
            unchanged.append(name)
        else:
            assert not same, 'Current document not refreshed: '+name
            changes.append(name)
    catalog_text = (ROOT / 'docs/document_catalog.md').read_text(encoding='utf-8')
    assert all(f'[{n}](' in catalog_text for n in names)
    for name in sorted(OPERATIVE | NEW_DOCS):
        path = ROOT / name
        text = path.read_text(encoding='utf-8')
        assert '\0' not in text and '\ufffd' not in text, 'Unexpected text corruption: '+name
        assert '2026-10-14' in text and ('141' in text or name == 'AGENTS.md'), name
        assert digest(path) == digest(WSL / name), 'Windows/WSL mismatch: '+name
        for match in re.finditer(r'\[[^\]\n]*\]\(([^)\n]+)\)',text):
            href=match.group(1).strip('<>')
            target,_,fragment=href.partition('#')
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',target):
                continue
            resolved = (path.parent / unquote(target)).resolve() if target else path
            if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():
                link_failures.append(dict(document=name,target=target))
            elif fragment and resolved.suffix in ('.md','.rst') and unquote(fragment) not in anchors(resolved):
                link_failures.append(dict(document=name,target=href,problem='missing_heading_anchor'))
        current.append(dict(path=name,sha256=digest(path),bytes=path.stat().st_size))
    assert not link_failures, json.dumps(link_failures,ensure_ascii=False)
    incoming=json.loads((RUN/'inbound_anchor_checks.json').read_text())
    assert not incoming['issues'] and incoming['source_documents']==len(names)
    for name in ('AGENTS.md','README.md','docs/autonomous_status.md','docs/15_project_roadmap.md','docs/windows_handoff.md','docs/10_next_steps.md'):
        text = (ROOT / name).read_text(encoding='utf-8')
        assert '141' in text and ('未完成' in text or 'unfinished' in text)
    for row in json.loads((RUN/'non_document_text_files.json').read_text()):
        assert not row['documentation_file'] and digest(ROOT/row['path'])==row['sha256']
    status_text=(ROOT/'docs/autonomous_status.md').read_text(encoding='utf-8')
    for value in ('28セット','6,132','2,634','3,646','1,899,557','56/80','15/24','−1.25〜+18.75','09f338e'):
        assert value in status_text,value
    # Frozen sources and experimental artifacts are separate from editable docs.
    config = json.loads((ROOT / 'configs/phase7/chat-lr-20261014.json').read_text())
    for name, sha in config['source_sha256'].items():
        assert digest(ROOT / name) == digest(WSL / name) == sha
    scientific=json.loads((ROOT/'reports/phase7/chat-lr-20261014/completion.json').read_text())
    selection=json.loads((ROOT/'reports/phase7/chat-lr-20261014/selection.json').read_text())
    delivery_path='reports/phase7/chat-lr-20261014/final_delivery_checks.json'
    old_delivery=json.loads((ROOT/delivery_path).read_text())
    assert scientific['all_three_step_decisions_complete'] and scientific['eligible_candidate'] is None
    assert not scientific['model_quality_complete'] and not scientific['independent_confirmation_executed']
    assert old_delivery['passed'] and old_delivery['result_commit']=='89275a88e7a23cd90f69c18a756f225e03de5c8d'
    assert selection['new_joint_CI_lower']==-.0125 and not selection['candidate_eligible']
    for suite,content,context in (('new',20,5),('semantic',18,5),('previous',19,5),('old',15,1)):
        row=selection['summary']['S1'][suite]['content']
        assert row['primary']['joint_grammar_relevance_score2']==content
        assert row['own_history_final24']['context_score2']==context
    for name in ('scope','intervention','progress','selection','analysis','conditional_branches','technical','training','GPU_ledger','source'):
        ref=scientific[name]
        assert digest(Path(ref['path']))==ref['sha256'], name
    previous_receipt_commit='09f338e3312f884dab84ba20a8467ff5e2011a9e'
    receipt_win=WIN_ROOT+'\\'+delivery_path.replace('/','\\')
    assert git('rev-parse',previous_receipt_commit+':'+delivery_path)==git('hash-object','--path='+delivery_path,receipt_win)
    changed = git('diff',baseline['baseline_commit'],'--name-only').splitlines()
    permitted = OPERATIVE | NEW_DOCS | {'scripts/refresh_project_documents.py','.gitattributes'}
    assert all(n in permitted or n.startswith('reports/investigation/documentation-refresh-20261014/') for n in changed), changed
    git('diff','--check')
    assert git('config','--local','user.name') == 'yousan'
    assert git('config','--local','user.email') == 'ka1357amnbpdr@gmail.com'
    proof = dict(passed=True, verified_at=now(), baseline_commit=baseline['baseline_commit'],
        documentation_only=True, original_document_count=len(original_names), total_documents=len(names),
        updated_existing_documents=len(changes), additional_documents=len(NEW_DOCS),
        historical_documents_preserved=len(unchanged), catalog_covers_every_document=True,
        current_local_links_valid=True, current_Windows_WSL_bytes_match=True, frozen_sources_unchanged=True,
        local_heading_anchors_verified=True, backup_Windows_WSL_bytes_match=True,
        incoming_heading_links_from_all_documents_verified=incoming['incoming_heading_links_checked'],
        changed_documents=changes, current_document_hashes=current,
        research_resumed=False, dataset_or_TEST_parsed=False, GPU_work=False,
        Base_adopted=False, Chat_adopted=False, push_executed=False, source_sha256=digest(Path(__file__)),
        original_scientific_evidence_and_previous_receipt_verified=True,
        previous_result_commit=old_delivery['result_commit'],previous_receipt_commit=previous_receipt_commit,
        current_numerical_claims_match_original_selection=True,
        backup_copy_paths_verified=len(baseline['files']))
    if commit:
        revision = git('rev-parse',commit+'^{commit}')
        committed_paths={r['path'] for r in current}|{r['archive'] for r in baseline['files']}
        committed_paths.update(str(p.relative_to(ROOT)) for p in RUN.rglob('*')
                               if p.is_file() and p.name!='commit_verification.json')
        committed_paths.update(('scripts/refresh_project_documents.py','.gitattributes'))
        for name in sorted(committed_paths):
            win = WIN_ROOT+'\\'+name.replace('/','\\')
            assert git('rev-parse',revision+':'+name) == git('hash-object','--path='+name,win)
        assert not git('status','--porcelain'), 'Final worktree must be clean'
        proof.update(result_commit=revision,committed_document_contents_verified=True,
                     committed_document_and_preservation_files=len(committed_paths))
        if receipt_commit:
            receipt_path=RUN/'commit_verification.json'
            receipt=json.loads(receipt_path.read_text())
            assert receipt['passed'] and receipt['result_commit']==revision
            assert receipt['source_sha256']==digest(Path(__file__))
            assert digest(receipt_path)==digest(WSL/receipt_path.relative_to(ROOT))
            relative=str(receipt_path.relative_to(ROOT))
            win=WIN_ROOT+'\\'+relative.replace('/','\\')
            last=git('rev-parse',receipt_commit+'^{commit}')
            assert git('rev-parse',last+':'+relative)==git('hash-object','--path='+relative,win)
            assert git('rev-parse','HEAD')==last
            proof.update(receipt_commit=last,all_documentation_scope_and_delivery_complete=True)
        else:
            save(RUN/'commit_verification.json',proof)
            (WSL/'reports/investigation/documentation-refresh-20261014/commit_verification.json').write_bytes(
                (RUN/'commit_verification.json').read_bytes())
        print(json.dumps({k:v for k,v in proof.items() if k not in ('current_document_hashes','changed_documents')},ensure_ascii=False))
        return
    save(RUN / 'verification.json',proof)
    print(json.dumps({key:proof[key] for key in ('passed','total_documents','updated_existing_documents','historical_documents_preserved')},ensure_ascii=False))


def operations():
    baseline=json.loads((RUN/'baseline.json').read_text(encoding='utf-8'))
    def original(name):
        entry=next(e for e in baseline['files'] if e['path']==name)
        return (ROOT/entry['archive']).read_text(encoding='utf-8-sig').replace('\r\n','\n')
    def write(name,text):
        (ROOT/name).write_text(text.strip()+'\n',encoding='utf-8',newline='\n')
    receipt='[科学監査](../reports/phase7/chat-lr-20261014/completion.json)、[採否](../reports/phase7/chat-lr-20261014/selection.json)、[納品記録](../reports/phase7/chat-lr-20261014/final_delivery_checks.json)'
    rules=original('AGENTS.md')
    rules=rules[rules.index('## Fixed model-size requirement'):]
    rules=rules.replace('The separately identified bounded Chat-first diagnostic is an ordering exception only when explicitly resumed;128,131 and133 are closed, with final four-item results in136. Later proposals in135 require explicit resumption.',
        'The bounded Chat-first diagnostics128/131/133/135/139 are closed and rejected; final results are136/138/141. New comparisons require explicit resumption and a separate frozen contract.')
    write('AGENTS.md','''# JMicro-10M development and training

Read `docs/autonomous_status.md`, `docs/15_project_roadmap.md`, and `docs/windows_handoff.md` before continuing. Current evidence is in result141; document coverage and update evidence are in docs/142_documentation_refresh.md and docs/document_catalog.md. Plans124 and future proposals are not execution authorization.

## Current scope — 2026-10-14 JST: documentation only

The user requested "ドキュメントをすべて最新にして". Update all current documentation, inventory every document, preserve dated reports/frozen histories and scientific evidence, verify references and Windows/WSL copies, and commit the documentation delivery locally. This does not resume research, diagnostics, data preparation, evaluation, GPU training or old jobs. No automatic push, publication, quantization or deployment.

The previous three-step goal was completed with the LR3e-5 candidate rejected:3646 updates/1899557 Assistant teachers, all28 suites/6132 judgments/7 fixed NLL points, full-state/stream/ledger audits and all seven conditional decisions. Final S1 content20/18/19/15 of80 and own context5/5/5/1 of24 fail the original56/80 and15/24 gates; new improvement CI lower−1.25pp, repetition regressions and new own-history Unicode failure also remain. Result commit89275a8 and receipt commit09f338e were verified; this is scientific comparison and delivery completion, not model quality completion.

All qualified-only branches (Base retention, sampling, fresh trained seed43, human blind, fullDEV, sealed TEST, adoption) are unexecuted, passed=false and quality-unconfirmed. Base/Chat remain unfinished and unadopted. No extra LR/seed/budget/data/architecture or Base intervention is authorized. For any later Base-only resumption, finish an evidence-qualified Base, notify the user and stop; do not automatically move to Chat/SFT/quantization.

Preserve the original Chat TEST20-row preparation parsing exposure and its correction. It was not used for learning or GPU selection, but cannot be called untouched. Any future qualified final Chat confirmation requires fresh sealed cases. Original Base TEST was not parsed in that incident.

Keep original10B WebUI available. Latest stored scientific observation2026-10-13T16:54:20Z: PID309447, boot4052bfc5-3850-44e4-9123-d34a9e19f36e, start55170810, HTTP parent/Tokenizer/10M and idle state, kernel lock verified. Recorded identity is not current/future liveness proof. Do not start GPU or relaunch jobs during documentation work.

Frozen scientific reports, manifests and dated histories describe their captured revision. Verify their original Git revision/snapshots when living docs change; do not rewrite old completion/receipt records to make current document hashes appear historical. The original operative texts are preserved byte-for-byte in the documentation-refresh baseline.

'''+rules)
    write('docs/autonomous_status.md','''# 現在の状態

更新: 2026-10-14 JST。**Base/Chatは未完成・未採用。研究・教材準備・診断・生成評価・GPU学習は停止中。** 現在の依頼は全ドキュメントの更新・整合確認とローカル保存。[更新142](142_documentation_refresh.md)、[全文書カタログ](document_catalog.md)。

## 最新の完了結果

[低学習率比較141](141_chat_lr_comparison_results.md)で、計画139の介入選定・同10M比較・有資格候補だけの独立確認への分岐を完了し、候補S1を不採用で閉鎖した。元10B親、同accepted TRAIN/Tokenizer/seed42/教師量/schedule/paddingでpeak LR1e-4→3e-5を比較。S0は138のS1の歴史state、新学習0。

| 項目 | 実際の証拠 |
|---|---|
| 固定参照 | native10,001,152 parameters、Tokenizer4096、context1024。9.5M〜10.1Mを維持 |
| 教材 | TRAIN41,529 target、660,109教師/周。280sample QAを再利用。新教材・新QA0 |
| S1学習 | 3,646更新・1,899,557 Assistant本文+EOT教師、許容内超過2。全3state・全update入力/label digest確認 |
| 全評価 | 28セット・6,132理由付き内容判断・共通NLL7点×2,634 target。既知12セット2,628判断は出典付き再利用 |
| 技術確認 | CUDA probe9＋連続/保存再開16の25検証更新。品質や本学習へ数えない |
| 資源 | 新GPU2,658.673158秒/33,600秒。過去の学習やCPUレビュー時間と別 |
| 保存 | 結果commit89275a8、納品commit09f338eの360ファイル保存・Git内容を確認。push/公開なし |

| 最終セット | S0内容 /80 | S1内容 /80 | S0自己文脈 /24 | S1自己文脈 /24 |
|---|---:|---:|---:|---:|
| 新DEV | 13 | 20 | 3 | 5 |
| 138 DEV | 19 | 18 | 3 | 5 |
| 133 DEV | 21 | 19 | 6 | 5 |
| 元旧DEV | 11 | 15 | 1 | 1 |

原条件は全セット内容56/80以上、自己生成文脈15/24以上など。新内容差+8.75ポイント、95%CI −1.25〜+18.75も改善条件未達。反復非退行・停止の条件も不成立、新自己生成Unicode失敗1を保存。低LRでDEV NLLが対照より低くても品質合格ではない。

'''+receipt+'''。

## 完了したことと未確認

前の「3まで進めてください」は比較・採否・条件分岐・報告・保全・ローカル納品まで完了した。Base保持、sampling、fresh学習seed43、人間blind、fullDEV、封印TEST、採用の7分岐は候補なしで未実行・passed=false・品質未確認。独立確認を実行した、モデルが完成したとは記載しない。

判断はCodex非blind、QAは標本、対照は歴史state。独立corpus監査・正式Base/Chat採用も未確認。Base単独原因・10M容量限界は確定していない。

元Chat TEST20行を準備時にCPU構文解析した事故を[141](141_chat_lr_comparison_results.md)へ保存。学習・GPU評価への使用0だが、未参照の主張は取り消した。将来の有資格Chat最終確認には新たな封印TESTが必要。元Base TESTは事故では解析していない。

## 次の判断と停止境界

文書更新を終えて通知・停止する。新介入・別LR/seed・教材・評価・学習は明示再開待ち。[Base復旧124](124_base_recovery_plan.md)を選ぶ場合は原品質・10M・独立確認を維持し、合格Baseで通知・停止。Chat・量子化・公開へ自動移行しない。

## UI・保存先・履歴

最新の保存された科学観測2026-10-13T16:54:20Zでは元[WebUI](http://127.0.0.1:7860) PID309447/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start55170810、元親/Tokenizer/10M・busy=false・kernel GPU lock一致・競合なし。現在の稼働保証ではなく必要時に実processを照合する。終了runは再起動しない。

最新S1はWSL `reports/phase7/chat-lr-20261014/S1/checkpoint-00003646.pt`、SHA `f7e8bb8b1569cb45ac399108455a66c5922f64d7898e8ab6b4931ba13c856018`。重み・samplerを含む全state・教材はWSL、Git正本はWindows。[引継ぎ](windows_handoff.md)。

Base結果[123](123_base_teacher_decay_2b_results.md)、教材汎化[136](136_chat_generalization_results.md)、意味多様性[138](138_chat_semantic_diversity_results.md)、最新LR[141](141_chat_lr_comparison_results.md)は別runの閉鎖済み証拠。元UI10B・別staged約10.6B・teacher-decay2B・後続SFTの学習量を合算しない。

[公開保存版126](126_model_archive.md)は2026-10-09の主要3系列保存で、dataset/samplerを除外。後続Chat重みは公開していない。当時のpush許可は当時の納品に限る。

旧運用全文と全311文書のhashは[更新前baseline](../reports/investigation/documentation-refresh-20261014/baseline.json)に保全。[全体125](125_project_retrospective.md)と[固定台帳](retrospective/README.md)は当時のrevisionを保持する。
''')
    roadmap=original('docs/15_project_roadmap.md')
    body=roadmap[roadmap.index('## 目的と停止境界'):]
    body=body.replace('最新の結果は138。最新の教材比較135は138で不採用終了し、','最新の結果は141。教材比較135は138、低LR比較139は141で不採用終了し、')
    body=body.replace('128/131/133の限定SFT比較と全内容確認は完了・不合格。138で6段階の実行監査を閉鎖、追加実験停止・採用未達',
        '128/131/133/135/139の限定SFT比較は全評価・不採用で閉鎖。141で3段階の条件分岐と納品を完了。採用未達・追加実験停止')
    body=body.replace('限定Chat診断と教材比較は138まで完了したが、','限定Chat診断と教材/低LR比較は141まで完了したが、')
    body=body.replace('次の介入は135末尾の未実行提案から別の明示再開時に選定する。','低LRの1件比較も不採用で閉じた。次の介入は既存証拠から別の明示再開時に選定・凍結する。')
    body=body.replace('128/131/133の限定Chat比較は実行・不合格終了し、追加の実行は135の提案から別の明示再開待ち。','128/131/133/135/139の限定Chat比較は実行・不合格終了し、追加の実行は別の明示再開・新契約待ち。')
    write('docs/15_project_roadmap.md','''# JMicro-10M フェーズ別実行計画

更新: 2026-10-14 JST。[最新結果141](141_chat_lr_comparison_results.md)の低LR比較は全28セット・6,132判断・NLL7点、学習/採否/予算・条件分岐・納品まで完了し不採用。**Base/Chat未完成・未採用。追加研究・学習停止。** 現依頼は[文書更新142](142_documentation_refresh.md)のみ。

## 次に検討する道筋

| 経路 | 現在の判断 | 次に必要なもの |
|---|---|---|
| 閉じた139 | 内容20/18/19/15 of80・自己文脈5/5/5/1 of24、主CI・反復/文字失敗も未達。不採用 | 終了job・採点・NLL・別LR/seed/予算の救済を再開しない |
| 独立確認 | 7分岐は候補なしで未実行・品質未確認 | 原gateを満たすrecipeが先。生成乱数やCPU準備でfresh学習を代替しない |
| Base復旧124 | 未再開、介入未選定 | 根拠ある介入1件と原品質・対照・資源・終了条件。合格Baseで通知停止 |
| 次SFT・教材/目的/効率 | 未選定・未凍結、提供履歴でも品質不足 | 未回答の問いと別の明示再開。既に拒否したpadding等を再試行しない |
| 量子化・20B/50B・公開 | 今回の範囲外 | 採用モデルと別の範囲判断。残予算を開始許可にしない |

最新139の新GPUは2,658.673158秒/33,600秒。以前の比較やCPU時間とは別。目的・Phase定義・原品質条件を以下に保持する。初期・途中のロードマップ全文は[更新前原文](../reports/investigation/documentation-refresh-20261014/baseline.json)から参照する。

'''+body)
    handoff=original('docs/windows_handoff.md')
    body=handoff[handoff.index('## 正本と保存場所'):]
    body=body.replace('chat-semantic-diversity-20261013/final_archive.json','chat-lr-20261014/final_archive.json').replace('chat-semantic-diversity-20261013/final_delivery_checks.json','chat-lr-20261014/final_delivery_checks.json')
    begin=body.index('## 閉じた最新runとUI')
    end=body.index('UI操作や明示実行再開時だけ、',begin)
    body=body[:begin]+'''## 閉じた最新runとUI

`reports/phase7/chat-lr-20261014/` は全28セット・6,132内容判断・NLL7点×2,634 target、S1全3state/実入力教師列/予算/採否を監査し不採用で閉鎖。結果commit89275a8と納品commit09f338eを確認した。独立確認の7分岐は候補なしで未実行・品質未確認。

元10B [WebUI](http://127.0.0.1:7860)の保存された科学観測2026-10-13T16:54:20ZはPID309447/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start55170810、HTTP親SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`、Tokenizer/10M一致、busy=false、kernel lock一致・競合なし。現在の生存保証ではない。文書更新では再起動・生成・GPU実験を行わない。

'''+body[end:]
    start=body.index('最新S1は ')
    end=body.index('\n\n| 場所',start)
    body=body[:start]+'''最新S1は `reports/phase7/chat-lr-20261014/S1/checkpoint-00003646.pt`、SHA `f7e8bb8b1569cb45ac399108455a66c5922f64d7898e8ab6b4931ba13c856018`。t1/t2/t3のmodel/Adam/scheduler/RNG/sampler/counters、metrics/job/resultを同directoryに保持。TRAINは前回semanticのaccepted教材を参照し、新DEV/固定NLLはdata rootの `phase7/chat-lr-20261014/`。Gitには重みとdataset実体を含めない。以下の旧系列も保全する。所在は原記録から案内し全重み・全corpusを今回再hashしない。''' +body[end:]
    body=body.replace('| 場所 | 保全する内容 |\n|---|---|','| 場所 | 保全する内容 |\n|---|---|\n| `reports/phase7/chat-semantic-diversity-20261013/S1/` | 前回意味教材の全3state。最終SHA `6ca25064fa4ccb6784a05fa5ade43bfdaa87aeb55f11458a233eaf32664fd2ea` |')
    body=body.replace('本書/結果136を読む。選んだ経路が教材比較なら135、Base復旧なら124を参照する。','本書/結果141を読む。Base復旧なら124、他の比較は別の新契約を参照する。')
    body=body.replace('閉じた128/131/133を復旧対象にしない。','閉じた128/131/133/135/139を復旧対象にしない。')
    body=body.replace('教材比較は新TRAIN版/未使用DEV/既知2回帰・専用contract/runnerを先に完成し、','新比較はTRAIN版/未使用DEV/全必要回帰・専用contract/runnerを先に完成し、')
    body=body.replace('独立学習seed43、人間blind、fullDEV、最終suite、protectedTEST、採用、量子化は別の再開判断。','有資格時だけ独立学習seed43、人間blind、fullDEV、最終suite、封印TESTへ進む。候補なしなら未実行・品質未確認で止める。量子化は別の再開判断。')
    write('docs/windows_handoff.md','''# Windows / WSL 引継ぎ

更新: 2026-10-14 JST。[最新結果141](141_chat_lr_comparison_results.md)の低LR比較・条件分岐とローカル納品は完了、不採用。Base/Chat未完成・未採用、研究・教材準備・診断・評価・GPU学習は停止中。現在は[全ドキュメント更新142](142_documentation_refresh.md)のみ。歴史的PIDや途中の進捗を再開指示にしない。

元Chat TEST20行の準備解析事故は[141](141_chat_lr_comparison_results.md)へ保存した。未参照とは呼ばず、将来有資格Chat確認には新しい封印TESTが必要。元Base TESTはこの事故では解析していない。

'''+body)
    write('docs/10_next_steps.md','''# 現在のチェックリスト

更新: 2026-10-14 JST。[最新結果141](141_chat_lr_comparison_results.md)、[状態](autonomous_status.md)、[ロードマップ](15_project_roadmap.md)を正とする。研究・学習は停止中。現在の依頼は[全ドキュメント更新142](142_documentation_refresh.md)。チェック印は証拠への案内で品質合格を意味しない。

## 固定方針

native10,001,152 parameters、9.5M〜10.1M、日本語Baseの原品質を維持。Base/Chat未完成・未採用。大型化・領域縮小・閾値変更で完成扱いにしない。Base単独原因・10M容量限界は未確定。

## 最新の閉じた比較139

- [x] 既存証拠からLR1件を選定し、同親/TRAIN/Tokenizer/seed/教師量/schedule/paddingで凍結。
- [x] 新DEVと既知3回帰、共通2,634 targetのNLLを分離。Chat TEST準備解析事故の原版/修正を保存。
- [x] 実CUDA25検証更新と時間gate、3,646更新/1,899,557教師の実学習、全3state/実入力・教師列を監査。
- [x] 全28セット/6,132判断/NLL7点、最終全原gate/paired CI/反復退行を判定。不合格・不採用。
- [x] 正式保持/sampling/独立seed43/人間blind/fullDEV/封印TEST/採用の7分岐を候補なしで未実行・品質未確認と記録。
- [x] 科学監査、結果141、小report保存と360ファイル/ローカル結果commit89275a8・納品commit09f338eの照合を完了。

## 正式完成に未確認の証拠

- [ ] 原品質と全保持条件を満たすrecipeの選定。
- [ ] fresh学習seed43と独立人間blind。生成乱数やCPU準備で代用しない。
- [ ] 独立corpus監査、正式保持、有資格sampling、全文DEV・全400生成＋長文40・最終継続suite。
- [ ] 選定封印後のTEST・正式採用・再現/復旧。Chatは新たな未使用封印TESTが必要。
- [ ] 採用floatモデルの量子化品質・実容量・独立環境での利用。

## 次の実行境界

全ドキュメント更新の検証・ローカル保存を終えて通知する。追加教材・旧run・再採点・GPU・別LR/seed/budgetを開始しない。Base復旧は[124](124_base_recovery_plan.md)の未再開の別経路で、合格Baseで通知・停止。新介入は既存証拠から1件の別契約が必要。

過去133/135のチェック全文と運用文書は[更新前baseline](../reports/investigation/documentation-refresh-20261014/baseline.json)と[全文書カタログ](document_catalog.md)へ保全した。
''')
    index=original('docs/README.md')
    table=index[index.index('## 番号付きの計画・結果'):]
    write('docs/README.md','''# 文書一覧

更新: 2026-10-14 JST。Base/Chat未完成・未採用、研究・学習は停止中。最新比較139は全28セット・6,132判断・NLL7点と採否・7分岐・納品まで完了し不採用。[最新結果141](141_chat_lr_comparison_results.md)。現依頼は[全ドキュメント更新142](142_documentation_refresh.md)。

## 読む順序

1. [現在の状態](autonomous_status.md)：実績・採否・停止・現在の依頼。
2. [最新結果141](141_chat_lr_comparison_results.md)：全保存点・原失敗・NLL・資源・事故・限界。
3. [ロードマップ](15_project_roadmap.md) / [チェックリスト](10_next_steps.md)：Phaseと正式完成までの不足。
4. [Windows/WSL引継ぎ](windows_handoff.md)：元UI・全state/data・欠損時の復元。
5. [Base復旧124](124_base_recovery_plan.md)：未再開の別経路。合格Baseで通知・停止。
6. [全文書カタログ](document_catalog.md)：311既存文書と今回追加2文書の全件区分。

## 現行仕様と履歴

目的・構成・Tokenizer・データ・学習・環境・評価は[01](01_project_goal.md)〜[08](08_evaluation.md)。凍結評価基準は[評価契約](evaluation_protocol.md)、実績を探す入口は[実験検索](base_experiment_lookup.md)・[全体記録125](125_project_retrospective.md)。

日付付き計画・結果と[固定revision台帳](retrospective/README.md)は原文を維持する。途中の「学習中」「次は」「未実施」やPIDは現在の実行許可ではない。原採否と条件は各runのcompletion/configが正本。以前のmanifest/納品証拠は当時のGit revisionとsnapshotに対する証拠で、今回のliving文書更新へ書き換えない。

閉じたChat比較の順序は128/129→131/132→133/134/136→135/137/138→139/140/141。最新の再開・採否を以前の未実行案へ戻さない。Phase0〜3、全日付付き報告、固定台帳の証拠を保全する。

[全311文書の更新前byte/hash](../reports/investigation/documentation-refresh-20261014/baseline.json)・[今回更新142](142_documentation_refresh.md)から現在の更新と原文を追える。[data](../data/README.md)、[eval](../eval/README.md)、[reports](../reports/README.md)の入口も最新化した。

'''+table+'\n| [142_documentation_refresh.md](142_documentation_refresh.md) | 全ドキュメントの棚卸し・現行説明更新・原証拠保全・検証 |\n')
    print('Current status, rules, roadmap, handoff and document navigation rewritten')


def supplements():
    baseline=json.loads((RUN/'baseline.json').read_text(encoding='utf-8'))
    def original(name):
        row=next(e for e in baseline['files'] if e['path']==name)
        return (ROOT/row['archive']).read_text(encoding='utf-8-sig').replace('\r\n','\n')
    def write(name,text):
        (ROOT/name).write_text(text.strip()+'\n',encoding='utf-8',newline='\n')
    def prepend(name,note,start=None):
        text=original(name)
        title=text.splitlines()[0]
        rest=text[text.index(start):] if start else text[text.index('\n')+1:].strip()
        write(name,title+'\n\n更新: 2026-10-14 JST。'+note+'\n\n## 当時の資料・保存手順\n\n'+rest)
    common='最新の判断は[結果141](141_chat_lr_comparison_results.md)と[状態](autonomous_status.md)。Base/Chat未完成・未採用、追加研究・学習は停止中。現在は[全ドキュメント更新142](142_documentation_refresh.md)のみ。'
    root=original('README.md')
    root=root.replace('文書・保存一覧・ローカルcommitの納品確認をそろえて停止します。','結果commit89275a8・納品commit09f338eと360ファイルの保存照合まで完了して停止しました。現在の依頼は全ドキュメントの最新化のみです。')
    root=root.replace('- [状態](docs/autonomous_status.md) / [ロードマップ](docs/15_project_roadmap.md) / [文書一覧](docs/README.md)。',
        '- [状態](docs/autonomous_status.md) / [ロードマップ](docs/15_project_roadmap.md) / [文書一覧](docs/README.md) / [全文書カタログ](docs/document_catalog.md) / [更新142](docs/142_documentation_refresh.md)。')
    root=root.replace('[最新結果138](docs/138_chat_semantic_diversity_results.md)','[前回教材結果138](docs/138_chat_semantic_diversity_results.md)')
    write('README.md',root)
    prepend('docs/09_prior_art_and_baselines.md',common+' 外部model card・論文は2026-10-02調査時点の記録で、今回最新revision・規模・利用条件を再調査したものではない。外部baselineを実比較へ採用する場合は別の比較契約で確認する。JMicroは外部baselineとの同条件品質比較・正式採用が未達。T4K NoNormの選定やSFT実行を日本語会話の成功へ読み替えない。',start='## ')
    prepend('docs/11_technical_research_gaps.md',common+'''\n\n## 現在の課題と解決に必要な証拠

| 課題 | 最新の証拠 | 改善を判断する方法 |
|---|---|---|
| 内容への応答不足 | 141新DEV内容20/80、文法66/80中46件は関連性不足 | 次介入は入力の対象・人物・数量・時点の失敗へ対応する仮説1件を既存証拠から定義。全回帰と原内容gateで判断 |
| 訂正・自己履歴の保持不足 | 新DEVの提供履歴11/24、自己履歴5/24 | 両履歴を分けた対照が必要。自己履歴だけを単独原因と決めない |
| 学習後半の汎化悪化 | 候補TRAIN NLL低下に対し新DEV NLL2.275270→2.689941 | 教材適合と未知能力を区別し、主要変更1つ・同教師量・新DEVで比較。追加周回で救済しない |
| 反復・停止・文字破損 | 141の全回帰とraw failuresが未達 | 原decodeで非退行・全文字失敗0を判定。表示修正・制約decodeは別policy |
| 独立確認不足 | fresh seed43・人間blind・正式保持/fullDEV/封印TEST未実行 | 有資格recipeと必要runner接続が先。CPU準備/生成seed/非blind採点では代用不可 |
| Base採用不足 | 123のBPB改善でも生成条件未達、後続SFTも不採用 | 124の原品質・10Mで1介入を選ぶ別の再開判断。大型化や閾値変更を使わない |

Chat trainer、document sampler、SFT全state再開、rollout、固定教師量比較は実装・実GPU実行済み。Phase0〜5基盤、元10B学習、後続の多数比較も完了済み。本学習前・Chat未実装という当時の記述は現在の説明ではない。どの次介入が有効かは未確定で、今回追加の診断・学習は開始しない。
''',start='## 結論')
    prepend('docs/12_training_implementation_research.md',common+' 現行nativeはNoQK-Norm/SwiGLU/13層/10,001,152。BaseのWSD stable/decay・StableExtensionTrainerと、Assistant教師量を管理するTeacherChatTrainer/document samplerは実装・実行済み。最新139はbatch32/context1024/BF16/math/compile=false/固定paddingで、同条件25CUDA検証更新と全state再開一致を確認した。\n\n全state・実消費列の不変条件は[学習計画06](06_training_plan.md)。旧Flash/compileの入力tokens/秒・LR0.002・500M開始案を、現在のSFT教師速度・採用recipe・開始指示にしない。ReLU²、共有block、KD等の閉じた条件は[全体125](125_project_retrospective.md)から原reportへ戻る。下の公式資料の引用と算術例は当時の研究記録。',start='## ')
    prepend('docs/13_tokenizer_dialogue_data_research.md',common+' 固定4096 Tokenizer・特殊ID0〜7を維持し、会話bodyは個別encode、role/EOTを構造IDで挿入する。Assistant本文+EOTのみの教師mask、document sampler、教師量正規化のscheduleと全state保存再開は実装・SFT実行済み。最新はaccepted TRAIN41,529 target・660,109教師/周と280sample QAの再利用。SFT実消費1,899,557教師と新規教材量を区別する。\n\n最新のTRAIN適合と未知NLL/内容不足は[141](141_chat_lr_comparison_results.md)。50〜100B供給や10M/30M/100M SFT量の初期案は自動的な実行量ではない。元Chat TEST準備解析事故を保存し、将来有資格Chat確認には新しい封印TESTが必要。評価本文をTRAINへ移さず、raw Unicode失敗をdecode修正で免除しない。下のsource候補・研究・規模は調査当時の記録。',start='## ')
    prepend('docs/14_evaluation_deployment_research.md',common+' Base/Chatの生成・内容評価・自己履歴評価・保存再開は実施済みだが正式品質は未採用。最新141は28セット/6,132判断/NLL7点、全回帰・停止・反復・raw文字の原gateを適用した。独立人間blind・独立学習seed43・全文/封印TESTは未確認。\n\nPhase3のHF/native float GGUF・量子化型の容量や、初期NoNorm CPU profileの変換確認は基盤の証拠。最新SFT重みのexport/量子化・RSS/CPU速度・独立環境・配布完成へ読み替えない。5〜10MB級は将来目標で、量子化は採用floatモデルとの許容退行を事前固定してから別の実行判断。下の当初の候補・gate・計算例は採用済み能力ではない。',start='## ')
    protocol=original('docs/evaluation_protocol.md')
    body=protocol[protocol.index('## 評価対象とsplit'):]
    body=body.replace('Phase 7でモデル生成を履歴へ戻すrolloutを追加し、dialogue全体の失敗も測る。','後続の限定SFTではモデル生成を戻す実履歴24会話59turnを評価済み。v1固定履歴と各実験の分母は別に保存する。')
    body=body.replace('Chat rubric/rollout、人手による誤検知確認は今後の検証に残る。','後続Chatのrubric/実履歴評価は実行済み。独立人間blindと人間による誤検知確認は未確認。')
    body=body.replace('複数source mixture samplerとstable予算延長forkは未実装。','この当時の準備では複数source mixture samplerとstable予算延長forkは未実装だった。後続の明示forkとChat document samplerは別の実装・証拠を持つ。')
    write('docs/evaluation_protocol.md','''# 評価仕様と現行の適用

更新: 2026-10-14 JST。機械可読の正本[protocol.json](../configs/evaluation/protocol.json)のv1 split・閾値・数値契約は変更しない。[最新結果141](141_chat_lr_comparison_results.md)と[状態](autonomous_status.md)は実際の採否。Base/Chat未完成・未採用、今回は文書更新のみ。

## v1契約と後続実験を区別する

最新139は4suite×219応答×7点の28セット/6,132内容判断とNLL7点×2,634 target。各suiteは固定履歴80、抑制なし80、自己生成履歴24会話59turn。原品質を維持し、最終t3の全回帰・内容56/80・自己文脈15/24・停止76/80と57/59・empty上限4/2・role/raw Unicode/履歴削除0、対照比反復非増加、新DEV family paired CI下限>0を判定して不採用。実験別の分母とguardは[凍結139](139_chat_lr_comparison_plan.md)を参照し、v1の文脈30問へ混ぜない。

Chatの全内容判断はCodex非blind。独立人間blind、fresh学習seed43、正式保持、全文DEV・最終suite、選定封印後TESTと正式採用は未確認。既存のhuman_scoresのnullをCodex評価で上書きしない。

元Chat TEST20行は139準備時にCPU構文解析した。学習・GPU評価への使用0だが未参照とは呼ばない。将来の有資格Chat最終確認には新たな封印TESTが必要。元Base TESTはこの事故では解析していない。raw EOT/EOS/反復/不正UTF8/置換文字を維持し、制約decodeと表示policyは別に記録する。

以下は凍結v1の設計契約・式・rubricと、その時点の基盤検証。途中の利用状況や計画は現在の採否・再開許可ではない。

'''+body)
    prepend('docs/124_base_recovery_plan.md',common+' このBase復旧は未再開・介入未選定。低LR139も141で不採用に閉じたが、Base単独原因を実証したものではない。以下の段階0〜5、10M、原品質・保持条件、独立確認と合格Baseで通知・停止を維持する。既存raw/全80判断を再利用し、文書更新だけで新しい診断や教師量を選定しない。',start='## 目指す状態と現在の判断')
    retrospective=original('docs/125_project_retrospective.md')
    body=retrospective[retrospective.index('記録日:'):]
    write('docs/125_project_retrospective.md','''# JMicro-10M 調査・検証・学習の全体記録

更新: 2026-10-14 JST。最新は[低LR結果141](141_chat_lr_comparison_results.md)。Base/Chat未完成・未採用、追加研究・学習は停止中。現在は[全文書更新142](142_documentation_refresh.md)のみ。

## 固定revision後の比較と判断

| 後続比較 | 実際の証拠 | 判断 |
|---|---|---|
| Chat-first128 / 教材131 | [129](129_chat_first_sft_execution.md) / [132](132_chat_improvement_execution.md) | 実学習・評価を完了、品質未達で不採用 |
| 教材汎化133 | [136](136_chat_generalization_results.md)、14セット/3,066判断/NLL7点 | 不採用。動的padding24検証更新も数値差で拒否 |
| 意味教材135 | [138](138_chat_semantic_diversity_results.md)、21セット/4,599判断/NLL7点 | 不採用、条件付き保持/sampling未実行 |
| 低LR139 | [141](141_chat_lr_comparison_results.md)、28セット/6,132判断/NLL7点、3,646更新/1,899,557教師 | 新内容差+8.75ポイント、CI−1.25〜+18.75。全原gate・反復/文字も未達、不採用 |

低LR候補の新/138/133/元旧内容20/18/19/15 of80、自己文脈5/5/5/1 of24。7条件分岐は候補なしで未実行・passed=false・品質未確認。結果commit89275a8・納品commit09f338eの保存とGit内容を確認した。各比較の教師量/GPU時間を独立実験数として足さない。

教材適合が強く未知内容・提供/自己履歴の利用が不足すること、反復/停止/Unicodeの原失敗が残ることを確認した。Base単独原因・10M容量限界は未確定。元Chat TEST20行のCPU準備解析事故と訂正を保存し、有資格Chat最終確認には新たな封印TESTが必要。独立seed・人間blind・fullDEV・正式採用は未確認。

## 2026-10-09までの固定台帳

以下はrevision `2d48062f5e29f7cb4cc9a1eb4352aa304e44827c`を対象にした原記録の説明。11,289file・4,947JSON等の数を後続の全件数へ書き換えない。[全文書カタログ](document_catalog.md)から現在の説明・日付付き報告・固定台帳を区別できる。

'''+body)
    prepend('docs/base_experiment_lookup.md',common+' Baseの最新固定不採用は[123](123_base_teacher_decay_2b_results.md)。後続Chatは[136](136_chat_generalization_results.md)→[138](138_chat_semantic_diversity_results.md)→[141](141_chat_lr_comparison_results.md)で閉鎖した。[全文書カタログ](document_catalog.md)と[全体125](125_project_retrospective.md)を入口にし、下の20261008索引を後続Chatまでの最新全件監査と扱わない。文書更新では索引再生成・GPU/data診断を実行しない。',start='現在の実状態は ')
    prepend('docs/retrospective/README.md','[最新結果141](../141_chat_lr_comparison_results.md)、[現在の状態](../autonomous_status.md)、[全体記録125](../125_project_retrospective.md)から後続のChat比較を読む。固定台帳本体のrevision・記録数・原キー・採否は変更していない。今回の[全文書カタログ](../document_catalog.md)と[更新142](../142_documentation_refresh.md)は後続文書までの入口であり、原台帳の対象範囲を拡張した再抽出・再採点ではない。')
    prepend('docs/126_model_archive.md',common+' 公開について下に示すrevision・manual gated・照合件数は2026-10-09の保存作業の実記録。今回Hubの現在設定・依存を再確認したものではない。公開版は主要3Base系列でdatasetとsamplerを含まず、後続Chat重みの公開や厳密ローカル再開の代替ではない。最新低LR全stateは[引継ぎ](windows_handoff.md)にあり、新しいpush/公開を行わない。',start='## ')
    prepend('docs/huggingface_handoff.md',common+' 新PC・欠損時の固定pilot/Tokenizer復元の補足。既存環境の再取得・Tokenizer学習は不要。主要3Base系列の2026-10-09公開保存は[126](126_model_archive.md)を参照し、後続SFT重み・dataset・samplerを公開済みとしない。最新ローカル納品は89275a8/09f338eで、当時のpush許可を今回へ引き継がない。以下のpayload/hash・bundle revisionは不変の保存契約で、今回再download・学習・外部設定の再調査をしていない。',start='## ')
    ui=original('docs/43_local_webui.md')
    body=ui[ui.index('## 使い方'):]
    body=body.replace('採用済み10B評価','当時の保存10B評価')
    write('docs/43_local_webui.md','''# 元10B BaseモデルのローカルWebUI

更新: 2026-10-14 JST。URLは **http://127.0.0.1:7860**。このUIは10,001,152 parameters・10,000,007,168 tokensの元Baseで文章の続きを生成する。最新の低LR Chat候補へ置き換えていない。後続SFTは[141](141_chat_lr_comparison_results.md)まで実行したが不採用で、UIの元Base自体も品質未採用。[状態](autonomous_status.md)。

保存された最新科学観測2026-10-13T16:54:20ZはPID309447/boot4052bfc5-3850-44e4-9123-d34a9e19f36e/start55170810、親SHA `410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290`、Tokenizer/10M・busy=false・kernel lock一致。これは現在の生存保証ではない。稼働中は重複起動せず、終了jobを再起動しない。

以下のUI操作・起動停止はユーザーが利用する時の手順。現在の文書更新ではサーバー起動・生成・GPU評価を行わない。表示補修をraw Unicode失敗の免除や品質合格へ数えない。

'''+body)
    write('docs/codex_automation.md','''# 自律runnerの現在の運用

更新: 2026-10-14 JST。[状態](autonomous_status.md)、[AGENTS](../AGENTS.md)、[最新結果141](141_chat_lr_comparison_results.md)を読む。前の3項目の比較・条件分岐・納品は不採用で完了し、現在の目標は[ドキュメント更新142](142_documentation_refresh.md)のみ。研究・data準備・診断・評価・GPU学習は停止中。

## 実行範囲と完了を区別する

権限が利用可能でも、現在の依頼で許可された範囲を越えない。文書依頼を研究の再開として扱わず、古いrunning/PID/next_actionを起動指示にしない。通常判断で許可を繰り返し求める必要はないが、OS昇格・restart・credentials・有料cloud・外部送信/公開等はそれぞれの境界に従う。

`continue`は許可範囲の有用な作業が残る状態、`needs_user`は外部操作が必要、`complete`は依頼範囲を現在の証拠で完了した状態。比較・文書の完了をBase/Chatの正式採用へ読み替えない。条件付き独立確認は有資格候補なしなら未実行・品質未確認と記録する。

## 保存と再開

プロジェクトのrunnerは[scripts/run_codex_autonomous.py](../scripts/run_codex_autonomous.py)と[profile installer](../scripts/install_codex_autonomous_profile.ps1)。これらの準備・stub試験は実Codex/GPUの成功証拠ではない。runner/CLIの製品versionや設定は今回確認・変更していない。2026-10-03のCLI0.159.3・権限画面・profile例は[更新前原文](../reports/investigation/documentation-refresh-20261014/baseline.json)の歴史資料として保全した。古い「環境から学習まで継続」のpromptを現在の依頼へ適用しない。

長期jobと無人runnerは別機能。再開する実jobがある場合はPID/boot/start・GPU lock・終端result・valid checkpointを照合し、同凍結条件の完了updateから再開する。観測timeoutだけで終了と扱わず同じhandleを確認し、終了したpilot/128/131/133/135/139は再起動しない。

Pythonはrunner・tests・one-offを含め`uv run --frozen`、Python3.12.7、通常WSL extras `--extra hub --extra data --extra ml --extra export`。source/data/config・logs・全state・消費カウンタを保存し、GPU診断・学習を文書更新の確認へ追加しない。

今回の文書更新は[全文書カタログ](document_catalog.md)、原byteの保全、現行説明とリンク、Windows/WSL一致、ローカルcommitの証拠で判断する。Git正本はWindows、identityは`yousan <ka1357amnbpdr@gmail.com>`。push/公開は今回の範囲に含まない。
''')
    # Directory READMEs describe live navigation and the older details retain
    # their own observation dates. The immutable dataset files are not parsed.
    prepend('data/README.md','最新は[結果141](../docs/141_chat_lr_comparison_results.md)と[引継ぎ](../docs/windows_handoff.md)。研究・data準備・学習は停止中、[文書更新142](../docs/142_documentation_refresh.md)のみ。Base/Chat未完成・未採用。元Web TRAIN12,225,819,077 tokens、accepted混合2B、後続SFTは別系列。最新139は以前のaccepted TRAIN41,529 target/660,109教師/周/280sample QAを再利用し、新教材0。TRAINはWSL data rootのsemantic系列、新DEV/固定NLLはphase7/chat-lr-20261014。\n\n教材の実体はGitや公開モデルarchiveに含まない。小metadata・原出力・教師量を教材実体の復元保証へ読み替えない。元Chat TEST20行のCPU準備解析事故を保存し未参照の主張を取り消した。新しい有資格Chat最終確認には封印TESTが必要。本文書更新でdataset/TESTを開封・再処理していない。下の初期pilot/拡張手順は履歴・欠損時の契約で再build指示ではない。',start='## ')
    eval_text=original('eval/README.md')
    rest=eval_text[eval_text.index('この評価例はプロジェクト用'):]
    rest=rest.replace('後者はPhase 7で加える。','後続SFTの実自己履歴24会話59turnは実施済みで、実験別reportに別の分母を保持する。')
    write('eval/README.md','''# 固定評価データと現在の利用状況

更新: 2026-10-14 JST。[最新結果141](../docs/141_chat_lr_comparison_results.md)は全28セット・6,132判断・NLL7点、全原gateで不採用。Base/Chat未完成・未採用、再採点・生成評価・TEST利用は停止中。現在は[文書更新142](../docs/142_documentation_refresh.md)のみ。

## 未参照と利用済みを区別する

元v1のBase/Chat各DEV80/TEST20とsplit/hashは不変。Chat DEVは後続SFTで利用済み。元Chat TEST20行も139のCPU準備で構文解析した事故があり、未参照とは呼ばない。学習・GPU評価には使用していない。将来有資格Chat確認には新たな封印TESTが必要。元Base TESTはこの事故では解析していない。今回の文書更新でもdataset/TESTを解析・採点しない。

最新139は新DEVと138/133/元旧DEVの4suite。各固定履歴80・role抑制なし80・実自己履歴24会話59turnを別に保存した。既知12セット2,628判断の再利用は原prompt/履歴/token/bytes/checksまで同一の場合だけ。Codex非blindで、独立人間の成績ではない。

v1のhuman_scoresのnull、v2.1の[診断結果](../docs/46_japanese_base_evaluation_v2_results.md)、原raw・notes・停止/反復/Unicode失敗を保持。提供履歴と実自己発話履歴、DEV256/固定NLLと正式fullDEV、生成seedとfresh学習seedを混同しない。[現行適用と凍結評価契約](../docs/evaluation_protocol.md)。

## v1固定入力の契約

'''+rest)
    reports=original('reports/README.md')
    rest=reports[reports.index('## モデル保存・公開'):]
    rest=rest.replace('最新Chat結果は[136]','2026-10-13当時のChat結果は[136]')
    write('reports/README.md','''# 実験台帳と検証結果

更新: 2026-10-14 JST。最新は[低LR結果141](../docs/141_chat_lr_comparison_results.md)。Base/Chat未完成・未採用、研究・data準備・診断・評価・学習は停止中。現在は[全ドキュメント更新142](../docs/142_documentation_refresh.md)のみ。

## 最新139の保存記録

| 記録 | 実際の範囲 |
|---|---|
| [completion](phase7/chat-lr-20261014/completion.json) | 全28セット/6,132判断/NLL7点×2,634、実学習/全state/原採否/資源/元UIの科学監査 |
| [selection](phase7/chat-lr-20261014/selection.json) / [analysis](phase7/chat-lr-20261014/final_analysis.json) | 全4回帰・主paired CI・全保存点・NLL。候補不合格 |
| [branches](phase7/chat-lr-20261014/conditional_branches.json) | 7分岐は候補なしで未実行・passed=false・品質未確認 |
| [TEST準備事故](phase7/chat-lr-20261014/protected_split_incident.json) | 元Chat TEST20行のCPU解析と訂正。未参照という主張を取り消し新封印版が必要 |
| [保存一覧](phase7/chat-lr-20261014/final_archive.json) / [納品記録](phase7/chat-lr-20261014/final_delivery_checks.json) | 当時360ファイルと結果89275a8/納品09f338eを照合。重み/dataはWSL |
| [今回の全文書baseline](investigation/documentation-refresh-20261014/baseline.json) | 更新前311文書のbyte/hash・分類。研究再開ではない |

以前のmanifest/納品記録は作成時点のGit revision/snapshotの証拠で、現行文書を更新しても原記録へ新しいhashを代入しない。日付付き報告と固定台帳を[全文書カタログ](../docs/document_catalog.md)から区別する。後続の一意な総GPU・教師量を既存report行の単純合算から認証しない。

過去のChat[136](../docs/136_chat_generalization_results.md)・[138](../docs/138_chat_semantic_diversity_results.md)、Base[123](../docs/123_base_teacher_decay_2b_results.md)、[全体125](../docs/125_project_retrospective.md)・[固定revision台帳](../docs/retrospective/README.md)も保全。以下の「最新」は各節に記載された日付の履歴。

'''+rest)
    print('Research summaries, retrospective entries, WebUI and all directory READMEs refreshed')


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('mode',choices=('snapshot','update','operations','supplements','catalog','anchors','verify'))
    parser.add_argument('--commit')
    parser.add_argument('--receipt-commit')
    args=parser.parse_args()
    {'snapshot':snapshot,'update':update,'operations':operations,'supplements':supplements,'catalog':catalog,'anchors':inbound_anchors,'verify':lambda:verify(args.commit,args.receipt_commit)}[args.mode]()
