"""Documentation-only inventory/preservation/catalog/audit after rejected Base.

No model, dataset, TEST, runtime diagnosis, GPU work or network service access.
"""
import argparse
from collections import Counter
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote

WIN=Path('/mnt/c/Users/AiHUB/Desktop/japanese-tiny-llm-10m')
WSL=Path('/home/aihub_ubuntu/src/japanese-tiny-llm-10m')
RUN=WIN/'reports/investigation/documentation-followup-20261014'
GIT='/mnt/c/Program Files/Git/cmd/git.exe'
WIN_GIT=r'C:\Users\AiHUB\Desktop\japanese-tiny-llm-10m'
sys.path.insert(0,str(Path(__file__).resolve().parent))
from refresh_project_documents import OPERATIVE,anchors
LIVING=set(OPERATIVE)|{'docs/document_catalog.md'}
NEW={'docs/145_post_rejection_next_plan.md','docs/146_documentation_followup.md'}


def now(): return datetime.now(timezone.utc).isoformat()
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path): return json.loads(path.read_text())
def git(*args): return subprocess.run([GIT,'-C',WIN_GIT,'-c','core.quotepath=false',*args],check=True,capture_output=True).stdout.decode().strip()
def save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
def mirror(path):
    destination=WSL/path.relative_to(WIN)
    destination.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(path,destination)
    assert sha(path)==sha(destination)


def category(name):
    if name in LIVING or name=='docs/145_post_rejection_next_plan.md': return 'current'
    if '/originals/' in name or '/previous_docs/' in name: return 'provenance_copy'
    return 'dated_or_frozen_history'


def snapshot():
    assert not (RUN/'baseline.json').exists(),'Preserve prior baseline'
    assert not git('status','--porcelain','--untracked-files=no'),'Require unchanged tracked scope; the new document helper may be untracked'
    names=git('ls-files','-z','--','*.md','*.rst').split('\0')
    names=sorted(n for n in names if n)
    assert not git('ls-files','--others','--exclude-standard','--','*.md','*.rst')
    records=[]
    for name in names:
        source=WIN/name
        digest=sha(source)
        archive=RUN/'originals'/(digest+source.suffix)
        if not archive.exists():
            archive.parent.mkdir(parents=True,exist_ok=True)
            archive.write_bytes(source.read_bytes())
            mirror(archive)
        assert sha(archive)==digest
        body=source.read_text(encoding='utf-8-sig')
        records.append(dict(path=name,sha256=digest,bytes=source.stat().st_size,category=category(name),
            title=next((line.lstrip('# ').strip() for line in body.splitlines() if line.startswith('#')),source.stem),
            snapshot=archive.relative_to(WIN).as_posix()))
    refs={}
    for name in ('reports/phase6/base_document_balance_comparison_completion.json',
        'reports/phase6/base_document_balance_comparison_review.json',
        'reports/phase6/base-document-balance-comparison-20261014/final_delivery_checks.json',
        'reports/phase6/base-document-balance-comparison-20261014/original_TEST_prompt_exposure.json',
        'reports/phase6/base-document-balance-comparison-20261014/numeric_completion_audit.json',
        'reports/phase7/chat-lr-20261014/completion.json',
        'reports/phase7/chat-lr-20261014/selection.json',
        'configs/phase6/base_document_balance_comparison.json',
        'configs/phase6/base_document_balance_review.json',
        'configs/phase6/base_parallel_residual_review.json',
        'configs/evaluation/protocol.json',
        'src/jmicro/model.py','src/jmicro/training.py','src/jmicro/tokenizer.py','uv.lock'):
        refs[name]=sha(WIN/name)
    blocker=WIN/'reports/investigation/base-goal-20261014/blocker_audit.json'
    if blocker.exists():
        shutil.copyfile(blocker,RUN/'previous_goal_blocker.json')
        mirror(RUN/'previous_goal_blocker.json')
    value=dict(captured_at=now(),initial_commit=git('rev-parse','HEAD'),all_document_paths=len(records),
        category_counts=dict(Counter(r['category'] for r in records)),documents=records,
        unique_original_copies=len(list((RUN/'originals').glob('*'))),
        preserved_scientific_and_frozen_sources=refs,
        scope='Every tracked Markdown/RST including archived copies; no corpus/model/TEST reads')
    save(RUN/'baseline.json',value);mirror(RUN/'baseline.json')
    print(json.dumps({k:value[k] for k in ('all_document_paths','category_counts','unique_original_copies','initial_commit')}))


