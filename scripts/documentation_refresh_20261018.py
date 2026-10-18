"""Inventory and verify every tracked document without changing scientific records.

Windows is authoritative. Run through uv in WSL. No corpus, TEST, weights,
training, generation, server restarts, or remote writes are performed here.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import posixpath
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m')
WSL = Path('/home/aihub_ubuntu/src/japanese-tiny-llm-10m')
GIT = '/mnt/c/Program Files/Git/cmd/git.exe'
WIN = r'C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m'
PREFIX = 'reports/investigation/documentation-refresh-20261018'
RUN = ROOT / PREFIX
sys.path.insert(0, str(Path(__file__).resolve().parent))
from refresh_project_documents import OPERATIVE, anchors
LIVING = set(OPERATIVE) | {'docs/document_catalog.md', 'docs/145_post_rejection_next_plan.md'}
NEW = 'docs/167_current_state_and_documentation.md'
HELPER = 'scripts/documentation_refresh_20261018.py'
WRITER = 'scripts/write_documents_20261018.py'
REMOVED = {'docs/142_documentation_refresh.md', 'docs/146_documentation_followup.md',
           'docs/148_latest_base_and_documentation.md'}


def now():
    return datetime.now(timezone.utc).isoformat()


def git(*args):
    return subprocess.run([GIT, '-C', WIN, '-c', 'core.quotepath=false', *args],
                          capture_output=True, check=True).stdout.decode('utf-8').rstrip('\r\n')


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False)+'\n', encoding='utf-8', newline='\n')


def is_document(name):
    return Path(name).suffix.lower() in ('.md','.markdown','.rst','.txt','.adoc') or Path(name).name in ('LICENSE','NOTICE','README')


def kind(name):
    if name in LIVING or name == NEW:
        return 'current'
    if name in ('LICENSE','NOTICE') or '/_vendor/' in name:
        return 'license_or_third_party_notice'
    if '/originals/' in name or '/previous_docs/' in name:
        return 'preserved_original'
    return 'dated_or_frozen_record'


def baseline():
    assert not (RUN/'baseline.json').exists()
    assert not git('status','--porcelain','--untracked-files=no')
    names = sorted(n for n in git('ls-files','-z').split('\0') if n)
    entries = []
    index = {}
    for line in git('ls-files','--stage','-z').split('\0'):
        if line:
            metadata, name = line.split('\t',1)
            index[name] = metadata.split()[1]
    for name in names:
        if not is_document(name):
            continue
        path=ROOT/name
        body=path.read_text(encoding='utf-8-sig')
        entries.append(dict(path=name, category=kind(name), sha256=sha(path),
            bytes=path.stat().st_size, git_blob=index[name],
            title=next((s.lstrip('# ').strip() for s in body.splitlines() if s.startswith('#')),Path(name).stem)))
    references = ['reports/phase7/chat-two-attribute-20261018/completion.json',
        'reports/phase7/chat-two-attribute-20261018/final_analysis.json',
        'reports/phase7/chat-two-attribute-20261018/learning_complete.json',
        'reports/phase7/chat-two-attribute-20261018/GPU_ledger.json',
        'reports/phase7/chat-recovery-20261018/input-structure-main/completion.json',
        'reports/publication/chat-sft-public-20261018-v2/SFT_public.json',
        'reports/publication/chat-sft-public-20261018-v2/Base_public.json',
        'reports/publication/chat-sft-public-20261018-v2/Base_README_manifest_clarification.json',
        'reports/publication/chat-sft-public-20261018-v2/namespace_public.json',
        'reports/publication/repository-public-20261018.json',
        'configs/phase7/chat-two-attribute-20261018.json',
        'src/jmicro/model.py','src/jmicro/tokenizer.py','src/jmicro/training.py','uv.lock']
    data=dict(captured_at=now(),initial_commit=git('rev-parse','HEAD'),documents=entries,
        count=len(entries),categories=dict(Counter(r['category'] for r in entries)),
        tracked_file_blobs=index,references={n:sha(ROOT/n) for n in references},
        scope='All Git-tracked Markdown/Markdown/RST/TXT/AsciiDoc and LICENSE/NOTICE/README; ignored data and model payloads excluded.')
    save(RUN/'baseline.json',data)
    print(json.dumps({k:data[k] for k in ('initial_commit','count','categories')},ensure_ascii=False))


def read_baseline():
    return json.loads((RUN/'baseline.json').read_text())


def href(name,target):
    return posixpath.relpath(target,posixpath.dirname(name) or '.')


def link(name,label,target):
    return f'[{label}]({href(name,target)})'


def navigation(name):
    return ' / '.join(link(name,label,target) for label,target in (
        ('現在の状態','docs/autonomous_status.md'),('最新SFT結果','docs/165_chat_two_attribute_diagnosis_results.md'),
        ('公開モデル','docs/166_public_models_and_oss.md'),('文書一覧','docs/README.md')))


def write(name,body):
    path=ROOT/name
    path.parent.mkdir(parents=True,exist_ok=True)
    old=anchors(path) if path.exists() and path.suffix=='.md' else set()
    path.write_text(body.rstrip()+'\n',encoding='utf-8',newline='\n')
    missing=old-anchors(path)
    if missing:
        with path.open('a',encoding='utf-8',newline='\n') as stream:
            stream.write('\n<!-- Preserve incoming links to earlier headings; previous text is in Git history. -->\n')
            stream.write('\n'.join(f'<a id="{s}"></a>' for s in sorted(missing))+'\n')


def page(name,title,body,previous=True):
    text=f'# {title}\n\n更新: 2026-10-18 JST。\n\n{body.strip()}\n\n{navigation(name)}\n'
    if previous:
        revision=read_baseline()['initial_commit']
        text+=f'\n前版の設計・調査・運用記録は[更新前の本文](https://github.com/ayutaz/japanese-tiny-llm-10m/blob/{revision}/{name})に保存しています。過去の「最新」「実行中」はその記載時点の状態です。\n'
    write(name,text)


def context(name):
    if kind(name)=='current':
        return '現在の説明・操作・入口'
    if kind(name)=='license_or_third_party_notice':
        return '許諾・帰属の原文を保持'
    if kind(name)=='preserved_original':
        return '保存原文。リンクは元文書の配置で解釈'
    match=re.fullmatch(r'docs/(\d+)_.*\.md',name)
    if match:
        number=int(match[1])
        if 149<=number<=150:return '実行済み・不採用。結果150、後続165'
        if 151<=number<=157:return '実行・判定済み。結果156/157、後続165'
        if 158<=number<=163:return '調査・対照SFT完了。結果162、後続165'
        if 164<=number<=165:return '最新SFTの固定契約・完了結果。不採用'
        if number==166:return '公開・Apache-2.0・匿名取得の完了記録'
        if number==148:return '2026-10-17時点の更新記録。現在は167'
    return '日付付きの計画・結果・source snapshot。現在の指示ではない'


def catalog():
    b=read_baseline()
    name='docs/document_catalog.md'
    rows=b['documents']+[dict(path=NEW,title='最新の研究状態と全文書更新',category='current')]
    pieces=['# 全ドキュメントと保存原文の一覧','',
        '更新: 2026-10-18 JST。全Git管理文書を棚卸しし、現行説明と固定した過去記録を区別しています。',
        '',navigation(name),'',
        f"更新前は{b['count']}パス。初期revisionは`{b['initial_commit']}`です。各文書のSHA256・Git blob・分類を[全件baseline](../{PREFIX}/baseline.json)へ保存しています。今回追加の現行説明は[167](167_current_state_and_documentation.md)です。",
        '', '現在のSFT試行は完了・不採用、Base 3系列と最新SFTは申請不要で公開済み、コードはApache-2.0です。過去記録の未完了・manual gate・非公開は当時の状態として読みます。',
        '', '現行文書は本文を更新し、日付付き科学記録・source snapshot・原文copy・ライセンス原文は保持しています。重複する文書更新報告142/146/148は167へ統合して現行treeから削除しました。削除前の本文は下表の固定Git revisionリンクで読めます。過去の文書更新件数やhashも、それぞれのrevisionの証拠です。']
    for category,title in [('current','現行説明と操作'),('dated_or_frozen_record','日付付き計画と固定記録'),('preserved_original','保存した原文'),('license_or_third_party_notice','ライセンスと帰属')]:
        pieces+=['',f'## {title}','','| 文書 | 内容と現在の扱い |','|---|---|']
        for row in sorted(rows,key=lambda r:r['path']):
            if row['category']==category:
                target = (f"https://github.com/ayutaz/japanese-tiny-llm-10m/blob/{b['initial_commit']}/{row['path']}"
                          if row['path'] in REMOVED else href(name,row['path']))
                handling = '更新記録167へ統合・現行treeから削除。リンク先は保存した原版' if row['path'] in REMOVED else context(row['path'])
                pieces.append(f"| [{row['path']}]({target}) | {row['title'].replace('|','/')} — {handling} |")
    write(name,'\n'.join(pieces))


def audit():
    b=read_baseline();rows=b['documents']; failures=[]
    # The audit report is itself linked from167. Materialize an honest running
    # state before checking links, rather than requiring a previous audit file.
    save(RUN/'coverage_audit.json',dict(status='running',started_at=now()))
    for r in rows:
        if r['path'] in REMOVED:
            if (ROOT/r['path']).exists():failures.append('Obsolete documentation not removed: '+r['path'])
            continue
        if r['category']!='current' and sha(ROOT/r['path'])!=r['sha256']:
            failures.append('Historical/third-party document changed: '+r['path'])
    for name,expected in b['references'].items():
        if sha(ROOT/name)!=expected:failures.append('Scientific/publication reference changed: '+name)
    batch_input=''.join(f"{b['initial_commit']}:{r['path']}\n" for r in rows)
    batch=subprocess.run([GIT,'-C',WIN,'cat-file','--batch-check'],input=batch_input.encode(),
                         capture_output=True,check=True).stdout.decode().splitlines()
    if len(batch)!=len(rows) or any(' missing' in line or ' blob ' not in line for line in batch):
        failures.append('Pre-edit documentation is not fully recoverable from baseline Git revision')
    for name in REMOVED:
        for config in (ROOT/'configs').rglob('*.json'):
            if name in config.read_text(encoding='utf-8-sig'):
                failures.append('Removed documentation is bound by a configuration: '+name)
    scientific=json.loads((ROOT/'reports/phase7/chat-two-attribute-20261018/final_analysis.json').read_text())
    learning=json.loads((ROOT/'reports/phase7/chat-two-attribute-20261018/learning_complete.json').read_text())
    factual_checks={
        '483_updates':learning['updates']==483,
        '250003_teachers':learning['teachers']==250003,
        'TRAIN64':scientific['diagnosis']['after_TRAIN']['content']==64,
        'values30of32':scientific['diagnosis']['after_unseen_values']['content']==30,
        'structure15of32':scientific['diagnosis']['after_unseen_structure']['content']==15,
        'own9of16':scientific['diagnosis']['own_final16']['content']==9,
        'public_task3of100':scientific['public100']['candidate']['final100']['task_pass']==3,
        'all1973_reviewed':scientific['judgments']==1973 and scientific['all1973_actual_histories_IDs_bytes_reviewed'],
        '1400_plus573':scientific['new_literal_reviews']==1400 and scientific['exact_raw_history_reused']==573,
        'no_adoption_or_new_TEST':not any(scientific[k] for k in ('Chat_adopted','Base_adopted','new_TEST'))}
    for name,value in factual_checks.items():
        if not value:failures.append('Current factual claim contradicts original result: '+name)
    current=sorted(LIVING|{NEW}); links_checked=0; bad_links=[]
    for name in current:
        path=ROOT/name
        if not path.exists(): failures.append('Missing current document: '+name);continue
        text=path.read_text(encoding='utf-8-sig')
        if text.count('```')%2:failures.append('Unpaired code fences: '+name)
        for value in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)',text):
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',value):continue
            relative,_,fragment=unquote(value).partition('#')
            target=(path.parent/relative).resolve() if relative else path
            links_checked+=1
            if not target.exists():bad_links.append(dict(source=name,target=value,reason='missing path'));continue
            if fragment and target.suffix=='.md' and fragment not in anchors(target):
                bad_links.append(dict(source=name,target=value,reason='missing anchor'))
    failures+=['Broken current link: '+json.dumps(r,ensure_ascii=False) for r in bad_links]
    catalog_text=(ROOT/'docs/document_catalog.md').read_text()
    for row in rows:
        if f"[{row['path']}]" not in catalog_text:failures.append('Uncatalogued: '+row['path'])
    changed=set(git('diff','--name-only',b['initial_commit']).splitlines())
    changed.update(n for n in git('ls-files','--others','--exclude-standard').splitlines() if n)
    allowed=LIVING|REMOVED|{NEW,HELPER,WRITER,'.gitattributes'}
    for name in changed:
        if name not in allowed and not name.startswith(PREFIX+'/'):
            failures.append('Out-of-scope tracked change: '+name)
    mirrored=[]
    for name in current+[HELPER,WRITER]:
        destination=WSL/name;destination.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/name,destination)
        if sha(ROOT/name)!=sha(destination):failures.append('Mirror mismatch: '+name)
        mirrored.append(dict(path=name,sha256=sha(ROOT/name)))
    for name in REMOVED:
        obsolete=WSL/name
        if obsolete.exists():
            expected=next(r['sha256'] for r in rows if r['path']==name)
            if sha(obsolete)!=expected:
                failures.append('Unrecognized WSL document at obsolete path: '+name)
            else:
                obsolete.unlink()
    result=dict(status='passed' if not failures else 'failed',audited_at=now(),
        original_document_count=b['count'],all_original_documents_accounted_for=True,
        current_documents=len(current),immutable_documents_checked=sum(r['category']!='current' and r['path'] not in REMOVED for r in rows),
        obsolete_maintenance_documents_removed=sorted(REMOVED),
        current_local_links_checked=links_checked,broken_current_links=bad_links,
        original_all_documents_recoverable_from_Git=True,original_result_fact_checks=factual_checks,
        frozen_references=len(b['references']),mirrored=mirrored,failures=failures,
        scope='All tracked documentation classified and catalogued; current text and links checked; dated/provenance/license text byte-preserved. No new model-quality, runtime-liveness or licensing-rights claim.')
    save(RUN/'coverage_audit.json',result)
    for name in ('baseline.json','coverage_audit.json'):
        destination=WSL/PREFIX/name;destination.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(RUN/name,destination)
    print(json.dumps({k:v for k,v in result.items() if k!='mirrored'},ensure_ascii=False))
    assert not failures


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=('baseline','catalog','audit'))
    args=parser.parse_args()
    globals()[args.action]()
