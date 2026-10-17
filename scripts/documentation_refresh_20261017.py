"""Documentation inventory, byte preservation and delivery; no research execution.

Run with the repository's pinned uv Python. Windows is the Git authority.
Only documentation, this helper and its dated audit directory may change.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from functools import cache
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
from refresh_project_documents import OPERATIVE, anchors

ROOT = Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m')
WSL = Path('/home/aihub_ubuntu/src/japanese-tiny-llm-10m')
PREFIX = 'reports/investigation/documentation-refresh-20261017'
RUN = ROOT / PREFIX
GIT = '/mnt/c/Program Files/Git/cmd/git.exe'
WIN = r'C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m'
LIVING = set(OPERATIVE) | {'docs/document_catalog.md', 'docs/145_post_rejection_next_plan.md'}
NEW = {'docs/148_latest_base_and_documentation.md'}
HELPER = 'scripts/documentation_refresh_20261017.py'
RESULT = 'reports/phase6/rdrop-science-20261016/completion.json'


def now():
    return datetime.now(timezone.utc).isoformat()


def git(*args):
    return subprocess.run([GIT, '-C', WIN, '-c', 'core.quotepath=false', *args],
                          check=True, capture_output=True).stdout.decode('utf-8').strip()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')


def mirror(name):
    destination = WSL / name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / name, destination)
    assert sha(ROOT / name) == sha(destination), name


def category(name):
    if name in LIVING | NEW:
        return 'living'
    if '/originals/' in name or '/previous_docs/' in name:
        return 'provenance_copy'
    return 'dated_or_frozen_history'


def baseline():
    assert not (RUN / 'baseline.json').exists(), 'Never overwrite a baseline'
    assert not git('status', '--porcelain', '--untracked-files=no'), 'Tracked baseline must be clean'
    names = sorted(n for n in git('ls-files', '-z').split('\0') if Path(n).suffix.lower() in ('.md', '.rst'))
    assert not git('ls-files', '--others', '--exclude-standard', '--', '*.md', '*.rst')
    existing = {}
    for name in names:
        if category(name) == 'provenance_copy':
            existing.setdefault(sha(ROOT / name), name)
    records = []
    created = []
    for name in names:
        p = ROOT / name
        digest = sha(p)
        snapshot = existing.get(digest)
        if snapshot is None:
            snapshot = f'{PREFIX}/originals/{digest}{p.suffix}'
            destination = ROOT / snapshot
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(p.read_bytes())
            mirror(snapshot)
            existing[digest] = snapshot
            created.append(snapshot)
        assert sha(ROOT / snapshot) == digest
        text = p.read_text(encoding='utf-8-sig')
        records.append(dict(path=name, sha256=digest, bytes=p.stat().st_size,
                            category=category(name), snapshot=snapshot,
                            title=next((s.lstrip('# ').strip() for s in text.splitlines() if s.startswith('#')), p.stem)))
    refs = ['src/jmicro/model.py', 'src/jmicro/training.py', 'src/jmicro/tokenizer.py', 'uv.lock',
            'src/jmicro/isolated_full_dev.py', 'scripts/rdrop_science_protocol.py',
            'scripts/run_rdrop_science.py', 'scripts/run_rdrop_science.ps1', 'scripts/review_rdrop_science.py',
            'configs/phase6/rdrop_science_20261016.json', 'configs/evaluation/protocol.json',
            'configs/phase6/base_parallel_residual_review.json', RESULT,
            'reports/phase6/rdrop-science-20261016/review.json',
            'reports/phase6/rdrop-science-20261016/notes.json',
            'reports/phase6/rdrop-science-preparation-20261016/authorization.json',
            'reports/phase6/scalegrad-science-20261015/completion.json',
            'reports/phase6/isolated-full-dev-preparation-20261015/completion.json']
    value = dict(captured_at=now(), initial_commit=git('rev-parse', 'HEAD'),
                 all_document_paths=len(records), category_counts=dict(Counter(r['category'] for r in records)),
                 documents=records, new_original_copies=created,
                 frozen_references={n: sha(ROOT / n) for n in refs},
                 scope='All tracked Markdown/RST, including source snapshots and provenance copies. No corpus, model weights or TEST reads.')
    save(RUN / 'baseline.json', value)
    mirror(f'{PREFIX}/baseline.json')
    print(json.dumps({k: value[k] for k in ('initial_commit', 'all_document_paths', 'category_counts')}))
    print('new_original_copies', len(created))


def read_baseline():
    return json.loads((RUN / 'baseline.json').read_text(encoding='utf-8'))


def original(name):
    r = next(r for r in read_baseline()['documents'] if r['path'] == name)
    return (ROOT / r['snapshot']).read_text(encoding='utf-8-sig')


SCOPE = '更新: 2026-10-17 JST。現在の依頼は「ドキュメントをすべて最新にして」。元の「4まで」の目標は未達のままユーザーが解除した。今回の作業範囲は文書更新・棚卸し・保存検証・ローカルGitコミット。Base/Chatは未完成・未採用。'
STATE = '最新のRDrop25M比較は4,420更新・正確25,000,000教師まで完了し、不採用で固定条件を閉鎖した。対照→候補は一貫性1→3/80、適切完結3→6/80、EOS11→19/80、反復53→49/80。BPBは0.9927168291→1.0279654060（3.5507%悪化）。全80件を理由付きで確認したCodex非blind評価で、独立人間blindではない。'
RESOURCE = 'ユーザーの「上限はないので無限に使っていいです」により、ローカルGPUの累積利用時間に上限はない。旧180/4800秒による閉鎖判断は当時の契約として保全する。今後の各比較には実行前の有限な教師量・時間上限・評価保存枠・終了条件が必要。累積上限解除は今回の文書依頼を学習再開へ変えるものではない。'
PENDING = '有資格のBase recipe、親の事前学習からやり直す真にfreshな独立学習seed43、実全文DEV、標準400生成＋長文40の全内容、新しい封印TEST、採用・復旧確認は未達。次の比較は未選定・未凍結。終了した条件の再起動や閾値緩和で進めない。'
BOUNDARY = 'DEV専用readerと隔離生成・reviewは実装済み。全文DEV集計/440生成の接続部品も36 CPU checksまで完了したが、実モデルの全文評価ではない。Python open監査はnative OS sandboxではなく、資格・独立全pipeline証拠を検証する永続native runner等の接続は未完成。'
EXPOSURE = '元Base TEST20 promptと元Chat TEST20行には別々のCPU解析履歴がある。学習・GPU TEST採点への使用0とCPU未開封は区別する。有資格recipeと選定封印後に新しい封印TESTが必要。今回の文書作業ではデータ本文・TEST・重みを読まない。'


def href(name, target):
    import posixpath
    return posixpath.relpath(target, posixpath.dirname(name) or '.')


def links(name):
    items = [('最新結果・更新記録148', 'docs/148_latest_base_and_documentation.md'),
             ('現在の計画145', 'docs/145_post_rejection_next_plan.md'),
             ('文書一覧', 'docs/README.md'), ('全件カタログ', 'docs/document_catalog.md')]
    return ' / '.join(f'[{label}]({href(name, path)})' for label, path in items) + '。'


def evidence(name):
    return f'[RDrop完了記録]({href(name, RESULT)}) / [原採点・全guard]({href(name, "reports/phase6/rdrop-science-20261016/review.json")}) / [GPU上限解除記録]({href(name, "reports/phase6/rdrop-science-preparation-20261016/authorization.json")})。'


def write(name, body):
    p = ROOT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body.rstrip() + '\n', encoding='utf-8', newline='\n')
    if name in LIVING:
        r = next(r for r in read_baseline()['documents'] if r['path'] == name)
        missing = sorted(anchors(ROOT / r['snapshot']) - anchors(p))
        if missing:
            with p.open('a', encoding='utf-8', newline='\n') as f:
                f.write('\n<!-- Historical incoming heading aliases. Original text is preserved in baseline snapshots. -->\n')
                f.write('\n'.join(f'<a id="{s}"></a>' for s in missing) + '\n')
    mirror(name)


def header(name, title=None):
    return '\n\n'.join((title or original(name).splitlines()[0], SCOPE, links(name))) + '\n\n'


TOPICS = {
    'data/README.md': 'accepted TRAINはWeb75%・textbook20%・story5%の既存poolを再利用。最新RDropの教師25Mは追加のuniqueデータ25Mではない。2回のdecoderでhardgold CE評価50M/整合対25Mとなる。入力・教師・source・bytes・EOS・digestの元streamを対照と照合した。dataset/samplerの実体はWSLに保全する。',
    'eval/README.md': '新しいDEV経路はDEV専用artifact/manifest/readerを使う。旧混在eval/base.jsonlの全行解析後filterへ戻さない。既知DEVの隔離であり未知DEVを作った証拠ではない。正式全件suiteとpilot80の特殊ID抑制は異なるため、rawと設定差を残す。',
    'reports/README.md': '最新の科学結果はreports/phase6/rdrop-science-20261016/。completion/review/result/training/notesとportable_artifactsが入口。全4,420履歴・型付き数値状態・主streamを監査し、80件の個別理由を保存した。checkpoint/Adam/RNG/sampler/全metricsはWSL。Windows/Gitには小さな原記録を保存し、portable viewを厳密再開の代替にしない。',
    'docs/01_project_goal.md': '最終成果物は約10Mの日本語Baseと、その後の短い会話を行うChat。日本語corpus→独自Tokenizer→スクラッチBase→Dialogue-oriented mid-training/Assistant本文+EOT SFT→採用float/量子化/ローカル利用という元目標を維持する。Baseが資格・独立学習・最終確認まで合格したら通知して停止し、後続Chatは別の再開範囲。',
    'docs/02_research_summary.md': 'Tokenizer/model/学習/再開基盤は成立している一方、文法やEOSの改善は意味の一貫性改善を保証しない。ScaleGradは文法44→71・反復53→6でも一貫性7/80、BPB悪化で不採用。RDropも一貫性3/80で不採用。SFT141までの失敗を含め、Base単独原因や10M容量限界は確定していない。外部論文の以下の記述は当時の調査記録。',
    'docs/03_architecture.md': '現参照はnative10,001,152 parameters。13層・hidden256・FFN640・4Q/2KV・head64・vocab4096・context1024・NoQKNorm/SwiGLU・tied embedding。最新RDropは学習時のみdropout/損失を追加し、推論構成・パラメータ数を変更していない。9層FFN1040および6層hidden384/FFN832の300M比較は既に不採用で、未検証案として再掲しない。9.5M〜10.1Mと原品質を維持する。',
    'docs/04_tokenizer.md': '固定4096 Tokenizer、構造ID0〜7、保護byteのencode/decode契約を維持する。SHA256はa7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318。モデル比較は同Tokenizer/common-byte BPB。既存4k/8k比較・Phase3変換を繰り返さず、不正UTF8のraw bytesを保存する。',
    'docs/05_dataset.md': '最新RDropは既存accepted TRAINの同25M教師/同source quotaであり、新規corpus作成ではない。TRAINとDEV/TESTを分離し、unique量と反復露出を区別する。既存受入・manifest・split証拠を再利用するが、独立の全corpus内容監査が完了したとは記載しない。',
    'docs/06_training_plan.md': '最新RDropは元10B親/fresh AdamW、LR1e-5・WD.1・batch48・seed42・同25M教師。2 stochastic viewsの平均CE＋.5×対称KL、学習時dropout.1で両viewへ勾配。固定recipeは品質不合格で閉鎖済み。全state保存再開の技術合格を品質合格へ置き換えない。独立seed43には親の事前学習を含む全pipelineが必要。',
    'docs/07_environment.md': 'Git正本はWindows、実行・大容量data/重み/samplerはWSL。Python3.12.7/uv frozen、WSL2/Linux disk/RTX4090が記録された環境。最新runの科学GPU777.297900秒を台帳へ全額加算済み。過去の高速Flash/compile速度をfresh独立native pipelineの見積りに流用しない。機器・package・PIDの値は観測時点の記録。',
    'docs/08_evaluation.md': '最新RDropはDEV256 BPB/Japanese診断と全80のraw/prefix/停止/反復/内容を確認して不採用。paired一貫性差+2/80、95%CI[0,.0625]は元+8/CI下限>0を満たさない。文法47/80・一貫性3/80等の絶対条件も未達。Codex非blind、独立人間blind未実施。',
    'docs/09_prior_art_and_baselines.md': 'akebono等の外部資料は当時の調査であり、今回最新revision/条件を再調査していない。外部10M表記やblock規模を総trainable数と混同せず、同条件の外部品質比較は未実施。NEFTuneは一次資料と適合性を確認したが根拠不足で未選定、実験で品質否定した手法ではない。',
    'docs/11_technical_research_gaps.md': '優先課題は意味の循環・因果/数量の誤りを改善する根拠ある未回答仮説、資格あるrecipe、独立fresh全pipeline、永続native fullDEV/TEST接続、必要な全内容/人間blind証拠。DEV読取り隔離と全文CPU部品は既に準備済みなので、未着手の一般reader修理を次の作業に戻さない。単独原因は未確定。',
    'docs/12_training_implementation_research.md': 'RDropの通常lossは最大48×1024二重graphでOOM、解析VJP/CPU一括target runtimeは全数値・再開・cache照合に合格。その当時は旧累積予算で科学を閉鎖したが、新資源契約で初めて科学25Mを実施し品質不合格だった。技術合格・旧費用閉鎖・今回品質拒否を区別し、閉じたprobeを再実行しない。',
    'docs/13_tokenizer_dialogue_data_research.md': 'Tokenizer4096と構造token挿入、Assistant本文+EOT教師maskを維持。直接SFTと後続教材/汎化/低LR比較は141まで不採用。追加SFTやmid-trainingが解決するという実証はない。現在の文書作業と、将来のBase資格確認、さらに後続Chat実験を区別する。',
    'docs/14_evaluation_deployment_research.md': 'Base/Chatとも未採用。Phase3のrandom-weight HF/native float GGUF、量子化型/容量確認は基盤で、学習済み量子化品質・配布完成ではない。正式float採用後に品質退行・実容量・CPU速度・独立環境を別段階で確認する。',
    'docs/huggingface_handoff.md': '2026-10-09の主要3Base系列のpublic/manual-gated保存は当時の記録。後続Chat/ScaleGrad/RDrop等の候補を公開した記録ではない。dataset/samplerを除く保存はnative厳密再開の代替ではない。固定pilot/Tokenizerのrevision/hashと欠損時復元手順を維持し、旧push許可を新しい公開の許可にしない。',
    'docs/126_model_archive.md': '2026-10-09の主要3Base系列・Tokenizer・数値学習状態の保存契約1544 files/396038805 bytes/revision853d52d2323653331b610249912fbe25615615fcは歴史記録。dataset/sampler除外。後続Chat/ScaleGrad/RDropはこの保存に含まれない。今回はHub照会・変更・公開を行っていない。',
    'docs/retrospective/README.md': '固定台帳は入力revision2d48062f5e29f7cb4cc9a1eb4352aa304e44827cの集合を維持する。今回living入口だけを最新RDrop/計画145へ接続し、当時のcoverage/experiment_records/source SHAへ後続実験を混ぜない。最新までの追加概要は148と全体総覧125を参照する。',
}


def technical_tail(name):
    body = original(name)
    pos = body.find('\n## ')
    if pos < 0:
        return ''
    tail = body[pos:].lstrip()
    tail = re.split(r'\n<!-- (?:Original heading aliases|Historical incoming)', tail)[0].rstrip()
    for marker in ('## 当時の資料・保存手順', '## 更新前の本文・契約（当時の記録）'):
        if tail.startswith(marker):
            tail = tail[len(marker):].lstrip()
    return ('## 設計・手順の保存記録\n\n以下は作成時点の仕様・調査・復元手順。途中の「最新」「次は」「未実施」やPIDはその時点の記録で、現在の状態は本ページ冒頭と148を参照する。外部サービス/依存の最新仕様は今回再照会していない。\n\n' + tail + '\n')


def quality():
    return '''DEV80の絶対条件は文法2≥56、一貫性2≥27、適切完結≥27、EOS≥37、規定反復≤18、empty/role/Unicode失敗0。相対一貫性差≥8、paired CI95下限>0、BPB/strong/cached/historical保持も必要。最終TEST停止95%は別条件であり、DEVのEOS37/80で代替しない。総trainable9.5M〜10.1M、参照10,001,152を維持し、日本語領域・元品質を勝手に狭めたり下げたりしない。'''


def ui():
    return '''RDrop終了記録の観測2026-10-16T15:06:52.7804980Z（JST10月17日）では、科学WSL PID459024/start80531912とWindows32704は終了。元UIはPID459564/start80610052、boot4052bfc5-3850-44e4-9123-d34a9e19f36e、元10B親/Tokenizer/native10M・idle HTTP・kernel FLOCK一致で復帰済み。これは時点付き証拠で現在の生存保証ではない。今回の文書作業ではHTTP/生成/再起動を行っていない。'''


def apply():
    # Topics preserve the original technical body explicitly as historical material.
    for name, topic in TOPICS.items():
        write(name, header(name) + topic + '\n\n' + STATE + '\n\n' + BOUNDARY + '\n\n' + PENDING +
              '\n\n' + RESOURCE + '\n\n' + EXPOSURE + '\n\n' + evidence(name) + '\n\n' + technical_tail(name))
    name = 'README.md'
    write(name, header(name) + '''約1,000万パラメータで自然な日本語の続きを生成し、その後に短い会話を行うモデルを目指す研究プロジェクトです。モデル・Tokenizer・学習評価基盤をスクラッチで構築しています。

''' + STATE + '\n\n' + evidence(name) + '''

| DEV80指標 | 同25M対照 | RDrop候補 | 元絶対条件 |
|---|---:|---:|---:|
| 文法成立 | 44 | 47 | ≥56 |
| 一貫性成立 | 1 | 3 | ≥27 |
| 適切な完結 | 3 | 6 | ≥27 |
| EOS停止 | 11 | 19 | ≥37 |
| 規定反復 | 53 | 49 | ≤18 |

意味の循環や因果・数量の誤りは残っています。EOS/反復flagだけの改善を能力完成とせず、この固定recipeは不採用です。10Mの限界や単独原因が証明されたわけではありません。

''' + PENDING + '\n\n' + RESOURCE + '''

## 現在の作業と次の計画

今回は全ドキュメントの更新です。DEV readerの隔離と全文CPU評価部品は準備済みですが、正式な独立学習・全文評価・最終TESTの接続と実証は残っています。将来の研究再開時は、既存の結果を根拠に新しい比較を最大1件定義します。[計画145](docs/145_post_rejection_next_plan.md)。

## 基盤と履歴

native10,001,152 parameters、13層/hidden256/FFN640/GQA4Q2KV、Tokenizer4096、context1024です。モデル/Tokenizer、WSLでの実学習、全state保存再開、各種評価は実装済みです。

Baseの文書長重み、進行長補助、ScaleGrad、今回RDrop、およびSFT141までの固定比較は不採用です。[総覧125](docs/125_project_retrospective.md)・[実験検索](docs/base_experiment_lookup.md)から原記録をたどれます。

## 保存したモデル

2026-10-09の[Hugging Face研究保存版](https://huggingface.co/japanese-data-analyze/JMicro-10M-research-archive)は、web-10b/staged-10p6b/teacher-decay-2bの当時の3系列です。ダウンロードは手動承認、dataset/samplerは含まず、後続候補の公開ではありません。[保存契約126](docs/126_model_archive.md)。10B/2Bは各系列の学習量で、パラメータ数は10Mです。

## ローカルで試す

元10B Base用の[WebUI](http://127.0.0.1:7860)を使います。[操作43](docs/43_local_webui.md)と[Windows/WSL引継ぎ](docs/windows_handoff.md)を参照してください。Git cloneに重み・大容量dataは含まれません。

## 開発環境

WindowsがGit正本、WSL2/Linux disk/RTX4090が実行環境。Python3.12.7をuvで管理し、全Pythonをuv run --frozenから実行します。欠損時の復元は[引継ぎ](docs/windows_handoff.md)、運用ルールは[AGENTS.md](AGENTS.md)。
''')
    name = 'AGENTS.md'
    old = original(name)
    rules = old[old.index('## Fixed model-size requirement'):]
    rules = re.split(r'\n<!-- Original heading aliases', rules)[0].rstrip()
    write(name, header(name) + STATE + '\n\n' + RESOURCE + '\n\n' + PENDING + '\n\n' + BOUNDARY + '\n\n' + EXPOSURE + '\n\n' + evidence(name) + '''

## Current documentation-only scope — 2026-10-17 JST

Inventory all Markdown/RST, including source snapshots and provenance copies. Update all living descriptions and plans, preserve dated/frozen scientific evidence and pre-edit bytes, verify links and Windows/WSL/Git delivery, then commit locally. The user cleared the unachieved four-item Base goal; do not mark it achieved or active. Documentation completion is separate from Base/Chat completion.

No research implementation, data/TEST preparation, runtime diagnostics, model inference/evaluation, new GPU training, old-job relaunch, dependency work, push/publication or external messages is authorized by this documentation request. The prior unlimited cumulative local GPU authorization remains valid for future authorized research; no repeat budget-cap question is required. Each future experiment still needs finite prospective teachers/timeouts, control, full-quality gates and stop conditions.

Latest scientific evidence is the rejected first RDrop25M run at commit cf113068. Its scientific process and Windows worker exited; original UI restoration is timestamped evidence, not current liveness. Full numerical histories, weights/Adam/RNG/sampler remain in WSL. Do not rehash/load model weights or scan corpora for documentation. Preserve every old closed condition and all carried GPU costs.

''' + rules + '''

The complete pre-refresh AGENTS progress chronology is byte-preserved through reports/investigation/documentation-refresh-20261017/baseline.json. Older “latest/live/active” paragraphs describe their own timestamps and do not override this scope.
''')
    name = 'docs/autonomous_status.md'
    write(name, header(name) + STATE + '\n\n' + evidence(name) + '\n\n' + RESOURCE + '''

## 完了した検証

- 第一回RDrop科学比較：元10B親/fresh Adam、同25M教師、4,420更新。全型付き状態・全履歴・元主streamを照合済み。
- 全80件の個別内容確認と原採否判定。paired一貫性差+2/80、CI95[0,.0625]、BPB3.5507%悪化で不採用。
- DEV入力の隔離と全文DEV/440 CPU接続部品。後者36 checksは合成fixtureの検証で実品質ではない。

## 未達事項

''' + PENDING + '\n\n' + EXPOSURE + '''

## 実行状態と保存

''' + ui() + '''

最新完了commitはcf113068。checkpoint-00004420.ptの全stateはWSLのreports/phase6/rdrop-science-20261016/、小raw/notes/receiptはGitに保全。累積台帳は技術169.2456279549515＋科学4241.304908989929＝4410.55053694488秒。これは当該継承台帳の範囲であり、プロジェクトの全歴史GPU時間の総計ではない。

## 現在の目標と次の行動

元「4まで」は未達のまま解除済み。現在の文書目標は、全件カタログ・現行説明・計画・原文保全・リンク/同期/Git検証まで。比較を実行したことや文書更新の完了をBaseの達成へ読み替えない。将来の順序は計画145を参照。
''')
    name = 'docs/145_post_rejection_next_plan.md'
    write(name, header(name) + STATE + '\n\n' + RESOURCE + '\n\n' + BOUNDARY + '''

## ここからの順序

| 段階 | 成果物と具体的な進め方 | 進行条件・現在の状態 |
|---|---|---|
| 今回 | 全文書の棚卸し、現行説明更新、原文保全、リンク/Windows-WSL/Git検証 | 文書だけを実行。研究目標は未達のまま解除済み |
| 1. 根拠のある次比較 | 原proposal/trainer/全件notes/結果を対応付け、意味の循環・因果/数量誤りの未回答仮説を最大1件選ぶ | 現時点は未選定・未凍結。既存width/ScaleGrad/RDrop等を未検証と呼ばない |
| 2. 実行前契約と必要実装 | 主要変更、対照、初期化/親、TRAIN/教師/seed/decoder、全品質条件、必要CLIを固定。技術probe・科学比較・独立全pipeline・最終評価の別段階予算を示す | 有限な教師量/時間上限、全既消費の継承、評価保存枠、成功/不採用/中断条件がそろうこと |
| 3. 最小技術gateと科学比較 | 必要なCPU数式/gradient、実CUDA最大shape/finite、全state保存再開、native cache、全計時を確認。新fresh条件で比較し全raw/理由/stream/状態を保存 | CPU準備を品質とせず、閉じたprobeや条件を再起動・救済しない。原採否未達なら固定条件を閉じる |
| 4. 主比較資格 | pilotの実測を根拠に別runの教師量/時間を前向き固定し、絶対/相対/strong/cached/historicalの全guardを判定 | 部分的なEOS/文法/BPB改善だけで進めない。有資格recipeはまだない |
| 5. 独立全pipelineと全文DEV | native永続runner/reviewerの型付き接続・資格証拠を実装し、親の初期化/事前学習から独立fresh seed43を実行。fullDEV・400生成＋長文40を全件確認 | 同学習済みseed42親からsampler/生成乱数を43へ変えるだけでは独立学習にならない |
| 6. 新封印TESTとBase採用 | 最終recipe選定を封印後、新しい別artifact TESTを用意し元最終基準で全件評価。weights/Tokenizer/config/復旧・採否を保存 | 全条件合格でBase完成を通知し停止。Chat/SFT・量子化・公開は別の再開範囲 |

## 既にできたことと実装の残り

DEV専用reader/manifest/生成review接続と全文DEV部品を一から作り直す計画には戻さない。全文集計は元89416文書/42003934本文token/164344743bytesを固定し、本文一度採点・EOS別集計・各ID/token/bytes照合・440 adapterを持つ。36 CPU checksは合成例であり、資格ある実モデルの全文DEVや440内容レビューは未実行。Python open監査の範囲を明記し、native OS隔離を完了扱いにしない。

残りは資格/全pipeline証拠を検証し永続化するnative runner、locks/予算/乱数/モード保全・失敗時停止、実fullDEV/全440の保存・全内容判定、新TEST橋渡し。旧stable+decayへcheckpoint kind/lineageを偽装して渡さない。[読取り修理147](147_evaluation_boundary_repair.md)は当時の修理記録。

## 次仮説の選定で避ける混同

RDropは旧予算で未評価だった状態から、累積上限解除後に初めて科学25Mを実施し不採用になった。今は一律に「品質未評価」と呼ばない。ScaleGradの反復減少も内容一貫性を達成していない。NEFTuneは適合根拠不足で未選定であり、品質失敗の実測ではない。9層256/FFN1040と6層384/FFN832の300M構成比較は既に存在する。

単独原因・全未知手法の不可能・10M限界は確定していない。候補名、CPU fixture数、記録追加、GPU時間の消費自体をBase品質の進捗としない。根拠がない場合は未選定と明記する。

## 品質と資源の契約

''' + quality() + '\n\n' + EXPOSURE + '''

ローカルGPUの累積上限は解除済み。旧technical180/total4800秒は過去の契約で、現在の残り利用可能量ではない。実験ごとの停止条件を後から延長せず、追加予算の根拠は新比較と独立全pipeline/最終評価それぞれに分けて事前に示す。研究を再開した範囲のroutine実装・保存再開を逐一再確認しない。有料cloud・大型化・公開・外部送信は別の指示が必要。

過去の元4.75B→10B枝の7657.678462524 GPU秒は、その当時のFlash/compile実測であり、親作成全体や将来独立native全pipelineの所要時間ではない。速度・教師量・入力量・評価保存を分けて見積もる。
''')
    name = 'docs/10_next_steps.md'
    write(name, header(name) + STATE + '\n\n' + RESOURCE + '''

## 実績

- [x] DEV専用読取り/生成reviewの分離修理とCPU/既知DEV証拠。
- [x] 全文DEV/440接続部品と36 CPU checks。実品質は別。
- [x] ScaleGrad25Mを全80/全state/全guardで不採用に閉鎖。
- [x] 上限解除を新資源契約へ記録し、第一回RDrop25M科学比較を実行。
- [x] RDrop全80理由付き内容/全4,420履歴/状態/stream監査。不採用で閉鎖。

## 残る成果物

- [ ] 根拠ある未回答仮説1件の選定と、新比較/独立学習/最終評価の段階別契約。
- [ ] 元の全品質条件を満たす主recipe。
- [ ] 資格・全pipeline証拠を接続する永続native runner/reviewer。
- [ ] 親の事前学習から独立fresh seed43を実行し全state/再現性を検証。
- [ ] 実全文DEV、400生成＋長文40の全内容、必要な独立人間blind/corpus監査。
- [ ] recipe封印後の新TEST、原採否、復旧、Base採用。
- [ ] 別再開範囲のChat/SFT・量子化/配布。

''' + quality() + '\n\n' + EXPOSURE + '\n\n' + evidence(name))
    name = 'docs/124_base_recovery_plan.md'
    write(name, header(name) + STATE + '\n\n' + BOUNDARY + '\n\n' + RESOURCE + '''

## 復旧の進め方

次の詳細な進行契約は[計画145](145_post_rejection_next_plan.md)。既存結果から根拠ある仮説を1件選び、対照/教師/親/seed/decoder/全品質/有限な停止条件を固定し、必要な技術gateを経て科学比較する。有資格候補なしで独立学習やTESTへ先行しない。

文書長重み100M、進行長補助25M、ScaleGrad25M、RDrop25M等の不採用を取り消さず、同条件の係数/教師/seed/親/精度/decoder/予算を救済しない。次の手法は未選定。根拠不足を無根拠な連続試行で埋めない。

## 完成までの不足

''' + PENDING + '\n\n' + quality() + '\n\n' + EXPOSURE + '\n\n' + evidence(name))
    name = 'docs/15_project_roadmap.md'
    write(name, header(name) + STATE + '\n\n' + RESOURCE + '''

## フェーズの状態

| Phase | 状態 | 残る成果物 |
|---|---|---|
| 0〜3 | 成功条件/データpilot/Tokenizer/model-cache-export基盤は完了 | 当時の16〜19の証拠を保全 |
| 4〜5 | WSL/4090学習・全state再開・小予算比較基盤は完了 | 技術成立と品質完成は区別 |
| 6 Base | 元10Bと多数の比較を実行、品質未達 | 有資格recipe→独立fresh全pipeline→fullDEV/全440→新TEST/採用 |
| 7 Chat | 限定SFT128〜141は実施・不採用 | 正式Chat、独立確認、人間blind、最終採用は未達 |
| 8 ローカル利用 | UI/変換基盤あり、正式量子化成果物は未完成 | 採用floatとの品質/容量/速度/独立環境の確認 |
| 9〜10 追加研究 | 条件付き後半構想 | 20B/50B・追加研究等を自動開始しない |

## 現在と今後の順序

現在は文書更新のみ。元「4まで」は未達で解除済み。将来の研究は[計画145](145_post_rejection_next_plan.md)の前向き契約で、次比較の選定・必要技術gate・科学比較・主資格・独立全pipeline・最終評価の順。累積時間が無制限でも、比較ごとの終了条件を保持する。

''' + BOUNDARY + '\n\n' + PENDING + '\n\n' + quality() + '\n\n' + EXPOSURE + '\n\n' + evidence(name) + '''

## 原定義と履歴

Phase0〜3の完了は[16](16_phase0_completion.md)・[17](17_phase1_completion.md)・[18](18_phase2_completion.md)・[19](19_phase3_completion.md)、学習基盤は[21](21_phase4_completion.md)・[23](23_phase5_completion.md)。過去の全ロードマップは今回baseline snapshotと[旧履歴](project_roadmap_history_20261008.md)に保全。基盤の完了をBase/Chat採用へ読み替えない。
''')
    name = 'docs/windows_handoff.md'
    write(name, header(name) + STATE + '\n\n' + RESOURCE + '''

## 最新の保存と最後の実行観測

''' + ui() + '''

最新RDrop checkpointはWSL reports/phase6/rdrop-science-20261016/checkpoint-00004420.pt、SHA256 e9154a2d5b8e385c978e597c8b65d3c73dc882680bbf143422d9acb363aa0c73。全model/Adam/RNG/sampler/counters/metricsを保全。元UIはこの候補でなく元10B親を使用する。

## 正本と保存場所

| 対象 | 場所・固定情報 |
|---|---|
| Git正本 | C:\\Users\\AiHUB\\Desktop\\japanese-tiny-llm-10m。最新HEADはgit logで確認 |
| 実行コピー | /home/aihub_ubuntu/src/japanese-tiny-llm-10m |
| データ | /home/aihub_ubuntu/jmicro-data。重み・data・samplerはGit外 |
| Python | uv固定3.12.7、既存WSL2/Linux disk/RTX4090。package/driver情報は観測値 |
| Tokenizer | artifacts/phase2/4096/tokenizer.model、SHA a7aabac51efa0712aef6f2e5956ac7d0e7fa92de869d730af2492f79c5cfa318 |
| 元UI親 | reports/phase6/base-10b-20261004/decay/checkpoint-00305176.pt、SHA 410f975d848938627aafb4fa1d5483bf45fadbb7f9c05ed7d1c8f9d45c368290 |
| native model | 10,001,152 parameters、src/jmicro/model.py SHA298bbac76c5b99c9831039116b704b0371612f9a28f68b81afc824a1d9bbde83 |
| 最新portable証拠 | reports/phase6/rdrop-science-20261016/portable_artifacts.json。全stateの代用ではない |

## 復元と操作

既存環境では[WebUI操作43](43_local_webui.md)。操作時にserver記録と実PID/boot/start/HTTP/kernel lockを照合し、重複起動しない。元UIが停止している場合だけscripts/start_webui.ps1を使う。今回の文書作業では再起動しない。

欠損時だけ[Hub引継ぎ](huggingface_handoff.md)・[保存126](126_model_archive.md)のpinned取得/uv frozen復元を行う。公開保存にsampler/dataがないことを確認し、元checkpointの厳密再開を装わない。過去のChatとBase各系列も原pathのまま保全する。

''' + PENDING + '\n\n' + EXPOSURE + '\n\n' + evidence(name))
    name = 'docs/43_local_webui.md'
    write(name, header(name) + '''元の10B Baseで文章の続きを試すUI。正式採用Base/Chatではなく、不採用の最新RDrop候補へ置き換えていない。URLは[http://127.0.0.1:7860](http://127.0.0.1:7860)。

''' + ui() + '''

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

''' + STATE + '\n\n' + PENDING + '\n\n' + evidence(name))
    name = 'docs/evaluation_protocol.md'
    old = original(name)
    tail = old[old.index('## v1契約と後続実験を区別する'):]
    tail = re.split(r'\n<!-- Original heading aliases', tail)[0]
    write(name, header(name) + STATE + '\n\n' + quality() + '\n\n' + BOUNDARY + '\n\n' + EXPOSURE + '''

## 最新評価の範囲と制約

同25M nativeCE対照とRDrop候補の元主教師streamを照合済み。二回forwardのphysical streamは倍になり、学習torch RNGはdropoutのため対照と意図的に異なる。腕内の保存再開ではRNGを含む全state一致が必要。全80個別理由はCodex非blindであり、人間blindではない。

全文DEVは89416文書/42003934本文token/164344743bytes、context1024/stride512/batch16/limitNoneを固定し本文一度/EOS別集計。36 CPU checksは合成fixtureで、実全文評価は未実行。標準440 suiteは特殊ID0,1,2,4,5,6を抑制、pilot80は7も抑制。設定差を消して同条件と主張しない。Python open監査をnative OS sandboxと記載しない。

''' + evidence(name) + '\n\n' + tail)
    name = 'docs/codex_automation.md'
    write(name, header(name) + RESOURCE + '\n\n' + PENDING + '''

## 目標状態と実行範囲

元「4まで」はBase未達のままユーザーが解除。現在の文書目標を旧研究の達成・再開にしない。履歴のrunning/PID/next_actionは日時付き証拠であり起動指示ではない。文書更新で研究・データ/TEST準備・推論・GPU・環境変更・公開を開始しない。

continueは許可範囲の有用な作業が残る状態、needs_userは外部判断が必要な状態、completeは依頼範囲が証拠で完了した状態。技術gate/比較の完了と正式Base採用を分ける。同じ外部障害の3連続goal turn確認はその目標/再開ごとに数える。旧上限でのblocked判定を、新しい累積上限解除後の現在障害へ流用しない。

## 将来の学習運用

新しい比較の前に根拠・全品質・対照・有限の教師/時間/評価保存枠・停止条件を固定。実CUDA最大shape/finite・全state再開・cache・全timingを確認する。長期runはPID/boot/start・logs/checkpoint/heartbeat・GPU/kernel lockを記録し、重複起動を防ぐ。真の中断だけを同一契約/残りrun予算で復旧する。

有効なprocessを観測したwaitは進捗確認。観測timeoutだけでrestartしない。完了・失敗した固定条件を係数/精度/shape/教師/decoder/予算変更で救済しない。元UIの停止はowned学習中のみ、終端で元親へ復帰し実identity/HTTP/lockを確認する。共有log handleをworker生存と混同しない。

## 保存と納品

WindowsがGit正本。全Pythonはuv run --frozenで3.12.7を使う。全重み/Adam/scheduler/RNG/sampler/countersをcompleted updateで保存し、大容量実体はWSL。小raw/個別notes/receiptはhashでWindows/WSL/Gitを照合しローカルcommit。push/公開・他者送信・paid cloudは別の明示指示が必要。

''' + STATE + '\n\n' + evidence(name))
    name = 'docs/base_experiment_lookup.md'
    write(name, header(name) + STATE + '''

## 最新までの入口

| 比較・部品 | 原記録 | 判断 |
|---|---|---|
| 第一回RDrop25M | [completion](../reports/phase6/rdrop-science-20261016/completion.json)・[review](../reports/phase6/rdrop-science-20261016/review.json) | 全80/全4,420履歴、不採用 |
| ScaleGrad25M | [completion](../reports/phase6/scalegrad-science-20261015/completion.json) | 文法/反復は改善、一貫性/適切完結/BPB等未達 |
| 進行長補助25M | [completion](../reports/phase6/document-progress-science-20261015/completion.json) | paired対照/候補、内容改善なし |
| 全文DEV部品 | [CPU completion](../reports/phase6/isolated-full-dev-preparation-20261015/completion.json) | 合成36 checks、実全文/440内容は未実行 |
| 上限解除前の選定監査 | [decision](../reports/phase6/post-scalegrad-selection-20261015/decision.json)・[primary fit](../reports/phase6/post-scalegrad-selection-20261015/primary_fit_review.json) | 当時の資源/根拠判断。NEFTuneは未選定 |
| 文書長重み100M | [144](144_base_document_balance_results.md) | 不採用 |
| 限定SFT低LR | [141](141_chat_lr_comparison_results.md) | 不採用 |

9層256/FFN1040、6層384/FFN832の構成配分はconfigs/phase6/architecture_comparison.jsonとreports/phase6/architecture_comparison_review.jsonに300M比較が存在する。以下の固定索引の検索語がないことは、未検証の証明ではない。proposal/trainer/結果を対応付ける。

''' + RESOURCE + '\n\n' + PENDING + '\n\n' + technical_tail(name))
    name = 'docs/125_project_retrospective.md'
    write(name, header(name) + STATE + '\n\n' + RESOURCE + '''

## 固定台帳後の追加判断

文書長重み100Mと限定Chat低LR141は不採用。10月15日にDEV読取り隔離を実装し、複数の独立仮説を比較したが資格あるBaseは得られていない。進行長補助は一貫性1→1/80、ScaleGradは1→7/80で原27以上に届かずBPBも悪化。反復flag/EOSの改善を意味の一貫性や適切な完結に置き換えない。

RDropは最大shapeのOOM後、数学的に一致する別loss runtimeとtarget転送を検証した。当時の累積時間上限では科学を費用閉鎖した。ユーザーの累積上限解除後、別の前向き科学契約で初めて同25M比較を実施し、今回品質不採用に閉じた。技術合格、旧費用閉鎖、今回品質失敗はそれぞれ別の証拠。

NEFTuneは一次資料の生成制約と対象規模/領域を照合し適合根拠不足で未選定。未知の全手法の否定・10M限界・単独原因の確定ではない。既存の構成配分300M比較を未検証案として繰り返さない。

''' + BOUNDARY + '\n\n' + PENDING + '\n\n' + EXPOSURE + '\n\n' + evidence(name) + '\n\n' + technical_tail(name))
    name = 'docs/README.md'
    numbered = sorted((r for r in read_baseline()['documents']
                       if re.fullmatch(r'docs/\d+_[^/]+\.md', r['path'])),
                      key=lambda r: int(r['path'].split('/')[1].split('_')[0]))
    rows = ['## 番号付きの計画・結果', '', '| 文書 | 主題 |', '|---|---|']
    for r in numbered:
        rows.append(f"| [{Path(r['path']).name}]({href(name, r['path'])}) | {r['title'].replace('|', '/')} |")
    rows.append('| [148_latest_base_and_documentation.md](148_latest_base_and_documentation.md) | 最新RDrop25Mの採否と全文書更新 |')
    table = '\n'.join(rows)
    write(name, header(name) + STATE + '\n\n' + RESOURCE + '''

## 読む順序

1. [状態](autonomous_status.md)・[最新結果と文書更新148](148_latest_base_and_documentation.md)。
2. [計画145](145_post_rejection_next_plan.md)・[ロードマップ](15_project_roadmap.md)・[チェックリスト](10_next_steps.md)。
3. [評価契約](evaluation_protocol.md)・[読取り分離の当時の修理147](147_evaluation_boundary_repair.md)。
4. [引継ぎ](windows_handoff.md)・[UI43](43_local_webui.md)・[保存126](126_model_archive.md)。
5. [実験検索](base_experiment_lookup.md)・[総覧125](125_project_retrospective.md)・[固定台帳](retrospective/README.md)。
6. [全件カタログ](document_catalog.md)。現行・日付付き/固定履歴・原文copyを区別する。

旧142/146はそれぞれの日付の文書納品記録。143/144は文書長重みの凍結計画/結果、147は修理当時の実行記録として保全する。固定履歴の「次は/稼働中」は現在の実行許可や状態ではない。

''' + table + '\n')
    latest()
    catalog()
    mirror(HELPER)
    mirror('.gitattributes')
    print(json.dumps(dict(updated_existing_living=len(LIVING), added_current=len(NEW))))


def latest():
    name = 'docs/148_latest_base_and_documentation.md'
    write(name, header(name, '# 最新Base結果と全文書更新（2026-10-17）') + STATE + '\n\n' + evidence(name) + '''

## 第一回RDrop科学比較の結果

元10B親/fresh AdamW、同native10,001,152、同TRAIN/25M主教師/batch48/seed42、平均二view CE＋.5×対称KL。dropout.1はembedding/attention-output/MLP-outputの学習時のみ。4,420更新、hardgold CE評価50M、consistency pairs25M。追加unique教材50Mではない。推論モデル/decoderは元native。

| 指標（80件） | nativeCE25M対照 | RDrop25M | 元絶対条件 |
|---|---:|---:|---:|
| 文法2 | 44 | 47 | ≥56 |
| 一貫性2 | 1 | 3 | ≥27 |
| 適切な完結 | 3 | 6 | ≥27 |
| EOS | 11 | 19 | ≥37 |
| 規定反復 | 53 | 49 | ≤18 |

BPB0.9927168290617072→1.0279654060355414、3.5507181848775993%悪化。対応一貫性差+2/80・CI95[0,.0625]は+8/下限>0未達。全5絶対品質/停止/反復gateと元保持guardに不合格。empty/role/Unicode等0だけでは合格しない。

全80のraw/個別理由、全4,420履歴/型付き全stateを確認。元主streamは対照一致。二viewのphysical streamは倍で、dropoutのため学習torch RNGは対照と意図的に異なる。腕内保存再開のRNGを含む全state一致を維持した。Codex非blindであり独立人間blindではない。KL単独の因果効果や全RDrop/10Mの不可能を示す結果ではない。

固定条件は不採用で閉鎖。係数/dropout/教師/親/seed/decoder/品質閾値を後から変更して救済しない。意味の循環、因果/数量誤りが残る。

## 資源と保存

''' + RESOURCE + '''

今回の科学GPU777.297899876954秒。継承台帳は技術169.2456279549515＋科学4241.304908989929＝総4410.55053694488秒。これは対象継承台帳の範囲で、全プロジェクトの歴史GPU総計ではない。今回runは実行前にcap1757秒を固定し、その範囲内で終了した。

科学commit cf113068。全weights/Adam/RNG/sampler/metricsはWSL、checkpoint-00004420.pt SHA e9154a2d5b8e385c978e597c8b65d3c73dc882680bbf143422d9acb363aa0c73。18小portable記録の同hash保全は原portable_artifactsを参照する。

''' + ui() + '''

## Base完成までの不足

''' + BOUNDARY + '\n\n' + PENDING + '\n\n' + EXPOSURE + '''

## 今回の全文書更新

更新前976パスの全Git管理Markdown/RSTを棚卸しし、現行34文書を最新化、148を追加した。日付付き/固定履歴284・以前の原文copy658（計942パス）は当時のbytesを保持する。旧本文の内容hash別copyは既存を再利用し、不足36件のみ追加した。今回以前の全文はbaselineのsnapshot列からたどれる。長い追記型の進捗は現行入口から整理し、旧文書中の全見出しanchorも保持する。

[全件カタログ](document_catalog.md) / [更新前baseline](../reports/investigation/documentation-refresh-20261017/baseline.json) / [保存・リンク・同期の検証](../reports/investigation/documentation-refresh-20261017/verification.json) / [Git納品確認](../reports/investigation/documentation-refresh-20261017/commit_verification.json)。検証recordは実チェック後に保存する。

今回の文書更新は学習・推論・GPU・data/TEST・外部公開を実行しない。旧「4まで」の目標は未達のまま解除済み。文書納品をBase/Chat完成にしない。今後の詳細は[計画145](145_post_rejection_next_plan.md)。
''')


def catalog():
    b = read_baseline()
    names = sorted({r['path'] for r in b['documents']} | NEW | set(b['new_original_copies']))
    name = 'docs/document_catalog.md'
    lines = [header(name, '# 全ドキュメント・保存原文の一覧').rstrip(), '',
             f"更新前の全Git管理Markdown/RSTは{b['all_document_paths']}パス。分類は{b['category_counts']}。今回追加currentは{len(NEW)}パス、内容hash別新原文copyは{len(b['new_original_copies'])}パス。既存の同hash原文copyは再利用し、copyを再帰的に増やさない。", '',
             '[baseline](../reports/investigation/documentation-refresh-20261017/baseline.json)のpath/hash/category/snapshot列で全元パスを追跡する。dated/frozen/provenanceは今回の現在説明へ書き換えない。原文copy内のrelative linkは元パスの文脈で読む。', '',
             '過去142/146の件数・納品hashは当時の証拠。今回の棚卸し件数へ書き換えない。', '']
    for kind, title in [('living', '現行説明・計画'), ('dated_or_frozen_history', '日付付き結果・固定履歴'), ('provenance_copy', '原文copy')]:
        lines += ['## ' + title, '', '| 文書 | 扱い |', '|---|---|']
        for path in names:
            if category(path) == kind:
                lines.append(f'| [{path}]({href(name, path)}) | ' + ('最新化' if kind == 'living' else '原文保全') + ' |')
        lines.append('')
    write(name, '\n'.join(lines))


def local_links(body):
    # Markdown inline links outside fenced code. Historical source copies are
    # separately classified, not evaluated in their relocated path context.
    body = re.sub(r'^```[^\n]*\n.*?^```[^\n]*$', '', body, flags=re.M | re.S)
    for match in re.finditer(r'\[[^\]\n]*\]\(([^)\n]+)\)', body):
        value = match.group(1).strip()
        if value.startswith('<'):
            value = value[1:value.index('>')]
        else:
            value = re.split(r'\s+[\"\']', value)[0]
        if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', value) or value.startswith('//'):
            continue
        yield value


@cache
def resolved_target(absolute):
    return Path(absolute).resolve()


def link_target(name, target):
    absolute = os.path.normpath(str((ROOT / name).parent / unquote(target))) if target else str(ROOT / name)
    return resolved_target(absolute)


@cache
def target_issue(path, fragment):
    if not path.is_relative_to(ROOT):
        return 'outside_workspace'
    if not path.exists():
        return 'missing_path'
    if fragment and path.suffix.lower() not in ('.md', '.rst'):
        return 'fragment_target_not_document'
    if fragment and unquote(fragment) not in anchors(path):
        return 'missing_anchor'
    return None


def check_link(name, link):
    target, _, fragment = link.partition('#')
    return target_issue(link_target(name, target), fragment)


def verify(commit=None):
    b = read_baseline()
    for filename in ('verification.json', 'commit_verification.json'):
        pending = RUN / filename
        if not pending.exists():
            save(pending, dict(status='pending_actual_verification', passed=False))
            mirror(pending.relative_to(ROOT).as_posix())
    changed = []
    for r in b['documents']:
        assert sha(ROOT / r['snapshot']) == r['sha256'], ('snapshot', r['path'])
        if r['path'] in LIVING:
            assert sha(ROOT / r['path']) != r['sha256'], ('not_updated', r['path'])
            assert anchors(ROOT / r['snapshot']) <= anchors(ROOT / r['path']), ('lost_anchor', r['path'])
            changed.append(r['path'])
        else:
            assert sha(ROOT / r['path']) == r['sha256'], ('changed_history', r['path'])
    for name, digest in b['frozen_references'].items():
        assert sha(ROOT / name) == sha(WSL / name) == digest, ('frozen_reference', name)
    print('Original documentation bytes, heading aliases and frozen references verified.', flush=True)
    errors, checked = [], 0
    for name in sorted(LIVING | NEW):
        assert sha(ROOT / name) == sha(WSL / name), ('mirror', name)
        body = (ROOT / name).read_text(encoding='utf-8-sig')
        assert '\ufffd' not in body and '\x00' not in body, name
        assert '2026-10-17' in body and '148' in body, ('stale_header', name)
        for link in local_links(body):
            error = check_link(name, link)
            checked += 1
            if error:
                errors.append(dict(source=name, link=link, error=error))
    # Audit all historical links too, while preserving old evidence. Original
    # copies are checked relative to their original source via baseline mapping.
    historic_issues, historic_checked, inbound = [], 0, 0
    for r in b['documents']:
        if r['path'] in LIVING or r['category'] == 'provenance_copy':
            continue
        for link in local_links((ROOT / r['path']).read_text(encoding='utf-8-sig')):
            historic_checked += 1
            error = check_link(r['path'], link)
            if error:
                historic_issues.append(dict(source=r['path'], link=link, error=error))
            target, _, fragment = link.partition('#')
            dest = link_target(r['path'], target)
            if dest.is_relative_to(ROOT) and dest.relative_to(ROOT).as_posix() in LIVING | NEW:
                inbound += 1
                assert not error, ('historical_incoming', r['path'], link)
    save(RUN / 'historical_link_audit.json', dict(observed_at=now(), checked=historic_checked,
         issues=historic_issues, note='Frozen historical evidence was not rewritten; links into current documents must remain valid. Relocated provenance copies are byte-verified, not treated as current standalone pages.'))
    mirror(f'{PREFIX}/historical_link_audit.json')
    if errors:
        print(json.dumps(dict(current_link_errors=errors), ensure_ascii=False))
        raise AssertionError(f'{len(errors)} current link errors')
    expected = {r['path'] for r in b['documents']} | NEW | set(b['new_original_copies'])
    paths = set()
    for link in local_links((ROOT / 'docs/document_catalog.md').read_text()):
        target = link.split('#', 1)[0]
        dest = link_target('docs/document_catalog.md', target)
        if dest.is_relative_to(ROOT):
            paths.add(dest.relative_to(ROOT).as_posix())
    assert expected <= paths, ('catalog_missing', sorted(expected - paths))
    allowed = LIVING | NEW | {HELPER, '.gitattributes'}
    for name in git('diff', '--name-only', b['initial_commit']).splitlines():
        assert name in allowed or name.startswith(PREFIX + '/'), ('scope', name)
    for name in git('ls-files', '--others', '--exclude-standard').splitlines():
        assert name in allowed or name.startswith(PREFIX + '/'), ('untracked_scope', name)
    mirror(HELPER)
    mirror('.gitattributes')
    for name in b['new_original_copies']:
        assert sha(ROOT / name) == sha(WSL / name), name
    c = json.loads((ROOT / RESULT).read_text())
    assert c['fixed_condition_closed'] and not c['Base_qualified'] and not c['Base_adopted']
    assert c['global_cumulative_GPU_cap'] is None and c['all80_individually_read']
    proof = dict(passed=True, verified_at=now(), baseline_commit=b['initial_commit'],
                 all_initial_documents=b['all_document_paths'], category_counts=b['category_counts'],
                 existing_living_documents_updated=len(changed), additional_living_documents=len(NEW),
                 dated_and_provenance_documents_unchanged=b['all_document_paths'] - len(changed),
                 new_original_copies_verified=len(b['new_original_copies']), catalog_targets=len(expected),
                 all_original_heading_aliases_preserved=True, current_local_links_checked=checked,
                 current_link_issues=0, historical_links_checked=historic_checked,
                 historical_link_issues_preserved=len(historic_issues), historical_incoming_links_checked=inbound,
                 Windows_WSL_changed_documents_and_new_copies_match=True,
                 frozen_scientific_references_unchanged=True, only_documentation_changes=True,
                 GPU_work=False, research_resumed=False, model_or_dataset_or_TEST_read=False,
                 Base_complete=False, Chat_complete=False, push_executed=False,
                 helper_sha256=sha(ROOT / HELPER))
    destination = RUN / 'verification.json'
    if commit:
        rev = git('rev-parse', commit + '^{commit}')
        files = git('diff', '--name-only', b['initial_commit'], rev).splitlines()
        for name in files:
            assert git('rev-parse', rev + ':' + name) == git('hash-object', '--path=' + name, WIN + '\\' + name.replace('/', '\\')), ('commit_blob', name)
        proof.update(result_commit=rev, committed_files_verified=len(files))
        destination = RUN / 'commit_verification.json'
    save(destination, proof)
    mirror(destination.relative_to(ROOT).as_posix())
    print(json.dumps(proof, ensure_ascii=False))


if __name__ == '__main__':
    assert sys.version_info[:3] == (3, 12, 7), 'Pinned uv Python required'
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('baseline', 'apply', 'verify'))
    parser.add_argument('--commit')
    args = parser.parse_args()
    if args.mode == 'baseline':
        baseline()
    elif args.mode == 'apply':
        apply()
    else:
        verify(args.commit)