def catalog():
    b=read(RUN/'baseline.json')
    lines=['# 全ドキュメント・保存原文の一覧','',
        '更新: 2026-10-14 JST。今回の依頼は全現行文書の最新化と今後の計画の作成。研究・教材準備・診断・生成評価・GPU学習は再開しない。',
        '',f"更新前の全Git管理Markdown/RST **{b['all_document_paths']}パス**を棚卸し。現行{b['category_counts']['current']}、日付付き/固定履歴{b['category_counts']['dated_or_frozen_history']}、既存原文copy{b['category_counts']['provenance_copy']}。",'',
        f"元bytesを{b['unique_original_copies']}件の内容hash別copyに保全した。同じ内容の複数パスもbaselineで個別に追跡する。追加文書は[計画145](145_post_rejection_next_plan.md)と[更新記録146](146_documentation_followup.md)。",'',
        '[今回baseline](../reports/investigation/documentation-followup-20261014/baseline.json) / [今回の更新原文copy](../reports/investigation/documentation-followup-20261014/originals/)。過去copyは当時の文書で、コピー先のrelative linkを現在の実行指示として使わない。','']
    names=sorted({r['path'] for r in b['documents']}|NEW)
    for kind,title in (('current','現行文書・計画'),('dated_or_frozen_history','日付付き結果・固定履歴'),('provenance_copy','以前から保全した原文copy')):
        lines+=['## '+title,'','| 文書 | 扱い |','|---|---|']
        for name in names:
            if category(name)!=kind:continue
            label=name.replace('|','\\|')
            href='../'+name if not name.startswith('docs/') else name[5:]
            lines.append(f'| [{label}]({href}) | '+('今回最新化' if kind=='current' else '原文保全')+' |')
        lines+=['']
    lines+=['## 今回追加した内容hash別の原文copy','',
        'baselineのsnapshot列は各元パスを以下のcopyへ対応付ける。これらは研究文書を増やした件数ではなく、更新前bytesの保全。','',
        '| 内容hash別copy |','|---|']
    for path in sorted((RUN/'originals').glob('*')):
        lines.append(f'| [{path.name}](../{path.relative_to(WIN).as_posix()}) |')
    p=WIN/'docs/document_catalog.md'
    p.write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n');mirror(p)
    print(json.dumps(dict(catalog_entries=len(names),new_preservation_copy_paths=b['unique_original_copies'])))


def verify(commit=None,receipt_commit=None):
    b=read(RUN/'baseline.json')
    changed=[]
    for r in b['documents']:
        p=WIN/r['path']; backup=WIN/r['snapshot']
        assert sha(backup)==sha(WSL/r['snapshot'])==r['sha256'],r['path']
        if r['path'] not in LIVING:assert sha(p)==r['sha256'],r['path']
        else:
            assert sha(p)!=r['sha256'],('Current document must be updated',r['path'])
            changed.append(r['path'])
    for name,digest in b['preserved_scientific_and_frozen_sources'].items():
        assert sha(WIN/name)==sha(WSL/name)==digest,name
    c=read(WIN/'reports/phase6/base_document_balance_comparison_completion.json')
    assert c['fixed_condition_closed'] and not c['Base_adopted'] and not c['all_six_stages_actually_executed']
    assert all(not r['executed'] and not r['passed'] for r in c['qualified_only_branches'].values())
    for name in sorted(LIVING|NEW):
        body=(WIN/name).read_text(encoding='utf-8-sig')
        assert '144' in body and (name=='docs/145_post_rejection_next_plan.md' or '145' in body),('Latest evidence/plan missing',name)
    plan=(WIN/'docs/145_post_rejection_next_plan.md').read_text()
    assert all(word in plan for word in ('9.5M','10.1M','10,001,152','CPU','seed43','400生成','長文40','95%','未選定','未凍結','別artifact','総予算'))
    for name in ('eval/README.md','docs/evaluation_protocol.md','docs/autonomous_status.md'):
        body=(WIN/name).read_text()
        assert 'Base TEST20' in body and 'Chat TEST20' in body and 'CPU' in body and '封印TEST' in body,name
    cat=(WIN/'docs/document_catalog.md').read_text()
    catalog_paths=set()
    for href in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',cat):
        target=href.strip('<>').split('#',1)[0]
        if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
        dest=(WIN/'docs'/unquote(target)).resolve()
        if dest.is_relative_to(WIN.resolve()):catalog_paths.add(dest.relative_to(WIN).as_posix())
    expected_paths={r['path'] for r in b['documents']}|NEW|{p.relative_to(WIN).as_posix() for p in (RUN/'originals').glob('*')}
    assert expected_paths<=catalog_paths,sorted(expected_paths-catalog_paths)
    allowed=LIVING|NEW|{'.gitattributes','scripts/documentation_followup_20261014.py','scripts/write_documentation_followup_20261014.py'}
    run_prefix=RUN.relative_to(WIN).as_posix()+'/'
    for name in git('diff','--name-only',b['initial_commit']).splitlines():
        assert name in allowed or name.startswith(run_prefix),('Unexpected tracked change',name)
    for name in git('ls-files','--others','--exclude-standard').splitlines():
        assert name in allowed or name.startswith(run_prefix),('Unexpected untracked change',name)
    link_count=inbound_count=0
    for name in sorted(LIVING|NEW):
        p=WIN/name
        assert sha(p)==sha(WSL/name),name
        body=p.read_text(encoding='utf-8-sig')
        assert '\x00' not in body and '\ufffd' not in body,name
        for href in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',body):
            target,_,fragment=href.strip('<>').partition('#')
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
            dest=(p.parent/unquote(target)).resolve() if target else p
            assert dest.exists(),(name,href)
            if fragment:assert unquote(fragment) in anchors(dest),(name,href)
            link_count+=1
    for r in b['documents']:
        if r['category']=='provenance_copy':continue
        p=WIN/r['path']
        for href in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',p.read_text(encoding='utf-8-sig')):
            target,_,fragment=href.strip('<>').partition('#')
            if not fragment or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
            dest=(p.parent/unquote(target)).resolve() if target else p
            if not dest.is_relative_to(WIN.resolve()):continue
            if dest.relative_to(WIN).as_posix() not in LIVING|NEW:continue
            assert dest.exists() and unquote(fragment) in anchors(dest),(r['path'],href)
            inbound_count+=1
    proof=dict(passed=True,verified_at=now(),all_initial_document_paths=b['all_document_paths'],
        existing_living_documents_updated=len(changed),dated_and_provenance_paths_unchanged=b['all_document_paths']-len(changed),
        additional_source_documents=len(NEW),original_copies_verified=b['unique_original_copies'],
        all_catalog_entries_verified=True,catalog_actual_document_target_paths=len(expected_paths),
        only_authorized_documentation_changes=True,current_Windows_WSL_match=True,
        current_local_file_and_heading_links_checked=link_count,historical_incoming_heading_links_checked=inbound_count,
        original_scientific_reports_and_sources_unchanged=True,source_sha256=sha(Path(__file__)),
        research_resumed=False,GPU_work=False,dataset_TEST_parsed=False,
        Base_complete=False,Chat_complete=False,push_executed=False)
    destination=RUN/'verification.json'
    if commit:
        revision=git('rev-parse',commit+'^{commit}')
        assert not git('status','--porcelain')
        paths=git('diff','--name-only',b['initial_commit'],revision).splitlines()
        for name in paths:
            if receipt_commit and name==(RUN/'commit_verification.json').relative_to(WIN).as_posix():continue
            assert git('rev-parse',revision+':'+name)==git('hash-object','--path='+name,WIN_GIT+'\\'+name.replace('/','\\')),name
        proof.update(result_commit=revision,committed_scope_objects_verified=len(paths))
        destination=RUN/'commit_verification.json'
        if receipt_commit:
            receipt=git('rev-parse',receipt_commit+'^{commit}')
            assert git('rev-parse','HEAD')==receipt
            old=read(destination)
            assert old['passed'] and old['result_commit']==revision and old['source_sha256']==sha(Path(__file__))
            name=destination.relative_to(WIN).as_posix()
            assert sha(destination)==sha(WSL/name)
            assert git('rev-parse',receipt+':'+name)==git('hash-object','--path='+name,WIN_GIT+'\\'+name.replace('/','\\'))
            proof.update(receipt_commit=receipt,documentation_and_plan_delivery_complete=True)
            print(json.dumps(proof));return
    save(destination,proof);mirror(destination)
    print(json.dumps(proof))


if __name__=='__main__':
    assert sys.version_info[:3]==(3,12,7),'Pinned uv Python required'
    p=argparse.ArgumentParser();p.add_argument('mode',choices=('snapshot','catalog','verify'))
    p.add_argument('--commit');p.add_argument('--receipt-commit');a=p.parse_args()
    if a.mode=='snapshot':snapshot()
    elif a.mode=='catalog':catalog()
    else:verify(a.commit,a.receipt_commit)
